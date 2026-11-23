"""Batch blust1984-mussau: Blust (1984), POc > Mussau.

Blust, Robert. 1984. A Mussau vocabulary, with phonological notes. In Malcolm Ross et al. (eds.),
Papers in New Guinea linguistics No. 23 (Pacific Linguistics A-69), 159-208.
Read from the PDF in Downloads (sealang.net scan with a text layer; the tables on pp. 177-181 read
from page images).

    python3 tools/batch_scripts/new_sources_2026_11_23/blust1984.py
"""
from common import write

S = "blust1984"
L = "muss1246"
BATCH = "blust1984-mussau"

SOURCES = [dict(
    id=S, author="Blust, Robert", year="1984", title="A Mussau vocabulary, with phonological notes",
    url_or_doi="https://doi.org/10.15144/PL-A69.159", kind="comparative", pub_type="chapter",
    container_title="Papers in New Guinea linguistics No. 23",
    editors="Malcolm Ross; Jeff Siegel; Robert Blust; Michael Colburn; Walter Seiler",
    pages="159-208", place="Canberra", publisher="Pacific Linguistics", series="Pacific Linguistics A-69",
    notes="Consulted directly on 23 November 2026 (sealang.net PDF; tables read from page images): phoneme "
          "inventory (§2.1, pp. 168-169), phonetics (§2.4, pp. 171-175), canonical changes (§3.1), regular "
          "unconditioned and conditioned changes from POc (§3.2.1, pp. 176-178), consonant grades (§3.2.2, "
          "pp. 179-180), Table 3 (p. 181) and irregular reflexes (§3.2.3, pp. 181-183). Blust writes POc in "
          "Grace's orthography, with *ns for Milke's *nj (n. 16, p. 203): his *mp, *nt, *nd, *d, *ŋk, *mpʷ, "
          "*j, *ns are Ross's *b, *d, *dr, *r, *ɡ, *bʷ, *c, *j. Appendix 1 (the POc etymologies, pp. 186-202) "
          "gives the examples cited by number."),
]

rows = []
n = 0


def c(parent, child, env="elsewhere", status="regular", count="", page="177", notes="", examples="",
      as_printed="", locator="", blank_type="", conditioning="", lexical_scope="", decision="", total=""):
    global n
    n += 1
    if env == "conditions unknown" and not conditioning:
        conditioning = "unknown"
    rows.append(dict(id=f"muss-bl84-{n}", child_lect_id=L, parent_phoneme=parent, child_phoneme=child,
                     environment=env, status=status if child or status != "regular" else "",
                     blank_type=blank_type, evidence_count=str(count), evidence_total=str(total),
                     source_id=S, page=page, notes=notes, examples=examples, as_printed=as_printed,
                     locator=locator, conditioning=conditioning, lexical_scope=lexical_scope,
                     decision=decision))


CROSS = ("Blust treats such reflexes as consonant-grade 'cross-over' (the etymon had the other grade in "
         "pre-Mussau), not as irregularities (pp. 179-180); his oral-grade reflex of this phoneme is the "
         "other row.")
GRADE = "cross-over etyma (nasal-grade reflex in pre-Mussau)"
DEC = "blust1984-grades"

# --- §3.2.1.1 regular unconditioned changes (p. 177) with the counts of §3.2.2 (pp. 179-180)
c("p", "∅", count=39, examples="9; 29; 153", as_printed="*p > ∅", page="177, 179",
  notes="Oral-grade reflex: *p was lost (39 instances in Appendix 1).")
c("p", "p", env="conditions unknown", conditioning="lexical", lexical_scope=GRADE, examples="17; 128; 134",
  as_printed="*p > p", notes=CROSS, decision=DEC)
c("p", "b", env="conditions unknown", conditioning="lexical", lexical_scope=GRADE, examples="30; 33; 35",
  as_printed="*p > b", notes=CROSS + " Example: *pakiwa > baio 'shark' (< *mpakiwa, p. 180).", decision=DEC)
c("b", "b", count=12, examples="31; 36; 38", as_printed="*mp > b", page="177, 179",
  notes="Blust's *mp (Ross's *b). Two reflexes, b (12) and p (10), with no stated condition (p. 179).")
c("b", "p", env="conditions unknown", count=10, examples="129; 131; 133", as_printed="*mp > p", page="177, 179",
  notes="Blust's *mp (Ross's *b); the two nasal-grade reflexes are not explained ('the multiple NG reflexes "
        "of *p and *k present difficulties', p. 180).")
c("m", "m", examples="13; 50; 98")
c("pʷ", "∅", count=1, page="180", as_printed="*pʷ > ∅",
  notes="Tentative: *kupʷena > uena 'casting net'. Blust suggests that *pʷ had oral and nasal grades too (p. 180).")
c("bʷ", "b", count=1, page="180", as_printed="*mpʷ > b",
  notes="Blust's *mpʷ (Ross's *bʷ): *mpʷoŋi > bo, bo-boŋi-ena 'night' (p. 180).")
c("mʷ", "m", status="sporadic", count=1, page="183", examples="136",
  notes="'The change *mw > m (136) may be regular, but the available data are insufficient to determine this' (p. 183).")
c("t", "t", count=39, examples="24; 25; 169", page="177, 179")
c("d", "r", count=2, examples="19; 194", as_printed="*nt > r", page="177, 179",
  notes="Blust's *nt (Ross's *d); merged with the reflexes of *nd and *ns (Table 3, p. 181).")
c("d", "t", env="conditions unknown", conditioning="lexical", lexical_scope="cross-over etyma (oral-grade reflex)",
  examples="168; 179", as_printed="*nt > t", notes="Blust's *nt (Ross's *d). Table 3 has *nt > r only; "
  "t is the oral-grade reflex, a consonant-grade cross-over (pp. 179-180).", decision=DEC)
c("r", "l", count=14, examples="60; 77; 164", as_printed="*d > l", page="177, 179",
  notes="Blust's *d (Ross's *r). Merged with *l (Table 3). Reflexes of final *d were recorded only before a "
        "transitive suffix (n. 14).")
c("dr", "r", count=10, examples="18; 20; 142", as_printed="*nd > r", page="177, 179",
  notes="Blust's *nd (Ross's *dr).")
c("n", "n", examples="10; 14; 116")
c("s", "s", count=41, examples="2; 21; 152", page="177, 179")
c("s", "r", env="conditions unknown", conditioning="lexical", lexical_scope="cross-over etyma (nasal-grade reflex)",
  examples="141; 143; 144", as_printed="*s > r", notes=CROSS + " Example: *siwa > sio 'nine' is the reverse case "
  "(< *nsiwa, p. 180).", decision=DEC)
c("j", "r", count=7, examples="138; 139; 140", as_printed="*ns > r", page="177, 179",
  notes="Blust's *ns (Milke's *nj; Ross's *j; n. 16).")
c("j", "s", env="conditions unknown", conditioning="lexical", lexical_scope="cross-over etyma (oral-grade reflex)",
  examples="106; 159; 160", as_printed="*ns > s", notes="Blust's *ns (Ross's *j). Table 3 has *ns > r only; "
  "s is the oral-grade reflex, a consonant-grade cross-over (pp. 179-180).", decision=DEC)
c("l", "l", examples="9; 78; 80")
c("l", "∅", env="conditions unknown", examples="52; 59; 179",
  notes="A minor rule or weakly attested reflex: in parentheses in Table 3 (n. 17).", locator="Table 3")
c("c", "s", count=2, examples="43; 122", as_printed="*j > s", page="177, 180",
  notes="Blust's *j (Ross's *c). Its nasal grade *nj has no examples (p. 180).")
c("ñ", "n", examples="69; 107; 111")
c("y", "i", examples="4; 7", notes="Merged with *i (Table 3). See also the contraction of *ya (p. 178).")
c("k", "∅", count=28, examples="4; 30; 105", page="177, 180")
c("k", "k", env="conditions unknown", conditioning="lexical", lexical_scope=GRADE, examples="61; 62; 176",
  as_printed="*k > k", notes=CROSS, decision=DEC)
c("ɡ", "k", count=15, examples="60; 63; 69", as_printed="*ŋk > k", page="177, 180",
  notes="Blust's *ŋk (Ross's *ɡ).")
c("ɡ", "ɡ", env="conditions unknown", count=3, as_printed="*ŋk > g", page="180",
  notes="Blust's *ŋk (Ross's *ɡ); the second nasal-grade reflex (3 instances), shown in Table 3.")
c("ŋ", "ŋ", examples="21; 80; 120")
c("R", "∅", examples="20; 47; 49")
c("R", "l", env="conditions unknown", examples="8; 85; 92",
  notes="A minor rule or weakly attested reflex: in parentheses in Table 3 (n. 17).", locator="Table 3")
c("q", "∅", examples="29; 38; 57")
for v in "ieaou":
    c(v, v, page="178", notes="'The Proto-Oceanic vowels are normally reflected without change in Mussau' (p. 178).")

# --- §3.2.1.2 conditioned changes (pp. 178-179)
c("l", "r", env="an adjacent syllable has r (< *dr, *j)", page="178", examples="138; 139; 140; 142",
  as_printed="*l (< *l, *R) > r if an adjacent syllable contains r (< *nd, *ns)",
  notes="ASSIMILATION (1): 'entirely regular'; the source of the constraint against l and r in one morpheme (§2.2).")
c("R", "r", env="an adjacent syllable has r (< *dr, *j)", page="178", examples="140",
  as_printed="*l (< *l, *R) > r if an adjacent syllable contains r (< *nd, *ns)",
  notes="ASSIMILATION (1), applying to *R after *R > l (example 140).")
c("a", "e", env="i(C)_", page="178", examples="10; 49; 50", as_printed="*a > e / i_",
  notes="ASSIMILATION (2): a subregularity; *a often remains unchanged here, even in contact (47, 48, 78, 148). "
        "Assimilation to a following *i is sporadic (87?, 155?).")
c("a", "o", env="_(C)o", page="178", examples="55; 106; 125", as_printed="*a > o / _o",
  notes="ASSIMILATION (3): recurrent, though *aCo generally remains unchanged (11, 20, 62, 80, 82, 92, 95).")
# CONTRACTION (1): *aw, *wa > o; CONTRACTION (2): *ya > e (fusions)
c("a", "o", env="_+w", page="178", examples="12; 162", as_printed="*aw > o",
  notes="CONTRACTION (1): *aw and *wa generally contracted to o; in *-awa- the *aw contraction predominated (12, 162) over *wa (172).")
c("w", "o", env="a+_", page="178", examples="12; 162", as_printed="*aw > o", notes="CONTRACTION (1).")
c("w", "o", env="_+a", page="178", examples="30; 121; 122; 160; 172", as_printed="*wa > o", notes="CONTRACTION (1).")
c("a", "o", env="w+_", page="178", examples="30; 121; 122; 160; 172", as_printed="*wa > o", notes="CONTRACTION (1).")
c("y", "e", env="_+a", status="sporadic", count=1, page="178", examples="77", as_printed="*ya > e",
  notes="CONTRACTION (2): in one known item; *Ra contracted likewise in 17, 135, 187, perhaps through *R > y. "
        "*ay and *aR did not contract.")
c("a", "e", env="y+_", status="sporadic", count=1, page="178", examples="77", as_printed="*ya > e",
  notes="CONTRACTION (2).")
c("q", "∅", env="V_V, trisyllables (like vowels then contract)", page="178", examples="97; 101; 126; 175",
  as_printed="*-aqa, *-aqo-, *-aqe- > a, o, e",
  notes="CONTRACTION (3): after the loss of *q in a trisyllable the like vowels contracted; not after the loss of "
        "other consonants (2, 20, 93, 102, 190), of *q in disyllables (75, 147), or if either vowel was high "
        "(57, 78). Ordered before the loss of *p, *k and *R (p. 184).")

# --- §3.2.3 irregular reflexes with two or more examples (pp. 181-182)
IRR = [("u", "i", "", "3/44; 157", "*u > i", "Irregular (1): the possessive -gi beside -gu (POc *-ŋku)."),
       ("t", "∅", "_#", "17; 39", "*-t > ∅", "Irregular (4); preceded the addition of echo vowels in *apaRat > apae (p. 184)."),
       ("∅", "e", "ŋ_#", "21; 91", "∅ > -e", "Irregular (5): an unexpected supporting vowel -e after *ŋ; not conditioned, "
        "given *nsalaŋ > raraŋa (p. 182)."),
       ("t", "k", "", "68; 147", "*t > k", "Irregular (9)."),
       ("n", "∅", "", "75; 81", "*n > ∅", "Irregular (10): *daqan > laa, *dapan > lapa, perhaps by wrong division of "
        "-na as the possessive (p. 182)."),
       ("i", "e", "", "104; 173", "*i > e", "Irregular (12)."),
       ("l", "r", "", "127; 195", "*l > r", "Irregular (16)."),
       ("a", "e", "", "87?; 155; 181; 185", "*a > e", "Irregular (17): could be a subregularity, but Blust treats all "
        "instances as irregular, given the different environments of 87 and 155 and of 181 and 185 (p. 182).")]
for p, ch, env, ex, ap, note in IRR:
    c(p, ch, env=env or "conditions unknown", status="sporadic", page="181-182", examples=ex, as_printed=ap,
      notes=note, count=len(ex.split(";")) if "?" not in ex else 3)
for v in "ieaou":
    c(v, "∅", env="_#, after a nasal", status="sporadic", page="181-182", examples="4; 45; 88; 141; 172",
      as_printed="*-V > ∅",
      notes="Irregular (3): loss of a final vowel after a nasal is 'sufficiently common to be considered a "
            "subregularity'; forms recorded with a final nasal may have a careful pronunciation with the vowel (p. 182).")

ALLO = [
    ("t", "t̪", "", "Postdental (p. 171)."),
    ("b", "β", "V_V", "Spirantised intervocalically, within a morpheme and across a morpheme boundary: /teba/ [teβa] 'a, one' (pp. 171-172)."),
    ("ɡ", "ɣ", "V_V, occasionally", "Occasionally a spirant intervocalically within a morpheme, much less consistently than /b/; not across a morpheme boundary (p. 172)."),
    ("r", "r", "", "A 2-3 tap alveolar trill; geminate r is a lengthened (5-6 tap?) trill (p. 171, n. 11)."),
    ("e", "e", "_V", "[e] before another vowel (p. 172)."),
    ("e", "ɛ", "elsewhere", "[ɛ] elsewhere (p. 172)."),
    ("i", "j", "#_V; V_#; V_V; V_C", "High vocoids tend to be non-syllabic word-initially before a vowel, word-finally after a vowel, "
     "intervocalically and postvocalically before a consonant (/iema/ [yema] 'knife'), except in words of two vocoids whose "
     "second vowel is non-high (/ia/ [iya]) (p. 172). Interpreted as vowels, since semivocalisation precedes stress (p. 173)."),
    ("u", "w", "#_V; V_#; V_V; V_C", "As for i: /niu/ [niw] 'coconut', /pouru/ [powru] 'mountain'; /ua/ [uwa] 'crocodile' stays "
     "syllabic (p. 172)."),
]
allo = []
for ph, al, env, note in ALLO:
    allo.append(dict(lect_id=L, phoneme=ph, allophone=al, environment=env, source_id=S, page="171-173", notes=note))
for v in "ieaou":
    allo.append(dict(lect_id=L, phoneme=v, allophone=v + "̥", environment="_#, optionally, after voiceless obstruents and nasals",
                     source_id=S, page="172", notes="Final vowels are optionally devoiced; when not devoiced they are sometimes followed "
                     "by slight glottal closure (p. 172)."))

DECISIONS = [dict(
    id=DEC, question="Blust (1984) lists several reflexes of POc *p, *k, *nt, *s and *ns in Mussau and then treats the "
             "minority ones as consonant-grade 'cross-over' (pp. 179-180). How are they entered?",
    chosen_reading="The oral-grade reflex of Table 3 as regular; each cross-over reflex as regular with conditioning "
                   "'lexical' and lexical_scope naming the cross-over etyma (p > p, p > b, k > k, s > r with the "
                   "nasal-grade reflex; nt > t and ns > s with the oral-grade one). The two nasal-grade reflexes of "
                   "*mp (b 12, p 10) and *ŋk (k 15, ɡ 3) are both regular, with no condition, as in Table 3.",
    alternatives="Enter the cross-over reflexes as sporadic; or leave them out, as Table 3 does.",
    status="open", source_id=S, page="177-181",
    notes="Blust's POc letters are mapped to Ross's (n. 16): *mp = b, *nt = d, *nd = dr, *d = r, *ŋk = ɡ, *mpʷ = bʷ, "
          "*j = c, *ns = j.")]

MD = f"""# {BATCH}

Blust, Robert. 1984. A Mussau vocabulary, with phonological notes. In Malcolm Ross et al. (eds.), *Papers in New Guinea linguistics No. 23* (Pacific Linguistics A-69), 159-208. Canberra: Pacific Linguistics. Read from the PDF the user put in Downloads on 23 November 2026 (sealang.net scan with a text layer; the tables of pp. 177, 180 and 181 read from page images). Generator: `tools/batch_scripts/new_sources_2026_11_23/blust1984.py`.

## Scope

- POc > Mussau (`muss1246`, which had an inventory from Ross 2002b and no rows): the regular unconditioned changes (p. 177) with Blust's counts (pp. 179-180), the conditioned changes (assimilations, contractions as fusion pairs, p. 178), and the irregular reflexes attested twice or more (pp. 181-182), as sporadic rows.
- Allophones (§2.4.1, pp. 171-173): postdental t, spirantised b and ɡ, e/ɛ, non-syllabic high vowels, final devoicing.
- Blust's Grace-style POc letters are mapped to Ross's (n. 16, p. 203); `as_printed` keeps his.

## Decisions (open)

- `{DEC}`.

## Not entered

- Blust's inventory (§2.1) is the same as the sourced one of Ross (2002b), so no phoneme rows; vowel length (contrastive, §2.4.2) has no column.
- Echo vowels after final consonants (§3.1), haplology, the stress rules and syncope (§2.4): canonical changes, not segment rows. The muss1246 notes already mention echo vowels.
- Irregular reflexes attested once (§3.2.3 items 2, 6-8, 11, 13-15, 18-20) and the doubtful etymologies of p. 183.
- The vocabulary itself (§5).
"""

write(BATCH, dict(sources=SOURCES, correspondences=rows, allophones=allo, decisions=DECISIONS), MD)
