#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 8: Introduction to Trigonometry
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Real-World Right Triangle Models (Qutub Minar, River Width, Hot-Air Balloon)
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🕌</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Real-World Right Triangle Trigonometry (Section 8.1)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8s1-badge">Qutub Minar Height</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickScene81(0)" id="btn-81-0" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">1. Qutub Minar</button>
        <button onclick="pickScene81(1)" id="btn-81-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. River Width</button>
        <button onclick="pickScene81(2)" id="btn-81-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. Hot-Air Balloon</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 120" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="c8s1-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold" id="c8s1-info"></div>
    </div>
</div>

<script>
const scenes81 = [
    {
        badge: "Monument Height",
        info: "Angle of elevation + horizontal ground distance build one vertical right triangle -> Finds Qutub Minar height without climbing!",
        svg: `<line x1="30" y1="100" x2="320" y2="100" stroke="#475569" stroke-width="2" />
              <rect x="255" y="20" width="16" height="80" fill="#b45309" stroke="#fbbf24" />
              <line x1="65" y1="100" x2="255" y2="20" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,2" />
              <text x="65" y="114" fill="#7dd3fc" font-size="9.5" text-anchor="middle">Observer (Angle)</text>
              <text x="263" y="14" fill="#fcd34d" font-size="9.5" text-anchor="middle">Minar Top</text>
              <text x="160" y="94" fill="#6ee7b7" font-size="9.5" text-anchor="middle">Ground Distance (Known)</text>`
    },
    {
        badge: "River Width",
        info: "Standing on balcony (known height) looking down to opposite-bank pot uses depression angle -> Calculates river width without crossing!",
        svg: `<rect x="35" y="25" width="22" height="75" fill="#475569" />
              <line x1="57" y1="100" x2="310" y2="100" stroke="#38bdf8" stroke-width="3" />
              <line x1="57" y1="25" x2="290" y2="100" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,2" />
              <circle cx="290" cy="96" r="5" fill="#34d399" />
              <text x="45" y="18" fill="#cbd5e1" font-size="9" text-anchor="middle">Balcony</text>
              <text x="180" y="114" fill="#7dd3fc" font-size="9.5" text-anchor="middle">River Width (Calculated Indirectly)</text>
              <text x="290" y="84" fill="#6ee7b7" font-size="9" text-anchor="middle">Flowerpot</text>`
    },
    {
        badge: "Balloon Altitude",
        info: "Tracking rising hot-air balloon at two elevation angles tracks height gain effortlessly using tangent & sine ratios!",
        svg: `<line x1="30" y1="105" x2="330" y2="105" stroke="#475569" stroke-width="2" />
              <circle cx="255" cy="30" r="14" fill="#f43f5e" stroke="#fda4af" stroke-width="2" />
              <line x1="255" y1="44" x2="255" y2="105" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,2" />
              <line x1="65" y1="105" x2="255" y2="30" stroke="#fde047" stroke-width="2" />
              <text x="65" y="116" fill="#fcd34d" font-size="9.5" text-anchor="middle">Tracker</text>
              <text x="275" y="75" fill="#fda4af" font-size="9.5">Altitude</text>`
    }
];
function pickScene81(i) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-81-" + k).className = (k === i)
            ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    }
    document.getElementById("c8s1-badge").textContent = scenes81[i].badge;
    document.getElementById("c8s1-svg").innerHTML = scenes81[i].svg;
    document.getElementById("c8s1-info").textContent = scenes81[i].info;
}
pickScene81(0);
</script>
"""

# Simulator 2: All 6 Trigonometric Ratios Explorer (Aryabhata & Edmund Gunter)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Six Trigonometric Ratios Lab: Opp, Adj & Hyp (Section 8.2)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">3-4-5, 5-12-13, 8-15-17</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="setTri82(4, 3, 5)" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Triple 3-4-5</button>
        <button onclick="setTri82(12, 5, 13)" class="p-2 rounded-xl bg-slate-900 text-cyan-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Triple 5-12-13</button>
        <button onclick="setTri82(15, 8, 17)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Triple 8-15-17</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-3 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="c8s2-sides">Relative to Acute ∠A: Opposite = 3, Adjacent = 4, Hypotenuse = 5</div>
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-center" id="c8s2-grid"></div>
        <div class="text-slate-400 font-sans pt-1 border-t border-slate-800">History: Aryabhata coined 'ardha-jya' (500 CE) -> 'sine'; Edmund Gunter coined abbreviations sin, cos, tan!</div>
    </div>
</div>

<script>
function setTri82(adj, opp, hyp) {
    document.getElementById("c8s2-sides").textContent = `For Angle A: Opposite (BC) = ${opp}  |  Adjacent (AB) = ${adj}  |  Hypotenuse (AC) = ${hyp}`;
    const items = [
        ["sin A = Opp/Hyp", `${opp}/${hyp}`, "text-amber-300"],
        ["cos A = Adj/Hyp", `${adj}/${hyp}`, "text-cyan-300"],
        ["tan A = Opp/Adj", `${opp}/${adj}`, "text-emerald-300"],
        ["cosec A = Hyp/Opp", `${hyp}/${opp}`, "text-amber-200"],
        ["sec A = Hyp/Adj", `${hyp}/${adj}`, "text-cyan-200"],
        ["cot A = Adj/Opp", `${adj}/${opp}`, "text-emerald-200"]
    ];
    document.getElementById("c8s2-grid").innerHTML = items.map(it =>
        `<div class="bg-slate-900 p-2 rounded-xl border border-slate-800"><div class="text-[10px] text-slate-400">${it[0]}</div><div class="text-sm font-bold ${it[2]}">${it[1]}</div></div>`
    ).join("");
}
setTri82(4, 3, 5);
</script>
"""

# Simulator 3: Perspective Shift Switcher (Angle A <-> Angle C) & Quotient Rules
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔄</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Angle Perspective Switcher (∠A ↔ ∠C Inside Right △ABC, Ex 8.1 Q1)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800" id="c8s3-badge">Viewing From ∠A</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="switchAng83('A')" id="btn-83-A" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">Focus on Bottom Angle ∠A</button>
        <button onclick="switchAng83('C')" id="btn-83-C" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Focus on Top Angle ∠C</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-slate-300">Fixed Triangle (∠B = 90°): AB = 24 cm, BC = 7 cm, Hypotenuse AC = 25 cm</div>
        <div class="text-amber-300 font-bold" id="c8s3-opp">Opposite Side = BC = 7 cm   |   Adjacent Side = AB = 24 cm</div>
        <div class="text-emerald-300 font-bold text-sm" id="c8s3-val">sin A = 7/25,   cos A = 24/25,   tan A = sin A / cos A = 7/24</div>
    </div>
</div>

<script>
function switchAng83(ang) {
    document.getElementById("btn-83-A").className = (ang === "A")
        ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-83-C").className = (ang === "C")
        ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";

    document.getElementById("c8s3-badge").textContent = "Viewing From ∠" + ang;
    if (ang === "A") {
        document.getElementById("c8s3-opp").textContent = "From ∠A: Opposite = BC = 7 cm   |   Adjacent = AB = 24 cm (Hyp AC = 25)";
        document.getElementById("c8s3-val").textContent = "sin A = 7/25,   cos A = 24/25,   tan A = 7/24";
    } else {
        document.getElementById("c8s3-opp").textContent = "From ∠C (Swapped!): Opposite = AB = 24 cm   |   Adjacent = BC = 7 cm (Hyp AC = 25)";
        document.getElementById("c8s3-val").textContent = "sin C = 24/25 (= cos A!),   cos C = 7/25 (= sin A!),   tan C = 24/7";
    }
}
switchAng83("A");
</script>
"""

# Simulator 4: Scale Invariance by AA Similarity & Strict Bounds
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔍</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Scale Invariance Visualizer (AA Similarity) & Ratio Bounds</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8s4-badge">sin A = 0.60 INVARIANT!</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Scale Triangle Size by k (0.5x to 4.0x — Angle A stays 37°):</span><span class="font-bold text-amber-300" id="c8s4-k-disp">k = 2.0x</span></div>
        <input type="range" min="0.5" max="4.0" step="0.5" value="2.0" id="c8s4-k" oninput="scaleTrig84()" class="w-full accent-emerald-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c8s4-sides">Opp = 6.0 cm,  Adj = 8.0 cm,  Hyp = 10.0 cm</div>
        <div class="text-emerald-300 font-bold text-sm" id="c8s4-rat">sin A = 6.0 / 10.0 = 0.60   |   cos A = 8.0 / 10.0 = 0.80  (NEVER CHANGES!)</div>
        <div class="text-slate-400 pt-1 border-t border-slate-800">Bounds: Since Hyp is longest, sin A <= 1 and cos A <= 1 ALWAYS (so sin θ = 4/3 is IMPOSSIBLE; sec θ >= 1).</div>
    </div>
</div>

<script>
function scaleTrig84() {
    const k = parseFloat(document.getElementById("c8s4-k").value);
    const opp = 3 * k, adj = 4 * k, hyp = 5 * k;
    document.getElementById("c8s4-k-disp").textContent = "k = " + k.toFixed(1) + "x";
    document.getElementById("c8s4-sides").textContent = `Opp = ${opp.toFixed(1)},  Adj = ${adj.toFixed(1)},  Hyp = ${hyp.toFixed(1)}`;
    document.getElementById("c8s4-rat").textContent = `sin A = ${opp.toFixed(1)}/${hyp.toFixed(1)} = 0.60   |   cos A = ${adj.toFixed(1)}/${hyp.toFixed(1)} = 0.80  (Scale factor k cancels!)`;
}
scaleTrig84();
</script>
"""

# Simulator 5: Pythagoras k-Multiplier & Ex 8.1 Q10 Solver
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧮</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Ex 8.1 Triangle Solver: k-Method & PR + QR = 25 Puzzle</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Pythagoras Engine</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="showEx85(0)" id="btn-85-0" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">tan A = 4/3 (k-Method)</button>
        <button onclick="showEx85(1)" id="btn-85-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">15 cot A = 8 (Q4)</button>
        <button onclick="showEx85(2)" id="btn-85-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">PR+QR=25, PQ=5 (Q10)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="c8s5-l1"></div>
        <div class="text-cyan-300" id="c8s5-l2"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c8s5-l3"></div>
    </div>
</div>

<script>
const ex85List = [
    {
        l1: "Given tan A = 4/3 -> Let Opposite = 4k and Adjacent = 3k (positive factor k > 0):",
        l2: "By Pythagoras: Hypotenuse AC = sqrt((4k)^2 + (3k)^2) = sqrt(25k^2) = 5k.",
        l3: "All ratios: sin A = 4/5, cos A = 3/5, cosec A = 5/4, sec A = 5/3, cot A = 3/4!"
    },
    {
        l1: "Ex 8.1 Q4: 15 cot A = 8 -> cot A = 8/15 -> Adjacent = 8k, Opposite = 15k:",
        l2: "Hypotenuse AC = sqrt(64k^2 + 225k^2) = sqrt(289k^2) = 17k.",
        l3: "Result: sin A = 15/17  and  sec A = 17/8!"
    },
    {
        l1: "Ex 8.1 Q10: Right △PQR (∠Q=90°), PQ = 5, PR + QR = 25 -> Set QR = x, PR = 25 - x:",
        l2: "(25 - x)^2 = 5^2 + x^2  =>  625 - 50x + x^2 = 25 + x^2  =>  50x = 600  =>  QR = 12, PR = 13!",
        l3: "Relative to ∠P: sin P = 12/13,  cos P = 5/13,  tan P = 12/5!"
    }
];
function showEx85(i) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-85-" + k).className = (k === i)
            ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    }
    document.getElementById("c8s5-l1").textContent = ex85List[i].l1;
    document.getElementById("c8s5-l2").textContent = ex85List[i].l2;
    document.getElementById("c8s5-l3").textContent = ex85List[i].l3;
}
showEx85(0);
</script>
"""

# Simulator 6: Deriving Exact 45° Ratios (Isosceles Right Triangle)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Geometric Derivation of 45° Ratios (Isosceles Right △ABC)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">45°-45°-90°</span>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 140" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <polygon points="50,115 160,115 160,25" fill="rgba(56,189,248,0.16)" stroke="#38bdf8" stroke-width="2" />
            <rect x="148" y="103" width="12" height="12" fill="none" stroke="#94a3b8" stroke-width="1.5" />
            <text x="105" y="130" fill="#fcd34d" font-size="10" font-weight="bold" text-anchor="middle">AB = a</text>
            <text x="184" y="72" fill="#fcd34d" font-size="10" font-weight="bold" text-anchor="middle">BC = a</text>
            <text x="88" y="62" fill="#6ee7b7" font-size="10.5" font-weight="bold" text-anchor="middle">AC = a√2</text>
            <text x="68" y="108" fill="#fff" font-size="9">45°</text>
            <text x="145" y="45" fill="#fff" font-size="9">45°</text>
        </svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
            <div class="text-amber-300">Equal 45° corners force legs AB = BC = a.</div>
            <div class="text-cyan-300">Pythagoras: AC = sqrt(a² + a²) = a√2</div>
            <div class="text-emerald-300 font-bold">sin 45° = 1/√2  |  cos 45° = 1/√2  |  tan 45° = 1</div>
            <div class="text-purple-300">cosec 45° = √2  |  sec 45° = √2  |  cot 45° = 1</div>
        </div>
    </div>
</div>
"""

# Simulator 7: Deriving Exact 30° & 60° Ratios (Equilateral Triangle Split)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔺</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Equilateral Split Derivation of 30° & 60° Ratios (Side 2a)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8s7-badge">Angle = 30°</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickAng87(30)" id="btn-87-30" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">Read Top Angle 30° (∠BAD)</button>
        <button onclick="pickAng87(60)" id="btn-87-60" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Read Base Angle 60° (∠B)</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 140" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <polygon points="110,15 35,120 185,120" fill="rgba(16,185,129,0.1)" stroke="#64748b" stroke-width="1.5" />
            <polygon points="110,15 35,120 110,120" fill="rgba(56,189,248,0.18)" stroke="#38bdf8" stroke-width="2" />
            <text x="64" y="65" fill="#7dd3fc" font-size="10" font-weight="bold">2a</text>
            <text x="122" y="75" fill="#fcd34d" font-size="10" font-weight="bold">AD = a√3</text>
            <text x="72" y="133" fill="#6ee7b7" font-size="10" font-weight="bold">BD = a</text>
            <text x="98" y="38" fill="#fff" font-size="9">30°</text>
            <text x="48" y="114" fill="#fff" font-size="9">60°</text>
        </svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
            <div class="text-cyan-300" id="c8s7-opp">From 30° (∠BAD): Opp = BD = a, Adj = AD = a√3, Hyp = 2a</div>
            <div class="text-emerald-300 font-bold text-sm" id="c8s7-vals">sin 30° = 1/2   |   cos 30° = √3/2   |   tan 30° = 1/√3</div>
            <div class="text-purple-300" id="c8s7-rec">cosec 30° = 2   |   sec 30° = 2/√3   |   cot 30° = √3</div>
        </div>
    </div>
</div>

<script>
function pickAng87(a) {
    document.getElementById("btn-87-30").className = (a === 30)
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-87-60").className = (a === 60)
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("c8s7-badge").textContent = "Angle = " + a + "°";
    if (a === 30) {
        document.getElementById("c8s7-opp").textContent = "From 30°: Opp = a,  Adj = a√3,  Hyp = 2a";
        document.getElementById("c8s7-vals").textContent = "sin 30° = 1/2   |   cos 30° = √3/2   |   tan 30° = 1/√3";
        document.getElementById("c8s7-rec").textContent = "cosec 30° = 2   |   sec 30° = 2/√3   |   cot 30° = √3";
    } else {
        document.getElementById("c8s7-opp").textContent = "From 60°: Opp = a√3,  Adj = a,  Hyp = 2a";
        document.getElementById("c8s7-vals").textContent = "sin 60° = √3/2  |   cos 60° = 1/2    |   tan 60° = √3";
        document.getElementById("c8s7-rec").textContent = "cosec 60° = 2/√3|   sec 60° = 2      |   cot 60° = 1/√3";
    }
}
pickAng87(30);
</script>
"""

# Simulator 8: Boundary Angle Limits (0° & 90° Collapsing Triangle)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚡</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Boundary Limits Animator: A → 0° & A → 90° (Not Defined Cases!)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c8s8-badge">A = 45°</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="setLim88(0)" class="p-2 rounded-xl bg-slate-900 text-cyan-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Collapse to 0°</button>
        <button onclick="setLim88(45)" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Middle 45°</button>
        <button onclick="setLim88(90)" class="p-2 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Open to 90°</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="c8s8-geom"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c8s8-vals"></div>
        <div class="text-rose-400 font-bold" id="c8s8-nd"></div>
    </div>
</div>

<script>
function setLim88(deg) {
    document.getElementById("c8s8-badge").textContent = "A = " + deg + "°";
    if (deg === 0) {
        document.getElementById("c8s8-geom").textContent = "As A -> 0°: Opposite side BC -> 0, and Hypotenuse AC merges down onto AB (AC -> AB)!";
        document.getElementById("c8s8-vals").textContent = "sin 0° = 0/AC = 0   |   cos 0° = AB/AB = 1   |   tan 0° = 0/AB = 0   |   sec 0° = 1";
        document.getElementById("c8s8-nd").textContent = "NOT DEFINED (1/0): cosec 0° and cot 0° divide by sin 0° = 0!";
    } else if (deg === 90) {
        document.getElementById("c8s8-geom").textContent = "As A -> 90°: Adjacent base AB -> 0, and Hypotenuse AC merges into wall BC (AC -> BC)!";
        document.getElementById("c8s8-vals").textContent = "sin 90° = BC/BC = 1 |   cos 90° = 0/AC = 0  |   cosec 90° = 1 |   cot 90° = 0";
        document.getElementById("c8s8-nd").textContent = "NOT DEFINED (1/0): tan 90° and sec 90° divide by cos 90° = 0!";
    } else {
        document.getElementById("c8s8-geom").textContent = "At A = 45°: Non-zero legs BC = AB = a and Hypotenuse AC = a√2 (All 6 ratios finite!)";
        document.getElementById("c8s8-vals").textContent = "sin 45° = 1/√2  |  cos 45° = 1/√2  |  tan 45° = 1";
        document.getElementById("c8s8-nd").textContent = "Zero division-by-zero issues inside 0° < A < 90°!";
    }
}
setLim88(0);
</script>
"""
