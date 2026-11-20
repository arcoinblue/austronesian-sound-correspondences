"""Chamorro from PMP: Blust (2000), read from the page images.

Chamorro spelling in Blust (after Topping, Ogo & Dungca 1975): ' glottal stop, ch [ts],
y [dz] (final [j] in Blust's -ay, -aw, -uy respelling, p. 85), ñ, ng, gw [ɡʷ]. Forms are
copied as printed, including the places where Blust's own spelling varies (see BATCH.md).
"""
L = "cham1312"
S = "blust2000"


def build(B):
    B.add("lects", id=L, name="Chamorro", alt_names="Chamoru", type="language", glottocode="cham1312",
          iso639_3="cha", parent_id="pmp",
          notes="Mariana Islands. Blust (2000) states its reflexes against PMP (p. 88) and finds no subgroup between "
                "the two: Chamorro is a primary branch of Malayo-Polynesian with no close relatives (§4, pp. 103-104). "
                "Glottocode from Glottolog 5.4.",
          orthography_note="Topping's spelling as Blust (2000: 84-85) uses it: ' glottal stop, ch [ts], y [dz] "
                           "(Blust respells final -ai, -ao, -ui as -ay, -aw, -uy), ñ, ng, gw. Low front æ is not "
                           "written in the dictionary; Blust marks it as ([æ]).")

    # ---- inventory: Topping (1973: 16, 27) as reported by Blust (2000: 84-85)
    def P(ipa, cls, sym="", page="84", **kw):
        B.P(L, ipa, cls, "topping1973", "27" if cls == "C" else "16", sym=sym, via=S, viap=page, **kw)

    LOAN = "Only in known or presumed loanwords (Blust 2000: 84)."
    for ipa, sym, kw in [("p", "", {}), ("t", "", {"notes": "Typically alveolar, postdental for some speakers (p. 84)."}),
                         ("k", "", {"notes": "Blust (p. 84) lists k with b, d and r as found only in loanwords, but "
                                             "gives six native words with final *k > k (p. 94); entered as a native "
                                             "phoneme (decision cha-k)."}),
                         ("ʔ", "'", {}), ("b", "", {"status": "marginal", "notes": LOAN}),
                         ("d", "", {"status": "marginal", "notes": LOAN}), ("ɡ", "g", {}),
                         ("t͡s", "ch", {"notes": "[ts] (p. 84)."}),
                         ("d͡z", "y", {"notes": "[dz], 'the voiced counterpart of ch' (p. 84). Blust treats final "
                                               "[j] of the diphthongs as its allophone (p. 85; decision cha-y)."}),
                         ("f", "", {}), ("s", "", {}), ("h", "", {}), ("m", "", {}), ("n", "", {}), ("ɲ", "ñ", {}),
                         ("ŋ", "ng", {}), ("l", "", {}), ("r", "", {"status": "marginal", "notes": LOAN}),
                         ("w", "", {"notes": "Very rare (p. 85); with Blust's respelling it occurs finally in -aw."})]:
        P(ipa, "C", sym, **kw)
    P("ɡʷ", "C", "gw", place="velar",
      notes="Not in Topping's list of 19; Blust adds the labiovelar, 'treated as a sequence gu before a vowel, but which "
            "patterns like a single consonant' (p. 84).")
    for ipa, kw in [("i", {}), ("e", {}), ("æ", {"notes": "'Of obscure origin', not written in the dictionary's main "
                                                          "entries (p. 85)."}),
                    ("u", {}), ("o", {}), ("a", {})]:
        P(ipa, "V", page="85", **kw)

    def C(par, ch, page, env="elsewhere", **kw):
        B.C(L, par, ch, env, src=S, page=page, **kw)

    # ---- vowels (§3.1, pp. 88-93)
    C("e", "u", 88, ap="Rule 1: *e > u", ex="*Rebek > gupu; *beRas > pugas; *tebuh > tupu; *qenay > unay",
      notes="'*a, *i, and *u remained unchanged, while *e merged with *u' (p. 88).")
    C("e", "∅", 88, env="VC_CV", ap="Rule 2: *V > Ø / VC__CV", n=14, tot=14, loc="Table 1",
      ex="*qalejaw > atdaw; *huqenap > go'naf; *aRemaŋ > h-akmang; *baqeRu > pa'go; *tuqelaŋ > to'lang",
      notes="'Only *e was consistently deleted': 14 deleted, none retained in the environment (Table 1, p. 89).")
    for v, ch, n, tot, ex in [("i", "∅", 5, 16, "*qali-maŋaw > akmangaw, atmangaw; *qanitu > anti; *qasin-i > asn-e; "
                                                "*baRiuh > pakyo; *taŋis-i > tangs-e"),
                              ("u", "∅", 1, 9, "*tutuŋ-i > totng-e"),
                              ("a", "∅", 2, 14, "*ma-qati > ma-ma'te, ma'te; *sakay-an > sahy-an")]:
        C(v, ch, 89, env="VC_CV", st="sporadic", n=n, tot=tot, loc="Table 1", ap="*V > Ø / VC__CV", ex=ex,
          notes="Syncope of a vowel other than *e (Table 1, p. 89; Table 2, p. 91). Blust finds it tends to follow "
                "Proto-Philippine stress but cannot predict it (pp. 89-92).")
    C("i", "i", 88, notes="Unchanged (p. 88), outside the conditions of the rows below.")
    C("u", "u", 88, notes="Unchanged (p. 88), outside the conditions of the rows below.")
    C("a", "a", 88, notes="Unchanged (p. 88).")
    LOW = ("'Another vocalic change was the lowering of high vowels in closed syllables, which presumably followed rule 1' "
           "(p. 92). Allophonic at first; e and o became phonemes through Spanish loans.")
    C("i", "e", 92, env="closed syllable", ap="Rule 3: *i, *u > e, o / __C+, /__C#", notes=LOW,
      ex="*peRes-i > foks-e; *mekmek > mohmo")
    C("u", "o", 92, env="closed syllable", ap="Rule 3: *i, *u > e, o / __C+, /__C#", notes=LOW,
      ex="*qapuR > afok; *zauq > chago'; *pa-lulun > falulon; *dalem > halom; *quRut > ugot; *nusnus > nosnos")
    FIN = ("'Rather surprisingly, word-final high vowels also lowered in many cases following a consonant cluster' "
           "(p. 92), so the referential-focus suffix -i has the allomorph -e. *ken > hun did not lower.")
    C("i", "e", 92, env="CC_#", notes=FIN, ex="*qatep-i > aft-e; *ma-qati > ma-ma'ti, ma-ma'te; *salaR-i > satg-e; *teken > tohn-e")
    C("u", "o", 92, env="CC_#", notes=FIN, ex="*kamiu > hamyo; *baqeRu > pa'go; *baRiuh > pakyo")
    C("u", "i", 92, st="sporadic", n=6, sf="i, e",
      ex="*qaninuŋ > anineng; *qanitu > anti; *inum > gimen; *ijuŋ > gwi'eng; *linduŋ > liheng; *butuŋ > puteng",
      notes="'Unexpected front vowel reflexes of *u or *e in eight forms' (pp. 92-93); e where rule 3 lowered the "
            "vowel. *inum > gimen is a problematic etymology (n. 8).")
    C("e", "i", 92, st="sporadic", n=2, sf="e, i", ex="*nipen > nifen; *beRŋi > pwengi",
      notes="The other two of the eight forms with a front vowel for *u or *e (p. 92).")
    C("i", "u", 93, st="sporadic", n=3, ex="*kasili > hasuli; *dilaq > hula'; *tian > tuyan",
      notes="'*i is reflected as a back vowel in three words' (p. 93): Blust suggests back-formation after a variation "
            "u ~ i arose from the merger of *e and *u.")
    C("a", "æ", 93, env="conditions unknown", sf="a ([æ])",
      ex="*paqit > fa'et ([æ]); *kamiu > hamyo ([æ]); *qudaŋ > uhang ([æ]); lahen ([æ])",
      notes="'This apparently unconditioned phonemic split' (p. 93); a stays in ma-'ase', halihan, uchan in the same "
            "environment, and *laki > lahi has a beside lahen ([æ]).")

    # ---- diphthongs (§3.2, pp. 93-94)
    C("a", "i", 93, env="_+y", st="sporadic", n=1, ex="*pajay > fa'i", ap="*-ay > -i",
      notes="'Unexpected monophthongization' (p. 93); *-ay otherwise stays (*qazay > achay, *m-atay > matay, "
            "*talisay > talisay). Blust doubts that *pajey explains it, since *m-atey stays matay.")
    C("y", "i", 93, env="a+_", st="sporadic", n=1, ex="*pajay > fa'i", ap="*-ay > -i")
    C("a", "u", 93, env="_+w", st="sporadic", n=1, ex="*lakaw > lahu", ap="*-aw > -u",
      notes="'Unexpected monophthongization' (p. 93); *-aw otherwise stays (*paRaw > a-fagaw, *tiqaw > ti'aw).")
    C("w", "u", 93, env="a+_", st="sporadic", n=1, ex="*lakaw > lahu", ap="*-aw > -u")
    C("u", "i", 94, env="_+y", st="sporadic", n=1, ex="*hapuy > guafi", sf="i", ap="*-uy > -i",
      notes="'*-uy is reflected once as -i and once as -u' (p. 94). Printed guafi on p. 94, gwafi on pp. 96-97.")
    C("y", "i", 94, env="u+_", st="sporadic", n=1, ex="*hapuy > guafi", ap="*-uy > -i")
    C("y", "∅", 94, env="u_#", st="sporadic", n=1, ex="*naŋuy > nangu", ap="*-uy > -u")
    C("i", "u", 94, env="_+w", n=1, ex="*pa-laRiw > fa-lagu", ap="*-iw > u",
      notes="'*-iw is reflected as u in the only diagnostic example' (p. 94). *kahiw > hayu resyllabified instead.")
    C("w", "u", 94, env="i+_", n=1, ex="*pa-laRiw > fa-lagu", ap="*-iw > u")

    # ---- consonants (§3.3, pp. 94-97)
    C("p", "f", 94, ex="*pasu > fasu; *pitu > fitu; *peReq > fugo'; *qapuR > afok; *qatep > atof",
      notes="'*p lenited to f in all positions' (p. 94).")
    C("t", "t", 94, ex="*tau > tawtaw; *telu > tulu; *mata > mata; *laŋit > langet")
    C("c", "s", 94, system="Blust", n=1, ex="*ceŋceŋ > songsong", notes="'Only known reflex of *c' (p. 94).")
    C("k", "h", 94, ex="*kima > hima; *kutu > hutu; *zakan > chahan; *paniki > fanihi; *teken > tohn-e",
      notes="'In nonfinal position, *k lenited to h' (p. 94).")
    KF = ("'The split of *k in final position is particularly puzzling, because etyma of identical phonemic shape have "
          "taken different paths'; zero predominates, 9:6 (p. 101).")
    C("k", "∅", 94, env="_#", n=9, tot=15, notes=KF, sf="Ø",
      ex="*Rebek > gupu; *ma-esak > masa; *nabek > napu; *ñamuk > ñamu; *bakbak > pappa; *tasik > tasi")
    C("k", "k", 94, env="_#", n=6, tot=15, notes=KF, dec="cha-k",
      ex="*apak > gwafak; *lubuk > lupok; *manuk > mannok; *ŋekŋek > ŋokŋok; *bakbak > pakpak; *tuktuk > toktok")
    C("q", "∅", 94, env="#_", sf="Ø", ex="*qalep > alof; *qipil > ifet; *quzan > uchan",
      notes="'*q became the glottal stop except in initial position, where it disappeared' (p. 94). Words with *q- "
            "never take the secondary gw- (p. 99).")
    C("q", "ʔ", 94, sf="'", ex="*daqani > ha'ani; *tuqelaŋ > to'lang; *ma-qasiq > ma-'ase'; *Rumaq > guma'; *daReq > hago'")
    C("b", "p", 95, ex="*baRu > pagu; *beRas > pugas; *qabu > apu; *zebzeb > chopchop; *niRab > nigap; *teRab > tugap",
      notes="Final *b is p, not f: the shift *b > p followed *p > f, and final devoicing is recent (p. 95).")
    C("d", "h", 95, ex="*daRaq > haga'; *danum > hanom; *duha > hugwa; *ma-tuduR > ma-tuhok; *sida > siha; *qudaŋ > uhang",
      notes="'PMP *d merged with *k as h in nonfinal position' (p. 94).")
    C("d", "∅", 95, env="_#", n=1, sf="Ø", ex="*lahud > lagu",
      notes="Zero word-finally, 'presumably through an intermediate stage in which it first lenited to *r' (p. 94).")
    C("z", "t͡s", 95, sf="ch", ex="*zalan > chalan; *zuRuq > chugo'; *qazay > achai; *quzan > uchan",
      notes="*z did not occur syllable-finally. *qazay is printed with achai here (p. 95) and achay on p. 93. Irregular: "
            "*tazem > tasm-e, with s (p. 101).")
    C("j", "ʔ", 95, sf="'", ex="*pajay > fa'i; *pija > fi'a; *ijuŋ > gwi'eng; *dalij > hale'; *lalej > lalo'; *tubuj > tupo'",
      notes="'*j fell together with *q' (p. 94); *j did not occur syllable-initially.")
    C("j", "d", 101, st="sporadic", n=1, ex="*qalejaw > atdaw",
      notes="'May be due to conditioned change following the loss of medial schwa, but without further examples, this "
            "can only be speculation' (p. 101).")
    C("g", "ɡ", 95, sf="g", ex="*ganas > ganas; *guŋguŋ > gonggong; *getus > gutos",
      notes="*ganas may be a loan of Spanish gana (n. 10).")
    C("g", "k", 95, env="next to a voiceless stop", n=1, ex="*ma-getus > ma-ktos",
      notes="'Next to a voiceless stop *g devoiced' (p. 95), after syncope.")
    C("m", "m", 95, ex="*mamis > mames; *muRmuR > mokmok; *lima > lima; *dalem > halom; *danum > hanom")
    C("n", "n", 95, ex="*niuR > niyok; *nepuq > nufo'; *paniki > fanihi; *bunut > punot; *nipen > nifen",
      notes="nangu 'to swim' and nufo' 'scorpion fish' have doublets with initial ñ (p. 102).")
    C("ñ", "ɲ", 96, sf="ñ", ex="*ñamñam > ñamñam; *ñamuk > ñamu; *laña > laña; *leñej > luño'",
      notes="*ñ did not occur syllable-finally.")
    C("ŋ", "ŋ", 96, sf="ng", ex="*ŋaqŋaq > nga'nga'; *deŋeR > hungok; *ma-liŋu > ma-lingu; *tuqelaŋ > to'lang; *quRuŋ > ugong")
    C("ŋ", "n", 102, st="sporadic", n=1, ex="*ŋajan > na'an",
      notes="'Possibly the result of an assimilation to the nasal of the final syllable' (p. 102).")
    C("s", "s", 96, ex="*sakaRu > sahagu; *siqsiq > se'se'; *pasu > fasu; *susu > susu; *nusnus > nosnos")
    C("s", "h", 102, st="sporadic", n=1, ex="*sai > hayi",
      notes="Blust suggests convergence with *apa > h-afa 'what?' (p. 102).")
    C("h", "∅", 96, sf="Ø", ex="*hapuy > gwafi; *hasaq > gwasa'; *dahun > hagon; *daqih > ha'i; *talih > tali",
      notes="Where *h was lost before a vowel, a glide formed and was strengthened (p. 96; see the inserted gw, g, y). "
            "Between like vowels the vowels contracted: *aRuhu > gagu (p. 96).")
    C("l", "l", 96, ex="*lasuq > laso'; *lima > lima; *lesuŋ > lusong; *qalu > alu; *bulu > pulu",
      notes="Syllable-initial (p. 96). 'The reflexes *l > l and *l > t appear to be exceptionless' (p. 102).")
    C("l", "t", 96, env="_C, _#", ex="*qalejaw > atdaw; *saleR-i > satg-e; *kawil > hagwet; *qipil > ifet; *selsel > sotsot",
      notes="Syllable-final. Blust takes it through *d, then final devoicing (pp. 96-97); Spanish syllable-final l "
            "and r are borrowed as t.")
    C("r", "", 96, blank="not-attested", notes="'Chamorro has no known reflexes of *r' (p. 96).")
    C("R", "ɡ", 96, sf="g", ex="*Ratus > gatos; *Runut > gunot; *qabaRa > apaga; *zuRuq > chugo'; *biRaq > piga'",
      notes="Syllable-initial (p. 96).")
    C("R", "k", 96, env="_C, _#", ex="*peRes > foks-e; *ma-qaRsem > ma-'aksom; *beRsay > poksay; *layaR > layak; *ma-tuduR > ma-tuhok",
      notes="Syllable-final, by final devoicing of g (p. 96). 'One known exception': *beRŋi > pwengi, probably a loan "
            "from an Oceanic language (p. 102).")
    GF = "'Both glides were strengthened to obstruents in Chamorro, *w becoming the labiovelar stop gw' (p. 97)."
    C("w", "ɡʷ", 97, env="#_, V_V", sf="gw", notes=GF,
      ex="*wada > gwaha; *walu > gwalu; *watu > gwatu; *qawa > agwa; *qasawa > asagwa; *kawil > hagwet; *siwa > sigwa")
    C("w", "ɡ", 97, env="_u", sf="g", notes="'Before a rounded vowel, the strengthened reflex of *w is g, not gw' (p. 97); "
                                             "Blust's examples are of the inserted glide (*zauq > chago').")
    C("w", "w", 93, env="_#", ex="*paRaw > a-fagaw; *qalejaw > atdaw; *tiqaw > ti'aw",
      notes="Final *-aw 'remained unchanged' (p. 93), in Blust's respelling of Topping's -ao.")
    C("y", "d͡z", 97, sf="y", dec="cha-y", ex="*qayuyu > ayuyu; *daya > haya; *layaR > layak; *qazay > achay",
      notes="'*y the alveolar affricate y [dz]' (p. 97); final -ay 'remained unchanged' (p. 93), as y in Blust's "
            "respelling of Topping's -ai, which Blust takes as the [j] allophone of the same phoneme (p. 85).")

    # ---- glide formation and fortition (pp. 97-98)
    TG = ("Glide fortition 'affected not only phonemic *w and *y, but also the predictable transitional glides that "
          "developed in the environments *ua, *au, *ia' (p. 97), including those that arose after the loss of *h.")
    C("∅", "ɡʷ", 97, env="u_a", sf="gw", n=3, notes=TG, ex="*buaq > pugwa'; *duha > hugwa; *bahu-an > pagwan")
    C("∅", "ɡ", 97, env="a_u", sf="g", n=4, notes=TG + " Before a rounded vowel the reflex is g.",
      ex="*zauq > chago'; *dahun > hagon; *kahu > hagu; *lahud > lagu")
    C("∅", "d͡z", 97, env="i_V", sf="y", n=6, notes=TG,
      ex="*ia > gwiya; *kamiu > hamyo; *liaŋ > liyang; *niuR > niyok; *baRiuh > pakyo; *tian > tuyan")
    WI = ("'gw or g appears in initial position in words that originally began with a vowel, or with *h, which was "
          "first lost' (p. 97), in two steps: addition of *w, then fortition (p. 98). Not in words with *q- (p. 99). "
          "afa'fa' 'armpit' lacks it, perhaps because the first vowel was unstressed (p. 102).")
    C("∅", "ɡʷ", 97, env="#_a, #_i", sf="gw", n=11, notes=WI,
      ex="*apak > gwafak; *aku > gwahu; *ijuŋ > gwi'eng; *ini > gwini; *hapuy > gwafi; *hasaŋ > gwasang; *hikan > gwihan")
    C("∅", "ɡ", 97, env="#_u", sf="g", n=4, notes=WI + " Before a rounded vowel (including *e, which became u) the "
                                                      "reflex is g.",
      ex="*uRat > gugat; *enem > gunum; *huqenap > go'naf; *hunus > gunos")
