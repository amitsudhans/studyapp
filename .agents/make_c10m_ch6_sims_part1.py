#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 6: Triangles
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Congruence vs Similarity + Indirect Mountain/Celestial Measurement
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔺</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Congruence vs Similarity & Scale Factor Explorer (Section 6.1)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c6s1-badge">Similar ONLY (k = 1.6)</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Adjust Scale Factor k (k = 1.0 gives CONGRUENCE!):</span><span class="font-bold text-amber-300" id="c6s1-k-disp">k = 1.60</span></div>
        <input type="range" min="0.6" max="2.0" step="0.1" value="1.6" id="c6s1-k" oninput="updateScale61()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 125" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="c6s1-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold" id="c6s1-info"></div>
    </div>
</div>

<script>
function updateScale61() {
    const k = parseFloat(document.getElementById("c6s1-k").value);
    document.getElementById("c6s1-k-disp").textContent = "k = " + k.toFixed(1);
    const isCong = Math.abs(k - 1.0) < 0.05;
    const badge = document.getElementById("c6s1-badge");
    badge.textContent = isCong ? "CONGRUENT & SIMILAR! (k = 1)" : `SIMILAR ONLY (k = ${k.toFixed(1)})`;
    badge.className = isCong
        ? "text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-700"
        : "text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800";

    // Fixed Triangle 1: base 60, height 45
    const ax = 40, ay = 100, bx = 100, by = 100, cx = 75, cy = 55;
    // Scaled Triangle 2 centered at x=210
    const px = 195, py = 105;
    const qx = px + 60 * k, qy = py;
    const rx = px + 35 * k, ry = py - 45 * k;

    const svg = document.getElementById("c6s1-svg");
    svg.innerHTML = `
        <polygon points="${ax},${ay} ${bx},${by} ${cx},${cy}" fill="rgba(56,189,248,0.22)" stroke="#38bdf8" stroke-width="2" />
        <text x="70" y="116" fill="#7dd3fc" font-size="9.5" text-anchor="middle">Base Triangle (Sides 3, 4, 5)</text>
        <polygon points="${px},${py} ${qx},${qy} ${rx},${ry}" fill="rgba(251,191,36,0.22)" stroke="#fbbf24" stroke-width="2" />
        <text x="${(px+qx)/2}" y="118" fill="#fcd34d" font-size="9.5" text-anchor="middle">Scaled Triangle (${(3*k).toFixed(1)}, ${(4*k).toFixed(1)}, ${(5*k).toFixed(1)})</text>
    `;
    document.getElementById("c6s1-info").textContent = isCong
        ? "k = 1.0: Identical shape AND identical size -> CONGRUENT (and therefore Similar)!"
        : `k = ${k.toFixed(1)}: Angles match identically yet sizes differ -> SIMILAR (Not Congruent)! Indirect measurement relies on this!`;
}
updateScale61();
</script>
"""

# Simulator 2: Always Similar Shapes vs Conditional Shapes
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⭕</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Shape Family Tester: Always Similar vs Depends on Angles (Ex 6.1)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c6s2-badge">ALWAYS SIMILAR!</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="pickShape62(0)" id="btn-s62-0" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">All Circles</button>
        <button onclick="pickShape62(1)" id="btn-s62-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">All Squares</button>
        <button onclick="pickShape62(2)" id="btn-s62-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Equilateral △</button>
        <button onclick="pickShape62(3)" id="btn-s62-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Isosceles △ (Trap!)</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 110" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="c6s2-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono font-bold" id="c6s2-info"></div>
    </div>
</div>

<script>
const shapeData62 = [
    {
        always: true,
        badge: "ALWAYS SIMILAR!",
        info: "All circles have identical round geometry parameterized solely by radius r -> Strictly Similar!",
        svg: `<circle cx="95" cy="55" r="22" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2" />
              <circle cx="245" cy="55" r="42" fill="rgba(16,185,129,0.2)" stroke="#34d399" stroke-width="2" />
              <text x="95" y="96" fill="#7dd3fc" font-size="10" text-anchor="middle">r = 2</text>
              <text x="245" y="106" fill="#6ee7b7" font-size="10" text-anchor="middle">r = 5  (Always Similar!)</text>`
    },
    {
        always: true,
        badge: "ALWAYS SIMILAR!",
        info: "Every square locks 4 angles at 90 degrees and equal side ratios s1/s2 -> Strictly Similar!",
        svg: `<rect x="70" y="38" width="36" height="36" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2" />
              <rect x="215" y="18" width="66" height="66" fill="rgba(16,185,129,0.2)" stroke="#34d399" stroke-width="2" />
              <text x="88" y="94" fill="#7dd3fc" font-size="10" text-anchor="middle">90° Corners</text>
              <text x="248" y="100" fill="#6ee7b7" font-size="10" text-anchor="middle">90° Corners (Ratio s1:s2)</text>`
    },
    {
        always: true,
        badge: "ALWAYS SIMILAR!",
        info: "Equilateral triangles ALWAYS have angles 60°-60°-60° and three equal edges -> Strictly Similar!",
        svg: `<polygon points="90,30 65,75 115,75" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2" />
              <polygon points="245,12 200,90 290,90" fill="rgba(16,185,129,0.2)" stroke="#34d399" stroke-width="2" />
              <text x="90" y="94" fill="#7dd3fc" font-size="10" text-anchor="middle">60°-60°-60°</text>
              <text x="245" y="104" fill="#6ee7b7" font-size="10" text-anchor="middle">60°-60°-60° (Always Similar!)</text>`
    },
    {
        always: false,
        badge: "NOT ALWAYS SIMILAR!",
        info: "TRAP! Skinny isosceles (30°-75°-75°) vs Wide isosceles (120°-30°-30°) have DIFFERENT angles -> NOT Similar!",
        svg: `<polygon points="90,15 72,88 108,88" fill="rgba(251,113,133,0.2)" stroke="#fb7185" stroke-width="2" />
              <polygon points="245,55 180,88 310,88" fill="rgba(251,113,133,0.2)" stroke="#fb7185" stroke-width="2" />
              <text x="90" y="103" fill="#fda4af" font-size="10" text-anchor="middle">Apex 30°</text>
              <text x="245" y="103" fill="#fda4af" font-size="10" text-anchor="middle">Apex 120° (NOT Similar!)</text>`
    }
];

function pickShape62(idx) {
    for (let i = 0; i < 4; i++) {
        const b = document.getElementById("btn-s62-" + i);
        if (b) {
            b.className = (i === idx)
                ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
                : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
        }
    }
    const item = shapeData62[idx];
    document.getElementById("c6s2-svg").innerHTML = item.svg;
    const badge = document.getElementById("c6s2-badge");
    badge.textContent = item.badge;
    badge.className = item.always
        ? "text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-700"
        : "text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-700";
    const info = document.getElementById("c6s2-info");
    info.textContent = item.info;
    info.className = item.always ? "bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono font-bold text-emerald-300" : "bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono font-bold text-rose-400";
}
pickShape62(0);
</script>
"""

# Simulator 3: Polygon Similarity Rules & Ex 6.1 Q3 Counterexamples
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🟪</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Polygon Condition Checker: Equal Angles + Proportional Sides (Ex 6.1 Q3)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c6s3-badge">NOT SIMILAR</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickPoly63(0)" id="btn-p63-0" class="p-2 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">Square vs Rhombus</button>
        <button onclick="pickPoly63(1)" id="btn-p63-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Square vs Rectangle</button>
        <button onclick="pickPoly63(2)" id="btn-p63-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Square vs Bigger Square</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-sans font-bold text-sm" id="c6s3-title"></div>
        <div id="c6s3-c1" class="text-slate-300"></div>
        <div id="c6s3-c2" class="text-slate-300"></div>
        <div id="c6s3-verdict" class="font-bold pt-1"></div>
    </div>
</div>

<script>
const polyPairs63 = [
    {
        title: "Ex 6.1 Q3: Tilted Rhombus (side 1.5 cm, 60°/120°) vs Square (side 3 cm, 90°)",
        c1: "Condition 1 (Equal Angles): FAILS! 60° != 90° and 120° != 90°.",
        c2: "Condition 2 (Proportional Sides): PASSES (1.5 / 3 = 1 : 2 on all 4 edges).",
        verdict: "VERDICT: NOT SIMILAR! Both conditions must pass together.",
        ok: false
    },
    {
        title: "Counterexample 2: Square (4 x 4, 90°) vs Wide Rectangle (4 x 8, 90°)",
        c1: "Condition 1 (Equal Angles): PASSES! All 4 angles equal 90°.",
        c2: "Condition 2 (Proportional Sides): FAILS! 4/4 = 1 != 4/8 = 1/2.",
        verdict: "VERDICT: NOT SIMILAR! Equal angles alone never suffice for polygons!",
        ok: false
    },
    {
        title: "True Similarity: Square A (side 3 cm, 90°) vs Square B (side 6 cm, 90°)",
        c1: "Condition 1 (Equal Angles): PASSES! Every angle equals 90°.",
        c2: "Condition 2 (Proportional Sides): PASSES! Every ratio equals 3/6 = 1/2.",
        verdict: "VERDICT: SIMILAR POLYGONS! Both conditions satisfied cleanly.",
        ok: true
    }
];

function pickPoly63(idx) {
    for (let i = 0; i < 3; i++) {
        const b = document.getElementById("btn-p63-" + i);
        if (b) {
            b.className = (i === idx)
                ? "p-2 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500"
                : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
        }
    }
    const p = polyPairs63[idx];
    document.getElementById("c6s3-title").textContent = p.title;
    document.getElementById("c6s3-c1").textContent = p.c1;
    document.getElementById("c6s3-c2").textContent = p.c2;
    const v = document.getElementById("c6s3-verdict");
    v.textContent = p.verdict;
    v.className = p.ok ? "font-bold pt-1 text-emerald-300" : "font-bold pt-1 text-rose-400";
    const badge = document.getElementById("c6s3-badge");
    badge.textContent = p.ok ? "SIMILAR!" : "NOT SIMILAR";
    badge.className = p.ok
        ? "text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-700"
        : "text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800";
}
pickPoly63(0);
</script>
"""

# Simulator 4: Similar Triangles Vertex Alignment & Equiangular Ratios
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔤</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Vertex Correspondence Inspector: Order Matters! (△ABC ~ △PQR)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800" id="c6s4-badge">AB/PQ = BC/QR = AC/PR</span>
    </div>

    <p class="text-xs text-slate-300">Switch exact vertex ordering to see how corresponding angles and proportional sides lock together!</p>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="setOrder64('PQR')" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">△ABC ~ △PQR</button>
        <button onclick="setOrder64('QRP')" class="p-2 rounded-xl bg-slate-900 text-cyan-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">△ABC ~ △QRP</button>
        <button onclick="setOrder64('RPQ')" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">△ABC ~ △RPQ</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="c6s4-ang">Equal Angles: ∠A = ∠P,  ∠B = ∠Q,  ∠C = ∠R</div>
        <div class="text-cyan-300 font-bold" id="c6s4-side">Proportional Sides: AB / PQ = BC / QR = AC / PR</div>
        <div class="text-slate-400" id="c6s4-note">Equiangular Triangles (Thales): Equal angle alignment automatically fixes constant side ratios!</div>
    </div>
</div>

<script>
function setOrder64(ord) {
    const v1 = ord[0], v2 = ord[1], v3 = ord[2];
    const sideStr = `AB/${v1}${v2} = BC/${v2}${v3} = AC/${v1}${v3}`;
    document.getElementById("c6s4-badge").textContent = sideStr;
    document.getElementById("c6s4-ang").textContent = `Equal Angles: angle A = angle ${v1},  angle B = angle ${v2},  angle C = angle ${v3}`;
    document.getElementById("c6s4-side").textContent = `Proportional Sides: ${sideStr}`;
}
setOrder64("PQR");
</script>
"""

# Simulator 5: Theorem 6.1 (Basic Proportionality Theorem / Thales Theorem) Interactive Proof & Ratio Slider
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Theorem 6.1 Lab (BPT / Thales): Parallel Cut DE ∥ BC</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c6s5-badge">AD/DB = AE/EC = 1.00</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Slide Parallel Line DE up & down (DE always stays ∥ BC):</span><span class="font-bold text-emerald-300" id="c6s5-pos-disp">50% down AB & AC</span></div>
        <input type="range" min="25" max="80" value="50" id="c6s5-pos" oninput="updateBPT65()" class="w-full accent-emerald-400">
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 130" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="c6s5-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono space-y-1">
            <div class="text-cyan-300" id="c6s5-ratio">AD/DB = ar(ADE)/ar(BDE) = 1.00   |   AE/EC = ar(ADE)/ar(CDE) = 1.00</div>
            <div class="text-emerald-300 font-bold" id="c6s5-proof">Same Base DE between DE || BC  =>  ar(BDE) = ar(CDE)  =>  AD/DB = AE/EC ALWAYS!</div>
        </div>
    </div>
</div>

<script>
function updateBPT65() {
    const pct = parseInt(document.getElementById("c6s5-pos").value, 10);
    const t = pct / 100;
    const ratio = (t / (1 - t)).toFixed(2);
    document.getElementById("c6s5-pos-disp").textContent = pct + "% down from Vertex A";
    document.getElementById("c6s5-badge").textContent = "AD/DB = AE/EC = " + ratio;

    // Triangle A(180,15), B(70,115), C(290,115)
    const Ax = 180, Ay = 15, Bx = 70, By = 115, Cx = 290, Cy = 115;
    const Dx = Ax + t * (Bx - Ax), Dy = Ay + t * (By - Ay);
    const Ex = Ax + t * (Cx - Ax), Ey = Ay + t * (Cy - Ay);

    const svg = document.getElementById("c6s5-svg");
    svg.innerHTML = `
        <polygon points="${Ax},${Ay} ${Bx},${By} ${Cx},${Cy}" fill="rgba(16,185,129,0.12)" stroke="#94a3b8" stroke-width="2" />
        <polygon points="${Dx},${Dy} ${Ex},${Ey} ${Bx},${By}" fill="rgba(56,189,248,0.18)" />
        <polygon points="${Dx},${Dy} ${Ex},${Ey} ${Cx},${Cy}" fill="rgba(251,191,36,0.18)" />
        <line x1="${Dx}" y1="${Dy}" x2="${Ex}" y2="${Ey}" stroke="#34d399" stroke-width="2.5" />
        <line x1="${Bx}" y1="${By}" x2="${Ex}" y2="${Ey}" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="3,2" />
        <line x1="${Cx}" y1="${Cy}" x2="${Dx}" y2="${Dy}" stroke="#fbbf24" stroke-width="1.2" stroke-dasharray="3,2" />
        <text x="${Ax}" y="11" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">A</text>
        <text x="${Bx-10}" y="120" fill="#fff" font-size="10" font-weight="bold">B</text>
        <text x="${Cx+6}" y="120" fill="#fff" font-size="10" font-weight="bold">C</text>
        <text x="${Dx-12}" y="${Dy+3}" fill="#34d399" font-size="10" font-weight="bold">D</text>
        <text x="${Ex+6}" y="${Ey+3}" fill="#34d399" font-size="10" font-weight="bold">E</text>
    `;
    document.getElementById("c6s5-ratio").textContent =
        `Upper AD/DB = ${pct}/${100-pct} = ${ratio}   |   Right AE/EC = ${pct}/${100-pct} = ${ratio}`;
}
updateBPT65();
</script>
"""

# Simulator 6: BPT Extensions & Trapezium Diagonals Proof
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">➕</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">BPT Extensions (+1 Corollary) & Trapezium Diagonals (Ex 6.2 Q9)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">AO/BO = CO/DO</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="tab66('cor')" id="btn-66-cor" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Part-to-Whole Corollaries</button>
        <button onclick="tab66('trap')" id="btn-66-trap" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Trapezium Diagonals Proof</button>
    </div>

    <div id="p66-cor" class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Start from BPT (DE || BC):  AD / DB = AE / EC</div>
        <div class="text-cyan-300">1) Add 1 to both sides: (AD + DB)/DB = (AE + EC)/EC  =>  AB / DB = AC / EC</div>
        <div class="text-emerald-300 font-bold">2) Flip & Add 1: DB/AD + 1 = EC/AE + 1  =>  AB / AD = AC / AE  =>  AD / AB = AE / AC</div>
    </div>

    <div id="p66-trap" class="hidden bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Trapezium ABCD (AB || DC), diagonals meet at O. Draw EO || AB || DC:</div>
        <div class="text-cyan-300">1) In triangle ADC (EO || DC): AE / ED = AO / OC</div>
        <div class="text-cyan-300">2) In triangle DAB (EO || AB): AE / ED = BO / OD</div>
        <div class="text-emerald-300 font-bold">3) Equating AE/ED: AO / OC = BO / OD  =>  AO / BO = CO / DO! (Proved!)</div>
    </div>
</div>

<script>
function tab66(t) {
    document.getElementById("p66-cor").classList.toggle("hidden", t !== "cor");
    document.getElementById("p66-trap").classList.toggle("hidden", t !== "trap");
    document.getElementById("btn-66-cor").className = (t === "cor")
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-66-trap").className = (t === "trap")
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
}
</script>
"""

# Simulator 7: Theorem 6.2 Converse of BPT Parallel Line Verifier
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔀</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Theorem 6.2 Verifier (Converse of BPT): Is EF ∥ QR?</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c6s7-badge">NOT Parallel</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="checkConv67(3.9, 3, 3.6, 2.4)" class="p-2 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 6.2 Q2(i): 3.9, 3, 3.6, 2.4</button>
        <button onclick="checkConv67(4, 4.5, 8, 9)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 6.2 Q2(ii): 4, 4.5, 8, 9</button>
        <button onclick="checkConv67(0.18, 1.10, 0.36, 2.20)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 6.2 Q2(iii): 0.18.. ratios</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c6s7-left">Left Ratio PE / EQ = 3.9 / 3 = 1.300</div>
        <div class="text-amber-300" id="c6s7-right">Right Ratio PF / FR = 3.6 / 2.4 = 1.500</div>
        <div class="font-bold text-sm" id="c6s7-verdict">Ratios UNEQUAL (1.300 != 1.500) -> EF is NOT parallel to QR!</div>
    </div>
</div>

<script>
function checkConv67(pe, eq, pf, fr) {
    const r1 = pe / eq;
    const r2 = pf / fr;
    const eqRatio = Math.abs(r1 - r2) < 0.0001;
    document.getElementById("c6s7-left").textContent = `Left Ratio  PE / EQ = ${pe} / ${eq} = ${r1.toFixed(4)}`;
    document.getElementById("c6s7-right").textContent = `Right Ratio PF / FR = ${pf} / ${fr} = ${r2.toFixed(4)}`;
    const badge = document.getElementById("c6s7-badge");
    const v = document.getElementById("c6s7-verdict");
    if (eqRatio) {
        badge.textContent = "EF || QR (PARALLEL!)";
        badge.className = "text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-700";
        v.textContent = `EQUAL RATIOS (${r1.toFixed(4)} == ${r2.toFixed(4)}) -> By Converse of BPT, EF IS parallel to QR!`;
        v.className = "font-bold text-sm text-emerald-300";
    } else {
        badge.textContent = "NOT Parallel";
        badge.className = "text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-700";
        v.textContent = `UNEQUAL RATIOS (${r1.toFixed(4)} != ${r2.toFixed(4)}) -> EF is NOT parallel to QR!`;
        v.className = "font-bold text-sm text-rose-400";
    }
}
checkConv67(3.9, 3, 3.6, 2.4);
</script>
"""

# Simulator 8: Double-Parallel Proofs (Ex 6.2 Q3) & Midpoint Theorem via Converse of BPT
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌉</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Shared Diagonal Bridge Lab (Ex 6.2 Q3 & Midpoint Theorem Q7)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Bridge: AL / AC</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="showProof68(0)" id="btn-68-0" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">Ex 6.2 Q3: AM/AB = AN/AD</button>
        <button onclick="showProof68(1)" id="btn-68-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 6.2 Q7: Midpoint Theorem</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="c6s8-s1"></div>
        <div class="text-cyan-300" id="c6s8-s2"></div>
        <div class="text-emerald-300 font-bold" id="c6s8-s3"></div>
    </div>
</div>

<script>
function showProof68(idx) {
    document.getElementById("btn-68-0").className = (idx === 0)
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-68-1").className = (idx === 1)
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";

    if (idx === 0) {
        document.getElementById("c6s8-s1").textContent = "Step 1 (Upper △ABC, LM || CB): By BPT Corollary, AM / AB = AL / AC";
        document.getElementById("c6s8-s2").textContent = "Step 2 (Lower △ADC, LN || CD): By BPT Corollary, AN / AD = AL / AC";
        document.getElementById("c6s8-s3").textContent = "Step 3 (Bridge AC!): Both equal AL / AC  =>  AM / AB = AN / AD! Proved!";
    } else {
        document.getElementById("c6s8-s1").textContent = "Step 1: D is midpoint of AB  =>  AD = DB  =>  AD / DB = 1";
        document.getElementById("c6s8-s2").textContent = "Step 2: E is midpoint of AC  =>  AE = EC  =>  AE / EC = 1";
        document.getElementById("c6s8-s3").textContent = "Step 3: AD / DB = AE / EC (= 1)  =>  By Converse of BPT, DE || BC! Proved!";
    }
}
showProof68(0);
</script>
"""
