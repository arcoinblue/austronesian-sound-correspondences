# ASC status

The state of the Austronesian Sound Correspondences database. The generated part is rewritten by the build (`python3 build.py --check --status STATUS.md`), which the hourly sync and the batch workflow run; the sections after it are kept by hand. This file replaces the appended handoffs and the Google to-do doc.

<!-- BEGIN GENERATED: python3 build.py --check --status STATUS.md; do not edit by hand -->

## Data

| Table | Rows | |
|---|---|---|
| sources | 253 |  |
| lects | 1049 | 259 dialect, 33 earlier-stage, 14 group, 455 language, 9 linkage, 279 proto-language |
| phonemes | 4534 |  |
| correspondences | 12417 | plus 12000 implied and 3370 stated retentions generated from lects.inherit |
| notation_map | 562 |  |
| allophones | 979 |  |
| decisions | 186 | 129 confirmed, 57 reverted |

Lects by `inherit`: (blank) 179, assumed-unchanged 582, assumed-unchanged (automatic, fewer than 13 phonemes known) 49, stated-unchanged 239.
Inventories: edited 28, empty 36, reverse-generated 803, sourced 182.

## Checks

`build.py --check`: 0 error(s), 327 warning(s), 1054 note(s).

| Warnings | Count |
|---|---|
| no glottocode | 138 |
| a work cited in notes has no sources row | 77 |
| a source is never cited | 52 |
| no page number for the citation | 26 |
| a reflex is not in the lect's sourced inventory | 25 |
| repeats the fusion row at … | 6 |
| an attested lect has symbols that are not IPA | 3 |

## Open decisions

From the `decisions` tab. Confirm or revert one by changing its `status` in the sheet.

None.

<!-- END GENERATED -->

## Not yet entered

Hand-kept. Collected from the handoffs of 2026-11-20 (09:20 to 15:00). The Google Doc "ASC to-do list" could not be read when this was written ("Permission denied"), so items that are only there still need adding here.

- Zobel 2020: the appendix of PKW reconstructions; the languages outside his Table 18 (Rai, Kamaru, Kalao). Lindu, Sedoa and Topoiyo are entered from prose only.
- Smith 2017a (Borneo): batch `smith2017-borneo` has Kayan, Murik-Merap, Segai-Modang, Kajang, Melanau, Punan, Müller-Schwaner, Land Dayak and Malayic (see its BATCH.md for what was left out). Proto-Kayanic and Proto-Kayan-Murik-Merap are held back as intermediate stages (`kayanic-held`), and Proto-Malayic carries the reflexes all seven lects share, marked composed (`pmal-shared`, reverted), by the user's rule of 20 Nov: correspondence tables and established microgroups yes, intermediate reconstructions above them not yet. Still to enter: §2.7 Barito beyond Tables 56-57 (Proto-Barito is a node since the revert of `smith-barito`), §2.9 Basap, §2.10 Sabah (Northeast Sabah, Molbog; Dusunic from Lobel), §2.11 Dayic, Berawan-Lower Baram, Bintulu (Kenyah has no table). The scripts are in `tools/batch_scripts/smith2017/`.
- Lobel 2013: nothing entered. Proto-Subanen (ch. 10) is stated against Proto-Greater Central Philippine and Southwest Sabah (ch. 11) against Proto-Southwest Sabah; neither node is in the database. Also Manide and Inagta Alabat (ch. 8).
- Grimes & Edwards 2026: only the classification trees are entered (Banda from summary (19), p. 505). The chapter tables (cognate sets) and the prose are not. Kept in lect notes, not as rows: *ma-p/*map, insertions (∅ > C, y-insertion, prothesis), metathesis (SW Maluku), whole-class rules (*C > ∅ /_#, *V > ∅ /_#), and changes whose input the tree never provides (Timaus **ʤ/**gʷ, East Nage **ʤ, Kei **d). The insertions could now be rows (parent `∅`).
- Bender et al. 2003a beyond p. 9 (the dictionary), and part 2 (2003b).
- Kosraean (Lee & Wang 1984): POC *q > ∅, *R > ∅, final-consonant loss; *a-raising, high-vowel lowering, low-vowel dissimilation and monophthongisation (weak evidence in the source; see batch `leewang1984-kosraean`). No reflexes for the ɻ series and the glides. Bender's Kosraean vowel respelling (Table 1) is only in the orthography note.
- Blust 2013: ch. 8, pp. 553-593, read directly (excerpt in Downloads/austdic). Batch `blust2013-reinforce` adds it as a second source for PMP > POc and for the PAN *j, *h and *R reflexes of the Formosan languages under PAN. Not entered: the PMP > POc cluster fusions (Ross's pairs are in), and the reflexes of languages below intermediate nodes (Tables 8.27, 8.30).
- Polynesian (batch `marck2000-polynesian`): Marck 2000 is entered from Tables 2.2, 3.1, 2.32 and 3.30 and Table A.1; Walworth 2014 and Wilson 2021 as alt_parents, plus Wilson's single-word changes. Not entered: Marck's Appendix B and Tables 3.15-3.29 (lexeme-level vowel changes); Table 2.2 "Pla" (undefined); vowel loss between identical consonants (Table 2.2 note 9); Wilson's PEPNP(N). Wilson 2012 (batch `todo-audit`) adds five single-word changes (§5.1, examples 6, 7, 33, 35, 41) on PNO-EPN, PSNO-EPN and PCNO-EPN; not entered are its grammatical innovations and the word changes that are not one-segment substitutions (*kiu > *kiwi, *tuafafine > *tuafine, *lele > *lei, *palu > *lapu, *qaho-qatea > *qooatea). PPn sits directly under POc (decision `ppn-parent`), so most POc phonemes are unentered for PPn.
- Blust's historical phonologies (batch `blust-histphon`): Chamorro (2000) and Palauan (2009) under PMP; Kiput (2002) and Òma Lóngh (2007) under the new Proto-North Sarawak and Proto-Kenyah nodes (decision `pns-node`); Dobel (2014) composed against the Grimes & Edwards Aru nodes (`dobel-composed`). Not entered: the irregular and loan forms each paper lists, Kiput's PMP > PNS changes (§3.1) and prenasalized stops, Dobel's diphthongs and *q > ʔ, the Chamorro and Palauan loanword strata (see the batch's BATCH.md). Berawan-Lower Baram, Lower Baram and Highland Kenyah are not nodes: Kiput and Òma Lóngh sit directly under PNS and PK. Smith's §2.11 (Berawan-Lower Baram, Bintulu) could now go under PNS.
- POc *R (François 2011): PEOc and Proto-Southern Oceanic are not entered.
- Southern Vanuatu (Lynch 2001; batches `lynch2001`, `lynch2001-reparent`): canonical-form changes (pretonic vowel loss, accretion, Article Reduction), vowel tendencies without stated conditions, Anejom vowel sequences, chapters 5-8 and Appendix II.
- Central Pacific (Geraghty 1986; batches `geraghty1986-pcp`, `geraghty1986-rotuman`): POc > PCP is entered only for *mʷ, the liquids and *R; the PCP > PPn rows are held until `ppn-parent` and `geraghty1986-ppn` are decided (`python3 tools/batch_scripts/geraghty1986/build.py ppn`); Western/Eastern Fijian and Nadrogā are not under Proto-Fijian. Geraghty 1983, Table 15 (38 communalects, pp. 183-186) is not entered (`geraghty1983-communalects`).
- New Caledonia (Ozanne-Rivierre 1992, Geraghty 1989; batch `nc-ozannerivierre1992`): PNC vowels; Geraghty's aspirates and internal nodes; the Loyalty, Mainland, Northern and Southern New Caledonian subgroups.
- Reverted decisions carried out on 23 Nov 2026 (`tools/batch_scripts/reverts_2026_11_23/`), with what is left: `wolff-vowels` not done (Wolff 2010 not read directly; the PDFs were not reachable); `yeh-puyuma-tree`: the three nodes below Proto-Nuclear Puyuma have no rows of their own, and Yeh's pp. 193-194 should be re-read for their innovations (Katripulr and Kasavakan share **v and perhaps **f, Tables 4.30-4.31); `ge-overlap`: the Peripheral Babar shared changes (overlapping sets) stay on the languages, and Glottolog's Wetar-Galolen (weta1247) may fit pwetgal; `pmal-shared`: Iban *a > æ / _C# now also covers the *ə merged into *a at Proto-Malayic; `pn-tree`: Marck's Proto-Central East Polynesian, Proto-Marquesic and Proto-Nuclear Marquesic have no daughters in the main tree.
- Five sources of 23 Nov 2026 (batches `blust1984-mussau`, `ross1996-yapese`, `ho1982-hienghene`, `francois2005-vowels`, `jackson1983-trukic`; scripts in `tools/batch_scripts/new_sources_2026_11_23/`): Ross 1996 Sets A, B, D, UW and E (`ross1996-strata`); Haudricourt & Ozanne-Rivierre 1982 palatal rows, *R and vowels of Table 3.3.4 and the conditions of §3.3 (`ho1982-composition`); François 2005 Table 1 inventories, §§4.3, 5 and 6; Jackson 1983 Figure 4 nodes (`jackson1983-tree`), rule (7), §§3.3.2-3.3.3 and chapter 4; Blust 1984 irregular reflexes attested once and the canonical changes.
- Ten sources of 23 Nov 2026, second set (batches `lynch2004-q`, `ross2011-kw`, `lynch2002h-labiovelars`, `charpentierfrancois2015-polynesia`, `barlowross2025-tomoip`, `bril2020-nc`, `rossnaess2007-temotu`, `lackeyboerger2021-temotu`, `francois2009-vanikoro`, `francoisetal2015-vanuatu`; scripts in `tools/batch_scripts/new_sources_2026_11_23b/`): Lynch 2002h Table 3 for Mota (waits for PNCV consonants) and the other columns (`lynch2002h-table3`); Ross 2011 *gʷ and the Southeast Solomonic and Papuan Tip reflexes (`ross2011-kw`); Barlow & Ross 2025 Proto-Tomoip-New Ireland (`barlowross2025-tree`); Bril 2020 vowels and PNNC (`bril2020-vowels`, `bril2020-pnnc`); Charpentier & François 2015 Pa'umotu dialects; Ross & Næss 2007 cells superseded by Lackey & Boerger 2021 (`temotu-composed`); Nalögo and Noipä; the Santa Cruz node; Sa (Garde 2015).
- Ten sources of 23 Nov 2026, third set (batches `lynch2019a-linguolabial`, `lynch2005b-nese`, `lynchbrotchie2010-tirax`, `lynch2003b-loyalties`, `lynch2003a-lvd`, `lynch2022-o`, `biggs1965-rotuman`, `nc-north-1993-1995`; scripts in `tools/batch_scripts/new_sources_2026_11_23c/`; migration `tools/batch_scripts/smith2023_nodes/`): not entered are Ozanne-Rivierre 1995 (Proto-North and Appendices 1-6, `ozannerivierre1995-north`, with `bril2020-pnnc`), Rivierre 1993 (tones, `rivierre1993-tones`), the Santo languages known from Tryon's wordlists and Tape (`lynch2019a-scope`, `lynchbrotchie2010-tirax`), the Loyalties vowels (PNC has no vowels), Biggs's Set I and PEO (`biggs1965-sets`), Lynch's six-vowel POc (`lynch2022-poc-vowels`), and Ross et al. 2023 Appendix A (a list of data sources).
- Six Micronesian sources of 24 Nov 2026 (batches `jackson1984-trukic`, `rehg1984-pohnpeian`, `harrison1984-mokilese`, `tawerilmangsohn1984-woleaian`, `hughes2020-nauruan`; scripts in `tools/batch_scripts/micronesia_2026_11_24/`): the Kiti and Ngatikese dialects of Pohnpeian (`rehg1984-dialects`); daughter reflexes of PCK *ɨ (`jackson1984-central-vowel`); Jackson's POC *nj and the POC *ŋk > k of Rehg, Harrison and Tawerilmang & Sohn, which conflict with PMc *x; Harrison's *e and single-form exceptions in all four 1984 papers; Hughes's pre-Nauruan stages (not entered by the user's choice), Cr10iv and Cr24vii, ch. 2-3 beyond the allophones, and §4.5.
- Papora, Taokas, Basay: Shibata 2025 gives no separate reflexes.
- About 50 works cited in notes have no sources row (Edwards 2015, Marck 1977, Brown 2001, Harrison 1978, Wolff 1982, ...): see the warnings above. Their details come from the citing sources' reference lists.
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
- Competing reconstructions (`competes_with`) are handled by the site, but no lect uses the column yet.

## Housekeeping

- "TEMP import" 1-12 in Google Drive can be deleted.
- Branches `layout-v2-phase1`, `batches-to-sheet`, `e2e-batch-test`, `push-batch-fix`, `phase3-inherit-decisions` can be deleted on GitHub.
