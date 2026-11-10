#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 4: Quadratic Equations
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Prayer Hall Equations
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🕌</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Prayer Hall Carpet Area Builder (Section 4.1)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">2x² + x − 300 = 0</span>
    </div>

    <p class="text-xs text-slate-300">Test trial breadths x (with length = 2x + 1) to hit the exact target carpet area of 300 m²!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="testPrayerHall(10)" id="btn-ph-10" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Breadth x = 10 m</button>
        <button onclick="testPrayerHall(12)" id="btn-ph-12" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Breadth x = 12 m</button>
        <button onclick="testPrayerHall(15)" id="btn-ph-15" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Breadth x = 15 m</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 240 140" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <rect x="30" y="25" width="180" height="80" rx="4" fill="#92400e" stroke="#fbbf24" stroke-width="2.5" />
            <text x="120" y="68" fill="#fef08a" font-size="13" font-weight="bold" text-anchor="middle" id="ph-svg-area">Area = 300 m² ✅</text>
            <text x="120" y="122" fill="#7dd3fc" font-size="10" font-weight="bold" text-anchor="middle" id="ph-svg-len">Length = 2(12) + 1 = 25 m</text>
            <text x="16" y="70" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle" transform="rotate(-90 16 70)" id="ph-svg-br">12 m</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
            <div class="text-cyan-300" id="ph-dims">Breadth x = 12 m  |  Length (2x + 1) = 25 m</div>
            <div class="text-emerald-300 font-bold" id="ph-eq">Check 2(12)² + 12 − 300 = 288 + 12 − 300 = 0 ✅</div>
        </div>
    </div>
</div>

<script>
function testPrayerHall(x) {
    const len = 2 * x + 1;
    const area = x * len;
    const lhs = 2 * x * x + x - 300;
    [10, 12, 15].forEach(k => {
        const b = document.getElementById('btn-ph-' + k);
        if (b) {
            b.className = (k === x)
                ? 'p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('ph-svg-area').textContent = area === 300 ? `Area = 300 m² ✅` : `Area = ${area} m²`;
    document.getElementById('ph-svg-len').textContent = `Length = 2(${x}) + 1 = ${len} m`;
    document.getElementById('ph-svg-br').textContent = `${x} m`;
    document.getElementById('ph-dims').textContent = `Breadth x = ${x} m  |  Length (2x + 1) = ${len} m`;
    document.getElementById('ph-eq').textContent = `2(${x})² + ${x} − 300 = ${lhs} ${lhs === 0 ? '✅ Match!' : '≠ 0'}`;
}
</script>
"""

# Simulator 2: Quadratic History Timeline
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏛️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">4,000 Years of Quadratic Discovery Timeline</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Historical Milestones</span>
    </div>

    <p class="text-xs text-slate-300">Click each civilization milestone from Section 4.1 to explore how mathematicians built quadratic algebra step by step!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectHist('bab')" id="btn-hs-bab" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Babylonians &amp; Euclid</button>
        <button onclick="inspectHist('bra')" id="btn-hs-bra" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Brahmagupta</button>
        <button onclick="inspectHist('sri')" id="btn-hs-sri" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Sridharacharya</button>
        <button onclick="inspectHist('alk')" id="btn-hs-alk" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Al-Khwarizmi &amp; Europe</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
        <h4 class="font-bold text-cyan-300 text-sm" id="hs-title">Ancient Babylonians (~2000 BC) &amp; Greek Euclid (~300 BC)</h4>
        <p class="text-slate-300 leading-relaxed" id="hs-desc">Babylonian clay tablets first solved rectangular area-sum-product problems, while Greek mathematician Euclid developed geometric square-cutting constructions to determine unknown side lengths.</p>
    </div>
</div>

<script>
function inspectHist(k) {
    const map = {
        bab: { t: 'Ancient Babylonians (~2000 BC) & Greek Euclid (~300 BC)', d: 'Babylonian clay tablets first solved rectangular area-sum-product problems, while Greek mathematician Euclid developed geometric square-cutting constructions to determine unknown side lengths.' },
        bra: { t: 'Indian Pioneer: Brahmagupta (AD 598–665)', d: 'In Brahmasphutasiddhanta, Brahmagupta gave an explicit algebraic rule in words solving equations of the form ax² + bx = c, treating negative values clearly!' },
        sri: { t: 'Indian Pioneer: Sridharacharya (AD 1025)', d: 'Sridharacharya derived the famous explicit Quadratic Formula x = (−b ± √(b² − 4ac)) / (2a) using the completing-the-square method still taught across classrooms today!' },
        alk: { t: 'Arab Scholar Al-Khwarizmi (~AD 800) & European Texts', d: 'Baghdad scholar Al-Khwarizmi classified quadratic types systematically in Al-Jabr (giving Algebra its name), later expanded across Europe via Abraham bar Hiyya (AD 1145).' }
    };
    const d = map[k];
    if (!d) return;
    ['bab', 'bra', 'sri', 'alk'].forEach(x => {
        const b = document.getElementById('btn-hs-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('hs-title').textContent = d.t;
    document.getElementById('hs-desc').textContent = d.d;
}
</script>
"""

# Simulator 3: Standard Quadratic Form
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📏</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Standard Form Sorter: ax² + bx + c = 0 (a ≠ 0)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Coeff Classifier</span>
    </div>

    <p class="text-xs text-slate-300">Rearrange scrambled equations cleanly into ax² + bx + c = 0 to identify exact coefficients a, b, and c (and catch a = 0 traps!).</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="sortStdQuad('s1')" id="btn-sq-s1" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">7 − 4x = −5x²</button>
        <button onclick="sortStdQuad('s2')" id="btn-sq-s2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2x² − 3 = 0</button>
        <button onclick="sortStdQuad('s3')" id="btn-sq-s3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">5x² = −7x</button>
        <button onclick="sortStdQuad('s4')" id="btn-sq-s4" class="p-2 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-rose-700 hover:bg-slate-800">0x² + 4x − 9 = 0</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="sq-std">Standard Form: 5x² − 4x + 7 = 0</div>
        <div class="text-cyan-300" id="sq-abc">a = 5,   b = −4,   c = 7</div>
        <div class="font-sans text-emerald-300 font-bold" id="sq-res">✅ Valid Quadratic Equation (a = 5 ≠ 0)</div>
    </div>
</div>

<script>
function sortStdQuad(k) {
    const map = {
        s1: { st: 'Standard Form: 5x² − 4x + 7 = 0', abc: 'a = 5,   b = −4,   c = 7', r: '✅ Valid Quadratic Equation (a = 5 ≠ 0)', ok: true },
        s2: { st: 'Standard Form: 2x² + 0x − 3 = 0', abc: 'a = 2,   b = 0,   c = −3', r: '✅ Valid Quadratic! Middle coefficient b is allowed to equal 0.', ok: true },
        s3: { st: 'Standard Form: 5x² + 7x + 0 = 0', abc: 'a = 5,   b = 7,   c = 0', r: '✅ Valid Quadratic! Constant term c is allowed to equal 0.', ok: true },
        s4: { st: 'Simplifies to: 4x − 9 = 0', abc: 'a = 0,   b = 4,   c = −9', r: '❌ NOT Quadratic! Since a = 0 eliminates x², this collapses to a degree-1 linear equation.', ok: false }
    };
    const d = map[k];
    if (!d) return;
    ['s1', 's2', 's3', 's4'].forEach(x => {
        const b = document.getElementById('btn-sq-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('sq-std').textContent = d.st;
    document.getElementById('sq-abc').textContent = d.abc;
    const rs = document.getElementById('sq-res');
    rs.textContent = d.r;
    rs.className = d.ok ? 'font-sans text-emerald-300 font-bold' : 'font-sans text-rose-300 font-bold';
}
</script>
"""

# Simulator 4: Disguised Equation Detector
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🕵️</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Exercise 4.1 Disguised Equation Detector</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">Expand Before Judging!</span>
    </div>

    <p class="text-xs text-slate-300">Expand both sides completely before judging—watch hidden cancellations expose true quadratics vs traps!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="detectDisguise('d1')" id="btn-dg4-d1" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">(x−2)(x+1) = (x−1)(x+3)</button>
        <button onclick="detectDisguise('d2')" id="btn-dg4-d2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">(x+1)² = 2(x−3)</button>
        <button onclick="detectDisguise('d3')" id="btn-dg4-d3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">x³−4x²−x+1 = (x−2)³</button>
        <button onclick="detectDisguise('d4')" id="btn-dg4-d4" class="p-2 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-rose-700 hover:bg-slate-800">(x+2)³ = 2x(x²−1)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="dg4-exp">Expand: x² − x − 2 = x² + 2x − 3</div>
        <div class="text-amber-300 font-bold" id="dg4-simp">Cancel x²: −3x + 1 = 0  (Degree 1 Linear!)</div>
        <div class="font-sans text-rose-300 font-bold" id="dg4-ver">❌ LINEAR TRAP! x² cancels cleanly out on both sides—NOT Quadratic!</div>
    </div>
</div>

<script>
function detectDisguise(k) {
    const map = {
        d1: { e: 'Expand: x² − x − 2 = x² + 2x − 3', s: 'Cancel x²: −3x + 1 = 0  (Degree 1 Linear!)', v: '❌ LINEAR TRAP! x² cancels cleanly out on both sides—NOT Quadratic!', ok: false },
        d2: { e: 'Expand: x² + 2x + 1 = 2x − 6', s: 'Simplify: x² + 7 = 0  (a = 1 ≠ 0, b = 0, c = 7)', v: '✅ TRUE QUADRATIC! Although 2x cancels, x² survives cleanly!', ok: true },
        d3: { e: 'Expand RHS: x³ − 4x² − x + 1 = x³ − 6x² + 12x − 8', s: 'Cancel x³: 2x² − 13x + 9 = 0  (a = 2 ≠ 0)', v: '✅ DISGUISED QUADRATIC! Both x³ terms cancel identically, leaving degree 2!', ok: true },
        d4: { e: 'Expand: x³ + 6x² + 12x + 8 = 2x³ − 2x', s: 'Simplify: x³ − 6x² − 14x − 8 = 0  (Degree 3!)', v: '❌ CUBIC TRAP! 2x³ − x³ leaves x³ alive—Degree 3 Cubic, NOT Quadratic!', ok: false }
    };
    const d = map[k];
    if (!d) return;
    ['d1', 'd2', 'd3', 'd4'].forEach(x => {
        const b = document.getElementById('btn-dg4-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('dg4-exp').textContent = d.e;
    document.getElementById('dg4-simp').textContent = d.s;
    const vv = document.getElementById('dg4-ver');
    vv.textContent = d.v;
    vv.className = d.ok ? 'font-sans text-emerald-300 font-bold' : 'font-sans text-rose-300 font-bold';
}
</script>
"""

# Simulator 5: Marbles And Toys
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔮</span>
            <h3 class="text-sm sm:text-base font-bold text-sky-300">Section 4.2 &amp; Ex 4.1 Word-Story Equation Modeler</h3>
        </div>
        <span class="text-[11px] bg-sky-950/80 text-sky-300 px-2.5 py-1 rounded-full border border-sky-800">Word Modeling</span>
    </div>

    <p class="text-xs text-slate-300">Select each classic NCERT story (Marbles, Cottage Toys, Consecutive Integers) to translate ONE unknown variable cleanly into quadratic form!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="modelWord42('mar')" id="btn-mw-mar" class="p-2 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500">45 Marbles Lost 5</button>
        <button onclick="modelWord42('toy')" id="btn-mw-toy" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Daily Toy Cost ₹750</button>
        <button onclick="modelWord42('int')" id="btn-mw-int" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Consecutive Product 306</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="mw-vars">Start: x and (45 − x)  ⟹  After losing 5: (x − 5) and (40 − x)</div>
        <div class="text-amber-300 font-bold" id="mw-eq">Product: (x − 5)(40 − x) = 124  ⟹  x² − 45x + 324 = 0</div>
        <div class="font-sans text-emerald-300 font-bold" id="mw-sol">Solved Counts: Student A &amp; B had 36 and 9 marbles cleanly!</div>
    </div>
</div>

<script>
function modelWord42(k) {
    const map = {
        mar: { v: 'Start: x and (45 − x)  ⟹  After losing 5: (x − 5) and (40 − x)', e: 'Product: (x − 5)(40 − x) = 124  ⟹  x² − 45x + 324 = 0', s: 'Solved Counts: Student A & B started with 36 and 9 marbles cleanly!' },
        toy: { v: 'Units produced = x  |  Cost per toy = ₹(55 − x)', e: 'Total Daily Bill: x(55 − x) = 750  ⟹  x² − 55x + 750 = 0', s: 'Solved Counts: 25 or 30 wooden toys produced that day!' },
        int: { v: 'Consecutive Positive Integers: x  and  (x + 1)', e: 'Product: x(x + 1) = 306  ⟹  x² + x − 306 = 0', s: 'Solved Integers: 17 and 18 (17 × 18 = 306 ✅)!' }
    };
    const d = map[k];
    if (!d) return;
    ['mar', 'toy', 'int'].forEach(x => {
        const b = document.getElementById('btn-mw-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('mw-vars').textContent = d.v;
    document.getElementById('mw-eq').textContent = d.e;
    document.getElementById('mw-sol').textContent = d.s;
}
</script>
"""

# Simulator 6: Zeroes Equal Roots
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔗</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Polynomial Zeroes vs. Equation Roots Bridge (2x² − 3x + 1)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Exact Twins</span>
    </div>

    <p class="text-xs text-slate-300">Test numbers inside both p(x) = 2x² − 3x + 1 and equation 2x² − 3x + 1 = 0 to witness root-zero equivalence!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="testTwinRoot('1')" id="btn-tr4-1" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">Test x = 1</button>
        <button onclick="testTwinRoot('half')" id="btn-tr4-half" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Test x = 1/2</button>
        <button onclick="testTwinRoot('2')" id="btn-tr4-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Test x = 2</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs font-mono">
        <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800">
            <div class="text-cyan-300 font-bold font-sans mb-1">Chapter 2 Polynomial View: p(x)</div>
            <div class="text-slate-200" id="tr4-poly">p(1) = 2(1)² − 3(1) + 1 = 0  ⟹  ZERO of p(x) ✅</div>
        </div>
        <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800">
            <div class="text-amber-300 font-bold font-sans mb-1">Chapter 4 Equation View: p(x) = 0</div>
            <div class="text-slate-200" id="tr4-eq">LHS = 0 = RHS  ⟹  ROOT of 2x²−3x+1=0 ✅</div>
        </div>
    </div>
</div>

<script>
function testTwinRoot(k) {
    const map = {
        '1': { p: 'p(1) = 2(1)² − 3(1) + 1 = 0  ⟹  ZERO of p(x) ✅', e: 'LHS = 0 = RHS  ⟹  ROOT of 2x²−3x+1=0 ✅' },
        'half': { p: 'p(1/2) = 2(1/4) − 3/2 + 1 = 0  ⟹  ZERO of p(x) ✅', e: 'LHS = 0 = RHS  ⟹  ROOT of 2x²−3x+1=0 ✅' },
        '2': { p: 'p(2) = 2(4) − 6 + 1 = +3 ≠ 0  (NOT a zero ❌)', e: 'LHS = 3 ≠ 0  (NOT a root ❌)' }
    };
    const d = map[k];
    if (!d) return;
    ['1', 'half', '2'].forEach(x => {
        const b = document.getElementById('btn-tr4-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('tr4-poly').textContent = d.p;
    document.getElementById('tr4-eq').textContent = d.e;
}
</script>
"""

# Simulator 7: Factoring Middle Term
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✂️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Factorisation Solver: Splitting the Middle Term (Sec 4.3)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Linear Factors</span>
    </div>

    <p class="text-xs text-slate-300">Pick any textbook equation to step cleanly through a·c products, middle splits, factor brackets, and exact roots!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="factorQuadEx('f1')" id="btn-fq-f1" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">2x² − 5x + 3 = 0</button>
        <button onclick="factorQuadEx('f2')" id="btn-fq-f2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">6x² − x − 2 = 0</button>
        <button onclick="factorQuadEx('f3')" id="btn-fq-f3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">100x² − 20x + 1 = 0</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs">
        <div class="text-amber-300 font-bold" id="fq-split">Target: a·c = +6, sum b = −5  ⟹  split −5x = −2x − 3x</div>
        <div class="text-cyan-300" id="fq-fac">Factor Pairs: 2x(x − 1) − 3(x − 1) = (2x − 3)(x − 1) = 0</div>
        <div class="text-emerald-300 font-bold" id="fq-roots">Roots (Zero Product Rule): x = 3/2  and  x = 1 ✅</div>
    </div>
</div>

<script>
function factorQuadEx(k) {
    const map = {
        f1: { sp: 'Target: a·c = +6, sum b = −5  ⟹  split −5x = −2x − 3x', fa: 'Factor Pairs: 2x(x − 1) − 3(x − 1) = (2x − 3)(x − 1) = 0', r: 'Roots (Zero Product Rule): x = 3/2  and  x = 1 ✅' },
        f2: { sp: 'Target: a·c = −12, sum b = −1  ⟹  split −x = +3x − 4x', fa: 'Factor Pairs: 3x(2x + 1) − 2(2x + 1) = (3x − 2)(2x + 1) = 0', r: 'Roots (Zero Product Rule): x = 2/3  and  x = −1/2 ✅' },
        f3: { sp: 'Perfect Square: a·c = +100, sum b = −20  ⟹  split −10x − 10x', fa: 'Factor Pairs: (10x − 1)(10x − 1) = (10x − 1)² = 0', r: 'Two Equal Repeated Roots: x = 1/10  and  x = 1/10 ✅' }
    };
    const d = map[k];
    if (!d) return;
    ['f1', 'f2', 'f3'].forEach(x => {
        const b = document.getElementById('btn-fq-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('fq-split').textContent = d.sp;
    document.getElementById('fq-fac').textContent = d.fa;
    document.getElementById('fq-roots').textContent = d.r;
}
</script>
"""

# Simulator 8: Radical Quadratic Factoring
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✳️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Square-Root Coefficient Factoring Studio</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Ex 5 &amp; Ex 4.2</span>
    </div>

    <p class="text-xs text-slate-300">Compare both square-root factoring challenges—notice how writing 3 = √3·√3 and 2 = √2·√2 unlocks common factors effortlessly!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="showRadFac('ex5')" id="btn-rf-ex5" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">3x² − 2√6x + 2 = 0</button>
        <button onclick="showRadFac('q13')" id="btn-rf-q13" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">√2x² + 7x + 5√2 = 0</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs">
        <div class="text-cyan-300" id="rf-sp">a·c = 3×2 = 6; (−√6)(−√6) = +6  ⟹  3x² − √6x − √6x + 2 = 0</div>
        <div class="text-amber-300 font-bold" id="rf-fac">Use 3 = √3·√3, √6 = √3·√2, 2 = √2·√2: √3x(√3x − √2) − √2(√3x − √2) = 0</div>
        <div class="text-emerald-300 font-bold" id="rf-rt">Roots: (√3x − √2)² = 0  ⟹  x = √(2/3), √(2/3) ✅</div>
    </div>
</div>

<script>
function showRadFac(k) {
    const map = {
        ex5: { s: 'a·c = 3×2 = 6; (−√6)(−√6) = +6  ⟹  3x² − √6x − √6x + 2 = 0', f: 'Use 3 = √3·√3, √6 = √3·√2, 2 = √2·√2: √3x(√3x − √2) − √2(√3x − √2) = 0', r: 'Roots: (√3x − √2)² = 0  ⟹  x = √(2/3), √(2/3) ✅' },
        q13: { s: 'a·c = √2 × 5√2 = 10; 2 + 5 = 7  ⟹  √2x² + 2x + 5x + 5√2 = 0', f: 'Use 2 = √2·√2 cleanly: √2x(x + √2) + 5(x + √2) = 0', r: 'Roots: (√2x + 5)(x + √2) = 0  ⟹  x = −5/√2, −√2 ✅' }
    };
    const d = map[k];
    if (!d) return;
    ['ex5', 'q13'].forEach(x => {
        const b = document.getElementById('btn-rf-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('rf-sp').textContent = d.s;
    document.getElementById('rf-fac').textContent = d.f;
    document.getElementById('rf-rt').textContent = d.r;
}
</script>
"""
