#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 2: Polynomials
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Degree Zero Bound
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📈</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Exercise 2.1 Visual Zero Counter &amp; Degree Bound Lab</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">At Most n Zeroes</span>
    </div>

    <p class="text-xs text-slate-300">Click each Exercise 2.1 style curve to count ONLY horizontal x-axis intersections (ignoring y-axis crossings!) and deduce minimum degree!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectEx21('zero')" id="btn-e21-zero" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Parallel Line (0)</button>
        <button onclick="inspectEx21('one')" id="btn-e21-one" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">1 Cross + y-Cut</button>
        <button onclick="inspectEx21('three')" id="btn-e21-three" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3 Waves (Cubic)</button>
        <button onclick="inspectEx21('four')" id="btn-e21-four" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">W-Curve (4 Cuts)</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 160" class="w-full h-auto max-h-[160px] rounded-xl bg-slate-950 border border-slate-800">
            <line x1="10" y1="85" x2="210" y2="85" stroke="#64748b" stroke-width="1.5" />
            <line x1="110" y1="10" x2="110" y2="150" stroke="#64748b" stroke-width="1.5" />
            <g id="e21-zero-svg"><line x1="25" y1="45" x2="195" y2="45" stroke="#f87171" stroke-width="3" /></g>
            <g id="e21-one-svg" class="hidden"><path d="M35,140 Q115,10 190,115" fill="none" stroke="#38bdf8" stroke-width="3" /><circle cx="63" cy="85" r="4.5" fill="#fde047" /><circle cx="177" cy="85" r="4.5" fill="#fde047" /></g>
            <g id="e21-three-svg" class="hidden"><path d="M30,145 C55,25 85,25 110,85 C135,145 165,145 190,20" fill="none" stroke="#22c55e" stroke-width="3" /><circle cx="52" cy="85" r="4" fill="#fde047" /><circle cx="110" cy="85" r="4" fill="#fde047" /><circle cx="168" cy="85" r="4" fill="#fde047" /></g>
            <g id="e21-four-svg" class="hidden"><path d="M25,25 Q50,145 75,85 Q95,30 115,85 Q140,145 165,85 Q185,35 200,25" fill="none" stroke="#a855f7" stroke-width="3" /><circle cx="40" cy="85" r="4" fill="#fde047" /><circle cx="75" cy="85" r="4" fill="#fde047" /><circle cx="115" cy="85" r="4" fill="#fde047" /><circle cx="165" cy="85" r="4" fill="#fde047" /></g>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-amber-300 text-sm" id="e21-title">Horizontal Parallel Line -> 0 Zeroes</h4>
            <p class="text-slate-300 leading-relaxed" id="e21-desc">Hovering strictly parallel above the x-axis means zero points share height y = 0! Therefore constant polynomial y = c has 0 zeroes.</p>
        </div>
    </div>
</div>

<script>
function inspectEx21(k) {
    ['zero', 'one', 'three', 'four'].forEach(x => {
        const b = document.getElementById('btn-e21-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        document.getElementById('e21-' + x + '-svg').classList.toggle('hidden', x !== k);
    });
    const map = {
        zero: { t: 'Horizontal Parallel Line -> 0 Zeroes', d: 'Hovering strictly parallel above the x-axis means zero points share height y = 0! Therefore constant polynomial y = c has 0 zeroes.' },
        one: { t: 'Two x-Cuts + One y-Cut -> 2 Zeroes (Ignore y-Cut!)', d: 'Notice the parabola cuts the vertical y-axis once—IGNORE y-axis cuts! Count strictly the 2 yellow dots lying on the horizontal x-axis -> 2 zeroes.' },
        three: { t: '3 x-Axis Intersections -> 3 Zeroes (Minimum Degree 3)', d: 'Slicing the x-axis 3 times yields 3 real zeroes! By the general bound (degree n has at most n zeroes), degree must be at least 3.' },
        four: { t: 'W-Shaped Curve Crossing 4 Times -> 4 Zeroes (Minimum Degree 4)', d: 'Four distinct x-axis intersections confirm 4 real zeroes—impossible for linear, quadratic, or cubic graphs!' }
    };
    document.getElementById('e21-title').textContent = map[k].t;
    document.getElementById('e21-desc').textContent = map[k].d;
}
</script>
"""

# Simulator 10: Quadratic Sum Product
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚖️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Quadratic Sum (α + β) &amp; Product (αβ) Formula Verifier</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">ax² + bx + c</span>
    </div>

    <p class="text-xs text-slate-300">Click any quadratic polynomial to verify both formulas: α + β = −b/a and αβ = c/a directly from its roots!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="verifyQuadVieta('q1')" id="btn-qv-q1" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">2x² − 8x + 6</button>
        <button onclick="verifyQuadVieta('q2')" id="btn-qv-q2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3x² − 12x + 7</button>
        <button onclick="verifyQuadVieta('q3')" id="btn-qv-q3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">x² + 7x + 10</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 font-mono text-xs">
        <div class="text-cyan-300" id="qv-abc">Coefficients: a = 2, b = −8, c = 6  |  Factored: 2(x − 1)(x − 3) -> Zeroes α = 1, β = 3</div>
        <div class="text-amber-300" id="qv-sum">Sum: α + β = 1 + 3 = 4   ≡   −b/a = −(−8)/2 = +4 ✅</div>
        <div class="text-emerald-300" id="qv-prod">Product: αβ = 1 × 3 = 3   ≡   c/a = 6/2 = +3 ✅</div>
    </div>
</div>

<script>
function verifyQuadVieta(k) {
    const map = {
        q1: { a: 'Coefficients: a = 2, b = −8, c = 6  |  Factored: 2(x − 1)(x − 3) -> Zeroes α = 1, β = 3', s: 'Sum: α + β = 1 + 3 = 4   ≡   −b/a = −(−8)/2 = +4 ✅', p: 'Product: αβ = 1 × 3 = 3   ≡   c/a = 6/2 = +3 ✅' },
        q2: { a: 'Coefficients: a = 3, b = −12, c = 7  (Direct Coefficient Formula without solving roots!)', s: 'Sum: α + β = −b/a = −(−12) / 3 = +4 ✅', p: 'Product: αβ = c/a = 7 / 3 ✅' },
        q3: { a: 'Coefficients: a = 1, b = 7, c = 10  |  Factored: (x + 2)(x + 5) -> Zeroes α = −2, β = −5', s: 'Sum: α + β = −2 + (−5) = −7   ≡   −b/a = −7/1 = −7 ✅', p: 'Product: αβ = (−2) × (−5) = +10   ≡   c/a = 10/1 = +10 ✅' }
    };
    const d = map[k];
    if (!d) return;
    ['q1', 'q2', 'q3'].forEach(x => {
        const b = document.getElementById('btn-qv-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('qv-abc').textContent = d.a;
    document.getElementById('qv-sum').textContent = d.s;
    document.getElementById('qv-prod').textContent = d.p;
}
</script>
"""

# Simulator 11: Middle Term Factoring
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✂️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Middle-Term Splitting &amp; Standard Reorder Trainer</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Exercise 2.2 Q1</span>
    </div>

    <p class="text-xs text-slate-300">Inspect clean middle-term splits—including the classic unsorted 6x² − 3 − 7x trap from Exercise 2.2!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="splitMiddle('m1')" id="btn-mt-m1" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">x² − 2x − 8</button>
        <button onclick="splitMiddle('m2')" id="btn-mt-m2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">4s² − 4s + 1</button>
        <button onclick="splitMiddle('m3')" id="btn-mt-m3" class="p-2 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-rose-700 hover:bg-slate-800">6x² − 3 − 7x (Trap!)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs">
        <div class="text-amber-300 font-bold" id="mt-std">Standard Form: x² − 2x − 8  (a·c = −8, sum b = −2 -> split −4 &amp; +2)</div>
        <div class="text-cyan-300" id="mt-fac">Split &amp; Group: x² − 4x + 2x − 8 = x(x − 4) + 2(x − 4) = (x − 4)(x + 2)</div>
        <div class="text-emerald-300 font-bold" id="mt-ver">Zeroes: 4, −2  |  Sum = 2 = −(−2)/1 ✅  |  Product = −8 = −8/1 ✅</div>
    </div>
</div>

<script>
function splitMiddle(k) {
    const map = {
        m1: { std: 'Standard Form: x² − 2x − 8  (a·c = −8, sum b = −2 -> split −4 & +2)', fac: 'Split & Group: x² − 4x + 2x − 8 = x(x − 4) + 2(x − 4) = (x − 4)(x + 2)', ver: 'Zeroes: 4, −2  |  Sum = 2 = −(−2)/1 ✅  |  Product = −8 = −8/1 ✅' },
        m2: { std: 'Standard Form: 4s² − 4s + 1  (a·c = +4, sum b = −4 -> split −2 & −2)', fac: 'Split & Group: 4s² − 2s − 2s + 1 = 2s(2s − 1) − 1(2s − 1) = (2s − 1)²', ver: 'Zeroes: 1/2, 1/2  |  Sum = 1 = −(−4)/4 ✅  |  Product = 1/4 = 1/4 ✅' },
        m3: { std: 'TRAP! Reorder FIRST: 6x² − 7x − 3  (a=6, b=−7, c=−3; a·c = −18 -> split −9 & +2)', fac: 'Split & Group: 6x² − 9x + 2x − 3 = 3x(2x − 3) + 1(2x − 3) = (2x − 3)(3x + 1)', ver: 'Zeroes: 3/2, −1/3  |  Sum = 7/6 = −(−7)/6 ✅  |  Product = −1/2 = −3/6 ✅' }
    };
    const d = map[k];
    if (!d) return;
    ['m1', 'm2', 'm3'].forEach(x => {
        const b = document.getElementById('btn-mt-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('mt-std').textContent = d.std;
    document.getElementById('mt-fac').textContent = d.fac;
    document.getElementById('mt-ver').textContent = d.ver;
}
</script>
"""

# Simulator 12: Missing Term Quadratics
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚡</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Fast Missing-Term Quadratic Solver (b = 0 or c = 0)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">Shortcuts</span>
    </div>

    <p class="text-xs text-slate-300">Master both special Exercise 2.2 shortcuts cleanly without wasting time trying middle-term splitting!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="solveMissing('x2_3')" id="btn-ms-x2_3" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">x² − 3 (b=0)</button>
        <button onclick="solveMissing('t2_15')" id="btn-ms-t2_15" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">t² − 15 (b=0)</button>
        <button onclick="solveMissing('4u2')" id="btn-ms-4u2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">4u² + 8u (c=0)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs">
        <div class="text-amber-300 font-bold" id="ms-trick">Use a² − b² Identity: x² − (√3)² = (x − √3)(x + √3) = 0</div>
        <div class="text-cyan-300" id="ms-roots">Zeroes: α = +√3, β = −√3</div>
        <div class="text-emerald-300" id="ms-check">Verify: α + β = 0 = −0/1 ✅  |  αβ = −3 = −3/1 ✅</div>
    </div>
</div>

<script>
function solveMissing(k) {
    const map = {
        x2_3: { t: 'Use a² − b² Identity: x² − (√3)² = (x − √3)(x + √3) = 0', r: 'Zeroes: α = +√3, β = −√3', c: 'Verify: α + β = 0 = −0/1 ✅  |  αβ = −3 = −3/1 ✅' },
        t2_15: { t: 'Use a² − b² Identity: t² − (√15)² = (t − √15)(t + √15) = 0', r: 'Zeroes: α = +√15, β = −√15', c: 'Verify: α + β = 0 = −0/1 ✅  |  αβ = −15 = −15/1 ✅' },
        '4u2': { t: 'Factor Common 4u Out (c = 0): 4u(u + 2) = 0 (Never cancel u!)', r: 'Zeroes: u = 0  and  u = −2', c: 'Verify: α + β = −2 = −8/4 ✅  |  αβ = 0 = 0/4 ✅' }
    };
    const d = map[k];
    if (!d) return;
    ['x2_3', 't2_15', '4u2'].forEach(x => {
        const b = document.getElementById('btn-ms-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('ms-trick').textContent = d.t;
    document.getElementById('ms-roots').textContent = d.r;
    document.getElementById('ms-check').textContent = d.c;
}
</script>
"""

# Simulator 13: Building Quadratic Polynomials
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏗️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Quadratic Polynomial Constructor: k[x² − Sx + P]</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Exercise 2.2 Q2</span>
    </div>

    <p class="text-xs text-slate-300">Select any given Sum (S) &amp; Product (P) pair from NCERT to build clean integer-coefficient quadratic polynomials automatically!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="buildQuad('b1')" id="btn-bq-b1" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">S=−3, P=2</button>
        <button onclick="buildQuad('b2')" id="btn-bq-b2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">S=1/4, P=−1</button>
        <button onclick="buildQuad('b3')" id="btn-bq-b3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">S=√2, P=1/3</button>
        <button onclick="buildQuad('b4')" id="btn-bq-b4" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">S=0, P=√5</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs">
        <div class="text-cyan-300" id="bq-sub">Plug into Template k[x² − Sx + P]: k[x² − (−3)x + 2]</div>
        <div class="text-amber-300 font-bold" id="bq-k">Choose Smart Multiplier: k = 1</div>
        <div class="text-emerald-400 font-bold text-sm pt-1" id="bq-final">Final Quadratic: x² + 3x + 2 ✅</div>
    </div>
</div>

<script>
function buildQuad(k) {
    const map = {
        b1: { s: 'Plug into Template k[x² − Sx + P]: k[x² − (−3)x + 2]', mul: 'Choose Smart Multiplier: k = 1', f: 'Final Quadratic: x² + 3x + 2 ✅' },
        b2: { s: 'Plug into Template k[x² − Sx + P]: k[x² − (1/4)x − 1]', mul: 'Choose Smart Multiplier: k = 4 (clears denominator 4!)', f: 'Final Quadratic: 4x² − x − 4 ✅' },
        b3: { s: 'Plug into Template k[x² − Sx + P]: k[x² − √2 x + 1/3]', mul: 'Choose Smart Multiplier: k = 3 (clears denominator 3!)', f: 'Final Quadratic: 3x² − 3√2 x + 1 ✅' },
        b4: { s: 'Plug into Template k[x² − Sx + P]: k[x² − 0·x + √5]', mul: 'Choose Smart Multiplier: k = 1', f: 'Final Quadratic: x² + √5 ✅' }
    };
    const d = map[k];
    if (!d) return;
    ['b1', 'b2', 'b3', 'b4'].forEach(x => {
        const b = document.getElementById('btn-bq-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('bq-sub').textContent = d.s;
    document.getElementById('bq-k').textContent = d.mul;
    document.getElementById('bq-final').textContent = d.f;
}
</script>
"""

# Simulator 14: Cubic Zero Relations
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧊</span>
            <h3 class="text-sm sm:text-base font-bold text-sky-300">Cubic Symmetric Identities (ax³ + bx² + cx + d)</h3>
        </div>
        <span class="text-[11px] bg-sky-950/80 text-sky-300 px-2.5 py-1 rounded-full border border-sky-800">Alternating Signs − + −</span>
    </div>

    <p class="text-xs text-slate-300">Inspect each of the three cubic coefficient laws showing why alternating minus, plus, minus signs appear naturally!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="inspectCubicLaw('s1')" id="btn-clw-s1" class="p-2 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500">1. α + β + γ</button>
        <button onclick="inspectCubicLaw('s2')" id="btn-clw-s2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. αβ + βγ + γα</button>
        <button onclick="inspectCubicLaw('s3')" id="btn-clw-s3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. αβγ</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="font-mono text-amber-300 font-bold text-sm" id="clw-eq">Sum of Singles: α + β + γ = −b / a   (Sign: MINUS −)</div>
        <p class="text-slate-300 leading-relaxed" id="clw-desc">In expanding a(x − α)(x − β)(x − γ), multiplying one root times two x terms creates −a(α + β + γ)x², equaling bx²!</p>
    </div>
</div>

<script>
function inspectCubicLaw(k) {
    const map = {
        s1: { e: 'Sum of Singles: α + β + γ = −b / a   (Sign: MINUS −)', d: 'In expanding a(x − α)(x − β)(x − γ), multiplying one root times two x terms creates −a(α + β + γ)x², equaling bx²!' },
        s2: { e: 'Pairwise Products Sum: αβ + βγ + γα = +c / a   (Sign: PLUS +)', d: 'Multiplying two negative roots (−α)(−β) = +αβ times one x yields +a(αβ + βγ + γα)x, matching +cx cleanly!' },
        s3: { e: 'Full Triple Product: αβγ = −d / a   (Sign: MINUS −)', d: 'Multiplying all three negative constants (−α)(−β)(−γ) = −αβγ gives −a(αβγ) = +d, so αβγ = −d/a!' }
    };
    const d = map[k];
    if (!d) return;
    ['s1', 's2', 's3'].forEach(x => {
        const b = document.getElementById('btn-clw-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('clw-eq').textContent = d.e;
    document.getElementById('clw-desc').textContent = d.d;
}
</script>
"""

# Simulator 15: Verifying Cubic Example
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✅</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Textbook Example 5 Live Cubic Verifier (3x³ − 5x² − 11x − 3)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">a=3, b=−5, c=−11, d=−3</span>
    </div>

    <p class="text-xs text-slate-300">Verify step by step that 3, −1, and −1/3 are all zeroes AND satisfy every single cubic coefficient relation!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="checkCubEx5('eval')" id="btn-ce5-eval" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">Step 1: Verify p(k) = 0</button>
        <button onclick="checkCubEx5('coeff')" id="btn-ce5-coeff" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Step 2: Verify Relations</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs" id="ce5-box">
        <div class="text-cyan-300">• p(3) = 3(27) − 5(9) − 11(3) − 3 = 81 − 45 − 33 − 3 = 0 ✅</div>
        <div class="text-amber-300">• p(−1) = 3(−1) − 5(1) − 11(−1) − 3 = −3 − 5 + 11 − 3 = 0 ✅</div>
        <div class="text-emerald-300">• p(−1/3) = −1/9 − 5/9 + 11/3 − 3 = −6/9 + 33/9 − 27/9 = 0 ✅</div>
    </div>
</div>

<script>
function checkCubEx5(step) {
    ['eval', 'coeff'].forEach(k => {
        const b = document.getElementById('btn-ce5-' + k);
        if (b) {
            b.className = (k === step)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    const box = document.getElementById('ce5-box');
    if (step === 'eval') {
        box.innerHTML = `<div class="text-cyan-300">• p(3) = 3(27) − 5(9) − 11(3) − 3 = 81 − 45 − 33 − 3 = 0 ✅</div>
            <div class="text-amber-300">• p(−1) = 3(−1) − 5(1) − 11(−1) − 3 = −3 − 5 + 11 − 3 = 0 ✅</div>
            <div class="text-emerald-300">• p(−1/3) = −1/9 − 5/9 + 11/3 − 3 = −6/9 + 33/9 − 27/9 = 0 ✅</div>`;
    } else {
        box.innerHTML = `<div class="text-cyan-300">• α + β + γ = 3 − 1 − 1/3 = 5/3  ≡  −b/a = −(−5)/3 = 5/3 ✅</div>
            <div class="text-amber-300">• αβ + βγ + γα = −3 + 1/3 − 1 = −11/3  ≡  c/a = −11/3 ✅</div>
            <div class="text-emerald-300">• αβγ = 3(−1)(−1/3) = +1  ≡  −d/a = −(−3)/3 = +1 ✅</div>`;
    }
}
</script>
"""

# Simulator 16: Chapter Two Summary
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎓</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Chapter 2 Master Reference Sheet (Polynomials)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">All Takeaways</span>
    </div>

    <p class="text-xs text-slate-300">Click each pillar to review every Chapter 2 rule before launching Exercise 2.1, Exercise 2.2, and Challenge Drills!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectCh2Sum('deg')" id="btn-c2s-deg" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Degrees</button>
        <button onclick="inspectCh2Sum('geo')" id="btn-c2s-geo" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Graph Meaning</button>
        <button onclick="inspectCh2Sum('quad')" id="btn-c2s-quad" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Quadratic Rules</button>
        <button onclick="inspectCh2Sum('cub')" id="btn-c2s-cub" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Cubic Rules</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 text-xs">
        <h4 class="font-bold text-cyan-300 text-sm" id="c2s-title">1. Polynomial Degree Classifications</h4>
        <p class="text-slate-300 leading-relaxed" id="c2s-desc">Linear (deg 1, ax+b), Quadratic (deg 2, ax²+bx+c), Cubic (deg 3, ax³+bx²+cx+d), all with a ≠ 0 and whole-number powers on x.</p>
    </div>
</div>

<script>
function inspectCh2Sum(k) {
    const map = {
        deg: { t: '1. Polynomial Degree Classifications', d: 'Linear (deg 1, ax+b), Quadratic (deg 2, ax²+bx+c), Cubic (deg 3, ax³+bx²+cx+d), all with a ≠ 0 and whole-number powers on x.' },
        geo: { t: '2. Graphical Meaning & Zero Bounds', d: 'Zeroes are x-coordinates of x-axis intersections. A polynomial of degree n cuts/touches the x-axis at AT MOST n points (at most n real zeroes).' },
        quad: { t: '3. Quadratic Coefficient Formulas & Builder', d: 'α + β = −b/a and αβ = c/a. Constructing quadratics cleanly from Sum S and Product P: k[x² − Sx + P].' },
        cub: { t: '4. Cubic Coefficient Formulas (α, β, γ)', d: 'α + β + γ = −b/a,  αβ + βγ + γα = +c/a,  αβγ = −d/a (alternating MINUS, PLUS, MINUS signs!).' }
    };
    const d = map[k];
    if (!d) return;
    ['deg', 'geo', 'quad', 'cub'].forEach(x => {
        const b = document.getElementById('btn-c2s-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('c2s-title').textContent = d.t;
    document.getElementById('c2s-desc').textContent = d.d;
}
</script>
"""
