#!/usr/bin/env python3
"""Oda (1977), The syntax of Pulo Annian, chapter II (Phonology, pp. 9-24) and the notes to chapter I.

The first sourced inventory of Pulo-Annan (pulo1240): Table I (p. 9), the geminate consonants and vowels
(pp. 11-13), and the allophones of the phonological rules PR 1-14 (pp. 13-20). Oda's notes to chapter I
(p. 7) describe Sonsorolese f and l; they go on the Sonsorolese lect (sons1243).
"""
from common import Batch, write

S = "oda1977"
L = "pulo1240"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Oda, Sachiko", year="1977", title="The syntax of Pulo Annian: A Nuclear Micronesian language",
    kind="grammar",
    notes="University of Hawaii dissertation, 1977. Consulted directly on 25 November 2026 (microfilm scan in "
          "Downloads; Table I and the rules of chapter II read from the page images). Data from Pulo Annian "
          "speakers in Echang, Palau (pp. 5-6). Oda refers the historical development of the phonemes from "
          "Proto-Oceanic to her unpublished 'Proto-Oceanic reflexes in Pulo Annian' (1976a; ch. II, n. 1), not seen. "
          "Data source of the Pulo-Annan column of Bender et al. (2003a).",
    pub_type="thesis", place="Honolulu", publisher="University of Hawaii dissertation"))

P9 = "Table I, p. 9."
C = [
    ("p", "p", "bilabial", "plosive", "voiceless", "Labial stop (Table I). A geminate is fortis, a single one lenis (p. 12)."),
    ("pʷ", "pw", "bilabial", "plosive", "voiceless", "Labio-velar stop (Table I); written pʷ. Single pʷ is always a voiced fricative [βʷ] (PR 4)."),
    ("t", "t", "alveolar", "plosive", "voiceless", "Alveolar stop (Table I). A geminate is fortis, a single one lenis (p. 12)."),
    ("k", "k", "velar", "plosive", "voiceless", "Velar stop (Table I). Single k is a fricative [x] (PR 4)."),
    ("ð", "d", "alveolar", "fricative", "voiced", "Written d; an alveolar fricative in Table I ([+continuant, -strident], Table II, p. 10), [ð] in the phonetic transcriptions ([ðaɨlɨ] 'deed', p. 14). In Pulo Annian it continues both Sonsorolese f and d (ch. I, n. 7). Jackson (1983: 17; 1984: 261) gives the value [θ], Bender et al. (2003a) and Jackson (1986) [ð]."),
    ("s", "s", "alveolar", "fricative", "voiceless", "Alveolar fricative (Table I)."),
    ("m", "m", "bilabial", "nasal", "voiced", "Labial nasal (Table I)."),
    ("mʷ", "mw", "bilabial", "nasal", "voiced", "Labio-velar nasal (Table I); written mʷ."),
    ("n", "n", "alveolar", "nasal", "voiced", "Alveolar nasal (Table I). Single n is a flap [ɾ] (PR 6)."),
    ("ŋ", "ŋ", "velar", "nasal", "voiced", "Velar nasal (Table I)."),
    ("l", "l", "alveolar", "lateral-approximant", "voiced", "Lateral (Table I). 'Pulo Annian /l/ is apical and more like the English clear /l/', against the velarised Sonsorolese l (ch. I, n. 7)."),
    ("w", "w", "labial-velar", "approximant", "voiced", "Labio-velar glide (Table I). Initial glides are underlying segments (ch. II, n. 3)."),
    ("j", "y", "palatal", "approximant", "voiced", "Glide written y (Table I). Initial glides are underlying segments (ch. II, n. 3)."),
]
for ipa, sym, pl, mn, vo, note in C:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="9", notes=note)
V = [
    ("i", "front", "close", "unrounded", "", ""),
    ("e", "front", "mid", "unrounded", "", ""),
    ("a", "central", "open", "unrounded", "", "Table I places a under the back unrounded column."),
    ("ə", "", "mid", "unrounded", "", "Mid back unrounded vowel in Table I."),
    ("ɨ", "", "close", "unrounded", "ɨ", "High back unrounded vowel in Table I (written ɨ)."),
    ("o", "back", "mid", "rounded", "", ""),
    ("u", "back", "close", "rounded", "", ""),
]
for v, pl, mn, rd, sym, note in V:
    b.ph(L, v, "V", pl, mn, "", rd, sym=sym or v, page="9", notes=note)
LV = ("'There is an underlying contrast between single and geminate vowels even though the phonetic length of "
      "the geminates is often neutralized on the surface' (p. 12); written double. 'A geminate e is yet to be found' (p. 13).")
for v, pl, mn, rd, ex in [("iː", "front", "close", "unrounded", "pwidi : pwidi-i"), ("aː", "central", "open", "unrounded", "mata 'eye' : maata 'garden'"),
                          ("əː", "", "mid", "unrounded", "nnəi 'to be wet' : təədi 'to be true'"), ("oː", "back", "mid", "rounded", "toko : sidoosia"),
                          ("uː", "back", "close", "rounded", "upwu : suusu"), ("ɨː", "", "close", "unrounded", "titi 'breast' : tittii 'to bathe'")]:
    b.ph(L, v, "V", pl, mn, "", rd, sym=v[0] * 2, page="12-13", notes=f"{LV} {ex} (p. 13).")
LC = ("'There exists a contrast between a single and a geminate consonants' (p. 11); written double. 'Initial "
      "geminate consonants are difficult to elicit' (p. 12).")
for ipa, sym, pl, mn, vo, ph in [
    ("pː", "pp", "bilabial", "plosive", "voiceless", "fortis (p. 12)"),
    ("pʷː", "pwpw", "bilabial", "plosive", "voiceless", "a stop, against the fricative single pʷ (p. 12)"),
    ("tː", "tt", "alveolar", "plosive", "voiceless", "fortis (p. 12)"),
    ("kː", "kk", "velar", "plosive", "voiceless", "a stop, against the fricative single k (p. 12)"),
    ("ðː", "dd", "alveolar", "fricative", "voiced", "with 'a slight affricate-like stoppage at the onset' (p. 12)"),
    ("sː", "ss", "alveolar", "fricative", "voiceless", "with 'a slight affricate-like stoppage at the onset' (p. 12)"),
    ("mː", "mm", "bilabial", "nasal", "voiced", "longer (p. 12)"),
    ("mʷː", "mwmw", "bilabial", "nasal", "voiced", "longer (p. 12)"),
    ("nː", "nn", "alveolar", "nasal", "voiced", "a nasal, against the flap single n (p. 12)"),
    ("ŋː", "ŋŋ", "velar", "nasal", "voiced", "longer (p. 12)"),
]:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="11-12", notes=f"{LC} Phonetically {ph}.")

A = b.allo
PR4 = ("PR 4, Consonant Weakening: 'Single k and pʷ are weakened and become fricatives. However, a single k is not "
       "obligatorily voiced (see PR 13), while a single pʷ is always voiced', word-initially before a vowel, between "
       "vowels and word-finally after a vowel: /kaɨ/ [xaɨ] 'to tell', /kapʷaɨkɨ/ [xaβʷaɨxɨ] 'to see' (p. 15).")
A(L, "k", "x", "single: #_V, V_V, V_#", "15", PR4)
A(L, "pʷ", "βʷ", "single: #_V, V_V, V_#", "15", PR4)
A(L, "k", "ɣ", "single, between voiced vowels (allegro speech, optional)", "19",
  "PR 13, Consonant Voicing (optional): the velar fricative from PR 4 'becomes voiced between two voiced vowels. "
  "This rule is not obligatory and only applies in allegro speech': /keli + keli/ [xeliɣelI] 'to scratch' (p. 19).")
A(L, "n", "ɾ", "single: #_V, V_V, V_#", "16",
  "PR 6, Denasalization: 'The alveolar nasal n is denasalized and becomes a flap [ɾ] ... when it occurs singly': "
  "/ɨnɨmɨ/ [ɨɾɨmɨ] 'to drink it', /nnaɨ/ [nnaɨ] 'good taste' (p. 16).")
PR10 = ("PR 10, Velarization and Rounding of Bilabials: 'A bilabial nasal m and a bilabial stop p become velarized "
        "before a round vowel'; single pʷ and p still contrast there ([βʷ] against [pʷ]), geminate pp and pʷpʷ do not "
        "(p. 18): /moni/ [mʷorI] 'already'.")
A(L, "m", "mʷ", "before a rounded vowel", "18", PR10)
A(L, "p", "pʷ", "before a rounded vowel", "18", PR10)
PR9 = ("PR 9, Vowel Devoicing: 'A final vowel is devoiced at phrase-boundary' (not after another vowel); it may be "
       "half-devoiced, whispered, or not phonated (p. 17). 'All the seven vowels become unvoiced vowels.'")
for v, vv in (("i", "i̥"), ("e", "e̥"), ("a", "ḁ"), ("ə", "ə̥"), ("ɨ", "ɨ̥"), ("o", "o̥"), ("u", "u̥")):
    A(L, v, vv, "word-final at a phrase boundary, after a consonant", "17", PR9)
A(L, "a", "æ", "before a single (short) high front vowel in the next syllable (optional)", "20",
  "PR 14, Low Vowel Fronting (optional): 'free variation between a single [a] and [æ] before a single high front "
  "vowel', varying among speakers: /malippi/ [mælippI] or [malippI] 'to be cracked' (p. 20).")
A(L, "a", "e", "single, between high unrounded vowels", "18",
  "PR 11, Low Vowel Raising and Fronting: a single low vowel is fronted and raised between two high unrounded "
  "vowels: /simʷa + i/ [simʷei] 'my head' (p. 18).")

# Sonsorolese, from Oda's notes to chapter I (p. 7).
SN = ("Oda (1977: 7, ch. I, n. 7): 'Sonsorolese /f/ (intervocalically [v]) and /d/ are merged into Pulo Annian /d/. "
      "Sonsorolese /l/ is velarized and has some fricative quality, while Pulo Annian /l/ is apical'.")
A("sons1243", "f", "v", "V_V", "7", SN)
A("sons1243", "l", "ɫ", "", "7", SN)

b.dec("oda1977-pua-rows",
      "Pulo-Annan now has a sourced inventory (Oda 1977: 9). Earlier rows write its reflexes in other ways: "
      "Bender et al. (2003a) d; Jackson (1983, 1984) θ ('PUA d is [θ]'); Jackson (1983, 1984, 1986) x and βʷ for "
      "single k and pʷ, which Oda treats as allophones (PR 4); Jackson (1984: 261) f for PTK *f, where Oda's "
      "Pulo Annian has no f (Sonsorolese f > Pulo Annian d, ch. I, n. 7). How are these rows written?",
      "d and θ respelled ð in the sheet (the letter in source_form, Jackson's value in the notes), as Puluwatese "
      "t͡ʃ was; x, βʷ and f kept as printed, so the build warns that they are not in the sourced inventory.",
      "Respell x > k and βʷ > pʷ as well (the allophones are in the allophones tab); or keep θ as printed.", "7, 9, 15")

md = """# oda1977-puloannian

Oda, Sachiko. 1977. *The syntax of Pulo Annian: A Nuclear Micronesian language*. Honolulu: University of Hawaii dissertation. Read from the microfilm scan in Downloads; the text layer garbles the symbols, so Table I (p. 9) and the rules (pp. 14-20) were read from page images. Generator: `tools/batch_scripts/four_grammars_2026_11_25/oda1977.py`.

## Scope

- **Inventory** (Table I, p. 9): the first sourced inventory of Pulo-Annan (`pulo1240`): 13 consonants (p pʷ t k ð s m mʷ n ŋ l w j) and 7 vowels (i e a ə ɨ o u), in IPA; Oda's d is [ð] in her transcriptions.
- **Long vowels and geminate consonants** (pp. 11-13): 6 long vowels (no long e found), 10 geminates.
- **Allophones**: PR 4 (single k [x], pʷ [βʷ]), PR 6 (single n [ɾ]), PR 9 (final devoicing of all seven vowels), PR 10 (m, p labialised before rounded vowels), PR 11, PR 13 ([ɣ] in allegro speech), PR 14 (a ~ æ).
- **Sonsorolese** (`sons1243`, ch. I, n. 7, p. 7): f [v] between vowels; velarised l.

## Sheet edits after landing (decision `oda1977-pua-rows`)

- `lects` (Pulo-Annan): orthography note: IPA after Oda (1977: 9).
- `correspondences` (Pulo-Annan): Bender et al.'s d (from PCK *f, *t, *T) and Jackson's θ (1983, 1984) respelled ð, with d in `source_form` and Jackson's [θ] in the notes.

## Not entered

- The morphophonemic rules PR 1, 2, 3, 5, 7, 8, 12 (glide epenthesis, lengthening, deletion, assimilation across morpheme boundaries) and stress and pitch (§2.5).
- Tobian: Oda's six cognate sets (ch. I, n. 8: Tobian x for l, s for Pulo Annian d, č for s) are dialect comparisons with no proto-language; Tobian is not a lect in the database.
- Oda (1976a), 'Proto-Oceanic reflexes in Pulo Annian' (MS), not seen.
- The dictionary in the appendix.
"""
write("oda1977-puloannian", b.t, md)
