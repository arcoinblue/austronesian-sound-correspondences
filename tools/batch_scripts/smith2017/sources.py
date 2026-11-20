"""Source rows for the Borneo batches. Details from the works' own title pages and
from the reference lists of Smith (2023) and Smith (2025)."""

SRC_COLS = ["id", "author", "year", "title", "url_or_doi", "kind", "notes", "year_suffix", "pub_type",
            "container_title", "editors", "volume", "issue", "pages", "place", "publisher", "series", "edition"]

def row(**kw):
    r = {c: "" for c in SRC_COLS}
    r.update(kw)
    return r

SOURCES = [
    row(id="smith2017a", author="Smith, Alexander D.", year="2017", year_suffix="a",
        title="The languages of Borneo: A comprehensive classification", kind="comparative",
        pub_type="thesis", place="Honolulu", publisher="University of Hawaiʻi at Mānoa dissertation",
        notes="Title page: May 2017. Chapter 2 gives, for each subgroup, tables of PMP reflexes in its member "
              "languages; a phoneme 'is not included in the sound correspondence table' where no language of "
              "the subgroup changed it (p. 50). Most data are the author's own fieldwork. The a/b/c suffixes on "
              "Smith 2017 are assigned in this database (alphabetical by title); Smith's own lists differ."),
    row(id="smith2017b", author="Smith, Alexander D.", year="2017", year_suffix="b",
        title="Merap historical phonology in the context of a central Bornean linguistic area",
        url_or_doi="https://www.jstor.org/stable/26408527", kind="comparative", pub_type="article",
        container_title="Oceanic Linguistics", volume="56", issue="1", pages="143-180",
        notes="Merap (Langap village, Malinau River) from the author's fieldwork; reconstructions are to "
              "Proto-Kayanic (p. 162)."),
    row(id="smith2017c", author="Smith, Alexander D.", year="2017", year_suffix="c",
        title="The Western Malayo-Polynesian problem", url_or_doi="https://doi.org/10.1353/ol.2017.0021",
        kind="comparative", pub_type="article", container_title="Oceanic Linguistics", volume="56", issue="2",
        pages="435-490",
        notes="Argues that Western Malayo-Polynesian is not a subgroup. No sound correspondences are entered "
              "from it."),
    row(id="smith2023", author="Smith, Alexander D.", year="2023",
        title="Evidence and models of linguistic relations: Subgroups, linkages, lexical innovations, and Borneo",
        url_or_doi="https://doi.org/10.1353/ol.2023.a913564", kind="comparative", pub_type="article",
        container_title="Oceanic Linguistics", volume="62", issue="2", pages="324-365",
        notes="Argues that the lexical evidence for Greater North Borneo and the Barito-Basap linkage does not "
              "justify those groups. No sound correspondences are entered from it."),
    row(id="smith2025", author="Smith, Alexander D.", year="2025",
        title="Late Malayo-Polynesian: A new model of Austronesian linguistic relations",
        url_or_doi="https://doi.org/10.1075/dia.23062.smi", kind="comparative", pub_type="article",
        container_title="Diachronica", volume="42", issue="5", pages="646-698",
        notes="Proposes a dialect network ('Late Malayo-Polynesian') in place of higher-order Malayo-Polynesian "
              "subgroups. No sound correspondences are entered from it."),
    ]
LOBEL = [
    row(id="lobel2013", author="Lobel, Jason William", year="2013",
        title="Philippine and North Bornean languages: Issues in description, subgrouping, and reconstruction",
        kind="comparative", pub_type="thesis", place="Honolulu",
        publisher="University of Hawaiʻi at Mānoa dissertation",
        notes="Title page: May 2013. Chapter 11 is a version of Lobel's 'Southwest Sabah revisited' "
              "(Oceanic Linguistics 52, 2013), which Smith (2017a) cites as a separate 2013 work."),
]
