"""Citations: labels, references in the Unified Style Sheet, works cited in notes."""
from __future__ import annotations

import re

def citation_label(author, year, suffix=""):
    """'Blust 1999b', 'Li & Tsuchida 2006', 'Ross et al. 2023' from 'Surname, Given; ...'."""
    names = [a.split(",")[0].strip() for a in author.split(";") if a.strip()]
    if not names:
        who = ""
    elif len(names) == 1:
        who = names[0]
    elif len(names) == 2:
        who = f"{names[0]} & {names[1]}"
    else:
        who = f"{names[0]} et al."
    return f"{who} {year}{suffix}".strip()


def _people(names, surname_first=True):
    """'Lee, Kee-dong & Judith W. Wang': the first name surname-first, the rest given-first."""
    out = []
    for i, n in enumerate(names):
        if "," in n and not (surname_first and i == 0):
            parts = [x.strip() for x in n.split(",")]
            # 'Stewart, Thomas W., Jr.' keeps its suffix after the given name
            n = " ".join([parts[1], parts[0]] + parts[2:])
        out.append(n.strip())
    if len(out) <= 1:
        return "".join(out)
    return ", ".join(out[:-1]) + " & " + out[-1]


def reference(r):
    """A source as a reference in the Unified Style Sheet for Linguistics.

    Returns segments [text, italic]. Italic: titles of books, dissertations and
    edited volumes, and journal names; nothing else. Without a pub_type only
    author, year and title are known, and the title is left upright.
    """
    seg = []
    def add(text, italic=False):
        if text:
            seg.append([text, italic])
    def stop(text):   # close a component, without doubling ?, ! or .
        return text if text.endswith(("?", "!", ".")) else text + "."
    authors = [a.strip() for a in r["author"].split(";") if a.strip()]
    eds = [a.strip() for a in r["editors"].split(";") if a.strip()]
    kind = r["pub_type"]
    add(stop(_people(authors)) + " " + r["year"] + r["year_suffix"] + ". ")
    title, cont = r["title"], r["container_title"]
    pub = ": ".join(x for x in (r["place"], r["publisher"]) if x)
    series = f" ({r['series']})" if r["series"] else ""
    if kind == "article":
        add(stop(title) + " ")
        add(cont, True)
        vol = r["volume"] + (f"({r['issue']})" if r["issue"] else "")
        tail = " ".join(x for x in (vol and stop(vol), r["pages"] and stop(r["pages"])) if x)
        add((" " + tail) if tail else ".")
    elif kind == "chapter":
        add(stop(title) + " In " + (f"{_people(eds, False)} ({'eds.' if len(eds) > 1 else 'ed.'}), " if eds else ""))
        add(cont, True)
        add((f", vol. {r['volume']}" if r["volume"] else "") + series + (f", {r['pages']}" if r["pages"] else "") + "."
            + (f" {stop(pub)}" if pub else ""))
    elif kind in ("book", "thesis"):
        add(title, True)
        tail = (f", {r['edition']}" if r["edition"] else "") + series
        add((stop(tail) if tail else "" if title.endswith(("?", "!")) else ".") + (f" {stop(pub)}" if pub else ""))
    else:   # presentation, dataset, other, or not yet classified
        add(stop(title))
        rest = " ".join(stop(x) for x in (cont, pub) if x)
        add((" " + rest) if rest else "")
    return seg   # the site appends the URL or DOI as a link


# 'Jackson (1983: 326; 1986: 203)', 'Lee & Wang (1984)', 'Bender et al. (2003a: 4)', 'Hughes 2020b: 200'
_NAME = r"(?:(?:van den|van der|van|de|von|den) )?[A-Z][\w‘-]+"
# Narrative 'Name (1983: 326; 1986)' (the bracket must open with a year), or bare 'Name 2020b'.
CITED = re.compile(rf"\b({_NAME}(?: (?:&|and) {_NAME}| et al\.)?)(?:['’]s)?,? "
                   rf"(\((?=(?:1[5-9]|20)\d\d)[^()]*\)|(?:1[5-9]|20)\d\d[a-z]?\b)")
YEAR = re.compile(r"(?<![\d:\-–] )(?<![\d\-–])\b((?:1[5-9]|20)\d\d)([a-z])?(?:\s*\[\d{4}\])?((?:, [a-z]\b)*)(?![\d\-–])")
NOT_AUTHORS = {"Table", "Tables", "Figure", "Section", "Appendix", "January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December", "Chapter", "In", "See", "Since", "Volume",
               "Proto", "Taipei", "Canberra", "Hsinchu", "Honolulu", "Tokyo", "Leiden", "Berlin", "Auckland"}


def cited_works(text, not_authors=frozenset()):
    """(author label, year, suffix) for each work a note cites by author and year."""
    out = []
    for m in CITED.finditer(text):
        who = re.sub(r" and ", " & ", m.group(1))
        words = {who.split()[0], who.split()[-1], who}
        if words & NOT_AUTHORS or words & not_authors or re.fullmatch(r"P[A-Za-z]{1,4}", who):
            continue
        for y in YEAR.finditer(m.group(2)):
            out.append((who, y.group(1), y.group(2) or ""))
            for extra in re.findall(r"[a-z]", y.group(3)):
                out.append((who, y.group(1), extra))
    return out
