# blust2013-reinforce

Blust, Robert. 2013. *The Austronesian languages*. Revised edn. (Asia-Pacific Linguistics 008). Canberra: Asia-Pacific Linguistics. Read directly: the excerpt of ch. 8, pp. 553-593 (§8.2 PAN phonology, §8.3 reconstruction below PAN), from the user's Downloads/austdic folder.

Generator: `tools/batch_scripts/blust2013/build.py`.

## Scope

24 correspondence rows and 1 decision. Each row is a second, direct source for a correspondence already entered from another work.

- **PMP > POc (7 rows), from pp. 592-593 and Table 8.32:**
  - *b > *p and *g > *k ('had merged in POC');
  - *d > *r, *z > *s (oral grade), *z > *j (nasal grade);
  - *h > ∅;
  - *e > *o ('most instances').
  Ross et al. (2023) already have these with counts.
- **Formosan languages entered directly under PAN (17 rows):**
  - PAN *j, Table 8.27 (p. 578): Kavalan, Siraya, Kanakanavu, Saaroa, Saisiyat, Thao, Tsou, Pazeh.
  - PAN *h, Table 8.29 (p. 586): Saisiyat, Pazeh.
  - PAN *R, Table 8.30 (p. 588): Taokas, Basay, Thao, Saisiyat, Kavalan, Pazeh.

## Method

Blust's letters are mapped to the IPA already in each lect's sourced inventory, with the printed letter in source_form. For example, Kavalan n is entered as n̪, Kanakanabu l as ɾ (the inventory has no l), Thao lh as ɬ̪, and Saisiyat L ('retroflex flap') as ɾ. Each such row has a note.

The rows Blust lists for proto-languages (Proto-Atayalic, Amis, Bunun, Paiwan, Puyuma, Rukai, Seediq) are not entered. In this database those are proto-language nodes, and Blust names the languages.

## Decision

`pazeh-j-final`: Blust lists Pazeh *j as '-d only' word-finally, an exception to final devoicing (p. 578). The existing row, from Blust (1999b) via Shibata (2025), has t̪. Both rows are kept.

## Not entered

- **The PMP > POc cluster fusions** (*mp, *mb > *b; *nt > *d; *nd > *dr; *-ay > *e; *-aw > *o). Ross's fusion pairs are in the sheet, and a second pair from another source is reported by the build as a repeated fusion row.
- **Blust's evaluations of other reconstructions** (§8.2: Dyen, Dahl, Wolff, Zorc). The Blust notation rows already summarise them.
- **The reflex lists for non-Formosan languages in Tables 8.27 and 8.30.** Most of those languages are not in the database, or sit below intermediate nodes.
- **POc *R > PPn ∅** (Table 8.30) is in batch `marck2000-polynesian`, which creates PPn.


## Applied

2026-11-20 13:57 UTC, by the push-batch workflow.
- correspondences: sheet rows 5092-5428
- decisions: sheet rows 49-60
