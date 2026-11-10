#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 6: Living in Harmony
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Shared Human Homes (Invited Pets vs Uninvited Visitors)
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏡</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Shared Domestic Space Explorer</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Coexistence Lab</span>
    </div>

    <p class="text-xs text-slate-300">Toggle between cared domestic pets and wild uninvited visitors to explore how humans and animals share indoor and courtyard living spaces!</p>

    <!-- Category Toggle Buttons -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="toggleHomeCreatures('pets')" id="btn-home-pets" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left">
            <span class="text-2xl">🐕</span>
            <div>
                <span class="text-xs block">Invited Domestic Companions</span>
                <span class="text-[10px] text-emerald-200">Cared with Food, Water & Shelter</span>
            </div>
        </button>
        <button onclick="toggleHomeCreatures('visitors')" id="btn-home-visitors" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🦎</span>
            <div>
                <span class="text-xs block">Uninvited Wild Visitors</span>
                <span class="text-[10px] text-slate-400">Seeking Warmth, Crumbs & Insects</span>
            </div>
        </button>
    </div>

    <!-- House Cutaway SVG Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800">
        <svg viewBox="0 0 700 240" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- House Outline -->
            <polygon points="120,70 350,15 580,70" fill="#1e293b" stroke="#475569" stroke-width="3" />
            <rect x="150" y="70" width="400" height="150" fill="#0f172a" stroke="#334155" stroke-width="3" rx="6" />

            <!-- Roof Eaves (Sparrow Nesting Zone) -->
            <rect x="140" y="66" width="420" height="8" fill="#475569" />

            <!-- Room Division -->
            <line x1="350" y1="70" x2="350" y2="220" stroke="#1e293b" stroke-width="2" stroke-dasharray="4,4" />

            <!-- Windows & Door -->
            <rect x="180" y="100" width="60" height="50" rx="4" fill="#38bdf8" opacity="0.25" stroke="#0284c7" stroke-width="2" />
            <rect x="460" y="100" width="60" height="50" rx="4" fill="#38bdf8" opacity="0.25" stroke="#0284c7" stroke-width="2" />
            <rect x="320" y="140" width="60" height="80" rx="4" fill="#78350f" stroke="#92400e" stroke-width="2" />

            <!-- Group A: Invited Pets View (Default) -->
            <g id="view-pets-group">
                <!-- Pet Dog in Courtyard -->
                <g transform="translate(210, 160)">
                    <text x="0" y="30" font-size="40">🐕</text>
                    <text x="-15" y="48" font-size="10" fill="#86efac" font-weight="bold">Pet Dog (Cared)</text>
                </g>
                <!-- Gentle Cat on Rug -->
                <g transform="translate(450, 165)">
                    <text x="0" y="25" font-size="34">🐈</text>
                    <text x="-15" y="45" font-size="10" fill="#86efac" font-weight="bold">Cat on Rug</text>
                </g>
                <!-- Milking Cow in Shed -->
                <g transform="translate(50, 140)">
                    <text x="0" y="45" font-size="44">🐄</text>
                    <text x="-10" y="68" font-size="10" fill="#86efac" font-weight="bold">Courtyard Cow</text>
                </g>
            </g>

            <!-- Group B: Uninvited Visitors View (Hidden initially) -->
            <g id="view-visitors-group" class="hidden">
                <!-- Wall Gecko near ceiling lamp -->
                <g transform="translate(260, 95)">
                    <text x="0" y="0" font-size="28">🦎</text>
                    <text x="-25" y="18" font-size="10" fill="#fde047" font-weight="bold">Wall Gecko (Moth Hunter)</text>
                </g>
                <!-- Sparrow nesting under roof rafters -->
                <g transform="translate(360, 60)">
                    <text x="0" y="0" font-size="24">🐦</text>
                    <text x="25" y="0" font-size="10" fill="#fde047" font-weight="bold">Sparrow in Eaves</text>
                </g>
                <!-- Worker Ants on floor -->
                <g transform="translate(370, 205)">
                    <text x="0" y="0" font-size="16">🐜 🐜 🐜</text>
                    <text x="50" y="0" font-size="10" fill="#fde047" font-weight="bold">Ants Gathering Crumbs</text>
                </g>
                <!-- Balcony Pigeon -->
                <g transform="translate(510, 85)">
                    <text x="0" y="0" font-size="24">🕊️</text>
                    <text x="-20" y="18" font-size="10" fill="#fde047" font-weight="bold">Balcony Pigeon</text>
                </g>
            </g>
        </svg>

        <div id="home-coexist-feedback" class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-emerald-500/30 text-xs text-slate-200">
            <strong>Invited Domestic Companions:</strong> Dogs, cats, and cows are welcomed members of human homes. We provide them with nutritious food, clean water, warm bedding, and healthcare.
        </div>
    </div>
</div>

<script>
function toggleHomeCreatures(type) {
    const btnPets = document.getElementById('btn-home-pets');
    const btnVis = document.getElementById('btn-home-visitors');
    const viewPets = document.getElementById('view-pets-group');
    const viewVis = document.getElementById('view-visitors-group');
    const feedback = document.getElementById('home-coexist-feedback');

    if (type === 'pets') {
        btnPets.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        btnVis.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
        viewPets.classList.remove('hidden');
        viewVis.classList.add('hidden');
        feedback.innerHTML = '<strong>Invited Domestic Companions:</strong> Dogs, cats, and cows are welcomed members of human households. We care for them lovingly with daily meals, clean water, and safe shelter!';
    } else if (type === 'visitors') {
        btnVis.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        btnPets.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
        viewPets.classList.add('hidden');
        viewVis.classList.remove('hidden');
        feedback.innerHTML = '<strong>Uninvited Wild Visitors:</strong> Geckos, sparrows, and ants share our homes peacefully. Geckos hunt nocturnal mosquitoes, sparrows nest in roof eaves, and ants clean up food crumbs!';
    }
}
</script>
"""

# Simulator 2: Kindness Toward Creatures (Kindness Sanctuary)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">💛</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Everyday Compassion & Kindness Lab</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Non-Cruelty Action Lab</span>
    </div>

    <p class="text-xs text-slate-300">Click each compassionate action button to care for dehydrated birds, release wandering insects, and provide comforting shade!</p>

    <!-- Compassion Action Buttons -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
        <button onclick="performKindness('water')" id="btn-kind-water" class="p-3 rounded-xl bg-slate-900 hover:bg-emerald-950/60 border border-slate-700 hover:border-emerald-600 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🥣</span>
            <div>
                <span class="text-xs font-bold text-white block">Earthen Water Bowl</span>
                <span class="text-[10px] text-slate-400">Save Dehydrated Birds</span>
            </div>
        </button>
        <button onclick="performKindness('moth')" id="btn-kind-moth" class="p-3 rounded-xl bg-slate-900 hover:bg-emerald-950/60 border border-slate-700 hover:border-emerald-600 transition flex items-center gap-3 text-left">
            <span class="text-2xl">📦</span>
            <div>
                <span class="text-xs font-bold text-white block">Cup & Release Moth</span>
                <span class="text-[10px] text-slate-400">Gentle Non-Violence</span>
            </div>
        </button>
        <button onclick="performKindness('shade')" id="btn-kind-shade" class="p-3 rounded-xl bg-slate-900 hover:bg-emerald-950/60 border border-slate-700 hover:border-emerald-600 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🌳</span>
            <div>
                <span class="text-xs font-bold text-white block">Courtyard Shade & Water</span>
                <span class="text-[10px] text-slate-400">Comfort for Stray Animals</span>
            </div>
        </button>
    </div>

    <!-- Animated Compassion Meter & Garden Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800">
        <div class="flex items-center justify-between text-xs mb-2">
            <span class="font-bold text-slate-300">Everyday Compassion Meter: <span id="kindness-pct" class="text-emerald-400 font-extrabold">35%</span></span>
            <span id="kindness-badge-text" class="text-xs font-bold text-cyan-400">Caring Citizen</span>
        </div>
        <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden mb-3">
            <div id="kindness-bar" class="bg-gradient-to-r from-emerald-500 via-teal-400 to-amber-400 h-2 w-[35%] transition-all duration-300"></div>
        </div>

        <svg viewBox="0 0 700 220" class="w-full h-auto rounded-xl bg-gradient-to-b from-sky-950 to-emerald-950/80 border border-slate-800">
            <!-- Balcony / Terrace Wall -->
            <rect x="0" y="160" width="700" height="60" fill="#334155" stroke="#475569" stroke-width="2" />

            <!-- Earthen Water Bowl Zone -->
            <g id="bowl-graphic" transform="translate(180, 135)" opacity="0.4">
                <ellipse cx="0" cy="20" rx="35" ry="14" fill="#78350f" stroke="#92400e" stroke-width="2" />
                <ellipse cx="0" cy="17" rx="30" ry="10" fill="#38bdf8" />
                <!-- Drinking Bird -->
                <text x="15" y="15" font-size="28">🕊️</text>
                <text x="-45" y="48" font-size="10" fill="#38bdf8" font-weight="bold">Cool Water Bowl</text>
            </g>

            <!-- Cardboard Cup Moth Release -->
            <g id="moth-release-graphic" transform="translate(360, 110)" opacity="0.4">
                <rect x="-15" y="20" width="30" height="35" rx="4" fill="#d97706" />
                <text x="-12" y="10" font-size="24">🦋</text>
                <text x="-40" y="70" font-size="10" fill="#fde047" font-weight="bold">Gentle Cup Release</text>
            </g>

            <!-- Shady Tree & Rest Zone -->
            <g id="shade-dog-graphic" transform="translate(540, 100)" opacity="0.4">
                <!-- Tree Canopy -->
                <ellipse cx="0" cy="20" rx="55" ry="35" fill="#15803d" />
                <!-- Resting Dog -->
                <text x="-20" y="65" font-size="34">🐕</text>
                <text x="-35" y="85" font-size="10" fill="#86efac" font-weight="bold">Resting in Shade</text>
            </g>
        </svg>

        <div id="kindness-feedback" class="mt-2 text-xs text-emerald-300 font-medium">
            <strong>Compassion in Action:</strong> Select an action above to practice non-cruelty and protect living creatures in your neighborhood!
        </div>
    </div>
</div>

<script>
let kindnessScore = 35;

function performKindness(act) {
    const feedback = document.getElementById('kindness-feedback');
    const bar = document.getElementById('kindness-bar');
    const pct = document.getElementById('kindness-pct');
    const badge = document.getElementById('kindness-badge-text');

    const bowlGfx = document.getElementById('bowl-graphic');
    const mothGfx = document.getElementById('moth-release-graphic');
    const shadeGfx = document.getElementById('shade-dog-graphic');

    if (act === 'water') {
        bowlGfx.style.opacity = '1';
        kindnessScore = Math.min(100, kindnessScore + 25);
        feedback.innerHTML = '<strong>Earthen Bowl Placed!</strong> You placed clean water in the shade! Thirsty pigeons, mynas, and honeybees drink safely and escape heat exhaustion!';
    } else if (act === 'moth') {
        mothGfx.style.opacity = '1';
        kindnessScore = Math.min(100, kindnessScore + 25);
        feedback.innerHTML = '<strong>Gentle Release:</strong> Instead of crushing the trapped moth, you safely trapped it in a cup and let it flutter peacefully back into the outdoor garden!';
    } else if (act === 'shade') {
        shadeGfx.style.opacity = '1';
        kindnessScore = Math.min(100, kindnessScore + 25);
        feedback.innerHTML = '<strong>Courtyard Sanctuary:</strong> You welcomed a stray dog with quiet shade and a bowl of fresh water, showing respect and non-cruelty!';
    }

    bar.style.width = kindnessScore + '%';
    pct.textContent = kindnessScore + '%';
    if (kindnessScore >= 80) {
        badge.textContent = '🌟 Earth Harmony Champion!';
    }
}
</script>
"""

# Simulator 3: Mango Tree Secrets (Monkey Eating Mango & Seed Drop)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🥭</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Mango Orchard Partnership Simulator</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Mutual Seed Dispersal</span>
    </div>

    <p class="text-xs text-slate-300">Click the buttons to watch the monkey feast on a sweet golden mango and drop the seed core, planting tomorrow's mango grove!</p>

    <!-- Interactive Step Buttons -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="mangoStep(1)" id="btn-mango-1" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left">
            <span class="text-2xl">🌿</span>
            <div>
                <span class="text-xs block">Step 1: Pluck Mango</span>
                <span class="text-[10px] text-emerald-200">Sweet Golden Reward</span>
            </div>
        </button>
        <button onclick="mangoStep(2)" id="btn-mango-2" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🐒</span>
            <div>
                <span class="text-xs block">Step 2: Savor Pulp</span>
                <span class="text-[10px] text-slate-400">Nutritious Fruit Feast</span>
            </div>
        </button>
        <button onclick="mangoStep(3)" id="btn-mango-3" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🌱</span>
            <div>
                <span class="text-xs block">Step 3: Drop Seed Core</span>
                <span class="text-[10px] text-slate-400">Sprout New Sapling</span>
            </div>
        </button>
    </div>

    <!-- Animated Orchard SVG -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 230" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Ground -->
            <rect x="0" y="170" width="700" height="60" fill="#14532d" />
            <!-- Grand Mango Tree Trunk -->
            <path d="M 180 70 L 160 230 L 240 230 L 220 70 Z" fill="#78350f" stroke="#92400e" stroke-width="3" />
            <!-- Canopy Foliage -->
            <ellipse cx="200" cy="65" rx="140" ry="55" fill="#15803d" stroke="#22c55e" stroke-width="2" />
            <ellipse cx="230" cy="50" rx="100" ry="40" fill="#16a34a" />

            <!-- Golden Mangoes on Tree -->
            <g id="hanging-mangoes">
                <text x="140" y="80" font-size="22">🥭</text>
                <text x="210" y="95" font-size="22">🥭</text>
                <text x="280" y="75" font-size="22">🥭</text>
            </g>

            <!-- Monkey on Branch -->
            <g id="orchard-monkey" transform="translate(230, 45)">
                <text x="0" y="30" font-size="44">🐒</text>
                <!-- Plucked Mango in Hand -->
                <text id="monkey-mango" x="35" y="25" font-size="20">🥭</text>
            </g>

            <!-- Falling Seed Animation Group -->
            <g id="falling-seed-grp" transform="translate(280, 85)" opacity="0">
                <ellipse cx="0" cy="0" rx="12" ry="7" fill="#fde047" stroke="#ca8a04" stroke-width="1.5" />
                <line x1="0" y1="-25" x2="0" y2="25" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3,3" />
                <text x="18" y="5" font-size="11" fill="#fde047" font-weight="bold">Discarded Seed</text>
            </g>

            <!-- New Sprouted Sapling on Ground -->
            <g id="sprouted-mango-sapling" transform="translate(380, 160)" opacity="0">
                <path d="M 0 15 L 0 0" stroke="#16a34a" stroke-width="3" />
                <text x="-12" y="0" font-size="22">🌱</text>
                <text x="-40" y="30" font-size="11" fill="#86efac" font-weight="bold">New Mango Sapling!</text>
            </g>

            <!-- Child and Elder Sitting Under Shade -->
            <g transform="translate(70, 160)">
                <text x="0" y="0" font-size="30">🧒</text>
                <text x="35" y="0" font-size="30">🧔</text>
                <text x="-25" y="25" font-size="10" fill="#86efac" font-weight="bold">Observing Nature's Wisdom</text>
            </g>
        </svg>

        <div id="mango-feedback" class="mt-2 text-xs text-emerald-300 font-medium">
            <strong>Step 1 Active:</strong> The mango tree produces sweet golden fruits as an evolutionary gift, enticing the monkey up into its shady branches!
        </div>
    </div>
</div>

<script>
function mangoStep(step) {
    for (let i = 1; i <= 3; i++) {
        const btn = document.getElementById(`btn-mango-${i}`);
        if (btn) {
            if (i === step) {
                btn.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
            } else {
                btn.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
            }
        }
    }

    const monkeyMango = document.getElementById('monkey-mango');
    const fallingSeed = document.getElementById('falling-seed-grp');
    const sapling = document.getElementById('sprouted-mango-sapling');
    const feedback = document.getElementById('mango-feedback');

    if (step === 1) {
        monkeyMango.style.opacity = '1';
        fallingSeed.style.opacity = '0';
        sapling.style.opacity = '0';
        feedback.innerHTML = '<strong>Step 1: Plucking the Fruit:</strong> The monkey plucks a sweet golden mango from the lush canopy, rewarded by the tree for visiting!';
    } else if (step === 2) {
        monkeyMango.style.opacity = '0.5';
        fallingSeed.style.opacity = '0';
        sapling.style.opacity = '0';
        feedback.innerHTML = '<strong>Step 2: Savoring Sweet Pulp:</strong> The monkey eats the juicy yellow pulp, gaining energy and water while leaving the tough seed core undamaged.';
    } else if (step === 3) {
        monkeyMango.style.opacity = '0';
        fallingSeed.style.opacity = '1';
        sapling.style.opacity = '1';
        feedback.innerHTML = '<strong>Step 3: Seed Dropped & Sprouting:</strong> The monkey drops the seed core onto sunny soil far from the tree canopy, where rain germinates it into a brand-new mango tree!';
    }
}
</script>
"""

# Simulator 4: Seed Germination Cycles (Waking the Sleeping Embryo)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌱</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Seed Germination Trigger Lab</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">4 Essential Triggers</span>
    </div>

    <p class="text-xs text-slate-300">Click the environmental triggers to provide moisture, gentle sun warmth, and aerated soil to awaken the sleeping seed embryo!</p>

    <!-- Trigger Toggle Controls -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="triggerGermination('water')" id="btn-trig-water" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">💧</span>
            <div>
                <span class="text-xs block">1. Add Rain Moisture</span>
                <span class="text-[10px] text-slate-400">Softens Hard Seed Coat</span>
            </div>
        </button>
        <button onclick="triggerGermination('warmth')" id="btn-trig-warmth" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">☀️</span>
            <div>
                <span class="text-xs block">2. Add Gentle Warmth</span>
                <span class="text-[10px] text-slate-400">Activates Growth Enzymes</span>
            </div>
        </button>
        <button onclick="triggerGermination('air')" id="btn-trig-air" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">💨</span>
            <div>
                <span class="text-xs block">3. Soil Oxygen Pores</span>
                <span class="text-[10px] text-slate-400">Cellular Respiration</span>
            </div>
        </button>
    </div>

    <!-- Seed Growth Stages SVG -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 230" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Soil Horizon -->
            <rect x="0" y="110" width="700" height="120" fill="#2d1500" stroke="#78350f" stroke-width="2" />
            <rect x="0" y="95" width="700" height="15" fill="#14532d" />

            <!-- Seed Coat Body -->
            <g id="seed-embryo-body" transform="translate(350, 130)">
                <!-- Split Seed Cotyledon -->
                <ellipse cx="0" cy="0" rx="28" ry="18" fill="#d97706" stroke="#b45309" stroke-width="2" />
                <path d="M 0 -18 L 0 18" stroke="#78350f" stroke-width="2" stroke-dasharray="2,2" />

                <!-- Downward Radicle (Root) -->
                <path id="germ-radicle" d="M 0 10 Q -10 40 -15 65" stroke="#f8fafc" stroke-width="4" fill="none" stroke-linecap="round" opacity="0" />

                <!-- Upward Plumule (Shoot & Leaves) -->
                <g id="germ-plumule" opacity="0">
                    <path d="M 0 -10 Q 5 -45 0 -70" stroke="#22c55e" stroke-width="4" fill="none" stroke-linecap="round" />
                    <!-- First Baby Leaves -->
                    <ellipse cx="-12" cy="-70" rx="14" ry="6" fill="#16a34a" transform="rotate(-30, -12, -70)" />
                    <ellipse cx="12" cy="-70" rx="14" ry="6" fill="#16a34a" transform="rotate(30, 12, -70)" />
                </g>
            </g>

            <!-- Rain Droplets Graphic -->
            <g id="water-drops-gfx" opacity="0">
                <text x="320" y="70" font-size="16">💧</text>
                <text x="360" y="60" font-size="16">💧</text>
            </g>

            <!-- Gentle Sun Graphic -->
            <g id="sun-warmth-gfx" opacity="0">
                <circle cx="560" cy="50" r="28" fill="#fef08a" stroke="#f59e0b" stroke-width="2" />
                <text x="540" y="95" font-size="11" fill="#fde047" font-weight="bold">Gentle Warmth ☀️</text>
            </g>
        </svg>

        <div id="germination-feedback" class="mt-2 text-xs text-emerald-300 font-medium">
            <strong>Dormant Seed:</strong> The seed contains an embryo and stored cotyledon food. Provide moisture, warmth, and air to awaken it!
        </div>
    </div>
</div>

<script>
let hasWater = false;
let hasWarmth = false;
let hasAir = false;

function triggerGermination(trigger) {
    const btnWater = document.getElementById('btn-trig-water');
    const btnWarmth = document.getElementById('btn-trig-warmth');
    const btnAir = document.getElementById('btn-trig-air');
    const radicle = document.getElementById('germ-radicle');
    const plumule = document.getElementById('germ-plumule');
    const waterGfx = document.getElementById('water-drops-gfx');
    const sunGfx = document.getElementById('sun-warmth-gfx');
    const feedback = document.getElementById('germination-feedback');

    if (trigger === 'water') {
        hasWater = true;
        btnWater.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        waterGfx.style.opacity = '1';
        radicle.style.opacity = '1';
        feedback.innerHTML = '<strong>Water Absorbed:</strong> The tough seed coat swells, cracks open, and the embryonic root (radicle) emerges to anchor into the soil!';
    } else if (trigger === 'warmth') {
        hasWarmth = true;
        btnWarmth.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        sunGfx.style.opacity = '1';
        if (hasWater) {
            plumule.style.opacity = '0.6';
            feedback.innerHTML = '<strong>Warmth Energizes:</strong> Gentle sun warmth activates growth enzymes! The green shoot (plumule) begins pushing upward toward the sky.';
        }
    } else if (trigger === 'air') {
        hasAir = true;
        btnAir.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        if (hasWater && hasWarmth) {
            plumule.style.opacity = '1';
            feedback.innerHTML = '<strong>Full Germination Complete!</strong> With moisture, warmth, and soil oxygen, the seedling unfolds its first green leaves and begins independent photosynthesis!';
        }
    }
}
</script>
"""

# Simulator 5: Bountiful Plant Gifts (Botanical Tree of Life)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎁</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Bountiful Plant Gifts Explorer</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">5 Vital Offerings</span>
    </div>

    <p class="text-xs text-slate-300">Click on each category of plant gifts to see how human civilization and forest animals depend entirely on botanical resources!</p>

    <!-- Gift Selectors -->
    <div class="grid grid-cols-2 sm:grid-cols-5 gap-2">
        <button onclick="exploreGift('oxygen')" id="btn-gift-oxygen" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex flex-col items-center gap-1">
            <span>💨 Oxygen Gas</span>
            <span class="text-[10px] text-emerald-200">Breath of Life</span>
        </button>
        <button onclick="exploreGift('food')" id="btn-gift-food" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🌾 Food Crops</span>
            <span class="text-[10px] text-slate-400">Grains, Veg & Fruits</span>
        </button>
        <button onclick="exploreGift('timber')" id="btn-gift-timber" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🪵 Wood & Timber</span>
            <span class="text-[10px] text-slate-400">Homes & School Desks</span>
        </button>
        <button onclick="exploreGift('fiber')" id="btn-gift-fiber" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🧵 Plant Fibers</span>
            <span class="text-[10px] text-slate-400">Cotton & Jute Bags</span>
        </button>
        <button onclick="exploreGift('medicine')" id="btn-gift-medicine" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🌿 Healing Herbs</span>
            <span class="text-[10px] text-slate-400">Tulsi & Neem</span>
        </button>
    </div>

    <!-- Animated Gift Showcase Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800">
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 items-center">
            <!-- Center Tree Graphic -->
            <div class="sm:col-span-1 text-center bg-slate-950 p-3 rounded-xl border border-slate-800">
                <span class="text-6xl block">🌳</span>
                <span class="text-xs font-bold text-emerald-400 mt-2 block">Living Tree of Life</span>
            </div>

            <!-- Dynamic Gift Details Display -->
            <div class="sm:col-span-2 space-y-2">
                <div class="p-3 rounded-xl bg-slate-950/80 border border-emerald-500/30">
                    <span id="gift-detail-title" class="text-xs font-bold text-emerald-400 uppercase tracking-wider block">💨 Oxygen Generation & Air Purification</span>
                    <p id="gift-detail-desc" class="text-xs text-slate-200 mt-1">
                        Through photosynthesis, green plant leaves absorb atmospheric carbon dioxide and release life-sustaining oxygen gas, powering the respiration of every human and animal.
                    </p>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-950/60 border border-slate-800 flex items-center justify-between text-xs">
                    <span class="text-slate-400">Ecological Value:</span>
                    <span id="gift-detail-value" class="text-cyan-400 font-extrabold">Fundamental Biosphere Lifeline</span>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
function exploreGift(gift) {
    const gifts = ['oxygen', 'food', 'timber', 'fiber', 'medicine'];
    gifts.forEach(g => {
        const btn = document.getElementById(`btn-gift-${g}`);
        if (btn) {
            if (g === gift) {
                btn.className = 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex flex-col items-center gap-1';
            } else {
                btn.className = 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1';
            }
        }
    });

    const titleEl = document.getElementById('gift-detail-title');
    const descEl = document.getElementById('gift-detail-desc');
    const valEl = document.getElementById('gift-detail-value');

    if (gift === 'oxygen') {
        titleEl.textContent = '💨 Oxygen Generation & Air Purification';
        descEl.textContent = 'Through photosynthesis, green plant leaves absorb atmospheric carbon dioxide and release life-sustaining oxygen gas, powering the respiration of every human and animal.';
        valEl.textContent = 'Fundamental Biosphere Lifeline';
    } else if (gift === 'food') {
        titleEl.textContent = '🌾 Wholesome Food Crops & Nutrition';
        descEl.textContent = 'Plants provide all foundational calories: staple grains (wheat, rice), lentils, protein-rich pulses, succulent garden vegetables, nuts, and sweet seasonal fruits.';
        valEl.textContent = 'Global Nutritional Sustenance';
    } else if (gift === 'timber') {
        titleEl.textContent = '🪵 Sustainable Timber & Wooden Shelter';
        descEl.textContent = 'Sturdy wood from sustainably harvested trees builds homes, roof beams, doors, tables, chairs, and classroom desks, providing durable, renewable building material.';
        valEl.textContent = 'Shelter & Architecture';
    } else if (gift === 'fiber') {
        titleEl.textContent = '🧵 Botanical Fibers: Cotton & Jute';
        descEl.textContent = 'Soft cotton harvested from plant seed bolls weaves cool summer clothes, while tough bast fibers from jute stems weave eco-friendly, biodegradable shopping bags.';
        valEl.textContent = 'Clothing & Sustainable Packaging';
    } else if (gift === 'medicine') {
        titleEl.textContent = '🌿 Medicinal Plants: Tulsi, Neem & Ginger';
        descEl.textContent = 'Traditional Ayurvedic medicines and modern pharmaceuticals utilize natural bioactive compounds from tulsi, neem, and ginger to soothe coughs, heal wounds, and fight infections.';
        valEl.textContent = 'Natural Healing & Healthcare';
    }
}
</script>
"""

# Simulator 6: Tree Canopy Shelter (Multistory Tree Apartment)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏢</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Tree Canopy Multistory Apartment</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Vertical Wildlife Suites</span>
    </div>

    <p class="text-xs text-slate-300">Click each vertical suite to discover how a single mature forest tree shelters different wild creatures across its levels!</p>

    <!-- Suite Selector Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectTreeSuite('canopy')" id="btn-suite-canopy" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex flex-col items-center gap-1">
            <span>🌿 Top Canopy</span>
            <span class="text-[10px] text-emerald-200">Tailorbirds & Sunbirds</span>
        </button>
        <button onclick="selectTreeSuite('fork')" id="btn-suite-fork" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🪵 Branch Forks</span>
            <span class="text-[10px] text-slate-400">Leopards & Fruit Bats</span>
        </button>
        <button onclick="selectTreeSuite('hollow')" id="btn-suite-hollow" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🕳️ Trunk Hollows</span>
            <span class="text-[10px] text-slate-400">Owlets & Squirrels</span>
        </button>
        <button onclick="selectTreeSuite('bark')" id="btn-suite-bark" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🦎 Bark Crevices</span>
            <span class="text-[10px] text-slate-400">Geckos & Beetles</span>
        </button>
    </div>

    <!-- Cutaway Tree SVG -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800">
        <svg viewBox="0 0 700 230" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Sky Background -->
            <rect x="0" y="0" width="700" height="230" fill="#0c4a6e" opacity="0.3" />

            <!-- Tree Structure -->
            <rect x="310" y="70" width="80" height="160" fill="#78350f" stroke="#92400e" stroke-width="3" />
            <path d="M 120 90 Q 350 20 580 90 Q 640 140 500 130 Q 350 140 200 130 Q 60 140 120 90 Z" fill="#15803d" stroke="#22c55e" stroke-width="2" />

            <!-- High Foliage Suite -->
            <g id="suite-canopy-gfx" class="cursor-pointer" onclick="selectTreeSuite('canopy')">
                <circle cx="240" cy="80" r="26" fill="#16a34a" stroke="#86efac" stroke-width="2" stroke-dasharray="3,3" />
                <text x="225" y="90" font-size="26">🐦</text>
                <text x="210" y="118" font-size="10" fill="#86efac" font-weight="bold">Canopy Nests</text>
            </g>

            <!-- Branch Fork Suite -->
            <g id="suite-fork-gfx" class="cursor-pointer" onclick="selectTreeSuite('fork')">
                <circle cx="460" cy="95" r="28" fill="#16a34a" stroke="#86efac" stroke-width="2" stroke-dasharray="3,3" />
                <text x="445" y="105" font-size="28">🐆</text>
                <text x="430" y="132" font-size="10" fill="#fde047" font-weight="bold">Fork Sanctuary</text>
            </g>

            <!-- Trunk Hollow Suite -->
            <g id="suite-hollow-gfx" class="cursor-pointer" onclick="selectTreeSuite('hollow')">
                <ellipse cx="350" cy="130" rx="20" ry="16" fill="#1a120b" stroke="#f59e0b" stroke-width="2" />
                <text x="340" y="136" font-size="18">🦉</text>
                <text x="280" y="155" font-size="10" fill="#fde047" font-weight="bold">Trunk Hollow</text>
            </g>

            <!-- Bark Crevice Suite -->
            <g id="suite-bark-gfx" class="cursor-pointer" onclick="selectTreeSuite('bark')">
                <rect x="325" y="170" width="50" height="40" rx="6" fill="#451a03" stroke="#d97706" stroke-width="2" stroke-dasharray="3,3" />
                <text x="340" y="195" font-size="18">🦎</text>
                <text x="280" y="222" font-size="10" fill="#d97706" font-weight="bold">Bark Crevice</text>
            </g>
        </svg>

        <div id="suite-feedback-card" class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-emerald-500/30 text-xs text-slate-200">
            <strong>Top Canopy Suite:</strong> Tailorbirds and sunbirds weave nests in high branch tips, keeping fragile eggs completely safe from ground prowlers like cats and snakes.
        </div>
    </div>
</div>

<script>
function selectTreeSuite(suite) {
    const suites = ['canopy', 'fork', 'hollow', 'bark'];
    suites.forEach(s => {
        const btn = document.getElementById(`btn-suite-${s}`);
        if (btn) {
            if (s === suite) {
                btn.className = 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex flex-col items-center gap-1';
            } else {
                btn.className = 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1';
            }
        }
    });

    const card = document.getElementById('suite-feedback-card');

    if (suite === 'canopy') {
        card.innerHTML = '<strong>Top Canopy Suite:</strong> Tailorbirds and sunbirds weave nests in high branch tips, keeping fragile eggs completely safe from ground prowlers like cats and snakes.';
    } else if (suite === 'fork') {
        card.innerHTML = '<strong>Branch Fork Suite:</strong> Broad horizontal limbs serve as elevated beds where leopards rest safely in cool breezes and fruit bats hang upside-down during the day.';
    } else if (suite === 'hollow') {
        card.innerHTML = '<strong>Trunk Hollow Suite:</strong> Natural cavities buffer spotted owlets, barbets, and striped squirrels against freezing winter winds and heavy monsoon downpours.';
    } else if (suite === 'bark') {
        card.innerHTML = '<strong>Bark Crevice Suite:</strong> Deep furrows in wooden bark shelter small geckos, jumping spiders, and beneficial beetles that sleep securely away from birds.';
    }
}
</script>
"""

# Simulator 7: Forest Tree Planters (Squirrel Caching & Bird Droppings)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🐿️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Wild Forest Tree Planters Lab</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Unintentional Arborists</span>
    </div>

    <p class="text-xs text-slate-300">Explore how forgetful squirrels bury nuts for winter and how fruit-eating birds disperse seeds across miles in natural fertilizer!</p>

    <!-- Planter Action Buttons -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="planterAction('squirrel')" id="btn-planter-sq" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left">
            <span class="text-2xl">🐿️</span>
            <div>
                <span class="text-xs block">Squirrel Bury & Forget</span>
                <span class="text-[10px] text-emerald-200">Forgotten Nuts Sprout in Spring</span>
            </div>
        </button>
        <button onclick="planterAction('bird')" id="btn-planter-bird" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🦜</span>
            <div>
                <span class="text-xs block">Bird Long-Distance Dispersal</span>
                <span class="text-[10px] text-slate-400">Viable Seeds in Rich Fertilizer</span>
            </div>
        </button>
    </div>

    <!-- Animated Planter Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800">
        <svg viewBox="0 0 700 220" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Soil and Grass -->
            <rect x="0" y="140" width="700" height="80" fill="#2d1500" />
            <rect x="0" y="125" width="700" height="18" fill="#14532d" />

            <!-- Squirrel Planter View -->
            <g id="view-sq-planter">
                <!-- Squirrel Digging -->
                <g transform="translate(140, 95)">
                    <text x="0" y="25" font-size="36">🐿️</text>
                    <text x="40" y="15" font-size="16">🌰</text>
                    <text x="-20" y="55" font-size="10" fill="#fde047" font-weight="bold">Burying 1,000+ Nuts</text>
                </g>

                <!-- Forgotten Seed Sprouting -->
                <g transform="translate(380, 110)">
                    <!-- Buried seed -->
                    <circle cx="0" cy="25" r="8" fill="#d97706" />
                    <!-- Sprout -->
                    <path d="M 0 25 L 0 -10" stroke="#22c55e" stroke-width="3" />
                    <text x="-12" y="-12" font-size="20">🌱</text>
                    <text x="-35" y="45" font-size="10" fill="#86efac" font-weight="bold">Forgotten Seed Sprouted!</text>
                </g>
            </g>

            <!-- Bird Planter View (Hidden initially) -->
            <g id="view-bird-planter" class="hidden">
                <!-- Flying Hornbill/Bulbul -->
                <g transform="translate(180, 40)">
                    <text x="0" y="20" font-size="34">🦜</text>
                    <text x="35" y="10" font-size="16">🍒</text>
                    <text x="-25" y="45" font-size="10" fill="#38bdf8" font-weight="bold">Feasting on Wild Fig</text>
                </g>

                <!-- Dropping and Germination 5 km away -->
                <g transform="translate(480, 110)">
                    <!-- Excreted Seed with Manure -->
                    <ellipse cx="0" cy="20" rx="14" ry="6" fill="#451a03" />
                    <circle cx="0" cy="18" r="4" fill="#fde047" />
                    <text x="-14" y="-8" font-size="24">🌿</text>
                    <text x="-40" y="45" font-size="10" fill="#86efac" font-weight="bold">Sprouted Miles Away!</text>
                </g>
            </g>
        </svg>

        <div id="planter-feedback-card" class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-emerald-500/30 text-xs text-slate-200">
            <strong>Forgetful Squirrel Arborists:</strong> Squirrels bury thousands of seeds as winter emergency food. Forgetting many cache spots allows spring rains to awaken seeds into flourishing forest trees!
        </div>
    </div>
</div>

<script>
function planterAction(planter) {
    const btnSq = document.getElementById('btn-planter-sq');
    const btnBi = document.getElementById('btn-planter-bird');
    const viewSq = document.getElementById('view-sq-planter');
    const viewBi = document.getElementById('view-bird-planter');
    const card = document.getElementById('planter-feedback-card');

    if (planter === 'squirrel') {
        btnSq.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        btnBi.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
        viewSq.classList.remove('hidden');
        viewBi.classList.add('hidden');
        card.innerHTML = '<strong>Forgetful Squirrel Arborists:</strong> Squirrels bury thousands of seeds as winter emergency food. Forgetting many cache spots allows spring rains to awaken seeds into flourishing forest trees!';
    } else if (planter === 'bird') {
        btnBi.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        btnSq.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
        viewSq.classList.add('hidden');
        viewBi.classList.remove('hidden');
        card.innerHTML = '<strong>Avian Seed Dispersal:</strong> Frugivorous birds eat wild fruits and fly miles away. Indigestible seeds pass unharmed and land encased in natural fertilizer, creating widespread new groves!';
    }
}
</script>
"""

# Simulator 8: Fertilizing Organic Waste (Dung Beetles & Vermicompost Cycle)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪲</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Organic Waste & Nutrient Recycling Lab</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Zero-Waste Circular Soil</span>
    </div>

    <p class="text-xs text-slate-300">Experience nature's zero-waste cycle! Watch dung beetles bury organic manure and earthworms process it into nutrient-rich vermicompost for plant roots.</p>

    <!-- Cycle Trigger Buttons -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="recycleStep(1)" id="btn-rec-1" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left">
            <span class="text-2xl">🐄</span>
            <div>
                <span class="text-xs block">Step 1: Herbivore Dung</span>
                <span class="text-[10px] text-emerald-200">Natural Organic Minerals</span>
            </div>
        </button>
        <button onclick="recycleStep(2)" id="btn-rec-2" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🪲</span>
            <div>
                <span class="text-xs block">Step 2: Dung Beetle Roll</span>
                <span class="text-[10px] text-slate-400">Bury Deep to Roots</span>
            </div>
        </button>
        <button onclick="recycleStep(3)" id="btn-rec-3" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🌿</span>
            <div>
                <span class="text-xs block">Step 3: Root Absorption</span>
                <span class="text-[10px] text-slate-400">Lush Green Growth</span>
            </div>
        </button>
    </div>

    <!-- Animated Nutrient Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 230" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Soil Cross Section -->
            <rect x="0" y="80" width="700" height="150" fill="#2d1500" stroke="#78350f" stroke-width="2" />
            <rect x="0" y="65" width="700" height="18" fill="#14532d" />

            <!-- Growing Plant with Roots -->
            <g transform="translate(480, 45)">
                <path d="M 0 35 L 0 -15" stroke="#16a34a" stroke-width="4" />
                <text x="-16" y="-20" font-size="28">🌱</text>
                <!-- Roots extending into soil -->
                <path d="M 0 35 Q -30 75 -60 110" stroke="#d7ccc8" stroke-width="3" fill="none" />
                <path d="M 0 35 Q 20 80 40 120" stroke="#d7ccc8" stroke-width="3" fill="none" />
                <text x="35" y="-15" font-size="11" fill="#86efac" font-weight="bold">Plant Roots</text>
            </g>

            <!-- Step 1: Dung Mound -->
            <g id="rec-dung-mound" transform="translate(180, 65)">
                <ellipse cx="0" cy="10" rx="28" ry="12" fill="#451a03" stroke="#78350f" stroke-width="2" />
                <text x="-40" y="-8" font-size="11" fill="#fde047" font-weight="bold">Fresh Organic Manure</text>
            </g>

            <!-- Step 2: Dung Beetle Rolling -->
            <g id="rec-beetle-roll" transform="translate(240, 85)" opacity="0">
                <circle cx="0" cy="0" r="14" fill="#451a03" stroke="#78350f" stroke-width="2" />
                <text x="14" y="8" font-size="22">🪲</text>
                <text x="-35" y="32" font-size="10" fill="#38bdf8" font-weight="bold">Rolling Underground</text>
            </g>

            <!-- Step 3: Earthworm Castings & Root Uptake -->
            <g id="rec-root-uptake" transform="translate(420, 140)" opacity="0">
                <circle cx="0" cy="0" r="8" fill="#170c04" />
                <circle cx="15" cy="5" r="6" fill="#170c04" />
                <text x="-25" y="-10" font-size="16">🪱</text>
                <text x="-50" y="30" font-size="10" fill="#fde047" font-weight="bold">Nitrogen Uptake ✨</text>
            </g>
        </svg>

        <div id="recycle-feedback-card" class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-emerald-500/30 text-xs text-slate-200">
            <strong>Step 1: Organic Manure:</strong> Herbivore manure is packed with organic plant fibers, nitrogen, and potassium, providing natural biological food for soil organisms.
        </div>
    </div>
</div>

<script>
function recycleStep(step) {
    for (let i = 1; i <= 3; i++) {
        const btn = document.getElementById(`btn-rec-${i}`);
        if (btn) {
            if (i === step) {
                btn.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
            } else {
                btn.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
            }
        }
    }

    const dungMound = document.getElementById('rec-dung-mound');
    const beetleRoll = document.getElementById('rec-beetle-roll');
    const rootUptake = document.getElementById('rec-root-uptake');
    const card = document.getElementById('recycle-feedback-card');

    if (step === 1) {
        dungMound.style.opacity = '1';
        beetleRoll.style.opacity = '0';
        rootUptake.style.opacity = '0';
        card.innerHTML = '<strong>Step 1: Organic Manure:</strong> Herbivore manure is packed with organic plant fibers, nitrogen, and potassium, providing natural biological food for soil organisms.';
    } else if (step === 2) {
        dungMound.style.opacity = '0.5';
        beetleRoll.style.opacity = '1';
        rootUptake.style.opacity = '0';
        card.innerHTML = '<strong>Step 2: Dung Beetle Rolling & Burial:</strong> Industrious beetles shape manure into balls and bury it underground, aerating compacted soil and delivering nutrients to roots!';
    } else if (step === 3) {
        dungMound.style.opacity = '0.2';
        beetleRoll.style.opacity = '0.4';
        rootUptake.style.opacity = '1';
        card.innerHTML = '<strong>Step 3: Vermicompost & Root Uptake:</strong> Earthworms process the buried manure into bioavailable castings, and plant roots absorb nitrogen to power vibrant green leaf growth!';
    }
}
</script>
"""

if __name__ == "__main__":
    print(f"Simulators Part 1 count: {len(simulators_part1)}")
    assert len(simulators_part1) == 8, "Expected 8 simulators in Part 1"
    for i in range(1, 9):
        assert i in simulators_part1, f"Missing simulator {i}"
        print(f"Sim {i} length: {len(simulators_part1[i])} chars")
    print("Simulators Part 1 verified successfully!")
