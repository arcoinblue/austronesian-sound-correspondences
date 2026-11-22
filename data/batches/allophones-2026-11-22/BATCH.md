# allophones-2026-11-22

The first rows of the new `allophones` tab: every allophone statement found in the sources already in the sheet, so that each phoneme's page explains how it is realised. 582 rows for 384 phonemes of 80 lects, from 48 sources.

Two kinds of input:

1. **The sheet's own notes.** Phoneme notes and correspondence notes that already quoted a source's allophones (Tsuchida's "[ʃ] before i, [s] elsewhere", Blumenfeld's rules 23 and 25, Smith's Malayic vowel breaking), each checked against the page it cites.
2. **The source PDFs** in the user's Downloads/austdic folder (and Hsieh 2007 in Downloads), read at the phonology chapter of every source that gives a lect's inventory: Goderich 2020, Blust 1999b, 2002, 2003, 2007, Tsuchida 1975, Zeitoun 2005a, 2024a, 2024b, Pan 2012, the Adelaar & Himmelmann (2005) chapters (Zeitoun on Tsou, Tsukida on Seediq, van Engelenhoven et al. on Tetun and Leti, Klamer on Kambera, Woollams on Karo), Li 2018, Jiang 2012, De Busser 2009, Shibata 2020, Teng 2008, Cauquelin 2015, Yeh 2024, Lin 2022, Chen 2006, Chang 2006, Chuang 2024, Song 2025, Li & Tsuchida 2006, Lu 2005, Hsin 2000, Hsieh 2007, Blumenfeld 2022a, Lee 1975, Lynch 2019b, c, Adelaar 2014, Smith 2017a, Billings & McDonnell 2024. The generator is `tools/batch_scripts/allophones_2026_11_22/`.

## Conventions

- One row per allophone; the elsewhere realisation is entered when the source states it.
- `environment` uses the correspondence notation where it fits (`_i`, `V_V`, `word-finally`) and the source's words otherwise ("older speakers", "free variation", "fast speech").
- Statements a source makes for a whole language or group are entered on each lect it covers (decision `allophones-readings`).
- A single phonetic value is not an allophone: "[p] (p. 85)" or Goderich's orthography table entries that only name the sound are not entered.
- Works cited only in passing (W. Chen 2017, Cheng 2017a-c, Ferrell 1970, Lee 2018, Yeh 1991 …) have no sources row; the notes name them without a year.

## Sheet edits made directly

- `phonemes` rows 1351 and 1355 (siraya-um u, a): the u note said "palatalized allophone äw", but Adelaar (2014: 6) finds no palatalization in UM. Both notes now say so.
- `decisions` row 134: `allophones-readings` (open).
- New tab `allophones` (header row only; this batch fills it).

## Not entered

- Distribution statements that are not allophony (Teruku p, b "become k word-finally", consonants that do not occur finally).
- Loanword phonemes and morphophonemic alternations (Pazeh z ~ d in reduplication, Paiwan v ~ w at morpheme edges), except where the source calls the variants allophones.
- Lynch (2000) on South Efate, Blust (2009) on Palauan, Blust (2014) on Dobel, Lobel (2013) on Manide and Inagta Alabat: no allophone statements for the lects' phonemes.
- Proto-language "phonetic values" that are alternative analyses rather than allophones (Shibata's PAn *C as [ʈ] or [ʈ͡ʂ]).


## Applied

2026-11-22 13:08 UTC, by the push-batch workflow.
- allophones: sheet rows 2-583
