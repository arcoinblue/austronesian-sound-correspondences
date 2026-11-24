#!/usr/bin/env python3
"""Jensen (1977), Yapese reference grammar, chapter 2 (Phonology), §§2.3.1-2.3.18 (pp. 13-41).

The first sourced inventory of Yapese (yape1248): 31 consonants (Table 1, p. 38) and 16 vowels (pp. 13-22),
with the allophones of the consonant sections and of palatalization (§2.3.18).
"""
from common import Batch, write

S = "jensen1977a"
L = "yape1248"
b = Batch(S)
# The sources row jensen1977a exists (from Ross 1996); its notes are updated in the sheet after landing.

GL = "Glottalized: the closed glottis is raised suddenly, so the release makes 'a popping sound' (pp. 27-28, 31): an ejective."
GN = ("A plain sonorant 'interrupted by a glottal stop': the glottal stop comes at the beginning word-initially, at the end "
      "word-finally and in the middle word-medially (pp. 34-37).")
C = [
    ("p", "p", "bilabial", "plosive", "voiceless", "23-24", "Voiceless bilabial stop; aspirated word-finally (pp. 23, 27)."),
    ("t", "t", "dental", "plosive", "voiceless", "23-24", "Voiceless dental stop (p. 24)."),
    ("ʈ", "ch", "retroflex", "plosive", "voiceless", "24", "Spelled ch: 'a voiceless retroflexed stop', 'sometimes called a voiceless retroflexed affricate'; Jensen 'will generally refer to it ... as a stop' (p. 24). Ross (1996) writes c (decision jensen1977-symbols)."),
    ("k", "k", "velar", "plosive", "voiceless", "24", "Voiceless velar stop (p. 24)."),
    ("ʔ", "q", "glottal", "plosive", "voiceless", "24-26", "Glottal stop, spelled q, also word-initially before a vowel (pp. 24-26)."),
    ("pʼ", "p'", "bilabial", "plosive", "voiceless", "27-28", "Glottalized bilabial stop. " + GL),
    ("tʼ", "t'", "dental", "plosive", "voiceless", "27-28", "Glottalized dental stop. " + GL),
    ("kʼ", "k'", "velar", "plosive", "voiceless", "27-28", "Glottalized velar stop. " + GL + " There is no glottalized retroflex consonant (pp. 28-29)."),
    ("f", "f", "labiodental", "fricative", "voiceless", "29-30", "Voiceless labiodental fricative (p. 29)."),
    ("θ", "th", "dental", "fricative", "voiceless", "29-30", "Spelled th: voiceless dental fricative (p. 29)."),
    ("ʂ", "s", "retroflex", "fricative", "voiceless", "29-30", "'A voiceless retroflexed fricative', made with the tip of the tongue 'somewhat behind the teeth' (p. 30)."),
    ("fʼ", "f'", "labiodental", "fricative", "voiceless", "30-31", "Glottalized labiodental fricative; rare (pp. 30-31). " + GL + " Ross (1996) writes fˀ."),
    ("θʼ", "th'", "dental", "fricative", "voiceless", "30-31", "Glottalized dental fricative; rare (pp. 30-31). " + GL),
    ("β", "b", "bilabial", "fricative", "voiced", "31-33", "Spelled b: 'a voiced bilabial obstruent', a stop after m and a fricative elsewhere (p. 33). Entered by its usual fricative value (decision jensen1977-symbols); Ross (1996) writes v."),
    ("ð", "d", "dental", "fricative", "voiced", "31-33", "Spelled d: 'a voiced dental obstruent', a stop after n (and for some speakers word-initially), a fricative elsewhere (p. 32)."),
    ("ɣ", "g", "velar", "fricative", "voiced", "31-33", "Spelled g: 'a voiced velar obstruent', a stop after ng and a fricative elsewhere (p. 33)."),
    ("m", "m", "bilabial", "nasal", "voiced", "33-34", "Bilabial nasal (p. 34)."),
    ("n", "n", "dental", "nasal", "voiced", "33-34", "Dental nasal (p. 34). There is no retroflex nasal."),
    ("ŋ", "ng", "velar", "nasal", "voiced", "33-34", "Velar nasal (p. 34)."),
    ("mˀ", "m'", "bilabial", "nasal", "voiced", "34-35", "Glottalized bilabial nasal; common, but rare word-finally (p. 35). " + GN),
    ("nˀ", "n'", "dental", "nasal", "voiced", "34-35", "Glottalized dental nasal (p. 35). " + GN),
    ("ŋˀ", "ng'", "velar", "nasal", "voiced", "34-35", "Glottalized velar nasal, 'extremely rare', in 'three or four words' (p. 35). " + GN),
    ("l", "l", "dental", "lateral-approximant", "voiced", "35-36", "Dental lateral (p. 36)."),
    ("r", "r", "retroflex", "trill", "voiced", "35-36", "'A voiced retroflexed trill': the tongue, 'in a retroflexed position', 'lightly taps the roof of the mouth a few times' (p. 36)."),
    ("lˀ", "l'", "dental", "lateral-approximant", "voiced", "36-37", "Glottalized lateral; there is no glottalized r (pp. 36-37). " + GN),
    ("w", "w", "labial-velar", "approximant", "voiced", "37", "Semivowel (p. 37)."),
    ("j", "y", "palatal", "approximant", "voiced", "37", "Semivowel, spelled y (p. 37)."),
    ("wˀ", "w'", "labial-velar", "approximant", "voiced", "37-38", "Glottalized semivowel, only syllable-finally, ending in a glottal stop; some speakers have q instead (pp. 37-38)."),
    ("jˀ", "y'", "palatal", "approximant", "voiced", "37-38", "Glottalized semivowel, only syllable-finally, ending in a glottal stop (pp. 37-38)."),
]
for ipa, sym, pl, mn, vo, pg, note in C:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page=pg, notes=note)
for ipa, sym, pl, mn, vo, note in [
    ("h", "h", "glottal", "fricative", "voiceless", "Voiceless glottal fricative, 'not a native Yapese sound': only in a few loans (haang 'seal', kaahool 'box'), never word-finally (p. 30)."),
    ("ʐ", "j", "retroflex", "fricative", "voiced", "'A voiced retroflexed obstruent' in 'a very few borrowed words' (juboeng 'trousers'): a fricative, a stop after n (p. 33)."),
]:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="30, 33", notes=note, status="marginal")

LIGHT = ("A light (palatalizing) vowel: next to it, dental and retroflex consonants are palatalized (pp. 20-21, 39-41). "
         "The high vowels are all light.")
PLAIN = "A plain (non-palatalizing) vowel (pp. 20-22)."
V = [  # ipa, symbol, place, height, rounding, light?
    ("i", "i", "front", "close", "unrounded", True), ("e", "e", "front", "mid", "unrounded", True),
    ("ɛ", "ë", "front", "open-mid", "unrounded", False), ("ɵ", "ö", "central", "mid", "rounded", True),
    ("ɔ", "o", "back", "open-mid", "rounded", False), ("æ", "ä", "front", "open", "unrounded", True),
    ("ɑ", "a", "back", "open", "unrounded", False), ("u", "u", "back", "close", "rounded", True),
]
LONG = {"i": "ii", "e": "ee", "ɛ": "ea", "ɵ": "oe", "ɔ": "oo", "æ": "ae", "ɑ": "aa", "u": "uu"}
for ipa, sym, pl, mn, rd, light in V:
    pos = ("Short vowel, placed in the chart of p. 20 (high, mid, lower-mid, low; front, central, back). "
           + (LIGHT if light else PLAIN) + " Decision jensen1977-vowels.")
    b.ph(L, ipa, "V", pl, mn, "", rd, sym=sym, page="16-22", notes=pos)
    b.ph(L, ipa + "ː", "V", pl, mn, "", rd, sym=LONG[ipa], page="13-15, 20-22",
         notes="Long vowel, spelled with a digraph (pp. 13-15). " + (LIGHT if light else PLAIN) + " Decision jensen1977-vowels.")

A = b.allo
ASP = ("'In Yapese, plain voiceless stops at the ends of words are aspirated' (p. 27); elsewhere unaspirated "
       "(p. 12).")
for c in ("p", "t", "ʈ", "k"):
    A(L, c, c + "ʰ", "word-finally", "27", ASP)
A(L, "ʈ", "ʈ͡ʂ", "sometimes", "24", "ch 'may sometimes sound like a type of t sound followed by a sound something like the English sh sound' (p. 24).")
OBS = ("'Voiced obstruents are pronounced as voiced stops when following a nasal, but they are pronounced as voiced "
       "fricatives elsewhere' (p. 33); 'people from certain parts of Yap may use the stop d also in other positions, such "
       "as at the beginning of words' (p. 32).")
A(L, "β", "b", "after m", "33", OBS)
A(L, "ð", "d", "after n; word-initially for some speakers", "32", OBS)
A(L, "ɣ", "ɡ", "after ŋ", "33", OBS)
A(L, "ʐ", "ɖ", "after n", "33", OBS)
PAL = ("Palatalization: 'in Yapese only dental and retroflexed consonants may be palatalized', next to light vowels "
       "(ii, i, uu, u, ee, e, oe, ö, ae, ä); it is clearest in l, r and n and less evident in obstruents (pp. 20-21, 39-41): "
       "mael 'war' has palatalized l, maal 'taro' a plain one.")
for c in ("l", "r", "n", "t", "ð", "θ", "ʂ", "ʈ", "lˀ", "nˀ"):
    A(L, c, c + "ʲ", "next to a light vowel (i, e, ɵ, æ, u, short or long)", "39-41", PAL)

b.dec("jensen1977-symbols",
      "Which IPA symbols for Jensen's (1977) Yapese ch, b d g j and glottalized consonants?",
      "ch = ʈ (Jensen's 'retroflexed stop'; [ʈ͡ʂ] as an allophone); b d g j = β ð ɣ ʐ, their usual fricative values, with "
      "the stops after nasals as allophones; glottalized obstruents as ejectives (pʼ tʼ kʼ fʼ θʼ), glottalized sonorants "
      "with ˀ (mˀ nˀ ŋˀ lˀ wˀ jˀ). After landing, Ross's (1996) Yapese rows are respelled to match: c > ʈ, v > β, fˀ > fʼ "
      "(his vˀ has no counterpart in Jensen and is kept).",
      "ch = ʈ͡ʂ; b d g j = b d ɡ ɖ (stops) with fricative allophones; Ross's symbols kept.", "24, 27-38")
b.dec("jensen1977-vowels",
      "Jensen (1977: 13-22) gives eight short and eight long Yapese vowels by height (high, mid, lower-mid, low) and "
      "backness (front, central, back). Which IPA symbols?",
      "Short i e ë ö o ä a u = i e ɛ ɵ ɔ æ ɑ u; long ii ee ea oe oo ae aa uu = iː eː ɛː ɵː ɔː æː ɑː uː.",
      "ö, oe as ə/əː (unrounded); o, oo as o/oː; a, aa as a/aː.", "13-22")

md = """# jensen1977-yapese

Jensen, John Thayer (with John Baptist Iou, Raphael Defeg & Leo David Pugram). 1977. *Yapese reference grammar* (PALI Language Texts: Micronesia). Honolulu: The University Press of Hawaii. Chapters 1-2 in Downloads (a scan of rotated two-page spreads), read from page images and OCR. Generator: `tools/batch_scripts/six_sources_2026_11_25/jensen1977.py`.

## Scope

- **Inventory** (§2.3, Table 1 p. 38; vowels pp. 13-22): the first sourced inventory of Yapese (`yape1248`): 29 consonants and the marginal loan h, ʐ; 8 short and 8 long vowels. Decisions `jensen1977-symbols` and `jensen1977-vowels` (open).
- **Allophones**: aspirated final stops (p. 27); affricate ch (p. 24); stop values of the voiced obstruents after nasals (pp. 32-33); palatalized dental and retroflex consonants next to light vowels (§2.3.18).

## Sheet edits after landing (decision `jensen1977-symbols`)

- `sources` (jensen1977a): notes and series (consulted directly on 25 Nov 2026, chapters 1-2; PALI Language Texts: Micronesia).
- `correspondences`: Ross's (1996) Yapese rows respelled to Jensen's IPA: c > ʈ, v > β, fˀ > fʼ (his letter in `source_form`); vˀ kept.
- `lects` (Yapese): orthography note.

## Not entered

- §2.4 (morphemes) and §2.5 (morphophonemics: vowel reduction and loss of final short vowels, sound changes, dialects); the scan ends in chapter 2.
- The uncertain quality of non-final short vowels (§2.3.2.1), which Jensen treats under morphophonemics.
"""
write("jensen1977-yapese", b.t, md)
