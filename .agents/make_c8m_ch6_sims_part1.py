#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 6: We Distribute, Yet Things Multiply
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Letters And Distribution (Rectangular Orchard Dot Array a(b + c) = ab + ac)
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🟩</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Distributive Orchard Array: a(b + c) = ab + ac</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c6s1-badge">3 × (4 + 2) = 18</span>
    </div>

    <div class="grid grid-cols-3 gap-2 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Rows (a):</span><span class="font-bold text-cyan-300" id="c8c6s1-av">3</span></div>
            <input type="range" min="1" max="5" step="1" value="3" id="c8c6s1-a" oninput="updC8C6S1()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Left (b):</span><span class="font-bold text-amber-300" id="c8c6s1-bv">4</span></div>
            <input type="range" min="1" max="6" step="1" value="4" id="c8c6s1-b" oninput="updC8C6S1()" class="w-full accent-amber-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Right (c):</span><span class="font-bold text-emerald-300" id="c8c6s1-cv">2</span></div>
            <input type="range" min="1" max="6" step="1" value="2" id="c8c6s1-c" oninput="updC8C6S1()" class="w-full accent-emerald-400">
        </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 110" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800" id="c8c6s1-svg"></svg>
        <div class="font-mono text-xs space-y-2">
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-cyan-300 font-bold" id="c8c6s1-m1"></div>
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold" id="c8c6s1-m2"></div>
        </div>
    </div>
</div>

<script>
function updC8C6S1() {
    const a = parseInt(document.getElementById("c8c6s1-a").value);
    const b = parseInt(document.getElementById("c8c6s1-b").value);
    const c = parseInt(document.getElementById("c8c6s1-c").value);
    const tot = a * (b + c);
    document.getElementById("c8c6s1-av").textContent = a;
    document.getElementById("c8c6s1-bv").textContent = b;
    document.getElementById("c8c6s1-cv").textContent = c;
    document.getElementById("c8c6s1-badge").textContent = a + "×(" + b + "+" + c + ") = " + tot;
    document.getElementById("c8c6s1-m1").textContent = "Whole Grid: " + a + " × (" + b + " + " + c + ") = " + a + " × " + (b + c) + " = " + tot;
    document.getElementById("c8c6s1-m2").textContent = "Two Blocks: (" + a + "×" + b + ") + (" + a + "×" + c + ") = " + (a * b) + " + " + (a * c) + " = " + tot;

    let dots = "";
    const step = 16;
    for (let r = 0; r < a; r++) {
        for (let col = 0; col < b + c; col++) {
            const x = 18 + col * step + (col >= b ? 10 : 0);
            const y = 20 + r * step;
            dots += `<circle cx="${x}" cy="${y}" r="5" fill="${col < b ? "#fbbf24" : "#34d399"}"/>`;
        }
    }
    document.getElementById("c8c6s1-svg").innerHTML = dots;
}
updC8C6S1();
</script>
"""

# Simulator 2: Increments In Products ((a+1)(b+1) vs (a+1)(b-1))
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📈</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Product Increment Explorer: (a+1)(b+1) &amp; (a+1)(b−1)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c6s2-badge">6 × 4 = 24</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Factor a:</span><span class="font-bold text-cyan-300" id="c8c6s2-av">6</span></div>
            <input type="range" min="2" max="20" step="1" value="6" id="c8c6s2-a" oninput="updC8C6S2()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Factor b:</span><span class="font-bold text-amber-300" id="c8c6s2-bv">4</span></div>
            <input type="range" min="2" max="20" step="1" value="4" id="c8c6s2-b" oninput="updC8C6S2()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-emerald-300 font-bold" id="c8c6s2-pp"></div>
        <div class="text-cyan-200 font-bold" id="c8c6s2-pm"></div>
    </div>
</div>

<script>
function updC8C6S2() {
    const a = parseInt(document.getElementById("c8c6s2-a").value);
    const b = parseInt(document.getElementById("c8c6s2-b").value);
    const ab = a * b;
    const incPP = a + b + 1;
    const chgPM = b - a - 1;
    document.getElementById("c8c6s2-av").textContent = a;
    document.getElementById("c8c6s2-bv").textContent = b;
    document.getElementById("c8c6s2-badge").textContent = a + " × " + b + " = " + ab;
    document.getElementById("c8c6s2-pp").textContent = "(a+1)(b+1) = " + (a + 1) + "×" + (b + 1) + " = " + (ab + incPP) + "   (Increased by a+b+1 = +" + incPP + ")";
    document.getElementById("c8c6s2-pm").textContent = "(a+1)(b−1) = " + (a + 1) + "×" + (b - 1) + " = " + (ab + chgPM) + "   (Change = b−a−1 = " + (chgPM >= 0 ? "+" : "") + chgPM + ")";
}
updC8C6S2();
</script>
"""

# Simulator 3: Identity One Proofs (4-Tile Area Sub-Grid (a+m)(b+n))
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪟</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Identity 1 Area Grid: (a + m)(b + n) = ab + an + mb + mn</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c6s3-badge">13 × 24 = 312</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">m (extra width):</span><span class="font-bold text-amber-300" id="c8c6s3-mv">3</span></div>
            <input type="range" min="1" max="9" step="1" value="3" id="c8c6s3-m" oninput="updC8C6S3()" class="w-full accent-amber-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">n (extra height):</span><span class="font-bold text-emerald-300" id="c8c6s3-nv">4</span></div>
            <input type="range" min="1" max="9" step="1" value="4" id="c8c6s3-n" oninput="updC8C6S3()" class="w-full accent-emerald-400">
        </div>
    </div>

    <div class="grid grid-cols-2 gap-1.5 max-w-sm mx-auto font-mono text-xs text-center" id="c8c6s3-grid"></div>
    <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 font-mono text-xs text-emerald-300 font-bold text-center" id="c8c6s3-sum"></div>
</div>

<script>
function updC8C6S3() {
    const a = 10, b = 20;
    const m = parseInt(document.getElementById("c8c6s3-m").value);
    const n = parseInt(document.getElementById("c8c6s3-n").value);
    const tot = (a + m) * (b + n);
    document.getElementById("c8c6s3-mv").textContent = m;
    document.getElementById("c8c6s3-nv").textContent = n;
    document.getElementById("c8c6s3-badge").textContent = (a + m) + " × " + (b + n) + " = " + tot;
    document.getElementById("c8c6s3-grid").innerHTML = `
        <div class="p-2 rounded-lg bg-cyan-950/60 border border-cyan-600 text-cyan-200 font-bold">a×b = ${a}×${b} = ${a * b}</div>
        <div class="p-2 rounded-lg bg-emerald-950/60 border border-emerald-600 text-emerald-200 font-bold">a×n = ${a}×${n} = ${a * n}</div>
        <div class="p-2 rounded-lg bg-amber-950/60 border border-amber-600 text-amber-200 font-bold">m×b = ${m}×${b} = ${m * b}</div>
        <div class="p-2 rounded-lg bg-indigo-950/60 border border-indigo-600 text-indigo-200 font-bold">m×n = ${m}×${n} = ${m * n}</div>
    `;
    document.getElementById("c8c6s3-sum").textContent = "(" + a + "+" + m + ")(" + b + "+" + n + ") = " + (a * b) + " + " + (a * n) + " + " + (m * b) + " + " + (m * n) + " = " + tot;
}
updC8C6S3();
</script>
"""

# Simulator 4: Negative Binomial Adjustments ((20-u)(20-v) Signed Sign Tracker)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">➖</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Signed Binomial Expander: (a − u)(b − v) = ab − av − ub + uv</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c8c6s4-badge">18 × 17 = 306</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Subtract u from 20:</span><span class="font-bold text-rose-300" id="c8c6s4-uv">u = 2 (factor = 18)</span></div>
            <input type="range" min="1" max="8" step="1" value="2" id="c8c6s4-u" oninput="updC8C6S4()" class="w-full accent-rose-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Subtract v from 20:</span><span class="font-bold text-amber-300" id="c8c6s4-vv">v = 3 (factor = 17)</span></div>
            <input type="range" min="1" max="8" step="1" value="3" id="c8c6s4-v" oninput="updC8C6S4()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-cyan-200" id="c8c6s4-exp"></div>
        <div class="text-emerald-300 font-bold" id="c8c6s4-res"></div>
    </div>
</div>

<script>
function updC8C6S4() {
    const u = parseInt(document.getElementById("c8c6s4-u").value);
    const v = parseInt(document.getElementById("c8c6s4-v").value);
    const f1 = 20 - u, f2 = 20 - v;
    const prod = f1 * f2;
    document.getElementById("c8c6s4-uv").textContent = "u = " + u + " (factor = " + f1 + ")";
    document.getElementById("c8c6s4-vv").textContent = "v = " + v + " (factor = " + f2 + ")";
    document.getElementById("c8c6s4-badge").textContent = f1 + " × " + f2 + " = " + prod;
    document.getElementById("c8c6s4-exp").textContent = "(20 − " + u + ")(20 − " + v + ") = 400 − " + (20 * v) + " − " + (20 * u) + " + " + (u * v) + "  [(−u)(−v) = +uv!]";
    document.getElementById("c8c6s4-res").textContent = "Final Product = " + prod;
}
updC8C6S4();
</script>
"""

# Simulator 5: Polynomial Distribution Proofs (Brahmagupta's Khaṇḍa-Guṇanam & Cubic Binomial)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📜</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">Polynomial Multiplier &amp; Brahmagupta's Khaṇḍa-Guṇanam (Verse 12.55)</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c6s5-badge">Cubic Expansion</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Test a:</span><span class="font-bold text-cyan-300" id="c8c6s5-av">2</span></div>
            <input type="range" min="1" max="5" step="1" value="2" id="c8c6s5-a" oninput="updC8C6S5()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Test b:</span><span class="font-bold text-amber-300" id="c8c6s5-bv">3</span></div>
            <input type="range" min="1" max="5" step="1" value="3" id="c8c6s5-b" oninput="updC8C6S5()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-amber-300 font-bold" id="c8c6s5-lhs"></div>
        <div class="text-emerald-300 font-bold" id="c8c6s5-rhs"></div>
    </div>
</div>

<script>
function updC8C6S5() {
    const a = parseInt(document.getElementById("c8c6s5-a").value);
    const b = parseInt(document.getElementById("c8c6s5-b").value);
    const t1 = Math.pow(a, 3), t2 = 3 * a * a * b, t3 = 3 * a * b * b, t4 = Math.pow(b, 3);
    const sum = t1 + t2 + t3 + t4;
    document.getElementById("c8c6s5-av").textContent = a;
    document.getElementById("c8c6s5-bv").textContent = b;
    document.getElementById("c8c6s5-lhs").textContent = "(a+b)(a²+2ab+b²) = (" + (a + b) + ") × (" + (a * a + 2 * a * b + b * b) + ") = " + sum;
    document.getElementById("c8c6s5-rhs").textContent = "a³ + 3a²b + 3ab² + b³ = " + t1 + " + " + t2 + " + " + t3 + " + " + t4 + " = " + sum + " ✓";
}
updC8C6S5();
</script>
"""

# Simulator 6: Fast Multiplication Shortcuts (Iṣṭa-Guṇana ×11, ×101, ×99, ×999)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚡</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Fast Mental Multipliers (×11, ×101, ×99, ×999 via Iṣṭa-Guṇana)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c6s6-badge">×11 Trick</span>
    </div>

    <div class="flex flex-wrap items-center justify-between gap-2 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div class="flex gap-1.5">
            <button onclick="setMulS6(11)" class="px-2.5 py-1 rounded bg-amber-700 text-white font-bold">× 11</button>
            <button onclick="setMulS6(101)" class="px-2.5 py-1 rounded bg-cyan-700 text-white font-bold">× 101</button>
            <button onclick="setMulS6(99)" class="px-2.5 py-1 rounded bg-emerald-700 text-white font-bold">× 99</button>
            <button onclick="setMulS6(999)" class="px-2.5 py-1 rounded bg-indigo-700 text-white font-bold">× 999</button>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-slate-300">N:</span>
            <input type="range" min="12" max="99" step="1" value="64" id="c8c6s6-n" oninput="updC8C6S6()" class="w-28 accent-amber-400">
            <span class="font-bold text-amber-300 font-mono" id="c8c6s6-nv">64</span>
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-cyan-200 font-bold" id="c8c6s6-steps"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c8c6s6-ans"></div>
    </div>
</div>

<script>
let mulS6 = 99;
function setMulS6(m) { mulS6 = m; updC8C6S6(); }
function updC8C6S6() {
    const N = parseInt(document.getElementById("c8c6s6-n").value);
    document.getElementById("c8c6s6-nv").textContent = N;
    document.getElementById("c8c6s6-badge").textContent = "×" + mulS6 + " Trick";
    let step = "";
    if (mulS6 === 11) step = N + " × (10 + 1) = " + (N * 10) + " + " + N;
    else if (mulS6 === 101) step = N + " × (100 + 1) = " + (N * 100) + " + " + N;
    else if (mulS6 === 99) step = N + " × (100 − 1) = " + (N * 100) + " − " + N;
    else step = N + " × (1,000 − 1) = " + (N * 1000).toLocaleString("en-IN") + " − " + N;
    document.getElementById("c8c6s6-steps").textContent = step;
    document.getElementById("c8c6s6-ans").textContent = N + " × " + mulS6 + " = " + (N * mulS6).toLocaleString("en-IN");
}
updC8C6S6();
</script>
"""

# Simulator 7: Square Of Sum (Identity 1A 4-Piece Dissection Visual)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🟦</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Identity 1A Square Dissection: (a + b)² = a² + 2ab + b²</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c6s7-badge">15² = 225</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Part a:</span><span class="font-bold text-cyan-300" id="c8c6s7-av">10</span></div>
            <input type="range" min="4" max="14" step="1" value="10" id="c8c6s7-a" oninput="updC8C6S7()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Part b:</span><span class="font-bold text-amber-300" id="c8c6s7-bv">5</span></div>
            <input type="range" min="1" max="8" step="1" value="5" id="c8c6s7-b" oninput="updC8C6S7()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800 font-mono text-xs">
        <svg viewBox="0 0 120 120" class="w-full max-h-32 bg-slate-950 rounded-xl border border-slate-800" id="c8c6s7-svg"></svg>
        <div class="space-y-2">
            <div class="p-2 bg-slate-950 rounded-lg border border-cyan-700/60 text-cyan-200 font-bold" id="c8c6s7-parts"></div>
            <div class="p-2 bg-slate-950 rounded-lg border border-emerald-700/60 text-emerald-300 font-bold" id="c8c6s7-tot"></div>
        </div>
    </div>
</div>

<script>
function updC8C6S7() {
    const a = parseInt(document.getElementById("c8c6s7-a").value);
    const b = parseInt(document.getElementById("c8c6s7-b").value);
    const tot = (a + b) * (a + b);
    document.getElementById("c8c6s7-av").textContent = a;
    document.getElementById("c8c6s7-bv").textContent = b;
    document.getElementById("c8c6s7-badge").textContent = (a + b) + "² = " + tot;
    document.getElementById("c8c6s7-parts").textContent = "a²=" + (a * a) + "  +  2ab=" + (2 * a * b) + "  +  b²=" + (b * b);
    document.getElementById("c8c6s7-tot").textContent = "(" + a + " + " + b + ")² = " + tot + " (Two ab strips NEVER drop!)";

    const scale = 96 / (a + b);
    const sa = a * scale, sb = b * scale;
    document.getElementById("c8c6s7-svg").innerHTML = `
        <rect x="12" y="12" width="${sa.toFixed(1)}" height="${sa.toFixed(1)}" fill="#06b6d4" fill-opacity="0.35" stroke="#22d3ee"/>
        <rect x="${(12 + sa).toFixed(1)}" y="12" width="${sb.toFixed(1)}" height="${sa.toFixed(1)}" fill="#10b981" fill-opacity="0.35" stroke="#34d399"/>
        <rect x="12" y="${(12 + sa).toFixed(1)}" width="${sa.toFixed(1)}" height="${sb.toFixed(1)}" fill="#10b981" fill-opacity="0.35" stroke="#34d399"/>
        <rect x="${(12 + sa).toFixed(1)}" y="${(12 + sa).toFixed(1)}" width="${sb.toFixed(1)}" height="${sb.toFixed(1)}" fill="#f59e0b" fill-opacity="0.45" stroke="#fbbf24"/>
    `;
}
updC8C6S7();
</script>
"""

# Simulator 8: Square Of Difference (Identity 1B Corner Restoration Proof)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🟧</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Identity 1B Corner Restoration: (a − b)² = a² − 2ab + b²</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c6s8-badge">97² = 9,409</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Subtract Strip Width b from a = 100 (1 to 15):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c6s8-bv">b = 3 → (100 − 3)² = 97²</span>
        </div>
        <input type="range" min="1" max="15" step="1" value="3" id="c8c6s8-b" oninput="updC8C6S8()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-cyan-200" id="c8c6s8-calc"></div>
        <div class="text-emerald-300 font-bold" id="c8c6s8-why"></div>
    </div>
</div>

<script>
function updC8C6S8() {
    const b = parseInt(document.getElementById("c8c6s8-b").value);
    const val = (100 - b) * (100 - b);
    document.getElementById("c8c6s8-bv").textContent = "b = " + b + " → (100 − " + b + ")² = " + (100 - b) + "²";
    document.getElementById("c8c6s8-badge").textContent = (100 - b) + "² = " + val.toLocaleString("en-IN");
    document.getElementById("c8c6s8-calc").textContent = "100² − 2(100)(" + b + ") + " + b + "² = 10,000 − " + (200 * b) + " + " + (b * b) + " = " + val.toLocaleString("en-IN");
    document.getElementById("c8c6s8-why").textContent = "Removing two 100×" + b + " strips cut the " + b + "² corner TWICE → Adding +" + (b * b) + " back fixes it!";
}
updC8C6S8();
</script>
"""

if __name__ == "__main__":
    print(f"Prepared {len(simulators_part1)} interactive simulators (Part 1).")
