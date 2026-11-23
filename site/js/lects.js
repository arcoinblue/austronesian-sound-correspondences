"use strict";
// Page 1: the lect list (#/lects/), and the same list pivoted on a proto-phoneme (#/lects/?reflex=pmp:R).

// How each list was left (the full list, and each reflex table): open groups,
// filter, the "hide empty" box. Kept while the site is open, so coming back
// from a lect finds the list as it was; the full list's open groups are also
// kept across visits.
const LIST_STATE = {};

// The tree labels a node by its name without Proto- or Pre- (the Type column says what it
// is; the lect's own page keeps the full name, which the link's title gives).
const treeName = l => l.name.replace(/^(Proto|Pre)-(?=\S)/, "");
// A node that is not an established subgroup: a linkage. Shown in italics, after the
// established lects and subgroups beside it.
const isLinkage = l => l.type === "linkage" ? 1 : 0;
function treeLink(id) {
  const l = LECTS[id], href = lectHref(id), name = esc(l ? treeName(l) : id), full = esc(l?.name || id);
  return href ? `<a href="${href}"${name !== full ? ` title="${full}"` : ""}>${name}</a>`
    : `<span class="node" title="${full}: a node of the tree, with no page of its own">${name}</span>`;
}

async function pageIndex(params) {
  const reflex = params.get("reflex");
  let pivot = null;
  if (reflex) {
    const [pl, ps] = splitPid(reflex);
    const d = await lectData(pl);
    const ph = d.phonemes.find(p => p.ipa === ps);
    if (!ph) throw new Error(`No phoneme ${reflex}`);
    const det = await phonemeData(ph);
    // implied: retentions the build adds below the first level ({lect: [its phonemes]}).
    pivot = { lect: pl, ph, byLect: {}, alt: new Set(), implied: det.implied_descendants || {} };
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
  const state = { q: mem.q, view: "tree", hideEmpty: mem.hideEmpty, only: !!mem.only };
  try { state.view = localStorage.getItem("asc-view") === "flat" ? "flat" : "tree"; } catch (e) {}
  // The address can carry the filter, the view and the reflex table's box (?q=tetun&view=flat&only=1).
  if (params.get("q") !== null) state.q = params.get("q");
  if (params.get("view")) state.view = params.get("view") === "flat" ? "flat" : "tree";
  if (pivot && params.get("only")) state.only = params.get("only") === "1";

  // The tree: daughters under their nearest ancestor. In a reflex table the
  // pivot's own daughters are the top level.
  const pool = INDEX.lects.filter(l => !pivot || ancestorsOf(l.id).includes(pivot.lect));
  const inPool = new Set(pool.map(l => l.id));
  const kids = {};
  for (const l of pool) (kids[inPool.has(treeParent(l)) ? treeParent(l) : inPool.has(l.parent_id) ? l.parent_id : ""] ||= []).push(l);
  // Established lects and subgroups first (branches, then leaves), then the nodes that are
  // not established (linkages), each by the name shown: a group by its clade (Basap for
  // Pre-Basap, Aru for Proto-Aru), so that Pre-X groups sort among the clades.
  const shownName = l => l.clade || treeName(l);
  for (const k of Object.values(kids))
    k.sort((x, y) => isLinkage(x) - isLinkage(y) || (kids[y.id] ? 1 : 0) - (kids[x.id] ? 1 : 0)
      || shownName(x).localeCompare(shownName(y)));
  // Open to start with: the top two levels; everything in a reflex table.
  const open = mem.open ||= new Set();
  if (!open.size) {
    for (const r of kids[""] || []) { open.add(r.id); for (const k of kids[r.id] || []) open.add(k.id); }
    if (pivot) pool.forEach(l => open.add(l.id));
  }
  const remember = () => {
    mem.q = state.q; mem.hideEmpty = state.hideEmpty; mem.only = state.only;
    setQuery({ q: state.q, view: state.view === "flat" ? "flat" : "", only: pivot && state.only ? "1" : "" });
    if (!pivot) try { localStorage.setItem("asc-open", JSON.stringify([...open])); } catch (e) {}
  };
  // The clades above a lect, shown when the pointer rests on its name.
  const pathOf = l => ancestorsOf(l.id).map(a => LECTS[a]?.clade || LECTS[a]?.name || a).join(" › ");

  app.innerHTML = `
    ${pivot ? `<div class="crumb"><a href="#/lects/">All lects</a> › reflexes of ${phLink(reflex)}</div>
      <h1>Reflexes of <span class="ipa">${esc(sym(reflex))}</span> <span class="muted" style="font-size:16px">${esc(LECTS[pivot.lect].name)}</span></h1>
      <p class="muted">Each descendant lect's reflex, through every intermediate stage. Lects outside ${esc(LECTS[pivot.lect].name)} are hidden.</p>`
      : `<h1>Lects</h1><p class="muted">Every language and reconstructed stage in the database. Groups are named after the clade and headed by its proto-language; click an arrow to open or close one. Names are given without Proto- and Pre-; the Type column and each lect's page give the full name. A group name in bold with no link (a linkage, a subgroup with no proto-language entered, a language whose dialects carry the data) has no page of its own; dialects are listed under their language. Linkages and proposed daughters, which are not established subgroups, are in italics, below the established lects and subgroups beside them.</p>`}
    <div class="controls">
      <input type="search" id="q" placeholder="Filter names and alternate names" aria-label="Filter">
      <span class="seg" role="group" aria-label="View">
        <button data-v="tree">Tree</button><button data-v="flat">A–Z</button>
      </span>
      <span class="treeonly"><button class="more" id="openall">Expand all</button> <button class="more" id="closeall">Collapse</button></span>
      <label class="muted" id="hideemptybox" style="font-size:13px"><input type="checkbox" id="hideempty" checked> Hide lects with no data</label>
      ${pivot ? `<label class="muted" style="font-size:13px" title="Hide the lects, and the groups, that have no reflex of this phoneme entered or implied"><input type="checkbox" id="onlyreflex"> Only lects with a reflex</label>` : ""}
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
    // In a reflex table: has the lect, or a lect under it, a reflex of the phoneme?
    const ownReflex = l => pivot && ((pivot.byLect[l.id] || []).length || (pivot.implied[l.id] || []).length);
    const hasReflex = l => ownReflex(l) || (kids[l.id] || []).some(hasReflex);
    const visible = l => !(state.hideEmpty && !pivot && !hasData(l)) && !(pivot && state.only && !hasReflex(l));
    const head = `<tr><th>Name</th><th class="ty">Type</th><th class="gc">Glottocode</th>${tree ? "" : "<th>Nearest ancestor</th>"}
      <th>${pivot ? "Reflex" : "Coverage"}</th></tr>`;
    const cells = l => {
      let mid;
      if (pivot && l.node_only) mid = "";
      else if (pivot) {
        const rs = pivot.byLect[l.id] || [];
        const sole = soleRows(rs);
        // A stage or lect that keeps the sound unchanged without the source saying so: the
        // same implied retention its own page shows, not "unentered".
        const imp = (pivot.implied[l.id] || []).filter(c => !rs.some(r => r.child === c))
          .map(c => `${phLink(c)} <span class="tag der" title="not mentioned by a source that lists only the changes: taken as retained">implied</span>`);
        mid = rs.length || imp.length ? rs.map(r => r.child
          ? `${phLink(r.child)} ${sole.has(r) ? "" : `<span class="muted">/ ${r.fusion ? fusionLabel(r.fusion) + " fuse" : esc(r.environment)}</span> `}${badge(r.status)}${r.via.length ? ` <span class="muted">via ${r.via.map(v => esc(sym(v))).join(" → ")}</span>` : ""}${r.alt_via ? ` <span class="muted">from ${esc(LECTS[splitPid(r.parent)[0]]?.name || "")} ${esc(sym(r.parent))}</span>` : ""}`
          : `<span class="blank">no reflex</span> <span class="muted">/ ${esc(r.environment)}</span> ${badge(r.blank_type)}`).concat(imp).join("<br>")
          : `<span class="blank">unentered</span>`;
      } else mid = l.node_only ? (l.representative ? `<span class="muted">see ${lectLink(l.representative)}</span>` : "")
        : coverage(l.coverage, l.index_status) + ({ "changes-only": " " + badge("changes-only"), empty: "", generated: "" }[l.index_status] ?? "");
      return `<td class="nw ty">${typeLabel(l.type)}</td>
        <td class="gc">${l.glottocode ? `<a href="https://glottolog.org/resource/languoid/id/${esc(l.glottocode)}" target="_blank" rel="noopener">${esc(l.glottocode)}</a>` : ""}</td>
        ${tree ? "" : `<td>${l.parent_id ? lectLink(l.parent_id) : ""}</td>`}<td class="${pivot ? "" : "cov"}">${mid}</td>`;
    };
    // The count is of lects that pass the filter and the box, whether or not their group is
    // open: opening a group does not change it. A tree node with no page of its own (a
    // linkage; Tsou, which opens Duhtu) is not counted.
    const isLect = l => !l.node_only;
    const lectsAll = pool.filter(isLect).length;
    const shown = pool.filter(l => isLect(l) && (!q || hit(l)) && visible(l)).length;
    let body = "";
    if (!tree) {
      const rows = pool.filter(l => hit(l) && visible(l) && !l.node_only).sort((a, b) => a.name.localeCompare(b.name));
      body = rows.map(l => `<tr><td>${lectLink(l.id)}</td>${cells(l)}</tr>`).join("");
    } else {
      // A filter keeps the matches and the ancestors that lead to them.
      const has = l => hit(l) || (kids[l.id] || []).some(has);
      const shows = l => !((q && !has(l)) || !visible(l));
      // Daughters that would be listed: with "hide lects with no data" on, a group
      // whose daughters all lack data has nothing to open.
      const shownKids = id => (kids[id] || []).filter(shows);
      const shownSize = id => shownKids(id).reduce((n, k) => n + 1 + shownSize(k.id), 0);
      // An earlier stage with one daughter listed is a chain (Pre-Gayo, then Gayo), not a group.
      const stageChain = l => l.type === "earlier-stage" && shownKids(l.id).length <= 1;
      const walk = (pid, depth) => {
        for (const l of kids[pid] || []) {
          if (!shows(l)) continue;
          // A proto-language with daughters heads a group, named after the clade
          // (Malayo-Polynesian, not Proto-Malayo-Polynesian). An earlier stage of
          // one language (Pre-Gayo > Gayo) heads none: its daughter simply follows it.
          // An earlier stage with several daughters (Pre-Basap > four dialects) heads a
          // group under its own name.
          const k = shownKids(l.id).length ? kids[l.id] : null, group = k && !stageChain(l);
          const isOpen = !group || q ? true : open.has(l.id);
          const clade = group ? (l.clade || treeName(l)) : "";
          const afterStage = treeParent(l) === l.parent_id && LECTS[l.parent_id]?.type === "earlier-stage"
            && inPool.has(l.parent_id) && stageChain(LECTS[l.parent_id]);
          body += `<tr class="${[q && !hit(l) ? "dim" : "", isLinkage(l) ? "unest" : ""].filter(Boolean).join(" ")}">
            <td class="nm" style="--d:${depth}" title="${esc(pathOf(l))}">${afterStage ? `<span class="twist after">↳</span>` : ""}${group
              ? `<button class="twist" data-id="${esc(l.id)}" aria-expanded="${isOpen}" aria-label="${isOpen ? "Close" : "Open"} ${esc(clade)}">${isOpen ? "▾" : "▸"}</button>${treeName(l) === clade || l.name === clade
                ? (lectHref(l.id) ? `<a class="clade" href="${lectHref(l.id)}" title="${esc(l.name)}${l.representative ? ": opens " + esc(LECTS[l.representative]?.name || "") : ""}">${esc(clade)}</a>`
                  : `<b class="clade" title="${isLinkage(l) ? "a linkage, not an established subgroup: no proto-language, no page of its own" : l.type === "group" ? "a group with no proto-language entered: no page of its own" : "no page of its own: the lects under it carry the data"}">${esc(clade)}</b>`)
                : `<b class="clade">${esc(clade)}</b> <span class="muted">·</span> ${treeLink(l.id)}`}`
              : (afterStage ? "" : `<span class="twist"></span>`) + treeLink(l.id)}${group && !isOpen ? ` <span class="muted count">${shownSize(l.id)} lect${shownSize(l.id) === 1 ? "" : "s"}</span>` : ""}</td>${cells(l)}</tr>`;
          if (k && isOpen) walk(l.id, group ? depth + 1 : depth);
          // Lects that another classification puts here: listed, dimmed, with the work that proposes it.
          if (isOpen && altKids[l.id] && !q) for (const a of altKids[l.id]) {
            if (pivot && !pivot.alt.has(a.lect.id)) continue;
            body += `<tr class="dim alt unest"><td class="nm" style="--d:${depth + 1}"><span class="twist"></span>${treeLink(a.lect.id)}
              <span class="muted" title="In the tree this lect descends from ${esc(LECTS[a.lect.parent_id]?.name || "")}">proposed daughter (${srcLink(a.source_id)})</span></td>${cells(a.lect)}</tr>`;
          }
        }
      };
      walk("", 0);
      // In a reflex table, lects that another classification puts directly under the pivot's lect.
      if (pivot && !q) for (const a of altKids[pivot.lect] || []) {
        body += `<tr class="alt unest"><td class="nm" style="--d:0"><span class="twist"></span>${treeLink(a.lect.id)}
          <span class="muted" title="In the tree this lect descends from ${esc(LECTS[a.lect.parent_id]?.name || "")}">proposed daughter (${srcLink(a.source_id)})</span></td>${cells(a.lect)}</tr>`;
      }
    }
    const cols = tree ? 4 : 5;
    const empty = pivot ? 0 : pool.filter(l => !hasData(l)).length;
    const hidden = state.hideEmpty ? empty : 0;
    // The box is offered only when some lect has no data to hide (none has, when every lect
    // has rows, an inheritance or a sourced inventory), and never in a reflex table.
    app.querySelector("#hideemptybox").hidden = !empty;
    const withReflex = pivot ? pool.filter(l => (pivot.byLect[l.id] || []).length || (pivot.implied[l.id] || []).length).length : 0;
    app.querySelector("#count").textContent = !pool.length ? ""
      : pivot ? `${q ? `${shown} of ` : ""}${lectsAll} lects, ${withReflex} with a reflex`
      : `${shown === lectsAll ? "" : `${shown} of `}${lectsAll} lects${hidden ? ` (${hidden} with no data hidden)` : ""}`;
    remember();
    app.querySelector("#t").innerHTML = head + (body || `<tr><td colspan="${cols}" class="muted">${INDEX.lects.length ? "No lects match." : "No lects entered yet. Add rows to cldf/lects.csv."}</td></tr>`);
  };
  app.querySelector("#q").value = state.q;
  app.querySelector("#hideempty").checked = state.hideEmpty;
  app.querySelector("#q").addEventListener("input", e => { state.q = e.target.value; draw(); });
  app.querySelector("#hideempty").addEventListener("change", e => { state.hideEmpty = e.target.checked; draw(); });
  const only = app.querySelector("#onlyreflex");
  if (only) { only.checked = state.only; only.addEventListener("change", e => { state.only = e.target.checked; draw(); }); }
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
