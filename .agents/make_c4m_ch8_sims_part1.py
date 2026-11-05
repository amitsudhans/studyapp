# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 8: Weigh It, Pour It
Part 1 Simulators: Slides 1 to 8
Bespoke SVG/HTML interactive simulators.
Zero human names (Shrinathan, Mirabai, Raghav, etc. replaced with generic roles).
Clean Unicode throughout.
"""

sim1 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">01</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Market Weight Estimates</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Pumpkin Scale Balance</span>
    </div>

    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setPumpkinMode('half')" id="btn-pm-half" class="pm-btn px-3 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs shadow transition">Half Pumpkin (1 kg)</button>
        <button onclick="setPumpkinMode('whole')" id="btn-pm-whole" class="pm-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Whole Pumpkin (2 kg)</button>
        <button onclick="setPumpkinMode('animals')" id="btn-pm-animals" class="pm-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Animal Weight Benchmark</button>
    </div>

    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="pumpkinScaleSvg" viewBox="0 0 360 190" class="w-full max-w-[340px] h-auto">
            <defs>
                <linearGradient id="pumpkinGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#f59e0b" />
                    <stop offset="100%" stop-color="#b45309" />
                </linearGradient>
            </defs>
            <!-- Fulcrum Stand -->
            <polygon points="180,120 160,170 200,170" fill="#334155" stroke="#475569" stroke-width="2"/>
            <circle cx="180" cy="120" r="5" fill="#f59e0b"/>
            <!-- Scale Base -->
            <rect x="140" y="170" width="80" height="8" rx="2" fill="#1e293b"/>

            <!-- Moving Beam -->
            <g id="pumpkinBeamGroup" transform="rotate(0, 180, 120)">
                <line x1="60" y1="120" x2="300" y2="120" stroke="#94a3b8" stroke-width="5" stroke-linecap="round"/>
                <!-- Left Pan Suspension -->
                <line x1="80" y1="120" x2="60" y2="145" stroke="#64748b" stroke-width="1.5"/>
                <line x1="80" y1="120" x2="100" y2="145" stroke="#64748b" stroke-width="1.5"/>
                <path d="M 50 145 Q 80 160 110 145 Z" fill="#475569" stroke="#64748b" stroke-width="2"/>

                <!-- Right Pan Suspension -->
                <line x1="280" y1="120" x2="260" y2="145" stroke="#64748b" stroke-width="1.5"/>
                <line x1="280" y1="120" x2="300" y2="145" stroke="#64748b" stroke-width="1.5"/>
                <path d="M 250 145 Q 280 160 310 145 Z" fill="#475569" stroke="#64748b" stroke-width="2"/>

                <!-- Left Content: Pumpkin -->
                <g id="leftScaleLoad">
                    <path d="M 60 145 C 60 125, 100 125, 100 145 Z" fill="url(#pumpkinGrad)" stroke="#78350f" stroke-width="1.5"/>
                    <rect x="78" y="122" width="4" height="6" fill="#15803d" rx="1"/>
                    <text x="80" y="140" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Half 1kg</text>
                </g>

                <!-- Right Content: Metal Weights -->
                <g id="rightScaleLoad">
                    <rect x="260" y="133" width="18" height="12" rx="2" fill="#64748b" stroke="#94a3b8"/>
                    <text x="269" y="142" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">500g</text>
                    <rect x="282" y="133" width="18" height="12" rx="2" fill="#64748b" stroke="#94a3b8"/>
                    <text x="291" y="142" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">500g</text>
                </g>
            </g>

            <!-- Status readout inside SVG -->
            <rect x="100" y="25" width="160" height="30" rx="6" fill="#020617" stroke="#334155"/>
            <text id="pumpkinSvgStatus" x="180" y="45" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Scale: Balanced (1 kg = 1000 g)</text>
        </svg>
    </div>

    <div id="pumpkinDescCard" class="bg-slate-800/60 p-3 rounded-xl border border-slate-700/60 text-xs text-slate-300">
        <strong>Observation:</strong> The half pumpkin balances two 500 g metal counterweights (500 g + 500 g = 1000 g = 1 kg). Therefore, the whole pumpkin weighed 2 kg!
    </div>
</div>
"""

sim2 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">02</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Kilograms And Grams</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Metric Converter & Fractions</span>
    </div>

    <!-- Presets -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setKgFraction(0.25)" class="kg-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">1/4 kg (250g)</button>
        <button onclick="setKgFraction(0.5)" class="kg-btn px-2.5 py-1 rounded-lg bg-emerald-500 text-slate-950 text-xs font-bold shadow">1/2 kg (500g)</button>
        <button onclick="setKgFraction(0.75)" class="kg-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">3/4 kg (750g)</button>
        <button onclick="setKgFraction(1.0)" class="kg-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">1 kg (1000g)</button>
    </div>

    <!-- Interactive Slider -->
    <div class="space-y-1.5 px-2">
        <div class="flex justify-between text-xs text-slate-400 font-medium">
            <span>Mass Slider</span>
            <span id="sliderKgLabel" class="text-emerald-400 font-bold text-sm">0.50 kg = 500 g</span>
        </div>
        <input type="range" id="massSlider" min="0.1" max="2.0" step="0.05" value="0.5" oninput="updateMassSlider(this.value)" class="w-full accent-emerald-500 cursor-pointer">
    </div>

    <!-- Visual Fraction Stacking Bar -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="text-xs text-slate-400 font-semibold flex justify-between">
            <span>Visual Metric Bar (1000 g scale):</span>
            <span id="fractionPctText" class="text-emerald-400 font-bold">50% of 1 kg</span>
        </div>
        <div class="w-full h-8 bg-slate-800 rounded-lg overflow-hidden flex border border-slate-700 relative">
            <div id="fractionBarFill" class="h-full bg-gradient-to-r from-emerald-500 to-teal-400 transition-all duration-300 flex items-center justify-center text-slate-950 font-black text-xs" style="width: 50%;">
                500 g
            </div>
            <!-- Quarter Guide Lines -->
            <div class="absolute inset-y-0 left-1/4 w-0.5 bg-slate-600/50"></div>
            <div class="absolute inset-y-0 left-2/4 w-0.5 bg-slate-600/50"></div>
            <div class="absolute inset-y-0 left-3/4 w-0.5 bg-slate-600/50"></div>
        </div>
        <div class="flex justify-between text-[10px] text-slate-500 font-mono">
            <span>0g</span>
            <span>250g (1/4)</span>
            <span>500g (1/2)</span>
            <span>750g (3/4)</span>
            <span>1000g (1kg)</span>
        </div>
    </div>

    <div id="kgConversionInfo" class="bg-emerald-950/40 p-3 rounded-xl border border-emerald-800/40 text-xs text-emerald-200">
        <strong>Metric Rule:</strong> 1 kilogram = 1,000 grams. Dividing into 2 gives 500 g (half kg). Dividing into 4 gives 250 g (quarter kg).
    </div>
</div>
"""

sim3 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">03</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Balancing Beam Scales</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Equilibrium Physics</span>
    </div>

    <!-- Weight Adder Controls -->
    <div class="grid grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800">
            <span class="font-bold text-cyan-400 block mb-1.5">Left Pan: <span id="leftPanWeightDisplay">500</span> g</span>
            <div class="flex flex-wrap gap-1">
                <button onclick="adjustPan('left', 100)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-700">+100g</button>
                <button onclick="adjustPan('left', 250)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-700">+250g</button>
                <button onclick="adjustPan('left', -100)" class="px-2 py-1 bg-red-950/50 hover:bg-red-900/50 text-red-300 rounded border border-red-800">-100g</button>
                <button onclick="clearPan('left')" class="px-2 py-1 bg-slate-900 text-slate-400 rounded">Clear</button>
            </div>
        </div>
        <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800">
            <span class="font-bold text-amber-400 block mb-1.5">Right Pan: <span id="rightPanWeightDisplay">500</span> g</span>
            <div class="flex flex-wrap gap-1">
                <button onclick="adjustPan('right', 100)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-700">+100g</button>
                <button onclick="adjustPan('right', 250)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-700">+250g</button>
                <button onclick="adjustPan('right', -100)" class="px-2 py-1 bg-red-950/50 hover:bg-red-900/50 text-red-300 rounded border border-red-800">-100g</button>
                <button onclick="clearPan('right')" class="px-2 py-1 bg-slate-900 text-slate-400 rounded">Clear</button>
            </div>
        </div>
    </div>

    <!-- Interactive Beam SVG -->
    <div class="bg-slate-950 rounded-xl p-3 flex flex-col items-center justify-center border border-slate-800 min-h-[190px]">
        <svg id="beamScaleSvg" viewBox="0 0 340 160" class="w-full max-w-[320px] h-auto">
            <!-- Central Pivot Post -->
            <polygon points="170,80 155,145 185,145" fill="#1e293b" stroke="#475569" stroke-width="2"/>
            <circle cx="170" cy="80" r="4" fill="#38bdf8"/>
            <rect x="140" y="145" width="60" height="6" rx="2" fill="#0f172a"/>

            <!-- Tilting Beam Group -->
            <g id="dynamicBeamGroup" transform="rotate(0, 170, 80)">
                <line x1="50" y1="80" x2="290" y2="80" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>
                <!-- Left Chain & Pan -->
                <line x1="70" y1="80" x2="50" y2="105" stroke="#64748b" stroke-width="1.5"/>
                <line x1="70" y1="80" x2="90" y2="105" stroke="#64748b" stroke-width="1.5"/>
                <path d="M 40 105 Q 70 120 100 105 Z" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
                <text id="svgLeftPanMassText" x="70" y="102" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">500g</text>

                <!-- Right Chain & Pan -->
                <line x1="270" y1="80" x2="250" y2="105" stroke="#64748b" stroke-width="1.5"/>
                <line x1="270" y1="80" x2="290" y2="105" stroke="#64748b" stroke-width="1.5"/>
                <path d="M 240 105 Q 270 120 300 105 Z" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
                <text id="svgRightPanMassText" x="270" y="102" fill="#fbbf24" font-size="8" font-weight="bold" text-anchor="middle">500g</text>
            </g>

            <!-- Balance Indicator Readout -->
            <rect x="80" y="15" width="180" height="26" rx="5" fill="#0f172a" stroke="#334155"/>
            <text id="beamScaleReadout" x="170" y="32" fill="#22c55e" font-size="11" font-weight="bold" text-anchor="middle">EQUILIBRIUM: BALANCED</text>
        </svg>
    </div>

    <div class="text-xs text-slate-400 bg-slate-800/40 p-2.5 rounded-lg border border-slate-700/40">
        <strong>Principle:</strong> The beam remains horizontal when Left Weight = Right Weight. When one side is heavier, gravity pulls that pan downward!
    </div>
</div>
"""

sim4 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-purple-500/20 text-purple-300 font-bold flex items-center justify-center text-sm">04</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Sweet Box Packaging</h3>
        </div>
        <span class="text-xs text-purple-400 font-medium">1000g Batch Divider</span>
    </div>

    <!-- Box Size Selectors -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setSweetBox(500)" id="sb-btn-500" class="sb-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">500g Boxes</button>
        <button onclick="setSweetBox(250)" id="sb-btn-250" class="sb-btn px-2.5 py-1 rounded-lg bg-purple-500 text-slate-950 text-xs font-bold shadow">250g Boxes</button>
        <button onclick="setSweetBox(100)" id="sb-btn-100" class="sb-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">100g Boxes</button>
        <button onclick="setSweetBox(50)" id="sb-btn-50" class="sb-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">50g Cartons</button>
    </div>

    <!-- Visual Box Grid -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 min-h-[170px] flex flex-col justify-center items-center space-y-3">
        <div class="text-xs text-purple-300 font-bold" id="sweetEquation">
            1000 g ÷ 250 g = 4 Boxes Needed
        </div>
        <div id="sweetBoxContainer" class="flex flex-wrap gap-2 justify-center max-w-[320px] max-h-[140px] overflow-y-auto p-1">
            <!-- Generated Sweet Boxes Dynamically -->
        </div>
    </div>

    <div class="bg-purple-950/40 p-3 rounded-xl border border-purple-800/40 text-xs text-purple-200 flex justify-between items-center">
        <span><strong>Key Takeaway:</strong> As box capacity decreases, total boxes required increases inversely!</span>
    </div>
</div>
"""

sim5 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-rose-500/20 text-rose-300 font-bold flex items-center justify-center text-sm">05</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Object Weight Comparisons</h3>
        </div>
        <span class="text-xs text-rose-400 font-medium">1 Eraser = 5 Grams</span>
    </div>

    <!-- Spice Packet Selector -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setSpiceTarget(10)" id="sp-btn-10" class="sp-btn px-2.5 py-1 rounded-lg bg-rose-500 text-slate-950 text-xs font-bold shadow">10g Turmeric</button>
        <button onclick="setSpiceTarget(20)" id="sp-btn-20" class="sp-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">20g Saffron</button>
        <button onclick="setSpiceTarget(50)" id="sp-btn-50" class="sp-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">50g Masala</button>
    </div>

    <!-- Interactive Eraser Counter -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-400">Erasers on Scale: <strong id="eraserCountDisplay" class="text-white text-sm">2</strong> (10 g)</span>
            <div class="flex gap-2">
                <button onclick="addEraser(1)" class="px-2.5 py-1 bg-rose-600 hover:bg-rose-500 text-white rounded font-bold text-xs">+1 Eraser</button>
                <button onclick="addEraser(-1)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-bold text-xs">-1 Eraser</button>
                <button onclick="resetErasers()" class="px-2 py-1 bg-slate-900 text-slate-500 rounded text-xs">Reset</button>
            </div>
        </div>

        <!-- Scale Balance Visual -->
        <div class="h-10 bg-slate-900 rounded-lg border border-slate-800 flex items-center justify-between px-3 text-xs">
            <span id="spicePanLabel" class="text-rose-400 font-bold">10g Turmeric</span>
            <span id="eraserMatchStatus" class="font-bold text-emerald-400">PERFECT BALANCE (2 × 5g = 10g)</span>
            <span id="eraserPanLabel" class="text-slate-300 font-bold">2 Erasers (10g)</span>
        </div>
    </div>

    <div class="text-xs text-slate-300 bg-slate-800/40 p-2.5 rounded-lg border border-slate-700/40">
        <strong>Classroom Discovery:</strong> Two 5 g erasers balance a 10 g packet. Ten erasers balance a 50 g packet. Small uniform items serve as dependable measuring units!
    </div>
</div>
"""

sim6 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-sky-500/20 text-sky-300 font-bold flex items-center justify-center text-sm">06</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Weighing Machine Types</h3>
        </div>
        <span class="text-xs text-sky-400 font-medium">Scales & Household Grains</span>
    </div>

    <!-- Scale Type Tabs -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 text-center">
        <button onclick="setScaleTab('beam')" id="st-btn-beam" class="st-btn p-2 rounded-xl bg-sky-500 text-slate-950 font-bold text-xs transition">Beam Scale</button>
        <button onclick="setScaleTab('spring')" id="st-btn-spring" class="st-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Spring Balance</button>
        <button onclick="setScaleTab('digital')" id="st-btn-digital" class="st-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Digital Scale</button>
        <button onclick="setScaleTab('platform')" id="st-btn-platform" class="st-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Platform Scale</button>
    </div>

    <!-- Active Scale Details -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 min-h-[140px] flex flex-col justify-center space-y-2">
        <div class="flex justify-between items-center">
            <h4 id="scaleTitle" class="text-sm font-bold text-sky-300">Beam Balance Scale</h4>
            <span id="scaleUsage" class="text-[11px] px-2 py-0.5 rounded bg-sky-950 text-sky-400 border border-sky-800">Market Produce</span>
        </div>
        <p id="scaleDesc" class="text-xs text-slate-300 leading-relaxed">
            Uses two suspended pans and gravitational counterweights to achieve physical equilibrium. Common in local grocery carts and vegetable stalls.
        </p>
    </div>

    <!-- Monthly Grain Calculator -->
    <div class="bg-slate-950/70 p-3 rounded-xl border border-slate-800 space-y-2">
        <span class="text-xs font-bold text-slate-300">Household Monthly Consumption (4 Members):</span>
        <div class="grid grid-cols-4 gap-2 text-center text-xs">
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
                <span class="block text-slate-400 text-[10px]">Flour</span>
                <strong class="text-white">15 kg</strong>
            </div>
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
                <span class="block text-slate-400 text-[10px]">Rice</span>
                <strong class="text-white">10 kg</strong>
            </div>
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
                <span class="block text-slate-400 text-[10px]">Pulses</span>
                <strong class="text-white">5 kg</strong>
            </div>
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
                <span class="block text-slate-400 text-[10px]">Sugar</span>
                <strong class="text-white">3 kg</strong>
            </div>
        </div>
        <div class="text-right text-xs text-sky-400 font-bold">
            Total Monthly Staples = 33 kg
        </div>
    </div>
</div>
"""

sim7 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">07</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Heavy Load Multiples</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">Mass Multipliers & Realistic Loads</span>
    </div>

    <!-- Multiplier Selector -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setHeavySack(10)" id="hs-btn-10" class="hs-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">10kg Sacks</button>
        <button onclick="setHeavySack(25)" id="hs-btn-25" class="hs-btn px-2.5 py-1 rounded-lg bg-orange-500 text-slate-950 text-xs font-bold shadow">25kg Rice Sacks</button>
        <button onclick="setHeavySack(50)" id="hs-btn-50" class="hs-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">50kg Grain Sacks</button>
    </div>

    <!-- Stepper & Comparison -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-400">Number of Sacks: <strong id="sackCountDisplay" class="text-white text-sm">4</strong></span>
            <div class="flex gap-2">
                <button onclick="adjustSackCount(1)" class="px-2.5 py-1 bg-orange-600 hover:bg-orange-500 text-white rounded font-bold text-xs">+1 Sack</button>
                <button onclick="adjustSackCount(-1)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-bold text-xs">-1 Sack</button>
            </div>
        </div>

        <div class="bg-slate-900 p-3 rounded-lg border border-slate-800 flex justify-between items-center text-xs">
            <span class="text-slate-400">Total Calculated Weight:</span>
            <span id="heavyTotalDisplay" class="text-orange-400 font-black text-base">100 kg</span>
        </div>

        <!-- Equivalent Real World Object Comparison -->
        <div class="text-xs text-slate-300 bg-slate-900/60 p-2.5 rounded-lg border border-slate-800/80">
            <strong>Real-World Benchmark:</strong> <span id="heavyBenchmarkText">Equivalent to about 7 gas cylinders (14kg each) or 4 medium dogs (25kg each).</span>
        </div>
    </div>

    <div class="text-[11px] text-slate-400 flex justify-between">
        <span>Bengal Tiger: ~250 kg</span>
        <span>Rhinoceros: ~2,000 kg</span>
        <span>Wild Elephant: ~3,500 kg</span>
    </div>
</div>
"""

sim8 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-yellow-500/20 text-yellow-300 font-bold flex items-center justify-center text-sm">08</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Olympic Weightlifting Feat</h3>
        </div>
        <span class="text-xs text-yellow-400 font-medium">Strength Ratio Math</span>
    </div>

    <!-- Sliders for Bodyweight and Lift -->
    <div class="grid grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between">
                <span class="text-slate-400">Bodyweight</span>
                <span id="athleteWeightLabel" class="text-yellow-400 font-bold">49 kg</span>
            </div>
            <input type="range" id="athleteWeightSlider" min="40" max="70" step="1" value="49" oninput="updateOlympicMath()" class="w-full accent-yellow-500 cursor-pointer">
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between">
                <span class="text-slate-400">Total Lift</span>
                <span id="liftedWeightLabel" class="text-yellow-400 font-bold">202 kg</span>
            </div>
            <input type="range" id="liftedWeightSlider" min="100" max="250" step="2" value="202" oninput="updateOlympicMath()" class="w-full accent-yellow-500 cursor-pointer">
        </div>
    </div>

    <!-- Interactive Ratio Display -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 text-center space-y-2">
        <span class="text-xs text-slate-400 uppercase tracking-wider font-semibold">Lift-To-Bodyweight Ratio</span>
        <div id="liftRatioDisplay" class="text-3xl font-black text-yellow-400 font-mono">
            4.12×
        </div>
        <p class="text-xs text-slate-300" id="liftRatioExplanation">
            The athlete hoisted more than 4 times her own bodyweight! (202 kg ÷ 49 kg = 4.12)
        </p>
    </div>

    <!-- Perspective Multiples -->
    <div class="bg-yellow-950/30 p-3 rounded-xl border border-yellow-800/40 text-xs text-yellow-200">
        <strong>Incredible Equivalent:</strong> 202 kg is equivalent to lifting eight 25 kg sacks of rice simultaneously, or 50 full-grown domestic cats!
    </div>
</div>
"""

simulators_part1 = {
    1: sim1,
    2: sim2,
    3: sim3,
    4: sim4,
    5: sim5,
    6: sim6,
    7: sim7,
    8: sim8,
}

if __name__ == "__main__":
    print(f"Loaded {len(simulators_part1)} simulators for Part 1.")
    for k, v in simulators_part1.items():
        print(f"Sim {k}: {len(v)} chars")

