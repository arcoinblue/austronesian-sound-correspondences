#!/usr/bin/env python3
"""Blevins & Harrison (1999), Trimoraic feet in Gilbertese.

The first sourced Kiribati inventory (Tables 1-2, §3) and the allophones described in §3.
The paper's subject (stress, the trimoraic minimal word) has no segment rows.
"""
from common import Batch, write

S = "blevinsharrison1999"
L = "gilb1244"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Blevins, Juliette; Harrison, Sheldon P.", year="1999", title="Trimoraic feet in Gilbertese",
    kind="grammar",
    notes="Consulted directly on 24 November 2026 (PDF in Downloads; Tables 1-2 read from the page image). "
          "Data from Harrison's field notes and tapes (n. 2).",
    pub_type="article", container_title="Oceanic Linguistics", volume="38", issue="2", pages="203-230"))

P = "205-206"
VEL = "Velarized labial (Table 1); IPA as printed."
for ipa, pl, mn, vo, sym, note in [
    ("p", "bilabial", "plosive", "voiceless", "b", "Written b; IPA [p] (Table 1). 'Voicing is nondistinctive in Gilbertese' (p. 206)."),
    ("t", "alveolar", "plosive", "voiceless", "t", "Apical (Table 1)."),
    ("k", "velar", "plosive", "voiceless", "k", ""),
    ("pʷ", "bilabial", "plosive", "voiceless", "bw", "Written bw; IPA [pʷ]. " + VEL),
    ("m", "bilabial", "nasal", "voiced", "m", ""),
    ("n", "alveolar", "nasal", "voiced", "n", "Apical (Table 1)."),
    ("ŋ", "velar", "nasal", "voiced", "ng", "Written ng."),
    ("mʷ", "bilabial", "nasal", "voiced", "mw", "Written mw. " + VEL + " Before a consonant the contrast of m and mʷ appears to be neutralised (n. 7)."),
    ("ɾ", "alveolar", "tap", "voiced", "r", "'r represents an alveolar tap or flap' (p. 206); excluded from the syllable rime (constraint 4vi)."),
    ("βʷ", "bilabial", "fricative", "voiced", "w", "Written w; IPA [βʷ]: 'a voiced labiovelar fricative that has both flap and approximant allophones' (p. 206)."),
]:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page=P, notes=note)
LN = ("'Quantity is distinctive for vowels and nasal consonants, but not for obstruents, or for /r, w/'; written "
      "double (p. 206, minimal pairs in (2): ana/anna, tuanga/tuangnga).")
for ipa, pl, sym in (("mː", "bilabial", "mm"), ("nː", "alveolar", "nn"), ("ŋː", "velar", "ngng")):
    b.ph(L, ipa, "C", pl, "nasal", "voiced", sym=sym, page="206", notes=LN + (" No pair with long mʷ is given." if ipa == "mː" else ""))
V = [("i", "front", "close", "unrounded"), ("e", "front", "mid", "unrounded"), ("a", "central", "open", "unrounded"),
     ("u", "back", "close", "rounded"), ("o", "back", "mid", "rounded")]
for v, pl, mn, rd in V:
    b.ph(L, v, "V", pl, mn, "", rd, page="205", notes="Table 2 places a in the central column." if v == "a" else "")
for v, pl, mn, rd in V:
    b.ph(L, v + "ː", "V", pl, mn, "", rd, sym=v + v, page="206", notes=LN)

b.allo(L, "t", "s", "_i", "206", "'The stop t is realized as [s] when followed by i in all dialects' (p. 206; ti [si], tii [sii]).")
b.allo(L, "βʷ", "w", "", "206", "Approximant allophone of w [βʷ]; the conditions are not given. The source also names a flap allophone, which has no IPA symbol (p. 206).")
ASSIM = ("Within a syllable rime V1V2, the two vowels assimilate to each other when they are low and mid, or mid "
         "and high (adjacent on the sonority scale); not across a syllable boundary: kaon 'tentacle of' [kɒɒn] or "
         "[kɒɔn], but ka.oo.na [kaoona] (p. 207).")
b.allo(L, "a", "ɒ", "before tautosyllabic o", "207", ASSIM)
b.allo(L, "o", "ɒ", "after tautosyllabic a", "207", ASSIM)
b.allo(L, "o", "ɔ", "after tautosyllabic a", "207", ASSIM)
DEV = ("'On the surface, short high vowels i,u may devocalize when followed by more sonorous vowels' (n. 8); "
       "ie 'sail' is still heterosyllabic [i.e].")
b.allo(L, "i", "j", "before a more sonorous vowel (optional)", "207", DEV)
b.allo(L, "u", "w", "before a more sonorous vowel (optional)", "207", DEV)
NAS = ("A morpheme-final moraic nasal keeps its mora: before a non-high vowel it is realised as a geminate "
       "(ambisyllabic), before a high vowel the vowel lengthens, and before a non-homorganic consonant an "
       "epenthetic vowel appears (p. 210, (8)).")
for n in ("m", "n", "ŋ"):
    b.allo(L, n, n + "ː", "morpheme-final, before a non-high vowel", "210", NAS)

md = """# blevinsharrison1999-kiribati

Blevins, Juliette & Sheldon P. Harrison. 1999. Trimoraic feet in Gilbertese. *Oceanic Linguistics* 38(2). 203-230. Read from the PDF in Downloads; Tables 1-2 and p. 207 from page images. Generator: `tools/batch_scripts/five_sources_2026_11_24/blevinsharrison1999.py`.

## Scope

- **Inventory** (Tables 1-2, p. 206): the first sourced inventory of Kiribati (`gilb1244`), in IPA as the paper gives it (b [p], bw [pʷ], ng [ŋ], mw [mʷ], r an alveolar tap [ɾ], w [βʷ]), with long vowels and long nasals ('quantity is distinctive for vowels and nasal consonants').
- **Allophones** (§3): t [s] before i; the flap and approximant realisations of w; tautosyllabic vowel assimilation; devocalised short high vowels; geminate final nasals before a non-high vowel.

## Sheet edits (done on 24 Nov 2026 at 23:45 KST)

The Kiribati rows of Bender et al. (2003a) used the comparative transcription (b, bʷ, r, w). They are respelled in the `correspondences` tab (rows 626, 627, 636, 640-642): b > p, bʷ > pʷ, w > βʷ, r > ɾ, the letters in `source_form`; the Kiribati `orthography_note` (lects J22) is rewritten.

## Not entered

- The prosody (trimoraic feet, minimal word, Rehg's 1993 PMc accent): no segment rows.
"""
write("blevinsharrison1999-kiribati", b.t, md)
