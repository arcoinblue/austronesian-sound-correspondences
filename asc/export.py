"""Writing the site's data files and the generated part of STATUS.md."""
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from .schema import *  # noqa: F401,F403

STATUS_BEGIN = "<!-- BEGIN GENERATED: python3 build.py --check --status STATUS.md; do not edit by hand -->"
STATUS_END = "<!-- END GENERATED -->"
STATUS_HAND = """
## Not yet entered

(Hand-kept. Sources or parts of sources still to read into the sheet.)

## Code to-do

(Hand-kept. Work on build.py, the site and the tools.)
"""


def _cell(text, limit=160):
    text = " ".join(str(text).split()).replace("|", "\\|")
    return text if len(text) <= limit else text[:limit - 1] + "…"


WARNING_KINDS = [
    (re.compile(r"is cited in notes but has no sources row"), "a work cited in notes has no sources row"),
    (re.compile(r"^reflex \S+ is not in .* sourced inventory"), "a reflex is not in the lect's sourced inventory"),
    (re.compile(r"has symbols that are not IPA"), "an attested lect has symbols that are not IPA"),
    (re.compile(r"^source \S+ is never cited"), "a source is never cited"),
    (re.compile(r"^lect id should be its Glottocode"), "lect id is not its Glottocode"),
]


def warning_kind(w):
    msg = w.split(": ", 1)[-1]
    for pat, kind in WARNING_KINDS:
        if pat.search(msg):
            return kind
    msg = re.sub(r"'[^']*'|\{[^}]*\}|\([^)]*\)", "…", msg.split(";")[0])
    return re.sub(r"\S*[\d:*]\S*", "…", msg)


def status_md(t, D, rep, counts=None):
    """The generated part of STATUS.md: table sizes, check results, open decisions.
    Deterministic (no dates), so it changes only when the data or the checks do."""
    out = [STATUS_BEGIN, "", "## Data", ""]
    gen = Counter(r["derivation"] for r in D["corrs"] if r["_where"].startswith("lects.csv"))
    out += ["| Table | Rows | |", "|---|---|---|"]
    for name in TABLES:
        n = (counts or {}).get(name, len(t.get(name, [])))
        extra = ""
        if name == "lects":
            types = Counter(r["type"] for r in t["lects"])
            extra = ", ".join(f"{v} {k}" for k, v in sorted(types.items()))
        elif name == "correspondences":
            extra = (f"plus {gen['implied-retention']} implied and {gen['stated-retention']} stated retentions "
                     "generated from lects.inherit")
        elif name == "decisions":
            st = Counter(d["status"] for d in D["decisions"].values())
            extra = ", ".join(f"{v} {k}" for k, v in sorted(st.items()))
        out.append(f"| {name} | {n} | {extra} |")
    inh = Counter(r["inherit"] or "(blank)" for r in D["lects"].values())
    inv = Counter(D["inv_status"].values())
    out += ["", "Lects by `inherit`: " + ", ".join(f"{k} {v}" for k, v in sorted(inh.items())) + ".",
            "Inventories: " + ", ".join(f"{k} {v}" for k, v in sorted(inv.items())) + ".",
            "", "## Checks", "",
            f"`build.py --check`: {len(rep.errors)} error(s), {len(rep.warnings)} warning(s), "
            f"{len(rep.notes)} note(s).", ""]
    kinds = Counter(warning_kind(w) for w in rep.warnings)
    if kinds:
        out += ["| Warnings | Count |", "|---|---|"]
        out += [f"| {_cell(k)} | {v} |" for k, v in kinds.most_common(20)]
        if len(kinds) > 20:
            out.append(f"| other kinds | {sum(v for _, v in kinds.most_common()[20:])} |")
        out.append("")
    opened = [d for d in D["decisions"].values() if d["status"] == "open"]
    out += ["## Open decisions", "",
            "From the `decisions` tab. Confirm or revert one by changing its `status` in the sheet.", ""]
    if opened:
        out += ["| id | Question | Reading taken | Rows |", "|---|---|---|---|"]
        out += [f"| `{d['id']}` | {_cell(d['question'])} | {_cell(d['chosen_reading'])} | {len(d['rows']) or ''} |"
                for d in opened]
    else:
        out.append("None.")
    out += ["", STATUS_END]
    return "\n".join(out) + "\n"


def write_status(path, text):
    """Replace the generated block of STATUS.md, keeping everything else (the hand-kept sections)."""
    path = Path(path)
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    if STATUS_BEGIN in old and STATUS_END in old:
        head, rest = old.split(STATUS_BEGIN, 1)
        tail = rest.split(STATUS_END, 1)[1]
        new = head + text.rstrip("\n") + tail
    elif old.strip():
        new = old.rstrip("\n") + "\n\n" + text   # no block yet: add it, keep the file
    else:
        new = ("# ASC status\n\nThe generated part is rewritten by every sync; the sections after it are kept by hand.\n\n"
               + text + STATUS_HAND)
    if new != old:
        path.write_text(new, encoding="utf-8")
