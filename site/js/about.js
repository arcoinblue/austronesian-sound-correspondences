"use strict";
// What the site is, where its data comes from and how to cite it (#/about/).

function pageAbout() {
  const n = INDEX.lects.filter(l => !l.node_only).length, src = Object.keys(SOURCES).length;
  const here = location.href.split("#")[0];
  app.innerHTML = `<h1>About</h1>
    <div class="prose">
    <p><i>Austronesian Sound Correspondences</i> records how the sounds of Austronesian languages correspond to those of
      their reconstructed ancestors. For each language, dialect and proto-language it gives a phoneme inventory, and for
      each phoneme its ancestry back to Proto-Austronesian and its reflexes in the languages below it. It has
      ${n.toLocaleString("en")} lects from ${src} published works.</p>
    <h2>Where the data comes from</h2>
    <p>Every correspondence is taken from a published source and cited with its page. Where a source was read through
      another work, both are named. The site adds two things of its own and marks them: an inventory inferred from the
      correspondences when no source states one, and a phoneme taken as unchanged when a source lists only the changes.
      The classification follows the sources entered; where they disagree, the alternatives are shown as proposed groupings.</p>
    <h2>How to cite</h2>
    <p>For a single correspondence or inventory, cite the original source given beside it. For the compilation:</p>
    <p class="citation"><i>Austronesian Sound Correspondences</i>. ${new Date().getFullYear()}. <a href="${esc(here)}">${esc(here)}</a></p>
    <h2>Data and code</h2>
    <p>The tables (CSV, in CLDF layout) and the code that builds the site are in the
      <a href="https://github.com/arcoinblue/austronesian-sound-correspondences" target="_blank" rel="noopener">GitHub repository</a>.
      The files this site reads are under <a href="data/index.json">data/</a>.</p>
    <p class="muted small">Set in Charis SIL (SIL Open Font License). Map outlines from Natural Earth; places from the sources and Glottolog.</p>
    </div>`;
}
