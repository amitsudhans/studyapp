#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 12: Taking Charge of Waste
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Cloth Quilts Bags
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧵</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Old Clothes Sewing &amp; Upcycling Studio</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">Textile Reuse</span>
    </div>

    <p class="text-xs text-slate-300">Select old worn cotton sarees, sturdy jeans, or border cloth scraps to transform textile waste into useful cozy household treasures!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="upcycleCloth('quilt')" id="btn-cl-quilt" class="p-2.5 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">🛏️ Patchwork Quilt</button>
        <button onclick="upcycleCloth('tote')" id="btn-cl-tote" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">👜 Denim Tote Bag</button>
        <button onclick="upcycleCloth('mat')" id="btn-cl-mat" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">⭕ Braided Floor Mat</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 170" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Quilt -->
            <g id="cl-quilt-svg">
                <rect x="75" y="45" width="55" height="45" fill="#ec4899" stroke="#fef3c7" />
                <rect x="130" y="45" width="55" height="45" fill="#f59e0b" stroke="#fef3c7" />
                <rect x="185" y="45" width="55" height="45" fill="#10b981" stroke="#fef3c7" />
                <rect x="75" y="90" width="55" height="45" fill="#3b82f6" stroke="#fef3c7" />
                <rect x="130" y="90" width="55" height="45" fill="#a855f7" stroke="#fef3c7" />
                <rect x="185" y="90" width="55" height="45" fill="#ef4444" stroke="#fef3c7" />
            </g>
            <!-- Tote Bag -->
            <g id="cl-tote-svg" class="hidden">
                <path d="M130,65 Q160,32 190,65" fill="none" stroke="#60a5fa" stroke-width="5" />
                <rect x="115" y="65" width="90" height="72" rx="6" fill="#1d4ed8" stroke="#93c5fd" stroke-width="2" />
                <text x="160" y="106" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">DENIM TOTE</text>
            </g>
            <!-- Braided Floor Mat -->
            <g id="cl-mat-svg" class="hidden">
                <ellipse cx="160" cy="92" rx="75" ry="42" fill="#f97316" />
                <ellipse cx="160" cy="92" rx="52" ry="28" fill="#14b8a6" />
                <ellipse cx="160" cy="92" rx="28" ry="15" fill="#fde047" />
            </g>
            <text x="160" y="158" fill="#d8b4fe" font-size="10" font-weight="bold" text-anchor="middle" id="cl-svg-lbl">Soft worn cotton saree layers stitch cleanly into warm patchwork gudris!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-purple-300 text-sm" id="cl-title">Warm Layered Patchwork Quilt (Gudri)</h4>
            <p class="text-slate-300 leading-relaxed" id="cl-desc">Old soft cotton clothes and faded sarees are washed clean, layered gently together, and hand-stitched into cozy breathable patchwork quilts keeping families warm for years!</p>
        </div>
    </div>
</div>

<script>
function upcycleCloth(kind) {
    const map = {
        quilt: { lbl: 'Soft worn cotton saree layers stitch cleanly into warm patchwork gudris!', t: 'Warm Layered Patchwork Quilt (Gudri)', d: 'Old soft cotton clothes and faded sarees are washed clean, layered gently together, and hand-stitched into cozy breathable patchwork quilts keeping families warm for years!' },
        tote: { lbl: 'Rugged denim jeans sew swiftly into washable heavy grocery market bags!', t: 'Strong Stitched Shopping Tote Bag', d: 'Worn jeans and stout cotton curtains sew cleanly into rugged market bags carrying heavy potatoes and greens without tearing—replacing hundreds of plastic carry bags!' },
        mat: { lbl: 'Trimmed colorful fabric strips braid tightly into soft doorway mats!', t: 'Colorful Braided Cloth Doormat', d: 'Narrow border ribbons braided in concentric circles become cozy washable bedroom rugs and kitchen pot holders instead of textile waste!' }
    };
    const d = map[kind];
    if (!d) return;
    ['quilt', 'tote', 'mat'].forEach(k => {
        const b = document.getElementById('btn-cl-' + k);
        if (b) {
            b.className = (k === kind)
                ? 'p-2.5 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('cl-' + k + '-svg');
        if (g) {
            if (k === kind) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('cl-svg-lbl').textContent = d.lbl;
    document.getElementById('cl-title').textContent = d.t;
    document.getElementById('cl-desc').textContent = d.d;
}
</script>
"""

# Simulator 10: Paper And Bottles
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🍶</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Smart Paper Reuse &amp; Metal Bottle Station</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Daily Habits</span>
    </div>

    <p class="text-xs text-slate-300">Explore four simple Class 3 reuse habits saving thousands of plastic bottles, shiny gift wraps, and crisp notebooks annually!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectReuseHabit('gift')" id="btn-rh-gift" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">🎁 Newspaper Wrap</button>
        <button onclick="inspectReuseHabit('back')" id="btn-rh-back" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">📝 Back-Page Pad</button>
        <button onclick="inspectReuseHabit('bag')" id="btn-rh-bag" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🛍️ Paper Bag</button>
        <button onclick="inspectReuseHabit('steel')" id="btn-rh-steel" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🍶 Steel Bottle</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 170" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Gift -->
            <g id="rh-gift-svg">
                <rect x="115" y="60" width="90" height="70" fill="#cbd5e1" stroke="#475569" stroke-width="2" />
                <rect x="155" y="60" width="10" height="70" fill="#ef4444" />
                <rect x="115" y="90" width="90" height="10" fill="#ef4444" />
                <text x="160" y="38" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">COMIC NEWSPAPER + CLOTH RIBBON WRAP!</text>
            </g>
            <!-- Back-Page -->
            <g id="rh-back-svg" class="hidden">
                <rect x="110" y="45" width="100" height="88" fill="#f8fafc" rx="4" />
                <text x="160" y="78" fill="#0284c7" font-size="14" font-weight="bold" text-anchor="middle">24 + 18 = 42</text>
                <text x="160" y="102" fill="#475569" font-size="10" text-anchor="middle">Blank Back Rough Sheet!</text>
            </g>
            <!-- Paper Bag -->
            <g id="rh-bag-svg" class="hidden">
                <rect x="115" y="60" width="90" height="75" fill="#94a3b8" stroke="#e2e8f0" stroke-width="2" />
                <path d="M140,60 Q160,38 180,60" fill="none" stroke="#f59e0b" stroke-width="4" />
                <text x="160" y="102" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">FOLDED PAPER BAG</text>
            </g>
            <!-- Steel Bottle -->
            <g id="rh-steel-svg" class="hidden">
                <rect x="138" y="48" width="44" height="88" rx="10" fill="#94a3b8" stroke="#f8fafc" stroke-width="2" />
                <rect x="148" y="36" width="24" height="12" rx="3" fill="#475569" />
                <text x="160" y="95" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">STEEL</text>
            </g>
            <text x="160" y="158" fill="#7dd3fc" font-size="10" font-weight="bold" text-anchor="middle" id="rh-svg-lbl">Colorful newspapers &amp; cotton kerchiefs wrap birthday boxes zero-waste!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-cyan-300 text-sm" id="rh-title">Newspaper &amp; Fabric Gift Wrapping</h4>
            <p class="text-slate-300 leading-relaxed" id="rh-desc">Replacing shiny single-use plastic gift foils with cheerful comic newspapers or washable cotton kerchiefs creates delightful eco-friendly gifts leaving zero shiny plastic litter!</p>
        </div>
    </div>
</div>

<script>
function inspectReuseHabit(habit) {
    const map = {
        gift: { lbl: 'Colorful newspapers & cotton kerchiefs wrap birthday boxes zero-waste!', t: 'Newspaper & Fabric Gift Wrapping', d: 'Replacing shiny single-use plastic gift foils with cheerful comic newspapers or washable cotton kerchiefs creates delightful eco-friendly gifts leaving zero shiny plastic litter!' },
        back: { lbl: 'Clean reverse pages double paper utility for maths & drawings!', t: 'Single-Sided Paper -> Rough Work Pads', d: 'Gather printed notices with blank clean backs into rough practice pads so every single sheet works twice before going to dry blue paper recycling!' },
        bag: { lbl: 'Folded newspaper sleeves carry dry groceries cleanly without plastic!', t: 'Handmade Recycled Newspaper Bags', d: 'Folding yesterday newspapers with flour glue creates sturdy crisp shopping bags ideal for fruits, stationery, and dry grains cleanly.' },
        steel: { lbl: 'Refilling 1 durable metal flask avoids 300+ disposable bottles yearly!', t: 'Refillable Steel or Copper Water Bottle', d: 'Carrying a sturdy steel or copper water flask keeps cool drinking water fresh everywhere while preventing mountains of crushed plastic bottle trash!' }
    };
    const d = map[habit];
    if (!d) return;
    ['gift', 'back', 'bag', 'steel'].forEach(k => {
        const b = document.getElementById('btn-rh-' + k);
        if (b) {
            b.className = (k === habit)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('rh-' + k + '-svg');
        if (g) {
            if (k === habit) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('rh-svg-lbl').textContent = d.lbl;
    document.getElementById('rh-title').textContent = d.t;
    document.getElementById('rh-desc').textContent = d.d;
}
</script>
"""

# Simulator 11: Clean Indian Villages
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏡</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">A Place of Pride: Clean Indian Village Models</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Rural Champions</span>
    </div>

    <p class="text-xs text-slate-300">Visit Silluk in Arunachal Pradesh and Chhota Narena in Rajasthan to see how caring communities achieve spotless zero-waste streets!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="inspectVillage('silluk')" id="btn-vil-silluk" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">🎋 Silluk (Arunachal Pradesh)</button>
        <button onclick="inspectVillage('narena')" id="btn-vil-narena" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🏺 Chhota Narena (Rajasthan)</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 170" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Silluk -->
            <g id="vil-silluk-svg">
                <polygon points="65,95 160,35 255,95" fill="#15803d" />
                <rect x="85" y="95" width="150" height="45" fill="#d97706" />
                <polygon points="245,105 275,105 270,138 250,138" fill="#ca8a04" stroke="#fef08a" stroke-width="2" />
                <text x="160" y="26" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">ZERO-WASTE VILLAGE + BAMBOO BINS!</text>
            </g>
            <!-- Chhota Narena -->
            <g id="vil-narena-svg" class="hidden">
                <rect x="75" y="65" width="170" height="72" fill="#f59e0b" />
                <rect x="145" y="98" width="30" height="39" fill="#78350f" />
                <circle cx="55" cy="95" r="18" fill="#22c55e" />
                <circle cx="265" cy="95" r="18" fill="#22c55e" />
                <text x="160" y="38" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">CLEAN SHARED LANES &amp; WATER SPOTS!</text>
            </g>
            <text x="160" y="158" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle" id="vil-svg-lbl">Hand-woven bamboo roadside baskets &amp; composting keep Silluk spotless!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-emerald-300 text-sm" id="vil-title">Silluk — Zero-Waste Village (Arunachal Pradesh)</h4>
            <p class="text-slate-300 leading-relaxed" id="vil-desc">Families weave natural bamboo waste baskets along green streets, compost all kitchen scraps locally, join monthly cleanup drives, and keep every avenue spotless without roadside plastic!</p>
        </div>
    </div>
</div>

<script>
function inspectVillage(v) {
    const map = {
        silluk: { lbl: 'Hand-woven bamboo roadside baskets & composting keep Silluk spotless!', t: 'Silluk — Zero-Waste Village (Arunachal Pradesh)', d: 'Families weave natural bamboo waste baskets along green streets, compost all kitchen scraps locally, join monthly cleanup drives, and keep every avenue spotless without roadside plastic!' },
        narena: { lbl: 'Citizen teamwork turns shared courtyards & water points clean & proud!', t: 'Chhota Narena — Community Pride Model (Rajasthan)', d: 'By organizing collective street sweeping and caring for shared community water areas together, neighbors proved unified local action builds healthy spotless villages!' }
    };
    const d = map[v];
    if (!d) return;
    ['silluk', 'narena'].forEach(k => {
        const b = document.getElementById('btn-vil-' + k);
        if (b) {
            b.className = (k === v)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('vil-' + k + '-svg');
        if (g) {
            if (k === v) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('vil-svg-lbl').textContent = d.lbl;
    document.getElementById('vil-title').textContent = d.t;
    document.getElementById('vil-desc').textContent = d.d;
}
</script>
"""

# Simulator 12: Clean Indian Cities
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏙️</span>
            <h3 class="text-sm sm:text-base font-bold text-sky-300">Indore, Mysuru &amp; Swachh Bharat Mission Lab</h3>
        </div>
        <span class="text-[11px] bg-sky-950/80 text-sky-300 px-2.5 py-1 rounded-full border border-sky-800">Clean Cities</span>
    </div>

    <p class="text-xs text-slate-300">Explore how India's cleanest benchmark cities Indore and Mysuru manage millions of residents cleanly under Swachh Bharat Mission!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="inspectCity('indore')" id="btn-ct-indore" class="p-2.5 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500">🚛 Indore Model</button>
        <button onclick="inspectCity('mysuru')" id="btn-ct-mysuru" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🌿 Mysuru Model</button>
        <button onclick="inspectCity('swachh')" id="btn-ct-swachh" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🇮🇳 Clean India Mission</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 170" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Indore -->
            <g id="ct-indore-svg">
                <rect x="65" y="75" width="120" height="52" rx="6" fill="#0284c7" />
                <rect x="185" y="90" width="45" height="37" rx="4" fill="#38bdf8" />
                <circle cx="95" cy="130" r="12" fill="#334155" /><circle cx="205" cy="130" r="12" fill="#334155" />
                <text x="125" y="106" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">WET + DRY VAN</text>
            </g>
            <!-- Mysuru -->
            <g id="ct-mysuru-svg" class="hidden">
                <rect x="75" y="65" width="170" height="68" fill="#d97706" />
                <path d="M135,65 Q160,35 185,65 Z" fill="#facc15" />
                <circle cx="55" cy="115" r="18" fill="#16a34a" /><circle cx="265" cy="115" r="18" fill="#16a34a" />
            </g>
            <!-- Swachh -->
            <g id="ct-swachh-svg" class="hidden">
                <circle cx="120" cy="85" r="24" fill="none" stroke="#f97316" stroke-width="5" />
                <circle cx="200" cy="85" r="24" fill="none" stroke="#22c55e" stroke-width="5" />
                <line x1="144" y1="85" x2="176" y2="85" stroke="#ffffff" stroke-width="5" />
                <text x="160" y="135" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">SWACHH BHARAT MISSION</text>
            </g>
            <text x="160" y="158" fill="#7dd3fc" font-size="10" font-weight="bold" text-anchor="middle" id="ct-svg-lbl">Indore sorts wet &amp; dry household bins every single morning!</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-sky-300 text-sm" id="ct-title">Indore — Cleanest Urban Sorting Network</h4>
            <p class="text-slate-300 leading-relaxed" id="ct-desc">Millions of Indore citizens faithfully hand sorted green wet kitchen food and blue dry recyclables directly to daily neighborhood collection vans, turning waste into city compost and fuel!</p>
        </div>
    </div>
</div>

<script>
function inspectCity(c) {
    const map = {
        indore: { lbl: 'Indore sorts wet & dry household bins every single morning!', t: 'Indore — Cleanest Urban Sorting Network', d: 'Millions of Indore citizens faithfully hand sorted green wet kitchen food and blue dry recyclables directly to daily neighborhood collection vans, turning waste into city compost and fuel!' },
        mysuru: { lbl: 'Historic Mysuru shines through decentralized parks & citizen discipline!', t: 'Mysuru — Heritage Clean City & Compost Parks', d: 'Known nationwide for tree-lined streets and smart neighborhood composting centers, Mysuru thrives because every citizen avoids street littering cleanly.' },
        swachh: { lbl: 'Swachh Bharat Mission unites Indian schools, villages, and cities!', t: 'Swachh Bharat Mission (Clean India Movement)', d: 'A nationwide cleanliness movement empowering schools, rural homes, and cities to separate waste, stop littering, maintain clean toilets, and honor sanitation workers!' }
    };
    const d = map[c];
    if (!d) return;
    ['indore', 'mysuru', 'swachh'].forEach(k => {
        const b = document.getElementById('btn-ct-' + k);
        if (b) {
            b.className = (k === c)
                ? 'p-2.5 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        const g = document.getElementById('ct-' + k + '-svg');
        if (g) {
            if (k === c) g.classList.remove('hidden');
            else g.classList.add('hidden');
        }
    });
    document.getElementById('ct-svg-lbl').textContent = d.lbl;
    document.getElementById('ct-title').textContent = d.t;
    document.getElementById('ct-desc').textContent = d.d;
}
</script>
"""

# Simulator 13: Green Wet Bin
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🟢</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">GREEN Dustbin &amp; Compost Maker Tester</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Biodegradable Only</span>
    </div>

    <p class="text-xs text-slate-300">Click items below to test whether each belongs safely inside the GREEN compost dustbin!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="testGreenBin('peels')" id="btn-gb-peels" class="p-2 rounded-xl bg-slate-900 text-slate-200 font-bold text-xs border border-slate-700 hover:bg-emerald-900/50">🍌 Mango Peels</button>
        <button onclick="testGreenBin('leaves')" id="btn-gb-leaves" class="p-2 rounded-xl bg-slate-900 text-slate-200 font-bold text-xs border border-slate-700 hover:bg-emerald-900/50">🍂 Dry Leaves</button>
        <button onclick="testGreenBin('eggshell')" id="btn-gb-eggshell" class="p-2 rounded-xl bg-slate-900 text-slate-200 font-bold text-xs border border-slate-700 hover:bg-emerald-900/50">🥚 Eggshells</button>
        <button onclick="testGreenBin('spoon')" id="btn-gb-spoon" class="p-2 rounded-xl bg-slate-900 text-slate-200 font-bold text-xs border border-slate-700 hover:bg-rose-900/50">🥄 Plastic Spoon</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 flex flex-col sm:flex-row items-center gap-4">
        <svg viewBox="0 0 140 130" class="w-32 h-28 shrink-0 rounded-xl bg-slate-950 border border-slate-800">
            <polygon points="35,40 105,40 95,115 45,115" fill="#16a34a" stroke="#86efac" stroke-width="2" />
            <rect x="28" y="30" width="84" height="10" rx="3" fill="#15803d" />
            <text x="70" y="82" fill="#fff" font-size="12" font-weight="bold" text-anchor="middle">GREEN</text>
        </svg>
        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex-1 space-y-1 text-xs">
            <h4 class="font-bold text-emerald-300 text-sm" id="gb-res-title">Test Any Kitchen or Garden Item!</h4>
            <p class="text-slate-300 leading-relaxed" id="gb-res-desc">Pure biodegradable food scraps and leaves inside green bins turn into nutrient-rich black garden compost thanks to earthworms and soil microbes!</p>
        </div>
    </div>
</div>

<script>
function testGreenBin(item) {
    const map = {
        peels: { title: '✅ YES! Biodegradable Fruit & Vegetable Peels', desc: 'Mango skins, banana peels, and kitchen veggie tops digest rapidly inside green compost pits, turning cleanly into black plant manure!' },
        leaves: { title: '✅ YES! Fallen Garden Leaves & Flowers', desc: 'Dry neem leaves and wilted marigold garlands break down harmoniously with microbes into light airy garden soil compost!' },
        eggshell: { title: '✅ YES! Crushed Natural Eggshells', desc: 'Crushed eggshells add precious natural calcium minerals into green compost heaps, strengthening growing garden vegetables!' },
        spoon: { title: '❌ STOP! Keep Plastic Out of Green Bins!', desc: 'Plastic spoons NEVER rot naturally inside compost! Dropping plastic inside green bins spoils garden soil—put dry plastics in the BLUE bin!' }
    };
    const d = map[item];
    if (!d) return;
    document.getElementById('gb-res-title').textContent = d.title;
    document.getElementById('gb-res-desc').textContent = d.desc;
}
</script>
"""

# Simulator 14: Blue Dry Bin
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔵</span>
            <h3 class="text-sm sm:text-base font-bold text-sky-300">BLUE Dry Recyclable Bin &amp; Battery Safety Lab</h3>
        </div>
        <span class="text-[11px] bg-sky-950/80 text-sky-300 px-2.5 py-1 rounded-full border border-sky-800">Recyclables Only</span>
    </div>

    <p class="text-xs text-slate-300">Sort dry factory-recyclable materials cleanly into the BLUE bin and discover where dangerous dead batteries belong!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="testBlueBin('paper')" class="p-2 rounded-xl bg-slate-900 text-slate-200 font-bold text-xs border border-slate-700 hover:bg-sky-900/50">📰 Dry Newspaper</button>
        <button onclick="testBlueBin('metal')" class="p-2 rounded-xl bg-slate-900 text-slate-200 font-bold text-xs border border-slate-700 hover:bg-sky-900/50">🥫 Clean Tin / Jar</button>
        <button onclick="testBlueBin('bottle')" class="p-2 rounded-xl bg-slate-900 text-slate-200 font-bold text-xs border border-slate-700 hover:bg-sky-900/50">🧴 Rinsed Plastic</button>
        <button onclick="testBlueBin('battery')" class="p-2 rounded-xl bg-slate-900 text-slate-200 font-bold text-xs border border-slate-700 hover:bg-amber-900/50">🔋 Dead Battery</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 flex flex-col sm:flex-row items-center gap-4">
        <svg viewBox="0 0 140 130" class="w-32 h-28 shrink-0 rounded-xl bg-slate-950 border border-slate-800">
            <polygon points="35,40 105,40 95,115 45,115" fill="#0284c7" stroke="#7dd3fc" stroke-width="2" />
            <rect x="28" y="30" width="84" height="10" rx="3" fill="#0369a1" />
            <text x="70" y="82" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle">BLUE</text>
        </svg>
        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex-1 space-y-1 text-xs">
            <h4 class="font-bold text-sky-300 text-sm" id="bb-res-title">Inspect Dry Recyclables &amp; Hazardous Cells</h4>
            <p class="text-slate-300 leading-relaxed" id="bb-res-desc">Dry clean paper, cardboard, rinsed plastic jugs, glass jars, and metal cans recycle smoothly inside the BLUE bin—saving trees, ores, and factory energy!</p>
        </div>
    </div>
</div>

<script>
function testBlueBin(item) {
    const map = {
        paper: { title: '✅ BLUE BIN! Dry Paper & Cardboard Boxes', desc: 'Clean dry newspapers and flattened cartons pulp smoothly into fresh recycled notebooks and kraft bags without chopping new forest trees!' },
        metal: { title: '✅ BLUE BIN! Metal Cans & Clean Glass Jars', desc: 'Aluminum tins and unbroken empty glass jars melt and remold endlessly inside recycling factories without losing strength!' },
        bottle: { title: '✅ BLUE BIN! Empty Rinsed Plastic Containers', desc: 'Rinsing sticky milk or juice out first keeps blue-bin newspapers dry and odor-free while plastic pellets turn into benches or fiber!' },
        battery: { title: '⚠️ SPECIAL E-WASTE BOX! Do Not Mix Batteries!', desc: 'Dead batteries contain toxic chemicals! Keep batteries out of green compost and burning heaps—drop dead cells safely inside school E-Waste boxes!' }
    };
    const d = map[item];
    if (!d) return;
    document.getElementById('bb-res-title').textContent = d.title;
    document.getElementById('bb-res-desc').textContent = d.desc;
}
</script>
"""

# Simulator 15: School Cleaning Tools
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧹</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Classroom &amp; Home Cleaning Tools Cupboard</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Sanitation Kit</span>
    </div>

    <p class="text-xs text-slate-300">Select each shared cleaning tool to inspect its exact job and how pupils keep rooms clean cleanly with respect!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectCleanTool('broom')" id="btn-ctool-broom" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">🧹 Broom &amp; Pan</button>
        <button onclick="inspectCleanTool('mop')" id="btn-ctool-mop" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪣 Mop &amp; Bucket</button>
        <button onclick="inspectCleanTool('gloves')" id="btn-ctool-gloves" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧤 Safety Gloves</button>
        <button onclick="inspectCleanTool('bin')" id="btn-ctool-bin" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🗑️ Covered Bin</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
        <h4 class="font-bold text-amber-300 text-sm" id="ctool-title">Soft Indoor Broom + Flat-Edged Dustpan</h4>
        <p class="text-slate-300 leading-relaxed" id="ctool-desc">Soft grass-bristle brooms sweep fine classroom chalk dust smoothly into one neat pile, while wide dustpans scoop gathered dirt straight inside covered bins cleanly—never under desks!</p>
    </div>
</div>

<script>
function inspectCleanTool(tool) {
    const map = {
        broom: { t: 'Soft Indoor Broom + Flat-Edged Dustpan', d: 'Soft grass-bristle brooms sweep fine classroom chalk dust smoothly into one neat pile, while wide dustpans scoop gathered dirt straight inside covered bins cleanly—never under desks!' },
        mop: { t: 'Cotton Floor Mop & Water Bucket', d: 'Damp mops wrung cleanly inside soapy water buckets wipe sticky food spills and muddy footprints bright, dry, and germ-free!' },
        gloves: { t: 'Protective Sanitation Gloves', d: 'Thick rubber cleanup gloves guard hands against hidden sharp edges, dirty pebbles, and germs during schoolyard cleanup drives!' },
        bin: { t: 'Tightly Covered Dustbin Lids', d: 'Clicking dustbin lids shut stops buzzing houseflies, odors, and stray dogs from knocking tidy garbage back across corridors!' }
    };
    const d = map[tool];
    if (!d) return;
    ['broom', 'mop', 'gloves', 'bin'].forEach(k => {
        const b = document.getElementById('btn-ctool-' + k);
        if (b) {
            b.className = (k === tool)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('ctool-title').textContent = d.t;
    document.getElementById('ctool-desc').textContent = d.d;
}
</script>
"""

# Simulator 16: National Cleanliness Day
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌟</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">January 30th Cleanliness Pledge &amp; Motto Board</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Want Not, Waste Not</span>
    </div>

    <p class="text-xs text-slate-300">Check all 4 daily Earth-Guardian promises to seal your National Cleanliness Day (January 30th) pledge!</p>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
        <button onclick="signPledge('p1')" id="btn-pl-p1" class="p-2.5 rounded-xl bg-slate-900 text-slate-200 font-bold text-xs border border-slate-700 hover:bg-emerald-900/50">☐ 1. Say No To Plastic Carry Bags</button>
        <button onclick="signPledge('p2')" id="btn-pl-p2" class="p-2.5 rounded-xl bg-slate-900 text-slate-200 font-bold text-xs border border-slate-700 hover:bg-emerald-900/50">☐ 2. Sort Green Wet &amp; Blue Dry Bins</button>
        <button onclick="signPledge('p3')" id="btn-pl-p3" class="p-2.5 rounded-xl bg-slate-900 text-slate-200 font-bold text-xs border border-slate-700 hover:bg-emerald-900/50">☐ 3. Reuse Books, Cloth &amp; Steel Bottles</button>
        <button onclick="signPledge('p4')" id="btn-pl-p4" class="p-2.5 rounded-xl bg-slate-900 text-slate-200 font-bold text-xs border border-slate-700 hover:bg-emerald-900/50">☐ 4. Live 'Want Not, Waste Not' Daily</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-center space-y-1.5 text-xs">
        <div class="text-amber-300 font-extrabold text-sm" id="pl-status">Promises Checked: 0 / 4</div>
        <p class="text-slate-300" id="pl-msg">Every small clean action on January 30th and every day keeps villages, schools, animals, and skies bright!</p>
    </div>
</div>

<script>
window.ch12Pledges = { p1: false, p2: false, p3: false, p4: false };
function signPledge(pid) {
    window.ch12Pledges[pid] = !window.ch12Pledges[pid];
    const labels = {
        p1: '1. Say No To Plastic Carry Bags',
        p2: '2. Sort Green Wet & Blue Dry Bins',
        p3: '3. Reuse Books, Cloth & Steel Bottles',
        p4: "4. Live 'Want Not, Waste Not' Daily"
    };
    const btn = document.getElementById('btn-pl-' + pid);
    if (btn) {
        const on = window.ch12Pledges[pid];
        btn.className = on
            ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-400'
            : 'p-2.5 rounded-xl bg-slate-900 text-slate-200 font-bold text-xs border border-slate-700 hover:bg-emerald-900/50';
        btn.textContent = (on ? '✅ ' : '☐ ') + labels[pid];
    }
    const count = Object.values(window.ch12Pledges).filter(Boolean).length;
    document.getElementById('pl-status').textContent = `Promises Checked: ${count} / 4`;
    document.getElementById('pl-msg').textContent = count === 4
        ? "🎉 Official Earth Guardian Badge Earned! Keep living 'Want not, Waste not!' across home & school!"
        : "Every small clean action on January 30th and every day keeps villages, schools, animals, and skies bright!";
}
</script>
"""
