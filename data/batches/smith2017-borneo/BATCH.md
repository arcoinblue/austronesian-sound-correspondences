# Batch smith2017-borneo

Source: Smith, Alexander D. 2017. *The languages of Borneo: A comprehensive classification* (University of Hawaiʻi dissertation), chapter 2, read from the PDF (text layer checked against page images for the tables used). Merap consonants from Smith (2017), "Merap historical phonology in the context of a central Bornean linguistic area", *Oceanic Linguistics* 56(1), §4 (pp. 162-166).

Also added as sources, with no correspondence rows: Smith 2017 "The Western Malayo-Polynesian problem", Smith 2023 "Evidence and models of linguistic relations", Smith 2025 "Late Malayo-Polynesian". They argue about higher-order groupings (decision `smith-higher-order`). Their three "never cited" warnings are expected.

The user asked for the papers not to be taken as fact but assessed critically, with only safe information entered. That shaped every choice below, and each reading that needs confirmation is a `decisions` row.

## Scope

54 lects, 1,563 correspondence rows.

| Subgroup | Nodes | Member lects (rows from) |
|---|---|---|
| Kayanic (§2.2) | Proto-Kayan, Proto-Murik-Merap, Proto-Segai-Modang, each under PMP (Proto-Kayanic and Proto-Kayan-Murik-Merap held back: decision `kayanic-held`) | Long Naah, Data Dian, Balui Liko, Busang, Bahau (Tables 3-4); Ngorek (Tables 8-9); Merap (Smith 2017 Merap paper, consonants); Modang, Long Gelat, Gaai, Kelai (Tables 14-15) |
| Kajang (§2.3.1) | Proto-Kajang | Sekapan, Kejaman, Lahanan (Tables 24-25) |
| Melanau (§2.3.2) | Proto-Melanau | Kanowit, Dalat, Mukah, Balingian, Sarikei, Matu (Tables 26-27) |
| Punan (§2.4) | Proto-Punan (Table 31) | Punan Tubu, Punan Bah, Punan Aput, Beketan, Ukit (Tables 29-30) |
| Müller-Schwaner (§2.5) | Proto-Müller-Schwaner (Table 39, Figure 31) | Seputan, Kereho, Hovongan (Tables 37-38) |
| Land Dayak (§2.6) | Proto-Land Dayak → Proto-Benyadu-Bekati, Proto-Bidayuh-Southern Land Dayak | Benyadu, Bekati, Hliboi, Sungkung, Jangkang, Ribun, Sanggau, Golik (Table 50; vowels from Table 52) |
| Malayic (§2.8) | Proto-Malayic | Indonesian, Ketapang Malay, Keninjal, Kendayan, Seberuang, Iban (Upper Kapuas), Mualang (Tables 59-60) |

## Method

- **Nodes.** Each proto-language is entered from Smith's own change list or reconstruction table: Table 23, Figures 10 and 18, Figure 23, Table 31, Table 39 with Figure 31, Table 52 with Figure 42. Its parent is PMP or the node above. Where the text and a figure disagree, the text's final argument is followed (decision `pkmm-glottal`). Where a cell is printed with "?" or hedged in the text, it is entered as disputed (decision `pkay-table23`).
- **Member lects.** Smith's tables give PMP > language. Each row is restated against the lect's nearest node: the PMP phoneme is followed through the node changes (`tools/batch_scripts/smith2017/` (`lib.compose()`); the scripts that wrote this batch are there). `as_printed` keeps the table cell, for example `*-b- > v; b / ə_`.
- **Smith's cell notation** (p. 52): the first reflex is regular. A reflex after a semicolon is "conditioned or irregular": entered as sporadic, or as regular in the printed environment where the cell or text gives one. Parenthesized reflexes are sporadic. Where a cell has three or more reflexes and no conditions, only the first is entered, unless the text states the conditions (decision `smith-semicolon`).
- **Positions.** `*b-` is `#_`, `*-b-` is `V_V`, `*-b` is `_#`. `*-aC` is `_C#`, `*-a` is `_#`, `*-aCVC` is `penultimate syllable`. Diphthongs (`*-ay`, `*-aw`) use the fusion encoding.
- **What is not listed.** Smith's tables list only phonemes that changed somewhere in the subgroup (p. 50), so the member lects are `stated-unchanged`, citing p. 50. Where a lect's rows cover only some positions of a phoneme, the remaining positions are explicit stated retentions (482 rows). Merap has no `inherit`: its vowels are not entered.
- **IPA.** Smith's j, c, ñ, y (p. 26) and Latin g are written in IPA in attested lects, d͡ʒ t͡ʃ ɲ j ɡ, with `source_form`. A final c is the palatal stop c. Proto-nodes keep Smith's spelling. *z > *j is entered as a respelling, not a change, as Smith says (p. 26).
- **Glottocodes** from Glottolog 5.4, matched by name and checked against the membership of the clade. Three Land Dayak varieties (Hliboi, Sungkung, Golik) and Ketapang Malay have no languoid and keep slugs. Decision `kayanic-glottocodes` lists the matches that needed judgement.

## Critical assessment: what was left out or flagged

- **The rule the user set (20 Nov):** add correspondence tables and the reconstructions of established microgroups, but hold back the intermediate reconstructions above them.
  - Proto-Kayanic (Table 23) and Proto-Kayan-Murik-Merap (§2.2.4.1) are therefore not nodes. Their changes are restated on Proto-Kayan, Proto-Murik-Merap and Proto-Segai-Modang, marked `composed` (`kayanic-held`).
  - Smith himself finds no phonological evidence for Kayanic (p. 86).

- **Higher-order groupings are not nodes:** North Borneo, Greater North Borneo, Central Sarawak, North Sarawak, Basap-Barito, Western Indonesian, Late MP (`smith-higher-order`). Smith himself later rejects the lexical evidence for Greater North Borneo and Barito-Basap (2023).
- **Not entered as nodes because the evidence conflicts:** Punan internal subgroups (`punan-internal`), Malayic lower groups (defined by changes in single lexemes), Segai and Modang, and the Bidayuh and Southern Land Dayak branches.
- **Proto-Melanau** has only the two changes Smith calls "likely" (`melanau-node`).
- **Proto-Malayic:** Smith gives no change list, so its rows are the reflexes shared by all seven lects, marked `composed` (`pmal-shared`).
- **Phonetic forms in tables.** Malayic tables print some forms phonetically (ɣ, ɹˠ, ow, ɪə̯) that the text calls allophones of /r/, /u/, /i/; they are entered as phonemes (`malayic-r`, `malayic-phonetic`). Kajang ɮ is allophonic and is entered once, at Proto-Kajang.
- **Contradictory or unclear cells, left out:**
  - Ngorek *nj, which is nc in Table 8 and nj in Table 11 (`ngorek-nj`).
  - Table 4's *-aʔ row and the vowel-length history of Figures 11-12 (`pkmm-glottal`).
  - Land Dayak Table 51, whose slashes are unexplained.
  - The Bidayuh column of Table 50.
  - Optional prenasalization such as (n)t (`landdayak-tables`).
- **Inferred:** Proto-Segai-Modang *j > *c (`psm-j`), needed to keep *z apart from *-y-.
- **Merap vowels** are not entered (reverse umlaut and stress shift; Smith 2017 Merap paper §4.10-4.14).

## Not entered (next sessions)

- Smith 2017a §2.7 Barito, a linkage with no node (Tables 56-57).
- §2.9 Basap (Tables 67-68).
- §2.10 Sabah: Dusunic, from Lobel; Northeast Sabah and Molbog (Tables 69-72).
- §2.11 North Sarawak: Dayic (Tables 74-75), Berawan-Lower Baram (Tables 77-78), Bintulu (Table 80), Kenyah (no table; refers to Smith 2015).
- Smith 2017a Table 51 and the Hliboi, Kelai, Merap and Punan Bah inventories (Tables 12-13, 19-20, 36, 54-55).
- Lobel 2013 entirely: Proto-Subanen (ch. 10) is stated against Proto-Greater Central Philippine, which is not in the database. Southwest Sabah (ch. 11, Dusunic and Murutic) is stated against Proto-Southwest Sabah. Manide and Inagta Alabat (ch. 8).


## Applied

2026-11-20 09:10 UTC, by the push-batch workflow.
- sources: sheet rows 75-79
- lects: sheet rows 564-619
- phonemes: sheet rows 717-717
- correspondences: sheet rows 3433-4970
- notation_map: sheet rows 408-420
- decisions: sheet rows 30-45

2026-11-20 09:35 UTC, restructured in the sheet by hand (Sheets connector), after the user's rule on intermediate stages: Proto-Kayanic and Proto-Kayan-Murik-Merap deleted from lects (rows 564-565), notation_map (408-409) and correspondences (22 rows); Proto-Kayan, Proto-Murik-Merap and Proto-Segai-Modang reparented to PMP; 47 composed rows appended (correspondences 4949-4995); the PKMM e override moved to Proto-Kayan and Proto-Murik-Merap; decision `kayanic-held` added and `pkay-table23`, `pkmm-glottal` updated. The files here are the restructured batch.

2026-11-20, Proto-Malayic: its six composed rows (pmal-shared) deleted from the sheet by hand (correspondences 4714-4719) and the node's note and decision updated; the Table 59-60 rows they stood for go on each lect through batch `smith2017-malayic`. The files here include them.
