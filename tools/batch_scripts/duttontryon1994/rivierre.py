#!/usr/bin/env python3
"""Rivierre (1994), Contact-induced phonological complexification in New Caledonia.

In Dutton & Tryon (eds.), Language contact and change in the Austronesian world, 497-522. §3: the Caac consonant
system of Hollyman (1962) (Table 1, p. 508), new lect Caac; PNC > Pwapwâ, Pwaamei and Kone (Haveke) initial oral
stops (Table 4, p. 513, with pp. 514-519); the Kone (Haveke) consonant chart including loans (p. 519) as Haveke's
sourced inventory.
"""
from common import Batch, write, chapter, CONSULTED

S = "rivierre1994"
H = "hollyman1962"
b = Batch(S)
b.t["sources"] += [
    chapter(S, "Rivierre, Jean-Claude", "Contact-induced phonological complexification in New Caledonia", "497-522",
            CONSULTED + "§2: Cèmuhî tone patterns of loanwords (tone levels, low-tone loans, marginalisation and "
            "nativisation). §3.1: the Far North languages, which neutralise the aspirate/plain contrast between "
            "vowels (Caac, Table 1, after Hollyman 1962; Table 2; Bondé 1893 vs 1965, Table 3), and loans that "
            "reintroduce aspirates and voiceless stops there. §3.2: the Kone area (Pwapwâ, Pwaamei, Kone dialects "
            "Bwatoo, Haeke, Haveke, Hmwaeke, Hmwaveke, Vamale): the northern 'double shift', PNC > PAP, PAM, KON "
            "initial oral consonants (Table 4, p. 513), each system's gaps (pp. 514-515), p- and k- borrowed back in "
            "Kone, voiced and voiceless spirants and aspirates spread by loans, and the Haveke chart (p. 519). "
            "Language abbreviations after Hollyman (1986), p. 520."),
    dict(id=H, author="Hollyman, K. J.", year="1962", title="Première esquisse de la phonologie du caaqac",
         kind="grammar", pub_type="article", container_title="Proceedings of the Linguistic Society of New Zealand",
         volume="5", pages="41-51",
         notes="Bibliographic details from the reference list of Rivierre (1994: 521); not consulted directly. The "
               "Caac consonant table by position (initial, intervocalic, final) is read in Rivierre (1994: 508)."),
]

b.t["sources"].append(dict(
    id="hollyman1986", author="Hollyman, K. J.", year="1986",
    title="Les emprunts polynésiens dans les langues de la Nouvelle-Calédonie et des îles Loyauté",
    kind="comparative", pub_type="article", container_title="Cahiers du LACITO", volume="1", pages="67-88",
    place="Paris", publisher="Centre National de la Recherche Scientifique",
    notes="Bibliographic details from the reference lists of Rivierre (1994: 521) and Ozanne-Rivierre (1994: 548); "
          "not consulted directly. Source of the three-letter language abbreviations used by Rivierre (1994: 520)."))

CAAC, PAP, PAM, HAV = "caac1237", "pwap1237", "pwaa1237", "have1241"
b.t["lects"].append(dict(
    id=CAAC, name="Caac", alt_names="Caaac;Caaqac;CAC", type="language", glottocode="caac1237", iso639_3="msq",
    parent_id="pnc", latitude="-20.4114", longitude="164.578", region="Far North of New Caledonia (Pouébo area)",
    notes="A Far North language of New Caledonia, north of the isogloss beyond which intervocalic consonants are "
          "neutralised (Rivierre 1994: 509, Map 1). Consonants only, from Hollyman (1962) as tabulated by Rivierre "
          "(1994: 508, Table 1); no vowels are given. Finally only p, t, c, k and m, n, ɲ, ŋ occur (Table 1). Coordinates from Glottolog 5.4."))

D = "rivierre1994-kone"
T4 = "Table 4 (p. 513), initial position: "
# Rivierre's PNC symbol -> the sheet's PNC phoneme (Ozanne-Rivierre 1992's spelling)
PNC = [("pp", "pp", "*pp-"), ("tt", "t̲t̲", "*t̲t̲-"), ("ṭṭ", "ṭṭ", "*ṭṭ-"), ("ss", "cc", "*cc"), ("kk", "kk", "*kk-"),
       ("qq", "qq", "*qq-"), ("p", "p", "*p-"), ("t", "t̲", "*t̲-"), ("ṭ", "ṭ", "*ṭ-"), ("s", "c", "*c-"),
       ("k", "k", "*k-"), ("q", "q", "*q-")]
ROWS = {
    PAP: ["pʰ", "cʰ", "tʰ", "tʰ", "s", "x", "p", "c", "t", "t", "c", "k"],
    PAM: ["f", "s", "ɬ", "tʰ", "s", "h", "p", "c", "t", "t", "ʝ", "k"],
    HAV: ["f", "θ", "tʰ", "tʰ", "θ", "x", "v", "c", "t", "t", "ð", "ɣ"],
}
PRINTED = {
    PAP: ["ph", "ch", "th", "th", "s", "x", "p", "c", "t", "t", "c", "k"],
    PAM: ["f", "s", "hl", "th", "s", "h", "p", "c", "t", "t", "y", "k"],
    HAV: ["f", "s", "th", "th", "s", "x", "v", "c", "t", "t", "y", "γ"],
}
NOTE = {
    PAP: "Pwapwâ, 'the most conservative of these languages' after the double shift; 'present-day ch derives from "
         "*t̲t̲-', *kk ch > s and *qq [kʰ] > x (p. 514).",
    PAM: "Pwaamei: 'near total stability of the non-aspirates (only (*k-) c > y while *t̲- > c)'; aspirates weakened: "
         "*qq [kʰ] > h, *kk, *t̲t̲ [cʰ] > s, *ṭṭ [tʰ] > hl, *pp [pʰ] > f; only *cc th remains an occlusive (p. 514). "
         "y is the voiced palatal spirant (p. 517); hl the voiceless lateral.",
    HAV: "Kone (KON column), entered on Haveke, whose chart (p. 519) has θ and ð where the KON column has s and y: "
         "Rivierre notes the dialectal variant ð-/θ- 'as in the Kone coastline dialects' (p. 517). Kone weakened "
         "the non-aspirates 'much more' than Pwaamei, spirantising labial and velar stops (p. 515).",
}
for lect in (PAP, PAM, HAV):
    for (ph, rp, ap), ch, pr in zip(PNC, ROWS[lect], PRINTED[lect]):
        note = T4 + NOTE[lect] + f" Rivierre's {ap} is the sheet's PNC *{ph}."
        b.corr(lect, ph, ch, "#_", "513-517", note, derivation="", decision=D, as_printed=pr)
b.corr(HAV, "p", "p", "#_", "516", "§3.2.3: 'p- and k-, which became respectively v- and y- in Kone have been easily "
       "re-introduced in initial position'; all words with p- but one come from Pwaamei or Pwapwâ (pad 'to warm up', "
       "pom 'butterfly', piu 'star' re-introduced in Haveke).", status="loan-stratum", derivation="", decision=D)
b.corr(HAV, "k", "k", "#_", "516", "§3.2.3: k- borrowed back in Kone, from Polynesian, the northern and the "
       "southern mainland (kathia 'leprosy', kele 'the strangles', kuha 'gun').", status="loan-stratum",
       derivation="", decision=D)

# Haveke inventory (p. 519)
HV = [
    ("m̥ʷ", "hmw", "bilabial", "nasal", "voiceless"), ("m̥", "hm", "bilabial", "nasal", "voiceless"),
    ("n̥", "hn", "alveolar", "nasal", "voiceless"), ("ɲ̊", "hɲ", "palatal", "nasal", "voiceless"),
    ("mʷ", "mw", "bilabial", "nasal", "voiced"), ("m", "m", "bilabial", "nasal", "voiced"),
    ("n", "n", "alveolar", "nasal", "voiced"), ("ɲ", "ɲ", "palatal", "nasal", "voiced"),
    ("ŋ", "ŋ", "velar", "nasal", "voiced"),
    ("ᵐbʷ", "mbw", "bilabial", "prenasalized-plosive", "voiced"), ("ᵐb", "mb", "bilabial", "prenasalized-plosive", "voiced"),
    ("ⁿd", "nd", "alveolar", "prenasalized-plosive", "voiced"), ("ᶮɟ", "ɲj", "palatal", "prenasalized-plosive", "voiced"),
    ("ᵑɡ", "ŋg", "velar", "prenasalized-plosive", "voiced"),
    ("pʰʷ", "phw", "bilabial", "plosive", "voiceless"), ("pʰ", "ph", "bilabial", "plosive", "voiceless"),
    ("tʰ", "th", "alveolar", "plosive", "voiceless"), ("cʰ", "ch", "palatal", "plosive", "voiceless"),
    ("kʰ", "kh", "velar", "plosive", "voiceless"),
    ("pʷ", "pw", "bilabial", "plosive", "voiceless"), ("p", "p", "bilabial", "plosive", "voiceless"),
    ("t", "t", "alveolar", "plosive", "voiceless"), ("c", "c", "palatal", "plosive", "voiceless"),
    ("k", "k", "velar", "plosive", "voiceless"),
    ("vʷ", "vw", "labiodental", "fricative", "voiced"), ("w", "w", "labial-velar", "approximant", "voiced"),
    ("v", "v", "labiodental", "fricative", "voiced"), ("l", "l", "alveolar", "lateral-approximant", "voiced"),
    ("ð", "ð", "dental", "fricative", "voiced"), ("ɣ", "γ", "velar", "fricative", "voiced"),
    ("fʷ", "fw", "labiodental", "fricative", "voiceless"), ("ʍ", "hw", "labial-velar", "approximant", "voiceless"),
    ("f", "f", "labiodental", "fricative", "voiceless"), ("ɬ", "hl", "alveolar", "lateral-fricative", "voiceless"),
    ("θ", "θ", "dental", "fricative", "voiceless"), ("x", "x", "velar", "fricative", "voiceless"),
    ("h", "h", "glottal", "fricative", "voiceless"),
]
for ipa, sym, place, manner, voicing in HV:
    note = ""
    if ipa in ("ð", "θ"):
        note = "In the palatal column of the chart (Kone y-, s- elsewhere, p. 517); placed as dental."
    if ipa in ("t", "tʰ", "ⁿd", "n", "n̥", "l", "ɬ"):
        note = ("The coronal column; after the double shift the orders are 'labial, retroflex, palatal and velar' "
                "(p. 513).")
    b.ph(HAV, ipa, "C", place, manner, voicing, sym=sym, page="519", notes=note)

# Caac inventory (Hollyman 1962 via Rivierre 1994: 508)
CA = [("p", "bilabial", "plosive", "voiceless", "p"), ("pʰ", "bilabial", "plosive", "voiceless", "ph"),
      ("pʷ", "bilabial", "plosive", "voiceless", "pw"), ("pʰʷ", "bilabial", "plosive", "voiceless", "phw"),
      ("t", "alveolar", "plosive", "voiceless", "t"), ("tʰ", "alveolar", "plosive", "voiceless", "th"),
      ("c", "palatal", "plosive", "voiceless", "c"), ("cʰ", "palatal", "plosive", "voiceless", "ch"),
      ("k", "velar", "plosive", "voiceless", "k"), ("kʰ", "velar", "plosive", "voiceless", "kh"),
      ("m", "bilabial", "nasal", "voiced", "m"), ("m̥", "bilabial", "nasal", "voiceless", "hm"),
      ("ᵐb", "bilabial", "prenasalized-plosive", "voiced", "mb"), ("mʷ", "bilabial", "nasal", "voiced", "mw"),
      ("m̥ʷ", "bilabial", "nasal", "voiceless", "hmw"), ("ᵐbʷ", "bilabial", "prenasalized-plosive", "voiced", "mbw"),
      ("n", "alveolar", "nasal", "voiced", "n"), ("n̥", "alveolar", "nasal", "voiceless", "hn"),
      ("ⁿd", "alveolar", "prenasalized-plosive", "voiced", "nd"), ("ɲ", "palatal", "nasal", "voiced", "ɲ"),
      ("ɲ̊", "palatal", "nasal", "voiceless", "hɲ"), ("ᶮɟ", "palatal", "prenasalized-plosive", "voiced", "ɲj"),
      ("ŋ", "velar", "nasal", "voiced", "ŋ"), ("ᵑɡ", "velar", "prenasalized-plosive", "voiced", "ŋg")]
VIA = dict(source=H, via_source_id=S, via_page="508")
for ipa, place, manner, voicing, sym in CA:
    b.ph(CAAC, ipa, "C", place, manner, voicing, sym=sym, page="", **VIA,
         via_note="Rivierre's Table 1 gives Hollyman's consonants by position; the initial column is the inventory.")
INTER = [("p", "v"), ("pʰ", "v"), ("pʷ", "w"), ("pʰʷ", "w"), ("t", "r"), ("tʰ", "r"), ("c", "j"), ("cʰ", "j"),
         ("k", "x"), ("kʰ", "x"), ("m̥", "m"), ("m̥ʷ", "mʷ"), ("n̥", "n"), ("ɲ̊", "ɲ")]
for ph, al in INTER:
    b.allo(CAAC, ph, al, "V_V (neutralised)", "", "Table 1, intervocalic column: 'a distinction is made for both oral "
           "and nasal consonants between aspirates and non-aspirates in the word-initial position, but this "
           "distinction is not upheld for the intervocalic position', which has voiced spirants and plain nasals "
           "(Rivierre 1994: 509). Printed y for j.", source=H, via_source_id=S, via_page="508-509")
b.dec(D, "How are Rivierre's (1994) PNC reflexes and the Kone chart entered?",
      "Table 4 as rows against PNC on Pwapwâ, Pwaamei and Haveke (Kone), initial position. Rivierre's *t̲, *ṭ, *c "
      "(and doubles) are the sheet's PNC *t, *ṭ, *s (Ozanne-Rivierre 1992's spelling): his dentals become palatals "
      "(*t̲- > c), his palatals retroflexes (*c- > t) and his retroflexes stay (*ṭ- > t). The KON column goes on "
      "Haveke with Haveke's θ, ð for KON s, y (chart, p. 519). The Haveke chart, loans included, is Haveke's sourced "
      "inventory. Pwaamei y = ʝ (a voiced palatal spirant, p. 517). Caac is added under PNC with Hollyman's "
      "(1962) consonants via Rivierre.",
      "Enter the KON column on a separate Kone lect, or as printed (s, y) on Haveke.", "508-519")
write("rivierre1994-newcaledonia", b.t, """# rivierre1994-newcaledonia

Rivierre, Jean-Claude. 1994. Contact-induced phonological complexification in New Caledonia. In Tom Dutton & Darrell T. Tryon (eds.), *Language contact and change in the Austronesian world*, 497-522. Berlin: Mouton de Gruyter. Generator: `tools/batch_scripts/duttontryon1994/rivierre.py`.

## Scope

- PNC initial oral consonants (singles and doubles) in Pwapwâ, Pwaamei and Kone (Haveke), Table 4 (p. 513); p- and k- borrowed back in Kone (p. 516). Decision `rivierre1994-kone`.
- Haveke's consonant chart including loans (p. 519) as its sourced inventory.
- New lect **Caac** (caac1237) under PNC with Hollyman's (1962) consonants (Table 1, p. 508) and their intervocalic and final neutralisation as allophones.

## Not entered

- Cèmuhî tone in loans (§2), Table 2 (Far North intervocalic consonants in general), Bondé 1893/1965 (Table 3), the loan lists (§3.1.3), the Pwapwâ and Pwaamei partial systems (pp. 514-515), the spread of v-, ɣ-, f-, ɬ- and aspirates by loans (§§3.2.4-3.2.5).
""")
