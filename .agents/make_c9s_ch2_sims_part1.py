#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Science Chapter 2: Cell: The Building Block of Life
Part 1: Simulators 1 to 8 (Slides 1 to 8)
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🌋</span> Origin of Life &amp; Cellular Hierarchy Explorer
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <button onclick="c9s2s1Pick(0)" class="py-2 rounded-xl bg-emerald-500/20 border border-emerald-400/50 text-emerald-200 font-bold">Puga Valley (3.5B yrs ago)</button>
    <button onclick="c9s2s1Pick(1)" class="py-2 rounded-xl bg-cyan-500/20 border border-cyan-400/50 text-cyan-200 font-bold">Cellular Organization</button>
  </div>
  <div id="c9s2s1Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2"></div>
</div>
<script>
(function(){
  const views = [
    `<div class="font-bold text-amber-300 text-sm">Early Aquatic Life &amp; Thermophilic Bacteria</div>
     <p class="text-slate-300">Life originated in water ~3.5 billion years ago. Hot springs in <b>Puga Valley, Ladakh</b> mirror early Earth, hosting single-celled thermophilic bacteria. The <b>Birbal Sahni Institute of Palaeosciences</b> studied protective calcium carbonate deposits around such microbes.</p>`,
    `<div class="font-bold text-cyan-300 text-sm">Unicellular vs. Multicellular Hierarchy</div>
     <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
       <div class="p-2 rounded bg-slate-900 border border-slate-800"><b class="text-emerald-300">Unicellular:</b> Bacteria, Yeast (1 cell performs all functions)</div>
       <div class="p-2 rounded bg-slate-900 border border-slate-800"><b class="text-amber-300">Multicellular:</b> Cells → Tissues → Organs → Organ Systems</div>
     </div>`
  ];
  window.c9s2s1Pick = function(i){
    document.getElementById('c9s2s1Out').innerHTML = views[i];
  };
  c9s2s1Pick(0);
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🔬</span> Activity 2.1: Microscope Cell Size Estimator
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Field Diameter:</span><span id="c9s2s2DL" class="text-cyan-300 font-bold">1.6 mm</span></div>
      <input id="c9s2s2D" type="range" min="0.5" max="3.0" step="0.1" value="1.6" oninput="c9s2s2Up()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Cells Across Field:</span><span id="c9s2s2CL" class="text-emerald-300 font-bold">20</span></div>
      <input id="c9s2s2C" type="range" min="5" max="40" step="1" value="20" oninput="c9s2s2Up()" class="w-full accent-emerald-400">
    </label>
  </div>
  <div id="c9s2s2Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs grid grid-cols-2 gap-2"></div>
</div>
<script>
(function(){
  window.c9s2s2Up = function(){
    const mm = parseFloat(document.getElementById('c9s2s2D').value);
    const n = parseInt(document.getElementById('c9s2s2C').value, 10);
    document.getElementById('c9s2s2DL').textContent = mm.toFixed(1) + ' mm';
    document.getElementById('c9s2s2CL').textContent = n;
    const um = Math.round(mm * 1000);
    const size = (um / n).toFixed(1);
    document.getElementById('c9s2s2Out').innerHTML = `
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Field in µm (mm × 1000)</div><div class="text-base font-bold text-cyan-300">${um} µm</div></div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Estimated Cell Size</div><div class="text-base font-bold text-amber-300">${size} µm</div></div>
      <div class="col-span-2 text-slate-400">Eye limit: 0.1 mm (~25 cm) | Hooke (1665): 200–300X | Electron Microscope: nm scale</div>`;
  };
  c9s2s2Up();
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🥔</span> Activity 2.2: Potato Osmosis &amp; Solution Tonicity
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s2s3Mode(0)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Hypotonic (Water)</button>
    <button onclick="c9s2s3Mode(1)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Isotonic (Equal)</button>
    <button onclick="c9s2s3Mode(2)" class="py-2 rounded-xl bg-slate-950 border border-rose-500/40 text-rose-300 font-bold">Hypertonic (20% Salt)</button>
  </div>
  <div id="c9s2s3Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const modes = [
    { t: 'Beaker A: Hypotonic (Plain Water)', col: 'text-cyan-300', res: 'Potato Block SWELLS & Gains Weight (+12%)', desc: 'Outside solute < inside solute. Net water enters potato cells across the 7–10 nm selectively permeable plasma membrane.' },
    { t: 'Isotonic Environment (Equal Concentration)', col: 'text-emerald-300', res: 'No Net Weight Change (0%)', desc: 'Extracellular and intracellular concentrations match. Equal water molecules move in and out continuously.' },
    { t: 'Beaker B: Hypertonic (20% Salt / Sugar)', col: 'text-rose-300', res: 'Potato Block SHRINKS & Loses Weight (-15%)', desc: 'Outside solute > inside solute. Net water exits cells by osmosis, reducing block weight and firmness.' }
  ];
  window.c9s2s3Mode = function(i){
    const m = modes[i];
    document.getElementById('c9s2s3Out').innerHTML = `
      <div class="font-bold text-sm ${m.col}">${m.t}</div>
      <div class="font-bold text-amber-300">${m.res}</div>
      <div class="text-slate-300">${m.desc}</div>`;
  };
  c9s2s3Mode(0);
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🧬</span> Fluid-Mosaic Model Explorer (7–10 nm Membrane)
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s2s4Part(0)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Hydrophilic Heads</button>
    <button onclick="c9s2s4Part(1)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Hydrophobic Tails</button>
    <button onclick="c9s2s4Part(2)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Gatekeeper Proteins</button>
  </div>
  <div id="c9s2s4Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const parts = [
    { t: 'Hydrophilic (Water-Loving) Heads', c: 'text-cyan-300', d: 'Face outward toward the watery exterior and inward toward the watery cytoplasm, stabilizing both membrane surfaces.' },
    { t: 'Hydrophobic (Water-Fearing) Tails', c: 'text-amber-300', d: 'Tuck inward facing each other away from water, forming an oily core that blocks random ions and large polar molecules.' },
    { t: 'Embedded Gatekeeper Proteins', c: 'text-emerald-300', d: 'Span the flexible lipid bilayer as selective channels and pumps, controlling which nutrients enter and wastes exit.' }
  ];
  window.c9s2s4Part = function(i){
    const p = parts[i];
    document.getElementById('c9s2s4Out').innerHTML = `<div class="font-bold text-sm ${p.c}">${p.t}</div><p class="text-slate-300 leading-relaxed">${p.d}</p>`;
  };
  c9s2s4Part(0);
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🧅</span> Activity 2.3: Onion, Rhoeo &amp; Cheek Microscopy
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s2s5Slide(0)" class="py-2 rounded-xl bg-slate-950 border border-rose-500/40 text-rose-300 font-bold">Onion / Rhoeo (Safranin)</button>
    <button onclick="c9s2s5Slide(1)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Cheek Cells (M. Blue)</button>
    <button onclick="c9s2s5Slide(2)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">20% Sugar (Plasmolysis)</button>
  </div>
  <div id="c9s2s5Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const slides = [
    { t: 'Plant Cells: Box-Shaped with Cellulose Cell Wall', c: 'text-rose-300', d: 'Stained with Safranin. Rigid permeable cellulose cell wall protects stationary plants from wind, rain, and bursting. Plain-water slide serves as control.' },
    { t: 'Animal Cheek Cells: Irregular &amp; Flexible', c: 'text-cyan-300', d: 'Stained with Methylene Blue. No cell wall—only the flexible plasma membrane, allowing mobile animals to move and change cell shape.' },
    { t: 'Plasmolysis in 20% Sugar Solution', c: 'text-amber-300', d: 'Water exits by osmosis; the living plasma membrane and cytoplasm shrink away from the rigid outer cellulose cell wall!' }
  ];
  window.c9s2s5Slide = function(i){
    const s = slides[i];
    document.getElementById('c9s2s5Out').innerHTML = `<div class="font-bold text-sm ${s.c}">${s.t}</div><p class="text-slate-300 leading-relaxed">${s.d}</p>`;
  };
  c9s2s5Slide(0);
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🦠</span> Activity 2.4: Prokaryote vs. Eukaryote vs. Acellular
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s2s6Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Prokaryote (1–10 µm)</button>
    <button onclick="c9s2s6Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Eukaryote (10–100 µm)</button>
    <button onclick="c9s2s6Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-rose-500/40 text-rose-300 font-bold">Acellular Agents</button>
  </div>
  <div id="c9s2s6Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Prokaryotic Cell (Bacteria)', c: 'text-amber-300', d: 'Size: 1–10 µm. Primitive nucleoid without a nuclear membrane; no membrane-bound organelles.' },
    { t: 'Eukaryotic Cell (Plant &amp; Animal)', c: 'text-emerald-300', d: 'Size: 10–100 µm. True membrane-bound nucleus, specialized organelles, cytoskeleton fibre network, and non-living inclusions (starch, calcium oxalate, silica crystals).' },
    { t: 'Acellular Infectious Agents (Viruses, Viroids, Prions)', c: 'text-rose-300', d: 'Non-cellular particles lacking cell membranes and independent metabolism; must infect living host cells to replicate.' }
  ];
  window.c9s2s6Pick = function(i){
    const d = items[i];
    document.getElementById('c9s2s6Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s2s6Pick(0);
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🧠</span> Nucleus, Enucleate RBC &amp; Ribosome Explorer
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s2s7Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Nucleus &amp; DNA</button>
    <button onclick="c9s2s7Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-rose-500/40 text-rose-300 font-bold">Enucleate RBCs</button>
    <button onclick="c9s2s7Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Ribosomes</button>
  </div>
  <div id="c9s2s7Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Nucleus: House of Coded Instructions', c: 'text-cyan-300', d: 'Double-layered nuclear membrane with pores; nucleolus assembles ribosomal subunits; chromatin (DNA + proteins) holds genes and condenses into rod chromosomes during division.' },
    { t: 'Threads of Curiosity: Enucleate Human RBCs', c: 'text-rose-300', d: 'Mature human red blood cells lose their nucleus to maximize internal space for hemoglobin oxygen transport, giving them a ~120-day lifespan.' },
    { t: 'Ribosomes: The Protein Factories', c: 'text-emerald-300', d: 'Tiny structures floating free in cytoplasm or attached to Rough ER that translate genetic messages to synthesize proteins.' }
  ];
  window.c9s2s7Pick = function(i){
    const d = items[i];
    document.getElementById('c9s2s7Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s2s7Pick(0);
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>📦</span> Endomembrane Factory: ER &amp; Golgi Apparatus
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s2s8Step(0)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">1. Rough ER (RER)</button>
    <button onclick="c9s2s8Step(1)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">2. Smooth ER (SER)</button>
    <button onclick="c9s2s8Step(2)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">3. Golgi Apparatus</button>
  </div>
  <div id="c9s2s8Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const steps = [
    { t: 'Rough Endoplasmic Reticulum (RER)', c: 'text-cyan-300', d: 'Continuous with the nuclear envelope and studded with ribosomes. Synthesizes and folds proteins for membranes and secretion.' },
    { t: 'Smooth Endoplasmic Reticulum (SER)', c: 'text-amber-300', d: 'Lacks ribosomes. Manufactures cellular lipids and steroid hormones.' },
    { t: 'Golgi Apparatus (Camillo Golgi, 1898)', c: 'text-emerald-300', d: 'Stacks of flattened sacs first observed by Camillo Golgi in barn owl nerve cells (1898). Modifies, sorts, and packages proteins/lipids into vesicles.' }
  ];
  window.c9s2s8Step = function(i){
    const s = steps[i];
    document.getElementById('c9s2s8Out').innerHTML = `<div class="font-bold text-sm ${s.c}">${s.t}</div><p class="text-slate-300 leading-relaxed">${s.d}</p>`;
  };
  c9s2s8Step(0);
})();
</script>
"""
}
