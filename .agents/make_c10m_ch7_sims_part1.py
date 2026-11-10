#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 7: Coordinate Geometry
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Coordinate Axes, Abscissa, Ordinate & Axis Points
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧭</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Cartesian Plane Explorer: Abscissa (x), Ordinate (y) & Axis Points (Section 7.1)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c7s1-badge">Quadrant I (+, +)</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Abscissa (x-coordinate):</span><span class="font-bold text-amber-300" id="c7s1-x-disp">x = 3</span></div>
            <input type="range" min="-5" max="5" step="1" value="3" id="c7s1-x" oninput="updateGrid71()" class="w-full accent-amber-400">
        </div>
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Ordinate (y-coordinate):</span><span class="font-bold text-cyan-300" id="c7s1-y-disp">y = 4</span></div>
            <input type="range" min="-5" max="5" step="1" value="4" id="c7s1-y" oninput="updateGrid71()" class="w-full accent-cyan-400">
        </div>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 160" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="c7s1-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
            <div class="text-white font-bold text-sm" id="c7s1-pt">Point P(3, 4)</div>
            <div class="text-amber-300" id="c7s1-ab">Abscissa (horizontal x) = 3</div>
            <div class="text-cyan-300" id="c7s1-or">Ordinate (vertical y) = 4</div>
            <div class="text-emerald-300" id="c7s1-loc">Location: Quadrant I (+, +)</div>
        </div>
    </div>
</div>

<script>
function updateGrid71() {
    const x = parseInt(document.getElementById("c7s1-x").value, 10);
    const y = parseInt(document.getElementById("c7s1-y").value, 10);
    document.getElementById("c7s1-x-disp").textContent = "x = " + x;
    document.getElementById("c7s1-y-disp").textContent = "y = " + y;
    document.getElementById("c7s1-pt").textContent = `Point P(${x}, ${y})`;
    document.getElementById("c7s1-ab").textContent = `Abscissa (x-coord) = ${x}  (dist from y-axis)`;
    document.getElementById("c7s1-or").textContent = `Ordinate (y-coord) = ${y}  (dist from x-axis)`;

    let loc = "";
    if (x === 0 && y === 0) loc = "Origin O(0, 0)";
    else if (y === 0) loc = "Strictly ON the x-axis (y = 0)";
    else if (x === 0) loc = "Strictly ON the y-axis (x = 0)";
    else if (x > 0 && y > 0) loc = "Quadrant I (+, +)";
    else if (x < 0 && y > 0) loc = "Quadrant II (-, +)";
    else if (x < 0 && y < 0) loc = "Quadrant III (-, -)";
    else loc = "Quadrant IV (+, -)";

    document.getElementById("c7s1-badge").textContent = loc;
    document.getElementById("c7s1-loc").textContent = "Location: " + loc;

    const ox = 110, oy = 80, step = 15;
    const px = ox + x * step;
    const py = oy - y * step;
    document.getElementById("c7s1-svg").innerHTML = `
        <line x1="15" y1="${oy}" x2="205" y2="${oy}" stroke="#475569" stroke-width="1.5" />
        <line x1="${ox}" y1="10" x2="${ox}" y2="150" stroke="#475569" stroke-width="1.5" />
        <line x1="${ox}" y1="${py}" x2="${px}" y2="${py}" stroke="#fbbf24" stroke-width="1" stroke-dasharray="3,2" />
        <line x1="${px}" y1="${oy}" x2="${px}" y2="${py}" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,2" />
        <circle cx="${px}" cy="${py}" r="5" fill="#34d399" stroke="#fff" stroke-width="1.5" />
        <text x="${px + 8}" y="${py - 6}" fill="#6ee7b7" font-size="10" font-weight="bold">P(${x},${y})</text>
        <text x="198" y="${oy - 4}" fill="#94a3b8" font-size="9">X</text>
        <text x="${ox + 5}" y="18" fill="#94a3b8" font-size="9">Y</text>
    `;
}
updateGrid71();
</script>
"""

# Simulator 2: Axes Distance & Origin Distance sqrt(x^2 + y^2) (Town A-B 39 km)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🛣️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Town A-B Right Triangle & Origin Distance Formula √(x² + y²)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c7s2-badge">OP = 39.00 km</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="setOrig72(36, 15)" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Town B (36, 15)</button>
        <button onclick="setOrig72(-6, 8)" class="p-2 rounded-xl bg-slate-900 text-cyan-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">(-6, 8) -> d = 10</button>
        <button onclick="setOrig72(5, 12)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">(5, 12) -> d = 13</button>
    </div>

    <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800">
            <label class="text-slate-400 block mb-1">East / Horizontal x:</label>
            <input type="number" value="36" id="c7s2-x" oninput="calcOrig72()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono">
        </div>
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800">
            <label class="text-slate-400 block mb-1">North / Vertical y:</label>
            <input type="number" value="15" id="c7s2-y" oninput="calcOrig72()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono">
        </div>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c7s2-step">OP^2 = (36)^2 + (15)^2 = 1296 + 225 = 1521</div>
        <div class="text-emerald-300 font-bold text-sm" id="c7s2-res">OP = sqrt(1521) = 39.00 units</div>
    </div>
</div>

<script>
function setOrig72(x, y) {
    document.getElementById("c7s2-x").value = x;
    document.getElementById("c7s2-y").value = y;
    calcOrig72();
}
function calcOrig72() {
    const x = parseFloat(document.getElementById("c7s2-x").value) || 0;
    const y = parseFloat(document.getElementById("c7s2-y").value) || 0;
    const sq = x * x + y * y;
    const dist = Math.sqrt(sq);
    document.getElementById("c7s2-badge").textContent = "OP = " + dist.toFixed(2);
    document.getElementById("c7s2-step").textContent = `Pythagoras from O(0,0): (${x})^2 + (${y})^2 = ${x*x} + ${y*y} = ${sq}`;
    document.getElementById("c7s2-res").textContent = `Distance OP = sqrt(${sq}) = ${dist.toFixed(2)} units`;
}
calcOrig72();
</script>
"""

# Simulator 3: Universal Distance Formula Calculator (with Right Triangle SVG)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Universal Distance Formula Lab: PQ = √[(x₂−x₁)² + (y₂−y₁)²]</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c7s3-badge">PQ = √8 ≈ 2.83</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="setPts73(2,3, 4,1)" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 7.1 Q1(i): (2,3) & (4,1)</button>
        <button onclick="setPts73(-5,7, -1,3)" class="p-2 rounded-xl bg-slate-900 text-cyan-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 7.1 Q1(ii): (-5,7) & (-1,3)</button>
        <button onclick="setPts73(1,-1, 4,3)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">(1,-1) & (4,3) -> d = 5</button>
    </div>

    <div class="grid grid-cols-4 gap-2 text-xs">
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800"><span class="text-slate-400">x₁:</span><input type="number" value="2" id="c7s3-x1" oninput="calcDist73()" class="w-full bg-slate-950 text-white p-1 rounded border border-slate-700 font-mono"></div>
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800"><span class="text-slate-400">y₁:</span><input type="number" value="3" id="c7s3-y1" oninput="calcDist73()" class="w-full bg-slate-950 text-white p-1 rounded border border-slate-700 font-mono"></div>
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800"><span class="text-slate-400">x₂:</span><input type="number" value="4" id="c7s3-x2" oninput="calcDist73()" class="w-full bg-slate-950 text-white p-1 rounded border border-slate-700 font-mono"></div>
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800"><span class="text-slate-400">y₂:</span><input type="number" value="1" id="c7s3-y2" oninput="calcDist73()" class="w-full bg-slate-950 text-white p-1 rounded border border-slate-700 font-mono"></div>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c7s3-legs">Horizontal dx = (4 - 2) = 2   |   Vertical dy = (1 - 3) = -2</div>
        <div class="text-emerald-300 font-bold text-sm" id="c7s3-res">PQ = sqrt(2^2 + (-2)^2) = sqrt(8) = 2.83 units</div>
    </div>
</div>

<script>
function setPts73(x1,y1, x2,y2) {
    document.getElementById("c7s3-x1").value = x1;
    document.getElementById("c7s3-y1").value = y1;
    document.getElementById("c7s3-x2").value = x2;
    document.getElementById("c7s3-y2").value = y2;
    calcDist73();
}
function calcDist73() {
    const x1 = parseFloat(document.getElementById("c7s3-x1").value) || 0;
    const y1 = parseFloat(document.getElementById("c7s3-y1").value) || 0;
    const x2 = parseFloat(document.getElementById("c7s3-x2").value) || 0;
    const y2 = parseFloat(document.getElementById("c7s3-y2").value) || 0;
    const dx = x2 - x1;
    const dy = y2 - y1;
    const sq = dx * dx + dy * dy;
    const dist = Math.sqrt(sq);
    document.getElementById("c7s3-badge").textContent = `PQ = √${sq} ≈ ${dist.toFixed(2)}`;
    document.getElementById("c7s3-legs").textContent = `Horizontal dx = (${x2} - ${x1}) = ${dx}   |   Vertical dy = (${y2} - ${y1}) = ${dy}`;
    document.getElementById("c7s3-res").textContent = `PQ = sqrt((${dx})^2 + (${dy})^2) = sqrt(${sq}) = ${dist.toFixed(2)} units`;
}
calcDist73();
</script>
"""

# Simulator 4: Triangle Classifier (Right, Isosceles, Equilateral, Scalene)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔺</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Coordinate Triangle Classifier (Example 1 & Exercise 7.1 Q4)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800" id="c7s4-badge">Right-Angled △</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="classifyTri74(0)" id="btn-74-0" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">Ex 1: (3,2), (-2,-3), (2,3)</button>
        <button onclick="classifyTri74(1)" id="btn-74-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 7.1 Q4: (5,-2),(6,4),(7,-2)</button>
        <button onclick="classifyTri74(2)" id="btn-74-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Equilateral (0,0),(6,0),(3,5.2)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c7s4-sides"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c7s4-verdict"></div>
    </div>
</div>

<script>
const triCases74 = [
    {
        badge: "Right-Angled Triangle!",
        sides: "PQ^2 = 50 (PQ = 5*sqrt(2)),   QR^2 = 52 (QR = 2*sqrt(13)),   PR^2 = 2 (PR = sqrt(2))",
        verdict: "CONVERSE OF PYTHAGORAS: PQ^2 + PR^2 = 50 + 2 = 52 = QR^2  =>  Right-angled at P!"
    },
    {
        badge: "Isosceles Triangle!",
        sides: "AB = sqrt((6-5)^2 + (4+2)^2) = sqrt(37)   |   BC = sqrt(37)   |   AC = 2",
        verdict: "TWO EQUAL SIDES (AB = BC = sqrt(37))  =>  Isosceles Triangle!"
    },
    {
        badge: "Equilateral Triangle!",
        sides: "PQ = 6.00   |   QR = 6.00   |   PR = 6.00 (for R = (3, 3*sqrt(3)))",
        verdict: "ALL THREE SIDES EQUAL (6 = 6 = 6)  =>  Equilateral Triangle!"
    }
];
function classifyTri74(i) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-74-" + k).className = (k === i)
            ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    }
    document.getElementById("c7s4-badge").textContent = triCases74[i].badge;
    document.getElementById("c7s4-sides").textContent = triCases74[i].sides;
    document.getElementById("c7s4-verdict").textContent = triCases74[i].verdict;
}
classifyTri74(0);
</script>
"""

# Simulator 5: Verifying Square vs Rhombus vs Parallelogram (4 sides + 2 diagonals)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🟦</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Quadrilateral Verifier: 4 Edges + 2 Diagonals (Ex 7.1 Q5 & Q6)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c7s5-badge">True SQUARE!</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="checkQuad75(0)" id="btn-75-0" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Seats Square (Q5)</button>
        <button onclick="checkQuad75(1)" id="btn-75-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Tilted Rhombus</button>
        <button onclick="checkQuad75(2)" id="btn-75-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Parallelogram (Q6 iii)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c7s5-edges"></div>
        <div class="text-amber-300" id="c7s5-diags"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c7s5-ver"></div>
    </div>
</div>

<script>
const quadCases75 = [
    {
        badge: "SQUARE Verified!",
        edges: "All 4 Edges Equal: AB = BC = CD = DA = sqrt(18) = 3*sqrt(2)",
        diags: "Both Diagonals Equal: AC = 6  and  BD = 6!",
        ver: "4 Equal Sides + 2 Equal Diagonals  =>  True 90° SQUARE! (Ex 7.1 Q5)"
    },
    {
        badge: "RHOMBUS Only!",
        edges: "All 4 Edges Equal: AB = BC = CD = DA = 5",
        diags: "Diagonals UNEQUAL: AC = 6  !=  BD = 8!",
        ver: "4 Equal Sides + Unequal Diagonals  =>  RHOMBUS (Corners are NOT 90°)!"
    },
    {
        badge: "PARALLELOGRAM!",
        edges: "Opposite Edges Equal: AB = CD = sqrt(10)  and  BC = DA = 3*sqrt(2)",
        diags: "Diagonals UNEQUAL: AC = 2  !=  BD = sqrt(52)!",
        ver: "Opposite Sides Equal + Unequal Diagonals  =>  PARALLELOGRAM! (Ex 7.1 Q6 iii)"
    }
];
function checkQuad75(i) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-75-" + k).className = (k === i)
            ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    }
    document.getElementById("c7s5-badge").textContent = quadCases75[i].badge;
    document.getElementById("c7s5-edges").textContent = quadCases75[i].edges;
    document.getElementById("c7s5-diags").textContent = quadCases75[i].diags;
    document.getElementById("c7s5-ver").textContent = quadCases75[i].ver;
}
checkQuad75(0);
</script>
"""

# Simulator 6: Collinearity Tester (AB + BC == AC)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📏</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Collinearity Detector: Does AB + BC = AC? (Ex 7.1 Q3)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c7s6-badge">NOT Collinear</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="testCol76(false)" id="btn-76-no" class="p-2 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">Ex 7.1 Q3: (1,5), (2,3), (-2,-11)</button>
        <button onclick="testCol76(true)" id="btn-76-yes" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Collinear: (1,2), (3,6), (4,8)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c7s6-segs"></div>
        <div class="text-amber-300" id="c7s6-sum"></div>
        <div class="font-bold text-sm" id="c7s6-ver"></div>
    </div>
</div>

<script>
function testCol76(isCol) {
    document.getElementById("btn-76-no").className = !isCol
        ? "p-2 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-76-yes").className = isCol
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";

    const badge = document.getElementById("c7s6-badge");
    const ver = document.getElementById("c7s6-ver");
    if (!isCol) {
        badge.textContent = "NOT Collinear";
        badge.className = "text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-700";
        document.getElementById("c7s6-segs").textContent = "AB = sqrt(5) ≈ 2.24   |   BC = sqrt(212) ≈ 14.56   |   AC = sqrt(265) ≈ 16.28";
        document.getElementById("c7s6-sum").textContent = "Sum of two shorter: 2.24 + 14.56 = 16.80  !=  16.28";
        ver.textContent = "FAILS! AB + BC != AC -> Points do NOT lie on one straight line!";
        ver.className = "font-bold text-sm text-rose-400";
    } else {
        badge.textContent = "COLLINEAR!";
        badge.className = "text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-700";
        document.getElementById("c7s6-segs").textContent = "AB = 2*sqrt(5)   |   BC = sqrt(5)   |   AC = 3*sqrt(5)";
        document.getElementById("c7s6-sum").textContent = "Exact Check: 2*sqrt(5) + 1*sqrt(5) = 3*sqrt(5) = AC!";
        ver.textContent = "COLLINEAR! All three points lie strictly on the same straight line!";
        ver.className = "font-bold text-sm text-emerald-300";
    }
}
testCol76(false);
</script>
"""

# Simulator 7: Equidistant Axis Solver & Perpendicular Bisector Relation
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚖️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Equidistant Solver: Squaring PA² = PB² Cancels x² & y² (Ex 7.1 Q7-10)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c7s7-badge">P(-7, 0)</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="showEq77(0)" id="btn-77-0" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">x-axis P(x,0) [Q7]</button>
        <button onclick="showEq77(1)" id="btn-77-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">y-axis P(0,y) [Ex 5]</button>
        <button onclick="showEq77(2)" id="btn-77-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Bisector Line [Q10]</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="c7s7-setup"></div>
        <div class="text-cyan-300" id="c7s7-cancel"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c7s7-ans"></div>
    </div>
</div>

<script>
const eqData77 = [
    {
        badge: "P(-7, 0)",
        setup: "Point P(x, 0) equidistant from A(2, -5) and B(-2, 9):",
        cancel: "(x - 2)^2 + 25 = (x + 2)^2 + 81  =>  -4x + 29 = 4x + 85  (x^2 cancels!)",
        ans: "8x = -56  =>  x = -7  =>  Point on x-axis is (-7, 0)!"
    },
    {
        badge: "P(0, 9)",
        setup: "Point P(0, y) equidistant from A(6, 5) and B(-4, 3):",
        cancel: "36 + (y - 5)^2 = 16 + (y - 3)^2  =>  61 - 10y = 25 - 6y  (y^2 cancels!)",
        ans: "4y = 36  =>  y = 9  =>  Point on y-axis is (0, 9)!"
    },
    {
        badge: "3x + y = 5",
        setup: "General point P(x, y) equidistant from A(3, 6) and B(-3, 4):",
        cancel: "(x-3)^2 + (y-6)^2 = (x+3)^2 + (y-4)^2  =>  -6x - 12y + 45 = 6x - 8y + 25",
        ans: "12x + 4y = 20  =>  Divide by 4: 3x + y = 5 (Perpendicular Bisector)!"
    }
];
function showEq77(i) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-77-" + k).className = (k === i)
            ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    }
    document.getElementById("c7s7-badge").textContent = eqData77[i].badge;
    document.getElementById("c7s7-setup").textContent = eqData77[i].setup;
    document.getElementById("c7s7-cancel").textContent = eqData77[i].cancel;
    document.getElementById("c7s7-ans").textContent = eqData77[i].ans;
}
showEq77(0);
</script>
"""

# Simulator 8: Section Formula Interactive Divider (AA Similarity Visualization)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✂️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Internal Section Formula Lab (Section 7.3 — via AA Similarity)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c7s8-badge">P(1.00, 3.00)</span>
    </div>

    <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
            <div class="flex justify-between"><span class="text-slate-300">Weight m₁ (towards B):</span><span class="font-bold text-amber-300" id="c7s8-m1-d">2</span></div>
            <input type="range" min="1" max="7" value="2" id="c7s8-m1" oninput="calcSec78()" class="w-full accent-amber-400">
        </div>
        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
            <div class="flex justify-between"><span class="text-slate-300">Weight m₂ (towards A):</span><span class="font-bold text-cyan-300" id="c7s8-m2-d">3</span></div>
            <input type="range" min="1" max="7" value="3" id="c7s8-m2" oninput="calcSec78()" class="w-full accent-cyan-400">
        </div>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 95" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="c7s8-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono space-y-1">
            <div class="text-cyan-300" id="c7s8-fx">x = (2*(4) + 3*(-1)) / (2 + 3) = 5 / 5 = 1.00</div>
            <div class="text-emerald-300 font-bold" id="c7s8-fy">y = (2*(-3) + 3*(7)) / (2 + 3) = 15 / 5 = 3.00  =>  P(1.00, 3.00)</div>
        </div>
    </div>
</div>

<script>
function calcSec78() {
    // Ex 7.2 Q1 endpoints: A(-1, 7) and B(4, -3)
    const x1 = -1, y1 = 7, x2 = 4, y2 = -3;
    const m1 = parseInt(document.getElementById("c7s8-m1").value, 10);
    const m2 = parseInt(document.getElementById("c7s8-m2").value, 10);
    document.getElementById("c7s8-m1-d").textContent = m1;
    document.getElementById("c7s8-m2-d").textContent = m2;

    const px = (m1 * x2 + m2 * x1) / (m1 + m2);
    const py = (m1 * y2 + m2 * y1) / (m1 + m2);
    document.getElementById("c7s8-badge").textContent = `P(${px.toFixed(2)}, ${py.toFixed(2)})`;
    document.getElementById("c7s8-fx").textContent = `x = (${m1}*(${x2}) + ${m2}*(${x1})) / (${m1}+${m2}) = ${px.toFixed(2)}`;
    document.getElementById("c7s8-fy").textContent = `y = (${m1}*(${y2}) + ${m2}*(${y1})) / (${m1}+${m2}) = ${py.toFixed(2)}  =>  Ratio ${m1}:${m2}`;

    const t = m1 / (m1 + m2);
    const ax = 45, ay = 20, bx = 315, by = 72;
    const sx = ax + t * (bx - ax), sy = ay + t * (by - ay);
    document.getElementById("c7s8-svg").innerHTML = `
        <line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#475569" stroke-width="2.5" />
        <line x1="${ax}" y1="${ay}" x2="${sx}" y2="${sy}" stroke="#fbbf24" stroke-width="3" />
        <line x1="${sx}" y1="${sy}" x2="${bx}" y2="${by}" stroke="#38bdf8" stroke-width="3" />
        <circle cx="${ax}" cy="${ay}" r="4.5" fill="#fbbf24" />
        <circle cx="${bx}" cy="${by}" r="4.5" fill="#38bdf8" />
        <circle cx="${sx}" cy="${sy}" r="5.5" fill="#34d399" stroke="#fff" stroke-width="1.5" />
        <text x="${ax}" y="14" fill="#fcd34d" font-size="9.5" text-anchor="middle">A(-1, 7)</text>
        <text x="${bx}" y="86" fill="#7dd3fc" font-size="9.5" text-anchor="middle">B(4, -3)</text>
        <text x="${sx}" y="${sy - 10}" fill="#6ee7b7" font-size="10" font-weight="bold" text-anchor="middle">P(${px.toFixed(1)}, ${py.toFixed(1)})</text>
    `;
}
calcSec78();
</script>
"""
