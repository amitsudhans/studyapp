#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 3: Pair of Linear Equations in Two Variables
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Fair Equation Modeling
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎡</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Carnival Fair Equation Modeler (Giant Wheel &amp; Hoopla)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Word-to-Algebra</span>
    </div>

    <p class="text-xs text-slate-300">Test candidate numbers of Giant Wheel rides (x, ₹3) and Hoopla games (y, ₹4) to discover which pair satisfies BOTH carnival fair rules!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="testFairPair(2, 1)" id="btn-fr-21" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">x=2 rides, y=1</button>
        <button onclick="testFairPair(4, 2)" id="btn-fr-42" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">x=4 rides, y=2</button>
        <button onclick="testFairPair(4, 3)" id="btn-fr-43" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">x=4 rides, y=3</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 font-mono text-xs">
        <div class="text-cyan-300" id="fr-eq1">Rule 1 (y = ½x  ⟹  x − 2y = 0):  4 − 2(2) = 0 ✅ Match!</div>
        <div class="text-amber-300" id="fr-eq2">Rule 2 (₹3x + ₹4y = ₹20):  3(4) + 4(2) = 12 + 8 = ₹20 ✅ Match!</div>
        <div class="font-sans text-emerald-400 font-bold pt-1" id="fr-ver">Both equations satisfied cleanly! Solution: 4 Giant Wheel rides and 2 Hoopla rounds!</div>
    </div>
</div>

<script>
function testFairPair(x, y) {
    const r1 = (x - 2 * y === 0);
    const cost = 3 * x + 4 * y;
    const r2 = (cost === 20);
    const keys = { '21': [2,1], '42': [4,2], '43': [4,3] };
    Object.keys(keys).forEach(k => {
        const b = document.getElementById('btn-fr-' + k);
        const [kx, ky] = keys[k];
        if (b) {
            b.className = (kx === x && ky === y)
                ? 'p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('fr-eq1').textContent = `Rule 1 (y = ½x ⟹ x − 2y = 0): ${x} − 2(${y}) = ${x - 2*y} ${r1 ? '✅ Match!' : '❌ Not 0'}`;
    document.getElementById('fr-eq2').textContent = `Rule 2 (₹3x + ₹4y = ₹20): 3(${x}) + 4(${y}) = ₹${cost} ${r2 ? '✅ Match!' : '❌ Not ₹20'}`;
    const v = document.getElementById('fr-ver');
    if (r1 && r2) {
        v.className = 'font-sans text-emerald-400 font-bold pt-1';
        v.textContent = 'Both equations satisfied cleanly! Solution: 4 Giant Wheel rides and 2 Hoopla rounds!';
    } else {
        v.className = 'font-sans text-rose-300 font-bold pt-1';
        v.textContent = 'Fails at least one condition! A simultaneous solution must make BOTH equations true together.';
    }
}
</script>
"""

# Simulator 2: Intersecting Unique Solution
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✖️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Graphical Case 1: Intersecting Lines &amp; Unique Solution</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Consistent Pair</span>
    </div>

    <p class="text-xs text-slate-300">Switch between Textbook Fair Rides and Ex 3.1 lines to see intersecting graphs lock onto ONE unique crossing point!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="showCase1Graph('fair')" id="btn-g1-fair" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">Fair: (4, 2)</button>
        <button onclick="showCase1Graph('axis')" id="btn-g1-axis" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">x+3y=6 &amp; 2x−3y=12</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 170" class="w-full h-auto max-h-[170px] rounded-xl bg-slate-950 border border-slate-800">
            <line x1="20" y1="140" x2="205" y2="140" stroke="#64748b" stroke-width="1.5" />
            <line x1="40" y1="15" x2="40" y2="155" stroke="#64748b" stroke-width="1.5" />
            <g id="g1-fair-svg">
                <line x1="40" y1="140" x2="180" y2="70" stroke="#38bdf8" stroke-width="2.5" />
                <line x1="40" y1="40" x2="173" y2="140" stroke="#f97316" stroke-width="2.5" />
                <circle cx="120" cy="100" r="5" fill="#fde047" />
                <text x="128" y="96" fill="#fde047" font-size="10" font-weight="bold">(4, 2)</text>
            </g>
            <g id="g1-axis-svg" class="hidden">
                <line x1="40" y1="100" x2="195" y2="152" stroke="#38bdf8" stroke-width="2.5" />
                <line x1="90" y1="165" x2="195" y2="95" stroke="#22c55e" stroke-width="2.5" />
                <circle cx="160" cy="140" r="5" fill="#fde047" />
                <text x="155" y="128" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">(6, 0)</text>
            </g>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-emerald-300 text-sm" id="g1-title">Crossing Point (4, 2) — Unique Solution</h4>
            <p class="text-slate-300 leading-relaxed" id="g1-desc">Lines x − 2y = 0 and 3x + 4y = 20 slice cleanly across one another at exactly ONE common coordinate (4, 2)—defining an independent CONSISTENT pair!</p>
        </div>
    </div>
</div>

<script>
function showCase1Graph(k) {
    document.getElementById('g1-fair-svg').classList.toggle('hidden', k !== 'fair');
    document.getElementById('g1-axis-svg').classList.toggle('hidden', k !== 'axis');
    ['fair', 'axis'].forEach(x => {
        const b = document.getElementById('btn-g1-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('g1-title').textContent = (k === 'fair') ? 'Crossing Point (4, 2) — Unique Solution' : 'Crossing Point (6, 0) on x-Axis — Unique Solution';
    document.getElementById('g1-desc').textContent = (k === 'fair')
        ? 'Lines x − 2y = 0 and 3x + 4y = 20 slice cleanly across one another at exactly ONE common coordinate (4, 2)—defining an independent CONSISTENT pair!'
        : 'Textbook lines x + 3y = 6 and 2x − 3y = 12 meet right on the horizontal x-axis at (6, 0)! Check: 6+0 = 6 and 12−0 = 12!';
}
</script>
"""

# Simulator 3: Parallel No Solution
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🛤️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Graphical Case 2: Parallel Railway Track Simulator (No Solution)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Inconsistent Pair</span>
    </div>

    <p class="text-xs text-slate-300">Inspect Textbook Rails x + 2y = 4 and 2x + 4y = 12: matching slope keeps both straight rails apart forever!</p>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 165" class="w-full h-auto max-h-[165px] rounded-xl bg-slate-950 border border-slate-800">
            <line x1="20" y1="135" x2="205" y2="135" stroke="#64748b" stroke-width="1.5" />
            <line x1="40" y1="15" x2="40" y2="150" stroke="#64748b" stroke-width="1.5" />
            <line x1="40" y1="95" x2="120" y2="135" stroke="#38bdf8" stroke-width="3" />
            <line x1="40" y1="75" x2="160" y2="135" stroke="#ef4444" stroke-width="3" />
            <text x="135" y="72" fill="#f87171" font-size="9" font-weight="bold">PARALLEL RAILS</text>
            <text x="135" y="84" fill="#cbd5e1" font-size="8">NEVER MEET (0 SOL)</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <div class="font-mono text-cyan-300 font-bold">Track 1: x + 2y = 4</div>
            <div class="font-mono text-rose-300 font-bold">Track 2: 2x + 4y = 12  ⟹  x + 2y = 6</div>
            <p class="text-slate-300 leading-relaxed">Since (x + 2y) cannot equal 4 and 6 simultaneously, zero coordinate pairs satisfy both rails—making the pair strictly INCONSISTENT!</p>
        </div>
    </div>
</div>
"""

# Simulator 4: Coincident Infinite Solutions
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">♾️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Graphical Case 3: Overlapping Coincident Lines</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Dependent (∞ Solutions)</span>
    </div>

    <p class="text-xs text-slate-300">Toggle Line 2 over Line 1 (2x + 3y = 9 and 4x + 6y = 18) to witness complete overlapping coincidence!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="toggleCoin(1)" id="btn-cn-1" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Show Line 1: 2x+3y=9</button>
        <button onclick="toggleCoin(2)" id="btn-cn-2" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-amber-700 hover:bg-slate-800">Overlay Line 2: 4x+6y=18</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 165" class="w-full h-auto max-h-[165px] rounded-xl bg-slate-950 border border-slate-800">
            <line x1="20" y1="135" x2="205" y2="135" stroke="#64748b" stroke-width="1.5" />
            <line x1="40" y1="15" x2="40" y2="150" stroke="#64748b" stroke-width="1.5" />
            <line x1="40" y1="65" x2="145" y2="135" stroke="#38bdf8" stroke-width="6" />
            <line id="cn-line2" x1="40" y1="65" x2="145" y2="135" stroke="#fde047" stroke-width="2.5" stroke-dasharray="6,4" class="hidden" />
            <circle cx="40" cy="65" r="4" fill="#fff" /><circle cx="110" cy="111.7" r="4" fill="#fff" /><circle cx="145" cy="135" r="4" fill="#fff" />
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-cyan-300 text-sm" id="cn-title">Line 1: 2x + 3y = 9</h4>
            <p class="text-slate-300 leading-relaxed" id="cn-desc">Passes cleanly through (0, 3), (3, 1), and (4.5, 0). Click 'Overlay Line 2' to watch 4x + 6y = 18 land directly on top!</p>
        </div>
    </div>
</div>

<script>
function toggleCoin(n) {
    document.getElementById('cn-line2').classList.toggle('hidden', n === 1);
    document.getElementById('btn-cn-1').className = (n === 1) ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500' : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
    document.getElementById('btn-cn-2').className = (n === 2) ? 'p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500' : 'p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-amber-700 hover:bg-slate-800';
    document.getElementById('cn-title').textContent = (n === 1) ? 'Line 1: 2x + 3y = 9' : 'COINCIDENT! 4x + 6y = 18 Lies Identically on Line 1!';
    document.getElementById('cn-desc').textContent = (n === 1)
        ? 'Passes cleanly through (0, 3), (3, 1), and (4.5, 0). Click Overlay Line 2 to watch 4x + 6y = 18 land directly on top!'
        : 'Because 4x + 6y = 18 is simply 2 × (2x + 3y = 9), EVERY single point on the dashed gold line matches the blue line—giving INFINITELY MANY solutions (Dependent Consistent)!';
}
</script>
"""

# Simulator 5: Coefficient Ratio Table
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📊</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Table 3.1 Ratio Comparison Interactive Radar</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">a₁/a₂, b₁/b₂, c₁/c₂</span>
    </div>

    <p class="text-xs text-slate-300">Inspect all three rows of NCERT Table 3.1 to predict lines, solution count, and consistency without drawing any graph!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="inspectTab31('int')" id="btn-t31-int" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">a₁/a₂ ≠ b₁/b₂</button>
        <button onclick="inspectTab31('coi')" id="btn-t31-coi" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">All 3 Equal</button>
        <button onclick="inspectTab31('par')" id="btn-t31-par" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">a₁/a₂ = b₁/b₂ ≠ c₁/c₂</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="grid grid-cols-3 gap-2 text-center">
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800"><span class="text-slate-400 block text-[10px]">Geometry</span><span class="font-bold text-cyan-300" id="t31-geo">Intersecting Lines</span></div>
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800"><span class="text-slate-400 block text-[10px]">Solutions</span><span class="font-bold text-amber-300" id="t31-sol">Exactly 1 (Unique)</span></div>
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800"><span class="text-slate-400 block text-[10px]">Consistency</span><span class="font-bold text-emerald-300" id="t31-con">Consistent</span></div>
        </div>
        <div class="font-mono text-slate-300 pt-1" id="t31-ex">Example: x − 2y = 0 and 3x + 4y − 20 = 0 -> Ratios: 1/3 ≠ −2/4</div>
    </div>
</div>

<script>
function inspectTab31(k) {
    const map = {
        int: { g: 'Intersecting Lines', s: 'Exactly 1 (Unique)', c: 'Consistent', e: 'Example: x − 2y = 0 and 3x + 4y − 20 = 0 -> Ratios: 1/3 ≠ −2/4' },
        coi: { g: 'Coincident Lines', s: 'Infinitely Many', c: 'Dependent (Consistent)', e: 'Example: 2x + 3y − 9 = 0 and 4x + 6y − 18 = 0 -> Ratios: 2/4 = 3/6 = (−9)/(−18) = 1/2' },
        par: { g: 'Parallel Lines', s: 'Zero (No Solution)', c: 'Inconsistent', e: 'Example: x + 2y − 4 = 0 and 2x + 4y − 12 = 0 -> Ratios: 1/2 = 2/4 ≠ (−4)/(−12) = 1/3' }
    };
    const d = map[k];
    if (!d) return;
    ['int', 'coi', 'par'].forEach(x => {
        const b = document.getElementById('btn-t31-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('t31-geo').textContent = d.g;
    document.getElementById('t31-sol').textContent = d.s;
    document.getElementById('t31-con').textContent = d.c;
    document.getElementById('t31-ex').textContent = d.e;
}
</script>
"""

# Simulator 6: Checking Consistency Live
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔎</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Exercise 3.1 Live Consistency &amp; Sign-Trap Tester</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">4 Classic Pairs</span>
    </div>

    <p class="text-xs text-slate-300">Evaluate real NCERT Exercise 3.1 equation pairs cleanly by inspecting simplified ratios!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="testConPair('p1')" id="btn-cp-p1" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">5x−4y+8 / 7x+6y−9</button>
        <button onclick="testConPair('p2')" id="btn-cp-p2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">9x+3y+12 / 18x+6y+24</button>
        <button onclick="testConPair('p3')" id="btn-cp-p3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">6x−3y+10 / 2x−y+9</button>
        <button onclick="testConPair('p4')" id="btn-cp-p4" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-amber-700 hover:bg-slate-800">3x+2y=5 / 2x−3y=7</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300" id="cp-rat">a₁/a₂ = 5/7   vs   b₁/b₂ = −4/6 = −2/3</div>
        <div class="font-sans text-emerald-300 font-bold" id="cp-res">✅ Intersecting Lines -> Consistent (Unique Solution)</div>
    </div>
</div>

<script>
function testConPair(k) {
    const map = {
        p1: { r: 'a₁/a₂ = 5/7   vs   b₁/b₂ = −4/6 = −2/3', res: '✅ Intersecting Lines -> Consistent (Unique Solution)', ok: true },
        p2: { r: 'a₁/a₂ = 9/18 = 1/2  |  b₁/b₂ = 3/6 = 1/2  |  c₁/c₂ = 12/24 = 1/2', res: '✅ Coincident Lines -> Consistent Dependent (∞ Many Solutions)', ok: true },
        p3: { r: 'a₁/a₂ = 6/2 = 3  |  b₁/b₂ = (−3)/(−1) = +3  ≠  c₁/c₂ = 10/9', res: '❌ Parallel Lines -> Inconsistent (0 Solutions)', ok: false },
        p4: { r: 'Sign Trap Check: a₁/a₂ = 3/2  ≠  b₁/b₂ = 2/(−3) = −2/3', res: '✅ Intersecting Lines -> Consistent (Unique Solution)! Opposite signs break equality immediately.', ok: true }
    };
    const d = map[k];
    if (!d) return;
    ['p1', 'p2', 'p3', 'p4'].forEach(x => {
        const b = document.getElementById('btn-cp-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('cp-rat').textContent = d.r;
    const rs = document.getElementById('cp-res');
    rs.textContent = d.res;
    rs.className = d.ok ? 'font-sans text-emerald-300 font-bold' : 'font-sans text-rose-300 font-bold';
}
</script>
"""

# Simulator 7: Shopping Pants Skirts
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🛍️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Boutique Riddle &amp; Garden Perimeter Graph Solver</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Graphical Examples</span>
    </div>

    <p class="text-xs text-slate-300">Inspect both NCERT graphical word puzzles—seeing how equations intersect at exact clean integer answers!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="showWordGraph('shop')" id="btn-wg-shop" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Pants &amp; Skirts Riddle</button>
        <button onclick="showWordGraph('garden')" id="btn-wg-garden" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Garden Perimeter (Ex 3.1 Q5)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="wg-eqs">Line 1: y = 2x − 2  [pts (1,0), (2,2)]   |   Line 2: y = 4x − 4  [pts (1,0), (0,−4)]</div>
        <div class="text-emerald-300 font-bold font-sans" id="wg-ans">✅ Graphical Crossing: (1, 0) -> 1 Pant and 0 Skirts purchased!</div>
    </div>
</div>

<script>
function showWordGraph(k) {
    const map = {
        shop: { e: 'Line 1: y = 2x − 2  [pts (1,0), (2,2)]   |   Line 2: y = 4x − 4  [pts (1,0), (0,−4)]', a: '✅ Graphical Crossing: (1, 0) -> 1 Pant and 0 Skirts purchased!' },
        garden: { e: 'Half Perimeter: x + y = 36  [pts (0,36), (36,0)]   |   Diff: x − y = 4  [pts (4,0), (20,16)]', a: '✅ Graphical Crossing: (20, 16) -> Garden Length = 20 m and Width = 16 m!' }
    };
    const d = map[k];
    if (!d) return;
    ['shop', 'garden'].forEach(x => {
        const b = document.getElementById('btn-wg-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('wg-eqs').textContent = d.e;
    document.getElementById('wg-ans').textContent = d.a;
}
</script>
"""

# Simulator 8: Substitution Method Steps
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔁</span>
            <h3 class="text-sm sm:text-base font-bold text-sky-300">Substitution Method 3-Step Fraction Solver</h3>
        </div>
        <span class="text-[11px] bg-sky-950/80 text-sky-300 px-2.5 py-1 rounded-full border border-sky-800">7x−15y=2 &amp; x+2y=3</span>
    </div>

    <p class="text-xs text-slate-300">Walk through Textbook Example 7 step by step to compute exact fractions (49/29, 19/29) impossible to read cleanly off graphs!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="stepSubst(1)" id="btn-sb-1" class="p-2 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500">1. Isolate x</button>
        <button onclick="stepSubst(2)" id="btn-sb-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. Substitute &amp; Solve y</button>
        <button onclick="stepSubst(3)" id="btn-sb-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. Back-Substitute x</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="sb-math">From simpler Eq 2 (x + 2y = 3):  x = 3 − 2y</div>
        <p class="font-sans text-slate-300 leading-relaxed" id="sb-note">Pick the equation with coefficient 1 in front of x so isolating x introduces zero fractions!</p>
    </div>
</div>

<script>
function stepSubst(n) {
    const map = {
        1: { m: 'From simpler Eq 2 (x + 2y = 3):  x = 3 − 2y', n: 'Pick the equation with coefficient 1 in front of x so isolating x introduces zero fractions!' },
        2: { m: '7(3 − 2y) − 15y = 2  ⟹  21 − 14y − 15y = 2  ⟹  −29y = −19  ⟹  y = 19 / 29', n: 'Plugging (3 − 2y) into Equation 1 leaves a single-variable linear equation in y alone, giving exact y = 19/29!' },
        3: { m: 'x = 3 − 2(19 / 29) = 87/29 − 38/29 = 49 / 29  ✅ Solution: (49/29, 19/29)', n: 'Substituting y back into Step 1 formula yields exact x = 49/29 cleanly!' }
    };
    const d = map[n];
    if (!d) return;
    [1, 2, 3].forEach(k => {
        const b = document.getElementById('btn-sb-' + k);
        if (b) {
            b.className = (k === n)
                ? 'p-2 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('sb-math').textContent = d.m;
    document.getElementById('sb-note').textContent = d.n;
}
</script>
"""
