"""Interactive Simulators 1 to 8 for Class 10 Science Chapter 4: Carbon and its Compounds
High-fidelity, responsive, SVG-based laboratory simulators with Tailwind CSS.
"""

simulators = {
    1: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Activity 4.1: Carbon Ubiquity & Physical Properties</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim1Mode('sort')" id="sim1BtnSort" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Activity 4.1 Item Sorter</button>
            <button onclick="setSim1Mode('constants')" id="sim1BtnConst" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Table 4.1 MP / BP Constants</button>
            <button onclick="setSim1Mode('circuit')" id="sim1BtnCircuit" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Conductivity Test</button>
        </div>
    </div>

    <!-- Mode 1: Item Sorter -->
    <div id="sim1SortView" class="space-y-3">
        <span class="text-xs text-slate-300 block">Classify everyday articles into their elemental categories (Activity 4.1):</span>
        <div class="grid grid-cols-3 gap-2 text-center text-xs">
            <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
                <span class="font-bold text-sky-400 block mb-1">Metallic Items</span>
                <div class="space-y-1 text-[11px] text-slate-300">
                    <div class="p-1 bg-slate-900 rounded">Steel Spoon</div>
                    <div class="p-1 bg-slate-900 rounded">Copper Wire</div>
                    <div class="p-1 bg-slate-900 rounded">Aluminium Pan</div>
                </div>
            </div>
            <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800">
                <span class="font-bold text-amber-400 block mb-1">Glass / Clay Items</span>
                <div class="space-y-1 text-[11px] text-slate-300">
                    <div class="p-1 bg-slate-900 rounded">Ceramic Mug</div>
                    <div class="p-1 bg-slate-900 rounded">Glass Tumbler</div>
                    <div class="p-1 bg-slate-900 rounded">Clay Pot</div>
                </div>
            </div>
            <div class="p-2.5 bg-slate-950/70 rounded-xl border border-emerald-500/40 bg-emerald-950/10">
                <span class="font-bold text-emerald-400 block mb-1">Others (Carbon Compounds)</span>
                <div class="space-y-1 text-[11px] text-emerald-200">
                    <div class="p-1 bg-emerald-900/30 rounded">Cotton Shirt & Silk</div>
                    <div class="p-1 bg-emerald-900/30 rounded">Food (Bread, Sugar)</div>
                    <div class="p-1 bg-emerald-900/30 rounded">Medicines & Books</div>
                </div>
            </div>
        </div>
        <p class="text-[11px] text-slate-400 text-center">Nearly all items in the 'Others' category are organic carbon compounds!</p>
    </div>

    <!-- Mode 2: MP / BP Constants -->
    <div id="sim1ConstView" class="hidden space-y-2 p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-xs">
        <span class="font-bold text-amber-300 block text-center">Table 4.1: Melting and Boiling Points of Covalent Carbon Compounds</span>
        <div class="grid grid-cols-4 gap-2 text-center text-[11px]">
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="font-bold text-sky-300 block">Methane (CH4)</span>
                <div class="text-slate-400 mt-1">MP: <strong class="text-slate-200">90 K</strong></div>
                <div class="text-slate-400">BP: <strong class="text-slate-200">111 K</strong></div>
            </div>
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="font-bold text-indigo-300 block">Chloroform (CHCl3)</span>
                <div class="text-slate-400 mt-1">MP: <strong class="text-slate-200">209 K</strong></div>
                <div class="text-slate-400">BP: <strong class="text-slate-200">334 K</strong></div>
            </div>
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="font-bold text-emerald-300 block">Ethanol (C2H5OH)</span>
                <div class="text-slate-400 mt-1">MP: <strong class="text-slate-200">156 K</strong></div>
                <div class="text-slate-400">BP: <strong class="text-slate-200">351 K</strong></div>
            </div>
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="font-bold text-rose-300 block">Acetic Acid (CH3COOH)</span>
                <div class="text-slate-400 mt-1">MP: <strong class="text-slate-200">290 K</strong></div>
                <div class="text-slate-400">BP: <strong class="text-slate-200">391 K</strong></div>
            </div>
        </div>
        <p class="text-[11px] text-slate-400 text-center">Compare with ionic NaCl (MP 1074 K): weak intermolecular forces mean carbon compounds boil at very low temperatures.</p>
    </div>

    <!-- Mode 3: Conductivity Circuit -->
    <div id="sim1CircuitView" class="hidden space-y-3 p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 block">Electrical Conductivity: Ionic Solution vs Covalent Carbon Solution</span>
        <svg viewBox="0 0 180 90" class="w-44 h-20 mx-auto">
            <rect x="40" y="20" width="100" height="65" rx="3" fill="#0f172a" stroke="#64748b"/>
            <rect id="sim1Liq" x="42" y="38" width="96" height="45" fill="#38bdf8" fill-opacity="0.15"/>
            <rect x="60" y="15" width="8" height="60" fill="#475569"/>
            <rect x="110" y="15" width="8" height="60" fill="#475569"/>
            <circle id="sim1Bulb" cx="90" cy="15" r="7" fill="#334155" stroke="#94a3b8"/>
        </svg>
        <div class="flex justify-center gap-2">
            <button onclick="testSim1Conduct('ionic')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold">Ionic NaCl Solution</button>
            <button onclick="testSim1Conduct('covalent')" class="px-2.5 py-1 rounded bg-amber-600/30 hover:bg-amber-600/50 text-amber-200 border border-amber-500/40 text-xs font-bold">Covalent Glucose / Alcohol</button>
        </div>
        <p id="sim1ConductMsg" class="text-[11px] text-slate-400">Carbon compounds do not dissociate into free ions and are non-conductors of electricity.</p>
    </div>
</div>
''',

    2: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Valency Dilemma: Why Carbon Shares Electrons</h4>
        <span class="text-xs text-sky-300 font-mono">Carbon (Z=6): 2, 4</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-center text-xs">
        <!-- Option 1: Gain 4 electrons -->
        <div class="p-3 bg-slate-950/70 rounded-xl border border-rose-500/30 space-y-2">
            <span class="font-bold text-rose-400 block">Hypothesis A: Gain 4e⁻ (C⁴⁻)</span>
            <div class="p-2 bg-slate-900 rounded font-mono text-[11px] text-rose-300">
                6 Protons vs 10 Electrons
            </div>
            <button onclick="testC4Minus()" class="px-2.5 py-1 rounded bg-rose-600/30 hover:bg-rose-600/50 text-rose-200 border border-rose-500/40 text-[11px] font-bold">Test C⁴⁻ Formation</button>
            <p id="sim2C4MinusMsg" class="text-[10px] text-slate-400">Tiny nucleus cannot stably hold 10 electrons due to intense inter-electron repulsion.</p>
        </div>

        <!-- Option 2: Lose 4 electrons -->
        <div class="p-3 bg-slate-950/70 rounded-xl border border-amber-500/30 space-y-2">
            <span class="font-bold text-amber-400 block">Hypothesis B: Lose 4e⁻ (C⁴⁺)</span>
            <div class="p-2 bg-slate-900 rounded font-mono text-[11px] text-amber-300">
                Astronomical Ionisation Energy
            </div>
            <button onclick="testC4Plus()" class="px-2.5 py-1 rounded bg-amber-600/30 hover:bg-amber-600/50 text-amber-200 border border-amber-500/40 text-[11px] font-bold">Test C⁴⁺ Formation</button>
            <p id="sim2C4PlusMsg" class="text-[10px] text-slate-400">Stripping 4 successive electrons requires massive energy, leaving an unstable nucleus.</p>
        </div>

        <!-- Solution: Covalent Sharing -->
        <div class="p-3 bg-slate-950/70 rounded-xl border border-emerald-500/40 bg-emerald-950/10 space-y-2">
            <span class="font-bold text-emerald-400 block">Solution: Covalent Sharing</span>
            <div class="p-2 bg-emerald-900/30 rounded font-mono text-[11px] text-emerald-300">
                Share 4 Pairs → Stable Octet (2,8)
            </div>
            <button onclick="testCovalentSharing()" class="px-2.5 py-1 rounded bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-200 border border-emerald-500/40 text-[11px] font-bold">Share Valence Pairs</button>
            <p id="sim2CovalentMsg" class="text-[10px] text-slate-400">Both atoms share electron pairs, attaining noble gas octet stability smoothly!</p>
        </div>
    </div>
</div>
''',

    3: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Covalent Bonds: Single, Double & Triple Sharing</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim3Molecule('h2')" id="sim3BtnH2" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">H2 & CH4 (Single)</button>
            <button onclick="setSim3Molecule('o2')" id="sim3BtnO2" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">O2 & CO2 (Double)</button>
            <button onclick="setSim3Molecule('n2')" id="sim3BtnN2" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">N2 (Triple)</button>
            <button onclick="setSim3Molecule('s8')" id="sim3BtnS8" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">S8 Crown Ring</button>
        </div>
    </div>

    <!-- H2 & CH4 Single Bond View -->
    <div id="sim3H2View" class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-sky-300 block">Single Covalent Bond: Sharing 1 Electron Pair</span>
        <svg viewBox="0 0 200 80" class="w-full h-20 mx-auto">
            <!-- Two overlapping hydrogen atoms -->
            <circle cx="85" cy="40" r="25" fill="#38bdf8" fill-opacity="0.15" stroke="#38bdf8" stroke-width="1.5"/>
            <circle cx="115" cy="40" r="25" fill="#38bdf8" fill-opacity="0.15" stroke="#38bdf8" stroke-width="1.5"/>
            <circle cx="97" cy="40" r="3" fill="#fde047"/>
            <circle cx="103" cy="40" r="3" fill="#fde047"/>
            <text x="75" y="44" font-size="10" fill="#fff" font-weight="bold">H</text>
            <text x="120" y="44" font-size="10" fill="#fff" font-weight="bold">H</text>
        </svg>
        <p class="text-[11px] text-slate-300">H:H (H–H single bond). In Methane (CH4), central carbon forms 4 single covalent bonds with 4 hydrogen atoms.</p>
    </div>

    <!-- O2 & CO2 Double Bond View -->
    <div id="sim3O2View" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-rose-300 block">Double Covalent Bond: Sharing 2 Electron Pairs</span>
        <div class="flex items-center justify-center gap-6 font-mono text-sm">
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="text-rose-400 font-bold block">O = O</span>
                <span class="text-[10px] text-slate-400">4 shared electrons</span>
            </div>
            <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="text-sky-300 font-bold block">O = C = O</span>
                <span class="text-[10px] text-slate-400">Carbon Dioxide (Linear)</span>
            </div>
        </div>
        <p class="text-[11px] text-slate-400">Each double bond consists of 2 shared electron pairs (4 electrons), completing octets for both atoms.</p>
    </div>

    <!-- N2 Triple Bond View -->
    <div id="sim3N2View" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-indigo-300 block">Triple Covalent Bond: Sharing 3 Electron Pairs</span>
        <div class="p-2 bg-slate-900 rounded inline-block font-mono text-base text-indigo-300 border border-slate-800">
            :N ≡ N:
        </div>
        <p class="text-[11px] text-slate-400">6 shared valence electrons (3 pairs) bind two nitrogen atoms with immense thermodynamic strength.</p>
    </div>

    <!-- S8 Crown Ring View -->
    <div id="sim3S8View" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-yellow-300 block">Cyclic S8 Crown Molecule (NCERT Section 4.1)</span>
        <svg viewBox="0 0 160 80" class="w-44 h-20 mx-auto">
            <!-- Crown shape polyline -->
            <polyline points="20,50 40,25 60,50 80,25 100,50 120,25 140,50 80,65 20,50" fill="none" stroke="#facc15" stroke-width="2"/>
            <circle cx="20" cy="50" r="5" fill="#ca8a04"/><circle cx="40" cy="25" r="5" fill="#ca8a04"/>
            <circle cx="60" cy="50" r="5" fill="#ca8a04"/><circle cx="80" cy="25" r="5" fill="#ca8a04"/>
            <circle cx="100" cy="50" r="5" fill="#ca8a04"/><circle cx="120" cy="25" r="5" fill="#ca8a04"/>
            <circle cx="140" cy="50" r="5" fill="#ca8a04"/><circle cx="80" cy="65" r="5" fill="#ca8a04"/>
        </svg>
        <p class="text-[11px] text-slate-400">Eight sulphur atoms share single bonds in a puckered, crown-shaped eight-membered ring.</p>
    </div>
</div>
''',

    4: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Allotropes of Carbon: Diamond, Graphite & Fullerene</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim4Allotrope('diamond')" id="sim4BtnDia" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Diamond (3D)</button>
            <button onclick="setSim4Allotrope('graphite')" id="sim4BtnGph" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Graphite (Layers)</button>
            <button onclick="setSim4Allotrope('fullerene')" id="sim4BtnFul" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Fullerene (C60)</button>
        </div>
    </div>

    <!-- Diamond View -->
    <div id="sim4DiaView" class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-cyan-300 block">Diamond: Rigid 3D Tetrahedral Network</span>
        <svg viewBox="0 0 160 90" class="w-44 h-20 mx-auto">
            <polygon points="80,10 115,35 80,75 45,35" fill="none" stroke="#38bdf8" stroke-width="2"/>
            <line x1="45" y1="35" x2="115" y2="35" stroke="#38bdf8" stroke-width="1.5"/>
            <line x1="80" y1="10" x2="80" y2="75" stroke="#38bdf8" stroke-width="1.5"/>
            <circle cx="80" cy="10" r="4" fill="#bae6fd"/><circle cx="115" cy="35" r="4" fill="#bae6fd"/>
            <circle cx="80" cy="75" r="4" fill="#bae6fd"/><circle cx="45" cy="35" r="4" fill="#bae6fd"/>
        </svg>
        <p class="text-[11px] text-slate-300">Each carbon bonded to 4 others in rigid tetrahedral array. Hardest known natural substance; electrical insulator.</p>
    </div>

    <!-- Graphite View -->
    <div id="sim4GphView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-indigo-300 block">Graphite: Hexagonal Planar Sheets & Delocalised Electrons</span>
        <svg viewBox="0 0 160 90" class="w-44 h-20 mx-auto">
            <polygon points="30,20 60,15 90,20 105,35 75,40 45,35" fill="none" stroke="#818cf8" stroke-width="1.5"/>
            <polygon points="30,55 60,50 90,55 105,70 75,75 45,70" fill="none" stroke="#818cf8" stroke-width="1.5"/>
            <line x1="45" y1="35" x2="45" y2="70" stroke="#94a3b8" stroke-dasharray="2 2"/>
            <line x1="75" y1="40" x2="75" y2="75" stroke="#94a3b8" stroke-dasharray="2 2"/>
        </svg>
        <p class="text-[11px] text-slate-300">Each carbon bonded to 3 others; free delocalised electron conducts electricity! Layers slide smoothly (lubricant).</p>
    </div>

    <!-- Fullerene View -->
    <div id="sim4FulView" class="hidden p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <span class="text-xs font-bold text-emerald-300 block">Buckminsterfullerene (C60): Geodesic Football Cage</span>
        <svg viewBox="0 0 160 90" class="w-44 h-20 mx-auto">
            <circle cx="80" cy="45" r="30" fill="none" stroke="#34d399" stroke-width="1.5"/>
            <polygon points="80,30 92,38 88,52 72,52 68,38" fill="none" stroke="#34d399" stroke-width="1.5"/>
            <line x1="80" y1="15" x2="80" y2="30" stroke="#34d399"/>
            <line x1="110" y1="45" x2="92" y2="38" stroke="#34d399"/>
            <line x1="50" y1="45" x2="68" y2="38" stroke="#34d399"/>
        </svg>
        <p class="text-[11px] text-slate-300">60 carbon atoms assembled into 20 hexagons and 12 pentagons resembling Buckminster Fuller's geodesic domes.</p>
    </div>
</div>
''',

    5: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Carbon Versatility: Catenation & Small Atomic Radius</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim5Framework('straight')" id="sim5BtnStr" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Straight Chain</button>
            <button onclick="setSim5Framework('branched')" id="sim5BtnBrn" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Branched Chain</button>
            <button onclick="setSim5Framework('ring')" id="sim5BtnRng" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Cyclic Ring</button>
        </div>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-3">
        <div id="sim5FrameworkVisual" class="font-mono text-base text-amber-300 tracking-wider">
            – C – C – C – C – C –
        </div>
        <div class="p-2 bg-slate-900 rounded border border-slate-800 text-xs text-slate-300">
            <strong>C–C Bond Energy:</strong> 348 kJ/mol (Extremely strong & stable) vs <strong>Si–Si Bond Energy:</strong> 222 kJ/mol (Weak & reactive).
        </div>
        <p id="sim5FrameworkDesc" class="text-[11px] text-slate-400">Catenation allows carbon to form infinitely long unbranched chains.</p>
    </div>
</div>
''',

    6: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">1828: Friedrich Wöhler's Urea Synthesis</h4>
        <span class="text-xs text-rose-400 font-mono">Vital Force Disproved</span>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-3">
        <svg viewBox="0 0 200 90" class="w-full h-22 mx-auto">
            <!-- Test tube with ammonium cyanate -->
            <rect x="70" y="10" width="60" height="40" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
            <!-- Crystals inside -->
            <ellipse id="sim6Crystals" cx="100" cy="35" rx="18" ry="6" fill="#cbd5e1" class="transition-colors duration-700"/>
            <!-- Flame -->
            <g id="sim6Flame" transform="translate(100, 55)" opacity="0" class="transition-opacity duration-300">
                <polygon points="0,0 6,-15 12,0" fill="#f97316"/>
                <polygon points="3,0 6,-10 9,0" fill="#fef08a"/>
            </g>
        </svg>
        <div class="p-2 bg-slate-900 rounded font-mono text-xs text-amber-300">
            NH4CNO (Inorganic Ammonium Cyanate) ⎯Δ⎯→ NH2CONH2 (Organic Urea)
        </div>
        <button onclick="heatWöhlerTube()" class="px-3 py-1 rounded bg-amber-600/30 hover:bg-amber-600/50 text-amber-200 border border-amber-500/40 text-xs font-bold">Apply Heat (Simulate 1828 Experiment)</button>
        <p id="sim6Status" class="text-[11px] text-slate-400">Heating inorganic ammonium cyanate produced organic urea, permanently disproving the vital force theory!</p>
    </div>
</div>
''',

    7: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Hydrocarbon Saturation & Bromine Water Test</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="testBromine('ethane')" id="sim7BtnEthane" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Ethane (Saturated C2H6)</button>
            <button onclick="testBromine('ethene')" id="sim7BtnEthene" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Ethene (Unsaturated C2H4)</button>
        </div>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-center justify-around gap-4">
        <svg viewBox="0 0 100 110" class="w-24 h-26">
            <rect x="30" y="15" width="40" height="85" rx="5" fill="#0f172a" stroke="#64748b"/>
            <!-- Liquid Bromine Solution -->
            <rect id="sim7BrLiquid" x="32" y="45" width="36" height="53" fill="#b91c1c" fill-opacity="0.6" class="transition-colors duration-700"/>
        </svg>
        <div class="space-y-1 text-center sm:text-left text-xs">
            <span id="sim7Title" class="font-bold text-amber-300 block">Saturated Alkane: Ethane (C2H6)</span>
            <p id="sim7Desc" class="text-slate-300">No double bond. Bromine water remains reddish-brown; no addition reaction occurs.</p>
            <div id="sim7Eq" class="p-1.5 bg-slate-900 rounded font-mono text-[10px] text-slate-400">
                C2H6 + Br2 → No reaction (in dark)
            </div>
        </div>
    </div>
</div>
''',

    8: '''
<div class="sim-container p-4 bg-slate-900 rounded-2xl border border-slate-800 text-slate-200">
    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
        <h4 class="text-sm font-bold text-amber-400">Chains, Branches & Rings: Butane Isomers & Benzene</h4>
        <div class="flex gap-1.5 text-xs">
            <button onclick="setSim8Model('nbutane')" id="sim8BtnNBut" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">n-Butane</button>
            <button onclick="setSim8Model('isobutane')" id="sim8BtnIso" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Isobutane</button>
            <button onclick="setSim8Model('benzene')" id="sim8BtnBen" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold">Benzene Ring</button>
        </div>
    </div>

    <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-center space-y-2">
        <div id="sim8FormulaBox" class="font-mono text-sm text-amber-300">
            CH3 – CH2 – CH2 – CH3
        </div>
        <p id="sim8Desc" class="text-xs text-slate-300">Normal Butane: straight 4-carbon chain (Formula C4H10, bp 273 K / 0°C).</p>
        <span id="sim8Note" class="text-[11px] text-slate-400 block">Structural isomers have identical molecular formula but different atom connectivity.</span>
    </div>
</div>
'''
}
