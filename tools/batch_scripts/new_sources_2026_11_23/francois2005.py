"""Batch francois2005-vowels: François (2005), vowel hybridization in 17 northern Vanuatu languages (+ Sakao).

François, Alexandre. 2005. Unraveling the history of the vowels of seventeen northern Vanuatu languages.
Oceanic Linguistics 44(2). 443-504. Read from the Project MUSE PDF (born digital; the charts of Appendix 1,
pp. 490-491, read from page images because the text layer garbles ɛ, ɔ and the ligatures).

    python3 tools/batch_scripts/new_sources_2026_11_23/francois2005.py
"""
from common import write

S = "francois2005"
G = "guy1977"
BATCH = "francois2005-vowels"
DEC = "francois2005-hybridization"

SOURCES = [
    dict(id=S, author="François, Alexandre", year="2005",
         title="Unraveling the history of the vowels of seventeen northern Vanuatu languages",
         url_or_doi="https://doi.org/10.1353/ol.2005.0034", kind="comparative", pub_type="article",
         container_title="Oceanic Linguistics", volume="44", issue="2", pages="443-504",
         notes="Consulted directly on 23 November 2026 (Project MUSE PDF; the charts read from page images). Table 1, the 17 "
               "Torres and Banks languages and their vowel inventories (p. 445); the method of vowel hybridization "
               "(§2.3, Mwesen Tables 2-3, pp. 449-451); its parallel, recent development in each language except Mota "
               "(§3, pp. 452-457); Appendix 1, charts of regular vowel correspondences *V1(C)V2 > V' for each language "
               "and for Sakao after Guy (1977) (pp. 489-491); Appendix 2, northern Vanuatu reconstructions. Data are the "
               "author's own (n. 2)."),
    dict(id=G, author="Guy, Jacques", year="1977", title="On the origins of the Sakao vowel system (New Hebrides)",
         kind="comparative", pub_type="article", container_title="Journal of the Polynesian Society", volume="86",
         pages="97-103", notes="Bibliographic details from the reference list of François (2005). Not consulted; its "
                               "correspondences are reproduced by François (2005: 491) as the 18th chart."),
]

L = {"HIU": "hiww1237", "LTG": "loto1240", "LHI": "leha1243", "LHR": "leha1244", "VLW": "volo1238", "MTP": "motl1237",
     "LMG": "leme1238", "VRA": "vera1241", "VRS": "vure1239", "MSN": "mwes1235", "MTA": "mota1237", "NUM": "nume1241",
     "DRG": "weta1242", "KRO": "koro1318", "OLR": "olra1234", "LKN": "lako1245", "MRL": "merl1237", "SAK": "port1296"}
PAGE = {k: "490" for k in ("HIU", "LTG", "LHI", "LHR", "VLW", "MTP", "LMG", "VRA")}
PAGE.update({k: "491" for k in L if k not in PAGE})

# Appendix 1. Rows: stressed *V1 = i e a o u; columns: posttonic *V2 = i e a o u.
# ';' separates the regular reflexes of one cell; X_ or X: V2 lost; X_Y: V1 > X and V2 > Y;
# <X>: the adjacent sequence *V1V2 (no consonant); (i)X: X with an optional on-glide (Lo-Toga diphthongs);
# Mota (i)_e: the stressed vowel may be lost; '?' and '-': no regular reflex given.
CH = {
 "HIU": ["i_ | i_ə | i_ə;e_ə | i_ə | i_", "e_ | e_ | e_ə | e_ | e_", "ɔ_;e_ | a_;e_ | a_ə;ɔ_ə | a_;e_ | ɔ_",
         "ɵ_ | o_ | ɔ_ə | o_ | ɵ_", "ʉ_;i_ | ʉ_ə | ʉ_ə;ɵ_ə | ɵ_ə | ʉ_;i_"],
 "LTG": ["i_ | i_ə | i_ə;e_ə | i_ə | i_", "e_ | i_ | e_ə;(i)ɛ_ə | i_;ɛ_ | e_",
         "(i)ɛ_ | (i)a_;e_ | (i)e_ə;(i)a_ə;ɔ_ə | a_;e_ | ɔ_;ɛ_", "(o)ə_ | o_ | (o)ɔ_ə | o_ | ə_",
         "ʉ_ | ʉ_ə | ə_ə;ʉ_ə | ə_ə | ʉ_;i_"],
 "LHI": ["i | e | e | e | i", "e | ɛ | æ | ɛ | e", "æ | a | a | a | ɔ", "o | ɔ | ɔ | ɔ;ɛ | e", "u | o | o | o | u"],
 "LHR": ["i | ? | i͡e | i͡e | ?", "e | ɛ | ɛ | ɛ | e", "ɛ | a | a | a | ɛ;œ", "o | ɔ | ɔ | ɔ | œ", "u;i | o | o | o | u;i"],
 "VLW": ["i | ɪ | ɪ | ɪ | i", "ɪ | ɛ | ɛ | ɛ | ɪ", "ɛ;ɪ | a | a | a | ɛ", "ʊ;ɪ | ɔ | ɔ | ɔ | ʊ;ɪ", "u;i | ʊ | ʊ | ʊ | u;i"],
 "MTP": ["i | ɪ | ɪ | ɪ | i", "ɪ | ɛ | ɛ | ɛ | ɪ", "ɛ;ɪ† | a | a;ɔ | a | ɛ;ɪ†", "ʊ;ɪ | ɔ | ɔ | ɔ | ʊ;ɪ", "u;i | ʊ | ʊ | ʊ | u;i"],
 "LMG": ["i | a | a;<ɪ> | a | i", "ɪ | ɛ | a | ɛ | ɪ", "ɛ;œ | a | a;ɒ | a | ɛ;œ", "ø | ɔ | ɔ | ɔ;œ | ø", "u | ʊ | ʊ | ʊ | u"],
 "VRA": ["i_ | i_ɪ | i_ɪ | i_ɪ | i_", "ɪ_ | ɪ_ | ɛ_ɛ;<i_ɛ> | ɪ_ | ɪ_", "a_;ɛ_ | a_;<i_ɛ> | a_a | a_ | a_;ɛ_;ɔ_",
         "ʊ_ | ʊ_ | ɔ_ɔ;<u_ɔ> | ʊ_ | ʊ_", "i_;u_ | u_ʊ | u_ʊ | u_ʊ | i_;u_"],
 "VRS": ["i | ɪ | ɪ | ɪ | i", "ɪ | ɪ | i͡a;<ɪ> | ɪ | ɪ", "ɛ;œ | i͡a;<ɪ> | a | a | ɛ;œ", "ø | ʊ | ɔ | ʊ | ø", "y | ʊ | ʊ | ʊ | y"],
 "MSN": ["i | ɪ | ɪ | ɪ | i", "ɪ | ɛ | ɛ | ɛ | ɪ", "ɛ | a | a | a | ɔ", "ʊ | ɔ | ɔ | ɔ | ʊ", "u | ʊ | ʊ | ʊ | u"],
 "MTA": ["i_ | (i)_e | (i)_a | (i)_o | i_", "e_ | e_e | e_a | e_o | e_", "a_ | a_e | a_a | a_o | a_",
         "o_ | o_e | o_a | o_o | o_", "u_ | (u)_e | (u)_a | (u)_o | u_"],
 "NUM": ["i | i | i;ɪ | i | i", "ɪ | ɛ | ɛ | ɛ | ɪ", "a;ɛ | a;ɛ | a | a | a", "ʊ | ɔ | ɔ | ɔ | ʊ", "u | u | u;ʊ | - | u"],
 "DRG": ["i | ɪ | ɪ | ɪ | i", "ɪ | ɛ | ɛ | ɛ | ɪ", "aː;<a> | a | a | a | aː;<a>", "ʊ | ɔ | ɔ | ɔ | ʊ", "u | ʊ | ʊ | ʊ | u"],
 "KRO": ["i | ɪ | ɪ | ɪ | i", "ɪ | ɛ | ɛ | ɛ | ɪ", "ɛ͡a;<a> | a | a | a | ɛ͡a;<a>", "ʊ | ɔ | ɔ | ɔ | ʊ", "u | ʊ | ʊ | ʊ | u"],
 "OLR": ["i | ɪ | ɪ | ɪ | i", "ɪ | ɛ | ɛ | ɛ | ɪ", "a;ɪ | a | a | a | a", "ʊ;ɪ | ɔ | ɔ | ɔ | ʊ;ɪ", "u | ʊ | ʊ | ʊ | u"],
 "LKN": ["i | ɪ | ɪ | ɪ | i", "ɪ | ɛ | ɛ | ɛ | ɪ", "æ | æ | a | a | a", "ɪ | ɔ | ɔ | ɔ | ɪ", "u | ʊ | ʊ | ʊ | u"],
 "MRL": ["i | ɛ͡a | ɛ͡a | ɛ͡a | i", "ɪ | ɪ | ɪ | ɪ | ɪ", "ɛ;ɛ͡a;<ɪ> | ɛ | a | a | ɔ;ɔ͡ɞ;<ʊ>", "ʊ;ɵ | œ | ɔ | ɔ | ʊ͡ɵ;ʊ",
         "ʉ | ʊ | ʊ | ʊ | ʉ"],
 "SAK": ["y | œ;<i> | œ;<i> | œ;<i> | y", "œ;<e> | ɒ | ɒ | ɒ | œ;<e>", "ɛ | a | a | a | ɛ", "œ;<ø> | ɔ | ɔ | ɔ | œ;<ø>",
         "y | œ;<u> | œ;<u> | œ;<u> | y"],
}
# Where François's symbol differs from that of a lect's sourced inventory (Lynch et al. 2002), the inventory's is used.
RESPELL = {"MTP": {"ɪ": "e", "ʊ": "o"}}
PRINTED = {"y": "ü"}  # Vurës and Sakao ü (Sakao's inventory, Crowley 2002, has y for ü)
V = "ieaou"

rows = []
n = 0


SEEN = set()


def add(code, parent, child, env, alt, printed, notes="", sf=""):
    global n
    if (code, parent, child, env) in SEEN:
        return  # the same posttonic outcome in two alternatives of one cell
    SEEN.add((code, parent, child, env))
    n += 1
    lect = L[code]
    child2 = RESPELL.get(code, {}).get(child, child)
    if child2 != child and not sf:
        sf = child
    if child in PRINTED and not sf:
        sf = PRINTED[child]
    r = dict(id=f"{lect[:4]}-fr05-{n}", child_lect_id=lect, parent_phoneme=parent, child_phoneme=child2, environment=env,
             status="regular", conditioning="unknown" if alt else "", source_id=S, page=PAGE[code],
             locator="Appendix 1", as_printed=printed, source_form=sf, notes=notes, decision=DEC)
    if code == "SAK":
        r.update(source_id=G, page="", via_source_id=S, via_page="491", locator="",
                 via_note="Reproduced by François as the 18th chart of Appendix 1, in his notation.")
    rows.append(r)


ALT = "One of several regular reflexes of this sequence, with no stated condition."
for code, chart in CH.items():
    lost = {v2: [] for v2 in V}
    for i, v1 in enumerate(V):
        cells = [c.strip() for c in chart[i].split("|")]
        for j, v2 in enumerate(V):
            cell = cells[j]
            if cell in ("?", "-"):
                continue
            alts = cell.split(";")
            n_cons = len([a for a in alts if not a.startswith("<")])
            printed = f"*{v1}(C){v2} > {cell.replace(';', ' || ')}"
            for a in alts:
                adjacent = a.startswith("<")
                a = a.strip("<>")
                dag = a.endswith("†")
                a = a.rstrip("†")
                env1 = f"_{v2} (adjacent)" if adjacent else f"_(C){v2}"
                env2 = f"{v1}_ (adjacent)" if adjacent else f"{v1}(C)_"
                alt = (not adjacent) and n_cons > 1
                note = ALT if alt else ""
                if adjacent:
                    note = "The sequence of two adjacent vowels *V1V2 (angled brackets), which did not hybridize as *V1CV2 did."
                if dag:
                    note = (note + " The reflex ɪ of *a…i and *a…u occurs only in word-internal syllables (Appendix 1, note; §5.1.2.1).").strip()
                if "_" in a:
                    x, y = a.split("_", 1)
                else:
                    x, y = a, ""
                glide = ""
                if x.startswith("(") and code == "LTG":   # (i)ɛ: ɛ or the diphthong i͡ɛ
                    g, x = x[1], x[3:]
                    glide = g
                if code == "MTA" and x.startswith("("):    # (i)_e: the stressed vowel may be lost
                    x = x.strip("()")
                    add(code, v1, x, env1, True, printed, "The stressed vowel is optional before a non-high posttonic vowel (parentheses).")
                    add(code, v1, "∅", env1, True, printed, "The stressed vowel is optional before a non-high posttonic vowel (parentheses).")
                else:
                    add(code, v1, x, env1, alt or bool(glide), printed, note)
                    if glide:
                        add(code, v1, f"{glide}͡{x}", env1, True, printed,
                            (note + f" Printed ({glide}){x}: {x} with an optional on-glide, the diphthong {glide}͡{x} of Table 1.").strip())
                if y:
                    add(code, v2, y, env2, False, printed, "The posttonic vowel survives as a final vowel Vf (*V1(C)V2 > *V'(C)Vf).")
                else:
                    k = f"{v1}{'' if adjacent else '(C)'}"
                    if k not in lost[v2]:
                        lost[v2].append(k)
    for v2, after in lost.items():
        if not after:
            continue
        add(code, v2, "∅", "posttonic, after " + ", ".join(f"*{a}" for a in after), False,
            f"*V1(C){v2} > V'(C)",
            "The posttonic vowel is lost, its quality absorbed into the stressed vowel (vowel hybridization, pp. 449-451, 489).")

PNCV = [dict(id=f"pncv-fr05-{v}", child_lect_id="pncv", parent_phoneme=v, child_phoneme=v, environment="elsewhere",
             status="regular", source_id=S, page="456-457", derivation="implied-retention", decision=DEC,
             notes="François derives the modern vowels from the five-vowel protosystem {*i e a o u}, through hybridization "
                   "that took place separately and fairly recently in each language (pp. 456-457); PNCV is taken to keep "
                   "the POc vowels.") for v in V]

DECISIONS = [dict(
    id=DEC, question="How are François's (2005) charts of vowel hybridization (Appendix 1, pp. 490-491) entered?",
    chosen_reading="As PNCV > language rows (the 17 Torres and Banks languages and Sakao already sit under PNCV), with five "
                   "implied PNCV retentions of the POc vowels, since François derives the modern vowels from *i e a o u "
                   "through changes that happened separately in each language (pp. 456-457). Each cell *V1(C)V2 > V' is a "
                   "row on the stressed vowel (*V1 > V' / _(C)V2), and each posttonic vowel gets one loss row (*V2 > ∅ "
                   "after the stressed vowels where it is lost) or, where it survives as a final vowel (Hiu, Lo-Toga, "
                   "Vera'a, Mota), a row *V2 > Vf / V1(C)_. Several reflexes in a cell are regular with conditioning "
                   "unknown; angled brackets (adjacent vowels) are rows with the environment '_V2 (adjacent)'. Lo-Toga "
                   "'(i)ɛ' is entered as ɛ and as the diphthong i͡ɛ; Mota '(i)_e' as *i > i and *i > ∅. Vurës and Sakao ü "
                   "are y (Sakao's inventory, Crowley 2002, has y for Guy's ü); Mwotlap ɪ, ʊ are e, o, the symbols of its "
                   "inventory (Lynch et al. 2002). Lehalurup '?' and the empty Nume cell (*u…o) have no rows. Sakao is "
                   "cited as Guy (1977) via François.",
    alternatives="Fusion pairs (*V1 + *V2 > V'); rows against POc on a Torres-Banks node; Table 1 vowel inventories as "
                 "sourced phonemes (they would leave the consonants unsourced).",
    status="open", source_id=S, page="489-491")]

MD = f"""# {BATCH}

François, Alexandre. 2005. Unraveling the history of the vowels of seventeen northern Vanuatu languages. *Oceanic Linguistics* 44(2). 443-504. Read from the Project MUSE PDF the user put in Downloads on 23 November 2026; Table 1 and the charts of Appendix 1 (pp. 490-491) read from page images. Generator: `tools/batch_scripts/new_sources_2026_11_23/francois2005.py`.

## Scope

- Appendix 1: vowel hybridization *V1(C)V2 > V'(C) for Hiu, Lo-Toga, Lehali, Lehalurup (Löyöp), Volow, Mwotlap, Lemerig, Vera'a, Vurës, Mwesen, Mota, Nume, Dorig, Koro, Olrat, Lakon, Mwerlap, and Sakao (after Guy 1977, via François). All 18 lects already existed under PNCV (from François 2011 and Lynch et al. 2002) with *R rows only.
- Five PNCV vowel rows (implied retention) so the rows have parents.
- See decision `{DEC}` for how cells become rows.

## Not entered

- Table 1's vowel inventories (no consonants given, so they cannot be sourced inventories); the vowel length and diphthong developments of §4.3, the asymmetries of word-internal syllables (§5.1), the fate of pretonic vowels (§5.2), morphology (§6) and Appendix 2.
"""

write(BATCH, dict(sources=SOURCES, correspondences=PNCV + rows, decisions=DECISIONS), MD)
