#!/usr/bin/env python3
"""Adelaar (1981), Reconstruction of Proto-Batak phonology.

Part I: the phoneme systems of the Batak dialects (pp. 1-10); Part II: the comparison and the PB reconstruction
(pp. 11-17); Part III: PB against PAN (pp. 17-18). Billings & McDonnell (2024: 118-119, 170) entered the Batak nodes
and their changes 'following primarily Adelaar (1981)'; this batch adds Adelaar's own inventories for Dairi, Toba,
Angkola, Mandailing and Simalungun, allophones, and his correspondences as a second source on the same nodes, with
the few he states that Billings & McDonnell lack. Read directly on 25 November 2026 (a scan with no text layer in
Downloads: OCR, charts and symbols checked against the page images).
"""
from common import Batch, write

S = "adelaar1981"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Adelaar, K. A.", year="1981", title="Reconstruction of Proto-Batak phonology", kind="comparative",
    pub_type="chapter", container_title="Historical linguistics in Indonesia, part I", editors="Blust, Robert A.",
    series="NUSA 10", pages="1-20", place="Jakarta", publisher="Badan Penyelenggara Seri NUSA",
    notes="Consulted directly on 25 November 2026 (a 20-page scan in Downloads, no title page; volume details as "
          "commonly cited). Six dialects: Karo, Dairi (Northern Batak), Toba, Angkola, Mandailing (Southern Batak) "
          "and Simalungun; Alas excluded for lack of data (p. 1). Part I gives each dialect's phoneme system and "
          "morphophonology from the written language and dictionaries (Neumann for Karo, the Dairi-Pakpak "
          "dictionary, van der Tuuk and Warneck for Toba, Eggink for Angkola-Mandailing, Saragih and Tarigan for "
          "Simalungun); Part II the PB vowels *a, *e, *i, *u, *ow, *uy, *ey and consonants *b, *d, *g, *j, *p, *t, *k, "
          "*c, *h, *m, *n, *ŋ, *r, *l, *s, *w, *y (PB lexical reconstructions numbered 1-136); §11 (p. 17) the tree: "
          "Proto-Batak > Proto-Northern-Batak (Karo, Dairi, Alas?) and Proto-Southern-Batak (Simalungun, "
          "Proto-Toba > Toba, Proto-Angkola-Mandailing > Angkola, Mandailing); Part III the PB system against PAN "
          "(§§12-14, pp. 17-18). Two asterisks mark PB etyma, two crosses loans; shwa is written ə."))

DAI, TOB, ANG, MAN, SIM, KAR = "bata1294", "bata1289", "bata1290", "bata1291", "bata1288", "bata1293"
# ---------------------------------------------------------------- inventories (Part I)
C = dict(b="b", d="d", ɟ="j", ɡ="g", p="p", t="t", c="c", k="k", m="m", n="n", ŋ="ŋ", ɲ="ñ", r="r", l="l", h="h",
         s="s", j="y", w="w")
INV = {
    DAI: ("4", "b d ɟ ɡ p t c k m n ŋ r l h s j w", "i e ə o a u", {}),
    TOB: ("5-6", "b d ɟ ɡ p t k m n ŋ r l s", "i e o a u", {}),
    MAN: ("8", "b d ɟ ɡ p t c k m n ɲ ŋ r l h s j", "i e o a u", {"c": "marginal"}),
    ANG: ("9", "b d ɟ ɡ p t c k m n ɲ ŋ r l s j", "i e o a u", {"c": "marginal"}),
    SIM: ("10", "b d ɟ ɡ p t k m n ŋ r l h s j w", "i e o a u ei ou ui", {}),
}
PN = {
    (DAI, "ə"): "Occurs in all syllables except before (h)#; all other vowels have a long variant (p. 4, §2.1).",
    (MAN, "c"): "In parentheses in the chart; see /s/ (p. 8, §4.1); elsewhere only in loans.",
    (ANG, "c"): "In parentheses in the chart, as in Mandailing; see /s/ (p. 9, §§5.3-5.4); 'secondary' (p. 15, §9.4.1).",
    (MAN, "ɲ"): "AnMa ñ has y as a variant in many lexemes and is the nasal substitute of s; its correspondences are "
                "unpredictable (pp. 15-16, §9.4.2).",
    (ANG, "ɲ"): "See Mandailing ñ (pp. 15-16, §9.4.2).",
    (MAN, "h"): "Mandailing [h] and [k] correspond to /k/ 'in the deep structure' (p. 19 n. 9); Ma [Ø] where Toba has [h] "
                "(p. 14, §9.3).",
}
# Place and manner as Adelaar's charts have them (columns glottal, velar, palatal, dental, labial; 'stops' plosive,
# 'vibrant' trill), so that j (his y) is the glide and c, ɟ the palatal stops.
F = dict(b=("bilabial", "plosive", "voiced"), p=("bilabial", "plosive", "voiceless"), m=("bilabial", "nasal", "voiced"),
         w=("labial-velar", "approximant", "voiced"), d=("dental", "plosive", "voiced"), t=("dental", "plosive", "voiceless"),
         n=("dental", "nasal", "voiced"), r=("dental", "trill", "voiced"), l=("dental", "lateral-approximant", "voiced"),
         s=("dental", "fricative", "voiceless"), ɟ=("palatal", "plosive", "voiced"), c=("palatal", "plosive", "voiceless"),
         ɲ=("palatal", "nasal", "voiced"), j=("palatal", "approximant", "voiced"), ɡ=("velar", "plosive", "voiced"),
         k=("velar", "plosive", "voiceless"), ŋ=("velar", "nasal", "voiced"), h=("glottal", "fricative", "voiceless"))
for L, (pg, cons, vows, st) in INV.items():
    for ipa in cons.split():
        pl, mn, vc = F[ipa]
        b.ph(L, ipa, "C", pl, mn, vc, sym=C[ipa], page=pg, status=st.get(ipa, ""),
             notes=PN.get((L, ipa), "") + (" " if (L, ipa) in PN else "") + f"Adelaar (1981: {pg}), chart of Part I.")
    for ipa in vows.split():
        sym = {"ei": "-ey", "ou": "-ow", "ui": "-uy"}.get(ipa, ipa)
        note = ("Final diphthong, written as two vowels in Simalungun spelling but analysed as a diphthong on "
                "P. Voorhoeve's advice (p. 10, §6.1); Tarigan analyses two vowels. " if ipa in ("ei", "ou", "ui") else "")
        b.ph(L, ipa, "V", sym=sym, page=pg, notes=note + f"Adelaar (1981: {pg}), chart of Part I.")

# ---------------------------------------------------------------- allophones (Part I)
b.allo(TOB, "k", "h", "word-initially, between vowels and after a liquid", "6",
       "'/h/ and /k/ are in complementary distribution: /h/ occurs in initial position, between V's and after liquids, "
       "whereas /k/ is the final C of a syllable' (§3.2); (h) is in parentheses in the chart.")
b.allo(TOB, "k", "∅", "medially before i (from the [h] variant)", "6", "'/h/ is not pronounced in medial position before /i/' (§3.2).")
b.allo(ANG, "k", "h", "word-initially and between vowels", "9",
       "'/h/ occurs in initial and intervocalic position, and /k/ occurs in final position, as a component of a "
       "consonant cluster, and in initial position in lexemes if the next syllable begins with /h/' (§5.1).")
b.allo(MAN, "s", "c", "after n, and in a word that contains [nc]", "8", "§4.1: lancat /lansat/; bincucur /binsusur/.")
b.allo(ANG, "s", "c", "as the second member of a cluster after a voiceless stop; after a final voiceless stop in sandhi",
       "9", "§§5.3-5.4: [makci], [halakcokkoni].")
b.allo(TOB, "s", "t͡s", "geminated, after a nasal", "6", "'N + vl. stop or /s/ yields gemination of the latter ... geminated /s/ is realized as [ts]': hinsu [hitsu] (§3.3.1).")
b.allo(KAR, "h", "x", "word-finally", "2", "'The -/h/# sounds like German -ch ([x]); /h/- is usually not pronounced and is hardly ever distinctive in this position' (§1.3).")
b.allo(KAR, "h", "∅", "word-initially", "2", "'/h/- is usually not pronounced' (§1.3): ayam/hayam, anat/hanat.")
b.allo(DAI, "h", "∅", "word-initially, often", "4", "'In initial position /h/ is weak, and is often omitted, as in hasa: [hasa]=[asa]; but in some lexemes /h/ is never omitted, as in hakum' (§2.3).")
for v in "ieoau":
    b.allo(DAI, v, v + "ː", "in (C)VC and (C)VCV(C) under the accent, and from contraction in affixation", "4",
           "'All V's but /ə/ have a long variant which originates from contraction in the process of affixation, or "
           "is correlated with accent' (§2.1).")
# ---------------------------------------------------------------- correspondences (Part II), on the nodes
D = "adelaar1981-batak"
def N(lect, par, child, env, page, notes, **k):
    k.setdefault("derivation", "composed" if lect in ("pnb", "pcsb", "psb") else "")
    b.corr(lect, par, child, env, page, notes=notes, decision=D, **k)

FV = ("'Final vd. stops in Si correspond to homorganic nasals in NB and homorganic vl. stops in SB' (§9.0, p. 13): "
      "**deleg 'mountain' > Si dolog, SB dolok, NB dələŋ; **abab 'ashes' > Si abab, SB abap, NB abəm.")
for ph, nb, sb in (("b", "m", "p"), ("d", "n", "t"), ("ɡ", "ŋ", "k")):
    N("pnb", ph, nb, "_#", "13", FV)
    N("psb", ph, sb, "_#", "13", FV + " Toba bodari 'night' keeps an old voiced *d inside a compound.")
    N(SIM, ph, ph, "_#", "13", FV, derivation="stated-retention")
DI = {"ey": ("e", "§7.2.7: Si matey [matey], NB-SB mate 'dead'"), "ow": ("o", "§7.2.5: Si rantou [rantow], SB-NB ranto"),
      "uy": ("i", "§7.2.6: Si apuy, NB-SB api 'fire'; Si lanuy, other dialects lane 'swim' (unexplained e)")}
for ph, (out, ex) in DI.items():
    for L in ("pnb", "psb"):
        N(L, ph, out, "_#", "11-12", f"PB *-{ph} is preserved only in Simalungun ({ex}).")
N("pnb", "t", "c", "_i", "15", "'Si, SB /t/ corresponds to NB /c/ before /i/': **kutiŋ 'cat' > SB, Si hutiŋ, Ka kuciŋ, "
  "Da kəciŋ; **tikep > Ka cikap (§9.4.1). Adelaar reconstructs *t 'because a development from *t to /c/ is much "
  "more common than one from *c to /t/'.")
N("pcsb", "ə", "o", "elsewhere", "11, 15", "'*e from /ə/ in Ka, /ə/ and /o/ in Da, /o/ in Si-SB' (§7.2.4): **enem > "
  "SB-Si onom, NB ənəm; a common innovation of Si and SB (§9.3.1d).")
N("pcsb", "k", "h", "#_, V_V", "14-15", "NB /k/ : To, An h~k, Ma k~Ø, Si h~k (§9.3): **kutu > SB, Si hutu, Ma [utu], NB "
  "kutu. 'Si agrees with SB in its change of *k to /h/ in initial and medial position' (§9.3.1a).")
N("pcsb", "h", "∅", "#_, V_V", "14-15", "NB /h/ corresponds to Ø-, -Ø-, -Ø in SB and to Ø-, -Ø-, -h in Si (§9.3): "
  "**tabeh > SB tabo, Si taboh; Si and SB share the loss of *h 'except in final position, where it is retained in "
  "Si' (§9.3.1a).")
N("pcsb", "h", "h", "_#", "14-15", "Retained in Si only: **si-ba(e)seh > Si si-basoh, SB si-baso (§9.3).",
  derivation="stated-retention")
N("psb", "h", "∅", "_#", "14", "SB -Ø for NB, Si -h (§9.3): **pereh > SB poro, Si poroh, Ka pereh.")
N("pcsb", "c", "s", "elsewhere", "15", "'PB *c became /s/ in both SB and Si' (§9.3.1c, §9.4.1): **racun > SB, Si "
  "rasun, NB racun; AnMa have s~c.")
N("psb", "w", "∅", "V_V", "13", "'/w/ occurs in intervocalic position in NB and Si. The correspondence in SB is usually "
  "Ø' (§8.2): **awak > To ak, Da awak; **sawit > To sait. Toba b between a's reflects *b, which merged with *w in NB "
  "and Si (**kaban > To haban, Si, Da kawan).")
N(DAI, "ə", "o", "_h#", "11", "'Da does not allow /ə/ before fin. /h/ and in monosyll. lexemes, and has /o/ instead' "
  "(§7.2.4): **taneh > Da tanoh, Ka tanəh.")
N(DAI, "ə", "o", "in monosyllables", "11", "§7.2.4: Ka bən, Da bon 'to get dark' (**bed); Ka dəm, Da dom 'full' (§7).")
N(TOB, "y", "∅", "elsewhere", "13", "'These do not occur in To ... In To y is contracted with a preceding or following "
  "V, and is lost between /a/ and /u/' (§8, 8.1): **kayu > To hau, Si-AnMa hayu.")

b.dec(D, "How are Adelaar's (1981) Batak reconstruction and correspondences entered beside Billings & McDonnell (2024)?",
      "Billings & McDonnell's nodes stay (pnb = Adelaar's Proto-Northern-Batak; pcsb = his Proto-Southern-Batak "
      "with Simalungun; psb = his Proto-Toba; his Proto-Angkola-Mandailing is not entered, as their AM-Batak is not). "
      "Adelaar's dialect correspondences are composed onto the node that all daughters showing them share, as a "
      "second source beside Billings & McDonnell's rows; new are *t > NB c before i and the loss of intervocalic *w "
      "in SB. His dialect inventories go in for Dairi, Toba, Angkola, Mandailing and Simalungun (Karo keeps Woollams "
      "2005); Toba and Angkola (h) is an allophone of /k/. Simalungun j is Adelaar's voiced palatal stop ɟ, so Billings & "
      "McDonnell's sporadic Simalungun d͡ʒ shows as a reflex outside the inventory. Part III (PAN > PB) is not entered: Billings & "
      "McDonnell already state PSUM > PB, and Adelaar's PAN (Dyen's) does not map onto PMP one to one (*Z > PB *d "
      "beside *z > PB *j).",
      "Rename the nodes after Adelaar (Proto-Southern-Batak for pcsb, Proto-Toba for psb); add Proto-Angkola-Mandailing; "
      "enter Part III as PB rows against PSUM.", "11-18")
write("adelaar1981-batak", b.t, """# adelaar1981-batak

Adelaar, K. A. 1981. Reconstruction of Proto-Batak phonology. In Robert A. Blust (ed.), *Historical linguistics in Indonesia, part I* (NUSA 10), 1-20. Jakarta: Badan Penyelenggara Seri NUSA. Generator: `tools/batch_scripts/nine_sources_2026_11_25/batak.py`.

## Scope

- Sourced inventories (Part I charts, from the page images) for Dairi, Toba, Angkola, Mandailing and Simalungun; AnMa c marginal; Simalungun final diphthongs as ei, ou, ui (as Billings & McDonnell's rows have them).
- Allophones: Toba and Angkola k [h], Toba s [ts], AnMa s [c], Karo h [x] and h- dropped, Dairi h- dropped, Dairi long vowels (Karo length, distinctive for Adelaar, is not entered).
- Correspondences of Part II composed onto Billings & McDonnell's nodes (decision `adelaar1981-batak`): final voiced stops, final diphthongs, *t > NB c / _i, *ə > o, *k > h, *h, *c > s, SB loss of *w, Dairi ə > o, Toba loss of y.

## Not entered

- Part III (PAN > PB), the PB lexical reconstructions (cited in notes), PB *(N)c and *(N)y, Karo /ö/, accent (§10), the morphophonology of each dialect beyond the allophones above, Proto-Angkola-Mandailing as a node.
""")
