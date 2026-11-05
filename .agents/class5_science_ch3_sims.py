"""
Bespoke SVG/HTML interactive simulators for NCERT Class 5 Science Chapter 3: The Mystery of Food
16 Interactive Simulators corresponding to Slides 1 to 16.
Zero raw LaTeX. Pure clean Unicode.
"""

SIMULATORS = {
    1: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Tiffin Box Inspection</span>
                <span id="sim1-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Lid Open: Spoiled</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Stainless Steel Box Base -->
                    <rect x="70" y="55" width="220" height="110" rx="20" fill="#334155" stroke="#64748b" stroke-width="4"/>
                    <rect x="78" y="63" width="204" height="94" rx="14" fill="#1e293b"/>

                    <!-- Uttapam Food Item -->
                    <ellipse id="sim1-food" cx="180" cy="110" rx="85" ry="38" fill="#d97706" stroke="#b45309" stroke-width="2"/>

                    <!-- Mold Patches Group (Visible in Spoiled state) -->
                    <g id="sim1-mold" opacity="1">
                        <circle cx="150" cy="100" r="14" fill="#065f46" opacity="0.85"/>
                        <circle cx="153" cy="98" r="9" fill="#10b981" opacity="0.9"/>
                        <circle cx="210" cy="115" r="16" fill="#1e3a5f" opacity="0.8"/>
                        <circle cx="208" cy="113" r="11" fill="#38bdf8" opacity="0.85"/>
                        <circle cx="180" cy="125" r="12" fill="#312e81" opacity="0.85"/>
                        <circle cx="180" cy="95" r="8" fill="#047857" opacity="0.8"/>
                        <circle cx="130" cy="115" r="10" fill="#111827" opacity="0.9"/>
                        <!-- Foul odor fumes -->
                        <path d="M 140 85 Q 135 65 145 50" stroke="#10b981" stroke-width="2" fill="none" stroke-dasharray="3,3" opacity="0.8"/>
                        <path d="M 180 80 Q 185 60 175 45" stroke="#10b981" stroke-width="2.5" fill="none" stroke-dasharray="3,3" opacity="0.9"/>
                        <path d="M 220 85 Q 215 65 225 50" stroke="#10b981" stroke-width="2" fill="none" stroke-dasharray="3,3" opacity="0.8"/>
                    </g>

                    <!-- Fresh Garnish Group (Hidden in Spoiled state) -->
                    <g id="sim1-fresh-garnish" opacity="0">
                        <circle cx="150" cy="105" r="4" fill="#ef4444"/>
                        <circle cx="170" cy="95" r="3" fill="#22c55e"/>
                        <circle cx="195" cy="115" r="4" fill="#ef4444"/>
                        <circle cx="210" cy="100" r="3" fill="#22c55e"/>
                        <!-- Steaming heat waves -->
                        <path d="M 160 80 Q 165 60 160 45" stroke="#f59e0b" stroke-width="2" fill="none" opacity="0.8"/>
                        <path d="M 190 80 Q 195 60 190 45" stroke="#f59e0b" stroke-width="2" fill="none" opacity="0.8"/>
                    </g>

                    <!-- Lid Object -->
                    <g id="sim1-lid" transform="translate(180, 25)">
                        <rect x="-115" y="-15" width="230" height="25" rx="10" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
                        <circle cx="0" cy="-3" r="6" fill="#cbd5e1"/>
                        <text x="0" y="3" text-anchor="middle" font-size="8" fill="#1e293b" font-weight="bold">LID OPEN</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setTiffinState('spoiled')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                    3 Days Later (Spoiled)
                </button>
                <button onclick="setTiffinState('fresh')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    Freshly Cooked
                </button>
            </div>
            <p id="sim1-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Foul sour odor escapes as the forgotten box opens. The uttapam is covered with fuzzy greenish mold colonies and black spore patches.
            </p>
        </div>
    """,

    2: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Microscope Magnification Lens</span>
                <span id="sim2-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Zoom: 100x (Mycelium)</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Circular Microscope Viewport -->
                    <circle cx="180" cy="95" r="85" fill="#042f2e" stroke="#0f766e" stroke-width="5"/>
                    <circle cx="180" cy="95" r="84" fill="none" stroke="#2dd4bf" stroke-width="1" opacity="0.3"/>

                    <!-- Level 1: 1x Naked Eye (Small fuzzy dot) -->
                    <g id="sim2-view-1x" opacity="0">
                        <rect x="100" y="30" width="160" height="130" fill="#d97706" opacity="0.3" rx="10"/>
                        <circle cx="180" cy="95" r="18" fill="#065f46" opacity="0.9"/>
                        <circle cx="178" cy="92" r="12" fill="#10b981" opacity="0.8"/>
                        <text x="180" y="145" text-anchor="middle" font-size="10" fill="#99f6e4" font-weight="bold">Fuzzy Mold Patch (1x)</text>
                    </g>

                    <!-- Level 2: 100x Microscope (Fungal Hyphae Network) -->
                    <g id="sim2-view-100x" opacity="1">
                        <!-- Branching hyphae threads -->
                        <path d="M 120 150 Q 150 110 180 90 T 240 60" stroke="#34d399" stroke-width="3" fill="none"/>
                        <path d="M 150 110 Q 180 130 210 140 T 250 130" stroke="#34d399" stroke-width="2.5" fill="none"/>
                        <path d="M 180 90 Q 190 70 200 50" stroke="#34d399" stroke-width="2.5" fill="none"/>
                        <path d="M 140 130 Q 160 80 170 50" stroke="#10b981" stroke-width="2" fill="none"/>
                        <path d="M 210 95 Q 230 110 245 100" stroke="#10b981" stroke-width="2" fill="none"/>
                        <!-- Growing spore knobs -->
                        <circle cx="200" cy="50" r="7" fill="#059669"/>
                        <circle cx="240" cy="60" r="6" fill="#059669"/>
                        <circle cx="170" cy="50" r="6" fill="#059669"/>
                        <circle cx="250" cy="130" r="7" fill="#059669"/>
                        <text x="180" y="170" text-anchor="middle" font-size="9" fill="#a7f3d0" font-weight="bold">Thread-like Hyphae (100x)</text>
                    </g>

                    <!-- Level 3: 1,000x High Power (Sporangium Head & Releasing Spores) -->
                    <g id="sim2-view-1000x" opacity="0">
                        <line x1="180" y1="180" x2="180" y2="105" stroke="#34d399" stroke-width="7"/>
                        <!-- Sporangium Spore Head -->
                        <circle cx="180" cy="90" r="30" fill="#065f46" stroke="#10b981" stroke-width="3"/>
                        <!-- Microscopic Spores floating -->
                        <circle cx="150" cy="60" r="4" fill="#6ee7b7"/>
                        <circle cx="160" cy="45" r="3.5" fill="#6ee7b7"/>
                        <circle cx="190" cy="40" r="4.5" fill="#6ee7b7"/>
                        <circle cx="215" cy="55" r="4" fill="#6ee7b7"/>
                        <circle cx="225" cy="75" r="3.5" fill="#6ee7b7"/>
                        <circle cx="140" cy="80" r="3" fill="#6ee7b7"/>
                        <circle cx="135" cy="110" r="4" fill="#6ee7b7"/>
                        <text x="180" y="145" text-anchor="middle" font-size="9" fill="#6ee7b7" font-weight="bold">Sporangium Bursting Spores (1,000x)</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-3 gap-1.5">
                <button onclick="setMicroscopeZoom('1x')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700">
                    1x Eye
                </button>
                <button onclick="setMicroscopeZoom('100x')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-teal-300 border border-slate-700">
                    100x Hyphae
                </button>
                <button onclick="setMicroscopeZoom('1000x')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-cyan-300 border border-slate-700">
                    1,000x Spores
                </button>
            </div>
            <p id="sim2-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                At 100x magnification, fuzzy mold resolves into an interconnected web of living fungal filaments called hyphae, absorbing food sugars.
            </p>
        </div>
    """,

    3: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Microbial Habitat Explorer</span>
                <span id="sim3-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Habitat: Human Gut</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Central Biosphere Earth Ring -->
                    <circle cx="180" cy="95" r="75" fill="#0f172a" stroke="#334155" stroke-width="2"/>

                    <!-- Habitat Nodes -->
                    <!-- Node 1: Air -->
                    <g onclick="selectHabitat('air')" class="cursor-pointer" transform="translate(180, 40)">
                        <circle id="sim3-node-air" cx="0" cy="0" r="18" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
                        <text x="0" y="4" text-anchor="middle" font-size="12">💨</text>
                        <text x="0" y="27" text-anchor="middle" font-size="8" fill="#94a3b8" font-weight="bold">Air</text>
                    </g>
                    <!-- Node 2: Soil -->
                    <g onclick="selectHabitat('soil')" class="cursor-pointer" transform="translate(110, 85)">
                        <circle id="sim3-node-soil" cx="0" cy="0" r="18" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                        <text x="0" y="4" text-anchor="middle" font-size="12">🌱</text>
                        <text x="0" y="27" text-anchor="middle" font-size="8" fill="#94a3b8" font-weight="bold">Soil</text>
                    </g>
                    <!-- Node 3: Water -->
                    <g onclick="selectHabitat('water')" class="cursor-pointer" transform="translate(250, 85)">
                        <circle id="sim3-node-water" cx="0" cy="0" r="18" fill="#1e293b" stroke="#06b6d4" stroke-width="2"/>
                        <text x="0" y="4" text-anchor="middle" font-size="12">💧</text>
                        <text x="0" y="27" text-anchor="middle" font-size="8" fill="#94a3b8" font-weight="bold">Water</text>
                    </g>
                    <!-- Node 4: Gut (Center) -->
                    <g onclick="selectHabitat('gut')" class="cursor-pointer" transform="translate(180, 110)">
                        <circle id="sim3-node-gut" cx="0" cy="0" r="22" fill="#312e81" stroke="#818cf8" stroke-width="3"/>
                        <text x="0" y="5" text-anchor="middle" font-size="14">🧬</text>
                        <text x="0" y="32" text-anchor="middle" font-size="8" fill="#c7d2fe" font-weight="bold">Gut (100 Trillion)</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-4 gap-1.5">
                <button onclick="selectHabitat('air')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-sky-300 border border-slate-700">
                    💨 Air
                </button>
                <button onclick="selectHabitat('soil')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-amber-300 border border-slate-700">
                    🌱 Soil
                </button>
                <button onclick="selectHabitat('water')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-cyan-300 border border-slate-700">
                    💧 Water
                </button>
                <button onclick="selectHabitat('gut')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-indigo-300 border border-slate-700">
                    🧬 Human Gut
                </button>
            </div>
            <p id="sim3-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Finding #1: More than 100 trillion beneficial bacteria live naturally inside your gut, digesting fibers and synthesizing Vitamin K!
            </p>
        </div>
    """,

    4: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Microbial Growth Triad Simulator</span>
                <span id="sim4-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Growth: Rapid Explosion</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Incubation Chamber Petri Dish -->
                    <circle cx="180" cy="95" r="78" fill="#1e1b4b" stroke="#4338ca" stroke-width="4"/>
                    <circle cx="180" cy="95" r="77" fill="#0f172a"/>

                    <!-- Microbe colony dots multiplying dynamically -->
                    <g id="sim4-colonies">
                        <circle cx="150" cy="80" r="8" fill="#ec4899" opacity="0.9"/>
                        <circle cx="170" cy="65" r="6" fill="#f43f5e" opacity="0.85"/>
                        <circle cx="210" cy="85" r="10" fill="#a855f7" opacity="0.9"/>
                        <circle cx="195" cy="115" r="9" fill="#06b6d4" opacity="0.9"/>
                        <circle cx="160" cy="120" r="7" fill="#10b981" opacity="0.85"/>
                        <circle cx="180" cy="95" r="12" fill="#e11d48" opacity="0.95"/>
                        <circle cx="140" cy="100" r="6" fill="#f59e0b" opacity="0.9"/>
                        <circle cx="215" cy="115" r="7" fill="#ec4899" opacity="0.85"/>
                    </g>

                    <!-- Status indicators on side -->
                    <rect x="20" y="25" width="80" height="22" rx="6" fill="#1e293b" stroke="#334155"/>
                    <text id="sim4-moist-text" x="60" y="39" text-anchor="middle" font-size="9" fill="#38bdf8" font-weight="bold">Moist: YES</text>

                    <rect x="20" y="55" width="80" height="22" rx="6" fill="#1e293b" stroke="#334155"/>
                    <text id="sim4-temp-text" x="60" y="69" text-anchor="middle" font-size="9" fill="#f59e0b" font-weight="bold">Warm: 30°C</text>

                    <rect x="20" y="85" width="80" height="22" rx="6" fill="#1e293b" stroke="#334155"/>
                    <text id="sim4-air-text" x="60" y="99" text-anchor="middle" font-size="9" fill="#a78bfa" font-weight="bold">Air: YES</text>
                </svg>
            </div>
            <div class="grid grid-cols-3 gap-1.5">
                <button onclick="toggleGrowthFactor('moisture')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-sky-300 border border-slate-700">
                    💧 Moisture
                </button>
                <button onclick="toggleGrowthFactor('temp')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-amber-300 border border-slate-700">
                    🌡️ Temperature
                </button>
                <button onclick="toggleGrowthFactor('air')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-indigo-300 border border-slate-700">
                    💨 Air (Oxygen)
                </button>
            </div>
            <p id="sim4-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Finding #2: All three essentials (Moisture + Warmth + Air) are present! Bacteria double every 20 minutes, rapidly spoiling the food.
            </p>
        </div>
    """,

    5: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Solar Dehydration Yard</span>
                <span id="sim5-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Day 1: 85% Moisture</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Sun with radiant rays -->
                    <circle cx="60" cy="45" r="22" fill="#f59e0b" opacity="0.9"/>
                    <circle cx="60" cy="45" r="28" fill="none" stroke="#fef08a" stroke-width="2" stroke-dasharray="4,4"/>

                    <!-- Woven Bamboo Drying Mat -->
                    <ellipse cx="200" cy="135" rx="130" ry="42" fill="#78350f" stroke="#b45309" stroke-width="2"/>
                    <line x1="100" y1="135" x2="300" y2="135" stroke="#92400e" stroke-dasharray="2,2"/>

                    <!-- Chillies on mat (morphs with drying day) -->
                    <g id="sim5-chillies">
                        <!-- Plump red chilli 1 -->
                        <path id="chilli-1" d="M 140 130 Q 165 120 185 132" stroke="#ef4444" stroke-width="12" stroke-linecap="round" fill="none"/>
                        <!-- Plump red chilli 2 -->
                        <path id="chilli-2" d="M 180 145 Q 210 135 235 142" stroke="#dc2626" stroke-width="11" stroke-linecap="round" fill="none"/>
                        <!-- Plump red chilli 3 -->
                        <path id="chilli-3" d="M 210 120 Q 235 110 255 125" stroke="#b91c1c" stroke-width="10" stroke-linecap="round" fill="none"/>
                    </g>

                    <!-- Steam / Water vapor rising -->
                    <g id="sim5-vapor" opacity="1">
                        <path d="M 160 115 Q 165 95 160 80" stroke="#38bdf8" stroke-width="2" fill="none" opacity="0.7"/>
                        <path d="M 200 125 Q 205 105 200 90" stroke="#38bdf8" stroke-width="2" fill="none" opacity="0.7"/>
                        <path d="M 235 105 Q 240 85 235 70" stroke="#38bdf8" stroke-width="2" fill="none" opacity="0.7"/>
                    </g>

                    <!-- Moisture Meter Gauge -->
                    <rect x="250" y="25" width="95" height="40" rx="8" fill="#1e293b" stroke="#334155"/>
                    <text x="297" y="42" text-anchor="middle" font-size="9" fill="#94a3b8">Moisture Level</text>
                    <text id="sim5-moist-pct" x="297" y="58" text-anchor="middle" font-size="12" fill="#38bdf8" font-weight="bold">85% (Juicy)</text>
                </svg>
            </div>
            <div class="grid grid-cols-3 gap-2">
                <button onclick="setDryingDay(1)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700">
                    Day 1 (Fresh)
                </button>
                <button onclick="setDryingDay(3)" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                    Day 3 (Wilting)
                </button>
                <button onclick="setDryingDay(5)" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    Day 5 (Crisp Dehydrated)
                </button>
            </div>
            <p id="sim5-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Finding #3: Under solar heat, internal cell water evaporates into air. At 8% moisture, the chillies are brittle and cannot support any mold growth!
            </p>
        </div>
    """,

    6: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Grandmother's Pickle Jar</span>
                <span id="sim6-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Oil Seal: 100% Sealed</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Glass Jar Outline -->
                    <path d="M 120 40 L 240 40 L 240 50 L 250 65 L 250 170 Q 250 180 240 180 L 120 180 Q 110 180 110 170 L 110 65 L 120 50 Z" fill="#0f172a" stroke="#cbd5e1" stroke-width="3" opacity="0.8"/>

                    <!-- Brine & Mango pieces at bottom -->
                    <rect x="113" y="100" width="134" height="77" fill="#b45309" opacity="0.6"/>
                    <!-- Raw Mango Chunks -->
                    <rect x="130" y="115" width="28" height="22" rx="4" fill="#65a30d" stroke="#365314"/>
                    <rect x="175" y="125" width="30" height="24" rx="4" fill="#84cc16" stroke="#365314"/>
                    <rect x="145" y="145" width="32" height="22" rx="4" fill="#65a30d" stroke="#365314"/>
                    <rect x="195" y="145" width="26" height="20" rx="4" fill="#4d7c0f" stroke="#365314"/>

                    <!-- Mustard Oil Layer (Floating on top) -->
                    <rect id="sim6-oil-layer" x="113" y="75" width="134" height="25" fill="#eab308" opacity="0.85"/>
                    <text id="sim6-oil-label" x="180" y="91" text-anchor="middle" font-size="9" fill="#713f12" font-weight="bold">Mustard Oil Barrier</text>

                    <!-- Mold Growth (Visible only if oil barrier is removed) -->
                    <g id="sim6-mold" opacity="0">
                        <circle cx="150" cy="110" r="10" fill="#047857"/>
                        <circle cx="185" cy="115" r="12" fill="#065f46"/>
                        <circle cx="215" cy="120" r="9" fill="#047857"/>
                        <text x="180" y="65" text-anchor="middle" font-size="9" fill="#ef4444" font-weight="bold">Oxygen Infiltrating!</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setPickleOil(true)" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    Oil Layer Intact (Preserved)
                </button>
                <button onclick="setPickleOil(false)" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                    Remove Oil (Air Enters)
                </button>
            </div>
            <p id="sim6-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Finding #4: Thick mustard oil floats on top, completely cutting off atmospheric oxygen so molds cannot respire or germinate!
            </p>
        </div>
    """,

    7: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Temperature Danger Zone Meter</span>
                <span id="sim7-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Refrigerator: 4°C</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Thermal Gauge Scale Bar -->
                    <rect x="40" y="80" width="280" height="25" rx="12" fill="#1e293b"/>
                    <!-- Color Zones: Blue (Freeze/Chilled), Red (Danger), Orange (Boiling) -->
                    <rect x="40" y="80" width="60" height="25" rx="6" fill="#0284c7" opacity="0.8"/>
                    <rect x="100" y="80" width="130" height="25" fill="#dc2626" opacity="0.8"/>
                    <rect x="230" y="80" width="90" height="25" rx="6" fill="#ea580c" opacity="0.8"/>

                    <!-- Labels on Gauge -->
                    <text x="60" y="70" text-anchor="middle" font-size="9" fill="#38bdf8" font-weight="bold">Cold (4°C)</text>
                    <text x="165" y="70" text-anchor="middle" font-size="9" fill="#f87171" font-weight="bold">Danger Zone (20-45°C)</text>
                    <text x="275" y="70" text-anchor="middle" font-size="9" fill="#fb923c" font-weight="bold">Boiling (100°C)</text>

                    <!-- Gauge Indicator Arrow -->
                    <polygon id="sim7-pointer" points="60,110 50,130 70,130" fill="#38bdf8"/>

                    <!-- Dynamic Microbial Behavior Display -->
                    <rect x="60" y="140" width="240" height="35" rx="8" fill="#0f172a" stroke="#334155"/>
                    <text id="sim7-status-text" x="180" y="162" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="bold">
                        Bacterial Growth: Sluggish / Sleeping
                    </text>
                </svg>
            </div>
            <div class="grid grid-cols-3 gap-1.5">
                <button onclick="setTempZone('fridge')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-sky-300 border border-slate-700">
                    ❄️ Fridge (4°C)
                </button>
                <button onclick="setTempZone('room')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-rose-300 border border-slate-700">
                    🌡️ Room (30°C)
                </button>
                <button onclick="setTempZone('boil')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-amber-300 border border-slate-700">
                    🔥 Boil (100°C)
                </button>
            </div>
            <p id="sim7-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Finding #5: In the refrigerator at 4°C, enzymes slow down dramatically. Bacteria cannot multiply fast enough to spoil milk for several days.
            </p>
        </div>
    """,

    8: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Pantry Preservation Vault</span>
                <span id="sim8-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Method: Sugar Murabba</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Glass Jar Vault Display -->
                    <rect x="90" y="30" width="180" height="135" rx="16" fill="#1e293b" stroke="#475569" stroke-width="3"/>

                    <!-- Graphic Object inside Jar (changes with method) -->
                    <g id="sim8-content">
                        <!-- Default: Sugar Murabba Amla -->
                        <circle cx="150" cy="95" r="22" fill="#ca8a04" stroke="#a16207" stroke-width="2"/>
                        <circle cx="210" cy="95" r="22" fill="#ca8a04" stroke="#a16207" stroke-width="2"/>
                        <circle cx="180" cy="125" r="20" fill="#ca8a04" stroke="#a16207" stroke-width="2"/>
                        <!-- Thick Golden Sugar Syrup -->
                        <rect x="95" y="70" width="170" height="90" rx="10" fill="#facc15" opacity="0.35"/>
                        <text x="180" y="60" text-anchor="middle" font-size="10" fill="#fde047" font-weight="bold">Thick Sugar Syrup (Osmosis)</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-4 gap-1.5">
                <button onclick="selectPreserveVault('sugar')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-amber-300 border border-slate-700">
                    🍯 Sugar
                </button>
                <button onclick="selectPreserveVault('salt')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-cyan-300 border border-slate-700">
                    🧂 Salt Brine
                </button>
                <button onclick="selectPreserveVault('spices')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-emerald-300 border border-slate-700">
                    🌿 Spices
                </button>
                <button onclick="selectPreserveVault('vacuum')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-indigo-300 border border-slate-700">
                    📦 Vacuum
                </button>
            </div>
            <p id="sim8-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Finding #6: High sugar syrup locks water tightly through osmotic pressure, starving bacteria of moisture and preserving amla murabba for months.
            </p>
        </div>
    """,

    9: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Idli Batter Fermentation Lab</span>
                <span id="sim9-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Status: Fermented & Fluffy</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Ceramic Bowl Container -->
                    <path d="M 100 80 Q 90 170 180 170 Q 270 170 260 80 Z" fill="#334155" stroke="#64748b" stroke-width="4"/>

                    <!-- Batter Level (Rises dynamically) -->
                    <path id="sim9-batter" d="M 106 90 Q 180 70 254 90 Q 260 160 180 160 Q 100 160 106 90 Z" fill="#f8fafc"/>

                    <!-- Carbon Dioxide Gas Bubbles -->
                    <g id="sim9-bubbles" opacity="1">
                        <circle cx="140" cy="110" r="5" fill="#cbd5e1"/>
                        <circle cx="160" cy="95" r="7" fill="#cbd5e1"/>
                        <circle cx="190" cy="100" r="6" fill="#cbd5e1"/>
                        <circle cx="215" cy="115" r="5" fill="#cbd5e1"/>
                        <circle cx="175" cy="125" r="8" fill="#cbd5e1"/>
                        <circle cx="130" cy="130" r="6" fill="#cbd5e1"/>
                        <circle cx="220" cy="135" r="5" fill="#cbd5e1"/>
                        <text x="180" y="55" text-anchor="middle" font-size="10" fill="#38bdf8" font-weight="bold">Carbon Dioxide (CO₂) Bubbles</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setBatterState('unfermented')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700">
                    Evening (Freshly Ground)
                </button>
                <button onclick="setBatterState('fermented')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                    Morning (Overnight Rise)
                </button>
            </div>
            <p id="sim9-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Finding #7: Beneficial airborne yeasts and lactic acid bacteria ferment batter starches, releasing CO2 gas bubbles that expand it into light, fluffy idlis!
            </p>
        </div>
    """,

    10: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Digestive Gut Microbiome</span>
                <span id="sim10-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Probiotic Curd Relief</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Stomach / Intestine Outline -->
                    <path d="M 120 40 Q 180 20 230 50 Q 260 90 230 140 Q 190 170 140 160 Q 90 140 100 90 Z" fill="#1e1b4b" stroke="#6366f1" stroke-width="3" opacity="0.7"/>

                    <!-- Bad Microbes Group (Active in Upset Stomach state) -->
                    <g id="sim10-bad-microbes" opacity="0">
                        <circle cx="140" cy="80" r="8" fill="#ef4444"/>
                        <circle cx="170" cy="70" r="9" fill="#dc2626"/>
                        <circle cx="200" cy="90" r="8" fill="#b91c1c"/>
                        <circle cx="160" cy="115" r="9" fill="#ef4444"/>
                        <circle cx="190" cy="130" r="8" fill="#dc2626"/>
                        <text x="180" y="30" text-anchor="middle" font-size="10" fill="#f87171" font-weight="bold">Harmful Pathogens (Fair Food)</text>
                    </g>

                    <!-- Good Lactobacillus Microbes Group (Active in Healed state) -->
                    <g id="sim10-good-microbes" opacity="1">
                        <ellipse cx="140" cy="85" rx="10" ry="5" fill="#10b981"/>
                        <ellipse cx="170" cy="75" rx="11" ry="5" fill="#34d399"/>
                        <ellipse cx="205" cy="95" rx="10" ry="5" fill="#10b981"/>
                        <ellipse cx="160" cy="110" rx="12" ry="6" fill="#34d399"/>
                        <ellipse cx="190" cy="125" rx="10" ry="5" fill="#10b981"/>
                        <ellipse cx="140" cy="130" rx="10" ry="5" fill="#34d399"/>
                        <text x="180" y="30" text-anchor="middle" font-size="10" fill="#6ee7b7" font-weight="bold">Lactobacillus Probiotics (Curd & Chaas)</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setGutState('upset')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                    Fair Food (Indigestion)
                </button>
                <button onclick="setGutState('curd')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    Buttermilk & Curd (Healed)
                </button>
            </div>
            <p id="sim10-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Finding #8: Fresh buttermilk supplies billions of helpful Lactobacillus bacteria that outcompete harmful germs and soothe digestive inflammation.
            </p>
        </div>
    """,

    11: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Vegetable Quality Inspector</span>
                <span id="sim11-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Tomato: Fresh & Firm</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Market Wooden Crate Base -->
                    <rect x="80" y="40" width="200" height="120" rx="12" fill="#78350f" stroke="#b45309" stroke-width="3"/>
                    <rect x="90" y="50" width="180" height="100" rx="8" fill="#1e293b"/>

                    <!-- Produce Graphic (Tomato default) -->
                    <g id="sim11-produce">
                        <circle cx="180" cy="100" r="35" fill="#ef4444" stroke="#b91c1c" stroke-width="3"/>
                        <!-- Green calyx stem -->
                        <polygon points="180,65 170,55 175,68 185,68 190,55" fill="#22c55e"/>
                        <!-- Highlight for freshness -->
                        <ellipse id="sim11-gloss" cx="165" cy="88" rx="8" ry="4" fill="#fecaca" opacity="0.8"/>
                        <!-- Defect spot (hidden in fresh) -->
                        <circle id="sim11-defect" cx="195" cy="110" r="9" fill="#047857" opacity="0"/>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setProduceQuality('fresh')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    Fresh & Firm (Select)
                </button>
                <button onclick="setProduceQuality('spoiled')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                    Bruised & Moldy (Reject)
                </button>
            </div>
            <p id="sim11-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Grandfather Thatha's rule: Look for taut, glossy skin and firm texture. Avoid bruises or punctures that let spoilage microbes inside!
            </p>
        </div>
    """,

    12: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Seasonal Harvest Calendar</span>
                <span id="sim12-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Summer: Mangoes & Lychees</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Seasonal Dial -->
                    <circle cx="180" cy="95" r="75" fill="#0f172a" stroke="#334155" stroke-width="3"/>

                    <!-- Season Quadrants -->
                    <!-- Summer (Top-Right) -->
                    <path d="M 180 95 L 180 20 A 75 75 0 0 1 255 95 Z" fill="#f59e0b" opacity="0.4"/>
                    <!-- Monsoon (Bottom-Right) -->
                    <path d="M 180 95 L 255 95 A 75 75 0 0 1 180 170 Z" fill="#06b6d4" opacity="0.2"/>
                    <!-- Winter (Bottom-Left) -->
                    <path d="M 180 95 L 180 170 A 75 75 0 0 1 105 95 Z" fill="#38bdf8" opacity="0.2"/>
                    <!-- Spring (Top-Left) -->
                    <path d="M 180 95 L 105 95 A 75 75 0 0 1 180 20 Z" fill="#10b981" opacity="0.2"/>

                    <!-- Center Fruit Icon & Label -->
                    <circle cx="180" cy="95" r="38" fill="#1e293b" stroke="#cbd5e1" stroke-width="2"/>
                    <text id="sim12-fruit-emoji" x="180" y="100" text-anchor="middle" font-size="24">🥭</text>
                    <text id="sim12-fruit-text" x="180" y="122" text-anchor="middle" font-size="8" fill="#fde047" font-weight="bold">Mango & Lychee</text>
                </svg>
            </div>
            <div class="grid grid-cols-3 gap-1.5">
                <button onclick="setSeasonCalendar('summer')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-amber-300 border border-slate-700">
                    ☀️ Summer (Mango)
                </button>
                <button onclick="setSeasonCalendar('winter')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-sky-300 border border-slate-700">
                    ❄️ Winter (Guava/Carrot)
                </button>
                <button onclick="setSeasonCalendar('monsoon')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-cyan-300 border border-slate-700">
                    🌧️ Monsoon (Jamun)
                </button>
            </div>
            <p id="sim12-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Finding #9: Seasonal fruits ripened under natural sunshine possess peak antioxidants and sweetness without long refrigerated transport!
            </p>
        </div>
    """,

    13: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Human Dental Arch (32 Teeth)</span>
                <span id="sim13-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Incisors: Cutting & Biting</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Horseshoe Dental Arch Jaw -->
                    <path d="M 80 150 Q 70 50 180 50 Q 290 50 280 150" fill="none" stroke="#e2e8f0" stroke-width="16" stroke-linecap="round"/>

                    <!-- Incisors (Front 4 teeth on arch) -->
                    <g id="sim13-incisors" onclick="selectTeethGroup('incisors')" class="cursor-pointer">
                        <circle cx="165" cy="52" r="7" fill="#38bdf8"/>
                        <circle cx="175" cy="50" r="7" fill="#38bdf8"/>
                        <circle cx="185" cy="50" r="7" fill="#38bdf8"/>
                        <circle cx="195" cy="52" r="7" fill="#38bdf8"/>
                    </g>
                    <!-- Canines (2 flanking teeth) -->
                    <g id="sim13-canines" onclick="selectTeethGroup('canines')" class="cursor-pointer">
                        <circle cx="145" cy="58" r="8" fill="#f59e0b"/>
                        <circle cx="215" cy="58" r="8" fill="#f59e0b"/>
                    </g>
                    <!-- Premolars (4 teeth behind canines) -->
                    <g id="sim13-premolars" onclick="selectTeethGroup('premolars')" class="cursor-pointer">
                        <circle cx="125" cy="72" r="8" fill="#10b981"/>
                        <circle cx="110" cy="90" r="8" fill="#10b981"/>
                        <circle cx="235" cy="72" r="8" fill="#10b981"/>
                        <circle cx="250" cy="90" r="8" fill="#10b981"/>
                    </g>
                    <!-- Molars (6 back grinding teeth) -->
                    <g id="sim13-molars" onclick="selectTeethGroup('molars')" class="cursor-pointer">
                        <circle cx="98" cy="110" r="9" fill="#818cf8"/>
                        <circle cx="90" cy="130" r="10" fill="#818cf8"/>
                        <circle cx="85" cy="150" r="10" fill="#818cf8"/>
                        <circle cx="262" cy="110" r="9" fill="#818cf8"/>
                        <circle cx="270" cy="130" r="10" fill="#818cf8"/>
                        <circle cx="275" cy="150" r="10" fill="#818cf8"/>
                    </g>

                    <!-- Center Information Tool Icon -->
                    <text id="sim13-tool-icon" x="180" y="115" text-anchor="middle" font-size="20">✂️</text>
                    <text id="sim13-tool-desc" x="180" y="135" text-anchor="middle" font-size="10" fill="#38bdf8" font-weight="bold">Chisel Action: Cutting</text>
                </svg>
            </div>
            <div class="grid grid-cols-4 gap-1.5">
                <button onclick="selectTeethGroup('incisors')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-sky-300 border border-slate-700">
                    Incisors (8)
                </button>
                <button onclick="selectTeethGroup('canines')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-amber-300 border border-slate-700">
                    Canines (4)
                </button>
                <button onclick="selectTeethGroup('premolars')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-emerald-300 border border-slate-700">
                    Premolars (8)
                </button>
                <button onclick="selectTeethGroup('molars')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-indigo-300 border border-slate-700">
                    Molars (12)
                </button>
            </div>
            <p id="sim13-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Finding #11: Incisors act like sharp kitchen knives to bite off crisp apple chunks with chisel-like efficiency!
            </p>
        </div>
    """,

    14: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Salivary Amylase Starch Digestion</span>
                <span id="sim14-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Chewing: 30 Seconds</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Oral Cavity Profile -->
                    <rect x="70" y="35" width="220" height="120" rx="18" fill="#1e293b" stroke="#475569" stroke-width="2"/>

                    <!-- Starch Chain vs Sweet Sugars -->
                    <g id="sim14-starch-group">
                        <!-- Macromolecule Chain (breaks into sugar) -->
                        <circle cx="120" cy="85" r="12" fill="#94a3b8"/>
                        <circle cx="145" cy="85" r="12" fill="#94a3b8"/>
                        <circle cx="170" cy="85" r="12" fill="#94a3b8"/>
                        <circle cx="195" cy="85" r="12" fill="#94a3b8"/>
                        <circle cx="220" cy="85" r="12" fill="#94a3b8"/>
                        <circle cx="245" cy="85" r="12" fill="#94a3b8"/>
                        <text x="180" y="60" text-anchor="middle" font-size="10" fill="#cbd5e1" font-weight="bold">Complex Starch (Tasteless)</text>
                    </g>

                    <!-- Saliva Droplets Showering Down -->
                    <g id="sim14-saliva" opacity="1">
                        <path d="M 130 50 Q 130 65 130 70" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
                        <path d="M 180 50 Q 180 65 180 70" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
                        <path d="M 230 50 Q 230 65 230 70" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
                    </g>

                    <!-- Taste Output Banner -->
                    <rect x="100" y="115" width="160" height="28" rx="8" fill="#0f172a" stroke="#0284c7"/>
                    <text id="sim14-taste-banner" x="180" y="133" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="bold">
                        Enzyme Action: Breaking Starch
                    </text>
                </svg>
            </div>
            <div class="grid grid-cols-3 gap-1.5">
                <button onclick="setChewTimer(0)" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-slate-300 border border-slate-700">
                    0s (Solid Roti)
                </button>
                <button onclick="setChewTimer(30)" class="p-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-[10px] font-bold text-white shadow transition">
                    30s (Enzyme Mixing)
                </button>
                <button onclick="setChewTimer(60)" class="p-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-[10px] font-bold text-white shadow transition">
                    60s (Sweet Maltose!)
                </button>
            </div>
            <p id="sim14-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Finding #10: Salivary amylase breaks tasteless starch into simple maltose sugars, while saliva shapes food into a slippery, swallowable bolus!
            </p>
        </div>
    """,

    15: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Dental Cavity Defense Station</span>
                <span id="sim15-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Healthy Enamel Shield</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Tooth Cross Section -->
                    <!-- Outer White Enamel Crown -->
                    <path id="sim15-enamel" d="M 130 110 Q 120 40 180 40 Q 240 40 230 110 L 220 160 L 140 160 Z" fill="#f8fafc" stroke="#cbd5e1" stroke-width="3"/>
                    <!-- Inner Yellow Dentin -->
                    <path d="M 145 110 Q 140 60 180 60 Q 220 60 215 110 L 205 150 L 155 150 Z" fill="#fde047" opacity="0.8"/>
                    <!-- Central Pink Pulp & Nerves -->
                    <path d="M 165 110 Q 160 80 180 80 Q 200 80 195 110 L 190 145 L 170 145 Z" fill="#f43f5e"/>

                    <!-- Cavity Hole & Acid Attack (Dynamic) -->
                    <g id="sim15-cavity" opacity="0">
                        <circle cx="180" cy="45" r="12" fill="#1e293b"/>
                        <circle cx="180" cy="45" r="8" fill="#450a0a"/>
                        <text x="180" y="25" text-anchor="middle" font-size="9" fill="#ef4444" font-weight="bold">Acid Cavity Hole!</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setDentalAction('brush')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    Brush Twice & Rinse (Protected)
                </button>
                <button onclick="setDentalAction('sugar')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                    Sticky Sweets No Rinse (Acid Attack)
                </button>
            </div>
            <p id="sim15-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Finding #12: Brushing twice daily flushes away bacterial plaque before microbes can ferment sugars into enamel-dissolving acid!
            </p>
        </div>
    """,

    16: """
        <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400 font-semibold">Throat Crossroads & Epiglottis Valve</span>
                <span id="sim16-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Safe Swallowing: Windpipe Sealed</span>
            </div>
            <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 360 190" class="w-full h-full">
                    <!-- Throat Conduit Branching -->
                    <!-- Upper Pharynx -->
                    <rect x="160" y="25" width="40" height="50" fill="#1e293b" stroke="#475569" stroke-width="2"/>
                    <!-- Trachea (Windpipe to Lungs - Front) -->
                    <rect x="130" y="95" width="35" height="80" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
                    <text x="147" y="145" text-anchor="middle" font-size="8" fill="#38bdf8" font-weight="bold">Windpipe</text>

                    <!-- Esophagus (Food pipe to Stomach - Back) -->
                    <rect x="195" y="95" width="35" height="80" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
                    <text x="212" y="145" text-anchor="middle" font-size="8" fill="#10b981" font-weight="bold">Food Pipe</text>

                    <!-- Epiglottis Flap Valve (Tilts dynamically) -->
                    <!-- In Safe Swallowing: folds down over windpipe at left -->
                    <line id="sim16-epiglottis" x1="165" y1="75" x2="135" y2="95" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>

                    <!-- Food Bolus -->
                    <circle id="sim16-bolus" cx="212" cy="110" r="8" fill="#d97706"/>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="setThroatAction('swallow')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                    Calm Swallowing (Epiglottis Closes)
                </button>
                <button onclick="setThroatAction('talk')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                    Talking While Eating (Choking Risk!)
                </button>
            </div>
            <p id="sim16-desc" class="text-[11px] text-slate-300 bg-slate-900 p-2.5 rounded-xl border border-slate-800 leading-relaxed">
                Finding #13: When you swallow calmly, the muscular epiglottis folds down to seal the windpipe, guiding food smoothly into the esophagus!
            </p>
        </div>
    """
}

