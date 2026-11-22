_v = ["i","y","u","e","ø","o","ɛ","ə","ɔ","a"]
LANG = dict(id="iaai1238", name="Iaai", glottocode="iaai1238", iso="iai", parent="pnc",
            notes="Loyalties subgroup of New Caledonian (with Nengone and Drehu); central Ouvéa. Sketch abstracted by John Lynch, based mainly on Ozanne-Rivierre (1976), with data from Tryon (1968b) and Ozanne-Rivierre (1984) (Lynch et al. 2002: 776-791). The contrast between velarised and simple bilabials is neutralised (as a simple bilabial) before rounded vowels and /a/; /ɛ/ and /a/ are neutralised as [ɛ] after /ü ɸ β/ (pp. 776-777).",
            page="776-777")
PH = [
 ("p","","C","",""),("t̪","t","C","","Dental."),("ʈ","ṭ","C","","Printed with a subscript dot."),("t͡ʃ","tʃ","C","",""),("k","","C","",""),
 ("bʷ","","C","","Velarised bilabial."),("b","","C","",""),("d̪","d","C","","Dental."),("ɖ","ḍ","C","",""),("d͡ʒ","dʒ","C","",""),("ɡ","g","C","",""),
 ("ʍ","w̥","C","","A voiceless labio-velar spirant."),("ɸ","","C","","A voiceless labio-palatalised spirant."),("f","","C","","Labio-dental."),
 ("θ","","C","","Dental."),("s","","C","","Alveolar."),("ʃ","","C","",""),("x","","C","",""),("h","","C","",""),
 ("w","","C","",""),("β","","C","",""),("ð","","C","","Dental."),
 ("m̥ʷ","","C","","Not word-final."),("m̥","","C","",""),("n̪̊","n̥","C","","Dental."),("ɳ̊","ṇ̥","C","",""),("ɲ̊","ñ̥","C","",""),("ŋ̊","","C","",""),
 ("mʷ","","C","","Not word-final."),("m","","C","",""),("n̪","n","C","","Dental."),("ɳ","ṇ","C","",""),("ɲ","ñ","C","",""),("ŋ","","C","",""),
 ("ɭ̊","ḷ̥","C","",""),("ɭ","ḷ","C","",""),("ɾ","","C","","Alveolar; does not occur word-initially."),
] + [(v,"ü" if v=="y" else "","V","","") for v in _v] + [(v+"ː","","V","","All vowels occur both short and long.") for v in _v]
AL = [
 ("ɔ","œ","after a non-velarised labial","777","A rounded allophone."),
 ("p","b","_# before a vowel-initial word","777","Word-final voiceless stops are voiced if the following word is vowel-initial (/tep aːŋ/ > /teb aːŋ/ 'this rat')."),
 ("t̪","d̪","_# before a vowel-initial word","777",""),("ʈ","ɖ","_# before a vowel-initial word","777",""),
 ("t͡ʃ","d͡ʒ","_# before a vowel-initial word","777",""),("k","ɡ","_# before a vowel-initial word","777",""),
]
