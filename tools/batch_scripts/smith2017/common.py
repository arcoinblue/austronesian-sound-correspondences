"""Row builders shared by the Borneo batches."""
import re
from collections import defaultdict
from lib import compose, label, split_cell, ipa, NFC

LECT_COLS = ["id", "name", "alt_names", "type", "glottocode", "iso639_3", "parent_id", "subgroup_path", "region",
             "orthography_note", "notes", "default_system", "systems", "clade", "competes_with", "latitude",
             "longitude", "overlap_groups", "inherit", "language_id", "alt_parents", "inherit_source_id",
             "inherit_page", "inherit_note"]

DEC_SEMICOLON = "smith-semicolon"
DEC_VOWELS = "smith-many-reflexes"


def lect(b, id, name, type, parent="", **kw):
    r = {c: "" for c in LECT_COLS}
    r.update(id=id, name=name, type=type, parent_id=parent)
    r.update(kw)
    b.lects.append(r)
    return r


def decision(id, question, chosen, alternatives, src, page, batch="", notes=""):
    return {"id": id, "batch": batch, "question": question, "chosen_reading": chosen,
            "alternatives": alternatives, "status": "open", "source_id": src, "page": page, "notes": notes}


def add_general_decisions(b):
    b.decisions.append(decision(DEC_SEMICOLON,
        "Smith's tables list several reflexes in a cell: 'the first listed reflex is the regular reflex, and the "
        "reflex(es) appearing after the semi-colon are conditioned or irregular' (2017a: 52). Some cells use "
        "commas instead.",
        "First reflex: regular. After a semicolon: sporadic, unless the text states a condition (then regular "
        "with that environment). After a comma: regular, conditions not given. A cell with three or more "
        "reflexes and no conditions in the text: only the first is entered, and the row's as_printed keeps the "
        "whole cell.",
        "enter every reflex as regular with conditions unknown; or enter only the first", "smith2017a", "52"))
    b.decisions.append(decision("smith-higher-order",
        "Smith's higher-order groupings: North Borneo, Greater North Borneo, Central Sarawak, Punan-Müller-Schwaner, "
        "North Sarawak, Basap-Barito, Western Indonesian (2017a ch. 3); Late Malayo-Polynesian (2025).",
        "Not entered as nodes. They rest mainly on lexical innovations, which Smith himself later rejects as "
        "subgrouping evidence for Greater North Borneo and Barito-Basap (2023). Each low-level proto-language "
        "is entered directly under PMP.",
        "enter Greater North Borneo and North Borneo as nodes", "smith2017a", "260-391"))


def norm_env(env, pos, vowel):
    """Smith's '_k,ŋ' > '_[k,ŋ]#' (a vowel of the final closed syllable), 'u,i_' > '[u,i]_'."""
    env = env.strip().replace(" ", "")
    env = re.sub(r"(?<![\[,])([^_\[\]#]+(?:,[^_\[\]#,]+)+)", lambda m: "[" + m.group(1) + "]", env)
    if vowel and pos == "_C#" and env.startswith("_") and not env.endswith("#"):
        env += "#"
    if not vowel and pos == "_#" and env.endswith("_"):
        env += "#"
    return env


def _strip(cell):
    """Phonetic detail in square brackets is left out ('e [e; ɛ]' is e)."""
    return re.sub(r"\s*\[[^\]]*\]", "", cell).strip()


def add_language_rows(b, nodes, chains, langs, parent_node, table, src, page, locator, clusters=None,
                      final_glottal=False, conditioned=None, expand=None, strip_cluster_nasal=False,
                      strip_final_glottal_note=False, many_ok=False, proto_cond=None):
    clusters, conditioned, expand = clusters or {}, conditioned or {}, expand or {}
    for lab, cells in table:
        cols = cells.split("|")
        for L, cell in zip(langs, cols):
            cell = cell.strip()
            if not cell:
                continue
            if (L, lab) in expand:
                for par, ch, env, st, note in expand[(L, lab)]:
                    if ch == par and st == "regular" and env != "penultimate syllable":
                        pass
                    b.corr(L, par, ipa(ch), env, src, page, status=st, notes=note, locator=locator,
                           as_printed=f"{lab} > {cell}", decision=DEC_SEMICOLON if ";" in cell else "")
                continue
            printed = f"{lab} > {cell}"
            body = lab.lstrip("*").strip("-")
            diph = body in ("ay", "aw", "iw", "uy")
            if lab in clusters:
                par, env = clusters[lab]
                vowel = False
            elif diph:
                v, g = body[0], body[1]
                pa = compose(nodes, chains[parent_node], v, "_C#")
                pg = compose(nodes, chains[parent_node], g, "_#")
                par, env, vowel = None, None, True
            else:
                ph, env = label(lab)
                vowel = ph in "aiuə"
                if ph == "ə":
                    ph = "e"          # PMP schwa is keyed e
                par = compose(nodes, chains[parent_node], ph, env)
                if par is None:
                    continue
            parts = split_cell(_strip(cell))
            single = len(parts) == 1
            extra = ""
            if len(parts) >= 3 and not many_ok and not any((L, lab, x) in conditioned for x, _ in parts[1:]):
                extra = ("The table also lists " + ", ".join(x for x, _ in parts[1:]) +
                         " without conditions; not entered (decision smith-semicolon).")
                parts = parts[:1]
            for x, kind in parts:
                note = []
                st = "regular"
                dec = ""
                if x == "?":
                    b.corr(L, par, "", env, src, page, status="", blank_type="not-attested", locator=locator,
                           as_printed=printed, notes="Printed '?': no reflex identified.")
                    continue
                if x.endswith("?"):
                    x = x[:-1].strip()
                    st_q = True
                else:
                    st_q = False
                if x.startswith("(") and x.endswith(")"):
                    x = x[1:-1]
                    kind = "semicolon"
                    note.append("In parentheses in the table.")
                if (final_glottal or strip_final_glottal_note) and vowel and env == "_#" and x.endswith("ʔ"):
                    x = x[:-1]
                    if final_glottal:
                        note.append("The final ʔ printed in the table is the glottal stop added after final "
                                    "vowels, entered at Proto-Kayan-Murik-Merap.")
                    else:
                        note.append("The final ʔ printed in the table is entered as an inserted glottal stop.")
                if strip_cluster_nasal and lab in clusters and len(x) == 2:
                    x = x[1]
                e = env
                cm = re.match(r"(.+?)\s*/\s*(\S*_\S*)$", x)
                if cm:
                    x, e = cm.group(1).strip(), norm_env(cm.group(2), env, vowel)
                    kind = "conditioned"
                    if proto_cond and (par, e) in proto_cond:
                        # the proto-node already made this conditioned change
                        if ipa(x) == proto_cond[(par, e)]:
                            continue
                if (L, lab, x) in conditioned:
                    e, cn = conditioned[(L, lab, x)]
                    note.append(cn)
                elif kind == "conditioned":
                    note.append("Conditioned as printed in the table.")
                elif kind == "semicolon":
                    st = "sporadic"
                    dec = DEC_SEMICOLON
                    note.append("Listed after a semicolon: 'conditioned or irregular' (Smith 2017a: 52); no "
                                "condition is given.")
                elif kind == "comma":
                    dec = DEC_SEMICOLON
                    note.append("Listed after a comma, with no condition given.")
                if kind == "first" and extra:
                    note.append(extra)
                    dec = DEC_SEMICOLON
                if st_q:
                    st = "disputed"
                    note.append("Printed with a question mark.")
                final_c = (not vowel) and env == "_#"
                if diph:
                    if strip_final_glottal_note and x.endswith("ʔ"):
                        x = x[:-1]
                        note.append("The final ʔ printed in the table is entered as an inserted glottal stop.")
                    if x == body:
                        continue
                    child = ipa(x)
                    b.corr(L, pa, child, f"_+{pg}", src, page, status=st, notes=" ".join(note), locator=locator,
                           as_printed=printed, decision=dec, source_form=x if child != x else "")
                    b.corr(L, pg, child, f"{pa}+_", src, page, status=st, notes=" ".join(note), locator=locator,
                           as_printed=printed, decision=dec, source_form=x if child != x else "")
                    continue
                child = "∅" if x in ("Ø", "ø") else ipa(x, final=final_c)
                if child == par and single and kind == "first" and not st_q:
                    continue        # a single unchanged reflex: covered by the lect's inherit
                if child == ipa(par):
                    note.append("Same sound: the attested form is written in IPA.")
                b.corr(L, par, child, e, src, page, status=st, notes=" ".join(note), locator=locator,
                       as_printed=printed, decision=dec, source_form=x if (child != x and child != "∅") else "")


PMP_C = list("pbtdkgqhszjmnlrRwy") + ["ñ", "ŋ"]
PMP_V = list("aiue")
POS_C = ("#_", "V_V", "_#")
POS_V = ("_#", "_C#", "penultimate syllable")


def occurrences(nodes, chain):
    occ = defaultdict(set)
    for ph in PMP_C:
        for pos in POS_C:
            if (ph == "j" and pos == "#_") or (ph == "z" and pos == "_#"):
                continue
            r = compose(nodes, chain, ph, pos)
            if r:
                occ[r].add(pos)
    for ph in PMP_V:
        for pos in POS_V:
            if ph == "e" and pos == "_#":
                continue        # no word-final schwa in PMP
            r = compose(nodes, chain, ph, pos)
            if r:
                occ[r].add(("V", pos))
    return occ


def _cls(env, vowel):
    """The position a row's environment fills completely. A conditioned final environment (a_#, i_#) is
    taken to be one of a full set; conditioned initial and medial ones (#_Vl, _C) leave the rest of the
    position to a retention."""
    if vowel:
        if env == "penultimate syllable":
            return ("V", "penultimate syllable")
        if env == "_#" or env.startswith("_# ("):
            return ("V", "_#")
        if env == "_C#":
            return ("V", "_C#")
        return None
    if env in ("#_", "V_V", "_#"):
        return env
    if env.endswith("_#") and not env.startswith("#"):
        return "_#"
    return None


def add_complements(b, langs, src, page, note, nodes=None, chains=None, parents=None, cite=None):
    """Where a lect's rows for a parent phoneme cover some positions only, the rest are stated retentions."""
    by = defaultdict(list)
    for r in b.corrs:
        if r["child_lect_id"] in langs and "+" not in r["environment"] and r["parent_phoneme"] != "∅":
            by[(r["child_lect_id"], r["parent_phoneme"])].append(r)
    for (L, P), rows in sorted(by.items()):
        if any(r["environment"] == "elsewhere" for r in rows):
            continue
        occ = parents[L][P] if parents else set()
        vowel = any(isinstance(o, tuple) for o in occ)
        covered = {_cls(r["environment"], vowel) for r in rows}
        for pos in sorted(occ, key=str):
            if pos in covered:
                continue
            env = pos[1] if isinstance(pos, tuple) else pos
            pg, nt = (cite or {}).get(L, (page, note))
            b.corr(L, P, P, env, src, pg, derivation="stated-retention", notes=nt)


RESPELL = {"g": ("ɡ", "Smith's g is IPA ɡ."), "j": ("d͡ʒ", "Smith writes j for [ʤ] (2017a: 26)."),
           "c": ("t͡ʃ", "Smith writes c for [ʧ] (2017a: 26)."), "ñ": ("ɲ", "Smith writes ñ for [ɲ] (2017a: 26)."),
           "y": ("j", "Smith writes y for [j] (2017a: 26)."),
           "z": ("d͡ʒ", "PMP *z is [ʤ] (Smith 2017a: 26).")}


def ipa_respell(b, langs, parents, src, page, j_is_affricate=False):
    """An attested lect continues a proto symbol that is not IPA (g, j, c, ñ, y): its retention rows get the
    IPA symbol, and where it has no row at all, one is added, so the lect's inventory is IPA."""
    for L in langs:
        occ = parents[L]
        rows = [r for r in b.corrs if r["child_lect_id"] == L]
        for sym, (ip, why) in RESPELL.items():
            if sym == "j" and not j_is_affricate:
                continue        # PMP *j [gʸ] kept: no IPA symbol is implied
            if sym not in occ:
                continue
            mine = [r for r in rows if r["parent_phoneme"] == sym]
            for r in mine:
                if r["child_phoneme"] == sym:
                    r["child_phoneme"] = ip
                    r["source_form"] = r["source_form"] or sym
                    r["notes"] = (r["notes"] + " " + why).strip()
            covered = any(r["environment"] == "elsewhere" for r in mine)
            if not covered and not mine:
                b.corr(L, sym, ip, "elsewhere", src, page, derivation="stated-retention", source_form=sym,
                       notes="Unchanged; written in IPA. " + why)
            elif not covered:
                # some positions changed: the remaining ones are retentions, respelled
                pass
