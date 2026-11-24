#!/usr/bin/env python3
"""Goodenough (1995), Proto-Micronesian palatals *L and *N.

PMc *L as a phoneme of a Goodenough system on PMc (the user's choice of 24 November 2026), its reflexes from
Tables 1-2 composed down the Bender et al. chain; the reflexes of *N (Table 3) as default-system rows.
"""
from common import Batch, write

S = "goodenough1995"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Goodenough, Ward H.", year="1995", title="Proto-Micronesian palatals *L and *N", kind="comparative",
    url_or_doi="https://www.jstor.org/stable/3623112",
    notes="Consulted directly on 24 November 2026 (JSTOR PDF in Downloads; Tables 1-3 read from page images). "
          "Table 1 is adapted from Jackson (1986: 202-203) with Goodenough's symbols; his *j (Table 1 only; "
          "discussion deferred to a separate paper, p. 73) has the reflexes of Bender et al.'s *Z.",
    pub_type="article", container_title="Oceanic Linguistics", volume="34", issue="1", pages="73-85"))
G = "Goodenough"
D = "goodenough1995-l"

# ---------------------------------------------------------------- the Goodenough system on PMc (Table 1, n. 2)
NM = "Table 1 (p. 74) and n. 2 (p. 83)."
import csv
from common import ROOT
FEAT = {r["ipa"]: (r["place"], r["manner"], r["voicing"]) for r in csv.DictReader(open(ROOT / "cldf" / "phonemes.csv"))
        if r["lect_id"] == "pmc"}
FEAT.update({"pʷ": ("bilabial", "plosive", "voiceless"), "mʷ": ("bilabial", "nasal", "voiced")})  # blank in phonemes.csv


def nm(lect, ph, sym, note="", page="74", system=G, place="", manner="", voicing=""):
    if lect == "pmc" and not place and ph in FEAT and sym != ph:
        place, manner, voicing = FEAT[ph]
    b.t["notation_map"].append(dict(lect_id=lect, phoneme=ph, system=system, symbol=sym, source_id=S, page=page,
                                    notes=note, place=place, manner=manner, voicing=voicing))
for ph, sym, note in [
    ("p", "p", ""), ("pʷ", "pw", ""), ("f", "f", ""), ("m", "m", ""), ("mʷ", "mw", ""), ("t", "t", ""),
    ("T", "c", "Jackson's (1986) T (Table 1 heading *c(T))."),
    ("c", "d", "Jackson's (1986) c (Table 1 heading *d(c))."),
    ("s", "s", "Jackson's (1986) d (Table 1 heading *s(d))."),
    ("S", "S", "Jackson's (1986) z (Table 1 heading *S(z))."),
    ("Z", "j", "A 'palatal spirant *j' (p. 73), whose evidence Goodenough leaves to a separate paper. Its reflexes in "
              "Table 1 (KSR s, PCMc *j, KIR r, PWMc *∅) are those of Bender et al.'s (2003a) *Z."),
    ("l", "l", ""), ("n", "n", ""), ("r", "r", ""), ("k", "k", ""), ("x", "x", ""),
    ("ŋ", "G", "Velar nasal (n. 2)."), ("ñ", "N", "Palatal nasal (n. 2)."), ("w", "w", ""),
    ("y", "y", "Added to Jackson's orthography (n. 2)."),
]:
    nm("pmc", ph, sym, note, page="74, 83" if "n. 2" in note else "74")
nm("pmc", "l", "L",
   "PMc *L, 'the PMc palatalized lateral' (n. 2), kept apart from *l by Chuukic and Kiribati, which lose *L "
   "and keep *l (Table 2). Four reasonably solid and four doubtful etyma (pp. 75-77: *GiLi 'buzz', "
   "*ma-[sS]aLu 'smooth', *pwuLu 'flow', *Lukuma 'bundle'; ? *Loo, *Luuwe, *paLu, *pweLe). Goodenough asks "
   "whether it continues a POc *L (with *GiLi, *GuLu behind Bugotu and Sa'a l beside r, pp. 78-79) but leaves it "
   "open; no POc *L is entered. Listed against *l, the default phoneme whose reflexes cover it (decision "
   "goodenough1995-l).", page="74-79, 83", place="palatal", manner="lateral-approximant", voicing="voiced")
for v, vn in (("i", "i"), ("e", "e"), ("a", "a"), ("o", "o"), ("u", "u")):
    nm("pmc", v, vn, "Vowel letters of the reconstructions (pp. 75-83); the paper gives no vowel table.", page="75-83")
# the intermediate nodes: *L in Goodenough's PCMc, PWMc and PTP rows of Table 1
for lect, label in (("pcmc", "PCMc"), ("pwmc", "PWMc"), ("ppc", "PTP"), ("ppon", "")):
    note = (f"*L of Goodenough's {label} row of Table 1 (p. 74)." if label else
            "Not in Goodenough's Table 1, which states Mokilese and Pohnpeian against PTP (PPC); carried down "
            "to keep his PON, MOK, PNG l (Table 2).")
    nm(lect, "L", "L", note + " Bender et al. (2003a) have no *L: it is part of their *l (decision goodenough1995-l).",
       system="canonical", page="74-75", place="palatal", manner="lateral-approximant", voicing="voiced")

# ---------------------------------------------------------------- *L rows (Tables 1-2)
C = "Goodenough states the reflexes against PMc (Table 2); restated here through his PCMc, PWMc and PTP *L (Table 1). "
def L(lect, child, env="elsewhere", notes="", system="", derivation="composed", page="74-75", printed=""):
    b.corr(lect, "L", child, env, page, (C if derivation else "") + notes, derivation=derivation, system=system,
           decision=D, as_printed=printed or f"*L > {child}", n="8" if lect == "kosr1238" else "")
L("kosr1238", "l", system=G, derivation="", page="74-77",
  notes="Ksr l (Table 2): *pwuLu > fuhl 'slip, drop', *paLu > pahpah, pahluh 'blow, fan', *Loo > loh 'found' (pp. 76-77).")
L("pcmc", "L", system=G, derivation="", printed="PCMc *L")
L("gilb1244", "∅", notes="Kiribati keeps *l as n (Table 2).")
L("pwmc", "L", printed="PWMc *L")
L("mars1254", "l", notes="Marshallese l (Table 2); *l has l, ļ, ļʷ (Table 1).")
L("ppc", "L", printed="PTP *L")
L("ppon", "L", printed="(no PPON row)")
for lang, nm_ in (("pohn1238", "PON"), ("moki1238", "MOK"), ("ping1243", "PNG")):
    L(lang, "l", notes=f"{nm_} l (Table 2).")
L("pck", "∅", "elsewhere", "PTk *∅/y (Table 2; Table 1 PTk *∅,y): every Chuukic language in Table 2 has ∅, and "
  "Chuukese ∅, y (Table 1). The conditions of y are not given.", printed="PTk *∅/y")
L("pck", "y", "conditions unknown", "Reconstructed in *pwuLu > PTk *pwuyu 'flow' (p. 77); see the ∅ row.",
  printed="PTk *∅/y")

# ---------------------------------------------------------------- *N (Table 3, §3)
CN = "Table 3 (p. 79) states PMc *N; restated here against the immediate parent through the rows of Bender et al. (2003a). "
def N(lect, child, env="elsewhere", notes="", status="regular", printed="", derivation="composed"):
    b.corr(lect, "ñ", child, env, "79-83", (CN if derivation else "Table 3 (p. 79). ") + notes, status=status,
           as_printed=printed or f"*N > {child}", n="18" if lect == "pck" else "", derivation=derivation)
N("pck", "ñ", notes="PTk *N 'was still present as a distinct phoneme in Proto-Trukic (PTk), at least in some "
  "environments' (p. 79): it raised a preceding *a and *e before merging with *n in the daughters.", printed="PTk *N,n")
N("pck", "n", "conditions unknown", "PTk *N, n (Table 3): merged with *n in some forms already (PTk *naamwu 'mosquito').",
  printed="PTk *N,n")
N("pohn1238", "j", "conditions unknown", "PON y, ∅ (Table 3; 'reflexes separated by a comma are the result of "
  "conditioned change', Table 1 note): *wooNu > weey 'turtle', *NaNau > iow 'delicious', *NaNoa > aio 'yesterday'.",
  printed="*N > y,∅")
N("pohn1238", "∅", notes="PON y, ∅ (Table 3): *-Na > -∅, *Naamwu > amwi-(se), *meNa-a > wia.", printed="*N > y,∅")
N("moki1238", "∅", printed="*N > ∅")
N("ping1243", "∅", printed="*N > ∅")
N("mars1254", "n", printed="*N > n")
N("gilb1244", "n", printed="*N > n")
N("kosr1238", "∅", notes="Ten possible Kosraean reflexes, five of them Jackson's (1983: 334) (p. 80).", printed="*N > ∅",
  derivation="")
RAISE = ("'In the Trukic languages PMc */N/ fell together with PMc */n/, but before doing so it raised a preceding short "
         "*/a/ to /e/ and a preceding short */e/ to /i/ in contrast to */n/' (p. 79): *NaNa 'taste' > Chk nnen, "
         "Mrt, Pul nennan; *meeNa 'thing' > Chk meen, mine-; *paNipaNi > Chk penipen. */N/ 'also fronted a "
         "following */o/ to /e/ in some of the Trukic languages' (*NaNoa > Chk nanew).")
b.corr("pck", "a", "e", "_ñ (short)", "79-82", RAISE, as_printed="*a > e / _*N", n="")
b.corr("pck", "e", "i", "_ñ (short)", "79-82", RAISE, as_printed="*e > i / _*N", n="")

b.dec(D, "Goodenough (1995) adds a PMc *L (palatalised lateral), split from *l. How is it entered?",
      "As a phoneme of a Goodenough system on PMc (the user's choice of 24 November 2026), listed against *l "
      "(notation_map.phoneme), with Goodenough's other PMc symbols as notation rows of the same system (his *j = "
      "Bender et al.'s *Z). Its reflexes are composed down Bender et al.'s chain: Goodenough's Table 1 has *L in "
      "PCMc, PWMc and PTP (= PPC), so PCMc, PWMc, PPC and PPON get *L as a reverse-generated phoneme with a "
      "canonical notation row (a reflex row always adds the reflex to the child's default inventory); Kiribati and "
      "PCK lose it (PCK *∅, y). lects.systems of pmc must read Bender;Goodenough before the batch is applied "
      "(sheet edit). POC *L (pp. 78-79) is only a note.",
      "Notes only, on PMc *l; or *L in the default PMc inventory.", "73-79")

md = """# goodenough1995-palatals

Goodenough, Ward H. 1995. Proto-Micronesian palatals *L and *N. *Oceanic Linguistics* 34(1). 73-85. Read from the JSTOR PDF in Downloads; Tables 1-3 from page images. Generator: `tools/batch_scripts/five_sources_2026_11_24/goodenough1995.py`.

## Before applying

Sheet edit, **done on 24 Nov 2026 at 23:35 KST**: `lects` row `pmc` (row 20), column `systems`: `Bender;Goodenough` (checked first: with no Goodenough rows yet this gives no error or warning). Without it the batch's Goodenough rows are errors; check that the next sync carried it to `cldf/lects.csv`.

## Scope

- **PMc *L** (Tables 1-2, §2): a phoneme of a new Goodenough system on PMc, listed against *l (decision `goodenough1995-l`, the user's choice). The system has Goodenough's symbols for every PMc phoneme of Table 1 (c = Bender's T, d = c, j = Z, G = ŋ, N = ñ) and the vowel letters of his reconstructions.
- *L reflexes composed down the chain of Bender et al. (2003a): PCMc, PWMc, PPC (his PTP) and PPON *L; Kosraean, Marshallese, Pohnpeian, Mokilese, Pingelapese l; Kiribati ∅; PCK ∅ and y.
- **PMc *N** (Table 3, §3): the reflexes, Pohnpeian y beside ∅, PCK *N beside *n, and the raising of *a, *e before *N in Trukic (entered at PCK, where Goodenough puts *N).

## Not entered

- Table 1 as a whole: it is Jackson's (1986) table in Goodenough's symbols (Jackson 1986 is entered from the original in batch `jackson1986-micronesian`). Its *j column is Bender et al.'s *Z.
- POC *L (pp. 78-79), the etymologies, Tanapag Carolinian (Crn) and Mapia.
- The fronting of *o after *N 'in some of the Trukic languages' (note on the raising rows).
"""
write("goodenough1995-palatals", b.t, md)
