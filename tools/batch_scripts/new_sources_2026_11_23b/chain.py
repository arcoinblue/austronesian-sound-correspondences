"""Walk the lect tree to restate a source's ancestor-based reflexes against a lect's own parent.

Loads cldf/ only, so that the batches written by these scripts do not feed back into them.
`reflex(ancestor, node, phoneme)` follows the regular 'elsewhere' rows from the ancestor down to
the node and returns the node's phoneme (or None when the chain loses it). A phoneme with no row at
a step is taken to be retained, as the build does for lects whose changes are listed.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def _read(table):
    rows = []
    paths = [ROOT / "cldf" / f"{table}.csv"]
    for p in paths:
        if p.exists():
            with open(p, encoding="utf-8") as f:
                rows += list(csv.DictReader(f))
    return rows


LECTS = {r["id"]: r for r in _read("lects")}
CORR = _read("correspondences")
BY = {}
for r in CORR:
    BY.setdefault((r["child_lect_id"], r["parent_phoneme"]), []).append(r)

ELSEWHERE = {"elsewhere", "", "word-internally"}


def chain(node, ancestor):
    """Lects from ancestor (exclusive) down to node (inclusive)."""
    path = []
    cur = node
    while cur and cur != ancestor:
        path.append(cur)
        cur = LECTS[cur]["parent_id"]
    if cur != ancestor:
        raise KeyError(f"{ancestor} is not an ancestor of {node}")
    return list(reversed(path))


def step(lect, ph):
    rows = [r for r in BY.get((lect, ph), []) if r["status"] in ("regular", "")]
    els = [r for r in rows if r["environment"] in ELSEWHERE]
    if els:
        return els[0]["child_phoneme"], len(els) > 1
    if rows and all(r["environment"] not in ELSEWHERE for r in rows):
        return ph, False  # only conditioned changes: elsewhere retained
    return ph, False


def reflex(ancestor, node, ph):
    amb = False
    for lect in chain(node, ancestor):
        if ph in (None, "∅"):
            return None, amb
        ph, a = step(lect, ph)
        amb = amb or a
    return (None if ph == "∅" else ph), amb


def parent_of(lect):
    return LECTS[lect]["parent_id"]
