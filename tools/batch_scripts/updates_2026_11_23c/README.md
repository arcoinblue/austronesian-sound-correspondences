# Updates, 23 November 2026 (18:00 KST)

The user's instructions of 23 November 2026 (decisions `linkage-type`, `formosan-inherit`, `small-inventory-inherit`, `alt-phoneme-links`). `apply.py` edits a copy of the tables (`cldf/` as synced at badabd9) and writes the result:

    python3 tools/batch_scripts/updates_2026_11_23c/apply.py cldf /tmp/out   # then copy /tmp/out/*.csv to cldf/

The edits reach the sheet through **Actions → Apply a migration to the sheet** (`archive` empty, `allow_append` on; dry run first; no deletions).

| instruction | where |
|---|---|
| non-established nodes in italics, below the established ones | lect type `linkage` (Southern Oceanic, the four Paiwan linkages); `site/js/lects.js`, `site/style.css` |
| no Proto- / Pre- in the tree labels | `site/js/lects.js` (`treeName`, `treeLink`); lect pages unchanged |
| changes stated against an alternative proto-phoneme link to its page | the `system` column (already linked); Shibata's (2020: 76) PAN *r > Proto-Bunun *l added against Blust's *r |
| Formosan lects under groups with no proto-language inherit PAn | `inherit` = `assumed-unchanged` on 21 lects (see decision `formosan-inherit`) |
| fewer than 13 phonemes: inherit from the immediate ancestor | build rule (`asc/validate.py`, `SMALL_INVENTORY`) |
| Smith (2023) Bornean subgroups | `smith2023.py`, read by `apply.py` when present |
