#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 9: Some Applications of Trigonometry
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Pedestal & Statue (Ex 9.1 Q8: 0.8(√3+1)) + Transmission Tower (Q7: 20(√3-1))
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🗽</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Pedestal & Statue Rationalization Solver (Ex 9.1 Q7 & Q8)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c9s9-badge">Pedestal = 0.8(√3+1) m</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="tab99('statue')" id="btn-99-s" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Q8: 1.6 m Statue -> Pedestal</button>
        <button onclick="tab99('tower')" id="btn-99-t" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Q7: 20 m Building -> Tower</button>
    </div>

    <div id="p99-statue" class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Ex 9.1 Q8: Bottom Pedestal (h) = ?, Top Statue = 1.6 m (45° & 60°)</div>
        <div class="text-cyan-300">45° sets base x = h  |  60° sets (h + 1.6) / h = √3  =>  h(√3 - 1) = 1.6</div>
        <div class="text-emerald-300 font-bold text-sm">Rationalize: h = 1.6(√3 + 1) / (3 - 1) = 0.8(√3 + 1) m!</div>
    </div>

    <div id="p99-tower" class="hidden bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Ex 9.1 Q7: Bottom Building = 20 m, Top Tower = ? (45° & 60°)</div>
        <div class="text-cyan-300">45° sets base x = 20 m  |  60° sets (20 + Tower) = 20√3</div>
        <div class="text-emerald-300 font-bold text-sm">Tower Height = 20√3 - 20 = 20(√3 - 1) m!</div>
    </div>
</div>

<script>
function tab99(t) {
    document.getElementById("p99-statue").classList.toggle("hidden", t !== "statue");
    document.getElementById("p99-tower").classList.toggle("hidden", t !== "tower");
    document.getElementById("btn-99-s").className = (t === "statue")
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-99-t").className = (t === "tower")
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("c9s9-badge").textContent = (t === "statue") ? "Pedestal = 0.8(√3+1) m" : "Tower = 20(√3-1) m";
}
</script>
"""

# Simulator 10: Sun's Altitude Shadow Shift (Example 5: +40 m shift, h = 20√3 m)
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">☀️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Sun Altitude Shadow Shift Lab (Example 5: 60° → 30°, +40 m)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c9s10-badge">Tower h = 20√3 m</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="setSun10(60)" id="btn-910-60" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Sun at 60° (Shadow x)</button>
        <button onclick="setSun10(30)" id="btn-910-30" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Sun Drops to 30° (+40 m!)</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 110" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="c9s10-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold" id="c9s10-info"></div>
    </div>
</div>

<script>
function setSun10(ang) {
    document.getElementById("btn-910-60").className = (ang === 60)
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-910-30").className = (ang === 30)
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";

    const endX = (ang === 60) ? 140 : 300;
    document.getElementById("c9s10-svg").innerHTML = `
        <line x1="30" y1="95" x2="335" y2="95" stroke="#475569" stroke-width="2" />
        <rect x="45" y="25" width="12" height="70" fill="#64748b" stroke="#cbd5e1" />
        <line x1="57" y1="25" x2="${endX}" y2="95" stroke="#fde047" stroke-width="2.5" stroke-dasharray="4,2" />
        <line x1="57" y1="95" x2="140" y2="95" stroke="#38bdf8" stroke-width="4" />
        ${ang === 30 ? '<line x1="140" y1="95" x2="300" y2="95" stroke="#f43f5e" stroke-width="4" />' : ''}
        <text x="98" y="108" fill="#7dd3fc" font-size="9.5" text-anchor="middle">x = 20 m</text>
        ${ang === 30 ? '<text x="220" y="108" fill="#fda4af" font-size="9.5" text-anchor="middle">+40 m Longer Shadow!</text>' : ''}
    `;
    document.getElementById("c9s10-info").textContent = (ang === 60)
        ? "High 60° Sun: x = h / √3 = 20 m (shorter crisp shadow)."
        : "Low 30° Sun: x + 40 = h√3 => h√3 - h/√3 = 40 => 2h = 40√3 => Tower Height h = 20√3 m!";
}
setSun10(30);
</script>
"""

# Simulator 11: Equal Poles Across an 80 m Road (Ex 9.1 Q10)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🛣️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">80 m Road Two Equal Poles Balance (Ex 9.1 Q10)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c9s11-badge">x = 20 m, h = 20√3 m</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Slide Point P along 80 m road (Exact Equal-Height Balance at x = 20 m):</span><span class="font-bold text-amber-300" id="c9s11-x-d">x = 20 m (60° pole) | 60 m (30° pole)</span></div>
        <input type="range" min="10" max="70" step="5" value="20" id="c9s11-x" oninput="checkRoad11()" class="w-full accent-cyan-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c9s11-h1">Left Pole Height (x tan 60°) = 20√3 = 34.64 m</div>
        <div class="text-amber-300" id="c9s11-h2">Right Pole Height ((80-x) tan 30°) = 60/√3 = 34.64 m</div>
        <div class="font-bold text-sm" id="c9s11-ver">EXACT MATCH! Both Poles Equal 20√3 m at x = 20 m and 60 m!</div>
    </div>
</div>

<script>
function checkRoad11() {
    const x = parseInt(document.getElementById("c9s11-x").value, 10);
    const rem = 80 - x;
    const h1 = x * Math.sqrt(3);
    const h2 = rem / Math.sqrt(3);
    document.getElementById("c9s11-x-d").textContent = `x = ${x} m (60° side)  |  ${rem} m (30° side)`;
    document.getElementById("c9s11-h1").textContent = `Left Pole Height  (x tan 60°)     = ${h1.toFixed(2)} m`;
    document.getElementById("c9s11-h2").textContent = `Right Pole Height ((80-x)tan 30°) = ${h2.toFixed(2)} m`;
    const v = document.getElementById("c9s11-ver");
    if (x === 20) {
        v.textContent = "EXACT BALANCE! Both poles stand identical height 20√3 ≈ 34.64 m!";
        v.className = "font-bold text-sm text-emerald-300";
    } else {
        v.textContent = `Heights differ (${h1.toFixed(1)} vs ${h2.toFixed(1)}) — Slide to x = 20 m for equal heights!`;
        v.className = "font-bold text-sm text-rose-400";
    }
}
checkRoad11();
</script>
"""

# Simulator 12: Multi-Storeyed Building Double Depression (Example 6: 4(3+√3))
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏢</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Multi-Storeyed Building Double Depression Proof (Example 6)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">Height = Gap = 4(3+√3) m</span>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 130" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <rect x="30" y="18" width="26" height="92" fill="#475569" stroke="#cbd5e1" />
            <rect x="155" y="65" width="24" height="45" fill="#1e293b" stroke="#38bdf8" />
            <line x1="56" y1="18" x2="155" y2="65" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,2" />
            <line x1="56" y1="18" x2="155" y2="110" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,2" />
            <line x1="56" y1="65" x2="155" y2="65" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2,2" />
            <text x="192" y="90" fill="#7dd3fc" font-size="9">8 m</text>
            <text x="105" y="59" fill="#fcd34d" font-size="9">30°</text>
            <text x="128" y="106" fill="#fda4af" font-size="9">45°</text>
        </svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
            <div class="text-cyan-300">1) Let top diff above 8 m be h, spacing = x.</div>
            <div class="text-amber-300">2) 45°: x = h + 8  |  30°: x = h√3  =>  h = 4(√3+1)</div>
            <div class="text-emerald-300 font-bold text-sm">3) Total = 8 + 4(√3+1) = 4(3 + √3) m for BOTH!</div>
        </div>
    </div>
</div>
"""

# Simulator 13: River Bridge Opposite Banks (Example 7: 3(√3+1)) & Canal TV Tower (Q11)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌉</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">River Bridge Opposite Banks (Ex 7) vs Same-Side Canal Tower (Q11)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c9s13-badge">Bridge = 3(√3+1) m</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="tab913(0)" id="btn-913-0" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Opposite Banks (ADD!)</button>
        <button onclick="tab913(1)" id="btn-913-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Same-Side Canal TV (SUBTRACT!)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="c9s13-l1"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c9s13-l2"></div>
    </div>
</div>

<script>
function tab913(i) {
    document.getElementById("btn-913-0").className = (i === 0)
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-913-1").className = (i === 1)
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";

    if (i === 0) {
        document.getElementById("c9s13-badge").textContent = "River = 3(√3+1) m";
        document.getElementById("c9s13-l1").textContent = "Ex 7 (Bridge 3m high): Left Bank = 3/tan 30° = 3√3 m | Right Bank = 3/tan 45° = 3 m";
        document.getElementById("c9s13-l2").textContent = "Opposite sides ADD: Width = 3√3 + 3 = 3(√3 + 1) meters!";
    } else {
        document.getElementById("c9s13-badge").textContent = "Canal 10m, TV 10√3m";
        document.getElementById("c9s13-l1").textContent = "Q11 (60° on bank -> 30° after 20 m back): x√3 = (x + 20)/√3 => 3x = x + 20";
        document.getElementById("c9s13-l2").textContent = "Canal Width x = 10 m   |   TV Tower Height h = 10√3 m!";
    }
}
tab913(0);
</script>
"""

# Simulator 14: 75 m Lighthouse Two Ships (Ex 9.1 Q13) & 7 m Building Cable Tower (Q12)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🚢</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">75 m Lighthouse Two Ships (Ex 9.1 Q13) & 7 m Building Tower (Q12)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c9s14-badge">Gap = 75(√3-1) m</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="tab914(0)" id="btn-914-0" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">Q13: 75 m Lighthouse & 2 Ships</button>
        <button onclick="tab914(1)" id="btn-914-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Q12: 7 m Building + Cable Tower</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="c9s14-l1"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c9s14-l2"></div>
    </div>
</div>

<script>
function tab914(i) {
    document.getElementById("btn-914-0").className = (i === 0)
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-914-1").className = (i === 1)
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";

    if (i === 0) {
        document.getElementById("c9s14-badge").textContent = "Gap = 75(√3-1) m";
        document.getElementById("c9s14-l1").textContent = "75 m high lighthouse: Ship 1 (45°) at 75 m  |  Ship 2 (30°) at 75√3 m (Same side!)";
        document.getElementById("c9s14-l2").textContent = "Distance Between Ships = 75√3 - 75 = 75(√3 - 1) meters!";
    } else {
        document.getElementById("c9s14-badge").textContent = "Tower = 7(√3+1) m";
        document.getElementById("c9s14-l1").textContent = "7 m building roof: Foot depression 45° -> horizontal gap = 7 m | Top elevation 60° -> rise = 7√3 m";
        document.getElementById("c9s14-l2").textContent = "Total Cable Tower Height = 7 + 7√3 = 7(√3 + 1) meters!";
    }
}
tab914(0);
</script>
"""

# Simulator 15: 88.2 m Drifting Balloon Simulator (Ex 9.1 Q14: 58√3 m)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎈</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Horizontal Balloon Drift Simulator (Ex 9.1 Q14: 88.2 m - 1.2 m = 87 m)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c9s15-badge">Drift = 58√3 m</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Slide Elevation Angle Downward (60° -> 30° at fixed 87 m net altitude):</span><span class="font-bold text-amber-300" id="c9s15-a-d">60° -> 30°</span></div>
        <input type="range" min="30" max="60" step="15" value="30" id="c9s15-a" oninput="drawBal15()" class="w-full accent-rose-400">
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 110" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="c9s15-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold" id="c9s15-info"></div>
    </div>
</div>

<script>
function drawBal15() {
    const ang = parseInt(document.getElementById("c9s15-a").value, 10);
    const netH = 87;
    const xPos = netH / Math.tan(ang * Math.PI / 180);
    const bx = ang === 60 ? 110 : (ang === 45 ? 185 : 295);

    document.getElementById("c9s15-a-d").textContent = `Current Elevation = ${ang}°  (Dist = ${xPos.toFixed(2)} m)`;
    document.getElementById("c9s15-svg").innerHTML = `
        <line x1="25" y1="95" x2="340" y2="95" stroke="#475569" stroke-width="2" />
        <line x1="40" y1="95" x2="40" y2="83" stroke="#38bdf8" stroke-width="3" />
        <line x1="40" y1="83" x2="330" y2="83" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,2" />
        <circle cx="${bx}" cy="24" r="10" fill="#f43f5e" stroke="#fda4af" stroke-width="2" />
        <line x1="40" y1="83" x2="${bx}" y2="24" stroke="#fde047" stroke-width="2" />
        <line x1="${bx}" y1="34" x2="${bx}" y2="83" stroke="#34d399" stroke-width="1.5" stroke-dasharray="3,2" />
        <text x="${bx}" y="12" fill="#fda4af" font-size="9" text-anchor="middle">Balloon (${ang}°)</text>
        <text x="180" y="106" fill="#6ee7b7" font-size="9.5" text-anchor="middle">Total Drift (60° -> 30°) = 87√3 - 29√3 = 58√3 m!</text>
    `;
    document.getElementById("c9s15-info").textContent =
        `Net Height = 88.2 - 1.2 = 87 m! At 60°: 29√3 m | At 30°: 87√3 m | Drift = 87√3 - 29√3 = 58√3 m!`;
}
drawBal15();
</script>
"""

# Simulator 16: Car Approaching Tower (3s) + Section 9.2 Formula Chooser
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🚗</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Approaching Car (Ex 9.1 Q15: 3 s) & Section 9.2 Master Cheat Sheet</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Remaining Time = 3 s!</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-mono">
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-amber-300 font-bold mb-1">1. Sightline & Reference</div>
            <div class="text-slate-300">Horizontal eye line FIRST -> Elev above, Depr below (Z-angles!).</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-cyan-300 font-bold mb-1">2. Ratio Selection</div>
            <div class="text-slate-300">Height + Base -> tan/cot | Ladder/Rope/Kite -> sin/cos.</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-emerald-300 font-bold mb-1">3. Car Speed Proof (Q15)</div>
            <div class="text-slate-300">6 s covers h√3 - h/√3 = 2(h/√3); remaining h/√3 takes 6/2 = 3 s!</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-purple-300 font-bold mb-1">4. Multi-Angle Sign Check</div>
            <div class="text-slate-300">Opposite sides -> ADD | Same side -> SUBTRACT!</div>
        </div>
    </div>
</div>
"""
