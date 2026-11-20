"""Dobel from PMP: Blust (2014), composed against Proto-Dobel-Koba (decision dobel-composed).

Dobel is already in the sheet under Grimes & Edwards's (2026: 292) Aru nodes:
PMP > Proto-Aru > Proto-Nuclear Aru > Proto-South Aru > Proto-Dobel-Koba > Dobel.
Blust states every reflex against PMP. Each row here is restated against the phoneme that
the Grimes & Edwards rows give Proto-Dobel-Koba for that PMP phoneme, with Blust's
statement in as_printed:
  *p > Aru ɸ > South Aru β;  *b > Aru p > South Aru ɸ (and the identity p, ge-identity-conflicts);
  *s > Nuclear Aru h;  *d, *j, *R > Aru r (*j via R);  *z > Aru y, initially s at PDK;
  *w > South Aru gʷ > PDK kʷ;  *q, *h > Aru ∅.
Dobel gets Blust's inventory (Table 3, after Hughes 1995a), so the implied retentions of
the assumed-unchanged lect no longer apply: the retentions are stated rows here.
"""
L = "dobe1238"
S = "blust2014"
DEC = "dobel-composed"


def build(B):
    # ---- inventory: Table 3 (p. 40), the analysis of Hughes (1995a)
    for ipa, cls, sym in [("t", "C", ""), ("kʷ", "C", "kʷ"), ("ʔ", "C", ""), ("b", "C", ""), ("d", "C", ""),
                          ("ɸ", "C", ""), ("s", "C", ""), ("m", "C", ""), ("n", "C", ""), ("ŋ", "C", ""),
                          ("l", "C", ""), ("r", "C", ""), ("w", "C", ""), ("j", "C", "y"),
                          ("i", "V", ""), ("e", "V", ""), ("a", "V", ""), ("o", "V", ""), ("u", "V", "")]:
        B.P(L, ipa, cls, "hughes1995a", "", sym=sym, via=S, viap="40",
            notes="Table 3 (Blust 2014: 40). Only l r m n y w occur syllable-finally (Hughes, as quoted on p. 41).")

    def C(par, ch, page, ap, env="elsewhere", **kw):
        kw.setdefault("loc", "Table 4" if page == 51 else "")
        kw.setdefault("deriv", "composed")
        kw.setdefault("dec", DEC)
        B.C(L, par, ch, env, src=S, page=page, ap=ap, **kw)

    # *p (PDK β): §2.1, pp. 41-42
    PN = ("Blust provisionally: '*p disappeared word-finally, became /y/ near a front vowel or palatal glide, and "
          "otherwise produced /w/' (p. 42). Table 4 gives the condition only for y. Through Aru *ɸ, South Aru *β.")
    C("β", "∅", 51, "*p > Ø (6)", env="_#", n=6, sf="Ø", notes=PN,
      ex="*dəpa > re; *malip > ʔa-mel; *sapa > ya; *qinəp > n-en; *alap > n-al; *hapuy > say")
    C("β", "w", 51, "*p > w (4)", n=4, notes=PN, ex="*dapuR > rawur; *əpat > ʔawa; *puluq > wur; *panaq > ʔa-wana")
    C("β", "j", 51, "*p > y/__(VC)i (3)", env="_(VC)i", n=3, sf="y", notes=PN,
      ex="*ŋipən > ŋeyan-; *pasək > ʔa-yay; *pija > yira")
    C("β", "b", 41, "*p > b (1)", st="sporadic", n=1, ex="*panaw > ʔa-bana",
      notes="'Evidently a retention from the PCMP innovation *p > b/m__ in bases that took a nasal-final prefix' (p. 41).")
    # *t: §2.2, p. 42
    C("t", "t", 51, "*t > t (8)", n=8, ex="*tasik > tay; *tuna > tuna; *mata > mata-; *batu > ɸatu",
      notes="'PMP *t remained unchanged before a vowel' (p. 42).")
    C("t", "∅", 51, "*t > Ø /__# (5)", env="_#", n=5, sf="Ø", ex="*əpat > ʔawa; *kaRat > ʔa-ʔara; *habaRat > ɸara; *uRat > kʷura-",
      notes="Final vowels were lost (irregularly) before final *t, so the vowels before it are kept (pp. 42, 52).")
    # *k: §2.4, p. 43 (PDK k; Grimes & Edwards already have k > ʔ)
    C("k", "ʔ", 51, "*k > ʔ (11)", n=11, deriv="", dec="",
      ex="*kahiw > ʔay; *kaka > ʔaʔa-; *kutu > ʔutu; *hikan > siʔa; *wakaR > kʷaʔar; *aku > saʔu",
      notes="'PMP *k clearly became Dobel glottal stop in nonfinal position' (p. 43). Second source beside Grimes & "
            "Edwards (2026: 292).")
    C("k", "∅", 51, "*k > Ø /__# (4)", env="_#", n=4, sf="Ø", ex="*manuk > man; *tasik > tay; *anak > yana-; *pasək > ʔa-yay",
      notes="Two of these lost the vowel before the *k too, two kept it (p. 43); Blust suggests the loss of final *k "
            "diffused through the lexicon (p. 52).")
    # *b (PDK ɸ): §2.6, p. 45
    BN = "Through Aru *p and South Aru *ɸ (Grimes & Edwards 2026: 292)."
    C("ɸ", "ɸ", 51, "*b > ɸ (13)", n=13, notes="'Apart from two possible loanwords ... PMP *b invariably became Dobel ɸ' "
                                                "(p. 45). " + BN,
      ex="*batu > ɸatu; *babuy > ɸaɸi; *bəli > ɸeli; *bulan > ɸulan; *qabaRa > la/ɸara/y-")
    C("ɸ", "b", 51, "*b > b (2)", st="sporadic", n=2, ex="*baReq > b-bara-; *baRa > bar-",
      notes="In the first, lenition may have been blocked by the gemination of a partial reduplication; the second is "
            "unexplained (p. 45). " + BN)
    C("p", "ɸ", 51, "*b > ɸ (13)", dec="ge-identity-conflicts",
      notes="Proto-South Aru has both *p > ɸ and an identity *p > p from Proto-Aru *p (< PMP *b) (decision "
            "ge-identity-conflicts); Blust's *b > ɸ is entered from both.")
    # *d, *D, *j, *R (PDK r): §§2.7, 2.8, 2.10, 2.20
    C("r", "r", 51, "*d > r (10); *D > r (1); *j > r (3); *R > r (10)", n=24,
      ex="*dahun > rakʷun; *duha > ro; *bayaD > ʔa-ɸasir; *pija > yira; *laləj > lalir; *Rumaq > ruma/y; *niuR > nor",
      notes="Aru merged *d, *j and *R as r (Grimes & Edwards 2026: 292). *D is reconstructed only finally (p. 45).")
    C("r", "∅", 51, "*d > Ø /__# (1); *R > Ø (2)", env="_#", n=3, sf="Ø", ex="*lahud > law; *um-aRi > ma; *laRiw > ʔa-la",
      notes="*d in the only final example (p. 45); *R 'in two cases in which it became final' (p. 48).")
    C("r", "l", 51, "*j > l (1)", st="sporadic", n=1, ex="*huaji > kʷali-")
    # *z, *y (PDK s initially, y medially)
    C("s", "s", 51, "*z > s (3); *y > s (12)", n=15,
      ex="*zalan > sala; *zauq > s/saw; *ama > sama; *aku > saʔu; *ina > sina; *hikan > siʔa",
      notes="Initial *z, *y and the glide added before initial *a, *i are s at Proto-Dobel-Koba (Grimes & Edwards "
            "2026: 292).")
    C("y", "s", 51, "*z > s (3); *y > s (12)", env="V_V", n=5,
      ex="*quzan > kʷusan; *bayaD > ʔa-ɸasir; *daya > rasa; *buqaya > kʷa-kʷasa; *liaŋ > lisa",
      notes="'In nonfinal position, the PMP palatal glide *y was usually strengthened to s' (p. 49), also the phonetic "
            "glide between i and an unlike vowel; Grimes & Edwards give the change only initially.")
    # *s (PDK h): §2.12, p. 46
    SN = ("'PMP *s usually became Dobel y, but sometimes it disappeared, or remained a voiceless sibilant ... without "
          "statable conditions' (p. 46). Through Nuclear Aru *h (Grimes & Edwards 2026: 292). Table 4 counts 7/8 and "
          "2/3: liya is ambiguous.")
    C("h", "j", 51, "*s > y (7/8)", n=7, sf="y", notes=SN,
      ex="*bəRas > ɸeray; *pasək > ʔa-yay; *sapa > ya; *qasawa > yakʷa-; *salaq > yala; *tasik > tay")
    C("h", "∅", 51, "*s > Ø (2/3)", env="conditions unknown", n=2, sf="Ø", notes=SN,
      ex="*lisəhaq > liya; *ləsuŋ > lowan; *Ratus > ratu")
    C("h", "s", 51, "*s > s (2)", env="conditions unknown", n=2, notes=SN, ex="*sudu > s-sur; *ma-qasin > masin")
    # nasals
    C("m", "m", 51, "*m > m (9)", n=9, ex="*manuk > man; *mata > mata-; *lima > lima; *kami > ʔama")
    C("n", "n", 51, "*n > n (12)", n=12, ex="*niuR > nor; *ina > sina; *tuna > tuna; *quzan > kʷusan")
    C("n", "∅", 51, "*n > Ø /__# (3)", env="_#", n=3, sf="Ø", ex="*kaən > ʔa-ʔa; *zalan > sala; *hikan > siʔa")
    C("ñ", "n", 51, "*ñ > n (1)", env="conditions unknown", n=1, ex="*ma-qañud > ʔa-men")
    C("ñ", "l", 51, "*ñ > l (1)", env="conditions unknown", n=1, ex="*miñak > mila")
    C("ŋ", "n", 51, "*ŋ > n (7)", n=7, ex="*bataŋ > ɸatan-; *naŋuy > ʔa-nen; *daŋi > r-ren; *taŋis > ʔa-ten; *quhaŋ > ʔuwan",
      notes="'PMP *ŋ usually became n' (p. 48).")
    C("ŋ", "ŋ", 51, "*ŋ > ŋ (4)", env="conditions unknown", n=4, ex="*baŋun > ʔa-ɸaŋun; *ŋipən > ŋeyan-; *haŋin > saŋin; *taŋan > taŋin")
    C("ŋ", "∅", 51, "*ŋ > Ø /__# (2)", env="_#", n=2, sf="Ø", ex="*lihaŋ > lisa; *tuqəlaŋ > tul")
    # liquids, glides
    C("l", "l", 51, "*l > l (12)", n=12, ex="*lawaq > l-lakʷa; *lima > lima; *alap > n-al; *bəli > ɸeli",
      notes="Attested only in nonfinal position (p. 48).")
    C("l", "r", 51, "*l > r (1)", st="sporadic", n=1, ex="*puluq > wur")
    C("kʷ", "kʷ", 51, "*w > kʷ (12)", n=12, deriv="", dec="",
      ex="*wahiR > kʷar; *lawaq > l-lakʷa; *qasawa > yakʷa; *uRat > kʷura-; *dahun > rakʷun",
      notes="'In nonfinal position, PMP *w was strengthened to kw', with the secondary glides before *u- and between u "
            "and an unlike vowel (p. 49). Second source beside Grimes & Edwards (2026: 292), whose South Aru *gʷ and "
            "Dobel-Koba *kʷ it agrees with.")
    C("∅", "kʷ", 51, "Ø > w/a__u (2); Ø > w/u__a (2); then *w > kw", env="a_u, u_a", n=4,
      ex="*dahun (> *dawun) > rakʷun; *buaq > ɸukʷa; *tuak > túkʷaʔu",
      notes="The glide inserted between unlike vowels, then fortition (pp. 49, 52). Blust's initial glides (w/#__u, "
            "y/#__a, y/#__i) are Grimes & Edwards's Proto-Aru ∅ > w, y /#_V and are not repeated.")
    C("g", "ŋ", 46, "*g: *gəlap > ŋela ~ ŋélaʔu", st="disputed", n=1, ex="*gəlap > ŋela ~ ŋélaʔu",
      notes="'One possible example of PMP *g was found in the data' (p. 46). Not in Table 4.")
    # vowels: §3, pp. 50-51
    C("a", "a", 50, "*a unchanged", ex="*mata > mata-; *lima > lima",
      notes="'In general, PMP *a, *i, and *u remained unchanged, but there are some conditioned changes' (p. 50).")
    C("a", "e", 50, "*a > e/__Ci", env="_Ci", n=5, ex="*malip > ʔa-mel; *naŋuy (> *naŋi) > ʔa-nen; *daŋi > r-ren; *taŋis > ʔa-ten; *kamuyu > ʔemi",
      notes="'Very widespread in Aru' (p. 50); Manombai keeps the condition without assimilation (n. 18).")
    C("i", "i", 50, "*i unchanged", ex="*lima > lima; *pija > yira")
    C("u", "u", 50, "*u unchanged", ex="*kutu > ʔutu; *tuna > tuna")
    SCH = ("'PMP *ə has no dominant reflex' (p. 51): a (3), e (6), u (3), i (2), o (1), a ~ i (1). It may also have "
           "syncopated in VC__CV.")
    for ch, n, st in [("e", 6, "regular"), ("a", 3, "regular"), ("u", 3, "regular"), ("i", 2, "regular"), ("o", 1, "sporadic")]:
        C("e", ch, 51, f"*ə > {ch} ({n})", env="conditions unknown", st=st, n=n, notes=SCH)
