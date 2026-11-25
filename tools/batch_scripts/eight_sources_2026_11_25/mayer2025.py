#!/usr/bin/env python3
"""Mayer (2025), A grammar of Woleaian, chapter 2 (Phonetics and phonology), §§2.1-2.2 (pp. 55-74).

Woleaian (wole1240) has the sourced inventory of Tawerilmang & Sohn (1984). Mayer's analysis differs in several
symbols and values (decision mayer2025-woleaian); this batch adds his allophones to the phonemes the two share.
"""
from common import Batch, write

S = "mayer2025"
L = "wole1240"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Mayer, Clemens J.", year="2025", title="A grammar of Woleaian", kind="grammar",
    notes="PhD dissertation, University of Hawai'i at Mānoa, August 2025 (committee Gary Holton, chair). Details from the "
          "title page. Consulted directly on 25 November 2026. Describes mainly the Eauripik variety, from a corpus of "
          "naturalistic speech.",
    pub_type="thesis", publisher="University of Hawai'i at Mānoa", place="Honolulu"))

A = b.allo
M = " Mayer's symbol in brackets; the phoneme is that of Tawerilmang & Sohn (1984) (decision mayer2025-woleaian)."
A(L, "x", "ɣ", "not word-initially (variably)", "57-58", "'/x/: #_ → [x]; else → [x~ɣ]' (example 2.1, p. 58)." + M)
B = ("Mayer's /b/ (Tawerilmang & Sohn's b, here ɸ): 'variably realized as [b~f~ɸ], [bʷ], [p~ɸ], and [pʷ~ɸʷ], depending on "
     "word position', with speaker variation (pp. 58-59).")
A(L, "ɸ", "b", "before u", "58-59", B + " It 'surfaces as [b] before high back vowel /u/' (/ʃobute/ [ʃɔ.ˈbu.te̥] 'woman')." + M)
A(L, "ɸ", "f", "word-initially, in free variation with [b] and [ɸ]", "58-59", B + " Word-initially [b~f~ɸ], 'although [b] is much more common'." + M)
A(L, "ɸ", "bʷ", "before vowels other than u", "58-59",
  B + " '[bʷ] or [pʷ] before all other vowels'; [bʷ] mostly in frequent grammatical forms such as bwe INC, bele INCEP." + M)
A(L, "ɸ", "pʷ", "before vowels other than u", "58-59", B + " '[bʷ] or [pʷ] before all other vowels' (/buetei/ [pʷ~ɸʷe.ˈtei] 'fat')." + M)
A(L, "ɸ", "p", "before a devoiced vowel (final syllable)", "58-59",
  B + " '/b/ surfaces as [p~ɸ] before a devoiced vowel' (/tabu/ [ˈtaː.pu̥] 'taboo')." + M)
R = ("'Both taps ... are devoiced' before a devoiced vowel or utterance-finally ('_(V)# → [ɾ̥]/[ɾ̺̥]'), with 'large "
     "variation both between and within speakers, from spirantization to trilling' there (pp. 60-61).")
A(L, "r", "ɾ̺̥", "before a devoiced vowel or utterance-finally", "60-61",
  R + " Mayer's apical post-alveolar tap /ɾ̺/, Tawerilmang & Sohn's retroflex r." + M)
A(L, "l", "ɾ", "younger and middle-aged speakers", "60-62",
  "Mayer's alveolar tap /ɾ/ (Tawerilmang & Sohn's l) 'seems to have arisen relatively recently': 'the oldest speakers still "
  "frequently use [l], which moves towards free variation between [l] and [ɾ] in middle-aged speakers, and finally (almost) "
  "exclusively [ɾ] in speakers younger than middle-aged' (p. 62)." + M)
A(L, "l", "ɾ̥", "before a devoiced vowel or utterance-finally", "60-61", R + M)
A(L, "l", "n", "before another l (lVl, the vowel deleted)", "61",
  "'/ɾ/, when underlyingly followed by another /ɾ/, surfaces as [n]', the vowel between them being deleted (/ʃaɾʉ-ɾe/ "
  "[ˈʃæ.ne̥] 'his/her/its water') (p. 61); compare Sohn (1975: 103) on doubled l." + M)
RED = "'Vowels and their surface forms', Table 2.12 (p. 68): reduced variants occur 'in unstressed positions or when part of a vowel sequence', with variation between and within speakers (pp. 67-68)."
for ph, als in (("i", ("ɪ", "ə")), ("e", ("æ", "ə")), ("ɨ", ("ə", "i", "u")), ("o", ("ɔ",)), ("a", ("æ", "ɛ", "e", "ə"))):
    for al in als:
        A(L, ph, al, "reduced or rapid speech, unstressed", "67-68",
          RED + (" Mayer's /ʉ/ is Tawerilmang & Sohn's ů (ɨ here)." if ph == "ɨ" else "") + M)
A(L, "a", "ɛ", "between syllables with high vowels", "68-69",
  "'/Vhigh _Vhigh/ /a/ → [ɛ]' (2.7a); Sohn (1975: 31-33) describes the result as [e], Mayer's data show mostly [ɛ] (pp. 68-69)." + M)
A(L, "a", "e", "before a syllable with a low vowel", "68-69", "'/_Vlow/ /a/ → [e]' (2.7b) (pp. 68-69)." + M)
A(L, "a", "aˤː", "lengthened", "68-69",
  "'In almost all tokens of lengthened /a/, there is a degree of pharyngealization' (/jafe/ [ˈjaˤː.fe̥] 'fire'), and speakers "
  "correct a lengthened [aː] without it (p. 69)." + M)

b.dec("mayer2025-woleaian",
      "Mayer (2025: 55-70) gives Woleaian 17 consonants, 9 marginal geminates and 8 vowels, with other symbols and values "
      "than the inventory of Tawerilmang & Sohn (1984) used here: b a voiced stop /b/ (here ɸ), apical post-alveolar "
      "ʃ̺ t͡ʃ̺ ɾ̺ (here ʂ ʈ͡ʂ r), the tap ɾ (here l), ʉ (here ɨ), and short and long œ, ɒ (here long-only əː, ɔː); no pʷ "
      "(Tawerilmang & Sohn's pw, here a phoneme, is one of his allophones of /b/). Which inventory should Woleaian show?",
      "Keep the inventory of Tawerilmang & Sohn (1984), with Mayer's allophones entered on the phonemes the two share and "
      "his analysis noted on the lect (sheet edit), until the user decides.",
      "Make Mayer's inventory the Woleaian inventory, with his marginal geminates, and respell the Woleaian rows of Bender "
      "et al. (2003a) and the allophones to it.",
      "55-70, 105-106")
b.dec("mayer2025-pck-vowels",
      "Mayer (2025: 72-74, Table 2.16) proposes Proto-Chuukic vowels *i *ʉ *u *e *o *æ *a *ɔ, with *e > ə, ɞ (e) in "
      "Central Chuukic, and gives cognates for them (Table 2.17). Enter them?",
      "Not entered: Proto-Chuukic here has the vowels it inherits from PMc, and Mayer marks the proposal as tentative "
      "('a full-fledged analysis ... is beyond the scope of this grammar', p. 72).",
      "Enter the proposal as a second vowel system of Proto-Chuukic (system Mayer), with the vowel rows of Woleaian and "
      "the other Chuukic lects of Table 2.17 against it.",
      "72-74")

md = """# mayer2025-woleaian

Mayer, Clemens J. 2025. *A grammar of Woleaian*. PhD dissertation, University of Hawai'i at Mānoa. Generator: `tools/batch_scripts/eight_sources_2026_11_25/mayer2025.py`.

## Scope

- **Allophones** (§2.1, pp. 55-70) on the inventory of Tawerilmang & Sohn (1984): [ɣ] of x; [b f bʷ pʷ p] of Mayer's /b/ (ɸ here); devoiced taps, [ɾ] for l in younger speakers, [n] for l + l; reduced vowels (Table 2.12); a-raising (Sohn 1975: 31-33); pharyngealized long a.
- Decisions `mayer2025-woleaian` (which inventory Woleaian shows) and `mayer2025-pck-vowels` (his proposed Proto-Chuukic vowels), both open.

## Sheet edits after landing

- `lects` (wole1240): notes on Mayer's analysis (Tables 2.1-2.2) and its differences from Tawerilmang & Sohn (§2.6).

## Not entered

- Mayer's inventory itself (decision `mayer2025-woleaian`) and his marginal geminates /pː mː mʷː nː fː ɾː kː wː ʃ̺ː/.
- Table 2.14 (Woleaian consonants against PMc and POc): adapted from Bender et al. (2003a), whose rows are already entered.
- The PCk vowel proposal (decision `mayer2025-pck-vowels`), phonotactics, stress and intonation.
"""
write("mayer2025-woleaian", b.t, md)
