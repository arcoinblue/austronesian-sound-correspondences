# lynch2001

Lynch, John. 2001. *The linguistic history of southern Vanuatu* (Pacific Linguistics 509). Canberra: Pacific Linguistics. Read from the PDF the user attached on 23 November 2026 (ABBYY text layer; every symbol table read from page images, since the text layer garbles superscripts, γ, ŋ and θ). Generator: `tools/batch_scripts/lynch2001/build.py`.

## Scope

- **Proto-Southern Vanuatu** (sout2868) under POc, in the Southern Oceanic group: inventory of Table 2.1 (p. 14), with place and manner written out (PSV *e is a mid front vowel and *ə a separate phoneme, so the proto-orthography reading of e as schwa must not apply). POc > PSV rows from Tables 2.2, 2.3, 2.5, 2.7 and 3.5 and the text (pp. 13-100): labials, velars, liquids, *R (half retained as *r, half lost, unpredictably; final *R lost), coronals and sibilants, *ñ > *y, velarisation of *n next to *q, the vowels, loss of final vowels, retention of *q.
- **Proto-Erromango** (erro1239) and **Proto-Tanna** (tann1242) under PSV, with inventories reconstructed in chapters 2-3; **Proto-Northern Tanna** (nort3218) and **Proto-Southern Tanna** (sout3195) under PTn, from Appendix I and pp. 45-47, 66 (no sourced inventory: generated).
- **New languages:** Ura (urav1235) and Utaha (Ifo, ifoo1237) under PEr; North Tanna, Whitesands, Lenakel under PNT; Southwest Tanna, Kwamera under PST. Sourced inventories from §1.5.1-1.5.2 (pp. 7-8) for Ura, Lenakel, Kwamera, and for Whitesands, North Tanna and Southwest Tanna by Lynch's statements of how they differ from Lenakel or Kwamera. Allophones: devoicing next to h in the Tanna languages, and glide realisations of the high vowels (p. 8).
- **Correspondences:** every cell of Appendix I (pp. 201-203) for each daughter against its immediate parent, with the conditions of parenthesised (conditioned) reflexes from chapters 2-3 (p. 74 says they are there). Lynch's Utaha reflexes are 'highly tentative'; Utaha vowels are not given.

Sye and Anejom are already in the sheet under POc (from Lynch et al. 2002). Their rows are in a second batch, `lynch2001-reparent`, added after their `parent_id` is changed in the sheet (Sye to `per`, Anejom to `psv`; `tree_parent` cleared).

## Decisions (open)

- `lynch2001-tree`: the tree, and moving Sye and Anejom.
- `lynch2001-variants`: 'x ~ y' and the fortis/lenis splits entered as regular + regular 'conditions unknown'.
- `lynch2001-pnt-pst`: PNT and PST *q, printed '?', entered as disputed.
- `lynch2001-psv-e`: PSV *e has two sources with different PTn reflexes.
- `lynch2001-ipa`: IPA for Lynch's letters (y = j, Anejom j = t͡ʃ, prenasalised b d g), and the inventories inferred from his statements.

## Not entered

- Canonical-form changes that are not segment correspondences (pretonic vowel loss, accretion of verb-initial vowels and of the article *na, Article Reduction, medial vowel deletion; ch. 4), except the loss of final vowels and of final *R. Lynch's PSV *nt (article + *t) and PEr clusters *n + *r, *n + *t are in the notes.
- The many vowel 'tendencies' with no statable conditioning, except where Lynch tabulates them (Tables 3.2-3.4); Anejom vowel sequences (§3.1.2).
- Chapters 5-8 (morphosyntax, subgrouping arguments, Polynesian contact) and the lexical reconstructions of Appendix II.

## Checks

`batches.py check` (with the other two batches of this PR): 0 errors. One new warning here: Whitesands *d > rh (a cluster) is not in its sourced inventory.
