#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 6: Living in Harmony
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Balanced Living Web
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🕸️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Ecological Food Web & Harmony Balance</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Balanced Ecosystem</span>
    </div>

    <p class="text-xs text-slate-300">Explore how plants, herbivores, predators, and soil recyclers maintain a healthy living equilibrium!</p>

    <!-- Interactive Role Toggles -->
    <div class="grid grid-cols-1 sm:grid-cols-4 gap-2">
        <button onclick="inspectWebRole('plants')" id="btn-web-plants" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-2 text-left">
            <span class="text-2xl">🌱</span>
            <div>
                <span class="text-xs block">1. Producers</span>
                <span class="text-[10px] text-emerald-200">Plants & Sunlight</span>
            </div>
        </button>
        <button onclick="inspectWebRole('herbivores')" id="btn-web-herbivores" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2 text-left">
            <span class="text-2xl">🐛</span>
            <div>
                <span class="text-xs block">2. Plant Eaters</span>
                <span class="text-[10px] text-slate-400">Caterpillar & Deer</span>
            </div>
        </button>
        <button onclick="inspectWebRole('predators')" id="btn-web-predators" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2 text-left">
            <span class="text-2xl">🦜</span>
            <div>
                <span class="text-xs block">3. Nature Balance</span>
                <span class="text-[10px] text-slate-400">Birds & Lizards</span>
            </div>
        </button>
        <button onclick="inspectWebRole('recyclers')" id="btn-web-recyclers" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2 text-left">
            <span class="text-2xl">🪱</span>
            <div>
                <span class="text-xs block">4. Recyclers</span>
                <span class="text-[10px] text-slate-400">Worms & Fungi</span>
            </div>
        </button>
    </div>

    <!-- Web Visualization SVG -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 240" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Background Nature Gradients -->
            <rect x="0" y="0" width="700" height="170" fill="#0f172a" />
            <rect x="0" y="170" width="700" height="70" fill="#14532d" />
            <line x1="0" y1="170" x2="700" y2="170" stroke="#16a34a" stroke-width="2" />

            <!-- Sun -->
            <circle cx="60" cy="50" r="30" fill="#fbbf24" opacity="0.8" />
            <text x="45" y="58" font-size="28">☀️</text>

            <!-- Connecting Web Lines -->
            <g id="web-lines" stroke-width="2" stroke-dasharray="5,5" opacity="0.7">
                <line x1="90" y1="60" x2="160" y2="160" stroke="#fbbf24" />
                <line x1="200" y1="160" x2="310" y2="120" stroke="#22c55e" />
                <line x1="360" y1="120" x2="480" y2="80" stroke="#38bdf8" />
                <line x1="510" y1="110" x2="580" y2="180" stroke="#eab308" />
                <line x1="560" y1="190" x2="220" y2="185" stroke="#a855f7" />
            </g>

            <!-- Producer Node (Plants) -->
            <g id="node-plants" class="cursor-pointer" onclick="inspectWebRole('plants')">
                <circle cx="180" cy="165" r="42" fill="#14532d" stroke="#22c55e" stroke-width="3" />
                <text x="160" y="175" font-size="34">🌿</text>
                <text x="180" y="222" fill="#86efac" font-size="12" font-weight="bold" text-anchor="middle">Plants (Producers)</text>
            </g>

            <!-- Herbivore Node -->
            <g id="node-herbivores" class="cursor-pointer" onclick="inspectWebRole('herbivores')">
                <circle cx="335" cy="115" r="40" fill="#1e293b" stroke="#64748b" stroke-width="2" />
                <text x="315" y="125" font-size="32">🐛</text>
                <text x="335" y="70" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">Caterpillar (Herbivore)</text>
            </g>

            <!-- Predator / Insectivore Node -->
            <g id="node-predators" class="cursor-pointer" onclick="inspectWebRole('predators')">
                <circle cx="495" cy="90" r="40" fill="#1e293b" stroke="#64748b" stroke-width="2" />
                <text x="475" y="100" font-size="32">🦜</text>
                <text x="495" y="42" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">Songbird (Insectivore)</text>
            </g>

            <!-- Decomposer Node -->
            <g id="node-recyclers" class="cursor-pointer" onclick="inspectWebRole('recyclers')">
                <circle cx="610" cy="180" r="40" fill="#1e293b" stroke="#64748b" stroke-width="2" />
                <text x="590" y="190" font-size="32">🪱</text>
                <text x="610" y="232" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">Earthworm (Recycler)</text>
            </g>

            <!-- Pulse highlight indicator -->
            <circle id="web-pulse" cx="180" cy="165" r="48" fill="none" stroke="#4ade80" stroke-width="3" opacity="0.8">
                <animate attributeName="r" values="44;52;44" dur="2s" repeatCount="indefinite" />
            </circle>
        </svg>
    </div>

    <!-- Dynamic Role Description Card -->
    <div id="web-info-card" class="bg-slate-900/90 rounded-2xl p-4 border border-emerald-800/60 flex items-start gap-3">
        <span class="text-3xl" id="web-info-icon">🌱</span>
        <div class="space-y-1">
            <h4 class="text-sm font-bold text-emerald-300" id="web-info-title">Producers: The Green Foundation of Life</h4>
            <p class="text-xs text-slate-300" id="web-info-desc">Green plants capture radiant sunlight and drink soil water to craft nourishing leaves, nectar, and fruits. They generate clean oxygen and sustain every living creature in the community!</p>
            <div class="text-[11px] text-emerald-400 font-semibold mt-1" id="web-info-fact">🌟 Ecological Rule: Without healthy plants, no animals or humans could survive on Earth!</div>
        </div>
    </div>
</div>

<script>
function inspectWebRole(role) {
    const roles = {
        plants: {
            icon: '🌱',
            title: 'Producers: The Green Foundation of Life',
            desc: 'Green plants capture radiant sunlight and drink soil water to craft nourishing leaves, nectar, and fruits. They generate clean oxygen and sustain every living creature in the community!',
            fact: '🌟 Ecological Rule: Without healthy plants, no animals or humans could survive on Earth!',
            cx: 180, cy: 165, stroke: '#22c55e'
        },
        herbivores: {
            icon: '🐛',
            title: 'Primary Consumers: Plant Nibblers',
            desc: 'Caterpillars, deer, cows, and butterflies feed directly on fresh plant tissues. They convert plant energy into animal energy, prune foliage moderately, and aid in pollination.',
            fact: '🌿 Natural Balance: If caterpillars eat too many leaves, birds and frogs step in to keep their numbers in check!',
            cx: 335, cy: 115, stroke: '#38bdf8'
        },
        predators: {
            icon: '🦜',
            title: 'Insectivores & Predators: Population Protectors',
            desc: 'Garden songbirds, garden lizards, and frogs eat pest insects. By keeping herbivore populations balanced, they protect forest canopies from being completely defoliated!',
            fact: '🦅 Harmony Insight: Every predator is nature\\'s regulator, preventing any single species from overcrowding.',
            cx: 495, cy: 90, stroke: '#eab308'
        },
        recyclers: {
            icon: '🪱',
            title: 'Decomposers & Recyclers: Soil Rebuilders',
            desc: 'Earthworms, beetles, fungi, and soil microbes digest dead leaves and animal droppings. They break down organic matter into rich black humus that feeds plant roots once again.',
            fact: '🔄 Endless Loop: The cycle of life has zero waste in nature! Everything is lovingly returned to Mother Earth.',
            cx: 610, cy: 180, stroke: '#a855f7'
        }
    };

    const data = roles[role];
    if (!data) return;

    ['plants', 'herbivores', 'predators', 'recyclers'].forEach(k => {
        const btn = document.getElementById('btn-web-' + k);
        const node = document.getElementById('node-' + k);
        if (btn) {
            btn.className = (k === role) 
                ? 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-2 text-left'
                : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2 text-left';
        }
        if (node) {
            const circle = node.querySelector('circle');
            if (circle) circle.setAttribute('stroke', (k === role) ? data.stroke : '#64748b');
        }
    });

    const pulse = document.getElementById('web-pulse');
    if (pulse) {
        pulse.setAttribute('cx', data.cx);
        pulse.setAttribute('cy', data.cy);
        pulse.setAttribute('stroke', data.stroke);
    }

    document.getElementById('web-info-icon').textContent = data.icon;
    document.getElementById('web-info-title').textContent = data.title;
    document.getElementById('web-info-desc').textContent = data.desc;
    document.getElementById('web-info-fact').textContent = data.fact;
}
</script>
"""

# Simulator 10: Local Animal Surveys (Field Notebook Survey Tool)
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📋</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Junior Naturalist Field Survey Notebook</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Field Activity</span>
    </div>

    <p class="text-xs text-slate-300">Select an animal observed during a neighborhood nature walk to record its habitat, activity, diet, and human interaction!</p>

    <!-- Observation Target Tabs -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="logFieldSurvey('sunbird')" id="btn-survey-sunbird" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-2">
            <span class="text-xl">🐦</span>
            <span class="text-xs">Purple Sunbird</span>
        </button>
        <button onclick="logFieldSurvey('squirrel')" id="btn-survey-squirrel" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2">
            <span class="text-xl">🐿️</span>
            <span class="text-xs">Palm Squirrel</span>
        </button>
        <button onclick="logFieldSurvey('garden_lizard')" id="btn-survey-garden_lizard" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2">
            <span class="text-xl">🦎</span>
            <span class="text-xs">Garden Lizard</span>
        </button>
        <button onclick="logFieldSurvey('honeybee')" id="btn-survey-honeybee" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2">
            <span class="text-xl">🐝</span>
            <span class="text-xs">Honeybee</span>
        </button>
    </div>

    <!-- Survey Notebook View & Binocular SVG -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Visual Binocular View -->
        <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 flex flex-col items-center justify-center">
            <svg viewBox="0 0 320 200" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
                <!-- Dual Binocular Circles Mask -->
                <defs>
                    <clipPath id="bino-clip">
                        <circle cx="110" cy="100" r="85" />
                        <circle cx="210" cy="100" r="85" />
                    </clipPath>
                </defs>

                <!-- Natural Scenery -->
                <rect x="0" y="0" width="320" height="200" fill="#064e3b" />
                <circle cx="160" cy="50" r="80" fill="#047857" opacity="0.6" />
                <path d="M 0 170 Q 160 140 320 170 L 320 200 L 0 200 Z" fill="#78350f" />

                <!-- Creature Display inside Binoculars -->
                <g clip-path="url(#bino-clip)">
                    <rect x="0" y="0" width="320" height="200" fill="#0f766e" opacity="0.4" />
                    <!-- Background branches -->
                    <path d="M 40 180 Q 160 120 280 150" stroke="#b45309" stroke-width="8" stroke-linecap="round" fill="none" />
                    <text id="bino-creature-emoji" x="140" y="130" font-size="54">🐦</text>
                    <circle cx="160" cy="100" r="70" fill="none" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="4,4" />
                    <!-- Crosshair -->
                    <line x1="160" y1="80" x2="160" y2="120" stroke="#4ade80" stroke-width="1" />
                    <line x1="140" y1="100" x2="180" y2="100" stroke="#4ade80" stroke-width="1" />
                </g>

                <!-- Binocular Outer Rims -->
                <circle cx="110" cy="100" r="85" fill="none" stroke="#0284c7" stroke-width="4" opacity="0.8" />
                <circle cx="210" cy="100" r="85" fill="none" stroke="#0284c7" stroke-width="4" opacity="0.8" />
                <text x="160" y="190" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">🔭 Binocular Field Focus</text>
            </svg>
        </div>

        <!-- Field Notebook Entries -->
        <div class="bg-amber-950/20 border border-amber-600/40 rounded-2xl p-4 text-xs space-y-2.5">
            <div class="flex items-center justify-between pb-1.5 border-b border-amber-600/30">
                <span class="font-bold text-amber-300 text-sm flex items-center gap-1.5">
                    <span>📖</span> Naturalist Log Sheet
                </span>
                <span class="text-[10px] bg-amber-900/60 text-amber-200 px-2 py-0.5 rounded border border-amber-700">Survey #06-A</span>
            </div>

            <div class="grid grid-cols-2 gap-2 text-[11px]">
                <div class="bg-slate-900/80 p-2 rounded-lg border border-slate-800">
                    <span class="text-slate-400 block">Creature Name:</span>
                    <span id="log-name" class="font-bold text-emerald-300 text-xs">Purple Sunbird</span>
                </div>
                <div class="bg-slate-900/80 p-2 rounded-lg border border-slate-800">
                    <span class="text-slate-400 block">Where Spotted:</span>
                    <span id="log-habitat" class="font-bold text-amber-200 text-xs">Hibiscus bush flowers</span>
                </div>
            </div>

            <div class="bg-slate-900/80 p-2 rounded-lg border border-slate-800 text-[11px]">
                <span class="text-slate-400 block">Observed Activity:</span>
                <span id="log-activity" class="text-slate-200">Hovering delicately and inserting curved beak into red flower blossoms.</span>
            </div>

            <div class="bg-slate-900/80 p-2 rounded-lg border border-slate-800 text-[11px]">
                <span class="text-slate-400 block">Primary Food Source:</span>
                <span id="log-food" class="text-amber-300 font-semibold">Sweet floral nectar & tiny aphids</span>
            </div>

            <div class="bg-emerald-950/40 p-2 rounded-lg border border-emerald-700/60 text-[11px]">
                <span class="text-emerald-400 font-bold block">Ethical Coexistence Rule:</span>
                <span id="log-rule" class="text-emerald-200">Observe quietly from a respectful distance without shaking branches or touching nests!</span>
            </div>
        </div>
    </div>
</div>

<script>
function logFieldSurvey(animal) {
    const data = {
        sunbird: {
            emoji: '🐦',
            name: 'Purple Sunbird',
            habitat: 'Hibiscus & Moringa flowers',
            activity: 'Hovering delicately and inserting curved beak into blossom cups.',
            food: 'Sweet floral nectar & tiny flower aphids',
            rule: 'Observe quietly from a respectful distance without shaking branches or touching nests!'
        },
        squirrel: {
            emoji: '🐿️',
            name: 'Three-Striped Palm Squirrel',
            habitat: 'Guava tree trunk & roof tiles',
            activity: 'Scurrying up bark, twitching bushy tail, and nibbling fallen seeds.',
            food: 'Guava fruit slices, sunflower seeds, nuts',
            rule: 'Never chase or corner squirrels; leave fresh water pots on garden ledges!'
        },
        garden_lizard: {
            emoji: '🦎',
            name: 'Oriental Garden Lizard',
            habitat: 'Sunlit stone wall & hedge branches',
            activity: 'Basking under morning sun to warm its body and bobbing head in defense.',
            food: 'Garden grasshoppers, moths, and caterpillars',
            rule: 'Lizards eat crop-harming pests! Protect them by avoiding poisonous chemical sprays.'
        },
        honeybee: {
            emoji: '🐝',
            name: 'Indian Honeybee',
            habitat: 'Mustard blossoms & garden blooms',
            activity: 'Collecting golden pollen pellets on hind legs while pollinating blossoms.',
            food: 'Flower nectar and pollen',
            rule: 'Never throw stones at beehives; honeybees create fruits through gentle pollination!'
        }
    };

    const entry = data[animal];
    if (!entry) return;

    ['sunbird', 'squirrel', 'garden_lizard', 'honeybee'].forEach(k => {
        const btn = document.getElementById('btn-survey-' + k);
        if (btn) {
            btn.className = (k === animal)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-2'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2';
        }
    });

    document.getElementById('bino-creature-emoji').textContent = entry.emoji;
    document.getElementById('log-name').textContent = entry.name;
    document.getElementById('log-habitat').textContent = entry.habitat;
    document.getElementById('log-activity').textContent = entry.activity;
    document.getElementById('log-food').textContent = entry.food;
    document.getElementById('log-rule').textContent = entry.rule;
}
</script>
"""

# Simulator 11: Ant Food Choices (Ant Cafeteria & Buffet Exploration)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🐜</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Ant Cafeteria Food Preference & Trail Experiment</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Investigation Lab</span>
    </div>

    <p class="text-xs text-slate-300">Place different food samples on the test tray to discover which items recruit the most ants and trace their invisible scent trails!</p>

    <!-- Food Tray Selection Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="testAntFood('jaggery')" id="btn-ant-jaggery" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-2.5 text-left">
            <span class="text-2xl">🍯</span>
            <div>
                <span class="text-xs block">Sweet Jaggery</span>
                <span class="text-[10px] text-emerald-200">Pure Sugar Crystals</span>
            </div>
        </button>
        <button onclick="testAntFood('chips')" id="btn-ant-chips" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2.5 text-left">
            <span class="text-2xl">🍟</span>
            <div>
                <span class="text-xs block">Oily Sev / Chips</span>
                <span class="text-[10px] text-slate-400">Fried Salted Snack</span>
            </div>
        </button>
        <button onclick="testAntFood('grains')" id="btn-ant-grains" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2.5 text-left">
            <span class="text-2xl">🌾</span>
            <div>
                <span class="text-xs block">Rice Grains</span>
                <span class="text-[10px] text-slate-400">Hard Dry Seeds</span>
            </div>
        </button>
        <button onclick="testAntFood('lemon')" id="btn-ant-lemon" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2.5 text-left">
            <span class="text-2xl">🍋</span>
            <div>
                <span class="text-xs block">Sour Lemon</span>
                <span class="text-[10px] text-slate-400">Acidic Citrus Peel</span>
            </div>
        </button>
    </div>

    <!-- Ant Trail Canvas SVG -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 230" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Soil Ground Floor -->
            <rect x="0" y="0" width="700" height="230" fill="#1c1917" />
            <line x1="0" y1="180" x2="700" y2="180" stroke="#292524" stroke-width="2" />

            <!-- Ant Nest Anthill on Left -->
            <path d="M 30 180 Q 80 80 130 180 Z" fill="#78350f" stroke="#92400e" stroke-width="2" />
            <ellipse cx="80" cy="175" rx="15" ry="6" fill="#1c1917" />
            <text x="80" y="70" fill="#fde68a" font-size="12" font-weight="bold" text-anchor="middle">Anthill Colony</text>

            <!-- Test Tray on Right -->
            <ellipse cx="580" cy="140" rx="75" ry="35" fill="#334155" stroke="#64748b" stroke-width="3" />
            <ellipse cx="580" cy="137" rx="65" ry="28" fill="#1e293b" />
            <text id="ant-food-emoji" x="580" y="145" font-size="34" text-anchor="middle">🍯</text>
            <text id="ant-food-label" x="580" y="195" fill="#fde68a" font-size="12" font-weight="bold" text-anchor="middle">Jaggery Lump</text>

            <!-- Pheromone Scent Trail Path -->
            <path id="pheromone-path" d="M 90 170 Q 250 110 380 150 T 520 140" fill="none" stroke="#fbbf24" stroke-width="3" stroke-dasharray="6,6" opacity="0.8">
                <animate attributeName="stroke-dashoffset" values="0;-36" dur="2s" repeatCount="indefinite" />
            </path>

            <!-- Dynamic Marching Ants Group -->
            <g id="marching-ants-group">
                <!-- High traffic ants for Jaggery -->
                <text x="140" y="160" font-size="18">🐜</text>
                <text x="190" y="145" font-size="18">🐜</text>
                <text x="240" y="135" font-size="18">🐜</text>
                <text x="300" y="132" font-size="18">🐜</text>
                <text x="360" y="145" font-size="18">🐜</text>
                <text x="420" y="152" font-size="18">🐜</text>
                <text x="470" y="145" font-size="18">🐜</text>
                <text x="515" y="140" font-size="18">🐜</text>
                <text x="555" y="135" font-size="18">🐜</text>
                <text x="590" y="130" font-size="18">🐜</text>
            </g>

            <text x="320" y="215" fill="#a8a29e" font-size="11" text-anchor="middle">🧪 Chemical Communication: Foragers lay invisible scent trails (pheromones) so colony sisters follow!</text>
        </svg>
    </div>

    <!-- Live Experiment Results Stats -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-center">
            <span class="text-slate-400 block text-[11px]">Ants Recruited (10 Mins):</span>
            <span id="ant-count" class="text-xl font-bold text-amber-400">48 Worker Ants</span>
        </div>
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-center">
            <span class="text-slate-400 block text-[11px]">Scent Trail Strength:</span>
            <span id="ant-trail-strength" class="text-xl font-bold text-emerald-400">Super Strong 🔥</span>
        </div>
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-center">
            <span class="text-slate-400 block text-[11px]">Food Transport Strategy:</span>
            <span id="ant-strategy" class="text-xl font-bold text-sky-400">Direct Feeding & Licking</span>
        </div>
    </div>
</div>

<script>
function testAntFood(food) {
    const data = {
        jaggery: {
            emoji: '🍯',
            label: 'Sweet Jaggery Lump',
            count: '48 Worker Ants',
            trail: 'Super Strong 🔥',
            strategy: 'Direct Licking & Liquid Swallowing',
            pathStroke: '#fbbf24',
            antsHtml: `
                <text x="140" y="160" font-size="18">🐜</text>
                <text x="190" y="145" font-size="18">🐜</text>
                <text x="240" y="135" font-size="18">🐜</text>
                <text x="300" y="132" font-size="18">🐜</text>
                <text x="360" y="145" font-size="18">🐜</text>
                <text x="420" y="152" font-size="18">🐜</text>
                <text x="470" y="145" font-size="18">🐜</text>
                <text x="515" y="140" font-size="18">🐜</text>
                <text x="555" y="135" font-size="18">🐜</text>
                <text x="590" y="130" font-size="18">🐜</text>
            `
        },
        chips: {
            emoji: '🍟',
            label: 'Oily Sev / Potato Chips',
            count: '24 Worker Ants',
            trail: 'Moderate Trail 🌾',
            strategy: 'Cutting Crumb Pieces & Carrying',
            pathStroke: '#f97316',
            antsHtml: `
                <text x="160" y="155" font-size="18">🐜</text>
                <text x="250" y="138" font-size="18">🐜</text>
                <text x="340" y="140" font-size="18">🐜</text>
                <text x="430" y="150" font-size="18">🐜</text>
                <text x="520" y="140" font-size="18">🐜</text>
                <text x="575" y="135" font-size="18">🐜</text>
            `
        },
        grains: {
            emoji: '🌾',
            label: 'Dry Rice Grain',
            count: '8 Worker Ants',
            trail: 'Faint Scout Trail 🔍',
            strategy: 'Team Lifting Overhead',
            pathStroke: '#38bdf8',
            antsHtml: `
                <text x="180" y="150" font-size="18">🐜</text>
                <text x="320" y="135" font-size="18">🐜</text>
                <text x="460" y="145" font-size="18">🐜</text>
                <text x="550" y="138" font-size="18">🐜</text>
            `
        },
        lemon: {
            emoji: '🍋',
            label: 'Sour Citrus Lemon',
            count: '0 Ants (Repelled)',
            trail: 'No Scent Trail ❌',
            strategy: 'Avoidance (Ants dislike strong acid)',
            pathStroke: '#64748b',
            antsHtml: `
                <text x="130" y="160" font-size="18" opacity="0.3">🐜</text>
            `
        }
    };

    const entry = data[food];
    if (!entry) return;

    ['jaggery', 'chips', 'grains', 'lemon'].forEach(k => {
        const btn = document.getElementById('btn-ant-' + k);
        if (btn) {
            btn.className = (k === food)
                ? 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-2.5 text-left'
                : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2.5 text-left';
        }
    });

    document.getElementById('ant-food-emoji').textContent = entry.emoji;
    document.getElementById('ant-food-label').textContent = entry.label;
    document.getElementById('ant-count').textContent = entry.count;
    document.getElementById('ant-trail-strength').textContent = entry.trail;
    document.getElementById('ant-strategy').textContent = entry.strategy;

    const path = document.getElementById('pheromone-path');
    if (path) path.setAttribute('stroke', entry.pathStroke);

    const group = document.getElementById('marching-ants-group');
    if (group) group.innerHTML = entry.antsHtml;
}
</script>
"""

# Simulator 12: Talking Tree Friends (Mindfulness Tree Friendship Sanctuary)
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌳</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Adopt-a-Tree Friendship Sanctuary</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Mindful Nature Connection</span>
    </div>

    <p class="text-xs text-slate-300">Click on different zones of your adopted Banyan Tree friend to experience its temperature cooling, trunk texture, and canopy life!</p>

    <!-- Zone Exploration Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="exploreTreeZone('trunk')" id="btn-tree-trunk" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-2">
            <span class="text-xl">🪵</span>
            <span>Trunk & Bark</span>
        </button>
        <button onclick="exploreTreeZone('canopy')" id="btn-tree-canopy" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2">
            <span class="text-xl">🍃</span>
            <span>Shade & Cooling</span>
        </button>
        <button onclick="exploreTreeZone('creatures')" id="btn-tree-creatures" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2">
            <span class="text-xl">🕊️</span>
            <span>Branch Residents</span>
        </button>
        <button onclick="exploreTreeZone('whisper')" id="btn-tree-whisper" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2">
            <span class="text-xl">💚</span>
            <span>Whisper Kindness</span>
        </button>
    </div>

    <!-- Tree Sanctuary SVG Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 240" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Sky & Ground -->
            <rect x="0" y="0" width="700" height="190" fill="#0f172a" />
            <rect x="0" y="190" width="700" height="50" fill="#14532d" />
            <line x1="0" y1="190" x2="700" y2="190" stroke="#16a34a" stroke-width="2" />

            <!-- Sun -->
            <circle cx="620" cy="50" r="30" fill="#fbbf24" opacity="0.6" />
            <text x="605" y="58" font-size="28">☀️</text>

            <!-- Grand Banyan Tree -->
            <!-- Roots into Ground -->
            <path d="M 280 200 Q 230 220 180 235" stroke="#78350f" stroke-width="8" fill="none" />
            <path d="M 420 200 Q 470 220 520 235" stroke="#78350f" stroke-width="8" fill="none" />

            <!-- Wide Trunk -->
            <path d="M 290 190 Q 320 120 280 80 L 420 80 Q 380 120 410 190 Z" fill="#5c2d16" stroke="#3e1b0c" stroke-width="3" />
            <!-- Bark Textures -->
            <path d="M 320 160 Q 340 130 330 100" stroke="#3e1b0c" stroke-width="2" fill="none" />
            <path d="M 370 170 Q 360 140 375 110" stroke="#3e1b0c" stroke-width="2" fill="none" />

            <!-- Lush Canopy Clouds -->
            <g id="tree-canopy-group" class="cursor-pointer" onclick="exploreTreeZone('canopy')">
                <circle cx="250" cy="70" r="60" fill="#15803d" />
                <circle cx="450" cy="70" r="60" fill="#15803d" />
                <circle cx="350" cy="50" r="80" fill="#16a34a" />
                <circle cx="300" cy="40" r="50" fill="#22c55e" opacity="0.5" />
                <circle cx="400" cy="40" r="50" fill="#22c55e" opacity="0.5" />
            </g>

            <!-- Hanging Prop Aerial Roots -->
            <line x1="220" y1="80" x2="210" y2="190" stroke="#78350f" stroke-width="4" stroke-dasharray="8,4" />
            <line x1="480" y1="80" x2="490" y2="190" stroke="#78350f" stroke-width="4" stroke-dasharray="8,4" />

            <!-- Branch Animals (Toggleable highlight) -->
            <g id="tree-animals-group">
                <text x="320" y="45" font-size="24">🕊️</text>
                <text x="210" y="110" font-size="22">🐿️</text>
                <text x="460" y="105" font-size="22">🦜</text>
            </g>

            <!-- Human Explorer Embracing Trunk -->
            <g transform="translate(370, 140)">
                <circle cx="20" cy="-10" r="12" fill="#fed7aa" />
                <path d="M 10 2 Q -10 10 -15 25" stroke="#3b82f6" stroke-width="4" fill="none" />
                <path d="M 20 2 L 20 40 L 12 50" stroke="#3b82f6" stroke-width="4" fill="none" />
                <text x="5" y="-2" font-size="12">😊</text>
            </g>

            <!-- Environmental Indicators -->
            <g transform="translate(60, 40)">
                <rect x="0" y="0" width="120" height="70" rx="8" fill="#1e293b" opacity="0.9" stroke="#475569" />
                <text x="10" y="22" fill="#94a3b8" font-size="10">Open Sun Temp:</text>
                <text x="10" y="40" fill="#f87171" font-size="14" font-weight="bold">36°C (Hot)</text>
                <text x="10" y="60" fill="#4ade80" font-size="11" font-weight="bold">Tree Shade: 28°C 🍃</text>
            </g>
        </svg>
    </div>

    <!-- Live Zone Exploration Card -->
    <div id="tree-info-box" class="bg-slate-900/90 rounded-2xl p-4 border border-emerald-800/60 flex items-start gap-3">
        <span class="text-3xl" id="tree-info-icon">🪵</span>
        <div class="space-y-1 text-xs">
            <h4 class="text-sm font-bold text-emerald-300" id="tree-info-title">Trunk Texture & Sturdy Backbone</h4>
            <p class="text-slate-300" id="tree-info-desc">Pressing your palms against the bark reveals rough grooves that protect inner water-carrying pipelines. You can feel the quiet strength of decades of growth anchoring the tree into the earth.</p>
            <div class="text-[11px] text-amber-300 font-semibold" id="tree-info-tip">💡 Activity Idea: Make a tree bark rubbing using butter paper and a soft wax crayon!</div>
        </div>
    </div>
</div>

<script>
function exploreTreeZone(zone) {
    const zones = {
        trunk: {
            icon: '🪵',
            title: 'Trunk Texture & Sturdy Backbone',
            desc: 'Pressing your palms against the bark reveals rough grooves that protect inner water-carrying pipelines. You can feel the quiet strength of decades of growth anchoring the tree into the earth.',
            tip: '💡 Activity Idea: Make a tree bark rubbing using butter paper and a soft wax crayon!'
        },
        canopy: {
            icon: '🍃',
            title: 'Canopy Umbrella & Natural Air Conditioning',
            desc: 'The leafy canopy blocks scorching heat radiation while constantly releasing water vapor through transpiration. This cools the air beneath it by up to 8°C, providing instant relief!',
            tip: '🌡️ Science Fact: Big trees act like living green umbrellas, cooling entire school grounds and village roads.'
        },
        creatures: {
            icon: '🕊️',
            title: 'Canopy Hotel: Shelter for Multiple Generations',
            desc: 'In this single tree, doves build cozy twig platforms, squirrels shelter their pups in bark hollows, and caterpillars munch on green shoots while tiny ants patrol the branches.',
            tip: '🏡 Observation Challenge: Sit quietly for 5 minutes and count how many different animal voices you can hear!'
        },
        whisper: {
            icon: '💚',
            title: 'Whisper Kindness: The Gift of Companionship',
            desc: 'Talking gently to plants and acknowledging trees as living friends builds deep compassion. Trees respond to our love and care by providing sweet oxygen and enduring shade.',
            tip: '🤝 Friendship Pledge: Promise to water your adopted tree friend during hot summer months!'
        }
    };

    const entry = zones[zone];
    if (!entry) return;

    ['trunk', 'canopy', 'creatures', 'whisper'].forEach(k => {
        const btn = document.getElementById('btn-tree-' + k);
        if (btn) {
            btn.className = (k === zone)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-2'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2';
        }
    });

    document.getElementById('tree-info-icon').textContent = entry.icon;
    document.getElementById('tree-info-title').textContent = entry.title;
    document.getElementById('tree-info-desc').textContent = entry.desc;
    document.getElementById('tree-info-tip').textContent = entry.tip;
}
</script>
"""

# Simulator 13: Nature Guessing Games (Kinesthetic Charade Guessing Cards)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎭</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Nature Charades & Animal Role-Play Challenge</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Kinesthetic Game</span>
    </div>

    <p class="text-xs text-slate-300">Read the physical clues describing a living creature\\'s movements and sounds, act them out, and reveal the mystery nature friend!</p>

    <!-- Clue Selection Tabs -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectCharade(1)" id="btn-charade-1" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-2">
            <span>Card 1</span>
            <span class="text-[10px] text-emerald-200">The Tailor</span>
        </button>
        <button onclick="selectCharade(2)" id="btn-charade-2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2">
            <span>Card 2</span>
            <span class="text-[10px] text-slate-400">The Planter</span>
        </button>
        <button onclick="selectCharade(3)" id="btn-charade-3" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2">
            <span>Card 3</span>
            <span class="text-[10px] text-slate-400">The Heavyweight</span>
        </button>
        <button onclick="selectCharade(4)" id="btn-charade-4" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2">
            <span>Card 4</span>
            <span class="text-[10px] text-slate-400">The Voyager</span>
        </button>
    </div>

    <!-- Riddle & Guessing Stage Area -->
    <div class="bg-slate-900/90 rounded-2xl p-5 border border-slate-800 space-y-4">
        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs space-y-2">
            <div class="flex items-center gap-2 text-amber-300 font-bold text-sm">
                <span>🧩</span>
                <span id="charade-riddle-title">Riddle #1: The Feathered Needle-Worker</span>
            </div>
            <p id="charade-clue-text" class="text-slate-200 leading-relaxed italic text-xs">
                "I use my needle-sharp bill to pierce holes along the edges of broad leaves. Then I pull plant fiber threads through them to stitch a safe cradle for my chicks! Who am I?"
            </p>
            <div class="flex items-center gap-2 text-[11px] text-sky-400 font-medium">
                <span>🎭 Action Prompt:</span>
                <span id="charade-action-prompt">Pinch your fingers together like a beak and make tiny stitching motions in the air!</span>
            </div>
        </div>

        <!-- 3 Guess Options -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2" id="charade-options">
            <button onclick="checkCharadeGuess('woodpecker')" class="p-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 text-left flex items-center gap-2">
                <span>🪵</span> Woodpecker
            </button>
            <button onclick="checkCharadeGuess('tailorbird')" class="p-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 text-left flex items-center gap-2">
                <span>🧵</span> Tailorbird
            </button>
            <button onclick="checkCharadeGuess('weaverbird')" class="p-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 text-left flex items-center gap-2">
                <span>🌾</span> Baya Weaver
            </button>
        </div>

        <!-- Reveal Result Box -->
        <div id="charade-result" class="hidden p-4 rounded-xl bg-emerald-950/60 border border-emerald-600/60 text-xs space-y-2">
            <div class="flex items-center gap-2 font-bold text-emerald-300 text-sm">
                <span id="charade-result-icon">🎉</span>
                <span id="charade-result-title">Splendid deduction! It is the Tailorbird!</span>
            </div>
            <p id="charade-result-desc" class="text-slate-300">
                Tailorbirds select two large mango or fig leaves, puncture their edges with surgical precision, and stitch them with cobwebs and plant cotton fibers to make cozy enclosed nests!
            </p>
        </div>
    </div>
</div>

<script>
let currentCharade = 1;

const charadesData = {
    1: {
        title: 'Riddle #1: The Feathered Needle-Worker',
        clue: '"I use my needle-sharp bill to pierce holes along the edges of broad leaves. Then I pull plant fiber threads through them to stitch a safe cradle for my chicks! Who am I?"',
        action: 'Pinch your fingers together like a beak and make tiny stitching motions in the air!',
        correct: 'tailorbird',
        options: [
            { id: 'woodpecker', icon: '🪵', name: 'Woodpecker' },
            { id: 'tailorbird', icon: '🧵', name: 'Tailorbird' },
            { id: 'weaverbird', icon: '🌾', name: 'Baya Weaver' }
        ],
        desc: 'Tailorbirds select two large mango or fig leaves, puncture their edges with surgical precision, and stitch them with cobwebs and plant cotton fibers to make cozy enclosed nests!'
    },
    2: {
        title: 'Riddle #2: The Forgetful Forest Planter',
        clue: '"I have three stripes on my back and a twitching bushy tail. I bury crunchy nuts and acorns deep underground for winter meals, but I forget where half of them are buried! Who am I?"',
        action: 'Squat down on your haunches, hold invisible nuts to your cheeks, and rapidly dig in the soil with your hands!',
        correct: 'squirrel',
        options: [
            { id: 'rabbit', icon: '🐇', name: 'Wild Hare' },
            { id: 'squirrel', icon: '🐿️', name: 'Three-Striped Squirrel' },
            { id: 'mole', icon: '🐾', name: 'Ground Mole' }
        ],
        desc: 'By burying thousands of nuts each season and forgetting their exact hiding spots, squirrels inadvertently plant entire forests of oak, teak, and fruit trees!'
    },
    3: {
        title: 'Riddle #3: The Chemical Scent-Scout Heavyweight',
        clue: '"I can lift things twenty times heavier than my own tiny body! My sisters and I march in neat straight lines, following an invisible perfumed trail on the ground. Who am I?"',
        action: 'Put your hands over your head as if carrying a giant watermelon while walking strictly on a straight line!',
        correct: 'ant',
        options: [
            { id: 'ant', icon: '🐜', name: 'Worker Ant' },
            { id: 'beetle', icon: '🪲', name: 'Dung Beetle' },
            { id: 'termite', icon: '🦗', name: 'Termite' }
        ],
        desc: 'Worker ants have immense hydraulic neck strength and communicate using invisible pheromones to organize team lifting expeditions.'
    },
    4: {
        title: 'Riddle #4: The Cold-Weather Flying Voyager',
        clue: '"When Siberian rivers freeze solid, I flap my slender wings across high mountains. I land in Indian tea gardens every September, wagging my long tail up and down near clear streams! Who am I?"',
        action: 'Stand on one foot, stretch out your arms like wings, and gently bob your rear up and down like a wagtail!',
        correct: 'wagtail',
        options: [
            { id: 'sparrow', icon: '🐦', name: 'House Sparrow' },
            { id: 'crow', icon: '🦅', name: 'Jungle Crow' },
            { id: 'wagtail', icon: '🐤', name: 'Grey Wagtail' }
        ],
        desc: 'Grey Wagtails undertake breathtaking 4,000-kilometer intercontinental migrations from freezing subarctic rivers to warm tea estates in southern India!'
    }
};

function selectCharade(num) {
    currentCharade = num;
    const c = charadesData[num];
    if (!c) return;

    for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById('btn-charade-' + i);
        if (btn) {
            btn.className = (i === num)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-2'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2';
        }
    }

    document.getElementById('charade-riddle-title').textContent = c.title;
    document.getElementById('charade-clue-text').textContent = c.clue;
    document.getElementById('charade-action-prompt').textContent = c.action;

    const optContainer = document.getElementById('charade-options');
    optContainer.innerHTML = c.options.map(opt => `
        <button onclick="checkCharadeGuess('${opt.id}')" class="p-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 text-left flex items-center gap-2">
            <span>${opt.icon}</span> ${opt.name}
        </button>
    `).join('');

    document.getElementById('charade-result').classList.add('hidden');
}

function checkCharadeGuess(guess) {
    const c = charadesData[currentCharade];
    const resBox = document.getElementById('charade-result');
    resBox.classList.remove('hidden');

    if (guess === c.correct) {
        resBox.className = 'p-4 rounded-xl bg-emerald-950/60 border border-emerald-600/60 text-xs space-y-2';
        document.getElementById('charade-result-icon').textContent = '🎉';
        document.getElementById('charade-result-title').textContent = 'Splendid deduction! You guessed correctly!';
        document.getElementById('charade-result-desc').textContent = c.desc;
    } else {
        resBox.className = 'p-4 rounded-xl bg-rose-950/60 border border-rose-600/60 text-xs space-y-2';
        document.getElementById('charade-result-icon').textContent = '🤔';
        document.getElementById('charade-result-title').textContent = 'Not quite! Try reading the physical clues again.';
        document.getElementById('charade-result-desc').textContent = 'Observe the special action and habitat mentioned in the riddle.';
    }
}
</script>
"""

# Simulator 14: Valparai Grey Wagtails (Migratory Flight Map & Tail Waggle)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🗺️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Valparai Grey Wagtail Migration & Ecosystem Service</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Migration Tracker</span>
    </div>

    <p class="text-xs text-slate-300">Trace the thousands-kilometer autumn flight of the Grey Wagtail from frozen Siberian streams to Valparai tea plantations in Tamil Nadu!</p>

    <!-- Migration Stage Controls -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="setMigrationStage(1)" id="btn-mig-1" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-2 text-left">
            <span class="text-2xl">❄️</span>
            <div>
                <span class="text-xs block">1. Siberian Freeze</span>
                <span class="text-[10px] text-emerald-200">August Departure</span>
            </div>
        </button>
        <button onclick="setMigrationStage(2)" id="btn-mig-2" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2 text-left">
            <span class="text-2xl">🏔️</span>
            <div>
                <span class="text-xs block">2. High Mountain Pass</span>
                <span class="text-[10px] text-slate-400">Crossing Himalayas</span>
            </div>
        </button>
        <button onclick="setMigrationStage(3)" id="btn-mig-3" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2 text-left">
            <span class="text-2xl">🍵</span>
            <div>
                <span class="text-xs block">3. Valparai Arrival</span>
                <span class="text-[10px] text-slate-400">September Influx</span>
            </div>
        </button>
    </div>

    <!-- Migration Route Canvas SVG -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 240" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Geographical Map Outline Simplified -->
            <!-- North Asia / Siberia -->
            <rect x="0" y="0" width="700" height="70" fill="#1e293b" />
            <text x="50" y="35" fill="#94a3b8" font-size="12" font-weight="bold">Siberia & Northern Mountains (Subarctic Cold)</text>

            <!-- Central Mountain Belt -->
            <polygon points="120,70 180,110 240,75 320,115 400,70 480,120 560,75 640,110 700,70 700,120 0,120 0,70" fill="#334155" />
            <text x="350" y="100" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">Himalayan Ranges & Central Plateau</text>

            <!-- Indian Peninsula Green Lands -->
            <polygon points="180,120 520,120 350,230" fill="#065f46" stroke="#047857" stroke-width="2" />
            <text x="350" y="150" fill="#a7f3d0" font-size="12" font-weight="bold" text-anchor="middle">Indian Subcontinent</text>

            <!-- Valparai Marker -->
            <circle cx="340" cy="205" r="8" fill="#fbbf24" stroke="#ffffff" stroke-width="2" />
            <text x="340" y="225" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">📍 Valparai, Tamil Nadu</text>

            <!-- Flight Path Line -->
            <path id="flight-trail" d="M 120 40 Q 220 100 340 205" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,6" opacity="0.9">
                <animate attributeName="stroke-dashoffset" values="0;-24" dur="1.5s" repeatCount="indefinite" />
            </path>

            <!-- Animated Wagtail Bird Token -->
            <g id="mig-bird-token" transform="translate(120, 40)">
                <circle cx="0" cy="0" r="14" fill="#0284c7" stroke="#ffffff" stroke-width="2" />
                <text x="-8" y="6" font-size="16">🐤</text>
            </g>

            <!-- Tail Wagging Closeup Inset -->
            <g transform="translate(520, 130)">
                <rect x="0" y="0" width="160" height="95" rx="8" fill="#1e293b" stroke="#475569" />
                <text x="80" y="18" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">Tail-Bobbing Motion</text>
                <!-- Stylized Bird Body -->
                <ellipse cx="60" cy="55" rx="25" ry="15" fill="#64748b" />
                <circle cx="45" cy="45" r="10" fill="#94a3b8" />
                <!-- Wagging Tail Animation -->
                <line x1="85" y1="55" x2="140" y2="50" stroke="#facc15" stroke-width="4" stroke-linecap="round">
                    <animateTransform attributeName="transform" type="rotate" values="0 85 55; 15 85 55; -15 85 55; 0 85 55" dur="0.8s" repeatCount="indefinite" />
                </line>
                <text x="80" y="85" fill="#38bdf8" font-size="9" text-anchor="middle">Flushes hiding tea pests!</text>
            </g>
        </svg>
    </div>

    <!-- Live Migration Information Card -->
    <div id="mig-info-card" class="bg-slate-900/90 rounded-2xl p-4 border border-emerald-800/60 text-xs space-y-1">
        <div class="flex items-center gap-2 text-emerald-300 font-bold text-sm">
            <span id="mig-info-icon">❄️</span>
            <span id="mig-info-title">Stage 1: Autumn Departure from Siberia</span>
        </div>
        <p id="mig-info-desc" class="text-slate-300">
            As Arctic cold arrives in August, freezing shallow streams and hiding insects under ice, Grey Wagtails gather energy and embark on an epic flight southwards to find food and sunshine.
        </p>
        <div class="text-[11px] text-amber-300 font-semibold" id="mig-info-fact">
            🌟 Migration Distance: Over 4,000 kilometers navigated using earth\\'s magnetic field and stars!
        </div>
    </div>
</div>

<script>
function setMigrationStage(stage) {
    const stages = {
        1: {
            x: 120, y: 40,
            icon: '❄️',
            title: 'Stage 1: Autumn Departure from Siberia',
            desc: 'As Arctic cold arrives in August, freezing shallow streams and hiding insects under ice, Grey Wagtails gather energy and embark on an epic flight southwards to find food and sunshine.',
            fact: '🌟 Migration Distance: Over 4,000 kilometers navigated using earth\\'s magnetic field and stars!'
        },
        2: {
            x: 230, y: 110,
            icon: '🏔️',
            title: 'Stage 2: Crossing Mountain Passes & Plains',
            desc: 'Flying day and night, the slender birds cross high altitude Himalayan valleys and the fertile plains of India, resting briefly near freshwater lakes to refuel on midges.',
            fact: '🌬️ High Altitude Flight: These tiny 20-gram birds can fly through mountain passes higher than 3,000 meters!'
        },
        3: {
            x: 340, y: 205,
            icon: '🍵',
            title: 'Stage 3: Joyful Arrival in Valparai Tea Estates',
            desc: 'Every late September, like clockwork, the Grey Wagtails arrive in the lush hills of Valparai, Tamil Nadu. Their presence signals the turning of seasons to local children and planters.',
            fact: '🌱 Eco-Benefactor: Their constant tail-bobbing stirs up leafhoppers in tea bushes, reducing insect damage naturally!'
        }
    };

    const s = stages[stage];
    if (!s) return;

    for (let i = 1; i <= 3; i++) {
        const btn = document.getElementById('btn-mig-' + i);
        if (btn) {
            btn.className = (i === stage)
                ? 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-2 text-left'
                : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2 text-left';
        }
    }

    const token = document.getElementById('mig-bird-token');
    if (token) {
        token.setAttribute('transform', `translate(${s.x}, ${s.y})`);
    }

    document.getElementById('mig-info-icon').textContent = s.icon;
    document.getElementById('mig-info-title').textContent = s.title;
    document.getElementById('mig-info-desc').textContent = s.desc;
    document.getElementById('mig-info-fact').textContent = s.fact;
}
</script>
"""

# Simulator 15: Welcoming Migrant Birds (School Welcome Festival & Citizen Science Tracker)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎊</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Schoolyard Migratory Bird Welcome Celebration</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Community Action</span>
    </div>

    <p class="text-xs text-slate-300">Take action as school eco-club students to welcome weary migratory birds with food, clean water, and celebratory awareness!</p>

    <!-- School Activity Action Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="triggerSchoolAction('banner')" id="btn-sch-banner" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-2 text-left">
            <span class="text-2xl">🎨</span>
            <div>
                <span class="text-xs block">Welcome Poster</span>
                <span class="text-[10px] text-emerald-200">Draw Colorful Banners</span>
            </div>
        </button>
        <button onclick="triggerSchoolAction('water')" id="btn-sch-water" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2 text-left">
            <span class="text-2xl">🥣</span>
            <div>
                <span class="text-xs block">Clean Birdbath</span>
                <span class="text-[10px] text-slate-400">Fresh Water Pot</span>
            </div>
        </button>
        <button onclick="triggerSchoolAction('sweets')" id="btn-sch-sweets" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2 text-left">
            <span class="text-2xl">🍬</span>
            <div>
                <span class="text-xs block">Share Sweets</span>
                <span class="text-[10px] text-slate-400">Celebrate Arrival Day</span>
            </div>
        </button>
        <button onclick="triggerSchoolAction('calendar')" id="btn-sch-calendar" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2 text-left">
            <span class="text-2xl">📅</span>
            <div>
                <span class="text-xs block">Date Logger</span>
                <span class="text-[10px] text-slate-400">Citizen Science Log</span>
            </div>
        </button>
    </div>

    <!-- Schoolyard Festival SVG Canvas -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 240" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- School Courtyard Background -->
            <rect x="0" y="0" width="700" height="190" fill="#0f172a" />
            <rect x="0" y="190" width="700" height="50" fill="#334155" />

            <!-- School Building in Background -->
            <polygon points="50,90 200,40 350,90" fill="#1e293b" stroke="#475569" stroke-width="2" />
            <rect x="70" y="90" width="260" height="100" fill="#0f172a" stroke="#334155" stroke-width="2" />
            <text x="200" y="80" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">VALPARAI ECO-CLUB SCHOOL</text>

            <!-- Tree on Right Side -->
            <path d="M 520 190 Q 530 130 520 90 L 550 90 Q 540 130 550 190 Z" fill="#78350f" />
            <circle cx="535" cy="70" r="50" fill="#15803d" />

            <!-- Welcome Banner (Toggleable) -->
            <g id="sch-banner-elem">
                <rect x="150" y="105" width="280" height="36" rx="6" fill="#fbbf24" stroke="#d97706" stroke-width="2" />
                <text x="290" y="128" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">🎉 VANAKKAM! WELCOME WAGTAIL FRIENDS! 🐦</text>
            </g>

            <!-- Bird Water Basin (Toggleable) -->
            <g id="sch-water-elem" transform="translate(430, 160)">
                <ellipse cx="25" cy="25" rx="28" ry="12" fill="#38bdf8" stroke="#0284c7" stroke-width="2" />
                <rect x="22" y="25" width="6" height="20" fill="#94a3b8" />
                <text x="25" y="12" font-size="18" text-anchor="middle">🐦</text>
            </g>

            <!-- Students Celebrating in Courtyard -->
            <g transform="translate(120, 150)">
                <circle cx="15" cy="0" r="10" fill="#fde047" />
                <path d="M 15 10 L 15 35 L 5 45" stroke="#38bdf8" stroke-width="3" />
                <text x="10" y="3" font-size="10">👧</text>
            </g>
            <g transform="translate(160, 150)">
                <circle cx="15" cy="0" r="10" fill="#fde047" />
                <path d="M 15 10 L 15 35 L 25 45" stroke="#34d399" stroke-width="3" />
                <text x="10" y="3" font-size="10">👦</text>
            </g>

            <!-- Sweets Plate (Toggleable) -->
            <g id="sch-sweets-elem" transform="translate(200, 165)">
                <ellipse cx="20" cy="15" rx="18" ry="8" fill="#e2e8f0" stroke="#cbd5e1" />
                <text x="10" y="14" font-size="16">🍬</text>
            </g>

            <!-- Calendar Display -->
            <g transform="translate(590, 30)">
                <rect x="0" y="0" width="95" height="75" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
                <rect x="0" y="0" width="95" height="20" fill="#0284c7" />
                <text x="47" y="14" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">SEPTEMBER</text>
                <text x="47" y="50" fill="#fbbf24" font-size="24" font-weight="bold" text-anchor="middle">24</text>
                <text x="47" y="68" fill="#94a3b8" font-size="8" text-anchor="middle">Arrival Day</text>
            </g>
        </svg>
    </div>

    <!-- Live Action Feedback Box -->
    <div id="sch-action-box" class="bg-slate-900/90 rounded-2xl p-4 border border-emerald-800/60 text-xs space-y-1">
        <div class="flex items-center gap-2 text-emerald-300 font-bold text-sm">
            <span id="sch-action-icon">🎨</span>
            <span id="sch-action-title">Welcome Banners & Awareness Art</span>
        </div>
        <p id="sch-action-desc" class="text-slate-300">
            Students paint vibrant signs reminding everyone that migrating birds have travelled thousands of miles, are exhausted, and need safe, undisturbed surroundings.
        </p>
        <div class="text-[11px] text-amber-300 font-semibold" id="sch-action-fact">
            💡 Value: Empathy turns children into active guardians of wildlife and nature!
        </div>
    </div>
</div>

<script>
function triggerSchoolAction(action) {
    const actions = {
        banner: {
            icon: '🎨',
            title: 'Welcome Banners & Awareness Art',
            desc: 'Students paint vibrant signs reminding everyone that migrating birds have travelled thousands of miles, are exhausted, and need safe, undisturbed surroundings.',
            fact: '💡 Value: Empathy turns children into active guardians of wildlife and nature!'
        },
        water: {
            icon: '🥣',
            title: 'Fresh Water Birdbaths & Feeding Shelves',
            desc: 'Clay pots filled with fresh clean water provide thirsty avian travellers with drinking water and a place to wash dusty feathers after their strenuous journey.',
            fact: '💧 Eco Tip: Change water pots daily to keep mosquitoes away and ensure clean water for birds!'
        },
        sweets: {
            icon: '🍬',
            title: 'Community Celebration & Sweet Distribution',
            desc: 'Teachers and students celebrate the arrival of the Grey Wagtails by sharing sweets and jaggery treats, honoring the punctual return of their seasonal winged friends.',
            fact: '🎊 Cultural Harmony: Celebrating animal arrivals makes wildlife conservation a joyous community festival!'
        },
        calendar: {
            icon: '📅',
            title: 'Citizen Science Arrival Date Logger',
            desc: 'Children mark the exact calendar date of the first wagtail sighting each year, helping scientists monitor climate change patterns and bird migration schedules.',
            fact: '📊 Scientific Fact: Students have recorded wagtails arriving in Valparai between Sept 20 and 26 for decades!'
        }
    };

    const entry = actions[action];
    if (!entry) return;

    ['banner', 'water', 'sweets', 'calendar'].forEach(k => {
        const btn = document.getElementById('btn-sch-' + k);
        if (btn) {
            btn.className = (k === action)
                ? 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex items-center gap-2 text-left'
                : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2 text-left';
        }
    });

    document.getElementById('sch-action-icon').textContent = entry.icon;
    document.getElementById('sch-action-title').textContent = entry.title;
    document.getElementById('sch-action-desc').textContent = entry.desc;
    document.getElementById('sch-action-fact').textContent = entry.fact;
}
</script>
"""

# Simulator 16: Harmonious Living Ethic (Universal Harmony Synthesis Hub)
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🕊️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Four Pillars of Harmonious Living & Earth Pledge</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Master Synthesis</span>
    </div>

    <p class="text-xs text-slate-300">Activate all four core pillars of living in harmony with nature to generate your official Junior Nature Guardian Pledge!</p>

    <!-- Four Pillars Selector Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="toggleHarmonyPillar(1)" id="btn-pillar-1" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex flex-col items-center text-center">
            <span class="text-2xl mb-1">❤️</span>
            <span class="text-xs">1. Ahimsa & Kindness</span>
            <span class="text-[10px] text-emerald-200">Never Hurt Creatures</span>
        </button>
        <button onclick="toggleHarmonyPillar(2)" id="btn-pillar-2" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center text-center">
            <span class="text-2xl mb-1">🤝</span>
            <span class="text-xs">2. Shared Commons</span>
            <span class="text-[10px] text-slate-400">Share Water & Space</span>
        </button>
        <button onclick="toggleHarmonyPillar(3)" id="btn-pillar-3" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center text-center">
            <span class="text-2xl mb-1">🏡</span>
            <span class="text-xs">3. Habitat Care</span>
            <span class="text-[10px] text-slate-400">Protect Green Homes</span>
        </button>
        <button onclick="toggleHarmonyPillar(4)" id="btn-pillar-4" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center text-center">
            <span class="text-2xl mb-1">🌍</span>
            <span class="text-xs">4. Zero Waste</span>
            <span class="text-[10px] text-slate-400">Recycle & Compost</span>
        </button>
    </div>

    <!-- Synthesis Visual Canvas SVG -->
    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 240" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Central Earth Sphere -->
            <circle cx="350" cy="120" r="55" fill="#0284c7" stroke="#38bdf8" stroke-width="3" />
            <!-- Continents -->
            <path d="M 330 90 Q 360 80 375 100 Q 380 130 350 150 Q 330 140 330 90 Z" fill="#22c55e" opacity="0.8" />
            <path d="M 320 120 Q 330 160 350 170 Q 315 150 320 120 Z" fill="#22c55e" opacity="0.8" />
            <text x="350" y="126" font-size="28" text-anchor="middle">🌏</text>

            <!-- 4 Orbiting Satellite Pillars -->
            <!-- Pillar 1: Compassion -->
            <g id="orbit-pillar-1" class="cursor-pointer" onclick="toggleHarmonyPillar(1)">
                <circle cx="160" cy="70" r="35" fill="#1e293b" stroke="#ef4444" stroke-width="2.5" />
                <text x="160" y="77" font-size="24" text-anchor="middle">❤️</text>
                <text x="160" y="118" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">Ahimsa</text>
                <line x1="195" y1="85" x2="300" y2="105" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4" />
            </g>

            <!-- Pillar 2: Shared Resources -->
            <g id="orbit-pillar-2" class="cursor-pointer" onclick="toggleHarmonyPillar(2)">
                <circle cx="540" cy="70" r="35" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5" />
                <text x="540" y="77" font-size="24" text-anchor="middle">🥣</text>
                <text x="540" y="118" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">Sharing</text>
                <line x1="505" y1="85" x2="400" y2="105" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4" />
            </g>

            <!-- Pillar 3: Habitat Care -->
            <g id="orbit-pillar-3" class="cursor-pointer" onclick="toggleHarmonyPillar(3)">
                <circle cx="160" cy="170" r="35" fill="#1e293b" stroke="#22c55e" stroke-width="2.5" />
                <text x="160" y="177" font-size="24" text-anchor="middle">🌳</text>
                <text x="160" y="218" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Habitats</text>
                <line x1="195" y1="155" x2="300" y2="135" stroke="#22c55e" stroke-width="2" stroke-dasharray="4,4" />
            </g>

            <!-- Pillar 4: Zero Waste -->
            <g id="orbit-pillar-4" class="cursor-pointer" onclick="toggleHarmonyPillar(4)">
                <circle cx="540" cy="170" r="35" fill="#1e293b" stroke="#eab308" stroke-width="2.5" />
                <text x="540" y="177" font-size="24" text-anchor="middle">🔄</text>
                <text x="540" y="218" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">No Waste</text>
                <line x1="505" y1="155" x2="400" y2="135" stroke="#eab308" stroke-width="2" stroke-dasharray="4,4" />
            </g>

            <text x="350" y="232" fill="#94a3b8" font-size="11" text-anchor="middle">✨ All life is interconnected in one vast family: Vasudhaiva Kutumbakam ✨</text>
        </svg>
    </div>

    <!-- Active Pillar Description / Official Certificate Box -->
    <div id="pillar-card" class="bg-gradient-to-r from-emerald-950/60 to-slate-900/90 rounded-2xl p-4 border border-emerald-600/50 text-xs space-y-2">
        <div class="flex items-center justify-between pb-1.5 border-b border-emerald-700/40">
            <span class="font-bold text-emerald-300 text-sm flex items-center gap-2">
                <span id="pillar-icon">❤️</span>
                <span id="pillar-title">Pillar 1: Ahimsa & Universal Kindness</span>
            </span>
            <span class="text-[10px] bg-emerald-900/80 text-emerald-200 px-2 py-0.5 rounded border border-emerald-700">Earth Ethic</span>
        </div>
        <p id="pillar-desc" class="text-slate-300">
            Never cause harm, throw stones, or destroy nests. Recognize that every stray puppy, crawling caterpillar, chirping sparrow, and buzzing bee has an equal right to life and happiness on this planet.
        </p>
        <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800 text-emerald-300 font-semibold text-[11px] flex items-center gap-2">
            <span>📜 Nature Guardian Oath:</span>
            <span id="pillar-oath">"I promise to walk gently upon the earth, protect defenseless creatures, and honor all forms of life."</span>
        </div>
    </div>
</div>

<script>
function toggleHarmonyPillar(p) {
    const pillars = {
        1: {
            icon: '❤️',
            title: 'Pillar 1: Ahimsa & Universal Kindness',
            desc: 'Never cause harm, throw stones, or destroy nests. Recognize that every stray puppy, crawling caterpillar, chirping sparrow, and buzzing bee has an equal right to life and happiness on this planet.',
            oath: '"I promise to walk gently upon the earth, protect defenseless creatures, and honor all forms of life."'
        },
        2: {
            icon: '🥣',
            title: 'Pillar 2: Shared Earth Commons',
            desc: 'Earth does not belong to humans alone! Keep clay water dishes in garden corners and balconies for thirsty birds and squirrels, especially during the sweltering heat of summer.',
            oath: '"I will share my water and space with wild friends, ensuring no visiting creature goes thirsty."'
        },
        3: {
            icon: '🌳',
            title: 'Pillar 3: Habitat Stewardship & Tree Care',
            desc: 'Protect local greenery! Plant native fruit and shade trees, leave hollow dead branches for owls and barbets, and ensure gardens remain safe havens with no harmful poisons.',
            oath: '"I will nurture native plant friends and safeguard natural shelters where creatures rear their young."'
        },
        4: {
            icon: '🔄',
            title: 'Pillar 4: Zero Waste & Living in Circles',
            desc: 'Emulate nature where every discarded leaf and fruit skin becomes food for soil recyclers. Refuse single-use plastics and compost food scraps to regenerate the earth.',
            oath: '"I will eliminate toxic waste, feed mother soil with organic compost, and live in cyclical balance."'
        }
    };

    const entry = pillars[p];
    if (!entry) return;

    for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById('btn-pillar-' + i);
        if (btn) {
            btn.className = (i === p)
                ? 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 shadow flex flex-col items-center text-center'
                : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex flex-col items-center text-center';
        }
    }

    document.getElementById('pillar-icon').textContent = entry.icon;
    document.getElementById('pillar-title').textContent = entry.title;
    document.getElementById('pillar-desc').textContent = entry.desc;
    document.getElementById('pillar-oath').textContent = entry.oath;
}
</script>
"""

if __name__ == "__main__":
    print(f"Generated {len(simulators_part2)} simulators for Part 2 (9 to 16).")
    for k in sorted(simulators_part2.keys()):
        print(f"Sim {k}: length {len(simulators_part2[k])} chars")
