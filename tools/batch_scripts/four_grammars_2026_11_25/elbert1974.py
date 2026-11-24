#!/usr/bin/env python3
"""Elbert (1974), Puluwat grammar, chapter 1 (Phonology, pp. 1-15).

The Puluwatese inventory in the sheet was entered from Lynch's sketch (Lynch et al. 2002: 804-814),
which is abstracted from Elbert's works. This batch adds what the sketch leaves out: the long
(geminate) consonants and the allophones of chapter 1. The existing phoneme and allophone rows are
re-cited to Elbert in the sheet after this batch lands (see BATCH.md).
"""
from common import Batch, write

S = "elbert1974"
L = "pulu1242"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Elbert, Samuel H.", year="1974", title="Puluwat grammar", url_or_doi="https://doi.org/10.15144/PL-B29",
    kind="grammar",
    notes="Consulted directly on 25 November 2026 (Internet Archive scan in Downloads; Table 1 and the liquids "
          "of p. 7 read from the page images). Chapter 1 (pp. 1-15) is the phonology. Puluwat Atoll, with "
          "notes on the closely related Ulul and Pisarach dialects (p. v). The Puluwatese sketch of Lynch "
          "et al. (2002: 804-814) is abstracted from Elbert's works.",
    pub_type="book", place="Canberra", publisher="The Australian National University",
    series="Pacific Linguistics B-29"))

# Long consonants: 'All consonants except /w y/ occur long and short, but long /r ŕ s/ are rare' (p. 2).
LONG = ("'All consonants except /w y/ occur long and short' (p. 2); written double. Geminates are extremely "
        "fortis word-medially and lenis word-initially, and are replaced by single consonants in "
        "utterance-final position (p. 2).")
for ipa, sym, pl, mn, vo, extra in [
    ("pː", "pp", "bilabial", "plosive", "voiceless", "Rare (p. 4)."),
    ("pʷː", "ppw", "bilabial", "plosive", "voiceless", "'Geminated /pw/ and /mw/ do not keep the velarisation of the first member and are written /ppw mmw/' (p. 2); rare, not noted medially (p. 4)."),
    ("tː", "tt", "dental", "plosive", "voiceless", ""),
    ("t͡ʃː", "cc", "postalveolar", "affricate", "voiceless", "'The release of /-cc/ is quite audible' (p. 4)."),
    ("kː", "kk", "velar", "plosive", "voiceless", ""),
    ("fː", "ff", "labiodental", "fricative", "voiceless", "Not noted word-finally (p. 2)."),
    ("sː", "ss", "dental", "fricative", "voiceless", "Rare (p. 2)."),
    ("hː", "hh", "glottal", "fricative", "voiceless", ""),
    ("mː", "mm", "bilabial", "nasal", "voiced", "Not noted word-finally (p. 6)."),
    ("mʷː", "mmw", "bilabial", "nasal", "voiced", "Written mmw (p. 2); not noted word-finally (p. 6)."),
    ("nː", "nn", "dental", "nasal", "voiced", ""),
    ("ŋː", "ngng", "velar", "nasal", "voiced", "Written nng; not noted word-finally (p. 6)."),
    ("lː", "ll", "alveolar", "lateral-approximant", "voiced", "Common initially and medially, rare finally (p. 7)."),
    ("rː", "ŕŕ", "alveolar", "trill", "voiced", "Rare; noted only medially (p. 7)."),
    ("ɻː", "rr", "retroflex", "approximant", "voiced", "Rare; noted only medially (p. 7)."),
]:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="2", notes=(LONG + " " + extra).strip())

A = b.allo
# Stops (p. 2, p. 4). The weak voicing of p t k c is already in the sheet (Lynch's rows, re-cited).
A(L, "p", "pʲ", "some dialects, some words", "4",
  "'A slightly palatalised [py] has been noted in some dialects, but no minimal pairs have been found, and "
  "informants vary as to degree of palatalisation or its complete absence' (p. 4); examples 'shark' and 'belt'.")
A(L, "t", "t̚", "_# (before a pause, sometimes)", "4", "'/-t -k/ are sometimes unreleased before a pause' (p. 4).")
A(L, "k", "k̚", "_# (before a pause, sometimes)", "4", "'/-t -k/ are sometimes unreleased before a pause' (p. 4).")
A(L, "t͡ʃ", "t͡s", "speech of school children", "4",
  "'School children often pronounce /c/ as [ts], but this may be a fad' (p. 4). Elbert calls /c/ an alveolar affricate.")
KG = ("'/k-/ is replaced by the glides /w-/ and /y-/ in some words', as kapong ~ yapong-i-y 'to greet', "
      "kereker ~ yereker 'rat', koow ~ woow 'coconut fibre'; also by ∅ (kee, yee, ee 'fishhook') (p. 4). "
      "Lexical variation, not a regular rule.")
A(L, "k", "w", "word-initially, in some words", "4", KG)
A(L, "k", "j", "word-initially, in some words", "4", KG)
A(L, "m", "mʲ", "before o (sometimes)", "6",
  "'/m/ is sometimes slightly palatalised before /o/, contrasting with unpalatalised /mw/' (p. 6).")
VEL = ("'The closure of the lips with /-pw -mw/ may be slight and rapid or even lacking' in utterance-final "
       "position, where they are hard to tell from /p m/ (p. 3).")
A(L, "pʷ", "p", "_# and before u, ɨ, o (contrast hard to hear)", "3", VEL)
A(L, "mʷ", "m", "_# and before u, o (contrast hard to hear)", "3,6", VEL)
GL = ("Between like vowels /w/ and /y/ may be realised 'as an open transition with rearticulation or even a "
      "glottal stop': [wupwuuwupw] 'to hit', [le ʔefáng] 'season without breadfruit' (p. 8). Glides before "
      "phonetically similar vowels are not heard after consonants in fast speech (p. 8).")
A(L, "w", "ʔ", "between like vowels", "8", GL)
A(L, "j", "ʔ", "between like vowels", "8", GL)
# Vowels (p. 11).
A(L, "eː", "ɛː", "", "11", "'/e/ suggests the vowel in English bed, and is a little lower when lengthened' (p. 11).")
A(L, "æ", "e", "fast speech", "11", "'In fast speech /á/ may be replaced by /e/, as in páyiy and peyiy my hand' (p. 11).")
A(L, "a", "ɛ", "after pʷ, mʷ, in fast speech", "3,11",
  "'/a/ ... after velarised consonants is in fast speech raised almost to /e/, as in pwangipwang custom or "
  "mmwan before' (p. 11); 'after /pw mw/ ... /a/ is slightly raised' (p. 3).")
CEN = ("'After /pw mw/ the back vowels and /é/ seem to be slightly centered' (p. 3); '/u/ is somewhat "
       "centered after velarised consonants, as in roopwut woman' (p. 11). A similar centering follows /w-/ (p. 3).")
A(L, "u", "ʉ", "after pʷ, mʷ, w", "3,11", CEN)
A(L, "o", "ɵ", "after pʷ, mʷ, w", "3", CEN)

b.dec("elbert1974-affricate",
      "Elbert (1974: 4) calls Puluwatese /c/ 'an alveolar affricate' and says school children 'often "
      "pronounce /c/ as [ts], but this may be a fad'. Which IPA symbol?",
      "Keep t͡ʃ (the symbol of the sheet's inventory, after Lynch et al. 2002); [ts] is entered as an allophone. "
      "Elbert's remark implies that the usual value is not [ts]; Jackson (1984: 261) gives a retroflex [ṭʃ] "
      "for the geminate.",
      "t͡s (Elbert's 'alveolar'); ʈ͡ʂ (Jackson's retroflex, as Woleaian).", "4")

md = """# elbert1974-puluwatese

Elbert, Samuel H. 1974. *Puluwat grammar* (Pacific Linguistics B-29). Canberra: The Australian National University. Read from the scan in Downloads; Table 1 (p. 1) and the liquids (p. 7) from page images. Generator: `tools/batch_scripts/four_grammars_2026_11_25/elbert1974.py`.

## Scope

- **Long consonants** (p. 2): 15 phonemes. 'All consonants except /w y/ occur long and short'; the sheet's inventory (from Lynch et al. 2002, a sketch abstracted from Elbert) had only the long vowels.
- **Allophones** (chapter 1): palatalised [pʲ] in some dialects; unreleased final t, k; [t͡s] for c among school children; word-initial k varying with w, j in some words; [mʲ] before o; weak lip closure of final pʷ, mʷ; glides as [ʔ] between like vowels; lowered long e; æ ~ e and raised a in fast speech; centred u, o after labiovelars.

## Sheet edits after landing

Lynch's Puluwatese rows are an abstract of Elbert, so they are re-cited to the original (as the Tsou and Kanakanavu rows were on 22 Nov 2026):

- `phonemes` (Puluwatese rows): `source_id` elbert1974, Elbert's pages and symbols. Lynch's ɾ becomes **ɻ**: Elbert's /r/ 'suggests an American "r" ... the tongue is often raised towards the hard palate', and his /ŕ/ is 'a double-tap trill' (p. 7); the rows of Bender et al. and Jackson already write ɻ and r for them.
- `allophones` (Puluwatese rows): re-cited to pp. 2, 4, 5, 11.
- `lects` (Puluwatese): orthography note (IPA after Elbert; the rows were already IPA).

## Decisions

- `elbert1974-affricate` (open): /c/ kept as t͡ʃ.

## Not entered

- 'Stops and fricatives are generally voiceless initially, weakly voiced medially' (p. 2), but 'the fricatives ... are always voiceless' (p. 5): only the stops get voiced allophones (as already in the sheet).
- c ~ ɻ interchange in a few words (caw, raw 'slow'), which Elbert puts down to Trukese influence (p. 5); s ~ h in loanwords (already in the sheet).
- Pitch, junctures and the excrescent vowels between consonants (pp. 10, 14-15); morphophonemics (chapter 2).
- The Ulul and Pisarach dialects (data in the grammar, no phonology of their own).
"""
write("elbert1974-puluwatese", b.t, md)
