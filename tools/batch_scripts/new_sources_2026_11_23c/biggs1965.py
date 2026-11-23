"""Batch biggs1965-rotuman: Biggs (1965), the two sets of Rotuman reflexes (direct and indirect inheritance).

Biggs, Bruce. 2004 [1965]. Direct and indirect inheritance in Rotuman. In Jan Tent & Paul Geraghty (eds.), Borrowing:
A Pacific perspective, 1-32. Canberra: Pacific Linguistics. (First published in Lingua 14. 383-415.)
Read from the PDF in Downloads (OCR text layer; Table 5 read from the page image).

    python3 tools/batch_scripts/new_sources_2026_11_23c/biggs1965.py

Biggs states the reflexes against Proto-Eastern Oceanic (PEO), which is not a node in the data; Rotuman's parent is
PCP (Geraghty 1986), whose Rotuman rows are Biggs's Set I (direct inheritance). Only Set II (indirect inheritance,
words that re-entered Rotuman from a Polynesian language) is entered here, as loan-stratum rows against PCP, for the
PEO phonemes whose PCP counterpart is clear from Set I matching Geraghty's reflex.
"""
from common import existing, write

S = "biggs1965"
assert S in existing("sources", "id")
rows = []
STRATUM = "Set II (indirect inheritance)"
NOTE = ("Set II reflex (Table 5, p. 7): found in words that re-entered Rotuman from a collateral (Polynesian) language, "
        "'indirectly inherited'; diagnostic Set II reflexes do not co-occur with diagnostic Set I ones in a word (pp. 6-8). "
        "Biggs's PEO *{peo} = PCP *{pcp}: its Set I reflex {set1} is Geraghty's (1986) reflex of PCP *{pcp}.")


def c(parent, child, peo, set1, notes="", examples="", printed=""):
    rows.append(dict(id=f"rotu1241-bg65-{len(rows) + 1}", child_lect_id="rotu1241", parent_phoneme=parent,
                     child_phoneme=child, environment="elsewhere", status="loan-stratum", stratum=STRATUM, source_id=S,
                     page="7-8", locator="Table 5", notes=(NOTE.format(peo=peo, pcp=parent, set1=set1) + " " + notes).strip(),
                     examples=examples, as_printed=printed or f"PEO *{peo} > II {child}"))


c("v", "f", "p", "h", "Doublet híti ~ fíti < PEO *pi(n)ti (p. 7).", "PEO *pi(n)ti > fíti 'to spring'")
c("b", "p", "mp", "p", "Not diagnostic: the same in both sets.")
c("t", "t", "t", "f", "Doublet fóʔa ~ tóka < PEO *toka (p. 7).", "PEO *toka > tóka 'to cease'")
c("d", "t", "nt", "t (medially; f initially)", "Biggs gives Set I f for initial *nt- and t for medial *-nt-; Geraghty "
  "has t for PCP *d. Set II has t in both positions.")
c("r", "r", "d", "r", "Set II prints r/Ø.", printed="PEO *d > II r/Ø")
c("r", "∅", "d", "r", "Set II prints r/Ø.", printed="PEO *d > II r/Ø")
c("dr", "r", "nd", "t")
c("k", "k", "k", "ʔ", "Doublet séʔe ~ sǽke < PEO *(n)sake (p. 7).", "PEO *(n)sake > sǽke 'project'")
c("ɡ", "k", "ŋk", "k", "Not diagnostic: the same in both sets.")
c("l", "r", "l", "l", "Doublet lúmu ~ rímu < PEO *limu (p. 7).", "PEO *limu > rímu 'lichen sp.'")
c("ʔ", "ʔ", "q", "Ø")
c("s", "s", "s", "s", "Set II prints s/h.", printed="PEO *s > II s/h")
c("s", "h", "s", "s", "Set II prints s/h; doublet sí'i ~ hiki < PPn *siki (p. 7).", "PPn *siki > hiki 'to exaggerate'",
  printed="PEO *s > II s/h")

DECISIONS = [dict(
    id="biggs1965-sets", question="Biggs (1965) gives two sets of Rotuman reflexes of Proto-Eastern Oceanic consonants "
    "(Table 5): Set I in directly inherited words, Set II in words that re-entered Rotuman from a Polynesian language. How "
    "are they entered?",
    chosen_reading="Set II only, as loan-stratum rows on Rotuman against PCP (stratum 'Set II (indirect inheritance)'): "
                   "Set I is Geraghty's (1986) PCP > Rotuman table, already in the data. A PEO phoneme is mapped to PCP "
                   "where its Set I reflex matches Geraghty's (PEO *p = PCP *v, *mp = *b, *nt = *d, *d = *r, *nd = *dr, "
                   "*ŋk = *ɡ, *q = *ʔ). Not entered: PEO *R, *r, *ns (no clear PCP counterpart), *m, *n, *ŋ, *w, *y (the "
                   "same in both sets), the vowels and the short forms (§3.1, Tables 3-4), and Table 1 (PEO with PAn and "
                   "PPn).",
    alternatives="Add a Proto-Eastern Oceanic node.", status="open", source_id=S, page="1-8")]

MD = """# biggs1965-rotuman

Biggs, Bruce. 2004 [1965]. Direct and indirect inheritance in Rotuman. In Jan Tent & Paul Geraghty (eds.), *Borrowing: A Pacific perspective*, 1-32. Canberra: Pacific Linguistics. Generator: `tools/batch_scripts/new_sources_2026_11_23c/biggs1965.py`.

Entered: the Set II (indirect inheritance) reflexes of Table 5 as loan-stratum rows on Rotuman against PCP. Set I is Geraghty's (1986) table, already in the data. Decision `biggs1965-sets` (open).
"""
write("biggs1965-rotuman", dict(correspondences=rows, decisions=DECISIONS), MD)
