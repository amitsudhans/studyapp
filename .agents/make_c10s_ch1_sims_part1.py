#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 1 Simulators (Part 1: Slides 1-8)
High-fidelity responsive SVG interactive laboratory widgets for Chemical Reactions and Equations.
"""

sims_part1 = {
    1: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Select Scenario:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800 flex-wrap">
        <button onclick="setC10S1('milk')" id="c10s1_btn_milk" class="px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition">Milk Souring</button>
        <button onclick="setC10S1('rust')" id="c10s1_btn_rust" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Iron Rusting</button>
        <button onclick="setC10S1('ferment')" id="c10s1_btn_fer" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Fermentation</button>
        <button onclick="setC10S1('digest')" id="c10s1_btn_dig" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Digestion</button>
        <button onclick="setC10S1('physical')" id="c10s1_btn_phy" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Wax Melting (Physical)</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s1_status">Chemical Change &bull; Bonds Broken &amp; Formed</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <g id="c10s1_svg_group"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Transformation Type</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c10s1_type">Chemical Reaction</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Bond Rearrangement</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c10s1_bonds">Lactose &rarr; Lactic Acid</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Reversibility</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c10s1_rev">Permanent / Irreversible</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-emerald-950 border border-emerald-700/60 text-emerald-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s1_badge">Chemical Change</span>
    <span id="c10s1_desc">Whenever the nature and identity of the initial substance change completely, a chemical reaction has taken place. New chemical bonds form with entirely different physical and chemical properties.</span>
  </div>
</div>
<script>
window.setC10S1 = function(type) {
  ['milk', 'rust', 'ferment', 'digest', 'physical'].forEach(b => {
    const el = document.getElementById('c10s1_btn_' + b);
    if(el) {
      if(b === type) el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
      else el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    }
  });

  const svg = document.getElementById('c10s1_svg_group');
  const status = document.getElementById('c10s1_status');
  const tType = document.getElementById('c10s1_type');
  const bonds = document.getElementById('c10s1_bonds');
  const rev = document.getElementById('c10s1_rev');
  const badge = document.getElementById('c10s1_badge');
  const desc = document.getElementById('c10s1_desc');

  if(type === 'milk') {
    status.textContent = "Summer Bacterial Fermentation • Lactose converted to Lactic Acid";
    tType.textContent = "Chemical Reaction";
    bonds.textContent = "Lactose → Lactic Acid";
    rev.textContent = "Irreversible Change";
    badge.textContent = "Milk Souring";
    desc.textContent = "Lactobacillus bacteria metabolize sugar lactose in milk into lactic acid, dropping pH and coagulating casein proteins into curd. New substances form with altered taste, smell, and pH.";
    svg.innerHTML = `
      <rect x="40" y="30" width="70" height="90" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
      <text x="75" y="75" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">Fresh Milk</text>
      <text x="75" y="90" fill="#64748b" font-size="7" text-anchor="middle">pH ~ 6.6</text>
      <path d="M 125,75 L 205,75" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrow)"/>
      <text x="165" y="65" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Bacteria 37&deg;C</text>
      <rect x="220" y="30" width="70" height="90" rx="8" fill="#fef08a" stroke="#eab308" stroke-width="2"/>
      <text x="255" y="75" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">Sour Curd</text>
      <text x="255" y="90" fill="#92400e" font-size="7" text-anchor="middle">Lactic Acid (pH ~ 4.5)</text>
      <circle cx="370" cy="75" r="30" fill="#047857" opacity="0.3"/>
      <text x="370" y="72" fill="#34d399" font-size="8" font-weight="bold" text-anchor="middle">New Substance</text>
      <text x="370" y="85" fill="#a7f3d0" font-size="7" text-anchor="middle">Chemical Bonds Formed</text>
    `;
  } else if(type === 'rust') {
    status.textContent = "Iron Corrosion • Fe + O2 + xH2O → Fe2O3·xH2O Flaky Rust";
    tType.textContent = "Chemical Reaction";
    bonds.textContent = "Fe → Fe2O3·xH2O";
    rev.textContent = "Irreversible Degradation";
    badge.textContent = "Iron Rusting";
    desc.textContent = "Iron exposed to damp monsoon air undergoes electrochemical oxidation. Shiny iron atoms oxidize and bond with oxygen and water molecules to form hydrated ferric oxide (reddish-brown rust).";
    svg.innerHTML = `
      <rect x="40" y="55" width="80" height="40" rx="4" fill="#94a3b8" stroke="#475569" stroke-width="2"/>
      <text x="80" y="78" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">Shiny Iron Tawa</text>
      <path d="M 135,75 L 210,75" stroke="#ef4444" stroke-width="3"/>
      <text x="172" y="65" fill="#f87171" font-size="8" font-weight="bold" text-anchor="middle">O2 + H2O</text>
      <rect x="225" y="55" width="80" height="40" rx="4" fill="#78350f" stroke="#b45309" stroke-width="2"/>
      <text x="265" y="78" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">Reddish Rust</text>
      <rect x="330" y="35" width="105" height="75" rx="6" fill="#1c1917" stroke="#dc2626" stroke-width="1.5"/>
      <text x="382" y="60" fill="#fca5a5" font-size="8" font-weight="bold" text-anchor="middle">Hydrated Ferric Oxide</text>
      <text x="382" y="78" fill="#cbd5e1" font-size="7" text-anchor="middle">Fe2O3 &bull; xH2O</text>
      <text x="382" y="92" fill="#f87171" font-size="7" text-anchor="middle">Flakes &amp; Destroys Metal</text>
    `;
  } else if(type === 'ferment') {
    status.textContent = "Grape Fermentation • C6H12O6 → 2 C2H5OH + 2 CO2";
    tType.textContent = "Chemical Reaction";
    bonds.textContent = "Glucose → Ethanol + CO2";
    rev.textContent = "Biochemical Cleavage";
    badge.textContent = "Fermentation";
    desc.textContent = "Natural yeast enzymes cleave glucose molecules in grapes into ethanol and carbon dioxide gas without oxygen. The sweet sugar bonds break to form alcohol and effervescing carbon dioxide.";
    svg.innerHTML = `
      <circle cx="75" cy="75" r="30" fill="#7c3aed" opacity="0.8"/>
      <text x="75" y="78" fill="#ede9fe" font-size="8" font-weight="bold" text-anchor="middle">Grape Glucose</text>
      <path d="M 120,75 L 195,75" stroke="#a855f7" stroke-width="3"/>
      <text x="157" y="65" fill="#d8b4fe" font-size="8" font-weight="bold" text-anchor="middle">Yeast Enzymes</text>
      <rect x="210" y="45" width="75" height="60" rx="6" fill="#0284c7"/>
      <text x="247" y="75" fill="#f0f9ff" font-size="8" font-weight="bold" text-anchor="middle">Ethanol C2H5OH</text>
      <circle cx="340" cy="55" r="14" fill="#64748b"/>
      <text x="340" y="58" fill="#f1f5f9" font-size="7" font-weight="bold" text-anchor="middle">CO2 &uarr;</text>
      <circle cx="380" cy="85" r="16" fill="#64748b"/>
      <text x="380" y="88" fill="#f1f5f9" font-size="7" font-weight="bold" text-anchor="middle">CO2 &uarr;</text>
    `;
  } else if(type === 'digest') {
    status.textContent = "Food Digestion & Respiration • Macromolecules into Glucose & Energy";
    tType.textContent = "Chemical Reaction";
    bonds.textContent = "Starch → Glucose → ATP";
    rev.textContent = "Metabolic Pathway";
    badge.textContent = "Digestion & Respiration";
    desc.textContent = "Enzymes in the stomach and intestines break down complex starches into glucose. In cells, glucose reacts with oxygen (C6H12O6 + 6O2 -> 6CO2 + 6H2O + Energy) to release life-sustaining ATP.";
    svg.innerHTML = `
      <rect x="35" y="45" width="80" height="55" rx="6" fill="#14532d" stroke="#22c55e" stroke-width="1.5"/>
      <text x="75" y="70" fill="#dcfce7" font-size="8" font-weight="bold" text-anchor="middle">Food (Starch)</text>
      <text x="75" y="85" fill="#86efac" font-size="7" text-anchor="middle">Complex Polymer</text>
      <path d="M 125,75 L 205,75" stroke="#22c55e" stroke-width="3"/>
      <text x="165" y="65" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">Amylase</text>
      <rect x="215" y="45" width="90" height="55" rx="6" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="260" y="70" fill="#fef3c7" font-size="8" font-weight="bold" text-anchor="middle">Glucose (C6H12O6)</text>
      <text x="260" y="85" fill="#fde68a" font-size="7" text-anchor="middle">+ 6O2 &rarr; 6CO2 + ATP</text>
      <circle cx="375" cy="72" r="26" fill="#ea580c"/>
      <text x="375" y="75" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">ATP Energy</text>
    `;
  } else {
    status.textContent = "Wax Melting • Phase Change Solid to Liquid (Physical Change)";
    tType.textContent = "Physical Change Only";
    bonds.textContent = "Hydrocarbon Molecules Intact";
    rev.textContent = "Easily Reversible on Cooling";
    badge.textContent = "Physical Change";
    desc.textContent = "Melting wax or boiling water alters only physical state. The chemical formula of hydrocarbon wax molecules remains completely unchanged; no chemical bonds are created or destroyed.";
    svg.innerHTML = `
      <rect x="50" y="40" width="60" height="70" rx="4" fill="#fde047" stroke="#ca8a04" stroke-width="2"/>
      <text x="80" y="75" fill="#713f12" font-size="8" font-weight="bold" text-anchor="middle">Solid Wax</text>
      <path d="M 125,75 L 210,75" stroke="#94a3b8" stroke-width="3" stroke-dasharray="4,3"/>
      <text x="167" y="65" fill="#cbd5e1" font-size="8" font-weight="bold" text-anchor="middle">+ Heat</text>
      <path d="M 230,85 Q 260,50 290,85 T 350,85" stroke="#eab308" stroke-width="8" fill="none"/>
      <text x="290" y="115" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Liquid Molten Wax</text>
      <text x="290" y="130" fill="#94a3b8" font-size="7" text-anchor="middle">Formula Identical &bull; Cools back to solid</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S1('milk'));
</script>""",

    2: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Experiment Step:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC10S2('sandpaper')" id="c10s2_btn_san" class="px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">1. Sandpaper Clean</button>
        <button onclick="setC10S2('burn')" id="c10s2_btn_bur" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">2. Dazzling Flame</button>
        <button onclick="setC10S2('ash')" id="c10s2_btn_ash" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">3. White Ash (MgO)</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s2_status">Step 1: Strip basic magnesium oxide protective layer</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Spirit Burner -->
        <rect x="40" y="100" width="40" height="35" rx="4" fill="#334155"/>
        <rect x="55" y="90" width="10" height="10" fill="#64748b"/>
        <polygon id="c10s2_burner_flame" points="60,65 52,90 68,90" fill="#3b82f6" opacity="0.8"/>

        <!-- Tongs -->
        <line x1="160" y1="20" x2="100" y2="75" stroke="#94a3b8" stroke-width="3"/>
        <line x1="160" y1="25" x2="105" y2="78" stroke="#94a3b8" stroke-width="3"/>

        <!-- Watch Glass on Right -->
        <ellipse cx="360" cy="120" rx="45" ry="12" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
        <text x="360" y="138" fill="#94a3b8" font-size="7" text-anchor="middle">Watch Glass</text>

        <!-- Dynamic elements -->
        <g id="c10s2_active_graphics"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Reactant Solid</div>
        <div class="text-xs font-bold text-slate-200 mt-0.5" id="c10s2_val1">Magnesium Ribbon (Mg)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Gaseous Partner</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c10s2_val2">Oxygen (O2 in Air)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Synthesized Product</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c10s2_val3">Magnesium Oxide (MgO)</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-amber-950 border border-amber-700/60 text-amber-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s2_badge">Activity 1.1</span>
    <span id="c10s2_desc">Rubbing with sandpaper removes the non-reactive basic magnesium oxide film. Clean magnesium ribbon burns with an intense, dazzling white flame to form white magnesium oxide powder: 2Mg + O2 &rarr; 2MgO.</span>
  </div>
</div>
<script>
window.setC10S2 = function(step) {
  ['san', 'bur', 'ash'].forEach(s => {
    const el = document.getElementById('c10s2_btn_' + s);
    if(el) {
      if((step === 'sandpaper' && s === 'san') || (step === 'burn' && s === 'bur') || (step === 'ash' && s === 'ash')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const gfx = document.getElementById('c10s2_active_graphics');
  const flame = document.getElementById('c10s2_burner_flame');
  const status = document.getElementById('c10s2_status');
  const v1 = document.getElementById('c10s2_val1');
  const v2 = document.getElementById('c10s2_val2');
  const v3 = document.getElementById('c10s2_val3');
  const badge = document.getElementById('c10s2_badge');
  const desc = document.getElementById('c10s2_desc');

  if(step === 'sandpaper') {
    flame.setAttribute('opacity', '0.4');
    status.textContent = "Step 1: Clean ribbon with sandpaper to remove passive oxide layer";
    v1.textContent = "Pure Shiny Mg Metal";
    v2.textContent = "Removes Passive Film";
    v3.textContent = "Prepares for Ignition";
    badge.textContent = "Surface Cleaning";
    desc.textContent = "Magnesium reacts slowly with ambient air to form a passive coating of basic magnesium oxide. Thoroughly rubbing with abrasive sandpaper strips this layer, exposing lustrous pure metal for rapid combustion.";
    gfx.innerHTML = `
      <rect x="75" y="70" width="60" height="8" rx="2" fill="#cbd5e1" stroke="#94a3b8"/>
      <rect x="110" y="60" width="25" height="28" rx="2" fill="#d97706" opacity="0.8"/>
      <text x="122" y="52" fill="#fde68a" font-size="7" font-weight="bold" text-anchor="middle">Sandpaper</text>
      <text x="105" y="95" fill="#94a3b8" font-size="8" text-anchor="middle">Stripping Passive MgO Barrier</text>
    `;
  } else if(step === 'burn') {
    flame.setAttribute('opacity', '0.9');
    status.textContent = "Step 2: Burning in air with a dazzling, brilliant white flame";
    v1.textContent = "Combusting Ribbon";
    v2.textContent = "+ O2 from Atmosphere";
    v3.textContent = "Exothermic Radiant Light";
    badge.textContent = "Dazzling Flame";
    desc.textContent = "Held over the burner flame with tongs, the magnesium ignites at high temperature, burning with a blinding, dazzling white flare. Immense radiant and thermal energy is liberated as oxygen bonds with magnesium.";
    gfx.innerHTML = `
      <line x1="100" y1="75" x2="60" y2="78" stroke="#f8fafc" stroke-width="4"/>
      <!-- Dazzling Star Flare -->
      <circle cx="60" cy="78" r="18" fill="#ffffff" filter="drop-shadow(0 0 12px #ffffff)"/>
      <polygon points="60,50 64,74 88,78 64,82 60,106 56,82 32,78 56,74" fill="#ffffff"/>
      <text x="140" y="50" fill="#fef08a" font-size="9" font-weight="bold">Dazzling White Flame!</text>
      <text x="140" y="65" fill="#f8fafc" font-size="7">Intense UV &amp; Visible Light</text>
    `;
  } else {
    flame.setAttribute('opacity', '0.4');
    status.textContent = "Step 3: White powdery ash of Magnesium Oxide (MgO) collected in watch glass";
    v1.textContent = "Mg Atoms Consumed";
    v2.textContent = "O2 Atoms Incorporated";
    v3.textContent = "2Mg + O2 → 2MgO (White Ash)";
    badge.textContent = "White Ash (MgO)";
    desc.textContent = "The combustion reaction yields solid magnesium oxide: 2Mg(s) + O2(g) -> 2MgO(s). The white powdery ash collects safely in the watch glass, demonstrating combination into an ionic oxide lattice.";
    gfx.innerHTML = `
      <!-- Powder on watch glass -->
      <ellipse cx="360" cy="118" rx="25" ry="6" fill="#f8fafc" filter="drop-shadow(0 0 3px #ffffff)"/>
      <circle cx="355" cy="116" r="3" fill="#ffffff"/>
      <circle cx="365" cy="117" r="2.5" fill="#ffffff"/>
      <text x="360" y="95" fill="#4ade80" font-size="9" font-weight="bold" text-anchor="middle">White Ash: MgO</text>
      <text x="360" y="107" fill="#86efac" font-size="7" text-anchor="middle">2 Mg + O2 &rarr; 2 MgO</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S2('sandpaper'));
</script>""",

    3: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-sky-400 uppercase tracking-wider">Hallmark Activity:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC10S3('act12')" id="c10s3_btn_12" class="px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition">Activity 1.2: Pb(NO3)2 + KI</button>
        <button onclick="setC10S3('act13')" id="c10s3_btn_13" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Activity 1.3: Zn + H2SO4</button>
        <button onclick="setC10S3('matrix')" id="c10s3_btn_mat" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">4 Hallmarks Matrix</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s3_status">Activity 1.2 &bull; Yellow PbI2 Precipitate Formation</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <g id="c10s3_svg_canvas"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Visual Hallmark</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c10s3_h1">Change in Colour &amp; State</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Chemical Reaction</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c10s3_h2">Precipitation of PbI2</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Observable Evidence</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c10s3_h3">Insoluble Yellow Solid</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-sky-950 border border-sky-700/60 text-sky-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s3_badge">Hallmarks</span>
    <span id="c10s3_desc">Mixing clear lead nitrate and potassium iodide solutions precipitates bright yellow lead iodide. Zinc with dilute acid evolves bubbling hydrogen gas with noticeable heat release.</span>
  </div>
</div>
<script>
window.setC10S3 = function(mode) {
  ['12', '13', 'mat'].forEach(b => {
    const el = document.getElementById('c10s3_btn_' + b);
    if(el) {
      if((mode === 'act12' && b === '12') || (mode === 'act13' && b === '13') || (mode === 'matrix' && b === 'mat')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const canvas = document.getElementById('c10s3_svg_canvas');
  const status = document.getElementById('c10s3_status');
  const h1 = document.getElementById('c10s3_h1');
  const h2 = document.getElementById('c10s3_h2');
  const h3 = document.getElementById('c10s3_h3');
  const badge = document.getElementById('c10s3_badge');
  const desc = document.getElementById('c10s3_desc');

  if(mode === 'act12') {
    status.textContent = "Activity 1.2: Lead Nitrate + Potassium Iodide → Yellow Lead Iodide Precipitate";
    h1.textContent = "Colour & State Change";
    h2.textContent = "Pb(NO3)2 + 2KI → PbI2↓";
    h3.textContent = "Bright Yellow Precipitate";
    badge.textContent = "Activity 1.2 (Precipitation)";
    desc.textContent = "Mixing two clear, colourless aqueous solutions—lead nitrate and potassium iodide—causes instant double displacement. An insoluble, brilliant yellow precipitate of lead iodide (PbI2) forms.";
    canvas.innerHTML = `
      <!-- Test tube 1 -->
      <rect x="50" y="25" width="22" height="85" rx="10" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
      <rect x="52" y="65" width="18" height="42" fill="#38bdf8" opacity="0.3"/>
      <text x="61" y="125" fill="#94a3b8" font-size="7" text-anchor="middle">Pb(NO3)2</text>
      <!-- Plus sign -->
      <text x="100" y="75" fill="#fde047" font-size="14" font-weight="bold" text-anchor="middle">+</text>
      <!-- Test tube 2 -->
      <rect x="130" y="25" width="22" height="85" rx="10" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
      <rect x="132" y="65" width="18" height="42" fill="#38bdf8" opacity="0.3"/>
      <text x="141" y="125" fill="#94a3b8" font-size="7" text-anchor="middle">KI (Clear)</text>
      <!-- Arrow -->
      <path d="M 175,70 L 220,70" stroke="#f59e0b" stroke-width="3"/>
      <!-- Mixed Tube with Yellow Precipitate -->
      <rect x="250" y="20" width="30" height="95" rx="12" fill="#1e293b" stroke="#cbd5e1" stroke-width="2"/>
      <rect x="252" y="50" width="26" height="62" fill="#facc15" opacity="0.9"/>
      <text x="265" y="130" fill="#fef08a" font-size="8" font-weight="bold" text-anchor="middle">Yellow PbI2 &darr;</text>
      <!-- Callout -->
      <rect x="310" y="30" width="130" height="80" rx="6" fill="#1c1917" stroke="#eab308" stroke-width="1.5"/>
      <text x="375" y="50" fill="#fef08a" font-size="8" font-weight="bold" text-anchor="middle">Precipitation Hallmark</text>
      <text x="375" y="68" fill="#cbd5e1" font-size="7" text-anchor="middle">Colourless &rarr; Bright Yellow</text>
      <text x="375" y="82" fill="#cbd5e1" font-size="7" text-anchor="middle">Liquid &rarr; Insoluble Solid</text>
      <text x="375" y="98" fill="#4ade80" font-size="7" font-weight="bold" text-anchor="middle">Pb(NO3)2 + 2KI &rarr; PbI2 + 2KNO3</text>
    `;
  } else if(mode === 'act13') {
    status.textContent = "Activity 1.3: Zinc Granules + Dilute H2SO4 → H2 Gas Evolution + Exothermic Heat";
    h1.textContent = "Gas Evolution & Heat";
    h2.textContent = "Zn + H2SO4 → ZnSO4 + H2↑";
    h3.textContent = "H2 Bubbles (Pop Test)";
    badge.textContent = "Activity 1.3 (Gas & Heat)";
    desc.textContent = "Zinc granules in dilute sulphuric acid undergo rapid effervescence, liberating hydrogen gas. The evolved gas pops near a flame, and the flask warms up noticeably, confirming an exothermic reaction.";
    canvas.innerHTML = `
      <!-- Conical Flask -->
      <polygon points="120,40 140,40 180,120 80,120" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
      <rect x="122" y="20" width="16" height="25" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
      <!-- Acid liquid -->
      <polygon points="90,118 170,118 155,80 105,80" fill="#0284c7" opacity="0.4"/>
      <!-- Zinc granules -->
      <circle cx="120" cy="112" r="5" fill="#94a3b8"/>
      <circle cx="135" cy="114" r="6" fill="#94a3b8"/>
      <circle cx="148" cy="112" r="4" fill="#94a3b8"/>
      <!-- Bubbles rising -->
      <circle cx="125" cy="95" r="2.5" fill="#ffffff" opacity="0.8"/>
      <circle cx="140" cy="85" r="3" fill="#ffffff" opacity="0.8"/>
      <circle cx="130" cy="60" r="3.5" fill="#ffffff" opacity="0.9"/>
      <circle cx="132" cy="35" r="4" fill="#ffffff"/>
      <!-- Gas label -->
      <text x="130" y="15" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">H2 Gas &uarr;</text>
      <!-- Heat radiating waves -->
      <path d="M 60,100 Q 65,110 60,120" stroke="#ef4444" stroke-width="2" fill="none"/>
      <path d="M 200,100 Q 195,110 200,120" stroke="#ef4444" stroke-width="2" fill="none"/>
      <text x="205" y="115" fill="#f87171" font-size="7" font-weight="bold">Warm Flask (+ Heat)</text>
      <!-- Callout box -->
      <rect x="250" y="30" width="190" height="85" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
      <text x="345" y="50" fill="#e0e7ff" font-size="8" font-weight="bold" text-anchor="middle">Dual Hallmarks Observed</text>
      <text x="345" y="68" fill="#bae6fd" font-size="7" text-anchor="middle">1. Gas Evolution: H2 gas bubbles</text>
      <text x="345" y="82" fill="#fca5a5" font-size="7" text-anchor="middle">2. Temperature Change: Exothermic heat</text>
      <text x="345" y="100" fill="#4ade80" font-size="7" font-weight="bold" text-anchor="middle">Burns with sharp 'pop' sound</text>
    `;
  } else {
    status.textContent = "The 4 Universal Hallmarks Indicating a Chemical Reaction";
    h1.textContent = "Universal Diagnostic Criteria";
    h2.textContent = "State, Colour, Gas & Temp";
    h3.textContent = "Proves Bond Rearrangement";
    badge.textContent = "4 Reaction Hallmarks";
    desc.textContent = "A chemical reaction is confirmed whenever one or more of four observations occur: 1. Change in state, 2. Change in colour, 3. Evolution of a gas, and 4. Change in temperature.";
    canvas.innerHTML = `
      <!-- 4 Grid Cards -->
      <rect x="20" y="20" width="95" height="100" rx="6" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
      <text x="67" y="45" fill="#60a5fa" font-size="8" font-weight="bold" text-anchor="middle">1. Change in State</text>
      <text x="67" y="70" fill="#cbd5e1" font-size="7" text-anchor="middle">Liquid &rarr; Solid</text>
      <text x="67" y="85" fill="#94a3b8" font-size="7" text-anchor="middle">Gas &rarr; Liquid</text>
      <text x="67" y="105" fill="#38bdf8" font-size="7" text-anchor="middle">Precipitation</text>

      <rect x="130" y="20" width="95" height="100" rx="6" fill="#0f172a" stroke="#eab308" stroke-width="1.5"/>
      <text x="177" y="45" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">2. Change in Colour</text>
      <text x="177" y="70" fill="#cbd5e1" font-size="7" text-anchor="middle">Clear &rarr; Yellow (PbI2)</text>
      <text x="177" y="85" fill="#cbd5e1" font-size="7" text-anchor="middle">Blue &rarr; Pale Green</text>
      <text x="177" y="105" fill="#facc15" font-size="7" text-anchor="middle">Iron in CuSO4</text>

      <rect x="240" y="20" width="95" height="100" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <text x="287" y="45" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">3. Gas Evolution</text>
      <text x="287" y="70" fill="#cbd5e1" font-size="7" text-anchor="middle">H2 gas (pops)</text>
      <text x="287" y="85" fill="#cbd5e1" font-size="7" text-anchor="middle">CO2 gas (milky lime)</text>
      <text x="287" y="105" fill="#86efac" font-size="7" text-anchor="middle">NO2 brown fumes</text>

      <rect x="350" y="20" width="95" height="100" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
      <text x="397" y="45" fill="#f87171" font-size="8" font-weight="bold" text-anchor="middle">4. Temp Change</text>
      <text x="397" y="70" fill="#cbd5e1" font-size="7" text-anchor="middle">Exothermic (+ Heat)</text>
      <text x="397" y="85" fill="#cbd5e1" font-size="7" text-anchor="middle">Endothermic (- Heat)</text>
      <text x="397" y="105" fill="#fca5a5" font-size="7" text-anchor="middle">CaO or Ba(OH)2</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S3('act12'));
</script>""",

    4: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Format Level:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC10S4('prose')" id="c10s4_btn_pro" class="px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">1. Descriptive Prose</button>
        <button onclick="setC10S4('word')" id="c10s4_btn_wor" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">2. Word Equation</button>
        <button onclick="setC10S4('skeletal')" id="c10s4_btn_ske" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">3. Skeletal Equation</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s4_status">Prose Description • Lengthy &amp; Descriptive</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <g id="c10s4_svg_display"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Equation Structure</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c10s4_str">Full English Narrative</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Reactant Side (LHS)</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c10s4_lhs">Magnesium + Oxygen</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Product Side (RHS)</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c10s4_rhs">Magnesium Oxide</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-amber-950 border border-amber-700/60 text-amber-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s4_badge">Chemical Shorthand</span>
    <span id="c10s4_desc">Chemical reactions are written concisely using equations. Reactants are placed on the left-hand side, products on the right, with a directional arrow pointing toward products.</span>
  </div>
</div>
<script>
window.setC10S4 = function(fmt) {
  ['pro', 'wor', 'ske'].forEach(b => {
    const el = document.getElementById('c10s4_btn_' + b);
    if(el) {
      if((fmt === 'prose' && b === 'pro') || (fmt === 'word' && b === 'wor') || (fmt === 'skeletal' && b === 'ske')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const disp = document.getElementById('c10s4_svg_display');
  const status = document.getElementById('c10s4_status');
  const str = document.getElementById('c10s4_str');
  const lhs = document.getElementById('c10s4_lhs');
  const rhs = document.getElementById('c10s4_rhs');
  const badge = document.getElementById('c10s4_badge');
  const desc = document.getElementById('c10s4_desc');

  if(fmt === 'prose') {
    status.textContent = "Format 1: Descriptive Prose • Long sentence format";
    str.textContent = "Full English Narrative";
    lhs.textContent = "Magnesium ribbon + Oxygen";
    rhs.textContent = "White ash of magnesium oxide";
    badge.textContent = "Descriptive Prose";
    desc.textContent = "Writing 'When magnesium ribbon is heated in air, it reacts with oxygen to form magnesium oxide' is lengthy. Chemical equations condense this into standardized symbolic shorthand.";
    disp.innerHTML = `
      <rect x="25" y="25" width="410" height="95" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
      <text x="230" y="55" fill="#f8fafc" font-size="9" text-anchor="middle">"When a cleaned strip of magnesium ribbon is heated in atmospheric air,"</text>
      <text x="230" y="75" fill="#f8fafc" font-size="9" text-anchor="middle">"it burns with a dazzling white flame to synthesize magnesium oxide powder."</text>
      <text x="230" y="100" fill="#f59e0b" font-size="8" font-weight="bold" text-anchor="middle">&rarr; Cumbersome for quantitative laboratory analysis</text>
    `;
  } else if(fmt === 'word') {
    status.textContent = "Format 2: Word Equation • Reactants (LHS) → Products (RHS)";
    str.textContent = "Condensed Word Equation";
    lhs.textContent = "Magnesium + Oxygen";
    rhs.textContent = "Magnesium oxide";
    badge.textContent = "Word Equation";
    desc.textContent = "A word equation condenses the chemical reaction: Reactants appear on the left (LHS) joined by '+', products on the right (RHS), connected by an arrow pointing towards the products.";
    disp.innerHTML = `
      <!-- LHS Reactants box -->
      <rect x="30" y="35" width="165" height="70" rx="8" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
      <text x="112" y="58" fill="#a7f3d0" font-size="7" font-weight="bold" text-anchor="middle">REACTANTS (LHS)</text>
      <text x="112" y="80" fill="#ecfdf5" font-size="11" font-weight="bold" text-anchor="middle">Magnesium + Oxygen</text>

      <!-- Center Arrow -->
      <path d="M 205,70 L 255,70" stroke="#f59e0b" stroke-width="3"/>
      <polygon points="255,65 267,70 255,75" fill="#f59e0b"/>
      <text x="233" y="60" fill="#fde047" font-size="7" text-anchor="middle">Yields</text>

      <!-- RHS Products box -->
      <rect x="275" y="35" width="155" height="70" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
      <text x="352" y="58" fill="#c7d2fe" font-size="7" font-weight="bold" text-anchor="middle">PRODUCTS (RHS)</text>
      <text x="352" y="80" fill="#e0e7ff" font-size="11" font-weight="bold" text-anchor="middle">Magnesium oxide</text>
    `;
  } else {
    status.textContent = "Format 3: Skeletal Equation • Mg + O2 → MgO (Unbalanced Atom Count)";
    str.textContent = "Skeletal Formula Equation";
    lhs.textContent = "1 Mg, 2 O atoms";
    rhs.textContent = "1 Mg, 1 O atom (Unbalanced)";
    badge.textContent = "Skeletal Equation";
    desc.textContent = "Replacing words with chemical formulas gives the skeletal equation: Mg + O2 -> MgO. It is unbalanced because the left side has 2 oxygen atoms while the right side has only 1 oxygen atom.";
    disp.innerHTML = `
      <rect x="40" y="35" width="140" height="75" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="110" y="60" fill="#fef08a" font-size="13" font-weight="bold" text-anchor="middle">Mg + O2</text>
      <text x="110" y="80" fill="#94a3b8" font-size="7" text-anchor="middle">1 Mg atom &bull; 2 O atoms</text>
      <text x="110" y="95" fill="#38bdf8" font-size="7" text-anchor="middle">Total Reactant Atoms: 3</text>

      <!-- Arrow -->
      <path d="M 195,72 L 250,72" stroke="#f59e0b" stroke-width="3"/>
      <polygon points="250,67 262,72 250,77" fill="#f59e0b"/>

      <rect x="275" y="35" width="145" height="75" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
      <text x="347" y="60" fill="#fda4af" font-size="13" font-weight="bold" text-anchor="middle">MgO</text>
      <text x="347" y="80" fill="#94a3b8" font-size="7" text-anchor="middle">1 Mg atom &bull; 1 O atom</text>
      <text x="347" y="95" fill="#f87171" font-size="7" font-weight="bold" text-anchor="middle">Missing 1 Oxygen! (Unbalanced)</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S4('prose'));
</script>""",

    5: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Conservation State:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC10S5('unbalanced')" id="c10s5_btn_unb" class="px-2.5 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition">Unbalanced (Violates)</button>
        <button onclick="setC10S5('balanced')" id="c10s5_btn_bal" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Balanced (Conserves Mass)</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s5_status">Lavoisier Principle: Mass of Reactants = Mass of Products</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Scale Pivot Fulcrum -->
        <polygon points="230,105 215,135 245,135" fill="#475569"/>
        <rect x="180" y="135" width="100" height="8" rx="2" fill="#334155"/>

        <!-- Dynamic Scale Beam -->
        <g id="c10s5_scale_beam"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Reactant Mass (LHS)</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c10s5_m1">56.3 g (Mg + O2)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Product Mass (RHS)</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c10s5_m2">40.3 g (MgO Only)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Mass Conservation</div>
        <div class="text-xs font-bold text-rose-400 mt-0.5" id="c10s5_law">Violated (-16 g)</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-emerald-950 border border-emerald-700/60 text-emerald-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s5_badge">Conservation Law</span>
    <span id="c10s5_desc">Antoine Lavoisier established that mass can neither be created nor destroyed in a chemical reaction. The number of atoms of each element must remain constant before and after a reaction.</span>
  </div>
</div>
<script>
window.setC10S5 = function(state) {
  const btnU = document.getElementById('c10s5_btn_unb');
  const btnB = document.getElementById('c10s5_btn_bal');
  const beam = document.getElementById('c10s5_scale_beam');
  const status = document.getElementById('c10s5_status');
  const m1 = document.getElementById('c10s5_m1');
  const m2 = document.getElementById('c10s5_m2');
  const law = document.getElementById('c10s5_law');
  const badge = document.getElementById('c10s5_badge');
  const desc = document.getElementById('c10s5_desc');

  if(state === 'unbalanced') {
    btnU.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition';
    btnB.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    status.textContent = "Unbalanced: Mg + O2 → MgO (Scale Tilted, Missing 1 Oxygen Atom)";
    m1.textContent = "56.3 g (Mg + O2)";
    m2.textContent = "40.3 g (MgO)";
    law.textContent = "Violated! (-16.0 g)";
    law.className = "text-xs font-bold text-rose-400 mt-0.5";
    badge.textContent = "Unbalanced";
    desc.textContent = "In the skeletal equation Mg + O2 -> MgO, two oxygen atoms enter on the left but only one emerges on the right. 16 grams of oxygen seemingly vanishes, violating the Law of Conservation of Mass!";
    beam.innerHTML = `
      <!-- Tilted Beam -->
      <line x1="80" y1="125" x2="380" y2="85" stroke="#ef4444" stroke-width="4"/>
      <!-- Left Pan (heavier) -->
      <line x1="100" y1="122" x2="100" y2="135" stroke="#94a3b8" stroke-width="2"/>
      <rect x="65" y="130" width="70" height="12" rx="3" fill="#065f46"/>
      <text x="100" y="140" fill="#a7f3d0" font-size="7" font-weight="bold" text-anchor="middle">LHS: Mg + O2</text>
      <!-- Right Pan (lighter) -->
      <line x1="360" y1="88" x2="360" y2="100" stroke="#94a3b8" stroke-width="2"/>
      <rect x="325" y="95" width="70" height="12" rx="3" fill="#991b1b"/>
      <text x="360" y="105" fill="#fda4af" font-size="7" font-weight="bold" text-anchor="middle">RHS: MgO (Lighter)</text>
      <text x="230" y="45" fill="#f87171" font-size="9" font-weight="bold" text-anchor="middle">Unbalanced: Violates Conservation of Mass</text>
    `;
  } else {
    btnU.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    btnB.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
    status.textContent = "Balanced: 2 Mg + O2 → 2 MgO (Level Balance, Mass Conserved)";
    m1.textContent = "80.6 g (2 Mg + O2)";
    m2.textContent = "80.6 g (2 MgO)";
    law.textContent = "Conserved! (Equal Mass)";
    law.className = "text-xs font-bold text-emerald-400 mt-0.5";
    badge.textContent = "Balanced (Conserved)";
    desc.textContent = "By placing coefficient 2 before Mg and MgO: 2Mg + O2 -> 2MgO. Two magnesium atoms and two oxygen atoms exist on both sides. Total mass of reactants equals total mass of products perfectly.";
    beam.innerHTML = `
      <!-- Level Beam -->
      <line x1="80" y1="105" x2="380" y2="105" stroke="#10b981" stroke-width="4"/>
      <!-- Left Pan -->
      <line x1="100" y1="105" x2="100" y2="120" stroke="#94a3b8" stroke-width="2"/>
      <rect x="60" y="120" width="80" height="15" rx="3" fill="#065f46" stroke="#10b981"/>
      <text x="100" y="131" fill="#ecfdf5" font-size="7" font-weight="bold" text-anchor="middle">2 Mg + O2 (80.6g)</text>
      <!-- Right Pan -->
      <line x1="360" y1="105" x2="360" y2="120" stroke="#94a3b8" stroke-width="2"/>
      <rect x="320" y="120" width="80" height="15" rx="3" fill="#065f46" stroke="#10b981"/>
      <text x="360" y="131" fill="#ecfdf5" font-size="7" font-weight="bold" text-anchor="middle">2 MgO (80.6g)</text>
      <text x="230" y="45" fill="#4ade80" font-size="9" font-weight="bold" text-anchor="middle">Perfect Mass Equilibrium (Lavoisier Principle)</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S5('unbalanced'));
</script>""",

    6: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Hit &amp; Trial Step:</span>
      <input type="range" min="1" max="7" value="3" step="1" id="c10s6_step" oninput="updateC10S6()" class="w-28 accent-amber-500 cursor-pointer">
      <span class="text-xs font-mono font-bold text-white" id="c10s6_step_lbl">Step 3: Balance O</span>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s6_status">Fe + H2O &rarr; Fe3O4 + H2</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Interactive Equation Display -->
        <g id="c10s6_eq_canvas"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Iron Atoms (LHS : RHS)</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c10s6_fe">1 : 3</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Hydrogen (LHS : RHS)</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c10s6_h">2 : 2</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Oxygen (LHS : RHS)</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c10s6_o">1 : 4</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-amber-950 border border-amber-700/60 text-amber-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s6_badge">Step 3</span>
    <span id="c10s6_desc">Balance the element with maximum atoms first: Oxygen has 4 in Fe3O4. Place coefficient 4 before H2O.</span>
  </div>
</div>
<script>
window.updateC10S6 = function() {
  const step = parseInt(document.getElementById('c10s6_step').value, 10);
  const lbl = document.getElementById('c10s6_step_lbl');
  const canvas = document.getElementById('c10s6_eq_canvas');
  const fe = document.getElementById('c10s6_fe');
  const h = document.getElementById('c10s6_h');
  const o = document.getElementById('c10s6_o');
  const badge = document.getElementById('c10s6_badge');
  const desc = document.getElementById('c10s6_desc');

  if(step === 1) {
    lbl.textContent = "Step 1: Box Formulas";
    badge.textContent = "Step 1: Formula Boxing";
    desc.textContent = "Draw boxes around each chemical formula. Never change subscripts or alter formulas inside the boxes.";
    fe.textContent = "1 : 3";
    h.textContent = "2 : 2";
    o.textContent = "1 : 4";
    canvas.innerHTML = `
      <rect x="50" y="45" width="45" height="40" rx="4" fill="#0f172a" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
      <text x="72" y="70" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Fe</text>
      <text x="110" y="70" fill="#f59e0b" font-size="14" font-weight="bold">+</text>
      <rect x="130" y="45" width="55" height="40" rx="4" fill="#0f172a" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
      <text x="157" y="70" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">H2O</text>
      <path d="M 200,65 L 245,65" stroke="#f59e0b" stroke-width="3"/>
      <rect x="260" y="45" width="70" height="40" rx="4" fill="#0f172a" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
      <text x="295" y="70" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Fe3O4</text>
      <text x="345" y="70" fill="#f59e0b" font-size="14" font-weight="bold">+</text>
      <rect x="365" y="45" width="50" height="40" rx="4" fill="#0f172a" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
      <text x="390" y="70" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">H2</text>
      <text x="230" y="115" fill="#fde047" font-size="8" text-anchor="middle">Boxes protect internal formula subscripts from modification</text>
    `;
  } else if(step === 2) {
    lbl.textContent = "Step 2: Count Atoms";
    badge.textContent = "Step 2: Atom Inventory";
    desc.textContent = "List the number of atoms of each element present in reactants (LHS) and products (RHS).";
    fe.textContent = "1 : 3 (Deficit)";
    h.textContent = "2 : 2 (Equal)";
    o.textContent = "1 : 4 (Deficit)";
    canvas.innerHTML = `
      <rect x="110" y="25" width="240" height="95" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="230" y="45" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">Initial Atom Inventory Table</text>
      <text x="140" y="68" fill="#e2e8f0" font-size="8">Element</text>
      <text x="210" y="68" fill="#e2e8f0" font-size="8">Reactants (LHS)</text>
      <text x="300" y="68" fill="#e2e8f0" font-size="8">Products (RHS)</text>
      <line x1="120" y1="73" x2="340" y2="73" stroke="#475569"/>
      <text x="140" y="88" fill="#cbd5e1" font-size="8">Iron (Fe)</text><text x="230" y="88" fill="#f87171" font-size="8">1</text><text x="320" y="88" fill="#4ade80" font-size="8">3</text>
      <text x="140" y="102" fill="#cbd5e1" font-size="8">Hydrogen (H)</text><text x="230" y="102" fill="#4ade80" font-size="8">2</text><text x="320" y="102" fill="#4ade80" font-size="8">2</text>
      <text x="140" y="115" fill="#cbd5e1" font-size="8">Oxygen (O)</text><text x="230" y="115" fill="#f87171" font-size="8">1</text><text x="320" y="115" fill="#4ade80" font-size="8">4</text>
    `;
  } else if(step === 3) {
    lbl.textContent = "Step 3: Balance Oxygen";
    badge.textContent = "Step 3: Balance Max Atom (O)";
    desc.textContent = "Oxygen has 4 atoms on RHS (in Fe3O4). Place coefficient 4 before H2O: Fe + 4H2O -> Fe3O4 + H2.";
    fe.textContent = "1 : 3";
    h.textContent = "8 : 2 (Now 8 on LHS)";
    o.textContent = "4 : 4 (Balanced!)";
    canvas.innerHTML = `
      <text x="70" y="70" fill="#94a3b8" font-size="12" font-weight="bold">Fe +</text>
      <rect x="100" y="45" width="20" height="30" rx="3" fill="#047857"/>
      <text x="110" y="66" fill="#ecfdf5" font-size="12" font-weight="bold" text-anchor="middle">4</text>
      <text x="140" y="70" fill="#ffffff" font-size="12" font-weight="bold">H2O &rarr; Fe3O4 + H2</text>
      <text x="230" y="110" fill="#4ade80" font-size="9" font-weight="bold" text-anchor="middle">Oxygen atoms are now balanced: 4 on LHS = 4 on RHS</text>
    `;
  } else if(step === 4) {
    lbl.textContent = "Step 4: Balance Hydrogen";
    badge.textContent = "Step 4: Balance H";
    desc.textContent = "LHS now has 4x2 = 8 Hydrogen atoms. Balance RHS by placing coefficient 4 before H2: Fe + 4H2O -> Fe3O4 + 4H2.";
    fe.textContent = "1 : 3";
    h.textContent = "8 : 8 (Balanced!)";
    o.textContent = "4 : 4 (Balanced!)";
    canvas.innerHTML = `
      <text x="70" y="70" fill="#94a3b8" font-size="12" font-weight="bold">Fe +</text>
      <text x="105" y="70" fill="#4ade80" font-size="12" font-weight="bold">4H2O &rarr; Fe3O4 +</text>
      <rect x="280" y="45" width="20" height="30" rx="3" fill="#047857"/>
      <text x="290" y="66" fill="#ecfdf5" font-size="12" font-weight="bold" text-anchor="middle">4</text>
      <text x="315" y="70" fill="#ffffff" font-size="12" font-weight="bold">H2</text>
      <text x="230" y="110" fill="#4ade80" font-size="9" font-weight="bold" text-anchor="middle">Hydrogen atoms balanced: 8 on LHS = 8 on RHS</text>
    `;
  } else if(step === 5) {
    lbl.textContent = "Step 5: Balance Iron";
    badge.textContent = "Step 5: Balance Fe";
    desc.textContent = "RHS has 3 Iron atoms in Fe3O4. Place coefficient 3 before Fe on the LHS: 3Fe + 4H2O -> Fe3O4 + 4H2.";
    fe.textContent = "3 : 3 (Balanced!)";
    h.textContent = "8 : 8 (Balanced!)";
    o.textContent = "4 : 4 (Balanced!)";
    canvas.innerHTML = `
      <rect x="50" y="45" width="20" height="30" rx="3" fill="#047857"/>
      <text x="60" y="66" fill="#ecfdf5" font-size="12" font-weight="bold" text-anchor="middle">3</text>
      <text x="180" y="70" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">Fe + 4H2O &rarr; Fe3O4 + 4H2</text>
      <text x="230" y="110" fill="#4ade80" font-size="9" font-weight="bold" text-anchor="middle">Iron atoms balanced: 3 on LHS = 3 on RHS</text>
    `;
  } else if(step === 6) {
    lbl.textContent = "Step 6: Verify Counts";
    badge.textContent = "Step 6: Atom Verification";
    desc.textContent = "Check atom counts on both sides: 3 Fe, 8 H, and 4 O. The equation is correctly and fully balanced!";
    fe.textContent = "3 : 3 (Equal)";
    h.textContent = "8 : 8 (Equal)";
    o.textContent = "4 : 4 (Equal)";
    canvas.innerHTML = `
      <rect x="40" y="30" width="380" height="85" rx="8" fill="#065f46" stroke="#10b981" stroke-width="2"/>
      <text x="230" y="65" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">3Fe + 4H2O &rarr; Fe3O4 + 4H2</text>
      <text x="230" y="90" fill="#a7f3d0" font-size="9" text-anchor="middle">Fe: 3 = 3 &bull; H: 8 = 8 &bull; O: 4 = 4 (All Conserved)</text>
    `;
  } else {
    lbl.textContent = "Step 7: Physical States";
    badge.textContent = "Step 7: State Notations";
    desc.textContent = "Add physical states: 3Fe(s) + 4H2O(g) -> Fe3O4(s) + 4H2(g). H2O(g) indicates water used in the form of steam.";
    fe.textContent = "3 Fe (Solid)";
    h.textContent = "8 H (Gas)";
    o.textContent = "4 O (Oxide Solid)";
    canvas.innerHTML = `
      <rect x="30" y="25" width="400" height="95" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
      <text x="230" y="60" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">3Fe(s) + 4H2O(g) &rarr; Fe3O4(s) + 4H2(g)</text>
      <text x="230" y="85" fill="#a5b4fc" font-size="8" text-anchor="middle">(s) = solid &bull; (g) = gas (steam) &bull; (l) = liquid &bull; (aq) = aqueous</text>
      <text x="230" y="105" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Reaction conditions (temp, pressure, catalyst) written above/below arrow</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', updateC10S6);
</script>""",

    7: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Combination Example:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC10S7('coal')" id="c10s7_btn_coa" class="px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition">Burning Coal (C + O2)</button>
        <button onclick="setC10S7('water')" id="c10s7_btn_wat" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Water (2H2 + O2)</button>
        <button onclick="setC10S7('concept')" id="c10s7_btn_con" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">General Rule: A + B &rarr; AB</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s7_status">C(s) + O2(g) &rarr; CO2(g) &bull; Single Product</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <g id="c10s7_svg_canvas"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Reactant Count</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c10s7_r">2 Distinct Reactants</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Product Count</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c10s7_p">Exactly 1 Product</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Energetics</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c10s7_e">Exothermic Heat Output</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-emerald-950 border border-emerald-700/60 text-emerald-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s7_badge">Combination</span>
    <span id="c10s7_desc">A combination reaction unites two or more reactants into a single product. Coal combustion and water formation both synthesize one compound from elemental reactants.</span>
  </div>
</div>
<script>
window.setC10S7 = function(mode) {
  ['coa', 'wat', 'con'].forEach(b => {
    const el = document.getElementById('c10s7_btn_' + b);
    if(el) {
      if((mode === 'coal' && b === 'coa') || (mode === 'water' && b === 'wat') || (mode === 'concept' && b === 'con')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const canvas = document.getElementById('c10s7_svg_canvas');
  const status = document.getElementById('c10s7_status');
  const r = document.getElementById('c10s7_r');
  const p = document.getElementById('c10s7_p');
  const e = document.getElementById('c10s7_e');
  const badge = document.getElementById('c10s7_badge');
  const desc = document.getElementById('c10s7_desc');

  if(mode === 'coal') {
    status.textContent = "Coal Combustion: C(s) + O2(g) → CO2(g) + Thermal Energy";
    r.textContent = "Carbon(s) + Oxygen(g)";
    p.textContent = "1 Product: CO2(g)";
    e.textContent = "Exothermic Burning";
    badge.textContent = "Coal Combustion";
    desc.textContent = "Solid coal (carbon) burns in oxygen gas from air to yield a single chemical compound, carbon dioxide gas. The reaction discharges immense thermal energy.";
    canvas.innerHTML = `
      <rect x="50" y="45" width="50" height="50" rx="4" fill="#1c1917" stroke="#475569" stroke-width="2"/>
      <text x="75" y="74" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">C (Solid)</text>
      <text x="125" y="74" fill="#f59e0b" font-size="16" font-weight="bold" text-anchor="middle">+</text>
      <circle cx="170" cy="70" r="22" fill="#0284c7" opacity="0.6"/>
      <text x="170" y="74" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">O2 (Gas)</text>
      <path d="M 215,70 L 265,70" stroke="#f59e0b" stroke-width="3"/>
      <polygon points="265,65 277,70 265,75" fill="#f59e0b"/>
      <rect x="290" y="35" width="130" height="70" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
      <text x="355" y="65" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">CO2 (Gas)</text>
      <text x="355" y="85" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">+ Heat Energy</text>
    `;
  } else if(mode === 'water') {
    status.textContent = "Water Synthesis: 2 H2(g) + O2(g) → 2 H2O(l)";
    r.textContent = "2 H2(g) + 1 O2(g)";
    p.textContent = "1 Product: 2 H2O(l)";
    e.textContent = "Explosive Energy Output";
    badge.textContent = "Water Synthesis";
    desc.textContent = "Two molecules of hydrogen gas combine with one molecule of oxygen gas to synthesize two molecules of liquid water: 2H2 + O2 -> 2H2O. Multiple reactants yield one single compound.";
    canvas.innerHTML = `
      <circle cx="65" cy="70" r="18" fill="#3b82f6" opacity="0.7"/>
      <circle cx="95" cy="70" r="18" fill="#3b82f6" opacity="0.7"/>
      <text x="80" y="74" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">2 H2 (g)</text>
      <text x="135" y="74" fill="#f59e0b" font-size="16" font-weight="bold" text-anchor="middle">+</text>
      <circle cx="175" cy="70" r="22" fill="#ef4444" opacity="0.7"/>
      <text x="175" y="74" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">O2 (g)</text>
      <path d="M 220,70 L 270,70" stroke="#f59e0b" stroke-width="3"/>
      <polygon points="270,65 282,70 270,75" fill="#f59e0b"/>
      <rect x="300" y="35" width="125" height="70" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
      <text x="362" y="65" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">2 H2O (Liquid)</text>
      <text x="362" y="85" fill="#a7f3d0" font-size="8" font-weight="bold" text-anchor="middle">Single Liquid Compound</text>
    `;
  } else {
    status.textContent = "General Combination Principle: A + B → AB";
    r.textContent = "Multiple Reactants";
    p.textContent = "Single United Product";
    e.textContent = "Bond Formation Favorable";
    badge.textContent = "General Principle";
    desc.textContent = "Any chemical process where two or more chemical species unite to form exactly one product compound is classified as a combination reaction: A + B -> AB.";
    canvas.innerHTML = `
      <rect x="40" y="40" width="60" height="60" rx="8" fill="#065f46" stroke="#10b981" stroke-width="2"/>
      <text x="70" y="75" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">A</text>
      <text x="130" y="75" fill="#f59e0b" font-size="18" font-weight="bold" text-anchor="middle">+</text>
      <rect x="160" y="40" width="60" height="60" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
      <text x="190" y="75" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">B</text>
      <path d="M 245,70 L 295,70" stroke="#f59e0b" stroke-width="3"/>
      <polygon points="295,65 307,70 295,75" fill="#f59e0b"/>
      <rect x="325" y="35" width="105" height="70" rx="8" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
      <text x="377" y="75" fill="#ffffff" font-size="18" font-weight="bold" text-anchor="middle">AB</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S7('coal'));
</script>""",

    8: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Lime Phase:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC10S8('hydrate')" id="c10s8_btn_hyd" class="px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">1. Quicklime Hydration</button>
        <button onclick="setC10S8('paint')" id="c10s8_btn_pai" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">2. Wall Painting</button>
        <button onclick="setC10S8('marble')" id="c10s8_btn_mar" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">3. Shiny Marble (CaCO3)</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c10s8_status">Activity 1.4: CaO + H2O &rarr; Ca(OH)2 + Boiling Heat</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <g id="c10s8_svg_canvas"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Calcium Species</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c10s8_sp">Quicklime (CaO)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Reaction Partner</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c10s8_rp">Liquid Water (H2O)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Product &amp; Heat</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c10s8_ph">Ca(OH)2 + Heat</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-amber-950 border border-amber-700/60 text-amber-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c10s8_badge">Quicklime Hydration</span>
    <span id="c10s8_desc">Calcium oxide combines vigorously with water to form calcium hydroxide (slaked lime), releasing tremendous heat. Applied on walls, it absorbs atmospheric CO2 over 2-3 days to form shiny calcium carbonate.</span>
  </div>
</div>
<script>
window.setC10S8 = function(phase) {
  ['hyd', 'pai', 'mar'].forEach(b => {
    const el = document.getElementById('c10s8_btn_' + b);
    if(el) {
      if((phase === 'hydrate' && b === 'hyd') || (phase === 'paint' && b === 'pai') || (phase === 'marble' && b === 'mar')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const canvas = document.getElementById('c10s8_svg_canvas');
  const status = document.getElementById('c10s8_status');
  const sp = document.getElementById('c10s8_sp');
  const rp = document.getElementById('c10s8_rp');
  const ph = document.getElementById('c10s8_ph');
  const badge = document.getElementById('c10s8_badge');
  const desc = document.getElementById('c10s8_desc');

  if(phase === 'hydrate') {
    status.textContent = "Activity 1.4: Quicklime (CaO) + Water → Slaked Lime Ca(OH)2 + Violent Boiling Heat";
    sp.textContent = "Quicklime: CaO(s)";
    rp.textContent = "Water: H2O(l)";
    ph.textContent = "Ca(OH)2 + Boiling Heat";
    badge.textContent = "1. Hydration";
    desc.textContent = "Adding water to solid quicklime triggers a violent, hissing combination reaction. Immense heat boils the water, yielding a suspension of slaked lime: CaO + H2O -> Ca(OH)2 + Heat.";
    canvas.innerHTML = `
      <!-- Beaker -->
      <rect x="70" y="30" width="70" height="90" rx="4" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
      <rect x="72" y="70" width="66" height="48" fill="#0284c7" opacity="0.4"/>
      <!-- Quicklime chunks -->
      <circle cx="95" cy="105" r="8" fill="#e2e8f0"/>
      <circle cx="115" cy="108" r="7" fill="#e2e8f0"/>
      <!-- Steam vapors & hissing -->
      <path d="M 90,65 Q 85,50 90,40" stroke="#f59e0b" stroke-width="2" fill="none"/>
      <path d="M 115,65 Q 120,50 115,40" stroke="#f59e0b" stroke-width="2" fill="none"/>
      <text x="105" y="30" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Hissing Boiling Heat!</text>
      <!-- Arrow -->
      <path d="M 160,75 L 210,75" stroke="#f59e0b" stroke-width="3"/>
      <!-- Slaked Lime result -->
      <rect x="230" y="30" width="190" height="90" rx="8" fill="#065f46" stroke="#10b981" stroke-width="2"/>
      <text x="325" y="55" fill="#a7f3d0" font-size="8" font-weight="bold" text-anchor="middle">Slaked Lime Suspension</text>
      <text x="325" y="75" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Ca(OH)2 (Aqueous)</text>
      <text x="325" y="95" fill="#fef08a" font-size="8" text-anchor="middle">Intensely Exothermic Combination</text>
    `;
  } else if(phase === 'paint') {
    status.textContent = "Whitewashing: Painting aqueous Ca(OH)2 paste onto masonry walls";
    sp.textContent = "Slaked Lime Coating";
    rp.textContent = "Ambient CO2 Gas";
    ph.textContent = "Begins Atmospheric Carbonation";
    badge.textContent = "2. Wall Application";
    desc.textContent = "Clear slaked lime solution is painted onto walls. Initially dull, it begins absorbing trace carbon dioxide gas from surrounding air to start building a mineral crust.";
    canvas.innerHTML = `
      <!-- Wall Bricks -->
      <rect x="50" y="30" width="120" height="90" rx="4" fill="#78350f" stroke="#b45309" stroke-width="1.5"/>
      <line x1="50" y1="60" x2="170" y2="60" stroke="#451a03"/>
      <line x1="50" y1="90" x2="170" y2="90" stroke="#451a03"/>
      <!-- Wet Slaked Lime Layer -->
      <rect x="170" y="30" width="20" height="90" fill="#cbd5e1" opacity="0.8"/>
      <text x="180" y="25" fill="#94a3b8" font-size="7" text-anchor="middle">Wet Ca(OH)2</text>
      <!-- Atmospheric CO2 arrows -->
      <path d="M 280,50 L 200,50" stroke="#38bdf8" stroke-width="2.5"/>
      <path d="M 280,85 L 200,85" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="300" y="70" fill="#7dd3fc" font-size="9" font-weight="bold">Atmospheric CO2</text>
      <text x="350" y="105" fill="#fde047" font-size="8">Slow 2-3 Day Carbonation</text>
    `;
  } else {
    status.textContent = "After 2-3 Days: Ca(OH)2 + CO2 → CaCO3 (Sparkling Marble Sheen)";
    sp.textContent = "Calcium Carbonate (CaCO3)";
    rp.textContent = "Limestone / Marble Crust";
    ph.textContent = "Shiny Hard White Finish";
    badge.textContent = "3. Marble Finish";
    desc.textContent = "Over 2 to 3 days, slaked lime reacts fully with atmospheric carbon dioxide: Ca(OH)2 + CO2 -> CaCO3 + H2O. Solid calcium carbonate forms a hard, gleaming, weather-resistant finish chemically identical to marble.";
    canvas.innerHTML = `
      <rect x="50" y="25" width="370" height="95" rx="8" fill="#1e293b" stroke="#e2e8f0" stroke-width="2"/>
      <!-- Sparkling Marble finish -->
      <rect x="70" y="40" width="110" height="65" rx="4" fill="#f8fafc" filter="drop-shadow(0 0 8px #ffffff)"/>
      <polygon points="125,50 128,58 136,60 128,62 125,70 122,62 114,60 122,58" fill="#facc15"/>
      <text x="125" y="85" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">Shiny CaCO3</text>
      <!-- Equation callout -->
      <text x="290" y="55" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Ca(OH)2 + CO2 &rarr; CaCO3 + H2O</text>
      <text x="290" y="75" fill="#fde047" font-size="8" text-anchor="middle">Forms Sparkling Calcium Carbonate</text>
      <text x="290" y="95" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">Chemically Identical to Natural Marble!</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC10S8('hydrate'));
</script>"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part1)} simulators for Part 1 (Slides 1-8).")
