# -*- coding: utf-8 -*-
"""Class 4 Mathematics Chapter 10 Simulators Dictionary"""

SIMULATORS = {
    1: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">01</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Nim Addition Game (To 10)</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Add 1 or 2 Strategy</span>
    </div>

    <!-- Running Total Display -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-4 text-center space-y-2">
        <div class="text-xs text-slate-400 uppercase tracking-wider font-semibold">Running Total</div>
        <div id="nim-total" class="text-4xl sm:text-5xl font-black text-amber-400 font-mono">0</div>
        <div id="nim-status" class="text-xs text-slate-300">Turn: <span class="font-bold text-emerald-400">Player 1</span>. Choose to add 1 or 2.</div>
    </div>

    <!-- Visual Track 0 to 10 -->
    <div class="grid grid-cols-11 gap-1 sm:gap-1.5 p-2 bg-slate-950/50 rounded-xl border border-slate-800/80 text-center font-mono text-xs">
        <div id="nim-step-0" class="py-1.5 rounded-lg bg-emerald-500/30 text-emerald-300 font-bold border border-emerald-500/50">0</div>
        <div id="nim-step-1" class="py-1.5 rounded-lg bg-slate-800/60 text-slate-400">1</div>
        <div id="nim-step-2" class="py-1.5 rounded-lg bg-slate-800/60 text-slate-400">2</div>
        <div id="nim-step-3" class="py-1.5 rounded-lg bg-slate-800/60 text-slate-400">3</div>
        <div id="nim-step-4" class="py-1.5 rounded-lg bg-slate-800/60 text-slate-400">4</div>
        <div id="nim-step-5" class="py-1.5 rounded-lg bg-slate-800/60 text-slate-400">5</div>
        <div id="nim-step-6" class="py-1.5 rounded-lg bg-slate-800/60 text-slate-400">6</div>
        <div id="nim-step-7" class="py-1.5 rounded-lg bg-slate-800/60 text-slate-400">7</div>
        <div id="nim-step-8" class="py-1.5 rounded-lg bg-slate-800/60 text-slate-400">8</div>
        <div id="nim-step-9" class="py-1.5 rounded-lg bg-slate-800/60 text-slate-400">9</div>
        <div id="nim-step-10" class="py-1.5 rounded-lg bg-amber-500/20 text-amber-300 font-bold border border-amber-500/40">10</div>
    </div>

    <!-- Controls -->
    <div class="flex items-center justify-center gap-3">
        <button onclick="nimAdd(1)" id="nim-btn-1" class="px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm shadow transition active:scale-95">+1</button>
        <button onclick="nimAdd(2)" id="nim-btn-2" class="px-5 py-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-sm shadow transition active:scale-95">+2</button>
        <button onclick="resetNim()" class="px-3.5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition">Reset</button>
    </div>
</div>
''',
    2: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">02</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Winning Position Backward Induction</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Milestones: 1, 4, 7, 10</span>
    </div>

    <!-- Interactive Tree / Sequence -->
    <div class="grid grid-cols-4 gap-2 text-center">
        <button onclick="inspectNimNode(1)" id="nim-node-1" class="nim-node p-3 rounded-xl bg-slate-800 border border-slate-700 hover:border-cyan-500 transition">
            <div class="text-xs text-slate-400">Milestone 1</div>
            <div class="text-2xl font-black text-white font-mono mt-1">1</div>
            <div class="text-[10px] text-emerald-400 mt-1 font-semibold">Opening Key</div>
        </button>
        <button onclick="inspectNimNode(4)" id="nim-node-4" class="nim-node p-3 rounded-xl bg-slate-800 border border-slate-700 hover:border-cyan-500 transition">
            <div class="text-xs text-slate-400">Milestone 2</div>
            <div class="text-2xl font-black text-white font-mono mt-1">4</div>
            <div class="text-[10px] text-cyan-400 mt-1 font-semibold">Controls 2 or 3</div>
        </button>
        <button onclick="inspectNimNode(7)" id="nim-node-7" class="nim-node p-3 rounded-xl bg-cyan-500/20 border border-cyan-500 text-cyan-300 transition">
            <div class="text-xs text-cyan-400">Milestone 3</div>
            <div class="text-2xl font-black text-white font-mono mt-1">7</div>
            <div class="text-[10px] text-amber-400 mt-1 font-semibold">Traps 8 or 9</div>
        </button>
        <button onclick="inspectNimNode(10)" id="nim-node-10" class="nim-node p-3 rounded-xl bg-amber-500/20 border border-amber-500/50 transition">
            <div class="text-xs text-amber-400">Winning Goal</div>
            <div class="text-2xl font-black text-amber-300 font-mono mt-1">10</div>
            <div class="text-[10px] text-amber-300 mt-1 font-semibold">Victory!</div>
        </button>
    </div>

    <!-- Explanatory Box -->
    <div id="nim-node-exp" class="bg-slate-950/60 border border-slate-800 rounded-xl p-3.5 text-xs text-slate-300 leading-relaxed space-y-1">
        <div class="font-bold text-white text-sm">Controlling Milestone 7:</div>
        <div>If you reach 7, the opponent can only choose <strong>8</strong> (by adding 1) or <strong>9</strong> (by adding 2). From 8, you add 2 to hit 10! From 9, you add 1 to hit 10! Reaching 7 guarantees victory.</div>
    </div>
</div>
''',
    3: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">03</span>
            <h3 class="font-bold text-white text-sm sm:text-base">13 × 13 Addition Chart Patterns</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Constant Anti-Diagonals</span>
    </div>

    <!-- Filter Buttons -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <span class="text-slate-400 mr-1 text-[11px]">Highlight Sum:</span>
        <button onclick="highlightChartSum(6)" class="chart-sum-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">6</button>
        <button onclick="highlightChartSum(9)" class="chart-sum-btn px-2.5 py-1 rounded-lg bg-amber-500 text-slate-950 font-bold">9</button>
        <button onclick="highlightChartSum(12)" class="chart-sum-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">12</button>
        <button onclick="highlightChartSum(15)" class="chart-sum-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">15</button>
        <button onclick="highlightChartSum(18)" class="chart-sum-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">18</button>
        <button onclick="highlightChartSum(-1)" class="chart-sum-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-400 hover:bg-slate-700">Clear</button>
    </div>

    <!-- Addition Chart Preview (7x7 visible slice with toggle) -->
    <div class="overflow-x-auto bg-slate-950/70 p-3 rounded-xl border border-slate-800">
        <div id="addition-grid" class="grid grid-cols-8 gap-1 min-w-[320px] text-center font-mono text-xs">
            <!-- Populated dynamically via JS -->
        </div>
    </div>

    <div id="chart-stat-badge" class="text-center text-xs text-amber-300 font-medium">
        Sum 9 appears across 10 distinct cell combinations forming a perfect diagonal line!
    </div>
</div>
''',
    4: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-purple-500/20 text-purple-300 font-bold flex items-center justify-center text-sm">04</span>
            <h3 class="font-bold text-white text-sm sm:text-base">3 × 3 Window Frame Centroid</h3>
        </div>
        <span class="text-xs text-purple-400 font-medium">Sum = 9 × Center</span>
    </div>

    <!-- Center Selector -->
    <div class="flex items-center justify-center gap-2 text-xs">
        <span class="text-slate-400">Center Number (C):</span>
        <button onclick="setWindowCenter(6)" class="wc-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">6</button>
        <button onclick="setWindowCenter(8)" class="wc-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">8</button>
        <button onclick="setWindowCenter(10)" class="wc-btn px-2.5 py-1 rounded-lg bg-purple-600 text-white font-bold">10</button>
        <button onclick="setWindowCenter(12)" class="wc-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">12</button>
    </div>

    <!-- 3x3 Window Visual -->
    <div class="flex justify-center">
        <div id="window-frame-cells" class="grid grid-cols-3 gap-2 w-56 text-center font-mono">
            <!-- Cell 1 to 9 generated via JS -->
        </div>
    </div>

    <!-- Sum Breakdown -->
    <div class="grid grid-cols-2 gap-2 text-xs font-mono">
        <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800 text-center">
            <div class="text-slate-400 text-[11px]">Center Row Sum (3 × C)</div>
            <div id="row-sum-val" class="text-lg font-bold text-cyan-400 mt-1">9 + 10 + 11 = 30</div>
        </div>
        <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800 text-center">
            <div class="text-slate-400 text-[11px]">Total Frame Sum (9 × C)</div>
            <div id="total-sum-val" class="text-lg font-bold text-purple-400 mt-1">9 × 10 = 90</div>
        </div>
    </div>
</div>
''',
    5: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-rose-500/20 text-rose-300 font-bold flex items-center justify-center text-sm">05</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Reverse and Add Multiples of 11</h3>
        </div>
        <span class="text-xs text-rose-400 font-medium">11 × (a + b) Invariant</span>
    </div>

    <!-- Preset Numbers -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <span class="text-slate-400 mr-1 text-[11px]">Try 2-Digit Number:</span>
        <button onclick="setReverseNum(27)" class="rev-btn px-2.5 py-1 rounded-lg bg-rose-600 text-white font-bold">27</button>
        <button onclick="setReverseNum(34)" class="rev-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">34</button>
        <button onclick="setReverseNum(48)" class="rev-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">48</button>
        <button onclick="setReverseNum(56)" class="rev-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">56</button>
        <button onclick="setReverseNum(73)" class="rev-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">73</button>
    </div>

    <!-- Equation Visualizer -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-4 text-center space-y-3">
        <div class="flex items-center justify-center gap-3 font-mono text-xl sm:text-2xl font-bold">
            <span id="rev-orig" class="text-cyan-400">27</span>
            <span class="text-slate-500">+</span>
            <span id="rev-swap" class="text-rose-400">72</span>
            <span class="text-slate-500">=</span>
            <span id="rev-total" class="text-amber-400">99</span>
        </div>
        <div id="rev-formula" class="text-xs text-slate-300 font-mono bg-slate-900/80 py-1.5 px-3 rounded-lg inline-block border border-slate-800">
            11 × (2 + 7) = 11 × 9 = 99
        </div>
    </div>

    <div id="rev-palindrome-note" class="text-center text-xs text-emerald-400 font-medium">
        99 is a symmetric palindromic number and an exact multiple of 11!
    </div>
</div>
''',
    6: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">06</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Wildlife Census Population Explorer</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Endangered Species Metrics</span>
    </div>

    <!-- Species Tabs -->
    <div class="flex justify-center gap-2 text-xs">
        <button onclick="setWildlifeSpecies('elephants')" id="wl-tab-elephants" class="wl-tab px-3 py-1.5 rounded-xl bg-teal-500 text-slate-950 font-bold">Elephants</button>
        <button onclick="setWildlifeSpecies('tigers')" id="wl-tab-tigers" class="wl-tab px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300">Tigers</button>
        <button onclick="setWildlifeSpecies('leopards')" id="wl-tab-leopards" class="wl-tab px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300">Leopards</button>
    </div>

    <!-- State Population Cards -->
    <div id="wildlife-cards" class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs font-mono">
        <!-- Injected via JS -->
    </div>

    <!-- Combined Total Badge -->
    <div id="wildlife-summary" class="bg-slate-950/70 border border-slate-800 rounded-xl p-3 text-center text-xs text-slate-300">
        Karnataka (6,049) + Kerala (3,054) = <span class="font-bold text-teal-400">9,103 wild elephants</span>
    </div>
</div>
''',
    7: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">07</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Place Value Column Addition</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">Bundling Across Columns</span>
    </div>

    <!-- Column Grid 6,049 + 3,054 -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-3 font-mono text-center">
        <div class="grid grid-cols-5 gap-1 text-[11px] text-slate-400 border-b border-slate-800 pb-1 mb-1 font-semibold">
            <span></span><span>Thousands</span><span>Hundreds</span><span>Tens</span><span>Ones</span>
        </div>
        <div class="grid grid-cols-5 gap-1 text-xs text-amber-300/80 mb-1">
            <span>Carry:</span><span id="c7-th-carry">0</span><span id="c7-h-carry" class="text-cyan-400 font-bold">1</span><span id="c7-t-carry" class="text-emerald-400 font-bold">1</span><span>-</span>
        </div>
        <div class="grid grid-cols-5 gap-1 text-sm font-bold text-white">
            <span class="text-slate-400">Karnataka:</span><span>6</span><span>0</span><span>4</span><span>9</span>
        </div>
        <div class="grid grid-cols-5 gap-1 text-sm font-bold text-white border-b border-slate-700 pb-1">
            <span class="text-slate-400">+ Kerala:</span><span>3</span><span>0</span><span>5</span><span>4</span>
        </div>
        <div class="grid grid-cols-5 gap-1 text-base font-black text-emerald-400 pt-1">
            <span class="text-slate-400 text-xs">Total:</span><span>9</span><span>1</span><span>0</span><span>3</span>
        </div>
    </div>

    <!-- Carry Explanation -->
    <div class="bg-slate-950/50 border border-slate-800 rounded-xl p-3 text-xs text-slate-300 leading-relaxed space-y-1">
        <div><strong>Ones:</strong> 9 + 4 = 13 ones &rarr; write 3, bundle 1 ten into tens column.</div>
        <div><strong>Tens:</strong> 1 (carry) + 4 + 5 = 10 tens &rarr; write 0, bundle 1 hundred into hundreds column!</div>
    </div>
</div>
''',
    8: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">08</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Multi-State Tiger Population Adder</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">3-State Addition Board</span>
    </div>

    <!-- Three States Addition Board -->
    <div class="grid grid-cols-3 gap-2 text-center text-xs font-mono">
        <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800">
            <div class="text-slate-400">Maharashtra</div>
            <div class="text-xl font-bold text-orange-400 mt-1">444</div>
        </div>
        <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800">
            <div class="text-slate-400">Uttarakhand</div>
            <div class="text-xl font-bold text-cyan-400 mt-1">560</div>
        </div>
        <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800">
            <div class="text-slate-400">Madhya Pradesh</div>
            <div class="text-xl font-bold text-amber-400 mt-1">785</div>
        </div>
    </div>

    <!-- Step Calculation -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-3 font-mono text-center space-y-1.5 text-xs">
        <div class="text-slate-400">Subtotal (Maharashtra + Uttarakhand): 444 + 560 = <span class="font-bold text-white">1,004</span></div>
        <div class="text-slate-400">Final Sum (+ Madhya Pradesh): 1,004 + 785 = <span class="font-bold text-orange-400 text-sm">1,789 Tigers</span></div>
    </div>

    <div class="text-center text-xs text-slate-400">
        Three contiguous tiger habitats shelter a combined 1,789 majestic Bengal tigers.
    </div>
</div>
''',
    9: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-red-500/20 text-red-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Regrouping Subtraction & Unbundling</h3>
        </div>
        <span class="text-xs text-red-400 font-medium">Assam vs Meghalaya Elephants</span>
    </div>

    <!-- Regrouping Column Grid: 5,719 - 1,754 -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-3 font-mono text-center">
        <div class="grid grid-cols-5 gap-1 text-[11px] text-slate-400 border-b border-slate-800 pb-1 mb-1 font-semibold">
            <span></span><span>Thousands</span><span>Hundreds</span><span>Tens</span><span>Ones</span>
        </div>
        <div class="grid grid-cols-5 gap-1 text-xs text-cyan-300/80 mb-1">
            <span>Regroup:</span><span id="s9-th-regroup">4</span><span id="s9-h-regroup" class="text-amber-400 font-bold">16</span><span id="s9-t-regroup" class="text-emerald-400 font-bold">11</span><span>-</span>
        </div>
        <div class="grid grid-cols-5 gap-1 text-sm font-bold text-white">
            <span class="text-slate-400">Assam:</span><span>5</span><span>7</span><span>1</span><span>9</span>
        </div>
        <div class="grid grid-cols-5 gap-1 text-sm font-bold text-white border-b border-slate-700 pb-1">
            <span class="text-slate-400">- Meghalaya:</span><span>1</span><span>7</span><span>5</span><span>4</span>
        </div>
        <div class="grid grid-cols-5 gap-1 text-base font-black text-rose-400 pt-1">
            <span class="text-slate-400 text-xs">Difference:</span><span>3</span><span>9</span><span>6</span><span>5</span>
        </div>
    </div>

    <!-- Regrouping Steps -->
    <div class="bg-slate-950/50 border border-slate-800 rounded-xl p-3 text-xs text-slate-300 leading-relaxed space-y-1">
        <div><strong>Tens:</strong> Unbundle 1 hundred into 10 tens &rarr; 1 + 10 = 11 tens. 11 - 5 = 6 tens.</div>
        <div><strong>Hundreds:</strong> Unbundle 1 thousand into 10 hundreds &rarr; 6 + 10 = 16 hundreds. 16 - 7 = 9 hundreds.</div>
    </div>
</div>
''',
    10: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Kaziranga Park Attendance Records</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">9,115 - 8,426 = 689</span>
    </div>

    <!-- Attendance Cards -->
    <div class="grid grid-cols-2 gap-3 text-center font-mono">
        <div class="bg-slate-950/70 p-3 rounded-xl border border-slate-800">
            <div class="text-xs text-slate-400">Year 2022 Visitors</div>
            <div class="text-2xl font-black text-emerald-400 mt-1">9,115</div>
        </div>
        <div class="bg-slate-950/70 p-3 rounded-xl border border-slate-800">
            <div class="text-xs text-slate-400">Year 2021 Visitors</div>
            <div class="text-2xl font-black text-cyan-400 mt-1">8,426</div>
        </div>
    </div>

    <!-- Difference Calculation & Inverse Check -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-3 text-center space-y-2">
        <div class="text-xs text-slate-400 font-mono">Attendance Increase: 9,115 - 8,426 = <span class="text-amber-400 font-bold text-sm">689 Visitors</span></div>
        <div class="text-xs text-emerald-400 font-mono bg-emerald-950/40 border border-emerald-800/60 py-1 px-3 rounded-lg inline-block">
            Verification Check: 8,426 + 689 = 9,115 &check;
        </div>
    </div>
</div>
''',
    11: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-yellow-500/20 text-yellow-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Beverage Crates & Vehicle Deliveries</h3>
        </div>
        <span class="text-xs text-yellow-400 font-medium">Multi-Row Column Addition</span>
    </div>

    <!-- Multi-Add Column 3,450 + 2,870 + 1,680 -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-3 font-mono text-center">
        <div class="grid grid-cols-5 gap-1 text-[11px] text-slate-400 border-b border-slate-800 pb-1 mb-1 font-semibold">
            <span>Item</span><span>Th</span><span>H</span><span>T</span><span>O</span>
        </div>
        <div class="grid grid-cols-5 gap-1 text-xs text-yellow-400/90 mb-1">
            <span>Carry:</span><span class="font-bold">2</span><span class="font-bold">2</span><span>-</span><span>-</span>
        </div>
        <div class="grid grid-cols-5 gap-1 text-xs text-slate-200">
            <span class="text-slate-400">Mango:</span><span>3</span><span>4</span><span>5</span><span>0</span>
        </div>
        <div class="grid grid-cols-5 gap-1 text-xs text-slate-200">
            <span class="text-slate-400">Apple:</span><span>2</span><span>8</span><span>7</span><span>0</span>
        </div>
        <div class="grid grid-cols-5 gap-1 text-xs text-slate-200 border-b border-slate-700 pb-1">
            <span class="text-slate-400">Orange:</span><span>1</span><span>6</span><span>8</span><span>0</span>
        </div>
        <div class="grid grid-cols-5 gap-1 text-base font-black text-yellow-400 pt-1">
            <span class="text-slate-400 text-xs">Total:</span><span>8</span><span>0</span><span>0</span><span>0</span>
        </div>
    </div>

    <div class="text-center text-xs text-slate-300">
        Tens: 5 + 7 + 8 = 20 &rarr; carry 2. Hundreds: 2 + 4 + 8 + 6 = 20 &rarr; carry 2. Total = 8,000 crates!
    </div>
</div>
''',
    12: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-green-500/20 text-green-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Baal Mela Bank Deposit Slip</h3>
        </div>
        <span class="text-xs text-green-400 font-medium">Currency Denominations</span>
    </div>

    <!-- Presets -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <span class="text-slate-400 mr-1 text-[11px]">Select Deposit:</span>
        <button onclick="setDepositPreset(2850)" class="dep-btn px-2.5 py-1 rounded-lg bg-green-600 text-white font-bold">₹2,850</button>
        <button onclick="setDepositPreset(1420)" class="dep-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">₹1,420</button>
        <button onclick="setDepositPreset(3650)" class="dep-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">₹3,650</button>
    </div>

    <!-- Interactive Deposit Slip Table -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-3 font-mono text-xs">
        <div class="grid grid-cols-4 gap-2 text-slate-400 border-b border-slate-800 pb-1 mb-2 font-semibold text-center">
            <span>Denomination</span><span>Count</span><span>Calculation</span><span>Amount</span>
        </div>
        <div class="space-y-1.5 text-center">
            <div class="grid grid-cols-4 gap-2 items-center">
                <span class="text-amber-400 font-bold">₹500</span>
                <span id="dep-c500" class="text-white">5</span>
                <span id="dep-calc500" class="text-slate-400">5 × 500</span>
                <span id="dep-amt500" class="text-white">₹2,500</span>
            </div>
            <div class="grid grid-cols-4 gap-2 items-center">
                <span class="text-cyan-400 font-bold">₹100</span>
                <span id="dep-c100" class="text-white">3</span>
                <span id="dep-calc100" class="text-slate-400">3 × 100</span>
                <span id="dep-amt100" class="text-white">₹300</span>
            </div>
            <div class="grid grid-cols-4 gap-2 items-center">
                <span class="text-emerald-400 font-bold">₹50</span>
                <span id="dep-c50" class="text-white">1</span>
                <span id="dep-calc50" class="text-slate-400">1 × 50</span>
                <span id="dep-amt50" class="text-white">₹50</span>
            </div>
            <div class="grid grid-cols-4 gap-2 items-center">
                <span class="text-purple-400 font-bold">₹10</span>
                <span id="dep-c10" class="text-white">0</span>
                <span id="dep-calc10" class="text-slate-400">0 × 10</span>
                <span id="dep-amt10" class="text-white">₹0</span>
            </div>
        </div>
        <div class="border-t border-slate-700 mt-2 pt-2 grid grid-cols-4 gap-2 font-bold text-center">
            <span class="col-span-3 text-right text-slate-300">Total Deposit:</span>
            <span id="dep-grand-total" class="text-green-400 text-sm">₹2,850</span>
        </div>
    </div>
</div>
''',
    13: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Four-Digit Column Algorithms</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Standard Arithmetic Practice</span>
    </div>

    <!-- Mode Selector -->
    <div class="flex justify-center gap-2 text-xs">
        <button onclick="setColMode('add')" id="col-mode-add" class="col-btn px-3 py-1.5 rounded-xl bg-indigo-600 text-white font-bold">Addition (4,786 + 3,847)</button>
        <button onclick="setColMode('sub')" id="col-mode-sub" class="col-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300">Subtraction (7,215 - 3,648)</button>
    </div>

    <!-- Display Board -->
    <div id="col-board" class="bg-slate-950/70 border border-slate-800 rounded-xl p-3 font-mono text-center">
        <!-- Rendered dynamically via JS -->
    </div>
</div>
''',
    14: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Mental Math Compensation Shortcuts</h3>
        </div>
        <span class="text-xs text-pink-400 font-medium">Friendly Landmark Numbers</span>
    </div>

    <!-- Preset Selector -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <button onclick="setCompensation(546, -99)" class="comp-btn px-2.5 py-1 rounded-lg bg-pink-600 text-white font-bold">546 - 99</button>
        <button onclick="setCompensation(372, 99)" class="comp-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">372 + 99</button>
        <button onclick="setCompensation(2740, -999)" class="comp-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">2,740 - 999</button>
    </div>

    <!-- Step Breakdown Visualizer -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-4 text-center space-y-3 font-mono">
        <div class="flex items-center justify-center gap-2 text-sm sm:text-base">
            <span class="text-slate-400">Step 1 (Landmark):</span>
            <span id="comp-step1" class="text-cyan-400 font-bold">546 - 100 = 446</span>
        </div>
        <div class="flex items-center justify-center gap-2 text-sm sm:text-base">
            <span class="text-slate-400">Step 2 (Adjust):</span>
            <span id="comp-step2" class="text-amber-400 font-bold">446 + 1 = 447</span>
        </div>
        <div id="comp-summary" class="text-xs text-pink-300 bg-pink-950/40 border border-pink-800/60 py-1.5 px-3 rounded-lg inline-block">
            546 - 99 = 447 (Computed in under 2 seconds!)
        </div>
    </div>
</div>
''',
    15: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-sky-500/20 text-sky-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Inequality Relational Logic Comparator</h3>
        </div>
        <span class="text-xs text-sky-400 font-medium">Compare Without Adding</span>
    </div>

    <!-- Expression Selector -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <button onclick="setInequality(1)" class="ineq-btn px-2.5 py-1 rounded-lg bg-sky-600 text-white font-bold">Case 1 (Addition)</button>
        <button onclick="setInequality(2)" class="ineq-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Case 2 (Subtraction)</button>
        <button onclick="setInequality(3)" class="ineq-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Case 3 (Balance Transfer)</button>
    </div>

    <!-- Comparison Display -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-4 text-center space-y-3 font-mono">
        <div class="flex items-center justify-center gap-3 text-lg sm:text-xl font-bold">
            <span id="ineq-left" class="text-cyan-400">2,450 + 320</span>
            <span id="ineq-symbol" class="text-2xl text-amber-400 px-2.5 py-0.5 rounded-lg bg-slate-800">&gt;</span>
            <span id="ineq-right" class="text-rose-400">2,450 + 310</span>
        </div>
        <div id="ineq-reason" class="text-xs text-slate-300 leading-relaxed text-center px-2">
            Both expressions contain common term 2,450. Since 320 &gt; 310, the left expression is strictly greater!
        </div>
    </div>
</div>
''',
    16: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Neighbouring Square Grid Parity Puzzle</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">No Adjacent Evens</span>
    </div>

    <!-- Instructions & Status -->
    <div class="text-xs text-slate-300 text-center">
        Arrange numbers 1 to 9 so no two <span class="text-cyan-400 font-bold">even numbers (2,4,6,8)</span> share an edge!
    </div>

    <!-- 3x3 Parity Grid -->
    <div class="flex justify-center">
        <div id="parity-grid" class="grid grid-cols-3 gap-2 w-56 text-center font-mono">
            <!-- Rendered dynamically via JS -->
        </div>
    </div>

    <!-- Controls -->
    <div class="flex items-center justify-center gap-3">
        <button onclick="revealParityPattern()" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow transition">Show Solution Pattern</button>
        <button onclick="resetParityGrid()" class="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition">Reset</button>
    </div>
</div>
''',
}
