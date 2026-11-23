"""Batch nc-north-1993-1995: Rivierre (1993) and Ozanne-Rivierre (1995), read but held (sources row and decisions).

Rivierre, Jean-Claude. 1993. Tonogenesis in New Caledonia. In Jerold A. Edmondson & Kenneth J. Gregerson (eds.),
  Tonality in Austronesian languages (Oceanic Linguistics Special Publication 24), 155-173. Honolulu: University of
  Hawai'i Press.

    python3 tools/batch_scripts/new_sources_2026_11_23c/nc1993.py
"""
from common import write

SOURCES = [dict(
    id="rivierre1993", author="Rivierre, Jean-Claude", year="1993", title="Tonogenesis in New Caledonia",
    url_or_doi="https://www.jstor.org/stable/20006754", kind="comparative", pub_type="chapter",
    container_title="Tonality in Austronesian languages", editors="Edmondson, Jerold A.; Gregerson, Kenneth J.",
    series="Oceanic Linguistics Special Publication 24", pages="155-173", place="Honolulu",
    publisher="University of Hawai'i Press",
    notes="Consulted directly on 23 November 2026 (JSTOR PDF). High tone in Cèmuhî and Paicî (Centre North) and in Drubea, "
          "Numèè and Kwênyii (Far South) comes from aspirated consonants that already existed in Proto-Mainland, themselves "
          "from geminates produced by syllable reduplication (§§2-3, Figures 1-3). Not entered as rows yet (decision "
          "rivierre1993-tones).")]
DECISIONS = [
    dict(id="rivierre1993-tones", question="Rivierre (1993) derives the high tone of Cèmuhî, Paicî, Drubea, Numèè and Kwênyii "
         "from aspirated consonants (from PNC geminates). Is it entered?",
         chosen_reading="Not yet. The data has no tone phonemes for these languages, and the rows would be PNC geminate > "
                        "plain consonant with a high tone on the vowel, which the correspondence table cannot write as one "
                        "segment; the Cèmuhî reflexes are given language by language in Ozanne-Rivierre (1995, Appendices "
                        "1-6), which waits for the Proto-North node (decision ozannerivierre1995-north).",
         alternatives="Enter the geminate rows with the tone in the note.", status="open", source_id="rivierre1993",
         page="155-173"),
    dict(id="ozannerivierre1995-north", question="Ozanne-Rivierre (1995) reconstructs Proto-North (Bril's PNNC) with *k > *c, "
         "*q > *k, *t > alveolar *t and *s > *t, aspirates from PNC geminates, and the subgroups of her Figure 1, with "
         "reflexes by language in Appendices 1-6. Is it entered?",
         chosen_reading="Not yet: a Proto-North node means restating every northern New Caledonian row (Bril 2020, "
                        "Haudricourt & Ozanne-Rivierre 1982, Ozanne-Rivierre 1992) against it, which is the open decision "
                        "bril2020-pnnc; the appendices' OCR text loses the diacritics and must be read from the page images. "
                        "Read and recorded in the sources row.",
         alternatives="Add Proto-North and the Figure 1 subgroups, restating the northern rows.", status="open",
         source_id="ozannerivierre1995", page="45-72")]
MD = """# nc-north-1993-1995

Rivierre (1993) and Ozanne-Rivierre (1995) were read on 23 November 2026. Only a sources row (Rivierre 1993) and two open decisions (`rivierre1993-tones`, `ozannerivierre1995-north`) are added; Ozanne-Rivierre's sources row is updated by the migration `tools/batch_scripts/smith2023_nodes/apply.py`. Generator: `tools/batch_scripts/new_sources_2026_11_23c/nc1993.py`.
"""
write("nc-north-1993-1995", dict(sources=SOURCES, decisions=DECISIONS), MD)
