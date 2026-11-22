"""Batch adelaar2005: the phonological histories in Adelaar (2005), 'Malayo-Sumbawan', section 4.

PMP > Proto-Chamic (after Thurgood 1999), > Proto-Balinese-Sasak-Sumbawa and its three languages
(after Mbete 1990, with Adelaar's own diphthongs), > Javanese, Sundanese, Madurese (after Nothofer 1975).
Run from the repository root: python3 tools/batch_scripts/adelaar2005/build.py
"""
import csv, io, sys, unicodedata
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
import build as B  # noqa: E402
OUT = ROOT / "data/incoming/adelaar2005"
N = lambda s: unicodedata.normalize("NFC", s)
A = "adelaar2005"
SOURCES = [
 dict(id=A, author="Adelaar, Alexander", year="2005", title="Malayo-Sumbawan", url_or_doi="https://doi.org/10.1353/ol.2005.0027", kind="comparative",
      pub_type="article", container_title="Oceanic Linguistics", volume="44", issue="2", pages="357-388",
      notes="Consulted directly on 22 November 2026: the phonological evidence (§2, pp. 360-372) and the fuller account of each language's phonological history (§4, pp. 373-377), entered with the changes as Adelaar lists them. Adelaar proposes a Malayo-Sumbawan subgroup with a Malayic-Chamic-BSS branch and Sundanese and Madurese as two other branches, excluding Javanese (pp. 357, 377-388); the subgroup is not entered as a node (decision adelaar2005-ms)."),
 dict(id="thurgood1999", author="Thurgood, Graham", year="1999", title="From ancient Cham to modern dialects: Two thousand years of language contact and change", kind="comparative",
      pub_type="book", place="Honolulu", publisher="University of Hawai'i Press", series="Oceanic Linguistics Special Publication 28",
      notes="Bibliographic details from the reference list of Adelaar (2005: 388), which prints the title as 'From ancient Chamic to modern dialects'. Not consulted directly: its Proto-Chamic developments are cited from Adelaar (2005: 373-374)."),
 dict(id="mbete1990", author="Mbete, Aron Meko", year="1990", title="Rekonstruksi protobahasa Bali-Sasak-Sumbawa", kind="comparative",
      pub_type="thesis", place="Jakarta", publisher="Universitas Indonesia dissertation",
      notes="Bibliographic details from the reference list of Adelaar (2005: 387). Not consulted directly: its developments from PMP to PBSS, Balinese, Sasak and Sumbawa are cited from Adelaar (2005: 374-375), who reinterprets the reflexes of PMP *-ay and *-aw (p. 359)."),
 dict(id="nothofer1975", author="Nothofer, Bernd", year="1975", title="The reconstruction of Proto-Malayo-Javanic", kind="comparative",
      pub_type="book", place="The Hague", publisher="Martinus Nijhoff", series="Verhandelingen van het KITLV 73",
      notes="Bibliographic details from the reference list of Adelaar (2005: 387). Not consulted directly: its developments from PMP to Javanese, Sundanese and Madurese are cited from Adelaar (2005: 375-376)."),
]
INH = dict(inherit="assumed-unchanged", inherit_source_id=A)
LECTS = [
 dict(id="pchamic", name="Proto-Chamic", alt_names="PC", type="proto-language", glottocode="cham1330", parent_id="pmp", clade="Chamic", inherit_page="373-374", **INH,
      notes="Developments from PMP after Thurgood (1999), as listed by Adelaar (2005: 373-374); ten of them are shared with Malayic. Not entered as rows: cluster reduction; nasals becoming homorganic to a following stop (a following voiced stop being lost); occasional homorganic nasal accretion between initial schwa and a following stop; occasional *j > ḷ (as printed); occasional reduction of the penultimate vowel (items 9, 10, 12, 15-16)."),
 dict(id="pbss", name="Proto-Balinese-Sasak-Sumbawa", alt_names="PBSS; Proto-Bali-Sasak-Sumbawa", type="proto-language", glottocode="bali1277", parent_id="pmp", clade="Balinese-Sasak-Sumbawa", inherit_page="374", **INH,
      notes="Developments from PMP after Mbete (1990), as listed by Adelaar (2005: 374); eight are shared with Malayic. Adelaar reconstructs the reflexes of PMP *-ay and *-aw as PBSS *-ey and *-ow, where Mbete has *-[i,e] and *-o, *-[i,o] (p. 359). Mbete distinguishes a Balinese branch and a Sasak-Sumbawa branch (p. 358); Proto-Sasak-Sumbawa is not entered. Not entered as a row: frequent homorganic nasal accretion between initial schwa and a following stop (item 12)."),
 dict(id="bali1278", name="Balinese", type="language", glottocode="bali1278", iso639_3="ban", parent_id="pbss", inherit_page="374", **INH,
      notes="Developments from PBSS after Mbete (1990), in Adelaar (2005: 374), with the reflexes of *r from his section 2 (p. 364). Old Balinese keeps *r and *h. Not entered as a row: *ə assimilated to the following vowel after the loss of *-r- (item 18)."),
 dict(id="sasa1249", name="Sasak", type="language", glottocode="sasa1249", iso639_3="sas", parent_id="pbss", inherit_page="375", **INH,
      notes="Developments from PBSS after Mbete (1990), in Adelaar (2005: 375); Sasak and Sumbawa form the other primary branch of BSS."),
 dict(id="sumb1241", name="Sumbawa", type="language", glottocode="sumb1241", iso639_3="smw", parent_id="pbss", inherit_page="375", **INH,
      notes="Developments from PBSS after Mbete (1990), in Adelaar (2005: 375). Not entered as a row: contraction of adjacent vowels, which did not take place in the Sumbawa Besar dialect (item 22)."),
 dict(id="java1254", name="Javanese", type="language", glottocode="java1254", iso639_3="jav", parent_id="pmp", inherit_page="375-376", **INH,
      notes="Developments from PMP after Nothofer (1975), in Adelaar (2005: 375-376); seven are shared with Malayic. Adelaar excludes Javanese from Malayo-Sumbawan. ò is written ɔ here. Not entered as rows: in modern Javanese, nasals become homorganic to following consonants, and non-nasal clusters are reduced to their second consonant (items 13-14)."),
 dict(id="sund1252", name="Sundanese", type="language", glottocode="sund1252", iso639_3="sun", parent_id="pmp", inherit_page="376", **INH,
      notes="Developments from PMP after Nothofer (1975), in Adelaar (2005: 376); 'fewer than six' are shared with Malayic. /ə/ also exists but is a loan phoneme. Adelaar puts Sundanese in Malayo-Sumbawan as a branch of its own."),
 dict(id="nucl1460", name="Madurese", type="language", glottocode="nucl1460", iso639_3="mad", parent_id="pmp", inherit_page="376", **INH,
      notes="Developments from PMP after Nothofer (1975), in Adelaar (2005: 376); four are shared with Malayic. è and ò are written ɛ and ɔ here. Not entered as rows: the fortition of non-final *w and *y (no outcome stated); the dental series d, dʰ, t contrasting with a retroflex series, with no conditioning factor (item 14, considered due to contact); gemination after schwa (item 15). Adelaar puts Madurese in Malayo-Sumbawan as a branch of its own."),
]
VIA = {"pchamic": ("thurgood1999", "373-374"), "pbss": ("mbete1990", "374"), "bali1278": ("mbete1990", "374"),
       "sasa1249": ("mbete1990", "375"), "sumb1241": ("mbete1990", "375"), "java1254": ("nothofer1975", "375-376"),
       "sund1252": ("nothofer1975", "376"), "nucl1460": ("nothofer1975", "376")}
CORR = []
def r(lect, n, p, ch, env="elsewhere", status="regular", notes="", direct=False, page=None, **kw):
    src, pg = VIA[lect]
    row = dict(id=f"{lect}-a05-{len([x for x in CORR if x['child_lect_id']==lect])+1}", child_lect_id=lect, parent_phoneme=p, child_phoneme=ch,
               environment=env, status=status, locator=f"§4, item {n}" if n else "", notes=notes)
    if direct:
        row.update(source_id=A, page=page or pg)
    else:
        row.update(source_id=src, page="", via_source_id=A, via_page=page or pg)
    if env not in ("elsewhere",) and "conditioning" not in kw:
        kw["conditioning"] = "unknown" if env == "conditions unknown" else "stated"
    row.update(kw); CORR.append(row)
U = "conditions unknown"
# Proto-Chamic (pp. 373-374)
L = "pchamic"
r(L,1,"j","d"); r(L,11,"j","t","_#",notes="*j > d with the devoicing of final voiced stops (item 11); PM, PC -d-, -t (p. 361).",as_printed="*j > d; devoicing of final voiced stops",derivation="composed")
r(L,2,"z","j"); r(L,3,"w","∅","#_"); r(L,3,"a","u","#w_",notes="*w- > ∅ 'with following *a changing to u'.")
r(L,4,"R","r"); r(L,5,"q","h"); r(L,6,"h","∅")
r(L,7,"u","ɔ","_#",notes="*-u > *-ɔw.",as_printed="*-u > -ɔw"); r(L,7,"∅","w","u_#",notes="*-u > *-ɔw.",as_printed="*-u > -ɔw")
r(L,8,"i","ɛ","_#",notes="*-i > *-ɛy.",as_printed="*-i > -ɛy"); r(L,8,"∅","y","i_#",notes="*-i > *-ɛy.",as_printed="*-i > -ɛy")
for p_, c_ in (("b","p"),("d","t"),("ɡ","k")): r(L,11,p_,c_,"_#",notes="Devoicing of final voiced stops.")
r(L,13,"l","r","#_",status="sporadic",notes="Sometimes, in part of the cases through regressive dissimilation.")
r(L,14,"n","l","#_",status="sporadic",notes="Sometimes, in part of the cases through regressive dissimilation.")
r(L,15,"d","r",U,status="sporadic",notes="Sometimes, in part of the cases through regressive assimilation.")
r(L,17,"a","aː","final syllable",status="sporadic",notes="Lengthening of some *a's in closed final syllables.")
# PBSS (p. 374)
L = "pbss"
r(L,1,"j","d",notes="PBSS -d-, -d/-t (p. 361)."); r(L,2,"z","j"); r(L,3,"w","∅","#_",notes="Intervocalic *w is usually kept in PBSS (p. 363).")
r(L,4,"q","h",notes="Section 2 gives PBSS ∅, *-h (p. 365); initial *q appears as *(h) in *quRat > PBSS *(h)urat."); r(L,5,"h","∅"); r(L,6,"R","r")
r(L,7,"b","w","V_V",status="sporadic",notes="*b > b, but sometimes becoming -w- intervocalically.")
r(L,8,"w","∅","i_#",status="sporadic",notes="*-iw > -i(w).",as_printed="*-iw > -i(w)")
r(L,9,"a","o","_w#",notes="*-aw > *-ow (Adelaar's reconstruction; Mbete has *-o and *-[i,o], p. 359).",direct=True,page="359, 374")
r(L,10,"u","i","_+y",notes="*-uy > -i (word-final).",as_printed="*-uy > -i"); r(L,10,"y","i","u+_",notes="*-uy > -i (word-final).",as_printed="*-uy > -i")
r(L,11,"a","e","_y#",notes="*-ay > -ey or -e; Adelaar reconstructs PBSS *-ey (Mbete *-[i,e], p. 359). Written e, a mid front vowel.",direct=True,page="359, 374")
r(L,11,"y","∅","a_#",conditioning="unknown",notes="*-ay > -ey or -e (the alternative -e).",as_printed="*-ay > -ey or -e")
# Balinese (p. 374; *r from p. 364)
L = "bali1278"
r(L,13,"r","∅","#_",notes="BSS r > OBal r, Sas, Sum r, Bal -Ø, -Ø-, -h (p. 364); the list has *r > OBal r, h > Bal Ø, with h kept in the Bali Aga dialect.",direct=True,page="364, 374")
r(L,13,"r","∅","V_V",direct=True,page="364, 374",notes="As above.")
r(L,13,"r","h","_#",direct=True,page="364",notes="Bal -h (p. 364): *Rumaq > Bal umah, *bibiR > Bal bibih.")
r(L,14,"h","∅","#_"); r(L,14,"h","∅","V_V"); r(L,14,"h","h","_#",notes="*h-, *-h-, *-h > OBal h-, -h-, -h > Bal Ø, -h.")
r(L,15,"w","b","i_#",status="sporadic",conditioning="lexical",lexical_scope="laib 'to run'",notes="*-iw > -ib, in the only Balinese form reflecting *-iw.")
r(L,16,"o","u","_+w",notes="*-ow > -u."); r(L,16,"w","u","o+_",notes="*-ow > -u.")
r(L,17,"e","i","_+y",notes="*-ey > -i."); r(L,17,"y","i","e+_",notes="*-ey > -i.")
r(L,19,"a","ə","_#",notes="Not in the Bali Aga dialect.")
# Sasak and Sumbawa (p. 375)
for L in ("sasa1249","sumb1241"):
    r(L,13,"h","∅","#_"); r(L,13,"h","∅","V_V"); r(L,13,"h","ʔ","_#",notes="*h > Ø, -q (-h).",source_form="q")
    r(L,13,"h","h","_#",status="sporadic",notes="The parenthesised alternative in *h > Ø, -q (-h).")
    r(L,14,"w","∅","i_#",notes="*-iw > -i."); r(L,15,"w","∅","o_#",notes="*-ow > -o."); r(L,16,"y","∅","e_#",notes="*-ey > -e.")
    r(L,17,"i","e",U,notes="*i and *u often become mid-vowels" + (" (not necessarily in the same cases as in Sasak)." if L=="sumb1241" else "."))
    r(L,17,"u","o",U,notes="As for *i.")
    r(L,18,"∅","ʔ","V_#",conditioning="unknown",notes="*-V(h) > -V, -Vq (-Vh).",source_form="q")
L = "sasa1249"
r(L,19,"a","ə","_#",variety="Meno-mene and Mriak-mriku dialects"); r(L,20,"d","r","V_V",variety="Meno-mene and Mriak-mriku dialects"); r(L,21,"r","h","_#",variety="Meno-mene and Mriak-mriku dialects")
L = "sumb1241"
r(L,19,"ə","a","final syllable",notes="Last syllable *ə > a.")
for p_, nas in (("b","m"),("d","n"),("ɡ","ŋ"),("j","ñ")):
    r(L,20,p_,"∅",f"{nas}_",notes="Clusters of a homorganic nasal and a voiced stop were reduced to their nasal.")
r(L,21,"u","i","_C# (C = l, n, r, s, t)",notes="*-u(l,n,r,s,t)# > -i(l,n,r,s,t)#; not in the Pusu dialect. Also in loanwords (umir 'age'); attested once before final m (jarim 'needle' < *zaRum) (p. 375 n. 23).")
r(L,23,"b","∅","V_V",status="sporadic",notes="*-b- sometimes became lost.")
# Javanese (pp. 375-376)
L = "java1254"
r(L,1,"R","∅"); r(L,2,"d","r"); r(L,3,"j","r"); r(L,4,"z","d")
r(L,5,"q","∅"); r(L,5,"q","h","_#",notes="*q > Ø, -h.")
r(L,6,"h","∅"); r(L,7,"b","w",notes="*b > w except in clusters, where it remains b."); r(L,7,"b","b","in clusters")
r(L,8,"e","u","_q#",notes="*ə > u before final h (< *q).")
r(L,9,"i","j","_w#",notes="*-iw > -yu.",as_printed="*-iw > -yu"); r(L,9,"w","u","i_#",notes="*-iw > -yu.",as_printed="*-iw > -yu")
r(L,10,"a","u","_+w",conditioning="unknown",notes="*-aw underwent an unconditioned split into OJav, Jav -u and OJav -o, Jav -ò."); r(L,10,"w","u","a+_",conditioning="unknown",notes="As above.")
r(L,10,"a","ɔ","_+w",conditioning="unknown",notes="As above; Jav ò.",source_form="ò"); r(L,10,"w","ɔ","a+_",conditioning="unknown",notes="As above.",source_form="ò")
r(L,11,"u","i","_+y",notes="*-uy > OJav -uy/-i, Jav -i."); r(L,11,"y","i","u+_",notes="As above.")
r(L,12,"a","i","_+y",conditioning="unknown",notes="*-ay underwent an unconditioned split into -i and OJav -ay/-e, Jav -e."); r(L,12,"y","i","a+_",conditioning="unknown",notes="As above.")
r(L,12,"a","e","_+y",conditioning="unknown",notes="As above."); r(L,12,"y","e","a+_",conditioning="unknown",notes="As above.")
# Sundanese (p. 376)
L = "sund1252"
for ch in ("r","j","∅"): r(L,1,"R",ch,U,notes="*R > r, y, Ø.",source_form="y" if ch=="j" else "")
r(L,2,"d","r"); r(L,3,"j","r"); r(L,4,"z","d͡ʒ",source_form="j")
r(L,5,"w","t͡ʃ","#_",conditioning="unknown",notes="*w- > c-, Ø.",source_form="c"); r(L,5,"w","∅","#_",conditioning="unknown",notes="*w- > c-, Ø.")
r(L,6,"q","h",notes="*q > h; (*h > h)."); r(L,6,"h","h",notes="Printed in parentheses: *h is kept.",derivation="")
r(L,7,"e","ɨ",notes="*ə > ɨ (in a few cases i)."); r(L,7,"e","i",U,status="sporadic",notes="In a few cases.")
r(L,8,"b","w","V_V",status="sporadic",notes="*b > b, but intervocalically sometimes w.")
r(L,9,"w","∅","i_#",conditioning="unknown",notes="*-iw > -i, -yu."); r(L,9,"i","j","_w#",conditioning="unknown",notes="*-iw > -i, -yu (the second outcome)."); r(L,9,"w","u","i_#",conditioning="unknown",notes="As above.")
r(L,10,"a","o","_+w",notes="*-aw > -o."); r(L,10,"w","o","a+_",notes="*-aw > -o.")
r(L,11,"a","e","_+y",conditioning="unknown",notes="*-ay underwent an unconditioned split into -e or -ay."); r(L,11,"y","e","a+_",conditioning="unknown",notes="As above.")
# Madurese (p. 376)
L = "nucl1460"
r(L,1,"R","r"); r(L,2,"j","l"); r(L,3,"z","d͡ʒʰ",source_form="jh",notes="*z > jh; *z is also among the voiced stops that are aspirated (item 7).")
r(L,5,"q","∅",notes="Loss of *q except between like vowels, where it appears as a glottal stop."); r(L,5,"q","ʔ","between like vowels")
r(L,6,"h","∅")
for p_, c_ in (("b","bʰ"),("d","dʰ"),("ɡ","ɡʰ")): r(L,7,p_,c_,"#_, V_V",notes="Aspiration of initial and intervocalic voiced stops and *z.",source_form=c_.replace("ʰ","h").replace("ɡ","g"))
for p_ in ("k","p","t"): r(L,8,p_,"ʔ","_#",notes="Final *k, *p, *t become glottal stop.")
for p_, c_ in (("b","p"),("d","t"),("ɡ","k")): r(L,9,p_,c_,"_#",notes="Devoicing of final *b, *d, *g; it occurred after the original final voiceless stops had become glottal stops, so the two did not merge (p. 377).")
r(L,10,"i","u","_w#",notes="*-iw > -uy.",as_printed="*-iw > -uy"); r(L,10,"w","j","i_#",notes="*-iw > -uy.",as_printed="*-iw > -uy",source_form="y")
r(L,11,"a","u","_+w",conditioning="unknown",notes="*-aw > -u, -ò."); r(L,11,"w","u","a+_",conditioning="unknown",notes="As above.")
r(L,11,"a","ɔ","_+w",conditioning="unknown",notes="As above.",source_form="ò"); r(L,11,"w","ɔ","a+_",conditioning="unknown",notes="As above.",source_form="ò")
r(L,12,"u","ɔ","_y#",conditioning="unknown",notes="*-uy > -uy, -òy.",source_form="ò")
r(L,13,"a","i","_+y",conditioning="unknown",notes="*-ay underwent an unconditioned split into -ay and -i/-è."); r(L,13,"y","i","a+_",conditioning="unknown",notes="As above.")
r(L,13,"a","ɛ","_+y",conditioning="unknown",notes="As above.",source_form="è"); r(L,13,"y","ɛ","a+_",conditioning="unknown",notes="As above.",source_form="è")
# Retentions entered explicitly: (1) phonemes whose other rows have unknown conditioning would get no
# implied retention; (2) a retained phoneme whose symbol differs between the parent's orthography and
# IPA (PMP schwa e, which Adelaar writes ə in PC and PBSS; y, ñ, and PBSS *j < *z in attested lects).
KEEP = {"pchamic": [("d", "d"), ("e", "ə")], "pbss": [("y", "y"), ("e", "ə")],
        "bali1278": [("w", "w"), ("y", "j"), ("ñ", "ɲ"), ("j", "d͡ʒ")],
        "sasa1249": [("i", "i"), ("u", "u"), ("y", "j"), ("ñ", "ɲ"), ("j", "d͡ʒ")],
        "sumb1241": [("i", "i"), ("u", "u"), ("y", "j"), ("ñ", "ɲ"), ("j", "d͡ʒ")],
        "java1254": [("a", "a"), ("w", "w"), ("y", "j"), ("ñ", "ɲ"), ("e", "ə")],
        "sund1252": [("w", "w"), ("i", "i"), ("a", "a"), ("y", "j"), ("ñ", "ɲ")],
        "nucl1460": [("a", "a"), ("w", "w"), ("u", "u"), ("y", "j"), ("ñ", "ɲ"), ("e", "ə")]}
for lect, pairs in KEEP.items():
    for p_, c_ in pairs:
        why = ("Retained elsewhere: Adelaar's list changes it only in some cases or positions (see the other rows); inferred, as for the lect's other unlisted phonemes."
               if p_ == c_ else f"Not changed in Adelaar's list: retained, written {c_} here (*{p_} in the parent's orthography).")
        CORR.append(dict(id=f"{lect}-a05-keep-{p_}", child_lect_id=lect, parent_phoneme=p_, child_phoneme=c_,
                         environment="elsewhere", status="regular", source_id=A, page=VIA[lect][1], derivation="implied-retention", notes=why))
for row in CORR:
    if row.get("derivation") == "" : row.pop("derivation")
NOTATION = [dict(lect_id=l, system="canonical", source_id=A, page=pg, notes=nt) for l, pg, nt in [
  ("pchamic", "373-374", "Adelaar's spelling of Thurgood's Proto-Chamic changes."),
  ("pbss", "374", "Adelaar's spelling; PBSS *e (from *-ay > *-ey) is a mid front vowel, not schwa.")]]
PHON = [dict(lect_id="pbss", ipa="e", **{"class": "V"}, place="front", manner="close-mid", rounding="unrounded", origin="override",
             reason="PBSS *e in *-ey (< PMP *-ay) is a mid front vowel (Adelaar 2005: 359, 374); the proto-orthography would read e as schwa.")]
DECISIONS = [
 dict(id="adelaar2005-ms", batch=A, status="open", source_id=A, page="357, 377-388",
      question="Adelaar's Malayo-Sumbawan: a Malayic-Chamic-BSS branch, with Sundanese and Madurese as two other branches, excluding Javanese. Enter it as nodes?",
      chosen_reading="Not entered as nodes. Proto-Chamic, Proto-Balinese-Sasak-Sumbawa, Sundanese, Madurese and Javanese are placed directly under PMP, each with the developments from PMP that Adelaar lists (§4); Proto-Malayic stays where it is.",
      alternatives="Add a group 'Malayo-Sumbawan' (and 'Malayic-Chamic-BSS') as tree parents; or a Proto-Malayo-Sumbawan node with the shared developments.", notes="Batch adelaar2005."),
 dict(id="adelaar2005-unconditioned", batch=A, status="open", source_id=A, page="373-376",
      question="How to enter Adelaar's 'unconditioned splits' of final diphthongs and changes stated with alternatives (*R > r, y, Ø; *-aw > -u, -ò)?",
      chosen_reading="One row per outcome with conditioning unknown; final diphthong mergers as fusions (V + glide), other diphthong changes as conditioned rows. Where a list item gives no outcome (Madurese fortition of *w, *y) or is not segmental (cluster reduction, nasal accretion, vowel contraction), it is in the lect's notes only.",
      alternatives="Leave the splits out.", notes="Batch adelaar2005."),
]
def write(table, rows):
    cols = B.TABLES[table]; OUT.mkdir(parents=True, exist_ok=True)
    buf = io.StringIO(); w = csv.writer(buf, lineterminator="\n"); w.writerow(cols)
    for row in rows: w.writerow([N(str(row.get(c, ""))) for c in cols])
    (OUT / f"{table}.csv").write_text(buf.getvalue(), encoding="utf-8"); print(table, len(rows))
write("sources", SOURCES); write("lects", LECTS); write("correspondences", CORR); write("notation_map", NOTATION); write("phonemes", PHON); write("decisions", DECISIONS)
