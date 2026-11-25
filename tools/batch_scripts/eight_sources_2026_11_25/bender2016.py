#!/usr/bin/env python3
"""Bender, Capelle & Pagotto (2016), Marshallese reference grammar, chapter 2 (The sound system, pp. 19-50).

The first sourced inventory of Marshallese (mars1254): 22 consonants (Table 2-1, p. 25) and 4 vowels (§2.3).
The book gives no IPA: it describes the consonants as light, heavy and rounded and the vowels by height only,
with front, back unrounded and back rounded sounds set by the flanking consonants. The IPA is decision bender2016-ipa.
"""
from common import Batch, write

S = "bender2016"
L = "mars1254"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Bender, Byron W.; Capelle, Alfred; Pagotto, Louise", year="2016", title="Marshallese reference grammar",
    kind="grammar", notes="Consulted directly on 25 November 2026 (chapter 2, The sound system of Marshallese). Phonemic "
                          "transcription in braces is that of the Marshallese-English dictionary, with ẹ for & and kʷ for q (p. 20).",
    pub_type="book", place="Honolulu", publisher="University of Hawai'i Press", series="PALI Language Texts: Micronesia"))

LIGHT = "Light (palatalized): the oral tube kept as short as possible (pp. 20-21)."
HEAVY = "Heavy (velarized): 'the back of the tongue is raised' toward the velum (p. 21)."
ROUND = "Rounded (velarized and labialized): heavy, with the lips protruded and pursed (p. 21)."
C = [  # ipa, spelling {transcription}, place, manner, group note
    ("pʲ", "p {p}", "bilabial", "plosive", "Light labial stop. " + LIGHT),
    ("pˠ", "b {b}", "bilabial", "plosive", "Heavy labial stop. " + HEAVY + " Voicing is not distinctive; the stops have "
     "'prompt onset of voicing for the following vowel and no aspiration' (pp. 35-36)."),
    ("mʲ", "m {m}", "bilabial", "nasal", "Light labial nasal. " + LIGHT),
    ("mˠ", "ṃ {ṃ}", "bilabial", "nasal", "Heavy labial nasal. " + HEAVY),
    ("tʲ", "j {j}", "dental", "plosive", "Light dental stop. " + LIGHT + " With 'a bit of frication in its release' (p. 37)."),
    ("tˠ", "t {t}", "dental", "plosive", "Heavy dental stop. " + HEAVY),
    ("nʲ", "n {n}", "dental", "nasal", "Light dental nasal. " + LIGHT),
    ("nˠ", "ṇ {ṇ}", "dental", "nasal", "Heavy dental nasal. " + HEAVY),
    ("nʷ", "ṇw {ṇʷ}", "dental", "nasal", "Rounded dental nasal, 'a rare sound in Marshallese' (p. 28). " + ROUND),
    ("k", "k {k}", "velar", "plosive", "(Heavy) velar stop; there are no light velars (p. 25). It closes 'against the same "
     "part of the velum whether vowels are front or back' (p. 37)."),
    ("kʷ", "kw {kʷ}", "velar", "plosive", "Rounded velar stop. " + ROUND),
    ("ŋ", "ñ {g}", "velar", "nasal", "(Heavy) velar nasal, transcribed {g}."),
    ("ŋʷ", "ñw {gʷ}", "velar", "nasal", "Rounded velar nasal. " + ROUND),
    ("lʲ", "l {l}", "alveolar", "lateral-approximant", "Light lateral. " + LIGHT),
    ("lˠ", "ḷ {ḷ}", "alveolar", "lateral-approximant", "Heavy lateral: the tongue tip against the back of the upper teeth "
     "or the gum ridge, open at the sides (p. 24). " + HEAVY),
    ("lʷ", "lw {ḷʷ}", "alveolar", "lateral-approximant", "Rounded lateral. " + ROUND),
    ("rʲ", "d {d}", "alveolar", "trill", "Light retroflex, spelled d (p. 21). " + LIGHT),
    ("rˠ", "r {r}", "alveolar", "trill", "Heavy retroflex: the tongue curled back and trilled 'against the gum ridge behind "
     "the upper teeth' (p. 24). " + HEAVY),
    ("rʷ", "rw {rʷ}", "alveolar", "trill", "Rounded retroflex. " + ROUND),
    ("j", "— {y}", "palatal", "approximant", "Light semiconsonant {y}, not written in the spelling (pp. 34-35)."),
    ("ɰ", "— {h}", "velar", "approximant", "Heavy semiconsonant {h}: the tongue root drawn back and the back of the tongue "
     "raised toward the velum, 'not as breathy as the English h' (pp. 34-35)."),
    ("w", "w {w}", "labial-velar", "approximant", "Rounded semiconsonant: {h} with lip rounding added (pp. 34-35)."),
]
for ipa, sym, pl, mn, note in C:
    vo = "voiced" if mn in ("nasal", "lateral-approximant", "trill", "approximant") else ""
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="20-35",
         notes=note + " Table 2-1 (p. 25); IPA per decision bender2016-ipa.")

VN = ("Height is the only distinctive dimension of the vowels: 'whether a vowel has a front or back sound ... and whether "
      "a back vowel is rounded or not ... are determined by the consonants on either side' (p. 39). IPA per decision "
      "bender2016-ipa.")
V = [("ɨ", "{i}: i, ū, u", "close", "The high vowel phoneme {i} (§2.3.1, pp. 39-42)."),
     ("ɘ", "{ẹ}: e, ō, o", "close-mid",
      "The high-mid 'derived' vowel {ẹ}, from a combination of {i} and {e} (§2.5.3); it contrasts with both (ki {kiy} "
      "'key' : ke {kẹy} 'porpoise' : ke {key} 'when') but is spelled like {e} and is 'unstable', interchanging with {e} "
      "between dialects and speakers (Rālik {ṃẹk} : Ratak {ṃek} 'tired') (§2.3.4, pp. 48-49)."),
     ("ə", "{e}: e, ō, o", "mid", "The mid vowel phoneme {e} (§2.3.2, pp. 43-44)."),
     ("ɐ", "{a}: ā, a, ọ", "open", "The low vowel phoneme {a} (§2.3.3, pp. 45-46).")]
for ipa, sym, mn, note in V:
    b.ph(L, ipa, "V", "central", mn, "", "", sym=sym, page="38-49", notes=note + " " + VN)

A = b.allo
ENV = {"F": "between light consonants", "B": "between heavy consonants", "R": "between rounded consonants"}
SOUNDS = {"ɨ": [("i", "F", "i"), ("ɯ", "B", "ū"), ("u", "R", "u")],
          "ɘ": [("e", "F", "e"), ("ɤ", "B", "ō"), ("o", "R", "o")],
          "ə": [("ɛ", "F", "e"), ("ʌ", "B", "ō"), ("ɔ", "R", "o")],
          "ɐ": [("æ", "F", "ā"), ("ɑ", "B", "a"), ("ɒ", "R", "ọ")]}
for ph, rows in SOUNDS.items():
    for allo, k, letter in rows:
        A(L, ph, allo, ENV[k], "38-49",
          f"Spelled {letter}. 'Each of the three phonemes has three distinct sounds: a front vowel sound when between light "
          "consonants, a back unrounded vowel sound when between heavy consonants, and a back rounded vowel sound when "
          "between rounded consonants' (p. 40); between consonants of different groups the vowel glides from one sound to "
          "the other (kij {kij} 'louse', p. 41). The IPA of the sounds is decision bender2016-ipa.")
for c in ("pʲ", "pˠ", "tʲ", "tˠ", "k", "kʷ"):
    A(L, c, c + "̚", "word-final", "36-37", "'Marshallese stops coming at the end of a word are generally not released, nor "
      "are they voiced as much as they might be at the beginning of a word or between vowels' (p. 36).")
for allo in ("t͡ʃ", "s", "z", "ʃ"):
    A(L, "tʲ", allo, "variation between words and speakers, especially younger speakers", "37",
      "{j} 'shows considerable variation in pronunciation from word to word and from speaker to speaker': jaja may be "
      "heard as chacha, sasa, zaza or shasha (a 'lisping' called weejej), spread from its use for English fricatives and "
      "affricates in loanwords (pp. 36-37).")

b.dec("bender2016-ipa",
      "Bender et al. (2016) give no IPA for Marshallese. Which IPA for their consonants and vowels?",
      "Light, heavy, rounded = palatalized, velarized, labialized(-velarized): p b m ṃ j t n ṇ ṇw k kw ñ ñw l ḷ lw d r rw "
      "{y} {h} w = pʲ pˠ mʲ mˠ tʲ tˠ nʲ nˠ nʷ k kʷ ŋ ŋʷ lʲ lˠ lʷ rʲ rˠ rʷ j ɰ w; the vowels by height only, with central "
      "symbols: {i} {ẹ} {e} {a} = ɨ ɘ ə ɐ, and their sounds between light, heavy and rounded consonants as allophones "
      "[i ɯ u], [e ɤ o], [ɛ ʌ ɔ], [æ ɑ ɒ] (the usual IPA of Marshallese, as in Choi 1992, not consulted). After landing, the "
      "Marshallese rows of Bender et al. (2003a), in their comparative transcription, are respelled to this IPA "
      "(p > pʲ, bʷ > pˠ, m > mʲ, mʷ > mˠ, j > tʲ, t > tˠ, n > nʲ, ņ > nˠ, ņʷ > nʷ, l > lʲ, ļ > lˠ, ļʷ > lʷ, d > rʲ, r > rˠ, "
      "y > j), with the old symbol in source_form (sheet edits).",
      "Keep the comparative transcription for the rows and enter the inventory in the book's transcription {p b ...}.",
      "20-49")

md = """# bender2016-marshallese

Bender, Byron W., Alfred Capelle & Louise Pagotto. 2016. *Marshallese reference grammar* (PALI Language Texts: Micronesia). Honolulu: University of Hawai'i Press. Generator: `tools/batch_scripts/eight_sources_2026_11_25/bender2016.py`.

## Scope

- **Inventory** (Table 2-1, p. 25; §2.3): the first sourced inventory of Marshallese (`mars1254`): 22 consonants in three series (light, heavy, rounded) and 4 vowels distinguished by height ({ẹ} is the 'derived' high-mid vowel).
- **Allophones**: the front, back unrounded and back rounded sound of each vowel between light, heavy and rounded consonants (12 rows); unreleased final stops; the variable fricative pronunciations of {j}.
- Decision `bender2016-ipa` (open): the book gives no IPA.

## Sheet edits after landing

- `mars1254`: orthography note (IPA per bender2016-ipa); the rows of Bender et al. (2003a) respelled to it (`sheet_edits.py`).

## Not entered

- The vowel sounds in mixed environments (Tables 2-13 to 2-16: spelling of glides between consonants of different groups).
- Initial double consonants, medial clusters and the "diphthongs" and "long" vowels (§§2.4-2.5), and the Rālik-Ratak differences, apart from the instability of {ẹ}.
"""
write("bender2016-marshallese", b.t, md)
