# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 14: Data Handling
Part 2 Simulators: Slides 9 to 16
Bespoke SVG/HTML interactive simulators.
Zero human names (replaced with generic roles).
Clean Unicode throughout.
"""

sim9 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Bal Mela Food Pictograph</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">1 Plate Icon = 5 Portions</span>
    </div>

    <!-- Day Filter Tabs -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button id="bm-tab-fri" onclick="showBalMelaDay('fri')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Friday</button>
        <button id="bm-tab-sat" onclick="showBalMelaDay('sat')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Saturday (Peak)</button>
        <button id="bm-tab-sun" onclick="showBalMelaDay('sun')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Sunday</button>
        <button id="bm-tab-all" onclick="showBalMelaDay('all')" class="px-3 py-1.5 rounded-lg border border-orange-500 bg-orange-950/40 text-orange-300 font-bold ring-2 ring-orange-500">All 3 Days</button>
    </div>

    <!-- Pictograph Rows -->
    <div class="space-y-3 bg-slate-950 p-4 rounded-xl border border-slate-800">
        <!-- Fruit Chaat -->
        <div>
            <div class="flex items-center justify-between text-xs font-semibold mb-1.5">
                <span class="text-emerald-400">🥗 Fruit Chaat</span>
                <span id="bm-chaat-stat" class="font-mono text-slate-300">18 plates = 90 portions</span>
            </div>
            <div id="bm-chaat-icons" class="flex flex-wrap gap-1.5 p-2 bg-slate-900 rounded-lg min-h-[40px] items-center">
                <!-- Plate SVGs injected by JS -->
            </div>
        </div>

        <!-- Sandwiches -->
        <div>
            <div class="flex items-center justify-between text-xs font-semibold mb-1.5">
                <span class="text-amber-400">🥪 Sandwiches</span>
                <span id="bm-sand-stat" class="font-mono text-slate-300">24 plates = 120 portions</span>
            </div>
            <div id="bm-sand-icons" class="flex flex-wrap gap-1.5 p-2 bg-slate-900 rounded-lg min-h-[40px] items-center">
                <!-- Plate SVGs injected by JS -->
            </div>
        </div>
    </div>

    <div class="flex items-center justify-between text-xs text-slate-400 px-1">
        <span>Scale Key: 🍽️ = 5 Servings</span>
        <span id="bm-day-total" class="font-bold text-orange-400">Total Weekend Sales: 210 Portions</span>
    </div>
</div>
"""

sim10 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-red-500/20 text-red-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Food Sales Trend & Revenue</h3>
        </div>
        <span class="text-xs text-red-400 font-medium">Comparative Analysis</span>
    </div>

    <!-- Analytical Query Buttons -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button onclick="analyzeFoodSales('peak')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium">Highlight Peak Day</button>
        <button onclick="analyzeFoodSales('diff')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium">Item Difference (120 vs 90)</button>
        <button onclick="analyzeFoodSales('revenue')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium">Total Revenue (₹)</button>
    </div>

    <!-- Multi-Day Sales Comparison Table -->
    <div class="overflow-x-auto">
        <table class="w-full text-center text-xs border-collapse">
            <thead>
                <tr class="bg-slate-950 text-slate-300 border-b border-slate-800 font-semibold">
                    <th class="p-2.5 text-left">Festive Day</th>
                    <th class="p-2.5 text-emerald-400">Fruit Chaat (₹10)</th>
                    <th class="p-2.5 text-amber-400">Sandwiches (₹15)</th>
                    <th class="p-2.5 text-white">Daily Volume</th>
                    <th class="p-2.5 text-red-400 border-l border-slate-800">Daily Revenue</th>
                </tr>
            </thead>
            <tbody id="food-sales-body" class="divide-y divide-slate-800 font-mono">
                <tr id="row-fri" class="hover:bg-slate-950/40">
                    <td class="p-2.5 text-left font-sans text-slate-300 font-bold">Friday</td>
                    <td class="p-2.5 text-emerald-300">20</td>
                    <td class="p-2.5 text-amber-300">30</td>
                    <td class="p-2.5 text-white font-bold">50</td>
                    <td class="p-2.5 text-red-300 border-l border-slate-800">₹650</td>
                </tr>
                <tr id="row-sat" class="hover:bg-slate-950/40 bg-red-950/20">
                    <td class="p-2.5 text-left font-sans text-slate-300 font-bold">Saturday (Peak)</td>
                    <td class="p-2.5 text-emerald-300">40</td>
                    <td class="p-2.5 text-amber-300">50</td>
                    <td class="p-2.5 text-white font-bold">90</td>
                    <td class="p-2.5 text-red-300 border-l border-slate-800">₹1,150</td>
                </tr>
                <tr id="row-sun" class="hover:bg-slate-950/40">
                    <td class="p-2.5 text-left font-sans text-slate-300 font-bold">Sunday</td>
                    <td class="p-2.5 text-emerald-300">30</td>
                    <td class="p-2.5 text-amber-300">40</td>
                    <td class="p-2.5 text-white font-bold">70</td>
                    <td class="p-2.5 text-red-300 border-l border-slate-800">₹900</td>
                </tr>
            </tbody>
            <tfoot>
                <tr class="bg-slate-950/90 font-bold border-t-2 border-red-500 font-mono">
                    <td class="p-2.5 text-left font-sans text-red-400">Total Weekend</td>
                    <td class="p-2.5 text-emerald-400">90</td>
                    <td class="p-2.5 text-amber-400">120</td>
                    <td class="p-2.5 text-white text-sm">210</td>
                    <td class="p-2.5 text-emerald-400 border-l border-slate-800 text-sm">₹2,700</td>
                </tr>
            </tfoot>
        </table>
    </div>

    <!-- Spotlight Explanation Box -->
    <div id="food-analysis-box" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
        <strong>Peak Sales Insight:</strong> Saturday generated 90 snack sales and ₹1,150 revenue, making it the most profitable day due to heavy weekend crowd footfall.
    </div>
</div>
"""

sim11 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-yellow-500/20 text-yellow-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Geometric Base-Ten Dienes Blocks</h3>
        </div>
        <span class="text-xs text-yellow-400 font-medium">Place-Value Manipulatives</span>
    </div>

    <!-- Block Controls -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 space-y-1.5">
            <span class="text-amber-400 font-bold block">Thousands (1,000)</span>
            <div class="flex items-center justify-center gap-2">
                <button onclick="adjustDienes('th', -1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">-</button>
                <span id="dienes-val-th" class="font-mono font-bold text-white w-4">1</span>
                <button onclick="adjustDienes('th', 1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">+</button>
            </div>
        </div>

        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 space-y-1.5">
            <span class="text-blue-400 font-bold block">Hundreds Flat (100)</span>
            <div class="flex items-center justify-center gap-2">
                <button onclick="adjustDienes('h', -1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">-</button>
                <span id="dienes-val-h" class="font-mono font-bold text-white w-4">2</span>
                <button onclick="adjustDienes('h', 1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">+</button>
            </div>
        </div>

        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 space-y-1.5">
            <span class="text-emerald-400 font-bold block">Tens Rod (10)</span>
            <div class="flex items-center justify-center gap-2">
                <button onclick="adjustDienes('t', -1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">-</button>
                <span id="dienes-val-t" class="font-mono font-bold text-white w-4">3</span>
                <button onclick="adjustDienes('t', 1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">+</button>
            </div>
        </div>

        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 space-y-1.5">
            <span class="text-rose-400 font-bold block">Unit Cube (1)</span>
            <div class="flex items-center justify-center gap-2">
                <button onclick="adjustDienes('u', -1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">-</button>
                <span id="dienes-val-u" class="font-mono font-bold text-white w-4">4</span>
                <button onclick="adjustDienes('u', 1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">+</button>
            </div>
        </div>
    </div>

    <!-- Visual Canvas & Assembled Quantity -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="dienes-canvas" class="min-h-[90px] flex flex-wrap items-center justify-center gap-3 p-3 bg-slate-900 rounded-lg">
            <!-- SVG shapes rendered by JS -->
        </div>

        <div class="flex flex-col sm:flex-row items-center justify-between gap-2 border-t border-slate-800 pt-3 text-xs">
            <div id="dienes-expanded" class="font-mono text-slate-300">
                1,000 + 200 + 30 + 4
            </div>
            <div class="flex items-center gap-2 font-mono">
                <span class="text-slate-400">Total Numeral:</span>
                <span id="dienes-total" class="text-lg font-black text-yellow-400">1,234</span>
            </div>
        </div>
    </div>
</div>
"""

sim12 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Folding Three-Dimensional Nets</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Spatial Unfolding Studio</span>
    </div>

    <!-- Shape Selection Tabs -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button id="net-btn-cube" onclick="selectNetShape('cube')" class="px-3 py-1.5 rounded-lg border border-teal-500 bg-teal-950/40 text-teal-300 font-bold ring-2 ring-teal-500">Cube (6 Squares)</button>
        <button id="net-btn-cuboid" onclick="selectNetShape('cuboid')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Cuboid (6 Rectangles)</button>
        <button id="net-btn-prism" onclick="selectNetShape('prism')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Triangular Prism</button>
        <button id="net-btn-pyramid" onclick="selectNetShape('pyramid')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Square Pyramid</button>
    </div>

    <!-- Interactive Fold Slider -->
    <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2">
        <div class="flex items-center justify-between text-xs text-slate-300">
            <span>2D Flat Net (0°)</span>
            <span id="net-angle-badge" class="font-mono text-teal-400 font-bold">Fold Angle: 0° (Flat)</span>
            <span>Folded 3D Solid (90°)</span>
        </div>
        <input type="range" id="net-fold-slider" min="0" max="90" value="0" oninput="updateNetFold(this.value)" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-teal-500">
    </div>

    <!-- SVG Net Visual Canvas -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[160px]">
        <svg id="net-svg-display" viewBox="0 0 300 160" class="w-full max-w-[280px] h-36">
            <!-- Dynamic 2D/3D net rendered by JS -->
        </svg>
        <p id="net-description" class="text-xs text-slate-300 text-center mt-2">
            A cube unfolds into 6 equal square faces meeting along shared edges.
        </p>
    </div>
</div>
"""

sim13 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-sky-500/20 text-sky-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Place Value Arrow Cards</h3>
        </div>
        <span class="text-xs text-sky-400 font-medium">Expanded vs Compact Numeral</span>
    </div>

    <!-- Place Value Selectors -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <div>
            <label class="block text-slate-400 mb-1 text-[11px]">Thousands</label>
            <select id="ac-th" onchange="updateArrowCards()" class="w-full p-2 bg-slate-950 border border-slate-800 rounded-lg text-amber-400 font-mono font-bold">
                <option value="4000">4,000</option>
                <option value="2000">2,000</option>
                <option value="5000">5,000</option>
                <option value="7000">7,000</option>
            </select>
        </div>
        <div>
            <label class="block text-slate-400 mb-1 text-[11px]">Hundreds</label>
            <select id="ac-h" onchange="updateArrowCards()" class="w-full p-2 bg-slate-950 border border-slate-800 rounded-lg text-blue-400 font-mono font-bold">
                <option value="300">300</option>
                <option value="500">500</option>
                <option value="800">800</option>
                <option value="0">0 (None)</option>
            </select>
        </div>
        <div>
            <label class="block text-slate-400 mb-1 text-[11px]">Tens</label>
            <select id="ac-t" onchange="updateArrowCards()" class="w-full p-2 bg-slate-950 border border-slate-800 rounded-lg text-emerald-400 font-mono font-bold">
                <option value="20">20</option>
                <option value="40">40</option>
                <option value="70">70</option>
                <option value="0">0 (None)</option>
            </select>
        </div>
        <div>
            <label class="block text-slate-400 mb-1 text-[11px]">Ones</label>
            <select id="ac-u" onchange="updateArrowCards()" class="w-full p-2 bg-slate-950 border border-slate-800 rounded-lg text-rose-400 font-mono font-bold">
                <option value="5">5</option>
                <option value="2">2</option>
                <option value="8">8</option>
                <option value="9">9</option>
            </select>
        </div>
    </div>

    <!-- Toggle Action -->
    <div class="flex items-center justify-center gap-3">
        <button id="ac-btn-stack" onclick="setArrowCardMode('stacked')" class="px-4 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs transition-colors shadow">
            Stack Arrow Cards (Compact)
        </button>
        <button id="ac-btn-expand" onclick="setArrowCardMode('expanded')" class="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-xs transition-colors">
            Deconstruct (Expanded Form)
        </button>
    </div>

    <!-- Cards Display Box -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex items-center justify-center min-h-[100px] overflow-x-auto">
        <div id="arrow-cards-visual" class="flex items-center gap-2 font-mono font-bold text-sm">
            <!-- Dynamic arrow cards rendered by JS -->
        </div>
    </div>
</div>
"""

sim14 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-purple-500/20 text-purple-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Fraction Strip Kit Comparator</h3>
        </div>
        <span class="text-xs text-purple-400 font-medium">24 cm Unit Benchmark</span>
    </div>

    <!-- Quick Equivalence Buttons -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button onclick="highlightFractionEquiv('half')" class="px-3 py-1 rounded bg-purple-950/60 hover:bg-purple-900 border border-purple-700 text-purple-200 font-medium">Show 1/2 = 2/4 = 4/8</button>
        <button onclick="highlightFractionEquiv('third')" class="px-3 py-1 rounded bg-purple-950/60 hover:bg-purple-900 border border-purple-700 text-purple-200 font-medium">Show 1/3 = 2/6 = 4/12</button>
        <button onclick="highlightFractionEquiv('quarter')" class="px-3 py-1 rounded bg-purple-950/60 hover:bg-purple-900 border border-purple-700 text-purple-200 font-medium">Show 1/4 = 2/8</button>
        <button onclick="resetFractionHighlights()" class="px-3 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs ml-auto">Reset</button>
    </div>

    <!-- Fraction Strips Stack -->
    <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2 text-[11px] font-mono">
        <!-- 1 Whole -->
        <div class="flex items-center gap-2">
            <span class="w-10 text-slate-400 shrink-0">1 Whole</span>
            <div id="fs-row-1" class="flex-1 h-6 rounded bg-slate-700 flex items-center justify-center text-white font-bold border border-slate-600">1 (24 cm)</div>
        </div>

        <!-- 1/2 Strips -->
        <div class="flex items-center gap-2">
            <span class="w-10 text-slate-400 shrink-0">1/2</span>
            <div class="flex-1 flex gap-1 h-6">
                <div id="fs-half-1" class="flex-1 rounded bg-blue-700/80 flex items-center justify-center text-white font-bold border border-blue-500">1/2 (12 cm)</div>
                <div id="fs-half-2" class="flex-1 rounded bg-blue-700/80 flex items-center justify-center text-white font-bold border border-blue-500">1/2 (12 cm)</div>
            </div>
        </div>

        <!-- 1/4 Strips -->
        <div class="flex items-center gap-2">
            <span class="w-10 text-slate-400 shrink-0">1/4</span>
            <div class="flex-1 flex gap-1 h-6">
                <div id="fs-q-1" class="flex-1 rounded bg-emerald-700/80 flex items-center justify-center text-white font-bold border border-emerald-500">1/4</div>
                <div id="fs-q-2" class="flex-1 rounded bg-emerald-700/80 flex items-center justify-center text-white font-bold border border-emerald-500">1/4</div>
                <div id="fs-q-3" class="flex-1 rounded bg-emerald-700/80 flex items-center justify-center text-white font-bold border border-emerald-500">1/4</div>
                <div id="fs-q-4" class="flex-1 rounded bg-emerald-700/80 flex items-center justify-center text-white font-bold border border-emerald-500">1/4</div>
            </div>
        </div>

        <!-- 1/8 Strips -->
        <div class="flex items-center gap-2">
            <span class="w-10 text-slate-400 shrink-0">1/8</span>
            <div class="flex-1 flex gap-0.5 h-6">
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
            </div>
        </div>
    </div>

    <!-- Comparison Feedback -->
    <div id="fraction-feedback-box" class="text-xs text-center text-purple-300 p-2.5 rounded-lg bg-purple-950/30 border border-purple-800/40">
        Equivalence Proof: Two 1/4 segments (6 cm + 6 cm = 12 cm) equal one 1/2 segment (12 cm).
    </div>
</div>
"""

sim15 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-green-500/20 text-green-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Word Problem Bar Models</h3>
        </div>
        <span class="text-xs text-green-400 font-medium">Box Diagram Schematics</span>
    </div>

    <!-- Model Type Tabs -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button id="wp-tab-combine" onclick="selectWordProblemModel('combine')" class="px-3 py-1.5 rounded-lg border border-green-500 bg-green-950/40 text-green-300 font-bold ring-2 ring-green-500">Combine Model (Add)</button>
        <button id="wp-tab-compare" onclick="selectWordProblemModel('compare')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Compare Model (Difference)</button>
        <button id="wp-tab-change" onclick="selectWordProblemModel('change')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Change Model (Subtract)</button>
    </div>

    <!-- Interactive Schematic Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-4">
        <div id="wp-problem-text" class="text-xs text-slate-300 font-medium bg-slate-900 p-3 rounded-lg border border-slate-800 leading-relaxed">
            In our class survey, 24 boys and 24 girls participated. What is the total number of students surveyed?
        </div>

        <!-- Visual Bar Diagram Container -->
        <div id="wp-diagram-container" class="space-y-2 py-2">
            <!-- Dynamic SVG or Flex bars rendered by JS -->
        </div>

        <!-- Equation and Operation Solution -->
        <div class="flex items-center justify-between border-t border-slate-800 pt-3 text-xs">
            <div id="wp-equation" class="font-mono text-emerald-400 font-bold text-sm">
                24 + 24 = 48 Students
            </div>
            <div id="wp-operation-badge" class="px-2.5 py-1 rounded bg-green-900/40 border border-green-700 text-green-300 font-bold">
                Operation: Addition
            </div>
        </div>
    </div>
</div>
"""

sim16 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Comprehensive Statistical Dashboard</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Unified Studio</span>
    </div>

    <!-- Multi-View Navigator Tabs -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button id="dash-tab-overview" onclick="switchDashboardView('overview')" class="px-3 py-1.5 rounded-lg border border-indigo-500 bg-indigo-950/40 text-indigo-300 font-bold ring-2 ring-indigo-500">Summary Cards</button>
        <button id="dash-tab-table" onclick="switchDashboardView('table')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Frequency Table</button>
        <button id="dash-tab-picto" onclick="switchDashboardView('picto')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Food Pictograph</button>
        <button id="dash-tab-matrix" onclick="switchDashboardView('matrix')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Two-Way Matrix</button>
    </div>

    <!-- Active View Display Area -->
    <div id="dashboard-view-content" class="bg-slate-950 p-4 rounded-xl border border-slate-800 min-h-[160px] text-xs">
        <!-- Default: Summary Cards -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <div class="p-3 bg-slate-900 rounded-xl border border-blue-900/40 text-center space-y-1">
                <span class="text-[10px] uppercase font-bold text-slate-400">Class Survey</span>
                <div class="text-xl font-bold font-mono text-blue-400">45 Students</div>
                <span class="text-[10px] text-slate-500">Top: Math (14)</span>
            </div>
            <div class="p-3 bg-slate-900 rounded-xl border border-orange-900/40 text-center space-y-1">
                <span class="text-[10px] uppercase font-bold text-slate-400">Bal Mela Sales</span>
                <div class="text-xl font-bold font-mono text-orange-400">210 Portions</div>
                <span class="text-[10px] text-slate-500">Peak: Sat (90)</span>
            </div>
            <div class="p-3 bg-slate-900 rounded-xl border border-teal-900/40 text-center space-y-1">
                <span class="text-[10px] uppercase font-bold text-slate-400">Sports Matrix</span>
                <div class="text-xl font-bold font-mono text-teal-400">48 Students</div>
                <span class="text-[10px] text-slate-500">Both: 11 (23%)</span>
            </div>
            <div class="p-3 bg-slate-900 rounded-xl border border-purple-900/40 text-center space-y-1">
                <span class="text-[10px] uppercase font-bold text-slate-400">Total Revenue</span>
                <div class="text-xl font-bold font-mono text-purple-400">₹2,700</div>
                <span class="text-[10px] text-slate-500">120 Sand + 90 Chaat</span>
            </div>
        </div>
    </div>

    <div class="text-xs text-slate-400 text-center">
        Data Handling enables structured observation, accurate recording, graphical communication, and evidence-based decision making.
    </div>
</div>
"""

simulators_part2 = {
    9: sim9,
    10: sim10,
    11: sim11,
    12: sim12,
    13: sim13,
    14: sim14,
    15: sim15,
    16: sim16,
}

