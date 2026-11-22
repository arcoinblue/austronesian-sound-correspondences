# Reverted decisions, 23 November 2026

The user set 24 decisions to `reverted` in the sheet. Three (mc-unchained-cells, ksr-s-before-i, ge-celebic) were carried out on 21 November; this folder carries out the others. `apply.py` edits `cldf/` (the sheet at the last sync) and writes the result; the decisions tab's `chosen_reading` of each decision is rewritten as "Reverted 23 November 2026: …" and the reading before goes to `alternatives`.

    python3 tools/batch_scripts/reverts_2026_11_23/apply.py cldf /tmp/out   # then copy /tmp/out/*.csv to cldf/

The edits change, delete and add rows, so they reach the sheet through **Actions → Apply a migration to the sheet** with `archive` empty and `allow_append` on (dry run first; the run fails unless a sync afterwards finds the sheet equal to `cldf/`). Rows whose key changes (a phoneme respelled, a lect merged) are deleted and appended.

Where a decision had several alternatives, the user chose on 23 November: Wilson's (2021) Polynesian tree (`pn-tree`), Wetar-Galolen as Wetar's parent (`ge-overlap`), nunu1252 without moving Salas (`pas-nunusaku`), Li (1981) alone for the Shibata-relayed Proto-Atayal rows (`atayal-original`). Elsewhere the first alternative was taken (`yeh-ting-inventories`: variety "1970s data").

| decision | done |
|---|---|
| thao-f | Thao ɸ (via Shibata), Blust's f in source_symbol |
| saaroa-inventory-pan | Tsuchida's inventory via Shibata again; Pan in notes; her allophones kept on β |
| yeh-ting-inventories | Ting's rows on Katripulr, Likavung, Kasavakan: variety "1970s data" |
| yeh-puyuma-tree | pnpuy (*b > β, *d̪ > ð, *ɖ > ʐ, *ɡ > h) and palmul, plikta, pkatkas (no own rows); dialect rows restated |
| chen-, chuang-paiwan-dialects | Northern Paiwan (Chen) and Timur (Chuang) merged into Santi |
| li-bunun-dialects | inherit cleared on the five dialects (the nodes already existed) |
| li-plains | Tsuchida-via-Li rows cited to Li (2003) |
| li-favorlang | already done by tree-nodes |
| atayal-original | 7 Shibata-relayed Proto-Atayal rows cited to Li (1981) via Shibata |
| ge-identity-conflicts | 4 identity rows dropped; 13 daughter rows restated (fusion partners too) |
| ge-overlap | pwetgal and pnwetatau; Wetar under pwetgal, pnwetatau a proposed parent |
| pas-nunusaku | pas = nunu1252 |
| lobel-pgcph | pgcph = grea1284 |
| lobel-umiray | Umiray under pgcph, rows restated; Lobel's PMP placement a proposed parent |
| lobel-swsabah | pgdus (grea1293), pgmur (grea1294); shared rows lifted from the members |
| smith-barito | Proto-Barito (the former group) with *-a > *-ə; final *a rows restated |
| pmal-shared | six shared reflexes on Proto-Malayic (composed); lect rows restated |
| cha-y | Chamorro j; *y > j / _# |
| pn-tree | Wilson's parents; Marck's dropped nodes composed onto the moved lects |
| wolff-vowels | **not done**: Wolff (2010) not in hand |
