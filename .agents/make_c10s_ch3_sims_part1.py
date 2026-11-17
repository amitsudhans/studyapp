"""Interactive Simulators 1 to 8 for Class 10 Science Chapter 3: Metals and Non-metals
High-fidelity, responsive, SVG-based laboratory simulators with Tailwind CSS.
"""

simulators = {
    1: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 3.1 - 3.7: Physical Properties of Metals</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim1Mode('lustre')" id="sim1BtnLustre" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Lustre & Knife</button>
            <button onclick="setSim1Mode('hammer')" id="sim1BtnHammer" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Malleability & Ductility</button>
            <button onclick="setSim1Mode('thermal')" id="sim1BtnThermal" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Conduction & Circuit</button>
        </div>
    </div>

    <!-- Mode 1: Lustre & Knife Test -->
    <div id="sim1LustreView" class="space-y-3">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-sky-400 block mb-1">Activity 3.1: Metallic Lustre & Sandpaper</span>
                <svg viewBox="0 0 200 110" class="w-full h-24 mx-auto">
                    <!-- Metal Strip (Iron/Copper) -->
                    <rect id="sim1MetalStrip" x="30" y="40" width="140" height="30" rx="4" fill="#64748b" stroke="#475569" stroke-width="2" class="transition-all duration-700"/>
                    <text id="sim1StripText" x="100" y="59" font-size="10" fill="#cbd5e1" font-weight="bold" text-anchor="middle">Dull / Oxidised Surface</text>
                    <!-- Sandpaper icon -->
                    <g id="sim1Sandpaper" transform="translate(140, 15)" opacity="0" class="transition-opacity duration-500">
                        <rect x="0" y="0" width="30" height="20" rx="2" fill="#d97706" stroke="#b45309" stroke-width="1"/>
                        <text x="15" y="13" font-size="7" fill="#fff" text-anchor="middle">Sandpaper</text>
                    </g>
                    <!-- Sparkle stars -->
                    <g id="sim1Sparkles" opacity="0" class="transition-opacity duration-700">
                        <path d="M 60 35 L 63 43 L 71 45 L 63 47 L 60 55 L 57 47 L 49 45 L 57 43 Z" fill="#fef08a"/>
                        <path d="M 130 35 L 133 43 L 141 45 L 133 47 L 130 55 L 127 47 L 119 45 L 127 43 Z" fill="#fef08a"/>
                    </g>
                </svg>
                <div class="flex justify-center gap-2 mt-2">
                    <button onclick="rubSandpaper()" class="px-3 py-1 rounded bg-sky-600/30 hover:bg-sky-600/50 text-sky-200 border border-sky-500/40 text-xs font-bold">Rub with Sandpaper</button>
                    <button onclick="resetLustre()" class="px-2 py-1 rounded bg-slate-800 text-slate-400 hover:text-slate-200 text-xs">Reset</button>
                </div>
                <p id="sim1LustreMsg" class="text-[11px] text-slate-400 mt-1">Metals in pure state have a shiny surface known as metallic lustre.</p>
            </div>

            <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-amber-400 block mb-1">Activity 3.2: Hardness vs Soft Sodium</span>
                <svg viewBox="0 0 200 110" class="w-full h-24 mx-auto">
                    <!-- Metal Sample -->
                    <rect id="sim1SampleBlock" x="40" y="55" width="55" height="35" rx="3" fill="#94a3b8" stroke="#64748b" stroke-width="1.5"/>
                    <rect id="sim1CutBlock" x="97" y="55" width="55" height="35" rx="3" fill="#94a3b8" stroke="#64748b" stroke-width="1.5" opacity="0" class="transition-all duration-500"/>
                    <text id="sim1SampleLabel" x="95" y="77" font-size="10" fill="#1e293b" font-weight="bold" text-anchor="middle">Iron (Hard)</text>
                    <!-- Knife -->
                    <g id="sim1Knife" transform="translate(85, 10)" class="transition-transform duration-500">
                        <polygon points="10,0 20,0 12,35 10,35" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1"/>
                        <rect x="7" y="-15" width="10" height="15" rx="2" fill="#78350f"/>
                    </g>
                </svg>
                <div class="flex justify-center gap-2 mt-2">
                    <button onclick="testKnife('iron')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold">Cut Iron</button>
                    <button onclick="testKnife('sodium')" class="px-2.5 py-1 rounded bg-amber-600/30 hover:bg-amber-600/50 text-amber-200 border border-amber-500/40 text-xs font-bold">Cut Sodium</button>
                </div>
                <p id="sim1KnifeMsg" class="text-[11px] text-slate-400 mt-1">Alkali metals (Li, Na, K) are soft and can easily be cut with a knife.</p>
            </div>
        </div>
    </div>

    <!-- Mode 2: Hammer & Wire -->
    <div id="sim1HammerView" class="hidden space-y-3">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-rose-400 block mb-1">Activity 3.3: Malleability (Hammer Test)</span>
                <svg viewBox="0 0 200 110" class="w-full h-24 mx-auto">
                    <!-- Anvil block -->
                    <rect x="30" y="80" width="140" height="20" fill="#334155" rx="3"/>
                    <!-- Metal piece beaten into thin sheet -->
                    <rect id="sim1HammerMetal" x="80" y="70" width="40" height="10" rx="1" fill="#f59e0b" class="transition-all duration-300"/>
                    <!-- Hammer -->
                    <g id="sim1HammerTool" transform="translate(85, 20)" class="transition-transform duration-200">
                        <rect x="0" y="15" width="30" height="18" rx="2" fill="#64748b" stroke="#334155"/>
                        <rect x="12" y="-15" width="6" height="30" fill="#78350f"/>
                    </g>
                </svg>
                <button onclick="strikeHammer()" class="mt-2 px-3 py-1 rounded bg-rose-600/30 hover:bg-rose-600/50 text-rose-200 border border-rose-500/40 text-xs font-bold">Strike with Hammer</button>
                <p id="sim1HammerMsg" class="text-[11px] text-slate-400 mt-1">Metals can be beaten into thin sheets without shattering (Gold & Silver most malleable).</p>
            </div>

            <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-amber-300 block mb-1">Activity 3.4: Ductility (1 g Gold = 2 km Wire)</span>
                <svg viewBox="0 0 200 110" class="w-full h-24 mx-auto">
                    <!-- Gold pellet -->
                    <circle id="sim1GoldPellet" cx="50" cy="55" r="14" fill="#fbbf24" stroke="#d97706" stroke-width="2" class="transition-all duration-700"/>
                    <!-- Drawn wire -->
                    <line id="sim1GoldWire" x1="50" y1="55" x2="50" y2="55" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="3 1" class="transition-all duration-700"/>
                    <circle id="sim1Spool" cx="170" cy="55" r="12" fill="#475569" stroke="#334155" stroke-width="2"/>
                    <text id="sim1WireLengthText" x="110" y="42" font-size="10" fill="#fbbf24" font-weight="bold" text-anchor="middle" opacity="0">Drawn into wire: 2,000 metres!</text>
                </svg>
                <button onclick="drawWire()" class="mt-2 px-3 py-1 rounded bg-amber-600/30 hover:bg-amber-600/50 text-amber-200 border border-amber-500/40 text-xs font-bold">Draw into Wire</button>
                <p id="sim1DuctileMsg" class="text-[11px] text-slate-400 mt-1">Ductility is the ability to be drawn into thin wires (Gold is the most ductile metal).</p>
            </div>
        </div>
    </div>

    <!-- Mode 3: Thermal & Circuit -->
    <div id="sim1ThermalView" class="hidden space-y-3">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-orange-400 block mb-1">Activity 3.5: Thermal Conduction (Wax Pin Drop)</span>
                <svg viewBox="0 0 200 110" class="w-full h-24 mx-auto">
                    <!-- Stand & clamp -->
                    <rect x="25" y="10" width="8" height="90" fill="#475569"/>
                    <rect x="20" y="30" width="20" height="8" fill="#334155"/>
                    <!-- Metal wire clamped -->
                    <line x1="30" y1="34" x2="170" y2="34" stroke="#cbd5e1" stroke-width="4"/>
                    <!-- Pin attached with wax -->
                    <g id="sim1WaxPin" transform="translate(150, 34)" class="transition-transform duration-700">
                        <ellipse cx="0" cy="4" rx="4" ry="3" fill="#fef08a"/>
                        <line x1="0" y1="6" x2="0" y2="22" stroke="#e2e8f0" stroke-width="1.5"/>
                    </g>
                    <!-- Burner flame at free end -->
                    <g id="sim1BurnerFlame" transform="translate(60, 50)" opacity="0" class="transition-opacity duration-300">
                        <polygon points="0,0 8,-20 16,0" fill="#f97316"/>
                        <polygon points="4,0 8,-12 12,0" fill="#facc15"/>
                    </g>
                    <!-- Burner base -->
                    <rect x="62" y="55" width="12" height="35" fill="#64748b"/>
                </svg>
                <button onclick="heatThermalWire()" class="mt-2 px-3 py-1 rounded bg-orange-600/30 hover:bg-orange-600/50 text-orange-200 border border-orange-500/40 text-xs font-bold">Apply Flame</button>
                <p id="sim1ThermalMsg" class="text-[11px] text-slate-400 mt-1">Heat conducts along wire, melting wax so the pin drops (Ag & Cu best; Pb & Hg poor).</p>
            </div>

            <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-emerald-400 block mb-1">Activity 3.6: Electrical Circuit Test</span>
                <svg viewBox="0 0 200 110" class="w-full h-24 mx-auto">
                    <!-- Battery -->
                    <rect x="30" y="25" width="25" height="15" fill="#334155" stroke="#64748b"/>
                    <text x="42" y="36" font-size="8" fill="#fff" text-anchor="middle">Cell</text>
                    <!-- Bulb -->
                    <circle id="sim1BulbGlow" cx="160" cy="32" r="14" fill="#fbbf24" opacity="0.1" class="transition-opacity duration-300"/>
                    <circle id="sim1Bulb" cx="160" cy="32" r="8" fill="#475569" stroke="#94a3b8" class="transition-colors duration-300"/>
                    <!-- Test clips & wire -->
                    <polyline points="55,32 100,32" stroke="#38bdf8" stroke-width="2"/>
                    <polyline points="120,32 160,32" stroke="#38bdf8" stroke-width="2"/>
                    <polyline points="160,40 160,85 30,85 30,40" stroke="#38bdf8" stroke-width="2" fill="none"/>
                    <!-- Test material bridge between 100,32 and 120,32 -->
                    <line id="sim1TestClip" x1="100" y1="32" x2="120" y2="32" stroke="#475569" stroke-width="4" stroke-dasharray="2 2" class="transition-all duration-300"/>
                    <text id="sim1ClipText" x="110" y="24" font-size="8" fill="#94a3b8" text-anchor="middle">Open Clip</text>
                </svg>
                <div class="flex justify-center gap-1.5 mt-2">
                    <button onclick="testCircuit('copper')" class="px-2 py-1 rounded bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-200 border border-emerald-500/40 text-[11px] font-bold">Copper Wire</button>
                    <button onclick="testCircuit('pvc')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] font-bold">PVC Plastic</button>
                    <button onclick="testCircuit('graphite')" class="px-2 py-1 rounded bg-indigo-600/30 hover:bg-indigo-600/50 text-indigo-200 border border-indigo-500/40 text-[11px] font-bold">Graphite</button>
                </div>
                <p id="sim1CircuitMsg" class="text-[11px] text-slate-400 mt-1">Metals conduct current (bulb glows); PVC is an insulator to prevent shock.</p>
            </div>
        </div>
    </div>
</div>
''',

    2: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Physical Exceptions: Metals & Non-metals</h4>
        <div class="flex gap-1 text-xs">
            <button onclick="setSim2Tab('mercury')" id="sim2TabHg" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Liquid Br2 & Hg</button>
            <button onclick="setSim2Tab('palmMelt')" id="sim2TabPalm" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Ga / Cs on Palm</button>
            <button onclick="setSim2Tab('allotropes')" id="sim2TabAllo" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Diamond vs Graphite</button>
        </div>
    </div>

    <!-- Tab 1: Bromine & Mercury -->
    <div id="sim2ViewHg" class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center">
            <span class="text-xs font-bold text-red-400 block mb-1">Bromine (Br2): Liquid Non-metal</span>
            <svg viewBox="0 0 160 110" class="w-full h-24 mx-auto">
                <!-- Sealed flask -->
                <path d="M 65 20 L 95 20 L 95 40 L 125 90 L 35 90 L 65 40 Z" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
                <!-- Liquid Bromine -->
                <path d="M 45 88 L 115 88 L 105 70 L 55 70 Z" fill="#b91c1c" class="transition-all duration-500"/>
                <!-- Red-brown vapor -->
                <ellipse cx="80" cy="50" rx="25" ry="15" fill="#ef4444" fill-opacity="0.25"/>
                <text x="80" y="82" font-size="8" fill="#fecaca" text-anchor="middle" font-weight="bold">Liquid Br2</text>
            </svg>
            <p class="text-[11px] text-slate-300 mt-1">Bromine is the <strong>only non-metal</strong> that is liquid at standard room temperature.</p>
        </div>

        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center">
            <span class="text-xs font-bold text-cyan-300 block mb-1">Mercury (Hg): Liquid Metal</span>
            <svg viewBox="0 0 160 110" class="w-full h-24 mx-auto">
                <!-- Thermometer capillary -->
                <rect x="72" y="15" width="16" height="65" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
                <circle cx="80" cy="85" r="14" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
                <!-- Liquid Mercury bead with convex meniscus -->
                <circle cx="80" cy="85" r="11" fill="#cbd5e1"/>
                <rect x="77" y="45" width="6" height="40" fill="#cbd5e1"/>
                <path d="M 77 45 Q 80 42 83 45" fill="#cbd5e1"/>
                <text x="80" y="88" font-size="8" fill="#0f172a" text-anchor="middle" font-weight="bold">Hg (l)</text>
            </svg>
            <p class="text-[11px] text-slate-300 mt-1">Mercury is the <strong>only metal</strong> that exists in liquid form at room temperature.</p>
        </div>
    </div>

    <!-- Tab 2: Gallium / Caesium melting on palm -->
    <div id="sim2ViewPalm" class="hidden space-y-3">
        <div class="p-4 bg-slate-950/70 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-center justify-around gap-4">
            <svg viewBox="0 0 220 130" class="w-56 h-32">
                <!-- Human hand silhouette -->
                <path d="M 30 110 C 30 80, 50 60, 80 60 C 90 60, 100 40, 110 40 C 120 40, 125 55, 135 45 C 145 35, 155 45, 160 55 C 165 65, 175 60, 185 70 C 190 75, 180 95, 170 105 C 150 120, 100 120, 30 110 Z" fill="#d97706" fill-opacity="0.25" stroke="#f59e0b" stroke-width="1.5"/>
                <!-- Palm temperature label -->
                <text x="110" y="115" font-size="9" fill="#fcd34d" text-anchor="middle">Body Temp: ~37°C (310 K)</text>
                <!-- Metal cube on palm -->
                <rect id="sim2GaCube" x="95" y="65" width="22" height="18" rx="2" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1.5" class="transition-all duration-1000"/>
                <!-- Melted liquid puddle -->
                <ellipse id="sim2GaPuddle" cx="106" cy="78" rx="22" ry="7" fill="#cbd5e1" opacity="0" class="transition-opacity duration-1000"/>
            </svg>
            <div class="text-center sm:text-left space-y-2">
                <span class="text-xs font-bold text-amber-300">Gallium (mp 302.8 K / 29.8°C) & Caesium (mp 301.6 K / 28.6°C)</span>
                <p class="text-xs text-slate-300">These metals have such low melting points that resting them on the palm supplies enough heat to melt them into shiny liquid puddles.</p>
                <div class="flex gap-2">
                    <button onclick="meltOnPalm()" class="px-3 py-1.5 rounded bg-amber-600/30 hover:bg-amber-600/50 text-amber-200 border border-amber-500/40 text-xs font-bold">Rest on Palm</button>
                    <button onclick="resetPalm()" class="px-2.5 py-1.5 rounded bg-slate-800 text-slate-400 hover:text-slate-200 text-xs">Reset</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Tab 3: Allotropes of Carbon & Iodine -->
    <div id="sim2ViewAllo" class="hidden grid grid-cols-1 sm:grid-cols-3 gap-2 text-center text-xs">
        <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
            <span class="font-bold text-cyan-300 block mb-1">Diamond</span>
            <svg viewBox="0 0 100 70" class="w-full h-16 mx-auto">
                <polygon points="50,10 75,30 50,60 25,30" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
                <line x1="25" y1="30" x2="75" y2="30" stroke="#38bdf8" stroke-width="1"/>
                <line x1="50" y1="10" x2="50" y2="60" stroke="#38bdf8" stroke-width="1"/>
            </svg>
            <p class="text-[11px] text-slate-400">Hardest known natural substance; high mp/bp; electrical insulator.</p>
        </div>
        <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
            <span class="font-bold text-indigo-300 block mb-1">Graphite</span>
            <svg viewBox="0 0 100 70" class="w-full h-16 mx-auto">
                <polygon points="20,20 40,15 60,20 70,30 50,35 30,30" fill="none" stroke="#818cf8" stroke-width="1.5"/>
                <polygon points="20,45 40,40 60,45 70,55 50,60 30,55" fill="none" stroke="#818cf8" stroke-width="1.5"/>
            </svg>
            <p class="text-[11px] text-slate-400">Hexagonal layers; delocalised electrons conduct electricity!</p>
        </div>
        <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
            <span class="font-bold text-purple-300 block mb-1">Iodine (I2)</span>
            <svg viewBox="0 0 100 70" class="w-full h-16 mx-auto">
                <polygon points="40,25 60,20 75,40 55,55 30,45" fill="#a855f7" stroke="#e9d5ff" stroke-width="1.5"/>
                <path d="M 68 28 L 72 34 L 70 40" stroke="#fff" stroke-width="1"/>
            </svg>
            <p class="text-[11px] text-slate-400">Non-metal exception: exhibits gleaming metallic lustre.</p>
        </div>
    </div>
</div>
''',

    3: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 3.8: Combustion & Oxide Litmus Testing</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="burnMetal('mg')" id="sim3BtnMg" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Burn Magnesium (Metal)</button>
            <button onclick="burnMetal('s')" id="sim3BtnS" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Burn Sulphur (Non-metal)</button>
            <button onclick="burnMetal('cu')" id="sim3BtnCu" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Heat Copper</button>
        </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center">
        <!-- Combustion stage SVG -->
        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center">
            <span id="sim3StageTitle" class="text-xs font-bold text-amber-300 block mb-1">Combustion in Air</span>
            <svg viewBox="0 0 200 120" class="w-full h-28 mx-auto">
                <!-- Tongs holding sample -->
                <path d="M 40 20 Q 70 30 100 45" stroke="#94a3b8" stroke-width="3" fill="none"/>
                <path d="M 40 30 Q 70 38 100 48" stroke="#94a3b8" stroke-width="3" fill="none"/>
                <!-- Sample (Magnesium ribbon / sulphur) -->
                <rect id="sim3Sample" x="98" y="42" width="25" height="6" fill="#cbd5e1" rx="1" class="transition-all duration-700"/>
                <!-- Burner Flame -->
                <g id="sim3Flame" transform="translate(100, 50)" opacity="0" class="transition-opacity duration-300">
                    <polygon points="5,0 12,-25 19,0" fill="#f97316"/>
                    <polygon points="8,0 12,-15 16,0" fill="#fef08a"/>
                </g>
                <rect x="105" y="55" width="14" height="40" fill="#475569"/>
                <!-- Watch glass with ash -->
                <path d="M 120 100 Q 150 115 180 100" stroke="#64748b" stroke-width="2" fill="none"/>
                <ellipse id="sim3Ash" cx="150" cy="103" rx="12" ry="4" fill="#f8fafc" opacity="0" class="transition-opacity duration-500"/>
            </svg>
            <p id="sim3CombustText" class="text-xs text-slate-300 mt-1">Select an element above to ignite in atmospheric oxygen.</p>
        </div>

        <!-- Oxide Litmus Solution Test -->
        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
            <span class="text-xs font-bold text-emerald-400 block">Dissolving Product in Water & Litmus Test</span>
            <svg viewBox="0 0 180 90" class="w-full h-20 mx-auto">
                <!-- Beaker with water -->
                <rect x="50" y="20" width="80" height="60" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
                <rect id="sim3SolWater" x="52" y="38" width="76" height="40" fill="#38bdf8" fill-opacity="0.2" class="transition-colors duration-700"/>
                <!-- Litmus Paper strip dipping -->
                <rect id="sim3LitmusStrip" x="80" y="10" width="20" height="50" rx="2" fill="#ef4444" class="transition-colors duration-700"/>
            </svg>
            <button onclick="testOxideLitmus()" id="sim3LitmusBtn" disabled class="px-3 py-1 rounded bg-slate-800 text-slate-500 text-xs font-bold">Dip Litmus Paper</button>
            <p id="sim3LitmusResult" class="text-[11px] text-slate-400">Metal oxides are basic; non-metal oxides are acidic.</p>
        </div>
    </div>
</div>
''',

    4: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Amphoteric Oxides & Anodising Chamber</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim4Tab('ampho')" id="sim4TabAmpho" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Al2O3 Amphoteric Nature</button>
            <button onclick="setSim4Tab('anodise')" id="sim4TabAnod" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Electrolytic Anodising</button>
        </div>
    </div>

    <!-- Tab 1: Amphoteric Reactions -->
    <div id="sim4ViewAmpho" class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-center">
        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <span class="text-xs font-bold text-rose-400 block mb-1">Reaction with Acid: Dilute HCl</span>
            <svg viewBox="0 0 160 100" class="w-full h-20 mx-auto">
                <rect x="60" y="20" width="40" height="70" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
                <rect id="sim4AcidLiquid" x="62" y="45" width="36" height="43" fill="#f43f5e" fill-opacity="0.25"/>
                <!-- Al2O3 powder -->
                <circle id="sim4Al2O3Acid" cx="80" cy="78" r="6" fill="#f8fafc" class="transition-all duration-700"/>
            </svg>
            <button onclick="reactAmpho('acid')" class="mt-2 px-3 py-1 rounded bg-rose-600/30 hover:bg-rose-600/50 text-rose-200 border border-rose-500/40 text-xs font-bold">Add Dilute HCl</button>
            <p id="sim4AcidMsg" class="text-[11px] text-slate-400 mt-1">Al2O3 + 6HCl → 2AlCl3 + 3H2O (Acts as Base)</p>
        </div>

        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <span class="text-xs font-bold text-cyan-400 block mb-1">Reaction with Base: Aqueous NaOH</span>
            <svg viewBox="0 0 160 100" class="w-full h-20 mx-auto">
                <rect x="60" y="20" width="40" height="70" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
                <rect id="sim4BaseLiquid" x="62" y="45" width="36" height="43" fill="#06b6d4" fill-opacity="0.25"/>
                <!-- Al2O3 powder -->
                <circle id="sim4Al2O3Base" cx="80" cy="78" r="6" fill="#f8fafc" class="transition-all duration-700"/>
            </svg>
            <button onclick="reactAmpho('base')" class="mt-2 px-3 py-1 rounded bg-cyan-600/30 hover:bg-cyan-600/50 text-cyan-200 border border-cyan-500/40 text-xs font-bold">Add Aqueous NaOH</button>
            <p id="sim4BaseMsg" class="text-[11px] text-slate-400 mt-1">Al2O3 + 2NaOH → 2NaAlO2 + H2O (Acts as Acid)</p>
        </div>
    </div>

    <!-- Tab 2: Anodising Cell -->
    <div id="sim4ViewAnodise" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2">
        <span class="text-xs font-bold text-indigo-300 block text-center">Electrolytic Anodising: Thickening Al2O3 Layer with Dilute H2SO4</span>
        <svg viewBox="0 0 240 110" class="w-full h-24 mx-auto">
            <!-- Tank -->
            <rect x="40" y="25" width="160" height="75" rx="4" fill="#0f172a" stroke="#475569" stroke-width="2"/>
            <rect x="42" y="40" width="156" height="58" fill="#38bdf8" fill-opacity="0.15"/>
            <!-- Anode: Aluminium Article -->
            <rect id="sim4AlAnode" x="70" y="20" width="18" height="60" fill="#94a3b8" stroke="#38bdf8" stroke-width="2"/>
            <rect id="sim4OxideLayer" x="67" y="17" width="24" height="66" fill="none" stroke="#f59e0b" stroke-width="0" stroke-dasharray="2 2" class="transition-all duration-700"/>
            <text x="79" y="93" font-size="8" fill="#38bdf8" font-weight="bold" text-anchor="middle">Al Anode (+)</text>
            <!-- Cathode: Lead / Platinum -->
            <rect x="150" y="20" width="14" height="60" fill="#64748b"/>
            <text x="157" y="93" font-size="8" fill="#94a3b8" text-anchor="middle">Cathode (-)</text>
            <!-- Battery connection wire -->
            <path d="M 79 20 L 79 10 L 110 10" stroke="#ef4444" stroke-width="2" fill="none"/>
            <path d="M 157 20 L 157 10 L 130 10" stroke="#3b82f6" stroke-width="2" fill="none"/>
            <circle cx="120" cy="10" r="6" fill="#eab308"/>
        </svg>
        <div class="flex justify-center gap-2">
            <button onclick="startAnodising()" class="px-3 py-1 rounded bg-indigo-600/30 hover:bg-indigo-600/50 text-indigo-200 border border-indigo-500/40 text-xs font-bold">Apply Electric Current</button>
            <button onclick="dyeAnodised()" id="sim4DyeBtn" disabled class="px-3 py-1 rounded bg-slate-800 text-slate-500 text-xs font-bold">Add Color Dye</button>
        </div>
        <p id="sim4AnodiseMsg" class="text-[11px] text-center text-slate-400">Oxygen evolved at anode reacts with Al to form a dense, corrosion-resistant oxide layer.</p>
    </div>
</div>
''',

    5: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 3.10: Metals Reacting with Water & Steam</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim5Mode('cold')" id="sim5BtnCold" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Cold Water</button>
            <button onclick="setSim5Mode('hot')" id="sim5BtnHot" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Hot Water (Mg)</button>
            <button onclick="setSim5Mode('steam')" id="sim5BtnSteam" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Steam (Fe / Al)</button>
        </div>
    </div>

    <!-- Cold Water View -->
    <div id="sim5ColdView" class="space-y-3">
        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-center justify-around gap-3">
            <svg viewBox="0 0 180 120" class="w-48 h-28">
                <!-- Water trough -->
                <path d="M 20 50 Q 20 110 90 110 Q 160 110 160 50" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
                <path d="M 24 60 Q 90 65 156 60 Q 156 106 90 106 Q 24 106 24 60" fill="#38bdf8" fill-opacity="0.25"/>
                <!-- Metal sample -->
                <circle id="sim5Sample" cx="90" cy="80" r="8" fill="#cbd5e1" class="transition-all duration-700"/>
                <!-- Fire / bubbles -->
                <g id="sim5Vigor" opacity="0" class="transition-opacity duration-300">
                    <polygon points="85,65 90,45 95,65" fill="#facc15"/>
                    <circle cx="85" cy="72" r="3" fill="#e0f2fe"/>
                    <circle cx="95" cy="70" r="2.5" fill="#e0f2fe"/>
                </g>
            </svg>
            <div class="space-y-2 text-center sm:text-left">
                <span class="text-xs font-bold text-sky-300 block">Select Metal to Drop into Cold Water:</span>
                <div class="flex flex-wrap gap-1.5 justify-center sm:justify-start">
                    <button onclick="testWater('na')" class="px-2.5 py-1 rounded bg-amber-600/30 hover:bg-amber-600/50 text-amber-200 border border-amber-500/40 text-xs font-bold">Sodium (Na)</button>
                    <button onclick="testWater('ca')" class="px-2.5 py-1 rounded bg-sky-600/30 hover:bg-sky-600/50 text-sky-200 border border-sky-500/40 text-xs font-bold">Calcium (Ca)</button>
                    <button onclick="testWater('cu')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold">Copper (Cu)</button>
                </div>
                <p id="sim5ColdMsg" class="text-[11px] text-slate-300">Na/K dart and ignite immediately. Ca sinks then floats with H2 bubbles. Cu is inert.</p>
            </div>
        </div>
    </div>

    <!-- Hot Water View -->
    <div id="sim5HotView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-amber-300 block">Magnesium with Hot Water</span>
        <svg viewBox="0 0 160 100" class="w-44 h-24 mx-auto">
            <rect x="50" y="20" width="60" height="75" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
            <rect x="52" y="45" width="56" height="48" fill="#f97316" fill-opacity="0.2"/>
            <!-- Steam wisps -->
            <path d="M 65 35 Q 70 25 65 15" stroke="#fed7aa" stroke-width="1.5" fill="none"/>
            <path d="M 85 35 Q 90 25 85 15" stroke="#fed7aa" stroke-width="1.5" fill="none"/>
            <!-- Mg ribbon floating -->
            <rect id="sim5MgPiece" x="70" y="80" width="20" height="5" rx="1" fill="#cbd5e1" class="transition-all duration-700"/>
        </svg>
        <button onclick="reactMgHot()" class="px-3 py-1 rounded bg-amber-600/30 hover:bg-amber-600/50 text-amber-200 border border-amber-500/40 text-xs font-bold">Heat Water with Magnesium</button>
        <p id="sim5HotMsg" class="text-[11px] text-slate-400">Mg does not react with cold water; reacts with hot water and floats as H2 bubbles stick.</p>
    </div>

    <!-- Steam Apparatus View -->
    <div id="sim5SteamView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2">
        <span class="text-xs font-bold text-cyan-300 block text-center">Action of Steam on Iron (3Fe + 4H2O(g) → Fe3O4 + 4H2)</span>
        <svg viewBox="0 0 240 100" class="w-full h-24 mx-auto">
            <!-- Glass boiling tube -->
            <rect x="20" y="35" width="110" height="18" rx="2" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
            <!-- Wet glass wool -->
            <circle cx="35" cy="44" r="7" fill="#64748b"/>
            <text x="35" y="30" font-size="7" fill="#94a3b8" text-anchor="middle">Wet Wool</text>
            <!-- Metal sample (iron coil) -->
            <rect id="sim5SteamFe" x="90" y="40" width="25" height="8" rx="1" fill="#475569" stroke="#94a3b8"/>
            <text x="102" y="30" font-size="7" fill="#cbd5e1" text-anchor="middle">Fe Sample</text>
            <!-- Delivery tube to water trough -->
            <path d="M 130 44 L 170 44 L 170 75 L 195 75" stroke="#94a3b8" stroke-width="2" fill="none"/>
            <!-- Water trough with inverted test tube -->
            <rect x="180" y="60" width="45" height="35" rx="3" fill="#0f172a" stroke="#64748b"/>
            <rect x="190" y="40" width="16" height="50" rx="2" fill="#38bdf8" fill-opacity="0.3" stroke="#94a3b8"/>
            <!-- Gas collection bubbles -->
            <g id="sim5SteamBubbles" opacity="0" class="transition-opacity duration-500">
                <circle cx="198" cy="50" r="3" fill="#e0f2fe"/>
                <circle cx="198" cy="60" r="2.5" fill="#e0f2fe"/>
            </g>
        </svg>
        <div class="flex justify-center">
            <button onclick="passSteam()" class="px-3 py-1 rounded bg-cyan-600/30 hover:bg-cyan-600/50 text-cyan-200 border border-cyan-500/40 text-xs font-bold">Pass Steam over Heated Iron</button>
        </div>
        <p id="sim5SteamMsg" class="text-[11px] text-center text-slate-400">Iron reacts with steam to form black magnetic oxide (Fe3O4) and hydrogen gas.</p>
    </div>
</div>
''',

    6: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Metals with Acids & Aqua Regia</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim6Tab('hcl')" id="sim6TabHCl" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">HCl Reactivity Order</button>
            <button onclick="setSim6Tab('aqua')" id="sim6TabAqua" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Aqua Regia Gold Test</button>
        </div>
    </div>

    <!-- HCl Reactivity Order View -->
    <div id="sim6HClView" class="space-y-3">
        <div class="grid grid-cols-4 gap-2 text-center">
            <div class="p-2 bg-slate-950/70 rounded-xl border border-slate-800">
                <span class="text-xs font-bold text-emerald-400">Magnesium</span>
                <svg viewBox="0 0 60 90" class="w-full h-20 mx-auto">
                    <rect x="15" y="15" width="30" height="70" rx="4" fill="#0f172a" stroke="#64748b"/>
                    <rect x="17" y="35" width="26" height="48" fill="#38bdf8" fill-opacity="0.2"/>
                    <circle id="sim6B1" cx="30" cy="50" r="3" fill="#e0f2fe" opacity="0"/>
                    <circle id="sim6B2" cx="25" cy="65" r="2.5" fill="#e0f2fe" opacity="0"/>
                </svg>
                <span class="text-[10px] text-emerald-300 font-semibold">Vigorous (Mg)</span>
            </div>
            <div class="p-2 bg-slate-950/70 rounded-xl border border-slate-800">
                <span class="text-xs font-bold text-sky-400">Aluminium</span>
                <svg viewBox="0 0 60 90" class="w-full h-20 mx-auto">
                    <rect x="15" y="15" width="30" height="70" rx="4" fill="#0f172a" stroke="#64748b"/>
                    <rect x="17" y="35" width="26" height="48" fill="#38bdf8" fill-opacity="0.2"/>
                    <circle id="sim6B3" cx="30" cy="55" r="2.5" fill="#e0f2fe" opacity="0"/>
                </svg>
                <span class="text-[10px] text-sky-300 font-semibold">Rapid (Al)</span>
            </div>
            <div class="p-2 bg-slate-950/70 rounded-xl border border-slate-800">
                <span class="text-xs font-bold text-amber-400">Zinc</span>
                <svg viewBox="0 0 60 90" class="w-full h-20 mx-auto">
                    <rect x="15" y="15" width="30" height="70" rx="4" fill="#0f172a" stroke="#64748b"/>
                    <rect x="17" y="35" width="26" height="48" fill="#38bdf8" fill-opacity="0.2"/>
                    <circle id="sim6B4" cx="30" cy="65" r="2" fill="#e0f2fe" opacity="0"/>
                </svg>
                <span class="text-[10px] text-amber-300 font-semibold">Moderate (Zn)</span>
            </div>
            <div class="p-2 bg-slate-950/70 rounded-xl border border-slate-800">
                <span class="text-xs font-bold text-rose-400">Copper</span>
                <svg viewBox="0 0 60 90" class="w-full h-20 mx-auto">
                    <rect x="15" y="15" width="30" height="70" rx="4" fill="#0f172a" stroke="#64748b"/>
                    <rect x="17" y="35" width="26" height="48" fill="#38bdf8" fill-opacity="0.2"/>
                </svg>
                <span class="text-[10px] text-rose-300 font-semibold">No reaction (Cu)</span>
            </div>
        </div>
        <div class="flex justify-center gap-2">
            <button onclick="startAcidBubbles()" class="px-3 py-1 rounded bg-amber-600/30 hover:bg-amber-600/50 text-amber-200 border border-amber-500/40 text-xs font-bold">Add Dilute HCl to All Tubes</button>
        </div>
        <p class="text-[11px] text-center text-slate-400">Reactivity order with dilute acid: <strong>Mg > Al > Zn > Fe > Cu (inert)</strong>.</p>
    </div>

    <!-- Aqua Regia View -->
    <div id="sim6AquaView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-yellow-300 block">Aqua Regia (3 HCl : 1 HNO3) Dissolving Pure Gold</span>
        <svg viewBox="0 0 160 100" class="w-44 h-24 mx-auto">
            <rect x="55" y="15" width="50" height="75" rx="5" fill="#0f172a" stroke="#64748b"/>
            <!-- Fuming liquid -->
            <rect id="sim6AquaLiquid" x="57" y="40" width="46" height="48" fill="#eab308" fill-opacity="0.4" class="transition-colors duration-700"/>
            <!-- Gold leaf dissolving -->
            <polygon id="sim6GoldLeaf" points="75,60 85,55 90,68 78,72" fill="#fbbf24" stroke="#d97706" class="transition-all duration-1000"/>
        </svg>
        <button onclick="dissolveGold()" class="px-3 py-1 rounded bg-yellow-600/30 hover:bg-yellow-600/50 text-yellow-200 border border-yellow-500/40 text-xs font-bold">Drop Gold Leaf into Aqua Regia</button>
        <p id="sim6AquaMsg" class="text-[11px] text-slate-400">Neither conc. HCl nor HNO3 alone dissolves gold, but fresh 3:1 Aqua Regia forms soluble HAuCl4.</p>
    </div>
</div>
''',

    7: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 3.12: Metal Salt Displacement</h4>
        <span class="text-xs text-slate-400 font-mono">Fe + CuSO4 → FeSO4 + Cu</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-center">
        <!-- Test Tube A: Fe in CuSO4 -->
        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2">
            <span class="text-xs font-bold text-sky-400 block">Tube A: Iron Nail in Blue CuSO4</span>
            <svg viewBox="0 0 140 120" class="w-full h-28 mx-auto">
                <rect x="50" y="15" width="40" height="95" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
                <!-- Solution (starts blue, turns green) -->
                <rect id="sim7SolutionA" x="52" y="45" width="36" height="63" fill="#0284c7" fill-opacity="0.4" class="transition-colors duration-1000"/>
                <!-- Iron nail suspended by thread -->
                <line x1="70" y1="15" x2="70" y2="50" stroke="#94a3b8" stroke-width="1"/>
                <polygon id="sim7NailA" points="68,50 72,50 72,90 70,98 68,90" fill="#94a3b8" stroke="#475569" class="transition-colors duration-1000"/>
            </svg>
            <button onclick="runDisplacementA()" class="px-3 py-1 rounded bg-sky-600/30 hover:bg-sky-600/50 text-sky-200 border border-sky-500/40 text-xs font-bold">Immerse 20 Minutes</button>
            <p id="sim7MsgA" class="text-[11px] text-slate-400">Blue CuSO4 turns pale green FeSO4; brown Cu deposits on iron nail.</p>
        </div>

        <!-- Test Tube B: Cu in FeSO4 -->
        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2">
            <span class="text-xs font-bold text-emerald-400 block">Tube B: Copper Wire in Pale Green FeSO4</span>
            <svg viewBox="0 0 140 120" class="w-full h-28 mx-auto">
                <rect x="50" y="15" width="40" height="95" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
                <!-- Solution (green FeSO4) -->
                <rect id="sim7SolutionB" x="52" y="45" width="36" height="63" fill="#10b981" fill-opacity="0.25"/>
                <!-- Copper wire coiled -->
                <line x1="70" y1="15" x2="70" y2="50" stroke="#94a3b8" stroke-width="1"/>
                <path d="M 68 50 Q 75 60 68 70 Q 75 80 68 90" stroke="#f97316" stroke-width="2.5" fill="none"/>
            </svg>
            <button onclick="runDisplacementB()" class="px-3 py-1 rounded bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-200 border border-emerald-500/40 text-xs font-bold">Immerse 20 Minutes</button>
            <p id="sim7MsgB" class="text-[11px] text-slate-400">No reaction occurs! Copper is less reactive than iron and cannot displace it.</p>
        </div>
    </div>
</div>
''',

    8: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Reactivity Series Ladder & Metal Duel</h4>
        <span class="text-xs text-amber-300 font-mono">K > Na > Ca > Mg > Al > Zn > Fe > Pb > [H] > Cu > Hg > Ag > Au</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <!-- Interactive Ladder -->
        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-1">
            <span class="text-xs font-bold text-sky-400 block mb-1">Reactivity Ranking:</span>
            <div class="space-y-1 text-xs">
                <div class="flex items-center justify-between p-1 bg-rose-500/10 border-l-2 border-rose-500 rounded px-2">
                    <span class="font-bold text-rose-300">K, Na, Ca, Mg, Al</span>
                    <span class="text-[10px] text-rose-400">Most Reactive (Molten Electrolysis)</span>
                </div>
                <div class="flex items-center justify-between p-1 bg-amber-500/10 border-l-2 border-amber-500 rounded px-2">
                    <span class="font-bold text-amber-300">Zn, Fe, Pb</span>
                    <span class="text-[10px] text-amber-400">Moderate (Carbon Reduction)</span>
                </div>
                <div class="flex items-center justify-between p-1 bg-slate-700/30 border-l-2 border-slate-400 rounded px-2">
                    <span class="font-bold text-slate-300">[Hydrogen]</span>
                    <span class="text-[10px] text-slate-400">Reference Benchmark (E° = 0)</span>
                </div>
                <div class="flex items-center justify-between p-1 bg-emerald-500/10 border-l-2 border-emerald-500 rounded px-2">
                    <span class="font-bold text-emerald-300">Cu, Hg, Ag, Au</span>
                    <span class="text-[10px] text-emerald-400">Least Reactive (Native / Thermal)</span>
                </div>
            </div>
        </div>

        <!-- Metal Duel Simulator -->
        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
            <span class="text-xs font-bold text-amber-300 block">Displacement Duel Tester</span>
            <div class="flex justify-center items-center gap-2 text-xs">
                <div>
                    <label class="block text-[10px] text-slate-400 mb-0.5">Free Metal A:</label>
                    <select id="sim8MetalA" class="bg-slate-900 border border-slate-700 rounded px-2 py-1 text-xs text-amber-300">
                        <option value="10">Potassium (K)</option>
                        <option value="8">Magnesium (Mg)</option>
                        <option value="6" selected>Zinc (Zn)</option>
                        <option value="5">Iron (Fe)</option>
                        <option value="3">Copper (Cu)</option>
                        <option value="1">Silver (Ag)</option>
                    </select>
                </div>
                <span class="text-sm font-bold text-slate-500">vs</span>
                <div>
                    <label class="block text-[10px] text-slate-400 mb-0.5">Salt Solution B:</label>
                    <select id="sim8SaltB" class="bg-slate-900 border border-slate-700 rounded px-2 py-1 text-xs text-sky-300">
                        <option value="10">Potassium Salt</option>
                        <option value="8">Magnesium Salt</option>
                        <option value="6">Zinc Salt</option>
                        <option value="5">Iron Salt</option>
                        <option value="3" selected>Copper Salt</option>
                        <option value="1">Silver Salt</option>
                    </select>
                </div>
            </div>
            <button onclick="testDuel()" class="px-3 py-1 rounded bg-amber-600/30 hover:bg-amber-600/50 text-amber-200 border border-amber-500/40 text-xs font-bold">Simulate Reaction</button>
            <div id="sim8DuelOutcome" class="p-2 bg-slate-900/90 rounded border border-slate-800 text-xs text-emerald-400">
                Select metals and click 'Simulate Reaction'.
            </div>
        </div>
    </div>
</div>
'''
}
