#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Science Chapter 2: Cell: The Building Block of Life
Part 2: Simulators 9 to 16 (Slides 9 to 16)
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>⚡</span> Lysosomes &amp; Mitochondria Powerhouse Lab
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <button onclick="c9s2s9Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-rose-500/40 text-rose-300 font-bold">Lysosomes (Clean-up)</button>
    <button onclick="c9s2s9Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Mitochondria (ATP)</button>
  </div>
  <div id="c9s2s9Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Lysosomes: Clean-up Crew &amp; Sperm Fertilization', c: 'text-rose-300', d: 'Membrane-bound sacs filled with digestive enzymes to break down cellular waste and worn-out organelles. In human sperm cells, lysosomal enzymes help penetrate the egg outer coat during fertilization.' },
    { t: 'Mitochondria: Powerhouse of the Cell', c: 'text-amber-300', d: 'Double-membrane organelle whose folded inner cristae maximize surface area for cellular respiration, producing ATP. Contains its own circular DNA and ribosomes.' }
  ];
  window.c9s2s9Pick = function(i){
    const d = items[i];
    document.getElementById('c9s2s9Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s2s9Pick(0);
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🌿</span> Plastids, Vacuoles &amp; Synthetic DNA Explorer
  </h3>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
    <button onclick="c9s2s10Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Chloroplast</button>
    <button onclick="c9s2s10Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Chromoplast</button>
    <button onclick="c9s2s10Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-slate-500/40 text-slate-200 font-bold">Leucoplast</button>
    <button onclick="c9s2s10Pick(3)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Vacuole</button>
  </div>
  <div id="c9s2s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Chloroplast (Green Chlorophyll)', c: 'text-emerald-300', d: 'Double-membrane plastid with thylakoids and stroma; absorbs sunlight for photosynthesis.' },
    { t: 'Chromoplast (Non-Green Pigments)', c: 'text-amber-300', d: 'Yellow, orange, or red pigments colour flowers and fruits, aiding pollination and seed dispersal. White petals lack chromoplasts.' },
    { t: 'Leucoplast (Colourless Storage)', c: 'text-slate-200', d: 'Colourless plastids in roots and tubers storing starch, oils, or proteins.' },
    { t: 'Vacuole &amp; Venter (2010) Note', c: 'text-cyan-300', d: 'Single-membrane cell-sap sac maintaining turgor pressure in plants to prevent wilting (small/temporary in animals). Also: J. Craig Venter (2010) booted a cell using synthetic bacterial DNA!' }
  ];
  window.c9s2s10Pick = function(i){
    const d = items[i];
    document.getElementById('c9s2s10Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s2s10Pick(0);
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🧪</span> Activity 2.5: Onion Root Tip Squash Protocol
  </h3>
  <div class="grid grid-cols-5 gap-1.5 text-xs">
    <button onclick="c9s2s11Step(0)" class="py-1.5 rounded-lg bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">1. Grow</button>
    <button onclick="c9s2s11Step(1)" class="py-1.5 rounded-lg bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">2. Fix</button>
    <button onclick="c9s2s11Step(2)" class="py-1.5 rounded-lg bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">3. HCl</button>
    <button onclick="c9s2s11Step(3)" class="py-1.5 rounded-lg bg-slate-950 border border-rose-500/40 text-rose-300 font-bold">4. Stain</button>
    <button onclick="c9s2s11Step(4)" class="py-1.5 rounded-lg bg-slate-950 border border-violet-500/40 text-violet-300 font-bold">5. Squash</button>
  </div>
  <div id="c9s2s11Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1"></div>
</div>
<script>
(function(){
  const steps = [
    { t: 'Step 1: Grow Onion Root Tips in Water', d: 'Suspend an onion bulb over water for a few days to sprout fresh, actively dividing root tips.' },
    { t: 'Step 2: Fix in Aceto-Alcohol', d: 'Snip root tips and immerse in aceto-alcohol fixative to halt and preserve cells in their division stages.' },
    { t: 'Step 3: Soften in Warm Dilute HCl', d: 'Gently warm tips in dilute hydrochloric acid to soften cementing layers between plant cell walls.' },
    { t: 'Step 4: Stain with Aceto-Carmine', d: 'Add aceto-carmine stain so condensed chromosomes turn bright crimson under the microscope.' },
    { t: 'Step 5: Squash &amp; Observe Mitosis', d: 'Tap the coverslip gently to spread cells into a single-cell layer and view dividing chromosomes!' }
  ];
  window.c9s2s11Step = function(i){
    const s = steps[i];
    document.getElementById('c9s2s11Out').innerHTML = `<div class="font-bold text-sm text-cyan-300">${s.t}</div><p class="text-slate-300">${s.d}</p>`;
  };
  c9s2s11Step(0);
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🧬</span> Mitosis (2n) vs. Meiosis (n) Calculator
  </h3>
  <label class="block bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-xs">
    <div class="flex justify-between"><span>Parent Cell Chromosomes (2n):</span><span id="c9s2s12NL" class="text-cyan-300 font-bold">46</span></div>
    <input id="c9s2s12N" type="range" min="4" max="48" step="2" value="46" oninput="c9s2s12Up()" class="w-full accent-cyan-400">
  </label>
  <div id="c9s2s12Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs grid grid-cols-2 gap-2"></div>
</div>
<script>
(function(){
  window.c9s2s12Up = function(){
    const n2 = parseInt(document.getElementById('c9s2s12N').value, 10);
    document.getElementById('c9s2s12NL').textContent = n2;
    document.getElementById('c9s2s12Out').innerHTML = `
      <div class="p-2 rounded bg-slate-900 border border-emerald-500/30"><div class="text-emerald-300 font-bold">Mitosis (Somatic)</div><div class="text-slate-200 mt-1">2 identical daughter cells, each with <b>${n2}</b> chromosomes</div></div>
      <div class="p-2 rounded bg-slate-900 border border-amber-500/30"><div class="text-amber-300 font-bold">Meiosis (Gametes)</div><div class="text-slate-200 mt-1">4 gametes, each with <b>${n2 / 2}</b> (n) chromosomes</div></div>
      <div class="col-span-2 text-slate-400">Meet a Scientist: <b>Arun Kumar Sharma</b> pioneered plant chromosome taxonomy and staining techniques!</div>`;
  };
  c9s2s12Up();
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🧫</span> Cell Culture &amp; Division Errors Explorer
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s2s13Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Cell Culture</button>
    <button onclick="c9s2s13Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-rose-500/40 text-rose-300 font-bold">Mitotic Error</button>
    <button onclick="c9s2s13Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Meiotic Error</button>
  </div>
  <div id="c9s2s13Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Sterile Cell Culture Technology', c: 'text-emerald-300', d: 'Growing plant and animal cells outside the body in sterile, nutrient-rich media for biological research, medicine testing, and vaccine production.' },
    { t: 'Errors in Mitosis (Somatic Cells)', c: 'text-rose-300', d: 'Broken division control causes cells to multiply uncontrollably without stopping, forming abnormal tissue masses called tumors.' },
    { t: 'Errors in Meiosis (Reproductive Organs)', c: 'text-amber-300', d: 'Uneven chromosome separation produces gametes with extra or missing chromosomes, leading to genetic disorders, developmental issues, or reduced fertility.' }
  ];
  window.c9s2s13Pick = function(i){
    const d = items[i];
    document.getElementById('c9s2s13Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s2s13Pick(0);
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>📜</span> Cell Theory Timeline &amp; Totipotency
  </h3>
  <div class="grid grid-cols-4 gap-1.5 text-xs">
    <button onclick="c9s2s14Pick(0)" class="py-2 rounded-lg bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">1838</button>
    <button onclick="c9s2s14Pick(1)" class="py-2 rounded-lg bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">1839</button>
    <button onclick="c9s2s14Pick(2)" class="py-2 rounded-lg bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">1855</button>
    <button onclick="c9s2s14Pick(3)" class="py-2 rounded-lg bg-slate-950 border border-violet-500/40 text-violet-300 font-bold">1902</button>
  </div>
  <div id="c9s2s14Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: '1838 — Matthias Schleiden', c: 'text-emerald-300', d: 'Concluded that all plants are composed of cells. Tenet 1: All living organisms are made of one or more cells.' },
    { t: '1839 — Theodor Schwann', c: 'text-cyan-300', d: 'Showed all animals are built from cells. Tenet 2: The cell is the basic unit of structure and function in living beings.' },
    { t: '1855 — Rudolf Virchow', c: 'text-amber-300', d: 'Added Tenet 3: All cells arise from pre-existing cells (never spontaneously from mud).' },
    { t: '1902 — Gottlieb Haberlandt', c: 'text-violet-300', d: 'Austrian botanist who proposed plant cell totipotency, laying the foundation for Plant Tissue Culture Technology.' }
  ];
  window.c9s2s14Pick = function(i){
    const d = items[i];
    document.getElementById('c9s2s14Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s2s14Pick(0);
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>✋</span> Contact Inhibition, Cancer &amp; Apoptosis (PCD)
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s2s15Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Contact Inhibition</button>
    <button onclick="c9s2s15Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-rose-500/40 text-rose-300 font-bold">Cancer Loss</button>
    <button onclick="c9s2s15Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Apoptosis (PCD)</button>
  </div>
  <div id="c9s2s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { t: 'Normal Cells: Contact Inhibition', c: 'text-emerald-300', d: 'Healthy animal cells divide until they touch neighbours on all sides, then stop dividing to keep tissues orderly.' },
    { t: 'Cancer Cells: Lost Growth Control', c: 'text-rose-300', d: 'Cancer cells lose contact inhibition, ignoring neighbour signals and dividing continuously to pile up into tumors.' },
    { t: 'Programmed Cell Death (PCD / Apoptosis)', c: 'text-cyan-300', d: 'Genetically regulated cell removal essential for normal development—for example, removing webbing tissue between embryonic hand digits!' }
  ];
  window.c9s2s15Pick = function(i){
    const d = items[i];
    document.getElementById('c9s2s15Out').innerHTML = `<div class="font-bold text-sm ${d.c}">${d.t}</div><p class="text-slate-300 leading-relaxed">${d.d}</p>`;
  };
  c9s2s15Pick(0);
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🥭</span> Fruit Pickling &amp; Applied Osmosis Simulator
  </h3>
  <label class="block bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-xs">
    <div class="flex justify-between"><span>Salt / Sugar Brine Concentration:</span><span id="c9s2s16SL" class="text-amber-300 font-bold">20%</span></div>
    <input id="c9s2s16S" type="range" min="0" max="25" step="5" value="20" oninput="c9s2s16Up()" class="w-full accent-amber-400">
  </label>
  <div id="c9s2s16Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9s2s16Up = function(){
    const s = parseInt(document.getElementById('c9s2s16S').value, 10);
    document.getElementById('c9s2s16SL').textContent = s + '%';
    let msg = '', col = 'text-emerald-300';
    if(s >= 15){
      msg = 'Hypertonic Preservation: Water exits spoilage microbes by osmosis—bacteria shrink and cannot multiply!';
      col = 'text-emerald-300';
    } else if(s >= 5){
      msg = 'Mild Gradient: Partial slowing, but not hypertonic enough for long-term fruit pickling.';
      col = 'text-amber-300';
    } else {
      msg = 'Hypotonic / Plain Water: Microbes absorb water and thrive; fruit spoils rapidly!';
      col = 'text-rose-300';
    }
    document.getElementById('c9s2s16Out').innerHTML = `
      <div class="font-bold ${col}">${msg}</div>
      <div class="text-slate-400">Also remember: Raw living potato cups show osmosis (boiled ones do not), and iodine turns root leucoplast starch blue-black!</div>`;
  };
  c9s2s16Up();
})();
</script>
"""
}
