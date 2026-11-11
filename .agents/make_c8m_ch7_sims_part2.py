#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 7: Proportional Reasoning-1
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Matching Measurement Units & Inverse Speed-Time Trap
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⏱️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Unit Matcher &amp; Inverse Speed-Time Trap (120 km Fixed Trip)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c8c7s9-badge">Speed 60 km/h</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Adjust Vehicle Speed Across Fixed 120 km Highway:</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c7s9-sv">60 km/h</span>
        </div>
        <input type="range" min="20" max="120" step="10" value="60" id="c8c7s9-s" oninput="updC8C7S9()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-emerald-300 font-bold text-sm" id="c8c7s9-time"></div>
        <div class="text-cyan-200 font-bold">Unit Guard: 45 sheets/3 min over 2 hours → convert 2 h = 120 min FIRST → 1,800 sheets!</div>
    </div>
</div>

<script>
function updC8C7S9() {
    const s = parseInt(document.getElementById("c8c7s9-s").value);
    const hrs = (120 / s).toFixed(2).replace(/\\.00$/, "");
    document.getElementById("c8c7s9-sv").textContent = s + " km/h";
    document.getElementById("c8c7s9-badge").textContent = hrs + " Hours";
    document.getElementById("c8c7s9-time").textContent = "INVERSE Variation: Time = 120 ÷ " + s + " = " + hrs + " hrs (Faster Speed = SHORTER Time!)";
}
updC8C7S9();
</script>
"""

# Simulator 10: Orbits Bricks Markets (Unit Price Shampoo Sachet vs Bottle Comparator)
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🛍️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Supermarket Unit-Price Value &amp; Brick Wall Calculator</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c7s10-badge">Sachets Save!</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-2xl border border-slate-800 font-mono text-xs">
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
            <div class="text-rose-300 font-bold">100 mL Bottle = ₹120</div>
            <div class="text-slate-300">Unit Rate = ₹120 ÷ 100 mL = ₹1.20 / mL</div>
        </div>
        <div class="p-3 bg-slate-950 rounded-xl border border-emerald-600/60 space-y-1">
            <div class="text-emerald-300 font-bold">5 mL Sachet = ₹4 (20× = 100 mL for ₹80)</div>
            <div class="text-emerald-200 font-bold">Unit Rate = ₹0.80 / mL (33% Cheaper! ✓)</div>
        </div>
    </div>

    <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 font-mono text-xs text-cyan-200 text-center">
        Wall Length (90 bricks/m): <input type="range" min="4" max="24" step="2" value="18" id="c8c7s10-m" oninput="updC8C7S10()" class="w-28 align-middle accent-cyan-400">
        <span class="font-bold text-amber-300" id="c8c7s10-bricks">18 m → 1,620 Bricks</span>
    </div>
</div>

<script>
function updC8C7S10() {
    const m = parseInt(document.getElementById("c8c7s10-m").value);
    document.getElementById("c8c7s10-bricks").textContent = m + " m wall → " + (90 * m).toLocaleString("en-IN") + " Bricks";
}
updC8C7S10();
</script>
"""

# Simulator 11: Sharing In Ratios (Group-Based Capital Profit Splitter x in m:n)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">💰</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Group Partitioning Profit Splitter: x ÷ (m + n)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c7s11-badge">Ratio 3 : 5</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Share Parts m:</span><span class="font-bold text-cyan-300" id="c8c7s11-mv">3</span></div>
            <input type="range" min="1" max="8" step="1" value="3" id="c8c7s11-m" oninput="updC8C7S11()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Share Parts n:</span><span class="font-bold text-amber-300" id="c8c7s11-nv">5</span></div>
            <input type="range" min="1" max="8" step="1" value="5" id="c8c7s11-n" oninput="updC8C7S11()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-cyan-200" id="c8c7s11-grp"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c8c7s11-sh"></div>
    </div>
</div>

<script>
function updC8C7S11() {
    const m = parseInt(document.getElementById("c8c7s11-m").value);
    const n = parseInt(document.getElementById("c8c7s11-n").value);
    const total = 400000;
    const grp = m + n;
    const unit = total / grp;
    const s1 = Math.round(m * unit), s2 = Math.round(n * unit);
    document.getElementById("c8c7s11-mv").textContent = m;
    document.getElementById("c8c7s11-nv").textContent = n;
    document.getElementById("c8c7s11-badge").textContent = "Ratio " + m + " : " + n;
    document.getElementById("c8c7s11-grp").textContent = "Total Groups = " + m + "+" + n + " = " + grp + "  |  Unit Group = ₹" + Math.round(unit).toLocaleString("en-IN");
    document.getElementById("c8c7s11-sh").textContent = "Share 1 = ₹" + s1.toLocaleString("en-IN") + "   |   Share 2 = ₹" + s2.toLocaleString("en-IN");
}
updC8C7S11();
</script>
"""

# Simulator 12: Mixtures Paints Batters (Mortar, Acid Dilution & Idli Batter)
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🥣</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">Mixture Partition Explorer (Mortar, Acid Lab, Paint, Idli Batter)</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c7s12-badge">Mortar 1:4</span>
    </div>

    <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-2.5 rounded-xl border border-slate-800 text-xs">
        <button onclick="setMixS12(0)" class="px-2.5 py-1 rounded bg-amber-700 text-white font-bold">Mortar (1:4)</button>
        <button onclick="setMixS12(1)" class="px-2.5 py-1 rounded bg-rose-700 text-white font-bold">Acid Dilute (2:3 → 1:2)</button>
        <button onclick="setMixS12(2)" class="px-2.5 py-1 rounded bg-cyan-700 text-white font-bold">Paint (5:2)</button>
        <button onclick="setMixS12(3)" class="px-2.5 py-1 rounded bg-emerald-700 text-white font-bold">Idli Batter (3:1)</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-amber-300 font-bold text-sm" id="c8c7s12-res"></div>
        <div class="text-cyan-200" id="c8c7s12-steps"></div>
    </div>
</div>

<script>
const mixItems = [
    { b: "Mortar 1:4", r: "75 kg Cement-Sand Mortar (1 : 4) → 15 kg Cement + 60 kg Sand", s: "Total groups = 1 + 4 = 5 → Unit = 75 ÷ 5 = 15 kg" },
    { b: "Acid Dilute", r: "600 mL Solution (2:3 = 240 mL Acid : 360 mL Water) → Add 120 mL Water for 1:2!", s: "Keep 240 mL acid steady → Target water = 2 × 240 = 480 mL → +120 mL water" },
    { b: "Paint 5:2", r: "3.5 L Paint (5 White : 2 Blue) → 2.5 L White + 1.0 L Blue", s: "7 groups × 0.5 L/group = 2.5 L White & 1.0 L Blue" },
    { b: "Idli Batter 3:1", r: "12 Cups Batter (3 Rice : 1 Urad Dal) → 9 Cups Rice + 3 Cups Urad", s: "4 groups × 3 cups/group = 9 cups Rice + 3 cups Urad Dal" }
];
function setMixS12(i) {
    document.getElementById("c8c7s12-badge").textContent = mixItems[i].b;
    document.getElementById("c8c7s12-res").textContent = mixItems[i].r;
    document.getElementById("c8c7s12-steps").textContent = mixItems[i].s;
}
setMixS12(0);
</script>
"""

# Simulator 13: Length Area Volume (Reference Conversion Board)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Live Unit Conversion Calculator (Metres, Acres, Hectares, Litres)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c7s13-badge">Value = 5</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Input Quantity k (1 to 20):</span>
            <span class="font-bold text-emerald-300 font-mono" id="c8c7s13-kv">k = 5</span>
        </div>
        <input type="range" min="1" max="20" step="1" value="5" id="c8c7s13-k" oninput="updC8C7S13()" class="w-full accent-emerald-400">
    </div>

    <div class="grid grid-cols-2 gap-2 font-mono text-xs text-center" id="c8c7s13-grid"></div>
</div>

<script>
function updC8C7S13() {
    const k = parseInt(document.getElementById("c8c7s13-k").value);
    document.getElementById("c8c7s13-kv").textContent = "k = " + k;
    document.getElementById("c8c7s13-badge").textContent = "k = " + k;
    document.getElementById("c8c7s13-grid").innerHTML = `
        <div class="p-2 rounded-xl bg-slate-950 border border-cyan-700/60 text-cyan-200 font-bold">${k} m = ${(k * 3.281).toFixed(2)} ft</div>
        <div class="p-2 rounded-xl bg-slate-950 border border-amber-700/60 text-amber-200 font-bold">${k} sq m = ${(k * 10.764).toFixed(2)} sq ft</div>
        <div class="p-2 rounded-xl bg-slate-950 border border-emerald-700/60 text-emerald-200 font-bold">${k} hectare = ${(k * 2.471).toFixed(3)} acres (${(k * 10000).toLocaleString("en-IN")} m²)</div>
        <div class="p-2 rounded-xl bg-slate-950 border border-indigo-700/60 text-indigo-200 font-bold">${k} Litres = ${(k * 1000).toLocaleString("en-IN")} mL = ${(k * 1000).toLocaleString("en-IN")} cc</div>
    `;
}
updC8C7S13();
</script>
"""

# Simulator 14: Temperature Scale Conversion (Live °C <-> °F Thermometer)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌡️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Celsius ⇄ Fahrenheit Dual Thermometer (F = 9C/5 + 32)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c8c7s14-badge">25°C = 77°F</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Slide Temperature in °C (−40°C to 100°C):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c7s14-cv">25°C</span>
        </div>
        <input type="range" min="-40" max="100" step="5" value="25" id="c8c7s14-c" oninput="updC8C7S14()" class="w-full accent-rose-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-amber-300 font-bold text-sm" id="c8c7s14-f"></div>
        <div class="text-cyan-200" id="c8c7s14-note"></div>
    </div>
</div>

<script>
function updC8C7S14() {
    const c = parseInt(document.getElementById("c8c7s14-c").value);
    const f = ((9 / 5) * c + 32).toFixed(1).replace(/\\.0$/, "");
    document.getElementById("c8c7s14-cv").textContent = c + "°C";
    document.getElementById("c8c7s14-badge").textContent = c + "°C = " + f + "°F";
    document.getElementById("c8c7s14-f").textContent = "F = (9/5) × (" + c + ") + 32 = " + f + "°F";
    document.getElementById("c8c7s14-note").textContent = c === 0 ? "Water Freezing Point: 0°C = 32°F (Non-zero offset!)" : (c === 100 ? "Water Boiling Point: 100°C = 212°F!" : (c === -40 ? "Unique Crossover: −40°C = −40°F!" : "Reverse: C = (5/9) × (" + f + " − 32) = " + c + "°C"));
}
updC8C7S14();
</script>
"""

# Simulator 15: Density Saffron Alloys (City Density, Gold 19.3x & Cupro-Nickel)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪙</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Gold Density (19.3× Water), Līlāvatī Saffron &amp; Coin Alloy Lab</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c7s15-badge">Gold = 19.3×</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Solid Block Volume (50 to 500 cc):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c7s15-vv">100 cc</span>
        </div>
        <input type="range" min="50" max="500" step="50" value="100" id="c8c7s15-v" oninput="updC8C7S15()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-amber-300 font-bold" id="c8c7s15-mass"></div>
        <div class="text-emerald-300 font-bold">Cupro-Nickel (75% Copper : 25% Nickel = 3:1) | Mumbai ~21,000/km² &gt; Delhi ~13,333/km²</div>
    </div>
</div>

<script>
function updC8C7S15() {
    const v = parseInt(document.getElementById("c8c7s15-v").value);
    const goldG = Math.round(v * 19.3);
    document.getElementById("c8c7s15-vv").textContent = v + " cc";
    document.getElementById("c8c7s15-mass").textContent = v + " cc Water = " + v + " g   |   Equal Volume Pure Gold (×19.3) = " + goldG.toLocaleString("en-IN") + " g (" + (goldG / 1000).toFixed(2) + " kg!)";
}
updC8C7S15();
</script>
"""

# Simulator 16: Binairo Chapter Summary (Interactive 4×4 Takuzu / Binairo Logic Verifier)
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧩</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Puzzle Time: Valid Solved 4×4 Binairo (Takuzu) Grid Checker</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c7s16-badge">All 3 Rules ✓</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <div class="grid grid-cols-4 gap-1 max-w-[170px] mx-auto font-mono text-sm font-black text-center">
            <div class="p-2 rounded bg-cyan-950 border border-cyan-600 text-cyan-300">—</div>
            <div class="p-2 rounded bg-amber-950 border border-amber-600 text-amber-300">|</div>
            <div class="p-2 rounded bg-amber-950 border border-amber-600 text-amber-300">|</div>
            <div class="p-2 rounded bg-cyan-950 border border-cyan-600 text-cyan-300">—</div>

            <div class="p-2 rounded bg-amber-950 border border-amber-600 text-amber-300">|</div>
            <div class="p-2 rounded bg-cyan-950 border border-cyan-600 text-cyan-300">—</div>
            <div class="p-2 rounded bg-cyan-950 border border-cyan-600 text-cyan-300">—</div>
            <div class="p-2 rounded bg-amber-950 border border-amber-600 text-amber-300">|</div>

            <div class="p-2 rounded bg-cyan-950 border border-cyan-600 text-cyan-300">—</div>
            <div class="p-2 rounded bg-cyan-950 border border-cyan-600 text-cyan-300">—</div>
            <div class="p-2 rounded bg-amber-950 border border-amber-600 text-amber-300">|</div>
            <div class="p-2 rounded bg-amber-950 border border-amber-600 text-amber-300">|</div>

            <div class="p-2 rounded bg-amber-950 border border-amber-600 text-amber-300">|</div>
            <div class="p-2 rounded bg-amber-950 border border-amber-600 text-amber-300">|</div>
            <div class="p-2 rounded bg-cyan-950 border border-cyan-600 text-cyan-300">—</div>
            <div class="p-2 rounded bg-cyan-950 border border-cyan-600 text-cyan-300">—</div>
        </div>
        <div class="font-mono text-xs space-y-1.5">
            <div class="p-2 bg-slate-950 rounded-lg border border-emerald-700/50 text-emerald-300 font-bold">1. Equal Count: Every row &amp; column has two (—) and two (|) ✓</div>
            <div class="p-2 bg-slate-950 rounded-lg border border-emerald-700/50 text-cyan-200 font-bold">2. Max 2 Adjacent: Zero (———) or (|||) triples anywhere ✓</div>
            <div class="p-2 bg-slate-950 rounded-lg border border-emerald-700/50 text-amber-200 font-bold">3. Unique Rows &amp; Cols: All 4 rows &amp; 4 columns distinct ✓</div>
        </div>
    </div>
</div>
"""

if __name__ == "__main__":
    print(f"Prepared {len(simulators_part2)} interactive simulators (Part 2).")
