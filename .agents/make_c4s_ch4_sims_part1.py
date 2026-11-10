# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 4: Simulators Part 1 (Sims 1 to 8)
Bespoke interactive SVG/HTML simulators with Tailwind styling and clean Unicode.
"""

simulators_part1 = {
    1: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-emerald-400 text-sm sm:text-base flex items-center gap-2">
                    <span>☀️</span> Solar Microgrid Simulator
                </h3>
                <p class="text-xs text-slate-400">Harvest clean sunlight and power village illumination</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-[11px] font-bold">Interactive Energy</span>
        </div>

        <!-- Solar Microgrid Canvas -->
        <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center relative overflow-hidden min-h-[200px]">
            <svg id="sim1-svg" class="w-full max-w-md h-40" viewBox="0 0 400 160">
                <!-- Sky Background -->
                <rect id="sim1-sky" x="0" y="0" width="400" height="120" fill="#0f172a" class="transition-colors duration-500"/>
                <!-- Sun / Moon -->
                <circle id="sim1-sun" cx="200" cy="40" r="22" fill="#fbbf24" class="transition-all duration-300 filter drop-shadow-[0_0_12px_rgba(251,191,36,0.6)]"/>
                <path d="M 170 40 L 230 40 M 200 10 L 200 70 M 178 18 L 222 62 M 178 62 L 222 18" stroke="#f59e0b" stroke-width="2" opacity="0.8"/>

                <!-- Ground -->
                <rect x="0" y="120" width="400" height="40" fill="#1e293b"/>

                <!-- Village Hut 1 with Solar Panel -->
                <polygon points="50,120 70,85 110,85 130,120" fill="#78350f"/>
                <rect x="65" y="100" width="50" height="20" fill="#b45309"/>
                <polygon id="sim1-panel1" points="75,82 105,82 115,92 65,92" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>

                <!-- Central Battery Bank & LED Streetlamp -->
                <rect x="185" y="105" width="30" height="18" rx="3" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
                <line x1="200" y1="105" x2="200" y2="70" stroke="#64748b" stroke-width="3"/>
                <circle id="sim1-lamp" cx="200" cy="68" r="8" fill="#fbbf24" class="transition-all duration-300 filter drop-shadow-[0_0_10px_rgba(251,191,36,0.8)]"/>

                <!-- Village Hut 2 with Solar Panel -->
                <polygon points="270,120 290,85 330,85 350,120" fill="#78350f"/>
                <rect x="285" y="100" width="50" height="20" fill="#b45309"/>
                <polygon id="sim1-panel2" points="295,82 325,82 335,92 285,92" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>

                <!-- Power Grid Connecting Lines -->
                <path d="M 90 92 Q 140 115 185 114" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4,4" class="animate-pulse"/>
                <path d="M 310 92 Q 260 115 215 114" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4,4" class="animate-pulse"/>
            </svg>
            <div id="sim1-mode-badge" class="absolute top-2 right-2 px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                Mode: Solar Powered (Silent & Clean)
            </div>
        </div>

        <!-- Controls & Metrics -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-center">
                <span class="text-[10px] text-slate-400 font-semibold block">Solar Generation</span>
                <span id="sim1-gen-val" class="text-base font-bold text-amber-400">4.8 kW</span>
            </div>
            <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-center">
                <span class="text-[10px] text-slate-400 font-semibold block">Battery Storage</span>
                <span id="sim1-bat-val" class="text-base font-bold text-emerald-400">92%</span>
            </div>
            <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-center">
                <span class="text-[10px] text-slate-400 font-semibold block">Carbon Emissions</span>
                <span id="sim1-carbon-val" class="text-base font-bold text-cyan-400">0.0 kg (Zero)</span>
            </div>
        </div>

        <div class="space-y-2">
            <div class="flex justify-between text-xs font-semibold">
                <span class="text-slate-300">Sunlight Intensity</span>
                <span id="sim1-sun-label" class="text-amber-400">85% (Bright Sun)</span>
            </div>
            <input id="sim1-sun-slider" type="range" min="0" max="100" value="85" oninput="updateSim1(this.value)" class="w-full accent-amber-500 cursor-pointer">
        </div>

        <div class="flex gap-2">
            <button onclick="setSim1Power('solar')" class="flex-1 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 border border-emerald-500/40 font-semibold text-xs transition">
                ☀️ Solar Mode
            </button>
            <button onclick="setSim1Power('diesel')" class="flex-1 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 font-semibold text-xs transition">
                ⛽ Diesel Mode (Compare)
            </button>
        </div>
    </div>
    """,

    2: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-amber-400 text-sm sm:text-base flex items-center gap-2">
                    <span>🔥</span> Palash Tree & Pollinator Explorer
                </h3>
                <p class="text-xs text-slate-400">Discover flame of the forest blooms and wildlife visitors</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[11px] font-bold">Kesuda Botany</span>
        </div>

        <!-- Palash Tree Canvas -->
        <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center relative min-h-[220px]">
            <svg id="sim2-svg" class="w-full max-w-md h-48" viewBox="0 0 400 180">
                <!-- Hill Background -->
                <path d="M 0 160 Q 150 110 400 160 L 400 180 L 0 180 Z" fill="#1e293b"/>

                <!-- Palash Tree Trunk & Crown -->
                <path d="M 185 170 Q 190 120 180 80 Q 200 120 215 170 Z" fill="#78350f"/>
                <path d="M 180 80 Q 140 50 110 55" stroke="#78350f" stroke-width="6" fill="none"/>
                <path d="M 195 80 Q 240 50 280 55" stroke="#78350f" stroke-width="6" fill="none"/>
                <path d="M 190 75 Q 190 35 190 20" stroke="#78350f" stroke-width="5" fill="none"/>

                <!-- Clusters of Flame Blossoms -->
                <g id="sim2-blossoms" class="cursor-pointer transition-transform hover:scale-105 duration-200" onclick="clickPalashBlossom()">
                    <circle cx="110" cy="55" r="14" fill="#ea580c" opacity="0.9"/>
                    <circle cx="118" cy="50" r="11" fill="#f97316"/>
                    <path d="M 105 55 Q 95 40 115 45 Z" fill="#dc2626"/>

                    <circle cx="280" cy="55" r="14" fill="#ea580c" opacity="0.9"/>
                    <circle cx="272" cy="50" r="11" fill="#f97316"/>
                    <path d="M 285 55 Q 295 40 275 45 Z" fill="#dc2626"/>

                    <circle cx="190" cy="25" r="16" fill="#ea580c" opacity="0.9"/>
                    <circle cx="196" cy="20" r="12" fill="#f97316"/>
                    <path d="M 185 25 Q 190 10 200 18 Z" fill="#dc2626"/>

                    <circle cx="150" cy="50" r="12" fill="#f97316"/>
                    <circle cx="235" cy="48" r="12" fill="#f97316"/>
                </g>

                <!-- Visiting Pollinator (Bird / Bee) -->
                <g id="sim2-pollinator" class="transition-all duration-500" transform="translate(130, 35)">
                    <!-- Purple Sunbird -->
                    <ellipse cx="0" cy="0" rx="9" ry="6" fill="#1e1b4b"/>
                    <circle cx="7" cy="-2" r="4" fill="#312e81"/>
                    <path d="M 11 -2 Q 18 -1 20 5" stroke="#0f172a" stroke-width="1.5" fill="none"/>
                    <path d="M -7 0 L -15 -3 L -13 2 Z" fill="#1e1b4b"/>
                    <path d="M -2 -4 Q 0 -12 6 -6 Z" fill="#3b82f6" opacity="0.8"/>
                </g>
            </svg>
            <div id="sim2-feedback" class="text-xs text-amber-300 font-semibold bg-amber-950/60 px-3 py-1 rounded-full border border-amber-800/50 mt-1">
                Click on the orange blossoms to observe pollinator activity!
            </div>
        </div>

        <!-- Botanical Traits Selector -->
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setPalashView('nectar')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold text-center transition">
                🍯 Sweet Nectar
            </button>
            <button onclick="setPalashView('pollinators')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold text-center transition">
                🦜 Bird Visitors
            </button>
            <button onclick="setPalashView('dye')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold text-center transition">
                🎨 Natural Dyes
            </button>
        </div>
        <div id="sim2-desc-box" class="text-xs text-slate-300 bg-slate-950 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
            The Palash tree sheds all leaves in late winter. In spring, dense clusters of brilliant orange blossoms bloom, drawing flocks of nectar-feeding birds and pollinating insects!
        </div>
    </div>
    """,

    3: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-amber-400 text-sm sm:text-base flex items-center gap-2">
                    <span>🏡</span> Eco-House Thermal Wall Simulator
                </h3>
                <p class="text-xs text-slate-400">Compare natural clay-straw insulation vs concrete</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[11px] font-bold">Thermal Mass</span>
        </div>

        <!-- Thermal Comparison Canvas -->
        <div class="grid grid-cols-2 gap-3 bg-slate-950 p-3 rounded-xl border border-slate-800">
            <!-- Natural Earthen House -->
            <div class="flex flex-col items-center p-2 rounded-lg bg-slate-900/80 border border-emerald-500/30 space-y-1.5">
                <span class="text-xs font-bold text-emerald-400">Earthen Clay & Thatch</span>
                <div class="w-full h-24 bg-amber-950/40 rounded-lg flex flex-col items-center justify-center relative border border-amber-800/40">
                    <span class="text-2xl">🛖</span>
                    <span class="text-[10px] text-slate-400 font-semibold">Indoor Temperature</span>
                    <span id="sim3-earth-temp" class="text-base font-extrabold text-emerald-300">24°C</span>
                    <span class="text-[9px] text-emerald-400">Comfortable & Cool</span>
                </div>
            </div>

            <!-- Modern Concrete Box -->
            <div class="flex flex-col items-center p-2 rounded-lg bg-slate-900/80 border border-slate-800 space-y-1.5">
                <span class="text-xs font-bold text-slate-300">Concrete & Metal</span>
                <div class="w-full h-24 bg-slate-900 rounded-lg flex flex-col items-center justify-center relative border border-slate-800">
                    <span class="text-2xl">🏢</span>
                    <span class="text-[10px] text-slate-400 font-semibold">Indoor Temperature</span>
                    <span id="sim3-conc-temp" class="text-base font-extrabold text-rose-400">38°C</span>
                    <span class="text-[9px] text-rose-400">Trapped Solar Heat</span>
                </div>
            </div>
        </div>

        <div class="space-y-2">
            <div class="flex justify-between text-xs font-semibold">
                <span class="text-slate-300">Outdoor Summer Sun Heat</span>
                <span id="sim3-out-temp" class="text-amber-400">42°C (Blazing Afternoon)</span>
            </div>
            <input id="sim3-slider" type="range" min="15" max="45" value="42" oninput="updateSim3Thermal(this.value)" class="w-full accent-amber-500 cursor-pointer">
        </div>

        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs text-slate-300 space-y-1 leading-relaxed">
            <strong class="text-amber-400">Architectural Principle:</strong> High thermal mass earthen walls (clay, sand, straw, cow dung) absorb intense solar radiation slowly during the day, preventing indoor overheating without air conditioning!
        </div>
    </div>
    """,

    4: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-slate-100 text-sm sm:text-base flex items-center gap-2">
                    <span>🎨</span> Traditional Rice Mural Studio
                </h3>
                <p class="text-xs text-slate-400">Paint sacred folk symbols with pure white rice paste</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700 text-[11px] font-bold">Organic Pigment</span>
        </div>

        <!-- Earthen Mud Wall Canvas -->
        <div id="sim4-canvas-wall" class="w-full h-44 rounded-xl border-2 border-amber-900/60 bg-[#78350f] relative overflow-hidden flex items-center justify-center p-3 select-none">
            <svg id="sim4-svg-mural" class="w-full h-full" viewBox="0 0 360 140">
                <!-- Earthen texture background -->
                <rect width="360" height="140" fill="#78350f"/>
                <!-- Group of stamped motifs -->
                <g id="sim4-motifs-group"></g>
            </svg>
            <div id="sim4-placeholder" class="text-xs text-amber-200/70 pointer-events-none text-center">
                Select a traditional folk motif below to stamp onto the clay wall!
            </div>
        </div>

        <!-- Motif Buttons -->
        <div class="grid grid-cols-4 gap-2">
            <button onclick="stampMuralMotif('tree')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold text-center transition">
                🌳 Tree of Life
            </button>
            <button onclick="stampMuralMotif('peacock')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold text-center transition">
                🦚 Peacock
            </button>
            <button onclick="stampMuralMotif('deer')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold text-center transition">
                🦌 Forest Deer
            </button>
            <button onclick="stampMuralMotif('dancers')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold text-center transition">
                💃 Folk Dancers
            </button>
        </div>

        <div class="flex items-center justify-between text-xs pt-1">
            <span class="text-slate-400">Paint: <strong>Ground Rice Flour & Water</strong> (Zero Chemicals)</span>
            <button onclick="clearMuralWall()" class="px-3 py-1 rounded-lg bg-red-950/40 hover:bg-red-900/50 text-red-300 border border-red-800/40 font-semibold transition">
                Reset Canvas
            </button>
        </div>
    </div>
    """,

    5: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-rose-400 text-sm sm:text-base flex items-center gap-2">
                    <span>🧪</span> Botanical Dye Extraction Lab
                </h3>
                <p class="text-xs text-slate-400">Simmer natural plant petals and dye pure cotton fabric</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-rose-500/20 text-rose-300 border border-rose-500/30 text-[11px] font-bold">Natural Chemistry</span>
        </div>

        <!-- Extraction Apparatus -->
        <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex items-center justify-around min-h-[170px]">
            <!-- Simmering Pot -->
            <div class="flex flex-col items-center">
                <div class="relative">
                    <div id="sim5-steam" class="hidden absolute -top-5 left-6 text-xs text-slate-400 animate-bounce">♨️ ♨️</div>
                    <svg class="w-24 h-24" viewBox="0 0 100 100">
                        <!-- Pot -->
                        <path d="M 20 40 L 80 40 L 75 80 Q 50 90 25 80 Z" fill="#334155" stroke="#64748b" stroke-width="2"/>
                        <!-- Handles -->
                        <path d="M 16 45 Q 10 50 16 55" stroke="#64748b" stroke-width="3" fill="none"/>
                        <path d="M 84 45 Q 90 50 84 55" stroke="#64748b" stroke-width="3" fill="none"/>
                        <!-- Liquid Liquid fill -->
                        <path id="sim5-liquid" d="M 24 50 L 76 50 L 73 78 Q 50 86 27 78 Z" fill="#e2e8f0" class="transition-colors duration-500"/>
                        <!-- Campfire below -->
                        <polygon points="35,98 50,88 65,98 55,92 45,92" fill="#ea580c"/>
                        <polygon points="42,96 50,90 58,96" fill="#facc15"/>
                    </svg>
                </div>
                <span id="sim5-pot-status" class="text-[11px] font-bold text-slate-400 mt-1">Water: Cold</span>
            </div>

            <!-- Dye Swatch Result -->
            <div class="flex flex-col items-center space-y-2">
                <span class="text-xs font-bold text-slate-300">Dyed Cotton Swatch</span>
                <div id="sim5-swatch" class="w-16 h-20 rounded-md bg-white border-2 border-slate-700 shadow-md flex items-center justify-center transition-colors duration-500">
                    <span id="sim5-swatch-text" class="text-[10px] text-slate-800 font-bold">Pure White</span>
                </div>
                <span id="sim5-mordant-tag" class="text-[10px] text-emerald-400 font-semibold bg-emerald-950/40 px-2 py-0.5 rounded border border-emerald-800/40">Alum Added</span>
            </div>
        </div>

        <!-- Ingredient Selection -->
        <div class="grid grid-cols-4 gap-2">
            <button onclick="extractDye('marigold')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700 text-xs font-semibold text-center transition">
                🌼 Marigold (Yellow)
            </button>
            <button onclick="extractDye('beetroot')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700 text-xs font-semibold text-center transition">
                🍠 Beetroot (Magenta)
            </button>
            <button onclick="extractDye('hibiscus')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-red-400 border border-slate-700 text-xs font-semibold text-center transition">
                🌺 Hibiscus (Crimson)
            </button>
            <button onclick="extractDye('acacia')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-600 border border-slate-700 text-xs font-semibold text-center transition">
                🪵 Acacia (Earthy Brown)
            </button>
        </div>
    </div>
    """,

    6: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-amber-400 text-sm sm:text-base flex items-center gap-2">
                    <span>🦌</span> Indigenous Gond Patterning Studio
                </h3>
                <p class="text-xs text-slate-400">Fill tribal forest silhouettes with rhythmic dots & lines</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[11px] font-bold">Madhya Pradesh Art</span>
        </div>

        <!-- Gond Art Canvas -->
        <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center min-h-[190px]">
            <svg id="sim6-svg" class="w-full max-w-sm h-40" viewBox="0 0 300 140">
                <!-- Canvas Frame -->
                <rect width="300" height="140" fill="#fef3c7" rx="8" stroke="#d97706" stroke-width="2"/>

                <!-- Forest Deer Silhouette with dynamic pattern fill -->
                <g id="sim6-deer-art" transform="translate(60, 10)">
                    <!-- Antlers -->
                    <path d="M 60 40 Q 50 15 35 10 M 50 22 Q 40 18 35 25" stroke="#78350f" stroke-width="2.5" fill="none"/>
                    <path d="M 65 40 Q 80 15 95 10 M 75 22 Q 85 18 90 25" stroke="#78350f" stroke-width="2.5" fill="none"/>

                    <!-- Body Silhouette -->
                    <path id="sim6-body-fill" d="M 60 40 Q 75 40 85 55 L 130 65 Q 145 70 140 100 L 135 125 L 125 125 L 128 95 L 90 95 L 85 125 L 75 125 L 80 85 Q 65 85 55 70 Z" fill="#b45309" stroke="#78350f" stroke-width="2"/>

                    <!-- Inner Decorative Pattern Overlay -->
                    <g id="sim6-pattern-overlay"></g>
                </g>
            </svg>
            <div id="sim6-status" class="text-xs font-semibold text-amber-300 mt-2">
                Selected Pattern: Rhythmic Dots (Geru Red & White)
            </div>
        </div>

        <!-- Pattern Styles -->
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setGondPattern('dots')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold text-center transition">
                • • • Traditional Dots
            </button>
            <button onclick="setGondPattern('dashes')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold text-center transition">
                — — Parallel Dashes
            </button>
            <button onclick="setGondPattern('scales')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold text-center transition">
                〰️ Water Waves
            </button>
        </div>
    </div>
    """,

    7: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-emerald-400 text-sm sm:text-base flex items-center gap-2">
                    <span>🏺</span> Organic Pest Control Simulator
                </h3>
                <p class="text-xs text-slate-400">Test neem leaf lining & cow-dung plaster grain preservation</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-[11px] font-bold">Azadirachtin Science</span>
        </div>

        <!-- Storage Pot Visualizer -->
        <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex items-center justify-around min-h-[180px]">
            <!-- Terracotta Pot Graphic -->
            <div class="relative flex flex-col items-center">
                <svg class="w-32 h-36" viewBox="0 0 120 140">
                    <!-- Pot Base & Body -->
                    <path id="sim7-pot-body" d="M 40 30 L 80 30 Q 110 70 85 125 L 35 125 Q 10 70 40 30 Z" fill="#9a3412" stroke="#7c2d12" stroke-width="2.5" class="transition-colors duration-300"/>
                    <ellipse cx="60" cy="30" rx="20" ry="6" fill="#7c2d12"/>

                    <!-- Grain Contents inside -->
                    <ellipse cx="60" cy="32" rx="18" ry="4" fill="#fde047"/>

                    <!-- Neem Leaves Layer Visual -->
                    <g id="sim7-neem-layer" class="transition-opacity duration-300 opacity-100">
                        <path d="M 50 32 Q 55 24 60 30 Q 55 35 50 32 Z" fill="#15803d"/>
                        <path d="M 62 30 Q 70 24 72 32 Q 66 36 62 30 Z" fill="#16a34a"/>
                    </g>
                </svg>
            </div>

            <!-- Protection Metrics -->
            <div class="space-y-2">
                <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                    <span class="text-[10px] text-slate-400 block font-semibold">Weevil Pest Invasion</span>
                    <span id="sim7-pest-status" class="text-sm font-bold text-emerald-400">0% (Completely Repelled)</span>
                </div>
                <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                    <span class="text-[10px] text-slate-400 block font-semibold">Chemical Residue</span>
                    <span class="text-sm font-bold text-cyan-400">Zero (100% Organic & Safe)</span>
                </div>
                <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                    <span class="text-[10px] text-slate-400 block font-semibold">Grain Shelf Life</span>
                    <span id="sim7-life-status" class="text-sm font-bold text-amber-400">12+ Months</span>
                </div>
            </div>
        </div>

        <!-- Toggles -->
        <div class="grid grid-cols-2 gap-3">
            <button id="sim7-neem-btn" onclick="toggleSim7Neem()" class="p-2.5 rounded-xl bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 text-xs font-semibold text-center transition">
                🌿 Neem Lining: Active
            </button>
            <button id="sim7-plaster-btn" onclick="toggleSim7Plaster()" class="p-2.5 rounded-xl bg-amber-600/30 text-amber-300 border border-amber-500/40 text-xs font-semibold text-center transition">
                🧱 Dung Plaster: Sealed
            </button>
        </div>
    </div>
    """,

    8: """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
                <h3 class="font-bold text-amber-400 text-sm sm:text-base flex items-center gap-2">
                    <span>🐝</span> Jenu Kuruba Honey Harvest Protocol
                </h3>
                <p class="text-xs text-slate-400">Gentle apology song & brood comb preservation</p>
            </div>
            <span class="px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 text-[11px] font-bold">Karnataka Ethic</span>
        </div>

        <!-- Beehive Interactive Diagram -->
        <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center min-h-[190px] relative">
            <svg class="w-full max-w-sm h-40" viewBox="0 0 300 150">
                <!-- Cliff Branch -->
                <rect x="0" y="20" width="300" height="15" fill="#451a03"/>

                <!-- Complete Honeycomb hanging -->
                <g id="sim8-comb" transform="translate(100, 35)">
                    <!-- Outer Surplus Honey Comb (Harvestable) -->
                    <path id="sim8-outer-honey" d="M 0 0 L 100 0 Q 115 50 80 90 L 20 90 Q -15 50 0 0 Z" fill="#d97706" stroke="#b45309" stroke-width="2" class="cursor-pointer transition-opacity duration-300"/>

                    <!-- Inner Brood Comb (Sacred Nursery - Protected) -->
                    <ellipse cx="50" cy="45" rx="30" ry="25" fill="#78350f" stroke="#fbbf24" stroke-width="2"/>
                    <text x="50" y="42" font-size="9" fill="#fde047" font-weight="bold" text-anchor="middle">BROOD COMB</text>
                    <text x="50" y="54" font-size="8" fill="#e2e8f0" text-anchor="middle">Eggs & Larvae</text>
                </g>

                <!-- Calming Herbal Smoke Stream -->
                <g id="sim8-smoke" class="opacity-0 transition-opacity duration-500">
                    <path d="M 60 140 Q 70 100 90 80 Q 80 50 110 40" stroke="#94a3b8" stroke-width="6" fill="none" opacity="0.6" stroke-linecap="round"/>
                    <path d="M 80 140 Q 95 110 110 90 Q 100 65 125 50" stroke="#cbd5e1" stroke-width="4" fill="none" opacity="0.5" stroke-linecap="round"/>
                </g>

                <!-- Flying Bees -->
                <g id="sim8-bees">
                    <circle cx="85" cy="50" r="3" fill="#facc15"/><line x1="83" y1="48" x2="87" y2="48" stroke="#000" stroke-width="1"/>
                    <circle cx="215" cy="65" r="3" fill="#facc15"/><line x1="213" y1="63" x2="217" y2="63" stroke="#000" stroke-width="1"/>
                    <circle cx="160" cy="115" r="3" fill="#facc15"/><line x1="158" y1="113" x2="162" y2="113" stroke="#000" stroke-width="1"/>
                </g>
            </svg>

            <div id="sim8-prompt" class="text-xs font-semibold text-amber-300 mt-2 bg-amber-950/60 px-3 py-1 rounded-full border border-amber-800/40">
                Step 1: Sing traditional apology prayer to the bee spirits.
            </div>
        </div>

        <!-- Action Protocol Sequence -->
        <div class="grid grid-cols-3 gap-2">
            <button id="sim8-btn-song" onclick="runSim8Step('song')" class="p-2 rounded-xl bg-amber-600/30 hover:bg-amber-600/50 text-amber-300 border border-amber-500/40 text-xs font-semibold text-center transition">
                🎶 1. Apology Song
            </button>
            <button id="sim8-btn-smoke" onclick="runSim8Step('smoke')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs font-semibold text-center transition">
                💨 2. Gentle Herbal Smoke
            </button>
            <button id="sim8-btn-harvest" onclick="runSim8Step('harvest')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs font-semibold text-center transition">
                🍯 3. Slice Surplus Comb
            </button>
        </div>
    </div>
    """
}

out_path = ".agents/class4_science_ch4_sims_part1.py"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write("simulators_part1 = " + repr(simulators_part1) + "\n")
print(f"Simulators Part 1 written to {out_path} ({len(simulators_part1)} sims)")

