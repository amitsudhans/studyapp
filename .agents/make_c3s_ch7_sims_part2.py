#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 7: Water - A Precious Gift
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Daily Water Needs (Household Water Budget Explorer)
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏠</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Daily Household Water Usage Estimator</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Daily Consumption</span>
    </div>

    <p class="text-xs text-slate-300">Inspect how many liters an average person uses across everyday activities—notice how cleaning consumes far more water than drinking!</p>

    <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
        <button onclick="inspectDailyNeed('drink')" id="btn-need-drink" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left flex items-center gap-2">
            <span class="text-xl">🥛</span><span>Drinking (3 L)</span>
        </button>
        <button onclick="inspectDailyNeed('cook')" id="btn-need-cook" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-xl">🍲</span><span>Cooking Food (6 L)</span>
        </button>
        <button onclick="inspectDailyNeed('bath')" id="btn-need-bath" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-xl">🛁</span><span>Bucket Bath (18 L)</span>
        </button>
        <button onclick="inspectDailyNeed('laundry')" id="btn-need-laundry" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-xl">👕</span><span>Laundry &amp; Wash (35 L)</span>
        </button>
        <button onclick="inspectDailyNeed('flush')" id="btn-need-flush" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-xl">🚽</span><span>Sanitation Flush (24 L)</span>
        </button>
        <button onclick="inspectDailyNeed('garden')" id="btn-need-garden" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-xl">🪴</span><span>Plants &amp; Pets (6 L)</span>
        </button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 space-y-3 text-xs">
        <div class="flex items-center justify-between">
            <span class="text-slate-400">Selected Activity Share:</span>
            <span class="text-cyan-300 font-bold text-sm" id="need-ratio">3 Liters (~12 Glasses) out of 92L Total</span>
        </div>
        <div class="w-full bg-slate-950 h-5 rounded-full overflow-hidden border border-slate-800 p-0.5">
            <div id="need-bar" class="h-full bg-gradient-to-r from-cyan-500 to-emerald-400 rounded-full transition-all duration-300" style="width: 8%;"></div>
        </div>
        <p id="need-tip" class="text-slate-200 bg-slate-950 p-3 rounded-xl border border-slate-800">
            <strong class="text-emerald-300">Vital Need:</strong> Drinking water keeps organs healthy and cools the body, yet represents under 5% of total home water spent!
        </p>
    </div>
</div>

<script>
function inspectDailyNeed(key) {
    const data = {
        drink: { ratio: '3 Liters (~12 Glasses) out of 92L Total', pct: '8%', tip: '<strong class="text-emerald-300">Vital Need:</strong> Drinking water keeps organs healthy and cools the body, yet represents under 5% of total home water spent!' },
        cook: { ratio: '6 Liters out of 92L Total', pct: '14%', tip: '<strong class="text-cyan-300">Kitchen Care:</strong> Washing grains, lentils, and vegetables needs clean water—afterward, reuse rinse water for flowerpots!' },
        bath: { ratio: '18 Liters (1 Full Bucket) out of 92L Total', pct: '36%', tip: '<strong class="text-amber-300">Smart Hygiene:</strong> Bathing with one bucket and mug uses ~18L instead of 100L wasted under long running showers.' },
        laundry: { ratio: '35 Liters out of 92L Total', pct: '70%', tip: '<strong class="text-rose-300">Highest Demand:</strong> Washing clothes consumes the largest household bucket share—wash full loads rather than tiny single items!' },
        flush: { ratio: '24 Liters out of 92L Total', pct: '50%', tip: '<strong class="text-sky-300">Sanitation Savings:</strong> Using leftover mop or laundry rinse water for flushing saves pure piped freshwater daily.' },
        garden: { ratio: '6 Liters out of 92L Total', pct: '14%', tip: '<strong class="text-emerald-300">Evening Watering:</strong> Water plants early morning or evening so hot midday sun does not evaporate moisture swiftly.' }
    };
    const d = data[key];
    if (!d) return;

    ['drink', 'cook', 'bath', 'laundry', 'flush', 'garden'].forEach(k => {
        const b = document.getElementById('btn-need-' + k);
        if (b) {
            b.className = (k === key)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left flex items-center gap-2'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';
        }
    });
    document.getElementById('need-ratio').textContent = d.ratio;
    document.getElementById('need-bar').style.width = d.pct;
    document.getElementById('need-tip').innerHTML = d.tip;
}
</script>
"""

# Simulator 10: Handling Water Scarcity (Emergency Rationing Simulator)
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🚨</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Pipe Burst Emergency Water Rationing Planner</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Scarcity Coping</span>
    </div>

    <p class="text-xs text-slate-300">Neighborhood pipes shut off for repairs! Decide wisely which tasks get priority from your covered 45-Liter emergency bucket reserve.</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="decideScarcity('drinking')" id="btn-sc-drinking" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 text-left">
            <span class="block">1. Covered Drinking &amp; Cooking</span>
            <span class="text-[10px] text-emerald-200">Priority #1 (Essential)</span>
        </button>
        <button onclick="decideScarcity('wipe')" id="btn-sc-wipe" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left">
            <span class="block">2. Small Mug Handwashing</span>
            <span class="text-[10px] text-slate-400">Priority #2 (Controlled)</span>
        </button>
        <button onclick="decideScarcity('carwash')" id="btn-sc-carwash" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left">
            <span class="block">3. Hosing Car &amp; Driveway</span>
            <span class="text-[10px] text-slate-400">Postpone Until Repairs!</span>
        </button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center text-xs">
        <div class="flex items-center justify-center gap-4">
            <div class="text-center p-3 rounded-xl bg-slate-900 border border-slate-700">
                <div class="text-4xl mb-1" id="sc-bucket-icon">🪣</div>
                <div class="font-bold text-cyan-300" id="sc-reserve">45L Covered Reserve: SAFE</div>
            </div>
        </div>
        <div class="space-y-2">
            <span class="inline-block px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 font-bold text-[10px]" id="sc-verdict-badge">WISE DECISION ✓</span>
            <p id="sc-verdict-text" class="text-slate-200 leading-relaxed">
                Reserving covered, germ-free buckets exclusively for drinking and cooking meals ensures family health stays completely safe throughout pipe repairs!
            </p>
        </div>
    </div>
</div>

<script>
function decideScarcity(choice) {
    const map = {
        drinking: {
            icon: '🥤🍲', reserve: '35L Drinking Reserve Remaining', badge: 'WISE PRIORITY #1 ✓',
            bClass: 'inline-block px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 font-bold text-[10px]',
            text: 'Reserving covered, germ-free buckets exclusively for drinking and cooking meals ensures family health stays completely safe throughout pipe repairs!'
        },
        wipe: {
            icon: '🧼☕', reserve: '28L Clean Reserve Remaining', badge: 'SMART RATIONING ✓',
            bClass: 'inline-block px-2 py-0.5 rounded bg-cyan-950 text-cyan-300 border border-cyan-800 font-bold text-[10px]',
            text: 'Using small steel mugs to scoop measured water avoids accidental splashing while keeping hand hygiene and utensil rinsing safe!'
        },
        carwash: {
            icon: '🚫🚗', reserve: '0L! Emergency Reserve Emptied!', badge: 'BAD IDEA — POSTPONE! ✕',
            bClass: 'inline-block px-2 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-800 font-bold text-[10px]',
            text: 'Wasting scarce stored water on cars or driveways leaves zero drinking water until the pipe repair truck finishes! Always postpone heavy non-essential chores.'
        }
    };
    const d = map[choice];
    if (!d) return;

    ['drinking', 'wipe', 'carwash'].forEach(k => {
        const b = document.getElementById('btn-sc-' + k);
        if (b) {
            b.className = (k === choice)
                ? 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 text-left'
                : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left';
        }
    });
    document.getElementById('sc-bucket-icon').textContent = d.icon;
    document.getElementById('sc-reserve').textContent = d.reserve;
    document.getElementById('sc-verdict-badge').textContent = d.badge;
    document.getElementById('sc-verdict-badge').className = d.bClass;
    document.getElementById('sc-verdict-text').textContent = d.text;
}
</script>
"""

# Simulator 11: Clay Water Pots (Evaporative Cooling Physics)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏺</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Matka &amp; Surahi Natural Evaporative Cooling Lab</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Cooling Physics</span>
    </div>

    <p class="text-xs text-slate-300">Compare porous unglazed terracotta clay pots against glazed/plastic bottles in 35°C summer heat to discover how pores chill water!</p>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="testPotCooling('porous')" id="btn-pot-porous" class="p-3 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500 text-left flex items-center gap-2">
            <span class="text-2xl">🏺</span>
            <div><span class="block">Porous Terracotta Matka</span><span class="text-[10px] text-amber-100">Microscopic Pores Open</span></div>
        </button>
        <button onclick="testPotCooling('sealed')" id="btn-pot-sealed" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-2xl">🧴</span>
            <div><span class="block">Sealed Painted / Plastic Jar</span><span class="text-[10px] text-slate-400">Zero Surface Evaporation</span></div>
        </button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 220" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Matka Body -->
            <circle id="pot-body" cx="250" cy="125" r="65" fill="#b45309" stroke="#f59e0b" stroke-width="3" />
            <rect x="220" y="52" width="60" height="16" rx="4" fill="#92400e" />
            <!-- Ladle sticking out cleanly -->
            <line x1="255" y1="52" x2="285" y2="20" stroke="#cbd5e1" stroke-width="4" stroke-linecap="round" />

            <!-- Evaporation Heat Vapor Waves -->
            <g id="pot-evap-waves" fill="#38bdf8" font-size="13" font-weight="bold">
                <text x="155" y="100">💨💧</text>
                <text x="325" y="100">💨💧</text>
                <text x="155" y="150">Heat Absorbed!</text>
            </g>

            <!-- Temperature Readout Box -->
            <g transform="translate(430, 55)">
                <rect x="0" y="0" width="220" height="110" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2" />
                <text x="110" y="25" fill="#94a3b8" font-size="11" text-anchor="middle">Ambient Room Air: 35°C</text>
                <text id="pot-temp-val" x="110" y="65" fill="#38bdf8" font-size="30" font-weight="bold" text-anchor="middle">23°C ❄️</text>
                <text id="pot-temp-note" x="110" y="92" fill="#4ade80" font-size="11" font-weight="bold" text-anchor="middle">Chilled Naturally (-12°C!)</text>
            </g>
        </svg>
    </div>

    <div class="bg-slate-900/90 p-3.5 rounded-xl border border-slate-800 text-xs">
        <p id="pot-physics-desc" class="text-slate-200">
            <strong class="text-amber-300">Natural Science Secret:</strong> Tiny invisible pores in unglazed clay let water seep outward and evaporate into warm summer breezes—stealing heat away from the water resting inside!
        </p>
    </div>
</div>

<script>
function testPotCooling(mode) {
    const isPorous = (mode === 'porous');
    document.getElementById('btn-pot-porous').className = isPorous
        ? 'p-3 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500 text-left flex items-center gap-2'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';
    document.getElementById('btn-pot-sealed').className = !isPorous
        ? 'p-3 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left flex items-center gap-2'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';

    document.getElementById('pot-body').setAttribute('fill', isPorous ? '#b45309' : '#0284c7');
    document.getElementById('pot-evap-waves').setAttribute('opacity', isPorous ? '1' : '0');
    document.getElementById('pot-temp-val').textContent = isPorous ? '23°C ❄️' : '34°C 🌡️';
    document.getElementById('pot-temp-val').setAttribute('fill', isPorous ? '#38bdf8' : '#f87171');
    document.getElementById('pot-temp-note').textContent = isPorous ? 'Chilled Naturally (-12°C!)' : 'Lukewarm (No Evaporation)';
    document.getElementById('pot-physics-desc').innerHTML = isPorous
        ? '<strong class="text-amber-300">Natural Science Secret:</strong> Tiny invisible pores in unglazed clay let water seep outward and evaporate into warm summer breezes—stealing heat away from the water resting inside!'
        : '<strong class="text-rose-300">Pores Blocked:</strong> Plastic walls or glossy enamel paint seal off every pore, trapping heat inside so stored water stays lukewarm at room temperature.';
}
</script>
"""

# Simulator 12: Vessel Material Exhibition (7 Materials Gallery)
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏺</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Water Storage Vessel Evolution Museum</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Activity 3 Exhibition</span>
    </div>

    <p class="text-xs text-slate-300">Select each exhibition specimen crafted from traditional and modern materials to examine its hygiene, durability, and planet impact!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-1.5">
        <button onclick="inspectVessel('clay')" id="btn-ves-clay" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-[11px] border border-cyan-500">🏺 Clay</button>
        <button onclick="inspectVessel('copper')" id="btn-ves-copper" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-[11px] border border-slate-700 hover:bg-slate-800">🟠 Copper</button>
        <button onclick="inspectVessel('brass')" id="btn-ves-brass" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-[11px] border border-slate-700 hover:bg-slate-800">🟡 Brass</button>
        <button onclick="inspectVessel('steel')" id="btn-ves-steel" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-[11px] border border-slate-700 hover:bg-slate-800">🪙 Steel</button>
        <button onclick="inspectVessel('alum')" id="btn-ves-alum" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-[11px] border border-slate-700 hover:bg-slate-800">🥫 Aluminium</button>
        <button onclick="inspectVessel('glass')" id="btn-ves-glass" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-[11px] border border-slate-700 hover:bg-slate-800">🥃 Glass</button>
        <button onclick="inspectVessel('plastic')" id="btn-ves-plastic" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-[11px] border border-slate-700 hover:bg-slate-800">🧴 Plastic</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-3 gap-4 items-center text-xs">
        <div class="text-center p-4 bg-slate-900 rounded-xl border border-slate-800">
            <div class="text-5xl mb-2" id="ves-emoji">🏺</div>
            <h4 class="font-bold text-cyan-300 text-sm" id="ves-title">Terracotta Clay (Matka / Surahi)</h4>
        </div>
        <div class="md:col-span-2 space-y-2">
            <div class="bg-emerald-950/50 p-2.5 rounded-xl border border-emerald-800/60">
                <span class="text-emerald-400 font-bold">✓ Key Advantage:</span>
                <span id="ves-pro" class="text-slate-200 block mt-0.5">Naturally chills water without electricity via porous evaporation; 100% biodegradable earth clay!</span>
            </div>
            <div class="bg-amber-950/40 p-2.5 rounded-xl border border-amber-800/50">
                <span class="text-amber-400 font-bold">⚠️ Caution &amp; Care:</span>
                <span id="ves-con" class="text-slate-200 block mt-0.5">Heavy and cracks easily if knocked over; scrub softly inside weekly without chemical soap.</span>
            </div>
        </div>
    </div>
</div>

<script>
function inspectVessel(mat) {
    const map = {
        clay: { e: '🏺', t: 'Terracotta Clay (Matka / Surahi)', p: 'Naturally chills water without electricity via porous evaporation; 100% biodegradable earth clay!', c: 'Heavy and cracks easily if knocked over; scrub softly inside weekly without chemical soap.' },
        copper: { e: '🟠', t: 'Copper Vessel (Tamba Pitcher)', p: 'Helps inhibit harmful waterborne bacteria naturally when clean water sits overnight inside!', c: 'Needs regular scrubbing with lemon juice or tamarind to remove greenish tarnish safely.' },
        brass: { e: '🟡', t: 'Brass Pitcher (Pital Kalash)', p: 'Strong traditional heritage metal alloy crafted by village artisans that lasts for generations.', c: 'Must be scrubbed clean diligently and never used for storing sour acidic liquids.' },
        steel: { e: '🪙', t: 'Stainless Steel Bottles & Drums', p: 'Rust-proof, virtually unbreakable, easy to wash squeaky clean, and zero microplastic leaching!', c: 'Conducts heat rapidly outdoors unless double-walled; water stays at ambient temperature.' },
        alum: { e: '🥫', t: 'Silvery Aluminium Cans', p: 'Very lightweight and strong for carrying large volumes of farm or utility water easily.', c: 'Dents under drops and reacts with salty or sour liquids—best reserved for non-cooking utility water.' },
        glass: { e: '🥃', t: 'Clear Glass Carafes & Bottles', p: 'Completely non-reactive and transparent so you spot any tiny floating specks instantly!', c: 'Heavy and shatters into sharp dangerous shards if dropped on hard tiles.' },
        plastic: { e: '🧴', t: 'Modern Plastic Bottles & Tanks', p: 'Featherlight and shatter-resistant for large rooftop storage tanks and travel crates.', c: 'Single-use plastic bottles pollute oceans for centuries and release microplastics when heated in sun!' }
    };
    const d = map[mat];
    if (!d) return;

    ['clay', 'copper', 'brass', 'steel', 'alum', 'glass', 'plastic'].forEach(k => {
        const b = document.getElementById('btn-ves-' + k);
        if (b) {
            b.className = (k === mat)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-[11px] border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-[11px] border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('ves-emoji').textContent = d.e;
    document.getElementById('ves-title').textContent = d.t;
    document.getElementById('ves-pro').textContent = d.p;
    document.getElementById('ves-con').textContent = d.c;
}
</script>
"""

# Simulator 13: Saving Every Drop (Water Conservation Calculator)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">💧</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Water Detective Savings &amp; Leak Fixer</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Every Drop Counts</span>
    </div>

    <p class="text-xs text-slate-300">Toggle smart water-saving habits below to calculate how many fresh liters ONE student rescues in a single day!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="toggleSaveHabit('brush')" id="btn-save-brush" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left">
            <span class="block">🪥 Close Tap Brushing</span>
            <span class="text-[10px] text-emerald-400">Saves +12 Liters / Day</span>
        </button>
        <button onclick="toggleSaveHabit('leak')" id="btn-save-leak" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left">
            <span class="block">🔧 Fix Dripping Faucet</span>
            <span class="text-[10px] text-emerald-400">Saves +30 Liters / Day</span>
        </button>
        <button onclick="toggleSaveHabit('bucket')" id="btn-save-bucket" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left">
            <span class="block">🪣 Bucket Bath vs Shower</span>
            <span class="text-[10px] text-emerald-400">Saves +80 Liters / Day</span>
        </button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="text-center sm:text-left">
            <span class="text-xs text-slate-400 uppercase tracking-wider block">Daily Freshwater Saved:</span>
            <span id="saved-liters-total" class="text-3xl font-extrabold text-emerald-400">0 Liters / Day</span>
            <span id="saved-monthly-note" class="text-[11px] text-cyan-300 block mt-1">Click the smart switches above to rescue precious drops!</span>
        </div>
        <div class="text-4xl bg-slate-900 px-5 py-3 rounded-2xl border border-slate-800" id="saved-badge-emoji">🚰</div>
    </div>
</div>

<script>
const saveState = { brush: false, leak: false, bucket: false };

function toggleSaveHabit(key) {
    saveState[key] = !saveState[key];
    const btn = document.getElementById('btn-save-' + key);
    if (btn) {
        btn.className = saveState[key]
            ? 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 text-left shadow'
            : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left';
    }

    let total = 0;
    if (saveState.brush) total += 12;
    if (saveState.leak) total += 30;
    if (saveState.bucket) total += 80;

    document.getElementById('saved-liters-total').textContent = `${total} Liters / Day`;
    document.getElementById('saved-monthly-note').textContent = total > 0
        ? `Amazing! That equals ${(total * 30).toLocaleString()} Liters rescued every single month!`
        : 'Click the smart switches above to rescue precious drops!';
    document.getElementById('saved-badge-emoji').textContent = total >= 100 ? '🏆🌊' : (total > 0 ? '💧✨' : '🚰');
}
</script>
"""

# Simulator 14: Reusing Household Water (Greywater Loop Router)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">♻️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Smart Greywater Reuse &amp; Pollution Shield</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Second-Life Water</span>
    </div>

    <p class="text-xs text-slate-300">Route different types of household used water to safe second uses while protecting ponds from chemical pollution!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="routeGreywater('veggie')" id="btn-gw-veggie" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 text-left flex items-center gap-2">
            <span class="text-xl">🥬</span><span>Rice &amp; Veggie Rinse</span>
        </button>
        <button onclick="routeGreywater('mop')" id="btn-gw-mop" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-xl">🧽</span><span>Mop / Laundry Rinse</span>
        </button>
        <button onclick="routeGreywater('bleach')" id="btn-gw-bleach" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-xl">🧪</span><span>Excess Harsh Soap</span>
        </button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-4xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="gw-dest-icon">🪴</div>
        <div class="space-y-1">
            <h4 class="font-bold text-emerald-300 text-sm" id="gw-dest-title">Best Match: Watering Tulsi &amp; Kitchen Garden</h4>
            <p class="text-slate-300" id="gw-dest-desc">Clean water from washing rice, dals, and leafy greens contains zero harsh detergents—it hydrates potted shrubs and nourishes gentle garden roots safely!</p>
        </div>
    </div>
</div>

<script>
function routeGreywater(type) {
    const map = {
        veggie: { icon: '🪴', title: 'Best Match: Watering Tulsi & Kitchen Garden', desc: 'Clean water from washing rice, dals, and leafy greens contains zero harsh detergents—it hydrates potted shrubs and nourishes gentle garden roots safely!' },
        mop: { icon: '🚽', title: 'Best Match: Toilet Flushing & Muddy Tire Wash', desc: 'Water remaining after floor mopping or final clothes rinsing should never touch drinking pots or soil herbs, yet works cleanly for flushing toilets!' },
        bleach: { icon: '⚠️', title: 'Pollution Warning: Avoid Excess Chemical Soaps!', desc: 'Dumping strong bleaches and heavy foaming detergents down street drains harms soil earthworms, poisons pond frogs, and pollutes local water!' }
    };
    const d = map[type];
    if (!d) return;

    ['veggie', 'mop', 'bleach'].forEach(k => {
        const b = document.getElementById('btn-gw-' + k);
        if (b) {
            b.className = (k === type)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 text-left flex items-center gap-2'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';
        }
    });
    document.getElementById('gw-dest-icon').textContent = d.icon;
    document.getElementById('gw-dest-title').textContent = d.title;
    document.getElementById('gw-dest-desc').textContent = d.desc;
}
</script>
"""

# Simulator 15: Public Water Pots (Community Pyau Builder)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🤝</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Summer Community Pyau &amp; Animal Water Stand</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Shared Kindness</span>
    </div>

    <p class="text-xs text-slate-300">Inspect the essential pieces of a welcoming neighborhood summer water stand helping tired travelers and street animals!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectPyau('shade')" id="btn-pyau-shade" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500 text-center">⛺ Shaded Roof</button>
        <button onclick="inspectPyau('cloth')" id="btn-pyau-cloth" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center">🧣 Wet Burlap</button>
        <button onclick="inspectPyau('ladle')" id="btn-pyau-ladle" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center">🥄 Brass Ladle</button>
        <button onclick="inspectPyau('bowl')" id="btn-pyau-bowl" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center">🐕 Animal Bowl</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-4xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="pyau-icon">⛺</div>
        <div class="space-y-1">
            <h4 class="font-bold text-amber-300 text-sm" id="pyau-title">Cool Thatched Shade Over Clay Pots</h4>
            <p class="text-slate-300" id="pyau-desc">Resting earthenware matkas beneath leafy or thatched shade blocks scorching May sunshine, keeping water naturally refreshingly chilled for tired postal carriers and walkers.</p>
        </div>
    </div>
</div>

<script>
function inspectPyau(part) {
    const map = {
        shade: { icon: '⛺', title: 'Cool Thatched Shade Over Clay Pots', desc: 'Resting earthenware matkas beneath leafy or thatched shade blocks scorching May sunshine, keeping water naturally refreshingly chilled for tired postal carriers and walkers.' },
        cloth: { icon: '🧣', title: 'Damp Jute Sackcloth Wrap', desc: 'Draping damp coarse cloth around clay pot walls boosts surface evaporation in dry winds, dropping drinking water temperature even lower!' },
        ladle: { icon: '🥄', title: 'Long-Handled Clean Serving Ladle', desc: 'A clean long-handled brass or steel ladle lets passersby pour crisp cool water without touching shared pot water with dusty fingers.' },
        bowl: { icon: '🐕', title: 'Ground-Level Stone Animal Basin', desc: 'Placing a shallow wide stone dish at the base ensures thirsty stray dogs, cows, and passing goats drink happily right alongside humans!' }
    };
    const d = map[part];
    if (!d) return;

    ['shade', 'cloth', 'ladle', 'bowl'].forEach(k => {
        const b = document.getElementById('btn-pyau-' + k);
        if (b) {
            b.className = (k === part)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500 text-center'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center';
        }
    });
    document.getElementById('pyau-icon').textContent = d.icon;
    document.getElementById('pyau-title').textContent = d.title;
    document.getElementById('pyau-desc').textContent = d.desc;
}
</script>
"""

# Simulator 16: Making Summer Birdbaths (Activity 4 Engineering Studio)
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🐦</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Activity 4: Four-Step Safe Birdbath Builder</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Wildlife Care Lab</span>
    </div>

    <p class="text-xs text-slate-300">Follow all four engineering steps to construct a safe, clean drinking sanctuary for summer birds, squirrels, and pollinators!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setBirdbathStep(1)" id="btn-bb-1" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">1. Shallow Tray</button>
        <button onclick="setBirdbathStep(2)" id="btn-bb-2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. Perch Stones</button>
        <button onclick="setBirdbathStep(3)" id="btn-bb-3" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. Safe Shade</button>
        <button onclick="setBirdbathStep(4)" id="btn-bb-4" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">4. Daily Scrub</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 210" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Shade Canopy -->
            <circle cx="150" cy="40" r="85" fill="#15803d" opacity="0.45" />
            <!-- Pedestal & Shallow Dish -->
            <rect x="330" y="150" width="40" height="55" fill="#64748b" />
            <ellipse cx="350" cy="145" rx="135" ry="26" fill="#92400e" stroke="#b45309" stroke-width="3" />
            <ellipse cx="350" cy="142" rx="120" ry="18" fill="#38bdf8" opacity="0.85" />

            <!-- Perching & Rescue Stones -->
            <g id="bb-stones">
                <ellipse cx="290" cy="142" rx="18" ry="8" fill="#64748b" />
                <ellipse cx="385" cy="145" rx="22" ry="9" fill="#475569" />
                <ellipse cx="340" cy="136" rx="14" ry="7" fill="#94a3b8" />
            </g>

            <!-- Wildlife Visitors -->
            <text x="275" y="128" font-size="26">🐦</text>
            <text x="380" y="130" font-size="20">🐝</text>
            <text x="430" y="124" font-size="22">🦋</text>
            <text x="350" y="38" fill="#86efac" font-size="13" font-weight="bold" text-anchor="middle" id="bb-svg-caption">Step 1: Choose Wide Shallow Clay Saucer (3-5 cm Depth)</text>
        </svg>
    </div>

    <div class="bg-slate-900/90 p-3.5 rounded-xl border border-emerald-800/60 text-xs">
        <p id="bb-step-desc" class="text-slate-200">
            <strong class="text-emerald-300">Why Shallow?</strong> Never use deep slippery buckets! A wide shallow earthen saucer lets sparrows splash safely without sinking while rough clay prevents claws from slipping.
        </p>
    </div>
</div>

<script>
function setBirdbathStep(step) {
    const steps = {
        1: { cap: 'Step 1: Choose Wide Shallow Clay Saucer (3-5 cm Depth)', desc: '<strong class="text-emerald-300">Why Shallow?</strong> Never use deep slippery buckets! A wide shallow earthen saucer lets sparrows splash safely without sinking while rough clay prevents claws from slipping.' },
        2: { cap: 'Step 2: Add Flat Rough Perching & Rescue Pebbles', desc: '<strong class="text-amber-300">Safety Islands:</strong> Flat river stones above the water surface offer sturdy feet grips for songbirds and dry rescue ramps so honeybees and butterflies drink without drowning!' },
        3: { cap: 'Step 3: Place Inside Cool Dappled Tree Shade Away From Cats', desc: '<strong class="text-cyan-300">Cool &amp; Safe Location:</strong> Shaded ledges keep water refreshingly cool while elevated open branches let nervous birds spot stalking cats immediately.' },
        4: { cap: 'Step 4: Scrub Dish Clean &amp; Refill Fresh Water Daily', desc: '<strong class="text-emerald-300">Mosquito-Free Care:</strong> Rinsing and refilling every morning eliminates slimy algae and breaks mosquito breeding cycles completely!' }
    };
    const s = steps[step];
    if (!s) return;

    for (let i = 1; i <= 4; i++) {
        const b = document.getElementById('btn-bb-' + i);
        if (b) {
            b.className = (i === step)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    }
    document.getElementById('bb-svg-caption').textContent = s.cap;
    document.getElementById('bb-step-desc').innerHTML = s.desc;
}
</script>
"""

if __name__ == "__main__":
    print(f"Generated {len(simulators_part2)} simulators for Part 2 (9 to 16).")
    for k in sorted(simulators_part2.keys()):
        print(f"Sim {k}: {len(simulators_part2[k])} chars")
