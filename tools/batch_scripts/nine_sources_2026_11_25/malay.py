#!/usr/bin/env python3
"""Malayic: Adelaar (2004), Where does Malay come from?, and Adelaar (1994b), Mise au point sur l'histoire
linguistique du malais jakartanais. Two batches.

- adelaar2004-malay: the sources adelaar2004 and adelaar1992 (Proto-Malayic, not at hand); the PAn > Proto-Malayic
  innovations Adelaar (2004: 12) lists from Adelaar (1992a: 2), with the Proto-Malayic column of Adelaar (1994a:
  Table 1, p. 5), as rows of Proto-Malayic against PMP, source adelaar1992, read via the two papers.
- adelaar1994b-jakarta: the source, Grijns (1991), Jakarta Malay (Betawi) with its final-syllable schwa, and
  Adelaar's (1992) Proto-Malayic schwa in final syllables (read via Adelaar 1995: 340).
Read directly on 25 November 2026 (PDFs in Downloads; the 2004 list from the page image).
"""
import hashlib
from common import Batch, write

PM = "pmalayic"

# ====================================================================== Adelaar 2004
S = "adelaar2004"
b = Batch(S)
b.t["sources"] += [
    dict(id=S, author="Adelaar, K. Alexander", year="2004",
         title="Where does Malay come from? Twenty years of discussions about homeland, migrations and classifications",
         kind="comparative", pub_type="article", container_title="Bijdragen tot de Taal-, Land- en Volkenkunde",
         volume="160", issue="1", pages="1-30", url_or_doi="https://www.jstor.org/stable/27868100",
         notes="Consulted directly on 25 November 2026 (JSTOR PDF in Downloads). Reviews the theories of the Malay "
               "homeland (§§2-5: West Borneo, between the Kapuas, Batang Lupar and Saribas rivers, p. 13ff.), the "
               "external classification of Malayic (§6: Adelaar's 1992a list of Proto-Malayic innovations, p. 12; "
               "Malayo-Chamic; Malayo-Sumbawan, Figure 1, p. 13) and its internal classification (§7: Collins's single "
               "Bornean Malay subgroup, Nothofer's western Bornean subgroups and his 'Southwest Malay', with Jakarta "
               "and Bangka Malay, pp. 14-23). Adelaar finds no diagnostic for a separate Iban branch and treats the "
               "western Bornean Malayic-Dayak isolects (Kendayan/Salako, Ibanic) as possible subgroups without "
               "entering a tree."),
    dict(id="adelaar1992", author="Adelaar, K. Alexander", year="1992", year_suffix="",
         title="Proto-Malayic: The reconstruction of its phonology and parts of its lexicon and morphology",
         kind="comparative", pub_type="book", series="Pacific Linguistics C-119", place="Canberra",
         publisher="Pacific Linguistics",
         notes="Bibliographic details from the reference lists of Adelaar (1994b, 2004, 2012). A revised version of "
               "the author's 1985 Leiden dissertation. Not consulted directly: its innovations are entered from "
               "Adelaar (2004: 12) and Adelaar (1994a: 5, Table 1)."),
]
D = "adelaar1992-pm"
VN = {"adelaar2004": "Adelaar's (2004) list of the innovations defining Malayic, from Adelaar (1992a: 2).",
      "adelaar1994a": "The Proto-Malayic (PML) column of Table 1 of Adelaar (1994a), stated against PMP."}


def PMr(par, child, env, via, vpage, ap, notes="", **k):
    b.corr(PM, par, child, env, "", as_printed=ap, notes=notes, decision=D, **k)
    r = b.t["correspondences"][-1]
    r.update(source_id="adelaar1992", via_source_id=via, via_page=vpage, via_note=VN[via])
    r["id"] = "c" + hashlib.sha1(("adelaar1992|" + via + "|" + r["id"]).encode()).hexdigest()[:10]


V4 = ("adelaar2004", "12")
for ph, out in (("b", "p"), ("d", "t"), ("ɡ", "k")):
    PMr(ph, out, "_#", *V4, "1. Devoicing of PAn final stops")
PMr("j", "d", "#_, V_V", *V4, "2. PAn *j > PM *d, *-t", notes="Also Table 1 of Adelaar (1994a: 5): PMP *j > PML d, -t; *(N)j > (n)d.")
PMr("j", "t", "_#", *V4, "2. PAn *j > PM *d, *-t")
PMr("w", "∅", "#_", *V4, "7. PAn initial *w was lost",
    notes="'A rather critical device for the establishment of the Malayic sub-group' (Adelaar 1994a: 13).")
for v, c in (("u", "y"), ("i", "w")):
    note = f"8. PAn *i, *-ey, *-uy, *-iw > PM *i: the diphthong *-{v}{c} (word-final)."
    PMr(v, "i", f"_+{c}", *V4, f"PAn *-{v}{c} > PM *i", notes=note)
    PMr(c, "i", f"{v}+_", *V4, f"PAn *-{v}{c} > PM *i", notes=note)
note = ("8. PAn *-ey > PM *i: Adelaar's *-ey is the schwa + y (PMP *e keyed for the schwa); Adelaar (1994a: 5, "
        "Table 1) has PMP *-əy > PML -i, *matəy > *mati.")
PMr("e", "i", "_+y", *V4, "PAn *-ey > PM *i", notes=note)
PMr("y", "i", "e+_", *V4, "PAn *-ey > PM *i", notes=note)
note = "9. PAn *u, *-ew > PM *u: the schwa + w; Adelaar (1994a: 5, Table 1) has PMP *-əw > PML -u, *laləw > *lalu."
PMr("e", "u", "_+w", *V4, "PAn *-ew > PM *u", notes=note)
PMr("w", "u", "e+_", *V4, "PAn *-ew > PM *u", notes=note)
PMr("q", "h", "_#", *V4, "10. PAn *q > PM *h",
    notes="Also Table 1 of Adelaar (1994a: 5): *-iq > -ih, *-uq > -uh. Adelaar states *q > *h in all positions; the row "
          "is entered word-finally only, as Smith (2017a: 184) has it, because Smith's Malayic lects are stated against "
          "a PM *q in other positions (decision adelaar1992-pm).")
PMr("h", "∅", "#_", *V4, "11. PAn *h, *ʔ > PM *ʔ or Ø",
    notes="'Lost in initial position in Proto-Malayic; intervocalically and finally they became PML *ʔ' (Adelaar "
          "1994a: 11). PMP *h continues PAn *S and *H.")
PMr("h", "ʔ", "V_V, _#", *V4, "11. PAn *h, *ʔ > PM *ʔ or Ø", status="disputed",
    notes="'The reconstruction of PML *-ʔ (instead of Ø) is uncertain (Adelaar 1992: 66)' (Adelaar 1994a: 5 n. 11, "
          "11).")

b.dec(D, "How are Adelaar's (1992) Proto-Malayic innovations entered?",
      "As rows of Proto-Malayic (Smith's node, mala1538) against PMP, source adelaar1992 read via Adelaar (2004: 12), "
      "with the details of Adelaar (1994a: 5, Table 1) in the notes. PAn is restated against PMP: *-ey and *-ew are "
      "the schwa + glide (PMP keys e + y, e + w); *h and *ʔ are PMP *h. *q > *h is entered word-finally only, as Smith (2017a) has it, since Smith's Malayic lects are stated against a PM *q elsewhere; for the same reason innovations 3 (*z > PM *j) and 4 (*R > PM *r) are not entered as rows: Smith (2017a) states his Malayic lects from PMP *z and *R directly, and their rows rest on a PM *z and *R. Innovations 5 (reduction of clusters to "
      "their last component) and 6 (homorganic nasals in heterorganic NC) concern clusters and are in the notes "
      "only.", "Wait for Adelaar (1992) itself; enter the 1994a PML column as a separate set of rows.", "12")
write("adelaar2004-malay", b.t, """# adelaar2004-malay

Adelaar, K. Alexander. 2004. Where does Malay come from? Twenty years of discussions about homeland, migrations and classifications. *Bijdragen tot de Taal-, Land- en Volkenkunde* 160(1). 1-30. Generator: `tools/batch_scripts/nine_sources_2026_11_25/malay.py`.

## Scope

- Sources `adelaar2004` and `adelaar1992` (Proto-Malayic, not at hand).
- Proto-Malayic rows from the list of innovations (p. 12, read from the page image), source `adelaar1992` via `adelaar2004`, details from Adelaar (1994a: Table 1) in the notes (decision `adelaar1992-pm`).

## Not entered

- Innovations 3 (*z > *j) and 4 (*R > *r), and *q > *h outside final position: Smith's (2017a) Malayic lects are stated against a PM *z, *R and *q, so these rows would cut them off (decision `adelaar1992-pm`).
- Innovations 5 and 6 (consonant clusters), the homeland discussion, Malayo-Chamic and Malayo-Sumbawan (already entered from Adelaar 2005), Collins's and Nothofer's internal classifications of Malayic (notes only).
""")

# ====================================================================== Adelaar 1994b (Jakarta Malay)
S = "adelaar1994b"
b = Batch(S)
b.t["sources"] += [
    dict(id=S, author="Adelaar, K. A.", year="1994", year_suffix="b",
         title="Mise au point sur l'histoire linguistique du malais jakartanais", kind="comparative",
         pub_type="article", container_title="Archipel", volume="47", pages="47-50",
         url_or_doi="https://doi.org/10.3406/arch.1994.2965",
         notes="Consulted directly on 25 November 2026 (Persée PDF in Downloads). A reply, in French, to Grijns (1991) "
               "and to Lombard's review of it: Jakarta Malay keeps the PAN schwa in closed final syllables (*qatep > "
               "atep, standard Malay atap) where other Malayic isolects have a, which Adelaar (1985/1992a, more than "
               "seven pages, fourteen words) takes as a retention from Proto-Malayic and Grijns as Javanese, "
               "Sundanese or Balinese influence. Banten letters of 1619 (Ricklefs 1976) already show such e (p. 49)."),
    dict(id="grijns1991", author="Grijns, C. D.", year="1991",
         title="Jakarta Malay: A multidimensional approach to spatial variation", kind="grammar", pub_type="book",
         series="Verhandelingen 149", place="Leiden", publisher="KITLV Press",
         notes="2 vols. Bibliographic details from the reference list of Adelaar (1994b: 50); not consulted directly."),
]
JM = "beta1252"
b.t["lects"].append(dict(
    id=JM, name="Jakarta Malay", alt_names="Betawi;Malais jakartanais", type="language", glottocode="beta1252",
    iso639_3="bew", parent_id=PM, latitude="-6.21174", longitude="107.022", region="Jakarta and surroundings, Java",
    notes="Glottolog's Betawi. Grijns (1991: 2-5) derives it from a Malay lingua franca of the north Java ports that "
          "became a mother tongue and stable dialect in colonial Batavia in the last quarter of the nineteenth "
          "century; Adelaar (1994b) takes it as a continuation of Proto-Malayic on the evidence of the final-syllable "
          "schwa. Adelaar (2004: 20-23) discusses Nothofer's grouping of Jakarta Malay with Bangka Malay in a "
          "'Southwest Malay' subgroup (decision adelaar1994b-jakarta)."))
D = "adelaar1994b-jakarta"
b.corr(JM, "ə", "ə", "_C#", "47-48", derivation="stated-retention", decision=D,
       as_printed="le malais jakartanais a gardé de l'austronésien commun un e (e muet, pepet ou schwa) en dernière "
                  "syllabe fermée",
       notes="*qatep 'roof' > atep (standard Malay hatap, atap), against *umpan > umpan; 'la distribution d'e et a en "
             "malais jakartanais correspond assez nettement avec la distribution de *e et *a en austronésien commun' "
             "(p. 47). Grijns (1991: 4-5) explains these e as Javanese, Balinese or Sundanese influence. Stated "
             "against the Proto-Malayic schwa: Smith (2017a) has PMP *ə > PM *a in this position, Adelaar (1992) "
             "keeps PM *ə (decision adelaar1994b-jakarta).")
b.corr(PM, "e", "ə", "_C#", "", decision=D, derivation="",
       notes="Adelaar (1995: 340): 'As *ə must also have occurred in Proto Malayic (see Adelaar 1992:32-42), the "
             "retention of *ə in Lom is compatible with inclusion of this language in the Malayic subgroup'; Jakarta "
             "Malay also keeps it. Against Smith's (2017a: 184) PMP *e > PM *a in final closed syllables.")
r = b.t["correspondences"][-1]
r.update(source_id="adelaar1992", via_source_id="adelaar1995", via_page="340",
         via_note="Adelaar's summary of his own reconstruction, cited for Lom.")
r["id"] = "c" + hashlib.sha1(("adelaar1992|adelaar1995|" + r["id"]).encode()).hexdigest()[:10]
b.dec(D, "Did Proto-Malayic keep the schwa in final closed syllables, and where does Jakarta Malay go?",
      "Both readings are entered on Proto-Malayic: Smith's (2017a) PMP *e > *a / _C# and Adelaar's (1992) retention "
      "of *ə (read via Adelaar 1995: 340); Jakarta Malay (Betawi, beta1252) goes directly under Proto-Malayic with "
      "its schwa as a stated retention (Adelaar 1994b). No Southwest Malay or Bangka grouping is entered.",
      "Follow Smith only and mark the Jakarta Malay e as a loan stratum (Grijns 1991); add Nothofer's Southwest "
      "Malay group.", "47-49")
write("adelaar1994b-jakarta", b.t, """# adelaar1994b-jakarta

Adelaar, K. A. 1994b. Mise au point sur l'histoire linguistique du malais jakartanais. *Archipel* 47. 47-50. Generator: `tools/batch_scripts/nine_sources_2026_11_25/malay.py`.

## Scope

- Sources `adelaar1994b` and `grijns1991`; new lect Jakarta Malay (Betawi, beta1252) under Proto-Malayic with its final-syllable schwa; Adelaar's (1992) Proto-Malayic schwa in final syllables, via Adelaar (1995: 340) (decision `adelaar1994b-jakarta`).

## Not entered

- The sociohistorical argument (lingua franca, Batavia, Banten letters): notes only.
""")
