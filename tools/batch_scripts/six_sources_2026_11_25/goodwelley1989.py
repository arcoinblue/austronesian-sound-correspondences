#!/usr/bin/env python3
"""Good & Welley (1989), A preliminary grammar sketch, text, and vocabulary of Pingilapese, §1 (pp. 1-6).

The first sourced inventory of Pingelapese (ping1243): §1.1 phonemes with their variants, §1.3 spelling.
"""
from common import Batch, write

S = "goodwelley1989"
L = "ping1243"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Good, Elaine M.; Welley, Weldis", year="1989",
    title="A preliminary grammar sketch, text, and vocabulary of Pingilapese",
    url_or_doi="https://doi.org/10.15144/PL-C112.1", kind="grammar",
    notes="Consulted directly on 25 November 2026 (sealang.net scan in Downloads; §1.1 read from the page images). "
          "§1 (pp. 1-6) is the sound system; data from Weldis Welley of Pingilap. The other papers in the volume "
          "(NP-NP constructions in Ponapeic, Kosraean clause-final determiners) have no phonology.",
    pub_type="chapter", container_title="Papers in Kosraean and Ponapeic", editors="Elaine M. Good; Weldis Welley",
    pages="1-114", place="Canberra", publisher="The Australian National University", series="Pacific Linguistics C-112"))

C = [
    ("p", "p", "bilabial", "plosive", "voiceless", "Voiceless bilabial stop (p. 2)."),
    ("pʷ", "pw", "bilabial", "plosive", "voiceless", "'Velarised rounded voiceless bilabial stop' (p. 2)."),
    ("t", "d", "dental", "plosive", "voiceless", "'Voiceless dental stop', spelled d (pp. 2, 5)."),
    ("k", "k", "velar", "plosive", "voiceless", "Voiceless velar stop (p. 2)."),
    ("s", "s", "alveolar", "fricative", "voiceless", "Voiceless alveolar fricative (p. 2)."),
    ("m", "m", "bilabial", "nasal", "voiced", "Voiced bilabial nasal (p. 2)."),
    ("mʷ", "mw", "bilabial", "nasal", "voiced", "'Rounded velarised voiced bilabial nasal' (p. 2)."),
    ("n", "n", "alveolar", "nasal", "voiced", "'Voiced alveolar (perhaps dental or with a dental variant) nasal' (p. 2)."),
    ("ŋ", "ng", "velar", "nasal", "voiced", "Voiced velar nasal, spelled ng (pp. 3, 5)."),
    ("l", "l", "alveolar", "lateral-approximant", "voiced", "'Voiced alveolar (doubly articulated with a velar point of articulation) lateral' (p. 3), that is, velarised."),
    ("r", "r", "alveolar", "trill", "voiced", "Voiced alveolar trill (p. 3)."),
]
for ipa, sym, pl, mn, vo, note in C:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page="2-3, 5", notes=note)
V = [
    ("i", "i", "front", "close", "unrounded", "High front close unrounded vowel (p. 3)."),
    ("e", "e", "front", "close-mid", "unrounded", "Mid front close unrounded vowel (p. 3). 'Variations of /e/ and /ɛ/ in the same word can be noted' (n. 3, p. 111)."),
    ("ɛ", "ae", "front", "open-mid", "unrounded", "Mid front open unrounded vowel, spelled ae (pp. 3, 6). Written separately from e 'until further phonological research is done', although in Northern Ponapean it is predictable (n. 4 of the NP-NP paper in the same volume, p. 125)."),
    ("a", "a", "central", "open", "unrounded", "Low central open unrounded vowel (p. 4)."),
    ("ɔ", "oa", "back", "open-mid", "rounded", "'Low back close rounded vowel', spelled oa (pp. 4, 6). 'Variations of /o/ and /ɔ/ in the same word can be noted' (n. 4, p. 111)."),
    ("o", "o", "back", "close-mid", "rounded", "Mid back close rounded vowel (p. 4)."),
    ("u", "u", "back", "close", "rounded", "High back close rounded vowel (p. 4)."),
]
for ipa, sym, pl, mn, rd, note in V:
    b.ph(L, ipa, "V", pl, mn, "", rd, sym=sym, page="3-4, 6", notes=note)
    b.ph(L, ipa + "ː", "V", pl, mn, "", rd, sym=sym + "h", page="3-6",
         notes="Long vowel, spelled with a following h as in Ponapean and Mokilese (p. 6); contrasts with the short vowel (p. 5).")

A = b.allo
UNREL = "'An unreleased variant may occur word finally' (p. 2)."
for c in ("p", "t", "k"):
    A(L, c, c + "̚", "word-finally (optional)", "2", UNREL)
A(L, "pʷ", "pˠ", "word-finally", "2", "'An unrounded variant (which may also be unreleased) occurs word finally' (p. 2).")
A(L, "mʷ", "mˠ", "word-finally", "2", "'An unrounded allophone occurs word finally' (p. 2).")
A(L, "r", "r̥", "utterance-final", "3", "'A voiceless variant and a variant that begins voiced and ends voiceless occurs utterance final' (p. 3).")
A(L, "i", "ɪ", "before n, r, l", "3", "'A high front open allophone occurs before an alveolar nasal, trill or lateral' (p. 3).")
A(L, "e", "ɛ", "in some words (variation)", "111", "'Variations of /e/ and /ɛ/ in the same word can be noted' (n. 3).")
A(L, "o", "ɔ", "in some words (variation)", "111", "'Variations of /o/ and /ɔ/ in the same word can be noted' (n. 4).")

md = """# goodwelley1989-pingelapese

Good, Elaine M. & Weldis Welley. 1989. A preliminary grammar sketch, text, and vocabulary of Pingilapese. In Elaine M. Good & Weldis Welley (eds.), *Papers in Kosraean and Ponapeic* (Pacific Linguistics C-112), 1-114. Canberra: The Australian National University. Read from the sealang.net scan in Downloads; §1.1 (pp. 2-4) from page images. Generator: `tools/batch_scripts/six_sources_2026_11_25/goodwelley1989.py`.

## Scope

- **Inventory** (§1.1-1.3, pp. 2-6): the first sourced inventory of Pingelapese, in IPA: 11 consonants (p pʷ t k s m mʷ n ŋ l r; the dental stop is spelled d), 7 vowels (i e ɛ a ɔ o u) and their long counterparts. No glides are listed as phonemes.
- **Allophones**: unreleased final stops, unrounded final pʷ and mʷ, voiceless final r, [ɪ] before n r l, e ~ ɛ and o ~ ɔ variation (nn. 3-4).

## Sheet edits after landing

- `correspondences`: the Pingelapese row of Bender et al. (2003a) with d (PPON *d > d) respelled t (Good & Welley: spelled d, a voiceless dental stop), d in `source_form`.
- `lects` (Pingelapese): orthography note (IPA after Good & Welley 1989: 2-6).

## Not entered

- The insignificant initial glottal stop (p. 4); stress, intonation, word-final releases and transitional vowels, which the authors leave for further research (p. 6).
- The other two papers of the volume (syntax).
"""
write("goodwelley1989-pingelapese", b.t, md)
