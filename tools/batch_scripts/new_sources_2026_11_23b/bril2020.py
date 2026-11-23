"""Batch bril2020-nc: Bril (2020), consonant evolution in Zuanga-Yuanga and Nêlêmwa-Nixumwak.

Bril, Isabelle. 2020. Processus évolutifs de langues de l'extrême nord de la Nouvelle-Calédonie : le cas
du nêlêmwa-nixumwak et du zuanga-yuanga. Journal de la Société des Océanistes 151. 197-216.
Read from the Cairn PDF in Downloads; Tableaux 7*-11 read from page images at 300 dpi.

Rows are restated against Proto-New Caledonian as the data has it (Ozanne-Rivierre 1992): POc *d > *nd,
*dr > *nḍ, *r > *ṭ, *j > *nj, *c > *s, *ñ and *l > *n, *b > *mb. Bril's own intermediate stage, Proto-North
New Caledonian (pnnc), is not entered (decision bril2020-pnnc).

    python3 tools/batch_scripts/new_sources_2026_11_23b/bril2020.py
"""
from common import write

S = "bril2020"
BATCH = "bril2020-nc"
GOS, BO, NEL, NIX = "thua1237", "juan1250", "nene1250", "nucl1483"

SOURCES = [dict(
    id=S, author="Bril, Isabelle", year="2020",
    title="Processus évolutifs de langues de l'extrême nord de la Nouvelle-Calédonie : le cas du nêlêmwa-nixumwak "
          "et du zuanga-yuanga", url_or_doi="https://doi.org/10.4000/jso.11996", kind="comparative",
    pub_type="article", container_title="Journal de la Société des Océanistes", volume="151", pages="197-216",
    notes="Consulted directly on 23 November 2026 (Cairn PDF; tables read from page images). Data from the "
          "author's fieldwork 1990-2012; Nemi and Jawe from Haudricourt & Ozanne-Rivierre (1982). Varieties: "
          "Zuanga of Kaala-Gomen (gos, dental vs post-alveolar consonants, no final consonants), Zuanga of Paimboa, "
          "Kuru-Wemu and Wehole (pa, wem, weh; 'gon', transitional), Yuanga of Bondé (bo), Nêlêmwa (nel) and "
          "Nixumwak (nix) (pp. 197-198). Vowels and diphthongs (Tableaux 1-3), aspirates from geminates (5a-b, 9), "
          "dentals vs post-alveolars in gos (6), order of changes after Ozanne-Rivierre (1995) (7, 7*), initial, "
          "intervocalic and final consonants (8, 10, 11), summary with PNC and Proto-North NC (12), and reflexes "
          "etymon by etymon (Tableaux 13-37). Written in French; translations here are ours."),
    dict(id="ozannerivierre1995", author="Ozanne-Rivierre, Françoise", year="1995",
         title="Structural changes in the languages of northern New Caledonia", kind="comparative", pub_type="article",
         container_title="Oceanic Linguistics", volume="34", issue="1", pages="45-72",
         notes="Bibliographic details from the reference list of Lynch (2004). Not consulted directly; the source of "
               "the order of changes in Bril (2020: Tableaux 7, 7*).")]

LECTS = [dict(
    id=NEL, name="Nêlêmwa", type="dialect", glottocode="nene1250", parent_id="pnc", language_id="kuma1276",
    latitude="-20.24", longitude="164.03", region="Poum and the far northern islets, New Caledonia",
    notes="Variety of Nêlêmwa-Nixumwak (nel), from Bril's fieldwork (Bril 2020: 197-198). It differs from "
          "Nixumwak by spirantising the aspirated voiceless consonants: nix kʰ, pʰw, pʰ, tʰ, cʰ = nel x/ɣ, fw, f "
          "[ɸ], [β], tʰ/rʰ, ʃ (p. 198). Glottocode from Glottolog 5.4 (Nêlêmwa, a dialect of Nêlêmwa-Nixumwak); "
          "coordinates from the language metadata of Ross et al. (2023), which print the Glottocode with a "
          "character missing (nene125).")]

rows = []
n = 0
SEEN = set()

ASPIRATE = {"kʰ": "kʰ", "xʰ": "x", "θ": "θ", "ð": "ð", "yʰ": "j̊", "h": "h", "ʃ": "ʃ", "tʰ": "tʰ", "rʰ": "r̥",
            "ʈʰ": "ʈʰ", "ɳʰ": "ɳ̊", "nʰ": "n̥", "mʰ": "m̥", "pʰ": "pʰ", "f(h)": "f", "pʰw": "pʰʷ", "fw": "fʷ"}


def c(lects, parent, child, env, page, locator, printed, notes="", status="regular", conditioning=""):
    global n
    for lect in lects:
        key = (lect, parent, child, env, status)
        if key in SEEN:
            continue
        SEEN.add(key)
        n += 1
        rows.append(dict(id=f"{lect}-br20-{n}", child_lect_id=lect, parent_phoneme=parent, child_phoneme=child,
                         environment=env, status=status, conditioning=conditioning, source_id=S, page=page,
                         locator=locator, notes=notes, derivation="composed", as_printed=printed))


def cell(lects, parents, env, page, locator, printed, alts, notes="", once=()):
    """alts: reflexes as IPA; more than one without a condition gets conditioning 'unknown'.
    once: reflexes printed in parentheses (less common): sporadic."""
    main = [a for a in alts if a not in once]
    for p in parents:
        for a in alts:
            if a in once:
                c(lects, p, a, env, page, locator, printed, (notes + " " if notes else "") + "In parentheses: less common.",
                  status="sporadic")
            else:
                c(lects, p, a, env, page, locator, printed, notes, conditioning="unknown" if len(main) > 1 else "")


B = "Prenasalised voiced stops: Bril writes b for [ᵐb] (p. 202: *baya > be [ᵐbe])."
# --- Tableau 8 (p. 202): initial consonants, gos | pa wem bo | nel. (Tableau 7* gives nix-nel as nel here.)
T8, P8 = "Tableau 8", "202"
I = "#_"
cell([GOS, BO, NEL], ["q"], I, P8, T8, "*q > gos k, ø; pa wem bo k, ø; nel k, ø", ["k", "∅"])
cell([GOS, BO, NEL], ["t"], I, P8, T8, "*ṯ > k", ["k"])
cell([GOS, BO, NEL], ["k"], I, P8, T8, "*k > c", ["c"])
cell([NIX], ["k"], I, P8, "Tableau 7*", "*k > nix-nel c, ʃ", ["c", "ʃ"],
     "Nixumwak-Nêlêmwa column of Tableau 7* (after Ozanne-Rivierre 1995); Tableau 8 gives Nêlêmwa c only.")
c([GOS], "s", "t̪", I, P8, T8, "*s, *j > gos t, ⁿd", "Dental in gos, as against post-alveolar ʈ < *d, *r (p. 201).")
c([GOS], "nj", "ⁿd̪", I, P8, T8, "*s, *j > gos t, ⁿd", "Dental in gos (p. 201).")
c([BO, NEL], "s", "t", I, P8, T8, "*s, *j > t, ⁿd")
c([BO, NEL], "nj", "ⁿd", I, P8, T8, "*s, *j > t, ⁿd")
c([GOS], "ṭ", "ʈ", I, P8, T8, "*d, *r > gos ʈ, ⁿɖ", "Post-alveolar in gos only; merged with the dentals elsewhere (p. 201).")
c([GOS], "nd", "ⁿɖ", I, P8, T8, "*d, *r > gos ʈ, ⁿɖ", "Post-alveolar in gos only (p. 201).")
c([BO, NEL], "ṭ", "t", I, P8, T8, "*d, *r > t, ⁿd", "Merged with the reflexes of *s, *j (p. 201).")
c([BO, NEL], "nd", "ⁿd", I, P8, T8, "*d, *r > t, ⁿd", "Merged with the reflexes of *s, *j (p. 201).")
NAS = "POc *n, *ñ and *l are PNC *n (Ozanne-Rivierre 1992); Bril gives them the same reflex (Tableau 8)."
c([GOS], "n", "ɳ", I, P8, T8, "*n̪, *l, *ñ > gos ɳ-", NAS + " Post-alveolar in gos, even where the dental would be expected (p. 202).")
c([BO, NEL], "n", "n", I, P8, T8, "*n̪, *l, *ñ > n-", NAS)
c([GOS, BO, NEL], "ŋ", "∅", I, P8, T8, "*ŋ > ø-")
c([GOS, BO, NEL], "mb", "ᵐb", I, P8, T8, "*b > ᵐb(ʷ)-", "Sometimes rounded: printed ᵐb(ʷ).")
c([GOS, BO, NEL], "mb", "ᵐbʷ", I, P8, T8, "*b > ᵐb(ʷ)-", "Printed ᵐb(ʷ): the rounding is not always present.",
  conditioning="unknown")
cell([GOS, BO, NEL], ["p"], I, P8, T8, "*p > p-, b-", ["p", "ᵐb"], B)
c([GOS, BO, NEL], "pʷ", "pʷ", I, P8, T8, "*pw > pw-")
c([NEL], "pʷ", "w", I, P8, T8, "*pw > nel pw-, w-", conditioning="unknown")

# --- Tableau 9 (p. 203): PNC initial geminates (> aspirates), gos | pa wem bo | nix-nel.
T9, P9 = "Tableau 9", "203"
G9 = [("qq", ["kʰ", "h"], ["h"], ["kʰ", "xʰ", "h"]),
      ("tt", ["kʰ"], ["kʰ"], ["kʰ", "xʰ"]),
      ("kk", ["θ", "ð", "h"], ["ð", "yʰ", "h"], ["yʰ", "ʃ"]),
      ("ss", ["tʰ"], ["tʰ"], ["tʰ", "rʰ"]),
      ("ṭṭ", ["ʈʰ"], ["tʰ"], ["tʰ", "rʰ"]),
      ("nn", ["ɳʰ"], ["nʰ"], ["nʰ"]),
      ("mm", ["mʰ"], ["mʰ"], ["mʰ"]),
      ("pp", ["pʰ"], ["pʰ"], ["pʰ", "f(h)"]),
      ("ppʷ", ["pʰw"], ["pʰw"], ["pʰw", "fw"])]
GNOTE = ("PNC geminates became aspirates in the northern languages; neutralisations are boxed in the table (p. 201, "
         "203). Bril's PNC *ṯṯ is *tt here, and her *ɲɲ and *ll are entered as *nn (PNC *ñ, *l > *n).")
NIXNEL = ("One column for Nixumwak and Nêlêmwa; the second reflex is the Nêlêmwa spirant (nix kʰ, pʰ, tʰ = nel x, f, "
          "rʰ, p. 198).")
for gem, gos, bo, nn in G9:
    pr = f"PNC *{gem} > gos {', '.join(gos)}; pa wem bo {', '.join(bo)}; nix-nel {', '.join(nn)}"
    cell([GOS], [gem], I, P9, T9, pr, [ASPIRATE[a] for a in gos], GNOTE)
    cell([BO], [gem], I, P9, T9, pr, [ASPIRATE[a] for a in bo], GNOTE)
    if len(nn) == 1:
        cell([NIX, NEL], [gem], I, P9, T9, pr, [ASPIRATE[nn[0]]], GNOTE)
    else:
        c([NIX], gem, ASPIRATE[nn[0]], I, P9, T9, pr, GNOTE + " " + NIXNEL)
        for a in nn[1:]:
            c([NEL], gem, ASPIRATE[a], I, P9, T9, pr, GNOTE + " " + NIXNEL)
        if gem == "qq":
            c([NIX, NEL], gem, "h", I, P9, T9, pr, GNOTE + " h outside the box: both varieties.", conditioning="unknown")

# --- Tableau 10 (p. 203): intervocalic consonants, gos | pa-bo | nix-nel.
T10, P10, V = "Tableau 10", "203", "V_V"
NN = [NIX, NEL]
cell([GOS, BO] + NN, ["q"], V, P10, T10, "*q > -ɣ-, -ø-", ["ɣ", "∅"])
cell([GOS, BO], ["k"], V, P10, T10, "*k > gos, pa-bo -c-, -j-, -ø-", ["c", "j", "∅"])
cell(NN, ["k"], V, P10, T10, "*k > nix-nel -j-, -ø-", ["j", "∅"])
cell([GOS] + NN, ["t"], V, P10, T10, "*ṯ > -ᵑɡ-, -ɣ-, -ø-", ["ᵑɡ", "ɣ", "∅"])
cell([BO], ["t"], V, P10, T10, "*ṯ > pa-bo -ᵑɡ-, -ø-", ["ᵑɡ", "∅"])
SJ = ("The prenasalised reflex (in parentheses, less common) is taken to continue *j (PNC *nj), the other *s; gos "
      "keeps the laminals apart from *d, *r, pa-bo and nix-nel do not (p. 203).")
c([GOS], "s", "ð", V, P10, T10, "*s, *j > gos -ð-, (-ⁿd-)", SJ)
c([BO], "s", "l", V, P10, T10, "*s, *j > pa-bo (-ⁿd-), -l-", SJ)
c(NN, "s", "r", V, P10, T10, "*s, *j > nix-nel (-ⁿd-), -r-", SJ + " Nêlêmwa keeps -r- (< *s, *j) apart from -l- (< *d, *r).")
c([GOS, BO] + NN, "nj", "ⁿd", V, P10, T10, "*s, *j > (-ⁿd-)", SJ)
DR = "Bril does not say which of the two continues *d and which *r; both are entered for both."
for p in ("ṭ", "nd"):
    for a in ("ɽ", "l"):
        c([GOS], p, a, V, P10, T10, "*d, *r > gos -ɽ-, -l-", DR + " gos ɽ: the post-alveolar trill/flap, written ŗ.",
          conditioning="unknown")
    c([BO] + NN, p, "l", V, P10, T10, "*d, *r > -l-")
c([GOS, BO], "n", "n", V, P10, T10, "*l > gos, pa-bo -n-, -ø-; *ŋ > -n-, -ø-", "PNC *n from POc *l (and *ñ, *n).",
  conditioning="unknown")
c([GOS], "n", "ɳ", V, P10, T10, "*n̪ > gos -ɳ-, (-n-), -ø-; *ñ > gos -ɳ-", "From POc *n and *ñ; *l gives -n- (p. 203).",
  conditioning="unknown")
c([GOS, BO] + NN, "n", "∅", V, P10, T10, "*l, *n̪ > -ø-", "Lost in some words.", conditioning="unknown")
c(NN, "n", "l", V, P10, T10, "*l, *n̪, *ñ, *ŋ > nix-nel -l-, -ø-",
  "The nasals became l in nix-nel after nasalising the neighbouring vowels, so this l is 'nasal' (p. 203).",
  conditioning="unknown")
c([GOS, BO], "ŋ", "n", V, P10, T10, "*ŋ > -n-, -ø-", "Merged with the reflex of *n, *l.", conditioning="unknown")
c([GOS, BO] + NN, "ŋ", "∅", V, P10, T10, "*ŋ > -ø-", conditioning="unknown")
c(NN, "ŋ", "l", V, P10, T10, "*ŋ > nix-nel -l-, -ø-", "'Nasal' l (p. 203).", conditioning="unknown")
c([GOS, BO] + NN, "mb", "ᵐb", V, P10, T10, "*b > -ᵐb(ʷ)-", "Sometimes rounded.")
c([GOS], "p", "p", V, P10, T10, "*p > gos -p-, -β-", "Voiceless intervocalic consonants are heard from older speakers only (n. 18).",
  conditioning="unknown")
c([GOS], "p", "β", V, P10, T10, "*p > gos -p-, -β-", "Printed ß.", conditioning="unknown")
for a in ("p", "v", "∅"):
    c([BO], "p", a, V, P10, T10, "*p > pa-bo -p-, -v-, ø", conditioning="unknown")
for a in ("ᵐb", "v", "∅"):
    c(NN, "p", a, V, P10, T10, "*p > nix-nel -ᵐb-, -v-, ø", conditioning="unknown")
c([GOS], "pʷ", "ᵐbʷ", V, P10, T10, "*pw > gos -bw-, -β-", B, conditioning="unknown")
c([GOS], "pʷ", "β", V, P10, T10, "*pw > gos -bw-, -β-", "Printed ß; merged with the lenis reflex of *p.", conditioning="unknown")
c([BO] + NN, "pʷ", "ᵐbʷ", V, P10, T10, "*pw > -bw-", B)

# --- Tableau 11 (p. 204): final consonants, gos | pa-bo | nix-nel. gos has lost every final consonant.
T11, P11, F = "Tableau 11", "204", "_#"
LATE = ("In parentheses: a final consonant that continues an intervocalic consonant of the etymon, final after the "
        "loss of the final vowel (n. 22).")
for p in ("q", "k", "t", "s", "nj", "ṭ", "nd", "n", "ŋ", "m", "p"):
    c([GOS], p, "∅", F, P11, T11, f"*-{p} > gos -ø", "Zuanga of Kaala-Gomen has lost all final consonants (pp. 197, 204).")
cell([BO], ["q", "k"], F, P11, T11, "*-q, *-k > pa-bo -ø", ["∅"])
cell(NN, ["q"], F, P11, T11, "*-q > nix-nel -k, -ø", ["k", "∅"], "*-q and *-k neutralised as -k in nel (p. 204).")
cell(NN, ["k"], F, P11, T11, "*-k > nix-nel -k, -c", ["k", "c"], "*-q and *-k neutralised as -k in nel (p. 204).")
c([BO], "t", "∅", F, P11, T11, "*-ṯ > pa-bo -ø, (-c)")
c([BO], "t", "c", "_V#", P11, T11, "*-ṯ > pa-bo -ø, (-c)", LATE)
c(NN, "t", "k", F, P11, T11, "*-ṯ > nix-nel -k")
for p in ("s", "nj", "ṭ", "nd"):
    cell([BO], [p], F, P11, T11, "*-s, *-j, *-d (*r) > pa-bo -l, -ø", ["l", "∅"], "*s, *j, *d and *r merged finally (p. 204).")
    cell(NN, [p], F, P11, T11, "*-s, *-j, *-d (*r) > nix-nel -t, -ø", ["t", "∅"], "*s, *j, *d and *r merged finally (p. 204).")
for p, extra in (("n", ["n"]), ("ŋ", ["n", "ŋ"]), ("m", ["m"]), ("p", [])):
    targets = [BO] + NN if p != "p" else NN
    c([BO] + NN if p != "p" else [BO] + NN, p, "∅", F, P11, T11, f"*-{p} > -ø",
      "The nasals are generally lost finally (p. 204)." if p != "p" else "")
    for a in extra if p != "p" else ["p"]:
        c(targets, p, a, "_V#", P11, T11, f"*-{p} > (-{a})", LATE)

DECISIONS = [
    dict(id="bril2020-pnnc", question="Bril (2020) gives the reflexes with an intermediate Proto-North New "
         "Caledonian (PNNC, after Ozanne-Rivierre 1995), where PNC *k > *c, *q > *k, *ṯ > *t (Ext. north k), *s > "
         "*t̪ (Tableaux 7, 12). Is a PNNC node entered?",
         chosen_reading="No: the rows are restated against PNC as the data has it (Ozanne-Rivierre 1992), and the "
                        "northern languages stay under PNC; Nemi, Jawe, Pije and Fwâi, which PNNC would also cover, "
                        "are under PNC too. Bril's columns are entered on Gomen Yuanga (gos), Bondé Yuanga (the "
                        "pa-bo and 'pa wem bo' columns, so Paimboa is not entered as a separate lect), Nêlêmwa (new) "
                        "and Kumak (Nixumwak: the nix-nel columns of Tableaux 9-11 and 7*). The Nemi column is not "
                        "entered (from Haudricourt & Ozanne-Rivierre 1982, already in the data).",
         alternatives="Add PNNC under PNC with the four changes of Tableau 7 and move the northern lects under it; "
                      "add Paimboa Zuanga (gon) as a lect with the pa-bo rows.",
         status="open", source_id=S, page="201-204"),
    dict(id="bril2020-vowels", question="Bril's vowel and diphthong correspondences (Tableaux 1-3: *u > i, e; *ai > "
         "e, ɛ, ɨ, i; *au, *ua, *ia > ɔ in Zuanga-Yuanga): enter them?",
         chosen_reading="Not entered: PNC has no vowels in the data (its inventory is consonants only), so vowel "
                        "rows against it would fail the inventory check.",
         alternatives="Give PNC its POc vowels (inherit) and enter Tableaux 1-2 as rows.",
         status="open", source_id=S, page="199-200"),
]

MD = f"""# {BATCH}

Bril, Isabelle. 2020. Processus évolutifs de langues de l'extrême nord de la Nouvelle-Calédonie : le cas du nêlêmwa-nixumwak et du zuanga-yuanga. *Journal de la Société des Océanistes* 151. 197-216. Generator: `tools/batch_scripts/new_sources_2026_11_23b/bril2020.py`.

## Scope

- Consonants, restated against PNC: initial (Tableau 8, with 7* for Nixumwak *k), PNC geminates > aspirates (Tableau 9), intervocalic (Tableau 10), final (Tableau 11).
- Lects: Gomen Yuanga (gos), Bondé Yuanga (pa-bo), new Nêlêmwa (nel), Kumak (nix).
- Reflexes with no stated condition: conditioning unknown; reflexes in parentheses: less common (sporadic) in Tableau 10, final after vowel loss (_V#) in Tableau 11.

## Not entered

- Vowels and diphthongs (decision `bril2020-vowels`), PNNC (decision `bril2020-pnnc`), the Nemi column, Tableau 12 (a summary of 8-11), the etymon tables 13-37.

## Decisions (open)

- `bril2020-pnnc`, `bril2020-vowels`.
"""

write(BATCH, dict(sources=SOURCES, lects=LECTS, correspondences=rows, decisions=DECISIONS), MD)
