#!/usr/bin/env python3
"""Write an .xlsx workbook to upload to Google Drive as the data-entry sheet.

    .venv/bin/python tools/make_sheet_template.py [--from cldf] [out.xlsx]

Tabs match the CSV tables exactly (same names, same headers). Columns with a
fixed vocabulary get dropdowns; lect_id/source_id columns get dropdowns fed
from the lects/sources tabs. Every cell is plain text so Sheets never turns
'2009a', '_#' or '40' into dates, formulas or numbers. Vocabularies come from
build.py, so the sheet and the validator cannot drift apart.

With --from DIR, existing CSV rows are copied in (to seed the sheet).
"""
import argparse
import csv
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402

ROWS = 2000  # rows pre-formatted as text and covered by dropdowns

LISTS = {
    "lect_type": sorted(build.LECT_TYPES),
    "source_kind": sorted(build.SOURCE_KINDS),
    "class": ["C", "V", "tone", "other"],
    "place": sorted(build.PLACES_C) + list(build.PLACES_V),
    "manner": sorted(build.MANNERS_C) + list(build.MANNERS_V),
    "voicing": sorted(build.VOICING),
    "rounding": sorted(build.ROUNDING),
    "origin": ["sourced", "manual-add", "suppressed"],
    "status": ["regular", "sporadic", "loan-stratum", "disputed"],
    "blank_type": ["not-attested", "lexeme-replaced", "irregular", "loan", "disputed"],
    "environment": ["elsewhere", "#_", "_#", "V_V", "_i", "_u", "_a", "C_", "_C", "#_V", "V_#"],
}

# (tab, column) -> list name, or "lects"/"sources" for an id from that tab.
VALIDATION = {
    ("sources", "kind"): "source_kind",
    ("lects", "type"): "lect_type",
    ("lects", "parent_id"): "lects",
    ("phonemes", "lect_id"): "lects",
    ("phonemes", "class"): "class",
    ("phonemes", "place"): "place",
    ("phonemes", "manner"): "manner",
    ("phonemes", "voicing"): "voicing",
    ("phonemes", "rounding"): "rounding",
    ("phonemes", "origin"): "origin",
    ("phonemes", "source_id"): "sources",
    ("correspondences", "child_lect_id"): "lects",
    ("correspondences", "status"): "status",
    ("correspondences", "blank_type"): "blank_type",
    ("correspondences", "source_id"): "sources",
    ("notation_map", "lect_id"): "lects",
    ("notation_map", "source_id"): "sources",
}
# Suggestions only: free text is allowed (environment can be any condition).
SOFT = {("correspondences", "environment"): "environment"}

REQUIRED = {
    "sources": {"id", "author", "year", "title", "kind"},
    "lects": {"id", "name", "type"},
    "phonemes": {"lect_id", "ipa", "class", "origin"},
    "correspondences": {"child_lect_id", "parent_phoneme", "environment", "source_id"},
    "notation_map": {"lect_id", "phoneme", "system", "symbol"},
}

HELP = [
    ("Austronesian Sound Correspondence Dictionary: data entry", True),
    ("", False),
    ("Enter data in the five tabs: sources, lects, phonemes, correspondences, notation_map.", False),
    ("Do not rename tabs or change row 1 (the headers). Bold headers are required columns.", False),
    ("Order: add the source, then the lect (its parent proto-language first), then phonemes, then correspondences, then notation.", False),
    ("Never type * in a symbol: write R, not *R. The site adds the asterisk.", False),
    ("A correspondence with no reflex must have a blank_type. Environment is never blank: use 'elsewhere'.", False),
    ("Every phoneme of a proto-language needs a notation_map row (system = canonical at least).", False),
    ("", False),
    ("Publishing: GitHub copies this sheet every hour (or when you press 'Run workflow' on the 'Sync from Google Sheets' action).", False),
    ("If the data passes every check, the site updates. If not, nothing changes and the run fails, listing errors as tab.csv:ROW, where ROW is the row number in this sheet.", False),
    ("Full column reference: README.md in the GitHub repository.", False),
    ("", False),
    ("Other tabs (like this one and _lists) are ignored by the sync.", False),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out", nargs="?", default=str(ROOT / "build" / "data-entry-template.xlsx"))
    ap.add_argument("--from", dest="src", help="directory of CSVs to copy rows from")
    args = ap.parse_args()

    wb = Workbook()
    about = wb.active
    about.title = "about"
    for i, (text, bold) in enumerate(HELP, start=1):
        c = about.cell(row=i, column=1, value=text)
        c.font = Font(bold=bold, size=13 if bold else 11)
    about.column_dimensions["A"].width = 140

    lists = wb.create_sheet("_lists")
    list_ref = {}
    for j, (name, values) in enumerate(LISTS.items(), start=1):
        col = get_column_letter(j)
        lists.cell(row=1, column=j, value=name).font = Font(bold=True)
        for i, v in enumerate(values, start=2):
            lists.cell(row=i, column=j, value=v)
        list_ref[name] = f"='_lists'!${col}$2:${col}${len(values) + 1}"
    list_ref["lects"] = f"=lects!$A$2:$A${ROWS}"
    list_ref["sources"] = f"=sources!$A$2:$A${ROWS}"

    head_fill = PatternFill("solid", fgColor="EDEAE3")
    for tab, cols in build.TABLES.items():
        ws = wb.create_sheet(tab)
        rows = []
        if args.src:
            p = Path(args.src) / f"{tab}.csv"
            if p.exists():
                rows = list(csv.reader(p.read_text(encoding="utf-8").splitlines()))[1:]
        for j, name in enumerate(cols, start=1):
            c = ws.cell(row=1, column=j, value=name)
            c.font = Font(bold=name in REQUIRED[tab])
            c.fill = head_fill
            ws.column_dimensions[get_column_letter(j)].width = max(12, len(name) + 4)
        for i, r in enumerate(rows, start=2):
            for j, v in enumerate(r[:len(cols)], start=1):
                if v:
                    ws.cell(row=i, column=j, value=v)
        for j in range(1, len(cols) + 1):
            dim = ws.column_dimensions[get_column_letter(j)]
            dim.number_format = "@"  # whole column is plain text
            for i in range(1, len(rows) + 2):
                ws.cell(row=i, column=j).number_format = "@"
        ws.freeze_panes = "A2"
        for (t, colname), lst in list(VALIDATION.items()) + list(SOFT.items()):
            if t != tab:
                continue
            letter = get_column_letter(cols.index(colname) + 1)
            strict = (t, colname) in VALIDATION
            dv = DataValidation(type="list", formula1=list_ref[lst], allow_blank=True,
                                showErrorMessage=strict, errorStyle="stop" if strict else "information",
                                error=f"Choose a value from the list for {colname}." if strict else None)
            dv.add(f"{letter}2:{letter}{ROWS}")
            ws.add_data_validation(dv)

    lists.sheet_state = "hidden"
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out)
    print(out)


if __name__ == "__main__":
    main()
