"""Batches lynch2001 and lynch2001-reparent: Southern Vanuatu from Lynch (2001).

Lynch, John. 2001. The linguistic history of southern Vanuatu (Pacific Linguistics 509).
Read from the PDF (ABBYY text layer, symbols checked against page images): Table 2.1 (p. 14),
chapters 2-3 (pp. 13-100), Table 4.1 (p. 102) and Appendix I (pp. 201-203).

    python3 tools/batch_scripts/lynch2001/build.py            # data/incoming/lynch2001
    python3 tools/batch_scripts/lynch2001/build.py reparent   # data/incoming/lynch2001-reparent

The second batch holds the rows of Sye and Anejom, which are already in the sheet with parent
POc: it is added after their parent_id has been changed in the sheet (Sye to Proto-Erromango,
Anejom to Proto-Southern Vanuatu).
"""
import csv, io, sys, unicodedata
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
import build as B  # noqa: E402
N = lambda s: unicodedata.normalize("NFC", s)
S = "lynch2001"
REPARENT = len(sys.argv) > 1 and sys.argv[1] == "reparent"
OUT = ROOT / ("data/incoming/lynch2001-reparent" if REPARENT else "data/incoming/lynch2001")

SOURCES = [dict(
    id=S, author="Lynch, John", year="2001", title="The linguistic history of southern Vanuatu", kind="comparative",
    pub_type="book", place="Canberra", publisher="Pacific Linguistics", series="Pacific Linguistics 509",
    notes="Consulted directly on 23 November 2026 (PDF, ABBYY text layer; symbol tables read from page images): "
          "Proto Southern Vanuatu phonemes (Table 2.1, p. 14), the consonants and vowels of PSV, Proto Erromango and "
          "Proto Tanna with their development from POc (chapters 2-3, pp. 13-100; summary Tables 2.2-2.7, 3.1-3.5), "
          "final consonants (Table 4.1, p. 102), the subgrouping (Figure 8.1, p. 184) and the full chart of sound "
          "correspondences (Appendix I, pp. 201-203). Lynch writes /y/ for the palatal glide, j for the Anejom "
          "affricate /tʃ/, and b, d, g for the prenasalised stops of Ura and North Tanna (§1.5.3, p. 9).")]

TREE = ("Lynch (2001: 13, 184) groups the Southern Vanuatu languages as Erromango (Sye, Ura, Utaha), Tanna "
        "(Northern: North Tanna, Whitesands, Lenakel; Southern: Southwest Tanna, Kwamera) and Anejom.")
LECTS = [
 dict(id="psv", name="Proto-Southern Vanuatu", alt_names="PSV; Proto Southern Vanuatu", type="proto-language",
      glottocode="sout2868", parent_id="poc", clade="Southern Vanuatu", tree_parent="soc",
      notes="Reconstructed by Lynch (2001) from Proto Erromango, Proto Tanna and Anejom, with its development from "
            "POc. " + TREE + " Lynch places Southern Vanuatu in Southern Oceanic (pp. 6, 190) but enters no PSOc "
            "changes of his own; the Southern Oceanic group (soc) is a linkage here (decision pocr-parents). Changes "
            "in canonical form that are not segment correspondences are in the notes only: loss of pretonic vowels "
            "(*na lima-ña > Lenakel nelman), accretion of an initial vowel to most verbs and of the article *na to most "
            "nouns, and retention of POc final consonants, which the Erromangan languages tend to lose after nasals and "
            "Anejom loses except *r (p. 14; Table 4.1, p. 102). Glottocode sout2868 (Southern Vanuatu), same membership."),
 dict(id="per", name="Proto-Erromango", alt_names="PEr; Proto Erromango; Proto Erromangan", type="proto-language",
      glottocode="erro1239", parent_id="psv", clade="Erromango",
      notes="Lynch (2001: 13-91). Utaha (Ifo) data are 'highly tentative, based as they are on the most fragmentary of "
            "data' and are given only in the tables of correspondences (p. 13). Lynch also reconstructs medial clusters "
            "*n + *r (Sye nr, Ura d-, -d-, -n; p. 42) and *n + *t (Sye nt, Ura d; pp. 53, 55), from the accreted "
            "article and from compounds; these are not entered as phonemes. Glottocode erro1239 (Erromanga), same membership."),
 dict(id="ptn", name="Proto-Tanna", alt_names="PTn; Proto Tanna", type="proto-language", glottocode="tann1242",
      parent_id="psv", clade="Tanna",
      notes="Lynch (2001: 13-99). Two subgroups, Northern and Southern Tanna (p. 13; justified in ch. 8). POc *l, *r and "
            "*R merged as PTn *r (p. 45). Glottocode tann1242 (Tanna), same membership."),
 dict(id="pnt", name="Proto-Northern Tanna", alt_names="PNT; Proto Northern Tanna", type="proto-language",
      glottocode="nort3218", parent_id="ptn", clade="Northern Tanna",
      notes="Given by Lynch (2001) only in Appendix I (pp. 201-203) and in the discussion of the liquids and sibilants "
            "(pp. 45-47, 66): PTn *r split into PNT *l and *i, and PTn *h into *h and *z. Glottocode nort3218 "
            "(Northern Tanna linkage in Glottolog), same membership."),
 dict(id="pst", name="Proto-Southern Tanna", alt_names="PST; Proto Southern Tanna", type="proto-language",
      glottocode="sout3195", parent_id="ptn", clade="Southern Tanna",
      notes="Given by Lynch (2001) only in Appendix I (pp. 201-203), where every PST phoneme is the same as in PTn "
            "(*q is marked '?'). Glottocode sout3195 (Southern Tanna), same membership."),
 dict(id="urav1235", name="Ura", alt_names="Ura (Vanuatu)", type="language", glottocode="urav1235", iso639_3="uur",
      parent_id="per", latitude="-18.65", longitude="169.10",
      notes="Erromango; moribund (Lynch 2001: 4-5). Lynch (2001: 7) quotes Terry Crowley on the considerable variation "
            "between [l] and [r] in Ura transcriptions. Many Ura words with medial t are probably Sye loans (Lynch 2001: 55). Coordinates from "
            "the language metadata of Ross et al. (2023: 629)."),
 dict(id="ifoo1237", name="Utaha", alt_names="Ifo", type="language", glottocode="ifoo1237", iso639_3="iff", parent_id="per",
      notes="Extinct language of Erromango. Lynch's Utaha reflexes are 'highly tentative, based as they are on the most "
            "fragmentary of data' (2001: 13), and the vowels could not be worked out (p. 91). Glottolog name Ifo."),
 dict(id="nort2847", name="North Tanna", type="language", glottocode="nort2847", iso639_3="tnn", parent_id="pnt",
      latitude="-19.37", longitude="169.30",
      notes="The dialect Lynch cites has, besides the voiceless stops, an incomplete set of prenasalised voiced stops "
            "/ᵐbʷ ᵐb ⁿd/; other dialects have the Lenakel system (2001: 7). It is not clear whether North Tanna and "
            "Whitesands have /w/ (p. 7, n. 6); not entered. Coordinates from the language metadata of "
            "Ross et al. (2023: 627)."),
 dict(id="whit1269", name="Whitesands", type="language", glottocode="whit1269", iso639_3="tnp", parent_id="pnt",
      latitude="-19.50", longitude="169.38",
      notes="Same consonant system as Lenakel, perhaps also with /fʷ/ (Lynch 2001: 7); whether it has /w/ is not "
            "clear (p. 7, n. 6), and /w/ is not entered. Coordinates from the language "
            "metadata of Ross et al. (2023: 629)."),
 dict(id="lena1238", name="Lenakel", type="language", glottocode="lena1238", iso639_3="tnl", parent_id="pnt",
      latitude="-19.48", longitude="169.26",
      notes="Lynch's own field language (2001: 7). Vowel length is contrastive, mostly in final syllables (p. 8); not "
            "entered. Coordinates from the language metadata of Ross et al. (2023: 625)."),
 dict(id="sout2869", name="Southwest Tanna", type="language", glottocode="sout2869", iso639_3="nwi", parent_id="pst",
      latitude="-19.58", longitude="169.36",
      notes="Same system as Kwamera, except that most dialects have /l/ for /r/ (Lynch 2001: 7-8); the Mess dialect has r "
            "(p. 45, n. 15). Coordinates from the language metadata of Ross et al. (2023: 628)."),
 dict(id="kwam1252", name="Kwamera", type="language", glottocode="kwam1252", iso639_3="tnk", parent_id="pst",
      latitude="-19.60", longitude="169.44",
      notes="Kwamera fluctuates between s and h more than the other Tanna languages (Lynch 2001: 65). Vowel length is "
            "contrastive (p. 8); not entered. Coordinates from the language metadata of Ross et al. (2023: 625)."),
]

# ---------------------------------------------------------------- inventories
def ph(lect, ipa, cls, place="", manner="", voicing="", rounding="", page="", notes="", sym="", status=""):
    return dict(lect_id=lect, ipa=ipa, source_symbol=sym, **{"class": cls}, place=place, manner=manner,
                voicing=voicing, rounding=rounding, origin="sourced", source_id=S, page=page, notes=notes, status=status)
V6 = [("i", "front", "close", "unrounded"), ("e", "front", "close-mid", "unrounded"), ("ə", "central", "mid", "unrounded"),
      ("a", "central", "open", "unrounded"), ("o", "back", "close-mid", "rounded"), ("u", "back", "close", "rounded")]
C_PSV = [("pʷ", "bilabial", "plosive", "voiceless"), ("p", "bilabial", "plosive", "voiceless"),
         ("t", "alveolar", "plosive", "voiceless"), ("c", "palatal", "", ""), ("k", "velar", "plosive", "voiceless"),
         ("q", "", "", ""), ("bʷ", "bilabial", "prenasalized-plosive", "voiced"), ("b", "bilabial", "prenasalized-plosive", "voiced"),
         ("d", "alveolar", "prenasalized-plosive", "voiced"), ("ɡ", "velar", "prenasalized-plosive", "voiced"),
         ("v", "", "fricative", "voiced"), ("s", "alveolar", "fricative", "voiceless"), ("j", "unknown", "", ""),
         ("ɣ", "velar", "fricative", "voiced"), ("mʷ", "bilabial", "nasal", "voiced"), ("m", "bilabial", "nasal", "voiced"),
         ("n", "alveolar", "nasal", "voiced"), ("ŋ", "velar", "nasal", "voiced"), ("l", "alveolar", "lateral-approximant", "voiced"),
         ("r", "alveolar", "", "voiced"), ("w", "", "", ""), ("y", "palatal", "approximant", "voiced")]
PH_NOTES = {
 ("psv", "c"): "Palatalised POc *t before *i, *e; 'it may well have been a palatal stop or affricate in PSV' (p. 62).",
 ("psv", "j"): "Continues POc *j, kept apart from *c and *s (p. 66); its phonetic value is not given.",
 ("psv", "q"): "Retained in PSV but lost in all modern SV languages; the argument is in §4.6 (pp. 74, 120-121).",
 ("psv", "v"): "A voiced labial fricative (p. 14).",
 ("psv", "w"): "'It is unclear from these data exactly what kind of sound *w was'; perhaps the velarised counterpart of *v (p. 28).",
 ("psv", "ɣ"): "Printed γ.",
 ("psv", "o"): "Its reflexes 'suggest that *o may not have been phonetically [o]' (p. 100): it conditions palatalisation like a front vowel.",
 ("psv", "e"): "From POc *e and, as a conditioned reflex, POc *a before *Ci, *Cu (p. 100).",
 ("psv", "ə"): "A conditioned reflex of POc *a before *Ca (p. 100).",
}
PHONEMES = []
for ipa, pl, mn, vc in C_PSV:
    PHONEMES.append(ph("psv", ipa, "C", pl, mn, vc, page="14", sym="γ" if ipa == "ɣ" else "", notes=PH_NOTES.get(("psv", ipa), "")))
for ipa, pl, ht, rd in V6:
    PHONEMES.append(ph("psv", ipa, "V", pl, ht, "", rd, page="14", notes=PH_NOTES.get(("psv", ipa), "")))
C_PER = [("p", "bilabial", "plosive", "voiceless", "17"), ("b", "bilabial", "prenasalized-plosive", "voiced", "17"),
         ("f", "", "fricative", "voiceless", "22"), ("v", "", "fricative", "voiced", "22"), ("w", "", "", "", "22"),
         ("m", "bilabial", "nasal", "voiced", "14"), ("t", "alveolar", "plosive", "voiceless", "53"),
         ("d", "alveolar", "prenasalized-plosive", "voiced", "53"), ("n", "alveolar", "nasal", "voiced", "50"),
         ("s", "alveolar", "fricative", "voiceless", "67"), ("h", "glottal", "fricative", "voiceless", "67"),
         ("l", "alveolar", "lateral-approximant", "voiced", "40"), ("r", "alveolar", "", "voiced", "40"),
         ("L", "alveolar", "", "voiced", "40"), ("k", "velar", "plosive", "voiceless", "32"),
         ("ɡ", "velar", "prenasalized-plosive", "voiced", "32"), ("ɣ", "velar", "fricative", "voiced", "32"),
         ("ŋ", "velar", "nasal", "voiced", "29"), ("y", "palatal", "approximant", "voiced", "49"), ("q", "", "", "", "202")]
PH_NOTES.update({
 ("per", "L"): "A third liquid (Sye r, Ura l); Lynch treats PEr *r and *L as variant reflexes of PSV *r (p. 43).",
 ("per", "f"): "From PSV *v next to a syllable with a sibilant (p. 24); Sye p-, -v-, Ura f.",
 ("per", "q"): "Appendix I (p. 202) gives PEr *q, lost in Sye, Ura and Utaha.",
 ("per", "ɣ"): "Printed γ.",
 ("per", "ə"): "Posited on Crowley's underlying Sye schwa (o ~ ∅) and Sye o : Ura i (pp. 90-91).",
})
for ipa, pl, mn, vc, pg in C_PER:
    PHONEMES.append(ph("per", ipa, "C", pl, mn, vc, page=pg, sym="γ" if ipa == "ɣ" else "", notes=PH_NOTES.get(("per", ipa), "")))
for ipa, pl, ht, rd in V6:
    PHONEMES.append(ph("per", ipa, "V", pl, ht, "", rd, page="82-83", notes=PH_NOTES.get(("per", ipa), "")))
C_PTN = [("pʷ", "bilabial", "plosive", "voiceless", "19"), ("p", "bilabial", "plosive", "voiceless", "19"),
         ("bʷ", "bilabial", "prenasalized-plosive", "voiced", "19"), ("b", "bilabial", "prenasalized-plosive", "voiced", "19"),
         ("v", "", "fricative", "voiced", "24"), ("kʷ", "velar", "plosive", "voiceless", "25"),
         ("mʷ", "bilabial", "nasal", "voiced", "14"), ("m", "bilabial", "nasal", "voiced", "14"),
         ("t", "alveolar", "plosive", "voiceless", "56"), ("d", "alveolar", "prenasalized-plosive", "voiced", "56"),
         ("n", "alveolar", "nasal", "voiced", "50"), ("s", "alveolar", "fricative", "voiceless", "65"),
         ("h", "glottal", "fricative", "voiceless", "65"), ("r", "alveolar", "", "voiced", "45"),
         ("k", "velar", "plosive", "voiceless", "36"), ("ɣ", "velar", "fricative", "voiced", "36"),
         ("ŋ", "velar", "nasal", "voiced", "29"), ("q", "", "", "", "202")]
PH_NOTES.update({
 ("ptn", "kʷ"): "Reconstructed as a labialised velar stop from SWT, Kwm kʷ, Lenakel underlying w and North Tanna final p (p. 25).",
 ("ptn", "ɣ"): "Not found in any modern Tanna language; reconstructed for its stop, nasal and zero reflexes (p. 36). Printed γ.",
 ("ptn", "q"): "Appendix I (p. 202) gives PTn *q, lost in all Tanna languages.",
 ("ptn", "e"): "Only a conditioned reflex of POc *a (p. 75).", ("ptn", "o"): "Only a conditioned reflex of POc *a (p. 75).",
})
for ipa, pl, mn, vc, pg in C_PTN:
    PHONEMES.append(ph("ptn", ipa, "C", pl, mn, vc, page=pg, sym="γ" if ipa == "ɣ" else "", notes=PH_NOTES.get(("ptn", ipa), "")))
for ipa, pl, ht, rd in V6:
    PHONEMES.append(ph("ptn", ipa, "V", pl, ht, "", rd, page="91-92", notes=PH_NOTES.get(("ptn", ipa), "")))

# attested inventories, §1.5.1-1.5.2 (pp. 7-8)
V5 = ["i", "e", "a", "o", "u"]; V6T = ["i", "e", "ə", "a", "o", "u"]
def inv(lect, cons, vows, notes=None, marginal=(), syms=None):
    notes = notes or {}; syms = syms or {}
    for x in cons:
        PHONEMES.append(ph(lect, x, "C", page="7", sym=syms.get(x, ""), notes=notes.get(x, ""), status="marginal" if x in marginal else ""))
    for x in vows:
        PHONEMES.append(ph(lect, x, "V", page="8", sym=syms.get(x, ""), notes=notes.get(x, "")))
inv("urav1235", ["p", "t", "k", "ᵐb", "ⁿd", "ᵑɡ", "f", "s", "h", "v", "ɣ", "m", "n", "ŋ", "l", "r", "w", "j"], V5,
    notes={"ᵐb": "Ura /b d g/ are prenasalised (p. 7).", "h": "h does not occur initially or finally, and is rare except before a consonant (p. 67)."},
    syms={"ᵐb": "b", "ⁿd": "d", "ᵑɡ": "g", "j": "y", "ɣ": "γ"})
LEN = ["pʷ", "p", "t", "k", "f", "s", "h", "v", "mʷ", "m", "n", "ŋ", "l", "r"]
inv("lena1238", LEN + ["w"], V6T,
    notes={"v": "Phonetically a high central glide [ɨ̯] with the lips approximated (p. 24, n. 7).",
           "w": "Underlying /w/, posited on verb morphology and final [ʊ] : [u]; it corresponds to SWT and Kwamera kʷ (p. 25).",
})
inv("whit1269", LEN + ["fʷ"], V6T, marginal=("fʷ",),
    notes={"fʷ": "Whitesands 'may also have the labialised fricative /fʷ/' (p. 7).",
})
inv("nort2847", LEN[:4] + ["ᵐbʷ", "ᵐb", "ⁿd"] + LEN[4:], V6T, syms={"ᵐbʷ": "bʷ", "ᵐb": "b", "ⁿd": "d"},
    notes={"ᵐbʷ": "The dialect Lynch cites has 'an incomplete set of prenasalised voiced stops' (p. 7)."})
KWM = ["pʷ", "p", "t", "k", "kʷ", "fʷ", "f", "s", "h", "v", "mʷ", "m", "n", "ŋ"]
inv("kwam1252", KWM + ["r"], V6T, marginal=("fʷ",), notes={"fʷ": "In parentheses in Lynch's chart (p. 7)."})
inv("sout2869", KWM + ["l", "r"], V6T, marginal=("fʷ", "r"),
    notes={"l": "Most dialects have /l/ instead of the Kwamera /r/ (pp. 7-8).", "r": "The Mess dialect has r for the l of other dialects (p. 45, n. 15).", "fʷ": "Same system as Kwamera, whose /fʷ/ is in parentheses (p. 7)."})

# ---------------------------------------------------------------- correspondences
CORR = []; CNT = {}
def c(lect, p, ch, env="elsewhere", page="201", notes="", status="regular", cond=None, **kw):
    CNT[lect] = CNT.get(lect, 0) + 1
    r = dict(id=f"{lect}-l01-{CNT[lect]}", child_lect_id=lect, parent_phoneme=p, child_phoneme=ch, environment=env,
             status=status, source_id=S, page=page, notes=notes)
    if cond: r["conditioning"] = cond
    elif env == "conditions unknown": r["conditioning"] = "unknown"
    elif env != "elsewhere": r["conditioning"] = "stated"
    if ch == "": r.pop("status"); r["blank_type"] = kw.pop("blank_type")
    r.update(kw); CORR.append(r)
U = "conditions unknown"
TILDE = "Lynch's 'x ~ y' means 'x or y, but more often x' (p. 11); the less frequent reflex has no stated conditioning (decision lynch2001-variants)."

# --- POc > PSV: Tables 2.2 (p. 29), 2.3 (p. 39), 2.5 (p. 48), 2.7 (p. 74), 3.5 (p. 99)
P = "psv"
c(P, "pʷ", "bʷ", page="20", locator="Table 2.2", notes="PSV *bʷ has three sources: POc *bʷ and *pʷ in all environments, and POc *b before *u (p. 20).")
c(P, "pʷ", "pʷ", U, page="22", locator="Table 2.2", decision="lynch2001-variants",
  notes="Table 2.2 (p. 29) also has POc *pʷ > PSV *pʷ. PSV *p and *pʷ 'occur less frequently than their voiced counterparts, and have less obvious sources' (p. 22).")
c(P, "bʷ", "bʷ", page="20", locator="Table 2.2")
c(P, "b", "bʷ", "_u", page="20", locator="Table 2.2", notes="Examples p. 21.")
c(P, "b", "b", page="21", locator="Table 2.2")
c(P, "p", "v", page="26", locator="Table 2.2", notes="'PSV *v derives from POc *p' (p. 26); Table 2.2 labels this the lenis *p.")
c(P, "p", "p", U, page="22", locator="Table 2.2", decision="lynch2001-variants",
  notes="Table 2.2 labels this the fortis *p ('*p fortis?'): after POc *p became *v a voiceless stop may have developed again, or fortis *p became PSV *p and lenis *p *v (Ross 1988: 47ff.) (p. 22).")
c(P, "w", "w", page="28", locator="Table 2.2", notes="'A fairly clear case for POc *w > PSV *w' (p. 27).")
c(P, "mʷ", "mʷ", page="16", locator="Table 2.2")
c(P, "m", "mʷ", "_u", page="16", locator="Table 2.2", notes="Some sets vary between *m and *mʷ, generally next to *u (p. 16).")
c(P, "m", "m", page="16", locator="Table 2.2")
c(P, "ɡ", "ɡ", page="39", locator="Table 2.3")
c(P, "k", "ɣ", page="39", locator="Table 2.3", notes="'The regular reflex of POc *k was PSV *ɣ' (p. 39); Table 2.3 labels this the lenis *k.")
c(P, "k", "k", U, page="39", locator="Table 2.3", decision="lynch2001-variants",
  notes="'After the lenition of POc *k to *ɣ, a third velar obstruent, PSV *k, developed. It is difficult to see what the conditioning was' (p. 39); labelled fortis *k.")
c(P, "ŋ", "ŋ", page="29", locator="Table 2.3")
c(P, "q", "q", page="74", notes="'POc *q seems to have been retained in PSV, but was subsequently lost in all SV languages' (p. 74); the argument is in §4.6 (pp. 120-121).")
c(P, "l", "l", page="48", locator="Table 2.5")
c(P, "r", "r", page="48", locator="Table 2.5")
c(P, "R", "r", U, page="40", locator="Table 2.5",
  notes="'Of the non-final occurrences of etyma containing POc *R ... about half show a merger of *R with *r (as PSV *r), while the other half show zero reflexes ... there seems to be no way of predicting the retention of non-final *R' (p. 40; Table 2.4).")
c(P, "R", "∅", U, page="40", locator="Table 2.4", notes="Non-final *R lost in about half of the etyma (p. 40).")
c(P, "R", "∅", "_#", page="40", notes="'POc word-final *R was lost in the SV languages'; the only apparent exception, *mimiR 'urinate', may reflect *mimiR-i (p. 40).")
c(P, "dr", "d", U, page="47", locator="Table 2.5", decision="lynch2001-variants", as_printed="*d ~ *r",
  notes="*dr is rare. Some etyma show *dr > PTn *d, Anj j, a merger with *d; others a merger with *r; *dr may have been a cluster *nr in pre-PSV that simplified sometimes as *d and sometimes as *r (pp. 47-48). " + TILDE)
c(P, "dr", "r", U, page="47", locator="Table 2.5", decision="lynch2001-variants", as_printed="*d ~ *r", notes="E.g. *madraR 'fermented breadfruit' (p. 47).")
c(P, "t", "c", "_i, _e", page="59", locator="Table 2.7",
  notes="Palatalisation. Before *o the reflexes vary between *t and *c; the words with *c may have changed the vowel already in PSOc, or had doublets (pp. 59-60).")
c(P, "t", "t", page="58", locator="Table 2.7",
  notes="Noun-initial *t after the accreted article *na fused as *nt (> PEr, PTn *d in some words), which Lynch writes PSV *nt (p. 58); not entered as a phoneme.")
c(P, "d", "d", page="58", locator="Table 2.7")
c(P, "s", "s", page="61", locator="Table 2.7", notes="'The first seems to reflect a genuine voiceless fricative' (p. 62).")
c(P, "c", "s", page="61", locator="Table 2.7")
c(P, "j", "j", page="66", locator="Table 2.7", notes="'*j was kept distinct from *c and *s' (p. 66).")
c(P, "n", "n", page="50", locator="Table 2.7")
c(P, "ñ", "y", page="49", locator="Table 2.7", notes="'POc *n is reflected as PSV *n, while POc *ñ merges with *y as PSV *y' (p. 49). The 3sg suffix *-ña has n everywhere, perhaps inherited as *-na (n. 18).")
c(P, "y", "y", page="49", locator="Table 2.7")
c(P, "n", "ŋ", "*q in an adjacent syllable, the vowel between lost", page="51",
  notes="Velarisation of *n in a few etyma: *nq and *qn both became *ŋ (*qanusi > Lenakel ayh 'spit') (p. 51).")
c(P, "i", "i", page="99", locator="Table 3.5")
c(P, "e", "e", page="99", locator="Table 3.5", notes="Few etyma retain *e, so its development is tentative (p. 75).")
c(P, "a", "a", page="99", locator="Table 3.5")
c(P, "a", "e", "_Ci, _Cu", page="99", locator="Table 3.5",
  notes="A conditioned reflex; in every daughter there are also cases of *a remaining *a in this environment (pp. 81, 89, 97-98).")
c(P, "a", "ə", "_Ca", page="99", locator="Table 3.5", notes="Dissimilation of *aCa, most pervasive in Tanna (pp. 90, 98).")
c(P, "o", "o", page="99", locator="Table 3.5", notes="Reflexes PEr *a, PTn *ə (occasionally *u), Anj e; perhaps not phonetically [o] (p. 100).")
c(P, "u", "u", page="99", locator="Table 3.5")
for v in "ieaou":
    c(P, v, "∅", "_#", page="14", notes="'POc vowels in absolute word-final position were regularly lost, but a vowel was retained before word-final *q' (p. 14; §4.1.2).")

# --- PSV > PEr
P = "per"
c(P, "pʷ", "p", page="20", locator="Table 2.2", notes="The simple/velarised distinction was lost in Erromango (p. 20).")
c(P, "p", "p", page="20", locator="Table 2.2")
c(P, "bʷ", "b", page="20", locator="Table 2.2")
c(P, "b", "b", page="20", locator="Table 2.2")
c(P, "v", "v", page="26", locator="Table 2.2", as_printed="*v-v-p", notes="Initial and medial.")
c(P, "v", "p", "_#", page="26", locator="Table 2.2", as_printed="*v-v-p")
c(P, "v", "f", "next to a syllable with a sibilant", page="24", as_printed="*v-v-p (*f)",
  notes="'PEr *f derives from PSV *v when an adjacent syllable contained a sibilant, reflected as h in at least some languages' (p. 24).")
c(P, "w", "w", page="28", locator="Table 2.2", as_printed="*w-w-u")
c(P, "w", "u", "_#", page="28", locator="Table 2.2", as_printed="*w-w-u")
c(P, "mʷ", "m", page="16", locator="Table 2.2")
c(P, "m", "m", page="16", locator="Table 2.2")
c(P, "k", "k", page="39", locator="Table 2.3")
c(P, "ɡ", "ɡ", page="39", locator="Table 2.3")
c(P, "ɣ", "ɣ", page="39", locator="Table 2.3")
c(P, "ŋ", "ŋ", page="39", locator="Table 2.3")
c(P, "q", "q", page="202", locator="Appendix I")
c(P, "l", "l", page="48", locator="Table 2.5")
c(P, "r", "r", U, page="43", locator="Table 2.5", as_printed="*r ~ *L", decision="lynch2001-variants",
  notes="POc *r and *R (when retained) have two reflexes, PEr *r (Sye r, Ura r) and *L (Sye r, Ura l): 'I am unable at this stage to account for this variation' (p. 43). " + TILDE)
c(P, "r", "L", U, page="43", locator="Table 2.5", as_printed="*r ~ *L", decision="lynch2001-variants")
c(P, "t", "t", page="58", locator="Table 2.7")
c(P, "t", "d", "n_", page="58", locator="Table 2.7", notes="Initial *t after the accreted article *na (p. 58).")
c(P, "d", "d", page="58", locator="Table 2.7", notes="'The only apparent reflex of POc *d in my data' is one etymon; Table 2.7 has *d, p. 58 '*d?' (p. 56).")
c(P, "c", "s", page="71", locator="Table 2.7", notes="'In initial position, PSV *c > PEr *s (Sye, Ura s), and PSV *s > PEr *h (Sye s, Ura ∅)' (p. 68).")
c(P, "s", "h", page="68", locator="Table 2.7")
c(P, "j", "s", page="72", locator="Table 2.7", as_printed="*s ?", notes="Table 2.7 prints '*s ?'; POc *j, when reflected, is s in Sye and Ura, but lost in two Sye words (p. 72).")
c(P, "n", "n", page="50", locator="Table 2.7")
c(P, "y", "y", page="49", locator="Table 2.7", as_printed="*y ~ *i")
c(P, "y", "i", page="49", status="sporadic", locator="Table 2.7", as_printed="*y ~ *i", notes="'Occasionally *i' (p. 49).")
c(P, "i", "i", page="91", locator="Table 3.3", notes="'When adjacent to another vowel, the reflexes are frequently y and w' (p. 83).")
c(P, "e", "e", page="91", locator="Table 3.3")
c(P, "a", "a", page="91", locator="Table 3.3")
c(P, "ə", "ə", page="91", locator="Table 3.3", notes="POc *aCa became *əC(a) in PEr (p. 91).")
c(P, "o", "a", page="87", locator="Table 3.3", notes="'A reasonably strong tendency for POc *o to be reflected as a in Ura and as either e or a in Sye, suggesting PEr *a' (p. 87).")
c(P, "u", "u", page="91", locator="Table 3.3")
c(P, "u", "o", "next to a labial", status="sporadic", page="84", notes="Sporadic lowering of *u, most commonly next to a labial; one set has Sye o : Ura o (p. 84).")

# --- PSV > PTn
P = "ptn"
for x in ["pʷ", "p", "bʷ", "b", "mʷ", "m"]:
    c(P, x, x, page="20" if x[0] in "pb" else "16", locator="Table 2.2")
c(P, "v", "kʷ", "next to *u", page="26", locator="Table 2.2", notes="'PTn has *kʷ when POc *p was adjacent to *u, and *v elsewhere' (p. 26).")
c(P, "v", "v", page="26", locator="Table 2.2")
c(P, "w", "kʷ", page="27", locator="Table 2.2", notes="Table 2.2 has PTn *kʷ; the text prints '*kʷ? *u?': 'the reflexes in Proto Tanna are variable' (pp. 27-28).")
c(P, "k", "k", page="39", locator="Table 2.3")
c(P, "ɡ", "k", page="36", locator="Table 2.3", notes="PTn *k 'derives from POc (or PSOc) *g and corresponds with Proto Erromango *g' (p. 36).")
c(P, "ɣ", "ɣ", page="39", locator="Table 2.3")
c(P, "ŋ", "ŋ", page="39", locator="Table 2.3")
c(P, "q", "q", page="202", locator="Appendix I")
c(P, "l", "r", page="45", locator="Table 2.5", notes="'POc *l, *r and *R all merged in Proto Tanna' (p. 45); *r rather than *l for reasons given on p. 48.")
c(P, "r", "r", page="45", locator="Table 2.5")
c(P, "t", "t", page="58", locator="Table 2.7")
c(P, "t", "d", "n_", page="57", locator="Table 2.7", notes="Noun-initial *t after the accreted article *na fused as PTn *d (p. 57).")
c(P, "d", "d", page="57", locator="Table 2.7")
c(P, "c", "s", page="65", locator="Table 2.7")
c(P, "s", "h", page="65", locator="Table 2.7")
c(P, "j", "h", page="66", locator="Table 2.7", notes="'*j seems to be reflected as PTn *h but as Anejom s' (p. 66).")
c(P, "n", "n", page="50", locator="Table 2.7")
c(P, "y", "i", page="49", locator="Table 2.7")
c(P, "i", "i", page="99", locator="Table 3.4")
c(P, "e", "i", page="96", locator="Table 3.4", notes="'POc *e appears to be reflected as PTn *i, with widespread reduction to ə in all languages except Kwamera' (p. 96).")
c(P, "e", "e", page="97", locator="Table 3.4", cond="lexical", lexical_scope="PSV *e from POc *a before *Ci, *Cu",
  decision="lynch2001-psv-e", notes="Table 3.4: POc *a > PTn *e before *Ci and *Cu (pp. 97-98), while POc *e > PTn *i. Both are PSV *e in Table 3.5.")
c(P, "a", "a", page="99", locator="Table 3.4")
c(P, "a", "o", "next to a labial or *u", page="97", locator="Table 3.4", notes="'Some evidence to suggest that it derives from POc *a adjacent to a labial/labialised consonant and/or *u' (p. 97).")
c(P, "ə", "ə", page="98", locator="Table 3.4")
c(P, "o", "ə", page="96", locator="Table 3.4", notes="'In most cases it becomes PTn *ə' (p. 96).")
c(P, "o", "u", U, page="96", locator="Table 3.4", notes="'POc *o appears to become PTn *u in some cases' (p. 96).")
c(P, "u", "u", page="94", locator="Table 3.4")

# --- PTn > PNT, PST (Appendix I and pp. 45-47, 66)
SAME_TN = ["pʷ", "p", "bʷ", "b", "v", "kʷ", "mʷ", "m", "t", "d", "s", "n", "k", "ɣ", "ŋ", "i", "e", "ə", "a", "o", "u"]
for x in SAME_TN:
    c("pnt", x, x, page="201-203", locator="Appendix I")
c("pnt", "q", "q", status="disputed", page="202", locator="Appendix I", as_printed="?", decision="lynch2001-pnt-pst",
  notes="Appendix I prints '?' for PNT *q; *q is lost in North Tanna, Whitesands and Lenakel.")
c("pnt", "h", "z", "*q in an adjacent syllable", page="66", locator="Appendix I", as_printed="*h (*z)",
  notes="PTn *h > PNT *z (NTn r, Wsn r, Len t), from POc *s or *c 'in the environment of the glottal stop *q in an adjacent syllable', though not in *qusan 'rain' (p. 66, n. 32).")
c("pnt", "h", "h", page="66", locator="Appendix I")
c("pnt", "r", "l", "_i, _e, _o", page="46", locator="Table 2.5", notes="'Before POc *i, *e and *o, PTn *r is reflected as PNT *l' (p. 46). Some fairly clear cognates have the wrong reflex, unexplained (p. 47).")
c("pnt", "r", "l", "i_", page="46", notes="'Some evidence' that POc *l, *r and *R became PNT *l immediately after *i (p. 46).")
c("pnt", "r", "i", page="46", locator="Table 2.5", notes="'In other environments, PTn *r is reflected as PNT *i' (phonetically [y] next to another vowel) (pp. 45-46).")
for x in SAME_TN + ["h", "r"]:
    c("pst", x, x, page="201-203", locator="Appendix I")
c("pst", "q", "q", status="disputed", page="202", locator="Appendix I", as_printed="?", decision="lynch2001-pnt-pst",
  notes="Appendix I prints '?' for PST *q; *q is lost in Southwest Tanna and Kwamera.")

# --- PNT > North Tanna, Whitesands, Lenakel
def rows(L, p, rs):
    for r in rs:
        c(L, p, *r[:6], **r[6])
def northern(L, bw, b, kw_rows, t_rows, d_rows, z, g_else, v_rows):
    c(L, "pʷ", "pʷ", page="19", locator="Appendix I"); c(L, "p", "p", page="19", locator="Appendix I")
    rows(L, "bʷ", bw)
    c(L, "b", b, page="19", locator="Appendix I")
    rows(L, "v", v_rows)
    rows(L, "kʷ", kw_rows)
    c(L, "mʷ", "mʷ", page="15", locator="Appendix I"); c(L, "m", "m", page="15", locator="Appendix I")
    rows(L, "t", t_rows)
    rows(L, "d", d_rows)
    c(L, "s", "s", page="65", locator="Appendix I"); c(L, "h", "h", page="65", locator="Appendix I")
    c(L, "z", z, page="66", locator="Appendix I")
    c(L, "n", "n", page="50", locator="Appendix I"); c(L, "ŋ", "ŋ", page="29", locator="Appendix I")
    c(L, "k", "k", page="36", locator="Appendix I")
    c(L, "ɣ", "∅", "next to *i, *e", page="37", locator="§2.3.2.3", notes="'Adjacent to a front vowel, *ɣ is reflected as k in Southwest Tanna and is lost in the other languages' (p. 37).")
    if L != "lena1238":
        c(L, "ɣ", "∅", "#_", page="37", notes="In absolute initial position (before a non-front vowel) *ɣ was lost in all Tanna languages except Lenakel (p. 37).")
        c(L, "ɣ", "∅", "root-finally before a possessive suffix", page="38", notes="Lost here in all Tanna languages except Lenakel (p. 37).")
    c(L, "ɣ", g_else, page="38", locator="§2.3.2.3")
    c(L, "q", "∅", page="202", locator="Appendix I")
    c(L, "l", "l", page="46", locator="Table 2.5")
    for v in ["i", "e", "a", "o", "u"]: c(L, v, v, page="92", locator="§3.3")
    c(L, "ə", "ə", page="92", locator="§3.3", as_printed="ə ~ ∅")
    c(L, "ə", "∅", U, page="92", locator="§3.3", as_printed="ə ~ ∅", decision="lynch2001-variants")
L = "nort2847"
northern(L, [("ᵐb", "elsewhere", "19", "Usually b, sometimes bʷ, with no apparent conditioning (p. 19).", "regular", None, {"as_printed": "b ~ bʷ", "locator": "Appendix I"}),
             ("ᵐbʷ", U, "19", TILDE, "regular", None, {"as_printed": "b ~ bʷ", "decision": "lynch2001-variants"})],
         "ᵐb",
         [("∅", "_u", "26", "", "regular", None, {"locator": "§2.2.3"}), ("p", "_#", "25", "Word-finally p, which supports a stop *kʷ (p. 25).", "regular", None, {"as_printed": "u-u-p"}),
          ("u", "elsewhere", "26", "", "regular", None, {"as_printed": "u-u-p"}),
          ("∅", "_a", "26", "'With occasional loss before a in North Tanna' (p. 26).", "sporadic", None, {})],
         [("t", "elsewhere", "58", "", "regular", None, {"locator": "Appendix I"})],
         [("k", "_q", "57", "", "regular", None, {"locator": "§2.5.2.3"}), ("ⁿd", "_*Vkʷ", "57", "Printed d (prenasalised in North Tanna).", "regular", None, {}),
          ("t", "elsewhere", "58", "", "regular", None, {})],
         "r", "ŋ",
         [("∅", "_i", "24", "'Lost before i in North Tanna' (p. 24).", "regular", None, {}), ("v", "elsewhere", "24", "", "regular", None, {})])
c(L, "u", "o", "next to another vowel", status="sporadic", page="95", notes="'North Tanna often has o < *u when it is adjacent to another vowel' (p. 95).")
L = "whit1269"
northern(L, [("pʷ", "elsewhere", "19", "", "regular", None, {"locator": "Appendix I"})], "p",
         [("∅", "_u", "26", "", "regular", None, {}), ("∅", "u_#", "26", "", "regular", None, {}), ("u", "elsewhere", "26", "", "regular", None, {})],
         [("t", "elsewhere", "58", "", "regular", None, {"locator": "Appendix I"})],
         [("r", "_q, _*Vkʷ", "57", "Printed 'r ~ rh' (p. 58).", "regular", None, {"as_printed": "r ~ rh"}),
          ("rh", "_q, _*Vkʷ", "57", "The less frequent variant of 'r ~ rh' (p. 58).", "sporadic", None, {"as_printed": "r ~ rh"}),
          ("t", "elsewhere", "58", "", "regular", None, {})],
         "r", "ŋ", [("v", "elsewhere", "24", "", "regular", None, {})])
L = "lena1238"
northern(L, [("pʷ", "elsewhere", "19", "", "regular", None, {"locator": "Appendix I"})], "p",
         [("∅", "_u", "26", "Printed '∅ ~ w' (p. 26).", "regular", None, {"as_printed": "∅ ~ w"}),
          ("∅", "u_#", "26", "Printed '∅ ~ w' (p. 26).", "regular", None, {"as_printed": "∅ ~ w"}),
          ("w", "elsewhere", "25", "Lenakel underlying /w/ corresponds to SWT, Kwm kʷ: [owas] = /awas/ 'old', cognate with SWT, Kwm akwas; Appendix I prints 'u ~ w' (pp. 25-26).", "regular", None, {"as_printed": "u ~ w"})],
         [("r", "elsewhere", "56", "", "regular", None, {"locator": "Appendix I"}),
          ("l", "_Vl", "56", "'PTn *t assimilates to an l in a following syllable in Lenakel' (p. 56).", "regular", None, {})],
         [("t", "elsewhere", "57", "", "regular", None, {"locator": "Appendix I"})],
         "t", "k", [("v", "elsewhere", "24", "", "regular", None, {})])

# --- PST > Southwest Tanna, Kwamera
def southern(L, t, s_rows, h_rows, kw_rows, g_rows, r_rows, schwa):
    c(L, "pʷ", "pʷ", page="19", locator="Appendix I"); c(L, "p", "p", page="19", locator="Appendix I")
    c(L, "bʷ", "pʷ", page="19", locator="Appendix I"); c(L, "b", "p", page="19", locator="Appendix I")
    c(L, "v", "v", page="24", locator="Appendix I")
    rows(L, "kʷ", kw_rows)
    c(L, "mʷ", "mʷ", page="15", locator="Appendix I"); c(L, "m", "m", page="15", locator="Appendix I")
    c(L, "t", t, page="56", locator="Appendix I"); c(L, "d", "t", page="57", locator="Appendix I")
    rows(L, "s", s_rows)
    rows(L, "h", h_rows)
    c(L, "n", "n", page="50", locator="Appendix I"); c(L, "ŋ", "ŋ", page="29", locator="Appendix I")
    c(L, "k", "k", page="36", locator="Appendix I")
    rows(L, "ɣ", g_rows)
    c(L, "q", "∅", page="202", locator="Appendix I")
    rows(L, "r", r_rows)
    for v in ["i", "e", "a", "o"]: c(L, v, v, page="92", locator="§3.3")
    c(L, "u", "u", page="94", locator="Table 3.4")
    c(L, "u", "e", "_Cu; next to *q", page="94", locator="Table 3.4", notes="Dissimilation of the first *u in *uCu, and next to *q (p. 94); some words have i (p. 95).")
    rows(L, "ə", schwa)
L = "sout2869"
southern(L, "l", [("s", "elsewhere", "65", "", "regular", None, {"locator": "Appendix I"})], [("h", "elsewhere", "65", "", "regular", None, {"locator": "Appendix I"})],
         [("kʷ", "elsewhere", "26", "", "regular", None, {"locator": "Appendix I"})],
         [("k", "next to *i, *e", "37", "'Adjacent to a front vowel, *ɣ is reflected as k in Southwest Tanna' (p. 37).", "regular", None, {}),
          ("∅", "#_; _#", "39", "Summary p. 39: '∅ /#__, __#; k else'.", "regular", None, {}),
          ("k", "elsewhere", "39", "In other environments SWT 'it is sometimes lost and sometimes reflected as k' (p. 38).", "regular", None, {"as_printed": "k ~ ∅"}),
          ("∅", U, "38", TILDE, "regular", None, {"as_printed": "k ~ ∅", "decision": "lynch2001-variants"})],
         [("l", "elsewhere", "45", "The dialect with most data; the Mess dialect has r (p. 45, n. 15).", "regular", None, {"locator": "Appendix I"}),
          ("r", "elsewhere", "45", "Mess dialect (p. 45, n. 15).", "regular", None, {"variety": "Mess dialect"})],
         [("ə", "#_; V_V", "92", "", "regular", None, {"as_printed": "ə-ə-a ~ ∅"}), ("a", "_#", "92", "", "regular", None, {"as_printed": "ə-ə-a ~ ∅"}),
          ("∅", U, "92", TILDE, "regular", None, {"as_printed": "ə-ə-a ~ ∅", "decision": "lynch2001-variants"})])
L = "kwam1252"
southern(L, "r",
         [("h", "elsewhere", "65", "'The most frequent reflex of palatalised *t is h in Kwamera, s in the other languages' (p. 64).", "regular", None, {"as_printed": "h (~ s)", "locator": "Appendix I"}),
          ("s", U, "65", "No statable conditioning; 'a slight tendency for Kwamera to prefer s initially, finally and before i, and to prefer h adjacent to consonants' (p. 65).", "regular", None, {"as_printed": "h (~ s)", "decision": "lynch2001-variants"})],
         [("s", "elsewhere", "65", "The h : s set is the predominant one (p. 65).", "regular", None, {"as_printed": "s (~ h)", "locator": "Appendix I"}),
          ("h", U, "65", "The marginal h : h set (p. 65).", "regular", None, {"as_printed": "s (~ h)", "decision": "lynch2001-variants"})],
         [("k", "_u", "26", "", "regular", None, {"locator": "§2.2.3"}),
          ("k", "u_#", "26", "Word-finally after u Kwamera has 'sometimes kʷ, sometimes k' (p. 25).", "sporadic", None, {"as_printed": "kʷ ~ k"}),
          ("kʷ", "elsewhere", "26", "", "regular", None, {})],
         [("∅", "elsewhere", "39", "Normally lost, though there are one or two instances of k (p. 38).", "regular", None, {"locator": "§2.3.2.3"})],
         [("r", "elsewhere", "45", "", "regular", None, {"locator": "Appendix I"})],
         [("e", "#_; V_V", "92", "", "regular", None, {"as_printed": "e-e-a"}), ("a", "_#", "92", "", "regular", None, {"as_printed": "e-e-a"})])

# --- PEr > Ura, Utaha
L = "urav1235"
c(L, "p", "ᵐb", "V_V", page="17", source_form="b", notes="Medial *p and *b merge as b intervocalically (p. 17).")
c(L, "p", "p", page="19")
c(L, "b", "m", "_C", page="19", notes="The prenasalised stop loses its stop quality before a consonant (p. 17).")
c(L, "b", "ᵐb", page="19", source_form="b")
c(L, "f", "f", page="23"); c(L, "v", "v", page="23"); c(L, "w", "w", page="23"); c(L, "m", "m", page="14")
c(L, "k", "k", page="34")
c(L, "ɡ", "ŋ", "_C", page="32"); c(L, "ɡ", "k", "_#", page="33"); c(L, "ɡ", "ᵑɡ", page="33", source_form="g")
c(L, "ɣ", "∅", "_#", page="33"); c(L, "ɣ", "ɣ", page="33")
c(L, "ŋ", "ŋ", page="29"); c(L, "q", "∅", page="202", locator="Appendix I")
c(L, "l", "l", page="42")
c(L, "r", "t", "n_V", page="42", notes="*r > t after *n, with nt coalescing as d (p. 42).")
c(L, "r", "∅", "n_#", page="42", notes="Final *nr became Ura n (p. 42).")
c(L, "r", "r", page="42")
c(L, "L", "l", page="42")
c(L, "t", "t", "#_", page="56", as_printed="t-r-t (h)")
c(L, "t", "r", "V_V", page="54", as_printed="t-r-t (h)")
c(L, "t", "h", "_n", page="54", notes="Medially before n (p. 54); one case before l, *tuRi > ehli (n. 21).")
c(L, "t", "t", "_#", page="55", as_printed="t-r-t (h)")
c(L, "t", "t", "V_V", status="loan-stratum", page="55", notes="Medial t in Ura (Sye t) is likely to be from Sye loans: Sye became the prestige language and the few Ura speakers speak Sye more than Ura (p. 55).")
c(L, "d", "ⁿd", page="56", source_form="d")
c(L, "s", "s", page="71")
c(L, "s", "h", "_C (continuant)", page="71", notes="'Medial s in Ura became h before a continuant consonant' (p. 71), after PEr *s and *h merged finally and next to a consonant.")
c(L, "h", "∅", "#_", page="68", notes="Initial s : ∅ occurs only in verbs (p. 67).")
c(L, "h", "s", page="68", notes="Intervocalically, and finally and next to a consonant, where PEr *s and *h merged (p. 71).")
c(L, "h", "h", "_C (continuant)", page="71")
c(L, "n", "n", page="50"); c(L, "y", "j", page="49", source_form="y")
c(L, "i", "i", page="83"); c(L, "e", "e", page="83"); c(L, "a", "a", page="83"); c(L, "o", "o", page="83"); c(L, "u", "u", page="83")
c(L, "ə", "i", page="90", as_printed="i, ∅", notes="Sye o (/ə/) corresponds to Ura i (pp. 90-91).")
c(L, "ə", "∅", U, page="83", as_printed="i, ∅")
L = "ifoo1237"
UTH = "Utaha reflexes are 'extremely tentative and based on just a few comparisons' (p. 19)."
c(L, "p", "p", page="19", notes=UTH, locator="Appendix I")
c(L, "b", "p", "#_", page="201", as_printed="p-mp-", locator="Appendix I"); c(L, "b", "mp", "V_V", page="201", as_printed="p-mp-", locator="Appendix I")
c(L, "v", "v", page="23"); c(L, "w", "w", page="23"); c(L, "m", "m", page="14", locator="Appendix I")
c(L, "k", "k", page="34", locator="Appendix I")
c(L, "ɡ", "ɡ", U, page="34", as_printed="g or ŋk", decision="lynch2001-variants")
c(L, "ɡ", "ŋk", U, page="34", as_printed="g or ŋk", decision="lynch2001-variants")
c(L, "ŋ", "ŋ", page="203", locator="Appendix I"); c(L, "q", "∅", page="202", locator="Appendix I")
c(L, "l", "l", page="42"); c(L, "r", "r", page="42"); c(L, "L", "l", page="42")
c(L, "t", "t", page="56", as_printed="t?", notes="Printed with a question mark (p. 56).")
c(L, "d", "r", page="56", as_printed="r?", notes="Printed with a question mark (p. 56).")
c(L, "n", "n", page="203", locator="Appendix I")

# --- reparent batch: PEr > Sye, PSV > Anejom
if REPARENT:
    CORR = []; CNT.clear()
    L = "siee1239"
    c(L, "p", "p", page="19")
    c(L, "b", "mp", "V_", page="19", notes="'The unit phoneme *b has been reanalysed as the cluster mp' after a vowel; *p and *b merge as p after a consonant (p. 17).")
    c(L, "b", "p", page="19", notes="Initially and after a consonant (p. 17).")
    c(L, "f", "p", "#_", page="23"); c(L, "f", "v", page="23", notes="Medially (p. 23).")
    c(L, "v", "v", page="23"); c(L, "w", "w", page="23"); c(L, "m", "m", page="14")
    c(L, "k", "k", page="32"); c(L, "k", "ɣ", "_#", page="32", notes="Sye disallows final k... 'the Sye reflex is ɣ rather than k' (p. 32).")
    c(L, "ɡ", "k", "#_", page="32"); c(L, "ɡ", "ŋk", "V_V", page="32", notes="Medially (p. 32); Sye ŋk loses the nasal after another nasal in namkai 'dry coconut' (p. 33).")
    c(L, "ɡ", "ŋ", "_#", page="33")
    c(L, "ɣ", "k", "_i", page="33"); c(L, "ɣ", "ɣ", page="33")
    c(L, "ŋ", "ŋ", page="29"); c(L, "q", "∅", page="202", locator="Appendix I")
    c(L, "l", "l", page="42"); c(L, "r", "r", page="42"); c(L, "L", "r", page="42")
    c(L, "t", "t", page="56")
    c(L, "d", "t", "#_", page="56", as_printed="t-nt-nt", notes="Initial d : t may also be initial *nt simplified in Sye (p. 54).")
    c(L, "d", "nt", page="56", as_printed="t-nt-nt")
    S_NOTE = "PEr *s and *h merged (probably as s) finally and next to a consonant; then medial s in Sye became h before any consonant and was lost before l, m and ŋ, and final s became h after a non-high vowel (p. 71)."
    for x in ["s", "h"]:
        c(L, x, "h", "_C", page="71", notes=S_NOTE)
        c(L, x, "∅", "_l, _m, _ŋ", page="71", notes=S_NOTE)
        c(L, x, "s", "i_#, u_#", page="70", notes=S_NOTE)
        c(L, x, "h", "e_#, a_#, o_#", page="70", notes=S_NOTE)
    c(L, "s", "s", page="67", notes="Initially, intervocalically and after a consonant (Table 2.6). Crowley reports massive free variation between [h] and [s] in Sye (Lynch 2001: 59).")
    c(L, "h", "s", "#_", page="68", notes="Initial s : ∅ (PEr *h) occurs only in verbs (p. 67).")
    c(L, "h", "h", "V_V", page="68")
    c(L, "n", "n", page="50")
    c(L, "y", "j", page="49", source_form="y", as_printed="y ~ i"); c(L, "y", "i", U, page="203", as_printed="y ~ i", locator="Appendix I", decision="lynch2001-variants")
    c(L, "i", "i", page="83")
    c(L, "i", "e", "next to (*s +) a labial obstruent", page="84", notes="'Lowering occurred in Sye when *i was adjacent to (*s plus) a labial obstruent' (p. 84).")
    c(L, "e", "e", page="83")
    c(L, "ə", "o", U, page="90", as_printed="/ə/ = o, ∅", notes="Crowley posits an underlying sixth vowel /ə/ in Sye, which surfaces as o or zero (Lynch 2001: 8, 90).")
    c(L, "ə", "∅", U, page="90", as_printed="/ə/ = o, ∅")
    c(L, "a", "a", page="88")
    c(L, "a", "o", "w_, m_, ŋ_", page="89", notes="'A tendency for Sye to reflect *a as o especially after w, m or ŋ' (p. 89).")
    c(L, "a", "e", "_#", page="89", notes="'A reasonably frequent trend for final POc *a after other consonants to become e in Sye (though there are exceptions)' (p. 89).")
    c(L, "o", "o", page="83"); c(L, "u", "u", page="83")
    L = "anei1239"
    c(L, "pʷ", "pʷ", page="20", locator="Table 2.2"); c(L, "p", "p", page="20", locator="Table 2.2")
    c(L, "bʷ", "pʷ", page="20", locator="Table 2.2", notes="Anejom 'has lost the voicing distinction but has retained the simple/velarised distinction' (p. 20).")
    c(L, "b", "p", page="20", locator="Table 2.2")
    c(L, "v", "h", page="26", locator="Table 2.2", as_printed="h-h-∅")
    c(L, "v", "∅", "_#", page="27", locator="Table 2.2", as_printed="h-h-∅", notes="Some cases of final h suggest that *v was once h finally too (p. 27).")
    c(L, "w", "v", page="28", locator="Table 2.2")
    c(L, "w", "w", U, page="28", as_printed="v (w)", notes="'Some cases where the Anejom reflex is w or u rather than v ... I am unable to specify the conditioning' (p. 28).")
    c(L, "mʷ", "mʷ", page="16", locator="Table 2.2"); c(L, "m", "m", page="16", locator="Table 2.2")
    c(L, "k", "ɣ", page="39", locator="Table 2.3", notes="Appendix I has Anj ɣ for both PSV *k and *ɣ (p. 202); a few POc *k are k in Anejom (p. 31).")
    c(L, "ɣ", "ɣ", page="31", locator="Table 2.3")
    c(L, "ɣ", "∅", status="sporadic", page="31", notes="'A small group of words in which non-final POc *k is inexplicably lost' (p. 31).")
    c(L, "ɡ", "k", page="30", locator="Table 2.3")
    c(L, "ŋ", "ɲ", "_i, _e", page="29", locator="Table 2.3", source_form="ñ")
    c(L, "ŋ", "ŋ", page="29", locator="Table 2.3")
    c(L, "q", "∅", page="74")
    c(L, "l", "t͡ʃ", "_i, _e, _o", page="44", locator="Table 2.5", source_form="j", notes="Before POc *i, *e and *o (p. 44); not in *lisaq 'nit' or *tolo 'swallow'.")
    c(L, "l", "l", page="45", locator="Table 2.5")
    c(L, "r", "r", page="44", locator="Table 2.5", as_printed="r-r-∅")
    c(L, "r", "∅", "_#", page="44", locator="Table 2.5", as_printed="r-r-∅", notes="Except *paRi > n/har 'stingray' (p. 44).")
    c(L, "t", "t", page="53", locator="Table 2.7")
    c(L, "t", "s", "_#", page="52", locator="Table 2.7", notes="Only word-final, not morpheme-final, *t (p. 53).")
    c(L, "c", "s", page="61", locator="Table 2.7")
    c(L, "d", "t͡ʃ", page="52", locator="Table 2.7", source_form="j")
    c(L, "s", "θ", page="61", locator="Table 2.7", notes="A few *s before *i are s (p. 62).")
    c(L, "s", "h", status="sporadic", page="74", notes="Apparent cognates with h for a sibilant (p. 74).")
    c(L, "j", "s", page="66", locator="Table 2.7")
    c(L, "n", "ɲ", "_i, _e", page="50", locator="Table 2.7", source_form="ñ", notes="Nasal palatalisation preceded final vowel loss (p. 51).")
    c(L, "n", "n", page="50", locator="Table 2.7")
    c(L, "y", "j", page="49", locator="Table 2.7", source_form="y")
    c(L, "i", "e", page="82", locator="Table 3.2")
    c(L, "i", "o", "u_, w_", page="77", locator="Table 3.2")
    c(L, "i", "i", "_-SUFFIX", page="77", locator="Table 3.2", notes="A tendency, morpheme-finally before a suffix, and morpheme-initially in some words (p. 77).")
    c(L, "e", "e", page="80", locator="Table 3.2")
    c(L, "e", "i", "_PALATAL", page="81", locator="Table 3.2", notes="*a > e before *Ci, *Cu 'was sometimes further raised to i when immediately preceding an Anejom palatal consonant' (p. 81).")
    c(L, "a", "a", page="80", locator="Table 3.2")
    c(L, "a", "o", "next to a labial", page="82", locator="Table 3.2", notes="'A tendency' (p. 82).")
    c(L, "a", "i", "CC_-i", page="82", locator="Table 3.2", notes="Sometimes, before the transitive suffix (p. 82).")
    c(L, "ə", "e", page="82", locator="Table 3.2", notes="POc *a > e before *Ca, with exceptions (p. 82).")
    c(L, "o", "e", page="79", locator="Table 3.2")
    c(L, "u", "o", page="76", locator="Table 3.2")
    c(L, "u", "e", "θ_, ɣ_", page="77", locator="Table 3.2", notes="'Adjacent to θ or following ɣ, though there are counter-examples' (p. 77).")
    c(L, "u", "u", "morpheme-initially; before a vowel", page="77", locator="Table 3.2", notes="Before another vowel sometimes w (p. 77).")
    c(L, "u", "i", status="sporadic", page="78", notes="'A residue of cases where *u > i whose conditioning I cannot determine' (p. 78).")

ALLO = []
def al(lect, ph_, allo, env, page, notes=""):
    ALLO.append(dict(lect_id=lect, phoneme=ph_, allophone=allo, environment=env, source_id=S, page=page, notes=notes))
DEV = "'In all Tanna languages, nasals, liquids, /v/ and semivowel allophones of the high vowels devoice when adjacent to /h/, which is then lost' (p. 8)."
GLIDE = "'High vowels have non-syllabic allophones when adjacent to vowels in certain contexts' (p. 8)."
for L, cons in [("lena1238", ["mʷ", "m", "n", "ŋ", "l", "r", "v"]), ("whit1269", ["mʷ", "m", "n", "ŋ", "l", "r", "v"]),
                ("nort2847", ["mʷ", "m", "n", "ŋ", "l", "r", "v"]), ("kwam1252", ["mʷ", "m", "n", "ŋ", "r", "v"]),
                ("sout2869", ["mʷ", "m", "n", "ŋ", "l", "v"])]:
    for x in cons:
        vl = {"mʷ": "m̥ʷ", "ŋ": "ŋ̊", "v": "v̥"}.get(x, x + "\u0325")
        al(L, x, unicodedata.normalize("NFC", vl), "next to h (h is lost)", "8", DEV)
    al(L, "i", "j", "next to a vowel (some contexts)", "8", GLIDE); al(L, "u", "w", "next to a vowel (some contexts)", "8", GLIDE)
    al(L, "i", "j̊", "next to h, as a glide (h is lost)", "8", DEV); al(L, "u", "w̥", "next to h, as a glide (h is lost)", "8", DEV)
al("urav1235", "i", "j", "next to a vowel (some contexts)", "8", GLIDE); al("urav1235", "u", "w", "next to a vowel (some contexts)", "8", GLIDE)

DECISIONS = [
 dict(id="lynch2001-tree", batch="lynch2001", status="open", source_id=S, page="13, 184",
      question="Where do the Southern Vanuatu lects go, and what happens to Sye and Anejom, which were entered from Lynch et al. (2002) directly under POc?",
      chosen_reading="Proto-Southern Vanuatu under POc (in the Southern Oceanic group), with Proto-Erromango (Sye, Ura, Utaha), Proto-Tanna (Proto-Northern Tanna: North Tanna, Whitesands, Lenakel; Proto-Southern Tanna: Southwest Tanna, Kwamera) and Anejom, as in Lynch (2001: 13, 184; Appendix I). Sye is moved under Proto-Erromango and Anejom under PSV in the sheet; their rows are a second batch (lynch2001-reparent).",
      alternatives="Keep Sye and Anejom under POc with POc-based rows; or leave out Proto-Northern and Proto-Southern Tanna, which Lynch gives only in Appendix I.",
      notes="Glottocodes: sout2868, erro1239, tann1242, nort3218 (a linkage in Glottolog), sout3195, each with the same membership."),
 dict(id="lynch2001-variants", batch="lynch2001", status="open", source_id=S, page="11, 74",
      question="How are Lynch's (2001) unconditioned variants entered: 'x ~ y' ('x or y, but more often x'), the fortis/lenis splits of POc *p, *pʷ and *k, and PEr *r ~ *L?",
      chosen_reading="The more frequent reflex as regular 'elsewhere', the other as regular with 'conditions unknown', each with the cell in as_printed. Parenthesised reflexes in Appendix I are conditioned (p. 74) and are entered with the condition from chapters 2-3; where the text calls a reflex sporadic, exceptional or a small group of words, it is sporadic.",
      alternatives="Enter the less frequent variant as sporadic."),
 dict(id="lynch2001-pnt-pst", batch="lynch2001", status="open", source_id=S, page="202",
      question="Appendix I prints '?' for *q in Proto-Northern and Proto-Southern Tanna. Was *q still there?",
      chosen_reading="PTn *q > PNT, PST *q with status disputed; each Tanna language has *q > ∅.",
      alternatives="*q lost at PNT and PST."),
 dict(id="lynch2001-psv-e", batch="lynch2001", status="open", source_id=S, page="96-99",
      question="PSV *e has two sources (POc *e; POc *a before *Ci, *Cu) with different Proto-Tanna reflexes (*i and *e; Tables 3.4-3.5).",
      chosen_reading="PSV *e > PTn *i regular, and PSV *e > PTn *e with conditioning 'lexical' (scope: PSV *e from POc *a before *Ci, *Cu). Not split into two PSV phonemes, since Lynch reconstructs one.",
      alternatives="Two PSV phonemes; or POc > PTn rows that skip PSV for these vowels."),
 dict(id="lynch2001-ipa", batch="lynch2001", status="open", source_id=S, page="7-9",
      question="Lynch's symbols for the modern Southern Vanuatu languages.",
      chosen_reading="IPA, with Lynch's letter in source_symbol or source_form: y = j (glide); Anejom j = t͡ʃ, ñ = ɲ; Ura b d g and North Tanna bʷ b d = ᵐb ⁿd ᵑɡ, ᵐbʷ ᵐb ⁿd (prenasalised); Sye clusters mp, ŋk, nt kept as clusters (Lynch: the unit phonemes were reanalysed as clusters, p. 17). Inventories: Ura, Lenakel, Kwamera from §1.5.1 (p. 7), and Whitesands, North Tanna, Southwest Tanna by Lynch's statements of how they differ; North Tanna and Whitesands /w/ (unclear, p. 7 n. 6) not entered; Kwamera and Southwest Tanna /fʷ/ marginal (in parentheses), Whitesands /fʷ/ marginal ('may also have').",
      alternatives="Keep Lynch's letters."),
]
NOTATION = [dict(lect_id=x, phoneme="", system="canonical", symbol="", source_id=S, page=pg,
                 notes="Lynch's orthography: POc orthography of Ross (1988) for consonants (§1.5.4), with *ɣ (printed γ) and *ə.")
            for x, pg in [("psv", "14"), ("per", "13-91"), ("ptn", "13-99"), ("pnt", "201-203"), ("pst", "201-203")]]

def write(table, rows):
    cols = B.TABLES[table]; OUT.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO(); w = csv.writer(buf, lineterminator="\n"); w.writerow(cols)
    for r in rows: w.writerow([N(str(r.get(c_, ""))) for c_ in cols])
    (OUT / f"{table}.csv").write_text(buf.getvalue(), encoding="utf-8"); print(table, len(rows))

if REPARENT:
    write("correspondences", CORR)
else:
    write("sources", SOURCES); write("lects", LECTS); write("phonemes", PHONEMES)
    write("correspondences", CORR); write("notation_map", NOTATION); write("decisions", DECISIONS)
    write("allophones", ALLO)
