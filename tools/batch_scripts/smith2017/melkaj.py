"""Kajang and Melanau (Smith 2017a, section 2.3, pp. 92-111)."""
from lib import Batch, Node, compose, label
from common import (add_language_rows, add_complements, ipa_respell, occurrences, decision, lect)

S = "smith2017a"


def build(b: Batch):
    lect(b, "pkajang", "Proto-Kajang", "proto-language", parent="pmp", glottocode="kaja1255", clade="Kajang",
         alt_names="PKAJ", inherit="assumed-unchanged",
         notes="Sekapan, Kejaman and Lahanan (Smith 2017a: 93-99; Figure 23, p. 97). The fricative *ɮ from *l in "
               "the onset of the final syllable is 'unique in all of Borneo' (p. 95). The internal subgrouping is "
               "unresolved (pp. 96-97). Smith finds no evidence for a Melanau-Kajang node (pp. 106-111, Figure 26), "
               "so Kajang and Melanau are entered separately under PMP. Figure 23 also has *CC > *ʔC (clusters from "
               "the loss of a middle vowel in three-syllable words, p. 96), not entered as a row. Glottolog's Kajang "
               "(kaja1255) has the same members.")
    lect(b, "pmelanau", "Proto-Melanau", "proto-language", parent="pmp", glottocode="mela1255", clade="Melanau",
         alt_names="PMEL", inherit="assumed-unchanged",
         notes="Kanowit, Dalat, Mukah, Balingian, Sarikei and Matu (Smith 2017a: 99-106), a dialect network. "
               "'There is no strong phonological evidence for a Melanau group'; the evidence is mainly lexical "
               "(p. 103). Smith thinks it 'likely' that final high vowels had become *əw and *əy in Proto-Melanau "
               "(p. 103); nothing else is assigned to it. Glottolog's Melanau (mela1255) has the same members.")
    L = "pkajang"
    rows = [
        ("b", "v", "V_V", 97, "*b > *v; b", "fig. 23", "Medial *b (Table 24: *-b- > v)."),
        ("b", "b", "ə_", 99, "*-b- > v; b / ə_", "Table 24", "Consonants were geminated after schwa, which kept "
         "*-əb- from weakening (p. 99)."),
        ("l", "ɮ", "_VC#", 97, "*l > *ɮ / _VC#", "fig. 23", "In the onset of the final syllable; an allophone of l "
         "in the modern languages (p. 95)."),
        ("w", "gʷ", "V_V", 97, "*-w- > *gʷ", "fig. 23", "Phonetic transition glides strengthened too (p. 95)."),
        ("y", "ʑ", "V_V", 97, "*-y- > *ʑ", "fig. 23", "Phonetic transition glides strengthened too (p. 95)."),
        ("u", "gʷ", "_a", 95, "*-uCVC > gʷ / _a", "Table 25", "Penultimate *u before *a in hiatus: the transition "
         "glide was strengthened (*dua > Sekapan dəgʷa, p. 96)."),
        ("i", "ʑ", "_a", 95, "*-iCVC > ʑ / _a", "Table 25", "Penultimate *i before *a in hiatus (p. 95)."),
        ("u", "əw", "_#", 97, "*-u > *əw", "fig. 23", ""),
        ("i", "əy", "_#", 97, "*-i > *əy", "fig. 23", ""),
        ("u", "uə̯", "_[k,ŋ]#", 97, "*-uŋ > *uə̯ŋ, *-uk > *uə̯k", "fig. 23", ""),
        ("i", "iə̯", "_[k,ŋ]#", 97, "*-iŋ > *iə̯ŋ, *-ik > *iə̯k", "fig. 23", ""),
        ("e", "ə", "elsewhere", 97, "*ə", "fig. 23", "The source writes ə for the PMP vowel keyed e here."),
    ]
    for par, ch, env, page, ap, loc, note in rows:
        b.corr(L, par, ch, env, S, page, as_printed=ap, locator=loc, notes=note)
    b.corr(L, "e", "a", "_[h,q]#", S, 97, as_printed="*-əh > *-ah; *-əʔ > *-aʔ", locator="fig. 23",
           notes="Schwa raised before final glottalics (p. 95). PMP *q is ʔ in all three languages (Table 24).")
    L = "pmelanau"
    b.corr(L, "u", "əw", "_#", S, 103, as_printed="word-final high vowels had become *əw and *əy in Proto-Melanau",
           notes="Smith: 'It is likely' (p. 103). All six lects of Table 27 have əw.")
    b.corr(L, "i", "əy", "_#", S, 103, as_printed="word-final high vowels had become *əw and *əy in Proto-Melanau",
           notes="Smith: 'It is likely' (p. 103). All six lects of Table 27 have əy.")
    b.corr(L, "e", "ə", "elsewhere", S, 101, as_printed="*ə", locator="Table 27",
           notes="The source writes ə for the PMP vowel keyed e here.")

    langs = [
        ("seka1248", "Sekapan", "pkajang", "seka1248", "skp", "", "Upper Rejang River, just below the Bakun dam "
         "(Smith 2017a: 93); author's fieldwork."),
        ("kaja1250", "Kejaman", "pkajang", "kaja1250", "", "Kajaman", "Upper Rejang River, just below the Bakun "
         "dam (Smith 2017a: 93); author's fieldwork."),
        ("laha1253", "Lahanan", "pkajang", "laha1253", "lhn", "", "Upper Rejang River, below the Bakun dam and "
         "Sungai Asap (Smith 2017a: 93); author's fieldwork."),
        ("kano1244", "Kanowit", "pmelanau", "kano1244", "kxn", "Kanowit-Tanjong Melanau", "Near Kanowit town "
         "(Smith 2017a: 93); author's fieldwork. Mutually intelligible with Tanjung (p. 99)."),
        ("dala1239", "Dalat Melanau", "pmelanau", "dala1239", "", "Dalat", "South of Mukah (Smith 2017a: 93); "
         "author's fieldwork."),
        ("muka1237", "Mukah Melanau", "pmelanau", "muka1237", "", "Mukah;Mukah-Oya", "Mukah town (Smith 2017a: "
         "93). Data from an unpublished Blust wordlist, as given in the source."),
        ("bali1282", "Balingian Melanau", "pmelanau", "bali1282", "", "Balingian", "Balingian town (Smith 2017a: "
         "93). Data from an unpublished Blust wordlist, as given in the source. *-b- > v and *-d- > r are put "
         "down to Bintulu influence (p. 102)."),
        ("sari1247", "Sarikei Melanau", "pmelanau", "sari1247", "", "Sarikei", "Near Sarikei town (Smith 2017a: "
         "93). Data from an unpublished Blust wordlist, as given in the source."),
        ("matu1262", "Matu Melanau", "pmelanau", "matu1262", "", "Matu", "Around the Rejang River delta (Smith "
         "2017a: 93). Data from an unpublished Blust wordlist, as given in the source."),
    ]
    for (i, name, par, gc, iso, alt, note) in langs:
        lect(b, i, name, "dialect" if i in ("dala1239", "muka1237", "bali1282", "sari1247", "matu1262") else
             "language", parent=par, glottocode=gc, iso639_3=iso, alt_names=alt,
             inherit="stated-unchanged", inherit_source_id=S, inherit_page="50",
             inherit_note="Unchanged: Smith's tables list only phonemes that changed somewhere in the subgroup "
                          "(p. 50), and this one is not listed for this lect.",
             notes=note)

    nodes = {
        "pkajang": Node("pkajang", "pmp", {("b", "V_V"): "v", ("w", "V_V"): "gʷ", ("y", "V_V"): "ʑ",
                                           ("u", "_#"): "əw", ("i", "_#"): "əy", ("e", "*"): "ə"}),
        "pmelanau": Node("pmelanau", "pmp", {("u", "_#"): "əw", ("i", "_#"): "əy", ("e", "*"): "ə"}),
    }
    chains = {"pkajang": ["pkajang"], "pmelanau": ["pmelanau"]}
    pc_kaj = {("b", "ə_"): "b", ("u", "_[k,ŋ]#"): "uə̯", ("i", "_[k,ŋ]#"): "iə̯", ("ə", "_[h,ʔ]#"): "a"}

    K = ["seka1248", "kaja1250", "laha1253"]
    # Table 24 (p. 94). *-b- "v; b / ə_" is Proto-Kajang; *-l- is Proto-Kajang (ɮ an allophone).
    t24 = [("*-k", "ʔ|k|k"), ("*q-", "Ø|Ø|Ø"), ("*-q-", "ʔ|ʔ|ʔ"), ("*-q", "ʔ|ʔ|ʔ"), ("*-b", "p|p|p"),
           ("*-d-", "r|r|r"), ("*-d", "t|t|t"), ("*-j-", "r|r|r"), ("*-j", "t|t|t"), ("*-ŋ", "Ø|ŋ|ŋ"),
           ("*-l", "n|n|n"), ("*-s-", "c|c|s"), ("*-s", "Ø; h|Ø; h|Ø; h"), ("*R-", "Ø|Ø|Ø"), ("*-R-", "Ø|Ø|Ø"),
           ("*-R", "Ø; h; y|Ø; h; y|Ø; h; y"), ("*-w-", "gʷ|gʷ; ŋʷ / NV_|gʷ; ŋ / NV_"),
           ("*-y-", "ʑ|ʑ; ñ / NV_|ʑ; ñ / NV_")]
    add_language_rows(b, nodes, chains, K, "pkajang", t24, S, 94, "Table 24", proto_cond=pc_kaj)
    # Table 25 (p. 95), read from the page image.
    t25 = [("*-a", "a|ah|ah"), ("*-aC", "a; eə̯ / _k,ŋ|a; eə̯ / _k,ŋ|a"),
           ("*-uC", "u; uə̯ / _k,ŋ; əw / _q|u; uə̯ / _k,ŋ; əw / _q|u; uə̯ / _k,ŋ"),
           ("*-uCVC", "u; o|u; o|u"), ("*-iC", "i; iə̯ / _k,ŋ; əy / _q|i; iə̯ / _k,ŋ; əy / _q|i; iə̯ / _k,ŋ"),
           ("*-iCVC", "i; e|i; e|i; e"), ("*-əC", "ə; a / _h,ʔ|ə; a / _h,ʔ|ə; a / _h,ʔ"),
           ("*-əCVC", "ə; Ø / #_|ə; Ø / #_|ə; Ø / #_")]
    add_language_rows(b, nodes, chains, K, "pkajang", t25, S, 95, "Table 25", proto_cond=pc_kaj, many_ok=True,
                      conditioned={})
    for L_ in ("kaja1250",):
        b.corr(L_, "gʷ", "ŋʷ", "N_a", S, 95, locator="Table 25", as_printed="*-uCVC > ŋʷ / N_a",
               notes="Progressive nasalization of the strengthened glide after a nasal onset (p. 96): *kami dua > "
                     "*mua > məŋʷa.")
        b.corr(L_, "ʑ", "ɲ", "N_a", S, 95, locator="Table 25", as_printed="*-iCVC > ñ / N_a",
               notes="Progressive nasalization (p. 96).")
    b.corr("laha1253", "gʷ", "ŋ", "N_a", S, 95, locator="Table 25", as_printed="*-uCVC > ŋ / N_a",
           notes="Progressive nasalization (p. 96): *mua > məŋa.")
    b.corr("laha1253", "ʑ", "ɲ", "N_a", S, 95, locator="Table 25", as_printed="*-iCVC > ñ / N_a",
           notes="Progressive nasalization (p. 96).")
    for L_ in ("kaja1250", "laha1253"):
        b.corr(L_, "∅", "h", "a_#", S, 95, locator="Table 25", as_printed="*-a > ah",
               notes="'the closing of word-final *-a with h in Kejaman and Lahanan but not Sekapan' (p. 96).")
    b.decisions.append(decision("kajang-hiatus", "Kajang reflexes of penultimate *u and *i before *a (Table 25: "
        "*-uCVC gʷ / _a; *-iCVC ʑ / _a).", "Entered at Proto-Kajang as *u > *gʷ, *i > *ʑ before *a: the "
        "strengthened transition glide (p. 95: *dua > dəgʷa).", "an inserted glide after the vowel", S, "95"))

    M = ["kano1244", "dala1239", "muka1237", "bali1282", "sari1247", "matu1262"]
    t26 = [("*-k", "k|ʔ; k|ʔ; k|k|k; ʔ / u,i_|k"), ("*-b-", "b|b|b|v|b|b"), ("*-b", "p|b|b|b|p; b|b"),
           ("*-d-", "d|d|d|r|d|d"), ("*-d", "t|d|d|d|t; d|d"), ("*-j-", "d|d|d|r|d|d"), ("*-j", "t|d|d|d|t; d|d"),
           ("*-ŋ", "ŋ|Ø; ŋ / ə_|ŋ|ŋ|ŋ|ŋ"), ("*-l", "n|n|n|n|l|l"), ("*-s", "h|h|h|h|s|s"),
           ("*R-", "Ø|Ø|Ø|Ø|Ø|"), ("*-R-", "r; (h); (y); (Ø)|h; y|Ø|h|ɣ; (y)|ɣ"), ("*-R", "y; h|h; y|h|h; y|y|h; y")]
    add_language_rows(b, nodes, chains, M, "pmelanau", t26, S, 100, "Table 26", many_ok=True)
    for L_ in ("kano1244", "dala1239", "muka1237"):
        b.corr(L_, "∅", "j", "V_s#", S, 101, locator="Table 26", as_printed="*-s > yh",
               notes="'word-final *-s to be reflected as *-yh, that is, with a palatalizing effect on the preceding "
                     "vowel, before *s is eventually reduced to h' (p. 101).")
    t27 = [("*-a", "a; (ah)|a; (ah)|a|a|əh|əh"),
           ("*-aC", "a|a; i / _k,ŋ|a; eə̯ / _k,ŋ|a|a; ə / _ʔ|a; ə / _ʔ"),
           ("*-aCVC", "a|a|a|a|a|a"),
           ("*-u", "əw|əw|əw|əw|əw; (aw)|əw"),
           ("*-uC", "u; uə̯ / _k,ŋ; o / _ʔ,h|u; o / _k|u; uə̯ / _k,ŋ; o / _ʔ,h|u; o / _h|u; uə̯ / _k,ŋ,ʔ,h|"
                    "u; uə̯ / _k,ŋ; o / _h"),
           ("*-i", "əy|əy|əy|əy|əy; (ay)|əy"),
           ("*-iC", "i; iə̯ / _k,ŋ|i; e / _ʔ|i; iə̯ / _k,ŋ; e / _ʔ,h|i; iə̯ / _k,ŋ|i; iə̯ / _k,ŋ,h,ʔ|i; eə̯ / _k,ŋ"),
           ("*-əC", "ə; e / _s|ə; ey / _s; a / _ʔ|ə; ay / _s; a / _ʔ,h|ə; a|ə; a|"),
           ("*-əCVC", "ə; Ø / #_|ə; Ø / #_|ə; Ø / #_|ə; Ø / #_|ə; Ø / #_|ə; Ø / #_")]
    add_language_rows(b, nodes, chains, M, "pmelanau", t27, S, 101, "Table 27", many_ok=True)
    # Kanowit vowel harmony across ʔ (Table 27): two rows, not the comma pair the parser would make.
    b.corr("kano1244", "a", "i", "penultimate syllable _ʔi", S, 101, locator="Table 27",
           as_printed="*-aCVC > a; i,u / _ʔi,ʔu", notes="Penultimate *a took the final vowel's quality across ʔ.")
    b.corr("kano1244", "a", "u", "penultimate syllable _ʔu", S, 101, locator="Table 27",
           as_printed="*-aCVC > a; i,u / _ʔi,ʔu", notes="Penultimate *a took the final vowel's quality across ʔ.")
    b.decisions.append(decision("melanau-node", "Is Proto-Melanau a node?",
        "Entered, with only *-u > *əw and *-i > *əy, which Smith thinks 'likely' (p. 103). He calls Melanau a "
        "dialect network with mainly lexical evidence.", "no node: the Melanau lects directly under PMP", S, "103"))

    occ = {k: occurrences(nodes, v) for k, v in chains.items()}
    par_of = {r["id"]: r["parent_id"] for r in b.lects}
    members = K + M
    add_complements(b, members, S, "50", "Not listed for this position: Smith's tables list only changes "
                    "(2017a: 50).", parents={L_: occ[par_of[L_]] for L_ in members})
    ipa_respell(b, members, {L_: occ[par_of[L_]] for L_ in members}, S, "50")
    for L_, page, note in (("pkajang", 97, "Smith's spelling (Figure 23)."), ("pmelanau", 103, "Smith's spelling.")):
        b.notation.append({"lect_id": L_, "phoneme": "", "system": "canonical", "symbol": "", "source_id": S,
                           "page": str(page), "notes": note})
