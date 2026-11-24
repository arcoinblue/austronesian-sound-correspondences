# decisions-2026-11-24

The decisions the user reverted or commented on in the sheet's `decisions` tab on 24 November 2026, acted on from the data already entered (the source PDFs were not at hand: folder access was refused in that session).

    python3 tools/batch_scripts/decisions_2026_11_24/apply.py SRC OUT

`SRC` is `cldf/` with the sheet's `decisions` tab of that day; copy `OUT/*.csv` to `cldf/`. The sheet gets the same edits from the workflow *Apply a migration to the sheet* (branch of this PR, `allow_append` on, `max_deletions` 22: 21 phonemes rows and one allophones row change their key, which the tool does as delete and append).

| Decision | What the script does |
|---|---|
| `marck-diffused`, `blust1984-grades` | the rows become sporadic (conditions and lexical scope kept) |
| `pto-r`, `pld-l` | PPn *r > PTo *l sporadic, with condition and borrowing in the note; PMP *l > PLD *r disputed |
| `pazeh-j-final` | both final reflexes kept, with the user's explanation in each row |
| `ren-bel` | Rennellese is `mung1271` (Munggava), Bellona `mung1270`, under the language node `renn1242` |
| `ross1996-symbols`, `yang-tree` | notes |
| `neluz-internal`, `song-seediq`, `punan-internal`, `jackson1983-tree` | group nodes (Paranan-Pahanan; Toda-Truku, Toda, Truku; Punan Tubu-Bah; five Trukic groups with Glottolog's names and codes) |
| `lynch-parents`, `sef-dialects` | group Central Vanuatu under POc, PNCV as proposed parent; South Efate a language node opening Erakor, with Eton and Epau |
| `himes-r-y` | the six rows conditioned on '*y < PMP *R', three of them sporadic |
| `lin-amis` | Shibata's *d and *ɮ for Lin's *z and *d in Proto-Amis-Sakizaya and Lin's lower proto-languages; Lin's values in notes and `source_form` |
| `tsou-tfuya` | Tfuya rows inferred from the Duhtu rows (marked composed); Teruku and Takivatan `inherit` assumed-unchanged |
| `lrc2002-readings` | long vowels for the seven sketches that call length phonemic; Tobati /~/ as N |
| `lrc2002-subgroups` | Proto-Admiralty, Proto-Southeast Solomonic, Proto-Papuan Tip with the changes of Lynch et al. (2002: ch. 5); Western Oceanic, North New Guinea and Meso-Melanesian linkages |
| `lrc2002-nadroga`, `lynch2002h-table3` | Nadrogā and Western Fijian under PCP; Proto-Eastern Oceanic as an alternative node |
| `neluz-parent` | Proto-Northeastern Luzon under Proto-Northern Luzon; rows restated against Reid's inventory, those for PMP *h and *z as a second system of PNL |
| `francois2005-hybridization` | `francois.py`: the charts entered again, fusion pairs where the outcome is neither input vowel |
| (the user's instruction on small inventories) | Proto-Central Micronesian `inherit` assumed-unchanged, so that it and Kiribati keep the PMc vowels |

Left, each with a dated note on its decision: `landdayak-tables`, `malayic-glottal`, `malayic-phonetic`, `malayic-r`, `kayanic-held` (they need Smith 2017a), the rest of `punan-internal` and `lynch2002h-table3`, and `shibata-pb` (merging rows).
