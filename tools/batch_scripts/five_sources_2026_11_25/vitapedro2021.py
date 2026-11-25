#!/usr/bin/env python3
"""Vita & Pedro (2021), Preliminary orthographic design for Ramari Dongosaro: §§3-5 (pp. 35-44).

Sonsorolese (sons1243) already has the sourced inventory of van den Berg (2014), on which Vita & Pedro build
(p. 35); this batch adds the allophonic and morphophonemic rules of §4 that van den Berg does not give.
Their phoneme symbols are mapped to van den Berg's: ɣɬ = ɡˡ, ʝ = j, bɣ/pɣ/mɣ = bʷ/pʷ/mʷ.
"""
from common import Batch, write

S = "vitapedro2021"
L = "sons1243"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Vita, Vasiliki; Pedro, Chelsea", year="2021",
    title="Preliminary orthographic design for Ramari Dongosaro", kind="grammar", pub_type="article",
    container_title="SOAS Working Papers in Linguistics", volume="20", pages="26-48",
    notes="Consulted directly on 25 November 2026 (PDF in Downloads). A community standardisation project for "
          "Sonsorolese (Ramari Dongosaro); the phonological analysis (§§3-4, pp. 35-42) re-examines van den Berg "
          "(2014) and Capell (1969) with recordings of Frank Pedro, and §5 proposes an alphabet with diacritics "
          "(Table 6, p. 43)."))
b.t["sources"].append(dict(
    id="capell1969", author="Capell, Arthur", year="1969", title="Grammar and vocabulary of the language of Sonsorol-Tobi",
    kind="grammar", pub_type="book", place="Sydney", publisher="University of Sydney",
    notes="Bibliographic details from the reference list of Vita & Pedro (2021: 46); not consulted directly."))

A = b.allo
A(L, "ɾ", "nː", "two taps across a morpheme boundary (stem-final ɾV + suffix in ɾ-)", "40",
  "Tap nasalization: 'two adjacent taps are pronounced as a long nasal, /ɾɾ/ → [n:]' (mɣɐɾɨ̆-ɾi ðoŋosaɾŏ → [mɣɐn:i "
  "ðoŋosaɾŏ] 'a man from Sonsorol'); the ɾ of the suffix is not kept. They suggest the nasal may be 'the realization "
  "of a geminate rhotic tap' (p. 40). Van den Berg (2014: 20) gives [n].")
A(L, "ɡˡ", "ɡ̊ˡ", "variably", "37",
  "Written ɣɬ, 'voiced lateral-fricativised velar': 'because of the fricativisation, at certain points, it comes out "
  "as devoiced' (p. 37). The devoiced value is written here with a ring below.")
A(L, "ɐ", "ɛ", "single, between high unrounded vowels", "41-42",
  "Low vowel raising and fronting: 'a single low vowel, /ɐ/, is fronted and raised to /ɛ/ between two high "
  "unrounded vowels' (imɣɐ̆-ɾi → [imɣɛɾi] 'house of', but i:mɣɐ̆-ɾ → [imɣɐɾ] 'his house') (pp. 41-42).")
A(L, "ɐ", "ɛ", "in the 1sg object suffix -ai after a stem-final ɐ", "38-39",
  "'The first vowel of the first person singular object marker suffix /-ai/ ... becomes [ɛ] after a stem-final /ɐ/', "
  "with glide epenthesis: xɐ-fɐðɐ̆-ai → [xɐfɐðɐjɛi] 'to give birth to me' (pp. 38-39).")
A(L, "i", "u", "before a rounded vowel", "42",
  "Vowel rounding: 'an unrounded vowel /i/, /ɪ/, /ɛ/, /ɐ/ becomes rounded when followed by a rounded vowel' "
  "(bɣi-wow → [bɣuwou] 'to go out') (p. 42).")
A(L, "ɨ", "u", "before a rounded vowel (a final ʉ resurfacing before a suffix)", "42",
  "Vowel rounding: ʝɐɾɨðʉ̆ 'ghost' + -ɾi → [ʝɐɾuðʉɾi] 'ghost of', where the suffix brings back the devoiced final ʉ "
  "(p. 42).")

b.dec("vitapedro2021-phonemes",
      "How do the analyses of Vita & Pedro (2021) that differ from van den Berg (2014) enter Sonsorolese?",
      "Van den Berg's inventory stays. Their ʝ (voiced palatal fricative) for her j, their view that ə is phonemic "
      "(xəɣə- 'tie up' in careful speech, p. 36), the seven diphthongs (Table 3) and the short final vowels ɨ̆ ʉ̆ ŏ ɐ̆ "
      "(Table 2) go into notes (sheet edits); their alphabet (Table 6) into the orthography note.",
      "Replace van den Berg's j with ʝ and drop the marginal mark on ə.", "35-43")

md = """# vitapedro2021-sonsorolese

Vita, Vasiliki & Chelsea Pedro. 2021. Preliminary orthographic design for Ramari Dongosaro. *SOAS Working Papers in Linguistics* 20. 26-48. Generator: `tools/batch_scripts/five_sources_2026_11_25/vitapedro2021.py`.

## Scope

- **Allophones** of Sonsorolese (`sons1243`, inventory of van den Berg 2014): tap nasalization [nː], devoiced ɡˡ, low vowel raising and the [ɛ] of the suffix -ai, vowel rounding of i and ɨ before rounded vowels.
- Decision `vitapedro2021-phonemes` (open).

## Sheet edits after landing

- Notes on `sons1243` j (ʝ), ə (phonemic) and the lect (diphthongs, short final vowels, proposed alphabet) (`sheet_edits.py`).

## Not entered

- Glide epenthesis, diphthongization before suffixes and high vowel backing before w (§§4.2, 4.3, 4.5): they insert or change sequences, not phonemes.
- The rules they repeat from van den Berg (2014: 27, 32) (ɛ > ə before ʉ, final ɐ > ɛ, o and ʉ > u before suffixes): to be entered from van den Berg directly.
- The project description and survey (§§1-2, 6).
"""
write("vitapedro2021-sonsorolese", b.t, md)
