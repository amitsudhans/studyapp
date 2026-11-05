"""
Bespoke SVG/HTML interactive simulators for NCERT Class 5 Science Chapter 4: Our School - A Happy Place
16 Interactive Simulators corresponding to Slides 1 to 16.
Zero raw LaTeX. Pure clean Unicode.
"""

SIMULATORS = {
    1: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Green Campus Explorer</span>
                <span id="sim1-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Zone: Shaded Veranda</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- School Building Main Block -->
                    <rect x="80" y="50" width="200" height="90" rx="8" fill="#1e293b" stroke="#334155" stroke-width="2"/>
                    <!-- Roof (White Reflective) -->
                    <polygon points="70,50 180,20 290,50" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                    <text x="180" y="42" text-anchor="middle" font-size="8" fill="#475569" font-weight="bold">WHITE COOL ROOF</text>

                    <!-- Interactive Campus Zones -->
                    <!-- Zone 1: Solar Panels (Top Roof) -->
                    <g onclick="selectCampusZone('solar')" class="cursor-pointer" transform="translate(130, 25)">
                        <rect x="0" y="0" width="35" height="15" rx="2" fill="#0284c7" stroke="#38bdf8"/>
                        <line x1="12" y1="0" x2="12" y2="15" stroke="#bae6fd"/>
                        <line x1="24" y1="0" x2="24" y2="15" stroke="#bae6fd"/>
                    </g>
                    <!-- Zone 2: Compost Yard (Left Ground) -->
                    <g onclick="selectCampusZone('compost')" class="cursor-pointer" transform="translate(25, 110)">
                        <rect x="0" y="0" width="40" height="35" rx="4" fill="#78350f" stroke="#b45309"/>
                        <text x="20" y="22" text-anchor="middle" font-size="14">🍂</text>
                        <text x="20" y="45" text-anchor="middle" font-size="7" fill="#fde047" font-weight="bold">Compost</text>
                    </g>
                    <!-- Zone 3: Rainwater Recharge Pit (Right Ground) -->
                    <g onclick="selectCampusZone('rainwater')" class="cursor-pointer" transform="translate(295, 110)">
                        <circle cx="20" cy="18" r="18" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
                        <text x="20" y="23" text-anchor="middle" font-size="14">💧</text>
                        <text x="20" y="45" text-anchor="middle" font-size="7" fill="#38bdf8" font-weight="bold">Recharge</text>
                    </g>
                    <!-- Zone 4: Native Neem Trees -->
                    <g onclick="selectCampusZone('trees')" class="cursor-pointer" transform="translate(45, 45)">
                        <circle cx="15" cy="15" r="20" fill="#15803d" opacity="0.9"/>
                        <circle cx="15" cy="15" r="14" fill="#22c55e" opacity="0.8"/>
                        <rect x="12" y="30" width="6" height="25" fill="#78350f"/>
                    </g>
                    <!-- Classroom Windows -->
                    <rect x="100" y="70" width="25" height="25" rx="2" fill="#38bdf8" opacity="0.7"/>
                    <rect x="140" y="70" width="25" height="25" rx="2" fill="#38bdf8" opacity="0.7"/>
                    <rect x="195" y="70" width="25" height="25" rx="2" fill="#38bdf8" opacity="0.7"/>
                    <rect x="235" y="70" width="25" height="25" rx="2" fill="#38bdf8" opacity="0.7"/>
                    <!-- Main Entrance Door -->
                    <rect x="167" y="105" width="26" height="35" rx="2" fill="#64748b"/>
                </svg>
            </div>
            <div class="grid grid-cols-4 gap-1.5">
                <button onclick="selectCampusZone('solar')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-sky-300 border border-slate-700">
                    ⚡ Solar Roof
                </button>
                <button onclick="selectCampusZone('compost')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-amber-300 border border-slate-700">
                    🍂 Compost Pit
                </button>
                <button onclick="selectCampusZone('rainwater')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-cyan-300 border border-slate-700">
                    💧 Rain Pit
                </button>
                <button onclick="selectCampusZone('trees')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-emerald-300 border border-slate-700">
                    🌳 Neem Shade
                </button>
            </div>
            <p id="sim1-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Click any zone on campus: A green school integrates renewable solar energy, composts organic food scraps, recharges rainwater aquifers, and cools classrooms naturally.
            </p>
        </div>
    """,

    2: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Student Explorer Brigades</span>
                <span id="sim2-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Active: Water Watchers</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Central Hub Ring -->
                    <circle cx="180" cy="95" r="70" fill="#0f172a" stroke="#334155" stroke-width="2"/>

                    <!-- Center Badge Display -->
                    <circle cx="180" cy="95" r="32" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
                    <text id="sim2-center-icon" x="180" y="102" text-anchor="middle" font-size="22">💧</text>

                    <!-- Orbiting Team Badges -->
                    <!-- Water Watchers (Top) -->
                    <g onclick="selectExplorerTeam('water')" class="cursor-pointer" transform="translate(180, 25)">
                        <circle cx="0" cy="0" r="16" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
                        <text x="0" y="4" text-anchor="middle" font-size="11">💧</text>
                    </g>
                    <!-- Electricity Savers (Right) -->
                    <g onclick="selectExplorerTeam('electricity')" class="cursor-pointer" transform="translate(250, 75)">
                        <circle cx="0" cy="0" r="16" fill="#b45309" stroke="#fbbf24" stroke-width="2"/>
                        <text x="0" y="4" text-anchor="middle" font-size="11">⚡</text>
                    </g>
                    <!-- Waste Warriors (Bottom Right) -->
                    <g onclick="selectExplorerTeam('waste')" class="cursor-pointer" transform="translate(225, 155)">
                        <circle cx="0" cy="0" r="16" fill="#be123c" stroke="#fb7185" stroke-width="2"/>
                        <text x="0" y="4" text-anchor="middle" font-size="11">🗑️</text>
                    </g>
                    <!-- Green Guardians (Bottom Left) -->
                    <g onclick="selectExplorerTeam('green')" class="cursor-pointer" transform="translate(135, 155)">
                        <circle cx="0" cy="0" r="16" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
                        <text x="0" y="4" text-anchor="middle" font-size="11">🌳</text>
                    </g>
                    <!-- Traffic Trackers (Left) -->
                    <g onclick="selectExplorerTeam('traffic')" class="cursor-pointer" transform="translate(110, 75)">
                        <circle cx="0" cy="0" r="16" fill="#4338ca" stroke="#818cf8" stroke-width="2"/>
                        <text x="0" y="4" text-anchor="middle" font-size="11">🚶</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-5 gap-1">
                <button onclick="selectExplorerTeam('water')" class="p-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-[9px] font-bold text-sky-300 border border-slate-700">
                    💧 Water
                </button>
                <button onclick="selectExplorerTeam('electricity')" class="p-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-[9px] font-bold text-amber-300 border border-slate-700">
                    ⚡ Power
                </button>
                <button onclick="selectExplorerTeam('waste')" class="p-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-[9px] font-bold text-rose-300 border border-slate-700">
                    🗑️ Waste
                </button>
                <button onclick="selectExplorerTeam('green')" class="p-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-[9px] font-bold text-emerald-300 border border-slate-700">
                    🌳 Green
                </button>
                <button onclick="selectExplorerTeam('traffic')" class="p-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-[9px] font-bold text-indigo-300 border border-slate-700">
                    🚶 Traffic
                </button>
            </div>
            <p id="sim2-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Water Watchers: Inspect taps, washrooms, and water coolers to detect drips, report worn washers, and ensure drinking water is never wasted.
            </p>
        </div>
    """,

    3: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Dual-Bin Waste Sorter</span>
                <span id="sim3-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Score: 4 / 4 Sorted</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Green Bin (Wet Waste) -->
                    <g transform="translate(60, 40)">
                        <path d="M 10 30 L 70 30 L 60 120 L 20 120 Z" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
                        <rect x="5" y="20" width="70" height="12" rx="3" fill="#166534"/>
                        <text x="40" y="70" text-anchor="middle" font-size="12" fill="#f0fdf4" font-weight="bold">WET</text>
                        <text x="40" y="85" text-anchor="middle" font-size="8" fill="#bbf7d0">COMPOST</text>
                        <!-- Food Peels inside -->
                        <text x="40" y="110" text-anchor="middle" font-size="14">🍌🍎</text>
                    </g>

                    <!-- Blue Bin (Dry Recyclables) -->
                    <g transform="translate(220, 40)">
                        <path d="M 10 30 L 70 30 L 60 120 L 20 120 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                        <rect x="5" y="20" width="70" height="12" rx="3" fill="#0369a1"/>
                        <text x="40" y="70" text-anchor="middle" font-size="12" fill="#f0f9ff" font-weight="bold">DRY</text>
                        <text x="40" y="85" text-anchor="middle" font-size="8" fill="#bae6fd">RECYCLE</text>
                        <!-- Paper & Bottles inside -->
                        <text x="40" y="110" text-anchor="middle" font-size="14">📄📦</text>
                    </g>

                    <!-- Active Item in Center -->
                    <g id="sim3-active-item" transform="translate(180, 80)">
                        <circle cx="0" cy="0" r="22" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
                        <text id="sim3-item-icon" x="0" y="6" text-anchor="middle" font-size="18">🍌</text>
                    </g>
                    <text id="sim3-item-name" x="180" y="125" text-anchor="middle" font-size="10" fill="#fde047" font-weight="bold">Banana Peel</text>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="sortItemToBin('green')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    🟢 Sort into Green Bin (Wet)
                </button>
                <button onclick="sortItemToBin('blue')" class="p-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-xs font-bold text-white shadow transition">
                    🔵 Sort into Blue Bin (Dry)
                </button>
            </div>
            <p id="sim3-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Source Segregation Rule: Banana peels are organic wet waste. They decompose into garden compost and must never contaminate clean paper!
            </p>
        </div>
    """,

    4: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Recycling & Dignity of Labour</span>
                <span id="sim4-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">1 Ton Paper = 17 Trees Saved</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Recycling Factory Pulper -->
                    <rect x="40" y="45" width="110" height="95" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2"/>
                    <text x="95" y="70" text-anchor="middle" font-size="10" fill="#38bdf8" font-weight="bold">Paper Mill Pulper</text>
                    <text x="95" y="95" text-anchor="middle" font-size="20">🗞️ ➔ 📚</text>
                    <text x="95" y="125" text-anchor="middle" font-size="8" fill="#94a3b8">Recycled Notebooks</text>

                    <!-- Green Forest Saved -->
                    <g transform="translate(200, 45)">
                        <rect x="0" y="0" width="120" height="95" rx="8" fill="#064e3b" stroke="#059669" stroke-width="2"/>
                        <circle cx="35" cy="40" r="18" fill="#10b981"/>
                        <circle cx="65" cy="35" r="22" fill="#22c55e"/>
                        <circle cx="95" cy="42" r="16" fill="#10b981"/>
                        <rect x="58" y="55" width="12" height="30" fill="#78350f"/>
                        <text x="60" y="110" text-anchor="middle" font-size="9" fill="#a7f3d0" font-weight="bold">17 Living Trees Spared!</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="triggerGratitudeAction('thank')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                    🤝 Greet Sanitation Staff
                </button>
                <button onclick="triggerGratitudeAction('clean')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    🧹 Clean Personal Desk
                </button>
            </div>
            <p id="sim4-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Dignity of Labour: Sanitation workers protect public health and recyclers save forest trees. We honor them by saying thank you and keeping desks tidy!
            </p>
        </div>
    """,

    5: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Passive Thermal Cooling Model</span>
                <span id="sim5-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Cool Roof: 28°C (Breezy)</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Classroom Cross-Section -->
                    <rect x="70" y="60" width="220" height="95" fill="#1e293b" stroke="#475569" stroke-width="2"/>

                    <!-- Roof Slab (Changes White vs Black) -->
                    <rect id="sim5-roof" x="65" y="45" width="230" height="15" rx="3" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                    <text id="sim5-roof-label" x="180" y="56" text-anchor="middle" font-size="8" fill="#475569" font-weight="bold">WHITE REFLECTIVE ROOF (85% REFLECTED)</text>

                    <!-- Windows (Open for Cross-Ventilation) -->
                    <rect id="sim5-win-left" x="80" y="80" width="25" height="35" rx="2" fill="#38bdf8" opacity="0.8"/>
                    <rect id="sim5-win-right" x="255" y="80" width="25" height="35" rx="2" fill="#38bdf8" opacity="0.8"/>

                    <!-- Breeze Air Stream -->
                    <path id="sim5-breeze" d="M 40 95 Q 180 90 320 95" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,4" fill="none"/>

                    <!-- Temperature Display -->
                    <rect x="135" y="90" width="90" height="32" rx="6" fill="#0f172a" stroke="#334155"/>
                    <text id="sim5-temp-text" x="180" y="111" text-anchor="middle" font-size="14" fill="#38bdf8" font-weight="bold">28°C</text>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setCoolingMode('cool')" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                    White Roof + Windows Open (28°C)
                </button>
                <button onclick="setCoolingMode('hot')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                    Dark Roof + Closed Windows (38°C)
                </button>
            </div>
            <p id="sim5-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Passive Cooling Physics: Reflective white roof bounces 85% of solar rays away, while cross-ventilation flushes out hot indoor air!
            </p>
        </div>
    """,

    6: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Leaking Tap Accumulator</span>
                <span id="sim6-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Dripping: 30 L / Day</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Water Tap Conduit -->
                    <path d="M 80 40 L 150 40 L 150 70 L 140 70 L 140 85 L 125 85 L 125 70 L 115 70" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
                    <!-- Handle -->
                    <rect x="125" y="25" width="30" height="10" rx="3" fill="#0284c7"/>

                    <!-- Water Drips falling -->
                    <g id="sim6-drips" opacity="1">
                        <circle cx="132" cy="100" r="3" fill="#38bdf8"/>
                        <circle cx="132" cy="118" r="3.5" fill="#38bdf8"/>
                        <circle cx="132" cy="135" r="4" fill="#38bdf8"/>
                    </g>

                    <!-- Measuring Bucket / Beaker -->
                    <path d="M 105 130 L 160 130 L 152 175 L 113 175 Z" fill="#1e293b" stroke="#cbd5e1" stroke-width="2"/>
                    <rect id="sim6-water-level" x="115" y="145" width="36" height="28" fill="#0284c7" opacity="0.8"/>

                    <!-- Cumulative Counter Display -->
                    <rect x="200" y="55" width="130" height="70" rx="8" fill="#1e293b" stroke="#334155"/>
                    <text x="265" y="75" text-anchor="middle" font-size="9" fill="#94a3b8">Wasted in 24 Hours:</text>
                    <text id="sim6-volume-text" x="265" y="98" text-anchor="middle" font-size="16" fill="#f59e0b" font-weight="bold">30.2 Liters</text>
                    <text x="265" y="115" text-anchor="middle" font-size="8" fill="#f87171">10,000+ Liters / Year!</text>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setTapRepair(true)" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    🛠️ Fix Washer (Stop Leak)
                </button>
                <button onclick="setTapRepair(false)" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                    💧 Worn Gasket (Dripping)
                </button>
            </div>
            <p id="sim6-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Shocking Math: A single tap dripping once per second loses over 30 liters daily. Replacing a 5-rupee rubber washer saves 10,000 liters every year!
            </p>
        </div>
    """,

    7: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Canopy Thermometer Probe</span>
                <span id="sim7-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Neem Canopy: 34°C</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Left: Open Asphalt Playground -->
                    <rect x="20" y="130" width="150" height="45" fill="#334155"/>
                    <text x="95" y="155" text-anchor="middle" font-size="9" fill="#cbd5e1" font-weight="bold">Asphalt Court</text>
                    <!-- Blistering Sun -->
                    <circle cx="95" cy="40" r="18" fill="#f59e0b"/>
                    <path d="M 95 65 L 95 120" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>

                    <!-- Right: Mature Shady Tree -->
                    <rect x="190" y="130" width="150" height="45" fill="#1e293b"/>
                    <!-- Leafy Crown -->
                    <circle cx="265" cy="65" r="45" fill="#15803d" opacity="0.9"/>
                    <circle cx="265" cy="65" r="35" fill="#22c55e" opacity="0.8"/>
                    <rect x="259" y="105" width="12" height="30" fill="#78350f"/>
                    <text x="265" y="155" text-anchor="middle" font-size="9" fill="#86efac" font-weight="bold">Neem Shade</text>

                    <!-- Moveable Thermometer Probe -->
                    <g id="sim7-probe" transform="translate(265, 120)">
                        <rect x="-8" y="-35" width="16" height="40" rx="4" fill="#f8fafc" stroke="#dc2626" stroke-width="2"/>
                        <circle cx="0" cy="8" r="8" fill="#dc2626"/>
                        <rect id="sim7-mercury" x="-3" y="-20" width="6" height="28" fill="#dc2626"/>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setProbeLocation('asphalt')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                    Asphalt Court (Sun: 43°C)
                </button>
                <button onclick="setProbeLocation('tree')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    Neem Canopy (Shade: 34°C)
                </button>
            </div>
            <p id="sim7-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Microclimate Science: Physical shade blocks radiant heat while foliar transpiration evaporates moisture, dropping temperature by 9°C!
            </p>
        </div>
    """,

    8: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Butterfly Habitat Designer</span>
                <span id="sim8-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Planted: Nectar & Host</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Garden Soil Bed -->
                    <path d="M 40 140 Q 180 130 320 140 L 320 180 L 40 180 Z" fill="#78350f"/>

                    <!-- Left: Nectar Plants (Marigold & Zinnia) -->
                    <g id="sim8-nectar-group">
                        <circle cx="90" cy="115" r="14" fill="#f59e0b"/>
                        <circle cx="90" cy="115" r="8" fill="#ef4444"/>
                        <line x1="90" y1="125" x2="90" y2="155" stroke="#22c55e" stroke-width="3"/>
                        <circle cx="130" cy="110" r="12" fill="#ec4899"/>
                        <line x1="130" y1="120" x2="130" y2="155" stroke="#22c55e" stroke-width="3"/>
                        <text x="110" y="170" text-anchor="middle" font-size="8" fill="#fde047" font-weight="bold">Nectar (Adults)</text>
                    </g>

                    <!-- Right: Host Plants (Curry Leaf Sapling) -->
                    <g id="sim8-host-group">
                        <line x1="250" y1="90" x2="250" y2="155" stroke="#15803d" stroke-width="4"/>
                        <ellipse cx="235" cy="100" rx="14" ry="7" fill="#22c55e"/>
                        <ellipse cx="265" cy="105" rx="14" ry="7" fill="#22c55e"/>
                        <ellipse cx="238" cy="120" rx="12" ry="6" fill="#22c55e"/>
                        <ellipse cx="262" cy="125" rx="12" ry="6" fill="#22c55e"/>
                        <!-- Tiny Caterpillar -->
                        <path d="M 230 100 Q 235 96 240 100" stroke="#84cc16" stroke-width="4" stroke-linecap="round" fill="none"/>
                        <text x="250" y="170" text-anchor="middle" font-size="8" fill="#86efac" font-weight="bold">Host (Caterpillar)</text>
                    </g>

                    <!-- Flying Butterfly -->
                    <g id="sim8-butterfly" transform="translate(180, 60)">
                        <text x="0" y="0" font-size="24">🦋</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="toggleGardenPlot('both')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    Complete Habitat (Nectar + Host)
                </button>
                <button onclick="toggleGardenPlot('nectar-only')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                    Nectar Only (No Caterpillars)
                </button>
            </div>
            <p id="sim8-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Biodiversity Secret: Adult butterflies sip sweet nectar, but females lay eggs only on specific host leaves like curry leaves for baby caterpillars to hatch!
            </p>
        </div>
    """,

    9: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">School Zone Traffic Calmer</span>
                <span id="sim9-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Speed: 20 km/h (Safe Zone)</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Road with Zebra Crossing -->
                    <rect x="0" y="100" width="360" height="75" fill="#1e293b"/>
                    <!-- Zebra Stripes -->
                    <rect x="180" y="105" width="10" height="65" fill="#f8fafc"/>
                    <rect x="200" y="105" width="10" height="65" fill="#f8fafc"/>
                    <rect x="220" y="105" width="10" height="65" fill="#f8fafc"/>

                    <!-- School Gate Wall in Background -->
                    <rect x="160" y="40" width="90" height="45" rx="4" fill="#334155"/>
                    <text x="205" y="65" text-anchor="middle" font-size="8" fill="#f8fafc" font-weight="bold">SCHOOL GATE</text>

                    <!-- Moving School Van -->
                    <g id="sim9-van" transform="translate(40, 115)">
                        <rect x="0" y="0" width="60" height="30" rx="6" fill="#f59e0b" stroke="#b45309" stroke-width="2"/>
                        <circle cx="15" cy="30" r="7" fill="#0f172a"/>
                        <circle cx="45" cy="30" r="7" fill="#0f172a"/>
                        <text x="30" y="18" text-anchor="middle" font-size="8" fill="#1e293b" font-weight="bold">BUS</text>
                    </g>

                    <!-- Stopping Distance Braking Marker -->
                    <line id="sim9-brake-line" x1="100" y1="130" x2="130" y2="130" stroke="#10b981" stroke-width="4" stroke-linecap="round"/>
                    <text id="sim9-brake-text" x="115" y="145" text-anchor="middle" font-size="8" fill="#10b981" font-weight="bold">Stop in 6m</text>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setSchoolSpeed(20)" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    School Zone Speed: 20 km/h
                </button>
                <button onclick="setSchoolSpeed(50)" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                    Speeding Hazard: 50 km/h
                </button>
            </div>
            <p id="sim9-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Stopping Physics: At 20 km/h, a vehicle halts within 6 meters. At 50 km/h, it skids 25 meters, creating severe hazards for crossing students!
            </p>
        </div>
    """,

    10: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Traffic Signboard Decrypter</span>
                <span id="sim10-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Mandatory: Stop Sign</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Central Signpost Pole -->
                    <rect x="175" y="110" width="10" height="70" fill="#64748b"/>

                    <!-- Dynamic Signboard Display -->
                    <g id="sim10-sign-display">
                        <!-- Default: Red Octagonal Mandatory STOP Sign -->
                        <polygon points="150,40 210,40 235,65 235,105 210,130 150,130 125,105 125,65" fill="#dc2626" stroke="#f8fafc" stroke-width="4"/>
                        <text x="180" y="92" text-anchor="middle" font-size="18" fill="#ffffff" font-weight="extrabold">STOP</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-3 gap-1.5">
                <button onclick="selectTrafficSign('mandatory')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-rose-300 border border-slate-700">
                    🛑 Mandatory (Circle)
                </button>
                <button onclick="selectTrafficSign('cautionary')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-amber-300 border border-slate-700">
                    ⚠️ Caution (Triangle)
                </button>
                <button onclick="selectTrafficSign('informatory')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-sky-300 border border-slate-700">
                    ℹ️ Information (Box)
                </button>
            </div>
            <p id="sim10-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Mandatory Signs: Red borders give direct legal orders. Drivers must come to a complete stop before proceeding into crosswalks.
            </p>
        </div>
    """,

    11: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Fire Evacuation Floorplan</span>
                <span id="sim11-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Muster Point: 100% Accounted</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Classroom Blocks -->
                    <rect x="30" y="30" width="100" height="60" rx="4" fill="#1e293b" stroke="#334155"/>
                    <text x="80" y="65" text-anchor="middle" font-size="9" fill="#94a3b8">Class 5A</text>

                    <!-- Corridor Pathway with Green Exit Arrows -->
                    <path d="M 130 60 L 220 60 L 220 130 L 280 130" stroke="#10b981" stroke-width="4" stroke-dasharray="6,4" fill="none"/>

                    <!-- Open Assembly Field (Muster Point) -->
                    <rect x="250" y="90" width="85" height="75" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
                    <text x="292" y="125" text-anchor="middle" font-size="10" fill="#86efac" font-weight="bold">ASSEMBLY</text>
                    <text x="292" y="140" text-anchor="middle" font-size="8" fill="#bbf7d0">POINT</text>

                    <!-- Evacuating Student Dots -->
                    <g id="sim11-students">
                        <circle cx="270" cy="115" r="4" fill="#38bdf8"/>
                        <circle cx="280" cy="115" r="4" fill="#38bdf8"/>
                        <circle cx="290" cy="115" r="4" fill="#38bdf8"/>
                        <circle cx="300" cy="115" r="4" fill="#38bdf8"/>
                        <circle cx="310" cy="115" r="4" fill="#38bdf8"/>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="triggerDrillStep('evacuate')" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                    🚨 Sound Alarm (Single File Exit)
                </button>
                <button onclick="triggerDrillStep('rollcall')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    📋 Assembly Roll Call (Safe)
                </button>
            </div>
            <p id="sim11-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Orderly Drill: Walk calmly in a single file down stairs without running. Assemble on the open sports ground for attendance roll call!
            </p>
        </div>
    """,

    12: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Low-Smoke Crawl Simulator</span>
                <span id="sim12-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Action: Crawl on Hands & Knees</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Smoke Stratification Cross-Section -->
                    <!-- Ceiling Hot Toxic Smoke Zone -->
                    <rect x="40" y="25" width="280" height="65" fill="#111827" opacity="0.95"/>
                    <text x="180" y="55" text-anchor="middle" font-size="10" fill="#f87171" font-weight="bold">SUPERHEATED TOXIC SMOKE & CO GAS (RISING)</text>

                    <!-- Middle Transition Zone -->
                    <rect x="40" y="90" width="280" height="25" fill="#374151" opacity="0.6"/>

                    <!-- Bottom Cool Clean Air Layer (30-60 cm) -->
                    <rect x="40" y="115" width="280" height="45" fill="#042f2e" stroke="#059669" stroke-width="2"/>
                    <text x="180" y="142" text-anchor="middle" font-size="10" fill="#34d399" font-weight="bold">CLEANEST, COOLEST AIR ZONE (0 - 60 cm)</text>

                    <!-- Student Figure (Crawling vs Standing) -->
                    <g id="sim12-student" transform="translate(100, 130)">
                        <!-- Crawling posture -->
                        <ellipse cx="0" cy="0" rx="14" ry="6" fill="#38bdf8"/>
                        <circle cx="-12" cy="-4" r="5" fill="#fed7aa"/>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setSmokePosture('crawl')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    🧎 Crawl Low (Clean Air: Safe)
                </button>
                <button onclick="setSmokePosture('stand')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                    🚶 Standing Up (Inhaling Toxic Smoke!)
                </button>
            </div>
            <p id="sim12-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Thermal Buoyancy Physics: Hot toxic gases rise toward the ceiling. Crawling on hands and knees keeps your nose in the coolest, oxygen-rich air layer!
            </p>
        </div>
    """,

    13: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Campus Kindness & Civility</span>
                <span id="sim13-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Happiness Index: 100%</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Classroom Wooden Desk Display -->
                    <rect x="70" y="65" width="220" height="85" rx="6" fill="#78350f" stroke="#b45309" stroke-width="3"/>
                    <rect x="80" y="75" width="200" height="65" rx="4" fill="#92400e"/>

                    <!-- Clean Desk vs Scribbled Graffiti -->
                    <g id="sim13-desk-content">
                        <!-- Clean Open Notebook with Pen -->
                        <rect x="140" y="85" width="80" height="45" rx="2" fill="#f8fafc"/>
                        <line x1="180" y1="85" x2="180" y2="130" stroke="#cbd5e1"/>
                        <text x="180" y="105" text-anchor="middle" font-size="8" fill="#1e293b" font-weight="bold">CLEAN DESK</text>
                        <text x="180" y="120" text-anchor="middle" font-size="7" fill="#64748b">Respect Shared Property</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setDeskEtiquette('clean')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    Clean Desk & Queue Discipline
                </button>
                <button onclick="setDeskEtiquette('graffiti')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                    Scribbled Graffiti / Pushing
                </button>
            </div>
            <p id="sim13-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Public Stewardship: Taking turns in line and keeping wooden desks clean preserves school heritage for younger students and builds mutual respect!
            </p>
        </div>
    """,

    14: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Universal Accessibility Station</span>
                <span id="sim14-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Accessible: Gentle Ramp (1:12)</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Entrance Elevation -->
                    <rect x="230" y="70" width="100" height="90" fill="#334155"/>
                    <rect x="250" y="90" width="30" height="70" fill="#0f172a"/>

                    <!-- Gentle Ramp (1:12 slope) -->
                    <g id="sim14-ramp" opacity="1">
                        <polygon points="50,160 230,70 230,160" fill="#0284c7" opacity="0.6"/>
                        <!-- Handrail -->
                        <line x1="50" y1="140" x2="230" y2="50" stroke="#f59e0b" stroke-width="4"/>
                        <text x="140" y="130" text-anchor="middle" font-size="9" fill="#f8fafc" font-weight="bold">Ramp (1:12 Slope)</text>
                    </g>

                    <!-- Tactile Guiding Pathway -->
                    <g id="sim14-tactile" transform="translate(50, 162)">
                        <rect x="0" y="0" width="180" height="12" fill="#eab308"/>
                        <line x1="0" y1="6" x2="180" y2="6" stroke="#713f12" stroke-width="2" stroke-dasharray="4,2"/>
                    </g>

                    <!-- Wheelchair User Icon -->
                    <g id="sim14-wheelchair" transform="translate(110, 115)">
                        <circle cx="10" cy="10" r="10" fill="none" stroke="#f8fafc" stroke-width="2"/>
                        <circle cx="10" cy="-5" r="4" fill="#fed7aa"/>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setAccessibilityFeature('ramp')" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                    ♿ Ramps & Handrails (Accessible)
                </button>
                <button onclick="setAccessibilityFeature('stairs')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                    🚫 Steep Stairs Only (Blocked)
                </button>
            </div>
            <p id="sim14-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Universal Design: A gentle 1:12 slope ramp with handrails and yellow tactile floor tiles ensures that friends using wheelchairs or canes navigate freely!
            </p>
        </div>
    """,

    15: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Classroom Power Switchboard</span>
                <span id="sim15-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Daylight Mode: Fans & Lights Off</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Classroom Wall Window with Daylight -->
                    <rect x="40" y="40" width="130" height="95" rx="4" fill="#38bdf8" opacity="0.6"/>
                    <line x1="105" y1="40" x2="105" y2="135" stroke="#0f172a" stroke-width="3"/>
                    <line x1="40" y1="87" x2="170" y2="87" stroke="#0f172a" stroke-width="3"/>
                    <text x="105" y="155" text-anchor="middle" font-size="9" fill="#fde047" font-weight="bold">Natural Sunlight Inflow</text>

                    <!-- Ceiling Fan (Idle / Spinning) -->
                    <g id="sim15-fan" transform="translate(260, 60)">
                        <circle cx="0" cy="0" r="8" fill="#64748b"/>
                        <ellipse cx="-20" cy="0" rx="14" ry="4" fill="#94a3b8"/>
                        <ellipse cx="20" cy="0" rx="14" ry="4" fill="#94a3b8"/>
                        <ellipse cx="0" cy="20" rx="4" ry="14" fill="#94a3b8"/>
                    </g>

                    <!-- Watt Meter Dial -->
                    <circle cx="260" cy="130" r="28" fill="#1e293b" stroke="#334155" stroke-width="2"/>
                    <line id="sim15-meter-needle" x1="260" y1="130" x2="245" y2="115" stroke="#10b981" stroke-width="3"/>
                    <text id="sim15-watt-text" x="260" y="150" text-anchor="middle" font-size="8" fill="#10b981" font-weight="bold">0 W (Idle)</text>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setPowerState('save')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    🌞 Open Curtains (Daylight Saved)
                </button>
                <button onclick="setPowerState('waste')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                    ⚡ Idle Lights/Fans Left ON
                </button>
            </div>
            <p id="sim15-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Energy Conservation: Daylight harvesting uses free solar light. Turning off fans during recess reduces coal burning and prevents air pollution!
            </p>
        </div>
    """,

    16: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">The Campus Happiness Tree</span>
                <span id="sim16-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Tree Status: Blooming with Kindness</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Tree Trunk and Branches -->
                    <path d="M 170 170 L 170 110 Q 150 90 120 70 M 170 110 Q 185 85 200 60 M 170 110 Q 210 95 240 85" stroke="#78350f" stroke-width="12" stroke-linecap="round" fill="none"/>

                    <!-- Blooming Leaves (Eco Pledges, Kindness, Gratitude) -->
                    <g id="sim16-leaves" opacity="1">
                        <!-- Green Eco Leaves -->
                        <circle cx="115" cy="65" r="9" fill="#10b981"/>
                        <circle cx="130" cy="55" r="8" fill="#22c55e"/>
                        <!-- Pink Kindness Leaves -->
                        <circle cx="195" cy="55" r="9" fill="#f43f5e"/>
                        <circle cx="215" cy="50" r="8" fill="#fb7185"/>
                        <!-- Yellow Gratitude Leaves -->
                        <circle cx="235" cy="80" r="9" fill="#facc15"/>
                        <circle cx="250" cy="75" r="8" fill="#fde047"/>
                        <!-- Center Heart Leaf -->
                        <circle cx="170" cy="75" r="10" fill="#38bdf8"/>
                    </g>

                    <text id="sim16-leaf-count" x="180" y="150" text-anchor="middle" font-size="11" fill="#86efac" font-weight="bold">
                        150 Pledges & Kind Acts!
                    </text>
                </svg>
            </div>
            <div class="grid grid-cols-3 gap-1.5">
                <button onclick="addHappinessLeaf('eco')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-emerald-300 border border-slate-700">
                    🍃 Eco Pledge
                </button>
                <button onclick="addHappinessLeaf('kind')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-rose-300 border border-slate-700">
                    💖 Kind Action
                </button>
                <button onclick="addHappinessLeaf('gratitude')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-amber-300 border border-slate-700">
                    🙏 Thank You
                </button>
            </div>
            <p id="sim16-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Reflective Synthesis: Pin your pledge! Our school becomes a happy place when every student saves water, shares kindness, and protects our living campus.
            </p>
        </div>
    """
}

