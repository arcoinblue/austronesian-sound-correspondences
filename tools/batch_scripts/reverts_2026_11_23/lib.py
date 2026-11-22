"""Helpers for editing the ASC tables in place, keeping sheet row numbers.

Every table is read from a cldf/-style folder. Row N of a CSV is row N of the sheet tab
(tools/sync_sheet.py keeps blank rows), so each record carries its sheet row in `_row`.
Edits change records in place; deletions set `_deleted`; new records have `_row` None and
are appended at the end of the tab. `diff()` lists what has to be written to the sheet.
"""
import csv, hashlib, io, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from asc import schema  # noqa: E402

TABS = ["sources", "lects", "phonemes", "correspondences", "notation_map", "allophones", "decisions"]
N = lambda s: unicodedata.normalize("NFC", s)


class Tables:
    def __init__(self, folder):
        self.folder = Path(folder)
        self.t, self.header, self.orig = {}, {}, {}
        for tab in TABS:
            with open(self.folder / f"{tab}.csv", newline="", encoding="utf-8") as f:
                rd = csv.DictReader(f)
                self.header[tab] = rd.fieldnames
                rows = []
                for i, r in enumerate(rd, start=2):
                    r = dict(r)
                    r["_row"] = i
                    rows.append(r)
            self.t[tab] = rows
            self.orig[tab] = {r["_row"]: {k: v for k, v in r.items() if not k.startswith("_")} for r in rows}

    # --- access
    def rows(self, tab, **kw):
        return [r for r in self.t[tab] if not r.get("_deleted")
                and all(r.get(k) == v for k, v in kw.items())]

    def one(self, tab, **kw):
        rs = self.rows(tab, **kw)
        assert len(rs) == 1, (tab, kw, len(rs))
        return rs[0]

    def lect(self, i):
        return self.one("lects", id=i)

    def kids(self, p):
        return [l for l in self.rows("lects") if l["parent_id"] == p]

    def corr(self, cid):
        return self.one("correspondences", id=cid)

    # --- edits
    def set(self, r, **kw):
        for k, v in kw.items():
            assert k in self.header[self._tab_of(r)], k
            r[k] = N(v)
        return r

    def _tab_of(self, r):
        for tab, rows in self.t.items():
            if any(x is r for x in rows):
                return tab
        raise KeyError

    def delete(self, r):
        r["_deleted"] = True

    def add(self, tab, **kw):
        r = {k: "" for k in self.header[tab]}
        for k, v in kw.items():
            assert k in self.header[tab], (tab, k)
            r[k] = N(v)
        if tab == "correspondences" and not r["id"]:
            r["id"] = self.new_id(r)
        r["_row"] = None
        self.t[tab].append(r)
        return r

    def new_id(self, r):
        used = {x["id"] for x in self.t["correspondences"]}
        key = "|".join(r[k] for k in ("child_lect_id", "parent_phoneme", "child_phoneme", "environment",
                                       "source_id", "status", "variety"))
        n = 0
        while True:
            h = "c" + hashlib.sha1(f"reverts-2026-11-23|{key}|{n}".encode()).hexdigest()[:10]
            if h not in used:
                return h
            n += 1

    def append_note(self, r, text, col="notes"):
        cur = r[col].strip()
        r[col] = N((cur + " " + text).strip() if cur else text)

    # --- output
    KEYS = {"sources": ["id"], "lects": ["id"], "phonemes": ["lect_id", "ipa"], "correspondences": ["id"],
            "notation_map": ["lect_id", "phoneme", "system", "symbol"],
            "allophones": ["lect_id", "phoneme", "system", "allophone", "environment", "source_id"],
            "decisions": ["id"]}

    def key(self, tab, r):
        return tuple(r.get(c, "") for c in self.KEYS[tab])

    def final(self, tab):
        """The tab as it should be: rows kept in place (edited), deleted rows removed, and at the end the rows
        whose key changed (moved: the old row is deleted and the new one appended) and the new rows."""
        inplace, moved, new = [], [], []
        for r in self.t[tab]:
            if r.get("_deleted"):
                continue
            if r["_row"] is None:
                new.append(r)
            elif self.key(tab, r) != self.key(tab, self.orig[tab][r["_row"]]) and any(self.orig[tab][r["_row"]].values()):
                moved.append(r)
            else:
                inplace.append(r)
        return inplace, moved, new

    def write(self, out):
        out = Path(out)
        out.mkdir(parents=True, exist_ok=True)
        summary = {}
        for tab in TABS:
            inplace, moved, new = self.final(tab)
            buf = io.StringIO()
            w = csv.DictWriter(buf, fieldnames=self.header[tab], lineterminator="\n", extrasaction="ignore")
            w.writeheader()
            for r in inplace + moved + new:
                w.writerow(r)
            (out / f"{tab}.csv").write_text(buf.getvalue(), encoding="utf-8")
            mod = sum(1 for r in inplace if {k: v for k, v in r.items() if not k.startswith("_")} != self.orig[tab][r["_row"]])
            dele = sum(1 for r in self.t[tab] if r.get("_deleted") and r["_row"] is not None)
            summary[tab] = dict(modified=mod, deleted=dele + len(moved), appended=len(moved) + len(new))
            keys = [self.key(tab, r) for r in inplace + moved + new if any(v for k, v in r.items() if not k.startswith("_"))]
            dup = {k for k in keys if keys.count(k) > 1} if tab != "allophones" else set()
            assert not dup, (tab, list(dup)[:5])
        return summary
