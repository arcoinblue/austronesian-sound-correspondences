"use strict";
// The map over the lect list: a point for every attested lect with a known place; a click
// opens the lect's page. Drawn on a canvas from land.json (coastlines, Natural Earth 1:10m,
// written by tools/make_land.py) and data/map.json (the points); no map service is called.
//
// Longitudes are counted eastward from Greenwich (0 to 360), so that the Pacific is in one
// piece: Madagascar is at the left edge and Rapa Nui at the right. Mercator projection.

const MAP_Y = lat => -Math.log(Math.tan(Math.PI / 4 + lat * Math.PI / 360)) * 180 / Math.PI;
const MAP_X = lon => lon < 0 ? lon + 360 : lon;

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
  box.innerHTML = `<div class="mapwrap"><canvas role="img" aria-label="Map of the lects with a known place. The same lects are listed, with links, in the table below."></canvas>
      <div class="mapbtns"><button type="button" data-z="in" aria-label="Zoom in" title="Zoom in">+</button><button type="button" data-z="out" aria-label="Zoom out" title="Zoom out">−</button><button type="button" data-z="fit" aria-label="Show all points" title="Show all points">⤢</button></div>
      <div class="maptip" hidden></div><div class="mappop" hidden></div></div>
    <p class="muted mapnote"></p>`;
  const wrap = box.querySelector(".mapwrap"), cv = wrap.querySelector("canvas"), ctx = cv.getContext("2d");
  const tip = wrap.querySelector(".maptip"), pop = wrap.querySelector(".mappop"), note = box.querySelector(".mapnote");
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

  const sx = x => (x - view.cx) * view.k + W / 2, sy = y => (y - view.cy) * view.k + H / 2;
  const KMAX = 150;     // past this the coastline (simplified to 0.04°) is all corners
  const kmin = () => Math.min(W / 250, H / 110);
  const clamp = () => {
    view.k = Math.max(kmin(), Math.min(KMAX, view.k));
    view.cx = Math.max(25, Math.min(265, view.cx));
    view.cy = Math.max(MAP_Y(40), Math.min(MAP_Y(-55), view.cy));
    mem.view = view;
  };
  const fit = () => {
    const ps = pts.length ? pts : all;
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
    const r = view.k > 40 ? 4.5 : 3.5, seen = [];
    // Glottolog's places first, so that a lect's own coordinates are drawn over them.
    for (const pass of [true, false]) for (const p of pts) {
      if (p.g !== pass) continue;
      const x = sx(p.x), y = sy(p.y);
      if (x < -8 || y < -8 || x > W + 8 || y > H + 8) continue;
      ctx.beginPath(); ctx.arc(x, y, r, 0, 2 * Math.PI);
      ctx.fillStyle = p.g ? bg : accent; ctx.strokeStyle = p.g ? accent : bg; ctx.lineWidth = p.g ? 1.4 : 1;
      ctx.fill(); ctx.stroke();
      seen.push([x, y, p]);
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
        tip.textContent = hit.length === 1 ? hit[0].name : `${hit[0].name} and ${hit.length - 1} more`;
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
      pop.innerHTML = `<div class="muted">${hit.length} lects here</div>` + hit.map(p => `<a href="${lectHref(p.id)}">${esc(p.name)}</a>`).join("");
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
      + `<span class="mapkey own"></span> the lect's own coordinates (${own}), <span class="mapkey glot"></span> Glottolog's place for its Glottocode (${glot}). `
      + `Click a point to open the lect; where several lie together, a list opens. Drag to move; zoom with the buttons, a double click, a pinch, or Ctrl/⌘ and the wheel. Reconstructed stages have no place.`;
  };
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
