#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 9 Science Chapter 13 Simulators (Part 1: Slides 1-8)
High-fidelity responsive SVG interactive laboratory widgets for Earth as a System: Energy, Matter, and Life.
"""

sims_part1 = {
    1: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Select Earth Sphere:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800 flex-wrap">
        <button onclick="setC13S1('geo')" id="c13s1_btn_geo" class="px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition">Geosphere</button>
        <button onclick="setC13S1('hydro')" id="c13s1_btn_hydro" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Hydrosphere</button>
        <button onclick="setC13S1('cryo')" id="c13s1_btn_cryo" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Cryosphere</button>
        <button onclick="setC13S1('atmo')" id="c13s1_btn_atmo" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Atmosphere</button>
        <button onclick="setC13S1('bio')" id="c13s1_btn_bio" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Biosphere</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s1_status">Deccan Basalt &bull; Thar Sand Dunes &bull; Mineral Crust</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div id="c13s1_graphic" class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 150" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <g id="c13s1_svg_group"></g>
      </svg>
    </div>

    <div id="c13s1_info" class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono" id="c13s1_lbl1">Core Domain</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c13s1_val1">Solid Earth Crust</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono" id="c13s1_lbl2">Indian Example</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s1_val2">Deccan / Thar</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono" id="c13s1_lbl3">Cross-Coupling</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c13s1_val3">Weathering &amp; Soil</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-emerald-950 border border-emerald-700/60 text-emerald-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c13s1_badge">System Overview</span>
    <span id="c13s1_desc">Earth operates as a single unified thermodynamic engine where matter cycles and energy flows continuously across five interconnected spheres.</span>
  </div>
</div>
<script>
window.setC13S1 = function(type) {
  const btns = ['geo', 'hydro', 'cryo', 'atmo', 'bio'];
  btns.forEach(b => {
    const el = document.getElementById('c13s1_btn_' + b);
    if(el) {
      if(b === type) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const svg = document.getElementById('c13s1_svg_group');
  const status = document.getElementById('c13s1_status');
  const val1 = document.getElementById('c13s1_val1');
  const val2 = document.getElementById('c13s1_val2');
  const val3 = document.getElementById('c13s1_val3');
  const badge = document.getElementById('c13s1_badge');
  const desc = document.getElementById('c13s1_desc');

  if(type === 'geo') {
    status.textContent = "Deccan Basalt • Thar Sand Dunes • Solid Lithosphere";
    val1.textContent = "Solid Earth & Rocks";
    val2.textContent = "Deccan Traps & Thar";
    val3.textContent = "Mineral Weathering";
    badge.textContent = "Geosphere";
    desc.textContent = "The geosphere encompasses rocks, minerals, soil, and the molten interior. In India, basaltic Deccan traps store groundwater while Thar sands define intense regional radiative heat absorption.";
    svg.innerHTML = `
      <polygon points="20,135 120,60 220,135" fill="#78350f" opacity="0.8"/>
      <polygon points="160,135 270,45 380,135" fill="#92400e" opacity="0.9"/>
      <polygon points="310,135 390,75 450,135" fill="#b45309" opacity="0.7"/>
      <rect x="0" y="130" width="460" height="20" fill="#451a03"/>
      <circle cx="270" cy="45" r="4" fill="#fde047"/>
      <text x="270" y="35" fill="#fef08a" font-size="9" font-weight="bold" text-anchor="middle">Plateau &amp; Dunes</text>
      <path d="M 50,120 Q 150,100 250,115 T 420,120" stroke="#f59e0b" stroke-width="2" fill="none" stroke-dasharray="4,4"/>
    `;
  } else if(type === 'hydro') {
    status.textContent = "Ganga-Brahmaputra Basin • Arabian Sea • Groundwater";
    val1.textContent = "Liquid Water Reservoirs";
    val2.textContent = "Ganga / Bay of Bengal";
    val3.textContent = "Monsoon Ocean Energy";
    badge.textContent = "Hydrosphere";
    desc.textContent = "The hydrosphere contains 97% saline ocean water and 3% freshwater in rivers, lakes, and aquifers. Arabian Sea heat energy fuels South Asian monsoon depressions, delivering water vital for Indian agriculture.";
    svg.innerHTML = `
      <rect x="0" y="80" width="460" height="70" fill="#0369a1" opacity="0.85"/>
      <path d="M 0,85 Q 115,65 230,85 T 460,85 L 460,150 L 0,150 Z" fill="#0284c7" opacity="0.6"/>
      <path d="M 0,95 Q 115,80 230,95 T 460,95 L 460,150 L 0,150 Z" fill="#0ea5e9" opacity="0.4"/>
      <text x="230" y="115" fill="#e0f2fe" font-size="11" font-weight="bold" text-anchor="middle">Hydrosphere: Ganga-Brahmaputra &amp; Oceans</text>
      <text x="230" y="132" fill="#bae6fd" font-size="8" text-anchor="middle">Liquid Thermal Reservoir &bull; Drives Indian Monsoon Moisture Influx</text>
    `;
  } else if(type === 'cryo') {
    status.textContent = "Himalayan Glaciers • Gangotri & Siachen • Ladakh Snow";
    val1.textContent = "Frozen Water Storage";
    val2.textContent = "Gangotri & Siachen";
    val3.textContent = "Albedo & River Flow";
    badge.textContent = "Cryosphere";
    desc.textContent = "The cryosphere consists of Earth's frozen water—ice caps, sea ice, and high-altitude mountain glaciers. Himalayan glaciers act as natural freshwater water towers, feeding perennial rivers like Ganga and Indus.";
    svg.innerHTML = `
      <polygon points="40,140 140,30 240,140" fill="#e0f2fe" opacity="0.95"/>
      <polygon points="130,30 140,30 240,140 180,140" fill="#38bdf8" opacity="0.5"/>
      <polygon points="180,140 280,20 380,140" fill="#f0f9ff" opacity="0.9"/>
      <polygon points="270,20 280,20 380,140 330,140" fill="#0284c7" opacity="0.4"/>
      <text x="280" y="15" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Gangotri &amp; Himalayan Glaciers</text>
      <text x="230" y="125" fill="#0c4a6e" font-size="8" font-weight="bold" text-anchor="middle">High Reflectance (Albedo 0.85) &bull; Perennial River Feeders</text>
    `;
  } else if(type === 'atmo') {
    status.textContent = "Protective Gaseous Envelope • 78% N2, 21% O2, Trace GHG";
    val1.textContent = "Gaseous Blanket";
    val2.textContent = "Troposphere Weather";
    val3.textContent = "Ozone UV Shield";
    badge.textContent = "Atmosphere";
    desc.textContent = "The atmosphere shields life from harmful cosmic and ultraviolet radiation while retaining thermal heat via the natural greenhouse effect. Tropospheric wind currents transport water vapor from ocean to land.";
    svg.innerHTML = `
      <defs>
        <linearGradient id="c13s1_grad_atmo" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.9"/>
          <stop offset="50%" stop-color="#0284c7" stop-opacity="0.5"/>
          <stop offset="100%" stop-color="#0f172a" stop-opacity="0.2"/>
        </linearGradient>
      </defs>
      <rect x="0" y="0" width="460" height="150" fill="url(#c13s1_grad_atmo)"/>
      <line x1="0" y1="50" x2="460" y2="50" stroke="#fde047" stroke-width="1.5" stroke-dasharray="5,5"/>
      <text x="230" y="42" fill="#fef08a" font-size="8" font-weight="bold" text-anchor="middle">Stratospheric Ozone Shield (15-35 km)</text>
      <text x="230" y="90" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Troposphere (0-12 km): All Clouds, Weather &amp; Monsoons</text>
      <text x="230" y="110" fill="#bfdbfe" font-size="8" text-anchor="middle">78% N2 &bull; 21% O2 &bull; 0.93% Ar &bull; 0.04% CO2</text>
    `;
  } else {
    status.textContent = "Living Organisms • Sundarban Mangroves • Coral Reefs";
    val1.textContent = "Global Living Matrix";
    val2.textContent = "Sundarbans & Western Ghats";
    val3.textContent = "Photosynthetic Carbon Sink";
    badge.textContent = "Biosphere";
    desc.textContent = "The biosphere spans all living systems, intersecting the lithosphere, hydrosphere, and atmosphere. Plants and marine phytoplankton actively pump oxygen and absorb billions of tonnes of carbon dioxide annually.";
    svg.innerHTML = `
      <rect x="0" y="100" width="460" height="50" fill="#14532d"/>
      <circle cx="100" cy="80" r="30" fill="#16a34a" opacity="0.9"/>
      <rect x="95" y="80" width="10" height="30" fill="#78350f"/>
      <circle cx="180" cy="70" r="38" fill="#22c55e" opacity="0.9"/>
      <rect x="174" y="75" width="12" height="35" fill="#78350f"/>
      <circle cx="260" cy="85" r="25" fill="#15803d" opacity="0.9"/>
      <rect x="256" y="85" width="8" height="25" fill="#78350f"/>
      <circle cx="350" cy="75" r="32" fill="#16a34a" opacity="0.9"/>
      <rect x="345" y="80" width="10" height="30" fill="#78350f"/>
      <text x="230" y="35" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Sundarbans Mangrove &amp; Western Ghats Canopy</text>
      <text x="230" y="52" fill="#bbf7d0" font-size="8" text-anchor="middle">Primary Producers &bull; Oxygen Release &bull; Carbon Sequestration</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC13S1('geo'));
</script>""",

    2: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Radiation Band:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC13S2('all')" id="c13s2_btn_all" class="px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">Full Spectrum</button>
        <button onclick="setC13S2('uv')" id="c13s2_btn_uv" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Ultraviolet (UV)</button>
        <button onclick="setC13S2('vis')" id="c13s2_btn_vis" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Visible (PAR)</button>
        <button onclick="setC13S2('ir')" id="c13s2_btn_ir" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Infrared (IR)</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s2_status">Speed of Light c = 3.0 &times; 10&sup8; m/s &bull; Total Solar Spectrum</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div id="c13s2_graphic" class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Sun emitter -->
        <circle cx="35" cy="72" r="28" fill="#f59e0b" filter="drop-shadow(0 0 10px #f59e0b)"/>
        <text x="35" y="75" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">Sun</text>

        <!-- Ozone Layer Barrier -->
        <rect x="220" y="10" width="16" height="125" rx="3" fill="#3b82f6" opacity="0.35" stroke="#60a5fa" stroke-dasharray="3,3"/>
        <text x="228" y="130" fill="#93c5fd" font-size="7" text-anchor="middle">Ozone Layer</text>

        <!-- Earth Surface -->
        <rect x="420" y="10" width="25" height="125" rx="4" fill="#047857"/>
        <text x="432" y="75" fill="#d1fae5" font-size="7" font-weight="bold" text-anchor="middle" transform="rotate(-90 432 75)">Earth Surface</text>

        <g id="c13s2_rays"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Wavelength Range</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s2_range">100 nm &ndash; 1 mm</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Solar Fraction</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c13s2_frac">~99% of Solar Flux</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Primary Role</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c13s2_role">Thermal &amp; Biological</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-amber-950 border border-amber-700/60 text-amber-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c13s2_badge">Solar Energy</span>
    <span id="c13s2_desc">Solar radiation spans ultraviolet, visible light, and infrared heat. Stratospheric ozone shields deadly high-energy UV, letting visible light power photosynthesis and infrared warm Earth.</span>
  </div>
</div>
<script>
window.setC13S2 = function(band) {
  ['all', 'uv', 'vis', 'ir'].forEach(b => {
    const el = document.getElementById('c13s2_btn_' + b);
    if(el) {
      if(b === band) el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
      else el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    }
  });

  const rays = document.getElementById('c13s2_rays');
  const status = document.getElementById('c13s2_status');
  const range = document.getElementById('c13s2_range');
  const frac = document.getElementById('c13s2_frac');
  const role = document.getElementById('c13s2_role');
  const badge = document.getElementById('c13s2_badge');
  const desc = document.getElementById('c13s2_desc');

  if(band === 'uv') {
    status.textContent = "Ultraviolet 100-400 nm • 99% Filtered in Stratosphere";
    range.textContent = "100 &ndash; 400 nm";
    frac.textContent = "~7% of Solar Flux";
    role.textContent = "Filtered by O3 Shield";
    badge.textContent = "Ultraviolet (UV)";
    desc.textContent = "UV radiation possesses sufficient quantum energy to break molecular DNA bonds. The stratospheric ozone layer absorbs UV-C completely and UV-B largely, preventing cellular sunburn and cataracts.";
    rays.innerHTML = `
      <path d="M 65,45 L 220,45" stroke="#a855f7" stroke-width="3" stroke-dasharray="4,2"/>
      <path d="M 65,55 L 220,55" stroke="#a855f7" stroke-width="3" stroke-dasharray="4,2"/>
      <circle cx="220" cy="50" r="6" fill="#c084fc" opacity="0.8"/>
      <text x="210" y="35" fill="#e9d5ff" font-size="8" font-weight="bold">Absorbed by O3</text>
    `;
  } else if(band === 'vis') {
    status.textContent = "Visible Spectrum 400-700 nm • Photosynthetically Active Radiation";
    range.textContent = "400 &ndash; 700 nm";
    frac.textContent = "~44% of Solar Flux";
    role.textContent = "Photosynthesis &amp; Vision";
    badge.textContent = "Visible Light (PAR)";
    desc.textContent = "The atmosphere is transparent to visible wavelengths (violet to red). This band penetrates clear air to reach terrestrial chloroplasts and marine algae, driving planetary photosynthesis.";
    rays.innerHTML = `
      <path d="M 65,70 L 420,70" stroke="#22c55e" stroke-width="3"/>
      <path d="M 65,80 L 420,80" stroke="#3b82f6" stroke-width="3"/>
      <path d="M 65,60 L 420,60" stroke="#eab308" stroke-width="3"/>
      <text x="320" y="55" fill="#86efac" font-size="8" font-weight="bold">Atmospheric Window: 100% Transmission</text>
    `;
  } else if(band === 'ir') {
    status.textContent = "Infrared Radiation >700 nm • Thermal Radiative Heat";
    range.textContent = "700 nm &ndash; 1 mm";
    frac.textContent = "~49% of Solar Flux";
    role.textContent = "Thermal Heating &amp; GHG";
    badge.textContent = "Infrared (IR)";
    desc.textContent = "Near-infrared arrives directly from the Sun, while thermal far-infrared is re-radiated back upward by Earth's surface and trapped by greenhouse gases, maintaining habitable temperatures.";
    rays.innerHTML = `
      <path d="M 65,95 L 420,95" stroke="#ef4444" stroke-width="3"/>
      <path d="M 420,105 L 260,105" stroke="#f87171" stroke-width="2.5" stroke-dasharray="3,3"/>
      <text x="340" y="120" fill="#fca5a5" font-size="7" font-weight="bold">Surface Re-radiation Absorbed by GHG</text>
    `;
  } else {
    status.textContent = "c = 3.0 &times; 10&sup8; m/s • 99% Energy in UV, Visible &amp; Infrared";
    range.textContent = "100 nm &ndash; 1 mm";
    frac.textContent = "99% Combined Solar Energy";
    role.textContent = "Planetary Heat Engine";
    badge.textContent = "Total Solar Spectrum";
    desc.textContent = "The solar spectrum spans shortwave UV (filtered by ozone), visible light (driving photosynthesis), and longwave infrared (driving thermal evaporation and atmospheric convection).";
    rays.innerHTML = `
      <path d="M 65,45 L 220,45" stroke="#a855f7" stroke-width="2" stroke-dasharray="3,2"/>
      <path d="M 65,72 L 420,72" stroke="#22c55e" stroke-width="2.5"/>
      <path d="M 65,100 L 420,100" stroke="#ef4444" stroke-width="2.5"/>
      <text x="140" y="38" fill="#d8b4fe" font-size="7">UV (Blocked by O3)</text>
      <text x="310" y="66" fill="#86efac" font-size="7">Visible PAR</text>
      <text x="310" y="94" fill="#fca5a5" font-size="7">Infrared Heat</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC13S2('all'));
</script>""",

    3: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Surface Hours:</span>
      <input type="range" min="1" max="10" value="4" step="1" id="c13s3_hours" oninput="updateC13S3()" class="w-24 accent-amber-500 cursor-pointer">
      <span class="text-xs font-mono font-bold text-white" id="c13s3_hours_lbl">4 Hours</span>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s3_status">Solar Constant = 1.4 kW/m&sup2; &bull; Surface Clear-Sky = 1.0 kW/m&sup2;</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Sun with 1.4 kW/m2 label -->
        <circle cx="45" cy="50" r="22" fill="#f59e0b" filter="drop-shadow(0 0 8px #f59e0b)"/>
        <text x="45" y="54" fill="#78350f" font-size="7" font-weight="bold" text-anchor="middle">Top: 1.4 kW/m&sup2;</text>

        <!-- Atmospheric attenuation bracket -->
        <rect x="120" y="15" width="20" height="115" rx="4" fill="#0284c7" opacity="0.3" stroke="#38bdf8" stroke-dasharray="3,3"/>
        <text x="130" y="75" fill="#bae6fd" font-size="7" text-anchor="middle" transform="rotate(-90 130 75)">Atmospheric Loss: 0.4 kW/m&sup2;</text>

        <!-- Ground Collector -->
        <rect x="200" y="80" width="100" height="40" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <text x="250" y="98" fill="#fef08a" font-size="8" font-weight="bold" text-anchor="middle">Solar Collector (1 m&sup2;)</text>
        <text x="250" y="112" fill="#94a3b8" font-size="7" text-anchor="middle">Surface Flux: 1.0 kW/m&sup2;</text>

        <!-- Thar Desert Map Icon -->
        <rect x="340" y="25" width="105" height="95" rx="6" fill="#451a03" stroke="#d97706" stroke-width="1.5"/>
        <text x="392" y="45" fill="#fde68a" font-size="8" font-weight="bold" text-anchor="middle">Indian Solar Atlas</text>
        <text x="392" y="60" fill="#fed7aa" font-size="7" text-anchor="middle">Anna Mani &amp; Rangarajan</text>
        <text x="392" y="80" fill="#f59e0b" font-size="9" font-weight="bold" text-anchor="middle">Thar Desert Grid</text>
        <text x="392" y="98" fill="#cbd5e1" font-size="7" text-anchor="middle">&gt;300 Sunny Days/Yr</text>
        <text x="392" y="110" fill="#4ade80" font-size="7" font-weight="bold" text-anchor="middle">Gigawatt Potential</text>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Energy Accumulated</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s3_energy">14.4 MJ / m&sup2;</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Hourly Influx (Ex 13.1)</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5">3.6 MJ / m&sup2; / hr</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Top vs Ground</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5">1.4 &rarr; 1.0 kW/m&sup2;</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-amber-950 border border-amber-700/60 text-amber-300 font-bold text-[10px] shrink-0 uppercase tracking-wide">Insolation Atlas</span>
    <span id="c13s3_desc">At the top of Earth's atmosphere, the solar constant is 1.4 kW/m&sup2;. Clear-sky absorption and scattering reduce surface insolation to 1.0 kW/m&sup2; (delivering 3.6 MJ/m&sup2; each hour). Anna Mani's solar radiation atlas mapped India's immense renewable solar resource in the Thar desert.</span>
  </div>
</div>
<script>
window.updateC13S3 = function() {
  const h = parseInt(document.getElementById('c13s3_hours').value, 10);
  document.getElementById('c13s3_hours_lbl').textContent = h + (h === 1 ? ' Hour' : ' Hours');
  const mj = (h * 3.6).toFixed(1);
  document.getElementById('c13s3_energy').textContent = mj + " MJ / m²";
};
window.addEventListener('DOMContentLoaded', updateC13S3);
</script>""",

    4: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-sky-400 uppercase tracking-wider">Surface Material:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800 flex-wrap">
        <button onclick="setC13S4('snow')" id="c13s4_btn_snow" class="px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition">Fresh Snow</button>
        <button onclick="setC13S4('ice')" id="c13s4_btn_ice" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Glacial Ice</button>
        <button onclick="setC13S4('rock')" id="c13s4_btn_rock" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Bare Rock</button>
        <button onclick="setC13S4('water')" id="c13s4_btn_water" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Ocean / Soil</button>
        <button onclick="setC13S4('city')" id="c13s4_btn_city" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Urban Concrete</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s4_status">Albedo &alpha; = 0.85 &bull; 85% Reflected &bull; 15% Absorbed</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Sun -->
        <circle cx="50" cy="30" r="18" fill="#f59e0b"/>
        
        <!-- Incident Ray -->
        <line x1="65" y1="40" x2="180" y2="105" stroke="#f59e0b" stroke-width="3"/>
        <text x="100" y="65" fill="#fef08a" font-size="7" font-weight="bold">Incident 100%</text>

        <!-- Reflected Ray -->
        <line id="c13s4_ref_ray" x1="180" y1="105" x2="280" y2="35" stroke="#38bdf8" stroke-width="4"/>
        <text id="c13s4_ref_txt" x="245" y="60" fill="#7dd3fc" font-size="7" font-weight="bold">Reflected 85%</text>

        <!-- Absorbed Arrow Down -->
        <line id="c13s4_abs_ray" x1="180" y1="105" x2="180" y2="135" stroke="#ef4444" stroke-width="2"/>
        <text id="c13s4_abs_txt" x="188" y="128" fill="#fca5a5" font-size="7" font-weight="bold">Absorbed 15%</text>

        <!-- Surface Ground -->
        <rect id="c13s4_ground" x="20" y="105" width="420" height="30" rx="3" fill="#e0f2fe"/>
        <text id="c13s4_ground_lbl" x="340" y="124" fill="#0f172a" font-size="9" font-weight="bold">Fresh Himalayan Snow</text>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Albedo (&alpha;)</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c13s4_albedo_val">0.80 &ndash; 0.90</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Heat Retained</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c13s4_heat_val">Minimal (10-20%)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Thermal Role</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s4_role_val">Planetary Coolant</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-sky-950 border border-sky-700/60 text-sky-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c13s4_badge">Albedo Physics</span>
    <span id="c13s4_desc">Albedo is the fraction of incident solar radiation reflected unchanged back into space. High albedo surfaces like snow reflect up to 90%, preventing surface warming, whereas dark oceans and asphalt absorb over 85% of solar radiation.</span>
  </div>
</div>
<script>
window.setC13S4 = function(mat) {
  ['snow', 'ice', 'rock', 'water', 'city'].forEach(m => {
    const el = document.getElementById('c13s4_btn_' + m);
    if(el) {
      if(m === mat) el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition';
      else el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    }
  });

  const refRay = document.getElementById('c13s4_ref_ray');
  const refTxt = document.getElementById('c13s4_ref_txt');
  const absRay = document.getElementById('c13s4_abs_ray');
  const absTxt = document.getElementById('c13s4_abs_txt');
  const ground = document.getElementById('c13s4_ground');
  const groundLbl = document.getElementById('c13s4_ground_lbl');
  const status = document.getElementById('c13s4_status');
  const albedoVal = document.getElementById('c13s4_albedo_val');
  const heatVal = document.getElementById('c13s4_heat_val');
  const roleVal = document.getElementById('c13s4_role_val');
  const badge = document.getElementById('c13s4_badge');
  const desc = document.getElementById('c13s4_desc');

  if(mat === 'snow') {
    status.textContent = "Albedo α = 0.85 • 85% Reflected • 15% Absorbed";
    refRay.setAttribute('stroke-width', '4');
    refTxt.textContent = "Reflected 85%";
    absRay.setAttribute('stroke-width', '1.5');
    absTxt.textContent = "Absorbed 15%";
    ground.setAttribute('fill', '#f0f9ff');
    groundLbl.textContent = "Fresh Snow (α = 0.8-0.9)";
    groundLbl.setAttribute('fill', '#0f172a');
    albedoVal.textContent = "0.80 – 0.90";
    heatVal.textContent = "Minimal (10-20%)";
    roleVal.textContent = "Planetary Coolant";
    badge.textContent = "Fresh Snow";
    desc.textContent = "Fresh snow has Earth's highest natural albedo (0.80 to 0.90). It reflects almost all sunlight, keeping polar and high Himalayan glacier regions cold and structurally stable.";
  } else if(mat === 'ice') {
    status.textContent = "Albedo α = 0.60 • 60% Reflected • 40% Absorbed";
    refRay.setAttribute('stroke-width', '3');
    refTxt.textContent = "Reflected 60%";
    absRay.setAttribute('stroke-width', '2.5');
    absTxt.textContent = "Absorbed 40%";
    ground.setAttribute('fill', '#7dd3fc');
    groundLbl.textContent = "Glacial Ice (α = 0.5-0.7)";
    groundLbl.setAttribute('fill', '#082f49');
    albedoVal.textContent = "0.50 – 0.70";
    heatVal.textContent = "Moderate (30-50%)";
    roleVal.textContent = "Cryospheric Core";
    badge.textContent = "Glacial Ice";
    desc.textContent = "Aged glacial ice reflects 50% to 70% of sunlight. When soot, dust, or melt ponds darken the ice surface, albedo drops sharply, accelerating further melting in a dangerous feedback loop.";
  } else if(mat === 'rock') {
    status.textContent = "Albedo α = 0.28 • 28% Reflected • 72% Absorbed";
    refRay.setAttribute('stroke-width', '2');
    refTxt.textContent = "Reflected 28%";
    absRay.setAttribute('stroke-width', '3.5');
    absTxt.textContent = "Absorbed 72%";
    ground.setAttribute('fill', '#78716c');
    groundLbl.textContent = "Bare Rock / Clay (α = 0.25-0.3)";
    groundLbl.setAttribute('fill', '#fafaf9');
    albedoVal.textContent = "0.25 – 0.30";
    heatVal.textContent = "High (70-75%)";
    roleVal.textContent = "Radiative Heating";
    badge.textContent = "Bare Rock";
    desc.textContent = "Bare mountain rocks and clays reflect only 25% to 30% of incident radiation. The remaining 70% to 75% is absorbed, warming slopes rapidly during midday sunshine.";
  } else if(mat === 'water') {
    status.textContent = "Albedo α = 0.08 • 8% Reflected • 92% Absorbed";
    refRay.setAttribute('stroke-width', '1');
    refTxt.textContent = "Reflected 8%";
    absRay.setAttribute('stroke-width', '5');
    absTxt.textContent = "Absorbed 92%";
    ground.setAttribute('fill', '#0284c7');
    groundLbl.textContent = "Ocean & Moist Black Soil (α = 0.05-0.15)";
    groundLbl.setAttribute('fill', '#e0f2fe');
    albedoVal.textContent = "0.05 – 0.15";
    heatVal.textContent = "Maximum (85-95%)";
    roleVal.textContent = "Primary Heat Sink";
    badge.textContent = "Ocean & Soil";
    desc.textContent = "Open oceans and wet black soil possess low albedo (0.05 to 0.15). They absorb over 85% to 95% of incoming solar energy, acting as Earth's primary thermal energy battery.";
  } else {
    status.textContent = "Albedo α = 0.12 • Concrete & Asphalt Heat Island";
    refRay.setAttribute('stroke-width', '1.5');
    refTxt.textContent = "Reflected 12%";
    absRay.setAttribute('stroke-width', '4.5');
    absTxt.textContent = "Absorbed 88%";
    ground.setAttribute('fill', '#334155');
    groundLbl.textContent = "Urban Concrete & Asphalt (Heat Island)";
    groundLbl.setAttribute('fill', '#f8fafc');
    albedoVal.textContent = "0.10 – 0.20";
    heatVal.textContent = "Trapped in Thermal Mass";
    roleVal.textContent = "Urban Heat Island";
    badge.textContent = "Urban Concrete";
    desc.textContent = "Urban centers replace reflective vegetation with dark asphalt and dense concrete. High absorption and immense thermal mass store heat by day and release it slowly at night, creating hot Urban Heat Islands.";
  }
};
window.addEventListener('DOMContentLoaded', () => setC13S4('snow'));
</script>""",

    5: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Earth Season:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC13S5('sol_jun')" id="c13s5_btn_jun" class="px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">June Solstice</button>
        <button onclick="setC13S5('equinox')" id="c13s5_btn_equ" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Equinox (Sep/Mar)</button>
        <button onclick="setC13S5('sol_dec')" id="c13s5_btn_dec" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">December Solstice</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s5_status">Axial Tilt 23.5&deg; &bull; Northern Hemisphere Summer</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Sun Parallel Beam Lines from Left -->
        <line x1="20" y1="35" x2="230" y2="35" stroke="#f59e0b" stroke-width="2"/>
        <line x1="20" y1="72" x2="230" y2="72" stroke="#f59e0b" stroke-width="2.5"/>
        <line x1="20" y1="110" x2="230" y2="110" stroke="#f59e0b" stroke-width="2"/>
        <text x="30" y="25" fill="#fde047" font-size="8" font-weight="bold">Parallel Solar Insolation</text>

        <!-- Tilted Earth Globe -->
        <g id="c13s5_globe" transform="translate(320, 72) rotate(23.5)">
          <!-- Earth sphere -->
          <circle cx="0" cy="0" r="50" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
          <!-- Equator line -->
          <line x1="-50" y1="0" x2="50" y2="0" stroke="#fde047" stroke-width="1.5" stroke-dasharray="3,2"/>
          <text x="25" y="-3" fill="#fef08a" font-size="6">Equator 0&deg;</text>
          <!-- Tropic of Cancer (North 23.5) -->
          <line x1="-46" y1="-20" x2="46" y2="-20" stroke="#f97316" stroke-width="1"/>
          <!-- Tropic of Capricorn (South 23.5) -->
          <line x1="-46" y1="20" x2="46" y2="20" stroke="#f97316" stroke-width="1"/>
          <!-- Axis line -->
          <line x1="0" y1="-65" x2="0" y2="65" stroke="#ef4444" stroke-width="1.5"/>
          <text x="5" y="-55" fill="#fca5a5" font-size="7" font-weight="bold">North Pole</text>
          <text x="5" y="60" fill="#fca5a5" font-size="7" font-weight="bold">South Pole</text>
        </g>

        <!-- Ray spread comparison callouts -->
        <rect x="18" y="115" width="180" height="22" rx="4" fill="#0f172a" stroke="#334155"/>
        <text x="25" y="130" fill="#94a3b8" font-size="7">Equator: Perpendicular &bull; Poles: Oblique Spread</text>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Subsolar Latitude</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s5_sublat">Tropic of Cancer (23.5&deg; N)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Indian Impact</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c13s5_ind">Peak Summer / Pre-Monsoon</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Polar Insolation</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c13s5_polar">Midnight Sun in Arctic</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-amber-950 border border-amber-700/60 text-amber-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c13s5_badge">Seasonal Insolation</span>
    <span id="c13s5_desc">Earth's permanent 23.5&deg; axial tilt means insolation strikes perpendicularly at low latitudes (concentrating heat over a smaller footprint) while striking obliquely at high latitudes. This geometric disparity drives global seasons and winds.</span>
  </div>
</div>
<script>
window.setC13S5 = function(season) {
  ['jun', 'equ', 'dec'].forEach(s => {
    const el = document.getElementById('c13s5_btn_' + s);
    if(el) {
      if((season === 'sol_jun' && s === 'jun') || (season === 'equinox' && s === 'equ') || (season === 'sol_dec' && s === 'dec')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const globe = document.getElementById('c13s5_globe');
  const status = document.getElementById('c13s5_status');
  const sublat = document.getElementById('c13s5_sublat');
  const ind = document.getElementById('c13s5_ind');
  const polar = document.getElementById('c13s5_polar');
  const badge = document.getElementById('c13s5_badge');
  const desc = document.getElementById('c13s5_desc');

  if(season === 'sol_jun') {
    globe.setAttribute('transform', 'translate(320, 72) rotate(23.5)');
    status.textContent = "Axial Tilt 23.5° • Northern Hemisphere Summer Solstice (June 21)";
    sublat.textContent = "Tropic of Cancer (23.5° N)";
    ind.textContent = "Peak Insolation & Heat Low";
    polar.textContent = "24-hr Arctic Light";
    badge.textContent = "June Solstice";
    desc.textContent = "Around June 21, the Northern Hemisphere tilts toward the Sun. Direct rays strike the Tropic of Cancer passing right through central India, creating a thermal low-pressure zone that draws in the South Asian monsoon.";
  } else if(season === 'equinox') {
    globe.setAttribute('transform', 'translate(320, 72) rotate(0)');
    status.textContent = "Equinox (March 21 & September 23) • Equal Day and Night Worldwide";
    sublat.textContent = "Equator (0°)";
    ind.textContent = "Mild Intermediate Climate";
    polar.textContent = "12-hr Day & Night";
    badge.textContent = "Equinox";
    desc.textContent = "During the equinoxes, neither hemisphere tilts toward or away from the Sun. Direct solar rays strike the equator perpendicularly, resulting in equal 12-hour day and night lengths globally.";
  } else {
    globe.setAttribute('transform', 'translate(320, 72) rotate(-23.5)');
    status.textContent = "Axial Tilt 23.5° • Southern Hemisphere Summer / Northern Winter (Dec 22)";
    sublat.textContent = "Tropic of Capricorn (23.5° S)";
    ind.textContent = "Cool Winter & Oblique Rays";
    polar.textContent = "24-hr Antarctic Light";
    badge.textContent = "December Solstice";
    desc.textContent = "Around December 22, the Southern Hemisphere tilts toward the Sun. Oblique rays spread weakly over northern India, leading to cold winter conditions with short daytime heating.";
  }
};
window.addEventListener('DOMContentLoaded', () => setC13S5('sol_jun'));
</script>""",

    6: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-sky-400 uppercase tracking-wider">Altitude Elevator:</span>
      <input type="range" min="0" max="85" value="10" step="1" id="c13s6_alt" oninput="updateC13S6()" class="w-28 accent-sky-500 cursor-pointer">
      <span class="text-xs font-mono font-bold text-white" id="c13s6_alt_lbl">10 km</span>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s6_status">Troposphere &bull; Lapse Rate = 6.5 &deg;C / km</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Strata background bars -->
        <!-- Troposphere: 0-12 km -->
        <rect x="30" y="105" width="280" height="30" fill="#0369a1" opacity="0.35"/>
        <text x="35" y="125" fill="#7dd3fc" font-size="8" font-weight="bold">Troposphere (0-12 km)</text>

        <!-- Stratosphere: 12-50 km -->
        <rect x="30" y="55" width="280" height="50" fill="#6366f1" opacity="0.25"/>
        <text x="35" y="85" fill="#c7d2fe" font-size="8" font-weight="bold">Stratosphere &bull; Ozone (12-50 km)</text>

        <!-- Mesosphere: 50-85 km -->
        <rect x="30" y="15" width="280" height="40" fill="#475569" opacity="0.3"/>
        <text x="35" y="38" fill="#cbd5e1" font-size="8" font-weight="bold">Mesosphere (50-85 km)</text>

        <!-- Temperature Curve line -->
        <!-- Ground: +15C, Tropopause (12km): -56C, Stratopause (50km): 0C, Mesopause (85km): -90C -->
        <polyline points="260,135 120,105 210,55 70,15" fill="none" stroke="#f43f5e" stroke-width="2"/>
        <text x="265" y="138" fill="#fda4af" font-size="7">+15&deg;C</text>
        <text x="95" y="102" fill="#93c5fd" font-size="7">-56&deg;C</text>
        <text x="215" y="52" fill="#fed7aa" font-size="7">0&deg;C</text>
        <text x="45" y="15" fill="#bae6fd" font-size="7">-90&deg;C</text>

        <!-- Dynamic Altitude Marker -->
        <circle id="c13s6_marker" cx="120" cy="105" r="5" fill="#facc15" stroke="#ffffff" stroke-width="1.5"/>
        <line id="c13s6_alt_line" x1="30" y1="105" x2="310" y2="105" stroke="#facc15" stroke-dasharray="2,2"/>

        <!-- Indian Scientist Sidebar: K. R. Ramanathan -->
        <rect x="325" y="15" width="125" height="115" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
        <text x="387" y="35" fill="#e0e7ff" font-size="8" font-weight="bold" text-anchor="middle">K. R. Ramanathan</text>
        <text x="387" y="48" fill="#a5b4fc" font-size="7" text-anchor="middle">Pioneering Physics (1934)</text>
        <text x="387" y="68" fill="#cbd5e1" font-size="7" text-anchor="middle">Mapped Ozone at 18,000 ft</text>
        <text x="387" y="80" fill="#cbd5e1" font-size="7" text-anchor="middle">across Indian Himalayas</text>
        <text x="387" y="100" fill="#38bdf8" font-size="7" font-weight="bold" text-anchor="middle">Stratospheric Inversion</text>
        <text x="387" y="115" fill="#86efac" font-size="7" text-anchor="middle">Ozone Heated by UV Flux</text>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Atmospheric Layer</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c13s6_layer">Troposphere</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Air Temperature</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s6_temp">-50.0 &deg;C</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Thermal Trend</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c13s6_trend">Cooling with Height</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-sky-950 border border-sky-700/60 text-sky-300 font-bold text-[10px] shrink-0 uppercase tracking-wide">Atmospheric Strata</span>
    <span id="c13s6_desc">In the troposphere, temperature drops by 6.5 &deg;C per kilometer (the environmental lapse rate). In the stratosphere, temperature reverses and warms upward because ozone absorbs solar UV. Ramanathan documented this Himalayan ozone profile in 1934.</span>
  </div>
</div>
<script>
window.updateC13S6 = function() {
  const alt = parseFloat(document.getElementById('c13s6_alt').value);
  document.getElementById('c13s6_alt_lbl').textContent = alt + ' km';

  let y = 135 - (alt / 85.0) * 120;
  let temp = 15;
  let layer = "Troposphere";
  let trend = "Cooling (6.5 °C/km)";
  let x = 260;

  if(alt <= 12) {
    layer = "Troposphere";
    temp = 15 - alt * 6.5;
    trend = "Lapse Rate (-6.5 °C/km)";
    x = 260 - (alt / 12) * (260 - 120);
  } else if(alt <= 50) {
    layer = "Stratosphere (Ozone)";
    temp = -63 + ((alt - 12) / 38) * 63;
    trend = "Ozone Inversion (Warming)";
    x = 120 + ((alt - 12) / 38) * (210 - 120);
  } else {
    layer = "Mesosphere";
    temp = 0 - ((alt - 50) / 35) * 90;
    trend = "Rapid Cooling to -90 °C";
    x = 210 - ((alt - 50) / 35) * (210 - 70);
  }

  const marker = document.getElementById('c13s6_marker');
  const altLine = document.getElementById('c13s6_alt_line');
  marker.setAttribute('cx', x);
  marker.setAttribute('cy', y);
  altLine.setAttribute('y1', y);
  altLine.setAttribute('y2', y);

  document.getElementById('c13s6_layer').textContent = layer;
  document.getElementById('c13s6_temp').textContent = temp.toFixed(1) + " °C";
  document.getElementById('c13s6_trend').textContent = trend;
};
window.addEventListener('DOMContentLoaded', updateC13S6);
</script>""",

    7: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Atmospheric Scenario:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC13S7('earth_nat')" id="c13s7_btn_en" class="px-2.5 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition">Natural Earth</button>
        <button onclick="setC13S7('earth_none')" id="c13s7_btn_eo" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Zero GHG Earth</button>
        <button onclick="setC13S7('venus')" id="c13s7_btn_ven" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Venus (Runaway)</button>
        <button onclick="setC13S7('montreal')" id="c13s7_btn_mon" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Montreal Protocol</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s7_status">Natural Greenhouse: +15 &deg;C &bull; H2O, CO2, CH4 Equilibrium</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Planet Base -->
        <circle id="c13s7_planet" cx="230" cy="180" r="110" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
        <!-- Atmosphere Shell -->
        <circle id="c13s7_atmo_ring" cx="230" cy="180" r="135" fill="none" stroke="#22c55e" stroke-width="12" opacity="0.35"/>

        <!-- Influx and Back-radiation arrows -->
        <g id="c13s7_radiation_arrows"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Mean Surface Temp</div>
        <div class="text-xs font-bold text-rose-300 mt-0.5" id="c13s7_temp">+15 &deg;C (Habitable)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Atmospheric State</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s7_comp">Trace CO2 &amp; Water Vapor</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Planetary Equilibrium</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c13s7_equil">Balanced Thermal Blanket</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-rose-950 border border-rose-700/60 text-rose-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c13s7_badge">Greenhouse Effect</span>
    <span id="c13s7_desc">Without greenhouse gases, Earth's thermal equilibrium would plunge to -18 &deg;C, freezing all liquid oceans solid. Venus demonstrates the extreme opposite: a runaway 96% CO2 greenhouse creating surface temperatures of 460 &deg;C.</span>
  </div>
</div>
<script>
window.setC13S7 = function(mode) {
  ['en', 'eo', 'ven', 'mon'].forEach(m => {
    const el = document.getElementById('c13s7_btn_' + m);
    if(el) {
      if((mode === 'earth_nat' && m === 'en') || (mode === 'earth_none' && m === 'eo') || (mode === 'venus' && m === 'ven') || (mode === 'montreal' && m === 'mon')) {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition';
      } else {
        el.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
      }
    }
  });

  const planet = document.getElementById('c13s7_planet');
  const ring = document.getElementById('c13s7_atmo_ring');
  const arrows = document.getElementById('c13s7_radiation_arrows');
  const status = document.getElementById('c13s7_status');
  const temp = document.getElementById('c13s7_temp');
  const comp = document.getElementById('c13s7_comp');
  const equil = document.getElementById('c13s7_equil');
  const badge = document.getElementById('c13s7_badge');
  const desc = document.getElementById('c13s7_desc');

  if(mode === 'earth_nat') {
    planet.setAttribute('fill', '#0369a1');
    ring.setAttribute('stroke', '#22c55e');
    ring.setAttribute('opacity', '0.4');
    status.textContent = "Natural Greenhouse: +15 °C • H2O, CO2, CH4 Equilibrium";
    temp.textContent = "+15 °C (Habitable)";
    comp.textContent = "Trace GHG Blanket";
    equil.textContent = "Liquid Water Stable";
    badge.textContent = "Natural Greenhouse";
    desc.textContent = "Natural concentrations of water vapor and carbon dioxide trap outgoing infrared, elevating surface temperatures by 33 °C from an icy -18 °C up to a life-sustaining +15 °C average.";
    arrows.innerHTML = `
      <line x1="120" y1="20" x2="190" y2="75" stroke="#f59e0b" stroke-width="2.5"/>
      <line x1="210" y1="75" x2="250" y2="40" stroke="#ef4444" stroke-width="2"/>
      <path d="M 250,40 Q 230,55 210,75" stroke="#f87171" stroke-width="2" fill="none" stroke-dasharray="3,3"/>
      <text x="230" y="30" fill="#fca5a5" font-size="8" font-weight="bold" text-anchor="middle">Downward IR Back-Radiation</text>
    `;
  } else if(mode === 'earth_none') {
    planet.setAttribute('fill', '#cbd5e1');
    ring.setAttribute('stroke', '#64748b');
    ring.setAttribute('opacity', '0.05');
    status.textContent = "Zero GHG Hypothetical: -18 °C (255 K) • Frozen World";
    temp.textContent = "-18 °C (Total Glaciation)";
    comp.textContent = "Zero Greenhouse Gases";
    equil.textContent = "Uninhabitable Ice Sheet";
    badge.textContent = "Zero GHG Earth";
    desc.textContent = "Without natural greenhouse absorption, all emitted infrared radiation would escape directly into space. Earth's surface would drop to -18 °C (255 K), locking all oceans and life in ice.";
    arrows.innerHTML = `
      <line x1="120" y1="20" x2="190" y2="75" stroke="#f59e0b" stroke-width="2.5"/>
      <line x1="210" y1="75" x2="300" y2="15" stroke="#ef4444" stroke-width="2.5"/>
      <text x="320" y="25" fill="#f87171" font-size="8" font-weight="bold">100% IR Escapes Unchecked</text>
    `;
  } else if(mode === 'venus') {
    planet.setAttribute('fill', '#b45309');
    ring.setAttribute('stroke', '#f97316');
    ring.setAttribute('opacity', '0.8');
    status.textContent = "Venus Runaway Greenhouse: 96% CO2 • 460 °C Surface";
    temp.textContent = "460 °C (Lead Melting)";
    comp.textContent = "96% Dense CO2 Blanket";
    equil.textContent = "Runaway Thermal Trap";
    badge.textContent = "Venus Runaway";
    desc.textContent = "Venus possesses a crushing 96% carbon dioxide atmosphere. Extreme infrared trapping produces a runaway greenhouse effect, heating the surface to 460 °C—hot enough to melt solid lead.";
    arrows.innerHTML = `
      <line x1="120" y1="20" x2="190" y2="75" stroke="#f59e0b" stroke-width="2.5"/>
      <path d="M 190,75 L 220,50 L 240,75 L 260,50 L 280,75" stroke="#ef4444" stroke-width="3" fill="none"/>
      <text x="230" y="30" fill="#fca5a5" font-size="8" font-weight="bold" text-anchor="middle">Multiple IR Internal Reflections</text>
    `;
  } else {
    planet.setAttribute('fill', '#0284c7');
    ring.setAttribute('stroke', '#3b82f6');
    ring.setAttribute('opacity', '0.6');
    status.textContent = "Montreal Protocol (1987) • CFC Phaseout & Antarctic Ozone Recovery";
    temp.textContent = "+15 °C &amp; UV Restored";
    comp.textContent = "CFCs Banned Globally";
    equil.textContent = "Stratospheric O3 Healing";
    badge.textContent = "Montreal Protocol";
    desc.textContent = "Signed in 1987, the Montreal Protocol phased out ozone-depleting chlorofluorocarbons (CFCs). It stands as humanity's most successful global environmental treaty, enabling the Antarctic ozone hole to recover.";
    arrows.innerHTML = `
      <circle cx="230" cy="50" r="16" fill="#3b82f6" opacity="0.6"/>
      <text x="230" y="53" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">O3 Shield Intact</text>
      <line x1="130" y1="20" x2="220" y2="45" stroke="#a855f7" stroke-width="2.5"/>
      <line x1="230" y1="65" x2="230" y2="75" stroke="#22c55e" stroke-width="2"/>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC13S7('earth_nat'));
</script>""",

    8: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Diurnal Cycle:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC13S8('day')" id="c13s8_btn_day" class="px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">Daytime (Valley Breeze)</button>
        <button onclick="setC13S8('night')" id="c13s8_btn_night" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Nighttime (Mountain Breeze)</button>
      </div>
    </div>
    <span class="text-xs text-slate-400 font-mono" id="c13s8_status">Anabatic Upslope Breeze &bull; Shimla &amp; Dehradun Valleys</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div class="w-full max-w-lg flex flex-col items-center justify-center">
      <svg viewBox="0 0 460 145" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <!-- Mountain Slopes -->
        <polygon points="0,140 100,30 200,140" fill="#334155"/>
        <polygon points="260,140 360,30 460,140" fill="#334155"/>
        <!-- Valley Floor -->
        <rect x="180" y="130" width="100" height="15" fill="#1e293b"/>
        <text x="230" y="142" fill="#94a3b8" font-size="7" font-weight="bold" text-anchor="middle">Valley Basin (Dehradun)</text>
        <text x="100" y="25" fill="#cbd5e1" font-size="7" font-weight="bold" text-anchor="middle">Ridge (Shimla)</text>

        <!-- Day / Night Sky Symbol -->
        <circle id="c13s8_celestial" cx="230" cy="30" r="14" fill="#f59e0b"/>

        <!-- Breeze Flow Vector Arrows -->
        <g id="c13s8_arrows"></g>
      </svg>
    </div>

    <div class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Breeze Designation</div>
        <div class="text-xs font-bold text-amber-300 mt-0.5" id="c13s8_type">Valley Breeze (Anabatic)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Flow Direction</div>
        <div class="text-xs font-bold text-emerald-300 mt-0.5" id="c13s8_dir">Upslope (Valley &rarr; Ridge)</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 uppercase font-mono">Driving Force</div>
        <div class="text-xs font-bold text-sky-300 mt-0.5" id="c13s8_cause">Slope Midday Thermal Low</div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 text-xs text-slate-300 flex items-start gap-2">
    <span class="px-2 py-0.5 rounded bg-amber-950 border border-amber-700/60 text-amber-300 font-bold text-[10px] shrink-0 uppercase tracking-wide" id="c13s8_badge">Mountain Breezes</span>
    <span id="c13s8_desc">During daylight hours, sun-drenched mountain slopes heat rapidly, causing air to expand and rise. Cooler dense air from the valley floor surges upslope as an anabatic valley breeze.</span>
  </div>
</div>
<script>
window.setC13S8 = function(time) {
  const btnDay = document.getElementById('c13s8_btn_day');
  const btnNight = document.getElementById('c13s8_btn_night');
  const celestial = document.getElementById('c13s8_celestial');
  const arrows = document.getElementById('c13s8_arrows');
  const status = document.getElementById('c13s8_status');
  const type = document.getElementById('c13s8_type');
  const dir = document.getElementById('c13s8_dir');
  const cause = document.getElementById('c13s8_cause');
  const badge = document.getElementById('c13s8_badge');
  const desc = document.getElementById('c13s8_desc');

  if(time === 'day') {
    btnDay.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition';
    btnNight.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    celestial.setAttribute('fill', '#f59e0b');
    status.textContent = "Anabatic Upslope Breeze • Daytime Slopes Heat Rapidly";
    type.textContent = "Valley Breeze (Anabatic)";
    dir.textContent = "Valley Floor → Mountain Slopes";
    cause.textContent = "Solar Slope Heating";
    badge.textContent = "Day: Valley Breeze";
    desc.textContent = "Intense solar insolation strikes Himalayan slopes, warming the rocky boundary layer faster than air over the deep valley. Rising buoyant air draws cooler air upward from Dehradun valley toward Shimla ridges.";
    arrows.innerHTML = `
      <!-- Upslope arrows -->
      <path d="M 180,120 L 120,60" stroke="#f59e0b" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
      <path d="M 280,120 L 340,60" stroke="#f59e0b" stroke-width="3" fill="none"/>
      <text x="130" y="95" fill="#fef08a" font-size="8" font-weight="bold">Warm Upslope Flow</text>
      <text x="290" y="95" fill="#fef08a" font-size="8" font-weight="bold">Warm Upslope Flow</text>
    `;
  } else {
    btnDay.className = 'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    btnNight.className = 'px-2.5 py-1 text-xs font-bold rounded-md bg-sky-600 text-white transition';
    celestial.setAttribute('fill', '#e2e8f0');
    status.textContent = "Katabatic Downslope Breeze • Nighttime Radiative Cooling";
    type.textContent = "Mountain Breeze (Katabatic)";
    dir.textContent = "Mountain Crests → Valley Floor";
    cause.textContent = "Radiative Chilling & Gravity";
    badge.textContent = "Night: Mountain Breeze";
    desc.textContent = "At night, high mountain ridges rapidly lose heat through clear radiative cooling. The chilled, heavy air drains downward under gravity into valleys like Dehradun, producing cold night-time breezes.";
    arrows.innerHTML = `
      <!-- Downslope arrows -->
      <path d="M 120,60 L 180,120" stroke="#38bdf8" stroke-width="3" fill="none"/>
      <path d="M 340,60 L 280,120" stroke="#38bdf8" stroke-width="3" fill="none"/>
      <text x="130" y="95" fill="#93c5fd" font-size="8" font-weight="bold">Cold Dense Downslope</text>
      <text x="290" y="95" fill="#93c5fd" font-size="8" font-weight="bold">Cold Dense Downslope</text>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC13S8('day'));
</script>"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part1)} simulators for Part 1 (Slides 1-8).")
