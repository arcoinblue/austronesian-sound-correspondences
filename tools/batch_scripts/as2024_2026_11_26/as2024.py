#!/usr/bin/env python3
"""Adelaar & Schapper (2024), the historical chapters named by the gap audit of 26 November 2026.

Batch as2024-historical-chapters. Chapters 2, 7, 8, 9, 10, 12, 13 and 36 were read for their tables and compared
with cldf/. Almost all of it is already rows from the works the chapters summarise, or concerns languages that
are not lects; BATCH.md has a line per table. Entered: three Long Terawan Berawan rows from Smith (2024, Table 8.1).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, existing

S = "smith2024"
D = "as2024-historical-chapters"
assert S not in existing("sources", "id")
assert "longterawan" in existing("lects", "id")
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Smith, Alexander D.", year="2024", title="Historical linguistics of Borneo",
    url_or_doi="https://doi.org/10.1093/oso/9780198807353.003.0008", kind="comparative", pub_type="chapter",
    container_title="The Oxford guide to the Malayo-Polynesian languages of Southeast Asia",
    editors="Alexander Adelaar; Antoinette Schapper", pages="92-110", place="Oxford",
    publisher="Oxford University Press", series="Oxford Guides to the World's Languages",
    notes="Chapter 8. Consulted directly on 26 November 2026 for Table 8.1 (p. 97, reflexes of the PNS terminally "
          "devoiced stops; checked on the page image) and Table 8.2 (p. 99, an image: distribution of sound changes "
          "in Barito, not read). A summary of Smith (2017a); only the Long Terawan Berawan cells of Table 8.1 were "
          "not rows already. PDF page of the file 'Ch.7-14' = printed page - 78. The DOI follows the volume's "
          "chapter pattern and was not opened."))

T = ("Table 8.1, 'Reflexes of PNS terminally devoiced stops', gives one word for each of PNS *bʰ, *dʰ, *jʰ, *ɡʰ; "
     "these are 'reflexes of voiced obstruents after a penultimate schwa' (p. 97). ")
b.corr("longterawan", "bʰ", "pp", "V_V", "97",
       T + "The row from Smith (2017a) has p for *bʰ and pp as a sporadic reflex of *p.",
       derivation="", decision=D, locator="Table 8.1", examples="*təbʰu > təppuh 'sugarcane'", n=1,
       as_printed="Long Terawan Berawan təppuh")
b.corr("longterawan", "dʰ", "t͡ʃ", "V_V", "97",
       T + "Smith writes c. The rows from Smith (2017a) have this reflex as sporadic t͡ʃ from PMP *d between "
       "vowels; Long Terawan had no row for PNS *dʰ.",
       derivation="", decision=D, locator="Table 8.1", examples="*dədʰuR > dicu 'woman'", n=1,
       as_printed="Long Terawan Berawan dicu")
b.corr("longterawan", "jʰ", "t͡ʃ", "V_V", "97",
       T + "Smith writes c. The rows from Smith (2017a) have this reflex as sporadic t͡ʃ beside regular s; Long "
       "Terawan had no row for PNS *jʰ.",
       derivation="", decision=D, locator="Table 8.1", examples="*Rəjʰan > acin 'ladder'", n=1,
       as_printed="Long Terawan Berawan acin")

b.dec(D,
      "Adelaar & Schapper (2024), the historical chapters 2, 7, 8, 9, 10, 12, 13 and 36 (gap audit of 26 November "
      "2026): what is entered from their tables?",
      "Three rows: Long Terawan Berawan *bʰ > pp, *dʰ > t͡ʃ, *jʰ > t͡ʃ (Smith 2024, Table 8.1). The other tables "
      "summarise works whose rows are already in (PAn > PMP mergers; Smith 2017a; Mead 2003; Mills 1975; Adelaar "
      "1994a; Grimes & Edwards 2026), are wordlists (Tables 10.1-10.3, 9.4), or need a lect or node that does not "
      "exist.",
      "Add Proto-Philippines with the phoneme system of Table 7.1 (Blust p.c. in Zorc et al. 2024: 88); decision "
      "blust1991-pph is open. Enter Adelaar's (1992) Proto-Malayic inventory from Tables 9.1-9.2 (Anderbeck 2024: "
      "112-113) as the sourced inventory of Proto-Malayic; decision adelaar1992-pm is open. Add Proto-Sangiric "
      "(Table 12.1, twelve etyma after Sneddon 1984), the Butonic languages Kaisabu, Cia-Cia, Kumbewaha and "
      "Lasalimu (Table 12.3, PMP *q) and Rampi (Table 12.9). Enter the consonant inventories of Buru and South "
      "Nuaulu from Table 36.1 (Grimes 2024: 599, after C. Grimes 1991 and Bolton 1990; consonants only, no vowel "
      "table) and add Asilulu. Give 'Lun Dayeh' of Table 8.1 (f, s, s) to one of the two Lun Dayeh dialects. "
      "Table 13.7 (Zobel 2024: 178; *z, *d, *j, *R in 21 CMP languages) was compared with the composed rows from "
      "Grimes & Edwards (2026) for Bima, Havu, Proto-Central Flores, Proto-Flores-Lembata and Buru only; the "
      "other 16 could be compared cell by cell.",
      "97")

write(D, b.t, """# as2024-historical-chapters

Source: Adelaar & Schapper (eds, 2024), *The Oxford guide to the Malayo-Polynesian languages of Southeast Asia*,
chapters 2, 7, 8, 9, 10, 12, 13 and 36, read from the text layer of the files in `Downloads/austdic` ('Ch.1-3',
'Ch.7-14', 'Eastern Indonesia'). Tables 8.1 and 36.1 were also read from page images. The tables are in two-column
pages and several are images with no text layer.

| Chapter, table | Result |
|---|---|
| 2 (Smith), Tables 2.5-2.8: PAn *t/*C, *n/*N, *S in PMP | images; the mergers are rows of PMP already; nothing added |
| 7 (Zorc, Lobel & Hall), Table 7.1: Proto-Philippines phoneme system | not entered: there is no Proto-Philippines node (decision `blust1991-pph`) |
| 8 (Smith), Table 8.1: PNS terminally devoiced stops | Long Terawan Berawan *bʰ > pp, *dʰ > c, *jʰ > c entered; Bintulu, Miri, Kiput, Bario are rows already; Lebo' Vo' and Lepo' Tau are not lects; 'Lun Dayeh' (f, s, s) is not assigned to a dialect |
| 8, Table 8.2: sound changes in Barito | an image, not read |
| 9 (Anderbeck), Tables 9.1-9.2: Proto-Malayic system after Adelaar (1992) | not entered (decision `adelaar1992-pm` is open) |
| 9, Table 9.4; 10 (Adelaar), Tables 10.1-10.3 | wordlists, no correspondences stated |
| 12 (Mead), Table 12.1 Proto-Sangiric; 12.3 Butonic *q; 12.9 Rampi | not entered: no such lects |
| 12, Table 12.6: Bugis and Tamanic *j > s | *j > s is rows already (Mills 1975: PSS *z > Bugis s; Adelaar 1994a: Pre-Tamanic s); the sporadic loss of initial *p was not checked |
| 13 (Zobel), Tables 13.7-13.8: *z, *d, *j, *R in CMP | a summary; the lects have rows from Grimes & Edwards (2026). Compared for five of the 21 only (see the decision) |
| 36 (C. Grimes), Table 36.1: consonants of Buru, Asilulu, South Nuaulu | not entered: consonants only, and Asilulu is not a lect |
| 36, Tables 36.2-36.3: VV sequences, final consonants | lexeme tables for lects that have rows from Grimes & Edwards (2026); not compared word by word |
""")
