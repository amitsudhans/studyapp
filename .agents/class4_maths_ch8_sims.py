# -*- coding: utf-8 -*-
"""Class 4 Mathematics Chapter 8 Simulators"""

simulators = {
    1: '''
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
''',
    2: '''
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
''',
    3: '''
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
''',
    4: '''
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
''',
    5: '''
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
''',
    6: '''
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
''',
    7: '''
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
''',
    8: '''
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
''',
    9: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Litres And Millilitres</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">1 L = 1000 ml Measuring Cylinder</span>
    </div>

    <!-- Presets -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setLiquidPreset(150, 'Teacup')" class="lq-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">Teacup (150 ml)</button>
        <button onclick="setLiquidPreset(250, 'Glass')" class="lq-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">Glass Tumbler (250 ml)</button>
        <button onclick="setLiquidPreset(500, 'Milk Pouch')" class="lq-btn px-2.5 py-1 rounded-lg bg-blue-500 text-slate-950 text-xs font-bold shadow">Milk Pouch (500 ml)</button>
        <button onclick="setLiquidPreset(1000, 'Water Bottle')" class="lq-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">Bottle (1000 ml = 1 L)</button>
    </div>

    <!-- Interactive Cylinder SVG & Slider -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center bg-slate-950 rounded-xl p-4 border border-slate-800">
        <div class="flex justify-center">
            <svg id="liquidCylinderSvg" viewBox="0 0 140 220" class="w-28 h-auto">
                <defs>
                    <linearGradient id="waterGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#0284c7" />
                        <stop offset="100%" stop-color="#38bdf8" />
                    </linearGradient>
                </defs>
                <!-- Glass Cylinder Outline -->
                <rect x="35" y="20" width="70" height="180" rx="4" fill="#0f172a" stroke="#475569" stroke-width="2"/>
                <!-- Liquid Fill Rect (Height 170 max) -->
                <rect id="liquidFillRect" x="37" y="115" width="66" height="83" rx="2" fill="url(#waterGrad)" class="transition-all duration-300"/>
                
                <!-- Graduation Marks -->
                <!-- 1000ml (y=30) -->
                <line x1="35" y1="30" x2="50" y2="30" stroke="#94a3b8" stroke-width="1.5"/>
                <text x="55" y="33" fill="#cbd5e1" font-size="8" font-family="monospace">1000ml (1L)</text>
                <!-- 750ml (y=72.5) -->
                <line x1="35" y1="72.5" x2="47" y2="72.5" stroke="#94a3b8" stroke-width="1"/>
                <text x="52" y="75" fill="#cbd5e1" font-size="7" font-family="monospace">750ml</text>
                <!-- 500ml (y=115) -->
                <line x1="35" y1="115" x2="50" y2="115" stroke="#94a3b8" stroke-width="1.5"/>
                <text x="55" y="118" fill="#38bdf8" font-size="8" font-weight="bold" font-family="monospace">500ml (1/2L)</text>
                <!-- 250ml (y=157.5) -->
                <line x1="35" y1="157.5" x2="47" y2="157.5" stroke="#94a3b8" stroke-width="1"/>
                <text x="52" y="160" fill="#cbd5e1" font-size="7" font-family="monospace">250ml</text>
                <!-- 0ml base -->
                <line x1="35" y1="200" x2="105" y2="200" stroke="#64748b" stroke-width="3"/>
            </svg>
        </div>

        <div class="space-y-3">
            <div class="space-y-1">
                <div class="flex justify-between text-xs text-slate-400">
                    <span>Selected Volume:</span>
                    <strong id="cylinderVolumeLabel" class="text-blue-400 text-sm">500 ml</strong>
                </div>
                <input type="range" id="cylinderSlider" min="0" max="1000" step="25" value="500" oninput="updateCylinderSlider(this.value)" class="w-full accent-blue-500 cursor-pointer">
            </div>
            <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800 text-xs text-slate-300 space-y-1">
                <div>Container: <strong id="containerNameLabel" class="text-white">Milk Pouch</strong></div>
                <div>Fraction of 1 L: <strong id="cylinderFractionLabel" class="text-blue-300">1/2 Litre</strong></div>
            </div>
        </div>
    </div>

    <div class="text-xs text-slate-300 bg-blue-950/30 p-2.5 rounded-lg border border-blue-800/40">
        <strong>Metric Rule:</strong> 1 Litre (L) = 1,000 Millilitres (ml). Small volumes are measured in ml, larger household volumes in L!
    </div>
</div>
''',
    10: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Fractional Litre Measures</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">1/4 L, 1/2 L, 3/4 L Subdivisions</span>
    </div>

    <!-- Fraction Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
        <button onclick="setFractionLitre(250)" id="fl-btn-250" class="fl-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            1/4 L (250 ml)
        </button>
        <button onclick="setFractionLitre(500)" id="fl-btn-500" class="fl-btn p-2 rounded-xl bg-teal-500 text-slate-950 font-bold shadow transition">
            1/2 L (500 ml)
        </button>
        <button onclick="setFractionLitre(750)" id="fl-btn-750" class="fl-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            3/4 L (750 ml)
        </button>
        <button onclick="setFractionLitre(1000)" id="fl-btn-1000" class="fl-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            1 L (1000 ml)
        </button>
    </div>

    <!-- 4 Quarter Blocks Visualization -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="flex justify-between text-xs text-slate-400 font-semibold">
            <span>Modular 250ml Quarter Segments:</span>
            <span id="activeFractionText" class="text-teal-400 font-bold">2 of 4 Quarters Filled (500 ml)</span>
        </div>
        <div class="grid grid-cols-4 gap-2">
            <div id="qblock-1" class="h-14 rounded-lg bg-teal-500 flex flex-col items-center justify-center text-slate-950 font-bold text-xs transition">
                <span>1/4 L</span>
                <span class="text-[10px] font-mono">250 ml</span>
            </div>
            <div id="qblock-2" class="h-14 rounded-lg bg-teal-500 flex flex-col items-center justify-center text-slate-950 font-bold text-xs transition">
                <span>1/4 L</span>
                <span class="text-[10px] font-mono">250 ml</span>
            </div>
            <div id="qblock-3" class="h-14 rounded-lg bg-slate-800 border border-slate-700 flex flex-col items-center justify-center text-slate-400 font-bold text-xs transition">
                <span>1/4 L</span>
                <span class="text-[10px] font-mono">250 ml</span>
            </div>
            <div id="qblock-4" class="h-14 rounded-lg bg-slate-800 border border-slate-700 flex flex-col items-center justify-center text-slate-400 font-bold text-xs transition">
                <span>1/4 L</span>
                <span class="text-[10px] font-mono">250 ml</span>
            </div>
        </div>
    </div>

    <div class="bg-teal-950/40 p-3 rounded-xl border border-teal-800/40 text-xs text-teal-200">
        <strong>Mathematical Identity:</strong> 250 ml + 250 ml = 500 ml (half litre). 500 ml + 250 ml = 750 ml (three-quarters litre). Four 250 ml blocks make 1 full litre!
    </div>
</div>
''',
    11: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Droppers And Spoons</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Miniature Medical Doses</span>
    </div>

    <!-- Medicine Dispenser Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
        <button onclick="setDispenser(1, 'Eye Dropper')" class="md-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            Dropper (1 ml)
        </button>
        <button onclick="setDispenser(5, 'Medicine Spoon')" class="md-btn p-2 rounded-xl bg-indigo-500 text-slate-950 font-bold shadow transition">
            Teaspoon (5 ml)
        </button>
        <button onclick="setDispenser(10, 'Dosing Cup')" class="md-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            Dosing Cup (10 ml)
        </button>
        <button onclick="setDispenser(15, 'Oral Syringe')" class="md-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            Syringe (15 ml)
        </button>
    </div>

    <!-- Interactive Dose Accumulator -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-400">Total Dosed: <strong id="totalDoseDisplay" class="text-white text-sm">5 ml</strong></span>
            <div class="flex gap-2">
                <button onclick="addDose()" class="px-3 py-1 bg-indigo-600 hover:bg-indigo-500 text-white rounded font-bold text-xs">+ Dispense Dose</button>
                <button onclick="resetDose()" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-400 rounded text-xs">Reset</button>
            </div>
        </div>

        <div class="bg-slate-900 p-3 rounded-lg border border-slate-800 space-y-2 text-xs">
            <div class="flex justify-between">
                <span class="text-slate-400">Standard 100 ml Syrup Bottle:</span>
                <span id="bottleRemainingLabel" class="text-indigo-400 font-bold">95 ml remaining</span>
            </div>
            <div class="w-full h-3 bg-slate-800 rounded-full overflow-hidden">
                <div id="bottleProgressBar" class="h-full bg-indigo-500 transition-all duration-300" style="width: 5%;"></div>
            </div>
            <div class="text-[11px] text-slate-400 text-right" id="daysLastText">
                At 10 ml/day (5ml twice daily), bottle lasts 10 days!
            </div>
        </div>
    </div>

    <div class="text-xs text-slate-300 bg-slate-800/40 p-2.5 rounded-lg border border-slate-700/40">
        <strong>Clinical Insight:</strong> About 20 drops from an eyedropper equal 1 ml. Accurate millilitre measurement prevents medicinal underdosing or overdosing!
    </div>
</div>
''',
    12: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Perfumed Oil Bottles</h3>
        </div>
        <span class="text-xs text-pink-400 font-medium">1000 ml Artisan Packaging</span>
    </div>

    <!-- Retail Bottle Size Selectors -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setOilBottleSize(50)" id="ob-btn-50" class="ob-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">50 ml Vials</button>
        <button onclick="setOilBottleSize(100)" id="ob-btn-100" class="ob-btn px-2.5 py-1 rounded-lg bg-pink-500 text-slate-950 text-xs font-bold shadow">100 ml Bottles</button>
        <button onclick="setOilBottleSize(200)" id="ob-btn-200" class="ob-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">200 ml Bottles</button>
        <button onclick="setOilBottleSize(250)" id="ob-btn-250" class="ob-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">250 ml Bottles</button>
    </div>

    <!-- Dynamic Bottle Yield Visualizer -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 min-h-[170px] flex flex-col justify-center items-center space-y-3">
        <div class="text-xs text-pink-300 font-bold" id="oilEquationText">
            1000 ml ÷ 100 ml = 10 Bottles Filled
        </div>
        <div id="oilBottlesGrid" class="flex flex-wrap gap-2 justify-center max-w-[320px] max-h-[140px] overflow-y-auto p-1">
            <!-- Dynamically generated bottles -->
        </div>
    </div>

    <div class="bg-pink-950/40 p-3 rounded-xl border border-pink-800/40 text-xs text-pink-200">
        <strong>Packaging Logic:</strong> 1 Litre master batch (1000 ml) divided into 50 ml bottles yields 20 bottles. Dividing into 200 ml bottles yields 5 bottles!
    </div>
</div>
''',
    13: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Milk Measuring Cans</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Standard Dairy Scoops</span>
    </div>

    <!-- Target Milk Order Selector -->
    <div class="flex items-center justify-between text-xs bg-slate-950 p-2.5 rounded-xl border border-slate-800">
        <span class="text-slate-400">Customer Order Target:</span>
        <div class="flex gap-1.5">
            <button onclick="setMilkOrder(750)" id="mo-btn-750" class="mo-btn px-2 py-1 rounded bg-amber-500 text-slate-950 font-bold text-xs">750 ml</button>
            <button onclick="setMilkOrder(1200)" id="mo-btn-1200" class="mo-btn px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700 text-xs">1200 ml</button>
            <button onclick="setMilkOrder(1500)" id="mo-btn-1500" class="mo-btn px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700 text-xs">1500 ml</button>
        </div>
    </div>

    <!-- Dairy Scoops Clicker -->
    <div class="space-y-2">
        <span class="text-xs font-semibold text-slate-400 block">Click Cans to Pour Milk:</span>
        <div class="grid grid-cols-5 gap-1.5 text-center text-xs">
            <button onclick="pourMilkScoop(50)" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 font-bold">+50ml</button>
            <button onclick="pourMilkScoop(100)" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 font-bold">+100ml</button>
            <button onclick="pourMilkScoop(200)" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 font-bold">+200ml</button>
            <button onclick="pourMilkScoop(500)" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 font-bold">+500ml</button>
            <button onclick="pourMilkScoop(1000)" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 font-bold">+1 L</button>
        </div>
    </div>

    <!-- Poured Milk Jug Status -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-2">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-400">Total Milk Poured:</span>
            <strong id="pouredMilkTotal" class="text-amber-400 text-base font-black">0 ml</strong>
        </div>
        <div id="milkPourFeedback" class="text-xs p-2 rounded-lg bg-slate-900 border border-slate-800 text-slate-300 flex justify-between items-center">
            <span>Target: 750 ml (Need 750 ml more)</span>
            <button onclick="resetMilkJug()" class="text-[10px] text-slate-400 underline">Clear Jug</button>
        </div>
    </div>
</div>
''',
    14: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Daily Water Consumption</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Household Audit (4 Members)</span>
    </div>

    <!-- Domestic Activity Sliders / Breakdown -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3 text-xs">
        <div class="space-y-2">
            <div class="flex justify-between text-slate-300">
                <span>Drinking & Cooking:</span>
                <span class="text-cyan-400 font-bold">30 Litres</span>
            </div>
            <div class="w-full h-2.5 bg-slate-800 rounded-full overflow-hidden">
                <div class="h-full bg-cyan-500" style="width: 12%;"></div>
            </div>

            <div class="flex justify-between text-slate-300">
                <span>Dishes & Cleaning:</span>
                <span class="text-cyan-400 font-bold">50 Litres</span>
            </div>
            <div class="w-full h-2.5 bg-slate-800 rounded-full overflow-hidden">
                <div class="h-full bg-blue-500" style="width: 20%;"></div>
            </div>

            <div class="flex justify-between text-slate-300">
                <span>Washing Laundry:</span>
                <span class="text-cyan-400 font-bold">50 Litres</span>
            </div>
            <div class="w-full h-2.5 bg-slate-800 rounded-full overflow-hidden">
                <div class="h-full bg-indigo-500" style="width: 20%;"></div>
            </div>

            <div class="flex justify-between text-slate-300">
                <span>Baths (4 Bucket Baths @ 30L):</span>
                <span class="text-cyan-400 font-bold">120 Litres</span>
            </div>
            <div class="w-full h-2.5 bg-slate-800 rounded-full overflow-hidden">
                <div class="h-full bg-sky-400" style="width: 48%;"></div>
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex justify-between items-center text-xs">
            <span class="font-bold text-slate-200">Total Family Daily Water:</span>
            <span class="text-base font-black text-cyan-300">250 Litres / Day</span>
        </div>
    </div>

    <div class="text-xs text-slate-400 bg-slate-800/40 p-2.5 rounded-lg border border-slate-700/40">
        <strong>Observation:</strong> Personal hygiene and laundry consume over 65% of total domestic water. Mindful conservation in these activities produces immediate substantial savings!
    </div>
</div>
''',
    15: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-red-500/20 text-red-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Leaking Tap Investigation</h3>
        </div>
        <span class="text-xs text-red-400 font-medium">Cumulative Drip Wastage</span>
    </div>

    <!-- Time Horizon Selectors -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 text-center text-xs">
        <button onclick="setLeakTime('hour')" id="lt-btn-hour" class="lt-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            1 Hour
        </button>
        <button onclick="setLeakTime('day')" id="lt-btn-day" class="lt-btn p-2 rounded-xl bg-red-500 text-slate-950 font-bold shadow transition">
            1 Day (24h)
        </button>
        <button onclick="setLeakTime('week')" id="lt-btn-week" class="lt-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            1 Week (7d)
        </button>
        <button onclick="setLeakTime('month')" id="lt-btn-month" class="lt-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            1 Month (30d)
        </button>
    </div>

    <!-- Animated Faucet & Bucket SVG -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center space-y-2">
        <svg viewBox="0 0 200 120" class="w-48 h-auto">
            <!-- Pipe & Faucet -->
            <path d="M 40 20 L 100 20 L 100 45 L 90 45 L 90 30 L 40 30 Z" fill="#64748b"/>
            <!-- Valve handle -->
            <rect x="92" y="10" width="16" height="6" rx="2" fill="#ef4444"/>
            <rect x="98" y="16" width="4" height="6" fill="#94a3b8"/>
            <!-- Dripping Water droplet -->
            <circle cx="95" cy="60" r="3.5" fill="#38bdf8" opacity="0.9">
                <animate attributeName="cy" values="45;85" dur="1.2s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="1;0.2" dur="1.2s" repeatCount="indefinite" />
            </circle>
            <!-- Water Bucket -->
            <polygon points="75,85 115,85 110,115 80,115" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
            <!-- Water inside bucket -->
            <polygon id="bucketWaterFill" points="76,95 114,95 110,115 80,115" fill="#0284c7"/>
        </svg>

        <div class="text-center space-y-1">
            <span class="text-xs text-slate-400 font-semibold" id="leakFormulaLabel">1 L/hour × 24 hours</span>
            <div id="leakVolumeDisplay" class="text-2xl font-black text-red-400 font-mono">
                24 Litres Lost!
            </div>
        </div>
    </div>

    <div class="bg-red-950/40 p-3 rounded-xl border border-red-800/40 text-xs text-red-200">
        <strong>Shocking Fact:</strong> A single tap dripping 1 drop every second wastes 24 L daily, 168 L weekly, and 720 L every month!
    </div>
</div>
''',
    16: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Conservation Volume Math</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Multiplied School Savings</span>
    </div>

    <!-- Student Population Slider -->
    <div class="space-y-1.5 px-2">
        <div class="flex justify-between text-xs text-slate-400 font-medium">
            <span>School Enrollment (Students):</span>
            <span id="studentCountLabel" class="text-emerald-400 font-bold text-sm">500 Students</span>
        </div>
        <input type="range" id="studentSlider" min="50" max="1000" step="50" value="500" oninput="updateConservationMath(this.value)" class="w-full accent-emerald-500 cursor-pointer">
    </div>

    <!-- Multiplied Conservation Impact Display -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="grid grid-cols-2 gap-3 text-center">
            <div class="bg-slate-900 p-3 rounded-lg border border-slate-800">
                <span class="block text-[11px] text-slate-400">Daily Water Saved:</span>
                <strong id="dailySchoolSavings" class="text-emerald-400 text-lg font-black font-mono">9,500 L</strong>
                <span class="block text-[10px] text-slate-500">(@ 19 L per student)</span>
            </div>
            <div class="bg-slate-900 p-3 rounded-lg border border-slate-800">
                <span class="block text-[11px] text-slate-400">Monthly School Saved:</span>
                <strong id="monthlySchoolSavings" class="text-teal-400 text-lg font-black font-mono">285,000 L</strong>
                <span class="block text-[10px] text-slate-500">(30 school days)</span>
            </div>
        </div>

        <!-- Equivalent Water Tankers -->
        <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-800 flex justify-between items-center text-xs text-slate-300">
            <span>Equivalent Water Tankers Saved:</span>
            <strong id="tankerEquivLabel" class="text-emerald-300">~28 Large Tankers (10,000L each)</strong>
        </div>
    </div>

    <div class="text-xs text-slate-300 bg-emerald-950/30 p-2.5 rounded-lg border border-emerald-800/40">
        <strong>Community Power:</strong> Simply turning off running taps while brushing saves 19 litres daily per person. Scaled across schools and neighborhoods, millions of litres are conserved!
    </div>
</div>
''',
}
