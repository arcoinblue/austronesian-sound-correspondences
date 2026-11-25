#!/usr/bin/env python3
"""Bugenhagen (1994), Language change on Umboi Island.

In Dutton & Tryon (eds.), Language contact and change in the Austronesian world, 43-108. Mangap-Mbula
(mbul1263, already in the sheet with Ross 1988's consonant rows): the segmental contrasts (Table 1, p. 48) as a
sourced inventory, allophones (pp. 48-50), the POC consonant developments (Table 3, p. 52; voiced stops p. 51) and
the vowel rules (pp. 53-59), all against POC (Mangap's parent).
"""
from common import Batch, write, chapter, CONSULTED

S = "bugenhagen1994"
b = Batch(S)
b.t["sources"].append(chapter(
    S, "Bugenhagen, Robert D.", "Language change on Umboi Island", "43-108",
    CONSULTED + "Mangap-Mbula (Austronesian, Siassi/Vitiaz) and Kovai (non-Austronesian) on Umboi Island, Morobe "
    "Province. §2.1: Mangap-Mbula synchronic phonology (Table 1, p. 48, distribution Table 2), POC consonant "
    "developments by position (Table 3, p. 52, after Ross's 1988 fortis/lenis grades), the voiced stops (p. 51) and "
    "seven ordered vowel rules (pp. 53-59); §2.2: Austronesian and non-Austronesian loans identified by irregular "
    "correspondences (Appendices 1-3); §2.3: grammatical change; §3: Kovai. Data from the author's field work."))

L = "mbul1263"
D = "bugenhagen1994-mangap"
T3 = "Table 3 (p. 52): "


def r(par, ch, env, page="52", notes="", **k):
    b.corr(L, par, ch, env, page, notes=notes, derivation="", decision=D, **k)


# Table 3
r("p", "p", "#_ (non-verb, fortis)", notes=T3 + "non-verb initial (fortis).")
r("p", "w", "#_ (verb, lenis)", notes=T3 + "verb initial (lenis); also in reduplications: -pese 'paddle' > -wes-wese, "
  "-pet 'appear' > -wed-et (p. 52 n. 9).")
r("p", "w", "a_a", notes=T3 + "intervocalic between a's.")
r("p", "∅", "V_V", notes=T3 + "intervocalic elsewhere. Ordered before Antepenultimate Vowel Loss: -twiri 'conch shell' "
  "< *tapuRi (p. 53 n. 14).")
r("p", "u", "_# (developed final)", notes=T3 + "'developed word final': a consonant made final by the loss of the "
  "vowel after it (n. 10). *Rapi > rawi > rowi > row > rou 'afternoon' (pp. 55-58).")
r("t", "t", "elsewhere", notes=T3 + "t in every position.")
for q in ("k", "q"):
    r(q, "k", "#_", notes=T3 + "POC *k and *q: initial k (fortis and lenis). Forms with initial *q lost or not "
      "reflected as k are loans: -win 'drink' < *qinu(m), iwa- 'affine' < *qipaR (p. 53).")
    r(q, "∅", "V_V", notes=T3 + "intervocalic Ø; ordered after Antepenultimate Vowel Loss (mbku- 'joint' < *buku, "
      "p. 53 n. 14). Forms that keep it are loans: makat 'dry reef' < *makati (p. 53).")
    r(q, "k", "_# (developed final)", notes=T3 + "developed word final k.")
r("c", "z", "V_V", notes=T3 + "no initial reflex known (data gap, n. 11).")
r("c", "s", "_# (developed final)", notes=T3 + "developed word final.")
r("s", "s", "#_ (non-verb, fortis)", notes=T3 + "non-verb initial.")
r("s", "z", "#_ (verb, lenis)", notes=T3 + "verb initial (lenis): -se 'ascend' > -ze-ze (n. 9).")
r("s", "s", "V_V", notes=T3 + "intervocalic s, synchronically voiced [z] when underlyingly intervocalic (n. 12).")
r("s", "s", "_# (developed final)", notes=T3 + "developed word final.")
r("j", "z", "elsewhere", notes=T3 + "z initial (both grades) and intervocalic.")
r("j", "s", "_# (developed final)", notes=T3 + "developed word final.")
for c in ("m", "n", "ŋ", "l"):
    r(c, c, "elsewhere", notes=T3 + f"{c} in every position.")
r("ñ", "n", "elsewhere", notes=T3 + "the row is printed 'n, .' with its second symbol lost in print; read as POC *n, "
  "*ñ, as in Ross (1988: 167-171).", status="disputed")
for q in ("r", "R"):
    r(q, "r", "elsewhere", notes=T3 + "POC *r, *R: r in every position (the summary on p. 59 has n for *r in "
      "developed final position, against Table 3).")
r("w", "w", "#_", notes=T3 + "initial (both grades).")
r("w", "w", "a_a", notes=T3 + "intervocalic between a's.")
r("w", "∅", "V_V", notes=T3 + "intervocalic elsewhere ('if either vowel was not /a/', p. 59); ordered after "
  "A-Assimilation to Glides (p. 56 n. 21).")
r("y", "j", "#_", notes=T3 + "initial y (both grades).")
r("y", "∅", "V_V", notes=T3 + "intervocalic Ø, after A-Assimilation to Glides: *kayu > keyu > ke 'tree' (pp. 57-58).")
for c, ini, med, fin in (("b", "ᵐb", "ᵐb", "m"), ("ɡ", "ᵑɡ", "ᵑɡ", "ŋ"), ("dr", "ⁿd", "ⁿd", ""), ("d", "", "r", "")):
    note = ("Voiced occlusives 'in all forms which are transparently derived from Proto-Oceanic forms' (p. 51): /b, dr, "
            "d, g/ > /mb, nd, -, ŋg/ initially, /mb, nd, r, ŋg/ intervocalically, /m, -, n, ŋ/ as developed finals (a "
            "dash is a data gap). Forms with oral voiced stops (biti 'yam' < PNNG *bidi) are probably loans; whether "
            "the synchronic oral/prenasalised harmony is inherited is left open (pp. 51-53).")
    if ini:
        r(c, ini, "#_", "51", note)
    r(c, med, "V_V", "51", note)
    if fin:
        r(c, fin, "_# (developed final)", "51", note)
r("d", "n", "_# (developed final)", "51", "p. 51 gives n for the developed final of *d and a gap for *dr; the summary "
  "on p. 59 lists /b, d, g, dr, r/ > /m, -, ŋ, n, n/, the other way round. Entered as on p. 51.", status="disputed")
for c in ("p", "t", "k", "q", "s", "c", "j", "m", "n", "ŋ", "r", "R", "l", "b", "d", "dr", "ɡ"):
    r(c, "∅", "_# (original final)", "51", "'the loss of all original word-final consonants' (p. 51): *namuk > "
      "nomnom 'mosquito', *kauR > ko 'bamboo' (p. 56).")
for c, base in (("mʷ", "m"), ("pʷ", "p"), ("bʷ", "b")):
    r(c, {"m": "m", "p": "p", "b": "ᵐb"}[base], "elsewhere", "51",
      f"'The labialised consonants /mw, pw, bw/ developed identically to /m, p, b/, but also caused following /a/s to "
      f"be rounded' (p. 51): *dramwa > ndomo- 'forehead' (p. 57).")

# Vowels (pp. 53-59)
V = "Vowel rule {} (p. {}): "
for v in ("i", "e", "a", "o", "u"):
    r(v, "∅", "antepenultimate syllable", "53", V.format("1, Antepenultimate Vowel Loss", 53) +
      "*waRisa > wrisi [uri:zi] 'yesterday', *malawa > mlo 'long'; the source of the consonant clusters broken up "
      "by an epenthetic vowel (n. 13). Ordered after *p > w / V_V and before the loss of intervocalic *k (n. 14).")
r("o", "e", "initial syllable, or after a [-back] vowel", "54", V.format("2, O-Fronting", 54) +
  "*pose > pese 'paddle', *pogu > peŋ 'turtle', *kadroRa > kndere 'cuscus'; left-to-right iterative. *tanoq > tono "
  "(no fronting after a back vowel).")
r("u", "i", "_(C)i#", "54-55", V.format("3, U-Assimilation to i", 54) +
  "*qupi > kiu 'yam', *tapuRi > twiri 'conch shell', *pudi > pir 'banana'; i does not assimilate to a following u "
  "(*pitiqun > ptik 'star').")
r("i", "e", "[-high, -round] V(C)_", "55", V.format("4a, I-Lowering", 55) +
  "*Raqi > re 'southeast wind', *kori > kere 'scrape'; not after o (*Rapi > rou 'afternoon', n. 19). Some forms "
  "without 4a and 4b are loans that came in while 4d was active (n. 18).")
r("a", "e", "e(C)_, _(C)e", "56", V.format("4b, A-Harmony", 56) +
  "a assimilates in rounding to a preceding or following low or mid vowel: *mate > mete 'die', *mena > mene 'sago', "
  "*tanoq > tono 'land', *kauR > ko 'bamboo', *namuk > nomnom 'mosquito'.")
r("a", "o", "o(C)_, _(C)o", "56", V.format("4b, A-Harmony", 56) + "*tanoq > tono 'land'; *kauR > ko 'bamboo'.")
r("a", "o", "next to w and labialised consonants", "56-57", V.format("4c, A-Assimilation to Glides", 56) +
  "*waga > woŋgo 'canoe', *dramwa > ndomo- 'forehead', *yapi > you 'fire'. Following labialised consonants are "
  "only assumed to round a (n. 22).")
r("a", "e", "_y", "56-57", V.format("4c, A-Assimilation to Glides", 56) +
  "*kayu > ke 'tree', *laya > le 'sail'; a preceding y has no effect (*maya > mia- 'tongue', n. 24).")
for v in ("i", "u"):
    r(v, "∅", "_#", "57-58", V.format("4d, Final Vowel Loss", 57) +
      "high vowels are lost word-finally: *Rapi > rou, *kayu > ke; not in inalienably possessed stems, which always "
      "carry an ending (n. 25). Ordered after I-Lowering (n. 26) and A-Assimilation to Glides (n. 27).")
r("e", "i", "next to i", "58", V.format("5, Mid-Vowel Raising", 58) + "*pican > pisi 'how many'.")
r("o", "u", "next to u", "58", V.format("5, Mid-Vowel Raising", 58) + "*tuna > tunu 'eel', *kuron > kuru 'pot'.")

# Inventory (Table 1, p. 48)
for ipa, sym, place, manner, voicing in (
        ("p", "p", "bilabial", "plosive", "voiceless"), ("t", "t", "alveolar", "plosive", "voiceless"),
        ("k", "k", "velar", "plosive", "voiceless"), ("b", "b", "bilabial", "plosive", "voiced"),
        ("d", "d", "alveolar", "plosive", "voiced"), ("ɡ", "g", "velar", "plosive", "voiced"),
        ("ᵐb", "mb", "bilabial", "prenasalized-plosive", "voiced"),
        ("ⁿd", "nd", "alveolar", "prenasalized-plosive", "voiced"),
        ("ᵑɡ", "ŋg", "velar", "prenasalized-plosive", "voiced"), ("s", "s", "alveolar", "fricative", "voiceless"),
        ("z", "z", "alveolar", "fricative", "voiced"), ("m", "m", "bilabial", "nasal", "voiced"),
        ("n", "n", "alveolar", "nasal", "voiced"), ("ŋ", "ŋ", "velar", "nasal", "voiced"),
        ("l", "l", "alveolar", "lateral-approximant", "voiced"), ("r", "r", "alveolar", "trill", "voiced"),
        ("w", "w", "labial-velar", "approximant", "voiced"), ("j", "y", "palatal", "approximant", "voiced")):
    b.ph(L, ipa, "C", place, manner, voicing, sym=sym, page="48")
for ipa, place, manner, rnd in (("i", "front", "close", "unrounded"), ("e", "front", "mid", "unrounded"),
                                ("a", "central", "open", "unrounded"), ("o", "back", "mid", "rounded"),
                                ("u", "back", "close", "rounded")):
    b.ph(L, ipa, "V", place, manner, rounding=rnd, page="48")
b.allo(L, "p", "β", "intervocalic, within a morpheme", "50", "'fricativisation of intramorphemic intervocalic /p/'.")
b.allo(L, "t", "d", "intervocalic after b, d, g, z, within a morpheme", "48", "n. 7; [t] after other consonants and "
       "when not underlyingly intervocalic.")
b.allo(L, "s", "z", "underlyingly intervocalic, no morpheme boundary before it", "52", "n. 12; morpheme-medially "
       "voiceless and voiced oral obstruents contrast only in a few loans (p. 48).")
b.allo(L, "k", "ɡ", "underlyingly intervocalic, within a morpheme", "48",
       "'the voiced versions surfacing when they are underlyingly intervocalic': [ga:ga] /gaka/ 'tomorrow' (p. 50).")

b.dec(D, "How is Bugenhagen's (1994) Mangap-Mbula entered beside Ross's (1988) consonant rows?",
      "Table 1 as Mangap's sourced inventory (prenasalised stops ᵐb ⁿd ᵑɡ beside oral b d ɡ, y = j); Table 3 and the "
      "voiced-stop statement (p. 51) as rows against POC by position (fortis/lenis initial, intervocalic, developed "
      "final), and the vowel rules 1-6 (pp. 53-59) as conditioned rows; Ross's rows are kept. Ross writes the "
      "prenasalised stops b, d, g (his orthography); Bugenhagen's mb, nd, ŋg are the same sounds.",
      "Enter only the inventory and leave the reflexes to Ross (1988).", "48-59")
write("bugenhagen1994-mangap", b.t, """# bugenhagen1994-mangap

Bugenhagen, Robert D. 1994. Language change on Umboi Island. In Tom Dutton & Darrell T. Tryon (eds.), *Language contact and change in the Austronesian world*, 43-108. Berlin: Mouton de Gruyter. Generator: `tools/batch_scripts/duttontryon1994/bugenhagen.py`.

## Scope

- Mangap-Mbula (`mbul1263`): sourced inventory (Table 1, p. 48) and four allophone rows; POC consonant reflexes by position (Table 3, p. 52; voiced stops p. 51); the loss of original final consonants; vowel rules 1-5 (pp. 53-58). Decision `bugenhagen1994-mangap`.

## Not entered

- Rule 6 (geminate vowel reduction) and vowel epenthesis (synchronic), the loan strata (§2.2, Table 4, Appendices 1-3), grammar (§2.3), Kovai (non-Austronesian, §3).
""")
