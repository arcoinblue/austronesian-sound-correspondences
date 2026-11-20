# ASC status

The state of the Austronesian Sound Correspondences database. The generated part is rewritten by the build (`python3 build.py --check --status STATUS.md`), which the hourly sync and the batch workflow run; the sections after it are kept by hand. This file replaces the appended handoffs and the Google to-do doc.

<!-- BEGIN GENERATED: python3 build.py --check --status STATUS.md; do not edit by hand -->

## Data

| Table | Rows | |
|---|---|---|
| sources | 78 |  |
| lects | 616 | 113 dialect, 30 earlier-stage, 295 language, 178 proto-language |
| phonemes | 717 |  |
| correspondences | 4994 | plus 6039 implied and 816 stated retentions generated from lects.inherit |
| notation_map | 417 |  |
| decisions | 45 | 45 open |

Lects by `inherit`: (blank) 253, assumed-unchanged 302, stated-unchanged 61.
Inventories: edited 24, empty 154, reverse-generated 409, sourced 29.

## Checks

`build.py --check`: 0 error(s), 155 warning(s), 509 note(s).

| Warnings | Count |
|---|---|
| a work cited in notes has no sources row | 61 |
| no glottocode | 56 |
| a source is never cited | 27 |
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
| `ksr-retroflex` | Lee's Kosraean palatal fricative and flap. | Entered as retroflex. The r series (r, rw, ro) is an approximant ɻ, ɻˠ, ɻʷ after Lee & Wang (1984: 436, n. 4), not Lee's flap: changed 20 Nov 2026 at the user'… |  |
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
| `pocr-glottocodes` | Glottocodes for Löyöp and Mwerlap, which have no Glottolog languoid under those names. | From the language metadata of Ross et al. (2023): Löyöp = leha1244 (urr), as listed (p. 625); Mwerlap = Merlav merl1237 (mrm) (p. 626), identified by the name … |  |
| `pocr-volow` | Volow: Glottolog has it as a dialect of Mwotlap. | Entered as a language. |  |
| `bm-stated-unchanged` | Billings & McDonnell tabulate only the nontrivial correspondence sets (Tables 3, 5, 7, 10; Appendix G). Is a phoneme they do not list stated to be unchanged, o… | Stated: the 17 lects have inherit = stated-unchanged, and their generated rows are shown as stated ("unchanged per source"). |  |
| `smith-semicolon` | Smith's tables list several reflexes in a cell: 'the first listed reflex is the regular reflex, and the reflex(es) appearing after the semi-colon are condition… | First reflex: regular. After a semicolon: sporadic, unless the text states a condition (then regular with that environment). After a comma: regular, conditions… | 167 |
| `smith-higher-order` | Smith's higher-order groupings: North Borneo, Greater North Borneo, Central Sarawak, Punan-Müller-Schwaner, North Sarawak, Basap-Barito, Western Indonesian (20… | Not entered as nodes. They rest mainly on lexical innovations, which Smith himself later rejects as subgrouping evidence for Greater North Borneo and Barito-Ba… |  |
| `kayanic-glottocodes` | Glottocodes for Smith's Kayanic varieties. | Long Naah = Baram Kayan bara1370; Data Dian = Kayan River Kayan kaya1325 (Glottolog alt name); Balui Liko = Rejang Kayan reja1241; Gaai = Segai sega1243 (langu… |  |
| `ngorek-nj` | Ngorek reflex of *nj: Table 8 (p. 64) has nc, Table 11 (p. 67) nj. | Not entered. |  |
| `psm-j` | Proto-Segai-Modang reflex of Proto-Kayanic *j (PMP *z- and *nz). | *j > *c, inferred from Table 14: it shares the reflexes of medial *c, while *-y- > j stays apart. | 1 |
| `pkay-table23` | Proto-Kayanic (Table 23, p. 86): rows Smith prints with a question mark or hedges in the text. | *q- entered as a disputed blank (printed Ø?); *-z- > *c entered as disputed (the text says only that it 'may' be Proto-Kayanic, p. 58); *R- > *h entered as pri… | 8 |
| `pkmm-glottal` | Where do the added final glottal stop and the lowering of final high vowels belong? | Shared by Kayan and Murik-Merap (section 2.2.4.1, p. 84), as Smith concludes, not Kayan alone as Figure 10 (p. 54) has it; entered on both Proto-Kayan and Prot… | 6 |
| `kajang-hiatus` | Kajang reflexes of penultimate *u and *i before *a (Table 25: *-uCVC gʷ / _a; *-iCVC ʑ / _a). | Entered at Proto-Kajang as *u > *gʷ, *i > *ʑ before *a: the strengthened transition glide (p. 95: *dua > dəgʷa). |  |
| `melanau-node` | Is Proto-Melanau a node? | Entered, with only *-u > *əw and *-i > *əy, which Smith thinks 'likely' (p. 103). He calls Melanau a dialect network with mainly lexical evidence. |  |
| `punan-internal` | Punan internal subgrouping (Figures 28-29, pp. 122-124). | No lower nodes: Punan Tubu-Bah (*a > *ə / _Ca(C)#, *z > *c) conflicts with the backing of final *ə shared by Punan Tubu, Bah, Aput and Beketan (pp. 120-122). T… |  |
| `pld-l` | Land Dayak *l > *r: Hliboi and Sungkung have l (Table 50). | *l > *r at Proto-Land Dayak, as Smith reads it (p. 142); the two languages are entered with r > l. | 1 |
| `landdayak-tables` | Land Dayak Tables 50-51 (pp. 141-142). | Consonant cells with '?', Bidayuh's column ('Bid', variety not named) and the optional prenasalization '(n)t' are left out; vowels are entered from the summary… |  |
| `pmal-shared` | Proto-Malayic changes: Smith gives none. | Entered at Proto-Malayic: the reflexes shared by all seven lects of Tables 59-60 (*-q > h, *-b > p, *-d, *-j > t, *-j- > d, *-əC > a), marked composed. | 6 |
| `malayic-glottal` | Malayic cells such as 'aʔ; a', 'u; (uʔ)', 'r; ʔ' (Tables 59-60): Smith ties final glottal stops to particular lexemes (Figures 60-61, p. 196). | The glottal stop after final vowels is entered as a sporadic inserted ʔ; the vowel itself as unchanged. | 5 |
| `malayic-phonetic` | Table 60 prints some vowels phonetically: Seberuang ow, ey; Iban ʊu̯, ɪi̯, ʊə̯, ɪə̯; Mualang oə̯, ɛə̯. The text calls these allophonic (pp. 185-186: /kutu/ [ku… | Entered as the phonemes: u, i (Seberuang, Iban), o, e (Mualang closed syllables). |  |
| `malayic-r` | Malayic *R: Tables 59 prints ɣ (Keninjal, Seberuang, Mualang) and ɹˠ (Seberuang, final), but Figure 56 (p. 185) gives these as phonetic values of /r/. | Entered as r for all seven lects (phonemic). |  |
| `kayanic-held` | Kayanic and Kayan-Murik-Merap: intermediate stages above the microgroups Kayan, Murik-Merap and Segai-Modang. | Held back, by the rule to add correspondence tables and the reconstructions of established microgroups but to hold the intermediate stages above them. Proto-Ka… |  |

<!-- END GENERATED -->

## Not yet entered

Hand-kept. Collected from the handoffs of 2026-11-20 (09:20 to 15:00). The Google Doc "ASC to-do list" could not be read when this was written ("Permission denied"), so items that are only there still need adding here.

- Zobel 2020: the appendix of PKW reconstructions; the languages outside his Table 18 (Rai, Kamaru, Kalao). Lindu, Sedoa and Topoiyo are entered from prose only.
- Smith 2017a (Borneo): batch `smith2017-borneo` has Kayanic, Kajang, Melanau, Punan, Müller-Schwaner, Land Dayak and Malayic (see its BATCH.md for what was left out). Still to enter: §2.7 Barito (a linkage, no node), §2.9 Basap, §2.10 Sabah (Northeast Sabah, Molbog; Dusunic from Lobel), §2.11 Dayic, Berawan-Lower Baram, Bintulu (Kenyah has no table). The scripts are in `tools/batch_scripts/smith2017/`.
- Lobel 2013: nothing entered. Proto-Subanen (ch. 10) is stated against Proto-Greater Central Philippine and Southwest Sabah (ch. 11) against Proto-Southwest Sabah; neither node is in the database. Also Manide and Inagta Alabat (ch. 8).
- Kosraean (user's to-do, 20 Nov): from Lee (1975) and Lee & Wang (1984), r as an approximant, not a tap; the velarized consonants in a column of their own, apart from plain and labialized; velarized and labialized consonants given the same origin as the plain ones (the adjacent-vowel conditions optional); the correspondences filled in from Lee & Wang. Waiting for the two PDFs (Downloads folder).
- Grimes & Edwards 2026: only the classification trees are entered (Banda from summary (19), p. 505). The chapter tables (cognate sets) and the prose are not. Kept in lect notes, not as rows: *ma-p/*map, insertions (∅ > C, y-insertion, prothesis), metathesis (SW Maluku), whole-class rules (*C > ∅ /_#, *V > ∅ /_#), and changes whose input the tree never provides (Timaus **ʤ/**gʷ, East Nage **ʤ, Kei **d). The insertions could now be rows (parent `∅`).
- Bender et al. 2003a beyond p. 9 (the dictionary), and part 2 (2003b).
- Kosraean (Lee & Wang 1984): POC *q > ∅, *R > ∅, final-consonant loss, and all vowel correspondences (there are no POc > PMc vowel rows). Bender's Kosraean vowel respelling (Table 1) is only in the orthography note.
- POc *R (François 2011): PEOc and Proto-Southern Oceanic are not entered.
- Papora, Taokas, Basay: Shibata 2025 gives no separate reflexes.
- About 50 works cited in notes have no sources row (Hughes 2020a, Edwards 2015, Marck 1977, Brown 2001, Harrison 1978, Wolff 1982, ...): see the warnings above. Their details come from the citing sources' reference lists.
- `locator` is empty: table, figure and section references are still in the notes.

## Code to-do

Hand-kept.

- One environment per row (split the 132 comma-separated environments).
- ISO 639-3, coordinates and alternate names from a pinned Glottolog CLDF release by glottocode.
- The largest phoneme files (PAn *N 530 KB, *a and *s 250 KB) carry every deeper descendant row; they could load those rows only when "show deeper rows" is pressed.
- Show decisions on the site (a row's `decision`, with its status).
- Diphthongs as their own class (the Sumatran ones are vowels with `unknown` height and backness).
- Vowel length (Nauruan and Kosraean long vs short).
- A status between `regular` and `sporadic` for "almost regular" changes.
- Structured environments for geminates and long vowels (free text now).
- Lee & Wang's composed Kosraean rows are not marked `derivation` `composed` (decision `ksr-composition`).

## Housekeeping

- "TEMP import" 1-12 in Google Drive can be deleted.
- Branches `layout-v2-phase1`, `batches-to-sheet`, `e2e-batch-test`, `push-batch-fix`, `phase3-inherit-decisions` can be deleted on GitHub.
