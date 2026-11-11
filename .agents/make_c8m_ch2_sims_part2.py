#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 2: Power Play
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Power Lines Scale (Logarithmic Base 4 / Base 7 Tick Line Explorer)
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📏</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Power Lines Explorer (Section 2.3: Base 4 &amp; Base 7 Lines)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c2s9-badge">Base 4 Line</span>
    </div>

    <div class="flex flex-wrap items-center justify-between gap-2 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div class="flex gap-2">
            <button onclick="setBaseS9(4)" id="c8c2s9-b4" class="px-3 py-1 rounded-lg bg-cyan-600 text-white font-bold">Base 4 Line</button>
            <button onclick="setBaseS9(7)" id="c8c2s9-b7" class="px-3 py-1 rounded-lg bg-slate-800 text-slate-300 font-bold border border-slate-700">Base 7 Line</button>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-slate-300">Step Exp (k):</span>
            <input type="range" min="-3" max="3" step="1" value="1" id="c8c2s9-k" oninput="updC8C2S9()" class="w-28 accent-amber-400">
            <span class="font-bold text-amber-300 font-mono" id="c8c2s9-kv">k = 1</span>
        </div>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2">
        <svg viewBox="0 0 360 88" class="w-full h-24 bg-slate-950 rounded-xl border border-slate-800" id="c8c2s9-svg"></svg>
        <div class="font-mono text-xs bg-slate-950 p-2 rounded-lg border border-slate-800 text-emerald-300 font-bold text-center" id="c8c2s9-info"></div>
    </div>
</div>

<script>
let baseS9 = 4;
function setBaseS9(b) {
    baseS9 = b;
    document.getElementById("c8c2s9-b4").className = b === 4 ? "px-3 py-1 rounded-lg bg-cyan-600 text-white font-bold" : "px-3 py-1 rounded-lg bg-slate-800 text-slate-300 font-bold border border-slate-700";
    document.getElementById("c8c2s9-b7").className = b === 7 ? "px-3 py-1 rounded-lg bg-cyan-600 text-white font-bold" : "px-3 py-1 rounded-lg bg-slate-800 text-slate-300 font-bold border border-slate-700";
    document.getElementById("c8c2s9-badge").textContent = "Base " + b + " Line";
    updC8C2S9();
}
function updC8C2S9() {
    const k = parseInt(document.getElementById("c8c2s9-k").value);
    document.getElementById("c8c2s9-kv").textContent = "k = " + k;

    let ticks = `<line x1="25" y1="45" x2="335" y2="45" stroke="#475569" stroke-width="2"/>`;
    for (let e = -3; e <= 3; e++) {
        const x = 180 + e * 46;
        const active = e === k;
        const lbl = baseS9 + "^" + e;
        const val = e >= 0 ? Math.pow(baseS9, e) : "1/" + Math.pow(baseS9, -e);
        ticks += `<circle cx="${x}" cy="45" r="${active ? 7 : 4.5}" fill="${active ? "#f59e0b" : "#38bdf8"}"/>`;
        ticks += `<text x="${x}" y="26" text-anchor="middle" fill="${active ? "#fde68a" : "#94a3b8"}" font-size="9" font-weight="bold">${lbl}</text>`;
        ticks += `<text x="${x}" y="68" text-anchor="middle" fill="${active ? "#34d399" : "#64748b"}" font-size="8">${val}</text>`;
    }
    document.getElementById("c8c2s9-svg").innerHTML = ticks;

    const valTxt = k >= 0 ? Math.pow(baseS9, k).toLocaleString("en-IN") : "1/" + Math.pow(baseS9, -k).toLocaleString("en-IN");
    document.getElementById("c8c2s9-info").textContent = "Selected Marker: " + baseS9 + "^(" + k + ") = " + valTxt + "   |   Step Right = ×" + baseS9 + ",   Step Left = ÷" + baseS9;
}
updC8C2S9();
</script>
"""

# Simulator 10: Decimal Place Powers (Interactive 561.903 Digit Expander)
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔟</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Decimal Expanded Form Lab (Section 2.4: Powers of 10)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c2s10-badge">561.903</span>
    </div>

    <div class="flex flex-wrap items-center gap-2 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <span class="text-slate-300 font-bold">Preset:</span>
        <button onclick="setDecS10('561.903')" class="px-2.5 py-1 rounded-lg bg-amber-600 text-white font-bold">561.903 (NCERT)</button>
        <button onclick="setDecS10('407.209')" class="px-2.5 py-1 rounded-lg bg-slate-800 text-cyan-300 font-bold border border-slate-700">407.209</button>
        <button onclick="setDecS10('892.045')" class="px-2.5 py-1 rounded-lg bg-slate-800 text-emerald-300 font-bold border border-slate-700">892.045</button>
    </div>

    <div class="grid grid-cols-6 gap-1.5 font-mono text-xs text-center" id="c8c2s10-grid"></div>
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs text-emerald-300 font-bold text-center" id="c8c2s10-sum"></div>
</div>

<script>
function setDecS10(val) {
    const parts = val.split(".");
    const intP = parts[0].padStart(3, "0");
    const decP = (parts[1] || "000").padEnd(3, "0");
    const digits = [intP[0], intP[1], intP[2], decP[0], decP[1], decP[2]];
    const exps = [2, 1, 0, -1, -2, -3];
    const names = ["100s", "10s", "1s", "1/10", "1/100", "1/1000"];

    let gridHtml = "";
    let terms = [];
    for (let i = 0; i < 6; i++) {
        const d = digits[i];
        const e = exps[i];
        gridHtml += `<div class="p-2 rounded-xl bg-slate-900 border ${e >= 0 ? "border-cyan-800" : "border-rose-800"}">
            <div class="text-base font-black ${d === "0" ? "text-slate-500" : "text-amber-300"}">${d}</div>
            <div class="text-[10px] font-bold text-cyan-300">× 10^${e}</div>
            <div class="text-[9px] text-slate-400">${names[i]}</div>
        </div>`;
        terms.push(d + "×10^" + e);
    }
    document.getElementById("c8c2s10-badge").textContent = val;
    document.getElementById("c8c2s10-grid").innerHTML = gridHtml;
    document.getElementById("c8c2s10-sum").textContent = val + " = " + terms.join(" + ");
}
setDecS10("561.903");
</script>
"""

# Simulator 11: Scientific Notation Form (x * 10^y converter with 1 <= x < 10)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔭</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Scientific Notation Converter (1 ≤ x &lt; 10)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c2s11-badge">Standard Form</span>
    </div>

    <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <button onclick="setSciS11(0)" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-bold">Earth Mass</button>
        <button onclick="setSciS11(1)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-cyan-300 font-bold border border-slate-700">Sun–Earth Dist</button>
        <button onclick="setSciS11(2)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-rose-300 font-bold border border-slate-700">Virus Size</button>
        <button onclick="setSciS11(3)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-amber-300 font-bold border border-slate-700">Fix 45 × 10⁸</button>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2 font-mono text-xs">
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-slate-300" id="c8c2s11-raw"></div>
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold text-sm" id="c8c2s11-std"></div>
        <div class="p-2 bg-cyan-950/30 rounded-lg border border-cyan-700/50 text-cyan-200 font-bold" id="c8c2s11-rule"></div>
    </div>
</div>

<script>
const sciItems = [
    { name: "Earth Mass (kg)", raw: "5,970,000,000,000,000,000,000,000 kg", std: "5.97 × 10²⁴ kg", rule: "Decimal moved 24 places LEFT → positive exponent +24 (1 ≤ 5.97 < 10)" },
    { name: "Earth–Sun Distance (m)", raw: "149,600,000,000 m", std: "1.496 × 10¹¹ m", rule: "Decimal moved 11 places LEFT → positive exponent +11 (1 ≤ 1.496 < 10)" },
    { name: "Microscopic Virus Width (m)", raw: "0.000000085 m", std: "8.5 × 10⁻⁸ m", rule: "Decimal moved 8 places RIGHT → negative exponent −8 (1 ≤ 8.5 < 10)" },
    { name: "Normalize 45 × 10⁸", raw: "45 × 10⁸ (NOT Standard Form because 45 ≥ 10!)", std: "4.5 × 10⁹", rule: "Rewrite 45 as (4.5 × 10¹), then apply Law 1: 4.5 × 10^(1+8) = 4.5 × 10⁹" }
];
function setSciS11(idx) {
    const it = sciItems[idx];
    document.getElementById("c8c2s11-badge").textContent = it.name;
    document.getElementById("c8c2s11-raw").textContent = "Original: " + it.raw;
    document.getElementById("c8c2s11-std").textContent = "Strict Standard Form: " + it.std;
    document.getElementById("c8c2s11-rule").textContent = it.rule;
}
setSciS11(0);
</script>
"""

# Simulator 12: Linear vs Exponential (Moon Ladder 1.92B steps vs 46 Paper Folds)
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🚀</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">Earth-to-Moon Race: Linear Ladder vs Paper Doubling</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c2s12-badge">Step n = 15</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Compare Day / Step Count (n):</span>
            <span class="font-bold text-cyan-300 font-mono" id="c8c2s12-nv">n = 15</span>
        </div>
        <input type="range" min="1" max="20" step="1" value="15" id="c8c2s12-n" oninput="updC8C2S12()" class="w-full accent-indigo-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-2xl border border-slate-800 font-mono text-xs">
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
            <div class="text-slate-400 font-bold">Linear (+₹100/day or +20 cm/step)</div>
            <div class="text-cyan-300 font-bold" id="c8c2s12-lin"></div>
            <div class="text-[10px] text-slate-400">To Moon (~3,84,000 km): 1.92 Billion rungs!</div>
        </div>
        <div class="p-3 bg-slate-950 rounded-xl border border-emerald-700/60 space-y-1">
            <div class="text-emerald-400 font-bold">Exponential (×2 each step)</div>
            <div class="text-emerald-300 font-bold" id="c8c2s12-exp"></div>
            <div class="text-[10px] text-amber-300">To Moon (0.001 cm paper): ONLY 46 Folds!</div>
        </div>
    </div>
</div>

<script>
function updC8C2S12() {
    const n = parseInt(document.getElementById("c8c2s12-n").value);
    const linAmt = n * 100;
    const expAmt = Math.pow(2, n - 1);
    document.getElementById("c8c2s12-nv").textContent = "n = " + n;
    document.getElementById("c8c2s12-badge").textContent = "Step n = " + n;
    document.getElementById("c8c2s12-lin").textContent = "Additive Jar: " + n + " × 100 = ₹" + linAmt.toLocaleString("en-IN");
    document.getElementById("c8c2s12-exp").textContent = "Doubling Coin: 2^" + (n - 1) + " = ₹" + expAmt.toLocaleString("en-IN");
}
updC8C2S12();
</script>
"""

# Simulator 13: Orders Of Magnitude (Seconds Age & Cosmic Scales Slider)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⏳</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Cosmic &amp; Time Scale Explorer (10⁷s Year to 10²⁵ Drops)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c2s13-badge">10⁹ s</span>
    </div>

    <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <button onclick="setScaleS13(0)" class="px-2.5 py-1 rounded-lg bg-cyan-700 text-white font-bold">10⁷ s (~1 Yr)</button>
        <button onclick="setScaleS13(1)" class="px-2.5 py-1 rounded-lg bg-emerald-700 text-white font-bold">10⁹ s (~31.7 Yrs)</button>
        <button onclick="setScaleS13(2)" class="px-2.5 py-1 rounded-lg bg-indigo-700 text-white font-bold">10¹⁰–10¹⁵ s (Eras)</button>
        <button onclick="setScaleS13(3)" class="px-2.5 py-1 rounded-lg bg-amber-700 text-white font-bold">10¹⁷ s (Universe)</button>
        <button onclick="setScaleS13(4)" class="px-2.5 py-1 rounded-lg bg-rose-700 text-white font-bold">10²³ vs 10²⁵</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-amber-300 font-bold text-sm" id="c8c2s13-title"></div>
        <div class="text-cyan-200" id="c8c2s13-desc"></div>
        <div class="text-emerald-300 font-bold" id="c8c2s13-math"></div>
    </div>
</div>

<script>
const scaleEvents = [
    { b: "10⁷ s", t: "1 Calendar Year ≈ 3.15 × 10⁷ Seconds", d: "365 days × 24 hours × 3,600 seconds/hour = 3,15,36,000 s", m: "Order of Magnitude: ~10⁷ seconds per year" },
    { b: "10⁹ s", t: "1 Billion Seconds = ~31.7 Years (Human Milestone!)", d: "10⁹ ÷ (3.15 × 10⁷ s/yr) ≈ 31.71 years — a 32-year-old has lived >10⁹ seconds!", m: "Also compares with ~8 × 10⁹ human population on Earth" },
    { b: "10¹⁰–10¹⁵ s", t: "Human Civilizations (10¹⁰ s) & Evolution (10¹²–10¹⁵ s)", d: "Recorded history sits around 10¹⁰ s while ancient evolutionary milestones span 10¹²–10¹⁵ s.", m: "Ratio 10¹⁵ ÷ 10¹⁰ = 10⁵ (1,00,000× longer!)" },
    { b: "10¹⁷ s", t: "Age of the Observable Universe (~4.3 × 10¹⁷ Seconds)", d: "13.8 billion years × (3.15 × 10⁷ s/yr) ≈ 4.3 × 10¹⁷ seconds", m: "Order of Magnitude: 10¹⁷ seconds total" },
    { b: "10²³ vs 10²⁵", t: "Stars in Universe (~10²³) vs Earth Water Drops (~10²⁵)", d: "Critically endangered species sit around 10⁰–10³; stars ~10²³; ocean drops ~10²⁵.", m: "Quotient Rule: 10²⁵ ÷ 10²³ = 10² = 100× more drops than stars!" }
];
function setScaleS13(idx) {
    const ev = scaleEvents[idx];
    document.getElementById("c8c2s13-badge").textContent = ev.b;
    document.getElementById("c8c2s13-title").textContent = ev.t;
    document.getElementById("c8c2s13-desc").textContent = ev.d;
    document.getElementById("c8c2s13-math").textContent = ev.m;
}
setScaleS13(1);
</script>
"""

# Simulator 14: Units Digit Cycles & Power Comparison (2^n, 3^n, 4^n, 9^n + 2^100 vs 3^75)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔁</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Cyclic Units-Digit Finder &amp; Giant Power Comparator</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c2s14-badge">Last Digit: 4</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Base Digit (2,3,4,5,6,9):</span></div>
            <select id="c8c2s14-b" onchange="updC8C2S14()" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2 py-1 text-cyan-300 font-bold">
                <option value="2" selected>Base 2 — Cycle {2, 4, 8, 6}</option>
                <option value="3">Base 3 — Cycle {3, 9, 7, 1}</option>
                <option value="4">Base 4 — Cycle {4, 6}</option>
                <option value="5">Base 5 — Always 5</option>
                <option value="6">Base 6 — Always 6</option>
                <option value="9">Base 9 — Cycle {9, 1}</option>
            </select>
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Exponent (n):</span><span class="font-bold text-amber-300" id="c8c2s14-nv">50</span></div>
            <input type="range" min="1" max="100" step="1" value="50" id="c8c2s14-n" oninput="updC8C2S14()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2 font-mono text-xs">
        <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-emerald-300 font-bold" id="c8c2s14-res"></div>
        <div class="p-2 bg-amber-950/30 rounded-lg border border-amber-700/50 text-amber-200 font-bold">Giant Comparison Trick: 2¹⁰⁰ = (2⁴)²⁵ = 16²⁵  vs  3⁷⁵ = (3³)²⁵ = 27²⁵ ⇒ 3⁷⁵ WINS!</div>
    </div>
</div>

<script>
const cycles14 = {
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    9: [9, 1]
};
function updC8C2S14() {
    const b = parseInt(document.getElementById("c8c2s14-b").value);
    const n = parseInt(document.getElementById("c8c2s14-n").value);
    const cyc = cycles14[b];
    const len = cyc.length;
    const rem = ((n - 1) % len);
    const last = cyc[rem];

    document.getElementById("c8c2s14-nv").textContent = n;
    document.getElementById("c8c2s14-badge").textContent = "Last Digit: " + last;
    document.getElementById("c8c2s14-res").textContent = b + "^" + n + " uses cycle {" + cyc.join(", ") + "} (period " + len + ") → entry #" + (rem + 1) + " gives Units Digit = " + last;
}
updC8C2S14();
</script>
"""

# Simulator 15: Ancient Large Powers (Indian Historical Texts & Naming Grids + Googol)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📜</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Historical Powers Gallery &amp; Indian vs International Grid</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c2s15-badge">Lalitavistara 10⁵³</span>
    </div>

    <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <button onclick="setHistS15(0)" class="px-2.5 py-1 rounded-lg bg-amber-700 text-white font-bold">Lalitavistara (10⁵³)</button>
        <button onclick="setHistS15(1)" class="px-2.5 py-1 rounded-lg bg-cyan-700 text-white font-bold">Amalasiddhi (10⁹⁶)</button>
        <button onclick="setHistS15(2)" class="px-2.5 py-1 rounded-lg bg-emerald-700 text-white font-bold">Pali (10¹⁴⁰)</button>
        <button onclick="setHistS15(3)" class="px-2.5 py-1 rounded-lg bg-indigo-700 text-white font-bold">Googol (10¹⁰⁰)</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-2">
        <div class="text-amber-300 font-bold" id="c8c2s15-desc"></div>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 text-center pt-1">
            <div class="p-1.5 rounded bg-slate-900 border border-slate-800"><span class="text-cyan-300 font-bold">Lakh</span><br><span class="text-slate-400">10⁵</span></div>
            <div class="p-1.5 rounded bg-slate-900 border border-slate-800"><span class="text-cyan-300 font-bold">Crore</span><br><span class="text-slate-400">10⁷</span></div>
            <div class="p-1.5 rounded bg-slate-900 border border-slate-800"><span class="text-emerald-300 font-bold">Arab / Billion</span><br><span class="text-slate-400">10⁹</span></div>
            <div class="p-1.5 rounded bg-slate-900 border border-slate-800"><span class="text-amber-300 font-bold">Shankh</span><br><span class="text-slate-400">10¹⁷</span></div>
        </div>
    </div>
</div>

<script>
const hist15 = [
    { b: "10⁵³ Tallakshana", d: "Lalitavistara (Buddhist text) named Tallakshana = 10⁵³! Mahaviracharya (850 CE) also listed up to 10²³." },
    { b: "10⁹⁶ Amalasiddhi", d: "Ancient Jaina treatise Amalasiddhi reached 10⁹⁶; Hungary printed a 10²¹ (1 sextillion) pengő note in 1946!" },
    { b: "10¹⁴⁰ Asankhyeya", d: "Ancient Pali texts climbed all the way to 10¹⁴⁰ — vastly larger than stars in the observable universe (10²³)!" },
    { b: "10¹⁰⁰ Googol", d: "1 Googol = 10¹⁰⁰ (1 followed by 100 zeros), while 1 Googolplex = 10^(10¹⁰⁰) = 1 followed by a googol zeros!" }
];
function setHistS15(idx) {
    document.getElementById("c8c2s15-badge").textContent = hist15[idx].b;
    document.getElementById("c8c2s15-desc").textContent = hist15[idx].d;
}
setHistS15(0);
</script>
"""

# Simulator 16: Chapter Two Summary (Tremendous in Ten! Max Tower Game with {2, 3, 4})
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏆</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Tremendous in Ten! Maximize {2, 3, 4} Tower Arena</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c2s16-badge">Champion: 2^(3⁴)</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs font-mono">
        <button onclick="pickTowerS16(0)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-200 font-bold">4 × 3 × 2</button>
        <button onclick="pickTowerS16(1)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-cyan-300 font-bold">(2³)⁴</button>
        <button onclick="pickTowerS16(2)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-700 text-amber-300 font-bold">4^(3²)</button>
        <button onclick="pickTowerS16(3)" class="p-2 rounded-xl bg-emerald-700 hover:bg-emerald-600 text-white font-bold">2^(3⁴) 👑</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1">
        <div class="text-emerald-300 font-bold text-sm" id="c8c2s16-val"></div>
        <div class="text-amber-200" id="c8c2s16-why"></div>
    </div>
</div>

<script>
const towers16 = [
    { lbl: "4 × 3 × 2", val: "24", why: "Pure multiplication barely reaches 24 — never waste digits on × or +!" },
    { lbl: "(2³)⁴", val: "2¹² = 4,096", why: "Parentheses multiply exponents (3 × 4 = 12), stopping early at 4,096." },
    { lbl: "4^(3²)", val: "4⁹ = 2¹⁸ = 2,62,144", why: "Strong try (over 2.6 lakh!), yet swapping base 2 bottom unlocks exponent 81!" },
    { lbl: "2^(3⁴)", val: "2⁸¹ ≈ 2.4178 × 10²⁴ (25-digit colossus!)", why: "CHAMPION! Putting 3⁴ = 81 high up top explodes 2⁸¹ past 2.4 septillion!" }
];
function pickTowerS16(idx) {
    const t = towers16[idx];
    document.getElementById("c8c2s16-badge").textContent = t.lbl;
    document.getElementById("c8c2s16-val").textContent = "Result: " + t.lbl + " = " + t.val;
    document.getElementById("c8c2s16-why").textContent = t.why;
}
pickTowerS16(3);
</script>
"""

if __name__ == "__main__":
    print(f"Prepared {len(simulators_part2)} interactive simulators (Part 2).")
