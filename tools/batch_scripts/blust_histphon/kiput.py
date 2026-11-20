"""Kiput from Proto-North Sarawak: Blust (2002), §3.2-3.3 and Tables 1-17.

Blust's Kiput spelling: e schwa, é [e], ʔ glottal stop, ë the mid-central glide that ends
the falling diphthongs (ië, éë, uë, oë), c [c͡ç], ñ, ŋ, small capital I and U (lax, in
loans). Rising diphthongs are written -y/-w finally and -i/-u before a final consonant
(ey ~ eiʔ). The PDF's text layer has ¥ for ŋ, ¿ for ʔ and ² for 'fi'; the forms here were
checked against the page images. PNS voiced aspirates are printed with a superscript h.

The rows give PNS segment > Kiput segment, so the long ordered derivations of §3.2 (36
changes, Table 17) are collapsed: each row says in its notes which changes produced it.
"""
L = "kipu1237"
S = "blust2002"
VO = ("'If there was a voiced obstruent anywhere earlier in the word' (p. 406): nasals block, voiceless stops and "
      "liquids generally or sometimes block (pp. 406-407).")


def build(B):
    B.add("lects", id=L, name="Kiput", type="language", glottocode="kipu1237", iso639_3="kyi", parent_id="pns",
          inherit="stated-unchanged", inherit_source_id=S, inherit_page="423",
          inherit_note="Unchanged: 'It will be assumed that no change has taken place unless stated otherwise' "
                       "(Blust 2002: 423), in the summary of shifts, splits and mergers.",
          notes="One longhouse (Long Kiput) on the Baram River, Sarawak; about 450 speakers. Berawan-Lower Baram branch "
                "of North Sarawak (Blust 2002: 384). Blust derives it directly from PNS (p. 385); Lower Baram and "
                "Berawan-Lower Baram nodes are not entered. Glottocode from Glottolog 5.4 (North Sarawakan > "
                "Berawan-Lower Baram > Lower Baram > Central Lower Baram A).",
          orthography_note="Blust's spelling (2002: 385): e is schwa, é a mid front vowel, ë a mid-central glide in "
                           "falling diphthongs, c a voiceless palatal affricate, ʔ the glottal stop; I and U are lax "
                           "vowels of loanwords. Final -ey, -ew are written -ei-, -eu- before a final consonant.")

    # ---- inventory: Table 1 (p. 385) and the vowels and diphthongs of p. 385 and p. 423
    def P(ipa, cls, sym="", page="385", **kw):
        B.P(L, ipa, cls, S, page, sym=sym or ipa, **kw)

    for ipa, sym in [("p", ""), ("t", ""), ("k", ""), ("ʔ", ""), ("b", ""), ("d", ""), ("ɡ", "g"), ("m", ""),
                     ("n", ""), ("ɲ", "ñ"), ("ŋ", ""), ("f", ""), ("s", ""), ("h", ""), ("l", ""), ("r", ""),
                     ("w", ""), ("j", "y")]:
        P(ipa, "C", sym, notes="Table 1 (p. 385).")
    P("c͡ç", "C", "c", place="palatal", manner="affricate", voicing="voiceless",
      notes="'The phoneme c is a voiceless palatal affricate' (p. 385).")
    P("ɟ͡ʝ", "C", "j", place="palatal", manner="affricate", voicing="voiced", status="marginal",
      notes="In parentheses in Table 1 (p. 385).")
    P("ə̯", "C", "ë", manner="approximant",
      notes="'A typologically rare mid-central glide ... identical to schwa except that it occurs only postvocalically "
            "as the coda of a falling diphthong' (p. 385).")
    for ipa, sym, kw in [("i", "", {}), ("ɪ", "I", {"status": "marginal", "notes": "Lax, in Malay loans only (p. 421)."}),
                         ("e", "é", {}), ("u", "", {}),
                         ("ʊ", "U", {"status": "marginal", "notes": "Lax, in Malay loans only (p. 421)."}),
                         ("o", "", {}), ("ə", "e", {}), ("a", "", {}),
                         ("aː", "aa", {"notes": "Stressed vowel lengthening; low vowel length 'has become phonemic' "
                                                "(p. 399)."})]:
        P(ipa, "V", sym, notes=kw.get("notes", "p. 385."), status=kw.get("status", ""))
    DIPH = "One of the 'at least twelve diphthongs' (p. 385); entered as a unit."
    for ipa, sym in [("iw", "iw"), ("ew", "éw"), ("uj", "uy"), ("oj", "oy"), ("əj", "ey"), ("əw", "ew"),
                     ("aj", "ay"), ("aw", "aw"), ("iə̯", "ië"), ("eə̯", "éë"), ("uə̯", "uë"), ("oə̯", "oë")]:
        P(ipa, "V", sym, place="unknown", manner="unknown", notes=DIPH)
    for ipa, sym in [("iə̯j", "iëy"), ("iə̯w", "iëw")]:
        P(ipa, "V", sym, place="unknown", manner="unknown", notes="One of the two triphthongs (p. 385).")
    for ipa, sym in [("aːj", "aay"), ("aːw", "aaw")]:
        P(ipa, "V", sym, page="423", place="unknown", manner="unknown",
          notes="'PNS diphthongs *-ay, *-aw became long diphthongs -aay, -aaw' (p. 423).")

    def C(par, ch, page, env="elsewhere", **kw):
        B.C(L, par, ch, env, src=S, page=page, **kw)

    # ---------------------------------------------------------------- consonants
    # *k (3.2.1.3, 3.2.1.26; 3.3.2.1, 3.3.3.1)
    C("k", "k", 393, env="#_", n=26, tot=28, ex="*kulat > kulaat; *kutu > kutew; *kami > kamay",
      notes="'PNS *k usually remained word-initially' (p. 393).")
    C("k", "∅", 393, env="#_", st="sporadic", n=2, tot=28, sf="Ø", ex="*kabiŋ > abië; *kuyad > ucit")
    C("k", "k", 393, env="V_V", n=14, tot=23, loc="Table 3", ex="*bakas > baka; *bukaq > bukaaʔ; *iket > iket; *tuka > tukeh",
      notes="'Intervocalic *k was lost in about 40 percent of known etymologies, with no clear conditioning factor' "
            "(p. 393); retained between like vowels (eight cases).")
    C("k", "∅", 393, env="V_V", cond="unknown", n=9, tot=23, loc="Table 3", sf="Ø",
      ex="*laki > laay; *paku > paaw; *sakit > séét; *bituka > tufih",
      notes="Tends to be lost after *i (five cases, one exception), where the glide that formed was strengthened to c "
            "(*liku > cew, *siku > ticew) (pp. 393-394). Some doublets may be borrowed (p. 425).")
    C("k", "ʔ", 414, env="i_#, u_#", n=16, loc="Table 14", ex="*betik > betiëʔ; *itik > itéëʔ; *buRuk > buruëʔ; *manuk > manoëʔ; *busak > buiëʔ",
      notes="Final velar lenition: 'wherever VB-2 occurred, final *k became glottal stop' (p. 414), after high vowels "
            "(and *a fronted to i, Table 14 Part B), which took a mid-central offglide.")
    C("k", "k", 414, env="a_#, ə_#", ex="*anak > anaak; *m-asak > masaak; *padek > padek; *utek > utek",
      notes="'Offgliding did not affect PNS *e, or PNS *a that was not affected by low vowel fronting, and following "
            "these vowels final *k and *ŋ did not change' (p. 414).")
    # *ʔ (PNS *q)
    C("ʔ", "∅", 392, env="V_V", sf="Ø", ex="*aqal > aan; *daqan > din; *paqit > péét; *taqun > toon",
      notes="'In Kiput, medial *q was also lost' (p. 392). Blust writes PNS *q for the glottal stop.")
    C("ʔ", "ʔ", 395, env="_#", ex="*ataq > ataaʔ; *bukaq > bukaaʔ; *utaq > utaaʔ", notes="Retained finally (p. 426).")
    # *ŋ (FVL)
    C("ŋ", "∅", 414, env="i_#, u_#", sf="Ø", loc="Table 14", ex="*kabiŋ > abië; *dindiŋ > dirië; *busuŋ > busuë; *munuŋ > munoë; *padaŋ > padië",
      notes="Final velar lenition: 'final *ŋ disappeared' after the offglided high vowels (p. 414).")
    C("ŋ", "ŋ", 414, ex="*bataŋ > bataaŋ; *tulaŋ > tulaaŋ; *tebʰeŋ > tepeŋ",
      notes="Unchanged after *a not fronted and after *ə (p. 414), and nonfinally.")
    # voiced stops (3.2.1.24 IVD, 3.2.1.36 FD)
    FD = "Final devoicing (p. 419): 'Final voiced stops are rare in PNS in comparison with their voiceless counterparts.'"
    C("b", "b", 411, ex="*abu > abew; *babuy > babuy; *iban > ibin; *lubuk > lubuëʔ; *tuba > tubih",
      notes="'Intervocalic *b and *d did not devoice. Rather, *b invariably remained a voiced bilabial stop' (p. 411).")
    C("b", "p", 419, env="_#", n=1, ex="*Ruab > lufiëp", notes=FD)
    C("d", "d", 415, ex="*adaq > adeiʔ; *adan > adin; *ida > idih; *kuda > kudih; *t-adi > tadey",
      notes="'PNS *d generally remained unchanged in nonfinal position (23 cases in the appendix)' (p. 415).")
    C("d", "r", 415, env="conditions unknown", n=5, ex="*adeŋ > areŋ; *dindiŋ > dirië; *kiday > kiraay; *kuduq > kurauʔ; *iduŋ > roë",
      notes="Blust takes the r of dirië and roë as reflexes of *nd (p. 415); areŋ may be a Malay loan.")
    C("d", "l", 415, env="conditions unknown", n=2, ex="*belida > belilih; *diRi > pe-lirey",
      notes="Both show assimilation or dissimilation to a liquid in an adjacent syllable (p. 415).")
    C("d", "s", 415, st="loan-stratum", n=2, ex="*dadem > dasem; *dilaq > silaaʔ",
      notes="Kiput deleiʔ 'tongue' and silaaʔ 'lick' both reflect *dilaq; Blust takes silaaʔ as the loan and suggests "
            "the other cases of *d > s are borrowed too (p. 415).")
    C("d", "t", 415, env="#_", st="sporadic", n=1, ex="*dalem > talom", notes="Probably borrowed; alem 'inside' is native (p. 415).")
    C("d", "∅", 425, env="#_", st="sporadic", n=1, sf="Ø", ex="*dalem > alem")
    C("d", "t", 419, env="_#", ex="*alud > alot; *likud > cut; *dalid > dalét; *laled > lalet; *tumid > tumét", notes=FD)
    C("j", "d", 418, env="#_", n=4, loc="Table 16", ex="*jaway > dafiëy; *jalan > dalaan; *janiq > danaiʔ; *jameq > dimeʔ",
      notes="'PNS *j (from PMP *z ...) split three ways in Kiput ... it is difficult to state conditions' (p. 418).")
    C("j", "ɟ͡ʝ", 418, env="#_", cond="unknown", n=2, sf="j", loc="Table 16", ex="*jauq > jeuʔ; *ajay > jey")
    C("j", "s", 418, env="#_", cond="unknown", n=2, loc="Table 16", ex="*jaqet > saat; *jelutuŋ > selutoë",
      notes="Blust suggests *j > d > s, perhaps by borrowing (p. 415).")
    C("j", "c͡ç", 418, env="V_V", sf="c", loc="Table 16", ex="*pujut > pucut; *tajem > tacem; *tujuq > ticeuʔ; *ujuŋ > ucuë; *ijam > p-iciëm",
      notes="Intervocalic devoicing (pp. 410-411): 'PNS *j, *g, and the phonetic glides [y] and [w] ... underwent "
            "this change, while *b and *d did not.'")
    C("g", "ɡ", 411, env="#_", sf="g", n=6, ex="*gaduŋ > gaduë; *gatel > gaten; *gelaŋ > gelië",
      notes="'PNS *g and *j did not normally devoice in initial position' (p. 411). Exception *tegeRaŋ > tegerië.")
    C("g", "k", 411, env="#_", st="sporadic", n=1, ex="*guta-an > ketaan")
    C("g", "k", 410, env="V_V", ex="*pager > pakin; *tugal > tukin", notes="Intervocalic devoicing (p. 410).")
    # voiced aspirates (3.2.1.22-23)
    ASP = "'It is more likely that these four phonetically complex phonemes ... changed together' (p. 408)."
    C("bʰ", "s", 408, n=7, loc="Table 12", ex="*bebʰal > basin; *bubʰuk > busuëʔ; *ebʰaq > seiʔ; *ebʰuk > suëʔ; *tebʰu > tesew",
      ap="*bʰ > f; *f > s", notes=ASP + " Through *f, which other Lower Baram languages keep (Dahl's proposal; p. 409).")
    C("bʰ", "p", 409, st="loan-stratum", n=3, ex="*bubʰun > bupun; *tebʰek > tepek; *tebʰeŋ > tepeŋ",
      notes="'The forms with *bh > p may be loans from Long Terawan Berawan' (p. 409).")
    C("dʰ", "s", 408, loc="Table 12", ex="*bedʰek > pesek; *pedʰu > peseuʔ; *tedʰaq > tesaaʔ; *tidʰaq > teseiʔ", notes=ASP)
    C("jʰ", "s", 408, loc="Table 12", ex="*ejʰan > asin; *ejʰa > sih", notes=ASP)
    C("gʰ", "k", 408, ex="*pegʰel > peken", notes=ASP + " 'The few examples of the latter have all become k' (p. 427).")
    # nasals
    C("n", "l", 417, env="#_", n=3, ex="*nanaq > lanaaʔ; *nipa > lipah; *nupi > lupay",
      notes="'It is possible that *n > l was regular in initial position' (p. 418); *nibuŋ > nibuë would then be a loan.")
    C("n", "n", 417, ex="*bana > baneh; *t-ina > tineh; *kena > keneh; *una > uneh", notes="'20 instances of *n > n' medially (p. 417).")
    C("n", "l", 417, env="V_V", st="sporadic", n=1, ex="*me-nipis > melipay")
    C("ñ", "ɲ", 385, sf="ñ", ex="*peñu > peñew; *teñel > teñen", notes="Unchanged; written ñ.")
    # *s (3.2.1.9, 3.2.1.16, 3.2.1.35)
    C("s", "s", 397, env="#_", n=12, tot=13, ex="*sakit > séét; *silaq > sileiʔ; *sepaq > sepaaʔ",
      notes="'In initial position, *s almost always is retained (12 cases, one exception)' (p. 397).")
    C("s", "∅", 397, env="#_", st="loan-stratum", n=1, tot=13, sf="Ø", ex="*sakit > akét",
      notes="'The single exception is akét ... suggesting that the former word is a loan' (p. 397).")
    SV = "'There is little obvious basis for the split of *s intervocalically' (p. 397): 10 cases each (p. 425)."
    C("s", "s", 397, env="V_V", n=10, tot=20, loc="Table 6", notes=SV, ex="*m-asak > m-asaak; *busuŋ > busuë; *m-asem > masem")
    C("s", "∅", 397, env="V_V", cond="unknown", n=10, tot=20, loc="Table 6", sf="Ø", notes=SV,
      ex="*um-asaq > maaʔ; *pusuq > peuʔ; *Rusuk > roëʔ; *lisa > lieh; *usek > uek")
    C("s", "∅", 397, env="_#", n=10, sf="Ø", ex="*Ratas > lata; *beRas > berey; *taŋis > taŋay; *Ratus > lataw",
      notes="'In final position, *s invariably disappeared (10 cases, no exceptions)' (p. 397).")
    C("s", "t", 418, env="#_ (sibilant in the next syllable)", n=3, ex="*sasaq > tasaaʔ; *siku > ticew; *sisiŋ > tiséë",
      notes="Sibilant dissimilation (p. 418), after *siku had become *sicew.")
    # liquids (3.2.1.12-13, 3.2.1.18, 3.2.1.32)
    C("l", "l", 400, n=57, tot=66, ex="*laki > laay; *lima > limeh; *bilaq > bileiʔ; *ŋilu > ŋilaw",
      notes="'In most cases (57 in the appendix), nonfinal *l was retained' (p. 400).")
    C("l", "∅", 400, env="conditions unknown", n=9, tot=66, loc="Table 8", sf="Ø",
      ex="*lamin > amén; *lubaŋ > lubië/ubië; *kilat > kicet; *tiluR > ticeuʔ",
      notes="'No condition can be stated for this change' (p. 401); perhaps a change in progress.")
    LN = "'PNS final liquids merged with *n as a word-final alveolar nasal in Kiput' (p. 417)."
    C("l", "n", 417, env="_#", loc="Table 15", notes=LN, ex="*aqal > aan; *gatel > gaten; *putul > puton; *tugal > tukin")
    C("r", "n", 417, env="_#", loc="Table 15", notes=LN, ex="*pager > pakin")
    C("r", "r", 417, notes="Unchanged nonfinally.")
    C("R", "l", 400, env="#_", n=6, tot=7, loc="Table 7", ex="*Ramut > lamut; *Ribu > libew; *Ratus > lataw",
      notes="'In initial position the change *R > l is attested six times, while *R > r is attested only once' (p. 400).")
    C("R", "r", 400, env="#_", st="sporadic", n=1, tot=7, loc="Table 7", ex="*Rusuk > roë",
      notes="Perhaps already monosyllabic when *R changed (p. 400).")
    C("R", "r", 400, env="V_V", n=16, tot=19, loc="Table 7", ex="*baReq > baraaʔ; *buRuk > buruëʔ; *taRiŋ > taréë",
      notes="'Intervocalically *R generally became r (16 cases, three exceptions)' (p. 426).")
    C("R", "l", 400, env="V_V", st="sporadic", n=3, tot=19, loc="Table 7", ex="*diRi > pe-lirey; *geRami > gelamay",
      notes="More often in words that were or became trisyllabic (p. 400).")
    C("R", "∅", 400, env="#_, V_V", st="sporadic", n=2, sf="Ø", ex="*Rabut > abut; *suRat > suiët",
      notes="Blust takes these through *l and its loss (p. 400).")
    RF = "'In final position, PNS *R became n in four known cases, ʔ in three others, and Ø in one more' (p. 426)."
    C("R", "n", 417, env="_#", n=4, tot=8, notes=RF + " " + LN, ex="*apuR > apun; *atuR > ŋ-aton; *besuR > besun; *sandaR > sattin")
    C("R", "ʔ", 404, env="_#", cond="unknown", n=3, tot=8, notes=RF, ex="*buleR > buleʔ; *ikuR > ceuʔ; *tiluR > ticeuʔ")
    C("R", "∅", 405, env="_#", st="sporadic", n=1, tot=8, sf="Ø", notes=RF, ex="*temedʰuR > temesu")
    # glides (3.2.1.14, Table 9; 3.2.1.24)
    C("w", "f", 402, env="V_V", loc="Table 9", ex="*jaway > dafiëy; *pawat > pafiët",
      notes="Glide fortition, then intervocalic devoicing (*w > v > f) (pp. 401-411).")
    C("w", "w", 423, env="_#", ex="*danaw > danaaw; *kasaw > kasaaw", notes="In the long diphthong -aaw (p. 423).")
    C("y", "c͡ç", 411, env="V_V", sf="c", ex="*kayu > kacew; *kuyu > kucew",
      notes="Glide fortition, then intervocalic devoicing (*y > j > c) (Table 13, p. 410). Irregular: *ayam > añim.")
    C("y", "j", 423, env="_#", sf="y", ex="*anay > anaay; *m-atay > m-ataay; *kiday > kiraay", notes="In the long diphthong -aay (p. 423).")
    GF = ("The transitional glide between a high vowel and an unlike vowel was strengthened and then devoiced (glide "
          "fortition, intervocalic devoicing; pp. 401-411). The high vowel before it sometimes became schwa or was lost "
          "with the initial syllable, irregularly (p. 403).")
    C("∅", "f", 402, env="u_V", loc="Table 9", notes=GF, ex="*dua > dufih; *Ruab > lufiëp; *bituka > tufih; *beRuaŋ > belufië; *uay > fiëy")
    C("∅", "c͡ç", 402, env="i_V", sf="c", loc="Table 9", notes=GF,
      ex="*diaq > ceiʔ; *lia > lecih; *tian > ticin; *liku > cew; *kilat > kicet; *tiluR > ticeuʔ")
    C("∅", "h", 396, env="a_#", loc="Table 5", ex="*bana > baneh; *mata > mateh; *dua > dufih; *ida > idih",
      notes="'The glottal fricative h was added after PNS final *a, whether this segment remained a low vowel or whether "
            "it was raised and fronted to i' (p. 396).")

    # ---------------------------------------------------------------- vowels (final syllable)
    VB1 = ("Vowel Breaking-1 made final high vowels (and those before final *q, *R, *s) into diphthongs -ey, -ew; "
           "lowering of diphthongal nuclei then gave -ay, -aw 'unless a voiced obstruent occurs earlier in the word' "
           "(pp. 396, 407-408). " + VO)
    C("i", "aj", 396, env="_#, _ʔ#, _s#", sf="ay", loc="Table 4, Table 11", notes=VB1,
      ex="*kami > kamay; *nupi > lupay; *tali > talay; *taŋis > taŋay; *m-uliq > m-ulaiʔ; *janiq > danaiʔ")
    C("i", "əj", 396, env="_#, _ʔ#, _s# after a voiced obstruent", sf="ey", loc="Table 4, Table 11", notes=VB1,
      ex="*duRi > durey; *gumi > gumey; *t-adi > tadey; *ubi > ubey; *pedʰiq > peseiʔ")
    C("u", "aw", 396, env="_#, _ʔ#, _s#", loc="Table 4, Table 11", notes=VB1,
      ex="*batu > bataw; *silu > silaw; *telu > telaw; *puluq > pulauʔ; *Ratus > lataw")
    C("u", "əw", 396, env="_#, _ʔ#, _s# after a voiced obstruent", sf="ew", loc="Table 4, Table 11", notes=VB1,
      ex="*abu > abew; *bulu > bulew; *Ribu > libew; *tebʰu > tesew; *buluq > buleuʔ; *kayu > kacew")
    VB2 = ("Vowel Breaking-2: 'high vowels acquired a mid-central offglide before final *k and *ŋ' (p. 413), and final "
           "*k became ʔ and final *ŋ was lost. High vowels lowered first in about half the words (p. 404), giving éë, oë.")
    C("i", "iə̯", 413, env="_k#, _ŋ#", sf="ië", loc="Table 14", notes=VB2, ex="*betik > betiëʔ; *tedʰik > tesiëʔ; *kabiŋ > abië; *dindiŋ > dirië")
    C("i", "eə̯", 413, env="_k#, _ŋ#", cond="unknown", sf="éë", loc="Table 14", notes=VB2,
      ex="*belatik > belatéëʔ; *itik > itéëʔ; *kesiŋ > séë; *taRiŋ > taréë; *sisiŋ > tiséë")
    C("u", "uə̯", 413, env="_k#, _ŋ#", sf="uë", loc="Table 14", notes=VB2,
      ex="*m-abuk > m-abuëʔ; *buRuk > buruëʔ; *lubuk > lubuëʔ; *busuŋ > busuë; *gaduŋ > gaduë")
    C("u", "oə̯", 413, env="_k#, _ŋ#", cond="unknown", sf="oë", loc="Table 14", notes=VB2,
      ex="*batuk > batoëʔ; *manuk > manoëʔ; *katuŋ > katoë; *munuŋ > munoë; *tuluŋ > tuloë")
    LHV = ("Lowering of high vowels 'before final alveolar, palatal, and velar consonants' in about half the etymologies "
           "(20 with, 17 without); 'no conditioning factor has been identified' (p. 404).")
    C("i", "e", 404, env="_C#", cond="unknown", sf="é", loc="Table 10", notes=LHV,
      ex="*sakit > akét; *lamin > amén; *atip > atép; *dalid > dalét; *kulit > kulét; *laŋit > laŋét")
    C("u", "o", 404, env="_C#", cond="unknown", loc="Table 10", notes=LHV, ex="*lulud > lulot; *etut > tot; *laŋuy > pe-laŋoy")
    C("i", "i", 404, notes="Unchanged elsewhere, including before a final consonant in about half the words (p. 404).")
    C("u", "u", 404, notes="Unchanged elsewhere, including before a final consonant in about half the words (p. 404).")
    C("i", "oj", 404, env="_+w", n=2, sf="oy", ex="*baRiw > baroy; *baliw > saloy",
      notes="'In the two available examples, the PNS diphthong *-iw metathesized' (p. 404), and lowered.")
    C("w", "oj", 404, env="i+_", n=2, sf="oy", ex="*baRiw > baroy; *baliw > saloy")
    # *a
    C("a", "ə", 396, env="_#", sf="e", loc="Table 5", ex="*bana > baneh; *lima > limeh; *mata > mateh; *t-ina > tineh; *tuka > tukeh",
      notes="Final *a, with -h added (p. 396).")
    LVF = "Low vowel fronting (pp. 406-407): last-syllable *a became i " + VO
    C("a", "i", 406, env="_# after a voiced obstruent", loc="Table 5", notes=LVF,
      ex="*depa > depih; *dua > dufih; *ida > idih; *kuda > kudih; *tuba > tubih; *ejʰa > sih")
    C("a", "a", 397, env="_s#", ex="*Ratas > lata; *teRas > tera", notes="Final *s lost after -h was added, so no h (p. 396).")
    C("a", "əj", 422, env="_s# after a voiced obstruent", sf="ey", ex="*beRas > berey",
      notes="Low vowel fronting, then Vowel Breaking-1 (Figure 5, p. 424).")
    C("a", "aː", 399, env="_C#", sf="aa", ex="*anak > anaak; *anay > anaay; *bataŋ > bataaŋ; *m-atay > m-ataay; *danaw > danaaw; *ataq > ataaʔ",
      notes="Stressed vowel lengthening 'before any final consonant except h' (p. 399), including the coda of *-ay, *-aw "
            "(p. 423).")
    C("a", "i", 406, env="_C# after a voiced obstruent", loc="", notes=LVF,
      ex="*adan > adin; *beRat > berit; *dadan > dadin; *iban > ibin; *tugal > tukin; *ejʰan > asin")
    C("a", "əj", 395, env="_ʔ# after a voiced obstruent", sf="ei", loc="Table 11",
      ex="*adaq > adeiʔ; *bilaq > bileiʔ; *diaq > ceiʔ; *ebʰaq > seiʔ; *tidʰaq > teseiʔ",
      notes="Low vowel fronting, then Vowel Breaking-1, 2nd cycle (pp. 395, 407).")
    C("a", "iə̯", 413, env="_k#, _ŋ# after a voiced obstruent", sf="ië", loc="Table 14",
      ex="*busak > buiëʔ; *burak > buriëʔ; *gelaŋ > gelië; *padaŋ > padië; *tegeRaŋ > tegerië",
      notes="Low vowel fronting, then Vowel Breaking-2 (p. 413).")
    C("a", "a", 399, env="nonfinal syllable", notes="Low vowel fronting affected only the last syllable (p. 406).")
    # *ə
    C("ə", "∅", 417, env="#_", sf="Ø", ex="*eluŋ > loë; *enem > nem; *epat > paat; *ebʰaq > seiʔ; *etut > tot",
      notes="'PNS *e (schwa) disappeared word-initially' (p. 417); Blust writes PNS schwa *e. Exception *ejʰan > asin.")
    C("ə", "aː", 395, env="_ʔ#", sf="aa", n=2, ex="*baReq > baraaʔ; *taneq > tanaaʔ",
      notes="'*-eq became pre-Kiput -aʔ', merging with *-aq before stressed vowel lengthening (p. 395).")
    C("ə", "əj", 395, env="_ʔ# after a voiced obstruent", sf="ei", n=1, ex="*baseq > beiʔ")
    C("ə", "a", 415, env="_C#", ex="matep/matap; let/lat; pesek/pesak; mitem/mitam; areŋ/araŋ",
      notes="'This is a change in progress, shown by the variation that Kiput speakers allow' (p. 415); not in the "
            "diphthongs.")
    C("ə", "o", 404, env="_p#, _m#", st="sporadic", n=2, ex="*sakep > sakop; *dalem > talom",
      notes="'An apparently sporadic change of *e to u preceding a final labial consonant, with subsequent lowering' "
            "(p. 404).")
    C("ə", "ə", 415, notes="Unchanged elsewhere; written e.")
