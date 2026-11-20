#!/usr/bin/env python3
"""Validate the CLDF tables and derive per-lect JSON for the site.

    python3 build.py                 # validate cldf/, write build/data/ and copy site/ to build/
    python3 build.py --check         # validate only, write nothing
    python3 build.py --data DIR --out DIR

Exit status is 1 if any error is found (the build fails rather than
rendering a misleading page). Warnings are reported but do not fail.

Standard library only (Python 3.9+).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# The modules, re-exported so that tools and tests can keep using build.<name>.
from asc.schema import *  # noqa: E402,F401,F403
from asc.load import *  # noqa: E402,F401,F403
from asc.cite import *  # noqa: E402,F401,F403
from asc.cite import _people  # noqa: E402,F401
from asc.validate import *  # noqa: E402,F401,F403
from asc.derive import *  # noqa: E402,F401,F403
from asc.export import *  # noqa: E402,F401,F403


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=str(ROOT / "cldf"), help="directory with the CSV tables")
    ap.add_argument("--out", default=str(ROOT / "build"), help="output directory")
    ap.add_argument("--check", action="store_true", help="validate only")
    ap.add_argument("--quiet", action="store_true", help="hide notes")
    ap.add_argument("--status", metavar="FILE", help="also rewrite the generated part of this STATUS.md")
    args = ap.parse_args(argv)

    rep = Report()
    tables = load(Path(args.data), rep)
    counts = {k: len(v) for k, v in tables.items()}   # as entered (the build adds implied rows)
    D = None if rep.fatal else validate_and_derive(tables, rep)
    if args.status and D is not None and not rep.errors:
        write_status(args.status, status_md(tables, D, rep, counts))
    if args.quiet:
        rep.notes = []
    print(rep.text())

    if rep.errors or D is None:
        print("\nBuild failed: fix the errors above.", file=sys.stderr)
        return 1
    if args.check:
        return 0

    files = write_site(D, args.out, ROOT / "site")
    (Path(args.out) / "report.txt").write_text(rep.text() + "\n", encoding="utf-8")
    print(f"\nWrote {len(D['lects'])} lect file(s) and {len(files) - len(D['lects']) - 2} phoneme file(s) "
          f"to {Path(args.out) / 'data'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
