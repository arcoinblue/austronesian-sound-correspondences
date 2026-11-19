# Austronesian Sound Correspondence Dictionary — data

The repository is the system of record. You enter what a source says into five CSV tables in `cldf/`, and `build.py` checks it, derives everything else, and writes one JSON file per lect for the site.

```
cldf/
  cldf-metadata.json     CSVW/CLDF description of the five tables
  sources.csv            citations
  lects.csv              languages, dialects, proto-languages
  phonemes.csv           hand-entered phonemes only (sourced / manual-add / suppressed)
  correspondences.csv    proto-phoneme > reflex / environment, one row each
  notation_map.csv       each author's symbol for each proto-phoneme
build.py                 validator + derivation (Python 3.9+, standard library only)
tests/                   constraint tests + a FICTIONAL example dataset
build/                   output (generated; don't edit)
```

```bash
python3 build.py --check
```

```bash
python3 build.py
```

```bash
python3 -m unittest discover tests
```

`tests/fixtures/example/` is a small, made-up dataset (Proto-Example-A, Examplese, …) that covers every row type. Copy its rows when you're unsure of a format. **None of it is real data.**

---

## Entry order (source-first)

1. **`sources.csv`**: add the citation before you use its id.
2. **`lects.csv`**: add the lect, with its nearest reconstructed ancestor in `parent_id`. That ancestor has to be entered first and needs phonemes.
3. **`phonemes.csv`**: enter the inventory, but only if the source gives one.
4. **`correspondences.csv`**: for each phoneme of the parent, add one row per reflex × environment, and include the gaps (typed blanks).
5. **`notation_map.csv`**: if the lect is a proto-language, give every phoneme at least a `canonical` row.
6. Run `python3 build.py`. Fix all errors, then read the notes it prints (unentered proto-phonemes, possible allophones).

Nothing is entered from memory. If the claim isn't in a source you have open, use `disputed` with a note, or leave it out.

---

## Conventions

- **UTF-8, NFC.** The build rejects text that isn't NFC. Most editors save NFC; a combining diacritic pasted from a PDF may not be.
- **No `*` anywhere.** Proto-symbols are stored bare (`R`, not `*R`), and the site adds the asterisk.
- **Phoneme key = (lect, symbol).** The build derives the id `<lect_id>:<symbol>` (e.g. `pmp:R`, `mala1479:r`), which also appears in the pivot URL `/lects/?reflex=pmp:R`. Phoneme URLs use `_` for `*` (`/lects/pmp/_R/`).
- **Lect ids** are the Glottocode where one exists (`mala1479`). Proto-languages get a short lowercase slug (`pan`, `pmp`, `pwmp`, `pcemp`, `poc`).
- **`ipa`** holds the IPA symbol for attested lects. For proto-languages it holds the site's canonical symbol (which can be non-IPA, e.g. `C`, `S`, `N`). The source's own spelling goes in `source_symbol`.
- **Lists:** `alt_names` are separated by `;`, and `subgroup_path` by `>` (`PAN > PMP > PWMP`).

---

## Tables

### `sources.csv`

| column | required | values |
|---|---|---|
| `id` | yes | lowercase slug, e.g. `blust2009`, `ross1995` |
| `author`, `year`, `title` | yes | |
| `url_or_doi` | | |
| `kind` | yes | `grammar` · `comparative` · `dictionary` · `database` |
| `notes` | | |
| `year_suffix` | | one lowercase letter when the same author has two works in a year: `b` for Blust (1999b). `year` stays `1999`. |

The site builds the citation label from `author` (`Surname, Given; Surname, Given; …`) and the year: one author gives `Blust 1999b`, two give `Li & Tsuchida 2006`, three or more give `Ross et al. 2023`.

**Columns added later** (`year_suffix` here, and the ones marked *optional column* below) sit at the right-hand end of each table. A sheet or CSV that does not have them yet still loads.

**Indirect citation.** `phonemes`, `correspondences` and `notation_map` each end with three optional columns:

| column | values |
|---|---|
| `via_source_id` | the work you actually read the claim in, when that is not the original |
| `via_page` | the page in that work |
| `via_note` | what that work changed (respelled symbols, a merged category, …) |

`source_id` and `page` are then the original work. The site shows `Li 1981, via Shibata 2025: 55 † note`. Leave all three blank for a direct citation. Two secondary works reporting the same original claim are two rows, each with its own `via_note`.

### `lects.csv`

| column | required | values |
|---|---|---|
| `id` | yes | Glottocode, or a slug for proto-languages |
| `name` | yes | the name used on the site |
| `alt_names` | | `;`-separated, searchable |
| `type` | yes | `language` · `dialect` · `proto-language` |
| `glottocode`, `iso639_3` | | the build warns if an attested lect has no Glottocode |
| `parent_id` | | nearest reconstructed ancestor the source uses; **must be a proto-language**. Empty only for the root (PAN). |
| `subgroup_path` | | established subgroups only, `>`-separated; disputed ⇒ stop at the lowest secure node |
| `default_system` | | *optional column.* The reconstruction system the lect's `phonemes` rows follow, e.g. `Shibata` for PAn. It names the first tab on the site; other systems come from `notation_map`. |
| `region`, `orthography_note`, `notes` | | |

`inventory_status` is not a column. The build derives it from `phonemes.csv`, so no one can promote a generated inventory to "sourced" by editing a label:

| phoneme rows for the lect | status |
|---|---|
| any `origin=sourced` | `sourced` |
| only `manual-add` / `suppressed` | `edited` (generated, plus a displayed diff) |
| none | `reverse-generated` (distinct reflexes in `correspondences.csv`) |

### `phonemes.csv`

One row per phoneme that a source states or that you corrected by hand. Generated phonemes are never stored here.

| column | required | values |
|---|---|---|
| `lect_id`, `ipa` | yes | |
| `source_symbol` | | the source's own spelling |
| `class` | yes | `C` · `V` · `tone` · `other` |
| `place` | | C: `bilabial labiodental labial-velar dental alveolar postalveolar alveolo-palatal retroflex palatal velar uvular pharyngeal glottal` · V (backness): `front central back` |
| `manner` | | C: `plosive prenasalized-plosive implosive affricate prenasalized-affricate nasal trill prenasalized-trill tap fricative lateral-fricative approximant lateral-approximant` · V (height): `close near-close close-mid mid open-mid near-open open` |
| `voicing` | | `voiced` · `voiceless` |
| `rounding` | | `rounded` · `unrounded` (vowels) |
| `origin` | yes | `sourced` (needs `source_id`) · `manual-add` (needs `reason`) · `suppressed` (needs `reason`; hides a generated phoneme) · `override` (needs `reason`; sets the chart position of a generated phoneme) |
| `source_id`, `page`, `reason`, `notes` | | |

**Labialised series.** A consonant whose symbol contains `ʷ` (`pʷ`, `kʷ`) is put in its own chart column, `labialized-<place>`, next to the plain place; enter the plain place (`bilabial`, `velar`) and the build does the rest. To put a symbol without `ʷ` in that column (POc `w`, which the source lists with the labialised bilabials), write the place out: `labialized-bilabial`.

**Chart position of generated phonemes.** A generated phoneme is placed from its symbol. The build reads through length, aspiration and secondary-articulation marks, so `t̪ʰ` is a dental plosive and `n̥` a voiceless nasal. Where that is wrong or impossible, add a row with origin `override`, a `reason`, and the class, place, manner or voicing you want; blank cells keep the inferred value. (A `manual-add` row for a phoneme that is already generated does the same.) A symbol the build cannot read is still put with the consonants or the vowels, according to the proto-phonemes it continues, and is listed under the chart as *unclassified consonants* or *unclassified vowels*.

A lect's rows are either all `sourced` or all `manual-add`/`suppressed`/`override`, never a mix. Leave place/manner blank when the phonetics of a proto-phoneme are unknown.

### `correspondences.csv`

One proto-segment → one reflex, in one daughter, in one environment. The parent lect is not a column: it is always the daughter's `parent_id`.

| column | required | values |
|---|---|---|
| `id` | | leave blank and the build assigns a stable hash; set it yourself only if you need to refer to the row |
| `child_lect_id` | yes | the daughter |
| `parent_phoneme` | yes | symbol in the parent's inventory (`R`, not `*R`) |
| `child_phoneme` | | the reflex in IPA; **blank only for a typed blank** |
| `environment` | yes | `elsewhere` · `#_` · `_#` · `V_V` · `_i` · `C_` … or free text; never blank |
| `status` | with a reflex | `regular` · `sporadic` · `loan-stratum` · `disputed` |
| `blank_type` | with no reflex | `not-attested` · `lexeme-replaced` · `irregular` · `loan` · `disputed` |
| `evidence_count` | | integer: number of supporting cognate sets |
| `source_id` | yes | |
| `page` | strongly advised | the build warns if missing (unless `via_page` is given) |
| `notes` | | |
| `system` | | *optional column.* Set it when `parent_phoneme` is a phoneme of another reconstruction system (`Ross`, with `parent_phoneme` `Z`). Blank means the parent's default inventory. |

How to enter the common cases:

```csv
id,child_lect_id,parent_phoneme,child_phoneme,environment,status,blank_type,evidence_count,source_id,page,notes
,pxb,t,t,elsewhere,regular,,25,example2026,20,
,pxb,C,t,elsewhere,regular,,12,example2026,20,merger: two parents → same child
,samp1234,p,p,elsewhere,regular,,10,example2026,61,
,samp1234,p,ɸ,_u,regular,,3,example2026,61,conditioned split: same parent, two rows
,exam1234,h,,_#,,not-attested,,example2026,46,typed blank
```

**Fusion of a cluster.** When two parent segments fuse into one reflex (PMP *mb* > POc *b*), enter two rows, one under each member, with the same `child_phoneme`. The first member's row has environment `_+Y`, the second member's row has `X+_`:

```csv
poc-mb-b-N,poc,m,b,_+b,regular,,7,ross2023,35,
poc-mb-b-C,poc,b,b,m+_,regular,,7,ross2023,35,
```

The build pairs the rows. The reflex's ancestry then shows one line of descent that starts at the cluster (*m + *b ↘↙ *b), and each member's descent lists the reflex as "*m + *b fuse". This is different from a segment that only changes next to another one, which is one ordinary row with a conditioning environment (`N_`, no `+`): there the neighbour survives as its own segment. If only one of the two rows is present the build warns and treats it as an ordinary conditioned change.

**Reflex depth.** A phoneme page lists reflexes one level down the tree. A deeper row is listed straight away only where the record disagrees about that stage: a `disputed` row, rows from more than one source, or a separate descent entered for another system's phoneme. The rest are behind a "show deeper rows" button.

A parent phoneme with no row at all for a daughter is reported as **unentered**, which is not the same as `not-attested`.

### `notation_map.csv`

| column | required | values |
|---|---|---|
| `lect_id`, `phoneme` | yes | a proto-phoneme already in that lect's inventory (sourced or generated) |
| `system` | yes | `canonical` (the site's own symbol), `Blust`, `Wolff`, `Ross`, `Zorc`, … |
| `symbol` | yes | that system's spelling, without `*` (`t₂`) |
| `source_id`, `page`, `notes` | | |
| `place`, `manner`, `voicing` | | *optional columns.* The phonetic value this system gives the phoneme, in the same vocabulary as `phonemes.csv` |

Every proto-phoneme needs at least one row, and the build fails otherwise.

**Reconstruction systems.** `phonemes.csv` holds the lect's default system (`lects.default_system`). Every other system's phonemes come from this table: a row with system `Ross` and symbol `D` defines Ross's \*D, keyed by lect, system and symbol, so it is a different phoneme from Blust's \*D. The `phoneme` column says which default phoneme it corresponds to; one system phoneme can be listed against several, and `phoneme` may be blank if it has no counterpart. `canonical` and the default system's own name are spellings only and define no phonemes.

On the site each proto-phoneme page has one tab per system. A system's tab shows its symbol and phonetic value. It shows its own reflexes only if `correspondences` has rows with that `system`; otherwise the reflexes are the default ones.

---

## What the build checks

**Errors** (the build fails):

- a header doesn't match
- text isn't NFC, or a symbol contains `*`
- an id is a duplicate, or a reference to a lect or source is unknown
- `parent_id` points to something that isn't a proto-language, or the parent chain loops
- a correspondence has no environment or no source
- a blank has no type, or a row has both a reflex and a blank type
- a status or blank type is outside the vocabulary
- `parent_phoneme` isn't in the parent's inventory, or the parent has no phonemes at all
- one lect mixes sourced and manual phoneme rows
- a `manual-add`/`suppressed` row has no reason
- a proto-phoneme has no `notation_map` row
- the root proto-language has no sourced inventory

**Warnings:**

- a citation has no page
- a reflex isn't in the lect's sourced inventory, or points at a suppressed phoneme
- an attested lect has no Glottocode, or its id isn't its Glottocode
- a `manual-add` row duplicates a generated phoneme

**Notes:**

- unentered proto-phonemes per daughter
- generated phonemes sharing place + manner (possible allophones)
- free-text environments

## Output

`build/data/<lect_id>.json` contains:

- the basic information block
- the derived inventory status, and coverage (phonemes with a sourced descent ÷ inventory size)
- every phoneme with its `notation`, upward `ancestry` (all chains, oldest first; a merger gives several chains) and flattened `descendants` (each with a `via` path, which is what the pivoted index reads)
- the inventory diff for edited inventories

`build/data/index.json` feeds page 1, and `build/data/sources.json` feeds the bibliography. `build/report.txt` keeps the last report.

The viewer in `site/` (plain HTML/JS, no dependencies) is copied into `build/` and renders the three page types from that JSON with hash routes (`#/lects/`, `#/lects/<id>/`, `#/lects/<id>/<phoneme>/`, `#/lects/?reflex=pmp:R`). To preview with the fictional data:

```bash
python3 build.py --data tests/fixtures/example && python3 -m http.server 8765 --directory build
```

Then open http://localhost:8765.

## Editing in Google Sheets

The data is entered in the Google Sheet [Austronesian Sound Correspondences — data](https://docs.google.com/spreadsheets/d/1mzL8wYSb73PeuJShX-Xor7y6iIFDS991F9CV2AZD7mk/edit). It has one tab per table, with the same headers, dropdowns for every fixed vocabulary, and every cell set to plain text. **The sheet is the source of truth: direct edits to `cldf/*.csv` are overwritten by the next sync.**

- `.github/workflows/sync-sheet.yml` runs every hour, or immediately from **Actions → Sync from Google Sheets → Run workflow**.
- It downloads the sheet (`tools/sync_sheet.py`), runs `build.py --check`, and, if the data passes and anything changed, commits `cldf/` and redeploys the site.
- If a check fails, nothing is committed and the run fails. Errors read `tab.csv:ROW`, where ROW is the row in that tab of the sheet.
- The sheet must stay shared as "anyone with the link can view". Its id is stored in the repository variable `SHEET_ID` (Settings → Secrets and variables → Actions → Variables).
- `tools/make_sheet_template.py` regenerates the workbook (tabs, dropdowns, help tab) from `build.py`'s vocabularies, should the schema change. Re-upload it, or copy the changed dropdowns by hand.
- GitHub pauses hourly schedules in repositories with no activity for 60 days. If that happens, re-enable the workflow in the Actions tab.

## Publishing

Every push to `main` runs `.github/workflows/pages.yml`: the tests run, then `build.py` builds from `cldf/`, and the result is deployed to https://arcoinblue.github.io/austronesian-sound-correspondences/. If the data has an error, the build fails and the previous site stays up; the error list is in the Actions log. Pull requests run the same checks without deploying.

## Decisions still open (from the design doc)

- Which proto-languages go in the first release. The schema takes any number; add them as `proto-language` rows.
- Canonical notation. Whatever you choose goes in the `canonical` system of `notation_map.csv` and in `phonemes.ipa` for proto-lects; other authors' symbols are extra rows.
- The first batch of lects and the source for each.

## Deviations from the design doc, and why

- `correspondences` uses `child_lect_id` + `parent_phoneme` + `child_phoneme` instead of `parent_phoneme_id`/`child_phoneme_id`. A typed blank has no child phoneme, so the daughter has to be named separately anyway. The build still derives both ids exactly as the doc describes.
- Generated phonemes are not stored. Only `manual-add` and `suppressed` rows are, so rerunning the build can't overwrite hand edits.
- `inventory_status` is derived rather than entered (see above).
- A `rounding` column was added so vowels can be charted.
- `pycldf` isn't required yet; the build uses only the standard library. `cldf-metadata.json` is in place so `pycldf`/`cldf validate` can read the dataset later, and ABVD/ACD `forms`/`cognates` tables can be added beside it.
