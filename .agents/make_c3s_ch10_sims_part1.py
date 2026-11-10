#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 10: This World of Things
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Sunlit Classroom Objects
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">☀️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Sunlit Classroom Scene &amp; Object Material Explorer</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Classroom Tour</span>
    </div>

    <p class="text-xs text-slate-300">Click items inside the sunlit classroom sketch to inspect why sunlight streams through glass yet stops at wooden doors!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectClassItem('window')" id="btn-cls-window" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">🪟 Window Glass</button>
        <button onclick="inspectClassItem('desk')" id="btn-cls-desk" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪑 Wooden Desk</button>
        <button onclick="inspectClassItem('latch')" id="btn-cls-latch" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🔒 Metal Hinge</button>
        <button onclick="inspectClassItem('curtain')" id="btn-cls-curtain" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪟 Cloth Curtain</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 185" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <rect x="0" y="0" width="320" height="145" fill="#1e293b" />
            <rect x="0" y="145" width="320" height="40" fill="#334155" />
            <!-- Sunlit Window -->
            <rect x="30" y="25" width="90" height="80" fill="#38bdf8" opacity="0.45" stroke="#cbd5e1" stroke-width="3" />
            <!-- Sunbeams Diagonal -->
            <polygon points="30,105 120,25 220,145 90,145" fill="#fde047" opacity="0.22" />
            <!-- Wooden Desk -->
            <rect x="135" y="100" width="85" height="12" fill="#92400e" />
            <rect x="142" y="112" width="10" height="33" fill="#78350f" />
            <rect x="202" y="112" width="10" height="33" fill="#78350f" />
            <!-- Metal Hinged Door -->
            <rect x="245" y="40" width="55" height="105" fill="#78350f" stroke="#451a03" stroke-width="2" />
            <rect x="245" y="65" width="8" height="12" fill="#cbd5e1" />
            <rect x="245" y="115" width="8" height="12" fill="#cbd5e1" />
            <text x="160" y="170" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle" id="cls-svg-lbl">Sunlight shines cleanly through transparent window glass!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-amber-300 text-sm" id="cls-title">Clear Glass Windowpanes</h4>
            <p class="text-slate-300 leading-relaxed" id="cls-desc">Clear glass lets golden sunshine stream brightly inside to illuminate desks and books while keeping wind, insects, and dust outside!</p>
        </div>
    </div>
</div>

<script>
function inspectClassItem(item) {
    const map = {
        window: { lbl: 'Sunlight shines cleanly through transparent window glass!', t: 'Clear Glass Windowpanes', d: 'Clear glass lets golden sunshine stream brightly inside to illuminate desks and books while keeping wind, insects, and dust outside!' },
        desk: { lbl: 'Sturdy hardwood desks support heavy notebooks!', t: 'Rigid Wooden Desks & Benches', d: 'Sawed from durable forest timber, rigid wood planks support heavy books and sitting learners cleanly without sagging.' },
        latch: { lbl: 'Strong metal hinges let wooden doors swing!', t: 'Strong Metal Hinges, Nails & Latches', d: 'Forged from tough iron and brass extracted from Earth ores, metal hardware handles constant heavy door swinging safely.' },
        curtain: { lbl: 'Flexible woven cloth curtains sway smoothly!', t: 'Flexible Woven Cotton Curtains', d: 'Soft pliable fabric folds effortlessly into neat pleats to shade bright afternoon glare while swaying peacefully in breezes.' }
    };
    const d = map[item];
    if (!d) return;

    ['window', 'desk', 'latch', 'curtain'].forEach(k => {
        const b = document.getElementById('btn-cls-' + k);
        if (b) {
            b.className = (k === item)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('cls-svg-lbl').textContent = d.lbl;
    document.getElementById('cls-title').textContent = d.t;
    document.getElementById('cls-desc').textContent = d.d;
}
</script>
"""

# Simulator 2: Wood And Metals (Tree Timber vs Earth Rock Ore)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⛏️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Activity 1 &amp; 2: Tree Wood vs Underground Earth Metal Ores</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Material Origins</span>
    </div>

    <p class="text-xs text-slate-300">Trace wooden chairs back to sunny forests versus metal hinges and nails back to rocky mineral ores deep inside Earth!</p>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="selectOriginType('wood')" id="btn-or-wood" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 text-left flex items-center gap-2">
            <span class="text-2xl">🌳</span>
            <div><span class="block">Wood Items (Desks, Doors, Rulers)</span><span class="text-[10px] text-emerald-200">Harvested Forest Timber</span></div>
        </button>
        <button onclick="selectOriginType('metal')" id="btn-or-metal" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-2xl">🪨</span>
            <div><span class="block">Metal Items (Nails, Hinges, Latches)</span><span class="text-[10px] text-slate-400">Excavated Rock Ores</span></div>
        </button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="or-emoji">🌳➡️🪑</div>
        <div class="space-y-1">
            <h4 class="font-bold text-emerald-300 text-sm" id="or-title">Forest Trees &rarr; Timber Planks &rarr; Desks &amp; Doors</h4>
            <p class="text-slate-300" id="or-desc">Living trees grow sturdy woody trunks above ground. Carpenters saw dried wood planks into light, strong, non-rusting furniture and pencils!</p>
        </div>
    </div>
</div>

<script>
function selectOriginType(t) {
    const isWood = (t === 'wood');
    document.getElementById('btn-or-wood').className = isWood
        ? 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 text-left flex items-center gap-2'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';
    document.getElementById('btn-or-metal').className = !isWood
        ? 'p-3 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500 text-left flex items-center gap-2'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';

    document.getElementById('or-emoji').textContent = isWood ? '🌳➡️🪑' : '⛏️🔥🔩';
    document.getElementById('or-title').textContent = isWood
        ? 'Forest Trees → Timber Planks → Desks & Doors'
        : 'Underground Mineral Ores → Hot Furnace Smelting → Nails & Hinges';
    document.getElementById('or-title').className = isWood ? 'font-bold text-emerald-300 text-sm' : 'font-bold text-amber-300 text-sm';
    document.getElementById('or-desc').textContent = isWood
        ? 'Living trees grow sturdy woody trunks above ground. Carpenters saw dried wood planks into light, strong, non-rusting furniture and pencils!'
        : 'Miners dig mineral-rich rock sediments called ores from deep underground. Fierce furnace heat melts out iron, copper, and aluminum to forge tough nails, latches, and bells!';
}
</script>
"""

# Simulator 3: Light Passing Through (Flashlight Shadow Bench)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔦</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Activity 3 &amp; 4: Flashlight Beam &amp; Shadow Test Lab</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Optics Lab</span>
    </div>

    <p class="text-xs text-slate-300">Shine a bright pocket flashlight against three objects and watch what appears on the white wall behind them!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="shineTorch('glass')" id="btn-trc-glass" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">1. Clear Glass Sheet</button>
        <button onclick="shineTorch('paper')" id="btn-trc-paper" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. Paper Lampshade</button>
        <button onclick="shineTorch('wood')" id="btn-trc-wood" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. Wooden Textbook</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 180" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Torch on Left -->
            <rect x="40" y="75" width="75" height="30" rx="6" fill="#475569" />
            <polygon points="115,72 135,62 135,118 115,108" fill="#fbbf24" />
            <text x="85" y="130" fill="#fde047" font-size="10" text-anchor="middle">Torch Beam</text>

            <!-- Incoming Light Cone -->
            <polygon points="135,65 340,42 340,138 135,115" fill="#fde047" opacity="0.45" />

            <!-- Test Object Center -->
            <rect id="trc-obj-bar" x="340" y="32" width="16" height="116" fill="#38bdf8" opacity="0.45" stroke="#ffffff" stroke-width="2" />

            <!-- Outgoing Light Cone -->
            <polygon id="trc-out-cone" points="356,42 610,18 610,162 356,138" fill="#fde047" opacity="0.42" />

            <!-- White Wall Right -->
            <rect x="610" y="15" width="22" height="150" fill="#f8fafc" />
            <ellipse id="trc-wall-spot" cx="621" cy="90" rx="8" ry="52" fill="#facc15" opacity="0.9" />

            <text id="trc-svg-status" x="480" y="165" fill="#7dd3fc" font-size="12" font-weight="bold" text-anchor="middle">Bright Beam Passes Cleanly! (No Dark Shadow)</text>
        </svg>
    </div>
</div>

<script>
function shineTorch(obj) {
    const map = {
        glass: { objFill: '#38bdf8', objOp: '0.45', outOp: '0.42', spotFill: '#facc15', spotOp: '0.9', lbl: 'Bright Beam Passes Cleanly! (No Dark Shadow)', lc: '#7dd3fc' },
        paper: { objFill: '#e2e8f0', objOp: '0.85', outOp: '0.18', spotFill: '#fef08a', spotOp: '0.5', lbl: 'Partial Soft Glow Filters Through (Fuzzy Scatter!)', lc: '#fde047' },
        wood: { objFill: '#92400e', objOp: '1', outOp: '0', spotFill: '#0f172a', spotOp: '0.95', lbl: 'ALL Light Blocked! Crisp Dark Shadow Cast on Wall!', lc: '#f87171' }
    };
    const d = map[obj];
    if (!d) return;

    ['glass', 'paper', 'wood'].forEach(k => {
        const b = document.getElementById('btn-trc-' + k);
        if (b) {
            b.className = (k === obj)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('trc-obj-bar').setAttribute('fill', d.objFill);
    document.getElementById('trc-obj-bar').setAttribute('opacity', d.objOp);
    document.getElementById('trc-out-cone').setAttribute('opacity', d.outOp);
    document.getElementById('trc-wall-spot').setAttribute('fill', d.spotFill);
    document.getElementById('trc-wall-spot').setAttribute('opacity', d.spotOp);
    document.getElementById('trc-svg-status').textContent = d.lbl;
    document.getElementById('trc-svg-status').setAttribute('fill', d.lc);
}
</script>
"""

# Simulator 4: See Through Glasses (Transparent vs Translucent vs Opaque Classifier)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">👓</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Transparent, Translucent &amp; Opaque Room Architect</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Optical Sorting</span>
    </div>

    <p class="text-xs text-slate-300">Inspect each of the three optical material families and discover why builders select each type purposefully!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="selectOptic('transparent')" id="btn-op-transparent" class="p-3 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left">
            <span class="block">1. Transparent</span>
            <span class="text-[10px] text-cyan-200">Sharp Crystal Visibility</span>
        </button>
        <button onclick="selectOptic('translucent')" id="btn-op-translucent" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left">
            <span class="block">2. Translucent</span>
            <span class="text-[10px] text-slate-400">Partial Cozy Soft Glow</span>
        </button>
        <button onclick="selectOptic('opaque')" id="btn-op-opaque" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left">
            <span class="block">3. Opaque</span>
            <span class="text-[10px] text-slate-400">Blocks Light &amp; Privacy</span>
        </button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="op-emoji">👓💧</div>
        <div class="space-y-1">
            <h4 class="font-bold text-cyan-300 text-sm" id="op-title">Transparent Materials — Clear Glass, Water &amp; Air</h4>
            <p class="text-slate-300" id="op-desc">Allows nearly 100% of light rays straight through cleanly without scattering. Ideal for car windshields, spectacles, fish aquariums, and sunny classroom windows!</p>
        </div>
    </div>
</div>

<script>
function selectOptic(op) {
    const map = {
        transparent: { e: '👓💧', t: 'Transparent Materials — Clear Glass, Water & Air', d: 'Allows nearly 100% of light rays straight through cleanly without scattering. Ideal for car windshields, spectacles, fish aquariums, and sunny classroom windows!' },
        translucent: { e: '🪔🌫️', t: 'Translucent Materials — Paper Lampshade, Butter Paper & Frosted Glass', d: 'Lets soft diffused glow filter through while hiding crisp sharp details—perfect for gentle non-glaring bedroom lampshades and private frosted bathroom windows!' },
        opaque: { e: '🧱🚪', t: 'Opaque Materials — Wood Doors, Brick Walls & Steel Plates', d: 'Stops ALL light rays completely so nothing shows behind—giving solid structural privacy for bedrooms, cupboards, and sun-blocking roof shades!' }
    };
    const d = map[op];
    if (!d) return;

    ['transparent', 'translucent', 'opaque'].forEach(k => {
        const b = document.getElementById('btn-op-' + k);
        if (b) {
            b.className = (k === op)
                ? 'p-3 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left'
                : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left';
        }
    });
    document.getElementById('op-emoji').textContent = d.e;
    document.getElementById('op-title').textContent = d.t;
    document.getElementById('op-desc').textContent = d.d;
}
</script>
"""

# Simulator 5: Colored Filter Magic
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌈</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Colored Transparent Wrapper &amp; Bottle Filter Lab</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Color Physics</span>
    </div>

    <p class="text-xs text-slate-300">Hold different colored transparent bags or bottles before your eyes and notice how perceived colors shift while shapes stay clear!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setColorFilter('clear')" id="btn-cf-clear" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">⬜ Colorless Clear</button>
        <button onclick="setColorFilter('red')" id="btn-cf-red" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🟥 Red Wrapper</button>
        <button onclick="setColorFilter('green')" id="btn-cf-green" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🟩 Green Bottle</button>
        <button onclick="setColorFilter('yellow')" id="btn-cf-yellow" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🟨 Yellow Sheet</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center relative overflow-hidden">
        <div id="cf-preview-box" class="p-6 rounded-xl bg-white text-slate-900 transition-colors duration-300 border-2 border-slate-700">
            <div class="text-3xl mb-1">🏡 🌸 📘</div>
            <div class="font-bold text-sm" id="cf-status-text">Natural Full-Spectrum View: White paper, pink flower, and blue book look completely normal!</div>
        </div>
    </div>
</div>

<script>
function setColorFilter(c) {
    const map = {
        clear: { bg: '#ffffff', txt: '#0f172a', msg: 'Natural Full-Spectrum View: All seven rainbow colors pass through equally so objects keep true natural hues!' },
        red: { bg: '#fca5a5', txt: '#7f1d1d', msg: 'Red Transparent Filter: Passes primarily RED light waves—white backgrounds glow rosy red while object outlines remain sharp!' },
        green: { bg: '#86efac', txt: '#14532d', msg: 'Green Glass Bottle Filter: Lets GREEN light pass cleanly through while absorbing red rays—still transparent enough to spot crisp shapes!' },
        yellow: { bg: '#fef08a', txt: '#713f12', msg: 'Yellow Transparent Sheet: Casts a bright golden sunny tint over books and chairs without blocking sharp outlines!' }
    };
    const d = map[c];
    if (!d) return;

    ['clear', 'red', 'green', 'yellow'].forEach(k => {
        const b = document.getElementById('btn-cf-' + k);
        if (b) {
            b.className = (k === c)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    const box = document.getElementById('cf-preview-box');
    box.style.backgroundColor = d.bg;
    box.style.color = d.txt;
    document.getElementById('cf-status-text').textContent = d.msg;
}
</script>
"""

# Simulator 6: Six Everyday Materials
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🗂️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Six Material Families &amp; Multi-Material Pencil Dissection</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Material Sorting</span>
    </div>

    <p class="text-xs text-slate-300">Sort everyday items across all six classic material groups—plus click the pencil to inspect three materials teaming up in one tool!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-1.5">
        <button onclick="selectMaterialCat('wood')" id="btn-mc-wood" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-[11px] border border-emerald-500">🪵 Wood</button>
        <button onclick="selectMaterialCat('metal')" id="btn-mc-metal" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-[11px] border border-slate-700 hover:bg-slate-800">🔩 Metal</button>
        <button onclick="selectMaterialCat('glass')" id="btn-mc-glass" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-[11px] border border-slate-700 hover:bg-slate-800">🥛 Glass</button>
        <button onclick="selectMaterialCat('plastic')" id="btn-mc-plastic" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-[11px] border border-slate-700 hover:bg-slate-800">🧴 Plastic</button>
        <button onclick="selectMaterialCat('clay')" id="btn-mc-clay" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-[11px] border border-slate-700 hover:bg-slate-800">🏺 Clay</button>
        <button onclick="selectMaterialCat('rubber')" id="btn-mc-rubber" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-[11px] border border-slate-700 hover:bg-slate-800">✏️ Rubber</button>
        <button onclick="selectMaterialCat('pencil')" id="btn-mc-pencil" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-[11px] border border-amber-700 hover:bg-slate-800">✏️ 3-in-1 Pencil</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-4xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="mc-emoji">🪵🪑</div>
        <div class="space-y-1">
            <h4 class="font-bold text-emerald-300 text-sm" id="mc-title">Wood — Desks, Cricket Bats, Rulers &amp; Spoons</h4>
            <p class="text-slate-300" id="mc-desc">Sturdy, rigid, thermally insulating timber carved easily by carpenters into long-lasting classroom furniture and warm handles!</p>
        </div>
    </div>
</div>

<script>
function selectMaterialCat(m) {
    const map = {
        wood: { e: '🪵🪑', t: 'Wood — Desks, Cricket Bats, Rulers & Spoons', d: 'Sturdy, rigid, thermally insulating timber carved easily by carpenters into long-lasting classroom furniture and warm handles!' },
        metal: { e: '🔩🥄', t: 'Metals — Steel Spoons, Locks, Brass Bells & Hinges', d: 'Extremely strong, shiny, heat-conducting, and ringing metals smelted from mineral ores inside deep Earth rocks!' },
        glass: { e: '🥛🪟', t: 'Glass — Clear Windows, Test Tubes, Marbles & Jars', d: 'Sparkling smooth and transparent material melted from sand—easy to see through cleanly yet shatters carefully if dropped.' },
        plastic: { e: '🧴📐', t: 'Plastic — Waterproof Raincoats, Scales & Lunchboxes', d: 'Featherlight, colorful, moldable waterproof synthetic material—best reused repeatedly rather than thrown into river litter!' },
        clay: { e: '🏺🧱', t: 'Clay — Terracotta Matkas, Red Bricks & Flowerpots', d: 'Cool porous earthen soil sculpted upon spinning wheels and kiln-baked hard to hold summer water or build houses.' },
        rubber: { e: '🚲🧽', t: 'Rubber — Pencil Erasers, Bike Tires & Hair Bands', d: 'Bouncy, waterproof, gripping flexible material prized for erasing pencil lines cleanly and absorbing bumpy bike road shocks!' },
        pencil: { e: '✏️✨', t: '3-in-1 Teammate Object: Eraser-Tipped Pencil!', d: 'Look closely: lightweight WOOD forms the shaft to grip, strong METAL clamps the top ring, and elastic RUBBER rubs pencil marks off paper!' }
    };
    const d = map[m];
    if (!d) return;

    ['wood', 'metal', 'glass', 'plastic', 'clay', 'rubber', 'pencil'].forEach(k => {
        const b = document.getElementById('btn-mc-' + k);
        if (b) {
            b.className = (k === m)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-[11px] border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-[11px] border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('mc-emoji').textContent = d.e;
    document.getElementById('mc-title').textContent = d.t;
    document.getElementById('mc-desc').textContent = d.d;
}
</script>
"""

# Simulator 7: Natural Source Chains
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⛓️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Material Origin Chain Game: Tracing Back to Earth</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Source Detective</span>
    </div>

    <p class="text-xs text-slate-300">Click any finished item to trace its manufacturing links backward until discovering its surprising raw origin in nature!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="traceChain('glass')" id="btn-ch-glass" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">🥛 Clear Glass Cup</button>
        <button onclick="traceChain('rubber')" id="btn-ch-rubber" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧽 Rubber Eraser</button>
        <button onclick="traceChain('clay')" id="btn-ch-clay" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🏺 Clay Matka</button>
        <button onclick="traceChain('paper')" id="btn-ch-paper" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">📓 School Notebook</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 space-y-3 text-center text-xs">
        <div class="flex flex-wrap items-center justify-center gap-3 text-sm font-bold text-amber-300" id="ch-steps-row">
            <span class="px-3 py-1.5 bg-slate-900 rounded-xl border border-slate-700">🥛 Glass Cup</span>
            <span>⬅️ Molten Furnace</span>
            <span class="px-3 py-1.5 bg-slate-900 rounded-xl border border-slate-700">🔥 1,500°C Melt</span>
            <span>⬅️ Earth Source</span>
            <span class="px-3 py-1.5 bg-emerald-950 rounded-xl border border-emerald-700 text-emerald-300">🏖️ White Silica Sand!</span>
        </div>
        <p id="ch-explanation" class="text-slate-300 max-w-2xl mx-auto">
            Incredibly, transparent glass tumblers and windowpanes begin life as fine white river or desert silica sand melted inside blazing factory furnaces!
        </p>
    </div>
</div>

<script>
function traceChain(item) {
    const map = {
        glass: {
            row: '<span class="px-3 py-1.5 bg-slate-900 rounded-xl border border-slate-700">🥛 Glass Cup</span><span>⬅️ Molded Glass</span><span class="px-3 py-1.5 bg-slate-900 rounded-xl border border-slate-700">🔥 Furnace Melt</span><span>⬅️ Raw Source</span><span class="px-3 py-1.5 bg-emerald-950 rounded-xl border border-emerald-700 text-emerald-300">🏖️ White Silica Sand!</span>',
            desc: 'Incredibly, transparent glass tumblers and windowpanes begin life as fine white river or desert silica sand melted inside blazing factory furnaces!'
        },
        rubber: {
            row: '<span class="px-3 py-1.5 bg-slate-900 rounded-xl border border-slate-700">🧽 Rubber Eraser</span><span>⬅️ Cured Elastic</span><span class="px-3 py-1.5 bg-slate-900 rounded-xl border border-slate-700">🥣 Milky Sap</span><span>⬅️ Living Source</span><span class="px-3 py-1.5 bg-emerald-950 rounded-xl border border-emerald-700 text-emerald-300">🌴 Rubber Tree Latex!</span>',
            desc: 'Natural bouncy rubber starts as milky white liquid latex tapped carefully from incisions on tropical rubber tree trunks!'
        },
        clay: {
            row: '<span class="px-3 py-1.5 bg-slate-900 rounded-xl border border-slate-700">🏺 Clay Matka</span><span>⬅️ Kiln Fired</span><span class="px-3 py-1.5 bg-slate-900 rounded-xl border border-slate-700">🎡 Potter Wheel</span><span>⬅️ Earth Source</span><span class="px-3 py-1.5 bg-emerald-950 rounded-xl border border-emerald-700 text-emerald-300">🟤 Wet River Bank Clay!</span>',
            desc: 'Cooling earthen water pots and strong house bricks begin as damp fine clay dug beside riverbeds and shaped by potters!'
        },
        paper: {
            row: '<span class="px-3 py-1.5 bg-slate-900 rounded-xl border border-slate-700">📓 Crisp Paper</span><span>⬅️ Pressed Pulp</span><span class="px-3 py-1.5 bg-slate-900 rounded-xl border border-slate-700">🪵 Wood Chips</span><span>⬅️ Living Source</span><span class="px-3 py-1.5 bg-emerald-950 rounded-xl border border-emerald-700 text-emerald-300">🌲 Forest Tree Timber!</span>',
            desc: 'Writing notebook sheets derive from crushed tree wood pulp—reminding students to write cleanly on both sides of paper and recycle!'
        }
    };
    const d = map[item];
    if (!d) return;

    ['glass', 'rubber', 'clay', 'paper'].forEach(k => {
        const b = document.getElementById('btn-ch-' + k);
        if (b) {
            b.className = (k === item)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('ch-steps-row').innerHTML = d.row;
    document.getElementById('ch-explanation').textContent = d.desc;
}
</script>
"""

# Simulator 8: Feel And Shine (Sensory Touch & Thermal Feel Bench)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✋</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Activity 5: Blindfolded Sensory Feel &amp; Shine Tester</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Sensory Physics</span>
    </div>

    <p class="text-xs text-slate-300">Touch and examine four items sitting at the same room temperature—discover why steel feels cold while wood feels warm!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="feelObject('steel')" id="btn-fl-steel" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">🥄 Steel Spoon</button>
        <button onclick="feelObject('wood')" id="btn-fl-wood" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪵 Wood Block</button>
        <button onclick="feelObject('glass')" id="btn-fl-glass" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🔮 Glass Marble</button>
        <button onclick="feelObject('bark')" id="btn-fl-bark" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🌳 Bark / Chalk</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 sm:grid-cols-3 gap-3 text-center text-xs">
        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <span class="text-slate-400 text-[10px] block">Visual Shine (Lustre):</span>
            <span id="fl-shine" class="font-bold text-cyan-300 text-sm">Bright Shiny Gleam ✨</span>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <span class="text-slate-400 text-[10px] block">Fingertip Surface Feel:</span>
            <span id="fl-texture" class="font-bold text-emerald-300 text-sm">Ultra Smooth Surface</span>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <span class="text-slate-400 text-[10px] block">Thermal Touch Sensation:</span>
            <span id="fl-temp" class="font-bold text-sky-300 text-sm">Feels Cold (Draws Finger Heat!)</span>
        </div>
    </div>
</div>

<script>
function feelObject(obj) {
    const map = {
        steel: { s: 'Bright Shiny Gleam ✨', tx: 'Ultra Smooth Surface', tm: 'Feels Cold (Draws Finger Heat!)' },
        wood: { s: 'Matte Warm Wood Grain', tx: 'Smooth-Sanded or Mildly Grainy', tm: 'Feels Warm (Insulates Finger Heat!)' },
        glass: { s: 'Glassy Crystal Shine ✨', tx: 'Slick Ice-Like Smoothness', tm: 'Moderately Cool to Touch' },
        bark: { s: 'Completely Dull Matte Surface', tx: 'Rough Bumpy / Powdery Feel', tm: 'Neutral / Dry Room Feel' }
    };
    const d = map[obj];
    if (!d) return;

    ['steel', 'wood', 'glass', 'bark'].forEach(k => {
        const b = document.getElementById('btn-fl-' + k);
        if (b) {
            b.className = (k === obj)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('fl-shine').textContent = d.s;
    document.getElementById('fl-texture').textContent = d.tx;
    document.getElementById('fl-temp').textContent = d.tm;
}
</script>
"""

if __name__ == "__main__":
    print(f"Generated {len(simulators_part1)} simulators for Part 1 (1 to 8).")
    for k in sorted(simulators_part1.keys()):
        print(f"Sim {k}: {len(simulators_part1[k])} chars")
