#!/usr/bin/env python3
"""Grimes & Grimes (1987), Blust (1991) and Tryon (2010): three batches with few rows.

- grimes1987-south-sulawesi: the source, one allophone of Mandar (p. 96), the tree decision. The lect notes of
  batch mills1975-pss cite its classification and dialect lists (pp. 15-18, 23-53, 96-97).
- blust1991-gcp: PGCPh *R > ɡ (p. 98) and the *R reflexes of Table 2 (p. 90) for the four lects of the table that
  are in the database; decisions on Proto-Philippines and the GCP members.
- tryon2010-santo: the source and a decision; the Santo lects' notes go in through sheet_edits.py.
All three read directly on 25 November 2026 (PDFs in Downloads).
"""
from common import Batch, write

# ------------------------------------------------------------------ Grimes & Grimes 1987
S = "grimes1987"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Grimes, Charles E.; Grimes, Barbara D.", year="1987", title="Languages of South Sulawesi",
    kind="comparative", pub_type="book", place="Canberra", publisher="Pacific Linguistics",
    series="Pacific Linguistics D-78; Materials in Languages of Indonesia 38",
    notes="Consulted directly on 25 November 2026 (Internet Archive scan in Downloads, OCR text layer). A "
          "lexicostatistical survey (202-item list, 39 word lists collected November 1982 to March 1983); "
          "classification in Figure 5 (pp. 15-18) and chapter 3: a South Sulawesi Stock of five divisions, the "
          "Makassar Subfamily, the Bugis Family, the Northern South Sulawesi Family (with the Toraja-Sa'dan and "
          "Masenrempulu Subfamilies), the Seko Family and Lemolang (p. 23); a Central Sulawesi Stock and a Muna-Buton "
          "Stock (Laiyolo, Bonerate, Kalaotoa, Wotu). Phonetic notes on single languages pp. 94-97; word lists "
          "Appendix E."))
b.allo("mand1442", "d", "ð̠", "Balanipa, Pamboang and Malunda dialects", "96",
       "'A [d] which sounds very much like the voiced interdental fricative of English but is actually articulated "
       "as a voiced alveolar fricative with ungrooved tongue blade', written d, dh or ð in the literature (p. 96).")
b.dec("grimes1987-tree",
      "Are the families of Grimes & Grimes (1987) entered as groups under Proto-South Sulawesi?",
      "No: the seven daughters of Mills (1975) sit directly under PSS. Grimes & Grimes's Northern South Sulawesi "
      "Family (Mandar, Mamuju, PUS, Pattae', the Toraja-Sa'dan and Masenrempulu Subfamilies) and Mills's 'Toraja, in "
      "the broadest sense, including PUS-Seko and Sa'dan' (1975: 217-218) each contain a group the other splits, and "
      "neither is a reconstructed node, so neither can be an alternative node (alt_parents must be a "
      "proto-language). Their other families each hold one lect of the database. Their classification is in the "
      "lect notes.",
      "Enter Makassar, Bugis, Northern South Sulawesi, Toraja-Sa'dan and Masenrempulu as `group` nodes (tree_parent) "
      "after Grimes & Grimes and Glottolog, with Mills's grouping in the notes.", "15-18, 23")
write("grimes1987-south-sulawesi", b.t, """# grimes1987-south-sulawesi

Grimes, Charles E. & Barbara D. Grimes. 1987. *Languages of South Sulawesi* (Pacific Linguistics D-78). Canberra: Pacific Linguistics. Generator: `tools/batch_scripts/five_sources_2026_11_25d/others.py`.

## Scope

- Source row; one allophone (Mandar d as a voiced alveolar non-sibilant fricative in three dialects, p. 96); decision `grimes1987-tree` (families not entered as groups).
- The classification and dialect lists (Figure 5, pp. 15-18; chapter 3) and the phonetic notes (pp. 96-97) are cited in the notes of the lects of batch `mills1975-pss`.

## Not entered

- The lexicostatistical percentages and the families as tree nodes (decision `grimes1987-tree`).
- Lects with no phonological data beyond the word lists: Konjo, Selayar, Campalagian, Mamuju, Pattae', Kalumpang, Mamasa, Rongkong, Toala', Pattinjo, Seko Padang, Panasuan, Lemolang, the Central Sulawesi and Muna-Buton languages. Their classification of Barang-Barang (Loa') and Wotu as Muna-Buton differs from Zobel's (2020) Southern Kaili–Wolio placement in the database.
- Phonetic notes on Mamuju, PUS, Mamasa, Rongkong, Enrekang, Seko Tengah, Topoiyo and Rampi (pp. 96-97): in lect notes where the lect exists, otherwise not entered. Comparative word lists (Appendix E).
""")

# ------------------------------------------------------------------ Blust 1991
S = "blust1991"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Blust, Robert", year="1991", title="The Greater Central Philippines hypothesis",
    kind="comparative", pub_type="article", container_title="Oceanic Linguistics", volume="30", issue="2",
    pages="73-129", url_or_doi="https://doi.org/10.2307/3623084",
    notes="Consulted directly on 25 November 2026 (JSTOR PDF in Downloads). §2 fifteen Philippine microgroups; §3 "
          "Proto-Philippines phonology (Figure 2, the revised PPh consonants, p. 88) and its main developments "
          "(p. 89); §4 the reflexes of *R in 26 languages (Table 2, p. 90); §§5-7 the Greater Central Philippines "
          "hypothesis (Central Philippines, South Mangyan, Palawanic, Manobo, Danaw, Subanun, Gorontalo-Mongondow), "
          "defined by the merger of PPh *R and *g and 94 lexical innovations (Appendix)."))
T2 = "Table 2, reflexes of *R (p. 90): direct reflex, indirect reflexes (counts in brackets) and the percentage of probable loans."
b.corr("pgcph", "R", "ɡ", "elsewhere", "98", derivation="", as_printed="PPH *R and *g merged in Proto-Greater Central Philippines",
       notes="The one phonological innovation of the group: 'the *R > /g/ languages of the central and southern "
             "Philippines and the Gorontalo-Mongondow languages of Sulawesi are descended from a single language that "
             "merged PPH *R and *g' (pp. 96, 98). Blust states it against Proto-Philippines, which is not a node here "
             "(decision blust1991-pph). Kalamian Tagbanwa (*R > l) cannot be a member.")
b.corr("molb1237", "ɡ", "ɡ", "elsewhere", "90", n=6, as_printed="*R > g (6)",
       notes=T2 + " Counts of PPh *R only; Blust: 'Both languages [Molbog and Banggi] appear to regularly reflect *R as /g/' (p. 92).")
b.corr("molb1237", "ɡ", "r", "conditions unknown", "90-92", n=2, status="sporadic", as_printed="*R > r (2)",
       notes=T2 + " Not explicable as Malay loans: PMP *zuRuq > duruʔ 'liquid', *Ramut > ramut 'root'; they may come "
             "from substrate languages of southern Palawan that reflected *R as r (pp. 92-93).")
b.corr("molb1237", "ɡ", "d͡z", "conditions unknown", "90", n=1, status="sporadic", source_form="dz", as_printed="*R > dz (1)", notes=T2)
b.corr("molb1237", "ɡ", "h", "conditions unknown", "90-92", n=1, status="sporadic", as_printed="*R > h (1)",
       notes=T2 + " '*R > /h/ in Molbog suggests borrowing from Samal', but PMP *zaRum > dohum 'needle' is not "
             "easily a Samalan loan (Samal jalum) (p. 92).")
b.corr("bong1289", "R", "ɡ", "elsewhere", "90", n=10, as_printed="Banggi *R > g (10)", notes=T2 + " Banggi data from Schneeberger (1937) (p. 91).")
b.corr("bong1289", "R", "r", "elsewhere", "90-92", n=8, status="loan-stratum", as_printed="Banggi *R > r (8)",
       notes=T2 + " 'Most instances of *R > /r/ in Banggi are best explained as Malay loans', but not PMP *deŋeR > "
             "ki-doŋor 'hear' (p. 92). 40% of the reflexes counted as probable loans.")
b.corr("bong1289", "R", "∅", "conditions unknown", "90", n=2, status="loan-stratum", as_printed="Banggi *R > zero (2)",
       notes=T2 + " Counted with the indirect reflexes (40% = 10 of 25). Smith (2017a) has *R > ∅ between vowels as regular.")
b.corr("ivat1242", "R", "j", "elsewhere", "90-91", n=19, source_form="y", as_printed="Itbayaten *R > y (19)",
       notes=T2 + " 'Some 79% of the known reflexes of *R are /y/' (p. 91); data from Reid (1971). Stated against "
             "PPh *R, here the *R of Proto-Batanic.")
b.corr("ivat1242", "R", "ɡ", "elsewhere", "90-91", n=3, status="loan-stratum", as_printed="Itbayaten *R > g (3)",
       notes=T2 + " 'Best attributed to borrowing from North Cordilleran languages' (12.5%, p. 91).")
for ch, ap in (("l", "l (1)"), ("∅", "zero (1)")):
    b.corr("ivat1242", "R", ch, "conditions unknown", "90-91", n=1, status="sporadic", as_printed="Itbayaten *R > " + ap,
           notes=T2 + " 'The possibility that conditioned change accounts for single instances of /l/ and zero' (p. 91).")
b.corr("cent2089", "ɡ", "ɡ", "elsewhere", "90", n=28, as_printed="Sindangan Subanun *R > g (28)",
       notes=T2 + " Blust's Sindangan Subanun (data from Reid 1971), read as Central Subanen; counts of PPh *R only, "
             "here PSub *ɡ, which continues PMP *R and *ɡ.")
b.t["sources"] += [
    dict(id="reid1971", author="Reid, Lawrence A.", year="1971", title="Philippine minor languages: Word lists and phonologies",
         kind="comparative", pub_type="book", place="Honolulu", publisher="University of Hawaii Press",
         series="Oceanic Linguistics Special Publication 8",
         notes="Editor, not author. Bibliographic details from the reference list of Blust (1991: 127); not consulted "
               "directly. The source of Blust's Table 2 data for nine languages (p. 90)."),
    dict(id="schneeberger1937", author="Schneeberger, W. F.", year="1937",
         title="A short vocabulary of the Banggi and Bajau languages", kind="dictionary", pub_type="article",
         container_title="Journal of the Malayan Branch of the Royal Asiatic Society", volume="15", pages="145-164",
         notes="Bibliographic details from the reference list of Blust (1991: 127); not consulted directly."),
]
b.dec("blust1991-pph",
      "Is Blust's (1991: 88) Proto-Philippines (Figure 2: p t k q b d z j g m n ñ ŋ s h l r R w y; vowels i u e a) "
      "entered?",
      "No: there is no Proto-Philippines node. Philippine subgroups (Proto-Batanic, Proto-Northern Luzon, "
      "Proto-Central Luzon, PGCPh, Proto-Manide-Alabat) sit under PMP, and Blust's PPh > microgroup statements "
      "(p. 89) and Table 2 are entered against those nodes where the lect exists.",
      "A node Proto-Philippines (pph) under PMP with Figure 2 as its inventory, the Philippine nodes moved under it "
      "(and Sangiric, Minahasan, which Blust 1991 counts as Philippine), with alt_parents for the classifications "
      "that reject the group.", "87-89")
b.dec("blust1991-gcp",
      "How are Blust's (1991) Greater Central Philippines members entered?",
      "PGCPh (grea1284, already under PMP) keeps its daughters (Umiray Dumaget, Proto-Subanen, Molbog). Central "
      "Philippines, South Mangyan, Palawanic, Manobo, Danaw and Gorontalo-Mongondow are not nodes, and the Table 2 "
      "languages that are not lects (Tagalog, Bikol, Hanunóo, Palawan Batak, Cebuano, Mansaka, Western Bukidnon "
      "Manobo, Maranao, Bolaang Mongondow, Gorontalo, and outside GCP Gaddang, Ilokano, Bontok, Pangasinan, Sambal, "
      "Kalamian Tagbanwa, Inati, Tiruray, Samal, Proto-Sangiric, Proto-Minahasan) are not added for one row each.",
      "Add them as lects with their *R row (they would be treated as assumed-unchanged, having fewer than 13 phonemes "
      "known); add the six microgroups as nodes.", "73-104")
write("blust1991-gcp", b.t, """# blust1991-gcp

Blust, Robert. 1991. The Greater Central Philippines hypothesis. *Oceanic Linguistics* 30(2). 73-129. Generator: `tools/batch_scripts/five_sources_2026_11_25d/others.py`.

## Scope

- PGCPh *R > ɡ (p. 98), second source beside Lobel (2013).
- Table 2 (*R reflexes, p. 90) for the four languages of the table that are lects: Molbog, Bonggi (Banggi), Itbayat (Itbayaten), Central Subanen (Sindangan Subanun), composed against their parents.
- Decisions `blust1991-pph` and `blust1991-gcp` (open).

## Not entered

- Proto-Philippines (Figure 2) and its developments (p. 89: Kalamian *k > ∅ and *q > k, Bilic *k > g, *s > h in Botolan Sambal and Kalamian, Tiruray final vowels and others): decision `blust1991-pph`.
- Table 2 rows for the 22 languages that are not lects; Kapampangan and Botolan Sambal, whose parents (Proto-Central Luzon, Proto-Sambalic) already have *R > *y, so that Blust's counts cannot be composed (decision `blust1991-gcp`).
- The 94 lexical innovations of the Appendix, the lexicostatistics of Table 4 and the language densities of Table 3.
""")

# ------------------------------------------------------------------ Tryon 2010
S = "tryon2010"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Tryon, Darrell", year="2010", title="The languages of Espiritu Santo, Vanuatu", kind="comparative",
    pub_type="chapter", pages="283-290",
    container_title="A journey through Austronesian and Papuan linguistic and cultural space: Papers in honour of "
                    "Andrew Pawley", editors="John Bowden; Nikolaus P. Himmelmann; Malcolm Ross",
    place="Canberra", publisher="Pacific Linguistics", series="Pacific Linguistics 615",
    notes="Consulted directly on 25 November 2026 (PDF of the chapter in Downloads; the volume details are not "
          "printed in it and come from the standard citation). A map and list of 35 languages of Santo by area, "
          "with villages and speaker numbers (pp. 287-289), after the Vanuatu Cultural Centre fieldworkers; no "
          "phonological data except that the Vasi and Pialulup dialect of Tolomako has a /k/ > /ʔ/ shift (p. 287 n. 5, "
          "after a 2006 field report by Ross Clark)."))
b.dec("tryon2010-santo",
      "Tryon (2010: 289) says the Santo languages 'appear more closely related to each other than to languages from "
      "any island outside Santo and so to constitute a Santo subgroup within Northern Vanuatu', on 'tentative shared "
      "phonological and lexical innovation'. Is a Santo group entered?",
      "No: Tryon gives no innovations, and the Santo lects of the database (Sakao, Tamambo, Araki) stay under "
      "Proto-North-Central Vanuatu. The language list goes into their notes (sheet edits).",
      "A `group` Santo (Espiritu Santo) under PNCV holding Sakao, Tamambo and Araki.", "285, 289")
write("tryon2010-santo", b.t, """# tryon2010-santo

Tryon, Darrell. 2010. The languages of Espiritu Santo, Vanuatu. In John Bowden, Nikolaus P. Himmelmann & Malcolm Ross (eds.), *A journey through Austronesian and Papuan linguistic and cultural space* (Pacific Linguistics 615), 283-290. Canberra: Pacific Linguistics. Generator: `tools/batch_scripts/five_sources_2026_11_25d/others.py`.

## Scope

- Source row and decision `tryon2010-santo` (open). The paper has no correspondences.
- `sheet_edits.py` adds Tryon's names, speaker numbers and villages to the notes of Sakao (Nekep), Tamambo and Araki.

## Not entered

- The 30-odd Santo languages that are not lects, the Tolomako dialect of Vasi and Pialulup with /k/ > /ʔ/ (p. 287 n. 5), and the history of the classification (Tryon 1976, Clark 1985, 2009, Lynch & Crowley 2001).
""")
