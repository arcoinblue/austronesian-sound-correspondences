"""Òma Lóngh from Proto-Kenyah: Blust (2007: 8-34), read from the page images.

Soriente's practical orthography (Blust 2007: 8-9; Table 4, p. 11), with Blust's ʔ for ':
é [e], è [ɛ], ó [o], ò [ɔ], e [ə] or [ɯ] (from *u), c [c], j [ɟ] (final unreleased [c]),
f [ɸ], v [β], gh [ɣ], ng [ŋ], ngh [ŋ̊], ny [ɲ]. Forms are copied as printed.
"""
L = "umal1238"
S = "blust2007"


def build(B):
    B.add("lects", id=L, name="Òma Lóngh", alt_names="Uma' Lung;OL;Oma Longh", type="language", glottocode="umal1238",
          iso639_3="ulu", parent_id="pk",
          notes="Upper Malinau and upper Pujungan rivers, East Kalimantan; about 3,000 speakers, long isolated from other "
                "Kenyah (Blust 2007: 8). A Highland Kenyah language (p. 10); Blust derives it from Proto-Kenyah. Data "
                "from Soriente (2006). Glottolog 5.4: Uma' Lung, under Highland Kenyah (Upper Pujungan).",
          orthography_note="Soriente's spelling (Blust 2007: 8-9): é è ó ò are tense and lax mid vowels, e is both [ə] "
                           "and [ɯ] (from *u), j is [ɟ] (unreleased [c] finally), f [ɸ], v [β], gh [ɣ], ngh a voiceless "
                           "velar nasal. Blust writes ʔ for Soriente's apostrophe.")

    # ---- inventory: Blust (2007: 8-9) and Table 4 (p. 11), after Soriente (2006)
    def P(ipa, cls, sym="", page="8-9", **kw):
        B.P(L, ipa, cls, "soriente2006", "", sym=sym or ipa, via=S, viap=page, **kw)

    P("b", "C"); P("c", "C", notes="Voiceless palatal stop.")
    P("d", "C", place="dental", notes="Voiced dental stop, 'varying freely with r medially, and occasionally initially'.")
    P("ɸ", "C", "f"); P("ɡ", "C", "g"); P("ɣ", "C", "gh", notes="Voiced velar fricative, 'varying freely with k initially'.")
    P("ɟ", "C", "j", notes="'Voiced palatal stop initially and medially; unreleased voiceless palatal stop finally'.")
    P("k", "C"); P("ʔ", "C", "ʔ", notes="Soriente's apostrophe; Blust writes ʔ.")
    P("l", "C"); P("m", "C"); P("n", "C", place="dental", notes="Voiced dental nasal.")
    P("ŋ", "C", "ng"); P("ŋ̊", "C", "ngh", place="velar", manner="nasal", voicing="voiceless", notes="Voiceless velar nasal.")
    P("ɲ", "C", "ny"); P("p", "C"); P("r", "C", notes="Apical trill, 'varying freely with d word-medially'.")
    P("s", "C"); P("t", "C", place="dental", notes="Voiceless dental stop.")
    P("β", "C", "v"); P("z", "C")
    for ipa, sym, n in [("i", "i", ""), ("e", "é", "Tense mid front."), ("ɛ", "è", "Lax mid front."),
                        ("ɯ", "e", "Written e, like schwa: [ɯ] where e corresponds to *u (Soriente, pers. comm., p. 11)."),
                        ("ə", "e", "Written e, like [ɯ]."), ("u", "u", ""), ("o", "ó", "Tense mid back."),
                        ("ɔ", "ò", "Lax mid back."), ("a", "a", "")]:
        P(ipa, "V", sym, page="11", notes=("Table 4 (p. 11). " + n).strip())

    def C(par, ch, page, env="elsewhere", **kw):
        B.C(L, par, ch, env, src=S, page=page, **kw)

    # ---- last-syllable vowels (§4.2.1.1-4.2.1.4, pp. 10-17; Table 5, p. 15)
    T5 = dict(loc="Table 5")
    C("i", "e", 10, env="_k#", sf="é", ap="*i > é /__k>ʔ#", ex="*bətik > betéʔ; *pəsik > feséʔ; *lidik > lédéʔ",
      notes="Before final *k, which became ʔ (p. 10).", **T5)
    C("∅", "ə", 10, env="i_ŋ#", sf="e", ap="*i > ie /__ŋ#", ex="*kadiŋ > kadiengh; *madiŋ > madiengh; *ndiŋ > se-ntiengh",
      notes="'*i developed a mid central offglide before final velar nasals' (p. 10), written ie.", **T5)
    C("i", "i", 10, env="final syllable", ap="*i > i /__e.w.", ex="*bəli > beli; *pəsi > fesi; *puti > futi; *anit > anij; *sadin > sadiny",
      notes="'The unmarked reflex of last-syllable *i' (p. 10).", **T5)
    C("u", "o", 12, env="_p#, _k#", sf="ó", ap="*u > ó /__p/k>ʔ#",
      ex="*baduk > badóʔ; *jamuk > jamóʔ; *layuk > lazóʔ; *anup > ng-anóʔ; *taup > taóʔ",
      notes="Before final *p or *k, which became ʔ (p. 12). Exceptions *kulup > kuluʔ, *kətuk > ngetuʔ.", **T5)
    C("u", "o", 12, env="_ŋ#", sf="ó", ap="*u > ó /__ŋ#", ex="*kaluŋ > kalóngh; *latuŋ > latóngh; *siluŋ > sélóngh",
      notes="'The same change generally took place before a final velar nasal' (p. 12), with at least six exceptions "
            "(*nduŋ > ntungh), and none in Malay loans.", **T5)
    C("u", "u", 13, env="_ʔ#", ap="*u > u /__ʔ#", ex="*baʔuʔ > baʔu; *buluʔ > bulu; *labuʔ > labu; *tujuʔ > tuju",
      notes="'In general *u remained unchanged if it was followed by PK *ʔ' (p. 13), which was then lost.", **T5)
    C("u", "ɯ", 13, env="final syllable", sf="e", ap="*u > e[ɯ] /__e.w.", ex="*abu > abe; *batu > bate; *kutu > kóte; *likut > lighek; *timun > timeng",
      notes="'The unmarked reflex of last-syllable *u' (p. 13): a high back unrounded vowel, written e. Blust knows no "
            "parallel in insular Southeast Asia (p. 15).", **T5)
    C("a", "ə", 13, env="_ʔ#", sf="e", ap="*a > e /__ʔ#",
      ex="*bayaʔ > bazeʔ; *budaʔ > bòdeʔ; *lataʔ > lateʔ; *ləkaʔ > lekeʔ; *tanaʔ > taneʔ",
      notes="'*a centralized to schwa before final glottal stop' (p. 13), where the glottal stop survives (see *ʔ).", **T5)
    C("a", "o", 13, env="_#", sf="ó", ap="*a > ó /__#", ex="*dua > devó/revó; *mata > mató; *ia > zó; *tuba > tóbó",
      notes="'Word-final *a often rounded to ó' (p. 13). Almost as many keep a; Blust orders the rounding before the "
            "loss of final ʔ, which explains some, not all (p. 14).", **T5)
    C("a", "ɛ", 14, env="_t#, _n#", sf="è", ap="*a > è /__t/n#",
      ex="*buat > bevèj; *kulat > kolèj; *kuyat > kòzèj; *bulan > bòlèny; *ujan > òjèny",
      notes="'Last-syllable *a fronted to è preceding a final dental consonant, which then palatalized' (p. 14). "
            "Exception *bahat > baat.", **T5)
    C("a", "a", 14, env="final syllable", ap="*a > a /__e.w.", ex="*anak > anaʔ; *pəsak > fesaʔ; *madam > madam; *iap > zaʔ",
      notes="'The default reflex found in the elsewhere environment' (p. 14).", **T5)
    DIPH = "'PK *ay became è, *aw became ò, and *uy and *iw became é in OL. There are no known exceptions' (p. 15)."
    for v, g, ch, sf, ex in [("a", "y", "ɛ", "è", "*asay > asè; *atay > atè; *paday > fadè; *taytay > tètè"),
                             ("a", "w", "ɔ", "ò", "*isaw > èsò; *ləpaw > lepò; *dʰaw > tò"),
                             ("u", "y", "e", "é", "*apuy > afé; *babuy > babé"),
                             ("i", "w", "e", "é", "*baliw > balé; *saliw > salé; *titiw > tété")]:
        C(v, ch, 15, env=f"_+{g}", sf=sf, ex=ex, notes=DIPH, ap=f"*{v}{g} > {sf}", **T5)
        C(g, ch, 15, env=f"{v}+_", sf=sf, ex=ex, ap=f"*{v}{g} > {sf}", **T5)
    C("ə", "ə", 15, sf="e", notes="'PK *ə, *-e, and *-o show no regular changes' (p. 15).")
    C("e", "e", 15, sf="é", notes="PK *-e shows no regular change (p. 15); it is OL tense é (p. 13).")
    C("o", "o", 15, sf="ó", notes="PK *-o shows no regular change (p. 15); it is OL tense ó (p. 13).")

    # ---- penult vowels (§4.2.1.5-4.2.1.8, pp. 17-25; Table 6, pp. 22-23)
    H = ("Harmonic lowering: 'penultimate *i regularly lowered to a tense mid vowel when there was a tense mid vowel in "
         "the final syllable', and to a lax one before a lax one (pp. 17-18); the same for *u (p. 18). Final ie counts "
         "as tense.")
    NH = ("Nonharmonic lowering (Table 6, pp. 22-23): before *ə or *a in a closed final syllable the penult lowers to a "
          "lax mid vowel, before *u in an open final syllable to a tense one; 48 of 55 forms follow this (p. 23).")
    GL = ("Penultimate *i and *u 'centralized to schwa when an intervening phonetic glide underwent fortition', and were "
          "lost word-initially (pp. 18-19).")
    for v, tense, lax, exs in [("i", "e", "ɛ", {"t": "*isiw > ésé; *nipe > nyéfé; *siluŋ > sélóngh; *tilo > téló",
                                                "l": "*inan > ènèny; *isaw > èsò; *kian > kèèny; *liway > lèvè",
                                                "g": "*biuʔ > bezu; *piat > fezèj; *lia > lezó; *sian > sezèny",
                                                "z": "*iap > zaʔ; *iu > ze; *iəŋ > zeng; *ia > zó",
                                                "k": "*iku > ighu; *inu > inu; *iti > iti; *liʔip > liʔij; *timun > timeng",
                                                "nl": "*ilaŋ > èlangh; *biləŋ > bèlengh; *litak > lètaʔ",
                                                "nt": "*ilu > éle"}),
                               ("u", "o", "ɔ", {"t": "*puke > fóghé; *juma > jómó; *muduŋ > módóngh; *tusuk > nósóʔ",
                                                "l": "*punay > fònè; *kujaw > kòjò; *kuyat > kòzèj; *ujan > òjèny",
                                                "g": "*buaʔ > (be)va; *buat > bevèj; *dua > devó/revó; *kuay > kevè",
                                                "z": "*uay > vè; *uiʔ > vi",
                                                "k": "*bulit > bulij; *pulut > fulek; *puti > futi; *tuju > tuju",
                                                "nl": "*buʔət > bòʔet; *pusət > bòset; *butaʔ > bòteʔ; *lubaŋ > lòbangh",
                                                "nt": "*bulu > bóle; *kutu > kóte; *putu > fóte"})]:
        st = {"i": ("é", "è"), "u": ("ó", "ò")}[v]
        C(v, tense, 17, env="penultimate syllable, before a tense mid vowel in the final syllable", sf=st[0],
          ex=exs["t"], notes=H, ap=f"*(C){v}- > {st[0]}")
        C(v, lax, 17, env="penultimate syllable, before a lax mid vowel in the final syllable", sf=st[1],
          ex=exs["l"], notes=H, ap=f"*(C){v}- > {st[1]}")
        C(v, lax, 22, env="penultimate syllable, before *ə or *a in a closed final syllable", sf=st[1], loc="Table 6",
          ex=exs["nl"], notes=NH, ap="LC")
        C(v, tense, 22, env="penultimate syllable, before *u in an open final syllable", sf=st[0], loc="Table 6",
          ex=exs["nt"], notes=NH, ap="TO")
        C(v, "ə", 18, env="C_V", sf="e", ex=exs["g"], notes=GL, ap=f"*{v} > e")
        C(v, "∅", 18, env="#_V", sf="Ø", ex=exs["z"], notes=GL, ap=f"*{v} > Ø")
        C(v, v, 18, env="penultimate syllable, before a high vowel in the final syllable", notes=f"Penultimate *{v} 'remained unchanged if there is a high vowel in the last syllable and the two "
                          f"vowels are separated by a consonant' (pp. 18-19).", ex=exs["k"])
    C("a", "a", 17, env="penultimate syllable",
      notes="'Of these four vowels neither *a nor *ə underwent any kind of recurrent change' in the penult (p. 17).")
    C("ə", "∅", 17, env="#_", sf="Ø", ex="*əpat > pèj; *ənəm > nem",
      notes="Schwa 'may have been lost in word-initial position' (p. 17); the evidence is slim (n. 8).", st="disputed")

    # ---- final consonants (§4.2.2.1, pp. 25-29)
    FIN = "Final consonants 'conditioned by the quality of the preceding vowel' (pp. 25-29)."
    C("p", "ʔ", 26, env="a_#, u_#", ap="*-ap > -aʔ; *-up > -óʔ", notes=FIN + " After *u through *-uk (p. 26).",
      ex="*jaʔap > jaʔaʔ; *kəlap > kelaʔ; *sap > saʔ; *iap > zaʔ; *anup > ng-anóʔ; *taup > taóʔ")
    C("p", "p", 26, env="ə_#", ap="*-əp > -ep", notes=FIN + " Exception *atay bəp > atè-vaʔ.",
      ex="*bətəp > betep; *ləp > lep; *m-əkəp > mekep; *isəp > n-èsep")
    C("p", "ɟ", 26, env="i_#", sf="j", ap="*-ip > -ij", notes=FIN, ex="*liʔip > liʔij; *m-udip > m-udij; *tisip > nisij")
    C("t", "ɟ", 26, env="a_#, i_#", sf="j", ap="*-at > -èj; *-it > -ij", notes=FIN + " After *a, which fronted to è (p. 14).",
      ex="*piat > fezèj; *taʔat > taʔèj; *tulat > tòlèj; *abit > abij; *bulit > bulij; *laŋit > langij")
    C("t", "t", 27, env="ə_#", ap="*-ət > -et", notes=FIN, ex="*abət > abet; *buʔət > bòʔet; *dəkət > deket; *ulət > òlet")
    C("t", "k", 27, env="u_#", ap="*-ut > -ek", notes=FIN + " 'Backed to a velar stop following *u (which then unrounded)'.",
      ex="*alut > alek; *pulut > fulek; *likut > lighek; *takut > taghek; *ubut > ubek")
    C("k", "ʔ", 27, env="_#", ap="*-k > ʔ", ex="*anak > anaʔ; *batək > bateʔ; *bətik > betéʔ; *baduk > badóʔ",
      notes="'PK *k is reflected as glottal stop in final position, regardless of the preceding vowel' (p. 27).")
    GS = ("'Following *a, the glottal stop shows an apparent unconditioned phonemic split, remaining in some forms and "
          "disappearing in others' (p. 27): a change in progress, which Blust believes began after high vowels (p. 28).")
    C("ʔ", "∅", 27, env="a_#", cond="unknown", n=18, sf="Ø", ap="*-aʔ > -a", notes=GS,
      ex="*alaʔ > ala; *bayaʔ > baza; *dahaʔ > daa/raa; *jəlaʔ > jela; *mataʔ > mata; *umaʔ > òma")
    C("ʔ", "ʔ", 27, env="a_#", n=21, ap="*-aʔ > -eʔ", notes=GS,
      ex="*bahaʔ > baaʔ; *basaʔ > baseʔ; *butaʔ > bòteʔ; *ləmaʔ > lemeʔ; *tanaʔ > taneʔ")
    C("ʔ", "∅", 28, env="i_#, u_#", sf="Ø", ap="*iʔ > -i; *uʔ > -u",
      ex="*akiʔ > aghi; *bəniʔ > beni; *putiʔ > futi; *buluʔ > bulu; *labuʔ > labu; *tujuʔ > tuju",
      notes="'After the high vowels it invariably disappeared' (p. 27).")
    C("m", "m", 28, env="a_#, ə_#", ap="*-am > -am; *-əm > -em", notes=FIN,
      ex="*madam > madam; *sanam > sanam; *aləm > alem; *dadəm > dadem; *ənəm > nem")
    C("m", "ɲ", 28, env="i_#", sf="ny", ap="*-im > -iny", notes=FIN, ex="*alim > aliny; *səŋim > senginy")
    C("m", "ŋ", 28, env="u_#", sf="ng", ap="*-um > -eng", notes=FIN + " One exception: *səlum > nyelem.",
      ex="*mimum > mimeng")
    C("n", "ɲ", 28, env="a_#, i_#", sf="ny", ap="*-an > -èny; *-in > -iny", notes=FIN,
      ex="*bəkan > bekèny; *uman > òmèny; *taban > tabèny; *buʔin > buʔiny; *sadin > sadiny")
    C("n", "n", 28, env="ə_#", ap="*-ən > -en", notes=FIN, ex="*bətuʔən > betòʔen; *kudən > kóden; *usən > òsen; *ipən > s-èfen")
    C("n", "ŋ", 28, env="u_#", sf="ng", ap="*-un > -eng", notes=FIN,
      ex="*abun > abeng; *aʔun > aʔeng; *puʔun > fuʔeng; *mutun > muteng; *tusun > tuseng")
    C("ŋ", "ŋ̊", 28, env="_#", sf="ngh", ap="*-ŋ > -ŋh",
      ex="*anaŋ > anangh; *bataŋ > batangh; *biləŋ > bèlengh; *kadiŋ > kadiengh; *kaluŋ > kalóngh",
      notes="'PK *ŋ in final position is regularly reflected as -ŋh regardless of the preceding vowel' (p. 28). Five "
            "exceptions with -ng are orthographic oversights (p. 29, n. 13).")

    # ---- nonfinal consonants (§4.2.2.2, pp. 29-34)
    C("p", "ɸ", 29, sf="f", ex="*pade > fadè; *paʔa > faʔa; *pəsak > fesaʔ; *apuy > afé; *kapan > kafèny; *upaʔ > òfa",
      notes="'Word-initially *p invariably became f. Intervocalically *p remained unchanged after a stressed schwa ... "
            "but otherwise became f' (p. 29). Exceptions *pusət > bòset, *pañən > panyen, *apit > pij.")
    C("p", "p", 29, env="ə_V (stressed ə)", ex="*ləpaʔ > lepeʔ; *ləpaw > lepò; *məpa > mepa; *təpap > tepaʔ",
      notes="After a stressed schwa, which geminates a following consonant phonetically (p. 29): *ləpuʔ > lepu but "
            "*ləpuʔ-ən > lefuʔeng.")
    PB = "'PK *bʰ had merged with *p prior to any of these changes' (p. 29); the Highland Kenyah p (p. 7)."
    C("bʰ", "p", 29, env="ə_V (stressed ə)", notes=PB, ap="*bʰ > *p",
      ex="*ləbʰuʔ (> *ləpuʔ) > lepu; *bəbʰaʔ (> *əpaʔ) > pa; *əbʰuk (> *əpuk) > póʔ; *təbʰu (> *təpu) > tepe")
    C("bʰ", "ɸ", 29, notes=PB + " Elsewhere, like *p.", ap="*bʰ > *p > f", deriv="composed")
    C("t", "t", 30, ex="*tapan > tafèny; *təlu > tele; *tudo > tódó; *atay > atè; *batu > bate",
      notes="'In nonfinal position PK *t did not change' (p. 30).")
    C("dʰ", "t", 30, ap="*dʰ > *t", ex="*təmədʰo (> *təməto) > temetó; *dʰaw > tò",
      notes="'PK *dʰ had already merged with *t prior to any of these changes' (p. 30).")
    C("k", "k", 30, env="#_, ə_V (stressed ə)",
      ex="*kaluŋ > kalóngh; *kutu > kóte; *bəkan > bekèny; *dəkət > deket; *səkut > sekek",
      notes="'In initial position k and gh are in free variation ... Intervocalically the voiceless velar stop occurs "
            "following a stressed schwa, and the voiced velar fricative in other positions' (p. 30).")
    C("k", "ɣ", 30, env="V_V", sf="gh", ex="*aka > agha; *dakit > daghij; *puke > fóghé; *lakət > laghet; *sakit > saghij",
      notes="Intervocalically except after a stressed schwa, also after an unstressed one (*pəkaləm > feghelem) (p. 30).")
    C("gʰ", "k", 30, ap="*gʰ > *k", ex="*məgʰən (> *məkən) > meken",
      notes="Merged with *k (p. 30); the Highland Kenyah k (p. 7).")
    C("jʰ", "c", 10, ex="*jʰa > có; *jʰan > cèny",
      notes="'Òma Lóngh is a Highland Kenyah language reflecting the PNS voiced aspirates as p t c k' (p. 10).")
    C("ʔ", "ʔ", 30, env="V_V", ex="*baʔuʔ > baʔu; *bətuʔən > betòʔen; *buʔin > buʔiny; *taʔi > taʔi",
      notes="'PK *-ʔ- remained unchanged' (p. 30), with five exceptions (*muʔat > mòèj).")
    C("b", "b", 30, ex="*baha > baa; *bulan > bòlèny; *abu > abe; *labi > labi; *tuba > tóbó",
      notes="'In nonfinal position PK *b is regularly reflected only as b' (p. 30). Exception *atay bəp > atè vaʔ.")
    C("d", "d", 31, env="V_V", ex="*badaʔ > bada; *baduk > badóʔ; *kaduʔ > kadu; *madiŋ > madiengh",
      notes="'An invariant d intervocalically' (p. 31).")
    C("d", "d", 31, env="#_", ex="*dakit > daghij; *dəŋən > dengen; *daʔun > daʔeng/raʔeng; *dadəm > dadem/radem",
      notes="'PK *d is reflected as d ~ r word-initially' (p. 31); some forms are recorded with d, some with r, some "
            "with both, probably from incomplete recording.")
    C("d", "r", 31, env="#_", ex="*daya > razó; *dipa > réfa; *dumit > rumit; *dua > devó/revó",
      notes="The r of initial d ~ r (p. 31). *dumit is printed rumit here and rumij on p. 26.")
    C("j", "ɟ", 31, sf="j", ex="*jaʔa > jaʔa; *jamuk > jamóʔ; *janan > janèny; *kəjaʔ > kejeʔ; *tajuŋ > tajóngh",
      notes="'PK nonfinal *j is regularly reflected as j' (p. 31). Exception *juʔ > ce.")
    C("g", "ɡ", 31, sf="g", n=4, ex="*tugan > nògèny; *ñaga > nyagó; *ugay > ògè; *pəguʔ > fegu",
      notes="'Only four examples of *-g- > g are available' (p. 31): *k lenited to gh but *g did not.")
    NC = "'In OL all stops devoiced after a nasal consonant. In a small number of forms the nasal then disappeared' (p. 32)."
    C("b", "p", 32, env="m_", ex="*kələmbit > kelempij; *ləmbuʔ > lempe; *mbaʔ > mpeʔ", notes=NC)
    C("d", "t", 32, env="n_", ex="*kəndaʔ > kenta; *ndaŋ > ntangh; *nduŋ > ntungh; *səndəŋ > sentengh",
      notes=NC + " Exception *pəlanduk > felanóʔ.")
    C("j", "c", 32, env="n_", ex="*lənjaw > lencò; *njam > ncam; *ŋənja > ngencó", notes=NC)
    C("g", "k", 32, env="ŋ_", ex="*ŋgaŋ > ngkangh; *ŋgin > ngkiny; *təŋgan > tengkèny", notes=NC)
    for nas, stop, ex in [("m", "b", "*kumbin > upiny"), ("n", "d", "*lunduʔ > lutu"), ("n", "j", "*kanjaw > kacò"),
                          ("ŋ", "g", "*saŋgit > sakij")]:
        C(nas, "∅", 32, env=f"_{stop}", st="sporadic", sf="Ø", ex=ex, notes=NC)
    C("m", "m", 32, ex="*mata > mató; *mipa > mèfa; *ama-i > amè; *pamən > famen; *umaʔ > òma",
      notes="'PK nonfinal *m is invariably reflected as m' (p. 32).")
    C("n", "n", 33, ex="*nakaw > naghò; *nawa > nava; *anak > anaʔ; *bəniʔ > beni; *tunu > tóne",
      notes="'PK nonfinal *n is regularly reflected as n' (p. 33). Exception *nipe > nyéfé.")
    C("ñ", "ɲ", 33, sf="ny", ex="*ñatəŋ > nyatengh; *ñatuŋ > nyatóngh; *ñaʔap > nyéaʔ; *laña > lanyó",
      notes="'PK *ñ was found only in syllable-initial position, and ... invariably remained a palatal nasal' (p. 33).")
    C("ŋ", "ŋ", 33, sf="ng", ex="*ŋadan > ngadèny; *ŋasa > ngasa; *dəŋən > dengen; *laŋit > langij; *taŋe > nangé",
      notes="'PK nonfinal *ŋ invariably became ng' (p. 33).")
    C("s", "s", 33, ex="*saʔaŋ > saangh; *sadin > sadiny; *asay > asè; *busi > busi; *usa > ósó",
      notes="'PK *s occurred only in nonfinal position, where it invariably remained s' (p. 33).")
    C("h", "∅", 33, sf="Ø", ex="*dahaʔ > daa/raa; *bahaʔ > baa; *bahat > baat; *suhat > sòèj; *suhaʔ > sòòʔ",
      notes="'PK *h was found only in intervocalic position. In OL it disappeared' (p. 33).")
    C("l", "l", 33, ex="*laki > laghi; *lidik > lédéʔ; *alaʔ > ala; *bila > bèla; *ulət > òlet",
      notes="'PK *l remained unchanged' (p. 33).")
    C("w", "β", 33, sf="v", ex="*wadi > fe-vadi; *nawa > nava; *naway > navè; *tawa > tavó; *təlawaʔ > telava",
      notes="'In nonfinal position PK *w was strengthened to v' (p. 33).")
    C("y", "z", 33, ex="*aya > azó; *ayaw > azò; *bayaʔ > baza; *kayu > kaze; *layuk > lazóʔ; *daya > razó",
      notes="'PK *y did not occur in initial position, but medial *y was strengthened to z' (p. 33).")
    C("r", "", 29, blank="not-attested", notes="'Because *r was rare, and is not attested in Soriente (2006), it is passed "
                                               "over here' (p. 29).")
    HI = ("Hiatus: the glide between a high vowel and an unlike vowel 'underwent the same fortition process as phonemic "
          "glides *w and *y' (pp. 33-34).")
    C("∅", "z", 34, env="i_V", ex="*biuʔ > bezu; *kiut > kezek; *lia > lezó; *sian > sezèny; *ia > zó", notes=HI,
      sf="z")
    C("∅", "β", 34, env="u_V", sf="v", ex="*bua > (be)va; *buat > bevèj; *dua > devó/revó; *kuay > kevè; *sui > sevi",
      notes=HI)
