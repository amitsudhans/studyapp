#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 5: Plants and Animals Live Together
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Underground Soil Inhabitants (Earthworm Tunneling & Castings)
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪱</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Subterranean Soil Aeration & Earthworm Burrower</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Nature's Living Plow</span>
    </div>

    <p class="text-xs text-slate-300">Click actions to guide the earthworm through compacted soil, carves aeration tunnels for plant roots, and trigger the millipede's spiral defense!</p>

    <!-- Subterranean Action Buttons -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="wormAction('burrow')" id="btn-worm-burrow" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left">
            <span class="text-2xl">🕳️</span>
            <div>
                <span class="text-xs block">Burrow & Aerate</span>
                <span class="text-[10px] text-emerald-200">Carve Oxygen Channels</span>
            </div>
        </button>
        <button onclick="wormAction('castings')" id="btn-worm-castings" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">💩</span>
            <div>
                <span class="text-xs block">Deposit Castings</span>
                <span class="text-[10px] text-slate-400">Natural Bio-Fertilizer</span>
            </div>
        </button>
        <button onclick="wormAction('millipede')" id="btn-worm-millipede" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🌀</span>
            <div>
                <span class="text-xs block">Touch Millipede</span>
                <span class="text-[10px] text-slate-400">Spiral Armor Defense</span>
            </div>
        </button>
    </div>

    <!-- Subterranean Canvas SVG -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 240" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Soil Cross Section Horizon -->
            <rect x="0" y="0" width="700" height="40" fill="#14532d" />
            <line x1="0" y1="40" x2="700" y2="40" stroke="#16a34a" stroke-width="2" />
            <!-- Subterranean Layer -->
            <rect x="0" y="40" width="700" height="200" fill="#3e2723" />

            <!-- Plant Stems & Subterranean Roots -->
            <g transform="translate(100, 20)">
                <text x="0" y="10" font-size="28">🌱</text>
                <path d="M 14 20 Q 0 80 -40 140" stroke="#d7ccc8" stroke-width="3" fill="none" />
                <path d="M 14 20 Q 30 90 60 150" stroke="#d7ccc8" stroke-width="3" fill="none" />
            </g>

            <!-- Tunnels carved by worm -->
            <g id="worm-tunnels">
                <path d="M 120 70 Q 220 120 320 80 Q 420 140 500 100" stroke="#1c100b" stroke-width="18" fill="none" stroke-linecap="round" />
                <!-- Oxygen & Water Ingress Markers -->
                <circle cx="220" cy="98" r="3" fill="#38bdf8" />
                <circle cx="320" cy="80" r="3" fill="#38bdf8" />
                <circle cx="420" cy="120" r="3" fill="#38bdf8" />
            </g>

            <!-- Earthworm Model -->
            <g id="earthworm-model" transform="translate(320, 80)" class="transition-transform duration-300">
                <path d="M -40 0 Q -20 -10 0 0 Q 20 10 40 0" stroke="#f472b6" stroke-width="12" fill="none" stroke-linecap="round" />
                <circle cx="40" cy="0" r="6" fill="#ec4899" />
                <!-- Segments -->
                <line x1="-20" y1="-5" x2="-20" y2="5" stroke="#db2777" stroke-width="1.5" />
                <line x1="0" y1="-5" x2="0" y2="5" stroke="#db2777" stroke-width="1.5" />
                <line x1="20" y1="-5" x2="20" y2="5" stroke="#db2777" stroke-width="1.5" />
                <text x="-35" y="-12" font-size="10" fill="#fbcfe8" font-weight="bold">Earthworm</text>
            </g>

            <!-- Earthworm Castings Group -->
            <g id="worm-castings-grp" opacity="0">
                <ellipse cx="260" cy="115" rx="12" ry="6" fill="#1b0c03" />
                <ellipse cx="275" cy="118" rx="8" ry="5" fill="#1b0c03" />
                <text x="230" y="140" font-size="10" fill="#fde047" font-weight="bold">Nutrient Castings ✨</text>
            </g>

            <!-- Millipede in Leaf Litter -->
            <g id="millipede-grp" transform="translate(560, 140)" class="cursor-pointer" onclick="wormAction('millipede')">
                <g id="millipede-extended">
                    <rect x="-35" y="-6" width="70" height="12" rx="6" fill="#78350f" stroke="#92400e" stroke-width="1.5" />
                    <!-- Lots of tiny legs -->
                    <line x1="-25" y1="6" x2="-25" y2="14" stroke="#d97706" stroke-width="1.5" />
                    <line x1="-15" y1="6" x2="-15" y2="14" stroke="#d97706" stroke-width="1.5" />
                    <line x1="-5" y1="6" x2="-5" y2="14" stroke="#d97706" stroke-width="1.5" />
                    <line x1="5" y1="6" x2="5" y2="14" stroke="#d97706" stroke-width="1.5" />
                    <line x1="15" y1="6" x2="15" y2="14" stroke="#d97706" stroke-width="1.5" />
                    <line x1="25" y1="6" x2="25" y2="14" stroke="#d97706" stroke-width="1.5" />
                    <text x="-30" y="-12" font-size="10" fill="#fde047" font-weight="bold">Millipede</text>
                </g>
                <g id="millipede-coiled" opacity="0">
                    <circle cx="0" cy="0" r="16" fill="#78350f" stroke="#92400e" stroke-width="2" />
                    <circle cx="0" cy="0" r="9" fill="#451a03" stroke="#d97706" stroke-width="1.5" />
                    <text x="-25" y="-22" font-size="10" fill="#38bdf8" font-weight="bold">Coiled Spiral!</text>
                </g>
            </g>
        </svg>

        <div id="subterranean-feedback" class="mt-2 text-xs text-emerald-300 font-medium">
            <strong>Burrowing Active:</strong> Earthworms glide through damp soil, carving micro-tunnels that allow oxygen and water to reach deep plant roots!
        </div>
    </div>
</div>

<script>
function wormAction(action) {
    const btnBu = document.getElementById('btn-worm-burrow');
    const btnCa = document.getElementById('btn-worm-castings');
    const btnMi = document.getElementById('btn-worm-millipede');
    const feedback = document.getElementById('subterranean-feedback');
    const wormModel = document.getElementById('earthworm-model');
    const castings = document.getElementById('worm-castings-grp');
    const milliExt = document.getElementById('millipede-extended');
    const milliCoil = document.getElementById('millipede-coiled');

    [btnBu, btnCa, btnMi].forEach(b => {
        b.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
    });

    if (action === 'burrow') {
        btnBu.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        wormModel.style.transform = 'translate(360px, 90px)';
        castings.style.opacity = '0';
        milliExt.style.opacity = '1';
        milliCoil.style.opacity = '0';
        feedback.innerHTML = '<strong>Burrowing & Aerating:</strong> As the earthworm crawls forward, it loosens hard soil, letting air and monsoon rain percolate straight to plant roots!';
    } else if (action === 'castings') {
        btnCa.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        castings.style.opacity = '1';
        feedback.innerHTML = '<strong>Natural Plant Fertilizer:</strong> Earthworms excrete nutrient-rich organic castings packed with nitrogen and phosphorus, enriching garden soil naturally!';
    } else if (action === 'millipede') {
        btnMi.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        milliExt.style.opacity = '0';
        milliCoil.style.opacity = '1';
        feedback.innerHTML = '<strong>Millipede Spiral Defense:</strong> When touched, the millipede curls into a tight armored spiral to shield its delicate walking legs and soft underside!';
    }
}
</script>
"""

# Simulator 10: Creeping Soil Insects (Ant Trails & Termite Recyclers)
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🐜</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Ant Pheromone Trails & Termite Wood Recycler</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Soil Surface Engineers</span>
    </div>

    <p class="text-xs text-slate-300">Lay invisible chemical scent trails (pheromones) for worker ants, or release termites to break down dead wood into rich organic soil carbon!</p>

    <!-- Insect Actions -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="insectAction('ant')" id="btn-ins-ant" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left">
            <span class="text-2xl">🐜</span>
            <div>
                <span class="text-xs block">Lay Ant Pheromone Trail</span>
                <span class="text-[10px] text-emerald-200">Guide Workers to Fallen Seed</span>
            </div>
        </button>
        <button onclick="insectAction('termite')" id="btn-ins-termite" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🪵</span>
            <div>
                <span class="text-xs block">Termite Wood Decomposition</span>
                <span class="text-[10px] text-slate-400">Recycle Fallen Branch Carbon</span>
            </div>
        </button>
    </div>

    <!-- Animated Surface Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800">
        <svg viewBox="0 0 700 230" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Ground Soil Horizon -->
            <rect x="0" y="80" width="700" height="150" fill="#2d1500" stroke="#78350f" stroke-width="2" />
            <rect x="0" y="60" width="700" height="20" fill="#14532d" />

            <!-- Ant Nest Underground Chamber -->
            <path d="M 80 80 Q 120 180 80 210 Q 30 180 80 80" fill="#170c04" stroke="#451a03" stroke-width="2" />
            <text x="50" y="160" font-size="11" fill="#fde047" font-weight="bold">Ant Nest</text>

            <!-- Fallen Seed Destination -->
            <g transform="translate(560, 65)">
                <ellipse cx="0" cy="0" rx="14" ry="9" fill="#d97706" />
                <ellipse cx="0" cy="0" rx="6" ry="4" fill="#fef3c7" />
                <text x="-25" y="24" font-size="10" fill="#fde047" font-weight="bold">Fallen Plant Seed</text>
            </g>

            <!-- Pheromone Scent Trail Dots -->
            <g id="pheromone-dots" opacity="0">
                <path d="M 100 70 Q 330 45 540 65" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6,4" fill="none" />
                <text x="260" y="45" font-size="11" fill="#38bdf8" font-weight="bold">Invisible Pheromone Scent Trail ✨</text>
            </g>

            <!-- Marching Ants -->
            <g id="ant-column" transform="translate(140, 68)">
                <text x="0" y="0" font-size="16">🐜</text>
                <text x="60" y="-3" font-size="16">🐜</text>
                <text x="120" y="0" font-size="16">🐜</text>
                <text x="180" y="-2" font-size="16">🐜</text>
                <text x="240" y="0" font-size="16">🐜</text>
                <text x="300" y="-3" font-size="16">🐜</text>
            </g>

            <!-- Fallen Tree Branch (Termite Decomposition) -->
            <g id="fallen-wood-grp" transform="translate(240, 140)">
                <rect id="log-body" x="0" y="0" width="160" height="30" rx="6" fill="#78350f" stroke="#92400e" stroke-width="2" />
                <text x="35" y="20" font-size="11" fill="#fed7aa" font-weight="bold">Fallen Dead Wood</text>
                <g id="termite-crew" opacity="0">
                    <circle cx="30" cy="15" r="3" fill="#ffffff" />
                    <circle cx="60" cy="15" r="3" fill="#ffffff" />
                    <circle cx="90" cy="15" r="3" fill="#ffffff" />
                    <circle cx="120" cy="15" r="3" fill="#ffffff" />
                    <text x="15" y="-6" font-size="11" fill="#a7f3d0" font-weight="bold">Termites Cycling Cellulose!</text>
                </g>
            </g>
        </svg>

        <div id="insects-feedback" class="mt-2 text-xs text-emerald-300 font-medium">
            <strong>Ant Colony Communication:</strong> Forager ants deposit chemical pheromone trails, guiding sisters to carry seeds into subterranean storage tunnels!
        </div>
    </div>
</div>

<script>
function insectAction(type) {
    const btnAnt = document.getElementById('btn-ins-ant');
    const btnTer = document.getElementById('btn-ins-termite');
    const phero = document.getElementById('pheromone-dots');
    const termiteCrew = document.getElementById('termite-crew');
    const logBody = document.getElementById('log-body');
    const feedback = document.getElementById('insects-feedback');

    if (type === 'ant') {
        btnAnt.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        btnTer.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
        phero.style.opacity = '1';
        termiteCrew.style.opacity = '0';
        logBody.style.fill = '#78350f';
        feedback.innerHTML = '<strong>Pheromone Trail Active:</strong> Ants follow invisible chemical scent trails to locate food and transport seeds to underground nests, aiding plant dispersal!';
    } else if (type === 'termite') {
        btnTer.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        btnAnt.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
        phero.style.opacity = '0';
        termiteCrew.style.opacity = '1';
        logBody.style.fill = '#451a03';
        feedback.innerHTML = '<strong>Cellulose Recycled:</strong> Subterranean termites digest tough dead wood using symbiotic gut microbes, cycling organic carbon directly back into fertile topsoil!';
    }
}
</script>
"""

# Simulator 11: Herbivore Plant Foragers (Camel Thorny Feeder & Canopy Monkey)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🐫</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Herbivore Forager Adaptations: Camel & Monkey</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Specialized Mouths & Diets</span>
    </div>

    <p class="text-xs text-slate-300">Observe how the desert camel chews sharp thorns without injury, and how canopy monkeys drop sweet fruits to feed ground animals!</p>

    <!-- Habitat Switcher -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="selectForager('camel')" id="btn-for-camel" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left">
            <span class="text-2xl">🐫</span>
            <div>
                <span class="text-xs block">Desert Camel & Thorny Acacia</span>
                <span class="text-[10px] text-emerald-200">Leathery Lips & Toughened Mouth</span>
            </div>
        </button>
        <button onclick="selectForager('monkey')" id="btn-for-monkey" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🐒</span>
            <div>
                <span class="text-xs block">Canopy Monkey & Dropped Fruit</span>
                <span class="text-[10px] text-slate-400">Feeding Ground Deer & Boars</span>
            </div>
        </button>
    </div>

    <!-- Forager Display Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800">
        <div id="forager-view-camel">
            <svg viewBox="0 0 700 220" class="w-full h-auto rounded-xl bg-gradient-to-b from-amber-950/50 to-amber-900/80 border border-slate-800">
                <!-- Sand Dune -->
                <path d="M 0 160 Q 250 120 450 160 Q 600 130 700 170 L 700 220 L 0 220 Z" fill="#b45309" />

                <!-- Thorny Desert Acacia Bush -->
                <g transform="translate(180, 100)">
                    <path d="M 0 80 Q 20 20 60 0 Q 100 20 120 80" stroke="#78350f" stroke-width="8" fill="none" />
                    <!-- Thorns -->
                    <line x1="40" y1="30" x2="25" y2="20" stroke="#fef3c7" stroke-width="2.5" />
                    <line x1="60" y1="20" x2="60" y2="5" stroke="#fef3c7" stroke-width="2.5" />
                    <line x1="80" y1="30" x2="95" y2="20" stroke="#fef3c7" stroke-width="2.5" />
                    <text x="15" y="105" font-size="11" fill="#fde047" font-weight="bold">Thorny Acacia Bush</text>
                </g>

                <!-- Dromedary Camel -->
                <g transform="translate(360, 60)">
                    <text x="0" y="80" font-size="70">🐫</text>
                    <!-- Leathery Mouth Callout -->
                    <circle cx="20" cy="50" r="14" fill="none" stroke="#22c55e" stroke-width="2" stroke-dasharray="3,3" />
                    <text x="45" y="45" font-size="11" fill="#86efac" font-weight="bold">Leathery Mouth Lining</text>
                    <text x="45" y="60" font-size="9" fill="#cbd5e1">Chews Sharp Spines Painlessly!</text>
                </g>
            </svg>
        </div>

        <div id="forager-view-monkey" class="hidden">
            <svg viewBox="0 0 700 220" class="w-full h-auto rounded-xl bg-gradient-to-b from-sky-950 to-emerald-950/80 border border-slate-800">
                <!-- Canopy Tree Branch -->
                <path d="M 50 50 Q 300 70 650 40" stroke="#78350f" stroke-width="12" fill="none" stroke-linecap="round" />
                <!-- Ground Forest Floor -->
                <rect x="0" y="170" width="700" height="50" fill="#14532d" />

                <!-- Monkey Plucking Fruit -->
                <g transform="translate(180, 20)">
                    <text x="0" y="45" font-size="44">🐒</text>
                    <text x="40" y="30" font-size="18">🥭</text>
                </g>

                <!-- Falling Fruit Animation -->
                <g transform="translate(240, 90)">
                    <text x="0" y="0" font-size="20">🥭</text>
                    <line x1="10" y1="-20" x2="10" y2="40" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3,3" />
                </g>

                <!-- Ground Herbivore Waiting (Spotted Deer) -->
                <g transform="translate(420, 140)">
                    <text x="0" y="35" font-size="40">🦌</text>
                    <text x="50" y="25" font-size="11" fill="#fde047" font-weight="bold">Waiting Deer Eating Dropped Fruit!</text>
                </g>
            </svg>
        </div>

        <div id="forager-desc-text" class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-emerald-500/30 text-xs text-slate-200">
            <strong>Camel Adaptation:</strong> Thick, leathery oral linings and toughened papillae enable the desert camel to grind tough thorns and thorny acacia branches without feeling any pain!
        </div>
    </div>
</div>

<script>
function selectForager(type) {
    const btnCam = document.getElementById('btn-for-camel');
    const btnMon = document.getElementById('btn-for-monkey');
    const viewCam = document.getElementById('forager-view-camel');
    const viewMon = document.getElementById('forager-view-monkey');
    const descText = document.getElementById('forager-desc-text');

    if (type === 'camel') {
        btnCam.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        btnMon.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
        viewCam.classList.remove('hidden');
        viewMon.classList.add('hidden');
        descText.innerHTML = '<strong>Camel Adaptation:</strong> Thick, leathery oral linings and toughened papillae enable the desert camel to grind tough thorns and thorny acacia branches without feeling any pain!';
    } else if (type === 'monkey') {
        btnMon.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        btnCam.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
        viewCam.classList.add('hidden');
        viewMon.classList.remove('hidden');
        descText.innerHTML = '<strong>Canopy Cooperation:</strong> As monkeys harvest wild figs and mangoes, dropped half-eaten fruits feed spotted deer waiting below, while seeds take root across the forest!';
    }
}
</script>
"""

# Simulator 12: Nectar Sipping Pollinators (Sunbird & Butterfly Proboscis)
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌺</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Mutualistic Nectar & Pollen Transfer Lab</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Flower & Pollinator Partnership</span>
    </div>

    <p class="text-xs text-slate-300">Test how the sunbird's curved bill slides into tubular hibiscus blooms, and how the butterfly's proboscis uncoils to sip nectar while dusting pollen!</p>

    <!-- Pollinator Switcher -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="pollinateAction('sunbird')" id="btn-pol-sunbird" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left">
            <span class="text-2xl">🦜</span>
            <div>
                <span class="text-xs block">Purple Sunbird & Hibiscus</span>
                <span class="text-[10px] text-emerald-200">Decurved Beak in Tubular Corolla</span>
            </div>
        </button>
        <button onclick="pollinateAction('butterfly')" id="btn-pol-butterfly" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🦋</span>
            <div>
                <span class="text-xs block">Swallowtail Butterfly & Marigold</span>
                <span class="text-[10px] text-slate-400">Uncoiling Tubular Proboscis</span>
            </div>
        </button>
    </div>

    <!-- Pollination Interactive Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 220" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Flower Graphic (Hibiscus) -->
            <g id="flower-hibiscus" transform="translate(180, 110)">
                <!-- Stem -->
                <path d="M 0 60 Q 20 20 60 0" stroke="#16a34a" stroke-width="6" fill="none" />
                <!-- Petals -->
                <path d="M 60 0 Q 120 -60 160 -10 Q 140 30 60 0" fill="#dc2626" opacity="0.9" />
                <path d="M 60 0 Q 130 0 170 40 Q 120 70 60 0" fill="#ef4444" opacity="0.9" />
                <path d="M 60 0 Q 90 -70 130 -40 Q 100 0 60 0" fill="#b91c1c" opacity="0.8" />
                <!-- Extended Stamen Tube & Anthers -->
                <path d="M 60 0 L 170 -15" stroke="#fef08a" stroke-width="4" />
                <circle cx="170" cy="-15" r="5" fill="#fde047" />
                <text x="70" y="85" font-size="11" fill="#fca5a5" font-weight="bold">Tubular Red Hibiscus</text>
            </g>

            <!-- Visiting Pollinator Figure -->
            <g id="pollinator-figure" transform="translate(380, 80)" class="transition-transform duration-300">
                <!-- Sunbird -->
                <g id="fig-sunbird">
                    <!-- Body -->
                    <ellipse cx="60" cy="20" rx="30" ry="18" fill="#4338ca" />
                    <!-- Head -->
                    <circle cx="25" cy="15" r="14" fill="#312e81" />
                    <circle cx="20" cy="12" r="2.5" fill="#ffffff" />
                    <!-- Downward Curved Beak -->
                    <path d="M 12 15 Q -15 22 -30 35" stroke="#0f172a" stroke-width="3" fill="none" stroke-linecap="round" />
                    <!-- Wings & Tail -->
                    <path d="M 60 10 Q 90 -10 100 5 Q 80 20 60 10" fill="#6366f1" />
                    <polygon points="90,20 125,25 90,30" fill="#1e1b4b" />
                    <text x="35" y="55" font-size="11" fill="#a5b4fc" font-weight="bold">Purple Sunbird</text>
                </g>

                <!-- Butterfly (Hidden initially) -->
                <g id="fig-butterfly" class="hidden">
                    <text x="10" y="30" font-size="44">🦋</text>
                    <!-- Proboscis line -->
                    <path d="M 15 25 Q -10 35 -30 40" stroke="#f59e0b" stroke-width="2" fill="none" stroke-linecap="round" />
                    <text x="0" y="55" font-size="11" fill="#fde047" font-weight="bold">Proboscis Uncoiled</text>
                </g>
            </g>

            <!-- Golden Pollen Dusting Glow -->
            <g id="pollen-dust" opacity="0">
                <circle cx="340" cy="95" r="8" fill="#fde047" opacity="0.6" />
                <circle cx="350" cy="85" r="5" fill="#fde047" opacity="0.8" />
                <circle cx="330" cy="105" r="6" fill="#fde047" opacity="0.7" />
                <text x="280" y="140" font-size="11" fill="#fde047" font-weight="bold">Golden Pollen Transferred! ✨</text>
            </g>
        </svg>

        <div id="pollination-feedback" class="mt-2 text-xs text-emerald-300 font-medium">
            <strong>Sunbird at Hibiscus:</strong> The slender downward-curved beak slides cleanly into the tubular flower. As the sunbird sips nectar, pollen dusts its forehead for cross-pollination!
        </div>
    </div>
</div>

<script>
function pollinateAction(type) {
    const btnSun = document.getElementById('btn-pol-sunbird');
    const btnBut = document.getElementById('btn-pol-butterfly');
    const figSun = document.getElementById('fig-sunbird');
    const figBut = document.getElementById('fig-butterfly');
    const pollenGlow = document.getElementById('pollen-dust');
    const feedback = document.getElementById('pollination-feedback');

    if (type === 'sunbird') {
        btnSun.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        btnBut.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
        figSun.classList.remove('hidden');
        figBut.classList.add('hidden');
        pollenGlow.style.opacity = '1';
        feedback.innerHTML = '<strong>Sunbird at Hibiscus:</strong> The decurved beak probes deep inside tubular petals. Pollen dusts the bird’s crown and gets carried to the next flower stigma!';
    } else if (type === 'butterfly') {
        btnBut.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        btnSun.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
        figSun.classList.add('hidden');
        figBut.classList.remove('hidden');
        pollenGlow.style.opacity = '1';
        feedback.innerHTML = '<strong>Butterfly Proboscis:</strong> The long, coiled mouthpart unrolls like a biological straw to drink sweet nectar, dusting butterfly legs in fertile golden pollen!';
    }
}
</script>
"""

# Simulator 13: Canopy Resting Creatures (Leopard Tree Fork & Bat Claws)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🐆</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Canopy Resting Sanctuary: Leopard & Flying Fox</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Elevated Safety</span>
    </div>

    <p class="text-xs text-slate-300">See why high tree branches provide safe elevated sanctuaries where leopards sleep protected from hyenas and fruit bats hang upside-down!</p>

    <!-- Sanctuary Toggle -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="canopySanctuary('leopard')" id="btn-can-leopard" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left">
            <span class="text-2xl">🐆</span>
            <div>
                <span class="text-xs block">Leopard Branch Perch</span>
                <span class="text-[10px] text-emerald-200">Hoisting Food Above Ground Hyenas</span>
            </div>
        </button>
        <button onclick="canopySanctuary('bat')" id="btn-can-bat" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🦇</span>
            <div>
                <span class="text-xs block">Roosting Flying Fox Bat</span>
                <span class="text-[10px] text-slate-400">Locking Tendon Claws</span>
            </div>
        </button>
    </div>

    <!-- Tree Sanctuary SVG Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800">
        <svg viewBox="0 0 700 230" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Ancient Canopy Branches -->
            <path d="M 0 100 Q 200 130 350 80 Q 500 50 700 80" stroke="#78350f" stroke-width="20" fill="none" />
            <!-- Branch Fork -->
            <path d="M 320 85 Q 420 150 560 170" stroke="#78350f" stroke-width="14" fill="none" />

            <!-- Green Canopy Foliage Canopy -->
            <ellipse cx="200" cy="50" rx="120" ry="40" fill="#15803d" opacity="0.6" />
            <ellipse cx="500" cy="40" rx="140" ry="45" fill="#15803d" opacity="0.6" />

            <!-- Leopard Resting View -->
            <g id="view-leopard-perch">
                <text x="280" y="80" font-size="52">🐆</text>
                <text x="250" y="115" font-size="11" fill="#fde047" font-weight="bold">Leopard Resting in Shaded Branch Fork</text>
                <!-- Ground Scavenger Looking Up -->
                <g transform="translate(480, 185)">
                    <text x="0" y="0" font-size="28">🐺</text>
                    <text x="-30" y="20" font-size="9" fill="#f87171">Hyena on ground cannot climb up!</text>
                </g>
            </g>

            <!-- Bat Roosting View (Hidden initially) -->
            <g id="view-bat-roost" class="hidden">
                <g transform="translate(340, 100)">
                    <!-- Upside-down Bat -->
                    <text x="0" y="30" font-size="44" transform="rotate(180, 20, 20)">🦇</text>
                    <text x="-40" y="70" font-size="11" fill="#a7f3d0" font-weight="bold">Flying Fox: Locking Claws</text>
                    <text x="-50" y="85" font-size="9" fill="#cbd5e1">Weight locks tendon tight with zero energy!</text>
                </g>
            </g>
        </svg>

        <div id="canopy-feedback" class="mt-2 text-xs text-emerald-300 font-medium">
            <strong>Leopard Canopy Safety:</strong> Strong limbs allow the leopard to hoist heavy prey high into tree forks, resting in breezy shade safe from ground scavengers!
        </div>
    </div>
</div>

<script>
function canopySanctuary(creature) {
    const btnLeo = document.getElementById('btn-can-leopard');
    const btnBat = document.getElementById('btn-can-bat');
    const viewLeo = document.getElementById('view-leopard-perch');
    const viewBat = document.getElementById('view-bat-roost');
    const feedback = document.getElementById('canopy-feedback');

    if (creature === 'leopard') {
        btnLeo.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        btnBat.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
        viewLeo.classList.remove('hidden');
        viewBat.classList.add('hidden');
        feedback.innerHTML = '<strong>Leopard Canopy Safety:</strong> Strong limbs allow the leopard to hoist heavy prey high into tree forks, resting in breezy shade safe from ground scavengers!';
    } else if (creature === 'bat') {
        btnBat.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        btnLeo.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
        viewLeo.classList.add('hidden');
        viewBat.classList.remove('hidden');
        feedback.innerHTML = '<strong>Bat Locking Tendons:</strong> Hanging body weight naturally locks the curved toe claws around tree twigs, allowing bats to sleep securely without muscular fatigue!';
    }
}
</script>
"""

# Simulator 14: Listening Bird Calls (Acoustic Chamber & Ear Cupping)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">👂</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Bird Bioacoustic Laboratory & Hand Cupping</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Sound Wave Physics</span>
    </div>

    <p class="text-xs text-slate-300">Listen to iconic Indian bird calls and toggle 'Cup Hands Behind Ears' to see how larger outer ear flaps funnel acoustic sound waves into your ear canal!</p>

    <!-- Bird Call Selector -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="playBirdAcoustic('pigeon')" id="btn-call-pigeon" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left">
            <span class="text-2xl">🕊️</span>
            <div>
                <span class="text-xs block">Blue Rock Pigeon</span>
                <span class="text-[10px] text-emerald-200">'Gutru-Gu, Gutru-Gu'</span>
            </div>
        </button>
        <button onclick="playBirdAcoustic('koel')" id="btn-call-koel" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🐦</span>
            <div>
                <span class="text-xs block">Asian Koel</span>
                <span class="text-[10px] text-slate-400">'Ku-oo, Ku-oo'</span>
            </div>
        </button>
        <button onclick="playBirdAcoustic('barbet')" id="btn-call-barbet" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left">
            <span class="text-2xl">🦜</span>
            <div>
                <span class="text-xs block">Coppersmith Barbet</span>
                <span class="text-[10px] text-slate-400">'Tuk... Tuk... Tuk...'</span>
            </div>
        </button>
    </div>

    <!-- Hand Cupping Toggle Button -->
    <div class="flex justify-center">
        <button id="btn-toggle-cupping" onclick="toggleHandCupping()" class="px-5 py-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow flex items-center gap-2">
            <span>👐</span>
            <span id="cupping-btn-label">Cup Hands Behind Ears (Amplify Sound)</span>
        </button>
    </div>

    <!-- Acoustic Waveform SVG -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 200" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Calling Bird -->
            <g transform="translate(100, 100)">
                <circle cx="0" cy="0" r="32" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
                <text id="active-bird-icon" x="-14" y="8" font-size="28">🕊️</text>
                <text id="active-bird-label" x="-45" y="45" font-size="11" fill="#38bdf8" font-weight="bold">Pigeon: Gutru-Gu</text>
            </g>

            <!-- Propagating Soundwaves -->
            <g id="soundwave-arcs">
                <path d="M 150 70 Q 180 100 150 130" stroke="#38bdf8" stroke-width="2.5" fill="none" />
                <path d="M 190 50 Q 230 100 190 150" stroke="#38bdf8" stroke-width="2.5" fill="none" />
                <path d="M 240 30 Q 290 100 240 170" stroke="#38bdf8" stroke-width="2.5" fill="none" />
                <path d="M 300 20 Q 360 100 300 180" stroke="#38bdf8" stroke-width="2.5" fill="none" />
            </g>

            <!-- Human Ear & Cupping Hands -->
            <g transform="translate(560, 100)">
                <ellipse cx="0" cy="0" rx="14" ry="24" fill="#fde047" stroke="#ca8a04" stroke-width="2" />
                <circle cx="-2" cy="0" r="5" fill="#a16207" />
                <!-- Cupping Hands Graphic -->
                <path id="cupping-hands-graphic" d="M 15 -35 Q 35 0 15 35" stroke="#38bdf8" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.3" />
                <text x="-40" y="45" font-size="11" fill="#fef08a" font-weight="bold">Listener Ear Canal</text>
                <text id="amplification-badge" x="-45" y="60" font-size="9" fill="#38bdf8">Normal Sound (1x)</text>
            </g>
        </svg>

        <div id="acoustic-feedback" class="mt-2 text-xs text-emerald-300 font-medium">
            <strong>Pigeon Sound:</strong> Rhythmic, low-frequency throat cooing 'Gutru-Gu, Gutru-Gu' resonates across rooftops and branches.
        </div>
    </div>
</div>

<script>
let isCuppingActive = false;

function playBirdAcoustic(bird) {
    const btnPi = document.getElementById('btn-call-pigeon');
    const btnKo = document.getElementById('btn-call-koel');
    const btnBa = document.getElementById('btn-call-barbet');
    const birdIcon = document.getElementById('active-bird-icon');
    const birdLabel = document.getElementById('active-bird-label');
    const feedback = document.getElementById('acoustic-feedback');

    [btnPi, btnKo, btnBa].forEach(b => {
        b.className = 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-3 text-left';
    });

    if (bird === 'pigeon') {
        btnPi.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        birdIcon.textContent = '🕊️';
        birdLabel.textContent = 'Pigeon: Gutru-Gu';
        feedback.innerHTML = '<strong>Pigeon Sound:</strong> Rhythmic, low-frequency throaty cooing "Gutru-Gu, Gutru-Gu" announces territorial presence on stone ledges and trees.';
        playToneSequence([260, 220, 260, 220]);
    } else if (bird === 'koel') {
        btnKo.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        birdIcon.textContent = '🐦';
        birdLabel.textContent = 'Koel: Ku-oo';
        feedback.innerHTML = '<strong>Asian Koel Call:</strong> Melodious rising two-syllable whistle "Ku-oo, Ku-oo" echoes through dense mango groves during spring and monsoon!';
        playToneSequence([350, 480]);
    } else if (bird === 'barbet') {
        btnBa.className = 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-3 text-left';
        birdIcon.textContent = '🦜';
        birdLabel.textContent = 'Barbet: Tuk-Tuk';
        feedback.innerHTML = '<strong>Coppersmith Barbet:</strong> Metallic, rhythmic striking sound "tuk... tuk... tuk..." resembles a coppersmith hammering a metal sheet with a mallet!';
        playToneSequence([440, 440, 440]);
    }
}

function toggleHandCupping() {
    isCuppingActive = !isCuppingActive;
    const handGfx = document.getElementById('cupping-hands-graphic');
    const badge = document.getElementById('amplification-badge');
    const btnLabel = document.getElementById('cupping-btn-label');
    const feedback = document.getElementById('acoustic-feedback');

    if (isCuppingActive) {
        handGfx.style.opacity = '1';
        badge.textContent = 'Amplified Sound (3x Focused)';
        badge.className = 'text-emerald-400 font-bold';
        btnLabel.textContent = 'Hands Cupped! (Click to Lower)';
        feedback.innerHTML = '<strong>Sound Wave Focusing:</strong> Cupping your hands mimics large animal ear flaps (pinnae), gathering more acoustic sound waves and funneling them directly into the eardrum!';
    } else {
        handGfx.style.opacity = '0.3';
        badge.textContent = 'Normal Sound (1x)';
        badge.className = 'text-sky-400';
        btnLabel.textContent = 'Cup Hands Behind Ears (Amplify Sound)';
    }
}

function playToneSequence(frequencies) {
    try {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (!AudioContext) return;
        const ctx = new AudioContext();
        let startTime = ctx.currentTime;
        frequencies.forEach((freq, idx) => {
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.frequency.setValueAtTime(freq, startTime + (idx * 0.15));
            gain.gain.setValueAtTime(isCuppingActive ? 0.3 : 0.1, startTime + (idx * 0.15));
            gain.gain.exponentialRampToValueAtTime(0.01, startTime + (idx * 0.15) + 0.12);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start(startTime + (idx * 0.15));
            osc.stop(startTime + (idx * 0.15) + 0.12);
        });
    } catch(e) {}
}
</script>
"""

# Simulator 15: Dawn Dusk Melodies (Diurnal Clock: Morning, Noon, Evening, Night)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌅</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Diurnal Bird Melody & Sun Synchronization Clock</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Circadian Rhythms</span>
    </div>

    <p class="text-xs text-slate-300">Click across the 4 times of day to observe how bird activity and singing change with sun height and ambient temperature!</p>

    <!-- Diurnal Time Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setDiurnalTime('dawn')" id="btn-time-dawn" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex flex-col items-center gap-0.5">
            <span>🌅 Early Dawn</span>
            <span class="text-[10px] text-emerald-200">Loud Dawn Chorus</span>
        </button>
        <button onclick="setDiurnalTime('noon')" id="btn-time-noon" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-0.5">
            <span>☀️ Midday Sun</span>
            <span class="text-[10px] text-slate-400">Quiet Shade Resting</span>
        </button>
        <button onclick="setDiurnalTime('dusk')" id="btn-time-dusk" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-0.5">
            <span>🌇 Twilight Dusk</span>
            <span class="text-[10px] text-slate-400">Roosting Parakeets</span>
        </button>
        <button onclick="setDiurnalTime('night')" id="btn-time-night" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-0.5">
            <span>🌙 Midnight Night</span>
            <span class="text-[10px] text-slate-400">Nocturnal Owlet Calls</span>
        </button>
    </div>

    <!-- Animated Sky & Woodland Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800">
        <svg viewBox="0 0 700 220" class="w-full h-auto rounded-xl">
            <!-- Sky Gradient (Swapped dynamically) -->
            <rect id="diurnal-sky" x="0" y="0" width="700" height="220" fill="#fdba74" />

            <!-- Sun / Moon Celestial Body -->
            <circle id="celestial-body" cx="160" cy="90" r="30" fill="#fef08a" stroke="#f59e0b" stroke-width="2" />

            <!-- Forest Silhouette Horizon -->
            <path d="M 0 160 Q 180 120 350 150 Q 520 110 700 150 L 700 220 L 0 220 Z" fill="#064e3b" />

            <!-- Tree Silhouettes & Active Bird -->
            <g transform="translate(320, 100)">
                <path d="M 0 60 Q 20 10 50 -10 Q 80 10 100 60" stroke="#022c22" stroke-width="8" fill="none" />
                <text id="diurnal-bird-icon" x="25" y="-15" font-size="34">🐦</text>
                <text id="diurnal-sound-label" x="-20" y="-30" font-size="12" fill="#ffffff" font-weight="extrabold">♪ Chirp! Tweet! Trill! ♪</text>
            </g>
        </svg>

        <div id="diurnal-explanation-card" class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-emerald-500/30 text-xs text-slate-200">
            <strong>Early Dawn Chorus:</strong> Cool, calm morning air carries sound waves far with minimal distortion. Magpie robins and bulbuls sing vigorously to announce territories and greet the new day!
        </div>
    </div>
</div>

<script>
function setDiurnalTime(time) {
    const times = ['dawn', 'noon', 'dusk', 'night'];
    times.forEach(t => {
        const btn = document.getElementById(`btn-time-${t}`);
        if (btn) {
            if (t === time) {
                btn.className = 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex flex-col items-center gap-0.5';
            } else {
                btn.className = 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-0.5';
            }
        }
    });

    const sky = document.getElementById('diurnal-sky');
    const celestial = document.getElementById('celestial-body');
    const birdIcon = document.getElementById('diurnal-bird-icon');
    const soundLabel = document.getElementById('diurnal-sound-label');
    const card = document.getElementById('diurnal-explanation-card');

    if (time === 'dawn') {
        sky.style.fill = '#fdba74';
        celestial.setAttribute('cx', '160');
        celestial.setAttribute('cy', '100');
        celestial.setAttribute('fill', '#fef08a');
        birdIcon.textContent = '🐦';
        soundLabel.textContent = '♪ Melodious Dawn Chorus! ♪';
        card.innerHTML = '<strong>Early Dawn Chorus:</strong> Cool, calm morning air carries sound waves far with minimal distortion. Magpie robins and bulbuls sing vigorously to announce territories!';
    } else if (time === 'noon') {
        sky.style.fill = '#38bdf8';
        celestial.setAttribute('cx', '350');
        celestial.setAttribute('cy', '40');
        celestial.setAttribute('fill', '#fde047');
        birdIcon.textContent = '🌿';
        soundLabel.textContent = 'Quiet Slumber in Dense Shade...';
        card.innerHTML = '<strong>Midday Slumber:</strong> As the sun blazes overhead, birds fall silent and retreat into deep canopy foliage to conserve bodily moisture and avoid overheating.';
    } else if (time === 'dusk') {
        sky.style.fill = '#fb7185';
        celestial.setAttribute('cx', '540');
        celestial.setAttribute('cy', '110');
        celestial.setAttribute('fill', '#f97316');
        birdIcon.textContent = '🦜';
        soundLabel.textContent = 'Screech! Roosting Parakeet Flocks!';
        card.innerHTML = '<strong>Twilight Dusk Activity:</strong> Noisy flocks of green parakeets and egrets call loudly as they gather on communal sleeping trees before darkness falls.';
    } else if (time === 'night') {
        sky.style.fill = '#090d16';
        celestial.setAttribute('cx', '540');
        celestial.setAttribute('cy', '50');
        celestial.setAttribute('fill', '#f8fafc');
        birdIcon.textContent = '🦉';
        soundLabel.textContent = 'Hoo-hoo... Spotted Owlet Call';
        card.innerHTML = '<strong>Night Nocturnal Watch:</strong> Day birds sleep soundly while nocturnal hunters awaken: spotted owlets screech from hollows and nightjars forage under the moon.';
    }
}
</script>
"""

# Simulator 16: Caterpillar Butterfly Cycle (4-Stage Metamorphosis Sequencer)
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🦋</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Interactive 4-Stage Metamorphosis Sequencer</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Holometabolous Life Cycle</span>
    </div>

    <p class="text-xs text-slate-300">Trace the life journey connecting plants and butterflies! Click each sequential stage to watch the miraculous transformation unfold.</p>

    <!-- Stage Navigation Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectMetamorphosisStage(1)" id="stage-btn-1" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex flex-col items-center gap-0.5">
            <span>Stage 1: Egg</span>
            <span class="text-[10px] text-emerald-200">Glued on Leaf</span>
        </button>
        <button onclick="selectMetamorphosisStage(2)" id="stage-btn-2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-0.5">
            <span>Stage 2: Larva</span>
            <span class="text-[10px] text-slate-400">Leaf Caterpillar</span>
        </button>
        <button onclick="selectMetamorphosisStage(3)" id="stage-btn-3" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-0.5">
            <span>Stage 3: Pupa</span>
            <span class="text-[10px] text-slate-400">Hanging Chrysalis</span>
        </button>
        <button onclick="selectMetamorphosisStage(4)" id="stage-btn-4" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-0.5">
            <span>Stage 4: Adult</span>
            <span class="text-[10px] text-slate-400">Winged Butterfly</span>
        </button>
    </div>

    <!-- Metamorphosis Display Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 230" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Garden Bush Twig -->
            <path d="M 60 70 Q 350 110 640 60" stroke="#78350f" stroke-width="10" fill="none" stroke-linecap="round" />
            <!-- Attached Green Leaf -->
            <path d="M 220 90 C 140 160 260 210 380 180 C 350 120 280 90 220 90 Z" fill="#15803d" stroke="#22c55e" stroke-width="2.5" />

            <!-- Stage 1 Graphic: Gem Eggs on Leaf -->
            <g id="meta-stage-1-gfx">
                <circle cx="280" cy="140" r="6" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5" />
                <circle cx="295" cy="145" r="6" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5" />
                <circle cx="290" cy="155" r="6" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5" />
                <text x="250" y="180" font-size="12" fill="#fde047" font-weight="bold">Stage 1: Glued Butterfly Eggs</text>
            </g>

            <!-- Stage 2 Graphic: Caterpillar Chewing Leaf -->
            <g id="meta-stage-2-gfx" class="hidden">
                <text x="260" y="130" font-size="52">🐛</text>
                <!-- Chewed Gaps -->
                <circle cx="230" cy="150" r="12" fill="#090d16" />
                <circle cx="340" cy="170" r="14" fill="#090d16" />
                <text x="220" y="210" font-size="12" fill="#86efac" font-weight="bold">Stage 2: Voracious Larva (Caterpillar)</text>
            </g>

            <!-- Stage 3 Graphic: Chrysalis Hanging from Silk Button -->
            <g id="meta-stage-3-gfx" class="hidden">
                <!-- Silk Button -->
                <circle cx="350" cy="95" r="4" fill="#ffffff" />
                <!-- Chrysalis Pod -->
                <path d="M 350 95 C 330 120 330 160 350 170 C 370 160 370 120 350 95 Z" fill="#166534" stroke="#4ade80" stroke-width="2" />
                <!-- Gold Spots -->
                <circle cx="345" cy="120" r="2" fill="#fde047" />
                <circle cx="355" cy="120" r="2" fill="#fde047" />
                <text x="280" y="200" font-size="12" fill="#a7f3d0" font-weight="bold">Stage 3: Pupa (Chrysalis Remodeling)</text>
            </g>

            <!-- Stage 4 Graphic: Emerged Radiant Butterfly -->
            <g id="meta-stage-4-gfx" class="hidden">
                <text x="310" y="120" font-size="64">🦋</text>
                <text x="250" y="180" font-size="12" fill="#fbcfe8" font-weight="bold">Stage 4: Adult Butterfly (Winged Imago)</text>
            </g>
        </svg>

        <div id="metamorphosis-desc-card" class="mt-3 p-3 rounded-xl bg-slate-950/80 border border-emerald-500/30 text-xs text-slate-200">
            <strong>Stage 1 - The Egg:</strong> Adult butterflies carefully glue tiny clutches of pearl-like eggs to the sheltered underside of host leaves, safe from rain and predators.
        </div>
    </div>
</div>

<script>
function selectMetamorphosisStage(stage) {
    for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`stage-btn-${i}`);
        const gfx = document.getElementById(`meta-stage-${i}-gfx`);
        if (btn) {
            if (i === stage) {
                btn.className = 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex flex-col items-center gap-0.5';
            } else {
                btn.className = 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center gap-0.5';
            }
        }
        if (gfx) {
            if (i === stage) {
                gfx.classList.remove('hidden');
            } else {
                gfx.classList.add('hidden');
            }
        }
    }

    const card = document.getElementById('metamorphosis-desc-card');
    if (stage === 1) {
        card.innerHTML = '<strong>Stage 1 - The Egg:</strong> Adult butterflies carefully glue tiny clutches of pearl-like eggs to the sheltered underside of host leaves, safe from rain and predators.';
    } else if (stage === 2) {
        card.innerHTML = '<strong>Stage 2 - The Caterpillar (Larva):</strong> The egg hatches into a hungry caterpillar equipped with chewing jaws, munching succulent leaves day and night to fuel rapid growth!';
    } else if (stage === 3) {
        card.innerHTML = '<strong>Stage 3 - The Chrysalis (Pupa):</strong> Fastening to a twig with silk, the caterpillar forms a smooth green casing inside which larval tissues dissolve and reorganize into wings and eyes!';
    } else if (stage === 4) {
        card.innerHTML = '<strong>Stage 4 - The Adult Butterfly:</strong> Pumping fluid into soft wings, the radiant winged butterfly expands in warm sunlight and flies off to sip nectar and pollinate garden blossoms!';
    }
}
</script>
"""

if __name__ == "__main__":
    print(f"Simulators Part 2 count: {len(simulators_part2)}")
    assert len(simulators_part2) == 8, "Expected 8 simulators in Part 2"
    for i in range(9, 17):
        assert i in simulators_part2, f"Missing simulator {i}"
        print(f"Sim {i} length: {len(simulators_part2[i])} chars")
    print("Simulators Part 2 verified successfully!")
