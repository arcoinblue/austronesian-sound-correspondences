# blust-histphon

Blust's historical phonologies of Chamorro, Palauan and Dobel, with the Proto-North Sarawak and Proto-Kenyah nodes that Kiput and Òma Lóngh need. All were read directly from the PDFs in the user's Downloads folder.

- Blust, Robert. 2000. Chamorro historical phonology. *Oceanic Linguistics* 39(1). 83-122.
- Blust, Robert. 2007. Òma Lóngh historical phonology. *Oceanic Linguistics* 46(1). 1-53. Only pp. 6-8 are used here (Table 2; the PNS > PK changes).
- Blust, Robert. 2009. Palauan historical phonology: Whence the intrusive velar nasal? *Oceanic Linguistics* 48(2). 307-336.
- Blust, Robert. 2014. Dobel historical phonology. *Oceanic Linguistics* 53(1). 37-60.

The generator is `tools/batch_scripts/blust_histphon/build.py`. There is one module per language.

## Scope

| Table | Rows |
|---|---|
| sources | 6 (blust2000, blust2007, blust2009, blust2014, topping1973, hughes1995a) |
| lects | 4 (Chamorro, Palauan, Proto-North Sarawak, Proto-Kenyah) |
| phonemes | 90 (Chamorro 26, Palauan 19, Dobel 19, PNS 26) |
| correspondences | 195 |
| notation_map | 2 |
| decisions | 6 |

- **Chamorro (cham1312)**, under PMP.
  - Rows: all of §3 (pp. 88-102).
    - Vowels: rules 1-3, syncope with the counts of Table 1, the irregular frontings and backings, and the a/æ split.
    - Diphthongs.
    - Consonants by class.
    - Glide formation and fortition: the inserted gw, g and y after the loss of *h and before initial vowels.
  - Inventory: Topping's (1973), as Blust reports it on pp. 84-85, plus gw. Entered with via_source_id blust2000.
- **Palauan (pala1344)**, under PMP.
  - Rows: Table 2 (p. 309), with the conditions and exceptions of §2.1 (pp. 310-323).
    - Vowels by pre-Palauan stress (decision `pal-vowels`).
    - The *pa-, *-ap, *-ep > o fusions.
    - Initial ŋ- accretion (Table 3).
  - Inventory: Blust's Table 1 (p. 308).
- **Proto-North Sarawak (pns, nort3171)**, under PMP (decision `pns-node`).
  - Rows: Table 2 (p. 6). PNS is stated-unchanged.
    - Each voiced obstruent has a plain and an aspirated reflex. The aspirated one is entered with 'conditions unknown', because Blust says most occur after *e, but not all (p. 7).
  - Inventory: the PNS row of Table 2.
- **Proto-Kenyah (pk, keny1280)**, under PNS, assumed-unchanged.
  - Rows: changes 1-7 of p. 7, with the examples of pp. 7-8.
- **Dobel (dobe1238)**, already in the sheet from Grimes & Edwards.
  - Rows: Table 4 (p. 51) with §§2-3, composed against Proto-Dobel-Koba (decision `dobel-composed`).
  - Inventory: Blust's Table 3 (p. 40), after Hughes (1995a).

## Method

- **Chamorro letters.** The Chamorro PDF is a JSTOR scan whose OCR layer is wrong in most special letters. For example, it gives fiamuk for *ñamuk, rj, 13 or IJ for ŋ, and 1 for l, and it cuts lines at the right margin. Every Chamorro form and symbol was therefore read from page images at 220 dpi, pp. 84-102.
  - Blust's own spelling varies between pages. Forms are copied as printed on the page each row cites:
    - *hapuy > guafi (p. 94), but gwafi (pp. 96-97).
    - *qazay > achay (p. 93), but achai (p. 95).
    - *ŋekŋek > ŋokŋok (p. 94), but ngokngok (p. 96).
    - *aRemaŋ (p. 88), but *aRemang (p. 96).
    - *hipi (p. 96), but *ipi (p. 97).
  - On p. 95 Blust says that without final devoicing *b, *d and *R would be 'f, t, and g'. The last should be k; nothing depends on it.
- **IPA.** Attested forms are entered in IPA, with the printed letter in source_form:
  - Chamorro: ' as ʔ, ch as t͡s, y as d͡z, ñ as ɲ, ng as ŋ, gw as ɡʷ.
  - Palauan: y as j.
  - Dobel: y as j. Blust prints kʷ with a superscript w, and it is entered as kʷ.
  - examples keeps the forms as printed.
- **Other text layers.** The Palauan and Dobel text layers are correct Unicode, and Tables 1-2 (Palauan) and 3-4 (Dobel) were checked against the page images. The Òma Lóngh text layer is a shifted font encoding, so its Table 2 and pp. 6-8 were read from the page images.
- **Counts.** evidence_count holds Blust's counts: Dobel Table 4 and Chamorro Table 1, with evidence_total for Table 1.
- **Unconditioned splits** follow decision `blust-unconditioned`.
- **Dobel composition.** Each Dobel row is restated against the Proto-Dobel-Koba symbol that the Grimes & Edwards rows give for the PMP phoneme, as follows. Blust's statement is in as_printed.

  | PMP | Proto-Dobel-Koba |
  |---|---|
  | *p | β |
  | *b | ɸ |
  | *s | h |
  | *d, *j, *R | r |
  | *z, *y | s initially, y medially |
  | *w | kʷ |

  - The Proto-South Aru identity row *p > p (decision `ge-identity-conflicts`) also gives Dobel ɸ.
  - Now that Dobel has a sourced inventory, its assumed-unchanged retentions are no longer generated. Blust's statements of retention (t, m, n, l, r, kʷ, a, i, u) are therefore entered as rows.

## Decisions

- `pns-node`
- `blust-unconditioned`
- `dobel-composed`
- `cha-k`
- `cha-y`
- `pal-vowels`

## Not entered

- **Chamorro**
  - Sporadic assimilation of syllable-final *k in reduplicated monosyllables (*bakbak > pappa, *bukbuk > poppo) and its loss in *nuknuk > nunu (p. 101).
  - The irregular losses in *bunbun > pupon, *buŋbuŋ > pupong and *tiŋadaq > ngaha' (p. 100).
  - The stray glottal stops and h (p. 101).
  - *beRŋi > pwengi, probably an Oceanic loan (pp. 101-102).
  - *bujeq > bu'o' with b (p. 101).
  - *tazem > tasm-e with s (p. 101).
  - The loanword strata (§3.4, Appendix 2).
  - PMP *D (not discussed).
- **Palauan**
  - *-iw (Table 2 has '?').
  - The problematic etymologies of §2.1.2.1 (*apaqpaq, *panpan, *panaq, *katapa, *ma-paqit, *sa-puluq).
  - *q > Ø after məŋ- (morphological).
  - The loanword adaptations of §3.
- **Proto-Kenyah:** change 8, loss of the first CV- in CVNCVC reduplications (*bəŋbəŋ > *mbəŋ), which is morphological.
- **Dobel**
  - *q > ʔ (1), *anak > yana-, and the conditions on the initial glides (decision `dobel-composed`).
  - The diphthongs (Table 4 has one or two examples each, and Blust says it is 'difficult to generalize', p. 50).
  - Vowel crasis and final-vowel loss, which are irregular.
  - Schwa syncope ('may have', p. 51).
  - The loss of prepenultimate initial vowels.
- **Kiput (Blust 2002) and Òma Lóngh (Blust 2007, §4):** not in this batch. Their parents, PNS and PK, are.
