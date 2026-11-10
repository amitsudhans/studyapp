# make_c4s_ch8_sims_part2.py
# Bespoke interactive simulators 9 to 16 for Chapter 8: How Things are Made

simulators_part2 = {}

# SIM 9: Industrial Paper Mill Process Flow
simulators_part2["sim-9"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-indigo-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-indigo-300">Industrial Paper Mill Process Flow</h4>
            </div>
            <span class="text-xs bg-indigo-500/20 text-indigo-300 px-2.5 py-1 rounded-full font-medium border border-indigo-500/30">Fourdrinier Machine</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="window.setMillStage(0)" id="mill-stage-0" class="mill-stage-btn active p-2 rounded-xl border border-indigo-500/60 bg-indigo-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">🪵</span>
                <span class="text-xs font-semibold text-indigo-200">1. Debark & Chip</span>
            </button>
            <button onclick="window.setMillStage(1)" id="mill-stage-1" class="mill-stage-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">♨️</span>
                <span class="text-xs font-semibold text-slate-300">2. Digester Cook</span>
            </button>
            <button onclick="window.setMillStage(2)" id="mill-stage-2" class="mill-stage-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">🌊</span>
                <span class="text-xs font-semibold text-slate-300">3. Wire Web Spray</span>
            </button>
            <button onclick="window.setMillStage(3)" id="mill-stage-3" class="mill-stage-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">🗞️</span>
                <span class="text-xs font-semibold text-slate-300">4. Heated Rollers</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="millProcessSvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <!-- Factory Base -->
                <rect x="20" y="140" width="280" height="20" fill="#1e293b" rx="3" />

                <!-- Stage 1: Chipper / Log -->
                <g id="millGraphicLogs" opacity="1">
                    <rect x="35" y="100" width="40" height="15" rx="3" fill="#92400e" stroke="#78350f" stroke-width="1.5" />
                    <rect x="40" y="80" width="40" height="15" rx="3" fill="#92400e" stroke="#78350f" stroke-width="1.5" />
                    <!-- Chipper blade -->
                    <circle cx="95" cy="100" r="14" fill="#64748b" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="4 2" />
                    <text x="32" y="132" fill="#94a3b8" font-size="8">Chipping</text>
                </g>

                <!-- Stage 2: Digester Vat -->
                <g id="millGraphicDigester" opacity="0.4">
                    <rect x="120" y="55" width="45" height="85" rx="10" fill="#334155" stroke="#94a3b8" stroke-width="2" />
                    <line x1="125" y1="90" x2="160" y2="90" stroke="#f59e0b" stroke-width="2" stroke-dasharray="2 2" />
                    <text x="122" y="50" fill="#f59e0b" font-size="8" font-weight="bold">Steam Vat</text>
                </g>

                <!-- Stage 3 & 4: Fourdrinier Wire and Steam Rollers -->
                <g id="millGraphicRollers" opacity="0.4">
                    <line x1="180" y1="110" x2="280" y2="110" stroke="#f8fafc" stroke-width="4" />
                    <circle cx="200" cy="95" r="12" fill="#475569" stroke="#94a3b8" stroke-width="2" />
                    <circle cx="240" cy="95" r="12" fill="#475569" stroke="#94a3b8" stroke-width="2" />
                    <circle cx="280" cy="95" r="12" fill="#475569" stroke="#94a3b8" stroke-width="2" />
                    <!-- Giant Paper Roll -->
                    <circle cx="285" cy="65" r="20" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" />
                </g>
            </svg>

            <div id="millStageDescBadge" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-indigo-950/80 text-indigo-300 border border-indigo-700/60">
                Stage 1: Tree trunks are mechanically debarked and sliced into small wood chips.
            </div>
        </div>

        <div class="flex items-center justify-between text-xs px-2 text-slate-400">
            <span>Water per Ton: <strong class="text-cyan-400">Up to 50,000 Liters</strong></span>
            <span>Energy: <strong class="text-amber-400">High Steam & Electricity</strong></span>
        </div>
    </div>
"""

# SIM 10: Ancient Writing Surfaces Interactive Museum
simulators_part2["sim-10"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-amber-300">Ancient Writing Surfaces Interactive Museum</h4>
            </div>
            <span class="text-xs bg-amber-500/20 text-amber-300 px-2.5 py-1 rounded-full font-medium border border-amber-500/30">Historical Indian Media</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="window.selectAncientSurface('talapatra')" id="surf-talapatra" class="ancient-surf-btn active p-2.5 rounded-xl border border-amber-500/60 bg-amber-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🌴</span>
                <span class="text-xs font-semibold text-amber-200">Talapatra</span>
                <span class="text-[10px] text-slate-400">Palm Leaf</span>
            </button>
            <button onclick="window.selectAncientSurface('bhojpatra')" id="surf-bhojpatra" class="ancient-surf-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🌳</span>
                <span class="text-xs font-semibold text-slate-300">Bhojpatra</span>
                <span class="text-[10px] text-slate-400">Birch Bark</span>
            </button>
            <button onclick="window.selectAncientSurface('phalka')" id="surf-phalka" class="ancient-surf-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🪵</span>
                <span class="text-xs font-semibold text-slate-300">Phalka</span>
                <span class="text-[10px] text-slate-400">Wooden Board</span>
            </button>
            <button onclick="window.selectAncientSurface('pata')" id="surf-pata" class="ancient-surf-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🧵</span>
                <span class="text-xs font-semibold text-slate-300">Pata</span>
                <span class="text-[10px] text-slate-400">Starched Cloth</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="ancientMuseumSvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <!-- Manuscript Display Board -->
                <rect x="40" y="30" width="240" height="120" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="2" />

                <!-- Dynamic Ancient Surface Graphic -->
                <g id="ancientSurfaceDisplayGroup">
                    <!-- Talapatra long strip by default -->
                    <rect x="60" y="55" width="200" height="45" rx="3" fill="#d97706" stroke="#92400e" stroke-width="2" />
                    <circle cx="85" cy="77" r="4" fill="#0f172a" />
                    <circle cx="235" cy="77" r="4" fill="#0f172a" />
                    <!-- Ancient inscribed script lines -->
                    <line x1="100" y1="68" x2="220" y2="68" stroke="#451a03" stroke-width="2" stroke-dasharray="6 3" />
                    <line x1="100" y1="85" x2="220" y2="85" stroke="#451a03" stroke-width="2" stroke-dasharray="5 2" />
                    <!-- Metal Stylus Tool -->
                    <line x1="245" y1="40" x2="215" y2="70" stroke="#94a3b8" stroke-width="3" stroke-linecap="round" />
                    <circle cx="215" cy="70" r="2" fill="#ef4444" />
                </g>
            </svg>
            <div id="ancientSurfaceReadout" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-amber-950/80 text-amber-300 border border-amber-700/60">
                Talapatra: Seasoned palm leaves inscribed with an iron stylus and highlighted with lampblack soot.
            </div>
        </div>
    </div>
"""

# SIM 11: Banana Stem Fiber Extraction Lab
simulators_part2["sim-11"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-emerald-300">Banana Stem Fiber Extraction Lab</h4>
            </div>
            <span class="text-xs bg-emerald-500/20 text-emerald-300 px-2.5 py-1 rounded-full font-medium border border-emerald-500/30">Tree-Free Agricultural Fiber</span>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="bananaStemSvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <!-- Banana Pseudostem Stalk Entering Left -->
                <g id="bananaStalkGraphic" style="transform: translateX(0px); transition: transform 0.6s ease;">
                    <rect x="25" y="75" width="90" height="30" rx="6" fill="#15803d" stroke="#166534" stroke-width="2" />
                    <ellipse cx="25" cy="90" rx="8" ry="15" fill="#16a34a" />
                    <text x="35" y="94" fill="#bbf7d0" font-size="9" font-weight="bold">Banana Stalk</text>
                </g>

                <!-- Decorticator Mechanical Rollers in Center -->
                <g id="decorticatorRollers">
                    <circle cx="150" cy="70" r="16" fill="#475569" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4 2" />
                    <circle cx="150" cy="110" r="16" fill="#475569" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4 2" />
                    <!-- Motor teeth -->
                    <circle cx="150" cy="70" r="4" fill="#cbd5e1" />
                    <circle cx="150" cy="110" r="4" fill="#cbd5e1" />
                </g>

                <!-- Extracted Glistening Fibers Exiting Right -->
                <g id="extractedFibersGraphic" opacity="0.2" style="transition: opacity 0.5s ease;">
                    <line x1="170" y1="80" x2="280" y2="80" stroke="#fef08a" stroke-width="2" stroke-dasharray="5 2" />
                    <line x1="170" y1="88" x2="285" y2="88" stroke="#fef08a" stroke-width="2.5" />
                    <line x1="170" y1="96" x2="280" y2="96" stroke="#fef08a" stroke-width="2" stroke-dasharray="4 2" />
                    <line x1="170" y1="104" x2="275" y2="104" stroke="#fef08a" stroke-width="2.5" />
                    <text x="185" y="125" fill="#fef08a" font-size="9" font-weight="bold">Pure Cellulose Strands</text>
                </g>
            </svg>

            <div id="decorticatorStatusText" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700">
                Decorticator Ready: Feed post-harvest banana pseudostem through rollers!
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.runBananaDecorticator()" class="py-2.5 px-4 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm flex items-center justify-center gap-2">
                <span>⚙️</span> Feed Stalk & Extract Fibers
            </button>
            <button onclick="window.resetBananaDecorticator()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Reset Machine
            </button>
        </div>
    </div>
"""

# SIM 12: Paper Thickness & Absorbency Analyzer
simulators_part2["sim-12"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-cyan-300">Paper Thickness & Absorbency Analyzer</h4>
            </div>
            <span class="text-xs bg-cyan-500/20 text-cyan-300 px-2.5 py-1 rounded-full font-medium border border-cyan-500/30">Porosity vs Rigidity</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="window.setPaperGrade('tissue')" id="grade-tissue" class="paper-grade-btn active p-2 rounded-xl border border-cyan-500/60 bg-cyan-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">🧻</span>
                <span class="text-xs font-semibold text-cyan-200">Tissue Paper</span>
                <span class="text-[10px] text-slate-400">18 GSM</span>
            </button>
            <button onclick="window.setPaperGrade('notebook')" id="grade-notebook" class="paper-grade-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">📓</span>
                <span class="text-xs font-semibold text-slate-300">Writing Paper</span>
                <span class="text-[10px] text-slate-400">75 GSM</span>
            </button>
            <button onclick="window.setPaperGrade('cardstock')" id="grade-cardstock" class="paper-grade-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">📜</span>
                <span class="text-xs font-semibold text-slate-300">Cardstock</span>
                <span class="text-[10px] text-slate-400">220 GSM</span>
            </button>
            <button onclick="window.setPaperGrade('corrugated')" id="grade-corrugated" class="paper-grade-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">📦</span>
                <span class="text-xs font-semibold text-slate-300">Corrugated Box</span>
                <span class="text-[10px] text-slate-400">450 GSM</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="gradeAnalyzerSvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <!-- Paper Sample cross-section in center -->
                <rect id="gradeSampleRect" x="60" y="85" width="200" height="10" rx="2" fill="#f8fafc" stroke="#94a3b8" stroke-width="2" style="transition: all 0.4s ease;" />

                <!-- Water Droplet Pipette above -->
                <g id="pipetteDropGroup" style="transform: translateY(0px); transition: transform 0.5s ease;">
                    <polygon points="156,20 164,20 160,35" fill="#38bdf8" />
                    <circle id="waterDroplet" cx="160" cy="45" r="5" fill="#0284c7" />
                </g>

                <!-- Wet capillary spread circle on paper (hidden by default) -->
                <ellipse id="capillarySpreadCircle" cx="160" cy="90" rx="0" ry="0" fill="#38bdf8" fill-opacity="0.6" style="transition: all 0.6s ease;" />
            </svg>

            <div class="flex items-center justify-between w-full max-w-md mt-2 text-xs font-semibold px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800">
                <span class="text-slate-300">Absorption Rate: <span id="absorbRateText" class="text-cyan-400">Instant (0.2s)</span></span>
                <span class="text-slate-300">Crush Strength: <span id="crushStrengthText" class="text-rose-400">Very Low</span></span>
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.dropWaterOnGrade()" class="py-2.5 px-4 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm flex items-center justify-center gap-2">
                <span>💧</span> Release Water Droplet
            </button>
            <button onclick="window.resetGradeTest()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Reset Sample
            </button>
        </div>
    </div>
"""

# SIM 13: Braille Dot Matrix Embossing Lab
simulators_part2["sim-13"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-violet-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-violet-300">Braille Dot Matrix Embossing Lab</h4>
            </div>
            <span class="text-xs bg-violet-500/20 text-violet-300 px-2.5 py-1 rounded-full font-medium border border-violet-500/30">Tactile Literacy</span>
        </div>

        <div class="grid grid-cols-4 gap-2">
            <button onclick="window.setBrailleChar('A')" id="br-char-A" class="braille-char-btn active py-2 rounded-xl border border-violet-500/60 bg-violet-950/40 text-xs font-bold text-violet-200">Letter A (⠁)</button>
            <button onclick="window.setBrailleChar('B')" id="br-char-B" class="braille-char-btn py-2 rounded-xl border border-slate-700 bg-slate-800/40 text-xs font-bold text-slate-300">Letter B (⠃)</button>
            <button onclick="window.setBrailleChar('C')" id="br-char-C" class="braille-char-btn py-2 rounded-xl border border-slate-700 bg-slate-800/40 text-xs font-bold text-slate-300">Letter C (⠉)</button>
            <button onclick="window.setBrailleChar('L')" id="br-char-L" class="braille-char-btn py-2 rounded-xl border border-slate-700 bg-slate-800/40 text-xs font-bold text-slate-300">Letter L (⠇)</button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <!-- 6-Dot Matrix Braille Cell (2 columns x 3 rows) -->
            <svg id="brailleCellSvg" class="w-44 h-48" viewBox="0 0 160 180">
                <!-- Heavy Braille cardstock surface -->
                <rect x="20" y="10" width="120" height="160" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" />

                <!-- Dot 1 (top-left) -->
                <circle id="bdot-1" cx="55" cy="40" r="12" fill="#7c3aed" stroke="#ffffff" stroke-width="2" />
                <text x="52" y="44" fill="#ffffff" font-size="10" font-weight="bold">1</text>

                <!-- Dot 2 (middle-left) -->
                <circle id="bdot-2" cx="55" cy="90" r="12" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" />
                <text x="52" y="94" fill="#64748b" font-size="10" font-weight="bold">2</text>

                <!-- Dot 3 (bottom-left) -->
                <circle id="bdot-3" cx="55" cy="140" r="12" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" />
                <text x="52" y="144" fill="#64748b" font-size="10" font-weight="bold">3</text>

                <!-- Dot 4 (top-right) -->
                <circle id="bdot-4" cx="105" cy="40" r="12" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" />
                <text x="102" y="44" fill="#64748b" font-size="10" font-weight="bold">4</text>

                <!-- Dot 5 (middle-right) -->
                <circle id="bdot-5" cx="105" cy="90" r="12" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" />
                <text x="102" y="94" fill="#64748b" font-size="10" font-weight="bold">5</text>

                <!-- Dot 6 (bottom-right) -->
                <circle id="bdot-6" cx="105" cy="140" r="12" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" />
                <text x="102" y="144" fill="#64748b" font-size="10" font-weight="bold">6</text>
            </svg>

            <div id="brailleMeaningText" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-violet-950/80 text-violet-300 border border-violet-700/60">
                Letter A: Dot 1 embossed. Heavy cardstock fibers stretch into a firm, permanent tactile dome!
            </div>
        </div>

        <div class="p-3 bg-slate-950/60 rounded-xl border border-slate-800 text-xs text-slate-300 text-center">
            Standard Braille Cell: <strong class="text-violet-300">2 Columns × 3 Rows (6-Dot System)</strong> invented by Louis Braille.
        </div>
    </div>
"""

# SIM 14: 5Rs Waste Hierarchy Sorting Machine
simulators_part2["sim-14"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-emerald-300">5Rs Waste Hierarchy Sorting Machine</h4>
            </div>
            <span class="text-xs bg-emerald-500/20 text-emerald-300 px-2.5 py-1 rounded-full font-medium border border-emerald-500/30">Ecological Priorities</span>
        </div>

        <div class="grid grid-cols-3 sm:grid-cols-5 gap-1.5">
            <button onclick="window.select5RAction('refuse')" id="r-refuse" class="r-btn active p-2 rounded-xl border border-emerald-500/60 bg-emerald-950/40 text-center flex flex-col items-center">
                <span class="text-base">🚫</span>
                <span class="text-[11px] font-bold text-emerald-200">1. Refuse</span>
            </button>
            <button onclick="window.select5RAction('reduce')" id="r-reduce" class="r-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center">
                <span class="text-base">📉</span>
                <span class="text-[11px] font-bold text-slate-300">2. Reduce</span>
            </button>
            <button onclick="window.select5RAction('reuse')" id="r-reuse" class="r-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center">
                <span class="text-base">🔁</span>
                <span class="text-[11px] font-bold text-slate-300">3. Reuse</span>
            </button>
            <button onclick="window.select5RAction('repurpose')" id="r-repurpose" class="r-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center">
                <span class="text-base">🎨</span>
                <span class="text-[11px] font-bold text-slate-300">4. Repurpose</span>
            </button>
            <button onclick="window.select5RAction('recycle')" id="r-recycle" class="r-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center">
                <span class="text-base">♻️</span>
                <span class="text-[11px] font-bold text-slate-300">5. Recycle</span>
            </button>
        </div>

        <div class="p-4 bg-slate-950/90 rounded-xl border border-slate-800 flex flex-col gap-2 min-h-[160px] justify-center">
            <div class="flex items-center gap-2">
                <span id="rIcon" class="text-3xl">🚫</span>
                <div>
                    <h5 id="rTitle" class="text-sm font-bold text-emerald-300">Refuse: Stop Waste at the Source</h5>
                    <p id="rSubtitle" class="text-xs text-slate-400">Say NO to single-use plastics and unnecessary disposables</p>
                </div>
            </div>
            <p id="rExample" class="text-xs text-slate-300 bg-slate-900/80 p-2.5 rounded-lg border border-slate-800">
                Example: Politely decline plastic drinking straws, disposable plastic cups, and plastic gift wrap wrappers at shops.
            </p>
        </div>
    </div>
"""

# SIM 15: Kinetic Newspaper Toy Workshop
simulators_part2["sim-15"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-pink-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-pink-300">Kinetic Newspaper Toy Workshop</h4>
            </div>
            <span class="text-xs bg-pink-500/20 text-pink-300 px-2.5 py-1 rounded-full font-medium border border-pink-500/30">Origami Engineering</span>
        </div>

        <div class="grid grid-cols-3 gap-2">
            <button onclick="window.setKineticToy('butterfly')" id="toy-butterfly" class="kinetic-toy-btn active p-2.5 rounded-xl border border-pink-500/60 bg-pink-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🦋</span>
                <span class="text-xs font-semibold text-pink-200">Flapping Butterfly</span>
            </button>
            <button onclick="window.setKineticToy('dancer')" id="toy-dancer" class="kinetic-toy-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">💃</span>
                <span class="text-xs font-semibold text-slate-300">Balancing Dancer</span>
            </button>
            <button onclick="window.setKineticToy('glider')" id="toy-glider" class="kinetic-toy-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🦅</span>
                <span class="text-xs font-semibold text-slate-300">Aerodynamic Glider</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="kineticToySvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <!-- Butterfly Wings (default) -->
                <g id="butterflyToyGroup">
                    <!-- Left wing (animated rotation) -->
                    <path id="bLeftWing" d="M160,90 C120,40 80,60 90,110 C95,130 140,120 160,90 Z" fill="#ec4899" stroke="#fbcfe8" stroke-width="2" style="transform-origin: 160px 90px; transition: transform 0.3s ease;" />
                    <!-- Right wing (animated rotation) -->
                    <path id="bRightWing" d="M160,90 C200,40 240,60 230,110 C225,130 180,120 160,90 Z" fill="#ec4899" stroke="#fbcfe8" stroke-width="2" style="transform-origin: 160px 90px; transition: transform 0.3s ease;" />
                    <!-- Body / antennae -->
                    <line x1="160" y1="65" x2="160" y2="125" stroke="#831843" stroke-width="4" stroke-linecap="round" />
                    <line x1="160" y1="65" x2="152" y2="52" stroke="#831843" stroke-width="2" />
                    <line x1="160" y1="65" x2="168" y2="52" stroke="#831843" stroke-width="2" />
                </g>
            </svg>

            <div id="toyActionText" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-pink-950/80 text-pink-300 border border-pink-700/60">
                Origami Butterfly: Pleated newspaper wings flap when pull tabs are tugged!
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.animateToyMotion()" class="py-2.5 px-4 bg-pink-600 hover:bg-pink-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm flex items-center justify-center gap-2">
                <span>✨</span> Animate Kinetic Motion
            </button>
            <button onclick="window.resetToyMotion()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Reset Position
            </button>
        </div>
    </div>
"""

# SIM 16: Classroom Paper Conservation Tracker
simulators_part2["sim-16"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-emerald-300">Classroom Paper Conservation Tracker</h4>
            </div>
            <span class="text-xs bg-emerald-500/20 text-emerald-300 px-2.5 py-1 rounded-full font-medium border border-emerald-500/30">Stewardship Impact</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div class="bg-slate-950/60 p-3 rounded-xl border border-slate-800 flex flex-col gap-1 text-center">
                <span class="text-2xl">🌳</span>
                <span class="text-xs text-slate-400">Living Trees Saved / Yr</span>
                <span id="treesSavedCount" class="text-xl font-bold text-emerald-400">12 Trees</span>
            </div>
            <div class="bg-slate-950/60 p-3 rounded-xl border border-slate-800 flex flex-col gap-1 text-center">
                <span class="text-2xl">💧</span>
                <span class="text-xs text-slate-400">Freshwater Preserved</span>
                <span id="waterSavedCount" class="text-xl font-bold text-cyan-400">24,000 Liters</span>
            </div>
            <div class="bg-slate-950/60 p-3 rounded-xl border border-slate-800 flex flex-col gap-1 text-center">
                <span class="text-2xl">⚡</span>
                <span class="text-xs text-slate-400">Electricity Conserved</span>
                <span id="energySavedCount" class="text-xl font-bold text-amber-400">4,800 kWh</span>
            </div>
        </div>

        <div class="flex flex-col gap-2 bg-slate-950/80 p-4 rounded-xl border border-slate-800">
            <label class="text-xs font-semibold text-slate-300 flex justify-between">
                <span>Classroom Conservation Habit Pledges:</span>
                <span id="pledgeCountText" class="text-emerald-400 font-bold">3 Active Habits</span>
            </label>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 mt-1">
                <button onclick="window.togglePledge('double')" id="pl-double" class="pledge-btn active py-2 px-2.5 rounded-lg border border-emerald-500/50 bg-emerald-950/40 text-xs text-emerald-200">
                    ✍️ 1. Write Both Sides
                </button>
                <button onclick="window.togglePledge('scrap')" id="pl-scrap" class="pledge-btn active py-2 px-2.5 rounded-lg border border-emerald-500/50 bg-emerald-950/40 text-xs text-emerald-200">
                    📦 2. Scrap Paper Box
                </button>
                <button onclick="window.togglePledge('cloth')" id="pl-cloth" class="pledge-btn active py-2 px-2.5 rounded-lg border border-emerald-500/50 bg-emerald-950/40 text-xs text-emerald-200">
                    🧺 3. Cloth Hand Towels
                </button>
            </div>
        </div>
    </div>
"""

