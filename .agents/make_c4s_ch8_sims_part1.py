# make_c4s_ch8_sims_part1.py
# Bespoke interactive simulators 1 to 8 for Chapter 8: How Things are Made

simulators_part1 = {}

# SIM 1: Tree To Paper Source Explorer
simulators_part1["sim-1"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-emerald-300">Tree To Paper Source Explorer</h4>
            </div>
            <span class="text-xs bg-emerald-500/20 text-emerald-300 px-2.5 py-1 rounded-full font-medium border border-emerald-500/30">Plant Cellulose Origin</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="window.setPaperSourceItem('notebook')" id="src-notebook" class="src-item-btn active p-2.5 rounded-xl border border-emerald-500/60 bg-emerald-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">📓</span>
                <span class="text-xs font-semibold text-emerald-200">Writing Notebook</span>
            </button>
            <button onclick="window.setPaperSourceItem('newspaper')" id="src-newspaper" class="src-item-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">📰</span>
                <span class="text-xs font-semibold text-slate-300">Daily Newspaper</span>
            </button>
            <button onclick="window.setPaperSourceItem('napkin')" id="src-napkin" class="src-item-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🧻</span>
                <span class="text-xs font-semibold text-slate-300">Paper Napkin</span>
            </button>
            <button onclick="window.setPaperSourceItem('box')" id="src-box" class="src-item-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">📦</span>
                <span class="text-xs font-semibold text-slate-300">Shipping Box</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="treeSourceSvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <!-- Living Forest Tree on left -->
                <g id="forestTreeGroup">
                    <rect x="50" y="90" width="20" height="70" fill="#78350f" rx="3" />
                    <!-- Crown -->
                    <circle cx="60" cy="80" r="35" fill="#15803d" />
                    <circle cx="45" cy="65" r="25" fill="#16a34a" />
                    <circle cx="75" cy="65" r="25" fill="#16a34a" />
                    <text x="35" y="172" fill="#86efac" font-size="10" font-weight="bold">Forest Tree</text>
                </g>

                <!-- Connecting Flow Arrow -->
                <path d="M90,100 L130,100" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4 2" marker-end="url(#arrow)" />
                <text x="96" y="92" fill="#7dd3fc" font-size="8">Cellulose</text>

                <!-- Wood Fiber Magnifier in center -->
                <g id="fiberMagnifierGroup">
                    <circle cx="160" cy="100" r="28" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5" />
                    <!-- Entangled plant fibers -->
                    <path d="M142,90 Q160,110 178,92" stroke="#fef08a" stroke-width="2" fill="none" />
                    <path d="M145,108 Q160,88 175,105" stroke="#fef08a" stroke-width="2" fill="none" />
                    <path d="M152,85 Q165,115 168,115" stroke="#fef08a" stroke-width="2" fill="none" />
                    <text x="135" y="142" fill="#bae6fd" font-size="9" font-weight="bold">Plant Fibers</text>
                </g>

                <!-- Connecting Flow Arrow 2 -->
                <path d="M192,100 L232,100" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4 2" />
                <text x="198" y="92" fill="#7dd3fc" font-size="8">Pulping</text>

                <!-- Selected Product Display on right -->
                <g id="productGraphicGroup">
                    <rect id="productBoxSvg" x="240" y="70" width="55" height="60" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="2" />
                    <text id="productIconSvg" x="252" y="105" font-size="24">📓</text>
                    <text id="productLabelSvg" x="238" y="146" fill="#6ee7b7" font-size="9" font-weight="bold">Notebook</text>
                </g>
            </svg>
            <div id="sourceExplText" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-700/60">
                School Notebook: Made from chemically refined, bleached wood pulp from forest trees.
            </div>
        </div>

        <div class="p-3 bg-slate-950/60 rounded-xl border border-slate-800 text-xs text-slate-300 flex items-center justify-between">
            <span>Trees felled globally per day for paper: <strong class="text-rose-400">Over 2.4 Million</strong></span>
            <span class="text-emerald-400 font-bold">100% Recyclable</span>
        </div>
    </div>
"""

# SIM 2: Paper Surface Texture Microscope
simulators_part1["sim-2"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-cyan-300">Paper Surface Texture Microscope</h4>
            </div>
            <span class="text-xs bg-cyan-500/20 text-cyan-300 px-2.5 py-1 rounded-full font-medium border border-cyan-500/30">Microscopic Topography</span>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.setTextureSample('virgin')" id="tex-virgin" class="tex-btn active p-2.5 rounded-xl border border-cyan-500/60 bg-cyan-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">📄</span>
                <span class="text-xs font-semibold text-cyan-200">1. Virgin Factory Paper</span>
                <span class="text-[10px] text-slate-400">Smooth & Calendered</span>
            </button>
            <button onclick="window.setTextureSample('recycled')" id="tex-recycled" class="tex-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">📜</span>
                <span class="text-xs font-semibold text-slate-300">2. Handmade Recycled Paper</span>
                <span class="text-[10px] text-slate-400">Rough & Fibrous Ridges</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <!-- Simulated Microscope Lens Viewport -->
            <div class="relative w-48 h-48 rounded-full border-4 border-cyan-500/50 overflow-hidden bg-slate-950 flex items-center justify-center shadow-inner">
                <svg id="microscopeViewSvg" class="w-full h-full" viewBox="0 0 160 160">
                    <!-- Default Virgin Smooth Paper under lens -->
                    <g id="microscopeSampleGroup">
                        <rect x="0" y="0" width="160" height="160" fill="#f8fafc" />
                        <line x1="10" y1="30" x2="150" y2="30" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4" />
                        <line x1="20" y1="80" x2="140" y2="80" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="6 3" />
                        <line x1="15" y1="130" x2="145" y2="130" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="5 5" />
                        <circle cx="80" cy="80" r="6" fill="#94a3b8" opacity="0.4" />
                    </g>
                    <!-- Lens crosshairs -->
                    <line x1="80" y1="0" x2="80" y2="160" stroke="#0ea5e9" stroke-width="1" stroke-opacity="0.4" />
                    <line x1="0" y1="80" x2="160" y2="80" stroke="#0ea5e9" stroke-width="1" stroke-opacity="0.4" />
                    <circle cx="80" cy="80" r="50" fill="none" stroke="#0ea5e9" stroke-width="1" stroke-opacity="0.3" />
                </svg>
            </div>
            <div id="textureReadoutBadge" class="mt-3 text-xs font-semibold px-3 py-1 rounded-full bg-cyan-950/80 text-cyan-300 border border-cyan-700/60">
                Smooth Texture: Mineral kaolin coating and heavy factory rollers seal fiber pores.
            </div>
        </div>

        <div class="flex flex-col gap-2">
            <div class="flex items-center justify-between text-xs text-slate-400">
                <span>Microscope Zoom Magnification:</span>
                <span id="zoomLevelText" class="font-bold text-cyan-300">100x</span>
            </div>
            <input type="range" id="microZoomSlider" min="20" max="400" step="20" value="100" oninput="window.updateMicroscopeZoom(this.value)" class="w-full accent-cyan-400 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-500">
                <span>20x (Hand Lens)</span>
                <span>100x (Cellulose Mesh)</span>
                <span>400x (Microfibril Chains)</span>
            </div>
        </div>
    </div>
"""

# SIM 3: Paper Shredding & Fiber Release Lab
simulators_part1["sim-3"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-amber-300">Paper Shredding & Fiber Release Lab</h4>
            </div>
            <span class="text-xs bg-amber-500/20 text-amber-300 px-2.5 py-1 rounded-full font-medium border border-amber-500/30">Mechanical Tearing</span>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.setTearDirection('grain')" id="tear-grain" class="tear-btn active p-2.5 rounded-xl border border-amber-500/60 bg-amber-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">↕️</span>
                <span class="text-xs font-semibold text-amber-200">With The Grain</span>
                <span class="text-[10px] text-slate-400">Clean, Easy Straight Rip</span>
            </button>
            <button onclick="window.setTearDirection('cross')" id="tear-cross" class="tear-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">↔️</span>
                <span class="text-xs font-semibold text-slate-300">Across The Grain</span>
                <span class="text-[10px] text-slate-400">Resistant, Jagged Tear</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="shredLabSvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <!-- Newspaper Sheet Graphic -->
                <g id="tearSheetGroup">
                    <!-- Left torn half -->
                    <polygon id="tearLeftHalf" points="50,30 145,30 148,80 144,130 147,150 50,150" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" style="transition: transform 0.4s ease;" />
                    <line x1="60" y1="50" x2="135" y2="50" stroke="#64748b" stroke-width="2" />
                    <line x1="60" y1="70" x2="130" y2="70" stroke="#64748b" stroke-width="2" />
                    <line x1="60" y1="90" x2="135" y2="90" stroke="#64748b" stroke-width="2" />
                    <line x1="60" y1="110" x2="125" y2="110" stroke="#64748b" stroke-width="2" />

                    <!-- Right torn half -->
                    <polygon id="tearRightHalf" points="165,30 260,30 260,150 167,150 164,130 168,80 165,30" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" style="transition: transform 0.4s ease;" />
                    <line x1="175" y1="50" x2="250" y2="50" stroke="#64748b" stroke-width="2" />
                    <line x1="175" y1="70" x2="245" y2="70" stroke="#64748b" stroke-width="2" />
                    <line x1="175" y1="90" x2="250" y2="90" stroke="#64748b" stroke-width="2" />
                    <line x1="175" y1="110" x2="240" y2="110" stroke="#64748b" stroke-width="2" />

                    <!-- Exposed Fiber Fringes between halves -->
                    <g id="fiberFringesGroup">
                        <line x1="147" y1="40" x2="166" y2="42" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2 1" />
                        <line x1="148" y1="65" x2="167" y2="68" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2 1" />
                        <line x1="145" y1="95" x2="165" y2="93" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2 1" />
                        <line x1="147" y1="125" x2="166" y2="128" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2 1" />
                    </g>
                </g>
            </svg>
            <div id="tearStatusText" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700">
                Tear Result: Pulling along the grain splits parallel fibers cleanly!
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.performTearAction()" class="py-2.5 px-4 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm flex items-center justify-center gap-2">
                <span>✂️</span> Pull & Tear Paper
            </button>
            <button onclick="window.resetTearAction()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Reset Sheet
            </button>
        </div>
    </div>
"""

# SIM 4: Methi Seed Mucilage Binding Engine
simulators_part1["sim-4"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-500 animate-pulse"></span>
                <h4 class="font-bold text-base text-amber-300">Methi Seed Mucilage Binding Engine</h4>
            </div>
            <span class="text-xs bg-amber-500/20 text-amber-300 px-2.5 py-1 rounded-full font-medium border border-amber-500/30">Natural Botanical Glue</span>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="methiSoakSvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <!-- Glass Soaking Beaker -->
                <rect x="70" y="40" width="100" height="120" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="2" />
                <rect id="beakerLiquid" x="72" y="70" width="96" height="88" fill="#0284c7" fill-opacity="0.3" />

                <!-- Golden Methi Seeds resting in liquid -->
                <g id="methiSeedsGroup">
                    <circle cx="95" cy="145" r="4.5" fill="#d97706" stroke="#f59e0b" stroke-width="1" />
                    <circle cx="110" cy="148" r="4.5" fill="#d97706" stroke="#f59e0b" stroke-width="1" />
                    <circle cx="125" cy="144" r="4.5" fill="#d97706" stroke="#f59e0b" stroke-width="1" />
                    <circle cx="140" cy="147" r="4.5" fill="#d97706" stroke="#f59e0b" stroke-width="1" />
                    <circle cx="102" cy="138" r="4.5" fill="#d97706" stroke="#f59e0b" stroke-width="1" />
                    <circle cx="118" cy="139" r="4.5" fill="#d97706" stroke="#f59e0b" stroke-width="1" />
                    <circle cx="132" cy="137" r="4.5" fill="#d97706" stroke="#f59e0b" stroke-width="1" />
                </g>

                <!-- Mucilage Gel Halos (expand as soaked) -->
                <g id="mucilageHalosGroup" opacity="0.3">
                    <circle cx="95" cy="145" r="10" fill="#fef08a" opacity="0.3" />
                    <circle cx="118" cy="139" r="12" fill="#fef08a" opacity="0.3" />
                    <circle cx="132" cy="137" r="11" fill="#fef08a" opacity="0.3" />
                </g>

                <!-- Tensile Strength Gauge on Right -->
                <g id="strengthMeterGroup">
                    <rect x="200" y="45" width="90" height="110" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2" />
                    <text x="212" y="65" fill="#94a3b8" font-size="9" font-weight="bold">Paper Strength</text>
                    <!-- Progress Bar -->
                    <rect x="215" y="75" width="60" height="16" rx="4" fill="#0f172a" />
                    <rect id="strengthBarElem" x="215" y="75" width="15" height="16" rx="4" fill="#eab308" style="transition: width 0.4s ease;" />
                    <text id="strengthValText" x="225" y="115" fill="#fef08a" font-size="12" font-weight="bold">Low (Crumbly)</text>
                    <text x="215" y="135" fill="#64748b" font-size="8">Without Methi Glue</text>
                </g>
            </svg>

            <div class="flex items-center justify-between w-full max-w-md mt-2 text-xs font-semibold px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800">
                <span class="text-amber-300">Soak Time: <span id="methiHoursLabel">0 Hours</span></span>
                <span class="text-slate-400">Mucilage Viscosity: <span id="viscosityLabel" class="text-cyan-400">Watery</span></span>
                <span class="text-emerald-400">Sheet Integrity: <span id="integrityLabel">Fragile</span></span>
            </div>
        </div>

        <div class="grid grid-cols-3 gap-2">
            <button onclick="window.setMethiSoak(0)" id="soak-0" class="methi-soak-btn active py-2 rounded-xl border border-amber-500/60 bg-amber-950/40 text-xs font-semibold text-amber-200">
                ⏳ 0 Hours (No Soak)
            </button>
            <button onclick="window.setMethiSoak(6)" id="soak-6" class="methi-soak-btn py-2 rounded-xl border border-slate-700 bg-slate-800/40 text-xs font-semibold text-slate-300">
                ⏳ 6 Hours (Moderate)
            </button>
            <button onclick="window.setMethiSoak(12)" id="soak-12" class="methi-soak-btn py-2 rounded-xl border border-slate-700 bg-slate-800/40 text-xs font-semibold text-slate-300">
                ⏳ 12 Hours (Optimal Gel)
            </button>
        </div>
    </div>
"""

# SIM 5: Pulp Mashing & Consistency Tank
simulators_part1["sim-5"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-blue-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-blue-300">Pulp Mashing & Consistency Tank</h4>
            </div>
            <span class="text-xs bg-blue-500/20 text-blue-300 px-2.5 py-1 rounded-full font-medium border border-blue-500/30">Slurry Homogenization</span>
        </div>

        <div class="grid grid-cols-3 gap-2">
            <button onclick="window.setPulpSlurryMode('thick')" id="slurry-thick" class="slurry-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">🥣</span>
                <span class="text-xs font-semibold text-slate-300">Too Thick (Doughy)</span>
                <span class="text-[10px] text-rose-400">Lumpy, Thick Sheet</span>
            </button>
            <button onclick="window.setPulpSlurryMode('optimal')" id="slurry-optimal" class="slurry-btn active p-2 rounded-xl border border-blue-500/60 bg-blue-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">🍲</span>
                <span class="text-xs font-semibold text-blue-200">Optimal (Soupy)</span>
                <span class="text-[10px] text-emerald-400">Smooth, Uniform Mat</span>
            </button>
            <button onclick="window.setPulpSlurryMode('watery')" id="slurry-watery" class="slurry-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">💧</span>
                <span class="text-xs font-semibold text-slate-300">Too Watery</span>
                <span class="text-[10px] text-amber-400">Fragile, Gaps & Holes</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="pulpTankSvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <!-- Vat outline -->
                <rect x="40" y="30" width="240" height="130" rx="8" fill="#0f172a" stroke="#3b82f6" stroke-width="2" />
                <rect id="vatFluidElem" x="42" y="60" width="236" height="98" fill="#1e3a8a" fill-opacity="0.4" />

                <!-- Dispersed Fiber Particles in slurry -->
                <g id="slurryFibersGroup">
                    <!-- Dynamic fibers drawn via JS -->
                </g>

                <!-- Mechanical Blender / Pestle Agitator in center -->
                <g id="blenderShaft" style="transform-origin: 160px 40px;">
                    <rect x="157" y="10" width="6" height="85" fill="#94a3b8" />
                    <!-- Blender blades -->
                    <polygon points="140,95 180,95 160,88" fill="#cbd5e1" />
                </g>
            </svg>
            <div id="slurryOutcomeText" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-700/60">
                Optimal Consistency: Fibers float freely, ready to form an even, continuous sheet!
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.stirPulpBlender()" class="py-2.5 px-4 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm flex items-center justify-center gap-2">
                <span>🔄</span> Stir & Mash Pulp Slurry
            </button>
            <button onclick="window.stopPulpBlender()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Stop Agitator
            </button>
        </div>
    </div>
"""

# SIM 6: Mesh Screen Deckle & Water Press Lab
simulators_part1["sim-6"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-teal-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-teal-300">Mesh Screen Deckle & Water Press Lab</h4>
            </div>
            <span class="text-xs bg-teal-500/20 text-teal-300 px-2.5 py-1 rounded-full font-medium border border-teal-500/30">Dewatering & Couching</span>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="screenPressSvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <!-- Water basin -->
                <rect x="30" y="80" width="260" height="90" fill="#0284c7" fill-opacity="0.3" rx="4" />
                <line x1="30" y1="80" x2="290" y2="80" stroke="#38bdf8" stroke-width="2" />
                <text x="40" y="72" fill="#7dd3fc" font-size="9" font-weight="bold">Water Basin</text>

                <!-- Mold and Deckle Assembly (moves up and down) -->
                <g id="deckleFrameGroup" style="transform: translateY(0px); transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);">
                    <!-- Wooden Frame -->
                    <rect x="90" y="70" width="140" height="15" rx="3" fill="#b45309" stroke="#78350f" stroke-width="2" />
                    <!-- Wire Mesh Screen -->
                    <line x1="95" y1="78" x2="225" y2="78" stroke="#f8fafc" stroke-width="2" stroke-dasharray="4 2" />
                    <!-- Caught Wet Paper Mat on top -->
                    <rect id="wetMatOnMesh" x="98" y="72" width="124" height="6" fill="#e2e8f0" opacity="0" style="transition: opacity 0.4s ease;" />
                </g>

                <!-- Water Drainage Droplets -->
                <g id="drainingDropsGroup" opacity="0">
                    <circle cx="120" cy="95" r="2.5" fill="#38bdf8" />
                    <circle cx="150" cy="105" r="2.5" fill="#38bdf8" />
                    <circle cx="180" cy="98" r="2.5" fill="#38bdf8" />
                    <circle cx="210" cy="102" r="2.5" fill="#38bdf8" />
                </g>
            </svg>

            <!-- Moisture Gauge -->
            <div class="w-full max-w-md mt-2">
                <div class="flex justify-between text-xs mb-1">
                    <span class="text-slate-400">Sheet Moisture Content:</span>
                    <span id="moisturePctLabel" class="font-bold text-cyan-400">100% (Submerged)</span>
                </div>
                <div class="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
                    <div id="moistureBarElem" class="h-full bg-cyan-500 transition-all duration-300" style="width: 100%;"></div>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-3 gap-2">
            <button onclick="window.submergeDeckle()" id="step-submerge" class="press-step-btn active py-2 rounded-xl border border-teal-500/60 bg-teal-950/40 text-xs font-semibold text-teal-200">
                1. Dip In Basin
            </button>
            <button onclick="window.liftDeckle()" id="step-lift" class="press-step-btn py-2 rounded-xl border border-slate-700 bg-slate-800/40 text-xs font-semibold text-slate-300">
                2. Lift & Drain
            </button>
            <button onclick="window.pressSponge()" id="step-press" class="press-step-btn py-2 rounded-xl border border-slate-700 bg-slate-800/40 text-xs font-semibold text-slate-300">
                3. Sponge Press
            </button>
        </div>
    </div>
"""

# SIM 7: Botanical Dye Extraction Chamber
simulators_part1["sim-7"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-yellow-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-yellow-300">Botanical Dye Extraction Chamber</h4>
            </div>
            <span class="text-xs bg-yellow-500/20 text-yellow-300 px-2.5 py-1 rounded-full font-medium border border-yellow-500/30">Plant Pigments & pH Test</span>
        </div>

        <div class="grid grid-cols-3 gap-2">
            <button onclick="window.selectBotanicalDye('turmeric')" id="dye-turmeric" class="botanical-dye-btn active p-2 rounded-xl border border-yellow-500/60 bg-yellow-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🟡</span>
                <span class="text-xs font-semibold text-yellow-200">Turmeric (Haldi)</span>
                <span class="text-[10px] text-slate-400">Curcumin (Yellow)</span>
            </button>
            <button onclick="window.selectBotanicalDye('beetroot')" id="dye-beetroot" class="botanical-dye-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🔴</span>
                <span class="text-xs font-semibold text-slate-300">Beetroot</span>
                <span class="text-[10px] text-slate-400">Betalain (Ruby)</span>
            </button>
            <button onclick="window.selectBotanicalDye('spinach')" id="dye-spinach" class="botanical-dye-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🟢</span>
                <span class="text-xs font-semibold text-slate-300">Spinach (Palak)</span>
                <span class="text-[10px] text-slate-400">Chlorophyll (Green)</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="botanicalSvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <!-- Dye Flask on Left -->
                <rect x="50" y="60" width="80" height="95" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="2" />
                <rect id="flaskFluid" x="52" y="85" width="76" height="68" fill="#eab308" fill-opacity="0.8" style="transition: fill 0.4s ease;" />
                <text x="60" y="52" fill="#cbd5e1" font-size="9" font-weight="bold">Plant Extract</text>

                <!-- Flow arrow -->
                <path d="M140,110 L180,110" stroke="#94a3b8" stroke-width="2" stroke-dasharray="3 2" />

                <!-- Dyed Paper Sheet Sample on Right -->
                <rect id="tintedPaperSheet" x="190" y="45" width="90" height="110" rx="4" fill="#fef08a" stroke="#d97706" stroke-width="2" style="transition: fill 0.4s ease;" />
                <text x="205" y="105" fill="#78350f" font-size="11" font-weight="bold">Tinted Paper</text>
            </svg>

            <div id="dyeScientificReadout" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-yellow-950/80 text-yellow-300 border border-yellow-700/60">
                Curcumin Pigment: Brilliant golden-yellow dye harvested from organic turmeric rhizomes.
            </div>
        </div>

        <!-- pH Indicator Magic Button (Only applies to Turmeric) -->
        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.addAlkalineSoap()" id="alkalineBtn" class="py-2.5 px-4 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded-xl shadow-lg transition-all text-xs flex items-center justify-center gap-1.5">
                <span>🧼</span> Add Baking Soda (Alkaline pH Shift)
            </button>
            <button onclick="window.resetBotanicalDye()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-xs font-medium">
                Reset Plant Dye
            </button>
        </div>
    </div>
"""

# SIM 8: Greeting Card Upcycling Workshop
simulators_part1["sim-8"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-rose-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-rose-300">Greeting Card Upcycling Workshop</h4>
            </div>
            <span class="text-xs bg-rose-500/20 text-rose-300 px-2.5 py-1 rounded-full font-medium border border-rose-500/30">Mindful Crafting</span>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <!-- Folded Card Canvas -->
            <svg id="greetingCardSvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <!-- Card Base (Recycled paper texture) -->
                <rect x="70" y="20" width="180" height="140" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="3" />
                <line x1="160" y1="20" x2="160" y2="160" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3 3" />

                <!-- Embellishments Group -->
                <g id="cardEmbellishmentsGroup">
                    <!-- Leaf / flower element (toggleable) -->
                    <path id="cardLeafElem" d="M100,50 Q120,40 130,60 Q110,80 100,50 Z" fill="#15803d" opacity="0" />
                    <!-- Twine Bow -->
                    <circle id="cardBowElem" cx="160" cy="35" r="6" fill="#78350f" opacity="0" />
                </g>

                <!-- Heartfelt message on right side -->
                <text x="175" y="60" fill="#92400e" font-size="11" font-weight="bold">Thank You!</text>
                <text x="175" y="80" fill="#78350f" font-size="8">Crafted with Love</text>
                <text x="175" y="95" fill="#78350f" font-size="8">& 100% Recycled Paper</text>
                <text x="175" y="130" fill="#059669" font-size="9" font-weight="bold">🌿 Zero Waste Gift</text>
            </svg>

            <div id="cardStatusBadge" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-rose-950/80 text-rose-300 border border-rose-700/60">
                Handmade Card: Blank folded recycled sheet ready for botanical embellishments!
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.addCardEmbellishment('leaf')" class="py-2.5 px-4 bg-rose-600 hover:bg-rose-500 text-white font-bold rounded-xl shadow-lg transition-all text-xs flex items-center justify-center gap-1.5">
                <span>🍃</span> Add Pressed Green Leaf
            </button>
            <button onclick="window.addCardEmbellishment('twine')" class="py-2.5 px-4 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded-xl shadow-lg transition-all text-xs flex items-center justify-center gap-1.5">
                <span>🧵</span> Add Natural Jute Twine Bow
            </button>
        </div>
    </div>
"""

