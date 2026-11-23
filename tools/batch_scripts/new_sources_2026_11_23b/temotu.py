"""Batches for the Temotu languages:

- rossnaess2007-temotu: Ross & Næss (2007), Table 2 (POc consonants in nine Temotu languages, p. 463) and the
  innovations of §2.2-2.4; the Temotu nodes and six new languages.
- lackeyboerger2021-temotu: Lackey & Boerger (2021), the changes of Proto-Temotu (Table 4), Proto-Reefs-Santa
  Cruz (Table 2) and Proto-Vanikoro (Table 3, with the ordered changes of (103)); the Proto-Vanikoro node.
- francois2009-vanikoro: François (2009), Proto-Vanikoro innovations and the lenis reflexes of *t (Table 3).

Ross, Malcolm & Åshild Næss. 2007. An Oceanic origin for Äiwoo, the language of the Reef Islands?
Oceanic Linguistics 46(2). 456-498. (JSTOR scan; Table 2 read from a page image at 400 dpi.)
Lackey, William James & Brenda H. Boerger. 2021. Reexamining the phonological history of Oceanic's Temotu
subgroup. Oceanic Linguistics 60(2). 367-411. (Project MUSE PDF; tables and Figure 1 from page images.)
François, Alexandre. 2009. The languages of Vanikoro: Three lexicons and one grammar. In Bethwyn Evans
(ed.), Discovering history through language: Papers in honour of Malcolm Ross, 103-126. Canberra: Pacific
Linguistics. (Author's PDF, paginated 1-24; pages cited as in that PDF.)

Tree (decision temotu-tree): Proto-Temotu under POc, with Proto-Reefs-Santa Cruz and Proto-Utupua below it,
which every classification has; the Vanikoro languages directly under Proto-Temotu, with Proto-Vanikoro
(Lackey & Boerger 2021, François 2009) and Proto-Utupua-Vanikoro (Ross & Næss 2007) as proposed parents.

    python3 tools/batch_scripts/new_sources_2026_11_23b/temotu.py
"""
from common import write

RN, LB, F9 = "rossnaess2007", "lackeyboerger2021", "francois2009"
T2 = "463"

SOURCES_RN = [dict(
    id=RN, author="Ross, Malcolm; Næss, Åshild", year="2007",
    title="An Oceanic origin for Äiwoo, the language of the Reef Islands?", url_or_doi="https://doi.org/10.1353/ol.2008.0003",
    kind="comparative", pub_type="article", container_title="Oceanic Linguistics", volume="46", issue="2", pages="456-498",
    notes="Consulted directly on 23 November 2026 (JSTOR scan; the text layer garbles the symbols, so Table 2 was read "
          "from a page image). Numerals (Table 1), reflexes of POc consonants in Äiwoo, Natügu, Nagu (Engdewu), "
          "Nebao, Asuboa, Tanibili, Buma (Teanu), Vano (Lovono) and Tanema (Table 2, p. 463), canonic forms: final "
          "consonants and paragogic vowels, truncation and syncope in RSC (§2.2), multiple reflexes: diphthongization, "
          "fortis and lenis initials, Tanibili *t (§2.3), subgrouping: Temotu as a primary subgroup of Oceanic, "
          "RSC, Utupua-Vanikoro, Utupua (§2.4, pp. 470-473); Äiwoo morphosyntax (§3). Data re-studied from Tryon "
          "& Hackman (1983) and from Næss and Boerger. DOI as given by Project MUSE for this issue."),
    dict(id="tryonhackman1983", author="Tryon, Darrell T.; Hackman, B. D.", year="1983",
         title="Solomon Islands languages: An internal classification", kind="comparative", pub_type="book",
         place="Canberra", publisher="Pacific Linguistics",
         notes="Bibliographic details from the reference list of Lackey & Boerger (2021). Not consulted directly: "
               "the wordlists behind Ross & Næss's (2007) Table 2 and the Utupua data of Lackey & Boerger (2021).")]

SOURCES_LB = [dict(
    id=LB, author="Lackey, William James; Boerger, Brenda H.", year="2021",
    title="Reexamining the phonological history of Oceanic's Temotu subgroup", url_or_doi="https://doi.org/10.1353/ol.2021.0020",
    kind="comparative", pub_type="article", container_title="Oceanic Linguistics", volume="60", issue="2", pages="367-411",
    notes="Consulted directly on 23 November 2026 (Project MUSE PDF). Sources (Table 1), tree (Figure 1, p. 370), RSC "
          "consonant changes (§3, Table 2, p. 376), syncope and truncation from POc stress (§4), Vanikoro changes in "
          "order (§5, (103), Table 3, p. 388), the Proto-Temotu merger of *s, *c, *j (§6.1, Table 4, p. 389), "
          "rejection of Utupua-Vanikoro (§6.2), archaeology (§7), RSC wordlist (appendix A), *a in RSC (appendix B). "
          "RSC orthography: ä [æ], â [ɔ], ü [y], ö [ø], ë [ə], y [j], j [dʒ], ng [ŋ]; voiced stops prenasalised "
          "(p. 369).")]

SOURCES_F9 = [dict(
    id=F9, author="François, Alexandre", year="2009", title="The languages of Vanikoro: Three lexicons and one grammar",
    kind="comparative", pub_type="chapter",
    container_title="Discovering history through language: Papers in honour of Malcolm Ross", editors="Bethwyn Evans",
    pages="103-126", place="Canberra", publisher="Pacific Linguistics",
    notes="Consulted directly on 23 November 2026 in the author's PDF (paginated 1-24; pages cited as in that PDF, "
          "e.g. Table 3 on p. 9). Oceanic reflexes in Teanu, Lovono and Tanema (Table 1), Proto-Vanikoro innovations: "
          "paragogic vowel, *t > k before u, lexical innovations (Table 2, pp. 5-6), regular correspondences such as "
          "the lenis reflexes of *t (Table 3, p. 9) and Teanu b : Lovono m : Tanema b (Table 4, p. 10), lexical "
          "divergence and structural isomorphism (§§2-4). The three languages share one inventory of five vowels and "
          "19 consonants (n. 7). Volume details from the reference list of Lackey & Boerger (2021).")]

PTM, PRSC, PUT, PUV, PVK = "ptm", "prsc", "putupua", "puv", "pvanikoro"
AIW, NAT, NAG = "ayiw1239", "natu1246", "nang1262"
NEB, ASU, TNB = "amba1266", "asum1237", "tani1255"
BUM, VNO, TNM = "tean1237", "vano1237", "tane1237"

TREE = ("Tree after decision temotu-tree: subgroups that both Ross & Næss (2007) and Lackey & Boerger (2021) accept "
        "are in the main tree.")
LECTS_RN = [
    dict(id=PTM, name="Proto-Temotu", alt_names="PTm; PTM; Temotu", type="proto-language", glottocode="temo1244",
         parent_id="poc",
         notes="Ancestor of the Oceanic (non-Polynesian) languages of Temotu Province, Solomon Islands: Reefs-Santa "
               "Cruz, Utupua and Vanikoro. A primary subgroup of Oceanic, not part of any other known subgroup "
               "(Ross & Næss 2007: 471), defined by the merger of POc *r and *l as *l (pp. 471-472) and of *s, *c and "
               "*j as *s (Lackey & Boerger 2021: 388-389), and by the loss of the initial consonant in three etyma "
               "(*Rumwaq, *lima, *ñamuk; Ross & Næss 2007: 472). Conservative: it kept POc final consonants (Ross & "
               "Næss 2007: 464), POc prosody, *k apart from *q and perhaps *ñ apart from *n (Lackey & Boerger 2021: "
               "370, 393); *q was perhaps lenited to a fricative (x or χ) that later languages restored or lost (p. "
               "390). Whether a Proto-Temotu node is needed at all has been doubted (François, p.c. in Lackey & "
               "Boerger 2021: 370). Glottocode temo1244 (Temotu).",
         inherit="assumed-unchanged", inherit_source_id=LB, inherit_page="370",
         inherit_note="Unchanged: Proto-Temotu was conservative, 'possibly trivially close to POC in structure' "
                      "(Lackey & Boerger 2021: 370)."),
    dict(id=PRSC, name="Proto-Reefs-Santa Cruz", alt_names="PRSC; Proto-RSC", type="proto-language", glottocode="reef1242",
         parent_id=PTM,
         notes="Äiwoo (Reef Islands) and the Santa Cruz languages Natügu, Nalögo, Noipä and Engdewu (Nagu). Defined by "
               "truncation of the final syllable of nouns and by syncope (Ross & Næss 2007: 465-467), which Lackey & "
               "Boerger (2021: 376-382) derive from POc stress, and by loss of initial *t- in *taŋis (Ross & Næss 2007: "
               "473). Lackey & Boerger (2021: 370) also have a Santa Cruz node (Engdewu, Nalögo, Noipä, Natügu), not "
               "entered. " + TREE,
         inherit="assumed-unchanged", inherit_source_id=LB, inherit_page="376"),
    dict(id=PUT, name="Proto-Utupua", alt_names="Utupua", type="proto-language", glottocode="utup1238", parent_id=PTM,
         alt_parents=f"{PUV}:{RN}",
         notes="Nebao (Amba), Asuboa (Asumboa) and Tanibili (Tanimbili). Defined by the loss of POc word-final *-r, "
               "*-s, *-q and *-R and the complete loss of *R (Ross & Næss 2007: 473), and the loss of *s (with *c, *j) "
               "between vowels (Lackey & Boerger 2021: 388). Ross & Næss put it under Utupua-Vanikoro; Lackey & Boerger "
               "directly under Proto-Temotu. " + TREE,
         inherit="assumed-unchanged", inherit_source_id=RN, inherit_page="473"),
    dict(id=PUV, name="Proto-Utupua-Vanikoro", alt_names="PUV; Utupua-Vanikoro", type="proto-language",
         glottocode="utup1237", parent_id=PTM,
         notes="Ross & Næss's (2007: 473) subgroup of the Utupua and Vanikoro languages, with four branches (Utupua, "
               "Buma, Vano, Tanema), defined by the loss of nonfinal POc *q (weak evidence, as Santa Cruz shares it) and "
               "by the diphthongization of final schwa, which cuts across the two islands (pp. 468-469). Lackey & "
               "Boerger (2021: 389-392) reject it; it has no daughters in the main tree (decision temotu-tree).",
         inherit="assumed-unchanged", inherit_source_id=RN, inherit_page="473"),
]
for lid, name, alt, gc, iso, par, lat, lon, reg, extra in [
        (AIW, "Äiwoo", "Aiwo; Ayiwo; Reefs; Aiw", "ayiw1239", "nfl", PRSC, "-10.28", "166.33", "Reef Islands",
         "Data from Næss's fieldwork (Ross & Næss 2007: 459). Practical orthography: ny = /ɲ/, ng = /ŋ/; /n/~/ɲ/, "
         "/t/~/s/ and /d/~/j/ are neutralised before /i/ (p. 461)."),
        (NAT, "Natügu", "Santa Cruz; Nat", "natu1246", "ntu", PRSC, "-10.69", "165.87", "Santa Cruz (Nendö)",
         "Data from Wurm's lists and Boerger (Ross & Næss 2007: 459)."),
        (NAG, "Engdewu", "Nagu; Nanggu; Nag", "nang1262", "ngr", PRSC, "", "", "Santa Cruz (Nendö)",
         "Engdewu was formerly called Nagu or Nanggu (Lackey & Boerger 2021: 369)."),
        (NEB, "Nebao", "Amba; Aba; Neb", "amba1266", "utp", PUT, "-11.30", "166.50", "Utupua",
         "Data from Tryon & Hackman (1983) (Ross & Næss 2007: 459; Lackey & Boerger 2021: 368). Nebao nh is the "
         "regular reflex of *pVn- (Ross & Næss 2007: 469)."),
        (ASU, "Asumboa", "Asuboa; Asu", "asum1237", "aua", PUT, "-11.30", "166.50", "Utupua",
         "Data from Tryon & Hackman (1983). Ross & Næss (2007: 471) write Asumboa; Table 2 has Asu."),
        (TNB, "Tanimbili", "Tanibili; Tnb", "tani1255", "tbe", PUT, "-11.30", "166.51", "Utupua",
         "Data from Tryon & Hackman (1983). Its reflexes of *t are analysed in Ross & Næss (2007: 470).")]:
    LECTS_RN.append(dict(
        id=lid, name=name, alt_names=alt, type="language", glottocode=gc, iso639_3=iso, parent_id=par,
        latitude=lat, longitude=lon, region=reg + ", Temotu Province, Solomon Islands",
        orthography_note="Ross & Næss write the prenasalised stops b, d, g and the RSC vowels as in the practical "
                         "orthographies; reflexes here are in IPA, with source_form where they differ.",
        notes=extra + " Glottocode, ISO code and coordinates from the language metadata of Ross et al. (2023)"
              + (" (no coordinates there)." if not lat else "."),
        inherit="assumed-unchanged", inherit_source_id=RN, inherit_page=T2,
        inherit_note="Unchanged: Table 2 gives the other consonants as the parent's; the vowels, which Ross & Næss "
                     "call complex (p. 463), are not described and are taken as unchanged."))

LECTS_LB = [dict(
    id=PVK, name="Proto-Vanikoro", alt_names="Vanikoro; *p-Vanikoro", type="proto-language", glottocode="",
    parent_id=PTM,
    notes="Teanu, Lovono and Tanema. François (2009: 5-6) argues for it from the paragogic vowel, *t > k before u and "
          "lexical innovations (Table 2), against Ross & Næss (2007: 473), for whom 'no innovations define Vanikoro'; "
          "Lackey & Boerger (2021: 383-388) give a set of ordered shared changes ((103), Table 3). Not in the main tree "
          "(decision temotu-tree); no Glottolog clade (Glottolog has Utupua-Vanikoro only).",
    inherit="assumed-unchanged", inherit_source_id=LB, inherit_page="387")]

rn, lb, f9 = [], [], []
cnt = {"rn": 0, "lb": 0, "f9": 0}


def mk(store, tag, src, lect, parent, child, env, page, printed="", notes="", status="regular", conditioning="",
       lexical="", source_form="", locator="", derivation="", examples="", decision=""):
    cnt[tag] += 1
    store.append(dict(id=f"{lect}-{tag}-{cnt[tag]}", child_lect_id=lect, parent_phoneme=parent, child_phoneme=child,
                      environment=env, status=status, conditioning=conditioning, lexical_scope=lexical, source_id=src,
                      page=page, notes=notes, source_form=source_form, as_printed=printed, locator=locator,
                      derivation=derivation, examples=examples, decision=decision))


def R(lect, parent, child, env, printed, notes="", status="regular", conditioning="", lexical="", sf="", page=T2,
      locator="Table 2", decision="temotu-composed"):
    mk(rn, "rn", RN, lect, parent, child, env, page, printed, notes, status, conditioning, lexical, sf, locator,
       derivation="composed" if locator == "Table 2" else "", decision=decision if locator == "Table 2" else "")


def L(lect, parent, child, env, page, printed="", notes="", status="regular", conditioning="", locator="", sf=""):
    mk(lb, "lb", LB, lect, parent, child, env, page, printed, notes, status, conditioning, "", sf, locator)


UNK = "unknown"
PAR = "In parentheses in Table 2: less common than the reflex outside them."
FL = ("Fortis and lenis reflexes of the initial stop: verbs have the fortis, non-verbs usually the lenis one "
      "(Ross & Næss 2007: 469-470, (19)).")

# ---------------- Ross & Næss (2007): node innovations ----------------
R(PTM, "r", "l", "elsewhere", "*r, *l > PTm *l", "POc *r and *l merged as *l, a Temotu innovation (pp. 471-472); "
  "the shared special reflexes before *u (y in Asuboa and Tanibili) and Asuboa n for both point to one phoneme. "
  "Word-final reflexes behave differently (n. 17).", page="471-472", locator="(22), (27)")
R(PTM, "r", "r", "_#", "PTm retained final *-r", "Proto-Temotu kept at least final *-p, *-m, *-s, *-r, *-R and *-k, "
  "reflected in Vanikoro followed by an added vowel (p. 464).", page="464", locator="§2.2")
for p in ("r", "s", "q", "R"):
    R(PUT, p, "∅", "_#", f"Utupua loss of final *-{p}", "Loss of word-final *-r, *-s, *-q and *-R, retained in "
      "Vanikoro: a shared innovation of Utupua (p. 473).", page="473", locator="§2.4.2.3")
R(PUT, "R", "∅", "elsewhere", "complete loss of *R", "Complete loss of POc *R, also a shared innovation (p. 473). "
  "Table 2 has Asuboa l, Ø for *R, which this does not cover (decision temotu-composed).", page="473",
  locator="§2.4.2.3")
R(PUV, "q", "∅", "elsewhere", "UV loss of nonfinal *q", "Defines Utupua-Vanikoro phonologically, 'but this is not "
  "strong evidence, as the same loss occurs in the Santa Cruz languages' (p. 473).", page="473", locator="§2.4.2.2")
R(PUT, "q", "∅", "elsewhere", "UV loss of nonfinal *q", "Ross & Næss's Utupua-Vanikoro loss of nonfinal *q (p. 473), "
  "entered on Proto-Utupua as Utupua-Vanikoro is not in the main tree.", page="473", locator="§2.4.2.2")

# ---------------- Ross & Næss (2007): Table 2, restated against the parent ----------------
# RSC (parent PRSC: *t > l, *p > v, *k, *q > Ø after a vowel; *s > t; *dr > d; *R > l)
for lect in (AIW, NAG):
    R(lect, "k", "k", "#_", "*k/*#_ > k, Ø", FL, conditioning="lexical", lexical="verbs (fortis)")
    R(lect, "k", "∅", "#_", "*k/*#_ > k, Ø", FL, conditioning="lexical", lexical="non-verbs (lenis)")
R(AIW, "q", "k", "elsewhere", "*q > Äiwoo k, Ø", "Two reflexes; *q, like *k, splits into k and zero (p. 466).",
  conditioning=UNK)
R(AIW, "q", "∅", "elsewhere", "*q > Äiwoo k, Ø", "Two reflexes; *q, like *k, splits into k and zero (p. 466).",
  conditioning=UNK)
for lect in (NAT, NAG):
    R(lect, "q", "∅", "elsewhere", "*q > Ø", "Lost also initially (Table 2).")
    R(lect, "ŋ", "n", "_i", "*ŋ/_*i > n")
    R(lect, "mʷ", "m", "elsewhere", "*mʷ > m", "Äiwoo keeps mʷ.")
    R(lect, "v", "∅", "_o", "*p/_*u, o > Ø", "*p becomes zero before *u in Äiwoo and before *u or *o in Natügu and "
      "Nagu (p. 467); the loss before *u is entered on Proto-Reefs-Santa Cruz.")
R(NAT, "t", "l", "#_", "*t/*#_ > Natügu t (l)", FL + " " + PAR, status="sporadic", lexical="non-verbs (lenis)")
R(AIW, "t", "∅", "V_V", "*t/V_V > Äiwoo Ø", "Table 2 has Äiwoo Ø against Natügu and Nagu l; the examples are nouns "
  "with the fossilised article, and Lackey & Boerger (2021: 374) give Äiwoo reflexes with l and s. Not explained.",
  status="disputed")

# Utupua (parent Proto-Utupua: *s, *c, *j > s; *r > l; final *-r, *-s, *-q, *-R, nonfinal *q and *R lost)
def U(lect, parent, cells, env, printed, notes="", lexical=False, once=()):
    main = [x for x in cells if x not in once]
    for ch in cells:
        sf = {"d͡ʒ": "j", "j": "y"}.get(ch, "")
        if ch in once:
            R(lect, parent, ch, env, printed, (notes + " " if notes else "") + PAR, status="sporadic", sf=sf)
        else:
            R(lect, parent, ch, env, printed, notes, conditioning=UNK if len(main) > 1 else "", sf=sf)


U(NEB, "p", ["v", "h", "∅"], "elsewhere", "*p > Nebao v (h, Ø)", once=("h", "∅"))
U(ASU, "p", ["v", "p", "∅"], "elsewhere", "*p > Asuboa v (p, Ø)", once=("p", "∅"))
R(ASU, "p", "∅", "_u, _o", "*p/_*u, o > Asuboa w‡", "Printed w with the note that it may be the transition between an "
  "unrounded and a rounded vowel, i.e. phonemic Ø (Table 2, ‡).", sf="w")
R(TNB, "p", "p", "_ə#", "*p > Tanibili v, p", "p before the word-final vowel sequence -io from PUV *-ə: lenition "
  "blocked (p. 468).")
R(TNB, "p", "v", "elsewhere", "*p > Tanibili v, p", "v is the default reflex (p. 468).")
R(TNB, "p", "∅", "_u", "*p/_*u > Tanibili Ø")
for lect in (NEB, ASU, TNB):
    R(lect, "w", "∅", "elsewhere", "*w > Ø", "Tanibili also w‡, phonemically Ø (Table 2)." if lect == TNB else "")
R(NEB, "pʷ", "vʷ", "elsewhere", "*pʷ > Nebao vʷ")
R(ASU, "pʷ", "w", "elsewhere", "*pʷ > Asuboa w")
R(TNB, "pʷ", "p", "elsewhere", "*pʷ > Tanibili p")
R(TNB, "bʷ", "b", "elsewhere", "*bw > Tanibili b")
R(ASU, "mʷ", "m", "elsewhere", "*mʷ > Asuboa m")
R(NEB, "t", "r", "#_", "*t/*#_ > Nebao r (t)", FL, conditioning="lexical", lexical="non-verbs (lenis)")
R(NEB, "t", "t", "#_", "*t/*#_ > Nebao r (t)", FL + " " + PAR, status="sporadic", lexical="verbs (fortis)")
U(NEB, "t", ["r", "t"], "V_V", "*t/V_V > Nebao r, t")
U(NEB, "t", ["r", "t"], "_u, _i", "*t/_*u, i > Nebao r, t", "Row printed '*t/_*u, i' below a row '*t/_*u'.")
R(ASU, "t", "j", "_u", "*t/_*u > Asuboa y", sf="y")
R(ASU, "t", "s", "_u, _i", "*t/_*u, i > Asuboa s", "Row printed '*t/_*u, i' below a row '*t/_*u' (Asuboa y).")
R(ASU, "t", "d", "V_V", "*t/V_V > Asuboa d")
TNBT = "Tanibili *t (p. 470): "
R(TNB, "t", "s", "_u", "*t/_*u > Tanibili s", TNBT + "s before present-day -u.")
R(TNB, "t", "kʷ", "_o", "*t > Tanibili t, r, kʷ", TNBT + "kʷ morpheme-initially before *-o (*topu, *tolu).")
R(TNB, "t", "t", "elsewhere", "*t > Tanibili t, r, kʷ", TNBT + "t and r are the fortis and lenis reflexes, unpredictably.",
  conditioning=UNK)
R(TNB, "t", "r", "elsewhere", "*t > Tanibili t, r, kʷ", TNBT + "t and r are the fortis and lenis reflexes, unpredictably.",
  conditioning=UNK)
R(TNB, "t", "∅", "elsewhere", "*t/V_V > Tanibili t, r, kʷ, Ø", TNBT + "zero in ami- 'father' and me-me 'die' only.",
  status="sporadic", conditioning=UNK)
R(TNB, "d", "d͡ʒ", "elsewhere", "*d > Tanibili j", sf="j")
U(ASU, "l", ["l", "n", "∅"], "elsewhere", "*r > Asuboa l, n, Ø; *l > n, Ø", "PTm *l from POc *r and *l; Asuboa n for "
  "both shows they were one phoneme (p. 471).")
for lect in (NEB, TNB):
    R(lect, "l", "∅", "elsewhere", "*r, *l > l (Ø)", PAR, status="sporadic")
R(NEB, "l", "∅", "_u", "*r/_*u > Nebao l, Ø", conditioning=UNK)
R(ASU, "l", "j", "_u", "*r, *l/_*u > Asuboa y", "The special reflex before *u shared by *r and *l (p. 471).", sf="y")
R(ASU, "l", "∅", "_u", "*r/_*u > Asuboa y, Ø", conditioning=UNK)
R(TNB, "l", "j", "_u", "*r, *l/_*u > Tanibili y", "The special reflex before *u shared by *r and *l (p. 471).", sf="y")
U(ASU, "dr", ["d", "d͡ʒ"], "elsewhere", "*dr > Asuboa d, j")
R(TNB, "dr", "d͡ʒ", "_i", "*dr > Tanibili j/_i", sf="j")
U(ASU, "s", ["∅", "s"], "elsewhere", "*s > Asuboa Ø, s")
R(TNB, "s", "∅", "elsewhere", "*s > Tanibili Ø")
U(ASU, "ñ", ["n", "j"], "elsewhere", "*ñ > Asuboa n, y")
R(NEB, "k", "∅", "#_", "*k/*#_ > Nebao Ø")
for lect in (ASU, TNB):
    R(lect, "k", "k", "#_", "*k/*#_ > k, Ø", FL, conditioning="lexical", lexical="verbs (fortis)")
    R(lect, "k", "∅", "#_", "*k/*#_ > k, Ø", FL, conditioning="lexical", lexical="non-verbs (lenis)")
    R(lect, "k", "∅", "V_V", "*k/*V_V > Ø")
U(ASU, "k", ["∅", "s"], "_#", "*k/_*# > Asuboa Ø, s")
U(TNB, "k", ["∅", "j"], "_#", "*k/_*# > Tanibili Ø, y")
R(NEB, "ŋ", "n", "_i", "*ŋ/_*i > Nebao n")

# Vanikoro languages, restated against Proto-Temotu (they are under PTm after the sheet edit in BATCH.md).
for lect in (BUM, VNO, TNM):
    R(lect, "p", "v", "elsewhere", "*p > v, p", "v is the default reflex; p for verbs initially (fortis) and before "
      "final -ie in Vano (pp. 468-469).", conditioning=UNK)
    R(lect, "p", "p", "elsewhere", "*p > v, p", "Fortis reflex: verbs initially (p. 469, (19)).", conditioning=UNK)
    R(lect, "p", "∅", "_u", "*p/_*u > Ø")
    R(lect, "w", "∅", "elsewhere", "*w > Ø, w" if lect != TNM else "*w > Ø", conditioning=UNK if lect != TNM else "")
    if lect != TNM:
        R(lect, "w", "w", "elsewhere", "*w > Ø, w", conditioning=UNK)
    R(lect, "pʷ", "b" if lect == TNM else "p", "elsewhere", "*pʷ > " + ("b" if lect == TNM else "p"))
    R(lect, "mʷ", "m", "elsewhere", "*mʷ > m") if lect != TNM else None
    R(lect, "k", "∅", "V_V", "*k/*V_V > Ø")
    R(lect, "q", "∅", "elsewhere", "*q > Ø", "Final *-q was kept long enough to take the added vowel (p. 465).")
    R(lect, "s", "r", "_#", "*s/_*# > r", "Followed by the added vowel (p. 464: *manipis > Buma meñeviro).")
R(BUM, "p", "∅", "_#", "*p/_*# > Buma Ø")
R(TNM, "p", "v", "_#", "*p/_*# > Tanema v")
R(BUM, "t", "s", "_u", "*t/_*u > Buma s, k", conditioning=UNK)
R(BUM, "t", "k", "_u", "*t/_*u > Buma s, k", "François (2009: 6) explains k as velarisation before u.", conditioning=UNK)
R(TNM, "t", "s", "_u", "*t/_*u > Tanema s")
R(VNO, "t", "s", "_u, _i", "*t/_*u, i > Vano s", "Row printed '*t/_*u, i'.")
R(VNO, "t", "l", "#_", "*t/*#_ > Vano l, t", "Nouns reflecting *t have initial l-, verbs t- (Table 2, ††).",
  conditioning="lexical", lexical="nouns")
R(VNO, "t", "t", "#_", "*t/*#_ > Vano l, t", "Nouns reflecting *t have initial l-, verbs t- (Table 2, ††).",
  conditioning="lexical", lexical="verbs")
R(VNO, "t", "l", "V_V", "*t/V_V > Vano l")
for ch in ("∅", "t"):
    R(TNM, "t", ch, "#_", "*t/*#_ > Tanema Ø, t", "Two reflexes; p. 469 says Tanema has no lenis reflex of *t-, but "
      "Table 2 has Ø, t, and François (2009: 9) gives Tanema Ø as the lenis reflex.", conditioning=UNK)
R(VNO, "l", "r", "_u", "*r/_*u > Vano r", "Against l for *l/_*u: probably too little data (p. 472).")
R(BUM, "k", "∅", "#_", "*k/*#_ > Buma Ø")
R(BUM, "ŋ", "ɡ", "elsewhere", "*ŋ > Buma ŋ, g", conditioning=UNK, sf="g")
R(BUM, "ŋ", "ŋ", "elsewhere", "*ŋ > Buma ŋ, g", conditioning=UNK)
U(TNM, "s", ["s", "d", "c"], "elsewhere", "*s > Tanema s, d, c")

DEC_RN = [
    dict(id="temotu-tree", question="How are the Temotu languages placed? Ross & Næss (2007): Temotu > RSC, "
         "Utupua-Vanikoro (> Utupua, Buma, Vano, Tanema, no Vanikoro node). Lackey & Boerger (2021): Temotu > RSC (> "
         "Reefs, Santa Cruz), Utupua, Vanikoro, rejecting Utupua-Vanikoro. François (2009) argues for Proto-Vanikoro.",
         chosen_reading="By the rule for competing classifications: Proto-Temotu (POc) > Proto-Reefs-Santa Cruz and "
                        "Proto-Utupua, which both have; Teanu, Lovono and Tanema directly under Proto-Temotu, with "
                        "Proto-Vanikoro (Lackey & Boerger 2021; François 2009) and Proto-Utupua-Vanikoro (Ross & Næss "
                        "2007) as proposed parents; Proto-Utupua's proposed parent is Proto-Utupua-Vanikoro. No Santa "
                        "Cruz node (Lackey & Boerger's figure only). The three Vanikoro languages need sheet edits: "
                        "parent_id ptm and alt_parents, and François's (2011) rows *r > l word-internally restated as "
                        "*l > l (PTm merged *r and *l).",
         alternatives="Put the Vanikoro languages under Proto-Vanikoro, following the later work (Lackey & Boerger, "
                      "François), and leave Utupua-Vanikoro as a proposed parent only.",
         status="open", source_id=RN, page="471-473"),
    dict(id="temotu-composed", question="Ross & Næss's Table 2 states POc > language. How is it restated against "
         "the new nodes, and where it disagrees with Lackey & Boerger (2021)?",
         chosen_reading="Each cell is restated against the lect's parent: PTm (*r, *l > *l; *s, *c, *j > *s), PRSC "
                        "(Lackey & Boerger's Table 2) and Proto-Utupua; a cell that the parent's changes already "
                        "predict is not a row. Cells that Lackey & Boerger correct are not entered: RSC *p > v "
                        "everywhere (initial *p is kept), Äiwoo *s > s (t; s only from *t before i), the *c row "
                        "(merged with *s at PTm, but Table 2's *c and *s reflexes disagree in Vano, Tanibili and "
                        "Buma). Asuboa l for *R is not entered (Utupua loses *R completely, p. 473). Multiple "
                        "reflexes without a condition: conditioning unknown; in parentheses: sporadic; fortis and "
                        "lenis initials: lexical (verbs, non-verbs). The row '*t/_*u, i' is entered as printed "
                        "(environments _u, _i).",
         alternatives="Enter every cell of Table 2 as printed; take '*t/_*u, i' to be '*t/_*i'.",
         status="open", source_id=RN, page="463-473"),
]

# ---------------- Lackey & Boerger (2021) ----------------
L(PTM, "c", "s", "elsewhere", "388-389", "*c, *j > PTm *s", "Merger of POc *s, *c and *j at the Proto-Temotu stage: "
  "RSC, Vanikoro and Utupua each reflect the three alike (§6.1).", locator="Table 4")
L(PTM, "j", "s", "elsewhere", "388-389", "*c, *j > PTm *s", "Merger of POc *s, *c and *j at the Proto-Temotu stage "
  "(§6.1).", locator="Table 4")
L(PUT, "s", "∅", "V_V", "388-389", "*s, *c, *j > Ø (Utupua)", "Utupua loses POc *s between vowels (and finally), "
  "and with it *c and *j (Tryon & Hackman 1983: 96): *na kasupe > Nembao nā ve, *losop > lo (§6.1).", locator="Table 4")
T2LB = "Table 2"
L(PRSC, "p", "v", "V_V", "372, 376", "*p > v, w, Ø /V_", "Lenition after a vowel; *p is kept initially (pp. "
  "372-373), against Ross & Næss's lenition everywhere.", locator=T2LB)
L(PRSC, "p", "w", "V_V", "376", "*p > v, w, Ø /V_", "Lenition after a vowel; no condition given for w.",
  conditioning=UNK, locator=T2LB)
L(PRSC, "p", "∅", "V_u", "376", "*p > v, w, Ø /V_", "Lost before a back vowel (Ross & Næss 2007: 467: before *u "
  "in Äiwoo, before *u or *o in Natügu and Nagu).", locator=T2LB)
L(PRSC, "t", "l", "V_V", "376", "*t > l /V_", "Lenition after a vowel.", locator=T2LB)
L(PRSC, "k", "∅", "V_V", "376", "*k > Ø /V_", "Lenition after a vowel.", locator=T2LB)
L(PRSC, "q", "∅", "V_V", "372, 376", "*q > Ø /V_", "Normally lost; final *q blocked syncope, so it survived for a "
  "time; a few words keep k or g (*qasu 'smoke') (p. 372).", locator=T2LB)
L(PRSC, "dr", "d", "elsewhere", "373, 376", "*dr > d", locator=T2LB)
L(PRSC, "s", "t", "elsewhere", "373-374, 376", "*s, *c, *j > t", "After *t > l: intervocalic *s does not become l "
  "(p. 374). PTm *s covers POc *s, *c, *j.", locator=T2LB)
L(PRSC, "ñ", "n", "elsewhere", "374-376", "*ñ > *ni", "Tentative: Äiwoo mi-biou < *mañawa may keep the palatal "
  "as i (p. 375).", status="disputed", locator=T2LB)
L(PRSC, "R", "l", "elsewhere", "375-376", "*l, *r, *R > l", "Three-way merger of the liquids (p. 375); PTm had "
  "already merged *r and *l.", locator=T2LB)
L(PRSC, "R", "∅", "elsewhere", "376", "", "*R is sporadically deleted, as in Mussau and Remote Oceania (Ross & Næss "
  "2007: 466).", status="sporadic")
L(AIW, "ŋ", "ɡ", "elsewhere", "375-376", "*ŋ > g (Äiwoo only)", "Several instances (prenasalised [ᵑɡ]); not "
  "before a coda nasal (vängä < *paŋan).", conditioning=UNK, locator=T2LB, sf="g")
L(AIW, "t", "s", "_i", "374, 376", "*t > s /_i", "Recent change, regular in Äiwoo.", locator=T2LB)
for lect in (NAT, NAG):
    L(lect, "t", "s", "_i", "374, 376", "*t > s /_i", "Recent change, sporadic outside Äiwoo; in Natügu also "
      "fast-speech [s] before /i/.", status="sporadic", locator=T2LB)
# Proto-Vanikoro, (103) and Table 3 (p. 386-388); PTm *s covers *s, *c, *j.
T3LB = "Table 3"
L(PVK, "s", "d", "#_", "385-388", "*s, *j > d /#_", "(103a), first in the order of changes.", locator=T3LB)
L(PVK, "s", "R", "V_V", "386-388", "*s, *c, *j > *R /V_", "(103b): after a vowel they merged with *R; then "
  "intervocalic l, final r + paragogic vowel (§5.3).", locator=T3LB)
L(PVK, "s", "R", "_#", "386-388", "*s, *c, *j > *R /V_", "(103b); coda *s > r followed by the paragogic vowel.",
  locator=T3LB)
for v in ("i", "u"):
    L(PVK, v, "∅", "C_#", "384, 387-388", "*i, *u > Ø /C_#", "(103c): loss of unstressed final high vowels, so that "
      "consonants before them behave as codas (*patu > *vat > *vak > Teanu voko).", locator=T3LB)
L(PVK, "t", "k", "_#", "384, 387-388", "*t > k /_#", "(103d): coda *t, including *t before a lost final high vowel; "
  "François (2009: 6) has *t > k before u instead.", locator=T3LB)
L(PVK, "R", "l", "_V", "384-388", "*R > l /_V", "Includes *R from *s, *c, *j; coda *R stays r (§5.2).",
  locator=T3LB)
L(PVK, "∅", "ə", "C_#", "384, 387-388", "Ø > ə /C_#", "(103e): a paragogic vowel after coda consonants, the last "
  "change.", locator=T3LB)
L(PVK, "l", "∅", "_#", "384-385", "", "*r and *l are lost in the coda (*maqurip > Teanu maluo, *palaur > Teanu "
  "pwalau), unlike *R and *s (§5.2).", locator="§5.2")
L(PVK, "n", "ñ", "_iV", "387-388", "*niV > *ñV", "Tentative (*niuR > Teanu luro, through *ñuR).", status="disputed",
  locator=T3LB)
L(PVK, "ñ", "l", "elsewhere", "387-388", "*ñ > l", "Tentative: one clear example, *poñu > Teanu anuele, Lovono pwile "
  "(p. 387).", status="disputed", locator=T3LB)
L(PVK, "l", "∅", "unstressed syllables", "388", "*l > Ø", "In unstressed syllables; tentative (*lima > Teanu ma, "
  "*taliŋa > Teanu taña).", status="disputed", locator=T3LB)

DEC_LB = [dict(
    id="lackeyboerger2021-q", question="Lackey & Boerger (2021: 389-390) suggest that Proto-Temotu lenited *q to a "
    "fricative (x or χ) that later languages lost or restored to k, g. Enter it?",
    chosen_reading="Not as a row (stated as 'perhaps'): it is in the Proto-Temotu notes, and *q is kept in PTm.",
    alternatives="Enter PTm *q > *χ as disputed and restate the daughters' rows.", status="open", source_id=LB,
    page="389-390")]

# ---------------- François (2009) ----------------
def F(lect, parent, child, env, page, printed="", notes="", status="regular", conditioning="", locator="", lexical=""):
    mk(f9, "f9", F9, lect, parent, child, env, page, printed, notes, status, conditioning, lexical, "", locator)


F(PVK, "∅", "ə", "C_#", "5", "", "Added after most word-final consonants, probably a schwa: *manuk > *manukə > Teanu "
  "menuko, Lovono menuka, Tanema manuke; an exclusively shared innovation (p. 5).", locator="(1)")
F(PVK, "t", "k", "_u", "6", "", "'Occasional velarisation of *t to /k/ before a high back vowel /u/': *patu > *vaku > "
  "Teanu voko, Lovono and Tanema vaka (p. 6). Lackey & Boerger (2021: 384) reanalyse it as coda *t > k.",
  status="sporadic", locator="(2)")
T3F = ("Lenis reflexes of *t: Teanu t, Lovono l, Tanema Ø in sit, three, sugarcane, soul and others (Table 3, after "
       "Tryon & Hackman 1983: 71). Gaimard's early 19th-century wordlists write these Tanema words with r, so Tanema had r two "
       "centuries ago (p. 9).")
F(VNO, "t", "l", "elsewhere", "9", "TEA /t/ ~ LVN /l/ ~ TNM Ø", T3F, locator="Table 3", conditioning="lexical",
  lexical="lenis reflex")
F(TNM, "t", "∅", "elsewhere", "9", "TEA /t/ ~ LVN /l/ ~ TNM Ø", T3F, locator="Table 3", conditioning="lexical",
  lexical="lenis reflex")

MD_RN = """# rossnaess2007-temotu

Ross, Malcolm & Åshild Næss. 2007. An Oceanic origin for Äiwoo, the language of the Reef Islands? *Oceanic Linguistics* 46(2). 456-498. Generator: `tools/batch_scripts/new_sources_2026_11_23b/temotu.py`.

## Scope

- New nodes Proto-Temotu (under POc), Proto-Reefs-Santa Cruz, Proto-Utupua and Proto-Utupua-Vanikoro (proposed parent only); new languages Äiwoo, Natügu, Engdewu (Nagu), Nebao, Asumboa, Tanimbili.
- Node innovations: PTm *r, *l > *l (pp. 471-472); Utupua final-consonant loss and loss of *R (p. 473); Utupua-Vanikoro loss of nonfinal *q.
- Table 2 (p. 463), restated against each language's parent; cells predicted by the parent's changes are not rows (decision `temotu-composed`).

## Sheet edits after applying (decision temotu-tree)

- `lects` Teanu (`tean1237`), Lovono (`vano1237`), Tanema (`tane1237`): `parent_id` `ptm`; `alt_parents` `pvanikoro:lackeyboerger2021;pvanikoro:francois2009;puv:rossnaess2007`; notes: replace "no Temotu node is entered, so the parent is POc" with the new placement.
- `correspondences` of `francois2011` on these three lects with `parent_phoneme` `r` and environment `word-internally`: `parent_phoneme` `l` (PTm merged *r and *l), note "Restated against Proto-Temotu (decision temotu-tree)."

## Not entered

- Table 1 (numerals), the vowels, syncope and truncation (not phoneme changes), the *c row and other cells listed in `temotu-composed`, §3 (morphosyntax).

## Decisions (open)

- `temotu-tree`, `temotu-composed`.
"""

MD_LB = """# lackeyboerger2021-temotu

Lackey, William James & Brenda H. Boerger. 2021. Reexamining the phonological history of Oceanic's Temotu subgroup. *Oceanic Linguistics* 60(2). 367-411. Generator: `tools/batch_scripts/new_sources_2026_11_23b/temotu.py`.

## Scope

- Proto-Temotu merger of *s, *c, *j (Table 4).
- Proto-Reefs-Santa Cruz changes (Table 2), with the Äiwoo-only *ŋ > g and the recent *t > s before i.
- New node Proto-Vanikoro (proposed parent of the Vanikoro languages) with the ordered changes of (103) and Table 3.

## Not entered

- Syncope and truncation from stress (§4: not phoneme changes), the Santa Cruz node of Figure 1, appendix A (wordlist), appendix B (*a in RSC); Nalögo and Noipä (no correspondences of their own).

## Decisions (open)

- `lackeyboerger2021-q` (and the shared `temotu-tree`, `temotu-composed`).
"""

MD_F9 = """# francois2009-vanikoro

François, Alexandre. 2009. The languages of Vanikoro: Three lexicons and one grammar. In Bethwyn Evans (ed.), *Discovering history through language: Papers in honour of Malcolm Ross*, 103-126. Canberra: Pacific Linguistics. Pages cited from the author's PDF (1-24). Generator: `tools/batch_scripts/new_sources_2026_11_23b/temotu.py`.

## Scope

- Proto-Vanikoro: paragogic vowel and the occasional *t > k before u (pp. 5-6).
- Table 3 (p. 9): lenis reflexes of *t in Lovono (l) and Tanema (Ø); Teanu t needs no row.

## Not entered

- Table 2 (lexical innovations), Table 4 (Teanu b : Lovono m : Tanema b, no POc etymon), Tables 5-14 (lexicon and grammar).
"""

NM_RN = [dict(lect_id=l, system="canonical", source_id=src, page=pg, notes=nt) for l, src, pg, nt in [
    (PTM, LB, "369", "POc orthography, as Lackey & Boerger write Proto-Temotu."),
    (PRSC, LB, "369, 376", "POc orthography, as in Lackey & Boerger's Table 2."),
    (PUT, RN, "463", "POc orthography (Ross & Næss do not write Proto-Utupua forms)."),
    (PUV, RN, "468-469", "Ross & Næss's PUV forms in POc orthography, with *ə.")]]
NM_LB = [dict(lect_id=PVK, system="canonical", source_id=LB, page="384-388",
              notes="Lackey & Boerger's Proto-Vanikoro, in POc orthography with *ə; François (2009) writes *p-Vanikoro forms in the same way.")]
write("rossnaess2007-temotu", dict(sources=SOURCES_RN, lects=LECTS_RN, correspondences=rn, notation_map=NM_RN,
                                  decisions=DEC_RN), MD_RN)
write("lackeyboerger2021-temotu", dict(sources=SOURCES_LB, lects=LECTS_LB, correspondences=lb, notation_map=NM_LB,
                                      decisions=DEC_LB), MD_LB)
write("francois2009-vanikoro", dict(sources=SOURCES_F9, correspondences=f9), MD_F9)
