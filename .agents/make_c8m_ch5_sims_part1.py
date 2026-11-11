#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 5: Number Play
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Consecutive Number Sums Finder (1 to 32)
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔢</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Consecutive Integer Sum Explorer (Powers of 2 Cannot Split!)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c5s1-badge">N = 15 (3 Ways)</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Test Any Natural Number N (2 to 32):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c5s1-nv">N = 15</span>
        </div>
        <input type="range" min="2" max="32" step="1" value="15" id="c8c5s1-n" oninput="updC8C5S1()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="font-bold text-sm" id="c8c5s1-count"></div>
        <div class="text-cyan-200 leading-relaxed" id="c8c5s1-list"></div>
    </div>
</div>

<script>
function updC8C5S1() {
    const N = parseInt(document.getElementById("c8c5s1-n").value);
    let ways = [];
    for (let k = 2; k * (k + 1) / 2 <= N; k++) {
        const rem = N - (k * (k - 1)) / 2;
        if (rem % k === 0) {
            const start = rem / k;
            if (start >= 1) {
                let seq = [];
                for (let j = 0; j < k; j++) seq.push(start + j);
                ways.push(seq.join(" + "));
            }
        }
    }
    document.getElementById("c8c5s1-nv").textContent = "N = " + N;
    document.getElementById("c8c5s1-badge").textContent = "N = " + N + " (" + ways.length + " Ways)";
    const cntEl = document.getElementById("c8c5s1-count");
    if (ways.length === 0) {
        cntEl.className = "font-bold text-sm text-rose-400";
        cntEl.textContent = "ZERO Ways! " + N + " is a pure POWER OF 2 (zero odd factors > 1)!";
        document.getElementById("c8c5s1-list").textContent = "Pure powers of 2 (2, 4, 8, 16, 32...) NEVER equal a sum of 2+ consecutive natural numbers.";
    } else {
        cntEl.className = "font-bold text-sm text-emerald-300";
        cntEl.textContent = ways.length + " Consecutive Way(s) Found for " + N + ":";
        document.getElementById("c8c5s1-list").textContent = ways.join("   |   ");
    }
}
updC8C5S1();
</script>
"""

# Simulator 2: Combining 4 Consecutive Numbers (±a ± b ± c ± d Always Even)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">➕</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">4 Consecutive Sign Flipper (±a ± b ± c ± d Always EVEN!)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c5s2-badge">Total: -2 (EVEN)</span>
    </div>

    <div class="flex items-center justify-between gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <span class="text-slate-300">Start Integer (a): <span class="font-bold text-amber-300" id="c8c5s2-av">5</span></span>
        <input type="range" min="1" max="25" step="1" value="5" id="c8c5s2-a" oninput="renderSignS2()" class="w-36 accent-amber-400">
    </div>

    <div class="grid grid-cols-4 gap-2 text-center font-mono text-xs" id="c8c5s2-btns"></div>
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs text-emerald-300 font-bold text-center" id="c8c5s2-res"></div>
</div>

<script>
let signsS2 = [1, -1, 1, -1];
function flipSignS2(idx) {
    signsS2[idx] *= -1;
    renderSignS2();
}
function renderSignS2() {
    const a = parseInt(document.getElementById("c8c5s2-a").value);
    document.getElementById("c8c5s2-av").textContent = a;
    let html = "", total = 0, expr = [];
    for (let i = 0; i < 4; i++) {
        const num = a + i;
        const s = signsS2[i];
        total += s * num;
        expr.push((s > 0 ? "+" : "−") + num);
        html += `<button onclick="flipSignS2(${i})" class="p-2 rounded-xl border font-bold ${s > 0 ? "bg-emerald-900/50 border-emerald-500 text-emerald-200" : "bg-rose-900/50 border-rose-500 text-rose-200"}">
            ${s > 0 ? "+" : "−"} ${num}<div class="text-[9px] font-normal text-slate-400">Click to Flip</div></button>`;
    }
    document.getElementById("c8c5s2-btns").innerHTML = html;
    document.getElementById("c8c5s2-badge").textContent = "Sum: " + total + " (EVEN)";
    document.getElementById("c8c5s2-res").textContent = expr.join(" ") + " = " + total + "  —  Always EVEN (2 Odds + 2 Evens combine into EVEN across ALL 16 flips!)";
}
renderSignS2();
</script>
"""

# Simulator 3: Parity Invariance Proof (±2b Shift & Breaking Even Rules)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚖️</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">Parity Invariance &amp; Breaking Even Expression Tester</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c5s3-badge">Δ = −2b (EVEN)</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Term Flipped (+b → −b):</span><span class="font-bold text-cyan-300" id="c8c5s3-bv">b = 7</span></div>
            <input type="range" min="1" max="20" step="1" value="7" id="c8c5s3-b" oninput="updC8C5S3()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Variable x (for x² + 3):</span><span class="font-bold text-amber-300" id="c8c5s3-xv">x = 4</span></div>
            <input type="range" min="1" max="15" step="1" value="4" id="c8c5s3-x" oninput="updC8C5S3()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-emerald-300 font-bold" id="c8c5s3-shift"></div>
        <div class="text-cyan-200 font-bold" id="c8c5s3-expr"></div>
    </div>
</div>

<script>
function updC8C5S3() {
    const b = parseInt(document.getElementById("c8c5s3-b").value);
    const x = parseInt(document.getElementById("c8c5s3-x").value);
    const x2p3 = x * x + 3;
    document.getElementById("c8c5s3-bv").textContent = "b = " + b;
    document.getElementById("c8c5s3-xv").textContent = "x = " + x;
    document.getElementById("c8c5s3-badge").textContent = "Δ = −" + (2 * b) + " (EVEN)";
    document.getElementById("c8c5s3-shift").textContent = "Sign Flip Shift: (+b) − (−b) = 2×" + b + " = " + (2 * b) + " (ALWAYS EVEN → Parity NEVER Changes!)";
    document.getElementById("c8c5s3-expr").textContent = "x² + 3 = " + x + "² + 3 = " + x2p3 + " (" + (x2p3 % 2 === 0 ? "EVEN because x is ODD" : "ODD because x is EVEN") + ")   |   4m + 2q = Always EVEN";
}
updC8C5S3();
</script>
"""

# Simulator 4: Pairs to Make Fours (4p vs 4p+2 Classifier)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">4️⃣</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Pairs to Make Fours Lab (4p vs 4p + 2 Modulo 4)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c5s4-badge">Sum: 20 (÷4 ✓)</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Even #1 (E₁):</span><span class="font-bold text-cyan-300" id="c8c5s4-e1v">6</span></div>
            <input type="range" min="2" max="40" step="2" value="6" id="c8c5s4-e1" oninput="updC8C5S4()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Even #2 (E₂):</span><span class="font-bold text-amber-300" id="c8c5s4-e2v">14</span></div>
            <input type="range" min="2" max="40" step="2" value="14" id="c8c5s4-e2" oninput="updC8C5S4()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-cyan-200" id="c8c5s4-types"></div>
        <div class="font-bold text-sm" id="c8c5s4-sum"></div>
    </div>
</div>

<script>
function updC8C5S4() {
    const e1 = parseInt(document.getElementById("c8c5s4-e1").value);
    const e2 = parseInt(document.getElementById("c8c5s4-e2").value);
    const s = e1 + e2;
    const t1 = e1 % 4 === 0 ? "4p (rem 0)" : "4p+2 (rem 2)";
    const t2 = e2 % 4 === 0 ? "4q (rem 0)" : "4q+2 (rem 2)";
    const ok = s % 4 === 0;
    document.getElementById("c8c5s4-e1v").textContent = e1;
    document.getElementById("c8c5s4-e2v").textContent = e2;
    document.getElementById("c8c5s4-badge").textContent = "Sum: " + s + (ok ? " (÷4 ✓)" : " (rem 2 ✗)");
    document.getElementById("c8c5s4-types").textContent = e1 + " is " + t1 + "   +   " + e2 + " is " + t2;
    const sumEl = document.getElementById("c8c5s4-sum");
    sumEl.className = "font-bold text-sm " + (ok ? "text-emerald-300" : "text-rose-300");
    sumEl.textContent = e1 + " + " + e2 + " = " + s + (ok ? " → DIVISIBLE BY 4! (Same bucket pair: 0+0=0 or 2+2=4)" : " → Leaves Remainder 2 (Mixed 4p with 4q+2!)");
}
updC8C5S4();
</script>
"""

# Simulator 5: Divisibility By Eight (Always, Sometimes, Never Counterexample Lab)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔍</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Always, Sometimes, or Never: Divisibility by 8 Splitter</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c5s5-badge">Sum = 24 (8×3)</span>
    </div>

    <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <button onclick="setSplitS5(16, 8)" class="px-2.5 py-1 rounded-lg bg-emerald-700 text-white font-bold">16 + 8 = 24 (Both 8k)</button>
        <button onclick="setSplitS5(11, 13)" class="px-2.5 py-1 rounded-lg bg-amber-700 text-white font-bold">11 + 13 = 24 (Neither 8k!)</button>
        <button onclick="setSplitS5(24, 15)" class="px-2.5 py-1 rounded-lg bg-rose-700 text-white font-bold">24 + 15 = 39 (8k + Non-8k)</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-amber-300 font-bold" id="c8c5s5-res"></div>
        <div class="text-cyan-200" id="c8c5s5-rule"></div>
    </div>
</div>

<script>
function setSplitS5(a, b) {
    const s = a + b;
    const da = a % 8 === 0, db = b % 8 === 0, ds = s % 8 === 0;
    document.getElementById("c8c5s5-badge").textContent = a + " + " + b + " = " + s;
    document.getElementById("c8c5s5-res").textContent = a + " (mod 8 = " + (a % 8) + ")  +  " + b + " (mod 8 = " + (b % 8) + ")  =  " + s + (ds ? " (Divisible by 8! ✓)" : " (NOT divisible by 8! ✗)");
    document.getElementById("c8c5s5-rule").textContent = (da && db)
        ? "ALWAYS TRUE: 8a + 8b = 8(a + b) ALWAYS divides by 8!"
        : (ds ? "SOMETIMES Counterexample: sum 24 divides by 8 even though 11 & 13 do NOT!"
              : "NEVER Rule: 8(multiple) + (non-multiple) can NEVER divide by 8!");
}
setSplitS5(11, 13);
</script>
"""

# Simulator 6: Factors And LCM (Divisibility Inheritance + LCM(k, m) Rule)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔗</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">LCM(k, m) Guaranteed Divisor &amp; Factor Inheritance Lab</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c5s6-badge">LCM(6, 9) = 18</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Divisor k:</span><span class="font-bold text-cyan-300" id="c8c5s6-kv">6</span></div>
            <input type="range" min="2" max="15" step="1" value="6" id="c8c5s6-k" oninput="updC8C5S6()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Divisor m:</span><span class="font-bold text-amber-300" id="c8c5s6-mv">9</span></div>
            <input type="range" min="2" max="15" step="1" value="9" id="c8c5s6-m" oninput="updC8C5S6()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-emerald-300 font-bold text-sm" id="c8c5s6-lcm"></div>
        <div class="text-amber-200" id="c8c5s6-trap"></div>
    </div>
</div>

<script>
function gcdS6(a, b) { return b === 0 ? a : gcdS6(b, a % b); }
function updC8C5S6() {
    const k = parseInt(document.getElementById("c8c5s6-k").value);
    const m = parseInt(document.getElementById("c8c5s6-m").value);
    const g = gcdS6(k, m);
    const lcm = (k * m) / g;
    document.getElementById("c8c5s6-kv").textContent = k;
    document.getElementById("c8c5s6-mv").textContent = m;
    document.getElementById("c8c5s6-badge").textContent = "LCM(" + k + ", " + m + ") = " + lcm;
    document.getElementById("c8c5s6-lcm").textContent = "Guaranteed Divisor = LCM(" + k + ", " + m + ") = " + lcm + " (HCF = " + g + ")";
    document.getElementById("c8c5s6-trap").textContent = g === 1
        ? "Coprime Pair (HCF = 1)! Divisibility by " + k + " & " + m + " guarantees product " + (k * m) + "!"
        : "Non-Coprime (HCF = " + g + ")! Counterexample N = " + lcm + " passes " + k + " & " + m + ", yet FAILS product " + (k * m) + "!";
}
updC8C5S6();
</script>
"""

# Simulator 7: What Remains Modulo (Dual Algebraic Remainder Forms 5k+3 = 5m-2)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌀</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">What Remains? Forward (dk + r) &amp; Deficit (dm − gap) Formulas</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c5s7-badge">5k + 3 = 5m − 2</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Divisor (d):</span><span class="font-bold text-cyan-300" id="c8c5s7-dv">5</span></div>
            <input type="range" min="3" max="12" step="1" value="5" id="c8c5s7-d" oninput="updC8C5S7()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Remainder (r):</span><span class="font-bold text-amber-300" id="c8c5s7-rv">3</span></div>
            <input type="range" min="1" max="11" step="1" value="3" id="c8c5s7-r" oninput="updC8C5S7()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-emerald-300 font-bold text-sm" id="c8c5s7-eq"></div>
        <div class="text-cyan-200" id="c8c5s7-seq"></div>
    </div>
</div>

<script>
function updC8C5S7() {
    const d = parseInt(document.getElementById("c8c5s7-d").value);
    const rSlider = document.getElementById("c8c5s7-r");
    let r = parseInt(rSlider.value);
    if (r >= d) { r = d - 1; rSlider.value = r; }
    const def = d - r;
    let seq = [];
    for (let k = 0; k < 5; k++) seq.push(d * k + r);

    document.getElementById("c8c5s7-dv").textContent = d;
    document.getElementById("c8c5s7-rv").textContent = r;
    document.getElementById("c8c5s7-badge").textContent = d + "k+" + r + " = " + d + "m−" + def;
    document.getElementById("c8c5s7-eq").textContent = "Equivalent Expressions:  " + d + "k + " + r + "   ≡   " + d + "m − " + def;
    document.getElementById("c8c5s7-seq").textContent = "Generated Sequence: " + seq.join(", ") + ", ...";
}
updC8C5S7();
</script>
"""

# Simulator 8: Last Digits Shortcuts (Place-Value Decomposition Scanner for 2, 4, 8, 5, 10)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚡</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Place-Value Tail Scanner (Divisibility by 2, 4, 8, 5, 10)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c5s8-badge">7,354,912</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Change Last 3 Digits (000 to 999) of 7,354,XXX:</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c5s8-tv">912</span>
        </div>
        <input type="range" min="100" max="999" step="1" value="912" id="c8c5s8-t" oninput="updC8C5S8()" class="w-full accent-amber-400">
    </div>

    <div class="grid grid-cols-5 gap-1.5 text-center font-mono text-xs" id="c8c5s8-grid"></div>
</div>

<script>
function updC8C5S8() {
    const tail = parseInt(document.getElementById("c8c5s8-t").value);
    const full = 7354000 + tail;
    const d1 = tail % 10, d2 = tail % 100;
    const checks = [
        ["÷2 (Last 1)", d1 % 2 === 0],
        ["÷4 (Last 2)", d2 % 4 === 0],
        ["÷8 (Last 3)", tail % 8 === 0],
        ["÷5 (Last 1)", d1 % 5 === 0],
        ["÷10 (End 0)", d1 === 0]
    ];
    document.getElementById("c8c5s8-tv").textContent = tail;
    document.getElementById("c8c5s8-badge").textContent = full.toLocaleString("en-IN");
    let html = "";
    for (const [lbl, ok] of checks) {
        html += `<div class="p-2 rounded-xl border ${ok ? "bg-emerald-950/60 border-emerald-500 text-emerald-200" : "bg-slate-900 border-slate-800 text-slate-500"}">
            <div class="text-[10px] font-bold">${lbl}</div>
            <div class="text-sm font-black mt-0.5">${ok ? "YES ✓" : "NO ✗"}</div>
        </div>`;
    }
    document.getElementById("c8c5s8-grid").innerHTML = html;
}
updC8C5S8();
</script>
"""

if __name__ == "__main__":
    print(f"Prepared {len(simulators_part1)} interactive simulators (Part 1).")
