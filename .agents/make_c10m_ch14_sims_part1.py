#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 14: Probability
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Monte Carlo Experimental -> Theoretical Coin Convergence Lab
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪙</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Experimental → Theoretical Convergence Simulator</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c14s1-badge">Theoretical = 0.500</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="tossCoinsS1(10)" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs">Toss +10</button>
        <button onclick="tossCoinsS1(100)" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs">Toss +100</button>
        <button onclick="tossCoinsS1(1000)" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs">Toss +1,000</button>
        <button onclick="resetCoinsS1()" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold text-xs border border-slate-700">Reset</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2">
        <div class="flex justify-between text-slate-300"><span id="c14s1-counts">Heads: 0  |  Total Tosses: 0</span><span class="text-amber-300 font-bold" id="c14s1-diff">Diff from 0.5: —</span></div>
        <div class="w-full h-4 bg-slate-900 rounded-full overflow-hidden border border-slate-700 relative">
            <div class="h-full bg-gradient-to-r from-cyan-500 to-emerald-400 transition-all duration-300" id="c14s1-bar" style="width: 50%"></div>
            <div class="absolute top-0 bottom-0 left-1/2 w-0.5 bg-amber-300"></div>
        </div>
        <div class="text-emerald-300 font-bold text-sm" id="c14s1-res">Click a button to toss unbiased coins and watch P(H) converge toward 0.500!</div>
    </div>
</div>

<script>
let c14H = 0, c14N = 0;
function tossCoinsS1(k) {
    for (let i = 0; i < k; i++) {
        if (Math.random() < 0.5) c14H++;
        c14N++;
    }
    const p = c14H / c14N;
    document.getElementById("c14s1-counts").textContent = `Heads: ${c14H}  |  Total Tosses: ${c14N}`;
    document.getElementById("c14s1-diff").textContent = `Diff from 0.5: ${Math.abs(p - 0.5).toFixed(4)}`;
    document.getElementById("c14s1-bar").style.width = (p * 100).toFixed(2) + "%";
    document.getElementById("c14s1-res").textContent = `Experimental P(Head) = ${c14H}/${c14N} = ${p.toFixed(4)}  (Laplace Theoretical = 0.5000)`;
}
function resetCoinsS1() {
    c14H = 0; c14N = 0;
    document.getElementById("c14s1-counts").textContent = "Heads: 0  |  Total Tosses: 0";
    document.getElementById("c14s1-diff").textContent = "Diff from 0.5: —";
    document.getElementById("c14s1-bar").style.width = "50%";
    document.getElementById("c14s1-res").textContent = "Toss coins repeatedly to watch Experimental Probability converge to 0.5000!";
}
</script>
"""

# Simulator 2: Equally Likely Symmetry Audit (Ex 14.1 Q2)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚖️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Equally Likely Experiment Checker (Ex 14.1 Q2)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Symmetry Check</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC14S2(0)" id="btn-142-0" class="p-2 rounded-xl bg-rose-600 text-white font-bold text-xs">Car Starts vs Fails</button>
        <button onclick="pickC14S2(1)" id="btn-142-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Basketball Shot</button>
        <button onclick="pickC14S2(2)" id="btn-142-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Blind True/False</button>
        <button onclick="pickC14S2(3)" id="btn-142-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Fair Coin / Die</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2" id="c14s2-box"></div>
</div>

<script>
function pickC14S2(idx) {
    for (let k = 0; k < 4; k++) {
        const activeColor = k < 2 ? "bg-rose-600" : "bg-emerald-600";
        document.getElementById("btn-142-" + k).className = k === idx
            ? `p-2 rounded-xl ${activeColor} text-white font-bold text-xs`
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const msgs = [
        `<div class="text-rose-300 font-bold">✗ NOT EQUALLY LIKELY!</div><div class="text-slate-200">Starting depends on engine, battery & fuel condition — Laplace ratio 1/2 does NOT apply!</div>`,
        `<div class="text-rose-300 font-bold">✗ NOT EQUALLY LIKELY!</div><div class="text-slate-200">Scoring depends on skill, distance & defenders — NOT a 50-50 unbiased coin!</div>`,
        `<div class="text-emerald-300 font-bold">✓ EQUALLY LIKELY!</div><div class="text-slate-200">Blind guessing between True and False gives symmetric 1/2 = 0.5 probability each!</div>`,
        `<div class="text-emerald-300 font-bold">✓ EQUALLY LIKELY!</div><div class="text-slate-200">Unbiased coin (1/2 each) or fair symmetric 6-faced die (1/6 each) satisfies Laplace's rule!</div>`
    ];
    document.getElementById("c14s2-box").innerHTML = msgs[idx];
}
pickC14S2(0);
</script>
"""

# Simulator 3: Probability Bounds 0 ≤ P(E) ≤ 1 Meter (Ex 14.1 Q4 & Q6)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📏</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Probability Scale Validator (0 ≤ P(E) ≤ 1)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Axioms Guard</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="pickC14S3(0)" id="btn-143-0" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs">P = 0 (Impossible)</button>
        <button onclick="pickC14S3(1)" id="btn-143-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">P = 1 (Sure)</button>
        <button onclick="pickC14S3(2)" id="btn-143-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">−1.5 (Invalid!)</button>
        <button onclick="pickC14S3(3)" id="btn-143-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">15% (Valid 0.15)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2" id="c14s3-box"></div>
</div>

<script>
function pickC14S3(idx) {
    for (let k = 0; k < 4; k++) {
        document.getElementById("btn-143-" + k).className = k === idx
            ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const msgs = [
        `<div class="text-cyan-300 font-bold">P(E) = 0: Impossible Event (e.g., orange candy from lemon-only bag, Ex 14.1 Q6)</div><div class="text-emerald-300">Valid Lower Boundary: Zero favourable outcomes.</div>`,
        `<div class="text-emerald-300 font-bold">P(E) = 1: Sure / Certain Event (e.g., lemon candy from lemon-only bag)</div><div class="text-cyan-300">Valid Upper Boundary: Every outcome is favourable.</div>`,
        `<div class="text-rose-300 font-bold">✗ REJECTED: −1.5 CANNOT BE A PROBABILITY! (Ex 14.1 Q4)</div><div class="text-amber-300">No probability can ever be negative (< 0) or exceed 1 (> 100%).</div>`,
        `<div class="text-emerald-300 font-bold">✓ VALID: 15% = 15 / 100 = 0.15 (Sits cleanly inside [0, 1]!)</div><div class="text-cyan-300">Same holds for 2/3 ≈ 0.67 and 0.7!</div>`
    ];
    document.getElementById("c14s3-box").innerHTML = msgs[idx];
}
pickC14S3(0);
</script>
"""

# Simulator 4: Complementary Events Slider (P(E) + P(not E) = 1)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌗</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Complement Conservation Lab (P(Ē) = 1 − P(E))</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Sum = 1.000</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Adjust Event Probability P(E) (Ex 14.1 Q5 = 0.05):</span><span class="font-bold text-cyan-300" id="c14s4-pv">0.050</span></div>
        <input type="range" min="0" max="1" step="0.01" value="0.05" id="c14s4-p" oninput="updC14S4()" class="w-full accent-cyan-400">
    </div>

    <div class="grid grid-cols-2 gap-2 font-mono text-xs">
        <div class="bg-slate-950 p-3 rounded-xl border border-cyan-800 text-cyan-200 font-bold" id="c14s4-e"></div>
        <div class="bg-slate-950 p-3 rounded-xl border border-emerald-800 text-emerald-200 font-bold" id="c14s4-ne"></div>
    </div>
    <div class="grid grid-cols-3 gap-2">
        <button onclick="setCompS4(0.05)" class="p-1.5 rounded-lg bg-slate-900 text-amber-300 text-xs font-bold border border-slate-700">Q5 (0.05)</button>
        <button onclick="setCompS4(0.62)" class="p-1.5 rounded-lg bg-slate-900 text-amber-300 text-xs font-bold border border-slate-700">Ex 4 Tennis (0.62)</button>
        <button onclick="setCompS4(0.992)" class="p-1.5 rounded-lg bg-slate-900 text-amber-300 text-xs font-bold border border-slate-700">Q7 Birthday (0.992)</button>
    </div>
</div>

<script>
function setCompS4(v) {
    document.getElementById("c14s4-p").step = "0.001";
    document.getElementById("c14s4-p").value = v;
    updC14S4();
}
function updC14S4() {
    const p = parseFloat(document.getElementById("c14s4-p").value);
    const q = 1 - p;
    document.getElementById("c14s4-pv").textContent = p.toFixed(3);
    document.getElementById("c14s4-e").textContent = `P(E) = ${p.toFixed(3)}`;
    document.getElementById("c14s4-ne").textContent = `P(not E) = 1 − ${p.toFixed(3)} = ${q.toFixed(3)}`;
}
updC14S4();
</script>
"""

# Simulator 5: Single Die Face Highlighter & Prime Trap (1 is NOT prime!)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎲</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Single Fair Die & Prime-1 Trap Explorer (Ex 14.1 Q13)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Total = 6 Faces</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="pickC14S5(0)" id="btn-145-0" class="p-2 rounded-xl bg-rose-600 text-white font-bold text-xs">Prime {2,3,5}</button>
        <button onclick="pickC14S5(1)" id="btn-145-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Between 2 & 6</button>
        <button onclick="pickC14S5(2)" id="btn-145-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Greater Than 4</button>
        <button onclick="pickC14S5(3)" id="btn-145-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Odd Number</button>
    </div>

    <div class="flex justify-center gap-3 py-1" id="c14s5-dice"></div>
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs text-emerald-300 font-bold text-center" id="c14s5-info"></div>
</div>

<script>
function pickC14S5(mode) {
    for (let k = 0; k < 4; k++) {
        document.getElementById("btn-145-" + k).className = k === mode
            ? "p-2 rounded-xl bg-rose-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const sets = [[2,3,5], [3,4,5], [5,6], [1,3,5]];
    const texts = [
        "Primes = {2, 3, 5} → 3/6 = 1/2! (Warning: 1 is NEITHER prime NOR composite!)",
        "Strictly between 2 and 6 = {3, 4, 5} → 3/6 = 1/2! (Excludes 2 and 6!)",
        "Greater than 4 = {5, 6} → 2/6 = 1/3! (Complement ≤ 4 = 4/6 = 2/3)",
        "Odd Faces = {1, 3, 5} → 3/6 = 1/2!"
    ];
    const fav = sets[mode];
    let html = "";
    for (let d = 1; d <= 6; d++) {
        const hit = fav.includes(d);
        html += `<div class="w-10 h-10 rounded-xl flex items-center justify-center font-extrabold text-sm border ${hit ? "bg-emerald-500/30 border-emerald-400 text-emerald-200 scale-105" : "bg-slate-900 border-slate-700 text-slate-500"}">${d}</div>`;
    }
    document.getElementById("c14s5-dice").innerHTML = html;
    document.getElementById("c14s5-info").textContent = texts[mode];
}
pickC14S5(0);
</script>
"""

# Simulator 6: Two-Coin & Three-Coin Sample Space Tree (Debunking 1/3 Fallacy)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪙</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">2-Coin & 3-Coin Sample Space Hierarchy (Ex 7 & Ex 14.1 Q23)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">HT ≠ TH!</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC14S6(2)" id="btn-146-2" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs">2 Coins (2² = 4 Outcomes)</button>
        <button onclick="pickC14S6(3)" id="btn-146-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">3 Coins (2³ = 8 Outcomes)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2" id="c14s6-box"></div>
</div>

<script>
function pickC14S6(n) {
    document.getElementById("btn-146-2").className = n === 2
        ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-146-3").className = n === 3
        ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const box = document.getElementById("c14s6-box");
    if (n === 2) {
        box.innerHTML = `<div class="text-cyan-300 font-bold">Sample Space (4 outcomes): { HH, HT, TH, TT }</div>
            <div class="text-rose-300">✗ Why 1/3 Claim Fails: "1 of each" splits across BOTH HT and TH (2/4 = 1/2)!</div>
            <div class="text-emerald-300 font-bold">✓ P(at least 1 Head) = {HH, HT, TH} = 3/4! | P(exactly 1 Head) = 2/4 = 1/2</div>`;
    } else {
        box.innerHTML = `<div class="text-cyan-300 font-bold">Sample Space (8 outcomes): { HHH, HHT, HTH, THH, TTT, TTH, THT, HTT }</div>
            <div class="text-emerald-300 font-bold">Ex 14.1 Q23 Game: Win ONLY on all identical {HHH, TTT} = 2/8 = 1/4</div>
            <div class="text-amber-300 font-bold">P(Lose) = 1 − 1/4 = 3/4 (6 mixed outcomes!)</div>`;
    }
}
pickC14S6(2);
</script>
"""

# Simulator 7: Interactive 6×6 Two-Dice Matrix (36 Ordered Pairs, Sum Pyramid)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎲</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Two-Dice 6×6 Ordered Grid Explorer (36 Pairs)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c14s7-badge">Sum 7 = 6/36 (1/6)</span>
    </div>

    <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Highlight Target Sum (2 to 12, Peak at Sum 7!):</span><span class="font-bold text-amber-300" id="c14s7-sv">Sum = 7</span></div>
        <input type="range" min="2" max="12" step="1" value="7" id="c14s7-s" oninput="updC14S7()" class="w-full accent-amber-400">
    </div>

    <div class="grid grid-cols-6 gap-1 max-w-xs mx-auto font-mono text-[10px]" id="c14s7-grid"></div>
    <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 font-mono text-xs text-emerald-300 font-bold text-center" id="c14s7-res"></div>
</div>

<script>
function updC14S7() {
    const target = parseInt(document.getElementById("c14s7-s").value, 10);
    document.getElementById("c14s7-sv").textContent = "Sum = " + target;
    let html = "", cnt = 0;
    for (let r = 1; r <= 6; r++) {
        for (let c = 1; c <= 6; c++) {
            const hit = (r + c === target);
            if (hit) cnt++;
            html += `<div class="p-1 rounded text-center border ${hit ? "bg-amber-500/40 border-amber-400 text-white font-bold" : "bg-slate-900 border-slate-800 text-slate-500"}">(${r},${c})</div>`;
        }
    }
    document.getElementById("c14s7-grid").innerHTML = html;
    document.getElementById("c14s7-badge").textContent = `Sum ${target} = ${cnt}/36`;
    document.getElementById("c14s7-res").textContent = `Favourable Pairs for Sum ${target}: ${cnt} out of 36  ⇒  P(Sum = ${target}) = ${cnt}/36 (${(cnt/36).toFixed(3)})`;
}
updC14S7();
</script>
"""

# Simulator 8: Standard 52-Card Deck Interactive Selector (Ex 14.1 Q14)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🃏</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Standard 52-Card Deck Explorer (Ex 14.1 Q14)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">4 Suits × 13 Ranks</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
        <button onclick="pickC14S8(0)" id="btn-148-0" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs">Face Card (12/52)</button>
        <button onclick="pickC14S8(1)" id="btn-148-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Red Face (6/52)</button>
        <button onclick="pickC14S8(2)" id="btn-148-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Red King (2/52)</button>
        <button onclick="pickC14S8(3)" id="btn-148-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Spade Suit (13/52)</button>
        <button onclick="pickC14S8(4)" id="btn-148-4" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Queen ♦ (1/52)</button>
        <button onclick="pickC14S8(5)" id="btn-148-5" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Not an Ace (48/52)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5" id="c14s8-box"></div>
</div>

<script>
function pickC14S8(idx) {
    for (let k = 0; k < 6; k++) {
        document.getElementById("btn-148-" + k).className = k === idx
            ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const info = [
        `<div class="text-cyan-300 font-bold">All Face Cards: J, Q, K across 4 Suits (Aces are NOT face cards!)</div><div class="text-emerald-300 font-bold">Count = 3 × 4 = 12 cards ⇒ P(Face) = 12/52 = 3/13!</div>`,
        `<div class="text-rose-300 font-bold">Red Face Cards: J♥, Q♥, K♥, J♦, Q♦, K♦</div><div class="text-emerald-300 font-bold">Count = 6 cards ⇒ P(Red Face) = 6/52 = 3/26!</div>`,
        `<div class="text-rose-300 font-bold">Red Kings: King of Hearts (K♥) & King of Diamonds (K♦)</div><div class="text-emerald-300 font-bold">Count = 2 cards ⇒ P(Red King) = 2/52 = 1/26!</div>`,
        `<div class="text-slate-200 font-bold">Spade Suit (♠): Complete 13-card black suit (A..K)</div><div class="text-emerald-300 font-bold">Count = 13 cards ⇒ P(Spade) = 13/52 = 1/4!</div>`,
        `<div class="text-rose-300 font-bold">Queen of Diamonds (Q♦): One unique named card in entire deck</div><div class="text-emerald-300 font-bold">Count = 1 card ⇒ P(Q♦) = 1/52!</div>`,
        `<div class="text-amber-300 font-bold">Not an Ace: Complement of 4 Aces (4/52 = 1/13)</div><div class="text-emerald-300 font-bold">Count = 52 − 4 = 48 cards ⇒ P(Not Ace) = 48/52 = 12/13!</div>`
    ];
    document.getElementById("c14s8-box").innerHTML = info[idx];
}
pickC14S8(0);
</script>
"""
