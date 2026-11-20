"""Punan and Müller-Schwaner (Smith 2017a, sections 2.4-2.5, pp. 111-139)."""
from lib import Batch, Node
from common import add_language_rows, add_complements, ipa_respell, occurrences, decision, lect

S = "smith2017a"
NOTE50 = ("Unchanged: Smith's tables list only phonemes that changed somewhere in the subgroup (p. 50), and this "
          "one is not listed for this lect.")


def build(b: Batch):
    lect(b, "ppunan", "Proto-Punan", "proto-language", parent="pmp", glottocode="puna1280", clade="Punan",
         alt_names="PPUN", inherit="stated-unchanged", inherit_source_id=S, inherit_page="114",
         inherit_note="Unchanged from PMP in Table 31 (p. 114), which sets PMP and Proto-Punan side by side.",
         notes="Punan Tubu, Punan Bah, Punan Aput, Beketan, Ukit and others (Smith 2017a: 111-127; Figure 27, "
               "p. 112). 'Proto-Punan had not undergone any major changes'; the subgroup rests on lexical "
               "innovations, above all the metathesis *təlaʔus > *təlasuʔ 'barking deer' (p. 114). Smith treats "
               "Punan as one language with dialects (p. 120). His internal split into Punan Tubu-Bah and the rest "
               "(Figures 28-29, pp. 122-124) has conflicting evidence (p. 122), so no lower nodes are entered; "
               "the changes are entered on each lect. Table 31 has '?' for PMP *r. Glottolog's Punan (puna1280) "
               "follows Smith's grouping.")
    lect(b, "pmuller", "Proto-Müller-Schwaner", "proto-language", parent="pmp", glottocode="mull1247",
         clade="Müller-Schwaner", alt_names="PMÜL;Proto-Muller-Schwaner", inherit="stated-unchanged",
         inherit_source_id=S, inherit_page="128",
         inherit_note="Unchanged from PMP in Table 39 (p. 128), which sets PMP and Proto-Müller-Schwaner side by "
                      "side.",
         notes="Aoheng, Seputan, Hovongan and Kereho (Smith 2017a: 127-139; Figure 30). Table 39 and Figure 31 "
               "(pp. 128-129) give the reconstruction. Smith keeps it apart from Punan here and discusses a "
               "Punan-Müller-Schwaner link in chapter 3 (pp. 330-335), which is not entered. His internal "
               "subgrouping has three primary branches (Upper Mahakam, Kereho, Hovongan; Figure 38, p. 139), so "
               "no lower nodes are entered. Table 39 has '?' for PMP *r. Glottolog's Muller-Schwaner (mull1247) "
               "has the same members.")

    L = "ppunan"
    for par, ch, env, ap, note in (
            ("q", "∅", "#_", "*q > *Ø/ʔ/ʔ", ""), ("q", "ʔ", "elsewhere", "*q > *Ø/ʔ/ʔ", "Medial and final."),
            ("b", "p", "_#", "*b > *b/b/p", ""), ("d", "r", "V_V", "*d > *d/r/t", ""),
            ("d", "t", "_#", "*d > *d/r/t", ""), ("j", "r", "V_V", "*j > *r/t", ""), ("j", "t", "_#", "*j > *r/t", ""),
            ("z", "j", "elsewhere", "*z [ʤ] > *j", "Not a sound change: below PMP Smith writes *z [ʤ] as *j (p. 26)."),
            ("l", "n", "_#", "*l > *l/l/n", ""), ("R", "∅", "#_", "*R > *Ø/h/Ø", ""),
            ("R", "h", "V_V", "*R > *Ø/h/Ø", "'a few Punan languages sporadically retain *R as h intervocalically, "
             "so it was likely present in this position in Proto-Punan' (p. 114)."),
            ("R", "∅", "_#", "*R > *Ø/h/Ø", ""), ("s", "∅", "_#", "*s > *s/s/Ø", ""),
            ("h", "∅", "elsewhere", "*h > *Ø", ""),
            ("a", "ə", "_#", "*a > *a/a/ə", "Word-final *a raised to *ə, 'although this change may have been "
             "allophonic' (p. 114)."),
            ("e", "ə", "elsewhere", "*ə > *ə", "The source writes ə for the PMP vowel keyed e here.")):
        b.corr(L, par, ch, env, S, 114, locator="Table 31", as_printed=ap, notes=note)
    b.corr(L, "r", "", "elsewhere", S, 114, status="", blank_type="not-attested", locator="Table 31",
           as_printed="*r > ?", notes="Table 31 prints '?' for PMP *r.")

    L = "pmuller"
    for par, ch, env, page, loc, ap, note in (
            ("k", "ʔ", "_#", 128, "Table 39", "*k > *k/k/ʔ", ""),
            ("q", "∅", "#_", 128, "Table 39", "*q > *Ø/ʔ/ʔ", ""),
            ("q", "ʔ", "elsewhere", 128, "Table 39", "*q > *Ø/ʔ/ʔ", "Medial and final."),
            ("b", "v", "V_V", 128, "Table 39", "*b > *b/v/p", ""), ("b", "p", "_#", 128, "Table 39", "*b > *b/v/p", ""),
            ("d", "r", "V_V", 128, "Table 39", "*d > *d/r/t", ""), ("d", "t", "_#", 128, "Table 39", "*d > *d/r/t", ""),
            ("j", "r", "V_V", 128, "Table 39", "*j > *r/t", ""), ("j", "t", "_#", 128, "Table 39", "*j > *r/t", ""),
            ("z", "c", "elsewhere", 128, "Table 39", "*z [ʤ] > *c", "Also in Kayanic, Kadorih, Tunjung and Kiput "
             "(p. 130)."),
            ("g", "k", "elsewhere", 128, "Table 39", "*g > *k", "Initially and medially (p. 130)."),
            ("l", "d", "#_i", 128, "Table 39", "*l > *l;d/l/Ø", "Before high front vowels (p. 130)."),
            ("l", "∅", "_#", 128, "Table 39", "*l > *l;d/l/Ø", "With *-al, *-əl > *-ɪ (p. 129)."),
            ("a", "ɪ", "_l#", 129, "fig. 31", "*-al; əl > *-ɪ", "Deletion of *-l 'is the only known condition for "
             "historical innovation of *ɪ' (p. 130)."),
            ("e", "ɪ", "_l#", 129, "fig. 31", "*-al; əl > *-ɪ", ""),
            ("R", "h", "#_", 128, "Table 39", "*R > *h/h/(met)", ""), ("R", "h", "V_V", 128, "Table 39", "*R > *h/h/(met)", ""),
            ("R", "∅", "_#", 128, "Table 39", "*R > *h/h/(met)", "Final *R lost, with *-aCuR > -oCa (p. 129)."),
            ("u", "a", "_R#", 129, "fig. 31", "*-aCuR > -oCa", "*bəsuR > bosa, *təluR > toa (p. 129)."),
            ("s", "∅", "elsewhere", 129, "fig. 31", "*s > Ø", "Table 39 also has Ø."),
            ("h", "∅", "elsewhere", 128, "Table 39", "*h > Ø", ""),
            ("a", "o", "_#", 128, "Table 39", "*a > *a/a/o; ɪ", ""),
            ("u", "ʉ", "_#", 129, "fig. 31", "*-u > -ʉ", "Kept in Aoheng and Seputan; Smith reconstructs it from "
             "the correspondences of section 2.5.1.2 (pp. 130-133)."),
            ("e", "o", "_C#", 128, "Table 39", "*ə > *ə/o", "Final syllable (Table 38: *-əC > o)."),
            ("e", "ə", "penultimate syllable", 128, "Table 39", "*ə > *ə/o", "The source writes ə.")):
        b.corr(L, par, ch, env, S, page, locator=loc, as_printed=ap, notes=note)
    b.corr(L, "u", "i", "_+y", S, 128, locator="Table 39", as_printed="*-uy > *-i")
    b.corr(L, "y", "i", "u+_", S, 128, locator="Table 39", as_printed="*-uy > *-i")
    b.corr(L, "y", "y", "elsewhere", S, 128, locator="Table 39", derivation="stated-retention",
           as_printed="*-ay > *-ay", notes="Kept except in *-uy (Table 39).")
    b.corr(L, "r", "", "elsewhere", S, 128, status="", blank_type="not-attested", locator="Table 39",
           as_printed="*r > ?", notes="Table 39 prints '?' for PMP *r.")

    langs = [
        ("puna1266", "Punan Tubu", "language", "ppunan", "puna1266", "puj", "", "Malinau regency, North "
         "Kalimantan (Smith 2017a: 112)."),
        ("puna1276", "Punan Bah", "dialect", "ppunan", "puna1276", "", "", "Middle Rejang River, between Kapit "
         "and Belaga (Smith 2017a: 112). Much influenced by Kajang and Melanau neighbours (p. 124)."),
        ("puna1267", "Punan Aput", "language", "ppunan", "puna1267", "pud", "", "East and North Kalimantan "
         "(Smith 2017a: 112)."),
        ("buki1248", "Beketan", "language", "ppunan", "buki1248", "", "Bukitan", "Near the headwaters of the "
         "Mahakam, Boh and Kapuas (Smith 2017a: 112). Glottolog's Bukitan."),
        ("ukit1237", "Ukit", "language", "ppunan", "ukit1237", "umi", "", "Sungai Asap resettlement area, "
         "Sarawak (Smith 2017a: 112). Listed under Melanau-Kajang by Ethnologue; a Punan dialect for Smith "
         "(p. 124)."),
        ("sepu1237", "Seputan", "dialect", "pmuller", "sepu1237", "", "", "Upper Mahakam River (Smith 2017a: "
         "127). Nearly identical to Aoheng (p. 127)."),
        ("kere1285", "Kereho", "language", "pmuller", "kere1285", "xke", "", "Upper Kapuas River (Smith 2017a: "
         "127)."),
        ("hovo1239", "Hovongan", "language", "pmuller", "hovo1239", "", "Hobongan", "Upper Kapuas River (Smith "
         "2017a: 127). Glottolog's Hobongan."),
    ]
    for (i, name, typ, par, gc, iso, alt, note) in langs:
        lect(b, i, name, typ, parent=par, glottocode=gc, iso639_3=iso, alt_names=alt, inherit="stated-unchanged",
             inherit_source_id=S, inherit_page="50", inherit_note=NOTE50, notes=note)

    nodes = {
        "ppunan": Node("ppunan", "pmp", {("q", "#_"): None, ("q", "V_V"): "ʔ", ("q", "_#"): "ʔ", ("b", "_#"): "p",
                                         ("d", "V_V"): "r", ("d", "_#"): "t", ("j", "V_V"): "r", ("j", "_#"): "t",
                                         ("z", "*"): "j", ("l", "_#"): "n", ("R", "#_"): None, ("R", "V_V"): "h",
                                         ("R", "_#"): None, ("s", "_#"): None, ("h", "*"): None, ("a", "_#"): "ə",
                                         ("e", "*"): "ə"}),
        "pmuller": Node("pmuller", "pmp", {("k", "_#"): "ʔ", ("q", "#_"): None, ("q", "V_V"): "ʔ", ("q", "_#"): "ʔ",
                                           ("b", "V_V"): "v", ("b", "_#"): "p", ("d", "V_V"): "r", ("d", "_#"): "t",
                                           ("j", "V_V"): "r", ("j", "_#"): "t", ("z", "*"): "c", ("g", "*"): "k",
                                           ("l", "_#"): None, ("R", "#_"): "h", ("R", "V_V"): "h", ("R", "_#"): None,
                                           ("s", "*"): None, ("h", "*"): None, ("a", "_#"): "o", ("u", "_#"): "ʉ",
                                           ("e", "_C#"): "o", ("e", "*"): "ə"}),
    }
    chains = {"ppunan": ["ppunan"], "pmuller": ["pmuller"]}

    P = ["puna1266", "puna1276", "puna1267", "buki1248", "ukit1237"]
    t29 = [("*-k", "k|ʔ|k|k|k"), ("*-q-", "ʔ|ʔ|ʔ|Ø|Ø"), ("*-b-", "f|v|v|v|v"), ("*d-", "d|d|d|d; l|d"),
           ("*-z-", "c|s|j|j|j"), ("*-R-", "Ø|Ø|Ø|Ø; h|Ø; h"), ("*s-", "Ø|Ø; s|s|Ø|s"),
           ("*-s-", "Ø|Ø; s|h; s|h; s|s")]
    add_language_rows(b, nodes, chains, P, "ppunan", t29, S, 113, "Table 29")
    # Table 30 (p. 113). Punan Tubu's final h (oh, uh, ih) is entered once as an inserted h.
    t30 = [("*-a", "o|o|o|o|ə"), ("*-aC", "a|a; eə̯ / _ŋ,k|a|a|a"),
           ("*-uC", "u|u; uə̯ / _ŋ,k|u|u|u"), ("*-iC", "i|i; iə̯ / _ŋ,k|i|i|i"),
           ("*-əC", "o; e / u,iC_|o; e / u,iC_|o; e / uC_|o; e / uC_|ə"),
           ("*-əCVC", "ə; o; Ø / #_|e; o|a; o|a; o|a")]
    add_language_rows(b, nodes, chains, P, "ppunan", t30, S, 113, "Table 30", many_ok=True)
    b.corr("puna1266", "∅", "h", "V_#", S, 113, locator="Table 30", as_printed="*-a > oh; *-u > uh; *-i > ih",
           notes="Final open syllables closed with h in Punan Tubu.")
    for L_, ch, note in (("puna1266", "ə", "*a became schwa before *a in the final syllable (p. 120, Table 33)."),
                         ("puna1276", "e", "*a became schwa before *a in the final syllable, then fronted to e "
                          "(pp. 120-121, Table 33); one example has o (məkopan).")):
        b.corr(L_, "a", ch, "penultimate syllable _Ca(C)#", S, 113, locator="Table 30",
               as_printed="*-aCVC > a; ə / _Ca" if ch == "ə" else "*-aCVC > a; e,o / _Ca", notes=note)
    b.decisions.append(decision("punan-internal", "Punan internal subgrouping (Figures 28-29, pp. 122-124).",
        "No lower nodes: Punan Tubu-Bah (*a > *ə / _Ca(C)#, *z > *c) conflicts with the backing of final *ə "
        "shared by Punan Tubu, Bah, Aput and Beketan (pp. 120-122). The changes are entered on each lect.",
        "a Punan Tubu-Bah node and an 'other Punan' node", S, "122"))

    MS = ["sepu1237", "kere1285", "hovo1239"]
    t37 = [("*-k", "Ø/ʔ|ʔ|ʔ"), ("*-q", "Ø/ʔ|ʔ|Ø/ʔ"), ("*-b-", "v|v; (w)|v"), ("*l-", "l|l|l"),
           ("*-l-", "Ø; ɾ; l|Ø; l; r|Ø; l; r")]
    # Table 37 'Ø/ʔ' (Seputan *-k, *-q; Hovongan *-q): two reflexes with no ranking given.
    add_language_rows(b, nodes, chains, MS, "pmuller", [r for r in t37 if r[0] in ("*-b-",)], S, 128, "Table 37")
    for L_, lab in (("sepu1237", "*-k"), ("sepu1237", "*-q"), ("hovo1239", "*-q")):
        for ch in ("∅", "ʔ"):
            b.corr(L_, "ʔ", ch, "_#", S, 128, locator="Table 37", as_printed=f"{lab} > Ø/ʔ",
                   notes="Printed 'Ø/ʔ', with no ranking or condition." + (" Same sound." if ch == "ʔ" else ""))
    for L_ in MS:
        b.corr(L_, "l", "∅", "V_V", S, 133, locator="§2.5.2.1", as_printed="*-l- > Ø; ɾ; l / Ø; l; r",
               notes="Medial *l has three correspondence sets in Müller-Schwaner (Tables 40-43, pp. 133-136); the "
                     "conditions are not recovered. Only the loss is entered, the first reflex in Table 37.",
               decision="smith-semicolon")
    t38 = [("*-al", "ɪ|i|e"), ("*-u", "ʉ|u|u"), ("*-uC", "u; o / _k#|u; o / _k#|u"),
           ("*-əCVC", "o|o|a; Ø / #_"), ("*-ay", "i|e|e"), ("*-aw", "u|o|o")]
    for L_, ch in zip(MS, ("ɪ", "i", "e")):
        b.corr(L_, "ɪ", ch, "_#", S, 128, locator="Table 38", as_printed=f"*-al, *-əl > {ch}",
               notes="Proto-Müller-Schwaner *ɪ (from *-al, *-əl)." + (" Same sound." if ch == "ɪ" else ""))
    add_language_rows(b, nodes, chains, MS, "pmuller", [r for r in t38 if r[0] in ("*-uC", "*-ay", "*-aw")], S,
                      128, "Table 38", many_ok=True)
    for L_, ch in zip(MS, ("ʉ", "u", "u")):
        if ch != "ʉ":
            b.corr(L_, "ʉ", ch, "_#", S, 128, locator="Table 38", as_printed=f"*-u > {ch}")
    b.corr("kere1285", "ə", "o", "penultimate syllable", S, 128, locator="Table 38", as_printed="*-əCVC > o")
    b.corr("sepu1237", "ə", "o", "penultimate syllable", S, 128, locator="Table 38", as_printed="*-əCVC > o")
    b.corr("hovo1239", "ə", "a", "penultimate syllable", S, 128, locator="Table 38", as_printed="*-əCVC > a; Ø / #_")
    b.corr("hovo1239", "ə", "∅", "#_", S, 128, locator="Table 38", as_printed="*-əCVC > a; Ø / #_",
           notes="Initial schwa lost (Table 49, p. 139).")
    pmp_occ = occurrences({}, [])
    add_complements(b, ["ppunan", "pmuller"], S, "", "", parents={"ppunan": pmp_occ, "pmuller": pmp_occ},
                    cite={"ppunan": ("114", "Unchanged in this position: Table 31 (p. 114)."),
                          "pmuller": ("128", "Unchanged in this position: Table 39 (p. 128).")})
    occ = {k: occurrences(nodes, v) for k, v in chains.items()}
    par_of = {r["id"]: r["parent_id"] for r in b.lects}
    members = P + MS
    add_complements(b, members, S, "50", "Not listed for this position: Smith's tables list only changes "
                    "(2017a: 50).", parents={L_: occ[par_of[L_]] for L_ in members})
    ipa_respell(b, members, {L_: occ[par_of[L_]] for L_ in members}, S, "50", j_is_affricate=True)
    for L_, page, note in (("ppunan", 114, "Smith's spelling (Table 31)."),
                           ("pmuller", 128, "Smith's spelling (Table 39).")):
        b.notation.append({"lect_id": L_, "phoneme": "", "system": "canonical", "symbol": "", "source_id": S,
                           "page": str(page), "notes": note})
