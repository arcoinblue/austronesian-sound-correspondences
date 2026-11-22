# lynch2002

Lynch, John, Malcolm Ross & Terry Crowley. 2002. *The Oceanic languages*. Richmond, Surrey: Curzon Press (read in the 2011 Routledge paperback, same pagination). Read from the PDF in the user's Downloads folder. Generator: `tools/batch_scripts/lrc2002/` (one file per sketch in `langs/`).

## Scope

- **The 43 grammar sketches, section 1 (phonology).** For each: the phoneme inventory (`phonemes`, origin `sourced`) and every allophone the section states (`allophones`). Each sketch is its own `sources` row, a chapter with its author (the adapter where the sketch is "adapted" or "abstracted"), with a year suffix in book order where an author has several (Ross 2002a-k, Crowley 2002a-h, Lynch 2002a-g, Early 2002a-b).
- **Ch. 4, Proto Oceanic (p. 64):** the probable phonetic values of POc phonemes as allophones (labio-velars as double articulations, prenasalised voiced obstruents, *[ɸ β], *[x ɣ], *[z] as allophones of *p, *k, *s), cited to the book (`lynch2002`).
- **New lects (39):** 35 sketch languages that were not in the database, plus language nodes where Glottolog has the described variety as a dialect: Taiof (dialect taio1240) is listed as a language, as the sketch treats it; Sakao keeps the Ross et al. (2023) code port1296; Nadrogā is a dialect under a new language node Western Fijian (west2519, representative Nadrogā); Mele (mele1251) is a dialect under the existing Mele-Fila (mele1250). Coordinates come from `reference/oceanic_metadata.csv` (Ross et al. 2023).
- **Existing lects that get a sourced inventory:** Teanu (Buma), Mwotlap, Ulithian, Puluwatese, North Marquesan (the sketch describes Nukuhiva).
- **Parents:** POc for Western Oceanic, Admiralties and Southeast Solomonic languages; Proto-North-Central Vanuatu for Sakao, Tamambo, Raga, Vinmavis, Port Sandwich, Southeast Ambrym, Lamen; Proto-New Caledonian for Cèmuhî, Xârâcùù, Iaai; POc with tree parent Southern Oceanic for Sye and Anejom̃; Proto-Nuclear Polynesian for Niuafo'ou and Mele; POc for Rotuman and Nadrogā (Central Pacific linkage, no node).
- **Correspondences:** only the four historical statements of the Nadrogā sketch (*t > s before i, e; *t > tʃ before u; *ⁿd > ⁿdʒ before i, u; *s > h), against POc (decision `lrc2002-nadroga`).

## Decisions (open)

- `lrc2002-readings`: IPA where the sketch's symbol is ambiguous (j as ɟ; Tobati /~/ as ŋ; Kairiru q as k̠; Kele lax vowels; which long vowels are phonemes).
- `lrc2002-nadroga`: the unnamed proto-language of the Nadrogā statements read as POc.
- `lrc2002-subgroups`: the Ch. 5 subgroup-defining changes (Admiralties *R, Southeast Solomonic *l = *R, Papuan Tip *k and *ñ, Micronesian *bʷ and *mʷ splits) are not entered as nodes.

## Checks

`batches.py check`: 0 errors, 280 warnings (276 on main). The four new warnings are reflexes from Bender et al. (2003) that are written in the practical orthography and so are not in the new sourced inventories: Ulithian b, g, th (the sketch's /βʷ/, /x/, /ð/) and Puluwatese R. They are left as they are; respelling the Bender rows is a sheet edit for the user to decide (see the handoff).

## Not entered

- Morphology, syntax and the rest of each sketch; stress and phonotactics except where they state an allophone.
- Vowel length where the sketch only says that length is phonemic, and tones (Jabêm, Cèmuhî).
- The PMP > POc correspondences of Ch. 4 (already in the database from Ross et al. 2023).
- Historical remarks given as examples rather than rules (Mussau echo vowels, Rotuman vowel developments, Mwotlap r > y since 1885, inland Takia l = r): kept in the lect notes.
- Works cited in passing in the sketches have no sources row; the notes name them without a year.
