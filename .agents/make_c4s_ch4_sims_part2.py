# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 4: Simulators Part 2 (Sims 9 to 16)
Bespoke interactive SVG/HTML simulators with Tailwind styling and clean Unicode.
"""

simulators_part2 = {
    9: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-amber-400 text-sm sm:text-base flex items-center gap-2">
                    <span>🫙</span> Himalayan Tumri Gourd Crafting Lab
                </h3>
                <p class="text-xs text-slate-400">Discover zero-waste bottle gourd vessels of Uttarakhand</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[11px] font-bold">Mountain Craft</span>
        </div>

        <!-- Tumri Visualizer -->
        <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex items-center justify-around min-h-[180px]">
            <!-- Bottle Gourd Graphic -->
            <div class="flex flex-col items-center">
                <svg class="w-32 h-36" viewBox="0 0 120 140">
                    <!-- Stem -->
                    <path d="M 60 10 Q 64 2 70 0" stroke="#713f12" stroke-width="3" fill="none"/>
                    <!-- Gourd Shape (Upper Bulb + Lower Bulb) -->
                    <path id="sim9-gourd-body" d="M 52 20 Q 42 35 48 55 Q 30 75 30 105 Q 30 135 60 135 Q 90 135 90 105 Q 90 75 72 55 Q 78 35 68 20 Z" fill="#ca8a04" stroke="#a16207" stroke-width="2.5" class="transition-colors duration-500"/>
                    <!-- Decorative Carvings / Strap -->
                    <path d="M 48 55 Q 60 62 72 55" stroke="#78350f" stroke-width="2" fill="none"/>
                    <line x1="30" y1="100" x2="90" y2="100" stroke="#78350f" stroke-width="1.5" stroke-dasharray="3,3"/>
                </svg>
                <span id="sim9-stage-name" class="text-xs font-bold text-amber-300 mt-1">Stage: Cured Tumri Vessel</span>
            </div>

            <!-- Gourd Traits -->
            <div class="space-y-2">
                <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                    <span class="text-[10px] text-slate-400 block font-semibold">Material Weight</span>
                    <span class="text-xs font-bold text-emerald-400">Ultra-Lightweight (Woody Rind)</span>
                </div>
                <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                    <span class="text-[10px] text-slate-400 block font-semibold">Spring Water Temp</span>
                    <span id="sim9-water-temp" class="text-xs font-bold text-cyan-400">14°C (Naturally Cold)</span>
                </div>
                <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                    <span class="text-[10px] text-slate-400 block font-semibold">Seed Protection</span>
                    <span class="text-xs font-bold text-amber-400">100% Weevil-Resistant</span>
                </div>
            </div>
        </div>

        <!-- 4-Stage Gourd Creation -->
        <div class="grid grid-cols-4 gap-1.5">
            <button onclick="setTumriStage(1)" class="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-[11px] font-semibold text-center transition">
                1. Fresh Gourd
            </button>
            <button onclick="setTumriStage(2)" class="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-[11px] font-semibold text-center transition">
                2. Sun Drying
            </button>
            <button onclick="setTumriStage(3)" class="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-[11px] font-semibold text-center transition">
                3. Smoke Curing
            </button>
            <button onclick="setTumriStage(4)" class="p-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 text-amber-300 border border-amber-500/40 text-[11px] font-semibold text-center transition">
                4. Water Storage
            </button>
        </div>
    </div>
    """,

    10: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-emerald-400 text-sm sm:text-base flex items-center gap-2">
                    <span>🌿</span> Forest First-Aid & Repellent Station
                </h3>
                <p class="text-xs text-slate-400">Prepare herbal remedies with neem & turmeric</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-[11px] font-bold">Natural Healing</span>
        </div>

        <!-- Remedy Display Canvas -->
        <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex items-center justify-around min-h-[170px]">
            <div id="sim10-icon-box" class="w-24 h-24 rounded-2xl bg-slate-900 border border-emerald-500/40 flex items-center justify-center text-4xl shadow-md">
                🦟
            </div>
            <div class="space-y-1.5 max-w-[200px]">
                <h4 id="sim10-title" class="font-bold text-amber-300 text-xs sm:text-sm">Neem Mosquito Shield</h4>
                <p id="sim10-desc" class="text-[11px] text-slate-300 leading-relaxed">
                    Blend cold-pressed neem seed oil with coconut oil. Apply to arms and ankles to safely repel biting mosquitoes.
                </p>
                <div id="sim10-tag" class="inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                    Active: Azadirachtin Bio-Shield
                </div>
            </div>
        </div>

        <!-- Remedy Toggles -->
        <div class="grid grid-cols-2 gap-3">
            <button onclick="setSim10Remedy('repellent')" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold text-center transition">
                🦟 Neem Mosquito Repellent
            </button>
            <button onclick="setSim10Remedy('antiseptic')" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold text-center transition">
                🩹 Turmeric Scratch Healer
            </button>
        </div>
    </div>
    """,

    11: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-amber-400 text-sm sm:text-base flex items-center gap-2">
                    <span>🌱</span> Kitchen Ayurvedic Pharmacy
                </h3>
                <p class="text-xs text-slate-400">Match healing plants with therapeutic first-aid remedies</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[11px] font-bold">Ayurvedic Botany</span>
        </div>

        <!-- Selected Remedy Card -->
        <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex items-center gap-4 min-h-[160px]">
            <div id="sim11-plant-icon" class="w-16 h-16 rounded-xl bg-emerald-950/40 border border-emerald-800/50 flex items-center justify-center text-3xl shrink-0">
                🌿
            </div>
            <div class="space-y-1">
                <div class="flex items-center gap-2">
                    <h4 id="sim11-plant-name" class="font-bold text-emerald-400 text-sm">Tulsi (Holy Basil)</h4>
                    <span id="sim11-plant-part" class="text-[10px] px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-semibold">Leaves</span>
                </div>
                <p id="sim11-remedy-use" class="text-xs text-slate-200 leading-relaxed">
                    Brewed with black pepper and honey to soothe persistent coughs, colds, and bronchial irritation.
                </p>
                <span id="sim11-compound" class="text-[10px] text-amber-400 font-semibold block">Key Compound: Eugenol & Antioxidants</span>
            </div>
        </div>

        <!-- Plant Selection Grid -->
        <div class="grid grid-cols-4 gap-2">
            <button onclick="selectHerb('tulsi')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700 text-xs font-semibold text-center transition">
                🌿 Tulsi
            </button>
            <button onclick="selectHerb('ajwain')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700 text-xs font-semibold text-center transition">
                🌾 Ajwain
            </button>
            <button onclick="selectHerb('ginger')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-orange-300 border border-slate-700 text-xs font-semibold text-center transition">
                🫚 Ginger
            </button>
            <button onclick="selectHerb('mint')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-teal-300 border border-slate-700 text-xs font-semibold text-center transition">
                🍃 Mint
            </button>
        </div>
    </div>
    """,

    12: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-amber-400 text-sm sm:text-base flex items-center gap-2">
                    <span>🪘</span> Solar Harvest Night Celebration
                </h3>
                <p class="text-xs text-slate-400">Play traditional folk percussion under clean solar lights</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[11px] font-bold">Folk Culture</span>
        </div>

        <!-- Festive Night Scene -->
        <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center relative min-h-[190px] overflow-hidden">
            <svg class="w-full max-w-sm h-40" viewBox="0 0 300 150">
                <!-- Night Sky -->
                <rect width="300" height="150" fill="#0f172a"/>
                <!-- Crescent Moon -->
                <path d="M 260 20 A 12 12 0 1 0 270 40 A 15 15 0 1 1 260 20 Z" fill="#fde047"/>

                <!-- String of Solar LED Lanterns -->
                <path d="M 20 25 Q 150 45 280 25" stroke="#475569" stroke-width="1.5" fill="none"/>
                <circle cx="50" cy="30" r="5" fill="#f59e0b" class="filter drop-shadow-[0_0_6px_rgba(245,158,11,0.8)] animate-pulse"/>
                <circle cx="100" cy="34" r="5" fill="#10b981" class="filter drop-shadow-[0_0_6px_rgba(16,185,129,0.8)] animate-pulse"/>
                <circle cx="150" cy="35" r="5" fill="#38bdf8" class="filter drop-shadow-[0_0_6px_rgba(56,189,248,0.8)] animate-pulse"/>
                <circle cx="200" cy="34" r="5" fill="#f59e0b" class="filter drop-shadow-[0_0_6px_rgba(245,158,11,0.8)] animate-pulse"/>
                <circle cx="250" cy="30" r="5" fill="#10b981" class="filter drop-shadow-[0_0_6px_rgba(16,185,129,0.8)] animate-pulse"/>

                <!-- Circular Folk Dancers (Silhouettes) -->
                <g id="sim12-dancers" class="transition-transform duration-300">
                    <circle cx="110" cy="90" r="6" fill="#f97316"/>
                    <path d="M 110 96 L 110 120 M 100 108 L 120 108 M 105 135 L 110 120 L 115 135" stroke="#f97316" stroke-width="2"/>

                    <circle cx="150" cy="85" r="6" fill="#ec4899"/>
                    <path d="M 150 91 L 150 115 M 140 103 L 160 103 M 145 130 L 150 115 L 155 130" stroke="#ec4899" stroke-width="2"/>

                    <circle cx="190" cy="90" r="6" fill="#06b6d4"/>
                    <path d="M 190 96 L 190 120 M 180 108 L 200 108 M 185 135 L 190 120 L 195 135" stroke="#06b6d4" stroke-width="2"/>
                </g>

                <!-- Sound Wave Pulses -->
                <circle id="sim12-wave" cx="150" cy="115" r="20" stroke="#fbbf24" stroke-width="2" fill="none" opacity="0" class="transition-all duration-300"/>
            </svg>

            <div id="sim12-rhythm-feedback" class="text-xs font-semibold text-amber-300 mt-2 bg-amber-950/60 px-3 py-1 rounded-full border border-amber-800/40">
                Click Dhol or Nagada below to beat the harvest rhythm!
            </div>
        </div>

        <!-- Drum Trigger Buttons -->
        <div class="grid grid-cols-2 gap-3">
            <button onclick="playHarvestDrum('dhol')" class="p-2.5 rounded-xl bg-amber-600/30 hover:bg-amber-600/50 text-amber-300 border border-amber-500/40 font-bold text-xs flex items-center justify-center gap-2 transition">
                <span>🥁</span> Beat Double-Headed Dhol
            </button>
            <button onclick="playHarvestDrum('nagada')" class="p-2.5 rounded-xl bg-cyan-600/30 hover:bg-cyan-600/50 text-cyan-300 border border-cyan-500/40 font-bold text-xs flex items-center justify-center gap-2 transition">
                <span>🪘</span> Strike Bronze Nagada
            </button>
        </div>
    </div>
    """,

    13: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-emerald-400 text-sm sm:text-base flex items-center gap-2">
                    <span>🌳</span> Protected Sacred Grove & Hydrology
                </h3>
                <p class="text-xs text-slate-400">Pristine biodiversity & aquifer recharge sponge</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-[11px] font-bold">Community Oran / Kavu</span>
        </div>

        <!-- Grove Cutaway Diagram -->
        <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center min-h-[190px]">
            <svg class="w-full max-w-sm h-40" viewBox="0 0 300 150">
                <!-- Sky & Canopy -->
                <rect x="0" y="0" width="300" height="70" fill="#0f172a"/>
                <path d="M 10 50 Q 50 15 100 35 Q 160 10 220 30 Q 270 15 290 50 L 300 70 L 0 70 Z" fill="#047857"/>

                <!-- Soil Layer (Deep Uncompacted Humus) -->
                <rect x="0" y="70" width="300" height="35" fill="#451a03"/>
                <!-- Tree Roots Sponging Rain -->
                <path d="M 60 70 Q 50 90 40 100 M 60 70 Q 75 95 85 102 M 160 70 Q 150 90 145 104 M 240 70 Q 250 95 260 104" stroke="#78350f" stroke-width="2.5" fill="none"/>

                <!-- Water Table & Aquifer Layer -->
                <rect id="sim13-aquifer" x="0" y="105" width="300" height="45" fill="#0284c7" opacity="0.8" class="transition-all duration-500"/>
                <text x="150" y="130" font-size="10" fill="#e0f2fe" font-weight="bold" text-anchor="middle">PERENNIAL VILLAGE WATER TABLE</text>

                <!-- Rain Drops falling -->
                <g id="sim13-raindrops" class="opacity-0 transition-opacity duration-300">
                    <line x1="50" y1="10" x2="48" y2="25" stroke="#38bdf8" stroke-width="2"/>
                    <line x1="120" y1="8" x2="118" y2="22" stroke="#38bdf8" stroke-width="2"/>
                    <line x1="210" y1="12" x2="208" y2="26" stroke="#38bdf8" stroke-width="2"/>
                </g>
            </svg>

            <div class="flex justify-between w-full text-[11px] text-slate-400 mt-2 px-2">
                <span>Rain Absorption: <strong id="sim13-absorb" class="text-emerald-400">95% (Natural Sponge)</strong></span>
                <span>Drinking Spring: <strong id="sim13-spring" class="text-cyan-400">Flowing Year-Round</strong></span>
            </div>
        </div>

        <button onclick="triggerGroveRain()" class="w-full py-2 rounded-xl bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 border border-emerald-500/40 text-xs font-semibold text-center transition">
            🌧️ Trigger Monsoon Rain Infiltration
        </button>
    </div>
    """,

    14: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-amber-400 text-sm sm:text-base flex items-center gap-2">
                    <span>🪔</span> Regional Nature Festivals
                </h3>
                <p class="text-xs text-slate-400">Cultural celebrations honoring trees, fruit, and wildlife</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[11px] font-bold">Stewardship</span>
        </div>

        <!-- Festival Detail Display -->
        <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex items-center gap-4 min-h-[160px]">
            <div id="sim14-badge-icon" class="w-16 h-16 rounded-xl bg-amber-950/40 border border-amber-800/50 flex items-center justify-center text-3xl shrink-0">
                🌳
            </div>
            <div class="space-y-1.5">
                <div class="flex items-center gap-2">
                    <h4 id="sim14-fest-name" class="font-bold text-amber-300 text-sm">Vat Purnima</h4>
                    <span id="sim14-region" class="text-[10px] px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-semibold">Maharashtra & Gujarat</span>
                </div>
                <p id="sim14-fest-desc" class="text-xs text-slate-200 leading-relaxed">
                    Women tie sacred threads around ancient Banyan trees, honoring their sprawling canopies that generate abundant oxygen and protect wildlife.
                </p>
                <span id="sim14-action" class="text-[10px] text-emerald-400 font-semibold block">Ecological Focus: Air Purification & Tree Longevity</span>
            </div>
        </div>

        <!-- 3 Festival Toggles -->
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setFestival('vat')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700 text-xs font-semibold text-center transition">
                🌳 Vat Purnima
            </button>
            <button onclick="setFestival('hari')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700 text-xs font-semibold text-center transition">
                🌱 Hari Jiroti
            </button>
            <button onclick="setFestival('elephant')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700 text-xs font-semibold text-center transition">
                🐘 Kaziranga Festival
            </button>
        </div>
    </div>
    """,

    15: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-emerald-400 text-sm sm:text-base flex items-center gap-2">
                    <span>📋</span> Everyday Conservation Action Tracker
                </h3>
                <p class="text-xs text-slate-400">Toggle green habits to boost your planetary eco-score</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-[11px] font-bold">Action Plan</span>
        </div>

        <!-- Score Meter -->
        <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex items-center justify-between">
            <div>
                <span class="text-xs text-slate-400">Eco-Stewardship Score</span>
                <div class="flex items-center gap-2">
                    <span id="sim15-score" class="text-2xl font-black text-emerald-400">100</span>
                    <span class="text-xs text-emerald-300 font-bold">/ 100 Points</span>
                </div>
            </div>
            <span id="sim15-badge" class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-xs font-bold">
                🌟 Forest Guardian
            </span>
        </div>

        <!-- Habit Checklist -->
        <div class="space-y-2">
            <label class="flex items-center gap-3 p-2 rounded-xl bg-slate-950 border border-slate-800 cursor-pointer">
                <input type="checkbox" id="sim15-chk-paper" checked onchange="updateSim15Score()" class="w-4 h-4 accent-emerald-500 rounded">
                <span class="text-xs text-slate-200">Write on both sides of every notebook page to save forest trees</span>
            </label>
            <label class="flex items-center gap-3 p-2 rounded-xl bg-slate-950 border border-slate-800 cursor-pointer">
                <input type="checkbox" id="sim15-chk-plastic" checked onchange="updateSim15Score()" class="w-4 h-4 accent-emerald-500 rounded">
                <span class="text-xs text-slate-200">Refuse single-use plastic bags; carry reusable unbleached cloth totes</span>
            </label>
            <label class="flex items-center gap-3 p-2 rounded-xl bg-slate-950 border border-slate-800 cursor-pointer">
                <input type="checkbox" id="sim15-chk-water" checked onchange="updateSim15Score()" class="w-4 h-4 accent-emerald-500 rounded">
                <span class="text-xs text-slate-200">Set out shallow earthenware water bowls for thirsty summer birds</span>
            </label>
            <label class="flex items-center gap-3 p-2 rounded-xl bg-slate-950 border border-slate-800 cursor-pointer">
                <input type="checkbox" id="sim15-chk-compost" checked onchange="updateSim15Score()" class="w-4 h-4 accent-emerald-500 rounded">
                <span class="text-xs text-slate-200">Compost vegetable peels and garden leaves into rich organic humus</span>
            </label>
        </div>
    </div>
    """,

    16: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-amber-400 text-sm sm:text-base flex items-center gap-2">
                    <span>🪴</span> Custom Herbal Garden Planner
                </h3>
                <p class="text-xs text-slate-400">Design sunny & shade medicinal zones with pebble paths</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[11px] font-bold">Landscape Botany</span>
        </div>

        <!-- 3x3 Garden Grid Canvas -->
        <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center">
            <div class="grid grid-cols-3 gap-2 w-full max-w-xs">
                <!-- Zone 1: Sunny -->
                <div id="sim16-cell-0" onclick="plantGardenCell(0)" class="h-16 rounded-xl bg-amber-950/30 border border-amber-800/40 flex flex-col items-center justify-center cursor-pointer hover:bg-amber-900/40 transition">
                    <span class="text-lg">🌿</span>
                    <span class="text-[10px] text-amber-300 font-bold">Tulsi (Sun)</span>
                </div>
                <!-- Zone 2: Pebble Path -->
                <div id="sim16-cell-1" onclick="plantGardenCell(1)" class="h-16 rounded-xl bg-slate-800 border border-slate-700 flex flex-col items-center justify-center cursor-pointer hover:bg-slate-700 transition">
                    <span class="text-lg">🪨</span>
                    <span class="text-[10px] text-slate-300 font-bold">Pebble Path</span>
                </div>
                <!-- Zone 3: Sunny -->
                <div id="sim16-cell-2" onclick="plantGardenCell(2)" class="h-16 rounded-xl bg-amber-950/30 border border-amber-800/40 flex flex-col items-center justify-center cursor-pointer hover:bg-amber-900/40 transition">
                    <span class="text-lg">🌼</span>
                    <span class="text-[10px] text-amber-300 font-bold">Marigold (Pest Guard)</span>
                </div>
                <!-- Zone 4: Partial Shade -->
                <div id="sim16-cell-3" onclick="plantGardenCell(3)" class="h-16 rounded-xl bg-emerald-950/30 border border-emerald-800/40 flex flex-col items-center justify-center cursor-pointer hover:bg-emerald-900/40 transition">
                    <span class="text-lg">🪴</span>
                    <span class="text-[10px] text-emerald-300 font-bold">Aloe Vera (Shade)</span>
                </div>
                <!-- Zone 5: Bird Bath Center -->
                <div id="sim16-cell-4" onclick="plantGardenCell(4)" class="h-16 rounded-xl bg-cyan-950/40 border border-cyan-800/50 flex flex-col items-center justify-center cursor-pointer hover:bg-cyan-900/50 transition">
                    <span class="text-lg">🥣</span>
                    <span class="text-[10px] text-cyan-300 font-bold">Bird Water Pot</span>
                </div>
                <!-- Zone 6: Partial Shade -->
                <div id="sim16-cell-5" onclick="plantGardenCell(5)" class="h-16 rounded-xl bg-emerald-950/30 border border-emerald-800/40 flex flex-col items-center justify-center cursor-pointer hover:bg-emerald-900/40 transition">
                    <span class="text-lg">🍃</span>
                    <span class="text-[10px] text-emerald-300 font-bold">Mint (Cool Shade)</span>
                </div>
            </div>
            <span class="text-[11px] text-slate-400 mt-2">Click any garden plot to rotate companion plants and features!</span>
        </div>

        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-xs text-slate-300 flex items-center justify-between">
            <span>Morning Sun Zone: <strong>Eastern Border</strong></span>
            <span>Companion Barrier: <strong>Marigold Nematode Guard</strong></span>
        </div>
    </div>
    """
}

out_path = ".agents/class4_science_ch4_sims_part2.py"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write("simulators_part2 = " + repr(simulators_part2) + "\n")
print(f"Simulators Part 2 written to {out_path} ({len(simulators_part2)} sims)")

