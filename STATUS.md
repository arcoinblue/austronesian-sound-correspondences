# ASC status

The state of the Austronesian Sound Correspondences database. The generated part is rewritten by the build (`python3 build.py --check --status STATUS.md`), which the hourly sync and the batch workflow run; the sections after it are kept by hand. This file replaces the appended handoffs and the Google to-do doc.

<!-- BEGIN GENERATED: python3 build.py --check --status STATUS.md; do not edit by hand -->

## Data

| Table | Rows | |
|---|---|---|
| sources | 165 |  |
| lects | 881 | 235 dialect, 33 earlier-stage, 376 language, 237 proto-language |
| phonemes | 2910 |  |
| correspondences | 9183 | plus 10127 implied and 3432 stated retentions generated from lects.inherit |
| notation_map | 514 |  |
| decisions | 127 | 19 confirmed, 102 open, 6 reverted |

Lects by `inherit`: (blank) 137, assumed-unchanged 505, stated-unchanged 239.
Inventories: edited 24, reverse-generated 735, sourced 122.

## Checks

`build.py --check`: 0 error(s), 277 warning(s), 840 note(s).

| Warnings | Count |
|---|---|
| no glottocode | 139 |
| a work cited in notes has no sources row | 66 |
| a source is never cited | 43 |
| a reflex is not in the lect's sourced inventory | 15 |
| an attested lect has symbols that are not IPA | 8 |
| repeats the fusion row at … | 6 |

## Open decisions

From the `decisions` tab. Confirm or revert one by changing its `status` in the sheet.

| id | Question | Reading taken | Rows |
|---|---|---|---|
| `kw-branches-unchanged` | Zobel's Table 18 has no column for the Northern and Southern Kaili–Wolio branches. What do their consonants continue? | Unchanged from PKW unless Zobel says otherwise; each such row says so and cites the PSKW/PNKW reconstructions of the appendix. | 32 |
| `ledo-subgroup` | Where does Ledo go? Zobel calls it mixed; Glottolog puts it in the Northern branch. | Under Southern Kaili–Wolio (its dominant lexical stratum). |  |
| `atayal-original` | Which work is the original of the Proto-Atayal reconstruction? | Goderich (2020) only. |  |
| `lynch-biggs-ids` | Are the Lynch (2022) and Biggs (1965) works the ones the citing sources mean? | As entered in sources. |  |
| `kanakanavu-d` | Kanakanavu *d > sʲ word-initially: the table has s-(?); the text says *d is regularly r. | Entered, marked disputed. | 1 |
| `wolff-vowels` | The Wolff system has no vowel rows: Shibata's Table 2.16 has none. | Consonants only; the site says Wolff's vowels are not compared. |  |
| `ge-earlier-stage` | Tree nodes printed as one language with an ISO code, whose members are its varieties. | Entered as earlier-stage Pre-X (Pre-Tetun, Pre-Mambae, Pre-Kei, ...). |  |
| `ge-overlap` | Overlapping subgroups (Wetar-Galolen, Nuclear Wetar-Atauro; the Peripheral Babar shared changes). | Entered on the member lects (overlap_groups). |  |
| `ge-appendix-codes` | Corrections to appendix A codes: So'a soaa1237 → cent2074; Lamalera lama1278 → lama1299 (lama1278 goes to the Peripheral Lembata node); Semau Helong without a … | As listed. |  |
| `ge-uncertain` | Hukumina and Salas ("classification uncertain"). | Under PMP. |  |
| `ge-identity-conflicts` | Four identity rows were added at a node because a daughter states a change from that phoneme, but the node itself states a change for it: Proto-Nuclear Rote *d… | Both kept: the stated change and the identity, as two elsewhere reflexes. | 5 |
| `pocr-parents` | Parents of PNCV, PNC and the Vanikoro languages (Teanu, Lovono, Tanema). | Directly under POc (PEOc, Proto-Southern Oceanic and a Temotu node are not entered). |  |
| `bm-stated-unchanged` | Billings & McDonnell tabulate only the nontrivial correspondence sets (Tables 3, 5, 7, 10; Appendix G). Is a phoneme they do not list stated to be unchanged, o… | Stated: the 17 lects have inherit = stated-unchanged, and their generated rows are shown as stated ("unchanged per source"). |  |
| `smith-semicolon` | Smith's tables list several reflexes in a cell: 'the first listed reflex is the regular reflex, and the reflex(es) appearing after the semi-colon are condition… | First reflex: regular. After a semicolon: sporadic, unless the text states a condition (then regular with that environment). After a comma: regular, conditions… | 396 |
| `smith-higher-order` | Smith's higher-order groupings: North Borneo, Greater North Borneo, Central Sarawak, Punan-Müller-Schwaner, North Sarawak, Basap-Barito, Western Indonesian (20… | Not entered as nodes. They rest mainly on lexical innovations, which Smith himself later rejects as subgrouping evidence for Greater North Borneo and Barito-Ba… |  |
| `kayanic-glottocodes` | Glottocodes for Smith's Kayanic varieties. | Long Naah = Baram Kayan bara1370; Data Dian = Kayan River Kayan kaya1325 (Glottolog alt name); Balui Liko = Rejang Kayan reja1241; Gaai = Segai sega1243 (langu… |  |
| `ngorek-nj` | Ngorek reflex of *nj: Table 8 (p. 64) has nc, Table 11 (p. 67) nj. | Not entered. |  |
| `psm-j` | Proto-Segai-Modang reflex of Proto-Kayanic *j (PMP *z- and *nz). | *j > *c, inferred from Table 14: it shares the reflexes of medial *c, while *-y- > j stays apart. | 1 |
| `pkay-table23` | Proto-Kayanic (Table 23, p. 86): rows Smith prints with a question mark or hedges in the text. | *q- entered as a disputed blank (printed Ø?); *-z- > *c entered as disputed (the text says only that it 'may' be Proto-Kayanic, p. 58); *R- > *h entered as pri… | 8 |
| `pkmm-glottal` | Where do the added final glottal stop and the lowering of final high vowels belong? | Shared by Kayan and Murik-Merap (section 2.2.4.1, p. 84), as Smith concludes, not Kayan alone as Figure 10 (p. 54) has it; entered on both Proto-Kayan and Prot… | 6 |
| `kajang-hiatus` | Kajang reflexes of penultimate *u and *i before *a (Table 25: *-uCVC gʷ / _a; *-iCVC ʑ / _a). | Entered at Proto-Kajang as *u > *ɡʷ, *i > *ʑ before *a: the strengthened transition glide (p. 95: *dua > dəgʷa). |  |
| `punan-internal` | Punan internal subgrouping (Figures 28-29, pp. 122-124). | No lower nodes: Punan Tubu-Bah (*a > *ə / _Ca(C)#, *z > *c) conflicts with the backing of final *ə shared by Punan Tubu, Bah, Aput and Beketan (pp. 120-122). T… |  |
| `pld-l` | Land Dayak *l > *r: Hliboi and Sungkung have l (Table 50). | *l > *r at Proto-Land Dayak, as Smith reads it (p. 142); the two languages are entered with r > l. | 1 |
| `landdayak-tables` | Land Dayak Tables 50-51 (pp. 141-142). | Consonant cells with '?', Bidayuh's column ('Bid', variety not named) and the optional prenasalization '(n)t' are left out; vowels are entered from the summary… |  |
| `pmal-shared` | Proto-Malayic changes: Smith gives none. | No Proto-Malayic rows; every change is entered on each lect. The reflexes shared by all seven lects of Tables 59-60 (*-q > h, *-b > p, *-d, *-j > t, *-j- > d, … |  |
| `malayic-glottal` | Malayic cells such as 'aʔ; a', 'u; (uʔ)', 'r; ʔ' (Tables 59-60): Smith ties final glottal stops to particular lexemes (Figures 60-61, p. 196). | The glottal stop after final vowels is entered as a sporadic inserted ʔ; the vowel itself as unchanged. | 5 |
| `malayic-phonetic` | Table 60 prints some vowels phonetically: Seberuang ow, ey; Iban ʊu̯, ɪi̯, ʊə̯, ɪə̯; Mualang oə̯, ɛə̯. The text calls these allophonic (pp. 185-186: /kutu/ [ku… | Entered as the phonemes: u, i (Seberuang, Iban), o, e (Mualang closed syllables). |  |
| `malayic-r` | Malayic *R: Tables 59 prints ɣ (Keninjal, Seberuang, Mualang) and ɹˠ (Seberuang, final), but Figure 56 (p. 185) gives these as phonetic values of /r/. | Entered as r for all seven lects (phonemic). |  |
| `kayanic-held` | Kayanic and Kayan-Murik-Merap: intermediate stages above the microgroups Kayan, Murik-Merap and Segai-Modang. | Held back, by the rule to add correspondence tables and the reconstructions of established microgroups but to hold the intermediate stages above them. Proto-Ka… |  |
| `pazeh-j-final` | Pazeh reflex of PAN *j word-finally: d (Blust 2013: 578) or t̪ (the row from Blust 1999b via Shibata 2025)? | Both rows are kept, each with its source: Blust (2013) lists Pazeh '-d only' as an exception to final devoicing; the earlier row has t̪ by final devoicing. | 1 |
| `ppn-parent` | What is the parent of Proto-Polynesian? | POc directly. Proto-Central Pacific (and Proto-Eastern Oceanic) are held back as intermediate stages, as in kayanic-held; POc > PPn rows are composed through P… | 5 |
| `pn-orthography` | How are the Polynesian glottal stop and velar nasal written? | ʔ and ŋ, in proto-languages and attested lects. Marck writes the glottal stop *q in proto-languages and ' in living languages (p. 34), the velar nasal ng, and … | 1 |
| `pto-r` | Proto-Tongic reflex of PPn *r: loss, or l (Table A.1 vs Table 2.2)? | *r > ∅ elsewhere and *r > *l between like vowels in words beginning with a stop other than *q, both regular (Table A.1, note 1, p. 237). | 2 |
| `pnp-h` | PPn *h, lost in Nuclear Polynesian except in a few words (Table 2.2 note 5). | PNP *h > ∅ regular and *h > *h sporadic; each daughter's s or h ('ø/s', 'ø/h') is entered as the reflex of that residual *h. Below PEP Table 2.2 has no *h colu… | 26 |
| `marck-diffused` | Marck's diffused changes (lexical diffusion, with residue): PCE *f > *w before *a(a)h, the Nuclear Marquesic low-vowel assimilation, the Kapingamarangi final-v… | Entered as regular with their conditions, each row noting that the change did not reach every eligible word; there is no status between regular and sporadic (S… | 8 |
| `mqa-general` | Marck's vowel rows and one sporadic row for 'Mqa (general)' (Table 3.1; Table 2.32), where Table 2.2 has Southern and Northern Marquesan. | Entered on both South and North Marquesan. | 10 |
| `mao-f` | Māori reflex of PPn *f, printed 'wh/h' with note 13, whose text ('In some place names only. Elsewhere ' (glottal stop)') fits Tubuai's *ng. | wh regular and h with conditions unknown; note 13 taken to belong to Tubuai. | 2 |
| `ren-bel` | Table 2.2 has rows Bel and Ren; Table 1.6 has only 'Ren Rennellese and Bellona'. | Ren on Rennellese (renn1242, Rennell-Bellona) and Bel on Bellona (Glottolog dialect mung1270, alternative name Mungiki). |  |
| `pns-node` | Are Proto-North Sarawak and Proto-Kenyah entered as nodes, when decision smith-higher-order holds Smith's North Sarawak back? | Yes, under PMP, from Blust (2007: 6-8), at the user's request (20 Nov 2026). Blust's PNS rests on a phonological innovation, the split of the voiced obstruents… |  |
| `blust-unconditioned` | Blust gives several reflexes of one phoneme with counts and no condition (Dobel Table 4; Chamorro final *k, 9:6). How are they entered? | The most frequent reflex is regular 'elsewhere' (or in the environment Blust gives); each other reflex attested twice or more is regular with environment 'cond… |  |
| `cha-k` | Chamorro k: Blust says b, d, k and r occur only in loanwords (2000: 84), but lists six native words with final *k > k (p. 94). | k entered as a native phoneme; b, d and r as marginal (loans only). | 1 |
| `kiput-collapsed` | Blust (2002) derives Kiput from PNS through 36 ordered changes (Table 17, p. 420). How are they entered? | As PNS segment > Kiput segment rows, as Blust's own summary of shifts, splits and mergers does (§3.3, pp. 423-427); each row's notes name the changes that prod… |  |
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
| `atayalic-node` | Goderich (2020: Tables 4.41, 4.46) gives Proto-Atayalic (Li 1981) between PAn and Proto-Atayal, with two changes from Proto-Atayalic to Proto-Atayal (*r > *ɹ, … | Not entered: pata and psed stay under PAN, and PAn > Proto-Atayal rows are stated directly. |  |
| `atayal-nodes` | Goderich's subgroup nodes (Proto-Northern, Proto-Nuclear Northern, Proto-Southern, Proto-Nuclear Southern and Proto-Southwestern Atayal; ch. 6): where do the d… | Each change is entered at the node to which ch. 6 assigns it (Tables 6.1-6.15), and only the rest on the dialects. Exception: the affrication of *t, which ch. … |  |
| `siraya-ipa` | Adelaar's Gospel (G) and Utrecht Manuscript (UM) symbols x, D, v, e, o, ʔ and the uncertain c, nḡ, z: how are they entered? | x as ʝ, the voiced palatal fricative of Adelaar (2014: 4 n. 2), not the velar of Adelaar (2011: 52); D kept as D (a root-initial phoneme realised d or r, with … |  |
| `puyuma-ting` | Ting's (1978) Puyuma tree (via Teng 2008: 5): Nanwang against a subgroup of the other five, which further divides into Pinaski-Ulivelivek, Rikavung and Kasavak… | No: Ting's statements are entered on each dialect under Yeh's Proto-Puyuma (ppuy), marked composed. The five non-Nanwang varieties have no glottocodes (Glottol… |  |
| `yeh-puyuma-tree` | Should Yeh’s Puyuma subgroups (fig. 6.1: Proto-Nuclear Puyuma > Proto-Alripay-Mulivelivek, Proto-Likavung-Tamalrakaw, Proto-Katripulr-Kasavakan) be entered as … | Not entered. Yeh’s Table 4.26 states every dialect’s reflexes against Proto-Puyuma, so the rows are entered against ppuy, as Ting’s are (decision puyuma-ting). | 110 |
| `yeh-ting-inventories` | Yeh’s 2023-2024 inventories are now the sourced inventories of Katripulr, Likavung and Kasavakan. Ting’s (1978) rows b > v (all three) and ɖ > ʐ (Kasavakan) de… | Ting’s rows are kept as they are; they now give 4 warnings (reflex outside the sourced inventory). | 5 |
| `saaroa-inventory-pan` | Saaroa (saar1237): whose inventory? | Pan’s (2012) Lha’alua inventory replaces the Tsuchida (1976)-via-Shibata one; Tsuchida’s β is restated as Pan’s v in the correspondence rows (notes say so). | 1 |
| `thao-f` | Thao: Shibata (2025) gives ɸ~f; Blust (2003: 30) says labiodental [f]. | The inventory now follows Blust: f. The PAn *b row is restated as b > f. |  |
| `chen-paiwan-dialects` | Chen (2006) describes Northern (Sandimen), Central (Piuma) and Southern (Mudan, Shimen) Paiwan. How to enter them? | Three dialect lects under ppai (paiwan-north, paiwan-central, paiwan-south) with Chen’s inventories and the changes of his Tables 2.4 and 7.4. Southern *k > ʔ … | 6 |
| `chen-budai-dh` | Chen’s Table 7.4 lists Budai *ð > j. Proto-Rukai *ð is Li’s (1977), but pruk (Li via Shibata) has no *ð. | Entered (22 Nov 2026): Proto-Rukai now has Li's *ð (formosan-ten-3), so the row is buda1252 *ð > j, beside Li's own ð ~ j rows. | 1 |
| `lu-mayrinax-c` | Lu (2004, via Lu 2005: 20) has Mayrinax *c > t before i and y. Goderich (2020) lists no change of *c in Matu’uwal. | Entered against Proto-Northern Atayal, with a hand-entered retention row for *c elsewhere so the stated-unchanged rule still covers it. | 3 |
| `tsou-tfuya` | Tfuya Tsou (Zeitoun 2005b) and Teruku Seediq (Tsukida 2005) give inventories only. Enter them as lects? | Entered as dialects with inventories and no correspondences: tfue1237 under PAn (language_id tsou1248; the existing Tsou lect is Tsuchida’s Duhtu), teru1237 un… |  |
| `maga-li-vowels` | Maga mid vowels (Li 1977, via Hsin 2000): PR *ay, *ai > e; *aw, *au > o; *i, *u > e, o after a lost *a. | Entered as fusion pairs and conditioned rows against Proto-Rukai. Hsin himself derives e and o synchronically (p. 80). | 12 |
| `lin-amis` | Lin (2022) read directly. Shibata’s Proto-Amis (pami) is Lin’s Proto-Amis-Sakizaya; Lin’s subgroups are entered as nodes under it. | pami renamed Proto-Amis-Sakizaya, with Lin’s values *z (fricative) and *d (stop) in place of Shibata’s d and ɮ (Shibata’s values in the notes). New nodes: Prot… |  |
| `chuang-paiwan-dialects` | Chuang’s (2024) sixteen Paiwan dialects are entered as separate lects under Proto-Paiwan. His Timur (三地門) may be Chang’s (2006) Santi (Stimur village), and his… | Kept apart; the linkages are entered as overlap groups, not nodes. |  |
| `tseng-nef` | Tseng (2022) read directly: Proto-Northeast Formosan (Glottolog’s Northern East Formosan) entered under Proto-East Formosan, with Proto-Kavalan and Proto-Basay… | Older PAn-level rows of Kavalan, Basay and Ketagalan (Li & Tsuchida 2006, Shibata 2025, Blust 2013, Ogawa 1931) restated against the new parents through Tseng’… |  |
| `song-seediq` | Song (2025) reconstructs Proto-Seediq from five dialects, with an inventory that differs from Shibata’s (2025) Proto-Seediq (psed): *c, *x, *h and fricative *g… | Song’s inventory entered as the reconstruction system “Song” of psed (notation_map), and the five dialects stated against it (correspondences with system Song)… |  |
| `li-reprints` | Li’s papers read in his Selected papers (2004): which work and pages are cited? | The original paper is the source (li1977, li1981, li1988, li2003, li2004, li1979); its sources row says it was read in the reprint, and pages are the reprint’s. |  |
| `li-atayalic` | Li’s (1981) Proto-Atayalic, read directly: enter it? | Entered as its own proto-language under PAN (patayalic, atay1246) with Li’s inventory and PAN > Proto-Atayalic rows; Proto-Atayal and Proto-Seediq keep PAN as … |  |
| `li-rukai` | Li’s (1977) Proto-Rukai, read directly: how are the rows changed? | Shibata’s via rows are now direct where Li agrees. PAN *R > PR *ʔ and *r both have conditions unknown (Li: conditions unclear); PR *ð is added to the inventory… |  |
| `li-bunun-dialects` | Li’s (1988) five Bunun dialects: which lects? | Takituduh and Takbanuað (no glottocodes) and Takibakha (taki1252) added under Proto-Bunun; Isbukun and Takivatan get Li’s rows. All five are stated-unchanged a… |  |
| `li-plains` | Li (2003) on the four coastal plains languages: whose claims, and the subgroup? | The three innovations Li takes from Tsuchida (1982: 9-10) and the Taokas-Babuza *p change are cited to Tsuchida via Li; *ŋ > n (from Li 1985), the *C and *S ro… |  |
| `li-favorlang` | Li’s (2005) Favorlang reflexes: where? | On Babuza (babu1240), each row labelled Favorlang, as the earlier rows are. His two PAN *S (Dahl’s *S1 > s, *S2 > ø) are two rows with conditions unknown; *p >… |  |
| `shibata-bunun-nodes` | Shibata’s (2020) Northern and Central Bunun: nodes? | Entered as Proto-Northern Bunun (pnbun, nort2902) and Proto-Central Bunun (pcbun, cent2105) under Proto-Bunun, both stated-unchanged with Shibata’s changes as … | 8 |
| `shibata-pb` | Shibata’s (2020) PAN > Proto-Bunun rows beside Li’s (1988): how? | Entered as separate rows on pbun. His *b, *d are Li’s ʔb, ʔd (source_form b, d). PAN *b, *d > *ʔ word-finally are regular rows, with his doubt about *b (p. 73)… | 6 |
| `bunun-dialect-inventories` | Inventories for Takituduh, Takbanuað and Takibakha: whose? | Takituduh from Cheng (2017) via Shibata (2020: 38) and Takbanuað from Shibata (2020: 46), both with implosive ɓ, ɗ; Takibakha from Jiang (2012: 23-30), with b,… |  |
| `litsuchida-amis` | Li & Tsuchida (2022) on Amis: where do their rows and groups go? | Their PAN > Proto-Amis list (pp. 96-97) is entered on pami (Lin’s Proto-Amis-Sakizaya) in Lin’s symbols. The list has *d > r but their summary of mergers has *… | 1 |
| `rau-mstbon` | Rau (2000), sound change in progress in Mstbon Squliq: how? | On Squliq (sqol1237) with variety ‘Mstbon (Ruiyan)’: -p > -k, -m > -ŋ, -l > -n as regular rows (lexical diffusion in the notes), the new variants as sporadic. … | 10 |
| `ross-sibilant-dissimilation` | Ross (2012) on sibilant dissimilation (*C > t when a sibilant follows): where? | On Tsou, Kanakanavu and Saaroa (there is no Proto-Tsouic node) and on Maga and Tona against Proto-Rukai *c, as regular conditioned rows, with the lexical exten… | 10 |
| `ten-4-groups` | Classifications in Blust (1996), Ross (2012), Sagart (2004, 2014, 2026) and Zeitoun & Teng (2016): nodes? | None are nodes. Overlap groups: ‘Western Plains (Blust 1996)’ on Thao and the four western plains languages; ‘Tsouic (Sagart 2014)’ on Tsou, Tfuya, Kanakanavu … |  |
| `lobel-pgcph` | Proto-Greater Central Philippine: node, rows and glottocode? | New node pgcph under PMP (user's choice of 22 Nov 2026: nodes with Lobel's rows). Rows only for what Lobel states in passing: *q > *ʔ, *R > *ɡ, *j > *d, *h kep… | 6 |
| `lobel-subanen` | Subanen internal nodes (Figure 10.1)? | Proto-Subanen with Lobel's inventory (Table 10.3) under pgcph. Nodes Western Subanen (west2811), Nuclear Subanen (nucl1726) and East Nuclear Subanen (east2769)… | 4 |
| `lobel-manide` | Manide and Inagta Alabat: where, and which reflexes? | Node Proto-Manide-Alabat (alab1255, the two languages only) directly under PMP: Lobel takes it as a primary branch of the Philippine macrogroup and there is no… |  |
| `lobel-umiray` | Umiray Dumaget: where? | Directly under PMP: Lobel finds no evidence for Greater Central Philippine and leaves four possibilities open (§7.9). Himes's placement in GCPh is an alt_paren… |  |
| `lobel-swsabah` | Southwest Sabah: which nodes? | Proto-Southwest Sabah (sout3154) under PMP with the four PMP > PSWSAB changes of §11.1.2 (h > ∅, *a > ə / _#, *R > h / [aiu]_[auə], *R > ɡ / ə_). Below it Prot… | 47 |
| `smith-barito` | Barito (Smith 2017a: 168-182): node? | No node: Smith finds no phonological innovation of quality for Proto-Barito (pp. 170-171) and calls Barito a linkage (§2.7.4-2.7.5). The ten lects of Tables 56… |  |
| `smith-basap` | Basap (Smith 2017a: 200-207): node? | An earlier stage Pre-Basap (Glottolog's Basap language, basa1286) with the one change Smith finds shared by all varieties, *-b > -m (p. 202). Lebo (his fieldwo… |  |
| `smith-nesabah` | Northeast Sabah and Molbog (Smith 2017a: 228-235)? | Northeast Sabah (Bonggi + Idaanic, after Blust) rests on lexical innovations only; it is held back as a node, so Bonggi sits under PMP. Idaanic (Idaan, Sungai … |  |
| `smith-nsarawak` | North Sarawak lects of Smith 2017a §2.11: nodes and voiced aspirates? | Dayic is a node (Glottolog kela1257) with its three changes (*z > d, *l > r before final *r, *-k- > *-ʔ-; pp. 238-239), and below it Proto-Kelabit (*t > s / #_… |  |
| `blust-c` | Blust's PAn *c: stored how? | User's choice of 22 Nov 2026: a Blust-system phoneme of PAN with its own descent. The PAN notation row for Blust's c no longer points to *s (phoneme blank, lik… | 4 |
| `tsuchida-1975` | Tsuchida’s 1975 dissertation, read directly: what changes in the 81 Tsouic rows cited to Tsuchida (1976) via Shibata (2025)? | They keep their via: Tsuchida states them against Dyen’s PAN (*D₁-*D₃, *k₁, *k₂, *S₁-*S₃, *H₁, *H₂ …), and matching those to the ACD phonemes is Shibata’s work… | 14 |
| `via-originals-groups` | Blust (1999) and Li (1985), read directly: their subgroups as nodes? | Overlap groups only: ‘Northwest Formosan (Blust 1999)’ on Saisiyat and Pazeh; ‘Central Western Plains (Blust 1999)’ on Taokas, Babuza, Papora and Hoanya; ‘Nort… |  |
| `ogawa-favorlang` | Li’s revised PAN > Favorlang list in Ogawa (2003): how is it entered beside Li (2005)? | Only where it differs: *R (∅ after *i and *e and word-finally, r between i’s, x elsewhere, against Li 2005’s x between a’s and ∅ elsewhere) and the one-word *y… | 4 |

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
- Polynesian (batch `marck2000-polynesian`): Marck 2000 is entered from Tables 2.2, 3.1, 2.32 and 3.30 and Table A.1; Walworth 2014 and Wilson 2021 as alt_parents, plus Wilson's single-word changes. Not entered: Marck's Appendix B and Tables 3.15-3.29 (lexeme-level vowel changes); Table 2.2 "Pla" (undefined); vowel loss between identical consonants (Table 2.2 note 9); Wilson's PEPNP(N). Wilson 2012 (batch `todo-audit`) adds five single-word changes (§5.1, examples 6, 7, 33, 35, 41) on PNO-EPN, PSNO-EPN and PCNO-EPN; not entered are its grammatical innovations and the word changes that are not one-segment substitutions (*kiu > *kiwi, *tuafafine > *tuafine, *lele > *lei, *palu > *lapu, *qaho-qatea > *qooatea). PPn sits directly under POc (decision `ppn-parent`), so most POc phonemes are unentered for PPn.
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
- Competing reconstructions (`competes_with`) are handled by the site, but no lect uses the column yet.

## Housekeeping

- "TEMP import" 1-12 in Google Drive can be deleted.
- Branches `layout-v2-phase1`, `batches-to-sheet`, `e2e-batch-test`, `push-batch-fix`, `phase3-inherit-decisions` can be deleted on GitHub.
