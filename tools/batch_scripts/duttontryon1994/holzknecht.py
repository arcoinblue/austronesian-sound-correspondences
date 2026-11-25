#!/usr/bin/env python3
"""Holzknecht (1994), The mechanisms of language change in Labu.

In Dutton & Tryon (eds.), Language contact and change in the Austronesian world, 351-376. Labu (labu1248, already
in the sheet with Ross 1988's rows under POC, tree_parent nng): the Proto-Huon-Gulf and Proto-Markham innovations
(§4.1), the Lower-Markham innovations Labu shares (§5.1) and the vowel split and loans from Bukawa (§6.1). Composed
onto Labu through Holzknecht's PHG, PMK and PLMK, which are not nodes here (decision ross1988-composition).
"""
from common import Batch, write, chapter, CONSULTED

S = "holzknecht1994"
b = Batch(S)
b.t["sources"].append(dict(
    id="holzknecht1989", author="Holzknecht, Susanne", year="1989",
    title="The Markham languages of Papua New Guinea", kind="comparative", pub_type="book", place="Canberra",
    publisher="Pacific Linguistics", series="Pacific Linguistics C-115",
    notes="Bibliographic details from the reference list of Holzknecht (1994: 374); not consulted directly. The "
          "source of the Markham subgrouping and Proto-Markham reconstructions summarised in Holzknecht (1994)."))
b.t["sources"].append(chapter(
    S, "Holzknecht, Susanne", "The mechanisms of language change in Labu", "351-376",
    CONSULTED + "Labu (Hapa), four villages south of the Markham mouth, Morobe Province. §3: the Markham family "
    "(Holzknecht 1989): Upper Markham (Mari, Adzera, Wampur, Sukurum, Sarasira), Watut (South, Middle, North Watut) "
    "and Lower Markham (Wampar, Musom, Duwet, Nafi, Aribwaungg, Aribwatsa, Labu). §4: phonological, morphosyntactic "
    "and lexical innovations from POC and Proto-Huon-Gulf shared by the Markham languages; §5: Lower-Markham "
    "innovations; §6: features Labu borrowed from Bukawa (seven vowels, tone, verb classes, numerals); §7: "
    "accommodation, bilingualism and structural pressure."))

L = "labu1248"
D = "holzknecht1994-labu"


def r(par, ch, env, page, notes, status="regular", **k):
    b.corr(L, par, ch, env, page, notes, status=status, decision=D, **k)


r("t", "l", "elsewhere", "353-354", "POC *t > PHG *t > PMK *r (§4.1.1), 'which in Labu is realised as /l/ only': "
  "*tagi(s) > PHG *tayis > PMK *rag > LAB lang 'cry'. Bukawa keeps t. As in Ross (1988).",
  as_printed="POC *t > PHG *t > PMK *r")
r("R", "l", "non-final", "353-354", "POC *R (non-final) > PHG *R > PMK *r (§4.1.1): *kaRati > PMK *-garar > LAB "
  "-kalu 'bite'.", as_printed="POC *R (non-final) > PHG *R > PMK *r")
r("r", "l", "non-final", "353-354", "POC *r (non-final) > PHG *r > PMK *r (§4.1.1).",
  as_printed="POC *r > PHG *r > PMK *r")
r("l", "n", "elsewhere", "354-356, 362-363", "POC *l > PHG *l > PMK *l, which split into late PMK *r and *n along "
  "a dialect chain (§4.1.2); in Lower Markham *-l- merged completely with *-n- (§5.1.1): *qulu[ŋa] > PMK *kulub > "
  "PLMK *kunub > LAB ini 'headrest', *qalipan > PLMK *ganif > LAB ani 'centipede', *lopu > late PMK *nafu "
  "'sibling of opposite sex'. Ross (1988) has *l > n only before i, u.",
  as_printed="PMK *-l- merges with PMK *-n- as PLMK *-n-")
r("k", "∅", "lenis grade", "356, 363", "POC *k (lenis) > PHG *ɣ > PMK *g (§4.1.3), lost in Proto-Lower-Markham "
  "(§§5.1.2-5.1.3): *kani > PMK *-gan > LAB -a 'eat', *kuron > PMK *gur > LAB u 'clay pot'.",
  as_printed="PMK *k- and *g- are lost; PMK *-g- is lost")
r("q", "∅", "non-final", "356-357, 363", "POC *q (non-final) > PHG *ɣ > PMK *g (§4.1.3), lost in Proto-Lower-Markham "
  "(§5.1.3): *paqal > PMK *faga- > PLMK *fa(a)- > LAB ha- 'foot, leg'.", as_printed="POC *q > PHG *ɣ > PMK *g")
r("p", "h", "lenis grade", "357", "POC *p (lenis) > PHG *v > PMK *f (§4.1.4), Labu h: *paqal > LAB ha- 'foot, "
  "leg'. As in Ross (1988).", as_printed="POC *p(lenis) > PHG *v > PMK *f")
r("u", "i", "elsewhere", "363, 365", "PMK *u > PLMK *i (§5.1.4): PMK *lijun > LAB nindyi 'seed, fruit', *jufif > "
  "LAB sihi 'march fly', *-ruk > -li 'downwards'.", as_printed="PMK *u > PLMK *i")
for v, ch, ex, st in (("i", "i", "PMK *jinji > si 'Cordyline', *rasi- > lasi(nala) 'yr. sister (fs)'", "regular"),
                      ("i", "e", "PMK *fina- > hêna 'female', *rini- > nênê 'skin, body'", "sporadic"),
                      ("u", "u", "PMK *gur > u 'clay pot', *-fuŋg > -hu 'blow'", "sporadic"),
                      ("u", "o", "PMK *mundu- > môtô 'brother-in-law', *-muŋg > -mô 'go ahead'", "sporadic")):
    r(v, ch, "conditions unknown", "365", "§6.1.1: the five PMK vowels 'split in Labu into i, ê, e, a, o, ô and u in "
      "imitation of Bukawa's vowel system', but 'the splits were irregular': " + ex + ". Labu ê, ô are written as "
      "in Bukawa (close-mid e, o; e and o are the open-mid vowels).", status=st, source_form=ch.replace("e", "ê").replace("o", "ô"))
r("t", "t", "in loans from Bukawa", "366", "§6.1.3: 'Labu has borrowed items from Bukawa which retain POC *t > PHG "
  "*t': *taqi > LAB ta 'faeces', *qate > BUK ŋatê, LAB anatê 'liver', *katimun > BUK gatim, LAB êti 'cucumber'; *topu > "
  "BUK tê, LAB di 'sugarcane'. 'Comparatively rare'; *t is regularly l.", status="loan-stratum")

b.dec(D, "How are Holzknecht's (1994) Markham and Lower-Markham innovations entered?",
      "Composed onto Labu only, through PHG, PMK and PLMK (not nodes here, as for Ross 1988), with the vowel "
      "splits as irregular rows and the Bukawa loans with t as a loan stratum. The other Markham languages, already "
      "entered from Ross (1988), get no rows from this chapter, which cites them as examples, not as "
      "correspondence tables. Holzknecht's subgroups (Upper Markham, Watut, Lower Markham) are not added as groups.",
      "Add Markham and Lower Markham as groups (Glottolog mark1257, lowe1411) under POC; or compose the "
      "innovations onto every Markham language.", "352-366")
write("holzknecht1994-labu", b.t, """# holzknecht1994-labu

Holzknecht, Susanne. 1994. The mechanisms of language change in Labu. In Tom Dutton & Darrell T. Tryon (eds.), *Language contact and change in the Austronesian world*, 351-376. Berlin: Mouton de Gruyter. Generator: `tools/batch_scripts/duttontryon1994/holzknecht.py`.

## Scope

- Labu (`labu1248`): POC > PHG > PMK > PLMK > Labu consonant changes (§§4.1, 5.1), the irregular vowel split after Bukawa (§6.1.1) and Bukawa loans with t (§6.1.3). Decision `holzknecht1994-labu`.

## Not entered

- The Markham subgroups as groups; the new PMK phonemes *p, *t, *kʷ with no POC antecedents (§4.1.5); tone (§6.1.2); morphosyntax and lexicon (§§4.2-4.3, 5.2-5.3, 6.2-6.3).
""")
