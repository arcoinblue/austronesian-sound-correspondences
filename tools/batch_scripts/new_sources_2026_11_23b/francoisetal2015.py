"""Batch francoisetal2015-vanuatu: The languages of Vanuatu: Unity and diversity (2015), read for this project.

François, Alexandre, Sébastien Lacrampe, Michael Franjieh & Stefan Schnell (eds.). 2015. The languages of
Vanuatu: Unity and diversity (Studies in the Languages of Island Melanesia 5). Canberra: Asia-Pacific
Linguistics. The PDF's text layer is in a shifted font encoding; it was decoded (each ASCII character + 29)
and searched for phonological content.

Only a sources row: the volume has no correspondence tables or phoneme inventories (decision francoisetal2015-scope).

    python3 tools/batch_scripts/new_sources_2026_11_23b/francoisetal2015.py
"""
from common import write

S = "francoisetal2015"
BATCH = "francoisetal2015-vanuatu"

SOURCES = [dict(
    id=S, author="François, Alexandre; Franjieh, Michael; Lacrampe, Sébastien; Schnell, Stefan", year="2015",
    title="The exceptional linguistic density of Vanuatu: Introduction to the volume", kind="comparative",
    pub_type="chapter", container_title="The languages of Vanuatu: Unity and diversity",
    editors="Alexandre François; Sébastien Lacrampe; Michael Franjieh; Stefan Schnell", place="Canberra",
    publisher="Asia-Pacific Linguistics", series="Studies in the Languages of Island Melanesia 5",
    notes="Consulted directly on 23 November 2026: the whole volume (270-page PDF; the text layer is in a shifted font "
          "encoding and was decoded for searching). The introduction and ten chapters are on morphosyntax, numerals, "
          "space systems, dialect documentation and oral narratives (Pearce on Unua, Budd on Bierebo, Touati on Sakao, "
          "Franjieh on North Ambrym, Garde on Sa numerals, François on Torres-Banks space systems, Schneider & Gray "
          "on Suru Kavian, Jauncey on Tamambo, Thieberger on Erromango). No table of sound correspondences and no "
          "phoneme inventory: Garde's chapter mentions in passing Raga-Sa correspondences in the numerals, an f kept "
          "only in some numerals and in four northern villages, and [t] palatalised to [c] before high vowels in all "
          "Sa dialects but that of Baie Martelli; Budd's Table 3 lists Bierebo reflexes of POc verbs. Cited here for "
          "the volume, whose chapters are not otherwise entered.")]

DECISIONS = [dict(
    id="francoisetal2015-scope", question="The languages of Vanuatu: Unity and diversity (2015) was read for this "
    "project. Is anything entered from it?",
    chosen_reading="Only a sources row. Its phonological remarks are incidental (Garde on Sa f and [t] > [c] before "
                   "high vowels; Budd's Bierebo reflexes of individual POc verbs) and concern lects that are not in "
                   "the data (Sa, Bierebo).",
    alternatives="Add Sa (saaa1241) with the allophone [c] of /t/ before high vowels and a note on f.",
    status="open", source_id=S, page="")]

MD = f"""# {BATCH}

François, Alexandre, Sébastien Lacrampe, Michael Franjieh & Stefan Schnell (eds.). 2015. *The languages of Vanuatu: Unity and diversity* (Studies in the Languages of Island Melanesia 5). Canberra: Asia-Pacific Linguistics. Generator: `tools/batch_scripts/new_sources_2026_11_23b/francoisetal2015.py`.

## Scope

- A sources row for the introduction (standing for the volume) recording what was read; no data rows (decision `francoisetal2015-scope`).
"""

write(BATCH, dict(sources=SOURCES, decisions=DECISIONS), MD)
