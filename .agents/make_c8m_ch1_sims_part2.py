#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 1: A Square and A Cube
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: 3D Cubic Numbers Stacker & Volume Scaling (n³)
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧊</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">3D Unit-Cube Builder & Dimension Scaling (n³ = n×n×n)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8s9-badge">3³ = 27 Unit Cubes</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Cube Edge Length n (1 to 6):</span><span class="font-bold text-cyan-300" id="c8s9-nv">n = 3</span></div>
        <input type="range" min="1" max="6" step="1" value="3" id="c8s9-n" oninput="updC8S9()" class="w-full accent-cyan-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2">
        <div class="text-emerald-300 font-bold text-sm" id="c8s9-vol"></div>
        <div class="text-amber-300" id="c8s9-layer"></div>
        <div class="text-purple-300">Fractions/Decimals: 0.2³ = 0.008  |  0.3³ = 0.027  |  (2/3)³ = 8/27</div>
    </div>
</div>

<script>
function updC8S9() {
    const n = parseInt(document.getElementById("c8s9-n").value, 10);
    const cube = n * n * n;
    document.getElementById("c8s9-nv").textContent = "n = " + n;
    document.getElementById("c8s9-badge").textContent = `${n}³ = ${cube} Unit Cubes`;
    document.getElementById("c8s9-vol").textContent = `Volume = ${n} × ${n} × ${n} = ${cube} unit cubes (${n} layers of ${n*n} cubes each!)`;
    document.getElementById("c8s9-layer").textContent = `Scaling check: A cube with edge ${n}× larger than 1×1×1 holds ${cube}× more volume!`;
}
updC8S9();
</script>
"""

# Simulator 10: Cube Units Digit Swap Rule (2↔8, 3↔7) & Zero Tripling
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔄</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Cube Last-Digit Swap Explorer (2↔8, 3↔7) & Zero Tripling</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">All 0–9 Allowed!</span>
    </div>

    <div class="grid grid-cols-5 sm:grid-cols-10 gap-1.5 font-mono text-xs" id="c8s10-btns"></div>
    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5" id="c8s10-box"></div>
</div>

<script>
function pickCubeDigS10(d) {
    let html = "";
    for (let k = 0; k <= 9; k++) {
        html += `<button onclick="pickCubeDigS10(${k})" class="p-2 rounded-lg font-bold border ${k === d ? "bg-amber-600 border-amber-400 text-white" : "bg-slate-900 border-slate-700 text-slate-300"}">${k}</button>`;
    }
    document.getElementById("c8s10-btns").innerHTML = html;
    const c = d * d * d;
    const last = c % 10;
    const tag = (d === last) ? "IDENTICAL (stays " + last + "!)" : "SWAPPED PAIR (" + d + " ↔ " + last + "!)";
    document.getElementById("c8s10-box").innerHTML = `
        <div class="text-cyan-300 font-bold">Compute ${d}³ = ${c}  ⇒  Units Digit of Cube = ${last}  [${tag}]</div>
        <div class="text-emerald-300">Zero Rule: Cubing TRIPLES trailing zeros! 10³ = 1,000 (3 zeros), 200³ = 8,000,000 (6 zeros), whereas 80,000 (4 zeros) fails!</div>`;
}
pickCubeDigS10(8);
</script>
"""

# Simulator 11: Hardy-Ramanujan Taxicab Number Visualizer (1729 & 4104)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🚕</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Hardy–Ramanujan Taxicab Number Lab (1729 & 4104)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">2 Distinct Cube Sums</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC8S11(1729)" id="btn-811-1729" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs">Ta(2) = 1,729 (Smallest!)</button>
        <button onclick="pickC8S11(4104)" id="btn-811-4104" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Next Taxicab: 4,104</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2" id="c8s11-box"></div>
</div>

<script>
function pickC8S11(num) {
    document.getElementById("btn-811-1729").className = num === 1729
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-811-4104").className = num === 4104
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const box = document.getElementById("c8s11-box");
    if (num === 1729) {
        box.innerHTML = `<div class="text-amber-300 font-bold">1,729 (1918 London Taxicab Story — Srinivasa Ramanujan & G. H. Hardy):</div>
            <div class="text-cyan-300 font-bold">Way 1:  1³ + 12³  =  1 + 1,728  =  1,729!</div>
            <div class="text-emerald-300 font-bold">Way 2:  9³ + 10³  =  729 + 1,000  =  1,729!</div>`;
    } else {
        box.innerHTML = `<div class="text-amber-300 font-bold">4,104 (Second Smallest Taxicab Number):</div>
            <div class="text-cyan-300 font-bold">Way 1:  2³ + 16³  =  8 + 4,096  =  4,104!</div>
            <div class="text-emerald-300 font-bold">Way 2:  9³ + 15³  =  729 + 3,375  =  4,104!</div>`;
    }
}
pickC8S11(1729);
</script>
"""

# Simulator 12: Nicomachus Consecutive Odd-Number Block Cube Pyramid (n³)
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪜</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Consecutive Odd-Block Cube Staircase (n terms → n³)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800" id="c8s12-badge">Row 4 → 64</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Select Cube Row n (1 to 7):</span><span class="font-bold text-purple-300" id="c8s12-nv">Row 4 (4³)</span></div>
        <input type="range" min="1" max="7" step="1" value="4" id="c8s12-n" oninput="updC8S12()" class="w-full accent-purple-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-cyan-300 font-bold" id="c8s12-terms"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c8s12-sum"></div>
    </div>
</div>

<script>
function updC8S12() {
    const n = parseInt(document.getElementById("c8s12-n").value, 10);
    const startOdd = n * (n - 1) + 1;
    const block = Array.from({length: n}, (_, i) => startOdd + 2 * i);
    document.getElementById("c8s12-nv").textContent = `Row ${n} (${n}³)`;
    document.getElementById("c8s12-badge").textContent = `Row ${n} → ${n*n*n}`;
    document.getElementById("c8s12-terms").textContent = `Block ${n} (${n} consecutive odd numbers centered at ${n}²=${n*n}): ${block.join(" + ")}`;
    document.getElementById("c8s12-sum").textContent = `Exact Sum = ${n} × ${n*n} = ${n}³ = ${n*n*n}!`;
}
updC8S12();
</script>
"""

# Simulator 13: Prime Triplets Cube Root Extractor & Asymmetric Multiplier/Divisor
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">∛</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Prime Factorization Triplets Cube Root Machine</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Groups of 3</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickC8S13(0)" id="btn-813-0" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs">∛3,375 = 15</button>
        <button onclick="pickC8S13(1)" id="btn-813-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">∛13,824 = 24</button>
        <button onclick="pickC8S13(2)" id="btn-813-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Repair 392 & 675</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5" id="c8s13-box"></div>
</div>

<script>
function pickC8S13(idx) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-813-" + k).className = k === idx
            ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const msgs = [
        `<div class="text-cyan-300 font-bold">3,375 = (3 × 3 × 3) × (5 × 5 × 5)</div><div class="text-emerald-300 font-bold text-sm">Pull 1 prime per triplet: ∛3,375 = 3 × 5 = 15!</div>`,
        `<div class="text-cyan-300 font-bold">13,824 = (2×2×2) × (2×2×2) × (2×2×2) × (3×3×3) = 2⁹ × 3³</div><div class="text-emerald-300 font-bold text-sm">Pull 1 per triplet: ∛13,824 = 2 × 2 × 2 × 3 = 24!</div>`,
        `<div class="text-rose-300 font-bold">Incomplete Triplet Alert!</div>
         <div class="text-amber-300">• 392 = (2³) × 7² ⇒ Multiply by 7 (→ 2744 = 14³) OR Divide by 49 (→ 8 = 2³)!</div>
         <div class="text-emerald-300 font-bold">• 675 = (3³) × 5² ⇒ Multiply by 5 (→ 3375 = 15³) OR Divide by 25 (→ 27 = 3³)!</div>`
    ];
    document.getElementById("c8s13-box").innerHTML = msgs[idx];
}
pickC8S13(0);
</script>
"""

# Simulator 14: Successive Finite Differences Cascade (Squares L2=2 vs Cubes L3=6)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔻</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Successive Finite Differences (Squares L2 = 2, Cubes L3 = 6)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Level Stabilization</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC8S14(2)" id="btn-814-2" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs">Squares Cascade (L2 = 2)</button>
        <button onclick="pickC8S14(3)" id="btn-814-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Cubes Cascade (L3 = 6)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center" id="c8s14-box"></div>
</div>

<script>
function pickC8S14(deg) {
    document.getElementById("btn-814-2").className = deg === 2
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-814-3").className = deg === 3
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const box = document.getElementById("c8s14-box");
    if (deg === 2) {
        box.innerHTML = `<div class="text-slate-200 font-bold">Squares:  1,   4,   9,   16,   25,   36</div>
            <div class="text-cyan-300">Level 1 Diff:   3,   5,   7,   9,   11   (Consecutive odds!)</div>
            <div class="text-emerald-300 font-bold text-sm">Level 2 Diff:     2,   2,   2,   2   (STABILIZED AT 2! = 2×1)</div>`;
    } else {
        box.innerHTML = `<div class="text-slate-200 font-bold">Cubes:   1,   8,   27,   64,   125,   216</div>
            <div class="text-cyan-300">Level 1 Diff:    7,   19,   37,   61,   91</div>
            <div class="text-amber-300">Level 2 Diff:      12,   18,   24,   30</div>
            <div class="text-emerald-300 font-bold text-sm">Level 3 Diff:        6,    6,    6   (STABILIZED AT 6! = 3×2×1)</div>`;
    }
}
pickC8S14(3);
</script>
"""

# Simulator 15: Historical Dictionary & Timeline (Babylon 1700 BCE, Varga, Ghana, Mula)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📜</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Pinch of History Explorer (1700 BCE Babylon → Aryabhata & Brahmagupta)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Section 1.3</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickC8S15(0)" id="btn-815-0" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs">1700 BCE Tablets</button>
        <button onclick="pickC8S15(1)" id="btn-815-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Varga & Ghana</button>
        <button onclick="pickC8S15(2)" id="btn-815-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Mula Roots</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5" id="c8s15-box"></div>
</div>

<script>
function pickC8S15(m) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-815-" + k).className = k === m
            ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const msgs = [
        `<div class="text-amber-300 font-bold">Babylonian Clay Tablets (~1700 BCE, e.g. YBC 7289):</div>
         <div class="text-slate-200">Ancient Mesopotamian scribes inscribed tables of squares, cubes, and accurate √2 estimates (1.41421296...) in cuneiform clay!</div>`,
        `<div class="text-cyan-300 font-bold">Aryabhata (499 CE) & Brahmagupta (628 CE) Sanskrit Terms:</div>
         <div class="text-emerald-300 font-bold">• Varga = Square / Area (rows of equal length)   |   • Ghana = Cube / Solid 3D Volume</div>`,
        `<div class="text-emerald-300 font-bold">Meaning of Mula (Sanskrit: Plant Root / Foundation):</div>
         <div class="text-slate-200">• Varga-mula = Square Root (√)   |   • Ghana-mula = Cube Root (∛) — the foundational edge growing a square or cube!</div>`
    ];
    document.getElementById("c8s15-box").innerHTML = msgs[m];
}
pickC8S15(1);
</script>
"""

# Simulator 16: IT'S PUZZLE TIME — Square Pairs (1..15 Adjacent Sums = Perfect Squares!)
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧩</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">IT'S PUZZLE TIME: Square Pairs Chain (1 to 15)</h3>
        </div>
        <button onclick="togglePairsS16()" id="c8s16-btn" class="text-[11px] bg-amber-600 hover:bg-amber-500 text-white font-bold px-3 py-1 rounded-full">Show Adjacent Sums!</button>
    </div>

    <div class="flex flex-wrap justify-center gap-1 font-mono text-xs" id="c8s16-chain"></div>
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs text-emerald-300 font-bold text-center" id="c8s16-info"></div>
</div>

<script>
let showSums16 = true;
function togglePairsS16() {
    showSums16 = !showSums16;
    renderPairsS16();
}
function renderPairsS16() {
    const seq = [8, 1, 15, 10, 6, 3, 13, 12, 4, 5, 11, 14, 2, 7, 9];
    let html = "";
    for (let i = 0; i < seq.length; i++) {
        const end = (i === 0 || i === seq.length - 1);
        html += `<span class="px-2 py-1 rounded-lg font-bold border ${end ? "bg-rose-600/40 border-rose-400 text-rose-100" : "bg-cyan-600/30 border-cyan-500 text-cyan-100"}">${seq[i]}</span>`;
        if (i < seq.length - 1 && showSums16) {
            html += `<span class="text-[10px] text-amber-300 self-center font-bold">(${seq[i]+seq[i+1]})</span>`;
        }
    }
    document.getElementById("c8s16-chain").innerHTML = html;
    document.getElementById("c8s16-btn").textContent = showSums16 ? "Hide Sums" : "Show Adjacent Sums!";
    document.getElementById("c8s16-info").textContent = "Notice 8 (only 8+1=9) and 9 (only 9+7=16) anchor the ends; ALL 14 adjacent sums equal 9, 16, or 25!";
}
renderPairsS16();
</script>
"""
