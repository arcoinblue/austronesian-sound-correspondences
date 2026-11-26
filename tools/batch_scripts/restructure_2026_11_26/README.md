# Tree and dialect edits of 26 November 2026

`apply.py` edits a copy of the tables (row numbers kept) and writes the result:

    python3 tools/batch_scripts/restructure_2026_11_26/apply.py cldf /tmp/out   # then copy /tmp/out/*.csv to cldf/

The edits change 42 lects, 23 correspondences and 1 decision in place, delete 3 lects, 1 correspondence and 1 allophone
row (moved to another lect, so deleted and appended), append 9 lects, 26 correspondences, 2 allophones and 2 decisions,
and add the column `correspondences.parent_lect_id`. They reach the sheet through **Actions → Apply a migration to the
sheet** (`archive` empty, `allow_append` on, `max_deletions` 5; dry run first). Run it straight after
the merge: a scheduled sync that runs in between copies the unchanged sheet over `cldf/` again.

| Item | What |
|---|---|
| Greater Micronesian | The alternative node `pgmc` is deleted (decision `jackson1986-pgmc` reverted by the user). |
| North and Central Vanuatu | One clade with the groups Northern Vanuatu (new, nort3205) and Central Vanuatu (cent2269, now under PNCV). The lects Lynch states against POc keep `parent_id` `poc` and are listed under Central Vanuatu (`tree_parent`). Decision `ncv-tree` (open). |
| Gayo | Bukit, Cik, Dëret, Lues and Serbejadi Gayo under Pre-Gayo; `gayo1244` retired. Billings & McDonnell (2024: 117-118), read again from the PDF. |
| Enggano | Southern and Western Enggano under Pre-Enggano (Table 10, p. 124); `engg1245` retired. |
| Mentawai | Simalegi (sima1259) split off with *s, *t > t (p. 143). The other varieties are not named by the source; Pampus (1989, 1994) and Blust (1997: 158-160) are not at hand. Decision `sumatran-dialects` (open). |

No row uses `parent_lect_id` yet: the Yapese strata of Ross (1996) that it was added for (Sets A, B against PMP; D and UW
against Nuclear Micronesian) are still to be entered.
