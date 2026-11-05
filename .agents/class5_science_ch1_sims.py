"""
Class 5 Science Chapter 1: Water - The Essence of Life
16 Bespoke Interactive SVG/HTML Simulators
Zero raw LaTeX. Pure clean Unicode.
"""

SIMULATORS = {
    1: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Rain Window & Global Water Distribution</span>
            <span id="sim1-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30">Display: Earth's Water Slices</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040817" />
                
                <!-- Window Frame & Rain Streak Simulation -->
                <rect x="20" y="15" width="130" height="170" rx="4" fill="#0f172a" stroke="#334155" stroke-width="2" />
                <rect x="25" y="20" width="58" height="78" fill="#1e293b" opacity="0.6" />
                <rect x="87" y="20" width="58" height="78" fill="#1e293b" opacity="0.6" />
                <rect x="25" y="102" width="58" height="78" fill="#1e293b" opacity="0.6" />
                <rect x="87" y="102" width="58" height="78" fill="#1e293b" opacity="0.6" />
                
                <!-- Animated Raindrops on Glass -->
                <g id="sim1-raindrops">
                    <line x1="45" y1="25" x2="43" y2="45" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" opacity="0.8" />
                    <circle cx="43" cy="45" r="2.5" fill="#38bdf8" />
                    <line x1="110" y1="35" x2="108" y2="60" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round" opacity="0.9" />
                    <circle cx="108" cy="60" r="3" fill="#38bdf8" />
                    <line x1="60" y1="115" x2="58" y2="140" stroke="#38bdf8" stroke-width="1.8" stroke-linecap="round" opacity="0.75" />
                    <circle cx="58" cy="140" r="2.2" fill="#38bdf8" />
                    <line x1="120" y1="125" x2="118" y2="155" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" opacity="0.85" />
                    <circle cx="118" cy="155" r="2.8" fill="#38bdf8" />
                </g>
                <text x="85" y="194" fill="#94a3b8" font-size="8" font-weight="bold" text-anchor="middle">Raindrops on Glass</text>

                <!-- Global Water Distribution Pie / Bar (Right Column) -->
                <g transform="translate(170, 20)">
                    <rect x="0" y="0" width="135" height="160" rx="8" fill="#090d1a" stroke="#1e293b" />
                    <text x="67" y="18" fill="#f8fafc" font-size="9" font-weight="bold" text-anchor="middle">Earth's Water Reservoirs</text>
                    
                    <!-- Saline Ocean Bar (97%) -->
                    <rect id="sim1-ocean-bar" x="15" y="30" width="105" height="42" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1" />
                    <text x="67" y="47" fill="#ffffff" font-size="8.5" font-weight="bold" text-anchor="middle">Oceans & Seas</text>
                    <text x="67" y="60" fill="#bae6fd" font-size="7.5" text-anchor="middle">~97% Saline (Undrinkable)</text>

                    <!-- Freshwater Total (3%) -->
                    <rect id="sim1-fresh-bar" x="15" y="80" width="105" height="32" rx="4" fill="#10b981" stroke="#34d399" stroke-width="1" />
                    <text x="67" y="94" fill="#ffffff" font-size="8.5" font-weight="bold" text-anchor="middle">Freshwater (~3%)</text>
                    <text x="67" y="104" fill="#a7f3d0" font-size="7" text-anchor="middle">2% Glaciers | <1% Accessible</text>

                    <!-- Accessible Drinkable Sliver (<1%) -->
                    <rect id="sim1-drink-bar" x="15" y="120" width="105" height="28" rx="4" fill="#f59e0b" stroke="#fbbf24" stroke-width="1" />
                    <text x="67" y="133" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Usable Freshwater</text>
                    <text x="67" y="143" fill="#fef3c7" font-size="7" text-anchor="middle">< 1% in Rivers, Lakes & Wells</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="inspectWaterFraction('ocean')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-sky-300 border border-slate-700">
                🌊 Ocean (97%)
            </button>
            <button onclick="inspectWaterFraction('glacier')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-emerald-300 border border-slate-700">
                🏔️ Frozen (2%)
            </button>
            <button onclick="inspectWaterFraction('usable')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-amber-300 border border-slate-700">
                💧 Usable (<1%)
            </button>
        </div>
        <div id="sim1-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Although water covers 71% of Earth's surface, 97% is salty seawater and 2% is locked in glaciers. Less than 1% is accessible freshwater that sustains all life.
        </div>
    </div>
    """,

    2: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Three States of Water Chamber</span>
            <span id="sim2-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">State: Liquid Water (25°C)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- Beaker / Chamber Glass Vessel -->
                <path d="M 110,30 L 110,165 Q 110,175 120,175 L 200,175 Q 210,175 210,165 L 210,30" fill="none" stroke="#64748b" stroke-width="3" />
                <line x1="100" y1="30" x2="115" y2="30" stroke="#64748b" stroke-width="3" />
                <line x1="205" y1="30" x2="220" y2="30" stroke="#64748b" stroke-width="3" />

                <!-- Substance Graphic Inside Chamber -->
                <!-- Solid Ice State -->
                <g id="sim2-ice" style="display: none;" transform="translate(130, 95)">
                    <polygon points="0,20 20,0 50,0 30,20" fill="#67e8f9" opacity="0.8" stroke="#a5f3fc" />
                    <polygon points="30,20 50,0 50,40 30,60" fill="#06b6d4" opacity="0.9" stroke="#a5f3fc" />
                    <polygon points="0,20 30,20 30,60 0,60" fill="#22d3ee" opacity="0.85" stroke="#a5f3fc" />
                    <text x="30" y="75" fill="#a5f3fc" font-size="8" font-weight="bold" text-anchor="middle">Rigid Ice Crystals</text>
                </g>

                <!-- Liquid Water State -->
                <g id="sim2-liquid" style="display: block;">
                    <rect x="112" y="95" width="96" height="78" rx="4" fill="#0284c7" fill-opacity="0.6" stroke="#38bdf8" />
                    <!-- Water surface ripples -->
                    <path d="M 112,95 Q 136,90 160,95 T 208,95" fill="none" stroke="#bae6fd" stroke-width="2" />
                    <circle cx="130" cy="120" r="3" fill="#bae6fd" opacity="0.6" />
                    <circle cx="175" cy="140" r="4" fill="#bae6fd" opacity="0.6" />
                    <circle cx="150" cy="155" r="2.5" fill="#bae6fd" opacity="0.6" />
                    <text x="160" y="135" fill="#ffffff" font-size="8.5" font-weight="bold" text-anchor="middle">Flowing Liquid</text>
                </g>

                <!-- Gaseous Steam State -->
                <g id="sim2-steam" style="display: none;">
                    <path d="M 140,80 Q 130,55 145,35 T 135,15" fill="none" stroke="#cbd5e1" stroke-width="2.5" stroke-dasharray="3,3" opacity="0.8" />
                    <path d="M 160,75 Q 175,50 160,30 T 170,10" fill="none" stroke="#cbd5e1" stroke-width="3" stroke-dasharray="3,3" opacity="0.85" />
                    <path d="M 180,85 Q 190,60 175,40 T 185,15" fill="none" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="3,3" opacity="0.75" />
                    <circle cx="145" cy="110" r="3" fill="#cbd5e1" />
                    <circle cx="175" cy="105" r="3" fill="#cbd5e1" />
                    <circle cx="160" cy="130" r="3" fill="#cbd5e1" />
                    <text x="160" y="150" fill="#94a3b8" font-size="8.5" font-weight="bold" text-anchor="middle">Fast Moving Vapour</text>
                </g>

                <!-- Thermometer on the side -->
                <rect x="40" y="30" width="10" height="130" rx="5" fill="#1e293b" stroke="#475569" />
                <rect id="sim2-thermo-mercury" x="42" y="100" width="6" height="60" rx="3" fill="#ef4444" />
                <circle cx="45" cy="165" r="8" fill="#ef4444" />
                <text id="sim2-temp-label" x="45" y="22" fill="#f87171" font-size="9" font-weight="bold" text-anchor="middle">25°C</text>

                <!-- Burner Flame at base -->
                <g id="sim2-flame" transform="translate(160, 185)" opacity="0">
                    <polygon points="-15,10 0,-10 15,10 0,5" fill="#f59e0b" />
                    <polygon points="-8,10 0,-3 8,10 0,6" fill="#fef08a" />
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="setWaterState('solid')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-cyan-300 border border-slate-700">
                🧊 Solid Ice (-10°C)
            </button>
            <button onclick="setWaterState('liquid')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-blue-300 border border-slate-700">
                💧 Liquid (25°C)
            </button>
            <button onclick="setWaterState('gas')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-amber-300 border border-slate-700">
                💨 Steam (100°C)
            </button>
        </div>
        <div id="sim2-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Water naturally exists as solid ice below 0°C, liquid water between 0°C and 100°C, and gaseous steam/vapour at 100°C and above.
        </div>
    </div>
    """,

    3: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">State Transition & Latent Heat Lab</span>
            <span id="sim3-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Action: Melting Ice</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040714" />

                <!-- 4 State Shifter Nodes -->
                <!-- Solid Node (Left) -->
                <g transform="translate(45, 100)">
                    <circle cx="0" cy="0" r="24" fill="#0f172a" stroke="#06b6d4" stroke-width="2" />
                    <text x="0" y="-4" fill="#67e8f9" font-size="14" text-anchor="middle">🧊</text>
                    <text x="0" y="12" fill="#a5f3fc" font-size="7.5" font-weight="bold" text-anchor="middle">Solid Ice</text>
                </g>

                <!-- Liquid Node (Center) -->
                <g transform="translate(160, 100)">
                    <circle cx="0" cy="0" r="26" fill="#0f172a" stroke="#0284c7" stroke-width="2.5" />
                    <text x="0" y="-4" fill="#38bdf8" font-size="14" text-anchor="middle">💧</text>
                    <text x="0" y="12" fill="#93c5fd" font-size="8" font-weight="bold" text-anchor="middle">Liquid Water</text>
                </g>

                <!-- Gas Node (Right) -->
                <g transform="translate(275, 100)">
                    <circle cx="0" cy="0" r="24" fill="#0f172a" stroke="#818cf8" stroke-width="2" />
                    <text x="0" y="-4" fill="#c084fc" font-size="14" text-anchor="middle">💨</text>
                    <text x="0" y="12" fill="#e0e7ff" font-size="7.5" font-weight="bold" text-anchor="middle">Vapour/Steam</text>
                </g>

                <!-- Arrows -->
                <!-- Melting Arrow (Top Left) -->
                <path id="sim3-arrow-melt" d="M 72,85 Q 115,60 133,85" fill="none" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)" />
                <text x="105" y="65" fill="#fbbf24" font-size="7.5" font-weight="bold" text-anchor="middle">+ Heat (Melting)</text>

                <!-- Freezing Arrow (Bottom Left) -->
                <path id="sim3-arrow-freeze" d="M 133,115 Q 115,140 72,115" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,2" />
                <text x="105" y="145" fill="#7dd3fc" font-size="7" text-anchor="middle">− Cool (Freezing)</text>

                <!-- Evaporation Arrow (Top Right) -->
                <path id="sim3-arrow-evap" d="M 188,85 Q 230,60 250,85" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2,2" />
                <text x="218" y="65" fill="#f87171" font-size="7.5" font-weight="bold" text-anchor="middle">+ Heat (Evaporation)</text>

                <!-- Condensation Arrow (Bottom Right) -->
                <path id="sim3-arrow-cond" d="M 250,115 Q 230,140 188,115" fill="none" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="2,2" />
                <text x="218" y="145" fill="#86efac" font-size="7" text-anchor="middle">− Cool (Condensation)</text>

                <!-- Explanation Banner -->
                <rect x="25" y="165" width="270" height="26" rx="5" fill="#0f172a" stroke="#334155" />
                <text id="sim3-info-text" x="160" y="181" fill="#fde047" font-size="8.5" font-weight="bold" text-anchor="middle">Ice absorbs thermal energy at 0°C to melt into liquid water.</text>
            </svg>
        </div>
        <div class="grid grid-cols-4 gap-1.5">
            <button onclick="triggerTransition('melt')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-amber-300 border border-slate-700">
                ☀️ Melting
            </button>
            <button onclick="triggerTransition('evap')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-rose-300 border border-slate-700">
                ♨️ Evaporate
            </button>
            <button onclick="triggerTransition('cond')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-emerald-300 border border-slate-700">
                💧 Condense
            </button>
            <button onclick="triggerTransition('freeze')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-cyan-300 border border-slate-700">
                ❄️ Freezing
            </button>
        </div>
        <div id="sim3-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Adding heat turns solid ice into liquid water (melting) and liquid into gas (evaporation). Removing heat condenses gas back into liquid and freezes liquid into ice.
        </div>
    </div>
    """,

    4: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Steel Tumbler Condensation Experiment</span>
            <span id="sim4-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Contents: Ice Water (4°C)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#020617" />

                <!-- Ambient Room Air with Gaseous Vapour Molecules -->
                <g id="sim4-air-molecules" opacity="0.6">
                    <circle cx="40" cy="50" r="2.5" fill="#38bdf8" />
                    <circle cx="80" cy="30" r="2" fill="#38bdf8" />
                    <circle cx="50" cy="110" r="2.2" fill="#38bdf8" />
                    <circle cx="70" cy="150" r="2" fill="#38bdf8" />
                    <circle cx="260" cy="40" r="2.5" fill="#38bdf8" />
                    <circle cx="280" cy="90" r="2" fill="#38bdf8" />
                    <circle cx="250" cy="140" r="2.2" fill="#38bdf8" />
                </g>
                <text x="50" y="25" fill="#64748b" font-size="8">Invisible Air Vapour</text>
                <text x="240" y="25" fill="#64748b" font-size="8">Invisible Air Vapour</text>

                <!-- Stainless Steel Tumbler -->
                <g transform="translate(130, 45)">
                    <!-- Steel Cup Body -->
                    <polygon points="0,0 60,0 50,120 10,120" fill="#94a3b8" stroke="#cbd5e1" stroke-width="2" />
                    <!-- Chilled Liquid Level Inside -->
                    <polygon points="4,20 56,20 48,116 12,116" fill="#0284c7" opacity="0.5" />
                    <!-- Floating Ice Cubes -->
                    <rect x="15" y="10" width="16" height="14" rx="2" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1" />
                    <rect x="30" y="15" width="16" height="14" rx="2" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1" />
                    
                    <!-- Condensation Beads on OUTER Wall -->
                    <g id="sim4-outer-beads">
                        <ellipse cx="-1" cy="40" rx="2.5" ry="3.5" fill="#38bdf8" stroke="#ffffff" stroke-width="0.5" />
                        <ellipse cx="1" cy="65" rx="3" ry="4" fill="#38bdf8" stroke="#ffffff" stroke-width="0.5" />
                        <ellipse cx="3" cy="90" rx="2.5" ry="3.5" fill="#38bdf8" stroke="#ffffff" stroke-width="0.5" />
                        <ellipse cx="61" cy="40" rx="2.5" ry="3.5" fill="#38bdf8" stroke="#ffffff" stroke-width="0.5" />
                        <ellipse cx="59" cy="65" rx="3" ry="4" fill="#38bdf8" stroke="#ffffff" stroke-width="0.5" />
                        <ellipse cx="56" cy="90" rx="2.5" ry="3.5" fill="#38bdf8" stroke="#ffffff" stroke-width="0.5" />
                    </g>
                    <text x="30" y="80" fill="#ffffff" font-size="7.5" font-weight="bold" text-anchor="middle">Steel Glass</text>
                </g>

                <!-- Callout Pointer Lines -->
                <line x1="85" y1="90" x2="125" y2="90" stroke="#f43f5e" stroke-width="1.5" marker-end="url(#arrow)" />
                <rect x="10" y="145" width="105" height="35" rx="4" fill="#0f172a" stroke="#334155" />
                <text x="15" y="158" fill="#f87171" font-size="7.5" font-weight="bold">Water from AIR</text>
                <text x="15" y="170" fill="#cbd5e1" font-size="7">Condenses on cold steel</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="toggleIceGlass('ice')" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                🧊 Fill with Chilled Ice Water
            </button>
            <button onclick="toggleIceGlass('warm')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-300 border border-slate-700 shadow transition">
                ☕ Fill with Lukewarm Water
            </button>
        </div>
        <div id="sim4-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Solid stainless steel does not leak! Droplets appear on the exterior because invisible moisture in the warm room air cools down and condenses on the cold metal surface.
        </div>
    </div>
    """,

    5: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Activity 3: Bag Sunbeam Water Cycle</span>
            <span id="sim5-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Solar Heat: Active Evaporation</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- The Sun through the Window -->
                <circle cx="45" cy="45" r="20" fill="#fbbf24" stroke="#f59e0b" stroke-width="2" />
                <line x1="45" y1="15" x2="45" y2="5" stroke="#fde047" stroke-width="2" />
                <line x1="45" y1="75" x2="45" y2="85" stroke="#fde047" stroke-width="2" />
                <line x1="15" y1="45" x2="5" y2="45" stroke="#fde047" stroke-width="2" />
                <line x1="75" y1="45" x2="85" y2="45" stroke="#fde047" stroke-width="2" />

                <!-- Sealed Transparent Plastic Bag -->
                <rect x="110" y="20" width="160" height="160" rx="8" fill="#1e293b" fill-opacity="0.3" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,2" />
                <!-- Tape strips at top -->
                <rect x="130" y="12" width="30" height="12" fill="#ca8a04" opacity="0.8" />
                <rect x="210" y="12" width="30" height="12" fill="#ca8a04" opacity="0.8" />

                <!-- Water Cup inside bag -->
                <path d="M 160,130 L 165,170 L 215,170 L 220,130 Z" fill="#475569" stroke="#94a3b8" />
                <path d="M 163,145 L 166,168 L 214,168 L 217,145 Z" fill="#0284c7" opacity="0.8" />
                <text x="190" y="162" fill="#bae6fd" font-size="7.5" font-weight="bold" text-anchor="middle">Water Cup</text>

                <!-- Rising Vapour Particles -->
                <g id="sim5-rising-vapour" stroke="#fef08a" stroke-width="1.5" stroke-dasharray="2,2">
                    <line x1="180" y1="125" x2="175" y2="85" />
                    <line x1="190" y1="125" x2="190" y2="80" />
                    <line x1="200" y1="125" x2="205" y2="85" />
                </g>

                <!-- Condensed Droplets on Upper Bag Ceiling -->
                <g id="sim5-ceiling-droplets">
                    <circle cx="140" cy="35" r="2.5" fill="#38bdf8" />
                    <circle cx="160" cy="32" r="3" fill="#38bdf8" />
                    <circle cx="180" cy="36" r="3.5" fill="#38bdf8" />
                    <circle cx="205" cy="32" r="3" fill="#38bdf8" />
                    <circle cx="230" cy="35" r="2.5" fill="#38bdf8" />
                    <circle cx="245" cy="38" r="2" fill="#38bdf8" />
                </g>

                <!-- Falling Mini Rain Streams -->
                <g id="sim5-mini-rain">
                    <line x1="140" y1="40" x2="140" y2="70" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" />
                    <line x1="230" y1="40" x2="230" y2="75" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" />
                </g>
                <text x="190" y="55" fill="#93c5fd" font-size="8" font-weight="bold" text-anchor="middle">Mini Clouds & Condensation</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="animateBagSolar('evaporate')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                ☀️ Sun Heat (Drive Evaporation)
            </button>
            <button onclick="animateBagSolar('rain')" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                🌧️ Cool Down (Trigger Mini-Rain)
            </button>
        </div>
        <div id="sim5-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            In a sealed bag on a sunny window, solar heat evaporates water into vapour. The vapour cools on the ceiling, condenses into droplets, and trickles down as mini-rain—a complete water cycle!
        </div>
    </div>
    """,

    6: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Planetary Water Cycle Engine</span>
            <span id="sim6-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30">Cycle: Complete Natural Flow</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <defs>
                    <linearGradient id="sim6-sky" x1="0%" y1="0%" x2="0%" y2="100%">
                        <stop offset="0%" stop-color="#0284c7" />
                        <stop offset="60%" stop-color="#38bdf8" />
                        <stop offset="100%" stop-color="#bae6fd" />
                    </linearGradient>
                </defs>
                <rect x="0" y="0" width="320" height="130" fill="url(#sim6-sky)" />

                <!-- The Sun -->
                <circle cx="45" cy="35" r="18" fill="#fbbf24" stroke="#f59e0b" stroke-width="2" />

                <!-- Clouds -->
                <g id="sim6-clouds" transform="translate(130, 25)">
                    <ellipse cx="30" cy="15" rx="20" ry="12" fill="#ffffff" />
                    <ellipse cx="45" cy="10" rx="16" ry="14" fill="#ffffff" />
                    <ellipse cx="60" cy="15" rx="18" ry="12" fill="#ffffff" />
                    <ellipse cx="75" cy="12" rx="14" ry="10" fill="#ffffff" />
                </g>

                <!-- Rain Falling from Clouds -->
                <g id="sim6-rain" stroke="#0284c7" stroke-width="1.8" stroke-linecap="round" stroke-dasharray="3,3">
                    <line x1="160" y1="45" x2="155" y2="70" />
                    <line x1="175" y1="45" x2="170" y2="75" />
                    <line x1="190" y1="45" x2="185" y2="70" />
                    <line x1="205" y1="45" x2="200" y2="75" />
                </g>

                <!-- Mountains (Right) -->
                <polygon points="180,130 240,50 280,130" fill="#475569" />
                <polygon points="230,64 240,50 250,64" fill="#ffffff" /> <!-- Snow peak -->
                <polygon points="250,130 285,65 320,130" fill="#334155" />
                <polygon points="278,78 285,65 292,78" fill="#ffffff" />

                <!-- Land & Forest Floor -->
                <rect x="0" y="130" width="320" height="70" fill="#15803d" />
                
                <!-- Ocean (Left) -->
                <path d="M 0,140 Q 40,135 80,140 L 80,200 L 0,200 Z" fill="#0284c7" />
                <text x="40" y="175" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Ocean</text>

                <!-- River flowing from Mountain to Ocean -->
                <path d="M 235,125 Q 160,140 80,150 L 80,165 Q 160,155 240,135 Z" fill="#38bdf8" />

                <!-- Tree on Land (Transpiration) -->
                <rect x="120" y="145" width="6" height="20" fill="#78350f" />
                <circle cx="123" cy="140" r="14" fill="#16a34a" />

                <!-- Dynamic Labels with Indicators -->
                <text x="45" y="75" fill="#b45309" font-size="7.5" font-weight="bold">1. Evaporation ⬆</text>
                <text x="175" y="20" fill="#1e293b" font-size="7.5" font-weight="bold">2. Condensation</text>
                <text x="160" y="88" fill="#0369a1" font-size="7.5" font-weight="bold">3. Rain ⬇</text>
                <text x="150" y="175" fill="#0f766e" font-size="7.5" font-weight="bold">4. River Runoff ➔</text>
            </svg>
        </div>
        <div class="grid grid-cols-4 gap-1.5">
            <button onclick="highlightCycleStep('evap')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-amber-300 border border-slate-700">
                ☀️ Evaporation
            </button>
            <button onclick="highlightCycleStep('cond')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-200 border border-slate-700">
                ☁️ Clouds
            </button>
            <button onclick="highlightCycleStep('precip')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-blue-300 border border-slate-700">
                🌧️ Rain
            </button>
            <button onclick="highlightCycleStep('runoff')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-emerald-300 border border-slate-700">
                🏞️ Runoff
            </button>
        </div>
        <div id="sim6-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            The water cycle circulates water endlessly: solar evaporation and plant transpiration lift vapour into clouds, falling as rain to recharge rivers, oceans, and groundwater.
        </div>
    </div>
    """,

    7: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Earth's Natural Filtration Sponge</span>
            <span id="sim7-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Process: Infiltration Active</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#050814" />

                <!-- Raindrops Falling on Soil Surface -->
                <g stroke="#38bdf8" stroke-width="1.8" stroke-linecap="round">
                    <line x1="50" y1="5" x2="48" y2="20" />
                    <line x1="110" y1="8" x2="108" y2="23" />
                    <line x1="180" y1="5" x2="178" y2="20" />
                    <line x1="250" y1="8" x2="248" y2="23" />
                </g>

                <!-- Layer 1: Topsoil & Grass (0-40) -->
                <rect x="20" y="25" width="280" height="30" fill="#78350f" stroke="#16a34a" stroke-width="3" />
                <text x="35" y="44" fill="#fef08a" font-size="8" font-weight="bold">1. Topsoil & Organic Humus</text>

                <!-- Layer 2: Sand & Gravel Filter (40-90) -->
                <rect x="20" y="55" width="280" height="40" fill="#a16207" />
                <!-- Pebbles / Gravel particles -->
                <circle cx="50" cy="75" r="4" fill="#ca8a04" />
                <circle cx="100" cy="80" r="5" fill="#ca8a04" />
                <circle cx="160" cy="70" r="3.5" fill="#ca8a04" />
                <circle cx="220" cy="82" r="4.5" fill="#ca8a04" />
                <circle cx="270" cy="74" r="4" fill="#ca8a04" />
                <text x="35" y="78" fill="#fde047" font-size="8" font-weight="bold">2. Sand & Gravel Natural Filter</text>

                <!-- Water Table Line -->
                <line id="sim7-water-table" x1="20" y1="95" x2="300" y2="95" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,2" />
                <text x="210" y="91" fill="#38bdf8" font-size="7.5" font-weight="bold">Water Table Level</text>

                <!-- Layer 3: Saturated Aquifer Zone (95-155) -->
                <rect id="sim7-aquifer" x="20" y="95" width="280" height="60" fill="#0284c7" opacity="0.45" />
                <text x="35" y="125" fill="#ffffff" font-size="8.5" font-weight="bold">3. Saturated Aquifer (Groundwater)</text>
                <text x="35" y="137" fill="#bae6fd" font-size="7">Pore spaces filled with pure filtered water</text>

                <!-- Layer 4: Impermeable Solid Bedrock (155-200) -->
                <rect x="20" y="155" width="280" height="40" fill="#1e293b" />
                <text x="35" y="180" fill="#94a3b8" font-size="8" font-weight="bold">4. Impermeable Solid Bedrock</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="simulateRainfallSeepage()" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🌧️ Raindown & Filter Infiltration
            </button>
            <button onclick="pumpAquiferWater()" class="p-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-bold text-white shadow transition">
                🚰 Pump Groundwater for Villages
            </button>
        </div>
        <div id="sim7-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Rainwater soaks down through soil and gravel layers, which filter out debris and suspended dirt. The water collects in deep porous rock formations called aquifers.
        </div>
    </div>
    """,

    8: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Dug Well vs Village Handpump Mechanics</span>
            <span id="sim8-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Device: Open Dug Well (Kuan)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- Ground Surface -->
                <rect x="0" y="80" width="320" height="120" fill="#3f2e18" />
                <rect x="0" y="80" width="320" height="6" fill="#15803d" />
                
                <!-- Water Table Line -->
                <line x1="0" y1="140" x2="320" y2="140" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" />
                <rect x="0" y="140" width="320" height="60" fill="#0284c7" opacity="0.35" />
                <text x="160" y="190" fill="#bae6fd" font-size="7.5" text-anchor="middle">Underground Saturated Aquifer</text>

                <!-- Left Half: Traditional Open Dug Well (Kuan) -->
                <g id="sim8-well-art" transform="translate(60, 40)">
                    <!-- Masonry Wall -->
                    <rect x="-35" y="40" width="10" height="90" fill="#94a3b8" />
                    <rect x="25" y="40" width="10" height="90" fill="#94a3b8" />
                    <rect x="-25" y="100" width="50" height="30" fill="#0284c7" opacity="0.8" />
                    <!-- Well Roof & Pulley (Charkhi) -->
                    <line x1="-30" y1="40" x2="-30" y2="-10" stroke="#78350f" stroke-width="3" />
                    <line x1="30" y1="40" x2="30" y2="-10" stroke="#78350f" stroke-width="3" />
                    <line x1="-35" y1="-10" x2="35" y2="-10" stroke="#78350f" stroke-width="3" />
                    <circle cx="0" cy="5" r="7" fill="#ca8a04" stroke="#facc15" stroke-width="1.5" />
                    <!-- Rope and Bucket -->
                    <line x1="0" y1="12" x2="0" y2="70" stroke="#fde047" stroke-width="1.5" />
                    <rect id="sim8-bucket" x="-7" y="70" width="14" height="16" rx="2" fill="#d97706" />
                    <text x="0" y="35" fill="#f8fafc" font-size="8" font-weight="bold" text-anchor="middle">Open Well</text>
                </g>

                <!-- Right Half: Village Handpump -->
                <g id="sim8-pump-art" transform="translate(240, 45)">
                    <!-- Pipe going down into aquifer -->
                    <rect x="-3" y="35" width="6" height="95" fill="#cbd5e1" stroke="#64748b" stroke-width="1" />
                    <!-- Pump Body & Spout -->
                    <rect x="-10" y="5" width="20" height="35" fill="#047857" stroke="#10b981" stroke-width="1.5" />
                    <polygon points="10,25 22,28 22,35 10,32" fill="#047857" />
                    <!-- Water Stream from Spout -->
                    <path id="sim8-pump-water" d="M 22,32 Q 28,45 28,55" stroke="#38bdf8" stroke-width="3" fill="none" opacity="0" />
                    <!-- Hand Lever -->
                    <line id="sim8-lever" x1="-10" y1="15" x2="-35" y2="5" stroke="#f59e0b" stroke-width="3.5" stroke-linecap="round" />
                    <text x="0" y="-2" fill="#6ee7b7" font-size="8" font-weight="bold" text-anchor="middle">Handpump</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="operateWellBucket()" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                🪢 Pull Well Bucket (Pulley)
            </button>
            <button onclick="operateHandpump()" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🚰 Work Handpump Lever
            </button>
        </div>
        <div id="sim8-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Open dug wells reach the water table using a rope and pulley, while handpumps use mechanical suction cylinders with one-way valves to lift clean water from deep underground.
        </div>
    </div>
    """,

    9: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Groundwater Recharge: Paved vs Natural</span>
            <span id="sim9-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Mode: Paved Concrete City</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040714" />

                <!-- Left Half: Concrete City (Impervious) -->
                <rect x="10" y="20" width="145" height="160" rx="6" fill="#0f172a" stroke="#334155" />
                <text x="82" y="36" fill="#f87171" font-size="8.5" font-weight="bold" text-anchor="middle">Concrete Paved City</text>
                
                <!-- Buildings & Tar Road -->
                <rect x="25" y="45" width="30" height="50" fill="#334155" />
                <rect x="60" y="55" width="25" height="40" fill="#1e293b" />
                <rect x="90" y="40" width="35" height="55" fill="#334155" />
                <rect x="20" y="95" width="125" height="12" fill="#475569" stroke="#94a3b8" />
                
                <!-- Rain & Runoff Flow -->
                <g stroke="#38bdf8" stroke-width="1.5">
                    <line x1="40" y1="25" x2="38" y2="40" />
                    <line x1="80" y1="25" x2="78" y2="40" />
                    <line x1="120" y1="25" x2="118" y2="40" />
                    <!-- Runoff Arrow rushing out -->
                    <path d="M 30,102 L 135,102" stroke="#ef4444" stroke-width="2.5" marker-end="url(#arrow)" />
                </g>
                <text x="82" y="117" fill="#fca5a5" font-size="7">90% Runoff ➔ Flash Floods</text>
                <!-- Dried Aquifer below city -->
                <rect x="20" y="125" width="125" height="45" fill="#78350f" />
                <text x="82" y="152" fill="#fca5a5" font-size="7.5" font-weight="bold" text-anchor="middle">Water Table Sinking!</text>

                <!-- Right Half: Natural Forest & Soak Pit (Permeable) -->
                <rect x="165" y="20" width="145" height="160" rx="6" fill="#0f172a" stroke="#15803d" />
                <text x="237" y="36" fill="#86efac" font-size="8.5" font-weight="bold" text-anchor="middle">Forest & Green Soil</text>

                <!-- Trees & Lawn -->
                <rect x="175" y="70" width="5" height="25" fill="#78350f" />
                <circle cx="177" cy="65" r="12" fill="#16a34a" />
                <rect x="210" y="70" width="5" height="25" fill="#78350f" />
                <circle cx="212" cy="65" r="14" fill="#22c55e" />
                <rect x="175" y="95" width="125" height="12" fill="#15803d" />

                <!-- Soak Pit in corner -->
                <rect x="260" y="85" width="25" height="22" rx="2" fill="#ca8a04" stroke="#eab308" />
                <text x="272" y="99" fill="#000000" font-size="6" font-weight="bold" text-anchor="middle">Soak Pit</text>

                <!-- Infiltration down arrows -->
                <g stroke="#22c55e" stroke-width="1.8">
                    <line x1="190" y1="107" x2="190" y2="125" marker-end="url(#arrow)" />
                    <line x1="230" y1="107" x2="230" y2="125" marker-end="url(#arrow)" />
                    <line x1="272" y1="107" x2="272" y2="125" marker-end="url(#arrow)" />
                </g>
                <!-- Recharged Full Aquifer -->
                <rect x="175" y="125" width="125" height="45" fill="#0284c7" opacity="0.8" />
                <text x="237" y="152" fill="#ffffff" font-size="7.5" font-weight="bold" text-anchor="middle">Aquifer Fully Recharged!</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setSurfaceComparison('paved')" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                🏢 Concrete City (Impervious Runoff)
            </button>
            <button onclick="setSurfaceComparison('green')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🌳 Green Soil & Soak Pit (Recharge)
            </button>
        </div>
        <div id="sim9-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Paved roads seal the ground, causing rainwater to rush away as flood runoff. In contrast, open soil, gardens, and gravel soak pits allow rainwater to percolate down and recharge the water table.
        </div>
    </div>
    """,

    10: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Natural Freshwater Reservoirs</span>
            <span id="sim10-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Feature: Perennial Himalayan River</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040817" />

                <!-- Landscape with Mountain, River, Pond, Lake -->
                <!-- Snow Mountains in Background -->
                <polygon points="120,60 160,15 200,60" fill="#475569" />
                <polygon points="150,28 160,15 170,28" fill="#ffffff" />
                <polygon points="180,60 215,20 250,60" fill="#334155" />
                <polygon points="208,30 215,20 222,30" fill="#ffffff" />

                <!-- Perennial River Path -->
                <path d="M 160,35 Q 150,70 120,90 T 80,130 T 40,200 L 0,200 L 0,160 Q 60,120 100,80 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" />
                <text x="60" y="145" fill="#ffffff" font-size="7.5" font-weight="bold" transform="rotate(-30 60 145)">Flowing River</text>

                <!-- Natural Lake (Jheel) Top Right -->
                <g onclick="selectSurfaceBody('lake')" class="cursor-pointer" transform="translate(230, 80)">
                    <ellipse cx="0" cy="0" rx="45" ry="22" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5" />
                    <text x="0" y="3" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Lake (Jheel)</text>
                    <text x="0" y="13" fill="#bae6fd" font-size="6.5" text-anchor="middle">Deep Freshwater Basin</text>
                </g>

                <!-- Village Pond (Talab) Bottom Right -->
                <g onclick="selectSurfaceBody('pond')" class="cursor-pointer" transform="translate(230, 150)">
                    <ellipse cx="0" cy="0" rx="35" ry="18" fill="#0284c7" stroke="#22d3ee" stroke-width="1.5" />
                    <text x="0" y="2" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Pond (Talab)</text>
                    <text x="0" y="11" fill="#bae6fd" font-size="6.5" text-anchor="middle">Rainfed Catchment</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="selectSurfaceBody('river')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-sky-300 border border-slate-700">
                🏔️ River (Nadi)
            </button>
            <button onclick="selectSurfaceBody('lake')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-cyan-300 border border-slate-700">
                🌊 Lake (Jheel)
            </button>
            <button onclick="selectSurfaceBody('pond')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-emerald-300 border border-slate-700">
                🏞️ Pond (Talab)
            </button>
        </div>
        <div id="sim10-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Perennial rivers like the Ganga flow year-round fed by melting Himalayan snow. Lakes store deep freshwater basins, while village ponds hold monsoon rainwater for community use.
        </div>
    </div>
    """,

    11: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Activity 6: Paper Mountain & River Contours</span>
            <span id="sim11-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Action: Spraying Mist & Seeds</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- Crumpled Newspaper Mountain Creases in Tray -->
                <polygon points="40,160 90,40 150,110 200,30 260,120 290,170 30,170" fill="#334155" stroke="#64748b" stroke-width="1.5" />
                <!-- Fold shading -->
                <polygon points="90,40 150,110 120,160 40,160" fill="#1e293b" opacity="0.6" />
                <polygon points="200,30 260,120 210,165 150,110" fill="#1e293b" opacity="0.6" />

                <!-- Water Mist Spray from Top -->
                <g id="sim11-spray" opacity="0.8">
                    <circle cx="190" cy="15" r="2" fill="#38bdf8" />
                    <circle cx="210" cy="20" r="2.5" fill="#38bdf8" />
                    <circle cx="200" cy="25" r="1.5" fill="#38bdf8" />
                </g>

                <!-- Flowing River Crease Path through valleys -->
                <path id="sim11-river-path" d="M 200,35 Q 170,80 150,110 T 110,140 T 70,170" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" />
                
                <!-- Tiny Mustard Seeds carried along by water -->
                <g id="sim11-seeds" fill="#facc15">
                    <circle cx="185" cy="55" r="2.2" />
                    <circle cx="165" cy="85" r="2.2" />
                    <circle cx="150" cy="110" r="2.5" />
                    <circle cx="130" cy="128" r="2.2" />
                    <circle cx="100" cy="145" r="2.5" />
                    <circle cx="70" cy="165" r="3" />
                </g>
                <text x="160" y="190" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Mustard seeds transport down valley creases under gravity</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="sprayMountainMist()" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                🌧️ Spray Mist on Mountain Paper
            </button>
            <button onclick="washDownSeeds()" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                🌾 Watch Mustard Seeds Flow Downhill
            </button>
        </div>
        <div id="sim11-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Water always flows downhill from high peaks to valleys along the path of least resistance. Just as water carries mustard seeds down the paper creases, rivers transport fertile sediment to the plains.
        </div>
    </div>
    """,

    12: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Freshwater Pond Ecosystem Layers</span>
            <span id="sim12-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Zone: Surface & Water Column</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040817" />

                <!-- Water Column in Pond -->
                <rect x="0" y="60" width="320" height="140" fill="#0284c7" fill-opacity="0.55" />
                <!-- Muddy Pond Bed -->
                <rect x="0" y="175" width="320" height="25" fill="#451a03" />

                <!-- Shoreline & Heron Wading (Left) -->
                <rect x="0" y="45" width="60" height="130" fill="#15803d" />
                <!-- Pond Heron Standing on Long Legs -->
                <g id="sim12-heron" transform="translate(45, 25)">
                    <line x1="0" y1="25" x2="0" y2="45" stroke="#ca8a04" stroke-width="1.8" />
                    <line x1="5" y1="25" x2="5" y2="45" stroke="#ca8a04" stroke-width="1.8" />
                    <!-- Body & Long Neck -->
                    <ellipse cx="2" cy="20" rx="9" ry="6" fill="#e2e8f0" stroke="#94a3b8" />
                    <path d="M 6,18 Q 12,8 14,3" stroke="#e2e8f0" stroke-width="2.5" fill="none" />
                    <polygon points="14,3 24,5 14,7" fill="#facc15" /> <!-- Spear Beak -->
                    <text x="2" y="-2" fill="#f8fafc" font-size="7" font-weight="bold" text-anchor="middle">Heron</text>
                </g>

                <!-- Floating Lotus & Leaves on Surface -->
                <g transform="translate(130, 55)">
                    <ellipse cx="0" cy="0" rx="20" ry="6" fill="#16a34a" stroke="#22c55e" stroke-width="1.2" />
                    <circle cx="2" cy="-4" r="1.5" fill="#38bdf8" /> <!-- Dew drop -->
                    <!-- Pink Blossom -->
                    <circle cx="0" cy="-6" r="6" fill="#f43f5e" />
                    <circle cx="0" cy="-6" r="3" fill="#fde047" />
                    <text x="0" y="-14" fill="#fda4af" font-size="7" font-weight="bold" text-anchor="middle">Lotus</text>
                </g>

                <!-- Swimming Fish in Mid-Water -->
                <g id="sim12-fish" transform="translate(180, 115)">
                    <ellipse cx="0" cy="0" rx="14" ry="7" fill="#f97316" stroke="#fb923c" stroke-width="1.2" />
                    <polygon points="-14,0 -22,-6 -22,6" fill="#ea580c" />
                    <circle cx="8" cy="-2" r="1.5" fill="#ffffff" />
                    <circle cx="9" cy="-2" r="0.8" fill="#000000" />
                </g>

                <!-- Submerged Hydrilla Weeds from bottom -->
                <path d="M 270,175 Q 260,130 275,95" stroke="#15803d" stroke-width="3" fill="none" />
                <path d="M 285,175 Q 295,140 280,105" stroke="#16a34a" stroke-width="2.5" fill="none" />
                <text x="280" y="85" fill="#86efac" font-size="7" font-weight="bold" text-anchor="middle">Hydrilla</text>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="inspectPondZone('surface')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-rose-300 border border-slate-700">
                🪷 Surface (Lotus)
            </button>
            <button onclick="inspectPondZone('midwater')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-amber-300 border border-slate-700">
                🐟 Mid-Water (Fish)
            </button>
            <button onclick="inspectPondZone('shore')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-sky-300 border border-slate-700">
                🦤 Shore (Heron)
            </button>
        </div>
        <div id="sim12-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            A freshwater pond is stratified into distinct biological zones: floating plants capture air and sun, swimming fish populate the mid-water column, and wading birds hunt along the shore.
        </div>
    </div>
    """,

    13: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Aquatic Plant Adaptations Laboratory</span>
            <span id="sim13-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Specimen: Lotus Leaf (Waxy Coating)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- Specimen Display Stage -->
                <!-- Lotus Leaf Mode -->
                <g id="sim13-specimen-lotus" style="display: block;">
                    <ellipse cx="160" cy="90" rx="90" ry="45" fill="#15803d" stroke="#22c55e" stroke-width="2" />
                    <!-- Radiating veins -->
                    <line x1="160" y1="90" x2="100" y2="70" stroke="#166534" stroke-width="1.5" />
                    <line x1="160" y1="90" x2="220" y2="70" stroke="#166534" stroke-width="1.5" />
                    <line x1="160" y1="90" x2="120" y2="120" stroke="#166534" stroke-width="1.5" />
                    <line x1="160" y1="90" x2="200" y2="120" stroke="#166534" stroke-width="1.5" />
                    <!-- Water Drop Beading Up without wetting -->
                    <circle cx="160" cy="85" r="9" fill="#38bdf8" filter="drop-shadow(0 0 4px #0284c7)" />
                    <circle cx="157" cy="82" r="3" fill="#ffffff" />
                    <text x="160" y="150" fill="#86efac" font-size="9" font-weight="bold" text-anchor="middle">Lotus Effect: Hydrophobic Wax Layer</text>
                    <text x="160" y="163" fill="#cbd5e1" font-size="7.5" text-anchor="middle">Droplets bead up and roll off; stomata located only on upper surface</text>
                </g>

                <!-- Water Hyacinth Spongy Aerenchyma Mode -->
                <g id="sim13-specimen-hyacinth" style="display: none;">
                    <!-- Cross Section of Petiole Stem -->
                    <ellipse cx="160" cy="90" rx="70" ry="40" fill="#166534" stroke="#22c55e" stroke-width="2" />
                    <!-- Air Cavity Honeycomb Lacunae -->
                    <g fill="#0f172a" stroke="#4ade80" stroke-width="1">
                        <circle cx="130" cy="80" r="8" />
                        <circle cx="150" cy="75" r="9" />
                        <circle cx="170" cy="75" r="9" />
                        <circle cx="190" cy="80" r="8" />
                        <circle cx="140" cy="98" r="8" />
                        <circle cx="160" cy="100" r="9" />
                        <circle cx="180" cy="98" r="8" />
                    </g>
                    <text x="160" y="150" fill="#a7f3d0" font-size="9" font-weight="bold" text-anchor="middle">Aerenchyma: Spongy Air Chambers</text>
                    <text x="160" y="163" fill="#cbd5e1" font-size="7.5" text-anchor="middle">Large gas pockets act as internal life jackets for buoyancy</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="selectPlantSpecimen('lotus')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🪷 Inspect Lotus Leaf (Wax & Stomata)
            </button>
            <button onclick="selectPlantSpecimen('hyacinth')" class="p-2 rounded-xl bg-purple-600 hover:bg-purple-500 text-xs font-bold text-white shadow transition">
                🎈 Inspect Hyacinth Stem (Air Pockets)
            </button>
        </div>
        <div id="sim13-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Lotus leaves have a waxy waterproof coating that prevents rotting, while water hyacinths contain spongy aerenchyma air pockets that provide buoyant lift on the surface.
        </div>
    </div>
    """,

    14: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Aquatic Animal Survival Adaptations</span>
            <span id="sim14-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Animal: Streamlined Fish (Gills & Fins)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040817" />

                <!-- Dynamic Animal Display -->
                <!-- Fish Architecture -->
                <g id="sim14-art-fish" style="display: block;" transform="translate(160, 95)">
                    <!-- Streamlined Body -->
                    <ellipse cx="0" cy="0" rx="65" ry="32" fill="#0284c7" stroke="#38bdf8" stroke-width="2" />
                    <!-- Caudal Tail Fin -->
                    <polygon points="-65,0 -100,-25 -95,0 -100,25" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5" />
                    <!-- Dorsal Fin -->
                    <polygon points="-10,-32 15,-48 25,-32" fill="#0369a1" stroke="#38bdf8" />
                    <!-- Pectoral Fin -->
                    <polygon points="5,5 25,18 10,22" fill="#38bdf8" />
                    <!-- Crimson Gill Slit -->
                    <path d="M 25,-18 Q 30,0 25,18" stroke="#ef4444" stroke-width="3" fill="none" />
                    <circle cx="45" cy="-8" r="4" fill="#ffffff" />
                    <circle cx="46" cy="-8" r="2" fill="#000000" />
                    <!-- Labels -->
                    <text x="25" y="-23" fill="#f87171" font-size="7.5" font-weight="bold">Crimson Gills</text>
                    <text x="-80" y="-30" fill="#7dd3fc" font-size="7.5" font-weight="bold">Streamlined Tail</text>
                    <text x="0" y="52" fill="#bae6fd" font-size="8.5" font-weight="bold" text-anchor="middle">Spindle body reduces friction; gills extract dissolved oxygen</text>
                </g>

                <!-- Water Scorpion Architecture -->
                <g id="sim14-art-scorpion" style="display: none;" transform="translate(160, 95)">
                    <!-- Water Surface Line -->
                    <line x1="-120" y1="-50" x2="120" y2="-50" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3" />
                    <text x="110" y="-55" fill="#38bdf8" font-size="7.5">Water Surface</text>
                    <!-- Long Breathing Snorkel Tube -->
                    <line x1="0" y1="10" x2="0" y2="-55" stroke="#facc15" stroke-width="2.5" />
                    <circle cx="0" cy="-55" r="3" fill="#ef4444" />
                    <!-- Insect Body -->
                    <ellipse cx="0" cy="25" rx="14" ry="25" fill="#78350f" stroke="#ca8a04" stroke-width="1.5" />
                    <!-- Grasping Raptor Forelegs -->
                    <path d="M -10,10 L -25,-5 L -35,5" fill="none" stroke="#78350f" stroke-width="2.5" />
                    <path d="M 10,10 L 25,-5 L 35,5" fill="none" stroke="#78350f" stroke-width="2.5" />
                    <text x="0" y="65" fill="#fde047" font-size="8.5" font-weight="bold" text-anchor="middle">Water Scorpion Breathing Snorkel Tube</text>
                    <text x="0" y="78" fill="#cbd5e1" font-size="7.5" text-anchor="middle">Breathes atmospheric air through tail tube while hiding underwater</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="selectAnimalSpecimen('fish')" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow transition">
                🐟 Streamlined Fish & Crimson Gills
            </button>
            <button onclick="selectAnimalSpecimen('scorpion')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                🦂 Water Scorpion Snorkel Tube
            </button>
        </div>
        <div id="sim14-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Fish use streamlined spindle bodies to slice through water and gills to extract dissolved oxygen. Water scorpions extend long tail tubes to the surface like snorkels to breathe atmospheric air.
        </div>
    </div>
    """,

    15: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">River Food Chain & Energy Flow</span>
            <span id="sim15-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Ecosystem: Healthy Balance</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />

                <!-- 4 Trophic Levels in a Line -->
                <!-- Level 1: Algae -->
                <g transform="translate(40, 100)">
                    <circle cx="0" cy="0" r="22" fill="#064e3b" stroke="#10b981" stroke-width="2" />
                    <text x="0" y="-4" fill="#6ee7b7" font-size="12" text-anchor="middle">🌿</text>
                    <text x="0" y="11" fill="#a7f3d0" font-size="7" font-weight="bold" text-anchor="middle">Algae</text>
                    <text x="0" y="32" fill="#6ee7b7" font-size="6.5" text-anchor="middle">Producers</text>
                </g>

                <line x1="64" y1="100" x2="96" y2="100" stroke="#34d399" stroke-width="2" marker-end="url(#arrow)" />

                <!-- Level 2: Insect Larva / Tadpole -->
                <g transform="translate(120, 100)">
                    <circle cx="0" cy="0" r="22" fill="#0c4a6e" stroke="#0284c7" stroke-width="2" />
                    <text x="0" y="-4" fill="#38bdf8" font-size="12" text-anchor="middle">🦐</text>
                    <text x="0" y="11" fill="#bae6fd" font-size="7" font-weight="bold" text-anchor="middle">Tadpole</text>
                    <text x="0" y="32" fill="#7dd3fc" font-size="6.5" text-anchor="middle">Herbivore</text>
                </g>

                <line x1="144" y1="100" x2="176" y2="100" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)" />

                <!-- Level 3: Small Fish -->
                <g transform="translate(200, 100)">
                    <circle cx="0" cy="0" r="22" fill="#78350f" stroke="#f59e0b" stroke-width="2" />
                    <text x="0" y="-4" fill="#fbbf24" font-size="12" text-anchor="middle">🐟</text>
                    <text x="0" y="11" fill="#fef3c7" font-size="7" font-weight="bold" text-anchor="middle">Small Fish</text>
                    <text x="0" y="32" fill="#fde047" font-size="6.5" text-anchor="middle">Carnivore</text>
                </g>

                <line x1="224" y1="100" x2="256" y2="100" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)" />

                <!-- Level 4: Pond Heron (Apex) -->
                <g transform="translate(280, 100)">
                    <circle cx="0" cy="0" r="22" fill="#4c0519" stroke="#f43f5e" stroke-width="2" />
                    <text x="0" y="-4" fill="#fda4af" font-size="12" text-anchor="middle">🦤</text>
                    <text x="0" y="11" fill="#fecdd3" font-size="7" font-weight="bold" text-anchor="middle">Heron</text>
                    <text x="0" y="32" fill="#f43f5e" font-size="6.5" text-anchor="middle">Apex Predator</text>
                </g>

                <!-- Feedback Banner -->
                <rect x="25" y="155" width="270" height="32" rx="5" fill="#0f172a" stroke="#334155" />
                <text id="sim15-chain-status" x="160" y="175" fill="#a7f3d0" font-size="8.5" font-weight="bold" text-anchor="middle">Energy flows smoothly from solar-powered algae to apex herons.</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="simulatePollutionImpact(false)" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🌿 Healthy Balanced River
            </button>
            <button onclick="simulatePollutionImpact(true)" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                ☣️ Discharge Toxic Pollutants
            </button>
        </div>
        <div id="sim15-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Energy flows along the food chain: green algae make food from sunlight, feeding insects and tadpoles, which nourish small fish, which sustain herons. Polluting water disrupts the entire chain.
        </div>
    </div>
    """,

    16: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Drought Impact & Water Conservation Meter</span>
            <span id="sim16-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Action: Water Guardian (Conserving)</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040714" />

                <!-- Left Half: Drought Landscape -->
                <g id="sim16-scene-drought" style="display: none;">
                    <rect x="20" y="20" width="280" height="130" rx="8" fill="#78350f" />
                    <!-- Cracked Earth Lines -->
                    <path d="M 40,60 L 80,90 L 120,70 L 160,110 L 220,80 L 280,120" stroke="#ca8a04" stroke-width="2.5" fill="none" />
                    <path d="M 80,90 L 90,130 M 160,110 L 170,140 M 220,80 L 240,110" stroke="#ca8a04" stroke-width="2" />
                    <!-- Withered Crop -->
                    <line x1="100" y1="120" x2="100" y2="100" stroke="#a16207" stroke-width="2" />
                    <line x1="200" y1="110" x2="200" y2="90" stroke="#a16207" stroke-width="2" />
                    <text x="160" y="45" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">Severe Drought (Sookha)</text>
                    <text x="160" y="60" fill="#fde047" font-size="8" text-anchor="middle">Wells run dry, crops wither, and cattle suffer acute water distress</text>
                </g>

                <!-- Right Half: Water-Wise Conserving Home -->
                <g id="sim16-scene-waterwise" style="display: block;">
                    <rect x="20" y="20" width="280" height="130" rx="8" fill="#064e3b" />
                    <!-- Rooftop Rainwater Harvest Tank -->
                    <rect x="50" y="50" width="60" height="40" fill="#0f766e" stroke="#14b8a6" stroke-width="1.5" />
                    <path d="M 40,50 L 80,30 L 120,50 Z" fill="#b91c1c" />
                    <!-- Rain Pipe to Soak Pit -->
                    <line x1="110" y1="50" x2="110" y2="110" stroke="#38bdf8" stroke-width="3" />
                    <rect x="95" y="110" width="30" height="25" rx="3" fill="#ca8a04" stroke="#facc15" />
                    <text x="110" y="125" fill="#000000" font-size="6" font-weight="bold" text-anchor="middle">Soak Pit</text>

                    <!-- Green Garden nourished by conserved water -->
                    <circle cx="210" cy="85" r="22" fill="#16a34a" />
                    <circle cx="240" cy="90" r="18" fill="#22c55e" />
                    <text x="225" y="125" fill="#a7f3d0" font-size="7.5" font-weight="bold" text-anchor="middle">Lush Recharged Garden</text>
                    <text x="160" y="42" fill="#a7f3d0" font-size="10" font-weight="bold" text-anchor="middle">Water-Wise Community Stewardship</text>
                </g>

                <!-- Savings Counter -->
                <rect x="25" y="160" width="270" height="30" rx="5" fill="#0f172a" stroke="#334155" />
                <text id="sim16-savings-text" x="160" y="180" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">Daily Conservation Savings: ~15 to 50 Liters per Household</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="toggleConservationView('wise')" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                🚰 Water-Wise Stewardship
            </button>
            <button onclick="toggleConservationView('drought')" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                🏜️ View Drought Devastation
            </button>
        </div>
        <div id="sim16-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Droughts dry up rivers, ruin crops, and deplete aquifers. Practicing simple water-wise habits—turning off taps, repairing leaks, and harvesting rainwater into soak pits—protects life.
        </div>
    </div>
    """
}

