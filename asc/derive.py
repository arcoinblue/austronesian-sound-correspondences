"""From the validated data to what the site shows: edges, ancestry, descent, lect records.

The site loads one small file per lect (its record and inventory) and, when a
phoneme is opened, one file per phoneme (its notation, ancestry and descent).
"""
from __future__ import annotations

import re
from collections import defaultdict

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


def descendants(phoneme_id, D, path=(), depth=0, beyond=False, seen=None):
    """Flattened downward rows, each with the path of intermediate phonemes.

    A row into a competing reconstruction is marked 'competing'. Rows below
    one are marked 'beyond_competing': they belong on that reconstruction's own
    pages and are left out of the ancestor's reflex list.

    Each intermediate phoneme is descended into once. Several rows can reach the
    same one (three sources giving *R > Proto-Bunun *l; two phonemes merging);
    its own rows are listed under the first path only, not once per row."""
    out = []
    if depth > 50:
        return out
    if seen is None:
        seen = set()
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
        below = beyond or row.get("competing", False)
        if r["child_phoneme_id"] and (r["child_phoneme_id"], below) not in seen:
            seen.add((r["child_phoneme_id"], below))
            out.extend(descendants(r["child_phoneme_id"], D, path + (r["child_phoneme_id"],), depth + 1,
                                   below, seen))
    return out


def alt_descendants(phoneme_id, L, D):
    """Rows of the lects that another classification puts under L (lects.alt_parents),
    for the phoneme phoneme_id of L.

    Such a lect hangs from its own parent Q in the tree, and its rows are stated
    against Q. Where Q is an ancestor of L, a row is listed under the phoneme of L
    that its Q phoneme becomes on the way down to L: PAn *j and *n both become
    Proto-East Formosan *n, so Kavalan's rows for PAn *j and *n are listed under
    PEF *n. Each row gets 'alt_via' (the Q phoneme and the path to L) and
    'alt_source' (the work that proposes the classification)."""
    out = []
    chain = lect_chain(L, D["lects"])
    for A, a_rec in D["lects"].items():
        for a in a_rec["alt_parent_list"]:
            if a["parent_id"] != L:
                continue
            Q = a_rec["parent_id"]
            if not Q or Q not in chain:
                continue
            stages = set(chain[chain.index(Q) + 1:]) | {L}
            for q in D["inventory"].get(Q, {}).values():
                paths = _paths_into(q["id"], phoneme_id, stages, D)
                if not paths:
                    continue
                for r in D["by_parent"].get(q["id"], []):
                    if r["child_lect_id"] != A:
                        continue
                    row = edge(r)
                    row["alt_via"] = paths[0]
                    row["alt_source"] = a["source_id"]
                    out.append(row)
    return out


def _paths_into(start, target, stages, D, depth=0):
    """Paths of phoneme ids from start down to target through the lects in stages."""
    if depth > 20:
        return []
    found = []
    for r in D["by_parent"].get(start, []):
        if r["child_lect_id"] not in stages or not r["child_phoneme_id"]:
            continue
        if r["child_phoneme_id"] == target:
            found.append([start, target])
        else:
            found += [[start] + p for p in _paths_into(r["child_phoneme_id"], target, stages, D, depth + 1)]
    # One path per route, shortest first.
    uniq = []
    for p in sorted(found, key=len):
        if p not in uniq:
            uniq.append(p)
    return uniq


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


def lect_full(L, D):
    """Everything about a lect, with each phoneme's ancestry and descent (as one record)."""
    rec = D["lects"][L]
    inv = D["inventory"][L]
    status = D["inv_status"][L]
    cov = coverage(L, D)
    index_status = data_status(L, D)
    used_sources = sorted({p["source_id"] for p in inv.values() if p["source_id"]})
    corr_sources = sorted({r["source_id"] for r in D["corrs"] if r["child_lect_id"] == L})
    has_alt = any(a["parent_id"] == L for v in D["lects"].values() for a in v["alt_parent_list"])
    phonemes = []
    for s, ph in inv.items():
        ph = dict(ph)
        ph["notation"] = D["notation"].get(ph["id"], [])
        ph["ancestry_graph"] = ancestry_graph(ph["id"], D)
        ph["descendants"] = descendants(ph["id"], D)
        ph["alt_descendants"] = alt_descendants(ph["id"], L, D) if has_alt else []
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
        "daughters": sorted(k for k, v in D["lects"].items() if v["parent_id"] == L and not v["node_only"]),
        # Where the lect list draws it, when that is not parent_id: a group (linkage), a
        # language (for a dialect) or a dialect (for a sub-dialect).
        "tree_parent": rec["tree_parent_id"] if rec["tree_parent_id"] != rec["parent_id"] else None,
        # A tree node with no page (a group; a language with no rows of its own).
        "node_only": rec["node_only"],
        "representative": rec["representative"] or None,
        # The language this lect is the representative dialect of (Duhtu for Tsou).
        "represents": next((k for k, v in D["lects"].items() if v["representative"] == L), None),
        "coordinates": rec["coordinates"],
        # A sourced inventory is the inventory, whatever inherit says: the page shows no
        # "changes only" notice for it.
        "changes_only": rec["changes_only_flag"] and status != "sourced",
        # What a parent phoneme with no row does here, and where the source says so.
        "inherit": rec["inherit"] or None,
        "inherit_auto": bool(rec.get("inherit_auto")) or None,
        "inherit_source_id": rec["inherit_source_id"] or None,
        "inherit_page": rec["inherit_page"] or None,
        "language_id": rec["language_id"] or None,
        "dialects": sorted(k for k, v in D["lects"].items()
                           if v["type"] == "dialect" and (v["language_id"] == L or v["tree_parent_id"] == L)),
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


# Kept on the phoneme's own file, not on the lect's: the lect page does not need them.
PHONEME_DETAIL = ("notation", "ancestry_graph", "descendants", "alt_descendants")
SYSTEM_DETAIL = ("rows", "descendants")


def phoneme_file(L, sym, system=None):
    """'pan/0052.json' for PAn *R, 'pan/0044@Ross.json' for Ross's *D. Code points, not the
    symbol itself: the names are plain ASCII and *R and *r differ on any file system."""
    key = "-".join(f"{ord(c):04x}" for c in sym)
    if system:
        key += "@" + re.sub(r"[^A-Za-z0-9]+", "-", system)
    return f"{L}/{key}.json"


def lect_files(L, D):
    """The lect's own file, and {path: record} for its phonemes' files.

    Each default phoneme's file has its notation, ancestry graph and descent, and the
    full records (sources, descent) of the other systems' phonemes that match it. A
    system phoneme with no counterpart in the default inventory has a file of its own."""
    full = lect_full(L, D)
    files, matching, systems = {}, defaultdict(list), []
    for sysrec in full["systems"]:
        out = []
        for sp in sysrec["phonemes"]:
            for c in sp["counterparts"]:
                matching[c].append(sp)
            short = {k: v for k, v in sp.items() if k not in SYSTEM_DETAIL}
            if not sp["counterparts"]:
                short["file"] = phoneme_file(L, sp["ipa"], sysrec["name"])
                files[short["file"]] = sp
            out.append(short)
        systems.append({**sysrec, "phonemes": out})
    phonemes = []
    for ph in full["phonemes"]:
        short = {k: v for k, v in ph.items() if k not in PHONEME_DETAIL}
        short["file"] = phoneme_file(L, ph["ipa"])
        files[short["file"]] = {"id": ph["id"], **{k: ph[k] for k in PHONEME_DETAIL},
                                "system_phonemes": matching.get(ph["id"], [])}
        phonemes.append(short)
    return {**full, "phonemes": phonemes, "systems": systems}, files


def lect_json(L, D):
    """The lect's own file: its record and inventory, without the phonemes' history."""
    return lect_files(L, D)[0]


# What the lect list needs of each lect (it is loaded on every page, so nothing more,
# and empty values are left out). The full record is in the lect's own file.
INDEX_FIELDS = ("id", "name", "alt_names", "type", "glottocode", "parent_id", "clade", "coverage", "index_status",
                "tree_parent", "node_only", "representative")


def index_json(D, lect_records=None):
    rows = []
    for L in D["lects"]:
        j = (lect_records or {}).get(L) or lect_json(L, D)
        row = {k: j[k] for k in INDEX_FIELDS if j[k] not in (None, "", [], False)}
        row["id"], row["name"] = j["id"], j["name"]
        groups = [g["name"] for g in j["overlap_groups"]]
        if groups:
            row["overlap_groups"] = groups
        # Other classifications: the lect tree also lists the lect under these nodes.
        if j["alt_parents"]:
            row["alt_parents"] = [{"parent_id": a["parent_id"], "source_id": a["source_id"]} for a in j["alt_parents"]]
        rows.append(row)
    return {"lects": rows}


def sources_json(D):
    return {"sources": [{k: v for k, v in s.items() if not k.startswith("_")}
                        for s in D["sources"].values()]}
