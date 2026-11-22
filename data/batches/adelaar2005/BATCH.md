# adelaar2005

Adelaar, Alexander. 2005. Malayo-Sumbawan. *Oceanic Linguistics* 44(2). 357-388. Read from the PDF in the user's Downloads folder; the text layer uses a font in which ə, ŋ and ʔ come out as º, ¥ and ¿, so the lists were checked on the page images (pp. 373-376). Generator: `tools/batch_scripts/adelaar2005/build.py`.

## Entered

Section 4 lists, for each language, its phonological developments from PMP. Each item is entered as one or more correspondences, with `locator` "§4, item n":

- **Proto-Chamic** (cham1330), after Thurgood (1999). Source `thurgood1999`, via Adelaar (2005: 373-374).
- **Proto-Balinese-Sasak-Sumbawa** (bali1277), after Mbete (1990), via Adelaar (p. 374). The PBSS reflexes of *-ay and *-aw are Adelaar's own (*-ey, *-ow; p. 359), so those rows cite `adelaar2005` directly.
- **Balinese, Sasak, Sumbawa**, under PBSS, after Mbete (1990), via Adelaar (pp. 374-375). The Balinese reflexes of *r (∅ initially and medially, h finally) are from Adelaar's section 2 (p. 364).
- **Javanese, Sundanese, Madurese**, under PMP, after Nothofer (1975), via Adelaar (pp. 375-376).
- All eight lects have `inherit` assumed-unchanged. Where a phoneme's other rows have unknown conditioning, or where its symbol differs between the parent's orthography and IPA (PMP schwa e, written ə in PC and PBSS; y, ñ and PBSS *j in attested lects), the retention is entered as an explicit implied-retention row.
- `notation_map` canonical rows for PC and PBSS; a `phonemes` override places PBSS *e (from *-ay) as a mid front vowel.
- Sources: `adelaar2005`, `thurgood1999`, `mbete1990`, `nothofer1975` (the last three not consulted directly).

## Decisions (open)

- `adelaar2005-ms`: the Malayo-Sumbawan subgroup is not entered as nodes.
- `adelaar2005-unconditioned`: unconditioned splits and alternatives are entered as rows with unknown conditioning; items with no stated outcome, or that are not segmental, go in the lect notes.

## Not entered

- Cluster reduction, nasal assimilation, homorganic nasal accretion, vowel contraction, Madurese fortition of *w and *y, the Madurese retroflex series and gemination, and Balinese schwa assimilation: all in the lect notes.
- Adelaar's 14 Malayic developments (Table 1): Proto-Malayic is already in the database (Smith 2017a).
- The lexical, formal and numeral evidence (§§6-7).

## Checks

`batches.py check`: 0 errors, 280 warnings (as on main). The generated inventories of all eight lects were listed from a local build and checked against the lists.


## Applied

2026-11-22 14:57 UTC, by the push-batch workflow.
- sources: sheet rows 219-222
- lects: sheet rows 944-951
- phonemes: sheet rows 4072-4072
- correspondences: sheet rows 9285-9460
- notation_map: sheet rows 519-520
- decisions: sheet rows 140-141
