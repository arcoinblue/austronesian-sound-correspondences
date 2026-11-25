#!/usr/bin/env python3
"""Rehg (1993), Proto-Micronesian prosody (pp. 25-46).

A paper on stress and pitch. What fits the tables: Rehg's PMc inventory (Figure 2, p. 26) as a spelling system of
PMc, and the PMc rule of final short high vowel devoicing (from Rehg 1991, restated on p. 38) as allophones. The
stress, pitch and lengthening rules go into the PMc notes (sheet edit); the long vowels into a decision.
"""
from common import Batch, write

S = "rehg1993"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Rehg, Kenneth L.", year="1993", title="Proto-Micronesian prosody", kind="comparative",
    url_or_doi="https://www.jstor.org/stable/20006746", pub_type="chapter",
    container_title="Tonality in Austronesian languages", editors="Jerold A. Edmondson; Kenneth J. Gregerson",
    pages="25-46", place="Honolulu", publisher="University of Hawai'i Press",
    series="Oceanic Linguistics Special Publication 24",
    notes="Consulted directly on 25 November 2026 (JSTOR PDF in Downloads; Figure 2 and Tables 1-3 read from the page "
          "images). Reconstructs PMc stress on the penultimate mora of a phrase and high pitch on the antepenultimate "
          "(§3.3), supported by final vowel lenition (Rehg 1991) and by phrase-initial lengthening, argued for in Rehg's earlier paper on "
          "'compensatory lengthening' rules (§4)."))
b.t["sources"].append(dict(
    id="rehg1991", author="Rehg, Kenneth L.", year="1991",
    title="Final vowel lenition in Micronesian languages: An exploration of the dynamics of drift", kind="comparative",
    pub_type="chapter", container_title="Currents in Pacific linguistics: Papers on Austronesian languages and "
    "ethnolinguistics in honour of George W. Grace", editors="Robert Blust", pages="383-401", place="Canberra",
    publisher="The Australian National University", series="Pacific Linguistics C-117",
    notes="Bibliographic details from the reference list of Rehg (1993); not consulted directly. Its PMc rules of "
          "final vowel lenition are restated in Rehg (1993: 38)."))

# Figure 2 (p. 26) and n. 9 (p. 42): Rehg's symbols against the canonical (Bender et al. 2003a) ones.
FN = ("Figure 2, 'adapted from Jackson 1983:353' (n. 9): 17 consonants and 'the same five (short and long) vowels' "
      "as Proto-Polynesian (p. 26).")
NM = [
    ("s", "s'", "Rehg's /s'/ corresponds to Jackson's d (n. 9, p. 42), the *s of Bender et al. (2003a)."),
    ("S", "s", "Rehg's /s/ corresponds to Jackson's z (n. 9, p. 42), the *S of Bender et al. (2003a)."),
    ("c", "t'", "Not in the correspondences of n. 9; read as the *c of Bender et al. (2003a), the only consonant of "
                "theirs besides *T, *Z and *y that Figure 2 lacks (decision rehg1993-pmc)."),
    ("pʷ", "pʷ", "Written pw in the text of n. 9."), ("mʷ", "mʷ", "Written mw in the text of n. 9."),
    ("ŋ", "ŋ", "Written ng in the text of n. 9."),
    ("T", "∅", "Not in Figure 2: 'Jackson also tentatively reconstructs PMC *T, but evidence for this phoneme is "
               "marginal' (n. 9, p. 42)."),
    ("Z", "∅", "Not in Figure 2."), ("y", "∅", "Not in Figure 2."),
]
for ph, sym, note in NM:
    b.t["notation_map"].append(dict(lect_id="pmc", phoneme=ph, system="Rehg", symbol=sym, source_id=S,
                                    page="26, 42", notes=note + " " + FN))

for v in ("i", "u"):
    b.allo("pmc", v, v + "̥", "phrase-final in polysyllabic words, after a nasal", "38",
           "Final Short Vowel Devoicing: 'Phrase-final short high vowels of polysyllabic words devoice after a nasal "
           "and before pause', motivated in part by their lack of stress. A companion rule, Final Long Vowel "
           "Shortening, optionally shortens phrase-final long high vowels after a nasal (p. 38); PMc has no long "
           "vowels here (decision rehg1993-pmc).",
           source="rehg1991", via_source_id=S, via_page="38",
           via_note="Rehg (1993) restates the rule as reconstructed in Rehg (1991) and adds that Pulo-Annan data "
                    "suggest devoicing rather than deletion of the second mora of long vowels (n. 30).")

b.dec("rehg1993-pmc",
      "What enters from Rehg's (1993) Proto-Micronesian: long vowels, t', and the prosodic rules?",
      "Rehg's symbols as the spelling system 'Rehg' of PMc (s' = *s, s = *S, t' = *c; no *T, *Z, *y); the final short "
      "high vowel devoicing as allophones of *i, *u; stress, pitch and phrase-initial lengthening in the PMc notes. "
      "The long vowels ('the same five (short and long) vowels', p. 26) are not added as phonemes: every lect below "
      "PMc that inherits by assumption would then carry five implied long vowels.",
      "Add *iː *eː *aː *oː *uː to PMc (with the optional final long vowel shortening as allophones); read t' as "
      "another consonant.", "26, 37-40")

md = """# rehg1993-pmc-prosody

Rehg, Kenneth L. 1993. Proto-Micronesian prosody. In Jerold A. Edmondson & Kenneth J. Gregerson (eds.), *Tonality in Austronesian languages* (Oceanic Linguistics Special Publication 24), 25-46. Honolulu: University of Hawai'i Press. Generator: `tools/batch_scripts/five_sources_2026_11_25/rehg1993.py`.

## Scope

- **Notation**: Rehg's PMc symbols (Figure 2, p. 26, and n. 9) as the spelling system `Rehg` of PMc.
- **Allophones** of PMc *i, *u: final short high vowel devoicing, cited to Rehg (1991) via Rehg (1993: 38). New sources row `rehg1991` (from the reference list).
- Decision `rehg1993-pmc` (open): the long vowels and t'.

## Sheet edits after landing

- `pmc` notes: primary stress on the penultimate mora of a phrase, high pitch on the antepenultimate, trimoraic phrases and phrase-initial lengthening (§§3.3, 4.2) (`sheet_edits.py`).

## Not entered

- The synchronic stress and pitch of the daughter languages (§2, Table 1) and their final vowel lenition (Table 2): the devoicing rules of Woleaian and Pulo-Annan are in the data from their grammars; the others are word-final deletions already covered by the correspondences.
- PMc long vowels (decision `rehg1993-pmc`).
"""
write("rehg1993-pmc-prosody", b.t, md)
