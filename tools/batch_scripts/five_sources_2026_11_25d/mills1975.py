#!/usr/bin/env python3
"""Mills (1975), The reconstruction of Proto South Sulawesi, Archipel 10: 205-224.

New proto-language Proto-South Sulawesi (pss) under PMP, its inventory (§2, pp. 205-206), the PAN > PSS changes
Mills states (pp. 208, 211-213), and seven daughters with the reflexes of §§3-5 (pp. 206-215). Read directly
(text layer, pp. 211 and 213 checked against the page images).
"""
from common import Batch, write

S = "mills1975"
b = Batch(S)
b.t["sources"].append(dict(
    id=S, author="Mills, Roger F.", year="1975", title="The reconstruction of Proto South Sulawesi",
    kind="comparative", pub_type="article", container_title="Archipel", volume="10", pages="205-224",
    url_or_doi="https://doi.org/10.3406/arch.1975.1250",
    notes="Consulted directly on 25 November 2026 (Persée PDF in Downloads). A summary of the author's Michigan "
          "dissertation (Proto South Sulawesi and Proto Austronesian phonology, 1975), which Jukes (2020) cites "
          "with this paper as 1975a and 1975b. §2 the PSS inventory, §§3-5 the reflexes in the daughter "
          "languages, §6 reduplicated roots, §7 morphology, §8 subgrouping and homeland, Appendix 60 PSS etyma "
          "(pp. 220-224). Language data from the author's field work and from Matthes (1859, 1874), van der Veen "
          "(1929, 1940) and Adriani & Kruijt (1914)."))

REFS = [
    dict(id="vanderveen1929", author="van der Veen, H.", year="1929",
         title="Nota betreffende de grenzen van de Sa'dansche taalgroep en het haar aanverwante taalgebied",
         kind="comparative", pub_type="article", container_title="Tijdschrift voor Indische Taal-, Land- en Volkenkunde",
         volume="69", pages="58-96", notes="Bibliographic details from the reference list of Mills (1975: 220); not consulted directly."),
    dict(id="vanderveen1940", author="van der Veen, H.", year="1940", title="Tae' (Zuid-Toradjasch)-Nederlandsch woordenboek",
         kind="dictionary", pub_type="book", place="'s-Gravenhage", publisher="Martinus Nijhoff",
         notes="Bibliographic details from the reference list of Mills (1975: 220); not consulted directly."),
    dict(id="matthes1859", author="Matthes, B. F.", year="1859", title="Makassaarsch-Hollandsch woordenboek",
         kind="dictionary", pub_type="book", place="'s-Gravenhage", publisher="Martinus Nijhoff",
         notes="Bibliographic details from the reference list of Mills (1975: 219); not consulted directly."),
    dict(id="matthes1874", author="Matthes, B. F.", year="1874", title="Boegineesch-Hollandsch woordenboek",
         kind="dictionary", pub_type="book", place="'s-Gravenhage", publisher="Martinus Nijhoff",
         notes="Bibliographic details from the reference list of Mills (1975: 219); not consulted directly."),
    dict(id="adrianikruijt1914", author="Adriani, N.; Kruijt, A. C.", year="1914",
         title="De Bare'e-sprekende Toradjas van Midden-Celebes, 3de deel: Taal- en letterkundige schets der Bare'e-taal "
               "en overzicht van het taalgebied Celebes-Zuid-Halmahera", kind="grammar", pub_type="book",
         place="Batavia", publisher="Landsdrukkerij",
         notes="Bibliographic details from the reference list of Mills (1975: 219); not consulted directly."),
    dict(id="pelenkahu1967", author="Pelenkahu, R. A.", year="1967", title="Gambaran sepintas lalu tentang dialek2 Mandar",
         kind="grammar", pub_type="thesis", publisher="IKIP-Makassar Sarjana thesis",
         notes="Bibliographic details from the reference list of Mills (1975: 220); not consulted directly."),
    dict(id="pelenkahu1972", author="Pelenkahu, R. A.; Muthalib, Abd.; Amin, Muh.; Manala M., W. M.", year="1972",
         title="Bahasa di lima Massenrempulu", kind="comparative", pub_type="book", place="Ujung Pandang",
         publisher="Lembaga Bahasa Nasional",
         notes="Editors, not authors, in the reference list of Mills (1975: 220), where the details come from; not "
               "consulted directly."),
]
b.t["sources"] += REFS

PSS = "pss"
BUG, MAK, MDR, SAD, MASS, PUS, SEKO = "bugi1244", "maka1311", "mand1442", "tora1261", "duri1242", "pitu1237", "seko1241"
ALL = [BUG, MAK, MDR, SAD, MASS, PUS, SEKO]

b.t["lects"].append(dict(
    id=PSS, name="Proto-South Sulawesi", alt_names="PSS;Proto South Sulawesi", type="proto-language",
    parent_id="pmp", clade="South Sulawesi", region="South Sulawesi; homeland placed on the lower Sa'dan river (p. 217)",
    default_system="Mills", systems="Mills",
    orthography_note="Mills writes ë for the schwa (ə here), ng for ŋ and q for the glottal stop (ʔ here); his e is "
                     "'a low or mid front vowel' (n. 4, p. 208), not the PMP schwa. *R is 'presumably a voiced velar "
                     "fricative' (p. 213); *z perhaps an affricate [dz], 'the voiced counterpart of *s' (p. 212).",
    notes="Mills (1975: 205): the ancestor of Buginese, Makassarese, Mandar, Sa'dan Toraja, Pitu Ulunna Salo, Seko "
          "and Massenrempulu', 'a minimum'. Nasal clusters *mp mb nt nd ñc ñj ŋk ŋg ns nz are reconstructed "
          "intervocalically only (p. 206); consonants after *ə were geminate (*tëllu 'three'), which Mills connects "
          "with a fixed penultimate stress (pp. 208-209); *q and *h are tentative, *q only in reduplicated "
          "monosyllabic roots (*buqbuk, *miqmis) and *h in two etyma (*(dr)ehde, *bahba) (§6, pp. 214-215). "
          "Final consonants *p t k m n ŋ r l s R (§5, p. 212); *-p is tentative (p. 213). '*(dr)' marks etyma with PAN "
          "*d or *D that show r in every daughter, where PSS *d or *r cannot be decided (pp. 210-211); '(C)' an "
          "unspecified final. The palatals may be loans in the three languages that keep them, so that 'PSS in fact "
          "had lost them' (p. 210). Mills states his PAN in Dempwolff's notation (*h for Dyen's *q, ë for the "
          "schwa); the PAN > PSS rows are restated against PMP (decision mills1975-pss). Mills's subgrouping "
          "(§8, pp. 217-218): Makassarese broke off first, before the change of nasal + voiceless stop to geminates, "
          "then Mandar, then Buginese; then 'Toraja, in the broadest sense, including PUS-Seko and Sa'dan', while "
          "Massenrempulu' stayed in the homeland, close to Sa'dan (71%). The daughters are entered directly under "
          "PSS (decision grimes1987-tree). Glottolog 5.4's South Sulawesi (sout3413) has no Seko and adds Tamanic; "
          "the Glottocode is left blank (decision mills1975-pss)."))

GL = dict(
    bugi1244=dict(name="Bugis", alt_names="Buginese;Bug.;Ugi", iso639_3="bug", latitude="-4.47", longitude="119.977",
                  region="South Sulawesi: the east coast, the central lakes and the west coast north of Maros",
                  notes="Mills's Bug., from his field work and Matthes (1874). Mills reconstructs the b/w and d/r "
                        "alternation after the prefix maq- (maqbere 'give' < were) as historical *b, *d > w, r in "
                        "absolute initial position, retained after q (p. 211); there are many doublets, and the "
                        "synchronic rule now also affects r from PAN *r, *R. Bug. -q alternates with r, s, k before "
                        "the suffixes -ëng and -i (p. 212). Final consonants only q and ng (p. 212). Grimes & Grimes "
                        "(1987: 15, 30-32): with Campalagian the Bugis Family; dialects Luwu, Wajo, Bone (Palakka), "
                        "Soppeng, Enna' (Sinjai, Bulukumba), Sidrap, Barru, Sawitto, Pangkep, Camba, Pasangkayu."),
    maka1311=dict(name="Makasar", alt_names="Makassar;Makassarese;Makasarese;Mangkasara';Mak.", iso639_3="mak",
                  latitude="-5.65551", longitude="119.838", region="South Sulawesi: the south-west of the peninsula",
                  notes="Mills's Mak., from Matthes (1859) and the Lembaga Bahasa Nasional. The final continuants r, l, "
                        "s survive with an echo vowel and q (ukiriq < *ukir), so that synchronically Makasar has "
                        "only final q and ng (pp. 212-213 and n. 11); -q > k before -ang and -i (p. 212). Mills "
                        "calls Konjo and Salayar dialects of Makasar (p. 211); Grimes & Grimes (1987: 15, 25-29) make "
                        "Makassar (dialects Maros-Pangkep, Gowa (Lakiung), Turatea (Jeneponto), Bantaeng), Konjo and "
                        "Selayar a 'language chain', the Makassar Subfamily, and Jukes (2020: 20-21) separate "
                        "languages. The sourced inventory is Jukes's (2020) Gowa (Lakiung) dialect."),
    mand1442=dict(name="Mandar", alt_names="Mdr.", iso639_3="mdr", latitude="-3.34717", longitude="119.068",
                  region="West Sulawesi: the coast from Polewali to Cenrana",
                  notes="Mills's Mdr. is the Balanipa dialect of his field work, with the Campalagiang and "
                        "Cendana dialects of Adriani & Kruijt (1914) and the Majene of Pelenkahu (1967) (p. 212, n. 10, 12). Final "
                        "consonants q n ng r l s, the status of l doubtful and n merging with ng in Balanipa; Majene "
                        "has q ng r l s (p. 212). -q is lost before -an/-ang (p. 213). Grimes & Grimes (1987: 15, "
                        "33-36): a dialect chain (Majene, Balanipa, Pamboang, Sendana, Awo' Sumakuyu, Malunda) in "
                        "their Northern South Sulawesi Family; their Balanipa, Pamboang and Malunda have a voiced "
                        "alveolar fricative with ungrooved blade for d (p. 96)."),
    tora1261=dict(name="Toraja-Sa'dan", alt_names="Sa'dan Toraja;Sa'dan;Tae';Sad.", iso639_3="sda",
                  latitude="-2.97144", longitude="119.829", region="South Sulawesi: the upper Sa'dan valley",
                  notes="Mills's Sad., from van der Veen's (1940) Tae' dictionary and van der Veen (1929). The "
                        "outlying dialects (Mamasa, Mangki, Rongkong) differ from Makale-Rantepao 'mainly in the "
                        "retention of palatals and intervocalic /w/' (p. 218). Final consonants q k n ng; -q "
                        "alternates with r, s before -an (p. 212). Grimes & Grimes (1987: 15, 43-48): Toraja-Sa'dan "
                        "(Makale, Rantepao, West Toraja) in their Toraja-Sa'dan Subfamily with Kalumpang, Mamasa, "
                        "Rongkong and Toala'; Mamasa and Rongkong have an unreleased final [k̚] (p. 96)."),
    duri1242=dict(name="Duri", alt_names="Massenrempulu';Masenrempulu;Mass.", iso639_3="mvp",
                  latitude="-3.37081", longitude="119.871", region="South Sulawesi: Kabupaten Enrekang",
                  notes="Mills's Mass. (Massenrempulu'), whose forms come mostly from the Duri dialects Cakke (DuriC) "
                        "and Kalosi (DuriK) (p. 205 n. 1) and from Pelenkahu et al. (1972); entered on Duri, with "
                        "the dialects as varieties (decision mills1975-lects). Final consonants q k n ng, Duri adding "
                        "h (p. 212); a final -t reappears before -an (sirakatan, p. 214); *R and *-s have merged as h "
                        "(p. 213). The Massenrempulu' lects measure over 80% with each other and 71% with Sa'dan "
                        "(p. 218). Grimes & Grimes (1987: 15, 49-51): Duri (Cakke, Kalosi) is a dialect of "
                        "Masenrempulu (with Maiwa and Enrekang) in their Masenrempulu Subfamily; Enrekang has a "
                        "back velar nasal where other languages have a final k or glottal stop (p. 96)."),
    pitu1237=dict(name="Pitu Ulunna Salu", alt_names="PUS;Pitu Ulunna Salo;Pitu Uluna Salu", iso639_3="",
                  region="West Sulawesi: the upper Mamasa and Mambi rivers",
                  notes="Mills's PUS, from his field work and van der Veen (1929) (PUS(V)); Glottolog's Pitu Ulunna "
                        "Salu is a family (Aralle-Tabulahan, Bambam, Ulumanda' and others), entered here as one "
                        "lect as Mills treats it (decision mills1975-lects). Final consonants q k n ng, some "
                        "dialects m (p. 212). Grimes & Grimes (1987: 15, 39-42, 96): dialects Aralle-Tabulahan, "
                        "Mambi, Rantebulahan, Bambang, Mehala'an, Tapango, Ulunda, in their Northern South Sulawesi "
                        "Family; Aralle-Tabulahan, Mambi and Rantebulahan have [h] where Bambang and Mehala'an have "
                        "[w]; Aralle-Tabulahan and Bambang have [h] for /r/; Bambang has [m] for every final nasal, "
                        "the others [m], [n] or [ŋ]; Aralle-Tabulahan contrasts a low front lax vowel with [a]."),
    seko1241=dict(name="Seko", alt_names="SekoL;SekoP", iso639_3="",
                  region="South Sulawesi: the upper Karama river",
                  notes="Mills's Seko, from word lists filled in by informants in the Lemo (SekoL) and Padang (SekoP) "
                        "dialects; forms are 'sic' unless heard (p. 220). Geminates after *ə are simplified (p. 209). "
                        "Final consonants q k ng, no n (p. 212). Glottolog 5.4's Seko is a family (Seko Padang "
                        "seko1243, Seko Tengah seko1242, Panasuan) under Rampi-Seko-Badaic, outside its South "
                        "Sulawesi; entered as one lect under PSS, the dialects as varieties (decision "
                        "mills1975-lects). Grimes & Grimes (1987: 15, 52-53) have a Seko Family (Seko Tengah, Seko "
                        "Padang, Panasuan) in their South Sulawesi Stock; Seko Tengah has long and short vowels "
                        "word-finally (p. 97)."),
)
for lid in ALL:
    d = GL[lid]
    b.t["lects"].append(dict(id=lid, glottocode=lid, type="language", parent_id=PSS, **d))

# ---------------------------------------------------------------- PSS inventory (pp. 205-206)
C = [("p", "p", "bilabial", "plosive", "voiceless"), ("t", "t", "dental", "plosive", "voiceless"),
     ("c", "c", "palatal", "affricate", "voiceless"), ("k", "k", "velar", "plosive", "voiceless"),
     ("b", "b", "bilabial", "plosive", "voiced"), ("d", "d", "dental", "plosive", "voiced"),
     ("j", "j", "palatal", "affricate", "voiced"), ("ɡ", "g", "velar", "plosive", "voiced"),
     ("m", "m", "bilabial", "nasal", "voiced"), ("n", "n", "dental", "nasal", "voiced"),
     ("ñ", "ñ", "palatal", "nasal", "voiced"), ("ŋ", "ng", "velar", "nasal", "voiced"),
     ("s", "s", "dental", "fricative", "voiceless"), ("z", "z", "dental", "affricate", "voiced"),
     ("w", "w", "labial-velar", "approximant", "voiced"), ("r", "r", "alveolar", "trill", "voiced"),
     ("l", "l", "alveolar", "lateral-approximant", "voiced"), ("y", "y", "palatal", "approximant", "voiced"),
     ("R", "R", "velar", "fricative", "voiced")]
NOTE = {"c": "Listed with the 'voiceless stops and affricate' (p. 205).",
        "j": "Listed with the 'voiced stops and affricate' (p. 205).",
        "z": "'Perhaps an affricate, phonetically [dz] and systematically the voiced counterpart of *s'; "
             "reconstructed intervocalically only (pp. 211-212).",
        "R": "'The voiced velar fricative usually symbolized with Greek gamma' (p. 206); attested in final "
             "position (§5c, p. 213).",
        "y": "Attested only intervocalically (p. 206).",
        "ñ": "Mills's symbol is n with a tilde (the text layer prints it as n, p. 205)."}
for ipa, sym, pl, mn, vo in C:
    b.ph(PSS, ipa, "C", pl, mn, vo, sym=sym, page="205-206",
         notes=(NOTE.get(ipa, "") + " " if ipa in NOTE else "") + "PSS sound system, §2 (pp. 205-206).")
b.ph(PSS, "ʔ", "C", "glottal", "plosive", "voiceless", sym="q", page="206, 214-215", status="dubious",
     notes="'We also tentatively reconstruct glottal stop (symbolized *q in PSS and in the modern languages) and *h, "
           "both of very limited distribution' (p. 206); *q occurs only as the first consonant of reduplicated "
           "monosyllabic roots (*buqbuk, *miqmis, §6, p. 215).")
b.ph(PSS, "h", "C", "glottal", "fricative", "voiceless", sym="h", page="206, 215", status="dubious",
     notes="Tentative; reconstructed in two etyma (*(dr)ehde 'to boil', *bahba 'door') to account for otherwise "
           "irregular correspondences; 'other analysts might prefer to dismiss the examples' (p. 215).")
V = [("i", "i", "front", "close", "unrounded"), ("e", "e", "front", "mid", "unrounded"),
     ("ə", "ë", "central", "mid", "unrounded"), ("a", "a", "central", "open", "unrounded"),
     ("u", "u", "back", "close", "rounded"), ("o", "o", "back", "mid", "rounded")]
VN = {"e": "'A low or mid front vowel' (n. 4, p. 208). Reconstructible with certainty only as a final, from PAN "
           "*-ay or *-ih (p. 208).",
      "o": "Reconstructible with certainty only as a final, from PAN *-aw or *-uh (p. 208).",
      "ə": "Written ë (the pepet), 'to avoid confusion with my e' (n. 4, p. 208). Consonants after it were geminate "
           "(pp. 208-209)."}
for ipa, sym, pl, mn, rd in V:
    b.ph(PSS, ipa, "V", pl, mn, "", rd, sym=sym, page="206",
         notes=(VN[ipa] + " " if ipa in VN else "") + "PSS vowels, §2 (p. 206).")

b.t["notation_map"] += [
    dict(lect_id=PSS, phoneme="", system="canonical", symbol="", source_id=S, page="205-206",
         notes="Mills's (1975) symbols, with ə for his ë, ŋ for ng and ʔ for q."),
    dict(lect_id=PSS, phoneme="ə", system="Mills", symbol="ë", source_id=S, page="206, 208",
         notes="The pepet, used 'instead of Dyen's *e to avoid confusion with my e' (n. 4)."),
    dict(lect_id=PSS, phoneme="ʔ", system="Mills", symbol="q", source_id=S, page="206"),
]

# ---------------------------------------------------------------- PMP > PSS (stated as PAN)
D = "mills1975-pss"
P = lambda *a, **k: b.corr(PSS, *a, decision=D, **k)
P("e", "ə", page="208", as_printed="PSS *ë (reflecting PAN *e)",
  notes="PAN *e (schwa) > PSS *ë, after which consonants became geminate: PAN *tëlu > pre-PSS [tël:u] > PSS *tëllu "
        "(pp. 208-209); PSS *w and *y never follow *ë. Gemination after *ë is also found in Madurese, Sangirese and "
        "some Philippine languages; parallel development or retention is unclear (p. 209).")
for v, c, out, ap in (("a", "y", "e", "PAN *-ay"), ("a", "w", "o", "PAN *-aw"), ("i", "q", "e", "PAN *-ih"),
                      ("u", "q", "o", "PAN *-uh")):
    note = (f"PSS *{out} in final position < {ap} (p. 208); Mills's PAN *h is Dempwolff's, Dyen's and Blust's *q "
            f"(n. 4)." if c == "q" else f"PSS *{out} in final position < {ap} (p. 208).")
    P(v, out, f"_+{c}", page="208", as_printed=f"PSS *{out} < {ap}", notes=note + " Word-final.")
    P(c, out, f"{v}+_", page="208", as_printed=f"PSS *{out} < {ap}", notes=note + " Word-final.")
P("j", "z", page="212", as_printed="PSS *z reflects Dempwolff's PAN *g",
  notes="Dempwolff's *g of the RLD law (Batak g, Malay d, Javanese r, Tagalog l, Fijian c), read here as PMP *j "
        "(decision mills1975-pss). PSS *z is reconstructed intervocalically only (p. 211).")
P("R", "r", page="211", as_printed="historic *r (< PAN *r or *R)",
  notes="Initial and medial: Bug. raiq 'carry on a raft' < PAN *Rakit (p. 211); PSS *raki 'dirt on the skin' "
        "(Appendix 27). Sirk (1989) counts PAN *R > r among the South Sulawesi innovations (Jukes 2020: 24).")
P("R", "R", "_#", page="212-213", as_printed="final *R",
  notes="Kept as a final, 'clearly reflected in Duri and Bug.' (p. 212): *ipaR, *sangiR (Appendix 53-54).")

# ---------------------------------------------------------------- PSS > daughters
def rows(lects, par, child, env="elsewhere", page="", **k):
    for l in lects:
        c = child[l] if isinstance(child, dict) else child
        if c is None:
            continue
        b.corr(l, par, c, env, page, derivation="", **k)

# §3a (p. 206)
for ph in ("p", "t", "m", "n", "ŋ", "r", "l", "s"):
    rows(ALL, ph, ph, page="206", notes="'Initial and intervocalic PSS *p t m n ng r l s > /p t m n ng r l s/ in "
                                       "all the languages' (§3a). Finals are separate rows (§5).")
b.corr(BUG, "p", "∅", "#_", "206", status="sporadic", derivation="",
       notes="'Occasionally' (n. 2): ile, mile 'choose' < *pile, perhaps from an -um- form; ase 'padi' must be native.")
b.corr(PUS, "r", "h", "conditions unknown", "206", derivation="",
       notes="'A frequent reflex in PUS is /h/; this change affects r < PSS *d as well as r < *r' (n. 2). Grimes & "
             "Grimes (1987: 96) find [h] for /r/ in the Aralle-Tabulahan and Bambang dialects only.")
# §3b
rows([x for x in ALL if x != SEKO], "ɡ", "ɡ", page="206", notes="'Initial and intervocalic PSS *g > ... all others /g/' (§3b).")
b.corr(SEKO, "ɡ", "k", "elsewhere", "206", derivation="", notes="'PSS *g > Seko /k/' (§3b); also after the nasal: "
       "tangkung 'carry' < *tanggung (Appendix 20).")
# §3c *y (intervocalic)
YN = "'PSS *y (attested only intervocalically) > Mak. Seko /y/, Bug. Duri PUS /j/; Mdr. /y/ or /j/, and Sad. /y/, /j/ or 0, depending on dialect' (§3c)."
rows([MAK, SEKO], "y", "j", "V_V", "206", source_form="y", notes=YN, decision="mills1975-symbols")
rows([BUG, MASS, PUS], "y", "ɟ", "V_V", "206", source_form="j", notes=YN, decision="mills1975-symbols")
b.corr(MDR, "y", "j", "V_V", "206", derivation="", source_form="y", conditioning="unknown", notes=YN, decision="mills1975-symbols")
b.corr(MDR, "y", "ɟ", "V_V", "206", derivation="", source_form="j", conditioning="unknown", notes=YN, decision="mills1975-symbols")
for c, sf in (("j", "y"), ("ɟ", "j")):
    b.corr(SAD, "y", c, "V_V", "206", derivation="", source_form=sf, decision="mills1975-symbols",
           notes=YN + " Van der Veen (1929) reports dialects with y or j.")
b.corr(SAD, "y", "∅", "V_V", "206", derivation="", notes=YN + " Regular in the dialect of van der Veen's (1940) "
       "dictionary.")
b.t["correspondences"][-1]["variety"] = "dialect of van der Veen (1940)"
# §3d-g vowels
rows(ALL, "a", "a", page="206", notes="'PSS *a > /a/ in all languages (but see §5a regarding *a before certain final consonants)' (§3d).")
b.corr(BUG, "a", "ə", "_C# (C a dental: t, n, r, l, s)", "213", derivation="", source_form="ë",
       notes="'The quite regular correspondence of Bug. /-ëq/ to a sequence of /a/ plus dental (t d n r l s)' in "
             "Javanese or Tagalog (§5a): urëq 'vein' < *ura(t), palëq 'palm' < *pala(t), apëq < *kapas, wulëng < "
             "*bulan. *-aR gives aq, not ëq (§5c).")
b.corr(MDR, "a", "e", "_t#", "213", derivation="", notes="Mdr. -eq for PAN *-at/-ad, 'mostly in Mdr., but "
       "occasionally in the other languages' (§5a): paleq < *pala(t), ateq < *ate(p?).")
b.corr(MDR, "ə", "i", "_t#", "213", derivation="", notes="Mdr. -iq for PAN *-ët/-ëd (§5a): ulliq 'worm' < *ulë(t).")
for v, w2, sec in (("i", "e", "e"), ("u", "o", "f")):
    rows(ALL, v, v, page="206", notes=f"'PSS *{v} > /{v}/ in all; occasionally /{w2}/, especially in closed syllables' (§3{sec}).")
    rows(ALL, v, w2, "closed syllable", "206", status="sporadic",
         notes=f"'Occasionally /{w2}/, especially in closed syllables' (§3{sec}); n. 3: /{v}/ varies between "
               f"[{v}] and [{w2}] in many of the modern languages, and the dictionaries list doublets.")
for v, w2 in (("u", "i"), ("o", "e")):
    rows([MDR, PUS], v, w2, "_C#", "206", notes="'In the Mdr/PUS area there is an unusual secondary development "
         "whereby /u o/ > /i e/ before a final consonant' (§3f).")
for v, w2 in (("i", "e"), ("u", "o")):
    rows([SAD, MASS], v, w2, "_R#", "213", as_printed="*i and *u > /e/ and /o/ preceding the reflex of *-R in most "
         "languages, but remain as /i/ and /u/ preceding that of *-r",
         notes="§5c; 'possibly this last change could be ascribed to PSS, but the lack of clear cognates from PUS and "
               "Seko makes this risky'. Entered on the languages whose forms show it: Sad. sangeq, DuriC sangeh "
               "'sharpen' < *sangiR (Appendix 54); Bug. sangiq and Mak. sângiriq keep i. The sentence on *-ar is "
               "printed incomplete ('*-ar > /e/ and /o/ preceding ...').")
rows(ALL, "e", "e", page="208", notes="'PSS *e and *o > /e/, /o/ in all' (§3g).")
rows(ALL, "o", "o", page="208", notes="'PSS *e and *o > /e/, /o/ in all' (§3g).")
# §3h *mp nt ngk
H = "'PSS *mp nt ngk > Bug. Mdr. SekoL /pp/ /tt/ /kk/, Mak. Mass. SekoP /mp/ /nt/ /ngk/. Sad. shows both developments' (§3h)."
for n, s in (("m", "p"), ("n", "t"), ("ŋ", "k")):
    rows([BUG, MDR], n, s, f"_{s}", "208", notes=H + (" Bug. /mp nt ngk/ are signs of outside influence, since "
         "nasals assimilate to a following voiceless stop in Bug. morphophonemics." if n == "m" else ""))
    b.corr(SEKO, n, s, f"_{s}", "208", derivation="", notes=H)
    b.t["correspondences"][-1]["variety"] = "Lemo dialect (SekoL)"
    b.corr(SAD, n, s, f"_{s}", "208", derivation="", notes=H + " 'at an earlier stage, this probably represented a "
           "dialect split, but nowadays there is considerable free variation', perhaps a change in progress.")
    b.corr(SAD, n, n, f"_{s}", "208", derivation="", notes=H + " In free variation with the geminate.")
# §3i *mb nd ngg
I = "'PSS *mb nd ngg > Bug. /mp/ /nr/ /ngk/, SekoP /mm/ /nn/ /ngk/, Mak. /mb/ /nr/ /ngg/, Mdr. Sad. Mass. PUS SekoL /mb/ /nd/ /ngg/' (§3i)."
for n, v, bug, sp in (("m", "b", "p", "m"), ("n", "d", "r", "n"), ("ŋ", "ɡ", "k", "k")):
    b.corr(BUG, v, bug, f"{n}_", "208", derivation="", notes=I + " Bug. /mb nd ngg/ are signs of outside influence.")
    b.corr(SEKO, v, sp, f"{n}_", "208", derivation="", notes=I)
    b.t["correspondences"][-1]["variety"] = "Padang dialect (SekoP)"
b.corr(MAK, "d", "r", "n_", "208", derivation="", notes=I + " Mak. /nd/ is a sign of outside influence. "
       "Jukes (2020: 77) hears /nr/ as [ndr].")
rows(ALL, "n", "s", "_s", "208", notes="'PSS *ns > /ss/ in all, though van der Veen (1929) cites examples of /-ns-/ in some "
     "PUS dialects' (§3j): *insAn > Bug. isseng, Sad. issan.")
# §4a *ə and geminates
A = "'The reflexes of PSS *ë ... /ë/ in Bug., /a/ in all the others, with instances in every language of irregular /i e u o/ due to assimilation to neighboring vowels' (§4a)."
b.corr(BUG, "ə", "ə", "elsewhere", "208", derivation="", source_form="ë", notes=A)
rows([x for x in ALL if x != BUG], "ə", "a", page="208", notes=A)
rows([SEKO, PUS], "ə", "u", "_m#", "213", status="sporadic",
     notes="'The change *ë > /u/ in a handful of examples involving known cognates in PAN with *-ëp ... the same change "
           "(*ë > u) before *-m' (§5b): Seko, PUS(V) unung 'six' < *ënnëm (Appendix 47).")
b.corr(SEKO, "ə", "u", "_p#", "213", status="sporadic", derivation="",
       notes="§5b, the evidence for final *p: Seko atuq 'roof' < *ate(p?) (Appendix 43).")
G = ("'PSS geminate voiced stops are reflected as: single stops in Seko (but no examples for *gg), preglottalized "
     "/qb/, /qd/ (further > /qr/ in Mak.) and /qg/ (very rare) in all the other languages' (p. 209). Geminate "
     "voiceless stops, nasals and continuants are true geminates in all languages but Seko, where they are single.")
for v in ("b", "d", "ɡ"):
    for l in ALL:
        if l == SEKO:
            continue
        out = "ʔr" if (l == MAK and v == "d") else "ʔ" + v
        b.corr(l, v, out, "ə_", "209", derivation="", status="sporadic" if v == "ɡ" else "regular",
               source_form="q" + {"b": "b", "d": "r" if l == MAK else "d", "ɡ": "g"}[v],
               notes=G + " Environment: the geminate after *ə (*sëbbu 'thousand' > Mak. Sad. saqbu).")
# §4b *k
K = "'Regularly > /k/ in Mak. Sad. Mass. and PUS. In Bug. we find both /k/ and 0; in Mdr. and Seko /k/ /q/ or 0. Since the items with 0 most often belong to the so-called basic vocabulary, loss is probably the \"native\" development, but inter-language and inter-dialect borrowing have reintroduced a phonemic /k/' (§4b)."
rows([MAK, SAD, MASS, PUS], "k", "k", page="210", notes=K)
for l in (BUG, MDR, SEKO):
    b.corr(l, "k", "∅", "elsewhere", "210", derivation="", notes=K + (" Bug. ita 'see' < *kita, but pakita "
           "'vision' (p. 210)." if l == BUG else ""))
    b.corr(l, "k", "k", "elsewhere", "210", status="loan-stratum", derivation="", notes=K)
    if l != BUG:
        b.corr(l, "k", "ʔ", "conditions unknown", "210", status="sporadic", derivation="", source_form="q", notes=K)
# §4c palatals
PL = "'Retained as palatals in Bug. Mak. and Mdr. (with *nc regularly > Bug. Mdr. /cc/, *ñj > Bug. /ñc/); elsewhere they have merged with *s d n ns nd respectively. But even in Bug. Mak. and Mdr., there are frequent doublets and irregular cognates showing these same mergers' (§4c). Mills suggests the palatals of these three languages may be due to Malay or Javanese influence, 'and that PSS in fact had lost them'."
for l in (BUG, MAK, MDR):
    b.corr(l, "c", "c", "elsewhere", "210", derivation="", notes=PL, decision="mills1975-symbols")
    b.corr(l, "j", "ɟ", "elsewhere", "210", derivation="", source_form="j", notes=PL, decision="mills1975-symbols")
    b.corr(l, "ñ", "ɲ", "elsewhere", "210", derivation="", source_form="ñ", notes=PL)
    for par, ch in (("c", "s"), ("j", "d"), ("ñ", "n")):
        b.corr(l, par, ch, "elsewhere", "210", status="sporadic", derivation="", notes=PL + " Doublets and irregular cognates.")
for l in (SAD, MASS, PUS, SEKO):
    for par, ch in (("c", "s"), ("j", "d"), ("ñ", "n")):
        b.corr(l, par, ch, "elsewhere", "210", derivation="", notes=PL + (" *cincin 'ring' > Sad. sissin (Appendix 28)." if par == "c" and l == SAD else ""))
    b.corr(l, "ñ", "s", "_c", "210", derivation="", notes=PL + " *ñc merges with *ns, which gives /ss/ (§3j).")
for l in (BUG, MDR):
    b.corr(l, "ñ", "c", "_c", "210", derivation="", notes=PL + " Bug. ciccing 'ring' < *cincin (Appendix 28).")
b.corr(BUG, "j", "c", "ñ_", "210", derivation="", notes=PL)
# §4d *b
B = "'PSS initial *b > /b/ most often in all the languages ... Sad. Mass. PUS and Seko also have the reflex of a secondary /w/ (> Sad. 0, PUS Seko h-) which must have been distinct from PSS *w-. PSS intervocalic *b > /w/ regularly, and this /w/ further > Sad. 0, PUS, Seko /h/. /b/ occasionally is found' (§4d)."
rows(ALL, "b", "b", "#_", "210", notes=B)
b.corr(BUG, "b", "w", "#_", "211", derivation="", notes="Bug. b and d 'change to /w/ and /r/ in absolute initial "
       "position, but are retained after /q/' of the prefix maq-: 'This is assumed to be the regular development; "
       "there are exceptions, of course, and many doublets' (p. 211): wulëng 'moon' < *bulan, wittoeng 'star'.")
for l, ch in ((SAD, "∅"), (MASS, "w"), (PUS, "h"), (SEKO, "h")):
    b.corr(l, "b", ch, "#_", "210", status="sporadic", derivation="",
           notes=B + (" Seko hulang 'moon'; n. 8: 'the correct Seko reflex is unclear', b outnumbers h." if l == SEKO else ""))
for l, ch in ((BUG, "w"), (MAK, "w"), (MDR, "w"), (MASS, "w"), (SAD, "∅"), (PUS, "h"), (SEKO, "h")):
    b.corr(l, "b", ch, "V_V", "210", derivation="", notes=B + (" 'The development in Sad. must have been *b > w > h > 0'." if l == SAD else ""))
# *d
DD = "'Initial and intervocalic PSS *d > either /d/ or /r/. Only Mak. shows /r/ with fair regularity; in the other languages, the reflex is quite mixed' (§4d)."
b.corr(MAK, "d", "r", "elsewhere", "210", derivation="", notes=DD)
for l in (BUG, MDR, SAD, MASS, PUS, SEKO):
    b.corr(l, "d", "d", "conditions unknown", "210", derivation="", notes=DD)
    b.corr(l, "d", "r", "conditions unknown", "210", derivation="", notes=DD)
b.corr(BUG, "d", "r", "#_", "211", derivation="", notes="In absolute initial position, retained as d after the q of "
       "maq-: maqdangëng 'be friends' < rangëng 'friend' (p. 211). See b.")
b.corr(MDR, "d", "r", "V_V", "211", derivation="", notes="The Cendana dialect described by Adriani & Kruijt has b and d "
       "'only initialy, but change to /w/ and /r/ when a vowel comes to precede them' (p. 211).")
b.t["correspondences"][-1]["variety"] = "Cendana dialect"
b.corr(MDR, "b", "w", "V_V", "211", derivation="", notes="Cendana dialect: boyang 'house' > diwoyang 'at home' (p. 211).")
b.t["correspondences"][-1]["variety"] = "Cendana dialect"
# *w
W = "'PSS initial *w > Bug. Mdr. Sad. Mass. /u/ (phonetically [uw...]) or /w/; the sequence uw- > uh- in PUS and Seko' (p. 211)."
for l in (BUG, MDR, SAD, MASS):
    b.corr(l, "w", "u", "#_", "211", derivation="", notes=W + " *wai 'water' > Sad. uai, Mdr. uai (Appendix 49).")
    b.corr(l, "w", "w", "#_", "211", derivation="", notes=W)
for l in (PUS, SEKO):
    b.corr(l, "∅", "u", "#_w", "211", derivation="", notes=W + " *wai > PUS, Seko uhai (Appendix 49).")
    b.corr(l, "w", "h", "#u_", "211", derivation="", notes=W)
for ch, ex in (("b", "bani 'bee' (Bug. uwani)"), ("∅", "akaq 'root' (Mdr. uakeq, PUS uhakaq)")):
    b.corr(MAK, "w", ch, "#_", "211", status="sporadic", n=1, derivation="",
           notes="'The only two examples of *w- in Mak. are contradictory': " + ex + " (p. 211).")
WV = "'PSS intervocalic *w > Bug. Mak. Mdr. Mass /w/, PUS /w, h, b, v/ and Sad. 0 or /w/ depending on dialect; Seko /h/. Interestingly, there are dialects of Bug. (Sinjai) and Mak. (Konjo, Salayar) where w > h also' (p. 211)."
rows([BUG, MAK, MDR, MASS], "w", "w", "V_V", "211", notes=WV)
for ch in ("w", "h", "b", "v"):
    b.corr(PUS, "w", ch, "V_V", "211", derivation="", conditioning="unknown", notes=WV + (
        " Grimes & Grimes (1987: 96): [h] in Aralle-Tabulahan, Mambi and Rantebulahan, [w] in Bambang and Mehala'an."
        if ch in "wh" else ""))
for ch in ("∅", "w"):
    b.corr(SAD, "w", ch, "V_V", "211", derivation="", notes=WV + " The outlying dialects retain intervocalic w (p. 218).")
    b.t["correspondences"][-1]["variety"] = "some dialects"
b.corr(SEKO, "w", "h", "V_V", "211", derivation="", notes=WV)
b.corr(BUG, "w", "h", "V_V", "211", derivation="", notes=WV)
b.t["correspondences"][-1]["variety"] = "Sinjai dialect"
b.corr(MAK, "w", "h", "V_V", "211", derivation="", notes=WV + " Konjo and Selayar are separate languages for Grimes & "
       "Grimes (1987) and Jukes (2020: 20), who notes that their h takes the place of Makasar w (2020: 76 n. 7).")
b.t["correspondences"][-1]["variety"] = "Konjo, Salayar"
# *z
Z = "'PSS *z is reconstructed in intervocalic position only. After *ë, the reflex seems to be: Bug. -ss-, Mdr. Sad. Mass PUS -qd-, but there are only two clear examples. Both show irregularities in Mak. and Seko ... After other vowels, *z is clearly reflected as Bug. -s-, all others -r-' (pp. 211-212)."
b.corr(BUG, "z", "s", "V_V", "211-212", derivation="", notes=Z)
rows([MAK, MDR, SAD, MASS, PUS, SEKO], "z", "r", "V_V", "211-212", notes=Z)
b.corr(BUG, "z", "s", "ə_", "211", derivation="", n=2, notes=Z + " The geminate ss: ëssuq 'gall' < *pëzzu (Appendix 41).")
rows([MDR, SAD, MASS, PUS], "z", "ʔd", "ə_", "211", n=2, source_form="qd", notes=Z + " Sad. Duri PUS paqdu 'gall' < *pëzzu (Appendix 41).")
for l in (MAK, SEKO):
    b.corr(l, "z", "", "ə_", "211", blank_type="irregular", derivation="", notes=Z)
# §5 finals (pp. 212-213)
F = "Final consonants (§5, p. 212): Bug. q ng; Sad. PUS Mass. q k n ng (some PUS dialects m; Seko lacks n; Mass.-Duri adds h); Mdr. q n ng r l s; Mak. q ng r l s, the continuants 'preserved by the addition of an echo-vowel plus /q/ sequence'."
rows(ALL, "p", "ʔ", "_#", "213", source_form="q", notes="'Final *p is reflected everywhere as /q/' (§5b); *-p itself is tentative.")
rows(ALL, "t", "ʔ", "_#", "212-214", source_form="q", notes=F + " Final stops shifted to q through an unreleased stage (§5d). "
     "Duri keeps t before -an (sirakatan, tukatan, p. 214); Bug. -q alternates with r, s, k, Sad. with r, s (p. 212).")
rows([BUG, MAK, MDR], "k", "ʔ", "_#", "212", source_form="q", notes=F + " Inferred from the final consonants these "
     "languages allow: Bug. Mak. tanruq, Mdr. tanduq 'horn' < *tanduk (Appendix 19). Mak. -q > k before -ang and -i.")
rows([SAD, MASS], "k", "k", "_#", "212", notes=F + " Sad. Duri tanduk 'horn' (Appendix 19).")
M = "'Final *m as /n/ in Sad. PUS (my data), Mass., /ng/ in Bug. Mak. Seko, /n/ or /ng/ in Mdr.' (§5b)."
rows([SAD, PUS, MASS], "m", "n", "_#", "213", notes=M)
rows([BUG, MAK, SEKO], "m", "ŋ", "_#", "213", source_form="ng", notes=M)
for ch in ("n", "ŋ"):
    b.corr(MDR, "m", ch, "_#", "213", derivation="", conditioning="unknown", notes=M)
b.corr(PUS, "m", "m", "_#", "213", derivation="", notes=M + " 'Adriani and Kruijt and van der Veen both report "
       "dialects of PUS with /-m/, in examples which do not appear to be borrowings'; Grimes & Grimes (1987: 96): "
       "Bambang has [m] for every final nasal.")
b.t["correspondences"][-1]["variety"] = "some dialects"
NN = F + " *bulan 'moon' > Bug. wulëng, Mak. Mdr. bulang, Sad. Mass. bulan, Seko hulang (Appendix 33)."
rows([BUG, MAK, SEKO], "n", "ŋ", "_#", "212", source_form="ng", notes=NN)
rows([SAD, MASS, PUS], "n", "n", "_#", "212", notes=NN)
b.corr(MDR, "n", "n", "_#", "212", derivation="", notes=NN + " Mdr. n 'is apparently in process of merging with ng' "
       "(Balanipa); Majene has only ng (n. 10).")
b.corr(MDR, "n", "ŋ", "_#", "212", derivation="", notes=NN + " See the row n > n.")
rows(ALL, "ŋ", "ŋ", "_#", "212", notes=F)
for ph, ex in (("r", "*ukir 'write' > Bug. Sad. Duri ukiq, Mak. ukiriq, Mdr. ukir (Appendix 52)"),
               ("l", "*so(m)bAl 'sail' > Bug. sompëq, Mak. sombalaq, Sad. sombaq, Mdr. sobal (Appendix 51)"),
               ("s", "*nipis 'thin' > Bug. Sad. manipiq, Mak. nipisiq, Mdr. nipis, DuriC nipih, DuriK, PUS nipi (Appendix 55)")):
    rows([MDR], ph, ph, "_#", "212", notes=F + " " + ex + "." + (" The status of final l is doubtful (p. 212)." if ph == "l" else ""))
    rows([MAK], ph, ph, "_#", "212", notes=F + " " + ex + ".")
    q = [BUG, SAD] + ([MASS] if ph == "r" else [])
    rows(q, ph, "ʔ", "_#", "212", source_form="q", notes=F + " " + ex + ".")
b.corr(MASS, "s", "h", "_#", "213", derivation="", notes="'In Duri, unlike all the other languages, *R and *-s have "
       "merged, both > /h/' (§5c): DuriC nipih 'thin', kapah, panah (Appendix 2, 55, 56).")
b.t["correspondences"][-1]["variety"] = "Cakke dialect (DuriC)"
b.corr(MASS, "s", "∅", "_#", "213", derivation="", notes="DuriK nipi 'thin', pana 'ginger' (Appendix 55, 56).")
b.t["correspondences"][-1]["variety"] = "Kalosi dialect (DuriK)"
R = "'*R > Duri (Cakke dial.) /h/, Duri (Kalosi dial.) 0, /r/ in Mdr. and Mak., /q/ elsewhere' (§5c, p. 213); *ipaR 'brother-in-law' > Bug. Sad. SekoL ipaq, Mak. iparaq, Mdr. ipar, DuriC ipah (Appendix 53)."
b.corr(MASS, "R", "h", "_#", "213", derivation="", notes=R)
b.t["correspondences"][-1]["variety"] = "Cakke dialect (DuriC)"
b.corr(MASS, "R", "∅", "_#", "213", derivation="", notes=R + " DuriK ipaq 'has irreg. /q/'.")
b.t["correspondences"][-1]["variety"] = "Kalosi dialect (DuriK)"
rows([MDR, MAK], "R", "r", "_#", "213", notes=R + " In Mak. with an echo vowel (iparaq).")
rows([BUG, SAD, PUS, SEKO], "R", "ʔ", "_#", "213", source_form="q", notes=R + " Bug. *-aR > aq, not ëq.")

# ---------------------------------------------------------------- decisions
b.dec("mills1975-pss",
      "How is Mills's (1975) Proto-South Sulawesi placed and its PAN > PSS changes entered?",
      "PSS under PMP, Glottocode blank (Glottolog 5.4's South Sulawesi, sout3413, has no Seko and adds Tamanic; Greater "
      "South Sulawesi adds Rampi and Badaic). Mills's PAN (Dempwolff's notation) is restated against PMP: PAN *h = "
      "PMP *q (n. 4), Dempwolff's *g of the RLD law = PMP *j (> PSS *z). Rows only for the changes Mills states "
      "(PMP *e > *ə, the final diphthongs and *-iq, *-uq, *j > *z, *R > *r and final *R); the lect's `inherit` is "
      "blank, so PMP phonemes Mills does not discuss are unentered for PSS.",
      "PSS under Proto-Celebic or a Greater South Sulawesi node; inherit assumed-unchanged (PMP *z and *h, which share "
      "symbols with PSS *z and *h of different origin, would then be implied wrongly).", "205-213")
b.dec("mills1975-lects",
      "Which lects carry Mills's (1975) language groups Mass., PUS and Seko, and the Makasar dialects?",
      "Mass. on Duri (duri1242), whose dialects Cakke and Kalosi supply most of the forms, as varieties; PUS on "
      "Glottolog's family pitu1237 and Seko on seko1241 (a family under Rampi-Seko-Badaic in Glottolog), each as one "
      "language, with SekoL (Lemo) and SekoP (Padang) as varieties; Konjo and Salayar as varieties of Makasar, as "
      "Mills has them. All seven directly under PSS. Mamuju (Appendix only) is not entered.",
      "Separate lects for Duri Cakke (cakk1237), Duri Kalosi (kalo1260), Seko Padang (seko1243) and Seko Tengah "
      "(seko1242, if Lemo is there); a Massenrempulu language node.", "205, 211-213")
b.dec("mills1975-symbols",
      "Which IPA for Mills's (1975) daughter-language letters c, j, y, ñ, ng, q, ë?",
      "c, ɟ, j, ɲ, ŋ, ʔ, ə: j as the voiced palatal stop, as Jukes (2020: 66) has it for Makasar; y the glide.",
      "j as d͡ʒ and c as t͡ʃ in Bugis and the northern languages.", "205-213")

md = """# mills1975-pss

Mills, Roger F. 1975. The reconstruction of Proto South Sulawesi. *Archipel* 10. 205-224. Generator: `tools/batch_scripts/five_sources_2026_11_25d/mills1975.py`.

## Scope

- **New proto-language** Proto-South Sulawesi (`pss`) under PMP, Glottocode blank (decision `mills1975-pss`), with Mills's inventory (§2, pp. 205-206): 19 consonants, tentative ʔ and h (`dubious`), six vowels. Spelling system `Mills` (ë, ng, q).
- **PMP > PSS**: the changes Mills states against PAN, restated against PMP: *e > *ə (gemination after it), *-ay, *-aw, *-iq, *-uq > *e, *o (fusions), *j > *z, *R > *r, final *R.
- **Seven new lects** under PSS: Bugis, Makasar, Mandar, Toraja-Sa'dan, Duri (Mills's Mass.), Pitu Ulunna Salu, Seko (decision `mills1975-lects`), with the reflexes of §§3-5 (pp. 206-215): retentions, nasal clusters, *ə and the geminates, *k, the palatals, *b, *d, *w, *z, the vowels before finals and the final consonants. Dialect statements carry `variety`. Glottolog coordinates; notes from Mills and Grimes & Grimes (1987).
- IPA decision `mills1975-symbols`.

## Not entered

- PSS *(dr) (PAN *d/*D with r everywhere, pp. 210-211), *nz (two uncertain examples, merged with *nd), the clusters as units, *q and *h in reduplicated roots (§6), and Mamuju (cited in the Appendix only).
- The irregular vowel reflexes of *ə by assimilation, the doublets and the synchronic b/w, d/r rules beyond the rows above, and the morphophonemics of final -q (notes only).
- Final *k, *r, *l, *s in PUS and Seko, and final *-k in Mdr./Seko beyond the inventory statement: Mills gives too few forms.
- §7 morphology, §8 migration scenario (notes only), the Appendix etyma (cited as examples in notes).
"""
write("mills1975-pss", b.t, md)
