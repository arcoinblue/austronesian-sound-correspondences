#!/usr/bin/env python3
"""Geraghty (1983), The history of the Fijian languages: Table 15, the 38 communalects.

Batch geraghty1983-communalects. Table 15 (pp. 183-185) gives the direct reflexes of 30 Proto-Eastern Oceanic
phonemes in 38 Fijian communalects, with numbers that refer to a key of 41 sound changes (p. 186). The user's
comment on decision geraghty1983-communalects: 'Do enter the communalects when ready, listing them under PCP'.
Every cell was read from a page image (the scan's text layer is unusable for the table). PEO is not a node, so the
rows are restated against Proto-Central Pacific, whose reconstruction Geraghty (1986: 289) 'largely based on
proposals made in Geraghty 1983 with respect to Proto-Eastern-Oceanic'.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "five_sources_2026_11_24"))
from common import Batch, write, existing

BATCH = "geraghty1983-communalects"
D = "geraghty1983-communalects-rows"
S = "geraghty1983"
LECTS = existing("lects", "id")
assert "pcp" in LECTS and "west2519" in LECTS and "pfj" in LECTS
b = Batch(S)

# ------------------------------------------------------------------ language nodes
LANG = [
    ("fiji1243", "Fijian", "Eastern Fijian;Bauan Fijian", "fij", "-18.00", "178.33",
     "Glottolog's language for the communalects of eastern Viti Levu, Kadavu and Vanua Levu. Standard Fijian "
     "(Bauan) is not one of Geraghty's (1983) 38 communalects and has no rows here."),
    ("namo1248", "Namosi-Naitasiri-Serua", "", "bwb", "-18.53", "177.64",
     "Glottolog's language (Western Fijian family) for Batiwai, Tubai and Nalea, which Geraghty's Table 15 lists "
     "with the Western communalects."),
    ("laua1243", "Lauan", "Lau", "llx", "-18.21", "-178.79",
     "Glottolog's language for the speech of the Lau group; Geraghty's Lau (LAU) and Vanua Balavu (VBL)."),
    ("loma1261", "Lomaiviti", "", "lmv", "-18.00", "179.31",
     "Glottolog's language for the Lomaiviti islands; Geraghty's Lovoni (LVN), on Ovalau, is entered under it."),
]
for lid, name, alt, iso, lat, lon, notes in LANG:
    assert lid not in LECTS, lid
    b.t["lects"].append(dict(
        id=lid, name=name, alt_names=alt, type="language", glottocode=lid, iso639_3=iso, parent_id="pcp",
        latitude=lat, longitude=lon, alt_parents="pfj:geraghty1986", region="Fiji",
        notes="Language node with no rows of its own. " + notes + " Glottocode, ISO code and coordinates from "
              "Glottolog 5.4."))
b.t["lects"].append(dict(
    id="kada1285", name="Kadavu", type="dialect", glottocode="kada1285", parent_id="pcp", language_id="fiji1243",
    alt_parents="pfj:geraghty1986", region="Kadavu, Fiji", latitude="-19.02", longitude="178.25",
    notes="Glottolog's Kadavu dialect of Fijian; a node with no rows of its own for Geraghty's (1983) Ono, Tavuki "
          "and Nabukelevu, which share its Glottocode. Geraghty's abbreviation K (p. xx)."))

# ------------------------------------------------------------------ communalects
# abbr, id, name, glottocode, language_id, tree_parent, lat, lon, no. in §2.3, page, villages, §2.3 rules, extra note
C = [
 ("WAY", "waya1268", "Waya", "waya1268", "west2519", "", "-17.29", "177.12", 1, "24-26",
  "Nalauwaki, Wayalevu, Natawa, Yalobi (Waya Island); all three villages on Viwa (Bā)",
  "a:ā/_(C)V(C)V#; u:∅/m_ (unstressed); i:∅/t_l,n; ∅:∅/#_a",
  "Geraghty's main source is notes and a draft dictionary by Andrew Pawley."),
 ("KBY", "nakoroboya", "Nakoroboya", "", "west2519", "", "", "", 2, "26",
  "Nakoroboya (alias Vikasē) (Bā)", "as for Waya, also k:x", ""),
 ("NKR", "noikoro", "Noikoro", "", "west2519", "", "", "", 4, "26",
  "Vatubalavu, Nukulau, Nubuyanitu, Draubuta, Vunatoto, Nakoro, Korolevu, Namoli (Nadrogā)",
  "a:ā/_(C)V(C)V#; k:x; t:j/_i", ""),
 ("MGD", "magodro", "Magodro", "", "west2519", "", "", "", 3, "26",
  "Tabuquto, Tabalei, Bukuya, Navagā, Nadevo (Bā)", "as for Waya, excluding the last rule", ""),
 ("TBW", "tubaniwai", "Tubaniwai", "", "west2519", "", "", "", 5, "26",
  "Volivoli, Vunavutu, Nasama, Sigatoka, Navulo, Laselase, Nayawa (Nadrogā)",
  "a:ā/_(C)V(C)V#; d:[ndʒ]/_i,u; s:h; t:j/_u; t:s/_i,e", ""),
 ("BRV(N)", "baravi-nadroga", "Baravi (Nadrogā)", "", "west2519", "", "", "", 6, "26-27",
  "Namada, Tagwaqe, Votualalai, Votua, part Biausevu, Natewa, Balenabelō, Vunayawa, Saru, Naivibuli, Sovi (Nadrogā)",
  "as for Tubaniwai", "Table 15 prints the abbreviation BRV twice; this is the first, among the Western "
  "communalects (BRV (N) in the list of abbreviations, p. xx)."),
 ("BTW", "bati1252", "Batiwai", "bati1252", "namo1248", "", "", "", 7, "27",
  "Nadolī, Korovou, Navuadrā, Wainilotulevu, Naiyalayala, Nasoqo (Namosi); Nuku, Masi, Wainadiro, Waibogi, "
  "Korovou, Veidrala, Galoa, Wainiabia (Sērua)", "a:ā/_(C)V(C)V#; d:[ndʒ]/_i; t:j/_i",
  "'This communalect is viewed by some of its speakers as being further subdivisible' (p. 27)."),
 ("TBI", "tuba1276", "Tubai", "tuba1276", "namo1248", "", "", "", 8, "27",
  "Naimasimasi, Sabata (Sērua)", "a:ā/_(C)V(C)V#; t:j/_i",
  "'Not a totally reliable witness, containing many loans from both Eastern and Western communalects' "
  "(Geraghty 1986: 298)."),
 ("NLE", "nale1237", "Nalea", "nale1237", "namo1248", "", "", "", 9, "27",
  "Nasava (Naitāsiri); Wainimākutu (Namosi)", "as for Tubai", ""),
 ("NMS", "namo1250", "Namosi", "namo1250", "fiji1243", "", "-18.02", "178.13", 10, "27",
  "Nukusere (Sērua); Veivatuloa, Nabukavesi, Naqwara, Lobau, Nakwavu, Namuamua, Nakavika, Navunikabi, Saliadrau, "
  "Naqwarawai, Naraiyawa, Vunibau, Navuniivi, Naduruyasi, Namosi, Narukunibua, Waivaka (Namosi)",
  "t:j/_i is reported by Schütz in 1963 for the Wainikoroiluva area, Namuamua to Naraiyawa; Geraghty's informant "
  "was from Vunibau", ""),
 ("WDN", "waid1240", "Waidina", "waid1240", "fiji1243", "", "", "", 11, "28",
  "Vanuakula, Lomai, Nabukāluka, Navurevure, Wainawaqa, Nadakuni, Nauluvatu, Nasirotū (Naitāsiri)", "none", ""),
 ("LUT", "lutu1234", "Lutu", "lutu1234", "fiji1243", "", "", "", 12, "28",
  "Lutu, Navuniyaro, Nukuloa (Naitāsiri)", "none", ""),
 ("NDR", "nadr1234", "Nadrau", "nadr1234", "fiji1243", "", "-17.75", "177.97", 13, "28",
  "Nadrau, Nagā (alias Vanualevu), Rewasau, Naqelewai (Nadrogā); Nasiriti (Naitāsiri)",
  "k:x; t:j/_i (only Nadrau and Nagā)", ""),
 ("TKM", "tokaimalo", "Tokaimalo", "", "fiji1243", "", "", "", 14, "28",
  "Nailawa, Naiserelagi, Namataveikai, Nabalabala, Vunisea, Nayaulevu (Rā)", "d:t; k:x; t:ʔ; no labiovelars", ""),
 ("NMN", "namena", "Namena", "", "fiji1243", "", "", "", 15, "28",
  "Nānanu, Namena, Burelevu, Lāwaki, Qelekuro, Luvunivuaka (Tailevu)", "no labiovelars", ""),
 ("LVN", "lovoni", "Lovoni", "", "loma1261", "", "-17.69", "178.79", 17, "28-29",
  "Lovoni, Visoto, Nacobo, Nukutōcia (Ovalau Island, Lomaiviti)", "no labiovelars",
  "Left out of Table 16 'because of insufficient data' (p. 182)."),
 ("NMM", "naim1234", "Naimasimasi", "naim1234", "fiji1243", "", "", "", 16, "28",
  "Naimasimasi (Tailevu)", "none", "The list of §2.3 prints its abbreviation as NMN (p. 28); Table 15 and the "
  "list of abbreviations have NMM."),
 ("ONO", "ono-kadavu", "Ono", "kada1285", "fiji1243", "kada1285", "-18.88", "178.48", 18, "29",
  "all on the island of Ono (Kadavu)", "d:[ndʒ]/_i; k:k,x; t:j/_i", ""),
 ("TVK", "tavuki", "Tavuki", "kada1285", "fiji1243", "kada1285", "-19.07", "178.12", 19, "29",
  "Muani, Nasalia, Baidamudamu, Solodamu, Waisomo, Tavuki, Namālata, Natumua, Wailevu (Kadavu)",
  "d:[ndʒ]/_i; k:x; t:j/_i,e; no labiovelars", ""),
 ("NBL", "nabukelevu", "Nabukelevu", "kada1285", "fiji1243", "kada1285", "-19.12", "177.98", 20, "29",
  "Talaulia, Tawava, Naqalotu, Yakita, Nalotu, Korovou, Natokalau, Dagai, Lomati, Nabukelevuirā, Naqaliirā, Nasau, "
  "Daviqele, Kabariki, Levuka, Muaninuku, Tabuya, Nasēgai (Kadavu)", "k:x; no labiovelars", ""),
 ("LAU", "lau-fiji", "Lau", "", "laua1243", "", "-18.22", "-178.80", 21, "29-30",
  "all on the islands of Nayau, Lakeba, Oneata, Moce, Komo, Namuka, Kabara, Vulaga, Ogea, Vatoa and Ono-i-Lau (Lau), "
  "with modern colonies at Veisari (Rewa), Lomaivuna (Naitāsiri) and Viro (Ovalau)",
  "i:i; u:u (a high vowel after a lower vowel does not form a diphthong); d:[ndʒ]/_i; t:j/_i",
  "The list of abbreviations calls it 'Moce, Lau' (p. xxi)."),
 ("VBL", "vanu1243", "Vanua Balavu", "vanu1243", "laua1243", "", "-17.25", "-178.95", 22, "30",
  "all in the Vanua Balavu group (Lau)", "as for Lau", ""),
 ("NVT(B)", "navatu-bua", "Navatu (Bua)", "", "fiji1243", "", "", "", 23, "30",
  "Navatu (Bua)", "k:x; t:ʔ; no labiovelars",
  "Table 15 prints the abbreviation NVT twice; this is the first, before Sōlevu (NVT (B) in the list of "
  "abbreviations). Navatu has a history of recent immigration 'from Tailevu or Lomaiviti' (p. 33)."),
 ("SLV", "solevu", "Sōlevu", "", "fiji1243", "", "", "", 24, "30-31",
  "Nakawakawa, Saolo, Sawani, Nasawana, Nasavu, Nasolo, Cavagā, Nawaidō, Makolei, Vuya, Navave, Nabouwalu, Wairiki, "
  "Nawaca, Tavulomo, Nasau, Dama (Bua)", "as for Navatu (Bua)", ""),
 ("BUA", "bua-fiji", "Bua", "", "fiji1243", "", "-16.80", "178.62", 25, "31-32",
  "Tiliva (part of Bua village), Bua, Dalomo, Vunievu, Waitabu, Koroinasolo (Bua)", "k:x; no labiovelars",
  "'Unique in Vanua Levu in having no glottal stop'; 'Tiliva would be historically preciser' as its name (p. 31)."),
 ("NVS", "navakasiga", "Navakasiga", "", "fiji1243", "", "", "", 26, "32",
  "Nasau, Naivaka, Naviqiri, Lekutu (alias Votua), Yaqaga (Bua)", "k:ʔ; no labiovelars", ""),
 ("GOD", "gone1237", "Gone Dau", "gone1237", "", "", "-16.59", "178.60", 27, "33",
  "Tavea, Galoa (Bua)", "as for Navakasiga",
  "The islands of Yaqaga, Tavea, Galoa and Macuata-i-wai; 'it seems more likely that they constitute a relic "
  "area' (p. 33). One of the four witnesses of PCP *z (Geraghty 1986: 297-298)."),
 ("BRV(M)", "baravi-macuata", "Baravi (Macuata)", "", "fiji1243", "", "", "", 28, "33-34",
  "Nasea, Nabouono, Nabukadogo (Macuata)", "d:t; t:ʔ; q:k; k:ʔ; no labiovelars",
  "Table 15 prints the abbreviation BRV twice; this is the second, among the Vanua Levu communalects (BRV (M)). "
  "The rules are those of most speakers of forty or younger in Nabukadogo (p. 34)."),
 ("SQQ", "seaqaqa", "Seaqāqā", "", "fiji1243", "", "", "", 29, "34-35",
  "Narāvuka, Nacereyaga, Natua, Nanivuda, Saivou (Macuata)", "d:t; t:ʔ; q:k; k:x; no labiovelars", ""),
 ("NBB", "nabalebale", "Nabalebale", "", "fiji1243", "", "", "", 38, "38",
  "part Nabalebale, part Levuka (Cakaudrove)", "d:t; t:ʔ; q:k; k:x; b:p; dr:tr; no labiovelars",
  "'The only communalect in Fiji with no phonetically prenasalized stops. It is spoken only by the very old' "
  "(p. 38)."),
 ("SAV", "savusavu", "Savusavu", "", "fiji1243", "", "-16.78", "179.33", 37, "38",
  "Nukubalavu, Nacēkoro (Cakaudrove)", "d:t; t:ʔ; q:k; k:x/ʔ (x close to a glottal stop); no labiovelars",
  "'This phonology is maintained only by the very old' (p. 38)."),
 ("LBS", "labasa", "Labasa", "", "fiji1243", "", "-16.43", "179.37", 30, "35",
  "Vatutadova, Vuō, Wailevu, Nasēkula, Matailabasa (?) and Mali Island (Macuata)",
  "k:∅; q:k; t:ʔ; ∅:∅/#_a; no labiovelars", ""),
 ("DGT", "dogotuki", "Dogotuki", "", "fiji1243", "", "", "", 31, "35-36",
  "Dogotuki, Rauriko, Vitua, Kedra, Qaranivai, Lagi (Macuata)", "k:ʔ; q:k; ∅:∅/#_a; no labiovelars", ""),
 ("SQN", "saqani", "Saqani", "", "fiji1243", "", "", "", 32, "36",
  "part Vuniwai, Lakeba, Natuvu, Biaugunu, Saqani (Cakaudrove)", "k:ʔ; no labiovelars", ""),
 ("KRL", "koroalau", "Koroalau", "", "fiji1243", "", "", "", 33, "36",
  "Vuinadi, part Koronatoga, Vunidogoloa, Nabua, Tabia, part Bucalevu, Matalōlō (Cakaudrove)",
  "d:t; t:ʔ; q:k; k:x/ʔ (x close to a glottal stop); no labiovelars", ""),
 ("NVT(C)", "navatu-cakaudrove", "Navatu (Cakaudrove)", "", "fiji1243", "", "", "", 34, "36-37",
  "part Navakakā, Naibalebale, Viani, Lea, Drekeniwai (Cakaudrove)", "k:ʔ; no labiovelars",
  "Table 15 prints the abbreviation NVT twice; this is the second, before Tunuloa (NVT (C))."),
 ("TNL", "tunuloa", "Tunuloa", "", "fiji1243", "", "", "", 35, "37",
  "Nasēsē, Qaravatu, Muana, Wailevu, Navetau, Salia, Nailou, Karoko, Koroivonu, Nakanakana (Cakaudrove)",
  "as for Navatu (Cakaudrove)", "Left out of Table 16 'because of insufficient data' (p. 182)."),
 ("NWN", "naweni", "Naweni", "", "fiji1243", "", "", "", 36, "37",
  "Nanuca, Tacilevu, Naweni, Dromuninuku (Cakaudrove)", "d:t; q:k; k:ʔ; no labiovelars",
  "§2.3's rules d:t and q:k are 'maintained only by the very old'; 'the old and middle-aged follow the k:ʔ d:d "
  "phonology of Waikava speech' (p. 37). Table 15 has d and q, the second of these."),
]
ORDER = [c[0] for c in C]
assert len(ORDER) == 38
ID = {c[0]: c[1] for c in C}
GROUP = {}
for g, abbrs in [("Western Fijian communalects", ORDER[0:9]), ("eastern Viti Levu and Lomaiviti", ORDER[9:17]),
                 ("Kadavu", ORDER[17:20]), ("Lau", ORDER[20:22]), ("Vanua Levu", ORDER[22:38])]:
    for a in abbrs:
        GROUP[a] = g
for abbr, lid, name, gc, lang, tp, lat, lon, no, pg, vill, rules, extra in C:
    assert lid not in LECTS, lid
    typ = "language" if lid == "gone1237" else "dialect"
    notes = (f"Geraghty's (1983) communalect no. {no} ({abbr}); villages: {vill} (§2.3, p. {pg}). His "
             f"phonetic realization rules for it: {rules}. Table 15 lists it with the {GROUP[abbr]}. " + extra).strip()
    if not gc:
        notes += " Glottolog 5.4 has no languoid of this name, so no Glottocode."
    elif gc == "kada1285":
        notes += " Shares the Glottocode of Glottolog's Kadavu dialect."
    if lat:
        notes += " Coordinates approximate, for the place named."
    b.t["lects"].append(dict(
        id=lid, name=name, alt_names=abbr, type=typ, glottocode=gc, iso639_3="goo" if lid == "gone1237" else "",
        parent_id="pcp", language_id=lang, tree_parent=tp, alt_parents="pfj:geraghty1986", region="Fiji",
        latitude=lat, longitude=lon, notes=notes,
        orthography_note="Geraghty's quasi-phonetic script (Table 1, pp. 21-22) is respelled in IPA: v β, c ð, j t͡ʃ, "
                         "d' d͡ʒ, y j, g ŋ, gw ŋʷ, q ɡ, qw ɡʷ, kw kʷ, xw xʷ, dr ⁿr, ' ʔ, ā aː. b, d, ɡ and ⁿr are "
                         "prenasalized ([mb], [nd], [ŋɡ], [ndr]); Table 1 gives e and o as [ɛ] and [ɔ]."))

# ------------------------------------------------------------------ Table 15
def spread(*pairs):
    """pairs of (abbreviations or slice, cell) -> {abbr: cell}; later pairs override."""
    out = {}
    for keys, cell in pairs:
        if keys == "*":
            keys = ORDER
        for k in keys:
            assert k in ORDER, k
            out[k] = cell
    assert len(out) == 38, len(out)
    return out


G1, G2, G3, G4 = ORDER[0:9], ORDER[9:17], ORDER[17:20], ORDER[20:22]
G5, G6, G7, G8 = ORDER[22:27], ORDER[27:31], ORDER[31:35], ORDER[35:38]
T = {
 # p. 183
 "a": spread(("*", "a/∅"), (G1[:8], "a/ā/e/o/∅"), (["NLE"], "a/ā/o/∅"), (["NMS", "WDN", "LUT", "NMM"], "a/ā/∅"),
             (["NDR", "TKM", "NMN"], "a/o/∅")),
 "e": spread(("*", "e/a"), (G1, "e/i/a"), (["NMS", "WDN", "LUT", "NMM", "TVK", "NBL", "GOD"], "e/i/a")),
 "i": spread(("*", "i/y"), (["WAY", "KBY"], "i/∅/y"), (["TBI"], "i/e/y"),
             (["SLV", "BUA", "NVS", "GOD", "BRV(M)", "SQQ", "SAV", "LBS", "DGT", "SQN"], "i/∅/y"),
             (["NBB", "KRL"], "i/∅/e/y")),
 "o": spread(("*", "o/a")),
 "u": spread(("*", "u"), (["WAY", "KBY", "SLV", "BUA", "NVS", "GOD"] + G6 + G7, "u/∅")),
 "v": spread(("*", "v")),
 "b": spread(("*", "b"), (["NBB"], "p")),
 "bw": spread(("*", "b"), (["NBB"], "p")),
 "p": spread(("*", "b"), (["LAU", "VBL", "NBB", "SQN", "TNL"], "p")),
 "pw": spread(("*", "b"), (["LAU", "VBL", "NBB", "SQN", "TNL"], "p")),
 # p. 184
 "t": spread(("*", "t/d"), (["WAY", "KBY", "MGD"], "t"), (["NKR"], "t/j"), (["TBW", "BRV(N)"], "t/j/s/h"),
             (["BTW", "TBI", "NLE", "TVK"], "t/j/d"), (["ONO", "LAU", "VBL"], "t/d/j"),
             (["TKM", "BRV(M)", "SQQ", "NBB", "SAV", "KRL"], "ʔ/t"), (["NVT(B)", "SLV", "LBS"], "ʔ/d")),
 "nt": spread(("*", "d"), (["TBW", "BRV(N)", "BTW", "ONO", "TVK", "LAU", "VBL"], "d/d'"),
              (["TKM", "BRV(M)", "SQQ", "NBB", "SAV", "KRL"], "t")),
 "j": spread(("*", "s"), (["TBW", "BRV(N)"], "h")),
 "s": spread(("*", "s"), (["TBW", "BRV(N)"], "h")),
 "z": spread(("*", "c/s"), (["WAY"], "c/y"), (["KBY", "NKR", "MGD", "TBW", "BRV(N)", "BTW"], "c"),
             (["TBI", "TVK", "NBL"], "c/s/y")),
 "y": spread(("*", "c"), (["WAY", "KBY", "TBW", "TBI"], "c/y")),
 "r": spread(("*", "r/dr"), (G1, "r"), (["TVK", "NBL"], "r"), (["NBB"], "r/tr")),
 "nr": spread(("*", "dr"), (["NBB"], "tr")),
 "l": spread(("*", "l"), (["TBI"], "l/y")),
 "R": spread(("*", "∅")),
 "k": spread(("*", "k/kw"), (["KBY", "NKR", "NDR"], "x/xw"), (["TKM", "TVK", "NBL", "NVT(B)", "SLV", "BUA", "SQQ",
             "NBB"], "x"), (["NMN", "LVN", "LAU", "VBL"], "k"), (["ONO"], "k,x"),
             (["NVS", "GOD", "BRV(M)", "DGT", "SQN"] + G8, "ʔ"), (["SAV", "KRL"], "ʔ/x"), (["LBS"], "∅")),
 "ŋk": spread(("*", "q"), (G1 + ["NMS", "WDN", "LUT", "NDR"], "q/qw"), (G6 + G7, "k")),
 # p. 185
 "m": spread(("*", "m"), (["WDN"], "m/∅")),
 "n": spread(("*", "n")),
 "ñ": spread(("*", "n"), (G1, "y"), (["WAY", "KBY"], "y/∅")),
 "ŋ": spread(("*", "g")),
 "mw": spread(("*", "g"), (G1 + ["NMS", "WDN", "LUT"], "gw"), (["NDR"], "gw/m"), (["NMM"], "g/gw")),
 "w": spread(("*", "w")),
 "q": spread(("*", "∅/y"), (["WAY", "KBY", "LBS", "DGT"], "∅")),
 "∅": spread(("*", "y"), (["WAY", "KBY", "LBS", "DGT"], "∅"), (["BUA"], "y/∅")),
}
PAGE = dict.fromkeys(["a", "e", "i", "o", "u", "v", "b", "bw", "p", "pw"], "183")
PAGE.update(dict.fromkeys(["t", "nt", "j", "s", "z", "y", "r", "nr", "l", "R", "k", "ŋk"], "184"))
PAGE.update(dict.fromkeys(["m", "n", "ñ", "ŋ", "mw", "w", "q", "∅"], "185"))
FOOT = {"a": "20, 30, 33, 34, 39", "e": "31, 32, 38", "i": "20, 29, 31, 32, 40", "o": "38", "u": "19, 29",
        "b": "16", "bw": "16", "p": "16, 25", "pw": "16, 25", "t": "4, 5, 6, 10, 22, 37", "nt": "7, 8, 11",
        "j": "9", "s": "9", "z": "24, 26, 41", "y": "41", "r": "23", "nr": "17", "l": "36", "k": "2, 12, 13, 14",
        "ŋk": "3, 15", "m": "35", "ñ": "27, 28", "mw": "1", "q": "18", "∅": "18"}
IPA = {"v": "β", "c": "ð", "j": "t͡ʃ", "d'": "d͡ʒ", "y": "j", "g": "ŋ", "gw": "ŋʷ", "q": "ɡ", "qw": "ɡʷ", "kw": "kʷ",
       "xw": "xʷ", "dr": "ⁿr", "ā": "aː"}
# Table 16 (pp. 187-188), read for the palatalization rules only: where rules 4-8 apply to all eligible forms.
R4 = {"NKR", "TBW", "BRV(N)", "BTW", "TBI", "NLE", "NDR", "ONO", "TVK", "LAU", "VBL"}
R5 = {"TBW", "BRV(N)", "TVK"}
R8 = {"TBW", "BRV(N)"}
KEY = {
 1: "*mw > *ŋw > ŋ", 2: "*k > k/kw /_a,e (lex)", 3: "*ŋk > q/qw /_a,e (lex)", 4: "*t > j/_i", 5: "*t > j/_e",
 6: "*t > s _i,e", 7: "*nt > d'/_i", 8: "*nt > d'/_u", 9: "*s > h", 10: "*t > ʔ", 11: "*nt > t", 12: "*k > x",
 13: "*k > ʔ", 14: "*k > ∅", 15: "*ŋk > k", 16: "*b > p", 17: "*nr > tr", 18: "*∅ > y/#_a", 19: "*u > ∅/m_",
 20: "*i > ∅/t_l,n", 21: "*a > ā/_(C)V(C)V##", 22: "*t > d (E.F.Ap.Pren.)", 23: "*r > dr (E.F.Ap.Pren.)",
 24: "*z > s (E.F.Ap.Pren.)", 25: "*p, *pw > b", 26: "*z > s (lex or PAN *j)", 27: "*ñ > y", 28: "*ñ > n",
 29: "*i, *u > ∅/a_CV#", 30: "*à > e/_i", 31: "*èi > i", 32: "*èi > e", 33: "*a > o/ó_", 34: "*a > ā/ó_",
 35: "*m > ∅/_ù", 36: "*l > y/_a,o", 37: "*t > s/_i (early pal.)", 38: "*e, *o > a/á", 39: "*a > e, o /_é, ó",
 40: "*i > y/á_a", 41: "*z > y (lex)"}
EFAP = ("#_ (common nouns)", "Eastern Fijian Apical Prenasalisation, by which *t, *r and *c became d, dr and s 'in "
        "initial position in many common nouns' (Geraghty 1986: 290; 1983: 74-96).")


def rule(n):
    return f"Key to sound changes (p. 186), no. {n}: '{KEY[n]}'."


def plan(col, abbr, reflexes):
    """-> list of (pcp phoneme, reflex in Geraghty's script, environment, status, note, parent_lect_id)"""
    out = []
    first = reflexes[0]

    def add(par, ref, env="elsewhere", status="regular", note="", pl=""):
        out.append((par, ref, env, status, note, pl))
    for ref in reflexes:
        main = ref == first
        if col == "a":
            if ref == "a": add("a", "a")
            elif ref == "ā":
                if abbr in G1: add("a", "ā", "_(C)V(C)V#", note=rule(21) + " The foot of the column prints 20, "
                                   "which is the loss of *i; 21 is meant.")
                else: add("a", "ā", "ó_", note=rule(34) + " In the sequence *oa (§4.5.5).")
            elif ref == "e": add("a", "e", "_i; _é", note=rule(30) + " " + rule(39) + " The first is Western Fijian "
                                 "a-raising (§4.5.3); the second belongs to the development of *a(R,q)e (§4.5.1).")
            elif ref == "o": add("a", "o", "ó_; _ó", note=rule(33) + " " + rule(39))
            elif ref == "∅": add("a", "∅", "conditions unknown", note="None of the changes numbered at the foot of "
                                 "the column (20, 30, 33, 34, 39) deletes *a; see §4.5.6 on the loss of initial *a-.")
        elif col == "e":
            if ref == "e": add("e", "e")
            elif ref == "i": add("e", "i", "_i (unstressed)", note=rule(31) + " Monophthongization of *ei (§4.5.4).")
            elif ref == "a": add("e", "a", "á_", note=rule(38) + " In *a(R,q)e (§4.5.1); the environment after "
                                 "'a/á' is not printed.")
        elif col == "i":
            if ref == "i": add("i", "i")
            elif ref == "∅":
                if abbr in ("WAY", "KBY"): add("i", "∅", "t_[l,n]", note=rule(20))
                else: add("i", "∅", "a_CV#", note=rule(29) + " The diphthong ai (§4.5.2).")
            elif ref == "e": add("i", "e", "è_", note=rule(32) + " Monophthongization of *ei (§4.5.4).")
            elif ref == "y": add("i", "y", "á_a", note=rule(40))
        elif col == "o":
            if ref == "o": add("o", "o")
            else: add("o", "a", "á_", note=rule(38) + " In *a(R,q)o (§4.5.1); the environment after 'a/á' is not "
                      "printed.")
        elif col == "u":
            if ref == "u": add("u", "u")
            elif abbr in ("WAY", "KBY"): add("u", "∅", "m_ (unstressed)", note=rule(19) + " §2.3 (p. 24): "
                                             "'u:∅/m_ [-stress]'.")
            else: add("u", "∅", "a_CV#", note=rule(29) + " The diphthong au (§4.5.2).")
        elif col == "v":
            add("v", "v")
        elif col in ("b", "bw", "p", "pw"):
            par, pl = {"b": ("b", ""), "p": ("p", ""), "bw": ("bʷ", "poc"), "pw": ("pʷ", "poc")}[col]
            n = ""
            if col in ("b", "bw") and ref == "p": n = rule(16)
            if col in ("p", "pw") and ref == "b": n = rule(25)
            if col in ("p", "pw") and ref == "p":
                n = ("The fortis stop is kept apart from *b here: 'kept apart from *p only in PFJ, on evidence "
                     "from parts of eastern Fiji' (Geraghty 1986: 292)." if abbr != "NBB" else
                     "Nabalebale has p for all four labial stops (" + KEY[16] + ").")
            if pl: n += (" PEO *" + col + " has no counterpart in Geraghty's (1986) PCP, so the row is stated "
                         "against POc *" + par + ".")
            add(par, ref, note=n.strip(), pl=pl)
        elif col == "t":
            if ref == "t":
                if main: add("t", "t")
                else: add("t", "t", "conditions unknown", note="Table 15 gives the glottal stop first and t second; "
                          "§2.3 has only 't:ʔ' for this communalect, so where t is kept is not stated.")
            elif ref == "j":
                env = "_[i,e]" if abbr in R5 else "_i"
                n = rule(4) + (" " + rule(5) if abbr in R5 else "")
                n += (" Table 16 (p. 187) marks " + ("both changes" if abbr in R5 else "the first, not the second,")
                      + " for this communalect.")
                if abbr in ("TBW", "BRV(N)"):
                    n += " §2.3 (p. 26) has the synchronic rules 't:j/_u' and 't:s/_i,e' for it."
                add("t", "j", env, note=n)
            elif ref == "s": add("t", "s", "_[i,e] (later palatalization)", note=rule(6) + " §2.3 (p. 26): "
                                 "'t:s/_i,e'. The table gives j, s and h for *t without saying which words have which.")
            elif ref == "h": add("t", "h", "_i (early palatalization)", note=rule(37) + " " + rule(9) +
                                 " Early palatalization in Nadrogā (§4.5.9): *t > s before *i, early enough to go "
                                 "on to h with *s.")
            elif ref == "ʔ": add("t", "ʔ", note=rule(10))
            elif ref == "d": add("t", "d", EFAP[0], note=rule(22) + " " + EFAP[1])
        elif col == "nt":
            if ref == "d": add("d", "d")
            elif ref == "d'":
                env = "_[i,u]" if abbr in R8 else "_i"
                add("d", "d'", env, note=rule(7) + (" " + rule(8) if abbr in R8 else "") +
                    " Geraghty's d' is the palatalized d, [ndʒ] (p. 182).")
            elif ref == "t": add("d", "t", note=rule(11))
        elif col in ("j", "s"):
            add(col, ref, note=(rule(9) if ref == "h" else "") +
                (" 'In PFJ *j merges with *s' (Geraghty 1986: 298)." if col == "j" else ""))
        elif col == "z":
            WIT = abbr in ("TBI", "NLE", "GOD")
            if ref == "c":
                add("c", "c", note="PEO *z of 1983 covers PCP *c and *z of Geraghty (1986), which have the same "
                    "reflex c in most communalects (1986: 297).")
                add("z", "c", note="PEO *z of 1983 covers PCP *c and *z of Geraghty (1986: 297): 'in most Fijian "
                    "communalects it is regularly realised as c, which is also the reflex of PCP *c'." +
                    (" Here beside s." if WIT else ""))
            elif ref == "s":
                if WIT:
                    add("z", "s", "conditions unknown", note=rule(26) + " One of the four communalects (Nalea, "
                        "Tubai, Vunaqumu, Gone Dau) where PCP *z 'is realised as s (or y/∅), not c' (Geraghty 1986: "
                        "297-298). Table 15 gives c first.")
                if abbr not in G1:
                    add("c", "s", EFAP[0], note=rule(24) + " " + EFAP[1])
                elif not WIT:
                    add("c", "s", "conditions unknown", note=rule(26))
            elif ref == "y":
                add("c", "y", "conditions unknown", "sporadic", rule(41) + " 'y is also a fairly common sporadic "
                    "reflex of PFJ *c' (Geraghty 1986: 298).")
        elif col == "y":
            if ref == "c": add("y", "c", note="'PCP *y is realised as PFJ *c' (Geraghty 1986: 304).")
            else: add("y", "y", "conditions unknown", "sporadic", "The foot of the column refers to no. 41, '" +
                      KEY[41] + "'.")
        elif col == "r":
            if ref == "r": add("r", "r")
            elif ref == "dr": add("r", "dr", EFAP[0], note=rule(23) + " " + EFAP[1])
            elif ref == "tr": add("r", "tr", EFAP[0], note=rule(23) + " " + rule(17) + " " + EFAP[1])
        elif col == "nr":
            add("dr", ref, note=rule(17) if ref == "tr" else "")
        elif col == "l":
            if ref == "l": add("l", "l")
            else: add("l", "y", "_[a,o]", note=rule(36))
        elif col == "R":
            pass  # PCP has no *R: the row POc *R > ∅ stands on Proto-Central Pacific
        elif col in ("k", "ŋk"):
            par = "k" if col == "k" else "ɡ"
            lab = {"kw": "k", "xw": "x", "qw": "q"}
            if ref in lab:
                add(par + "ʷ", ref, note=(rule(2) if col == "k" else rule(3)) + (" " + rule(12) if ref == "xw" else "")
                    + " The lexically conditioned labiovelar of 1983 is the PCP phoneme *" +
                    ("kw" if col == "k" else "qw") + " of Geraghty (1986: 305-306).")
            else:
                n = {"x": rule(12), "ʔ": rule(13), "∅": rule(14)}.get(ref, "")
                if col == "ŋk" and ref == "k": n = rule(15)
                env, st = "elsewhere", "regular"
                if "," in "".join(reflexes) or (len(reflexes) > 1 and not any(r in lab for r in reflexes)):
                    # k,x (Ono) and ʔ/x (Savusavu, Koroalau)
                    if abbr == "ONO":
                        env = "conditions unknown"; n += " Table 15 prints 'k,x'; §2.3 (p. 29): 'k:k,x'."
                    elif ref == "x":
                        env = "close to a glottal stop"
                        n += (" 'k is realized as glottal stop, except when close to a glottal stop (the realization "
                              "of t), where it is realized as a velar fricative' (p. 36).")
                add(par, ref, env, st, n.strip())
                if not any(r in lab for r in reflexes) and ref == first and abbr != "ONO":
                    add(par + "ʷ", ref, note="Composed: this communalect has 'no labiovelars' (§2.3), which 'means "
                        "that kw, qw, and gw are realized the same way as k, q, and g' (p. 24). " + n)
        elif col == "m":
            if ref == "m": add("m", "m")
            else: add("m", "∅", "_u (unstressed)", note=rule(35))
        elif col in ("n", "w"):
            add(col, ref)
        elif col == "ŋ":
            add("ŋ", ref)
        elif col == "ñ":
            if ref == "y": add("ñ", "y", note=rule(27) + " 'PCP *ñ survives in Western Fijian (n before u, y before "
                               "a)' (Geraghty 1986: 303), restated in the Proto-Fijian row.")
            elif ref == "n": add("ñ", "n", note=rule(28))
            else: add("ñ", "∅", "conditions unknown", note="No change at the foot of the column (27, 28) deletes *ñ.")
        elif col == "mw":
            if ref == "gw": add("ŋʷ", "gw", "elsewhere" if main else "conditions unknown",
                                note="The first step of no. 1, '" + KEY[1] + "': 'PCP *gw is the reflex of POC *mw' "
                                "(Geraghty 1986: 306).")
            elif ref == "g": add("ŋʷ", "g", "elsewhere" if main else "conditions unknown", note=rule(1))
            else: add("ŋʷ", "m", "conditions unknown", note="No change in the key gives m for *mw.")
        elif col == "q":
            if ref == "∅": add("ʔ", "∅")
            else: add("ʔ", "y", "#_a", note=rule(18) + " After the loss of *q.")
        elif col == "∅":
            if ref == "y": add("∅", "y", "#_a", note=rule(18) + " Prothesis before initial *a (§4.5.6)." +
                               (" Table 15 prints 'y/∅': beside y, no prothesis." if "∅" in reflexes else ""))
            # a lone ∅ (no prothesis) is not a row
    return out


n_rows = 0
for col, cells in T.items():
    for abbr in ORDER:
        cell = cells[abbr]
        reflexes = cell.replace(",", "/").split("/")
        for par, ref, env, status, note, pl in plan(col, abbr, reflexes):
            child = IPA.get(ref, ref)
            printed = f"PEO *{col if col != '∅' else '∅/#_a'} : {abbr} {cell}"
            base = (f"Table 15, 'Direct reflexes of PEO phonemes in Fiji' (p. {PAGE[col]}), column PEO *"
                    f"{col if col != '∅' else '∅/#_a'}, row {abbr}"
                    + (f"; sound changes at the foot of the column: {FOOT[col]}" if col in FOOT else "") + ". "
                    + ("'I have attempted to list the most common reflex first' (p. 182). " if len(reflexes) > 1 else ""))
            b.corr(ID[abbr], par, child, env, PAGE[col], base + note, status=status, derivation="composed",
                   as_printed=printed, source_form=ref if ref != child else "", decision=D, locator="Table 15")
            if pl:
                b.t["correspondences"][-1]["parent_lect_id"] = pl
            n_rows += 1

b.dec(D,
      "Geraghty (1983) Table 15 states the reflexes of Proto-Eastern Oceanic, which is not a node. Against what are "
      "the 38 communalects stated, and which lects carry them?",
      "Against Proto-Central Pacific (the user's comment on decision geraghty1983-communalects: 'listing them under "
      "PCP'), composed: PEO *nt, *nr, *ŋk, *q, *mw are PCP *d, *dr, *ɡ (q), *ʔ, *ŋʷ (gw); PEO *z is PCP *c and *z, "
      "which Geraghty (1986: 297) separates (s in Tubai, Nalea and Gone Dau is the reflex of *z; s elsewhere is *c "
      "under Eastern Fijian Apical Prenasalisation); the lexically conditioned kw, qw of 1983 are PCP *kw, *qw, and a "
      "communalect with 'no labiovelars' has the reflex of *k, *q for them. PEO *bw and *pw have no PCP counterpart "
      "and are stated against POc (parent_lect_id poc); PEO *R (zero everywhere) is not entered, since the row "
      "POc *R > ∅ stands on PCP. Environments are those of the key to sound changes (p. 186); a reflex that no "
      "numbered change accounts for has 'conditions unknown'. 37 dialects and Gone Dau (a Glottolog language), with "
      "new language nodes Fijian, Namosi-Naitasiri-Serua, Lauan and Lomaiviti and a dialect node Kadavu; a "
      "communalect has a Glottocode only where Glottolog 5.4 has a languoid of the same name (11) or it is one of "
      "the three Kadavu communalects. Reflexes in IPA as in the Nadrogā inventory of Lynch et al. (2002).",
      "1. Proto-Fijian as parent_id (now a proposed parent of each, like Western Fijian). 2. Enter Table 16 "
      "(pp. 187-188), the percentage of eligible forms each change affects in 36 communalects: read here only for "
      "which communalects have the palatalization changes 4, 5 and 8; its rows for changes 12 and 25 did not agree "
      "with Table 15 as read from the image, so nothing else was taken from it. 3. Read chapters 3 and 4 for the "
      "conditions that the key abbreviates and for examples (none are entered). 4. Assign the Vanua Levu and Viti "
      "Levu communalects to Glottolog's dialects (West, Central, Northeast, Southeast Vanua Levu; Northeast, "
      "Southeast Viti Levu; Northwest Viti Levu; Nadrogaa) after chapters 6-7; the existing Nadrogā lect "
      "(nadr1235, Lynch et al. 2002) has h for *s like Tubaniwai and Baravi (Nadrogā) and may be one of them. "
      "5. Write the prenasalized stops ᵐb ⁿd ᵑɡ. 6. Enter PEO *bw, *pw against a Proto-Eastern Oceanic with "
      "phonemes instead of POc.",
      "182-190")

BATCH_MD = f"""# geraghty1983-communalects

Geraghty (1983), Table 15 (pp. 183-185): the direct reflexes of 30 Proto-Eastern Oceanic phonemes in 38 Fijian
communalects, {n_rows} rows, composed onto Proto-Central Pacific. Decision `geraghty1983-communalects` carries the
user's comment 'Do enter the communalects when ready, listing them under PCP'.

Read from page images (the scan's OCR is unusable for tables): Table 15 at 230 dpi, the key (p. 186) at 190 dpi,
Table 1 (pp. 21-22) and §2.3 (pp. 24-38) at 105 dpi, the abbreviations (pp. xx-xxiv) at 110 dpi.

- 43 lect rows: language nodes Fijian, Namosi-Naitasiri-Serua, Lauan, Lomaiviti; dialect node Kadavu; Gone Dau
  (language); 37 dialects. Western Fijian (`west2519`) exists.
- Table 15 prints BRV and NVT twice each: Baravi (Nadrogā) and Baravi (Macuata), Navatu (Bua) and Navatu
  (Cakaudrove), by their place in the table.
- The foot of column *a prints change 20 (loss of *i); 21 (*a > ā) is meant.
- Not entered: Table 16 (percentages), Table 17 (changes shared by pairs), the examples and conditions of chapters
  3-4, PEO *R, the vowel length of the reflexes other than ā.
- 23 lects have no Glottocode (Glottolog 5.4 has no languoid of the name).
"""
if __name__ == "__main__":
    write(BATCH, b.t, BATCH_MD)
    print("rows", n_rows)
