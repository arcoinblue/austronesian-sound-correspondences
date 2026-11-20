"""Land Dayak (Smith 2017a, section 2.6, pp. 139-167)."""
from lib import Batch, Node
from common import add_language_rows, add_complements, ipa_respell, occurrences, decision, lect

S = "smith2017a"
NOTE50 = ("Unchanged: Smith's tables list only phonemes that changed somewhere in the subgroup (p. 50), and this "
          "one is not listed for this lect.")


def build(b: Batch):
    lect(b, "pld", "Proto-Land Dayak", "proto-language", parent="pmp", glottocode="land1261", clade="Land Dayak",
         alt_names="PLD", inherit="assumed-unchanged",
         notes="Smith 2017a, section 2.6 (pp. 139-167). 'The most prominent sound change with subgrouping value' "
               "is *R > *h and *l > *r (p. 142), but it is not attested in every language (Hliboi and Sungkung "
               "have l), so the subgroup rests mainly on lexical innovations (pp. 143-149). Many words are "
               "Malayic loans, and some reflexes could not be identified (p. 140). Smith's internal subgrouping "
               "(Figure 45, p. 193) differs from an earlier classification by Rensch and colleagues. Glottolog's Land Dayak (land1261) follows "
               "Smith.")
    lect(b, "pbenbek", "Proto-Benyadu-Bekati", "proto-language", parent="pld", glottocode="beny1238",
         clade="Benyadu-Bekati", inherit="assumed-unchanged",
         notes="Benyadu and Bekati (Smith 2017a: 149-155). Changes from Table 52 (p. 151) and Figure 42 (p. 153), "
               "with lexical innovations (pp. 153-155).")
    lect(b, "pbsld", "Proto-Bidayuh-Southern Land Dayak", "proto-language", parent="pld", glottocode="bida1239",
         clade="Bidayuh-Southern Land Dayak", alt_names="PBSLD", inherit="assumed-unchanged",
         notes="Bidayuh (Hliboi, Sungkung, Singai, Biatah, Bukar-Sadong) and Southern Land Dayak (Jangkang, "
               "Ribun, Sanggau, Golik) (Smith 2017a: 155-162). Changes from Table 52 (p. 151) and Figure 42 "
               "(p. 153). Smith's lower nodes (Bidayuh, Southern Land Dayak) are not entered: the languages hang "
               "from this node.")
    L = "pld"
    b.corr(L, "R", "h", "elsewhere", S, 142, as_printed="*R > *h", locator="§2.6.1",
           notes="'The most prominent sound change with subgrouping value in Land Dayak is the shift of *R > *h "
                 "and *l > r' (p. 142).")
    b.corr(L, "l", "r", "elsewhere", S, 142, as_printed="*l > r", locator="§2.6.1",
           notes="Many languages have ɣ, through 'an intermediate stage, *l > *r' (p. 142). Hliboi and Sungkung "
                 "have l; Smith suspects a later *r > l there, since Malay r is borrowed as l (p. 142).",
           decision="pld-l")
    b.corr(L, "e", "ə", "elsewhere", S, 151, as_printed="*ə", locator="Table 52",
           notes="The source writes ə for the PMP vowel keyed e here.")
    L = "pbenbek"
    b.corr(L, "ə", "a", "penultimate syllable", S, 151, locator="Table 52", as_printed="*əCVC > a",
           notes="'Penultimate *ə and *a merged everywhere' (Figure 42, p. 153).")
    b.corr(L, "∅", "ʔ", "V_#", S, 151, locator="Table 52", as_printed="*-V > -Vʔ")
    for v, g, ch in (("a", "w", "o"), ("a", "y", "e")):
        b.corr(L, v, ch, f"_+{g}", S, 151, locator="Table 52", as_printed="*aw, *ay > o, e")
        b.corr(L, g, ch, f"{v}+_", S, 151, locator="Table 52", as_printed="*aw, *ay > o, e")
    L = "pbsld"
    for v, g, ch in (("a", "w", "u"), ("a", "y", "i")):
        b.corr(L, v, ch, f"_+{g}", S, 151, locator="Table 52", as_printed="*aw, ay > u, i")
        b.corr(L, g, ch, f"{v}+_", S, 151, locator="Table 52", as_printed="*aw, ay > u, i")
    b.corr(L, "a", "ɨ", "_#", S, 151, locator="Table 52", as_printed="*-a > *ɨh")
    b.corr(L, "∅", "h", "[a,u]_#", S, 151, locator="Table 52", as_printed="*-a > *ɨh; *-u > *uh",
           notes="An h added after final *a and *u.")
    b.corr(L, "ə", "a", "penultimate syllable", S, 153, locator="fig. 42", as_printed="schwa split",
           notes="'Penultimate *ə did not merge with *a after *p or *b; penultimate *ə and *a merged everywhere "
                 "else' (Figure 42, p. 153).")
    b.corr(L, "ə", "ə", "penultimate syllable after p or b", S, 153, locator="fig. 42", as_printed="schwa split",
           notes="After *p and *b schwa kept apart: deleted in Hliboi, i in Sungkung, assimilated elsewhere "
                 "(p. 153).")
    b.decisions.append(decision("pld-l", "Land Dayak *l > *r: Hliboi and Sungkung have l (Table 50).",
        "*l > *r at Proto-Land Dayak, as Smith reads it (p. 142); the two languages are entered with r > l.",
        "*l unchanged at Proto-Land Dayak; r and ɣ as parallel changes", S, "142"))

    langs = [
        ("beny1237", "Benyadu", "pbenbek", "beny1237", "byd", "Benyadu'", "Landak Regency, West Kalimantan "
         "(Smith 2017a: 140)."),
        ("beka1241", "Bekati", "pbenbek", "beka1241", "bei", "Riuk Bekati'", "Bengkayang Regency (Smith 2017a: "
         "140). Glottolog has Bakati' as a family; Riuk Bekati' (beka1241) is taken for Smith's Bekati, which he "
         "lists apart from Rara Bekati."),
        ("hliboi", "Hliboi", "pbsld", "", "", "Hliboi Bidayuh", "Bengkayang Regency (Smith 2017a: 140); first data "
         "on this Bidayuh dialect (pp. 164-167). No Glottolog languoid by this name."),
        ("sungkung", "Sungkung", "pbsld", "", "", "", "Bengkayang Regency (Smith 2017a: 140). No Glottolog "
         "languoid by this name."),
        ("jang1257", "Jangkang", "pbsld", "jang1257", "djo", "", "Sanggau Regency (Smith 2017a: 140)."),
        ("ribu1241", "Ribun", "pbsld", "ribu1241", "rir", "", "Sanggau Regency (Smith 2017a: 140)."),
        ("sang1339", "Sanggau", "pbsld", "sang1339", "scg", "", "Sanggau Regency (Smith 2017a: 140)."),
        ("golik", "Golik", "pbsld", "", "", "", "Sanggau Regency (Smith 2017a: 140). No Glottolog languoid by "
         "this name."),
    ]
    for (i, name, par, gc, iso, alt, note) in langs:
        lect(b, i, name, "language", parent=par, glottocode=gc, iso639_3=iso, alt_names=alt,
             inherit="stated-unchanged", inherit_source_id=S, inherit_page="50", inherit_note=NOTE50,
             notes=note + " Vowel reflexes are entered from Table 52 (p. 151) only: Table 51 separates reflexes "
                          "with '/' without saying what the slash means.")
    nodes = {
        "pld": Node("pld", "pmp", {("R", "*"): "h", ("l", "*"): "r", ("e", "*"): "ə"}),
        "pbenbek": Node("pbenbek", "pld", {}),
        "pbsld": Node("pbsld", "pld", {("a", "_#"): "ɨ"}),
    }
    chains = {"pbenbek": ["pld", "pbenbek"], "pbsld": ["pld", "pbsld"]}
    LD = ["beny1237", "beka1241", "hliboi", "sungkung", "jang1257", "ribu1241", "sang1339", "golik"]
    # Table 50 (p. 141), cleaned: cells with '?' and the optional prenasalization '(n)t', '(ŋ)k', '(n)s' left out
    # (see the lects' notes); Bidayuh ('Bid') left out because the column does not say which variety it is.
    t50 = [("*p-", "|||||||"), ("*-p", "|||||ʔ||"), ("*t-", "||t; (k)|||||"), ("*-t", "|||||ʔ||"),
           ("*-k", "k|ʔ|k|k|ʔ|ʔ|ʔ|k"), ("*q-", "Ø|Ø|Ø|Ø|Ø|Ø|Ø|Ø"), ("*-q-", "Ø|Ø|ʔ|ʔ|Ø|Ø|Ø|Ø"),
           ("*-q", "ʔ|Ø|ʔ|ʔ|Ø|Ø|Ø|ʔ"), ("*-b", "p||b|b|p||?|p?"), ("*-d-", "|d|d|d|d|d|d|d"), ("*-j-", "d|d|d|d|d|d|d|d"),
           ("*-d", "t|t|d|d|t?|ʔ|?|t"), ("*-j", "t|t|d|d|t?|ʔ|?|t"), ("*s-", "|||||c; s||"), ("*-s", "|h; s||||h?|s?|"),
           ("*l-", "r|ɣ|Ø?|Ø|ɣ|h|ɣ|ʀ"), ("*-l-", "r|ɣ|l|l|ɣ|h|ɣ|ʀ"), ("*-l", "Ø|Ø|?|Ø|?|Ø?|Ø?|Ø?"),
           ("*R-", "||Ø?||Ø|Ø|?|Ø?"), ("*-R-", "h; (y); (r)|h; (y); (r)|Ø|Ø, y|Ø; (y)|Ø; (y)|?; (y)|Ø; y"),
           ("*-R", "h|h|h||h|h|Ø; h?|Ø; (y)")]
    add_language_rows(b, nodes, {**chains, "pbenbek": chains["pbenbek"], "pbsld": chains["pbsld"]},
                      LD[:2], "pbenbek", [(l, "|".join(c.split("|")[:2])) for l, c in t50], S, 141, "Table 50",
                      many_ok=True)
    add_language_rows(b, nodes, chains, LD[2:], "pbsld", [(l, "|".join(c.split("|")[2:])) for l, c in t50], S, 141,
                      "Table 50", many_ok=True)
    b.corr("hliboi", "∅", "h", "#_n", S, 141, locator="Table 50", as_printed="*p- > p; h/_n",
           notes="Before n (from the loss of the penultimate vowel).")
    # Preploded final nasals (p. 142): areal, so entered on the lects.
    for L_ in ("beny1237", "hliboi", "sungkung", "jang1257", "ribu1241", "golik"):
        for n, p_ in (("m", "p"), ("n", "t"), ("ŋ", "k")):
            b.corr(L_, "∅", p_, f"_{n}#", S, 141, locator="Table 50", as_printed=f"*-{n} > {p_}{n}; {n}",
                   notes="Preploded final nasal (p. 142); the plain nasal is also listed. Golik's is printed "
                         "with a glottal mark.")
    for n, p_ in (("m", "p"), ("n", "t"), ("ŋ", "k")):
        b.corr("beka1241", n, p_, "_#", S, 141, locator="Table 50", as_printed=f"*-{n} > {p_}; {n}",
               notes="Preploded nasals 'further simplified to p, t, and k' in Bekati (p. 142); the nasal is also "
                     "listed.")
    # Table 52 (p. 151): later vowel changes in single languages.
    for L_ in ("jang1257", "ribu1241", "sang1339"):
        b.corr(L_, "ɨ", "u", "_#", S, 151, locator="Table 52", as_printed="*ɨh > uh")
    for L_ in ("sang1339", "golik"):
        b.corr(L_, "∅", "h", "i_#", S, 151, locator="Table 52", as_printed="*-i > *ih")
    b.decisions.append(decision("landdayak-tables", "Land Dayak Tables 50-51 (pp. 141-142).",
        "Consonant cells with '?', Bidayuh's column ('Bid', variety not named) and the optional prenasalization "
        "'(n)t' are left out; vowels are entered from the summary Table 52 only. Table 52 has *-i > *ih for "
        "Jangkang and Ribun, and *-i > -itn for Hliboi and Sungkung, where Table 51 prints is, is, əi̯, i: those "
        "are left out.", "enter Table 51 with '/' read as 'or'", S, "141"))

    occ = {k: occurrences(nodes, v) for k, v in chains.items()}
    par_of = {r["id"]: r["parent_id"] for r in b.lects}
    add_complements(b, LD, S, "50", "Not listed for this position: Smith's tables list only changes (2017a: 50).",
                    parents={L_: occ[par_of[L_]] for L_ in LD})
    ipa_respell(b, LD, {L_: occ[par_of[L_]] for L_ in LD}, S, "50")
    for L_, page in (("pld", 142), ("pbenbek", 151), ("pbsld", 151)):
        b.notation.append({"lect_id": L_, "phoneme": "", "system": "canonical", "symbol": "", "source_id": S,
                           "page": str(page), "notes": "Smith's spelling."})
