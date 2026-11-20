# ASC status

The state of the Austronesian Sound Correspondences database. The generated part is rewritten by the build (`python3 build.py --check --status STATUS.md`), which the hourly sync and the batch workflow run; the sections after it are kept by hand. This file replaces the appended handoffs and the Google to-do doc.

<!-- BEGIN GENERATED: python3 build.py --check --status STATUS.md; do not edit by hand -->

## Data

| Table | Rows | |
|---|---|---|
| sources | 73 |  |
| lects | 562 | 102 dialect, 30 earlier-stage, 263 language, 167 proto-language |
| phonemes | 715 |  |
| correspondences | 3431 | plus 5809 implied and 279 stated retentions generated from lects.inherit |
| notation_map | 406 |  |
| decisions | 28 | 28 open |

Lects by `inherit`: (blank) 254, assumed-unchanged 291, stated-unchanged 17.
Inventories: edited 22, empty 154, reverse-generated 357, sourced 29.

## Checks

`build.py --check`: 0 error(s), 150 warning(s), 350 note(s).

| Warnings | Count |
|---|---|
| a work cited in notes has no sources row | 61 |
| no glottocode | 54 |
| a source is never cited | 24 |
| an attested lect has symbols that are not IPA | 8 |
| a reflex is not in the lect's sourced inventory | 3 |

## Open decisions

From the `decisions` tab. Confirm or revert one by changing its `status` in the sheet.

| id | Question | Reading taken | Rows |
|---|---|---|---|
| `mc-unchained-cells` | Two Micronesian cells cannot be chained: PCK *x (the PPC row has r and ∅, PCK only ∅) and Pohnpeian *ñ (the PPON row has ∅ and n, Pohnpeian only ∅). | Omitted; a note on each lect says so. |  |
| `kw-branches-unchanged` | Zobel's Table 18 has no column for the Northern and Southern Kaili–Wolio branches. What do their consonants continue? | Unchanged from PKW unless Zobel says otherwise; each such row says so and cites the PSKW/PNKW reconstructions of the appendix. | 32 |
| `ledo-subgroup` | Where does Ledo go? Zobel calls it mixed; Glottolog puts it in the Northern branch. | Under Southern Kaili–Wolio (its dominant lexical stratum). |  |
| `pmp-parent` | Chen et al. (2022) put PMP under Proto-Coastal Formosan. What is PMP's parent? | PAN; Chen et al.'s classification is noted on both lects. |  |
| `pmc-glottocode` | Which glottocode does Proto-Micronesian get? | micr1243, which includes Nauruan (as Blumenfeld 2022 does). |  |
| `atayal-original` | Which work is the original of the Proto-Atayal reconstruction? | Goderich (2020) only. |  |
| `lynch-biggs-ids` | Are the Lynch (2022) and Biggs (1965) works the ones the citing sources mean? | As entered in sources. |  |
| `ross2023-pages` | Page range of Ross, Pawley & Osmond 2023, ch. 1. | 1-46. |  |
| `kanakanavu-d` | Kanakanavu *d > sʲ word-initially: the table has s-(?); the text says *d is regularly r. | Entered, marked disputed. | 1 |
| `wolff-vowels` | The Wolff system has no vowel rows: Shibata's Table 2.16 has none. | Consonants only; the site says Wolff's vowels are not compared. |  |
| `ksr-ipa` | Kosraean consonants: Bender's transcription or IPA? | IPA (Bender's KSR sr, r are ʂ, ɾ). |  |
| `ksr-composition` | Lee & Wang (1984) state Kosraean against POc. How are their rows entered? | Composed to PMc through Bender's POc > PMc rows; the notes keep the POc statement. | 31 |
| `ksr-s-before-i` | Lee & Wang: POc *s lost before *i. Bender et al. have *s > s / _i. | s > ∅ / _i entered as regular. | 1 |
| `ksr-dr` | Lee & Wang's POC *(dr) > Kosraean ɾ. | Marked disputed. | 1 |
| `ksr-retroflex` | Lee's Kosraean palatal fricative and flap. | Entered as retroflex. |  |
| `ge-unchanged-nodes` | A phoneme that the tree does not mention at a node: what happens to it there? | Unchanged (lects.inherit = assumed-unchanged; the build generates the rows, shown grey as implied). |  |
| `ge-earlier-stage` | Tree nodes printed as one language with an ISO code, whose members are its varieties. | Entered as earlier-stage Pre-X (Pre-Tetun, Pre-Mambae, Pre-Kei, ...). |  |
| `ge-overlap` | Overlapping subgroups (Wetar-Galolen, Nuclear Wetar-Atauro; the Peripheral Babar shared changes). | Entered on the member lects (overlap_groups). |  |
| `ge-helong-d` | Helong "*l/-j-/z/d- > l": which *d? | Medial *d (text §4.1). | 1 |
| `ge-appendix-codes` | Corrections to appendix A codes: So'a soaa1237 → cent2074; Lamalera lama1278 → lama1299 (lama1278 goes to the Peripheral Lembata node); Semau Helong without a … | As listed. |  |
| `ge-uncertain` | Hukumina and Salas ("classification uncertain"). | Under PMP. |  |
| `ge-celebic` | Grimes & Edwards's Celebic changes. | Not re-entered on pcel (Zobel's). |  |
| `ge-iso` | ISO codes that differ between the tree and appendix A: Ngadha nxq/nxg, Baikeno bxq/bkx, Taliabu tly/tlv. | Ngadha nxg and Baikeno bkx (13:40); Taliabu still to settle. |  |
| `ge-identity-conflicts` | Four identity rows were added at a node because a daughter states a change from that phoneme, but the node itself states a change for it: Proto-Nuclear Rote *d… | Both kept: the stated change and the identity, as two elsewhere reflexes. | 4 |
| `pocr-parents` | Parents of PNCV, PNC and the Vanikoro languages (Teanu, Lovono, Tanema). | Directly under POc (PEOc, Proto-Southern Oceanic and a Temotu node are not entered). |  |
| `pocr-glottocodes` | Löyöp and Mwerlap have no Glottolog languoid under those names. | Left without glottocodes. |  |
| `pocr-volow` | Volow: Glottolog has it as a dialect of Mwotlap. | Entered as a language. |  |
| `bm-stated-unchanged` | Billings & McDonnell tabulate only the nontrivial correspondence sets (Tables 3, 5, 7, 10; Appendix G). Is a phoneme they do not list stated to be unchanged, o… | Stated: the 17 lects have inherit = stated-unchanged, and their generated rows are shown as stated ("unchanged per source"). |  |

<!-- END GENERATED -->

## Not yet entered

Hand-kept. Collected from the handoffs of 2026-11-20 (09:20 to 15:00). The Google Doc "ASC to-do list" could not be read when this was written ("Permission denied"), so items that are only there still need adding here.

- Zobel 2020: the appendix of PKW reconstructions; the languages outside his Table 18 (Rai, Kamaru, Kalao). Lindu, Sedoa and Topoiyo are entered from prose only.
- Lobel 2013 (Philippines) and Smith 2017 (Borneo).
- Grimes & Edwards 2026: only the classification trees are entered (Banda from summary (19), p. 505). The chapter tables (cognate sets) and the prose are not. Kept in lect notes, not as rows: *ma-p/*map, insertions (∅ > C, y-insertion, prothesis), metathesis (SW Maluku), whole-class rules (*C > ∅ /_#, *V > ∅ /_#), and changes whose input the tree never provides (Timaus **ʤ/**gʷ, East Nage **ʤ, Kei **d). The insertions could now be rows (parent `∅`).
- Bender et al. 2003a beyond p. 9 (the dictionary), and part 2 (2003b).
- Kosraean (Lee & Wang 1984): POC *q > ∅, *R > ∅, final-consonant loss, and all vowel correspondences (there are no POc > PMc vowel rows). Bender's Kosraean vowel respelling (Table 1) is only in the orthography note.
- POc *R (François 2011): PEOc and Proto-Southern Oceanic are not entered.
- Papora, Taokas, Basay: Shibata 2025 gives no separate reflexes.
- About 50 works cited in notes have no sources row (Hughes 2020a, Edwards 2015, Marck 1977, Brown 2001, Harrison 1978, Wolff 1982, ...): see the warnings above. Their details come from the citing sources' reference lists.
- `locator` is empty: table, figure and section references are still in the notes.

## Code to-do

Hand-kept.

- Restructuring plan, rest of phase 3: one environment per row (split the 132 comma-separated environments); ISO 639-3, coordinates and alternate names from a pinned Glottolog CLDF release by glottocode.
- Restructuring plan, phase 4: per-phoneme output loaded on demand (`pan.json` is 7.6 MB); split `build.py` and `site/app.js`.
- Show decisions on the site (a row's `decision`, with its status).
- Diphthongs as their own class (the Sumatran ones are vowels with `unknown` height and backness).
- Vowel length (Nauruan and Kosraean long vs short).
- A status between `regular` and `sporadic` for "almost regular" changes.
- Structured environments for geminates and long vowels (free text now).
- Lee & Wang's composed Kosraean rows are not marked `derivation` `composed` (decision `ksr-composition`).

## Housekeeping

- "TEMP import" 1-12 in Google Drive can be deleted.
- Branches `layout-v2-phase1`, `batches-to-sheet`, `e2e-batch-test`, `push-batch-fix` can be deleted on GitHub.
