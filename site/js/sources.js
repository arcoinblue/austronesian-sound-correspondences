"use strict";
// The reference list (#/sources/ and #/sources/<id>/).

// A long list of lects is cut in the full list (Bender et al. 2003a is cited in 20); the
// source's own page gives all of them.
function lectList(ids, all) {
  if (all || ids.length <= 8) return ids.map(lectLink).join(", ");
  return `${ids.slice(0, 6).map(lectLink).join(", ")}<details class="morelects"><summary>and ${ids.length - 6} more</summary>${ids.slice(6).map(lectLink).join(", ")}</details>`;
}

function citedBy(s, all) {
  const c = s.cited_by;
  if (!c) return "";
  const n = c.phonemes + c.correspondences + c.notation + (c.allophones || 0);
  const kinds = [[c.correspondences, "correspondence"], [c.phonemes, "phoneme"], [c.notation, "notation"], [c.allophones || 0, "allophone"]]
    .filter(([k]) => k).map(([k, w]) => `${k} ${w} row${k === 1 ? "" : "s"}`).join(", ");
  const relayed = c.relays.reduce((a, r) => a + r.rows, 0);
  // A work cited only in running text (a lect's notes, another source's notes): no row rests on it.
  const inNotes = c.notes ? `<span class="muted">named in notes ${c.notes} time${c.notes === 1 ? "" : "s"}${c.note_lects?.length ? " (" : ""}</span>${(c.note_lects || []).map(lectLink).join(", ")}${c.note_lects?.length ? '<span class="muted">)</span>' : ""}` : "";
  if (!n && !relayed) return inNotes ? `<span class="badge">notes only</span><br>${inNotes}` : `<span class="badge b-suppressed">not cited</span>`;
  return [
    n ? `<b>${n}</b> row${n === 1 ? "" : "s"}: ${kinds}` : "",
    // Indirect citations sit under the original work, grouped by where it was read.
    ...c.read_via.map(v => `<span class="muted">↳ ${v.rows} read via</span> ${srcLink(v.source_id)}`),
    relayed ? `<span class="muted">relays ${relayed} row${relayed === 1 ? "" : "s"} from</span> ${c.relays.map(r => `${srcLink(r.source_id)} <span class="muted">(${r.rows})</span>`).join(", ")}` : "",
    c.lects.length ? `<span class="muted">in</span> ${lectList(c.lects, all)}` : "",
  ].filter(Boolean).join("<br>");
}

function pageSources(id) {
  const list = id ? [SOURCES[id]].filter(Boolean) : Object.values(SOURCES);
  if (id && !list.length) throw new Error(`No source ${id}`);
  const rowless = list.filter(s => s.cited_by && !(s.cited_by.phonemes + s.cited_by.correspondences + s.cited_by.notation + (s.cited_by.allophones || 0) + s.cited_by.relays.length));
  const idle = rowless.length, notesOnly = rowless.filter(s => s.cited_by.notes).length;
  // A reference list: by first author's surname, then year.
  list.sort((p, q) => p.author.localeCompare(q.author) || String(p.year + (p.year_suffix || "")).localeCompare(q.year + (q.year_suffix || "")));
  // The reference as the build wrote it, in the Unified Style Sheet for Linguistics.
  const ref = s => (s.reference || []).map(([t, i]) => i ? `<i>${esc(t)}</i>` : esc(t)).join("")
    + (s.url_or_doi ? ` <a href="${esc(/^10\./.test(s.url_or_doi) ? "https://doi.org/" + s.url_or_doi : s.url_or_doi)}" target="_blank" rel="noopener">${esc(s.url_or_doi)}</a>` : "");
  app.innerHTML = `<div class="crumb"><a href="#/sources/">Sources</a></div><h1>${id ? esc(SOURCES[id].label || id) : "Sources"}</h1>
    ${!id && idle ? `<p class="muted">${idle} of ${list.length} sources are not cited by any row yet${notesOnly ? `; ${notesOnly} of them are named in notes` : ""}.</p>` : ""}
    <div class="scroll"><table class="refs"><tr><th>Reference</th><th class="kd">Kind</th><th>Cited by</th><th class="nt">Notes</th></tr>
    ${list.map(s => `<tr><td class="ref" id="${esc(s.id)}">${ref(s)}<br><a class="muted refid" href="#/sources/${esc(s.id)}/">${esc(s.id)}</a></td>
      <td class="kd">${esc(s.kind)}</td><td>${citedBy(s, !!id)}</td><td class="nt">${fold(s.notes, 140)}</td></tr>`).join("")}</table></div>`;
}
