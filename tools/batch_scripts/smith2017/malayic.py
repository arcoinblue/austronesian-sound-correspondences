"""Malayic of West Kalimantan (Smith 2017a, section 2.8, pp. 183-230)."""
from lib import Batch, Node
from common import add_language_rows, add_complements, ipa_respell, occurrences, decision, lect

S = "smith2017a"
NOTE50 = ("Unchanged: Smith's tables list only phonemes that changed somewhere in the subgroup (p. 50), and this "
          "one is not listed for this lect.")


def build(b: Batch):
    lect(b, "pmalayic", "Proto-Malayic", "proto-language", parent="pmp", glottocode="mala1538", clade="Malayic",
         alt_names="PMAL", inherit="assumed-unchanged",
         notes="Smith 2017a, section 2.8 (pp. 183-230), covers only Malayic languages of West Kalimantan and "
               "refers to earlier work for the definition of Malayic (p. 183); he gives no list of Proto-Malayic "
               "changes. The rows entered here are the reflexes that all seven lects of Tables 59-60 (p. 184) "
               "share, so they are inferred from his tables (decision pmal-shared). His lower groups (West Bornean "
               "Malayic, Kendayan-Salako, Ibanic; Figures 60 and 62, pp. 196-197) are defined by changes in "
               "particular lexemes only, so they are not entered as nodes.")
    L = "pmalayic"
    for par, ch, env, ap in (("q", "h", "_#", "*-q > h"), ("b", "p", "_#", "*-b > p"), ("d", "t", "_#", "*-d > t"),
                             ("j", "t", "_#", "*-j > t"), ("j", "d", "V_V", "*-j- > d"),
                             ("e", "a", "_C#", "*-əC > a")):
        b.corr(L, par, ch, env, S, 184, locator="Tables 59-60", as_printed=ap + " (all seven lects)",
               derivation="composed", decision="pmal-shared",
               notes="Shared by all seven lects of Tables 59-60; not stated by Smith as a Proto-Malayic change.")
    b.corr(L, "e", "ə", "elsewhere", S, 184, locator="Table 60", as_printed="*ə",
           notes="The source writes ə for the PMP vowel keyed e here.")
    b.decisions.append(decision("pmal-shared", "Proto-Malayic changes: Smith gives none.",
        "Entered at Proto-Malayic: the reflexes shared by all seven lects of Tables 59-60 (*-q > h, *-b > p, *-d, "
        "*-j > t, *-j- > d, *-əC > a), marked composed.", "no Proto-Malayic rows; every change on each lect", S,
        "184"))
    langs = [
        ("indo1316", "Indonesian", "indo1316", "ind", "Standard Indonesian", "Standard Malay as given in Smith's "
         "tables (Figure 55, p. 183)."),
        ("ketapang", "Ketapang Malay", "", "", "", "Interior of Ketapang Regency, West Kalimantan (p. 183). No "
         "Glottolog languoid by this name."),
        ("keni1248", "Keninjal", "keni1248", "knl", "", "Melawi Regency, West Kalimantan (p. 183)."),
        ("kend1254", "Kendayan", "kend1254", "knx", "Kendayan-Belangin", "Spoken in Pontianak, away from its "
         "traditional area; 'the data has several inconsistencies as a result' (p. 183 n. 18)."),
        ("sebe1242", "Seberuang", "sebe1242", "sbx", "", "Upper Kapuas River (p. 183)."),
        ("iban1264", "Iban (Upper Kapuas)", "iban1264", "iba", "Kapuas River Iban", "Dusun Sadap, Embaloh Hulu, "
         "Kapuas Hulu (p. 197 n. 22): 'distinct from the more widely reported Iban language of Sarawak' (p. 183). "
         "Glottolog's Iban, which covers both."),
        ("mual1241", "Mualang", "mual1241", "mtd", "", "Middle-upper Kapuas River (p. 183)."),
    ]
    for (i, name, gc, iso, alt, note) in langs:
        lect(b, i, name, "language", parent="pmalayic", glottocode=gc, iso639_3=iso, alt_names=alt,
             inherit="stated-unchanged", inherit_source_id=S, inherit_page="50", inherit_note=NOTE50,
             notes=note + " Author's fieldwork, except Indonesian.")
    nodes = {"pmalayic": Node("pmalayic", "pmp", {("q", "_#"): "h", ("b", "_#"): "p", ("d", "_#"): "t",
                                                  ("j", "_#"): "t", ("j", "V_V"): "d", ("e", "_C#"): "a",
                                                  ("e", "*"): "ə"})}
    chains = {"pmalayic": ["pmalayic"]}
    ML = [x[0] for x in langs]
    # Table 59 (p. 184). 'mp', 'nt', 'nd', 'ns', 'nj' after a semicolon: the obstruent with a nasal before it in
    # some words; entered as a sporadic inserted nasal below, not as a reflex of the obstruent.
    t59 = [("*-k", "k|k|k|k|k|ʔ|k; ʔ"), ("*q-", "Ø; h|h|Ø|Ø|Ø|Ø; h|Ø; h"), ("*-q-", "h|h|h; Ø|h; Ø|Ø|Ø|Ø"),
           ("*-b-", "b; w|b; w|b; w|b; (w)|b|b|b"), ("*-d-", "d|d|d; n|d; (r)|d|d; n|d; n"),
           ("*-d", "t|t|t|t|t|t|t"), ("*-z-", "j|j|j; ñ|j|j; ñ|j; ñ|j; ñ"),
           ("*s-", "s|s|s|s|s|s; t|s"), ("*-s", "s|s|s|s|h|h|s"), ("*l-", "l|l|l|l; (Ø)|l|l|l"),
           ("*-l-", "l|l|l|l; Ø|l|l|l"), ("*R-", "r|r|r|r|r|r|r"), ("*-R-", "r|r|r|r|r|r|r"),
           ("*-R", "r|r|r; ʔ|r; ʔ|r; ʔ|r; ʔ|r; ʔ")]
    add_language_rows(b, nodes, chains, ML, "pmalayic", t59, S, 184, "Table 59", many_ok=True)
    t60 = [("*-a", "a|o|aʔ; a|aʔ; a|aʔ; a|aʔ; a|aʔ; a"), ("*-aC", "a|a|a|a|a|a; æ|a"),
           ("*-aCVC", "a|a; o|a|a|a|a|a"), ("*-u", "u|u|u; (uʔ)|u; uʔ|u; (oʔ)|u; oʔ|u; (oʔ)"),
           ("*-uC", "u|o|u; o|u|u; o|u|o"), ("*-uCVC", "u|u|u|u; o|u|u|u"),
           ("*-i", "i|i|i; (iʔ)|i; iʔ|i; iʔ|i; eʔ|i; iʔ"), ("*-iC", "i|ɛ|i; (e)|i; (e)|i|i|e"),
           ("*-iCVC", "i|i|i|i; e|i|i|i"), ("*-əCVC", "ə|o|o|a|ə|ə|ə"),
           ("*-ay", "ay; i|ay; i|ay; i|ey; i|ay; ey|ay; i|ay; i"), ("*-aw", "aw|aw|aw|ow|aw|aw; oʔ|aw")]
    add_language_rows(b, nodes, chains, ML, "pmalayic", t60, S, 184, "Table 60", many_ok=True,
                      strip_final_glottal_note=True)
    for i in ("keni1248", "kend1254", "sebe1242", "iban1264", "mual1241"):
        b.corr(i, "∅", "ʔ", "V_#", S, 184, status="sporadic", locator="Table 60",
               as_printed="*-a > aʔ; a; *-u > u; (uʔ); *-i > i; (iʔ)",
               notes="A glottal stop after final vowels in some words: in Ibanic 'in a specific set of lexemes' "
                     "(Figure 60, p. 196). Table 60 prints aʔ first for *-a.", decision="malayic-glottal")
    for (i, *_rest) in langs:
        for o, n in (("p", "m"), ("t", "n")):
            b.corr(i, "∅", n, f"V_{o}", S, 184, status="sporadic", locator="Table 59",
                   as_printed=f"*-{o}- > {o}; {n}{o}", notes="A nasal before the medial obstruent in some words.")
    b.decisions.append(decision("malayic-glottal", "Malayic cells such as 'aʔ; a', 'u; (uʔ)', 'r; ʔ' (Tables "
        "59-60): Smith ties final glottal stops to particular lexemes (Figures 60-61, p. 196).",
        "The glottal stop after final vowels is entered as a sporadic inserted ʔ; the vowel itself as unchanged.",
        "aʔ as the regular reflex of *-a, as Table 60 lists it first", S, "184"))
    b.decisions.append(decision("malayic-phonetic", "Table 60 prints some vowels phonetically: Seberuang ow, ey; "
        "Iban ʊu̯, ɪi̯, ʊə̯, ɪə̯; Mualang oə̯, ɛə̯. The text calls these allophonic (pp. 185-186: /kutu/ [kutow], "
        "/taun/ [taʊə̯n], /kulet/ [kulɛə̯t]).", "Entered as the phonemes: u, i (Seberuang, Iban), o, e (Mualang "
        "closed syllables).", "the printed phonetic forms", S, "185"))
    b.decisions.append(decision("malayic-r", "Malayic *R: Tables 59 prints ɣ (Keninjal, Seberuang, Mualang) and "
        "ɹˠ (Seberuang, final), but Figure 56 (p. 185) gives these as phonetic values of /r/.",
        "Entered as r for all seven lects (phonemic).", "ɣ as printed", S, "185"))

    occ = {k: occurrences(nodes, v) for k, v in chains.items()}
    add_complements(b, ML, S, "50", "Not listed for this position: Smith's tables list only changes (2017a: 50).",
                    parents={L_: occ["pmalayic"] for L_ in ML})
    ipa_respell(b, ML, {L_: occ["pmalayic"] for L_ in ML}, S, "50")
    b.notation.append({"lect_id": "pmalayic", "phoneme": "", "system": "canonical", "symbol": "", "source_id": S,
                       "page": "184", "notes": "PMP orthography, schwa written ə."})
