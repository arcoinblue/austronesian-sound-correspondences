#!/usr/bin/env python3
"""Ross (2012), In defense of Nuclear Austronesian: the cells of Table 4 (pp. 1274-1275) with no row yet.

Batch ross2012-table4. Table 4 gives the reflexes of 26 PAn consonants (in Tsuchida's, Blust's and Ross's
notations) in 20 Formosan languages and PMP. ross2012_table4.json is the table as parsed from the PDF's text
layer (which has the IPA), with five lines repaired by hand and compared with the page image. Every cell was
compared with the rows in cldf/: a cell is entered only where the lect had no row at all for that phoneme.
"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, existing

BATCH = D = "ross2012-table4"
S = "ross2012"
T = json.loads((Path(__file__).parent / "ross2012_table4.json").read_text(encoding="utf-8"))
LECTS = existing("lects", "id")
b = Batch(S)
ROSS = {"d", "Z", "D", "z", "θ", "x", "S", "s"}
P1 = {"p", "b", "t", "C", "d", "Z", "D", "z", "s", "k", "ɡ", "q", "w", "y"}
U = "conditions unknown"
# column, lect, phoneme, [(reflex, environment, status, note)], parent_lect_id
ROWS = [
 ("Taokas", "taok1237", "b", [("b", "elsewhere", "regular", "")], ""),
 ("Taokas", "taok1237", "q", [("h", "elsewhere", "regular", "")], ""),
 ("Taokas", "taok1237", "j", [("t", U, "regular", ""), ("∅", U, "regular", "")], ""),
 ("Taokas", "taok1237", "m", [("m", "elsewhere", "regular", "")], ""),
 ("Taokas", "taok1237", "n", [("n", "elsewhere", "regular", "")], ""),
 ("Taokas", "taok1237", "N", [("t", "elsewhere", "regular", "")], ""),
 ("Taokas", "taok1237", "l", [("l", U, "regular", ""), ("r", U, "regular", "")], ""),
 ("Papora", "nucl1579", "p", [("p", U, "regular", ""), ("∅", U, "regular", "")], ""),
 ("Papora", "nucl1579", "b", [("b", "elsewhere", "regular", "")], ""),
 ("Papora", "nucl1579", "t", [("t", "elsewhere", "regular", "")], ""),
 ("Papora", "nucl1579", "q", [("∅", "elsewhere", "regular", "")], ""),
 ("Papora", "nucl1579", "j", [("d", U, "regular", ""), ("∅", U, "regular", "")], ""),
 ("Papora", "nucl1579", "m", [("m", "elsewhere", "regular", "")], ""),
 ("Papora", "nucl1579", "n", [("n", "elsewhere", "regular", "")], ""),
 ("Papora", "nucl1579", "N", [("l", "elsewhere", "regular", "")], ""),
 ("Papora", "nucl1579", "l", [("r", "elsewhere", "regular", "")], ""),
 ("Papora", "nucl1579", "R", [("l", "elsewhere", "disputed", "Printed 'l (?)'.")], ""),
 ("Hoanya", "hoan1238", "p", [("p", "elsewhere", "regular", "")], ""),
 ("Hoanya", "hoan1238", "b", [("b", "elsewhere", "regular", "")], ""),
 ("Hoanya", "hoan1238", "t", [("t", "elsewhere", "regular", "")], ""),
 ("Hoanya", "hoan1238", "q", [("∅", "elsewhere", "regular", "")], ""),
 ("Hoanya", "hoan1238", "j", [("d͡z", "elsewhere", "regular", "Printed dz.")], ""),
 ("Hoanya", "hoan1238", "m", [("m", "elsewhere", "regular", "")], ""),
 ("Hoanya", "hoan1238", "n", [("n", "elsewhere", "regular", "")], ""),
 ("Hoanya", "hoan1238", "N", [("s", "elsewhere", "regular", "")], ""),
 ("Hoanya", "hoan1238", "l", [("l", "elsewhere", "regular", "")], ""),
 ("Hoanya", "hoan1238", "R", [("h", "elsewhere", "regular", "")], ""),
 ("Fav-Babuza", "favo1235", "x", [("∅", "elsewhere", "regular", "")], ""),
 ("P Atayal", "pata", "Z", [("d", "elsewhere", "regular", "")], ""),
 ("P Atayal", "pata", "D", [("d", "elsewhere", "regular", "")], ""),
 ("Siraya", "sira1267", "p", [("p", "elsewhere", "regular", "")], "pan"),
 ("Siraya", "sira1267", "b", [("v", "elsewhere", "regular", "")], "pan"),
 ("Siraya", "sira1267", "C", [("t", "elsewhere", "regular", "")], "pan"),
 ("Siraya", "sira1267", "k", [("k", "elsewhere", "regular", "")], "pan"),
 ("Siraya", "sira1267", "y", [("j", "_#", "regular", "Printed '-y': the final reflex only.")], "pan"),
 ("Siraya", "sira1267", "j", [("n", "elsewhere", "regular", "Printed 'n [n̪]'.")], "pan"),
 ("Siraya", "sira1267", "m", [("m", "elsewhere", "regular", "")], "pan"),
 ("Siraya", "sira1267", "ŋ", [("ŋ", "elsewhere", "regular", "")], "pan"),
 ("Siraya", "sira1267", "N", [("l", "elsewhere", "regular", "")], "pan"),
 ("Siraya", "sira1267", "l", [("r", "elsewhere", "regular", "")], "pan"),
 ("Siraya", "sira1267", "R", [("ɡ", "elsewhere", "regular", "Printed g.")], "pan"),
 ("P Amis", "pami", "C", [("t", "elsewhere", "regular", "Printed 't [t̪]'.")], "pan"),
 ("P Amis", "pami", "Z", [("ɾ", "elsewhere", "regular", "Printed 'r, l [ɾ]': two spellings of one flap.")], "pan"),
 ("P Amis", "pami", "D", [("ɾ", "elsewhere", "regular", "Printed r; the neighbouring cells give r as [ɾ].")], "pan"),
 ("P Amis", "pami", "j", [("n", "elsewhere", "regular", "")], "pan"),
]
n = 0
for col, lid, ph, refl, pl in ROWS:
    assert lid in LECTS, lid
    cell = T[col][ph]
    page = "1274" if ph in P1 else "1275"
    for child, env, status, note in refl:
        notes = (f"Table 4, 'Formosan and PMP consonant correspondences' (p. {page}), column PAn (Ross) *{ph if ph != 'N' else 'L'}"
                 f", row {col}. A summary after Blust (1999a) in Ross's notation; entered because the lect had no row for "
                 f"this phoneme. " + ("Alternants separated by a comma, no conditions given. " if len(refl) > 1 else "") + note)
        b.corr(lid, ph, child, env, page, notes, status=status, derivation="as-stated", decision=D, locator="Table 4",
               as_printed=f"*{ph if ph != 'N' else 'L'} : {col} {cell}", system="Ross" if ph in ROSS else "")
        if pl:
            b.t["correspondences"][-1]["parent_lect_id"] = pl
        n += 1

b.dec(D,
      "Ross (2012) Table 4 (pp. 1274-1275), all PAn consonants in 20 Formosan languages: what is entered beside the "
      "rows of the language sources and of Ross (2015)?",
      "Only the cells of lects that had no row at all for the phoneme: Taokas (*b, *q, *j, *m, *n, *L, *l), Papora "
      "(*p, *b, *t, *q, *j, *m, *n, *L, *l, *R), Hoanya (the same ten), Favorlang *x, Proto-Atayal *Z and *D, "
      "Siraya (*p, *b, *C, *k, *-y, *j, *m, *ŋ, *L, *l, *R) and Amis (*C, *Z, *D, *j; on Proto-Amis-Sakizaya), the "
      "last two stated against PAn (parent_lect_id pan) because the lects stand under Proto-East Formosan. Cells that "
      "repeat a phoneme the lect already has a row for were not compared symbol by symbol.",
      "1. Enter every cell as a second source. 2. Enter *ñ (Puyuma l, Tsou n, Kanakanavu ŋ, Saaroa ɬ, Saisiyat l, "
      "Siraya l, Kavalan n): the default PAn inventory has no *ñ. 3. Enter Basay, Trobiawan and Kavalan: they stand "
      "under Proto-Basay and Proto-Kavalan (decision tseng-nef), and Tseng's (2023) Table 6.4 takes its Taokas "
      "and Saisiyat columns from this table. 4. Table 9 (p. 1311), the reflexes that keep *z, *d, *Z, *D apart: the "
      "rows of Ross (2015) have them.",
      "1274-1275")
b.dec("audit-s1-not-entered",
      "Gap audit of 26 November 2026, §1: Walworth (2014) and Li (1985) have no rows. Are their tables entered?",
      "Not in this batch. Walworth (2014): Tables 1, 4, 7, 10, 11 and 12 are taken or adapted from Marck (2000: "
      "24-26, 45, 132-134), whose rows are entered from the original; Tables 2, 3, 5, 6, 8 and 13 are word lists. "
      "What is Walworth's own is her judgement of Marck's sporadic changes (five of the six PCEP changes kept, "
      "*kumi > *kumu rejected; five of the six Proto-Marquesic and eight of the ten Proto-Tahitic changes "
      "questioned, pp. 262-265), which is not on the rows. Li (1985): Table 2 (pp. 261-262 and following) gives the "
      "reflexes of the PAN consonants (in Dyen's symbols *D, *d', *Z, *g', *γ) in some thirty Formosan dialects "
      "(five Atayal, three Sediq, Tsou, Kanakanavu, Saaroa, three Rukai, two Bunun, Paiwan, two Puyuma, Thao, "
      "Saisiyat, Pazeh, Kavalan, two Amis, Taokas, Babuza, Papora, Hoanya, Siraya); it was looked at on one page "
      "image and not read.",
      "Mark Marck's rows that Walworth questions as disputed, with her page. Enter Li's (1985) Table 2 for the "
      "dialects that are lects, from enlarged page images.",
      "261-262")
b.t["decisions"][-1]["source_id"] = "li1985"
if __name__ == "__main__":
    write(BATCH, b.t, f"""# ross2012-table4

Ross (2012: 1274-1275), Table 4: {n} rows for cells of lects that had no row for the phoneme (Taokas, Papora,
Hoanya, Favorlang, Proto-Atayal, Siraya, Amis). Parsed from the text layer (`ross2012_table4.json` in the script
folder), five lines repaired by hand. The page image of p. 1274 was looked at (low resolution), not compared
cell by cell; p. 1275 was not opened as an image. Tseng (2023) Table 6.4 and Ross's Table 9 add nothing beyond it.
""")
