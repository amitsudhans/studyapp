"""Interactive Simulators 9 to 16 for Class 10 Science Chapter 3: Metals and Non-metals
High-fidelity, responsive, SVG-based laboratory simulators with Tailwind CSS.
"""

simulators = {
    9: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Ionic Bond Formation: Electron Dot Transfer</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim9Compound('nacl')" id="sim9BtnNaCl" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Sodium Chloride (NaCl)</button>
            <button onclick="setSim9Compound('mgcl2')" id="sim9BtnMgCl2" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Magnesium Chloride (MgCl2)</button>
        </div>
    </div>

    <!-- NaCl view -->
    <div id="sim9NaClView" class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-3">
        <div class="flex flex-col sm:flex-row items-center justify-around gap-4">
            <!-- Sodium Atom / Ion -->
            <div class="text-center">
                <span class="text-xs font-bold text-amber-300 block mb-1">Sodium: Na (2,8,1)</span>
                <svg viewBox="0 0 110 110" class="w-24 h-24 mx-auto">
                    <circle cx="55" cy="55" r="48" fill="none" stroke="#475569" stroke-dasharray="2 2"/>
                    <circle cx="55" cy="55" r="34" fill="none" stroke="#475569" stroke-dasharray="2 2"/>
                    <circle cx="55" cy="55" r="20" fill="none" stroke="#475569" stroke-dasharray="2 2"/>
                    <circle cx="55" cy="55" r="12" fill="#d97706"/>
                    <text x="55" y="58" font-size="8" fill="#fff" font-weight="bold" text-anchor="middle">11p+</text>
                    <!-- Valence electron -->
                    <circle id="sim9NaValence" cx="55" cy="7" r="4" fill="#fbbf24" class="transition-all duration-1000"/>
                </svg>
                <span id="sim9NaState" class="text-[11px] text-slate-300 font-mono">Na Atom (2,8,1)</span>
            </div>

            <!-- Transfer Arrow & Action -->
            <div class="text-center space-y-2">
                <button onclick="transferElectronNaCl()" class="px-3 py-1.5 rounded bg-amber-600/30 hover:bg-amber-600/50 text-amber-200 border border-amber-500/40 text-xs font-bold">Transfer 1 Electron →</button>
                <div class="text-[11px] text-slate-400">Na loses 1e⁻ → Na⁺ (2,8)<br>Cl gains 1e⁻ → Cl⁻ (2,8,8)</div>
                <button onclick="resetSim9()" class="text-[10px] text-slate-500 hover:text-slate-300 underline">Reset</button>
            </div>

            <!-- Chlorine Atom / Ion -->
            <div class="text-center">
                <span class="text-xs font-bold text-emerald-400 block mb-1">Chlorine: Cl (2,8,7)</span>
                <svg viewBox="0 0 110 110" class="w-24 h-24 mx-auto">
                    <circle cx="55" cy="55" r="48" fill="none" stroke="#475569" stroke-dasharray="2 2"/>
                    <circle cx="55" cy="55" r="34" fill="none" stroke="#475569" stroke-dasharray="2 2"/>
                    <circle cx="55" cy="55" r="20" fill="none" stroke="#475569" stroke-dasharray="2 2"/>
                    <circle cx="55" cy="55" r="12" fill="#059669"/>
                    <text x="55" y="58" font-size="8" fill="#fff" font-weight="bold" text-anchor="middle">17p+</text>
                    <!-- Target octet spot -->
                    <circle id="sim9ClHole" cx="55" cy="7" r="4" fill="none" stroke="#34d399" stroke-width="1.5" stroke-dasharray="1 1"/>
                </svg>
                <span id="sim9ClState" class="text-[11px] text-slate-300 font-mono">Cl Atom (2,8,7)</span>
            </div>
        </div>
        <p id="sim9Msg" class="text-xs text-center text-amber-300">Complete transfer of valence electrons yields stable noble gas octets and powerful electrostatic attraction.</p>
    </div>

    <!-- MgCl2 view -->
    <div id="sim9MgCl2View" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-sky-300 block">Formation of Magnesium Chloride (MgCl2)</span>
        <div class="flex items-center justify-center gap-4 text-xs font-mono">
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="text-amber-400 font-bold block">Mg (2,8,2)</span>
                <span class="text-[10px] text-slate-400">Loses 2e⁻ → Mg²⁺ (2,8)</span>
            </div>
            <span class="text-xl text-slate-500">+</span>
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="text-emerald-400 font-bold block">2 × Cl (2,8,7)</span>
                <span class="text-[10px] text-slate-400">Each gains 1e⁻ → 2 Cl⁻ (2,8,8)</span>
            </div>
            <span class="text-xl text-slate-500">=</span>
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="text-cyan-300 font-bold block">[Mg²⁺] [Cl⁻]₂</span>
                <span class="text-[10px] text-slate-400">Ionic Compound MgCl2</span>
            </div>
        </div>
        <p class="text-[11px] text-slate-400">Divalent magnesium requires two monovalent chlorine atoms to achieve mutual octet electrical neutrality.</p>
    </div>
</div>
''',

    10: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 3.13: Properties of Ionic Compounds</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim10Mode('brittle')" id="sim10BtnBrittle" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Brittleness</button>
            <button onclick="setSim10Mode('melting')" id="sim10BtnMelt" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Melting Point</button>
            <button onclick="setSim10Mode('conduct')" id="sim10BtnConduct" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Conductivity</button>
        </div>
    </div>

    <!-- Brittleness View -->
    <div id="sim10BrittleView" class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-rose-400 block">Mechanical Shear & Crystal Cleavage (Brittleness)</span>
        <svg viewBox="0 0 220 100" class="w-full h-24 mx-auto">
            <!-- Anvil -->
            <rect x="30" y="80" width="160" height="15" fill="#334155" rx="2"/>
            <!-- Top ionic layer (+ - + -) -->
            <g id="sim10TopLayer" class="transition-transform duration-500">
                <circle cx="65" cy="45" r="9" fill="#f59e0b"/>
                <text x="65" y="48" font-size="10" fill="#000" font-weight="bold" text-anchor="middle">+</text>
                <circle cx="95" cy="45" r="9" fill="#06b6d4"/>
                <text x="95" y="48" font-size="10" fill="#000" font-weight="bold" text-anchor="middle">-</text>
                <circle cx="125" cy="45" r="9" fill="#f59e0b"/>
                <text x="125" y="48" font-size="10" fill="#000" font-weight="bold" text-anchor="middle">+</text>
                <circle cx="155" cy="45" r="9" fill="#06b6d4"/>
                <text x="155" y="48" font-size="10" fill="#000" font-weight="bold" text-anchor="middle">-</text>
            </g>
            <!-- Bottom ionic layer (- + - +) -->
            <g id="sim10BottomLayer">
                <circle cx="65" cy="65" r="9" fill="#06b6d4"/>
                <text x="65" y="68" font-size="10" fill="#000" font-weight="bold" text-anchor="middle">-</text>
                <circle cx="95" cy="65" r="9" fill="#f59e0b"/>
                <text x="95" y="68" font-size="10" fill="#000" font-weight="bold" text-anchor="middle">+</text>
                <circle cx="125" cy="65" r="9" fill="#06b6d4"/>
                <text x="125" y="68" font-size="10" fill="#000" font-weight="bold" text-anchor="middle">-</text>
                <circle cx="155" cy="65" r="9" fill="#f59e0b"/>
                <text x="155" y="68" font-size="10" fill="#000" font-weight="bold" text-anchor="middle">+</text>
            </g>
            <!-- Hammer striking top layer -->
            <g id="sim10Hammer" transform="translate(140, 10)" class="transition-transform duration-300">
                <rect x="0" y="5" width="22" height="14" fill="#64748b" rx="2"/>
                <rect x="9" y="-12" width="4" height="20" fill="#78350f"/>
            </g>
        </svg>
        <button onclick="strikeIonicCrystal()" class="px-3 py-1 rounded bg-rose-600/30 hover:bg-rose-600/50 text-rose-200 border border-rose-500/40 text-xs font-bold">Apply Shear Stress (Hammer)</button>
        <p id="sim10BrittleMsg" class="text-[11px] text-slate-400">Shear forces shift lattice planes: like charges align (+ next to +), causing strong repulsion that shatters the crystal.</p>
    </div>

    <!-- Melting Point View -->
    <div id="sim10MeltView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-amber-300 block">Thermal Lattice Breakdown: High Melting Point of NaCl (1074 K / 801°C)</span>
        <div class="flex items-center justify-center gap-6">
            <svg viewBox="0 0 100 110" class="w-24 h-24">
                <!-- Spatula with salt -->
                <line x1="10" y1="50" x2="80" y2="50" stroke="#94a3b8" stroke-width="3"/>
                <ellipse cx="70" cy="48" rx="10" ry="3" fill="#f8fafc"/>
                <!-- Burner flame -->
                <polygon points="65,90 70,55 75,90" fill="#f97316"/>
                <polygon points="67,90 70,65 73,90" fill="#facc15"/>
            </svg>
            <div class="text-left space-y-1 text-xs">
                <div>NaCl mp: <strong class="text-amber-300">1074 K (801°C)</strong></div>
                <div>CaO mp: <strong class="text-rose-400">2850 K (2577°C)</strong></div>
                <div>MgCl2 mp: <strong class="text-sky-300">987 K (714°C)</strong></div>
                <p class="text-[10px] text-slate-400 mt-1">High lattice energy demands massive kinetic energy to overcome electrostatic bonds.</p>
            </div>
        </div>
    </div>

    <!-- Conductivity View -->
    <div id="sim10ConductView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-emerald-400 block">Electrical Conduction: Solid vs Aqueous / Molten State</span>
        <svg viewBox="0 0 180 90" class="w-44 h-20 mx-auto">
            <!-- Beaker with solution -->
            <rect x="40" y="20" width="100" height="65" rx="3" fill="#0f172a" stroke="#64748b"/>
            <rect id="sim10Liq" x="42" y="38" width="96" height="45" fill="#38bdf8" fill-opacity="0.15"/>
            <!-- Electrodes -->
            <rect x="60" y="15" width="8" height="60" fill="#475569"/>
            <rect x="110" y="15" width="8" height="60" fill="#475569"/>
            <!-- Circuit Bulb -->
            <circle id="sim10Bulb" cx="90" cy="15" r="7" fill="#334155" stroke="#94a3b8"/>
        </svg>
        <div class="flex justify-center gap-2">
            <button onclick="testConductivity('solid')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold">Solid Dry Salt</button>
            <button onclick="testConductivity('aqueous')" class="px-2.5 py-1 rounded bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-200 border border-emerald-500/40 text-xs font-bold">Aqueous / Molten Salt</button>
        </div>
        <p id="sim10ConductMsg" class="text-[11px] text-slate-400">Solid: ions fixed in lattice (no conduction). Solution/Molten: ions move freely (conducts current!).</p>
    </div>
</div>
''',

    11: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Metallurgy: Mineral, Ore, Gangue & Extraction Branching</h4>
        <span class="text-xs text-sky-300 font-mono">Ore = Mineral + Economic Viability</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-center text-xs">
        <div class="p-2.5 bg-slate-950/70 rounded-xl border border-rose-500/30">
            <span class="font-bold text-rose-300 block mb-1">High Reactivity</span>
            <p class="text-[11px] text-rose-400 font-mono">K, Na, Ca, Mg, Al</p>
            <div class="my-2 p-1 bg-slate-900 rounded text-[10px] text-slate-300">
                Cannot be reduced by carbon (high oxygen affinity).
            </div>
            <span class="text-[10px] font-bold text-emerald-400 block">Method: Electrolytic Reduction of Molten Chlorides/Oxides</span>
        </div>

        <div class="p-2.5 bg-slate-950/70 rounded-xl border border-amber-500/30">
            <span class="font-bold text-amber-300 block mb-1">Medium Reactivity</span>
            <p class="text-[11px] text-amber-400 font-mono">Zn, Fe, Pb</p>
            <div class="my-2 p-1 bg-slate-900 rounded text-[10px] text-slate-300">
                Occur as sulphides or carbonates in crust.
            </div>
            <span class="text-[10px] font-bold text-amber-300 block">Method: Roasting / Calcination → Carbon Reduction</span>
        </div>

        <div class="p-2.5 bg-slate-950/70 rounded-xl border border-emerald-500/30">
            <span class="font-bold text-emerald-300 block mb-1">Low Reactivity</span>
            <p class="text-[11px] text-emerald-400 font-mono">Cu, Hg, Ag, Au</p>
            <div class="my-2 p-1 bg-slate-900 rounded text-[10px] text-slate-300">
                Occur native or as weak sulphides (cinnabar, copper glance).
            </div>
            <span class="text-[10px] font-bold text-sky-400 block">Method: Simple Heating in Air / Native Extraction</span>
        </div>
    </div>
</div>
''',

    12: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Low Reactivity Metallurgy: Cinnabar (HgS) & Copper Glance (Cu2S)</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim12Ore('cinnabar')" id="sim12BtnHg" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Cinnabar (HgS)</button>
            <button onclick="setSim12Ore('copper')" id="sim12BtnCu" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Copper Glance (Cu2S)</button>
        </div>
    </div>

    <!-- Cinnabar View -->
    <div id="sim12HgView" class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-rose-400 block">Two-Step Thermal Extraction of Mercury from Cinnabar (HgS)</span>
        <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="font-bold text-amber-300 block">Step 1: Roasting</span>
                <span class="text-[10px] text-slate-300 font-mono">2HgS + 3O2 → 2HgO + 2SO2</span>
                <p class="text-[10px] text-slate-400 mt-1">Cinnabar ore is heated strongly in air to form mercuric oxide.</p>
            </div>
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="font-bold text-cyan-300 block">Step 2: Thermal Decomposition</span>
                <span class="text-[10px] text-slate-300 font-mono">2HgO → 2Hg(l) + O2</span>
                <p class="text-[10px] text-slate-400 mt-1">Further heating decomposes HgO directly into liquid mercury droplets.</p>
            </div>
        </div>
        <button onclick="roastCinnabar()" class="px-3 py-1 rounded bg-rose-600/30 hover:bg-rose-600/50 text-rose-200 border border-rose-500/40 text-xs font-bold">Simulate Heating Cinnabar</button>
        <p id="sim12HgMsg" class="text-[11px] text-slate-400">Mercury has very low affinity for oxygen; no chemical reducing agent like carbon is needed.</p>
    </div>

    <!-- Copper Glance View -->
    <div id="sim12CuView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-amber-400 block">Auto-Reduction of Copper Glance (Cu2S)</span>
        <div class="p-2 bg-slate-900 rounded border border-slate-800 text-xs font-mono">
            2Cu2O + Cu2S → 6Cu + SO2 ↑
        </div>
        <p class="text-xs text-slate-300">Heating copper glance partially forms Cu2O. In restricted air, unreacted Cu2S reduces Cu2O to crude molten blister copper!</p>
    </div>
</div>
''',

    13: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Moderate Reactivity: Roasting, Calcination & Thermit Reaction</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim13Tab('roast')" id="sim13TabRoast" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Roasting vs Calcination</button>
            <button onclick="setSim13Tab('thermit')" id="sim13TabThermit" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Thermit Welding</button>
        </div>
    </div>

    <!-- Tab 1: Roasting vs Calcination -->
    <div id="sim13ViewRoast" class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-center">
        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <span class="text-xs font-bold text-amber-400 block mb-1">Roasting (Sulphide Ore in Excess Air)</span>
            <div class="p-1.5 bg-slate-900 rounded font-mono text-[10px] text-amber-200 mb-1">
                2ZnS + 3O2 → 2ZnO + 2SO2 ↑
            </div>
            <p class="text-[11px] text-slate-400">Zinc blende is heated strongly in continuous supply of air, releasing SO2 gas.</p>
        </div>

        <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <span class="text-xs font-bold text-sky-400 block mb-1">Calcination (Carbonate Ore in Limited Air)</span>
            <div class="p-1.5 bg-slate-900 rounded font-mono text-[10px] text-sky-200 mb-1">
                ZnCO3 → ZnO + CO2 ↑
            </div>
            <p class="text-[11px] text-slate-400">Calamine is heated strongly in absence/limited air, driving off CO2 gas.</p>
        </div>
    </div>

    <!-- Tab 2: Thermit Railway Welding -->
    <div id="sim13ViewThermit" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-orange-400 block">Thermit Reaction: Fe2O3 + 2Al → 2Fe(l) + Al2O3 + Immense Heat</span>
        <svg viewBox="0 0 200 100" class="w-full h-24 mx-auto">
            <!-- Crucible -->
            <polygon points="80,10 120,10 110,50 90,50" fill="#475569" stroke="#94a3b8"/>
            <!-- Thermit mixture & spark -->
            <polygon id="sim13ThermitSpark" points="95,15 105,15 102,40 98,40" fill="#f59e0b" class="transition-colors duration-500"/>
            <!-- Molten iron stream pouring -->
            <line id="sim13IronStream" x1="100" y1="50" x2="100" y2="80" stroke="#ef4444" stroke-width="3" opacity="0" class="transition-opacity duration-300"/>
            <!-- Railway track gap -->
            <rect x="30" y="80" width="65" height="15" fill="#334155"/>
            <rect x="105" y="80" width="65" height="15" fill="#334155"/>
            <!-- Weld joint filling -->
            <rect id="sim13Weld" x="95" y="80" width="10" height="15" fill="#f97316" opacity="0" class="transition-opacity duration-500"/>
        </svg>
        <button onclick="igniteThermit()" class="px-3 py-1 rounded bg-orange-600/30 hover:bg-orange-600/50 text-orange-200 border border-orange-500/40 text-xs font-bold">Ignite Thermit Mixture</button>
        <p id="sim13ThermitMsg" class="text-[11px] text-slate-400">Extreme displacement heat produces iron in white-hot liquid state, welding cracked railway tracks!</p>
    </div>
</div>
''',

    14: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Electrolytic Reduction: Molten NaCl (Down's Cell)</h4>
        <span class="text-xs text-rose-400 font-mono">Cathode (-): Na⁺ + e⁻ → Na | Anode (+): 2Cl⁻ → Cl2 + 2e⁻</span>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2">
        <svg viewBox="0 0 240 120" class="w-full h-28 mx-auto">
            <!-- Cell vessel with molten NaCl (800°C) -->
            <rect x="40" y="20" width="160" height="85" rx="5" fill="#0f172a" stroke="#475569" stroke-width="2"/>
            <rect x="42" y="38" width="156" height="65" fill="#f59e0b" fill-opacity="0.2"/>
            <!-- Cathode (Iron ring / cathode) -->
            <rect x="65" y="25" width="12" height="70" fill="#64748b" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="71" y="103" font-size="8" fill="#3b82f6" font-weight="bold" text-anchor="middle">Cathode (-)</text>
            <!-- Molten sodium collection -->
            <circle id="sim14NaMetal" cx="71" cy="40" r="5" fill="#fde047" opacity="0" class="transition-opacity duration-500"/>
            <!-- Anode (Carbon / Graphite) -->
            <rect x="160" y="25" width="12" height="70" fill="#334155" stroke="#ef4444" stroke-width="1.5"/>
            <text x="166" y="103" font-size="8" fill="#ef4444" font-weight="bold" text-anchor="middle">Anode (+)</text>
            <!-- Chlorine gas bubbles -->
            <g id="sim14ClGas" opacity="0" class="transition-opacity duration-500">
                <circle cx="166" cy="45" r="3" fill="#86efac"/>
                <circle cx="166" cy="35" r="2.5" fill="#86efac"/>
            </g>
        </svg>
        <div class="flex justify-center">
            <button onclick="electrolyseMoltenNaCl()" class="px-3 py-1 rounded bg-amber-600/30 hover:bg-amber-600/50 text-amber-200 border border-amber-500/40 text-xs font-bold">Pass Electrolytic Current</button>
        </div>
        <p id="sim14Msg" class="text-[11px] text-center text-slate-400">Pure sodium metal collects at negative cathode; greenish-yellow Cl2 gas bubbles at positive anode.</p>
    </div>
</div>
''',

    15: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Electrolytic Refining of Copper & Anode Mud</h4>
        <span class="text-xs text-sky-300 font-mono">Acidified CuSO4 Electrolyte Bath</span>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2">
        <svg viewBox="0 0 240 120" class="w-full h-28 mx-auto">
            <!-- Glass Tank with Acidified CuSO4 -->
            <rect x="35" y="20" width="170" height="85" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
            <rect x="37" y="35" width="166" height="68" fill="#0284c7" fill-opacity="0.3"/>
            <!-- Impure Copper Anode (+) -->
            <rect id="sim15Anode" x="65" y="15" width="22" height="70" fill="#b45309" stroke="#9a3412" stroke-width="1.5" class="transition-all duration-1000"/>
            <text x="76" y="98" font-size="8" fill="#f97316" font-weight="bold" text-anchor="middle">Impure Anode (+)</text>
            <!-- Pure Copper Cathode (-) -->
            <rect id="sim15Cathode" x="150" y="15" width="8" height="70" fill="#f97316" stroke="#ea580c" stroke-width="1.5" class="transition-all duration-1000"/>
            <text x="154" y="98" font-size="8" fill="#38bdf8" font-weight="bold" text-anchor="middle">Pure Cathode (-)</text>
            <!-- Anode Mud at tank bottom -->
            <ellipse id="sim15Mud" cx="76" cy="100" rx="14" ry="3" fill="#64748b" opacity="0" class="transition-opacity duration-1000"/>
            <text id="sim15MudLabel" x="76" y="112" font-size="7" fill="#fbbf24" text-anchor="middle" opacity="0">Anode Mud (Au, Ag)</text>
        </svg>
        <div class="flex justify-center gap-2">
            <button onclick="refineCopper()" class="px-3 py-1 rounded bg-sky-600/30 hover:bg-sky-600/50 text-sky-200 border border-sky-500/40 text-xs font-bold">Start Electrolytic Refining</button>
            <button onclick="resetRefining()" class="px-2 py-1 rounded bg-slate-800 text-slate-400 hover:text-slate-200 text-xs">Reset</button>
        </div>
        <p id="sim15Msg" class="text-[11px] text-center text-slate-400">Pure Cu transfers from dissolving anode to growing cathode. Precious insoluble metals settle as anode mud.</p>
    </div>
</div>
''',

    16: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Corrosion Testing (Activity 3.14) & Alloy Forge</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim16Tab('tubes')" id="sim16TabTubes" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Activity 3.14 (3-Tube Test)</button>
            <button onclick="setSim16Tab('alloys')" id="sim16TabAlloys" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Alloy Forge & Delhi Pillar</button>
        </div>
    </div>

    <!-- 3-Tube Corrosion Test View -->
    <div id="sim16TubesView" class="space-y-3">
        <div class="grid grid-cols-3 gap-2 text-center">
            <!-- Tube A -->
            <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
                <span class="text-xs font-bold text-rose-400 block mb-1">Tube A: Air + Water</span>
                <svg viewBox="0 0 60 100" class="w-full h-24 mx-auto">
                    <rect x="15" y="10" width="30" height="85" rx="4" fill="#0f172a" stroke="#64748b"/>
                    <rect x="17" y="45" width="26" height="48" fill="#38bdf8" fill-opacity="0.25"/>
                    <polygon id="sim16NailA" points="28,40 32,40 32,80 30,86 28,80" fill="#94a3b8" stroke="#475569" class="transition-colors duration-1000"/>
                </svg>
                <span id="sim16ResA" class="text-[10px] text-slate-400 font-semibold block mt-1">Rusts Heavily</span>
            </div>

            <!-- Tube B -->
            <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
                <span class="text-xs font-bold text-sky-400 block mb-1">Tube B: Boiled + Oil</span>
                <svg viewBox="0 0 60 100" class="w-full h-24 mx-auto">
                    <rect x="15" y="10" width="30" height="85" rx="4" fill="#0f172a" stroke="#64748b"/>
                    <rect x="17" y="55" width="26" height="38" fill="#38bdf8" fill-opacity="0.25"/>
                    <!-- Oil layer -->
                    <rect x="17" y="48" width="26" height="7" fill="#eab308" fill-opacity="0.5"/>
                    <polygon points="28,52 32,52 32,85 30,90 28,85" fill="#94a3b8" stroke="#475569"/>
                </svg>
                <span class="text-[10px] text-emerald-400 font-semibold block mt-1">No Rust (No Air)</span>
            </div>

            <!-- Tube C -->
            <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
                <span class="text-xs font-bold text-amber-400 block mb-1">Tube C: Dry Air + CaCl2</span>
                <svg viewBox="0 0 60 100" class="w-full h-24 mx-auto">
                    <rect x="15" y="10" width="30" height="85" rx="4" fill="#0f172a" stroke="#64748b"/>
                    <!-- Anhydrous CaCl2 pellets -->
                    <circle cx="25" cy="85" r="3" fill="#cbd5e1"/>
                    <circle cx="35" cy="85" r="3" fill="#cbd5e1"/>
                    <polygon points="28,30 32,30 32,70 30,76 28,70" fill="#94a3b8" stroke="#475569"/>
                </svg>
                <span class="text-[10px] text-emerald-400 font-semibold block mt-1">No Rust (No Water)</span>
            </div>
        </div>
        <div class="flex justify-center">
            <button onclick="incubateRust()" class="px-3 py-1 rounded bg-rose-600/30 hover:bg-rose-600/50 text-rose-200 border border-rose-500/40 text-xs font-bold">Leave for Several Days</button>
        </div>
        <p class="text-[11px] text-center text-slate-400">Activity 3.14 proves both oxygen (air) and water (moisture) are essential for iron rusting.</p>
    </div>

    <!-- Alloy Forge View -->
    <div id="sim16AlloysView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-3 text-xs">
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center">
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="font-bold text-amber-300 block">Brass</span>
                <span class="text-[10px] text-slate-300">Cu + Zn</span>
                <span class="text-[10px] text-slate-400 block mt-0.5">Hardware & bells</span>
            </div>
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="font-bold text-orange-400 block">Bronze</span>
                <span class="text-[10px] text-slate-300">Cu + Sn</span>
                <span class="text-[10px] text-slate-400 block mt-0.5">Statues & medals</span>
            </div>
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="font-bold text-sky-300 block">Solder</span>
                <span class="text-[10px] text-slate-300">Pb + Sn</span>
                <span class="text-[10px] text-slate-400 block mt-0.5">Low mp wire joints</span>
            </div>
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="font-bold text-emerald-300 block">Stainless Steel</span>
                <span class="text-[10px] text-slate-300">Fe + C + Ni + Cr</span>
                <span class="text-[10px] text-slate-400 block mt-0.5">Never rusts</span>
            </div>
        </div>
        <div class="p-2 bg-slate-900/90 rounded border border-slate-800 flex items-center justify-between text-slate-300">
            <span><strong>Ancient Delhi Iron Pillar:</strong> 1600 years old, 8 m tall, 6 tonnes, rust-free near Qutub Minar due to a protective passive phosphate film!</span>
            <span class="text-amber-400 font-bold ml-2">400 CE</span>
        </div>
    </div>
</div>
'''
}
