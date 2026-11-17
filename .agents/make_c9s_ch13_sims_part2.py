#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 9 Science Chapter 13 Simulators (Part 2: Slides 9-16)
High-fidelity responsive SVG interactive laboratory widgets for Earth as a System: Energy, Matter, and Life.
"""

sims_part2 = {
    9: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-sky-400 uppercase tracking-wider">Circulation Cell:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC13S9('hadley')" id="c13s9_btn_had" class="px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition">Hadley Cell (0&deg;-30&deg;)</button>
        <button onclick="setC13S9('ferrel')" id="c13s9_btn_fer" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Ferrel Cell (30&deg;-60&deg;)</button>
        <button onclick="setC13S9('polar')" id="c13s9_btn_pol" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Polar Cell (60&deg;-90&deg;)</button>
        <button onclick="setC13S9('coriolis')" id="c13s9_btn_cor" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Coriolis Effect</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s9_status">Trade Winds &bull; Equatorial Low to Subtropical High</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Earth Profile Half Arc -->
        <path d="M 50,135 A 140,140 0 0,1 50,10" fill="none" stroke="#38bdf8" stroke-width="2"/>
        
        <!-- Latitude markers -->
        <text x="25" y="138" fill="#fde047" font-size="7" font-weight="bold">0&deg; Eq</text>
        <text x="20" y="95" fill="#bae6fd" font-size="7">30&deg; N</text>
        <text x="20" y="55" fill="#bae6fd" font-size="7">60&deg; N</text>
        <text x="25" y="15" fill="#fde047" font-size="7" font-weight="bold">90&deg; NP</text>

        <!-- Dynamic Cell Visualization -->
        <g id="c13s9_cell_graphics"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Pressure Belt</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c13s9_pres">Equatorial Low (ITCZ)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Prevailing Wind</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c13s9_wind">NE Trade Winds</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Coriolis Deflection</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s9_cor">Right in North / Left in South</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-sky-950 border border-sky-700/60 text-sky-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c13s9_badge">Planetary Winds</span>
    <span id="c13s9_desc">Hadley cells lift warm moist air at the equator and sink cool dry air at 30&deg; latitudes. Earth's rotation introduces the Coriolis force, deflecting winds to the right in the Northern Hemisphere.</span>
  </div>
</div>
<script>
window.setC13S9 = function(cell) {
  ['had', 'fer', 'pol', 'cor'].forEach(c => {
    const el = document.getElementById('c13s9_btn_' + c);
    if(el) {
      if((cell === 'hadley' && c === 'had') || (cell === 'ferrel' && c === 'fer') || (cell === 'polar' && c === 'pol') || (cell === 'coriolis' && c === 'cor')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const gfx = document.getElementById('c13s9_cell_graphics');
  const status = document.getElementById('c13s9_status');
  const pres = document.getElementById('c13s9_pres');
  const wind = document.getElementById('c13s9_wind');
  const cor = document.getElementById('c13s9_cor');
  const badge = document.getElementById('c13s9_badge');
  const desc = document.getElementById('c13s9_desc');

  if(cell === 'hadley') {
    status.textContent = "Hadley Cell (0°-30°) • NE Trade Winds & Doldrums";
    pres.textContent = "Equatorial Low (ITCZ)";
    wind.textContent = "Northeast Trade Winds";
    cor.textContent = "Deflected Westward";
    badge.textContent = "Hadley Cell";
    desc.textContent = "Intense solar heating at the equator causes warm air to ascend, forming the Intertropical Convergence Zone (ITCZ). Air flows poleward aloft, cools, sinks at 30° N/S (subtropical highs), and returns as trade winds.";
    gfx.innerHTML = `
      <ellipse cx="140" cy="115" rx="55" ry="18" fill="none" stroke="#22c55e" stroke-width="2" stroke-dasharray="4,2"/>
      <text x="140" y="118" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">Hadley Cell (0&deg;-30&deg;)</text>
      <!-- Trade winds arrow -->
      <path d="M 170,128 L 80,132" stroke="#f59e0b" stroke-width="2.5"/>
      <text x="210" y="132" fill="#fde68a" font-size="7">NE Trade Winds</text>
      <text x="260" y="90" fill="#93c5fd" font-size="7">Subtropical High (30&deg;)</text>
      <circle cx="240" cy="95" r="3" fill="#38bdf8"/>
    `;
  } else if(cell === 'ferrel') {
    status.textContent = "Ferrel Cell (30°-60°) • Mid-Latitude Westerlies";
    pres.textContent = "Subpolar Low (60° N)";
    wind.textContent = "Prevailing Westerlies";
    cor.textContent = "Deflected Eastward";
    badge.textContent = "Ferrel Cell";
    desc.textContent = "The Ferrel cell operates like a reverse mechanical gear between the Hadley and Polar cells. Surface winds flow poleward from 30° to 60° and are deflected by Coriolis into strong prevailing westerlies.";
    gfx.innerHTML = `
      <ellipse cx="130" cy="75" rx="50" ry="18" fill="none" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4,2"/>
      <text x="130" y="78" fill="#93c5fd" font-size="8" font-weight="bold" text-anchor="middle">Ferrel Cell (30&deg;-60&deg;)</text>
      <!-- Westerlies arrow -->
      <path d="M 80,88 L 160,68" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="210" y="70" fill="#bae6fd" font-size="7">Prevailing Westerlies</text>
    `;
  } else if(cell === 'polar') {
    status.textContent = "Polar Cell (60°-90°) • Polar Easterlies & Cold High";
    pres.textContent = "Polar High (90° N)";
    wind.textContent = "Polar Easterlies";
    cor.textContent = "Deflected Westward";
    badge.textContent = "Polar Cell";
    desc.textContent = "Extreme radiative cooling at the poles creates dense, sinking air (polar high). This air surges equatorward toward 60° latitude, deflected by Coriolis to form the bitterly cold polar easterlies.";
    gfx.innerHTML = `
      <ellipse cx="110" cy="35" rx="40" ry="15" fill="none" stroke="#a855f7" stroke-width="2" stroke-dasharray="4,2"/>
      <text x="110" y="38" fill="#d8b4fe" font-size="8" font-weight="bold" text-anchor="middle">Polar Cell (60&deg;-90&deg;)</text>
      <!-- Polar Easterlies arrow -->
      <path d="M 120,25 L 70,45" stroke="#c084fc" stroke-width="2.5"/>
      <text x="200" y="35" fill="#e9d5ff" font-size="7">Polar Easterlies</text>
    `;
  } else {
    status.textContent = "Coriolis Force • Right in North, Left in South Hemisphere";
    pres.textContent = "Inertial Deflection";
    wind.textContent = "Right Deflection (North)";
    cor.textContent = "Proportional to 2Ω sin(φ)";
    badge.textContent = "Coriolis Effect";
    desc.textContent = "Because Earth rotates fastest at the equator (1670 km/h) and zero at the poles, moving parcels of air conserve angular momentum, deflecting to their right in the Northern Hemisphere and left in the Southern Hemisphere.";
    gfx.innerHTML = `
      <line x1="80" y1="120" x2="80" y2="30" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3"/>
      <path d="M 80,120 Q 95,75 140,40" stroke="#f59e0b" stroke-width="3" fill="none"/>
      <text x="90" y="115" fill="#94a3b8" font-size="7">Straight Inertial Target</text>
      <text x="145" y="42" fill="#fde047" font-size="8" font-weight="bold">Deflected Path (Right)</text>
      <text x="250" y="60" fill="#fef08a" font-size="8">Northern Hemisphere: Clockwise Deflection</text>
      <text x="250" y="80" fill="#38bdf8" font-size="8">Southern Hemisphere: Counter-Clockwise</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC13S9('hadley'));
</script>""",

    10: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-sky-400 uppercase tracking-wider">Oceanic System:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC13S10('gyre_n')" id="c13s10_btn_gn" class="px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition">North Atlantic Gyre</button>
        <button onclick="setC13S10('stream')" id="c13s10_btn_str" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Gulf Stream &amp; Drift</button>
        <button onclick="setC13S10('iitm')" id="c13s10_btn_iit" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">IITM Pune Monsoon</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s10_status">Clockwise Subtropical Gyre &bull; North Atlantic Thermal Conveyor</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Ocean Base Grid -->
        <rect x="0" y="0" width="460" height="145" fill="#082f49" opacity="0.6"/>
        
        <g id="c13s10_ocean_graphics"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Current / Model</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c13s10_val1">North Atlantic Gyre</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Flow Rotation</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c13s10_val2">Clockwise Gyre</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Climate Influence</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s10_val3">Warms NW Europe</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-sky-950 border border-sky-700/60 text-sky-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c13s10_badge">Ocean Currents</span>
    <span id="c13s10_desc">Wind stress and Earth's Coriolis deflection drive massive circular ocean gyres—clockwise in the Northern Hemisphere and counter-clockwise in the Southern. The warm Gulf Stream keeps northwestern European ports ice-free in winter.</span>
  </div>
</div>
<script>
window.setC13S10 = function(mode) {
  ['gn', 'str', 'iit'].forEach(m => {
    const el = document.getElementById('c13s10_btn_' + m);
    if(el) {
      if((mode === 'gyre_n' && m === 'gn') || (mode === 'stream' && m === 'str') || (mode === 'iitm' && m === 'iit')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const gfx = document.getElementById('c13s10_ocean_graphics');
  const status = document.getElementById('c13s10_status');
  const v1 = document.getElementById('c13s10_val1');
  const v2 = document.getElementById('c13s10_val2');
  const v3 = document.getElementById('c13s10_val3');
  const badge = document.getElementById('c13s10_badge');
  const desc = document.getElementById('c13s10_desc');

  if(mode === 'gyre_n') {
    status.textContent = "North Atlantic Gyre • Clockwise Circulation & Coriolis Balance";
    v1.textContent = "North Atlantic Basin";
    v2.textContent = "Clockwise Gyre";
    v3.textContent = "Transports Tropical Heat";
    badge.textContent = "Subtropical Gyres";
    desc.textContent = "Ocean gyres are vast circular current systems driven by trade winds, mid-latitude westerlies, and Coriolis deflection. In the Northern Hemisphere, gyres rotate clockwise; in the Southern Hemisphere, counter-clockwise.";
    gfx.innerHTML = `
      <ellipse cx="230" cy="72" rx="140" ry="50" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6,4"/>
      <polygon points="360,65 372,72 360,79" fill="#38bdf8"/>
      <polygon points="100,79 88,72 100,65" fill="#38bdf8"/>
      <text x="230" y="65" fill="#e0f2fe" font-size="10" font-weight="bold" text-anchor="middle">Clockwise Subtropical Gyre</text>
      <text x="230" y="82" fill="#7dd3fc" font-size="8" text-anchor="middle">Wind Stress + Coriolis Deflection Balance</text>
    `;
  } else if(mode === 'stream') {
    status.textContent = "Gulf Stream & North Atlantic Drift • Heat Delivery to NW Europe";
    v1.textContent = "Gulf Stream Drift";
    v2.textContent = "Warm Western Boundary";
    v3.textContent = "Ice-Free Ports in UK/Norway";
    badge.textContent = "Gulf Stream System";
    desc.textContent = "Originating in the Gulf of Mexico, the warm Gulf Stream carries enormous thermal energy northeast across the Atlantic as the North Atlantic Drift, moderating coastal European climates by up to 10 &deg;C.";
    gfx.innerHTML = `
      <path d="M 60,120 Q 140,80 240,60 T 390,30" stroke="#f43f5e" stroke-width="4" fill="none"/>
      <text x="110" y="115" fill="#fda4af" font-size="8" font-weight="bold">Warm Gulf Stream</text>
      <text x="320" y="25" fill="#fecdd3" font-size="8" font-weight="bold">North Atlantic Drift &rarr; UK/Norway</text>
      <circle cx="390" cy="30" r="5" fill="#f43f5e"/>
    `;
  } else {
    status.textContent = "IITM Pune Pratyush & Mihir • Coupled Ocean-Atmosphere Monsoon Forecast";
    v1.textContent = "IITM Pune Coupled Model";
    v2.textContent = "Atmosphere + Ocean";
    v3.textContent = "Indian Monsoon Prediction";
    badge.textContent = "IITM Pune Supercomputer";
    desc.textContent = "The Indian Institute of Tropical Meteorology (IITM) in Pune utilizes coupled ocean-atmosphere models on petascale supercomputers to simulate sea-surface temperatures across the Arabian Sea and Bay of Bengal for accurate monsoon forecasts.";
    gfx.innerHTML = `
      <rect x="140" y="20" width="180" height="105" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
      <text x="230" y="45" fill="#e0e7ff" font-size="9" font-weight="bold" text-anchor="middle">IITM Pune Supercomputing</text>
      <text x="230" y="65" fill="#a5b4fc" font-size="8" text-anchor="middle">Coupled Ocean-Atmosphere Model</text>
      <text x="230" y="85" fill="#38bdf8" font-size="8" text-anchor="middle">Arabian Sea &amp; Bay of Bengal SST</text>
      <text x="230" y="105" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">Monsoon Onset &amp; Rainfall Forecast</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC13S10('gyre_n'));
</script>""",

    11: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-sky-400 uppercase tracking-wider">Hydrological Stage:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC13S11('evap')" id="c13s11_btn_eva" class="px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition">Evaporation</button>
        <button onclick="setC13S11('cond')" id="c13s11_btn_con" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Condensation</button>
        <button onclick="setC13S11('prec')" id="c13s11_btn_pre" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Precipitation</button>
        <button onclick="setC13S11('glacier')" id="c13s11_btn_gla" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Himalayan Glaciers</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s11_status">Ocean Evaporation &bull; Solar-Driven Phase Change</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Mountain left, plain center, ocean right -->
        <polygon points="0,140 70,35 150,140" fill="#334155"/>
        <rect x="130" y="115" width="160" height="30" fill="#14532d"/>
        <rect x="280" y="105" width="180" height="40" fill="#0369a1"/>
        <text x="370" y="130" fill="#e0f2fe" font-size="8" font-weight="bold" text-anchor="middle">Arabian Sea / Bay of Bengal</text>
        <text x="70" y="30" fill="#f8fafc" font-size="7" font-weight="bold" text-anchor="middle">Himalayas</text>

        <!-- Hydrological Dynamics -->
        <g id="c13s11_dynamic"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Thermodynamic Phase</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c13s11_phase">Liquid &rarr; Vapor (Latent Heat)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Driver / Mechanism</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c13s11_driver">Solar Insolation Influx</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Indian Climate Impact</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s11_impact">Monsoon Moisture Surge</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-sky-950 border border-sky-700/60 text-sky-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c13s11_badge">The Water Cycle</span>
    <span id="c13s11_desc">Water circulates continuously between ocean, atmosphere, and land via evaporation, condensation, precipitation, and runoff. Himalayan glaciers act as natural freshwater storage towers, sustaining perennial river flow.</span>
  </div>
</div>
<script>
window.setC13S11 = function(stage) {
  ['eva', 'con', 'pre', 'gla'].forEach(s => {
    const el = document.getElementById('c13s11_btn_' + s);
    if(el) {
      if((stage === 'evap' && s === 'eva') || (stage === 'cond' && s === 'con') || (stage === 'prec' && s === 'pre') || (stage === 'glacier' && s === 'gla')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const dyn = document.getElementById('c13s11_dynamic');
  const status = document.getElementById('c13s11_status');
  const phase = document.getElementById('c13s11_phase');
  const driver = document.getElementById('c13s11_driver');
  const impact = document.getElementById('c13s11_impact');
  const badge = document.getElementById('c13s11_badge');
  const desc = document.getElementById('c13s11_desc');

  if(stage === 'evap') {
    status.textContent = "Evaporation & Transpiration • Solar Absorption & Vapor Ascent";
    phase.textContent = "Liquid → Vapor (Latent Heat)";
    driver.textContent = "Solar Insolation Influx";
    impact.textContent = "Monsoon Ocean Evaporation";
    badge.textContent = "Evaporation";
    desc.textContent = "Solar heating evaporates ocean water and powers vegetative transpiration. Ascending vapor stores latent heat of vaporization, which fuels massive monsoon convective storm systems.";
    dyn.innerHTML = `
      <path d="M 330,105 Q 340,75 350,55" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3" fill="none"/>
      <path d="M 370,105 Q 380,75 390,55" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3" fill="none"/>
      <path d="M 200,115 Q 210,85 220,60" stroke="#4ade80" stroke-width="2" stroke-dasharray="3,3" fill="none"/>
      <text x="360" y="48" fill="#bae6fd" font-size="7">Ocean Evaporation</text>
      <text x="210" y="52" fill="#86efac" font-size="7">Plant Transpiration</text>
    `;
  } else if(stage === 'cond') {
    status.textContent = "Condensation • Adiabatic Cooling & Cloud Microphysics";
    phase.textContent = "Vapor → Droplets (Latent Release)";
    driver.textContent = "Adiabatic Expansion & Cooling";
    impact.textContent = "Monsoon Cloud Bands";
    badge.textContent = "Condensation";
    desc.textContent = "As moist air rises, expanding adiabatically at higher tropospheric altitudes, it cools to its dew point. Vapor condenses around aerosol condensation nuclei to form cumulus clouds, releasing latent heat.";
    dyn.innerHTML = `
      <ellipse cx="230" cy="40" rx="35" ry="16" fill="#e2e8f0" opacity="0.9"/>
      <ellipse cx="255" cy="35" rx="30" ry="18" fill="#cbd5e1" opacity="0.9"/>
      <ellipse cx="205" cy="42" rx="25" ry="14" fill="#94a3b8" opacity="0.8"/>
      <text x="230" y="44" fill="#0f172a" font-size="8" font-weight="bold" text-anchor="middle">Cloud Formation</text>
      <text x="230" y="68" fill="#bae6fd" font-size="7" text-anchor="middle">Latent Heat Released Aloft</text>
    `;
  } else if(stage === 'prec') {
    status.textContent = "Precipitation & Infiltration • Monsoon Downpour & Runoff";
    phase.textContent = "Droplets → Rain / Snow";
    driver.textContent = "Gravity & Droplet Coalescence";
    impact.textContent = "Ganga Basin Groundwater Recharge";
    badge.textContent = "Precipitation";
    desc.textContent = "When droplets grow heavy enough, gravity pulls them down as precipitation. Water infiltrates aquifers, recharges groundwater tables, and flows into rivers back to the sea.";
    dyn.innerHTML = `
      <ellipse cx="230" cy="35" rx="40" ry="16" fill="#64748b"/>
      <line x1="210" y1="55" x2="200" y2="105" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,2"/>
      <line x1="230" y1="55" x2="220" y2="105" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,2"/>
      <line x1="250" y1="55" x2="240" y2="105" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,2"/>
      <!-- River arrow to ocean -->
      <path d="M 140,120 Q 210,125 280,120" stroke="#0284c7" stroke-width="3" fill="none"/>
      <text x="210" y="132" fill="#7dd3fc" font-size="7" font-weight="bold">River Runoff to Sea</text>
    `;
  } else {
    status.textContent = "Cryosphere Risk • Gangotri Retreat & Coastal Sea Level Threat";
    phase.textContent = "Solid Ice → Rapid Meltwater";
    driver.textContent = "Global Atmospheric Warming";
    impact.textContent = "Coastal Threats to Mumbai & Chennai";
    badge.textContent = "Glacial Retreat";
    desc.textContent = "Accelerating melt of Himalayan glaciers disrupts perennial dry-season flow for hundreds of millions in India. Simultaneously, global ice-sheet loss drives sea level rise, threatening coastal cities like Mumbai and Chennai.";
    dyn.innerHTML = `
      <polygon points="50,45 70,35 110,95 70,95" fill="#bae6fd"/>
      <path d="M 80,95 Q 110,110 150,120" stroke="#38bdf8" stroke-width="2.5" fill="none"/>
      <text x="120" y="90" fill="#f43f5e" font-size="7" font-weight="bold">Glacier Melt Acceleration</text>
      <!-- Coastal inundation mark on ocean -->
      <rect x="270" y="102" width="40" height="8" fill="#f43f5e" opacity="0.7"/>
      <text x="350" y="95" fill="#fda4af" font-size="7" font-weight="bold">Sea Level Rise: Mumbai &amp; Chennai</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC13S11('evap'));
</script>""",

    12: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Carbon Reservoir:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC13S12('fast')" id="c13s12_btn_fas" class="px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition">Fast Biological</button>
        <button onclick="setC13S12('slow')" id="c13s12_btn_slo" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Slow Geological</button>
        <button onclick="setC13S12('ocean')" id="c13s12_btn_oce" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Ocean Sink (71%)</button>
        <button onclick="setC13S12('keeling')" id="c13s12_btn_kee" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Keeling Curve</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s12_status">Photosynthesis &bull; 6 CO2 + 6 H2O &rarr; C6H12O6 + 6 O2</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <g id="c13s12_svg_content"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Timescale / Sink</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c13s12_val1">Days to Decades</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Atmospheric State</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s12_val2">Balanced Biosphere</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Equilibrium Status</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c13s12_val3">Rapid Biogeochemical Cycle</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-emerald-950 border border-emerald-700/60 text-emerald-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c13s12_badge">The Carbon Cycle</span>
    <span id="c13s12_desc">The carbon cycle links the fast biological exchange of photosynthesis and respiration with slow geological carbonate sedimentation. Oceans store 71% of all active carbon on Earth.</span>
  </div>
</div>
<script>
window.setC13S12 = function(mode) {
  ['fas', 'slo', 'oce', 'kee'].forEach(m => {
    const el = document.getElementById('c13s12_btn_' + m);
    if(el) {
      if((mode === 'fast' && m === 'fas') || (mode === 'slow' && m === 'slo') || (mode === 'ocean' && m === 'oce') || (mode === 'keeling' && m === 'kee')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const svg = document.getElementById('c13s12_svg_content');
  const status = document.getElementById('c13s12_status');
  const v1 = document.getElementById('c13s12_val1');
  const v2 = document.getElementById('c13s12_val2');
  const v3 = document.getElementById('c13s12_val3');
  const badge = document.getElementById('c13s12_badge');
  const desc = document.getElementById('c13s12_desc');

  if(mode === 'fast') {
    status.textContent = "Fast Biological Cycle • Photosynthesis vs Cellular Respiration";
    v1.textContent = "Days to Decades";
    v2.textContent = "Biological Dynamic Balance";
    v3.textContent = "Carbon Fixed in Biomass";
    badge.textContent = "Fast Biological";
    desc.textContent = "Terrestrial forests and phytoplankton fix atmospheric CO2 into glucose via photosynthesis. Organisms release it back via respiration and decomposition within days to decades.";
    svg.innerHTML = `
      <rect x="40" y="80" width="10" height="40" fill="#78350f"/>
      <circle cx="45" cy="70" r="30" fill="#22c55e" opacity="0.8"/>
      <!-- CO2 absorbed -->
      <path d="M 120,40 Q 80,45 60,60" stroke="#22c55e" stroke-width="2.5" fill="none"/>
      <text x="130" y="42" fill="#86efac" font-size="8" font-weight="bold">Photosynthesis: CO2 Uptake</text>
      <!-- Respiration emitted -->
      <path d="M 60,85 Q 100,90 140,85" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3" fill="none"/>
      <text x="150" y="88" fill="#fde68a" font-size="8">Respiration: CO2 Release</text>
    `;
  } else if(mode === 'slow') {
    status.textContent = "Slow Geological Cycle • Limestone Carbonates & Fossil Fuels";
    v1.textContent = "Millions of Years";
    v2.textContent = "Lithospheric Deep Storage";
    v3.textContent = "Volcanic & Mining Release";
    badge.textContent = "Slow Geological";
    desc.textContent = "Carbon dissolves in rainwater to form weak carbonic acid, weathering rocks into bicarbonate ions that wash into seas. Marine shells form calcium carbonate limestone, trapping carbon for millions of years.";
    svg.innerHTML = `
      <rect x="20" y="100" width="420" height="35" rx="4" fill="#451a03"/>
      <text x="230" y="122" fill="#fde68a" font-size="9" font-weight="bold" text-anchor="middle">Deep Lithosphere: Coal, Petroleum &amp; Limestone (CaCO3)</text>
      <!-- Combustion arrow upward -->
      <line x1="230" y1="95" x2="230" y2="40" stroke="#ef4444" stroke-width="3"/>
      <text x="240" y="55" fill="#fca5a5" font-size="8" font-weight="bold">Fossil Combustion: Releases Millions of Years of Stored C Instantly</text>
    `;
  } else if(mode === 'ocean') {
    status.textContent = "Ocean Carbon Sink • Holds 71% of Earth's Active Carbon";
    v1.textContent = "71% Global Carbon";
    v2.textContent = "Dissolved Inorganic Carbon";
    v3.textContent = "Chemical Solubility Pump";
    badge.textContent = "Ocean Carbon Sink";
    desc.textContent = "Oceans represent Earth's largest active carbon reservoir, storing 71% of global carbon as dissolved bicarbonate and carbonate ions. Phytoplankton incorporate carbon into biological shells.";
    svg.innerHTML = `
      <rect x="20" y="30" width="420" height="95" rx="6" fill="#0369a1" opacity="0.8"/>
      <text x="230" y="60" fill="#e0f2fe" font-size="11" font-weight="bold" text-anchor="middle">Oceanic Carbon Sink: 71% of Active Carbon</text>
      <text x="230" y="85" fill="#bae6fd" font-size="8" text-anchor="middle">CO2 (gas) + H2O &harr; H2CO3 &harr; H+ + HCO3- &harr; 2H+ + CO3(2-)</text>
      <text x="230" y="105" fill="#7dd3fc" font-size="8" text-anchor="middle">Marine Biocalcification: Plankton Shells &amp; Deep-Sea Sedimentation</text>
    `;
  } else {
    status.textContent = "Charles Keeling Curve • Mauna Loa CO2: 315 ppm (1958) to >420 ppm Today";
    v1.textContent = "315 &rarr; >420 ppm";
    v2.textContent = "Unprecedented Spike";
    v3.textContent = "Anthropogenic Forcing";
    badge.textContent = "Keeling Curve";
    desc.textContent = "Started by Charles Keeling at Mauna Loa in 1958, precise atmospheric measurements reveal rising CO2 from 315 ppm to over 420 ppm today, superimposed on annual vegetative seasonal oscillations.";
    svg.innerHTML = `
      <!-- Graph Axes -->
      <line x1="50" y1="120" x2="410" y2="120" stroke="#64748b" stroke-width="1.5"/>
      <line x1="50" y1="120" x2="50" y2="20" stroke="#64748b" stroke-width="1.5"/>
      <text x="50" y="132" fill="#94a3b8" font-size="7">1958 (315 ppm)</text>
      <text x="400" y="132" fill="#94a3b8" font-size="7">Today (&gt;420 ppm)</text>
      <!-- Upward curve with seasonal saw-tooth -->
      <path d="M 50,115 Q 230,95 400,25" stroke="#f43f5e" stroke-width="2.5" fill="none"/>
      <circle cx="400" cy="25" r="4" fill="#f43f5e"/>
      <text x="320" y="25" fill="#fda4af" font-size="8" font-weight="bold">&gt;420 ppm Today</text>
      <text x="230" y="70" fill="#fde047" font-size="8" text-anchor="middle">Keeling Curve: Rapid Industrial Atmospheric Enrichment</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC13S12('fast'));
</script>""",

    13: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Nitrogen Step:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800 flex-wrap">
        <button onclick="setC13S13('fix')" id="c13s13_btn_fix" class="px-2 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition">1. N2 Fixation</button>
        <button onclick="setC13S13('nit')" id="c13s13_btn_nit" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">2. Nitrification</button>
        <button onclick="setC13S13('ass')" id="c13s13_btn_ass" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">3. Assimilation</button>
        <button onclick="setC13S13('amm')" id="c13s13_btn_amm" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">4. Ammonification</button>
        <button onclick="setC13S13('den')" id="c13s13_btn_den" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">5. Denitrification</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s13_status">Rhizobium &bull; Azotobacter &bull; Nitrogenase Enzyme</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- 5 Box Linear Pathway -->
        <rect id="c13s13_box1" x="10" y="55" width="75" height="40" rx="4" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
        <text x="47" y="72" fill="#ecfdf5" font-size="7" font-weight="bold" text-anchor="middle">1. Fixation</text>
        <text x="47" y="85" fill="#a7f3d0" font-size="6" text-anchor="middle">N2 &rarr; NH3/NH4+</text>

        <rect id="c13s13_box2" x="100" y="55" width="75" height="40" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
        <text x="137" y="72" fill="#cbd5e1" font-size="7" font-weight="bold" text-anchor="middle">2. Nitrification</text>
        <text x="137" y="85" fill="#94a3b8" font-size="6" text-anchor="middle">NH3 &rarr; NO2- &rarr; NO3-</text>

        <rect id="c13s13_box3" x="190" y="55" width="75" height="40" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
        <text x="227" y="72" fill="#cbd5e1" font-size="7" font-weight="bold" text-anchor="middle">3. Assimilation</text>
        <text x="227" y="85" fill="#94a3b8" font-size="6" text-anchor="middle">Plant Proteins</text>

        <rect id="c13s13_box4" x="280" y="55" width="75" height="40" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
        <text x="317" y="72" fill="#cbd5e1" font-size="7" font-weight="bold" text-anchor="middle">4. Ammonification</text>
        <text x="317" y="85" fill="#94a3b8" font-size="6" text-anchor="middle">Waste &rarr; NH3</text>

        <rect id="c13s13_box5" x="370" y="55" width="80" height="40" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
        <text x="410" y="72" fill="#cbd5e1" font-size="7" font-weight="bold" text-anchor="middle">5. Denitrification</text>
        <text x="410" y="85" fill="#94a3b8" font-size="6" text-anchor="middle">NO3- &rarr; N2 Gas</text>

        <!-- Dynamic Microbe Annotation -->
        <text id="c13s13_microbe_txt" x="230" y="30" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">Microbe: Rhizobium (Legume Nodules) &amp; Free Azotobacter</text>
        <text id="c13s13_chem_txt" x="230" y="125" fill="#bae6fd" font-size="8" text-anchor="middle">Triple bond N&equiv;N cleaved by nitrogenase enzyme into usable ammonia</text>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Microbial Agent</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c13s13_agent">Rhizobium / Azotobacter</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Chemical Transform</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s13_trans">N2 Gas &rarr; Ammonia (NH3)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Biological Role</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c13s13_role">Unlocks Inert N2 Pool</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-emerald-950 border border-emerald-700/60 text-emerald-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c13s13_badge">Nitrogen Cycle</span>
    <span id="c13s13_desc">Atmospheric N2 (78%) is biologically inert due to its powerful triple bond. Specialized diazotrophic bacteria break this bond to produce reactive ammonia, allowing plant protein synthesis.</span>
  </div>
</div>
<script>
window.setC13S13 = function(step) {
  ['fix', 'nit', 'ass', 'amm', 'den'].forEach(s => {
    const el = document.getElementById('c13s13_btn_' + s);
    if(el) {
      if(s === step) el.className = 'px-2 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
      else el.className = 'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    }
  });

  const boxes = [1, 2, 3, 4, 5];
  boxes.forEach(b => {
    const box = document.getElementById('c13s13_box' + b);
    if(box) {
      box.setAttribute('fill', '#1e293b');
      box.setAttribute('stroke', '#334155');
    }
  });

  const mTxt = document.getElementById('c13s13_microbe_txt');
  const cTxt = document.getElementById('c13s13_chem_txt');
  const status = document.getElementById('c13s13_status');
  const agent = document.getElementById('c13s13_agent');
  const trans = document.getElementById('c13s13_trans');
  const role = document.getElementById('c13s13_role');
  const badge = document.getElementById('c13s13_badge');
  const desc = document.getElementById('c13s13_desc');

  if(step === 'fix') {
    document.getElementById('c13s13_box1').setAttribute('fill', '#065f46');
    document.getElementById('c13s13_box1').setAttribute('stroke', '#10b981');
    mTxt.textContent = "Microbe: Rhizobium (Legume Nodules) & Free Azotobacter";
    cTxt.textContent = "Triple bond N≡N cleaved by nitrogenase enzyme into ammonia (NH3)";
    status.textContent = "Rhizobium • Azotobacter • Nitrogenase Enzyme";
    agent.textContent = "Rhizobium & Azotobacter";
    trans.textContent = "N2 Gas → Ammonia (NH3)";
    role.textContent = "Inert N2 Cleavage";
    badge.textContent = "1. N2 Fixation";
    desc.textContent = "Atmospheric dinitrogen possesses an exceptionally stable triple covalent bond. Diazotrophic bacteria in legume root nodules synthesize nitrogenase enzymes to convert N2 into bioavailable ammonia.";
  } else if(step === 'nit') {
    document.getElementById('c13s13_box2').setAttribute('fill', '#075985');
    document.getElementById('c13s13_box2').setAttribute('stroke', '#0284c7');
    mTxt.textContent = "Microbes: Nitrosomonas (NH3 → NO2-) then Nitrobacter (NO2- → NO3-)";
    cTxt.textContent = "Two-step aerobic oxidation produces bioavailable nitrate (NO3-)";
    status.textContent = "Nitrosomonas • Nitrobacter • Two-Step Oxidation";
    agent.textContent = "Nitrosomonas & Nitrobacter";
    trans.textContent = "Ammonia → Nitrite → Nitrate";
    role.textContent = "Soil Chemical Oxidation";
    badge.textContent = "2. Nitrification";
    desc.textContent = "Nitrification is a two-step aerobic microbial oxidation: Nitrosomonas converts ammonia to nitrite (NO2-), and Nitrobacter oxidizes nitrite to nitrate (NO3-), the primary form plants absorb.";
  } else if(step === 'ass') {
    document.getElementById('c13s13_box3').setAttribute('fill', '#15803d');
    document.getElementById('c13s13_box3').setAttribute('stroke', '#22c55e');
    mTxt.textContent = "Plants: Root Transporters absorb NO3- & NH4+ for Biosynthesis";
    cTxt.textContent = "Inorganic nitrate converted into amino acids, proteins, and DNA";
    status.textContent = "Plant Assimilation • Amino Acid & Nucleotide Synthesis";
    agent.textContent = "Crop Plants & Trees";
    trans.textContent = "Nitrate → Amino Acids & RNA";
    role.textContent = "Biomass Protein Synthesis";
    badge.textContent = "3. Assimilation";
    desc.textContent = "Plant roots absorb soil nitrates through active membrane transporters. Nitrate is chemically incorporated into essential amino acids, proteins, and nucleic acids across the food web.";
  } else if(step === 'amm') {
    document.getElementById('c13s13_box4').setAttribute('fill', '#854d0e');
    document.getElementById('c13s13_box4').setAttribute('stroke', '#eab308');
    mTxt.textContent = "Decomposers: Fungi & Putrefying Bacteria in Forest Litter / Soil";
    cTxt.textContent = "Organic animal wastes and dead tissues decomposed into ammonia";
    status.textContent = "Decomposers • Organic Waste Breakdown";
    agent.textContent = "Fungi & Saprophytic Bacteria";
    trans.textContent = "Protein Waste → Ammonia";
    role.textContent = "Organic Nutrient Recycling";
    badge.textContent = "4. Ammonification";
    desc.textContent = "When organisms excrete metabolic waste or die, saprophytic fungi and bacteria decompose cellular proteins and urea, releasing organic nitrogen back to the soil as ammonia.";
  } else {
    document.getElementById('c13s13_box5').setAttribute('fill', '#991b1b');
    document.getElementById('c13s13_box5').setAttribute('stroke', '#ef4444');
    mTxt.textContent = "Microbe: Pseudomonas Denitrificans in Waterlogged Anaerobic Soils";
    cTxt.textContent = "Anaerobic respiration reduces soil nitrate back into atmospheric N2 gas";
    status.textContent = "Pseudomonas • Anaerobic Reduction back to N2";
    agent.textContent = "Pseudomonas denitrificans";
    trans.textContent = "Nitrate (NO3-) → N2 Gas";
    role.textContent = "Closes Atmospheric Loop";
    badge.textContent = "5. Denitrification";
    desc.textContent = "In waterlogged, oxygen-depleted soils, anaerobic denitrifying bacteria like Pseudomonas use soil nitrates as terminal electron acceptors, converting NO3- back to N2 gas to complete the cycle.";
  }
};
window.addEventListener('DOMContentLoaded', () => setC13S13('fix'));
</script>""",

    14: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Industrial Reactor:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC13S14('haber')" id="c13s14_btn_hab" class="px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">Haber-Bosch Synthesis</button>
        <button onclick="setC13S14('green')" id="c13s14_btn_gre" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Green Revolution</button>
        <button onclick="setC13S14('trade')" id="c13s14_btn_tra" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Ecological Tradeoffs</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s14_status">450 &deg;C &bull; 200 atm &bull; Fe Catalyst &bull; N2 + 3 H2 &harr; 2 NH3</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <g id="c13s14_svg_display"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Reaction Conditions</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s14_cond">450 &deg;C &bull; 200 atm</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Primary Product</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c13s14_prod">Anhydrous Ammonia / Urea</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Global Impact</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c13s14_imp">Feeds ~50% of Humanity</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-amber-950 border border-amber-700/60 text-amber-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c13s14_badge">Haber-Bosch</span>
    <span id="c13s14_desc">Developed by Fritz Haber and Carl Bosch, the synthesis fixes atmospheric nitrogen into ammonia under high temperature (450 &deg;C) and pressure (200 atm) over an iron catalyst, producing synthetic urea.</span>
  </div>
</div>
<script>
window.setC13S14 = function(mode) {
  ['hab', 'gre', 'tra'].forEach(m => {
    const el = document.getElementById('c13s14_btn_' + m);
    if(el) {
      if((mode === 'haber' && m === 'hab') || (mode === 'green' && m === 'gre') || (mode === 'trade' && m === 'tra')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const svg = document.getElementById('c13s14_svg_display');
  const status = document.getElementById('c13s14_status');
  const cond = document.getElementById('c13s14_cond');
  const prod = document.getElementById('c13s14_prod');
  const imp = document.getElementById('c13s14_imp');
  const badge = document.getElementById('c13s14_badge');
  const desc = document.getElementById('c13s14_desc');

  if(mode === 'haber') {
    status.textContent = "450 °C • 200 atm • Fe Catalyst • N2 + 3 H2 ⇌ 2 NH3";
    cond.textContent = "450 °C • 200 atm";
    prod.textContent = "Ammonia (NH3) & Urea";
    imp.textContent = "Feeds ~50% of Humanity";
    badge.textContent = "Haber-Bosch Synthesis";
    desc.textContent = "The Haber-Bosch process combines atmospheric N2 and hydrogen from natural gas over an iron catalyst at 450 °C and 200 atmospheres to synthesize ammonia, which is converted to urea fertilizer.";
    svg.innerHTML = `
      <!-- Reactor Vessel -->
      <rect x="150" y="20" width="160" height="105" rx="10" fill="#1c1917" stroke="#f59e0b" stroke-width="2"/>
      <text x="230" y="42" fill="#fef08a" font-size="9" font-weight="bold" text-anchor="middle">Catalytic Chamber: Fe Catalyst</text>
      <text x="230" y="60" fill="#fed7aa" font-size="8" text-anchor="middle">450 &deg;C &bull; 200 atm Pressure</text>
      <text x="230" y="82" fill="#4ade80" font-size="10" font-weight="bold" text-anchor="middle">N2 + 3 H2 &harr; 2 NH3</text>
      <text x="230" y="105" fill="#bae6fd" font-size="8" text-anchor="middle">&rarr; Synthetic Urea: CO(NH2)2</text>
      <!-- Inflow -->
      <path d="M 60,60 L 150,60" stroke="#38bdf8" stroke-width="3"/>
      <text x="100" y="52" fill="#bae6fd" font-size="7">N2 + H2 In</text>
      <!-- Outflow -->
      <path d="M 310,80 L 400,80" stroke="#4ade80" stroke-width="3"/>
      <text x="350" y="72" fill="#86efac" font-size="7">NH3 Out</text>
    `;
  } else if(mode === 'green') {
    status.textContent = "Green Revolution • High-Yield Wheat & Rice in Punjab, Haryana & UP";
    cond.textContent = "Synthetic Urea Applications";
    prod.textContent = "Quadrupled Crop Harvests";
    imp.textContent = "Food Self-Sufficiency";
    badge.textContent = "Green Revolution";
    desc.textContent = "In the 1960s, synthetic urea fertilizer combined with high-yielding semi-dwarf wheat and rice varieties transformed Indian agriculture, averting widespread famine in Punjab, Haryana, and Uttar Pradesh.";
    svg.innerHTML = `
      <rect x="40" y="25" width="380" height="95" rx="8" fill="#14532d" stroke="#22c55e" stroke-width="1.5"/>
      <text x="230" y="50" fill="#ecfdf5" font-size="10" font-weight="bold" text-anchor="middle">Green Revolution: High-Yield Crop Varieties</text>
      <text x="230" y="72" fill="#bbf7d0" font-size="8" text-anchor="middle">Intensive Synthetic Nitrogen Application &bull; Tubewell Irrigation</text>
      <text x="230" y="95" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">Punjab, Haryana &amp; UP Achieved Historic Food Security</text>
    `;
  } else {
    status.textContent = "Ecological Tradeoffs • 1-2% Global Energy & Groundwater Nitrate Leaching";
    cond.textContent = "Fossil Energy Intensive";
    prod.textContent = "Runoff & Eutrophication";
    imp.textContent = "Soil Acidity & Blue-Baby Risk";
    badge.textContent = "Ecological Tradeoffs";
    desc.textContent = "The process consumes 1% to 2% of total global energy and 3% to 5% of natural gas. Over-application of fertilizers leaches nitrates into village drinking wells and triggers toxic eutrophication in lakes.";
    svg.innerHTML = `
      <rect x="40" y="25" width="380" height="95" rx="8" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
      <text x="230" y="50" fill="#fee2e2" font-size="10" font-weight="bold" text-anchor="middle">Heavy Ecological &amp; Energy Footprint</text>
      <text x="230" y="72" fill="#fca5a5" font-size="8" text-anchor="middle">1-2% Global Energy Consumption &bull; High Carbon Emissions</text>
      <text x="230" y="95" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Groundwater Nitrate Pollution &bull; Lake Eutrophication</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC13S14('haber'));
</script>""",

    15: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-sky-400 uppercase tracking-wider">Oxygen Flux:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC13S15('budget')" id="c13s15_btn_bud" class="px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition">Global Budget (21%)</button>
        <button onclick="setC13S15('plankton')" id="c13s15_btn_pla" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Marine Phytoplankton (&gt;50%)</button>
        <button onclick="setC13S15('forest')" id="c13s15_btn_for" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Terrestrial Forests</button>
        <button onclick="setC13S15('sinks')" id="c13s15_btn_sin" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Oxygen Sinks</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s15_status">Atmospheric 20.95% &bull; Dynamic Equilibrium</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <g id="c13s15_svg_budget"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Atmospheric Fraction</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c13s15_pool">20.95% by Volume</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Primary Source</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c13s15_src">Marine Plankton (&gt;50%)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Major Sink</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s15_snk">Aerobic Respiration</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-sky-950 border border-sky-700/60 text-sky-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c13s15_badge">The Oxygen Cycle</span>
    <span id="c13s15_desc">Oxygen comprises 20.95% of our atmosphere, held in dynamic balance. Marine phytoplankton in the sunlit photic zone produce more than 50% of Earth's oxygen, while forests generate the remainder.</span>
  </div>
</div>
<script>
window.setC13S15 = function(mode) {
  ['bud', 'pla', 'for', 'sin'].forEach(m => {
    const el = document.getElementById('c13s15_btn_' + m);
    if(el) {
      if((mode === 'budget' && m === 'bud') || (mode === 'plankton' && m === 'pla') || (mode === 'forest' && m === 'for') || (mode === 'sinks' && m === 'sin')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const svg = document.getElementById('c13s15_svg_budget');
  const status = document.getElementById('c13s15_status');
  const pool = document.getElementById('c13s15_pool');
  const src = document.getElementById('c13s15_src');
  const snk = document.getElementById('c13s15_snk');
  const badge = document.getElementById('c13s15_badge');
  const desc = document.getElementById('c13s15_desc');

  if(mode === 'budget') {
    status.textContent = "Global Oxygen Balance • 20.95% Atmospheric Reservoir";
    pool.textContent = "20.95% by Volume";
    src.textContent = "Ocean Plankton + Forests";
    snk.textContent = "Respiration & Decay";
    badge.textContent = "Atmospheric Budget";
    desc.textContent = "Earth's atmospheric oxygen is maintained in steady state. Biological sinks (respiration, combustion, microbial decay) consume oxygen at nearly the exact rate photosynthetic sources regenerate it.";
    svg.innerHTML = `
      <rect x="30" y="25" width="400" height="95" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="230" y="55" fill="#e0f2fe" font-size="12" font-weight="bold" text-anchor="middle">Atmospheric Oxygen Pool: 20.95% (~21%)</text>
      <!-- Dual balanced arrows -->
      <path d="M 120,95 L 120,70" stroke="#22c55e" stroke-width="3"/>
      <text x="120" y="110" fill="#86efac" font-size="8" font-weight="bold" text-anchor="middle">Photosynthesis Source</text>
      <path d="M 340,70 L 340,95" stroke="#ef4444" stroke-width="3"/>
      <text x="340" y="110" fill="#fca5a5" font-size="8" font-weight="bold" text-anchor="middle">Respiration/Decay Sink</text>
    `;
  } else if(mode === 'plankton') {
    status.textContent = "Marine Phytoplankton • Microscopic Organisms Produce >50% of Global O2";
    pool.textContent = ">50% of Global O2";
    src.textContent = "Diatoms & Prochlorococcus";
    snk.textContent = "Oceanic Deep Respiration";
    badge.textContent = "Marine Phytoplankton";
    desc.textContent = "Vast numbers of diatoms and cyanobacteria (like Prochlorococcus) drifting in ocean photic zones carry out marine photosynthesis, contributing over half of the oxygen breathed by all land organisms.";
    svg.innerHTML = `
      <rect x="30" y="20" width="400" height="105" rx="8" fill="#0369a1" opacity="0.85"/>
      <text x="230" y="48" fill="#e0f2fe" font-size="11" font-weight="bold" text-anchor="middle">Oceanic Photic Zone: Marine Phytoplankton</text>
      <text x="230" y="70" fill="#bae6fd" font-size="9" text-anchor="middle">Diatoms &bull; Coccolithophores &bull; Cyanobacteria</text>
      <text x="230" y="95" fill="#4ade80" font-size="10" font-weight="bold" text-anchor="middle">Generates &gt;50% of Global Planetary Oxygen!</text>
    `;
  } else if(mode === 'forest') {
    status.textContent = "Terrestrial Forests • Canopy Photosynthesis in Western Ghats & Amazon";
    pool.textContent = "~45% of Global O2";
    src.textContent = "Canopy Leaves & Chlorophyll";
    snk.textContent = "Soil Respiration & Wood Decay";
    badge.textContent = "Terrestrial Forests";
    desc.textContent = "Tropical rainforests and mountain canopies like India's Western Ghats provide the terrestrial portion of global oxygen production through dense leaf surface area exposed to sunlight.";
    svg.innerHTML = `
      <rect x="30" y="20" width="400" height="105" rx="8" fill="#14532d" stroke="#22c55e" stroke-width="1.5"/>
      <text x="230" y="48" fill="#ecfdf5" font-size="11" font-weight="bold" text-anchor="middle">Terrestrial Forests &amp; Western Ghats Canopy</text>
      <text x="230" y="72" fill="#bbf7d0" font-size="8" text-anchor="middle">Dense multi-tiered vegetation captures sunlight and releases atmospheric O2</text>
      <text x="230" y="95" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">Crucial Continental Oxygen Generators</text>
    `;
  } else {
    status.textContent = "Oxygen Sinks • Aerobic Cellular Respiration, Decay & Fossil Fuel Burning";
    pool.textContent = "Continuously Consumed";
    src.textContent = "Balanced by Primary Production";
    snk.textContent = "Cellular Oxidation";
    badge.textContent = "Oxygen Sinks";
    desc.textContent = "Major oxygen sinks include aerobic cellular respiration in all animals and plants, microbial organic matter decomposition in soils, and human combustion of fossil fuels.";
    svg.innerHTML = `
      <rect x="30" y="20" width="400" height="105" rx="8" fill="#3b0764" stroke="#c084fc" stroke-width="1.5"/>
      <text x="230" y="45" fill="#f3e8ff" font-size="10" font-weight="bold" text-anchor="middle">Planetary Oxygen Consumption Sinks</text>
      <text x="230" y="68" fill="#e9d5ff" font-size="8" text-anchor="middle">1. Aerobic Respiration (C6H12O6 + 6 O2 &rarr; 6 CO2 + 6 H2O)</text>
      <text x="230" y="85" fill="#e9d5ff" font-size="8" text-anchor="middle">2. Bacterial Decay of Dead Biomass</text>
      <text x="230" y="102" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">3. Industrial Combustion of Hydrocarbon Fuels</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC13S15('budget'));
</script>""",

    16: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Planetary Impact:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC13S16('acid')" id="c13s16_btn_aci" class="px-2.5 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition">Ocean Acidification</button>
        <button onclick="setC13S16('eutro')" id="c13s16_btn_eut" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Eutrophication</button>
        <button onclick="setC13S16('defor')" id="c13s16_btn_def" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Deforestation</button>
        <button onclick="setC13S16('life')" id="c13s16_btn_lif" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Mission LiFE</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s16_status">CO2 + H2O &rarr; H2CO3 &bull; Ocean pH Drop Dissolves CaCO3 Shells</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <g id="c13s16_svg_impact"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Disrupted System</div>
        <div class="text-xs font-bold text-rose-300 mt-0.5" id="c13s16_sys">Marine Calcification</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Chemical Consequence</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s16_chem">pH Drop (30% More Acidic)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Mitigation Framework</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c13s16_mit">Paris &bull; Mission LiFE</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-rose-950 border border-rose-700/60 text-rose-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c13s16_badge">Ocean Acidification</span>
    <span id="c13s16_desc">Dissolving excess CO2 in seawater forms carbonic acid, reducing ocean pH and depleting carbonate ions needed by coral reefs and shellfish. India's Mission LiFE champions circular community sustainability.</span>
  </div>
</div>
<script>
window.setC13S16 = function(type) {
  ['aci', 'eut', 'def', 'lif'].forEach(m => {
    const el = document.getElementById('c13s16_btn_' + m);
    if(el) {
      if((type === 'acid' && m === 'aci') || (type === 'eutro' && m === 'eut') || (type === 'defor' && m === 'def') || (type === 'life' && m === 'lif')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const svg = document.getElementById('c13s16_svg_impact');
  const status = document.getElementById('c13s16_status');
  const sys = document.getElementById('c13s16_sys');
  const chem = document.getElementById('c13s16_chem');
  const mit = document.getElementById('c13s16_mit');
  const badge = document.getElementById('c13s16_badge');
  const desc = document.getElementById('c13s16_desc');

  if(type === 'acid') {
    status.textContent = "CO2 + H2O → H2CO3 • Ocean pH Drop Dissolves CaCO3 Shells";
    sys.textContent = "Marine Calcification";
    chem.textContent = "pH Drops from 8.25 to 8.14";
    mit.textContent = "Carbon Emission Reduction";
    badge.textContent = "Ocean Acidification";
    desc.textContent = "Absorbing excess atmospheric CO2 produces carbonic acid, which releases H+ ions that bind with carbonate (CO3(2-)). Depleted carbonate prevents corals and mollusks from building calcium carbonate shells.";
    svg.innerHTML = `
      <rect x="30" y="20" width="400" height="105" rx="8" fill="#082f49" stroke="#ef4444" stroke-width="1.5"/>
      <text x="230" y="45" fill="#fee2e2" font-size="10" font-weight="bold" text-anchor="middle">Ocean Acidification: pH Decline</text>
      <text x="230" y="68" fill="#fda4af" font-size="8" text-anchor="middle">CO2 (aq) + H2O &harr; H2CO3 &harr; H+ + HCO3-</text>
      <text x="230" y="90" fill="#fde047" font-size="8" text-anchor="middle">Excess H+ binds carbonate &rarr; Dissolves Coral Reefs &amp; Shellfish</text>
      <text x="230" y="110" fill="#bae6fd" font-size="7" text-anchor="middle">Andaman &amp; Lakshadweep Coral Reef Bleaching Risk</text>
    `;
  } else if(type === 'eutro') {
    status.textContent = "Eutrophication • Fertilizer Runoff, Algal Blooms & Hypoxic Dead Zones";
    sys.textContent = "Freshwater & Coastal Ecology";
    chem.textContent = "Severe Hypoxia (DO < 2 mg/L)";
    mit.textContent = "Precision Nutrient Management";
    badge.textContent = "Eutrophication";
    desc.textContent = "Agricultural nitrate and phosphate runoff causes massive algal blooms. When algae die, bacterial decomposition consumes dissolved oxygen, creating hypoxic dead zones where fish suffocate.";
    svg.innerHTML = `
      <rect x="30" y="20" width="400" height="105" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
      <text x="230" y="45" fill="#d1fae5" font-size="10" font-weight="bold" text-anchor="middle">Eutrophication: Fertilizer Runoff Cascade</text>
      <text x="230" y="68" fill="#6ee7b7" font-size="8" text-anchor="middle">1. N &amp; P Runoff &rarr; 2. Algal Bloom &rarr; 3. Bacterial Decomposition</text>
      <text x="230" y="90" fill="#f87171" font-size="8" font-weight="bold" text-anchor="middle">4. Severe Oxygen Depletion (Hypoxia) &rarr; Massive Fish Kills</text>
    `;
  } else if(type === 'defor') {
    status.textContent = "Deforestation • Loss of Carbon Sinks, Soil Erosion & Flash Flooding";
    sys.textContent = "Terrestrial Biosphere";
    chem.textContent = "Carbon Sinks Turn into Sources";
    mit.textContent = "Afforestation & Soil Conservation";
    badge.textContent = "Deforestation";
    desc.textContent = "Clearing forests eliminates living carbon sinks, destabilizes hillside soil in the Western Ghats and Himalayas, increases monsoon siltation, and escalates flash flooding risks in downstream valleys.";
    svg.innerHTML = `
      <rect x="30" y="20" width="400" height="105" rx="8" fill="#451a03" stroke="#d97706" stroke-width="1.5"/>
      <text x="230" y="45" fill="#fef3c7" font-size="10" font-weight="bold" text-anchor="middle">Deforestation &amp; Watershed Degradation</text>
      <text x="230" y="68" fill="#fed7aa" font-size="8" text-anchor="middle">Lost Carbon Storage &bull; Soil Erosion &bull; Siltation of Rivers</text>
      <text x="230" y="90" fill="#f87171" font-size="8" font-weight="bold" text-anchor="middle">Accelerated Landslides &amp; Flood Disasters in Himalayan Valleys</text>
    `;
  } else {
    status.textContent = "Mission LiFE (Lifestyle for Environment) • COP26 Community Action";
    sys.textContent = "Global Sustainability";
    chem.textContent = "Circular Resource Conservation";
    mit.textContent = "Mission LiFE at COP26";
    badge.textContent = "Mission LiFE";
    desc.textContent = "Introduced at COP26, India's Mission LiFE mobilizes individual actions into a global mass movement, replacing mindless consumption with mindful resource utilization to protect planetary boundaries.";
    svg.innerHTML = `
      <rect x="30" y="20" width="400" height="105" rx="8" fill="#14532d" stroke="#22c55e" stroke-width="2"/>
      <text x="230" y="45" fill="#f0fdf4" font-size="11" font-weight="bold" text-anchor="middle">Mission LiFE: Lifestyle for Environment</text>
      <text x="230" y="68" fill="#86efac" font-size="8" text-anchor="middle">Pro-Planet People (P3) Movement &bull; Mindful Resource Utilization</text>
      <text x="230" y="90" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Energy Conservation &bull; Circular Economy &bull; Sustainable Living</text>
      <text x="230" y="108" fill="#bbf7d0" font-size="7" text-anchor="middle">Global Mass Movement Championed by India at COP26</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC13S16('acid'));
</script>"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part2)} simulators for Part 2 (Slides 9-16).")
