# Updates, 23 November 2026 (17:00 KST)

Carried out on the user's instruction ("both": the temotu-tree alternative and the pending sheet items). `apply.py` edits a copy of the tables (`cldf/` as synced at ace200f) and writes the result; the reverted decisions' `chosen_reading` is rewritten "Reverted 23 November 2026: …", with the earlier reading in `alternatives`.

    python3 tools/batch_scripts/updates_2026_11_23b/apply.py cldf /tmp/out   # then copy /tmp/out/*.csv to cldf/

It needs the held PCP > PPn rows: `python3 tools/batch_scripts/geraghty1986/build.py ppn` (writes /home/claude/held/geraghty1986-ppn).

The edits reach the sheet through **Actions → Apply a migration to the sheet** with `archive` empty and `allow_append` on (dry run first; 6 deletions).

| item | done |
|---|---|
| temotu-tree (user's choice) | Teanu, Lovono, Tanema under Proto-Vanikoro; PUV a proposed parent; 6 Ross & Næss rows restated (final *s now *R; Tanema *s rows on initial *d) |
| geraghty1986-ppn (reverted) | PPn under PCP; 31 PCP > PPn rows added; 5 composed POc > PPn rows and the Ross (2011) *kʷ row removed; ppn-parent and ross2011-kw readings updated |
| rau-mstbon (reverted) | already done on 22 November (lect `mstbon`); reading updated |
| shwng-nodes (reverted) | Proto-Nuclear Cenderawasih Bay, Proto-Yapen, Proto-Western Yapen, Proto-Central Yapen, Proto-Southwest Cenderawasih Bay, Proto-South Halmahera, Proto-Central-Eastern South Halmahera as pass-through nodes; Pom, Proto-Yaur-Yerisiam, Patani moved under them |
| wolff-vowels (reverted) | Wolff (2010: 46) read: four Wolff vowel notation rows on PAn |
| adelaar2005-ms (comment) | Proto-Malayo-Sumbawan as a proposed parent of Proto-Malayic, Proto-Chamic, PBSS, Sundanese, Madurese |
| geraghty1986-pfj (comment) | Proto-Fijian a proposed parent of Western Fijian |
| lynch2001-variants (comment) | 'fortis'/'lenis' as the environment of the PSV *p, *k rows and of the 23 November fortis/lenis rows |

Not done: geraghty1983-communalects ("when ready": Table 15 needs reading from page images); nc1992-lects ("accept further subgroupings under PNC": no node added yet; decision bril2020-pnnc stays open).
