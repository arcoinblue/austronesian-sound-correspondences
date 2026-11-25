#!/usr/bin/env python3
"""Tryon (1994), Language contact and contact-induced language change in the Eastern Outer Islands, Solomon Islands.

In Dutton & Tryon (eds.), Language contact and change in the Austronesian world, 611-648. Appendix 1 (pp. 638-645):
the reflexes of POC consonants, initial and medial, in 17 lects numbered as in Tryon & Hackman (1983): Reefs, Malo,
Lwepe, Nanggu (Reefs-Santa Cruz), Nembao, Asumboa, Tanimbili (Utupua), Buma, Vano, Tanema (Vanikoro), Bellona,
Rennell, Ontong Java, Sikaiana, Pileni, Tikopia, Anuta (Polynesian Outliers). Transcribed from the page images.

Tryon writes POC in Grace's (1969) orthography: mp = b, nt = d, ŋk = ɡ, ŋp = bʷ, ŋm = mʷ, d = r, nd = dr, ns = j.
Every row is restated against the lect's parent (decision tryon1994-composition): the Temotu lects through the
sheet's chain POC > PTm > PRSC/PUtupua/PVanikoro, the Outliers against PNP through the standard POC > PPN > PNP
correspondences (the sheet's POC > PCP rows are incomplete; PNP's daughters change none of these consonants).
"""
from collections import OrderedDict
from common import Batch, write, chapter, CONSULTED
from chain import reflex, LECTS

S = "tryon1994"
b = Batch(S)
b.t["sources"].append(chapter(
    S, "Tryon, Darrell T.",
    "Language contact and contact-induced language change in the Eastern Outer Islands, Solomon Islands",
    "611-648",
    CONSULTED + "The languages of Temotu Province (§2): Santa Cruz (Nendö), Nanggu, Ayiwo (Reefs), Pileni, "
    "Tikopia-Anuta, Nembao, Asumboa, Tanimbili (Utupua), Buma, Vano, Tanema (Vanikoro); their status (§3), "
    "grammatical sketches (§4), morphosyntactic contact phenomena (§5) and Polynesian loans (§5.1). Reefs and "
    "Santa Cruz are marked Papuan (non-Austronesian) after Wurm. Appendix 1 (pp. 638-645): POC consonant "
    "correspondences in 17 lists of Tryon & Hackman (1983), initial and medial, with footnotes; Appendix 2: shared "
    "cognate percentages. Glottocodes of Ross et al. (2023)."))

# --- lects -------------------------------------------------------------------------------------------------
LW = "lwepe"
b.t["lects"] += [
    dict(id="malo1246", name="Malo", alt_names="Santa Cruz (Malo);S. Cruz Mal", type="dialect", glottocode="malo1246",
         parent_id="prsc", language_id="natu1246", latitude="-10.68038", longitude="165.89784",
         region="Nendö, Santa Cruz Islands", inherit="assumed-unchanged", inherit_source_id=S, inherit_page="638-645",
         notes="List 96 of Tryon & Hackman (1983) and Tryon (1994: 638-645), a Santa Cruz (Natügu) dialect; 97.1% "
               "cognate with Lwepe (Appendix 2, p. 646). Glottolog's Malo, a dialect of Natügu. Coordinates from "
               "Glottolog 5.4."),
    dict(id=LW, name="Lwepe", alt_names="Santa Cruz (Lwepe);S. Cruz L", type="dialect", glottocode="natu1246",
         parent_id="prsc", language_id="natu1246", latitude="-10.69", longitude="165.87",
         region="Nendö, Santa Cruz Islands", inherit="assumed-unchanged", inherit_source_id=S, inherit_page="638-645",
         notes="List 97 of Tryon & Hackman (1983) and Tryon (1994: 638-645), 'S. Cruz L', a Santa Cruz dialect 97.1% "
               "cognate with Malo (p. 646). Glottolog has no code for it; it shares Natügu's. Coordinates are "
               "Natügu's (Ross et al. 2023: 626)."),
    dict(id="pile1238", name="Pileni", alt_names="Vaeakau-Taumako;Pil", type="language", glottocode="pile1238",
         iso639_3="piv", parent_id="pnp", latitude="-10.17", longitude="166.25",
         region="Pileni, Nupani, Nukapu and Matema (Reef Islands), and Taumako (Duff Islands)",
         inherit="assumed-unchanged", inherit_source_id=S, inherit_page="638-645",
         notes="Polynesian Outlier, list 109 of Tryon & Hackman (1983) (Tryon 1994: 612, 638-645); Glottolog's "
               "Vaeakau-Taumako. Placed under PNP, the lowest node every classification in the sheet agrees on "
               "(decision tryon1994-composition). Coordinates from Ross et al. (2023: 627)."),
]

PARENT = {
    "ayiw1239": "prsc", "malo1246": "prsc", LW: "prsc", "nang1262": "prsc",
    "amba1266": "putupua", "asum1237": "putupua", "tani1255": "putupua",
    "tean1237": "pvanikoro", "vano1237": "pvanikoro", "tane1237": "pvanikoro",
    "mung1270": "psso", "mung1271": "psso", "onto1237": "pcno", "sika1261": "psnoep", "pile1238": "pnp",
    "tiko1237": "psso", "anut1237": "psso",
}
NAMES = {"ayiw1239": "Reefs", "malo1246": "Malo", LW: "Lwepe", "nang1262": "Nanggu", "amba1266": "Nembao",
         "asum1237": "Asumboa", "tani1255": "Tanimbili", "tean1237": "Buma", "vano1237": "Vano",
         "tane1237": "Tanema", "mung1270": "Bellona", "mung1271": "Rennell", "onto1237": "Ontong Java",
         "sika1261": "Sikaiana", "pile1238": "Pileni", "tiko1237": "Tikopia", "anut1237": "Anuta"}
ORDER = ["ayiw1239", "malo1246", LW, "nang1262", "amba1266", "asum1237", "tani1255", "tean1237", "vano1237",
         "tane1237", "mung1270", "mung1271", "onto1237", "sika1261", "pile1238", "tiko1237", "anut1237"]
OUTLIERS = set(ORDER[10:])
# POC (Ross) > PNP, for the Outliers' parents (all below PNP, which change none of these)
PNP = {"p": "f", "b": "p", "bʷ": "p", "t": "t", "d": "t", "k": "k", "ɡ": "k", "q": "ʔ", "r": "l", "dr": "l",
       "l": "l", "m": "m", "mʷ": "ŋ", "n": "n", "ñ": "n", "ŋ": "ŋ", "s": "s", "j": None, "w": "w", "y": None,
       "R": None}

# --- the tables: columns (Grace symbol, Ross phoneme, position), pages, footnotes, rows -----------------------
# A cell is a comma-separated list of reflexes; a trailing number is the footnote; '(?)' marks doubt.
TABLES = [
    dict(page="638-639", cols=[("p", "p", 0), ("p", "p", 1), ("mp", "b", 0), ("mp", "b", 1), ("t", "t", 0),
                               ("t", "t", 1), ("nt", "d", 0), ("nt", "d", 1)],
         notes={1: "Before non-high vowels mainly.", 2: "Before POC *a, reflecting POC *pakiwak 'shark' and *pano "
                "'go'; also in occasional loanwords, e.g. to-ponu (POC *poñu) 'turtle'; perhaps oral/nasal grade "
                "reflex mixing.", 3: "Doubtful correspondence; possibly only in loanwords.",
                4: "Apparently unconditioned reflex.", 5: "Mainly before high vowels; oral/nasal grade reflex mixing.",
                6: "Before POC *a, reflecting POC *pakiwak 'shark' and *pati 'four'.", 7: "Unexplained reflex.",
                8: "Mainly before non-low back vowels.", 9: "Reflecting POC *pilak 'lighting'; unexplained reflex.",
                10: "Reflex unexplained; perhaps in loanwords, cf. nahue 'paddle' and naŋa 'bow'.",
                11: "Word finally.", 12: "Before high vowels.", 13: "Word finally.", 14: "Apparently before POC *a.",
                15: "Reflecting POC *topu 'sugar-cane'; reflex unexplained.",
                16: "Reflecting POC *pakiwak 'shark' only."},
         rows=[["∅, v1, p2", "∅", "p", "p", "∅, t3", "∅, t3", "", ""],
               ["∅, v4, p5, pʷ6", "p, ∅7", "p", "", "∅, t8", "∅, t8", "", "ⁿd"],
               ["∅, v4, p5, pʷ6", "p, ∅7, w7", "p", "", "∅, t8", "∅, t8", "", ""],
               ["p, v9", "p, ᵐbʷ7", "ᵐb", "", "∅, t8", "∅, t8", "", "t"],
               ["v, ∅8, h10", "v, vʷ7", "", "", "r, t8", "r, t8", "", ""],
               ["v, ∅8, ᵐb11", "v, ∅7", "", "", "t, s4", "t, ⁿd11, s4, j8", "", ""],
               ["v, ∅8, p2, w7", "v, ∅7, p11", "", "", "t, s8, ∅7", "t, s8", "", "ⁿd͡ʒ"],
               ["v, ∅8, p11", "v, p11", "ᵐb", "", "t", "t, ⁿd11, s12", "", "ⁿd"],
               ["v, ∅13, p11", "v, p11", "ᵐb", "", "t, l14", "t, l14, s12", "", "t"],
               ["v, ∅8, b11", "v, p11", "b", "", "t, ∅14, r15", "t, ⁿd11, ∅14, s12", "", "ⁿd"],
               ["h", "h", "p", "p", "t", "t", "t", "t"],
               ["h", "h", "p", "p", "t", "t", "t", "t"],
               ["h", "h", "p", "p", "k", "k", "k", "k"],
               ["h, p16", "h", "p", "p", "t", "t", "t", "t"],
               ["h, p16, f7", "h", "p", "p", "t", "t", "t", "t"],
               ["f", "f", "p", "p", "t", "t", "t", "t"],
               ["p", "p", "p", "p", "t", "t", "t", "t"]]),
    dict(page="639-640", cols=[("k", "k", 0), ("k", "k", 1), ("ŋk", "ɡ", 0), ("ŋk", "ɡ", 1), ("q", "q", 0),
                               ("q", "q", 1)],
         notes={1: "Unconditioned reflex; possible oral/nasal grade reflex mixing.",
                2: "POC final *k retained in Vanikoro languages, reflecting, for example, *manuk 'bird' and *ñamuk "
                   "'mosquito'; a trace of POC *k remains also in Buma manda-u (POC *matakut) 'fear'.",
                3: "Reflecting POC *koe 'thou' only; unexplained reflex."},
         rows=[["∅, k1", "∅", "", "", "", ""], ["∅, k1", "∅", "", "∅", "", "∅"], ["∅, k1", "∅", "", "∅", "", "∅"],
               ["∅, k1", "∅", "", "", "", "∅"], ["∅, k1", "", "", "ᵑɡ", "", ""], ["∅, k1", "∅", "", "ᵑɡ", "", "∅"],
               ["∅, k1", "∅", "", "ŋk", "∅", "∅"], ["∅, k1", "∅", "", "", "∅", "∅"], ["k, ŋ3", "∅", "", "∅", "∅", "∅"],
               ["k, ŋ3", "∅", "", "∅", "", ""],
               ["k, ∅", "k", "", "k", "ʔ", "ʔ"], ["k, ∅", "k", "", "k", "ʔ", "ʔ"], ["ʔ, ∅", "ʔ", "ʔ", "ʔ", "∅", "∅"],
               ["k, ∅", "k", "", "k", "∅", "∅"], ["k, ∅", "k", "", "k", "∅", "∅"], ["k, ∅", "k", "k", "k", "∅", "∅"],
               ["k, ∅", "k", "k", "k", "∅", "∅"]]),
    dict(page="640-641", cols=[("ŋp", "bʷ", 0), ("ŋp", "bʷ", 1), ("d", "r", 0), ("d", "r", 1), ("nd", "dr", 0),
                               ("nd", "dr", 1)],
         notes={1: "Reflex unexplained.", 2: "Reflecting POC *daRaq 'blood' only; possible oral/nasal grade mixing.",
                3: "Uncertain reflex; only in naœ POC *ŋpatu 'head'.",
                4: "Reflex uncertain; reflecting POC *sida 'they' only.", 5: "Reflecting POC *ŋpoe 'pig' only.",
                6: "Reflex uncertain; reflecting POC *maqudip 'live' only.",
                7: "Uncertain reflex; insufficient examples; possible palatalisation (Asumboa and Tanimbili) "
                   "before front vowels.", 8: "Before back rounded vowels.",
                9: "In taru 'two' (POC *dua) only; possible borrowing.",
                10: "Apparently unconditioned reflex; nœtou 'they' pl., *nœua 'they' dl."},
         rows=[["p, ᵐb1", "", "l, ⁿd2", "", "", ""], ["p, ᵐb1, ∅3", "", "l", "ⁿd4 (?)", "l", ""],
               ["p, ᵐb1, ∅3", "", "l", "ⁿd4 (?)", "l", ""], ["p, ᵐb1, ∅3", "", "l", "", "l", ""],
               ["ᵐb, vʷ5", "", "l", "l", "l", ""], ["p", "", "j, l6", "", "l, ⁿd7 (?)", "ᶮɟ7 (?)"],
               ["p", "", "j", "", "l, ⁿd7 (?)", "ᶮɟ7 (?)"], ["ᵐb, pʷ8", "", "l", "ⁿd4 (?)", "", "ⁿd7 (?)"],
               ["ᵐb, pʷ8", "", "l, r9", "ⁿd4 (?)", "", ""], ["ᵐb", "", "l", "ⁿd4 (?)", "l", "ⁿd7 (?)"],
               ["p", "", "ŋ", "ŋ", "ŋ", ""], ["p", "", "ᵑɡ", "ᵑɡ", "ᵑɡ", ""], ["p", "", "l", "l", "l", ""],
               ["p", "", "l", "l", "l", ""], ["p", "", "l", "l", "l", ""], ["p", "", "r", "r", "r", ""],
               ["p", "", "r", "r, n10", "r", ""]]),
    dict(page="641-643", cols=[("m", "m", 0), ("m", "m", 1), ("n", "n", 0), ("n", "n", 1), ("ŋ", "ŋ", 0),
                               ("ŋ", "ŋ", 1)],
         notes={1: "Only reflecting POC *lima 'five', not 'hand, arm'; unexplained reflex.",
                2: "Reflecting POC *ŋpoŋi 'night'; reflex unexplained.", 3: "Reflex uncertain; insufficient examples.",
                4: "Only recorded reflecting POC *paŋa 'eat'.", 5: "Only in malo 'bird', possibly cognate with POC "
                "*manuk.", 6: "Before high vowels.", 7: "Only in no-loŋgo 'fly' (POC *laŋo).",
                8: "Only in ole 'sand' (POC *qone), intervocalically.",
                9: "Only in ᵐbʷoᵑgo 'night', probably cognate with POC *ŋpoŋi.",
                10: "Reflecting POC *taliŋa 'ear' only; apparently unconditioned reflex.",
                11: "Only in mʷaure 'left' (POC *mauRi); possible mishearing."},
         rows=[["m", "m, ∅1", "n", "n", "", "ŋ, ∅2"], ["m", "m, ∅1", "l3 (?)", "n", "n3 (?)", "n, ∅2"],
               ["m", "m, ∅1", "l3 (?)", "ⁿd4 (?)", "n3 (?)", "n, ∅2"], ["m", "m, ∅1", "", "n", "n3 (?)", "n, ∅2, ŋ4"],
               ["m", "m", "n", "n, l5", "n3 (?)", "n, ɲ6"], ["m", "m", "n, ɲ6", "n", "ŋ", "ŋ"],
               ["m", "m, ∅1", "n, ɲ6", "n, ɲ6", "ŋ", "ŋ, ᵑɡ7"], ["m", "m, ∅1", "l3 (?)", "n, l8", "ŋ", "ŋ, ᵑɡ9, ɲ10"],
               ["m", "m, ∅1", "n", "n", "", "ŋ, ɲ10"], ["m, mʷ11", "m, ∅1", "n", "n", "", "ŋ, ɲ10"],
               ["m", "m", "n", "n", "ŋ", "ŋ"], ["m", "m", "n", "n", "ŋ", "ŋ"], ["m", "m", "ŋ", "ŋ", "ŋ", "ŋ"],
               ["m", "m", "n", "n", "n", "n"], ["m", "m", "n", "n", "ŋ", "ŋ"], ["m", "m", "n", "n", "ŋ", "ŋ"],
               ["m", "m", "n", "n", "ŋ", "ŋ"]]),
    dict(page="642", cols=[("ŋm", "mʷ", 0), ("ŋm", "mʷ", 1), ("s", "s", 0), ("s", "s", 1), ("ns", "j", 0),
                           ("ns", "j", 1)],
         notes={1: "Reflex uncertain; insufficient examples.", 2: "Unconditioned reflex.",
                3: "Reflecting POC *nsai 'who'; reflex unexplained.", 4: "Reflecting POC *ŋmea 'tongue' only.",
                5: "Reflecting POC *susu 'breast', and *sala(n) 'road'; unexplained reflex.",
                6: "Observed only in ŋutu 'mouth'; POC *ŋusu; PPN *ŋutu.",
                7: "keʔaka (POC *ŋmata) 'snake' only; reflex uncertain.",
                8: "Reflecting POC *nsiwa 'nine' only; unexplained reflex.", 9: "tikutiku (POC *siku) 'tail' only."},
         rows=[["", "", "j1 (?)", "j1 (?)", "∅", "∅"], ["m", "m", "∅, j1 (?)", "j, s1 (?)", "∅", "∅"],
               ["m", "m", "∅, j1 (?)", "j, s1 (?)", "∅", "∅"], ["mʷ1", "m", "∅, j1 (?)", "j, s1 (?)", "∅", "∅"],
               ["m", "mʷ, m2", "", "", "h, ∅3", ""], ["mʷ, m4", "mʷ", "∅, j1 (?)", "∅, j1 (?)", "s, ∅3", "d͡ʒ, ∅2"],
               ["mʷ", "", "∅, j1 (?)", "∅, j1 (?)", "∅", "s, ∅2"], ["mʷ, m4", "mʷ", "", "s1", "", "∅, t1"],
               ["mʷ, m4", "mʷ", "", "s1", "s", "∅, t1"], ["m1", "", "", "", "s1", "∅"],
               ["ŋ", "ŋ", "s, ∅5", "s, ∅5, t6", "∅", "∅"], ["ŋ", "ŋ", "s, ∅5", "s, ∅5, t6", "∅", "∅"],
               ["ŋ, ʔ7", "ŋ", "s, ∅5", "∅", "∅, s8", "∅"], ["", "n", "s, ∅5", "∅", "∅, s8", "∅"],
               ["ŋ", "ŋ", "s, ∅5", "∅, t6", "∅", "∅"], ["ŋ", "ŋ", "s, ∅5", "∅, t6", "∅, s8", "∅"],
               ["ŋ", "ŋ", "s, ∅, t9", "∅, t6", "∅", "∅"]]),
    dict(page="643-645", cols=[("w", "w", 0), ("w", "w", 1), ("y", "y", 0), ("y", "y", 1), ("ñ", "ñ", 0),
                               ("ñ", "ñ", 1)],
         notes={1: "Only in one or two examples.", 2: "Doubtful correspondence; insufficient examples.",
                3: "Reflex unexplained.", 4: "ve-viro 'eight' (POC *walu); unexplained reflex.",
                5: "aru (POC *walu) 'eight' only."},
         rows=[["w1", "", "", "", "n", ""], ["w1", "", "", "", "∅2 (?)", ""], ["w1", "", "", "", "∅2 (?)", ""],
               ["", "", "", "", "∅2 (?)", ""], ["v, ∅3", "∅", "", "∅", "", "n"], ["∅", "w, ∅", "", "∅", "", "n"],
               ["w, ∅3, v4", "", "", "∅", "", ""], ["∅", "", "", "∅", "", "n"], ["w", "", "", "∅", "", "n"],
               ["∅", "", "", "∅", "", "n"],
               ["b", "b", "", "", "n", "n"], ["v", "v", "", "", "n", "n"], ["v", "v", "", "", "ŋ", ""],
               ["v", "v", "", "", "n", "n"], ["v", "v", "", "", "n", "n"], ["v", "v", "", "", "n", "n"],
               ["v, ∅5", "v", "", "", "n", "n"]]),
    dict(page="644-645", cols=[("l", "l", 0), ("l", "l", 1), ("r", "r", 0), ("r", "r", 1), ("R", "R", 0),
                               ("R", "R", 1)],
         notes={1: "Apparently unconditioned reflex.", 2: "Only in varo (POC *walu) 'eight'; probable borrowing.",
                3: "Only in kuli 'dog'; probable loanword.", 4: "Probable borrowing; ve-viro (POC *walu) 'eight'.",
                5: "Word final *R also retained in Vanikoro languages (Buma, Vano, Tanema), reflecting POC *waiR "
                   "'water'; Buma luro (POC *niR) 'coconut'; elsewhere in Eastern Outer Islands final *R is lost."},
         rows=[["l, ∅1", "l, ∅1", "", "", "l, ∅1", "l, ∅1"], ["l, ∅1", "l, ∅1", "", "", "l, ∅1", "∅"],
               ["l, ∅1", "l, ∅1", "", "", "l, ∅1", "∅"], ["l, ∅1", "l, ∅1", "", "", "l", "l, ∅1"],
               ["l", "l, ∅1, r2", "", "", "∅", "j"], ["", "∅, l3", "", "", "∅", "l"],
               ["l, ∅1, j1", "l, ∅1, r4", "ⁿd", "", "∅", "j"], ["l, ∅1", "l, ∅1", "", "", "∅", "r5"],
               ["l, ∅1", "l, ∅1", "ⁿd", "", "∅", "r5"], ["l, ∅1", "l, ∅1", "", "", "∅", "r5"],
               ["ŋ", "ŋ", "ŋ", "ŋ", "∅", "∅"], ["ᵑɡ", "ᵑɡ", "ᵑɡ", "ᵑɡ", "∅", "∅"], ["l", "l", "l", "l", "∅", "∅"],
               ["l", "l", "l", "l", "∅", "∅"], ["l", "l", "l", "l", "∅", "∅"], ["r", "r", "r", "r", "∅", "∅"],
               ["r", "r", "r", "r", "∅", "∅"]]),
]
# How the printed symbols map to IPA (only where they differ); kept in as_printed.
PRINT = {"j": "y", "ᵐb": "mb", "ⁿd": "nd", "ᵑɡ": "ŋg", "ᶮɟ": "nj̆", "ⁿd͡ʒ": "nǰ", "d͡ʒ": "ǰ", "ɲ": "ñ", "pʷ": "pw",
         "vʷ": "vw", "mʷ": "mw", "ᵐbʷ": "mbw", "b": "b"}
OVERRIDE_PRINT = {("asum1237", "mʷ"): "mu", ("malo1246", "w"): "u", (LW, "w"): "u"}
# Asumboa's 'mu' for POC *ŋm and Malo/Lwepe's 'u' for *w- are read as mʷ and w.


def classify(note):
    """(status, environment add-on) for a footnote."""
    n = note.lower()
    if note.startswith("Word final") and "*R" in note:
        return "regular", ""
    if "word finally" in n:
        return "regular", "_#"
    if "before non-high vowels" in n:
        return "regular", "_V[-high]"
    if "before high vowels" in n:
        return "regular", "_V[+high]"
    if "before non-low back vowels" in n:
        return "regular", "_V[+back, -low]"
    if "before back rounded vowels" in n:
        return "regular", "_V[+back, +round]"
    if "before poc *a" in n and "only" not in n:
        return "regular", "_a"
    if "apparently unconditioned" in n and "only" in n:
        return "sporadic", ""
    if "unconditioned" in n:
        return "regular", "conditions unknown"
    if "borrowing" in n or "loanword" in n:
        return "loan-stratum", ""
    if "uncertain" in n or "doubtful" in n or "insufficient" in n:
        return "disputed", ""
    return "sporadic", ""


def parse(cell):
    out = []
    for tok in [t.strip() for t in cell.replace("∅ ", "∅, ").split(",") if t.strip()]:
        doubt = "(?)" in tok
        tok = tok.replace("(?)", "").strip()
        num = ""
        while tok and tok[-1].isdigit():
            num = tok[-1] + num
            tok = tok[:-1]
        out.append((tok, [int(x) for x in num.split(",")] if num else [], doubt))
    return out


# Phonemes the chain yields but the parent's inventory (as the build generates it) does not have: PRSC's
# reflex of initial *p and of *ñ is not in the sheet (Lackey & Boerger 2021 give *p only between vowels and
# *ñ > *n as disputed). Such cells are not entered.
NOT_IN_PARENT = {("prsc", "p"), ("prsc", "ñ")}
D = "tryon1994-composition"
rows = OrderedDict()
skipped = []
for T in TABLES:
    for li, lect in enumerate(ORDER):
        par_lect = PARENT[lect]
        for (gr, ph, pos), cell in zip(T["cols"], T["rows"][li]):
            if not cell:
                continue
            if lect in OUTLIERS:
                X = PNP[ph]
            else:
                X, _ = reflex("poc", par_lect, ph)
            col = f"*{'-' if pos else ''}{gr}-"
            toks = parse(cell)
            if cell == "∅, k1,2":  # Buma: k carries footnotes 1 and 2
                toks = [("∅", [], False), ("k", [1, 2], False)]
            if X is None or (par_lect, X) in NOT_IN_PARENT:
                if X is not None or any(t[0] != "∅" for t in toks):
                    skipped.append((NAMES[lect], col, cell))
                continue
            base = "#_" if pos == 0 else "V_V"
            first = True
            for refl, fns, doubt in toks:
                orig = refl
                if lect == "tean1237":  # Teanu's sourced inventory writes the prenasalised stops b, d, ɡ
                    refl = {"ᵐb": "b", "ⁿd": "d", "ᵑɡ": "ɡ"}.get(refl, refl)
                fnote = " ".join(f"n. {f}: {T['notes'][f]}" for f in fns)
                if fns:
                    status, add = classify(T["notes"][fns[0]])
                    if 2 in fns and T is TABLES[1]:
                        status, add = "regular", "conditions unknown"
                elif first:
                    status, add = "regular", ""
                else:
                    status, add = "sporadic", ""
                if doubt:
                    status = "disputed"
                if len(toks) > 1 and status == "regular" and not add and not first:
                    add = "conditions unknown"
                if not add:
                    env = base
                elif add in ("_#", "conditions unknown"):
                    env = add
                else:
                    env = ("#_" if pos == 0 else "V_") + add[1:]
                first = False
                pr = OVERRIDE_PRINT.get((lect, orig)) or PRINT.get(orig, orig)
                key = (lect, X, refl, env, status)
                txt = (f"{col}{' (' + ('initial' if pos == 0 else 'medial') + ')' if add == 'conditions unknown' else ''} '{cell}'" + (f" ({fnote})" if fnote else "") + (" Printed '(?)'." if doubt else ""))
                if key in rows:
                    rows[key]["cols"].append(txt)
                    rows[key]["pos"].add(ph)
                else:
                    rows[key] = dict(cols=[txt], pos={ph}, page=T["page"], pr=pr, par=par_lect)
for lect in ("tean1237", "vano1237", "tane1237"):
    X, _ = reflex("poc", PARENT[lect], "k")
    rows[(lect, X, "k", "_#", "regular")] = dict(
        cols=["*k- n. 2: 'POC final *k retained in Vanikoro languages, reflecting, for example, *manuk 'bird' and "
              "*ñamuk 'mosquito''."], pos={"k"}, page="640", pr="k", par=PARENT[lect])
    X, _ = reflex("poc", PARENT[lect], "R")
    rows[(lect, X, "r", "_#", "regular")] = dict(
        cols=["*-R- n. 5: 'Word final *R also retained in Vanikoro languages (Buma, Vano, Tanema), reflecting POC "
              "*waiR 'water'; Buma luro (POC *niR) 'coconut'; elsewhere in Eastern Outer Islands final *R is lost'."],
        pos={"R"}, page="645", pr="r", par=PARENT[lect])

for (lect, X, refl, env, status), v in rows.items():
    pocs = "/".join(sorted(v["pos"]))
    restate = (f"Stated against POC *{pocs}; restated against {LECTS[v['par']]['name']} *{X}"
               + (" (through POC > PPN > PNP)." if lect in OUTLIERS else " (the sheet's POC > PTm chain)."))
    note = f"Tryon (1994), Appendix 1, {NAMES[lect]}: " + "; ".join(v["cols"]) + " " + restate
    b.corr(lect, X, refl, env, v["page"], note, status=status, decision=D, as_printed=v["pr"])

b.dec(D, "How is Tryon's (1994) Appendix 1 (POC consonants in 17 Eastern Outer Islands lects) entered?",
      "Grace's POC symbols read as Ross's (mp = b, nt = d, ŋk = ɡ, ŋp = bʷ, ŋm = mʷ, d and r = r, nd = dr, ns = j). "
      "Each reflex is restated against the lect's parent: the Temotu lects through the sheet's chain (POC > PTm > "
      "PRSC, PUtupua, PVanikoro), the Outliers against PNP through POC > PPN > PNP (p > f, b and bʷ > p, d > t, ɡ > "
      "k, q > ʔ, r and dr > l, mʷ > ŋ, ñ > n; *j, *y, *R lost), since the sheet's POC > PCP rows are incomplete. "
      "Cells whose phoneme the parent does not have are not entered: lost in the parent, or, for PRSC *p- and "
      "*ñ, not stated in the sheet (Lackey & Boerger 2021 give PRSC *p only between vowels) (" + str(len(skipped)) +
      " cells: " +
      "; ".join(f"{a} {b_} '{c}'" for a, b_, c in skipped) + "). The first reflex in a cell is regular; footnoted "
      "ones are conditioned where the footnote gives a condition ('Mainly before non-low back vowels'), "
      "regular with conditions unknown where it says 'unconditioned', a loan stratum where it says 'borrowing', "
      "disputed where it says 'uncertain' or '(?)', sporadic otherwise. Malo and Lwepe are new Santa Cruz "
      "dialects of Natügu (Lwepe sharing Natügu's code), Pileni (Vaeakau-Taumako) a new Outlier under PNP. "
      "Printed y = j, ñ = ɲ, mb nd ŋg = ᵐb ⁿd ᵑɡ (b d ɡ in Buma, as in Teanu's sourced inventory), nj̆ = ᶮɟ, ǰ = d͡ʒ; Asumboa mu for *ŋm and Malo, Lwepe u for *w- "
      "are read as mʷ and w.",
      "Enter the rows against POC as printed, as in Tryon, without restating; or leave the Outliers out.",
      "638-645")
write("tryon1994-eoi", b.t, """# tryon1994-eoi

Tryon, Darrell T. 1994. Language contact and contact-induced language change in the Eastern Outer Islands, Solomon Islands. In Tom Dutton & Darrell T. Tryon (eds.), *Language contact and change in the Austronesian world*, 611-648. Berlin: Mouton de Gruyter. Generator: `tools/batch_scripts/duttontryon1994/tryon.py`.

## Scope

- Appendix 1 (pp. 638-645): POC consonant reflexes, initial and medial, with footnoted variants, in Reefs (Äiwoo), Malo, Lwepe, Nanggu (Engdewu), Nembao, Asumboa, Tanimbili, Buma (Teanu), Vano (Lovono), Tanema, Bellona, Rennell, Ontong Java, Sikaiana, Pileni, Tikopia and Anuta, restated against each lect's parent (decision `tryon1994-composition`).
- New lects: Malo (malo1246) and Lwepe (dialects of Natügu), Pileni (pile1238, Vaeakau-Taumako) under PNP.

## Not entered

- Cells whose POC phoneme the parent has already lost (listed in the decision); the grammatical sketches (§4), morphosyntax (§5), loans (§5.1), and the cognate percentages (Appendix 2).
""")
print(len(skipped), "cells skipped")
