#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 6: We Distribute, Yet Things Multiply
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Sum Of Squares & Calendar Diagonal Proofs
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📅</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">Pattern 1: 2(a² + b²) &amp; Calendar 2×2 Diagonal Product Proof</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c6s9-badge">Diff = 7 Always</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Pick Starting Calendar Date n (1 to 22):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c6s9-nv">n = 8</span>
        </div>
        <input type="range" min="1" max="22" step="1" value="8" id="c8c6s9-n" oninput="updC8C6S9()" class="w-full accent-indigo-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-2xl border border-slate-800 font-mono text-xs">
        <div class="grid grid-cols-2 gap-1.5 text-center max-w-[160px] mx-auto w-full" id="c8c6s9-cal"></div>
        <div class="space-y-2">
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold" id="c8c6s9-diff"></div>
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-cyan-200 font-bold">Sum Pattern 1: (a+b)² + (a−b)² = 2(a² + b²)</div>
        </div>
    </div>
</div>

<script>
function updC8C6S9() {
    const n = parseInt(document.getElementById("c8c6s9-n").value);
    const p1 = (n + 1) * (n + 7), p2 = n * (n + 8);
    document.getElementById("c8c6s9-nv").textContent = "n = " + n;
    document.getElementById("c8c6s9-cal").innerHTML = `
        <div class="p-2 rounded bg-slate-950 border border-cyan-600 text-cyan-200 font-bold">${n}</div>
        <div class="p-2 rounded bg-slate-950 border border-amber-600 text-amber-200 font-bold">${n + 1}</div>
        <div class="p-2 rounded bg-slate-950 border border-amber-600 text-amber-200 font-bold">${n + 7}</div>
        <div class="p-2 rounded bg-slate-950 border border-cyan-600 text-cyan-200 font-bold">${n + 8}</div>
    `;
    document.getElementById("c8c6s9-diff").textContent = "(" + (n + 1) + "×" + (n + 7) + ") − (" + n + "×" + (n + 8) + ") = " + p1 + " − " + p2 + " = " + (p1 - p2) + " ALWAYS!";
}
updC8C6S9();
</script>
"""

# Simulator 10: Difference Of Squares (Identity 1C L-Cut Rearrangement)
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✂️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Identity 1C Mental Calculator: (a + b)(a − b) = a² − b²</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c6s10-badge">104 × 96 = 9,984</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Symmetric Distance b Around Center a = 100 (1 to 15):</span>
            <span class="font-bold text-emerald-300 font-mono" id="c8c6s10-bv">b = 4 → 104 × 96</span>
        </div>
        <input type="range" min="1" max="15" step="1" value="4" id="c8c6s10-b" oninput="updC8C6S10()" class="w-full accent-emerald-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-cyan-200" id="c8c6s10-exp"></div>
        <div class="text-amber-300 font-bold text-sm" id="c8c6s10-res"></div>
    </div>
</div>

<script>
function updC8C6S10() {
    const b = parseInt(document.getElementById("c8c6s10-b").value);
    const val = 10000 - b * b;
    document.getElementById("c8c6s10-bv").textContent = "b = " + b + " → " + (100 + b) + " × " + (100 - b);
    document.getElementById("c8c6s10-badge").textContent = (100 + b) + "×" + (100 - b) + " = " + val.toLocaleString("en-IN");
    document.getElementById("c8c6s10-exp").textContent = "(100 + " + b + ")(100 − " + b + ") = 100² − " + b + "² = 10,000 − " + (b * b);
    document.getElementById("c8c6s10-res").textContent = (100 + b) + " × " + (100 - b) + " = " + val.toLocaleString("en-IN");
}
updC8C6S10();
</script>
"""

# Simulator 11: Sridharacharya Squaring Trick (a² = (a+b)(a-b) + b²)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧠</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Śrīdharācārya's Squaring Machine: a² = (a + b)(a − b) + b²</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c6s11-badge">197² = 38,809</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Pick Any Integer Near 200 (191 to 209):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c6s11-av">a = 197 (distance b = 3)</span>
        </div>
        <input type="range" min="191" max="209" step="1" value="197" id="c8c6s11-a" oninput="updC8C6S11()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-cyan-200" id="c8c6s11-step"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c8c6s11-res"></div>
    </div>
</div>

<script>
function updC8C6S11() {
    const a = parseInt(document.getElementById("c8c6s11-a").value);
    const b = Math.abs(200 - a);
    const other = a <= 200 ? a - b : a + b;
    const prod = 200 * other;
    const tot = prod + b * b;
    document.getElementById("c8c6s11-av").textContent = "a = " + a + " (distance b = " + b + " from 200)";
    document.getElementById("c8c6s11-badge").textContent = a + "² = " + tot.toLocaleString("en-IN");
    document.getElementById("c8c6s11-step").textContent = a + "² = (200 × " + other + ") + " + b + "² = " + prod.toLocaleString("en-IN") + " + " + (b * b);
    document.getElementById("c8c6s11-res").textContent = "Result = " + tot.toLocaleString("en-IN") + " ✓";
}
updC8C6S11();
</script>
"""

# Simulator 12: Mend Algebraic Mistakes (Sign Drops & Freshman's Dream Fixer)
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🛠️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Error Clinic: Mind the Mistake, Mend the Mistake (Part 1)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c8c6s12-badge">Case 1 / 4</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 bg-slate-900/90 p-2.5 rounded-xl border border-slate-800 text-xs">
        <button onclick="setErrS12(0)" class="p-1.5 rounded bg-rose-700 text-white font-bold">4(x+5)</button>
        <button onclick="setErrS12(1)" class="p-1.5 rounded bg-slate-800 text-rose-300 font-bold border border-slate-700">−3(y−7)</button>
        <button onclick="setErrS12(2)" class="p-1.5 rounded bg-slate-800 text-rose-300 font-bold border border-slate-700">(x+y)²</button>
        <button onclick="setErrS12(3)" class="p-1.5 rounded bg-slate-800 text-rose-300 font-bold border border-slate-700">5−2(3x−4)</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-2">
        <div class="text-rose-300 font-bold" id="c8c6s12-bad"></div>
        <div class="text-emerald-300 font-bold" id="c8c6s12-fix"></div>
        <div class="text-cyan-200" id="c8c6s12-why"></div>
    </div>
</div>

<script>
const errs12 = [
    { b: "Case 1 / 4", bad: "Wrong: 4(x + 5) = 4x + 5", fix: "Fixed: 4(x + 5) = 4x + 20", why: "Outer factor 4 must distribute cleanly onto BOTH x AND +5!" },
    { b: "Case 2 / 4", bad: "Wrong: −3(y − 7) = −3y − 21", fix: "Fixed: −3(y − 7) = −3y + 21", why: "Negative (−3) × Negative (−7) = POSITIVE (+21)!" },
    { b: "Case 3 / 4", bad: "Wrong: (x + y)² = x² + y²", fix: "Fixed: (x + y)² = x² + 2xy + y²", why: "Missing middle rectangles (+2xy)! Check x=3, y=4: 49 ≠ 25." },
    { b: "Case 4 / 4", bad: "Wrong: 5 − 2(3x − 4) = 3(3x − 4)", fix: "Fixed: 5 − 6x + 8 = 13 − 6x", why: "Never subtract 5 − 2 before distributing −2 across (3x − 4)!" }
];
function setErrS12(i) {
    document.getElementById("c8c6s12-badge").textContent = errs12[i].b;
    document.getElementById("c8c6s12-bad").textContent = errs12[i].bad;
    document.getElementById("c8c6s12-fix").textContent = errs12[i].fix;
    document.getElementById("c8c6s12-why").textContent = errs12[i].why;
}
setErrS12(0);
</script>
"""

# Simulator 13: Sign Like Terms (Error Clinic Part 2: Unlike Terms & Double-Distribution)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔎</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Error Clinic Part 2: Like Terms &amp; Scalar Brackets</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c6s13-badge">Trap #1</span>
    </div>

    <div class="grid grid-cols-3 gap-1.5 bg-slate-900/90 p-2.5 rounded-xl border border-slate-800 text-xs">
        <button onclick="setErrS13(0)" class="p-1.5 rounded bg-cyan-700 text-white font-bold">3x + 2y Trap</button>
        <button onclick="setErrS13(1)" class="p-1.5 rounded bg-slate-800 text-amber-300 font-bold border border-slate-700">(3x)² Coeff Trap</button>
        <button onclick="setErrS13(2)" class="p-1.5 rounded bg-slate-800 text-emerald-300 font-bold border border-slate-700">2(x+1)(x+5)</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-2">
        <div class="text-rose-300 font-bold" id="c8c6s13-bad"></div>
        <div class="text-emerald-300 font-bold" id="c8c6s13-fix"></div>
        <div class="text-cyan-200" id="c8c6s13-why"></div>
    </div>
</div>

<script>
const errs13 = [
    { b: "Trap #1", bad: "Wrong: 3x + 2y = 5xy   or   2x² + 5x = 7x³", fix: "Fixed: Stays strictly 3x + 2y (and 2x² + 5x)!", why: "Only LIKE terms with matching variable powers can ever combine coefficients!" },
    { b: "Trap #2", bad: "Wrong: (3x)² = 3x²", fix: "Fixed: (3x)² = 3² · x² = 9x²", why: "Exponents over a product square BOTH numerical factor 3 AND letter x!" },
    { b: "Trap #3", bad: "Wrong: 2(x+1)(x+5) = (2x+2)(2x+10)", fix: "Fixed: 2(x² + 6x + 5) = 2x² + 12x + 10", why: "Multiplying BOTH brackets by 2 scales the answer by 4 instead of 2!" }
];
function setErrS13(i) {
    document.getElementById("c8c6s13-badge").textContent = errs13[i].b;
    document.getElementById("c8c6s13-bad").textContent = errs13[i].bad;
    document.getElementById("c8c6s13-fix").textContent = errs13[i].fix;
    document.getElementById("c8c6s13-why").textContent = errs13[i].why;
}
setErrS13(0);
</script>
"""

# Simulator 14: Four Pattern Perspectives (Methods 1-4 -> k² + 2k Equivalence)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧩</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Section 6.4 Equivalence: 4 Distinct Visual Methods = k² + 2k</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c6s14-badge">k = 5 → 35 Tiles</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Pattern Step (k = 1 to 15):</span>
            <span class="font-bold text-emerald-300 font-mono" id="c8c6s14-kv">k = 5</span>
        </div>
        <input type="range" min="1" max="15" step="1" value="5" id="c8c6s14-k" oninput="updC8C6S14()" class="w-full accent-emerald-400">
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center font-mono text-xs" id="c8c6s14-cards"></div>
</div>

<script>
function updC8C6S14() {
    const k = parseInt(document.getElementById("c8c6s14-k").value);
    const m1 = (k + 1) * (k + 1) - 1;
    const m2 = k * k + 2 * k;
    const m3 = k * (k + 1) + k;
    const m4 = k * (k + 2);
    document.getElementById("c8c6s14-kv").textContent = "k = " + k;
    document.getElementById("c8c6s14-badge").textContent = "k = " + k + " → " + m2 + " Tiles";
    document.getElementById("c8c6s14-cards").innerHTML = `
        <div class="p-2 rounded-xl bg-slate-900 border border-cyan-600"><div class="text-[10px] text-cyan-300">M1: (k+1)²−1</div><div class="text-base font-black text-white">${m1}</div></div>
        <div class="p-2 rounded-xl bg-slate-900 border border-amber-600"><div class="text-[10px] text-amber-300">M2: k²+2k</div><div class="text-base font-black text-white">${m2}</div></div>
        <div class="p-2 rounded-xl bg-slate-900 border border-emerald-600"><div class="text-[10px] text-emerald-300">M3: k(k+1)+k</div><div class="text-base font-black text-white">${m3}</div></div>
        <div class="p-2 rounded-xl bg-slate-900 border border-indigo-600"><div class="text-[10px] text-indigo-300">M4: k(k+2)</div><div class="text-base font-black text-white">${m4}</div></div>
    `;
}
updC8C6S14();
</script>
"""

# Simulator 15: Border Walkway Areas (Concentric Outer-Inner vs 4-Strip + Corners)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏞️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Park Border Walkway Equivalence Calculator (10m × 6m Park)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c6s15-badge">w = 2 m → 80 m²</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Walkway Width w (1 to 5 m):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c6s15-wv">w = 2 m</span>
        </div>
        <input type="range" min="1" max="5" step="1" value="2" id="c8c6s15-w" oninput="updC8C6S15()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-cyan-300 font-bold" id="c8c6s15-p1"></div>
        <div class="text-emerald-300 font-bold" id="c8c6s15-p2"></div>
    </div>
</div>

<script>
function updC8C6S15() {
    const L = 10, B = 6, w = parseInt(document.getElementById("c8c6s15-w").value);
    const outW = L + 2 * w, outH = B + 2 * w;
    const p1 = outW * outH - L * B;
    const s1 = 2 * w * L, s2 = 2 * w * B, c4 = 4 * w * w;
    document.getElementById("c8c6s15-wv").textContent = "w = " + w + " m";
    document.getElementById("c8c6s15-badge").textContent = "w = " + w + " m → " + p1 + " m²";
    document.getElementById("c8c6s15-p1").textContent = "Path 1 (Outer − Inner): (" + outW + " × " + outH + ") − (10 × 6) = " + (outW * outH) + " − 60 = " + p1 + " m²";
    document.getElementById("c8c6s15-p2").textContent = "Path 2 (2wL + 2wB + 4w²): " + s1 + " + " + s2 + " + " + c4 + " = " + (s1 + s2 + c4) + " m² ✓";
}
updC8C6S15();
</script>
"""

# Simulator 16: Coin Conjoin Summary (Minimum Moves for Triangular Inversion floor(T_n / 3))
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪙</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">Puzzle Time: Coin Conjoin Triangle Inverter (T₄ = 10 → 3 Moves!)</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c6s16-badge">T₄ = 10 Coins</span>
    </div>

    <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <button onclick="setTriCoinS16(4)" class="px-2.5 py-1 rounded-lg bg-amber-700 text-white font-bold">10-Coin Triangle (n=4)</button>
        <button onclick="setTriCoinS16(5)" class="px-2.5 py-1 rounded-lg bg-cyan-700 text-white font-bold">15-Coin Triangle (n=5)</button>
        <button onclick="setTriCoinS16(6)" class="px-2.5 py-1 rounded-lg bg-emerald-700 text-white font-bold">21-Coin Triangle (n=6)</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-amber-300 font-bold text-sm" id="c8c6s16-res"></div>
        <div class="text-emerald-300 font-bold" id="c8c6s16-core"></div>
    </div>
</div>

<script>
function setTriCoinS16(n) {
    const total = (n * (n + 1)) / 2;
    const moves = Math.floor(total / 3);
    const fixed = total - moves;
    document.getElementById("c8c6s16-badge").textContent = "T_" + n + " = " + total + " Coins";
    document.getElementById("c8c6s16-res").textContent = "Invert " + total + "-Coin Triangle (" + n + " rows) in MINIMUM = floor(" + total + "/3) = " + moves + " Moves!";
    document.getElementById("c8c6s16-core").textContent = fixed + " overlapping interior coins remain stationary; move ONLY " + moves + " outer corner coins!";
}
setTriCoinS16(4);
</script>
"""

if __name__ == "__main__":
    print(f"Prepared {len(simulators_part2)} interactive simulators (Part 2).")
