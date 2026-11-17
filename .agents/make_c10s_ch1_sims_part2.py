#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 1 Simulators (Part 2: Slides 9-16)
High-fidelity responsive SVG interactive laboratory widgets for Chemical Reactions and Equations.
"""

sims_part2 = {
    9: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Exothermic Reaction:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC10S9('gas')" id="c10s9_btn_gas" class="px-2.5 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition">Methane Combustion</button>
        <button onclick="setC10S9('resp')" id="c10s9_btn_res" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Cellular Respiration</button>
        <button onclick="setC10S9('comp')" id="c10s9_btn_com" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Compost Degradation</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s9_status">CH4 + 2O2 &rarr; CO2 + 2H2O + Thermal Heat</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <g id="c10s9_svg_display"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Reactant Energy</div>
        <div class="text-xs font-bold text-rose-300 mt-0.5" id="c10s9_er">High Chemical Potential</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Thermal Output</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c10s9_eo">+ Heat Released (&Delta;H &lt; 0)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Product State</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c10s9_ep">Lower Stable Energy</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-rose-950 border border-rose-700/60 text-rose-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s9_badge">Exothermic Reaction</span>
    <span id="c10s9_desc">Reactions that release heat energy along with products are classified as exothermic reactions. Natural gas burning, cellular respiration, and composting all discharge thermal energy.</span>
  </div>
</div>
<script>
window.setC10S9 = function(type) {
  ['gas', 'res', 'com'].forEach(b => {
    const el = document.getElementById('c10s9_btn_' + b);
    if(el) {
      if((type === 'gas' && b === 'gas') || (type === 'resp' && b === 'res') || (type === 'comp' && b === 'com')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const disp = document.getElementById('c10s9_svg_display');
  const status = document.getElementById('c10s9_status');
  const er = document.getElementById('c10s9_er');
  const eo = document.getElementById('c10s9_eo');
  const ep = document.getElementById('c10s9_ep');
  const badge = document.getElementById('c10s9_badge');
  const desc = document.getElementById('c10s9_desc');

  if(type === 'gas') {
    status.textContent = "Combustion of Natural Gas: CH4(g) + 2 O2(g) → CO2(g) + 2 H2O(g) + Heat";
    er.textContent = "Methane + 2 O2";
    eo.textContent = "Intense Flame & Heat";
    ep.textContent = "CO2 + 2 H2O (Gases)";
    badge.textContent = "Methane Combustion";
    desc.textContent = "Burning natural gas (methane) releases substantial heat to cook food and heat homes: CH4(g) + 2O2(g) -> CO2(g) + 2H2O(g) + Heat. Product bonds have lower potential energy than reactants.";
    disp.innerHTML = `
      <!-- Potential Energy Curve -->
      <line x1="40" y1="120" x2="420" y2="120" stroke="#475569" stroke-width="1.5"/>
      <line x1="40" y1="120" x2="40" y2="20" stroke="#475569" stroke-width="1.5"/>
      <text x="35" y="15" fill="#94a3b8" font-size="7">Potential Energy</text>
      <!-- Reactant platform -->
      <line x1="50" y1="45" x2="130" y2="45" stroke="#f43f5e" stroke-width="3"/>
      <text x="90" y="38" fill="#fda4af" font-size="8" font-weight="bold" text-anchor="middle">CH4 + 2O2</text>
      <!-- Activation hump & drop -->
      <path d="M 130,45 Q 170,20 200,30 T 260,95 L 340,95" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
      <!-- Product platform -->
      <line x1="260" y1="95" x2="350" y2="95" stroke="#10b981" stroke-width="3"/>
      <text x="305" y="112" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">CO2 + 2H2O</text>
      <!-- Heat delta arrow -->
      <line x1="375" y1="45" x2="375" y2="95" stroke="#ef4444" stroke-width="2"/>
      <text x="410" y="72" fill="#fca5a5" font-size="8" font-weight="bold" text-anchor="middle">&Delta;H &lt; 0 (Heat)</text>
    `;
  } else if(type === 'resp') {
    status.textContent = "Cellular Respiration: C6H12O6(aq) + 6 O2(aq) → 6 CO2 + 6 H2O + ATP Energy";
    er.textContent = "Glucose + 6 O2";
    eo.textContent = "Body Warmth & ATP";
    ep.textContent = "6 CO2 + 6 H2O";
    badge.textContent = "Cellular Respiration";
    desc.textContent = "In human cells, glucose from digested food combines with inhaled oxygen: C6H12O6 + 6O2 -> 6CO2 + 6H2O + Energy. This exothermic biochemical oxidation sustains living body temperature at 37 °C.";
    disp.innerHTML = `
      <rect x="40" y="35" width="130" height="75" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
      <text x="105" y="58" fill="#c7d2fe" font-size="8" font-weight="bold" text-anchor="middle">Mitochondria Reactants</text>
      <text x="105" y="75" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">C6H12O6 + 6 O2</text>
      <text x="105" y="95" fill="#a5b4fc" font-size="7" text-anchor="middle">High Biochemical Energy</text>
      <!-- Arrow with energy burst -->
      <path d="M 180,72 L 240,72" stroke="#f59e0b" stroke-width="3"/>
      <circle cx="210" cy="72" r="14" fill="#ea580c"/>
      <text x="210" y="75" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">ATP</text>
      <rect x="250" y="35" width="170" height="75" rx="6" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
      <text x="335" y="58" fill="#a7f3d0" font-size="8" font-weight="bold" text-anchor="middle">Exothermic Products</text>
      <text x="335" y="75" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">6 CO2 + 6 H2O + Energy</text>
      <text x="335" y="95" fill="#fde047" font-size="7" font-weight="bold" text-anchor="middle">Maintains 37&deg;C Body Temperature</text>
    `;
  } else {
    status.textContent = "Composting: Organic Matter → Microbial Compost + Heat (50-65 °C)";
    er.textContent = "Vegetable Matter";
    eo.textContent = "50-65&deg;C Pile Heat";
    ep.textContent = "Nutrient-Rich Humus";
    badge.textContent = "Compost Degradation";
    desc.textContent = "Microbes enzymatically break chemical bonds in vegetable peelings and agricultural biomass, releasing biological heat in an exothermic decomposition that elevates compost pile temperatures to 60 °C.";
    disp.innerHTML = `
      <rect x="40" y="35" width="130" height="75" rx="6" fill="#14532d" stroke="#22c55e" stroke-width="1.5"/>
      <text x="105" y="60" fill="#dcfce7" font-size="8" font-weight="bold" text-anchor="middle">Vegetable Peelings</text>
      <text x="105" y="80" fill="#86efac" font-size="7" text-anchor="middle">Complex Starch &amp; Cellulose</text>
      <path d="M 180,72 L 250,72" stroke="#f59e0b" stroke-width="3"/>
      <text x="215" y="62" fill="#fde047" font-size="7" font-weight="bold" text-anchor="middle">Microbes</text>
      <rect x="260" y="35" width="160" height="75" rx="6" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="340" y="58" fill="#fef3c7" font-size="8" font-weight="bold" text-anchor="middle">Organic Compost</text>
      <text x="340" y="75" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Humus + Mineral Nutrients</text>
      <text x="340" y="95" fill="#ef4444" font-size="8" font-weight="bold" text-anchor="middle">Generates 50-65&deg;C Heat!</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S9('gas'));
</script>""",

    10: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Thermal Reaction:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC10S10('lead')" id="c10s10_btn_lea" class="px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">Lead Nitrate (NO2 Fumes)</button>
        <button onclick="setC10S10('iron')" id="c10s10_btn_iro" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Ferrous Sulphate (SO2/SO3)</button>
        <button onclick="setC10S10('lime')" id="c10s10_btn_lim" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Limestone (Cement CaO)</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s10_status">Activity 1.6: 2Pb(NO3)2 &rarr; 2PbO + 4NO2&uarr; + O2&uarr;</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Test tube on clamp stand -->
        <g id="c10s10_tube_graphics"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Reactant Species</div>
        <div class="text-xs font-bold text-slate-200 mt-0.5" id="c10s10_r1">Lead Nitrate (White)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Evolved Gas</div>
        <div class="text-xs font-bold text-amber-400 mt-0.5" id="c10s10_r2">Brown NO2 + O2</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Solid Residue</div>
        <div class="text-xs font-bold text-yellow-300 mt-0.5" id="c10s10_r3">Lead Oxide (Yellow PbO)</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-amber-950 border border-amber-700/60 text-amber-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s10_badge">Thermal Cleavage</span>
    <span id="c10s10_desc">When decomposition is carried out by heating, it is termed thermal decomposition. Heating lead nitrate produces pungent brown nitrogen dioxide fumes and a yellow residue of lead oxide.</span>
  </div>
</div>
<script>
window.setC10S10 = function(mode) {
  ['lea', 'iro', 'lim'].forEach(b => {
    const el = document.getElementById('c10s10_btn_' + b);
    if(el) {
      if((mode === 'lead' && b === 'lea') || (mode === 'iron' && b === 'iro') || (mode === 'lime' && b === 'lim')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const tube = document.getElementById('c10s10_tube_graphics');
  const status = document.getElementById('c10s10_status');
  const r1 = document.getElementById('c10s10_r1');
  const r2 = document.getElementById('c10s10_r2');
  const r3 = document.getElementById('c10s10_r3');
  const badge = document.getElementById('c10s10_badge');
  const desc = document.getElementById('c10s10_desc');

  if(mode === 'lead') {
    status.textContent = "Activity 1.6: 2 Pb(NO3)2(s) → 2 PbO(s) [Yellow] + 4 NO2(g) [Brown] + O2(g)";
    r1.textContent = "White Lead Nitrate";
    r2.textContent = "Dense Brown NO2 Fumes";
    r3.textContent = "Yellow PbO Residue";
    badge.textContent = "Activity 1.6 (Lead Nitrate)";
    desc.textContent = "Heating white lead nitrate powder produces crackling decrepitation. Dense, pungent reddish-brown fumes of nitrogen dioxide gas billow out, leaving a yellow residue of lead monoxide (PbO).";
    tube.innerHTML = `
      <!-- Boiling tube slanted -->
      <polygon points="120,50 140,55 90,120 70,115" fill="#1e293b" stroke="#cbd5e1" stroke-width="1.5"/>
      <circle cx="80" cy="118" r="8" fill="#facc15"/>
      <text x="65" y="135" fill="#fde047" font-size="7" font-weight="bold">Yellow PbO Residue</text>
      <!-- Burner flame under bottom -->
      <polygon points="75,135 70,125 80,125" fill="#ef4444"/>
      <!-- Brown Fumes billowing out -->
      <ellipse cx="140" cy="38" rx="16" ry="10" fill="#92400e" opacity="0.8"/>
      <ellipse cx="165" cy="30" rx="22" ry="14" fill="#78350f" opacity="0.85"/>
      <ellipse cx="195" cy="22" rx="26" ry="16" fill="#451a03" opacity="0.75"/>
      <text x="175" y="34" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">Brown NO2 Fumes &uarr;</text>
      <!-- Callout Equation -->
      <rect x="235" y="25" width="205" height="95" rx="8" fill="#1c1917" stroke="#b45309" stroke-width="1.5"/>
      <text x="337" y="48" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">2 Pb(NO3)2 &rarr; 2 PbO + 4 NO2 + O2</text>
      <text x="337" y="68" fill="#cbd5e1" font-size="7" text-anchor="middle">Thermal Cleavage: 1 Reactant &rarr; 3 Products</text>
      <text x="337" y="84" fill="#f87171" font-size="7" text-anchor="middle">Pungent NO2 gas + Oxygen gas</text>
      <text x="337" y="102" fill="#4ade80" font-size="7" font-weight="bold" text-anchor="middle">Endothermic Heat-Driven Reaction</text>
    `;
  } else if(mode === 'iron') {
    status.textContent = "Activity 1.5: 2 FeSO4(s) → Fe2O3(s) [Red-Brown] + SO2(g) + SO3(g) [Sulphur Odour]";
    r1.textContent = "Green FeSO4·7H2O Crystals";
    r2.textContent = "Pungent SO2 + SO3 Gases";
    r3.textContent = "Reddish-Brown Fe2O3";
    badge.textContent = "Activity 1.5 (Ferrous Sulphate)";
    desc.textContent = "Green ferrous sulphate crystals first lose water of crystallization to turn white. Further strong heating decomposes anhydrous FeSO4 into solid ferric oxide and gases smelling of burning sulphur (SO2 & SO3).";
    tube.innerHTML = `
      <polygon points="120,50 140,55 90,120 70,115" fill="#1e293b" stroke="#cbd5e1" stroke-width="1.5"/>
      <circle cx="80" cy="118" r="8" fill="#7f1d1d"/>
      <text x="65" y="135" fill="#fca5a5" font-size="7" font-weight="bold">Fe2O3 Red-Brown</text>
      <!-- Choking fumes -->
      <ellipse cx="145" cy="35" rx="18" ry="10" fill="#64748b" opacity="0.7"/>
      <ellipse cx="175" cy="25" rx="22" ry="12" fill="#475569" opacity="0.6"/>
      <text x="160" y="30" fill="#fde047" font-size="7" font-weight="bold">SO2 + SO3 Gases</text>
      <rect x="235" y="25" width="205" height="95" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
      <text x="337" y="48" fill="#e0e7ff" font-size="8" font-weight="bold" text-anchor="middle">2 FeSO4 &rarr; Fe2O3 + SO2 + SO3</text>
      <text x="337" y="68" fill="#cbd5e1" font-size="7" text-anchor="middle">Green crystals &rarr; White anhydrous &rarr; Red-brown</text>
      <text x="337" y="84" fill="#bae6fd" font-size="7" text-anchor="middle">Burning sulphur match odour (SO2/SO3)</text>
      <text x="337" y="102" fill="#4ade80" font-size="7" font-weight="bold" text-anchor="middle">Industrial Sulphuric Acid Precursor</text>
    `;
  } else {
    status.textContent = "Limestone Decomposition: CaCO3(s) → CaO(s) [Quicklime] + CO2(g)";
    r1.textContent = "Limestone: CaCO3";
    r2.textContent = "Carbon Dioxide Gas";
    r3.textContent = "Quicklime for Cement (CaO)";
    badge.textContent = "Cement Manufacturing";
    desc.textContent = "Heating limestone (calcium carbonate) produces calcium oxide (quicklime) and carbon dioxide: CaCO3 -> CaO + CO2. Quicklime is the indispensable binder used in global cement manufacturing.";
    tube.innerHTML = `
      <rect x="50" y="40" width="100" height="70" rx="8" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
      <text x="100" y="70" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">CaCO3 (Limestone)</text>
      <text x="100" y="88" fill="#fde047" font-size="8" text-anchor="middle">+ 1000&deg;C Kiln Heat</text>
      <path d="M 165,75 L 225,75" stroke="#f59e0b" stroke-width="3"/>
      <rect x="240" y="30" width="195" height="90" rx="8" fill="#065f46" stroke="#10b981" stroke-width="2"/>
      <text x="337" y="55" fill="#a7f3d0" font-size="9" font-weight="bold" text-anchor="middle">CaO (Quicklime) + CO2 &uarr;</text>
      <text x="337" y="75" fill="#ffffff" font-size="8" text-anchor="middle">Essential Raw Material for Cement</text>
      <text x="337" y="95" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Thermal Decomposition Powers Construction</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S10('lead'));
</script>""",

    11: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-sky-400 uppercase tracking-wider">Electrolysis State:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC10S11('run')" id="c10s11_btn_run" class="px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition">6V Current ON (Bubbles)</button>
        <button onclick="setC10S11('test')" id="c10s11_btn_tes" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Splinter Test (Pop vs Flame)</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s11_status">Activity 1.7: 2H2O(l) &rarr; 2H2(g) [Cathode] + O2(g) [Anode] (2:1 Volume)</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Plastic Mug Container -->
        <rect x="130" y="25" width="200" height="95" rx="6" fill="#1e293b" stroke="#475569" stroke-width="2"/>
        <rect x="132" y="45" width="196" height="73" fill="#0284c7" opacity="0.3"/>

        <!-- 6V Battery underneath -->
        <rect x="190" y="125" width="80" height="16" rx="3" fill="#0f172a" stroke="#f59e0b"/>
        <text x="230" y="136" fill="#fde047" font-size="7" font-weight="bold" text-anchor="middle">6V DC Battery</text>

        <!-- Cathode (-) on Left: H2 -->
        <!-- Inverted tube -->
        <rect x="165" y="30" width="30" height="75" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
        <rect x="175" y="60" width="10" height="45" fill="#334155"/>
        <text x="180" y="118" fill="#38bdf8" font-size="7" font-weight="bold" text-anchor="middle">Cathode (-)</text>

        <!-- Anode (+) on Right: O2 -->
        <rect x="265" y="30" width="30" height="75" rx="4" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
        <rect x="275" y="60" width="10" height="45" fill="#334155"/>
        <text x="280" y="118" fill="#f87171" font-size="7" font-weight="bold" text-anchor="middle">Anode (+)</text>

        <!-- Dynamic Gas volumes & bubbles -->
        <g id="c10s11_dynamic"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Cathode Volume (H2)</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c10s11_h2">20 mL (2 Volumes)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Volume Ratio (H2 : O2)</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5">2 : 1 Ratio (H2O)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Anode Volume (O2)</div>
        <div class="text-xs font-bold text-rose-300 mt-0.5" id="c10s11_o2">10 mL (1 Volume)</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-sky-950 border border-sky-700/60 text-sky-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s11_badge">Electrolysis</span>
    <span id="c10s11_desc">Electric current cleaves liquid water into hydrogen gas at the cathode and oxygen gas at the anode in a 2:1 volume ratio, proving water contains two hydrogen atoms for every one oxygen atom.</span>
  </div>
</div>
<script>
window.setC10S11 = function(mode) {
  const btnR = document.getElementById('c10s11_btn_run');
  const btnT = document.getElementById('c10s11_btn_tes');
  const dyn = document.getElementById('c10s11_dynamic');
  const status = document.getElementById('c10s11_status');
  const badge = document.getElementById('c10s11_badge');
  const desc = document.getElementById('c10s11_desc');

  if(mode === 'run') {
    btnR.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition';
    btnT.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    status.textContent = "Activity 1.7: 6V DC Current Flowing • H2 (Double Volume) & O2 Bubbles Forming";
    badge.textContent = "Electrolysis In Action";
    desc.textContent = "Dilute sulphuric acid provides conductive ions. Hydrogen gas displaces twice as much water at the cathode as oxygen does at the anode, confirming the chemical formula H2O.";
    dyn.innerHTML = `
      <!-- Gas space at top of cathode tube (Double volume: 40px) -->
      <rect x="166" y="31" width="28" height="40" fill="#0284c7" opacity="0.6"/>
      <text x="180" y="55" fill="#f8fafc" font-size="8" font-weight="bold" text-anchor="middle">2x H2</text>
      <!-- Bubbles rising at cathode -->
      <circle cx="178" cy="78" r="2" fill="#ffffff"/>
      <circle cx="182" cy="85" r="2.5" fill="#ffffff"/>
      <circle cx="177" cy="95" r="2" fill="#ffffff"/>

      <!-- Gas space at top of anode tube (Single volume: 20px) -->
      <rect x="266" y="31" width="28" height="20" fill="#b91c1c" opacity="0.6"/>
      <text x="280" y="44" fill="#f8fafc" font-size="8" font-weight="bold" text-anchor="middle">1x O2</text>
      <!-- Bubbles rising at anode -->
      <circle cx="278" cy="68" r="2" fill="#ffffff"/>
      <circle cx="282" cy="80" r="2" fill="#ffffff"/>

      <text x="50" y="65" fill="#38bdf8" font-size="8" font-weight="bold">Cathode Gas (2 Vol)</text>
      <text x="410" y="65" fill="#f87171" font-size="8" font-weight="bold" text-anchor="end">Anode Gas (1 Vol)</text>
    `;
  } else {
    btnR.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    btnT.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
    status.textContent = "Gas Identification: Cathode H2 burns with 'Pop' sound; Anode O2 rekindles flame";
    badge.textContent = "Splinter Test";
    desc.textContent = "Bringing a burning candle near the cathode tube produces a sharp 'pop' sound as hydrogen burns. Bringing a glowing splinter near the anode tube rekindles it into a bright flame, confirming oxygen.";
    dyn.innerHTML = `
      <rect x="166" y="31" width="28" height="40" fill="#0284c7" opacity="0.8"/>
      <rect x="266" y="31" width="28" height="20" fill="#b91c1c" opacity="0.8"/>
      <!-- Splinter on left: POP -->
      <circle cx="180" cy="20" r="10" fill="#facc15" filter="drop-shadow(0 0 6px #f59e0b)"/>
      <text x="180" y="23" fill="#0f172a" font-size="7" font-weight="bold" text-anchor="middle">POP!</text>
      <!-- Splinter on right: Rekindled flame -->
      <polygon points="280,5 274,25 286,25" fill="#f97316"/>
      <text x="280" y="2" fill="#fdba74" font-size="7" font-weight="bold" text-anchor="middle">Rekindles!</text>
      <text x="230" y="70" fill="#4ade80" font-size="9" font-weight="bold" text-anchor="middle">2:1 Volume Stoichiometry Proved</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S11('run'));
</script>""",

    12: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Photolysis System:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC10S12('agcl')" id="c10s12_btn_cl" class="px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">Silver Chloride (AgCl)</button>
        <button onclick="setC10S12('agbr')" id="c10s12_btn_br" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Silver Bromide (B&amp;W Photo)</button>
        <button onclick="setC10S12('endo')" id="c10s12_btn_end" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Endothermic Concept</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s12_status">Activity 1.8: 2AgCl(s) --[Sunlight]--> 2Ag(s) [Grey] + Cl2(g)</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Sun with beams -->
        <circle cx="50" cy="30" r="18" fill="#f59e0b" filter="drop-shadow(0 0 8px #f59e0b)"/>
        <line x1="68" y1="35" x2="180" y2="95" stroke="#fde047" stroke-width="2" stroke-dasharray="3,2"/>
        <line x1="60" y1="48" x2="170" y2="105" stroke="#fde047" stroke-width="2" stroke-dasharray="3,2"/>
        <text x="50" y="60" fill="#fde68a" font-size="7" font-weight="bold" text-anchor="middle">Sunlight (h&nu;)</text>

        <!-- China Dish -->
        <ellipse cx="200" cy="115" rx="55" ry="15" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
        <text x="200" y="138" fill="#94a3b8" font-size="7" text-anchor="middle">China Dish</text>

        <g id="c10s12_active_dish"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Reactant Solid</div>
        <div class="text-xs font-bold text-slate-200 mt-0.5" id="c10s12_v1">Silver Chloride (White)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Energy Absorbed</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c10s12_v2">Solar Photons (Light)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Photolytic Product</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c10s12_v3">Grey Silver Metal + Cl2</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-amber-950 border border-amber-700/60 text-amber-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s12_badge">Photolysis</span>
    <span id="c10s12_desc">Photolytic decomposition occurs when light photons break chemical bonds. White silver chloride turns grey in sunlight as metallic silver is formed, releasing chlorine gas.</span>
  </div>
</div>
<script>
window.setC10S12 = function(mode) {
  ['cl', 'br', 'end'].forEach(b => {
    const el = document.getElementById('c10s12_btn_' + b);
    if(el) {
      if((mode === 'agcl' && b === 'cl') || (mode === 'agbr' && b === 'br') || (mode === 'endo' && b === 'end')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const dish = document.getElementById('c10s12_active_dish');
  const status = document.getElementById('c10s12_status');
  const v1 = document.getElementById('c10s12_v1');
  const v2 = document.getElementById('c10s12_v2');
  const v3 = document.getElementById('c10s12_v3');
  const badge = document.getElementById('c10s12_badge');
  const desc = document.getElementById('c10s12_desc');

  if(mode === 'agcl') {
    status.textContent = "Activity 1.8: 2 AgCl(s) [White] --[Sunlight]--> 2 Ag(s) [Grey] + Cl2(g)";
    v1.textContent = "White AgCl Crystals";
    v2.textContent = "Solar Photons (hν)";
    v3.textContent = "Grey Silver Metal Powder";
    badge.textContent = "Silver Chloride Photolysis";
    desc.textContent = "When white silver chloride crystals are exposed to sunlight in a china dish, radiant photons cleave the ionic bond: 2AgCl -> 2Ag + Cl2. Chlorine gas escapes, leaving grey elemental silver.";
    dish.innerHTML = `
      <!-- Crystals turning grey -->
      <ellipse cx="200" cy="112" rx="35" ry="8" fill="#94a3b8"/>
      <circle cx="185" cy="110" r="3" fill="#cbd5e1"/>
      <circle cx="210" cy="112" r="4" fill="#64748b"/>
      <text x="200" y="98" fill="#e2e8f0" font-size="8" font-weight="bold" text-anchor="middle">Grey Silver (Ag) Metal</text>
      <!-- Cl2 gas rising -->
      <path d="M 235,95 Q 245,70 260,55" stroke="#a3e635" stroke-width="2" stroke-dasharray="3,3" fill="none"/>
      <text x="280" y="55" fill="#bef264" font-size="7" font-weight="bold">Cl2 Gas Escapes &uarr;</text>
      <!-- Equation box -->
      <rect x="290" y="25" width="155" height="80" rx="6" fill="#1c1917" stroke="#eab308" stroke-width="1.5"/>
      <text x="367" y="48" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">2 AgCl &rarr; 2 Ag + Cl2</text>
      <text x="367" y="68" fill="#cbd5e1" font-size="7" text-anchor="middle">White &rarr; Lustrous Grey</text>
      <text x="367" y="85" fill="#4ade80" font-size="7" font-weight="bold" text-anchor="middle">Light-Activated Photolysis</text>
    `;
  } else if(mode === 'agbr') {
    status.textContent = "Silver Bromide: 2 AgBr(s) --[Light]--> 2 Ag(s) + Br2(g) (Black-and-White Photography)";
    v1.textContent = "Pale Yellow AgBr";
    v2.textContent = "Photographic Exposure";
    v3.textContent = "Metallic Silver Image";
    badge.textContent = "B&W Photography";
    desc.textContent = "Pale yellow silver bromide crystals decompose under light into metallic silver: 2AgBr -> 2Ag + Br2. This light-sensitive photochemical reaction served as the foundation of photography for over a century.";
    dish.innerHTML = `
      <ellipse cx="200" cy="112" rx="35" ry="8" fill="#475569"/>
      <text x="200" y="98" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">Metallic Silver Image</text>
      <!-- Br2 gas -->
      <path d="M 235,95 Q 245,70 260,55" stroke="#f97316" stroke-width="2" stroke-dasharray="3,3" fill="none"/>
      <text x="280" y="55" fill="#fdba74" font-size="7" font-weight="bold">Br2 Gas &uarr;</text>
      <rect x="290" y="25" width="155" height="80" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
      <text x="367" y="48" fill="#c7d2fe" font-size="8" font-weight="bold" text-anchor="middle">2 AgBr &rarr; 2 Ag + Br2</text>
      <text x="367" y="68" fill="#cbd5e1" font-size="7" text-anchor="middle">Historic B&amp;W Photography</text>
      <text x="367" y="85" fill="#38bdf8" font-size="7" font-weight="bold" text-anchor="middle">Light-Sensitive Film Emulsion</text>
    `;
  } else {
    status.textContent = "All Decomposition Reactions Require Energy Input (Heat, Light, Electricity) = Endothermic";
    v1.textContent = "Stable Single Reactant";
    v2.textContent = "Requires Energy (+ &Delta;H)";
    v3.textContent = "Multiple Simpler Fragments";
    badge.textContent = "Endothermic Core";
    desc.textContent = "Because breaking chemical bonds requires energy input—whether in the form of thermal heat, electric current, or radiant light photons—decomposition reactions are fundamentally endothermic.";
    dish.innerHTML = `
      <rect x="140" y="25" width="180" height="95" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="230" y="48" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">3 Energy Drivers of Cleavage</text>
      <text x="230" y="68" fill="#fde047" font-size="8" text-anchor="middle">1. Heat: Thermal (CaCO3, FeSO4)</text>
      <text x="230" y="84" fill="#a7f3d0" font-size="8" text-anchor="middle">2. Electricity: Electrolysis (H2O)</text>
      <text x="230" y="100" fill="#fda4af" font-size="8" text-anchor="middle">3. Light: Photolysis (AgCl, AgBr)</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S12('agcl'));
</script>""",

    13: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-sky-400 uppercase tracking-wider">Metal Tested:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC10S13('iron')" id="c10s13_btn_iro" class="px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition">Iron in CuSO4 (Activity 1.9)</button>
        <button onclick="setC10S13('zinc')" id="c10s13_btn_zin" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Zinc in CuSO4</button>
        <button onclick="setC10S13('copper')" id="c10s13_btn_cop" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Copper in FeSO4 (No Reaction)</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s13_status">Fe(s) + CuSO4(aq) [Blue] &rarr; FeSO4(aq) [Pale Green] + Cu(s) [Brown Coating]</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Test tube container -->
        <g id="c10s13_tube_canvas"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Solution Colour Shift</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c10s13_col">Deep Blue &rarr; Pale Green</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Metal Nail Coating</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c10s13_coat">Reddish-Brown Copper</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Reactivity Comparison</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c10s13_react">Fe &gt; Cu (Displaces)</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-sky-950 border border-sky-700/60 text-sky-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s13_badge">Single Displacement</span>
    <span id="c10s13_desc">In a displacement reaction, a more reactive element expels a less reactive element from its compound. Iron is more reactive than copper, displacing copper from blue CuSO4 solution into pale green FeSO4.</span>
  </div>
</div>
<script>
window.setC10S13 = function(metal) {
  ['iro', 'zin', 'cop'].forEach(b => {
    const el = document.getElementById('c10s13_btn_' + b);
    if(el) {
      if((metal === 'iron' && b === 'iro') || (metal === 'zinc' && b === 'zin') || (metal === 'copper' && b === 'cop')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const canvas = document.getElementById('c10s13_tube_canvas');
  const status = document.getElementById('c10s13_status');
  const col = document.getElementById('c10s13_col');
  const coat = document.getElementById('c10s13_coat');
  const react = document.getElementById('c10s13_react');
  const badge = document.getElementById('c10s13_badge');
  const desc = document.getElementById('c10s13_desc');

  if(metal === 'iron') {
    status.textContent = "Activity 1.9: Fe(s) + CuSO4(aq) [Blue] → FeSO4(aq) [Pale Green] + Cu(s) [Brown Deposit]";
    col.textContent = "Blue → Pale Green (FeSO4)";
    coat.textContent = "Reddish-Brown Copper Coat";
    react.textContent = "Iron > Copper (Displaces)";
    badge.textContent = "Activity 1.9 (Iron & CuSO4)";
    desc.textContent = "Clean iron nails dipped into blue copper sulphate displace copper ions over 20 minutes: Fe + CuSO4 -> FeSO4 + Cu. The solution fades to pale green ferrous sulphate, while brown copper plates onto the nail.";
    canvas.innerHTML = `
      <!-- Before Test tube: Blue -->
      <rect x="50" y="25" width="30" height="90" rx="12" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
      <rect x="52" y="55" width="26" height="58" fill="#0284c7" opacity="0.8"/>
      <!-- Grey Nail inside -->
      <line x1="65" y1="40" x2="65" y2="105" stroke="#94a3b8" stroke-width="5"/>
      <text x="65" y="130" fill="#38bdf8" font-size="7" font-weight="bold" text-anchor="middle">Start: Blue CuSO4</text>
      <!-- Arrow -->
      <path d="M 105,70 L 165,70" stroke="#f59e0b" stroke-width="3"/>
      <text x="135" y="60" fill="#fde047" font-size="7" text-anchor="middle">20 Mins</text>
      <!-- After Test tube: Pale Green -->
      <rect x="185" y="25" width="30" height="90" rx="12" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
      <rect x="187" y="55" width="26" height="58" fill="#86efac" opacity="0.6"/>
      <!-- Brown coated Nail -->
      <line x1="200" y1="40" x2="200" y2="105" stroke="#b45309" stroke-width="6"/>
      <text x="200" y="130" fill="#86efac" font-size="7" font-weight="bold" text-anchor="middle">End: Pale Green</text>
      <!-- Callout box -->
      <rect x="235" y="25" width="205" height="95" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
      <text x="337" y="48" fill="#ecfdf5" font-size="8" font-weight="bold" text-anchor="middle">Fe + CuSO4 &rarr; FeSO4 + Cu</text>
      <text x="337" y="68" fill="#a7f3d0" font-size="7" text-anchor="middle">Iron is more reactive than Copper</text>
      <text x="337" y="85" fill="#fde68a" font-size="7" text-anchor="middle">Reddish-brown copper coats the nail</text>
      <text x="337" y="103" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Blue Cu(2+) ions reduced to metallic Cu</text>
    `;
  } else if(metal === 'zinc') {
    status.textContent = "Zinc in CuSO4: Zn(s) + CuSO4(aq) [Blue] → ZnSO4(aq) [Colourless] + Cu(s) [Spongy Brown]";
    col.textContent = "Blue → Colourless (ZnSO4)";
    coat.textContent = "Spongy Copper Deposit";
    react.textContent = "Zinc > Copper (Displaces)";
    badge.textContent = "Zinc Displacement";
    desc.textContent = "Zinc strips react rapidly with copper sulphate solution: Zn + CuSO4 -> ZnSO4 + Cu. The blue solution turns completely colourless as zinc sulphate forms, depositing spongy metallic copper.";
    canvas.innerHTML = `
      <rect x="70" y="30" width="35" height="85" rx="12" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
      <rect x="72" y="60" width="31" height="52" fill="#f8fafc" opacity="0.2"/>
      <line x1="87" y1="45" x2="87" y2="105" stroke="#b45309" stroke-width="5"/>
      <text x="87" y="130" fill="#cbd5e1" font-size="7" text-anchor="middle">Colourless ZnSO4</text>
      <rect x="145" y="25" width="290" height="95" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
      <text x="290" y="50" fill="#e0e7ff" font-size="9" font-weight="bold" text-anchor="middle">Zn(s) + CuSO4(aq) &rarr; ZnSO4(aq) + Cu(s)</text>
      <text x="290" y="70" fill="#bae6fd" font-size="8" text-anchor="middle">Zinc is much more reactive than copper</text>
      <text x="290" y="90" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Reactivity Order: Zn &gt; Fe &gt; Pb &gt; Cu</text>
    `;
  } else {
    status.textContent = "Copper in FeSO4: Cu(s) + FeSO4(aq) → NO REACTION (Copper is less reactive than Iron)";
    col.textContent = "Pale Green Unchanged";
    coat.textContent = "No Coating (Zero Reaction)";
    react.textContent = "Cu < Fe (Cannot Displace)";
    badge.textContent = "No Reaction";
    desc.textContent = "Immersing a copper wire into pale green ferrous sulphate solution produces no change whatsoever. Copper is less reactive than iron and lacks the electron potential to displace iron from its salt.";
    canvas.innerHTML = `
      <rect x="70" y="30" width="35" height="85" rx="12" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
      <rect x="72" y="60" width="31" height="52" fill="#86efac" opacity="0.6"/>
      <line x1="87" y1="45" x2="87" y2="105" stroke="#b45309" stroke-width="4"/>
      <text x="87" y="130" fill="#86efac" font-size="7" text-anchor="middle">Remains Green</text>
      <rect x="145" y="25" width="290" height="95" rx="8" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
      <text x="290" y="50" fill="#fee2e2" font-size="9" font-weight="bold" text-anchor="middle">Cu(s) + FeSO4(aq) &rarr; NO REACTION</text>
      <text x="290" y="70" fill="#fca5a5" font-size="8" text-anchor="middle">Copper is lower than Iron on the Activity Series</text>
      <text x="290" y="90" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Less reactive metals cannot displace more reactive metals!</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S13('iron'));
</script>""",

    14: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Double Displacement:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC10S14('baso4')" id="c10s14_btn_ba" class="px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition">Na2SO4 + BaCl2 (White BaSO4)</button>
        <button onclick="setC10S14('pbi2')" id="c10s14_btn_pb" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Pb(NO3)2 + 2KI (Yellow PbI2)</button>
        <button onclick="setC10S14('matrix')" id="c10s14_btn_mx" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Ion Exchange Pattern</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s14_status">Activity 1.10: Na2SO4(aq) + BaCl2(aq) &rarr; BaSO4(s)&darr; + 2NaCl(aq)</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <g id="c10s14_svg_canvas"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Reactant Solutions</div>
        <div class="text-xs font-bold text-slate-200 mt-0.5" id="c10s14_d1">2 Clear Aqueous Salts</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Precipitate Formed</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c10s14_d2">White BaSO4 Solid &darr;</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Reaction Classification</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c10s14_d3">Double Displacement</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-emerald-950 border border-emerald-700/60 text-emerald-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s14_badge">Precipitation</span>
    <span id="c10s14_desc">In double displacement reactions, mutual exchange of ions between two aqueous compounds yields an insoluble precipitate. Barium ions bond with sulphate ions to precipitate white barium sulphate.</span>
  </div>
</div>
<script>
window.setC10S14 = function(mode) {
  ['ba', 'pb', 'mx'].forEach(b => {
    const el = document.getElementById('c10s14_btn_' + b);
    if(el) {
      if((mode === 'baso4' && b === 'ba') || (mode === 'pbi2' && b === 'pb') || (mode === 'matrix' && b === 'mx')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const canvas = document.getElementById('c10s14_svg_canvas');
  const status = document.getElementById('c10s14_status');
  const d1 = document.getElementById('c10s14_d1');
  const d2 = document.getElementById('c10s14_d2');
  const d3 = document.getElementById('c10s14_d3');
  const badge = document.getElementById('c10s14_badge');
  const desc = document.getElementById('c10s14_desc');

  if(mode === 'baso4') {
    status.textContent = "Activity 1.10: Na2SO4(aq) + BaCl2(aq) → BaSO4(s)↓ [White Precipitate] + 2 NaCl(aq)";
    d1.textContent = "Na2SO4 + BaCl2";
    d2.textContent = "White BaSO4 Solid";
    d3.textContent = "Double Displacement";
    badge.textContent = "Activity 1.10 (Barium Sulphate)";
    desc.textContent = "Mixing aqueous sodium sulphate with barium chloride causes instant double displacement: Na2SO4 + BaCl2 -> BaSO4 + 2NaCl. Insoluble white barium sulphate precipitates while NaCl stays dissolved.";
    canvas.innerHTML = `
      <!-- Beaker mixing -->
      <rect x="70" y="30" width="80" height="85" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
      <rect x="72" y="65" width="76" height="48" fill="#f8fafc" opacity="0.9"/>
      <ellipse cx="110" cy="100" rx="30" ry="8" fill="#ffffff" filter="drop-shadow(0 0 4px #ffffff)"/>
      <text x="110" y="125" fill="#f8fafc" font-size="8" font-weight="bold" text-anchor="middle">White BaSO4 &darr;</text>
      <!-- Arrow -->
      <path d="M 175,70 L 235,70" stroke="#f59e0b" stroke-width="3"/>
      <!-- Callout -->
      <rect x="250" y="25" width="195" height="95" rx="8" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
      <text x="347" y="48" fill="#a7f3d0" font-size="8" font-weight="bold" text-anchor="middle">Na2SO4 + BaCl2 &rarr; BaSO4&darr; + 2NaCl</text>
      <text x="347" y="68" fill="#ffffff" font-size="8" text-anchor="middle">Ba(2+) + SO4(2-) &rarr; BaSO4(s)</text>
      <text x="347" y="85" fill="#fde047" font-size="7" text-anchor="middle">Mutual Ion Exchange Between Two Salts</text>
      <text x="347" y="103" fill="#a7f3d0" font-size="7" font-weight="bold" text-anchor="middle">Insoluble Precipitate Formation</text>
    `;
  } else if(mode === 'pbi2') {
    status.textContent = "Revisiting Activity 1.2: Pb(NO3)2(aq) + 2 KI(aq) → PbI2(s)↓ [Bright Yellow] + 2 KNO3(aq)";
    d1.textContent = "Pb(NO3)2 + 2 KI";
    d2.textContent = "Bright Yellow PbI2";
    d3.textContent = "Double Displacement";
    badge.textContent = "Lead Iodide Precipitation";
    desc.textContent = "Lead nitrate reacts with potassium iodide through double displacement: Pb(NO3)2 + 2KI -> PbI2 + 2KNO3. Lead cations and potassium cations swap nitrate and iodide partners, precipitating yellow PbI2.";
    canvas.innerHTML = `
      <rect x="70" y="30" width="80" height="85" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
      <rect x="72" y="65" width="76" height="48" fill="#facc15" opacity="0.9"/>
      <text x="110" y="125" fill="#fef08a" font-size="8" font-weight="bold" text-anchor="middle">Yellow PbI2 &darr;</text>
      <path d="M 175,70 L 235,70" stroke="#f59e0b" stroke-width="3"/>
      <rect x="250" y="25" width="195" height="95" rx="8" fill="#1c1917" stroke="#eab308" stroke-width="1.5"/>
      <text x="347" y="48" fill="#fef08a" font-size="8" font-weight="bold" text-anchor="middle">Pb(NO3)2 + 2KI &rarr; PbI2&darr; + 2KNO3</text>
      <text x="347" y="68" fill="#ffffff" font-size="8" text-anchor="middle">Pb(2+) + 2 I(-) &rarr; PbI2(s)</text>
      <text x="347" y="85" fill="#cbd5e1" font-size="7" text-anchor="middle">Instant Golden Yellow Precipitate</text>
      <text x="347" y="103" fill="#4ade80" font-size="7" font-weight="bold" text-anchor="middle">Classic Analytical Test for Lead</text>
    `;
  } else {
    status.textContent = "General Double Displacement Rule: AB + CD → AD + CB (Mutual Ion Partner Exchange)";
    d1.textContent = "Cation A + Anion B";
    d2.textContent = "Cation C + Anion D";
    d3.textContent = "New Pairs AD + CB";
    badge.textContent = "Ion Exchange Pattern";
    desc.textContent = "Double displacement reactions require two compounds in aqueous solution where cations and anions swap places mutually: AB + CD -> AD + CB, commonly forming one insoluble precipitate.";
    canvas.innerHTML = `
      <rect x="50" y="40" width="120" height="65" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
      <text x="110" y="65" fill="#e0e7ff" font-size="12" font-weight="bold" text-anchor="middle">A(+) B(-)</text>
      <text x="110" y="85" fill="#a5b4fc" font-size="8" text-anchor="middle">+ C(+) D(-)</text>
      <path d="M 185,72 L 255,72" stroke="#f59e0b" stroke-width="3"/>
      <polygon points="255,67 267,72 255,77" fill="#f59e0b"/>
      <rect x="275" y="40" width="140" height="65" rx="8" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
      <text x="345" y="65" fill="#ecfdf5" font-size="12" font-weight="bold" text-anchor="middle">A(+) D(-) &darr;</text>
      <text x="345" y="85" fill="#a7f3d0" font-size="8" text-anchor="middle">+ C(+) B(-) (aq)</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S14('baso4'));
</script>""",

    15: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Redox Cycle:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC10S15('ox')" id="c10s15_btn_ox" class="px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">1. Copper Oxidation (Black)</button>
        <button onclick="setC10S15('red')" id="c10s15_btn_red" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">2. Hydrogen Reduction (Brown)</button>
        <button onclick="setC10S15('other')" id="c10s15_btn_oth" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">ZnO + C / MnO2 + HCl</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s15_status">Activity 1.11: 2Cu + O2 &rarr; 2CuO (Black Surface Coating)</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <g id="c10s15_svg_canvas"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Oxidised Substance</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c10s15_ox">Copper: Cu &rarr; CuO</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Reduced Substance</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c10s15_red">Oxygen: O2 &rarr; O(2-)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Redox Hallmark</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c10s15_hl">Brown Cu &rarr; Jet Black CuO</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-amber-950 border border-amber-700/60 text-amber-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s15_badge">Redox Chemistry</span>
    <span id="c10s15_desc">Oxidation is the gain of oxygen (or loss of hydrogen); reduction is the loss of oxygen (or gain of hydrogen). Heating copper forms black CuO; passing H2 over it restores brown copper metal.</span>
  </div>
</div>
<script>
window.setC10S15 = function(mode) {
  ['ox', 'red', 'oth'].forEach(b => {
    const el = document.getElementById('c10s15_btn_' + b);
    if(el) {
      if((mode === 'ox' && b === 'ox') || (mode === 'red' && b === 'red') || (mode === 'other' && b === 'oth')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const canvas = document.getElementById('c10s15_svg_canvas');
  const status = document.getElementById('c10s15_status');
  const sOx = document.getElementById('c10s15_ox');
  const sRed = document.getElementById('c10s15_red');
  const sHl = document.getElementById('c10s15_hl');
  const badge = document.getElementById('c10s15_badge');
  const desc = document.getElementById('c10s15_desc');

  if(mode === 'ox') {
    status.textContent = "Step 1: 2 Cu + O2 --[Heat]--> 2 CuO (Copper Gains Oxygen = Oxidation)";
    sOx.textContent = "Copper (gains Oxygen)";
    sRed.textContent = "Oxygen (is reduced)";
    sHl.textContent = "Brown Cu → Black CuO";
    badge.textContent = "1. Copper Oxidation";
    desc.textContent = "Heating brown copper powder in air oxidizes it: 2Cu + O2 -> 2CuO. Copper gains oxygen atoms, forming a jet black surface coating of copper(II) oxide.";
    canvas.innerHTML = `
      <ellipse cx="120" cy="115" rx="55" ry="15" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
      <!-- Black powder -->
      <ellipse cx="120" cy="112" rx="35" ry="8" fill="#0f172a" stroke="#334155"/>
      <text x="120" y="98" fill="#f8fafc" font-size="8" font-weight="bold" text-anchor="middle">Black CuO Powder</text>
      <!-- Burner flame underneath -->
      <polygon points="120,135 110,122 130,122" fill="#ef4444"/>
      <!-- Arrow -->
      <path d="M 195,70 L 255,70" stroke="#f59e0b" stroke-width="3"/>
      <rect x="270" y="25" width="175" height="95" rx="8" fill="#1c1917" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="357" y="48" fill="#fef08a" font-size="9" font-weight="bold" text-anchor="middle">2 Cu + O2 &rarr; 2 CuO</text>
      <text x="357" y="68" fill="#fca5a5" font-size="8" text-anchor="middle">Copper gains Oxygen &rarr; Oxidised</text>
      <text x="357" y="86" fill="#cbd5e1" font-size="7" text-anchor="middle">Jet Black Surface Coating</text>
      <text x="357" y="103" fill="#4ade80" font-size="7" font-weight="bold" text-anchor="middle">Exothermic High-Temp Oxidation</text>
    `;
  } else if(mode === 'red') {
    status.textContent = "Step 2: CuO + H2 --[Heat]--> Cu + H2O (CuO Loses Oxygen = Reduction)";
    sOx.textContent = "Hydrogen: H2 → H2O";
    sRed.textContent = "Copper Oxide: CuO → Cu";
    sHl.textContent = "Black CuO → Brown Cu";
    badge.textContent = "2. Hydrogen Reduction";
    desc.textContent = "Passing hydrogen gas over hot black copper oxide reverses the reaction: CuO + H2 -> Cu + H2O. CuO loses oxygen (reduced to brown copper), while H2 gains oxygen (oxidised to water).";
    canvas.innerHTML = `
      <!-- Glass tube with H2 stream -->
      <rect x="50" y="55" width="180" height="35" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <!-- Brown copper restored -->
      <ellipse cx="140" cy="78" rx="30" ry="7" fill="#b45309"/>
      <text x="140" y="68" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">Restored Brown Cu</text>
      <!-- H2 Inflow -->
      <path d="M 20,72 L 50,72" stroke="#38bdf8" stroke-width="3"/>
      <text x="35" y="65" fill="#bae6fd" font-size="7">H2 In</text>
      <rect x="250" y="25" width="195" height="95" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
      <text x="347" y="48" fill="#ecfdf5" font-size="9" font-weight="bold" text-anchor="middle">CuO + H2 &rarr; Cu + H2O</text>
      <text x="347" y="68" fill="#a7f3d0" font-size="8" text-anchor="middle">CuO loses Oxygen &rarr; REDUCED to Cu</text>
      <text x="347" y="86" fill="#fde047" font-size="8" text-anchor="middle">H2 gains Oxygen &rarr; OXIDISED to H2O</text>
      <text x="347" y="103" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Simultaneous Redox Transfer</text>
    `;
  } else {
    status.textContent = "Other Redox Reactions: ZnO + C → Zn + CO  &bull;  MnO2 + 4HCl → MnCl2 + 2H2O + Cl2";
    sOx.textContent = "C & HCl are Oxidised";
    sRed.textContent = "ZnO & MnO2 are Reduced";
    sHl.textContent = "Coupled Electron/Oxygen Transfer";
    badge.textContent = "Redox Examples";
    desc.textContent = "In ZnO + C -> Zn + CO, carbon oxidizes to CO while ZnO reduces to Zn. In MnO2 + 4HCl -> MnCl2 + 2H2O + Cl2, HCl oxidizes to Cl2 while MnO2 reduces to MnCl2.";
    canvas.innerHTML = `
      <rect x="40" y="25" width="380" height="95" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
      <text x="230" y="50" fill="#e0e7ff" font-size="10" font-weight="bold" text-anchor="middle">1. ZnO + C &rarr; Zn + CO</text>
      <text x="230" y="68" fill="#cbd5e1" font-size="8" text-anchor="middle">C is oxidised to CO &bull; ZnO is reduced to Zn</text>
      <text x="230" y="90" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">2. MnO2 + 4 HCl &rarr; MnCl2 + 2 H2O + Cl2</text>
      <text x="230" y="108" fill="#bae6fd" font-size="8" text-anchor="middle">HCl loses H (oxidised) &bull; MnO2 loses O (reduced)</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S15('ox'));
</script>""",

    16: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Oxidation Effect:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC10S16('iron_cor')" id="c10s16_btn_iro" class="px-2.5 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition">Iron Rusting</button>
        <button onclick="setC10S16('metals')" id="c10s16_btn_met" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Silver &amp; Copper Patinas</button>
        <button onclick="setC10S16('rancid')" id="c10s16_btn_ran" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Rancidity &amp; N2 Flush</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s16_status">Corrosion: Environmental Degradation of Metals by Moisture &amp; Oxygen</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <g id="c10s16_svg_canvas"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Corrosive Agent</div>
        <div class="text-xs font-bold text-rose-300 mt-0.5" id="c10s16_ca">O2 + H2O Moisture</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Degradation Product</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c10s16_dp">Red-Brown Fe2O3·xH2O</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Prevention Technique</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c10s16_pt">Galvanizing &bull; Painting</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-rose-950 border border-rose-700/60 text-rose-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s16_badge">Corrosion</span>
    <span id="c10s16_desc">Corrosion damages metallic infrastructure such as bridges and railings. Rancidity oxidizes fats and oils in stored food; sealing snacks with nitrogen gas prevents rancidity.</span>
  </div>
</div>
<script>
window.setC10S16 = function(type) {
  ['iro', 'met', 'ran'].forEach(b => {
    const el = document.getElementById('c10s16_btn_' + b);
    if(el) {
      if((type === 'iron_cor' && b === 'iro') || (type === 'metals' && b === 'met') || (type === 'rancid' && b === 'ran')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const canvas = document.getElementById('c10s16_svg_canvas');
  const status = document.getElementById('c10s16_status');
  const ca = document.getElementById('c10s16_ca');
  const dp = document.getElementById('c10s16_dp');
  const pt = document.getElementById('c10s16_pt');
  const badge = document.getElementById('c10s16_badge');
  const desc = document.getElementById('c10s16_desc');

  if(type === 'iron_cor') {
    status.textContent = "Iron Rusting: 4 Fe + 3 O2 + 2x H2O → 2 Fe2O3·xH2O (Flaky Reddish-Brown Crust)";
    ca.textContent = "Moist Air (O2 + H2O)";
    dp.textContent = "Hydrated Ferric Oxide";
    pt.textContent = "Painting &amp; Galvanizing";
    badge.textContent = "Rusting of Iron";
    desc.textContent = "Iron corrodes when attacked by moisture and atmospheric oxygen, forming a flaky reddish-brown powder of hydrated ferric oxide. This causes billions of rupees in damage to bridges, ships, and railings.";
    canvas.innerHTML = `
      <!-- Bridge girder rusting -->
      <rect x="40" y="45" width="160" height="25" rx="4" fill="#94a3b8" stroke="#475569" stroke-width="2"/>
      <rect x="70" y="45" width="100" height="15" fill="#78350f"/>
      <circle cx="85" cy="52" r="3" fill="#b45309"/>
      <circle cx="115" cy="50" r="4" fill="#b45309"/>
      <circle cx="145" cy="53" r="3.5" fill="#b45309"/>
      <text x="120" y="90" fill="#f87171" font-size="8" font-weight="bold" text-anchor="middle">Flaking Rust Layer</text>
      <!-- Callout -->
      <rect x="230" y="25" width="200" height="95" rx="8" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
      <text x="330" y="50" fill="#fee2e2" font-size="9" font-weight="bold" text-anchor="middle">Corrosion of Iron (Rusting)</text>
      <text x="330" y="70" fill="#fca5a5" font-size="8" text-anchor="middle">Fe2O3 &bull; xH2O flakes away continuously</text>
      <text x="330" y="88" fill="#fde047" font-size="8" text-anchor="middle">Weakens bridges, ships, and car bodies</text>
      <text x="330" y="106" fill="#a7f3d0" font-size="7" font-weight="bold" text-anchor="middle">Prevention: Galvanizing with Zinc coating</text>
    `;
  } else if(type === 'metals') {
    status.textContent = "Silver Tarnishing (Ag2S Black) & Copper Corrosion (CuCO3·Cu(OH)2 Green Patina)";
    ca.textContent = "H2S Gas / Moist CO2";
    dp.textContent = "Black Ag2S &amp; Green Patina";
    pt.textContent = "Protective Polishing";
    badge.textContent = "Silver &amp; Copper Patinas";
    desc.textContent = "Silver reacts with airborne hydrogen sulphide to form a black coating of silver sulphide (Ag2S). Copper reacts with moist carbon dioxide to form a protective green patina of basic copper carbonate.";
    canvas.innerHTML = `
      <!-- Silver spoon tarnished black -->
      <rect x="50" y="35" width="150" height="35" rx="6" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
      <circle cx="75" cy="52" r="10" fill="#334155"/>
      <text x="135" y="50" fill="#f8fafc" font-size="8" font-weight="bold">Silver Tarnish: Ag2S</text>
      <text x="135" y="62" fill="#94a3b8" font-size="7">Black Silver Sulphide</text>
      <!-- Copper vessel green patina -->
      <rect x="50" y="80" width="150" height="40" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
      <circle cx="75" cy="100" r="10" fill="#059669"/>
      <text x="135" y="96" fill="#ecfdf5" font-size="8" font-weight="bold">Copper Patina: Green</text>
      <text x="135" y="108" fill="#a7f3d0" font-size="7">CuCO3 &bull; Cu(OH)2</text>
      <!-- Summary Box -->
      <rect x="225" y="25" width="210" height="95" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
      <text x="330" y="50" fill="#e0e7ff" font-size="9" font-weight="bold" text-anchor="middle">Surface Patina Formation</text>
      <text x="330" y="70" fill="#cbd5e1" font-size="8" text-anchor="middle">Silver: 2Ag + H2S &rarr; Ag2S (Black)</text>
      <text x="330" y="88" fill="#86efac" font-size="8" text-anchor="middle">Copper: Cu + CO2 + H2O &rarr; Green Patina</text>
      <text x="330" y="106" fill="#fde047" font-size="7" font-weight="bold" text-anchor="middle">Cleaned by acidic lemon juice (citric acid)</text>
    `;
  } else {
    status.textContent = "Rancidity: Lipid Oxidation in Food & Nitrogen Flushing Prevention in Snack Packaging";
    ca.textContent = "Atmospheric O2 on Fats";
    dp.textContent = "Foul-Smelling Aldehydes";
    pt.textContent = "Flush N2 Gas &bull; Airtight";
    badge.textContent = "Rancidity &amp; N2 Flush";
    desc.textContent = "When fats and oils in food are exposed to air, they oxidize, producing foul tastes and stale odors (rancidity). Chip manufacturers flush snack bags with inert nitrogen gas to displace oxygen and keep chips fresh.";
    canvas.innerHTML = `
      <!-- Potato chip packet puffed with Nitrogen -->
      <rect x="60" y="30" width="110" height="85" rx="10" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
      <ellipse cx="115" cy="65" rx="35" ry="16" fill="#f59e0b"/>
      <text x="115" y="68" fill="#78350f" font-size="8" font-weight="bold" text-anchor="middle">Crispy Chips</text>
      <text x="115" y="95" fill="#e0f2fe" font-size="8" font-weight="bold" text-anchor="middle">Flushed with N2 Gas</text>
      <!-- Arrow -->
      <path d="M 190,72 L 245,72" stroke="#f59e0b" stroke-width="3"/>
      <!-- Nitrogen protection explanation -->
      <rect x="255" y="25" width="190" height="95" rx="8" fill="#14532d" stroke="#22c55e" stroke-width="1.5"/>
      <text x="350" y="50" fill="#ecfdf5" font-size="9" font-weight="bold" text-anchor="middle">Preventing Rancidity</text>
      <text x="350" y="70" fill="#bbf7d0" font-size="8" text-anchor="middle">1. Flushed with unreactive N2 gas</text>
      <text x="350" y="88" fill="#bbf7d0" font-size="8" text-anchor="middle">2. Adding antioxidants (BHA/BHT)</text>
      <text x="350" y="106" fill="#fde047" font-size="7" font-weight="bold" text-anchor="middle">3. Airtight storage prevents O2 contact</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S16('iron_cor'));
</script>"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part2)} simulators for Part 2 (Slides 9-16).")
