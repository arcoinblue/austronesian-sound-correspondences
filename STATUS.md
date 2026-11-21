# ASC status

The state of the Austronesian Sound Correspondences database. The generated part is rewritten by the build (`python3 build.py --check --status STATUS.md`), which the hourly sync and the batch workflow run; the sections after it are kept by hand. This file replaces the appended handoffs and the Google to-do doc.

<!-- BEGIN GENERATED: python3 build.py --check --status STATUS.md; do not edit by hand -->

## Data

| Table | Rows | |
|---|---|---|
| sources | 107 |  |
| lects | 713 | 128 dialect, 30 earlier-stage, 350 language, 205 proto-language |
| phonemes | 1130 |  |
| correspondences | 6497 | plus 6459 implied and 1555 stated retentions generated from lects.inherit |
| notation_map | 444 |  |
| decisions | 83 | 83 open |

Lects by `inherit`: (blank) 263, assumed-unchanged 330, stated-unchanged 120.
Inventories: edited 24, empty 154, reverse-generated 489, sourced 46.

## Checks

`build.py --check`: 0 error(s), 166 warning(s), 661 note(s).

| Warnings | Count |
|---|---|
| a work cited in notes has no sources row | 66 |
| no glottocode | 58 |
| a source is never cited | 31 |
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
| `ksr-composition` | Lee & Wang (1984) state Kosraean against POc. How are their rows entered? | Composed to PMc through Bender's POc > PMc rows; the notes keep the POc statement. | 48 |
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
| `ge-identity-conflicts` | Four identity rows were added at a node because a daughter states a change from that phoneme, but the node itself states a change for it: Proto-Nuclear Rote *d… | Both kept: the stated change and the identity, as two elsewhere reflexes. | 5 |
| `pocr-parents` | Parents of PNCV, PNC and the Vanikoro languages (Teanu, Lovono, Tanema). | Directly under POc (PEOc, Proto-Southern Oceanic and a Temotu node are not entered). |  |
| `pocr-glottocodes` | Glottocodes for Löyöp and Mwerlap, which have no Glottolog languoid under those names. | From the language metadata of Ross et al. (2023): Löyöp = leha1244 (urr), as listed (p. 625); Mwerlap = Merlav merl1237 (mrm) (p. 626), identified by the name … |  |
| `pocr-volow` | Volow: Glottolog has it as a dialect of Mwotlap. | Entered as a language. |  |
| `bm-stated-unchanged` | Billings & McDonnell tabulate only the nontrivial correspondence sets (Tables 3, 5, 7, 10; Appendix G). Is a phoneme they do not list stated to be unchanged, o… | Stated: the 17 lects have inherit = stated-unchanged, and their generated rows are shown as stated ("unchanged per source"). |  |
| `smith-semicolon` | Smith's tables list several reflexes in a cell: 'the first listed reflex is the regular reflex, and the reflex(es) appearing after the semi-colon are condition… | First reflex: regular. After a semicolon: sporadic, unless the text states a condition (then regular with that environment). After a comma: regular, conditions… | 171 |
| `smith-higher-order` | Smith's higher-order groupings: North Borneo, Greater North Borneo, Central Sarawak, Punan-Müller-Schwaner, North Sarawak, Basap-Barito, Western Indonesian (20… | Not entered as nodes. They rest mainly on lexical innovations, which Smith himself later rejects as subgrouping evidence for Greater North Borneo and Barito-Ba… |  |
| `kayanic-glottocodes` | Glottocodes for Smith's Kayanic varieties. | Long Naah = Baram Kayan bara1370; Data Dian = Kayan River Kayan kaya1325 (Glottolog alt name); Balui Liko = Rejang Kayan reja1241; Gaai = Segai sega1243 (langu… |  |
| `ngorek-nj` | Ngorek reflex of *nj: Table 8 (p. 64) has nc, Table 11 (p. 67) nj. | Not entered. |  |
| `psm-j` | Proto-Segai-Modang reflex of Proto-Kayanic *j (PMP *z- and *nz). | *j > *c, inferred from Table 14: it shares the reflexes of medial *c, while *-y- > j stays apart. | 1 |
| `pkay-table23` | Proto-Kayanic (Table 23, p. 86): rows Smith prints with a question mark or hedges in the text. | *q- entered as a disputed blank (printed Ø?); *-z- > *c entered as disputed (the text says only that it 'may' be Proto-Kayanic, p. 58); *R- > *h entered as pri… | 8 |
| `pkmm-glottal` | Where do the added final glottal stop and the lowering of final high vowels belong? | Shared by Kayan and Murik-Merap (section 2.2.4.1, p. 84), as Smith concludes, not Kayan alone as Figure 10 (p. 54) has it; entered on both Proto-Kayan and Prot… | 6 |
| `kajang-hiatus` | Kajang reflexes of penultimate *u and *i before *a (Table 25: *-uCVC gʷ / _a; *-iCVC ʑ / _a). | Entered at Proto-Kajang as *u > *ɡʷ, *i > *ʑ before *a: the strengthened transition glide (p. 95: *dua > dəgʷa). |  |
| `melanau-node` | Is Proto-Melanau a node? | Entered, with only *-u > *əw and *-i > *əy, which Smith thinks 'likely' (p. 103). He calls Melanau a dialect network with mainly lexical evidence. |  |
| `punan-internal` | Punan internal subgrouping (Figures 28-29, pp. 122-124). | No lower nodes: Punan Tubu-Bah (*a > *ə / _Ca(C)#, *z > *c) conflicts with the backing of final *ə shared by Punan Tubu, Bah, Aput and Beketan (pp. 120-122). T… |  |
| `pld-l` | Land Dayak *l > *r: Hliboi and Sungkung have l (Table 50). | *l > *r at Proto-Land Dayak, as Smith reads it (p. 142); the two languages are entered with r > l. | 1 |
| `landdayak-tables` | Land Dayak Tables 50-51 (pp. 141-142). | Consonant cells with '?', Bidayuh's column ('Bid', variety not named) and the optional prenasalization '(n)t' are left out; vowels are entered from the summary… |  |
| `pmal-shared` | Proto-Malayic changes: Smith gives none. | No Proto-Malayic rows; every change is entered on each lect. The reflexes shared by all seven lects of Tables 59-60 (*-q > h, *-b > p, *-d, *-j > t, *-j- > d, … |  |
| `malayic-glottal` | Malayic cells such as 'aʔ; a', 'u; (uʔ)', 'r; ʔ' (Tables 59-60): Smith ties final glottal stops to particular lexemes (Figures 60-61, p. 196). | The glottal stop after final vowels is entered as a sporadic inserted ʔ; the vowel itself as unchanged. | 5 |
| `malayic-phonetic` | Table 60 prints some vowels phonetically: Seberuang ow, ey; Iban ʊu̯, ɪi̯, ʊə̯, ɪə̯; Mualang oə̯, ɛə̯. The text calls these allophonic (pp. 185-186: /kutu/ [ku… | Entered as the phonemes: u, i (Seberuang, Iban), o, e (Mualang closed syllables). |  |
| `malayic-r` | Malayic *R: Tables 59 prints ɣ (Keninjal, Seberuang, Mualang) and ɹˠ (Seberuang, final), but Figure 56 (p. 185) gives these as phonetic values of /r/. | Entered as r for all seven lects (phonemic). |  |
| `kayanic-held` | Kayanic and Kayan-Murik-Merap: intermediate stages above the microgroups Kayan, Murik-Merap and Segai-Modang. | Held back, by the rule to add correspondence tables and the reconstructions of established microgroups but to hold the intermediate stages above them. Proto-Ka… |  |
| `ksr-secondary` | Origin of the Kosraean velarised and rounded consonants. | Each is entered as a reflex of the same PMc consonant as the plain one, before e and ɛ, marked sporadic: Lee & Wang put distinctive velarisation after PMc and … | 23 |
| `vowel-default` | A lect whose sourced vowels are a bare i e a o u system (below POc) or i ə a u system (below PMP or PAN), with no stated vowel change: what are its vowel corre… | Taken as its parent's vowels unchanged, as implied retentions, until a source says otherwise. The build adds the rows (asc/validate.py, vowel_default); a lect … | 10 |
| `pazeh-j-final` | Pazeh reflex of PAN *j word-finally: d (Blust 2013: 578) or t̪ (the row from Blust 1999b via Shibata 2025)? | Both rows are kept, each with its source: Blust (2013) lists Pazeh '-d only' as an exception to final devoicing; the earlier row has t̪ by final devoicing. | 1 |
| `pn-tree` | Which Polynesian tree goes in parent_id: Marck (2000), Walworth (2014) or Wilson (2021)? | Marck's (Figure 1.2, p. 3), the only one with regular sound changes at each node (Table 2.2). Walworth's tree (no Proto-Marquesic or Proto-Tahitic; 2014: 268) … |  |
| `ppn-parent` | What is the parent of Proto-Polynesian? | POc directly. Proto-Central Pacific (and Proto-Eastern Oceanic) are held back as intermediate stages, as in kayanic-held; POc > PPn rows are composed through P… | 5 |
| `pn-orthography` | How are the Polynesian glottal stop and velar nasal written? | ʔ and ŋ, in proto-languages and attested lects. Marck writes the glottal stop *q in proto-languages and ' in living languages (p. 34), the velar nasal ng, and … | 1 |
| `pto-r` | Proto-Tongic reflex of PPn *r: loss, or l (Table A.1 vs Table 2.2)? | *r > ∅ elsewhere and *r > *l between like vowels in words beginning with a stop other than *q, both regular (Table A.1, note 1, p. 237). | 2 |
| `pnp-h` | PPn *h, lost in Nuclear Polynesian except in a few words (Table 2.2 note 5). | PNP *h > ∅ regular and *h > *h sporadic; each daughter's s or h ('ø/s', 'ø/h') is entered as the reflex of that residual *h. Below PEP Table 2.2 has no *h colu… | 26 |
| `marck-diffused` | Marck's diffused changes (lexical diffusion, with residue): PCE *f > *w before *a(a)h, the Nuclear Marquesic low-vowel assimilation, the Kapingamarangi final-v… | Entered as regular with their conditions, each row noting that the change did not reach every eligible word; there is no status between regular and sporadic (S… | 8 |
| `mqa-general` | Marck's vowel rows and one sporadic row for 'Mqa (general)' (Table 3.1; Table 2.32), where Table 2.2 has Southern and Northern Marquesan. | Entered on both South and North Marquesan. | 10 |
| `mao-f` | Māori reflex of PPn *f, printed 'wh/h' with note 13, whose text ('In some place names only. Elsewhere ' (glottal stop)') fits Tubuai's *ng. | wh regular and h with conditions unknown; note 13 taken to belong to Tubuai. | 2 |
| `ren-bel` | Table 2.2 has rows Bel and Ren; Table 1.6 has only 'Ren Rennellese and Bellona'. | Ren on Rennellese (renn1242, Rennell-Bellona) and Bel on Bellona (Glottolog dialect mung1270, alternative name Mungiki). |  |
| `tok-placement` | Where does Tokelauan go? | Under Proto-Ellicean Outlier, as Table 2.2 lists it (pp. 23-24). Marck also suggests a Samoan-Tokelauan subgroup from four shared sporadic vowel changes (§5.8,… |  |
| `wilson-nodes` | How are Wilson's (2021) proto-languages entered? | As nodes under Marck's PNP and PEP, with stated-unchanged inventories where Wilson says so (PCNO-EPN, PEPND, PFEPN, PEPNP; p. 44) and assumed-unchanged for PSS… |  |
| `pns-node` | Are Proto-North Sarawak and Proto-Kenyah entered as nodes, when decision smith-higher-order holds Smith's North Sarawak back? | Yes, under PMP, from Blust (2007: 6-8), at the user's request (20 Nov 2026). Blust's PNS rests on a phonological innovation, the split of the voiced obstruents… |  |
| `blust-unconditioned` | Blust gives several reflexes of one phoneme with counts and no condition (Dobel Table 4; Chamorro final *k, 9:6). How are they entered? | The most frequent reflex is regular 'elsewhere' (or in the environment Blust gives); each other reflex attested twice or more is regular with environment 'cond… |  |
| `dobel-composed` | Blust (2014) states Dobel against PMP; Dobel is under four Grimes & Edwards (2026) nodes. How are his rows entered? | Each is restated against the Proto-Dobel-Koba phoneme the Grimes & Edwards rows give for that PMP phoneme (derivation composed, Blust's statement in as_printed… | 38 |
| `cha-k` | Chamorro k: Blust says b, d, k and r occur only in loanwords (2000: 84), but lists six native words with final *k > k (p. 94). | k entered as a native phoneme; b, d and r as marginal (loans only). | 1 |
| `cha-y` | Chamorro y: Topping's y is [dz], and Blust respells final -ai, -ao, -ui as -ay, -aw, -uy, taking [dz] and final [j] as one phoneme (2000: 85). | One phoneme d͡z (printed y); PMP *y > d͡z in all positions, final *-ay included. | 1 |
| `kiput-collapsed` | Blust (2002) derives Kiput from PNS through 36 ordered changes (Table 17, p. 420). How are they entered? | As PNS segment > Kiput segment rows, as Blust's own summary of shifts, splits and mergers does (§3.3, pp. 423-427); each row's notes name the changes that prod… |  |
| `pal-vowels` | Palauan vowel reflexes depend on pre-Palauan penultimate stress, which shifted under suffixation (Blust 2009: 310). | Entered with the set terms 'stressed syllable' (unchanged; *e > e or o) and 'unstressed syllable' (ə), and _# (lost). The stress is that of the pre-Palauan wor… |  |
| `lynch-parents` | Lynch states South Efate, Naman and Nese against POc. PNCV is in the sheet (from François 2011). What is their parent? | POc, as Lynch states them. Lynch (2000b: 321, n. 2) doubts that PNCV existed and suggests South Efate subgroups with Southern Vanuatu; the 2019 papers cite PNC… |  |
| `lynch-brackets` | How are Lynch's bracketed reflexes entered? The 2000 paper (p. 328) puts conditioned reflexes in parentheses and reflexes whose conditioning he cannot establis… | Unbracketed or first: regular, elsewhere. Conditioned: regular, with the environment from the text. Square brackets (2000) and the 2019 parentheses: regular wi… |  |
| `lynch-ipa` | Lynch writes the three languages in a practical orthography. How are the reflexes entered? | As IPA, with Lynch's symbol in source_symbol and as_printed. South Efate ᵏp, ᵑm = k͡p, ŋ͡m (labiovelars 'coarticulated with initial velar closure followed by l… |  |
| `nese-linguolabial-place` | The schema has no place 'linguolabial' for the Nese consonants d̼ ð̼ n̼. | Entered with manner and voicing but place blank, so they are listed under the chart; the notes say linguolabial. A 'linguolabial' place (between bilabial and l… |  |
| `sef-dialects` | South Efate: Lynch's data are Erakor (Thieberger); Clark (1985) reports other reflexes for Eton and Epau. | One lect, South Efate (sout2856), with Erakor as its data. Eton and Epau reflexes Lynch reports from Clark are entered as rows with variety 'Eton, Epau', sourc… |  |
| `nese-final-vowels` | Nese final syllables (Lynch 2019c: 75-78): high vowels lost and a final e or o added. How are they entered? | As loss rows for the lost vowels and two insertion rows (∅ > e, ∅ > o) at the end of the word, each with Lynch's rule (52a-c) in as_printed. Lynch argues the f… | 2 |
| `ph-no-pph` | Is there a Proto-Philippine node between PMP and the northern Philippine subgroups? | No. Proto-Batanic, Proto-Northern Luzon, Proto-Northeastern Luzon and Proto-Central Luzon are entered directly under PMP. Ross (2005: 12-15) finds no convincin… |  |
| `pb-r` | Did PMP *R become Proto-Batanic *y (Ross) or stay distinct (Yang)? | Both rows are entered on Proto-Batanic: *R > *R from Yang (2002: 37), whose Proto-Batanic keeps *R apart from *y because Yami has l for it (daRa > rala 'blood'… | 2 |
| `pb-liquids` | Yang's Proto-Batanic *l1, *l2 and *L: what are they? | Entered as the proto-phonemes l₁, l₂ and L (Yang writes l1, l2 with subscripts, Table 4-1, p. 43). Yang says PMP *l split into *l1 and *l2 (p. 47; *qulu 'head'… | 2 |
| `yang-ipa` | What IPA values do Yang's daughter symbols have? | The IPA glyphs in Yang's §3.1 are lost in the PDF, so the values follow his prose (pp. 15-17): Yami d retroflex stop ɖ, s voiceless retroflex fricative ʂ, h vo… |  |
| `yang-tree` | Yang's subgrouping inside Batanic | Not entered as nodes. Yang (2002: 65) separates Itbayat from Yami-Ivatan-Babuyan (*q > h, loss of *h) and Yami from Ivatan-Babuyan (*l1 > d, *r > l) but recons… |  |
| `neluz-parent` | Where does Proto-Northeastern Luzon attach? | Under PMP, with Proto-Northern Luzon as an alternative parent. Robinson & Lobel argue that Northeastern Luzon is a primary branch of Northern Luzon, not part o… |  |
| `neluz-internal` | Robinson & Lobel's internal tree of Northeastern Luzon | Not entered as nodes. They make Dupaningan Agta a primary branch, group Casiguran with Nagtipunan ('very closely related, if not dialects of a single language'… |  |
| `neluz-gemination` | Gemination after schwa in Northeastern Luzon | Not entered as correspondence rows: it is a change in consonant length after ə, not in any phoneme. Recorded in the notes of Proto-Northeastern Luzon and each … |  |
| `himes-apicals` | Himes's (2) lists *j > d, *d > l / V[-back]_V and *z > d for Proto-Central Luzon, but his inventory (3) keeps *z and *j. Where do these changes go? | On the branches. (3) keeps *d, *z and *j apart, and §§2.4.4, 2.5.2, 2.5.5 and 2.6.6-2.6.8 describe the merger of *j and *z with *d, and the lenition of intervo… | 32 |
| `himes-r-y` | Himes's Sinauna, Kapampangan and Sambalic rules for *R, after Proto-Central Luzon *R > *y | Entered on Proto-Central Luzon *y, with a note that they apply only to *y from PMP *R; as_printed keeps Himes's *R. Himes states them for *R (§§2.4.1, 2.5.1, 2… | 6 |
| `himes-nodes` | Which Central Luzon nodes are entered? | Proto-Central Luzon with three equidistant branches, Sinauna, Kapampangan and Proto-Sambalic, as Himes concludes (p. 527). His Proto-Sambal-Sinauna (p. 510) is… |  |

<!-- END GENERATED -->

## Not yet entered

Hand-kept. Collected from the handoffs of 2026-11-20 (09:20 to 15:00). The Google Doc "ASC to-do list" could not be read when this was written ("Permission denied"), so items that are only there still need adding here.

- Zobel 2020: the appendix of PKW reconstructions; the languages outside his Table 18 (Rai, Kamaru, Kalao). Lindu, Sedoa and Topoiyo are entered from prose only.
- Smith 2017a (Borneo): batch `smith2017-borneo` has Kayan, Murik-Merap, Segai-Modang, Kajang, Melanau, Punan, Müller-Schwaner, Land Dayak and Malayic (see its BATCH.md for what was left out). Proto-Kayanic and Proto-Kayan-Murik-Merap are held back as intermediate stages (`kayanic-held`), and Proto-Malayic has no changes of its own (`pmal-shared`), by the user's rule of 20 Nov: correspondence tables and established microgroups yes, intermediate reconstructions above them not yet. Still to enter: §2.7 Barito (a linkage, no node), §2.9 Basap, §2.10 Sabah (Northeast Sabah, Molbog; Dusunic from Lobel), §2.11 Dayic, Berawan-Lower Baram, Bintulu (Kenyah has no table). The scripts are in `tools/batch_scripts/smith2017/`.
- Lobel 2013: nothing entered. Proto-Subanen (ch. 10) is stated against Proto-Greater Central Philippine and Southwest Sabah (ch. 11) against Proto-Southwest Sabah; neither node is in the database. Also Manide and Inagta Alabat (ch. 8).
- Grimes & Edwards 2026: only the classification trees are entered (Banda from summary (19), p. 505). The chapter tables (cognate sets) and the prose are not. Kept in lect notes, not as rows: *ma-p/*map, insertions (∅ > C, y-insertion, prothesis), metathesis (SW Maluku), whole-class rules (*C > ∅ /_#, *V > ∅ /_#), and changes whose input the tree never provides (Timaus **ʤ/**gʷ, East Nage **ʤ, Kei **d). The insertions could now be rows (parent `∅`).
- Bender et al. 2003a beyond p. 9 (the dictionary), and part 2 (2003b).
- Kosraean (Lee & Wang 1984): POC *q > ∅, *R > ∅, final-consonant loss; *a-raising, high-vowel lowering, low-vowel dissimilation and monophthongisation (weak evidence in the source; see batch `leewang1984-kosraean`). No reflexes for the ɻ series and the glides. Bender's Kosraean vowel respelling (Table 1) is only in the orthography note.
- Blust 2013: ch. 8, pp. 553-593, read directly (excerpt in Downloads/austdic). Batch `blust2013-reinforce` adds it as a second source for PMP > POc and for the PAN *j, *h and *R reflexes of the Formosan languages under PAN. Not entered: the PMP > POc cluster fusions (Ross's pairs are in), and the reflexes of languages below intermediate nodes (Tables 8.27, 8.30).
- Polynesian (batch `marck2000-polynesian`): Marck 2000 is entered from Tables 2.2, 3.1, 2.32 and 3.30 and Table A.1; Walworth 2014 and Wilson 2021 as alt_parents, plus Wilson's single-word changes. Not entered: Marck's Appendix B and Tables 3.15-3.29 (lexeme-level vowel changes); Table 2.2 "Pla" (undefined); vowel loss between identical consonants (Table 2.2 note 9); Wilson's PEPNP(N); Wilson 2012. PPn sits directly under POc (decision `ppn-parent`), so most POc phonemes are unentered for PPn.
- Blust's historical phonologies (batch `blust-histphon`): Chamorro (2000) and Palauan (2009) under PMP; Kiput (2002) and Òma Lóngh (2007) under the new Proto-North Sarawak and Proto-Kenyah nodes (decision `pns-node`); Dobel (2014) composed against the Grimes & Edwards Aru nodes (`dobel-composed`). Not entered: the irregular and loan forms each paper lists, Kiput's PMP > PNS changes (§3.1) and prenasalized stops, Dobel's diphthongs and *q > ʔ, the Chamorro and Palauan loanword strata (see the batch's BATCH.md). Berawan-Lower Baram, Lower Baram and Highland Kenyah are not nodes: Kiput and Òma Lóngh sit directly under PNS and PK. Smith's §2.11 (Berawan-Lower Baram, Bintulu) could now go under PNS.
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
