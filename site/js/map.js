"use strict";
// The map over the lect list: a point for every attested lect with a known place; a click
// opens the lect's page. Drawn on a canvas from land.json (coastlines, Natural Earth 1:10m,
// written by tools/make_land.py) and data/map.json (the points); no map service is called.
//
// Longitudes are counted eastward from Greenwich (0 to 360), so that the Pacific is in one
// piece: Madagascar is at the left edge and Rapa Nui at the right. Mercator projection.

const MAP_Y = lat => -Math.log(Math.tan(Math.PI / 4 + lat * Math.PI / 360)) * 180 / Math.PI;
const MAP_X = lon => lon < 0 ? lon + 360 : lon;

// Colouring by subgroup. A mode colours the lects under one node by the daughter of that node
// they stand under in the tree (Taiwan: the daughters of Austronesian; then those of
// Malayo-Polynesian, and of Oceanic); the lects outside it are grey, and so is the daughter
// that has a mode of its own (Malayo-Polynesian in the first, Oceanic in the second).
// Eight hues (one set for light, one for dark surfaces) by five shapes: daughters are numbered
// in the tree's order (by geography), the hue changes from one to the next and the shape after
// every eight, so neighbours differ in hue and no two daughters share both. The numbering is
// over all the node's daughters with a point, whatever the filter shows. A daughter that is a
// single language (Thao, Chamorro, Yapese) gets no mark of its own: such languages share one,
// "etc." (the user's instruction of 27 Nov 2026).
const MAP_MODES = [["pan", "Taiwan"], ["pmp", "Malayo-Polynesian"], ["poc", "Oceanic"]];
const MAP_NESTED = { pan: "pmp", pmp: "poc" };
const MAP_HUES = { light: ["#257de0", "#f47230", "#00b894", "#f2a600", "#ee7fac", "#008a17", "#6a4ce2", "#ec4647"],
  dark: ["#338ced", "#e76624", "#00a888", "#d28e05", "#e24d8b", "#0aac23", "#9887ef", "#eb6263"] };
const MAP_ETC = "~etc";
const MAP_SHAPES = ["circle", "square", "diamond", "up", "down"];
// The outline of a shape of "radius" r about (x, y), as [x, y] corners (null: a circle).
function mapShape(kind, x, y, r) {
  if (kind === "square") { const h = r * 0.86; return [[x - h, y - h], [x + h, y - h], [x + h, y + h], [x - h, y + h]]; }
  if (kind === "diamond") { const h = r * 1.2; return [[x, y - h], [x + h, y], [x, y + h], [x - h, y]]; }
  if (kind === "up") { const h = r * 1.15; return [[x, y - h], [x + h, y + h * 0.8], [x - h, y + h * 0.8]]; }
  if (kind === "down") { const h = r * 1.15; return [[x, y + h], [x + h, y - h * 0.8], [x - h, y - h * 0.8]]; }
  return null;
}
const mapDark = () => window.matchMedia("(prefers-color-scheme: dark)").matches;

let LAND_PATH = null;
async function landPath() {
  if (LAND_PATH) return LAND_PATH;
  const land = await json("land.json");
  const p = new Path2D();
  for (const r of land.rings) {
    let x = r[0], y = r[1];
    p.moveTo(x / land.q, MAP_Y(y / land.q));
    for (let i = 2; i < r.length; i += 2) { x += r[i]; y += r[i + 1]; p.lineTo(x / land.q, MAP_Y(y / land.q)); }
    p.closePath();
  }
  return LAND_PATH = p;
}

// box: the element the map goes into. mem: an object that keeps the view while the site is
// open. Returns { show(ids, refit) }: draw the points of these lects only (a Set of lect ids,
// or null for all), and with refit move the view to hold them.
async function lectMap(box, mem) {
  const modes = MAP_MODES.filter(([id]) => LECTS[id]);
  box.innerHTML = `${modes.length ? `<div class="mapmodes"><span class="muted">Colour by subgroup</span>
      <span class="seg" role="group" aria-label="Colour by subgroup"><button type="button" data-m="">Off</button>${modes.map(([id, name]) => `<button type="button" data-m="${id}">${name}</button>`).join("")}</span></div>` : ""}
    <div class="mapwrap"><canvas role="img" aria-label="Map of the lects with a known place. The same lects are listed, with links, in the table below."></canvas>
      <div class="mapbtns"><button type="button" data-z="in" aria-label="Zoom in" title="Zoom in">+</button><button type="button" data-z="out" aria-label="Zoom out" title="Zoom out">−</button><button type="button" data-z="fit" aria-label="Show all points" title="Show all points">⤢</button></div>
      <div class="maptip" hidden></div><div class="mappop" hidden></div></div>
    <div class="maplegend" hidden></div>
    <p class="muted mapnote"></p>`;
  const wrap = box.querySelector(".mapwrap"), cv = wrap.querySelector("canvas"), ctx = cv.getContext("2d");
  const tip = wrap.querySelector(".maptip"), pop = wrap.querySelector(".mappop"), note = box.querySelector(".mapnote");
  const legend = box.querySelector(".maplegend");
  note.textContent = "Loading the map…";
  let all, land;
  try { [{ points: all }, land] = await Promise.all([json("data/map.json"), landPath()]); }
  catch (e) { note.textContent = `The map could not be loaded (${e.message}).`; return { show() {} }; }
  // A lect the index does not have (the two files are of different builds) is left out.
  all = all.filter(p => LECTS[p[0]] && lectHref(p[0]))
    .map(p => ({ id: p[0], x: MAP_X(p[2]), y: MAP_Y(p[1]), g: !!p[3], name: LECTS[p[0]].name }));
  // fresh: no view is remembered, so the first points shown decide it.
  let fresh = !mem.view;
  let pts = all, W = 0, H = 0, view = mem.view || null;   // view: { cx, cy, k } (k: pixels per degree of longitude)

  // mode: the node whose daughters are coloured ("" for none). styles: {daughter id: {i, shape}}.
  // hot: the daughter picked out in the legend (the others are drawn faint); pinned by a click.
  // etc: the daughters that are single languages; they share one mark, in the text colour.
  let mode = "", styles = {}, hot = null, pinned = null, etc = [];
  try { mode = localStorage.getItem("asc-mapcolour") || ""; } catch (e) {}
  if (!modes.some(([id]) => id === mode)) mode = "";
  const daughterOf = (id, node) => {
    const seen = new Set();
    for (let cur = id; cur && LECTS[cur] && !seen.has(cur);) {
      seen.add(cur);
      const up = treeParent(LECTS[cur]);
      if (up === node) return cur;
      cur = up;
    }
    return null;
  };
  const groupName = g => g === MAP_ETC ? "etc." : LECTS[g].clade || LECTS[g].name.replace(/^(Proto|Pre)-(?=\S)/, "");
  const setMode = m => {
    mode = m; styles = {}; hot = pinned = null;
    etc = [];
    for (const p of all) {
      const d = mode ? daughterOf(p.id, mode) : null;
      // A daughter that is itself a language or a dialect is no subgroup.
      const single = d && ["language", "dialect"].includes(LECTS[d].type);
      if (single && !etc.includes(d)) etc.push(d);
      p.grp = single ? MAP_ETC : d;
    }
    const ds = [...new Set(all.map(p => p.grp).filter(g => g && g !== MAP_ETC && g !== MAP_NESTED[mode]))]
      .sort((a, b) => (LECTS[a].o ?? 1e9) - (LECTS[b].o ?? 1e9));
    ds.forEach((g, i) => { styles[g] = { i: i % 8, shape: MAP_SHAPES[Math.floor(i / 8) % MAP_SHAPES.length] }; });
    if (etc.length) styles[MAP_ETC] = { etc: true, shape: "circle" };
    etc.sort((a, b) => (LECTS[a].o ?? 1e9) - (LECTS[b].o ?? 1e9));
    box.querySelectorAll(".mapmodes button").forEach(b => b.classList.toggle("on", b.dataset.m === mode));
  };
  const colourOf = g => styles[g].etc ? "var(--fg)" : MAP_HUES[mapDark() ? "dark" : "light"][styles[g].i];
  const swatch = (g, glot) => {
    const c = g && styles[g] ? colourOf(g) : "var(--muted)", sh = mapShape(g && styles[g] ? styles[g].shape : "circle", 7, 7, 4.2);
    // In a style, not in attributes: an attribute does not take var().
    const paint = `style="${glot ? `fill:var(--bg);stroke:${c};stroke-width:1.5` : `fill:${c}${g && styles[g] ? "" : ";fill-opacity:.55"}`}"`;
    return `<svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true">${sh ? `<polygon points="${sh.map(q => q.join(",")).join(" ")}" ${paint}/>` : `<circle cx="7" cy="7" r="4.2" ${paint}/>`}</svg>`;
  };

  const sx = x => (x - view.cx) * view.k + W / 2, sy = y => (y - view.cy) * view.k + H / 2;
  const KMAX = 150;     // past this the coastline (simplified to 0.04°) is all corners
  const kmin = () => Math.min(W / 250, H / 110);
  const clamp = () => {
    view.k = Math.max(kmin(), Math.min(KMAX, view.k));
    view.cx = Math.max(25, Math.min(265, view.cx));
    view.cy = Math.max(MAP_Y(40), Math.min(MAP_Y(-55), view.cy));
    mem.view = view;
  };
  const fit = only => {
    const ps = only && only.length ? only : pts.length ? pts : all;
    if (!ps.length) { view = { cx: 150, cy: 5, k: W / 230 }; return clamp(); }
    let x0 = Infinity, x1 = -Infinity, y0 = Infinity, y1 = -Infinity;
    for (const p of ps) { x0 = Math.min(x0, p.x); x1 = Math.max(x1, p.x); y0 = Math.min(y0, p.y); y1 = Math.max(y1, p.y); }
    const pad = 28;
    view = { cx: (x0 + x1) / 2, cy: (y0 + y1) / 2,
      k: Math.min((W - 2 * pad) / Math.max(x1 - x0, 1e-6), (H - 2 * pad) / Math.max(y1 - y0, 1e-6), 60) };
    clamp();
  };

  const css = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
  let pending = false;
  const draw = () => { if (!pending) { pending = true; requestAnimationFrame(paint); } };
  function paint() {
    pending = false;
    if (!W || !view) return;
    const dpr = window.devicePixelRatio || 1;
    const bg = css("--bg"), line = css("--line"), accent = css("--accent"), fg = css("--fg");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    ctx.setTransform(dpr * view.k, 0, 0, dpr * view.k, dpr * (W / 2 - view.cx * view.k), dpr * (H / 2 - view.cy * view.k));
    ctx.fillStyle = bg; ctx.strokeStyle = line; ctx.lineWidth = 1 / view.k; ctx.lineJoin = "round";
    ctx.fill(land); ctx.stroke(land);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const r = view.k > 40 ? 5 : 4, seen = [], muted = css("--muted"), dark = mapDark();
    // Grey points first, then the coloured; in each, Glottolog's places under the lects' own.
    const rank = p => (mode && p.grp && styles[p.grp] ? 2 : 0) + (p.g ? 0 : 1);
    for (const p of [...pts].sort((a, b) => rank(a) - rank(b))) {
      const x = sx(p.x), y = sy(p.y);
      if (x < -8 || y < -8 || x > W + 8 || y > H + 8) continue;
      const st = mode ? styles[p.grp] : null, grey = mode && !st;
      const c = st ? (st.etc ? fg : MAP_HUES[dark ? "dark" : "light"][st.i]) : grey ? muted : accent;
      const sh = mapShape(st ? st.shape : "circle", x, y, grey ? r - 1 : r);
      ctx.beginPath();
      if (sh) { sh.forEach((q, i) => i ? ctx.lineTo(q[0], q[1]) : ctx.moveTo(q[0], q[1])); ctx.closePath(); }
      else ctx.arc(x, y, grey ? r - 1 : r, 0, 2 * Math.PI);
      ctx.globalAlpha = (hot && p.grp !== hot) ? 0.15 : grey ? 0.55 : 1;
      ctx.fillStyle = p.g ? bg : c; ctx.strokeStyle = p.g ? c : bg; ctx.lineWidth = p.g ? 1.5 : 1;
      ctx.fill(); ctx.stroke();
      ctx.globalAlpha = 1;
      if (!hot || p.grp === hot) seen.push([x, y, p]);
    }
    // Names, once few enough points are in view to read them; a name that would run over
    // another is left out (its point still answers the pointer).
    if (seen.length && seen.length <= 45) {
      ctx.font = `12px ${getComputedStyle(document.body).fontFamily}`; ctx.textBaseline = "middle";
      const boxes = [];
      for (const [x, y, p] of seen) {
        const w = ctx.measureText(p.name).width, b = [x + 7, y - 8, x + 9 + w, y + 8];
        if (b[2] > W - 2 || boxes.some(o => b[0] < o[2] && o[0] < b[2] && b[1] < o[3] && o[1] < b[3])) continue;
        boxes.push(b);
        ctx.lineWidth = 3; ctx.strokeStyle = bg; ctx.strokeText(p.name, x + 8, y);
        ctx.fillStyle = fg; ctx.fillText(p.name, x + 8, y);
      }
    }
  }

  // The points under the pointer: the nearest one and those drawn on or beside it.
  const near = (mx, my, reach) => {
    let best = null, bd = reach * reach;
    for (const p of pts) { const d = (sx(p.x) - mx) ** 2 + (sy(p.y) - my) ** 2; if (d <= bd) { bd = d; best = p; } }
    if (!best) return [];
    const bx = sx(best.x), by = sy(best.y);
    return pts.filter(p => (sx(p.x) - bx) ** 2 + (sy(p.y) - by) ** 2 <= 36)
      .sort((a, b) => (a === best ? -1 : b === best ? 1 : a.name.localeCompare(b.name)));
  };
  const place = (el, x, y) => {
    el.hidden = false;
    el.style.left = Math.max(4, Math.min(W - el.offsetWidth - 4, x + 12)) + "px";
    el.style.top = Math.max(4, Math.min(H - el.offsetHeight - 4, y + 12)) + "px";
  };
  const closePop = () => { pop.hidden = true; pop.innerHTML = ""; };
  const zoomAt = (mx, my, f) => {
    const wx = view.cx + (mx - W / 2) / view.k, wy = view.cy + (my - H / 2) / view.k;
    view.k = Math.max(kmin(), Math.min(KMAX, view.k * f));
    view.cx = wx - (mx - W / 2) / view.k; view.cy = wy - (my - H / 2) / view.k;
    clamp(); closePop(); tip.hidden = true; draw();
  };
  const at = e => { const b = cv.getBoundingClientRect(); return [e.clientX - b.left, e.clientY - b.top]; };

  // Dragging moves the map; two fingers zoom it; a press released where it began is a click.
  const down = new Map();
  let moved = 0, pinch = 0;
  cv.addEventListener("pointerdown", e => {
    cv.setPointerCapture(e.pointerId);
    down.set(e.pointerId, at(e));
    if (down.size === 1) moved = 0;
    if (down.size === 2) { const [a, b] = [...down.values()]; pinch = Math.hypot(a[0] - b[0], a[1] - b[1]); moved = 99; }
  });
  cv.addEventListener("pointermove", e => {
    const [mx, my] = at(e);
    if (!down.has(e.pointerId)) {
      const hit = near(mx, my, 8);
      cv.style.cursor = hit.length ? "pointer" : "grab";
      if (hit.length && pop.hidden) {
        const grp = mode && hit[0].grp ? ` · ${groupName(hit[0].grp)}` : "";
        tip.textContent = hit.length === 1 ? hit[0].name + grp : `${hit[0].name} and ${hit.length - 1} more${hit.every(p => p.grp === hit[0].grp) ? grp : ""}`;
        place(tip, mx, my);
      } else tip.hidden = true;
      return;
    }
    const was = down.get(e.pointerId);
    down.set(e.pointerId, [mx, my]);
    if (down.size === 2) {
      const [a, b] = [...down.values()], d = Math.hypot(a[0] - b[0], a[1] - b[1]);
      if (pinch) zoomAt((a[0] + b[0]) / 2, (a[1] + b[1]) / 2, d / pinch);
      pinch = d;
      return;
    }
    moved += Math.abs(mx - was[0]) + Math.abs(my - was[1]);
    if (moved < 5) return;
    cv.style.cursor = "grabbing"; tip.hidden = true; closePop();
    view.cx -= (mx - was[0]) / view.k; view.cy -= (my - was[1]) / view.k;
    clamp(); draw();
  });
  const up = e => {
    if (!down.has(e.pointerId)) return;
    down.delete(e.pointerId); pinch = 0;
    if (e.type !== "pointerup" || down.size || moved >= 5) return;
    const [mx, my] = at(e), hit = near(mx, my, e.pointerType === "touch" ? 16 : 8);
    closePop();
    if (hit.length === 1) location.hash = lectHref(hit[0].id);
    else if (hit.length) {
      // Several lects at one place (the dialects of a language placed by its Glottocode,
      // neighbouring villages): a list to choose from.
      tip.hidden = true;
      pop.innerHTML = `<div class="muted">${hit.length} lects here</div>` + hit.map(p => `<a href="${lectHref(p.id)}">${mode ? swatch(p.grp, p.g) + " " : ""}${esc(p.name)}</a>`).join("");
      place(pop, mx, my);
    }
  };
  cv.addEventListener("pointerup", up);
  cv.addEventListener("pointercancel", up);
  cv.addEventListener("pointerleave", () => { tip.hidden = true; });
  cv.addEventListener("dblclick", e => { const [mx, my] = at(e); if (!near(mx, my, 8).length) zoomAt(mx, my, 2); });
  // The wheel zooms only with Ctrl or ⌘ held (a trackpad pinch arrives so): the map stands
  // over a long list, and a bare wheel must go on scrolling the page.
  cv.addEventListener("wheel", e => {
    if (!e.ctrlKey && !e.metaKey) return;
    e.preventDefault();
    zoomAt(...at(e), Math.exp(-e.deltaY * (e.deltaMode ? 0.05 : 0.01)));
  }, { passive: false });
  wrap.querySelector(".mapbtns").addEventListener("click", e => {
    const z = e.target.closest("button")?.dataset.z;
    if (!z) return;
    if (z === "fit") { fit(); closePop(); draw(); } else zoomAt(W / 2, H / 2, z === "in" ? 1.6 : 1 / 1.6);
  });
  document.addEventListener("keydown", e => { if (e.key === "Escape") closePop(); });

  const size = () => {
    if (!cv.isConnected) return ro.disconnect();
    const w = wrap.clientWidth, h = wrap.clientHeight, dpr = window.devicePixelRatio || 1;
    if (!w || !h || (w === W && h === H)) return;
    W = w; H = h; cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    if (!view) fit(); else clamp();
    paint();
  };
  const ro = new ResizeObserver(size);
  ro.observe(wrap);
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener?.("change", draw);
  const caption = () => {
    const own = pts.filter(p => !p.g).length, glot = pts.length - own;
    note.innerHTML = `${pts.length} lect${pts.length === 1 ? "" : "s"} with a known place${pts.length < all.length ? ` (of ${all.length})` : ""}: `
      + (mode ? `a filled mark is at the lect's own coordinates (${own}), an outlined one at Glottolog's place for its Glottocode (${glot}). `
        : `<span class="mapkey own"></span> the lect's own coordinates (${own}), <span class="mapkey glot"></span> Glottolog's place for its Glottocode (${glot}). `)
      + `Click a point to open the lect; where several lie together, a list opens. Drag to move; zoom with the buttons, a double click, a pinch, or Ctrl/⌘ and the wheel. Reconstructed stages have no place.`;
    // The legend: every daughter of the node with a point, in the tree's order, with the
    // number of its lects now shown; then the grey ones.
    legend.hidden = !mode;
    if (!mode) { legend.innerHTML = ""; return; }
    const n = {};
    for (const p of pts) n[p.grp || ""] = (n[p.grp || ""] || 0) + 1;
    const nested = MAP_NESTED[mode], outside = n[""] || 0;
    legend.innerHTML = `<span class="muted">${esc(LECTS[mode].clade || groupName(mode))}:</span> `
      + Object.keys(styles).map(g => `<button type="button" class="mapleg${pinned === g ? " on" : ""}${n[g] ? "" : " none"}" data-g="${esc(g)}" aria-pressed="${pinned === g}" title="${g === MAP_ETC ? "Single languages, not subgroups: " + esc(etc.map(d => LECTS[d].name).join(", ")) : "Show only " + esc(groupName(g)) + " in colour"}">${swatch(g)} ${esc(groupName(g))} <span class="muted">${n[g] || 0}</span></button>`).join("")
      + (nested && n[nested] ? `<span class="mapleg plain">${swatch(null)} ${esc(groupName(nested))} <span class="muted">${n[nested]}</span></span>` : "")
      + (outside ? `<span class="mapleg plain">${swatch(null)} outside ${esc(LECTS[mode].clade || groupName(mode))} <span class="muted">${outside}</span></span>` : "");
  };
  legend.addEventListener("pointerover", e => { const g = e.target.closest("button.mapleg")?.dataset.g; if (g && hot !== g) { hot = g; draw(); } });
  legend.addEventListener("pointerleave", () => { if (hot !== pinned) { hot = pinned; draw(); } });
  legend.addEventListener("click", e => {
    const g = e.target.closest("button.mapleg")?.dataset.g;
    if (!g) return;
    pinned = hot = pinned === g ? null : g;
    caption(); draw();
  });
  box.querySelector(".mapmodes")?.addEventListener("click", e => {
    const b = e.target.closest("button");
    if (!b || b.dataset.m === mode) return;
    setMode(b.dataset.m);
    try { localStorage.setItem("asc-mapcolour", mode); } catch (err) {}
    closePop(); tip.hidden = true; caption();
    // The view moves to the lects now in colour (Taiwan is a speck on the whole map).
    const col = pts.filter(p => styles[p.grp]);
    if (W && mode && col.length) fit(col);
    draw();
  });
  setMode(mode);
  caption(); size();
  return {
    show(ids, refit) {
      pts = ids ? all.filter(p => ids.has(p.id)) : all;
      closePop(); tip.hidden = true; caption();
      if ((refit || fresh) && W) fit();
      fresh = false;
      draw();
    },
  };
}
