#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 9: Staying Healthy and Happy
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Daily Hygiene Habits
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✨</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Clean &amp; Bright Daily Hygiene Armor Checklist</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Personal Care</span>
    </div>

    <p class="text-xs text-slate-300">Toggle all five daily personal hygiene habits below to build your 100% sparkling Germ-Free Armor Shield!</p>

    <div class="grid grid-cols-2 sm:grid-cols-5 gap-2">
        <button onclick="toggleHygiene('brush')" id="btn-hy-brush" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪥 Brush Twice</button>
        <button onclick="toggleHygiene('bath')" id="btn-hy-bath" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🚿 Daily Bath</button>
        <button onclick="toggleHygiene('comb')" id="btn-hy-comb" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">💇 Comb Hair</button>
        <button onclick="toggleHygiene('soap')" id="btn-hy-soap" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧼 Soap Hands</button>
        <button onclick="toggleHygiene('nails')" id="btn-hy-nails" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">✂️ Trim Nails</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 space-y-2.5 text-xs">
        <div class="flex items-center justify-between">
            <span class="text-slate-400">Hygiene Shield Strength:</span>
            <span id="hy-pct-label" class="font-extrabold text-amber-400 text-sm">0% Active</span>
        </div>
        <div class="w-full bg-slate-900 h-4 rounded-full overflow-hidden border border-slate-800 p-0.5">
            <div id="hy-progress-bar" class="h-full bg-gradient-to-r from-emerald-500 to-cyan-400 rounded-full transition-all duration-300" style="width: 0%;"></div>
        </div>
        <p id="hy-feedback" class="text-slate-300 pt-1">Click every hygiene habit above to shield your healthy body cleanly from germs!</p>
    </div>
</div>

<script>
const hyState = { brush: false, bath: false, comb: false, soap: false, nails: false };

function toggleHygiene(key) {
    hyState[key] = !hyState[key];
    const btn = document.getElementById('btn-hy-' + key);
    if (btn) {
        btn.className = hyState[key]
            ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow'
            : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
    }
    const count = Object.values(hyState).filter(Boolean).length;
    const pct = count * 20;
    document.getElementById('hy-pct-label').textContent = `${pct}% Active`;
    document.getElementById('hy-progress-bar').style.width = `${pct}%`;
    document.getElementById('hy-feedback').textContent = pct === 100
        ? '100% Clean & Bright! Short trimmed nails, scrubbed teeth, clean hair, fresh baths, and soapy hands block germs completely!'
        : `Great! Activated ${count} of 5 clean habits—keep tapping to complete your daily shield.`;
}
</script>
"""

# Simulator 2: Washing Hands Cleanly
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧼</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">20-Second Scientific Handwashing Lab</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Soap &amp; Friction</span>
    </div>

    <p class="text-xs text-slate-300">Follow all four handwashing steps with real soap and watch stubborn germs vanish off palms and fingernails!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setWashStep(1)" id="btn-ws-1" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">1. Wet &amp; Soap</button>
        <button onclick="setWashStep(2)" id="btn-ws-2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. Palms &amp; Webs</button>
        <button onclick="setWashStep(3)" id="btn-ws-3" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. Nails (20s!)</button>
        <button onclick="setWashStep(4)" id="btn-ws-4" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">4. Rinse &amp; Dry</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs">
        <div class="text-center p-4 bg-slate-900 rounded-xl border border-slate-800 min-w-[160px]">
            <div class="text-4xl mb-1" id="ws-emoji">🖐️🦠</div>
            <span id="ws-germs" class="text-rose-400 font-bold block">Microbes Remaining: 90%</span>
        </div>
        <div class="space-y-1 flex-1">
            <h4 class="font-bold text-cyan-300 text-sm" id="ws-title">Step 1: Wet Hands, Shut Tap &amp; Apply Mild Soap</h4>
            <p class="text-slate-300" id="ws-desc">Plain 2-second splashes slide right over oily dirt! Closing the faucet while building soap lather cleans cleanly while saving fresh tap water.</p>
        </div>
    </div>
</div>

<script>
function setWashStep(step) {
    const map = {
        1: { e: '🖐️🦠', g: 'Microbes Remaining: 90%', gc: 'text-rose-400 font-bold block', t: 'Step 1: Wet Hands, Shut Tap & Apply Mild Soap', d: 'Plain 2-second splashes slide right over oily dirt! Closing the faucet while building soap lather cleans cleanly while saving fresh tap water.' },
        2: { e: '🫧🤝', g: 'Microbes Remaining: 45%', gc: 'text-amber-300 font-bold block', t: 'Step 2: Scrub Palms, Back of Hands & Interlaced Fingers', d: 'Rub soapy palms briskly together and weave fingers tightly back and forth so creamy soap lather lifts hidden dust between finger webs.' },
        3: { e: '✨💅', g: 'Microbes Remaining: 10%', gc: 'text-cyan-300 font-bold block', t: 'Step 3: Swirl Thumbs & Fingertip Nails (20 Seconds Total!)', d: 'Hum a joyful birthday rhyme while twisting thumbs and swirling fingertips gently on opposite palms to clear sneaky germs under fingernails!' },
        4: { e: '🖐️✨', g: 'Microbes Remaining: 0% CLEAN!', gc: 'text-emerald-400 font-bold block', t: 'Step 4: Clean Flowing Rinse & Fresh Dry Cloth Towel', d: 'Rinse away all soap bubbles thoroughly under brief clear water and dry gently—ready safely for eating homemade meals and fresh fruit!' }
    };
    const s = map[step];
    if (!s) return;

    for (let i = 1; i <= 4; i++) {
        const b = document.getElementById('btn-ws-' + i);
        if (b) {
            b.className = (i === step)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    }
    document.getElementById('ws-emoji').textContent = s.e;
    document.getElementById('ws-germs').textContent = s.g;
    document.getElementById('ws-germs').className = s.gc;
    document.getElementById('ws-title').textContent = s.t;
    document.getElementById('ws-desc').textContent = s.d;
}
</script>
"""

# Simulator 3: Consistent Daily Routines
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📋</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Daily Wellness Routine &amp; Water-Glass Tracker</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Healthy Checklist</span>
    </div>

    <p class="text-xs text-slate-300">Inspect expected daily benchmarks keeping third-graders hydrated, strong, well-rested, and upbeat throughout school weeks!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectRoutine('water')" id="btn-rt-water" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">💧 6–8 Glasses Water</button>
        <button onclick="inspectRoutine('brush')" id="btn-rt-brush" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪥 Brush Twice</button>
        <button onclick="inspectRoutine('sleep')" id="btn-rt-sleep" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">😴 8+ Hours Sleep</button>
        <button onclick="inspectRoutine('play')" id="btn-rt-play" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">⚽ Outdoor Play</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="rtn-emoji">💧🥛</div>
        <div class="space-y-1">
            <h4 class="font-bold text-cyan-300 text-sm" id="rtn-title">6 to 8 Full Glasses of Clean Water Daily</h4>
            <p class="text-slate-300" id="rtn-desc">Sipping clean water steadily from morning until evening prevents dry throats, tiredness, and classroom headaches while keeping digestion smooth!</p>
        </div>
    </div>
</div>

<script>
function inspectRoutine(key) {
    const map = {
        water: { e: '💧🥛', t: '6 to 8 Full Glasses of Clean Water Daily', d: 'Sipping clean water steadily from morning until evening prevents dry throats, tiredness, and classroom headaches while keeping digestion smooth!' },
        brush: { e: '🪥✨', t: 'Morning + Bedtime Brushing (Twice Daily)', d: 'Nighttime brushing clears lingering dinner sugars away before sleep slows down saliva—shielding tooth enamel from acid cavities!' },
        sleep: { e: '😴🌙', t: 'At Least 8 Hours of Restful Night Sleep', d: 'Deep early sleep powers physical bone growth, heals active muscles, and files daytime school learning securely inside memory.' },
        play: { e: '⚽🌳', t: 'Daily Active Outdoor Playtime in Fresh Air', d: 'Running games under natural daylight strengthen beating hearts, deepen breathing lungs, and spark bright cheerful friendships!' }
    };
    const d = map[key];
    if (!d) return;

    ['water', 'brush', 'sleep', 'play'].forEach(k => {
        const b = document.getElementById('btn-rt-' + k);
        if (b) {
            b.className = (k === key)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('rtn-emoji').textContent = d.e;
    document.getElementById('rtn-title').textContent = d.t;
    document.getElementById('rtn-desc').textContent = d.d;
}
</script>
"""

# Simulator 4: Natural Neem Datun
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌿</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Traditional Neem/Babool Datun vs Plastic Toothbrush</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Eco Oral Hygiene</span>
    </div>

    <p class="text-xs text-slate-300">Compare traditional fresh neem and babool chewing twigs against plastic shop brushes for oral cleaning and planet waste!</p>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="compareOralTool('datun')" id="btn-oral-datun" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 text-left flex items-center gap-2">
            <span class="text-2xl">🌿</span>
            <div><span class="block">Fresh Neem / Babool Datun Twig</span><span class="text-[10px] text-emerald-200">Zero Plastic Waste Tradition</span></div>
        </button>
        <button onclick="compareOralTool('plastic')" id="btn-oral-plastic" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-2xl">🪥</span>
            <div><span class="block">Modern Plastic Toothbrush</span><span class="text-[10px] text-slate-400">Synthetic Landfill Waste</span></div>
        </button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <span class="text-emerald-400 font-bold block mb-1">Cleaning &amp; Gum Care:</span>
            <p id="oral-care" class="text-slate-300">Chewing the twig tip splits plant fibers into soft natural bristles that scrub food particles cleanly, gently massage gums, and release mild bitter antibacterial sap!</p>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <span class="text-amber-400 font-bold block mb-1">After-Use Earth Impact:</span>
            <p id="oral-earth" class="text-slate-300">Returns swiftly to garden soil compost—biodegrading completely into harmless earth humus with ZERO plastic pollution!</p>
        </div>
    </div>
</div>

<script>
function compareOralTool(tool) {
    const isDatun = (tool === 'datun');
    document.getElementById('btn-oral-datun').className = isDatun
        ? 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 text-left flex items-center gap-2'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';
    document.getElementById('btn-oral-plastic').className = !isDatun
        ? 'p-3 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left flex items-center gap-2'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';

    document.getElementById('oral-care').textContent = isDatun
        ? 'Chewing the twig tip splits plant fibers into soft natural bristles that scrub food particles cleanly, gently massage gums, and release mild bitter antibacterial sap!'
        : 'Soft synthetic bristles reach back molars easily when used gently with mild toothpaste—just remember to replace every 3 months and never share brushes!';
    document.getElementById('oral-earth').textContent = isDatun
        ? 'Returns swiftly to garden soil compost—biodegrading completely into harmless earth humus with ZERO plastic pollution!'
        : 'Discarded nylon plastic toothbrushes persist in garbage landfills for centuries unless recycled or swapped for bamboo handles!';
}
</script>
"""

# Simulator 5: Making Eco Cleaners (Activity 1 Natural Cleaner Studio)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🍊</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Activity 1: Homemade Citrus-Vinegar Eco Cleaner Lab</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Green Chemistry</span>
    </div>

    <p class="text-xs text-slate-300">Mix all four simple pantry steps cleanly in sequence to craft a safe, fragrant floor and bathroom cleaner without toxic fumes!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setCleanerStep(1)" id="btn-cl-1" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">1. Citrus Peels</button>
        <button onclick="setCleanerStep(2)" id="btn-cl-2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. Cloves / Bay</button>
        <button onclick="setCleanerStep(3)" id="btn-cl-3" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. White Vinegar</button>
        <button onclick="setCleanerStep(4)" id="btn-cl-4" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">4. Strain &amp; Clean</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 190" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Glass Jar -->
            <rect x="95" y="42" width="130" height="125" rx="14" fill="#0f172a" stroke="#94a3b8" stroke-width="3" />
            <rect x="112" y="28" width="96" height="14" rx="4" fill="#475569" />
            <!-- Liquid -->
            <rect id="cl-jar-liquid" x="100" y="75" width="120" height="87" rx="10" fill="#f59e0b" opacity="0.35" />
            <!-- Peels & Spices inside -->
            <text x="125" y="138" font-size="22">🍊</text>
            <text x="168" y="145" font-size="22">🍋</text>
            <text id="cl-spices-txt" x="148" y="112" font-size="18" opacity="0.25">🌿</text>
            <text x="160" y="182" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Glass Jar Bio-Infusion</text>
        </svg>

        <div class="space-y-2 text-xs">
            <h4 class="font-bold text-amber-300 text-sm" id="cl-step-title">Step 1: Fill Clean Glass Jar With Orange &amp; Lemon Peels</h4>
            <p class="text-slate-300 leading-relaxed" id="cl-step-desc">Instead of throwing away citrus skins, pack zesty orange or lemon rinds inside a clean jar! Their fragrant peel oils cut kitchen grease effortlessly.</p>
        </div>
    </div>
</div>

<script>
function setCleanerStep(step) {
    const map = {
        1: { op: '0.25', sp: '0.25', t: 'Step 1: Fill Clean Glass Jar With Orange & Lemon Peels', d: 'Instead of throwing away citrus skins, pack zesty orange or lemon rinds inside a clean jar! Their fragrant peel oils cut kitchen grease effortlessly.' },
        2: { op: '0.35', sp: '1', t: 'Step 2: Add Whole Aromatic Cloves or Crisp Bay Leaves', d: 'Drop in fragrant whole cloves or dried bay leaves to boost fresh herbal scent and natural germ-fighting power cleanly!' },
        3: { op: '0.70', sp: '1', t: 'Step 3: Submerge Completely With White Vinegar & Wait', d: 'Pour clear white vinegar completely over the peels and spices, seal tightly, and store inside cool shade for 2 weeks while citrus oils infuse smoothly!' },
        4: { op: '0.88', sp: '1', t: 'Step 4: Strain Into Spray Bottle & Polish Safely!', d: 'Dilute strained golden cleaner lightly with water to sparkle floors and bathroom tiles—leaving fresh citrus fragrance and ZERO toxic fumes!' }
    };
    const s = map[step];
    if (!s) return;

    for (let i = 1; i <= 4; i++) {
        const b = document.getElementById('btn-cl-' + i);
        if (b) {
            b.className = (i === step)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    }
    document.getElementById('cl-jar-liquid').setAttribute('opacity', s.op);
    document.getElementById('cl-spices-txt').setAttribute('opacity', s.sp);
    document.getElementById('cl-step-title').textContent = s.t;
    document.getElementById('cl-step-desc').textContent = s.d;
}
</script>
"""

# Simulator 6: Stronger Beating Hearts (Exercise & Heart/Lung Meter)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">❤️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Exercise Heartbeat &amp; Lung Oxygen Simulator</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Cardio Physiology</span>
    </div>

    <p class="text-xs text-slate-300">Switch between quiet sitting rest and outdoor playground sprinting to inspect how exercise strengthens your tireless heart pump!</p>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="setHeartMode('rest')" id="btn-hr-rest" class="p-3 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left flex items-center gap-2">
            <span class="text-2xl">🪑</span>
            <div><span class="block">Quiet Bench Resting</span><span class="text-[10px] text-cyan-200">Steady Slow Beat (~75 BPM)</span></div>
        </button>
        <button onclick="setHeartMode('sprint')" id="btn-hr-sprint" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-2xl">🏃</span>
            <div><span class="block">Outdoor Park Sprinting</span><span class="text-[10px] text-slate-400">Strong Fast Beat (~130 BPM)</span></div>
        </button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 sm:grid-cols-3 gap-3 text-center text-xs">
        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <div class="text-3xl mb-1" id="hr-heart-icon">❤️</div>
            <span class="text-slate-400 block text-[10px]">Heart Pump Rhythm:</span>
            <span id="hr-bpm" class="text-lg font-extrabold text-cyan-300">75 Beats / Min</span>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <div class="text-3xl mb-1" id="hr-lung-icon">🫁</div>
            <span class="text-slate-400 block text-[10px]">Oxygen Inhalation:</span>
            <span id="hr-breath" class="text-lg font-extrabold text-emerald-300">Calm Even Breaths</span>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <div class="text-3xl mb-1" id="hr-mood-icon">😊</div>
            <span class="text-slate-400 block text-[10px]">Fitness Benefit:</span>
            <span id="hr-benefit" class="text-xs font-bold text-amber-300 block mt-1">Conserves Calm Energy</span>
        </div>
    </div>
</div>

<script>
function setHeartMode(mode) {
    const isSprint = (mode === 'sprint');
    document.getElementById('btn-hr-rest').className = !isSprint
        ? 'p-3 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left flex items-center gap-2'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';
    document.getElementById('btn-hr-sprint').className = isSprint
        ? 'p-3 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500 text-left flex items-center gap-2'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';

    document.getElementById('hr-heart-icon').textContent = isSprint ? '💓' : '❤️';
    document.getElementById('hr-bpm').textContent = isSprint ? '130 Beats / Min!' : '75 Beats / Min';
    document.getElementById('hr-bpm').className = isSprint ? 'text-lg font-extrabold text-rose-400' : 'text-lg font-extrabold text-cyan-300';
    document.getElementById('hr-breath').textContent = isSprint ? 'Deep Rapid O2 Pulls!' : 'Calm Even Breaths';
    document.getElementById('hr-mood-icon').textContent = isSprint ? '🤩' : '😊';
    document.getElementById('hr-benefit').textContent = isSprint
        ? 'Trains Stronger Heart & Builds Vitamin D!'
        : 'Conserves Calm Energy';
}
</script>
"""

# Simulator 7: Playful Animal Movements (Activity 2 Fitness Studio)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🐸</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Activity 2: Animal Fitness &amp; Skipping Rhyme Arena</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Active Body</span>
    </div>

    <p class="text-xs text-slate-300">Select each playful animal exercise to practice posture steps and see which muscles and balance skills grow stronger!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectMove('duck')" id="btn-mv-duck" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">🦆 Duck Walk</button>
        <button onclick="selectMove('frog')" id="btn-mv-frog" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🐸 Frog Jump</button>
        <button onclick="selectMove('cat')" id="btn-mv-cat" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🐈 Cat Run</button>
        <button onclick="selectMove('rope')" id="btn-mv-rope" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">➰ Skipping Rope</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="mv-emoji">🦆</div>
        <div class="space-y-1">
            <h4 class="font-bold text-emerald-300 text-sm" id="mv-title">Duck Walk — Thigh Strength &amp; Balance Control</h4>
            <p class="text-slate-300" id="mv-desc">Squat smoothly low with bent knees, tuck hands beneath shoulders like flapping pond wings, and waddle briskly across soft grass to fire thigh endurance!</p>
        </div>
    </div>
</div>

<script>
function selectMove(mv) {
    const map = {
        duck: { e: '🦆', t: 'Duck Walk — Thigh Strength & Balance Control', d: 'Squat smoothly low with bent knees, tuck hands beneath shoulders like flapping pond wings, and waddle briskly across soft grass to fire thigh endurance!' },
        frog: { e: '🐸', t: 'Frog Jump — Explosive Leg Spring Power', d: 'Crouch gently with fingertips touching soft turf, then launch brightly upward into safe playful bounds—building sturdy ankles and springy leg power!' },
        cat: { e: '🐈', t: 'Cat Run — Nimble Shoulder & Spine Flexibility', d: 'Scurry swiftly forward upon palms and tiptoes while arching backs softly like agile cats—strengthening upper arm bones and total body coordination!' },
        rope: { e: '➰', t: 'Skipping Rope Rhymes — Heart Cardio & Team Timing', d: 'Leap cleanly on the balls of your feet over swirling ropes while friends chant cheerful rhythmic rhymes—training endurance, ear-foot timing, and joy!' }
    };
    const d = map[mv];
    if (!d) return;

    ['duck', 'frog', 'cat', 'rope'].forEach(k => {
        const b = document.getElementById('btn-mv-' + k);
        if (b) {
            b.className = (k === mv)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('mv-emoji').textContent = d.e;
    document.getElementById('mv-title').textContent = d.t;
    document.getElementById('mv-desc').textContent = d.d;
}
</script>
"""

# Simulator 8: Sharp Mind Games
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">♟️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Grandmother's Indoor Board Game Brain Gym</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Active Mind</span>
    </div>

    <p class="text-xs text-slate-300">Inspect classic indoor board games that keep sharp minds busy during rainy afternoons or midday summer heat!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="inspectGame('chess')" id="btn-gm-chess" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">♟️ Strategy Chess</button>
        <button onclick="inspectGame('carrom')" id="btn-gm-carrom" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🎯 Carrom Board</button>
        <button onclick="inspectGame('snakes')" id="btn-gm-snakes" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🎲 Snakes &amp; Ladders</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="gm-emoji">♟️🧠</div>
        <div class="space-y-1">
            <h4 class="font-bold text-amber-300 text-sm" id="gm-title">Chess — Logic Foresight &amp; Calm Concentration</h4>
            <p class="text-slate-300" id="gm-desc">Thinking three clever moves ahead across 64 black-and-white squares sharpens spatial reasoning, patience, problem solving, and polite sportsmanship!</p>
        </div>
    </div>
</div>

<script>
function inspectGame(gm) {
    const map = {
        chess: { e: '♟️🧠', t: 'Chess — Logic Foresight & Calm Concentration', d: 'Thinking three clever moves ahead across 64 black-and-white squares sharpens spatial reasoning, patience, problem solving, and polite sportsmanship!' },
        carrom: { e: '🎯🪵', t: 'Carrom — Precision Aim & Hand-Eye Focus', d: 'Flicking smooth strikers across fine boric powder teaches steady finger control, geometry angles, and friendly turn-taking!' },
        snakes: { e: '🎲🪜', t: 'Snakes & Ladders — Number Counting & Emotional Resilience', d: 'Counting rolled dice steps builds swift arithmetic while laughing gracefully whenever a playful snake slides pieces down teaches emotional resilience!' }
    };
    const d = map[gm];
    if (!d) return;

    ['chess', 'carrom', 'snakes'].forEach(k => {
        const b = document.getElementById('btn-gm-' + k);
        if (b) {
            b.className = (k === gm)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('gm-emoji').textContent = d.e;
    document.getElementById('gm-title').textContent = d.t;
    document.getElementById('gm-desc').textContent = d.d;
}
</script>
"""

if __name__ == "__main__":
    print(f"Generated {len(simulators_part1)} simulators for Part 1 (1 to 8).")
    for k in sorted(simulators_part1.keys()):
        print(f"Sim {k}: {len(simulators_part1[k])} chars")
