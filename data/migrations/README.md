# Migrations

Rows a layout migration removed from the sheet because the build now generates them.

- `v3_removed_correspondences.csv`: the 854 X > X rows that `tools/migrate_v3.py` removed (phase 3 of the restructuring plan). The build generates each of them from its lect's `inherit`; `tests/test_migration_v3.py` checks that it still does. Their original notes are kept here.
