"""Writing the site's data files and the generated part of STATUS.md."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
from collections import Counter
from pathlib import Path

from .schema import *  # noqa: F401,F403
from .derive import lect_files, index_json, sources_json


def site_files(D):
    """{path under data/: record} for every file the site reads."""
    out, lites = {}, {}
    for L in D["lects"]:
        lite, files = lect_files(L, D)
        lites[L] = lite
        out[f"{L}.json"] = lite
        out.update(files)
    out["index.json"] = index_json(D, lites)
    out["sources.json"] = sources_json(D)
    out["segments.json"] = segments_json(D, lites)
    return out


def segments_json(D, lites):
    """Every lect's inventory as its page shows it (the default system's
    phonemes), for the Segments page: [ipa, url id, class, place, manner,
    voicing, rounding, flags], flags "i" implied, "m" marginal or doubtful."""
    out = []
    for L in D["lects"]:
        lite = lites[L]
        ds = lite.get("default_system")
        rows = [[p["ipa"], p["url_id"], p["class"], p["place"], p["manner"], p["voicing"], p["rounding"],
                 ("i" if p.get("implied") else "") + ("m" if p.get("status") else "")]
                for p in lite["phonemes"] if not (ds and ds in p.get("absent_from", []))]
        if rows:
            out.append({"l": L, "st": lite.get("inventory_status", ""), "p": rows})
    return {"lects": out}


def write_site(D, out_dir, site_dir):
    """Write data/ (compact JSON, one folder per lect for its phonemes) and copy the viewer."""
    out_dir = Path(out_dir)
    data = out_dir / "data"
    if data.exists():
        shutil.rmtree(data)
    files = site_files(D)
    for rel, obj in files.items():
        p = data / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(obj, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    for f in Path(site_dir).rglob("*"):
        if f.is_file():
            dest = out_dir / f.relative_to(site_dir)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(f, dest)
    stamp_index(out_dir, files)
    return files


def stamp_index(out_dir, files):
    """Give every script and stylesheet in index.html a ?v=<content hash>, and
    the data a build stamp, so that a browser fetches them again after a
    deploy instead of using its cached copy."""
    index = Path(out_dir) / "index.html"
    if not index.exists():
        return
    digest = lambda b: hashlib.sha1(b).hexdigest()[:10]
    def stamp(m):
        f = Path(out_dir) / m.group(2)
        return f'{m.group(1)}="{m.group(2)}?v={digest(f.read_bytes())}"' if f.is_file() else m.group(0)
    html = re.sub(r'(src|href)="((?:js/)?[\w.-]+\.(?:js|css))"', stamp, index.read_text(encoding="utf-8"))
    build = digest(json.dumps(files.get("index.json"), ensure_ascii=False, sort_keys=True).encode("utf-8")
                   + json.dumps(files.get("sources.json"), ensure_ascii=False, sort_keys=True).encode("utf-8")
                   + str(len(files)).encode())
    html = html.replace("</head>", f'<meta name="asc-build" content="{build}">\n</head>', 1)
    index.write_text(html, encoding="utf-8")

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
    (re.compile(r"^implied \*\S+ of .* is kept as"), "an implied phoneme of an attested lect could not be written in IPA"),
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
    inh = Counter((r["inherit"] + (" (automatic, fewer than 13 phonemes known)" if r.get("inherit_auto") else ""))
                  or "(blank)" for r in D["lects"].values())
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
        out += ["| id | Question | Reading taken | Rows | Comments |", "|---|---|---|---|---|"]
        out += [f"| `{d['id']}` | {_cell(d['question'])} | {_cell(d['chosen_reading'])} | {len(d['rows']) or ''} "
                f"| {_cell(d.get('comments', ''))} |"
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
