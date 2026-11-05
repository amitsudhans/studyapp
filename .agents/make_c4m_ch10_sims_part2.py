# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 10: Elephants, Tigers, and Leopards
Part 2 Simulators: Slides 9 to 16
Bespoke SVG/HTML interactive simulators.
Zero human names (replaced with generic roles).
Clean Unicode throughout.
"""

sim9 = """
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
"""

sim10 = """
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
"""

sim11 = """
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
"""

sim12 = """
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
"""

sim13 = """
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
"""

sim14 = """
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
"""

sim15 = """
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
"""

sim16 = """
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
