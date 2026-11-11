#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 4: Quadrilaterals
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: What Are Quadrilaterals (4-Sided Polygon Validator)
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Quadrilateral Validator (quadri = 4, latus = side)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c4s1-badge">Valid Quad</span>
    </div>

    <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <button onclick="setShapeS1(0)" class="px-2.5 py-1 rounded-lg bg-emerald-700 text-white font-bold">Tilted 4-Gon</button>
        <button onclick="setShapeS1(1)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-rose-300 font-bold border border-slate-700">Curved Edge</button>
        <button onclick="setShapeS1(2)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-rose-300 font-bold border border-slate-700">Open Gap</button>
        <button onclick="setShapeS1(3)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-rose-300 font-bold border border-slate-700">Crossed Bowtie</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 120" class="w-full h-32 bg-slate-950 rounded-xl border border-slate-800" id="c8c4s1-svg"></svg>
        <div class="font-mono text-xs space-y-2">
            <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800 font-bold" id="c8c4s1-verdict"></div>
            <div class="p-2.5 bg-slate-950 rounded-lg border border-slate-800 text-cyan-200" id="c8c4s1-reason"></div>
        </div>
    </div>
</div>

<script>
const quadTests = [
    { b: "VALID Quad ✓", ok: true, svg: '<polygon points="45,25 170,20 190,95 30,98" fill="#10b981" fill-opacity="0.22" stroke="#34d399" stroke-width="3"/>', r: "Closed 4-edge polygon with strictly straight non-intersecting sides!" },
    { b: "INVALID ✗ (Curve)", ok: false, svg: '<path d="M 45 95 L 55 25 Q 115 5 175 25 L 180 95 Z" fill="#f43f5e" fill-opacity="0.2" stroke="#fb7185" stroke-width="3"/>', r: "Top edge is curved — polygons require 4 strictly STRAIGHT segments!" },
    { b: "INVALID ✗ (Open)", ok: false, svg: '<polyline points="45,95 50,25 165,25 175,90" fill="none" stroke="#fb7185" stroke-width="3"/>', r: "Missing bottom closing edge — boundary is OPEN instead of closed!" },
    { b: "INVALID ✗ (Crossed)", ok: false, svg: '<polygon points="45,25 175,95 175,25 45,95" fill="#f43f5e" fill-opacity="0.18" stroke="#fb7185" stroke-width="3"/>', r: "Self-intersecting bowtie fails simple non-crossing 4-sided polygon definition!" }
];
function setShapeS1(i) {
    const t = quadTests[i];
    document.getElementById("c8c4s1-badge").textContent = t.b;
    document.getElementById("c8c4s1-svg").innerHTML = t.svg;
    const v = document.getElementById("c8c4s1-verdict");
    v.className = "p-2.5 bg-slate-950 rounded-lg border border-slate-800 font-bold " + (t.ok ? "text-emerald-300" : "text-rose-300");
    v.textContent = t.ok ? "Accepted: Simple Closed Quadrilateral!" : "Rejected: NOT a Simple Quadrilateral!";
    document.getElementById("c8c4s1-reason").textContent = t.r;
}
setShapeS1(0);
</script>
"""

# Simulator 2: Rectangles And Properties (Deduction 4 Frame Builder)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🖼️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Rectangle Frame Explorer (Four 90° Corners → Parallel &amp; Equal)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c4s2-badge">14 × 8 cm</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Width (AB = DC):</span><span class="font-bold text-cyan-300" id="c8c4s2-wv">14 cm</span></div>
            <input type="range" min="6" max="20" step="1" value="14" id="c8c4s2-w" oninput="updC8C4S2()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Height (AD = BC):</span><span class="font-bold text-amber-300" id="c8c4s2-hv">8 cm</span></div>
            <input type="range" min="4" max="14" step="1" value="8" id="c8c4s2-h" oninput="updC8C4S2()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 120" class="w-full h-32 bg-slate-950 rounded-xl border border-slate-800" id="c8c4s2-svg"></svg>
        <div class="font-mono text-xs space-y-2">
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold" id="c8c4s2-diag"></div>
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-cyan-200" id="c8c4s2-ded4"></div>
        </div>
    </div>
</div>

<script>
function updC8C4S2() {
    const w = parseInt(document.getElementById("c8c4s2-w").value);
    const h = parseInt(document.getElementById("c8c4s2-h").value);
    const diag = Math.sqrt(w * w + h * h).toFixed(2);
    document.getElementById("c8c4s2-wv").textContent = w + " cm";
    document.getElementById("c8c4s2-hv").textContent = h + " cm";
    document.getElementById("c8c4s2-badge").textContent = w + " × " + h + " cm";
    document.getElementById("c8c4s2-diag").textContent = "AC = BD = √(" + w + "²+" + h + "²) = " + diag + " cm (Equal!)";
    document.getElementById("c8c4s2-ded4").textContent = (w === h ? "Special Square (all 4 sides = " + w + " cm)" : "Oblong Rectangle: AB=DC=" + w + ", AD=BC=" + h + ", 4×90°");

    const rw = w * 7, rh = h * 6;
    const x = 110 - rw / 2, y = 60 - rh / 2;
    document.getElementById("c8c4s2-svg").innerHTML = `
        <rect x="${x}" y="${y}" width="${rw}" height="${rh}" fill="#0ea5e9" fill-opacity="0.22" stroke="#38bdf8" stroke-width="2.5"/>
        <line x1="${x}" y1="${y}" x2="${x + rw}" y2="${y + rh}" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="4 3"/>
        <line x1="${x + rw}" y1="${y}" x2="${x}" y2="${y + rh}" stroke="#34d399" stroke-width="1.5" stroke-dasharray="4 3"/>
        <text x="110" y="${y - 4}" text-anchor="middle" fill="#7dd3fc" font-size="9">${w} cm (90° corners)</text>
    `;
}
updC8C4S2();
</script>
"""

# Simulator 3: Rectangle Diagonal Proofs (Carpenter's Equal Bisecting Strips Hinge!)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪚</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Carpenter's Hinged Diagonal Strips Lab (Deductions 1–3)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c4s3-badge">∠O = 60°</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Pivot Angle Between Two Equal Bisecting Strips (25° to 155°):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c4s3-av">60°</span>
        </div>
        <input type="range" min="25" max="155" step="1" value="60" id="c8c4s3-a" oninput="updC8C4S3()" class="w-full accent-amber-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 120" class="w-full h-32 bg-slate-950 rounded-xl border border-slate-800" id="c8c4s3-svg"></svg>
        <div class="font-mono text-xs space-y-2">
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold" id="c8c4s3-shape"></div>
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-cyan-200" id="c8c4s3-proof"></div>
        </div>
    </div>
</div>

<script>
function updC8C4S3() {
    const deg = parseInt(document.getElementById("c8c4s3-a").value);
    const rad = (deg * Math.PI) / 180;
    const R = 50;
    const cx = 110, cy = 60;
    const dx1 = R * Math.cos(rad / 2), dy1 = R * Math.sin(rad / 2);
    const p1 = [cx - dx1, cy - dy1], p2 = [cx + dx1, cy - dy1], p3 = [cx + dx1, cy + dy1], p4 = [cx - dx1, cy + dy1];

    document.getElementById("c8c4s3-av").textContent = deg + "°";
    document.getElementById("c8c4s3-badge").textContent = "∠O = " + deg + "°";
    document.getElementById("c8c4s3-shape").textContent = deg === 90
        ? "Corners = 90° AND Pivot = 90° → EXACT SQUARE!"
        : "Corners ALWAYS = 90° → Always a RECTANGLE!";
    document.getElementById("c8c4s3-proof").textContent = "OA = OB = OC = OD = 5 cm → ΔADC ≅ ΔDAB (SAS) & ΔAOB ≅ ΔCOD (AAS)";

    document.getElementById("c8c4s3-svg").innerHTML = `
        <polygon points="${p1[0].toFixed(1)},${p1[1].toFixed(1)} ${p2[0].toFixed(1)},${p2[1].toFixed(1)} ${p3[0].toFixed(1)},${p3[1].toFixed(1)} ${p4[0].toFixed(1)},${p4[1].toFixed(1)}" fill="#06b6d4" fill-opacity="0.2" stroke="#22d3ee" stroke-width="2.5"/>
        <line x1="${p1[0].toFixed(1)}" y1="${p1[1].toFixed(1)}" x2="${p3[0].toFixed(1)}" y2="${p3[1].toFixed(1)}" stroke="#f59e0b" stroke-width="2.5"/>
        <line x1="${p2[0].toFixed(1)}" y1="${p2[1].toFixed(1)}" x2="${p4[0].toFixed(1)}" y2="${p4[1].toFixed(1)}" stroke="#f59e0b" stroke-width="2.5"/>
        <circle cx="${cx}" cy="${cy}" r="4" fill="#fb7185"/>
    `;
}
updC8C4S3();
</script>
"""

# Simulator 4: Special Rectangle Squares (Deduction 5: 90° Center + 45° Corners + Venn Subset)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🟦</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">Square Diagonal Split (90° Center, 45° Corners) &amp; Venn Subset</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c4s4-badge">Deduction 5</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 120" class="w-full h-32 bg-slate-950 rounded-xl border border-slate-800">
            <rect x="65" y="15" width="90" height="90" fill="#6366f1" fill-opacity="0.22" stroke="#818cf8" stroke-width="2.5"/>
            <line x1="65" y1="15" x2="155" y2="105" stroke="#fbbf24" stroke-width="2"/>
            <line x1="155" y1="15" x2="65" y2="105" stroke="#fbbf24" stroke-width="2"/>
            <rect x="110" y="51" width="9" height="9" fill="none" stroke="#34d399" stroke-width="1.5"/>
            <text x="110" y="42" text-anchor="middle" fill="#34d399" font-size="9" font-weight="bold">90°</text>
            <text x="80" y="29" fill="#fde68a" font-size="8" font-weight="bold">45°</text>
            <text x="70" y="42" fill="#fde68a" font-size="8" font-weight="bold">45°</text>
        </svg>
        <div class="font-mono text-xs space-y-2">
            <div class="p-2 bg-slate-950 rounded-lg border border-indigo-700/50 text-indigo-200 font-bold">Venn Logic: Squares ⊂ Rectangles (Every square IS a rectangle!)</div>
            <div class="p-2 bg-slate-950 rounded-lg border border-emerald-700/50 text-emerald-300 font-bold">SSS ΔAOB ≅ ΔCOB → ∠O = 90° &amp; Corner Split = 45° + 45°</div>
        </div>
    </div>
</div>
"""

# Simulator 5: Quadrilateral Angle Sum (Triangulation + Missing Angle Finder)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔺</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Quadrilateral Angle-Sum Calculator (ΔSEM + ΔSOM = 360°)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c4s5-badge">Sum = 360°</span>
    </div>

    <div class="grid grid-cols-3 gap-2 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">∠A:</span><span class="font-bold text-cyan-300" id="c8c4s5-av">90°</span></div>
            <input type="range" min="30" max="120" step="5" value="90" id="c8c4s5-a" oninput="updC8C4S5()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">∠B:</span><span class="font-bold text-amber-300" id="c8c4s5-bv">90°</span></div>
            <input type="range" min="30" max="120" step="5" value="90" id="c8c4s5-b" oninput="updC8C4S5()" class="w-full accent-amber-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">∠C:</span><span class="font-bold text-emerald-300" id="c8c4s5-cv">90°</span></div>
            <input type="range" min="30" max="120" step="5" value="90" id="c8c4s5-c" oninput="updC8C4S5()" class="w-full accent-emerald-400">
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1 text-center">
        <div class="text-amber-300 font-bold text-sm" id="c8c4s5-d"></div>
        <div class="text-emerald-300 font-bold" id="c8c4s5-trap"></div>
    </div>
</div>

<script>
function updC8C4S5() {
    const a = parseInt(document.getElementById("c8c4s5-a").value);
    const b = parseInt(document.getElementById("c8c4s5-b").value);
    const c = parseInt(document.getElementById("c8c4s5-c").value);
    const d = 360 - (a + b + c);
    document.getElementById("c8c4s5-av").textContent = a + "°";
    document.getElementById("c8c4s5-bv").textContent = b + "°";
    document.getElementById("c8c4s5-cv").textContent = c + "°";
    document.getElementById("c8c4s5-d").textContent = "Forced 4th Angle ∠D = 360° − (" + a + " + " + b + " + " + c + ")° = " + d + "°";
    document.getElementById("c8c4s5-trap").textContent = (a === 90 && b === 90 && c === 90)
        ? "Three 90° corners FORCE ∠D = 90° too — impossible to have EXACTLY 3 right angles!"
        : "Two Triangles (180° + 180° = 360°) hold for EVERY quadrilateral!";
}
updC8C4S5();
</script>
"""

# Simulator 6: Parallel Opposite Sides (Parallelogram Set-Square Tilter)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">▱</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Parallelogram Rail &amp; Compass Explorer</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c4s6-badge">Skew: 30 px</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Slide Top Parallel Rail Sideways:</span>
            <span class="font-bold text-cyan-300 font-mono" id="c8c4s6-sv">Tilt = 30</span>
        </div>
        <input type="range" min="0" max="55" step="5" value="30" id="c8c4s6-s" oninput="updC8C4S6()" class="w-full accent-cyan-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 110" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800" id="c8c4s6-svg"></svg>
        <div class="font-mono text-xs space-y-2">
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold" id="c8c4s6-state"></div>
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-cyan-200">Venn Hierarchy: Squares ⊂ Rectangles ⊂ Parallelograms</div>
        </div>
    </div>
</div>

<script>
function updC8C4S6() {
    const s = parseInt(document.getElementById("c8c4s6-s").value);
    document.getElementById("c8c4s6-sv").textContent = "Tilt = " + s;
    document.getElementById("c8c4s6-badge").textContent = s === 0 ? "Rectangle (90°)" : "Slanted Parallelogram";
    document.getElementById("c8c4s6-state").textContent = s === 0
        ? "Zero tilt → Special Parallelogram (Rectangle)!"
        : "AB ∥ DC & AD ∥ BC maintained cleanly via compass arcs!";
    document.getElementById("c8c4s6-svg").innerHTML = `
        <polygon points="${50 + s},20 ${160 + s},20 160,90 50,90" fill="#06b6d4" fill-opacity="0.22" stroke="#22d3ee" stroke-width="2.5"/>
        <text x="110" y="104" text-anchor="middle" fill="#94a3b8" font-size="8">Both Opposite Pairs Stay Parallel</text>
    `;
}
updC8C4S6();
</script>
"""

# Simulator 7: Parallelogram Angle Rules (Deduction 6 Supplementary & Opposite Equal)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📏</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Deduction 6: Transversal Co-Interior Angles (Sum = 180°)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c4s7-badge">∠A = 65°</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Adjust Corner Angle ∠A (30° to 150°):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c4s7-av">∠A = 65°</span>
        </div>
        <input type="range" min="30" max="150" step="1" value="65" id="c8c4s7-a" oninput="updC8C4S7()" class="w-full accent-amber-400">
    </div>

    <div class="grid grid-cols-4 gap-2 text-center font-mono text-xs" id="c8c4s7-cards"></div>
    <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 font-mono text-xs text-emerald-300 font-bold text-center" id="c8c4s7-law"></div>
</div>

<script>
function updC8C4S7() {
    const a = parseInt(document.getElementById("c8c4s7-a").value);
    const b = 180 - a;
    document.getElementById("c8c4s7-av").textContent = "∠A = " + a + "°";
    document.getElementById("c8c4s7-badge").textContent = "∠A = " + a + "°";
    document.getElementById("c8c4s7-cards").innerHTML = `
        <div class="p-2 rounded-xl bg-slate-900 border border-amber-600/60"><div class="text-[10px] text-amber-400">∠A</div><div class="text-base font-black text-white">${a}°</div></div>
        <div class="p-2 rounded-xl bg-slate-900 border border-cyan-600/60"><div class="text-[10px] text-cyan-400">∠B (Adj)</div><div class="text-base font-black text-cyan-200">${b}°</div></div>
        <div class="p-2 rounded-xl bg-slate-900 border border-amber-600/60"><div class="text-[10px] text-amber-400">∠C (Opp)</div><div class="text-base font-black text-white">${a}°</div></div>
        <div class="p-2 rounded-xl bg-slate-900 border border-cyan-600/60"><div class="text-[10px] text-cyan-400">∠D (Adj)</div><div class="text-base font-black text-cyan-200">${b}°</div></div>
    `;
    document.getElementById("c8c4s7-law").textContent = "Co-Interior: " + a + "° + " + b + "° = 180°   |   Opposite Match: ∠A=∠C=" + a + "°, ∠B=∠D=" + b + "°";
}
updC8C4S7();
</script>
"""

# Simulator 8: Parallelogram Side Proofs (Deductions 7 & 8: Equal Opposite Sides & ASA Bisecting Diagonals)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✂️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Deductions 7 &amp; 8: Opposite Sides &amp; Bisecting Diagonals</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c4s8-badge">ASA Congruence</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800 font-mono text-xs">
        <svg viewBox="0 0 220 110" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800">
            <polygon points="60,20 185,20 155,90 30,90" fill="#10b981" fill-opacity="0.2" stroke="#34d399" stroke-width="2.5"/>
            <line x1="60" y1="20" x2="155" y2="90" stroke="#fbbf24" stroke-width="2"/>
            <line x1="185" y1="20" x2="30" y2="90" stroke="#38bdf8" stroke-width="2"/>
            <circle cx="107.5" cy="55" r="4" fill="#fb7185"/>
            <text x="107.5" y="45" text-anchor="middle" fill="#fda4af" font-size="9" font-weight="bold">O</text>
        </svg>
        <div class="space-y-2">
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold">Deduction 7 (ΔABD ≅ ΔCDB via ASA): AB = CD &amp; AD = BC</div>
            <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-cyan-200 font-bold">Deduction 8 (ΔAOE ≅ ΔYOS via ASA): AO = OY &amp; EO = OS (Diagonals bisect, lengths unequal!)</div>
        </div>
    </div>
</div>
"""

if __name__ == "__main__":
    print(f"Prepared {len(simulators_part1)} interactive simulators (Part 1).")
