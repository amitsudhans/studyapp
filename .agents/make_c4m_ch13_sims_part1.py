# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 13: The Transport Museum
Part 1 Simulators: Slides 1 to 8
Bespoke SVG/HTML interactive simulators.
Zero human names (replaced with generic roles).
Clean Unicode throughout.
"""

sim1 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">01</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Mystery Matrix Puzzle</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Grid Factor Deduction</span>
    </div>

    <!-- 3x3 Multiplication Matrix Container -->
    <div class="flex justify-center">
        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 inline-block">
            <div class="grid grid-cols-4 gap-2 text-center text-xs font-mono font-bold">
                <!-- Top-Left Corner (Operation Symbol) -->
                <div class="w-12 h-12 flex items-center justify-center rounded-lg bg-indigo-950/60 text-indigo-400 border border-indigo-800 text-base">×</div>
                <!-- Column Headers (Inputs/Selects) -->
                <div>
                    <input type="number" id="mm-col-1" min="1" max="9" value="3" onchange="checkMysteryMatrix()" class="w-12 h-12 text-center bg-slate-800 border border-indigo-500/50 rounded-lg text-white font-bold text-sm focus:ring-1 focus:ring-indigo-500">
                </div>
                <div>
                    <input type="number" id="mm-col-2" min="1" max="9" value="4" onchange="checkMysteryMatrix()" class="w-12 h-12 text-center bg-slate-800 border border-indigo-500/50 rounded-lg text-white font-bold text-sm focus:ring-1 focus:ring-indigo-500">
                </div>
                <div>
                    <input type="number" id="mm-col-3" min="1" max="9" value="6" onchange="checkMysteryMatrix()" class="w-12 h-12 text-center bg-slate-800 border border-indigo-500/50 rounded-lg text-white font-bold text-sm focus:ring-1 focus:ring-indigo-500">
                </div>

                <!-- Row 1 -->
                <div>
                    <input type="number" id="mm-row-1" min="1" max="9" value="8" onchange="checkMysteryMatrix()" class="w-12 h-12 text-center bg-slate-800 border border-indigo-500/50 rounded-lg text-white font-bold text-sm focus:ring-1 focus:ring-indigo-500">
                </div>
                <div id="mm-c-1-1" class="w-12 h-12 flex items-center justify-center rounded-lg bg-slate-900 border border-slate-700 text-white">24</div>
                <div id="mm-c-1-2" class="w-12 h-12 flex items-center justify-center rounded-lg bg-amber-950/40 border border-amber-600/60 text-amber-300">32</div>
                <div id="mm-c-1-3" class="w-12 h-12 flex items-center justify-center rounded-lg bg-slate-900 border border-slate-700 text-white">48</div>

                <!-- Row 2 -->
                <div>
                    <input type="number" id="mm-row-2" min="1" max="9" value="5" onchange="checkMysteryMatrix()" class="w-12 h-12 text-center bg-slate-800 border border-indigo-500/50 rounded-lg text-white font-bold text-sm focus:ring-1 focus:ring-indigo-500">
                </div>
                <div id="mm-c-2-1" class="w-12 h-12 flex items-center justify-center rounded-lg bg-cyan-950/40 border border-cyan-600/60 text-cyan-300">15</div>
                <div id="mm-c-2-2" class="w-12 h-12 flex items-center justify-center rounded-lg bg-slate-900 border border-slate-700 text-white">20</div>
                <div id="mm-c-2-3" class="w-12 h-12 flex items-center justify-center rounded-lg bg-amber-950/40 border border-amber-600/60 text-amber-300">30</div>

                <!-- Row 3 -->
                <div>
                    <input type="number" id="mm-row-3" min="1" max="9" value="7" onchange="checkMysteryMatrix()" class="w-12 h-12 text-center bg-slate-800 border border-indigo-500/50 rounded-lg text-white font-bold text-sm focus:ring-1 focus:ring-indigo-500">
                </div>
                <div id="mm-c-3-1" class="w-12 h-12 flex items-center justify-center rounded-lg bg-slate-900 border border-slate-700 text-white">21</div>
                <div id="mm-c-3-2" class="w-12 h-12 flex items-center justify-center rounded-lg bg-cyan-950/40 border border-cyan-600/60 text-cyan-300">28</div>
                <div id="mm-c-3-3" class="w-12 h-12 flex items-center justify-center rounded-lg bg-slate-900 border border-slate-700 text-white">42</div>
            </div>
        </div>
    </div>

    <!-- Feedback & Matrix Verification -->
    <div id="mm-status" class="text-center text-xs p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-800/60 text-emerald-300 font-medium">
        All 9 matrix cells match their respective row and column multiplier factors perfectly!
    </div>

    <div class="flex justify-center gap-2 text-xs">
        <button onclick="resetMysteryMatrix(1)" class="px-3 py-1.5 rounded-lg bg-indigo-600 text-white font-bold hover:bg-indigo-500 transition">Preset Puzzle A</button>
        <button onclick="resetMysteryMatrix(2)" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition">Preset Puzzle B</button>
    </div>
</div>
"""

sim2 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">02</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Visualizing Tens Bundles</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Base-Ten Rods & Units</span>
    </div>

    <!-- Tens Multiplier Slider -->
    <div class="bg-slate-950/60 p-4 rounded-xl border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-400">Number of Tens Bundles: <strong id="tens-count-val" class="text-cyan-400 text-base font-bold">4</strong></span>
            <span id="tens-place-label" class="px-2.5 py-1 rounded-full text-[11px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">4 Tens = 40</span>
        </div>
        <input type="range" id="tens-slider" min="1" max="10" step="1" value="4" oninput="updateTensSim(this.value)" class="w-full accent-cyan-500 cursor-pointer">
        <div class="flex justify-between text-[10px] text-slate-500 font-mono">
            <span>1 (10)</span>
            <span>2 (20)</span>
            <span>4 (40)</span>
            <span>6 (60)</span>
            <span>8 (80)</span>
            <span>10 (100 Flat)</span>
        </div>
    </div>

    <!-- Visual Rods Display Container -->
    <div id="tens-rods-container" class="flex flex-wrap items-center justify-center gap-2 min-h-[70px] bg-slate-950 p-4 rounded-xl border border-slate-800">
        <!-- Injected via updateTensSim -->
    </div>

    <div class="text-center text-xs text-slate-300 bg-slate-800/40 p-2.5 rounded-xl border border-slate-800 font-mono" id="tens-math-formula">
        Calculation: <strong>4 × 10 = 40 Units</strong> (4 Tens rods bundled together)
    </div>
</div>
"""

sim3 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">03</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Constructing Table Arrays</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Tens & Ones Area Breakdown</span>
    </div>

    <!-- Multiplier Selector -->
    <div class="flex items-center justify-between bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs">
        <span class="text-slate-400">Select Multiple of 15:</span>
        <div class="flex items-center gap-1.5 font-mono">
            <span class="text-slate-300">Multiply by:</span>
            <select id="table-mult-sel" onchange="renderTableArraySim(this.value)" class="bg-slate-800 text-white font-bold px-2 py-1 rounded-lg border border-slate-700">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6" selected>6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
            </select>
        </div>
    </div>

    <!-- Visual Area Model Rectangle -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
        <div class="flex justify-between text-[11px] font-mono text-slate-400 px-1">
            <span class="text-cyan-400 font-bold">Section 1: Tens Area (10)</span>
            <span class="text-amber-400 font-bold">Section 2: Ones Area (5)</span>
        </div>
        <div class="flex h-16 rounded-xl overflow-hidden border border-slate-700 font-mono font-bold text-xs">
            <!-- 10x Column (Width 66%) -->
            <div id="table-area-10" class="w-2/3 bg-cyan-600/30 border-r-2 border-dashed border-cyan-400 flex flex-col items-center justify-center text-cyan-300">
                <span id="table-math-10">6 × 10 = 60</span>
                <span class="text-[10px] text-slate-400 font-normal">Tens Block</span>
            </div>
            <!-- 5x Column (Width 33%) -->
            <div id="table-area-5" class="w-1/3 bg-amber-600/30 flex flex-col items-center justify-center text-amber-300">
                <span id="table-math-5">6 × 5 = 30</span>
                <span class="text-[10px] text-slate-400 font-normal">Ones Block</span>
            </div>
        </div>
    </div>

    <!-- Final Combined Sum Card -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs font-mono">
        <div class="bg-slate-800/60 p-3 rounded-xl border border-slate-700 text-slate-300">
            <span class="text-[10px] uppercase text-slate-400">Additive Equation</span>
            <div id="table-add-str" class="text-sm font-bold text-white mt-0.5">60 + 30 = 90</div>
        </div>
        <div class="bg-emerald-950/40 p-3 rounded-xl border border-emerald-800 text-emerald-200">
            <span class="text-[10px] uppercase text-emerald-400">Table Product Result</span>
            <div id="table-res-str" class="text-base font-bold mt-0.5">6 × 15 = 90</div>
        </div>
    </div>
</div>
"""

sim4 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-300 font-bold flex items-center justify-center text-sm">04</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Comparing Number Tables</h3>
        </div>
        <span class="text-xs text-pink-400 font-medium">Times-5 vs Times-15 Patterns</span>
    </div>

    <!-- Comparative Table Grid -->
    <div class="overflow-x-auto">
        <table class="w-full text-center text-xs font-mono border-collapse">
            <thead>
                <tr class="border-b border-slate-800 text-[10px] uppercase text-slate-400">
                    <th class="py-1.5 px-2">Multiplier</th>
                    <th class="py-1.5 px-2 text-pink-400 font-bold">Times-5 Table</th>
                    <th class="py-1.5 px-2 text-cyan-400 font-bold">Times-15 Table</th>
                    <th class="py-1.5 px-2 text-amber-400 font-bold">Scaling Ratio</th>
                </tr>
            </thead>
            <tbody id="comp-table-body" class="divide-y divide-slate-800/60">
                <!-- Injected via renderTableComparison -->
            </tbody>
        </table>
    </div>

    <div class="text-center text-xs text-slate-300 bg-slate-950/60 p-2.5 rounded-xl border border-slate-800">
        Key Pattern: Since <strong>15 = 3 × 5</strong>, every multiple in the 15-table is exactly <strong>3 times</strong> the corresponding 5-table multiple!
    </div>
</div>
"""

sim5 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">05</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Halving And Doubling</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Mental Arithmetic Factor Splitting</span>
    </div>

    <!-- Interactive Problem Picker -->
    <div class="flex flex-wrap items-center justify-center gap-2 text-xs">
        <span class="text-slate-400">Try Problem:</span>
        <button onclick="setHalvingProblem(3, 14)" class="px-2.5 py-1 rounded-lg bg-amber-600 text-white font-bold">3 × 14</button>
        <button onclick="setHalvingProblem(4, 16)" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200">4 × 16</button>
        <button onclick="setHalvingProblem(5, 18)" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200">5 × 18</button>
        <button onclick="setHalvingProblem(6, 12)" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200">6 × 12</button>
    </div>

    <!-- 3-Step Transformation Pipeline -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs font-mono">
        <!-- Step 1: Halving -->
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-center space-y-1">
            <span class="text-[10px] text-amber-400 uppercase font-bold">Step 1: Halve Factor</span>
            <div id="hd-step-1" class="text-sm font-bold text-white">Half of 14 is 7</div>
            <div class="text-[10px] text-slate-400">14 ÷ 2 = 7</div>
        </div>
        <!-- Step 2: Intermediate Product -->
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-center space-y-1">
            <span class="text-[10px] text-cyan-400 uppercase font-bold">Step 2: Base Product</span>
            <div id="hd-step-2" class="text-sm font-bold text-cyan-300">3 × 7 = 21</div>
            <div class="text-[10px] text-slate-400">Simpler table fact</div>
        </div>
        <!-- Step 3: Doubling -->
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-center space-y-1">
            <span class="text-[10px] text-emerald-400 uppercase font-bold">Step 3: Double Result</span>
            <div id="hd-step-3" class="text-sm font-bold text-emerald-300">21 × 2 = 42</div>
            <div class="text-[10px] text-slate-400">Final answer: 3 × 14 = 42</div>
        </div>
    </div>

    <div id="hd-summary-note" class="text-center text-xs text-slate-300 bg-slate-800/40 p-2.5 rounded-xl border border-slate-800 font-mono">
        Factor Manipulation Rule: Halving one factor and doubling the resulting product maintains exact mathematical equivalence.
    </div>
</div>
"""

sim6 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">06</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Scaling Decade Multiples</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Factoring Multiples of 10</span>
    </div>

    <!-- Interactive Factor Inputs -->
    <div class="grid grid-cols-2 gap-3 bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono">
        <div>
            <label class="block text-slate-400 text-[10px] mb-1">First Factor:</label>
            <input type="number" id="dec-f1" value="12" min="1" max="99" onchange="runDecadeScalingSim()" class="w-full bg-slate-800 border border-slate-700 text-white font-bold p-1.5 rounded-lg text-center">
        </div>
        <div>
            <label class="block text-slate-400 text-[10px] mb-1">Decade Factor (Multiple of 10):</label>
            <select id="dec-f2" onchange="runDecadeScalingSim()" class="w-full bg-slate-800 border border-slate-700 text-white font-bold p-1.5 rounded-lg text-center">
                <option value="10">10</option>
                <option value="20" selected>20</option>
                <option value="30">30</option>
                <option value="40">40</option>
                <option value="50">50</option>
            </select>
        </div>
    </div>

    <!-- 2-Step Factoring Pipeline -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-slate-400 text-[11px]">Decomposition Breakdown:</div>
        <div id="dec-breakdown-str" class="text-sm font-bold text-white">12 × 20 = 12 × 2 × 10</div>
        <div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-800">
            <div>
                <span class="text-[10px] text-cyan-400">Step 1: Single-Digit Multiplication</span>
                <div id="dec-step1-res" class="text-base font-bold text-cyan-300">12 × 2 = 24</div>
            </div>
            <div>
                <span class="text-[10px] text-emerald-400">Step 2: Base-10 Place-Value Shift</span>
                <div id="dec-step2-res" class="text-base font-bold text-emerald-300">24 × 10 = 240</div>
            </div>
        </div>
    </div>

    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <span class="text-slate-400 text-[11px]">Quick Jumps:</span>
        <button onclick="setDecadePreset(14, 10)" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">14 × 10</button>
        <button onclick="setDecadePreset(12, 20)" class="px-2 py-0.5 rounded bg-teal-600 text-white font-bold">12 × 20</button>
        <button onclick="setDecadePreset(25, 30)" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">25 × 30</button>
        <button onclick="setDecadePreset(30, 40)" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200">30 × 40</button>
    </div>
</div>
"""

sim7 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">07</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Transport Museum Fleet Math</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">Historical Fleet Capacity & Logistics</span>
    </div>

    <!-- Historical Vehicle Cards -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-center space-y-1">
            <span class="text-lg">🐂</span>
            <div class="text-white font-bold text-[11px]">Bullock Cart</div>
            <div class="text-blue-400 font-mono">4 seats</div>
            <div class="text-[10px] text-slate-500">Ancient Transit</div>
        </div>
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-center space-y-1">
            <span class="text-lg">🚋</span>
            <div class="text-white font-bold text-[11px]">Heritage Tram</div>
            <div class="text-emerald-400 font-mono">32 seats</div>
            <div class="text-[10px] text-slate-500">City Rail</div>
        </div>
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-center space-y-1">
            <span class="text-lg">🚂</span>
            <div class="text-white font-bold text-[11px]">Steam Train</div>
            <div class="text-amber-400 font-mono">210 seats</div>
            <div class="text-[10px] text-slate-500">15 Coaches</div>
        </div>
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-center space-y-1">
            <span class="text-lg">✈️</span>
            <div class="text-white font-bold text-[11px]">Vintage Plane</div>
            <div class="text-purple-400 font-mono">180 seats</div>
            <div class="text-[10px] text-slate-500">Air Transit</div>
        </div>
    </div>

    <!-- Fleet Capacity Computation Interactive Box -->
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between items-center text-slate-300">
            <span>Calculate Total for: <strong class="text-blue-400">Heritage Trams</strong></span>
            <div class="flex items-center gap-1 font-mono">
                <span>Number of Trams:</span>
                <input type="number" id="museum-tram-count" value="5" min="1" max="20" onchange="calcMuseumFleet()" class="w-12 bg-slate-800 text-white font-bold text-center rounded border border-slate-700 py-0.5">
            </div>
        </div>
        <div id="museum-fleet-res" class="text-sm font-bold text-white font-mono bg-slate-900 p-2.5 rounded-lg border border-slate-800">
            5 Trams × 32 seats per tram = 160 Total Passenger Capacity
        </div>
    </div>
</div>
"""

sim8 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-rose-500/20 text-rose-300 font-bold flex items-center justify-center text-sm">08</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Toy Train Box Grid</h3>
        </div>
        <span class="text-xs text-rose-400 font-medium">15 Coaches × 14 Children = 210</span>
    </div>

    <!-- 2x2 Box Area Grid Visualization -->
    <div class="flex justify-center">
        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 inline-block font-mono text-xs">
            <div class="grid grid-cols-3 gap-2 text-center">
                <!-- Top-Left Corner -->
                <div class="w-16 h-12 flex items-center justify-center font-bold text-rose-400 text-base">×</div>
                <!-- Column Headers (15 split into 10 + 5) -->
                <div class="w-24 h-12 flex flex-col items-center justify-center rounded-lg bg-indigo-950/60 border border-indigo-800 text-indigo-300 font-bold">
                    <span>10</span>
                    <span class="text-[9px] text-slate-400">Tens</span>
                </div>
                <div class="w-24 h-12 flex flex-col items-center justify-center rounded-lg bg-indigo-950/60 border border-indigo-800 text-indigo-300 font-bold">
                    <span>5</span>
                    <span class="text-[9px] text-slate-400">Ones</span>
                </div>

                <!-- Row 1 Header (14 split into 10) -->
                <div class="w-16 h-16 flex flex-col items-center justify-center rounded-lg bg-amber-950/60 border border-amber-800 text-amber-300 font-bold">
                    <span>10</span>
                    <span class="text-[9px] text-slate-400">Tens</span>
                </div>
                <!-- Chamber 1: 10x10 -->
                <div class="w-24 h-16 flex flex-col items-center justify-center rounded-lg bg-slate-900 border border-slate-700 text-white font-bold">
                    <span class="text-sm text-cyan-300">100</span>
                    <span class="text-[9px] text-slate-500">(10 × 10)</span>
                </div>
                <!-- Chamber 2: 5x10 -->
                <div class="w-24 h-16 flex flex-col items-center justify-center rounded-lg bg-slate-900 border border-slate-700 text-white font-bold">
                    <span class="text-sm text-cyan-300">50</span>
                    <span class="text-[9px] text-slate-500">(5 × 10)</span>
                </div>

                <!-- Row 2 Header (14 split into 4) -->
                <div class="w-16 h-16 flex flex-col items-center justify-center rounded-lg bg-amber-950/60 border border-amber-800 text-amber-300 font-bold">
                    <span>4</span>
                    <span class="text-[9px] text-slate-400">Ones</span>
                </div>
                <!-- Chamber 3: 10x4 -->
                <div class="w-24 h-16 flex flex-col items-center justify-center rounded-lg bg-slate-900 border border-slate-700 text-white font-bold">
                    <span class="text-sm text-cyan-300">40</span>
                    <span class="text-[9px] text-slate-500">(10 × 4)</span>
                </div>
                <!-- Chamber 4: 5x4 -->
                <div class="w-24 h-16 flex flex-col items-center justify-center rounded-lg bg-slate-900 border border-slate-700 text-white font-bold">
                    <span class="text-sm text-cyan-300">20</span>
                    <span class="text-[9px] text-slate-500">(5 × 4)</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Summing All Partial Products -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs font-mono">
        <div class="bg-slate-800/60 p-3 rounded-xl border border-slate-700 text-slate-300">
            <span class="text-[10px] uppercase text-slate-400">Partial Products Addition</span>
            <div class="text-sm font-bold text-white mt-0.5">100 + 50 + 40 + 20 = 210</div>
        </div>
        <div class="bg-rose-950/40 p-3 rounded-xl border border-rose-800 text-rose-200">
            <span class="text-[10px] uppercase text-rose-400">Total Train Capacity</span>
            <div class="text-base font-bold mt-0.5">15 × 14 = 210 Children</div>
        </div>
    </div>
</div>
"""

simulators_part1 = {1: sim1, 2: sim2, 3: sim3, 4: sim4, 5: sim5, 6: sim6, 7: sim7, 8: sim8}

