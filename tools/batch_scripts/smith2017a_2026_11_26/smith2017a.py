#!/usr/bin/env python3
"""Smith (2017a): the small tables named by the gap audit of 26 November 2026.

Batch smith2017a-small-tables. The tables that illustrate one change with lexemes were compared with the rows that
batch smith2017-borneo composed from the main tables; only what those rows did not yet say is entered here.
BATCH.md lists every table and what was done with it.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, existing

S = "smith2017a"
D = "smith2017a-small-tables"
b = Batch(S)
LECTS = existing("lects", "id")


def row(lect, par, child, env, page, notes, loc, ex="", status="regular", derivation="", cond="", n="", total=""):
    b.corr(lect, par, child, env, page, notes, status=status, derivation=derivation, decision=D, locator=loc,
           examples=ex, conditioning=cond, n=n, total=total)


# ================================================================== Müller-Schwaner (Tables 44-48, pp. 136-138)
assert "aohe1238" not in LECTS
b.t["lects"].append(dict(
    id="aohe1238", name="Aoheng", alt_names="Penihing", type="dialect", glottocode="aohe1238", parent_id="pmuller",
    latitude="0.87404", longitude="114.127", inherit="assumed-unchanged", inherit_source_id=S, inherit_page="127",
    inherit_note="Smith's Tables 37-38 have no Aoheng column: he uses 'Seputan data exclusively, rather than Seputan "
                 "and Aoheng, since these two groups speak nearly identical languages' (p. 127). What Tables 44-48 "
                 "do not show for Aoheng is assumed unchanged here, which is known to be too little: the Seputan "
                 "rows of Tables 37-38 are not copied.",
    notes="Upper Mahakam River, above the Boh tributary, East Kalimantan (Smith 2017a: 127). Nearly identical to "
          "Seputan (p. 127); the two share the retention of medial *l before final *ʔ and *ŋ and are grouped "
          "together against Hovongan and Kereho (p. 138). Rows only from Tables 44-48 (pp. 137-138), the five "
          "changes Aoheng shares with Kereho and Seputan against Hovongan. The Aoheng forms of those tables have "
          "no final glottal stop where Kereho has one (oso, mose, ane, cela), as in Seputan; Smith does not state "
          "this for Aoheng and it is not a row. Glottolog: a dialect of Aoheng-Seputan (aohe1237)."))

MS = [("kere1285", "Kereho"), ("sepu1237", "Seputan"), ("aohe1238", "Aoheng")]
T46 = {"kere1285": ("u", "*uRəŋ > ohoŋ; *uvɪ > ovi; *qudaŋ > ore; but *upət > upot", "*ilat > elat"),
       "sepu1237": ("u", "*upət > opot; *uRəŋ > ohoŋ; *uvɪ > ovɪ; *qudaŋ > oraŋ", "*ilat > elat"),
       "aohe1238": ("u", "*upət > opot; *uRəŋ > ohoŋ; *uvɪ > ovɪ; *qudaŋ > oraŋ", "*ilat > elat")}
T47 = {"kere1285": "*ma-həsak > moseʔ; *anak > aneʔ; *əñak > oñeʔ",
       "sepu1237": "*ma-həsak > mose; *anak > ane; *əñak > oñe",
       "aohe1238": "*ma-həsak > mose; *anak > ane; *əñak > oñe"}
T44 = {"kere1285": "*cəlaʔ > celaʔ", "sepu1237": "*cəlaʔ > celaʔ", "aohe1238": "*cəlaʔ > cela"}
for lect, name in MS:
    row(lect, "u", "o", "#_", "137",
        f"'High vowels lowered to mid vowels at the beginning of words in Kereho, Seputan, and Aoheng (with a small "
        f"number of exceptions) but not in Hovongan' (p. 137)."
        + (" Kereho upot 'bait' keeps u." if lect == "kere1285" else ""),
        "Table 46", ex=T46[lect][1])
    row(lect, "i", "e", "#_", "137",
        "Lowering of initial high vowels (p. 137); Table 46 has one example with *i.", "Table 46", ex=T46[lect][2])
    row(lect, "i", "e", "_ʔ# (PMÜL *-iʔ from PMP *-ak)", "138",
        "'PMÜL *-i (from PMP *-ak) lowered to *-e in Kereho, Seputan, and Aoheng, but not in Hovongan' (p. 138). "
        "Smith states it only for the *i that comes from *-ak.", "Table 47", ex=T47[lect])
    row(lect, "ə", "e", "penultimate syllable, after c", "136",
        "'In one case, reflexes of *ə from *zəlaq are e in Kereho, Seputan, and Aoheng. This is apparently the "
        "result of a palatalizing effect from *z' (p. 136).", "Table 44", ex=T44[lect], status="sporadic", n=1)
row("aohe1238", "ə", "o", "penultimate syllable", "136",
    "'In Hovongan, penultimate *ə lowered to *a, but in Kereho, Seputan, and Aoheng it backed to *o' (p. 136). "
    "Initial schwa too: it 'was deleted in Hovongan, but it was retained as *o in Kereho, Seputan, and Aoheng' "
    "(p. 138, Table 48). *bətəhiʔ > bətohi is printed with ə in the first syllable.",
    "Tables 44, 48", ex="*bəhat > bohat; *həcan > hocan; *əpat > opat; *ənəm > onom; *əbun > ovun")
row("aohe1238", "u", "o", "_k#", "137",
    "'In Kereho, Seputan, and Aoheng, *u lowered to *o before *k, but it did not in Hovongan' (p. 137). The "
    "environment is written as in the Kereho and Seputan rows of Table 38; final *k is ʔ in Proto-Müller-Schwaner.",
    "Table 45", ex="*manuk > manoʔ; *mabuk > mavoʔ; *Rusuk > oso; *bəduk > boroʔ")
row("pmuller", "a", "i", "_k#", "138",
    "'PMÜL *-i (from PMP *-ak)' (p. 138); the section list on p. 136 calls it 'raising in reflexes of *-ak'. "
    "Table 39 does not have it. Hovongan keeps the i (oniʔ 'child', mosiʔ 'ripe').", "Table 47",
    ex="*anak > Hovongan oniʔ, Kereho aneʔ; *ma-həsak > Hovongan mosiʔ, Kereho moseʔ")

# ================================================================== Punan (Tables 32, 34; pp. 120-122)
PUN = [("punanlisum", "Punan Lisum", "", "Lisum", "", "",
        "East and North Kalimantan (Smith 2017a: 112). No Glottocode: Glottolog's Lisum (lisu1251) is filed as a "
        "dialect of Rejang Kayan, although its Punan subgroup Bukat-Ukit-Beketan-Lugat-Lisum (buka1263) is named "
        "after it (decision smith2017a-small-tables).",
        dict(horn="wəŋ", I="jək", night="maləm", die="kavə", five="limə", three="taloŋ", fell="navəŋ",
             hut="lapow", four="apat", full="panuʔ", gall="parun")),
       ("buka1261", "Buket", "Bukat", "", "1.29075", "113.246",
        "Upper Kapuas, West Kalimantan (Smith 2017a: 112). Glottolog's Bukat.",
        dict(horn="uəŋ", I="jək", night="maləm", die="kavə", five="limə", three="talo", fell="navəŋ",
             hut="lapo", four="apat", full="panuʔ", gall="parun"))]
for lid, name, alt, alt2, lat, lon, notes, f in PUN:
    assert lid not in LECTS
    b.t["lects"].append(dict(
        id=lid, name=name, alt_names=";".join(x for x in (alt, alt2) if x), type="language",
        glottocode=lid if lid == "buka1261" else "", iso639_3="bvk" if lid == "buka1261" else "",
        parent_id="ppunan", latitude=lat, longitude=lon, inherit="assumed-unchanged", inherit_source_id=S,
        inherit_page="120-122",
        inherit_note="Tables 29-30 have no column for this dialect; apart from the two statements about *ə "
                     "(pp. 120-122) nothing is stated, and the rest is assumed unchanged from Proto-Punan.",
        notes=notes + " A Punan dialect for Smith; rows only from Tables 32 and 34 (pp. 120, 122) and Figure 28."))
    row(lid, "ə", "ə", "_#", "120",
        "'Although Proto-Punan had raised final *-a to schwa, only Ukit, Buket and Punan Lisum retain PPUN *-ə "
        "(from *-a) unchanged. All other Punan dialects have backed *-ə to o' (p. 120). In dialects 'like Ukit and "
        "Buket, where ə is found word-finally, it is realized as [ɘ]' (p. 126).",
        "Table 32", ex=f"*lima > {f['five']}; PCS *kəbəs > {f['die']}", derivation="stated-retention")
    row(lid, "ə", "ə", "_C#", "120",
        "Final-syllable *ə is not backed to o (Table 32); 'Punan Lisum, Ukit, and Buket retain *ə unchanged in "
        "final syllables' (p. 122).",
        "Table 32", ex=f"*uRəŋ > {f['horn']}; PPUN *jək > {f['I']}; *maləm > {f['night']}; *təbəŋ > {f['fell']}",
        derivation="stated-retention")
    row(lid, "ə", "a", "penultimate syllable", "122",
        "Figure 28: 'Other Punan: Penultimate *ə > *a' (the dialects other than Punan Tubu and Punan Bah).",
        "Table 34; Figure 28",
        ex=f"*kəvə > {f['die']}; *təlu > {f['three']}; *təbəŋ > {f['fell']}; *ləpaw > {f['hut']}; "
           f"*pənuʔ > {f['full']}; *qapəju > {f['gall']}")

# Punan Bah: Table 36 (p. 126)
PB = "puna1276"
for ph, al, src in [("i", "iə̯", "*-ik > iə̯ʔ: *mudik > mudiə̯ʔ"), ("u", "uə̯", "*-uk > uə̯ʔ: *ñamuk > ñamuə̯ʔ"),
                    ("e", "eə̯", "*-ak > eə̯ʔ: *burak > bureə̯ʔ; e here is from *a"),
                    ("o", "oə̯", "*-ək > oə̯ʔ: *ambək > aboə̯ʔ; o here is from *ə")]:
    b.allo(PB, ph, al, "before word-final /k/ [ʔ]", "125-126",
           f"Table 36 lists it in parentheses as an allophone: 'uə̯ʔ, iə̯ʔ, eə̯ʔ, and oə̯ʔ are allophones of uk, ik, "
           f"ek, and ok in final position' (p. 126). {src}. The correspondence rows from Table 30 have the "
           f"off-glide vowels as reflexes before final *k and *ŋ (decision {D}).")
b.allo(PB, "k", "ʔ", "word-finally", "126",
       "'There are no examples of word-final *-k': off-glides and glottal stop appear word-finally, pure vowels and "
       "k elsewhere (p. 126). Before this ʔ a vowel has an off-glide; before ʔ from *q it does not "
       "(*pusuq > pusuʔ, p. 125).")

# ================================================================== Land Dayak (Table 53, pp. 152-153)
T53 = "Table 53"
PB_NOTE = ("'Generally, schwa after *p, or *b was deleted in Hliboi, is reflected with i in Sungkung, and assimilated "
           "to the place of the following vowel in other languages. These correspondences are not perfect' (p. 153). ")
row("hliboi", "ə", "∅", "penultimate syllable, after p or b", "152-153",
    PB_NOTE + "Table 53: deleted in five of the six words; *qapəju 'gall' has i.", T53,
    ex="*bəsuR, *pənuq (hnuə̯ʔ, p. 166), *bəli, *bətis (/ddis/, p. 167), *pədeʔ: Ø", n=5, total=6)
row("sungkung", "ə", "i", "penultimate syllable, after p or b", "152-153",
    PB_NOTE + "Table 53: i in the four words with a Sungkung form; *qapəju 'gall' has u.", T53,
    ex="*bəsuR, *pənuq, *bəli, *pədeʔ: i", n=4, total=5)
SLD = {"jang1257": ("Jangkang", "*bəsuR, *pənuq, *qapəju: u", 3, 3, "*bəli, *bətis: i", 2, 2, ""),
       "ribu1241": ("Ribun", "*bəsuR, *pənuq, *qapəju: u", 3, 3, "*bəli: i", 1, 1, ""),
       "golik": ("Golik", "*pənuq, *qapəju: u", 2, 3, "*bəli, *pədeʔ: i", 2, 2, " *bəsuR has i in Golik."),
       "sang1339": ("Sanggau", "*bəsuR, *pənuq, *qapəju: u", 3, 3, "*bəli: i", 1, 1, "")}
for lid, (name, exu, nu, tu, exi, ni, ti, extra) in SLD.items():
    row(lid, "ə", "u", "penultimate syllable, after p or b, before u in the next syllable", "152-153",
        PB_NOTE + "Read from the table for this language: u where the next vowel is *u." + extra, T53,
        ex=exu, n=nu, total=tu)
    row(lid, "ə", "i", "penultimate syllable, after p or b, before a front vowel in the next syllable", "152-153",
        PB_NOTE + "Read from the table for this language: i where the next vowel is *i (or *e in *pədeʔ).", T53,
        ex=exi, n=ni, total=ti)
A_NOTE = ("Penultimate *a, with the *ə that merged with it in Proto-Bidayuh-Southern Land Dayak, is reflected "
          "'with o in the Southern Land Dayak languages, as well as in Singai' (p. 152). Counted over the thirteen "
          "words of Table 53 with *a or merged *ə (from *təbəŋ down). ")
SLDA = {"jang1257": ("*təbuh, *təlu, *kəbəs, *lamin, *pajay, *hapuy, *paku, *batu: o", 8, 10,
                     "a in *təRas; i in *təbəŋ."),
        "ribu1241": ("*təbuh, *dəpa, *kəbəs, *lamin, *pajay, *hapuy, *batu: o", 7, 10,
                     "a in *təlu and *təRas; i in *təbəŋ."),
        "golik": ("*təbuh, *kəbəs, *lamin, *pajay, *hapuy, *paku: o", 6, 10,
                  "a in *təlu, *təRas, *batu and *tanəq."),
        "sang1339": ("*təbuh, *təlu, *kəbəs, *lamin, *pajay, *hapuy, *paku, *batu: o", 8, 9, "i in *təbəŋ.")}
for lid, (ex, n, tot, exc) in SLDA.items():
    row(lid, "a", "o", "penultimate syllable", "152", A_NOTE + "Exceptions in the table: " + exc, T53, ex=ex,
        n=n, total=tot)
row("hliboi", "a", "i", "conditions unknown", "152",
    "Penultimate syllable. Table 53: Hliboi has i in six of the ten words with penultimate *a or merged *ə and a "
    "in four; 'penultimate schwa in *təbu 'sugarcane' is reflected with i in Hliboi' and 'the same "
    "correspondences are found with reflexes of *a in penultimate position' (p. 152). Smith gives no condition "
    "for i against a.", T53, ex="*təbəŋ, *təbuh, *kəbəs, *pajay, *hapuy, *paku: i", n=6, total=10)
row("hliboi", "a", "a", "conditions unknown", "152",
    "Penultimate syllable: a in four of the ten words of Table 53, beside i in six.", T53,
    ex="*təlu, *təRas, *batu, *tanəq: a", n=4, total=10)

# Hliboi inventory (Tables 54-55, pp. 164, 166)
HL = "hliboi"
for ipa, sym, note in [("p", "p", ""), ("t", "t", ""), ("k", "k", ""), ("ʔ", "ʔ", ""), ("b", "b", ""), ("d", "d", ""),
                       ("ɟ", "j", "Printed 'j [ɟ]': 'a voiced palatal stop ɟ' (p. 164)."), ("ɡ", "g", ""),
                       ("m", "m", ""), ("n", "n", ""), ("ɲ", "ñ", ""), ("ŋ", "ŋ", ""), ("s", "s", ""), ("h", "h", ""),
                       ("l", "l", "'r is not found in Hliboi, and loanwords with r are altered to l' (p. 164)."),
                       ("w", "w", ""), ("j", "y", "")]:
    b.t["phonemes"].append(dict(lect_id=HL, ipa=ipa, source_symbol=sym, **{"class": "C"}, origin="sourced",
                                source_id=S, page="164", notes=("Table 54. " + note).strip()))
for ipa, sym, note, st in [("i", "i", "", ""), ("u", "u", "", ""), ("e", "e", "", ""), ("o", "o", "", ""),
                           ("a", "a", "", ""), ("ej", "ey", "A diphthong.", ""), ("uj", "uy", "A diphthong.", ""),
                           ("əw", "əw", "A diphthong.", ""), ("aj", "ay", "A diphthong.", ""),
                           ("ə", "ə", "In parentheses in the table: 'there are no examples of schwa in native "
                                      "vocabulary. Schwa does appear, however, in loanwords' (p. 166).", "marginal"),
                           ("aw", "aw", "In parentheses in the table; the text does not say why.", "marginal")]:
    b.t["phonemes"].append(dict(lect_id=HL, ipa=ipa, source_symbol=sym, **{"class": "V"}, origin="sourced",
                                source_id=S, page="166",
                                notes=("Table 55: 'Hliboi has nine vowels, including diphthongs' (p. 166). "
                                       + note).strip(), status=st))
for ph, al, env, note in [
        ("i", "əi̯", "word-finally", "'High vowels have a lowered nucleus in word-final position' (p. 166): /bati/ [baˈtəi̯]."),
        ("i", "iə̯", "in closed syllables", "A mid-central off-glide in closed syllables (pp. 166-167): /ddis/ [ˈddiə̯s]."),
        ("i", "ɪ", "before alveolars, particularly -n and -t", "'Often' (p. 167): /mlitn/ [ˈmlɪtn]."),
        ("u", "əu̯", "word-finally; before ʔ and h", "pp. 166-167: /njuʔ/ [ˈnjəu̯ʔ]."),
        ("u", "uə̯", "in closed syllables", "pp. 166-167: /ŋkuʔub/ [ŋkuˈʔuə̯b]."),
        ("ej", "i̯ei̯", "not stated", "Table 55 prints 'ey [i̯ei̯]'."),
        ("uj", "uə̯j", "not stated", "Table 55 prints 'uy [uə̯y]'.")]:
    b.allo(HL, ph, al, env, "166-167", note)

# ================================================================== Kelai inventory (Tables 19-20, p. 78)
KE = "kela1259"
for ipa, sym, note, st in [("p", "p", "", ""), ("t", "t", "", ""), ("t͡ʃ", "c", "Smith's c is [ʧ] (p. 26).", ""),
                           ("k", "k", "", ""), ("ʔ", "ʔ", "", ""), ("b", "b", "", ""), ("d", "d", "", ""),
                           ("d͡ʒ", "j", "Smith's j is [ʤ] (p. 26).", ""), ("ɡ", "g", "", ""), ("m", "m", "", ""),
                           ("n", "n", "", ""), ("ɲ", "ñ", "", ""), ("ŋ", "ŋ", "", ""), ("s", "s", "", ""),
                           ("h", "h", "", ""), ("l", "l", "Printed 'l/(r)' in the row of approximants.", ""),
                           ("r", "r", "Printed in parentheses, 'l/(r)'; the text does not say why.", "marginal"),
                           ("w", "w", "The only glide in the table; there is no y.", "")]:
    b.t["phonemes"].append(dict(lect_id=KE, ipa=ipa, source_symbol=sym, **{"class": "C"}, origin="sourced",
                                source_id=S, page="78", notes=("Table 19. " + note).strip(), status=st))
for ipa, sym in [("i", "i"), ("u", "u"), ("e", "e"), ("ɛ", "ɛ"), ("ə", "ə"), ("o", "o"), ("æ", "æ"), ("a", "a"),
                 ("ɒ", "ɒ"), ("iw", "iw"), ("uj", "uy"), ("ew", "ew"), ("əw", "əw"), ("oj", "oy"), ("æw", "æw"),
                 ("ao̯", "ao̯"), ("ai̯", "ai̯"), ("ae̯", "ae̯")]:
    b.t["phonemes"].append(dict(lect_id=KE, ipa=ipa, source_symbol=sym, **{"class": "V"}, origin="sourced",
                                source_id=S, page="78",
                                notes="Table 20: '18 distinctions, including a number of diphthongs, but no "
                                      "triphthongs' (p. 78)."))

# ================================================================== Malayic (Tables 61, 63-65; pp. 186-195)
T61 = "Table 61"
BR = ("'Where *a is followed by *u or *i, the high vowels became *ye and *wo, and eventually, in Seberuang, Iban, "
      "and Mualang, yə and wə' (p. 186). Entered as an inserted glide and the change of the vowel. ")
BRK = {"ketapang": ("*jauh > jowoh; *daun > dowon; *laut > lowot", "*jahit > johet; *kail > koyel"),
       "sebe1242": ("*jauh > jawəh; *daun > dawən; *laut > lawət", "*baik > bayək; *naik > nayək; *jahit > jayet"),
       "iban1264": ("*jauh > jawəh; *daun > dawən", "*jahit > jayet"),
       "mual1241": ("*jauh > jawəh; *daun > dawən; *laut > lawət", "*baik > bayək; *jahit > jayet; *kail > kayel")}
for lid, (exu, exi) in BRK.items():
    row(lid, "∅", "w", "a_u", "186-187", BR, T61, ex=exu)
    row(lid, "∅", "j", "a_i", "186-187", BR + "Smith's y.", T61, ex=exi)
    if lid == "ketapang":
        row(lid, "u", "o", "a_ (after the inserted glide)", "186-187",
            BR + "Ketapang keeps the stage *wo; the *a before it is o in these words.", T61, ex=exu)
        row(lid, "i", "e", "a_ (after the inserted glide)", "186-187", BR + "Ketapang keeps the stage *ye.", T61,
            ex=exi)
    else:
        row(lid, "u", "ə", "a_ (after the inserted glide)", "186-187", BR, T61, ex=exu)
        if lid != "iban1264":
            row(lid, "i", "ə", "a_ (after the inserted glide)", "186-187",
                BR + "Table 61 has ə in *baik and *naik, but e in *jahit and *kail, which Smith does not explain.",
                T61, ex="; ".join(x for x in exi.split("; ") if "ə" in x))
        row(lid, "i", "e", "a_ (after the inserted glide)", "186-187",
            BR + "The stage *ye is what Table 61 shows in *jahit (and *kail); Smith's statement would give yə."
            + (" The only Iban form with *ai in the table." if lid == "iban1264" else ""),
            T61, ex="; ".join(x for x in exi.split("; ") if "ə" not in x), cond="unknown")

H63 = {"kend1254": "'raw' mantaʔ; 'wet' basaʔ; 'fall' jantuʔ", "keni1248": "'raw' mataʔ; 'wet' basaʔ; 'fall' jatuʔ",
       "sebe1242": "'raw' mataʔ; 'greedy' ɣaŋkaʔ; 'fall' jatoʔ", "iban1264": "'raw' mataʔ; 'greedy' raŋkaʔ; 'tired' ləlaʔ",
       "mual1241": "'raw' mantaʔ; 'tired' ləlaʔ"}
for lid, ex in H63.items():
    row(lid, "h", "ʔ", "_#", "193",
        "'The irregular change *-q > *-ʔ (where *q normally became *h) is very inconsistent': only *mataq 'raw; "
        "unripe' has a final glottal stop across the board (Ketapang matah excepted), and the other words 'do not "
        "show any consistency across languages' (p. 193).", "Table 63", ex=ex, status="sporadic",
        n=len(ex.split(";")), total=5)

DI = {"iban1264": ("'hold' məgay; 'road' jalay; 'come' datay; 'big' bəsay; 'long' pañay; 'old' tuay; 'eat' makay; "
                   "'fly' tərbay; 'mat' tikay; 'we incl' kitay; 'feel' asay; 'go home' pulay; 'shrimp' unay; "
                   "'plate' piŋay; 'flower' buŋay; 'derris' tubay; 'naked' təlañay",
                   "'above' ataw; 'with' ŋaw; 'shadow' ayaw; 'rice grain' bəraw; 'harvest' ŋətaw; 'ripe' mansaw",
                   "In the Iban of the upper Kapuas it 'agrees with that reported in Adelaar (1992a) and Nothofer "
                   "(1988), lexeme-by-lexeme' (p. 193); 13 of the 23 inconsistent cases are in Iban alone (p. 194)."),
      "sebe1242": ("'hold' məgay; 'road' jalay; 'come' datay; 'big' bəsay; 'long' pañay; 'old' tuay; 'eat' makay; "
                   "'exist' aday; 'we incl' kitay; 'feel' pəɣasay; 'go home' pulay",
                   "'above' ataw; 'with' ŋaw",
                   "'Diphthongization is also found in Seberuang and Mualang, but to a lesser degree', spread 'from "
                   "an Iban core of influence' and not inherited (p. 193)."),
      "mual1241": ("'hold' məgay; 'road' jalay; 'come' datay; 'big' bəsay; 'long' pañay; 'old' tuay; 'eat' makay; "
                   "'exist' aday; 'cockroach' kicay; 'crush' ŋancay; 'discard' muay; 'fly' təɣbay; 'mat' tikay",
                   "'above' ataw; 'with' ŋaw",
                   "'Diphthongization is also found in Seberuang and Mualang, but to a lesser degree', spread 'from "
                   "an Iban core of influence' and not inherited (p. 193).")}
for lid, (exy, exw, extra) in DI.items():
    base = ("Iban diphthongization: 'a process where final *-a(C) became -ay or -aw in a number of lexemes' (p. 193); "
            "a final consonant is lost with it. Smith found 25 cases of -ay, eight of them in all of Iban, Seberuang "
            "and Mualang, and eight of -aw, two of them in all three. ")
    row(lid, "a", "aj", "_(C)# (the consonant is lost)", "193-195", base + extra, "Tables 64-65", ex=exy,
        status="sporadic", n=len(exy.split(";")))
    row(lid, "a", "aw", "_(C)# (the consonant is lost)", "193-195", base + extra, "Tables 64-65", ex=exw,
        status="sporadic", n=len(exw.split(";")))

# ================================================================== Siang (Table 82, pp. 278-279)
assert "sian1254" not in LECTS
b.t["lects"].append(dict(
    id="sian1254", name="Siang", type="language", glottocode="sian1254", iso639_3="sya", parent_id="pbarito",
    latitude="-0.38398", longitude="114.693", inherit="assumed-unchanged", inherit_source_id=S, inherit_page="278-279",
    inherit_note="Smith states one reflex for Siang (*z); it has no column in Tables 56-57. Everything else is "
                 "assumed unchanged from PMP, which the Siang forms of Table 82 show to be too little (they have ɾ "
                 "for *l and o for *ə, as Kadorih does).",
    notes="Data from Hudson (1967), as Smith cites it (2017a: 278). 'It appears that Siang belongs to the same group "
          "of Barito languages that Kadorih does' (p. 279). The only row is the reflex of *z, which Smith uses to "
          "argue that Kadorih *z > c is inherited and its j borrowed from Ngaju."))
row("sian1254", "z", "t͡ʃ", "elsewhere", "278-279",
    "'Siang regularly reflects *z as c' (p. 279). Smith's c is [ʧ] (p. 26). Siang data from Hudson (1967).",
    "Table 82", ex="*zəlaq > coɾaʔ; *zaʔa > caa; *zalan > caɾan; *haRəzan > kucan; *quzan > ucan; *azuq > ocu; "
                   "*zaqat > ceet", n=7, total=7)

# ================================================================== decision
b.dec(D,
      "Smith (2017a): the tables that illustrate single changes with lexemes, and the inventories of the language "
      "sketches (gap audit of 26 November 2026). What is entered from them?",
      "Only what the rows of batch smith2017-borneo did not yet say. New lects from tables with a variety that was "
      "not a lect: Aoheng (aohe1238, Tables 44-48), Punan Lisum (no Glottocode) and Buket (buka1261, Tables 32, 34), "
      "Siang (sian1254, Table 82), each with only the rows those tables state and the rest assumed unchanged. Rows "
      "added to existing lects: the lowering of initial high vowels and of *-iʔ from *-ak in Kereho and Seputan, "
      "and PMÜL *-ak > *-i(ʔ) (Tables 46-47); penultimate schwa after *p, *b and penultimate *a in Hliboi, Sungkung, "
      "Jangkang, Ribun, Golik and Sanggau, read off Table 53 with counts; vowel breaking after *a in Ketapang, "
      "Seberuang, Iban and Mualang (Table 61) as an inserted glide plus a vowel change; sporadic *-h > ʔ (Table 63) "
      "and Iban diphthongization (Tables 64-65). Sourced inventories: Hliboi (Tables 54-55, j entered as ɟ) and "
      "Kelai (Tables 19-20). Punan Bah's off-glide vowels are entered as allophones (Table 36) beside the existing "
      "rows that have them as reflexes. Not entered: the Merap inventory (Tables 12-13), because the Merap rows "
      "from Smith (2017b) use symbols the table does not have; Biatah, Bukar-Sadong and Singai (Table 53), Lepo' "
      "Tau and Lepo' Sawa' (Table 81) and Western Penan (Tables 89-90), which are not lects; Table 79; Table 88 "
      "(Proto-Central Sarawak is held back). Kadorih *z (Tables 82-83) is left as it is: see the alternatives.",
      "Enter no lect from a lexeme table; or copy Seputan's rows to Aoheng; or give Punan Lisum lisu1251. Replace "
      "the off-glide reflex rows of Punan Bah by the plain vowels. Respell the existing Hliboi row *z > d͡ʒ as ɟ, and "
      "the Kelai rows with aj, aw, aːe̯, j, which are outside the sourced inventories. For Kadorih, mark the rows "
      "*z > d͡ʒ as borrowed from Ngaju (loan-stratum): Smith argues that *z became c and that j is secondary "
      "(pp. 279-280).", "54-280")

write("smith2017a-small-tables", b.t, """# smith2017a-small-tables

Source: Smith (2017a), *The languages of Borneo: A comprehensive classification* (PhD dissertation, University of
Hawai'i at Mānoa). The tables the gap audit of 26 November 2026 listed as not cited. Printed page = PDF page - 30.
Read from the text layer; Tables 12-13, 19-20, 36, 55 and 66 were also compared with page images.

Every table was compared with the rows of batch `smith2017-borneo` before anything was entered.

| Table (page) | Result |
|---|---|
| 5, 6 (pp. 54-55) glottal stop in Kayan | already rows (Proto-Kayan ∅ > ʔ, *i > e, *u > o; Long Naah and Balui Liko ʔ > ∅; Bahau aː); nothing added |
| 10 (p. 66) final voiced obstruents in Kayanic | every cell is already a row; nothing added. Smith (2017b) Tables 5-6 are the same tables |
| 12-13 (p. 68) Merap inventory | not entered (see below). Smith (2017b) Tables 3-4 are the same tables |
| 19-20 (p. 78) Kelai inventory | entered as the sourced inventory of Kelai |
| 32, 34 (pp. 120, 122) Punan *ə | new lects Punan Lisum and Buket; the other columns are already rows |
| 35 (p. 125) schwa off-glides | already rows on Punan Bah, Sekapan, Kejaman |
| 36 (p. 126) Punan Bah vowels | allophone rows (off-glide vowels, final k as ʔ) |
| 44-48 (pp. 137-138) Müller-Schwaner | new lect Aoheng; Kereho and Seputan: initial high vowels, *-iʔ > eʔ, ə > e after c; PMÜL *-ak > *-i |
| 53 (p. 152) Land Dayak penultimate schwa | rows for Hliboi, Sungkung, Jangkang, Ribun, Golik, Sanggau, with counts |
| 54-55 (pp. 164, 166) Hliboi inventory | entered as the sourced inventory of Hliboi, with allophones |
| 61 (p. 187) breaking after *a | rows for Ketapang, Seberuang, Iban, Mualang |
| 62 (p. 192) added final glottal stop | already rows (sporadic ∅ > ʔ); nothing added |
| 63 (p. 193) *-h as glottal stop | sporadic rows for Kendayan, Keninjal, Seberuang, Iban, Mualang |
| 64-65 (pp. 194-195) Iban diphthongization | sporadic rows for Iban, Seberuang, Mualang |
| 66 (p. 199) Kapuas Iban vowels | the seven vowels and the allophones are already in; nothing added |
| 69 (p. 221) *R > g / _i in Dusunic | already rows of Proto-Dusunic and Proto-Bisaya-Lotud from Lobel (2013) |
| 79 (p. 244) low vowel fronting | not entered: the rows on Berawan and Lower Baram have it as sporadic; restating them with Smith's conditions is a revision of existing rows |
| 81 (p. 255) Highland Kenyah | not entered: Lepo' Tau and Lepo' Sawa' are not lects, and Proto-Kenyah has no nasal-obstruent rows |
| 82-83, 85 (pp. 279-281) Kadorih | new lect Siang (*z > c); Kadorih *y > c and *l > ɾ are already rows; Kadorih *z is in the decision |
| 88 (p. 321) Proto-Central Sarawak | not entered (held back) |
| 89-90 (p. 341) Kajang after schwa | already rows of Proto-Kajang; Western Penan is not a lect |
| 91 (p. 428) Barito changes | not compared row by row with the Barito lects |

Not entered: the Merap inventory. The Merap rows come from Smith (2017b) §4 and use ay, aw, ow, iːə̯, uːə̯, kʷ, ŋʷ, c
and ʄ, which Tables 12-13 do not list; a sourced inventory would put a warning on each. It needs a reading of the
paper's §3 beside its §4.

After the merge the build warns for reflexes outside the two new sourced inventories (Hliboi d͡ʒ; Kelai aj, aw, aːe̯,
j and others). They are listed in decision `smith2017a-small-tables`.
""")
