"use strict";
// Static viewer over build/data/*.json. Hash routes mirror the planned URLs:
//   #/lects/                 page 1 (index)
//   #/lects/?reflex=pmp:R    page 1 pivoted on a proto-phoneme
//   #/lects/<lect>/          page 3 (inventory)
//   #/lects/<lect>/<ph>/     page 2 (phoneme)
//   #/sources/ and #/sources/<id>/

const app = document.getElementById("app");
const cache = {};
let INDEX, SOURCES, LECTS;

const PLACES = ["bilabial", "labiodental", "labial-velar", "dental", "alveolar", "postalveolar",
  "alveolo-palatal", "retroflex", "palatal", "velar", "uvular", "pharyngeal", "glottal"];
const MANNERS = ["plosive", "prenasalized-plosive", "implosive", "affricate", "prenasalized-affricate",
  "nasal", "trill", "prenasalized-trill", "tap", "fricative", "lateral-fricative", "approximant",
  "lateral-approximant"];
const BACKNESS = ["front", "central", "back"];
const HEIGHTS = ["close", "near-close", "close-mid", "mid", "open-mid", "near-open", "open"];

const esc = s => String(s ?? "").replace(/[&<>"']/g, c =>
  ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const label = s => esc(String(s || "").replace(/-/g, " "));
const badge = s => s ? `<span class="badge b-${esc(s)}">${label(s)}</span>` : "";

async function json(path) {
  if (!cache[path]) cache[path] = fetch(path).then(r => {
    if (!r.ok) throw new Error(`${path}: ${r.status}`);
    return r.json();
  });
  return cache[path];
}
const lectData = id => json(`data/${encodeURIComponent(id)}.json`);

function splitPid(pid) { const i = pid.indexOf(":"); return [pid.slice(0, i), pid.slice(i + 1)]; }
function isProto(lectId) { return LECTS[lectId]?.type === "proto-language"; }
function sym(pid) {
  const [l, s] = splitPid(pid);
  return isProto(l) ? `*${s}` : s;
}
function urlId(lectId, s) {
  return encodeURIComponent(isProto(lectId) ? "_" + s : s);
}
function phLink(pid, text) {
  const [l, s] = splitPid(pid);
  return `<a class="ipa" href="#/lects/${esc(l)}/${urlId(l, s)}/">${esc(text ?? sym(pid))}</a>`;
}
function lectLink(id) {
  return `<a href="#/lects/${esc(id)}/">${esc(LECTS[id]?.name || id)}</a>`;
}
function srcLink(id, page) {
  if (!id) return "";
  const s = SOURCES[id];
  const name = s ? `${esc(s.author.split(",")[0])} ${esc(s.year)}` : esc(id);
  return `<a href="#/sources/${esc(id)}/">${name}</a>${page ? `: ${esc(page)}` : ""}`;
}
function ancestorsOf(id) {
  const out = []; let cur = LECTS[id]?.parent_id;
  while (cur && LECTS[cur] && !out.includes(cur)) { out.unshift(cur); cur = LECTS[cur].parent_id; }
  return out;
}
function coverage(c) { return c ? `${c.with_descent}/${c.inventory_size}` : `<span class="muted">root</span>`; }

// ------------------------------------------------------------------ page 1

function sortLects(rows) {
  return rows.slice().sort((a, b) =>
    (a.type === "proto-language" ? 0 : 1) - (b.type === "proto-language" ? 0 : 1) ||
    a.name.localeCompare(b.name));
}

async function pageIndex(params) {
  const reflex = params.get("reflex");
  let pivot = null;
  if (reflex) {
    const [pl, ps] = splitPid(reflex);
    const d = await lectData(pl);
    const ph = d.phonemes.find(p => p.ipa === ps);
    if (!ph) throw new Error(`No phoneme ${reflex}`);
    pivot = { lect: pl, ph, byLect: {} };
    for (const r of ph.descendants) (pivot.byLect[r.child_lect_id] ||= []).push(r);
  }
  const state = { q: "", view: "grouped" };
  try { state.view = localStorage.getItem("asc-view") || "grouped"; } catch (e) {}

  app.innerHTML = `
    ${pivot ? `<div class="crumb"><a href="#/lects/">All lects</a> › reflexes of ${phLink(reflex)}</div>
      <h1>Reflexes of <span class="ipa">${esc(sym(reflex))}</span> <span class="muted" style="font-size:16px">${esc(LECTS[pivot.lect].name)}</span></h1>
      <p class="muted">Each descendant lect's reflex, through every intermediate stage. Lects outside ${esc(LECTS[pivot.lect].name)} are hidden.</p>`
      : `<h1>Lects</h1><p class="muted">Every language and proto-language in the database. Grouping follows established subgroups only.</p>`}
    <div class="controls">
      <input type="search" id="q" placeholder="Filter names and alternate names" aria-label="Filter">
      <span class="seg" role="group" aria-label="View">
        <button data-v="grouped">Grouped</button><button data-v="flat">A–Z</button>
      </span>
    </div>
    <div class="scroll"><table id="t"></table></div>`;

  const draw = () => {
    app.querySelectorAll(".seg button").forEach(b => b.classList.toggle("on", b.dataset.v === state.view));
    const q = state.q.toLowerCase();
    let rows = INDEX.lects.filter(l => !q || [l.name, ...l.alt_names].some(n => n.toLowerCase().includes(q)));
    if (pivot) rows = rows.filter(l => ancestorsOf(l.id).includes(pivot.lect));
    const head = `<tr><th>Name</th><th>Type</th><th>Glottocode</th><th>Nearest ancestor</th>
      <th>${pivot ? "Reflex" : "Coverage"}</th><th>Status</th></tr>`;
    const row = l => {
      let mid;
      if (pivot) {
        const rs = pivot.byLect[l.id] || [];
        mid = rs.length ? rs.map(r => r.child
          ? `${phLink(r.child)} <span class="muted">/ ${esc(r.environment)}</span>${r.via.length ? ` <span class="muted">via ${r.via.map(v => esc(sym(v))).join(" → ")}</span>` : ""}`
          : `<span class="blank">${label(r.blank_type)}</span> <span class="muted">/ ${esc(r.environment)}</span>`).join("<br>")
          : `<span class="blank">unentered</span>`;
      } else mid = coverage(l.coverage);
      return `<tr><td>${lectLink(l.id)}</td><td>${label(l.type)}</td>
        <td>${l.glottocode ? `<a href="https://glottolog.org/resource/languoid/id/${esc(l.glottocode)}" target="_blank" rel="noopener">${esc(l.glottocode)}</a>` : ""}</td>
        <td>${l.parent_id ? lectLink(l.parent_id) : ""}</td><td>${mid}</td><td>${badge(l.index_status)}</td></tr>`;
    };
    let body = "";
    if (state.view === "flat") {
      body = rows.slice().sort((a, b) => a.name.localeCompare(b.name)).map(row).join("");
    } else {
      const groups = {};
      for (const l of rows) (groups[l.subgroup_path.join(" › ") || "Unclassified"] ||= []).push(l);
      for (const g of Object.keys(groups).sort())
        body += `<tr class="group"><td colspan="6">${esc(g)}</td></tr>` + sortLects(groups[g]).map(row).join("");
    }
    app.querySelector("#t").innerHTML = head + (body || `<tr><td colspan="6" class="muted">${INDEX.lects.length ? "No lects match." : "No lects entered yet. Add rows to cldf/lects.csv."}</td></tr>`);
  };
  app.querySelector("#q").addEventListener("input", e => { state.q = e.target.value; draw(); });
  app.querySelectorAll(".seg button").forEach(b => b.addEventListener("click", () => {
    state.view = b.dataset.v; try { localStorage.setItem("asc-view", state.view); } catch (e) {} draw();
  }));
  draw();
}

// ------------------------------------------------------------------ page 3

function cellLink(L, p) {
  const title = [p.source_symbol && `source: ${p.source_symbol}`, `origin: ${p.origin}`].filter(Boolean).join(" · ");
  return `<a class="o-${esc(p.origin)}" href="#/lects/${esc(L)}/${esc(p.url_id)}/" title="${esc(title)}">${esc(isProto(L) ? "*" + p.ipa : p.ipa)}</a>`;
}

function consonantChart(L, cons) {
  const placed = cons.filter(p => PLACES.includes(p.place) && MANNERS.includes(p.manner));
  const unplaced = cons.filter(p => !placed.includes(p));
  let html = "";
  if (placed.length) {
    const places = PLACES.filter(pl => placed.some(p => p.place === pl));
    const manners = MANNERS.filter(m => placed.some(p => p.manner === m));
    html += `<div class="scroll"><table class="chart"><tr><th></th>${places.map(p => `<th>${label(p)}</th>`).join("")}</tr>`;
    for (const m of manners) {
      html += `<tr><th class="row">${label(m)}</th>`;
      for (const pl of places) {
        const here = placed.filter(p => p.place === pl && p.manner === m)
          .sort((a, b) => (a.voicing === "voiced") - (b.voicing === "voiced"));
        html += `<td>${here.map(p => cellLink(L, p)).join(" ")}</td>`;
      }
      html += "</tr>";
    }
    html += "</table></div>";
  }
  if (unplaced.length)
    html += `<p><span class="muted">Phonetic value not specified:</span> ${unplaced.map(p => `<span class="chart">${cellLink(L, p)}</span>`).join(" ")}</p>`;
  return html;
}

function vowelChart(L, vs) {
  const placed = vs.filter(p => BACKNESS.includes(p.place) && HEIGHTS.includes(p.manner));
  const unplaced = vs.filter(p => !placed.includes(p));
  let html = "";
  if (placed.length) {
    const heights = HEIGHTS.filter(h => placed.some(p => p.manner === h));
    html += `<table class="chart" style="width:auto"><tr><th></th>${BACKNESS.map(b => `<th>${b}</th>`).join("")}</tr>`;
    for (const h of heights) {
      html += `<tr><th class="row">${label(h)}</th>`;
      for (const b of BACKNESS) {
        const here = placed.filter(p => p.place === b && p.manner === h)
          .sort((x, y) => (x.rounding === "rounded") - (y.rounding === "rounded"));
        html += `<td>${here.map(p => cellLink(L, p)).join(" ")}</td>`;
      }
      html += "</tr>";
    }
    html += "</table>";
  }
  if (unplaced.length)
    html += `<p><span class="muted">Unplaced:</span> ${unplaced.map(p => `<span class="chart">${cellLink(L, p)}</span>`).join(" ")}</p>`;
  return html;
}

async function pageLect(L) {
  const d = await lectData(L);
  const C = d.phonemes.filter(p => p.class === "C");
  const V = d.phonemes.filter(p => p.class === "V");
  const O = d.phonemes.filter(p => p.class !== "C" && p.class !== "V");
  const ancestors = d.ancestors.map(lectLink).join(" › ");
  const statusNote = {
    "reverse-generated": "No source gives this inventory. It is the set of distinct reflexes in the correspondence data, and may miss loan phonemes or include allophones.",
    "edited": "Reverse-generated from the correspondence data, then corrected by hand. Every change is listed below.",
    "empty": "No inventory yet: no source gives one and no correspondences have been entered.",
  }[d.inventory_status];

  app.innerHTML = `
    <div class="crumb"><a href="#/lects/">Lects</a>${ancestors ? " › " + ancestors : ""}</div>
    <h1>${esc(d.name)} ${badge(d.inventory_status)}</h1>
    <dl class="info">
      ${d.alt_names.length ? `<dt>Also</dt><dd>${esc(d.alt_names.join(", "))}</dd>` : ""}
      <dt>Type</dt><dd>${label(d.type)}</dd>
      ${d.glottocode ? `<dt>Glottocode</dt><dd><a href="https://glottolog.org/resource/languoid/id/${esc(d.glottocode)}" target="_blank" rel="noopener">${esc(d.glottocode)}</a></dd>` : ""}
      ${d.iso639_3 ? `<dt>ISO 639-3</dt><dd>${esc(d.iso639_3)}</dd>` : ""}
      ${d.subgroup_path.length ? `<dt>Subgroup</dt><dd>${esc(d.subgroup_path.join(" > "))}</dd>` : ""}
      <dt>Nearest ancestor</dt><dd>${d.parent_id ? lectLink(d.parent_id) : '<span class="muted">none (root)</span>'}</dd>
      ${d.daughters.length ? `<dt>Daughters</dt><dd>${d.daughters.map(lectLink).join(", ")}</dd>` : ""}
      ${d.region ? `<dt>Region</dt><dd>${esc(d.region)}</dd>` : ""}
      <dt>Coverage</dt><dd>${d.coverage ? `${d.coverage.with_descent} of ${d.coverage.inventory_size} phonemes have a sourced descent` : "root proto-language"}</dd>
      <dt>Inventory source</dt><dd>${d.inventory_sources.map(s => srcLink(s)).join("; ") || '<span class="muted">none</span>'}</dd>
      <dt>Correspondences</dt><dd>${d.correspondence_sources.map(s => srcLink(s)).join("; ") || '<span class="muted">none</span>'}</dd>
      ${d.orthography_note ? `<dt>Orthography</dt><dd>${esc(d.orthography_note)}</dd>` : ""}
      ${d.notes ? `<dt>Notes</dt><dd>${esc(d.notes)}</dd>` : ""}
    </dl>
    ${statusNote ? `<div class="notice">${esc(statusNote)}</div>` : ""}
    ${C.length ? `<h2>Consonants</h2>${consonantChart(L, C)}` : ""}
    ${V.length ? `<h2>Vowels</h2>${vowelChart(L, V)}` : ""}
    ${O.length ? `<h2>Other</h2><p>${O.map(p => `<span class="chart">${cellLink(L, p)}</span>`).join(" ")}</p>` : ""}
    ${d.phonemes.length ? `<p class="legend">Click a symbol for its history. Hover for the source's own symbol.
      ${d.inventory_status !== "sourced" ? "Dotted underline = generated; solid = added by hand." : ""}</p>` : ""}
    ${d.inventory_diff.length ? `<h2>Hand edits to the generated inventory</h2>
      <table><tr><th>Change</th><th>Phoneme</th><th>Reason</th><th>Source</th></tr>
      ${d.inventory_diff.map(x => `<tr><td>${badge(x.op === "add" ? "manual-add" : "suppressed")}</td>
        <td class="ipa">${esc(x.ipa)}</td><td>${esc(x.reason)}</td><td>${srcLink(x.source_id)}</td></tr>`).join("")}</table>` : ""}`;
}

// ------------------------------------------------------------------ page 2

function chainHtml(chain, herePid) {
  let html = `<div class="chain">`;
  chain.forEach((e, i) => {
    if (i === 0) html += node(e.parent, herePid);
    const meta = [esc(e.environment), e.status ? label(e.status) : "",
      e.evidence_count != null ? `n=${e.evidence_count}` : ""].filter(Boolean).join(" · ");
    html += `<span class="arrow"><span>${meta}</span><span class="glyph">→</span><span>${srcLink(e.source_id, e.page)}</span></span>`;
    html += node(e.child, herePid);
  });
  return html + "</div>";
}
function node(pid, herePid) {
  const [l] = splitPid(pid);
  return `<span class="node${pid === herePid ? " here" : ""}"><span class="sym">${pid === herePid ? esc(sym(pid)) : phLink(pid)}</span><span class="lect">${esc(LECTS[l]?.name || l)}</span></span>`;
}

async function pagePhoneme(L, uid) {
  const d = await lectData(L);
  const ph = d.phonemes.find(p => p.url_id === uid || p.url_id === encodeURIComponent(decodeURIComponent(uid)));
  if (!ph) throw new Error(`No phoneme ${decodeURIComponent(uid)} in ${L}`);
  const proto = isProto(L);
  const ancestorPids = [...new Set(ph.ancestry.flatMap(c => c.map(e => e.parent)))];

  const descRows = ph.descendants.map(r => `<tr class="${r.via.length ? "dim" : ""}">
      <td>${lectLink(r.child_lect_id)}${r.via.length ? `<br><span class="muted">via ${r.via.map(v => esc(sym(v))).join(" → ")}</span>` : ""}</td>
      <td>${r.child ? phLink(r.child) : `<span class="blank">${label(r.blank_type)}</span>`}</td>
      <td><code>${esc(r.environment)}</code></td>
      <td>${r.child ? badge(r.status) : badge(r.blank_type)}</td>
      <td>${r.evidence_count ?? ""}</td>
      <td>${srcLink(r.source_id, r.page)}</td>
      <td>${esc(r.notes)}</td></tr>`).join("");

  app.innerHTML = `
    <div class="crumb"><a href="#/lects/">Lects</a> › ${lectLink(L)}</div>
    <h1><span class="ipa">${esc(proto ? "*" + ph.ipa : "/" + ph.ipa + "/")}</span>
      <span class="muted" style="font-size:16px">in ${lectLink(L)}</span> ${badge(ph.origin)}</h1>
    <dl class="info">
      ${ph.source_symbol && ph.source_symbol !== ph.ipa ? `<dt>Source symbol</dt><dd class="ipa">${esc(ph.source_symbol)}</dd>` : ""}
      ${[ph.voicing, ph.rounding, ph.place, ph.manner].some(Boolean) ? `<dt>Description</dt><dd>${label([ph.voicing, ph.rounding, ph.place, ph.manner].filter(Boolean).join(" "))}</dd>` : ""}
      ${ph.source_id ? `<dt>Inventory source</dt><dd>${srcLink(ph.source_id, ph.page)}</dd>` : ""}
      ${ph.reason ? `<dt>Reason</dt><dd>${esc(ph.reason)}</dd>` : ""}
      ${ph.notes ? `<dt>Notes</dt><dd>${esc(ph.notes)}</dd>` : ""}
    </dl>
    ${ph.notation.length ? `<h3>Notation by reconstruction system</h3>
      <table style="width:auto"><tr><th>System</th><th>Symbol</th><th>Source</th></tr>
      ${ph.notation.map(n => `<tr><td>${esc(n.system)}</td><td class="ipa">*${esc(n.symbol)}</td><td>${srcLink(n.source_id, n.page)}</td></tr>`).join("")}</table>` : ""}

    <h2>Ancestry</h2>
    ${ph.ancestry.length
      ? (ph.ancestry.length > 1 ? `<p class="muted">${ph.ancestry.length} chains: this phoneme continues more than one ancestor segment.</p>` : "")
        + ph.ancestry.map(c => chainHtml(c, ph.id)).join("")
      : `<p class="muted">${d.parent_id ? "No correspondence entered for this phoneme yet." : "Root proto-language: no ancestor."}</p>`}
    ${ancestorPids.length ? `<p>Same ancestor across the family: ${ancestorPids.map(p =>
        `<a href="#/lects/?reflex=${encodeURIComponent(p)}">all reflexes of <span class="ipa">${esc(sym(p))}</span> (${esc(LECTS[splitPid(p)[0]].name)})</a>`).join(" · ")}</p>` : ""}

    <h2>Descent</h2>
    ${ph.descendants.length ? `
      <p><a href="#/lects/?reflex=${encodeURIComponent(ph.id)}">Open as a table of all lects →</a></p>
      <div class="scroll"><table><tr><th>Daughter lect</th><th>Reflex</th><th>Environment</th><th>Status</th><th>Evidence</th><th>Source</th><th>Notes</th></tr>${descRows}</table></div>`
      : `<p class="muted">${d.daughters.length ? "No descendant reflexes entered." : "No daughter lects in the database."}</p>`}`;
}

// ------------------------------------------------------------------ sources

function pageSources(id) {
  const list = id ? [SOURCES[id]].filter(Boolean) : Object.values(SOURCES);
  if (id && !list.length) throw new Error(`No source ${id}`);
  app.innerHTML = `<div class="crumb"><a href="#/sources/">Sources</a></div><h1>${id ? esc(id) : "Sources"}</h1>
    <table><tr><th>Id</th><th>Citation</th><th>Kind</th><th>Notes</th></tr>
    ${list.map(s => `<tr><td><a href="#/sources/${esc(s.id)}/">${esc(s.id)}</a></td>
      <td>${esc(s.author)} (${esc(s.year)}). <i>${esc(s.title)}</i>.${s.url_or_doi ? ` <a href="${esc(/^10\./.test(s.url_or_doi) ? "https://doi.org/" + s.url_or_doi : s.url_or_doi)}" target="_blank" rel="noopener">${esc(s.url_or_doi)}</a>` : ""}</td>
      <td>${esc(s.kind)}</td><td>${esc(s.notes)}</td></tr>`).join("")}</table>`;
}

// ------------------------------------------------------------------ router

async function route() {
  const hash = location.hash.replace(/^#/, "") || "/lects/";
  const [path, query] = hash.split("?");
  const parts = path.split("/").filter(Boolean);
  try {
    if (parts[0] === "sources") pageSources(parts[1] && decodeURIComponent(parts[1]));
    else if (parts[0] !== "lects" || parts.length === 1) await pageIndex(new URLSearchParams(query || ""));
    else if (parts.length === 2) await pageLect(decodeURIComponent(parts[1]));
    else await pagePhoneme(decodeURIComponent(parts[1]), parts[2]);
  } catch (e) {
    app.innerHTML = `<h1>Not found</h1><p class="muted">${esc(e.message)}</p><p><a href="#/lects/">Back to all lects</a></p>`;
  }
  window.scrollTo(0, 0);
}

(async () => {
  try {
    [INDEX, { sources: SOURCES }] = await Promise.all([json("data/index.json"), json("data/sources.json")]);
    SOURCES = Object.fromEntries(SOURCES.map(s => [s.id, s]));
    LECTS = Object.fromEntries(INDEX.lects.map(l => [l.id, l]));
  } catch (e) {
    app.innerHTML = `<h1>No data</h1><p>Run <code>python3 build.py</code> first. (${esc(e.message)})</p>`;
    return;
  }
  window.addEventListener("hashchange", route);
  route();
})();
