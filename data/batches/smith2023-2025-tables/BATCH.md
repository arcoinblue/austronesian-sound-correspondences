# smith2023-2025-tables

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


## Applied

2026-11-26 08:59 UTC, by the push-batch workflow.
- correspondences: sheet rows 23442-23468
- decisions: sheet rows 261-261
