"""Batch nc-ozannerivierre1992: Proto-New Caledonian consonants (Ozanne-Rivierre 1992; Geraghty 1989).

Ozanne-Rivierre, Françoise. 1992. The Proto-Oceanic consonantal system and the languages of New Caledonia.
Oceanic Linguistics 31(2). 191-207. Geraghty, Paul. 1989. The reconstruction of Proto-Southern Oceanic.
In Ray Harlow & Robin Hooper (eds.), VICAL 1, 141-156. Both read from PDFs (text layers; tables and
examples checked against page images).

    python3 tools/batch_scripts/nc1992/build.py
"""
import csv, io, sys, unicodedata
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
import build as B  # noqa: E402
N = lambda s: unicodedata.normalize("NFC", s)
S = "ozannerivierre1992"; G = "geraghty1989"
OUT = ROOT / "data/incoming/nc-ozannerivierre1992"

SOURCES = [
 dict(id=S, author="Ozanne-Rivierre, Françoise", year="1992", title="The Proto-Oceanic consonantal system and the languages of New Caledonia",
      url_or_doi="https://doi.org/10.2307/3623014", kind="comparative", pub_type="article", container_title="Oceanic Linguistics",
      volume="31", issue="2", pages="191-207",
      notes="Consulted directly on 23 November 2026 (JSTOR PDF; tables and examples read from page images): the POc system she "
            "assumes (Table 1, p. 192), reflexes of POc *t, *d, *s, *k in the northern languages (Table 2, p. 194), POc *q "
            "(pp. 194-196), the prenasalised series (pp. 196-201; Table 3, Drubea, p. 199), and the PNC consonant system with "
            "its innovations from POc (Table 4 and §5, p. 202; notes 5, 9-12, pp. 204-205). Her POc *d is Ross's *r and her "
            "*nt, *nd are Ross's *d, *dr (p. 196)."),
 dict(id=G, author="Geraghty, Paul", year="1989", title="The reconstruction of Proto-Southern Oceanic", kind="comparative",
      pub_type="chapter", container_title="VICAL 1: Oceanic languages. Papers from the Fifth International Conference on Austronesian Linguistics",
      editors="Ray Harlow; Robin Hooper", pages="141-156", place="Auckland", publisher="Linguistic Society of New Zealand",
      notes="Consulted directly on 23 November 2026 (scan with a cropped left margin, ABBYY text layer): orthography (Table 1, "
            "p. 143), innovations shared with Vanuatu (pp. 148-150) and the phonological innovations of PSO (pp. 150-151). "
            "Geraghty's Southern Oceanic is New Caledonia and the Loyalty Islands (p. 141), the Proto-New Caledonian node here, "
            "not the Southern Oceanic of Lynch and Ross, which includes Vanuatu. He derives PSO from his Proto-Eastern Oceanic."),
]
LECTS = [
 dict(id="yuag1237", name="Zuanga-Yuanga", alt_names="Yuanga", type="language", glottocode="yuag1237", iso639_3="nua", parent_id="pnc",
      notes="Language node for its dialects Gomen Yuanga and Bondé Yuanga (Ozanne-Rivierre 1992: 192-193)."),
 dict(id="thua1237", name="Gomen Yuanga", alt_names="Yua2; Zuanga", type="dialect", glottocode="thua1237", parent_id="pnc", language_id="yuag1237",
      notes="Northern New Caledonian. Keeps dental /t̪/ (< POc *s) apart from retroflex /ʈ/ (< POc *d, Ross's *r), while POc *t became k (Ozanne-Rivierre 1992: 192-193). Glottocode thua1237 (Zuanga) is an identification (decision nc1992-lects)."),
 dict(id="juan1250", name="Bondé Yuanga", alt_names="Yua1; Yuanga", type="dialect", glottocode="juan1250", parent_id="pnc", language_id="yuag1237",
      notes="Northern New Caledonian; data from Corne's manuscript dictionary (Ozanne-Rivierre 1992: 206). Glottocode juan1250 (Yuanga dialect) is an identification (decision nc1992-lects)."),
 dict(id="kuma1276", name="Nêlêmwa-Nixumwak", type="language", glottocode="kuma1276", iso639_3="nee", parent_id="pnc",
      notes="Language node for its dialect Kumak (Nixumwak)."),
 dict(id="nucl1483", name="Kumak", alt_names="Nixumwak; Koumac", type="dialect", glottocode="nucl1483", parent_id="pnc", language_id="kuma1276",
      notes="Northern New Caledonian (Koumac); data from Haudricourt (via Ozanne-Rivierre 1992)."),
 dict(id="bala1316", name="Nyelâyu", alt_names="Balade; Yalayu", type="language", glottocode="bala1316", parent_id="pnc", latitude="-20.25", longitude="164.20",
      notes="Far North New Caledonian. Some spontaneous nasalisation of a in the Belep variety may attest an earlier initial glottal (Ozanne-Rivierre 1992: 194). Glottocode and coordinates from the language metadata of Ross et al. (2023: 627), which has Nyelâyu as bala1316."),
 dict(id="pwap1237", name="Pwapwâ", alt_names="Pwapwa", type="language", glottocode="pwap1237", iso639_3="pop", parent_id="pnc",
      notes="Northern New Caledonian (Ozanne-Rivierre 1992)."),
 dict(id="pwaa1237", name="Pwaamei", type="language", glottocode="pwaa1237", iso639_3="pme", parent_id="pnc", latitude="-20.84", longitude="164.77",
      notes="Northern New Caledonian (Ozanne-Rivierre 1992). Coordinates from the language metadata of Ross et al. (2023: 627)."),
 dict(id="nemi1240", name="Nemi", type="language", glottocode="nemi1240", iso639_3="nem", parent_id="pnc", latitude="-20.68", longitude="164.80",
      notes="Northern New Caledonian, Hienghène region (Ozanne-Rivierre 1992). Coordinates from the language metadata of Ross et al. (2023: 626), which prints the Glottocode as nemi124."),
 dict(id="have1241", name="Haveke", type="language", glottocode="have1241", iso639_3="hvk", parent_id="pnc",
      notes="Northern New Caledonian (Ozanne-Rivierre 1992)."),
 dict(id="nume1242", name="Numèè", alt_names="Numee", type="language", glottocode="nume1242", iso639_3="kdk", parent_id="pnc", latitude="-22.25", longitude="166.87",
      notes="Extreme southern New Caledonian; keeps POc *q apart from *k, as Drubea does (Ozanne-Rivierre 1992: 195). Coordinates from the language metadata of Ross et al. (2023: 627)."),
 dict(id="dumb1241", name="Drubea", alt_names="Dumbea", type="language", glottocode="dumb1241", iso639_3="duf", parent_id="pnc", latitude="-22.09", longitude="166.53",
      notes="Extreme southern New Caledonian. Vowel nasality is phonological only after oral consonants (Ozanne-Rivierre 1992: 199, after Rivierre's study of the Far South dialects). Coordinates from the language metadata of Ross et al. (2023: 624)."),
 dict(id="dehu1237", name="Drehu", alt_names="Dehu", type="language", glottocode="dehu1237", iso639_3="dhv", parent_id="pnc", latitude="-20.89", longitude="167.23",
      notes="Loyalty Islands (Lifou). Its voiced /b/ comes from English loans; prenasalised consonants no longer exist in the Loyalties (Ozanne-Rivierre 1992: 197). Coordinates from the language metadata of Ross et al. (2023: 624)."),
 dict(id="neng1238", name="Nengone", type="language", glottocode="neng1238", iso639_3="nen", parent_id="pnc", latitude="-21.53", longitude="167.96",
      notes="Loyalty Islands (Maré) (Ozanne-Rivierre 1992: 197). Coordinates from the language metadata of Ross et al. (2023: 626)."),
]

def ph(ipa, place, manner, voicing, notes=""):
    return dict(lect_id="pnc", ipa=ipa, **{"class": "C"}, place=place, manner=manner, voicing=voicing, origin="sourced",
                source_id=S, page="202", notes=notes)
GEM = "Geminate, from the loss of the pretonic vowel in reduplicated forms and proclitics (pp. 202-203); Geraghty (1989: 151) has aspirated stops and voiceless sonorants here."
PH = [("pʷ", "bilabial", "plosive", "voiceless", "Developed in PNC by devocalisation of *u before an accented vowel: POc *puaq > PNC *pwa-n 'its fruit' (p. 205, n. 12)."),
      ("ppʷ", "bilabial", "plosive", "voiceless", GEM), ("p", "bilabial", "plosive", "voiceless", ""), ("pp", "bilabial", "plosive", "voiceless", GEM),
      ("t", "dental", "plosive", "voiceless", "Apical dental (Table 4)."), ("tt", "dental", "plosive", "voiceless", GEM),
      ("ṭ", "retroflex", "plosive", "voiceless", "Apical retroflex, from POc *d (Ross's *r); still a stop in most languages (p. 192)."), ("ṭṭ", "retroflex", "plosive", "voiceless", GEM),
      ("s", "alveolar", "fricative", "voiceless", "Laminal (Table 4); charted as alveolar."), ("ss", "alveolar", "fricative", "voiceless", GEM),
      ("k", "velar", "plosive", "voiceless", ""), ("kk", "velar", "plosive", "voiceless", GEM),
      ("q", "uvular", "plosive", "voiceless", "Postvelar; a uvular stop, as Haudricourt suggested (p. 195)."), ("qq", "uvular", "plosive", "voiceless", GEM),
      ("mbʷ", "bilabial", "prenasalized-plosive", "voiced", "Printed mbw."), ("mb", "bilabial", "prenasalized-plosive", "voiced", ""),
      ("nd", "dental", "prenasalized-plosive", "voiced", ""), ("nḍ", "retroflex", "prenasalized-plosive", "voiced", ""),
      ("nj", "palatal", "prenasalized-plosive", "voiced", "Laminal; still a true prenasalised consonant on the mainland (p. 201)."),
      ("ŋɡ", "velar", "prenasalized-plosive", "voiced", "Printed ŋg."),
      ("mʷ", "bilabial", "nasal", "voiced", "Printed mw."), ("mmʷ", "bilabial", "nasal", "voiced", GEM), ("m", "bilabial", "nasal", "voiced", ""),
      ("mm", "bilabial", "nasal", "voiced", GEM), ("n", "alveolar", "nasal", "voiced", "Apical (one nasal for the dental and retroflex columns)."),
      ("nn", "alveolar", "nasal", "voiced", GEM), ("ŋ", "velar", "nasal", "voiced", ""), ("ŋŋ", "velar", "nasal", "voiced", GEM),
      ("w", "labial-velar", "approximant", "voiced", "")]
PHONEMES = [ph(*x) for x in PH]
for r in PHONEMES:
    if r["ipa"] in ("pʷ", "mbʷ", "mʷ", "ŋɡ"): r["source_symbol"] = {"pʷ": "pw", "mbʷ": "mbw", "mʷ": "mw", "ŋɡ": "ŋg"}[r["ipa"]]
    if r["ipa"] in ("ppʷ", "mmʷ"): r["source_symbol"] = {"ppʷ": "ppw", "mmʷ": "mmw"}[r["ipa"]]

CORR = []; CNT = {}
def c(lect, p, ch, env="elsewhere", page="202", notes="", status="regular", src=S, cond=None, **kw):
    CNT[lect] = CNT.get(lect, 0) + 1
    r = dict(id=f"{lect}-or92-{CNT[lect]}" if src == S else f"{lect}-g89-{CNT[lect]}", child_lect_id=lect, parent_phoneme=p,
             child_phoneme=ch, environment=env, status=status, source_id=src, page=page, notes=notes)
    if cond: r["conditioning"] = cond
    elif env == "conditions unknown": r["conditioning"] = "unknown"
    elif env != "elsewhere": r["conditioning"] = "stated"
    r.update(kw); CORR.append(r)
U = "conditions unknown"
MAP = "Ozanne-Rivierre writes POc in Milke's spelling: her *d is Ross's *r, her *mpw, *mp, *nt, *nd, *nj, *ŋk are Ross's *bʷ, *b, *d, *dr, *j, *ɡ (pp. 192, 196); decision nc1992-orthography."
P = "pnc"
c(P, "p", "p", page="202", locator="Table 4"); c(P, "t", "t", page="192", locator="Table 4", notes="Dental *t and retroflex *d (Ross's *r) did not merge (p. 194).")
c(P, "r", "ṭ", page="192", locator="Table 4", decision="nc1992-orthography", as_printed="POc *d > PNC *ṭ",
  notes="'The widely observed *d to r drift in the Oceanic languages has not occurred in Proto-New Caledonian'; POc *d is reflected by a retroflex stop (p. 192). " + MAP)
c(P, "s", "s", page="202", locator="Table 4")
c(P, "c", "s", page="202", locator="§5 (a)", as_printed="the merger of Blust's *j with *s", notes="Blust's *j is Ross's *c (p. 192).")
c(P, "j", "nj", page="201", locator="Table 4", decision="nc1992-orthography", as_printed="POc *nj > PNC *nj", notes=MAP)
for p_, ch in [("bʷ", "mbʷ"), ("b", "mb"), ("d", "nd"), ("dr", "nḍ"), ("ɡ", "ŋɡ")]:
    c(P, p_, ch, page="202", locator="Table 4", decision="nc1992-orthography", notes=MAP)
c(P, "k", "k", page="194", locator="Table 4"); c(P, "q", "q", page="195", locator="Table 4", notes="Kept apart from *k in the northern languages and in Numèè and Drubea (pp. 194-195).")
c(P, "mʷ", "mʷ", locator="Table 4"); c(P, "m", "m", locator="Table 4"); c(P, "n", "n", locator="Table 4")
c(P, "ñ", "n", locator="§5 (b)", notes="The apparent retention of *ñ in Iaai is secondary (p. 205, n. 9).")
c(P, "ŋ", "ŋ", locator="Table 4")
c(P, "l", "n", locator="§5 (c)", notes="Palatal reflexes of *l in Kone dialects (*laŋo > Haveke ñiin) are secondary, like those of *n (p. 205, n. 10).")
c(P, "R", "∅", locator="§5 (d)", notes="Geraghty's sporadic retention of *R is worth exploring, but his examples other than *paRu are too irregular (p. 205, n. 11).")
c(P, "y", "∅", locator="§5 (d)"); c(P, "w", "w", locator="Table 4")
c(P, "p", "pʷ", "_+u", page="205", locator="n. 12", notes="'*pw has developed in PNC by devocalization of /u/ before accented vowels': *puaq > *pwa-n (n. 12, citing Geraghty 1989: 152).")
c(P, "u", "pʷ", "p+_", page="205", locator="n. 12", notes="Before an accented vowel.")
# Geraghty 1989 on the same node (PSO)
c(P, "ñ", "n", page="150", src=G, notes="Innovation 2 of PSO: *ñ merges with *n (*-ñ > *-n 'his').")
c(P, "l", "n", page="151", src=G, notes="Innovation 4: *l merges with *n (*lima- > *nima-).")
c(P, "l", "r", "after *ka-", page="151", src=G, decision="nc1992-geraghty",
  notes="'A strange exception': *l becomes *r after *xa- (< *k-): *xarov 'beckon' (*kalo-v), *xharab 'swallow' (*kalaba) (p. 151).")
c(P, "R", "∅", page="151", src=G, notes="Innovation 3: *R is lost 'in all but a handful of forms'.")
c(P, "R", "r", "V_i, V_u", status="sporadic", page="148", src=G, decision="nc1992-geraghty", locator="Table 2",
  notes="Sporadic retention as r intervocalically before a high vowel (pp. 148-149): *vaRu 'Hibiscus tiliaceus' > Drehu elu, Nengone eru. Ozanne-Rivierre (1992: 205, n. 11) accepts only this example.")
c(P, "y", "∅", page="151", src=G, notes="Innovation 5: *y is lost (certainly initially).")
for p_ in ["k", "p"]:
    c(P, p_, "x", "V_V", page="151", src=G, status="disputed", decision="nc1992-geraghty",
      notes="'Intervocalic *k and *p merge as PSO *x, which is then lost in certain environments (after a?)': *vupu- > *vuxu- 'cause', *toko > *toxo- 'stick' (p. 151). Ozanne-Rivierre's PNC has no *x.")

# daughters, composed through PNC (Table 2, examples (1)-(14))
T2 = dict(locator="Table 2", page="194")
def comp(L, p_, ch, env, printed, **kw):
    c(L, p_, ch, env, derivation="composed", as_printed=printed, **kw)
for L, t_, d_, s_, k_ in [("thua1237", "k", "ʈ", "t̪", "c"), ("juan1250", "k", "t", "t", "c"), ("nucl1483", "k", "t", None, "c"),
                          ("pwap1237", "c", "t", None, "c"), ("pwaa1237", "c", "t", None, "ɣ"), ("cemu1238", "c", "t", None, "∅")]:
    comp(L, "t", t_, "#_", f"POc *t- > {t_}-", **T2)
    comp(L, "ṭ", d_, "#_", "POc *d- > " + ("ṭ-" if d_ == "ʈ" else "t-"), source_form="ṭ" if d_ == "ʈ" else "",
         notes="In the other northern languages the dentals have merged with the retroflexes (p. 192)." if d_ == "t" else "", **T2)
    if s_: comp(L, "s", s_, "#_", "POc *s- > " + ("t̪-" if s_ == "t̪" else "t-"), notes="Merges with the reflex of *d (Table 2 arrow)." if s_ == "t" else "", **T2)
    comp(L, "k", k_, "#_", f"POc *k- > {'γ' if k_ == 'ɣ' else k_}-", notes="'One of this group's common innovations is the palatalization of *k to c' (p. 194)." if k_ == "c" else "", **T2)
comp("nemi1240", "t", "t", "#_", "POc *t- > t-, c-", **T2); comp("nemi1240", "t", "c", U, "POc *t- > t-, c-", **T2)
comp("nemi1240", "ṭ", "t", "#_", "POc *d- > t-", **T2); comp("nemi1240", "k", "c", "#_", "POc *k- > c-", **T2)
comp("juan1250", "ṭ", "l", "_#", "POc *tuqud > kɔɔl", page="193", notes="'A few northern languages where -ṭ > -l or -r' (p. 193).")
comp("bala1316", "ṭ", "r", "_#", "POc *tuqud > cuur", page="193", notes="'A few northern languages where -ṭ > -l or -r' (p. 193).")
Q = dict(page="194-195", locator="(3)")
comp("bala1316", "q", "∅", "elsewhere", "POc *q > ∅", notes="'In all contexts, probably after a glottal phase' (p. 194).", **Q)
comp("nucl1483", "q", "∅", "_a, _o", "POc *q > ∅ / low vowels", notes="'Zero before low vowels (3a), probably after a glottal phase', with *qone 'sand' > on (p. 195).", **Q)
comp("nucl1483", "q", "k", "_u", "POc *q > k / high vowels", notes="Exception: *qate 'liver' > kayi- (p. 205, n. 7).", **Q)
comp("pwap1237", "q", "k", "elsewhere", "POc *q > k", **Q)
comp("have1241", "q", "ɣ", "elsewhere", "POc *q > γ", source_form="γ", **Q)
comp("cemu1238", "q", "∅", "elsewhere", "POc *q > ∅", **Q)
comp("nume1242", "q", "k", "elsewhere", "POc *q > k", page="195", locator="(4a)")
comp("nume1242", "k", "ɣ", "elsewhere", "POc *k > γ", page="195", locator="(4b)", source_form="γ", notes="'Weakened to a velar spirant /γ/' (p. 195).")
comp("nume1242", "k", "ŋ", "before a nasal vowel", "POc *k > ŋ", page="195", locator="(4b)", notes="'Which becomes a nasal before nasal vowels' (p. 195).")
D3 = dict(page="199", locator="Table 3")
comp("dumb1241", "p", "v", "elsewhere", "PNC *p > v", notes="Before oral and nasal vowels.", **D3)
comp("dumb1241", "mb", "p", "before an oral vowel", "PNC *mbV > pV", **D3)
comp("dumb1241", "mb", "m", "before a nasal vowel", "PNC *mbṼ > mV [mṼ]", **D3)
comp("dumb1241", "m", "mb", "before an oral vowel", "PNC *mV > mbV", notes="New prenasalised consonants by regressive oralisation of nasals (p. 199): *mate > mbe.", **D3)
comp("dumb1241", "m", "m", "before a nasal vowel", "PNC *mṼ > mV [mṼ]", **D3)
comp("xara1244", "mb", "m", "before a nasal vowel", "POc *mpoiri > m-", page="198", locator="(9)", notes="'Prenasalized consonants followed by nasal vowels tend to be simple nasal consonants' (p. 198).")
L5 = dict(page="197", locator="(5)-(6)")
comp("iaai1238", "p", "β", "elsewhere", "POc *p > β", notes="'POc *p has become a voiced spirant /β/ in Iaai' (p. 197).", **L5)
comp("dehu1237", "p", "∅", "elsewhere", "POc *p > ∅", **L5); comp("neng1238", "p", "∅", "elsewhere", "POc *p > ∅", **L5)
comp("dehu1237", "mb", "p", "elsewhere", "POc *mp [mb] > p", notes="Voiceless in Drehu; the asymmetry in the Loyalties is attributed to contact with English (p. 197).", **L5)
comp("iaai1238", "mb", "b", "elsewhere", "POc *mp [mb] > b", **L5)
comp("neng1238", "mb", "b", "elsewhere", "POc *mp [mb] > b (d)", **L5)
comp("neng1238", "mb", "d", "before a front vowel", "POc *mp [mb] > b (d)", notes="'/b/ (or /d/ before front vowels) in Nengone' (p. 197).", **L5)
comp("iaai1238", "t", "k", "elsewhere", "POc *t > k", page="204-205", locator="n. 5", notes="'*t generally becomes /k/ unless the original preceding or following consonant was velar or uvular' (n. 5); she notes two unexplained exceptions.")
comp("iaai1238", "t", "t̪", "next to a velar or uvular consonant", "POc *t > t̪", page="204-205", locator="n. 5", source_form="t̪", notes="*taku 'back' > (ho)t̪oo-n, *kutu > o-ut̪o (n. 5; (2), p. 193).")
comp("iaai1238", "ṭ", "ɭ", "#_; V_V", "POc *d > /l/", page="193", locator="(2)", source_form="l",
     notes="'In Iaai the earlier *d lenites to /l/ in initial and medial position' (p. 193); entered as the Iaai lateral of Lynch et al. (2002), whose inventory has no other (decision nc1992-lects).", decision="nc1992-lects")
comp("iaai1238", "ṭ", "ʈ", "_#", "POc *d > -ṭ", page="193", locator="(2)", source_form="ṭ", notes="Younger speakers are leniting final -ṭ towards -r (*matuduR > mokuṭ ~ mokur) (p. 193).")

DECISIONS = [
 dict(id="nc1992-orthography", batch="nc-ozannerivierre1992", status="open", source_id=S, page="192, 196, 202",
      question="Ozanne-Rivierre writes POc in Milke's spelling (*d, *mpw, *mp, *nt, *nd, *nj, *ŋk) and PNC with geminates (Table 4). How are her statements entered?",
      chosen_reading="Against Ross's POc in the database: her *d = Ross *r, *mpw *mp *nt *nd *nj *ŋk = Ross *bʷ *b *d *dr *j *ɡ (p. 196). PNC symbols as in Table 4, with ṭ and nḍ for the retroflexes, ʷ for her w, and ɡ for g; the eleven geminates are phonemes of the inventory, but their source (loss of a pretonic vowel between identical consonants) is not a segment correspondence and is in the notes. Ross's *pʷ and *kʷ are unentered; her PNC *pʷ comes from *p + *u (a fusion). PNC vowels are not discussed and are not entered.",
      alternatives="Keep her POc letters in parent_phoneme (they are not POc phonemes in the database)."),
 dict(id="nc1992-geraghty", batch="nc-ozannerivierre1992", status="open", source_id=G, page="141, 148-151",
      question="Geraghty's (1989) Proto-Southern Oceanic reconstructs the same node as Proto-New Caledonian (New Caledonia and the Loyalties). How is it entered?",
      chosen_reading="As rows on PNC citing Geraghty (1989) where he names a change from a POc phoneme: *ñ, *l > *n, *y > ∅, *R > ∅ with sporadic r before high vowels, *l > *r after *ka-, and intervocalic *k, *p > *x (disputed: Ozanne-Rivierre has no *x). His *z > *c (from Proto-Eastern Oceanic *z), aspirates from geminates, the prenasalisation of initial *r in two nouns, and his internal nodes (Proto-Loyalty, Proto-New Caledonia, Proto-North and Proto-South New Caledonia) are not entered.",
      alternatives="A competing lect for Geraghty's PSO; or a reconstruction system 'Geraghty' on PNC."),
 dict(id="nc1992-lects", batch="nc-ozannerivierre1992", status="open", source_id=S, page="194-205",
      question="New Caledonian lects in Ozanne-Rivierre (1992): codes and symbols.",
      chosen_reading="Gomen Yuanga = Glottolog Zuanga (thua1237) and Bondé Yuanga = Yuanga (juan1250), dialects of Zuanga-Yuanga; Kumak = Nixumwak (nucl1483), dialect of Nêlêmwa-Nixumwak; Nyelâyu = bala1316 (as in Ross et al. 2023). All rows are composed POc > PNC > language with her statement in as_printed. Table 2's t- for POc *d outside Gomen Yuanga is entered as t (the dentals and retroflexes merged); its y- for Pwaamei *k- and Haveke *q are read as γ = ɣ, the velar spirant of the text; Iaai /l/ < *d is entered as ɭ, the only lateral in the Iaai inventory of Lynch et al. (2002). No Loyalty, Mainland, Northern or Southern New Caledonian nodes.",
      alternatives="Other Glottocodes; enter t- as ʈ; Iaai l as a new phoneme."),
]
NOTATION = [dict(lect_id="pnc", phoneme="", system="canonical", symbol="", source_id=S, page="202",
                 notes="Spelling of Ozanne-Rivierre's Table 4, with ʷ for w, ɡ for g, and ṭ, nḍ for the retroflexes (decision nc1992-orthography).")]

def write(table, rows):
    cols = B.TABLES[table]; OUT.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO(); w = csv.writer(buf, lineterminator="\n"); w.writerow(cols)
    for r in rows: w.writerow([N(str(r.get(c_, ""))) for c_ in cols])
    (OUT / f"{table}.csv").write_text(buf.getvalue(), encoding="utf-8"); print(table, len(rows))
write("sources", SOURCES); write("lects", LECTS); write("phonemes", PHONEMES)
write("correspondences", CORR); write("notation_map", NOTATION); write("decisions", DECISIONS)
