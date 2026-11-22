_short = ["i","ɨ","u","e","ə","o","ɛ","ʌ","ɔ","a","ĩ","ɨ̃","ũ","ɛ̃","ʌ̃","ɔ̃","ã"]
LANG = dict(id="xara1244", name="Xârâcùù", alt="Canala", glottocode="xara1244", iso="ane", parent="pnc",
            notes="South New Caledonian subgroup; Canala area, southern New Caledonia. Sketch abstracted by John Lynch from Moyse-Faurie (1995) (Lynch et al. 2002: 765-775). The oral/nasal contrast appears to be neutralised (as a nasal vowel) before a nasal or prenasalised stop, but only intra-morphemically (p. 765).",
            page="765-766")
PH = [
 ("pʷ","","C","",""),("p","","C","",""),("t","","C","",""),("c","","C","",""),("k","","C","",""),("kʷ","","C","",""),
 ("bʷ","","C","","All voiced stops are prenasalised."),("b","","C","",""),("d","","C","",""),("ɟ","j","C","","Printed j (decision lrc2002-readings)."),("ɡ","g","C","",""),("ɡʷ","gʷ","C","",""),
 ("f","","C","",""),("ʃ","","C","","Written ch."),("ç","","C","","Written s."),("x","","C","",""),("xʷ","","C","",""),("v","","C","",""),
 ("mʷ","","C","",""),("m","","C","",""),("n","","C","",""),("ɲ","ñ","C","",""),("ŋ","","C","",""),
 ("r","","C","","Lightly trilled; initially only in a handful of grammatical morphemes."),("l","","C","marginal","Only in borrowed words."),
 ("w","","C","",""),("j","y","C","",""),
] + [(v,"","V","","") for v in _short] + [(v+"ː","","V","","Each short vowel also occurs long (34 vocalic contrasts in all).") for v in _short]
AL = [
 ("bʷ","ᵐbʷ","","765","All voiced stops are prenasalised."),("b","ᵐb","","765",""),("d","ⁿd","","765",""),("ɟ","ᶮɟ","","765",""),("ɡ","ᵑɡ","","765",""),("ɡʷ","ᵑɡʷ","","765",""),
]
