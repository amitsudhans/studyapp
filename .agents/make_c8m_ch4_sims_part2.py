#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 4: Quadrilaterals
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Rhombus Equal Sides (Compass Construction & Corner Angle Bisection Deduction 9)
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">♦️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Rhombus Compass Builder &amp; Corner Bisection (Deduction 9)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c8c4s9-badge">∠A = 60°</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Adjust Rhombus Corner Angle ∠A (40° to 120°):</span>
            <span class="font-bold text-rose-300 font-mono" id="c8c4s9-av">∠A = 60°</span>
        </div>
        <input type="range" min="40" max="120" step="2" value="60" id="c8c4s9-a" oninput="updC8C4S9()" class="w-full accent-rose-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 110" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800" id="c8c4s9-svg"></svg>
        <div class="font-mono text-xs space-y-2">
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-amber-300 font-bold" id="c8c4s9-half"></div>
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold">SSS ΔABC ≅ ΔADC proves diagonal AC bisects corners &amp; AB ∥ DC, AD ∥ BC!</div>
        </div>
    </div>
</div>

<script>
function updC8C4S9() {
    const deg = parseInt(document.getElementById("c8c4s9-a").value);
    const rad = (deg * Math.PI) / 180;
    const side = 62;
    const ax = 60, ay = 88;
    const bx = ax + side, by = ay;
    const dx = ax + side * Math.cos(rad), dy = ay - side * Math.sin(rad);
    const cx = dx + side, cy = dy;

    document.getElementById("c8c4s9-av").textContent = "∠A = " + deg + "°";
    document.getElementById("c8c4s9-badge").textContent = "∠A = " + deg + "°";
    document.getElementById("c8c4s9-half").textContent = "Diagonal splits ∠A (" + deg + "°) into exact halves: " + (deg / 2) + "° & " + (deg / 2) + "°!";
    document.getElementById("c8c4s9-svg").innerHTML = `
        <polygon points="${ax},${ay} ${bx},${by} ${cx.toFixed(1)},${cy.toFixed(1)} ${dx.toFixed(1)},${dy.toFixed(1)}" fill="#f43f5e" fill-opacity="0.22" stroke="#fb7185" stroke-width="2.5"/>
        <line x1="${ax}" y1="${ay}" x2="${cx.toFixed(1)}" y2="${cy.toFixed(1)}" stroke="#fbbf24" stroke-width="2"/>
    `;
}
updC8C4S9();
</script>
"""

# Simulator 10: Rhombus Diagonal Proofs & Multi-Set Venn Diagram
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⭕</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">Multi-Set Venn Hierarchy &amp; Deduction 10 (90° Rhombus Diagonals)</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c4s10-badge">Square = Rect ∩ Rhom</span>
    </div>

    <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <button onclick="setVennS10(0)" class="px-2.5 py-1 rounded-lg bg-cyan-700 text-white font-bold">Parallelograms</button>
        <button onclick="setVennS10(1)" class="px-2.5 py-1 rounded-lg bg-amber-700 text-white font-bold">Rectangles</button>
        <button onclick="setVennS10(2)" class="px-2.5 py-1 rounded-lg bg-rose-700 text-white font-bold">Rhombuses</button>
        <button onclick="setVennS10(3)" class="px-2.5 py-1 rounded-lg bg-emerald-700 text-white font-bold">Intersection (Square!)</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-amber-300 font-bold text-sm" id="c8c4s10-t"></div>
        <div class="text-cyan-200" id="c8c4s10-d"></div>
        <div class="text-emerald-300 font-bold" id="c8c4s10-p"></div>
    </div>
</div>

<script>
const vennData = [
    { b: "Parallelograms", t: "Outer Set: Parallelograms", d: "2 pairs of parallel sides; opposite sides & angles equal; diagonals bisect cleanly.", p: "Contains ALL Rectangles, Rhombuses, and Squares!" },
    { b: "Rectangles", t: "Left Oval: Rectangles (4 × 90°)", d: "Every Rectangle is a Parallelogram with four 90° angles AND equal diagonals.", p: "Oblong 8×5 rectangle sits outside Squares yet inside Parallelograms." },
    { b: "Rhombuses", t: "Right Oval: Rhombuses (4 Equal Sides)", d: "Deduction 10: SSS ΔGEO ≅ ΔMEO proves diagonals cross at EXACT 90°!", p: "60°-120° diamond sits outside Rectangles yet inside Parallelograms." },
    { b: "Square = Rect ∩ Rhom", t: "Center Intersection: SQUARES", d: "Combines 4 × 90° (Rectangle) AND 4 equal sides (Rhombus)!", p: "Diagonals are EQUAL + PERPENDICULAR (90°) + BISECTING + 45° corner splits!" }
];
function setVennS10(i) {
    const v = vennData[i];
    document.getElementById("c8c4s10-badge").textContent = v.b;
    document.getElementById("c8c4s10-t").textContent = v.t;
    document.getElementById("c8c4s10-d").textContent = v.d;
    document.getElementById("c8c4s10-p").textContent = v.p;
}
setVennS10(3);
</script>
"""

# Simulator 11: Geoboard Diagonal Lab (Lengths + Intersection Angle Switcher)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📌</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Dot-Grid Geoboard Diagonal Lab (Section 4.5)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c4s11-badge">Square</span>
    </div>

    <div class="grid grid-cols-2 gap-2 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <button onclick="setGeoS11(true, 90)" class="p-2 rounded-lg bg-indigo-700 text-white font-bold">Equal + 90° → Square</button>
        <button onclick="setGeoS11(true, 60)" class="p-2 rounded-lg bg-cyan-700 text-white font-bold">Equal + 60° → Rectangle</button>
        <button onclick="setGeoS11(false, 90)" class="p-2 rounded-lg bg-rose-700 text-white font-bold">Unequal + 90° → Rhombus</button>
        <button onclick="setGeoS11(false, 60)" class="p-2 rounded-lg bg-emerald-700 text-white font-bold">Unequal + 60° → Parallelogram</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 110" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800" id="c8c4s11-svg"></svg>
        <div class="font-mono text-xs space-y-2">
            <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800 text-amber-300 font-bold" id="c8c4s11-out"></div>
            <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800 text-cyan-200" id="c8c4s11-why"></div>
        </div>
    </div>
</div>

<script>
function setGeoS11(eq, ang) {
    const r1 = 44;
    const r2 = eq ? 44 : 26;
    const rad = (ang * Math.PI) / 180;
    const cx = 110, cy = 55;
    const p1 = [cx - r1, cy], p3 = [cx + r1, cy];
    const dx = r2 * Math.cos(rad), dy = r2 * Math.sin(rad);
    const p2 = [cx + dx, cy - dy], p4 = [cx - dx, cy + dy];

    let name = "", why = "";
    if (eq && ang === 90) { name = "SQUARE"; why = "Equal perpendicular bisecting diagonals!"; }
    else if (eq) { name = "RECTANGLE"; why = "Equal bisecting diagonals at oblique " + ang + "° angle!"; }
    else if (ang === 90) { name = "RHOMBUS"; why = "Unequal diagonals crossing cleanly at 90°!"; }
    else { name = "PARALLELOGRAM"; why = "Unequal bisecting diagonals at oblique " + ang + "° angle!"; }

    document.getElementById("c8c4s11-badge").textContent = name;
    document.getElementById("c8c4s11-out").textContent = "Resulting Peg Shape: " + name;
    document.getElementById("c8c4s11-why").textContent = why;
    document.getElementById("c8c4s11-svg").innerHTML = `
        <polygon points="${p1[0]},${p1[1]} ${p2[0].toFixed(1)},${p2[1].toFixed(1)} ${p3[0]},${p3[1]} ${p4[0].toFixed(1)},${p4[1].toFixed(1)}" fill="#38bdf8" fill-opacity="0.22" stroke="#38bdf8" stroke-width="2.5"/>
        <line x1="${p1[0]}" y1="${p1[1]}" x2="${p3[0]}" y2="${p3[1]}" stroke="#fbbf24" stroke-width="2"/>
        <line x1="${p2[0].toFixed(1)}" y1="${p2[1].toFixed(1)}" x2="${p4[0].toFixed(1)}" y2="${p4[1].toFixed(1)}" stroke="#34d399" stroke-width="2"/>
    `;
}
setGeoS11(true, 90);
</script>
"""

# Simulator 12: Joining Congruent Triangles (Equilateral, Isosceles, Scalene Pairs)
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔺</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Triangle Pair Assembler (Equilateral, Isosceles, Scalene)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c4s12-badge">Rhombus</span>
    </div>

    <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <button onclick="setTriS12(0)" class="px-2.5 py-1 rounded-lg bg-emerald-700 text-white font-bold">2 Equilateral → Rhombus</button>
        <button onclick="setTriS12(1)" class="px-2.5 py-1 rounded-lg bg-cyan-700 text-white font-bold">2 Isosceles → Rhombus / Kite</button>
        <button onclick="setTriS12(2)" class="px-2.5 py-1 rounded-lg bg-amber-700 text-white font-bold">2 Scalene → Parallelogram / Kite</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-amber-300 font-bold text-sm" id="c8c4s12-res"></div>
        <div class="text-cyan-200" id="c8c4s12-exp"></div>
    </div>
</div>

<script>
const triJoinCases = [
    { b: "Rhombus", r: "2 Identical Equilateral Triangles → ALWAYS 60°–120° Rhombus", e: "All 4 outer edges share equal length s along the boundary!" },
    { b: "Rhombus / Kite", r: "2 Identical Isosceles Triangles → Rhombus OR Kite", e: "Join along base → Rhombus (4 equal legs); reflect/join legs cleanly → Kite!" },
    { b: "Parallelogram / Kite", r: "2 Identical Scalene Triangles → Parallelogram OR Kite", e: "Flip 180° around midpoint → Parallelogram (equal opposite edges); mirror across seam → Kite!" }
];
function setTriS12(i) {
    document.getElementById("c8c4s12-badge").textContent = triJoinCases[i].b;
    document.getElementById("c8c4s12-res").textContent = triJoinCases[i].r;
    document.getElementById("c8c4s12-exp").textContent = triJoinCases[i].e;
}
setTriS12(0);
</script>
"""

# Simulator 13: Kite Symmetric Geometry (AB=BC, CD=DA, 90° Single-Bisected Cross Bar)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪁</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Kite Symmetry &amp; Single-Bisected Diagonal Explorer</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c4s13-badge">∠A = ∠C</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 120" class="w-full h-32 bg-slate-950 rounded-xl border border-slate-800">
            <polygon points="110,12 165,45 110,108 55,45" fill="#f59e0b" fill-opacity="0.2" stroke="#fbbf24" stroke-width="2.5"/>
            <line x1="110" y1="12" x2="110" y2="108" stroke="#34d399" stroke-width="2"/>
            <line x1="55" y1="45" x2="165" y2="45" stroke="#38bdf8" stroke-width="2"/>
            <rect x="110" y="37" width="8" height="8" fill="none" stroke="#34d399" stroke-width="1.5"/>
            <text x="110" y="10" text-anchor="middle" fill="#fde68a" font-size="8">B</text>
            <text x="46" y="48" fill="#7dd3fc" font-size="8">A</text>
            <text x="171" y="48" fill="#7dd3fc" font-size="8">C</text>
            <text x="110" y="118" text-anchor="middle" fill="#fde68a" font-size="8">D</text>
        </svg>
        <div class="font-mono text-xs space-y-2">
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-amber-300 font-bold">Adjacent Equal Pairs: AB = BC (short crown) &amp; CD = DA (long tail)</div>
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold">Main Spine BD bisects ∠B, ∠D, and perpendicularly bisects AC (AO = OC, 90°)!</div>
        </div>
    </div>
</div>
"""

# Simulator 14: Trapezium And Isosceles (Transversal Sum 180° & Congruent Base Angles)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⏢</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Trapezium &amp; Isosceles Base-Angle Slider</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c4s14-badge">Isosceles</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Base Angle ∠V (= ∠W in Isosceles Trapezium):</span>
            <span class="font-bold text-cyan-300 font-mono" id="c8c4s14-vv">68°</span>
        </div>
        <input type="range" min="45" max="85" step="1" value="68" id="c8c4s14-v" oninput="updC8C4S14()" class="w-full accent-cyan-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-amber-300 font-bold" id="c8c4s14-bases"></div>
        <div class="text-emerald-300 font-bold" id="c8c4s14-sum"></div>
    </div>
</div>

<script>
function updC8C4S14() {
    const v = parseInt(document.getElementById("c8c4s14-v").value);
    const t = 180 - v;
    document.getElementById("c8c4s14-vv").textContent = v + "°";
    document.getElementById("c8c4s14-bases").textContent = "Equal Non-Parallel Legs TW = UV → Base Angles Match: ∠V = ∠W = " + v + "°, Top ∠T = ∠U = " + t + "°";
    document.getElementById("c8c4s14-sum").textContent = "Co-Interior Transversal Sum: ∠T + ∠W = " + t + "° + " + v + "° = 180° (All 4 sum to 360°!)";
}
updC8C4S14();
</script>
"""

# Simulator 15: Square Inside Square (Rotated Split Point a:b Proof Explorer)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">💠</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">Square-in-a-Square Proof (SAS Congruent Corner Triangles)</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c4s15-badge">3–4–5 Triangle</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Corner Cut x on 7-cm Outer Square Edge (1 to 6 cm):</span>
            <span class="font-bold text-indigo-300 font-mono" id="c8c4s15-xv">x = 3 cm, y = 4 cm</span>
        </div>
        <input type="range" min="1" max="6" step="1" value="3" id="c8c4s15-x" oninput="updC8C4S15()" class="w-full accent-indigo-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 110" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800" id="c8c4s15-svg"></svg>
        <div class="font-mono text-xs space-y-2">
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold" id="c8c4s15-side"></div>
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-amber-200">All 4 corners form identical SAS right triangles → PQ=QR=RS=SP &amp; 90° inner angles!</div>
        </div>
    </div>
</div>

<script>
function updC8C4S15() {
    const x = parseInt(document.getElementById("c8c4s15-x").value);
    const y = 7 - x;
    const area = x * x + y * y;
    const side = Math.sqrt(area).toFixed(2);
    document.getElementById("c8c4s15-xv").textContent = "x = " + x + " cm, y = " + y + " cm";
    document.getElementById("c8c4s15-badge").textContent = "Area = " + area + " cm²";
    document.getElementById("c8c4s15-side").textContent = "Inner Square Side = √(" + x + "² + " + y + "²) = √" + area + " ≈ " + side + " cm";

    const s = 84, ox = 68, oy = 13;
    const px = (x / 7) * s;
    document.getElementById("c8c4s15-svg").innerHTML = `
        <rect x="${ox}" y="${oy}" width="${s}" height="${s}" fill="none" stroke="#64748b" stroke-width="2"/>
        <polygon points="${ox + px},${oy} ${ox + s},${oy + px} ${ox + s - px},${oy + s} ${ox},${oy + s - px}" fill="#6366f1" fill-opacity="0.3" stroke="#818cf8" stroke-width="2.5"/>
    `;
}
updC8C4S15();
</script>
"""

# Simulator 16: Which Quad Summary & Paper-Folding Simulator
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📄</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Which Quad? Master Property &amp; Paper-Fold Matrix</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c4s16-badge">6 Families</span>
    </div>

    <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <button onclick="pickFoldS16(0)" class="px-2.5 py-1 rounded-lg bg-rose-700 text-white font-bold">Quadrant Fold + Slant Cut → Rhombus</button>
        <button onclick="pickFoldS16(1)" class="px-2.5 py-1 rounded-lg bg-indigo-700 text-white font-bold">Quadrant Fold + 45° Cut → Square</button>
        <button onclick="pickFoldS16(2)" class="px-2.5 py-1 rounded-lg bg-amber-700 text-white font-bold">Single Fold + Unequal Wings → Kite</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-emerald-300 font-bold text-sm" id="c8c4s16-res"></div>
        <div class="text-cyan-200" id="c8c4s16-why"></div>
    </div>
</div>

<script>
const foldCases = [
    { b: "Rhombus Fold", r: "Unfolded Shape: RHOMBUS (4 Equal Cut Edges, 90° Fold Diagonals)", w: "Two orthogonal fold lines act as perpendicular bisecting diagonals!" },
    { b: "Square Fold", r: "Unfolded Shape: SQUARE (45° Cut Creates Equal Diagonals Too!)", w: "Equal cuts along both 90° fold creases produce 4×90° corners + 4 equal edges!" },
    { b: "Kite Fold", r: "Unfolded Shape: KITE (Single Fold Line Reflects Asymmetric Triangle)", w: "One symmetry crease connects short top legs (a=a) and long bottom legs (b=b)!" }
];
function pickFoldS16(i) {
    document.getElementById("c8c4s16-badge").textContent = foldCases[i].b;
    document.getElementById("c8c4s16-res").textContent = foldCases[i].r;
    document.getElementById("c8c4s16-why").textContent = foldCases[i].w;
}
pickFoldS16(0);
</script>
"""

if __name__ == "__main__":
    print(f"Prepared {len(simulators_part2)} interactive simulators (Part 2).")
