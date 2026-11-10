#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 12: Taking Charge of Waste
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Everyday Waste
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🗑️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Daily Home &amp; School Waste Detective</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Waste Sources</span>
    </div>

    <p class="text-xs text-slate-300">Click everyday items created around homes and schools to inspect what kind of waste they become and why sorting them matters!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectDailyWaste('peels')" id="btn-dw-peels" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">🍌 Kitchen Peels</button>
        <button onclick="inspectDailyWaste('school')" id="btn-dw-school" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">✏️ Pencil &amp; Paper</button>
        <button onclick="inspectDailyWaste('plastic')" id="btn-dw-plastic" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🥡 Wrappers &amp; Tins</button>
        <button onclick="inspectDailyWaste('battery')" id="btn-dw-battery" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🔋 Dead Batteries</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 175" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Kitchen Peels -->
            <g id="dw-peels-svg">
                <path d="M105,118 Q135,62 185,95 Q160,122 105,118 Z" fill="#facc15" />
                <ellipse cx="205" cy="108" rx="22" ry="15" fill="#fed7aa" />
                <path d="M185,108 L202,95 L220,108" stroke="#f97316" stroke-width="2" fill="none" />
                <text x="160" y="46" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">NATURAL WET ORGANIC WASTE</text>
            </g>
            <!-- Pencil & Paper -->
            <g id="dw-school-svg" class="hidden">
                <rect x="85" y="55" width="70" height="82" fill="#e2e8f0" rx="4" />
                <line x1="95" y1="75" x2="145" y2="75" stroke="#94a3b8" stroke-width="2" />
                <line x1="95" y1="95" x2="145" y2="95" stroke="#94a3b8" stroke-width="2" />
                <path d="M175,115 Q205,72 235,115 Q205,128 175,115 Z" fill="#d97706" />
                <text x="160" y="38" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">SHAVINGS &amp; TORN PAPER</text>
            </g>
            <!-- Wrappers & Tins -->
            <g id="dw-plastic-svg" class="hidden">
                <rect x="80" y="70" width="75" height="50" rx="5" fill="#ec4899" />
                <text x="117" y="100" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">CHIPS</text>
                <rect x="180" y="65" width="48" height="62" rx="6" fill="#94a3b8" />
                <line x1="180" y1="85" x2="228" y2="85" stroke="#64748b" stroke-width="2" />
                <line x1="180" y1="105" x2="228" y2="105" stroke="#64748b" stroke-width="2" />
                <text x="160" y="42" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">PERSISTENT WRAPPERS &amp; TINS</text>
            </g>
            <!-- Dead Batteries -->
            <g id="dw-battery-svg" class="hidden">
                <rect x="120" y="62" width="80" height="45" rx="6" fill="#dc2626" />
                <rect x="200" y="75" width="10" height="19" rx="2" fill="#cbd5e1" />
                <text x="160" y="90" fill="#fde047" font-size="16" font-weight="bold" text-anchor="middle">+   -</text>
                <text x="160" y="40" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">HAZARDOUS E-WASTE (TOXIC)</text>
            </g>
            <text x="160" y="160" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle" id="dw-svg-lbl">Banana peels, onion skins &amp; eggshells turn softly into soil food!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-emerald-300 text-sm" id="dw-title">Wet Kitchen Fruit &amp; Vegetable Peels</h4>
            <p class="text-slate-300 leading-relaxed" id="dw-desc">Daily kitchen chores drop fresh vegetable trimmings, fruit skins, tea leaves, and eggshells. Sorted cleanly away from plastic, these become healthy plant compost!</p>
        </div>
    </div>
</div>

<script>
function inspectDailyWaste(item) {
    const map = {
        peels: { lbl: 'Banana peels, onion skins & eggshells turn softly into soil food!', t: 'Wet Kitchen Fruit & Vegetable Peels', d: 'Daily kitchen chores drop fresh vegetable trimmings, fruit skins, tea leaves, and eggshells. Sorted cleanly away from plastic, these become healthy plant compost!' },
        school: { lbl: 'Pencil shavings & dry scrap sheets should never pile up on classroom floors!', t: 'Classroom Shavings & Scrap Paper', d: 'Sharpening wooden pencils and finishing old notebooks fill desks daily. Use clean blank backs for maths practice, then place scrap paper in dry blue bins!' },
        plastic: { lbl: 'Plastic wrappers & old metal tins never rot away quickly outdoors!', t: 'Plastic Wrappers, Bottles & Old Metal Tins', d: 'Snack packets, crushed bottles, worn clothes, and empty metal cans pile fast if dropped outdoors. Rinse clean recyclables into dry blue bins or reduce packaging first!' },
        battery: { lbl: 'Toxic battery chemicals must stay strictly away from soil and fires!', t: 'Old Dead Torch & Toy Batteries', d: 'Exhausted batteries hold heavy metals and acidic paste that leak poison into gardens and water. Collect dead batteries safely inside dedicated e-waste drop boxes!' }
    };
    const d = map[item];
    if (!d) return;
    ['peels', 'school', 'plastic', 'battery'].forEach(k => {
        const b = document.getElementById('btn-dw-' + k);
        if (b) {
            b.className = (k === item)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('dw-' + k + '-svg');
        if (g) {
            if (k === item) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('dw-svg-lbl').textContent = d.lbl;
    document.getElementById('dw-title').textContent = d.t;
    document.getElementById('dw-desc').textContent = d.d;
}
</script>
"""

# Simulator 2: Garbage Heaps
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⏳</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Garbage Pile Breakdown &amp; Drain Hazard Lab</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Time Comparison</span>
    </div>

    <p class="text-xs text-slate-300">Compare what happens after 6 months when organic leaves sit outdoors versus unmanaged plastic bags, tins, and leaking batteries!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="setHeapTime('leaves')" id="btn-hp-leaves" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">🍂 Fallen Leaves</button>
        <button onclick="setHeapTime('drains')" id="btn-hp-drains" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🛍️ Plastic In Drains</button>
        <button onclick="setHeapTime('leaks')" id="btn-hp-leaks" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧪 Toxic Heap Leaks</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 175" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Fallen Leaves -->
            <g id="hp-leaves-svg">
                <rect x="60" y="110" width="200" height="32" rx="6" fill="#451a03" />
                <ellipse cx="160" cy="108" rx="55" ry="15" fill="#78350f" />
                <path d="M160,92 L160,55" stroke="#22c55e" stroke-width="4" />
                <ellipse cx="148" cy="60" rx="10" ry="5" fill="#22c55e" />
                <ellipse cx="172" cy="60" rx="10" ry="5" fill="#22c55e" />
                <text x="160" y="38" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">ROTS CLEANLY IN WEEKS -> PLANT SOIL!</text>
            </g>
            <!-- Choked Drain -->
            <g id="hp-drains-svg" class="hidden">
                <rect x="40" y="95" width="240" height="45" fill="#0284c7" opacity="0.55" />
                <rect x="135" y="75" width="50" height="65" fill="#475569" />
                <path d="M120,102 L195,92 L185,120 L125,122 Z" fill="#ec4899" />
                <text x="160" y="45" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">PLASTIC CHOKES DRAIN -> DIRTY FLOODS!</text>
            </g>
            <!-- Toxic Leaks -->
            <g id="hp-leaks-svg" class="hidden">
                <polygon points="80,120 155,60 240,120" fill="#64748b" />
                <rect x="140" y="90" width="32" height="18" fill="#dc2626" />
                <path d="M156,108 L156,142" stroke="#a3e635" stroke-width="5" stroke-dasharray="4,2" />
                <text x="160" y="38" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">POISONOUS JUICE SEEPS INTO GROUNDWATER!</text>
            </g>
            <text x="160" y="162" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle" id="hp-svg-lbl">Soil worms convert natural fallen leaves cleanly into healthy dark soil!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-amber-300 text-sm" id="hp-title">Natural Leaf Biodegradation (Fast &amp; Safe)</h4>
            <p class="text-slate-300 leading-relaxed" id="hp-desc">Dry leaves and fresh vegetable peels decompose swiftly via microbes and earthworms into rich dark soil food, feeding vibrant green saplings safely!</p>
        </div>
    </div>
</div>

<script>
function setHeapTime(mode) {
    const map = {
        leaves: { lbl: 'Soil worms convert natural fallen leaves cleanly into healthy dark soil!', t: 'Natural Leaf Biodegradation (Fast & Safe)', d: 'Dry leaves and fresh vegetable peels decompose swiftly via microbes and earthworms into rich dark soil food, feeding vibrant green saplings safely!' },
        drains: { lbl: 'Synthetic plastics linger for centuries choking gutters & drains!', t: 'Non-Rotting Plastic Bags Blocking Drains', d: 'Unlike leaves, shiny plastic wrappers never rot swiftly in nature. Wind carries light bags into roadside grilles, backing up foul rainwater onto neighborhood streets!' },
        leaks: { lbl: 'Mixed batteries & rotting trash leak poison straight downward into wells!', t: 'Toxic Leachate & Shattered Glass Hazards', d: 'When dead batteries, broken glass, and rotting food pile together outdoors, rain washes toxic black liquids straight down into underground drinking water!' }
    };
    const d = map[mode];
    if (!d) return;
    ['leaves', 'drains', 'leaks'].forEach(k => {
        const b = document.getElementById('btn-hp-' + k);
        if (b) {
            b.className = (k === mode)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('hp-' + k + '-svg');
        if (g) {
            if (k === mode) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('hp-svg-lbl').textContent = d.lbl;
    document.getElementById('hp-title').textContent = d.t;
    document.getElementById('hp-desc').textContent = d.d;
}
</script>
"""

# Simulator 3: Danger To Animals
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🐄</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Protecting Stray Animals From Plastic Ingestion</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Animal Welfare</span>
    </div>

    <p class="text-xs text-slate-300">Compare tossing food inside knotted plastic carry bags against placing loose vegetable scraps inside green compost bins!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="setAnimalSafety('danger')" id="btn-as-danger" class="p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">❌ Food Inside Plastic Bag</button>
        <button onclick="setAnimalSafety('safe')" id="btn-as-safe" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">✅ Loose Compost + Cloth Bag</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 175" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Stylized Cow Silhouette -->
            <ellipse cx="145" cy="95" rx="48" ry="28" fill="#cbd5e1" />
            <circle cx="92" cy="80" r="18" fill="#e2e8f0" />
            <rect x="108" y="112" width="10" height="32" fill="#94a3b8" />
            <rect x="172" y="112" width="10" height="32" fill="#94a3b8" />
            <!-- Danger State -->
            <g id="as-danger-svg">
                <circle cx="148" cy="95" r="14" fill="#ef4444" opacity="0.85" />
                <text x="148" y="99" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">KNOT</text>
                <polygon points="215,120 250,98 265,128" fill="#ec4899" />
                <text x="160" y="38" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">SWALLOWED PLASTIC BLOCKS COW STOMACH!</text>
            </g>
            <!-- Safe State -->
            <g id="as-safe-svg" class="hidden">
                <rect x="215" y="95" width="42" height="48" rx="4" fill="#16a34a" />
                <text x="236" y="122" fill="#fff" font-size="8" font-weight="bold" text-anchor="middle">COMPOST</text>
                <text x="160" y="38" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">LOOSE SCRAPS IN BIN — ANIMALS STAY SAFE!</text>
            </g>
            <text x="160" y="162" fill="#fda4af" font-size="10" font-weight="bold" text-anchor="middle" id="as-svg-lbl">Hungry cows swallow knotted plastic sheets chasing food smells!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-rose-300 text-sm" id="as-title">Hazardous Knotted Plastic Food Bundles</h4>
            <p class="text-slate-300 leading-relaxed" id="as-desc">Unable to untie tight plastic knots with hooves, hungry cows, goats, and street dogs rip and swallow indigestible plastic sheets right alongside smells of vegetable scraps, causing painful fatal blockages!</p>
        </div>
    </div>
</div>

<script>
function setAnimalSafety(mode) {
    const map = {
        danger: { lbl: 'Hungry cows swallow knotted plastic sheets chasing food smells!', t: 'Hazardous Knotted Plastic Food Bundles', d: 'Unable to untie tight plastic knots with hooves, hungry cows, goats, and street dogs rip and swallow indigestible plastic sheets right alongside smells of vegetable scraps, causing painful fatal blockages!' },
        safe: { lbl: 'Covered green bins & cloth shopping totes save street animals daily!', t: 'Safe Composting & Cloth Tote Habits', d: 'Dropping loose kitchen peels strictly into covered green compost bins while carrying washable cloth bags keeps plastic bags completely out of street animal feeding paths!' }
    };
    const d = map[mode];
    if (!d) return;
    ['danger', 'safe'].forEach(k => {
        const b = document.getElementById('btn-as-' + k);
        if (b) {
            b.className = (k === mode)
                ? 'p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('as-' + k + '-svg');
        if (g) {
            if (k === mode) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('as-svg-lbl').textContent = d.lbl;
    document.getElementById('as-title').textContent = d.t;
    document.getElementById('as-desc').textContent = d.d;
}
</script>
"""

# Simulator 4: Burning Plastic Smoke
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">💨</span>
            <h3 class="text-sm sm:text-base font-bold text-slate-200">Burning Rubbish vs. Smoke-Free Composting</h3>
        </div>
        <span class="text-[11px] bg-slate-800 text-rose-300 px-2.5 py-1 rounded-full border border-slate-700">Air Quality Lab</span>
    </div>

    <p class="text-xs text-slate-300">Compare what happens to breathing air, lungs, and birds when street piles are set ablaze versus sorted cleanly for compost and recycling!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="setSmokeSim('burn')" id="btn-smk-burn" class="p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">🔥 Open Plastic Fire</button>
        <button onclick="setSmokeSim('clean')" id="btn-smk-clean" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🌿 Compost + Recycle</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 175" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Burn -->
            <g id="smk-burn-svg">
                <circle cx="135" cy="70" r="28" fill="#475569" opacity="0.85" />
                <circle cx="170" cy="52" r="34" fill="#334155" opacity="0.85" />
                <circle cx="205" cy="68" r="24" fill="#475569" opacity="0.85" />
                <path d="M125,135 Q160,82 195,135 Z" fill="#f97316" />
                <text x="160" y="34" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">POISONOUS GASES &amp; SOOT CLOUD SKY!</text>
            </g>
            <!-- Clean -->
            <g id="smk-clean-svg" class="hidden">
                <circle cx="265" cy="40" r="18" fill="#fde047" />
                <rect x="80" y="90" width="60" height="50" rx="5" fill="#16a34a" />
                <rect x="180" y="90" width="60" height="50" rx="5" fill="#0284c7" />
                <text x="110" y="120" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">COMPOST</text>
                <text x="210" y="120" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">RECYCLE</text>
                <text x="160" y="36" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">SPARKLING BLUE SKY &amp; PURE LUNGS!</text>
            </g>
            <text x="160" y="162" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle" id="smk-svg-lbl">Burning plastic melts into toxic black fumes irritating eyes &amp; lungs!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-rose-300 text-sm" id="smk-title">Hazardous Toxic Plastic Smoke</h4>
            <p class="text-slate-300 leading-relaxed" id="smk-desc">Setting plastic wrappers and leaves on fire releases invisible poisonous gases and heavy soot particles that cause coughing, trigger asthma attacks, sting eyes, and pollute clean sky air!</p>
        </div>
    </div>
</div>

<script>
function setSmokeSim(mode) {
    const map = {
        burn: { lbl: 'Burning plastic melts into toxic black fumes irritating eyes & lungs!', t: 'Hazardous Toxic Plastic Smoke', d: 'Setting plastic wrappers and leaves on fire releases invisible poisonous gases and heavy soot particles that cause coughing, trigger asthma attacks, sting eyes, and pollute clean sky air!' },
        clean: { lbl: 'Composting crisp leaves & recycling plastic keeps sky air crisp & clear!', t: 'Zero-Fire Leaf Compost & Dry Recycling', d: 'Burying dry garden leaves inside compost pits produces rich plant manure cleanly while dry plastic goes to recycling factories—leaving zero smoke anywhere!' }
    };
    const d = map[mode];
    if (!d) return;
    ['burn', 'clean'].forEach(k => {
        const b = document.getElementById('btn-smk-' + k);
        if (b) {
            b.className = (k === mode)
                ? 'p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('smk-' + k + '-svg');
        if (g) {
            if (k === mode) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('smk-svg-lbl').textContent = d.lbl;
    document.getElementById('smk-title').textContent = d.t;
    document.getElementById('smk-desc').textContent = d.d;
}
</script>
"""

# Simulator 5: Stagnant Water Danger
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🦟</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Eliminate Mosquito Stagnant Water Puddles</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="mosq-count-badge">3 Hazards Active</span>
    </div>

    <p class="text-xs text-slate-300">Click each backyard water trap below to tip standing puddles dry or clear clogged drains cleanly before mosquitoes hatch!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="clearMosqTrap('tire')" id="btn-mq-tire" class="p-2.5 rounded-xl bg-rose-900/60 text-rose-200 font-bold text-xs border border-rose-700 hover:bg-rose-800">🛞 Empty Old Tire</button>
        <button onclick="clearMosqTrap('can')" id="btn-mq-can" class="p-2.5 rounded-xl bg-rose-900/60 text-rose-200 font-bold text-xs border border-rose-700 hover:bg-rose-800">🥫 Remove Rusty Tin</button>
        <button onclick="clearMosqTrap('gutter')" id="btn-mq-gutter" class="p-2.5 rounded-xl bg-rose-900/60 text-rose-200 font-bold text-xs border border-rose-700 hover:bg-rose-800">🌊 Unblock Gutter</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 170" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Tire -->
            <g id="mq-tire-bad">
                <circle cx="70" cy="90" r="28" fill="none" stroke="#475569" stroke-width="12" />
                <ellipse cx="70" cy="100" rx="16" ry="7" fill="#0ea5e9" />
            </g>
            <g id="mq-tire-ok" class="hidden">
                <circle cx="70" cy="90" r="26" fill="none" stroke="#22c55e" stroke-width="3" />
                <text x="70" y="94" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">DRY</text>
            </g>
            <!-- Tin -->
            <g id="mq-can-bad">
                <rect x="140" y="65" width="40" height="50" fill="#94a3b8" />
                <rect x="142" y="72" width="36" height="15" fill="#0ea5e9" />
            </g>
            <g id="mq-can-ok" class="hidden">
                <rect x="140" y="65" width="40" height="50" rx="4" fill="none" stroke="#22c55e" stroke-width="3" />
                <text x="160" y="94" fill="#4ade80" font-size="10" font-weight="bold" text-anchor="middle">CLEANED</text>
            </g>
            <!-- Gutter -->
            <g id="mq-gutter-bad">
                <rect x="215" y="70" width="75" height="40" fill="#0284c7" opacity="0.6" />
                <circle cx="252" cy="90" r="10" fill="#ec4899" />
            </g>
            <g id="mq-gutter-ok" class="hidden">
                <rect x="215" y="70" width="75" height="40" fill="#0f172a" stroke="#22c55e" stroke-width="2" />
                <text x="252" y="94" fill="#4ade80" font-size="10" font-weight="bold" text-anchor="middle">FLOWING</text>
            </g>
            <text x="160" y="150" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle" id="mq-svg-lbl">Tap all 3 stagnant rainwater traps above to wipe out mosquitoes!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-cyan-300 text-sm" id="mq-title">Check Yard Corners Weekly</h4>
            <p class="text-slate-300 leading-relaxed" id="mq-desc">Calm standing rainwater inside discarded tires, empty open cans, flower trays, and plastic-choked drains lets dengue &amp; malaria mosquitoes lay hundreds of eggs effortlessly!</p>
        </div>
    </div>
</div>

<script>
window.clearedMq = { tire: false, can: false, gutter: false };
function clearMosqTrap(id) {
    window.clearedMq[id] = true;
    const bad = document.getElementById('mq-' + id + '-bad');
    const ok = document.getElementById('mq-' + id + '-ok');
    if (bad) bad.classList.add('hidden');
    if (ok) ok.classList.remove('hidden');
    const btn = document.getElementById('btn-mq-' + id);
    if (btn) {
        btn.className = 'p-2.5 rounded-xl bg-emerald-700 text-white font-bold text-xs border border-emerald-500';
        btn.textContent = '✅ Cleared!';
    }
    const left = Object.values(window.clearedMq).filter(v => !v).length;
    const badge = document.getElementById('mosq-count-badge');
    if (badge) badge.textContent = left === 0 ? 'All Clear!' : `${left} Hazards Left`;
    if (left === 0) {
        document.getElementById('mq-svg-lbl').textContent = 'Zero standing water — mosquitoes cannot breed around home!';
        document.getElementById('mq-title').textContent = '100% Mosquito-Safe Courtyard!';
        document.getElementById('mq-desc').textContent = 'Every stagnant puddle has been drained cleanly! Without quiet trapped rainwater, mosquito larvae cannot survive cleanly around homes or schools.';
    }
}
</script>
"""

# Simulator 6: First Rule Reduce
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🛍️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">First Rule REDUCE: Smart Market Basket Lab</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Stop Trash Early</span>
    </div>

    <p class="text-xs text-slate-300">Compare filling a heavily wrapped disposable shopping basket against picking unpackaged fresh goods inside a washable cloth bag!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="setReduceCart('heavy')" id="btn-rd-heavy" class="p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">🥡 Heavily Packaged Cart</button>
        <button onclick="setReduceCart('smart')" id="btn-rd-smart" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🌿 Unpackaged + Cloth Bag</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 170" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Heavy Packaging -->
            <g id="rd-heavy-svg">
                <rect x="65" y="55" width="55" height="65" rx="4" fill="#ec4899" />
                <rect x="130" y="50" width="55" height="70" rx="4" fill="#f97316" />
                <rect x="195" y="60" width="55" height="60" rx="4" fill="#a855f7" />
                <text x="160" y="38" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">HIGH PLASTIC WASTE (6 BAGS + WRAPPERS)</text>
            </g>
            <!-- Smart Cloth Bag -->
            <g id="rd-smart-svg" class="hidden">
                <path d="M125,65 Q160,30 195,65" fill="none" stroke="#22c55e" stroke-width="5" />
                <rect x="115" y="65" width="90" height="68" rx="6" fill="#16a34a" />
                <circle cx="145" cy="60" r="11" fill="#ef4444" />
                <circle cx="172" cy="58" r="11" fill="#facc15" />
                <text x="160" y="103" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">CLOTH TOTE</text>
                <text x="160" y="28" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">ZERO SINGLE-USE PLASTIC TRASH!</text>
            </g>
            <text x="160" y="154" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle" id="rd-svg-lbl">Five mini packets + double carry bags create instant street rubbish!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-emerald-300 text-sm" id="rd-title">High-Packaging Disposable Shopping</h4>
            <p class="text-slate-300 leading-relaxed" id="rd-desc">Individual single-serve snack packets and extra plastic shop handles produce bulky wrappers that litter drains minutes after snacking!</p>
        </div>
    </div>
</div>

<script>
function setReduceCart(kind) {
    const map = {
        heavy: { lbl: 'Five mini packets + double carry bags create instant street rubbish!', t: 'High-Packaging Disposable Shopping', d: 'Individual single-serve snack packets and extra plastic shop handles produce bulky wrappers that litter drains minutes after snacking!' },
        smart: { lbl: 'Cloth bags & fresh loose foods shrink waste right at the checkout!', t: 'Eco-Smart REDUCE Shopping Basket', d: 'Bringing your own folded cloth tote and buying fresh unpackaged bananas, nuts, or apples keeps dozens of stubborn plastic wrappers off planet Earth!' }
    };
    const d = map[kind];
    if (!d) return;
    ['heavy', 'smart'].forEach(k => {
        const b = document.getElementById('btn-rd-' + k);
        if (b) {
            b.className = (k === kind)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('rd-' + k + '-svg');
        if (g) {
            if (k === kind) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('rd-svg-lbl').textContent = d.lbl;
    document.getElementById('rd-title').textContent = d.t;
    document.getElementById('rd-desc').textContent = d.d;
}
</script>
"""

# Simulator 7: Sharing Old Things
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📚</span>
            <h3 class="text-sm sm:text-base font-bold text-sky-300">Share-and-Care Book &amp; Toy Shelf</h3>
        </div>
        <span class="text-[11px] bg-sky-950/80 text-sky-300 px-2.5 py-1 rounded-full border border-sky-800">Kind Sharing</span>
    </div>

    <p class="text-xs text-slate-300">Select neat outgrown belongings to pass them lovingly onward through school book banks instead of letting good items hit garbage heaps!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="inspectShare('books')" id="btn-sh-books" class="p-2.5 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500">📖 Storybooks</button>
        <button onclick="inspectShare('toys')" id="btn-sh-toys" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧩 Wooden Toys</button>
        <button onclick="inspectShare('coats')" id="btn-sh-coats" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧥 Warm Coats</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 170" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Books -->
            <g id="sh-books-svg">
                <rect x="85" y="75" width="150" height="22" rx="3" fill="#2563eb" />
                <rect x="95" y="52" width="130" height="22" rx="3" fill="#16a34a" />
                <rect x="105" y="30" width="110" height="21" rx="3" fill="#f59e0b" />
                <text x="160" y="128" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">SCHOOL BOOK BANK = SAVES FOREST TREES!</text>
            </g>
            <!-- Toys -->
            <g id="sh-toys-svg" class="hidden">
                <circle cx="115" cy="95" r="22" fill="#ef4444" />
                <rect x="145" y="68" width="55" height="55" rx="6" fill="#eab308" />
                <polygon points="225,120 245,68 265,120" fill="#22c55e" />
                <text x="160" y="42" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">CLEAN TOYS SPARK FRESH SMILES!</text>
            </g>
            <!-- Coats -->
            <g id="sh-coats-svg" class="hidden">
                <polygon points="105,52 140,42 160,55 180,42 215,52 225,115 95,115" fill="#9333ea" />
                <text x="160" y="138" fill="#d8b4fe" font-size="11" font-weight="bold" text-anchor="middle">OUTGROWN CLEAN SWEATERS KEEP OTHERS WARM!</text>
            </g>
            <text x="160" y="160" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle" id="sh-svg-lbl">Next-year Class 2 readers welcome clean picture books joyfully!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-sky-300 text-sm" id="sh-title">Clean Storybooks &amp; School Textbooks</h4>
            <p class="text-slate-300 leading-relaxed" id="sh-desc">Passing crisp storybooks and neat Class 3 textbooks onward through school Share-and-Care book banks cuts paper demand, saves tall trees, and delights incoming younger learners!</p>
        </div>
    </div>
</div>

<script>
function inspectShare(item) {
    const map = {
        books: { lbl: 'Next-year Class 2 readers welcome clean picture books joyfully!', t: 'Clean Storybooks & School Textbooks', d: 'Passing crisp storybooks and neat Class 3 textbooks onward through school Share-and-Care book banks cuts paper demand, saves tall trees, and delights incoming younger learners!' },
        toys: { lbl: 'Complete wooden blocks & board games brighten younger kids!', t: 'Sturdy Outgrown Toys & Puzzles', d: 'Donating whole wooden puzzles, chess boards, and clean dolls keeps long-lasting toys out of dumps while inspiring playful learning elsewhere!' },
        coats: { lbl: 'Neat washed sweaters give warm winter comfort cleanly!', t: 'Outgrown Sweaters, Shoes & Uniforms', d: 'Children grow fast every year! Sharing freshly washed snug uniforms and warm coats helps neighboring families while reducing textile piles.' }
    };
    const d = map[item];
    if (!d) return;
    ['books', 'toys', 'coats'].forEach(k => {
        const b = document.getElementById('btn-sh-' + k);
        if (b) {
            b.className = (k === item)
                ? 'p-2.5 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('sh-' + k + '-svg');
        if (g) {
            if (k === item) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('sh-svg-lbl').textContent = d.lbl;
    document.getElementById('sh-title').textContent = d.t;
    document.getElementById('sh-desc').textContent = d.d;
}
</script>
"""

# Simulator 8: Second Rule Reuse
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🫙</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Second Rule REUSE: Creative Container Upcycler</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Kitchen Upcycling</span>
    </div>

    <p class="text-xs text-slate-300">Give sturdy empty kitchen containers bright creative second jobs instead of letting useful glass, tin, and terracotta land inside rubbish bins!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="reuseContainer('jar')" id="btn-ru-jar" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">🫙 Glass Jam Jar</button>
        <button onclick="reuseContainer('tin')" id="btn-ru-tin" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🥫 Biscuit Tin Box</button>
        <button onclick="reuseContainer('pot')" id="btn-ru-pot" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪴 Chipped Clay Cup</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 170" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Glass Jar -->
            <g id="ru-jar-svg">
                <rect x="125" y="55" width="70" height="82" rx="10" fill="#0ea5e9" opacity="0.35" stroke="#7dd3fc" stroke-width="3" />
                <rect x="132" y="42" width="56" height="14" rx="3" fill="#dc2626" />
                <circle cx="148" cy="112" r="6" fill="#fde047" /><circle cx="165" cy="116" r="6" fill="#22c55e" /><circle cx="172" cy="100" r="6" fill="#f97316" />
                <text x="160" y="28" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">SPICES, PENCILS OR BUTTONS ORGANIZER!</text>
            </g>
            <!-- Biscuit Tin -->
            <g id="ru-tin-svg" class="hidden">
                <rect x="95" y="65" width="130" height="65" rx="6" fill="#d97706" stroke="#fde047" stroke-width="2" />
                <text x="160" y="102" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">SEWING &amp; CRAFT KIT</text>
                <text x="160" y="38" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">RUST-FREE ART TREASURE BOX!</text>
            </g>
            <!-- Chipped Clay Cup -->
            <g id="ru-pot-svg" class="hidden">
                <polygon points="125,85 195,85 182,135 138,135" fill="#b45309" />
                <path d="M160,85 L160,42 M160,65 L142,50 M160,62 L178,48" stroke="#22c55e" stroke-width="3" fill="none" />
                <circle cx="140" cy="48" r="8" fill="#22c55e" /><circle cx="180" cy="46" r="8" fill="#22c55e" />
                <text x="160" y="28" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">FRESH BALCONY MINT HERB PLANTER!</text>
            </g>
            <text x="160" y="160" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle" id="ru-svg-lbl">Clear washed jars reveal spices and crayons neatly inside kitchen shelves!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-amber-300 text-sm" id="ru-title">Washed Clear Glass Jam Jar</h4>
            <p class="text-slate-300 leading-relaxed" id="ru-desc">Sturdy washed glass jars with tight lids store spices cleanly, keep dampness out of lentils, or showcase shiny crayons on study desks without buying extra plastic tubs!</p>
        </div>
    </div>
</div>

<script>
function reuseContainer(type) {
    const map = {
        jar: { lbl: 'Clear washed jars reveal spices and crayons neatly inside kitchen shelves!', t: 'Washed Clear Glass Jam Jar', d: 'Sturdy washed glass jars with tight lids store spices cleanly, keep dampness out of lentils, or showcase shiny crayons on study desks without buying extra plastic tubs!' },
        tin: { lbl: 'Strong metal cookie tins guard needles, marbles & crayons neatly!', t: 'Metal Biscuit Tin -> Craft Treasure Chest', d: 'Durable tin biscuit boxes protect sewing needles, buttons, brushes, and marbles cleanly indoors instead of sitting wasted inside scrap piles.' },
        pot: { lbl: 'Chipped cups sprout lush kitchen mint & coriander leaves beautifully!', t: 'Chipped Terracotta Cup -> Herb Planter', d: 'Cracked or chipped clay cups become charming windowsill herb gardens for fragrant kitchen mint or coriander leaves!' }
    };
    const d = map[type];
    if (!d) return;
    ['jar', 'tin', 'pot'].forEach(k => {
        const b = document.getElementById('btn-ru-' + k);
        if (b) {
            b.className = (k === type)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('ru-' + k + '-svg');
        if (g) {
            if (k === type) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('ru-svg-lbl').textContent = d.lbl;
    document.getElementById('ru-title').textContent = d.t;
    document.getElementById('ru-desc').textContent = d.d;
}
</script>
"""
