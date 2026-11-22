# ASC status

The state of the Austronesian Sound Correspondences database. The generated part is rewritten by the build (`python3 build.py --check --status STATUS.md`), which the hourly sync and the batch workflow run; the sections after it are kept by hand. This file replaces the appended handoffs and the Google to-do doc.

<!-- BEGIN GENERATED: python3 build.py --check --status STATUS.md; do not edit by hand -->

## Data

| Table | Rows | |
|---|---|---|
| sources | 226 |  |
| lects | 978 | 249 dialect, 33 earlier-stage, 9 group, 438 language, 249 proto-language |
| phonemes | 4339 |  |
| correspondences | 10096 | plus 10467 implied and 3451 stated retentions generated from lects.inherit |
| notation_map | 527 |  |
| allophones | 963 |  |
| decisions | 153 | 55 confirmed, 74 open, 24 reverted |

Lects by `inherit`: (blank) 222, assumed-unchanged 516, stated-unchanged 240.
Inventories: edited 28, empty 17, reverse-generated 754, sourced 179.

## Checks

`build.py --check`: 0 error(s), 289 warning(s), 924 note(s).

| Warnings | Count |
|---|---|
| no glottocode | 136 |
| a work cited in notes has no sources row | 66 |
| a source is never cited | 46 |
| a reflex is not in the lect's sourced inventory | 27 |
| an attested lect has symbols that are not IPA | 8 |
| repeats the fusion row at … | 6 |

## Open decisions

From the `decisions` tab. Confirm or revert one by changing its `status` in the sheet.

| id | Question | Reading taken | Rows | Comments |
|---|---|---|---|---|
| `ngorek-nj` | Ngorek reflex of *nj: Table 8 (p. 64) has nc, Table 11 (p. 67) nj. | Not entered. |  |  |
| `psm-j` | Proto-Segai-Modang reflex of Proto-Kayanic *j (PMP *z- and *nz). | *j > *c, inferred from Table 14: it shares the reflexes of medial *c, while *-y- > j stays apart. | 1 |  |
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
| `ppn-parent` | What is the parent of Proto-Polynesian? | POc directly. Proto-Central Pacific (and Proto-Eastern Oceanic) are held back as intermediate stages, as in kayanic-held; POc > PPn rows are composed through P… | 5 |  |
| `pn-orthography` | How are the Polynesian glottal stop and velar nasal written? | ʔ and ŋ, in proto-languages and attested lects. Marck writes the glottal stop *q in proto-languages and ' in living languages (p. 34), the velar nasal ng, and … | 1 |  |
| `pto-r` | Proto-Tongic reflex of PPn *r: loss, or l (Table A.1 vs Table 2.2)? | *r > ∅ elsewhere and *r > *l between like vowels in words beginning with a stop other than *q, both regular (Table A.1, note 1, p. 237). | 2 |  |
| `pnp-h` | PPn *h, lost in Nuclear Polynesian except in a few words (Table 2.2 note 5). | PNP *h > ∅ regular and *h > *h sporadic; each daughter's s or h ('ø/s', 'ø/h') is entered as the reflex of that residual *h. Below PEP Table 2.2 has no *h colu… | 26 |  |
| `marck-diffused` | Marck's diffused changes (lexical diffusion, with residue): PCE *f > *w before *a(a)h, the Nuclear Marquesic low-vowel assimilation, the Kapingamarangi final-v… | Entered as regular with their conditions, each row noting that the change did not reach every eligible word; there is no status between regular and sporadic (S… | 8 |  |
| `mqa-general` | Marck's vowel rows and one sporadic row for 'Mqa (general)' (Table 3.1; Table 2.32), where Table 2.2 has Southern and Northern Marquesan. | Entered on both South and North Marquesan. | 10 |  |
| `mao-f` | Māori reflex of PPn *f, printed 'wh/h' with note 13, whose text ('In some place names only. Elsewhere ' (glottal stop)') fits Tubuai's *ng. | wh regular and h with conditions unknown; note 13 taken to belong to Tubuai. | 2 |  |
| `ren-bel` | Table 2.2 has rows Bel and Ren; Table 1.6 has only 'Ren Rennellese and Bellona'. | Ren on Rennellese (renn1242, Rennell-Bellona) and Bel on Bellona (Glottolog dialect mung1270, alternative name Mungiki). |  |  |
| `blust-unconditioned` | Blust gives several reflexes of one phoneme with counts and no condition (Dobel Table 4; Chamorro final *k, 9:6). How are they entered? | The most frequent reflex is regular 'elsewhere' (or in the environment Blust gives); each other reflex attested twice or more is regular with environment 'cond… |  |  |
| `cha-k` | Chamorro k: Blust says b, d, k and r occur only in loanwords (2000: 84), but lists six native words with final *k > k (p. 94). | k entered as a native phoneme; b, d and r as marginal (loans only). | 1 |  |
| `kiput-collapsed` | Blust (2002) derives Kiput from PNS through 36 ordered changes (Table 17, p. 420). How are they entered? | As PNS segment > Kiput segment rows, as Blust's own summary of shifts, splits and mergers does (§3.3, pp. 423-427); each row's notes name the changes that prod… |  |  |
| `lynch-parents` | Lynch states South Efate, Naman and Nese against POc. PNCV is in the sheet (from François 2011). What is their parent? | POc, as Lynch states them. Lynch (2000b: 321, n. 2) doubts that PNCV existed and suggests South Efate subgroups with Southern Vanuatu; the 2019 papers cite PNC… |  |  |
| `lynch-brackets` | How are Lynch's bracketed reflexes entered? The 2000 paper (p. 328) puts conditioned reflexes in parentheses and reflexes whose conditioning he cannot establis… | Unbracketed or first: regular, elsewhere. Conditioned: regular, with the environment from the text. Square brackets (2000) and the 2019 parentheses: regular wi… |  |  |
| `lynch-ipa` | Lynch writes the three languages in a practical orthography. How are the reflexes entered? | As IPA, with Lynch's symbol in source_symbol and as_printed. South Efate ᵏp, ᵑm = k͡p, ŋ͡m (labiovelars 'coarticulated with initial velar closure followed by l… |  |  |
| `nese-linguolabial-place` | The schema has no place 'linguolabial' for the Nese consonants d̼ ð̼ n̼. | Entered with manner and voicing but place blank, so they are listed under the chart; the notes say linguolabial. A 'linguolabial' place (between bilabial and l… |  |  |
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
| `chen-budai-dh` | Chen’s Table 7.4 lists Budai *ð > j. Proto-Rukai *ð is Li’s (1977), but pruk (Li via Shibata) has no *ð. | Entered (22 Nov 2026): Proto-Rukai now has Li's *ð (formosan-ten-3), so the row is buda1252 *ð > j, beside Li's own ð ~ j rows. | 1 |  |
| `tsou-tfuya` | Tfuya Tsou (Zeitoun 2005b) and Teruku Seediq (Tsukida 2005) give inventories only. Enter them as lects? | Entered as dialects with inventories and no correspondences: tfue1237 under PAn (language_id tsou1248; the existing Tsou lect is Tsuchida’s Duhtu), teru1237 un… |  |  |
| `maga-li-vowels` | Maga mid vowels (Li 1977, via Hsin 2000): PR *ay, *ai > e; *aw, *au > o; *i, *u > e, o after a lost *a. | Entered as fusion pairs and conditioned rows against Proto-Rukai. Hsin himself derives e and o synchronically (p. 80). | 12 |  |
| `lin-amis` | Lin (2022) read directly. Shibata’s Proto-Amis (pami) is Lin’s Proto-Amis-Sakizaya; Lin’s subgroups are entered as nodes under it. | pami renamed Proto-Amis-Sakizaya, with Lin’s values *z (fricative) and *d (stop) in place of Shibata’s d and ɮ (Shibata’s values in the notes). New nodes: Prot… |  |  |
| `tseng-nef` | Tseng (2022) read directly: Proto-Northeast Formosan (Glottolog’s Northern East Formosan) entered under Proto-East Formosan, with Proto-Kavalan and Proto-Basay… | Older PAn-level rows of Kavalan, Basay and Ketagalan (Li & Tsuchida 2006, Shibata 2025, Blust 2013, Ogawa 1931) restated against the new parents through Tseng’… |  |  |
| `song-seediq` | Song (2025) reconstructs Proto-Seediq from five dialects, with an inventory that differs from Shibata’s (2025) Proto-Seediq (psed): *c, *x, *h and fricative *g… | Song’s inventory entered as the reconstruction system “Song” of psed (notation_map), and the five dialects stated against it (correspondences with system Song)… |  |  |
| `li-reprints` | Li’s papers read in his Selected papers (2004): which work and pages are cited? | The original paper is the source (li1977, li1981, li1988, li2003, li2004, li1979); its sources row says it was read in the reprint, and pages are the reprint’s. |  |  |
| `shibata-pb` | Shibata’s (2020) PAN > Proto-Bunun rows beside Li’s (1988): how? | Entered as separate rows on pbun. His *b, *d are Li’s ʔb, ʔd (source_form b, d). PAN *b, *d > *ʔ word-finally are regular rows, with his doubt about *b (p. 73)… | 6 |  |
| `rau-mstbon` | Rau (2000), sound change in progress in Mstbon Squliq: how? | On Squliq (sqol1237) with variety ‘Mstbon (Ruiyan)’: -p > -k, -m > -ŋ, -l > -n as regular rows (lexical diffusion in the notes), the new variants as sporadic. … | 10 |  |
| `lobel-subanen` | Subanen internal nodes (Figure 10.1)? | Proto-Subanen with Lobel's inventory (Table 10.3) under pgcph. Nodes Western Subanen (west2811), Nuclear Subanen (nucl1726) and East Nuclear Subanen (east2769)… | 4 |  |
| `lobel-manide` | Manide and Inagta Alabat: where, and which reflexes? | Node Proto-Manide-Alabat (alab1255, the two languages only) directly under PMP: Lobel takes it as a primary branch of the Philippine macrogroup and there is no… |  |  |
| `allophones-readings` | Readings taken while entering the allophones tab from the sources' descriptions (22 Nov 2026). | General statements are entered on every lect they cover: Goderich (2020: 15) on c, s and r for each Atayal dialect; Chen (2006: 60-68) on 'Paiwan' for the thre… |  |  |
| `lrc2002-readings` | Symbols in the Lynch et al. (2002) sketches whose IPA value is not stated or is ambiguous. | j (a voiced palatal stop or affricate, value not stated) entered as ɟ in Sudest, Teanu (Buma) and Xârâcùù, and ⁿj as ᶮɟ; Tobati /~/ (a nasalisation phoneme in … |  |  |
| `lrc2002-nadroga` | Nadrogā: the sketch says that historically *t became /s/ before /i e/ and /tʃ/ before /u/, *ⁿd became /ⁿdʒ/ before /i u/, and *s became /h/, without naming the… | Entered against Proto-Oceanic (the parent in this database), with a row for each statement; no elsewhere rows for *t and *d. | 4 |  |
| `lrc2002-subgroups` | Ch. 5 names subgroup-defining sound changes: Proto Admiralties *R > *y before high vowels, lost elsewhere (p. 99); Southeast Solomonic merger of POc *l and *R … | Not entered: no Proto-Admiralties, Proto-Southeast Solomonic or Proto-Papuan Tip node was added, and the sketch languages are placed directly under POc (Southe… |  |  |
| `shwng-nodes` | Which of Kamholz's SHWNG subgroups (Table 14.1) to enter as proto-languages? | Only those defined by sound changes and needed for a lect: Proto-Yaur-Yerisiam (*ŋ > ∅) and Proto-Raja Ampat–South Halmahera (*R > ∅), both directly under PSHW… |  |  |
| `shwng-k` | PMP *k > ∅ (change 9) was probably not complete in PSHWNG: *k survives as k in some words, especially in South Halmahera and Moor. | Two rows: *k > ∅ regular, and *k > k sporadic with conditions unknown. | 2 |  |
| `adelaar2005-ms` | Adelaar's Malayo-Sumbawan: a Malayic-Chamic-BSS branch, with Sundanese and Madurese as two other branches, excluding Javanese. Enter it as nodes? | Not entered as nodes. Proto-Chamic, Proto-Balinese-Sasak-Sumbawa, Sundanese, Madurese and Javanese are placed directly under PMP, each with the developments fr… |  |  |
| `adelaar2005-unconditioned` | How to enter Adelaar's 'unconditioned splits' of final diphthongs and changes stated with alternatives (*R > r, y, Ø; *-aw > -u, -ò)? | One row per outcome with conditioning unknown; final diphthong mergers as fusions (V + glide), other diphthong changes as conditioned rows. Where a list item g… |  |  |
| `ross1992-tables` | Ross (1992) was read directly (22 November 2026). Should its Table 2 (Formosan evidence: Proto-Atayal, Saisiyat, Thao, Proto-Bunun, Amis, Proto-Tsou, Proto-Ruk… | Not entered. The database's Ross system on PAn is Ross (2015); Ross (1992) uses a different inventory (*d1, *d2, *d3, *Z, no *θ or *x, Blust's *r folded into *… |  |  |
| `geraghty1986-pcp` | Proto-Central Pacific (Geraghty 1986): where does it attach, and what of its descent from POc is entered? | Under POc, with Glottocode cent2060. POc > PCP rows only where a source states them: *mʷ > *ŋʷ (Geraghty 1986: 306), the liquids from Marck (2000: Table A.1) a… |  |  |
| `geraghty1986-ppn` | Geraghty (1986) gives the PPn reflex of every PCP phoneme. Should Proto-Polynesian now go under PCP? | Not yet: decision ppn-parent (open) keeps PPn under POc. PPn is listed under PCP as a proposed daughter (alt_parents pcp:geraghty1986). The 31 PCP > PPn rows a… |  |  |
| `geraghty1986-pfj` | Proto-Fijian: Glottocode, and its *ñ ('ñ/n' in Table 6). | No Glottocode: Glottolog has no Fijian clade (Western Fijian, and Tokalau Fijian with Polynesian). PFJ keeps *ñ, which Western Fijian keeps apart (n before u, … | 1 |  |
| `geraghty1983-communalects` | Geraghty (1983), Table 15: direct reflexes of 37 Proto-Eastern Oceanic phonemes in 38 Fijian communalects, with a key to 41 sound changes. Enter them? | Not entered in this session. The table states reflexes from Proto-Eastern Oceanic, which is not a node here (decision pocr-parents), and the scan's OCR is unus… |  |  |
| `lynch2001-tree` | Where do the Southern Vanuatu lects go, and what happens to Sye and Anejom, which were entered from Lynch et al. (2002) directly under POc? | Proto-Southern Vanuatu under POc (in the Southern Oceanic group), with Proto-Erromango (Sye, Ura, Utaha), Proto-Tanna (Proto-Northern Tanna: North Tanna, White… |  |  |
| `lynch2001-variants` | How are Lynch's (2001) unconditioned variants entered: 'x ~ y' ('x or y, but more often x'), the fortis/lenis splits of POc *p, *pʷ and *k, and PEr *r ~ *L? | The more frequent reflex as regular 'elsewhere', the other as regular with 'conditions unknown', each with the cell in as_printed. Parenthesised reflexes in Ap… | 18 |  |
| `lynch2001-pnt-pst` | Appendix I prints '?' for *q in Proto-Northern and Proto-Southern Tanna. Was *q still there? | PTn *q > PNT, PST *q with status disputed; each Tanna language has *q > ∅. | 2 |  |
| `lynch2001-psv-e` | PSV *e has two sources (POc *e; POc *a before *Ci, *Cu) with different Proto-Tanna reflexes (*i and *e; Tables 3.4-3.5). | PSV *e > PTn *i regular, and PSV *e > PTn *e with conditioning 'lexical' (scope: PSV *e from POc *a before *Ci, *Cu). Not split into two PSV phonemes, since Ly… | 1 |  |
| `lynch2001-ipa` | Lynch's symbols for the modern Southern Vanuatu languages. | IPA, with Lynch's letter in source_symbol or source_form: y = j (glide); Anejom j = t͡ʃ, ñ = ɲ; Ura b d g and North Tanna bʷ b d = ᵐb ⁿd ᵑɡ, ᵐbʷ ᵐb ⁿd (prenasa… |  |  |
| `nc1992-orthography` | Ozanne-Rivierre writes POc in Milke's spelling (*d, *mpw, *mp, *nt, *nd, *nj, *ŋk) and PNC with geminates (Table 4). How are her statements entered? | Against Ross's POc in the database: her *d = Ross *r, *mpw *mp *nt *nd *nj *ŋk = Ross *bʷ *b *d *dr *j *ɡ (p. 196). PNC symbols as in Table 4, with ṭ and nḍ fo… | 7 |  |
| `nc1992-geraghty` | Geraghty's (1989) Proto-Southern Oceanic reconstructs the same node as Proto-New Caledonian (New Caledonia and the Loyalties). How is it entered? | As rows on PNC citing Geraghty (1989) where he names a change from a POc phoneme: *ñ, *l > *n, *y > ∅, *R > ∅ with sporadic r before high vowels, *l > *r after… | 4 |  |
| `nc1992-lects` | New Caledonian lects in Ozanne-Rivierre (1992): codes and symbols. | Gomen Yuanga = Glottolog Zuanga (thua1237) and Bondé Yuanga = Yuanga (juan1250), dialects of Zuanga-Yuanga; Kumak = Nixumwak (nucl1483), dialect of Nêlêmwa-Nix… | 1 |  |

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
- Southern Vanuatu (Lynch 2001; batches `lynch2001`, `lynch2001-reparent`): canonical-form changes (pretonic vowel loss, accretion, Article Reduction), vowel tendencies without stated conditions, Anejom vowel sequences, chapters 5-8 and Appendix II.
- Central Pacific (Geraghty 1986; batches `geraghty1986-pcp`, `geraghty1986-rotuman`): POc > PCP is entered only for *mʷ, the liquids and *R; the PCP > PPn rows are held until `ppn-parent` and `geraghty1986-ppn` are decided (`python3 tools/batch_scripts/geraghty1986/build.py ppn`); Western/Eastern Fijian and Nadrogā are not under Proto-Fijian. Geraghty 1983, Table 15 (38 communalects, pp. 183-186) is not entered (`geraghty1983-communalects`).
- New Caledonia (Ozanne-Rivierre 1992, Geraghty 1989; batch `nc-ozannerivierre1992`): PNC vowels; Geraghty's aspirates and internal nodes; the Loyalty, Mainland, Northern and Southern New Caledonian subgroups.
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
