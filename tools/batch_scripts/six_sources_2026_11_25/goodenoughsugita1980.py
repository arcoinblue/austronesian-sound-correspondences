#!/usr/bin/env python3
"""Goodenough & Sugita (1980), Trukese-English dictionary, Introduction §§1-2 (pp. xi-xvii).

The first sourced inventory of Chuukese (chuu1238), lagoon dialects: the alphabet of §2.2 describes each
phoneme and its main variants.
"""
from common import Batch, write

S = "goodenoughsugita1980"
L = "chuu1238"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Goodenough, Ward H.; Sugita, Hiroshi", year="1980", title="Trukese-English dictionary",
    kind="dictionary",
    notes="Consulted directly on 25 November 2026 in an excerpt (Downloads: front matter, Introduction pp. xi-xvii, "
          "read from page images). The dictionary is of the lagoon dialects of Truk (pp. xi-xii). Memoirs of the "
          "American Philosophical Society 141.",
    pub_type="book", place="Philadelphia", publisher="American Philosophical Society",
    series="Memoirs of the American Philosophical Society 141"))

P = "xiv-xvii"
DBL = " Long (double) consonants are written twice (p. xiv)."
C = [
    ("p", "p", "bilabial", "plosive", "voiceless", "'A voiceless, bilabial stop, unaspirated' (p. xvi)." + DBL),
    ("pʷ", "pw", "bilabial", "plosive", "voiceless", "Bilabial stop 'with accompanying velar constriction but with lip rounding only when preceded or followed by a back, rounded vowel' (p. xvi)." + DBL),
    ("t", "t", "dental", "plosive", "voiceless", "'A voiceless, dental or alveolar stop, unaspirated' (p. xvi)." + DBL),
    ("k", "k", "velar", "plosive", "voiceless", "'A velar, voiceless stop, unaspirated' (p. xv)." + DBL),
    ("ʈ͡ʂ", "ch", "retroflex", "affricate", "voiceless", "Spelled ch: 'a voiceless, usually retroflex, affricate' (p. xvi). In the Hall Islands dialects it is a retroflex continuant (p. xi)." + DBL),
    ("f", "f", "labiodental", "fricative", "voiceless", "'A voiceless, labiodental spirant' (p. xv)." + DBL),
    ("s", "s", "dental", "fricative", "voiceless", "'A voiceless, dental spirant' (p. xv)." + DBL),
    ("m", "m", "bilabial", "nasal", "voiced", "Bilabial nasal 'without accompanying velar constriction or lip rounding', tending (unless double) to be denasalised between vowels, 'where it approaches a bilabial flap' (p. xv)." + DBL),
    ("mʷ", "mw", "bilabial", "nasal", "voiced", "Bilabial nasal 'with accompanying velar constriction but with lip rounding only when preceded or followed by a back, rounded vowel', tending (unless double) to be denasalised between vowels (pp. xv-xvi)." + DBL),
    ("n", "n", "dental", "nasal", "voiced", "'A voiced, dental or alveolar, nasal continuant' (p. xvi). Lagoon n continues both n and l, which stay distinct in the Hall Islands, Mortlockese and Puluwatese (pp. xi, xv)." + DBL),
    ("ŋ", "ng", "velar", "nasal", "voiced", "Velar nasal, tending (unless double) 'to be partially denasalized between vowels, where it approaches a velar flap' (p. xvi)." + DBL),
    ("r", "r", "alveolar", "trill", "voiced", "'An alveolar trill' (p. xvi)." + DBL),
    ("w", "w", "bilabial", "approximant", "voiced", "'A bilabial glide, unrounded except when preceded or followed by a back rounded vowel' (p. xvii)."),
    ("j", "y", "alveolo-palatal", "approximant", "voiced", "'An alveo-palatal glide, unrounded', not written word-initially, 'where it is phonetically absent in some dialects' (p. xvii)."),
]
for ipa, sym, pl, mn, vo, note in C:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page=P, notes=note)
LC = "Long consonant: 'both vowels and consonants may be long as well as short. When long, they are written twice' (p. xiv)."
for ipa, sym, pl, mn, vo, ex in [
    ("pː", "pp", "bilabial", "plosive", "voiceless", "pan : ppan (p. xvi)"), ("pʷː", "pwpw", "bilabial", "plosive", "voiceless", "pwó : pwpwó (p. xvi)"),
    ("tː", "tt", "dental", "plosive", "voiceless", "taf : ttaf (p. xvi)"), ("kː", "kk", "velar", "plosive", "voiceless", "kóón : kkóón (p. xv)"),
    ("ʈ͡ʂː", "chch", "retroflex", "affricate", "voiceless", "chú : chchú (p. xvi)"), ("fː", "ff", "labiodental", "fricative", "voiceless", "faat : ffaat (p. xv)"),
    ("sː", "ss", "dental", "fricative", "voiceless", "son : sson (p. xv)"), ("mː", "mm", "bilabial", "nasal", "voiced", "mas : mmas (p. xv)"),
    ("mʷː", "mwmw", "bilabial", "nasal", "voiced", "mwáán : mwmwáán (p. xvi)"), ("nː", "nn", "dental", "nasal", "voiced", "num : nnum (p. xvi)"),
    ("ŋː", "ngng", "velar", "nasal", "voiced", "ngút : ngngút (p. xvi)"), ("rː", "rr", "alveolar", "trill", "voiced", "rusi : rrus (p. xvi)"),
]:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page=P, notes=f"{LC} {ex}.")
V = [
    ("a", "a", "central", "open", "unrounded", "'A low, central unrounded vowel' (p. xiv)."),
    ("æ", "á", "front", "open", "unrounded", "Spelled á: 'a low, front, unrounded vowel (like the a of English hat)' (p. xiv)."),
    ("e", "e", "front", "mid", "unrounded", "'A mid, front, unrounded vowel' (p. xv)."),
    ("ə", "é", "central", "mid", "unrounded", "Spelled é: 'a mid, central, unrounded vowel (close to the u of English but)' (p. xv)."),
    ("i", "i", "front", "close", "unrounded", "'A high, front, unrounded vowel' (p. xv)."),
    ("o", "o", "back", "mid", "rounded", "'A mid, back, rounded vowel' (p. xv)."),
    ("ɔ", "ó", "back", "open", "rounded", "Spelled ó: 'a low, back rounded vowel (like the aw of English law)' (p. xv)."),
    ("u", "u", "back", "close", "rounded", "'A high, back rounded vowel' (p. xv)."),
    ("ɨ", "ú", "central", "close", "unrounded", "Spelled ú: 'a high, central, unrounded vowel' (p. xv)."),
]
for ipa, sym, pl, mn, rd, note in V:
    b.ph(L, ipa, "V", pl, mn, "", rd, sym=sym, page="xiv-xv", notes=note + " Nine vowels in all (p. xiv).")
    b.ph(L, ipa + "ː", "V", pl, mn, "", rd, sym=sym * 2, page="xiv-xv", notes="Long vowel, written twice (p. xiv).")

A = b.allo
VOI = "Voiced 'unless double' between vowels (pp. xv-xvi)."
for c, v in (("p", "b"), ("pʷ", "bʷ"), ("t", "d"), ("k", "ɡ"), ("ʈ͡ʂ", "ɖ͡ʐ")):
    A(L, c, v, "single, between vowels", "xv-xvi", VOI)
A(L, "k", "kʷ", "before or after a back rounded vowel", "xv", "k is 'pronounced with lip rounding if preceded or followed by a back rounded vowel' (p. xv).")
UNR = "Lip rounding 'only when preceded or followed by a back, rounded vowel' (pp. xv-xvi); elsewhere velarised without rounding."
A(L, "pʷ", "pˠ", "not next to a back rounded vowel", "xvi", UNR)
A(L, "mʷ", "mˠ", "not next to a back rounded vowel", "xv-xvi", UNR)
A(L, "n", "ɾ", "single, between vowels", "xvi", "n tends 'to be denasalized between vowels, where it sounds more like an alveolar flap' (p. xvi).")
A(L, "r", "r̥", "before or after a pause", "xvi", "r is 'voiced between vowels and tending to be voiceless before or after pause' (p. xvi).")
CH = "'For some speakers it is an alveo-palatal affricate (like English ch and j), and for some it is an alveolar affricate' (p. xvi)."
A(L, "ʈ͡ʂ", "t͡ʃ", "some speakers", "xvi", CH)
A(L, "ʈ͡ʂ", "t͡s", "some speakers", "xvi", CH)
A(L, "ʈ͡ʂ", "ɻ", "Hall Islands dialects", "xi", "In the Hall Islands 'the retroflex affricate of lagoon Trukese is pronounced as a retroflex continuant' (p. xi).")
A(L, "w", "w", "before or after a back rounded vowel", "xvii", "w is 'a bilabial glide, unrounded except when preceded or followed by a back rounded vowel in Trukese' (p. xvii).")

b.dec("goodenoughsugita1980-symbols",
      "Goodenough & Sugita (1980: xiv-xvii) describe Chuukese ch as 'usually retroflex', w as an unrounded bilabial "
      "glide (rounded only next to back rounded vowels) and pʷ, mʷ as velarised, rounded only next to back rounded "
      "vowels. Which IPA symbols?",
      "ʈ͡ʂ for ch (as Woleaian and Pohnpeian; the alveo-palatal and alveolar variants are allophones); w and pʷ, mʷ "
      "as in the other Micronesian inventories, with the unrounded variants as allophones.",
      "β̞ (unrounded bilabial glide) for w, pˠ and mˠ for the labiovelars; t͡ʃ for ch.", "xiv-xvii")

md = """# goodenoughsugita1980-chuukese

Goodenough, Ward H. & Hiroshi Sugita. 1980. *Trukese-English dictionary* (Memoirs of the American Philosophical Society 141). Philadelphia: American Philosophical Society. Read from an excerpt in Downloads (front matter and Introduction, pp. xi-xvii, from page images). Generator: `tools/batch_scripts/six_sources_2026_11_25/goodenoughsugita1980.py`.

## Scope

- **Inventory** (§2.2, pp. xiv-xvii): the first sourced inventory of Chuukese (`chuu1238`, lagoon dialects), in IPA: 12 consonants (p pʷ t k ʈ͡ʂ f s m mʷ n ŋ r), 2 glides (w j), 9 vowels (a æ e ə i o ɔ u ɨ); long vowels and long consonants ('both vowels and consonants may be long as well as short', p. xiv).
- **Allophones**: intervocalic voicing of single stops and ch; rounded k; unrounded pʷ mʷ; denasalised n; voiceless r near a pause; the alveo-palatal and alveolar variants of ch and its Hall Islands value [ɻ]; rounded w.
- Decision `goodenoughsugita1980-symbols` (open).

## Sheet edits after landing

- `correspondences`: the Chuukese row of Bender et al. (2003a) with ch (PCK *c) respelled ʈ͡ʂ, ch in `source_form`.
- `lects` (Chuukese): orthography note (IPA after Goodenough & Sugita 1980: xiv-xvii).

## Not entered

- The denasalised m and ŋ between vowels ('approaches a bilabial flap', 'approaches a velar flap', p. xv-xvi): in the phoneme notes, no IPA symbol.
- The Hall Islands l and the Mortlockese vowels (twelve 'if that is indeed their number', p. xi; the extra letters of p. xvii); Puluwatese h and ŕ (p. xvii: ŕ, the retroflex continuant, is r in Elbert's dictionary, the values of r and ŕ being 'exactly opposite').
- Puluwatese dialect forms (maah, maha, mha 'eye', p. xii).
"""
write("goodenoughsugita1980-chuukese", b.t, md)
