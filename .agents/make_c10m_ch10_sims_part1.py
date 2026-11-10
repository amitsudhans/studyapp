#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 10: Circles
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Three Circle-Line Relationships (Non-intersecting, Secant, Tangent)
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⭕</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Circle-Line Relationships Explorer (Section 10.1)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c10s1-badge">Tangent (1 Point)</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickLine101(0)" id="btn-101-0" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Non-Intersecting (0 pts)</button>
        <button onclick="pickLine101(1)" id="btn-101-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Secant (2 pts)</button>
        <button onclick="pickLine101(2)" id="btn-101-2" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Tangent (1 pt)</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 120" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="c10s1-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold" id="c10s1-info"></div>
    </div>
</div>

<script>
function pickLine101(mode) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-101-" + k).className = (k === mode)
            ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    }
    const svg = document.getElementById("c10s1-svg");
    const cx = 180, cy = 60, r = 40;
    let extra = "";
    if (mode === 0) {
        document.getElementById("c10s1-badge").textContent = "0 Shared Points";
        extra = `<line x1="60" y1="110" x2="300" y2="110" stroke="#94a3b8" stroke-width="2.5" />
                 <text x="180" y="103" fill="#cbd5e1" font-size="9.5" text-anchor="middle">Non-Intersecting Line (Zero common points)</text>`;
        document.getElementById("c10s1-info").textContent = "Distance > Radius r: Line misses circle completely -> ZERO intersection points!";
    } else if (mode === 1) {
        document.getElementById("c10s1-badge").textContent = "Secant (2 Points)";
        extra = `<line x1="60" y1="45" x2="300" y2="45" stroke="#fbbf24" stroke-width="2.5" />
                 <circle cx="143" cy="45" r="4" fill="#f43f5e" /><circle cx="217" cy="45" r="4" fill="#f43f5e" />
                 <text x="135" y="38" fill="#fda4af" font-size="9.5">A</text><text x="223" y="38" fill="#fda4af" font-size="9.5">B</text>`;
        document.getElementById("c10s1-info").textContent = "SECANT cuts through the circle at TWO distinct points A and B!";
    } else {
        document.getElementById("c10s1-badge").textContent = "Tangent (1 Point)";
        extra = `<line x1="60" y1="100" x2="300" y2="100" stroke="#34d399" stroke-width="2.5" />
                 <circle cx="180" cy="100" r="4.5" fill="#fde047" />
                 <text x="180" y="114" fill="#6ee7b7" font-size="9.5" font-weight="bold" text-anchor="middle">Point of Contact P (1 Unique Point — Wheel on Ground!)</text>`;
        document.getElementById("c10s1-info").textContent = "TANGENT touches cleanly at ONE single point P — just like a wheel on road or taut pulley rope!";
    }
    svg.innerHTML = `<circle cx="${cx}" cy="${cy}" r="${r}" fill="rgba(56,189,248,0.12)" stroke="#38bdf8" stroke-width="2" />
                     <circle cx="${cx}" cy="${cy}" r="3" fill="#fff" />${extra}`;
}
pickLine101(2);
</script>
"""

# Simulator 2: Rotating Secant Limiting Case Activity
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎡</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Rotating Secant -> Tangent Limit Activity (Section 10.2)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c10s2-badge">TANGENT REACHED!</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Rotate Secant Until Chord Endpoints P & Q Coincide (Tilt = 0°):</span><span class="font-bold text-amber-300" id="c10s2-d">Tilt = 0°</span></div>
        <input type="range" min="-45" max="45" step="5" value="0" id="c10s2-ang" oninput="rotSec102()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c10s2-ch">Chord Length PQ = 0.00 cm (Endpoints Merged!)</div>
        <div class="font-bold text-sm" id="c10s2-res">Tilt 0°: Q coincides completely onto P -> Tangent (Max 2 parallel tangents per slope!)</div>
    </div>
</div>

<script>
function rotSec102() {
    const tilt = parseInt(document.getElementById("c10s2-ang").value, 10);
    document.getElementById("c10s2-d").textContent = "Tilt = " + tilt + "°";
    const chord = (2 * 5 * Math.abs(Math.sin(tilt * Math.PI / 180))).toFixed(2);
    const badge = document.getElementById("c10s2-badge");
    const res = document.getElementById("c10s2-res");
    if (tilt === 0) {
        badge.textContent = "TANGENT (Coincident!)";
        badge.className = "text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-700";
        document.getElementById("c10s2-ch").textContent = "Chord Length PQ = 0.00 cm (P & Q Coincided!)";
        res.textContent = "EXACT TANGENT LIMIT! Secant chord length shrank to zero -> Single Contact Point P!";
        res.className = "font-bold text-sm text-emerald-300";
    } else {
        badge.textContent = "SECANT (2 Hits)";
        badge.className = "text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800";
        document.getElementById("c10s2-ch").textContent = `Chord Length PQ ≈ ${chord} cm (2 Distinct Intersections P & Q)`;
        res.textContent = `Active Secant at ${tilt}°! Slide slider toward 0° to merge Q smoothly onto P!`;
        res.className = "font-bold text-sm text-amber-300";
    }
}
rotSec102();
</script>
"""

# Simulator 3: Theorem 10.1 Shortest Distance Proof (OQ > OP)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Theorem 10.1 Shortest-Distance Proof: OP ⊥ XY</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c10s3-badge">OP = r (SHORTEST!)</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Move Point Q along Tangent XY (PQ = 0 places Q right at P):</span><span class="font-bold text-amber-300" id="c10s3-q-d">PQ = 6 cm</span></div>
        <input type="range" min="-8" max="8" step="2" value="6" id="c10s3-q" oninput="prove101()" class="w-full accent-emerald-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c10s3-len">Radius OP = 5.00 cm   |   Distance OQ = sqrt(5^2 + 6^2) = 7.81 cm</div>
        <div class="text-emerald-300 font-bold text-sm" id="c10s3-ver">For every Q != P: OQ (7.81) > OP (5.00)! Shortest distance OP MUST be perpendicular (OP ⊥ XY)!</div>
    </div>
</div>

<script>
function prove101() {
    const pq = parseInt(document.getElementById("c10s3-q").value, 10);
    const oq = Math.sqrt(25 + pq * pq);
    document.getElementById("c10s3-q-d").textContent = "PQ = " + pq + " cm";
    document.getElementById("c10s3-len").textContent = `Radius OP = 5.00 cm   |   Distance OQ = sqrt(25 + ${pq*pq}) = ${oq.toFixed(2)} cm`;
    const v = document.getElementById("c10s3-ver");
    if (pq === 0) {
        v.textContent = "Q == P (On Circle): Shortest Distance = Radius 5.00 cm  =>  ∠OPQ = 90° strictly!";
    } else {
        v.textContent = `Q lies strictly OUTSIDE circle: OQ (${oq.toFixed(2)}) > OP (5.00)  =>  OP is shortest, so OP ⊥ XY!`;
    }
}
prove101();
</script>
"""

# Simulator 4: Normals, Uniqueness & Ex 10.1 Pythagoras Solver
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧮</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Normal Line & Ex 10.1 Pythagoras Tangent Solver (∠P = 90°)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800" id="c10s4-badge">PQ = √119 cm</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="setEx101(5, 12)" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 10.1 Q3: r=5, OQ=12</button>
        <button onclick="setEx101(7, 25)" class="p-2 rounded-xl bg-slate-900 text-cyan-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 10.2 Q1: r=7, OQ=25 (PQ=24)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300" id="c10s4-hyp">Right Angle at Contact P (Radius OP is the NORMAL!): Hypotenuse OQ = 12 cm</div>
        <div class="text-emerald-300 font-bold text-sm" id="c10s4-res">Tangent PQ = sqrt(12^2 - 5^2) = sqrt(119) ≈ 10.91 cm!</div>
    </div>
</div>

<script>
function setEx101(r, oq) {
    const pq2 = oq * oq - r * r;
    const pq = Math.sqrt(pq2);
    document.getElementById("c10s4-badge").textContent = `PQ = √${pq2}`;
    document.getElementById("c10s4-hyp").textContent = `Right angle ALWAYS sits at contact P (Line OP is NORMAL)! Hypotenuse OQ = ${oq}, Radius = ${r}`;
    document.getElementById("c10s4-res").textContent = `Tangent PQ = sqrt(${oq}^2 - ${r}^2) = sqrt(${pq2}) ≈ ${pq.toFixed(2)} cm!`;
}
setEx101(5, 12);
</script>
"""

# Simulator 5: Number of Tangents From Interior, Boundary & External Point
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎯</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Point Region Counter: 0 vs 1 vs 2 Tangents (Section 10.3)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c10s5-badge">2 Tangents!</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickReg105(0)" id="btn-105-0" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Inside Circle (0)</button>
        <button onclick="pickReg105(1)" id="btn-105-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">On Circle (1)</button>
        <button onclick="pickReg105(2)" id="btn-105-2" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Outside Circle (2)</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 115" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="c10s5-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold" id="c10s5-info"></div>
    </div>
</div>

<script>
function pickReg105(rMode) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-105-" + k).className = (k === rMode)
            ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    }
    const cx = 120, cy = 58, rad = 38;
    let extra = "";
    if (rMode === 0) {
        document.getElementById("c10s5-badge").textContent = "0 Tangents!";
        extra = `<circle cx="132" cy="58" r="4" fill="#f43f5e" />
                 <line x1="70" y1="38" x2="180" y2="75" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,2" />
                 <text x="195" y="60" fill="#fda4af" font-size="10" font-weight="bold">Inside P -> Every line cuts twice (0 Tangents!)</text>`;
        document.getElementById("c10s5-info").textContent = "Point INSIDE circle: Every straight ray through P cuts the boundary twice as a secant -> ZERO tangents!";
    } else if (rMode === 1) {
        document.getElementById("c10s5-badge").textContent = "1 Unique Tangent!";
        extra = `<circle cx="${cx+rad}" cy="${cy}" r="4.5" fill="#34d399" />
                 <line x1="${cx+rad}" y1="10" x2="${cx+rad}" y2="108" stroke="#34d399" stroke-width="2.5" />
                 <text x="195" y="60" fill="#6ee7b7" font-size="10" font-weight="bold">On Circle P -> Exactly 1 Unique Tangent!</text>`;
        document.getElementById("c10s5-info").textContent = "Point ON circle: Only ONE line stands perpendicular to radius OP -> Exactly ONE tangent!";
    } else {
        document.getElementById("c10s5-badge").textContent = "2 Equal Tangents!";
        extra = `<circle cx="275" cy="58" r="4.5" fill="#fbbf24" />
                 <line x1="275" y1="58" x2="132" y2="22" stroke="#34d399" stroke-width="2" />
                 <line x1="275" y1="58" x2="132" y2="94" stroke="#34d399" stroke-width="2" />
                 <text x="275" y="75" fill="#fcd34d" font-size="10" font-weight="bold" text-anchor="middle">External P</text>
                 <text x="200" y="25" fill="#6ee7b7" font-size="9.5">PT1 = PT2</text>`;
        document.getElementById("c10s5-info").textContent = "Point OUTSIDE circle: Exactly TWO equal tangent segments PT1 and PT2 can be drawn!";
    }
    document.getElementById("c10s5-svg").innerHTML = `<circle cx="${cx}" cy="${cy}" r="${rad}" fill="rgba(56,189,248,0.12)" stroke="#38bdf8" stroke-width="2" />${extra}`;
}
pickReg105(2);
</script>
"""

# Simulator 6: Theorem 10.2 RHS Congruence Explorer (PQ = PR & Angle Bisector)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚖️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Theorem 10.2 RHS Congruence Proof: Tangents PQ = PR</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">△OQP ≅ △ORP (RHS)</span>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Compare Right Triangles OQP and ORP (with external tangents PQ & PR):</div>
        <div class="text-cyan-300">1) R (Right Angle): ∠OQP = ∠ORP = 90°   [by Theorem 10.1]</div>
        <div class="text-cyan-300">2) H (Hypotenuse):  OP = OP               [common central segment]</div>
        <div class="text-cyan-300">3) S (Equal Side):  OQ = OR = radius r    [same circle radii]</div>
        <div class="text-emerald-300 font-bold text-sm">Therefore △OQP ≅ △ORP (RHS)  =>  PQ = PR  AND  ∠QPO = ∠RPO (Bisector)!</div>
    </div>
</div>
"""

# Simulator 7: Concentric Circles Chord Bisector Calculator (Ex 1 & Ex 10.2 Q7)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎯</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Concentric Circles Chord Calculator: AB = 2√(R² − r²) (Ex 1 & Q7)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c10s7-badge">Chord AB = 8.0 cm</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="setConc107(5, 3)" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 10.2 Q7: R=5, r=3 (AB=8)</button>
        <button onclick="setConc107(10, 6)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">R=10, r=6 (AB=16)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c10s7-half">Theorem 10.1 (OP ⊥ AB) + Center Bisects Chord: Half-Chord AP = sqrt(5² - 3²) = 4.00 cm</div>
        <div class="text-emerald-300 font-bold text-sm" id="c10s7-full">Full Outer Chord AB = 2 x 4.00 = 8.00 cm!</div>
    </div>
</div>

<script>
function setConc107(R, r) {
    const half = Math.sqrt(R*R - r*r);
    const full = 2 * half;
    document.getElementById("c10s7-badge").textContent = `Chord AB = ${full.toFixed(1)} cm`;
    document.getElementById("c10s7-half").textContent = `Outer R=${R}, Inner r=${r}: Half-Chord AP = sqrt(${R}² - ${r}²) = ${half.toFixed(2)} cm`;
    document.getElementById("c10s7-full").textContent = `Full Bisected Chord AB = 2 * ${half.toFixed(2)} = ${full.toFixed(2)} cm!`;
}
setConc107(5, 3);
</script>
"""

# Simulator 8: Example 2 Double Angle Identity (∠PTQ = 2 ∠OPQ)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Example 2 Angle Doubling Lab: ∠PTQ = 2 ∠OPQ</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800" id="c10s8-badge">∠PTQ = 70°, ∠OPQ = 35°</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Set External Tangent Angle θ = ∠PTQ:</span><span class="font-bold text-amber-300" id="c10s8-t-d">θ = 70°</span></div>
        <input type="range" min="20" max="140" step="10" value="70" id="c10s8-t" oninput="calcDbl108()" class="w-full accent-purple-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c10s8-iso">Isosceles △TPQ (TP = TQ): Base ∠TPQ = (180° - 70°) / 2 = 55°</div>
        <div class="text-amber-300" id="c10s8-right">Right Angle ∠OPT = 90°  =>  ∠OPQ = 90° - 55° = 35°</div>
        <div class="text-emerald-300 font-bold text-sm" id="c10s8-res">Exact Identity: ∠PTQ (70°) == 2 x ∠OPQ (35°)!</div>
    </div>
</div>

<script>
function calcDbl108() {
    const theta = parseInt(document.getElementById("c10s8-t").value, 10);
    const tpq = (180 - theta) / 2;
    const opq = 90 - tpq;
    document.getElementById("c10s8-t-d").textContent = "θ = " + theta + "°";
    document.getElementById("c10s8-badge").textContent = `∠PTQ = ${theta}°, ∠OPQ = ${opq}°`;
    document.getElementById("c10s8-iso").textContent = `Isosceles △TPQ (TP = TQ): Base ∠TPQ = (180° - ${theta}°) / 2 = ${tpq}°`;
    document.getElementById("c10s8-right").textContent = `Right Angle ∠OPT = 90°  =>  ∠OPQ = 90° - ${tpq}° = ${opq}°`;
    document.getElementById("c10s8-res").textContent = `Identity Holds! ∠PTQ (${theta}°) = 2 × ∠OPQ (${opq}°)!`;
}
calcDbl108();
</script>
"""
