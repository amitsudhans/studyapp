#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 12: Surface Areas and Volumes
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Real-World Object Decomposer (Section 12.1)
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧊</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Combined Solid Decomposer (Section 12.1)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c12s1-badge">Oil Tanker</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="pickC12S1(0)" id="btn-121-0" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs">Oil Tanker</button>
        <button onclick="pickC12S1(1)" id="btn-121-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Test Tube</button>
        <button onclick="pickC12S1(2)" id="btn-121-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Ice Cream Cone</button>
        <button onclick="pickC12S1(3)" id="btn-121-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Rocket / Pencil</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 220 120" class="w-full max-h-32 bg-slate-950 rounded-xl border border-slate-800" id="c12s1-svg"></svg>
        <div class="font-mono text-xs space-y-1.5" id="c12s1-info"></div>
    </div>
</div>

<script>
function pickC12S1(idx) {
    const names = ["Oil Tanker", "Test Tube", "Ice Cream Cone", "Rocket / Pencil"];
    for (let k = 0; k < 4; k++) {
        document.getElementById("btn-121-" + k).className = k === idx
            ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    document.getElementById("c12s1-badge").textContent = names[idx];
    const svg = document.getElementById("c12s1-svg");
    const info = document.getElementById("c12s1-info");

    if (idx === 0) {
        svg.innerHTML = `
            <path d="M 65 35 A 25 25 0 0 0 65 85" fill="rgba(251,191,36,0.35)" stroke="#fbbf24" stroke-width="2"/>
            <rect x="65" y="35" width="90" height="50" fill="rgba(6,182,212,0.35)" stroke="#22d3ee" stroke-width="2"/>
            <path d="M 155 35 A 25 25 0 0 1 155 85" fill="rgba(251,191,36,0.35)" stroke="#fbbf24" stroke-width="2"/>
            <text x="110" y="63" fill="#fff" font-size="10" text-anchor="middle">Cylinder + 2 Hemispheres</text>`;
        info.innerHTML = `<div class="text-cyan-300 font-bold">Parts: 1 Cylinder + 2 Hemispheres</div>
            <div class="text-emerald-300">TSA = 2πrh + 4πr² (no hidden circles!)</div>
            <div class="text-amber-300">Vol = πr²h + (4/3)πr³</div>`;
    } else if (idx === 1) {
        svg.innerHTML = `
            <rect x="85" y="18" width="50" height="55" fill="rgba(6,182,212,0.35)" stroke="#22d3ee" stroke-width="2"/>
            <path d="M 85 73 A 25 25 0 0 0 135 73" fill="rgba(16,185,129,0.4)" stroke="#34d399" stroke-width="2"/>
            <text x="110" y="50" fill="#fff" font-size="9.5" text-anchor="middle">Open Rim</text>`;
        info.innerHTML = `<div class="text-cyan-300 font-bold">Parts: 1 Cylinder + 1 Bottom Hemisphere</div>
            <div class="text-emerald-300">Outer/Inner CSA = 2πrh + 2πr²</div>
            <div class="text-amber-300">Capacity = πr²h + (2/3)πr³</div>`;
    } else if (idx === 2) {
        svg.innerHTML = `
            <path d="M 80 55 A 30 30 0 0 1 140 55" fill="rgba(244,63,94,0.45)" stroke="#fb7185" stroke-width="2"/>
            <polygon points="80,55 140,55 110,110" fill="rgba(251,191,36,0.35)" stroke="#fbbf24" stroke-width="2"/>`;
        info.innerHTML = `<div class="text-cyan-300 font-bold">Parts: 1 Cone + 1 Hemisphere Scoop</div>
            <div class="text-emerald-300">TSA = πrl + 2πr² = πr(l + 2r)</div>
            <div class="text-amber-300">Vol = ⅓πr²h + (2/3)πr³</div>`;
    } else {
        svg.innerHTML = `
            <polygon points="85,55 135,55 110,15" fill="rgba(244,63,94,0.4)" stroke="#fb7185" stroke-width="2"/>
            <rect x="85" y="55" width="50" height="50" fill="rgba(56,189,248,0.35)" stroke="#38bdf8" stroke-width="2"/>`;
        info.innerHTML = `<div class="text-cyan-300 font-bold">Parts: 1 Cone + 1 Cylinder</div>
            <div class="text-emerald-300">TSA = πrl + 2πrh + πr² (solid base)</div>
            <div class="text-amber-300">Vol = ⅓πr²h_cone + πr²h_cyl</div>`;
    }
}
pickC12S1(0);
</script>
"""

# Simulator 2: Visible Surface Rule (Joined vs Carved Cavity Paint Test)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎨</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Paint Accessibility Rule (Glued vs Carved Faces)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Section 12.2 Golden Rule</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC12S2(0)" id="btn-122-0" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs">Joined Solids (Hidden Faces)</button>
        <button onclick="pickC12S2(1)" id="btn-122-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Carved Cavity (New Pit Wall)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2" id="c12s2-box"></div>
</div>

<script>
function pickC12S2(m) {
    document.getElementById("btn-122-0").className = m === 0
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-122-1").className = m === 1
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const box = document.getElementById("c12s2-box");
    if (m === 0) {
        box.innerHTML = `
            <div class="text-cyan-300 font-bold">Case A: Gluing Cone + Hemisphere (Radius r) Base-to-Base</div>
            <div class="text-rose-300">✗ Hidden Inside Joint: Cone base (πr²) + Hemisphere rim (πr²) DISAPPEAR!</div>
            <div class="text-emerald-300 font-bold">✓ Exposed Exterior Paint: Cone CSA (πrl) + Hemisphere CSA (2πr²)</div>
            <div class="text-amber-300 font-bold">Combined TSA = πrl + 2πr² (NEVER add the hidden πr² circles!)</div>`;
    } else {
        box.innerHTML = `
            <div class="text-cyan-300 font-bold">Case B: Scooping a Hemispherical Pit OUT of a Solid Block Top</div>
            <div class="text-rose-300">✗ Flat Disc Removed: Top circular lid (−πr²) is cut away!</div>
            <div class="text-emerald-300 font-bold">✓ New Cavity Wall Exposed: Curved inner hemisphere bowl (+2πr²) can be painted!</div>
            <div class="text-amber-300 font-bold">Net Surface Change = −πr² + 2πr² = +πr² (TSA actually INCREASES!)</div>`;
    }
}
pickC12S2(0);
</script>
"""

# Simulator 3: Playing Top (Lattu) — Section 12.2 Example 1
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪀</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Playing Top (Lattu) Coloring Solver (Example 1)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">H = 5 cm, d = 3.5 cm</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickC12S3(1)" id="btn-123-1" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs">1. Cone Height</button>
        <button onclick="pickC12S3(2)" id="btn-123-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">2. Slant l ≈ 3.7</button>
        <button onclick="pickC12S3(3)" id="btn-123-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">3. Total 39.6 cm²</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 160 130" class="w-full max-h-32 bg-slate-950 rounded-xl border border-slate-800">
            <path d="M 45 50 A 35 35 0 0 1 115 50" fill="rgba(244,63,94,0.45)" stroke="#fb7185" stroke-width="2"/>
            <polygon points="45,50 115,50 80,115" fill="rgba(16,185,129,0.4)" stroke="#34d399" stroke-width="2"/>
            <line x1="80" y1="50" x2="80" y2="115" stroke="#fde047" stroke-dasharray="3 2" stroke-width="1.5"/>
            <text x="84" y="85" fill="#fde047" font-size="9">h=3.25</text>
            <text x="80" y="42" fill="#fda4af" font-size="9" text-anchor="middle">r=1.75</text>
        </svg>
        <div class="font-mono text-xs space-y-1.5" id="c12s3-info"></div>
    </div>
</div>

<script>
function pickC12S3(st) {
    for (let k = 1; k <= 3; k++) {
        document.getElementById("btn-123-" + k).className = k === st
            ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const info = document.getElementById("c12s3-info");
    if (st === 1) {
        info.innerHTML = `<div class="text-cyan-300 font-bold">Total H = 5 cm, d = 3.5 cm ⇒ r = 1.75 cm</div>
            <div class="text-slate-200">Hemisphere Height = radius r = 1.75 cm</div>
            <div class="text-emerald-300 font-bold">Cone Height h = 5 − 1.75 = 3.25 cm!</div>`;
    } else if (st === 2) {
        info.innerHTML = `<div class="text-amber-300 font-bold">Pythagoras Slant Height l:</div>
            <div class="text-slate-200">l = √(r² + h²) = √(1.75² + 3.25²)</div>
            <div class="text-emerald-300 font-bold">= √(3.0625 + 10.5625) ≈ 3.7 cm!</div>`;
    } else {
        info.innerHTML = `<div class="text-cyan-300 font-bold">TSA = Hemisphere (2πr²) + Cone (πrl)</div>
            <div class="text-slate-200">= πr(2r + l) = (22/7) × (3.5/2) × (3.5 + 3.7)</div>
            <div class="text-emerald-300 font-bold">= 5.5 × 7.2 = 39.6 cm² (approx.)!</div>`;
    }
}
pickC12S3(3);
</script>
"""

# Simulator 4: Decorative Cube Block — Section 12.2 Example 2
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎁</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Decorative Cube + Dome Block (Example 2: 6a² + πr²)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c12s4-badge">163.86 cm²</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Cube Edge a (cm):</span><span class="font-bold text-cyan-300" id="c12s4-av">5 cm</span></div>
            <input type="range" min="4" max="14" step="1" value="5" id="c12s4-a" oninput="updC12S4()" class="w-full accent-cyan-400">
        </div>
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Dome Diameter d (cm):</span><span class="font-bold text-amber-300" id="c12s4-dv">4.2 cm</span></div>
            <input type="range" min="2" max="7" step="0.7" value="4.2" id="c12s4-d" oninput="updC12S4()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-slate-300" id="c12s4-cube"></div>
        <div class="text-amber-300" id="c12s4-net"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c12s4-ans"></div>
    </div>
</div>

<script>
function updC12S4() {
    const a = parseFloat(document.getElementById("c12s4-a").value);
    let d = parseFloat(document.getElementById("c12s4-d").value);
    if (d > a) { d = a; document.getElementById("c12s4-d").value = d; }
    document.getElementById("c12s4-av").textContent = a + " cm";
    document.getElementById("c12s4-dv").textContent = d.toFixed(1) + " cm";

    const r = d / 2;
    const cubeTSA = 6 * a * a;
    const piR2 = (22 / 7) * r * r;
    const total = cubeTSA + piR2;

    document.getElementById("c12s4-badge").textContent = total.toFixed(2) + " cm²";
    document.getElementById("c12s4-cube").textContent = `6 Cube Faces = 6 × ${a}² = ${cubeTSA.toFixed(2)} cm²`;
    document.getElementById("c12s4-net").textContent = `−πr² (covered base) + 2πr² (dome) = +πr² = +${piR2.toFixed(2)} cm²`;
    document.getElementById("c12s4-ans").textContent = `Total TSA (6a² + πr²) = ${total.toFixed(2)} cm²`;
}
updC12S4();
</script>
"""

# Simulator 5: Rocket Model Painting (Overhanging Annular Skirt) — Example 3
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🚀</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Wooden Rocket Painting Solver (Example 3: π = 3.14)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">R=2.5 vs r=1.5 cm</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC12S5(1)" id="btn-125-1" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs">Orange Coat (Cone + Skirt)</button>
        <button onclick="pickC12S5(2)" id="btn-125-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Yellow Coat (Cylinder + Base)</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 150 140" class="w-full max-h-36 bg-slate-950 rounded-xl border border-slate-800" id="c12s5-svg"></svg>
        <div class="font-mono text-xs space-y-1.5" id="c12s5-info"></div>
    </div>
</div>

<script>
function pickC12S5(color) {
    document.getElementById("btn-125-1").className = color === 1
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-125-2").className = color === 2
        ? "p-2 rounded-xl bg-yellow-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const coneFill = color === 1 ? "rgba(249,115,22,0.72)" : "rgba(249,115,22,0.18)";
    const cylFill = color === 2 ? "rgba(250,204,21,0.72)" : "rgba(250,204,21,0.18)";
    document.getElementById("c12s5-svg").innerHTML = `
        <polygon points="40,50 110,50 75,12" fill="${coneFill}" stroke="#fb923c" stroke-width="2"/>
        <rect x="54" y="50" width="42" height="75" fill="${cylFill}" stroke="#fde047" stroke-width="2"/>
        <line x1="40" y1="53" x2="54" y2="53" stroke="#fb923c" stroke-width="3"/>
        <line x1="96" y1="53" x2="110" y2="53" stroke="#fb923c" stroke-width="3"/>
        <text x="75" y="136" fill="#cbd5e1" font-size="8.5" text-anchor="middle">Overhang Skirt π(R² − r²)</text>
    `;

    const info = document.getElementById("c12s5-info");
    if (color === 1) {
        info.innerHTML = `<div class="text-orange-300 font-bold">Cone R = 2.5 cm, h₁ = 6 cm ⇒ l = 6.5 cm</div>
            <div class="text-slate-200">Cone CSA = π R l = 3.14 × 2.5 × 6.5 = 51.025</div>
            <div class="text-amber-300">+ Overhang Ring π(2.5² − 1.5²) = 12.56</div>
            <div class="text-emerald-300 font-bold text-sm">Orange Area = 63.585 cm²!</div>`;
    } else {
        info.innerHTML = `<div class="text-yellow-300 font-bold">Cylinder r = 1.5 cm, h₂ = 26 − 6 = 20 cm</div>
            <div class="text-slate-200">Cylinder CSA = 2 × 3.14 × 1.5 × 20 = 188.40</div>
            <div class="text-amber-300">+ Bottom Circle π r² = 3.14 × 2.25 = 7.065</div>
            <div class="text-emerald-300 font-bold text-sm">Yellow Area = 195.465 cm²!</div>`;
    }
}
pickC12S5(1);
</script>
"""

# Simulator 6: Bird-Bath Cylinder + Hemisphere + m² Converter — Example 4
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🐦</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Bird-Bath Cylinder & Unit Converter (Example 4)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">33,000 cm² = 3.3 m²</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Adjust Cylinder Height h (Example 4 uses 1.45 m = 145 cm, r = 30 cm):</span><span class="font-bold text-cyan-300" id="c12s6-hv">145 cm (1.45 m)</span></div>
        <input type="range" min="105" max="210" step="5" value="145" id="c12s6-h" oninput="updC12S6()" class="w-full accent-emerald-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-cyan-300" id="c12s6-f"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c12s6-cm"></div>
        <div class="text-amber-300 font-bold" id="c12s6-m"></div>
    </div>
</div>

<script>
function updC12S6() {
    const h = parseInt(document.getElementById("c12s6-h").value, 10);
    const r = 30;
    document.getElementById("c12s6-hv").textContent = `${h} cm (${(h/100).toFixed(2)} m)`;
    const cm2 = 2 * (22 / 7) * r * (h + r);
    const m2 = cm2 / 10000;
    document.getElementById("c12s6-f").textContent = `TSA = 2πr(h + r) = 2 × (22/7) × 30 × (${h} + 30) = 2 × (22/7) × 30 × ${h+30}`;
    document.getElementById("c12s6-cm").textContent = `Area in cm² = ${cm2.toFixed(0)} cm²`;
    document.getElementById("c12s6-m").textContent = `Area in m² (÷ 10,000) = ${m2.toFixed(4)} m²` + (h === 145 ? "  [EXACT Ex 4: 3.3 m²!]" : "");
}
updC12S6();
</script>
"""

# Simulator 7: Exercise 12.1 Classic Models (Q1 Twin Cubes, Q6 Capsule, Q7 Tent)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">💊</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Ex 12.1 Solver: Joined Cubes, Capsule & Circus Tent</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">π = 22/7 Mode</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickC12S7(1)" id="btn-127-1" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs">Q1: 2 Cubes (160)</button>
        <button onclick="pickC12S7(6)" id="btn-127-6" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Q6: Capsule (220)</button>
        <button onclick="pickC12S7(7)" id="btn-127-7" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Q7: Tent (₹22k)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2" id="c12s7-box"></div>
</div>

<script>
function pickC12S7(q) {
    for (const k of [1, 6, 7]) {
        document.getElementById("btn-127-" + k).className = k === q
            ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const box = document.getElementById("c12s7-box");
    if (q === 1) {
        box.innerHTML = `<div class="text-purple-300 font-bold">Ex 12.1 Q1: Two Cubes of 64 cm³ Each Joined End-to-End</div>
            <div class="text-slate-200">Cube side a = ∛64 = 4 cm ⇒ Resulting Cuboid: 8 cm × 4 cm × 4 cm</div>
            <div class="text-emerald-300 font-bold text-sm">TSA = 2(8×4 + 4×4 + 4×8) = 2(80) = 160 cm²!</div>`;
    } else if (q === 6) {
        box.innerHTML = `<div class="text-purple-300 font-bold">Ex 12.1 Q6: Medicine Capsule (L = 14 mm, d = 5 mm ⇒ r = 2.5 mm)</div>
            <div class="text-slate-200">Cylinder length h = 14 − 2.5 − 2.5 = 9 mm; TSA = 2πrh + 4πr² = 2πr(h + 2r)</div>
            <div class="text-emerald-300 font-bold text-sm">Exact Surface Area = 2 × (22/7) × 2.5 × 14 = 220 mm²!</div>`;
    } else {
        box.innerHTML = `<div class="text-purple-300 font-bold">Ex 12.1 Q7: Tent (Cyl h=2.1 m, d=4 m + Cone l=2.8 m)</div>
            <div class="text-slate-200">Canvas = 2πrh + πrl = πr(2h + l) = (22/7) × 2 × (4.2 + 2.8) = 44 m²</div>
            <div class="text-emerald-300 font-bold text-sm">Cost at ₹500/m² = 44 × 500 = ₹22,000!</div>`;
    }
}
pickC12S7(6);
</script>
"""

# Simulator 8: Cavity vs Dome Lab (Ex 12.1 Q4, Q5, Q8 & Q9)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🕳️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Ex 12.1 Cavity Solver (Q4 Dome, Q5 Pit, Q8 Cone-Cut, Q9 Twin-Scoop)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">4 Key Board Models</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="pickC12S8(4)" id="btn-128-4" class="p-2 rounded-xl bg-rose-600 text-white font-bold text-xs">Q4 Dome (332.5)</button>
        <button onclick="pickC12S8(5)" id="btn-128-5" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Q5 Pit (l²/4)</button>
        <button onclick="pickC12S8(8)" id="btn-128-8" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Q8 Drill (~18)</button>
        <button onclick="pickC12S8(9)" id="btn-128-9" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Q9 Scoop (374)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2" id="c12s8-box"></div>
</div>

<script>
function pickC12S8(q) {
    for (const k of [4, 5, 8, 9]) {
        document.getElementById("btn-128-" + k).className = k === q
            ? "p-2 rounded-xl bg-rose-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const box = document.getElementById("c12s8-box");
    if (q === 4) {
        box.innerHTML = `<div class="text-rose-300 font-bold">Ex 12.1 Q4: Cube (a = 7 cm) Topped by Hemisphere (d_max = 7 cm ⇒ r = 3.5 cm)</div>
            <div class="text-slate-200">TSA = 6a² + πr² = 294 + (22/7)×3.5×3.5 = 294 + 38.5</div>
            <div class="text-emerald-300 font-bold text-sm">Result = 332.5 cm²!</div>`;
    } else if (q === 5) {
        box.innerHTML = `<div class="text-rose-300 font-bold">Ex 12.1 Q5: Hemisphere Pit (d = l) Carved INSIDE Cube (edge l)</div>
            <div class="text-slate-200">TSA = 6l² − π(l/2)² + 2π(l/2)² = 6l² + πl²/4</div>
            <div class="text-emerald-300 font-bold text-sm">Exact Formula = (l² / 4)(24 + π)  [Identical algebra to a raised dome!]</div>`;
    } else if (q === 8) {
        box.innerHTML = `<div class="text-rose-300 font-bold">Ex 12.1 Q8: Conical Cavity (h=2.4, r=0.7 ⇒ l=2.5 cm) Inside Solid Cylinder</div>
            <div class="text-slate-200">Visible = 2πrh + πr² + πrl = πr(2h + r + l) = 2.2 × (4.8 + 0.7 + 2.5)</div>
            <div class="text-emerald-300 font-bold text-sm">Exact = 17.6 cm² → Nearest cm² = 18 cm²!</div>`;
    } else {
        box.innerHTML = `<div class="text-rose-300 font-bold">Ex 12.1 Q9: Wooden Cylinder (h=10, r=3.5) Scooped With Hemispheres at BOTH Ends</div>
            <div class="text-slate-200">Visible = 2πrh + 4πr² = 2πr(h + 2r) = 2 × (22/7) × 3.5 × (10 + 7)</div>
            <div class="text-emerald-300 font-bold text-sm">Result = 22 × 17 = 374 cm²!</div>`;
    }
}
pickC12S8(8);
</script>
"""
