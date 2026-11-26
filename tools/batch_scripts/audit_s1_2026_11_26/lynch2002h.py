#!/usr/bin/env python3
"""Lynch (2002h), The Proto-Oceanic labiovelars: the cells of Table 3 (p. 315) that were not yet rows.

Batch lynch2002h-table3. Decision lynch2002h-table3 (reverted by the user on 24 November 2026: 'PEOc only as an
alternative proposal') left undone 'the cross-over reflexes of Table 3 (Nemi, Pohnpeian) and Mota, which need the
PDF and PNCV's consonants'. Table 3 states the reflexes against POc, so the rows whose lect does not descend
directly from POc name POc as their predecessor (parent_lect_id, a column added on 26 November 2026).
The table was read from a page image (170 dpi).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, existing

BATCH = D = "lynch2002h-table3-rows"
S = "lynch2002h"
LECTS = existing("lects", "id")
b = Batch(S)
T3 = ("Table 3, 'Sample reflexes of labiovelars and labials' (p. 315), 'a small sample of reflexes of the three "
      "labiovelars and the corresponding bilabials in a few representative diagnostic languages' (p. 314), after "
      "Geraghty (1983) and Ross (1988). ")


def row(lect, par, child, printed, notes="", env="elsewhere", status="regular", form="", pl="poc", blank=""):
    assert lect in LECTS or lect == "waya1268", lect
    b.corr(lect, par, child, env, "315", T3 + notes, status=status, derivation="as-stated", decision=D,
           locator="Table 3", as_printed=printed, source_form=form, blank_type=blank)
    if pl:
        b.t["correspondences"][-1]["parent_lect_id"] = pl


# Mota (NCV): its parent PNCV has no rows for the stops, so every cell is new.
M = "mota1237"
row(M, "bʷ", "k͡pʷ", "*bw : Mota kpw", form="kpw", notes="Printed with a raised k: a labial-velar stop, Mota q.")
row(M, "b", "p", "*b : Mota p")
row(M, "pʷ", "v", "*pw : Mota v (w)")
row(M, "pʷ", "w", "*pw : Mota v (w)", env="conditions unknown", notes="The reflex in brackets.")
row(M, "p", "p", "*p FORTIS : Mota p", env="fortis grade")
row(M, "p", "v", "*p LENIS : Mota v (w)", env="lenis grade")
row(M, "p", "w", "*p LENIS : Mota v (w)", env="lenis grade (conditions unknown)", notes="The reflex in brackets.")
row(M, "mʷ", "mʷ", "*mw : Mota mw")
row(M, "m", "m", "*m : Mota m")

# Loniu (Admiralties): Proto-Admiralty has the POc phonemes, so no parent_lect_id.
LO = "loni1238"
row(LO, "bʷ", "pʷ", "*bw : Loniu pw", pl="")
row(LO, "pʷ", "p", "*pw : Loniu p,pw", env="conditions unknown", pl="",
    notes="Two reflexes with no conditions; '*pw has far fewer labiovelar reflexes' than *bw and *mw (p. 314).")
row(LO, "pʷ", "pʷ", "*pw : Loniu p,pw", env="conditions unknown (labiovelar kept)", pl="")
row(LO, "mʷ", "mʷ", "*mw : Loniu mw-mw-m", env="V_V", pl="",
    notes="Printed as initial-medial-final; the initial reflex is a row from Ross (1988: 321).")
row(LO, "mʷ", "m", "*mw : Loniu mw-mw-m", env="_#", pl="", notes="Printed as initial-medial-final.")

# Manam, Dobu: one cell each that Ross's (1988) rows lack.
row("mana1295", "pʷ", "p", "*pw : Manam p", pl="",
    notes="Manam is under POc. The cells *bw 'bo' and *mw 'mo' (the labiovelar as a labial followed by o) are "
          "Ross's (1988: 126-128) rows bʷ and mʷ.")
row("dobu1241", "pʷ", "p", "*pw : Dobu p,pw", env="conditions unknown",
    notes="Beside pw, which is a row from Ross (1988: 198), stated against Proto-Papuan Tip.")

# Nemi (New Caledonia): the cross-over reflexes.
NE = "nemi1240"
row(NE, "bʷ", "ᵑɡ", "*bw : Nemi ŋg, mbw", env="conditions unknown", form="ŋg",
    notes="A cross-over reflex: a velar for the labiovelar (§3.3). Listed first.")
row(NE, "bʷ", "ᵐbʷ", "*bw : Nemi ŋg, mbw", env="conditions unknown (labiovelar kept)", form="mbw")
row(NE, "pʷ", "pʷ", "*pw : Nemi pw?", status="disputed", notes="Printed with a question mark.")
row(NE, "mʷ", "ŋ", "*mw : Nemi ŋ,mw", env="conditions unknown",
    notes="A cross-over reflex: a velar for the labiovelar (§3.3). Listed first.")
row(NE, "mʷ", "mʷ", "*mw : Nemi ŋ,mw", env="conditions unknown (labiovelar kept)")

# Tongan: PCP has no *bw, *pw, so these two cells cannot be read off the PCP > PPn > PTo chain.
row("tong1325", "bʷ", "p", "*bw : Tongan p")
row("tong1325", "pʷ", "p", "*pw : Tongan p")

# Wayan (Western Fijian), a lect of batch geraghty1983-communalects in this same set.
W = "waya1268"
row(W, "bʷ", "ɡ", "*bw : Wayan mb,ŋg", env="conditions unknown", form="ŋg",
    notes="A cross-over reflex beside mb [b in the Fijian spelling used here], which is the row from Geraghty "
          "(1983: 183). The prenasalized velar stop is written ɡ as in the other Fijian lects.")
row(W, "mʷ", "ŋ", "*mw : Wayan ŋ,ŋw", env="conditions unknown",
    notes="Listed before ŋw, which is the row from Geraghty (1983: 185, PEO *mw > gw).")

b.dec(D,
      "Lynch (2002h) Table 3 (p. 315): which cells are entered now that the PDF is at hand and a row can name its "
      "predecessor?",
      "The cells that were not rows: Mota (all seven columns; nine rows), Loniu *bw, *pw and medial and final *mw, "
      "Manam and Dobu *pw > p, Nemi's cross-over reflexes (*bw > ŋg beside mbw, *mw > ŋ beside mw, *pw 'pw?' as "
      "disputed), Tongan *bw and *pw > p, Wayan *bw > ŋg and *mw > ŋ. Rows of lects that do not descend directly "
      "from POc name POc as predecessor (parent_lect_id poc): Mota (under PNCV), Nemi (under Proto-New Caledonian), "
      "Tongan (under Proto-Tongic), Dobu (under Proto-Papuan Tip), Waya (under PCP). Not entered: Lau (Solomons), "
      "which is not a lect; Anejom̃, whose cells are the Lynch (2001) rows through Proto-Southern Vanuatu; "
      "Pohnpeian (pw beside p for *b, mw beside m for *m), which are the PMc rows 'before round vowels' of Bender "
      "et al. (2003a); the PEOc row (*p fortis, *v lenis), since Proto-Eastern Oceanic is an alternative node "
      "without rows (the user's decision); Table 4 and the appendix, which are word lists.",
      "Enter the Pohnpeian doublets as sporadic rows on Pohnpeian; add Lau (lauu1247) as a lect.",
      "315")

if __name__ == "__main__":
    write(BATCH, b.t, """# lynch2002h-table3-rows

Lynch (2002h: 315), Table 3, read from a page image: the cells that were not yet rows (Mota, Loniu, Manam, Dobu,
Nemi, Tongan, Wayan). Rows of lects that are not daughters of POc carry `parent_lect_id` `poc`. Depends on batch
`geraghty1983-communalects` for the lect `waya1268`. Table 4 (p. 325) and the appendix are word lists.
""")
