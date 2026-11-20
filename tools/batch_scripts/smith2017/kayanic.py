"""Kayanic (Smith 2017a, section 2.2, pp. 51-92; Merap from Smith 2017b)."""
from lib import Batch, Node, compose, label, split_cell, ipa, NFC
from sources import SOURCES
from common import add_language_rows, add_complements, DEC_SEMICOLON, DEC_VOWELS, decision, lect

S = "smith2017a"

def build(b: Batch):
    # ---------------- proto-nodes ----------------
    lect(b, "pkayanic", "Proto-Kayanic", "proto-language", parent="pmp", glottocode="kaya1335", clade="Kayanic",
         alt_names="PKAY", inherit="stated-unchanged", inherit_source_id=S, inherit_page="86",
         inherit_note="Unchanged from PMP in Table 23 (p. 86), which sets PMP and Proto-Kayanic side by side.",
         notes="Kayan, Murik-Merap and Segai-Modang (Smith 2017a: 51, Figure 22 p. 92). Table 23 (p. 86) is the "
               "reconstruction. Smith finds 'essentially zero high quality sound changes' for this node (p. 86); "
               "the subgroup rests on lexical innovations, chiefly *bibiR > *sibih 'lip' (pp. 87-91). Glottolog's "
               "Kayan-Murik-Modang (kaya1335) has the same members. Table 23 does not list PMP *w and *y; their "
               "retention is entered as implied.")
    lect(b, "pkmm", "Proto-Kayan-Murik-Merap", "proto-language", parent="pkayanic", glottocode="kaya1336",
         clade="Kayan-Murik-Merap", alt_names="PKM;Proto-Kayan-Murik", inherit="assumed-unchanged",
         notes="Smith endorses a node above Kayan and Murik-Merap that excludes Segai-Modang (Smith 2017a: 84, "
               "section 2.2.4.1; Figure 22, p. 92), on the shared development of word-final glottal stops "
               "and the lowering of final high vowels (pp. 54-57, 83-84), after Blust's earlier work. Smith also "
               "discusses a linkage reading (p. 85) and does not adopt it. Glottolog's Kayan-Murik (kaya1336) "
               "has the same members.")
    lect(b, "pkayan", "Proto-Kayan", "proto-language", parent="pkmm", glottocode="kaya1333", clade="Kayan",
         alt_names="PKYN", inherit="assumed-unchanged",
         notes="Long Naah, Data Dian, Balui Liko, Busang and Bahau (Smith 2017a: 52-62). Smith calls the "
               "phonological evidence for Kayan 'relatively weak' (p. 60) and rests the group on lexical "
               "innovations (pp. 60-62). Figure 10 (p. 54) lists the PMP to Proto-Kayan changes. Glottolog's Kayanic "
               "(kaya1333) is this group (Kayan languages and Bahau).")
    lect(b, "pmurik", "Proto-Murik-Merap", "proto-language", parent="pkmm", glottocode="muri1259",
         clade="Murik-Merap", alt_names="PMUR;Murik-Merap",
         inherit="assumed-unchanged",
         notes="Ngorek (Murik) and Merap (Smith 2017a: 62-72; Smith 2017b). Smith calls Merap 'an aberrant "
               "dialect of Ngorek' (2017a: 67), and Glottolog's Murik (muri1259), a language, has Ngorek, "
               "Pua', Merap and Huang Bau as dialects; the node is entered as Smith names it.")
    lect(b, "psegmod", "Proto-Segai-Modang", "proto-language", parent="pkayanic", glottocode="moda1243",
         clade="Segai-Modang", alt_names="PSM", inherit="assumed-unchanged",
         notes="Modang, Long Gelat (Modang) and Gaai, Kelai (Segai) (Smith 2017a: 72-82; Figure 18, p. 74). "
               "Smith gives no separate changes for Segai and Modang, so the four lects are entered directly "
               "under this node. Glottolog's Modang-Segai (moda1243) has the same members.")

    # PMP > Proto-Kayanic (Table 23, p. 86)
    L = "pkayanic"
    b.corr(L, "q", "", "#_", S, 86, status="", blank_type="disputed", locator="Table 23",
           as_printed="*q > *Ø?/ʔ/ʔ",
           notes="Printed with a question mark for initial position: Smith does not commit to loss or ʔ here. "
                 "Every Kayanic language in Tables 3, 8 and 14 has Ø.", decision="pkay-table23")
    b.corr(L, "q", "ʔ", "elsewhere", S, 86, locator="Table 23", as_printed="*q > *Ø?/ʔ/ʔ",
           notes="Medial and final.")
    b.corr(L, "d", "r", "V_V", S, 86, locator="Table 23", as_printed="*d > *d/r/d")
    b.corr(L, "d", "d", "elsewhere", S, 86, locator="Table 23", as_printed="*d > *d/r/d", notes="Initial and final.")
    b.corr(L, "j", "r", "V_V", S, 86, locator="Table 23", as_printed="*j > *r/d")
    b.corr(L, "j", "d", "_#", S, 86, locator="Table 23", as_printed="*j > *r/d")
    b.corr(L, "z", "j", "elsewhere", S, 86, locator="Table 23", as_printed="*z [ʤ] > *j",
           notes="Not a sound change: below PMP Smith writes *z [ʤ] as *j (p. 26). Initial, and after a nasal "
                 "(*nz > *nj).")
    b.corr(L, "z", "c", "V_V", S, 86, status="disputed", locator="Table 23", as_printed="*z [ʤ] > *j/c",
           notes="Medial *z: Kayan, Ngorek and Modang have s, Merap c (and ʄ), Segai c. In the text Smith says "
                 "only that *-z- > *-c- 'may actually be assignable to Proto-Kayanic' (p. 58); Table 23 prints c.",
           decision="pkay-table23")
    b.corr(L, "R", "h", "#_", S, 86, locator="Table 23", as_printed="*R > *h/h/R",
           notes="Every Kayanic language in Tables 3, 8 and 14 has Ø for *R-.", decision="pkay-table23")
    b.corr(L, "R", "h", "V_V", S, 86, locator="Table 23", as_printed="*R > *h/h/R")
    b.corr(L, "R", "R", "_#", S, 86, locator="Table 23", as_printed="*R > *h/h/R",
           notes="Kept: Balui Liko and Busang lost final *s but not final *R, so *-s and *-R had not merged "
                 "(p. 58).")
    b.corr(L, "h", "∅", "elsewhere", S, 86, locator="Table 23", as_printed="*h > Ø")
    b.corr(L, "e", "ə", "elsewhere", S, 86, locator="Table 23", as_printed="*ə > *ə",
           notes="The source writes ə for the PMP vowel keyed e here (p. 27).")
    for ph in ("w", "y"):
        b.corr(L, ph, ph, "elsewhere", S, 86, derivation="implied-retention", locator="Table 23",
               notes="Not in Table 23; entered as unchanged. Segai-Modang alone changed medial *w and *y (p. 76).")

    # Proto-Kayanic > Proto-Kayan-Murik-Merap (pp. 54-57, 83-84)
    L = "pkmm"
    b.corr(L, "∅", "ʔ", "V_#", S, 84, locator="§2.2.4.1",
           as_printed="*-V > *-Vʔ (accompanied by lowering of final high vowels)",
           notes="Glottal stop added after every final vowel (pp. 54, 83-84; Table 22). Figure 10 (p. 54) lists "
                 "this under Proto-Kayan, but section 2.2.4.1 assigns it to Kayan and Murik-Merap together, "
                 "since Segai-Modang did not add it after high vowels.", decision="pkmm-glottal")
    b.corr(L, "i", "e", "_#", S, 84, locator="§2.2.4.1", as_printed="*-i > *-eʔ",
           notes="Short final high vowels lowered before the added glottal stop (pp. 54-57); vowels before an "
                 "inherited glottal stop (from *q) did not lower.", decision="pkmm-glottal")
    b.corr(L, "u", "o", "_#", S, 84, locator="§2.2.4.1", as_printed="*-u > *-oʔ",
           notes="As for *-i.", decision="pkmm-glottal")

    b.phonemes.append({"lect_id": "pkmm", "ipa": "e", "source_symbol": "e", "class": "V", "place": "front",
                       "manner": "mid", "voicing": "", "rounding": "unrounded", "origin": "override", "source_id": S,
                       "page": "54", "reason": "A front mid vowel from lowered final *i (*-i > *-eʔ), not the schwa "
                       "that e spells in PMP orthography.", "notes": "", "via_source_id": "", "via_page": "",
                       "via_note": "", "status": ""})

    # Proto-Kayan-Murik-Merap > Proto-Kayan (Figure 10, p. 54; pp. 57-58)
    L = "pkayan"
    b.corr(L, "b", "v", "V_V", S, 54, locator="fig. 10", as_printed="*-b- > *v")
    for n, o in (("m", "b"), ("n", "d"), ("n", "j"), ("ŋ", "g")):
        b.corr(L, n, "∅", f"_{o}", S, 54, locator="fig. 10", as_printed=f"*{n}{o} > *{o}",
               notes="Nasal + voiced obstruent simplified. Segai-Modang did the same, which Smith treats as "
                     "parallel (pp. 60, 84-85).")
    b.corr(L, "h", "∅", "#_", S, 54, locator="fig. 10", as_printed="*R- > *Ø",
           notes="Proto-Kayanic *h- is from PMP *R- (Table 23).")
    b.corr(L, "s", "h", "#_", S, 54, locator="fig. 10", as_printed="*s- > *h")
    b.corr(L, "s", "h", "_#", S, 58, locator="§2.2.1.1.3", as_printed="*-s > *-h",
           notes="'All Kayan languages reflect the change *-s > *-h' (p. 58); Balui Liko and Busang went on to "
                 "lose it. *-R stayed apart (p. 58).")

    # Proto-Kayan-Murik-Merap > Proto-Murik-Merap (pp. 65-67)
    L = "pmurik"
    b.corr(L, "b", "p", "_#", S, 65, locator="§2.2.2.1.1", as_printed="*-b > *-p")
    b.corr(L, "d", "n", "_#", S, 65, locator="§2.2.2.1.1", as_printed="*-d > *-n",
           notes="Final *d and *j (Proto-Kayanic *d). Devoiced *-b with nasal *-d is found nowhere else in Borneo "
                 "(p. 67).")
    b.corr(L, "l", "n", "_#", S, 64, locator="Table 8", as_printed="*-l > n",
           notes="Ngorek and Merap both have n (Table 8); Merap *-l > *n (Smith 2017b: 165).")
    for n, o, c in (("m", "b", "p"), ("n", "d", "t"), ("ŋ", "g", "k")):
        b.corr(L, o, c, f"{n}_", S, 66, locator="§2.2.2.1.2", as_printed=f"*{n}{o} > {n}{c}",
               notes="Obstruent devoiced after a homorganic nasal, the cluster kept (pp. 66-67).")

    # Proto-Kayanic > Proto-Segai-Modang (Figure 18, p. 74; pp. 75-77)
    L = "psegmod"
    for v in ("a", "i", "u"):
        b.corr(L, v, "ə", "penultimate syllable", S, 74, locator="fig. 18",
               as_printed="Penultimate vowels reduced to schwa",
               notes="Kelai and Gaai later deleted most penultimate vowels (pp. 80, 104 Table 15).")
    b.corr(L, "y", "j", "V_V", S, 74, locator="fig. 18", as_printed="*-y- > j",
           notes="Glide fortition, also of transition glides (*dua [duwa]) (p. 76).")
    b.corr(L, "w", "g", "V_V", S, 74, locator="fig. 18", as_printed="*-w- > g")
    b.corr(L, "j", "c", "elsewhere", S, 73, status="regular", locator="Table 14", derivation="composed",
           as_printed="*z- > s, s, c, c; *nj > s, s, c, c",
           notes="Not stated by Smith; inferred here. Proto-Kayanic *j (PMP *z, initial and after a nasal) has "
                 "the same reflexes as medial *c in all four languages (s in Modang and Long Gelat, c in Gaai "
                 "and Kelai), while *-y- became j (Table 14). The two must have been apart when *-y- > *j.",
           decision="psm-j")
    b.corr(L, "b", "b", "#_", S, 75, locator="§2.2.3.1.1.1", as_printed="*b- > b; w",
           notes="Fortis reflex of an apparently unconditioned split (p. 75, Table 16).")
    b.corr(L, "b", "w", "#_", S, 75, locator="§2.2.3.1.1.1", as_printed="*b- > b; w",
           notes="Lenis reflex of the split (p. 75, Table 16): *batu > Modang wətaɵ̯, *bəRuaŋ > wahguə̯ŋ.")
    b.corr(L, "b", "p", "#_ before s", S, 75, locator="§2.2.3.1.1.1",
           as_printed="fortis *b- devoiced before *s in the following onset",
           notes="*bəsuR > Long Gelat, Modang pəsoh, Gaai, Kelai psɒh (Table 16).")
    b.corr(L, "b", "w", "V_V", S, 74, locator="fig. 18", as_printed="*-b- > w")
    b.corr(L, "b", "g", "u_a", S, 74, locator="fig. 18", as_printed="*-b- > g / u_a",
           notes="Between *u and *a, *-b- > *w came early enough to feed *-w- > g (pp. 76-77, Table 18).")
    b.corr(L, "b", "w", "_#", S, 74, locator="fig. 18", as_printed="*-b > w")
    b.corr(L, "d", "l", "#_", S, 75, locator="§2.2.3.1.1.2", as_printed="*d- > l; d")
    b.corr(L, "d", "d", "#_ with l in a following syllable", S, 75, locator="§2.2.3.1.1.2",
           as_printed="*d- > l; d",
           notes="Three lexemes keep d: *dali, *dəhaləm, *daləm. Smith's condition: *d- did not become l if *l "
                 "followed in a later syllable (p. 75).")
    b.corr(L, "l", "∅", "#_", S, 76, locator="§2.2.3.1.1.3", as_printed="*l- > Ø; l",
           notes="An apparently unconditioned split: 'roughly half of the examples' delete *l- (p. 76, Table 17).")
    b.corr(L, "l", "l", "#_", S, 76, locator="§2.2.3.1.1.3", as_printed="*l- > Ø; l",
           notes="The other half of the split (p. 76, Table 17).")
    for n, o in (("m", "b"), ("n", "d"), ("n", "j")):
        b.corr(L, n, "∅", f"_{o}", S, 73, locator="Table 14", as_printed=f"*{n}{o} > {o}",
               notes="Nasal + obstruent simplified in all four languages (Table 14; Table 11, p. 67). Smith treats "
                     "it as parallel to Kayan (pp. 84-85).")

    # ---------------- member languages ----------------
    langs = [
        ("bara1370", "Long Naah Kayan", "language", "pkayan", "bara1370", "kys", "Baram Kayan",
         "Long Naah, middle Baram River, Sarawak (Smith 2017a: 51). Glottolog's Baram Kayan."),
        ("kaya1325", "Data Dian Kayan", "language", "pkayan", "kaya1325", "xkn", "Kayan River Kayan;Data Dian",
         "Data Dian, upper Apo Kayan, North Kalimantan (Smith 2017a: 51). Glottolog lists Data Dian as an "
         "alternate name of Kayan River Kayan."),
        ("reja1241", "Balui Liko Kayan", "language", "pkayan", "reja1241", "ree", "Rejang Kayan;Balui Liko",
         "Balui Liko, Sungai Asap resettlement area, Sarawak (Smith 2017a: 51). Smith groups it with Uma Juman "
         "and Busang (Figure 22, p. 92); Glottolog has Uma Juman as a dialect of Rejang Kayan."),
        ("busa1255", "Busang", "language", "pkayan", "busa1255", "bfg", "Busang Kayan",
         "Busang of the upper Mahakam River, East Kalimantan (Smith 2017a: 51)."),
        ("baha1257", "Bahau", "language", "pkayan", "baha1257", "bhv", "Bahau Saq",
         "Bahau Saq of the middle Mahakam River (Smith 2017a: 51). Its place within Kayanic is discussed on "
         "pp. 84-86; Figure 22 puts it in Kayan."),
        ("ngor1244", "Ngorek", "dialect", "pmurik", "ngor1244", "", "Murik",
         "Long Semiang, upper Baram River, Sarawak (Smith 2017a: 51). Smith uses Ngorek for this dialect and "
         "Murik for the larger group (p. 62 n. 4)."),
        ("mera1243", "Merap", "dialect", "pmurik", "mera1243", "", "Mpraa;Mbraa",
         "Langap village, Malinau River, North Kalimantan (Smith 2017b: 143). Consonants from Smith (2017b: "
         "163-166), which states the conditions that Table 8 of Smith (2017a) leaves out. The vowel reflexes "
         "(Smith 2017b: 166-171; 2017a Table 9) are not entered: they depend on the vowel of the preceding "
         "syllable through reverse umlaut, and on stress shift."),
        ("moda1244", "Modang", "language", "psegmod", "moda1244", "mxd", "Kelinjau Modang;Long Wai",
         "Kelinjau Modang, Woeq Helaq on the Kelinjau River, East Kutai (Smith 2017a: 51; 2017b: 145)."),
        ("long1405", "Long Gelat", "dialect", "psegmod", "long1405", "", "Long Glat",
         "Upper Mahakam River (Smith 2017a: 51; 2017b: 145). A Modang dialect, under Busang influence."),
        ("sega1243", "Gaai", "language", "psegmod", "sega1243", "sge", "Segai;Mengga'ai",
         "Long Laai on the Segah River, Berau (Smith 2017b: 145). Gaai and Kelai are mutually intelligible "
         "Segai varieties; Glottolog has a Segai language with dialects Segah and Kelai, and gives Gaai no code "
         "of its own, so the language code is used."),
        ("kela1259", "Kelai", "dialect", "psegmod", "kela1259", "", "Punan Kelai",
         "Long Lamjan on the Kelai River, Berau (Smith 2017b: 145). Not a Punan language despite the name "
         "(Smith 2017b: 145)."),
    ]
    for (i, name, typ, par, gc, iso, alt, note) in langs:
        lect(b, i, name, typ, parent=par, glottocode=gc, iso639_3=iso, alt_names=alt,
             inherit="" if i == "mera1243" else "stated-unchanged", inherit_source_id="" if i == "mera1243" else S,
             inherit_page="" if i == "mera1243" else "50",
             inherit_note="" if i == "mera1243" else
                          "Unchanged: Smith's tables list only phonemes that changed somewhere in the subgroup "
                          "(p. 50), and this one is not listed for this lect.",
             notes=note)
    b.decisions.append(decision("kayanic-glottocodes", "Glottocodes for Smith's Kayanic varieties.",
        "Long Naah = Baram Kayan bara1370; Data Dian = Kayan River Kayan kaya1325 (Glottolog alt name); Balui "
        "Liko = Rejang Kayan reja1241; Gaai = Segai sega1243 (language code; Glottolog's dialect Segah sega1244 "
        "may be Gaai); Kelinjau Modang = Modang moda1244.",
        "Gaai = sega1244 (Segah)", S, "51"))

    nodes = {
        "pkayanic": Node("pkayanic", "pmp", {("q", "#_"): None, ("q", "V_V"): "ʔ", ("q", "_#"): "ʔ",
                                             ("d", "V_V"): "r", ("j", "V_V"): "r", ("j", "_#"): "d",
                                             ("z", "V_V"): "c", ("z", "*"): "j", ("R", "#_"): "h",
                                             ("R", "V_V"): "h", ("h", "*"): None, ("e", "*"): "ə"}),
        "pkmm": Node("pkmm", "pkayanic", {("i", "_#"): "e", ("u", "_#"): "o"}),
        "pkayan": Node("pkayan", "pkmm", {("b", "V_V"): "v", ("h", "#_"): None, ("s", "#_"): "h",
                                         ("s", "_#"): "h"}),
        "pmurik": Node("pmurik", "pkmm", {("b", "_#"): "p", ("d", "_#"): "n", ("l", "_#"): "n"}),
        "psegmod": Node("psegmod", "pkayanic", {("a", "penultimate syllable"): "ə",
                                               ("i", "penultimate syllable"): "ə",
                                               ("u", "penultimate syllable"): "ə", ("y", "V_V"): "j",
                                               ("w", "V_V"): "g", ("j", "*"): "c", ("b", "V_V"): "w",
                                               ("b", "_#"): "w"}),
    }
    chains = {"pkayan": ["pkayanic", "pkmm", "pkayan"], "pmurik": ["pkayanic", "pkmm", "pmurik"],
              "psegmod": ["pkayanic", "psegmod"]}

    # Table 3 (p. 53): Kayan consonants. Columns: Long Naah, Data Dian, Balui Liko, Busang, Bahau.
    K = ["bara1370", "kaya1325", "reja1241", "busa1255", "baha1257"]
    t3 = [("*-q-", "ʔ|ʔ|ʔ|ʔ; Ø|ʔ"), ("*-q", "Ø|ʔ|Ø|ʔ|ʔ"), ("*-b-", "v|f|v|v|f"), ("*-b", "m|m|v|v|p"),
          ("*-d-", "r|r|r|r|r"), ("*-d", "n|n|r|r|l"), ("*-j-", "r|r|r|r|r"), ("*-j", "n|n|r|r|l"),
          ("*z-", "j|j|j|j|s"), ("*-z-", "s|s|s|s|s"), ("*mb", "b|b|b|b|b"), ("*nd", "d|d|d|d|d"),
          ("*nj", "j|j|j|j|j"), ("*ŋg", "g|g|g|g|g"), ("*-l", "n|n|l|l|l"), ("*s-", "h|h|h|h|h"),
          ("*-s-", "s; h|s|s|s|h"), ("*-s", "h|h|Ø|Ø; h|h"), ("*-R-", "h|h|h|h|Ø"), ("*-R", "h|h|h|h|h")]
    clusters_kayan = {"*mb": ("b", "V_V"), "*nd": ("d", "V_V"), "*nj": ("j", "V_V"), "*ŋg": ("g", "V_V")}
    add_language_rows(b, nodes, chains, K, "pkayan", t3, S, 53, "Table 3", clusters=clusters_kayan,
                      conditioned={("busa1255", "*-s", "h"): ("ə_#", "Busang has h for *-s 'only after schwa in "
                                                              "the final syllable' (p. 58): *hapəjəs > pərah.")})
    # Table 4 (p. 53): Kayan vowels. *-aʔ is left out: see the decision pkmm-glottal.
    t4 = [("*-a", "aʔ|aʔ|aʔ|aʔ|aːʔ"), ("*-aC", "a|a; eə̯|a|a|aː"), ("*-aCVC", "a|a|a|a; i; u; e; o|a"),
          ("*-u", "oʔ|oʔ|oʔ|oʔ|oːʔ"), ("*-uC", "u; o|u; o|u; o|u; o|u; o"), ("*-i", "eʔ|eʔ|eʔ|eʔ|eːʔ"),
          ("*-iC", "i; e|i; e; iə̯|i; e; iə̯|i; e|i; e"), ("*-əC", "ə; a|ə; a|ə; a|ə; a|a"),
          ("*-ay", "ay|ay|e|e|ay"), ("*-aw", "aw|aw|o|o|aw")]
    add_language_rows(b, nodes, chains, K, "pkayan", t4, S, 53, "Table 4", final_glottal=True,
                      conditioned={
                          # Data Dian: *a before a final velar fronted with a schwa off-glide (p. 59, Table 7)
                          ("kaya1325", "*-aC", "eə̯"): ("_[k,ŋ]#", "*a in a final syllable before a velar stop "
                                                       "fronted to *e and developed a schwa off-glide (p. 59)."),
                          # Data Dian, Balui Liko: off-glide after *i before velars (p. 59)
                          ("kaya1325", "*-iC", "iə̯"): ("_[k,ŋ]#", "Off-glide after *i before a final velar "
                                                       "consonant (p. 59, Table 7)."),
                          ("reja1241", "*-iC", "iə̯"): ("_[k,ŋ]#", "Off-glide after *i before a final velar "
                                                       "consonant (p. 59, Table 7)."),
                          ("reja1241", "*-uC", "o"): ("_[k,ŋ]#", "*u lowers to o before final velar consonants "
                                                      "in Balui Liko (p. 59)."),
                      },
                      expand={
                          # Busang vowel harmony (pp. 58-59)
                          ("busa1255", "*-aCVC"): [
                              ("a", "a", "penultimate syllable", "regular", ""),
                              ("a", "i", "_[ʔ,h]i", "regular", "Vowel harmony: penultimate *a took the quality "
                               "of the final vowel when only ʔ or h stood between (pp. 58-59): *baʔik > biʔik."),
                              ("a", "u", "_[ʔ,h]u", "regular", "Vowel harmony (pp. 58-59): *kahuŋ > kuhuŋ."),
                              ("a", "e", "_[ʔ,h]e", "regular", "Vowel harmony (pp. 58-59): *taqi > teʔeʔ, with "
                               "the lowered final vowel."),
                              ("a", "o", "_[ʔ,h]o", "regular", "Vowel harmony (pp. 58-59): *pahu > pohoʔ."),
                          ]})

    # Table 8 (p. 64): Ngorek only (Merap from Smith 2017b below).
    t8 = [("*-q-", "ʔ"), ("*-q", "Ø"), ("*b-", "b"), ("*-b-", "b"), ("*-b", "p"), ("*d-", "l"), ("*-d-", "r"),
          ("*-d", "n"), ("*-j-", "r"), ("*-j", "n"), ("*z-", "j; s"), ("*-z-", "s"), ("*mb", "mp"), ("*nd", "nt"),
          ("*ŋg", "ŋk"), ("*-l", "n"), ("*s-", "Ø"), ("*-s-", "h"), ("*-s", "h"), ("*R-", "Ø"), ("*-R-", "Ø"),
          ("*-R", "h")]
    clusters_murik = {"*mb": ("p", "m_"), "*nd": ("t", "n_"), "*ŋg": ("k", "ŋ_")}
    add_language_rows(b, nodes, chains, ["ngor1244"], "pmurik", t8, S, 64, "Table 8", clusters=clusters_murik,
                      strip_cluster_nasal=True)
    t9 = [("*-a", "aʔ"), ("*-aC", "a"), ("*-aCVC", "a"), ("*-u", "oʔ"), ("*-uC", "u; o"), ("*-uCVC", "u; o"),
          ("*-i", "eʔ"), ("*-iC", "i; e"), ("*-iCVC", "i; e"), ("*-əC", "ə; a"), ("*-əCVC", "ə"), ("*-ay", "e"),
          ("*-aw", "o")]
    add_language_rows(b, nodes, chains, ["ngor1244"], "pmurik", t9, S, 65, "Table 9", final_glottal=True)
    b.decisions.append(decision("ngorek-nj", "Ngorek reflex of *nj: Table 8 (p. 64) has nc, Table 11 (p. 67) nj.",
        "Not entered.", "nc; nj", S, "64"))

    # Merap consonants (Smith 2017b: 163-166), against Proto-Murik-Merap.
    M, S2 = "mera1243", "smith2017b"
    def m(parent, child, env, page, ap, note="", status="regular", **kw):
        b.corr(M, parent, child, env, S2, page, status=status, as_printed=ap, notes=note, **kw)
    for p_ in ("p", "t", "k"):
        m(p_, "ʔ", "a_#", 163, "*-p, *-t, *-k > -ʔ after *a", "§4.1: *siap > heaʔ, *əpat > paːʔ, *anak > nayəʔ.")
        m(p_, p_, "ə_#", 163, "*-p, *-t, *-k unchanged after schwa", "§4.1: *kələb > *kələp > klap; *utək > tiwk.")
    for v in ("i", "u"):
        m("k", "ʔ", f"{v}_#", 163, "*-k > ʔ after *i and *u", "§4.1: also after *i and *u, 'although not before "
          "altering the quality of the vowel'.")
    for p_ in ("p", "t"):
        m(p_, "c", "i_#", 163, "*-t, *-p > c after *i", "§4.1: an unreleased voiceless palatal stop; *murip > "
          "mpruyc, *laŋit > laŋayc.")
        m(p_, "kʷ", "u_#", 163, "*-t, *-p > kʷ after *u", "§4.1: *pulut > pləwkʷ, *takut > takawkʷ; also final "
          "*-b, which had become *-p (*kaʔub > ŋaʔawkʷ).")
    m("ʔ", "∅", "_#", 163, "Glottal stop in word-final position was deleted", "§4.1. This is the glottal stop "
      "added after final vowels; Proto-Kayanic final *ʔ (from *q) was already lost in Proto-Murik-Merap's "
      "reflexes in Table 8.")
    m("t", "k", "#_Vl", 163, "*t- > k before *l when the vowel was deleted", "§4.2: *tulad > klũə̯, *təlu > klawʔ.")
    m("b", "m", "#_", 164, "*b- is reflected as m", "§4.4: *baya > mayaːʔ, *batu > matawʔ.")
    m("b", "ɓ", "V_V", 164, "*b > ɓ medially", "§4.4: *tabu > təɓawʔ, *mabuk > maɓawəʔ.")
    m("b", "ɓ", "#_ of a monosyllable", 164, "*b- > ɓ as the initial of a monosyllable", "§4.4: *buk > ɓawəʔ.")
    b.corr(M, "∅", "b", "m_l", S2, 164, as_printed="*b- before medial *-l- > mb",
           notes="§4.4 and §3.4: a b inserted between m (from *b-) and l: *buluʔ > mblaw, *bulan > mblũə̯.")
    m("d", "l", "#_", 164, "In initial position *d became l", "§4.4: *daʔan > laʔãə̯, *duman > lumũə̯.")
    m("j", "ɲ", "#_", 165, "*z- (Proto-Kayanic *j) is reflected as ñ", "§4.4: three examples (*jalan > nalãə̯); "
      "also t and j in one example each.", evidence_count=3)
    m("j", "t", "#_", 165, "*z- ... also as t", "§4.4: *jaʔak > taʔayəʔ.", status="sporadic", evidence_count=1)
    m("j", "d͡ʒ", "#_", 165, "*z- ... also as j", "§4.4: *jəpitan > jəʔtĩə̯.", status="sporadic",
      evidence_count=1, source_form="j")
    m("c", "t͡ʃ", "V_V", 165, "In medial position *z became c", "§4.4: *kajal > kacan; Proto-Kayanic *c "
      "(Table 23).", source_form="c")
    m("c", "ʄ", "V_V", 165, "*-z- > ʄ, a voiced palatal implosive", "§4.4: in two cases.", status="sporadic",
      evidence_count=2)
    m("j", "t͡ʃ", "n_", 165, "*nj > nc", "§4.5: *manjuʔ > ncau. Table 8 of Smith 2017a has nc too.",
      source_form="c")
    m("s", "h", "elsewhere", 165, "In all positions *s became h", "§4.6: *saləŋ > halaŋ, *paRəs > prah.")
    m("m", "∅", "a_#", 165, "the nasals delete after *a, and nasalize the preceding vowel",
      "§4.8: *maram > marãə̯. The vowel is nasalized.")
    m("n", "∅", "a_#", 165, "the nasals delete after *a, and nasalize the preceding vowel",
      "§4.8: *jalan > nalãə̯. Also final *-d and *-l (Proto-Murik-Merap *n): *tulad > klũə̯. The vowel is "
      "nasalized.")
    m("ŋ", "∅", "a_#", 165, "the nasals delete after *a, and nasalize the preceding vowel", "§4.8: *lubaŋ > ...")
    for v in ("i", "u"):
        m("ŋ", "∅", f"{v}_#", 166, "*-ŋ also deleted after *i and *u, but did not nasalize the preceding vowel",
          "§4.8: *uruŋ > rua, *ikiŋ > kia.")
    m("n", "n", "i_#", 166, "*-n became n after *i", "§4.8: *lamin > lanayn. Also from *-d and *-l: *apid > "
      "kapayn.")
    m("n", "ŋʷ", "u_#", 166, "*-n became ŋʷ after *u", "§4.8: *puʔun > puʔowŋʷ.")
    m("l", "l", "elsewhere", 165, "In initial and medial positions, *l did not change", "§4.7: *lubaŋ > loɓoyə.")
    m("r", "r", "V_V", 164, "In medial position, PMP *d became r, which is likely a retention from PKAY",
      "§4.4: Proto-Kayanic *-r- (from *-d- and *-j-) kept: *tiduR > *tiruh > terewh.")
    # From Table 8 of the dissertation, where the paper adds nothing:
    for lab, cell, page in (("*R-", "Ø", 64), ("*-R-", "Ø", 64), ("*-R", "h", 64)):
        ph, pos = label(lab)
        par = compose(nodes, chains["pmurik"], ph, pos)
        b.corr(M, par, "∅" if cell == "Ø" else cell, pos, S, page, locator="Table 8", as_printed=f"{lab} > {cell}")

    # Table 14 (p. 73): Segai-Modang consonants. Columns: Modang, Long Gelat, Gaai, Kelai.
    SM = ["moda1244", "long1405", "sega1243", "kela1259"]
    t14 = [("*p-", "p|p|p; b|p; b"), ("*t-", "t|t|t;k|t;k"), ("*k-", "k|k|k; g|k"),
           ("*-d-", "l|l; (y)|l; y|l; y"), ("*-d", "n|n|l|l"), ("*-j-", "l|l|l; y|l; y"), ("*-j", "n|n|l|l"),
           ("*z-", "s|s|c|c"), ("*-z-", "s|s|c|c"), ("*-l", "n|n|l|l"), ("*s-", "s|s; h|s|s"),
           ("*-s", "h|h|s|s"), ("*R-", "Ø|Ø|Ø|Ø"), ("*-R", "h|h|h|h")]
    add_language_rows(b, nodes, chains, SM, "psegmod", t14, S, 73, "Table 14")
    for L_ in ("moda1244", "long1405"):
        b.corr(L_, "l", "n", "_C", S, 73, locator="Table 14", as_printed="*-l- > l; n / _C",
               notes="Before a consonant, after the penultimate vowel was lost.")
    for L_, cell in (("moda1244", "b; w; Ø; p"), ("long1405", "b; w; u; Ø; p"), ("sega1243", "b; w; u; p"),
                     ("kela1259", "b; w; u; Ø; p")):
        parts = [x.strip() for x in cell.split(";")]
        if "u" in parts:
            b.corr(L_, "w", "u", "_a", S, 75, locator="§2.2.3.1.1.1", as_printed=f"*b- > {cell}",
                   notes="Lenis *b- before *a: *ba- became *u- (p. 75): *batu > Long Gelat utaː, Gaai utaw.")
        if "Ø" in parts:
            b.corr(L_, "w", "∅", "_u", S, 75, status="sporadic", locator="§2.2.3.1.1.1",
                   as_printed=f"*b- > {cell}",
                   notes="Lenis *b- before *u: 'the entire syllable containing *bu- is optionally deleted' "
                         "(p. 75): *buluq > ləwʔ.")
    b.corr("sega1243", "∅", "a", "#_l", S, 76, status="sporadic", locator="Table 17",
           as_printed="*d- > al; d; *l- > Ø; al",
           notes="Gaai has a vowel before initial l in alŋeə̯t, almoə̯t, alʔaw, but not in las (Table 17).")
    t15 = [("*-a", "ao̯ʔ|ao̯ʔ|oʔ|"), ("*-aC", "e; i; u; a|i; u; ü; e|a; æ; eə̯, i, u|æ; u; i"),
           ("*-uC", "əw; o; u|ə; əo̯; u; o; oa̯|o [əo̯, oə̯], ɒ|u, o [əo̯, oə̯], ɒ"), ("*-aCVC", "ə; Ø|ə; Ø; a|Ø; a|Ø; a"), ("*-u", "aɵ̯|aː|aw|aw"),
           ("*-uCVC", "ə; Ø|ə; Ø|Ø|Ø"), ("*-i", "ae̯|ae̯|ay|ay"), ("*-iC", "e; ay|ae̯; ey|e [e; ɛ]|e [ɪ, e]"),
           ("*-iCVC", "ə; Ø|ə; Ø|Ø|Ø"), ("*-əC", "aː|aː; eə̯|a, o|a, o"), ("*-əCVC", "ə; Ø|ə; Ø|Ø|Ø"),
           ("*-ay", "ey|ɛy|ɑːy|aːe̯"), ("*-aw", "eə̯|iə̯|eə̯w|æw")]
    add_language_rows(b, nodes, chains, SM, "psegmod", t15, S, 74, "Table 15", strip_final_glottal_note=True)
    for L_ in ("moda1244", "long1405", "sega1243", "kela1259"):
        b.corr(L_, "∅", "ʔ", "a_#", S, 83, locator="Table 22", as_printed="*-a > aʔ",
               notes="A glottal stop was added after final *a only; Segai-Modang did not add one after final high "
                     "vowels (p. 83, Table 22).")
    # Kelai final *a (p. 78): conditioned by the preceding vowel or glide.
    for env, ch, ex in (("after *i or *y", "ɛ", "*lima > mɛʔ, *buqaya > wajɛʔ"),
                        ("after *u or *w", "o", "*dua > agoʔ"),
                        ("after *a or *ə", "a", "*dəpa > paʔ, *paRa > phaʔ")):
        b.corr("kela1259", "a", ch, f"_# ({env})", S, 78, locator="§2.2.3.2.1", as_printed="*-a > ɛʔ",
               notes=f"Table 15 gives ɛʔ; the text conditions the reflex (p. 78): {ex}.")
    b.decisions.append(decision("psm-j", "Proto-Segai-Modang reflex of Proto-Kayanic *j (PMP *z- and *nz).",
        "*j > *c, inferred from Table 14: it shares the reflexes of medial *c, while *-y- > j stays apart.",
        "leave Proto-Segai-Modang *j unchanged and state the reflexes in each language", S, "73"))

    from common import occurrences
    occ = {k: occurrences(nodes, v) for k, v in chains.items()}
    par_of = {r["id"]: r["parent_id"] for r in b.lects}
    members = ["bara1370", "kaya1325", "reja1241", "busa1255", "baha1257", "ngor1244", "mera1243",
               "moda1244", "long1405", "sega1243", "kela1259"]
    add_complements(b, members, S, "50",
                    "Not listed for this position: Smith's tables list only changes (2017a: 50).",
                    parents={L_: occ[par_of[L_]] for L_ in members})
    from lib import cid
    for r in b.corrs:
        if r["child_lect_id"] == "mera1243" and r["derivation"] == "stated-retention":
            r["source_id"], r["page"] = "smith2017b", "162"
            r["notes"] = ("Not among Smith's statements of Merap sound changes for this position (2017b: 162-166, "
                          "section 4): unchanged.")
            r["id"] = cid(r["child_lect_id"], r["parent_phoneme"], r["child_phoneme"], r["environment"],
                          r["source_id"], r["page"])
    from common import ipa_respell
    ipa_respell(b, members, {L_: occ[par_of[L_]] for L_ in members}, S, "50", j_is_affricate=True)

    # notation: default canonical rows
    for L_, page, note in (("pkayanic", 86, "Smith's spelling (Table 23); *j is [ʤ] (p. 26)."),
                           ("pkmm", 84, "Smith's spelling."), ("pkayan", 54, "Smith's spelling (Figure 10)."),
                           ("pmurik", 65, "Smith's spelling."), ("psegmod", 74, "Smith's spelling (Figure 18).")):
        b.notation.append({"lect_id": L_, "phoneme": "", "system": "canonical", "symbol": "", "source_id": S,
                           "page": str(page), "notes": note})

    b.decisions.append(decision("pkay-table23", "Proto-Kayanic (Table 23, p. 86): rows Smith prints with a "
        "question mark or hedges in the text.",
        "*q- entered as a disputed blank (printed Ø?); *-z- > *c entered as disputed (the text says only that it "
        "'may' be Proto-Kayanic, p. 58); *R- > *h entered as printed, although every daughter has Ø.",
        "leave these out", S, "86"))
    b.decisions.append(decision("pkmm-glottal", "Where do the added final glottal stop and the lowering of "
        "final high vowels belong?",
        "Shared by Kayan and Murik-Merap (section 2.2.4.1, p. 84), as Smith concludes, not Kayan alone as "
        "Figure 10 (p. 54) has it; entered on both Proto-Kayan and Proto-Murik-Merap (decision kayanic-held). The "
        "lengthening of vowels before an inherited glottal stop and the later loss of that stop (Figures 11-12, "
        "pp. 56-57) are not entered, nor is Table 4's row *-aʔ, which does not match Table 6 for Long Naah.",
        "Proto-Kayan only, as in Figure 10", S, "54"))


if __name__ == "__main__":
    b = Batch("smith2017-kayanic")
    b.sources.extend(SOURCES)
    from common import add_general_decisions
    add_general_decisions(b)
    build(b)
    out = b.write()
    print(out, len(b.corrs), "rows")


HELD_NOTE = ("Smith states this for Proto-Kayanic{x}; that node is held back as an intermediate stage above the "
             "established microgroups (decision kayanic-held), so the change is entered on each microgroup.")


def hold_intermediate(b: Batch):
    """Proto-Kayanic and Proto-Kayan-Murik-Merap are held back: their rows are restated on Proto-Kayan,
    Proto-Murik-Merap and Proto-Segai-Modang, which then hang directly from PMP."""
    from lib import cid
    held = {"pkayanic": [], "pkmm": []}
    keep = []
    for r in b.corrs:
        if r["child_lect_id"] in held:
            held[r["child_lect_id"]].append(r)
        else:
            keep.append(r)
    b.corrs[:] = keep
    b._ids = {r["id"] for r in keep}

    def copy(r, L, **kw):
        n = dict(r)
        n.update(child_lect_id=L)
        x = "" if r["child_lect_id"] == "pkayanic" else " (with Kayan and Murik-Merap only, section 2.2.4.1)"
        if r["child_lect_id"] == "pkmm":
            pass
        n["notes"] = (HELD_NOTE.format(x=x) + (" " + r["notes"] if r["notes"] else "")).strip()
        if r["child_lect_id"] == "pkmm":
            n["notes"] = n["notes"].replace("for Proto-Kayanic", "for Proto-Kayan-Murik-Merap")
        if n["derivation"] in ("", "as-stated"):
            n["derivation"] = "composed"
        n.update(kw)
        n["id"] = cid(L, n["parent_phoneme"], n["child_phoneme"], n["environment"], n["source_id"], n["page"])
        return n

    def key(r):
        return (r["parent_phoneme"], r["environment"])

    plan = {
        "pkayan": (["pkayanic", "pkmm"], {("R", "#_")}),
        "pmurik": (["pkayanic", "pkmm"], {("j", "_#")}),
        "psegmod": (["pkayanic"], {("z", "elsewhere")}),
    }
    new = []
    for L, (chain, drop) in plan.items():
        for h in chain:
            for r in held[h]:
                if r["derivation"] == "implied-retention" or key(r) in drop:
                    continue
                new.append(copy(r, L))
    # the node's own rows, restated in PMP symbols where a held change made the symbol
    for r in b.corrs:
        L = r["child_lect_id"]
        if L == "pkayan" and key(r) == ("h", "#_"):
            r.update(parent_phoneme="R", as_printed="*R- > *Ø",
                     notes="Figure 10 states PMP *R- > Proto-Kayan Ø (Table 23 has *h- for Proto-Kayanic).")
        elif L in ("pkayan", "psegmod") and key(r) == ("n", "_j"):
            r.update(environment="_z", notes=r["notes"] + " PMP *nz (Smith's *nj).")
        elif L == "psegmod" and key(r) == ("j", "elsewhere"):
            r.update(parent_phoneme="z", as_printed="*z- > s, s, c, c; *nj > s, s, c, c (Table 14)",
                     notes=r["notes"] + " Stated here against PMP *z, initial and after a nasal; medial *z "
                                        "(Proto-Kayanic *c) has the same reflexes.")
        else:
            continue
        r["id"] = cid(L, r["parent_phoneme"], r["child_phoneme"], r["environment"], r["source_id"], r["page"])
    new.append(copy({"child_lect_id": "pkayanic", "parent_phoneme": "j", "child_phoneme": "n", "environment": "_#",
                     "notes": "Table 23 has *-j > *-d for Proto-Kayanic, and Proto-Murik-Merap *-d > *-n (p. 65).",
                     "as_printed": "*j > *r/d; *-d > *-n", "derivation": "", "source_id": S, "page": "65",
                     "locator": "Table 23; §2.2.2.1.1", "status": "regular",
                     **{c: "" for c in ("blank_type", "evidence_count", "system", "via_source_id", "via_page",
                                        "via_note", "conditioning", "evidence_total", "variety", "stratum",
                                        "lexical_scope", "examples", "source_form", "decision")}}, "pmurik"))
    for n in new:
        if n["id"] not in b._ids:
            b._ids.add(n["id"])
            b.corrs.append(n)
    # lects
    b.lects[:] = [r for r in b.lects if r["id"] not in ("pkayanic", "pkmm")]
    for r in b.lects:
        if r["id"] in ("pkayan", "pmurik", "psegmod"):
            r["parent_id"] = "pmp"
            r["notes"] += (" Proto-Kayanic (Smith's Table 23, p. 86) and Proto-Kayan-Murik-Merap (section 2.2.4.1) "
                           "are held back as intermediate stages; their changes are entered on this node "
                           "(decision kayanic-held).") if r["id"] != "psegmod" else (
                           " Proto-Kayanic (Smith's Table 23, p. 86) is held back as an intermediate stage; its "
                           "changes are entered on this node (decision kayanic-held).")
            r["alt_parents"] = ""
    b.phonemes[:] = [dict(p, lect_id=L) for p in b.phonemes if p["lect_id"] == "pkmm" for L in ("pkayan", "pmurik")] \
        + [p for p in b.phonemes if p["lect_id"] != "pkmm"]
    b.notation[:] = [n for n in b.notation if n["lect_id"] not in ("pkayanic", "pkmm")]
    b.decisions.append(decision("kayanic-held", "Kayanic and Kayan-Murik-Merap: intermediate stages above the "
        "microgroups Kayan, Murik-Merap and Segai-Modang.",
        "Held back, by the rule to add correspondence tables and the reconstructions of established "
        "microgroups but to hold the intermediate stages above them. Proto-Kayan, Proto-Murik-Merap and "
        "Proto-Segai-Modang hang from PMP; the Table 23 and section 2.2.4.1 changes are restated on each, "
        "marked composed. Smith himself finds no phonological evidence for Kayanic (p. 86).",
        "enter Proto-Kayanic and Proto-Kayan-Murik-Merap as nodes", S, "86"))
