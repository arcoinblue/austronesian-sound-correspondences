"""Shared writer for the batches of 26 November 2026 (Dutton & Tryon 1994, eleven chapters).

Each source script builds lists of dicts and calls write(batch_id, tables, batch_md).
Columns come from the headers of cldf/<table>.csv; text is NFC-normalised.
"""
import csv, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TABLES = ["sources", "lects", "phonemes", "allophones", "correspondences", "notation_map", "decisions"]


def N(s):
    return unicodedata.normalize("NFC", s) if isinstance(s, str) else s


def header(table):
    with open(ROOT / "cldf" / f"{table}.csv", encoding="utf-8") as f:
        return next(csv.reader(f))


def existing(table, col):
    with open(ROOT / "cldf" / f"{table}.csv", encoding="utf-8") as f:
        return {r[col] for r in csv.DictReader(f)}


def write(batch, tables, batch_md):
    out = ROOT / "data" / "incoming" / batch
    out.mkdir(parents=True, exist_ok=True)
    for t in TABLES:
        rows = tables.get(t) or []
        p = out / f"{t}.csv"
        if not rows:
            if p.exists():
                p.unlink()
            continue
        cols = header(t)
        if t == "decisions" and "batch" in cols:
            for r in rows:
                r.setdefault("batch", batch)
        extra = {k for r in rows for k in r} - set(cols)
        if extra:
            raise SystemExit(f"{batch}/{t}: unknown columns {sorted(extra)}")
        if t == "correspondences":
            ids = [r["id"] for r in rows]
            dup = {i for i in ids if ids.count(i) > 1}
            if dup:
                raise SystemExit(f"{batch}: duplicate ids {sorted(dup)[:5]}")
        with open(p, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
            w.writeheader()
            for r in rows:
                w.writerow({c: N(str(r.get(c, ""))).strip() for c in cols})
    (out / "BATCH.md").write_text(N(batch_md), encoding="utf-8")
    print(batch, {t: len(tables.get(t) or []) for t in TABLES})


import hashlib


class Batch:
    """Row builders shared by the batches of 25 November 2026."""

    def __init__(self, source):
        self.S = source
        self.t = {k: [] for k in TABLES}

    def corr(self, lect, par, child, env="elsewhere", page="", notes="", status="regular", n="", total="",
             derivation="composed", as_printed="", source_form="", conditioning="", decision="", locator="",
             lexical_scope="", examples="", blank_type="", system="", via_source_id="", via_page="", via_note="",
             source=None):
        src = source or self.S
        key = "|".join([lect, par, child, env, status, src, page, as_printed, source_form])
        cid = "c" + hashlib.sha1(key.encode()).hexdigest()[:10]
        if env == "conditions unknown" and not conditioning:
            conditioning = "unknown"
        self.t["correspondences"].append(dict(
            id=cid, child_lect_id=lect, parent_phoneme=par, child_phoneme=child, environment=env,
            status="" if blank_type else status, blank_type=blank_type, evidence_count=str(n), source_id=src,
            page=page, notes=notes.strip(), conditioning=conditioning, evidence_total=str(total), derivation=derivation,
            as_printed=as_printed, source_form=source_form, decision=decision, locator=locator,
            lexical_scope=lexical_scope, examples=examples, system=system, via_source_id=via_source_id,
            via_page=via_page, via_note=via_note))

    def ph(self, lect, ipa, cls, place="", manner="", voicing="", rounding="", sym="", page="", notes="", status="",
           source=None, via_source_id="", via_page="", via_note=""):
        self.t["phonemes"].append(dict(lect_id=lect, ipa=ipa, source_symbol=sym or ipa, **{"class": cls},
                                       place=place, manner=manner, voicing=voicing, rounding=rounding,
                                       origin="sourced", source_id=source or self.S, page=page, notes=notes,
                                       status=status, via_source_id=via_source_id, via_page=via_page,
                                       via_note=via_note))

    def allo(self, lect, ph, allophone, env, page, notes="", source=None, via_source_id="", via_page="",
             via_note=""):
        self.t["allophones"].append(dict(lect_id=lect, phoneme=ph, allophone=allophone, environment=env,
                                         source_id=source or self.S, page=page, notes=notes,
                                         via_source_id=via_source_id, via_page=via_page, via_note=via_note))

    def dec(self, id, question, chosen, alternatives, page, notes=""):
        self.t["decisions"].append(dict(id=id, question=question, chosen_reading=chosen, alternatives=alternatives,
                                        status="open", source_id=self.S, page=page, notes=notes))


VOLUME = dict(kind="comparative", pub_type="chapter",
              container_title="Language contact and change in the Austronesian world",
              editors="Dutton, Tom; Tryon, Darrell T.", series="Trends in Linguistics: Studies and Monographs 77",
              place="Berlin", publisher="Mouton de Gruyter", year="1994")


def chapter(id, author, title, pages, notes):
    """A sources row for a chapter of Dutton & Tryon (1994)."""
    return dict(id=id, author=author, title=title, pages=pages, notes=notes, **VOLUME)


CONSULTED = ("Consulted directly on 26 November 2026 (PDF of the volume in Downloads; tables read from page "
             "images). ")
