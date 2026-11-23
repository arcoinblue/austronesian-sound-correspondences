"""Batch barlowross2025-tomoip: Barlow & Ross (2025), the historical phonology of Tomoip.

Barlow, Russell & Malcolm Ross. 2025. The position of Tomoip in the Oceanic family. Oceanic
Linguistics 64(2). 322-379. Read from the Project MUSE PDF in Downloads (Tables 1-5 checked against
page images).

    python3 tools/batch_scripts/new_sources_2026_11_23b/barlow2025.py
"""
from common import write

S = "barlowross2025"
BATCH = "barlowross2025-tomoip"
L = "tomo1244"

SOURCES = [dict(
    id=S, author="Barlow, Russell; Ross, Malcolm", year="2025", title="The position of Tomoip in the Oceanic family",
    url_or_doi="https://doi.org/10.1353/ol.2025.a974305", kind="comparative", pub_type="article",
    container_title="Oceanic Linguistics", volume="64", issue="2", pages="322-379",
    notes="Consulted directly on 23 November 2026 (Project MUSE PDF; tables checked against page images). "
          "Canonical-form changes (§3: final consonant deletion, antepenultimate vowel deletion, penultimate "
          "vowels coloured by the lost final vowel, Tables 1-2), POc consonants in Tomoip (§4, summary Table 3, "
          "p. 351-352), the split of *p and of merged *k/*q shared with Proto-New Ireland (Tables 4-5, pp. "
          "356-357), pronouns and class terms (§5.2.2), loans from Kol and Sulka (appendix). Proposes "
          "Proto-Tomoip-New Ireland, with Tomoip coordinate to Proto-New Ireland (Figure 2).")]

LECTS = [dict(
    id=L, name="Tomoip", alt_names="Tomoyp; Tumuip; Tmuip", type="language", glottocode="tomo1244", iso639_3="tqp",
    parent_id="poc", latitude="-5.31", longitude="151.83", region="Pomio and Talasea districts, New Britain, Papua New Guinea",
    orthography_note="Barlow & Ross write IPA (β, ʝ, ŋ).",
    notes="Oceanic language of New Britain, once thought non-Austronesian; about 23 percent of a 1,050-item wordlist "
          "is identified as Oceanic (Barlow & Ross 2025: 323). Barlow & Ross place it with the New Ireland languages "
          "under a proposed Proto-Tomoip-New Ireland, sharing the split of POc *p into *p and *v and the merger of "
          "*k and *q followed by a split into *k and *ɣ (pp. 355-358); Ross (1988: 258) had derived Tomoip from New "
          "Ireland. Neither node is entered (decision barlowross2025-tree), so the parent is POc. Glottocode, ISO "
          "code and coordinates from the language metadata of Ross et al. (2023)."),
]

rows = []
n = 0


def c(parent, child, env, page, notes="", status="regular", conditioning="", lexical="", as_printed="", locator="Table 3",
      examples="", count=""):
    global n
    n += 1
    rows.append(dict(id=f"tomo-br25-{n}", child_lect_id=L, parent_phoneme=parent, child_phoneme=child,
                     environment=env, status=status, conditioning=conditioning, lexical_scope=lexical,
                     source_id=S, page=page, locator=locator, notes=notes, as_printed=as_printed,
                     examples=examples, evidence_count=count))


FORTIS = ("Two reflexes of each voiceless obstruent, unlenited and lenis, as in many Western Oceanic languages; the "
          "split has not spread through the whole lexicon and has no stated condition (p. 340). Lenis reflexes do "
          "not occur word-finally.")
T3 = "351-352"

# Labials
c("p", "p", "elsewhere", T3, FORTIS, conditioning="lexical", lexical="unlenited reflex", as_printed="*p > p")
c("p", "b", "#_, before n", T3, "Initial b- before /n/ (Table 3).", as_printed="*p > b- (before /n/)")
c("p", "β", "elsewhere", T3, FORTIS + " The lenis reflex is much less frequent (p. 340).", conditioning="lexical",
  lexical="lenis reflex", as_printed="*p > β (lenis)")
c("p", "∅", "_o, _u", T3, "Lenis reflex, lost before the rounded vowels (p. 340).", lexical="lenis reflex",
  as_printed="*p > Ø/_o,u (lenis)")
c("b", "b", "elsewhere", T3, as_printed="*b > b")
c("bʷ", "b", "elsewhere", T3, "The labiovelars merged with the plain labials (p. 339).", as_printed="*bʷ > b")
c("mʷ", "m", "elsewhere", T3, "Merged with *m; the old rounding sometimes survives as a following u, printed 'mu' "
  "in Table 3 (p. 339).", as_printed="*mʷ > m, mu", examples="*mʷapo(q) 'taro' > muop; *mʷaRuqane 'man' > muor 'person'")
c("w", "u", "#_", T3, "Word-initial *w- becomes u- (p. 341).", as_printed="*w > u, β",
  examples="*na waiR > n-uʝe 'water'; *wasa > uʝe 'Abelmoschus manihot'")
c("w", "β", "elsewhere", T3, as_printed="*w > u, β")
# Coronals
c("t", "t", "#_", T3, as_printed="*t > t-")
c("t", "d", "#_, before n", T3, "Printed (n)d-: some nouns have d- or nd- (p. 342).", as_printed="*t > (n)d- (before /n/)",
  examples="*tasik > nde 'sea'; *tanoq > ndan 'earth'")
c("t", "t", "V_a, V_e, V_o, V_u", T3, "Medial *t before vowels other than *i (p. 342).", as_printed="*t > -t-/a,e,o,u")
c("t", "s", "V_i", T3, as_printed="*t > -s-/_i")
c("t", "d", "V_i, V_e", T3, "Table 3 gives -d- before i and e, the text before *e only (p. 342).",
  as_printed="*t > -d-/_i,e")
c("t", "r", "V_V#", T3, "Final after the loss of the final vowel.", as_printed="*t > -r", examples="*patu > per 'stone'; *mate > mer 'die'")
for p in ("s", "c", "j"):
    merged = "" if p == "s" else f" Table 3: *{p} merged with *s."
    c(p, "t", "elsewhere", T3, FORTIS + " The unlenited reflex of *s merged with *t." + merged, conditioning="lexical",
      lexical="unlenited reflex", as_printed=f"*{p} > (merged with *s); *s > (merged with *t)")
    c(p, "∅", "elsewhere", T3, FORTIS + merged, conditioning="lexical", lexical="lenis reflex",
      as_printed=f"*{p} > (merged with *s); *s > Ø (lenis)")
c("dr", "r", "elsewhere", T3, "*d and *dr merged, as throughout Western Oceanic (p. 345).", as_printed="*dR > r")
c("d", "r", "elsewhere", T3, "Merged with *dr; one example (p. 345).", as_printed="*d > (merged with *dr)")
c("l", "l", "elsewhere", T3, as_printed="*l > l")
c("l", "ʝ", "u_", T3, "After *u; then lost word-finally (p. 345).", as_printed="*l > ʝ/u_")
for ch in ("r", "l", "∅"):
    c("R", ch, "conditions unknown", T3, "Three reflexes with no stated condition.", conditioning="unknown",
      as_printed="*R > r, l, Ø")
    c("r", ch, "conditions unknown", T3, "Table 3: '*r (merged with *R ?)', with a question mark.",
      conditioning="unknown", status="disputed", as_printed="*r > (merged with *R ?)")
c("m", "m", "elsewhere", T3, as_printed="*m > m")
c("n", "n", "elsewhere", T3, as_printed="*n > n")
c("ñ", "n", "elsewhere", T3, "Only in the suffix -n '3SG.POSS' < *-ña (p. 348).", as_printed="*ñ > (merged with *n)")
c("ŋ", "ŋ", "elsewhere", T3, as_printed="*ŋ > ŋ")
c("y", "ʝ", "elsewhere", T3, "Few reflexes; ʝo '1SG' < *iau is the one certain case (p. 349).", as_printed="*y > ʝ")
# Dorsals: *k, *kʷ, *q merged, then split into k and h (p. 349).
for p in ("k", "kʷ", "q"):
    merged = "" if p == "k" else f" *{p} merged with *k (Table 3)."
    pr = f"*{p} > (merged with *k)" if p != "k" else "*k > k; h-h-Ø"
    c(p, "k", "elsewhere", T3, "*k, *kʷ and *q merged, then split into k and the lenis h (p. 349)." + merged,
      conditioning="lexical", lexical="unlenited reflex", as_printed=pr)
    c(p, "h", "#_, V_V", T3, "Lenis reflex, initial and medial (printed h-h-Ø)." + merged, conditioning="lexical",
      lexical="lenis reflex", as_printed=pr)
    c(p, "∅", "_#", T3, "Lenis reflex, final (printed h-h-Ø)." + merged, lexical="lenis reflex", as_printed=pr)
c("ɡ", "k", "elsewhere", T3, "Two examples (p. 351).", as_printed="*g > k")

# Canonical form (§3).
for p in ("p", "t", "k", "q", "s", "c", "m", "n", "ŋ", "l", "r", "R"):
    c(p, "∅", "_#", "330", "Final consonant deletion, the earliest change after POc (§3.1); a Tomoip form that keeps "
      "a POc final consonant is a loan (p. 330).", locator="§3.1", as_printed="final consonant deletion")
for v in ("a", "e", "i", "o", "u"):
    c(v, "∅", "_#", "330-332", "The final vowels left by final consonant deletion were also lost, after colouring "
      "the penultimate vowel (§3.3).", locator="§3.3", as_printed="final vowel deletion")
    c(v, "∅", "antepenultimate syllable of a trisyllable", "331", "Antepenultimate vowel deletion in trisyllables "
      "(and in roots with a monosyllabic possessor suffix); *qatoluR > hotel is an exception (§3.2).",
      locator="§3.2", as_printed="antepenultimate vowel deletion")

# Table 1 (p. 332): penultimate vowel outcomes by final vowel. The header prints -a -e -e -i -u; the cells
# fit -a -e -i -o -u (checked against Table 2), so they are read that way (decision barlowross2025-table1).
T1 = {
    ("a", "a"): "a, e, (u)", ("a", "e"): "e", ("a", "i"): "a, e, (i)", ("a", "o"): "a, (o)", ("a", "u"): "o",
    ("e", "e"): "(u)",
    ("i", "a"): "(e)", ("i", "i"): "(e), i", ("i", "o"): "(u)", ("i", "u"): "u",
    ("o", "e"): "(i, o)", ("o", "i"): "(e)", ("o", "o"): "o", ("o", "u"): "e",
    ("u", "a"): "(e, o, u)", ("u", "i"): "i, (o, u)", ("u", "u"): "e, i, u",
}
for (pen, fin), cell in T1.items():
    once = set()
    if "(" in cell:
        inner = cell[cell.index("(") + 1:cell.index(")")]
        once = {x.strip() for x in inner.split(",")}
    outs = [x.strip(" ()") for x in cell.replace("(", "").replace(")", "").split(",")]
    many = [o for o in outs if o not in once]
    for o in outs:
        single = o in once
        c(pen, o, f"_C{fin}#", "332", "Penultimate vowel before a final *" + fin + " (lost later), Table 1. "
          + ("Attested once (in parentheses)." if single else
             "Most frequent outcome in this cell." if len(many) == 1 else "One of several outcomes, no condition stated."),
          status="sporadic" if single else "regular", conditioning="unknown" if (not single and len(many) > 1) else "",
          count="1" if single else "", locator="Table 1", as_printed=f"*{pen}C{fin} : {cell}")

DECISIONS = [
    dict(id="barlowross2025-tree", question="Barlow & Ross (2025) propose Proto-Tomoip-New Ireland, with Tomoip and "
         "Proto-New Ireland as coordinate branches; Ross (1988) derived Tomoip from New Ireland. Are the nodes entered?",
         chosen_reading="No: Tomoip is entered under POc with POc > Tomoip rows (Table 3). No New Ireland language and "
                        "no Western Oceanic or Meso-Melanesian node is in the data, so a PTMNI or PNI node would have "
                        "no other daughters. Its innovations (*p > *p, *v; *k, *q > *k > *k, *ɣ) are in the lect notes.",
         alternatives="Add Proto-Tomoip-New Ireland (and Proto-New Ireland) under POc with the split rows of Tables 4-5, "
                      "and Tomoip under it.",
         status="open", source_id=S, page="323-324, 352-358"),
    dict(id="barlowross2025-table1", question="Table 1 (p. 332) prints the final-vowel header as -a -e -e -i -u.",
         chosen_reading="Read as -a -e -i -o -u: the cells match Table 2 that way (*aCi > a, e, i; *aCo > a, o; "
                        "*iCo > u).",
         alternatives="", status="open", source_id=S, page="332-333"),
]

MD = f"""# {BATCH}

Barlow, Russell & Malcolm Ross. 2025. The position of Tomoip in the Oceanic family. *Oceanic Linguistics* 64(2). 322-379. Generator: `tools/batch_scripts/new_sources_2026_11_23b/barlow2025.py`.

## Scope

- New lect Tomoip (`tomo1244`) under POc.
- POc consonants > Tomoip from Table 3 (pp. 351-352), with the unlenited and lenis reflexes as lexical; mergers entered with the reflexes of the phoneme merged into.
- Canonical form: final consonant deletion, final vowel deletion, antepenultimate vowel deletion (§§3.1-3.3).
- Penultimate vowels by the following (lost) final vowel, Table 1 (p. 332); outcomes attested once as sporadic.

## Not entered

- Tables 4-5 (Tomoip compared with Proto-New Ireland) and the PTMNI node (decision `barlowross2025-tree`); morphology; the loans of the appendix.
- No inventory: none is given; it is generated from the rows.

## Decisions (open)

- `barlowross2025-tree`, `barlowross2025-table1`.
"""

write(BATCH, dict(sources=SOURCES, lects=LECTS, correspondences=rows, decisions=DECISIONS), MD)
