# Austronesian Sound Correspondence Dictionary — data

The data is entered in the Google Sheet (see *Editing in Google Sheets*), which is synced into seven CSV tables in `cldf/` (six of data, and `decisions`). `build.py` checks them, derives everything else, and writes one JSON file per lect for the site. `STATUS.md` says where things stand: table sizes, check results, open decisions, and what is still to enter or to code.

```
cldf/
  cldf-metadata.json     CSVW/CLDF description of the tables (kept in step by tools/make_metadata.py)
  sources.csv            citations
  lects.csv              languages, dialects, proto-languages
  phonemes.csv           hand-entered phonemes only (sourced / manual-add / suppressed)
  correspondences.csv    proto-phoneme > reflex / environment, one row each
  notation_map.csv       each author's symbol for each proto-phoneme
  decisions.csv          readings taken during entry that wait for confirmation
build.py                 the command line (Python 3.9+, standard library only)
asc/                     the build, in modules:
  schema.py              vocabularies, table columns, what a symbol means (IPA, proto orthography)
  load.py                reading the CSV tables; the report
  cite.py                citation labels, USS references, works cited in notes
  validate.py            every check, and the inventories, retentions, notation and systems
  derive.py              edges, ancestry, descent, the lect and phoneme records
  export.py              writing build/data/ and STATUS.md
site/                    the viewer: index.html, style.css, js/ (one script per page type)
tools/                   sync, batches, migrations, sheet template
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
4. **`correspondences.csv`**: for each phoneme of the parent, add one row per reflex × environment, and include the gaps (typed blanks). Where the source lists only changes, or only the nontrivial correspondences, set the lect's `inherit` instead of typing the X > X rows.
5. **`notation_map.csv`**: if the lect is a proto-language, add one default `canonical` row (phoneme and symbol blank) citing where its spelling comes from, plus a row for each phoneme the source spells differently.
6. Run `python3 build.py`. Fix all errors, then read the notes it prints (unentered proto-phonemes, possible allophones).

Nothing is entered from memory. If the claim isn't in a source you have open, use `disputed` with a note, or leave it out.

---

## Conventions

- **UTF-8, NFC.** The build rejects text that isn't NFC. Most editors save NFC; a combining diacritic pasted from a PDF may not be.
- **No `*` anywhere.** Proto-symbols are stored bare (`R`, not `*R`), and the site adds the asterisk.
- **Phoneme key = (lect, symbol).** The build derives the id `<lect_id>:<symbol>` (e.g. `pmp:R`, `mala1479:r`), which also appears in the pivot URL `/lects/?reflex=pmp:R`. Phoneme URLs use `_` for `*` (`/lects/pmp/_R/`).
- **Lect ids** are the Glottocode where one exists (`mala1479`). Proto-languages get a short lowercase slug (`pan`, `pmp`, `pwmp`, `pcemp`, `poc`).
- **`ipa`** holds the IPA symbol for attested lects. For proto-languages it holds the site's canonical symbol (which can be non-IPA, e.g. `C`, `S`, `N`). The source's own spelling goes in `source_symbol`.
- **Lists:** `alt_names` are separated by `;`, and `subgroup_path` by `>` (`Austronesian > Malayo-Polynesian`).

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
| `pub_type` | | *optional column.* `book` · `article` · `chapter` · `thesis` · `presentation` · `dataset` · `other` |
| `container_title` | | the journal (article), the edited volume (chapter), or "Paper presented at …" (presentation) |
| `editors` | | of the volume, given name first, `;`-separated: `Ray Harlow; Robin Hooper` |
| `volume`, `issue`, `pages` | | `59`, `1/2`, `297-346` |
| `place`, `publisher` | | for a thesis the publisher is the degree line: `National Tsing Hua University dissertation` |
| `series`, `edition` | | `Pacific Linguistics C-98`; `2nd edn.` |

**Reference list.** The Sources page prints each work in the form of the [Unified Style Sheet for Linguistics](https://langsci-press.org/unifiedstylesheet): `Lee, Kee-dong & Judith W. Wang. 1984. Kosraean reflexes of Proto-Oceanic phonemes. In Byron W. Bender (ed.), *Studies in Micronesian linguistics* (Pacific Linguistics C-80), 403-442. Canberra: The Australian National University.` The first author is surname-first and the others given-name-first, joined by commas and `&`; the year has no brackets; only titles of books, dissertations and edited volumes and names of journals are italic. A row with no `pub_type` prints author, year and title only, with nothing in italics. Titles are stored as they should print (sentence case; journal names with capitals).

`tools/split_source_notes.py` moves publication details that still sit at the start of `notes` into these columns (`--write` to save; without it, a preview). It skips rows that already have a `pub_type` and lists the ones it cannot read.

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
| `type` | yes | `language` · `dialect` · `proto-language` · `earlier-stage` (an earlier state of one language, reached by internal reconstruction or inferred from a proto-language: Pre-Gayo) · `group` (a node of the tree that is not a lect: a linkage, or a subgroup that every proposal agrees on but for which no proto-language is entered, such as Central Western Plains; it has no rows and no page) · `linkage` (a group that is a linkage, not a subgroup with a proto-language: Southern Oceanic, the Paiwan linkages, Barito-Basap; handled like `group`). Both reconstructed types can be a parent and have starred symbols. |
| `glottocode`, `iso639_3` | | the build warns if an attested lect has no Glottocode |
| `parent_id` | | nearest reconstructed ancestor the source uses; **must be a proto-language or an earlier-stage**. Empty only for the root (PAN). |
| `subgroup_path` | | **leave blank**: the build derives it from `parent_id`, each ancestor's `clade` (or name without Proto-), root first. Fill it only to override the derived path, `>`-separated: the root, a group with no proto node entered (Atayalic), a member whose node is missing (Island Kaili–Wolio). The build notes cells that equal the derived path. |
| `default_system` | | *optional column.* The reconstruction system the lect's `phonemes` rows follow, e.g. `Shibata` for PAn. It names the first tab on the site; other systems come from `notation_map`. |
| `systems` | | *optional column.* The lect's reconstruction systems, `;`-separated, in tab order: `Shibata;Blust;Ross;Wolff`. Any other system in `notation_map` is then a spelling only (Grace's POc orthography): it appears in the notation table and gets no tab. Blank: every system in `notation_map` gets a tab, in the order first seen. |
| `clade` | | *optional column.* The group a proto-language is the ancestor of, used as the heading in the lect tree. Blank: the name without `Proto-` (Proto-Malayo-Polynesian heads *Malayo-Polynesian*). An earlier-stage heads no group. |
| `competes_with` | | *optional column.* Id(s) of other lects that reconstruct the same node, `;`-separated; one direction is enough. See *Competing reconstructions*. |
| `latitude`, `longitude` | | *optional columns.* Decimal degrees, south and west negative (`-8.38`, `118.18`). The lect page links them to a map. `tools/extract_coordinates.py` moves "coordinates -8.38, 118.18" out of `notes` into these columns. |
| `inherit` | | *optional column.* What happens to a parent phoneme for which the lect has no row; the build then generates the X > X rows instead of their being typed. Blank: nothing (the phoneme is reported as unentered). `assumed-unchanged`: the source lists only the changes into this lect (a classification tree such as Grimes & Edwards 2026), so retention is our inference. A parent phoneme with no row is retained, and one with only conditioned rows is retained elsewhere. The rows are `implied-retention`, shown in grey, and never count as stated. Where the lect has a sourced inventory, only the parent phonemes that this inventory also has (same symbol, no conflicting place or manner) get such a row; the others stay open. `stated-unchanged`: the source says that what it does not list is unchanged (it tabulates only the nontrivial correspondences, as Billings & McDonnell 2024). A parent phoneme with no row, or only sporadic or borrowed ones, is retained; conditioned rows get no complement, because such a source states its conditions in full. The rows are `stated-retention`, count as stated, and are marked "unchanged per source". An explicit row always wins. Blank on a lect with rows of its own but fewer than 13 phonemes known (its sourced inventory, else its distinct reflexes): the build treats it as `assumed-unchanged`, carrying down what of the immediate ancestor its rows leave open, and the lect page says so (decision `small-inventory-inherit`). (This column was `changes_only`, `TRUE` = `assumed-unchanged`.) |
| `language_id` | | *optional column.* For a dialect: the language it belongs to. The dialect's page says "Dialect of …" and the language's page lists its dialects. The lect tree lists the dialect under its language when both have the same `parent_id`. |
| `inherit_source_id`, `inherit_page` | | *optional columns.* The citation of the generated rows: where the source says (or shows) that the rest is unchanged. Blank: the source and page the lect's own rows cite most. Give them for `stated-unchanged`. |
| `inherit_note` | | *optional column.* The note of the generated rows (`Unchanged: not among the nontrivial sets of Table 3 (p. 119).`). Blank: a standard note. |
| `alt_parents` | | *optional column.* Other classifications, `parent_id:source_id`, `;`-separated: `pef:chen2022`. The tree and the correspondences follow `parent_id`; the lect page lists the other hypotheses under "Proposed parents" and the proposed parent lists the lect under "Proposed daughters". In the lect tree a node that has members only in this way (Proto-Atayalic, Proto-Coastal Formosan) is an *alternative node*: in italics, marked "proposed grouping (source)", after its established sisters, with its members listed under it in ordinary type; an established node that a classification gives further members shows them under a line "proposed grouping (source)". The *Alternative nodes* switch hides both. |
| `tree_parent` | | *optional column.* The node the lect tree lists the lect under, when that is not `parent_id`: a `group` (a linkage, an agreed subgroup), a language (for a dialect whose `language_id` is not given), a dialect (for a sub-dialect), or, since 26 Nov 2026, any lect that stands at or below the lect's `parent_id`, a reconstructed one included. The tree is the classification; `parent_id` is the predecessor of the lect's rows and the lect it inherits from. Nese is stated against POc by Lynch (`parent_id` `poc`) and listed under North and Central Vanuatu > Central Vanuatu (`tree_parent` `central-vanuatu`, a group whose own `parent_id` is `pncv`). The lect's page says both ("Nearest ancestor", "Listed under"). A tree parent that does not stand under the lect's `parent_id`, or a loop, is an error. A sub-dialect may share its dialect's Glottocode. Blank: the dialect's `language_id`, else `parent_id`. |
| `representative` | | *optional column.* For a language with no rows of its own: the dialect its entry opens (Duhtu for Tsou). A language or dialect with no rows of its own and lects listed under it is a node of the tree with no page (Babuza, Pazeh-Kaxabu). |
| `overlap_groups` | | *optional column.* Names of subgroups that cut across the tree, `;`-separated (`Wetar-Galolen`). They are labels, not nodes: a lect can be in several, its `parent_id` stays what the tree says, and the changes that define the group are entered on each member. The lect page lists the other members, and the lect filter finds the name. |
| `region`, `orthography_note`, `notes` | | |

**Names.** A proto-language is `Proto-X`, with the hyphen even where the source writes "Proto X"; an earlier stage is `Pre-X`. The build warns otherwise.

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
| `status` | | *optional last column.* `marginal` (a marginal phoneme of an attested lect: loans only, or an allophone the source lists) · `dubious` (a doubtful proto-phoneme). The inventory shows it in parentheses. |

**Labialised and velarised series.** A consonant whose symbol contains `ʷ` (`pʷ`, `kʷ`) is put in its own chart column, `labialized-<place>`, next to the plain place; one whose symbol contains `ˠ` (Kosraean `tˠ`) goes to `velarized-<place>`, between the two. Enter the plain place (`bilabial`, `velar`) and the build does the rest. To put a symbol without `ʷ` in that column (POc `w`, which the source lists with the labialised bilabials), write the place out: `labialized-bilabial`.

**Blank and unknown features.** If a sourced row leaves place or manner blank, the build fills it from the symbol and the site shows the phoneme in italics, with "inferred from the symbol" on hover (see *Marks in the charts* under *Output*). In a proto-language the reconstruction orthography is read first (`y` palatal glide, `e` schwa, `c z j ñ N C S R` with the ACD values), then IPA. Two readings come before these tables. Where a lect writes both `y` and `j`, `y` is the palatal glide and `j` a palatal (or palatalised coronal) stop or affricate, in proto-languages and attested languages alike. And a letter that is not plain IPA and is continued unchanged from the parent is read as the parent reads it, so the `y` of the Micronesian languages is the glide of PMc \*y. Write `unknown` where the source deliberately leaves the value open (place of PAn \*R): it is never inferred. A phoneme with only a place or only a manner sits in an *unspecified* row or column of the chart; with neither, it is listed as unclassified.

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
| `as_printed` | | *optional column.* The source's statement as printed, when the row restates it (`*b > **β, **b`; a tree's clause composed against an intermediate node). Shown before the notes as "As printed: …". |
| `locator` | | *optional column.* Where on the page: `Table 18`, `fig. 4`, `§4.8.3`, `tree`. Shown after the page number. Keep `page` a page number. |
| `conditioning` | | *optional column.* `stated` (the environment is the condition) · `unknown` (the source gives no condition; environment `conditions unknown`, set automatically) · `lexical` (in some words only; say which in `lexical_scope`) |
| `evidence_total` | | *optional column.* N where the source gives "n of N": `evidence_count` 12, `evidence_total` 94. Shown as "12 of 94". |
| `derivation` | | *optional column.* `as-stated` (blank) · `composed` (restated against an intermediate node from the source's statements) · `implied-retention` and `stated-retention` (the build adds these for lects with `inherit`; enter them by hand only for a single retention, inferred or stated) |
| `variety`, `stratum`, `lexical_scope` | | *optional columns.* What used to go into `environment` but is not a phonological condition: `Southern dialect`, `older generations`; `Kiribati loans`, `Northern stratum`; `*kəmpuŋ`, `two etyma`. |
| `examples` | | *optional column.* Cognate-set ids (ACD) or example forms as printed, `;`-separated. |
| `source_form` | | *optional column.* The reflex as printed, when `child_phoneme` is its IPA (printed `ʤ`, stored `d͡ʒ`). |
| `decision` | | *optional column.* The `id` of a `decisions` row when the row depends on a reading that waits for confirmation. |
| `parent_lect_id` | | *optional column (26 Nov 2026).* The row's predecessor, when it is not the lect's `parent_id`: the lect that `parent_phoneme` belongs to. Blank in almost every row. Use it for a loan stratum, stated against the donor or the donor's ancestor (Yapese words from a pre-Oceanic source against `pmp`, from Nuclear Micronesian against `pmc`), and for a reflex that a source states against a stage other than the one the lect inherits from. An attested lect can be named only by a `loan-stratum` row (its donor). Such a row is the lect's reflex of that phoneme and nothing more: it adds the reflex to a generated inventory and is listed on the predecessor's phoneme page (tagged "not its parent") and on the lect's page under "Stated against other lects" and on the reflex's page under "Also from other lects"; it is not a line of the ancestry diagram, it is not followed further down, and inheritance (`inherit`), coverage and the unentered-phoneme notes leave it aside. |
| `system` | | *optional column.* Set it when `parent_phoneme` is a phoneme of another reconstruction system (`Ross`, with `parent_phoneme` `Z`). Blank means the parent's default inventory. A change the source states against a proto-phoneme that only another system has (Blust's PAn \*r, \*c, \*ñ) always gets that system, so that it links to that system's page for the phoneme (decision `alt-phoneme-links`). |

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

The build pairs the rows. In the reflex's ancestry diagram the two members run to a "+" junction and one line goes on to the reflex, and each member's descent lists the reflex as "*m + *b fuse". A vowel and a glide that fuse are entered the same way (PMP *-aw* > POc *-o*: `a > o / _+w` and `w > o / a+_`). This is different from a segment that only changes next to another one, which is one ordinary row with a conditioning environment (`N_`, no `+`): there the neighbour survives as its own segment. If only one of the two rows is present the build warns and treats it as an ordinary conditioned change.

**IPA in attested lects.** `phonemes.ipa` and `child_phoneme` hold IPA for languages and dialects: `ɡ` (not Latin g), `j` for the palatal glide, `ɲ`, affricates with a tie bar (`t͡ʃ d͡ʒ t͡s d͡z`). The printed form goes in `source_symbol` / `source_form`. The build warns about Latin g, y, ñ, the old ligatures ʤ ʧ, untied affricates, digraphs and cedilla/caron letters. Proto-languages keep their reconstruction orthography (`*y`, `*ñ`, `*j`).

**/ɡ/ is always `ɡ` (U+0261).** In every symbol column (`phonemes.ipa`, `notation_map.phoneme` and `symbol`, `correspondences.parent_phoneme` and `child_phoneme`), proto-languages included, Latin g is a build error, and so is a g standing as a symbol in an environment (`_ɡ`). Reconstructions written with `*` in notes and examples use `ɡ` too; `as_printed` and `source_symbol` keep the source's letter. The digraph `ng` of an orthography (Polynesian `*ngau`) is left as printed.

**Unknown conditioning** is written one way: environment `conditions unknown`. "not stated", "conditions unclear" and similar spellings are warned about.

**Stable ids.** Every correspondence row has an `id`. One left blank gets a hash of its content, which changes when the row is edited; fill it in (the build's report gives the value) so links to the row keep working.

**Inserted sounds.** A sound with nothing behind it in the parent (an epenthetic vowel, a glide before an initial vowel, a paragogic consonant) is a row with `parent_phoneme` `∅` and the sound in `child_phoneme`, with the environment it appears in: `∅ > ə / C_#`. Its ancestry starts from ∅, and the parent's page lists it under *Sounds inserted in daughter lects*. Leave `system` blank.

**Syllable positions.** Where a condition counts syllables and no segment slot can say it (a source's σσ# with one σ marked), use one of these set terms as the environment: `final syllable` · `penultimate syllable` · `antepenultimate syllable` · `initial syllable` · `non-final syllable` · `stressed syllable` · `unstressed syllable` · `pretonic syllable` · `posttonic syllable`. Any other environment without a `_` slot is reported as free text.

**Loss of a nasal before a consonant.** Where a nasal + consonant cluster is reflected exactly like the plain consonant (PMP *mp* > POc *p*), enter the loss of the nasal: parent the nasal, `child_phoneme` `∅`, environment `_p`, status `sporadic` unless it is the regular outcome, and the number of instances in `evidence_count`. The consonant needs no row of its own for the cluster.

**Borrowed correspondences.** Status `loan-stratum` (shown as *borrowed*) is for a correspondence found only in loanwords or suspected loans; say in `notes` what the source says. If only some of the examples are loans, keep the normal status and mention the loans in `notes`.

**Stating reflexes against the immediate ancestor.** A source may tabulate every language against the top proto-language (Bender et al. 2003 against PMc). Where the same table also gives the intermediate proto-languages, the rows are composed and entered step by step (PMc > PCMc > PWMc > PPC > PCK > Chuukese), and each row's notes keep the statement as printed.

**Ancestry diagram.** A phoneme page draws its ancestry as a node diagram: one row per stage, every ancestor phoneme once, a line per correspondence (dashed if never regular), with the steps, conditions and sources in a table underneath.

**Competing reconstructions.** Where two lects B1 and B2 reconstruct the same stage under A (set `competes_with` on one of them), A's reflex list shows the reflexes in both, marked *competing*, and nothing below either: C's reflexes are on the pages of B1 and B2 only, also when "show deeper rows" is on. The table of all lects still lists everything.

**One page per proto-phoneme.** A phoneme of another reconstruction system gets a tab of its own only if its descent differs, that is, if `correspondences` has rows with that `system` for it, or if nothing in the default inventory matches it. A system phoneme that differs only in spelling or phonetic value is shown on the default phoneme's page, under *In other reconstructions*, with its value, source and explanation.

**Reflex depth.** A phoneme page lists reflexes one level down the tree. A deeper row is listed straight away only where the record disagrees about that stage: a `disputed` row, rows from more than one source, or a separate descent entered for another system's phoneme. The rest are behind a "show deeper rows" button.

A parent phoneme with no row at all for a daughter is reported as **unentered**, which is not the same as `not-attested`.

### `notation_map.csv`

| column | required | values |
|---|---|---|
| `lect_id` | yes | |
| `phoneme` | yes, except on a default row | a proto-phoneme already in that lect's inventory (sourced or generated) |
| `system` | yes | `canonical` (the site's own symbol), `Blust`, `Wolff`, `Ross`, `Zorc`, … |
| `symbol` | yes, except on a default row | that system's spelling, without `*` (`t₂`) |
| `source_id`, `page`, `notes` | | |
| `place`, `manner`, `voicing` | | *optional columns.* The phonetic value this system gives the phoneme, in the same vocabulary as `phonemes.csv` |

Every proto-phoneme needs a `canonical` spelling, and the build fails otherwise. Most are spelled as themselves, so one **default row** per lect covers them: system `canonical`, `phoneme` and `symbol` blank, and the citation (`source_id`, `page`, `notes`) for the lect's spelling:

```
lect_id,phoneme,system,symbol,source_id,page,notes,...
poc,,canonical,,ross2023,26,"Orthography of Ross (1988, 1989)."
poc,R,canonical,R,ross2023,27,"Orthography of Ross (1988, 1989)."
```

The build gives every phoneme of the lect without a `canonical` row of its own a row with the default's citation (implied phonemes of an assumed-unchanged lect get none). Enter a phoneme's own row only where the spelling or the citation differs; it wins over the default. `tools/migrate_v2.py` collapsed the per-phoneme rows into defaults (see *Layout v2* below).

**Reconstruction systems.** `phonemes.csv` holds the lect's default system (`lects.default_system`). Every other system's phonemes come from this table: a row with system `Ross` and symbol `D` defines Ross's \*D, keyed by lect, system and symbol, so it is a different phoneme from Blust's \*D. The `phoneme` column says which default phoneme it corresponds to; one system phoneme can be listed against several, and `phoneme` may be blank if it has no counterpart. `canonical` and the default system's own name are spellings only and define no phonemes.

A system phoneme with blank place or manner is filled the same way: from a distinctive IPA symbol (`θ`), else from the default phoneme it matches, else from the symbol tables. To say that a system does not have one of the default phonemes at all, add a row with symbol `∅`. With the default system's own name, that removes the phoneme from the default tab's chart; its page stays, for the systems that do reconstruct it.

On the site each proto-phoneme page has one tab per system. A system's tab shows its symbol and phonetic value. It shows its own reflexes only if `correspondences` has rows with that `system`; otherwise the reflexes are the default ones.

### `allophones.csv`

How a phoneme is realised, as the source describes it. **Wherever a source gives the allophones of a phoneme, they go here**, one row per allophone, so that the phoneme's page lists them (with their environments and sources) and the chart shows them on hover. This holds for every kind of inventory: a sourced phoneme, a generated or implied one, a proto-phoneme, a phoneme of another reconstruction system. Free variation and variation between speakers or generations are entered the same way, with the condition in `environment`. A single phonetic value (the source's [ħ] for a phoneme written h) is not an allophone: it belongs in the phoneme's place and manner, `source_symbol` or notes. The phoneme's `notes` may still say it in the source's words; the build warns when a phoneme row's notes describe realisations (`[ɣ] between vowels`, `allophone`, `free variation`, `realised`) and the phoneme has no row here.

| column | required | values |
|---|---|---|
| `lect_id` | yes | |
| `phoneme` | yes | the phoneme as it is in the lect's inventory (`ipa` of `phonemes.csv`, or the generated symbol), without `*` |
| `system` | | blank for the default system; a system name for a phoneme of that system (`notation_map`) |
| `allophone` | yes | the realisation, in IPA, without brackets: `ʃ`, `ɣ`, `t͡ʃ`. Include the elsewhere realisation when the source states it. |
| `environment` | | where it occurs, in the notation of `correspondences.environment` or in words: `_i`, `V_V`, `elsewhere`, `word-finally`, `free variation`, `younger speakers` |
| `source_id`, `page` | yes, `page` where known | the description that states it |
| `notes` | | |
| `via_source_id`, `via_page`, `via_note` | | as in the other tables |

```
lect_id,phoneme,system,allophone,environment,source_id,page,notes,...
duht1237,s,,ʃ,_i,tung1964,86,
duht1237,s,,s,elsewhere,tung1964,86,
```

A row whose phoneme is not in the lect's inventory is reported and not shown. (Added November 2026; a data folder without this table reads it as empty.)

### `decisions.csv`

A reading taken during data entry that the user has still to confirm: how a table was read, a classification chosen, a code corrected. One row per decision; rows of `correspondences` that depend on it name it in `decision`. The open ones are listed in `STATUS.md` and in the build's notes. To settle one, change its `status` in the sheet (and the rows, if the other reading wins), or write what should be done in `instructions`.

| column | required | values |
|---|---|---|
| `id` | yes | lowercase slug, e.g. `ge-helong-d` |
| `batch` | | the batch or source it came from |
| `question` | yes | what had to be decided |
| `chosen_reading` | | what was entered |
| `alternatives` | | the other reading(s) |
| `instructions` | | optional: the user's answer or directions, in their words, for the next data-entry session to carry out |
| `status` | yes | `open` · `confirmed` · `reverted` |
| `source_id`, `page` | | where the question arises |
| `notes` | | |
| `comments` | | optional: the user's comments on the decision, free text; read by the next session with `instructions`, and shown beside open decisions in `STATUS.md` |
| `applied` | | *optional last column (27 Nov 2026).* For a `reverted` decision: the date on which the reversal was carried out in the data (`2026-11-23`), with a word on what was done if that helps. Blank on a reverted decision means the work is still owed: the build warns, and `STATUS.md` lists it under *Reverted decisions not yet carried out*. |

---

## Layout v2 (November 2026)

Defaults the build fills in, so they are not typed row by row (restructuring plan, phase 1):

- `notation_map`: one default `canonical` row per lect (above).
- `lects.subgroup_path`: derived from `parent_id` + `clade`; filled only to override.
- `correspondences.as_printed` and `locator`: the printed statement and the table/figure reference, out of `notes`.
- Correspondence `id`s are frozen: every row has one, and a new row should get one (the build's report gives the hash it would use).

`tools/migrate_v2.py` rewrites tables to this layout and `--reverse` writes every default out again. Both layouts build the same site data; `tests/test_migration.py` checks that on the repository's tables. Row provenance is described by `derivation` (as-stated · composed · implied-retention), so there is no separate `basis` column.

## Layout v3 (November 2026)

Restructuring plan, phase 3:

- `lects.changes_only` became `inherit` (`TRUE` = `assumed-unchanged`), with `inherit_source_id`, `inherit_page`, `inherit_note`.
- 854 explicit X > X rows that said only "unchanged" are generated instead: 575 Grimes & Edwards identity rows at intermediate nodes (implied retentions) and 279 Billings & McDonnell rows "not among the nontrivial sets" (17 lects set to `stated-unchanged`). 32 such rows stay, because another row covers the same phoneme. The removed rows are kept in `data/migrations/v3_removed_correspondences.csv`.
- The `decisions` table, seeded with the open items of the handoffs, and `correspondences.decision`.
- `STATUS.md`, whose first part the build writes (`python3 build.py --check --status STATUS.md`).

`tools/migrate_v3.py` does the rewrite; `tests/test_migration_v3.py` checks that the build generates every removed row unchanged (lect, phonemes, environment, status, source, page) and that putting them back changes nothing the build derives.

A migration reaches the sheet through **Actions → Apply a migration to the sheet** (`sheet-apply.yml`, `tools/sheet_apply.py`): run it with `dry-run` to see the plan, then with `apply` and the number of rows to delete. It renames and adds columns, creates missing tabs, changes cells and deletes rows (each deleted correspondence must be in the archive file), never reorders rows, and fails unless a sync afterwards finds the sheet equal to `cldf/`. With `allow_append` (and an empty `archive`) it also appends the rows that follow the last matched row of each table, if their keys are new to the sheet: this is how a data edit that changes, deletes and adds rows at once reaches the sheet (`tools/batch_scripts/reverts_2026_11_23/`). Run it straight after merging such a pull request, before the hourly sync copies the sheet back over `cldf/`, and check that the dry run's counts are the ones expected.

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
- an implied phoneme of an attested lect could not be written in IPA, because the lect's own rows use that IPA symbol for another sound

**Notes:**

- unentered proto-phonemes per daughter
- generated phonemes sharing place + manner (possible allophones)
- free-text environments

Warnings added for citations and systems: a source that no phoneme, correspondence or notation row cites; a `notes` cell that says "quoted from" or "via" while `via_source_id` is empty; a system phoneme with no place or manner that cannot be inferred; a system with consonants but no vowel rows.

Also warned about: a proto-language not named `Proto-X` or an earlier stage not named `Pre-X`; and a work cited by author and year in any notes column (`Jackson (1983: 326)`, `Lee & Wang 1984`) that has no `sources` row, once per work, with the row where it is first mentioned.

## Output

The site loads a small file per lect, and a phoneme's history only when the phoneme is opened (restructuring plan, phase 4; the PAn page went from 5.1 MB of data to 34 KB). All files are compact JSON.

- `build/data/<lect_id>.json`: the basic information block; the derived inventory status and coverage; the inventory (each phoneme's symbol, chart position, origin and source, and `file`, the name of its own file); the other systems' phonemes (chart fields and counterparts); the changes that define the lect; the inventory diff for edited inventories.
- `build/data/<lect_id>/<code points>.json`, one per phoneme (`pan/0052.json` is PAn *R; code points keep the names ASCII and *R apart from *r on any file system): its `notation`, its `ancestry_graph`, its flattened `descendants` (each with a `via` path, which is what the pivoted index reads), and the full records of the other systems' phonemes that match it. A system phoneme with no counterpart in the default inventory has a file of its own (`pan/0072@Blust.json`).
- The lect list (`#/lects/`) names tree nodes without Proto- and Pre- (each lect's page keeps the full name, and the link's title gives it); alternative nodes (see `alt_parents`) are in italics, after the attested lects and established subgroups beside them, and can be hidden with the *Alternative nodes* switch.
- Sister nodes in the lect tree are listed by geography, not by name: by region from Taiwan through the Philippines, Borneo, Sumatra, Java, Sulawesi, the Lesser Sundas and Maluku, Halmahera, New Guinea and the Bismarcks, the Solomons, Micronesia, Vanuatu and New Caledonia to Fiji and Polynesia, and from north to south, then west to east, inside a region (`asc/geo.py`; index field `o`). A lect is placed by `latitude`/`longitude`, else by Glottolog's coordinates for its glottocode (`reference/glottolog_coordinates.csv`, used for this order only); a node by the region most of the lects under it are in. Add a new lect's glottocode to that file when it has no coordinates of its own.
- A link to a phoneme of another reconstruction system that has a descent of its own (`#/lects/pan/_ñ@Blust/`) opens a page for that phoneme alone, with the changes stated against it; its default-system counterparts are named at the top.
- A reflex that a row states and the lect's inventory lacks (not in the source's own list, or suppressed by hand; the build warns about each) is not added to the inventory, but it has a page: the lect file lists it under `stray_phonemes`, its file has its ancestry, the lect page lists it under *Reflexes outside this inventory*, and its own page carries the badge *not in the inventory* and a notice. Every link to a reflex therefore opens a page; `tests/test_output_size.py` checks this on the repository's data.
- A phoneme's file also has `implied_descendants` ({lect: [its phonemes]}): the implied retentions below the first level, which `descendants` leaves out. The table of all lects (`#/lects/?reflex=…`) shows them with the mark *implied*, so a lect or stage that keeps the sound without its source saying so reads as on its own page, not as *unentered*.
- The count beside the lect list is of lects (those with a page of their own) that pass the filter, whether or not their group is open; in a table of all lects it also gives how many have a reflex. *Hide lects with no data* is offered only while some lect has no data to hide. Each page sets its own browser title; an address the site does not have gives *Not found*.
- Over the lect list stands a map (`site/js/map.js`): a point for every attested lect with a page of its own and a known place, filled at the lect's own `latitude`/`longitude`, outlined at Glottolog's place for its glottocode (`reference/glottolog_coordinates.csv`); reconstructed stages and tree nodes have none. A click opens the lect's page; where several lects lie at one place a list opens. The map shows the lects the list's filter and *Hide lects with no data* leave, and the *Map* switch puts it away. It calls no map service: the coastlines are `site/land.json` (Natural Earth 1:10m, public domain; rewritten by `python3 tools/make_land.py land-10m.json`), drawn on a canvas with the Pacific in one piece. *Colour by subgroup* (Off, Taiwan, Malayo-Polynesian, Oceanic) colours the lects under Austronesian, Malayo-Polynesian or Oceanic by the daughter of that node they stand under in the tree, with a legend under the map: eight hues by five shapes, numbered in the tree's order; a daughter that is a single language shares the mark *etc.*; the lects outside the node, and the daughter with a mode of its own (Malayo-Polynesian, Oceanic), are grey. A legend entry picks its group out.
- Implied inheritance into an attested lect (`language`, `dialect`; `inherit` = `assumed-unchanged`, set or automatic, and no sourced inventory): the generated X > X row is written with the IPA symbol for the parent phoneme's value where the parent's letter is reconstruction orthography (*y > j, *ñ > ɲ, *e 'central mid' > ə, *j 'palatal affricate' > d͡ʒ; the table is `IMPLIED_IPA` in `asc/schema.py`), and no row is generated for *q, *R, *z or *N (`NOT_IMPLIED_IN_ATTESTED`): the lect file lists these as `not_implied`, and the lect page says they were not carried down. A row or a sourced inventory that states one of them is untouched. Where the lect's own rows already have that IPA symbol as the same sound (Habun's j from *z), the implied retention joins it; where they use it for another sound (the lect's rows write both y and j, or a phoneme row places the symbol elsewhere), the letter is kept and the build warns. The ligatures ʤ and ʧ are respelled d͡ʒ and t͡ʃ in the same way. Proto-languages and earlier stages keep the reconstruction's letters.
- A page's own state is in its address, so it can be linked: the lect list's filter and view (`#/lects/?q=tetun&view=flat`), a reflex table's *Only lects with a reflex* box (`&only=1`, which hides the lects and groups with no reflex entered or implied), a proto-language's reconstruction-system tab (`#/lects/pan/?system=Blust`) and the Segments search (`#/segments/?q=tʃ&view=segment&kind=attested`). The address is replaced as the reader types; it adds nothing to the history.
- The ancestry section opens with the history in one line (the regular line of descent, without the stages where nothing changes: *Proto-Central Pacific \*t, \*d, \*j > Proto-Polynesian \*t > Hawaiian k*). *Fold unchanged stages* takes out every stage in which each phoneme of the history continues one earlier phoneme unchanged (one parent, the same symbol, no condition, no fusion, nothing sporadic); the stage above a folded run is marked *⋯ n stages unchanged* (hover for their names, click to show them), and the list of steps under the diagram still has every step. It is on by itself when the history has more than five stages; the reader's choice is kept. *From* starts the diagram at a later stage.
- The ancestry section has a box *Regular changes only* where the history has sporadic, borrowed or doubtful steps: it hides them and the lines that reach the phoneme only through them. The choice is kept across pages.
- On the Segments page a search that matches a segment or feature words is not also matched against lect names.
- A tree node with no data of its own (a linkage, an agreed subgroup, a language whose dialects carry the rows and that has no `representative`) has a short page: its type, Glottocode, the node it is listed under, and its members as links (`pageNode` in `site/js/lect.js`). Links to such a node open that page.
- Several `regular` reflexes of one phoneme in one environment, from one source, with no condition (`conditioning` blank, no `lexical_scope`) are an *unconditioned split*: each row carries `split` (the number of reflexes) and the tag *one of n, no condition stated*; the build notes each group and `STATUS.md` counts them. Nothing in the rows is changed. Set `conditioning` `unknown` (or enter the condition) to settle one.
- In a descent table, rows that make the same statement (same lect, reflex, environment, status and tags) from different sources are one line with every citation; the table of all lects prints a repeated line once. A descent table is built for what is shown: the deeper rows are added when *Show deeper rows* is pressed, and only one layout (merged for lects, or a line per row) is in the page at a time.
- On a screen narrower than 640 px the ancestry diagram shortens the stage names (P- for Proto-, cut at 16 letters; the full name is the link's title).
- The lect list has its filter and switches first; the explanation is folded under *How to read this list*, and the map follows.
- `build/data/index.json`: what the lect list shows of each lect (name, alternate names, type, glottocode, parent, clade, coverage, status, overlapping groups); loaded on every page.
- `build/data/segments.json`: every lect's displayed inventory (default system), each distinct phoneme with its features written once (`seg`) and each lect listing indexes into it, with flags (implied, marginal) where they apply; loaded only by the Segments page (`#/segments/`), which lists and searches it by lect or by segment. Its search ignores tie bars (tʃ finds t͡ʃ) and reads a typed ? as ʔ.
- `build/data/map.json`: `points`, one `[lect id, latitude, longitude]` per mapped lect, with a fourth item `1` when the place is Glottolog's and not the lect's own; loaded only by the lect list.
- `build/data/sources.json`: what a citation link needs (id, label, author, year), loaded by every page; `build/data/sources_full.json`: the full bibliography with `reference` and `cited_by`, fetched only by the Sources page. `build/report.txt` keeps the last report.

### Marks in the charts

The inventory charts on lect pages use four marks, each for one thing, and the legend under a chart names those it uses:

| mark | means |
|---|---|
| *italic* | the source lists the phoneme but gives no place or manner; its position in the chart is read off the symbol (our inference, not the source's) |
| grey | implied: the lect's source lists only changes (`inherit` = `assumed-unchanged`) and does not mention this phoneme, so it is taken as kept from the parent |
| underline | no source gives the inventory: dotted = generated from the correspondences and placed from its symbol; double = placed by hand (`override`); solid = added by hand (`manual-add`) |
| (parentheses) | `status` `marginal` or `dubious` |

Blue is only the link colour. On a phoneme page, grey rows in the descent table are lects below a daughter (reached via the stage named under them) or implied retentions, and grey italic cells are blank reflexes; on the Segments page grey is implied and a wavy underline marks a symbol with no place or manner. No style changes the case of a symbol: `s` and `S` are different phonemes.

`tests/test_output_size.py` keeps the PAn lect file under 100 KB, and everything the PAn page fetches under 100 KB as served (gzip).

The viewer in `site/` (plain HTML/JS, no dependencies; `js/common.js`, then one script per page type, `js/main.js` last) is copied into `build/` and renders the three page types from that JSON with hash routes (`#/lects/`, `#/lects/<id>/`, `#/lects/<id>/<phoneme>/`, `#/lects/?reflex=pmp:R`). To preview with the fictional data:

```bash
python3 build.py --data tests/fixtures/example && python3 -m http.server 8765 --directory build
```

Then open http://localhost:8765.

## Editing in Google Sheets

The data is entered in the Google Sheet [Austronesian Sound Correspondences — data](https://docs.google.com/spreadsheets/d/1mzL8wYSb73PeuJShX-Xor7y6iIFDS991F9CV2AZD7mk/edit). It has one tab per table (`sources`, `lects`, `phonemes`, `correspondences`, `notation_map`, `allophones`, `decisions`), with the same headers, dropdowns for every fixed vocabulary, and every cell set to plain text. **The sheet is the source of truth: direct edits to `cldf/*.csv` are overwritten by the next sync.**

- `.github/workflows/sync-sheet.yml` runs every hour, or immediately from **Actions → Sync from Google Sheets → Run workflow**.
- It downloads the sheet (`tools/sync_sheet.py`), runs `build.py --check --status STATUS.md`, and, if the data passes and anything changed, commits `cldf/` and `STATUS.md` and redeploys the site.
- If a check fails, nothing is committed and the run fails. Errors read `tab.csv:ROW`, where ROW is the row in that tab of the sheet.
- The sheet must stay shared as "anyone with the link can view". Its id is stored in the repository variable `SHEET_ID` (Settings → Secrets and variables → Actions → Variables).
- `tools/make_sheet_template.py` regenerates the workbook (tabs, dropdowns, help tab) from `build.py`'s vocabularies, should the schema change. Re-upload it, or copy the changed dropdowns by hand.
- The sync also checks every Glottocode and ISO code against a pinned Glottolog release (`tools/check_glottolog.py`): a code Glottolog does not have, or an ISO code that belongs to a different languoid, stops the sync.
- GitHub often delays or skips scheduled runs, so "every hour" is a best case. Run the workflow by hand when an edit should appear at once.
- The sync is scheduled three times an hour (minutes 7, 27, 47), because GitHub delays and drops scheduled runs: with one slot an hour it ran 5 to 10 hours apart. After a sheet edit that should show at once, run **Actions → Sync from Google Sheets** by hand.
- GitHub pauses hourly schedules in repositories with no activity for 60 days. If that happens, re-enable the workflow in the Actions tab.

## Adding data in batches

Hand edits and a few new rows go straight into the sheet. A larger addition (one source read into many rows) goes through a pull request, and a workflow appends the rows to the sheet; the sheet stays the source of truth and the only place rows are changed.

1. Make a folder `data/incoming/<batch-id>/` (lowercase, e.g. `lobel2013`). Put in it one CSV per table you add to (`sources.csv`, `lects.csv`, `phonemes.csv`, `correspondences.csv`, `notation_map.csv`, `decisions.csv`), each with a header row of that table's columns, any order, unused columns left out, **new rows only**. Every correspondence needs an `id`. Add `BATCH.md`: source and pages read, scope, method, what was not entered. Readings that need the user's confirmation go into `decisions.csv` (and the rows that depend on them name it in `decision`); what is left to enter goes into `STATUS.md`.
2. Open a pull request. CI runs `python tools/batches.py check`: it checks the batch against `cldf/` (the sheet at the last sync), runs all of `build.py`'s checks on the combined data with errors pointing at `data/incoming/<batch-id>/<table>.csv:LINE`, and refuses a row whose key is already in the sheet with different content. Keys: `id` (sources, lects, correspondences, decisions), `lect_id`+`ipa` (phonemes), `lect_id`+`phoneme`+`system`+`symbol` (notation_map).
3. Merge. **Actions → Add batch to Google Sheets** (`push-batch.yml`) then syncs the sheet, checks again, appends the new rows below the last row of each tab (values written as plain text, exactly as in the CSV), syncs back, verifies that every row arrived unchanged, moves the folder to `data/batches/<batch-id>/` with the sheet rows noted in `BATCH.md`, commits and redeploys.

A tab whose grid ends at its last data row (as after a migration) gets new rows before the write. Running it again adds nothing: rows whose key is already in the sheet with the same content are skipped. If something in the sheet changed in between, so that the rows below the data are not empty or a key now has different content, the run stops before writing anything.

The workflow signs in with a Google service account: the repository secret `GOOGLE_SERVICE_ACCOUNT_JSON` holds its key file, and the sheet is shared with the account's address as Editor. To test the setup, run the workflow by hand with mode `auth-check`; it signs in, reads the tabs, and rewrites the `sources!A1` header with its own value.

This replaces the earlier route of uploading an .xlsx to Drive and copying tabs into the sheet.

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
- `pycldf` isn't required yet; the build uses only the standard library. `cldf-metadata.json` describes every table and column (`python3 tools/make_metadata.py` after a schema change; a test compares it with `asc/schema.py`) and is in place so `pycldf`/`cldf validate` can read the dataset later, and ABVD/ACD `forms`/`cognates` tables can be added beside it.
