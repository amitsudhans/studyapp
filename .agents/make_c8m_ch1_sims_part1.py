#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 1: A Square and A Cube
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: 25-Locker Toggle Experiment (Odd Factors = Squares)
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔐</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">25-Locker Toggle Simulator (Odd Factors Stay OPEN!)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8s1-badge">Visitor: 0 / 25</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="stepLockerS1()" class="p-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs">Next Visitor (+1)</button>
        <button onclick="runAllLockersS1()" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs">Run All 25 Visitors</button>
        <button onclick="resetLockersS1()" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold text-xs border border-slate-700">Reset Closed</button>
    </div>

    <div class="grid grid-cols-5 gap-1.5 max-w-sm mx-auto font-mono text-xs" id="c8s1-grid"></div>
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs text-emerald-300 font-bold text-center" id="c8s1-info"></div>
</div>

<script>
let lockVis = 0;
let lockState = Array(26).fill(false);
let lockToggles = Array(26).fill(0);

function renderLockersS1() {
    let html = "";
    let openList = [];
    for (let i = 1; i <= 25; i++) {
        if (lockState[i]) openList.push(i);
        html += `<div class="p-1.5 rounded-lg text-center border font-bold ${lockState[i] ? "bg-emerald-500/35 border-emerald-400 text-emerald-100" : "bg-slate-900 border-slate-800 text-slate-500"}">
            #${i}<div class="text-[9px] font-normal">${lockState[i] ? "OPEN" : "shut"} (${lockToggles[i]})</div></div>`;
    }
    document.getElementById("c8s1-grid").innerHTML = html;
    document.getElementById("c8s1-badge").textContent = `Visitor: ${lockVis} / 25`;
    document.getElementById("c8s1-info").textContent = lockVis === 25
        ? `Done! Open Lockers (Odd Factors): { ${openList.join(", ")} } — ALL PERFECT SQUARES!`
        : (lockVis === 0 ? "All 25 lockers start CLOSED. Step visitors 1..25 to toggle multiples!" : `Open now: { ${openList.join(", ")} }`);
}
function stepLockerS1() {
    if (lockVis >= 25) return;
    lockVis++;
    for (let i = lockVis; i <= 25; i += lockVis) {
        lockState[i] = !lockState[i];
        lockToggles[i]++;
    }
    renderLockersS1();
}
function runAllLockersS1() {
    while (lockVis < 25) stepLockerS1();
}
function resetLockersS1() {
    lockVis = 0;
    lockState = Array(26).fill(false);
    lockToggles = Array(26).fill(0);
    renderLockersS1();
}
runAllLockersS1();
</script>
"""

# Simulator 2: Square Number Geometric Tile Grid + Decimal/Fraction Squares (Section 1.1)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🟧</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Geometric Square Tile Grid & Fractional/Decimal Lab</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8s2-badge">4² = 16 Tiles</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Side Length n (Natural Integer 1 to 10):</span><span class="font-bold text-cyan-300" id="c8s2-nv">n = 4</span></div>
        <input type="range" min="1" max="10" step="1" value="4" id="c8s2-n" oninput="updC8S2()" class="w-full accent-cyan-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 120 120" class="w-full max-h-32 bg-slate-950 rounded-xl border border-slate-800" id="c8s2-svg"></svg>
        <div class="font-mono text-xs space-y-2">
            <div class="text-emerald-300 font-bold text-sm" id="c8s2-area"></div>
            <div class="text-amber-300">Decimal Check: 0.4² = 0.16  |  1.5² = 2.25</div>
            <div class="text-purple-300">Fraction Check: (3/4)² = 9/16</div>
        </div>
    </div>
</div>

<script>
function updC8S2() {
    const n = parseInt(document.getElementById("c8s2-n").value, 10);
    document.getElementById("c8s2-nv").textContent = "n = " + n;
    document.getElementById("c8s2-badge").textContent = `${n}² = ${n*n} Tiles`;
    document.getElementById("c8s2-area").textContent = `Area of ${n}×${n} Square = ${n} × ${n} = ${n*n}`;

    const cell = Math.min(18, Math.floor(96 / n));
    const startX = (120 - n * cell) / 2, startY = (120 - n * cell) / 2;
    let tiles = "";
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            tiles += `<rect x="${startX + c*cell}" y="${startY + r*cell}" width="${cell-1.5}" height="${cell-1.5}" rx="1.5" fill="rgba(6,182,212,0.55)" stroke="#22d3ee" stroke-width="0.8"/>`;
        }
    }
    document.getElementById("c8s2-svg").innerHTML = tiles;
}
updC8S2();
</script>
"""

# Simulator 3: Instant Square Rejector by Units Digit {2,3,7,8}
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔎</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Units Digit Instant Square Tester ({2, 3, 7, 8} Banned!)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Click Any Last Digit</span>
    </div>

    <div class="grid grid-cols-5 sm:grid-cols-10 gap-1.5 font-mono text-xs" id="c8s3-btns"></div>
    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5" id="c8s3-box"></div>
</div>

<script>
function pickDigitS3(d) {
    const allowed = [0, 1, 4, 5, 6, 9];
    let html = "";
    for (let k = 0; k <= 9; k++) {
        const isSel = k === d;
        const ok = allowed.includes(k);
        html += `<button onclick="pickDigitS3(${k})" class="p-2 rounded-lg font-bold border ${isSel ? (ok ? "bg-emerald-600 border-emerald-400 text-white" : "bg-rose-600 border-rose-400 text-white") : "bg-slate-900 border-slate-700 text-slate-300"}">${k}</button>`;
    }
    document.getElementById("c8s3-btns").innerHTML = html;

    const sources = {0: "0² = 0", 1: "1²=1, 9²=81", 4: "2²=4, 8²=64", 5: "5²=25", 6: "4²=16, 6²=36", 9: "3²=9, 7²=49"};
    const box = document.getElementById("c8s3-box");
    if (allowed.includes(d)) {
        box.innerHTML = `<div class="text-emerald-300 font-bold">✓ ALLOWED SQUARE ENDING: Digit ${d} CAN end a perfect square!</div>
            <div class="text-cyan-300">Produced whenever root ends in: ${sources[d]} (remember: still verify full factors — not every ending-${d} number like ${10+d} is square!).</div>`;
    } else {
        box.innerHTML = `<div class="text-rose-300 font-bold">✗ IMPOSSIBLE SQUARE ENDING: No integer square EVER ends in ${d}!</div>
            <div class="text-amber-300">Instant Rejection: Numbers ending in {2, 3, 7, 8} are GUARANTEED NOT perfect squares!</div>`;
    }
}
pickDigitS3(7);
</script>
"""

# Simulator 4: Trailing Zeros Doubling Checker (Even Zeros + Square Front)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">0️⃣</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Trailing Zeros Even-Count & Front-Square Auditor</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">2k Trailing Zeros</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="pickC8S4(0)" id="btn-84-0" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs">19,600 (Valid)</button>
        <button onclick="pickC8S4(1)" id="btn-84-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">9,000 (Odd 3 Zeros)</button>
        <button onclick="pickC8S4(2)" id="btn-84-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">1,200 (Trap!)</button>
        <button onclick="pickC8S4(3)" id="btn-84-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">1,60,000 (Valid)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5" id="c8s4-box"></div>
</div>

<script>
function pickC8S4(idx) {
    for (let k = 0; k < 4; k++) {
        const col = (k === 0 || k === 3) ? "bg-emerald-600" : "bg-rose-600";
        document.getElementById("btn-84-" + k).className = k === idx
            ? `p-2 rounded-xl ${col} text-white font-bold text-xs`
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const msgs = [
        `<div class="text-emerald-300 font-bold">✓ 19,600 IS A PERFECT SQUARE (= 140²)!</div><div class="text-slate-200">Check 1: 2 trailing zeros (EVEN ✓). Check 2: Front part 196 = 14² (SQUARE ✓).</div>`,
        `<div class="text-rose-300 font-bold">✗ 9,000 IS NOT A PERFECT SQUARE!</div><div class="text-slate-200">Even though front 9 = 3², count of trailing zeros = 3 (ODD ✗ — squares double zeros!).</div>`,
        `<div class="text-rose-300 font-bold">✗ WATCH TRAP! 1,200 IS NOT A PERFECT SQUARE!</div><div class="text-slate-200">It has 2 trailing zeros (EVEN ✓), YET remaining front part 12 is NOT a square (✗)!</div>`,
        `<div class="text-emerald-300 font-bold">✓ 1,60,000 IS A PERFECT SQUARE (= 400²)!</div><div class="text-slate-200">4 trailing zeros (EVEN ✓) AND front 16 = 4² (SQUARE ✓)!</div>`
    ];
    document.getElementById("c8s4-box").innerHTML = msgs[idx];
}
pickC8S4(0);
</script>
"""

# Simulator 5: Consecutive Odd Sums Gnomon Builder & Successive Subtraction Stepper
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">➕</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Odd-Sum Square Builder & Successive Subtraction Lab</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8s5-badge">n = 7 → 49</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Number of Consecutive Odd Layers n (1 to 10):</span><span class="font-bold text-emerald-300" id="c8s5-nv">7 odd layers</span></div>
        <input type="range" min="1" max="10" step="1" value="7" id="c8s5-n" oninput="updC8S5()" class="w-full accent-emerald-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2">
        <div class="text-cyan-300" id="c8s5-sum"></div>
        <div class="text-amber-300 font-bold" id="c8s5-sub"></div>
    </div>
</div>

<script>
function updC8S5() {
    const n = parseInt(document.getElementById("c8s5-n").value, 10);
    const odds = Array.from({length: n}, (_, i) => 2 * i + 1);
    const sq = n * n;
    document.getElementById("c8s5-nv").textContent = `${n} odd layers`;
    document.getElementById("c8s5-badge").textContent = `n = ${n} → ${sq}`;
    document.getElementById("c8s5-sum").textContent = `Sum: ${odds.join(" + ")} = ${n}² = ${sq}`;
    document.getElementById("c8s5-sub").textContent = `Successive Subtraction: Subtracting [${odds.join(", ")}] from ${sq} hits EXACT 0 in ${n} steps ⇒ √${sq} = ${n}!`;
}
updC8S5();
</script>
"""

# Simulator 6: Triangular Number Sums (T_{n-1} + T_n = n²) & 2n Non-Squares Visualizer
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔺</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Consecutive Triangular Sum Lab (Tₙ₋₁ + Tₙ = n²)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800" id="c8s6-badge">6 + 10 = 16</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Square Size n (2 to 8):</span><span class="font-bold text-purple-300" id="c8s6-nv">n = 4 (Square = 16)</span></div>
        <input type="range" min="2" max="8" step="1" value="4" id="c8s6-n" oninput="updC8S6()" class="w-full accent-purple-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 120 120" class="w-full max-h-32 bg-slate-950 rounded-xl border border-slate-800" id="c8s6-svg"></svg>
        <div class="font-mono text-xs space-y-2">
            <div class="text-cyan-300 font-bold" id="c8s6-tri"></div>
            <div class="text-emerald-300 font-bold" id="c8s6-gap"></div>
        </div>
    </div>
</div>

<script>
function updC8S6() {
    const n = parseInt(document.getElementById("c8s6-n").value, 10);
    const tPrev = (n - 1) * n / 2;
    const tCurr = n * (n + 1) / 2;
    document.getElementById("c8s6-nv").textContent = `n = ${n} (Square = ${n*n})`;
    document.getElementById("c8s6-badge").textContent = `${tPrev} + ${tCurr} = ${n*n}`;
    document.getElementById("c8s6-tri").textContent = `T_${n-1} (${tPrev}) + T_${n} (${tCurr}) = ${n}² = ${n*n}!`;
    document.getElementById("c8s6-gap").textContent = `Non-squares strictly between ${n}² (${n*n}) and ${n+1}² (${(n+1)*(n+1)}) = 2×${n} = ${2*n} numbers!`;

    const cell = Math.floor(90 / n), sx = (120 - n * cell) / 2, sy = (120 - n * cell) / 2;
    let dots = "";
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            const isUpper = c > r;
            dots += `<circle cx="${sx + c*cell + cell/2}" cy="${sy + r*cell + cell/2}" r="${Math.max(3, cell*0.32)}" fill="${isUpper ? "#fbbf24" : "#22d3ee"}"/>`;
        }
    }
    document.getElementById("c8s6-svg").innerHTML = dots;
}
updC8S6();
</script>
"""

# Simulator 7: Square Root Estimation (Tens Landmarks + Units Filter)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">√</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Square Root Interval Estimator & Principal Radical Lab</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Positive √y</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="pickC8S7(529)" id="btn-87-529" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs">√529</button>
        <button onclick="pickC8S7(784)" id="btn-87-784" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">√784</button>
        <button onclick="pickC8S7(1369)" id="btn-87-1369" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">√1,369</button>
        <button onclick="pickC8S7(2025)" id="btn-87-2025" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">√2,025</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5" id="c8s7-box"></div>
</div>

<script>
function pickC8S7(val) {
    for (const k of [529, 784, 1369, 2025]) {
        document.getElementById("btn-87-" + k).className = k === val
            ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const data = {
        529: ["20² (400) < 529 < 25² (625)", "Ends in 9 ⇒ candidate ending 3 or 7", "√529 = 23 (and two integer roots are +23, −23)!"],
        784: ["25² (625) < 784 < 30² (900)", "Ends in 4 ⇒ candidate > 25 ending in 2 or 8", "√784 = 28 (check: 28×28 = 784)!"],
        1369: ["35² (1225) < 1,369 < 40² (1600)", "Ends in 9 ⇒ candidate > 35 ending in 3 or 7", "√1,369 = 37!"],
        2025: ["40² (1600) < 2,025 < 50² (2500)", "Ends in 5 ⇒ ONLY units digit 5 fits!", "√2,025 = 45 (shortcut: 4 × 5 = 20 → 2025)!"]
    };
    const [b1, b2, b3] = data[val];
    document.getElementById("c8s7-box").innerHTML = `<div class="text-cyan-300 font-bold">Step 1 (Landmark Bounds): ${b1}</div>
        <div class="text-amber-300">Step 2 (Units Filter): ${b2}</div>
        <div class="text-emerald-300 font-bold text-sm">Step 3 (Exact Principal Root): ${b3}</div>`;
}
pickC8S7(529);
</script>
"""

# Simulator 8: Prime Factorization Pairing & Unpaired Factor Repair
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧬</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Prime Factorization Pairing Machine (Exact vs Repair)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Equal Pairs</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickC8S8(0)" id="btn-88-0" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs">324 → 18</button>
        <button onclick="pickC8S8(1)" id="btn-88-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">1,764 → 42</button>
        <button onclick="pickC8S8(2)" id="btn-88-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">180 (Repair ×5/÷5)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5" id="c8s8-box"></div>
</div>

<script>
function pickC8S8(idx) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-88-" + k).className = k === idx
            ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const msgs = [
        `<div class="text-cyan-300 font-bold">324 = (2 × 2) × (3 × 3) × (3 × 3)</div><div class="text-emerald-300 font-bold text-sm">Pull 1 factor per pair: √324 = 2 × 3 × 3 = 18!</div>`,
        `<div class="text-cyan-300 font-bold">1,764 = (2 × 2) × (3 × 3) × (7 × 7)</div><div class="text-emerald-300 font-bold text-sm">Pull 1 factor per pair: √1,764 = 2 × 3 × 7 = 42!</div>`,
        `<div class="text-rose-300 font-bold">180 = (2 × 2) × (3 × 3) × [ 5 lonely! ]</div>
         <div class="text-amber-300">Multiply by 5 → 900 (√900 = 30)  |  OR Divide by 5 → 36 (√36 = 6)!</div>`
    ];
    document.getElementById("c8s8-box").innerHTML = msgs[idx];
}
pickC8S8(0);
</script>
"""
