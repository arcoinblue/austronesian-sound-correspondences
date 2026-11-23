"""Batch ho1982-hienghene: Haudricourt & Ozanne-Rivierre (1982), Pije, Fwâi, Nemi, Jawe.

Haudricourt, André-Georges & Françoise Ozanne-Rivierre. 1982. Dictionnaire thématique des langues de la
région de Hienghène (Nouvelle-Calédonie): pije, fwâi, nemi, jawe (LACITO-documents, Asie-Austronésie 4;
SELAF 212). Paris: SELAF. The introduction 'Langues de Hienghène et proto-océanien: phonologie comparée'
(pp. 9-59) is by Ozanne-Rivierre. Read from the excerpt in Downloads (macOS OCR text layer, unusable for
the tables; the inventories (pp. 17-23) and Table 3.3.4 (pp. 54-55) read from page images).

    python3 tools/batch_scripts/new_sources_2026_11_23/ho1982.py
"""
from common import write

S = "haudricourt1982"
BATCH = "ho1982-hienghene"
LANGS = {"P": "pije1237", "F": "fwai1237", "N": "nemi1240", "J": "jawe1237"}
NAMES = {"P": "Pije", "F": "Fwâi", "N": "Nemi", "J": "Jawe"}

SOURCES = [dict(
    id=S, author="Haudricourt, André-Georges; Ozanne-Rivierre, Françoise", year="1982",
    title="Dictionnaire thématique des langues de la région de Hienghène (Nouvelle-Calédonie): pije, fwâi, nemi, jawe",
    kind="dictionary", pub_type="book", place="Paris", publisher="SELAF",
    series="LACITO-documents, Asie-Austronésie 4; SELAF 212",
    notes="Consulted directly on 23 November 2026 (excerpt, pp. 1-61 of the Peeters reprint; tables read from page "
          "images, the OCR layer being unusable). The comparative introduction 'Langues de Hienghène et proto-océanien: "
          "phonologie comparée' (pp. 9-59) is by Ozanne-Rivierre: the four languages and their dialects (§1, pp. 9-16), "
          "their phoneme systems (§2, pp. 17-23), POc correspondences (§3.3, pp. 33-53) and the summary Table 3.3.4 "
          "(pp. 54-55). Data from fieldwork by Haudricourt in 1959 and by Ozanne-Rivierre in 1973, 1976 and 1978. POc is written in "
          "Grace's (1969) orthography with *d for the retroflex (Ross's *r), *nt, *nd, *mp, *ŋp, *ŋm, *ŋk (Ross's "
          "*d, *dr, *b, *bʷ, *mʷ, *ɡ), and *s and *ns interchanged with respect to Grace's lists (n. 57)."),
]

LECTS = [
    dict(id="pije1237", name="Pije", alt_names="Pijé", type="language", glottocode="pije1237", iso639_3="piz",
         parent_id="pnc", latitude="-20.78", longitude="164.94", region="Hienghène, New Caledonia",
         orthography_note="Practical orthography of Haudricourt & Ozanne-Rivierre (1982: 17): h before a consonant marks "
                          "aspiration (ph, hm, hl), b d j g bw are prenasalised, ny ng = ɲ ŋ, a circumflex marks a "
                          "nasal vowel, doubled vowels are long. IPA here.",
         notes="Northern New Caledonian, Hienghène region: Tiendanite, Ouenghip, Tiouandé (Haudricourt & Ozanne-Rivierre "
               "1982: 9-10). With Fwâi and Nemi it keeps old POc dentals before *a as apicals, which Jawe palatalises "
               "(§1.2); it has a thematic vowel a in possessed nouns where the others have e (§1.3); the old "
               "post-nasalised consonants appear as aspirates followed by nasal vowels (§1.4). Glottocode and "
               "coordinates from the language metadata of Ross et al. (2023)."),
    dict(id="fwai1237", name="Fwâi", alt_names="Fwai; Yalayu de Hienghène", type="language", glottocode="fwai1237",
         iso639_3="fwa", parent_id="pnc", latitude="-20.69", longitude="164.90", region="Hienghène, New Caledonia",
         orthography_note="As for Pije (Haudricourt & Ozanne-Rivierre 1982: 17-18). IPA here.",
         notes="Northern New Caledonian: lower Hienghène valley, Tanghène valley and the coast from Pindache to the mouth "
               "of the Ouaième; it is replacing Nemi in the villages north of that mouth (Haudricourt & Ozanne-Rivierre "
               "1982: 18). Oral stops and strong continuants occur only in loans (p. 18). Glottocode and coordinates from "
               "the language metadata of Ross et al. (2023)."),
    dict(id="jawe1237", name="Jawe", alt_names="Jawé", type="language", glottocode="jawe1237", iso639_3="jaz",
         parent_id="pnc", latitude="-20.66", longitude="164.68", region="Hienghène, New Caledonia",
         orthography_note="As for Pije; ch is written c before a nasal vowel; ü and ë are [y] and [œ] (Haudricourt & "
                          "Ozanne-Rivierre 1982: 21-23). IPA here.",
         notes="Northern New Caledonian: east coast from Colnett to Tchambouène, the Ouaième valley at Pangou, and the "
               "central chain at Ouayaguette (Wevia) and Ouahat. Two varieties: Yambé (Y), whose system is entered here, "
               "and Wevia (W), which keeps the post-nasalised consonants of Nemi 2, at least initially; in Yambé they "
               "became aspirated stops followed by nasal vowels (Haudricourt & Ozanne-Rivierre 1982: 21). Jawe "
               "palatalises old dentals before *a (§1.2). Glottocode and coordinates from the language metadata of Ross "
               "et al. (2023)."),
]

# ---------------------------------------------------------------- inventories (§2, pp. 17-23)
def C(ipa, place, manner, voicing, sym="", notes="", status=""):
    return dict(ipa=ipa, source_symbol=sym, cls="C", place=place, manner=manner, voicing=voicing, notes=notes, status=status)


def V(ipa, place, height, rounding, sym="", notes="", status=""):
    return dict(ipa=ipa, source_symbol=sym, cls="V", place=place, manner=height, rounding=rounding, notes=notes, status=status)


LV = "labial-velar"
ASP = "Aspirated nasal (written h + nasal)."
BASE = [  # Pije (p. 17)
    C("pʰʷ", "bilabial", "plosive", "voiceless", "phw"), C("pʷ", "bilabial", "plosive", "voiceless", "pw"),
    C("fʷ", "labiodental", "fricative", "voiceless", "fw"), C("ʍ", LV, "approximant", "voiceless", "hw", "Aspirated soft continuant."),
    C("w", LV, "approximant", "voiced"), C("ᵐbʷ", "bilabial", "prenasalized-plosive", "voiced", "bw"),
    C("m̥ʷ", "bilabial", "nasal", "voiceless", "hmw", ASP), C("mʷ", "bilabial", "nasal", "voiced", "mw"),
    C("pʰ", "bilabial", "plosive", "voiceless", "ph"), C("p", "bilabial", "plosive", "voiceless"),
    C("f", "labiodental", "fricative", "voiceless", "", "Strong continuant."),
    C("ɸ", "bilabial", "fricative", "voiceless", "vh", "Aspirated soft continuant, [ɸ]."),
    C("β", "bilabial", "fricative", "voiced", "v", "Soft continuant, [β]."),
    C("ᵐb", "bilabial", "prenasalized-plosive", "voiced", "b"), C("m̥", "bilabial", "nasal", "voiceless", "hm", ASP),
    C("m", "bilabial", "nasal", "voiced"),
    C("tʰ", "alveolar", "plosive", "voiceless", "th", "Apical (apico-alveolar)."), C("t", "alveolar", "plosive", "voiceless", "", "Apical."),
    C("r", "alveolar", "trill", "voiced", "", "Apical vibrant; very rare, intervocalic in a few recent loans (pwarawa 'bread', geree 'fat') (p. 17).", "marginal"),
    C("l̥", "alveolar", "lateral-approximant", "voiceless", "hl"), C("l", "alveolar", "lateral-approximant", "voiced"),
    C("ⁿd", "alveolar", "prenasalized-plosive", "voiced", "d"), C("n̥", "alveolar", "nasal", "voiceless", "hn", ASP),
    C("n", "alveolar", "nasal", "voiced"),
    C("c", "palatal", "plosive", "voiceless"), C("s", "alveolar", "fricative", "voiceless", "", "Listed with the palatals (strong continuant)."),
    C("j̊", "palatal", "approximant", "voiceless", "hy", "Aspirated soft continuant."), C("j", "palatal", "approximant", "voiced", "y"),
    C("ᶮɟ", "palatal", "prenasalized-plosive", "voiced", "j"), C("ɲ̊", "palatal", "nasal", "voiceless", "hny", "[hɲ]; " + ASP),
    C("ɲ", "palatal", "nasal", "voiced", "ny"),
    C("kʰ", "velar", "plosive", "voiceless", "kh", "Post-palatal."), C("k", "velar", "plosive", "voiceless", "", "Post-palatal."),
    C("x", "velar", "fricative", "voiceless", "xh", "Strong continuant, [x]."),
    C("h", "glottal", "fricative", "voiceless", "", "Aspirated soft continuant, in the post-palatal column."),
    C("ᵑɡ", "velar", "prenasalized-plosive", "voiced", "g"), C("ŋ", "velar", "nasal", "voiced", "ng"),
]
VOW = [V("i", "front", "close", "unrounded"), V("e", "front", "close-mid", "unrounded"), V("a", "central", "open", "unrounded"),
       V("o", "back", "close-mid", "rounded"), V("u", "back", "close", "rounded")]
NAS = [V(v + "̃", p, h, r, v + "̂") for v, p, h, r in
       (("i", "front", "close", "unrounded"), ("e", "front", "close-mid", "unrounded"), ("a", "central", "open", "unrounded"),
        ("o", "back", "close-mid", "rounded"), ("u", "back", "close", "rounded"))]
LONG = "Long vowels are written double (p. 18)."


def inv(code):
    out = []
    if code == "P":
        out = [dict(r) for r in BASE] + [dict(v) for v in VOW + NAS]
        page = "17-18"
    elif code == "F":
        page = "18"
        loans = {"pʷ", "p", "tʰ", "t", "c", "kʰ", "k", "fʷ", "f", "s"}
        for r in BASE:
            r = dict(r)
            if r["ipa"] in ("pʰʷ", "pʰ", "x"):
                continue  # not in the Fwâi table
            if r["ipa"] in loans:
                r["status"] = "marginal"
                r["notes"] = "In parentheses: very rare, in loans only (p. 18)."
            if r["ipa"] == "r":
                r.update(status="", notes="Apical vibrant.")
            out.append(r)
        out += [C("r̥", "alveolar", "trill", "voiceless", "rh", "Aspirated soft continuant."),
                C("ɣ", "velar", "fricative", "voiced", "x", "Soft continuant, [ɣ].")]
        out += [dict(v) for v in VOW + NAS]
    elif code == "N":
        page = "19-20"
        for r in BASE:
            r = dict(r)
            if r["ipa"] in ("fʷ", "ɸ"):
                continue
            if r["ipa"] == "β":
                r["notes"] = "Soft continuant (written v)."
            if r["ipa"] == "x":
                r["notes"] = "Strong continuant, [x]; Nemi 1 (Témala) only (p. 19)."
            if r["ipa"] == "r":
                r.update(status="", notes="Apical vibrant.")
            out.append(r)
        PN = "Post-nasalised stop (nasal release), kept in Nemi 1 (Témala) initially and intervocalically, in Nemi 2 (east coast) initially (pp. 19-20; §1.4)."
        out += [C("r̥", "alveolar", "trill", "voiceless", "rh", "Aspirated soft continuant."),
                C("ɣ", "velar", "fricative", "voiced", "x", "Soft continuant, [ɣ]."),
                C("pᵐʷ", "bilabial", "plosive", "voiceless", "pmw", PN), C("pᵐ", "bilabial", "plosive", "voiceless", "pm", PN),
                C("tⁿ", "alveolar", "plosive", "voiceless", "tn", PN), C("cᶮ", "palatal", "plosive", "voiceless", "cn", PN),
                C("kᵑ", "velar", "plosive", "voiceless", "kn", PN),
                C("ŋ̊", "velar", "nasal", "voiceless", "hng", "[hŋ]; Nemi 1 (Témala) only (p. 19).")]
        out += [dict(v) for v in VOW]
        out += [dict(v, status="marginal", notes="Nemi has only a few nasal vowels, after ∅, w, hw and h (p. 20).") for v in NAS]
    elif code == "J":
        page = "21-23"
        for r in BASE:
            r = dict(r)
            if r["ipa"] in ("fʷ", "ɸ", "x", "r"):
                continue
            out.append(r)
        out += [C("cʰ", "palatal", "plosive", "voiceless", "ch", "Always followed by a nasal vowel, written c + nasal vowel; "
                  "from an old post-nasalised cn (p. 22)."),
                C("ɣ", "velar", "fricative", "voiced", "x", "Soft continuant, [ɣ]."),
                C("r", "alveolar", "trill", "voiced", "", "Intervocalic only (p. 22).")]
        out += [dict(v) for v in VOW + NAS]
        out += [V("y", "front", "close", "rounded", "ü", "In a few words; old variants of u before v, phonemic now (uvi 'buy' : üi 'blow') (p. 23)."),
                V("œ", "front", "open-mid", "rounded", "ë", "In a few words; an old variant of o before v (yœa 'crawl' : hoa 'watch') (p. 23).")]
    rows = []
    for r in out:
        notes = r["notes"]
        if r["cls"] == "V" and r["ipa"] in "ieaou":
            notes = (notes + " " + LONG).strip()
        rows.append(dict(lect_id=LANGS[code], ipa=r["ipa"], source_symbol=r["source_symbol"], **{"class": r["cls"]},
                         place=r["place"], manner=r["manner"], voicing=r.get("voicing", ""), rounding=r.get("rounding", ""),
                         origin="sourced", source_id=S, page=page, notes=notes, status=r["status"]))
    return rows


phon = []
for k in "PFNJ":
    phon += inv(k)

# ---------------------------------------------------------------- correspondences (Table 3.3.4, pp. 54-55)
# Composed through PNC (Ozanne-Rivierre 1992): the parent phoneme is the PNC phoneme that continues the POc one.
rows = []
n = 0
PNC = {"q": "q", "k": "k", "ɡ": "ŋɡ", "r": "ṭ", "dr": "nḍ", "t": "t", "d": "nd", "l": "n", "p": "p", "b": "mb",
       "bʷ": "mbʷ", "w": "w", "ŋ": "ŋ", "ñ": "n", "n": "n", "m": "m", "mʷ": "mʷ"}
HER = {"r": "d", "dr": "nd", "d": "nt", "b": "mp", "bʷ": "ŋp", "mʷ": "ŋm", "ɡ": "ŋk", "ñ": "ɲ"}
ENV = {"I": "#_", "Mf": "V_V, now word-final", "Mm": "V_V", "F": "_#"}
DEC_COMP = "ho1982-composition"
FWAI_LOANS = {"pʷ", "p", "tʰ", "t", "c", "kʰ", "k", "fʷ", "f", "s"}


def c(poc, child, env, langs="PFNJ", printed="", status="regular", alt=False, notes="", lexical="", page="54",
      decision=DEC_COMP, sf=""):
    global n
    for k in langs:
        if k == "F" and child in FWAI_LOANS and env not in ("Mf", "F"):
            continue  # Fwâi oral stops and strong continuants occur only in loans (p. 18; §1.6)
        n += 1
        parent = PNC.get(poc, poc)
        e = ENV.get(env, env)
        rows.append(dict(id=f"ho82-{LANGS[k][:4]}-{n}", child_lect_id=LANGS[k], parent_phoneme=parent, child_phoneme=child,
                         environment=e, status=status, source_id=S, page=page, locator="Table 3.3.4",
                         derivation="composed", as_printed=printed, source_form=sf,
                         conditioning="lexical" if lexical else ("unknown" if alt else ""), lexical_scope=lexical,
                         notes=" ".join(x for x in (notes, "One of the reflexes listed for this position; the conditions are in §3.3 (pp. 33-53)." if alt else "") if x),
                         decision=decision))


def P(poc, s):
    return f"POc *{HER.get(poc, poc)}{s}"


# uvular *q (PNC *q)
c("q", "k", "I", printed=P("q", "- > k-"))
c("q", "k", "Mf", printed=P("q", "- > -k, -∅- (P, F), -k, -∅-, (-ɣ-) (N, J)"))
c("q", "∅", "Mm", printed=P("q", "- > -k, -∅- (P, F), -k, -∅-, (-ɣ-) (N, J)"))
c("q", "ɣ", "Mm", langs="NJ", status="sporadic", printed=P("q", "- > -k, -∅-, (-ɣ-) (N, J)"),
  notes="In parentheses; cf. POc (20) *puqu(n) (n. 55).")
c("q", "k", "F", alt=True, printed=P("-q", " > -k, -∅"))
c("q", "∅", "F", alt=True, printed=P("-q", " > -k, -∅"), notes="On the loss of these final consonants see §3.3.5.2 (n. 56).")
# velars
c("k", "c", "I", printed=P("k", "- > c-"))
c("k", "k", "Mf", printed=P("-k", "- > -k, -∅-"))
c("k", "∅", "Mm", printed=P("-k", "- > -k, -∅-"))
c("k", "k", "F", printed=P("-k", " > -k"))
c("ɡ", "ŋ", "Mf", printed=P("-ŋk", "- > -ŋ"), notes="Blust's and Grace's *ŋk (Ross's *ɡ).")
# retroflex *d (Ross *r, PNC *ṭ), *nd (Ross *dr, PNC *nḍ)
c("r", "t", "I", printed=P("r", "- > t-"))
c("r", "t", "Mf", printed=P("-d", "- > -t, -l-"), notes="Her retroflex *d is Ross's *r.")
c("r", "l", "Mm", printed=P("-d", "- > -t, -l-"))
c("r", "t", "F", printed=P("-d", " > -t"))
c("dr", "ⁿd", "I", printed=P("nd", "- > ⁿd-"), sf="d")
# dentals *t, *nt (Ross *d), *l
c("t", "t", "#_a", langs="PFN", alt=True, printed=P("t", "(a) > t(a), ⁿd(a) (P, F, N), c(a), ⁿj(a) (J)"))
c("t", "ⁿd", "#_a", langs="PFN", alt=True, printed=P("t", "(a) > t(a), ⁿd(a) (P, F, N), c(a), ⁿj(a) (J)"), sf="d",
  notes="Table 3.3.4 also lists *t(a) / *nt(a) > ⁿd(a) (P, F, N), ⁿj(a) (J).")
c("t", "c", "#_a", langs="J", alt=True, printed=P("t", "(a) > c(a), ⁿj(a) (J)"),
  notes="Jawe palatalises the old dentals before *a (§1.2).")
c("t", "ᶮɟ", "#_a", langs="J", alt=True, printed=P("t", "(a) > c(a), ⁿj(a) (J)"), sf="j")
c("t", "c", "#_i, #_u, #_o", printed=P("t", "(i,u,o) > c(i,e), ⁿj(i,e)"), alt=True,
  notes="The following *u, *o appear as i, e.")
c("t", "ᶮɟ", "#_u, #_o", printed=P("t", "(u,o) / *nt(u,o) > ⁿj(i,e)"), alt=True, sf="j")
c("t", "c", "Mf", printed=P("-t", "- > -c, -∅- (P, F), -c, -∅-, -y- (N, J)"))
c("t", "∅", "Mm", printed=P("-t", "- > -c, -∅- (P, F), -c, -∅-, -y- (N, J)"), alt=True)
c("t", "j", "Mm", langs="NJ", printed=P("-t", "- > -c, -∅-, -y- (N, J)"), alt=True, sf="y",
  notes="Footnote 58 cites POc (108) *mata, (109) *ŋmata, (110) *natu, (111) *patu.")
c("t", "c", "F", printed=P("-t", " > -c"))
c("d", "ⁿd", "#_a", langs="PFN", printed=P("nt", "(a) > ⁿd(a) (P, F, N), ⁿj(a) (J)"), sf="d", notes="Her *nt is Ross's *d (PNC *nd).")
c("d", "ᶮɟ", "#_a", langs="J", printed=P("nt", "(a) > ⁿj(a) (J)"), sf="j")
c("d", "ᶮɟ", "#_u, #_o", printed=P("nt", "(u,o) > ⁿj(i,e)"), sf="j")
c("d", "ⁿd", "V_a", langs="PFN", printed=P("-nt", "(a) > -ⁿd(a) (P, F, N), ⁿj(a) (J)"), sf="d")
c("d", "ᶮɟ", "V_a", langs="J", printed=P("-nt", "(a) > ⁿj(a) (J)"), sf="j")
c("d", "ᶮɟ", "V_i", printed=P("-nt", "(i) > -ⁿj(i)"), sf="j")
LS = "PNC *n from POc *l"
c("l", "n", "I", printed=P("l", "- > n-"), lexical=LS, notes="POc *l merged with *n in PNC (Ozanne-Rivierre 1992), but it has its own medial reflexes here.")
c("l", "n", "Mf", printed=P("-l", "- > -n, -∅-"), lexical=LS)
c("l", "∅", "Mm", printed=P("-l", "- > -n, -∅-"), lexical=LS)
# labials
c("p", "p", "I", alt=True, printed=P("p", "- > p-, pw-"))
c("p", "pʷ", "I", alt=True, printed=P("p", "- > p-, pw-"), sf="pw")
c("p", "p", "Mf", printed=P("-p", "- > -p, -v-, -∅-"))
c("p", "β", "Mm", alt=True, printed=P("-p", "- > -p, -v-, -∅-"), sf="v")
c("p", "∅", "Mm", alt=True, printed=P("-p", "- > -p, -v-, -∅-"))
c("p", "p", "F", printed=P("-p", " > -p"))
c("b", "ᵐb", "I", alt=True, printed=P("mp", "- > ᵐb-, ᵐbw-, ⁿg-"), sf="b")
c("b", "ᵐbʷ", "I", alt=True, printed=P("mp", "- > ᵐb-, ᵐbw-, ⁿg-"), sf="bw")
c("b", "ᵑɡ", "I", alt=True, printed=P("mp", "- > ᵐb-, ᵐbw-, ⁿg-"), sf="g",
  notes="The labials became velars before rounded vowels (pp. 42-45).")
c("bʷ", "ᵑɡ", "I", printed=P("ŋp", "- > ⁿg-"), sf="g")
c("b", "ᵐb", "Mm", alt=True, printed=P("-mp", "- > -ᵐb-, -ⁿg-"), sf="b")
c("b", "ᵑɡ", "Mm", alt=True, printed=P("-mp", "- > -ᵐb-, -ⁿg-"), sf="g")
c("w", "w", "I", printed=P("w", "- > w-"))
# nasals
c("ŋ", "n", "Mf", printed=P("-ŋ", "- > -n, -n-"))
c("ŋ", "n", "Mm", printed=P("-ŋ", "- > -n, -n-"))
c("ŋ", "∅", "F", printed=P("-ŋ", " > ∅"), notes="On the loss of these final consonants see §3.3.5.2 (n. 56).")
c("ñ", "n", "I", printed=P("ñ", "- > n-"), lexical="PNC *n from POc *ñ")
c("ñ", "n", "Mf", printed=P("-ñ", "- > -n"), lexical="PNC *n from POc *ñ")
c("n", "n", "I", printed=P("n", "- > n-"), lexical="PNC *n from POc *n")
c("n", "n", "Mf", printed=P("-n", "- > -n, -n-"), lexical="PNC *n from POc *n")
c("n", "n", "Mm", printed=P("-n", "- > -n, -n-"), lexical="PNC *n from POc *n")
c("n", "∅", "F", printed=P("-n", " > ∅"), lexical="PNC *n from POc *n", notes="See §3.3.5.2 (n. 56).")
c("m", "m", "I", printed=P("m", "- > m-"))
c("mʷ", "m", "I", printed=P("ŋm", "- > m-"))
c("m", "m", "Mf", printed=P("-m", "- > -m, -m-, -mw-, (-)ŋ-"))
c("m", "m", "Mm", alt=True, printed=P("-m", "- > -m, -m-, -mw-, (-)ŋ-"))
c("m", "mʷ", "Mm", alt=True, printed=P("-m", "- > -m, -m-, -mw-, (-)ŋ-"), sf="mw")
c("m", "ŋ", "Mm", status="sporadic", printed=P("-m", "- > -m, -m-, -mw-, (-)ŋ-"), notes="In parentheses in the table.")
c("m", "m", "F", printed=P("-m", " > -m"))
DECISIONS = [
    dict(id=DEC_COMP, question="Ozanne-Rivierre's Table 3.3.4 (Haudricourt & Ozanne-Rivierre 1982: 54-55) gives POc > "
         "'langues de Hienghène' for all four languages at once, naming a language only where they differ. How is it entered?",
         chosen_reading="One row per language (Pije, Fwâi, Nemi, Jawe), composed POc > PNC > language with the printed cell in "
                        "as_printed; a cell without a language label applies to all four, except that Fwâi gets no row whose reflex is an oral stop or strong continuant other than word-finally, since these occur in Fwâi only in loans (p. 18) and Fwâi turns intervocalic stops into continuants or zero (§1.6, p. 14). Her notation -x (now final) and -x- "
                        "(still intervocalic) for a medial POc consonant becomes the environments 'V_V, now word-final' and "
                        "'V_V'; several reflexes in one position are entered with conditioning unknown (the conditions are "
                        "discussed in §3.3, not tabulated). Her POc letters are mapped to Ross's (*d = r, *nd = dr, *nt = d, "
                        "*mp = b, *ŋp = bʷ, *ŋm = mʷ, *ŋk = ɡ). POc *l and *ñ, merged with *n in PNC, keep their own rows with "
                        "conditioning 'lexical'. *R > ∅ in all positions is not entered (PNC has already lost *R), nor are the vowels of "
                        "Table 3.3.4 B (*a > a, e; *e > e, Pije also a; *i > i; *o > e, (o); *u > u, i; *ai > e; *au > o; p. 55), "
                        "since PNC has no vowels in the database (Ozanne-Rivierre 1992 does not discuss them). The "
                        "palatal rows ((*s-), (*-s-) and *-j-, (*ns-), (*-ns-)) are not entered: by n. 57 her (*s) is Grace's "
                        "*ns and her (*ns) Grace's *s, and her *-j- (Ross's *c) is grouped with (*-s-), which does not fit "
                        "Ozanne-Rivierre's (1992) PNC merger of *c with *s.",
         alternatives="Enter the palatal rows after deciding which Ross phonemes (*s, *j, *c) her (*s), (*ns) and *j are; add "
                      "Hienghène nodes; read §3.3 to give each alternative its condition.",
         status="open", source_id=S, page="34-55"),
]

MD = f"""# {BATCH}

Haudricourt, André-Georges & Françoise Ozanne-Rivierre. 1982. *Dictionnaire thématique des langues de la région de Hienghène (Nouvelle-Calédonie): pije, fwâi, nemi, jawe* (LACITO-documents, Asie-Austronésie 4; SELAF 212). Paris: SELAF. Read from the excerpt (pp. 1-61) the user put in Downloads on 23 November 2026; the OCR layer scrambles the rotated tables, so the inventories (pp. 17-23) and Table 3.3.4 (pp. 54-55) were read from page images. Generator: `tools/batch_scripts/new_sources_2026_11_23/ho1982.py`.

## Scope

- New lects **Pije** (`pije1237`), **Fwâi** (`fwai1237`), **Jawe** (`jawe1237`) under PNC; Nemi (`nemi1240`) already existed.
- Sourced inventories of all four (§2): consonants with the aspirated, prenasalised and (Nemi) post-nasalised series, oral and nasal vowels; Fwâi loan consonants and Nemi nasal vowels as marginal; Jawe ü, ë as y, œ.
- Table 3.3.4 A (consonants): POc > each language, composed through PNC (decision `{DEC_COMP}`).

## Decisions (open)

- `{DEC_COMP}`.

## Not entered

- The palatal rows of Table 3.3.4, *R and the vowels of Table 3.3.4 B (see `{DEC_COMP}`); the detailed discussion of §3.3 (conditions of each alternative), the dialect differences of §1 (Nemi 1 vs 2, Jawe Yambé vs Wevia) beyond notes, the canonical forms (§3.3.5), the reduced final and intervocalic systems (pp. 17-22), and the dictionary.
"""

write(BATCH, dict(sources=SOURCES, lects=LECTS, phonemes=phon, correspondences=rows, decisions=DECISIONS), MD)
