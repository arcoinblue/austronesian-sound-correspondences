"use strict";
// The reference list (#/sources/) and one work's record (#/sources/<id>/).

// A long list of lects is cut in the full list (Bender et al. 2003a is cited in 20); the
// source's own page gives all of them.
function lectList(ids, all) {
  if (all || ids.length <= 6) return ids.map(lectLink).join(", ");
  return `${ids.slice(0, 4).map(lectLink).join(", ")}<details class="morelects"><summary>and ${ids.length - 4} more</summary>${ids.slice(4).map(lectLink).join(", ")}</details>`;
}

const plural = (k, w) => `${k.toLocaleString("en")} ${w}${k === 1 ? "" : "s"}`;

// What a work is used for, in words: the lects, then what was taken from it.
function usedFor(s, all) {
  const c = s.cited_by;
  if (!c) return "";
  const kinds = [[c.correspondences, "correspondence"], [c.phonemes, "phoneme"], [c.notation, "notation"], [c.allophones || 0, "allophone"]]
    .filter(([k]) => k).map(([k, w]) => plural(k, w)).join(", ");
  const relayed = c.relays.reduce((a, r) => a + r.rows, 0);
  const inNotes = c.notes ? `Mentioned in the notes${c.note_lects?.length ? " on " + lectList(c.note_lects, all) : ""}` : "";
  if (!kinds && !relayed) return inNotes || "Not used yet";
  return [
    c.lects.length ? `Used for ${lectList(c.lects, all)}` : "",
    kinds,
    ...c.read_via.map(v => `${plural(v.rows, "statement")} read through ${srcLink(v.source_id)}`),
    relayed ? `relays ${c.relays.map(r => srcLink(r.source_id)).join(", ")}` : "",
  ].filter(Boolean).join(" · ");
}

// Notes on a source say when and from which file it was read; the page keeps what a reader can use.
function sourceNote(t) {
  return tidy(t).replace(/Consulted directly on \d+ \w+ \d{4}/g, "Read directly")
    .replace(/\s*\([^)]*(?:PDF|Downloads|scan)[^)]*\)/g, "");
}

// sources.json (loaded by every page) has only what a citation link needs; the
// reference list fetches the full records.
let SOURCES_FULL;
async function pageSources(id) {
  if (!SOURCES_FULL) SOURCES_FULL = Object.fromEntries((await json("data/sources_full.json")).sources.map(s => [s.id, s]));
  if (id && !SOURCES_FULL[id]) throw new Error(`No source ${id}`);
  // The reference as the build wrote it, in the Unified Style Sheet for Linguistics.
  const ref = s => (s.reference || []).map(([t, i]) => i ? `<i>${esc(t)}</i>` : esc(t)).join("")
    + (s.url_or_doi ? ` <a href="${esc(/^10\./.test(s.url_or_doi) ? "https://doi.org/" + s.url_or_doi : s.url_or_doi)}" target="_blank" rel="noopener">${esc(s.url_or_doi.replace(/^https?:\/\//, ""))}</a>` : "");
  if (id) {
    const s = SOURCES_FULL[id];
    app.innerHTML = `<div class="crumb"><a href="#/sources/">Sources</a></div><h1>${esc(s.label || id)}</h1>
      <p class="bibentry">${ref(s)}</p>
      <dl class="info">
        ${s.kind ? `<dt>Kind</dt><dd>${esc(s.kind)}</dd>` : ""}
        <dt>Use</dt><dd>${usedFor(s, true)}</dd>
        ${s.notes ? `<dt>Notes</dt><dd>${esc(sourceNote(s.notes))}</dd>` : ""}
      </dl>`;
    return;
  }
  const list = Object.values(SOURCES_FULL);
  const used = s => { const c = s.cited_by; return c && c.phonemes + c.correspondences + c.notation + (c.allophones || 0) + c.relays.length > 0; };
  const idle = list.filter(s => !used(s)).length;
  // A reference list: by first author's surname, then year.
  list.sort((p, q) => p.author.localeCompare(q.author) || String(p.year + (p.year_suffix || "")).localeCompare(q.year + (q.year_suffix || "")));
  app.innerHTML = `<h1>Sources</h1>
    <p class="subline">${list.length} works${idle ? `; ${list.length - idle} supply data, the rest are cited in notes or not used yet` : ""}.</p>
    <div class="controls"><input id="bq" type="search" placeholder="Author, year, title or lect" aria-label="Filter the sources" autocomplete="off"><span class="muted" id="bcount"></span></div>
    <ol class="bib">${list.map(s => `<li id="${esc(s.id)}"${used(s) ? "" : ' class="idle"'}><div class="bibentry">${ref(s)}</div>
      <div class="bibmeta">${usedFor(s, false)} · <a href="#/sources/${esc(s.id)}/">details</a></div></li>`).join("")}</ol>`;
  const q = app.querySelector("#bq"), items = [...app.querySelectorAll("ol.bib > li")], count = app.querySelector("#bcount");
  const text = items.map(li => li.textContent.toLowerCase());
  const apply = () => {
    const words = q.value.toLowerCase().split(/\s+/).filter(Boolean);
    let n = 0;
    items.forEach((li, i) => { const on = words.every(w => text[i].includes(w)); li.hidden = !on; n += on; });
    count.textContent = words.length ? `${n} of ${items.length}` : "";
    setQuery({ q: q.value.trim() });
  };
  q.value = new URLSearchParams(location.hash.split("?")[1] || "").get("q") || "";
  q.addEventListener("input", apply);
  if (q.value) apply();
}
