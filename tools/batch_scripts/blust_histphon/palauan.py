"""Palauan from PMP: Blust (2009), Table 2 (p. 309) with the conditions of §2.1.

Forms are in Blust's phonemicization (y = [j]); the orthography of McManus & Josephs
(1977) is in parentheses where Blust gives it.
"""
L = "pala1344"
S = "blust2009"


def build(B):
    B.add("lects", id=L, name="Palauan", alt_names="Belauan", type="language", glottocode="pala1344",
          iso639_3="pau", parent_id="pmp",
          notes="Palau. With Chamorro one of the two non-Oceanic Austronesian languages of the Pacific (Blust 2000: 83); "
                "Blust (2009) states its reflexes against PMP (Table 2, p. 309) and gives it no closer relatives. "
                "Glottocode from Glottolog 5.4.",
          orthography_note="Blust's phonemicization (2009: 308): y and w are glides, written i/e and u/o in the standard "
                           "orthography; ð is written d, ʔ ch, ŋ ng.")

    # ---- inventory: Table 1 (p. 308), 'slightly modified from that in Josephs (1975)'
    for ipa, cls, sym, kw in [("t", "C", "", {}), ("k", "C", "", {}), ("ʔ", "C", "ʔ", {}), ("b", "C", "", {}),
                              ("s", "C", "", {}), ("h", "C", "", {"status": "marginal",
                                                                   "notes": "In parentheses: a loan phoneme (p. 308)."}),
                              ("ð", "C", "", {}), ("m", "C", "", {}), ("ŋ", "C", "", {}), ("l", "C", "", {}),
                              ("r", "C", "", {}), ("w", "C", "", {}),
                              ("j", "C", "y", {"notes": "Blust follows Dyen's suggestion in adding the glides w and y; "
                                                        "written as vowels in the standard orthography (p. 308, n. 2)."}),
                              ("i", "V", "", {}), ("u", "V", "", {}), ("e", "V", "", {}), ("ə", "V", "", {}),
                              ("o", "V", "", {}), ("a", "V", "", {})]:
        B.P(L, ipa, cls, S, "308", sym=sym, notes=kw.get("notes", "Table 1 (p. 308)."), status=kw.get("status", ""))

    def C(par, ch, page, env="elsewhere", **kw):
        kw.setdefault("loc", "Table 2" if page == 309 else "")
        B.C(L, par, ch, env, src=S, page=page, **kw)

    # ---- vowels (§2.1.1, pp. 310-312)
    UN = ("'All unstressed vowels normally weakened to schwa, which deleted in absolute word-final position and in some "
          "nonfinal environments' (p. 310). Pre-Palauan stress was penultimate and shifted rightward under suffixation, "
          "so the vowel often reappears in suffixed forms (*mata > mað, *mata-ña > məða-l).")
    for v, ex_s in [("i", "*kima > kim"), ("u", "*susu > tut"), ("a", "*batu > bað")]:
        C(v, v, 310, env="stressed syllable", ex=ex_s, ap=f"*{v} > {v}/ə",
          notes="'These vowels remained unchanged under primary stress' (p. 310).")
        C(v, "ə", 310, env="unstressed syllable", ap=f"*{v} > {v}/ə", notes=UN,
          ex={"i": "*tiŋadaq > ðəŋarəʔ (dengárech); *kanasay > kəlat",
              "u": "*Ruqanay > səʔal (sechál); *qutan > ʔuðəl (chúdel)",
              "a": "*daRaq > rasəʔ (rásech); *mata-ña > məða-l"}[v])
        C(v, "∅", 310, env="_#", notes=UN, sf="Ø",
          ex={"i": "*puki > wuk (uúk)", "u": "*susu > tut; *qabu > ʔab (chab)", "a": "*mata > mað; *batu > bað"}[v])
    E = ("'Penultimate schwas in pre-Palauan apparently carried primary stress, and these are reflected unpredictably as "
         "o or e' (p. 311).")
    C("e", "o", 311, env="stressed syllable", n=4, notes=E, ap="*e ([ə]) > e/o/ə",
      ex="*enem > -loləm; *teRas > ðort; *qalejaw > ʔyos (cheós); *lebaq > yobəʔ (ióbech)")
    C("e", "e", 311, env="stressed syllable", n=12, notes=E, ap="*e ([ə]) > e/o/ə",
      ex="*baqeRu > bəʔes (bechés); *qeti > ʔeð (ched); *tebuh > ðeb; *teken > ðekəl; *deŋeR > or-reŋəs; *peñu > wel (uél)")
    C("e", "ə", 311, env="unstressed syllable", ap="*e ([ə]) > e/o/ə", notes=UN)
    C("e", "o", 312, env="unstressed syllable", st="sporadic", n=3,
      ex="*paen > wáol (uáol); *taeb > ðáob (dáob); *saet > táoð",
      notes="'In three plausible etymologies, an unstressed schwa is reflected as /o/' (p. 312); the first may be an "
            "early loan, the second a chance resemblance.")
    C("e", "∅", 312, env="#_", n=2, sf="Ø", ex="*esa > -ta-ŋ; *epat > -wa-ŋ",
      notes="'PMP initial *e apparently disappeared, although the evidence for this is limited' (p. 312).")
    C("∅", "o", 312, env="C_C", ap="-CC- > CoC", n=4,
      ex="*beRsay > bəsos; *saRman > ðəsoməl; *paŋdan > oŋór; *bejbej > bəsebəs",
      notes="'A penultimate schwa was added in pre-Palauan to break up a medial consonant cluster, and then carried the "
            "primary stress' (p. 312), becoming o or e like inherited stressed schwa.")
    DIPH = ("'PMP *-ay, *-aw, and *-uy evidently monophthongized to *-e, *-o, and *-i before the loss of unstressed final "
            "vowels, since they invariably disappeared' (p. 312). *tiqaw > ðeʔ (expected **ðiʔ) and *may > me 'and' "
            "keep the vowel.")
    for v, g, ex in [("a", "y", "*qatay > ʔað (chad); *qumay > ʔum (chum); *titay > ðið; *m-atay > mað; *anay > ŋal"),
                     ("a", "w", "*babaw > bab; *balabaw > byab (beáb); *kaRaw > kas"),
                     ("u", "y", "*hapuy > ŋaw")]:
        C(v, "∅", 312, env=f"_{g}#", ap=f"*-{v}{g} > Ø", notes=DIPH, ex=ex, sf="Ø")
        C(g, "∅", 312, env=f"{v}_#", ap=f"*-{v}{g} > Ø", notes=DIPH, ex=ex, sf="Ø")

    # ---- consonants (§2.1.2, pp. 313-323)
    C("p", "w", 313, ap="*p > w", sf="w (u/o)",
      ex="*pusej > wuðəs (uúdes); *puki > wuk (uúk); *qapuR > ʔaws (cháus); *kapet > kawð (káud)",
      notes="'Nonfinally, PMP *p preceding any vowel other than *a became a Palauan labiovelar glide' (p. 313).")
    PO = ("'The initial sequence *pa- and the final sequences *-ap and *-ep became o, presumably through *wa- and *-aw "
          "respectively' (p. 313); also *-pa in *depa > réo. *pa- became wa- if stressed (*paen > wáol).")
    C("p", "o", 313, env="_+a", notes=PO, ex="*paniki > olík; *pa-susu > ol-tut ~ o-tut")
    C("a", "o", 313, env="p+_", notes=PO, ex="*paniki > olík; *pa-susu > ol-tut ~ o-tut")
    C("p", "o", 313, env="a+_", notes=PO, ex="*qatep > ʔaðo (chádo); *kaRakap > kəsako; *dapdap > róro")
    C("a", "o", 313, env="_+p", notes=PO, ex="*kaRakap > kəsako; *dapdap > róro")
    C("p", "o", 313, env="e+_", notes=PO, ex="*qatep > ʔaðo (chádo)")
    C("e", "o", 313, env="_+p", notes=PO, ex="*qatep > ʔaðo (chádo)")
    C("t", "ð", 314, sf="ð (d)", ex="*taqi > ðaʔ; *tinaqi > ðəlaʔ (delách); *batu > bað; *laŋit > yaŋð (eánged)",
      notes="'Except when it came to be adjacent to another stop, PMP *t became the voiced interdental fricative ð' "
            "(p. 314).")
    C("t", "t", 314, env="#b_, C_#", n=5, ex="*bitaquR > btaʔəs (btáches); *bituqen > btuʔ (btuch); *takut > ðakt; *sakit > rakt",
      notes="'Immediately following initial b, or following a voiceless stop in final position *t did not change' "
            "(p. 314), after the loss of unstressed vowels.")
    C("c", "", 314, blank="not-attested", system="Blust",
      notes="'No plausible etymologies that contain PMP *c have been found in Palauan' (p. 314).")
    C("k", "k", 315, ex="*kutu > kuð; *kuku > kuk; *hikan > ŋikəl; *manuk > malk; *anak > ŋalək",
      notes="'*k is the only voiceless obstruent that did not change' (p. 315).")
    C("q", "ʔ", 315, sf="ʔ (ch)", ex="*qabu > ʔab (chab); *qasu > ʔat (chat); *bituqen > btuʔ (btuch); *nanaq > laləʔ (lálech)",
      notes="'*q became a glottal stop in all positions' (p. 315), except word-initially after the prefix məŋ- "
            "(*maŋ-ququs > məŋuʔət, p. 316). Palauan keeps the PAN contrast of *V- and *qV-.")
    C("b", "b", 316, ex="*balay > bay (bái); *bubu > bub; *qabu > ʔab (chab); *niRab > e-lisəb",
      notes="'*b is the only voiced obstruent that did not change' (p. 316).")
    C("d", "r", 316, ex="*daqan > raʔəl (ráchel); *danum > ralm; *duha > -ru-ŋ; *tuduR > ðurs; *sida > tir")
    C("z", "r", 317, ex="*zalan > rayl (ráel); *zaRum > rasm; *tazem > kə-ðorəm",
      notes="PMP *z did not occur word-finally (p. 317).")
    C("z", "l", 317, env="_n", n=1, ex="*quzan > *ʔurl > ʔull (chull)",
      notes="'The derived cluster rl assimilated to ll' (p. 317), after *n > l and loss of the vowel.")
    C("j", "s", 317, ex="*qajeŋ > ʔas (chas); *qalejaw > ʔyos (cheós); *laji > las; *lalej > yays (iáes); *dalij > rays (ráis)",
      notes="'*j was probably a palatalized voiced velar stop (*gy) that did not occur word-initially. In Palauan it "
            "normally became s' (p. 317).")
    C("j", "k", 317, env="_C#", n=1, ex="*ŋajan > ŋakl", notes="'Before a final consonant, *j became k' (p. 317).")
    C("j", "l", 317, env="_#", st="sporadic", n=1, ex="*bukij > bukl",
      notes="'In a single known case, final *j is reflected as l' (p. 317).")
    C("g", "", 317, blank="not-attested", notes="'No clear etymologies that contain PMP *g have been identified' (p. 317).")
    C("D", "r", 317, env="_#", system="Blust", n=1, ex="*hateD > ŋ-adər",
      notes="'A single etymology is available for PMP *-D, and its reflex is the same as that for *d' (p. 317).")
    C("m", "m", 317, ex="*mata > mað; *qumay > ʔum (chum); *lamun > yaml (iáml); *danum > ralm",
      notes="'*m has been extremely stable in Palauan' (p. 317).")
    C("n", "l", 318, ex="*nanaq > laləʔ (lálech); *niuR > líus; *anak > ŋalək; *bulan > buyl (búil); *quzan > ʔull (chúll)",
      notes="'Since no other phoneme became n, Palauan has a rare set of nasals consisting only of m and ŋ' (p. 318).")
    C("n", "ŋ", 318, env="_#", st="sporadic", n=4, ex="*bituqen-ña > bətəʔəŋ-el; *ma-ŋaen > məŋaŋ; *paŋdan > oŋór; *pa-kaen > okáŋ",
      notes="'In four plausible etymologies, morpheme-final *n is reflected as a velar nasal' (p. 318).")
    C("ñ", "l", 318, n=3, ex="*-ni-a > *-ña > -el; *peñu > wel (uél); *leñeb > yeləb (iéleb)",
      notes="'What evidence we have suggests that it merged with *n as l' (pp. 318-319). *ñ did not occur "
            "syllable-finally.")
    C("ñ", "ŋ", 319, st="sporadic", n=2, ex="*ñeñu > ŋel; *(nñ)ituq > ŋíðəʔ (ngídech)",
      notes="'Two comparisons suggest contrarily that *ñ became Palauan ŋ' (p. 319).")
    C("ŋ", "ŋ", 319, ex="*ŋajan > ŋakl; *ŋesuŋ > ŋot; *buŋa > buŋ; *teŋeR > ðəŋəs", notes="'In nonfinal position, *ŋ did not change' (p. 319).")
    C("ŋ", "∅", 319, env="_#", sf="Ø", ex="*bituqen > btuʔ (btuch); *qajeŋ > ʔas (chas); *liaŋ > yiy (íi); *ŋesuŋ > ŋot",
      notes="Word-final *ŋ, after the loss of the unstressed vowel before it, 'regularly disappeared through cluster "
            "reduction' (p. 319); it returns in suffixed forms (*liaŋ-ña > yəŋél).")
    C("s", "t", 319, ex="*sida > tir; *siwa > -tiw; *qasu > ʔat (chat); *susu > tut; *tales > ðayt (dáit)",
      notes="'PMP *s normally became Palauan t' (p. 319).")
    DIS = ("'In pre-Palauan, the sequences *tV(C)s and *sV(C)t were avoided by exploiting several strategies' (p. 320): "
           "*s became ð, or remained s.")
    C("s", "s", 320, env="where t would give *sV(C)t or *tV(C)s", n=3, notes=DIS,
      ex="*beRsay > bəsos; *sinaR > sils; *siRi > sis")
    C("s", "ð", 320, env="where t would give *sV(C)t or *tV(C)s", n=2, notes=DIS, ex="*pusej > wuðəs; *saRman > ðəsoməl")
    C("s", "r", 320, st="sporadic", n=1, ex="*sakit > rakt", notes="Irregular; 'more puzzling' (p. 320).")
    C("h", "∅", 320, sf="Ø", ex="*bahu > baw (báu); *kahu > kaw (káu); *duha > ru-ŋ; *baRah > bas; *talih > ðay",
      notes="'PMP *h disappeared' (p. 320), before the addition of initial ŋ- (p. 323).")
    C("l", "j", 321, sf="y (i/e)", ex="*laji > yas (iás); *liaŋ > yiy (íi); *buliq > buyʔ (búich); *qalu > ʔay (chái); *telu > -ðey",
      notes="'PMP *l became Palauan y (written i or e in the standard orthography)' (p. 321). No examples of final *l.")
    C("l", "l", 321, st="sporadic", n=1, ex="*lulun > mə-luyl (melúil)")
    C("l", "r", 321, st="sporadic", n=2, ex="*bulaka > burak; *saku layaR > təkrar",
      notes="'These may be early loanwords from a still unidentified Nuclear Micronesian source' (p. 321).")
    C("l", "∅", 322, st="sporadic", n=1, ex="*lima > -im", notes="'This change probably is due to reanalysis' (p. 322).")
    C("r", "r", 322, n=1, ex="*remes > mə-remət", notes="'A single plausible etymology exemplifying PMP *r has been found' (p. 322).")
    C("R", "s", 322, ex="*Rebek > s<u>ebək; *Runut > sulð; *baRah > bas; *naRa > las; *tuduR > ðurs; *deŋeR > or-reŋəs",
      notes="'PMP *R (probably an alveolar trill) normally became Palauan s' (p. 322).")
    C("R", "r", 322, env="_[t,s]", ex="*Ratus > ðart; *teRas > ðort; *ma-ŋaRat > məŋarð; *uRat > ŋurð",
      notes="'Immediately preceding a dental consonant, *R became r' (p. 322): the following *t, or *s, which became t.")
    C("R", "∅", 323, st="sporadic", n=2, ex="*um-aRi > mei; *qaRta > ʔað (chad)",
      notes="'Two otherwise excellent etymologies show *R > Ø' (p. 323); Blust suspects *mai and *qata as variants.")
    C("w", "w", 322, sf="w (u/o)", ex="*waqay > waʔ (oách); *kanawa > kəlaw (keláu); *sawaq > tawʔ (táoch); *siwa > e-tiw")
    C("w", "∅", 322, st="sporadic", n=2, ex="*walu > e-ay; *wada > *ada > ŋar")
    C("y", "r", 322, ex="*qayam > ʔarm (charm); *layaR > yars (eárs); *kahiw > kərrəkar",
      notes="'PMP *y did not occur word-initially, and in final position occurred only as a diphthongal coda' "
            "(p. 322). Medially it is r.")
    C("∅", "ŋ", 323, env="#_V", ap="Ø- > ŋ", loc="Table 3",
      ex="*aku > ŋak; *anak > ŋalək; *aRuhu > ŋas; *hapuy > ŋaw; *ia > ŋiy; *hikan > ŋíkəl; *uRat > ŋurð",
      notes="'The accretion of a velar nasal before bases that originally began with a vowel or *h- (which disappeared "
            "very early)' (p. 323); Table 3 lists the forms (p. 324). Blust argues for a sound change, not "
            "metanalysis of an article (pp. 323-328).")
