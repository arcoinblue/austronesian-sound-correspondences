#!/usr/bin/env python3
"""Malagasy and Southeast Barito: four batches from the papers of 25 November 2026.

- adelaar2012-malagasy: Adelaar (2012), Malagasy phonological history and Bantu influence, Oceanic Linguistics 51:
  123-159. New nodes Proto-Southeast Barito (pseb, under Proto-Barito) and Proto-Malagasy (pmlg), the Malagasy lects,
  and the changes of Tables 1-6 and §§3-6 (PSEB1-9, PMLG1-4, MLG1-4, MRN1-4).
- adelaar2013-malagasy: Adelaar (2013), Malagasy dialect divisions, Oceanic Linguistics 52: 457-480. The *li, *ti
  and final *t reflexes of Tables 1-6, *y of Table 7, final *i/*e of Table 8 (§4.1), the classification decision.
- adelaar1991-malagasy: Adelaar (1991), New ideas on the early history of Malagasy. The source, Mahdi (1988), and
  Mahdi's chain of Table 1 (p. 9), PAN > Proto-Barito > Proto-East Barito > PSEB > Proto-Malagasy > Merina, entered
  with source_id mahdi1988, read via Adelaar (1991: 9).
- adelaar1995-malagasy: Adelaar (1995), Asian roots of the Malagasy. The source, Hudson (1967), and the PSEB schwa
  (p. 340).
All read directly on 25 November 2026 (PDFs in Downloads; the 1991 table read from the page image).
"""
from common import Batch, write

PB, PSEB, PMLG = "pbarito", "pseb", "pmlg"
MRN, PLAT, SAK, NSK, BARA, TDR, TNK, TSM, SBM, TNS, OSE = (
    "meri1243", "plat1254", "saka1291", "north-sakalava", "bara1369", "tand1256", "anta1255", "tsim1257",
    "sout2920", "tano1246", "old-southeast-malagasy")

# ====================================================================== Adelaar 2012
S = "adelaar2012"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Adelaar, Alexander", year="2012", title="Malagasy phonological history and Bantu influence",
    kind="comparative", pub_type="article", container_title="Oceanic Linguistics", volume="51", issue="1",
    pages="123-159", url_or_doi="https://doi.org/10.1353/ol.2012.0003",
    notes="Consulted directly on 25 November 2026 (Project MUSE PDF in Downloads). A critique of Wolff's (2010) "
          "treatment of Malagasy. §2.3 states the changes in three stages: Proto-South East Barito (PSEB1-9, Table 3, "
          "p. 131, premigratory, shared with the SEB languages of Kalimantan), Proto-Malagasy (PMLG1-4, Table 4, p. "
          "135, postmigratory) and the dialects (MLG1-4, Table 5, p. 136; Merina MRN1-4, Table 6, p. 138); §3 the "
          "spirantization of stops and semivowels, §4 the retroflex affricate tr, §5 the reduction of nasal + stop "
          "clusters, §6 PAN *s; §7 Bantu (Sabaki, Comorian) contact. Data sources in the Appendix (pp. 155-156): "
          "Maanyan from Dahl (1951), Merina from Webber (1853), Richardson (1885) and Abinal & Malzac, South Sakalava "
          "from Gueunier (n.d.), North Sakalava from Thomas-Fattier (1982), Bara from Elli (1988), South "
          "Betsimisaraka from Ruud (1955), Old South Betsimisaraka from Flacourt (1658), Old Taimoro (Sorabe script) "
          "from Ferrand (1904). Malagasy written in its orthography with o as u, ŋ for the velar nasal, paragogic "
          "vowels with a breve and stress marked; PAN and PMP in Blust's ACD notation with ə for *e."))

# ---------------------------------------------------------------- lects
LN = dict
b.t["lects"] += [
    LN(id=PSEB, name="Proto-Southeast Barito", alt_names="PSEB;Proto-South East Barito;Proto-South-East Barito",
       type="proto-language", glottocode="sout2919", parent_id=PB, clade="Southeast Barito",
       region="Central and South Kalimantan, east of the Barito river; Madagascar",
       inherit="assumed-unchanged",
       inherit_note="Phonemes for which no source states a change (p, t, k, m, n, ŋ, ɲ, l, a, i, u, w) are carried "
                    "down from Proto-Barito unchanged.",
       orthography_note="Adelaar (2012) writes PSEB e for the mid front vowel that continues both the PMP schwa and "
                        "final *a (*katen 'itchy' < *katəl, *rue 'two' < *duSa); Adelaar (1995: 340), after Hudson "
                        "(1967), calls it 'a mid-front vowel'. Mahdi (1988) writes ɛ in *-ɛy.",
       notes="The language ancestral to Malagasy and to the Southeast Barito languages of Kalimantan (Ma'anyan, "
             "Samihim, Paku, Dusun Witu and others: Hudson 1967; Dahl 1951, 1977), 'spoken along the eastern shores "
             "of the Barito River in Central Kalimantan Province, and in a few disconnected areas in South Kalimantan' "
             "(Adelaar 2012: 124 n. 4). Its changes are premigratory and attested in the SEB languages of Kalimantan "
             "(Table 3, p. 131). Adelaar (2012: 132 n. 12) finds Ma'anyan and Samihim mutually understandable "
             "dialects 'more closely related to MLG than other forms of SEB'; Mahdi (1988) puts Malagasy as a "
             "separate branch at equal distance from the other SEB languages (Adelaar 1991: 8). Adelaar (2013: "
             "467) places the split of Proto-East Barito into PSEB and Proto-Central East Barito before the *li > "
             "di and *ti > tsi tendencies. Ma'anyan and Dusun Witu stay under Proto-Barito with Smith's (2017a) rows "
             "(decision adelaar2012-pseb). PAN etyma are restated against PMP (Proto-Barito inherits the PMP "
             "inventory)."),
    LN(id=PMLG, name="Proto-Malagasy", alt_names="PMLG", type="proto-language", glottocode="mala1537",
       parent_id=PSEB, clade="Malagasy", region="Madagascar (and the Comoros, Mayotte)",
       inherit="assumed-unchanged",
       inherit_note="Phonemes for which no source states a change are carried down from PSEB unchanged.",
       orthography_note="Adelaar's (2012, 2013) PMLG forms are not consistent in the stops and glides: *fitu, *afu, "
                        "*lelef-an and *hali, *hatuk beside *katen, *wulan, *waye (2012: 127, 130, 135-136). The "
                        "rows enter *p > f and *k > h at this stage, *w > v in the dialects.",
       notes="'Any stage after SEB speakers had sailed to East Africa' (Adelaar 2012: 135 n. 27); the changes of "
             "Table 4 (p. 135) are postmigratory. All three final nasals *-m, *-n, *-ŋ were still distinct, as "
             "Flacourt's (1658) Old South Betsimisaraka shows (p. 137). Adelaar (2012: §§3-5, 7) ascribes the "
             "spirantization of stops, the fricativization of the semivowels, the paragogic vowels, the affricate "
             "tr and the reduction of nasal + stop clusters to contact with Sabaki (Comorian) and Makhuwa after the "
             "migration; the settlers reached Madagascar from the East African coast as a mixed Austronesian-Bantu "
             "population (pp. 145-146; Adelaar 2013: 477). Dialect classification is left open (decision "
             "adelaar2013-classification)."),
]

DIALECTS = [
    LN(id=PLAT, name="Plateau Malagasy", alt_names="Standard Malagasy;Malagasy", type="language",
       glottocode="plat1254", iso639_3="plt", parent_id=PMLG, latitude="-19.5907", longitude="47.1211",
       region="Central highlands of Madagascar", representative=MRN,
       notes="Glottolog's language for Merina, Betsileo, Antaimoro and other central varieties; entered as the node "
             "of Merina, the dialect the sources cite."),
    LN(id=MRN, name="Merina", alt_names="MRN;Standard Malagasy", type="dialect", glottocode="meri1243",
       parent_id=PMLG, language_id=PLAT, latitude="-19.5907", longitude="47.1211",
       region="Imerina, the central highlands around Antananarivo", inherit="assumed-unchanged",
       orthography_note="IPA. Adelaar writes the orthography with o as u: tr = ʈ͡ʂ, ts = t͡s, z = z, y (final) = i, "
                        "and marks the paragogic (whispered) vowel with a breve (-tră, -kă, -nă). Final -tr, -k and "
                        "-n are entered as the consonant; the paragogic vowel is in the notes.",
       notes="The dialect on which Standard Malagasy is based; 'not only the dominant dialect but ... also one of the "
             "most innovative of all Malagasy dialects' (Adelaar 2013: 473). Historical final consonants merged as "
             "-tră, -kă, -nă or were lost; before a vowel-initial suffix other consonants can reappear (-tră/-r-, "
             "-t-, -f-; -kă/-f-, -h-; -nă/-m-), by the rules of Mahdi (1988: 241-262) (Adelaar 2012: 124-125). "
             "Stress is contrastive on any of the last three syllables (MLG3, p. 137). Data from Webber (1853), "
             "Richardson (1885) and Abinal & Malzac (Adelaar 2012: 155)."),
    LN(id=SAK, name="Sakalava", alt_names="South Sakalava;SSK;West Malagasy Sakalava", type="language",
       glottocode="saka1291", iso639_3="skg", parent_id=PMLG, latitude="-20.28", longitude="44.32",
       region="West coast of Madagascar around Morondava", inherit="assumed-unchanged",
       orthography_note="IPA; the paragogic vowel is -ĕ (Adelaar 2012: 128 n. 8).",
       notes="Adelaar (2012) calls it South Sakalava (SSK), from Gueunier (n.d.); Adelaar (2013: 461) uses 'Sakalava' "
             "for the dialect of Morondava and thereabout, a western dialect, and keeps South Sakalava and North "
             "Sakalava apart: 'the northern and southern dialects appear to be less akin to one another than to "
             "other nearby dialects' (2012: 155). It has lost all final nasals but keeps *-t and *-k (2012: 128); it "
             "still distinguishes final *-i and *-e (2012: 136; 2013: 474, Table 8). Sakalava and Tandroy have "
             "productive ni- and <in> marking past tense (2013: 476)."),
    LN(id=NSK, name="North Sakalava", alt_names="NSK;Northern Sakalava", type="language",
       parent_id=PMLG, region="North-west Madagascar, north of Majunga", inherit="assumed-unchanged",
       notes="Adelaar's NSK, from Thomas-Fattier (1982) (2012: 155). A northern dialect, 'more similar to Tsimihety "
             "and Tankarana' than to Sakalava of Morondava (2013: 461). Glottolog 5.4 has no languoid for it "
             "(decision adelaar2012-dialects). The paragoge echoes the vowel of the preceding syllable, and original "
             "final nasals are often not followed by a vowel (2012: 130)."),
    LN(id=BARA, name="Bara", alt_names="Bara Malagasy", type="language", glottocode="bara1369", iso639_3="bhr",
       parent_id=PMLG, latitude="-23.9716", longitude="45.5937", region="South-central Madagascar",
       inherit="assumed-unchanged",
       notes="From Elli (1988) (Adelaar 2012: 155). The paragogic vowel is -ĭ (2012: 130). Western varieties of Bara "
             "belong to the western dialects, eastern Bara to the central ones (2013: 458, 461)."),
    LN(id=TDR, name="Tandroy", alt_names="Antandroy;Tandroy Malagasy", type="language", glottocode="tand1256",
       iso639_3="tdx", parent_id=PMLG, latitude="-24.80155", longitude="45.9", region="Far south of Madagascar",
       inherit="assumed-unchanged",
       notes="From Rajaonarimanana & Fee (1996) (Adelaar 2012: 155-156). A southwestern dialect (2013: 458). Has no "
             "locative voice but an instrumental and an applicative voice (2013: 476)."),
    LN(id=TNK, name="Tankarana", alt_names="Antankarana;Antankarana Malagasy", type="language",
       glottocode="anta1255", iso639_3="xmv", parent_id=PMLG, latitude="-13.2164", longitude="49.2402",
       region="Northern tip of Madagascar", inherit="assumed-unchanged",
       notes="Adelaar (2013: 463-464, Table 3) compares three subdialects (Ambiloha, Antalaha, Vohemar) from Serva & "
             "Petroni's (2011) lists. A northern dialect; Vérin, Kottak & Gorlin (1969) make it a primary branch."),
    LN(id=TSM, name="Tsimihety", alt_names="Tsimihety Malagasy", type="language", glottocode="tsim1257",
       iso639_3="xmw", parent_id=PMLG, latitude="-15.4294", longitude="48.8102",
       region="North-central Madagascar", inherit="assumed-unchanged",
       notes="Data from Faridanona (1977) and Hideo Fukazawa (Adelaar 2013: 464-465, Table 4). A northern dialect; "
             "Vérin, Kottak & Gorlin (1969) make it a primary branch."),
    LN(id=SBM, name="South Betsimisaraka", alt_names="SBM;Southern Betsimisaraka", type="language",
       glottocode="sout2920", iso639_3="bzc", parent_id=PMLG, latitude="-22.8", longitude="47.82",
       region="Central and southern east coast of Madagascar", inherit="assumed-unchanged",
       notes="From Ruud (1955) (Adelaar 2012: 155; 2013 cites pages as R47 etc.). 'Betsimisaraka' covers several "
             "subdialects along a long stretch of the east coast and 'needs to be defined more clearly' (2013: 467, "
             "477). Ruud's final r 'must be a retroflex affricate' (2013: 463, Table 2 note). Adelaar (2012) also "
             "cites Flacourt's (1658) dictionary as Old South Betsimisaraka; in 2013 (p. 466) he treats Flacourt as "
             "a Tanosy source (decision adelaar2012-dialects)."),
    LN(id=TNS, name="Tanosy", alt_names="Antanosy;Tanosy Malagasy", type="language", glottocode="tano1246",
       iso639_3="txy", parent_id=PMLG, latitude="-24.9186", longitude="47.1357",
       region="South-east coast of Madagascar around Tolanaro (Fort-Dauphin)", inherit="assumed-unchanged",
       notes="An eastern dialect (Adelaar 2013: 458). Dez (1963) has Tanosy as the only dialect with *ti > tsi but "
             "*li kept; current Tanosy has many di and tsi forms from standard Malagasy (2013: 465-466 and n. 6). "
             "Flacourt's (1658) dictionary was compiled around Fort-Dauphin (2013: 466)."),
    LN(id=OSE, name="Old South East Malagasy", alt_names="Old Taimoro;Sorabe Malagasy", type="language",
       parent_id=PMLG, region="South-east coast of Madagascar", inherit="assumed-unchanged",
       notes="The language of the oldest Malagasy literature, in Sorabe (Arabic) script, 'an old form of coastal "
             "South East Malagasy'; 'often incorrectly assumed to be an old form of Taimoro' (Adelaar 2013: 458 n. "
             "2), as Adelaar (2012) still calls it (Old Taimoro). Data from a sixteenth-century text in Ferrand "
             "(1904), cited with page numbers (F114 etc.). Sorabe writes tr as a geminated r sign (2012: 141 n. 38); "
             "vowels are diacritics, so a written waw or yod marks a semivowel or a long vowel (2012: 139 n. 34). "
             "An attested historical variety, entered as a language with no Glottocode (decision adelaar2012-dialects)."),
]
b.t["lects"] += DIALECTS
b.t["notation_map"] += [
    dict(lect_id=PSEB, phoneme="", system="canonical", symbol="", source_id=S, page="131",
         notes="Symbols as Adelaar (2012) writes PSEB, with ŋ for the velar nasal; e is the mid front vowel. Mahdi's "
               "(1988) ɛ and ʔ (Adelaar 1991: 9) are kept."),
    dict(lect_id=PMLG, phoneme="", system="canonical", symbol="", source_id=S, page="135",
         notes="Symbols as Adelaar (2012) writes PMLG; e is the mid front vowel. Mahdi's (1988) *-C (a preglottalised or "
               "implosive voiceless palatal stop, Adelaar 1991: 9) is given in the notes of the Merina -tr row."),
]

# ---------------------------------------------------------------- PSEB (Table 3, p. 131; §§2.3, 3)
D = "adelaar2012-pseb"
P = lambda *a, **k: b.corr(PSEB, *a, decision=D, **k)
P("l", "n", "_#", "131-132", as_printed="PSEB2. PAN *-l, *-ł, *-n > PSEB *-n",
  notes="PMP *katəl 'itchy' > PSEB *katen > MNY katen, MRN hàtină; PMP *təbəl > *tewen (ex. 3). PAN *ł is the "
        "ACD's *N, PMP *n. Some words lost *-l altogether: probably Malay loans borrowed after *-l > *-n "
        "(*paŋkal > faka, ex. 4).")
P("R", "y", "_#", "131-132", as_printed="PSEB3. PAN *-R > PSEB *-y",
  notes="PMP *niuR > PSEB *niuy > MNY niui; *saluR > *haluy; *dəŋəR > *reŋey > MNY reŋei (ex. 5).")
P("R", "y", "#_, V_V", "131", conditioning="unknown", as_printed="(in nonfinal positions, *R > *y, Ø)",
  notes="PAN *uRaC > PSEB *uyat 'vein' (ex. 6), *Ratus > *yatuh. Mahdi (1988: 161) has nonfinal *R > Ø as "
        "regular and y as a borrowing from other Barito languages (Adelaar 2012: 133 n. 14). MNY uwat and MRN "
        "ùzatră differ in *R, so both languages 'already had separate histories in premigratory times' (p. 133).")
P("R", "∅", "#_, V_V", "131", conditioning="unknown", as_printed="(in nonfinal positions, *R > *y, Ø)",
  notes="PAN *baqəRuh 'new' > PSEB *wau (ex. 11).")
for ph, ex in (("d", "PMP *qatəd > PSEB *atet; *pənəd > *penet"), ("j", "PMP *pusəj > PSEB *puhet; *laləj > *lalet")):
    P(ph, "t", "_#", "131-133", as_printed="PSEB4. PAN *-d, *-j, *-t, *-C > PSEB *-t", notes=ex + " (ex. 6).")
P("r", "t", "_#", "131, 133", status="loan-stratum", as_printed="PSEB5. The final *-r in loanwords > PSEB *-t",
  notes="Malay bayar > MNY wayat; butir > MNY butit; OJ həlar > MNY elat, MRN èlatră (ex. 7). 'Not the default "
        "correspondence': MNY keeps r in many other loans; in Malagasy the merger persisted (p. 133).")
b.t["correspondences"][-1]["stratum"] = "Malay and Javanese loans"
P("b", "p", "_#", "131, 133", as_printed="PSEB6. PAN *-b, *-p > PSEB *-p",
  notes="'(some PAN *-b and *-p possibly already became *-t)'. PMP *uŋkab > PSEB *ukap; *ləbləb > *lelep (ex. 8); "
        "MNY tabit 'doctor' < Malay tabip and k/alat 'steal' < *alap suggest the merger with *-t was under way "
        "before the migration (ex. 9, p. 134).")
P("ɡ", "k", "_#", "131, 134", as_printed="PSEB7. PAN *-g, *-k > PSEB *-k",
  notes="PMP *kuḍug > MRN kùtrukă (very doubtful, n. 19); etyma in *-g are 'extremely rare' (n. 18).")
for ph, ex in (("h", "PAN *baRah > PSEB *waye; *kalih > *kali; PAN *S (PMP *h): *CaliS > *tali"),
               ("q", "PAN *ludaq > PSEB *rura; *bajaq > *wara")):
    P(ph, "∅", "elsewhere", "131, 134", as_printed="PSEB8. PAN *S, *q, *h > PSEB Ø",
      notes=ex + " (ex. 11). MNY waraʔ: final glottal stop accretion is not historical (n. 20).")
P("s", "h", "elsewhere", "131, 134-135, 142-144", as_printed="PSEB9. PAN *s > PSEB *h in all positions",
  notes="'(with exceptions: numerals and *sVsVC)': MLG, MNY ìsa 'one', MRN sìvi, MNY suei 'nine'. *sapaw > "
        "*hapaw, *sida > *hire, *qasəŋ > *aheŋ, *Ratus > *yatuh (ex. 12). MNY has lenition (h), Malagasy loss "
        "(PMLG2). Loanwords tend to keep s; MNY hehep < *səpsəp shows the change also ran in each language "
        "separately (p. 144). Dahl (1951: 42) had shown most Malagasy s for *s to be borrowed (§6).")
P("s", "s", "elsewhere", "131, 135, 143-144", status="sporadic", conditioning="lexical",
  as_printed="(with exceptions: numerals and *sVsVC)",
  notes="*isa 'one' > MLG, MNY ìsa; *siwa 'nine' > MRN sìvi, MNY suei; roots of the shape *sVsVC: *se(ŋ)seŋ > MRN "
        "tsèntsină, *susuł > sùsună, *səpsəp > MRN sèsitră (but MNY hehep) (Dahl 1951: 42; pp. 143-144).")
P("b", "w", "#_, V_V", "140", as_printed="the weakening of PAN *b ... a PSEB development",
  notes="'It involved a change from *b to *w, not one from *b to v, as the fricativization of semivowels only "
        "happened after the migration' (p. 140), known since Dahl (1951). PAN *bulaɫ > PSEB *wulan; *babuy > "
        "*babuy (sic, ex. 16).")
P("d", "r", "#_, V_V", "140-141", as_printed="PAN *d had become *r and *-t in this protolanguage",
  notes="PMP *daSun > PSEB *rawen; *dəŋəR > *reŋey; *ludaq > *rura (exx. 3, 5, 11). PSEB 'was left without *d' "
        "(p. 141).")
P("j", "r", "V_V", "132-134", as_printed="PAN *ajan > PSEB *ŋ/aran",
  notes="From the examples, not stated as a rule: PAN *ajan > *ŋ/aran (ex. 3), *qapəjuS > *aperu (ex. 11), *pija "
        "> *pire (ex. 18).")
P("z", "r", "elsewhere", "132", as_printed="PAN *quzaɫ 'rain' > PSEB *uran",
  notes="From the example (ex. 3), not stated as a rule.")
P("y", "∅", "#_, V_V", "139", as_printed="nonfinal PAN *y was lost in PSEB",
  notes="'PSEB and PMLG *y- and *-y- do not reflect PAN/PMP *y'; agreeing with Mahdi (1988: 150) that MNY "
        "ka-kau 'tree' is inherited from *kaSiw and MNY kayu, MLG hàzu borrowed from Malay (p. 139).")
P("e", "e", "elsewhere", "132", as_printed="PMP *katəl > PSEB *katen",
  notes="The PMP schwa (keyed e) is a mid front vowel in PSEB, written e: *təbəl > *tewen, *ənəm > *enem "
        "(exx. 3, 20). Not stated as a rule in Adelaar (2012); see Adelaar (1995: 340).")
P("ə", "e", "elsewhere", "134, 136, 138", as_printed="PAN *duSa > PSEB *rue",
  notes="Word-final PMP *a, which Smith (2017a) has as Proto-Barito *ə (it occurs only there): *duSa > *rue, *pija > *pire, *siwa > *siwe, "
        "*baRah > *waye (exx. 11, 17, 18). From the examples, not stated as a rule; Mahdi (1988) states it "
        "(Adelaar 1991: 9).")
P("a", "e", "_y#", "136", as_printed="PMP *pajay > PSEB *parey",
  notes="*m-aCay > *matey (ex. 17). From the examples; PSEB *-ey then merged with *-e in PMLG (PMLG4).")

# ---------------------------------------------------------------- PMLG (Table 4, p. 135; §3)
D = "adelaar2012-pseb"
M = lambda *a, **k: b.corr(PMLG, *a, decision=D, **k)
M("p", "k", "_#", "129, 135", conditioning="unknown", n="8", total="14",
  as_printed="PMLG1. PSEB *-p > PMLG *-k, *-t",
  notes="'(possibly already started before)'. PSEB *lelap > PMLG *lelak (*lelaf-en); *raqup > *rauk; *sisip > "
        "*sisik (ex. 14). Of fourteen Malagasy words with a historical final labial, eight have -kă and six -tră, "
        "and none -nă or Ø (pp. 128-129, after Dahl 1951: 68-69); eight still show -f- before a suffix.")
M("p", "t", "_#", "129, 135", conditioning="unknown", n="6", total="14",
  as_printed="PMLG1. PSEB *-p > PMLG *-k, *-t",
  notes="PSEB *lelep > PMLG *lelet (*lelef-an); *tutup > *tutut; *sesep > *seset (ex. 14). Dahl: 'an attempt by "
        "final labial stops to realign with the only two other final stops left' (p. 129).")
M("h", "∅", "elsewhere", "135-136", as_printed="PMLG2. PSEB *h > PMLG Ø in all positions",
  notes="PSEB *hire > PMLG *ire; *aheŋ > *aeŋ; *lepah > *lefa; *yatuh > *yatu (ex. 15).")
for v, c in (("a", "w"), ("u", "y")):
    note = (f"PMLG3. PSEB *-u, *-aw, *-uy > PMLG *-u: " +
            ("*anraw > *andru, *hapaw > *t-afu, *lalaw > *lalu" if c == "w" else "*apuy > *afu, *babuy > *vavu, "
             "*laŋuy > *laŋu (*laŋuy-en)") + " (ex. 16, p. 136). Word-final.")
    M(v, "u", f"_+{c}", "135-136", as_printed=f"PSEB *-{v}{c} > PMLG *-u", notes=note)
    M(c, "u", f"{v}+_", "135-136", as_printed=f"PSEB *-{v}{c} > PMLG *-u", notes=note)
note = "PMLG4. PSEB *-ey, *-e > PMLG *-e: *parey > *pare, *matey > *mate, *tetey > *tete (*tetey-an) (ex. 17). Word-final."
M("e", "e", "_+y", "135-136", as_printed="PSEB *-ey > PMLG *-e", notes=note)
M("y", "e", "e+_", "135-136", as_printed="PSEB *-ey > PMLG *-e", notes=note)
M("p", "f", "elsewhere", "135, 140", as_printed="the one from PAN *p to MLG f, which must also have gone [through] an intermediate *ϕ stage",
  notes="Postmigratory, comparable to Proto-Sabaki *p > Comorian β through *ϕ; North Betsimisaraka still has ϕ "
        "(Kikusawa 2006: 8) (p. 140). Adelaar's PMLG forms have f: *fitu, *afu, *lelef-an (pp. 135-136).")
M("k", "h", "#_, V_V", "128, 130, 140", as_printed="the change from *k to h",
  notes="Shared with Comorian (Nurse & Hinnebusch 1993: 71-73); where k has not become h it palatalizes next to i "
        "in both (p. 140). PMLG forms in Table 2 (p. 130) and in Adelaar (2013) have h (*hatuk 'neck', *hali 'pit'), "
        "Table 1 (p. 127) *katen. Final *-k stays (-kă).")

# ---------------------------------------------------------------- dialects (Tables 1-2, 5-6; §§3-5)
def R(lect, *a, **k):
    k.setdefault("derivation", "")
    b.corr(lect, *a, **k)

FN = "Final nasals: Table 1 (p. 127) and MLG1 (Table 5, pp. 136-137)."
R(MRN, "ŋ", "n", "elsewhere", "138", as_printed="MRN1. PMLG *n, *ŋ > n in all positions",
  notes="*aŋ/aran > anàrană, *taŋan > tànană, *wulaŋ > vùlană (ex. 19); 'in MRN, *n and *ŋ have also merged as n in "
        "intervocalic position, whereas in most other dialects they have not' (p. 137).")
R(MRN, "m", "n", "_#", "137-139", as_printed="MRN2. PMLG *-m, *-n, *-ŋ > n (-m-, -n-, before a suffix)",
  notes="*welum > vèlună (velùm-ină), *enem > ènină, *alem > àlină (ex. 20). 'The merger of final nasals was total "
        "in MRN, which only has -nă' (p. 137), with the paragogic -ă. *-m sometimes reemerges before a suffix. "
        "Merina also 'occasionally' lost final nasals: *ipən > ìfy (pp. 126-127).")
R(MRN, "y", "z", "elsewhere", "138-140", as_printed="MRN3. PMLG *y (in all positions) > z",
  notes="*y- > z/- (personal article), *yatuh > zàtu, *uyat > ùzatră, *tetey-an > tetèz-ană (ex. 21). A recent "
        "change 'not representative of PMLG': it never fully took place in SBM, Tandroy or Old South East "
        "Malagasy (p. 140). Comorian *j > ž is comparable.")
R(MRN, "e", "i", "_#", "136, 138-139", as_printed="MRN4. PMLG *-e > -i",
  notes="*pare > fàri, *waye > vài, *tete > tèti, *mate > màti (ex. 22); MLG4: PMLG *-e, *-i > MRN -i (ex. 18). Not "
        "in fè 'hip' < *pee, whose final è comes from contraction (ex. 23).")
R(MRN, "t", "ʈ͡ʂ", "_#", "136-137", as_printed="MLG2. PMLG *-t > ... -tră in MRN", source_form="tr",
  notes="With the paragogic vowel: -tră (Table 2, p. 130: ùzatră, fùitră, tàhutră, rìvutră). tr is a retroflex "
        "affricate (§4); -tră usually becomes -r- before a suffix, but -t- for a historical *t or after a root "
        "with r (p. 125 n. 5). Paragogic vowels are 'a very recent development' (p. 130).", decision="adelaar2012-symbols")
R(MRN, "w", "v", "elsewhere", "139-140", as_printed="the fricativization of semivowels only happened after the migration",
  notes="*wulan > vùlană, *waye > vài (Tables 1-2). Postmigratory, 'in a contact situation involving both MLG and "
        "Comorian languages' (p. 140).")
for L, nm in ((SAK, "SSK"), (BARA, "Bara")):
    for ph in ("m", "n", "ŋ"):
        R(L, ph, "∅", "_#", "127, 137", as_printed=f"{nm}: word-final nasals were lost",
          notes=FN + (" 'In southwestern MLG dialects such as SSK, word-final nasals were lost' (p. 137): làla, ùlu, "
                      "vàza, hàndri, vèlu (-m-), ène." if L == SAK else " Bara làla, ùlu, vàza, hàndri, tìli (Table 2, p. 130)."))
for L, nm, pv, pg in ((SAK, "SSK", "ĕ", "tsĕ"), (BARA, "Bara", "ĭ", "tsĭ"), (TDR, "Antandroy", "ĕ", "tsĕ")):
    R(L, "t", "t͡s", "_#", "130, 137", as_printed=f"MLG2. PMLG *-t > ... -tsĕ or -tsĭ in southwestern dialects (SSK, Bara MLG, Antandroy MLG)",
      source_form="ts", decision="adelaar2012-symbols",
      notes=f"With the paragogic -{pv}: {nm} -{pg} (Table 2, p. 130; p. 137).")
R(SAK, "k", "k", "_#", "128, 130", derivation="stated-retention", as_printed="SSK ... maintained *-t and *-k as a rule",
  notes="With the paragogic -ĕ: làtakĕ, vìtikĕ, hàtukĕ (Table 2).")
R(SAK, "e", "e", "_#", "136, 138", derivation="stated-retention", as_printed="in SSK, *-i and *-e are still distinguished",
  notes="MLG4: sìve, rùe, fìre, vàe, màte against hàli (ex. 18).")
R(SAK, "w", "v", "elsewhere", "127, 130", notes="vùla, vàza, vùru (Tables 1-2); postmigratory (§3).")
R(BARA, "m", "∅", "_p", "142", as_printed="a more general reduction of homorganic nasal + stop clusters",
  notes="MRN tùmpu : Bara tùpu 'lord', ampèla : apèla 'woman', ùmpa : ùpa (ex. 25). Also, 'somewhat less "
        "systematically', in the dialects of South East Madagascar (Dahl 1983: 7) and in the Sorabe texts; compare "
        "Shimaore (Mayotte) (pp. 142-143).")
R(BARA, "n", "∅", "_t, _t͡s", "142", as_printed="a more general reduction of homorganic nasal + stop clusters",
  notes="MRN vìntană : Bara vìta 'destiny', tantàra : tàtara, vinàntu : vinàtu, hàntsină : hàtsi, tsèntsină : tsètsi "
        "(ex. 25).")
NK = "North Sakalava (Thomas-Fattier 1982), Table 1 (p. 127): "
R(NSK, "n", "ŋ", "_#", "127", conditioning="unknown", notes=NK + "làlaŋă 'path' < *lalan, aŋàraŋă 'name' < *aŋaran. 'Dialects distinguishing *-n and *-ŋ sometimes substitute *-ŋ for *-n' (p. 137).")
R(NSK, "n", "∅", "_#", "127", conditioning="unknown", notes=NK + "ùlu 'person' < *ulun.")
R(NSK, "ŋ", "ŋ", "_#", "127, 130", derivation="stated-retention", notes=NK + "vàzaŋă, ùruŋ, vùruŋ, vùzuŋ; 'original final nasals are often not followed by any vowel' (p. 130).")
R(NSK, "t", "ʈ͡ʂ", "_#", "130, 137", source_form="tr", decision="adelaar2012-symbols",
  as_printed="final *-t became -trĭ in northern dialects (Tsimihety MLG, NSK)",
  notes="With an echo vowel: fùetrĭ, rìvutrŭ (Table 2, p. 130).")
R(TSM, "t", "ʈ͡ʂ", "_#", "137", source_form="tr", decision="adelaar2012-symbols",
  as_printed="final *-t became -trĭ in northern dialects (Tsimihety MLG, NSK)")
R(SBM, "t", "ʈ͡ʂ", "_#", "137", source_form="r", decision="adelaar2012-symbols",
  as_printed="a 'mute r' in SBM (Dahl 1951:65; Ruud 1955:35)",
  notes="Old SBM (Flacourt 1658) has -ts or -te (ozats, foetse, tahotse, Table 2). Adelaar (2013: 463) takes "
        "Ruud's final r to be a retroflex affricate like Merina's.")
R(SBM, "n", "n", "_#", "137", derivation="stated-retention", as_printed="SBM still distinguishes -n and -ŋ",
  notes="'and, in Flacourt's (1658) dictionary, also -m' (p. 137); Old SBM lalan, oulon, voulan (Table 1).")
R(SBM, "ŋ", "ŋ", "_#", "137", derivation="stated-retention", as_printed="SBM still distinguishes -n and -ŋ",
  notes="Old SBM vazaŋ, monengh (Table 1).")
R(SBM, "i", "e", "_#", "136, 138", as_printed="MLG4. PMLG *-e, *-i > MRN -i, SBM -e",
  notes="SBM sìve, rùe, fìre, àbe < *awi, aŋgàde < *hadi (ex. 18).")
R(SBM, "y", "j", "elsewhere", "140", derivation="stated-retention",
  as_printed="this change [*y > z] never fully took place in the SBM dialect",
  notes="'or in part of the vocabulary of SBM' (p. 139); SBM kayo 'wood' (Ruud 1951) beside MRN hàzu (ex. 21).")
R(OSE, "y", "j", "elsewhere", "139-140", derivation="stated-retention",
  as_printed="PMLG *y is still reflected as y in the Old Taimoro writings in Sorabe script",
  notes="Old Taimoro wayaŋ 'molar', wuyuŋ 'neck', uyarri 'nerve' (Tables 1-2).")
R(OSE, "ŋ", "ŋ", "_#", "127", derivation="stated-retention",
  notes="Old Taimoro wayaŋ, handriŋ, uruŋ, wuyuŋ, faniŋ, aiŋ, f/uneŋ (Table 1, from Ferrand 1904).")
R(OSE, "n", "n", "_#", "127", derivation="stated-retention", notes="Old Taimoro ulun, l<um>alan (Table 1).")
R(OSE, "t", "ʈ͡ʂ", "_#", "130, 141", source_form="rr", decision="adelaar2012-symbols",
  notes="Old Taimoro uyarri 'nerve', fuirri 'navel', matahurru 'afraid' (Table 2): 'tr itself is rendered by a "
        "geminated r sign in Sorabe' (p. 141 n. 38). Old Taimoro also had echo vowels (Dahl 1983: 67) (p. 130).")

OV = dict(origin="override", source_id="", voicing="", rounding="")
for L in (PSEB, PMLG):
    b.t["phonemes"].append(dict(lect_id=L, ipa="e", source_symbol="e", **{"class": "V"}, place="front", manner="mid",
                                reason="A mid front vowel ('a mid-front vowel' at the PSEB level, Adelaar 1995: 340, "
                                       "after Hudson 1967), not the schwa that e stands for in a reconstruction.",
                                **{k: v for k, v in OV.items()}))
for L in (MRN, NSK, TSM, TNK, SBM, OSE):
    b.t["phonemes"].append(dict(lect_id=L, ipa="ʈ͡ʂ", source_symbol="tr", **{"class": "C"}, place="retroflex",
                                manner="affricate", reason="The Malagasy tr, a retroflex affricate (Adelaar 2012: §4).",
                                **{k: v for k, v in OV.items()}))
EV = ("PMLG *e is a mid front vowel ('a mid-front vowel' at the PSEB level, Adelaar 1995: 340); entered so that the "
      "implied vowel is not respelled ə, the reading of e in a reconstruction (decision adelaar2012-symbols).")
for L in (SAK, NSK, BARA, TDR, TNK, TSM, SBM, TNS, OSE):
    R(L, "e", "e", "elsewhere", "131-138", derivation="implied-retention", notes=EV)
b.dec("adelaar2012-pseb",
      "How are Adelaar's (2012) Proto-South East Barito and Proto-Malagasy placed, and his PAN etyma entered?",
      "PSEB (Glottolog's Southeast Barito, sout2919) under Proto-Barito, with PMLG (Malagasic, mala1537) under it. "
      "PAN is restated against PMP, which Proto-Barito inherits (PAN *S and *h = PMP *h; *C, *T = *t; *ł = *n). "
      "Ma'anyan and Dusun Witu stay under Proto-Barito with Smith's (2017a) rows; moving them under PSEB would "
      "leave Smith's Proto-Barito rows on the wrong parent. Mahdi's (1988) Proto-East Barito (Adelaar 1991: 9) is "
      "not entered as a node. Rows marked 'from the examples' follow the cited etyma, not a stated rule.",
      "Move Ma'anyan (and Samihim, Dusun Witu) under PSEB, restating Smith's rows; or list Ma'anyan as a proposed "
      "daughter of PSEB through alt_parents; enter Proto-East Barito.", "124, 131-140")
b.dec("adelaar2012-dialects",
      "Which Malagasy varieties are entered, and with which Glottocodes?",
      "Merina (meri1243, a dialect of Glottolog's Plateau Malagasy, plt, entered as its language node), Sakalava "
      "(saka1291; Adelaar's 2012 SSK and 2013 Sakalava of Morondava), North Sakalava (no Glottolog languoid, code "
      "blank), Bara, Tandroy, Tankarana, Tsimihety, South Betsimisaraka (Ruud's, sout2920), Tanosy, and Old South "
      "East Malagasy (the Sorabe texts of Ferrand 1904, Adelaar's 2012 'Old Taimoro') as an attested language with no Glottocode. All "
      "directly under PMLG. Flacourt's (1658) data (2012 'Old SBM', 2013 a Tanosy source) are cited in notes, not "
      "entered as a lect. Antaisaka, Betsileo, Tanala, Vezo, Masikoro and Mahafaly, cited for single forms, are not "
      "entered.",
      "A separate Old South Betsimisaraka (Flacourt) lect; Betsileo, Antaisaka and Tanala as dialects of Plateau "
      "Malagasy and Tesaka; Glottolog's Malagasic subgroups as groups.", "127, 130, 155-156")
b.dec("adelaar2012-symbols",
      "Which IPA for the Malagasy affricates tr and ts and the paragogic vowels?",
      "tr = ʈ͡ʂ (a retroflex affricate, Adelaar 2012: §4), ts = t͡s; Ruud's SBM final r and the Sorabe geminated r "
      "as ʈ͡ʂ, as Adelaar reads them; the paragogic (whispered) vowel after -tr, -ts, -k, -n is not part of the "
      "reflex and is given in the notes; o = u (Adelaar's own respelling); final y = i.",
      "ʈʳ or ʈ͡ɽ for tr; t͡ʃ for the southwestern ts; the paragogic vowel as part of the reflex (ʈ͡ʂə̆).",
      "127-141")

write("adelaar2012-malagasy", b.t, """# adelaar2012-malagasy

Adelaar, Alexander. 2012. Malagasy phonological history and Bantu influence. *Oceanic Linguistics* 51(1). 123-159. Generator: `tools/batch_scripts/nine_sources_2026_11_25/malagasy.py`.

## Scope

- **New proto-languages** Proto-Southeast Barito (`pseb`, sout2919) under Proto-Barito and Proto-Malagasy (`pmlg`, mala1537) under it (decision `adelaar2012-pseb`), both `assumed-unchanged`.
- **PSEB** rows: Table 3 (PSEB2-9, p. 131) with the examples of §2.3, *b > *w and *d > *r (§3, pp. 140-141), *y lost (p. 139), and the vowels from the examples (schwa and final *a > *e, *-ay > *-ey). PAN restated against PMP.
- **PMLG** rows: Table 4 (PMLG1-4, p. 135), *p > f and *k > h (§3).
- **Eleven Malagasy lects** (decision `adelaar2012-dialects`): Plateau Malagasy (node) with Merina, Sakalava, North Sakalava, Bara, Tandroy, Tankarana, Tsimihety, South Betsimisaraka, Tanosy, Old South East Malagasy (attested in the Sorabe texts). Rows from Tables 1-2, 5-6 (MLG1-4, MRN1-4), §3 (w > v) and §5 (Bara cluster reduction). Glottolog 5.4 coordinates.
- IPA decision `adelaar2012-symbols`.

## Not entered

- PSEB1 and MLG3 (stress), the paragogic vowels as reflexes (notes only), the morphophonemic alternations before suffixes (Mahdi 1988), §4 Malay d > tr in loans, §6 the *s exceptions beyond the notes, §8 etymologies, §7 contact history (notes only).
- Ma'anyan, Samihim and Dusun Witu stay under Proto-Barito.
""")

# ====================================================================== Adelaar 2013
S = "adelaar2013"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Adelaar, Alexander", year="2013",
    title="Malagasy dialect divisions: Genetic versus emblematic criteria", kind="comparative", pub_type="article",
    container_title="Oceanic Linguistics", volume="52", issue="2", pages="457-480",
    url_or_doi="https://doi.org/10.1353/ol.2013.0025",
    notes="Consulted directly on 25 November 2026 (Project MUSE PDF in Downloads). Reviews Dez (1963), Vérin, Kottak "
          "& Gorlin (1969), Mahdi (1988), Gueunier (1988), Simon (2006), lexicostatistics and the Levenshtein method "
          "(§3), and proposes criteria for a genetic classification (§4): *li and *ti, final *t (Tables 1-6), *y > z "
          "and *w > v (Table 7), the merger of final-syllable *i and *e (Table 8), the personal prefixes *i and "
          "*ra-, numeral compounds, <in>, voice and lexical taxonomy. Tentatively a Northern-Central-Eastern branch "
          "against the southwestern dialects; the place of the western dialects is open (pp. 476-477). Malagasy in "
          "its orthography with o as u, final y as i, paragogic vowels with a breve, ŋ; PMP for PAN."))
D = "adelaar2013-classification"
T1 = "Table 1 (p. 462): *li and *ti across the dialect areas."
R(MRN, "l", "d", "_i", "462-463", decision=D, as_printed="*li ... as di ... in central and eastern dialects",
  notes=T1 + " dìmi < *lima, hùditră < *kulit, vìdi < *bəli. Only di and tsi are innovations; li and ti are "
        "retentions with no subgrouping value (p. 463). The tendency began 'before the split of Proto-East Barito' "
        "and lasted until after the present dialects formed (p. 467); Simon (1988: 222, 239) notes the same changes "
        "in Ma'anyan.")
R(MRN, "t", "t͡s", "_i", "462-463", decision=D, source_form="ts", notes=T1 + " tsìukă < *teyup, fùtsi < *putiq, atsìmu.")
R(MRN, "e", "i", "_(C)#", "474", decision=D, as_printed="the merger of PMLG *i and *e (< PMP *ə) as i in final (open and closed) syllables",
  notes="Table 8 (p. 474): hàdi, tsìdină, hùditră, fàti, fùitră, dumùhină against Sakalava hàli, tìli, hùlitsĕ, "
        "fàte, fùetsĕ, limùhe. 'Diagnostic of a central group, as it seems to be limited to its members' (p. 474).")
for L, ex in ((SAK, "lìme, hùlitsĕ, vìli; tìukĕ, ràti, fùti, atìmu"), (TDR, "lìme, hùlitsĕ, vìli; tìukĕ, ràti, fùti, atìmu")):
    R(L, "l", "l", "_i", "462", decision=D, derivation="stated-retention", notes=T1 + " " + ex.split(";")[0] + ".")
    R(L, "t", "t", "_i", "462, 466", decision=D, derivation="stated-retention",
      notes=T1 + ex.split(";")[1] + ". Even the southwestern dialects 'occasionally show tsi'; the 1PL.INCL "
            "(Sakalava tsìka) is affricated in many western and southwestern dialects (p. 466).")
R(SAK, "e", "e", "_(C)#", "474", decision=D, derivation="stated-retention",
  notes="Table 8 (p. 474): the merger of final-syllable *i and *e 'has not taken place in Sakalava': fàte, fùetsĕ, limùhe.")
TK = "Table 3 (p. 464): three Tankarana subdialects (Serva & Petroni 2011). "
R(TNK, "l", "d", "_i", "463-464", decision=D,
  notes=TK + "atudi, man-gadi, huditrĭ, dimi, tadi, vadi. Adelaar takes di and tsi here to be 'the result of lexical "
        "replacement and/or influence from standard Malagasy'; historically Tankarana kept *li and *ti (pp. 463, "
        "465). Dez (1963) had it with li and ti.")
R(TNK, "l", "l", "_i", "463-464", decision=D, derivation="stated-retention", status="sporadic",
  notes=TK + "only liu/li 'blood' < *liu 'saliva' of nine instances.")
R(TNK, "t", "t͡s", "_i", "463-464", decision=D, source_form="ts",
  notes=TK + "futsi, tsi, atsika, tsinai, tsikŭ; Vérin, Kottak & Gorlin (1969) recorded atika (p. 463).")
R(TNK, "t", "t", "_i", "463-464", decision=D, derivation="stated-retention", status="sporadic",
  notes=TK + "rati (Ambiloha) and mi-tiliŋĭ (Antalaha) only.")
R(TNK, "t", "ʈ͡ʂ", "_#", "463", decision="adelaar2012-symbols", source_form="tr",
  notes="Table 2 (p. 463): efatră, rivutrŭ, laŋitrĭ, huditrĭ, man-tutrĭ.")
TS = "Table 4 (p. 465), from Faridanona (1977): "
R(TSM, "l", "l", "_i", "464-465", decision=D, derivation="stated-retention", conditioning="lexical",
  notes=TS + "tìliŋi < PSEB *tiliŋ, li 'wild', lìu 'blood'; doublets tàli 'plait', vali-làhi. Forms with li and ti "
        "'have more idiosyncratic meanings', those with di and tsi are closer to Merina and 'suspect of borrowing' "
        "(p. 464).")
R(TSM, "l", "d", "_i", "464-465", decision=D, conditioning="lexical",
  notes=TS + "a/ùdi, an/tsùdiŋĭ, mùdi, tàdi 'rope', vàdi 'spouse'; also dìmi, vìdi (Fukazawa).")
R(TSM, "t", "t", "_i", "464-465", decision=D, derivation="stated-retention", conditioning="lexical",
  notes=TS + "tìliŋy 'flight of birds', tìŋgi, tìpakă, tinàini 'Monday' (Arabic; Merina alatsinaini): 'at one point in "
        "time, *ti without affricatization was the default pronunciation' (p. 465).")
R(TSM, "t", "t͡s", "_i", "464-465", decision=D, source_form="ts", conditioning="lexical",
  notes=TS + "fùntsi, tsìukŭ, vavìtsi, fàtsikĭ, atsìka; doublets tiŋànana/atsiŋànana, atìmu/atsìmu.")
R(SBM, "l", "d", "_i", "462", decision=D, notes=T1 + " dime (R47), vua-vide (R52).")
R(SBM, "t", "s", "_i", "462", decision=D, notes=T1 + " fuse (R53); atsimu (R47).")
R(TNS, "l", "l", "_i", "465-466", decision=D, derivation="stated-retention",
  notes="Table 5 (p. 466): tali 'rope'; Dez: Tanosy 'the only dialect showing a change from *ti to tsi while "
        "maintaining *li as li'. Current Tanosy has many di and tsi forms from standard Malagasy (n. 6): tadiŋi.")
R(TNS, "t", "s", "_i", "466", decision=D, notes="Table 5 (p. 466): fusi 'white', tsi 'not'; hulisi 'skin' < *hulit.")
R(OSE, "l", "l", "_i", "465-466", decision=D, derivation="stated-retention",
  notes="Table 5 (p. 466): haliŋu (F115), hulitri (F87), talimpali (F115), taliŋi (F88). Simon (1988: 267) took li "
        "for a spelling convention; Adelaar argues against it.")
R(OSE, "t", "t͡s", "_i", "466", decision=D, source_form="ts",
  notes="Table 5 (p. 466): futsi (F86), afuntsi (F112), tsi (F114), vuavitsi (F92).")
R(OSE, "w", "w", "elsewhere", "474", decision=D, derivation="stated-retention",
  notes="Table 7 (p. 474): 'Old South East Malagasy has maintained both *y and *w': weluŋ 'alive', wuyuŋ 'neck'.")
R(TDR, "y", "j", "elsewhere", "474", decision=D, derivation="stated-retention", status="sporadic",
  notes="Table 7 (p. 474): ìe 3SG.NOM, ìe(ŋe) 'dark' against Merina ìzi, ìzină; *y kept 'in a few cases' in Tandroy "
        "and Tanala.")
R(SBM, "y", "j", "elsewhere", "474", decision=D, derivation="stated-retention",
  notes="Table 7 (p. 474): kàyo, vayan/kòo, rafoyaŋ-ô against Merina hàzu, vàzană, rafùzan-o.")

b.dec(D, "Is a subgrouping of the Malagasy dialects entered?",
      "No: all lects sit directly under Proto-Malagasy. Adelaar (2013) rejects Dez's (1963) li/ti division on "
      "methodological and distributional grounds (li and ti are retentions), finds the lexicostatistical "
      "classifications (Vérin, Kottak & Gorlin 1969; Mahdi 1988; Simon 2006) weak, and only tentatively groups the "
      "northern dialects with the central and eastern ones (Northern-Central-Eastern) against the southwestern ones, "
      "leaving the western dialects (Sakalava, West Bara) open (pp. 476-477). The *li > di, *ti > tsi and final *i/*e "
      "rows mark the evidence on the lects.",
      "Enter a Northern-Central-Eastern group and a Southwestern group; or Glottolog's Malagasic subgroups "
      "(North-Central, Southwestern).", "462-477")

write("adelaar2013-malagasy", b.t, """# adelaar2013-malagasy

Adelaar, Alexander. 2013. Malagasy dialect divisions: Genetic versus emblematic criteria. *Oceanic Linguistics* 52(2). 457-480. Generator: `tools/batch_scripts/nine_sources_2026_11_25/malagasy.py`.

## Scope

- Rows on the Malagasy lects of batch `adelaar2012-malagasy`: *li and *ti (Tables 1, 3-5), final *t (Table 2), *y and *w (Table 7), final-syllable *i/*e (Table 8, §4.1). Retentions are `stated-retention`; Tsimihety doublets are `lexical`.
- Decision `adelaar2013-classification`: no dialect subgroups.

## Not entered

- Table 6 (final tr/ts in the Betsimisaraka sources of 1603-1905), the personal prefixes, numerals, <in>, voice and lexical taxonomy (§§4.2-4.6), the lexicostatistical figures of §3: notes and decision only.
""")

# ====================================================================== Adelaar 1991 (+ Mahdi 1988)
S = "adelaar1991"
b = Batch(S)
b.t["sources"] += [
    dict(id=S, author="Adelaar, K. A.", year="1991", title="New ideas on the early history of Malagasy",
         kind="comparative", pub_type="chapter", container_title="Papers in Austronesian linguistics No. 1",
         editors="Steinhauer, Hein", series="Pacific Linguistics A-81", pages="1-22", place="Canberra",
         publisher="Pacific Linguistics",
         notes="Consulted directly on 25 November 2026 (PDF in Downloads; Table 1 read from the page image). A review "
               "of Simon (1988) and Mahdi (1988). Mahdi's Table 1 (p. 9) traces the changes from PAN via Proto-Barito, "
               "Proto-East Barito and Proto-South-East Barito to Proto-Malagasy and Merina; Hudson's (1967: 34) and "
               "Mahdi's East Barito trees are compared in Figures 2 and 4. Adelaar argues against Mahdi's East "
               "Austronesian substratum for the Malagasy word-final changes and against Simon's chronology. Volume "
               "and series details as commonly cited; the PDF has no title page."),
    dict(id="mahdi1988", author="Mahdi, Waruno", year="1988",
         title="Morphophonologische Besonderheiten und historische Phonologie des Malagasy", kind="comparative",
         pub_type="book", series="Veröffentlichungen des Seminars für Indonesische und Südseesprachen der "
                                 "Universität Hamburg 20", place="Berlin", publisher="Dietrich Reimer",
         notes="Bibliographic details from the reference list of Adelaar (1995). Not consulted directly: its sound "
               "changes are entered from Adelaar's (1991: 9) summary table; Adelaar (2012) cites its morphophonemics "
               "(pp. 241-262) and *R (p. 161)."),
]
VIA = dict(via_source_id=S, via_page="9")
D = "mahdi1988-chain"


def Mh(lect, par, child, env="elsewhere", notes="", **k):
    k.setdefault("derivation", "composed")
    b.corr(lect, par, child, env, "", notes=notes, decision=D, **k)
    r = b.t["correspondences"][-1]
    r["source_id"] = "mahdi1988"
    r.update(VIA)
    r["via_note"] = "Summary table of Mahdi's (1988) changes, Proto-Barito to Merina."
    # the id was made with source adelaar1991; keep it unique and stable
    r["id"] = "c" + __import__("hashlib").sha1(("mahdi|" + r["id"]).encode()).hexdigest()[:10]


T = "Mahdi's Table 1 column "
Mh(PSEB, "ə", "e", "elsewhere", T + "'Proto South-East Barito': PAN -a[S/H/ʔ]# > PB, PEB ə > PSEB e, i.e. word-final *a "
   "and *a before a final *S, *H or *ʔ. Smith (2017a) has final *a > Proto-Barito *ə, which occurs only there.",
   as_printed="-a[S/H/ʔ]# > ə > ə > e")
Mh(PSEB, "d", "d", "N_", T + "PAN d/D/j > PB D > PEB D; after a nasal the stop stays d (PSEB *handriŋ 'forehead', "
   "Adelaar 2012: 127). Composed: the table gives no post-nasal reflex.", as_printed="d/D/j > D > D",
   derivation="stated-retention")
Mh(PSEB, "j", "d", "N_", T + "PAN d/D/j > PB D > PEB D: Mahdi merges *j with *d; after a nasal the merged stop stays d "
   "(PSEB *handriŋ 'forehead', Adelaar 2012: 127; *andri 'younger sibling' < *a(n)ji, Adelaar 2013: 475). Composed: "
   "the table gives no post-nasal reflex.", as_printed="d/D/j > D > D")
Mh(PSEB, "e", "e", "elsewhere", T + "PAN ə > PB ə > PEB ə > PSEB e. The PMP schwa is keyed e here.",
   as_printed="ə > ə > ə > e")
Mh(PSEB, "y", "∅", "#_, V_V", T + "PAN iV-, -ViV- (the glide) > PB i > PEB Ø.", as_printed="iV-, -ViV- > i > ø")
Mh(PSEB, "a", "ɛ", "_y#", T + "PAN -ai > PB -ay > PEB, PSEB -ɛy; PAN -əi, -əHi > PB -əy, -əi > PEB -ɛy.",
   as_printed="-ai > -ay > -ɛy > -ɛy")
Mh(PSEB, "e", "ɛ", "_y#", T + "PAN -əi, -əHi > PB -əy, -əi > PEB, PSEB -ɛy.", as_printed="-əi, -əHi > -əy, -əi > -ɛy")
Mh(PSEB, "b", "w", "elsewhere", T + "PAN b/B > PB b > PEB b > PSEB w.", as_printed="b/B > b > b > w")
Mh(PSEB, "ɡ", "k", "elsewhere", T + "PAN g > PB g > PEB k.", as_printed="g > g > k > k")
Mh(PSEB, "R", "∅", "#_, V_V", T + "PAN R > PB R > PEB y > PSEB Ø, -y.", as_printed="R > R > y > ø, -y")
Mh(PSEB, "R", "y", "_#", T + "PAN R > PB R > PEB y > PSEB Ø, -y.", as_printed="R > R > y > ø, -y")
Mh(PSEB, "h", "∅", "elsewhere", T + "PAN S/H/ʔ > PB Ø (PMP *h).", as_printed="S/H/ʔ > ø")
Mh(PSEB, "q", "ʔ", "elsewhere", T + "PAN q > PB, PEB, PSEB ʔ; lost only in Proto-Malagasy. Adelaar (2012: 131) has "
   "PSEB Ø.", as_printed="q > ʔ > ʔ > ʔ")
Mh(PSEB, "l", "n", "_#", T + "PAN -l/-L > PB -l > PEB ? > PSEB -n.", as_printed="-l/-L > -l > ? > -n")
for ph, ap in (("d", "d/D/j > D"), ("j", "d/D/j > D"), ("z", "Z > z")):
    Mh(PSEB, ph, "r", "elsewhere", T + f"PAN {ap} > PEB D > PSEB r-, -r-, -t.", as_printed=f"{ap} > D > r-, -r-")
    Mh(PSEB, ph, "t", "_#", T + f"PAN {ap} > PEB D > PSEB r-, -r-, -t.", as_printed=f"{ap} > D > -t")
T = "Mahdi's Table 1 column 'Proto Malagasy': "
Mh(PMLG, "ɛ", "e", "elsewhere", T + "PSEB -ɛy > PMLG -ey (PSEB *ɛ occurs only before final *y).", as_printed="-ɛy > -ey")
Mh(PMLG, "a", "u", "_w#", T + "PSEB -aw > PMLG -uw (also PAN -əuq > PB -əuʔ > PMLG -uw).", as_printed="-aw > -uw")
Mh(PMLG, "k", "h", "#_, V_V", T + "PSEB k > PMLG h, -k.", as_printed="k > h, -k")
Mh(PMLG, "p", "f", "elsewhere", T + "PSEB p > PMLG f.", as_printed="p > f")
Mh(PMLG, "s", "s", "elsewhere", T + "PSEB (blank in the table) > PMLG s, h.", conditioning="unknown", as_printed="s > s, h")
Mh(PMLG, "s", "h", "elsewhere", T + "PSEB (blank in the table) > PMLG s, h.", conditioning="unknown", as_printed="s > s, h")
Mh(PMLG, "ʔ", "∅", "elsewhere", T + "PSEB ʔ > PMLG Ø.", as_printed="ʔ > ø")
Mh(PMLG, "n", "∅", "_#", T + "PSEB -n > PMLG -Ø, -n.", conditioning="unknown", as_printed="-n > -ø, -n")
Mh(PMLG, "n", "n", "_#", T + "PSEB -n > PMLG -Ø, -n.", conditioning="unknown", as_printed="-n > -ø, -n")
T = "Mahdi's Table 1 column 'Malagasy' (Merina): "
Mh(MRN, "e", "i", "_+y", T + "PMLG -ey > Merina -y (= i), /ez/ at a morpheme boundary (note a).", as_printed="-ey > -y/ez/")
Mh(MRN, "y", "i", "e+_", T + "PMLG -ey > Merina -y (= i), /ez/ at a morpheme boundary (note a).", as_printed="-ey > -y/ez/")
Mh(MRN, "e", "i", "_(C)#", T + "PMLG e > Merina e; i in last syllable.", as_printed="e > e; i in last syllable")
Mh(MRN, "e", "e", "elsewhere", T + "PMLG e > Merina e; i in last syllable. The mid front vowel.", as_printed="e > e; i in last syllable",
   derivation="stated-retention")
Mh(MRN, "w", "v", "elsewhere", T + "PMLG w > Merina v (also from PAN b: 'v (b)').", as_printed="w > v")
Mh(MRN, "t", "t͡s", "_i", T + "PMLG t > Merina t, ts (/_i); 'ts preceding i reflects Proto Austronesian *t, *T or *C' "
   "(note c).", source_form="ts", as_printed="t > t, ts (/_i)")
Mh(MRN, "t", "ʈ͡ʂ", "_#", T + "PSEB t > PMLG t, -C > Merina t, ts (/_i), -tra. Mahdi's PMLG *-C 'was probably a "
   "preglottalised or implosive voiceless palatal stop' (p. 175, note b); it is not entered as a PMLG phoneme of its "
   "own. 'tr preceding final ă reflects Proto Austronesian *-t, *-C, *-j or *-d. When occurring in other positions, tr "
   "and ts are not inherited' (note c).", source_form="tr", as_printed="t > t, -C > t, ts (/_i), -tra")
Mh(MRN, "ŋ", "n", "elsewhere", T + "PMLG ŋ > Merina n.", as_printed="ŋ > n")
Mh(MRN, "ñ", "n", "elsewhere", T + "PMLG ɲ > Merina n. PMP *ñ, carried down unchanged.", as_printed="ɲ > n")
Mh(MRN, "l", "d", "_i", T + "PMLG l > Merina l, d (/_i).", as_printed="l > l, d (/_i)")
Mh(MRN, "s", "∅", "elsewhere", T + "PMLG s, h > Merina s, Ø; 's usually occurs in loanwords, but in a few cases it "
   "seems to reflect Proto Austronesian *s' (note d). The table's PMLG h from *s, lost in Merina, has merged here with "
   "PMLG h from *k, which Merina keeps; only the s row is entered.", as_printed="s, h > s, ø")

b.dec(D, "How is Mahdi's (1988) chain of changes, read in Adelaar (1991: 9), entered?",
      "Composed onto the nodes in the database: his PAN > Proto-Barito > Proto-East Barito > PSEB columns as rows of "
      "PSEB against Proto-Barito (which carries the PMP inventory, not Mahdi's Proto-Barito with *D and *z), then "
      "PMLG against PSEB and Merina against PMLG, all with source mahdi1988 via adelaar1991: 9. Only changes are "
      "entered; identities stay implied. His Proto-East Barito is not a node; his PAN (no *r, *z, *c, *T; *w and *y "
      "as vowels; preglottalised *b, *C, *j) is restated in PMP terms.",
      "Enter Mahdi's Proto-Barito and Proto-East Barito as nodes of their own; enter every line of the table "
      "including identities.", "9")
write("adelaar1991-malagasy", b.t, """# adelaar1991-malagasy

Adelaar, K. A. 1991. New ideas on the early history of Malagasy. In Hein Steinhauer (ed.), *Papers in Austronesian linguistics No. 1* (Pacific Linguistics A-81), 1-22. Canberra: Pacific Linguistics. Generator: `tools/batch_scripts/nine_sources_2026_11_25/malagasy.py`.

## Scope

- Sources `adelaar1991` and `mahdi1988`.
- Mahdi's Table 1 (p. 9, read from the page image), PAN to Merina, composed onto PSEB, PMLG and Merina (decision `mahdi1988-chain`), source `mahdi1988` via `adelaar1991`: 9.

## Not entered

- Mahdi's Proto-Barito and Proto-East Barito as nodes; his PAN inventory; his Austronesian classification and East Austronesian substratum; Simon (1988); the classifications of Figures 2 and 4 (notes only).
""")

# ====================================================================== Adelaar 1995 (+ Hudson 1967)
S = "adelaar1995"
b = Batch(S)
b.t["sources"] += [
    dict(id=S, author="Adelaar, Alexander", year="1995", title="Asian roots of the Malagasy: A linguistic perspective",
         kind="comparative", pub_type="article", container_title="Bijdragen tot de Taal-, Land- en Volkenkunde",
         volume="151", issue="3", pages="325-356", url_or_doi="https://www.jstor.org/stable/27864676",
         notes="Consulted directly on 25 November 2026 (JSTOR PDF in Downloads). An overview of the linguistic "
               "research on the Asian origins of Malagasy (§1), a critique of Dahl (1991) on Malay loans, Islam and "
               "Bangka (§2, including Lom, which Adelaar shows to be Malayic, pp. 339-341), and South Sulawesi "
               "loanwords in Malagasy (§3.1: vadi, taneti, vuhu, ta-, huta; pp. 341-352). Phonological statements on "
               "Southeast Barito: the PSEB schwa (p. 340), *R lost or y, *s split into h (Malagasy Ø) and s (p. "
               "340)."),
    dict(id="hudson1967", author="Hudson, Alfred B.", year="1967", title="The Barito isolects of Borneo",
         kind="comparative", pub_type="book", series="Southeast Asia Program Data Paper 68", place="Ithaca, NY",
         publisher="Cornell University",
         notes="Bibliographic details from the reference lists of Adelaar (1991, 1995). Not consulted directly. "
               "The lexicostatistical classification of the Barito languages (Proto Central + South-East Barito, "
               "p. 34, in Adelaar 1991: Figure 2)."),
]
b.corr(PSEB, "e", "e", "elsewhere", "", source_form="", derivation="",
       notes="'The reflexes of schwa in Maanyan and Malagasy had already changed into a mid-front vowel at the "
             "Proto Southeast Barito level' (Adelaar 1995: 340, citing Hudson 1967); an argument against Dahl's "
             "Southeast Barito link for Lom, which keeps the schwa.", decision="adelaar2012-pseb")
r = b.t["correspondences"][-1]
r.update(source_id="hudson1967", via_source_id=S, via_page="340", via_note="Cited without page.")
r["id"] = "c" + __import__("hashlib").sha1(("hudson|" + r["id"]).encode()).hexdigest()[:10]
b.corr(PSEB, "R", "∅", "#_, V_V", "340", conditioning="unknown", derivation="", decision="adelaar2012-pseb",
       notes="'In Southeast Barito languages the loss is general in the inherited lexicon: *R became y (Merina "
             "Malagasy) or 0, and this happened in initial, intervocalic and final positions. In loanwords it "
             "remained r in initial and intervocalic positions, and became t (Merina Malagasy -tra) in final "
             "position' (p. 340).")
b.corr(PSEB, "s", "h", "elsewhere", "340", derivation="", decision="adelaar2012-pseb",
       notes="'In Southeast Barito, *s usually became h (Malagasy 0) but remained s in a number of words': h/Ø in "
             "inherited words, s in loans, with exceptions both ways; Dahl (1991: 65) puts this down to lexical "
             "diffusion (p. 340).")
write("adelaar1995-malagasy", b.t, """# adelaar1995-malagasy

Adelaar, Alexander. 1995. Asian roots of the Malagasy: A linguistic perspective. *Bijdragen tot de Taal-, Land- en Volkenkunde* 151(3). 325-356. Generator: `tools/batch_scripts/nine_sources_2026_11_25/malagasy.py`.

## Scope

- Sources `adelaar1995` and `hudson1967`; three PSEB rows (p. 340): the schwa (Hudson 1967 via Adelaar 1995), *R and *s.

## Not entered

- The loanword evidence (Malay, Javanese, South Sulawesi) and the history of the debate (§§1-3): no correspondences. Lom is not entered.
""")
