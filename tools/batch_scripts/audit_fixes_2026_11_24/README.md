# Data fixes from the site audit of 23 November 2026

`apply.py` edits a copy of the tables (row numbers kept) and writes the result:

    python3 tools/batch_scripts/audit_fixes_2026_11_24/apply.py cldf /tmp/out   # then copy /tmp/out/*.csv to cldf/

The edits change and delete rows and append one decision, so they reach the sheet through **Actions → Apply a migration to the sheet** (`archive` empty, `allow_append` on, `max_deletions` 8; dry run first).

| Item | What | Source checked |
|---|---|---|
| Grimes & Edwards's splits | 68 splits printed 'x > a, b' with no conditions: the first reflex stays regular 'elsewhere', the 83 others get environment 'conditions unknown'. Decision `ge-splits` (open). 15 splits are left: their notes point to a table with the conditions, or the rows are not in the printed order. | 'most common reflex listed first' (Abbreviations and conventions, p. xxxiii) |
| Marquesan | The six rows composed from Proto-Nuclear Marquesic repeated the direct South and North Marquesan rows (one as sporadic beside regular); removed, the direct rows annotated. | Marck (2000: 74, note 20) |
| Dobel, Yapese | Dobel *ɸ > ɸ and Yapese *mʷ > m were each entered twice; one row kept. | Ross (1996: 129), Table 2: mᵒ and m- are one phoneme |
| Long Jegan | *-a > 'i̯ əj' is one triphthong, i̯əj. | Smith (2017a: 243), Table 78, page image |
| Chuukic lects | Eleven Bender et al. (2003) reflexes in practical orthography (sh, gh, b, g, th, R) respelled in IPA as in the Jackson (1983) rows of the same lects and Lynch's (2002e) Ulithian inventory. Chuukese ch is left (no IPA value entered for it). | not reread: the values are those already entered from Jackson (1983: 16-18) |
