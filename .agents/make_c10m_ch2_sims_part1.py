#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 2: Polynomials
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Polynomial Degree Intro
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Polynomial Degree &amp; Imposter Expression Classifier</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Degree Check</span>
    </div>

    <p class="text-xs text-slate-300">Click each algebraic expression to inspect variable exponents, verify whether it is a genuine polynomial, and classify its degree!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="checkPolyExpr('lin')" id="btn-pe-lin" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">2x − 3</button>
        <button onclick="checkPolyExpr('quad')" id="btn-pe-quad" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">√3x² − 5x + 1</button>
        <button onclick="checkPolyExpr('cub')" id="btn-pe-cub" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">5x³ − x² + 3</button>
        <button onclick="checkPolyExpr('trap')" id="btn-pe-trap" class="p-2 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-rose-700 hover:bg-slate-800">√x + 1/x (Trap!)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex items-center justify-between">
            <h4 class="font-bold text-cyan-300 text-sm" id="pe-title">Genuine Linear Polynomial (Degree = 1)</h4>
            <span class="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-900/70 text-emerald-300 border border-emerald-700" id="pe-badge">POLYNOMIAL ✅</span>
        </div>
        <p class="text-slate-300 leading-relaxed" id="pe-desc">Exponents on x are whole numbers {1, 0}. Highest exponent of x with nonzero coefficient is 1—defining a Linear Polynomial (ax + b, a ≠ 0)!</p>
    </div>
</div>

<script>
function checkPolyExpr(k) {
    const map = {
        lin: { t: 'Genuine Linear Polynomial (Degree = 1)', b: 'POLYNOMIAL ✅', ok: true, d: 'Exponents on x are whole numbers {1, 0}. Highest exponent of x with nonzero coefficient is 1—defining a Linear Polynomial (ax + b, a ≠ 0)!' },
        quad: { t: 'Genuine Quadratic Polynomial (Degree = 2)', b: 'POLYNOMIAL ✅', ok: true, d: 'Careful! Irrational coefficient √3 on x² is totally allowed! Since exponents on x are whole numbers {2, 1, 0}, highest power 2 gives a Quadratic Polynomial!' },
        cub: { t: 'Genuine Cubic Polynomial (Degree = 3)', b: 'POLYNOMIAL ✅', ok: true, d: 'All exponents on x are whole numbers {3, 2, 0}. Highest nonzero power 3 defines a Cubic Polynomial (ax³ + bx² + cx + d, a ≠ 0)!' },
        trap: { t: 'NOT A POLYNOMIAL! (Fractional & Negative Powers)', b: 'IMPOSTER ❌', ok: false, d: '√x equals x^(1/2) and 1/x equals x^(−1). Neither 1/2 nor −1 is a whole number! Any radical or denominator variable disqualifies an expression from being a polynomial.' }
    };
    const d = map[k];
    if (!d) return;
    ['lin', 'quad', 'cub', 'trap'].forEach(x => {
        const b = document.getElementById('btn-pe-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('pe-title').textContent = d.t;
    const bd = document.getElementById('pe-badge');
    bd.textContent = d.b;
    bd.className = d.ok
        ? 'px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-900/70 text-emerald-300 border border-emerald-700'
        : 'px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-rose-900/70 text-rose-300 border border-rose-700';
    document.getElementById('pe-desc').textContent = d.d;
}
</script>
"""

# Simulator 2: Value And Zeroes
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎯</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Polynomial Evaluator p(k) &amp; Zero Detector</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">p(x) = x² − 3x − 4</span>
    </div>

    <p class="text-xs text-slate-300">Plug different real numbers k into p(x) = x² − 3x − 4 to compute output values p(k) and hunt down exact zeroes where p(k) = 0!</p>

    <div class="grid grid-cols-4 gap-2">
        <button onclick="evalPolyAt(-1)" id="btn-ev--1" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">k = −1</button>
        <button onclick="evalPolyAt(0)" id="btn-ev-0" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">k = 0</button>
        <button onclick="evalPolyAt(2)" id="btn-ev-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">k = 2</button>
        <button onclick="evalPolyAt(4)" id="btn-ev-4" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">k = 4</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300 font-bold" id="ev-sub">p(−1) = (−1)² − 3(−1) − 4 = 1 + 3 − 4 = 0</div>
        <div class="font-sans text-emerald-400 font-bold" id="ev-res">✅ ZERO FOUND! Because p(−1) = 0, x = −1 is a ZERO of p(x)!</div>
        <div class="pt-2 border-t border-slate-800 font-sans text-slate-400">Linear Shortcut: For any p(x) = ax + b (a ≠ 0), unique zero is always k = −b / a.</div>
    </div>
</div>

<script>
function evalPolyAt(k) {
    const val = k * k - 3 * k - 4;
    [-1, 0, 2, 4].forEach(x => {
        const b = document.getElementById('btn-ev-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    const ks = k < 0 ? `(${k})` : `${k}`;
    document.getElementById('ev-sub').textContent = `p(${k}) = ${ks}² − 3${ks} − 4 = ${k*k} − (${3*k}) − 4 = ${val}`;
    const r = document.getElementById('ev-res');
    if (val === 0) {
        r.className = 'font-sans text-emerald-400 font-bold';
        r.textContent = `✅ ZERO FOUND! Because p(${k}) = 0, x = ${k} is a ZERO of p(x)!`;
    } else {
        r.className = 'font-sans text-amber-300 font-bold';
        r.textContent = `Value p(${k}) = ${val} ≠ 0, so ${k} is NOT a zero of p(x).`;
    }
}
</script>
"""

# Simulator 3: Linear Graph Zeroes
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📏</span>
            <h3 class="text-sm sm:text-base font-bold text-sky-300">Linear Straight-Line Graph &amp; x-Intercept Plotter</h3>
        </div>
        <span class="text-[11px] bg-sky-950/80 text-sky-300 px-2.5 py-1 rounded-full border border-sky-800">y = ax + b</span>
    </div>

    <p class="text-xs text-slate-300">Switch linear equations below to see each straight line cross the horizontal x-axis at exact zero (−b/a, 0)!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="plotLinearLine('l1')" id="btn-ln-l1" class="p-2 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500">y = 2x + 3</button>
        <button onclick="plotLinearLine('l2')" id="btn-ln-l2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">y = 2x − 4</button>
        <button onclick="plotLinearLine('l3')" id="btn-ln-l3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">y = −x + 2</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 170" class="w-full h-auto max-h-[170px] rounded-xl bg-slate-950 border border-slate-800">
            <!-- Axes (origin at 110, 85; 20px = 1 unit) -->
            <line x1="10" y1="85" x2="210" y2="85" stroke="#64748b" stroke-width="1.5" />
            <line x1="110" y1="10" x2="110" y2="160" stroke="#64748b" stroke-width="1.5" />
            <text x="202" y="80" fill="#94a3b8" font-size="9">x</text>
            <text x="115" y="18" fill="#94a3b8" font-size="9">y</text>
            <!-- Line -->
            <line id="ln-svg-line" x1="50" y1="145" x2="150" y2="-55" stroke="#38bdf8" stroke-width="3" />
            <!-- Zero Crossing Dot -->
            <circle id="ln-svg-dot" cx="80" cy="85" r="5" fill="#fde047" stroke="#0f172a" stroke-width="1.5" />
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <div class="font-mono font-bold text-amber-300" id="ln-zero">x-Intercept (Zero): (−3/2, 0) = (−1.5, 0)</div>
            <p class="text-slate-300 leading-relaxed" id="ln-desc">Straight line y = 2x + 3 slices upward through y-intercept (0, 3) and hits the horizontal x-axis at ONE unique spot: (−3/2, 0), matching k = −b/a cleanly!</p>
        </div>
    </div>
</div>

<script>
function plotLinearLine(k) {
    // origin (110, 85), scale = 20px per unit: sx = 110 + 20*x, sy = 85 - 20*y
    const map = {
        l1: { x1: 30, y1: 185, x2: 140, y2: -35, dx: 80, z: 'x-Intercept (Zero): (−3/2, 0) = (−1.5, 0)', d: 'Straight line y = 2x + 3 slices upward through y-intercept (0, 3) and hits the horizontal x-axis at ONE unique spot: (−3/2, 0), matching k = −b/a cleanly!' },
        l2: { x1: 80, y1: 225, x2: 200, y2: -15, dx: 150, z: 'x-Intercept (Zero): (2, 0)', d: 'Line y = 2x − 4 crosses y = 0 strictly at x = −(−4)/2 = +2, intersecting the horizontal x-axis at (2, 0)!' },
        l3: { x1: 30, y1: -35, x2: 210, y2: 145, dx: 150, z: 'x-Intercept (Zero): (2, 0)', d: 'Negative-slope line y = −x + 2 drops downward left-to-right, still crossing the x-axis at exactly ONE point (2, 0)!' }
    };
    const d = map[k];
    if (!d) return;
    ['l1', 'l2', 'l3'].forEach(x => {
        const b = document.getElementById('btn-ln-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-sky-600 text-white font-bold text-xs border border-sky-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    const l = document.getElementById('ln-svg-line');
    l.setAttribute('x1', d.x1); l.setAttribute('y1', d.y1);
    l.setAttribute('x2', d.x2); l.setAttribute('y2', d.y2);
    document.getElementById('ln-svg-dot').setAttribute('cx', d.dx);
    document.getElementById('ln-zero').textContent = d.z;
    document.getElementById('ln-desc').textContent = d.d;
}
</script>
"""

# Simulator 4: Up Down Parabolas
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌈</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Parabola Direction Flipper: a &gt; 0 (Up) vs. a &lt; 0 (Down)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">U-Shape Curve</span>
    </div>

    <p class="text-xs text-slate-300">Toggle leading coefficient sign between positive a &gt; 0 and negative a &lt; 0 to flip the parabola opening cleanly!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="flipParabola('up')" id="btn-ud-up" class="p-2.5 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">∪ Upward (a = +1 &gt; 0)</button>
        <button onclick="flipParabola('down')" id="btn-ud-down" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">∩ Downward (a = −1 &lt; 0)</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 170" class="w-full h-auto max-h-[170px] rounded-xl bg-slate-950 border border-slate-800">
            <line x1="10" y1="85" x2="210" y2="85" stroke="#64748b" stroke-width="1.5" />
            <line x1="110" y1="10" x2="110" y2="160" stroke="#64748b" stroke-width="1.5" />
            <path id="ud-parab-up" d="M50,20 Q110,195 170,20" fill="none" stroke="#22c55e" stroke-width="3.5" />
            <path id="ud-parab-down" d="M50,150 Q110,-25 170,150" fill="none" stroke="#f97316" stroke-width="3.5" class="hidden" />
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-purple-300 text-sm" id="ud-title">y = x² − 2 (a = +1 &gt; 0: Opens Upwards ∪)</h4>
            <p class="text-slate-300 leading-relaxed" id="ud-desc">Positive leading coefficient a &gt; 0 makes +x² grow large upwards on both sides, creating a smiling valley opening upward forever!</p>
        </div>
    </div>
</div>

<script>
function flipParabola(dir) {
    const up = document.getElementById('ud-parab-up');
    const dn = document.getElementById('ud-parab-down');
    if (dir === 'up') { up.classList.remove('hidden'); dn.classList.add('hidden'); }
    else { up.classList.add('hidden'); dn.classList.remove('hidden'); }
    ['up', 'down'].forEach(k => {
        const b = document.getElementById('btn-ud-' + k);
        if (b) {
            b.className = (k === dir)
                ? 'p-2.5 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('ud-title').textContent = (dir === 'up')
        ? 'y = x² − 2 (a = +1 > 0: Opens Upwards ∪)'
        : 'y = −x² + 2 (a = −1 < 0: Opens Downwards ∩)';
    document.getElementById('ud-desc').textContent = (dir === 'up')
        ? 'Positive leading coefficient a > 0 makes +x² grow large upwards on both sides, creating a smiling valley opening upward forever!'
        : 'Negative leading coefficient a < 0 flips the curve upside down, curving both wings sharply downwards like a rainbow bridge!';
}
</script>
"""

# Simulator 5: Two Zero Parabolas
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✌️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Case 1 Viewer: Two Distinct Real x-Intercepts</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">2 Zeroes</span>
    </div>

    <p class="text-xs text-slate-300">Inspect both upward and downward Case 1 parabolas slashing cleanly through the horizontal x-axis at two distinct points A and A'!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="setCase1('u')" id="btn-c1-u" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">y = x² − 3x − 4</button>
        <button onclick="setCase1('d')" id="btn-c1-d" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">y = −x² + 4</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 170" class="w-full h-auto max-h-[170px] rounded-xl bg-slate-950 border border-slate-800">
            <line x1="10" y1="85" x2="210" y2="85" stroke="#64748b" stroke-width="1.5" />
            <line x1="90" y1="10" x2="90" y2="160" stroke="#64748b" stroke-width="1.5" />
            <g id="c1-u-svg">
                <path d="M55,15 Q115,215 175,15" fill="none" stroke="#22c55e" stroke-width="3" />
                <circle cx="72" cy="85" r="5" fill="#fde047" /><circle cx="158" cy="85" r="5" fill="#fde047" />
                <text x="62" y="75" fill="#fde047" font-size="9" font-weight="bold">A(-1,0)</text>
                <text x="155" y="75" fill="#fde047" font-size="9" font-weight="bold">A'(4,0)</text>
            </g>
            <g id="c1-d-svg" class="hidden">
                <path d="M35,160 Q90,-25 145,160" fill="none" stroke="#f97316" stroke-width="3" />
                <circle cx="55" cy="85" r="5" fill="#fde047" /><circle cx="125" cy="85" r="5" fill="#fde047" />
                <text x="34" y="75" fill="#fde047" font-size="9" font-weight="bold">A(-2,0)</text>
                <text x="122" y="75" fill="#fde047" font-size="9" font-weight="bold">A'(2,0)</text>
            </g>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-emerald-300 text-sm" id="c1-title">y = x² − 3x − 4 -> Zeroes: −1 and 4</h4>
            <p class="text-slate-300 leading-relaxed" id="c1-desc">Opening upwards (a = +1 &gt; 0) with vertex dipping below y = 0, the parabola cuts the horizontal x-axis cleanly twice at A(−1, 0) and A'(4, 0)!</p>
        </div>
    </div>
</div>

<script>
function setCase1(m) {
    document.getElementById('c1-u-svg').classList.toggle('hidden', m !== 'u');
    document.getElementById('c1-d-svg').classList.toggle('hidden', m !== 'd');
    ['u', 'd'].forEach(k => {
        const b = document.getElementById('btn-c1-' + k);
        if (b) {
            b.className = (k === m)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('c1-title').textContent = (m === 'u') ? "y = x² − 3x − 4 -> Zeroes: −1 and 4" : "y = −x² + 4 -> Zeroes: −2 and 2";
    document.getElementById('c1-desc').textContent = (m === 'u')
        ? "Opening upwards (a = +1 > 0) with vertex dipping below y = 0, the parabola cuts the horizontal x-axis cleanly twice at A(−1, 0) and A'(4, 0)!"
        : "Opening downwards (a = −1 < 0) with peak crest rising above y = 0 at (0, 4), the arch intersects twice at A(−2, 0) and A'(2, 0)!";
}
</script>
"""

# Simulator 6: Touch Zero Parabolas
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">☝️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Case 2 Viewer: Parabola Touching x-Axis at 1 Coincident Point</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">1 Zero Only</span>
    </div>

    <p class="text-xs text-slate-300">Inspect perfect-square parabolas where vertex sits strictly ON the x-axis—merging both zeroes cleanly into ONE tangent point!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="setCase2('up')" id="btn-c2-up" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">y = (x − 2)²</button>
        <button onclick="setCase2('dn')" id="btn-c2-dn" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">y = −(x + 1)²</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 170" class="w-full h-auto max-h-[170px] rounded-xl bg-slate-950 border border-slate-800">
            <line x1="10" y1="105" x2="210" y2="105" stroke="#64748b" stroke-width="1.5" />
            <line x1="100" y1="10" x2="100" y2="160" stroke="#64748b" stroke-width="1.5" />
            <g id="c2-up-svg">
                <path d="M85,15 Q140,195 195,15" fill="none" stroke="#facc15" stroke-width="3" />
                <circle cx="140" cy="105" r="5" fill="#ef4444" stroke="#fff" stroke-width="1.5" />
                <text x="140" y="122" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">Touches at (2, 0)</text>
            </g>
            <g id="c2-dn-svg" class="hidden">
                <path d="M25,165 Q80,45 135,165" fill="none" stroke="#f97316" stroke-width="3" />
                <circle cx="80" cy="105" r="5" fill="#fde047" stroke="#fff" stroke-width="1.5" />
                <text x="80" y="96" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">Touches at (-1, 0)</text>
            </g>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-amber-300 text-sm" id="c2-title">y = x² − 4x + 4 = (x − 2)² -> 1 Zero (x = 2)</h4>
            <p class="text-slate-300 leading-relaxed" id="c2-desc">The vertex settles right onto y = 0 at x = 2 without ever dropping below! Two equal roots coalesce geometrically into a single touching point (2, 0).</p>
        </div>
    </div>
</div>

<script>
function setCase2(m) {
    document.getElementById('c2-up-svg').classList.toggle('hidden', m !== 'up');
    document.getElementById('c2-dn-svg').classList.toggle('hidden', m !== 'dn');
    ['up', 'dn'].forEach(k => {
        const b = document.getElementById('btn-c2-' + k);
        if (b) {
            b.className = (k === m)
                ? 'p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('c2-title').textContent = (m === 'up') ? 'y = x² − 4x + 4 = (x − 2)² -> 1 Zero (x = 2)' : 'y = −(x + 1)² -> 1 Zero (x = −1)';
    document.getElementById('c2-desc').textContent = (m === 'up')
        ? 'The vertex settles right onto y = 0 at x = 2 without ever dropping below! Two equal roots coalesce geometrically into a single touching point (2, 0).'
        : 'Peak crest rises just up to ( −1, 0 ) from below without crossing above the x-axis—again yielding exactly ONE tangent contact point!';
}
</script>
"""

# Simulator 7: No Zero Parabolas
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🚫</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Case 3 Viewer: Floating Parabolas With Zero Real Zeroes</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">0 Zeroes</span>
    </div>

    <p class="text-xs text-slate-300">Inspect parabolas floating wholly above or wholly below the horizontal x-axis—never crossing y = 0 anywhere!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="setCase3('above')" id="btn-c3-above" class="p-2 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">y = x² + 1 (Above)</button>
        <button onclick="setCase3('below')" id="btn-c3-below" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">y = −x² − 2 (Below)</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 170" class="w-full h-auto max-h-[170px] rounded-xl bg-slate-950 border border-slate-800">
            <line x1="10" y1="85" x2="210" y2="85" stroke="#94a3b8" stroke-width="1.5" />
            <line x1="110" y1="10" x2="110" y2="160" stroke="#64748b" stroke-width="1.5" />
            <g id="c3-above-svg">
                <path d="M55,10 Q110,125 165,10" fill="none" stroke="#38bdf8" stroke-width="3" />
                <text x="110" y="108" fill="#f87171" font-size="9" font-weight="bold" text-anchor="middle">NEVER REACHES x-AXIS (y ≥ 1)!</text>
            </g>
            <g id="c3-below-svg" class="hidden">
                <path d="M55,160 Q110,55 165,160" fill="none" stroke="#f97316" stroke-width="3" />
                <text x="110" y="65" fill="#f87171" font-size="9" font-weight="bold" text-anchor="middle">NEVER REACHES x-AXIS (y ≤ −2)!</text>
            </g>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-rose-300 text-sm" id="c3-title">y = x² + 1 -> 0 Real Zeroes</h4>
            <p class="text-slate-300 leading-relaxed" id="c3-desc">Since x² ≥ 0 for every real number x, y = x² + 1 stays ≥ 1 strictly above the x-axis forever—cutting the x-axis zero times!</p>
        </div>
    </div>
</div>

<script>
function setCase3(m) {
    document.getElementById('c3-above-svg').classList.toggle('hidden', m !== 'above');
    document.getElementById('c3-below-svg').classList.toggle('hidden', m !== 'below');
    ['above', 'below'].forEach(k => {
        const b = document.getElementById('btn-c3-' + k);
        if (b) {
            b.className = (k === m)
                ? 'p-2 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('c3-title').textContent = (m === 'above') ? 'y = x² + 1 -> 0 Real Zeroes' : 'y = −x² − 2 -> 0 Real Zeroes';
    document.getElementById('c3-desc').textContent = (m === 'above')
        ? 'Since x² ≥ 0 for every real number x, y = x² + 1 stays ≥ 1 strictly above the x-axis forever—cutting the x-axis zero times!'
        : 'Since −x² ≤ 0 everywhere, y = −x² − 2 stays strictly ≤ −2 below the x-axis forever—never hitting y = 0!';
}
</script>
"""

# Simulator 8: Cubic Curve Graphs
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">〰️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Cubic Polynomial Curves Explorer (1, 2, or 3 Zeroes)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Degree 3 Curves</span>
    </div>

    <p class="text-xs text-slate-300">Switch between all three classic NCERT textbook cubic equations to count their x-axis intersections live!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="showCubic('c3')" id="btn-cub-c3" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">y = x³ − 4x (3)</button>
        <button onclick="showCubic('c1')" id="btn-cub-c1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">y = x³ (1)</button>
        <button onclick="showCubic('c2')" id="btn-cub-c2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">y = x³ − x² (2)</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 170" class="w-full h-auto max-h-[170px] rounded-xl bg-slate-950 border border-slate-800">
            <line x1="10" y1="85" x2="210" y2="85" stroke="#64748b" stroke-width="1.5" />
            <line x1="110" y1="10" x2="110" y2="160" stroke="#64748b" stroke-width="1.5" />
            <g id="cub-c3-svg">
                <path d="M35,165 C55,20 85,20 110,85 C135,150 165,150 185,5" fill="none" stroke="#22c55e" stroke-width="3" />
                <circle cx="52" cy="85" r="4.5" fill="#fde047" /><circle cx="110" cy="85" r="4.5" fill="#fde047" /><circle cx="168" cy="85" r="4.5" fill="#fde047" />
            </g>
            <g id="cub-c1-svg" class="hidden">
                <path d="M55,160 C80,85 140,85 165,10" fill="none" stroke="#38bdf8" stroke-width="3" />
                <circle cx="110" cy="85" r="5" fill="#fde047" />
            </g>
            <g id="cub-c2-svg" class="hidden">
                <path d="M55,160 C80,85 100,85 110,85 C120,85 135,115 155,85 C165,65 175,30 185,10" fill="none" stroke="#a855f7" stroke-width="3" />
                <circle cx="110" cy="85" r="4.5" fill="#fde047" /><circle cx="155" cy="85" r="4.5" fill="#fde047" />
            </g>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-cyan-300 text-sm" id="cub-title">y = x³ − 4x -> 3 Distinct Zeroes (−2, 0, 2)</h4>
            <p class="text-slate-300 leading-relaxed" id="cub-desc">Factoring x(x−2)(x+2) shows the S-curve crossing the x-axis three times at (−2,0), (0,0), and (2,0)—maximum 3 zeroes for cubic degree 3!</p>
        </div>
    </div>
</div>

<script>
function showCubic(c) {
    ['c3', 'c1', 'c2'].forEach(k => {
        const b = document.getElementById('btn-cub-' + k);
        if (b) {
            b.className = (k === c)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        document.getElementById('cub-' + k + '-svg').classList.toggle('hidden', k !== c);
    });
    const map = {
        c3: { t: 'y = x³ − 4x -> 3 Distinct Zeroes (−2, 0, 2)', d: 'Factoring x(x−2)(x+2) shows the S-curve crossing the x-axis three times at (−2,0), (0,0), and (2,0)—maximum 3 zeroes for cubic degree 3!' },
        c1: { t: 'y = x³ -> 1 Distinct Zero (0)', d: 'Inflecting gently right through the origin (0, 0), y = x³ touches the x-axis ONLY once—giving exactly 1 real zero!' },
        c2: { t: 'y = x³ − x² = x²(x − 1) -> 2 Distinct Zeroes (0, 1)', d: 'Grazing tangent at origin (0, 0) then slicing upwards through (1, 0), the curve reveals 2 distinct real zeroes!' }
    };
    document.getElementById('cub-title').textContent = map[c].t;
    document.getElementById('cub-desc').textContent = map[c].d;
}
</script>
"""
