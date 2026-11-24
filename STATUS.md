# ASC status

The state of the Austronesian Sound Correspondences database. The generated part is rewritten by the build (`python3 build.py --check --status STATUS.md`), which the hourly sync and the batch workflow run; the sections after it are kept by hand. This file replaces the appended handoffs and the Google to-do doc.

<!-- BEGIN GENERATED: python3 build.py --check --status STATUS.md; do not edit by hand -->

## Data

| Table | Rows | |
|---|---|---|
| sources | 253 |  |
| lects | 1027 | 255 dialect, 33 earlier-stage, 3 group, 455 language, 6 linkage, 275 proto-language |
| phonemes | 4498 |  |
| correspondences | 12074 | plus 11850 implied and 3374 stated retentions generated from lects.inherit |
| notation_map | 557 |  |
| allophones | 979 |  |
| decisions | 185 | 91 confirmed, 59 open, 35 reverted |

Lects by `inherit`: (blank) 172, assumed-unchanged 569, assumed-unchanged (automatic, fewer than 13 phonemes known) 47, stated-unchanged 239.
Inventories: edited 28, empty 19, reverse-generated 798, sourced 182.

## Checks

`build.py --check`: 0 error(s), 297 warning(s), 1109 note(s).

| Warnings | Count |
|---|---|
| no glottocode | 136 |
| a work cited in notes has no sources row | 74 |
| a source is never cited | 52 |
| a reflex is not in the lect's sourced inventory | 25 |
| repeats the fusion row at … | 6 |
| an attested lect has symbols that are not IPA | 4 |

## Open decisions

From the `decisions` tab. Confirm or revert one by changing its `status` in the sheet.

| id | Question | Reading taken | Rows | Comments |
|---|---|---|---|---|
| `pkmm-glottal` | Where do the added final glottal stop and the lowering of final high vowels belong? | Shared by Kayan and Murik-Merap (section 2.2.4.1, p. 84), as Smith concludes, not Kayan alone as Figure 10 (p. 54) has it; entered on both Proto-Kayan and Prot… | 6 |  |
| `kajang-hiatus` | Kajang reflexes of penultimate *u and *i before *a (Table 25: *-uCVC gʷ / _a; *-iCVC ʑ / _a). | Entered at Proto-Kajang as *u > *ɡʷ, *i > *ʑ before *a: the strengthened transition glide (p. 95: *dua > dəgʷa). |  |  |
| `punan-internal` | Punan internal subgrouping (Figures 28-29, pp. 122-124). | No lower nodes: Punan Tubu-Bah (*a > *ə / _Ca(C)#, *z > *c) conflicts with the backing of final *ə shared by Punan Tubu, Bah, Aput and Beketan (pp. 120-122). T… |  |  |
| `pld-l` | Land Dayak *l > *r: Hliboi and Sungkung have l (Table 50). | *l > *r at Proto-Land Dayak, as Smith reads it (p. 142); the two languages are entered with r > l. | 1 |  |
| `landdayak-tables` | Land Dayak Tables 50-51 (pp. 141-142). | Consonant cells with '?', Bidayuh's column ('Bid', variety not named) and the optional prenasalization '(n)t' are left out; vowels are entered from the summary… |  |  |
| `malayic-glottal` | Malayic cells such as 'aʔ; a', 'u; (uʔ)', 'r; ʔ' (Tables 59-60): Smith ties final glottal stops to particular lexemes (Figures 60-61, p. 196). | The glottal stop after final vowels is entered as a sporadic inserted ʔ; the vowel itself as unchanged. | 5 |  |
| `malayic-phonetic` | Table 60 prints some vowels phonetically: Seberuang ow, ey; Iban ʊu̯, ɪi̯, ʊə̯, ɪə̯; Mualang oə̯, ɛə̯. The text calls these allophonic (pp. 185-186: /kutu/ [ku… | Entered as the phonemes: u, i (Seberuang, Iban), o, e (Mualang closed syllables). |  |  |
| `malayic-r` | Malayic *R: Tables 59 prints ɣ (Keninjal, Seberuang, Mualang) and ɹˠ (Seberuang, final), but Figure 56 (p. 185) gives these as phonetic values of /r/. | Entered as r for all seven lects (phonemic). |  |  |
| `kayanic-held` | Kayanic and Kayan-Murik-Merap: intermediate stages above the microgroups Kayan, Murik-Merap and Segai-Modang. | Held back, by the rule to add correspondence tables and the reconstructions of established microgroups but to hold the intermediate stages above them. Proto-Ka… |  |  |
| `pazeh-j-final` | Pazeh reflex of PAN *j word-finally: d (Blust 2013: 578) or t̪ (the row from Blust 1999b via Shibata 2025)? | Both rows are kept, each with its source: Blust (2013) lists Pazeh '-d only' as an exception to final devoicing; the earlier row has t̪ by final devoicing. | 1 |  |
| `ppn-parent` | What is the parent of Proto-Polynesian? | Proto-Central Pacific, since 23 November 2026 (decision geraghty1986-ppn, reverted by the user), with Geraghty's (1986) PCP > PPn rows. Before: POc directly. P… |  |  |
| `pn-orthography` | How are the Polynesian glottal stop and velar nasal written? | ʔ and ŋ, in proto-languages and attested lects. Marck writes the glottal stop *q in proto-languages and ' in living languages (p. 34), the velar nasal ng, and … | 1 |  |
| `pto-r` | Proto-Tongic reflex of PPn *r: loss, or l (Table A.1 vs Table 2.2)? | *r > ∅ elsewhere and *r > *l between like vowels in words beginning with a stop other than *q, both regular (Table A.1, note 1, p. 237). | 2 |  |
| `pnp-h` | PPn *h, lost in Nuclear Polynesian except in a few words (Table 2.2 note 5). | PNP *h > ∅ regular and *h > *h sporadic; each daughter's s or h ('ø/s', 'ø/h') is entered as the reflex of that residual *h. Below PEP Table 2.2 has no *h colu… | 31 |  |
| `marck-diffused` | Marck's diffused changes (lexical diffusion, with residue): PCE *f > *w before *a(a)h, the Nuclear Marquesic low-vowel assimilation, the Kapingamarangi final-v… | Entered as regular with their conditions, each row noting that the change did not reach every eligible word; there is no status between regular and sporadic (S… | 12 |  |
| `mqa-general` | Marck's vowel rows and one sporadic row for 'Mqa (general)' (Table 3.1; Table 2.32), where Table 2.2 has Southern and Northern Marquesan. | Entered on both South and North Marquesan. | 10 |  |
| `mao-f` | Māori reflex of PPn *f, printed 'wh/h' with note 13, whose text ('In some place names only. Elsewhere ' (glottal stop)') fits Tubuai's *ng. | wh regular and h with conditions unknown; note 13 taken to belong to Tubuai. | 2 |  |
| `ren-bel` | Table 2.2 has rows Bel and Ren; Table 1.6 has only 'Ren Rennellese and Bellona'. | Ren on Rennellese (renn1242, Rennell-Bellona) and Bel on Bellona (Glottolog dialect mung1270, alternative name Mungiki). |  |  |
| `lynch-parents` | Lynch states South Efate, Naman and Nese against POc. PNCV is in the sheet (from François 2011). What is their parent? | POc, as Lynch states them. Lynch (2000b: 321, n. 2) doubts that PNCV existed and suggests South Efate subgroups with Southern Vanuatu; the 2019 papers cite PNC… |  |  |
| `lynch-brackets` | How are Lynch's bracketed reflexes entered? The 2000 paper (p. 328) puts conditioned reflexes in parentheses and reflexes whose conditioning he cannot establis… | Unbracketed or first: regular, elsewhere. Conditioned: regular, with the environment from the text. Square brackets (2000) and the 2019 parentheses: regular wi… |  |  |
| `lynch-ipa` | Lynch writes the three languages in a practical orthography. How are the reflexes entered? | As IPA, with Lynch's symbol in source_symbol and as_printed. South Efate ᵏp, ᵑm = k͡p, ŋ͡m (labiovelars 'coarticulated with initial velar closure followed by l… |  |  |
| `sef-dialects` | South Efate: Lynch's data are Erakor (Thieberger); Clark (1985) reports other reflexes for Eton and Epau. | One lect, South Efate (sout2856), with Erakor as its data. Eton and Epau reflexes Lynch reports from Clark are entered as rows with variety 'Eton, Epau', sourc… |  |  |
| `nese-final-vowels` | Nese final syllables (Lynch 2019c: 75-78): high vowels lost and a final e or o added. How are they entered? | As loss rows for the lost vowels and two insertion rows (∅ > e, ∅ > o) at the end of the word, each with Lynch's rule (52a-c) in as_printed. Lynch argues the f… | 2 |  |
| `pb-r` | Did PMP *R become Proto-Batanic *y (Ross) or stay distinct (Yang)? | Both rows are entered on Proto-Batanic: *R > *R from Yang (2002: 37), whose Proto-Batanic keeps *R apart from *y because Yami has l for it (daRa > rala 'blood'… | 2 |  |
| `pb-liquids` | Yang's Proto-Batanic *l1, *l2 and *L: what are they? | Entered as the proto-phonemes l₁, l₂ and L (Yang writes l1, l2 with subscripts, Table 4-1, p. 43). Yang says PMP *l split into *l1 and *l2 (p. 47; *qulu 'head'… | 2 |  |
| `yang-ipa` | What IPA values do Yang's daughter symbols have? | The IPA glyphs in Yang's §3.1 are lost in the PDF, so the values follow his prose (pp. 15-17): Yami d retroflex stop ɖ, s voiceless retroflex fricative ʂ, h vo… |  |  |
| `yang-tree` | Yang's subgrouping inside Batanic | Not entered as nodes. Yang (2002: 65) separates Itbayat from Yami-Ivatan-Babuyan (*q > h, loss of *h) and Yami from Ivatan-Babuyan (*l1 > d, *r > l) but recons… |  |  |
| `neluz-parent` | Where does Proto-Northeastern Luzon attach? | Under PMP, with Proto-Northern Luzon as an alternative parent. Robinson & Lobel argue that Northeastern Luzon is a primary branch of Northern Luzon, not part o… |  |  |
| `neluz-internal` | Robinson & Lobel's internal tree of Northeastern Luzon | Not entered as nodes. They make Dupaningan Agta a primary branch, group Casiguran with Nagtipunan ('very closely related, if not dialects of a single language'… |  |  |
| `neluz-gemination` | Gemination after schwa in Northeastern Luzon | Not entered as correspondence rows: it is a change in consonant length after ə, not in any phoneme. Recorded in the notes of Proto-Northeastern Luzon and each … |  |  |
| `himes-apicals` | Himes's (2) lists *j > d, *d > l / V[-back]_V and *z > d for Proto-Central Luzon, but his inventory (3) keeps *z and *j. Where do these changes go? | On the branches. (3) keeps *d, *z and *j apart, and §§2.4.4, 2.5.2, 2.5.5 and 2.6.6-2.6.8 describe the merger of *j and *z with *d, and the lenition of intervo… | 32 |  |
| `himes-r-y` | Himes's Sinauna, Kapampangan and Sambalic rules for *R, after Proto-Central Luzon *R > *y | Entered on Proto-Central Luzon *y, with a note that they apply only to *y from PMP *R; as_printed keeps Himes's *R. Himes states them for *R (§§2.4.1, 2.5.1, 2… | 6 |  |
| `atayalic-node` | Goderich (2020: Tables 4.41, 4.46) gives Proto-Atayalic (Li 1981) between PAn and Proto-Atayal, with two changes from Proto-Atayalic to Proto-Atayal (*r > *ɹ, … | Not entered: pata and psed stay under PAN, and PAn > Proto-Atayal rows are stated directly. |  |  |
| `atayal-nodes` | Goderich's subgroup nodes (Proto-Northern, Proto-Nuclear Northern, Proto-Southern, Proto-Nuclear Southern and Proto-Southwestern Atayal; ch. 6): where do the d… | Each change is entered at the node to which ch. 6 assigns it (Tables 6.1-6.15), and only the rest on the dialects. Exception: the affrication of *t, which ch. … |  |  |
| `siraya-ipa` | Adelaar's Gospel (G) and Utrecht Manuscript (UM) symbols x, D, v, e, o, ʔ and the uncertain c, nḡ, z: how are they entered? | x as ʝ, the voiced palatal fricative of Adelaar (2014: 4 n. 2), not the velar of Adelaar (2011: 52); D kept as D (a root-initial phoneme realised d or r, with … |  |  |
| `puyuma-ting` | Ting's (1978) Puyuma tree (via Teng 2008: 5): Nanwang against a subgroup of the other five, which further divides into Pinaski-Ulivelivek, Rikavung and Kasavak… | No: Ting's statements are entered on each dialect under Yeh's Proto-Puyuma (ppuy), marked composed. The five non-Nanwang varieties have no glottocodes (Glottol… |  |  |
| `tsou-tfuya` | Tfuya Tsou (Zeitoun 2005b) and Teruku Seediq (Tsukida 2005) give inventories only. Enter them as lects? | Entered as dialects with inventories and no correspondences: tfue1237 under PAn (language_id tsou1248; the existing Tsou lect is Tsuchida’s Duhtu), teru1237 un… |  |  |
| `maga-li-vowels` | Maga mid vowels (Li 1977, via Hsin 2000): PR *ay, *ai > e; *aw, *au > o; *i, *u > e, o after a lost *a. | Entered as fusion pairs and conditioned rows against Proto-Rukai. Hsin himself derives e and o synchronically (p. 80). | 12 |  |
| `lin-amis` | Lin (2022) read directly. Shibata’s Proto-Amis (pami) is Lin’s Proto-Amis-Sakizaya; Lin’s subgroups are entered as nodes under it. | pami renamed Proto-Amis-Sakizaya, with Lin’s values *z (fricative) and *d (stop) in place of Shibata’s d and ɮ (Shibata’s values in the notes). New nodes: Prot… |  |  |
| `tseng-nef` | Tseng (2022) read directly: Proto-Northeast Formosan (Glottolog’s Northern East Formosan) entered under Proto-East Formosan, with Proto-Kavalan and Proto-Basay… | Older PAn-level rows of Kavalan, Basay and Ketagalan (Li & Tsuchida 2006, Shibata 2025, Blust 2013, Ogawa 1931) restated against the new parents through Tseng’… |  |  |
| `song-seediq` | Song (2025) reconstructs Proto-Seediq from five dialects, with an inventory that differs from Shibata’s (2025) Proto-Seediq (psed): *c, *x, *h and fricative *g… | Song’s inventory entered as the reconstruction system “Song” of psed (notation_map), and the five dialects stated against it (correspondences with system Song)… |  |  |
| `li-reprints` | Li’s papers read in his Selected papers (2004): which work and pages are cited? | The original paper is the source (li1977, li1981, li1988, li2003, li2004, li1979); its sources row says it was read in the reprint, and pages are the reprint’s. |  |  |
| `shibata-pb` | Shibata’s (2020) PAN > Proto-Bunun rows beside Li’s (1988): how? | Entered as separate rows on pbun. His *b, *d are Li’s ʔb, ʔd (source_form b, d). PAN *b, *d > *ʔ word-finally are regular rows, with his doubt about *b (p. 73)… | 6 |  |
| `lobel-subanen` | Subanen internal nodes (Figure 10.1)? | Proto-Subanen with Lobel's inventory (Table 10.3) under pgcph. Nodes Western Subanen (west2811), Nuclear Subanen (nucl1726) and East Nuclear Subanen (east2769)… | 4 |  |
| `lobel-manide` | Manide and Inagta Alabat: where, and which reflexes? | Node Proto-Manide-Alabat (alab1255, the two languages only) directly under PMP: Lobel takes it as a primary branch of the Philippine macrogroup and there is no… |  |  |
| `lrc2002-readings` | Symbols in the Lynch et al. (2002) sketches whose IPA value is not stated or is ambiguous. | j (a voiced palatal stop or affricate, value not stated) entered as ɟ in Sudest, Teanu (Buma) and Xârâcùù, and ⁿj as ᶮɟ; Tobati /~/ (a nasalisation phoneme in … |  |  |
| `lrc2002-nadroga` | Nadrogā: the sketch says that historically *t became /s/ before /i e/ and /tʃ/ before /u/, *ⁿd became /ⁿdʒ/ before /i u/, and *s became /h/, without naming the… | Entered against Proto-Oceanic (the parent in this database), with a row for each statement; no elsewhere rows for *t and *d. | 4 |  |
| `lrc2002-subgroups` | Ch. 5 names subgroup-defining sound changes: Proto Admiralties *R > *y before high vowels, lost elsewhere (p. 99); Southeast Solomonic merger of POc *l and *R … | Not entered: no Proto-Admiralties, Proto-Southeast Solomonic or Proto-Papuan Tip node was added, and the sketch languages are placed directly under POc (Southe… |  |  |
| `shwng-k` | PMP *k > ∅ (change 9) was probably not complete in PSHWNG: *k survives as k in some words, especially in South Halmahera and Moor. | Two rows: *k > ∅ regular, and *k > k sporadic with conditions unknown. | 2 |  |
| `blust1984-grades` | Blust (1984) lists several reflexes of POc *p, *k, *nt, *s and *ns in Mussau and then treats the minority ones as consonant-grade 'cross-over' (pp. 179-180). H… | The oral-grade reflex of Table 3 as regular; each cross-over reflex as regular with conditioning 'lexical' and lexical_scope naming the cross-over etyma (p > p… | 6 |  |
| `francois2005-hybridization` | How are François's (2005) charts of vowel hybridization (Appendix 1, pp. 490-491) entered? | As PNCV > language rows (the 17 Torres and Banks languages and Sakao already sit under PNCV), with five implied PNCV retentions of the POc vowels, since Franço… | 672 |  |
| `ho1982-composition` | Ozanne-Rivierre's Table 3.3.4 (Haudricourt & Ozanne-Rivierre 1982: 54-55) gives POc > 'langues de Hienghène' for all four languages at once, naming a language … | One row per language (Pije, Fwâi, Nemi, Jawe), composed POc > PNC > language with the printed cell in as_printed; a cell without a language label applies to al… | 229 |  |
| `jackson1983-table18` | How are the rules of Jackson's (1983: 226) Table 18 entered? | As PCK > language rows, one per rule and language, with the rule as printed in as_printed and Jackson's PTK *p', *m', *g mapped to PCK *pʷ, *mʷ, *ŋ. Marks: XX … |  |  |
| `jackson1983-tree` | Jackson's Figure 4 (p. 231) is a Trukic tree with five unnamed intermediate nodes defined by the rules of Table 18 (ULI first; then PUA; then WOL; then CRL-STW… | Not entered: all eight languages stay directly under PCK, as in Bender et al. (2003a), whose Figure 1 (adapted from Jackson) is also not entered as nodes. Jack… |  |  |
| `ross1996-strata` | Ross (1996) assigns Yapese vocabulary to five strata: Sets A and B (non-Oceanic, stated against PMP), Set C (inherited, POc), Sets D and UW (Nuclear Micronesia… | Set C only, as POc > Yapese rows with stratum 'Set C (inherited)', Yapese under POc. Sets A, B, D and UW are described in the lect notes, not entered: A and B … |  |  |
| `ross1996-symbols` | Ross transcribes Yapese in a comparative orthography (n. 3). What are c, y and the superscript glottal stop? | c kept as c (the Yapese ch affricate; Ross gives no phonetic value, so it is not turned into an IPA affricate); y = j; fˀ, vˀ as printed (glottalised); Ross's … | 1 |  |
| `barlowross2025-table1` | Table 1 (p. 332) prints the final-vowel header as -a -e -e -i -u. | Read as -a -e -i -o -u: the cells match Table 2 that way (*aCi > a, e, i; *aCo > a, o; *iCo > u). |  |  |
| `lynch2002h-table3` | Lynch (2002h) Table 3 gives sample reflexes of the POc labials and labiovelars in eleven languages. Which are entered? | None for now. Mota, the one column not yet covered, cannot be restated against PNCV, whose inventory in the data has no labials (PNCV has neither consonant row… |  |  |
| `lynch2004-q` | Lynch (2004) lists sporadic overt reflexes of POc *q in Southern Vanuatu (Table 6) and occasional reflexes of *R in Vanuatu (Table 8). How are they entered? | As sporadic rows on the languages, with the parent phoneme of the lect's own parent (*q and *R are kept in PSV, Proto-Erromango, Proto-Tanna and PNCV in the da… |  |  |

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
- Competing reconstructions (`competes_with`) are handled by the site, but no lect uses the column yet.

## Housekeeping

- "TEMP import" 1-12 in Google Drive can be deleted.
- Branches `layout-v2-phase1`, `batches-to-sheet`, `e2e-batch-test`, `push-batch-fix`, `phase3-inherit-decisions` can be deleted on GitHub.
