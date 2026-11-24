"""François (2005), Appendix 1, entered again after the user's reading of 24 November 2026
(decision francois2005-hybridization, reverted): 'fusion if different from any of the input vowels;
change and loss if identical with either vowel'.

A cell *V1(C)V2 > V' with the posttonic vowel lost:
- V' is neither *V1 nor *V2: a fusion pair, *V1 > V' / _+V2 and *V2 > V' / V1+_;
- V' is *V1 or *V2: *V1 > V' / _(C)V2 (a retention when V' = *V1) and the loss *V2 > ∅ after *V1.
A cell where the posttonic vowel survives as a final vowel (X_Y) is entered as before.

The charts are those of tools/batch_scripts/new_sources_2026_11_23/francois2005.py (read from the
page images on 23 November 2026); this module reads them from that file. Rows keep the ids of the
rows they replace, in order, so that the sheet's rows are edited in place.
"""
from pathlib import Path

OLD = Path(__file__).resolve().parents[1] / "new_sources_2026_11_23" / "francois2005.py"
DEC = "francois2005-hybridization"
ALT = "One of several regular reflexes of this sequence, with no stated condition."
FUS = ("Vowel hybridization: the stressed and the posttonic vowel give one vowel that is neither of them "
       "(pp. 449-451, 489), entered as a fusion.")
LOSS = ("The posttonic vowel is lost; the outcome is one of the two input vowels, so this is entered as a change of the "
        "stressed vowel and a loss, not as a fusion (pp. 449-451, 489).")


def charts():
    src = OLD.read_text(encoding="utf-8")
    src = src[:src.index("rows = []")].replace("from common import write", "")
    ns = {}
    exec(compile(src, str(OLD), "exec"), ns)
    return ns


def generate():
    ns = charts()
    L, PAGE, CH, RESPELL, PRINTED, V, S, G = (ns[k] for k in ("L", "PAGE", "CH", "RESPELL", "PRINTED", "V", "S", "G"))
    out = {}
    for code, chart in CH.items():
        rows, seen = [], set()

        def add(parent, child, env, alt, printed, notes="", sf=""):
            if (parent, child, env) in seen:
                return
            seen.add((parent, child, env))
            child2 = RESPELL.get(code, {}).get(child, child)
            if child2 != child and not sf:
                sf = child
            if child in PRINTED and not sf:
                sf = PRINTED[child]
            r = dict(child_lect_id=L[code], parent_phoneme=parent, child_phoneme=child2, environment=env,
                     status="regular", conditioning="unknown" if alt else "", source_id=S, page=PAGE[code],
                     locator="Appendix 1", as_printed=printed, source_form=sf, notes=notes, decision=DEC)
            if code == "SAK":
                r.update(source_id=G, page="", via_source_id=S, via_page="491", locator="",
                         via_note="Reproduced by François as the 18th chart of Appendix 1, in his notation.")
            rows.append(r)

        lost = {v2: [] for v2 in V}
        for i, v1 in enumerate(V):
            cells = [c.strip() for c in chart[i].split("|")]
            for j, v2 in enumerate(V):
                cell = cells[j]
                if cell in ("?", "-"):
                    continue
                alts = cell.split(";")
                n_cons = len([a for a in alts if not a.startswith("<")])
                printed = f"*{v1}(C){v2} > {cell.replace(';', ' || ')}"
                for a in alts:
                    adjacent = a.startswith("<")
                    a = a.strip("<>")
                    dag = a.endswith("†")
                    a = a.rstrip("†")
                    env1 = f"_{v2} (adjacent)" if adjacent else f"_(C){v2}"
                    env2 = f"{v1}_ (adjacent)" if adjacent else f"{v1}(C)_"
                    alt = (not adjacent) and n_cons > 1
                    note = ALT if alt else ""
                    if adjacent:
                        note = ("The sequence of two adjacent vowels *V1V2 (angled brackets), which did not hybridize as "
                                "*V1CV2 did.")
                    if dag:
                        note = (note + " The reflex ɪ of *a…i and *a…u occurs only in word-internal syllables "
                                       "(Appendix 1, note; §5.1.2.1).").strip()
                    x, y = a.split("_", 1) if "_" in a else (a, "")
                    survives = "_" in a and y != ""
                    glides = [""]
                    if x.startswith("(") and code == "LTG":   # (i)ɛ: ɛ or the diphthong i͡ɛ
                        glides, x = ["", x[1]], x[3:]
                    if code == "MTA" and x.startswith("("):    # (i)_e: the stressed vowel may be lost
                        x = x.strip("()")
                        opt = "The stressed vowel is optional before a non-high posttonic vowel (parentheses)."
                        add(v1, x, env1, True, printed, opt)
                        add(v1, "∅", env1, True, printed, opt)
                        add(v2, y, env2, False, printed, "The posttonic vowel survives as a final vowel Vf (*V1(C)V2 > *V'(C)Vf).")
                        continue
                    for g in glides:
                        out_v = f"{g}͡{x}" if g else x
                        gnote = (note + f" Printed ({g}){x}: {x} with an optional on-glide, the diphthong {g}͡{x} of "
                                        "Table 1.").strip() if g else note
                        many = alt or len(glides) > 1
                        if survives:
                            add(v1, out_v, env1, many, printed, gnote)
                            continue
                        shown = RESPELL.get(code, {}).get(out_v, out_v)
                        if shown not in (v1, v2):
                            # A new vowel: the two fuse. An adjacent sequence with the same outcome is the same pair.
                            where = " In the adjacent sequence *V1V2 (angled brackets)." if adjacent else ""
                            add(v1, out_v, f"_+{v2}", many, printed, (FUS + where + (" " + gnote if gnote and not adjacent else "")).strip())
                            add(v2, out_v, f"{v1}+_", many, printed, (FUS + where + (" " + gnote if gnote and not adjacent else "")).strip())
                        else:
                            add(v1, out_v, env1, many, printed, gnote)
                            k = f"{v1}{'' if adjacent else '(C)'}"
                            if k not in lost[v2]:
                                lost[v2].append(k)
                    if survives:
                        add(v2, y, env2, False, printed, "The posttonic vowel survives as a final vowel Vf (*V1(C)V2 > *V'(C)Vf).")
        for v2, after in lost.items():
            if after:
                add(v2, "∅", "posttonic, after " + ", ".join(f"*{a}" for a in after), False, f"*V1(C){v2} > V'(C)", LOSS)
        out[L[code]] = rows
    return out


def apply(T):
    new = generate()
    old = {}
    for r in T.rows("correspondences", decision=DEC):
        if r["child_lect_id"] != "pncv":
            old.setdefault(r["child_lect_id"], []).append(r)
    assert set(old) == set(new), set(old) ^ set(new)
    n = fus = dele = 0
    for lect, rows in new.items():
        olds = old[lect]
        for k, r in enumerate(rows):
            fus += "+" in r["environment"]
            n += 1
            if k < len(olds):
                blank = {c: "" for c in T.header["correspondences"] if c != "id"}
                T.set(olds[k], **{**blank, **r})
            else:
                T.add("correspondences", id=f"{lect}-fr05b-{k + 1}", **r)
        for r in olds[len(rows):]:
            T.delete(r)
            dele += 1
    return dict(rows=n, fusions=fus, deleted=dele)
