#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 12: Surface Areas and Volumes
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Industrial Shed Volume (Cuboid + Half-Cylinder Roof) — Section 12.3 Example 5
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏭</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Industrial Shed Air Volume Lab (Example 5)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c12s9-badge">Air = 827.15 m³</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Machinery Volume Occupied Inside Shed (Example 5 uses 300 m³):</span><span class="font-bold text-amber-300" id="c12s9-mv">300 m³</span></div>
        <input type="range" min="0" max="500" step="50" value="300" id="c12s9-m" oninput="updC12S9()" class="w-full accent-cyan-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 180 120" class="w-full max-h-32 bg-slate-950 rounded-xl border border-slate-800">
            <path d="M 35 45 A 55 28 0 0 1 145 45 Z" fill="rgba(56,189,248,0.45)" stroke="#38bdf8" stroke-width="2"/>
            <rect x="35" y="45" width="110" height="55" fill="rgba(16,185,129,0.3)" stroke="#34d399" stroke-width="2"/>
            <text x="90" y="34" fill="#bae6fd" font-size="9" text-anchor="middle">½ Cylinder: 288.75 m³</text>
            <text x="90" y="75" fill="#a7f3d0" font-size="9" text-anchor="middle">Cuboid 15×7×8 = 840 m³</text>
        </svg>
        <div class="font-mono text-xs space-y-1.5">
            <div class="text-cyan-300">Total Shed = 840 + 288.75 = 1,128.75 m³</div>
            <div class="text-amber-300" id="c12s9-occ"></div>
            <div class="text-emerald-300 font-bold text-sm" id="c12s9-air"></div>
        </div>
    </div>
</div>

<script>
function updC12S9() {
    const mach = parseInt(document.getElementById("c12s9-m").value, 10);
    const workers = 20 * 0.08;
    const total = 1128.75;
    const air = total - mach - workers;
    document.getElementById("c12s9-mv").textContent = mach + " m³";
    document.getElementById("c12s9-badge").textContent = "Air = " + air.toFixed(2) + " m³";
    document.getElementById("c12s9-occ").textContent = `Minus Machinery (${mach}) + 20 Workers (1.6) = ${(mach + workers).toFixed(1)} m³`;
    document.getElementById("c12s9-air").textContent = `Remaining Air Volume = ${air.toFixed(2)} m³`;
}
updC12S9();
</script>
"""

# Simulator 10: Juice Glass Raised Bottom (Apparent vs Actual Capacity) — Example 6
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🥤</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Juice Glass Raised Bottom Trap (Example 6: π = 3.14)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">d = 5 cm, h = 10 cm</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC12S10(0)" id="btn-1210-0" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs">Apparent Flat Glass (196.25)</button>
        <button onclick="pickC12S10(1)" id="btn-1210-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Raised Bulge Actual (163.54)</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 140 130" class="w-full max-h-32 bg-slate-950 rounded-xl border border-slate-800" id="c12s10-svg"></svg>
        <div class="font-mono text-xs space-y-1.5" id="c12s10-info"></div>
    </div>
</div>

<script>
function pickC12S10(mode) {
    document.getElementById("btn-1210-0").className = mode === 0
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-1210-1").className = mode === 1
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const svg = document.getElementById("c12s10-svg");
    const info = document.getElementById("c12s10-info");
    if (mode === 0) {
        svg.innerHTML = `<rect x="42" y="18" width="56" height="96" fill="rgba(56,189,248,0.45)" stroke="#38bdf8" stroke-width="2.5"/>`;
        info.innerHTML = `<div class="text-cyan-300 font-bold">Apparent Cylinder Capacity:</div>
            <div class="text-slate-200">r = 2.5 cm, h = 10 cm, π = 3.14</div>
            <div class="text-emerald-300 font-bold text-sm">π r² h = 3.14×6.25×10 = 196.25 cm³</div>`;
    } else {
        svg.innerHTML = `<rect x="42" y="18" width="56" height="96" fill="rgba(251,191,36,0.35)" stroke="#38bdf8" stroke-width="2.5"/>
            <path d="M 42 114 A 28 28 0 0 1 98 114 Z" fill="#0f172a" stroke="#fb7185" stroke-width="2"/>
            <text x="70" y="108" fill="#fda4af" font-size="8" text-anchor="middle">−32.71</text>`;
        info.innerHTML = `<div class="text-rose-300 font-bold">Raised Solid Glass Bulge = ⅔π(2.5)³ = 32.71 cm³</div>
            <div class="text-slate-200">Juice cannot enter solid bottom hemisphere!</div>
            <div class="text-emerald-300 font-bold text-sm">Actual = 196.25 − 32.71 = 163.54 cm³!</div>`;
    }
}
pickC12S10(1);
</script>
"""

# Simulator 11: Circumscribed Cylinder 1 : 2 Ratio — Example 7
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚖️</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Circumscribed Cylinder Exact 1 : 2 Ratio (Example 7)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">R = 2 cm, H = 4 cm</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 140 130" class="w-full max-h-32 bg-slate-950 rounded-xl border border-slate-800">
            <rect x="35" y="18" width="70" height="92" fill="rgba(168,85,247,0.16)" stroke="#c084fc" stroke-width="2" stroke-dasharray="4 2"/>
            <polygon points="35,64 105,64 70,18" fill="rgba(56,189,248,0.5)" stroke="#38bdf8" stroke-width="2"/>
            <path d="M 35 64 A 35 35 0 0 0 105 64 Z" fill="rgba(16,185,129,0.5)" stroke="#34d399" stroke-width="2"/>
            <text x="70" y="122" fill="#e9d5ff" font-size="8.5" text-anchor="middle">Cylinder H = 2 + 2 = 4 cm</text>
        </svg>
        <div class="font-mono text-xs space-y-1.5">
            <div class="text-cyan-300">Toy = ⅓π(4)(2) + ⅔π(8) = 8π = 25.12 cm³</div>
            <div class="text-purple-300">Cylinder = π(2²)(4) = 16π = 50.24 cm³</div>
            <div class="text-emerald-300 font-bold text-sm">Difference = 50.24 − 25.12 = 25.12 cm³ (Half!)</div>
        </div>
    </div>
</div>

<script>
// Static interactive breakdown ready
</script>
"""

# Simulator 12: Ex 12.2 Q1 (r=1, h=1 -> π) & Q2 (Engineering Air Model = 66 cm³)
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🛩️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Ex 12.2 Q1 & Q2 Volume Models</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Additive Volumes</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC12S12(1)" id="btn-1212-1" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs">Ex 12.2 Q1: Cone+Hemi (π)</button>
        <button onclick="pickC12S12(2)" id="btn-1212-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Ex 12.2 Q2: Air Model (66)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2" id="c12s12-box"></div>
</div>

<script>
function pickC12S12(q) {
    document.getElementById("btn-1212-1").className = q === 1
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-1212-2").className = q === 2
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const box = document.getElementById("c12s12-box");
    if (q === 1) {
        box.innerHTML = `<div class="text-cyan-300 font-bold">Ex 12.2 Q1: Cone (r=1, h=1) Standing on Hemisphere (r=1)</div>
            <div class="text-slate-200">Total Volume = ⅓π(1²)(1) + ⅔π(1³) = ⅓π + ⅔π</div>
            <div class="text-emerald-300 font-bold text-sm">Exact Result = π cm³!</div>`;
    } else {
        box.innerHTML = `<div class="text-cyan-300 font-bold">Ex 12.2 Q2: Cylinder (h=12−2−2=8 cm, d=3 ⇒ r=1.5) + Two 2 cm Cones</div>
            <div class="text-slate-200">Air Volume = πr²h_cyl + 2×(⅓πr²h_cone) = πr²(8 + 4/3) = (22/7)×(9/4)×(28/3)</div>
            <div class="text-emerald-300 font-bold text-sm">Exact Result = 22 × 3 = 66 cm³!</div>`;
    }
}
pickC12S12(2);
</script>
"""

# Simulator 13: 45 Gulab Jamuns 30% Sugar Syrup — Ex 12.2 Q3
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🍯</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Gulab Jamun 30% Sugar Syrup Lab (Ex 12.2 Q3)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c12s13-badge">45 Jamuns → 338 cm³</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Number of Gulab Jamuns in Jar (Ex 12.2 Q3 uses 45):</span><span class="font-bold text-amber-300" id="c12s13-nv">45 Jamuns</span></div>
        <input type="range" min="5" max="60" step="5" value="45" id="c12s13-n" oninput="updC12S13()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-cyan-300">1 Jamun: r = 1.4 cm, h_cyl = 5 − 2.8 = 2.2 cm ⇒ V₁ = (22/7)×1.4²×(2.2 + 5.6/3) ≈ 25.0507 cm³</div>
        <div class="text-slate-200" id="c12s13-tot"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c12s13-syr"></div>
    </div>
</div>

<script>
function updC12S13() {
    const n = parseInt(document.getElementById("c12s13-n").value, 10);
    const v1 = (22 / 7) * 1.4 * 1.4 * (2.2 + (4 / 3) * 1.4);
    const tot = n * v1;
    const syr = 0.30 * tot;
    document.getElementById("c12s13-nv").textContent = n + " Jamuns";
    document.getElementById("c12s13-badge").textContent = `${n} Jamuns → ${Math.round(syr)} cm³`;
    document.getElementById("c12s13-tot").textContent = `${n} Jamuns Total Volume = ${tot.toFixed(2)} cm³`;
    document.getElementById("c12s13-syr").textContent = `30% Sugar Syrup = 0.30 × ${tot.toFixed(2)} = ${syr.toFixed(2)} cm³` + (n === 45 ? " (≈ 338 cm³ NCERT!)" : "");
}
updC12S13();
</script>
"""

# Simulator 14: Pen Stand Cavities (Q4) & Iron Pole Mass (Q6)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪵</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Pen Stand Wood (Ex 12.2 Q4) & Iron Pole Mass (Q6)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Subtract vs Stack</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC12S14(4)" id="btn-1214-4" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs">Q4: Wood Pen Stand (523.53)</button>
        <button onclick="pickC12S14(6)" id="btn-1214-6" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Q6: Iron Pole (892.26 kg)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2" id="c12s14-box"></div>
</div>

<script>
function pickC12S14(q) {
    document.getElementById("btn-1214-4").className = q === 4
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-1214-6").className = q === 6
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const box = document.getElementById("c12s14-box");
    if (q === 4) {
        box.innerHTML = `<div class="text-emerald-300 font-bold">Ex 12.2 Q4: 15×10×3.5 Cuboid − 4 Conical Depressions (r=0.5, h=1.4)</div>
            <div class="text-slate-200">Cuboid = 525 cm³ | 4 Cones = 4 × ⅓ × (22/7) × 0.25 × 1.4 = 4.4 / 3 ≈ 1.47 cm³</div>
            <div class="text-amber-300 font-bold text-sm">Remaining Wood = 525 − 1.47 = 523.53 cm³!</div>`;
    } else {
        box.innerHTML = `<div class="text-emerald-300 font-bold">Ex 12.2 Q6: Twin Cylinder Iron Pole (π = 3.14, Density = 8 g/cm³)</div>
            <div class="text-slate-200">Volume = 3.14 × (12² × 220 + 8² × 60) = 3.14 × 35,520 = 111,532.8 cm³</div>
            <div class="text-amber-300 font-bold text-sm">Mass = 111,532.8 × 8 g = 892,262.4 g = 892.26 kg!</div>`;
    }
}
pickC12S14(4);
</script>
"""

# Simulator 15: Lead Shot Water Displacement — Ex 12.2 Q5, Q7 & Q8
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">💧</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Water Overflow Displacement Lab (Ex 12.2 Q5: N = 100)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c12s15-badge">100 Shots = ¼ Overflow!</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Drop Spherical Lead Shots (r = 0.5 cm) into Full Cone (h=8, r=5):</span><span class="font-bold text-rose-300" id="c12s15-nv">100 shots</span></div>
        <input type="range" min="10" max="120" step="10" value="100" id="c12s15-n" oninput="updC12S15()" class="w-full accent-rose-500">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-cyan-300">Target ¼ Cone Overflow = ¼ × ⅓π(5²)(8) = (50/3)π ≈ 16.67π cm³</div>
        <div class="text-amber-300" id="c12s15-cur"></div>
        <div class="text-emerald-300 font-bold" id="c12s15-stat"></div>
    </div>
</div>

<script>
function updC12S15() {
    const n = parseInt(document.getElementById("c12s15-n").value, 10);
    const displacedPi = n / 6;
    const pct = (displacedPi / (200 / 3)) * 100;
    document.getElementById("c12s15-nv").textContent = n + " shots";
    document.getElementById("c12s15-badge").textContent = pct.toFixed(1) + "% Overflow";
    document.getElementById("c12s15-cur").textContent = `N × (4/3)π(0.5)³ = ${n}/6 π = ${displacedPi.toFixed(2)}π cm³ displaced (${pct.toFixed(1)}% of cone)`;
    document.getElementById("c12s15-stat").textContent = n === 100
        ? "EXACT 25% (¼) OVERFLOW ACHIEVED AT N = 100 LEAD SHOTS!"
        : "Slide to N = 100 to match exact 25% (¼) NCERT Ex 12.2 Q5 overflow!";
}
updC12S15();
</script>
"""

# Simulator 16: Section 12.4 Master All-Solid Interactive Calculator
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏆</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Section 12.4 Master Combined Solid Solver (π = 22/7)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Live TSA & Volume</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="setShapeS16(0)" id="btn-1216-0" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs">Cone + Hemisphere</button>
        <button onclick="setShapeS16(1)" id="btn-1216-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Cyl + 2 Hemispheres</button>
        <button onclick="setShapeS16(2)" id="btn-1216-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Cone + Cylinder</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Common Radius r (cm):</span><span class="font-bold text-cyan-300" id="c12s16-rv">7 cm</span></div>
            <input type="range" min="3" max="14" step="1" value="7" id="c12s16-r" oninput="updC12S16()" class="w-full accent-cyan-400">
        </div>
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Height h (cm):</span><span class="font-bold text-emerald-300" id="c12s16-hv">10 cm</span></div>
            <input type="range" min="4" max="24" step="1" value="10" id="c12s16-h" oninput="updC12S16()" class="w-full accent-emerald-400">
        </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 font-mono text-xs">
        <div class="bg-slate-950 p-3 rounded-xl border border-cyan-800 text-cyan-200 font-bold" id="c12s16-tsa"></div>
        <div class="bg-slate-950 p-3 rounded-xl border border-emerald-800 text-emerald-200 font-bold" id="c12s16-vol"></div>
    </div>
</div>

<script>
let shapeS16 = 0;
function setShapeS16(s) {
    shapeS16 = s;
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-1216-" + k).className = k === s
            ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    updC12S16();
}
function updC12S16() {
    const r = parseInt(document.getElementById("c12s16-r").value, 10);
    const h = parseInt(document.getElementById("c12s16-h").value, 10);
    document.getElementById("c12s16-rv").textContent = r + " cm";
    document.getElementById("c12s16-hv").textContent = h + " cm";
    const pi = 22 / 7;
    const l = Math.sqrt(r * r + h * h);

    let tsa = 0, vol = 0, tf = "", vf = "";
    if (shapeS16 === 0) {
        tsa = pi * r * (l + 2 * r);
        vol = (1 / 3) * pi * r * r * h + (2 / 3) * pi * r * r * r;
        tf = "πr(l + 2r)"; vf = "⅓πr²h + ⅔πr³";
    } else if (shapeS16 === 1) {
        tsa = 2 * pi * r * (h + 2 * r);
        vol = pi * r * r * h + (4 / 3) * pi * r * r * r;
        tf = "2πr(h + 2r)"; vf = "πr²h + 4/3 πr³";
    } else {
        tsa = pi * r * (l + 2 * h + r);
        vol = pi * r * r * h * (4 / 3);
        tf = "πrl + 2πrh + πr²"; vf = "πr²h + ⅓πr²h";
    }
    document.getElementById("c12s16-tsa").textContent = `Exposed TSA [${tf}] = ${tsa.toFixed(2)} cm²`;
    document.getElementById("c12s16-vol").textContent = `Total Volume [${vf}] = ${vol.toFixed(2)} cm³`;
}
updC12S16();
</script>
"""
