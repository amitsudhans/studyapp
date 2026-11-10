#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 9: Some Applications of Trigonometry
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Line of Sight, Horizontal Level, Elevation vs Depression Visualizer
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">👁️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Line of Sight & Horizontal Level Visualizer (Section 9.1)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c9s1-badge">Angle of Elevation</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickView91('elev')" id="btn-91-e" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Looking UP (Elevation)</button>
        <button onclick="pickView91('dep')" id="btn-91-d" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Looking DOWN (Depression)</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 120" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="c9s1-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold" id="c9s1-info"></div>
    </div>
</div>

<script>
function pickView91(mode) {
    document.getElementById("btn-91-e").className = (mode === "elev")
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-91-d").className = (mode === "dep")
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";

    const svg = document.getElementById("c9s1-svg");
    if (mode === "elev") {
        document.getElementById("c9s1-badge").textContent = "Angle of Elevation";
        svg.innerHTML = `
            <line x1="60" y1="88" x2="290" y2="88" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,2" />
            <line x1="60" y1="88" x2="275" y2="25" stroke="#fbbf24" stroke-width="2.5" />
            <circle cx="60" cy="88" r="5" fill="#38bdf8" />
            <circle cx="275" cy="25" r="5" fill="#34d399" />
            <text x="60" y="106" fill="#7dd3fc" font-size="9.5" text-anchor="middle">Observer Eye</text>
            <text x="275" y="18" fill="#6ee7b7" font-size="9.5" text-anchor="middle">Elevated Object (Above)</text>
            <text x="175" y="102" fill="#cbd5e1" font-size="9.5" text-anchor="middle">Horizontal Level</text>
            <text x="155" y="48" fill="#fcd34d" font-size="9.5" font-weight="bold">Line of Sight</text>
            <text x="115" y="80" fill="#facc15" font-size="10" font-weight="bold">θ (Elev)</text>
        `;
        document.getElementById("c9s1-info").textContent = "Object lies ABOVE horizontal eye level -> Tilting gaze UPWARD creates Angle of Elevation!";
    } else {
        document.getElementById("c9s1-badge").textContent = "Angle of Depression";
        svg.innerHTML = `
            <line x1="60" y1="28" x2="290" y2="28" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,2" />
            <line x1="60" y1="28" x2="275" y2="95" stroke="#fbbf24" stroke-width="2.5" />
            <circle cx="60" cy="28" r="5" fill="#38bdf8" />
            <circle cx="275" cy="95" r="5" fill="#f43f5e" />
            <text x="60" y="16" fill="#7dd3fc" font-size="9.5" text-anchor="middle">Observer Eye</text>
            <text x="275" y="112" fill="#fda4af" font-size="9.5" text-anchor="middle">Object BELOW Horizontal</text>
            <text x="195" y="21" fill="#cbd5e1" font-size="9.5" text-anchor="middle">Horizontal Sky Level</text>
            <text x="150" y="75" fill="#fcd34d" font-size="9.5" font-weight="bold">Line of Sight</text>
            <text x="115" y="42" fill="#facc15" font-size="10" font-weight="bold">θ (Depr)</text>
        `;
        document.getElementById("c9s1-info").textContent = "Object lies BELOW horizontal eye level -> Looking DOWNWARD from horizontal level creates Angle of Depression!";
    }
}
pickView91("elev");
</script>
"""

# Simulator 2: Angle of Elevation Tower Calculator (Example 1: 15 m, 60°)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🗼</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Tower Height Calculator: Tangent Elevation Lab (Example 1)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c9s2-badge">h = 15√3 = 25.98 m</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
            <div class="flex justify-between"><span class="text-slate-300">Ground Distance d (m):</span><span class="font-bold text-amber-300" id="c9s2-d-disp">15 m</span></div>
            <input type="range" min="5" max="50" step="5" value="15" id="c9s2-d" oninput="calcTower92()" class="w-full accent-amber-400">
        </div>
        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
            <div class="flex justify-between"><span class="text-slate-300">Elevation Angle θ:</span><span class="font-bold text-cyan-300" id="c9s2-a-disp">60°</span></div>
            <select id="c9s2-a" onchange="calcTower92()" class="w-full bg-slate-950 text-white p-1 rounded border border-slate-700 font-mono mt-1">
                <option value="30">30° (tan = 1/√3)</option>
                <option value="45">45° (tan = 1)</option>
                <option value="60" selected>60° (tan = √3)</option>
            </select>
        </div>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c9s2-eq">tan(60°) = Tower Height h / 15</div>
        <div class="text-emerald-300 font-bold text-sm" id="c9s2-res">h = 15 * √3 = 25.98 m (Example 1!)</div>
    </div>
</div>

<script>
function calcTower92() {
    const d = parseFloat(document.getElementById("c9s2-d").value);
    const a = parseInt(document.getElementById("c9s2-a").value, 10);
    document.getElementById("c9s2-d-disp").textContent = d + " m";
    document.getElementById("c9s2-a-disp").textContent = a + "°";

    let exact = "", num = 0;
    if (a === 30) { exact = `(${d}/√3)`; num = d / Math.sqrt(3); }
    else if (a === 45) { exact = `${d}`; num = d; }
    else { exact = `${d}√3`; num = d * Math.sqrt(3); }

    document.getElementById("c9s2-badge").textContent = `h = ${exact} ≈ ${num.toFixed(2)} m`;
    document.getElementById("c9s2-eq").textContent = `tan(${a}°) = h / ${d}   =>   h = ${d} * tan(${a}°)`;
    document.getElementById("c9s2-res").textContent = `Exact Height h = ${exact} m   (Approx. ${num.toFixed(2)} m)`;
}
calcTower92();
</script>
"""

# Simulator 3: Alternate Interior Angles for Depression
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚡</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Alternate Interior Angles: Moving Depression Into the Ground Triangle</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">Z-Angle Rule</span>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 120" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <line x1="70" y1="25" x2="290" y2="25" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,2" />
            <line x1="40" y1="95" x2="320" y2="95" stroke="#34d399" stroke-width="2" />
            <line x1="70" y1="25" x2="70" y2="95" stroke="#94a3b8" stroke-width="2.5" />
            <line x1="70" y1="25" x2="265" y2="95" stroke="#fbbf24" stroke-width="2.5" />
            <text x="155" y="38" fill="#7dd3fc" font-size="10" font-weight="bold">θ (Depression at Top)</text>
            <text x="200" y="90" fill="#6ee7b7" font-size="10" font-weight="bold">θ (Equal at Ground!)</text>
            <text x="195" y="18" fill="#cbd5e1" font-size="9">Upper Horizontal || Ground</text>
        </svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold">
            Because Top Horizontal || Bottom Ground, Alternate Interior Z-Angles force: Angle of Depression (Top) == Angle of Elevation (Bottom)!
        </div>
    </div>
</div>
"""

# Simulator 4: Observer Eye Height Offset Calculator (Example 3 & Ex 9.1 Q6)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📏</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Observer Height Offset Lab (Example 3 Chimney & Ex 9.1 Q6)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c9s4-badge">Total = 30.0 m</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="setEye94(1.5, 28.5, 45)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 3: Eye 1.5 m, Dist 28.5 m, 45°</button>
        <button onclick="setEye94(1.6, 34.64, 30)" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Eye 1.6 m, Dist 20√3 m, 30°</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300" id="c9s4-net">Vertical Triangle Rise ABOVE eye level = 28.5 * tan(45°) = 28.50 m</div>
        <div class="text-emerald-300 font-bold text-sm" id="c9s4-tot">Add Observer Eye Height (+1.5 m)  =>  Full Height = 28.50 + 1.50 = 30.00 m!</div>
    </div>
</div>

<script>
function setEye94(eye, dist, ang) {
    const rise = dist * Math.tan(ang * Math.PI / 180);
    const total = rise + eye;
    document.getElementById("c9s4-badge").textContent = "Full Height = " + total.toFixed(1) + " m";
    document.getElementById("c9s4-net").textContent = `Rise ABOVE ${eye} m eye line = ${dist} * tan(${ang}°) = ${rise.toFixed(2)} m`;
    document.getElementById("c9s4-tot").textContent = `Full Tower/Chimney Height = ${rise.toFixed(2)} + ${eye} = ${total.toFixed(2)} m!`;
}
setEye94(1.5, 28.5, 45);
</script>
"""

# Simulator 5: Pole & Ladder Hypotenuse Solver (Example 2 & Ex 9.1 Q1)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪜</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Hypotenuse Sine/Cosine Solver (Example 2 Ladder & Ex 9.1 Q1 Rope)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">sin & cot</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="tab95(0)" id="btn-95-0" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Ex 2: 5 m Pole Ladder</button>
        <button onclick="tab95(1)" id="btn-95-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 9.1 Q1: 20 m Circus Rope</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="c9s5-l1"></div>
        <div class="text-cyan-300" id="c9s5-l2"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c9s5-l3"></div>
    </div>
</div>

<script>
function tab95(i) {
    document.getElementById("btn-95-0").className = (i === 0)
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-95-1").className = (i === 1)
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";

    if (i === 0) {
        document.getElementById("c9s5-l1").textContent = "5 m pole reaching 1.3 m below top => Vertical Climb BD = 5 - 1.3 = 3.7 m!";
        document.getElementById("c9s5-l2").textContent = "Ladder Length (Hyp) via sin 60°: 3.7 / (√3/2) = 7.4 / 1.73 = 4.28 m";
        document.getElementById("c9s5-l3").textContent = "Foot Distance (Adj) via cot 60°: 3.7 / √3 = 2.14 m from pole base!";
    } else {
        document.getElementById("c9s5-l1").textContent = "20 m taut circus rope (Hypotenuse) inclined at 30° to flat ground:";
        document.getElementById("c9s5-l2").textContent = "Vertical Pole Height = 20 * sin(30°) = 20 * (1/2)";
        document.getElementById("c9s5-l3").textContent = "Pole Height = EXACTLY 10 meters!";
    }
}
tab95(0);
</script>
"""

# Simulator 6: Broken Storm Tree Visualizer (Ex 9.1 Q2: 8/√3 + 16/√3 = 8√3 m)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌳</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Storm Broken Tree Proof: Vertical Stump + Bent Hypotenuse (Ex 9.1 Q2)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Total = 8√3 m</span>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 130" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <line x1="20" y1="105" x2="200" y2="105" stroke="#475569" stroke-width="2" />
            <line x1="55" y1="105" x2="55" y2="55" stroke="#854d0e" stroke-width="6" />
            <line x1="55" y1="55" x2="175" y2="105" stroke="#22c55e" stroke-width="4" />
            <text x="115" y="120" fill="#7dd3fc" font-size="9.5" text-anchor="middle">Ground Base = 8 m</text>
            <text x="34" y="82" fill="#fcd34d" font-size="9.5" text-anchor="middle">8/√3</text>
            <text x="128" y="72" fill="#6ee7b7" font-size="9.5" font-weight="bold">16/√3 (Bent Top)</text>
            <text x="150" y="100" fill="#fff" font-size="9">30°</text>
        </svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
            <div class="text-amber-300">Piece 1 (Standing): BD = 8 tan 30° = 8/√3 m</div>
            <div class="text-cyan-300">Piece 2 (Hypotenuse): AD = 8 / cos 30° = 16/√3 m</div>
            <div class="text-emerald-300 font-bold text-sm">Full Tree = 8/√3 + 16/√3 = 24/√3 = 8√3 m!</div>
        </div>
    </div>
</div>
"""

# Simulator 7: Park Slides & Kite String Sine Calculator (Ex 9.1 Q3 & Q5)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪁</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Park Slides & Taut Kite String Calculator (Ex 9.1 Q3 & Q5)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c9s7-badge">Slide 1 = 3.0 m</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickSine97(0)" id="btn-97-0" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Child Slide (1.5m, 30°)</button>
        <button onclick="pickSine97(1)" id="btn-97-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Elder Slide (3m, 60°)</button>
        <button onclick="pickSine97(2)" id="btn-97-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Flying Kite (60m, 60°)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="c9s7-l1"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c9s7-l2"></div>
    </div>
</div>

<script>
const sineCases97 = [
    { badge: "Slide 1 = 3.0 m", l1: "Vertical Height = 1.5 m, Angle = 30° -> sin 30° = 1.5 / Length", l2: "Length = 1.5 / (1/2) = 3.00 meters!" },
    { badge: "Slide 2 = 2√3 m", l1: "Vertical Height = 3.0 m, Angle = 60° -> sin 60° = 3.0 / Length", l2: "Length = 3 / (√3/2) = 6/√3 = 2√3 ≈ 3.46 meters!" },
    { badge: "Kite String = 40√3 m", l1: "Kite Height = 60 m, Angle = 60° -> sin 60° = 60 / String", l2: "String = 120 / √3 = 40√3 ≈ 69.28 meters!" }
];
function pickSine97(i) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-97-" + k).className = (k === i)
            ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    }
    document.getElementById("c9s7-badge").textContent = sineCases97[i].badge;
    document.getElementById("c9s7-l1").textContent = sineCases97[i].l1;
    document.getElementById("c9s7-l2").textContent = sineCases97[i].l2;
}
pickSine97(0);
</script>
"""

# Simulator 8: Flagstaff & 10 m Building Two-Elevation Shared Base (Example 4)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏁</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Building & Roof Flagstaff Shared Base Solver (Example 4)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Flagstaff = 7.32 m</span>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 130" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <line x1="25" y1="110" x2="195" y2="110" stroke="#475569" stroke-width="2" />
            <rect x="45" y="65" width="22" height="45" fill="#334155" stroke="#94a3b8" />
            <line x1="56" y1="65" x2="56" y2="25" stroke="#f43f5e" stroke-width="3" />
            <line x1="56" y1="65" x2="175" y2="110" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,2" />
            <line x1="56" y1="25" x2="175" y2="110" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,2" />
            <text x="115" y="124" fill="#7dd3fc" font-size="9.5" text-anchor="middle">Shared Base AP = 10√3 = 17.32 m</text>
            <text x="28" y="90" fill="#cbd5e1" font-size="9">10 m</text>
            <text x="32" y="45" fill="#fda4af" font-size="9" font-weight="bold">7.32m</text>
        </svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
            <div class="text-cyan-300">1) Small △PAB (30°): AP = 10 / tan 30° = 10√3 = 17.32 m</div>
            <div class="text-amber-300">2) Tall △PAD (45°): AD = AP tan 45° = 17.32 m</div>
            <div class="text-emerald-300 font-bold text-sm">3) Flagstaff BD = AD - 10 = 7.32 m!</div>
        </div>
    </div>
</div>
"""
