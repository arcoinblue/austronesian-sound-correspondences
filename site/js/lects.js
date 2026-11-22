"use strict";
// Page 1: the lect list (#/lects/), and the same list pivoted on a proto-phoneme (#/lects/?reflex=pmp:R).

// How each list was left (the full list, and each reflex table): open groups,
// filter, the "hide empty" box. Kept while the site is open, so coming back
// from a lect finds the list as it was; the full list's open groups are also
// kept across visits.
const LIST_STATE = {};

async function pageIndex(params) {
  const reflex = params.get("reflex");
  let pivot = null;
  if (reflex) {
    const [pl, ps] = splitPid(reflex);
    const d = await lectData(pl);
    const ph = d.phonemes.find(p => p.ipa === ps);
    if (!ph) throw new Error(`No phoneme ${reflex}`);
    const det = await phonemeData(ph);
    pivot = { lect: pl, ph, byLect: {}, alt: new Set() };
    for (const r of det.descendants) (pivot.byLect[r.child_lect_id] ||= []).push(r);
    // Lects another classification puts under the pivot's lect: their rows, through the pivot's phoneme.
    for (const r of det.alt_descendants || []) {
      (pivot.byLect[r.child_lect_id] ||= []).push({ ...r, via: [] });
      pivot.alt.add(r.child_lect_id);
    }
  }
  // Lects that other classifications put under each node.
  const altKids = {};
  for (const l of INDEX.lects) for (const a of l.alt_parents || []) (altKids[a.parent_id] ||= []).push({ lect: l, source_id: a.source_id });
  const key = reflex || "";
  const mem = LIST_STATE[key] ||= { q: "", hideEmpty: true, open: null };
  if (!mem.open && !pivot) try {
    const saved = JSON.parse(localStorage.getItem("asc-open") || "null");
    if (Array.isArray(saved)) mem.open = new Set(saved);
  } catch (e) {}
  const state = { q: mem.q, view: "tree", hideEmpty: mem.hideEmpty };
  try { state.view = localStorage.getItem("asc-view") === "flat" ? "flat" : "tree"; } catch (e) {}

  // The tree: daughters under their nearest ancestor. In a reflex table the
  // pivot's own daughters are the top level.
  const pool = INDEX.lects.filter(l => !pivot || ancestorsOf(l.id).includes(pivot.lect));
  const inPool = new Set(pool.map(l => l.id));
  const kids = {};
  for (const l of pool) (kids[inPool.has(l.parent_id) ? l.parent_id : ""] ||= []).push(l);
  // Branches first, then leaves, each by name.
  for (const k of Object.values(kids))
    k.sort((x, y) => (kids[y.id] ? 1 : 0) - (kids[x.id] ? 1 : 0) || x.name.localeCompare(y.name));
  // Open to start with: the top two levels; everything in a reflex table.
  const open = mem.open ||= new Set();
  if (!open.size) {
    for (const r of kids[""] || []) { open.add(r.id); for (const k of kids[r.id] || []) open.add(k.id); }
    if (pivot) pool.forEach(l => open.add(l.id));
  }
  const remember = () => {
    mem.q = state.q; mem.hideEmpty = state.hideEmpty;
    if (!pivot) try { localStorage.setItem("asc-open", JSON.stringify([...open])); } catch (e) {}
  };
  // The clades above a lect, shown when the pointer rests on its name.
  const pathOf = l => ancestorsOf(l.id).map(a => LECTS[a]?.clade || LECTS[a]?.name || a).join(" › ");

  app.innerHTML = `
    ${pivot ? `<div class="crumb"><a href="#/lects/">All lects</a> › reflexes of ${phLink(reflex)}</div>
      <h1>Reflexes of <span class="ipa">${esc(sym(reflex))}</span> <span class="muted" style="font-size:16px">${esc(LECTS[pivot.lect].name)}</span></h1>
      <p class="muted">Each descendant lect's reflex, through every intermediate stage. Lects outside ${esc(LECTS[pivot.lect].name)} are hidden.</p>`
      : `<h1>Lects</h1><p class="muted">Every language and reconstructed stage in the database. Groups are named after the clade and headed by its proto-language; click an arrow to open or close one.</p>`}
    <div class="controls">
      <input type="search" id="q" placeholder="Filter names and alternate names" aria-label="Filter">
      <span class="seg" role="group" aria-label="View">
        <button data-v="tree">Tree</button><button data-v="flat">A–Z</button>
      </span>
      <span class="treeonly"><button class="more" id="openall">Expand all</button> <button class="more" id="closeall">Collapse</button></span>
      <label class="muted" style="font-size:13px"><input type="checkbox" id="hideempty" checked> Hide lects with no data</label>
      <span class="muted" id="count"></span>
    </div>
    <div class="scroll"><table id="t" class="lects"></table></div>`;

  const draw = () => {
    app.querySelectorAll(".seg button").forEach(b => b.classList.toggle("on", b.dataset.v === state.view));
    const tree = state.view === "tree";
    app.querySelector(".treeonly").hidden = !tree;
    const q = state.q.toLowerCase();
    const hit = l => !q || [l.name, ...(l.alt_names || []), ...(l.overlap_groups || [])].some(n => n.toLowerCase().includes(q));
    // A lect with no rows and no daughters with rows says nothing yet.
    const hasData = l => l.index_status !== "empty" || (kids[l.id] || []).some(hasData);
    const visible = l => !(state.hideEmpty && !pivot && !hasData(l));
    const head = `<tr><th>Name</th><th>Type</th><th>Glottocode</th>${tree ? "" : "<th>Nearest ancestor</th>"}
      <th>${pivot ? "Reflex" : "Coverage"}</th></tr>`;
    const cells = l => {
      let mid;
      if (pivot) {
        const rs = pivot.byLect[l.id] || [];
        mid = rs.length ? rs.map(r => r.child
          ? `${phLink(r.child)} <span class="muted">/ ${r.fusion ? fusionLabel(r.fusion) + " fuse" : esc(r.environment)}</span> ${badge(r.status)}${r.via.length ? ` <span class="muted">via ${r.via.map(v => esc(sym(v))).join(" → ")}</span>` : ""}${r.alt_via ? ` <span class="muted">from ${esc(LECTS[splitPid(r.parent)[0]]?.name || "")} ${esc(sym(r.parent))}</span>` : ""}`
          : `<span class="blank">no reflex</span> <span class="muted">/ ${esc(r.environment)}</span> ${badge(r.blank_type)}`).join("<br>")
          : `<span class="blank">unentered</span>`;
      } else mid = coverage(l.coverage) + ({ "changes-only": " " + badge("changes-only"), empty: "", generated: "" }[l.index_status] ?? "");
      return `<td class="nw">${label(l.type)}</td>
        <td>${l.glottocode ? `<a href="https://glottolog.org/resource/languoid/id/${esc(l.glottocode)}" target="_blank" rel="noopener">${esc(l.glottocode)}</a>` : ""}</td>
        ${tree ? "" : `<td>${l.parent_id ? lectLink(l.parent_id) : ""}</td>`}<td>${mid}</td>`;
    };
    let body = "", shown = 0;
    if (!tree) {
      const rows = pool.filter(l => hit(l) && visible(l)).sort((a, b) => a.name.localeCompare(b.name));
      shown = rows.length;
      body = rows.map(l => `<tr><td>${lectLink(l.id)}</td>${cells(l)}</tr>`).join("");
    } else {
      // A filter keeps the matches and the ancestors that lead to them.
      const has = l => hit(l) || (kids[l.id] || []).some(has);
      const shows = l => !((q && !has(l)) || !visible(l));
      // Daughters that would be listed: with "hide lects with no data" on, a group
      // whose daughters all lack data has nothing to open.
      const shownKids = id => (kids[id] || []).filter(shows);
      const shownSize = id => shownKids(id).reduce((n, k) => n + 1 + shownSize(k.id), 0);
      const walk = (pid, depth) => {
        for (const l of kids[pid] || []) {
          if (!shows(l)) continue;
          // A proto-language with daughters heads a group, named after the clade
          // (Malayo-Polynesian, not Proto-Malayo-Polynesian). An earlier stage of
          // one language (Pre-Gayo) heads none: its daughter simply follows it.
          const k = shownKids(l.id).length ? kids[l.id] : null, group = k && l.type !== "earlier-stage";
          const isOpen = !group || q ? true : open.has(l.id);
          const clade = group ? (l.clade || l.name) : "";
          // The daughter of an earlier stage (Pre-Gayo > Gayo) follows it at the same depth.
          const afterStage = LECTS[l.parent_id]?.type === "earlier-stage" && inPool.has(l.parent_id);
          shown++;
          body += `<tr class="${q && !hit(l) ? "dim" : ""}">
            <td class="nm" style="--d:${depth}" title="${esc(pathOf(l))}">${afterStage ? `<span class="twist after">↳</span>` : ""}${group
              ? `<button class="twist" data-id="${esc(l.id)}" aria-expanded="${isOpen}" aria-label="${isOpen ? "Close" : "Open"} ${esc(clade)}">${isOpen ? "▾" : "▸"}</button>${l.name === "Proto-" + clade
                ? `<a class="clade" href="#/lects/${esc(l.id)}/" title="${esc(l.name)}">${esc(clade)}</a>`
                : `<b class="clade">${esc(clade)}</b> <span class="muted">·</span> ${lectLink(l.id)}`}`
              : (afterStage ? "" : `<span class="twist"></span>`) + lectLink(l.id)}${group && !isOpen ? ` <span class="muted count">${shownSize(l.id)} lect${shownSize(l.id) === 1 ? "" : "s"}</span>` : ""}</td>${cells(l)}</tr>`;
          if (k && isOpen) walk(l.id, l.type === "earlier-stage" ? depth : depth + 1);
          // Lects that another classification puts here: listed, dimmed, with the work that proposes it.
          if (isOpen && altKids[l.id] && !q) for (const a of altKids[l.id]) {
            if (pivot && !pivot.alt.has(a.lect.id)) continue;
            body += `<tr class="dim alt"><td class="nm" style="--d:${depth + 1}"><span class="twist"></span>${lectLink(a.lect.id)}
              <span class="muted" title="In the tree this lect descends from ${esc(LECTS[a.lect.parent_id]?.name || "")}">proposed daughter (${srcLink(a.source_id)})</span></td>${cells(a.lect)}</tr>`;
          }
        }
      };
      walk("", 0);
      // In a reflex table, lects that another classification puts directly under the pivot's lect.
      if (pivot && !q) for (const a of altKids[pivot.lect] || []) {
        shown++;
        body += `<tr class="alt"><td class="nm" style="--d:0"><span class="twist"></span>${lectLink(a.lect.id)}
          <span class="muted" title="In the tree this lect descends from ${esc(LECTS[a.lect.parent_id]?.name || "")}">proposed daughter (${srcLink(a.source_id)})</span></td>${cells(a.lect)}</tr>`;
      }
    }
    const cols = tree ? 4 : 5;
    const hidden = state.hideEmpty && !pivot ? pool.filter(l => !hasData(l)).length : 0;
    app.querySelector("#count").textContent = pool.length ? `${shown} of ${pool.length} shown${hidden ? ` (${hidden} with no data hidden)` : ""}` : "";
    remember();
    app.querySelector("#t").innerHTML = head + (body || `<tr><td colspan="${cols}" class="muted">${INDEX.lects.length ? "No lects match." : "No lects entered yet. Add rows to cldf/lects.csv."}</td></tr>`);
  };
  app.querySelector("#q").value = state.q;
  app.querySelector("#hideempty").checked = state.hideEmpty;
  app.querySelector("#q").addEventListener("input", e => { state.q = e.target.value; draw(); });
  app.querySelector("#hideempty").addEventListener("change", e => { state.hideEmpty = e.target.checked; draw(); });
  app.querySelectorAll(".seg button").forEach(b => b.addEventListener("click", () => {
    state.view = b.dataset.v; try { localStorage.setItem("asc-view", state.view); } catch (e) {} draw();
  }));
  app.querySelector("#t").addEventListener("click", e => {
    const b = e.target.closest("button.twist");
    if (!b) return;
    open.has(b.dataset.id) ? open.delete(b.dataset.id) : open.add(b.dataset.id);
    draw();
  });
  app.querySelector("#openall").addEventListener("click", () => { pool.forEach(l => kids[l.id] && open.add(l.id)); draw(); });
  app.querySelector("#closeall").addEventListener("click", () => { open.clear(); (kids[""] || []).forEach(r => open.add(r.id)); draw(); });
  draw();
}
