# Scripts for the Smith 2017 Borneo batches

These wrote `data/incoming/smith2017-borneo/`. They are kept so the remaining subgroups (Barito, Basap, Sabah,
North Sarawak) can be added the same way. They expect the dissertation's pages as `pdftotext -layout` text
(`tables.py`, path `PAGES`) and write to the repository's `data/incoming/` (`lib.py`, path `ASC`): adjust both.

- `lib.py`: the batch writer, Smith's position labels (`*b-`, `*-b-`, `*-aC` ...), `compose()` (a PMP
  phoneme followed down through the proto-nodes), IPA for Smith's letters.
- `common.py`: rows from a reflex table (`add_language_rows`), retentions for unlisted positions
  (`add_complements`), IPA respelling of retained proto symbols (`ipa_respell`), lects and decisions.
- `tables.py`: reads a table from a page's layout text (check the result against the page image).
- One module per subgroup; `build_all.py` runs them; `merge.py` combines `cldf/` and a batch for a local build.
