#!/usr/bin/env python3
"""Batch blust2013-reinforce: rows read directly from Blust (2013: 553-593), the
excerpt of ch. 8 in the user's Downloads/austdic folder.

    python3 tools/batch_scripts/blust2013/build.py

The PAn and PMP notation rows already cite Blust (2013) directly. This batch
adds Blust as a second, direct source for rows that are entered from other works:
- PMP > POc changes illustrated in Table 8.32 and stated on pp. 592-593 (Ross et
  al. 2023 has the same changes with counts);
- the reflexes of PAN *j (Table 8.27), *h (Table 8.29) and *R (Table 8.30) in
  the Formosan languages that are entered directly under PAN.
Blust's segment letters are mapped to the IPA already in each lect's inventory;
the printed letter goes in source_form.
"""
import csv
import hashlib
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "data" / "incoming" / "blust2013-reinforce"
NFC = lambda s: unicodedata.normalize("NFC", s)
S = "blust2013"
CORR = ("id,child_lect_id,parent_phoneme,child_phoneme,environment,status,blank_type,evidence_count,source_id,page,notes,"
        "system,via_source_id,via_page,via_note,conditioning,evidence_total,derivation,variety,stratum,lexical_scope,"
        "examples,source_form,as_printed,locator,decision").split(",")
DEC = "id,batch,question,chosen_reading,alternatives,status,source_id,page,notes".split(",")
rows, decs = [], []


def C(L, par, ch, page, loc, env="elsewhere", notes="", ex="", sf="", ap="", dec=""):
    rid = "c" + hashlib.sha1("|".join([L, par, ch, env, S, str(page)]).encode()).hexdigest()[:10]
    r = dict.fromkeys(CORR, "")
    r.update(id=rid, child_lect_id=L, parent_phoneme=par, child_phoneme=ch, environment=env, status="regular",
             source_id=S, page=str(page), notes=notes, locator=loc, examples=ex, source_form=sf, as_printed=ap,
             decision=dec)
    rows.append({k: NFC(v) for k, v in r.items()})


# --- PMP > POc (pp. 592-593, Table 8.32)
MERGE = "'Although PMP *b and *p (and *g and *k) had merged in POC, simple and prenasalised stops yielded different reflexes' (p. 592)."
C("poc", "b", "p", 592, "Table 8.32", ex="*bulan > *pulan; *qabu > *qapu", notes=MERGE + " Oral grade.")
C("poc", "g", "k", 592, "Table 8.32", notes=MERGE)
C("poc", "d", "r", 592, "Table 8.32", ex="*duha > *rua; *kuden > *kuron", notes="Oral grade.")
C("poc", "z", "s", 592, "Table 8.32", ex="*quzan > *qusan", notes="Oral grade.")
C("poc", "z", "j", 592, "Table 8.32", ex="*zalan > *jalan; *tazim > *tajim",
  notes="Nasal grade. Blust finds no satisfactory source for nasal-grade reflexes in initial position (pp. 592-593).")
C("poc", "h", "∅", 592, "Table 8.32", ex="*hapuy > *api; *duha > *rua")
C("poc", "e", "o", 593, "", ex="*beRek > *boRok; *kuden > *kuron",
  notes="'Most instances of POC *o derive from PMP *e (schwa), with others reflecting *-aw' (p. 593). Blust adds that the "
        "change is shared with Central Malayo-Polynesian and South Halmahera-West New Guinea, 'and so must predate POC'.")

# --- PAN *j (Table 8.27, p. 578)
J = "Table 8.27"
C("kava1241", "j", "n̪", 578, J, sf="n", notes="Blust prints n; entered as n̪, the symbol of the sourced inventory.")
C("sira1267", "j", "n", 578, J)
C("kana1286", "j", "ɾ", 578, J, sf="l", notes="Blust prints l (Kanakanabu); the sourced inventory has ɾ and r but no l.")
C("saar1237", "j", "ɬ", 578, J, env="V_V", sf="ɬ", notes="'-ɬ- only'.")
C("sais1237", "j", "ð", 578, J, sf="z", notes="Printed z ([ð]).")
C("thao1240", "j", "ð", 578, J, sf="z", notes="Printed z ([ð]).")
C("tsou1248", "j", "∅", 578, J, sf="Ø")
C("kulo1237", "j", "d͡z", 578, J, env="V_V", sf="z", notes="Printed z ([dz]), '-z- only'.")
C("kulo1237", "j", "d", 578, J, env="_#", sf="d", dec="pazeh-j-final",
  notes="'-d only'. Blust lists Pazeh among the exceptions to his remark that languages with general final devoicing "
        "reflect *j as a voiceless stop word-finally (p. 578).")
# --- PAN *h (Table 8.29, p. 586)
H = "Table 8.29"
C("sais1237", "h", "h", 586, H, ex="*baRah > baLah; *CuNuh > s-om-olœh; *buhet > ka-bhœt",
  notes="One of the four languages in Taiwan that give the primary evidence for PAN *h (p. 586).")
C("kulo1237", "h", "ħ", 586, H, sf="h", ex="*baRah > bahah; *Capuh > sapuh; *nunuh > nunuh; *qumah > u-ma-mah; *buhet > buhut",
  notes="Printed h; entered as ħ, the symbol of the sourced inventory. One of the four languages in Taiwan that give the "
        "primary evidence for PAN *h (p. 586).")
# --- PAN *R (Table 8.30, p. 588)
RT = "Table 8.30"
C("taok1237", "R", "l", 588, RT)
C("basa1287", "R", "l", 588, RT)
C("thao1240", "R", "ɬ̪", 588, RT, sf="lh", notes="Printed lh, 'voiceless lateral'; entered as ɬ̪, the symbol of the sourced inventory.")
C("sais1237", "R", "ɾ", 588, RT, sf="L", notes="Printed L, 'retroflex flap'; entered as ɾ, the only flap in the sourced inventory (from Li 1978).")
C("kava1241", "R", "ʁ", 588, RT, sf="R", notes="Printed R, 'contrastive uvular rhotic'; entered as ʁ, the symbol of the sourced inventory.")
C("kulo1237", "R", "x", 588, RT)

decs.append({k: NFC(v) for k, v in dict(
    id="pazeh-j-final", batch="blust2013-reinforce",
    question="Pazeh reflex of PAN *j word-finally: d (Blust 2013: 578) or t̪ (the row from Blust 1999b via Shibata 2025)?",
    chosen_reading="Both rows are kept, each with its source: Blust (2013) lists Pazeh '-d only' as an exception to final "
                   "devoicing; the earlier row has t̪ by final devoicing.",
    alternatives="Keep only one of the two.", status="open", source_id=S, page="578", notes="").items()})

OUT.mkdir(parents=True, exist_ok=True)
with open(OUT / "correspondences.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=CORR); w.writeheader(); w.writerows(rows)
with open(OUT / "decisions.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=DEC); w.writeheader(); w.writerows(decs)
print("correspondences", len(rows), "decisions", len(decs))
