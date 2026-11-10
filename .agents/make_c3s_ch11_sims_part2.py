#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 11: Making Things
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Moulding Mud Bricks
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧱</span>
            <h3 class="text-sm sm:text-base font-bold text-orange-300">Brick Moulding &amp; Kiln Baking Factory</h3>
        </div>
        <span class="text-[11px] bg-orange-950/80 text-orange-300 px-2.5 py-1 rounded-full border border-orange-800">Masonry Basics</span>
    </div>

    <p class="text-xs text-slate-300">Click each brick-making stage to turn soft wet mud into rock-hard uniform red bricks ready to raise strong walls!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setBrickStage('mould')" id="btn-brk-mould" class="p-2.5 rounded-xl bg-orange-600 text-white font-bold text-xs border border-orange-500">1. Wooden Mould</button>
        <button onclick="setBrickStage('sun')" id="btn-brk-sun" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. Dry In Sun</button>
        <button onclick="setBrickStage('kiln')" id="btn-brk-kiln" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. Bake In Kiln</button>
        <button onclick="setBrickStage('ready')" id="btn-brk-ready" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">4. Red Brick Ready</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 175" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Stage 1: Wooden Mould -->
            <g id="brk-mould-svg">
                <rect x="85" y="65" width="150" height="55" fill="#92400e" stroke="#f59e0b" stroke-width="4" />
                <rect x="92" y="72" width="136" height="41" fill="#78350f" />
                <rect x="75" y="120" width="170" height="8" fill="#475569" />
            </g>
            <!-- Stage 2: Sun Dry -->
            <g id="brk-sun-svg" class="hidden">
                <circle cx="260" cy="38" r="18" fill="#fde047" />
                <rect x="70" y="95" width="80" height="32" rx="2" fill="#a8a29e" stroke="#d6d3d1" />
                <rect x="165" y="95" width="80" height="32" rx="2" fill="#a8a29e" stroke="#d6d3d1" />
            </g>
            <!-- Stage 3: Brick Kiln -->
            <g id="brk-kiln-svg" class="hidden">
                <polygon points="105,135 135,45 185,45 215,135" fill="#7f1d1d" stroke="#ef4444" stroke-width="2" />
                <path d="M145,45 Q150,25 145,15 M175,45 Q180,25 175,15" stroke="#94a3b8" stroke-width="3" fill="none" />
                <path d="M135,125 Q160,92 185,125 Z" fill="#f97316" />
            </g>
            <!-- Stage 4: Hard Red Brick -->
            <g id="brk-ready-svg" class="hidden">
                <polygon points="95,90 195,90 215,72 115,72" fill="#dc2626" />
                <rect x="95" y="90" width="100" height="40" fill="#b91c1c" />
                <polygon points="195,90 215,72 215,112 195,130" fill="#991b1b" />
                <rect x="122" y="77" width="60" height="8" fill="#991b1b" opacity="0.7" />
            </g>
            <text x="160" y="160" fill="#fdba74" font-size="10" font-weight="bold" text-anchor="middle" id="brk-svg-lbl">Wooden frames press wet mud neatly into identical brick rectangles!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-orange-300 text-sm" id="brk-title">Step 1: Pressing Wet Mud Into Wooden Moulds</h4>
            <p class="text-slate-300 leading-relaxed" id="brk-desc">Workers pack wet clayey soil firmly into hollow rectangular wooden boxes called moulds and scrape the top flat so thousands of bricks share the exact same length, width, and height!</p>
        </div>
    </div>
</div>

<script>
function setBrickStage(st) {
    const map = {
        mould: { lbl: 'Wooden frames press wet mud neatly into identical brick rectangles!', t: 'Step 1: Pressing Wet Mud Into Wooden Moulds', d: 'Workers pack wet clayey soil firmly into hollow rectangular wooden boxes called moulds and scrape the top flat so thousands of bricks share the exact same length, width, and height!' },
        sun: { lbl: 'Warm open sunshine evaporates moisture so green bricks hold shape!', t: 'Step 2: Sun-Drying Raw Mud Bricks', d: 'Unmoulded wet blocks sit neatly in long open rows under warm sunshine for days until stiff enough to stack inside tall brick kilns without squashing.' },
        kiln: { lbl: 'Intense glowing kiln heat bakes thousands of stacked mud blocks hard!', t: 'Step 3: Firing Inside Huge Brick Kilns', d: 'Bricks are stacked carefully with air vents inside massive glowing kilns. High steady firing bakes soft mud permanently into dense stony ceramic!' },
        ready: { lbl: 'Crisp ringing red fired bricks endure rainstorms and multi-floor weight!', t: 'Step 4: Durable Ringing Red Bricks', d: 'Tap two well-baked red bricks together and hear a clear metallic clink! Waterproof and stone-hard, they raise strong houses, schools, and bridges cleanly.' }
    };
    const d = map[st];
    if (!d) return;
    ['mould', 'sun', 'kiln', 'ready'].forEach(k => {
        const b = document.getElementById('btn-brk-' + k);
        if (b) {
            b.className = (k === st)
                ? 'p-2.5 rounded-xl bg-orange-600 text-white font-bold text-xs border border-orange-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('brk-' + k + '-svg');
        if (g) {
            if (k === st) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('brk-svg-lbl').textContent = d.lbl;
    document.getElementById('brk-title').textContent = d.t;
    document.getElementById('brk-desc').textContent = d.d;
}
</script>
"""

# Simulator 10: Building Public Spaces
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏫</span>
            <h3 class="text-sm sm:text-base font-bold text-sky-300">Brick &amp; Mortar Civic Architecture Explorer</h3>
        </div>
        <span class="text-[11px] bg-sky-950/80 text-sky-300 px-2.5 py-1 rounded-full border border-sky-800">Community Structures</span>
    </div>

    <p class="text-xs text-slate-300">Select essential community buildings made with strong baked bricks, cement mortar, steel beams, and glass windows!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectBuilding('home')" id="btn-bld-home" class="p-2.5 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500">🏠 Family Home</button>
        <button onclick="inspectBuilding('school')" id="btn-bld-school" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🏫 School Hall</button>
        <button onclick="inspectBuilding('hospital')" id="btn-bld-hospital" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🏥 Clinic</button>
        <button onclick="inspectBuilding('bridge')" id="btn-bld-bridge" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🌉 Arch Bridge</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 175" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Home -->
            <g id="bld-home-svg">
                <polygon points="85,78 160,32 235,78" fill="#b91c1c" />
                <rect x="95" y="78" width="130" height="65" fill="#d97706" />
                <rect x="145" y="102" width="30" height="41" fill="#78350f" />
                <rect x="108" y="92" width="24" height="22" fill="#38bdf8" />
                <rect x="188" y="92" width="24" height="22" fill="#38bdf8" />
            </g>
            <!-- School -->
            <g id="bld-school-svg" class="hidden">
                <rect x="65" y="58" width="190" height="85" fill="#ea580c" />
                <rect x="135" y="42" width="50" height="22" fill="#dc2626" />
                <rect x="85" y="78" width="26" height="20" fill="#7dd3fc" />
                <rect x="147" y="98" width="26" height="45" fill="#78350f" />
                <rect x="209" y="78" width="26" height="20" fill="#7dd3fc" />
                <text x="160" y="57" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">SCHOOL</text>
            </g>
            <!-- Hospital -->
            <g id="bld-hospital-svg" class="hidden">
                <rect x="80" y="52" width="160" height="92" fill="#e2e8f0" />
                <rect x="145" y="104" width="30" height="40" fill="#0284c7" />
                <rect x="155" y="62" width="10" height="30" fill="#ef4444" />
                <rect x="145" y="72" width="30" height="10" fill="#ef4444" />
            </g>
            <!-- Bridge -->
            <g id="bld-bridge-svg" class="hidden">
                <rect x="30" y="125" width="260" height="20" fill="#0284c7" opacity="0.6" />
                <path d="M40,125 L40,78 L280,78 L280,125 L235,125 Q200,88 165,125 L155,125 Q120,88 85,125 Z" fill="#b91c1c" />
            </g>
            <text x="160" y="164" fill="#7dd3fc" font-size="10" font-weight="bold" text-anchor="middle" id="bld-svg-lbl">Baked bricks &amp; cement mortar glue solid multi-room family shelters!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-sky-300 text-sm" id="bld-title">Safe Family Brick Home</h4>
            <p class="text-slate-300 leading-relaxed" id="bld-desc">Baked red bricks bonded tightly with wet cement-sand mortar form durable waterproof walls protecting families safely from scorching sun, monsoon storms, and strong winds.</p>
        </div>
    </div>
</div>

<script>
function inspectBuilding(type) {
    const map = {
        home: { lbl: 'Baked bricks & cement mortar glue solid multi-room family shelters!', t: 'Safe Family Brick Home', d: 'Baked red bricks bonded tightly with wet cement-sand mortar form durable waterproof walls protecting families safely from scorching sun, monsoon storms, and strong winds.' },
        school: { lbl: 'Wide sunlit classrooms let dozens of children read, play, and learn safely!', t: 'Sturdy Village & Town Schools', d: 'Tall brick columns, sturdy concrete roofs, and bright clear glass windows create lively sunlit classrooms built to serve generations of curious students.' },
        hospital: { lbl: 'Clean paved clinics support doctors caring peacefully for healing patients!', t: 'Community Health Clinics & Hospitals', d: 'Well-built brick wards, smooth wiped tiled walls, and clean water pipes keep doctors, nurses, and healing patients safe around the clock.' },
        bridge: { lbl: 'Curved brick & stone arches carry traffic smoothly over flowing streams!', t: 'Strong Masonry & Concrete Bridges', d: 'Solid interlocking brick piers and rounded stone arches carry villagers, school buses, and bicycles safely across flooding monsoon streams!' }
    };
    const d = map[type];
    if (!d) return;
    ['home', 'school', 'hospital', 'bridge'].forEach(k => {
        const b = document.getElementById('btn-bld-' + k);
        if (b) {
            b.className = (k === type)
                ? 'p-2.5 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('bld-' + k + '-svg');
        if (g) {
            if (k === type) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('bld-svg-lbl').textContent = d.lbl;
    document.getElementById('bld-title').textContent = d.t;
    document.getElementById('bld-desc').textContent = d.d;
}
</script>
"""

# Simulator 11: Cool Mud Houses (Activity 5)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏡</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Activity 5: Cool Mud-Straw-Dung Plaster House Lab</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Eco Insulation</span>
    </div>

    <p class="text-xs text-slate-300">Compare scorching 44°C midday afternoon sunshine hitting a Metal Sheet Shed versus a Traditional Mud-Straw-Cow-Dung House!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="setCoolHouse('tin')" id="btn-ch-tin" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Hot Metal Tin Shed</button>
        <button onclick="setCoolHouse('mud')" id="btn-ch-mud" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Cool Mud + Straw House</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 175" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <circle cx="275" cy="34" r="18" fill="#fbbf24" />
            <text x="230" y="38" fill="#fde047" font-size="11" font-weight="bold">OUTSIDE 44°C</text>
            <!-- Tin Shed -->
            <g id="ch-tin-svg">
                <polygon points="75,70 160,48 245,70" fill="#94a3b8" />
                <rect x="85" y="70" width="150" height="72" fill="#475569" />
                <text x="160" y="108" fill="#f87171" font-size="18" font-weight="bold" text-anchor="middle">INSIDE: 46°C 🔥</text>
                <text x="160" y="128" fill="#fca5a5" font-size="10" text-anchor="middle">Thin walls transfer intense heat inside!</text>
            </g>
            <!-- Cool Mud House -->
            <g id="ch-mud-svg" class="hidden">
                <polygon points="70,74 160,34 250,74" fill="#d97706" />
                <rect x="82" y="74" width="156" height="68" fill="#92400e" stroke="#b45309" stroke-width="8" />
                <text x="160" y="108" fill="#4ade80" font-size="18" font-weight="bold" text-anchor="middle">INSIDE: 29°C ❄️🌿</text>
                <text x="160" y="128" fill="#bbf7d0" font-size="10" text-anchor="middle">Thick mud + straw traps heat outside!</text>
            </g>
            <text x="160" y="164" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle" id="ch-svg-lbl">Thin metal conducts afternoon heat cleanly straight into the room!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-amber-300 text-sm" id="ch-title">Thin Metal Sheet Roof Shed (46°C Inside)</h4>
            <p class="text-slate-300 leading-relaxed" id="ch-desc">Thin metal sheets soak up burning afternoon sunlight quickly and bake indoor air hotter than outside shade, needing expensive fans or coolers continuously.</p>
        </div>
    </div>
</div>

<script>
function setCoolHouse(kind) {
    const map = {
        tin: { lbl: 'Thin metal conducts afternoon heat cleanly straight into the room!', t: 'Thin Metal Sheet Roof Shed (46°C Inside)', d: 'Thin metal sheets soak up burning afternoon sunlight quickly and bake indoor air hotter than outside shade, needing expensive fans or coolers continuously.' },
        mud: { lbl: 'Thick mud, chopped straw & cow-dung plaster keep rooms remarkably cool!', t: 'Cool Mud, Straw & Cow-Dung Plaster House (29°C Inside)', d: 'Thick mud walls mixed with golden straw act like natural cooling jackets blocking fierce sun heat—while smooth cow-dung wall plaster stops hairline cracks and repels crawling insects cleanly!' }
    };
    const d = map[kind];
    if (!d) return;
    ['tin', 'mud'].forEach(k => {
        const b = document.getElementById('btn-ch-' + k);
        if (b) {
            b.className = (k === kind)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('ch-' + k + '-svg');
        if (g) {
            if (k === kind) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('ch-svg-lbl').textContent = d.lbl;
    document.getElementById('ch-title').textContent = d.t;
    document.getElementById('ch-desc').textContent = d.d;
}
</script>
"""

# Simulator 12: Diverse House Shelters
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⛰️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Climate &amp; Regional Shelter Adaptation Map</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Local Design</span>
    </div>

    <p class="text-xs text-slate-300">Explore how wise local builders adapt roof angles, stilts, and wall materials to fit rainy wetlands, snowy peaks, and sunny deserts!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="inspectRegion('assam')" id="btn-reg-assam" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">🌧️ Assam Stilts</button>
        <button onclick="inspectRegion('snow')" id="btn-reg-snow" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">❄️ Snow Mountains</button>
        <button onclick="inspectRegion('desert')" id="btn-reg-desert" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🏜️ Desert Plains</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 175" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Assam Stilt Bamboo House -->
            <g id="reg-assam-svg">
                <rect x="0" y="132" width="320" height="25" fill="#0284c7" opacity="0.5" />
                <line x1="100" y1="105" x2="100" y2="150" stroke="#78350f" stroke-width="6" />
                <line x1="160" y1="105" x2="160" y2="150" stroke="#78350f" stroke-width="6" />
                <line x1="220" y1="105" x2="220" y2="150" stroke="#78350f" stroke-width="6" />
                <rect x="90" y="65" width="140" height="42" fill="#d97706" />
                <polygon points="80,65 160,32 240,65" fill="#92400e" />
            </g>
            <!-- Mountain Snow Roof -->
            <g id="reg-snow-svg" class="hidden">
                <polygon points="75,90 160,25 245,90" fill="#cbd5e1" stroke="#f8fafc" stroke-width="4" />
                <rect x="95" y="90" width="130" height="55" fill="#64748b" />
                <rect x="148" y="112" width="24" height="33" fill="#78350f" />
                <circle cx="55" cy="40" r="3" fill="#e2e8f0" /><circle cx="265" cy="55" r="3" fill="#e2e8f0" /><circle cx="280" cy="30" r="3" fill="#e2e8f0" />
            </g>
            <!-- Desert Mud Flat Roof -->
            <g id="reg-desert-svg" class="hidden">
                <circle cx="265" cy="32" r="16" fill="#fde047" />
                <rect x="85" y="70" width="150" height="75" fill="#d97706" />
                <rect x="80" y="64" width="160" height="8" fill="#b45309" />
                <rect x="148" y="105" width="24" height="40" fill="#78350f" />
            </g>
            <text x="160" y="168" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle" id="reg-svg-lbl">Strong bamboo stilts raise Assam floors safely above heavy monsoon floodwater!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-emerald-300 text-sm" id="reg-title">Heavy-Rain Assam Bamboo Stilt House</h4>
            <p class="text-slate-300 leading-relaxed" id="reg-desc">Where monsoon rivers swell frequently, builders lift sturdy woven bamboo homes high on vertical wooden stilts with steep slanted roofs so floodwater flows safely underneath without soaking floors!</p>
        </div>
    </div>
</div>

<script>
function inspectRegion(reg) {
    const map = {
        assam: { lbl: 'Strong bamboo stilts raise Assam floors safely above heavy monsoon floodwater!', t: 'Heavy-Rain Assam Bamboo Stilt House', d: 'Where monsoon rivers swell frequently, builders lift sturdy woven bamboo homes high on vertical wooden stilts with steep slanted roofs so floodwater flows safely underneath without soaking floors!' },
        snow: { lbl: 'Steep wooden triangular roofs let heavy winter snow slide straight off cleanly!', t: 'Snowy Mountain Sloped Timber & Stone House', d: 'Steep triangular pitched roofs stop heavy piles of mountain snow from crushing ceilings, while thick stone and wood walls keep cozy fireplace warmth indoors.' },
        desert: { lbl: 'Thick mud walls & flat roofs block blistering dry desert sunshine!', t: 'Hot Desert Thick Mud & Flat Roof Home', d: 'Where rainfall is rare and afternoon sun blazes fiercely, thick earthen walls keep interiors refreshingly shaded and cool terraces offer breezy evening resting space.' }
    };
    const d = map[reg];
    if (!d) return;
    ['assam', 'snow', 'desert'].forEach(k => {
        const b = document.getElementById('btn-reg-' + k);
        if (b) {
            b.className = (k === reg)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('reg-' + k + '-svg');
        if (g) {
            if (k === reg) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('reg-svg-lbl').textContent = d.lbl;
    document.getElementById('reg-title').textContent = d.t;
    document.getElementById('reg-desc').textContent = d.d;
}
</script>
"""

# Simulator 13: Testing Wall Strength (Activity 6)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏗️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Activity 6: Brick Wall Stacking &amp; Push Strength Test</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Structural Engineering</span>
    </div>

    <p class="text-xs text-slate-300">Compare pushing against a Straight Stacked Wall versus a Staggered Interlocking Wall to discover why masons never align vertical seams!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="testWallBond('straight')" id="btn-wb-straight" class="p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">Weak: Straight Columns</button>
        <button onclick="testWallBond('staggered')" id="btn-wb-staggered" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Strong: Staggered Bond</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 175" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Straight Columns -->
            <g id="wb-straight-svg">
                <rect x="75" y="105" width="52" height="25" fill="#dc2626" stroke="#fde047" />
                <rect x="75" y="78" width="52" height="25" fill="#dc2626" stroke="#fde047" />
                <rect x="75" y="51" width="52" height="25" fill="#dc2626" stroke="#fde047" />
                <g transform="rotate(8 160 130)">
                    <rect x="132" y="105" width="52" height="25" fill="#b91c1c" stroke="#fde047" />
                    <rect x="132" y="78" width="52" height="25" fill="#b91c1c" stroke="#fde047" />
                    <rect x="132" y="51" width="52" height="25" fill="#b91c1c" stroke="#fde047" />
                </g>
                <rect x="189" y="105" width="52" height="25" fill="#dc2626" stroke="#fde047" />
                <rect x="189" y="78" width="52" height="25" fill="#dc2626" stroke="#fde047" />
                <rect x="189" y="51" width="52" height="25" fill="#dc2626" stroke="#fde047" />
                <line x1="129" y1="45" x2="129" y2="135" stroke="#ef4444" stroke-width="3" stroke-dasharray="4,3" />
                <text x="160" y="34" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">CRACK SPLITS STRAIGHT DOWN SEAM!</text>
            </g>
            <!-- Staggered Interlocking Bond -->
            <g id="wb-staggered-svg" class="hidden">
                <!-- Row 1 -->
                <rect x="75" y="105" width="54" height="25" fill="#b91c1c" stroke="#cbd5e1" />
                <rect x="131" y="105" width="54" height="25" fill="#b91c1c" stroke="#cbd5e1" />
                <rect x="187" y="105" width="54" height="25" fill="#b91c1c" stroke="#cbd5e1" />
                <!-- Row 2 (Shifted Half) -->
                <rect x="75" y="78" width="26" height="25" fill="#dc2626" stroke="#cbd5e1" />
                <rect x="103" y="78" width="54" height="25" fill="#dc2626" stroke="#cbd5e1" />
                <rect x="159" y="78" width="54" height="25" fill="#dc2626" stroke="#cbd5e1" />
                <rect x="215" y="78" width="26" height="25" fill="#dc2626" stroke="#cbd5e1" />
                <!-- Row 3 -->
                <rect x="75" y="51" width="54" height="25" fill="#b91c1c" stroke="#cbd5e1" />
                <rect x="131" y="51" width="54" height="25" fill="#b91c1c" stroke="#cbd5e1" />
                <rect x="187" y="51" width="54" height="25" fill="#b91c1c" stroke="#cbd5e1" />
                <text x="160" y="34" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">INTERLOCKED BRICKS LOCK SOLIDLY!</text>
            </g>
            <text x="160" y="162" fill="#fda4af" font-size="10" font-weight="bold" text-anchor="middle" id="wb-svg-lbl">Aligned vertical seams let individual brick towers tip apart easily!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-rose-300 text-sm" id="wb-title">Straight Vertical Columns (Weak Split)</h4>
            <p class="text-slate-300 leading-relaxed" id="wb-desc">Stacking bricks strictly directly on top of each other builds tall independent towers separated by long vertical cracks! A gentle side push topples one strip right away.</p>
        </div>
    </div>
</div>

<script>
function testWallBond(mode) {
    const map = {
        straight: { lbl: 'Aligned vertical seams let individual brick towers tip apart easily!', t: 'Straight Vertical Columns (Weak Split)', d: 'Stacking bricks strictly directly on top of each other builds tall independent towers separated by long vertical cracks! A gentle side push topples one strip right away.' },
        staggered: { lbl: 'Overlapping staggered joints spread sideways weight evenly everywhere!', t: 'Staggered Running-Bond Interlock (Rock Solid)', d: 'Every upper brick bridges securely right across the meeting seam of two lower bricks! Sideways force transfers down through the whole locked wall cleanly without splitting.' }
    };
    const d = map[mode];
    if (!d) return;
    ['straight', 'staggered'].forEach(k => {
        const b = document.getElementById('btn-wb-' + k);
        if (b) {
            b.className = (k === mode)
                ? 'p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('wb-' + k + '-svg');
        if (g) {
            if (k === mode) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('wb-svg-lbl').textContent = d.lbl;
    document.getElementById('wb-title').textContent = d.t;
    document.getElementById('wb-desc').textContent = d.d;
}
</script>
"""

# Simulator 14: Construction Safety Gear
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⛑️</span>
            <h3 class="text-sm sm:text-base font-bold text-yellow-300">Construction Site Protective Gear Inspector</h3>
        </div>
        <span class="text-[11px] bg-yellow-950/80 text-yellow-300 px-2.5 py-1 rounded-full border border-yellow-800">Safety First</span>
    </div>

    <p class="text-xs text-slate-300">Click each piece of protective site equipment to discover which real construction hazards it shields workers against!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectPPE('helmet')" id="btn-ppe-helmet" class="p-2.5 rounded-xl bg-yellow-600 text-white font-bold text-xs border border-yellow-500">⛑️ Hard Helmet</button>
        <button onclick="inspectPPE('vest')" id="btn-ppe-vest" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🦺 Safety Vest</button>
        <button onclick="inspectPPE('boots')" id="btn-ppe-boots" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🥾 Heavy Boots</button>
        <button onclick="inspectPPE('gloves')" id="btn-ppe-gloves" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧤 Gloves &amp; Goggles</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 175" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Hard Helmet -->
            <g id="ppe-helmet-svg">
                <path d="M95,105 Q160,30 225,105 Z" fill="#facc15" />
                <rect x="85" y="103" width="150" height="12" rx="5" fill="#eab308" />
                <path d="M115,115 L145,142 L175,142 L205,115" fill="none" stroke="#94a3b8" stroke-width="3" />
                <line x1="160" y1="22" x2="160" y2="52" stroke="#38bdf8" stroke-width="3" />
            </g>
            <!-- Safety Vest -->
            <g id="ppe-vest-svg" class="hidden">
                <polygon points="105,45 140,45 160,82 180,45 215,45 225,135 95,135" fill="#f97316" />
                <rect x="98" y="88" width="124" height="10" fill="#fde047" />
                <rect x="96" y="112" width="128" height="10" fill="#fde047" />
            </g>
            <!-- Heavy Boots -->
            <g id="ppe-boots-svg" class="hidden">
                <path d="M115,48 L155,48 L160,105 L198,108 Q210,122 195,132 L112,132 Z" fill="#78350f" />
                <rect x="110" y="130" width="90" height="10" rx="3" fill="#334155" />
            </g>
            <!-- Gloves & Goggles -->
            <g id="ppe-gloves-svg" class="hidden">
                <rect x="85" y="55" width="60" height="32" rx="10" fill="#38bdf8" opacity="0.65" stroke="#e2e8f0" stroke-width="3" />
                <rect x="175" y="55" width="60" height="32" rx="10" fill="#38bdf8" opacity="0.65" stroke="#e2e8f0" stroke-width="3" />
                <line x1="145" y1="70" x2="175" y2="70" stroke="#e2e8f0" stroke-width="4" />
                <text x="160" y="122" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">SHIELDS HANDS &amp; EYES FROM DUST!</text>
            </g>
            <text x="160" y="162" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle" id="ppe-svg-lbl">Tough strapped plastic shells deflect accidentally dropped tools &amp; bricks!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-yellow-300 text-sm" id="ppe-title">Strapped Hard Safety Helmet</h4>
            <p class="text-slate-300 leading-relaxed" id="ppe-desc">Tough impact-proof yellow helmets fastened snugly with chin straps guard workers heads safely from unexpected falling bricks, wooden planks, or low scaffolding pipes.</p>
        </div>
    </div>
</div>

<script>
function inspectPPE(item) {
    const map = {
        helmet: { lbl: 'Tough strapped plastic shells deflect accidentally dropped tools & bricks!', t: 'Strapped Hard Safety Helmet', d: 'Tough impact-proof yellow helmets fastened snugly with chin straps guard workers heads safely from unexpected falling bricks, wooden planks, or low scaffolding pipes.' },
        vest: { lbl: 'Neon glowing stripes warn crane & truck operators clearly across busy sites!', t: 'Bright Reflective Safety Vest', d: 'Fluorescent orange fabric lined with bright reflective silver bands makes every worker clearly visible around moving cranes, trucks, and dusty scaffolds!' },
        boots: { lbl: 'Thick treaded soles stop sharp nails & rolling stones from hurting feet!', t: 'Sturdy Thick-Soled Safety Boots', d: 'Reinforced protective boots shield toes against dropped heavy stones and keep sharp scattered metal nails or broken brick edges from poking feet.' },
        gloves: { lbl: 'Snug gloves & clear eye goggles block wet lime burns & flying sparks!', t: 'Work Gloves & Clear Protective Goggles', d: 'Rough bricks and damp cement irritate bare palms quickly while sawing wood sprays sharp dust. Snug gloves and wrap-around goggles keep skin and eyes protected!' }
    };
    const d = map[item];
    if (!d) return;
    ['helmet', 'vest', 'boots', 'gloves'].forEach(k => {
        const b = document.getElementById('btn-ppe-' + k);
        if (b) {
            b.className = (k === item)
                ? 'p-2.5 rounded-xl bg-yellow-600 text-white font-bold text-xs border border-yellow-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('ppe-' + k + '-svg');
        if (g) {
            if (k === item) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('ppe-svg-lbl').textContent = d.lbl;
    document.getElementById('ppe-title').textContent = d.t;
    document.getElementById('ppe-desc').textContent = d.d;
}
</script>
"""

# Simulator 15: Meeting Craft Makers
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪵</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Neighborhood Artisans &amp; Toy Makers Notebook</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Community Crafts</span>
    </div>

    <p class="text-xs text-slate-300">Visit skilled local creators around town to discover their raw materials, traditional hand tools, and patient craftsmanship!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectArtisan('potter')" id="btn-art-potter" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">🏺 Potter</button>
        <button onclick="inspectArtisan('toymaker')" id="btn-art-toymaker" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪀 Toy Maker</button>
        <button onclick="inspectArtisan('weaver')" id="btn-art-weaver" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧺 Bamboo Weaver</button>
        <button onclick="inspectArtisan('mason')" id="btn-art-mason" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧱 Brick Mason</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 175" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Potter -->
            <g id="art-potter-svg">
                <ellipse cx="160" cy="128" rx="75" ry="12" fill="#64748b" />
                <path d="M135,126 Q110,95 142,68 L178,68 Q210,95 185,126 Z" fill="#ea580c" />
                <text x="160" y="42" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Clay + Wheel + Hot Kiln</text>
            </g>
            <!-- Toymaker -->
            <g id="art-toymaker-svg" class="hidden">
                <polygon points="160,128 125,65 195,65" fill="#ef4444" />
                <rect x="125" y="65" width="70" height="16" fill="#fde047" />
                <rect x="155" y="42" width="10" height="23" fill="#b45309" />
                <text x="160" y="150" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Carved Spinning Wood Top (Lattu)</text>
            </g>
            <!-- Bamboo Weaver -->
            <g id="art-weaver-svg" class="hidden">
                <polygon points="105,65 215,65 195,130 125,130" fill="#d97706" stroke="#fde047" stroke-width="2" />
                <line x1="115" y1="88" x2="205" y2="88" stroke="#78350f" stroke-width="3" />
                <line x1="120" y1="108" x2="200" y2="108" stroke="#78350f" stroke-width="3" />
                <text x="160" y="42" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Interlaced Split Bamboo Baskets</text>
            </g>
            <!-- Brick Mason -->
            <g id="art-mason-svg" class="hidden">
                <rect x="95" y="95" width="60" height="28" fill="#b91c1c" stroke="#cbd5e1" />
                <rect x="160" y="95" width="60" height="28" fill="#b91c1c" stroke="#cbd5e1" />
                <rect x="125" y="64" width="60" height="28" fill="#dc2626" stroke="#cbd5e1" />
                <polygon points="200,72 245,55 215,92" fill="#94a3b8" />
                <text x="160" y="42" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Brick Trowel + Plumb Bob Level</text>
            </g>
            <text x="160" y="164" fill="#fdba74" font-size="10" font-weight="bold" text-anchor="middle" id="art-svg-lbl">Potters blend wet earth, swift wheel motion, and kiln fire cleanly!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-amber-300 text-sm" id="art-title">Local Terracotta Clay Potter</h4>
            <p class="text-slate-300 leading-relaxed" id="art-desc">Guided by practiced eyes and smooth water-wetted hands, neighborhood potters turn ordinary riverbank mud into useful cooling matkas, lamps, and flowerpots without polluting plastic!</p>
        </div>
    </div>
</div>

<script>
function inspectArtisan(role) {
    const map = {
        potter: { lbl: 'Potters blend wet earth, swift wheel motion, and kiln fire cleanly!', t: 'Local Terracotta Clay Potter', d: 'Guided by practiced eyes and smooth water-wetted hands, neighborhood potters turn ordinary riverbank mud into useful cooling matkas, lamps, and flowerpots without polluting plastic!' },
        toymaker: { lbl: 'Seasoned soft timber turns smoothly into safe lac-colored spinning tops!', t: 'Traditional Wooden Toy Maker', d: 'Using natural timber offcuts and safe glossy vegetable-lac dyes, wooden toy makers carve spinning tops, rolling carts, and colorful dolls passed joyfully across families!' },
        weaver: { lbl: 'Flexible split bamboo strips weave airy light grain baskets & fans!', t: 'Patient Bamboo Basket Weaver', d: 'Soaked flexible cane and split bamboo strips interlace smoothly over-and-under into durable airy storage baskets, sleeping mats, and summer hand fans.' },
        mason: { lbl: 'Steel trowels, string lines & plumb bobs raise razor-straight walls!', t: 'Skilled Brick Mason & Builder', d: 'Measuring angles carefully with weighted string plumb bobs and steel trowels, masons interlock thousands of bricks securely into tall schools and family homes.' }
    };
    const d = map[role];
    if (!d) return;
    ['potter', 'toymaker', 'weaver', 'mason'].forEach(k => {
        const b = document.getElementById('btn-art-' + k);
        if (b) {
            b.className = (k === role)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('art-' + k + '-svg');
        if (g) {
            if (k === role) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('art-svg-lbl').textContent = d.lbl;
    document.getElementById('art-title').textContent = d.t;
    document.getElementById('art-desc').textContent = d.d;
}
</script>
"""

# Simulator 16: Making Things Review
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧠</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Chapter 11 Master Craft Review Workbench</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Rapid Matcher</span>
    </div>

    <p class="text-xs text-slate-300">Select each craft item below and pick its exact scientific purpose across Pottery, Nature Patterns, Bricks, and Safety!</p>

    <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
        <button onclick="checkCh11Review('kiln')" id="btn-c11r-kiln" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Hot Clay Kiln</button>
        <button onclick="checkCh11Review('sieve')" id="btn-c11r-sieve" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Mesh Sieve</button>
        <button onclick="checkCh11Review('mould')" id="btn-c11r-mould" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Brick Mould</button>
        <button onclick="checkCh11Review('straw')" id="btn-c11r-straw" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Straw &amp; Cow Dung</button>
        <button onclick="checkCh11Review('stagger')" id="btn-c11r-stagger" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Staggered Bricks</button>
        <button onclick="checkCh11Review('helmet')" id="btn-c11r-helmet" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Hard Helmet</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex items-center justify-between">
            <h4 class="font-bold text-cyan-300 text-sm" id="c11r-title">Hot Clay &amp; Brick Baking Kiln</h4>
            <span class="px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 font-bold text-[10px]" id="c11r-tag">Thermal Transformation</span>
        </div>
        <p class="text-slate-300 leading-relaxed" id="c11r-desc">Bakes dried clay pots and moulded mud bricks under intense glowing heat until grains fuse permanently into hard, strong, waterproof terracotta!</p>
    </div>
</div>

<script>
function checkCh11Review(item) {
    const map = {
        kiln: { tag: 'Thermal Transformation', t: 'Hot Clay & Brick Baking Kiln', d: 'Bakes dried clay pots and moulded mud bricks under intense glowing heat until grains fuse permanently into hard, strong, waterproof terracotta!' },
        sieve: { tag: 'Soil Purification', t: 'Fine Wire Mesh Sieve', d: 'Separates hard stones, gravel pebbles, and dry sticks away from garden soil so only pure silky clay dust sinks to the bottom of settling water!' },
        mould: { tag: 'Uniform Shaping', t: 'Hollow Rectangular Wooden Mould', d: 'Shapes soft mud paste into crisp bricks sharing identical size and flat faces so tall masonry walls stack evenly without gaps.' },
        straw: { tag: 'Natural Insulation', t: 'Chopped Straw & Smooth Cow-Dung Plaster', d: 'Mixes fibrous straw into mud bricks to prevent cracking and keep rooms delightfully cool, while glossy cow-dung plaster naturally wards off household pests!' },
        stagger: { tag: 'Structural Strength', t: 'Staggered Interlocking Brick Rows', d: 'Places every upper brick centered cleanly over lower brick joints, eliminating long vertical fault cracks and locking strong walls together tightly.' },
        helmet: { tag: 'Site Protection', t: 'Strapped Hard Construction Helmet', d: 'Shields builders and masons reliably against accidental falling bricks, wood planks, or overhead scaffolding bumps on active construction sites.' }
    };
    const d = map[item];
    if (!d) return;
    ['kiln', 'sieve', 'mould', 'straw', 'stagger', 'helmet'].forEach(k => {
        const b = document.getElementById('btn-c11r-' + k);
        if (b) {
            b.className = (k === item)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('c11r-tag').textContent = d.tag;
    document.getElementById('c11r-title').textContent = d.t;
    document.getElementById('c11r-desc').textContent = d.d;
}
</script>
"""
