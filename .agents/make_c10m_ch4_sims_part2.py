#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 4: Quadratic Equations
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Triangle And Pottery
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Exercise 4.2 Applied Solver: Right Triangle &amp; Pottery Workshop</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Ex 4.2 Q5 &amp; Q6</span>
    </div>

    <p class="text-xs text-slate-300">Explore how factoring solves geometric right-triangle lengths and daily cottage pottery unit pricing—rejecting invalid negative roots!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="showEx42App('tri')" id="btn-e42-tri" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">Right Triangle (5, 12, 13)</button>
        <button onclick="showEx42App('pot')" id="btn-e42-pot" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Pottery Workshop (₹90)</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 155" class="w-full h-auto max-h-[155px] rounded-xl bg-slate-950 border border-slate-800">
            <g id="e42-tri-svg">
                <polygon points="45,125 180,125 45,45" fill="#064e3b" stroke="#34d399" stroke-width="2.5" />
                <rect x="45" y="113" width="12" height="12" fill="none" stroke="#fde047" stroke-width="1.5" />
                <text x="115" y="142" fill="#7dd3fc" font-size="10" font-weight="bold" text-anchor="middle">Base x = 12 cm</text>
                <text x="32" y="88" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle" transform="rotate(-90 32 88)">Alt = 5 cm</text>
                <text x="128" y="75" fill="#fde047" font-size="10" font-weight="bold">Hyp = 13 cm</text>
            </g>
            <g id="e42-pot-svg" class="hidden">
                <ellipse cx="110" cy="115" rx="45" ry="20" fill="#b45309" />
                <ellipse cx="110" cy="80" rx="35" ry="24" fill="#d97706" />
                <text x="110" y="84" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">6 Pots × ₹15 = ₹90</text>
            </g>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 text-xs font-mono">
            <div class="text-cyan-300" id="e42-eq">x² + (x − 7)² = 13²  ⟹  x² − 7x − 60 = 0</div>
            <div class="text-amber-300" id="e42-fac">Factor: (x − 12)(x + 5) = 0  ⟹  x = 12 or −5</div>
            <div class="font-sans text-emerald-300 font-bold" id="e42-ans">Reject x = −5 (length &gt; 0): Base = 12 cm, Altitude = 5 cm!</div>
        </div>
    </div>
</div>

<script>
function showEx42App(k) {
    document.getElementById('e42-tri-svg').classList.toggle('hidden', k !== 'tri');
    document.getElementById('e42-pot-svg').classList.toggle('hidden', k !== 'pot');
    ['tri', 'pot'].forEach(x => {
        const b = document.getElementById('btn-e42-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    const map = {
        tri: { e: 'x² + (x − 7)² = 13²  ⟹  x² − 7x − 60 = 0', f: 'Factor: (x − 12)(x + 5) = 0  ⟹  x = 12 or −5', a: 'Reject x = −5 (length > 0): Base = 12 cm, Altitude = 5 cm!' },
        pot: { e: 'x(2x + 3) = 90  ⟹  2x² + 3x − 90 = 0', f: 'Factor: (2x + 15)(x − 6) = 0  ⟹  x = 6 or −15/2', a: 'Reject −15/2 (articles > 0): 6 pottery articles at ₹15 each!' }
    };
    document.getElementById('e42-eq').textContent = map[k].e;
    document.getElementById('e42-fac').textContent = map[k].f;
    document.getElementById('e42-ans').textContent = map[k].a;
}
</script>
"""

# Simulator 10: Sridharacharya Quadratic Formula
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🗝️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Sridharacharya's Universal Quadratic Formula Engine</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">x = (−b ± √D)/(2a)</span>
    </div>

    <p class="text-xs text-slate-300">Solve both rational and non-factorable irrational equations step by step using Sridharacharya's universal formula!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="runQuadFormula('q1')" id="btn-qf-q1" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">2x² − 7x + 3 = 0</button>
        <button onclick="runQuadFormula('q2')" id="btn-qf-q2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">x² − 4x + 1 = 0</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs">
        <div class="text-cyan-300" id="qf-abc">Coefficients: a = 2,  b = −7,  c = 3   |   D = (−7)² − 4(2)(3) = 49 − 24 = 25</div>
        <div class="text-amber-300 font-bold" id="qf-sub">x = [ −(−7) ± √25 ] / (2 × 2) = (7 ± 5) / 4</div>
        <div class="text-emerald-300 font-bold" id="qf-res">Roots: (7 + 5)/4 = 3   and   (7 − 5)/4 = 1/2 ✅</div>
    </div>
</div>

<script>
function runQuadFormula(k) {
    const map = {
        q1: { a: 'Coefficients: a = 2,  b = −7,  c = 3   |   D = (−7)² − 4(2)(3) = 49 − 24 = 25', s: 'x = [ −(−7) ± √25 ] / (2 × 2) = (7 ± 5) / 4', r: 'Roots: (7 + 5)/4 = 3   and   (7 − 5)/4 = 1/2 ✅' },
        q2: { a: 'Coefficients: a = 1,  b = −4,  c = 1   |   D = (−4)² − 4(1)(1) = 16 − 4 = 12', s: 'x = [ 4 ± √12 ] / 2 = (4 ± 2√3) / 2', r: 'Roots: 2 + √3   and   2 − √3 ✅ (irrational conjugates!)' }
    };
    const d = map[k];
    if (!d) return;
    ['q1', 'q2'].forEach(x => {
        const b = document.getElementById('btn-qf-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('qf-abc').textContent = d.a;
    document.getElementById('qf-sub').textContent = d.s;
    document.getElementById('qf-res').textContent = d.r;
}
</script>
"""

# Simulator 11: Discriminant D Value
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎛️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Discriminant D = b² − 4ac Root Sign Analyzer</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Inside √D</span>
    </div>

    <p class="text-xs text-slate-300">Evaluate D = b² − 4ac on three equations to see how positive, zero, and negative values behave under the square root sign!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="evalDiscD('d1')" id="btn-dd-d1" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">2x² − 4x + 3 = 0</button>
        <button onclick="evalDiscD('d2')" id="btn-dd-d2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3x² − 2x + 1/3 = 0</button>
        <button onclick="evalDiscD('d3')" id="btn-dd-d3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2x² − 5x + 3 = 0</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs">
        <div class="text-amber-300 font-bold" id="dd-calc">D = (−4)² − 4(2)(3) = 16 − 24 = −8  (&lt; 0)</div>
        <div class="text-rose-300 font-bold font-sans" id="dd-ver">❌ No Real Roots! Because no real number squared equals −8, √(−8) is not real.</div>
    </div>
</div>

<script>
function evalDiscD(k) {
    const map = {
        d1: { c: 'D = (−4)² − 4(2)(3) = 16 − 24 = −8  (< 0)', v: '❌ No Real Roots! Because no real number squared equals −8, √(−8) is not real.', cls: 'text-rose-300 font-bold font-sans' },
        d2: { c: 'D = (−2)² − 4(3)(1/3) = 4 − 4 = 0  (= 0)', v: '🎯 Two EQUAL Real Roots! √0 = 0 collapses both branches to −b/(2a) = 1/3 twice.', cls: 'text-amber-300 font-bold font-sans' },
        d3: { c: 'D = (−5)² − 4(2)(3) = 25 − 24 = +1  (> 0)', v: '✅ Two DISTINCT Real Roots! √1 = 1 creates two unique roots: 3/2 and 1.', cls: 'text-emerald-300 font-bold font-sans' }
    };
    const d = map[k];
    if (!d) return;
    ['d1', 'd2', 'd3'].forEach(x => {
        const b = document.getElementById('btn-dd-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('dd-calc').textContent = d.c;
    const vv = document.getElementById('dd-ver');
    vv.textContent = d.v;
    vv.className = d.cls;
}
</script>
"""

# Simulator 12: Three Root Cases
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌗</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Discriminant &amp; Parabola 3-Case Matcher (D &gt; 0, D = 0, D &lt; 0)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">Algebra + Geometry</span>
    </div>

    <p class="text-xs text-slate-300">Watch how D &gt; 0, D = 0, and D &lt; 0 correspond directly to cutting twice, grazing tangent once, or floating above the x-axis!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="show3Cases('gt')" id="btn-3c-gt" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">D &gt; 0 (2 Roots)</button>
        <button onclick="show3Cases('eq')" id="btn-3c-eq" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">D = 0 (Equal)</button>
        <button onclick="show3Cases('lt')" id="btn-3c-lt" class="p-2 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-rose-700 hover:bg-slate-800">D &lt; 0 (0 Real)</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 140" class="w-full h-auto max-h-[140px] rounded-xl bg-slate-950 border border-slate-800">
            <line x1="15" y1="88" x2="205" y2="88" stroke="#64748b" stroke-width="1.5" />
            <g id="3c-gt-svg"><path d="M55,15 Q110,165 165,15" fill="none" stroke="#22c55e" stroke-width="3" /><circle cx="77" cy="88" r="4.5" fill="#fde047" /><circle cx="143" cy="88" r="4.5" fill="#fde047" /></g>
            <g id="3c-eq-svg" class="hidden"><path d="M55,15 Q110,161 165,15" fill="none" stroke="#facc15" stroke-width="3" /><circle cx="110" cy="88" r="5" fill="#ef4444" /></g>
            <g id="3c-lt-svg" class="hidden"><path d="M55,15 Q110,115 165,15" fill="none" stroke="#f87171" stroke-width="3" /></g>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 text-xs">
            <h4 class="font-bold text-purple-300 text-sm" id="3c-title">D = b² − 4ac &gt; 0 -> Two Distinct Real Roots</h4>
            <p class="text-slate-300 leading-relaxed" id="3c-desc">Parabola dips across y = 0 twice cleanly! Roots equal (−b + √D)/(2a) and (−b − √D)/(2a).</p>
        </div>
    </div>
</div>

<script>
function show3Cases(k) {
    ['gt', 'eq', 'lt'].forEach(x => {
        const b = document.getElementById('btn-3c-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
        document.getElementById('3c-' + x + '-svg').classList.toggle('hidden', x !== k);
    });
    const map = {
        gt: { t: 'D = b² − 4ac > 0 -> Two Distinct Real Roots', d: 'Parabola dips across y = 0 twice cleanly! Roots equal (−b + √D)/(2a) and (−b − √D)/(2a).' },
        eq: { t: 'D = b² − 4ac = 0 -> Two Equal Real Roots', d: 'Vertex kisses x-axis tangent at one point! Roots coalesce into −b/(2a) twice (e.g., 3x² − 4√3x + 4 = 0).' },
        lt: { t: 'D = b² − 4ac < 0 -> No Real Roots', d: 'Parabola floats strictly above (or below) the x-axis forever—zero real solutions exist!' }
    };
    document.getElementById('3c-title').textContent = map[k].t;
    document.getElementById('3c-desc').textContent = map[k].d;
}
</script>
"""

# Simulator 13: Circular Boundary Pole
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⭕</span>
            <h3 class="text-sm sm:text-base font-bold text-sky-300">Circular Park Pole Geometry Simulator (Example 8)</h3>
        </div>
        <span class="text-[11px] bg-sky-950/80 text-sky-300 px-2.5 py-1 rounded-full border border-sky-800">∠APB = 90° Semicircle</span>
    </div>

    <p class="text-xs text-slate-300">Verify circular pole placement on diameter AB = 13 m when |PA − PB| = 7 m using D = b² − 4ac &amp; Pythagoras!</p>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 160" class="w-full h-auto max-h-[160px] rounded-xl bg-slate-950 border border-slate-800">
            <circle cx="110" cy="80" r="62" fill="#0f172a" stroke="#38bdf8" stroke-width="2" />
            <line x1="48" y1="80" x2="172" y2="80" stroke="#94a3b8" stroke-width="2" />
            <!-- Pole P at top-right forming right angle 5-12-13 -->
            <polygon points="48,80 172,80 154,36" fill="none" stroke="#22c55e" stroke-width="2.5" />
            <circle cx="154" cy="36" r="5" fill="#fde047" />
            <text x="38" y="84" fill="#cbd5e1" font-size="10" font-weight="bold">A</text>
            <text x="178" y="84" fill="#cbd5e1" font-size="10" font-weight="bold">B</text>
            <text x="160" y="30" fill="#fde047" font-size="10" font-weight="bold">Pole P (90°)</text>
            <text x="110" y="95" fill="#94a3b8" font-size="9" text-anchor="middle">Diameter AB = 13 m</text>
            <text x="95" y="52" fill="#7dd3fc" font-size="9" font-weight="bold">PA = 12m</text>
            <text x="176" y="56" fill="#86efac" font-size="9" font-weight="bold">PB = 5m</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs">
            <div class="text-cyan-300">Semicircle Theorem ⟹ ∠APB = 90°</div>
            <div class="text-amber-300">x² + (x + 7)² = 13²  ⟹  x² + 7x − 60 = 0</div>
            <div class="text-emerald-300 font-bold">D = 49 + 240 = 289 &gt; 0  ⟹  PB = 5 m, PA = 12 m ✅</div>
        </div>
    </div>
</div>
"""

# Simulator 14: Finding Constant k
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔎</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Exercise 4.3 Q2 Solver: Finding Constant k for Equal Roots</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">D = 0 Traps!</span>
    </div>

    <p class="text-xs text-slate-300">Inspect both Exercise 4.3 Q2 problems carefully—especially rejecting k = 0 when k sits on leading x²!</p>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="findConstK('k1')" id="btn-fk-k1" class="p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">2x² + kx + 3 = 0</button>
        <button onclick="findConstK('k2')" id="btn-fk-k2" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">kx(x − 2) + 6 = 0 (Trap!)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs">
        <div class="text-cyan-300" id="fk-eq">Equal Roots ⟹ D = k² − 4(2)(3) = 0  ⟹  k² = 24</div>
        <div class="text-emerald-300 font-bold" id="fk-ans">Result: k = +2√6  and  k = −2√6  (both valid since a = 2 ≠ 0 ✅)</div>
    </div>
</div>

<script>
function findConstK(k) {
    const map = {
        k1: { e: 'Equal Roots ⟹ D = k² − 4(2)(3) = 0  ⟹  k² = 24', a: 'Result: k = +2√6  and  k = −2√6  (both valid since a = 2 ≠ 0 ✅)' },
        k2: { e: 'Expand: kx² − 2kx + 6 = 0  |  D = 4k² − 24k = 4k(k − 6) = 0  ⟹  k = 0 or 6', a: '⚠️ Reject k = 0 (makes 0x² + 6 = 0, invalid!)  ⟹  ONLY k = 6 works ✅!' }
    };
    const d = map[k];
    if (!d) return;
    ['k1', 'k2'].forEach(x => {
        const b = document.getElementById('btn-fk-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('fk-eq').textContent = d.e;
    document.getElementById('fk-ans').textContent = d.a;
}
</script>
"""

# Simulator 15: Geometric Design Feasibility
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📋</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Exercise 4.3 Feasibility Checker (Possible vs. Impossible Designs)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Ex 4.3 Q3–Q5</span>
    </div>

    <p class="text-xs text-slate-300">Click each proposed design or riddle from Exercise 4.3 to let Discriminant D decide whether real dimensions exist!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="checkFeas('grove')" id="btn-fs-grove" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">Mango Grove 800m²</button>
        <button onclick="checkFeas('ages')" id="btn-fs-ages" class="p-2 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-rose-700 hover:bg-slate-800">Friends Ages (D&lt;0)</button>
        <button onclick="checkFeas('park')" id="btn-fs-park" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Park P=80, A=400</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 font-mono text-xs">
        <div class="text-cyan-300" id="fs-eq">Length = 2b  ⟹  2b² = 800  ⟹  b² − 400 = 0</div>
        <div class="font-sans text-emerald-300 font-bold" id="fs-ver">✅ POSSIBLE! D &gt; 0 yields breadth = 20 m and length = 40 m!</div>
    </div>
</div>

<script>
function checkFeas(k) {
    const map = {
        grove: { e: 'Length = 2b  ⟹  2b² = 800  ⟹  b² − 400 = 0', v: '✅ POSSIBLE! D > 0 yields breadth = 20 m and length = 40 m!', ok: true },
        ages: { e: 'Four yrs ago: (x − 4)(16 − x) = 48  ⟹  x² − 20x + 112 = 0  |  D = 400 − 448 = −48', v: '❌ IMPOSSIBLE! Since D = −48 < 0, NO real friends satisfy those ages!', ok: false },
        park: { e: 'Half-perimeter = 40: x(40 − x) = 400  ⟹  x² − 40x + 400 = 0  |  D = 1600 − 1600 = 0', v: '✅ POSSIBLE! D = 0 gives a valid 20 m × 20 m square rectangle!', ok: true }
    };
    const d = map[k];
    if (!d) return;
    ['grove', 'ages', 'park'].forEach(x => {
        const b = document.getElementById('btn-fs-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('fs-eq').textContent = d.e;
    const vv = document.getElementById('fs-ver');
    vv.textContent = d.v;
    vv.className = d.ok ? 'font-sans text-emerald-300 font-bold' : 'font-sans text-rose-300 font-bold';
}
</script>
"""

# Simulator 16: Chapter Four Summary
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎓</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Chapter 4 Master Formula &amp; Nature of Roots Hub</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Revision Sheet</span>
    </div>

    <p class="text-xs text-slate-300">Review every core formula and condition in NCERT Class 10 Chapter 4 before tackling Exercises 4.1, 4.2, and 4.3!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="inspectCh4Sum('std')" id="btn-c4s-std" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Standard Form</button>
        <button onclick="inspectCh4Sum('fac')" id="btn-c4s-fac" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Factorisation</button>
        <button onclick="inspectCh4Sum('frm')" id="btn-c4s-frm" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Formula</button>
        <button onclick="inspectCh4Sum('dsc')" id="btn-c4s-dsc" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Discriminant D</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-1.5 text-xs">
        <h4 class="font-bold text-cyan-300 text-sm" id="c4s-title">1. Standard Quadratic Equation</h4>
        <p class="text-slate-300 leading-relaxed" id="c4s-desc">ax² + bx + c = 0 where a, b, c ∈ ℝ and strictly a ≠ 0. Real α is a root of ax² + bx + c = 0 iff α is a zero of quadratic polynomial p(x).</p>
    </div>
</div>

<script>
function inspectCh4Sum(k) {
    const map = {
        std: { t: '1. Standard Quadratic Equation', d: 'ax² + bx + c = 0 where a, b, c ∈ ℝ and strictly a ≠ 0. Real α is a root of ax² + bx + c = 0 iff α is a zero of quadratic polynomial p(x).' },
        fac: { t: '2. Factorisation Method', d: 'Split middle term bx cleanly into p + q = b with p·q = a·c, factor into two linear brackets, and equate each factor to 0.' },
        frm: { t: "3. Sridharacharya's Quadratic Formula", d: 'When D = b² − 4ac ≥ 0, exact roots equal x = (−b ± √(b² − 4ac)) / (2a). Works universally even on irrational or prime constants.' },
        dsc: { t: '4. Nature of Roots via D = b² − 4ac', d: 'D > 0 -> 2 distinct real roots; D = 0 -> 2 equal real roots (−b/(2a)); D < 0 -> no real roots (impossible physical constraints).' }
    };
    const d = map[k];
    if (!d) return;
    ['std', 'fac', 'frm', 'dsc'].forEach(x => {
        const b = document.getElementById('btn-c4s-' + x);
        if (b) {
            b.className = (x === k)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('c4s-title').textContent = d.t;
    document.getElementById('c4s-desc').textContent = d.d;
}
</script>
"""
