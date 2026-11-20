"""From the validated data to what the site shows: edges, ancestry, descent, lect records."""
from __future__ import annotations

from .schema import *  # noqa: F401,F403

def edge(r, include_child=True):
    e = {
        "correspondence_id": r["id"],
        "parent": r["parent_phoneme_id"],
        "environment": r["environment"],
        "status": r["status"] or None,
        "blank_type": r["blank_type"] or None,
        "evidence_count": int(r["evidence_count"]) if r["evidence_count"].isdigit() else None,
        "source_id": r["source_id"],
        "page": r["page"],
        "notes": r["notes"],
        "fusion": r.get("fusion"),
        "system": r.get("system") or None,
        "via_source_id": r.get("via_source_id", ""), "via_page": r.get("via_page", ""),
        "via_note": r.get("via_note", ""),
        **{k: r.get(k, "") for k in ("conditioning", "variety", "stratum", "lexical_scope", "examples", "source_form",
                                    "as_printed", "locator", "decision")},
        "evidence_total": int(r["evidence_total"]) if r.get("evidence_total", "").isdigit() else None,
        "derivation": r.get("derivation") or "as-stated",
    }
    if include_child:
        e["child_lect_id"] = r["child_lect_id"]
        e["child"] = r["child_phoneme_id"]
    # Empty fields are left out: the files list thousands of rows.
    return {k: v for k, v in e.items()
            if not (v is None or v is False or v == "" or (k == "derivation" and v == "as-stated"))
            or k in ("parent", "child")}


def ancestry(phoneme_id, D, depth=0):
    """All upward chains, oldest first. Each chain is a list of edges.

    A fused cluster gives one chain, not two, and the chain starts at the
    cluster: its edge has parent None and fusion.members naming both segments.
    """
    if depth > 50:
        return [[]]
    rows = D["by_child"].get(phoneme_id, [])
    if not rows:
        return [[]]
    chains = []
    for r in rows:
        if r.get("fusion"):
            if r["fusion"]["role"] == "second":
                e = edge(r)
                e["parent"] = None
                e["environment"] = "fusion"
                chains.append([e])
            continue
        for up in ancestry(r["parent_phoneme_id"], D, depth + 1):
            chains.append(up + [edge(r)])
    return chains


def ancestry_graph(phoneme_id, D):
    """The ancestry as one graph: every ancestor phoneme once, however many
    lines of descent pass through it, and one edge per correspondence row.
    Both rows of a fusion are edges, so the two members converge on the reflex."""
    nodes, edges, seen, todo = [phoneme_id], [], set(), [phoneme_id]
    while todo:
        cur = todo.pop()
        for r in D["by_child"].get(cur, []):
            if r["id"] in seen:
                continue
            seen.add(r["id"])
            edges.append(edge(r))
            parent = r["parent_phoneme_id"]
            if parent not in nodes:
                nodes.append(parent)
                todo.append(parent)
    return {"nodes": nodes, "edges": edges}


def descendants(phoneme_id, D, path=(), depth=0, beyond=False):
    """Flattened downward rows, each with the path of intermediate phonemes.

    A row into a competing reconstruction is marked 'competing'. Rows below
    one are marked 'beyond_competing': they belong on that reconstruction's own
    pages and are left out of the ancestor's reflex list."""
    out = []
    if depth > 50:
        return out
    for r in D["by_parent"].get(phoneme_id, []):
        row = edge(r)
        row["via"] = list(path)
        # Beyond the first level, a row is shown by default only where sources
        # or reconstructions disagree about this stage.
        row["conflict"] = (r["child_lect_id"], r["parent_phoneme_id"]) in D["conflicts"]
        if r["child_lect_id"] in D["competing"]:
            row["competing"] = True
        if beyond:
            row["beyond_competing"] = True
        # An implied retention is listed one level down only; deeper, it would
        # repeat the same "unchanged" for every node of an assumed-unchanged tree.
        if not (path and row.get("derivation") == "implied-retention"):
            out.append(row)
        if r["child_phoneme_id"]:
            out.extend(descendants(r["child_phoneme_id"], D, path + (r["child_phoneme_id"],), depth + 1,
                                   beyond or row.get("competing", False)))
    return out


def lect_chain(L, lects):
    chain, cur = [], lects[L]["parent_id"]
    while cur and cur in lects and cur not in chain:
        chain.append(cur)
        cur = lects[cur]["parent_id"]
    return list(reversed(chain))


def coverage(L, D):
    """How much of the parent's inventory has an outcome in L.

    stated: parent phonemes with a row from the source (or composed from its rows);
    implied: retentions the build added for an assumed-unchanged source;
    parent_size: the parent's inventory. None for a root."""
    P = D["lects"][L]["parent_id"]
    if not P or P not in D["inventory"]:
        return None
    par = D["inventory"][P]
    stated = D["entered_pairs"].get(L, set()) & set(par)
    implied = {r["parent_phoneme"] for r in D["corrs"]
               if r["child_lect_id"] == L and r["derivation"] == "implied-retention"} - stated
    return {"stated": len(stated), "implied": len(implied), "parent_size": len(par)}


def data_status(L, D):
    """What the lect page and the index say about the data behind a lect."""
    rows = [r for r in D["corrs"] if r["child_lect_id"] == L]
    if D["inv_status"][L] == "sourced":
        return "sourced"
    if D["lects"][L]["changes_only_flag"]:
        return "changes-only"
    if not rows and D["lects"][L]["parent_id"]:
        return "empty"
    return "generated"


def lect_json(L, D):
    rec = D["lects"][L]
    inv = D["inventory"][L]
    status = D["inv_status"][L]
    cov = coverage(L, D)
    index_status = data_status(L, D)
    used_sources = sorted({p["source_id"] for p in inv.values() if p["source_id"]})
    corr_sources = sorted({r["source_id"] for r in D["corrs"] if r["child_lect_id"] == L})
    phonemes = []
    for s, ph in inv.items():
        ph = dict(ph)
        ph["notation"] = D["notation"].get(ph["id"], [])
        ph["ancestry_graph"] = ancestry_graph(ph["id"], D)
        ph["descendants"] = descendants(ph["id"], D)
        phonemes.append(ph)
    default = rec["default_system"]
    systems = []
    found = D["sysph"].get(L, {})
    order = [S for S in rec["systems_list"] if S in found] + [S for S in found if S not in rec["systems_list"]]
    for S in order:
        phs = found[S]
        out = []
        for sp in phs.values():
            sp = dict(sp)
            sp["descendants"] = descendants(sp["id"], D)   # empty: descent is the default phoneme's
            # A page of its own only where the descent differs (it has reflex
            # rows of its own) or nothing in the default inventory matches it.
            # Otherwise it is a spelling or phonetic value, explained on the default page.
            sp["separate"] = bool(sp["descendants"]) or not sp["counterparts"]
            out.append(sp)
        systems.append({"name": S, "phonemes": out})
    return {
        "id": L,
        "name": rec["name"],
        "alt_names": rec["alt_names_list"],
        "type": rec["type"],
        "glottocode": rec["glottocode"] or None,
        "iso639_3": rec["iso639_3"] or None,
        "parent_id": rec["parent_id"] or None,
        "ancestors": lect_chain(L, D["lects"]),
        "subgroup_path": rec["subgroup_list"],
        "clade": rec["clade_label"],
        "competes_with": sorted(set(rec["competes_list"]) | {k for k, v in D["lects"].items() if L in v["competes_list"]}),
        "region": rec["region"],
        "orthography_note": rec["orthography_note"],
        "notes": rec["notes"],
        "default_system": default or None,
        # The first tab is named after the default system, or failing that the inventory's source.
        "default_label": default or ", ".join(D["sources"][x]["label"] for x in used_sources
                                              if x in D["sources"]) or "Inventory",
        # Tab order as listed in lects.systems; the default goes first unless listed elsewhere.
        "tab_order": ([S for S in rec["systems_list"] if S == default or S in found]
                      if default in rec["systems_list"] else [default or ""] + order),
        "systems": systems,
        "inventory_status": status,
        "index_status": index_status,
        "coverage": cov,
        "inventory_sources": used_sources,
        "correspondence_sources": corr_sources,
        "phonemes": phonemes,
        "inventory_diff": [
            {"op": "add", "ipa": p["ipa"], "reason": p["reason"], "source_id": p["source_id"]}
            for p in inv.values() if p["origin"] == "manual-add"
        ] + [
            {"op": "place", "ipa": p["ipa"], "reason": p["reason"], "source_id": p["source_id"]}
            for p in inv.values() if p["origin"] == "generated" and p["placement"] == "hand"
        ] + [
            {"op": "suppress", "ipa": p["ipa"], "reason": p["reason"], "source_id": p["source_id"]}
            for p in rec.get("_suppressed", [])
        ],
        "daughters": sorted(k for k, v in D["lects"].items() if v["parent_id"] == L),
        "coordinates": rec["coordinates"],
        "changes_only": rec["changes_only_flag"],
        # What a parent phoneme with no row does here, and where the source says so.
        "inherit": rec["inherit"] or None,
        "inherit_source_id": rec["inherit_source_id"] or None,
        "inherit_page": rec["inherit_page"] or None,
        "language_id": rec["language_id"] or None,
        "dialects": sorted(k for k, v in D["lects"].items() if v["language_id"] == L and v["type"] == "dialect"),
        "alt_parents": rec["alt_parent_list"],
        "alt_daughters": sorted(({"lect_id": k, "source_id": a["source_id"]} for k, v in D["lects"].items()
                                 for a in v["alt_parent_list"] if a["parent_id"] == L), key=lambda x: x["lect_id"]),
        # The rows into this lect as the source states them: the changes that define it.
        "changes": [edge(r) for r in D["corrs"] if r["child_lect_id"] == L
                    and r["derivation"] not in ("implied-retention", "stated-retention")
                    and (r["child_phoneme"] != r["parent_phoneme"] or r["environment"] != "elsewhere")],
        # Each overlapping subgroup with its other members.
        "overlap_groups": [{"name": g, "members": [m for m in D["overlap"][g] if m != L]} for g in rec["overlap_list"]],
        # Sounds inserted in the daughters: they have no phoneme here to descend from.
        "insertions": [edge(r) for r in D["by_parent"].get(pid(L, ZERO), [])],
    }


def index_json(D):
    rows = []
    for L in D["lects"]:
        j = lect_json(L, D)
        rows.append({k: j[k] for k in ("id", "name", "alt_names", "type", "glottocode",
                                        "parent_id", "subgroup_path", "clade", "competes_with", "coverage", "index_status",
                                        "coordinates", "language_id", "changes_only", "inherit")})
        rows[-1]["overlap_groups"] = [g["name"] for g in j["overlap_groups"]]
    return {"lects": rows}


def sources_json(D):
    return {"sources": [{k: v for k, v in s.items() if not k.startswith("_")}
                        for s in D["sources"].values()]}
