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
            elif r["id"] != r["glottocode"] and r["type"] not in RECONSTRUCTED | GROUP_TYPES:
                # Checked once the tree is known: a sub-dialect may share the code of the lect it is listed under.
                r["_code_differs"] = True
        elif r["type"] not in RECONSTRUCTED | GROUP_TYPES:
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
        r["tree_parent"] = r.get("tree_parent", "").strip()
        r["representative"] = r.get("representative", "").strip()
        if r["type"] in GROUP_TYPES:
            for col in ("inherit", "language_id", "alt_parents", "competes_with", "clade"):
                if r[col]:
                    rep.warn(w, f"{col} does not apply to a group (a tree node with no rows); ignored")
                    r[col] = ""
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
        if r["representative"]:
            if r["type"] != "language":
                rep.warn(w, "representative is for a language node; ignored")
                r["representative"] = ""
            elif r["representative"] not in lects:
                rep.error(w, f"representative {r['representative']!r} is not a lect")
                r["representative"] = ""
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

    # The tree the lect list draws: each lect under its tree_parent. Usually that is a group
    # (a linkage, or a subgroup with no proto-language), a language (for its dialects) or a
    # dialect (for its sub-dialects) under the same parent_id. It may also stand lower than
    # the lect's parent_id, and be a reconstructed lect: the classification puts the lect in
    # a subgroup whose proto-language its rows are not stated against (Nese, stated against
    # POc by Lynch, listed under North-Central Vanuatu > Central Vanuatu). The tree is the
    # classification; parent_id is the predecessor of the lect's rows and the lect it inherits
    # from. The one rule: the tree parent stands at or below the lect's parent_id, so that
    # the lect is still drawn somewhere under the stage it descends from.
    # Blank: a dialect goes under its language_id when the two have the same parent_id;
    # anything else under its parent_id.
    def stands_under(tp, P):
        seen = set()
        while tp and tp in lects and tp not in seen:
            if tp == P or lects[tp]["parent_id"] == P:
                return True
            seen.add(tp)
            tp = lects[tp]["tree_parent"] if lects[tp]["tree_parent"] in lects else lects[tp]["parent_id"]
        return False
    for r in lects.values():
        w, tp = r["_where"], r["tree_parent"]
        if tp:
            if tp not in lects:
                rep.error(w, f"tree_parent {tp!r} is not a lect")
                tp = ""
            elif tp == r["id"]:
                rep.error(w, "tree_parent names the lect itself")
                tp = ""
            elif not stands_under(tp, r["parent_id"]):
                rep.error(w, f"tree_parent {tp!r} does not stand under {r['parent_id'] or 'nothing'!r}, this lect's "
                             "parent_id: a tree parent is the lect's parent_id or a node below it")
                tp = ""
        elif r["type"] == "dialect" and r["language_id"] in lects:
            lg = lects[r["language_id"]]
            if lg["parent_id"] == r["parent_id"]:
                tp = r["language_id"]
            else:
                rep.note(w, f"listed under {r['parent_id']!r}, not under its language {r['language_id']!r}, "
                            f"which stands under {lg['parent_id'] or 'nothing'!r}")
        r["tree_parent_id"] = tp or r["parent_id"]
    for r in lects.values():
        seen, cur = {r["id"]}, r["tree_parent_id"]
        while cur and cur in lects:
            if cur in seen:
                rep.error(r["_where"], f"tree_parent chain loops back to {cur!r}")
                r["tree_parent_id"] = r["parent_id"]
                break
            seen.add(cur)
            cur = lects[cur]["tree_parent_id"]
    tree_kids = defaultdict(list)
    for L, r in lects.items():
        if r["tree_parent_id"]:
            tree_kids[r["tree_parent_id"]].append(L)
    for r in lects.values():
        r["tree_children"] = sorted(tree_kids.get(r["id"], []))
        if r.get("_code_differs"):
            tp = lects.get(r["tree_parent_id"])
            if not (tp and tp["glottocode"] == r["glottocode"] and r["tree_parent_id"] != r["parent_id"]):
                rep.warn(r["_where"], f"lect id should be its Glottocode ({r['glottocode']})")
        if r["type"] in GROUP_TYPES and not r["tree_children"]:
            rep.warn(r["_where"], "group with no members (no lect has it as tree_parent)")
        rp = r["representative"]
        if rp and lects[rp]["tree_parent_id"] != r["id"]:
            rep.error(r["_where"], f"representative {rp!r} is not listed under this language "
                                   "(give it language_id or tree_parent)")
            r["representative"] = ""

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
        # The row's predecessor: the lect its parent_phoneme belongs to. Blank, it is the
        # lect's own parent_id. A row may name another lect (correspondences.parent_lect_id):
        # a loan stratum stated against its donor or the donor's ancestor (Yapese words from
        # a pre-Oceanic source, against PMP), or a reflex that a source states against a
        # stage other than the one the lect inherits from. Such a row is the lect's reflex
        # of that lect's phoneme and nothing more: it does not count as an outcome of the
        # lect's own parent, so inheritance and coverage leave it aside.
        P = lects[L]["parent_id"]
        own = r.get("parent_lect_id", "").strip()
        r["other_predecessor"] = False
        if own and own != P:
            if own not in lects:
                rep.error(w, f"parent_lect_id {own!r} is not in lects.csv")
                continue
            if own == L:
                rep.error(w, "parent_lect_id names the lect itself")
                continue
            if lects[own]["type"] in GROUP_TYPES:
                rep.error(w, f"parent_lect_id {own!r} is a {lects[own]['type']}: it has no phonemes")
                continue
            if lects[own]["type"] not in RECONSTRUCTED and r["status"] != "loan-stratum":
                rep.error(w, f"parent_lect_id {own!r} is an attested lect; only a loan-stratum row can be "
                             "stated against one (its donor)")
                continue
            P = own
            r["other_predecessor"] = True
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
            if r["child_phoneme"] == r["parent_phoneme"] and not r["system"] and not r["other_predecessor"]:
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
                return (row["class"], row["place"].replace(LABIALIZED, "").replace(VELARIZED, ""), row["manner"],
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
                votes = [inventory[r["parent_lect_id"]][r["parent_phoneme"]]["class"] for r in corrs
                         if r["child_lect_id"] == L and r["child_phoneme"] == s and not r["system"]
                         and r["parent_phoneme"] in inventory.get(r["parent_lect_id"], {})]
                votes = [v for v in votes if v in ("C", "V")]
                if votes:
                    cls = max(set(votes), key=votes.count)
        if cls == "C":
            place = secondary_column(place, s)
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

    def retentions(L, P, mode, attested_rule=False):
        """The X > X rows `inherit` stands for: one per parent phoneme the lect's rows leave open.

        attested_rule (an attested lect with no sourced inventory, assumed-unchanged): *q, *R,
        *z and *N are not carried down (listed in the lect's `_not_implied`), and a letter of the
        reconstruction orthography is respelled in IPA (*y > j; IMPLIED_IPA, NOT_IMPLIED_IN_ATTESTED).
        Where the lect's own rows already have that IPA symbol, the retention joins it (Habun has
        j from *z, and *y is j too), unless the lect writes the symbol for another sound: its
        rows have both y and j (YJ_PAIR), or a phoneme row places it elsewhere.

        assumed-unchanged (a tree that lists only changes): a parent phoneme with no
        row is retained, and one with only conditioned rows is retained elsewhere.
        stated-unchanged (the source lists only the nontrivial correspondences, and
        those in full): a parent phoneme with no row, or only sporadic or borrowed
        ones, is retained; conditioned rows get no complement.
        Cited to inherit_source_id / inherit_page, else to the source and page the
        lect's rows cite most."""
        rec = lects[L]
        mine = [r for r in corrs if r["child_lect_id"] == L and not r["system"] and not r.get("other_predecessor")]
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
        # Symbols the lect is already written with (its own rows): a respelling must not land on one.
        taken = {r["child_phoneme"] for r in mine if r["child_phoneme"]} \
            | {s for s, row in entered.get(L, {}).items() if row["origin"] != "suppressed"}
        def own_is_ipa(s):
            """Is s, in the lect's own rows, the sound the IPA table gives it?"""
            if s in YJ_PAIR and set(YJ_PAIR) <= taken:
                return False
            row = entered.get(L, {}).get(s)
            want = ipa_features(s)
            return not (row and row["origin"] != "suppressed" and any(
                row[k] and row[k] != UNKNOWN and row[k].replace(LABIALIZED, "").replace(VELARIZED, "") != w
                for k, w in (("place", want[1]), ("manner", want[2]))))
        for sym in inventory[P]:
            stated = by_sym.get(sym, [])
            if not retention_open(mode, stated):
                continue
            child = sym
            if attested_rule:
                if sym in NOT_IMPLIED_IN_ATTESTED:
                    rec.setdefault("_not_implied", []).append(sym)
                    continue
                child = implied_ipa(sym, inventory[P][sym])
                # Kept as printed where the lect's own rows use the IPA symbol for another sound.
                if child != sym and child in taken and not own_is_ipa(child):
                    rep.warn(rec["_where"], f"implied *{sym} of {rec_name(P)} is kept as {sym} in {rec['name']}: "
                                            f"its IPA symbol {child} is already used by the lect's own rows "
                                            "for another sound; respell that one in IPA")
                    child = sym
            if mode == "assumed-unchanged" and rec.get("inherit_auto"):
                note = rec["inherit_note"] or (
                    ("Retained elsewhere: the sources state this phoneme's development only under the "
                     "conditions in the rows above.") if stated else
                    f"Not mentioned by the sources entered, which give fewer than {SMALL_INVENTORY} phonemes "
                    "for this lect: taken as retained from its immediate ancestor.")
            elif mode == "assumed-unchanged":
                note = rec["inherit_note"] or (
                    ("Retained elsewhere: the source states this phoneme's development only under the "
                     "conditions in the rows above.") if stated else
                    "Not mentioned by the source, which lists only the changes into this node: retained.")
            else:
                note = rec["inherit_note"] or ("Unchanged: the source lists only the correspondences "
                                               "that are not identities.")
            r = {c: "" for c in TABLES["correspondences"]}
            if child != sym:
                note = note.rstrip(".") + f"; written {child}, the IPA symbol for the value of {rec_name(P)} *{sym}."
            r.update(child_lect_id=L, parent_phoneme=sym, child_phoneme=child, environment="elsewhere",
                     status="regular", source_id=source_id, page=page, derivation=RETENTION_OF[mode],
                     conditioning="", notes=note, _where=f"lects.csv ({L}, inherit {mode})")
            r["parent_lect_id"] = P
            r["parent_phoneme_id"] = pid(P, sym)
            r["child_phoneme_id"] = pid(L, child)
            tag = "implied" if mode == "assumed-unchanged" else "stated"
            r["id"] = "i" + hashlib.sha1(f"{L}|{sym}|{tag}".encode()).hexdigest()[:10]
            out.append(r)
        return out

    def rec_name(L):
        return lects[L]["name"]

    def ancestors(L):
        seen, P = [], lects[L]["parent_id"]
        while P in lects and P not in seen:
            seen.append(P)
            P = lects[P]["parent_id"]
        return seen

    def vowel_default(L, P, rows):
        """Implied V > V rows for a lect whose sourced vowels are a bare five- or four-vowel system and
        whose rows state no vowel change (decision vowel-default): i e a o u under POc takes its parent's
        five vowels unchanged, i e/ə a u under PMP (or PAN) its parent's four, the schwa matched by place
        and height, whatever symbol each uses for it."""
        if P not in inventory or inv_status.get(L) != "sourced":
            return []
        vow = {s: rec for s, rec in inventory[L].items() if rec["class"] == "V"}
        pv = {s: rec for s, rec in inventory[P].items() if rec["class"] == "V"}
        up = set(ancestors(L))

        def schwa(recs):
            hits = [s for s, rec in recs.items() if rec["place"] == "central" and "mid" in rec["manner"]]
            return hits[0] if len(hits) == 1 else None

        if set(vow) == set("ieaou") and set(pv) == set("ieaou") and VOWEL_DEFAULT_POC in up:
            pairs, kind = {s: s for s in "ieaou"}, "five-vowel system i e a o u below POc"
        elif len(vow) == 4 and len(pv) == 4 and up & VOWEL_DEFAULT_PMP and set("iau") <= set(vow) \
                and set("iau") <= set(pv) and schwa(vow) and schwa(pv):
            pairs, kind = {**{s: s for s in "iau"}, schwa(pv): schwa(vow)}, "four-vowel system i ə a u below PMP"
        else:
            return []
        if any(r["child_lect_id"] == L and not r["system"] and not r.get("other_predecessor")
               and r["parent_phoneme"] in pv for r in corrs):
            return []   # the source states something about the vowels: no default
        cites = Counter((rows[s]["source_id"], rows[s]["page"]) for s in vow if s in rows).most_common(1)
        source_id, page = cites[0][0] if cites else ("", "")
        out = []
        for ps, cs in pairs.items():
            r = {c: "" for c in TABLES["correspondences"]}
            r.update(child_lect_id=L, parent_phoneme=ps, child_phoneme=cs, environment="elsewhere",
                     status="regular", source_id=source_id, page=page, derivation="implied-retention",
                     decision=VOWEL_DEFAULT_DECISION if VOWEL_DEFAULT_DECISION in decisions else "",
                     notes=f"Not stated: a {kind} with no stated vowel change is taken to keep "
                           f"{P}'s vowels unchanged until a source says otherwise (decision vowel-default).",
                     _where=f"lects.csv ({L}, vowel default)")
            r["parent_lect_id"] = P
            r["parent_phoneme_id"] = pid(P, ps)
            r["child_phoneme_id"] = pid(L, cs)
            r["id"] = "i" + hashlib.sha1(f"{L}|{ps}|vowel-default".encode()).hexdigest()[:10]
            if r["decision"]:
                decisions[r["decision"]]["rows"].append(r["id"])
            out.append(r)
        return out

    def rec_inherit_note(L):
        return lects[L]["inherit_note"]

    implied_rows = []   # every row the build adds for `inherit` (implied and stated retentions)
    with_corrs = {r["child_lect_id"] for r in corrs if not r["system"]}
    for L in order:
        rows = entered.get(L, {})
        origins = {r["origin"] for r in rows.values()}
        P = lects[L]["parent_id"]
        # A lect for which fewer than SMALL_INVENTORY phonemes are known (from its sourced
        # inventory, else from its reflexes) inherits, as assumed-unchanged, whatever of its
        # immediate ancestor's phonemes its rows leave open: so few phonemes are a partial
        # record, not an inventory. Lects with no rows of their own are left alone.
        if not lects[L]["inherit"] and lects[L]["type"] not in GROUP_TYPES and P in inventory \
                and (L in with_corrs or "sourced" in origins):
            known = ({s for s, r in rows.items() if r["origin"] == "sourced"} if "sourced" in origins
                     else set(reflexes_by_lect.get(L, {})) | {s for s, r in rows.items() if r["origin"] == "manual-add"})
            if len(known - {ZERO}) < SMALL_INVENTORY:
                lects[L]["inherit"] = "assumed-unchanged"
                lects[L]["changes_only_flag"] = True
                lects[L]["inherit_auto"] = True
                rep.note(lects[L]["_where"], f"fewer than {SMALL_INVENTORY} phonemes known ({len(known - {ZERO})}): "
                                             "inherits the rest of its parent's phonemes as assumed-unchanged")
        mode = lects[L]["inherit"]
        if mode and P in inventory and (mode == "stated-unchanged" or "sourced" not in origins):
            attested_rule = (mode == "assumed-unchanged" and "sourced" not in origins
                             and lects[L]["type"] in ("language", "dialect"))
            for r in retentions(L, P, mode, attested_rule):
                corrs.append(r)
                implied_rows.append(r)
                reflexes_by_lect[L].setdefault(r["child_phoneme"], r)
                symbols_of[L].add(r["child_phoneme"])
                # A respelled retention (*y > j) is read as IPA, not as the parent reads the letter.
                if r["child_phoneme"] == r["parent_phoneme"]:
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
                    if rec["class"] == "C":
                        rec["place"] = secondary_column(rec["place"], s)
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
        for r in vowel_default(L, P, rows):
            corrs.append(r)
            implied_rows.append(r)
            unchanged.add((L, r["child_phoneme"]))
        # A sourced inventory under an assumed-unchanged source: the parent's phonemes the source
        # does not mention are taken as kept where the inventory has the same phoneme (same symbol,
        # and no place or manner that contradicts the parent's). Without these rows the lect would
        # have an inventory and no history at all (Fehan Tetun, Kambera).
        if mode == "assumed-unchanged" and "sourced" in origins and P in inventory:
            def same(a, b):
                return a["class"] == b["class"] and all(
                    not a[k] or not b[k] or "unknown" in (a[k], b[k]) or a[k] == b[k] for k in ("place", "manner"))
            for r in retentions(L, P, mode):
                s = r["child_phoneme"]
                if s in inv and same(inv[s], inventory[P][s]):
                    if not rec_inherit_note(L):
                        r["notes"] = r["notes"].rstrip(".") + "; the lect's own inventory has the same phoneme."
                    corrs.append(r)
                    implied_rows.append(r)
                    unchanged.add((L, s))

    # Reflexes that a row states and the lect's inventory does not have (the source's own list
    # lacks them, or a hand edit suppressed them). They are not phonemes of the inventory, but
    # every row links to its reflex, so each still gets a page: lect -> sym -> phoneme dict.
    stray = defaultdict(dict)

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
            if r["child_phoneme"] not in stray[L]:
                stray[L][r["child_phoneme"]] = phoneme_record(L, r["child_phoneme"], None, "outside-inventory")
        if r["child_phoneme"] and r["child_phoneme"] != ZERO and inv_status[L] == "edited" \
                and r["child_phoneme"] not in inventory[L]:
            rep.warn(w, f"reflex {L}:{r['child_phoneme']} was suppressed from {L}'s inventory; "
                        "this row still points at it")
            if r["child_phoneme"] not in stray[L]:
                rec = phoneme_record(L, r["child_phoneme"], None, "suppressed")
                rec["reason"] = next((x["reason"] for x in lects[L].get("_suppressed", [])
                                      if x["ipa"] == r["child_phoneme"]), "")
                stray[L][r["child_phoneme"]] = rec

    # --- fusions: pair the two rows of a cluster X+Y > R
    halves = {}  # (child lect, first, second, reflex) -> {"first": row, "second": row}
    for r in corrs:
        r["fusion"] = None
        if not r["child_phoneme"] or r["system"]:
            continue
        inv_p = inventory.get(r["parent_lect_id"]) or {}
        m1, m2 = FUSION_FIRST.match(r["environment"]), FUSION_SECOND.match(r["environment"])
        if m1 and m1.group(1) in inv_p:
            key, role = (r["child_lect_id"], r["parent_phoneme"], m1.group(1), r["child_phoneme"], r["parent_lect_id"]), "first"
        elif m2 and m2.group(1) in inv_p:
            key, role = (r["child_lect_id"], m2.group(1), r["parent_phoneme"], r["child_phoneme"], r["parent_lect_id"]), "second"
        else:
            continue
        slot = halves.setdefault(key, {})
        if role in slot:
            rep.warn(r["_where"], f"repeats the fusion row at {slot[role]['_where']}; ignored for the diagram")
            continue
        slot[role] = r
    for (L, a, b, R, P), slot in halves.items():
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
                if rec["class"] == "C":
                    rec["place"] = secondary_column(rec["place"], sym)
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

    # --- allophones: how a phoneme is realised, as the source describes it. Every
    # allophone a source gives belongs here, so that the phoneme's page explains it.
    allophones = defaultdict(list)   # phoneme id (lect:sym or lect:sym@System) -> rows
    for r in t.get("allophones", []):
        w, L, s, S = r["_where"], r["lect_id"], r["phoneme"], r["system"]
        if L not in lects:
            rep.error(w, f"lect_id {L!r} is not in lects.csv")
            continue
        if not s or not r["allophone"]:
            rep.error(w, "phoneme and allophone are required")
            continue
        if "[" in r["allophone"] or "/" in r["allophone"]:
            rep.error(w, "write the allophone without brackets or slashes; the site adds [ ]")
        check_source(w, r["source_id"])
        check_via(w, r)
        if S and S not in (CANONICAL, lects[L]["default_system"]):
            if s not in sysph.get(L, {}).get(S, {}):
                rep.warn(w, f"{S} phoneme {L}:{s} is not in notation_map; allophone row not shown")
                continue
            key = pid(L, s, S)
        else:
            if s not in inventory.get(L, {}):
                rep.warn(w, f"phoneme {L}:{s} is not in {L}'s inventory; allophone row not shown")
                continue
            key = pid(L, s)
        allophones[key].append({"allophone": r["allophone"], "environment": r["environment"],
                                "source_id": r["source_id"], "page": r["page"], "notes": r["notes"],
                                **via_of(r)})
    for L, inv in inventory.items():
        for s, rec in inv.items():
            rec["allophones"] = allophones.get(rec["id"], [])
    for L, systems in sysph.items():
        for S, phs in systems.items():
            for s, rec in phs.items():
                rec["allophones"] = allophones.get(rec["id"], [])
    # A phoneme row whose notes describe its realisations needs them in the allophones tab.
    # A note copied onto several phonemes of a lect is about the lect (Leti: 'pretonic high
    # vowels have glide allophones'); it is answered once any of those phonemes has rows.
    shared = defaultdict(list)
    for r in t["phonemes"]:
        if r["lect_id"] in inventory and r["ipa"] in inventory[r["lect_id"]] and ALLOPHONY_RE.search(r["notes"]):
            shared[(r["lect_id"], r["notes"])].append(r)
    # A note can describe another phoneme's realisation ('surface [e] can also be short /ʌ/'):
    # it is answered when a bracketed sound in it is an allophone row of another phoneme.
    lect_allo = defaultdict(set)   # lect -> {(phoneme, allophone)}
    for key, rows_ in allophones.items():
        L_, s_ = key.split(":", 1)
        s_ = s_.rsplit("@", 1)[0] if "@" in s_ else s_
        for a in rows_:
            lect_allo[L_].add((s_, a["allophone"]))

    def answered(L, r):
        if allophones.get(pid(L, r["ipa"])):
            return True
        heard = set(re.findall(r"\[([^\]\s,~]{1,8})\]", r["notes"]))
        return any(a in heard and s_ != r["ipa"] for s_, a in lect_allo[L])

    for (L, _), rows in shared.items():
        has = [r for r in rows if answered(L, r)]
        if len(rows) >= 3:
            if not has:
                rep.warn(rows[0]["_where"], f"the notes of {L}:{' '.join(r['ipa'] for r in rows)} describe "
                                            "allophones; give each in the allophones tab so the phoneme's page lists it")
            continue
        for r in rows:
            if r not in has:
                rep.warn(r["_where"], f"the notes of {L}:{r['ipa']} describe allophones; give each in the "
                                      "allophones tab so the phoneme's page lists it")

    # --- who cites what
    cited = {sid: {"phonemes": 0, "correspondences": 0, "notation": 0, "allophones": 0, "lects": set(),
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
    for r in t.get("allophones", []):
        count("allophones", r["lect_id"], r)
    for sid, c in cited.items():
        if not (c["phonemes"] or c["correspondences"] or c["notation"] or c["allophones"] or c["relays"]):
            rep.warn(sources[sid]["_where"], f"source {sid} is never cited by a phoneme, correspondence "
                                             "or notation row")
        sources[sid]["cited_by"] = {
            "phonemes": c["phonemes"], "correspondences": c["correspondences"], "notation": c["notation"],
            "allophones": c["allophones"], "lects": sorted(c["lects"]),
            "read_via": [{"source_id": k, "rows": v} for k, v in sorted(c["read_via"].items())],
            "relays": [{"source_id": k, "rows": v} for k, v in sorted(c["relays"].items())],
        }

    # --- attested lects are transcribed in IPA; the printed form goes in source_symbol / source_form
    odd = defaultdict(lambda: defaultdict(set))
    for r in t["phonemes"]:
        if r["lect_id"] in lects and lects[r["lect_id"]]["type"] in ("language", "dialect"):
            for why in non_ipa(r["ipa"]):
                if r["class"] == "V" and why.startswith("j for"):
                    continue   # y as a vowel is IPA (close front rounded): Sakao, Rotuman, Iaai
                odd[r["lect_id"]][why].add(r["ipa"])
    for r in t["correspondences"]:
        if r["child_lect_id"] in lects and lects[r["child_lect_id"]]["type"] in ("language", "dialect") \
                and r["child_phoneme"]:
            for why in non_ipa(r["child_phoneme"]):
                if why.startswith("j for") and symbol_features(r["parent_phoneme"], proto=True)[0] == "V":
                    continue   # y from a vowel is the close front rounded vowel (Vurës, Sakao ü)
                odd[r["child_lect_id"]][why].add(r["child_phoneme"])
    for L, whys in sorted(odd.items()):
        rep.warn(lects[L]["_where"], f"{lects[L]['name']} has symbols that are not IPA: "
                 + "; ".join(f"{' '.join(sorted(v))} (use {why})" for why, v in whys.items())
                 + ". Keep the printed form in source_symbol / source_form.")

    # --- /g/ is written ɡ (U+0261) in every symbol, reconstructions included
    latin_g = defaultdict(list)
    for r in t["phonemes"]:
        if "g" in r["ipa"]:
            latin_g["phonemes.csv"].append(f"{r['lect_id']}:{r['ipa']}")
    for r in t["notation_map"]:
        for c in ("phoneme", "symbol"):
            if "g" in r[c]:
                latin_g["notation_map.csv"].append(f"{r['lect_id']} {r['system']} {c} {r[c]}")
    for r in t["correspondences"]:
        for c in ("parent_phoneme", "child_phoneme"):
            if "g" in r[c]:
                latin_g["correspondences.csv"].append(f"{r['id'] or r['child_lect_id']} {c} {r[c]}")
        # In an environment only a g standing as a symbol (_g, _+g), not one in a word (high).
        if re.search(r"(?<![A-Za-z])g(?![A-Za-z])", r["environment"]):
            latin_g["correspondences.csv"].append(f"{r['id'] or r['child_lect_id']} environment {r['environment']}")
    for r in t.get("allophones", []):
        for c in ("phoneme", "allophone"):
            if "g" in r[c]:
                latin_g["allophones.csv"].append(f"{r['lect_id']}:{r['phoneme']} {c} {r[c]}")
    for where, items in latin_g.items():
        rep.error(where, f"{len(items)} symbol(s) with Latin g; write ɡ (U+0261): "
                  + "; ".join(items[:12]) + (" …" if len(items) > 12 else ""))

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
    # A source cited only in running text is not "not cited": the Sources page says where.
    by_label = defaultdict(list)   # 'Li 1981' -> [source ids]
    for sid, sr in sources.items():
        by_label[sr["label"]].append(sid)
    note_cites = defaultdict(lambda: {"n": 0, "lects": set()})
    lect_of = {"lects": "id", "phonemes": "lect_id", "correspondences": "child_lect_id", "notation_map": "lect_id",
               "allophones": "lect_id"}
    for table in ("sources", "lects", "phonemes", "correspondences", "notation_map", "allophones"):
        for r in t.get(table, []):
            for col in text_cols:
                for who, year, suffix in cited_works(r.get(col, "") or "", lect_words):
                    hits = by_label.get(f"{who} {year}{suffix}") or next(
                        (v for k, v in by_label.items() if k.endswith(f" {who} {year}{suffix}")), [])
                    if len(hits) == 1 and not (table == "sources" and r.get("id") == hits[0]):
                        nc = note_cites[hits[0]]
                        nc["n"] += 1
                        if table in lect_of and r.get(lect_of[table]) in lects:
                            nc["lects"].add(r[lect_of[table]])
                    known = labels.get(who) or next((v for k, v in labels.items() if k.endswith(" " + who)), set())
                    if year + suffix in known or (not suffix and any(k.startswith(year) for k in known)):
                        continue
                    entry = missing_works.setdefault((who, year + suffix), [r["_where"], 0])
                    entry[1] += 1
    for sid, sr in sources.items():
        nc = note_cites.get(sid)
        sr["cited_by"]["notes"] = nc["n"] if nc else 0
        sr["cited_by"]["note_lects"] = sorted(nc["lects"]) if nc else []
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
        if not r["system"] and r["parent_phoneme"] != ZERO and r["derivation"] != "implied-retention" \
                and not r.get("other_predecessor"):
            entered_pairs[r["child_lect_id"]].add(r["parent_phoneme"])

    # Nodes with no page: a group, and a language or dialect with no rows of its own whose
    # page would only list what the tree already lists under it (Babuza, Pazeh-Kaxabu). A
    # language with a representative opens that dialect's page instead (Tsou: Duhtu).
    has_rows = {r["lect_id"] for r in t["phonemes"]} | {r["child_lect_id"] for r in corrs} \
        | {r["lect_id"] for r in t["notation_map"]}
    for L, r in lects.items():
        if r["type"] in GROUP_TYPES:
            if L in has_rows:
                rep.error(r["_where"], "a group is a tree node only; its rows belong to its members")
            r["node_only"] = True
        else:
            r["node_only"] = (r["type"] in ("language", "dialect") and L not in has_rows and not r["inherit"]
                              and bool(r["tree_children"]))
        if r["representative"] and L in has_rows:
            rep.warn(r["_where"], "representative is set, but the language has rows of its own; "
                                  "its page shows them, not the representative's")
            r["representative"] = ""
        if r["node_only"] and r["type"] not in GROUP_TYPES:
            rep.note(r["_where"], "no rows of its own: a tree node with no page"
                                  + (f" (opens {r['representative']})" if r["representative"] else ""))

    for L, rec in lects.items():
        P = rec["parent_id"]
        if not P or P not in inventory or rec["node_only"]:
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
        "stray": {L: v for L, v in stray.items() if v},
        "corrs": corrs, "by_parent": by_parent, "by_child": by_child, "notation": notation,
        "sysph": sysph, "allophones": allophones, "conflicts": find_conflicts(corrs, sysph), "entered_pairs": entered_pairs,
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
