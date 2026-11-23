"""Batch ross1996-yapese: Ross (1996), POc > Yapese (Set C, the inherited stratum).

Ross, Malcolm. 1996. Is Yapese Oceanic? In Bernd Nothofer (ed.), Reconstruction, classification,
description: Festschrift in honor of Isidore Dyen, 121-166. Hamburg: Verlag Meyer & Co.
Read from the scan in Downloads (OCR text layer; Tables 2 and 3 read from page images at 300 dpi).
The scan has no printed page numbers; pages are given as 120 + the PDF page (the chapter runs 121-166).

    python3 tools/batch_scripts/new_sources_2026_11_23/ross1996.py
"""
from common import write

S = "ross1996"
L = "yape1248"
BATCH = "ross1996-yapese"
T2 = "129"  # Table 2 (PDF p. 9)

SOURCES = [dict(
    id=S, author="Ross, Malcolm", year="1996", title="Is Yapese Oceanic?", kind="comparative", pub_type="chapter",
    container_title="Reconstruction, classification, description: Festschrift in honor of Isidore Dyen",
    editors="Bernd Nothofer", pages="121-166", place="Hamburg", publisher="Verlag Meyer & Co.",
    notes="Consulted directly on 23 November 2026 (scan without printed page numbers; pages here are counted from "
          "p. 121, so Table 2 is p. 129 and Table 3 p. 131). Table 1, PMP > POc (p. 123); Table 2, Yapese, Palauan, "
          "PMc, Ulithian and Woleaian reflexes of PMP and POc consonants in five strata, Sets A-D and UW (p. 129); "
          "Table 3, origins of Yapese consonants (p. 131); bound morphemes (§2.2) and the position of Yapese "
          "(§2.3). Yapese data from Hsu (1969) and Jensen (1977a, 1977b), transcribed by Ross into 'a more or less "
          "self-evident orthography' (n. 3); POc in the orthography of Ross (1988) (n. 4). Publication details from "
          "the TLOPO bibliography."),
    dict(id="hsu1969", author="Hsu, Robert Wen", year="1969", title="Phonology and morphophonemics of Yapese",
         kind="grammar", pub_type="thesis", publisher="University of California, Berkeley dissertation",
         notes="Bibliographic details from the reference list of Ross (1996). Not consulted."),
    dict(id="jensen1977a", author="Jensen, John Thayer", year="1977", year_suffix="a", title="Yapese reference grammar",
         kind="grammar", pub_type="book", place="Honolulu", publisher="University Press of Hawaii",
         notes="Bibliographic details from the reference list of Ross (1996). Not consulted."),
    dict(id="jensen1977b", author="Jensen, John Thayer", year="1977", year_suffix="b", title="Yapese-English dictionary",
         kind="dictionary", pub_type="book", place="Honolulu", publisher="University Press of Hawaii",
         notes="Bibliographic details from the reference list of Ross (1996). Not consulted."),
]

LECTS = [dict(
    id=L, name="Yapese", type="language", glottocode="yape1248", iso639_3="yap", parent_id="poc",
    latitude="9.56", longitude="138.13", region="Yap, Federated States of Micronesia",
    orthography_note="Ross's comparative transcription of Hsu (1969) and Jensen (1977a, 1977b) (Ross 1996: n. 3): "
                     "c is the affricate written ch in Yapese orthography (value not stated by Ross; decision "
                     "ross1996-symbols); y is the palatal glide (j here); a superscript ʔ marks a glottalised "
                     "consonant (fˀ, vˀ), which Table 3 derives from *CVq.",
    notes="Western Micronesia; not Nuclear Micronesian. Ross (1996) separates five strata of Austronesian vocabulary: "
          "Sets A and B from non-Oceanic sources (an older stage of Palauan or a lect close to it; an unidentified "
          "conservative language), Set C from an Oceanic source outside Nuclear Micronesian, Set D and its variant "
          "Set UW from Nuclear Micronesian (mostly Western Trukic) and recent Ulithian and Woleaian loans, and a "
          "small Set E from a Central Pacific source (pp. 128-131). Set C is the inherited stratum: the bound "
          "morphemes reflect it, so Yapese is Oceanic (p. 130). Ross tentatively links its inherited stratum with "
          "the Admiralties, as an early offshoot (§2.3, pp. 143-151); there is no Admiralties node here. Every "
          "Yapese word must begin and end with a consonant, so a glottal stop is added to vowel-initial and "
          "vowel-final words (p. 131). Glottocode and coordinates from the language metadata of Ross et al. (2023)."),
]

rows = []
n = 0
POS = {"I": "#_", "M": "V_V", "F": "_#", "": "elsewhere"}


def c(parent, child, pos="", alt=False, env=None, notes="", as_printed="", source_form="", status="regular",
      page=T2, decision=""):
    global n
    n += 1
    e = env or POS[pos]
    rows.append(dict(id=f"yap-ro96-{n}", child_lect_id=L, parent_phoneme=parent, child_phoneme=child,
                     environment=e, status=status, source_id=S, page=page, locator="Table 2",
                     stratum="Set C (inherited)", notes=notes, as_printed=as_printed, source_form=source_form,
                     conditioning="unknown" if alt else "", decision=decision))


ALT = "One of two or more Set C reflexes in this position; Ross takes the alternatives to show that some items "  \
      "assigned to Set C belong to another stratum (p. 131)."


def cell(parent, printed, spec, extra_notes=""):
    """spec: list of (child, pos, alternative?) parsed by hand from the printed cell."""
    for child, pos, alt, *sf in spec:
        c(parent, child, pos=pos, alt=alt, as_printed=f"POc *{parent} > Set C {printed}",
          source_form=sf[0] if sf else "", notes=" ".join(x for x in (ALT if alt else "", extra_notes) if x))


# Table 2, column 'Yapese set C' (p. 129). x-y-z = initial, medial, final; x|y = x or y.
cell("p", "p-p|f-; ∅/_o|u", [("p", "I", False), ("p", "M", True), ("f", "M", True)])
c("p", "∅", env="_o, _u", as_printed="POc *p > Set C p-p|f-; ∅/_o|u")
cell("b", "v; ∅|v/_u", [("v", "", False)])
c("b", "∅", env="_u", alt=True, as_printed="POc *b > Set C v; ∅|v/_u", notes=ALT)
c("b", "v", env="_u", alt=True, as_printed="POc *b > Set C v; ∅|v/_u", notes=ALT)
cell("pʷ", "fˀ-", [("fˀ", "I", False, "f?")], "Printed f with a superscript glottal stop: a glottalised f (Table 3: glottalised consonants come from *CVq).")
cell("bʷ", "vˀ-", [("vˀ", "I", False, "v?")], "Printed v with a superscript glottal stop: a glottalised v.")
cell("t", "ð|t; c/_i", [("ð", "", True), ("t", "", True)])
c("t", "c", env="_i", as_printed="POc *t > Set C ð|t; c/_i", decision="ross1996-symbols")
cell("d", "-ð-", [("ð", "M", False)])
cell("r", "r", [("r", "", False)])
cell("dr", "ð|r-r-", [("ð", "I", True), ("r", "I", True), ("r", "M", False)])
cell("s", "θ|ʔ-θ|∅-ʔ", [("θ", "I", True), ("ʔ", "I", True), ("θ", "M", True), ("∅", "M", True), ("ʔ", "F", False)],
     "Ross: *s probably had two Set C reflexes, θ and zero, and zero has been replaced by a glottal stop "
     "initially and finally by the rule that every word begins and ends with a consonant (p. 131).")
cell("j", "-r-", [("r", "M", False)])
cell("c", "-θ-", [("θ", "M", False)])
cell("k", "ʔ|k|ɣ-ɣ|∅-k|ɣ", [("ʔ", "I", True), ("k", "I", True), ("ɣ", "I", True), ("ɣ", "M", True), ("∅", "M", True),
                             ("k", "F", True), ("ɣ", "F", True)])
cell("ɡ", "ɣ|k-ɣ-", [("ɣ", "I", True), ("k", "I", True), ("ɣ", "M", False)])
cell("m", "m", [("m", "", False)])
c("mʷ", "m", env="#_", as_printed="POc *mʷ > Set C mᵒ|m-", source_form="mᵒ", alt=True,
  notes=ALT + " Printed mᵒ: m with a following rounded vowel, as in moʔon 'male' < *mʷaqane (appendix).")
c("mʷ", "m", env="#_", as_printed="POc *mʷ > Set C mᵒ|m-", alt=True, notes=ALT + " Example: mala:l 'village square' < *mʷalala (appendix).")
for p in ("n", "ñ"):
    cell(p, "n|l", [("n", "", True), ("l", "", True)], "Table 2 gives one cell for *n and *ñ.")
cell("ŋ", "ŋ-ŋ|∅-", [("ŋ", "I", False), ("ŋ", "M", True), ("∅", "M", True)])
cell("w", "w-", [("w", "I", False)])
cell("y", "y", [("j", "", False, "y")])
cell("l", "l|r", [("l", "", True), ("r", "", True)])
cell("q", "ʔ", [("ʔ", "", False)], "Glottalised consonants come from *CVq (Table 3, p. 131).")
cell("R", "ʔ-ʔ|r|∅-", [("ʔ", "I", False), ("ʔ", "M", True), ("r", "M", True), ("∅", "M", True)])
c("∅", "ʔ", env="#_V", as_printed="POc *∅-/_V > Set C ʔ-",
  notes="Consonant accretion before an initial vowel: a glottal stop, added by the Yapese rule that every word "
        "begins and ends with a consonant (p. 131).")

DECISIONS = [
    dict(id="ross1996-strata", question="Ross (1996) assigns Yapese vocabulary to five strata: Sets A and B "
         "(non-Oceanic, stated against PMP), Set C (inherited, POc), Sets D and UW (Nuclear Micronesian loans) "
         "and Set E (Central Pacific; no correspondences given). Which are entered?",
         chosen_reading="Set C only, as POc > Yapese rows with stratum 'Set C (inherited)', Yapese under POc. Sets "
                        "A, B, D and UW are described in the lect notes, not entered: A and B are stated against "
                        "PMP phonemes that POc merged, so they cannot be rows of a lect whose parent is POc; D and "
                        "UW are loans whose source is a Nuclear Micronesian language, not POc. Ross's Palauan, "
                        "PMc, Ulithian and Woleaian columns are not entered either (those lects have rows from "
                        "Blust 2009 and Bender et al. 2003a).",
         alternatives="Enter Sets A, B, D and UW as loan-stratum rows composed through POc; add Ross's Palauan "
                      "column as a second source for PMP > Palauan.",
         status="open", source_id=S, page="128-131"),
    dict(id="ross1996-symbols", question="Ross transcribes Yapese in a comparative orthography (n. 3). What are "
         "c, y and the superscript glottal stop?",
         chosen_reading="c kept as c (the Yapese ch affricate; Ross gives no phonetic value, so it is not turned "
                        "into an IPA affricate); y = j; fˀ, vˀ as printed (glottalised); Ross's mᵒ entered as m, "
                        "with the rounding noted. Medial reflexes are entered in the environment V_V.",
         alternatives="c as t͡ʃ (or another affricate) once a source for its value is read.",
         status="open", source_id=S, page="129, 152"),
]

MD = f"""# {BATCH}

Ross, Malcolm. 1996. Is Yapese Oceanic? In Bernd Nothofer (ed.), *Reconstruction, classification, description: Festschrift in honor of Isidore Dyen*, 121-166. Hamburg: Verlag Meyer & Co. Read from the scan the user put in Downloads on 23 November 2026 (OCR text layer; Tables 2 and 3 read from page images). The scan has no page numbers: pages are counted from p. 121. Generator: `tools/batch_scripts/new_sources_2026_11_23/ross1996.py`.

## Scope

- New lect **Yapese** (`yape1248`) under POc, with Ross's strata in the notes.
- POc > Yapese from the Set C column of Table 2 (p. 129), position by position (x-y-z = initial, medial, final; x|y = alternatives, entered with conditioning unknown), with `stratum` "Set C (inherited)" and the printed cell in `as_printed`.

## Decisions (open)

- `ross1996-strata`, `ross1996-symbols`.

## Not entered

- Sets A, B (against PMP), D and UW (Nuclear Micronesian loans) and E; the Palauan, PMc, Ulithian and Woleaian columns; Table 3 (a summary of Table 2).
- No inventory: Ross gives none (Table 3 lists the consonants by origin, without vowels); the inventory is generated from the rows.
- Bound morphemes (Tables 4-7), the Admiralties comparison (Table 8), the appendix data.
"""

write(BATCH, dict(sources=SOURCES, lects=LECTS, correspondences=rows, decisions=DECISIONS), MD)
