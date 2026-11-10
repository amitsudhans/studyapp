#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 5: Plants and Animals Live Together
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Shared Living Spaces
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌳</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Forest Layer Habitat Explorer</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">4 Interconnected Layers</span>
    </div>

    <p class="text-xs text-slate-300">Click each forest layer to explore how animals and plants share living spaces—from the breezy upper canopy to deep subterranean soil!</p>

    <!-- Interactive Layer Selection Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectLayer(1, 'canopy')" id="btn-layer-canopy" class="layer-btn p-2 rounded-xl bg-emerald-600 text-white font-semibold text-xs border border-emerald-500 shadow transition flex flex-col items-center gap-1">
            <span>🌿 Upper Canopy</span>
            <span class="text-[10px] text-emerald-200">Sunbirds & Caterpillars</span>
        </button>
        <button onclick="selectLayer(1, 'trunk')" id="btn-layer-trunk" class="layer-btn p-2 rounded-xl bg-slate-900 text-slate-300 font-semibold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🪵 Tree Trunk</span>
            <span class="text-[10px] text-slate-400">Woodpeckers & Barbets</span>
        </button>
        <button onclick="selectLayer(1, 'floor')" id="btn-layer-floor" class="layer-btn p-2 rounded-xl bg-slate-900 text-slate-300 font-semibold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🍂 Forest Floor</span>
            <span class="text-[10px] text-slate-400">Elephants & Deer</span>
        </button>
        <button onclick="selectLayer(1, 'soil')" id="btn-layer-soil" class="layer-btn p-2 rounded-xl bg-slate-900 text-slate-300 font-semibold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🪱 Under Soil</span>
            <span class="text-[10px] text-slate-400">Earthworms & Roots</span>
        </button>
    </div>

    <!-- Dynamic Interactive SVG Ecosystem -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 relative overflow-hidden">
        <svg viewBox="0 0 700 320" class="w-full h-auto rounded-xl">
            <!-- Sky / Background -->
            <rect x="0" y="0" width="700" height="180" fill="#0c4a6e" opacity="0.4" />
            <circle cx="620" cy="50" r="35" fill="#fef08a" opacity="0.3" />

            <!-- Canopy Foliage Zone -->
            <g id="layer-canopy-gfx" class="transition-all duration-300 cursor-pointer" onclick="selectLayer(1, 'canopy')">
                <path d="M 120 110 Q 200 40 350 50 Q 500 40 580 110 Q 620 140 560 160 Q 350 175 140 160 Q 80 140 120 110 Z" fill="#15803d" stroke="#22c55e" stroke-width="2" />
                <path d="M 160 90 Q 260 30 350 35 Q 460 30 540 90 Z" fill="#16a34a" opacity="0.8" />
                <!-- Birds / Leaves -->
                <text x="240" y="85" font-size="22">🦜</text>
                <text x="360" y="70" font-size="20">🦋</text>
                <text x="440" y="95" font-size="20">🐛</text>
                <text x="480" y="130" font-size="14" fill="#bbf7d0" font-weight="bold">Canopy (High Leaves & Nectar)</text>
            </g>

            <!-- Trunk Zone -->
            <g id="layer-trunk-gfx" class="transition-all duration-300 cursor-pointer" onclick="selectLayer(1, 'trunk')">
                <rect x="310" y="150" width="80" height="90" fill="#78350f" stroke="#92400e" stroke-width="2" rx="6" />
                <!-- Bark Lines -->
                <line x1="330" y1="160" x2="330" y2="230" stroke="#451a03" stroke-width="2" />
                <line x1="350" y1="155" x2="350" y2="235" stroke="#451a03" stroke-width="2" />
                <line x1="370" y1="165" x2="370" y2="230" stroke="#451a03" stroke-width="2" />
                <!-- Woodpecker & Hollow -->
                <circle cx="330" cy="180" r="12" fill="#1e1b4b" stroke="#312e81" stroke-width="1.5" />
                <text x="350" y="185" font-size="18">🐿️</text>
                <text x="385" y="200" font-size="18">🪵</text>
                <text x="210" y="200" font-size="14" fill="#fcd34d" font-weight="bold">Trunk (Bark & Hollows)</text>
            </g>

            <!-- Ground Forest Floor Zone -->
            <g id="layer-floor-gfx" class="transition-all duration-300 cursor-pointer" onclick="selectLayer(1, 'floor')">
                <rect x="0" y="230" width="700" height="35" fill="#14532d" stroke="#16a34a" stroke-width="1.5" />
                <!-- Grass blades & Floor Animals -->
                <text x="80" y="245" font-size="24">🐘</text>
                <text x="170" y="250" font-size="18">🦌</text>
                <text x="480" y="250" font-size="18">🌱</text>
                <text x="560" y="250" font-size="16">🍂</text>
                <text x="230" y="252" font-size="13" fill="#86efac" font-weight="bold">Forest Floor (Grass, Fallen Leaves & Grazers)</text>
            </g>

            <!-- Subterranean Soil Zone -->
            <g id="layer-soil-gfx" class="transition-all duration-300 cursor-pointer" onclick="selectLayer(1, 'soil')">
                <rect x="0" y="265" width="700" height="55" fill="#3e2723" stroke="#5d4037" stroke-width="2" />
                <!-- Roots -->
                <path d="M 320 265 Q 260 295 180 310" stroke="#d7ccc8" stroke-width="3" fill="none" stroke-linecap="round" />
                <path d="M 380 265 Q 430 290 510 305" stroke="#d7ccc8" stroke-width="3" fill="none" stroke-linecap="round" />
                <path d="M 350 265 L 350 315" stroke="#d7ccc8" stroke-width="3" fill="none" stroke-linecap="round" />
                <!-- Underground creatures -->
                <text x="240" y="295" font-size="18">🪱</text>
                <text x="420" y="300" font-size="16">🐜</text>
                <text x="460" y="300" font-size="13" fill="#d7ccc8" font-weight="bold">Underground Soil (Roots, Earthworms & Ants)</text>
            </g>
        </svg>

        <!-- Information Card for Selected Layer -->
        <div id="layer-info-card" class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-emerald-500/30 flex items-start justify-between gap-3">
            <div>
                <span id="layer-info-title" class="text-xs font-bold text-emerald-400 uppercase tracking-wider block">🌿 Upper Canopy Ecosystem</span>
                <p id="layer-info-desc" class="text-xs text-slate-200 mt-1">
                    High above, dense green foliage catches bright sunlight. Birds like sunbirds sip sweet nectar from blooms, caterpillars chew chlorophyll-rich leaves, and tree frogs camouflage among broad foliage.
                </p>
            </div>
            <span id="layer-stat-badge" class="px-2.5 py-1 rounded-lg bg-emerald-900/60 text-emerald-300 border border-emerald-700 text-[11px] font-bold shrink-0">Sunlight & Biomass</span>
        </div>
    </div>
</div>

<script>
function selectLayer(simId, layer) {
    const buttons = ['canopy', 'trunk', 'floor', 'soil'];
    buttons.forEach(l => {
        const btn = document.getElementById(`btn-layer-${l}`);
        if (btn) {
            if (l === layer) {
                btn.className = 'layer-btn p-2 rounded-xl bg-emerald-600 text-white font-semibold text-xs border border-emerald-500 shadow flex flex-col items-center gap-1';
            } else {
                btn.className = 'layer-btn p-2 rounded-xl bg-slate-900 text-slate-300 font-semibold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1';
            }
        }
    });

    const titleEl = document.getElementById('layer-info-title');
    const descEl = document.getElementById('layer-info-desc');
    const badgeEl = document.getElementById('layer-stat-badge');

    if (layer === 'canopy') {
        titleEl.textContent = '🌿 Upper Canopy Ecosystem';
        descEl.textContent = 'High above, dense green foliage catches bright sunlight. Birds like sunbirds sip sweet nectar from blooms, caterpillars chew chlorophyll-rich leaves, and tree frogs camouflage among broad foliage.';
        badgeEl.textContent = 'Sunlight & Biomass';
    } else if (layer === 'trunk') {
        titleEl.textContent = '🪵 Wooden Tree Trunk Ecosystem';
        descEl.textContent = 'Rugged vertical bark hosts industrious woodpeckers pecking for wood-boring beetle grubs, while tree hollows shelter sleeping squirrels, coppersmith barbets, and roosting owlets.';
        badgeEl.textContent = 'Bark & Hollow Shelters';
    } else if (layer === 'floor') {
        titleEl.textContent = '🍂 Forest Floor Grazing Ground';
        descEl.textContent = 'Rich understory where wild elephants graze on tall grasses, deer forage fallen pods, and dropped fruits feed wild boars, while decomposing leaves replenish moisture.';
        badgeEl.textContent = 'Herbivores & Fallen Leaves';
    } else if (layer === 'soil') {
        titleEl.textContent = '🪱 Subterranean Soil Habitat';
        descEl.textContent = 'Beneath our feet, sprawling tree roots anchor soil, while earthworms carve air channels and termites decompose organic matter into nutrient-packed humus.';
        badgeEl.textContent = 'Roots & Aerators';
    }
}
</script>
"""

# Simulator 2: Leaf Grazing Giants (Elephants and Plant Consumption)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🐘</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Megaherbivore Biomass & Seed Nursery Simulator</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Feeding & Sprouting Cycle</span>
    </div>

    <p class="text-xs text-slate-300">Feed wild grasses, leafy branches, and tree bark to the elephant. Watch food pass through digestion and sprout new saplings from organic manure!</p>

    <!-- Interactive Feeding Dashboard -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
        <button onclick="feedElephant('grass')" class="p-3 rounded-xl bg-slate-900 hover:bg-emerald-950/60 border border-slate-700 hover:border-emerald-600 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🌾</span>
            <div>
                <span class="text-xs font-bold text-white block">Feed Wild Grasses</span>
                <span class="text-[10px] text-slate-400">+25 kg Daily Intake</span>
            </div>
        </button>
        <button onclick="feedElephant('branches')" class="p-3 rounded-xl bg-slate-900 hover:bg-emerald-950/60 border border-slate-700 hover:border-emerald-600 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🌿</span>
            <div>
                <span class="text-xs font-bold text-white block">Feed Leafy Branches</span>
                <span class="text-[10px] text-slate-400">+40 kg Nutrient Foliage</span>
            </div>
        </button>
        <button onclick="feedElephant('bark')" class="p-3 rounded-xl bg-slate-900 hover:bg-emerald-950/60 border border-slate-700 hover:border-emerald-600 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🪵</span>
            <div>
                <span class="text-xs font-bold text-white block">Peel Fibrous Bark</span>
                <span class="text-[10px] text-slate-400">+35 kg Minerals & Fiber</span>
            </div>
        </button>
    </div>

    <!-- Animated Forest & Sprouting Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800">
        <div class="flex items-center justify-between text-xs mb-2">
            <span class="font-bold text-slate-300">Daily Plant Intake: <span id="elephant-intake-val" class="text-emerald-400 font-extrabold">50</span> / 150 kg</span>
            <span class="font-bold text-slate-300">Sprouted Forest Saplings: <span id="sapling-count-val" class="text-cyan-400 font-extrabold">2</span></span>
        </div>
        <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden mb-3">
            <div id="elephant-intake-bar" class="bg-gradient-to-r from-emerald-500 to-teal-400 h-2 w-[33%] transition-all duration-300"></div>
        </div>

        <svg viewBox="0 0 700 240" class="w-full h-auto rounded-xl bg-gradient-to-b from-sky-950 to-emerald-950/60 border border-slate-800">
            <!-- Distant Hills -->
            <path d="M 0 160 Q 150 110 320 160 Q 500 120 700 160 L 700 240 L 0 240 Z" fill="#064e3b" opacity="0.6" />
            <!-- Ground -->
            <rect x="0" y="160" width="700" height="80" fill="#14532d" />

            <!-- Elephant Graphic -->
            <g id="elephant-body" class="transition-transform duration-300">
                <!-- Body -->
                <ellipse cx="200" cy="140" rx="75" ry="50" fill="#64748b" stroke="#475569" stroke-width="2" />
                <!-- Legs -->
                <rect x="145" y="150" width="22" height="50" fill="#475569" rx="4" />
                <rect x="180" y="150" width="22" height="50" fill="#475569" rx="4" />
                <rect x="220" y="150" width="22" height="50" fill="#475569" rx="4" />
                <rect x="250" y="150" width="22" height="50" fill="#475569" rx="4" />
                <!-- Head & Ear -->
                <circle cx="120" cy="120" r="32" fill="#64748b" stroke="#475569" stroke-width="2" />
                <ellipse cx="140" cy="120" rx="18" ry="26" fill="#475569" stroke="#334155" stroke-width="1.5" />
                <circle cx="112" cy="112" r="3.5" fill="#0f172a" />
                <!-- Eye Sparkle -->
                <circle cx="113" cy="111" r="1" fill="#ffffff" />
                <!-- Tusk -->
                <path d="M 110 135 Q 95 145 90 135" stroke="#f8fafc" stroke-width="4" fill="none" stroke-linecap="round" />
                <!-- Trunk -->
                <path id="elephant-trunk" d="M 100 128 Q 70 145 65 170" stroke="#64748b" stroke-width="14" fill="none" stroke-linecap="round" />
            </g>

            <!-- Food in Trunk Animation -->
            <text id="food-in-trunk" x="50" y="185" font-size="22" opacity="0">🌾</text>

            <!-- Dung Nursery & Sapling Mounds -->
            <g id="dung-nursery-group">
                <g transform="translate(420, 175)">
                    <ellipse cx="0" cy="10" rx="20" ry="8" fill="#451a03" />
                    <text x="-8" y="2" font-size="16">🌱</text>
                    <text x="-25" y="24" font-size="10" fill="#86efac" font-weight="bold">Manure Sprout #1</text>
                </g>
                <g transform="translate(540, 170)">
                    <ellipse cx="0" cy="10" rx="20" ry="8" fill="#451a03" />
                    <text x="-8" y="2" font-size="18">🌿</text>
                    <text x="-25" y="24" font-size="10" fill="#86efac" font-weight="bold">Manure Sprout #2</text>
                </g>
            </g>
        </svg>

        <div id="elephant-feedback" class="mt-2 text-xs text-emerald-300 font-medium">
            Elephant is grazing peacefully! Total daily requirement is 150 kg of wild vegetation.
        </div>
    </div>
</div>

<script>
let elephantIntake = 50;
let saplingCount = 2;

function feedElephant(type) {
    const feedback = document.getElementById('elephant-feedback');
    const intakeVal = document.getElementById('elephant-intake-val');
    const intakeBar = document.getElementById('elephant-intake-bar');
    const saplingVal = document.getElementById('sapling-count-val');
    const foodIcon = document.getElementById('food-in-trunk');

    let gain = 25;
    let icon = '🌾';
    let label = 'wild grasses';

    if (type === 'branches') {
        gain = 40;
        icon = '🌿';
        label = 'fresh leafy branches';
    } else if (type === 'bark') {
        gain = 35;
        icon = '🪵';
        label = 'mineral-rich tree bark';
    }

    elephantIntake += gain;
    if (elephantIntake > 150) elephantIntake = 150;

    intakeVal.textContent = elephantIntake;
    intakeBar.style.width = ((elephantIntake / 150) * 100) + '%';

    if (foodIcon) {
        foodIcon.textContent = icon;
        foodIcon.style.opacity = '1';
        setTimeout(() => { foodIcon.style.opacity = '0'; }, 800);
    }

    if (elephantIntake >= 100 && saplingCount < 5) {
        saplingCount++;
        saplingVal.textContent = saplingCount;
        feedback.innerHTML = `<strong>Magnificent!</strong> Elephant consumed ${gain} kg of ${label}. Undigested seeds passed in rich organic manure, sprouting a brand new sapling!`;
    } else {
        feedback.innerHTML = `Elephant grasped ${label} with its dextrous trunk! Daily intake now at ${elephantIntake} kg.`;
    }
}
</script>
"""

# Simulator 3: Foliage Leaf Dwellers (Magnifier Leaf Explorer)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔍</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Magnifier Leaf Micro-Habitat Explorer</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">4 Micro-Creatures</span>
    </div>

    <p class="text-xs text-slate-300">Click on different regions of the giant tropical leaf to reveal how caterpillars, tree frogs, butterfly eggs, and resting moths inhabit green foliage!</p>

    <!-- Zone Selector Pills -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectLeafZone('caterpillar')" id="btn-zone-caterpillar" class="p-2 rounded-xl bg-emerald-600 text-white font-semibold text-xs border border-emerald-500 shadow flex flex-col items-center gap-1">
            <span>🐛 Caterpillar Margin</span>
            <span class="text-[10px] text-emerald-200">Chewing Leaf Tissue</span>
        </button>
        <button onclick="inspectLeafZone('frog')" id="btn-zone-frog" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-semibold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🐸 Tree Frog Perch</span>
            <span class="text-[10px] text-slate-400">Suction Toe Pads</span>
        </button>
        <button onclick="inspectLeafZone('eggs')" id="btn-zone-eggs" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-semibold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🥚 Butterfly Eggs</span>
            <span class="text-[10px] text-slate-400">Underside Nursery</span>
        </button>
        <button onclick="inspectLeafZone('moth')" id="btn-zone-moth" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-semibold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🦋 Resting Moth</span>
            <span class="text-[10px] text-slate-400">Rain & Sun Shield</span>
        </button>
    </div>

    <!-- Leaf Interactive SVG Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800">
        <svg viewBox="0 0 700 250" class="w-full h-auto rounded-xl">
            <!-- Background Garden Gradient -->
            <rect x="0" y="0" width="700" height="250" fill="#022c22" opacity="0.6" />

            <!-- Giant Leaf Structure -->
            <path d="M 60 130 C 140 40, 480 30, 640 120 C 480 220, 140 210, 60 130 Z" fill="#15803d" stroke="#22c55e" stroke-width="3" />
            <!-- Main Vein -->
            <path d="M 60 130 Q 350 125 640 120" stroke="#86efac" stroke-width="4" fill="none" stroke-linecap="round" />
            <!-- Secondary Veins -->
            <path d="M 200 128 Q 240 80 290 60" stroke="#86efac" stroke-width="2" fill="none" />
            <path d="M 200 128 Q 230 170 280 190" stroke="#86efac" stroke-width="2" fill="none" />
            <path d="M 350 125 Q 390 75 450 55" stroke="#86efac" stroke-width="2" fill="none" />
            <path d="M 350 125 Q 380 175 440 195" stroke="#86efac" stroke-width="2" fill="none" />
            <path d="M 480 122 Q 520 80 570 70" stroke="#86efac" stroke-width="2" fill="none" />

            <!-- Highlight Hotspots -->
            <!-- 1. Caterpillar on Leaf Margin -->
            <g id="hotspot-caterpillar" class="cursor-pointer" onclick="inspectLeafZone('caterpillar')">
                <circle cx="210" cy="65" r="24" fill="#059669" fill-opacity="0.3" stroke="#34d399" stroke-width="2" stroke-dasharray="3,3" />
                <text x="195" y="73" font-size="24">🐛</text>
                <!-- Chewed hole -->
                <circle cx="180" cy="55" r="8" fill="#022c22" />
            </g>

            <!-- 2. Tree Frog on Mid-blade -->
            <g id="hotspot-frog" class="cursor-pointer" onclick="inspectLeafZone('frog')">
                <circle cx="360" cy="150" r="26" fill="#059669" fill-opacity="0.3" stroke="#34d399" stroke-width="2" stroke-dasharray="3,3" />
                <text x="345" y="160" font-size="26">🐸</text>
            </g>

            <!-- 3. Eggs under leaf edge -->
            <g id="hotspot-eggs" class="cursor-pointer" onclick="inspectLeafZone('eggs')">
                <circle cx="530" cy="80" r="22" fill="#059669" fill-opacity="0.3" stroke="#34d399" stroke-width="2" stroke-dasharray="3,3" />
                <circle cx="522" cy="76" r="3" fill="#fef08a" />
                <circle cx="530" cy="74" r="3" fill="#fef08a" />
                <circle cx="538" cy="78" r="3" fill="#fef08a" />
                <circle cx="528" cy="84" r="3" fill="#fef08a" />
                <text x="548" y="85" font-size="12" fill="#fef08a" font-weight="bold">Eggs</text>
            </g>

            <!-- 4. Resting Moth -->
            <g id="hotspot-moth" class="cursor-pointer" onclick="inspectLeafZone('moth')">
                <circle cx="470" cy="165" r="24" fill="#059669" fill-opacity="0.3" stroke="#34d399" stroke-width="2" stroke-dasharray="3,3" />
                <text x="455" y="174" font-size="24">🦋</text>
            </g>
        </svg>

        <!-- Dynamic Specimen Card -->
        <div id="leaf-zone-card" class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-emerald-500/30 flex items-start justify-between gap-3">
            <div>
                <span id="leaf-zone-title" class="text-xs font-bold text-emerald-400 uppercase tracking-wider block">🐛 Voracious Leaf-Eating Caterpillar</span>
                <p id="leaf-zone-desc" class="text-xs text-slate-200 mt-1">
                    Equipped with sharp chewing mandibles, the caterpillar chews crescent-shaped gaps into the leaf blade, digesting chlorophyll and water to fuel its dramatic growth before pupation.
                </p>
            </div>
            <span id="leaf-zone-badge" class="px-2.5 py-1 rounded-lg bg-emerald-900/60 text-emerald-300 border border-emerald-700 text-[11px] font-bold shrink-0">Herbivore Larva</span>
        </div>
    </div>
</div>

<script>
function inspectLeafZone(zone) {
    const zones = ['caterpillar', 'frog', 'eggs', 'moth'];
    zones.forEach(z => {
        const btn = document.getElementById(`btn-zone-${z}`);
        if (btn) {
            if (z === zone) {
                btn.className = 'p-2 rounded-xl bg-emerald-600 text-white font-semibold text-xs border border-emerald-500 shadow flex flex-col items-center gap-1';
            } else {
                btn.className = 'p-2 rounded-xl bg-slate-900 text-slate-300 font-semibold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1';
            }
        }
    });

    const titleEl = document.getElementById('leaf-zone-title');
    const descEl = document.getElementById('leaf-zone-desc');
    const badgeEl = document.getElementById('leaf-zone-badge');

    if (zone === 'caterpillar') {
        titleEl.textContent = '🐛 Voracious Leaf-Eating Caterpillar';
        descEl.textContent = 'Equipped with sharp chewing mandibles, the caterpillar chews crescent-shaped gaps into the leaf blade, digesting chlorophyll and water to fuel its dramatic growth before pupation.';
        badgeEl.textContent = 'Herbivore Larva';
    } else if (zone === 'frog') {
        titleEl.textContent = '🐸 Green Tree Frog on Moist Leaf';
        descEl.textContent = 'Using specialized suction-cupped toe pads, the tree frog adheres to slippery wet leaves without falling, perfectly camouflaged against green chlorophyll while ambushing passing insects.';
        badgeEl.textContent = 'Suction Grip Predator';
    } else if (zone === 'eggs') {
        titleEl.textContent = '🥚 Butterfly Eggs on Leaf Underside';
        descEl.textContent = 'Mother butterflies carefully glue clutches of tiny gem-like eggs to the sheltered underside of host leaves, shielding them from heavy raindrops, direct midday sun, and flying predators.';
        badgeEl.textContent = 'Nursery Platform';
    } else if (zone === 'moth') {
        titleEl.textContent = '🦋 Nocturnal Moth Under Leaf Umbrella';
        descEl.textContent = 'During bright daylight hours, moths rest quietly beneath broad leaves. The waterproof foliage acts as a natural green umbrella, shielding delicate powdered wings from rain and heat.';
        badgeEl.textContent = 'Rain & Heat Shield';
    }
}
</script>
"""

# Simulator 4: Tailorbird Leaf Nests (Leaf Stitching Workshop)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪡</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Tailorbird Leaf Stitching Workshop</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Avian Architecture</span>
    </div>

    <p class="text-xs text-slate-300">Experience how the tailorbird pierces holes in living mango leaves, threads plant cotton strands, and lines the cozy cradle with downy feathers!</p>

    <!-- Stitching Step Controls -->
    <div class="grid grid-cols-1 sm:grid-cols-4 gap-2">
        <button onclick="stitchingStep(1)" id="step-btn-1" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex flex-col items-center gap-0.5">
            <span>Step 1: Puncture</span>
            <span class="text-[10px] text-emerald-200">Needle Beak Holes</span>
        </button>
        <button onclick="stitchingStep(2)" id="step-btn-2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-0.5">
            <span>Step 2: Thread</span>
            <span class="text-[10px] text-slate-400">Plant Cotton Strands</span>
        </button>
        <button onclick="stitchingStep(3)" id="step-btn-3" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-0.5">
            <span>Step 3: Knot & Curl</span>
            <span class="text-[10px] text-slate-400">Green Cradle Pouch</span>
        </button>
        <button onclick="stitchingStep(4)" id="step-btn-4" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-0.5">
            <span>Step 4: Feather Bed</span>
            <span class="text-[10px] text-slate-400">Insulated Eggs</span>
        </button>
    </div>

    <!-- Animated Nest View -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 240" class="w-full h-auto rounded-xl bg-gradient-to-b from-slate-950 to-emerald-950/60 border border-slate-800">
            <!-- Living Bush Branch -->
            <path d="M 50 40 Q 250 80 650 50" stroke="#78350f" stroke-width="8" fill="none" stroke-linecap="round" />

            <!-- Left Leaf -->
            <path id="nest-leaf-left" d="M 280 65 Q 200 130 260 210 Q 320 180 320 70 Z" fill="#16a34a" stroke="#22c55e" stroke-width="2.5" />
            <!-- Right Leaf -->
            <path id="nest-leaf-right" d="M 340 70 Q 420 130 360 210 Q 300 180 300 70 Z" fill="#15803d" stroke="#16a34a" stroke-width="2.5" />

            <!-- Puncture Holes (Step 1+) -->
            <g id="nest-holes" opacity="0">
                <circle cx="280" cy="110" r="4" fill="#022c22" stroke="#fde047" stroke-width="1.5" />
                <circle cx="285" cy="140" r="4" fill="#022c22" stroke="#fde047" stroke-width="1.5" />
                <circle cx="295" cy="170" r="4" fill="#022c22" stroke="#fde047" stroke-width="1.5" />

                <circle cx="340" cy="110" r="4" fill="#022c22" stroke="#fde047" stroke-width="1.5" />
                <circle cx="335" cy="140" r="4" fill="#022c22" stroke="#fde047" stroke-width="1.5" />
                <circle cx="325" cy="170" r="4" fill="#022c22" stroke="#fde047" stroke-width="1.5" />
            </g>

            <!-- Cotton Thread Stitches (Step 2+) -->
            <g id="nest-stitches" opacity="0">
                <line x1="280" y1="110" x2="340" y2="110" stroke="#f8fafc" stroke-width="2.5" stroke-dasharray="4,2" />
                <line x1="285" y1="140" x2="335" y2="140" stroke="#f8fafc" stroke-width="2.5" stroke-dasharray="4,2" />
                <line x1="295" y1="170" x2="325" y2="170" stroke="#f8fafc" stroke-width="2.5" stroke-dasharray="4,2" />
                <!-- Knots -->
                <circle cx="278" cy="110" r="3" fill="#e2e8f0" />
                <circle cx="342" cy="110" r="3" fill="#e2e8f0" />
                <circle cx="283" cy="140" r="3" fill="#e2e8f0" />
                <circle cx="337" cy="140" r="3" fill="#e2e8f0" />
            </g>

            <!-- Inside Bed & Eggs (Step 4) -->
            <g id="nest-cradle-interior" opacity="0">
                <!-- Soft Down Bed -->
                <ellipse cx="310" cy="175" rx="28" ry="12" fill="#fef3c7" />
                <!-- White Spotted Eggs -->
                <ellipse cx="304" cy="172" rx="5" ry="7" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
                <ellipse cx="316" cy="172" rx="5" ry="7" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
                <text x="290" y="200" font-size="11" fill="#fde047" font-weight="bold">Cozy Egg Nursery</text>
            </g>

            <!-- Tailorbird Flying / Perched -->
            <g transform="translate(140, 50)">
                <text x="0" y="30" font-size="34">🐦</text>
                <text x="-40" y="55" font-size="11" fill="#86efac" font-weight="bold">Tailorbird with Fiber</text>
            </g>
        </svg>

        <div id="stitching-feedback" class="mt-2 text-xs text-emerald-300 font-medium">
            <strong>Step 1 Active:</strong> The tailorbird pierces tidy holes along the edges of two living mango leaves using its needle-like beak.
        </div>
    </div>
</div>

<script>
function stitchingStep(step) {
    for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`step-btn-${i}`);
        if (btn) {
            if (i === step) {
                btn.className = 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex flex-col items-center gap-0.5';
            } else {
                btn.className = 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-0.5';
            }
        }
    }

    const holes = document.getElementById('nest-holes');
    const stitches = document.getElementById('nest-stitches');
    const cradle = document.getElementById('nest-cradle-interior');
    const feedback = document.getElementById('stitching-feedback');

    if (step === 1) {
        holes.style.opacity = '1';
        stitches.style.opacity = '0';
        cradle.style.opacity = '0';
        feedback.innerHTML = '<strong>Step 1: Puncturing Holes:</strong> With its fine, needle-like beak, the tailorbird punches matching holes along the margins of living mango leaves.';
    } else if (step === 2) {
        holes.style.opacity = '1';
        stitches.style.opacity = '1';
        cradle.style.opacity = '0';
        feedback.innerHTML = '<strong>Step 2: Threading Plant Fibers:</strong> The bird pulls Kapok tree cotton strands and flexible plant fibers through opposing holes, drawing leaves together.';
    } else if (step === 3) {
        holes.style.opacity = '1';
        stitches.style.opacity = '1';
        cradle.style.opacity = '0.4';
        feedback.innerHTML = '<strong>Step 3: Knotting into a Cradle:</strong> Knots on the outer leaf surfaces lock the living green leaves into an enclosed cone that never wilts or loses camouflage!';
    } else if (step === 4) {
        holes.style.opacity = '1';
        stitches.style.opacity = '1';
        cradle.style.opacity = '1';
        feedback.innerHTML = '<strong>Step 4: Feather Bedding & Eggs:</strong> The tailorbird lines the pouch with soft kapok down and animal hair, laying glossy eggs safe from snakes and crows!';
    }
}
</script>
"""

# Simulator 5: Woodpecker Tree Trunks (Drumming and Grub Extraction)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪵</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Woodpecker Bark Anatomy & Grub Hunter</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Vertical Trunk Biomechanics</span>
    </div>

    <p class="text-xs text-slate-300">Click the action buttons to examine the woodpecker's zygodactyl gripping feet, stiff tripod tail, and rapid tap-tap drumming to extract wood-boring grubs!</p>

    <!-- Biomechanics Action Buttons -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="woodpeckerAction('feet')" id="btn-wp-feet" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left">
            <span class="text-2xl">🦶</span>
            <div>
                <span class="text-xs block">Zygodactyl Feet</span>
                <span class="text-[10px] text-emerald-200">2 Forward + 2 Backward</span>
            </div>
        </button>
        <button onclick="woodpeckerAction('tail')" id="btn-wp-tail" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🪶</span>
            <div>
                <span class="text-xs block">Stiff Tail Prop</span>
                <span class="text-[10px] text-slate-400">Tripod Stability Brace</span>
            </div>
        </button>
        <button onclick="woodpeckerAction('drum')" id="btn-wp-drum" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">⚡</span>
            <div>
                <span class="text-xs block">Drum & Catch Grub</span>
                <span class="text-[10px] text-slate-400">Tap-Tap-Tap Chiseling</span>
            </div>
        </button>
    </div>

    <!-- Animated Tree Trunk & Woodpecker Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 240" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Massive Vertical Tree Trunk -->
            <rect x="180" y="0" width="180" height="240" fill="#451a03" stroke="#78350f" stroke-width="3" />
            <!-- Bark Furrows -->
            <line x1="210" y1="0" x2="210" y2="240" stroke="#291002" stroke-width="3" />
            <line x1="240" y1="0" x2="240" y2="240" stroke="#291002" stroke-width="4" />
            <line x1="280" y1="0" x2="280" y2="240" stroke="#291002" stroke-width="3" />
            <line x1="320" y1="0" x2="320" y2="240" stroke="#291002" stroke-width="4" />

            <!-- Hidden Grub Inside Bark Gallery -->
            <g id="bark-grub-gallery" transform="translate(230, 95)">
                <ellipse cx="0" cy="0" rx="14" ry="8" fill="#1e1b4b" />
                <text id="grub-icon" x="-10" y="5" font-size="14">🐛</text>
                <text x="-35" y="24" font-size="10" fill="#fde047" font-weight="bold">Wood Beetle Grub</text>
            </g>

            <!-- Woodpecker Figure -->
            <g id="woodpecker-figure" transform="translate(130, 70)" class="transition-transform duration-200">
                <!-- Stiff Tail Pressed Against Bark -->
                <path id="wp-tail-gfx" d="M 15 80 L 50 110 L 15 90 Z" fill="#1e293b" stroke="#e2e8f0" stroke-width="1.5" />
                <!-- Feet Clasping Bark (Zygodactyl) -->
                <g id="wp-feet-gfx">
                    <!-- Forward Claws -->
                    <line x1="25" y1="70" x2="52" y2="65" stroke="#f59e0b" stroke-width="3.5" stroke-linecap="round" />
                    <!-- Backward Claws -->
                    <line x1="25" y1="70" x2="10" y2="78" stroke="#f59e0b" stroke-width="3.5" stroke-linecap="round" />
                </g>
                <!-- Body -->
                <ellipse cx="10" cy="45" rx="22" ry="35" fill="#dc2626" />
                <ellipse cx="5" cy="45" rx="16" ry="28" fill="#f8fafc" />
                <!-- Head & Crest -->
                <circle cx="20" cy="15" r="16" fill="#dc2626" />
                <!-- Crest -->
                <path d="M 10 10 L -5 0 L 15 5 Z" fill="#ef4444" />
                <circle cx="25" cy="12" r="3" fill="#0f172a" />
                <!-- Chisel Beak -->
                <polygon points="32,12 65,16 32,20" fill="#94a3b8" />
                <!-- Barbed Sticky Tongue (Visible on drum) -->
                <line id="wp-tongue" x1="65" y1="16" x2="100" y2="25" stroke="#f43f5e" stroke-width="2" opacity="0" />
            </g>

            <!-- Vibration Soundwaves on Drumming -->
            <g id="drum-waves" opacity="0">
                <circle cx="230" cy="95" r="22" fill="none" stroke="#38bdf8" stroke-width="2" />
                <circle cx="230" cy="95" r="35" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4" />
                <text x="260" y="80" font-size="14" fill="#38bdf8" font-weight="bold">TAP-TAP-TAP!</text>
            </g>
        </svg>

        <div id="woodpecker-feedback" class="mt-2 text-xs text-emerald-300 font-medium">
            <strong>Zygodactyl Feet Active:</strong> Two toes point forward and two point backward, providing a vice-like clamp on the tree bark!
        </div>
    </div>
</div>

<script>
function woodpeckerAction(action) {
    const btnFeet = document.getElementById('btn-wp-feet');
    const btnTail = document.getElementById('btn-wp-tail');
    const btnDrum = document.getElementById('btn-wp-drum');
    const feedback = document.getElementById('woodpecker-feedback');
    const wpFigure = document.getElementById('woodpecker-figure');
    const wpTongue = document.getElementById('wp-tongue');
    const drumWaves = document.getElementById('drum-waves');
    const grubIcon = document.getElementById('grub-icon');

    // Reset button styles
    [btnFeet, btnTail, btnDrum].forEach(b => {
        b.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
    });

    if (action === 'feet') {
        btnFeet.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        drumWaves.style.opacity = '0';
        wpTongue.style.opacity = '0';
        feedback.innerHTML = '<strong>Zygodactyl Feet:</strong> Having two forward and two backward toes enables the woodpecker to cling to vertical tree trunks without slipping downward!';
    } else if (action === 'tail') {
        btnTail.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        drumWaves.style.opacity = '0';
        wpTongue.style.opacity = '0';
        feedback.innerHTML = '<strong>Stiff Tail Prop:</strong> The rigid central tail feathers press against the rough bark like a third leg, creating a stable tripod that absorbs chiseling recoil!';
    } else if (action === 'drum') {
        btnDrum.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        drumWaves.style.opacity = '1';
        wpFigure.style.transform = 'translate(138px, 70px)';
        wpTongue.style.opacity = '1';

        setTimeout(() => {
            wpFigure.style.transform = 'translate(130px, 70px)';
            grubIcon.textContent = '✨';
            feedback.innerHTML = '<strong>Tap-Tap-Tap! Grub Extracted:</strong> The woodpecker chisels into the bark and extends its long, barbed sticky tongue to catch the harmful beetle grub, saving the tree from fungal rot!';
        }, 500);
    }
}
</script>
"""

# Simulator 6: Tree Hollow Shelters (Cavity Inhabitants)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🕳️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Tree Hollow Wildlife Sanctuary</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Thermal Insulation Chambers</span>
    </div>

    <p class="text-xs text-slate-300">Explore who lives inside ancient hollow trees! Switch between different forest residents to see how thick wooden walls insulate animals through extreme seasons.</p>

    <!-- Resident Switcher -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="selectHollowResident('squirrel')" id="btn-res-squirrel" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left">
            <span class="text-2xl">🐿️</span>
            <div>
                <span class="text-xs block">Striped Palm Squirrel</span>
                <span class="text-[10px] text-emerald-200">Shredded Bark Drey</span>
            </div>
        </button>
        <button onclick="selectHollowResident('barbet')" id="btn-res-barbet" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🦜</span>
            <div>
                <span class="text-xs block">Coppersmith Barbet</span>
                <span class="text-[10px] text-slate-400">Chiseled Nest Cavity</span>
            </div>
        </button>
        <button onclick="selectHollowResident('owl')" id="btn-res-owl" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🦉</span>
            <div>
                <span class="text-xs block">Spotted Owlet</span>
                <span class="text-[10px] text-slate-400">Daytime Camouflage Roost</span>
            </div>
        </button>
    </div>

    <!-- Tree Hollow Cutaway SVG -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800">
        <svg viewBox="0 0 700 240" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Ancient Oak / Banyan Trunk -->
            <path d="M 120 0 L 140 240 L 560 240 L 580 0 Z" fill="#3e2723" stroke="#5d4037" stroke-width="4" />
            <path d="M 160 0 L 175 240 M 230 0 L 240 240 M 470 0 L 460 240 M 530 0 L 520 240" stroke="#271510" stroke-width="3" />

            <!-- Hollow Cavity Cutaway -->
            <ellipse cx="350" cy="120" rx="95" ry="85" fill="#1a120b" stroke="#8d6e63" stroke-width="4" />
            <!-- Inner Soft Bedding -->
            <path d="M 270 150 Q 350 185 430 150 Q 350 200 270 150 Z" fill="#d7ccc8" opacity="0.6" />

            <!-- Resident Graphic Placeholder (Swapped dynamically) -->
            <g id="hollow-resident-content" class="transition-all duration-300">
                <text x="325" y="135" font-size="52">🐿️</text>
                <text x="300" y="165" font-size="12" fill="#fde047" font-weight="bold">Baby Squirrel Drey</text>
            </g>

            <!-- Thermometer Graphic & Insulation Badge -->
            <g transform="translate(480, 50)">
                <rect x="0" y="0" width="160" height="75" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5" />
                <text x="12" y="24" font-size="11" fill="#94a3b8" font-weight="bold">HOLLOW MICROCLIMATE</text>
                <text id="hollow-temp-text" x="12" y="46" font-size="14" fill="#34d399" font-weight="extrabold">Cool & Shaded (24°C)</text>
                <text id="outside-temp-text" x="12" y="64" font-size="10" fill="#f87171">Outside Air: 38°C Blazing</text>
            </g>
        </svg>

        <div id="hollow-desc-card" class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-emerald-500/30">
            <span id="hollow-resident-title" class="text-xs font-bold text-emerald-400 uppercase tracking-wider block">🐿️ Striped Palm Squirrel Nursery</span>
            <p id="hollow-resident-desc" class="text-xs text-slate-200 mt-1">
                Striped squirrels gather dried grass and shredded eucalyptus bark into deep hollows. This thick wooden shelter shields newborn pups from hungry hawks, cats, and torrential monsoon rains.
            </p>
        </div>
    </div>
</div>

<script>
function selectHollowResident(res) {
    const btnSq = document.getElementById('btn-res-squirrel');
    const btnBa = document.getElementById('btn-res-barbet');
    const btnOw = document.getElementById('btn-res-owl');
    const content = document.getElementById('hollow-resident-content');
    const titleEl = document.getElementById('hollow-resident-title');
    const descEl = document.getElementById('hollow-resident-desc');
    const tempText = document.getElementById('hollow-temp-text');
    const outTemp = document.getElementById('outside-temp-text');

    [btnSq, btnBa, btnOw].forEach(b => {
        b.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
    });

    if (res === 'squirrel') {
        btnSq.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        content.innerHTML = '<text x="325" y="135" font-size="52">🐿️</text><text x="300" y="165" font-size="12" fill="#fde047" font-weight="bold">Baby Squirrel Drey</text>';
        titleEl.textContent = '🐿️ Striped Palm Squirrel Nursery';
        descEl.textContent = 'Striped squirrels gather dried grass and shredded eucalyptus bark into deep hollows. This thick wooden shelter shields newborn pups from hungry hawks, cats, and torrential monsoon rains.';
        tempText.textContent = 'Cool & Shaded (24°C)';
        outTemp.textContent = 'Outside Air: 38°C Blazing';
    } else if (res === 'barbet') {
        btnBa.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        content.innerHTML = '<text x="325" y="135" font-size="52">🦜</text><text x="295" y="165" font-size="12" fill="#86efac" font-weight="bold">Barbet Chiseled Chamber</text>';
        titleEl.textContent = '🦜 Coppersmith Barbet Nesting Cavity';
        descEl.textContent = 'Using its heavy, sharp bill, the barbet chips a perfectly circular entrance into decaying wood. Inside, it lays smooth white eggs safe from monkeys and ground snakes.';
        tempText.textContent = 'Insulated Air (25°C)';
        outTemp.textContent = 'Outside Air: 14°C Chilly Wind';
    } else if (res === 'owl') {
        btnOw.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        content.innerHTML = '<text x="325" y="135" font-size="52">🦉</text><text x="300" y="165" font-size="12" fill="#c084fc" font-weight="bold">Spotted Owlet Roost</text>';
        titleEl.textContent = '🦉 Spotted Owlet Daytime Sanctuary';
        descEl.textContent = 'During bright daylight hours, owlets huddle quietly inside hollow trunks. Their speckled grey-brown plumage matches bark shadows, keeping them invisible while resting.';
        tempText.textContent = 'Dark & Quiet (22°C)';
        outTemp.textContent = 'Outside Air: Bright Sun & Crows';
    }
}
</script>
"""

# Simulator 7: Exploring Ground Soil (Tactile Soil Laboratory)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧪</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Tactile Soil Exploration Laboratory</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">4 Soil Formations</span>
    </div>

    <p class="text-xs text-slate-300">Perform the textbook activity! Select a soil sample from different locations to analyze its color, tactile feel, moisture level, and organic content.</p>

    <!-- Soil Sample Trays -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="testSoilSample('garden')" id="btn-soil-garden" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex flex-col items-center gap-1">
            <span>🪴 Garden Soil</span>
            <span class="text-[10px] text-emerald-200">Beneath Shady Neem</span>
        </button>
        <button onclick="testSoilSample('rain')" id="btn-soil-rain" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🌧️ Post-Rain Earth</span>
            <span class="text-[10px] text-slate-400">Moist & Fragrant</span>
        </button>
        <button onclick="testSoilSample('path')" id="btn-soil-path" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🏜️ Barren Pathway</span>
            <span class="text-[10px] text-slate-400">Dry & Gritty Sand</span>
        </button>
        <button onclick="testSoilSample('clay')" id="btn-soil-clay" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1">
            <span>🏺 Heavy Clay Soil</span>
            <span class="text-[10px] text-slate-400">Sticky & Dense</span>
        </button>
    </div>

    <!-- Diagnostic Magnification Display -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
            <!-- Digital Magnifier Dish -->
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-center relative overflow-hidden">
                <span class="text-[10px] uppercase font-bold text-slate-500 block mb-1">Microscope Tray View (10x)</span>
                <div id="soil-dish-display" class="w-36 h-36 mx-auto rounded-full border-4 border-emerald-500/40 shadow-inner flex items-center justify-center bg-[#2b1810] relative">
                    <span id="soil-icon-cluster" class="text-3xl">🍂 🪱 🪨</span>
                </div>
                <span id="soil-sample-label" class="text-xs font-bold text-emerald-300 block mt-2">Shady Neem Garden Soil</span>
            </div>

            <!-- Soil Properties Gauges -->
            <div class="space-y-2.5 text-xs">
                <div>
                    <div class="flex justify-between text-slate-300 mb-1">
                        <span>Tactile Texture:</span>
                        <strong id="soil-prop-texture" class="text-emerald-400">Crumbly, Soft & Damp</strong>
                    </div>
                </div>
                <div>
                    <div class="flex justify-between text-slate-300 mb-1">
                        <span>Moisture Level:</span>
                        <strong id="soil-prop-moisture" class="text-cyan-400">65% (Optimal)</strong>
                    </div>
                    <div class="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden">
                        <div id="bar-soil-moisture" class="bg-cyan-400 h-1.5 w-[65%]"></div>
                    </div>
                </div>
                <div>
                    <div class="flex justify-between text-slate-300 mb-1">
                        <span>Organic Humus Content:</span>
                        <strong id="soil-prop-humus" class="text-amber-400">High (Decomposed Leaves)</strong>
                    </div>
                    <div class="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden">
                        <div id="bar-soil-humus" class="bg-amber-400 h-1.5 w-[80%]"></div>
                    </div>
                </div>
            </div>
        </div>

        <div id="soil-analysis-card" class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-emerald-500/30 text-xs text-slate-200">
            <strong>Observation:</strong> Garden soil sheltered by tree leaves contains rich decomposed plant humus, tangled root hairs, and earthworm castings, staying moist and loose.
        </div>
    </div>
</div>

<script>
function testSoilSample(type) {
    const buttons = ['garden', 'rain', 'path', 'clay'];
    buttons.forEach(t => {
        const btn = document.getElementById(`btn-soil-${t}`);
        if (btn) {
            if (t === type) {
                btn.className = 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex flex-col items-center gap-1';
            } else {
                btn.className = 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-1';
            }
        }
    });

    const dish = document.getElementById('soil-dish-display');
    const icons = document.getElementById('soil-icon-cluster');
    const label = document.getElementById('soil-sample-label');
    const propTex = document.getElementById('soil-prop-texture');
    const propMoist = document.getElementById('soil-prop-moisture');
    const barMoist = document.getElementById('bar-soil-moisture');
    const propHumus = document.getElementById('soil-prop-humus');
    const barHumus = document.getElementById('bar-soil-humus');
    const card = document.getElementById('soil-analysis-card');

    if (type === 'garden') {
        dish.style.backgroundColor = '#2b1810';
        icons.textContent = '🍂 🪱 🪨';
        label.textContent = 'Shady Neem Garden Soil';
        propTex.textContent = 'Crumbly, Soft & Damp';
        propMoist.textContent = '65% (Optimal)';
        barMoist.style.width = '65%';
        propHumus.textContent = 'High (Decomposed Leaves)';
        barHumus.style.width = '80%';
        card.innerHTML = '<strong>Observation:</strong> Shaded garden soil holds abundant dark humus, root hairs, and organic castings, supporting earthworms and seedling growth.';
    } else if (type === 'rain') {
        dish.style.backgroundColor = '#1c100b';
        icons.textContent = '🌧️ 🪱 🌿';
        label.textContent = 'Fresh Post-Rain Topsoil';
        propTex.textContent = 'Spongy, Wet & Earthy (Petrichor)';
        propMoist.textContent = '90% (Saturated)';
        barMoist.style.width = '90%';
        propHumus.textContent = 'High (Active Microbes)';
        barHumus.style.width = '85%';
        card.innerHTML = '<strong>Observation:</strong> Rainwater activates actinobacteria microbes that release fragrant geosmin. Spongy humus stores moisture like a natural aquifer reservoir.';
    } else if (type === 'path') {
        dish.style.backgroundColor = '#d4a373';
        icons.textContent = '🪨 ☀️ 💨';
        label.textContent = 'Barren Pathway Soil';
        propTex.textContent = 'Rough, Gritty & Hard Sand';
        propMoist.textContent = '10% (Very Dry)';
        barMoist.style.width = '10%';
        propHumus.textContent = 'Minimal (No Plants)';
        barHumus.style.width = '15%';
        card.innerHTML = '<strong>Observation:</strong> Far from vegetation, sun and foot traffic bake the soil. Lacking leaf mulch and roots, it consists mainly of gritty mineral sand and small stones.';
    } else if (type === 'clay') {
        dish.style.backgroundColor = '#7f4f24';
        icons.textContent = '🏺 💧 🧱';
        label.textContent = 'Heavy Potters Clay';
        propTex.textContent = 'Sticky, Dense & Moldable';
        propMoist.textContent = '75% (Poor Drainage)';
        barMoist.style.width = '75%';
        propHumus.textContent = 'Low (Dense Mineral Clay)';
        barHumus.style.width = '30%';
        card.innerHTML = '<strong>Observation:</strong> Composed of ultra-fine microscopic mineral plates that pack tightly. Sticky when wet and hard like brick when dry without organic humus.';
    }
}
</script>
"""

# Simulator 8: Rich Soil Composition (Sedimentation Column Fractionation)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🫙</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Soil Jar Sedimentation & Fractionation</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">4 Core Components</span>
    </div>

    <p class="text-xs text-slate-300">Shake the glass soil jar with water to see gravity separate soil particles into distinct natural layers based on weight and buoyancy!</p>

    <div class="flex items-center justify-center gap-3">
        <button onclick="shakeSoilJar()" class="px-5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition shadow flex items-center gap-2">
            <span>🔄</span> Shake Soil Jar
        </button>
        <button onclick="settleSoilJar()" class="px-5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs border border-slate-700 transition">
            ⏳ Settle Layers
        </button>
    </div>

    <!-- Soil Column Jar SVG -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
            <!-- Glass Jar SVG -->
            <svg viewBox="0 0 260 300" class="w-full max-w-[220px] mx-auto h-auto">
                <!-- Glass Jar Body -->
                <rect x="50" y="30" width="160" height="250" rx="16" fill="#0f172a" stroke="#94a3b8" stroke-width="4" />
                <rect x="80" y="14" width="100" height="16" rx="4" fill="#64748b" stroke="#94a3b8" stroke-width="2" />

                <!-- Layer 1: Floating Organic Humus (Top) -->
                <g id="jar-layer-humus" class="transition-opacity duration-500">
                    <rect x="54" y="60" width="152" height="30" fill="#2d1500" opacity="0.9" />
                    <text x="65" y="80" font-size="11" fill="#fde047" font-weight="bold">🍂 Humus (Floating)</text>
                </g>

                <!-- Layer 2: Cloudy Water & Suspended Clay -->
                <g id="jar-layer-clay" class="transition-opacity duration-500">
                    <rect x="54" y="90" width="152" height="50" fill="#92400e" opacity="0.75" />
                    <text x="65" y="120" font-size="11" fill="#fed7aa" font-weight="bold">🏺 Clay & Silt</text>
                </g>

                <!-- Layer 3: Settled Sand Particles -->
                <g id="jar-layer-sand" class="transition-opacity duration-500">
                    <rect x="54" y="140" width="152" height="70" fill="#d97706" opacity="0.85" />
                    <text x="65" y="180" font-size="11" fill="#fef3c7" font-weight="bold">🏖️ Fine Sand</text>
                </g>

                <!-- Layer 4: Heavy Gravel & Small Stones (Bottom) -->
                <g id="jar-layer-gravel" class="transition-opacity duration-500">
                    <rect x="54" y="210" width="152" height="66" rx="10" fill="#475569" opacity="0.95" />
                    <circle cx="80" cy="245" r="10" fill="#334155" />
                    <circle cx="120" cy="250" r="14" fill="#1e293b" />
                    <circle cx="160" cy="242" r="12" fill="#334155" />
                    <text x="65" y="235" font-size="11" fill="#f8fafc" font-weight="bold">🪨 Heavy Gravel</text>
                </g>
            </svg>

            <!-- Composition Chart -->
            <div class="space-y-3">
                <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block">Ideal Topsoil Composition</span>
                <div class="space-y-2 text-xs">
                    <div class="p-2 rounded-xl bg-slate-950 border border-slate-800 flex justify-between items-center">
                        <span class="text-slate-300 font-medium">🪨 Weathered Minerals (Sand/Silt/Clay)</span>
                        <span class="text-emerald-400 font-bold">45%</span>
                    </div>
                    <div class="p-2 rounded-xl bg-slate-950 border border-slate-800 flex justify-between items-center">
                        <span class="text-slate-300 font-medium">💧 Retained Soil Moisture</span>
                        <span class="text-cyan-400 font-bold">25%</span>
                    </div>
                    <div class="p-2 rounded-xl bg-slate-950 border border-slate-800 flex justify-between items-center">
                        <span class="text-slate-300 font-medium">💨 Aerated Oxygen Pockets</span>
                        <span class="text-sky-400 font-bold">25%</span>
                    </div>
                    <div class="p-2 rounded-xl bg-slate-950 border border-slate-800 flex justify-between items-center">
                        <span class="text-slate-300 font-medium">🍂 Organic Humus & Organisms</span>
                        <span class="text-amber-400 font-bold">5%</span>
                    </div>
                </div>
            </div>
        </div>

        <div id="jar-status-text" class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-emerald-500/30 text-xs text-slate-200">
            <strong>Settled State:</strong> Dense mineral stones settle instantly at the bottom, followed by sand and fine clay, while light organic humus floats on top!
        </div>
    </div>
</div>

<script>
function shakeSoilJar() {
    const humus = document.getElementById('jar-layer-humus');
    const clay = document.getElementById('jar-layer-clay');
    const sand = document.getElementById('jar-layer-sand');
    const gravel = document.getElementById('jar-layer-gravel');
    const status = document.getElementById('jar-status-text');

    humus.style.opacity = '0.3';
    clay.style.opacity = '0.9';
    sand.style.opacity = '0.5';
    gravel.style.opacity = '0.7';

    status.innerHTML = '<strong>Shaking:</strong> Water and soil particles are swirling in turbulent suspension! All particles are mixed together.';
}

function settleSoilJar() {
    const humus = document.getElementById('jar-layer-humus');
    const clay = document.getElementById('jar-layer-clay');
    const sand = document.getElementById('jar-layer-sand');
    const gravel = document.getElementById('jar-layer-gravel');
    const status = document.getElementById('jar-status-text');

    humus.style.opacity = '0.9';
    clay.style.opacity = '0.75';
    sand.style.opacity = '0.85';
    gravel.style.opacity = '0.95';

    status.innerHTML = '<strong>Settled State:</strong> Heaviest gravel sinks first to the base, sand settles above it, fine clay remains suspended before settling, and organic humus floats at the top water surface!';
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
