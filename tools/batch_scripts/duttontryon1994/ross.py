#!/usr/bin/env python3
"""Ross (1994), Areal phonological features in north central New Ireland.

In Dutton & Tryon (eds.), Language contact and change in the Austronesian world, 551-572. New nodes Proto-New
Ireland (PNI), Proto-Lavongai/Nalik (PLN) and Proto-Madak (PMAD), with Ross's consonant systems (1), (5) and the
correspondence sets (2) and (3) (p. 556), and the shared intervocalic rules (11), (30) as allophones (pp. 559, 563).
The user chose on 26 November 2026 to enter these nodes as stated, although Ross's (1988) intermediate
reconstructions are held back elsewhere (decision ross1994-nodes).
"""
from common import Batch, write, chapter, CONSULTED

S = "ross1994"
b = Batch(S)
b.t["sources"].append(chapter(
    S, "Ross, Malcolm", "Areal phonological features in north central New Ireland", "551-572",
    CONSULTED + "A 'phonological alliance' of the Papuan language Kuot with the Oceanic languages Lamasong and Madak "
    "(and, more weakly, Nalik and Kara), ascribed to shift by earlier Kuot speakers. §2: the languages, of three "
    "local groups descended from a Proto-New Ireland dialect network (Ross 1988: 261-262, 280, 291-292): "
    "Lavongai/Nalik, Tabar (Notsi) and Madak (Lamasong, Madak, Barok). §3.1: the consonant systems of PNI (1), PLN "
    "with its daughters (2), PNI > Patpatar and PMAD > Barok, Madak, Lamasong (3), PMAD (5), Kuot (6), p. 556-557. "
    "§3.2: the shared rules l > n / _# (7) and voiceless stop > voiced fricative between vowels (11), the Nalik "
    "and Kara variant (30). Data from the author's consultants (n. 2)."))

PNI, PLN, PMAD = "pni", "pln", "pmad"
NAL, KAR, TIA, TIG, LAV = "nali1244", "kara1486", "tian1237", "tiga1245", "tung1290"
PAT, BAR, MAD, LML, LAM = "patp1243", "baro1253", "mada1285", "lava1239", "lamu1255"
NET = ("Ross (1994: 554) leaves open whether PNI was a single proto-language or a network resynthesised from several "
       "groups that came from New Britain (Ross 1988: 261-262, 280).")
b.t["lects"] += [
    dict(id=PNI, name="Proto-New Ireland", alt_names="PNI", type="proto-language", parent_id="poc",
         region="New Ireland", notes="The ancestral dialect network of the Austronesian languages of New Ireland "
         "(Ross 1994: 554); consonant system (1), p. 556. " + NET + " Glottocode blank: Glottolog's New "
         "Ireland-Northwest Solomonic linkage (newi1242) also has the Northwest Solomonic languages "
         "(decision ross1994-nodes). Ross (1994) gives no POC > PNI correspondences."),
    dict(id=PLN, name="Proto-Lavongai/Nalik", alt_names="PLN;Proto-Lavongai-Nalik", type="proto-language",
         glottocode="tung1294", parent_id=PNI, region="Northern New Ireland, New Hanover and Tigak Islands",
         clade="Lavongai/Nalik", inherit="stated-unchanged", inherit_source_id=S, inherit_page="556",
         inherit_note="'The consonant system of Proto-Lavongai/Nalik (PLN) differs from (1) only in that PNI *mʷ has "
                      "merged with *m' (p. 556).",
         notes="Ross's Lavongai/Nalik network: Lavongai, Tigak, Tiang, Kara, Nalik (Ross 1994: 554, after Ross 1988: "
               "291-292). Glottolog's Tungak-Nalik (tung1294), the same five languages."),
    dict(id=PMAD, name="Proto-Madak", alt_names="PMAD", type="proto-language", glottocode="mada1284",
         parent_id=PNI, region="Central New Ireland", clade="Madak",
         notes="Ross's Madak chain: Lamasong, Madak, Barok (Ross 1994: 554). Consonant system (5), p. 557; its changes "
               "from PNI (4) are not shared by Patpatar or other New Ireland languages: *mʷ > *m, *p and *f deleted "
               "before *u and merged as *p elsewhere, *R lost in most environments, *l > *n word-finally (p. 557). "
               "Glottolog's Madak linkage (mada1284)."),
    dict(id=NAL, name="Nalik", type="language", glottocode="nali1244", iso639_3="nal", parent_id=PLN,
         latitude="-2.94411", longitude="151.332", region="North central New Ireland",
         notes="Consultants from Fisoa and Bol villages (Ross 1994: 553 n. 2). Coordinates from Glottolog 5.4."),
    dict(id=KAR, name="Kara", alt_names="Kara (Papua New Guinea);Lemakot", type="language", glottocode="kara1486",
         iso639_3="leu", parent_id=PLN, latitude="-2.81957", longitude="151.111", region="North central New Ireland",
         notes="West-coast and east-coast dialects differ in the intervocalic rules (Ross 1994: 564). Consultants "
               "from Lemekot, Fangalava and Panemecho villages (p. 553 n. 2). Coordinates from Glottolog 5.4."),
    dict(id=TIA, name="Tiang", type="language", glottocode="tian1237", iso639_3="tbj", parent_id=PLN,
         latitude="-2.95505", longitude="150.935", region="Djaul Island, New Ireland",
         notes="Coordinates from Glottolog 5.4."),
    dict(id=TIG, name="Tigak", type="language", glottocode="tiga1245", iso639_3="tgc", parent_id=PLN,
         latitude="-2.70951", longitude="150.893", region="Northern New Ireland and the Tigak Islands",
         notes="Coordinates from Glottolog 5.4."),
    dict(id=LAV, name="Lavongai", alt_names="Tungag;Tungak;Lavongai", type="language", glottocode="tung1290",
         iso639_3="lcm", parent_id=PLN, latitude="-2.52188", longitude="150.198", region="New Hanover",
         notes="Ross's Lavongai, Glottolog's Tungag. Coordinates from Glottolog 5.4."),
    dict(id=PAT, name="Patpatar", type="language", glottocode="patp1243", iso639_3="gfk", parent_id=PNI,
         latitude="-3.74711", longitude="152.493", region="Southern New Ireland, south of Barok",
         notes="Included in Ross's (1994: 556) table (3) for comparison with PMAD; not in the Madak chain. "
               "Coordinates from Glottolog 5.4."),
    dict(id=BAR, name="Barok", type="language", glottocode="baro1253", iso639_3="bjk", parent_id=PMAD,
         latitude="-3.47672", longitude="152.193", region="Central New Ireland",
         notes="Coordinates from Glottolog 5.4."),
    dict(id=MAD, name="Madak", type="language", glottocode="mada1285", iso639_3="mmx", parent_id=PMAD,
         latitude="-3.34342", longitude="151.967", region="Lelet Plateau, central New Ireland",
         notes="Consultants from Malom, Lasiki and Kaluan villages (Ross 1994: 553 n. 2); analysis of Lee & Lee "
               "(1976, 1978). Coordinates from Glottolog 5.4."),
    dict(id=LML, name="Lavatbura-Lamusong", type="language", glottocode="lava1239", iso639_3="lbv", parent_id=PMAD,
         representative=LAM, latitude="-3.21903", longitude="151.728", region="Central New Ireland",
         notes="Glottolog's language for Ross's Lamasong, which is its dialect Lamusong (lamu1255)."),
    dict(id=LAM, name="Lamasong", alt_names="Lamusong", type="dialect", glottocode="lamu1255", parent_id=PMAD,
         language_id=LML, latitude="-3.21903", longitude="151.728", region="Lamasong village, central New Ireland",
         notes="Consultant from Lamasong village (Ross 1994: 553 n. 2). Glottolog's Lamusong, a dialect of "
               "Lavatbura-Lamusong."),
]

D = "ross1994-nodes"
CS = "Correspondence set (2), p. 556: "
CS3 = "Correspondence set (3), p. 556: "


def r(lect, par, ch, env="elsewhere", page="556", notes="", status="regular", **k):
    b.corr(lect, par, ch, env, page, notes, status=status, derivation="", decision=D, **k)


# PNI inventory (1)
for ipa, place, manner, voicing in (("p", "bilabial", "plosive", "voiceless"), ("t", "alveolar", "plosive", "voiceless"),
                                    ("k", "velar", "plosive", "voiceless"), ("b", "bilabial", "plosive", "voiced"),
                                    ("d", "alveolar", "plosive", "voiced"), ("ɡ", "velar", "plosive", "voiced"),
                                    ("f", "", "fricative", "voiceless"), ("s", "alveolar", "fricative", "voiceless"),
                                    ("m", "bilabial", "nasal", "voiced"), ("n", "alveolar", "nasal", "voiced"),
                                    ("ŋ", "velar", "nasal", "voiced"), ("mʷ", "bilabial", "nasal", "voiced"),
                                    ("l", "alveolar", "lateral-approximant", "voiced"),
                                    ("R", "uvular", "trill", "voiced"),
                                    ("w", "labial-velar", "approximant", "voiced"),
                                    ("y", "palatal", "approximant", "voiced")):
    note = ("'Phonetically a uvular trill, reflected variously in daughter-languages as /r/, /y/, /Ø/ or a velar' "
            "(p. 556).") if ipa == "R" else ("Labial fricative; the place is not given (bilabial [ɸ] in Nalik, "
                                             "p. 563).") if ipa == "f" else ""
    b.ph(PNI, ipa, "C", place, manner, voicing, sym="g" if ipa == "ɡ" else "", page="556", notes=note)
for lect, pg in ((PNI, "556"), (PLN, "556"), (PMAD, "557")):
    b.t["notation_map"].append(dict(lect_id=lect, phoneme="", system="canonical", symbol="", source_id=S, page=pg,
                                    notes="Ross's symbols, with ɡ for g."))
b.t["sources"] += [
    dict(id="leelee1976", author="Lee, Robert; Lee, Carolyn", year="1976",
         title="A tentative phonemic statement of Mandak", kind="grammar", pub_type="other", place="Ukarumpa",
         publisher="Summer Institute of Linguistics",
         notes="Unpublished manuscript. Bibliographic details from the reference list of Ross (1994: 569); not "
               "consulted directly. Its analysis of Madak intervocalic [β, r, ɣ] as allophones of /p, t, k/ is "
               "read in Ross (1994: 559)."),
    dict(id="leelee1978", author="Lee, Robert; Lee, Carolyn", year="1978", title="Mandak grammar essentials",
         kind="grammar", pub_type="other", place="Ukarumpa", publisher="Summer Institute of Linguistics",
         notes="Unpublished manuscript. Bibliographic details from the reference list of Ross (1994: 569); not "
               "consulted directly."),
]
# PLN inventory: PNI's minus *mʷ (stated, p. 556)
for ipa, place, manner, voicing in (("p", "bilabial", "plosive", "voiceless"), ("t", "alveolar", "plosive", "voiceless"),
                                    ("k", "velar", "plosive", "voiceless"), ("b", "bilabial", "plosive", "voiced"),
                                    ("d", "alveolar", "plosive", "voiced"), ("ɡ", "velar", "plosive", "voiced"),
                                    ("f", "", "fricative", "voiceless"), ("s", "alveolar", "fricative", "voiceless"),
                                    ("m", "bilabial", "nasal", "voiced"), ("n", "alveolar", "nasal", "voiced"),
                                    ("ŋ", "velar", "nasal", "voiced"), ("l", "alveolar", "lateral-approximant", "voiced"),
                                    ("R", "uvular", "trill", "voiced"), ("w", "labial-velar", "approximant", "voiced"),
                                    ("y", "palatal", "approximant", "voiced")):
    b.ph(PLN, ipa, "C", place, manner, voicing, sym="g" if ipa == "ɡ" else "", page="556",
         notes="PNI's system (1) less *mʷ (p. 556)." if ipa == "m" else "")
# PLN: only *mʷ > *m (the rest by stated-unchanged)
r(PLN, "mʷ", "m", notes="'The consonant system of Proto-Lavongai/Nalik (PLN) differs from (1) only in that PNI *mʷ "
  "has merged with *m' (p. 556).")
# PMAD (3), (4)
P3 = CS3 + "PMAD row. "
r(PMAD, "p", "∅", "_u", notes=P3 + "(4a) 'PNI *p and *f were deleted before *u and remained as PMAD *p elsewhere' (p. 557).")
r(PMAD, "f", "∅", "_u", notes=P3 + "(4a).")
r(PMAD, "f", "p", notes=P3 + "(4a): the merger of PNI *p and *f, which Ross tentatively links to the absence of /f/ "
  "in an earlier stage of Kuot (p. 557).")
r(PMAD, "k", "∅", "conditions unknown", notes=P3 + "PMAD *k, Ø, as in Patpatar and the three daughters; no "
  "condition given.")
r(PMAD, "l", "n", "_#", notes=P3 + "(4c) 'PNI *l became *n word-finally', shared with Kuot's synchronic rule (7): "
  "*tolu > PMAD *-tun 'three', *sagafulu > *sanaun 'ten' (pp. 557-558).")
r(PMAD, "R", "∅", "elsewhere", notes=P3 + "(4b) 'PNI *R disappeared in most environments'; possibly connected with "
  "the absence of /r/ in Kuot (p. 557).")
r(PMAD, "R", "r", "V_V", notes=P3 + "'*Ø; r,Ø/V_V': r or Ø between vowels; PMAD (5) has a marginal (r) (p. 557).")
r(PMAD, "R", "∅", "V_V", notes=P3 + "'*Ø; r,Ø/V_V'.")
for ph in ("t", "b", "d", "ɡ", "s", "m", "n", "ŋ", "w", "y"):
    r(PMAD, ph, ph, notes=P3 + "Unchanged in PMAD.", as_printed="*" + ph.replace("ɡ", "g"))
r(PMAD, "p", "p", notes=P3 + "'*p; Ø/_*u'.", as_printed="*p; Ø/_*u")
r(PMAD, "k", "k", notes=P3 + "'*k, Ø'.", as_printed="*k, Ø")
r(PMAD, "l", "l", notes=P3 + "'*l; n/_#'.", as_printed="*l; n/_#")
r(PMAD, "mʷ", "m", page="557", notes="'As well as the change which also took place in Proto-Lavongai/Nalik (i.e. "
  "PNI *mʷ > *m)' (p. 557).")
for ipa, place, manner, voicing, st in (("p", "bilabial", "plosive", "voiceless", ""),
                                        ("t", "alveolar", "plosive", "voiceless", ""),
                                        ("k", "velar", "plosive", "voiceless", ""),
                                        ("b", "bilabial", "plosive", "voiced", ""),
                                        ("d", "alveolar", "plosive", "voiced", ""),
                                        ("ɡ", "velar", "plosive", "voiced", ""),
                                        ("s", "alveolar", "fricative", "voiceless", ""),
                                        ("m", "bilabial", "nasal", "voiced", ""),
                                        ("n", "alveolar", "nasal", "voiced", ""),
                                        ("ŋ", "velar", "nasal", "voiced", ""),
                                        ("l", "alveolar", "lateral-approximant", "voiced", ""),
                                        ("r", "alveolar", "trill", "voiced", "marginal"),
                                        ("w", "labial-velar", "approximant", "voiced", ""),
                                        ("y", "palatal", "approximant", "voiced", "")):
    b.ph(PMAD, ipa, "C", place, manner, voicing, sym="g" if ipa == "ɡ" else "", page="557", status=st,
         notes="In parentheses in (5) (p. 557)." if st else "")

# PLN daughters (2): one cell per PLN phoneme
PLNPH = ["p", "t", "k", "b", "d", "ɡ", "f", "s", "m", "n", "ŋ", "l", "R", "w", "y"]
T2 = {
    NAL: ["w; p/_o", "t", "k", "b", "d", "ɡ", "ɸ", "s", "m", "n", "ŋ", "l", "r", "∅", "j"],
    KAR: ["p", "t", "k", "b", "d", "ɡ", "ɸ", "s", "m", "n", "ŋ", "l", "j", "w", "j"],
    TIA: ["p", "t", "k", "b; w/V_V", "r", "ɡ", "∅", "s", "m", "n", "ŋ", "l", "j", "w", "j"],
    TIG: ["p", "t", "k", "b; w/V_V", "r", "ɡ", "∅", "s", "m", "n", "ŋ", "l", "ɡ", "w", "j"],
    LAV: ["p", "t", "k", "v", "r", "ɡ", "∅", "s", "m", "n", "ŋ", "l", "ŋ", "w", "j"],
}
PRINT = {"ɸ": "f", "j": "y", "ɡ": "g"}
for lect, cells in T2.items():
    for par, cell in zip(PLNPH, cells):
        if ";" in cell:
            main, cond = [x.strip() for x in cell.split(";")]
            ch, env = cond.split("/")
            r(lect, par, main, "elsewhere", notes=CS + f"'{cell}'.", as_printed=cell)
            r(lect, par, ch, env, notes=CS + f"'{cell}'.", as_printed=cell)
        else:
            note = CS
            if cell == "ɸ":
                note += "f, [ɸ] in Nalik (p. 563); Kara taken to be the same."
            r(lect, par, cell, notes=note, as_printed=PRINT.get(cell, cell))

# PNI > Patpatar and PMAD > daughters (3)
PNIPH = ["p", "t", "k", "b", "d", "ɡ", "f", "s", "m", "n", "ŋ", "l", "R", "w", "y"]
PATC = ["p", "t", "k, ∅", "b", "d", "ɡ", "h", "s", "m", "n", "ŋ", "l", "r", "u", "i"]
for par, cell in zip(PNIPH, PATC):
    if cell == "k, ∅":
        r(PAT, par, "k", notes=CS3 + "'k, Ø'.", as_printed=cell)
        r(PAT, par, "∅", "conditions unknown", notes=CS3 + "'k, Ø'.", as_printed=cell)
    elif cell in ("u", "i"):
        r(PAT, par, {"u": "w", "i": "j"}[cell], notes=CS3 + f"printed {cell}, taken to be the glide written as a "
          "vowel letter.", as_printed=cell)
    else:
        r(PAT, par, cell, notes=CS3 + "Patpatar row.", as_printed=PRINT.get(cell, cell))
PMADPH = ["p", "t", "k", "b", "d", "ɡ", "s", "m", "n", "ŋ", "l", "R", "w", "y"]
DTRS = {
    BAR: ["p; ∅/_u", "t", "k, ∅", "b", "d", "ɡ", "s", "m", "n", "ŋ", "l; n/_#", "∅; r,∅/V_V", "∅", "j"],
    MAD: ["p; ∅/_u", "t", "k, ∅", "b", "d", "ɡ", "s", "m", "n", "ŋ", "l; n/_#", "∅", "β", "ɣ"],
    LAM: ["p; ∅/_u", "t", "k, ∅", "b", "d", "ɡ", "s", "m", "n", "ŋ", "l; n/_#", "∅", "β", "∅"],
}
for lect, cells in DTRS.items():
    for par, cell in zip(PMADPH, cells):
        pre = CS3 + f"'{cell}'. "
        if par == "p":
            r(lect, "p", "p", notes=pre + "Stated against PNI *p (and *f); PMAD had already lost *p before *u and the "
              "daughters repeat the table's condition.", as_printed=cell)
        elif par == "k":
            r(lect, "k", "k", notes=pre + "As in PMAD *k, Ø.", as_printed=cell)
            r(lect, "k", "∅", "conditions unknown", notes=pre + "As in PMAD *k, Ø.", as_printed=cell)
        elif par == "l":
            r(lect, "l", "l", notes=pre + "PMAD *l; n/_#: the word-final n is PMAD's.", as_printed=cell)
        elif par == "R":
            if lect == BAR:
                r(lect, "r", "r", "V_V", notes=pre + "Barok repeats PMAD's 'Ø; r,Ø/V_V': PMAD's intervocalic *r stays.",
                  as_printed=cell)
            else:
                r(lect, "r", "∅", "V_V", notes=pre + "Madak and Lamasong have Ø for PNI *R everywhere, so PMAD's "
                  "intervocalic *r is lost.", as_printed=cell)
        elif cell in ("β",):
            r(lect, par, "β", notes=pre + "Printed v; Ross gives v = [β] for Madak (p. 559).", as_printed="v")
        elif cell == "ɣ":
            r(lect, par, "ɣ", notes=pre + "Printed γ.", as_printed="γ")
        else:
            r(lect, par, cell, notes=pre.strip(), as_printed=PRINT.get(cell, cell))

# Allophones: (11) Kuot-Madak alliance, (30) Nalik/Kara
for lect in (MAD, LAM, BAR):
    for ph, al in (("p", "β"), ("t", "ɾ"), ("k", "ɣ")):
        b.allo(lect, ph, al, "V_V (single consonant, also across morpheme boundaries)", "559-561",
               "Rule (11): 'a voiceless stop becomes a corresponding voiced fricative intervocalically', shared "
               "with Kuot; Ross writes v [β], r, γ. Lee & Lee (1976) treat [β, r, ɣ] as allophones of /p, t, k/ and "
               "intervocalic [p, t, k] as /pp, tt, kk/. Examples are from Madak; 'parallel Lamasong and Barok "
               "examples could be cited' (p. 559).")
for lect in (NAL, KAR):
    rows = (("ɸ", "β"), ("t", "ɾ"), ("k", "ɣ"), ("s", "z")) if lect == NAL else (("k", "ɣ"),)
    for ph, al in rows:
        b.allo(lect, ph, al, "V_V" if lect == NAL else "V_V (both dialects)", "563-564",
               "Rule (30) in Nalik: f > v, t > r, k > γ, s > z between vowels, also across word and morpheme "
               "boundaries (f = [ɸ], v = [β]); [p t k] occur between vowels only in careful citation forms. "
               "Intervocalic [r] < /t/ is indistinguishable from /r/ < PNI *R (pp. 563-564).")
    if lect == KAR:
        for ph, al in (("ɸ", "β"), ("t", "ɾ"), ("s", "z")):
            b.allo(lect, ph, al, "V_V (west-coast dialect)", "564", "'The operation of the rule in (30) in "
                   "west-coast Kara is similar to that in Nalik. The east-coast dialect of Kara, however, has only "
                   "(30c)' (k > ɣ).")

b.dec(D, "How are Ross's (1994) New Ireland reconstructions entered?",
      "As three proto-language nodes, the user's choice of 26 November 2026: Proto-New Ireland under POC "
      "(Glottocode blank, its inventory (1) only; no POC > PNI rows, which the chapter does not give), "
      "Proto-Lavongai/Nalik (tung1294) and Proto-Madak (mada1284) under PNI, with Nalik, Kara, Tiang, Tigak and "
      "Lavongai under PLN, Barok, Madak and Lamasong under PMAD, and Patpatar directly under PNI, as in tables "
      "(2) and (3). Symbols: y = j, Nalik and Kara f = ɸ, Madak v = β, γ = ɣ. Rule (11) and rule (30) are "
      "allophones. Kuot (Papuan) and Notsi (Tabar) are not entered.",
      "Hold the nodes back and compose the daughters onto POC through Ross (1988), as the user chose for "
      "Ross (1988) on 24 November 2026.", "554-564")
write("ross1994-newireland", b.t, """# ross1994-newireland

Ross, Malcolm. 1994. Areal phonological features in north central New Ireland. In Tom Dutton & Darrell T. Tryon (eds.), *Language contact and change in the Austronesian world*, 551-572. Berlin: Mouton de Gruyter. Generator: `tools/batch_scripts/duttontryon1994/ross.py`.

## Scope

- New nodes **Proto-New Ireland** (`pni`, under POC, inventory (1)), **Proto-Lavongai/Nalik** (`pln`, tung1294) and **Proto-Madak** (`pmad`, mada1284, inventory (5)), the user's choice of 26 November 2026 (decision `ross1994-nodes`).
- New languages Nalik, Kara, Tiang, Tigak, Lavongai (Tungag) under PLN; Barok, Madak and Lavatbura-Lamusong with its dialect Lamasong under PMAD; Patpatar under PNI; their consonant reflexes from tables (2) and (3), p. 556.
- Allophones: rule (11) in Madak, Lamasong, Barok; rule (30) in Nalik and Kara (pp. 559-564).

## Not entered

- POC > PNI (not in this chapter; see Ross 1988 Tables 28-37), vowels, Kuot (Papuan, (6)), Notsi, the Tabar chain, the agglutination and vowel-reduction rules (§3.2).
""")
