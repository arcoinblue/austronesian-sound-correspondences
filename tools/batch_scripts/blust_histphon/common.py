"""Shared table writer for the Blust historical-phonology batch."""
import csv
import hashlib
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NFC = lambda s: unicodedata.normalize("NFC", s)

COLS = {
    "sources": "id,author,year,title,url_or_doi,kind,notes,year_suffix,pub_type,container_title,editors,volume,issue,pages,place,publisher,series,edition",
    "lects": "id,name,alt_names,type,glottocode,iso639_3,parent_id,subgroup_path,region,orthography_note,notes,default_system,systems,clade,competes_with,latitude,longitude,overlap_groups,inherit,language_id,alt_parents,inherit_source_id,inherit_page,inherit_note",
    "phonemes": "lect_id,ipa,source_symbol,class,place,manner,voicing,rounding,origin,source_id,page,reason,notes,via_source_id,via_page,via_note,status",
    "correspondences": "id,child_lect_id,parent_phoneme,child_phoneme,environment,status,blank_type,evidence_count,source_id,page,notes,system,via_source_id,via_page,via_note,conditioning,evidence_total,derivation,variety,stratum,lexical_scope,examples,source_form,as_printed,locator,decision",
    "notation_map": "lect_id,phoneme,system,symbol,source_id,page,notes,place,manner,voicing,via_source_id,via_page,via_note",
    "decisions": "id,batch,question,chosen_reading,alternatives,status,source_id,page,notes",
}


class Batch:
    def __init__(self, name):
        self.name = name
        self.out = ROOT / "data" / "incoming" / name
        self.T = {k: [] for k in COLS}
        self.seen = set()

    def add(self, table, **kw):
        cols = COLS[table].split(",")
        bad = set(kw) - set(cols)
        assert not bad, (table, bad)
        self.T[table].append({c: NFC(str(kw.get(c, ""))) for c in cols})

    def C(self, L, par, ch, env="elsewhere", st="regular", src="", page="", notes="", loc="", blank="", n="", tot="",
          ex="", sf="", ap="", dec="", deriv="", cond="", lex="", system="", via="", viap="", vian=""):
        """One correspondence row; the id is a hash of its key."""
        if blank:
            st = ""
        if env == "conditions unknown" and not cond:
            cond = "unknown"
        if lex and not cond:
            cond = "lexical"
        key = (L, par, ch, env, src, system, lex)
        assert key not in self.seen, key
        self.seen.add(key)
        rid = "c" + hashlib.sha1("|".join(map(str, (L, par, ch, env, src, page, system, lex))).encode()).hexdigest()[:10]
        self.add("correspondences", id=rid, child_lect_id=L, parent_phoneme=par, child_phoneme=ch, environment=env,
                 status=st, blank_type=blank, evidence_count=n, evidence_total=tot, source_id=src, page=page,
                 notes=notes, locator=loc, examples=ex, source_form=sf, as_printed=ap, decision=dec, derivation=deriv,
                 conditioning=cond, lexical_scope=lex, system=system, via_source_id=via, via_page=viap, via_note=vian)

    def P(self, L, ipa, cls, src, page, sym="", place="", manner="", voicing="", rnd="", notes="", status="",
          via="", viap="", vian=""):
        self.add("phonemes", lect_id=L, ipa=ipa, source_symbol=sym or ipa, **{"class": cls}, place=place,
                 manner=manner, voicing=voicing, rounding=rnd, origin="sourced", source_id=src, page=page,
                 notes=notes, status=status, via_source_id=via, via_page=viap, via_note=vian)

    def D(self, id, q, chosen, alt="", src="", page="", notes=""):
        self.add("decisions", id=id, batch=self.name, question=q, chosen_reading=chosen, alternatives=alt,
                 status="open", source_id=src, page=page, notes=notes)

    def write(self):
        self.out.mkdir(parents=True, exist_ok=True)
        for t, rows in self.T.items():
            if not rows:
                continue
            with open(self.out / f"{t}.csv", "w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=COLS[t].split(","))
                w.writeheader()
                w.writerows(rows)
        return {t: len(r) for t, r in self.T.items() if r}
