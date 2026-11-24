#!/usr/bin/env python3
"""Sohn & Bender (1973), A Ulithian grammar, chapter III (Phonology, pp. 17-75).

The Ulithian inventory in the sheet was entered from Lynch's sketch (Lynch et al. 2002: 792-803),
abstracted from this grammar. This batch adds the long (geminate) consonants of the base forms
(pp. 35-36) and the allophones of the phonetic rules that the sketch leaves out. The existing rows
are re-cited to Sohn & Bender in the sheet after the batch lands (see BATCH.md).
"""
from common import Batch, write

S = "sohnbender1973"
L = "ulit1238"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Sohn, Ho-min; Bender, Byron W.", year="1973", title="A Ulithian grammar",
    url_or_doi="https://doi.org/10.15144/PL-C27", kind="grammar",
    notes="Consulted directly on 25 November 2026 (Internet Archive scan in Downloads, no text layer; chapter III "
          "read from page images and OCR). A revised version of the first author's University of Hawaii dissertation of 1969 "
          "(Preface). Data from Mogmog speakers, with Falalop and Fais forms (pp. 5-6). A generative analysis: "
          "the phonemes are those of base forms, from which ordered rules derive the surface forms (§3.6). "
          "The Ulithian sketch of Lynch et al. (2002: 792-803) is abstracted from this grammar.",
    pub_type="book", place="Canberra", publisher="The Australian National University",
    series="Pacific Linguistics C-27"))

LONG = ("Short and long consonants contrast in base forms ('Short vs. long consonants', pp. 35-36); long "
        "segments are 'phonemically geminate' and tense (PR 56, p. 73). n and x have no long counterpart (p. 35).")
for ipa, sym, pl, mn, vo, ex in [
    ("pː", "pp", "bilabial", "plosive", "voiceless", "pale 'dry' : ppale 'light'."),
    ("cː", "cc", "alveolo-palatal", "plosive", "voiceless", "caga 'short of reach' : ccaga 'skinny'."),
    ("kː", "kk", "velar", "plosive", "voiceless", "makili 'sugar cane' : makkala 'comb' (Falalop). Few convincing pairs (p. 25)."),
    ("βʷː", "bb", "bilabial", "fricative", "voiced", "barexe 'hot (taste)' : bbarexe 'pain'."),
    ("fː", "ff", "labiodental", "fricative", "voiceless", "fisi 'star' : ffisi 'lightning'."),
    ("ðː", "dd", "dental", "fricative", "voiced", "dare 'to walk' : ddare 'to run'."),
    ("sː", "ss", "alveolo-palatal", "fricative", "voiceless", "sogo 'mangrove' : ssogo 'angry'."),
    ("mʷː", "ṁṁ", "bilabial", "nasal", "voiced", "ṁolo 'desire' : ṁṁolo 'generous, kind'."),
    ("mː", "mm", "bilabial", "nasal", "voiced", "mata 'eye' : mmata 'to wake up'."),
    ("ŋː", "gg", "velar", "nasal", "voiced", "gata 'hole' : ggata 'hurry'."),
    ("lː", "ll", "alveolar", "lateral-approximant", "voiced", "loyo 'perfume' : lloyo 'wet'."),
    ("rː", "rr", "alveolar", "trill", "voiced", "raxe 'year, age' : rrayi 'happy'."),
    ("jː", "yy", "palatal", "approximant", "voiced", "wayele 'plane' : fayye 'to whet'."),
    ("wː", "ww", "labial-velar", "approximant", "voiced", "wele 'strange' : wwele 'straight'."),
]:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="35-36", notes=f"{LONG} {ex}")

A = b.allo
A(L, "u", "y", "after ð, s, l, m, unless a labiovelar consonant, n, mʷ or w follows", "70",
  "PR 51: 'The high back vowel becomes fronted ([ü]) after the given consonants if not followed by velarised "
  "consonants, n, ṁ, w': dudu 'breast' [düüd], suru 'house-pillar' [süür] (p. 70).")
ASP = "PR 55: p, t, c, k are 'slightly aspirated' before a pause (p. 73); otherwise unaspirated (PR 12, p. 22)."
for c in ("p", "t", "c", "k"):
    A(L, c, c + "ʰ", "_# (before a pause)", "73", ASP)
A(L, "x", "x̟", "before a consonant, a pause, or i, e, æ, ə, u", "73",
  "PR 57: x is 'fronted' before a consonant, a pause or a front or high vowel, 'slightly voiced' after a pause "
  "before ə, and has an offglide before i, e, æ (p. 73).")
DEV = ("Final vowels are dropped, except single back vowels after x, which are devoiced: base buraxo 'smoke', "
       "bulaxa 'taro' end in voiceless [o], [a] (pp. 24, 31; PR 40, p. 61).")
for v, vv in (("o", "o̥"), ("a", "ḁ"), ("u", "u̥")):
    A(L, v, vv, "word-finally after x", "24, 31", DEV)
A(L, "a", "ɑ", "conditioned by the following syllable (retracted unless a front vowel follows)", "26-27, 33",
  "A fronted [a] and a retracted [ɑ] contrast on the surface before a final consonant, but are 'conditioned "
  "variants of a' in base forms: fronted before a front vowel (i, e, æ, ə) in the next syllable, retracted "
  "elsewhere (pp. 26-27, 33; PR 32).")

b.dec("sohnbender1973-schwa",
      "Sohn & Bender (1973: 17, 19) write the Ulithian mid vowel ė as /ə/ but class it as a mid front rounded "
      "vowel (Table II, Figure 4); its usual long realisation is 'very close' to French e (p. 27). Which IPA symbol?",
      "Keep ə (the symbol of the source and of the sheet's inventory); the classification is in the note.",
      "ø (front rounded, as in the feature matrix).", "17, 19, 27")

md = """# sohnbender1973-ulithian

Sohn, Ho-min & Byron W. Bender. 1973. *A Ulithian grammar* (Pacific Linguistics C-27). Canberra: The Australian National University. Read from the Internet Archive scan in Downloads, which has no text layer: chapter III (pp. 17-75) from page images and OCR. Generator: `tools/batch_scripts/four_grammars_2026_11_25/sohnbender1973.py`.

## Scope

- **Long consonants** of the base forms (pp. 35-36): 14 phonemes (pp, cc, kk, bb, ff, dd, ss, ṁṁ, mm, gg, ll, rr, yy, ww). n and x have none; no tt pair is given.
- **Allophones**: fronted [y] for u (PR 51); aspirated final p, t, c, k (PR 55); fronted x (PR 57); final back vowels devoiced after x (pp. 24, 31); fronted and retracted a (pp. 26-27, 33).

## Sheet edits after landing

Lynch's Ulithian rows are an abstract of this grammar and are re-cited to it: the 33 `phonemes` rows (Tables II-III, pp. 17-18, with Sohn & Bender's letters as `source_symbol`: b, d, ṁ, g, à, ȯ, ė, y) and the 7 `allophones` rows (PR 52-53, p. 71; x ~ k, p. 33; light and dark l, pp. 22-23). The `lects` orthography note is updated.

## Decisions

- `sohnbender1973-schwa` (open): ė kept as ə.

## Not entered

- The morphophonemic rules (PR 14-50): stem-vowel alternations before the construct and 3sg suffixes, final-vowel loss with compensatory lengthening, vowel reduction, assimilation of l to coronals.
- The rare long mid-central [ɘ:] (pp. 27, 33-34; PR 58), which the authors derive from ayė/awu sequences, not a phoneme.
- Dialect differences (Falalop, Fais, Mogmog, pp. 5-6): almost all in vowels and semivowels; no rules given.
- Elbert's (1947) Ulithian-Trukese correspondences cited on p. 6 (Ulithian x : Trukese k, l : n, d : t, t : s, s : ∅).
"""
write("sohnbender1973-ulithian", b.t, md)
