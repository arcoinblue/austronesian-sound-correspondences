#!/usr/bin/env python3
"""Tawerilmang & Sohn (1984), Proto-Oceanic reflexes in Woleaian.

Inventory (4), p. 175, as the sourced Woleaian inventory; allophones (SR 7, p. 177-178); diachronic rules
DR 1-15 (pp. 179-190, summary (39) pp. 191-192) composed to PCK > Woleaian (decision mc1984-composition).
"""
from common import Batch, write

S = "tawerilmangsohn1984"
L = "wole1240"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Tawerilmang, Anthony F.; Sohn, Ho-min", year="1984", title="Proto-Oceanic reflexes in Woleaian",
    url_or_doi="https://doi.org/10.15144/PL-C80.171", kind="comparative",
    notes="Consulted directly on 24 November 2026 (sealang.net scan; inventory and rule statements read from page "
          "images). Woleai Atoll dialect (Tawerilmang's own). Diachronic rules derive Woleaian base forms from POC "
          "(Grace 1969); synchronic rules derive surface forms from base forms (pp. 171-173).",
    pub_type="chapter", container_title="Studies in Micronesian linguistics", editors="Byron W. Bender",
    pages="171-199", place="Canberra", publisher="The Australian National University",
    series="Pacific Linguistics C-80"))

INV = "Phonological inventory of the native vocabulary (4), p. 175. "
for ipa, pl, mn, vo, sym, note in [
    ("p", "bilabial", "plosive", "voiceless", "p", ""),
    ("pʷ", "bilabial", "plosive", "voiceless", "pw", "Occurs only doubled in native words (the fortis counterpart of b)."),
    ("ɸ", "bilabial", "fricative", "voiceless", "b", "Occurs only singly in native words. Written b; ɸ as in the rows of Jackson (1983). Jackson (1984: 261) gives [βʷ]."),
    ("f", "labiodental", "fricative", "voiceless", "f", "Not in the chart (4), but the regular reflex of POC *p (DR 5, p. 182) and frequent in the cited forms (fale, fisi)."),
    ("t", "alveolar", "plosive", "voiceless", "t", ""),
    ("s", "alveolar", "fricative", "voiceless", "s", ""),
    ("ʈ͡ʂ", "retroflex", "affricate", "voiceless", "c", "Occurs only doubled in native words (the fortis counterpart of š and r)."),
    ("ʂ", "retroflex", "fricative", "voiceless", "š", "Occurs only singly in native words; Jackson's (1984) sh [ʃ̣]."),
    ("r", "alveolar", "trill", "voiced", "r", "Occurs only singly in native words."),
    ("k", "velar", "plosive", "voiceless", "k", "Occurs only doubled in native words (the fortis counterpart of x)."),
    ("x", "velar", "fricative", "voiceless", "x", "Occurs only singly in native words."),
    ("m", "bilabial", "nasal", "voiced", "m", ""),
    ("mʷ", "bilabial", "nasal", "voiced", "mw", ""),
    ("n", "alveolar", "nasal", "voiced", "n", "Occurs only doubled in native words (the fortis counterpart of l)."),
    ("ŋ", "velar", "nasal", "voiced", "ŋ", ""),
    ("l", "alveolar", "lateral-approximant", "voiced", "l", "Occurs only singly in native words."),
    ("j", "palatal", "approximant", "voiced", "y", "Semivowel."),
    ("w", "labial-velar", "approximant", "voiced", "w", "Semivowel."),
]:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="173-175", notes=INV + note +
         (" In native vocabulary the single and double members of b/pw, š/c, r/c, x/k, l/n are in complementary "
          "distribution; loans (largely Japanese) have made them contrast (pp. 173-174)." if ipa in {"pʷ", "ɸ", "ʈ͡ʂ", "ʂ", "r", "k", "x", "n", "l"} else ""))
for v, pl, mn, rd, sym, note in [
    ("i", "front", "close", "unrounded", "i", ""),
    ("ɨ", "central", "close", "unrounded", "ů", "High central vowel, from POC *u by DR 2 (p. 180); rounding not stated."),
    ("u", "back", "close", "rounded", "u", ""),
    ("e", "front", "mid", "unrounded", "e", ""),
    ("o", "back", "mid", "rounded", "o", ""),
    ("a", "central", "open", "unrounded", "a", ""),
    ("aː", "central", "open", "unrounded", "aa", "Long a. Not in the chart (4), which lists only the long vowels without short counterparts; base forms such as faa 'stone', saa 'leaf' have it (p. 181)."),
    ("əː", "central", "mid", "unrounded", "əə", "Long only (from vowel fusion, p. 181)."),
    ("ɔː", "back", "open-mid", "rounded", "ɔɔ", "Long only (from vowel fusion, p. 181)."),
]:
    b.ph(L, v, "V", pl, mn, "", rd, sym=sym, page="175", notes=(INV + note).strip())

b.allo(L, "e", "ə", "before or after ɨ", "177", "'e is pronounced with the lips rounded (i.e. [ə]) before or after ů' (p. 177).")
for v in ("i", "ɨ", "u", "e", "o", "a"):
    b.allo(L, v, v + "̥", "after a consonant or glide, before a phrase boundary", "178",
           "SR 7, vowel devoicing: a simple vowel after a consonant or semivowel is devoiced before a phrase boundary; a long vowel is shortened there.")

C = ("Stated against POC (§4, DR 1-15; summary (39), pp. 191-192); restated against PCK through the POc > PMc > ... "
     "> PCK rows of Bender et al. (2003a). ")
D = "mc1984-composition"


def r(par, child, env, page, printed, notes="", status="regular", n="", sf="", cond=""):
    b.corr(L, par, child, env, page, C + notes, status=status, n=n, as_printed=printed, source_form=sf, decision=D,
           conditioning=cond)


r("f", "f", "elsewhere", "182", "DR 5: *p > f / elsewhere",
  "*p > ∅ before a POC back vowel (*u, *o) is the PMc loss before round vowels of Bender et al.")
r("f", "p", "conditions unknown", "183", "*p > p", "*tupa > supa, *Ripa > repa (p. 183).", status="sporadic", n=2)
r("pʷ", "ɸ", "elsewhere", "183", "DR 6: *mp, *ŋp > b / _*u, *o",
  "Before a round vowel, where PMc has *pʷ (Bender et al.); *mpua > bbua (geminate) 'for reasons not statable'.", sf="b")
r("pʷ", "pʷ", "geminate", "173-174, 178", "SR 9: b + b > ppw", "Fortition of doubled b.")
r("p", "p", "elsewhere", "183", "DR 6: *mp > p / elsewhere")
r("t", "t", "_a", "183-184", "DR 7: *t > t / _*a")
r("t", "s", "elsewhere", "183-184", "DR 7: *t > s / elsewhere",
  "'Predominantly s'; exceptions *puti > utu, *kato > xato keep t (p. 184).")
r("t", "∅", "_u", "183-184", "DR 7: *t > ∅ / _*u (only in certain words)",
  "Perhaps loans from or influence of other Trukic languages (p. 184): fasů ~ faů 'stone'.", cond="lexical")
r("T", "s", "elsewhere", "183-184", "DR 7: *t > s / elsewhere", "PCK *T is POC *t before a non-low vowel (Bender et al.).")
r("T", "∅", "_u", "183-184", "DR 7: *t > ∅ / _*u (only in certain words)", cond="lexical")
r("c", "ʂ", "elsewhere", "184-185", "DR 8: *nt, *nd > š", sf="š")
r("c", "ʈ͡ʂ", "geminate", "184-185, 191", "š (cc when doubled)", sf="cc")
r("k", "x", "elsewhere", "185", "DR 9: simple *k, *ŋk > x",
  "*ŋk > x has one example (*ŋkiniti > xili-), which does not fit Bender et al., in whose chain POc *ŋk is PMc *x, lost in PCK.")
r("k", "k", "geminate", "185, 191", "*kk > kk; x (kk when doubled)")
r("r", "r", "elsewhere", "186", "DR 10: *d, *r > r",
  "POC *R > r or ∅ (DR 11, 'more examples favour loss') is the PMc split of Bender et al.")
r("r", "ʈ͡ʂ", "geminate", "186, 191", "r (cc when doubled)", sf="cc")
r("r", "ʂ", "conditions unknown", "186", "*d > š", "*(dr)odo > rošo, *(dl)iki > šixi; perhaps *nd (p. 186).",
  status="sporadic", n=2, sf="š")
r("d", "t", "elsewhere", "187", "DR 13: *ns, *s > t",
  "Some exceptions show š or ∅ (32), perhaps Trukic loans (p. 188). POC *nj > ∅ in one example.")
r("l", "l", "elsewhere", "188-189", "DR 14: simple *l, *n > l")
r("n", "l", "elsewhere", "188-189", "DR 14: simple *l, *n > l")
r("n", "n", "geminate", "188", "DR 14: *n retained only when geminate")
r("l", "n", "geminate", "178, 188", "SR 9: l + l > nn")
r("n", "ŋ", "conditions unknown", "190", "*n > ŋ",
  "*nuns(io) > ŋiso, *kani > xaŋi(i), *ŋmane > mʷaŋea-, *nipon > ŋii, *ponu > oŋi: 'no way to state a quasi-productive rule' (p. 190).",
  status="sporadic", n=5)
r("m", "m", "elsewhere", "189", "DR 15: *m > m / elsewhere", "*m > mʷ before a POC round vowel is the PMc change of Bender et al.")
r("mʷ", "mʷ", "elsewhere", "189", "*ŋm > mw")
r("ŋ", "ŋ", "elsewhere", "189", "*ŋ retained")
r("w", "w", "elsewhere", "189-190", "*w > w", "One exception, *waRo > jɔɔ.")
r("y", "j", "elsewhere", "189-190", "*y > y", "Only one example (*yaŋo > jaŋojaŋo); *mpaya > paa loses it.", n=1, sf="y")
# vowels
for v in "eao":
    r(v, v, "elsewhere", "190", f"*{v} > {v}", "'Consistently retained unchanged' apart from DR 2, 3 and 12 (p. 190).")
r("i", "i", "elsewhere", "190", "*i > i")
r("u", "ɨ", "not next to a bilabial", "180", "DR 2: *u > ů / if not preceded or followed by a POC bilabial consonant",
  "*?atun > aso, *dua > roa-, *kutu > xosů, *natu > laů, *susu > tosů; also not after another unchanged u (*putu > utu).",
  sf="ů")
r("u", "u", "next to a bilabial", "180", "DR 2 does not apply next to a POC bilabial",
  "*lumu > lumʷu, *-mu > -mʷu, *puko > uxo, *tampu > tabu.")
r("i", "ɨ", "_(C)ɨ", "180-181", "DR 3: *i > ů / _(C)ů (after DR 2)",
  "Applies 'fairly widely': *anitu > alůsů, *iku > ůxů, *inu(m) > ůlů, *niu(R) > lůů, *pitu?u > fůsů; *pitu > fisi "
  "keeps i, perhaps to avoid homophony (p. 181).", sf="ů")
FU = "DR 12: when *a and *o met after the loss of the consonant between them they fused as ɔɔ (p. 187): *mapo > mɔɔ, *waRo > jɔɔ, *mawap > mɔɔ."
r("a", "ɔː", "_+o", "187", "DR 12: *ao > ɔɔ", FU, n=3, sf="ɔɔ")
r("o", "ɔː", "a+_", "187", "DR 12: *ao > ɔɔ", FU, n=3, sf="ɔɔ")
AU = "Vowel assimilation after a lost consonant (20), p. 181: *pa?u > faa, *ndau(n) > saa, *paRu > (xili-)faa, *pa?oRu > ffaa; 'not entirely regular'."
r("a", "aː", "_+u", "181", "*au > aa", AU, status="sporadic", n=4, sf="aa")
r("u", "aː", "a+_", "181", "*au > aa", AU, status="sporadic", n=4, sf="aa")
AI = "(20), p. 181: *mai > me, *sa?it > tee-tee."
r("a", "e", "_+i", "181", "*ai > e(e)", AI, status="sporadic", n=2)
r("i", "e", "a+_", "181", "*ai > e(e)", AI, status="sporadic", n=2)

md = """# tawerilmangsohn1984-woleaian

Tawerilmang, Anthony F. & Ho-min Sohn. 1984. Proto-Oceanic reflexes in Woleaian. In Byron W. Bender (ed.), *Studies in Micronesian linguistics* (Pacific Linguistics C-80), 171-199. Read from the PDF in Downloads (sealang.net scan); inventory and rules from page images. Generator: `tools/batch_scripts/micronesia_2026_11_24/tawerilmangsohn1984.py`.

## Scope

- **Inventory** (4), p. 175: the first sourced inventory of Woleaian (`wole1240`). š = ʂ, c = ʈ͡ʂ, b = ɸ (as in the existing rows), ů = ɨ (high central, rounding not stated).
- **Allophones**: e [ə] next to ɨ; phrase-final vowel devoicing (SR 7).
- **Correspondences**: DR 2-15 and the fortition of doubled consonants (SR 9), composed to PCK > Woleaian (decision `mc1984-composition`); the vowel fusion of DR 12 and the assimilations of (20) as fusion pairs.

## Not entered

- DR 1 (final consonant apocope), DR 4 (*? > ∅), DR 11 (*R), *p > ∅ and *m > mʷ before round vowels: changes above PCK in Bender et al.'s chain (notes).
- The synchronic rules SR 1-6, 8 (semivowel insertion, a-rounding, a-raising, i-assimilation, lengthening): morphophonemic, not allophones of one phoneme.
- *e u > əə, *keu > xoo and other single forms; the Appendix cognate list.
- The Woleai Atoll dialect (Glottolog nucl1479, Nuclear Woleaian) is not split from Woleaian; the rows go on wole1240 with the earlier Woleaian rows.
"""
write("tawerilmangsohn1984-woleaian", b.t, md)
