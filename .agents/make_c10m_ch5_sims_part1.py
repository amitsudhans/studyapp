#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 5: Arithmetic Progressions
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Patterns Around Us (Salary, Ladder, Fibonacci vs Unit Squares)
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌿</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Pattern Detective Lab: Constant Step vs Varying Step (Section 5.1)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="pat-badge">AP: Constant Step!</span>
    </div>

    <p class="text-xs text-slate-300">Compare real-world sequences! Click any pattern to inspect consecutive differences between adjacent terms.</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectPattern51(0)" id="btn-pat-0" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Salary Raise (+500)</button>
        <button onclick="selectPattern51(1)" id="btn-pat-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ladder Rungs (-2 cm)</button>
        <button onclick="selectPattern51(2)" id="btn-pat-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Fibonacci (Rabbits)</button>
        <button onclick="selectPattern51(3)" id="btn-pat-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Unit Squares (n^2)</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 115" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="pat-svg">
            <text x="180" y="22" fill="#fcd34d" font-size="11" font-weight="bold" text-anchor="middle" id="pat-svg-title">Office Annual Salary: 8000, 8500, 9000, 9500, 10000</text>
            <g id="pat-svg-nodes"></g>
        </svg>

        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-1 text-xs font-mono">
            <div class="text-cyan-300" id="pat-diffs">Differences: 8500 - 8000 = +500 | 9000 - 8500 = +500 | 9500 - 9000 = +500</div>
            <div class="text-emerald-300 font-bold" id="pat-verdict">Verdict: CONSTANT step (+500) -> Forms a valid Arithmetic Progression!</div>
        </div>
    </div>
</div>

<script>
const patData51 = [
    {
        title: "Annual Salary: 8000, 8500, 9000, 9500, 10000",
        terms: [8000, 8500, 9000, 9500, 10000],
        diffs: ["+500", "+500", "+500", "+500"],
        badge: "AP: Constant Step!",
        verdict: "Verdict: CONSTANT addition (+500) at every step -> Valid Arithmetic Progression!",
        isAp: true
    },
    {
        title: "Wooden Ladder Rungs (cm): 45, 43, 41, 39, 37",
        terms: [45, 43, 41, 39, 37],
        diffs: ["-2", "-2", "-2", "-2"],
        badge: "AP: Constant Step!",
        verdict: "Verdict: CONSTANT step (-2 cm) at every rung -> Valid Arithmetic Progression!",
        isAp: true
    },
    {
        title: "Rabbit Pairs (Fibonacci): 1, 1, 2, 3, 5, 8",
        terms: [1, 1, 2, 3, 5],
        diffs: ["+0", "+1", "+1", "+2"],
        badge: "NOT AP!",
        verdict: "Verdict: Differences (+0, +1, +1, +2) keep changing -> NOT an Arithmetic Progression!",
        isAp: false
    },
    {
        title: "Unit Squares Count: 1, 4, 9, 16, 25",
        terms: [1, 4, 9, 16, 25],
        diffs: ["+3", "+5", "+7", "+9"],
        badge: "NOT AP!",
        verdict: "Verdict: Odd jumps (+3, +5, +7, +9) are NOT constant -> NOT an Arithmetic Progression!",
        isAp: false
    }
];

function selectPattern51(idx) {
    for (let i = 0; i < 4; i++) {
        const b = document.getElementById("btn-pat-" + i);
        if (b) {
            b.className = (i === idx)
                ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
                : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
        }
    }
    const item = patData51[idx];
    document.getElementById("pat-badge").textContent = item.badge;
    document.getElementById("pat-svg-title").textContent = item.title;
    document.getElementById("pat-diffs").textContent = "Consecutive jumps: " + item.diffs.join("  |  ");
    const vEl = document.getElementById("pat-verdict");
    vEl.textContent = item.verdict;
    vEl.className = item.isAp ? "text-emerald-300 font-bold" : "text-rose-400 font-bold";

    let html = "";
    const xs = [36, 108, 180, 252, 324];
    for (let k = 0; k < 5; k++) {
        const col = item.isAp ? "#059669" : "#be123c";
        html += `<rect x="${xs[k]-24}" y="42" width="48" height="32" rx="6" fill="#0f172a" stroke="${col}" stroke-width="2" />`;
        html += `<text x="${xs[k]}" y="62" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">${item.terms[k]}</text>`;
        if (k < 4) {
            const mx = (xs[k] + xs[k+1]) / 2;
            html += `<path d="M ${xs[k]+18} 82 Q ${mx} 102 ${xs[k+1]-18} 82" fill="none" stroke="#38bdf8" stroke-width="1.6" />`;
            html += `<text x="${mx}" y="106" fill="#7dd3fc" font-size="10" font-weight="bold" text-anchor="middle">${item.diffs[k]}</text>`;
        }
    }
    document.getElementById("pat-svg-nodes").innerHTML = html;
}
selectPattern51(0);
</script>
"""

# Simulator 2: Common Difference d (Positive, Negative, Zero & Verification)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">➕</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">AP Generator & Sign Tester: Positive, Negative, Zero d (Section 5.2)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="sim2-type">Increasing AP</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2">
            <div class="flex justify-between text-xs"><span class="text-slate-300">First Term (a):</span><span class="font-bold text-amber-300" id="sim2-a-val">3</span></div>
            <input type="range" min="-10" max="20" value="3" id="sim2-a" oninput="updateAP52()" class="w-full accent-amber-400">
        </div>
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2">
            <div class="flex justify-between text-xs"><span class="text-slate-300">Common Difference (d):</span><span class="font-bold text-cyan-300" id="sim2-d-val">4</span></div>
            <input type="range" min="-6" max="6" value="4" id="sim2-d" oninput="updateAP52()" class="w-full accent-cyan-400">
        </div>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="presetAP52(1, 2)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">d > 0 (a=1, d=2)</button>
        <button onclick="presetAP52(20, -5)" class="p-2 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">d < 0 (a=20, d=-5)</button>
        <button onclick="presetAP52(3, 0)" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">d = 0 (3, 3, 3...)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-3">
        <div class="grid grid-cols-5 gap-2 text-center" id="sim2-boxes"></div>
        <div class="text-xs font-mono text-slate-300 pt-2 border-t border-slate-800" id="sim2-form"></div>
    </div>
</div>

<script>
function presetAP52(a, d) {
    document.getElementById("sim2-a").value = a;
    document.getElementById("sim2-d").value = d;
    updateAP52();
}
function updateAP52() {
    const a = parseInt(document.getElementById("sim2-a").value, 10);
    const d = parseInt(document.getElementById("sim2-d").value, 10);
    document.getElementById("sim2-a-val").textContent = a;
    document.getElementById("sim2-d-val").textContent = d;

    const badge = document.getElementById("sim2-type");
    if (d > 0) {
        badge.textContent = "d > 0 (Increasing AP)";
        badge.className = "text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-700";
    } else if (d < 0) {
        badge.textContent = "d < 0 (Decreasing AP)";
        badge.className = "text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-700";
    } else {
        badge.textContent = "d = 0 (Constant AP!)";
        badge.className = "text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-700";
    }

    let html = "";
    const labels = ["a", "a+d", "a+2d", "a+3d", "a+4d"];
    const vals = [];
    for (let i = 0; i < 5; i++) {
        const val = a + i * d;
        vals.push(val);
        html += `<div class="bg-slate-900 p-2 rounded-xl border border-slate-700">
            <div class="text-[10px] text-slate-400">${labels[i]}</div>
            <div class="text-sm font-bold text-white">${val}</div>
        </div>`;
    }
    document.getElementById("sim2-boxes").innerHTML = html;
    document.getElementById("sim2-form").textContent =
        "General AP: " + vals.join(", ") + ", ...  |  Verify: a2 - a1 = " + (vals[1] - vals[0]) + ", a3 - a2 = " + (vals[2] - vals[1]);
}
updateAP52();
</script>
"""

# Simulator 3: Testing Real Situations (Ex 5.1 Q1 scenarios)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🚕</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Exercise 5.1 Real-World Model Verifier (Q1 i-iv)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="sim3-badge">Valid AP!</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectCase51(0)" id="btn-c51-0" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">1. Taxi Fare</button>
        <button onclick="selectCase51(1)" id="btn-c51-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. Vacuum Pump</button>
        <button onclick="selectCase51(2)" id="btn-c51-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. Well Digging</button>
        <button onclick="selectCase51(3)" id="btn-c51-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">4. Compound Int.</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3 text-xs font-mono">
        <div class="text-amber-300 font-sans font-bold text-sm" id="sim3-title"></div>
        <div class="grid grid-cols-4 gap-2 text-center" id="sim3-terms"></div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="text-cyan-300" id="sim3-diff"></div>
            <div class="font-bold" id="sim3-result"></div>
        </div>
    </div>
</div>

<script>
const ex51Cases = [
    {
        title: "Taxi Fare: Rs 15 first km + Rs 8 every extra km",
        terms: ["km 1: Rs 15", "km 2: Rs 23", "km 3: Rs 31", "km 4: Rs 39"],
        diffs: "a2 - a1 = +8  |  a3 - a2 = +8  |  a4 - a3 = +8",
        verdict: "TRUE AP! Constant additive increase of +8 rupees per km.",
        ok: true
    },
    {
        title: "Vacuum Pump: Removes 1/4 of REMAINING air V each stroke",
        terms: ["Start: V", "S1: 3/4 V", "S2: 9/16 V", "S3: 27/64 V"],
        diffs: "a2 - a1 = -1/4 V  |  a3 - a2 = -3/16 V  (Unequal!)",
        verdict: "NOT AN AP! Multiplying by (3/4) shrinks each drop (Geometric, not AP).",
        ok: false
    },
    {
        title: "Well Digging Cost: Rs 150 first metre + Rs 50 each deeper metre",
        terms: ["1m: Rs 150", "2m: Rs 200", "3m: Rs 250", "4m: Rs 300"],
        diffs: "a2 - a1 = +50  |  a3 - a2 = +50  |  a4 - a3 = +50",
        verdict: "TRUE AP! Constant step +50 rupees per additional metre.",
        ok: true
    },
    {
        title: "Compound Interest: Rs 10,000 growing at 8% compounded yearly",
        terms: ["Y0: 10000", "Y1: 10800", "Y2: 11664", "Y3: 12597.12"],
        diffs: "Y1-Y0 = +800  |  Y2-Y1 = +864  |  Y3-Y2 = +933.12",
        verdict: "NOT AN AP! Interest accrues on larger principal each year.",
        ok: false
    }
];

function selectCase51(idx) {
    for (let i = 0; i < 4; i++) {
        const b = document.getElementById("btn-c51-" + i);
        if (b) {
            b.className = (i === idx)
                ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500"
                : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
        }
    }
    const c = ex51Cases[idx];
    document.getElementById("sim3-title").textContent = c.title;
    document.getElementById("sim3-badge").textContent = c.ok ? "Valid AP!" : "NOT an AP!";
    document.getElementById("sim3-badge").className = c.ok
        ? "text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800"
        : "text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800";
    document.getElementById("sim3-terms").innerHTML = c.terms.map(t =>
        `<div class="bg-slate-950 p-2 rounded-xl border border-slate-700 text-white font-bold">${t}</div>`
    ).join("");
    document.getElementById("sim3-diff").textContent = c.diffs;
    const r = document.getElementById("sim3-result");
    r.textContent = c.verdict;
    r.className = c.ok ? "font-bold text-emerald-300" : "font-bold text-rose-400";
}
selectCase51(0);
</script>
"""

# Simulator 4: General nth Term Explorer a_n = a + (n - 1)d
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎯</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">nth Term Builder: a_n = a + (n - 1)d (Section 5.3)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800" id="sim4-out-badge">a_30 = -77</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="presetNth(10, -3, 30)" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 5.2 Q2(i): 10,7,4.. (30th)</button>
        <button onclick="presetNth(-3, 2.5, 11)" class="p-2 rounded-xl bg-slate-900 text-cyan-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 5.2 Q2(ii): -3,-0.5.. (11th)</button>
        <button onclick="presetNth(2, 5, 10)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 3: 2, 7, 12.. (10th)</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
            <label class="text-slate-400 block mb-1">First Term a:</label>
            <input type="number" step="0.5" value="10" id="sim4-a" oninput="calcNth53()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono">
        </div>
        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
            <label class="text-slate-400 block mb-1">Common Diff d:</label>
            <input type="number" step="0.5" value="-3" id="sim4-d" oninput="calcNth53()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono">
        </div>
        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
            <label class="text-slate-400 block mb-1">Target Index n (1..50):</label>
            <input type="range" min="1" max="50" value="30" id="sim4-n" oninput="calcNth53()" class="w-full accent-purple-400 mt-1">
            <div class="text-right font-bold text-purple-300" id="sim4-n-disp">n = 30</div>
        </div>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-slate-300" id="sim4-jumps">Steps needed from Term 1: (n - 1) = 29 jumps of d = -3</div>
        <div class="text-cyan-300" id="sim4-step1">a_30 = 10 + (30 - 1) * (-3)</div>
        <div class="text-emerald-300 text-sm font-bold" id="sim4-step2">a_30 = 10 + (-87) = -77</div>
    </div>
</div>

<script>
function presetNth(a, d, n) {
    document.getElementById("sim4-a").value = a;
    document.getElementById("sim4-d").value = d;
    document.getElementById("sim4-n").value = n;
    calcNth53();
}
function calcNth53() {
    const a = parseFloat(document.getElementById("sim4-a").value) || 0;
    const d = parseFloat(document.getElementById("sim4-d").value) || 0;
    const n = parseInt(document.getElementById("sim4-n").value, 10) || 1;
    const nm1 = n - 1;
    const prod = Math.round(nm1 * d * 100) / 100;
    const ans = Math.round((a + prod) * 100) / 100;

    document.getElementById("sim4-n-disp").textContent = "n = " + n;
    document.getElementById("sim4-out-badge").textContent = "a_" + n + " = " + ans;
    document.getElementById("sim4-jumps").textContent = `Counting from Term 1 (0 steps of d): Term ${n} requires exactly (${n} - 1) = ${nm1} forward jumps!`;
    document.getElementById("sim4-step1").textContent = `Formula: a_${n} = ${a} + (${nm1}) x (${d})`;
    document.getElementById("sim4-step2").textContent = `Result:  a_${n} = ${a} + (${prod}) = ${ans}`;
}
calcNth53();
</script>
"""

# Simulator 5: Term Position & Integer Membership Verifier (78 -> 16th, 0 -> 8th, -150 rejected)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔍</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Membership Verifier: Does Target Belong? (n MUST be a Positive Integer)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="sim5-badge">n = 16 (VALID!)</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="runMemCheck(3, 5, 78)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">AP 3,8,13.. Target = 78</button>
        <button onclick="runMemCheck(21, -3, 0)" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">AP 21,18,15.. Target = 0</button>
        <button onclick="runMemCheck(11, -3, -150)" class="p-2 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">AP 11,8,5.. Target = -150</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-slate-300" id="sim5-setup">Given: a = 3, d = 5, Target a_n = 78</div>
        <div class="text-cyan-300" id="sim5-solve">78 = 3 + (n - 1)(5)  ->  n - 1 = 75 / 5 = 15  ->  n = 16</div>
        <div class="font-bold text-sm" id="sim5-verdict">VERDICT: n = 16 is a positive whole integer -> 78 IS Term 16!</div>
    </div>
</div>

<script>
function runMemCheck(a, d, target) {
    document.getElementById("sim5-setup").textContent = `Given AP parameters: a = ${a}, d = ${d}, Suspect Target = ${target}`;
    const diff = target - a;
    const rawRatio = diff / d;
    const nVal = rawRatio + 1;
    const isInt = Number.isInteger(nVal) && nVal >= 1;
    const nDisp = isInt ? nVal : nVal.toFixed(2) + " (NOT an integer!)";

    document.getElementById("sim5-solve").textContent = `${target} = ${a} + (n - 1)(${d})  =>  (${diff}) / (${d}) + 1  =>  n = ${nDisp}`;
    const b = document.getElementById("sim5-badge");
    const v = document.getElementById("sim5-verdict");
    if (isInt) {
        b.textContent = "n = " + nVal + " (VALID!)";
        b.className = "text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-700";
        v.textContent = `ACCEPTED! Since n = ${nVal} is a positive integer, ${target} IS the ${nVal}th term!`;
        v.className = "font-bold text-sm text-emerald-300";
    } else {
        b.textContent = "REJECTED! (Non-Integer)";
        b.className = "text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-700";
        v.textContent = `REJECTED! n = ${nVal.toFixed(2)} is fractional/non-positive, so ${target} NEVER occurs in this AP!`;
        v.className = "font-bold text-sm text-rose-400";
    }
}
runMemCheck(3, 5, 78);
</script>
"""

# Simulator 6: Terms From the End (Reversing Finite AP Shortcut)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔄</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Reverse AP Shortcut: kth Term From Last Term l</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="sim6-badge">11th from end = -32</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="setRevCase(10, -3, -62, 11)" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 8: 10, 7, 4.. -62 (11th from end)</button>
        <button onclick="setRevCase(3, 5, 253, 20)" class="p-2 rounded-xl bg-slate-900 text-cyan-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 5.2 Q17: 3, 8, 13.. 253 (20th from end)</button>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Position k from the LAST term:</span><span class="font-bold text-amber-300" id="sim6-k-disp">k = 11</span></div>
        <input type="range" min="1" max="25" value="11" id="sim6-k" oninput="calcRevAP()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-slate-300" id="sim6-orig">Original AP: a = 10, d = -3, Last Term l = -62 (Total n = 25 terms)</div>
        <div class="text-cyan-300" id="sim6-rev">Reversed AP: New first = -62, New step (-d) = +3</div>
        <div class="text-emerald-300 font-bold text-sm" id="sim6-res">kth from end = -62 + (11 - 1)(+3) = -32  [Same as forward Term 15!]</div>
    </div>
</div>

<script>
let revState = { a: 10, d: -3, l: -62 };
function setRevCase(a, d, l, k) {
    revState = { a, d, l };
    const totalN = Math.round((l - a) / d) + 1;
    const slider = document.getElementById("sim6-k");
    slider.max = totalN;
    slider.value = k;
    calcRevAP();
}
function calcRevAP() {
    const k = parseInt(document.getElementById("sim6-k").value, 10);
    const { a, d, l } = revState;
    const totalN = Math.round((l - a) / d) + 1;
    const revD = -d;
    const ans = l + (k - 1) * revD;
    const fwdPos = totalN - k + 1;

    document.getElementById("sim6-k-disp").textContent = "k = " + k;
    document.getElementById("sim6-badge").textContent = `${k}th from end = ${ans}`;
    document.getElementById("sim6-orig").textContent = `Original AP: a = ${a}, d = ${d}, Last Term l = ${l}  (Total n = ${totalN} terms)`;
    document.getElementById("sim6-rev").textContent = `Flip Direction: Start at ${l}, step by -d = ${revD > 0 ? "+" + revD : revD}`;
    document.getElementById("sim6-res").textContent = `Result: ${l} + (${k} - 1)(${revD}) = ${ans}   [Matches Forward Term #${fwdPos}!]`;
}
setRevCase(10, -3, -62, 11);
</script>
"""

# Simulator 7: Two-Term Linear System Solver & Salary/Savings Models
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚖️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Elimination Decoder: Unlocking a & d From Any Two Terms</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="sim7-badge">a = 3, d = 1</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="solvePair52(3, 5, 7, 9)" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 5: a3=5, a7=9</button>
        <button onclick="solvePair52(3, 4, 9, -8)" class="p-2 rounded-xl bg-slate-900 text-cyan-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 5.2 Q9: a3=4, a9=-8</button>
        <button onclick="solvePair52(1, 5000, 11, 7000)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Salary Model: a1=5000, a11=7000</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300" id="sim7-eq1">Eq (1): a + 2d = 5</div>
        <div class="text-cyan-300" id="sim7-eq2">Eq (2): a + 6d = 9</div>
        <div class="text-slate-300" id="sim7-sub">Subtract Eq (2) - Eq (1): (6 - 2)d = 4  =>  d = 1</div>
        <div class="text-emerald-300 font-bold text-sm" id="sim7-ap">AP Found: a = 3, d = 1  ->  3, 4, 5, 6, 7, ...</div>
    </div>
</div>

<script>
function solvePair52(p, vp, q, vq) {
    const c1 = p - 1;
    const c2 = q - 1;
    const d = (vq - vp) / (c2 - c1);
    const a = vp - c1 * d;
    document.getElementById("sim7-badge").textContent = `a = ${a}, d = ${d}`;
    document.getElementById("sim7-eq1").textContent = `Eq (1) for Term #${p}: a + ${c1}d = ${vp}`;
    document.getElementById("sim7-eq2").textContent = `Eq (2) for Term #${q}: a + ${c2}d = ${vq}`;
    document.getElementById("sim7-sub").textContent = `Eliminate 'a' via Eq(2) - Eq(1): ${c2 - c1}d = ${vq - vp}   =>   d = ${d}`;
    const preview = [a, a + d, a + 2*d, a + 3*d, a + 4*d].join(", ");
    document.getElementById("sim7-ap").textContent = `Result: a = ${a}, d = ${d}   |   AP: ${preview}, ...`;
}
solvePair52(3, 5, 7, 9);
</script>
"""

# Simulator 8: Gauss Summation Pairing Symmetry (1 + 2 + ... + n)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✨</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Carl Friedrich Gauss Pairing Visualizer (Section 5.4)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="sim8-badge">S_100 = 5,050</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="setGaussN(10)" class="p-2 rounded-xl bg-slate-900 text-cyan-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">First n = 10 (Sum 55)</button>
        <button onclick="setGaussN(50)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">First n = 50 (Sum 1,275)</button>
        <button onclick="setGaussN(100)" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Gauss Classic n = 100</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3 text-xs font-mono">
        <svg viewBox="0 0 360 110" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <text x="180" y="18" fill="#fcd34d" font-size="10.5" font-weight="bold" text-anchor="middle" id="g-svg-head">Write Forward S + Reversed S Vertically:</text>
            <text x="180" y="42" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle" id="g-svg-fwd">S = 1   +   2   +   3   + ... +  99  +  100</text>
            <text x="180" y="64" fill="#c4b5fd" font-size="11" font-weight="bold" text-anchor="middle" id="g-svg-rev">S = 100 +  99   +  98   + ... +   2  +    1</text>
            <line x1="25" y1="73" x2="335" y2="73" stroke="#475569" stroke-width="1.5" />
            <text x="180" y="95" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle" id="g-svg-sum">2S = 101  +  101  +  101  + ... + 101 +  101  (100 identical pairs!)</text>
        </svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-emerald-300 font-bold text-center text-sm" id="sim8-final">
            2S = 100 x 101 = 10,100   =>   S = (100 x 101) / 2 = 5,050!
        </div>
    </div>
</div>

<script>
function setGaussN(n) {
    const pair = n + 1;
    const total = (n * pair) / 2;
    document.getElementById("sim8-badge").textContent = `S_${n} = ${total.toLocaleString()}`;
    document.getElementById("g-svg-fwd").textContent = `S = 1 + 2 + 3 + ... + ${n-1} + ${n}`;
    document.getElementById("g-svg-rev").textContent = `S = ${n} + ${n-1} + ${n-2} + ... + 2 + 1`;
    document.getElementById("g-svg-sum").textContent = `2S = ${pair} + ${pair} + ${pair} + ... + ${pair}  (${n} identical pairs!)`;
    document.getElementById("sim8-final").textContent = `2S = ${n} x ${pair} = ${(n*pair).toLocaleString()}   =>   S_${n} = ${total.toLocaleString()}!`;
}
setGaussN(100);
</script>
"""
