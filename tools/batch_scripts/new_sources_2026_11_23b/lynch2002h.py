"""Batch lynch2002h-labiovelars: Lynch (2002), the POc labiovelars.

Lynch, John. 2002. The Proto-Oceanic labiovelars: Some new observations. Oceanic Linguistics 41(2).
310-362. Read from the Project MUSE PDF in Downloads (Table 3 read from a page image).

    python3 tools/batch_scripts/new_sources_2026_11_23b/lynch2002h.py
"""
from common import write

S = "lynch2002h"
BATCH = "lynch2002h-labiovelars"

SOURCES = [
    dict(id=S, author="Lynch, John", year="2002", year_suffix="h",
         title="The Proto-Oceanic labiovelars: Some new observations",
         url_or_doi="https://doi.org/10.1353/ol.2002.0009", kind="comparative", pub_type="article",
         container_title="Oceanic Linguistics", volume="41", issue="2", pages="310-362",
         notes="Consulted directly on 23 November 2026 (Project MUSE PDF; Table 3 read from a page image). "
               "Descriptions of labiovelars (Table 1), secure POc reconstructions with labiovelars (Table 2), sample "
               "reflexes in eleven languages with PEOc fortis *p and lenis *v (Table 3, p. 315), theories of origin "
               "(contact, conditioning, unrecognised precursor), phonotactic distribution and crossover (§3.3), "
               "conditioning by an adjacent rounded vowel with a post-velar (§5.2) or initial *u (§5.3), "
               "disambiguation and functional load (§6), with an appendix of cognate sets. Year suffix h: Lynch's "
               "grammar sketches in Lynch et al. (2002) are 2002a-g."),
    dict(id="lynch2000a", author="Lynch, John", year="2000", year_suffix="a", title="A grammar of Anejom̃",
         kind="grammar", pub_type="book", place="Canberra", publisher="Pacific Linguistics",
         notes="Bibliographic details from the references of Lynch (2002h) and Lackey & Boerger (2021). Not "
               "consulted directly; cited for the Anejom̃ allophone of /a/ next to labiovelars (p. 19)."),
]

ALLO = [dict(lect_id="anei1239", phoneme="a", allophone="ɒ", environment="next to a labiovelar",
             source_id="lynch2000a", page="19", via_source_id=S, via_page="311",
             notes="Normally [a], backed and rounded next to labiovelars.")]

DECISIONS = [dict(
    id="lynch2002h-table3", question="Lynch (2002h) Table 3 gives sample reflexes of the POc labials and "
    "labiovelars in eleven languages. Which are entered?",
    chosen_reading="None for now. Mota, the one column not yet covered, cannot be restated against PNCV, "
                   "whose inventory in the data has no labials (PNCV has neither consonant rows nor inherit): Mota "
                   "*bʷ ᵏpʷ, *b p, *pʷ v (w), *p p (fortis) and v (w) (lenis), *mʷ mʷ, *m m wait for PNCV's "
                   "consonants (Clark 2009). Anejom̃, Nemi and Pohnpeian already have "
                   "these correspondences from Lynch (2001), Haudricourt & Ozanne-Rivierre (1982) and Bender et "
                   "al. (2003); Tongan is left out because the data has no PPn rows for the labiovelars to restate "
                   "it against; Loniu, Manam, Dobu, Lau and Wayan are not in the data.",
    alternatives="Add Lynch's crossover reflexes (Nemi ᵐbʷ for *bʷ, mʷ for *mʷ; Pohnpeian pʷ for *b) as sporadic "
                 "rows; add a Proto-Eastern Oceanic node with fortis *p and lenis *v.",
    status="open", source_id=S, page="315")]

MD = f"""# {BATCH}

Lynch, John. 2002h. The Proto-Oceanic labiovelars: Some new observations. *Oceanic Linguistics* 41(2). 310-362. Generator: `tools/batch_scripts/new_sources_2026_11_23b/lynch2002h.py`.

## Scope

- Anejom̃ allophone [ɒ] of /a/ next to labiovelars (Lynch 2000a: 19, via p. 311).

## Not entered

- Table 3 (see decision); the cognate sets of Tables 2, 4-9 and the appendix; the conditioning statements of §5, which are tendencies stated on etyma, not regular changes. The PSV change *b, *m > *bʷ, *mʷ before *u (p. 322) is already in the data from Lynch (2001), the PMc split (Jackson 1986: 204) from Bender et al. (2003).

## Decisions (open)

- `lynch2002h-table3`.
"""

write(BATCH, dict(sources=SOURCES, allophones=ALLO, decisions=DECISIONS), MD)
