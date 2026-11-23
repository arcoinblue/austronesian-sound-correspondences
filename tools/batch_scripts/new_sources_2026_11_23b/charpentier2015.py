"""Batch charpentierfrancois2015-polynesia: Charpentier & François (2015), consonant correspondences of
the languages of French Polynesia (Table 6) and Tahitian glottal stops (Table 7).

Charpentier, Jean-Michel & Alexandre François. 2015. Atlas linguistique de la Polynésie française /
Linguistic atlas of French Polynesia. Berlin: De Gruyter Mouton & Université de la Polynésie française.
Read from the PDF of section 4 in Downloads (Table 6 from a page image: the text layer garbles the
symbols).

    python3 tools/batch_scripts/new_sources_2026_11_23b/charpentier2015.py
"""
from common import write
import chain

S = "charpentierfrancois2015"
BATCH = "charpentierfrancois2015-polynesia"
P6, P7 = "93", "94"

SOURCES = [dict(
    id=S, author="Charpentier, Jean-Michel; François, Alexandre", year="2015",
    title="Atlas linguistique de la Polynésie française / Linguistic atlas of French Polynesia",
    url_or_doi="https://doi.org/10.1515/9783110260359", kind="comparative", pub_type="book",
    place="Berlin", publisher="De Gruyter Mouton & Université de la Polynésie française",
    notes="Consulted directly on 23 November 2026: section 4 only (pp. 72-100 of the PDF the user supplied): "
          "languages and dialects with speaker numbers (Table 5, p. 76), the twenty survey locations (Map 4, "
          "Table 8), regular consonant correspondences between the languages and Proto-Polynesian with the size "
          "of each consonant inventory (Table 6, p. 93), Tahitian glottal stops for Pa'umotu t and r (Table 7, "
          "p. 94), glottal stop and vowel length. Bilingual French-English text; the English is cited.")]

rows = []
n = 0


SEEN = set()


def c(lect, parent, child, notes="", status="regular", conditioning="", as_printed="", page=P6, locator="Table 6",
      examples="", count=""):
    global n
    if (lect, parent, child, status) in SEEN:
        return
    SEEN.add((lect, parent, child, status))
    n += 1
    rows.append(dict(id=f"{lect}-cf15-{n}", child_lect_id=lect, parent_phoneme=parent, child_phoneme=child,
                     environment="conditions unknown" if conditioning == "unknown" else "elsewhere",
                     status=status, conditioning=conditioning, source_id=S, page=page, locator=locator,
                     notes=notes, derivation="composed", as_printed=as_printed, examples=examples,
                     evidence_count=count))


G = "ʔ"
COLS = ["p", "t", "k", "m", "n", "ŋ", "ʔ", "f", "s", "h", "w", "l/r"]
# Table 6 (p. 93): reflexes as printed (‘ = glottal stop, – = lost), with the survey-point numbers and C.
T6 = [
    ("nuku1261", "Nuku Hiva", "1", "p t k/‘ m n k – h/f h – v ‘", "9"),
    ("uahuna", "Ua Huna", "2", "p t k/‘ m n n/k – h/f h – v ‘", "9"),
    ("uapo1237", "Ua Pou", "3", "p t k m n k – h/f h – v ‘", "9"),
    ("sout2866", "S Marquesan", "4-5", "p t ‘/k m n n – f/h h – v k/‘", "9"),
    ("maupiti", "Maupiti", "6", "p k/t ‘ m n ‘ – f/h h – v r", "10"),
    ("tahi1242", "Tahitian", "7", "p t ‘ m n ‘ – f/h h – v r", "9"),
    ("tuam1242", "Pa'umotu", "8-16", "p t k m n ŋ – f/h h – v r", "10"),
    ("ruru1237", "Rurutu", "17", "p t ‘ m n ‘ – ‘/f ‘ – v r", "8"),
    ("raiv1237", "Ra'ivavae", "18", "p t ‘ m n ‘ – h h – v ɡ", "8"),
    ("mang1401", "Mangarevan", "19", "p t k m n ŋ – ‘ ‘ – v r", "9"),
    ("oldr1239", "Rapa Iti", "20", "p t k m n ŋ – –/‘ h/‘ – v r", "10"),
]


def norm(x):
    return {"‘": G, "–": "∅", "g": "ɡ"}.get(x, x)


skipped = []
for lect, label, pts, cells, ncons in T6:
    par = chain.parent_of(lect) if lect in chain.LECTS else {"nuku1261": "pepnd", "uahuna": "pepnd", "uapo1237": "pepnd", "maupiti": "pta", "raiv1237": "pta"}[lect]
    for col, cell in zip(COLS, cells.split()):
        alts = [norm(a) for a in cell.split("/")]
        for ppn in (["l", "r"] if col == "l/r" else [col]):
            pp, _ = chain.reflex("ppn", par, ppn)
            if pp is None:
                if alts != ["∅"]:
                    skipped.append((lect, ppn, cell))
                continue
            printed = f"PPn *{col} > {label} {cell}"
            if alts == [pp]:
                continue
            existing = {r["child_phoneme"] for r in chain.BY.get((lect, pp), []) if r["status"] == "regular"}
            for a in alts:
                if len(alts) == 1 and a in existing:
                    continue  # already stated by an earlier source
                note = ""
                if len(alts) > 1:
                    note = (f"One of two reflexes printed '{cell}', with no condition given ('only the most regular "
                            "correspondences are noted here', n. 56).")
                if col == "l/r":
                    note = (note + " " if note else "") + "Table 6 has one column for PPn *l and *r, merged as *r in East Polynesian."
                c(lect, pp, a, note, conditioning="unknown" if len(alts) > 1 else "", as_printed=printed)

# Table 7 (p. 94): Tahitian glottal stops where Pa'umotu dialects have t or r.
T7 = ("Rarer correspondence: the Tahitian glottal stop, usually for /k/ and /ŋ/ of the conservative eastern "
      "languages, here matches Pa'umotu {c} (p. 94).")
c("tahi1242", "t", G, T7.format(c="t"), status="sporadic", page=P7, locator="Table 7",
  examples="mā‘ira : Tatakoto mātira 'fishing rod'; ma‘i‘u‘u : Napuka matikuku 'nail'", count="2")
c("tahi1242", "r", G, T7.format(c="r"), status="sporadic", page=P7, locator="Table 7",
  examples="ru‘u : Reao ruru 'attach, bundle'; ‘opu : Anaa ropu 'wash in water'", count="2")

ORTH = ("Atlas transcription: the glottal stop is written with a reversed apostrophe, ‘ (p. 93); vowel length "
        "with a macron.")
LECTS = [
    dict(id="aust1304", name="Austral", type="language", glottocode="aust1304", iso639_3="aut", parent_id="pta",
         notes="Language node for the Austral dialects Rurutu, Ra'ivavae, Rimatara and the extinct Tupua'i (Tubuai) "
               "(Charpentier & François 2015: 76, Table 5). Glottocode and ISO code from Glottolog 5.4."),
    dict(id="raiv1237", name="Ra'ivavae", alt_names="Raivavae", type="dialect", glottocode="raiv1237",
         parent_id="pta", language_id="aust1304", latitude="-23.87", longitude="-147.67",
         region="Ra'ivavae, Austral Islands, French Polynesia", orthography_note=ORTH,
         notes="Dialect of Austral; survey point 18 of the atlas. Its reflex of PPn *l, *r is a stop [ɡ] "
               "(Charpentier & François 2015: 93). Eight consonants (Table 6). Glottocode from Glottolog 5.4; "
               "coordinates of the island.",
         inherit="stated-unchanged", inherit_source_id=S, inherit_page=P6,
         inherit_note="Unchanged: the consonants Table 6 gives as identical with the Proto-Tahitic ones."),
    dict(id="maupiti", name="Maupiti", type="dialect", glottocode="", parent_id="pta", language_id="tahi1242",
         latitude="-16.44", longitude="-152.25", region="Maupiti, Leeward Islands, French Polynesia",
         orthography_note=ORTH,
         notes="Variety of Maupiti, 'sometimes described as strange', survey point 6 (Charpentier & François "
               "2015: 79, 93): k (and t) for Tahitian t, ten consonants. Not in Glottolog 5.4 (a Leeward Islands "
               "variety of Tahitian); coordinates of the island.",
         inherit="stated-unchanged", inherit_source_id=S, inherit_page=P6,
         inherit_note="Unchanged: the consonants Table 6 gives as identical with the Proto-Tahitic ones."),
]
for lid, name, gc, lat, lon, pt, extra in [
        ("nuku1261", "Nuku Hiva", "nuku1261", "-8.86", "-140.14", "1", ""),
        ("uahuna", "Ua Huna", "", "", "", "2",
         " The atlas names the survey point Ua Huna (Map 3, Table 6); Map 3 also has 'Nuku Hiva (Ua Huka)', so Ua "
         "Huna is not taken to be the island Ua Huka (Glottolog uahu1237); no Glottocode."),
        ("uapo1237", "Ua Pou", "uapo1237", "-9.40", "-140.08", "3", "")]:
    LECTS.append(dict(
        id=lid, name=name, type="dialect", glottocode=gc, parent_id="pepnd", language_id="nort2845",
        latitude=lat, longitude=lon, region="Marquesas Islands, French Polynesia", orthography_note=ORTH,
        notes=f"North Marquesan variety, survey point {pt} of the atlas (Charpentier & François 2015: 77, 93)."
              + (" Glottocode from Glottolog 5.4 (a dialect of North Marquesan); coordinates of the island." if gc else "")
              + extra,
        inherit="stated-unchanged", inherit_source_id=S, inherit_page=P6,
        inherit_note="Unchanged: the consonants Table 6 gives as identical with the Proto-East Polynesian Distal ones."))

DECISIONS = [dict(
    id="cf2015-table6", question="Charpentier & François (2015) Table 6 gives PPn consonant reflexes for eleven "
    "French Polynesian varieties, with 'x/y' for two reflexes. How are they entered?",
    chosen_reading="Restated against each lect's parent in the data (Proto-East Polynesian Distal, Proto-Far "
                   "Eastern Polynesian or Proto-Tahitic). A cell that only repeats a reflex an earlier source "
                   "already gives (Marck 2000) is not entered again; 'x/y' cells give two rows with conditions "
                   "unknown. New lects: the North Marquesan varieties Nuku Hiva, Ua Huna and Ua Pou, Maupiti "
                   "(under Tahitian) and Ra'ivavae, with an Austral language node; Rurutu and Tubuai should be put "
                   "under that node (language_id aust1304) in the sheet. Table 6 is consonants only; the vowels of "
                   "the new lects are inherited.",
    alternatives="Enter every cell, repeating Marck's correspondences with this source; enter the Pa'umotu "
                 "dialects (survey points 8-16) separately.",
    status="open", source_id=S, page="76, 93")]

MD = f"""# {BATCH}

Charpentier, Jean-Michel & Alexandre François. 2015. *Atlas linguistique de la Polynésie française / Linguistic atlas of French Polynesia*. Berlin: De Gruyter Mouton & Université de la Polynésie française. Section 4 only. Generator: `tools/batch_scripts/new_sources_2026_11_23b/charpentier2015.py`.

## Scope

- Table 6 (p. 93): PPn consonants > eleven varieties, restated against the lect's parent; cells already entered from Marck (2000) are not repeated.
- Table 7 (p. 94): sporadic Tahitian ʔ for Pa'umotu t and r.
- New lects: Austral (language node), Ra'ivavae, Maupiti, Nuku Hiva, Ua Huna, Ua Pou.

## Sheet edits after applying

- `lects`: `language_id` = `aust1304` for Rurutu (`ruru1237`) and Tubuai (`tubu1240`).

## Not entered

- Vowels (no table), the Pa'umotu dialect points 8-16 separately, the consonant counts (column C) except in notes.
- Cells that disagree with nothing and add nothing: {len(skipped)} cells where the parent has already lost the phoneme.

## Decisions (open)

- `cf2015-table6`.
"""

write(BATCH, dict(sources=SOURCES, lects=LECTS, correspondences=rows, decisions=DECISIONS), MD)
print("skipped", skipped)
