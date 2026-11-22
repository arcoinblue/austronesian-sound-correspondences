# Working on ASC: rules for every session

Read this before touching the sheet, the code or the site. It lists the user's standing rules and the mistakes earlier sessions made more than once. `README.md` documents the tables; `STATUS.md` has the counts and open decisions; the handoffs in the claude.ai Project say what each session did.

## 1. Before saying something is done

- **Done means live.** A fix counts when it shows on https://arcoinblue.github.io/austronesian-sound-correspondences/, not when a PR is merged or a cell is written. After a merge or a sheet edit, check the Actions runs: a queued *Build and deploy site* run has been cancelled three times, and each time the site stayed one commit behind while the handoff said the work was live. If the last deploy of `main`'s head did not succeed, run the workflow again (`gh api -X POST repos/arcoinblue/austronesian-sound-correspondences/actions/workflows/pages.yml/dispatches -f ref=main`).
- **Look at the page.** Open the changed pages in a browser (the built-in browser, or headless Chrome on a local `python3 build.py --out build`), at about 800 px and at full width, and read the console. Most layout and display bugs so far were invisible to `build.py --check` and the unit tests.
- **Check what a note promises.** If a note says "has its own page, linked from the table", open the page and find the link. The PAn *s note said this about Blust's *c for two days while no link existed.
- **Re-test the old bug after a neighbouring change.** "Tetun does not appear" was fixed twice and came back in a new form when sourced inventories were added. After touching inventories, `inherit` or the Lects filters, search the Lects page for a lect of each kind: no rows, inventory only, changes only, node only.
- Stamp handoffs with the real time (ask the clock tool), and say which checks ran and which did not.

## 2. Where the data lives

- The Google Sheet is the only source of truth. An edit to `cldf/*.csv` is overwritten by the next hourly sync. Small edits go into the sheet; bulk rows go through `data/incoming/<batch>/` in a PR.
- A new column or tab: merge the code that accepts it first, then change the sheet. In the other order the hourly sync fails until the PR is merged.
- Read the `decisions` tab before starting. The user confirms or reverts decisions there; a reverted decision is an instruction, an open one is not permission to act.
- Never retype IPA by hand into a tool call for more than a few cells. Generate the rows in Python, NFC-normalised.

## 3. Access (do not report these as blockers before trying)

- GitHub: call `add_repo` with `access: "push"`. If it is refused, try once more; it has worked on the second call every time. Use `env -u GH_TOKEN gh api …` (REST only; GraphQL is blocked).
- Source PDFs: `~/Downloads/austdic` and `~/Downloads` on the user's Mac (ask for folder access). `pdftotext` works there, but it drops or garbles IPA and subscripts in tables: read symbol tables from a page image. Put scratch files in the session's scratch folder, not in Downloads (the session cannot delete them afterwards).
- The sheet: Google Sheets connector, spreadsheet id in `README.md`.

## 4. The user's standing rules

**Symbols**
- Never capitalise a (proto)phoneme symbol, in data, headings or CSS (`text-transform`). *s and *S are different phonemes; searches on symbols are case-sensitive.
- /g/ is always ɡ (U+0261).

**Names and tree**
- Proto-languages are written Proto-X with a hyphen, whatever the source prints. Pre-X is an earlier stage of X (type `earlier-stage`), not a proto-language.
- Groups in the Lects tree are named after the clade (Malayo-Polynesian), not the proto-language.
- Every dialect sits under its language node. A language with a representative dialect and no proto-language is a node that redirects to that dialect (Tsou to Duhtu). Identifiable sub-dialects get their own lects; if Glottolog has no code for them they share the dialect's code.
- Linkages are groups with no proto-language. A subgroup that every competing classification contains goes into the main tree; the rest stay as "Proposed parents/daughters".
- Glottocodes: a proto-language takes the code of the Glottolog clade with the same membership (never its name); leave it blank and record a decision when the membership differs. Oceanic codes come from Ross et al. (2023), `reference/oceanic_metadata.csv`.

**Reconstructions**
- A protophoneme gets separate pages by source only when the stated descent differs. Differences of spelling or phonetic value are notation rows and notes.
- A system-only phoneme with its own descent (Blust's *c) still needs `notation_map.phoneme` set to the default-system phoneme that covers it; otherwise nothing links to its page.
- Competing reconstructions B1, B2 of one stage: both listed under A; their daughters only on the B pages (`competes_with`).
- Lobel (2013), Smith (2017 and later): enter correspondence tables and established microgroups; hold back the intermediate nodes above them.

**Inventories and inheritance**
- Place every phoneme in the chart when place and manner can be inferred; list the rest as unclassified consonants or vowels under the chart, never in it.
- Phonemes untouched by any stated change are inherited. An unexplained i e ə a u system keeps the PAN/PMP vowels; an unexplained i e a o u system keeps the POc vowels.
- Every lect needs a way to be shown: rows, or `inherit` with `inherit_source_id` and `inherit_page`, or a sourced inventory. A lect with none of these is hidden by "Hide lects with no data".
- If a source describes allophones, they go in the `allophones` tab for that phoneme. `build.py --check` warns when a note describes realisations and no row exists.

**Citations**
- Unified Style Sheet for Linguistics. Three or more authors: first author et al.; two: "&".
- Cite the original work in `source_id`; record where it was read in `via_source_id`/`via_page` and what the secondary source changed in `via_note`. Prefer reading the original when the PDF is at hand.

**Wording**
- "Proposed parents", "Proposed daughters" (not "in other classifications").
- Answer the user in English; memory notes are kept in Korean.

## 5. Checks to run before a PR

```
python3 build.py --check          # 0 errors; compare the warning count with STATUS.md
python3 -m unittest discover tests   # slow (several minutes); let it finish
python3 tools/batches.py check    # when a batch is in data/incoming
python3 tools/check_glottolog.py  # after lect changes
```

Add a test for every bug fixed in the build, and a line in `README.md` for every new column, mark or page element.
