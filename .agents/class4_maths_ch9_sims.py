# -*- coding: utf-8 -*-
"""Class 4 Mathematics Chapter 9 Simulators"""

simulators = {
    1: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">01</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Animal Jump Multiples</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Number Trail Skip-Counting</span>
    </div>

    <!-- Animal Selector -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setJumpAnimal(3, 'Frog')" id="ja-btn-3" class="ja-btn px-2.5 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs shadow transition">Frog (3 steps)</button>
        <button onclick="setJumpAnimal(4, 'Squirrel')" id="ja-btn-4" class="ja-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Squirrel (4 steps)</button>
        <button onclick="setJumpAnimal(6, 'Rabbit')" id="ja-btn-6" class="ja-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Rabbit (6 steps)</button>
        <button onclick="setJumpAnimal(8, 'Kangaroo')" id="ja-btn-8" class="ja-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Kangaroo (8 steps)</button>
    </div>

    <!-- Interactive Track SVG -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-400">Current Jump Count: <strong id="jumpCountLabel" class="text-white text-sm">4 Jumps</strong></span>
            <span id="jumpFormulaLabel" class="text-emerald-400 font-bold font-mono text-sm">4 × 3 = Step 12</span>
        </div>
        <input type="range" id="jumpSlider" min="1" max="8" step="1" value="4" oninput="updateAnimalJumps(this.value)" class="w-full accent-emerald-500 cursor-pointer">

        <!-- Trail stepping stones -->
        <div class="overflow-x-auto py-2">
            <div id="trailMarkersContainer" class="flex gap-1.5 min-w-[500px] justify-between">
                <!-- Dynamically generated trail stones -->
            </div>
        </div>
    </div>

    <div id="jumpDescCard" class="bg-emerald-950/40 p-3 rounded-xl border border-emerald-800/40 text-xs text-emerald-200">
        <strong>Observation:</strong> Each jump adds an equal group of steps. 4 jumps of 3 steps = 12. Skip-counting builds multiplication tables naturally!
    </div>
</div>
''',
    2: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">02</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Target Step Paths</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Path Reachability & Division</span>
    </div>

    <!-- Target Milestone Selector -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setTargetMilestone(48)" class="tm-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">Target: 48</button>
        <button onclick="setTargetMilestone(60)" class="tm-btn px-2.5 py-1 rounded-lg bg-teal-500 text-slate-950 text-xs font-bold shadow">Target: 60</button>
        <button onclick="setTargetMilestone(67)" class="tm-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">Target: 67 (Skip test)</button>
        <button onclick="setTargetMilestone(72)" class="tm-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">Target: 72</button>
    </div>

    <!-- Divisibility Table -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-2">
        <div class="text-xs text-slate-400 font-semibold mb-2 flex justify-between">
            <span>Can Animals Reach Milestone <strong id="activeTargetNum" class="text-white">60</strong>?</span>
            <span class="text-[11px] text-teal-400">Target ÷ Step Size</span>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
            <div id="reach-frog" class="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                <span class="block text-slate-400 text-[10px]">Frog (3)</span>
                <strong class="text-emerald-400 text-sm">20 Jumps</strong>
                <span class="block text-[10px] text-slate-500">60 ÷ 3 = 20 (Exact)</span>
            </div>
            <div id="reach-squirrel" class="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                <span class="block text-slate-400 text-[10px]">Squirrel (4)</span>
                <strong class="text-emerald-400 text-sm">15 Jumps</strong>
                <span class="block text-[10px] text-slate-500">60 ÷ 4 = 15 (Exact)</span>
            </div>
            <div id="reach-rabbit" class="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                <span class="block text-slate-400 text-[10px]">Rabbit (6)</span>
                <strong class="text-emerald-400 text-sm">10 Jumps</strong>
                <span class="block text-[10px] text-slate-500">60 ÷ 6 = 10 (Exact)</span>
            </div>
            <div id="reach-kangaroo" class="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                <span class="block text-slate-400 text-[10px]">Kangaroo (8)</span>
                <strong class="text-rose-400 text-sm">Skips!</strong>
                <span class="block text-[10px] text-slate-500">Rem 4 (Lands on 56, 64)</span>
            </div>
        </div>
    </div>

    <div id="reachSummaryText" class="text-xs text-slate-300 bg-slate-800/40 p-2.5 rounded-lg border border-slate-700/40">
        <strong>Rule:</strong> An animal reaches a milestone only if the target is an exact multiple (remainder is zero). If a remainder exists, the milestone is skipped!
    </div>
</div>
''',
    3: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">03</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Shared Landing Numbers</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Common Multiples Explorer</span>
    </div>

    <!-- Pair Selector -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setSharedPair('frog_squirrel')" id="sp-btn-fs" class="sp-btn px-2.5 py-1.5 rounded-xl bg-cyan-500 text-slate-950 font-bold text-xs shadow transition">Frog (3) & Squirrel (4)</button>
        <button onclick="setSharedPair('rabbit_kangaroo')" id="sp-btn-rk" class="sp-btn px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Rabbit (6) & Kangaroo (8)</button>
    </div>

    <!-- Dual Trail Alignment Visualizer -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="text-xs text-slate-400 font-semibold flex justify-between">
            <span>Overlapping Milestones (0 to 48):</span>
            <span id="lcmLabel" class="text-cyan-400 font-bold">First Meeting: Step 12</span>
        </div>
        <div id="dualTrailDisplay" class="space-y-2">
            <!-- Dynamically populated dual landing rows -->
        </div>
        <div id="commonMultiplesList" class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-200">
            <strong>Shared Landing Stones:</strong> <span class="text-cyan-300 font-bold font-mono">12, 24, 36, 48</span> (Multiples of 12)
        </div>
    </div>

    <div class="text-xs text-slate-400 bg-cyan-950/30 p-2.5 rounded-lg border border-cyan-800/40">
        <strong>Mathematical Insight:</strong> All shared landing numbers are multiples of the Least Common Multiple (LCM)!
    </div>
</div>
''',
    4: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">04</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Cat Rat Chase</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Linear Pursuit Simulation</span>
    </div>

    <!-- Turn Controls -->
    <div class="flex items-center justify-between bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-xs">
        <span class="text-slate-400">Turn: <strong id="chaseTurnDisplay" class="text-white text-sm">0</strong> / 8</span>
        <div class="flex gap-2">
            <button onclick="advanceChaseTurn()" id="btnChaseAdvance" class="px-3 py-1.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-lg text-xs shadow transition">Next Bound 🐾</button>
            <button onclick="resetChaseGame()" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs transition">Reset</button>
        </div>
    </div>

    <!-- Track Display -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="grid grid-cols-2 gap-3 text-xs">
            <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800 flex justify-between items-center">
                <span class="text-slate-400">🐭 Mouse (starts 24, +2):</span>
                <strong id="mousePosDisplay" class="text-emerald-400 text-sm">Step 24</strong>
            </div>
            <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800 flex justify-between items-center">
                <span class="text-slate-400">🐱 Cat (starts 12, +3):</span>
                <strong id="catPosDisplay" class="text-amber-400 text-sm">Step 12</strong>
            </div>
        </div>

        <div id="chaseStatusAlert" class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-center text-slate-300 font-medium">
            Mouse is running toward the safety hole at Step 40! Click 'Next Bound'.
        </div>
    </div>

    <div class="text-[11px] text-slate-400 flex justify-between px-1">
        <span>Mouse speed: 2 steps/bound</span>
        <span>Cat speed: 3 steps/bound</span>
        <span>Safety Hole: Step 40</span>
    </div>
</div>
''',
    5: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">05</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Grid Equation Hunt</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Spot Fact Triplets</span>
    </div>

    <!-- Interactive 4x4 Grid Matrix -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-400">Click 3 connected cells to form an equation:</span>
            <span class="text-indigo-400 font-bold">Selected: <span id="huntSelectedText">None</span></span>
        </div>

        <div class="grid grid-cols-4 gap-2 max-w-[280px] mx-auto text-center" id="huntGridMatrix">
            <!-- 16 number cells generated dynamically -->
        </div>

        <div id="huntFeedbackMsg" class="p-2 rounded-lg bg-slate-900 border border-slate-800 text-xs text-center text-slate-300 min-h-[32px] flex items-center justify-center">
            Find equations like: 4 × 5 = 20 or 24 ÷ 4 = 6!
        </div>
    </div>

    <div class="flex justify-between items-center text-xs px-1">
        <span class="text-slate-400">Equations Found: <strong id="huntEquationsFound" class="text-white">0</strong></span>
        <button onclick="resetHuntGrid()" class="text-indigo-400 hover:text-indigo-300 underline">Reset Grid</button>
    </div>
</div>
''',
    6: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-300 font-bold flex items-center justify-center text-sm">06</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Flower Petal Groups</h3>
        </div>
        <span class="text-xs text-pink-400 font-medium">Multiplier, Multiplicand & Product</span>
    </div>

    <!-- Mode Selector -->
    <div class="flex justify-center gap-2">
        <button onclick="setFlowerMode('lily')" id="fm-btn-lily" class="fm-btn px-3 py-1.5 rounded-xl bg-pink-500 text-slate-950 font-bold text-xs shadow transition">Lilies (6 Petals Each)</button>
        <button onclick="setFlowerMode('hibiscus')" id="fm-btn-hibiscus" class="fm-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700 transition">Hibiscus Division (5 Petals)</button>
    </div>

    <!-- Flower Model Container -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div id="flowerControlArea" class="space-y-1.5">
            <div class="flex justify-between text-xs text-slate-400">
                <span id="flowerSliderLabel">Number of Lily Blossoms (Multiplier):</span>
                <strong id="flowerSliderVal" class="text-pink-400 text-sm">12 Flowers</strong>
            </div>
            <input type="range" id="flowerCountSlider" min="1" max="15" step="1" value="12" oninput="updateFlowerMath(this.value)" class="w-full accent-pink-500 cursor-pointer">
        </div>

        <div class="grid grid-cols-3 gap-2 text-center text-xs">
            <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                <span class="block text-[10px] text-slate-400 uppercase font-semibold">Multiplier</span>
                <strong id="termMultiplier" class="text-white text-base">12</strong>
                <span class="block text-[9px] text-slate-500">Equal Groups</span>
            </div>
            <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                <span class="block text-[10px] text-slate-400 uppercase font-semibold">Multiplicand</span>
                <strong id="termMultiplicand" class="text-white text-base">6</strong>
                <span class="block text-[9px] text-slate-500">Group Size</span>
            </div>
            <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                <span class="block text-[10px] text-slate-400 uppercase font-semibold">Product</span>
                <strong id="termProduct" class="text-pink-400 text-base font-black">72</strong>
                <span class="block text-[9px] text-slate-500">Total Petals</span>
            </div>
        </div>
    </div>

    <div id="flowerExplNote" class="text-xs text-slate-300 bg-pink-950/30 p-2.5 rounded-lg border border-pink-800/40">
        <strong>Vocabulary:</strong> Multiplier (12 flowers) × Multiplicand (6 petals) = Product (72 petals in total).
    </div>
</div>
''',
    7: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">07</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Rectangular Planting Arrays</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">Commutative Property (a × b = b × a)</span>
    </div>

    <!-- Array Dimensions Sliders -->
    <div class="grid grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between">
                <span class="text-slate-400">Rows:</span>
                <strong id="arrayRowsLabel" class="text-orange-400">4 Rows</strong>
            </div>
            <input type="range" id="arrayRowsSlider" min="2" max="6" step="1" value="4" oninput="updateArrayDimensions()" class="w-full accent-orange-500 cursor-pointer">
        </div>
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between">
                <span class="text-slate-400">Columns:</span>
                <strong id="arrayColsLabel" class="text-orange-400">6 Columns</strong>
            </div>
            <input type="range" id="arrayColsSlider" min="2" max="6" step="1" value="6" oninput="updateArrayDimensions()" class="w-full accent-orange-500 cursor-pointer">
        </div>
    </div>

    <!-- Visual Array Grid -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs">
            <span id="arrayFormulaText" class="text-orange-300 font-bold">4 Rows × 6 Columns = 24 Saplings</span>
            <button onclick="rotateArray()" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-700 text-[11px] font-semibold transition">Rotate 90° 🔄</button>
        </div>
        <div id="seedlingGridContainer" class="flex flex-col gap-1.5 items-center justify-center min-h-[120px] p-2 bg-slate-900 rounded-lg border border-slate-800">
            <!-- Dynamically generated rows of seedling dots -->
        </div>
    </div>

    <div class="text-xs text-slate-300 bg-orange-950/30 p-2.5 rounded-lg border border-orange-800/40">
        <strong>Commutative Rule:</strong> 4 × 6 = 24 and 6 × 4 = 24. Rotating an array swaps rows and columns without changing the total count!
    </div>
</div>
''',
    8: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-yellow-500/20 text-yellow-300 font-bold flex items-center justify-center text-sm">08</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Doubling Magic Patterns</h3>
        </div>
        <span class="text-xs text-yellow-400 font-medium">Mental Arithmetic & Even Parity</span>
    </div>

    <!-- Magic Wand Interaction -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 text-center space-y-3">
        <div class="flex justify-between items-center text-xs px-2">
            <span class="text-slate-400">Current Amount:</span>
            <button onclick="doubleMagicNumber()" class="px-3 py-1.5 rounded-xl bg-yellow-500 hover:bg-yellow-400 text-slate-950 font-bold text-xs shadow flex items-center gap-1.5 transition">
                <span>✨</span> Wave Wand (Double)
            </button>
            <button onclick="resetMagicDouble()" class="text-xs text-slate-400 hover:text-slate-200 underline">Reset (3)</button>
        </div>

        <div class="py-2">
            <span id="magicNumberDisplay" class="text-4xl font-black text-yellow-400 font-mono">3</span>
            <span class="block text-xs text-slate-400 mt-1" id="magicFormulaText">Initial Count</span>
        </div>

        <!-- Parity Analyzer -->
        <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800 flex justify-between items-center text-xs">
            <span class="text-slate-400">Ones Digit: <strong id="magicOnesDigit" class="text-white">3</strong></span>
            <span id="magicParityBadge" class="px-2 py-0.5 rounded bg-amber-950 text-amber-300 border border-amber-800 font-bold">ODD</span>
            <span class="text-slate-400">Next Double: <strong id="magicNextDouble" class="text-yellow-300">6</strong></span>
        </div>
    </div>

    <div class="text-xs text-slate-300 bg-yellow-950/30 p-2.5 rounded-lg border border-yellow-800/40">
        <strong>Parity Rule:</strong> Doubling ANY whole number always produces an EVEN result ending in 0, 2, 4, 6, or 8!
    </div>
</div>
''',
    9: '''
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
''',
    10: '''
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
''',
    11: '''
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
''',
    12: '''
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
''',
    13: '''
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
''',
    14: '''
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
''',
    15: '''
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
''',
    16: '''
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
''',
}
