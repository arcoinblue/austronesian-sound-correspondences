"""Batch geraghty1986-pcp: Proto-Central Pacific and Proto-Fijian from Geraghty (1986).

Geraghty, Paul. 1986. The sound system of Proto-Central-Pacific. In Paul Geraghty, Lois Carrington &
S. A. Wurm (eds.), FOCAL II (Pacific Linguistics C-94), 289-312. Read from the PDF (text layer,
tables checked against page images).

    python3 tools/batch_scripts/geraghty1986/build.py            # data/incoming/geraghty1986-pcp
    python3 tools/batch_scripts/geraghty1986/build.py rotuman    # Rotuman rows, after Rotuman's parent is PCP
    python3 tools/batch_scripts/geraghty1986/build.py ppn        # PCP > PPN rows, held (decision geraghty1986-ppn)
"""
import csv, io, sys, unicodedata
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
import build as B  # noqa: E402
N = lambda s: unicodedata.normalize("NFC", s)
S = "geraghty1986"
MODE = sys.argv[1] if len(sys.argv) > 1 else "main"
OUT = {"main": ROOT / "data/incoming/geraghty1986-pcp", "rotuman": ROOT / "data/incoming/geraghty1986-rotuman",
       "ppn": Path("/home/claude/held/geraghty1986-ppn")}[MODE]

SOURCES = [
 dict(id=S, author="Geraghty, Paul", year="1986", title="The sound system of Proto-Central-Pacific", kind="comparative",
      url_or_doi="https://doi.org/10.15144/PL-C94.289", pub_type="chapter",
      container_title="FOCAL II: Papers from the Fourth International Conference on Austronesian Linguistics",
      editors="Paul Geraghty; Lois Carrington; S. A. Wurm", pages="289-312", place="Canberra",
      publisher="Pacific Linguistics", series="Pacific Linguistics C-94",
      notes="Consulted directly on 23 November 2026 (PDF; tables read from page images): orthography (p. 289), the PCP "
            "sound system (Table 1, p. 290) and the reflexes in Proto-Fijian, Proto-Polynesian and Rotuman (Tables 2-14, "
            "pp. 291-308), with notes (p. 309). Fijian data are the author's fieldnotes and Proto-Fijian his own "
            "reconstructions; PPn mostly from Biggs's word lists; Rotuman from Churchward's grammar and dictionary."),
 dict(id="geraghty1983", author="Geraghty, Paul", year="1983", title="The history of the Fijian languages",
      kind="comparative", pub_type="book", place="Honolulu", publisher="University of Hawaii Press",
      series="Oceanic Linguistics Special Publication 19",
      notes="Consulted directly on 23 November 2026 (Internet Archive scan, OCR text layer): table of contents, the "
            "summary of sound changes (§4.6, pp. 182-190; Table 15, direct reflexes of Proto-Eastern Oceanic phonemes in "
            "38 Fijian communalects) and the subgrouping chapters (6-7). Geraghty (1986: 289) builds his PCP on the "
            "Proto-Eastern Oceanic of this book. Not entered row by row: see decision geraghty1983-communalects."),
]
LECTS = [
 dict(id="pcp", name="Proto-Central Pacific", alt_names="PCP; Proto-Central-Pacific; Proto Central Pacific", type="proto-language",
      glottocode="cent2060", parent_id="poc", clade="Central Pacific",
      notes="Ancestor of Fijian, Rotuman and Polynesian, a subgroup first proposed and named by George Grace. Geraghty (1986: 289) reconstructs its sound "
            "system without assuming any internal subgrouping, while holding that 'a compelling case for Central Pacific "
            "has yet to be made' (1983: 352-366). His PCP is based on the Proto-Eastern Oceanic of Geraghty (1983), with "
            "*x added. A five-vowel system with phonemic length (p. 309, n. 5); length is not entered. Proto-Polynesian "
            "stays under POc (decision ppn-parent) and is listed as a proposed daughter; Geraghty's PCP > PPn rows wait "
            "for decision geraghty1986-ppn. Glottocode cent2060 (Central Pacific linkage), same membership."),
 dict(id="pfj", name="Proto-Fijian", alt_names="PFJ; PFj", type="proto-language", parent_id="pcp", clade="Fijian",
      inherit="assumed-unchanged", inherit_source_id=S, inherit_page="291-308",
      notes="Geraghty's own reconstruction (1986: 289). Geraghty and Pawley have suggested that some features found in both "
            "Eastern and Western Fijian may have diffused after the break-up of Proto-Fijian (Geraghty 1986: 309, n. 3). "
            "Glottolog has no Fijian clade (it splits Central Pacific into Western Fijian and Tokalau Fijian, the latter "
            "with Polynesian), so no Glottocode (decision geraghty1986-pfj). Vowels are not discussed and are taken as "
            "unchanged (inherit assumed-unchanged)."),
]
# PCP inventory, Table 1 (p. 290); orthography p. 289
def ph(lect, ipa, cls, place="", manner="", voicing="", rounding="", page="290", notes="", sym=""):
    return dict(lect_id=lect, ipa=ipa, source_symbol=sym, **{"class": cls}, place=place, manner=manner, voicing=voicing,
                rounding=rounding, origin="sourced", source_id=S, page=page, notes=notes)
PCP = [("v", "", "fricative", "voiced", "", "Written v: [v] or [β] (p. 289). Preferred to *f because external witnesses (PSS, PNCV) more often have v (p. 292)."),
       ("p", "bilabial", "plosive", "voiceless", "", ""), ("b", "bilabial", "prenasalized-plosive", "voiced", "", "Written b: [mb] (p. 289). Kept apart from *p only in PFJ, on evidence from parts of eastern Fiji (p. 292)."),
       ("m", "bilabial", "nasal", "voiced", "", ""), ("w", "labial-velar", "approximant", "voiced", "", ""),
       ("t", "dental", "plosive", "voiceless", "", ""), ("d", "dental", "prenasalized-plosive", "voiced", "", "Written d: [nd]."),
       ("n", "dental", "nasal", "voiced", "", ""), ("r", "alveolar", "", "voiced", "", ""),
       ("dr", "alveolar", "prenasalized-trill", "voiced", "", "Written dr: [ndr]."),
       ("l", "alveolar", "lateral-approximant", "voiced", "", "Table 1 puts *l in the nasal row; 'it is not claimed ... that *l was a nasal' (p. 290)."),
       ("c", "alveolar", "fricative", "", "", "The non-prenasalised member of the *c-*s pair: it occurs as a base-final consonant, and East Fijian Apical Prenasalisation turned *c into s (p. 297). The orthography of the data has c = [ð] (p. 289)."),
       ("s", "alveolar", "", "", "", "In the prenasalised row of Table 1, but 'it is not claimed that *s was phonetically prenasalised' (p. 290)."),
       ("z", "palatal", "fricative", "voiced", "", "'[z] seems to be a reasonable guess at its phonetic nature' (p. 298); distinguished from *c only in PFJ, by s (or y, ∅) in four communalects: Nalea, Tubai, Vunaqumu and Gonedau (Table 7, p. 300)."),
       ("j", "palatal", "affricate", "", "", "'Probably [tʃ] or [ts], like its only unique reflex, Rotuman j'; the prenasalised counterpart of *z (p. 298)."),
       ("ñ", "palatal", "nasal", "voiced", "", "Distinct from *n by its reflexes in Rotuman and Western Fijian (Table 9, p. 304)."),
       ("y", "palatal", "approximant", "voiced", "", ""), ("x", "velar", "fricative", "voiceless", "", "New in this paper; perhaps 'the result of an incomplete change, rather than an actual PCP phoneme' (p. 305)."),
       ("k", "velar", "plosive", "voiceless", "", ""), ("kʷ", "velar", "plosive", "voiceless", "kw", "Labiovelars occur only before a and, less often, e (p. 306)."),
       ("ɡ", "velar", "prenasalized-plosive", "voiced", "q", "Written q: [ŋg] (p. 289)."), ("ɡʷ", "velar", "prenasalized-plosive", "voiced", "qw", "Written qw."),
       ("ŋ", "velar", "nasal", "voiced", "g", "Written g: [ŋ] (p. 289)."), ("ŋʷ", "velar", "nasal", "voiced", "gw", "Written gw; the reflex of POc *mʷ (p. 306)."),
       ("ʔ", "glottal", "plosive", "voiceless", "?", "Written ? (p. 289).")]
PHONEMES = [ph("pcp", ipa, "C", pl, mn, vc, sym=sym, notes=nt) for ipa, pl, mn, vc, sym, nt in PCP]
for ipa, pl, ht, rd in [("i", "front", "close", "unrounded"), ("e", "front", "close-mid", "unrounded"), ("a", "central", "open", "unrounded"),
                        ("o", "back", "close-mid", "rounded"), ("u", "back", "close", "rounded")]:
    PHONEMES.append(ph("pcp", ipa, "V", pl, ht, "", rd, page="309", notes="'A five-vowel system, with phonemic length, is also indicated by the evidence' (n. 5)." if ipa == "i" else ""))

CORR = []; CNT = {}
def c(lect, p, ch, env="elsewhere", page="291", notes="", status="regular", src=S, cond=None, **kw):
    CNT[lect] = CNT.get(lect, 0) + 1
    r = dict(id=f"{lect}-g86-{CNT[lect]}", child_lect_id=lect, parent_phoneme=p, child_phoneme=ch, environment=env,
             status=status, source_id=src, page=page, notes=notes)
    if cond: r["conditioning"] = cond
    elif env == "conditions unknown": r["conditioning"] = "unknown"
    elif env != "elsewhere": r["conditioning"] = "stated"
    r.update(kw); CORR.append(r)
U = "conditions unknown"
if MODE == "main":
    # POc > PCP: only what the sources state
    c("pcp", "mʷ", "ŋʷ", page="306", notes="'PCP *gw is the reflex of POC *mw' (p. 306).")
    for p_ in ["l", "r", "dr"]:
        c("pcp", p_, p_, page="237", src="marck2000", locator="Table A.1", as_printed=f"POc *{p_} > PCP *{p_}",
          notes="From Marck's Table A.1, which states POc > PCP > PPn for the liquids.")
    c("pcp", "R", "∅", page="588", src="blust2013", locator="Table 8.30", as_printed="PAN *R > Ø (Proto Central Pacific)",
      notes="Blust lists Proto Central Pacific among the languages with zero for PAN *R; composed through POc *R.")
    # PCP > PFJ: Tables 2-6, 11, 14
    P = "pfj"
    for p_, pg, loc in [("v", "291", "Table 2"), ("p", "291", "Table 2"), ("b", "291", "Table 2"), ("m", "291", "Table 2"), ("w", "291", "Table 2"),
                        ("t", "293", "Table 3"), ("d", "293", "Table 3"), ("n", "293", "Table 3"),
                        ("r", "294", "Table 4"), ("dr", "294", "Table 4"), ("l", "294", "Table 4"),
                        ("c", "296", "Table 5"), ("s", "296", "Table 5"), ("z", "297", "Table 6"),
                        ("k", "305", "Table 11"), ("kʷ", "305", "Table 11"), ("ɡ", "305", "Table 11"), ("ɡʷ", "305", "Table 11"),
                        ("ŋ", "305", "Table 11"), ("ŋʷ", "305", "Table 11")]:
        c(P, p_, p_, page=pg, locator=loc)
    c(P, "v", "b", status="sporadic", page="309", notes="'PCP *v is sporadically reflected as *b in PFJ (or parts of Fiji)': *va?a > ba 'taro stem', *vo > bo 'squeeze', *vuka > buka 'firewood' (n. 9).")
    c(P, "j", "s", page="297", locator="Table 6", notes="In PFJ *j merges with *s (p. 298).")
    c(P, "ñ", "ñ", page="297", locator="Table 6", as_printed="ñ/n", decision="geraghty1986-pfj",
      notes="Table 6 prints 'ñ/n': PCP *ñ survives in Western Fijian (n before u, y before a) and merges with *n in Eastern Fijian (p. 303; Table 9, p. 304).")
    c(P, "y", "c", page="297", locator="Table 6", notes="'PCP *y is realised as PFJ *c' (p. 304; Table 10).")
    c(P, "x", "k", page="305", locator="Table 11")
    c(P, "ʔ", "∅", page="307", locator="Table 14", as_printed="∅/y(/#_a)")
    c(P, "ʔ", "y", "#_a", page="307", locator="Table 14", as_printed="∅/y(/#_a)")
    c(P, "∅", "y", "#_a", page="307", locator="Table 14", notes="Table 14: PCP zero before initial *a > PFJ y.")
elif MODE == "rotuman":
    P = "rotu1241"
    PN = "Rotuman forms are 'directly inherited', not Polynesian loans, unless marked (p. 290)."
    c(P, "v", "h", page="291", locator="Table 2", notes=PN)
    c(P, "v", "∅", "mostly before a high vowel", page="292", status="sporadic", locator="Table 2",
      notes="'Some instances of PCP *v become ∅ or ? in Rotuman'; the most common environment is before a high back vowel (p. 292).")
    c(P, "v", "ʔ", "_u", page="292", status="sporadic", locator="Table 2", source_form="?", notes="'Both cases of glottal stop are before u' (p. 292).")
    c(P, "p", "p", page="291", locator="Table 2"); c(P, "b", "p", page="291", locator="Table 2")
    c(P, "m", "m", page="291", locator="Table 2")
    c(P, "m", "∅", "V_u", page="292", status="sporadic", locator="Table 2", notes="Sporadic loss of intervocalic *m before *u, also in PPN: *kamu > ?au (p. 292).")
    c(P, "w", "v", page="291", locator="Table 2")
    c(P, "t", "f", page="293", locator="Table 3", notes="Via an intermediate [θ] recorded by Hale (1846) and Turner (1884) (p. 293).")
    c(P, "t", "t͡ʃ", "before a syllable with *j", page="293", locator="Table 3", source_form="j", notes="*t assimilated to a following j: *taji > jaji 'shave'. 'There are no counter-examples in my data' (pp. 293-294).")
    c(P, "t", "s", "before a syllable with s (from *c, *s, *z)", page="293", locator="Table 3", notes="*taci > sasi 'sea', *tazi-na > sasiga (pp. 293-294).")
    c(P, "d", "t", page="293", locator="Table 3")
    c(P, "d", "t͡ʃ", "before a syllable with *j", page="294", locator="Table 3", source_form="j", notes="One eligible form, *du(cj)(iu) > juju 'point' (p. 294).")
    c(P, "d", "t͡ʃ", "before l or n", page="294", status="sporadic", source_form="j", notes="Two further cases, *dulī > juli 'plover', *donu > nojo; j before l or n is more likely than j before *u, but 'the problem ... requires more data' (p. 294).")
    c(P, "n", "n", page="293", locator="Table 3")
    c(P, "r", "r", page="294", locator="Table 4")
    c(P, "r", "∅", "between high vowels", page="295", locator="Table 4", notes="'PCP *r apparently becomes Rotuman ∅ between high vowels, though there is some contradictory evidence' (*curu > suru, *viri > hiri) (p. 295).")
    c(P, "dr", "t", page="294", locator="Table 4"); c(P, "l", "l", page="294", locator="Table 4")
    c(P, "c", "s", page="296", locator="Table 5"); c(P, "s", "s", page="296", locator="Table 5")
    c(P, "s", "t͡ʃ", "before a syllable with *j", page="297", locator="Table 5", source_form="j", notes="*sije > jija 'garfish' (p. 297).")
    c(P, "z", "s", page="297", locator="Table 6")
    c(P, "j", "t͡ʃ", page="297", locator="Table 6", source_form="j", notes="'Only in Rotuman is it retained as a distinct phoneme' (p. 298).")
    c(P, "ñ", "r", "#_", page="303", locator="Table 6", notes="PCP *ñ, *y and zero before initial *a merged as pre-Rotuman *y, which became r initially (p. 308).")
    c(P, "ñ", "∅", "V_V", page="303", locator="Table 6", notes="Medially lost, 'usually fronting or raising the following vowel' (p. 303).")
    c(P, "ñ", "n", page="303", status="sporadic", locator="Table 6", notes="'The n and ŋ reflexes appear to be sporadic' (p. 303); -na is productive, -ga fossilised (Table 9, n. 1).")
    c(P, "ñ", "ŋ", page="303", status="sporadic", locator="Table 6", source_form="g")
    c(P, "y", "r", "#_", page="304", locator="Table 6"); c(P, "y", "∅", "V_V", page="304", locator="Table 6", notes="Medial *y changed a to e and u to i before it, and was then lost (p. 308).")
    c(P, "x", "∅", "_a", page="305", locator="Table 11", notes="'What little Rotuman evidence there is points to the reflex ∅ before a and ? before u, with the reflex before o equivocal' (p. 305).")
    c(P, "x", "ʔ", "_u", page="305", locator="Table 11", source_form="?")
    c(P, "k", "ʔ", page="305", locator="Table 11", source_form="?"); c(P, "kʷ", "ʔ", page="305", locator="Table 11", source_form="?")
    c(P, "ɡ", "k", page="305", locator="Table 11"); c(P, "ɡʷ", "k", page="305", locator="Table 11")
    c(P, "ŋ", "n", "#_", page="305", locator="Table 11", as_printed="n/g", notes="Initially n (*guju- > nuju 'mouth'), medially g = [ŋ] (*tagi > fagi) (pp. 306-307).")
    c(P, "ŋ", "ŋ", page="305", locator="Table 11", as_printed="n/g", source_form="g")
    c(P, "ŋʷ", "v", page="305", locator="Table 11")
    c(P, "ʔ", "∅", page="307", locator="Table 14", as_printed="∅/?")
    c(P, "ʔ", "ʔ", page="308", status="sporadic", locator="Table 14", source_form="?", notes="'In some cases, however, PCP *? appears to be retained', especially before u; these may be intrusive glottal stops (p. 308, n. 11).")
    c(P, "∅", "r", "#_a", page="307", locator="Table 14", notes="'All instances of PCP initial *a reflected in Rotuman show a prothetic r or, in two cases, g' (p. 307).")
    c(P, "∅", "ŋ", "#_a", page="307", status="sporadic", locator="Table 14", source_form="g", notes="Two cases: *aka > ga?a, *au > goula (p. 307).")
    for v_ in ["e", "o"]:
        c(P, v_, "a", "_#", page="309", status="sporadic", notes="'A major feature of Rotuman is the lowering of final *o and *e to a ... under conditions yet to be determined' (n. 5).")
elif MODE == "ppn":
    P = "ppn"; D = dict(decision="geraghty1986-ppn")
    for p_, ch, pg, loc in [("v", "f", "291", "Table 2"), ("p", "p", "291", "Table 2"), ("b", "p", "291", "Table 2"), ("m", "m", "291", "Table 2"),
                            ("w", "w", "291", "Table 2"), ("t", "t", "293", "Table 3"), ("d", "t", "293", "Table 3"), ("n", "n", "293", "Table 3"),
                            ("l", "l", "294", "Table 4"), ("s", "s", "296", "Table 5"), ("ñ", "n", "297", "Table 6"), ("y", "∅", "297", "Table 6"),
                            ("x", "ʔ", "305", "Table 11"), ("k", "k", "305", "Table 11"), ("kʷ", "k", "305", "Table 11"), ("ɡ", "k", "305", "Table 11"),
                            ("ɡʷ", "k", "305", "Table 11"), ("ŋ", "ŋ", "305", "Table 11"), ("ŋʷ", "ŋ", "305", "Table 11"), ("ʔ", "ʔ", "307", "Table 14")]:
        c(P, p_, ch, page=pg, locator=loc, **D)
    c(P, "m", "∅", "V_u", page="292", status="sporadic", locator="Table 2", notes="*malumu > *malu, *N-mu > *-u (p. 292).", **D)
    c(P, "r", "r", page="295", locator="Table 4", as_printed="r,l", notes="The merger of *r with *l was completed in Proto-Nuclear-Polynesian; in Proto-Tongic *r became ∅ (p. 295).", **D)
    c(P, "r", "l", U, page="295", locator="Table 4", as_printed="r,l", notes="'Under conditions yet to be determined' (p. 295).", **D)
    c(P, "dr", "r", U, page="295", locator="Table 4", as_printed="r,l", notes="*dr merged with *r, which then merged partially with *l (p. 295).", **D)
    c(P, "dr", "l", U, page="295", locator="Table 4", as_printed="r,l", **D)
    c(P, "c", "h", page="296", locator="Table 5", as_printed="h,s", **D)
    c(P, "c", "s", U, page="297", locator="Table 5", as_printed="h,s", notes="'There is no obvious conditioning for PCP *c > PPN *h, s' (p. 297).", **D)
    c(P, "z", "h", page="297", locator="Table 6", as_printed="h,s", **D)
    c(P, "z", "s", U, page="298", locator="Table 6", as_printed="h,s", notes="Five instances (p. 298).", **D)
    c(P, "j", "t", U, page="298", locator="Table 6", as_printed="t,s", notes="'No obvious conditioning, only a tendency to *t before back vowels and *s before front vowels' (p. 298).", **D)
    c(P, "j", "s", U, page="298", locator="Table 6", as_printed="t,s", **D)

DECISIONS = [
 dict(id="geraghty1986-pcp", batch="geraghty1986-pcp", status="open", source_id=S, page="289-290",
      question="Proto-Central Pacific (Geraghty 1986): where does it attach, and what of its descent from POc is entered?",
      chosen_reading="Under POc, with Glottocode cent2060. POc > PCP rows only where a source states them: *mʷ > *ŋʷ (Geraghty 1986: 306), the liquids from Marck (2000: Table A.1) and *R > ∅ from Blust (2013: Table 8.30); the other POc phonemes are unentered for PCP. Canonical symbols: Geraghty's letters, except g, gw, q, qw, kw and ? which are written ŋ, ŋʷ, ɡ, ɡʷ, kʷ and ʔ (Latin g cannot be a symbol; q = [ŋg] matches POc *ɡ); Geraghty's letters are in source_symbol.",
      alternatives="Leave PCP out, as before; or derive POc > PCP rows from Geraghty's (1983) Proto-Eastern Oceanic."),
 dict(id="geraghty1986-ppn", batch="geraghty1986-pcp", status="open", source_id=S, page="291-308",
      question="Geraghty (1986) gives the PPn reflex of every PCP phoneme. Should Proto-Polynesian now go under PCP?",
      chosen_reading="Not yet: decision ppn-parent (open) keeps PPn under POc. PPn is listed under PCP as a proposed daughter (alt_parents pcp:geraghty1986). The 31 PCP > PPn rows are generated and held (tools/batch_scripts/geraghty1986/build.py ppn); they replace the five composed POc > PPn rows if PPn is moved.",
      alternatives="Move PPn under PCP now, with these rows."),
 dict(id="geraghty1986-pfj", batch="geraghty1986-pcp", status="open", source_id=S, page="289, 297",
      question="Proto-Fijian: Glottocode, and its *ñ ('ñ/n' in Table 6).",
      chosen_reading="No Glottocode: Glottolog has no Fijian clade (Western Fijian, and Tokalau Fijian with Polynesian). PFJ keeps *ñ, which Western Fijian keeps apart (n before u, y before a) and Eastern Fijian merges with n. The Western and Eastern Fijian nodes of Table 9 are not entered, and Nadrogā stays under POc.",
      alternatives="Put Nadrogā (Western Fijian) under PFJ with Table 9's *ñ rows."),
 dict(id="geraghty1983-communalects", batch="geraghty1986-pcp", status="open", source_id="geraghty1983", page="182-190",
      question="Geraghty (1983), Table 15: direct reflexes of 37 Proto-Eastern Oceanic phonemes in 38 Fijian communalects, with a key to 41 sound changes. Enter them?",
      chosen_reading="Not entered in this session. The table states reflexes from Proto-Eastern Oceanic, which is not a node here (decision pocr-parents), and the scan's OCR is unusable for it, so each cell has to be read from the page images and composed through PCP and PFJ; most communalects have no Glottocode of their own.",
      alternatives="Enter the communalects under PFJ (Western and Eastern Fijian groups) with rows composed from Table 15."),
]
NOTATION = [dict(lect_id="pcp", phoneme="", system="canonical", symbol="", source_id=S, page="289-290",
                 notes="Geraghty's orthography, with ŋ, ŋʷ, ɡ, ɡʷ, kʷ and ʔ for his g, gw, q, qw, kw and ? (decision geraghty1986-pcp)."),
            dict(lect_id="pfj", phoneme="", system="canonical", symbol="", source_id=S, page="289",
                 notes="As for PCP.")]

def write(table, rows):
    cols = B.TABLES[table]; OUT.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO(); w = csv.writer(buf, lineterminator="\n"); w.writerow(cols)
    for r in rows: w.writerow([N(str(r.get(c_, ""))) for c_ in cols])
    (OUT / f"{table}.csv").write_text(buf.getvalue(), encoding="utf-8"); print(table, len(rows))
if MODE == "main":
    write("sources", SOURCES); write("lects", LECTS); write("phonemes", PHONEMES)
    write("correspondences", CORR); write("notation_map", NOTATION); write("decisions", DECISIONS)
else:
    write("correspondences", CORR)
