#!/usr/bin/env python3
"""Formosan leftovers of the gap audit of 26 November 2026.

Batch formosan-leftovers. Lin (2022) Tables 4.3-4.38 and 7.1-7.5, Shibata (2020) Table 5.6 and the (?) items of
the audit (Tseng 2023, Yeh 2024, Goderich 2020, Shibata 2025, Chuang 2024) were compared with the rows in cldf/.
Nearly everything is already there, through the summary tables and the stated-unchanged inheritance of the
dialects; BATCH.md has one line per item. Entered: the two sporadic changes of Yeh (2024: 210, Tables 6.14-6.15).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, existing

D = "formosan-leftovers"
b = Batch("yeh2024")
LECTS = existing("lects", "id")
for lid in ("katipul", "kasavakan", "pkatkas"):
    assert lid in LECTS, lid

b.corr("katipul", "s", "t̪", "_#", "210",
       "Table 6.14, 'Sporadic sound change in Katripulr': Proto-Puyuma *ɡaməs 'to catch' is hamut in Katripulr, "
       "against Tamalrakaw and Kasavakan haməs, Likavung hamus, Nanwang ɡaməs. One word; the vowel is u as in "
       "Likavung. Printed t; the Katripulr stop is dental (t̪ in the inventory).", source_form="t", status="sporadic", n=1, derivation="as-stated", decision=D, locator="Table 6.14",
       lexical_scope="*ɡaməs 'to catch'", examples="*ɡaməs > hamut", as_printed="P-Puy *ɡaməs : Katripulr hamut")
b.corr("kasavakan", "ʐ", "h", "#_", "210",
       "Table 6.15, 'Sporadic sound change in Kasavakan': Proto-Puyuma *ɖənan 'mountain' is hənan in Kasavakan "
       "(Nanwang ɖənan, Tamalrakaw and Likavung ʐənan, Katripulr ðənan). 'The expected form in Kasavakan is "
       "**ðənan, while in this word, there is a specific sound change **ð > h, and it is not found in other forms "
       "and dialects' (p. 210). The parent phoneme is Proto-Katripulr-Kasavakan *ʐ, Yeh's Proto-Puyuma *ɖ.",
       status="sporadic", n=1, derivation="as-stated", decision=D, locator="Table 6.15",
       lexical_scope="*ɖənan 'mountain'", examples="*ɖənan > hənan", as_printed="P-Puy *ɖənan : Kasavakan hənan")

b.dec(D,
      "The Formosan leftovers of the gap audit of 26 November 2026 (Lin 2022 Tables 4.3-4.38, 7.1-7.5; Shibata 2020 "
      "Table 5.6; Tseng 2023 Tables 3.2.x, 4.2.x, 6.4; Yeh 2024 Tables 4.3-4.25, 6.14-6.15; Goderich 2020 Tables "
      "4.42-4.45, 4.50; Shibata 2025 Tables 3.14, 3.16, 3.29, 3.31, 6.15-6.31; Chuang 2024 Table 6.1): what is entered?",
      "Two sporadic rows from Yeh (2024: 210): Katripulr *-s > -t in 'to catch' and Kasavakan *ɖ (here *ʐ) > h in "
      "'mountain'. Nothing else. Lin's Tables 4.3-4.23 illustrate dialect reflexes that the rows of his chapter 6 "
      "and the stated-unchanged inheritance of the ten dialects already give; his consonant harmony (Tables "
      "4.31-4.38) is word by word, 'the directionality and the environment ... seems random' (p. 97); Tables "
      "7.1-7.5 list regular and irregular reflexes of PAN *d, the irregular ones being loans, contamination or "
      "doubtful PAN etyma. Shibata (2020) Table 5.6 is a list of seven irregular words. Goderich's Table 4.50 is the "
      "list of changes already entered on the Atayal nodes and dialects; Tables 4.42-4.44 are its examples. Shibata "
      "(2025) Tables 3.14-3.31 reproduce the reconstructions of Tseng, Lin, Yeh and Chuang, entered from those "
      "works, and Tables 6.15-6.31 restate the reflexes in his own PAn values, which are the notation system "
      "'Shibata'. Chuang's Table 6.1 has the Proto-Paiwan reflexes already entered from his chapter 4, beside "
      "Li's (1977) Proto-Rukai and Ting's (1978) Proto-Puyuma.",
      "Enter the lexical irregularities as sporadic rows: Lin's PAN *d > PAS *t in *duSa, *qaRidaŋ, *kudəm and *d > "
      "*k in *dapa, *dəRuŋ (pp. 147-150), and his harmony forms dialect by dialect. Enter Tseng's Table 6.4 "
      "(Taokas and Saisiyat reflexes of six PAN phonemes after Ross 2012: 1274-1275) with Ross (2012), the next "
      "source of the audit; Taokas is not a lect. Enter Shibata's (2025) notes on phonetic paths (Table 6.15: PAn "
      "*S > Proto-Atayal s, 'sporadically [ʃ]') as allophones.", "210")

BATCH_MD = """# formosan-leftovers

**Scope.** The Formosan items left by the gap audit of 26 November 2026, compared with `cldf/` at ae731d3.

**Entered.** Two sporadic rows from Yeh (2024: 210, Tables 6.14-6.15): Katripulr *-s > -t in *ɡaməs 'to catch';
Kasavakan *ʐ (Yeh's *ɖ) > h in *ɖənan 'mountain'.

**Not entered, one line per item.**
- Lin (2022) Tables 4.3-4.23 (reflexes of each Proto-Amis-Sakizaya phoneme in ten dialects): word lists; the
  reflexes stated in the prose of §4.2 (pp. 57-80) equal the rows of chapter 6 (Tables 6.1-6.25) composed with the
  dialects' stated-unchanged inheritance (*b, Lin's *d and *z, *ɾ; the rest unchanged). The Sakizaya [o] of /u/
  is in `allophones`.
- Lin (2022) Tables 4.31-4.38 (consonant harmony): word-by-word assimilations with no rule (p. 97).
- Lin (2022) Tables 7.1-7.5: regular PAN *d > PAS *z (entered, as *d) and irregular etyma.
- Shibata (2020) Table 5.6: seven words with apparent sporadic changes in Takituduh and Takibakha.
- Tseng (2023) Tables 3.2.x, 4.2.x: entered (locators Table 3.2.1, 4.2.1). Table 6.4: Taokas and Saisiyat after
  Ross (2012); left for Ross (2012).
- Yeh (2024) Tables 4.3-4.25: the examples behind Table 4.26, which is entered (110 rows).
- Goderich (2020) Tables 4.42-4.44 (the merger of -lit and -liʔ), 4.50 (eleven changes by dialect): entered on
  the Atayal nodes and dialects. Table 4.45 (Li's *g') not read.
- Shibata (2025) Tables 3.14, 3.16, 3.29, 3.31 and 6.15-6.31: restatements (see the decision).
- Chuang (2024) Table 6.1: the Proto-Paiwan column equals the rows from his chapter 4.

**How the comparison was done, and its limits.** From the text layer of the PDFs, not from page images: Lin §4.2,
§4.4 and §7.1 (prose; the cells of Tables 4.3-4.23 were not compared one by one), Shibata (2020) p. 99, Tseng
p. 127, Yeh p. 210, Goderich pp. 138, 140, 148, Chuang p. 161, Shibata (2025) Tables 3.16, 6.15, 6.16, 6.23.
Not opened: Yeh's Tables 4.3-4.25, Goderich's Tables 4.43 and 4.45, Shibata's (2025) Tables 3.14, 3.29, 3.31 and
the other tables of his §6.5; for these the result rests on the captions and on the rows already entered.
"""
write(D, b.t, BATCH_MD)
