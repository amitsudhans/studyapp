#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 9 Science Chapter 12 Simulators (Part 1: Slides 1-8)
High-fidelity responsive SVG interactive laboratory widgets for Patterns in Life: Diversity and Classification.
"""

sims_part1 = {
    1: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Biome &amp; Niche:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S1('himalaya')" id="c12s1_btn_him" class="px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition">Himalayan Alpine</button>
        <button onclick="setC12S1('andaman')" id="c12s1_btn_and" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Andaman Reef</button>
        <button onclick="setC12S1('forest')" id="c12s1_btn_for" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Tropical Forest</button>
        <button onclick="setC12S1('cycle')" id="c12s1_btn_cyc" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Ecological Roles</button>
      </div>
    </div>
    <span class="text-xs text-slate-400" id="c12s1_status">High Altitude &bull; Endemic Rhododendrons &amp; Snow Leopard</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-center items-center">
    <div id="c12s1_graphic" class="w-full max-w-lg flex flex-col items-center justify-center">
      <!-- SVG Biome Representation -->
      <svg viewBox="0 0 460 150" class="w-full h-36 rounded-lg border border-slate-800 bg-slate-900/50 shadow-inner">
        <defs>
          <linearGradient id="c12s1_grad_sky" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#0f172a" />
            <stop offset="100%" stop-color="#1e293b" />
          </linearGradient>
          <linearGradient id="c12s1_grad_reef" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#0369a1" />
            <stop offset="100%" stop-color="#082f49" />
          </linearGradient>
        </defs>
        <g id="c12s1_svg_group">
          <!-- Background and foreground elements will be dynamically swapped -->
        </g>
      </svg>
    </div>

    <!-- Data cards & metrics -->
    <div id="c12s1_info" class="w-full max-w-lg grid grid-cols-3 gap-2 mt-2">
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 font-semibold uppercase" id="c12s1_m1_lbl">Altitude / Depth</div>
        <div class="text-xs font-bold text-emerald-300" id="c12s1_m1_val">3,500 - 5,500 m</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 font-semibold uppercase" id="c12s1_m2_lbl">Keystone Organisms</div>
        <div class="text-xs font-bold text-cyan-300" id="c12s1_m2_val">Snow Leopard, Juniper</div>
      </div>
      <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2 text-center">
        <div class="text-[10px] text-slate-400 font-semibold uppercase" id="c12s1_m3_lbl">Ecological Service</div>
        <div class="text-xs font-bold text-amber-300" id="c12s1_m3_val">Water Catchment Towers</div>
      </div>
    </div>
  </div>

  <div class="bg-emerald-950/30 border border-emerald-800/40 rounded-xl px-3 py-2 text-xs text-emerald-200" id="c12s1_desc">
    <strong>Himalayan Alpine Biome:</strong> Extreme temperature fluctuations and thin atmosphere host specialized cold-adapted flora and fauna. From snow-clad crags to subalpine meadows, biodiversity forms fragile hydrological networks that sustain perennial Indian river systems.
  </div>
</div>
<script>
window.setC12S1 = function(mode){
  const btns = ['him', 'and', 'for', 'cyc'];
  btns.forEach(b => {
    const el = document.getElementById('c12s1_btn_' + b);
    if(el) el.className = (b === mode.substring(0,3) || (mode==='cycle' && b==='cyc')) ?
      'px-2.5 py-1 text-xs font-bold rounded-md bg-emerald-600 text-white transition' :
      'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  });

  const svg = document.getElementById('c12s1_svg_group');
  const status = document.getElementById('c12s1_status');
  const m1_lbl = document.getElementById('c12s1_m1_lbl');
  const m1_val = document.getElementById('c12s1_m1_val');
  const m2_lbl = document.getElementById('c12s1_m2_lbl');
  const m2_val = document.getElementById('c12s1_m2_val');
  const m3_lbl = document.getElementById('c12s1_m3_lbl');
  const m3_val = document.getElementById('c12s1_m3_val');
  const desc = document.getElementById('c12s1_desc');

  if(mode === 'himalaya'){
    status.innerHTML = "High Altitude &bull; Endemic Rhododendrons &amp; Snow Leopard";
    svg.innerHTML = `
      <rect width="460" height="150" fill="url(#c12s1_grad_sky)"/>
      <polygon points="40,150 140,40 220,150" fill="#334155" />
      <polygon points="120,62 140,40 160,65 145,60" fill="#f8fafc" />
      <polygon points="160,150 260,20 360,150" fill="#1e293b" />
      <polygon points="230,55 260,20 290,58 275,52 260,57" fill="#f8fafc" />
      <polygon points="300,150 390,50 460,150" fill="#334155" />
      <polygon points="370,72 390,50 410,75" fill="#f8fafc" />
      <!-- Alpine Conifers & Rhododendron bushes -->
      <path d="M70,150 L80,120 L90,150 Z M110,150 L120,125 L130,150 Z M330,150 L340,122 L350,150 Z" fill="#10b981" opacity="0.8"/>
      <circle cx="210" cy="135" r="4" fill="#f43f5e" title="Rhododendron flower"/>
      <circle cx="218" cy="138" r="3" fill="#f43f5e"/>
      <text x="140" y="32" fill="#94a3b8" font-size="10" font-weight="bold">Snowbound Peak</text>
      <text x="260" y="15" fill="#cbd5e1" font-size="10" font-weight="bold">Himalayan Ridge (5,000m)</text>
    `;
    m1_lbl.textContent = "Altitude Range";
    m1_val.textContent = "3,500 – 5,500 m";
    m2_lbl.textContent = "Keystone Species";
    m2_val.textContent = "Snow Leopard, Alpine Musk Deer";
    m3_lbl.textContent = "Ecosystem Role";
    m3_val.textContent = "Perennial Water Catchment";
    desc.innerHTML = "<strong>Himalayan Alpine Biome:</strong> Spanning northern India, the Himalayas create extreme climatic gradients. From subalpine rhododendron forests to alpine meadows and snowline rockfaces, specialized flora and fauna act as Asia's primary freshwater reservoirs.";
  } else if(mode === 'andaman'){
    status.innerHTML = "Marine Biodiversity &bull; Coral Reefs &amp; Seagrass Meadows";
    svg.innerHTML = `
      <rect width="460" height="150" fill="url(#c12s1_grad_reef)"/>
      <!-- Sun rays underwater -->
      <polygon points="80,0 120,0 200,150 140,150" fill="#38bdf8" opacity="0.1"/>
      <polygon points="260,0 300,0 360,150 310,150" fill="#38bdf8" opacity="0.1"/>
      <!-- Coral formations on seabed -->
      <path d="M0,150 Q40,120 70,150 Q100,105 130,150 Q180,90 220,150 Q270,110 320,150 Q380,95 420,150 L460,150 Z" fill="#0f766e" />
      <!-- Branching Acropora Coral -->
      <path d="M120,135 Q115,100 100,90 M120,115 Q135,100 140,85 M120,110 L120,80" stroke="#f43f5e" stroke-width="4" stroke-linecap="round" fill="none"/>
      <!-- Brain Coral dome -->
      <ellipse cx="260" cy="130" rx="28" ry="18" fill="#eab308" opacity="0.9"/>
      <path d="M245,125 Q260,115 275,125 M248,132 Q260,122 272,132" stroke="#713f12" stroke-width="2" fill="none"/>
      <!-- Marine fish -->
      <path d="M340,70 Q355,60 370,70 L380,62 L378,75 L380,78 Z" fill="#fb923c"/>
      <circle cx="348" cy="68" r="1.5" fill="#0f172a"/>
      <!-- Marine Algae / Phytoplankton -->
      <text x="30" y="45" fill="#38bdf8" font-size="11" font-weight="bold">Phytoplankton &amp; Microalgae (&gt;50% Global O₂)</text>
    `;
    m1_lbl.textContent = "Ocean Depth";
    m1_val.textContent = "0 – 40 m (Euphotic Zone)";
    m2_lbl.textContent = "Keystone Organisms";
    m2_val.textContent = "Acropora Corals, Dugong, Clownfish";
    m3_lbl.textContent = "Ecosystem Role";
    m3_val.textContent = "Oxygen Production &amp; Coastal Shield";
    desc.innerHTML = "<strong>Andaman Sea Coral Reefs:</strong> Coral reefs represent the rainforests of the ocean. Microscopic symbiotic zooxanthellae and marine algae perform intensive photosynthesis, releasing immense oxygen while calcium carbonate structures shield islands from cyclonic waves.";
  } else if(mode === 'forest'){
    status.innerHTML = "Western Ghats &bull; Stratified Tropical Evergreen Canopy";
    svg.innerHTML = `
      <rect width="460" height="150" fill="#064e3b"/>
      <!-- Forest Canopy layers -->
      <ellipse cx="60" cy="40" rx="55" ry="35" fill="#047857" opacity="0.8"/>
      <ellipse cx="160" cy="30" rx="70" ry="40" fill="#10b981" opacity="0.7"/>
      <ellipse cx="280" cy="45" rx="80" ry="45" fill="#059669" opacity="0.85"/>
      <ellipse cx="400" cy="35" rx="65" ry="38" fill="#047857" opacity="0.9"/>
      <!-- Tree Trunks -->
      <rect x="55" y="65" width="12" height="85" fill="#78350f"/>
      <rect x="155" y="60" width="14" height="90" fill="#78350f"/>
      <rect x="275" y="75" width="16" height="75" fill="#78350f"/>
      <rect x="395" y="65" width="14" height="85" fill="#78350f"/>
      <!-- Epiphytes / Lianes -->
      <path d="M60,65 Q80,100 65,130" stroke="#15803d" stroke-width="2" fill="none"/>
      <path d="M280,75 Q310,110 285,145" stroke="#15803d" stroke-width="2" fill="none"/>
      <!-- Forest Floor Litter -->
      <rect x="0" y="140" width="460" height="10" fill="#451a03"/>
      <text x="20" y="20" fill="#a7f3d0" font-size="10" font-weight="bold">Emergent &amp; Canopy Layer (30-45m)</text>
      <text x="20" y="135" fill="#fde68a" font-size="10" font-weight="bold">Herbaceous Understory &amp; Humus Floor</text>
    `;
    m1_lbl.textContent = "Canopy Stratification";
    m1_val.textContent = "4 Continuous Strata";
    m2_lbl.textContent = "Floral Diversity";
    m2_val.textContent = "Epiphytes, Lianes, Dipterocarps";
    m3_lbl.textContent = "Ecosystem Role";
    m3_val.textContent = "Carbon Sink &amp; Climate Regulation";
    desc.innerHTML = "<strong>Tropical Wet Evergreen Forest:</strong> Characterized by dense, multi-tiered canopies that block direct sunlight from the forest floor. These ancient forests harbor immense genetic diversity, driving rainfall recycling and acting as colossal carbon sequestration sinks.";
  } else {
    status.innerHTML = "Ecological Interdependence &bull; Producers, Decomposers, Pollinators";
    svg.innerHTML = `
      <rect width="460" height="150" fill="#0f172a"/>
      <!-- Solar Energy -->
      <circle cx="50" cy="50" r="22" fill="#f59e0b" filter="drop-shadow(0 0 8px #f59e0b)"/>
      <text x="35" y="54" fill="#ffffff" font-size="9" font-weight="bold">Sun</text>
      <!-- Producers (Plants & Algae) -->
      <rect x="130" y="30" width="75" height="40" rx="8" fill="#065f46" stroke="#10b981" stroke-width="2"/>
      <text x="138" y="47" fill="#6ee7b7" font-size="10" font-weight="bold">Producers</text>
      <text x="134" y="60" fill="#a7f3d0" font-size="8">Plants &amp; Algae</text>
      <!-- Pollinators -->
      <rect x="250" y="15" width="80" height="38" rx="8" fill="#831843" stroke="#f43f5e" stroke-width="2"/>
      <text x="258" y="32" fill="#fbcfe8" font-size="10" font-weight="bold">Pollinators</text>
      <text x="255" y="45" fill="#f9a8d4" font-size="8">Bees &amp; Butterflies</text>
      <!-- Decomposers -->
      <rect x="250" y="85" width="85" height="40" rx="8" fill="#713f12" stroke="#eab308" stroke-width="2"/>
      <text x="256" y="102" fill="#fef08a" font-size="10" font-weight="bold">Decomposers</text>
      <text x="254" y="115" fill="#fef9c3" font-size="8">Fungi &amp; Bacteria</text>
      <!-- Consumers -->
      <rect x="370" y="45" width="75" height="40" rx="8" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
      <text x="378" y="62" fill="#bfdbfe" font-size="10" font-weight="bold">Consumers</text>
      <text x="377" y="75" fill="#93c5fd" font-size="8">Animals &amp; Man</text>
      <!-- Connecting arrows -->
      <path d="M75,50 L125,50" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)" stroke-dasharray="3,3"/>
      <path d="M205,42 L245,30" stroke="#10b981" stroke-width="2"/>
      <path d="M205,55 L365,60" stroke="#10b981" stroke-width="2"/>
      <path d="M400,90 L340,105" stroke="#94a3b8" stroke-width="2"/>
      <path d="M250,110 L180,72" stroke="#eab308" stroke-width="2"/>
    `;
    m1_lbl.textContent = "Energy Flow";
    m1_val.textContent = "Unidirectional (Sun &rarr; Food)";
    m2_lbl.textContent = "Nutrient Flow";
    m2_val.textContent = "Cyclic via Decomposers";
    m3_lbl.textContent = "Crop Pollination";
    m3_val.textContent = "80% Flowering Species Dependent";
    desc.innerHTML = "<strong>The Web of Life:</strong> Biodiversity is not an isolated inventory of species, but an intricate functional web. Plants harness solar energy, pollinators ensure crop reproduction, and decomposers recycle soil nutrients—sustaining the entire human agricultural base.";
  }
};
window.addEventListener('DOMContentLoaded', () => setC12S1('himalaya'));
</script>""",

    2: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">India's 4 Hotspots:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S2('wg')" id="c12s2_btn_wg" class="px-2 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">Western Ghats</button>
        <button onclick="setC12S2('eh')" id="c12s2_btn_eh" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Himalayas</button>
        <button onclick="setC12S2('ib')" id="c12s2_btn_ib" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Indo-Burma</button>
        <button onclick="setC12S2('sl')" id="c12s2_btn_sl" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Sundaland</button>
      </div>
    </div>
    <span class="text-xs text-amber-300 font-mono" id="c12s2_species">Nilgiri Tahr &amp; Lion-tailed Macaque</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col md:flex-row gap-3 items-center">
    <!-- Map / Region Visualization SVG -->
    <div class="w-full md:w-1/2 h-44 flex items-center justify-center bg-slate-900/40 rounded-xl border border-slate-800/80 p-1">
      <svg viewBox="0 0 240 200" class="w-full h-full">
        <!-- Simplified India Outline -->
        <path d="M90,20 L120,15 L140,40 L160,50 L200,60 L210,80 L180,95 L145,100 L130,120 L115,160 L105,190 L95,160 L80,130 L65,110 L50,90 L60,65 L85,45 Z" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
        <!-- Western Ghats highlighted ribbon -->
        <path id="c12s2_map_wg" d="M80,125 Q70,150 95,185" stroke="#f59e0b" stroke-width="6" stroke-linecap="round" fill="none" opacity="1"/>
        <!-- Himalayas ribbon -->
        <path id="c12s2_map_eh" d="M95,30 Q145,45 195,55" stroke="#38bdf8" stroke-width="5" stroke-linecap="round" fill="none" opacity="0.3"/>
        <!-- Indo-Burma region -->
        <path id="c12s2_map_ib" d="M185,60 Q215,70 205,95" stroke="#ec4899" stroke-width="6" stroke-linecap="round" fill="none" opacity="0.3"/>
        <!-- Sundaland / Nicobar -->
        <circle id="c12s2_map_sl" cx="195" cy="180" r="5" fill="#10b981" opacity="0.3"/>
        <text x="180" y="195" fill="#64748b" font-size="7">Nicobar</text>
        <circle cx="105" cy="190" r="2" fill="#f8fafc"/>
        <text x="110" y="192" fill="#94a3b8" font-size="7">Kanyakumari</text>
      </svg>
    </div>

    <!-- Endemic Details Panel -->
    <div class="w-full md:w-1/2 flex flex-col justify-between space-y-2">
      <div class="bg-slate-900/80 border border-slate-700/60 rounded-xl p-2.5">
        <div class="flex justify-between items-center mb-1">
          <span class="text-xs font-bold text-amber-300" id="c12s2_card_title">Western Ghats (Sahyadri)</span>
          <span class="text-[10px] px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 font-semibold uppercase" id="c12s2_badge">Global Hotspot #1</span>
        </div>
        <p class="text-xs text-slate-300 leading-relaxed" id="c12s2_card_body">
          Flanking India's western coastline, this mountain range features montane evergreen shola-grassland ecosystems. Home to over 5,000 vascular plant species and high endemism among amphibians and mammals.
        </p>
      </div>

      <div class="grid grid-cols-2 gap-2">
        <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2">
          <span class="text-[10px] text-slate-400 font-semibold uppercase block">Endemic Organisms</span>
          <span class="text-xs font-bold text-emerald-400" id="c12s2_endemic_list">Nilgiri Tahr, Lion-tailed Macaque</span>
        </div>
        <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2">
          <span class="text-[10px] text-slate-400 font-semibold uppercase block">Unique Floral Bloom</span>
          <span class="text-xs font-bold text-purple-400" id="c12s2_bloom">Neelakurinji (12-Year Cycle)</span>
        </div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-700/80 rounded-xl px-3 py-2 text-xs text-slate-300 flex items-center justify-between">
    <div>
      <span class="font-bold text-amber-400">Endemism Definition:</span> Species restricted exclusively to a defined geographical territory and found nowhere else on Earth.
    </div>
    <span class="text-[11px] text-cyan-300 font-semibold" id="c12s2_threat">Threat Status: Critical Forest Fragmentation</span>
  </div>
</div>
<script>
window.setC12S2 = function(hs){
  const btns = ['wg', 'eh', 'ib', 'sl'];
  btns.forEach(b => {
    const el = document.getElementById('c12s2_btn_' + b);
    if(el) el.className = (b === hs) ?
      'px-2 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition' :
      'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
    const mapEl = document.getElementById('c12s2_map_' + b);
    if(mapEl) mapEl.style.opacity = (b === hs) ? "1" : "0.2";
  });

  const sp = document.getElementById('c12s2_species');
  const title = document.getElementById('c12s2_card_title');
  const badge = document.getElementById('c12s2_badge');
  const body = document.getElementById('c12s2_card_body');
  const endemic = document.getElementById('c12s2_endemic_list');
  const bloom = document.getElementById('c12s2_bloom');
  const threat = document.getElementById('c12s2_threat');

  if(hs === 'wg'){
    sp.textContent = "Nilgiri Tahr & Lion-tailed Macaque";
    title.textContent = "Western Ghats (Sahyadri)";
    badge.textContent = "Global Hotspot #1";
    body.textContent = "A 1,600 km continuous chain moderating Indian monsoon precipitation. Features unique shola forests nestled in high-altitude valleys and cliff edges inhabited by cliff-dwelling Nilgiri tahr.";
    endemic.textContent = "Nilgiri Tahr, Purple Frog";
    bloom.textContent = "Neelakurinji (Every 12 Years)";
    threat.textContent = "Threat: Plantation monocultures & mining";
  } else if(hs === 'eh'){
    sp.textContent = "Snow Leopard & Red Panda";
    title.textContent = "Himalaya Hotspot";
    badge.textContent = "Global Hotspot #2";
    body.textContent = "Encompasses northern Pakistan, Nepal, Bhutan, and north-east Indian states. Rapid elevation gain produces dramatic habitat transitions from tropical foot-slopes to alpine scree.";
    endemic.textContent = "Golden Langur, Himalayan Monal";
    bloom.textContent = "Over 600 Rhododendron Species";
    threat.textContent = "Threat: Glacier retreat & road infrastructure";
  } else if(hs === 'ib'){
    sp.textContent = "Nepenthes khasiana Pitcher Plant";
    title.textContent = "Indo-Burma Hotspot";
    badge.textContent = "Global Hotspot #3";
    body.textContent = "Includes the Meghalaya plateau and northeastern hills south of the Brahmaputra. Known for karst limestone landscapes and carnivorous pitcher plants evolved on nitrogen-poor soils.";
    endemic.textContent = "Pitcher Plant (N. khasiana), Hoolock Gibbon";
    bloom.textContent = "Rare Epiphytic Blue Vanda Orchids";
    threat.textContent = "Threat: Shifting jhum cultivation & poaching";
  } else {
    sp.textContent = "Nicobar Megapode & Crab-eating Macaque";
    title.textContent = "Sundaland (Nicobar Islands)";
    badge.textContent = "Global Hotspot #4";
    body.textContent = "Encompassing the Nicobar archipelago with rich Indo-Malayan affinities. Pristine coastal mangroves, coral reefs, and dense wet tropical rain forests isolate ancient endemic insular lineages.";
    endemic.textContent = "Nicobar Tree Shrew, Nicobar Megapode";
    bloom.textContent = "Giant Mangrove Rhizophora Forests";
    threat.textContent = "Threat: Tsunami disturbance & coastal development";
  }
};
window.addEventListener('DOMContentLoaded', () => setC12S2('wg'));
</script>""",

    3: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Classification Criteria:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S3Mode('activity')" id="c12s3_btn_act" class="px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">Activity 12.1 (Day vs Night)</button>
        <button onclick="setC12S3Mode('matrix')" id="c12s3_btn_mat" class="px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">7 Taxonomic Criteria Matrix</button>
      </div>
    </div>
    <span class="text-xs text-slate-400" id="c12s3_subhead">Day vs Night Ecosystem Partitioning</span>
  </div>

  <!-- Activity 12.1 View -->
  <div id="c12s3_view_act" class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-between">
    <div class="flex items-center justify-center gap-3">
      <button onclick="toggleC12S3DNR('day')" id="c12s3_btn_day" class="px-4 py-1.5 text-xs font-bold rounded-lg bg-amber-500 text-slate-950 transition flex items-center gap-1.5 shadow-md shadow-amber-500/20">
        <span>☀️ Diurnal (Daytime)</span>
      </button>
      <button onclick="toggleC12S3DNR('night')" id="c12s3_btn_night" class="px-4 py-1.5 text-xs font-bold rounded-lg bg-slate-800 text-slate-400 hover:text-white transition flex items-center gap-1.5">
        <span>🌙 Nocturnal (Nighttime)</span>
      </button>
    </div>

    <!-- Visual Arena -->
    <div id="c12s3_arena" class="h-32 rounded-xl border border-slate-800 flex items-center justify-around p-3 bg-gradient-to-b from-sky-900/30 to-amber-950/20 transition-all">
      <!-- Dynamic cards rendered by JS -->
    </div>

    <div class="bg-cyan-950/30 border border-cyan-800/40 rounded-xl px-3 py-1.5 text-xs text-cyan-200" id="c12s3_act_desc">
      <strong>Activity 12.1 Observation:</strong> Identical physical habitats support completely distinct assemblages of species across 24 hours. Diurnal species rely on visual cues and sunlight, while nocturnal species activate acoustic, echolocation, and scent-based adaptations.
    </div>
  </div>

  <!-- 7 Criteria Matrix View -->
  <div id="c12s3_view_mat" class="hidden relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-between">
    <div class="grid grid-cols-4 sm:grid-cols-7 gap-1.5">
      <button onclick="selectC12S3Crit(1)" id="c12s3_cbtn_1" class="px-1.5 py-1 text-[11px] font-bold rounded bg-cyan-600 text-white transition">1. Morphology</button>
      <button onclick="selectC12S3Crit(2)" id="c12s3_cbtn_2" class="px-1.5 py-1 text-[11px] font-bold rounded bg-slate-900 text-slate-400 hover:text-white transition">2. Nutrition</button>
      <button onclick="selectC12S3Crit(3)" id="c12s3_cbtn_3" class="px-1.5 py-1 text-[11px] font-bold rounded bg-slate-900 text-slate-400 hover:text-white transition">3. Organs</button>
      <button onclick="selectC12S3Crit(4)" id="c12s3_cbtn_4" class="px-1.5 py-1 text-[11px] font-bold rounded bg-slate-900 text-slate-400 hover:text-white transition">4. Cell Type</button>
      <button onclick="selectC12S3Crit(5)" id="c12s3_cbtn_5" class="px-1.5 py-1 text-[11px] font-bold rounded bg-slate-900 text-slate-400 hover:text-white transition">5. Eco Niche</button>
      <button onclick="selectC12S3Crit(6)" id="c12s3_cbtn_6" class="px-1.5 py-1 text-[11px] font-bold rounded bg-slate-900 text-slate-400 hover:text-white transition">6. Reproduction</button>
      <button onclick="selectC12S3Crit(7)" id="c12s3_cbtn_7" class="px-1.5 py-1 text-[11px] font-bold rounded bg-slate-900 text-slate-400 hover:text-white transition">7. DNA Code</button>
    </div>

    <div class="bg-slate-900/80 border border-slate-700/60 rounded-xl p-3 my-1">
      <div class="flex items-center justify-between mb-1.5">
        <h4 class="text-xs font-bold text-cyan-300" id="c12s3_crit_title">Criterion 1: External Morphology</h4>
        <span class="text-[10px] px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-mono" id="c12s3_crit_tag">Observable Body Architecture</span>
      </div>
      <p class="text-xs text-slate-300 leading-relaxed" id="c12s3_crit_body">
        Structural traits like body shape, symmetry, presence of appendages, scales, feathers, or floral whorls. While essential as an initial sorting guide, relying on morphology alone can be misleading due to convergent evolution (e.g., dolphins vs sharks).
      </p>
    </div>

    <div class="grid grid-cols-2 gap-2 text-xs">
      <div class="bg-slate-900/50 border border-slate-800 rounded-lg p-2">
        <span class="text-[10px] text-slate-400 font-semibold uppercase block">Application Example</span>
        <span class="text-emerald-300 font-semibold" id="c12s3_crit_ex">Grouped plants by leaf arrangement and flower parts.</span>
      </div>
      <div class="bg-slate-900/50 border border-slate-800 rounded-lg p-2">
        <span class="text-[10px] text-slate-400 font-semibold uppercase block">Taxonomic Weight</span>
        <span class="text-amber-300 font-semibold" id="c12s3_crit_wt">Initial Field Survey &amp; Primary Grouping</span>
      </div>
    </div>
  </div>
</div>
<script>
window.setC12S3Mode = function(m){
  document.getElementById('c12s3_btn_act').className = (m === 'activity') ?
    'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition' :
    'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  document.getElementById('c12s3_btn_mat').className = (m === 'matrix') ?
    'px-2.5 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition' :
    'px-2.5 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';

  document.getElementById('c12s3_view_act').className = (m === 'activity') ?
    'relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-between' :
    'hidden';
  document.getElementById('c12s3_view_mat').className = (m === 'matrix') ?
    'relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-between' :
    'hidden';
};

window.toggleC12S3DNR = function(time){
  const dayBtn = document.getElementById('c12s3_btn_day');
  const nightBtn = document.getElementById('c12s3_btn_night');
  const arena = document.getElementById('c12s3_arena');
  const desc = document.getElementById('c12s3_act_desc');

  if(time === 'day'){
    dayBtn.className = 'px-4 py-1.5 text-xs font-bold rounded-lg bg-amber-500 text-slate-950 transition flex items-center gap-1.5 shadow-md shadow-amber-500/20';
    nightBtn.className = 'px-4 py-1.5 text-xs font-bold rounded-lg bg-slate-800 text-slate-400 hover:text-white transition flex items-center gap-1.5';
    arena.className = 'h-32 rounded-xl border border-slate-800 flex items-center justify-around p-3 bg-gradient-to-b from-sky-900/30 to-amber-950/20 transition-all';
    arena.innerHTML = `
      <div class="flex flex-col items-center p-2 rounded-lg bg-slate-900/70 border border-amber-500/30">
        <span class="text-2xl">🦋</span>
        <span class="text-xs font-bold text-amber-300 mt-1">Sunbirds &amp; Butterflies</span>
        <span class="text-[10px] text-slate-400">Diurnal Nectar Pollinators</span>
      </div>
      <div class="flex flex-col items-center p-2 rounded-lg bg-slate-900/70 border border-emerald-500/30">
        <span class="text-2xl">🌻</span>
        <span class="text-xs font-bold text-emerald-300 mt-1">Heliotropic Flowers</span>
        <span class="text-[10px] text-slate-400">Open for Solar Exposure</span>
      </div>
      <div class="flex flex-col items-center p-2 rounded-lg bg-slate-900/70 border border-sky-500/30">
        <span class="text-2xl">🦅</span>
        <span class="text-xs font-bold text-sky-300 mt-1">Black Kite / Eagle</span>
        <span class="text-[10px] text-slate-400">High-Acuity Visual Predators</span>
      </div>
    `;
    desc.innerHTML = "<strong>Activity 12.1 Day Phase:</strong> Daylight triggers phototactic foraging. Butterflies, sunbirds, and diurnal raptors operate via sharp optical vision and thermal soaring.";
  } else {
    nightBtn.className = 'px-4 py-1.5 text-xs font-bold rounded-lg bg-indigo-600 text-white transition flex items-center gap-1.5 shadow-md shadow-indigo-600/30';
    dayBtn.className = 'px-4 py-1.5 text-xs font-bold rounded-lg bg-slate-800 text-slate-400 hover:text-white transition flex items-center gap-1.5';
    arena.className = 'h-32 rounded-xl border border-indigo-900/60 flex items-center justify-around p-3 bg-gradient-to-b from-slate-950 to-indigo-950/40 transition-all';
    arena.innerHTML = `
      <div class="flex flex-col items-center p-2 rounded-lg bg-slate-900/70 border border-indigo-500/30">
        <span class="text-2xl">🦇</span>
        <span class="text-xs font-bold text-indigo-300 mt-1">Microbats &amp; Flying Foxes</span>
        <span class="text-[10px] text-slate-400">Echolocation &amp; Fruit Dispersal</span>
      </div>
      <div class="flex flex-col items-center p-2 rounded-lg bg-slate-900/70 border border-purple-500/30">
        <span class="text-2xl">🌸</span>
        <span class="text-xs font-bold text-purple-300 mt-1">Raat ki Rani (Jasmine)</span>
        <span class="text-[10px] text-slate-400">Intense Nocturnal Fragrance</span>
      </div>
      <div class="flex flex-col items-center p-2 rounded-lg bg-slate-900/70 border border-slate-700">
        <span class="text-2xl">🦉</span>
        <span class="text-xs font-bold text-slate-300 mt-1">Spotted Owlet</span>
        <span class="text-[10px] text-slate-400">Asymmetric Auditory Hunting</span>
      </div>
    `;
    desc.innerHTML = "<strong>Activity 12.1 Night Phase:</strong> In darkness, visual classification gives way to acoustic, olfaction, and tactile adaptations. Flowers produce heavy fragrances for night-flying sphingid moths and bats.";
  }
};

window.selectC12S3Crit = function(num){
  for(let i=1; i<=7; i++){
    const b = document.getElementById('c12s3_cbtn_' + i);
    if(b) b.className = (i === num) ?
      'px-1.5 py-1 text-[11px] font-bold rounded bg-cyan-600 text-white transition' :
      'px-1.5 py-1 text-[11px] font-bold rounded bg-slate-900 text-slate-400 hover:text-white transition';
  }

  const title = document.getElementById('c12s3_crit_title');
  const tag = document.getElementById('c12s3_crit_tag');
  const body = document.getElementById('c12s3_crit_body');
  const ex = document.getElementById('c12s3_crit_ex');
  const wt = document.getElementById('c12s3_crit_wt');

  const criteriaData = {
    1: {
      t: "Criterion 1: External Morphology",
      tag: "Observable Outer Structure",
      b: "Physical features such as body symmetry, limbs, wings, leaf venation, and floral geometry. Provides the foundational layer for taxonomists in botanical and zoological keys.",
      ex: "Separating monocots with parallel venation from dicots with reticulate venation.",
      wt: "Foundational Taxonomic Sorting"
    },
    2: {
      t: "Criterion 2: Mode of Nutrition",
      tag: "Bio-energetic Acquisition",
      b: "Distinguishes autotrophs (photosynthetic plants synthesizing glucose from solar energy) from heterotrophs. Heterotrophs further divide into ingestive animals and absorptive saprophytic fungi.",
      ex: "Classifying non-photosynthetic fungi separate from green Plantae.",
      wt: "Fundamental Kingdom-Level Divider"
    },
    3: {
      t: "Criterion 3: Internal Organs & Anatomy",
      tag: "Tissue & Organ Complexity",
      b: "Examines anatomical organization: cellular grade (sponges) vs tissue grade (cnidaria) vs organ-system grade (annelids, chordates). Evaluates coelom type and digestive completeness.",
      ex: "Differentiating pseudocoelomate roundworms from true coelomate earthworms.",
      wt: "Phylum & Class Differentiation"
    },
    4: {
      t: "Criterion 4: Cell Structure & Organization",
      tag: "Cytological Architecture",
      b: "First divides prokaryotes (lacking nuclear membrane, e.g. Monera) from eukaryotes (membrane-bound nucleus and organelles). Evaluates whether cell wall contains cellulose, chitin, or peptidoglycan.",
      ex: "Isolating bacteria into Kingdom Monera away from unicellular protists.",
      wt: "Primary Super-Kingdom Threshold"
    },
    5: {
      t: "Criterion 5: Ecological Niche & Role",
      tag: "Trophic Functional Position",
      b: "Identifies whether an organism operates as a primary producer, primary/secondary consumer, or decomposer. Essential for understanding how biodiversity maintains nutrient cycling.",
      ex: "Categorizing forest mycorrhizal fungi as decomposers/mutualistic recyclers.",
      wt: "Ecological System Integration"
    },
    6: {
      t: "Criterion 6: Reproduction & Life Cycle",
      tag: "Generational Continuity",
      b: "Evaluates asexual fission, budding, spore formation, seed production (gymnosperms vs angiosperms), and larval metamorphosis (e.g. tadpole to adult frog).",
      ex: "Distinguishing non-seed ferns (spores) from naked-seeded conifers.",
      wt: "Division & Family Classification"
    },
    7: {
      t: "Criterion 7: DNA & Genetic Similarity",
      tag: "Molecular Phylogenetics",
      b: "Compares nucleotide base sequences of conserved genes (e.g., 16S/18S ribosomal RNA). Reveals true evolutionary lineage, resolving ambiguities created by physical convergent evolution.",
      ex: "Proving birds are avian theropod dinosaurs via molecular phylogenetics.",
      wt: "Definitive Modern Evolutionary Standard"
    }
  };

  const d = criteriaData[num];
  title.textContent = d.t;
  tag.textContent = d.tag;
  body.textContent = d.b;
  ex.textContent = d.ex;
  wt.textContent = d.wt;
};

window.addEventListener('DOMContentLoaded', () => {
  toggleC12S3DNR('day');
  selectC12S3Crit(1);
});
</script>""",

    4: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Pakke Tiger Reserve:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S4('great')" id="c12s4_btn_great" class="px-2 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">Great Hornbill</button>
        <button onclick="setC12S4('rufous')" id="c12s4_btn_rufous" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Rufous-necked</button>
        <button onclick="setC12S4('wreathed')" id="c12s4_btn_wreathed" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Wreathed</button>
        <button onclick="setC12S4('pied')" id="c12s4_btn_pied" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Oriental Pied</button>
      </div>
    </div>
    <span class="text-xs text-slate-400" id="c12s4_sciname">Buceros bicornis</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col md:flex-row gap-3 items-center">
    <!-- Visual Tree Canopy & Niche Partitioning SVG -->
    <div class="w-full md:w-1/2 h-44 flex items-center justify-center bg-slate-900/40 rounded-xl border border-slate-800/80 p-1">
      <svg viewBox="0 0 240 180" class="w-full h-full">
        <!-- Giant Emergent Tree -->
        <rect x="0" y="0" width="240" height="180" fill="#09141f"/>
        <rect x="95" y="40" width="22" height="140" fill="#582f0e"/>
        <!-- Branching arms -->
        <path d="M100,80 Q60,65 30,75" stroke="#582f0e" stroke-width="7" fill="none"/>
        <path d="M115,60 Q150,45 200,50" stroke="#582f0e" stroke-width="9" fill="none"/>
        <path d="M110,120 Q160,110 210,130" stroke="#582f0e" stroke-width="6" fill="none"/>
        <!-- Foliage canopies -->
        <circle cx="30" cy="70" r="28" fill="#1b4332" opacity="0.8"/>
        <circle cx="200" cy="45" r="38" fill="#2d6a4f" opacity="0.9"/>
        <circle cx="205" cy="130" r="24" fill="#1b4332" opacity="0.8"/>
        <circle cx="106" cy="30" r="35" fill="#40916c" opacity="0.85"/>

        <!-- Nest cavity highlighting -->
        <ellipse id="c12s4_cavity" cx="106" cy="65" rx="8" ry="12" fill="#1e1e1e" stroke="#f59e0b" stroke-width="2"/>
        <circle id="c12s4_bird_dot" cx="106" cy="65" r="4" fill="#f59e0b"/>
        <text id="c12s4_svg_label" x="125" y="70" fill="#fde047" font-size="9" font-weight="bold">Top Canopy Nest</text>
      </svg>
    </div>

    <!-- Comparative Niche Metrics -->
    <div class="w-full md:w-1/2 flex flex-col justify-between space-y-2">
      <div class="bg-slate-900/80 border border-slate-700/60 rounded-xl p-2.5">
        <h4 class="text-xs font-bold text-amber-300 mb-1" id="c12s4_title">Great Hornbill (Buceros bicornis)</h4>
        <p class="text-xs text-slate-300 leading-relaxed" id="c12s4_body">
          India's largest hornbill. Requires enormous mature forest trees with massive natural cavities for nesting. Female seals herself inside cavity with mud and droppings during incubation, relying on male for food.
        </p>
      </div>

      <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2">
          <span class="text-[10px] text-slate-400 font-semibold uppercase block">Nest Cavity Girth</span>
          <span class="text-xs font-bold text-amber-400" id="c12s4_girth">&gt; 120 cm DBH Required</span>
        </div>
        <div class="bg-slate-900/60 border border-slate-800 rounded-lg p-2">
          <span class="text-[10px] text-slate-400 font-semibold uppercase block">Primary Foraging Diet</span>
          <span class="text-xs font-bold text-emerald-400" id="c12s4_diet">Large Wild Figs &amp; Drupes</span>
        </div>
      </div>
    </div>
  </div>

  <div class="bg-slate-900/90 border border-slate-700/80 rounded-xl px-3 py-2 text-xs text-slate-300">
    <strong class="text-cyan-400">Activity 12.2 Insight (Competitive Exclusion Avoided):</strong> Though all four hornbill species live in Arunachal's Pakke Tiger Reserve, differences in body mass, nest-cavity diameters, and vertical foraging strata prevent direct competition, enabling peaceful coexistence!
  </div>
</div>
<script>
window.setC12S4 = function(h){
  const btns = ['great', 'rufous', 'wreathed', 'pied'];
  btns.forEach(b => {
    const el = document.getElementById('c12s4_btn_' + b);
    if(el) el.className = (b === h) ?
      'px-2 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition' :
      'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  });

  const sciname = document.getElementById('c12s4_sciname');
  const title = document.getElementById('c12s4_title');
  const body = document.getElementById('c12s4_body');
  const girth = document.getElementById('c12s4_girth');
  const diet = document.getElementById('c12s4_diet');
  const cav = document.getElementById('c12s4_cavity');
  const dot = document.getElementById('c12s4_bird_dot');
  const lbl = document.getElementById('c12s4_svg_label');

  if(h === 'great'){
    sciname.textContent = "Buceros bicornis (Arunachal State Bird)";
    title.textContent = "Great Hornbill (Massive Canopy Specialist)";
    body.textContent = "Largest species with a prominent yellow-black casque. Needs mature emergent trees like Tetrameles nudiflora with massive hollows. Consumes large lipid-rich fruits and acts as a key forest seed disperser.";
    girth.textContent = "> 120 cm DBH Tree Cavity";
    diet.textContent = "Large Figs, Lauraceae, Aglaia";
    cav.setAttribute('cx', '106'); cav.setAttribute('cy', '65'); cav.setAttribute('rx', '9'); cav.setAttribute('ry', '13');
    dot.setAttribute('cx', '106'); dot.setAttribute('cy', '65');
    lbl.setAttribute('x', '125'); lbl.setAttribute('y', '70'); lbl.textContent = "Top Canopy Hollow (30m)";
  } else if(h === 'rufous'){
    sciname.textContent = "Aceros nipalensis";
    title.textContent = "Rufous-necked Hornbill (High Elevation)";
    body.textContent = "Lacks a heavy casque. Inhabits higher elevation sub-tropical hill forests above 1,000 meters. Feeds predominantly on larger drupes and nests in deep montane hardwood cavities.";
    girth.textContent = "90 – 110 cm DBH Cavities";
    diet.textContent = "Oak fruits, Drupes, Mountain Berries";
    cav.setAttribute('cx', '195'); cav.setAttribute('cy', '50'); cav.setAttribute('rx', '8'); cav.setAttribute('ry', '11');
    dot.setAttribute('cx', '195'); dot.setAttribute('cy', '50');
    lbl.setAttribute('x', '140'); lbl.setAttribute('y', '40'); lbl.textContent = "High Ridge Canopy";
  } else if(h === 'wreathed'){
    sciname.textContent = "Rhyticeros undulatus";
    title.textContent = "Wreathed Hornbill (Long-Distance Nomad)";
    body.textContent = "Possesses a corrugated casque base and vivid yellow/blue throat pouch. Highly nomadic species that flies vast distances across valleys in large flocks tracking fluctuating fruit seasons.";
    girth.textContent = "80 – 100 cm DBH Cavities";
    diet.textContent = "Wide Array of Mid-Sized Drupes";
    cav.setAttribute('cx', '45'); cav.setAttribute('cy', '78'); cav.setAttribute('rx', '7'); cav.setAttribute('ry', '10');
    dot.setAttribute('cx', '45'); dot.setAttribute('cy', '78');
    lbl.setAttribute('x', '20'); lbl.setAttribute('y', '110'); lbl.textContent = "Mid-Canopy Branch";
  } else {
    sciname.textContent = "Anthracoceros albirostris";
    title.textContent = "Oriental Pied Hornbill (Flexible Generalist)";
    body.textContent = "The smallest and most adaptable hornbill in Pakke. Can tolerate secondary forests and riverine fringes. Nests in smaller tree hollows and feeds on small berries, figs, and insects.";
    girth.textContent = "50 – 70 cm DBH Cavities";
    diet.textContent = "Small Berries, Insects, Lizards";
    cav.setAttribute('cx', '205'); cav.setAttribute('cy', '130'); cav.setAttribute('rx', '6'); cav.setAttribute('ry', '8');
    dot.setAttribute('cx', '205'); dot.setAttribute('cy', '130');
    lbl.setAttribute('x', '135'); lbl.setAttribute('y', '150'); lbl.textContent = "Lower Secondary Hollow";
  }
};
window.addEventListener('DOMContentLoaded', () => setC12S4('great'));
</script>""",

    5: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-purple-400 uppercase tracking-wider">Evolution of Kingdoms:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S5('aristotle')" id="c12s5_btn_ari" class="px-2 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition">Aristotle (350 BCE)</button>
        <button onclick="setC12S5('linnaeus')" id="c12s5_btn_lin" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Linnaeus 2K (1758)</button>
        <button onclick="setC12S5('haeckel')" id="c12s5_btn_hae" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Haeckel 3K (1866)</button>
        <button onclick="setC12S5('copeland')" id="c12s5_btn_cop" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Copeland 4K (1938)</button>
        <button onclick="setC12S5('whittaker')" id="c12s5_btn_whi" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Whittaker 5K (1969)</button>
      </div>
    </div>
    <span class="text-xs text-purple-300 font-mono" id="c12s5_kcount">Classification: Habitat-Based</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-between">
    <!-- Visual Kingdom Blocks -->
    <div id="c12s5_kingdom_blocks" class="grid grid-cols-2 sm:grid-cols-5 gap-2 my-auto">
      <!-- Dynamic Kingdom Badges -->
    </div>

    <!-- Details Box -->
    <div class="bg-slate-900/80 border border-slate-700/60 rounded-xl p-3">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-bold text-purple-300" id="c12s5_era_title">Aristotle's Ancient System (350 BCE)</span>
        <span class="text-[10px] px-2 py-0.5 rounded bg-purple-500/20 text-purple-300 font-semibold" id="c12s5_era_badge">Habitat Sorting</span>
      </div>
      <p class="text-xs text-slate-300 leading-relaxed" id="c12s5_era_desc">
        Aristotle classified living beings on simple habitat criteria: Land Dwellers, Water Dwellers, and Air Dwellers. This artificially grouped radically different animals together (e.g. fish, whales, and octopuses under water).
      </p>
    </div>

    <!-- Major limitation / Breakthrough -->
    <div class="grid grid-cols-2 gap-2 text-xs">
      <div class="bg-slate-900/50 border border-slate-800 rounded-lg p-2">
        <span class="text-[10px] text-slate-400 font-semibold uppercase block">Primary Criteria Used</span>
        <span class="text-amber-300 font-semibold" id="c12s5_criteria">Habitat (Land / Air / Water)</span>
      </div>
      <div class="bg-slate-900/50 border border-slate-800 rounded-lg p-2">
        <span class="text-[10px] text-slate-400 font-semibold uppercase block">Flaw / Limitation Solved</span>
        <span class="text-rose-300 font-semibold" id="c12s5_flaw">Grouped birds and insects together</span>
      </div>
    </div>
  </div>
</div>
<script>
window.setC12S5 = function(era){
  const btns = ['ari', 'lin', 'hae', 'cop', 'whi'];
  btns.forEach(b => {
    const el = document.getElementById('c12s5_btn_' + b);
    if(el) el.className = (b === era.substring(0,3)) ?
      'px-2 py-1 text-xs font-bold rounded-md bg-purple-600 text-white transition' :
      'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  });

  const kcount = document.getElementById('c12s5_kcount');
  const blocks = document.getElementById('c12s5_kingdom_blocks');
  const title = document.getElementById('c12s5_era_title');
  const badge = document.getElementById('c12s5_era_badge');
  const desc = document.getElementById('c12s5_era_desc');
  const criteria = document.getElementById('c12s5_criteria');
  const flaw = document.getElementById('c12s5_flaw');

  if(era === 'aristotle'){
    kcount.textContent = "System: 3 Artificial Habitats";
    title.textContent = "Aristotle (c. 350 BCE) - Habitat Classification";
    badge.textContent = "Ancient Artificial System";
    desc.textContent = "Grouped organisms by where they reside: Terrestrial (land), Aquatic (water), and Aerial (air). While intuitive, it failed to reflect underlying anatomical and evolutionary relationships.";
    criteria.textContent = "Habitat (Land / Water / Air)";
    flaw.textContent = "Whales lumped with fish; bats lumped with birds";
    blocks.innerHTML = `
      <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700 text-center">
        <span class="text-xs font-bold text-emerald-400 block">Land Dwellers</span>
        <span class="text-[10px] text-slate-400">Horses, Snakes, Humans</span>
      </div>
      <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700 text-center">
        <span class="text-xs font-bold text-cyan-400 block">Water Dwellers</span>
        <span class="text-[10px] text-slate-400">Fish, Whales, Jellyfish</span>
      </div>
      <div class="p-2.5 rounded-xl bg-slate-800/80 border border-slate-700 text-center col-span-2 sm:col-span-1">
        <span class="text-xs font-bold text-amber-400 block">Air Dwellers</span>
        <span class="text-[10px] text-slate-400">Birds, Bats, Butterflies</span>
      </div>
    `;
  } else if(era === 'linnaeus'){
    kcount.textContent = "2 Kingdoms (1758)";
    title.textContent = "Carolus Linnaeus (1758) - Two Kingdom System";
    badge.textContent = "Plantae & Animalia";
    desc.textContent = "Divided all living things into Plantae (fixed, autotrophic, cell-walled) and Animalia (motile, ingestive, lacking cell walls). Could not classify microbes, fungi, or distinguish prokaryotes.";
    criteria.textContent = "Motility & Cell Wall Presence";
    flaw.textContent = "Forced non-photosynthetic fungi & bacteria into Plantae";
    blocks.innerHTML = `
      <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-700 text-center sm:col-span-2">
        <span class="text-xs font-bold text-emerald-300 block">Kingdom Plantae</span>
        <span class="text-[10px] text-slate-300">Trees, Herbs, Fungi, Bacteria, Algae</span>
      </div>
      <div class="p-3 rounded-xl bg-blue-950/40 border border-blue-700 text-center sm:col-span-3">
        <span class="text-xs font-bold text-blue-300 block">Kingdom Animalia</span>
        <span class="text-[10px] text-slate-300">Invertebrates, Birds, Fish, Mammals</span>
      </div>
    `;
  } else if(era === 'haeckel'){
    kcount.textContent = "3 Kingdoms (1866)";
    title.textContent = "Ernst Haeckel (1866) - Three Kingdom System";
    badge.textContent = "Added Protista";
    desc.textContent = "With microscopy advancing, Haeckel introduced Kingdom Protista to house all unicellular organisms (Amoeba, bacteria, simple algae) that did not fit neatly into plants or animals.";
    criteria.textContent = "Unicellular vs Multicellular Organization";
    flaw.textContent = "Lumped nucleated Amoeba together with anucleated bacteria";
    blocks.innerHTML = `
      <div class="p-2.5 rounded-xl bg-purple-950/40 border border-purple-600 text-center">
        <span class="text-xs font-bold text-purple-300 block">Protista</span>
        <span class="text-[9px] text-slate-300">Microbes &amp; Unicells</span>
      </div>
      <div class="p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-600 text-center">
        <span class="text-xs font-bold text-emerald-300 block">Plantae</span>
        <span class="text-[9px] text-slate-300">Multicellular Plants</span>
      </div>
      <div class="p-2.5 rounded-xl bg-blue-950/40 border border-blue-600 text-center col-span-2 sm:col-span-1">
        <span class="text-xs font-bold text-blue-300 block">Animalia</span>
        <span class="text-[9px] text-slate-300">Multicellular Animals</span>
      </div>
    `;
  } else if(era === 'copeland'){
    kcount.textContent = "4 Kingdoms (1938)";
    title.textContent = "Herbert Copeland (1938) - Four Kingdom System";
    badge.textContent = "Added Monera";
    desc.textContent = "Recognized the critical cytological divide between prokaryotes and eukaryotes. Created Kingdom Monera for organisms lacking a membrane-bound nucleus (bacteria and cyanobacteria).";
    criteria.textContent = "Prokaryotic vs Eukaryotic Cell Structure";
    flaw.textContent = "Fungi were still misplaced inside Kingdom Plantae";
    blocks.innerHTML = `
      <div class="p-2 rounded-xl bg-amber-950/40 border border-amber-600 text-center">
        <span class="text-xs font-bold text-amber-300 block">Monera</span>
        <span class="text-[9px] text-slate-300">Prokaryotes</span>
      </div>
      <div class="p-2 rounded-xl bg-purple-950/40 border border-purple-600 text-center">
        <span class="text-xs font-bold text-purple-300 block">Protista</span>
        <span class="text-[9px] text-slate-300">Eukaryotic Unicells</span>
      </div>
      <div class="p-2 rounded-xl bg-emerald-950/40 border border-emerald-600 text-center">
        <span class="text-xs font-bold text-emerald-300 block">Plantae</span>
        <span class="text-[9px] text-slate-300">Plants &amp; Fungi</span>
      </div>
      <div class="p-2 rounded-xl bg-blue-950/40 border border-blue-600 text-center">
        <span class="text-xs font-bold text-blue-300 block">Animalia</span>
        <span class="text-[9px] text-slate-300">Animals</span>
      </div>
    `;
  } else {
    kcount.textContent = "5 Kingdoms (1969)";
    title.textContent = "Robert Whittaker (1969) - Five Kingdom System";
    badge.textContent = "Added Fungi (NCERT Standard)";
    desc.textContent = "Whittaker separated Fungi into their own kingdom based on chitinous cell walls and absorptive saprophytic nutrition. Standard system based on cell complexity, body organization, and nutritional mode.";
    criteria.textContent = "Cell Type, Body Complexity, Nutrition &amp; Ecology";
    flaw.textContent = "Resolved major taxonomic conflicts for cellular life";
    blocks.innerHTML = `
      <div class="p-2 rounded-xl bg-amber-950/40 border border-amber-500 text-center">
        <span class="text-xs font-bold text-amber-300 block">Monera</span>
        <span class="text-[8px] text-slate-300">Bacteria (Prokaryotes)</span>
      </div>
      <div class="p-2 rounded-xl bg-purple-950/40 border border-purple-500 text-center">
        <span class="text-xs font-bold text-purple-300 block">Protista</span>
        <span class="text-[8px] text-slate-300">Amoeba, Euglena</span>
      </div>
      <div class="p-2 rounded-xl bg-rose-950/40 border border-rose-500 text-center">
        <span class="text-xs font-bold text-rose-300 block">Fungi</span>
        <span class="text-[8px] text-slate-300">Absorptive Chitin</span>
      </div>
      <div class="p-2 rounded-xl bg-emerald-950/40 border border-emerald-500 text-center">
        <span class="text-xs font-bold text-emerald-300 block">Plantae</span>
        <span class="text-[8px] text-slate-300">Photosynthetic Autotrophs</span>
      </div>
      <div class="p-2 rounded-xl bg-blue-950/40 border border-blue-500 text-center">
        <span class="text-xs font-bold text-blue-300 block">Animalia</span>
        <span class="text-[8px] text-slate-300">Ingestive Heterotrophs</span>
      </div>
    `;
  }
};
window.addEventListener('DOMContentLoaded', () => setC12S5('whittaker'));
</script>""",

    6: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Kingdom Monera:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S6('cell')" id="c12s6_btn_cell" class="px-2 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition">Prokaryotic Cell</button>
        <button onclick="setC12S6('biogas')" id="c12s6_btn_biogas" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Biogas Digester (1957)</button>
        <button onclick="setC12S6('fossil')" id="c12s6_btn_fossil" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Fossil Stromatolites</button>
      </div>
    </div>
    <span class="text-xs text-amber-300 font-mono" id="c12s6_badge">Prokaryote &bull; Non-Enveloped DNA</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c12s6_visual" class="w-full max-w-lg flex flex-col items-center justify-center">
      <!-- SVG rendering container -->
    </div>

    <div class="w-full max-w-lg mt-2 bg-slate-900/80 border border-slate-700/60 rounded-xl p-2.5">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-bold text-amber-300" id="c12s6_title">Prokaryotic Bacterial Architecture</span>
        <span class="text-[10px] text-slate-400 font-mono" id="c12s6_tag">No Nuclear Envelope</span>
      </div>
      <p class="text-xs text-slate-300 leading-relaxed" id="c12s6_body">
        Monerans lack membrane-bound organelles (no mitochondria, endoplasmic reticulum, or nucleus). Genetic material is an unbound circular DNA strand located in the nucleoid region. Cell wall contains peptidoglycan.
      </p>
    </div>
  </div>

  <div class="bg-amber-950/30 border border-amber-800/40 rounded-xl px-3 py-1.5 text-xs text-amber-200 flex items-center justify-between">
    <span id="c12s6_foot">Indian Innovation: Ram Bux Singh (1957) engineered the world's first practical continuous-flow biogas digester in Ramnagar, UP, harnessing anaerobic methanogenic archaebacteria!</span>
  </div>
</div>
<script>
window.setC12S6 = function(view){
  const btns = ['cell', 'biogas', 'fossil'];
  btns.forEach(b => {
    const el = document.getElementById('c12s6_btn_' + b);
    if(el) el.className = (b === view) ?
      'px-2 py-1 text-xs font-bold rounded-md bg-amber-600 text-white transition' :
      'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  });

  const badge = document.getElementById('c12s6_badge');
  const vis = document.getElementById('c12s6_visual');
  const title = document.getElementById('c12s6_title');
  const tag = document.getElementById('c12s6_tag');
  const body = document.getElementById('c12s6_body');
  const foot = document.getElementById('c12s6_foot');

  if(view === 'cell'){
    badge.textContent = "Prokaryote • Non-Enveloped DNA";
    vis.innerHTML = `
      <svg viewBox="0 0 400 130" class="w-full h-32">
        <!-- Capsule & Cell Wall -->
        <rect x="50" y="20" width="260" height="90" rx="45" fill="#14532d" stroke="#22c55e" stroke-width="3"/>
        <!-- Plasma membrane -->
        <rect x="58" y="28" width="244" height="74" rx="37" fill="#052e16" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="4,2"/>
        <!-- Naked circular nucleoid DNA -->
        <path d="M120,65 Q140,40 170,60 T200,65 T230,55 T180,80 T130,65" fill="none" stroke="#facc15" stroke-width="3"/>
        <text x="145" y="68" fill="#fef08a" font-size="9" font-weight="bold">Nucleoid DNA</text>
        <!-- 70S Ribosomes -->
        <circle cx="95" cy="50" r="2.5" fill="#38bdf8"/>
        <circle cx="110" cy="80" r="2.5" fill="#38bdf8"/>
        <circle cx="250" cy="55" r="2.5" fill="#38bdf8"/>
        <circle cx="260" cy="75" r="2.5" fill="#38bdf8"/>
        <circle cx="220" cy="85" r="2.5" fill="#38bdf8"/>
        <!-- Flagellum -->
        <path d="M50,65 Q20,40 10,70 T-10,60" fill="none" stroke="#22c55e" stroke-width="2.5" stroke-linecap="round"/>
        <!-- Labels -->
        <text x="320" y="45" fill="#4ade80" font-size="9">Cell Wall (Peptidoglycan)</text>
        <text x="320" y="75" fill="#38bdf8" font-size="9">70S Ribosomes</text>
        <text x="320" y="105" fill="#22c55e" font-size="9">Locomotory Flagellum</text>
      </svg>
    `;
    title.textContent = "Prokaryotic Cell Architecture";
    tag.textContent = "Bacteria & Cyanobacteria";
    body.textContent = "Prokaryotic cells have no membrane-enclosed nucleus or organelles. Their metabolic enzymes are distributed in the cytosol or cell membrane folds (mesosomes). Cyanobacteria possess photosynthetic thylakoid membranes releasing oxygen.";
    foot.textContent = "Cyanobacteria introduced oxygen into Earth's primordial atmosphere over 2.5 billion years ago!";
  } else if(view === 'biogas'){
    badge.textContent = "Methanogenic Archaea • Circular Economy";
    vis.innerHTML = `
      <svg viewBox="0 0 400 130" class="w-full h-32">
        <!-- Underground Digester Tank -->
        <rect x="130" y="35" width="140" height="90" rx="10" fill="#1c1917" stroke="#78350f" stroke-width="2"/>
        <!-- Slurry level -->
        <rect x="132" y="65" width="136" height="58" rx="8" fill="#451a03"/>
        <text x="155" y="95" fill="#fde047" font-size="9" font-weight="bold">Anaerobic Slurry</text>
        <text x="145" y="110" fill="#cbd5e1" font-size="8">Methanogen Archaea</text>
        <!-- Inlet Pipe (Dung/Water) -->
        <path d="M70,30 L130,70" stroke="#a16207" stroke-width="8" fill="none"/>
        <text x="50" y="25" fill="#ca8a04" font-size="8" font-weight="bold">Inlet: Cow Dung + Water</text>
        <!-- Biogas Dome & Outlet -->
        <path d="M165,35 Q200,10 235,35" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
        <line x1="200" y1="20" x2="200" y2="5" stroke="#38bdf8" stroke-width="3"/>
        <text x="210" y="15" fill="#38bdf8" font-size="9" font-weight="bold">Biogas (65% CH₄)</text>
        <!-- Outlet Fertilizer Slurry -->
        <path d="M270,75 L330,40" stroke="#15803d" stroke-width="7" fill="none"/>
        <text x="310" y="30" fill="#4ade80" font-size="8" font-weight="bold">Organic Manure</text>
      </svg>
    `;
    title.textContent = "Ram Bux Singh Biogas Digester (1957, Ramnagar UP)";
    tag.textContent = "Methanogenesis & Bio-energy";
    body.textContent = "Anaerobic methanogens (Archaea) decompose agricultural biomass and cattle waste, producing combustible methane (CH₄) gas for clean rural cooking while generating mineral-rich nitrogen-phosphorus bio-manure.";
    foot.textContent = "Indian scientist Ram Bux Singh standardized biogas generation, pioneering decentralized rural clean energy worldwide.";
  } else {
    badge.textContent = "Precambrian Stromatolites • Rajasthan & MP";
    vis.innerHTML = `
      <svg viewBox="0 0 400 130" class="w-full h-32">
        <!-- Geological Bedrock -->
        <rect x="30" y="85" width="340" height="40" fill="#334155"/>
        <!-- Layered Stromatolite Domes -->
        <path d="M60,85 Q110,20 160,85" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
        <path d="M75,85 Q110,35 145,85" fill="none" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3,2"/>
        <path d="M90,85 Q110,50 130,85" fill="none" stroke="#cbd5e1" stroke-width="1.5"/>

        <path d="M170,85 Q230,10 290,85" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
        <path d="M190,85 Q230,30 270,85" fill="none" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3,2"/>
        <path d="M210,85 Q230,50 250,85" fill="none" stroke="#cbd5e1" stroke-width="1.5"/>

        <text x="180" y="45" fill="#f1f5f9" font-size="10" font-weight="bold">Layered Cyanobacterial Mats</text>
        <text x="80" y="110" fill="#94a3b8" font-size="9">Vindhyan / Aravalli Supergroup (~1.5 to 2.5 Billion Years Old)</text>
      </svg>
    `;
    title.textContent = "Fossil Stromatolites (Rajasthan & Madhya Pradesh)";
    tag.textContent = "Deep Geological Time";
    body.textContent = "Stromatolites are layered bio-chemical accretionary structures formed by colonies of cyanobacteria trapping sediment grains. Abundant stromatolite rock formations across Rajasthan and the Vindhyan basin preserve Earth's earliest life forms.";
    foot.textContent = "Stromatolites prove that Kingdom Monera organisms thrived in India's shallow ancient seas over a billion years ago!";
  }
};
window.addEventListener('DOMContentLoaded', () => setC12S6('cell'));
</script>""",

    7: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Kingdom Protista:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S7('amoeba')" id="c12s7_btn_amoeba" class="px-2 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition">Amoeba</button>
        <button onclick="setC12S7('paramecium')" id="c12s7_btn_para" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Paramecium</button>
        <button onclick="setC12S7('euglena')" id="c12s7_btn_eug" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Euglena</button>
        <button onclick="setC12S7('infusion')" id="c12s7_btn_inf" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Hay Infusion Lab</button>
      </div>
    </div>
    <span class="text-xs text-cyan-300 font-mono" id="c12s7_locomotion">Pseudopodia &bull; Phagocytosis</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c12s7_stage" class="w-full max-w-lg flex flex-col items-center justify-center">
      <!-- Dynamic SVG Protist -->
    </div>

    <div class="w-full max-w-lg mt-2 bg-slate-900/80 border border-slate-700/60 rounded-xl p-2.5">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-bold text-cyan-300" id="c12s7_name">Amoeba proteus</span>
        <span class="text-[10px] text-emerald-400 font-mono" id="c12s7_trait">Unicellular Eukaryote</span>
      </div>
      <p class="text-xs text-slate-300 leading-relaxed" id="c12s7_details">
        Amoeba moves and captures food via false feet (pseudopodia). Cytoplasmic streaming flows forward, enveloping bacterial prey into a food vacuole for intracellular lysosomal enzymatic digestion.
      </p>
    </div>
  </div>

  <div class="bg-cyan-950/30 border border-cyan-800/40 rounded-xl px-3 py-1.5 text-xs text-cyan-200" id="c12s7_foot">
    <strong>Microscopic Distinction:</strong> Unlike bacteria, all protists possess a true membrane-bound nucleus, mitochondria, and specialized vacuoles for osmoregulation.
  </div>
</div>
<script>
window.setC12S7 = function(org){
  const btns = ['amoeba', 'para', 'eug', 'inf'];
  btns.forEach(b => {
    const el = document.getElementById('c12s7_btn_' + b);
    if(el) el.className = (b === org.substring(0,4) || (org==='paramecium' && b==='para') || (org==='infusion' && b==='inf')) ?
      'px-2 py-1 text-xs font-bold rounded-md bg-cyan-600 text-white transition' :
      'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  });

  const loc = document.getElementById('c12s7_locomotion');
  const stage = document.getElementById('c12s7_stage');
  const name = document.getElementById('c12s7_name');
  const trait = document.getElementById('c12s7_trait');
  const details = document.getElementById('c12s7_details');
  const foot = document.getElementById('c12s7_foot');

  if(org === 'amoeba'){
    loc.textContent = "Pseudopodia • Phagocytosis";
    stage.innerHTML = `
      <svg viewBox="0 0 360 130" class="w-full h-32">
        <!-- Irregular amoeboid body -->
        <path d="M80,60 Q100,20 160,35 Q220,15 260,50 Q300,75 270,105 Q220,125 150,110 Q90,120 70,85 Z" fill="#0891b2" fill-opacity="0.3" stroke="#06b6d4" stroke-width="2"/>
        <!-- Nucleus with membrane -->
        <circle cx="165" cy="70" r="14" fill="#0e7490" stroke="#22d3ee" stroke-width="2"/>
        <circle cx="165" cy="70" r="6" fill="#e0f2fe"/>
        <text x="185" y="74" fill="#a5f3fc" font-size="9" font-weight="bold">True Nucleus</text>
        <!-- Contractile vacuole -->
        <circle cx="230" cy="55" r="10" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,2"/>
        <text x="245" y="58" fill="#7dd3fc" font-size="8">Contractile Vacuole</text>
        <!-- Food vacuole capturing prey -->
        <circle cx="110" cy="80" r="8" fill="#1e293b" stroke="#eab308" stroke-width="1.5"/>
        <circle cx="110" cy="80" r="3" fill="#eab308"/>
        <text x="95" y="105" fill="#fde047" font-size="8">Food Vacuole</text>
        <!-- Pseudopodia labels -->
        <path d="M260,50 L290,40" stroke="#22d3ee" stroke-width="1.5"/>
        <text x="295" y="42" fill="#22d3ee" font-size="8">Pseudopodium</text>
      </svg>
    `;
    name.textContent = "Amoeba proteus (Amoeboid Locomotion)";
    trait.textContent = "Contractile Vacuole & Pseudopodia";
    details.textContent = "Amoeba has no fixed shape. Its gelatinous ectoplasm and fluid endoplasm enable cytoplasmic streaming, projecting blunt pseudopodia to engulf organic food and bacteria via phagocytosis.";
    foot.innerHTML = "<strong>Osmoregulation:</strong> The contractile vacuole pumps out excess water, preventing the freshwater cell from bursting!";
  } else if(org === 'paramecium'){
    loc.textContent = "Cilia Waves • Slipper Animalcule";
    stage.innerHTML = `
      <svg viewBox="0 0 360 130" class="w-full h-32">
        <!-- Slipper body -->
        <path d="M60,65 Q110,25 240,30 Q300,50 300,75 Q280,105 200,105 Q100,105 60,65 Z" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
        <!-- Cilia boundary -->
        <path d="M55,65 Q110,20 240,25 Q305,48 305,75 Q285,110 200,110 Q95,110 55,65 Z" fill="none" stroke="#7dd3fc" stroke-width="1" stroke-dasharray="2,3"/>
        <!-- Oral groove / Cytostome -->
        <path d="M180,30 Q160,60 170,80" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
        <text x="180" y="70" fill="#fde047" font-size="8">Oral Groove</text>
        <!-- Dual Nuclei: Macro and Micro -->
        <ellipse cx="130" cy="65" rx="14" ry="9" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
        <circle cx="150" cy="62" r="4" fill="#fbbf24"/>
        <text x="110" y="68" fill="#e0f2fe" font-size="8">Macronucleus</text>
        <text x="145" y="55" fill="#fde047" font-size="7">Micronucleus</text>
        <!-- Radiating Contractile Vacuoles -->
        <circle cx="85" cy="65" r="6" fill="#38bdf8"/>
        <circle cx="265" cy="70" r="6" fill="#38bdf8"/>
      </svg>
    `;
    name.textContent = "Paramecium caudatum (Ciliate Protist)";
    trait.textContent = "Dual Nuclei & Pellicle Guard";
    details.textContent = "Equipped with thousands of coordinated cilia beating rhythmically to propel the cell and sweep food down the oral groove. Features nuclear dimorphism: a large vegetative macronucleus and a tiny reproductive micronucleus.";
    foot.innerHTML = "<strong>High-Speed Locomotion:</strong> Paramecium rotates along its longitudinal axis, reversing direction upon encountering physical obstacles.";
  } else if(org === 'euglena'){
    loc.textContent = "Flagellum • Mixotrophic Nutrition";
    stage.innerHTML = `
      <svg viewBox="0 0 360 130" class="w-full h-32">
        <!-- Spindle shaped body -->
        <path d="M100,65 Q180,35 280,65 Q180,95 100,65 Z" fill="#15803d" fill-opacity="0.4" stroke="#22c55e" stroke-width="2"/>
        <!-- Anterior Flagellum whip -->
        <path d="M100,65 Q70,40 50,75 T20,50" fill="none" stroke="#4ade80" stroke-width="2.5" stroke-linecap="round"/>
        <!-- Red Eyespot (Stigma) -->
        <circle cx="115" cy="62" r="4" fill="#ef4444"/>
        <text x="122" y="60" fill="#fca5a5" font-size="8">Red Eyespot</text>
        <!-- Chloroplasts -->
        <ellipse cx="170" cy="55" rx="10" ry="5" fill="#16a34a"/>
        <ellipse cx="210" cy="60" rx="10" ry="5" fill="#16a34a"/>
        <ellipse cx="190" cy="75" rx="10" ry="5" fill="#16a34a"/>
        <ellipse cx="235" cy="70" rx="10" ry="5" fill="#16a34a"/>
        <text x="180" y="60" fill="#bbf7d0" font-size="8">Chloroplasts</text>
        <!-- Central Nucleus -->
        <circle cx="215" cy="65" r="10" fill="#166534" stroke="#86efac" stroke-width="1.5"/>
      </svg>
    `;
    name.textContent = "Euglena viridis (Mixotrophic Protist)";
    trait.textContent = "Phototaxis & Chloroplasts";
    details.textContent = "Euglena possesses chloroplasts with chlorophyll for photosynthesis in sunlight. In darkness, it switches to heterotrophic saprozoic feeding—a unique nutritional plasticity called mixotrophy. The red eyespot directs movement toward light.";
    foot.innerHTML = "<strong>Bridging Kingdoms:</strong> Possesses plant-like chloroplasts but lacks a cellulose cell wall, enclosed instead by a proteinaceous pellicle!";
  } else {
    loc.textContent = "Activity 12.5 • Biosafety Sterilisation";
    stage.innerHTML = `
      <svg viewBox="0 0 360 130" class="w-full h-32">
        <!-- Beaker 1: Infusion preparation -->
        <rect x="50" y="35" width="60" height="70" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
        <rect x="52" y="55" width="56" height="48" fill="#713f12" opacity="0.6"/>
        <text x="55" y="75" fill="#fef08a" font-size="8">Hay Straw</text>
        <text x="53" y="87" fill="#93c5fd" font-size="7">+ Pond Water</text>
        <text x="45" y="118" fill="#94a3b8" font-size="8">1. 3-Day Culture</text>
        <!-- Microscope lens -->
        <circle cx="180" cy="65" r="32" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="170" cy="60" r="3" fill="#38bdf8"/>
        <circle cx="190" cy="72" r="4" fill="#22c55e"/>
        <circle cx="182" cy="55" r="2" fill="#eab308"/>
        <text x="145" y="118" fill="#38bdf8" font-size="8">2. Slide Microscopy</text>
        <!-- Autoclave / Heat Sterilisation symbol -->
        <rect x="250" y="35" width="60" height="70" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
        <path d="M265,90 Q280,75 280,60 M275,90 Q290,75 290,60" stroke="#f43f5e" stroke-width="2" fill="none"/>
        <text x="254" y="50" fill="#fca5a5" font-size="8">121°C Steam</text>
        <text x="240" y="118" fill="#818cf8" font-size="8">3. Autoclave Safe</text>
      </svg>
    `;
    name.textContent = "Activity 12.5: Hay Infusion Protocol";
    trait.textContent = "Microscopic Succession & Safety";
    details.textContent = "Boiling water added to dried hay extracts soluble nutrients. Inoculated with pond water, bacteria proliferate first, followed by ciliates and amoeboid protists feeding on bacteria in ecological succession.";
    foot.innerHTML = "<strong>Mandatory Biosafety:</strong> All culture vessels must be autoclaved at 121°C or boiled thoroughly before disposal to prevent environmental contamination!";
  }
};
window.addEventListener('DOMContentLoaded', () => setC12S7('amoeba'));
</script>""",

    8: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Kingdom Fungi:</span>
      <div class="inline-flex rounded-lg p-0.5 bg-slate-950 border border-slate-800">
        <button onclick="setC12S8('hyphae')" id="c12s8_btn_hyp" class="px-2 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition">Mycelium Network</button>
        <button onclick="setC12S8('chitin')" id="c12s8_btn_chi" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Chitin Wall</button>
        <button onclick="setC12S8('farming')" id="c12s8_btn_far" class="px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition">Mushroom Farming</button>
      </div>
    </div>
    <span class="text-xs text-rose-300 font-mono" id="c12s8_status">Absorptive Saprophyte &bull; Exoenzymes</span>
  </div>

  <div class="relative flex-1 min-h-[220px] bg-slate-950/70 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col items-center justify-center">
    <div id="c12s8_visual" class="w-full max-w-lg flex flex-col items-center justify-center">
      <!-- Dynamic SVG Canvas -->
    </div>

    <div class="w-full max-w-lg mt-2 bg-slate-900/80 border border-slate-700/60 rounded-xl p-2.5">
      <div class="flex items-center justify-between mb-1">
        <span class="text-xs font-bold text-rose-300" id="c12s8_title">Absorptive Heterotrophy &amp; Forest Recycling</span>
        <span class="text-[10px] text-slate-400 font-mono" id="c12s8_badge">Mycelial Wood-Wide Web</span>
      </div>
      <p class="text-xs text-slate-300 leading-relaxed" id="c12s8_body">
        Fungi do not ingest food. Instead, hyphae secrete digestive hydrolytic exoenzymes directly into surrounding substrate (wood, leaves), breaking complex polymers (lignin, cellulose) into simple soluble molecules absorbed across chitinous walls.
      </p>
    </div>
  </div>

  <div class="bg-rose-950/30 border border-rose-800/40 rounded-xl px-3 py-1.5 text-xs text-rose-200" id="c12s8_foot">
    <strong>Forest Health:</strong> Without fungal decomposers, forests would choke under miles of dead plant litter within decades!
  </div>
</div>
<script>
window.setC12S8 = function(view){
  const btns = ['hyp', 'chi', 'far'];
  btns.forEach(b => {
    const el = document.getElementById('c12s8_btn_' + b);
    if(el) el.className = (b === view) ?
      'px-2 py-1 text-xs font-bold rounded-md bg-rose-600 text-white transition' :
      'px-2 py-1 text-xs font-bold rounded-md text-slate-400 hover:text-white transition';
  });

  const status = document.getElementById('c12s8_status');
  const vis = document.getElementById('c12s8_visual');
  const title = document.getElementById('c12s8_title');
  const badge = document.getElementById('c12s8_badge');
  const body = document.getElementById('c12s8_body');
  const foot = document.getElementById('c12s8_foot');

  if(view === 'hyp'){
    status.textContent = "Absorptive Saprophyte • Exoenzymes";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Decaying log / substrate -->
        <rect x="30" y="60" width="320" height="60" rx="8" fill="#451a03" stroke="#78350f" stroke-width="2"/>
        <text x="40" y="105" fill="#d97706" font-size="9" font-weight="bold">Dead Log Substrate (Lignin &amp; Cellulose)</text>
        <!-- Branching Hyphal Mycelium -->
        <path d="M190,60 Q170,80 140,85 T90,95 M140,85 Q120,70 95,75 M190,60 Q210,80 250,85 T310,90 M250,85 Q270,72 295,70" stroke="#fde047" stroke-width="2.5" fill="none"/>
        <!-- Fruiting Body (Mushroom) -->
        <rect x="184" y="15" width="12" height="48" fill="#f8fafc" rx="4"/>
        <path d="M150,22 Q190,-8 230,22 Z" fill="#e11d48"/>
        <circle cx="170" cy="12" r="2.5" fill="#ffffff"/>
        <circle cx="210" cy="14" r="2" fill="#ffffff"/>
        <circle cx="190" cy="7" r="3" fill="#ffffff"/>
        <text x="235" y="18" fill="#fca5a5" font-size="8">Fruiting Body (Agaricus)</text>
        <!-- Secretion beads (Enzymes) -->
        <circle cx="115" cy="85" r="2" fill="#38bdf8"/>
        <circle cx="270" cy="85" r="2" fill="#38bdf8"/>
        <text x="260" y="115" fill="#38bdf8" font-size="8">Exoenzyme Secretion</text>
      </svg>
    `;
    title.textContent = "Mycelium Network & Extracellular Digestion";
    badge.textContent = "Hyphae &amp; Mycelium";
    body.textContent = "A mushroom is merely the reproductive spore-bearing organ. The vegetative fungal body consists of a vast network of microscopic threads called hyphae, collectively termed mycelium, pervading soil and rotting wood.";
    foot.innerHTML = "<strong>Nutrient Highway:</strong> Mycelia form mycorrhizal partnerships with 90% of plant roots, exchanging phosphorus and minerals for plant glucose.";
  } else if(view === 'chi'){
    status.textContent = "Structural Biopolymer • Chitin vs Cellulose";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Chitin molecular strand illustration -->
        <rect x="40" y="30" width="140" height="70" rx="8" fill="#881337" stroke="#f43f5e" stroke-width="2"/>
        <text x="50" y="50" fill="#fecdd3" font-size="10" font-weight="bold">Fungal Cell Wall</text>
        <text x="50" y="68" fill="#ffffff" font-size="11" font-weight="extrabold">CHITIN</text>
        <text x="50" y="85" fill="#fda4af" font-size="8">N-acetylglucosamine</text>

        <!-- Plant Cellulose comparison -->
        <rect x="200" y="30" width="140" height="70" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
        <text x="210" y="50" fill="#a7f3d0" font-size="10" font-weight="bold">Plant Cell Wall</text>
        <text x="210" y="68" fill="#ffffff" font-size="11" font-weight="extrabold">CELLULOSE</text>
        <text x="210" y="85" fill="#6ee7b7" font-size="8">Poly-β-1,4-D-glucose</text>
      </svg>
    `;
    title.textContent = "Chitinous Cell Wall Chemistry";
    badge.textContent = "Nitrogenous Polysaccharide";
    body.textContent = "While plant cell walls are built of cellulose, fungal walls consist of chitin—the same tough nitrogenous polymer found in the exoskeletons of insects and crabs. This biochemical difference proved fungi are more closely related to animals than plants!";
    foot.innerHTML = "<strong>Taxonomic Landmark:</strong> Robert Whittaker established Kingdom Fungi largely due to its unique chitinous wall and absorptive heterotrophic nutrition.";
  } else {
    status.textContent = "30-45 Day Cycle • Protein-Rich Food";
    vis.innerHTML = `
      <svg viewBox="0 0 380 130" class="w-full h-32">
        <!-- Step 1: Substrate Straw -->
        <rect x="20" y="35" width="70" height="65" rx="6" fill="#1c1917" stroke="#78350f" stroke-width="1.5"/>
        <text x="26" y="55" fill="#fde047" font-size="8" font-weight="bold">1. Pasteurise</text>
        <text x="25" y="70" fill="#a8a29e" font-size="7">Paddy Straw</text>
        <text x="25" y="82" fill="#a8a29e" font-size="7">Boiling Water</text>

        <!-- Step 2: Inoculate Spawn -->
        <rect x="110" y="35" width="70" height="65" rx="6" fill="#1c1917" stroke="#e11d48" stroke-width="1.5"/>
        <text x="116" y="55" fill="#fda4af" font-size="8" font-weight="bold">2. Spawning</text>
        <text x="115" y="70" fill="#a8a29e" font-size="7">Grain Spawn</text>
        <text x="115" y="82" fill="#a8a29e" font-size="7">Dark Run</text>

        <!-- Step 3: Pinheads -->
        <rect x="200" y="35" width="70" height="65" rx="6" fill="#1c1917" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="206" y="55" fill="#93c5fd" font-size="8" font-weight="bold">3. Pinheading</text>
        <text x="205" y="70" fill="#a8a29e" font-size="7">Moisture 85%</text>
        <text x="205" y="82" fill="#a8a29e" font-size="7">Ventilation</text>

        <!-- Step 4: Harvest -->
        <rect x="290" y="35" width="70" height="65" rx="6" fill="#1c1917" stroke="#22c55e" stroke-width="1.5"/>
        <text x="296" y="55" fill="#86efac" font-size="8" font-weight="bold">4. Harvest</text>
        <text x="295" y="70" fill="#a8a29e" font-size="7">Button / Oyster</text>
        <text x="295" y="82" fill="#a8a29e" font-size="7">30-45 Days</text>
      </svg>
    `;
    title.textContent = "Mushroom Farming Cycle (Oyster &amp; Button Cultivation)";
    badge.textContent = "Agricultural Biotechnology";
    body.textContent = "Cultivating mushrooms converts waste agricultural residues (paddy straw, wheat husks) into nutritious protein in 30 to 45 days. The substrate is pasteurized, spawned with mycelial culture, cased, and kept humid until fruiting bodies appear.";
    foot.innerHTML = "<strong>Nutritional Value:</strong> Mushrooms provide low-calorie dietary fiber, essential vitamins (B &amp; D), and complete amino acid profiles!";
  }
};
window.addEventListener('DOMContentLoaded', () => setC12S8('hyp'));
</script>"""
}
