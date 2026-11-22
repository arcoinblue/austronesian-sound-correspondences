# kamholz2024-shwng

South Halmahera–West New Guinea, from two chapters of Adelaar, Alexander & Antoinette Schapper (eds.). 2024. *The Oxford guide to the Malayo-Polynesian languages of Southeast Asia*. Oxford: Oxford University Press. Read from the PDFs in the user's Downloads folder (born-digital text, IPA intact). Generator: `tools/batch_scripts/as2024/build.py`.

- Kamholz, David. 2024. Historical linguistics of the South Halmahera–West New Guinea subgroup. 181-188.
- Gasser, Emily, Laura Arnold & David Kamholz. 2024. The languages of Halmahera and West New Guinea. 629-652.

## Entered

- **Proto-South Halmahera–West New Guinea** (sout3229) under PMP, with Kamholz's changes 1-11 and 13 (pp. 181-183), `inherit` assumed-unchanged. Change 12 (lexically specific syncope) is in the notes only.
- **Proto-Yaur-Yerisiam** (yaur1240; *ŋ > ∅) and **Proto-Raja Ampat–South Halmahera** (raja1255; *R > ∅) under PSHWNG (p. 184).
- **Pom, Yaur, Patani**: sourced inventories (Tables 37.1-37.3, p. 632). Yaur and Patani also get the language-level changes of §14.5 that name them, or name their subgroup (Yaur *t > ʔ/∅ through *k, *p > ∅ through f, h, *b > β, sporadic final *u > i; Patani *b > p, *p > f, word-initial y- before *a, final vowel loss), and Yaur gets the Cenderawasih Bay merger of *l and *r as /r/ (Gasser et al., p. 631).
- `notation_map`: canonical rows for the three proto-languages; `phonemes` override rows place their *e (a mid front vowel from *pəñu) as front, since the proto-orthography reads e as schwa.

## Decisions (open)

- `shwng-nodes`: which of Kamholz's subgroups are entered (only the two defined by sound changes); Pom is placed directly under PSHWNG.
- `shwng-k`: *k > ∅ (incomplete in PSHWNG) is entered as regular, plus a sporadic *k > k.

## Not entered

- The morphologically defined nodes (Nuclear Cenderawasih Bay, Yapen and its subgroups, South Halmahera, Central-Eastern South Halmahera), Proto-Southwest Cenderawasih Bay (tentative) and Proto-Biakic.
- The changes of §14.5 for languages not in the database (Biak, Moor, Umar, Wamesa, …), the tonal developments, and the PSHWNG morphology of §14.6.
- Yaur vowel length and tone.

## Checks

`batches.py check`: 0 errors, 280 warnings (as on main). PSHWNG page checked in a local build (headless Chrome, 1100 px).
