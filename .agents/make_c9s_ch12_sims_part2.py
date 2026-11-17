#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 9 Science Chapter 12 Simulators (Part 2: Slides 9-16)
High-fidelity responsive SVG interactive laboratory widgets for Patterns in Life: Diversity and Classification.
"""

sims_part2 = {
    9: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Plant Evolution:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S9('thallo')" id="c12s9_btn_tha" class="px-2 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition">1. Thallophyta (Algae)</button>
        <button onclick="setC12S9('bryo')" id="c12s9_btn_bry" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">2. Bryophyta (Amphibians)</button>
        <button onclick="setC12S9('pteri')" id="c12s9_btn_pte" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">3. Pteridophyta (Ferns)</button>
        <button onclick="setC12S9('lichen')" id="c12s9_btn_lic" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Lichen Bioindicator</button>
      </div>
    </div>
    <span class="text-xs text-emerald-300 font-mono" id="c12s9_status">Undifferentiated Thallus &bull; Aquatic</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c12s9_visual" class="w-full max-w-lg flex flex-col items-center justify-center">
      <!-- SVG Plant Structure -->
    </div>

    <div class="w-full max-w-lg mt-2 bg-slate-900/80 border border-slate-700/60 rounded-xl p-2.5">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-bold text-emerald-300" id="c12s9_title">Division Thallophyta (Algae)</span>
        <span class="text-[10px] text-slate-400 font-mono" id="c12s9_badge">No Vascular Tissues</span>
      </div>
      <p class="text-xs text-slate-300 leading-relaxed" id="c12s9_body">
        Algae possess an undifferentiated plant body called a thallus, lacking true roots, stems, or leaves. Predominantly aquatic organisms like Spirogyra with ribbon-like spiral chloroplasts and Ulothrix.
      </p>
    </div>
  </div>

  <div class="bg-emerald-950/30 border border-emerald-800/40 rounded-xl px-3 py-1.5 text-xs text-emerald-200" id="c12s9_foot">
    <strong>Evolutionary Trend:</strong> Transitioning from aquatic thallus to land-adapted vascular systems with xylem and phloem.
  </div>
</div>
<script>
window.setC12S9 = function(div){
  const btns = ['tha', 'bry', 'pte', 'lic'];
  btns.forEach(b => {
    const el = document.getElementById('c12s9_btn_' + b);
    if(el) el.className = (b === div.substring(0,3)) ?
      'px-2 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition' :
      'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  });

  const status = document.getElementById('c12s9_status');
  const vis = document.getElementById('c12s9_visual');
  const title = document.getElementById('c12s9_title');
  const badge = document.getElementById('c12s9_badge');
  const body = document.getElementById('c12s9_body');
  const foot = document.getElementById('c12s9_foot');

  if(div === 'thallo'){
    status.textContent = "Undifferentiated Thallus • Aquatic Algae";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Spirogyra Filament -->
        <rect x="50" y="35" width="280" height="60" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
        <line x1="140" y1="35" x2="140" y2="95" stroke="#10b981" stroke-width="2"/>
        <line x1="230" y1="35" x2="230" y2="95" stroke="#10b981" stroke-width="2"/>
        <!-- Spiral chloroplast ribbon -->
        <path d="M50,45 Q70,85 90,45 T130,45 M140,45 Q160,85 180,45 T220,45 M230,45 Q250,85 270,45 T310,45" fill="none" stroke="#4ade80" stroke-width="4"/>
        <!-- Pyrenoid protein granules -->
        <circle cx="80" cy="65" r="3" fill="#facc15"/>
        <circle cx="170" cy="65" r="3" fill="#facc15"/>
        <circle cx="260" cy="65" r="3" fill="#facc15"/>
        <!-- Cell labels -->
        <text x="60" y="25" fill="#a7f3d0" font-size="9" font-weight="bold">Cell 1</text>
        <text x="150" y="25" fill="#a7f3d0" font-size="9" font-weight="bold">Cell 2 (Pyrenoids)</text>
        <text x="240" y="25" fill="#a7f3d0" font-size="9" font-weight="bold">Cell 3 (Spiral Chloroplast)</text>
        <text x="100" y="115" fill="#cbd5e1" font-size="8">Spirogyra (Green Filamentous Alga)</text>
      </svg>
    `;
    title.textContent = "Division Thallophyta: Spirogyra & Algae";
    badge.textContent = "Aquatic &amp; Non-Vascular";
    body.textContent = "Thallophytes show no differentiation into root, stem, or leaves. Cell wall is composed of cellulose. Spirogyra cells possess distinctive ribbon-shaped spiral chloroplasts with starch-storing pyrenoids.";
    foot.innerHTML = "<strong>Global Significance:</strong> Marine and freshwater algae perform over 50% of the planetary photosynthetic carbon fixation!";
  } else if(div === 'bryo'){
    status.textContent = "Amphibians of Plant Kingdom • Water for Fertilisation";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Substrate soil -->
        <rect x="40" y="100" width="300" height="25" fill="#451a03"/>
        <!-- Funaria moss clump -->
        <!-- Rhizoids -->
        <path d="M120,100 L115,115 M125,100 L128,118 M190,100 L185,115 M195,100 L200,118" stroke="#a16207" stroke-width="1.5"/>
        <!-- Gametophyte leafy axis -->
        <path d="M120,100 L120,65 M115,80 L105,75 M125,85 L135,80 M115,70 L108,62 M125,72 L132,65" stroke="#15803d" stroke-width="2.5"/>
        <text x="60" y="75" fill="#86efac" font-size="8" font-weight="bold">Gametophyte (n)</text>
        <!-- Sporophyte stalk (Seta) & Capsule -->
        <path d="M120,65 Q122,35 130,20" stroke="#ca8a04" stroke-width="2" fill="none"/>
        <ellipse cx="132" cy="18" rx="6" ry="4" fill="#854d0e"/>
        <text x="145" y="22" fill="#fde047" font-size="8" font-weight="bold">Sporophyte (2n Capsule)</text>
        <!-- Marchantia thallus -->
        <path d="M210,100 Q240,80 270,100 Q260,95 240,90 Z" fill="#166534" stroke="#22c55e" stroke-width="1.5"/>
        <circle cx="235" cy="94" r="3" fill="#15803d"/>
        <text x="245" y="85" fill="#a7f3d0" font-size="8">Marchantia (Liverwort)</text>
        <text x="160" y="115" fill="#cbd5e1" font-size="8">Rhizoids anchor into soil</text>
      </svg>
    `;
    title.textContent = "Division Bryophyta: Mosses & Liverworts";
    badge.textContent = "Amphibious Flora";
    body.textContent = "Bryophytes live on moist soil but rely strictly on an external film of water for flagellated male gametes (antherozoids) to swim to the female organ (archegonium). Body has stem-like and leaf-like structures anchored by rhizoids.";
    foot.innerHTML = "<strong>Ecological Role:</strong> Mosses like Sphagnum retain huge volumes of water, forming peat bogs and preventing soil erosion.";
  } else if(div === 'pteri'){
    status.textContent = "First Vascular Land Plants • Xylem & Phloem";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Underground Rhizome & True roots -->
        <rect x="40" y="105" width="300" height="20" fill="#292524"/>
        <path d="M100,105 Q140,112 180,105" stroke="#78350f" stroke-width="4" fill="none"/>
        <path d="M120,110 L115,122 M140,110 L142,124 M160,110 L165,122" stroke="#a8a29e" stroke-width="1.5"/>
        <text x="45" y="120" fill="#a8a29e" font-size="7">True Roots</text>
        <!-- Circinate Vernation (Coiled fiddlehead) -->
        <path d="M120,105 Q125,75 118,60 Q112,50 120,45 Q126,50 120,55" fill="none" stroke="#22c55e" stroke-width="2"/>
        <text x="70" y="50" fill="#86efac" font-size="7">Fiddlehead (Coiled)</text>
        <!-- Mature Fern Frond (Pinnate leaf) -->
        <path d="M160,105 Q175,60 210,25" stroke="#15803d" stroke-width="2.5" fill="none"/>
        <!-- Pinnae leaflets -->
        <path d="M175,80 L195,75 M170,80 L150,78 M185,60 L205,52 M180,60 L160,56 M195,42 L215,36 M190,42 L175,38" stroke="#16a34a" stroke-width="2"/>
        <text x="220" y="30" fill="#4ade80" font-size="8" font-weight="bold">Fern Frond (Xylem/Phloem)</text>
        <!-- Spores in sori under fronds -->
        <circle cx="190" cy="74" r="2" fill="#ca8a04"/>
        <circle cx="200" cy="51" r="2" fill="#ca8a04"/>
        <text x="210" y="65" fill="#fde047" font-size="7">Sori (Spore Clusters)</text>
      </svg>
    `;
    title.textContent = "Division Pteridophyta: Ferns & Marsilea";
    badge.textContent = "Seedless Vascular Plants";
    body.textContent = "Pteridophytes are the first terrestrial plants possessing specialized vascular tissues—xylem for conducting water and minerals, and phloem for translocating sugars. Leaves bear microscopic sporangia clustered in sori.";
    foot.innerHTML = "<strong>Fossil Wealth:</strong> Giant carboniferous pteridophyte tree-ferns that lived 300 million years ago formed today's primary coal deposits!";
  } else {
    status.textContent = "Mutualism: Alga + Fungus • SO₂ Bioindicator";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Tree bark / Rock surface -->
        <rect x="40" y="25" width="120" height="85" rx="6" fill="#44403c" stroke="#78716c" stroke-width="2"/>
        <text x="50" y="45" fill="#d6d3d1" font-size="8" font-weight="bold">Rock / Tree Bark</text>
        <!-- Foliose / Crustose Lichen Patch -->
        <path d="M60,60 Q80,48 100,55 Q130,50 140,70 Q135,95 105,90 Q75,100 60,80 Z" fill="#a3e635" fill-opacity="0.7" stroke="#65a30d" stroke-width="2"/>
        <text x="70" y="75" fill="#365314" font-size="8" font-weight="extrabold">Patthar ke Phool</text>

        <!-- Symbiotic Cross Section -->
        <rect x="180" y="25" width="165" height="85" rx="8" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
        <text x="190" y="42" fill="#38bdf8" font-size="8" font-weight="bold">Lichen Anatomy (Mutualism)</text>
        <!-- Fungal upper cortex -->
        <line x1="190" y1="50" x2="330" y2="50" stroke="#fda4af" stroke-width="3"/>
        <text x="190" y="60" fill="#fda4af" font-size="7">Mycobiont (Fungus: Shelter/Water)</text>
        <!-- Algal layer -->
        <circle cx="210" cy="72" r="4" fill="#22c55e"/>
        <circle cx="230" cy="70" r="4" fill="#22c55e"/>
        <circle cx="250" cy="73" r="4" fill="#22c55e"/>
        <circle cx="270" cy="71" r="4" fill="#22c55e"/>
        <text x="190" y="87" fill="#86efac" font-size="7">Phycobiont (Alga: Photosynthesis)</text>
        <!-- Fungal lower cortex -->
        <line x1="190" y1="95" x2="330" y2="95" stroke="#fda4af" stroke-width="3"/>
      </svg>
    `;
    title.textContent = "Lichens & Indian Spice: Patthar ke Phool";
    badge.textContent = "Symbiotic Mutualism";
    body.textContent = "A lichen is an obligate mutualistic association between an alga/cyanobacterium (phycobiont) providing food via photosynthesis and a fungus (mycobiont) providing moisture, anchorage, and protection. Known in Indian cuisine as 'patthar ke phool'.";
    foot.innerHTML = "<strong>Pollution Warning:</strong> Lichens are highly vulnerable to sulphur dioxide (SO₂) pollution and vanish completely from contaminated urban skies!";
  }
};
window.addEventListener('DOMContentLoaded', () => setC12S9('thallo'));
</script>""",

    10: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Seed Plants:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S10('gymno')" id="c12s10_btn_gym" class="px-2 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">Gymnosperms (Cones)</button>
        <button onclick="setC12S10('angio')" id="c12s10_btn_ang" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Angiosperms (Flowers)</button>
        <button onclick="setC12S10('monodicot')" id="c12s10_btn_mnd" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Monocot vs Dicot</button>
        <button onclick="setC12S10('hortus')" id="c12s10_btn_hor" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Hortus Malabaricus</button>
      </div>
    </div>
    <span class="text-xs text-amber-300 font-mono" id="c12s10_status">Naked Seeds &bull; Cones</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c12s10_visual" class="w-full max-w-lg flex flex-col items-center justify-center">
      <!-- Dynamic SVG Illustration -->
    </div>

    <div class="w-full max-w-lg mt-2 bg-slate-900/80 border border-slate-700/60 rounded-xl p-2.5">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-bold text-amber-300" id="c12s10_title">Gymnosperms: Naked-Seeded Plants</span>
        <span class="text-[10px] text-slate-400 font-mono" id="c12s10_badge">Pinus &amp; Cycas</span>
      </div>
      <p class="text-xs text-slate-300 leading-relaxed" id="c12s10_body">
        In gymnosperms (gymnos = naked, sperma = seed), ovules are not enclosed inside an ovary wall. They remain exposed on the surface of megasporophylls, typically organized into woody female cones.
      </p>
    </div>
  </div>

  <div class="bg-amber-950/30 border border-amber-800/40 rounded-xl px-3 py-1.5 text-xs text-amber-200" id="c12s10_foot">
    <strong>Reproductive Breakthrough:</strong> Evolution of pollen tubes (siphonogamy) enabled seed plants to reproduce completely independent of swimming water!
  </div>
</div>
<script>
window.setC12S10 = function(tab){
  const btns = ['gym', 'ang', 'mnd', 'hor'];
  btns.forEach(b => {
    const el = document.getElementById('c12s10_btn_' + b);
    if(el) el.className = (b === tab.substring(0,3)) ?
      'px-2 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition' :
      'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  });

  const status = document.getElementById('c12s10_status');
  const vis = document.getElementById('c12s10_visual');
  const title = document.getElementById('c12s10_title');
  const badge = document.getElementById('c12s10_badge');
  const body = document.getElementById('c12s10_body');
  const foot = document.getElementById('c12s10_foot');

  if(tab === 'gymno'){
    status.textContent = "Naked Seeds • Woody Cones";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Pine Branch with Needle leaves -->
        <path d="M50,90 Q120,65 210,75" stroke="#78350f" stroke-width="4" fill="none"/>
        <!-- Needle fascicles -->
        <line x1="80" y1="80" x2="70" y2="40" stroke="#15803d" stroke-width="1.5"/>
        <line x1="80" y1="80" x2="85" y2="35" stroke="#15803d" stroke-width="1.5"/>
        <line x1="80" y1="80" x2="95" y2="42" stroke="#15803d" stroke-width="1.5"/>
        <line x1="140" y1="72" x2="135" y2="30" stroke="#15803d" stroke-width="1.5"/>
        <line x1="140" y1="72" x2="150" y2="28" stroke="#15803d" stroke-width="1.5"/>
        <!-- Female Pine Cone -->
        <ellipse cx="230" cy="70" rx="20" ry="32" fill="#582f0e" stroke="#854d0e" stroke-width="2"/>
        <path d="M215,55 Q230,50 245,55 M212,68 Q230,62 248,68 M215,82 Q230,76 245,82" stroke="#a16207" stroke-width="2" fill="none"/>
        <text x="210" y="115" fill="#fde047" font-size="8" font-weight="bold">Woody Seed Cone</text>
        <!-- Naked winged seed -->
        <ellipse cx="320" cy="65" rx="6" ry="10" fill="#78350f"/>
        <path d="M320,55 Q345,40 355,55 Q345,75 320,75 Z" fill="#fde68a" fill-opacity="0.7" stroke="#ca8a04"/>
        <text x="305" y="95" fill="#fde68a" font-size="8">Winged Seed (Naked)</text>
      </svg>
    `;
    title.textContent = "Gymnosperms: Pinus, Deodar & Cycas";
    badge.textContent = "Conifers &amp; Cycads";
    body.textContent = "Gymnosperms are perennial evergreen woody trees. They possess needle-like leaves with thick cuticles and sunken stomata to conserve water in cold montane climates. Seeds are not enclosed in fruits.";
    foot.innerHTML = "<strong>Xerophytic Mastery:</strong> Sunken stomata and resin ducts protect Himalayan deodars and pines from severe freezing and dehydration.";
  } else if(tab === 'angio'){
    status.textContent = "Enclosed Seeds • Flowers & Fruits";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Flower Cut Section -->
        <rect x="186" y="80" width="8" height="45" fill="#15803d"/>
        <!-- Receptacle -->
        <ellipse cx="190" cy="80" rx="18" ry="6" fill="#166534"/>
        <!-- Petals -->
        <path d="M172,80 Q140,50 160,25 Q180,45 185,75 Z" fill="#f43f5e" fill-opacity="0.8"/>
        <path d="M208,80 Q240,50 220,25 Q200,45 195,75 Z" fill="#f43f5e" fill-opacity="0.8"/>
        <!-- Carpel / Pistil (Ovary enclosing Ovules) -->
        <ellipse cx="190" cy="70" rx="14" ry="16" fill="#15803d" stroke="#86efac" stroke-width="1.5"/>
        <line x1="190" y1="54" x2="190" y2="28" stroke="#86efac" stroke-width="2"/>
        <ellipse cx="190" cy="26" rx="6" ry="3" fill="#fbbf24"/>
        <!-- Enclosed Ovules -->
        <circle cx="186" cy="68" r="3" fill="#fef08a"/>
        <circle cx="194" cy="68" r="3" fill="#fef08a"/>
        <text x="215" y="72" fill="#86efac" font-size="8" font-weight="bold">Ovary &rarr; Fruit</text>
        <text x="215" y="84" fill="#fef08a" font-size="7">Ovule &rarr; Enclosed Seed</text>
        <!-- Stamens -->
        <path d="M182,75 Q160,50 165,35" stroke="#fbbf24" stroke-width="1.5" fill="none"/>
        <circle cx="165" cy="35" r="3" fill="#eab308"/>
        <path d="M198,75 Q220,50 215,35" stroke="#fbbf24" stroke-width="1.5" fill="none"/>
        <circle cx="215" cy="35" r="3" fill="#eab308"/>
      </svg>
    `;
    title.textContent = "Angiosperms: Flowering Plants";
    badge.textContent = "Ovary Encloses Ovules";
    body.textContent = "Angiosperms (angeion = vessel, sperma = seed) are the most diverse land plants. Seeds develop within an ovary, which ripens into a fruit following fertilisation. Possess vessels in xylem and companion cells in phloem.";
    foot.innerHTML = "<strong>Dominant Flora:</strong> Over 85% of all living plant species are angiosperms, powering terrestrial animal food webs.";
  } else if(tab === 'monodicot'){
    status.textContent = "Monocots vs Dicots • Venation & Cotyledons";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Monocot Panel -->
        <rect x="30" y="15" width="150" height="100" rx="8" fill="#042f2e" stroke="#0d9488" stroke-width="1.5"/>
        <text x="40" y="32" fill="#2dd4bf" font-size="9" font-weight="bold">MONOCOTS (e.g. Grass, Maize)</text>
        <!-- Parallel venation leaf -->
        <path d="M50,95 Q55,50 70,40 Q85,50 90,95 Z" fill="#065f46" stroke="#34d399"/>
        <line x1="60" y1="95" x2="68" y2="42" stroke="#a7f3d0" stroke-width="1"/>
        <line x1="70" y1="95" x2="70" y2="40" stroke="#a7f3d0" stroke-width="1"/>
        <line x1="80" y1="95" x2="72" y2="42" stroke="#a7f3d0" stroke-width="1"/>
        <text x="100" y="60" fill="#99f6e4" font-size="7">• 1 Cotyledon</text>
        <text x="100" y="73" fill="#99f6e4" font-size="7">• Parallel Venation</text>
        <text x="100" y="86" fill="#99f6e4" font-size="7">• Fibrous Roots</text>

        <!-- Dicot Panel -->
        <rect x="200" y="15" width="150" height="100" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
        <text x="210" y="32" fill="#a5b4fc" font-size="9" font-weight="bold">DICOTS (e.g. Pea, Mango)</text>
        <!-- Reticulate venation leaf -->
        <path d="M220,95 Q210,65 240,45 Q270,65 260,95 Z" fill="#1e3a8a" stroke="#60a5fa"/>
        <line x1="240" y1="95" x2="240" y2="45" stroke="#bfdbfe" stroke-width="1.5"/>
        <line x1="240" y1="80" x2="225" y2="70" stroke="#bfdbfe" stroke-width="1"/>
        <line x1="240" y1="70" x2="255" y2="60" stroke="#bfdbfe" stroke-width="1"/>
        <text x="270" y="60" fill="#c7d2fe" font-size="7">• 2 Cotyledons</text>
        <text x="270" y="73" fill="#c7d2fe" font-size="7">• Reticulate Network</text>
        <text x="270" y="86" fill="#c7d2fe" font-size="7">• Taproot System</text>
      </svg>
    `;
    title.textContent = "Monocotyledons vs Dicotyledons";
    badge.textContent = "Embryo &amp; Leaf Venation";
    body.textContent = "Angiosperms are bifurcated into Monocots (single seed-leaf, parallel-veined leaves, trimerous floral parts) and Dicots (two seed-leaves, intricate net-like reticulate venation, tetramerous/pentamerous floral whorls, and sturdy taproots).";
    foot.innerHTML = "<strong>Field Identification:</strong> You can accurately classify a flowering plant as monocot or dicot simply by observing its leaf venation without digging up roots!";
  } else {
    status.textContent = "12 Volumes (1678-1693) • Kerala Ethnobotany";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Antique Book / Manuscript -->
        <rect x="70" y="25" width="240" height="85" rx="6" fill="#292524" stroke="#d97706" stroke-width="2"/>
        <rect x="75" y="30" width="110" height="75" fill="#fef3c7" stroke="#b45309"/>
        <rect x="195" y="30" width="110" height="75" fill="#fef3c7" stroke="#b45309"/>
        <!-- Botanical sketch in book -->
        <path d="M130,95 Q125,65 140,45" stroke="#15803d" stroke-width="2" fill="none"/>
        <ellipse cx="140" cy="45" rx="6" ry="3" fill="#16a34a"/>
        <text x="85" y="50" fill="#78350f" font-size="8" font-weight="bold">Hortus</text>
        <text x="85" y="62" fill="#78350f" font-size="8" font-weight="bold">Malabaricus</text>
        <text x="85" y="85" fill="#92400e" font-size="7">Malayalam / Latin</text>

        <!-- Right page: Details -->
        <text x="205" y="48" fill="#78350f" font-size="8" font-weight="bold">Collaborative Science:</text>
        <text x="205" y="62" fill="#451a03" font-size="7">• Hendrik van Rheede</text>
        <text x="205" y="74" fill="#451a03" font-size="7">• Itty Achudan (Physician)</text>
        <text x="205" y="86" fill="#451a03" font-size="7">• 742 Malabar Plants</text>
      </svg>
    `;
    title.textContent = "Hortus Malabaricus: Landmark of Indian Botany";
    badge.textContent = "Itty Achudan &amp; Van Rheede";
    body.textContent = "A monumental 12-volume Latin botanical treatise published between 1678 and 1693 in Amsterdam. Compiled with extensive ethnobotanical guidance from legendary traditional Ezhava Vaidyan Itty Achudan, it documented 742 medicinal plants of Kerala.";
    foot.innerHTML = "<strong>Linnaean Reliance:</strong> Carolus Linnaeus himself based hundreds of Indian plant descriptions directly on the Hortus Malabaricus!";
  }
};
window.addEventListener('DOMContentLoaded', () => setC12S10('gymno'));
</script>""",

    11: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-sky-400 uppercase tracking-wider">Lower Invertebrates:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S11('porifera')" id="c12s11_btn_por" class="px-2 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition">Porifera (Sponges)</button>
        <button onclick="setC12S11('cnidaria')" id="c12s11_btn_cni" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Cnidaria (Hydra)</button>
        <button onclick="setC12S11('platy')" id="c12s11_btn_pla" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Platyhelminthes</button>
        <button onclick="setC12S11('nema')" id="c12s11_btn_nem" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Nematoda</button>
      </div>
    </div>
    <span class="text-xs text-sky-300 font-mono" id="c12s11_status">Cellular Level &bull; 24,000 L/Day Filtration</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c12s11_visual" class="w-full max-w-lg flex flex-col items-center justify-center">
      <!-- Dynamic SVG Anatomical Model -->
    </div>

    <div class="w-full max-w-lg mt-2 bg-slate-900/80 border border-slate-700/60 rounded-xl p-2.5">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-bold text-sky-300" id="c12s11_title">Phylum Porifera: Sponges</span>
        <span class="text-[10px] text-slate-400 font-mono" id="c12s11_badge">Pore-Bearing Non-Motile</span>
      </div>
      <p class="text-xs text-slate-300 leading-relaxed" id="c12s11_body">
        Poriferans are non-motile multicellular animals with cellular-grade body organization. Bodies are perforated with thousands of microscopic pores (ostia) leading to a central cavity (spongocoel) and exiting through the osculum.
      </p>
    </div>
  </div>

  <div class="bg-sky-950/30 border border-sky-800/40 rounded-xl px-3 py-1.5 text-xs text-sky-200" id="c12s11_foot">
    <strong>Sponge Power:</strong> A single 1-meter marine sponge can filter over 24,000 liters of seawater per day, purifying coastal ecosystems!
  </div>
</div>
<script>
window.setC12S11 = function(phylum){
  const btns = ['por', 'cni', 'pla', 'nem'];
  btns.forEach(b => {
    const el = document.getElementById('c12s11_btn_' + b);
    if(el) el.className = (b === phylum.substring(0,3)) ?
      'px-2 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition' :
      'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  });

  const status = document.getElementById('c12s11_status');
  const vis = document.getElementById('c12s11_visual');
  const title = document.getElementById('c12s11_title');
  const badge = document.getElementById('c12s11_badge');
  const body = document.getElementById('c12s11_body');
  const foot = document.getElementById('c12s11_foot');

  if(phylum === 'porifera'){
    status.textContent = "Cellular Level • 24,000 L/Day Filtration";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Vase-shaped Sycon sponge -->
        <path d="M150,115 C130,85 140,35 160,25 L220,25 C240,35 250,85 230,115 Z" fill="#0369a1" fill-opacity="0.4" stroke="#38bdf8" stroke-width="2"/>
        <!-- Central cavity (Spongocoel) -->
        <path d="M175,115 C165,85 170,40 180,25 L200,25 C210,40 215,85 205,115 Z" fill="#082f49"/>
        <!-- Osculum top opening -->
        <ellipse cx="190" cy="25" rx="15" ry="5" fill="#38bdf8"/>
        <path d="M190,20 L190,5" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
        <text x="210" y="15" fill="#7dd3fc" font-size="8">Osculum (Water Outflow)</text>
        <!-- Ostia pores on lateral walls with arrows -->
        <circle cx="145" cy="65" r="2" fill="#facc15"/>
        <circle cx="142" cy="85" r="2" fill="#facc15"/>
        <circle cx="235" cy="65" r="2" fill="#facc15"/>
        <circle cx="238" cy="85" r="2" fill="#facc15"/>
        <text x="65" y="70" fill="#fde047" font-size="8">Ostia Pores (Inflow) &rarr;</text>
        <text x="145" y="125" fill="#94a3b8" font-size="8">Substrate Anchorage</text>
      </svg>
    `;
    title.textContent = "Phylum Porifera: Sycon & Spongilla";
    badge.textContent = "Cellular Organization";
    body.textContent = "Poriferans feature specialized flagellated collar cells (choanocytes) lining the inner spongocoel. Rapid flagellar beating generates an internal water current drawing in microscopic food and dissolved oxygen.";
    foot.innerHTML = "<strong>Filtration Marvel:</strong> A 1-meter sponge pumps over 24,000 liters of seawater daily, removing 90% of suspended marine bacteria!";
  } else if(phylum === 'cnidaria'){
    status.textContent = "Tissue Grade • Radial Symmetry & Stinging Cells";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Substrate base -->
        <rect x="140" y="115" width="60" height="10" fill="#334155"/>
        <!-- Hydra body stalk -->
        <path d="M165,115 C160,85 160,65 170,55 L170,50 L175,50 C185,65 185,85 180,115 Z" fill="#047857" stroke="#10b981" stroke-width="2"/>
        <!-- Tentacles radiating from hypostome -->
        <path d="M170,50 Q140,30 115,20" stroke="#34d399" stroke-width="2.5" fill="none"/>
        <path d="M171,50 Q150,15 140,5" stroke="#34d399" stroke-width="2.5" fill="none"/>
        <path d="M173,50 Q173,15 173,-5" stroke="#34d399" stroke-width="2.5" fill="none"/>
        <path d="M174,50 Q195,15 205,5" stroke="#34d399" stroke-width="2.5" fill="none"/>
        <path d="M175,50 Q205,30 230,20" stroke="#34d399" stroke-width="2.5" fill="none"/>
        <text x="225" y="35" fill="#6ee7b7" font-size="8" font-weight="bold">Tentacles with Cnidocytes</text>
        <!-- Cnidocyte Stinging Cell Zoom -->
        <rect x="260" y="45" width="105" height="70" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
        <text x="266" y="60" fill="#a7f3d0" font-size="8" font-weight="bold">Cnidocyte (Nematocyst)</text>
        <path d="M280,95 Q290,75 320,80" stroke="#f43f5e" stroke-width="2" fill="none"/>
        <text x="266" y="105" fill="#fca5a5" font-size="7">Coiled Stinging Barb</text>
      </svg>
    `;
    title.textContent = "Phylum Cnidaria: Hydra, Jellyfish & Corals";
    badge.textContent = "Radial Symmetry &amp; Cnidocytes";
    body.textContent = "Cnidarians have tissue-grade organization and radial symmetry around a central gastrovascular cavity (coelenteron) with a single opening. Tentacles possess stinging cells (cnidocytes) containing paralyzing toxin-injecting nematocysts.";
    foot.innerHTML = "<strong>Coral Reef Foundations:</strong> Tiny colonial cnidarian polyps secrete massive calcium carbonate skeletons, creating ocean reefs visible from space!";
  } else if(phylum === 'platy'){
    status.textContent = "Bilateral Flatworms • Dorsoventrally Flattened";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Planaria body outline -->
        <path d="M60,65 Q110,45 190,52 Q260,58 310,65 Q260,72 190,78 Q110,85 60,65 Z" fill="#9333ea" fill-opacity="0.4" stroke="#c084fc" stroke-width="2"/>
        <!-- Spade head with auricles -->
        <path d="M60,65 L75,50 L85,55 L90,65 L85,75 L75,80 Z" fill="#7e22ce" stroke="#c084fc" stroke-width="1.5"/>
        <!-- Eye spots -->
        <circle cx="75" cy="60" r="2.5" fill="#ffffff"/>
        <circle cx="75" cy="60" r="1.2" fill="#000000"/>
        <circle cx="75" cy="70" r="2.5" fill="#ffffff"/>
        <circle cx="75" cy="70" r="1.2" fill="#000000"/>
        <text x="45" y="45" fill="#e9d5ff" font-size="8" font-weight="bold">Eye Spots &amp; Auricles</text>
        <!-- Incomplete gut / pharynx -->
        <path d="M175,65 Q210,65 240,65" stroke="#f43f5e" stroke-width="3"/>
        <circle cx="175" cy="65" r="4" fill="#fbbf24"/>
        <text x="145" y="95" fill="#fde047" font-size="8">Ventral Mouth / Pharynx</text>
        <text x="210" y="42" fill="#e9d5ff" font-size="8">Acoelomate (No Body Cavity)</text>
      </svg>
    `;
    title.textContent = "Phylum Platyhelminthes: Planaria & Tapeworms";
    badge.textContent = "Bilateral &amp; Acoelomate";
    body.textContent = "First animals with bilateral symmetry (distinct left and right sides, front and back). Body is flattened dorsoventrally ('flat worms') with triploblastic germ layers but lacking a coelom (acoelomate). Digestive cavity has only one opening.";
    foot.innerHTML = "<strong>Hygiene Imperative:</strong> Parasitic tapeworms and liver flukes lack their own digestive system, absorbing host nutrients directly through tegument!";
  } else {
    status.textContent = "Pseudocoelomate • Complete Alimentary Canal";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Ascaris cylindrical body -->
        <path d="M40,65 Q190,40 340,65 Q190,75 40,65 Z" fill="#ea580c" fill-opacity="0.3" stroke="#f97316" stroke-width="2"/>
        <!-- Complete gut running mouth to anus -->
        <line x1="45" y1="65" x2="335" y2="65" stroke="#22c55e" stroke-width="3"/>
        <circle cx="45" cy="65" r="3" fill="#eab308"/>
        <circle cx="335" cy="65" r="3" fill="#ef4444"/>
        <text x="35" y="52" fill="#fde047" font-size="8" font-weight="bold">Mouth (Anterior)</text>
        <text x="310" y="52" fill="#f87171" font-size="8" font-weight="bold">Anus (Posterior)</text>
        <text x="130" y="90" fill="#86efac" font-size="8" font-weight="bold">Complete Digestive Tube (One-Way Flow)</text>
        <text x="140" y="110" fill="#fdba74" font-size="8">Pseudocoelom (False Body Cavity)</text>
      </svg>
    `;
    title.textContent = "Phylum Nematoda: Ascaris & Roundworms";
    badge.textContent = "Pseudocoelomate";
    body.textContent = "Nematodes have cylindrical bodies unsegmented along their length. Possess a pseudocoelom (body cavity not completely lined by mesoderm) and achieve an evolutionary landmark: a complete through-gut with separate mouth and anus.";
    foot.innerHTML = "<strong>Public Health:</strong> Intestinal roundworms like Ascaris spread via contaminated water and unwashed raw vegetables; sanitation breaks transmission!";
  }
};
window.addEventListener('DOMContentLoaded', () => setC12S11('porifera'));
</script>""",

    12: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Higher Invertebrates:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S12('annelida')" id="c12s12_btn_ann" class="px-2 py-1 text-xs font-bold rounded-md bg-indigo-600 text-white transition">Annelida</button>
        <button onclick="setC12S12('arthro')" id="c12s12_btn_art" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Arthropoda</button>
        <button onclick="setC12S12('mollusca')" id="c12s12_btn_mol" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Mollusca</button>
        <button onclick="setC12S12('echino')" id="c12s12_btn_ech" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Echinodermata</button>
        <button onclick="setC12S12('proto')" id="c12s12_btn_pro" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Protochordata</button>
      </div>
    </div>
    <span class="text-xs text-indigo-300 font-mono" id="c12s12_status">True Coelom &bull; Metameric Segments</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c12s12_visual" class="w-full max-w-lg flex flex-col items-center justify-center">
      <!-- Dynamic SVG Visual -->
    </div>

    <div class="w-full max-w-lg mt-2 bg-slate-900/80 border border-slate-700/60 rounded-xl p-2.5">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-bold text-indigo-300" id="c12s12_title">Phylum Annelida: Earthworms &amp; Leeches</span>
        <span class="text-[10px] text-slate-400 font-mono" id="c12s12_badge">Metameric Segmentation</span>
      </div>
      <p class="text-xs text-slate-300 leading-relaxed" id="c12s12_body">
        Annelids possess a true coelom (mesoderm-lined body cavity) and ring-like metameric segments externally and internally. They feature closed blood circulation with hemoglobin and nephridia for nitrogenous excretion.
      </p>
    </div>
  </div>

  <div class="bg-indigo-950/30 border border-indigo-800/40 rounded-xl px-3 py-1.5 text-xs text-indigo-200" id="c12s12_foot">
    <strong>Soil Engineer:</strong> Earthworms ingest organic matter, burrowing millions of tunnels that aerate soil and produce nutrient-rich vermicompost.
  </div>
</div>
<script>
window.setC12S12 = function(p){
  const btns = ['ann', 'art', 'mol', 'ech', 'pro'];
  btns.forEach(b => {
    const el = document.getElementById('c12s12_btn_' + b);
    if(el) el.className = (b === p.substring(0,3)) ?
      'px-2 py-1 text-xs font-bold rounded-md bg-indigo-600 text-white transition' :
      'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  });

  const status = document.getElementById('c12s12_status');
  const vis = document.getElementById('c12s12_visual');
  const title = document.getElementById('c12s12_title');
  const badge = document.getElementById('c12s12_badge');
  const body = document.getElementById('c12s12_body');
  const foot = document.getElementById('c12s12_foot');

  if(p === 'annelida'){
    status.textContent = "True Coelom • Metameric Segments";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Segmented Earthworm body -->
        <g stroke="#9333ea" stroke-width="2" fill="#7e22ce" fill-opacity="0.3">
          <ellipse cx="60" cy="65" rx="8" ry="12"/>
          <ellipse cx="75" cy="65" rx="8" ry="13"/>
          <ellipse cx="90" cy="65" rx="8" ry="14"/>
          <ellipse cx="105" cy="65" rx="8" ry="14"/>
          <!-- Clitellum saddle -->
          <ellipse cx="125" cy="65" rx="14" ry="16" fill="#c084fc" fill-opacity="0.8"/>
          <ellipse cx="145" cy="65" rx="8" ry="14"/>
          <ellipse cx="160" cy="65" rx="8" ry="14"/>
          <ellipse cx="175" cy="65" rx="8" ry="14"/>
          <ellipse cx="190" cy="65" rx="8" ry="13"/>
          <ellipse cx="205" cy="65" rx="8" ry="13"/>
          <ellipse cx="220" cy="65" rx="8" ry="12"/>
          <ellipse cx="235" cy="65" rx="8" ry="11"/>
          <ellipse cx="250" cy="65" rx="8" ry="10"/>
        </g>
        <text x="110" y="38" fill="#e9d5ff" font-size="8" font-weight="bold">Clitellum (Egg Cocoon)</text>
        <text x="50" y="98" fill="#c084fc" font-size="8">Mouth / Prostomium</text>
        <text x="210" y="98" fill="#c084fc" font-size="8">Metameric Segments &amp; Setae</text>
      </svg>
    `;
    title.textContent = "Phylum Annelida: Earthworms & Leeches";
    badge.textContent = "True Coelomate";
    body.textContent = "Annelids feature metameric segmentation: the body is divided into repeated anatomical compartments. The true coelom acts as a hydrostatic skeleton against which circular and longitudinal muscles contract during peristaltic crawling.";
    foot.innerHTML = "<strong>Soil Engine:</strong> Earthworms process tons of fallen leaves into fertile soil castings, vital for sustainable Indian agriculture.";
  } else if(p === 'arthro'){
    status.textContent = "Jointed Legs • Chitinous Exoskeleton (80% Animalia)";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Insect Body: Head, Thorax, Abdomen -->
        <!-- Head -->
        <circle cx="80" cy="65" r="14" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <!-- Antennae -->
        <path d="M75,52 Q60,35 45,30 M85,52 Q95,35 110,30" stroke="#f59e0b" stroke-width="1.5" fill="none"/>
        <!-- Thorax -->
        <ellipse cx="120" cy="65" rx="22" ry="18" fill="#334155" stroke="#f59e0b" stroke-width="2"/>
        <!-- Abdomen (Segmented) -->
        <ellipse cx="180" cy="65" rx="35" ry="16" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <line x1="160" y1="50" x2="160" y2="80" stroke="#64748b"/>
        <line x1="180" y1="50" x2="180" y2="80" stroke="#64748b"/>
        <line x1="200" y1="50" x2="200" y2="80" stroke="#64748b"/>
        <!-- 3 Pairs Jointed legs -->
        <path d="M110,75 L95,100 L85,115 M120,78 L120,105 L115,120 M130,75 L145,102 L155,118" stroke="#f59e0b" stroke-width="2" fill="none"/>
        <text x="65" y="22" fill="#fde047" font-size="8">Antennae</text>
        <text x="105" y="38" fill="#fde047" font-size="8">Thorax</text>
        <text x="170" y="38" fill="#fde047" font-size="8">Abdomen</text>
        <text x="90" y="128" fill="#cbd5e1" font-size="7">3 Pairs Jointed Limbs (Arthropod = Jointed Foot)</text>
      </svg>
    `;
    title.textContent = "Phylum Arthropoda: Insects, Arachnids & Crabs";
    badge.textContent = "Largest Animal Phylum";
    body.textContent = "Comprises over 80% of all animal species. Characterized by jointed appendages, bilateral symmetry, open circulatory system with hemolymph bathing tissues, and a rigid, waterproof chitinous exoskeleton that undergoes molting (ecdysis).";
    foot.innerHTML = "<strong>Unmatched Success:</strong> Their impervious exoskeleton and jointed flight appendages allowed arthropods to conquer every terrestrial ecological niche!";
  } else if(p === 'mollusca'){
    status.textContent = "Soft Body • Mantle & Muscular Foot";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Snail Soft Body -->
        <path d="M80,105 Q120,85 160,95 Q240,95 270,105 Q180,115 80,105 Z" fill="#ca8a04" fill-opacity="0.5" stroke="#eab308" stroke-width="2"/>
        <text x="150" y="120" fill="#fef08a" font-size="8">Muscular Locomotory Foot</text>
        <!-- Head with tentacles -->
        <circle cx="75" cy="95" r="10" fill="#ca8a04"/>
        <path d="M72,85 L60,65 M78,85 L72,60" stroke="#eab308" stroke-width="1.5"/>
        <circle cx="60" cy="65" r="2" fill="#000000"/>
        <circle cx="72" cy="60" r="2" fill="#000000"/>
        <!-- Calcium Carbonate Spiral Shell -->
        <path d="M140,95 C120,40 180,20 220,50 C240,65 240,90 210,95 Z" fill="#78350f" stroke="#d97706" stroke-width="2"/>
        <path d="M165,85 C150,55 190,40 210,65" stroke="#fde68a" stroke-width="1.5" fill="none"/>
        <text x="215" y="45" fill="#fde68a" font-size="8" font-weight="bold">Calcareous Shell (Mantle)</text>
      </svg>
    `;
    title.textContent = "Phylum Mollusca: Snails, Pila & Octopus";
    badge.textContent = "Mantle &amp; Shell";
    body.textContent = "Molluscs have soft, unsegmented bodies divided into head, visceral hump, and muscular ventral foot. A soft fold of skin called the mantle covers the visceral hump and secretes a protective calcium carbonate shell.";
    foot.innerHTML = "<strong>Octopus Intelligence:</strong> While snails retain heavy external shells, octopuses internalized or lost shells, developing advanced problem-solving brains!";
  } else if(p === 'echino'){
    status.textContent = "Spiny Skin • Water Vascular Tube Feet";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- 5-Armed Starfish (Pentamerous Radial) -->
        <g stroke="#f43f5e" stroke-width="2" fill="#e11d48" fill-opacity="0.4">
          <polygon points="190,20 205,55 240,55 212,75 222,110 190,90 158,110 168,75 140,55 175,55"/>
        </g>
        <circle cx="190" cy="65" r="10" fill="#be123c"/>
        <circle cx="190" cy="65" r="4" fill="#fde047"/>
        <text x="140" y="70" fill="#fecdd3" font-size="8">Central Disc</text>
        <!-- Tube Feet hints -->
        <circle cx="190" cy="35" r="1.5" fill="#38bdf8"/>
        <circle cx="190" cy="45" r="1.5" fill="#38bdf8"/>
        <circle cx="215" cy="60" r="1.5" fill="#38bdf8"/>
        <circle cx="205" cy="85" r="1.5" fill="#38bdf8"/>
        <text x="230" y="90" fill="#38bdf8" font-size="8">Tube Feet (Hydraulic Pressure)</text>
        <text x="70" y="115" fill="#fda4af" font-size="8">Calcareous Endoskeleton with Spines</text>
      </svg>
    `;
    title.textContent = "Phylum Echinodermata: Starfish & Sea Urchins";
    badge.textContent = "Spiny Endoskeleton";
    body.textContent = "Exclusively marine animals with calcareous endoskeletal plates and projecting spines (echinos = hedgehog, derma = skin). Larvae are bilaterally symmetrical, but adults adopt pentamerous radial symmetry and move via hydraulic tube feet.";
    foot.innerHTML = "<strong>Hydraulic Locomotion:</strong> The water vascular system powers thousands of suction tube feet to grip rocks and pry open bivalve prey!";
  } else {
    status.textContent = "Marine Invertebrate Chordates • Notochord";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Amphioxus fish-like body -->
        <path d="M50,65 Q190,40 330,65 Q190,85 50,65 Z" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
        <!-- Dorsal Nerve Cord -->
        <path d="M60,56 Q190,46 315,58" stroke="#f43f5e" stroke-width="2" fill="none"/>
        <text x="70" y="42" fill="#fca5a5" font-size="8">Dorsal Tubular Nerve Cord</text>
        <!-- Notochord rod below nerve cord -->
        <path d="M65,62 Q190,52 320,64" stroke="#eab308" stroke-width="3" fill="none"/>
        <text x="140" y="75" fill="#fde047" font-size="8" font-weight="bold">Rigid Notochord Rod (Persistent)</text>
        <!-- Pharyngeal gill slits -->
        <line x1="85" y1="65" x2="85" y2="78" stroke="#38bdf8" stroke-width="1.5"/>
        <line x1="95" y1="65" x2="95" y2="78" stroke="#38bdf8" stroke-width="1.5"/>
        <line x1="105" y1="65" x2="105" y2="78" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="80" y="92" fill="#7dd3fc" font-size="7">Pharyngeal Slits</text>
      </svg>
    `;
    title.textContent = "Protochordata: Amphioxus & Herdmania";
    badge.textContent = "Precursor of Vertebrates";
    body.textContent = "Protochordates are marine organisms that possess a notochord—a flexible, rod-like structure providing skeletal support along the back—at certain life stages. They bridge the evolutionary gap between non-chordates and vertebrates.";
    foot.innerHTML = "<strong>Evolutionary Milestone:</strong> The notochord provides internal anchorage for muscles, prefiguring the bony vertebral column of true vertebrates!";
  }
};
window.addEventListener('DOMContentLoaded', () => setC12S12('annelida'));
</script>""",

    13: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Vertebrata Classes:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S13('pisces')" id="c12s13_btn_pis" class="px-2 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition">Pisces</button>
        <button onclick="setC12S13('amphibia')" id="c12s13_btn_amp" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Amphibia</button>
        <button onclick="setC12S13('reptilia')" id="c12s13_btn_rep" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Reptilia</button>
        <button onclick="setC12S13('aves')" id="c12s13_btn_ave" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Aves</button>
        <button onclick="setC12S13('mammalia')" id="c12s13_btn_mam" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Mammalia</button>
        <button onclick="setC12S13('shield')" id="c12s13_btn_shi" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Bioshield</button>
      </div>
    </div>
    <span class="text-xs text-emerald-300 font-mono" id="c12s13_status">2-Chambered Heart &bull; Gills &bull; Cold-Blooded</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c12s13_visual" class="w-full max-w-lg flex flex-col items-center justify-center">
      <!-- Dynamic SVG Visual -->
    </div>

    <!-- Metrics Bar -->
    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <span class="text-[10px] text-slate-400 font-semibold uppercase block" id="c12s13_m1_lbl">Heart Chambers</span>
        <span class="text-xs font-bold text-rose-400" id="c12s13_m1_val">2 Chambers (1A + 1V)</span>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <span class="text-[10px] text-slate-400 font-semibold uppercase block" id="c12s13_m2_lbl">Thermal Regulation</span>
        <span class="text-xs font-bold text-cyan-400" id="c12s13_m2_val">Poikilothermic (Cold)</span>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <span class="text-[10px] text-slate-400 font-semibold uppercase block" id="c12s13_m3_lbl">Respiration</span>
        <span class="text-xs font-bold text-amber-400" id="c12s13_m3_val">Gills with Operculum</span>
      </div>
    </div>
  </div>

  <div class="bg-emerald-950/30 border border-emerald-800/40 rounded-xl px-3 py-1.5 text-xs text-emerald-200" id="c12s13_desc">
    <strong>Comparative Vertebrata:</strong> Vertebrates replace the embryonic notochord with a segmented cartilaginous or bony vertebral column, protecting the central nervous cord and enabling complex locomotion.
  </div>
</div>
<script>
window.setC12S13 = function(cls){
  const btns = ['pis', 'amp', 'rep', 'ave', 'mam', 'shi'];
  btns.forEach(b => {
    const el = document.getElementById('c12s13_btn_' + b);
    if(el) el.className = (b === cls.substring(0,3)) ?
      'px-2 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition' :
      'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  });

  const status = document.getElementById('c12s13_status');
  const vis = document.getElementById('c12s13_visual');
  const m1 = document.getElementById('c12s13_m1_val');
  const m2 = document.getElementById('c12s13_m2_val');
  const m3 = document.getElementById('c12s13_m3_val');
  const desc = document.getElementById('c12s13_desc');

  if(cls === 'pisces'){
    status.textContent = "2-Chambered Heart • Gills • Cold-Blooded";
    vis.innerHTML = `
      <svg viewBox="0 0 380 120" class="w-full h-28">
        <!-- Fish Body -->
        <path d="M60,60 Q150,20 280,60 Q150,100 60,60 Z" fill="#0284c7" fill-opacity="0.4" stroke="#38bdf8" stroke-width="2"/>
        <polygon points="280,60 330,30 315,60 330,90" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
        <path d="M140,35 Q180,25 210,40" stroke="#38bdf8" stroke-width="2" fill="none"/>
        <!-- Gills & Eye -->
        <circle cx="95" cy="52" r="3" fill="#ffffff"/>
        <circle cx="95" cy="52" r="1.5" fill="#000000"/>
        <path d="M125,48 Q115,60 125,72" stroke="#f43f5e" stroke-width="2.5" fill="none"/>
        <text x="130" y="62" fill="#fca5a5" font-size="8">Gills (O₂ Intake)</text>
        <!-- Heart illustration -->
        <circle cx="110" cy="75" r="7" fill="#ef4444"/>
        <text x="75" y="95" fill="#fca5a5" font-size="8">2-Chamber Heart</text>
      </svg>
    `;
    m1.textContent = "2 Chambers (1A + 1V)";
    m2.textContent = "Poikilotherm (Cold)";
    m3.textContent = "Gills with Counter-Current";
    desc.innerHTML = "<strong>Class Pisces:</strong> Exclusively aquatic jawed vertebrates. Streamlined body covered by dermal scales. Fins provide propulsion and balance; heart pumps purely deoxygenated blood in a single circuit.";
  } else if(cls === 'amphibia'){
    status.textContent = "3-Chambered Heart • Dual Aquatic/Terrestrial Life";
    vis.innerHTML = `
      <svg viewBox="0 0 380 120" class="w-full h-28">
        <!-- Frog Body -->
        <ellipse cx="180" cy="65" rx="35" ry="24" fill="#15803d" fill-opacity="0.5" stroke="#22c55e" stroke-width="2"/>
        <ellipse cx="150" cy="50" rx="15" ry="12" fill="#15803d"/>
        <circle cx="145" cy="42" r="4" fill="#eab308"/>
        <circle cx="145" cy="42" r="2" fill="#000000"/>
        <!-- Limbs -->
        <path d="M160,75 L140,95 L125,95 M205,72 L230,95 L250,90" stroke="#22c55e" stroke-width="3" fill="none"/>
        <text x="110" y="32" fill="#86efac" font-size="8">Moist Cutaneous Skin</text>
        <!-- 3-Chamber Heart -->
        <circle cx="180" cy="65" r="8" fill="#ef4444"/>
        <text x="155" y="80" fill="#fca5a5" font-size="8">3-Chamber Heart</text>
      </svg>
    `;
    m1.textContent = "3 Chambers (2A + 1V)";
    m2.textContent = "Poikilotherm (Cold)";
    m3.textContent = "Lungs, Gills (Larva) & Skin";
    desc.innerHTML = "<strong>Class Amphibia:</strong> Lead dual lives. Aquatic larvae respire via gills (tadpoles), metamorphosing into adults that respire via lungs and moist vascular skin. Must lay shell-less eggs in water.";
  } else if(cls === 'reptilia'){
    status.textContent = "Dry Scales • Shelled Cleidoic Eggs on Land";
    vis.innerHTML = `
      <svg viewBox="0 0 380 120" class="w-full h-28">
        <!-- Lizard / Reptile Body -->
        <path d="M70,60 Q180,45 280,60" stroke="#78350f" stroke-width="12" stroke-linecap="round" fill="none"/>
        <!-- Epidermal scales pattern -->
        <line x1="120" y1="52" x2="120" y2="68" stroke="#ca8a04" stroke-width="2"/>
        <line x1="150" y1="50" x2="150" y2="68" stroke="#ca8a04" stroke-width="2"/>
        <line x1="180" y1="50" x2="180" y2="68" stroke="#ca8a04" stroke-width="2"/>
        <!-- Cleidoic egg with shell -->
        <ellipse cx="320" cy="60" rx="14" ry="10" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
        <text x="295" y="85" fill="#f8fafc" font-size="8">Amniotic Egg (Shell)</text>
        <text x="90" y="35" fill="#fde047" font-size="8">Waterproof Epidermal Scales</text>
      </svg>
    `;
    m1.textContent = "3 Chambers (4 in Crocs)";
    m2.textContent = "Poikilotherm (Cold)";
    m3.textContent = "Pulmonary Lungs Exclusively";
    desc.innerHTML = "<strong>Class Reptilia:</strong> First truly terrestrial vertebrates. Epidermal horny scales prevent dehydration. Shelled cleidoic eggs with fluid-filled amnion free reproduction entirely from aquatic bodies.";
  } else if(cls === 'aves'){
    status.textContent = "4-Chambered Heart • Feathers & Hollow Pneumatic Bones";
    vis.innerHTML = `
      <svg viewBox="0 0 380 120" class="w-full h-28">
        <!-- Bird in Flight -->
        <ellipse cx="180" cy="60" rx="25" ry="14" fill="#3b82f6" fill-opacity="0.4" stroke="#60a5fa" stroke-width="2"/>
        <!-- Wing feathers -->
        <path d="M170,55 Q130,15 90,20 Q130,40 165,58 Z" fill="#2563eb" stroke="#93c5fd"/>
        <path d="M190,55 Q230,15 270,20 Q230,40 195,58 Z" fill="#2563eb" stroke="#93c5fd"/>
        <!-- Beak & Eye -->
        <circle cx="160" cy="55" r="2" fill="#000000"/>
        <polygon points="155,58 140,62 155,66" fill="#f59e0b"/>
        <text x="140" y="100" fill="#93c5fd" font-size="8" font-weight="bold">Pneumatic Hollow Bones &amp; Warm-Blooded</text>
      </svg>
    `;
    m1.textContent = "4 Chambers (Complete)";
    m2.textContent = "Homeotherm (Warm-Blooded)";
    m3.textContent = "Lungs with Air Sacs";
    desc.innerHTML = "<strong>Class Aves:</strong> Endothermic vertebrates evolved for aerial locomotion. Forelimbs modified into wings with aerodynamic feathers. Bones are pneumatic and filled with air cavities to reduce body mass.";
  } else if(cls === 'mammalia'){
    status.textContent = "Mammary Glands • Hair • Viviparity & Endothermy";
    vis.innerHTML = `
      <svg viewBox="0 0 380 120" class="w-full h-28">
        <!-- Mammal outline (Tiger silhouette motif) -->
        <ellipse cx="180" cy="60" rx="38" ry="20" fill="#d97706" fill-opacity="0.4" stroke="#f59e0b" stroke-width="2"/>
        <circle cx="135" cy="48" r="14" fill="#b45309"/>
        <path d="M130,36 L126,28 L136,32 M144,36 L148,28 L140,32" stroke="#f59e0b" stroke-width="2" fill="none"/>
        <text x="110" y="98" fill="#fde047" font-size="8">Mammary Glands (Milk)</text>
        <text x="210" y="98" fill="#fde047" font-size="8">Body Hair / Fur</text>
        <!-- Heart -->
        <circle cx="170" cy="62" r="7" fill="#ef4444"/>
        <text x="180" y="65" fill="#fca5a5" font-size="7">4-Chamber Heart</text>
      </svg>
    `;
    m1.textContent = "4 Chambers (Complete)";
    m2.textContent = "Homeotherm (Warm-Blooded)";
    m3.textContent = "Pulmonary Diaphragm Lungs";
    desc.innerHTML = "<strong>Class Mammalia:</strong> Distinguished by mammary glands that produce milk for nourishing neonates. Possess epidermal hair/fur, sweat glands, external pinnae, and give birth to live young (viviparous).";
  } else {
    status.textContent = "Odisha Cyclone Bioshield &amp; Forest Buffers";
    vis.innerHTML = `
      <svg viewBox="0 0 380 120" class="w-full h-28">
        <!-- Coastal Mangrove Bioshield -->
        <rect x="30" y="70" width="120" height="40" fill="#0f766e"/>
        <text x="35" y="85" fill="#a7f3d0" font-size="8" font-weight="bold">Mangrove Bioshield</text>
        <text x="35" y="98" fill="#ccfbf1" font-size="7">Bhitarkanika / Odisha</text>
        <!-- Storm Surge Waves dissipated -->
        <path d="M150,85 Q170,70 190,85 T230,85" stroke="#38bdf8" stroke-width="3" fill="none"/>
        <text x="160" y="65" fill="#38bdf8" font-size="8">Cyclonic Tidal Surge</text>
        <!-- Protected Villages -->
        <rect x="250" y="60" width="100" height="50" rx="4" fill="#1e293b" stroke="#64748b"/>
        <text x="260" y="80" fill="#f8fafc" font-size="8" font-weight="bold">Human Settlement</text>
        <text x="260" y="95" fill="#4ade80" font-size="8">Zero Wave Damage</text>
      </svg>
    `;
    m1.textContent = "Mangrove Stilt Roots";
    m2.textContent = "Wave Energy Absorption";
    m3.textContent = "Kyasanur Disease Buffer";
    desc.innerHTML = "<strong>Ecological Bioshield:</strong> During the catastrophic 1999 Odisha super cyclone, villages sheltered behind intact mangrove forests suffered negligible mortality compared to exposed cleared coasts. Intact forests also prevent viral spillover!";
  }
};
window.addEventListener('DOMContentLoaded', () => setC12S13('pisces'));
</script>""",

    14: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Taxonomic Hierarchy:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S14('tiger')" id="c12s14_btn_tig" class="px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">Tiger (Panthera tigris)</button>
        <button onclick="setC12S14('pea')" id="c12s14_btn_pea" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Garden Pea (Pisum sativum)</button>
        <button onclick="setC12S14('human')" id="c12s14_btn_hum" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Human (Homo sapiens)</button>
      </div>
    </div>
    <span class="text-xs text-cyan-300 font-mono" id="c12s14_sciname">Panthera tigris</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-between">
    <!-- 7 Obligate Ranks Visual Hierarchy Ladder -->
    <div id="c12s14_ladder" class="grid grid-cols-7 gap-1.5 my-auto">
      <!-- Generated dynamically -->
    </div>

    <!-- Hierarchy Details Card -->
    <div class="bg-slate-900/80 border border-slate-700/60 rounded-xl p-3">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-bold text-cyan-300" id="c12s14_rank_title">Kingdom to Species Progression</span>
        <span class="text-[10px] text-slate-400 font-mono" id="c12s14_rule">Broadest &rarr; Specific</span>
      </div>
      <p class="text-xs text-slate-300 leading-relaxed" id="c12s14_rank_desc">
        Taxonomic categories form a descending obligate hierarchy. As we descend from Kingdom to Species, the number of shared morphological, physiological, and genetic characteristics increases while total member count narrows.
      </p>
    </div>

    <div class="grid grid-cols-2 gap-2 text-xs">
      <div class="bg-slate-900/50 border border-slate-800 rounded-lg p-2">
        <span class="text-[10px] text-slate-400 font-semibold uppercase block">Species Definition</span>
        <span class="text-emerald-300 font-semibold">Organisms capable of freely interbreeding in nature to yield fertile offspring.</span>
      </div>
      <div class="bg-slate-900/50 border border-slate-800 rounded-lg p-2">
        <span class="text-[10px] text-slate-400 font-semibold uppercase block">Linnaean Memory Aid</span>
        <span class="text-amber-300 font-semibold">"King Philip Came Over For Good Soup" (K-P-C-O-F-G-S)</span>
      </div>
    </div>
  </div>
</div>
<script>
window.setC12S14 = function(spec){
  const btns = ['tig', 'pea', 'hum'];
  btns.forEach(b => {
    const el = document.getElementById('c12s14_btn_' + b);
    if(el) el.className = (b === spec.substring(0,3)) ?
      'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition' :
      'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  });

  const sciname = document.getElementById('c12s14_sciname');
  const ladder = document.getElementById('c12s14_ladder');
  const title = document.getElementById('c12s14_rank_title');
  const desc = document.getElementById('c12s14_rank_desc');

  const data = {
    tiger: {
      sci: "Panthera tigris",
      t: "Taxonomic Hierarchy: Bengal Tiger (National Animal of India)",
      d: "Belongs to apex mammalian carnivores. Shares the family Felidae with domestic cats, but separated into genus Panthera due to roaring hyoid anatomy.",
      ranks: [
        { r: "Kingdom", v: "Animalia" },
        { r: "Phylum", v: "Chordata" },
        { r: "Class", v: "Mammalia" },
        { r: "Order", v: "Carnivora" },
        { r: "Family", v: "Felidae" },
        { r: "Genus", v: "Panthera" },
        { r: "Species", v: "tigris" }
      ]
    },
    pea: {
      sci: "Pisum sativum",
      t: "Taxonomic Hierarchy: Garden Pea (Mendel's Genetic Model)",
      d: "A dicotyledonous legume in family Fabaceae. Produces nitrogen-fixing root nodules in symbiosis with Rhizobium bacteria.",
      ranks: [
        { r: "Kingdom", v: "Plantae" },
        { r: "Division", v: "Magnoliophyta" },
        { r: "Class", v: "Magnoliopsida" },
        { r: "Order", v: "Fabales" },
        { r: "Family", v: "Fabaceae" },
        { r: "Genus", v: "Pisum" },
        { r: "Species", v: "sativum" }
      ]
    },
    human: {
      sci: "Homo sapiens",
      t: "Taxonomic Hierarchy: Anatomically Modern Human",
      d: "Bipedal primate characterized by an enlarged neocortex, stereoscopic binocular vision, and complex linguistic communication.",
      ranks: [
        { r: "Kingdom", v: "Animalia" },
        { r: "Phylum", v: "Chordata" },
        { r: "Class", v: "Mammalia" },
        { r: "Order", v: "Primates" },
        { r: "Family", v: "Hominidae" },
        { r: "Genus", v: "Homo" },
        { r: "Species", v: "sapiens" }
      ]
    }
  };

  const cur = data[spec];
  sciname.textContent = cur.sci;
  title.textContent = cur.t;
  desc.textContent = cur.d;

  ladder.innerHTML = cur.ranks.map((item, idx) => `
    <div class="flex flex-col items-center p-2 rounded-xl bg-slate-900/70 border border-slate-800 text-center transition hover:border-cyan-500">
      <span class="text-[9px] text-cyan-400 font-bold uppercase tracking-wider">${item.r}</span>
      <span class="text-xs font-bold text-slate-200 mt-1">${item.v}</span>
      <span class="text-[8px] text-slate-500 mt-0.5">Rank ${idx+1}</span>
    </div>
  `).join('');
};
window.addEventListener('DOMContentLoaded', () => setC12S14('tiger'));
</script>""",

    15: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-purple-400 uppercase tracking-wider">Binomial &amp; 3 Domains:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S15('rules')" id="c12s15_btn_rul" class="px-2 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition">Linnaean Rules</button>
        <button onclick="setC12S15('domains')" id="c12s15_btn_dom" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Woese 3 Domains (1977)</button>
        <button onclick="setC12S15('frog')" id="c12s15_btn_fro" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Purple Frog Fossil</button>
      </div>
    </div>
    <span class="text-xs text-purple-300 font-mono" id="c12s15_status">Genus capitalized &bull; species lowercase</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c12s15_visual" class="w-full max-w-lg flex flex-col items-center justify-center">
      <!-- Dynamic SVG Visual -->
    </div>

    <div class="w-full max-w-lg mt-2 bg-slate-900/80 border border-slate-700/60 rounded-xl p-2.5">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-bold text-purple-300" id="c12s15_title">Rules of Binomial Nomenclature</span>
        <span class="text-[10px] text-slate-400 font-mono" id="c12s15_badge">Universal Latin Code</span>
      </div>
      <p class="text-xs text-slate-300 leading-relaxed" id="c12s15_body">
        Devised by Carolus Linnaeus. Every scientific name consists of two parts: the generic name (Genus) starting with a capital letter, followed by the specific epithet (species) in lowercase. Printed in italics or underlined when handwritten.
      </p>
    </div>
  </div>

  <div class="bg-purple-950/30 border border-purple-800/40 rounded-xl px-3 py-1.5 text-xs text-purple-200" id="c12s15_foot">
    <strong>Universal Language:</strong> Eliminates global confusion caused by local vernacular names across different languages and regions.
  </div>
</div>
<script>
window.setC12S15 = function(v){
  const btns = ['rul', 'dom', 'fro'];
  btns.forEach(b => {
    const el = document.getElementById('c12s15_btn_' + b);
    if(el) el.className = (b === v.substring(0,3)) ?
      'px-2 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition' :
      'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  });

  const status = document.getElementById('c12s15_status');
  const vis = document.getElementById('c12s15_visual');
  const title = document.getElementById('c12s15_title');
  const badge = document.getElementById('c12s15_badge');
  const body = document.getElementById('c12s15_body');
  const foot = document.getElementById('c12s15_foot');

  if(v === 'rules'){
    status.textContent = "Genus capitalized • species lowercase • Italics";
    vis.innerHTML = `
      <svg viewBox="0 0 380 120" class="w-full h-28">
        <!-- Botanical Example: Mangifera indica -->
        <rect x="30" y="25" width="320" height="70" rx="10" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <text x="50" y="65" font-family="serif" font-style="italic" font-size="24" fill="#ffffff">
          <tspan fill="#38bdf8" font-weight="bold">Mangifera</tspan>
          <tspan dx="15" fill="#f43f5e" font-weight="bold">indica</tspan>
        </text>
        <!-- Annotations -->
        <path d="M95,75 L95,85" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="60" y="95" fill="#38bdf8" font-size="8" font-weight="bold">1. Genus (Capital M)</text>
        <path d="M225,75 L225,85" stroke="#f43f5e" stroke-width="1.5"/>
        <text x="180" y="95" fill="#f43f5e" font-size="8" font-weight="bold">2. Specific Epithet (Lowercase i)</text>
      </svg>
    `;
    title.textContent = "Linnaean Latin Binomial System";
    badge.textContent = "International Code (ICBN/ICZN)";
    body.textContent = "Latinized names provide a permanent international benchmark. When handwritten, both words must be underlined separately (e.g. Mangifera indica). Example: Mango is Mangifera indica; Tiger is Panthera tigris.";
    foot.innerHTML = "<strong>Linnaean Genius:</strong> Replaced cumbersome 10-word descriptive polynomial phrases with an elegant 2-word identifier!";
  } else if(v === 'domains'){
    status.textContent = "Carl Woese (1977) • 16S Ribosomal RNA Divergence";
    vis.innerHTML = `
      <svg viewBox="0 0 380 120" class="w-full h-28">
        <!-- 3 Domains Tree -->
        <!-- Ancestral Root -->
        <circle cx="50" cy="60" r="10" fill="#64748b"/>
        <text x="35" y="85" fill="#94a3b8" font-size="8">LUCA</text>
        <path d="M55,60 Q100,60 140,30" stroke="#f59e0b" stroke-width="3" fill="none"/>
        <path d="M55,60 Q100,60 140,60" stroke="#ec4899" stroke-width="3" fill="none"/>
        <path d="M55,60 Q100,60 140,90" stroke="#06b6d4" stroke-width="3" fill="none"/>
        <!-- Domain 1: Bacteria -->
        <rect x="140" y="15" width="180" height="25" rx="5" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="150" y="32" fill="#fde68a" font-size="9" font-weight="bold">Domain Bacteria (True Bacteria)</text>
        <!-- Domain 2: Archaea -->
        <rect x="140" y="48" width="180" height="25" rx="5" fill="#831843" stroke="#ec4899" stroke-width="1.5"/>
        <text x="150" y="65" fill="#fbcfe8" font-size="9" font-weight="bold">Domain Archaea (Methanogens)</text>
        <!-- Domain 3: Eukarya -->
        <rect x="140" y="80" width="180" height="25" rx="5" fill="#083344" stroke="#06b6d4" stroke-width="1.5"/>
        <text x="150" y="97" fill="#a5f3fc" font-size="9" font-weight="bold">Domain Eukarya (Plants, Animals, Fungi)</text>
      </svg>
    `;
    title.textContent = "Carl Woese's Three Domains of Life (1977)";
    badge.textContent = "Molecular Phylogenetics";
    body.textContent = "By comparing base sequences in 16S and 18S ribosomal RNA, Carl Woese revealed that Archaea differ as profoundly from true Bacteria as both do from Eukaryotes, fundamentally reorganizing the tree of life into three primary Domains.";
    foot.innerHTML = "<strong>Deep Ancestry:</strong> Archaea thrive in extreme conditions (boiling hot springs, hypersaline lakes) resembling Earth's primordial crust!";
  } else {
    status.textContent = "Western Ghats Endemic • Gondwana Living Fossil";
    vis.innerHTML = `
      <svg viewBox="0 0 380 120" class="w-full h-28">
        <!-- Nasikabatrachus sahyadrensis (Purple Frog) -->
        <ellipse cx="190" cy="65" rx="38" ry="26" fill="#581c87" stroke="#a855f7" stroke-width="2.5"/>
        <!-- Pointed Snout -->
        <polygon points="152,65 140,65 152,69" fill="#c084fc"/>
        <circle cx="158" cy="58" r="2.5" fill="#ffffff"/>
        <circle cx="158" cy="58" r="1.2" fill="#000000"/>
        <!-- Digging Spades on Hind Limbs -->
        <ellipse cx="225" cy="80" rx="8" ry="6" fill="#7e22ce" stroke="#c084fc"/>
        <text x="80" y="30" fill="#e9d5ff" font-size="9" font-weight="bold">Nasikabatrachus sahyadrensis (Purple Frog)</text>
        <text x="110" y="105" fill="#c084fc" font-size="8">Subterranean Fossorial Digger &bull; Western Ghats</text>
      </svg>
    `;
    title.textContent = "Western Ghats Purple Frog: Nasikabatrachus sahyadrensis";
    badge.textContent = "Gondwana Living Fossil";
    body.textContent = "Discovered in 2003 in Kerala's Western Ghats. Its closest living relatives are burrowing frogs found only in the Seychelles Islands, proving continental drift tore apart the ancient Gondwanaland supercontinent over 100 million years ago!";
    foot.innerHTML = "<strong>Fossorial Life:</strong> Spends nearly 360 days a year underground in deep mud, emerging only for two days of monsoon breeding!";
  }
};
window.addEventListener('DOMContentLoaded', () => setC12S15('rules'));
</script>""",

    16: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Fossils &amp; Conservation:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S16('strata')" id="c12s16_btn_str" class="px-2 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">Geological Strata</button>
        <button onclick="setC12S16('sahni')" id="c12s16_btn_sah" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Birbal Sahni Institute</button>
        <button onclick="setC12S16('loktak')" id="c12s16_btn_lok" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Loktak Phumdis &amp; Sangai</button>
      </div>
    </div>
    <span class="text-xs text-amber-300 font-mono" id="c12s16_status">Sedimentary Layers &bull; Deep Time</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c12s16_visual" class="w-full max-w-lg flex flex-col items-center justify-center">
      <!-- Dynamic SVG Visual -->
    </div>

    <div class="w-full max-w-lg mt-2 bg-slate-900/80 border border-slate-700/60 rounded-xl p-2.5">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-bold text-amber-300" id="c12s16_title">Geological Rock Strata &amp; Fossil Progression</span>
        <span class="text-[10px] text-slate-400 font-mono" id="c12s16_badge">Law of Superposition</span>
      </div>
      <p class="text-xs text-slate-300 leading-relaxed" id="c12s16_body">
        Sedimentary rock layers preserve physical chronological records of past life. Deeper strata contain simpler micro-organisms and invertebrates, while recent upper layers hold complex reptiles, birds, and mammals.
      </p>
    </div>
  </div>

  <div class="bg-amber-950/30 border border-amber-800/40 rounded-xl px-3 py-1.5 text-xs text-amber-200" id="c12s16_foot">
    <strong>Conservation Sanctuary:</strong> Keibul Lamjao National Park on Loktak Lake is the world's only floating sanctuary, protecting the endangered brow-antlered dancing deer!
  </div>
</div>
<script>
window.setC12S16 = function(m){
  const btns = ['str', 'sah', 'lok'];
  btns.forEach(b => {
    const el = document.getElementById('c12s16_btn_' + b);
    if(el) el.className = (b === m.substring(0,3)) ?
      'px-2 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition' :
      'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  });

  const status = document.getElementById('c12s16_status');
  const vis = document.getElementById('c12s16_visual');
  const title = document.getElementById('c12s16_title');
  const badge = document.getElementById('c12s16_badge');
  const body = document.getElementById('c12s16_body');
  const foot = document.getElementById('c12s16_foot');

  if(m === 'strata'){
    status.textContent = "Sedimentary Layers • Chronological Progression";
    vis.innerHTML = `
      <svg viewBox="0 0 380 120" class="w-full h-28">
        <!-- Layer 4 (Recent Top) -->
        <rect x="40" y="10" width="300" height="25" fill="#475569" stroke="#94a3b8" stroke-width="1"/>
        <text x="50" y="27" fill="#f1f5f9" font-size="8" font-weight="bold">Top Layer (Cenozoic): Mammals &amp; Birds</text>
        <!-- Layer 3 -->
        <rect x="40" y="35" width="300" height="25" fill="#334155" stroke="#64748b" stroke-width="1"/>
        <text x="50" y="52" fill="#cbd5e1" font-size="8" font-weight="bold">Layer 3 (Mesozoic): Dinosaurs, Conifers &amp; Reptiles</text>
        <!-- Layer 2 -->
        <rect x="40" y="60" width="300" height="25" fill="#1e293b" stroke="#475569" stroke-width="1"/>
        <text x="50" y="77" fill="#94a3b8" font-size="8" font-weight="bold">Layer 2 (Paleozoic): Early Fish, Ferns &amp; Trilobites</text>
        <!-- Layer 1 (Deepest Bottom) -->
        <rect x="40" y="85" width="300" height="25" fill="#0f172a" stroke="#334155" stroke-width="1"/>
        <text x="50" y="102" fill="#64748b" font-size="8" font-weight="bold">Deepest Layer (Precambrian): Stromatolites &amp; Cyanobacteria</text>
      </svg>
    `;
    title.textContent = "Geological Superposition: Simpler to Complex";
    badge.textContent = "Fossil Time Horizon";
    body.textContent = "According to the Law of Superposition, younger rock strata lie atop older strata unless disturbed. Deepest sedimentary rocks hold exclusively unicellular prokaryotes, proving that complex organisms evolved gradually over millions of years.";
    foot.innerHTML = "<strong>Fossilization:</strong> Hard mineral parts (bones, shells, woody stems) petrify under sediment, replacing organic matter with silica and calcium.";
  } else if(m === 'sahni'){
    status.textContent = "Birbal Sahni (1891-1949) • BSIP Lucknow";
    vis.innerHTML = `
      <svg viewBox="0 0 380 120" class="w-full h-28">
        <!-- Fossil Leaf / Petrifaction Block -->
        <rect x="50" y="20" width="130" height="80" rx="8" fill="#3f3f46" stroke="#a1a1aa" stroke-width="2"/>
        <text x="60" y="40" fill="#f4f4f5" font-size="8" font-weight="bold">Glossopteris Fossil</text>
        <path d="M115,85 Q110,60 115,45 M115,65 L100,55 M115,65 L130,55 M115,55 L105,48 M115,55 L125,48" stroke="#fde047" stroke-width="1.5" fill="none"/>
        <text x="60" y="92" fill="#fbbf24" font-size="7">Gondwana Seed Fern</text>
        <!-- BSIP Lucknow Memorial Plaque -->
        <rect x="200" y="20" width="140" height="80" rx="8" fill="#1c1917" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="210" y="38" fill="#fde68a" font-size="8" font-weight="bold">BSIP, Lucknow</text>
        <text x="210" y="52" fill="#cbd5e1" font-size="7">Birbal Sahni Institute</text>
        <text x="210" y="64" fill="#cbd5e1" font-size="7">of Palaeosciences</text>
        <text x="210" y="80" fill="#38bdf8" font-size="7">• Pentoxylon discovery</text>
        <text x="210" y="92" fill="#38bdf8" font-size="7">• Continental Drift Proof</text>
      </svg>
    `;
    title.textContent = "Birbal Sahni: Father of Indian Palaeobotany";
    badge.textContent = "BSIP Lucknow Pioneer";
    body.textContent = "Birbal Sahni investigated ancient plant fossils across the Rajmahal Hills and Vindhyas. His discovery of the extinct gymnosperm genus Pentoxylon and studies on Glossopteris flora provided critical evidence proving India was once part of the Gondwana supercontinent.";
    foot.innerHTML = "<strong>World Authority:</strong> Established the prestigious Birbal Sahni Institute of Palaeosciences (BSIP) in Lucknow in 1946.";
  } else {
    status.textContent = "Keibul Lamjao National Park • Floating Phumdis";
    vis.innerHTML = `
      <svg viewBox="0 0 380 120" class="w-full h-28">
        <!-- Loktak Lake Water -->
        <rect x="30" y="75" width="320" height="35" fill="#0369a1"/>
        <text x="40" y="100" fill="#e0f2fe" font-size="8">Loktak Lake (Manipur)</text>
        <!-- Floating Phumdi biomass mat -->
        <ellipse cx="190" cy="75" rx="90" ry="14" fill="#166534" stroke="#4ade80" stroke-width="2"/>
        <path d="M120,75 Q150,70 190,75 T260,75" stroke="#15803d" stroke-width="3" fill="none"/>
        <text x="145" y="70" fill="#bbf7d0" font-size="8" font-weight="bold">Floating Phumdi Mat</text>
        <!-- Sangai Deer silhouette -->
        <ellipse cx="205" cy="45" rx="14" ry="10" fill="#92400e"/>
        <circle cx="192" cy="38" r="5" fill="#92400e"/>
        <!-- Brow antlers -->
        <path d="M190,34 L184,24 M190,34 L194,22" stroke="#d97706" stroke-width="1.5"/>
        <line x1="200" y1="55" x2="198" y2="70" stroke="#78350f" stroke-width="1.5"/>
        <line x1="212" y1="55" x2="214" y2="70" stroke="#78350f" stroke-width="1.5"/>
        <text x="215" y="35" fill="#fde68a" font-size="8" font-weight="bold">Sangai Deer (Rucervus eldii)</text>
      </svg>
    `;
    title.textContent = "Loktak Lake Phumdis &amp; Endemic Sangai Deer";
    badge.textContent = "Floating National Park";
    body.textContent = "Keibul Lamjao National Park in Manipur is the world's only floating wildlife sanctuary. Formed of thick floating mats of soil and decomposed vegetation called phumdis, it serves as the last natural refuge for the critically endangered Sangai (dancing deer).";
    foot.innerHTML = "<strong>Community Conservation:</strong> Protecting Loktak's unique phumdi hydrology is crucial to saving the dancing deer from extinction!";
  }
};
window.addEventListener('DOMContentLoaded', () => setC12S16('strata'));
</script>"""
}
