#!/usr/bin/env python3
"""Smith (2023) Tables 6-7 and Smith (2025) Table 7: the cells that were not yet rows.

Batch smith2023-2025-tables (gap audit of 26 November 2026). Each table was compared with the rows already in
cldf/ (Blust 2002, 2007; Smith 2017a; Grimes & Edwards 2026); only what they did not say is entered.
BATCH.md lists every table of the audit items read in this session and what was done with it.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, existing

D = "smith2023-2025-tables"
LECTS = existing("lects", "id")
b23 = Batch("smith2023")
b25 = Batch("smith2025")

# ================================================================== Smith (2023: 354), Table 6: Miri
for lect in ("miri1269", "bega1240", "sabu1255", "kamb1299", "keda1252", "komo1261", "sika1262", "lioo1240",
             "ngad1261"):
    assert lect in LECTS, lect

T6 = ("Table 6 gives the 'typical reflexes of voiced plosives in medial position in North Sarawak languages'; the "
      "shaded column is the reflex of the pre-PNS geminate, PNS voiced aspirate (p. 354). ")
b23.corr("miri1269", "jʰ", "s", "V_V", "354",
         T6 + "Smith (2017a) has s in Miri only as a sporadic reflex of *j. Blust (2013: 556, Table 8.20) has the "
         "same reflex (his PNS *jS > Miri s).",
         derivation="", decision=D, locator="Table 6", as_printed="PNS *jʰ [dʃ] : Miri s")
b23.corr("miri1269", "ɡʰ", "k", "V_V", "354",
         T6 + "Blust (2013: 556, Table 8.20) has the same reflex (his PNS *gS > Miri k).",
         derivation="", decision=D, locator="Table 6", as_printed="PNS *gʰ : Miri k")

# ================================================================== Smith (2023: 355), Table 7: Begak
T7 = ("Table 7, 'Reflexes of voiced plosives in medial position in Bario Kelabit and Idaan Begak' (p. 355). The "
      "shaded column is the reflex of the geminate, which arose after a penultimate schwa and from assimilated "
      "clusters (p. 353). ")
b23.corr("bega1240", "ɡ", "ɡ", "V_V", "355",
         T7 + "The plain reflex. Smith (2017a: 228, Table 70) has no row for *g.",
         derivation="stated-retention", decision=D, locator="Table 7", as_printed="*g : Idaan Begak g")
b23.corr("bega1240", "ɡ", "ɡk", "ə_", "355",
         T7 + "The environment is written here as after schwa, the main source of the geminates; a geminate from a "
         "cluster (PMP *butbut > pre-PNS *bubːut) can follow any vowel (p. 353). The rows from Smith (2017a) have "
         "bp, dt and ɡk as sporadic reflexes between vowels.",
         decision=D, derivation="", locator="Table 7", as_printed="*g : Idaan Begak gk")
b23.corr("bega1240", "R", "∅", "V_V", "355",
         "'In Idaan Begak *R deleted in medial position except after schwa, where it became gk. In the final and "
         "initial positions, *R became g' (p. 355; Table 7 has *R : Ø, gk). This differs from Smith (2017a: 228, "
         "Table 70), which has *-R- > g; gk for Begak and is the source of the row *R > ɡ / V_V; his text there "
         "says that *-R- became *h in Sabah except after schwa (p. 229).",
         derivation="", decision=D, locator="Table 7", as_printed="*R : Idaan Begak Ø")

# ================================================================== Smith (2025: 672), Table 7: Bima-Lembata
P = "672"
T = ("Table 7, 'Reflexes of word-final glides in Bima-Lembata' (p. 672), states the reflex against PMP; the row "
     "names PMP as its predecessor. ")


def diph(lect, v, g, out, notes, cond=""):
    """PMP *-Vg > out: the vowel and the glide fuse (two paired rows)."""
    for par, env in ((v, f"_+{g}"), (g, f"{v}+_")):
        b25.corr(lect, par, out, env, P, T + notes, derivation="", decision=D, locator="Table 7",
                 as_printed=f"*{v}{g} reflex: {out}", conditioning=cond)
        b25.t["correspondences"][-1]["parent_lect_id"] = "pmp"


diph("sabu1255", "a", "y", "e",
     "Smith's Hawu. The rows from Grimes & Edwards (2026) have *aw > o and *uy > i on Proto-Havu-Dhao, as this table "
     "does, and no row for *ay.")
diph("kamb1299", "a", "y", "i", "No row on the Sumba nodes states the final diphthongs.")
diph("kamb1299", "a", "w", "u", "No row on the Sumba nodes states the final diphthongs.")
diph("kamb1299", "u", "y", "i", "No row on the Sumba nodes states the final diphthongs.")
diph("keda1252", "a", "y", "e", "'[Glide truncation] does not appear in any form in Flores-Lembata' (p. 671).")
diph("keda1252", "a", "w", "o", "'[Glide truncation] does not appear in any form in Flores-Lembata' (p. 671).")
diph("keda1252", "u", "y", "i", "'[Glide truncation] does not appear in any form in Flores-Lembata' (p. 671).")
diph("komo1261", "u", "y", "i",
     "*ay > e and *aw > o are already rows (Komodo, Proto-West Flores) from Grimes & Edwards (2026).")
diph("sika1262", "u", "y", "i", "*ay > e and *aw > o are already rows from Grimes & Edwards (2026).")
for lect, name in (("lioo1240", "Lio"), ("ngad1261", "Ngadha")):
    diph(lect, "a", "y", "e",
         f"The table has a/e for {name}, with the cell outlined as possible glide truncation; Smith gives no "
         "condition for the two reflexes. The a reflex is the row *y > ∅ / a_# of Proto-Central Flores (Grimes & "
         "Edwards 2026); this row is the e reflex. *aw > a and *uy > u/i agree with the Proto-Central Flores rows.",
         cond="unknown")

b25.t["decisions"] = []
b23.dec(D,
        "Smith (2023) Tables 6-7 and Smith (2025) Table 7, and the other tables of the gap audit of 26 November 2026 "
        "read with them (Robinson & Lobel 2013 Tables 4, 10; Blust 2013 Tables 8.20, 8.21, 8.24, 8.31; Smith 2017c "
        "Tables 2, 3, 8; Smith 2023 Tables 8-9): what is entered?",
        "Only the cells that were not yet rows. Miri *jʰ > s and *ɡʰ > k (Smith 2023, Table 6). Begak *ɡ > ɡ and ɡk "
        "after schwa, and *R > ∅ between vowels (Smith 2023, Table 7), the last beside the existing row *R > ɡ / V_V "
        "from Smith (2017a, Table 70), which it contradicts. From Smith (2025, Table 7), stated against PMP "
        "(parent_lect_id pmp): Havu *ay > e; Kambera *ay > i, *aw > u, *uy > i; Kedang *ay > e, *aw > o, *uy > i; "
        "Komodo and Sika *uy > i; Lio and Ngadha *ay > e beside the truncated reflex a that Proto-Central Flores "
        "already has. Everything else in the tables is already a row from Blust (2002, 2007), Smith (2017a), Mead "
        "(2003), Billings & McDonnell (2024), Nothofer (1975) or Grimes & Edwards (2026), or concerns a variety that "
        "is not a lect.",
        "Enter the Manggarai (*ay > a/i, *aw > o, *uy > i) and Lamaholot (*ay > a/e, *aw > a/o, *uy > i) rows of "
        "Smith (2025) Table 7 on Proto-Manggarai and Proto-Lamaholot, or on one dialect each; they are held back "
        "because Smith's 'Manggarai' and 'Lamaholot' name a language that is a proto-language with dialects here. "
        "Make lects of Lebo' Vo', Lepo' Tau and Penan (Smith 2023, Table 6), Long Anap Kenyah (Blust 2013, Table "
        "8.20), Tiruray (Smith 2023, Table 9), Moken (Smith 2017c, Table 3), Kasiguranin and the Cagayan Valley "
        "languages (Robinson & Lobel 2013, Tables 4, 10). Restate the Proto-North Sarawak rows *b > *bʰ etc., now "
        "'conditions unknown', with the conditions of Blust (2013: 557-558) and Smith (2023: 353): after penultimate "
        "schwa, and from assimilated clusters. Restate the Begak and Idaan rows bp, dt, ɡk (now sporadic, V_V) the "
        "same way, and replace Begak *R > ɡ / V_V by ∅. Enter the low vowel fronting of Robinson & Lobel's Table 4 "
        "language by language, with its lexemes (now one sporadic row on Proto-Northeastern Luzon). Smith (2017c) "
        "Table 2 has Karo -k for final *j; the Proto-Northern Batak row from Billings & McDonnell (2024) and "
        "Adelaar (1981) has -ŋ, and is left as it is.",
        "353-355; Smith 2025: 671-672")

tables = {k: b23.t[k] + b25.t[k] for k in b23.t}
write(D, tables, """# smith2023-2025-tables

Sources: Smith (2023), *Oceanic Linguistics* 62(2), Tables 6-7 (pp. 354-355; PDF pages 32-33), and Smith (2025),
*Diachronica* 42(5), Table 7 (p. 672; PDF page 27). The three tables were read from the text layer and compared
with page images. The other tables below were read from the text layer only.

These are the next items of the gap audit of 26 November 2026. Every table was compared with the rows in `cldf/`
before anything was entered; most of them repeat rows that are already there.

| Source, table | Result |
|---|---|
| Robinson & Lobel (2013) Table 4 (p. 137), low vowel fronting | not entered: the change is one sporadic row on Proto-Northeastern Luzon; the table shows it word by word in each language (see the decision) |
| Robinson & Lobel (2013) Table 10 (p. 155), *s > t and *ti > s | nothing to enter: the Northeastern Luzon languages do not have the changes, and the Cagayan Valley languages are not lects |
| Blust (2013) Table 8.20 (p. 556), PNS *S clusters | already rows (Kiput, Miri, Bintulu, the Kelabit dialects), except Miri *jʰ, *ɡʰ, entered from Smith (2023). Long Anap Kenyah is not a lect. Blust has Bintulu b/v, r, j, g where the rows from Smith (2017a) have v, ɣ, ʄ, ɠ |
| Blust (2013) Table 8.21 (p. 557), revised PNS sources | lexemes for the same reflexes; the conditions (after schwa, assimilated clusters) are not on the PNS rows (see the decision) |
| Blust (2013) Table 8.24 (p. 567), final *ʔ, *q, ∅ after Zorc | not entered: Tagalog, Bikol, Aklanon, Cebuano, Western Bukidnon Manobo, Kalamian Tagbanwa, Tboli, Malay and Old Javanese are not lects, and Blust treats PAn *ʔ as unsettled |
| Blust (2013) Table 8.31 (p. 590), *-ey and *-ew after Nothofer | not entered: Blust leaves the correspondences 'unexplained'; the Javanese and Sundanese reflexes of *-ay, *-aw are rows from Nothofer (1975); Tagalog, Malay and Madurese are not lects |
| Smith (2017c) Table 2 (p. 458), *j in Sumatra | already rows from Billings & McDonnell (2024): PMP *j > Proto-Sumatran *ɡ and its reflexes. Karo final -k differs (see the decision) |
| Smith (2017c) Table 3 (p. 459), *j in Moken | not entered: Moken is not a lect |
| Smith (2017c) Table 8 (p. 473), Proto-Celebic | already rows of Proto-Celebic from Mead (2003), whom Smith cites |
| Smith (2023) Table 6 (p. 354), North Sarawak voiced plosives | Miri *jʰ > s, *ɡʰ > k entered; the rest are rows already; Lebo' Vo', Lepo' Tau and Penan are not lects |
| Smith (2023) Table 7 (p. 355), Bario Kelabit and Begak | Begak *ɡ > ɡ, ɡk and *R > ∅ entered; the rest are rows already |
| Smith (2023) Table 8 (p. 356), stages in North Borneo | not entered: Smith's reading of Blust's PGNB, PNB, PSWS, PNES stages, which he argues against; intermediate nodes are held back |
| Smith (2023) Table 9 (p. 359), geminate-triggered splits | nothing to enter: Sekapan is covered by Proto-Kajang *b > v, b / ə_; Tiruray is not a lect; the Kambera split (*j > r, d after schwa; *b > w, b after schwa) is shown with four words and not stated as a rule |
| Smith (2025) Table 7 (p. 672), final glides in Bima-Lembata | 22 rows for Havu, Kambera, Kedang, Komodo, Sika, Lio, Ngadha; Bima is complete already; Manggarai and Lamaholot held back (see the decision) |

The rows from Smith (2025) name PMP in `parent_lect_id`, because the table states the reflexes against PMP and the
lects hang under Grimes & Edwards's nodes.

After the merge, two source notes in the sheet say that no sound correspondences are entered from Smith (2023) and
Smith (2025); `sheet_edits.py` beside the script has the new text.
""")
