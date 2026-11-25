#!/usr/bin/env python3
"""Reid (1994), Unravelling the linguistic histories of Philippine Negritos.

In Dutton & Tryon (eds.), Language contact and change in the Austronesian world, 443-475. New lects Northern Alta,
Southern Alta (group Altan) and Arta under Proto-Northern Luzon (Reid 2006's Cordilleran, whose tree has Altan and
Arta as branches), with the reflexes Reid gives in §5 (Tables 1, 12-15, 18 and the text), stated against
Proto-Philippines and Proto-Cordilleran.
"""
from common import Batch, write, chapter, CONSULTED

S = "reid1994"
b = Batch(S)
b.t["sources"].append(chapter(
    S, "Reid, Lawrence A.", "Unravelling the linguistic histories of Philippine Negritos", "443-475",
    CONSULTED + "§§1-4: Philippine Negritos, their names and earlier views of their languages. §5: the Alta "
    "(Northern and Southern; Sierra Madre, Nueva Ecija and Aurora) and the Arta (Addalem River, Quirino), from the "
    "author's field work in 1987 (Reid 1988b, 1989): Alta l < *R (Table 1, p. 452), conservative lexicon and "
    "pronouns (Tables 2-3), loans with g < *R from Tagalog and other groups (Tables 4-10); Arta's unique forms (Table "
    "11), its reflexes of *R (r; g in loans, Tables 12-13), *j (d, Table 14) and *k (Ø, Table 15), pronouns (Tables "
    "16-17), vowel harmony after voiced stops (Table 18) and loans from Gaddang, Ilokano and Casiguran Dumagat "
    "(Tables 19-21)."))

b.t["sources"] += [
    dict(id="reid1988b", author="Reid, Lawrence A.", year="1988", year_suffix="b",
         title="The Alta languages of the Philippines", kind="comparative", pub_type="presentation",
         notes="Paper presented to the Fifth International Conference on Austronesian Linguistics, Auckland. "
               "Bibliographic details from the reference list of Reid (1994: 474); not consulted directly."),
    dict(id="reid1989", author="Reid, Lawrence A.", year="1989", title="Arta, another Philippine Negrito language",
         kind="comparative", pub_type="article", container_title="Oceanic Linguistics", volume="28", issue="1",
         pages="47-74", notes="Bibliographic details from the reference list of Reid (1994: 474); not consulted "
                              "directly."),
]

PNL, ALT, ALN, ALS, ART = "pnl", "altan", "nort2875", "sout2905", "arta1239"
TREE = ("Under Proto-Northern Luzon (Reid 2006's Cordilleran), which Reid's tree (2006: 4) divides into Altan, "
        "Meso-Cordilleran, Arta, Ilokano and Northern Cordilleran. Reid (1994: 452-455) relates the Alta languages "
        "to Meso-Cordilleran (Central and Southern Cordilleran) by their l < *R and man- prefix, but notes that "
        "they keep forms and pronouns that all other Meso-Cordilleran languages replaced; no Meso-Cordilleran node "
        "is entered.")
b.t["lects"] += [
    dict(id=ALT, name="Altan", alt_names="Alta", type="group", parent_id=PNL, region="Sierra Madre, Luzon",
         notes="The two Alta languages, 'very distinct languages one from the other' (Reid 1994: 450). " + TREE +
               " No proto-language is reconstructed; Glottolog has no node for the pair."),
    dict(id=ALN, name="Northern Alta", alt_names="AltN;Alta", type="language", glottocode="nort2875",
         iso639_3="aqn", parent_id=PNL, tree_parent=ALT, latitude="15.6913", longitude="121.454",
         region="Baler River valley, Aurora, and Dingalan; Nueva Ecija", inherit="assumed-unchanged",
         inherit_source_id=S, inherit_page="452",
         notes="Negrito language; most speakers are bilingual in Tagalog (Reid 1994: 450). Data from Reid's field "
               "work (1987; Reid 1988b). Coordinates from Glottolog 5.4."),
    dict(id=ALS, name="Southern Alta", alt_names="AltS;Kabulowan", type="language", glottocode="sout2905",
         iso639_3="agy", parent_id=PNL, tree_parent=ALT, latitude="15.1841", longitude="121.054",
         region="South-eastern Nueva Ecija to the boundary of Aurora and Nueva Vizcaya", inherit="assumed-unchanged",
         inherit_source_id=S, inherit_page="452",
         notes="Negrito language, strongly influenced by Tagalog and in contact with Umiray Dumaget (Reid 1994: 450, "
               "455-462). Coordinates from Glottolog 5.4."),
    dict(id=ART, name="Arta", type="language", glottocode="arta1239", iso639_3="atz", parent_id=PNL,
         latitude="16.4185", longitude="121.656", region="Addalem River near Aglipay and Maddela, Quirino",
         inherit="assumed-unchanged", inherit_source_id=S, inherit_page="463-467",
         notes="Fewer than fifty families of Negritos (Reid 1994: 462). About 29% of Reid's 512 items are unique to "
               "Arta, and it keeps only 26.9% of Blust's 200 PMP basic items (p. 463). Many loans from Ilokano, "
               "Gaddang and Casiguran Dumagat (Tables 19-21). " + TREE + " Coordinates from Glottolog 5.4."),
]
D = "reid1994-negritos"


def r(lect, par, ch, env, page, notes, status="regular", **k):
    b.corr(lect, par, ch, env, page, notes, status=status, derivation="", decision=D, **k)


for L in (ALN, ALS):
    r(L, "R", "l", "elsewhere", "452", "Table 1: 'the l reflex of *R, the reflex also found in all the Central and "
      "Southern Cordilleran languages' (p. 452): *kaRat > AltN qalat, AltS kalat 'bite', *qaRtaq > qalta 'man', "
      "*baqeRu > AltN balu, AltS belo 'new'. Words with g are loans (Table 4, p. 455).")
    r(L, "R", "ɡ", "in loans", "455-462", "Tables 4-10: Southern Alta words with g < *R are borrowed, mostly from "
      "Tagalog, since *R > g in all Northern Cordilleran and Central Philippine languages.", status="loan-stratum")
    r(L, "j", "d", "elsewhere", "464", "'The only languages in Northern Luzon which are presently known to have a d "
      "reflex of *j, apart from Arta, are the Alta languages, and the Agta language spoken in Casiguran' (p. 464).")
r(ALS, "ə", "o", "elsewhere", "453-454", "AltS qoddomun 'to borrow' < PPh *hedam shows 'the loss of *h, its o "
  "reflex of *e, and gemination of the consonant following *e' (p. 454 n. 12); also qolop 'cloud' < *qulep, dalmot "
  "'heavy' < *daRmet (Table 1).", as_printed="*e")
r(ALS, "ə", "o", "_C (with gemination of C)", "454", "The consonant after *e is geminated: qoddomun < *hedam "
  "(n. 12), susbo 'boil' < *sebu, tedokbum < *tidug.", as_printed="*e", status="sporadic")
r(ART, "R", "r", "elsewhere", "463", "Table 12, 'the most common reflex': *qaRtaq > arta 'man', *qeRes > ares "
  "'worm', *kaRat > arat 'bite', *takaRang > tarang 'rib'. Elsewhere in Luzon only Ilokano has r < *R (p. 464).")
r(ART, "R", "ɡ", "in loans", "464", "Table 13: *baRat > bagat 'banana', *uleR > ulag 'snake', *liqeR > lig 'neck'. "
  "g is the reflex of all the Northern Cordilleran languages; Reid takes these words to be loans from them "
  "(p. 464).", status="loan-stratum")
r(ART, "j", "d", "elsewhere", "464-465", "Table 14, the main reflex: *qujing > quding 'charcoal', *qapeju > apdu "
  "'gall', *pusej > pusəd 'navel', *palaj > palad 'palm'.")
r(ART, "j", "ɡ", "in loans", "464", "'Only two forms show g and these are both probably borrowings from Ilokano' "
  "(p. 464).", status="loan-stratum")
r(ART, "k", "∅", "elsewhere", "465-466", "Table 15, at least 20 forms: *kutu > utu 'louse', *ikan > iyan 'fish', "
  "*manuk > manu 'bird', *takaRang > tarang 'rib'. 'This is the only Philippine language which, to my knowledge, "
  "lost *k'; words with k are mostly loans from Northern Cordilleran or Ilokano (p. 466). The loss reshaped the "
  "pronouns (Tables 16-17).")
r(ART, "k", "k", "in loans", "466", "'A large proportion of these forms give evidence of having been borrowed from "
  "a Northern Cordilleran language, or from Ilokano' (p. 466).", status="loan-stratum")
r(ART, "ʔ", "∅", "elsewhere", "466", "'Glottal stop was also lost in words inherited from the proto-language, "
  "resulting in the reduction of several vowel sequences to single vowels' (p. 466).")
r(ART, "a", "u", "{b,d,ɡ}_Cu (penultimate)", "467", "Table 18: vowel harmony after the voiced stops b, d, g: 'if "
  "the final vowel of the root was u, the penultimate vowel also became u': *babuy > bubuy 'pig', *ba:lu > bulu "
  "'widow', *dapuR > dupug 'dust', dupuran 'hearth'.")

b.dec(D, "Where do Reid's (1994) Alta and Arta go, and against what are their reflexes stated?",
      "Northern Alta, Southern Alta (under a group Altan) and Arta under Proto-Northern Luzon, as in Reid's (2006) "
      "tree, whose primary branches include Altan and Arta; their reflexes, which Reid gives against Proto-"
      "Philippines and Proto-Cordilleran, are entered against PNL (Proto-Cordilleran). Loans that Reid "
      "identifies by g < *R, g < *j or k are a loan stratum. The lects inherit what Reid does not discuss "
      "(assumed-unchanged).",
      "Put the Alta languages under a Meso-Cordilleran node (Glottolog meso1254), as Reid's (1994: 452) genetic "
      "argument suggests.", "449-467")
write("reid1994-negritos", b.t, """# reid1994-negritos

Reid, Lawrence A. 1994. Unravelling the linguistic histories of Philippine Negritos. In Tom Dutton & Darrell T. Tryon (eds.), *Language contact and change in the Austronesian world*, 443-475. Berlin: Mouton de Gruyter. Generator: `tools/batch_scripts/duttontryon1994/reid.py`.

## Scope

- New group **Altan** with **Northern Alta** (nort2875) and **Southern Alta** (sout2905), and new language **Arta** (arta1239), all under Proto-Northern Luzon (decision `reid1994-negritos`).
- Alta *R > l (Table 1) and *j > d; Southern Alta *e > o with gemination; Arta *R > r, *j > d, *k > Ø, *ʔ > Ø and vowel harmony (Tables 12-15, 18); loans with g and k as a loan stratum.

## Not entered

- A Meso-Cordilleran node; the Alta conservative lexicon and pronouns (Tables 2-3); the loan lists (Tables 4-10, 19-21); Arta's unique forms (Table 11) and pronouns (Tables 16-17).
""")
