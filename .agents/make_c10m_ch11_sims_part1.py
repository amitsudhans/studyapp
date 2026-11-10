#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 11: Areas Related to Circles
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Sectors vs Segments (Minor & Major) Explorer
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🍕</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Sectors vs Segments Visual Slicer (Section 11.1)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c11s1-badge">Minor Sector OAPB</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="pickC11S1(0)" id="btn-111-0" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Minor Sector</button>
        <button onclick="pickC11S1(1)" id="btn-111-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Major Sector</button>
        <button onclick="pickC11S1(2)" id="btn-111-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Minor Segment</button>
        <button onclick="pickC11S1(3)" id="btn-111-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Major Segment</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 170" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="c11s1-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold" id="c11s1-info"></div>
    </div>
</div>

<script>
function pickC11S1(mode) {
    for (let k = 0; k < 4; k++) {
        document.getElementById("btn-111-" + k).className = (k === mode)
            ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    }
    const cx = 180, cy = 85, r = 62;
    const a1 = -40 * Math.PI / 180, a2 = 40 * Math.PI / 180;
    const ax = cx + r * Math.cos(a1), ay = cy + r * Math.sin(a1);
    const bx = cx + r * Math.cos(a2), by = cy + r * Math.sin(a2);
    const px = cx + r, py = cy;
    const qx = cx - r, qy = cy;

    let shape = "";
    let boundary = "";
    if (mode === 0) {
        document.getElementById("c11s1-badge").textContent = "Minor Sector OAPB (θ = 80°)";
        shape = `<path d="M ${cx} ${cy} L ${ax} ${ay} A ${r} ${r} 0 0 1 ${bx} ${by} Z" fill="rgba(6,182,212,0.42)" stroke="#22d3ee" stroke-width="2.5"/>`;
        boundary = `<line x1="${cx}" y1="${cy}" x2="${ax}" y2="${ay}" stroke="#fbbf24" stroke-width="2.5"/>
                    <line x1="${cx}" y1="${cy}" x2="${bx}" y2="${by}" stroke="#fbbf24" stroke-width="2.5"/>`;
        document.getElementById("c11s1-info").textContent = "MINOR SECTOR OAPB: Bounded by TWO radii OA & OB + Minor Arc APB (θ < 180°).";
    } else if (mode === 1) {
        document.getElementById("c11s1-badge").textContent = "Major Sector OAQB (280°)";
        shape = `<path d="M ${cx} ${cy} L ${ax} ${ay} A ${r} ${r} 0 1 0 ${bx} ${by} Z" fill="rgba(168,85,247,0.38)" stroke="#c084fc" stroke-width="2.5"/>`;
        boundary = `<line x1="${cx}" y1="${cy}" x2="${ax}" y2="${ay}" stroke="#fbbf24" stroke-width="2.5"/>
                    <line x1="${cx}" y1="${cy}" x2="${bx}" y2="${by}" stroke="#fbbf24" stroke-width="2.5"/>`;
        document.getElementById("c11s1-info").textContent = "MAJOR SECTOR OAQB: Bounded by TWO radii OA & OB + Major Arc AQB (360° − θ = 280°).";
    } else if (mode === 2) {
        document.getElementById("c11s1-badge").textContent = "Minor Segment APB";
        shape = `<path d="M ${ax} ${ay} A ${r} ${r} 0 0 1 ${bx} ${by} Z" fill="rgba(16,185,129,0.45)" stroke="#34d399" stroke-width="2.5"/>`;
        boundary = `<line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#f43f5e" stroke-width="3"/>`;
        document.getElementById("c11s1-info").textContent = "MINOR SEGMENT APB: Bounded by ONE straight CHORD AB + Minor Arc APB (does NOT touch center O!).";
    } else {
        document.getElementById("c11s1-badge").textContent = "Major Segment AQB";
        shape = `<path d="M ${ax} ${ay} A ${r} ${r} 0 1 0 ${bx} ${by} Z" fill="rgba(245,158,11,0.36)" stroke="#fbbf24" stroke-width="2.5"/>`;
        boundary = `<line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#f43f5e" stroke-width="3"/>`;
        document.getElementById("c11s1-info").textContent = "MAJOR SEGMENT AQB: Large region enclosed by Chord AB + Major Arc AQB (contains center O!).";
    }

    document.getElementById("c11s1-svg").innerHTML = `
        <circle cx="${cx}" cy="${cy}" r="${r}" fill="rgba(30,41,59,0.5)" stroke="#475569" stroke-width="1.5" stroke-dasharray="4 3"/>
        ${shape}${boundary}
        <circle cx="${cx}" cy="${cy}" r="3.5" fill="#fff"/>
        <text x="${cx-12}" y="${cy+4}" fill="#e2e8f0" font-size="11" font-weight="bold">O</text>
        <circle cx="${ax}" cy="${ay}" r="3.5" fill="#fde047"/><text x="${ax+6}" y="${ay-2}" fill="#fde047" font-size="11" font-weight="bold">A</text>
        <circle cx="${bx}" cy="${by}" r="3.5" fill="#fde047"/><text x="${bx+6}" y="${by+10}" fill="#fde047" font-size="11" font-weight="bold">B</text>
        <text x="${px+8}" y="${py+4}" fill="#34d399" font-size="10" font-weight="bold">P</text>
        <text x="${qx-14}" y="${qy+4}" fill="#c084fc" font-size="10" font-weight="bold">Q</text>
    `;
}
pickC11S1(0);
</script>
"""

# Simulator 2: Dynamic Sector Area Lab (Unitary Method + Minor/Major Split)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Unitary Sector Area Calculator (θ/360° × πr²)</h3>
        </div>
        <button onclick="togglePiS2()" id="c11s2-pibtn" class="text-[11px] bg-amber-600 text-white font-bold px-3 py-1 rounded-full">π = 3.14</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Central Angle θ:</span><span class="font-bold text-cyan-300" id="c11s2-thv">30°</span></div>
            <input type="range" min="15" max="180" step="15" value="30" id="c11s2-th" oninput="updC11S2()" class="w-full accent-cyan-400">
        </div>
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Radius r (cm):</span><span class="font-bold text-emerald-300" id="c11s2-rv">4 cm</span></div>
            <input type="range" min="2" max="21" step="1" value="4" id="c11s2-r" oninput="updC11S2()" class="w-full accent-emerald-400">
        </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 180 140" class="w-full max-h-36 bg-slate-950 rounded-xl border border-slate-800" id="c11s2-svg"></svg>
        <div class="space-y-2 font-mono text-xs">
            <div class="bg-slate-950 p-2 rounded-lg border border-slate-800 text-slate-300" id="c11s2-unit"></div>
            <div class="bg-cyan-950/60 p-2 rounded-lg border border-cyan-800 text-cyan-200 font-bold" id="c11s2-min"></div>
            <div class="bg-purple-950/60 p-2 rounded-lg border border-purple-800 text-purple-200 font-bold" id="c11s2-maj"></div>
        </div>
    </div>
</div>

<script>
let use22S2 = false;
function togglePiS2() {
    use22S2 = !use22S2;
    document.getElementById("c11s2-pibtn").textContent = use22S2 ? "π = 22/7" : "π = 3.14";
    updC11S2();
}
function updC11S2() {
    const th = parseInt(document.getElementById("c11s2-th").value, 10);
    const r = parseInt(document.getElementById("c11s2-r").value, 10);
    document.getElementById("c11s2-thv").textContent = th + "°";
    document.getElementById("c11s2-rv").textContent = r + " cm";

    const piVal = use22S2 ? (22 / 7) : 3.14;
    const full = piVal * r * r;
    const oneDeg = full / 360;
    const minor = (th / 360) * full;
    const major = full - minor;

    document.getElementById("c11s2-unit").textContent = `1° Area = πr²/360 = ${oneDeg.toFixed(4)} cm² | Full = ${full.toFixed(2)} cm²`;
    document.getElementById("c11s2-min").textContent = `Minor Sector (${th}°): (${th}/360)×π×${r}² = ${minor.toFixed(2)} cm²`;
    document.getElementById("c11s2-maj").textContent = `Major Sector (${360-th}°): ${full.toFixed(2)} − ${minor.toFixed(2)} = ${major.toFixed(2)} cm²`;

    const cx = 90, cy = 70, sr = 48;
    const rad = th * Math.PI / 180;
    const x2 = cx + sr * Math.cos(-rad), y2 = cy + sr * Math.sin(-rad);
    const la = th > 180 ? 1 : 0;
    document.getElementById("c11s2-svg").innerHTML = `
        <circle cx="${cx}" cy="${cy}" r="${sr}" fill="rgba(168,85,247,0.22)" stroke="#a855f7" stroke-width="1.5"/>
        <path d="M ${cx} ${cy} L ${cx+sr} ${cy} A ${sr} ${sr} 0 ${la} 0 ${x2} ${y2} Z" fill="rgba(6,182,212,0.55)" stroke="#22d3ee" stroke-width="2"/>
        <circle cx="${cx}" cy="${cy}" r="3" fill="#fff"/>
        <text x="${cx+10}" y="${cy-8}" fill="#fde047" font-size="10" font-weight="bold">${th}°</text>
    `;
}
updC11S2();
</script>
"""

# Simulator 3: Arc Length, A = 1/2 l r & Perimeter Trap (l + 2r)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📏</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Arc Length, A = ½lr & Perimeter (l + 2r) Lab</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Trap Check: Perimeter = l + 2r!</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Angle θ:</span><span class="font-bold text-cyan-300" id="c11s3-thv">90°</span></div>
            <input type="range" min="30" max="240" step="30" value="90" id="c11s3-th" oninput="updC11S3()" class="w-full accent-cyan-400">
        </div>
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Radius r (cm):</span><span class="font-bold text-amber-300" id="c11s3-rv">7 cm</span></div>
            <input type="range" min="7" max="28" step="7" value="7" id="c11s3-r" oninput="updC11S3()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 font-mono text-xs">
        <div class="bg-slate-950 p-3 rounded-xl border border-cyan-800 text-cyan-200">
            <div class="text-[10px] text-cyan-400 uppercase font-bold">Arc Length l</div>
            <div class="text-sm font-bold mt-1" id="c11s3-arc"></div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-emerald-800 text-emerald-200">
            <div class="text-[10px] text-emerald-400 uppercase font-bold">Area (½ l r)</div>
            <div class="text-sm font-bold mt-1" id="c11s3-area"></div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-rose-800 text-rose-200">
            <div class="text-[10px] text-rose-400 uppercase font-bold">Sector Perimeter</div>
            <div class="text-sm font-bold mt-1" id="c11s3-per"></div>
        </div>
    </div>
</div>

<script>
function updC11S3() {
    const th = parseInt(document.getElementById("c11s3-th").value, 10);
    const r = parseInt(document.getElementById("c11s3-r").value, 10);
    document.getElementById("c11s3-thv").textContent = th + "°";
    document.getElementById("c11s3-rv").textContent = r + " cm";

    const pi = 22 / 7;
    const l = (th / 360) * 2 * pi * r;
    const area = 0.5 * l * r;
    const per = l + 2 * r;

    document.getElementById("c11s3-arc").textContent = `${l.toFixed(2)} cm`;
    document.getElementById("c11s3-area").textContent = `${area.toFixed(2)} cm²`;
    document.getElementById("c11s3-per").textContent = `${per.toFixed(2)} cm (l + 2×${r})`;
}
updC11S3();
</script>
"""

# Simulator 4: Exercise 11.1 Q1 (60° r=6) & Q2 (Quadrant from C=22) Stepper
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🍰</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Ex 11.1 Q1 & Q2 Fraction Exactness Solver</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">π = 22/7 Exact Mode</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC11S4(1)" id="btn-114-1" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Ex 11.1 Q1: θ=60°, r=6 cm</button>
        <button onclick="pickC11S4(2)" id="btn-114-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 11.1 Q2: Quadrant (C=22 cm)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 font-mono text-xs" id="c11s4-box"></div>
</div>

<script>
function pickC11S4(q) {
    document.getElementById("btn-114-1").className = q === 1
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-114-2").className = q === 2
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";

    const box = document.getElementById("c11s4-box");
    if (q === 1) {
        box.innerHTML = `
            <div class="text-amber-300 font-bold">Given: Radius r = 6 cm, Sector Angle θ = 60°, π = 22/7</div>
            <div class="text-slate-300">Step 1: Sector Area = (60° / 360°) × (22 / 7) × 6 × 6</div>
            <div class="text-slate-300">Step 2: Simplify (60/360) = 1/6, cancel 6 cleanly with 6!</div>
            <div class="text-emerald-300 font-bold text-sm">Exact Result = (22 × 6) / 7 = 132 / 7 cm² (≈ 18.86 cm²)</div>
        `;
    } else {
        box.innerHTML = `
            <div class="text-amber-300 font-bold">Given: Circumference C = 22 cm, Quadrant θ = 90° (¼ circle), π = 22/7</div>
            <div class="text-slate-300">Step 1: 2 × (22/7) × r = 22  ⇒  r = (22 × 7) / 44 = 7 / 2 cm (3.5 cm)</div>
            <div class="text-slate-300">Step 2: Quadrant Area = (1/4) × (22/7) × (7/2) × (7/2)</div>
            <div class="text-emerald-300 font-bold text-sm">Exact Result = (11 × 7) / 8 = 77 / 8 cm² (= 9.625 cm²)</div>
        `;
    }
}
pickC11S4(1);
</script>
"""

# Simulator 5: Animated Clock Minute Hand (6°/min) — Ex 11.1 Q3
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🕒</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Clock Minute Hand Sweep Lab (6° / min — Ex 11.1 Q3)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c11s5-badge">5 min = 30°</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Minutes Elapsed (Hand Length r = 14 cm):</span><span class="font-bold text-cyan-300" id="c11s5-mv">5 minutes</span></div>
        <input type="range" min="1" max="45" step="1" value="5" id="c11s5-m" oninput="updC11S5()" class="w-full accent-amber-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 160 150" class="w-full max-h-36 bg-slate-950 rounded-xl border border-slate-800" id="c11s5-svg"></svg>
        <div class="space-y-2 font-mono text-xs">
            <div class="bg-slate-950 p-2 rounded-lg border border-slate-800 text-amber-300 font-bold" id="c11s5-ang"></div>
            <div class="bg-emerald-950/60 p-2 rounded-lg border border-emerald-800 text-emerald-200 font-bold" id="c11s5-area"></div>
            <div class="bg-cyan-950/60 p-2 rounded-lg border border-cyan-800 text-cyan-200" id="c11s5-q3"></div>
        </div>
    </div>
</div>

<script>
function updC11S5() {
    const mins = parseInt(document.getElementById("c11s5-m").value, 10);
    const th = mins * 6;
    document.getElementById("c11s5-mv").textContent = `${mins} min`;
    document.getElementById("c11s5-badge").textContent = `${mins} min = ${th}°`;

    const r = 14;
    const area = (th / 360) * (22 / 7) * r * r;
    document.getElementById("c11s5-ang").textContent = `Angle θ = ${mins} × 6° = ${th}° (${th}/360 of circle)`;
    document.getElementById("c11s5-area").textContent = `Swept Area = (${th}/360)×(22/7)×14² = ${area.toFixed(2)} cm²`;
    document.getElementById("c11s5-q3").textContent = mins === 5 ? "Ex 11.1 Q3 EXACT: 616/12 = 154/3 cm²!" : "Slide to 5 min to verify Ex 11.1 Q3 (154/3 cm²)!";

    const cx = 80, cy = 75, sr = 55;
    const rad = (-90 + th) * Math.PI / 180;
    const x2 = cx + sr * Math.cos(rad), y2 = cy + sr * Math.sin(rad);
    const la = th > 180 ? 1 : 0;
    document.getElementById("c11s5-svg").innerHTML = `
        <circle cx="${cx}" cy="${cy}" r="${sr}" fill="rgba(30,41,59,0.5)" stroke="#94a3b8" stroke-width="2"/>
        <path d="M ${cx} ${cy} L ${cx} ${cy-sr} A ${sr} ${sr} 0 ${la} 1 ${x2} ${y2} Z" fill="rgba(251,191,36,0.45)" stroke="#fbbf24" stroke-width="2"/>
        <line x1="${cx}" y1="${cy}" x2="${cx}" y2="${cy-sr}" stroke="#94a3b8" stroke-dasharray="3 2" stroke-width="1.5"/>
        <line x1="${cx}" y1="${cy}" x2="${x2}" y2="${y2}" stroke="#fde047" stroke-width="3"/>
        <circle cx="${cx}" cy="${cy}" r="3.5" fill="#fff"/>
        <text x="${cx}" y="${cy-sr-4}" fill="#cbd5e1" font-size="9" text-anchor="middle">12</text>
    `;
}
updC11S5();
</script>
"""

# Simulator 6: Circular Segment Subtraction Visualizer (Sector - Triangle) — Ex 11.1 Q4
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✂️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Segment Subtraction Lab: Sector − △OAB (Ex 11.1 Q4)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">90° Right Segment</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickC11S6(0)" id="btn-116-0" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">1. Full Sector (78.5)</button>
        <button onclick="pickC11S6(1)" id="btn-116-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">2. Minus △OAB (−50)</button>
        <button onclick="pickC11S6(2)" id="btn-116-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">3. Segment = 28.5!</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 180 140" class="w-full max-h-36 bg-slate-950 rounded-xl border border-slate-800" id="c11s6-svg"></svg>
        <div class="space-y-2 font-mono text-xs" id="c11s6-info"></div>
    </div>
</div>

<script>
function pickC11S6(step) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-116-" + k).className = k === step
            ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const cx = 55, cy = 115, r = 82;
    const ax = cx + r, ay = cy, bx = cx, by = cy - r;
    let extra = "";
    const info = document.getElementById("c11s6-info");
    if (step === 0) {
        extra = `<path d="M ${cx} ${cy} L ${ax} ${ay} A ${r} ${r} 0 0 0 ${bx} ${by} Z" fill="rgba(6,182,212,0.5)" stroke="#22d3ee" stroke-width="2"/>`;
        info.innerHTML = `<div class="text-cyan-300 font-bold">Given: r = 10 cm, θ = 90°, π = 3.14</div>
            <div class="text-slate-200">Minor Sector = ¼ × 3.14 × 10² = 78.5 cm²</div>
            <div class="text-purple-300">Major Sector = 314 − 78.5 = 235.5 cm²</div>`;
    } else if (step === 1) {
        extra = `<path d="M ${cx} ${cy} L ${ax} ${ay} A ${r} ${r} 0 0 0 ${bx} ${by} Z" fill="rgba(6,182,212,0.3)" stroke="#22d3ee" stroke-width="1.5"/>
                 <polygon points="${cx},${cy} ${ax},${ay} ${bx},${by}" fill="rgba(244,63,94,0.55)" stroke="#fb7185" stroke-width="2"/>`;
        info.innerHTML = `<div class="text-rose-300 font-bold">Subtract Right Triangle △OAB:</div>
            <div class="text-slate-200">∠AOB = 90° ⇒ Base = 10 cm, Height = 10 cm</div>
            <div class="text-rose-200 font-bold">Area(△OAB) = ½ × 10 × 10 = 50 cm²</div>`;
    } else {
        extra = `<polygon points="${cx},${cy} ${ax},${ay} ${bx},${by}" fill="rgba(100,116,139,0.22)" stroke="#64748b" stroke-dasharray="3 3"/>
                 <path d="M ${ax} ${ay} A ${r} ${r} 0 0 0 ${bx} ${by} Z" fill="rgba(16,185,129,0.65)" stroke="#34d399" stroke-width="2.5"/>`;
        info.innerHTML = `<div class="text-emerald-300 font-bold">Minor Segment = Sector − △OAB</div>
            <div class="text-white font-bold text-sm">78.5 − 50 = 28.5 cm²!</div>
            <div class="text-purple-300">Major Segment = 314 − 28.5 = 285.5 cm²</div>`;
    }
    document.getElementById("c11s6-svg").innerHTML = `${extra}
        <circle cx="${cx}" cy="${cy}" r="3" fill="#fff"/>
        <text x="${cx-12}" y="${cy+4}" fill="#fff" font-size="10">O</text>
        <text x="${ax+5}" y="${ay+4}" fill="#fde047" font-size="10">A</text>
        <text x="${bx-12}" y="${by+4}" fill="#fde047" font-size="10">B</text>`;
}
pickC11S6(2);
</script>
"""

# Simulator 7: Equilateral 60° Chord Segment Lab (Ex 11.1 Q5 & Q6)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔺</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">60° Equilateral Chord Segment Lab (Ex 11.1 Q5 & Q6)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">All Angles 60°!</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC11S7(5)" id="btn-117-5" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">Ex 11.1 Q5 (r = 21 cm, π = 22/7)</button>
        <button onclick="pickC11S7(6)" id="btn-117-6" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Ex 11.1 Q6 (r = 15 cm, π = 3.14)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2" id="c11s7-box"></div>
</div>

<script>
function pickC11S7(q) {
    document.getElementById("btn-117-5").className = q === 5
        ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-117-6").className = q === 6
        ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const box = document.getElementById("c11s7-box");
    if (q === 5) {
        box.innerHTML = `
            <div class="text-purple-300 font-bold">Ex 11.1 Q5: r = 21 cm, θ = 60°, π = 22/7</div>
            <div class="text-cyan-300">(i) Arc Length = (60/360) × 2 × (22/7) × 21 = 22 cm</div>
            <div class="text-amber-300">(ii) Sector Area = ½ × l × r = ½ × 22 × 21 = 231 cm²</div>
            <div class="text-emerald-300 font-bold">(iii) Minor Segment = 231 − (√3/4)×21² = (231 − 441√3/4) cm² ≈ 40.05 cm²</div>
        `;
    } else {
        box.innerHTML = `
            <div class="text-purple-300 font-bold">Ex 11.1 Q6: r = 15 cm, θ = 60°, π = 3.14, √3 = 1.73</div>
            <div class="text-cyan-300">Sector = (1/6) × 3.14 × 225 = 117.75 cm² | Equilateral △ = (1.73/4)×225 = 97.3125 cm²</div>
            <div class="text-emerald-300 font-bold">Minor Segment = 117.75 − 97.3125 = 20.4375 cm²</div>
            <div class="text-amber-300 font-bold">Major Segment = 706.5 − 20.4375 = 686.0625 cm²</div>
        `;
    }
}
pickC11S7(5);
</script>
"""

# Simulator 8: 120° Obtuse Angle Altitude Splitting (OM ⊥ AB) — Textbook Ex 3 & Ex 11.1 Q7
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">120° Obtuse Segment Altitude Splitter (OM ⊥ AB)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Ex 11.1 Q7 (r = 12)</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="pickC11S8(0)" id="btn-118-0" class="p-2 rounded-xl bg-rose-600 text-white font-bold text-xs">1. 120° Sector</button>
        <button onclick="pickC11S8(1)" id="btn-118-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">2. Draw OM ⊥ AB</button>
        <button onclick="pickC11S8(2)" id="btn-118-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">3. Trig 60° Split</button>
        <button onclick="pickC11S8(3)" id="btn-118-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">4. Segment 88.44!</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 130" class="w-full max-h-36 bg-slate-950 rounded-xl border border-slate-800" id="c11s8-svg"></svg>
        <div class="font-mono text-xs space-y-1.5" id="c11s8-info"></div>
    </div>
</div>

<script>
function pickC11S8(st) {
    for (let k = 0; k < 4; k++) {
        document.getElementById("btn-118-" + k).className = k === st
            ? "p-2 rounded-xl bg-rose-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const cx = 110, cy = 100, r = 78;
    const ax = cx - r * Math.sin(Math.PI / 3), ay = cy - r * Math.cos(Math.PI / 3);
    const bx = cx + r * Math.sin(Math.PI / 3), by = cy - r * Math.cos(Math.PI / 3);
    const mx = cx, my = ay;

    let extra = `<path d="M ${cx} ${cy} L ${ax} ${ay} A ${r} ${r} 0 0 1 ${bx} ${by} Z" fill="rgba(56,189,248,0.22)" stroke="#38bdf8" stroke-width="2"/>`;
    const info = document.getElementById("c11s8-info");

    if (st === 0) {
        info.innerHTML = `<div class="text-cyan-300 font-bold">r = 12 cm, θ = 120°, π = 3.14</div>
            <div class="text-slate-200">Sector Area = (120/360) × 3.14 × 12²</div>
            <div class="text-emerald-300 font-bold">= 1/3 × 3.14 × 144 = 150.72 cm²</div>`;
    } else if (st === 1) {
        extra += `<line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#fb7185" stroke-width="2.5"/>
                  <line x1="${cx}" y1="${cy}" x2="${mx}" y2="${my}" stroke="#fde047" stroke-width="2" stroke-dasharray="4 2"/>`;
        info.innerHTML = `<div class="text-amber-300 font-bold">Drop Altitude OM ⊥ Chord AB!</div>
            <div class="text-slate-200">Isosceles △OAB splits symmetrically:</div>
            <div class="text-emerald-300 font-bold">∠AOM = ∠BOM = 60° & AM = MB</div>`;
    } else if (st === 2) {
        extra += `<polygon points="${cx},${cy} ${ax},${ay} ${bx},${by}" fill="rgba(244,63,94,0.35)" stroke="#fb7185" stroke-width="2"/>
                  <line x1="${cx}" y1="${cy}" x2="${mx}" y2="${my}" stroke="#fde047" stroke-width="2"/>
                  <text x="${cx+4}" y="${(cy+my)/2}" fill="#fde047" font-size="9">OM=6</text>
                  <text x="${(ax+mx)/2}" y="${my-5}" fill="#fda4af" font-size="9">AM=6√3</text>`;
        info.innerHTML = `<div class="text-rose-300 font-bold">In right △OMA (60°):</div>
            <div class="text-slate-200">OM = 12 cos 60° = 6 cm | AB = 2(12 sin 60°) = 12√3</div>
            <div class="text-rose-200 font-bold">Area(△OAB) = ½×12√3×6 = 36×1.73 = 62.28 cm²</div>`;
    } else {
        extra = `<path d="M ${ax} ${ay} A ${r} ${r} 0 0 1 ${bx} ${by} Z" fill="rgba(16,185,129,0.65)" stroke="#34d399" stroke-width="2.5"/>
                 <polygon points="${cx},${cy} ${ax},${ay} ${bx},${by}" fill="rgba(100,116,139,0.18)" stroke="#64748b" stroke-dasharray="3 3"/>`;
        info.innerHTML = `<div class="text-emerald-300 font-bold">Segment = Sector − △OAB</div>
            <div class="text-white font-bold text-sm">150.72 − 62.28 = 88.44 cm²!</div>
            <div class="text-cyan-300">(Same shortcut: ½ × r² × sin 120° = (√3/4)r²)</div>`;
    }
    document.getElementById("c11s8-svg").innerHTML = `${extra}
        <circle cx="${cx}" cy="${cy}" r="3" fill="#fff"/>
        <text x="${cx}" y="${cy+12}" fill="#fff" font-size="9" text-anchor="middle">O</text>
        <text x="${ax-10}" y="${ay}" fill="#fde047" font-size="9">A</text>
        <text x="${bx+5}" y="${by}" fill="#fde047" font-size="9">B</text>`;
}
pickC11S8(3);
</script>
"""
