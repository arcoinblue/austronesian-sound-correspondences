#!/usr/bin/env python3
"""Blevins & Garrett (1993), The evolution of Ponapeic nasal substitution.

The sound changes of §4 (18): Proto-Ponapeic geminate preaspiration (TT > hT) and prothesis, then aspirate
nasalisation (hT > NT) in Mokilese and Pohnpeian and h-loss with compensatory lengthening in Pingelapese;
Pohnpeian loss of the prothetic vowel (15e). Pingelapese n allophones from (1).
"""
from common import Batch, write

S = "blevinsgarrett1993"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Blevins, Juliette; Garrett, Andrew", year="1993", title="The evolution of Ponapeic nasal substitution",
    url_or_doi="https://www.jstor.org/stable/3623193", kind="comparative",
    notes="Consulted directly on 24 November 2026 (JSTOR PDF in Downloads; table (1) read from the page image).",
    pub_type="article", container_title="Oceanic Linguistics", volume="32", issue="2", pages="199-236"))
D = "blevinsgarrett1993-preaspiration"
GEMN = ("The geminates arose in Proto-Ponapeic-Trukic by syncope and total regressive assimilation (*CiVCj > *CiCj > "
        "*CjCj, (15a)), mostly across reduplication boundaries. ")

# PPON (parent PPC): Geminate Preaspiration TiTi > hTi (18a), and prothesis (15b-i)
PRE = ("'Geminate Preaspiration: TiTi > hTi' (18a), a Proto-Ponapeic change (p. 215): the first half of a voiceless "
       "geminate obstruent becomes h. " + GEMN)
for par, ex in (("p", "*pap-pap > *pah-pap 'swimming' (19)"), ("pʷ", "*pʷpʷul 'flame' (6e)"), ("k", "*kkol (6c)"),
                ("d", "*ttil (6d); B&G's PPON *t is Bender et al.'s *d (table (1))"),
                ("t", "PPC *t, PPON *j (Bender et al.), B&G's *c"),
                ("c", "*cca 'blood' > *icca > *ihca (19); B&G's *č (table (1)), Bender et al.'s *c")):
    b.corr("ppon", par, "h", f"_{par} (first half of a geminate)", "215-216", PRE + ex + ".", derivation="",
           as_printed="TiTi > hTi", decision=D, locator="(18a)")
PROT = ("'High vowel prothesis before initial geminates' (15b-i), a Proto-Ponapeic innovation after Rehg (1984), "
        "Harrison (1984): *cca > *icca 'blood'. ")
b.corr("ppon", "∅", "i", "#_CC (an initial geminate)", "206, 211-212", PROT, derivation="", as_printed="prothesis",
       decision=D)
b.corr("ppon", "∅", "u", "#_CC (an initial velarised geminate before a round vowel)", "206", PROT +
       "'a prothetic i (or u before velarized consonants or clusters followed by round vowels)' (p. 206): Mok "
       "umʷpʷul 'flaming'.", derivation="", as_printed="prothesis", decision=D)
b.t["notation_map"].append(dict(lect_id="ppon", phoneme="h", system="canonical", symbol="h", source_id=S, page="215",
    notes="The h of Proto-Ponapeic preaspirated geminates hT (Blevins & Garrett 1993: (18a)); found only before a "
          "voiceless obstruent (decision blevinsgarrett1993-preaspiration).", place="glottal", manner="fricative",
          voicing="voiceless"))

# Mokilese, Pohnpeian: Aspirate Nasalization hTi > NiTi (18b)
NAS = ("'Aspirate Nasalization: hTi > NiTi' (18b), in Mokilese and Pohnpeian (p. 215), through 'rhinoglottophilia' "
       "(§6); the source of synchronic Nasal Substitution, later levelled away in Mokilese. ")
for L, ex in (("pohn1238", "Pnp pampap 'swimming', nca 'blood', mʷpʷul 'flame'"),
              ("moki1238", "Mok insa 'blood', umʷpʷul 'flaming', iŋkoŋ 'sharp'")):
    for par, nas in (("p", "m"), ("pʷ", "mʷ"), ("k", "ŋ"), ("d", "n"), ("j", "n"), ("c", "n")):
        b.corr(L, "h", nas, f"_{par}", "215-216", NAS + ex + ".", derivation="", as_printed="hTi > NiTi",
               decision=D, locator="(18b)")
b.corr("pohn1238", "i", "∅", "#_NC (the prothetic vowel)", "206, 211-212",
       "'\"Optional\" prothetic vowel loss' (15e): Pnp nsar ~ insar 'snare', nca 'blood' beside Mok insa; Rehg "
       "(1984) takes the prothetic vowel as a Proto-Ponapeic innovation now being lost (p. 206).",
       status="sporadic", derivation="", as_printed="optional prothetic vowel loss", decision=D, conditioning="")
# Pingelapese: h loss with compensatory lengthening
b.corr("ping1243", "h", "∅", "V_C (the preceding vowel lengthens)", "212, 215",
       "In Pingelapese 'by h loss with compensatory vowel lengthening' (p. 215): iisa 'blood', iitil 'to torch "
       "fish', tootol 'to pick' (9); Pingelapese V:C answers Ponapean VNC. Words with VNC are loans from Pohnpeian "
       "or later formations (pp. 208-210).", derivation="", as_printed="hT > V:T", decision=D)
# Pingelapese n (table (1))
b.allo("ping1243", "n", "n", "free variation", "200", "Table (1): Pingelapese n [n ~ n̪].")
b.allo("ping1243", "n", "n̪", "free variation", "200", "Table (1): Pingelapese n [n ~ n̪].")

b.dec(D, "Blevins & Garrett (1993) derive Ponapeic Nasal Substitution from Proto-Ponapeic geminate preaspiration "
         "(TT > hT) and later aspirate nasalisation (hT > NT). How are the changes entered?",
      "As segment rows: PPON *p, *pʷ, *k, *d, *t, *c > h before the same consonant (the first half of a geminate), "
      "so PPON has an *h (canonical notation row) found only before a voiceless obstruent; Pohnpeian and Mokilese h "
      "> m, mʷ, ŋ, n before the obstruent, Pingelapese h > ∅ with the vowel lengthened; prothetic i, u at PPON and "
      "its optional loss in Pohnpeian. B&G's PPON *t, *c, *č are Bender et al.'s *d, *j, *c (table (1)).",
      "Only notes on the PPON page, as with the syncope and assimilation of Proto-Ponapeic-Trukic (not entered).",
      "206-216")

md = """# blevinsgarrett1993-ponapeic

Blevins, Juliette & Andrew Garrett. 1993. The evolution of Ponapeic nasal substitution. *Oceanic Linguistics* 32(2). 199-236. Read from the JSTOR PDF in Downloads; table (1) from the page image. Generator: `tools/batch_scripts/five_sources_2026_11_24/blevinsgarrett1993.py`.

## Scope

- The sound changes of §4 (18), with the stages of (15): PPON geminate preaspiration TT > hT and high-vowel prothesis before initial geminates; aspirate nasalisation hT > NT in Mokilese and Pohnpeian; Pingelapese h loss with compensatory lengthening; Pohnpeian optional loss of the prothetic vowel (decision `blevinsgarrett1993-preaspiration`).
- Pingelapese n [n ~ n̪] (table (1)).

## Not entered

- The PPC syncope and total regressive assimilation (*CiVCj > *CiCj > *CjCj): no segment rows (the rows above name the geminate in the environment).
- Table (1) as rows: it restates the coronal correspondences of Bender et al. in B&G's symbols (PPON *t, *c, *č = Bender et al.'s *d, *j, *c); single phonetic values (Pingelapese, Pohnpeian t [t̪], Pohnpeian s [sʸ], n [n̪], l [l̪], Pingelapese l [ɫ]) are not allophones.
- The synchronic rules NS-I and NS-II of Pohnpeian (§1.1), the phonetics of §§5-6, the cross-linguistic parallels.
"""
write("blevinsgarrett1993-ponapeic", b.t, md)
