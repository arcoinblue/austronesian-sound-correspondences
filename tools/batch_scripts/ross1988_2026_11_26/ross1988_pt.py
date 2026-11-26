#!/usr/bin/env python3
"""Ross (1988), chapter 6: the Papuan Tip cluster (Tables 28-30, pp. 198-206). Batch `ross1988-papuan-tip`.

Unlike the North New Guinea tables (batch ross1988-nng, rows composed POC > language), these rows are stated against
Proto-Papuan Tip (`ppt`), which is a node of the tree already and which Ross prints as a row of every table.
Table 30 goes through Proto Central Papuan (PCP), which is not a node: its rows are composed PPT > language.
"""
import csv
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "five_sources_2026_11_24"))
from common import Batch, write  # noqa: E402
from ross1988_lib import cells, to_ipa, ROUND, RAISE, LOW  # noqa: E402
import ross1988_pt_data as D  # noqa: E402

ROOT = HERE.parents[2]
S = "ross1988"
b = Batch(S)
DEC, DECL = "ross1988-ppt", "ross1988-pt-lects"
EXTRA = {"ɣw": "ɣʷ", "?w": "ʔʷ", "?o": "ʔo"}
# lects with a sourced inventory (Lynch et al. 2002 sketches): Ross's letters as that inventory writes them
LECT_EXTRA = {"gapa1238": {"v": "v", "r": "ɾ"}, "lala1268": {"v": "v"}}
G = {r["ID"]: r for r in csv.DictReader(open("/home/claude/glottolog_languages.csv", encoding="utf-8"))}
OLD = {r["id"]: r for r in csv.DictReader(open(ROOT / "cldf" / "lects.csv", encoding="utf-8"))}
SEEN = {}
COUNT = {}


def split_loan(cell):
    m = re.fullmatch(r"(.*?)\s*\((.*)\)", cell.strip())
    return (m.group(1).strip(), m.group(2).strip()) if m else (cell.strip(), "")


def emit(name, parents, cell, label, page, locator, grade=None, penv=None, pcp=None):
    lid = D.LECTS[name]["id"]
    main, loan = split_loan(cell)
    EX = {**EXTRA, **LECT_EXTRA.get(lid, {})}
    for part, status in ((main, "regular"), (loan, "loan-stratum")):
        for it in cells(part):
            child = to_ipa(it["letters"], EX)
            notes = []
            if ROUND in it["marks"]:
                notes.append("Superscript o: with rounding of the adjacent vowel.")
            if RAISE in it["marks"]:
                notes.append("Superscript i: with raising of the following vowel.")
            alts = [x for x in dict.fromkeys(to_ipa(a, EX) for a in it["alts"]) if x != child]
            if alts:
                notes.append("Alternates with " + ", ".join(alts) + " in the same environments (Ross's comma).")
            if status == "loan-stratum":
                notes.append("Ross's bracketed reflex: indirectly inherited, through borrowing (pp. 7, 197).")
            env = it["env"]
            unknown = it["unknown"]
            if unknown:
                env = "conditions unknown" if env == "elsewhere" else env + ", conditions unknown"
            extras = [x for x in (penv, grade and grade + " grade") if x]
            if extras:
                env = ", ".join(extras) if env == "elsewhere" else f"{env} ({', '.join(extras)})"
            printed = f"{label} > " + (f"PCP {pcp} > " if pcp else "") + f"{name} {cell}"
            for par in parents:
                key = (lid, par, child, env, status)
                if key in SEEN:
                    prev = SEEN[key]
                    extra = " ".join(n for n in notes if n.startswith("Superscript"))
                    if extra and extra not in prev["notes"]:
                        prev["notes"] = (prev["notes"] + " Also printed with the superscript: " + extra).strip()
                    if printed not in prev["as_printed"]:
                        prev["as_printed"] += " | " + printed
                    continue
                b.corr(lid, par, child, env, page, " ".join(notes), status=status,
                       derivation="composed" if pcp else "", as_printed=printed,
                       source_form=it["letters"] if it["letters"] not in (child, "0") else "",
                       decision=DEC, locator=locator, conditioning="unknown" if unknown else "")
                SEEN[key] = b.t["correspondences"][-1]
                COUNT[name] = COUNT.get(name, 0) + 1


def parse(block, ncols):
    out = {}
    for line in block.strip().split("\n"):
        f = [x.strip() for x in line.split("|")]
        if len(f) != ncols + 1:
            raise SystemExit(f"{f[0]}: {len(f) - 1} cells for {ncols} columns")
        out[f[0]] = f[1:]
    return out


def graded(name, cols, row, page, locator, pcp=None):
    """cols: (label, parent, grade). The fortis and lenis cells of *s are one row set when they are the same."""
    gi = {c[2]: i for i, c in enumerate(cols) if c[2]}
    same = gi and row[gi["fortis"]] == row[gi["lenis"]]
    for i, ((label, par, grade), cell) in enumerate(zip(cols, row)):
        if grade and same:
            if grade == "lenis":
                continue
            emit(name, [par], cell, "PPT *s fortis and lenis (POC *s, *c)", page, locator)
        else:
            emit(name, [par], cell, label, page, locator, grade=grade)


# Table 28
start = 0
for (n, page), block in zip(D.T28_PAGES, D.T28):
    cols = D.T28_COLS[start:start + n]
    for name, row in parse(block, n).items():
        graded(name, cols, row, page, "Table 28")
    start += n
# Table 29
LABEL = {c[1] + (":" + c[2] if c[2] else ""): c[0] for c in D.T28_COLS}
LABEL["q"] = "PPT *q (POC *k lenis, *q)"
for pars, page, block in D.T29_BLOCKS:
    cols = []
    seen_q = 0
    for p in pars:
        par, _, grade = p.partition(":")
        label = LABEL[p]
        if par == "q":
            label = ("PPT *q- (POC *k lenis, *q)", "PPT *-q- (POC *k lenis, *q)")[seen_q]
            seen_q += 1
        cols.append((label, par, grade or None))
    for name, row in parse(block, len(cols)).items():
        graded(name, cols, row, page, "Table 29")
# Table 30
for specs, page, block in D.T30_BLOCKS:
    for name, row in parse(block, len(specs)).items():
        for spec, cell in zip(specs, row):
            pars = spec[0].split()
            penv = spec[2] if len(spec) > 2 else None
            label = "PPT " + ", ".join("*" + {"ɡ": "g", "mʷ": "mw", "kʷ": "kw", "ɡʷ": "gw"}.get(p, p) for p in pars)
            emit(name, pars, cell, label, page, "Table 30", penv=penv, pcp=spec[1])

# POC > PPT (p. 196, innovations A-G, and the POC and PPT rows of Table 28)
PPT = [
    ("p", "p", "fortis grade", "D. POC *p split into (fortis) PPT *p and (lenis) PPT *v, with all languages agreeing on "
     "their reflex of POC *p in a given item. PPT *v occurs far more often than PPT *p."),
    ("p", "v", "lenis grade", "D. POC *p split into (fortis) PPT *p and (lenis) PPT *v"),
    ("R", "r", "elsewhere", "A. POC *r and *R merged as PPT *r."),
    ("dr", "d", "elsewhere", "B. POC *d and *dr merged as PPT *d."),
    ("c", "s", "elsewhere", "C. POC *s and *c merged as PPT *s."),
]
for par, child, env, printed in PPT:
    b.corr("ppt", par, child, env, "196", "The grade of a given item is not predictable (p. 196)." if "grade" in env
           else "", derivation="", as_printed=printed, decision=DEC, locator="§6.2.1",
           conditioning="lexical" if "grade" in env else "")
b.t["phonemes"].append(dict(
    lect_id="ppt", ipa="ɡʷ", source_symbol="gw", **{"class": "C"}, place="labial-velar", manner="plosive",
    voicing="voiced", origin="manual-add", source_id=S, page="202",
    reason="PPT *gw of Ross (1988: Tables 28-30), with no POC source (the POC row has a dot); the daughters' rows "
           "need it."))

# lects
def lect(name, info, loc, pages, group, rows=True):
    lid, gc = info["id"], info["glottocode"]
    g = G.get(gc) if gc else None
    if gc and not g:
        raise SystemExit(f"{name}: {gc} not in Glottolog")
    own = g and g["ID"] == lid
    if rows:
        notes = (f"{group} (Ross 1988: 191-192). Consonant reflexes of Proto-Papuan Tip from {loc} of Ross "
                 f"(1988: {pages})" + (", composed through his Proto Central Papuan, which is not a node here"
                                       if loc == "Table 30" else "") +
                 f" (decision {DEC}). Ross writes every language in one orthography (pp. 3-4), mapped to IPA here. "
                 "No vowels: Ross tabulates consonants only (p. 6).")
    else:
        notes = f"{group}. No rows of its own: its varieties in {loc} of Ross (1988: {pages}) are its dialects."
    if g:
        notes += " Coordinates from Glottolog 5.4."
    if info.get("note"):
        notes += " " + info["note"]
    b.t["lects"].append(dict(
        id=lid, name=info.get("name") or name, alt_names=info.get("alt_names", ""), type=info["type"], glottocode=gc,
        iso639_3=(g["ISO639P3code"] if g and info["type"] == "language" and own else ""), parent_id="ppt",
        language_id=info.get("language_id", ""), representative=info.get("representative", ""),
        latitude=g["Latitude"] if g else "", longitude=g["Longitude"] if g else "", notes=notes))


CP = "Peripheral Papuan Tip network: Central Papuan family"
TAB = {}
for (n, page), block in zip(D.T28_PAGES[:1], D.T28[:1]):
    for name in parse(block, n):
        TAB[name] = ("Table 28", "198-202")
for name in parse(D.T29_BLOCKS[0][2], 6):
    TAB[name] = ("Table 29", "203-204")
for name in parse(D.T30_BLOCKS[0][2], 8):
    TAB[name] = ("Table 30", "205-206")
done = set()
for name, info in D.LECTS.items():
    loc, pages = TAB[name]
    group = D.SUBGROUP.get(name, CP)
    lang = info["language_id"]
    if lang and lang not in OLD and lang not in done and lang in D.GROUPS:
        gname, rep = D.GROUPS[lang]
        lect(gname, dict(id=lang, glottocode=lang, type="language", representative=rep, name=gname), loc, pages, group,
             rows=False)
        done.add(lang)
    if info["id"] in OLD:
        continue
    if not COUNT.get(name):
        raise SystemExit(f"{name}: no rows")
    lect(name, info, loc, pages, group)

b.dec(DEC, "Ross (1988) prints the Papuan Tip consonant correspondences (Tables 28-30) as POC > PPT > language, and "
           "for the Central Papuan family as POC > PPT > PCP > language. Against which stage are the rows stated?",
      "Against Proto-Papuan Tip (ppt), an established node already in the tree, with PPT in the sheet's Oceanic "
      "spelling (*bw bʷ, *mw mʷ, *pw pʷ, *kw kʷ, *gw ɡʷ, *g ɡ); the rows are direct, not composed. POC > PPT: the "
      "mergers and the split of *p into *p and *v (p. 196) are added; the split of *k and the merger of *ñ were "
      "already entered from Lynch et al. (2002). PPT *gw has no POC source and is a manual-add phoneme; PPT *pw and "
      "*kw, for which Ross (1988) prints no POC source either, continue the sheet's POc *pʷ and *kʷ. PPT *s fortis "
      "and lenis are one phoneme, the grade named in the environment when the two cells differ. Proto Central Papuan "
      "(Table 30) is held back like Ross's other intermediate reconstructions (decision ross1988-composition): the "
      "Central Papuan rows are composed PPT > language with the PCP value in as_printed, and the column POC *Ø- "
      "(PCP *y before *a) is not entered. A bracketed reflex is a loan-stratum row. Hyphens, ';', ',' and the "
      "superscripts as in ross1988-composition. Not entered: Wedau and Taupota *y, printed as a small capital D "
      "(p. 200); Table 31 (a postposition, not a correspondence).",
      "Compose every row POC > language as in the North New Guinea batch; or add Proto Central Papuan as a node.",
      "196-206")
b.dec(DECL, "How are Ross's (1988) Papuan Tip language names matched to Glottolog and to lects?",
      "By Ross's own equations (Figures 7-8: Paiwa = Gapapaiwa, Kukuya = Minaveha, Gumasi = Gumawana, Kakabai = "
      "Igora; Lala = Nara, p. 190) and Glottolog 5.4 and Ross et al. (2023): Boianaki = Ghayavi, Garuwahi = Gweda, "
      "Kalokalo = Koluwawa, Yamalele = Iamalele, Bosilewa = Boselewa, Kurada = 'Auhelawa, Tubetube = Bwanabwana, "
      "Bohutu = Buhutu, Gabadi = Abadi, Doura = Toura (tour1243), Bina = bina1271. Dialects under their language: "
      "Arifama and Miniafia (Arifama-Miniafia), Kwato and Daui (Suau), Iwa and Gawa (Muyuw, whose own row is the "
      "language's), Madawa, Pamela and Varavarae (Sudest), West Mekeo (Mekeo), Balawaia and Taboro (Sinaugoro), "
      "Aroma (Keapara); Hula is a language, as in Glottolog. Dialects with no Glottolog code share the language's "
      "(Kwato, Gawa, Madawa, Varavarae). Fagululu is not identified (no glottocode). All are under ppt; Ross's "
      "networks and chains (Figures 6-9) are in the notes, not nodes.",
      "Other matches; network and chain nodes below PPT.", "190-192, 203, 205")

md = f"""# ross1988-papuan-tip

Ross, Malcolm D. 1988. *Proto Oceanic and the Austronesian languages of western Melanesia* (Pacific Linguistics C-98). Chapter 6, Tables 28-30 (pp. 198-206), transcribed cell by cell from page images of the PDF in Downloads. Generator: `tools/batch_scripts/ross1988_2026_11_26/ross1988_pt.py`, data in `ross1988_pt_data.py`, Ross's cell notation in `five_sources_2026_11_24/ross1988_lib.py`.

- Table 28, Nuclear Papuan Tip network (34 varieties); Table 29, Kilivila/Louisiades network (11); Table 30, Central Papuan family (16).
- Rows are stated against Proto-Papuan Tip (decision `{DEC}`); Table 30 is composed through Proto Central Papuan.
- Lects: decision `{DECL}`. Existing lects that get rows: Gapapaiwa (Ross's Paiwa), 'Ala'ala (Lala). Sudest keeps no rows of its own: its three varieties are new dialect lects.

## Sheet edit after the batch

`lects` row `sude1239`: `representative` = `sudest-madawa` (the language now has dialects and no rows of its own).

## Not entered

- Wedau and Taupota *y (printed as a small capital D, p. 200).
- Table 30, the column POC *Ø- (PCP *y before *a).
- Table 31 (reflexes of the PPT postposition *[i]ai): morphology.
- Vowels (Ross tabulates consonants only).
"""
write("ross1988-papuan-tip", b.t, md)
print("rows", len(b.t["correspondences"]), "lects", len(b.t["lects"]))
