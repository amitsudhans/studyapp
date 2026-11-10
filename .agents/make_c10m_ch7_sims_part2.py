#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 7: Coordinate Geometry
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Midpoint Formula Applications (Circle Diameter & Parallelogram Missing Vertex)
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⭕</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Midpoint Formula Lab: Circle Diameter & Parallelogram (Ex 7.2 Q6-7)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c7s9-badge">A(3, -10)</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="tab79('circle')" id="btn-79-c" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Circle Diameter Endpoint (Q7)</button>
        <button onclick="tab79('para')" id="btn-79-p" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Parallelogram Diagonals (Q6)</button>
    </div>

    <div id="p79-circle" class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Ex 7.2 Q7: Diameter AB with Center O(2, -3) and Endpoint B(1, 4)</div>
        <div class="text-cyan-300">Midpoint Equations: (x + 1)/2 = 2   and   (y + 4)/2 = -3</div>
        <div class="text-emerald-300 font-bold text-sm">Solve cleanly: x = 4 - 1 = 3,   y = -6 - 4 = -10   =>   A(3, -10)!</div>
    </div>

    <div id="p79-para" class="hidden bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Ex 7.2 Q6: Parallelogram vertices A(1, 2), B(4, y), C(x, 6), D(3, 5)</div>
        <div class="text-cyan-300">Diagonals bisect each other: Midpoint(AC) = ((1+x)/2, (2+6)/2) == Midpoint(BD) = ((4+3)/2, (y+5)/2)</div>
        <div class="text-emerald-300 font-bold text-sm">Equate: 1 + x = 7 => x = 6!   And 8 = y + 5 => y = 3!</div>
    </div>
</div>

<script>
function tab79(t) {
    document.getElementById("p79-circle").classList.toggle("hidden", t !== "circle");
    document.getElementById("p79-para").classList.toggle("hidden", t !== "para");
    document.getElementById("btn-79-c").className = (t === "circle")
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-79-p").className = (t === "para")
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("c7s9-badge").textContent = (t === "circle") ? "A(3, -10)" : "x = 6, y = 3";
}
</script>
"""

# Simulator 10: k:1 Division Ratio Finder
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔍</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">k : 1 Single-Variable Ratio Solver (Example 7 & Ex 7.2 Q4)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c7s10-badge">Ratio 2 : 7</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="solveRatio10(-3, 10, 6, -8, -1, 6)" class="p-2 rounded-xl bg-slate-900 text-cyan-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 7.2 Q4: (-1,6) on (-3,10) to (6,-8)</button>
        <button onclick="solveRatio10(-6, 10, 3, -8, -4, 6)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Example 7: (-4,6) on (-6,10) to (3,-8)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300" id="c7s10-eq">Assume ratio k : 1 -> x = (6k + (-3)) / (k + 1) = -1</div>
        <div class="text-cyan-300" id="c7s10-sol">6k - 3 = -k - 1  =>  7k = 2  =>  k = 2/7</div>
        <div class="text-emerald-300 font-bold text-sm" id="c7s10-res">Exact Internal Ratio = 2 : 7!</div>
    </div>
</div>

<script>
function solveRatio10(x1,y1, x2,y2, px,py) {
    // (k*x2 + x1)/(k+1) = px => k(x2 - px) = px - x1
    const num = px - x1;
    const den = x2 - px;
    const gcd = (a, b) => b === 0 ? a : gcd(b, a % b);
    const g = gcd(Math.abs(num), Math.abs(den)) || 1;
    const m1 = Math.abs(num / g);
    const m2 = Math.abs(den / g);

    document.getElementById("c7s10-badge").textContent = `Ratio ${m1} : ${m2}`;
    document.getElementById("c7s10-eq").textContent = `Let ratio be k : 1 -> x-eq: (${x2}k + ${x1}) / (k + 1) = ${px}`;
    document.getElementById("c7s10-sol").textContent = `Cross-multiply: ${den}k = ${num}  =>  k = ${m1}/${m2}`;
    document.getElementById("c7s10-res").textContent = `Exact Ratio = ${m1} : ${m2}!   [Verify y = (${m1}*(${y2}) + ${m2}*(${y1})) / (${m1+m2}) = ${py}]`;
}
solveRatio10(-3, 10, 6, -8, -1, 6);
</script>
"""

# Simulator 11: Points of Trisection (1:2 & 2:1) and 4 Equal Parts
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📏</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Equal Partition Visualizer: Trisection (1:2 & 2:1) & 4 Equal Parts</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800" id="c7s11-badge">3 Equal Pieces</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="showPart11(3)" id="btn-711-3" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">Trisection (Ex 7.2 Q2)</button>
        <button onclick="showPart11(4)" id="btn-711-4" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">4 Equal Parts (Ex 7.2 Q9)</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 70" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="c7s11-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold" id="c7s11-info"></div>
    </div>
</div>

<script>
function showPart11(n) {
    document.getElementById("btn-711-3").className = (n === 3)
        ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-711-4").className = (n === 4)
        ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";

    const svg = document.getElementById("c7s11-svg");
    if (n === 3) {
        svg.innerHTML = `
            <line x1="40" y1="35" x2="320" y2="35" stroke="#475569" stroke-width="3" />
            <circle cx="40" cy="35" r="5" fill="#fbbf24" /><text x="40" y="18" fill="#fcd34d" font-size="9.5" text-anchor="middle">A(4,-1)</text>
            <circle cx="133" cy="35" r="5" fill="#34d399" /><text x="133" y="18" fill="#6ee7b7" font-size="9.5" text-anchor="middle">P (1:2)</text>
            <circle cx="226" cy="35" r="5" fill="#38bdf8" /><text x="226" y="18" fill="#7dd3fc" font-size="9.5" text-anchor="middle">Q (2:1)</text>
            <circle cx="320" cy="35" r="5" fill="#fbbf24" /><text x="320" y="18" fill="#fcd34d" font-size="9.5" text-anchor="middle">B(-2,-3)</text>
            <text x="180" y="58" fill="#cbd5e1" font-size="9.5" text-anchor="middle">AP = PQ = QB (P = (2, -5/3), Q = (0, -7/3))</text>
        `;
        document.getElementById("c7s11-badge").textContent = "3 Equal Parts (1:2 & 2:1)";
        document.getElementById("c7s11-info").textContent = "Point P uses ratio 1:2 -> (2, -5/3); Point Q uses ratio 2:1 (or Mid(P,B)) -> (0, -7/3)!";
    } else {
        svg.innerHTML = `
            <line x1="40" y1="35" x2="320" y2="35" stroke="#475569" stroke-width="3" />
            <circle cx="40" cy="35" r="5" fill="#fbbf24" /><text x="40" y="18" fill="#fcd34d" font-size="9.5" text-anchor="middle">A(-2,2)</text>
            <circle cx="110" cy="35" r="5" fill="#34d399" /><text x="110" y="18" fill="#6ee7b7" font-size="9.5" text-anchor="middle">P(-1,3.5)</text>
            <circle cx="180" cy="35" r="5" fill="#c4b5fd" /><text x="180" y="18" fill="#ddd6fe" font-size="9.5" text-anchor="middle">Q(0,5)</text>
            <circle cx="250" cy="35" r="5" fill="#38bdf8" /><text x="250" y="18" fill="#7dd3fc" font-size="9.5" text-anchor="middle">R(1,6.5)</text>
            <circle cx="320" cy="35" r="5" fill="#fbbf24" /><text x="320" y="18" fill="#fcd34d" font-size="9.5" text-anchor="middle">B(2,8)</text>
            <text x="180" y="58" fill="#cbd5e1" font-size="9.5" text-anchor="middle">Use Midpoint Formula 3 Times: Q=Mid(A,B), P=Mid(A,Q), R=Mid(Q,B)!</text>
        `;
        document.getElementById("c7s11-badge").textContent = "4 Equal Parts (Midpoints!)";
        document.getElementById("c7s11-info").textContent = "Zero m1:m2 needed! Q = Mid(A,B) = (0,5); P = Mid(A,Q) = (-1, 7/2); R = Mid(Q,B) = (1, 13/2)!";
    }
}
showPart11(3);
</script>
"""

# Simulator 12: Rhombus Area Formula (1/2 * d1 * d2) Explorer
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">♦️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Rhombus Area via Perpendicular Diagonals (Ex 7.2 Q10)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Area = 24 sq units</span>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 150" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <polygon points="150,115 170,35 70,50 50,130" fill="rgba(251,191,36,0.16)" stroke="#fbbf24" stroke-width="2" />
            <line x1="150" y1="115" x2="70" y2="50" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,2" />
            <line x1="170" y1="35" x2="50" y2="130" stroke="#34d399" stroke-width="2" stroke-dasharray="4,2" />
            <text x="155" y="128" fill="#fcd34d" font-size="9">A(3,0)</text>
            <text x="174" y="33" fill="#fcd34d" font-size="9">B(4,5)</text>
            <text x="45" y="45" fill="#fcd34d" font-size="9">C(-1,4)</text>
            <text x="12" y="140" fill="#fcd34d" font-size="9">D(-2,-1)</text>
        </svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
            <div class="text-cyan-300">Diagonal AC = sqrt((3+1)^2 + (0-4)^2) = sqrt(32) = 4*sqrt(2)</div>
            <div class="text-emerald-300">Diagonal BD = sqrt((4+2)^2 + (5+1)^2) = sqrt(72) = 6*sqrt(2)</div>
            <div class="text-amber-300 font-bold text-sm">Area = 1/2 x 4*sqrt(2) x 6*sqrt(2) = 24 sq. units!</div>
        </div>
    </div>
</div>
"""

# Simulator 13: Axis Cuts (y=0 / x=0) & Fractional Segment Split AP = (3/7)AB
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎯</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Axis Cuts (y=0, x=0) & Fractional AP = (3/7)AB Trap Solver (Ex 7.2 Q5 & Q8)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c7s13-badge">Ex 7.2 Q5 & Q8</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="tab13('ax')" id="btn-713-ax" class="p-2 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">x-Axis Cut (Ex 7.2 Q5)</button>
        <button onclick="tab13('frac')" id="btn-713-fr" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">AP = (3/7)AB Split (Q8)</button>
    </div>

    <div id="p713-ax" class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Segment A(1, -5) to B(-4, 5) cut by x-axis at (x, 0):</div>
        <div class="text-cyan-300">y = 0 forces (5k - 5)/(k + 1) = 0  =>  k = 1 (Ratio 1 : 1 midpoint!)</div>
        <div class="text-emerald-300 font-bold text-sm">Substitute k = 1 into x: (1*(-4) + 1*1)/2 = -3/2  =>  Cut Point (-3/2, 0)!</div>
    </div>

    <div id="p713-frac" class="hidden bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Ex 7.2 Q8: A(-2, -2), B(2, -4), and AP = (3/7) AB:</div>
        <div class="text-rose-300">TRAP CHECK: Never use 3:7! PB = AB - (3/7)AB = (4/7)AB -> True Ratio AP:PB = 3 : 4!</div>
        <div class="text-emerald-300 font-bold text-sm">P = ((3*2 + 4*(-2))/7, (3*(-4) + 4*(-2))/7) = (-2/7, -20/7)!</div>
    </div>
</div>

<script>
function tab13(t) {
    document.getElementById("p713-ax").classList.toggle("hidden", t !== "ax");
    document.getElementById("p713-frac").classList.toggle("hidden", t !== "frac");
    document.getElementById("btn-713-ax").className = (t === "ax")
        ? "p-2 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-713-fr").className = (t === "frac")
        ? "p-2 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
}
</script>
"""

# Simulator 14: Sports Day Rectangular Track Flags (Ex 7.2 Q3 — Neutral Labels)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🚩</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Sports Track Coordinate Lab: 100-Pot Field Flags (Ex 7.2 Q3)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">GR = √61 m | Mid(5, 22.5)</span>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 130" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <rect x="25" y="15" width="175" height="95" fill="rgba(16,185,129,0.08)" stroke="#475569" stroke-width="1.5" />
            <line x1="60" y1="60" x2="165" y2="75" stroke="#fde047" stroke-width="2" stroke-dasharray="3,2" />
            <circle cx="60" cy="60" r="5" fill="#22c55e" />
            <circle cx="112.5" cy="67.5" r="5" fill="#38bdf8" />
            <circle cx="165" cy="75" r="5" fill="#f43f5e" />
            <text x="60" y="48" fill="#4ade80" font-size="9" font-weight="bold" text-anchor="middle">Green (2, 25)</text>
            <text x="112" y="54" fill="#7dd3fc" font-size="9" font-weight="bold" text-anchor="middle">Blue (5, 22.5)</text>
            <text x="165" y="92" fill="#fda4af" font-size="9" font-weight="bold" text-anchor="middle">Red (8, 20)</text>
        </svg>

        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
            <div class="text-emerald-300">Runner 1 (Line 2, 1/4 of 100): G(2, 25)</div>
            <div class="text-rose-300">Runner 2 (Line 8, 1/5 of 100): R(8, 20)</div>
            <div class="text-amber-300">Distance GR = sqrt((8-2)^2 + (20-25)^2) = sqrt(61) m</div>
            <div class="text-cyan-300 font-bold">Halfway Blue Flag = Midpoint = (5, 22.5)!</div>
        </div>
    </div>
</div>
"""

# Simulator 15: Algebra-Geometry Bridge (Triangle Centroid via 2:1 Section Formula)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚖️</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Triangle Centroid Lab: Section Ratio 2:1 on Median AD</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800" id="c7s15-badge">Centroid G(2, -1)</span>
    </div>

    <div class="grid grid-cols-3 gap-2 text-xs">
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800">
            <div class="text-amber-300 font-bold mb-1">A(x₁, y₁)</div>
            <input type="number" value="3" id="g-x1" oninput="calcCen15()" class="w-1/2 bg-slate-950 text-white p-1 rounded border border-slate-700 font-mono"><input type="number" value="-5" id="g-y1" oninput="calcCen15()" class="w-1/2 bg-slate-950 text-white p-1 rounded border border-slate-700 font-mono">
        </div>
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800">
            <div class="text-cyan-300 font-bold mb-1">B(x₂, y₂)</div>
            <input type="number" value="-7" id="g-x2" oninput="calcCen15()" class="w-1/2 bg-slate-950 text-white p-1 rounded border border-slate-700 font-mono"><input type="number" value="4" id="g-y2" oninput="calcCen15()" class="w-1/2 bg-slate-950 text-white p-1 rounded border border-slate-700 font-mono">
        </div>
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800">
            <div class="text-emerald-300 font-bold mb-1">C(x₃, y₃)</div>
            <input type="number" value="10" id="g-x3" oninput="calcCen15()" class="w-1/2 bg-slate-950 text-white p-1 rounded border border-slate-700 font-mono"><input type="number" value="-2" id="g-y3" oninput="calcCen15()" class="w-1/2 bg-slate-950 text-white p-1 rounded border border-slate-700 font-mono">
        </div>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c7s15-mid">Midpoint D of BC = (1.50, 1.00)</div>
        <div class="text-emerald-300 font-bold text-sm" id="c7s15-cen">2:1 Section on AD = ((3 - 7 + 10)/3, (-5 + 4 - 2)/3) = G(2.00, -1.00)</div>
    </div>
</div>

<script>
function calcCen15() {
    const x1 = parseFloat(document.getElementById("g-x1").value) || 0;
    const y1 = parseFloat(document.getElementById("g-y1").value) || 0;
    const x2 = parseFloat(document.getElementById("g-x2").value) || 0;
    const y2 = parseFloat(document.getElementById("g-y2").value) || 0;
    const x3 = parseFloat(document.getElementById("g-x3").value) || 0;
    const y3 = parseFloat(document.getElementById("g-y3").value) || 0;

    const dx = (x2 + x3) / 2, dy = (y2 + y3) / 2;
    const gx = (x1 + x2 + x3) / 3, gy = (y1 + y2 + y3) / 3;
    document.getElementById("c7s15-badge").textContent = `G(${gx.toFixed(1)}, ${gy.toFixed(1)})`;
    document.getElementById("c7s15-mid").textContent = `Step 1: Midpoint D of BC = (${dx.toFixed(2)}, ${dy.toFixed(2)})`;
    document.getElementById("c7s15-cen").textContent = `Step 2 (2:1 along AD): Centroid G = (${gx.toFixed(2)}, ${gy.toFixed(2)})`;
}
calcCen15();
</script>
"""

# Simulator 16: Chapter 7 Master Formula Vault & Live Calculator
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📘</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Chapter 7 Formula Vault & Instant Distance / Midpoint Solver</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Ready for Exercises!</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-mono">
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-amber-300 font-bold mb-1">1. Distance Formula</div>
            <div class="text-slate-300">PQ = sqrt[(x₂-x₁)² + (y₂-y₁)²] | Origin OP = sqrt(x² + y²)</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-cyan-300 font-bold mb-1">2. Collinear & Square Tests</div>
            <div class="text-slate-300">Collinear: AB+BC = AC | Square: 4 equal edges + equal diagonals</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-emerald-300 font-bold mb-1">3. Internal Section Formula</div>
            <div class="text-slate-300">((m₁x₂+m₂x₁)/(m₁+m₂), (m₁y₂+m₂y₁)/(m₁+m₂)) | Ratio trick: k : 1</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-purple-300 font-bold mb-1">4. Midpoint & Axis Points</div>
            <div class="text-slate-300">Mid = ((x₁+x₂)/2, (y₁+y₂)/2) | x-axis (x,0), y-axis (0,y)</div>
        </div>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2 text-xs">
        <div class="font-bold text-amber-300">Instant Distance & Midpoint Check for A(x₁, y₁) and B(x₂, y₂):</div>
        <div class="grid grid-cols-4 gap-2">
            <div><span class="text-slate-400">x₁:</span><input type="number" value="-5" id="s16-x1" oninput="calcVault716()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
            <div><span class="text-slate-400">y₁:</span><input type="number" value="7" id="s16-y1" oninput="calcVault716()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
            <div><span class="text-slate-400">x₂:</span><input type="number" value="-1" id="s16-x2" oninput="calcVault716()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
            <div><span class="text-slate-400">y₂:</span><input type="number" value="3" id="s16-y2" oninput="calcVault716()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
        </div>
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-emerald-300 font-mono font-bold text-center" id="s16-out">
            AB = sqrt(32) = 5.66   |   Midpoint M(-3.0, 5.0)
        </div>
    </div>
</div>

<script>
function calcVault716() {
    const x1 = parseFloat(document.getElementById("s16-x1").value) || 0;
    const y1 = parseFloat(document.getElementById("s16-y1").value) || 0;
    const x2 = parseFloat(document.getElementById("s16-x2").value) || 0;
    const y2 = parseFloat(document.getElementById("s16-y2").value) || 0;
    const sq = (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1);
    const dist = Math.sqrt(sq).toFixed(2);
    const mx = ((x1 + x2)/2).toFixed(1), my = ((y1 + y2)/2).toFixed(1);
    document.getElementById("s16-out").textContent = `AB = sqrt(${sq}) = ${dist}   |   Midpoint M(${mx}, ${my})`;
}
</script>
"""
