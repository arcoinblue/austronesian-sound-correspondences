#!/usr/bin/env python3
"""Jackson (1984), Reflexes of Proto-Oceanic in the Trukic languages of Micronesia.

Table 1 (p. 261): PTK > eight Trukic languages, entered as PCK > language rows.
Table 2 and section 3 (pp. 263-273): POC > PTK, composed to PPC > PCK through Bender et al.'s (2003a) chain.
PTK vowel allophony (p. 262) goes to allophones.
"""
from common import Batch, write

S = "jackson1984"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Jackson, Frederick Henry", year="1984",
    title="Reflexes of Proto-Oceanic in the Trukic languages of Micronesia",
    url_or_doi="https://doi.org/10.15144/PL-C80.259", kind="comparative",
    notes="Consulted directly on 24 November 2026 (sealang.net scan; Tables 1 and 2 and the vowel section read from "
          "page images). Proto-Trukic (PTK) is the Proto-Chuukic (PCK) of Bender et al. (2003a); Jackson's *θ is "
          "their *d. POC is in the orthography of Grace (1969) and others (p. 262).",
    pub_type="chapter", container_title="Studies in Micronesian linguistics", editors="Byron W. Bender",
    pages="259-280", place="Canberra", publisher="The Australian National University",
    series="Pacific Linguistics C-80"))

# ---------------------------------------------------------------- Table 1: PCK > language
LANG = {"TRK": "chuu1238", "ULI": "ulit1238", "PUA": "pulo1240", "MRT": "mort1237", "PUL": "pulu1242",
        "STW": "sata1237", "CRL": "caro1242", "WOL": "wole1240"}
FN = {
    1: "voiceless stop [pʷpʷ] when geminate",
    2: "usually before non-low vowels",
    3: "irregularly before non-low vowels",
    4: "h → s when geminate",
    5: "voiceless stop [ṭʃṭʃ] when geminate",
    6: "*k > ∅ before low vowels and sporadically before mid vowels",
    7: "*k > s / _i sporadically (less frequent in MRT)",
    8: "*k > ∅ sporadically before low vowels",
    9: "voiceless stop [kk] when geminate",
    10: "*ŋ > n / _i in most cases",
    11: "the distinction between *l and *n is apparently collapsing in STW",
    12: "both *n and *l are [l] singly, [nn] when geminate in WOL",
    13: "before non-low vowels and irregularly before a",
}
T1 = "Table 1"
PTK2PCK = {"θ": "d"}
NOTE_THETA = "Jackson's PTK *θ (pp. 260-262) is the PCK *d of Bender et al. (2003a): the reflex of POC *s, *ns, *j."
NOTE_T = ("Jackson's PTK *t covers both *t and *T of Bender et al. (2003a); entered against PCK *t only.")


def t1(lang, ptk, child, env="elsewhere", status="regular", printed="", sf="", fn=(), extra="", cond=""):
    par = PTK2PCK.get(ptk, ptk)
    notes = [f"note {f}: {FN[f]}" for f in fn]
    notes = ("Footnote " + "; ".join(notes) + ". ") if notes else ""
    if ptk == "θ":
        notes += NOTE_THETA + " "
    if ptk == "t":
        notes += NOTE_T + " "
    b.corr(LANG[lang], par, child, env, "261", (notes + extra).strip(), status=status, derivation="",
           as_printed=f"PTK *{ptk} > {lang} {printed or child}", source_form=sf, locator=T1, conditioning=cond)


GEM = "geminate"
SINGLE = "single (not geminate)"
for L in LANG:
    t1(L, "p", "p")
    t1(L, "f", "f")
    t1(L, "m", "m")
    t1(L, "mʷ", "mʷ", printed="mw")
    t1(L, "ŋ", "ŋ", printed="ng") if L != "TRK" else None
    t1(L, "w", "w")
    if L != "ULI":
        t1(L, "θ", "t", printed="t")
for L in ("TRK", "MRT", "PUL", "STW"):
    t1(L, "pʷ", "pʷ", printed="pw")
t1("ULI", "pʷ", "βʷ", printed="b[βʷ]", sf="b")
t1("PUA", "pʷ", "βʷ", SINGLE, printed="pw[βʷ]¹", sf="pw", fn=(1,))
t1("PUA", "pʷ", "pʷ", GEM, printed="pw[βʷ]¹ ([pʷpʷ] when geminate)", sf="pw", fn=(1,))
t1("CRL", "pʷ", "bʷ", printed="bw", sf="bw")
t1("WOL", "pʷ", "ɸ", SINGLE, printed="b[βʷ]¹", sf="b",
   fn=(1,), extra="Jackson prints [βʷ]; entered as ɸ, the symbol of the Woleaian rows of Jackson (1983) and "
                   "the inventory of Tawerilmang & Sohn (1984), where it is written b.")
t1("WOL", "pʷ", "pʷ", GEM, printed="b[βʷ]¹ ([pʷpʷ] when geminate)", sf="pw", fn=(1,))
# *t
for L in ("TRK", "MRT", "STW", "CRL"):
    t1(L, "t", "∅", "_V[-low]", printed="∅,²s", fn=(2,), extra="Footnote 2 is read as qualifying ∅ (as footnote 6 qualifies ∅ in the *k column).")
    t1(L, "t", "s", "elsewhere", printed="∅,²s")
t1("ULI", "t", "s", "_V[-low]", printed="s,²t", fn=(2,))
t1("ULI", "t", "t", "elsewhere", printed="s,²t")
t1("PUA", "t", "θ", "_V[-low]", printed="d[θ],²t", sf="d", fn=(2,))
t1("PUA", "t", "t", "elsewhere", printed="d[θ],²t")
t1("PUL", "t", "∅", "_V[-low]", printed="∅,²h,ss⁴", fn=(2,))
t1("PUL", "t", "h", "elsewhere", printed="∅,²h,ss⁴", fn=(4,), extra="Single; geminate ss (footnote 4).")
t1("PUL", "t", "s", GEM, printed="∅,²h,ss⁴", fn=(4,))
t1("WOL", "t", "∅", "_V[-low]", "regular", printed="∅,³s,¹³t", fn=(3,), cond="lexical")
t1("WOL", "t", "s", "_V[-low]", printed="∅,³s,¹³t", fn=(13,))
t1("WOL", "t", "s", "_a", "sporadic", printed="∅,³s,¹³t", fn=(13,))
t1("WOL", "t", "t", "elsewhere", printed="∅,³s,¹³t")
# *c
t1("TRK", "c", "ʈ͡ʂ", printed="ch[ṭʃ]", sf="ch")
t1("ULI", "c", "c", printed="c[ṭʃ]", sf="c", extra="Jackson prints [ṭʃ]; entered as c, the symbol of the Ulithian inventory (Lynch 2002e).")
t1("PUA", "c", "s", printed="s")
for L, pr, ch in (("MRT", "sh[ʃ̣]⁵", "ʂ"), ("PUL", "r[ɻ]⁵", "ɻ"), ("STW", "rh[ɻ]⁵", "ɻ"), ("CRL", "sch[ʃ̣]⁵", "ʂ"),
                  ("WOL", "sh[ʃ̣]⁵", "ʂ")):
    t1(L, "c", ch, SINGLE, printed=pr, sf=pr.split("[")[0], fn=(5,),
       extra="Jackson's dotted [ʃ̣] is entered as ʂ, as in the rows of Jackson (1983)." if ch == "ʂ" else "")
    t1(L, "c", "t͡ʃ" if L == "PUL" else "ʈ͡ʂ", GEM, printed=pr + " ([ṭʃṭʃ] when geminate)", fn=(5,),
       extra="Entered as t͡ʃ, the symbol of the Puluwatese inventory (Lynch 2002f)." if L == "PUL" else "")
# *k
t1("TRK", "k", "k", "elsewhere", printed="k,∅,⁶s⁷")
t1("MRT", "k", "k", "elsewhere", printed="k,∅,⁶s⁷")
for L in ("TRK", "MRT"):
    t1(L, "k", "∅", "_V[+low]", printed="k,∅,⁶s⁷", fn=(6,))
    t1(L, "k", "∅", "_V[mid]", "sporadic", printed="k,∅,⁶s⁷", fn=(6,))
    t1(L, "k", "s", "_i", "sporadic", printed="k,∅,⁶s⁷", fn=(7,))
for L in ("PUL", "STW"):
    t1(L, "k", "k", "elsewhere", printed="k,∅⁶")
    t1(L, "k", "∅", "_V[+low]", printed="k,∅⁶", fn=(6,))
    t1(L, "k", "∅", "_V[mid]", "sporadic", printed="k,∅⁶", fn=(6,))
for L, pr, sf in (("ULI", "g[x]⁹", "g"), ("PUA", "k[x]⁹", "k"), ("CRL", "gh[x],∅⁶,⁹", "gh"), ("WOL", "g[x],∅⁸,⁹", "g")):
    t1(L, "k", "x", SINGLE, printed=pr, sf=sf, fn=(9,))
    t1(L, "k", "k", GEM, printed=pr + " ([kk] when geminate)", fn=(9,))
t1("CRL", "k", "∅", "_V[+low]", printed="gh[x],∅⁶,⁹", fn=(6,))
t1("CRL", "k", "∅", "_V[mid]", "sporadic", printed="gh[x],∅⁶,⁹", fn=(6,))
t1("WOL", "k", "∅", "_V[+low]", "sporadic", printed="g[x],∅⁸,⁹", fn=(8,))
# *ŋ, *n, *l, *r
t1("TRK", "ŋ", "ŋ", "elsewhere", printed="ng,n¹⁰")
t1("TRK", "ŋ", "n", "_i", printed="ng,n¹⁰", fn=(10,), extra="'In most cases'.")
for L in ("TRK", "PUA", "MRT", "PUL"):
    t1(L, "n", "n")
t1("ULI", "n", "l", printed="l")
t1("CRL", "n", "l", printed="l")
t1("STW", "n", "n", printed="n,l¹¹", fn=(11,))
t1("STW", "n", "l", "conditions unknown", "disputed", printed="n,l¹¹", fn=(11,))
t1("WOL", "n", "l", SINGLE, printed="l¹²", fn=(12,))
t1("WOL", "n", "n", GEM, printed="l¹² ([nn] when geminate)", fn=(12,))
for L in ("MRT", "PUL", "ULI", "CRL"):
    t1(L, "l", "l")
t1("TRK", "l", "n")
t1("PUA", "l", "n")
t1("STW", "l", "l", printed="l,n¹¹", fn=(11,))
t1("STW", "l", "n", "conditions unknown", "disputed", printed="l,n¹¹", fn=(11,))
t1("WOL", "l", "l", SINGLE, printed="l¹²", fn=(12,))
t1("WOL", "l", "n", GEM, printed="l¹² ([nn] when geminate)", fn=(12,))
for L in ("TRK", "ULI", "MRT", "STW", "CRL", "WOL"):
    t1(L, "r", "r")
t1("PUL", "r", "r", printed="ŕ", sf="ŕ")
t1("PUA", "r", "l")

# ---------------------------------------------------------------- Table 2: POC > PTK, composed to PPC > PCK
C = ("Stated against POC (Table 2, p. 263; §3); restated against PPC through the POc > PMc > ... > PPC rows of "
     "Bender et al. (2003a). ")


def t2(par, child, env, page, printed, notes="", status="regular", n="", decision="jackson1984-composition"):
    b.corr("pck", par, child, env, page, C + notes, status=status, n=n, as_printed=printed, locator="Table 2",
           decision=decision)


t2("p", "p", "elsewhere", "264", "POC *mp > PTK *p", "Before non-round vowels; before round vowels *mp merged with *ŋp as *pw (in PMc, Bender et al.).")
t2("pʷ", "pʷ", "elsewhere", "264", "POC *mp, *ŋp > PTK *pw")
t2("f", "f", "elsewhere", "263", "POC *p > PTK *f",
   "Jackson's loss of POC *p before round vowels (POC *p > PTK ∅) is the PMc change of Bender et al. (2003a); it has no PPC phoneme behind it.")
t2("m", "m", "elsewhere", "264-265", "POC *m > PTK *m", "*m became *mw before round vowels, in PMc according to Bender et al.")
t2("mʷ", "mʷ", "elsewhere", "264-265", "POC *ŋm > PTK *mw")
t2("k", "k", "elsewhere", "266", "POC *k > PTK *k", "'Consistently retained' (p. 266).")
t2("x", "∅", "elsewhere", "266", "POC *ŋk > PTK ∅", "PPC *x is POC *ŋk (POc *ɡ).")
t2("ŋ", "ŋ", "elsewhere", "266-267", "POC *ŋ > PTK *ŋ", "One exception: *uŋa > PTK *umwa 'hermit crab'.")
t2("n", "n", "elsewhere", "269-270", "POC *n, *ñ > PTK *n")
t2("n", "ŋ", "a_i", "270", "POC *n > PTK *ŋ / a_i", "'Usually' (p. 270): *(n)tani > *taŋi, *kani > *kaŋi, *mani > *maŋi, *kani > *(k)kaŋi.", n=4)
t2("ñ", "n", "elsewhere", "270", "POC *ñ > PTK *n",
   "Jackson merges POC *ñ with *n in PTK (innovation 5, p. 273); Bender et al. (2003a) keep PCK *ñ, whose reflexes differ from those of *n in Woleaian, Pulo-Annan and Sonsorolese. Marked disputed for that reason.",
   status="disputed")
t2("ñ", "ŋ", "conditions unknown", "270", "POC *ñ > PTK *ŋ",
   "In *ŋuθi/*ŋiθo 'squid' < *ñ,ñunsi,o and *ŋenú 'shadow, ghost' < *ñ,ñunu.", status="sporadic", n=2)
t2("w", "w", "elsewhere", "272", "POC *w > PTK *w")
t2("y", "∅", "elsewhere", "272", "POC *y > PTK ∅",
   "'Seems to be lost, with two exceptions' (p. 272). Bender et al. (2003a) have PCK *y; marked disputed.",
   status="disputed")
t2("t", "t", "elsewhere", "267", "POC *t > PTK *t",
   "Exceptions: *t lost in *watu, *natu (all TK) and *pati (all MC); PTK *θ in *kato > *kaθo, *tale > *θale, perhaps *kita > *kuθθa (possibly loans).")
t2("t", "d", "conditions unknown", "267", "POC *t > PTK *θ", "*kato > *kaθo, *tale > *θale, perhaps *kita > *kuθθa; 'these may be borrowings' (p. 267). Jackson's *θ is PCK *d.",
   status="sporadic", n=3)
t2("d", "d", "elsewhere", "268-269", "POC *s, *ns, *j > PTK *θ", NOTE_THETA + " Table 1 gives ULI d [θ] and t in the other languages.")
t2("d", "∅", "conditions unknown", "269", "POC *s, *ns > PTK ∅",
   "Unexpected loss in *masi > *mai, *(n)soko > *(y)oko, *monse > *(mw)mwee (p. 269).", status="sporadic", n=3)
t2("d", "t", "conditions unknown", "269", "POC *s, *ns > PTK *t",
   "*so(ŋ)ka(r) > *toa, *suli > *tili, *sidi(t) > *tiri, *nsiŋi > *tiŋi, *(n)sai > (i-)te,au; 'these exceptions defy explanation' (p. 269).",
   status="sporadic", n=5)
t2("c", "c", "elsewhere", "268", "POC *nt, *nd > PTK *c", "With no apparent exceptions (p. 268); the merger is also MC-wide.")
t2("r", "r", "elsewhere", "271", "POC *d > PTK *r",
   "POC *R is lost or merges with *r (pp. 271-272), the PMc split of Bender et al.; four cases of POC *d > PTK *c reflect the nasal grade *nd, as in all MC (p. 273).")
t2("l", "l", "elsewhere", "270-271", "POC *l > PTK *l")
t2("l", "r", "conditions unknown", "271", "POC *l > PTK *r", "*kula > *kura, *sakulaya > *θakul,raara.", status="sporadic", n=2)
for v in "eao":
    t2(v, v, "elsewhere", "263, 273", f"POC *{v} > PTK *{v}", "'Generally identical' (p. 273).")
t2("i", "i", "elsewhere", "263, 273", "POC *i > PTK *i")
t2("u", "u", "elsewhere", "263, 273", "POC *u > PTK *u")
V = ("The high central unrounded vowel, printed *ú: 'in pre-TRK an allophonic variant of *u in the environment of a "
     "nonround vowel, and of *i before *u', but distinctive in PTK in *nɨɨ 'coconut' < *niu(R) and *θɨɨ 'bathe' "
     "< *(n)su(ŋ)ki (p. 262). Table 2 links POC *i and *u to it.")
t2("u", "ɨ", "next to a non-round vowel", "262-263", "POC *u > PTK *ú", V, decision="jackson1984-central-vowel")
t2("i", "ɨ", "_Cu", "262-263", "POC *i > PTK *ú", V, decision="jackson1984-central-vowel")
b.t["notation_map"].append(dict(lect_id="pck", phoneme="ɨ", system="canonical", symbol="ɨ", source_id=S, page="262",
                                notes="Printed *ú; 'the high central unrounded vowel' (p. 262)."))

# ---------------------------------------------------------------- PTK allophones (p. 262)
for a, env in (("æ", "_(C){i,e}"), ("ə", "_(C)u"), ("ɔ", "_(C)o")):
    b.allo("pck", "a", a, env, "262", "'Apparently' (p. 262); printed á [æ], é [ə], ó [ɔ].")
for v in "ieaou":
    b.allo("pck", v, v + "̥", "phrase-finally", "262",
           "Phrase-final vowel devoicing, which Jackson reconstructs for PTK (p. 262).")

b.dec("jackson1984-composition", "Jackson (1984) states PTK reflexes of POC (Table 2). How are they entered?",
      "As PPC > PCK rows composed through the POc > PMc > ... > PPC rows of Bender et al. (2003a), with the "
      "POC statement in as_printed. A change Bender et al. place higher (loss of *p before round vowels, *q, the "
      "split of *R, *m > *mw before round vowels) is a note, not a row. Where Jackson's PTK disagrees with "
      "Bender et al.'s PCK (*ñ merged with *n; *y lost) the row is disputed. Jackson's *θ is PCK *d; his *t is "
      "entered against PCK *t only. The rows of Table 1 (PTK > language) are entered as printed against PCK.",
      "Enter Table 2 against POc on a separate PTK lect competing with PCK.", "261-263")
b.dec("jackson1984-central-vowel", "PTK *ú (high central unrounded vowel, p. 262): a PCK phoneme?",
      "Added as PCK *ɨ, with *u > *ɨ next to a non-round vowel and *i > *ɨ before *u, both regular: Jackson "
      "calls it allophonic in pre-Trukese but distinctive in PTK. Its daughter reflexes are not entered.",
      "Leave it out (no PCK *ɨ) and describe it in the PCK notes.", "262-263")

md = """# jackson1984-trukic

Jackson, Frederick Henry. 1984. Reflexes of Proto-Oceanic in the Trukic languages of Micronesia. In Byron W. Bender (ed.), *Studies in Micronesian linguistics* (Pacific Linguistics C-80), 259-280. Read from the PDF in Downloads (sealang.net scan); Tables 1-2 and p. 262 from page images. Generator: `tools/batch_scripts/micronesia_2026_11_24/jackson1984.py`.

## Scope

- **Table 1 (p. 261)**: PTK > eight Trukic languages, as PCK > language rows with the printed cell in `as_printed` and the footnotes in the notes. IPA as in the rows of Jackson (1983): sh [ʃ̣] = ʂ, rh/r [ɻ] = ɻ, ch [ṭʃ] = ʈ͡ʂ, g/gh/k [x] = x; Woleaian b [βʷ] is ɸ and Ulithian d [θ], c [ṭʃ] are ð, c, the symbols of the inventories already in the sheet. Geminate realisations (footnotes 1, 5, 9, 12) are rows with environment `geminate`. Footnote 2 ('usually before non-low vowels') is read as qualifying the ∅ (Ulithian s, Pulo-Annan θ) before it, as footnote 6 qualifies ∅ in the *k column.
- **Table 2 and §3 (pp. 263-273)**: POC > PTK, composed to PPC > PCK (decision `jackson1984-composition`), with sporadic rows for the exceptions Jackson lists with two or more forms.
- **PTK *ú** as PCK *ɨ (decision `jackson1984-central-vowel`), with a notation row.
- **Allophones**: PTK *a fronted, raised and backed before i/e, u, o; phrase-final devoicing of the vowels (p. 262).

## Not entered

- Changes above PPC in Bender et al.'s chain: loss of POC *p before round vowels, *q, *R, *m > *mw before round vowels (notes on the rows).
- POC *nj > ∅ (four forms, p. 269): POc *j corresponds to PMc *s and *Z, and *Z is lost before PPC.
- Long vowels and compensatory lengthening (p. 262): no column; Jackson's PTK *T is not distinguished from *t.
- Single exceptions (*uŋa > *umwa; *kula is entered with *sakulaya).
"""
write("jackson1984-trukic", b.t, md)
