"""Checks every table and resolves inventories, retentions, notation and systems."""
from __future__ import annotations

import hashlib
import re
from collections import Counter, defaultdict
from urllib.parse import quote

from .schema import *  # noqa: F401,F403
from .schema import _c, _v  # noqa: F401
from .cite import citation_label, reference, cited_works
from .load import Report

def validate_and_derive(t, rep: Report):
    sources = {}
    for r in t["sources"]:
        w = r["_where"]
        if not ID_RE.match(r["id"]):
            rep.error(w, f"source id {r['id']!r} must be lowercase [a-z0-9_-]")
        if r["id"] in sources:
            rep.error(w, f"duplicate source id {r['id']!r}")
        for col in ("author", "year", "title", "kind"):
            if not r[col]:
                rep.error(w, f"'{col}' is required")
        if r["kind"] and r["kind"] not in SOURCE_KINDS:
            rep.error(w, f"kind {r['kind']!r} not in {sorted(SOURCE_KINDS)}")
        if r["year_suffix"] and not re.fullmatch(r"[a-z]", r["year_suffix"]):
            rep.error(w, f"year_suffix {r['year_suffix']!r} must be one lowercase letter (the b of 1999b)")
        if r["pub_type"] and r["pub_type"] not in PUB_TYPES:
            rep.error(w, f"pub_type {r['pub_type']!r} not in {sorted(PUB_TYPES)}")
        if r["pub_type"] in ("article", "chapter") and not r["container_title"]:
            rep.warn(w, f"pub_type {r['pub_type']} needs a container_title (the journal or the volume)")
        r["label"] = citation_label(r["author"], r["year"], r["year_suffix"])
        r["reference"] = reference(r)
        sources[r["id"]] = r

    decisions = {}
    for r in t.get("decisions", []):
        w = r["_where"]
        if not ID_RE.match(r["id"]):
            rep.error(w, f"decision id {r['id']!r} must be lowercase [a-z0-9_-]")
        elif r["id"] in decisions:
            rep.error(w, f"duplicate decision id {r['id']!r}")
        if not r["question"]:
            rep.error(w, "'question' is required")
        if r["status"] not in DECISION_STATUS:
            rep.error(w, f"status {r['status']!r} must be one of {sorted(DECISION_STATUS)}")
        if r["source_id"] and r["source_id"] not in sources:
            rep.error(w, f"source_id {r['source_id']!r} is not in sources.csv")
        r["rows"] = []
        decisions[r["id"]] = r

    def check_via(w, r):
        """An indirect citation: source_id is the original, via_* the work it was read in."""
        if r["via_source_id"]:
            if r["via_source_id"] not in sources:
                rep.error(w, f"via_source_id {r['via_source_id']!r} is not in sources.csv")
            elif r["via_source_id"] == r["source_id"]:
                rep.warn(w, "via_source_id is the same as source_id; leave it blank for a direct citation")
        elif r["via_page"] or r["via_note"]:
            rep.error(w, "via_page / via_note need a via_source_id")

    def via_of(r):
        return {"via_source_id": r.get("via_source_id", ""), "via_page": r.get("via_page", ""),
                "via_note": r.get("via_note", "")}

    def check_source(w, sid, required=True):
        if not sid:
            if required:
                rep.error(w, "source_id is required")
            return
        if sid not in sources:
            rep.error(w, f"source_id {sid!r} is not in sources.csv (add the citation first)")

    # --- lects
    lects = {}
    for r in t["lects"]:
        w = r["_where"]
        if not ID_RE.match(r["id"]):
            rep.error(w, f"lect id {r['id']!r} must be lowercase [a-z0-9_-]")
        if r["id"] in lects:
            rep.error(w, f"duplicate lect id {r['id']!r}")
        if not r["name"]:
            rep.error(w, "name is required")
        if r["type"] not in LECT_TYPES:
            rep.error(w, f"type {r['type']!r} not in {sorted(LECT_TYPES)}")
        if r["glottocode"]:
            if not GLOTTOCODE_RE.match(r["glottocode"]):
                rep.error(w, f"glottocode {r['glottocode']!r} is malformed")
            elif r["id"] != r["glottocode"] and r["type"] not in RECONSTRUCTED:
                rep.warn(w, f"lect id should be its Glottocode ({r['glottocode']})")
        elif r["type"] not in RECONSTRUCTED:
            rep.warn(w, "no glottocode")
        if r["iso639_3"] and not ISO_RE.match(r["iso639_3"]):
            rep.error(w, f"iso639_3 {r['iso639_3']!r} is malformed")
        r["alt_names_list"] = [a.strip() for a in r["alt_names"].split(";") if a.strip()]
        r["subgroup_list"] = [a.strip() for a in r["subgroup_path"].split(">") if a.strip()]
        # Reconstruction systems, in tab order. Blank: every system in
        # notation_map counts as one. Listed: the others are spellings only.
        r["systems_list"] = [a.strip() for a in r["systems"].split(";") if a.strip()]
        # Names: Proto-X for a proto-language (with the hyphen, whatever the source writes), Pre-X for an earlier stage.
        if r["type"] == "proto-language" and not re.match(r"Proto-\S", r["name"]):
            rep.warn(w, f"proto-language name {r['name']!r} should have the form Proto-X")
        elif r["type"] == "earlier-stage" and not re.match(r"Pre-\S", r["name"]):
            rep.warn(w, f"earlier-stage name {r['name']!r} should have the form Pre-X")
        elif r["type"] in ("language", "dialect") and re.match(r"(Proto|Pre)[- ]", r["name"]):
            rep.warn(w, f"{r['name']!r} looks reconstructed but its type is {r['type']}; "
                        "use proto-language (Proto-X) or earlier-stage (Pre-X)")
        # The group a proto-language is the ancestor of: 'clade', or the name without Proto-.
        # An earlier stage of one language heads no group.
        r["clade_label"] = r["clade"] or (re.sub(r"^Proto-", "", r["name"]) if r["type"] == "proto-language" else "")
        if r["clade"] and r["type"] != "proto-language":
            rep.warn(w, "clade is for proto-languages; ignored here")
            r["clade_label"] = ""
        # Where the lect is spoken, in decimal degrees (south and west negative).
        r["coordinates"] = None
        if r["latitude"] or r["longitude"]:
            try:
                lat, lon = float(r["latitude"]), float(r["longitude"])
                if not (-90 <= lat <= 90 and -180 <= lon <= 180):
                    raise ValueError
                r["coordinates"] = [lat, lon]
            except ValueError:
                rep.error(w, f"latitude {r['latitude']!r} and longitude {r['longitude']!r} must both be decimal "
                             "degrees, within -90..90 and -180..180")
        # A source that lists only the changes into this lect: everything else is retained.
        if r["inherit"] and r["inherit"] not in INHERIT:
            rep.error(w, f"inherit {r['inherit']!r} must be blank or one of {sorted(INHERIT)}")
            r["inherit"] = ""
        if not r["inherit"] and (r["inherit_source_id"] or r["inherit_page"] or r["inherit_note"]):
            rep.warn(w, "inherit_source_id / inherit_page / inherit_note apply only when inherit is set; ignored")
        if r["inherit_source_id"] and r["inherit_source_id"] not in sources:
            rep.error(w, f"inherit_source_id {r['inherit_source_id']!r} is not in sources.csv")
        if r["inherit"] == "stated-unchanged" and not (r["inherit_source_id"] and r["inherit_page"]):
            rep.warn(w, "stated-unchanged: give inherit_source_id and inherit_page (where the source says so)")
        r["changes_only_flag"] = r["inherit"] == "assumed-unchanged"
        # Other classifications: 'pef:chen2022; ...' (parent id, the source that proposes it).
        r["alt_parent_list"] = []
        for item in (a.strip() for a in r["alt_parents"].split(";") if a.strip()):
            par, _, src = item.partition(":")
            r["alt_parent_list"].append({"parent_id": par.strip(), "source_id": src.strip()})
        # Subgroups that cut across the tree (a lect can be in several): names only, not nodes.
        r["overlap_list"] = [a.strip() for a in r["overlap_groups"].split(";") if a.strip()]
        if CANONICAL in r["systems_list"]:
            rep.error(w, f"'{CANONICAL}' is a spelling, not a reconstruction system; remove it from systems")
        lects[r["id"]] = r

    for r in lects.values():
        w = r["_where"]
        p = r["parent_id"]
        if p:
            if p not in lects:
                rep.error(w, f"parent_id {p!r} is not a lect")
            elif lects[p]["type"] not in RECONSTRUCTED:
                rep.error(w, f"parent_id {p!r} is a {lects[p]['type']}, must be a proto-language or an earlier-stage")
        elif r["type"] not in RECONSTRUCTED:
            rep.warn(w, "attested lect with no parent_id: nothing can be stated about its history")
        for a in r["alt_parent_list"]:
            if a["parent_id"] not in lects:
                rep.error(w, f"alt_parents names {a['parent_id']!r}, which is not a lect")
            elif lects[a["parent_id"]]["type"] not in RECONSTRUCTED:
                rep.error(w, f"alt_parents {a['parent_id']!r} is a {lects[a['parent_id']]['type']}, must be reconstructed")
            elif a["parent_id"] == p:
                rep.warn(w, f"alt_parents repeats parent_id {p!r}")
            if not a["source_id"]:
                rep.error(w, f"alt_parents {a['parent_id']!r} needs the source that proposes it ('{a['parent_id']}:source_id')")
            elif a["source_id"] not in sources:
                rep.error(w, f"alt_parents source {a['source_id']!r} is not in sources.csv")
        if r["language_id"]:
            if r["type"] != "dialect":
                rep.warn(w, "language_id is for dialects; ignored")
            elif r["language_id"] not in lects:
                rep.error(w, f"language_id {r['language_id']!r} is not a lect")
            elif lects[r["language_id"]]["type"] != "language":
                rep.error(w, f"language_id {r['language_id']!r} is a {lects[r['language_id']]['type']}, must be a language")
        # Competing reconstructions of the same node: both are listed under the
        # parent, and nothing below either of them is.
        r["competes_list"] = [a.strip() for a in r["competes_with"].split(";") if a.strip()]
        for c in r["competes_list"]:
            if c not in lects:
                rep.error(w, f"competes_with {c!r} is not a lect")
            elif c == r["id"]:
                rep.error(w, "a lect cannot compete with itself")
            elif lects[c]["parent_id"] != p:
                rep.warn(w, f"competes_with {c!r} has a different parent_id; competing reconstructions "
                            "should stand under the same parent")
        # cycle check
        seen, cur = {r["id"]}, p
        while cur and cur in lects:
            if cur in seen:
                rep.error(w, f"parent_id chain loops back to {cur!r}")
                break
            seen.add(cur)
            cur = lects[cur]["parent_id"]

    # subgroup_path: derived from the parent chain (each ancestor's clade, root first).
    # A filled cell overrides it, for the few lects the tree cannot say (the root,
    # a group without a proto node, a member whose node is not entered).
    same_as_derived = []
    for r in lects.values():
        derived, seen, cur = [], {r["id"]}, r["parent_id"]
        while cur and cur in lects and cur not in seen:
            seen.add(cur)
            if lects[cur]["clade_label"]:
                derived.append(lects[cur]["clade_label"])
            cur = lects[cur]["parent_id"]
        r["derived_subgroup"] = derived[::-1]
        if not r["subgroup_list"]:
            r["subgroup_list"] = r["derived_subgroup"]
        elif r["subgroup_list"] == r["derived_subgroup"]:
            same_as_derived.append(r["id"])
    if same_as_derived:
        rep.note("lects.csv", f"{len(same_as_derived)} lect(s) have a subgroup_path equal to the one derived "
                              "from parent_id and clade; it can be left blank")

    # --- entered phonemes
    entered = defaultdict(dict)  # lect -> sym -> row
    for r in t["phonemes"]:
        w = r["_where"]
        L, s = r["lect_id"], r["ipa"]
        if L not in lects:
            rep.error(w, f"lect_id {L!r} is not in lects.csv")
            continue
        if not s:
            rep.error(w, "ipa is required")
            continue
        if s in entered[L]:
            rep.error(w, f"duplicate phoneme {L}:{s}")
        if r["class"] not in PHONEME_CLASSES and not (r["origin"] == "override" and not r["class"]):
            rep.error(w, f"class {r['class']!r} not in {sorted(PHONEME_CLASSES)}")
        if r["origin"] not in PHONEME_ORIGINS_ENTERED:
            rep.error(w, f"origin {r['origin']!r} must be one of {sorted(PHONEME_ORIGINS_ENTERED)} "
                         "(generated rows are produced by the build, not entered)")
        if r["origin"] == "sourced":
            check_source(w, r["source_id"])
        else:
            check_source(w, r["source_id"], required=False)
            if not r["reason"]:
                rep.error(w, f"origin={r['origin']} requires a reason")
        check_via(w, r)
        if r["status"] and r["status"] not in PHONEME_STATUS:
            rep.error(w, f"status {r['status']!r} must be blank or one of {sorted(PHONEME_STATUS)}")
        if r["class"] == "C":
            if r["place"] and r["place"] not in PLACES_C | {UNKNOWN}:
                rep.error(w, f"consonant place {r['place']!r} not in vocabulary")
            if r["manner"] and r["manner"] not in MANNERS_C | {UNKNOWN}:
                rep.error(w, f"consonant manner {r['manner']!r} not in vocabulary")
            if r["voicing"] and r["voicing"] not in VOICING:
                rep.error(w, f"voicing {r['voicing']!r} not in {sorted(VOICING)}")
        elif r["class"] == "V":
            if r["place"] and r["place"] not in PLACES_V | {UNKNOWN}:
                rep.error(w, f"vowel place (backness) {r['place']!r} not in {sorted(PLACES_V)}")
            if r["manner"] and r["manner"] not in MANNERS_V | {UNKNOWN}:
                rep.error(w, f"vowel manner (height) {r['manner']!r} not in vocabulary")
        if r["rounding"] and r["rounding"] not in ROUNDING:
            rep.error(w, f"rounding {r['rounding']!r} not in {sorted(ROUNDING)}")
        entered[L][s] = r

    for L, rows in entered.items():
        # A suppressed ∅ row is harmless anywhere: ∅ is never a phoneme.
        origins = {r["origin"] for s, r in rows.items() if not (s == ZERO and r["origin"] == "suppressed")}
        if "sourced" in origins and origins - {"sourced"}:
            rep.error(f"phonemes.csv ({L})",
                      "a sourced inventory cannot also have manual-add/suppressed/override rows; "
                      "either the source gives the inventory or it is generated")

    # --- correspondences (first pass: shape)
    corrs = []
    for r in t["correspondences"]:
        w = r["_where"]
        L = r["child_lect_id"]
        if L not in lects:
            rep.error(w, f"child_lect_id {L!r} is not in lects.csv")
            continue
        P = lects[L]["parent_id"]
        if not P:
            rep.error(w, f"{L} has no parent_id, so it cannot have correspondences")
            continue
        if not r["parent_phoneme"]:
            rep.error(w, "parent_phoneme is required")
            continue
        if not r["environment"]:
            rep.error(w, "environment is required (use 'elsewhere' for the default)")
        check_source(w, r["source_id"])
        check_via(w, r)
        if not r["page"] and not r["via_page"]:
            rep.warn(w, "no page number for the citation")
        # A row about another reconstruction system's proto-phoneme. Blank, the
        # parent's default system and "canonical" all mean the default inventory.
        if r["system"] in (CANONICAL, lects[P]["default_system"]):
            r["system"] = ""
        if r["parent_phoneme"] == ZERO and r["child_phoneme"] in ("", ZERO):
            rep.error(w, f"an inserted sound (parent_phoneme {ZERO}) needs the sound in child_phoneme")
        if r["parent_phoneme"] == ZERO and r["system"]:
            rep.error(w, f"an inserted sound (parent_phoneme {ZERO}) belongs to no reconstruction system; leave system blank")
        if r["child_phoneme"]:
            if r["blank_type"]:
                rep.error(w, "has both a child_phoneme and a blank_type; use one")
            if r["status"] not in CORR_STATUS:
                rep.error(w, f"status {r['status']!r} must be one of {sorted(CORR_STATUS)}")
        else:
            if not r["blank_type"]:
                rep.error(w, "empty child_phoneme needs a blank_type "
                             f"({', '.join(sorted(BLANK_TYPES))}); an untyped blank is a data error")
            elif r["blank_type"] not in BLANK_TYPES:
                rep.error(w, f"blank_type {r['blank_type']!r} not in {sorted(BLANK_TYPES)}")
            if r["status"]:
                rep.error(w, "status applies to reflexes; leave it empty on a typed blank")
        if r["evidence_count"]:
            if not r["evidence_count"].isdigit():
                rep.error(w, f"evidence_count {r['evidence_count']!r} must be a non-negative integer")
        if r["evidence_total"]:
            if not r["evidence_total"].isdigit():
                rep.error(w, f"evidence_total {r['evidence_total']!r} must be a non-negative integer")
            elif r["evidence_count"].isdigit() and int(r["evidence_count"]) > int(r["evidence_total"]):
                rep.error(w, f"evidence_count {r['evidence_count']} is more than evidence_total {r['evidence_total']}")
            elif not r["evidence_count"]:
                rep.warn(w, "evidence_total without evidence_count: give n with N")
        if r["evidence_count"] == "0" and r["child_phoneme"]:
            rep.warn(w, "a reflex with evidence_count 0 has no examples; make it a typed blank or delete it")
        if r["conditioning"] and r["conditioning"] not in CONDITIONING:
            rep.error(w, f"conditioning {r['conditioning']!r} not in {sorted(CONDITIONING)}")
        if r["derivation"] and r["derivation"] not in DERIVATIONS:
            rep.error(w, f"derivation {r['derivation']!r} not in {sorted(DERIVATIONS)}")
        if r["environment"].strip().lower() in ENV_UNKNOWN_SPELLINGS:
            rep.warn(w, f"environment {r['environment']!r}: write {ENV_UNKNOWN!r} (and conditioning 'unknown')")
        if r["environment"] == ENV_UNKNOWN and not r["conditioning"]:
            r["conditioning"] = "unknown"
        if r["lexical_scope"] and not r["conditioning"]:
            r["conditioning"] = "lexical"
        if not r["derivation"]:
            r["derivation"] = "as-stated"
        if r["decision"]:
            if r["decision"] not in decisions:
                rep.error(w, f"decision {r['decision']!r} is not in decisions.csv")
            else:
                decisions[r["decision"]]["rows"].append(r["id"] or w)
        env = r["environment"]
        if env and env not in ENV_SHORTHANDS and env not in ENV_SYLLABLES and env != ENV_UNKNOWN and "_" not in env:
            rep.note(w, f"environment {env!r} is free text (no '_' slot)")
        r["parent_lect_id"] = P
        r["parent_phoneme_id"] = pid(P, r["parent_phoneme"], r["system"])
        r["child_phoneme_id"] = pid(L, r["child_phoneme"]) if r["child_phoneme"] else None
        if not r["id"]:
            key = "|".join([L, r["parent_phoneme"], r["child_phoneme"], env, r["source_id"], r["page"]]
                           + ([r["system"]] if r["system"] else [])
                           + ([r["via_source_id"], r["via_page"]] if r["via_source_id"] else []))
            r["id"] = "c" + hashlib.sha1(key.encode()).hexdigest()[:10]
            rep.note(w, f"no id: fill in {r['id']} so links to this row survive edits")
        corrs.append(r)

    seen_ids = {}
    for r in corrs:
        if r["id"] in seen_ids:
            rep.error(r["_where"], f"duplicate correspondence id {r['id']!r} "
                                   f"(also {seen_ids[r['id']]})")
        seen_ids[r["id"]] = r["_where"]

    # --- inventories, resolved top-down so a generated parent exists before its children
    inventory = {}   # lect -> sym -> phoneme dict
    inv_status = {}
    reflexes_by_lect = defaultdict(dict)  # lect -> sym -> first row seen
    for r in corrs:
        if r["child_phoneme"] and r["child_phoneme"] != ZERO:
            reflexes_by_lect[r["child_lect_id"]].setdefault(r["child_phoneme"], r)

    symbols_of = defaultdict(set)   # every symbol a lect is written with
    for L, rows in entered.items():
        symbols_of[L] |= {s for s, r in rows.items() if r["origin"] != "suppressed"}
    unchanged = set()               # (lect, symbol) continued unchanged from the parent
    for r in corrs:
        if r["child_phoneme"]:
            symbols_of[r["child_lect_id"]].add(r["child_phoneme"])
            if r["child_phoneme"] == r["parent_phoneme"] and not r["system"]:
                unchanged.add((r["child_lect_id"], r["child_phoneme"]))

    def reading(L, s, seen=()):
        """Features for a symbol the lect's rows do not describe.

        1. y and j, where the lect writes both (YJ_PAIR).
        2. A letter that is not plain IPA and is continued unchanged from the
           parent is read as the parent reads it (PMc *y > Chuukese y).
        3. The reconstruction orthography, in a proto-language.
        4. The IPA table.
        """
        if s in YJ_PAIR and set(YJ_PAIR) <= symbols_of[L]:
            return YJ_PAIR[s]
        P = lects[L]["parent_id"]
        if (s in PROTO_ORTHO or ipa_features(s)[0] == "other") and (L, s) in unchanged \
                and P and L not in seen:
            row = entered.get(P, {}).get(s)
            if row and row["origin"] != "suppressed" and row["class"] in ("C", "V") \
                    and row["place"] not in ("", UNKNOWN) and row["manner"] not in ("", UNKNOWN):
                return (row["class"], row["place"].replace(LABIALIZED, ""), row["manner"],
                        row["voicing"], row["rounding"])
            if s in symbols_of[P]:
                return reading(P, s, seen + (L,))
        return symbol_features(s, lects[L]["type"] in RECONSTRUCTED)

    def phoneme_record(L, s, row, origin):
        inferred = []
        if row is not None:
            got = {"class": row["class"], "place": row["place"], "manner": row["manner"],
                   "voicing": row["voicing"], "rounding": row["rounding"]}
            # The source gave no place or manner: read them off the symbol.
            inferred = fill_blanks(got, reading(L, s))
            cls, place, manner, voicing, rnd = (got[k] for k in ("class", "place", "manner", "voicing", "rounding"))
        else:
            cls, place, manner, voicing, rnd = reading(L, s)
            if cls == "other":
                # Not a symbol the chart knows: at least say consonant or vowel,
                # from what it continues, so it lands in the right unclassified group.
                P = lects[L]["parent_id"]
                votes = [inventory[P][r["parent_phoneme"]]["class"] for r in corrs
                         if r["child_lect_id"] == L and r["child_phoneme"] == s and not r["system"]
                         and r["parent_phoneme"] in inventory.get(P, {})]
                votes = [v for v in votes if v in ("C", "V")]
                if votes:
                    cls = max(set(votes), key=votes.count)
        if cls == "C" and place in PLACES_C_PLAIN and LABIAL_MARK in s:
            place = LABIALIZED + place
        return {
            "placement": ("inferred" if row is None or {"place", "manner"} & set(inferred)
                          else "source" if origin == "sourced" else "hand"),
            "inferred_fields": inferred if row is not None else ["place", "manner", "voicing", "rounding"],
            "absent_from": [],
            **via_of(row or {}),
            "id": pid(L, s), "lect_id": L, "ipa": s,
            "url_id": phoneme_url_id(s, lects[L]["type"]),
            "source_symbol": (row or {}).get("source_symbol", ""),
            "class": cls, "place": place, "manner": manner, "voicing": voicing, "rounding": rnd,
            "origin": origin,
            "source_id": (row or {}).get("source_id", ""),
            "page": (row or {}).get("page", ""),
            "reason": (row or {}).get("reason", ""),
            "notes": (row or {}).get("notes", ""),
            "status": (row or {}).get("status", ""),
            "implied": False,
        }

    # Parents before daughters, so a lect with `inherit` can carry its parent's inventory down.
    order, placed = [], set()
    def visit(L, stack=()):
        if L in placed or L in stack:
            return
        P = lects[L]["parent_id"]
        if P in lects:
            visit(P, stack + (L,))
        placed.add(L)
        order.append(L)
    for L in lects:
        visit(L)

    def retentions(L, P, mode):
        """The X > X rows `inherit` stands for: one per parent phoneme the lect's rows leave open.

        assumed-unchanged (a tree that lists only changes): a parent phoneme with no
        row is retained, and one with only conditioned rows is retained elsewhere.
        stated-unchanged (the source lists only the nontrivial correspondences, and
        those in full): a parent phoneme with no row, or only sporadic or borrowed
        ones, is retained; conditioned rows get no complement.
        Cited to inherit_source_id / inherit_page, else to the source and page the
        lect's rows cite most."""
        rec = lects[L]
        mine = [r for r in corrs if r["child_lect_id"] == L and not r["system"]]
        cites = Counter((r["source_id"], r["page"]) for r in mine).most_common(1)
        source_id = rec["inherit_source_id"] or (cites[0][0][0] if cites else "")
        page = rec["inherit_page"] if rec["inherit_source_id"] or rec["inherit_page"] \
            else (cites[0][0][1] if cites else "")
        if not source_id:
            rep.warn(rec["_where"], f"inherit {mode}: the lect has no rows to take a citation from; "
                                    "give inherit_source_id and inherit_page")
        by_sym = defaultdict(list)
        for r in mine:
            by_sym[r["parent_phoneme"]].append(r)
        out = []
        for sym in inventory[P]:
            stated = by_sym.get(sym, [])
            if not retention_open(mode, stated):
                continue
            if mode == "assumed-unchanged":
                note = rec["inherit_note"] or (
                    ("Retained elsewhere: the source states this phoneme's development only under the "
                     "conditions in the rows above.") if stated else
                    "Not mentioned by the source, which lists only the changes into this node: retained.")
            else:
                note = rec["inherit_note"] or ("Unchanged: the source lists only the correspondences "
                                               "that are not identities.")
            r = {c: "" for c in TABLES["correspondences"]}
            r.update(child_lect_id=L, parent_phoneme=sym, child_phoneme=sym, environment="elsewhere",
                     status="regular", source_id=source_id, page=page, derivation=RETENTION_OF[mode],
                     conditioning="", notes=note, _where=f"lects.csv ({L}, inherit {mode})")
            r["parent_lect_id"] = P
            r["parent_phoneme_id"] = pid(P, sym)
            r["child_phoneme_id"] = pid(L, sym)
            tag = "implied" if mode == "assumed-unchanged" else "stated"
            r["id"] = "i" + hashlib.sha1(f"{L}|{sym}|{tag}".encode()).hexdigest()[:10]
            out.append(r)
        return out

    implied_rows = []   # every row the build adds for `inherit` (implied and stated retentions)
    for L in order:
        rows = entered.get(L, {})
        origins = {r["origin"] for r in rows.values()}
        P = lects[L]["parent_id"]
        mode = lects[L]["inherit"]
        if mode and P in inventory and (mode == "stated-unchanged" or "sourced" not in origins):
            for r in retentions(L, P, mode):
                corrs.append(r)
                implied_rows.append(r)
                reflexes_by_lect[L].setdefault(r["child_phoneme"], r)
                symbols_of[L].add(r["child_phoneme"])
                unchanged.add((L, r["child_phoneme"]))
        inv = {}
        if "sourced" in origins:
            # The source's list is the inventory (a suppressed ∅ row is skipped).
            inv_status[L] = "sourced"
            for s, row in rows.items():
                if row["origin"] == "sourced":
                    inv[s] = phoneme_record(L, s, row, "sourced")
            lects[L]["_suppressed"] = []
        else:
            generated = reflexes_by_lect.get(L, {})
            for s in generated:
                inv[s] = phoneme_record(L, s, None, "generated")
                # Only implied by an assumed-unchanged source: shown, but not as a stated phoneme.
                inv[s]["implied"] = all(r.get("derivation") == "implied-retention"
                                        for r in corrs if r["child_lect_id"] == L and r["child_phoneme"] == s)
            suppressed = []
            for s, row in rows.items():
                if row["origin"] == "override" or (row["origin"] == "manual-add" and s in inv):
                    # A hand placement of a generated phoneme: the row's class,
                    # place, manner, voicing and rounding replace the inferred ones.
                    if s not in inv:
                        rep.warn(row["_where"], f"override {L}:{s} is not a generated phoneme; row ignored")
                        continue
                    rec = inv[s]
                    for k in ("class", "place", "manner", "voicing", "rounding"):
                        if row[k]:
                            rec[k] = row[k]
                    if rec["class"] == "C" and rec["place"] in PLACES_C_PLAIN and LABIAL_MARK in s:
                        rec["place"] = LABIALIZED + rec["place"]
                    rec.update(placement="hand", reason=row["reason"], source_id=row["source_id"],
                               page=row["page"], notes=row["notes"], **via_of(row))
                elif row["origin"] == "manual-add":
                    inv[s] = phoneme_record(L, s, row, "manual-add")
                elif row["origin"] == "suppressed":
                    if s == ZERO:
                        continue  # ∅ is never generated; the row is harmless
                    if s not in inv:
                        rep.warn(row["_where"], f"suppressed {L}:{s} is not a generated phoneme")
                    else:
                        rec = inv.pop(s)
                        rec.update(origin="suppressed", reason=row["reason"],
                                   source_id=row["source_id"], page=row["page"])
                        suppressed.append(rec)
            inv_status[L] = "edited" if rows else ("reverse-generated" if inv else "empty")
            lects[L]["_suppressed"] = suppressed
        inventory[L] = inv

    # --- correspondences (second pass: referential integrity)
    for g in {g for r in lects.values() for g in r["overlap_list"]}:
        members = [L for L, r in lects.items() if g in r["overlap_list"]]
        if len(members) == 1:
            rep.warn(lects[members[0]]["_where"], f"overlapping subgroup {g!r} has only one member; check the spelling")
        if any(r["clade_label"] == g for r in lects.values()):
            rep.warn(lects[members[0]]["_where"], f"overlapping subgroup {g!r} has the name of a clade in the tree")
    for r in corrs:
        w, L, P = r["_where"], r["child_lect_id"], r["parent_lect_id"]
        if r["system"]:
            pass  # checked against the system's phonemes once notation_map is read
        elif not inventory.get(P):
            rep.error(w, f"ancestor {P} has no phoneme rows; enter its inventory first")
        elif r["parent_phoneme"] == ZERO:
            pass  # an inserted sound: nothing in the parent corresponds to it
        elif r["parent_phoneme"] not in inventory[P]:
            rep.error(w, f"parent phoneme {P}:{r['parent_phoneme']} is not in {P}'s inventory")
        if r["child_phoneme"] and r["child_phoneme"] != ZERO and inv_status[L] == "sourced" \
                and r["child_phoneme"] not in inventory[L]:
            rep.warn(w, f"reflex {L}:{r['child_phoneme']} is not in {L}'s sourced inventory")
        if r["child_phoneme"] and r["child_phoneme"] != ZERO and inv_status[L] == "edited" \
                and r["child_phoneme"] not in inventory[L]:
            rep.warn(w, f"reflex {L}:{r['child_phoneme']} was suppressed from {L}'s inventory; "
                        "this row still points at it")

    # --- fusions: pair the two rows of a cluster X+Y > R
    halves = {}  # (child lect, first, second, reflex) -> {"first": row, "second": row}
    for r in corrs:
        r["fusion"] = None
        if not r["child_phoneme"] or r["system"]:
            continue
        inv_p = inventory.get(r["parent_lect_id"]) or {}
        m1, m2 = FUSION_FIRST.match(r["environment"]), FUSION_SECOND.match(r["environment"])
        if m1 and m1.group(1) in inv_p:
            key, role = (r["child_lect_id"], r["parent_phoneme"], m1.group(1), r["child_phoneme"]), "first"
        elif m2 and m2.group(1) in inv_p:
            key, role = (r["child_lect_id"], m2.group(1), r["parent_phoneme"], r["child_phoneme"]), "second"
        else:
            continue
        slot = halves.setdefault(key, {})
        if role in slot:
            rep.warn(r["_where"], f"repeats the fusion row at {slot[role]['_where']}; ignored for the diagram")
            continue
        slot[role] = r
    for (L, a, b, R), slot in halves.items():
        P = lects[L]["parent_id"]
        if len(slot) < 2:
            r = next(iter(slot.values()))
            other = (f"parent_phoneme {b}, environment {a}+_" if "first" in slot
                     else f"parent_phoneme {a}, environment _+{b}")
            rep.warn(r["_where"], f"looks like half of the fusion {P}:{a}+{b} > {L}:{R}, but the other row "
                                  f"({other}, child_phoneme {R}) is missing; shown as an ordinary conditioned change")
            continue
        for role, r in slot.items():
            partner = slot["second" if role == "first" else "first"]
            r["fusion"] = {"members": [pid(P, a), pid(P, b)], "role": role,
                           "partner_correspondence_id": partner["id"]}
        if slot["first"]["evidence_count"] != slot["second"]["evidence_count"]:
            rep.warn(slot["second"]["_where"], f"the two rows of the fusion {P}:{a}+{b} > {L}:{R} "
                                               "have different evidence_count values")

    for L, rec in ((L, lects[L]) for L in lects):
        if rec["type"] == "proto-language" and not rec["parent_id"] and inv_status[L] != "sourced":
            rep.error(rec["_where"], f"root proto-language {L} needs a sourced inventory")

    # --- notation map, and the phonemes of every non-default reconstruction system
    # A lect's default canonical row stands for one row per phoneme that has no
    # canonical row of its own. The rows it stands for are made here, ahead of the
    # entered rows, and are treated exactly like entered ones from here on.
    defaults, entered_nm = {}, []
    for r in t["notation_map"]:
        if r["system"] == CANONICAL and not r["phoneme"] and not r["symbol"]:
            if r["lect_id"] not in lects:
                rep.error(r["_where"], f"lect_id {r['lect_id']!r} is not in lects.csv")
            elif r["lect_id"] in defaults:
                rep.error(r["_where"], f"a second default canonical row for {r['lect_id']} "
                                       f"(the first is {defaults[r['lect_id']]['_where']})")
            else:
                defaults[r["lect_id"]] = r
            continue
        entered_nm.append(r)
    own_canonical = {(r["lect_id"], r["phoneme"]) for r in entered_nm if r["system"] == CANONICAL}
    implicit_nm = []
    for L, d in defaults.items():
        for s, ph in inventory.get(L, {}).items():
            if not ph.get("implied") and (L, s) not in own_canonical:
                implicit_nm.append({**d, "phoneme": s, "symbol": s, "_where": f"{d['_where']} (default, *{s})"})
        # (A lect whose phonemes are all implied retentions needs no spelling yet.)
        if not any(r["lect_id"] == L for r in implicit_nm) \
                and not all(ph.get("implied") for ph in inventory.get(L, {}).values()):
            rep.warn(d["_where"], f"default canonical row for {L} applies to no phoneme")
    t["notation_map"] = implicit_nm + entered_nm

    notation = defaultdict(list)
    sysph = defaultdict(lambda: defaultdict(dict))   # lect -> system -> symbol -> record
    for r in t["notation_map"]:
        w = r["_where"]
        L = r["lect_id"]
        if L not in lects:
            rep.error(w, f"lect_id {L!r} is not in lects.csv")
            continue
        if lects[L]["type"] not in RECONSTRUCTED:
            rep.warn(w, f"{L} is not a proto-language; notation_map is for proto-phonemes")
        for col in ("system", "symbol"):
            if not r[col]:
                rep.error(w, f"'{col}' is required")
        S = r["system"]
        listed = lects[L]["systems_list"]
        # Another reconstruction system's phoneme, or only a spelling?
        own = bool(S) and S not in (CANONICAL, lects[L]["default_system"]) and (not listed or S in listed)
        if r["phoneme"]:
            if r["phoneme"] not in inventory.get(L, {}):
                rep.error(w, f"phoneme {L}:{r['phoneme']} is not in {L}'s inventory")
        elif not own:
            rep.error(w, "'phoneme' is required (it may be blank only for a phoneme of another "
                         "reconstruction system that has no counterpart in the default one)")
        if r["place"] and r["place"] not in PLACES_C | PLACES_V | {UNKNOWN}:
            rep.error(w, f"place {r['place']!r} not in vocabulary")
        if r["manner"] and r["manner"] not in MANNERS_C | MANNERS_V | {UNKNOWN}:
            rep.error(w, f"manner {r['manner']!r} not in vocabulary")
        if r["voicing"] and r["voicing"] not in VOICING:
            rep.error(w, f"voicing {r['voicing']!r} not in {sorted(VOICING)}")
        check_source(w, r["source_id"], required=False)
        check_via(w, r)
        entry = {"system": S, "symbol": r["symbol"], "source_id": r["source_id"], "page": r["page"],
                 "notes": r["notes"], "place": r["place"], "manner": r["manner"], "voicing": r["voicing"],
                 **via_of(r)}
        if r["phoneme"]:
            notation[pid(L, r["phoneme"])].append(entry)
        if r["symbol"] == ZERO:
            # This system does not have the phoneme at all.
            if r["phoneme"] in inventory.get(L, {}):
                inventory[L][r["phoneme"]]["absent_from"].append(S)
            else:
                rep.error(w, f"symbol {ZERO} marks a default phoneme as absent from {S}; 'phoneme' is required")
            continue
        if not own or not r["symbol"]:
            continue
        rec = sysph[L][S].setdefault(r["symbol"], {
            "id": pid(L, r["symbol"], S), "lect_id": L, "system": S, "ipa": r["symbol"],
            "url_id": phoneme_url_id(r["symbol"], lects[L]["type"]) + "@" + quote(S, safe=""),
            "class": "", "place": "", "manner": "", "voicing": "", "rounding": "",
            "placement": "source", "inferred_fields": [], "counterparts": [], "rows": []})
        for k in ("place", "manner", "voicing"):
            if r[k] and rec[k] and r[k] != rec[k]:
                rep.warn(w, f"{S} {L}:{r['symbol']} has {k} {rec[k]!r} on another row and {r[k]!r} here; "
                            "the first is used")
            rec[k] = rec[k] or r[k]
        if r["phoneme"] and pid(L, r["phoneme"]) not in rec["counterparts"]:
            rec["counterparts"].append(pid(L, r["phoneme"]))
        rec["rows"].append({**entry, "phoneme": r["phoneme"]})
    for L, systems in sysph.items():
        for S, phs in systems.items():
            for sym, rec in phs.items():
                mates = [inventory[L][c.split(":", 1)[1]] for c in rec["counterparts"]
                         if c.split(":", 1)[1] in inventory.get(L, {})]
                # Consonant or vowel: from the features, else from the default
                # phoneme it corresponds to, else from the symbol.
                if rec["place"] in PLACES_V or rec["manner"] in MANNERS_V:
                    rec["class"] = "V"
                elif rec["place"] or rec["manner"] or rec["voicing"]:
                    rec["class"] = "C"
                else:
                    rec["class"] = mates[0]["class"] if mates else symbol_features(sym, True)[0]
                # Blank place or manner. A distinctive IPA letter (θ, ɬ) speaks
                # for itself; a plain letter (d, S) takes the value of the default
                # phoneme it matches; failing that, the symbol tables.
                filled = []
                if not sym.isascii():
                    filled += fill_blanks(rec, ipa_features(sym))
                # Read only from this system's own symbol: the default phoneme's value
                # is another author's and is not inherited.
                filled += fill_blanks(rec, symbol_features(sym, True))
                rec["inferred_fields"] = filled
                if {"place", "manner"} & set(filled):
                    rec["placement"] = "inferred"
                if rec["class"] == "C" and rec["place"] in PLACES_C_PLAIN and LABIAL_MARK in sym:
                    rec["place"] = LABIALIZED + rec["place"]
                if not (rec["place"] or rec["manner"]):
                    rep.warn(f"notation_map.csv ({L})", f"{S} phoneme {L}:{sym} has no place or manner, "
                                                        "and none could be inferred; it is listed as unclassified")
            classes = {rec["class"] for rec in phs.values()}
            if "C" in classes and "V" not in classes:
                # A source may compare consonants only (Wolff's table has no vowels): say so, don't warn.
                rep.note(f"notation_map.csv ({L})", f"system {S} has consonants but no vowel rows; "
                                                    "the site says its vowels are not compared")
    for L, inv in inventory.items():
        if lects[L]["type"] not in RECONSTRUCTED:
            continue
        for s in inv:
            if not notation.get(pid(L, s)) and not inv[s].get("implied"):
                rep.error(f"notation_map.csv ({L})", f"proto-phoneme {L}:{s} has no notation_map row")

    # --- correspondences stated for another system's proto-phoneme
    for r in corrs:
        if r["system"] and r["parent_phoneme"] not in sysph[r["parent_lect_id"]].get(r["system"], {}):
            P = r["parent_lect_id"]
            if lects[P]["systems_list"] and r["system"] not in lects[P]["systems_list"]:
                rep.error(r["_where"], f"{r['system']} is not one of {P}'s reconstruction systems "
                                       f"({'; '.join(lects[P]['systems_list'])}); add it to lects.systems")
            else:
                rep.error(r["_where"], f"{r['system']} phoneme {P}:{r['parent_phoneme']} is not in notation_map "
                                       f"(add a row with system {r['system']}, symbol {r['parent_phoneme']})")

    # --- who cites what
    cited = {sid: {"phonemes": 0, "correspondences": 0, "notation": 0, "lects": set(),
                   "read_via": defaultdict(int), "relays": defaultdict(int)} for sid in sources}
    loose_via = re.compile(r"\bquoted from\b|\bvia\b", re.I)

    def count(kind, L, r):
        sid, via = r.get("source_id", ""), r.get("via_source_id", "")
        if sid in cited:
            cited[sid][kind] += 1
            cited[sid]["lects"].add(L)
            if via in cited:
                cited[sid]["read_via"][via] += 1
        if via in cited:
            cited[via]["lects"].add(L)
            if sid in cited:
                cited[via]["relays"][sid] += 1
        if not via and loose_via.search(r.get("notes", "")):
            rep.warn(r["_where"], "notes mention an indirect citation ('quoted from' / 'via') but "
                                  "via_source_id is empty")

    for r in t["phonemes"]:
        count("phonemes", r["lect_id"], r)
    for r in t["correspondences"]:
        count("correspondences", r["child_lect_id"], r)
    for r in t["notation_map"]:
        count("notation", r["lect_id"], r)
    for sid, c in cited.items():
        if not (c["phonemes"] or c["correspondences"] or c["notation"] or c["relays"]):
            rep.warn(sources[sid]["_where"], f"source {sid} is never cited by a phoneme, correspondence "
                                             "or notation row")
        sources[sid]["cited_by"] = {
            "phonemes": c["phonemes"], "correspondences": c["correspondences"], "notation": c["notation"],
            "lects": sorted(c["lects"]),
            "read_via": [{"source_id": k, "rows": v} for k, v in sorted(c["read_via"].items())],
            "relays": [{"source_id": k, "rows": v} for k, v in sorted(c["relays"].items())],
        }

    # --- attested lects are transcribed in IPA; the printed form goes in source_symbol / source_form
    odd = defaultdict(lambda: defaultdict(set))
    for r in t["phonemes"]:
        if r["lect_id"] in lects and lects[r["lect_id"]]["type"] in ("language", "dialect"):
            for why in non_ipa(r["ipa"]):
                odd[r["lect_id"]][why].add(r["ipa"])
    for r in t["correspondences"]:
        if r["child_lect_id"] in lects and lects[r["child_lect_id"]]["type"] in ("language", "dialect") \
                and r["child_phoneme"]:
            for why in non_ipa(r["child_phoneme"]):
                odd[r["child_lect_id"]][why].add(r["child_phoneme"])
    for L, whys in sorted(odd.items()):
        rep.warn(lects[L]["_where"], f"{lects[L]['name']} has symbols that are not IPA: "
                 + "; ".join(f"{' '.join(sorted(v))} (use {why})" for why, v in whys.items())
                 + ". Keep the printed form in source_symbol / source_form.")

    # --- works cited in running text (notes) need a sources row
    labels = defaultdict(set)   # 'Lee & Wang' -> {'1984', '2022a', ...}
    for sr in sources.values():
        who = sr["label"].rsplit(" ", 1)[0]
        labels[who].add(sr["year"] + sr["year_suffix"])
        labels[who].add(sr["year"])
    missing_works = {}
    lect_words = frozenset(w for r in lects.values() for n in [r["name"]] + r["alt_names_list"]
                           for w in [n] + n.replace("-", " ").split())
    text_cols = ("notes", "orthography_note", "reason", "via_note")
    for table in ("sources", "lects", "phonemes", "correspondences", "notation_map"):
        for r in t[table]:
            for col in text_cols:
                for who, year, suffix in cited_works(r.get(col, "") or "", lect_words):
                    known = labels.get(who) or next((v for k, v in labels.items() if k.endswith(" " + who)), set())
                    if year + suffix in known or (not suffix and any(k.startswith(year) for k in known)):
                        continue
                    entry = missing_works.setdefault((who, year + suffix), [r["_where"], 0])
                    entry[1] += 1
    for (who, year), (where, n) in sorted(missing_works.items()):
        rep.warn(where, f"{who} ({year}) is cited in notes but has no sources row"
                        + (f" ({n} mentions; this is the first)" if n > 1 else ""))

    # --- build reports
    by_parent = defaultdict(list)   # parent_phoneme_id -> rows
    by_child = defaultdict(list)    # child_phoneme_id -> rows
    entered_pairs = defaultdict(set)  # child lect -> parent symbols with any row
    for r in corrs:
        by_parent[r["parent_phoneme_id"]].append(r)
        if r["child_phoneme_id"]:
            by_child[r["child_phoneme_id"]].append(r)
        if not r["system"] and r["parent_phoneme"] != ZERO and r["derivation"] != "implied-retention":
            entered_pairs[r["child_lect_id"]].add(r["parent_phoneme"])

    for L, rec in lects.items():
        P = rec["parent_id"]
        if not P or P not in inventory:
            continue
        missing = [s for s in inventory[P] if s not in entered_pairs.get(L, set())]
        if rec["changes_only_flag"]:
            continue   # the rest is implied retention
        if missing and entered_pairs.get(L):
            rep.note(f"{L}", f"unentered proto-phonemes of {P}: {' '.join('*' + m for m in missing)}")
        elif missing and inventory[P]:
            rep.note(f"{L}", f"no correspondences entered yet against {P}")
        if inv_status[L] in ("reverse-generated", "edited"):
            groups = defaultdict(list)
            for s, ph in inventory[L].items():
                if ph["origin"] == "generated" and ph["place"] and ph["manner"]:
                    groups[(ph["class"], ph["place"], ph["manner"])].append(s)
            for key, syms in groups.items():
                if len(syms) > 1:
                    rep.note(L, f"generated phonemes {' '.join(syms)} share {key[1]} {key[2]}; "
                                "check whether they are allophones")

    for d in decisions.values():
        if d["status"] == "open":
            rep.note(d["_where"], f"open decision {d['id']}: {d['question']}"
                                  + (f" ({len(d['rows'])} row(s))" if d["rows"] else ""))
    return {
        "decisions": decisions,
        "sources": sources, "lects": lects, "inventory": inventory, "inv_status": inv_status,
        "corrs": corrs, "by_parent": by_parent, "by_child": by_child, "notation": notation,
        "sysph": sysph, "conflicts": find_conflicts(corrs, sysph), "entered_pairs": entered_pairs,
        "overlap": {g: sorted(L for L, r in lects.items() if g in r["overlap_list"])
                    for g in {g for r in lects.values() for g in r["overlap_list"]}},
        "competing": {L for L, r in lects.items() if r["competes_list"]}
                     | {c for r in lects.values() for c in r["competes_list"]},
    }


def find_conflicts(corrs, sysph):
    """(child lect, default parent phoneme id) pairs where the record disagrees
    with itself: a disputed row, rows from more than one source, or a separate
    descent stated for another reconstruction system's phoneme."""
    groups = defaultdict(list)
    for r in corrs:
        if not r["system"]:
            groups[(r["child_lect_id"], r["parent_phoneme_id"])].append(r)
    out = set()
    for key, rows in groups.items():
        cites = {(r["source_id"], r["via_source_id"]) for r in rows}
        if len(cites) > 1 or any("disputed" in (r["status"], r["blank_type"]) for r in rows):
            out.add(key)
    for r in corrs:
        if r["system"]:
            rec = sysph[r["parent_lect_id"]][r["system"]].get(r["parent_phoneme"])
            for c in (rec or {}).get("counterparts", []):
                out.add((r["child_lect_id"], c))
    return out
