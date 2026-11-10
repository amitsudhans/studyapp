#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 3: Pair of Linear Equations in Two Variables
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Substitution Cost Problems
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏏</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Substitution Word Problems: Coincident Bills, Sports &amp; Fractions</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">3 Applications</span>
    </div>

    <p class="text-xs text-slate-300">Click each real-world scenario solved by Substitution—including the subtle 18 = 18 identity trap!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="inspectSubApp('pen')" id="btn-sa-pen" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">Pencils (18=18)</button>
        <button onclick="inspectSubApp('bat')" id="btn-sa-bat" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Cricket Bats &amp; Balls</button>
        <button onclick="inspectSubApp('frac')" id="btn-sa-frac" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Fraction +2 / +3</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="sa-eq">2x + 3y = 9  ⟹  x = (9 − 3y)/2   |   Plug in 4x + 6y = 18: 2(9 − 3y) + 6y = 18</div>
        <div class="text-amber-300 font-bold" id="sa-res">Result: 18 − 6y + 6y = 18  ⟹  18 = 18 (True Identity -> Infinitely Many Solutions!)</div>
    </div>
</div>

<script>
function inspectSubApp(k) {
    const map = {
        pen: { e: '2x + 3y = 9  ⟹  x = (9 − 3y)/2   |   Plug in 4x + 6y = 18: 2(9 − 3y) + 6y = 18', r: 'Result: 18 − 6y + 6y = 18  ⟹  18 = 18 (True Identity -> Infinitely Many Solutions!)' },
        bat: { e: '7x + 6y = 3800  &  3x + 5y = 1750  ⟹  y = (1750 − 3x)/5', r: 'Solving yields Bat x = ₹500 and Ball y = ₹50 (check: 3500 + 300 = 3800 ✅)!' },
        frac: { e: '11x − 9y = −4  &  6x − 5y = −3  ⟹  x = (9y − 4)/11', r: 'Solving cleanly yields x = 7, y = 9 -> Fraction = 7/9 (check: 9/11 and 10/12 = 5/6 ✅)!' }
    };
    const d = map[k];
    if (!d) return;
    ['pen', 'bat', 'frac'].forEach(x => {
        const b = document.getElementById('btn-sa-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('sa-eq').textContent = d.e;
    document.getElementById('sa-res').textContent = d.r;
}
</script>
"""

# Simulator 10: Substitution Age Problems
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⏳</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Age Time-Shift Interactive Timeline (Past, Present, Future)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">Ex 3.2 Age Puzzle</span>
    </div>

    <p class="text-xs text-slate-300">Shift along the timeline to watch Parent (40 yrs) &amp; Child (10 yrs) satisfy BOTH the 5-years-ago (7×) and 5-years-hence (3×) clues!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="setAgeTimeline('past')" id="btn-ag-past" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">⏪ 5 Years Ago</button>
        <button onclick="setAgeTimeline('now')" id="btn-ag-now" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">📍 Present Today</button>
        <button onclick="setAgeTimeline('fut')" id="btn-ag-fut" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">⏩ 5 Years Hence</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="font-mono text-amber-300 font-bold text-sm" id="ag-ages">Present: Elder Parent = 40 yrs   |   Child = 10 yrs</div>
        <div class="font-mono text-cyan-300" id="ag-eq">Algebraic Pair: x − 3y = 10  &amp;  x − 7y = −30</div>
        <p class="text-slate-300" id="ag-check">Remember: Moving +5 or −5 years ALWAYS shifts BOTH people's ages equally by 5 years!</p>
    </div>
</div>

<script>
function setAgeTimeline(t) {
    const map = {
        past: { a: '5 Years Ago: Parent = 35 yrs (40−5)   |   Child = 5 yrs (10−5)', e: 'Ratio Check: 35 = 7 × 5  ⟹  (x − 5) = 7(y − 5) ✅', c: 'Five years earlier, parent age (35) was exactly SEVEN times child age (5)!' },
        now: { a: 'Present: Elder Parent = 40 yrs   |   Child = 10 yrs', e: 'Algebraic Pair: x − 3y = 10  &  x − 7y = −30', c: 'Remember: Moving +5 or −5 years ALWAYS shifts BOTH ages equally by 5 years!' },
        fut: { a: '5 Years Hence: Parent = 45 yrs (40+5)   |   Child = 15 yrs (10+5)', e: 'Ratio Check: 45 = 3 × 15  ⟹  (x + 5) = 3(y + 5) ✅', c: 'Five years into the future, parent age (45) equals exactly THREE times child age (15)!' }
    };
    const d = map[t];
    if (!d) return;
    ['past', 'now', 'fut'].forEach(k => {
        const b = document.getElementById('btn-ag-' + k);
        if (b) {
            b.className = (k === t)
                ? 'p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('ag-ages').textContent = d.a;
    document.getElementById('ag-eq').textContent = d.e;
    document.getElementById('ag-check').textContent = d.c;
}
</script>
"""

# Simulator 11: Elimination Method Steps
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚡</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Elimination Scaling &amp; Variable-Canceling Machine</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Scale &amp; Cancel</span>
    </div>

    <p class="text-xs text-slate-300">Inspect opposite-sign Addition (OA) vs same-sign Subtraction (SS) to knock out one variable immediately!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="runElimEx('e1')" id="btn-el-e1" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">x+y=5 &amp; 2x−3y=4 (Add)</button>
        <button onclick="runElimEx('e2')" id="btn-el-e2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2x+3y=11 &amp; 2x−4y=−24 (Sub)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs">
        <div class="text-amber-300 font-bold" id="el-scale">Scale Eq 1 by ×3:  3x + 3y = 15   &amp;   Eq 2: 2x − 3y = 4</div>
        <div class="text-cyan-300" id="el-op">Opposite signs (+3y, −3y) -> ADD vertically: (3x + 2x) = 15 + 4  ⟹  5x = 19</div>
        <div class="text-emerald-300 font-bold" id="el-ans">✅ Solution: x = 19/5, and y = 5 − 19/5 = 6/5!</div>
    </div>
</div>

<script>
function runElimEx(k) {
    const map = {
        e1: { sc: 'Scale Eq 1 by ×3:  3x + 3y = 15   &   Eq 2: 2x − 3y = 4', op: 'Opposite signs (+3y, −3y) -> ADD vertically: (3x + 2x) = 15 + 4  ⟹  5x = 19', ans: '✅ Solution: x = 19/5, and y = 5 − 19/5 = 6/5!' },
        e2: { sc: 'Already Matched x (+2x and +2x):  2x + 3y = 11   &   2x − 4y = −24', op: 'Same signs (+2x, +2x) -> SUBTRACT Eq 2 from Eq 1: 3y − (−4y) = 11 − (−24)  ⟹  7y = 35', ans: '✅ Solution: y = 5, and 2x = 11 − 15 = −4 -> x = −2!' }
    };
    const d = map[k];
    if (!d) return;
    ['e1', 'e2'].forEach(x => {
        const b = document.getElementById('btn-el-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('el-scale').textContent = d.sc;
    document.getElementById('el-op').textContent = d.op;
    document.getElementById('el-ans').textContent = d.ans;
}
</script>
"""

# Simulator 12: Elimination Edge Cases
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚠️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Zero-Variable Edge Case Decoder (0 = 0 vs. 0 = k)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Diagnostic</span>
    </div>

    <p class="text-xs text-slate-300">Compare both surprising algebraic endings whenever scaling causes BOTH x and y to vanish at once!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="inspectEdge('true0')" id="btn-ed-true0" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">Leaves True 0 = 0</button>
        <button onclick="inspectEdge('falsek')" id="btn-ed-falsek" class="p-2.5 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-rose-700 hover:bg-slate-800">Leaves False 0 = −4</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 text-xs font-mono">
        <div class="text-cyan-300" id="ed-eq">System: (2x + 3y = 9) × 2  −  (4x + 6y = 18)  ⟹  0 = 0</div>
        <div class="font-sans text-emerald-300 font-bold" id="ed-ver">✅ ALWAYS TRUE -> Coincident Overlapping Lines -> Infinitely Many Solutions!</div>
    </div>
</div>

<script>
function inspectEdge(k) {
    const map = {
        true0: { e: 'System: (2x + 3y = 9) × 2  −  (4x + 6y = 18)  ⟹  0 = 0', v: '✅ ALWAYS TRUE -> Coincident Overlapping Lines -> Infinitely Many Solutions!', ok: true },
        falsek: { e: 'System: (x + 2y = 4) × 2  −  (2x + 4y = 12)  ⟹  0 = −4', v: '❌ ALWAYS FALSE -> Separated Parallel Lines -> Inconsistent (NO Solution)!', ok: false }
    };
    const d = map[k];
    if (!d) return;
    document.getElementById('btn-ed-true0').className = (k === 'true0') ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500' : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
    document.getElementById('btn-ed-falsek').className = (k === 'falsek') ? 'p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500' : 'p-2.5 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-rose-700 hover:bg-slate-800';
    document.getElementById('ed-eq').textContent = d.e;
    const vv = document.getElementById('ed-ver');
    vv.textContent = d.v;
    vv.className = d.ok ? 'font-sans text-emerald-300 font-bold' : 'font-sans text-rose-300 font-bold';
}
</script>
"""

# Simulator 13: Income Ratio Problems
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">💰</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Monthly Income (9:7) &amp; Expense (4:3) Balance Solver</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Textbook Ex 8</span>
    </div>

    <p class="text-xs text-slate-300">Walk step by step through Textbook Example 8 solving monthly incomes when savings equal ₹2,000 each!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="stepIncome(1)" id="btn-inc-1" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">1. Dual Ratios</button>
        <button onclick="stepIncome(2)" id="btn-inc-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. Eliminate y</button>
        <button onclick="stepIncome(3)" id="btn-inc-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. Verify Budget</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs">
        <div class="text-amber-300 font-bold" id="inc-math">Incomes: 9x &amp; 7x   |   Expenses: 4y &amp; 3y   ⟹   9x − 4y = 2000 &amp; 7x − 3y = 2000</div>
        <p class="font-sans text-slate-300" id="inc-note">Always assign TWO separate ratio multipliers (x for incomes, y for expenses) since income and spending scales differ!</p>
    </div>
</div>

<script>
function stepIncome(n) {
    const map = {
        1: { m: 'Incomes: 9x & 7x   |   Expenses: 4y & 3y   ⟹   9x − 4y = 2000 & 7x − 3y = 2000', n: 'Always assign TWO separate ratio multipliers (x for incomes, y for expenses) since income and spending scales differ!' },
        2: { m: '×3 Eq1: 27x − 12y = 6000   |   ×4 Eq2: 28x − 12y = 8000   ⟹   Subtract: x = 2,000!', n: 'Scaling y to matched 12y and subtracting eliminates y immediately, revealing x = 2,000!' },
        3: { m: 'Incomes: 9(2000) = ₹18,000 & 7(2000) = ₹14,000 ✅  |  Expenses: ₹16,000 & ₹12,000 (4:3)', n: 'Check savings cleanly: 18,000 − 16,000 = ₹2,000 and 14,000 − 12,000 = ₹2,000!' }
    };
    const d = map[n];
    if (!d) return;
    [1, 2, 3].forEach(k => {
        const b = document.getElementById('btn-inc-' + k);
        if (b) {
            b.className = (k === n)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('inc-math').textContent = d.m;
    document.getElementById('inc-note').textContent = d.n;
}
</script>
"""

# Simulator 14: Digit Reversal Puzzles
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔄</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Two-Digit Place-Value Reverser (Ex 10: 42 &amp; 24)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Two Valid Numbers</span>
    </div>

    <p class="text-xs text-slate-300">Explore both cases of |x − y| = 2 when (10x + y) + (10y + x) = 66, yielding TWO valid 2-digit numbers!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="showDigitCase('gt')" id="btn-dg-gt" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Case A: x − y = 2 (Tens &gt; Units)</button>
        <button onclick="showDigitCase('lt')" id="btn-dg-lt" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Case B: y − x = 2 (Units &gt; Tens)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs">
        <div class="text-cyan-300" id="dg-eqs">x + y = 6   &amp;   x − y = 2   ⟹   Add: 2x = 8 -> x = 4, y = 2</div>
        <div class="text-emerald-300 font-bold" id="dg-num">Number = 10(4) + 2 = 42  (Check: 42 + 24 = 66, |4−2| = 2 ✅)</div>
    </div>
</div>

<script>
function showDigitCase(k) {
    const map = {
        gt: { e: 'x + y = 6   &   x − y = 2   ⟹   Add: 2x = 8 -> x = 4, y = 2', n: 'Number = 10(4) + 2 = 42  (Check: 42 + 24 = 66, |4−2| = 2 ✅)' },
        lt: { e: 'x + y = 6   &   y − x = 2   ⟹   Add: 2y = 8 -> y = 4, x = 2', n: 'Number = 10(2) + 4 = 24  (Check: 24 + 42 = 66, |2−4| = 2 ✅)' }
    };
    const d = map[k];
    if (!d) return;
    ['gt', 'lt'].forEach(x => {
        const b = document.getElementById('btn-dg-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('dg-eqs').textContent = d.e;
    document.getElementById('dg-num').textContent = d.n;
}
</script>
"""

# Simulator 15: Comparing Solution Methods
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧭</span>
            <h3 class="text-sm sm:text-base font-bold text-sky-300">Strategic Method Selector: Graph vs. Substitution vs. Elimination</h3>
        </div>
        <span class="text-[11px] bg-sky-950/80 text-sky-300 px-2.5 py-1 rounded-full border border-sky-800">Strategy Guide</span>
    </div>

    <p class="text-xs text-slate-300">Click any method below to review when it shines brightest and watch out for messy-fraction traps!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickStrat('g')" id="btn-st-g" class="p-2 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500">Graphical Method</button>
        <button onclick="pickStrat('s')" id="btn-st-s" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Substitution Method</button>
        <button onclick="pickStrat('e')" id="btn-st-e" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Elimination Method</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 text-xs">
        <h4 class="font-bold text-sky-300 text-sm" id="st-title">Best For: Visualizing Line Behaviour &amp; Clean Integer Grid Crossings</h4>
        <p class="text-slate-300 leading-relaxed" id="st-desc">Ideal for geometric area triangles (Ex 3.1 Q7) or checking intersections visually—yet imprecise when coordinates are non-integer fractions like (49/29, 19/29).</p>
    </div>
</div>

<script>
function pickStrat(k) {
    const map = {
        g: { t: 'Best For: Visualizing Line Behaviour & Clean Integer Grid Crossings', d: 'Ideal for geometric area triangles (Ex 3.1 Q7) or checking intersections visually—yet imprecise when coordinates are non-integer fractions like (49/29, 19/29).' },
        s: { t: 'Best For: Lonely Variable With Coefficient ±1 (e.g., x + 2y = 3)', d: 'When one equation isolates x or y cleanly without creating denominators, Substitution solves smoothly with zero scaling setup!' },
        e: { t: 'Best For: Large / Symmetric / Ratio Coefficients (e.g., 9x − 4y = 2000)', d: 'Elimination avoids messy fractions altogether—scaling equations once and adding/subtracting eliminates one variable swiftly!' }
    };
    const d = map[k];
    if (!d) return;
    ['g', 's', 'e'].forEach(x => {
        const b = document.getElementById('btn-st-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('st-title').textContent = d.t;
    document.getElementById('st-desc').textContent = d.d;
}
</script>
"""

# Simulator 16: Chapter Three Summary
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎓</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Chapter 3 Master Formula &amp; Consistency Cheat Sheet</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Revision Hub</span>
    </div>

    <p class="text-xs text-slate-300">Select each core pillar of Chapter 3 to verify definitions and edge rules right before launching Exercise 3.1 &amp; 3.2 quizzes!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectCh3Sum('std')" id="btn-c3s-std" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Standard Pair</button>
        <button onclick="inspectCh3Sum('tab')" id="btn-c3s-tab" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Table 3.1 Ratios</button>
        <button onclick="inspectCh3Sum('alg')" id="btn-c3s-alg" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Algebraic Rules</button>
        <button onclick="inspectCh3Sum('word')" id="btn-c3s-word" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Word Traps</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 text-xs">
        <h4 class="font-bold text-cyan-300 text-sm" id="c3s-title">1. General Simultaneous Linear Pair</h4>
        <p class="text-slate-300 leading-relaxed" id="c3s-desc">a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0 where a₁²+b₁² ≠ 0 and a₂²+b₂² ≠ 0. Always move all constants onto the same side before comparing ratios!</p>
    </div>
</div>

<script>
function inspectCh3Sum(k) {
    const map = {
        std: { t: '1. General Simultaneous Linear Pair', d: 'a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0 where a₁²+b₁² ≠ 0 and a₂²+b₂² ≠ 0. Always move all constants onto the same side before comparing ratios!' },
        tab: { t: '2. Table 3.1 Graphical & Consistency Map', d: 'a₁/a₂ ≠ b₁/b₂ -> Intersecting (1 sol, Consistent). All 3 equal -> Coincident (∞ sol, Dependent). Slopes equal ≠ c₁/c₂ -> Parallel (0 sol, Inconsistent).' },
        alg: { t: '3. Substitution & Elimination Signals', d: 'Both give exact fractional answers. If all variables vanish leaving true 0 = 0 -> ∞ solutions; if false 0 = k (k ≠ 0) -> no solution.' },
        word: { t: '4. Common Word-Problem Traps', d: 'Two-digit number = 10x + y (reversed 10y + x); half-perimeter = x + y; age shifts add/subtract equally for both people; fixed+daily fee separates base days.' }
    };
    const d = map[k];
    if (!d) return;
    ['std', 'tab', 'alg', 'word'].forEach(x => {
        const b = document.getElementById('btn-c3s-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('c3s-title').textContent = d.t;
    document.getElementById('c3s-desc').textContent = d.d;
}
</script>
"""
