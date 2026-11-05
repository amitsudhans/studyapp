# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 9: Equal Groups
Part 2 Simulators: Slides 9 to 16
Bespoke SVG/HTML interactive simulators.
Zero human names (Gulabo, Anvi, Raghav, etc. replaced with generic roles).
Clean Unicode throughout.
"""

sim9 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-sky-500/20 text-sky-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Table Grid Symmetry</h3>
        </div>
        <span class="text-xs text-sky-400 font-medium">Diagonal Reflections & Row 8 Cycle</span>
    </div>

    <!-- Symmetry Controls -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setGridSymmetryPair(3, 7)" class="sg-btn px-2.5 py-1 rounded-lg bg-sky-500 text-slate-950 font-bold text-xs shadow">3 × 7 vs 7 × 3 (21)</button>
        <button onclick="setGridSymmetryPair(4, 9)" class="sg-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold border border-slate-700 text-xs">4 × 9 vs 9 × 4 (36)</button>
        <button onclick="setGridSymmetryPair(6, 8)" class="sg-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold border border-slate-700 text-xs">6 × 8 vs 8 × 6 (48)</button>
        <button onclick="toggleRow8Cycle()" id="btnRow8Cycle" class="sg-btn px-2.5 py-1 rounded-lg bg-slate-800 text-amber-300 font-semibold border border-slate-700 text-xs">Row 8 Ones Cycle</button>
    </div>

    <!-- Interactive Grid Display -->
    <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center space-y-2">
        <div id="gridSymmetryStatus" class="text-xs text-sky-300 font-bold">
            Row 3 Col 7 (21) mirrors Row 7 Col 3 (21) across the diagonal!
        </div>
        <div class="overflow-x-auto max-w-full">
            <table class="text-[10px] text-center font-mono border-collapse border border-slate-800" id="miniTableGrid">
                <!-- Dynamically generated 6x6 table sample -->
            </table>
        </div>
    </div>

    <div class="text-xs text-slate-400 bg-sky-950/30 p-2.5 rounded-lg border border-sky-800/40" id="gridNoteText">
        <strong>Commutative Reflection:</strong> Off-diagonal products mirror each other because a × b = b × a.
    </div>
</div>
"""

sim10 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Scaling Tens Products</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">Vehicle Wheels Multiplied by 10</span>
    </div>

    <!-- Vehicle Selector -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setScalingVehicle(3, 'Tricycles')" id="sv-btn-3" class="sv-btn px-2.5 py-1 rounded-lg bg-blue-500 text-slate-950 font-bold text-xs shadow">Tricycles (3 wheels)</button>
        <button onclick="setScalingVehicle(4, 'Cars')" id="sv-btn-4" class="sv-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold border border-slate-700 text-xs">Cars (4 wheels)</button>
        <button onclick="setScalingVehicle(6, 'Trucks')" id="sv-btn-6" class="sv-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold border border-slate-700 text-xs">Trucks (6 wheels)</button>
    </div>

    <!-- Interactive Tens Multiplier Slider -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="space-y-1">
            <div class="flex justify-between text-xs text-slate-400">
                <span>Vehicle Fleet Count (Multiples of 10):</span>
                <strong id="tensFleetCountLabel" class="text-blue-400 text-sm">60 Tricycles</strong>
            </div>
            <input type="range" id="tensCountSlider" min="10" max="90" step="10" value="60" oninput="updateTensFleetMath(this.value)" class="w-full accent-blue-500 cursor-pointer">
        </div>

        <!-- Scaling Calculation Card -->
        <div class="bg-slate-900 p-3 rounded-lg border border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-2 text-xs">
            <div class="text-slate-300">
                <span class="block text-slate-400 text-[11px]">Base Fact:</span>
                <strong id="baseFactText">6 × 3 = 18</strong>
            </div>
            <span class="text-slate-500 font-bold hidden sm:inline">➜ Scale by 10 ➜</span>
            <div class="text-right">
                <span class="block text-slate-400 text-[11px]">Scaled Total Wheels:</span>
                <strong id="scaledProductText" class="text-blue-400 font-black text-base">60 × 3 = 180</strong>
            </div>
        </div>
    </div>

    <div class="text-xs text-slate-300 bg-blue-950/30 p-2.5 rounded-lg border border-blue-800/40">
        <strong>Zero Rule:</strong> Calculate single-digit product first, then shift one place left by appending a zero (60 × 3 = 18 tens = 180).
    </div>
</div>
"""

sim11 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Tens Breakdown Area</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Decomposition & Partial Products</span>
    </div>

    <!-- Problem Presets -->
    <div class="flex justify-center gap-2">
        <button onclick="setBreakdownProblem(18, 4, 'Book Rack Screws')" id="bp-btn-18" class="bp-btn px-3 py-1.5 rounded-xl bg-teal-500 text-slate-950 font-bold text-xs shadow">18 × 4 (Screws)</button>
        <button onclick="setBreakdownProblem(23, 8, 'Cart Bamboo Poles')" id="bp-btn-23" class="bp-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700">23 × 8 (Bamboo)</button>
    </div>

    <!-- Area Model Visualizer -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-400 font-semibold" id="breakdownHeading">18 × 4 = (10 + 8) × 4</span>
            <span class="text-teal-400 font-bold font-mono text-sm" id="breakdownFinalSum">40 + 32 = 72</span>
        </div>

        <!-- Visual Partitioned Box -->
        <div class="grid grid-cols-12 gap-2 text-center text-xs">
            <div id="tensPartialBox" class="col-span-7 bg-teal-900/40 border border-teal-500/50 p-3 rounded-lg flex flex-col justify-center">
                <span class="text-slate-400 text-[10px]" id="tensLabel">10 × 4</span>
                <strong class="text-teal-300 text-base" id="tensVal">40</strong>
            </div>
            <div id="onesPartialBox" class="col-span-5 bg-teal-950/60 border border-teal-600/40 p-3 rounded-lg flex flex-col justify-center">
                <span class="text-slate-400 text-[10px]" id="onesLabel">8 × 4</span>
                <strong class="text-teal-300 text-base" id="onesVal">32</strong>
            </div>
        </div>
    </div>

    <div class="text-xs text-slate-300 bg-teal-950/30 p-2.5 rounded-lg border border-teal-800/40">
        <strong>Distributive Method:</strong> Break the multi-digit number into tens and ones. Multiply each part separately and sum the partial products!
    </div>
</div>
"""

sim12 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Animal Leg Counts</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Composite Word Problems</span>
    </div>

    <!-- Farm Animal Sliders -->
    <div class="grid grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between">
                <span class="text-slate-400">🪿 Geese (2 legs):</span>
                <strong id="geeseCountLabel" class="text-emerald-400">20 Geese</strong>
            </div>
            <input type="range" id="geeseSlider" min="0" max="40" step="5" value="20" oninput="updateAnimalLegsMath()" class="w-full accent-emerald-500 cursor-pointer">
        </div>
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between">
                <span class="text-slate-400">🐑 Sheep (4 legs):</span>
                <strong id="sheepCountLabel" class="text-emerald-400">15 Sheep</strong>
            </div>
            <input type="range" id="sheepSlider" min="0" max="30" step="5" value="15" oninput="updateAnimalLegsMath()" class="w-full accent-emerald-500 cursor-pointer">
        </div>
    </div>

    <!-- Calculated Sum Breakdown -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-2 text-xs">
        <div class="grid grid-cols-2 gap-2 text-center">
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
                <span class="text-slate-400 text-[11px]">Goose Legs:</span>
                <strong id="geeseLegsText" class="block text-white text-sm">20 × 2 = 40</strong>
            </div>
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
                <span class="text-slate-400 text-[11px]">Sheep Legs:</span>
                <strong id="sheepLegsText" class="block text-white text-sm">15 × 4 = 60</strong>
            </div>
        </div>
        <div class="pt-2 border-t border-slate-800 flex justify-between items-center">
            <span class="font-bold text-slate-300">Total Animal Legs in Meadow:</span>
            <span id="totalAnimalLegsText" class="text-base font-black text-emerald-400">40 + 60 = 100 Legs</span>
        </div>
    </div>

    <div class="text-xs text-slate-400 bg-slate-800/40 p-2.5 rounded-lg border border-slate-700/40">
        <strong>Composite Logic:</strong> Solve each species grouping separately, then add the sub-totals together to find the grand total!
    </div>
</div>
"""

sim13 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-purple-500/20 text-purple-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Partial Quotient Division</h3>
        </div>
        <span class="text-xs text-purple-400 font-medium">Friendly Chunking (10s & 5s)</span>
    </div>

    <!-- Division Problem Selector -->
    <div class="flex justify-center gap-2">
        <button onclick="setDivisionProblem(48, 3, 'Rickshaw Wheels')" id="dp-btn-48" class="dp-btn px-3 py-1.5 rounded-xl bg-purple-500 text-slate-950 font-bold text-xs shadow">48 ÷ 3 (Rickshaws)</button>
        <button onclick="setDivisionProblem(64, 4, 'Shuttlecock Tubes')" id="dp-btn-64" class="dp-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700">64 ÷ 4 (Shuttlecocks)</button>
    </div>

    <!-- Step-by-Step Chunking Display -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-2 text-xs font-mono">
        <div class="flex justify-between items-center text-slate-400 pb-2 border-b border-slate-800 font-sans">
            <span id="divProblemLabel">48 Wheels ÷ 3 Wheels per Rickshaw</span>
            <span id="divQuotientResult" class="text-purple-400 font-bold text-sm">Quotient: 16</span>
        </div>

        <div class="space-y-1.5 text-slate-300" id="chunkingStepsArea">
            <div class="flex justify-between bg-slate-900 p-2 rounded border border-slate-800">
                <span>Chunk 1: 10 groups of 3 = 30</span>
                <span class="text-purple-300">48 - 30 = 18 left</span>
            </div>
            <div class="flex justify-between bg-slate-900 p-2 rounded border border-slate-800">
                <span>Chunk 2: 6 groups of 3 = 18</span>
                <span class="text-emerald-400">18 - 18 = 0 left!</span>
            </div>
            <div class="text-right text-purple-400 font-bold font-sans pt-1">
                Total Rickshaws = 10 + 6 = 16
            </div>
        </div>
    </div>

    <div class="text-xs text-slate-300 bg-purple-950/30 p-2.5 rounded-lg border border-purple-800/40">
        <strong>Friendly Chunking:</strong> Subtract easy multiples (like 10s or 5s) instead of guessing. Add partial quotients together at the end!
    </div>
</div>
"""

sim14 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Scaling Hundreds Math</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">Multiples of 100 & Large Batches</span>
    </div>

    <!-- Problem Selector -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setHundredsScenario('cars')" id="hs-btn-cars" class="hs-btn px-2.5 py-1.5 rounded-xl bg-orange-500 text-slate-950 font-bold text-xs shadow">500 Cars (4 Pass.)</button>
        <button onclick="setHundredsScenario('bus')" id="hs-btn-bus" class="hs-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700">8 Shuttles (125 Pass.)</button>
        <button onclick="setHundredsScenario('cups')" id="hs-btn-cups" class="hs-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700">6 Crates (174 Cups)</button>
    </div>

    <!-- Calculation Container -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs">
            <span id="hundredsEquationLabel" class="text-slate-300 font-semibold">500 Cars × 4 Passengers</span>
            <strong id="hundredsTotalLabel" class="text-orange-400 text-base font-black">2,000 Passengers</strong>
        </div>

        <div id="hundredsBreakdownCard" class="bg-slate-900 p-3 rounded-lg border border-slate-800 text-xs text-slate-300 space-y-1">
            <div>Base Fact: <strong>5 × 4 = 20</strong></div>
            <div>Scale by 100: <strong>20 hundreds = 2,000</strong></div>
        </div>
    </div>

    <div class="text-xs text-slate-400 bg-slate-800/40 p-2.5 rounded-lg border border-slate-700/40">
        <strong>Scaling Rule:</strong> Multiplying by hundreds is identical to multiplying by single digits and affixing two zeros to shift two place values!
    </div>
</div>
"""

sim15 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Sharing Measure Division</h3>
        </div>
        <span class="text-xs text-pink-400 font-medium">Partitive vs Quotative Grouping</span>
    </div>

    <!-- Division Meaning Toggle -->
    <div class="flex justify-center gap-2">
        <button onclick="setDivType('sharing')" id="dt-btn-sharing" class="dt-btn px-3 py-1.5 rounded-xl bg-pink-500 text-slate-950 font-bold text-xs shadow">Sharing Division (Find Share)</button>
        <button onclick="setDivType('measure')" id="dt-btn-measure" class="dt-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700">Measurement Division (Find Count)</button>
    </div>

    <!-- Interactive Visual Representation -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs">
            <h4 id="divConceptTitle" class="font-bold text-pink-300 text-sm">72 People Shared in 9 Boats</h4>
            <span id="divConceptFormula" class="font-mono text-white text-xs bg-slate-900 px-2 py-1 rounded">72 ÷ 9 = 8 per boat</span>
        </div>

        <p id="divConceptDesc" class="text-xs text-slate-300 leading-relaxed">
            <strong>Sharing (Partitive):</strong> The number of boats (groups) is fixed at 9. Division determines each boat's passenger capacity: 8 people per boat.
        </p>

        <div id="divVisualIcons" class="flex flex-wrap gap-1.5 justify-center p-2 bg-slate-900 rounded-lg border border-slate-800">
            <!-- Dynamically populated boats or trucks -->
        </div>
    </div>

    <div class="text-xs text-slate-400 bg-pink-950/30 p-2.5 rounded-lg border border-pink-800/40">
        <strong>Core Distinction:</strong> Sharing division finds the size of each group. Measurement division finds how many equal groups can be made.
    </div>
</div>
"""

sim16 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Logical Reasoning Statements</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">True / Sometimes / Never Validator</span>
    </div>

    <!-- Statement Selector -->
    <div class="space-y-2">
        <span class="text-xs text-slate-400 font-semibold block">Select a Mathematical Claim:</span>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-1.5 text-xs text-center">
            <button onclick="setLogicClaim(1)" id="lc-btn-1" class="lc-btn p-2 rounded-xl bg-emerald-500 text-slate-950 font-bold shadow">Claim 1: Even × Even</button>
            <button onclick="setLogicClaim(2)" id="lc-btn-2" class="lc-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700">Claim 2: Number ÷ 2</button>
            <button onclick="setLogicClaim(3)" id="lc-btn-3" class="lc-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700">Claim 3: Odd × Odd</button>
        </div>
    </div>

    <!-- Statement Analysis Display -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 text-xs text-slate-200">
            <strong class="text-slate-400 block mb-1">Statement:</strong>
            <span id="logicStatementText" class="text-sm font-semibold text-white">The product of any two even numbers is always even.</span>
        </div>

        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-400">Mathematical Classification:</span>
            <strong id="logicVerdictBadge" class="px-3 py-1 rounded-full bg-emerald-950 text-emerald-400 border border-emerald-800 font-bold">ALWAYS TRUE</strong>
        </div>

        <div id="logicProofText" class="text-xs text-slate-300 bg-slate-900/60 p-2.5 rounded-lg border border-slate-800">
            Testing: 2 × 4 = 8 (Even), 6 × 8 = 48 (Even). Even numbers have a factor of 2, so their product always contains a factor of 2.
        </div>
    </div>

    <div class="text-xs text-slate-400 bg-slate-800/40 p-2.5 rounded-lg border border-slate-700/40">
        <strong>Proof Technique:</strong> A statement is 'Always True' if proven universally. If even a single counterexample exists, it is 'Sometimes True' or 'Never True'!
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

if __name__ == "__main__":
    print(f"Loaded {len(simulators_part2)} simulators for Part 2.")
    for k, v in simulators_part2.items():
        print(f"Sim {k}: {len(v)} chars")

