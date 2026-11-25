#!/usr/bin/env python3
"""Jackson & Marck (1991), Carolinian-English dictionary: Introduction (pp. xv-xxiv), 'The sounds of Carolinian'
(p. 27) and the entries for the letters of the alphabet.

The phonetic values of p. 27 were read from the page image; the Open Access PDF prints several IPA letters in a
substitute font ([Ω] for ɡ, [Γ] for ŋ), so only the unambiguous values are used.
"""
from common import Batch, write

S = "jacksonmarck1991"
L = "caro1242"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Jackson, Frederick H.; Marck, Jeffrey C.", year="1991", title="Carolinian-English dictionary",
    kind="dictionary", pub_type="book", place="Honolulu",
    publisher="University of Hawaii Press", series="PALI Language Texts: Micronesia",
    notes="In collaboration with Jesus Mareham Elameto, Rosario M. Elameto, Antonio Flores Kaipat, Francisco Mettao "
          "Olopai, Margarita O. Sarapau, Teresa I. Taitano and Rosa Roppul Warakai (title page). Consulted directly "
          "on 25 November 2026 (Open Access edition of 2019, CC BY-NC-SA 4.0, in Downloads): the Introduction (pp. "
          "xv-xxiv), 'The sounds of Carolinian' (p. 27, read from the page image) and the entries for the letters. "
          "Three dialects: Tanapag (TAN, descendants of Namonuito settlers) and two southern ones, the majority EL "
          "(Elle, l only) and LN (with both l and n), descended from Satawalese-Lamotrekese and from "
          "Puluwatese-Pulusukese settlers; the southern EL dialect is the fullest represented (pp. xv-xxi). Data "
          "source of the Carolinian columns of Bender et al. (2003a). The Open Access edition is listed at "
          "www.hawaiiopen.org (p. ii)."))

# Letters 'not found in native words', 'used in writing the Tanapag (Enne) dialect and in borrowed words'.
LOAN = [
    ("b", "b", "bilabial", "plosive", "voiced", "27, 123",
     "Letter b [b] 'not found in native words' (p. 123): loans (Bennis 'Friday' from Chamorro, bileet 'blade' from "
     "English). Distinct from bw (p. 27)."),
    ("d", "d", "alveolar", "plosive", "voiced", "27, 148",
     "Letter d [d] 'not found in native words except in Tanapag' (p. 148): in the southern dialects, loans from "
     "Chamorro, Japanese, English and Spanish (dakkun, daikon, dais, danamita)."),
    ("ɡ", "g", "velar", "plosive", "voiced", "27, 187",
     "Letter g, 'used in writing the Tanapag (Enne) dialect and in borrowed words' (p. 187): in the southern dialects, "
     "loans (gakko 'school', ganna 'win'); Tanapag g corresponds to southern gh (gareeta, see ghareeta). The value on "
     "p. 27 is printed in a substitute font ([Ω], compared with English go)."),
    ("d͡z", "z", "alveolar", "affricate", "voiced", "27, 489",
     "Letter z [dz] 'not found in native words' (p. 489): loans from English and Japanese (zaam 'jam', zoori "
     "'slippers')."),
    ("n", "n", "alveolar", "nasal", "voiced", "xx-xxi, 27, 324",
     "Letter n [n]: the LN dialect 'has both l and n consonant sounds, the EL dialect has only l' (p. xxi), and the "
     "Tanapag dialect has n; otherwise in loans. Ellis (2012: 160-161) counts 26 headwords in n, most of them loans or "
     "LN and Tanapag words."),
    ("k", "k", "velar", "plosive", "voiceless", "27, 229",
     "Single k is 'not found singly in native words' (p. 229); native words have kk. Unaspirated (p. 27)."),
]
for ipa, sym, pl, mn, vo, pg, note in LOAN:
    b.ph(L, ipa, "C", pl, mn, vo, sym=sym, page=pg, notes=note, status="marginal")

b.allo(L, "x", "ɣ", "conditions not given", "27",
       "Letter gh has the values '[x], [γ]' (German nach) (p. 27); the conditions are not given.")
b.allo(L, "l", "n", "LN (Elle-Enne) dialect, in many words", "xx-xxi",
       "The LN dialect, spoken by those of Tanapag heritage who have spread to the south, 'has both l and n "
       "consonant sounds', where the majority EL dialect has only l (pp. xx-xxi).")

b.dec("jacksonmarck1991-dialects",
      "How are the dialects of Jackson & Marck (1991) entered: the southern EL (Elle) and LN (Elle-Enne) dialects and "
      "Tanapag (Enne)?",
      "Carolinian (caro1242) is the southern speech of Ellis's (2012) inventory, the EL dialect; LN's n is a marginal "
      "phoneme and an allophone row of l, not a lect of its own, since the sources give no inventory or rows for it. "
      "Tanapag stays the dialect tana1281 with the rows of Bender et al. (2003a); its spelling differences (n for l, rh "
      "for sch, h for s, g for gh; Ellis 2012: 9) go into its notes (sheet edit).",
      "Make EL and LN dialect lects under Carolinian; or treat Tanapag as a separate language (Talaabog), as Ellis "
      "(2012: 10-11) prefers.",
      "xv, xx-xxi")

md = """# jacksonmarck1991-carolinian

Jackson, Frederick H. & Jeffrey C. Marck. 1991. *Carolinian-English dictionary*. Honolulu: University of Hawaii Press. Generator: `tools/batch_scripts/five_sources_2026_11_25/jacksonmarck1991.py`.

## Scope

- **Marginal phonemes** of Carolinian (`caro1242`) from the entries for the letters: b, d, ɡ (g), d͡z (z) in loans; n (LN dialect, Tanapag, loans); single k (loans). They join the inventory of Ellis (2012).
- **Allophones**: [ɣ] of x (gh, p. 27); [n] for l in the LN dialect.
- Decision `jacksonmarck1991-dialects` (open).
- The spelling of Ellis's phonemes is given in their notes (`ellis2012-saipan-carolinian`).

## Sheet edits after landing

- `caro1242`: orthography note with the alphabet of p. xvii and the values of p. 27; `tana1281`: the Tanapag letters d, g, h, rh and n (`sheet_edits.py`).

## Not entered

- The vowel values of p. 27 (a [a], e [ʌ], é, ó, ú): several are printed in a substitute font, and Ellis (2012) gives IPA for the same vowels.
- Tanapag correspondences from the TAN entries: the dictionary gives no table, and the rows of Bender et al. (2003a) already cover the consonants.
"""
write("jacksonmarck1991-carolinian", b.t, md)
