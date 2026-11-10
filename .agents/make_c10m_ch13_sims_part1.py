#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 13: Statistics
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Central Tendency Visual Explorer (Section 13.1)
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📊</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Three Central Measures on Grouped Histogram (Section 13.1)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c13s1-badge">Mean / Median / Mode</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickC13S1(0)" id="btn-131-0" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs">Mean (Balance Avg)</button>
        <button onclick="pickC13S1(1)" id="btn-131-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Mode (Tallest Peak)</button>
        <button onclick="pickC13S1(2)" id="btn-131-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Median (50% Split)</button>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2">
        <svg viewBox="0 0 320 110" class="w-full max-h-32 bg-slate-950 rounded-xl border border-slate-800" id="c13s1-svg"></svg>
        <div class="font-mono text-xs text-emerald-300 font-bold bg-slate-950 p-2.5 rounded-xl border border-slate-800" id="c13s1-info"></div>
    </div>
</div>

<script>
function pickC13S1(m) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-131-" + k).className = k === m
            ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const bars = [20, 45, 80, 52, 28];
    let rects = "";
    bars.forEach((h, i) => {
        const hi = (m === 1 && i === 2) ? "#f43f5e" : "#38bdf8";
        const op = (m === 1 && i === 2) ? "0.75" : "0.32";
        rects += `<rect x="${35 + i*50}" y="${95-h}" width="46" height="${h}" fill="${hi}" fill-opacity="${op}" stroke="${hi}" stroke-width="1.5"/>`;
    });
    let marker = "";
    if (m === 0) {
        marker = `<line x1="168" y1="8" x2="168" y2="95" stroke="#fde047" stroke-width="2.5" stroke-dasharray="4 2"/>
                  <text x="168" y="106" fill="#fde047" font-size="9" text-anchor="middle" font-weight="bold">Mean (Weighted Center)</text>`;
        document.getElementById("c13s1-info").textContent = "MEAN: Balance center Σ(fᵢxᵢ)/Σfᵢ factoring every single class interval's frequency & midpoint!";
    } else if (m === 1) {
        marker = `<text x="158" y="12" fill="#fda4af" font-size="9.5" text-anchor="middle" font-weight="bold">MODAL CLASS PEAK (f₁ Max!)</text>`;
        document.getElementById("c13s1-info").textContent = "MODE: Locates the exact peak inside the tallest bar (highest frequency Modal Class)!";
    } else {
        marker = `<line x1="158" y1="8" x2="158" y2="95" stroke="#34d399" stroke-width="2.5"/>
                  <text x="158" y="106" fill="#34d399" font-size="9" text-anchor="middle" font-weight="bold">Median Splits Area 50% | 50%</text>`;
        document.getElementById("c13s1-info").textContent = "MEDIAN: Cumulative 50% boundary (n/2) splitting lower half from upper half cleanly!";
    }
    document.getElementById("c13s1-svg").innerHTML = `${rects}${marker}`;
}
pickC13S1(0);
</script>
"""

# Simulator 2: Direct Method & Class Mark Midpoint Calculator (Table 13.1)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧮</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Direct Method Explorer (Table 13.1: Mean = 62.0)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Σfᵢ = 30</span>
    </div>

    <div class="overflow-x-auto bg-slate-950 rounded-xl border border-slate-800 p-2 font-mono text-[11px]">
        <table class="w-full text-center">
            <thead><tr class="text-cyan-300 border-b border-slate-800"><th>Class</th><th>fᵢ</th><th>Class Mark xᵢ</th><th>fᵢ × xᵢ</th></tr></thead>
            <tbody class="text-slate-200">
                <tr><td>10–25</td><td>2</td><td>17.5</td><td>35.0</td></tr>
                <tr><td>25–40</td><td>3</td><td>32.5</td><td>97.5</td></tr>
                <tr><td>40–55</td><td>7</td><td>47.5</td><td>332.5</td></tr>
                <tr><td>55–70</td><td>6</td><td>62.5</td><td>375.0</td></tr>
                <tr><td>70–85</td><td>6</td><td>77.5</td><td>465.0</td></tr>
                <tr><td>85–100</td><td>6</td><td>92.5</td><td>555.0</td></tr>
                <tr class="text-emerald-300 font-bold border-t border-slate-700"><td>Total</td><td>30</td><td>—</td><td>1,860.0</td></tr>
            </tbody>
        </table>
    </div>

    <div class="bg-emerald-950/50 p-3 rounded-xl border border-emerald-800 font-mono text-xs text-emerald-200 font-bold">
        Direct Mean x̄ = Σ(fᵢxᵢ) / Σfᵢ = 1,860 / 30 = 62.0! (Notice fᵢxᵢ can get large — next let's shrink it!)
    </div>
</div>

<script>
// Direct method verification complete
</script>
"""

# Simulator 3: Assumed Mean Method (Pick Any Baseline 'a' -> Exact 62.0!)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🎯</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Assumed Mean Method: Choose Any Baseline a (Always 62.0!)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c13s3-badge">a = 47.5</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickC13S3(1)" id="btn-133-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">a = 32.5</button>
        <button onclick="pickC13S3(2)" id="btn-133-2" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs">a = 47.5 (Middle)</button>
        <button onclick="pickC13S3(3)" id="btn-133-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">a = 62.5</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2" id="c13s3-box"></div>
</div>

<script>
function pickC13S3(idx) {
    const aVals = [0, 32.5, 47.5, 62.5];
    for (let k = 1; k <= 3; k++) {
        document.getElementById("btn-133-" + k).className = k === idx
            ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const a = aVals[idx];
    const xs = [17.5, 32.5, 47.5, 62.5, 77.5, 92.5];
    const fs = [2, 3, 7, 6, 6, 6];
    let sumfd = 0;
    const ds = xs.map((x, i) => { const d = x - a; sumfd += fs[i] * d; return d; });
    const mean = a + (sumfd / 30);

    document.getElementById("c13s3-badge").textContent = "a = " + a;
    document.getElementById("c13s3-box").innerHTML = `
        <div class="text-amber-300 font-bold">Deviations dᵢ = xᵢ − ${a}: [ ${ds.join(", ")} ]</div>
        <div class="text-slate-200">Sum Σ(fᵢdᵢ) = ${sumfd >= 0 ? "+" + sumfd : sumfd}  |  Σfᵢ = 30</div>
        <div class="text-emerald-300 font-bold text-sm">x̄ = ${a} + (${sumfd}/30) = ${a} + ${(sumfd/30).toFixed(2)} = ${mean.toFixed(1)} (EXACT SAME!)</div>`;
}
pickC13S3(2);
</script>
"""

# Simulator 4: Step-Deviation Super-Shortcut & Forget-h Trap Detector
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚡</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Step-Deviation Speedup & Don't-Forget-h Checker</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">a = 47.5, h = 15</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC13S4(1)" id="btn-134-1" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs">Correct Step-Dev (× h = 15)</button>
        <button onclick="pickC13S4(0)" id="btn-134-0" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Common Trap (Forgot × h!)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5" id="c13s4-box"></div>
</div>

<script>
function pickC13S4(ok) {
    document.getElementById("btn-134-1").className = ok === 1
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-134-0").className = ok === 0
        ? "p-2 rounded-xl bg-rose-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const box = document.getElementById("c13s4-box");
    if (ok === 1) {
        box.innerHTML = `<div class="text-cyan-300">Step Values uᵢ = [ −2, −1, 0, +1, +2, +3 ] ⇒ Σ(fᵢuᵢ) = −4−3+0+6+12+18 = +29</div>
            <div class="text-slate-200">Formula: x̄ = a + h × (Σfᵢuᵢ / Σfᵢ) = 47.5 + 15 × (29 / 30)</div>
            <div class="text-emerald-300 font-bold text-sm">✓ EXACT MEAN = 47.5 + 14.5 = 62.0!</div>`;
    } else {
        box.innerHTML = `<div class="text-rose-300 font-bold">✗ ALERT! Student calculated uᵢ cleanly (Σfᵢuᵢ = 29) but FORGOT multiplying by h = 15!</div>
            <div class="text-slate-300">Wrong calc: 47.5 + (29 / 30) = 47.5 + 0.97 = 48.47 (13.5 points OFF!)</div>
            <div class="text-amber-300 font-bold">ALWAYS multiply (Σfᵢuᵢ / Σfᵢ) × h before adding to a!</div>`;
    }
}
pickC13S4(1);
</script>
"""

# Simulator 5: Unequal Class Intervals Solver (Ex 13.1 Q7 Cricket Bowlers)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏏</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Unequal Class Widths: Cricket Bowlers (Ex 13.1 Q7)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">Widths: 40, 50, 100</span>
    </div>

    <div class="overflow-x-auto bg-slate-950 rounded-xl border border-slate-800 p-2 font-mono text-[11px]">
        <table class="w-full text-center">
            <thead><tr class="text-purple-300 border-b border-slate-800"><th>Wickets</th><th>Width</th><th>fᵢ</th><th>Midpoint xᵢ</th><th>dᵢ = xᵢ − 200</th></tr></thead>
            <tbody class="text-slate-200">
                <tr><td>20–60</td><td>40</td><td>7</td><td>40</td><td>−160</td></tr>
                <tr><td>60–100</td><td>40</td><td>5</td><td>80</td><td>−120</td></tr>
                <tr><td>100–150</td><td>50</td><td>16</td><td>125</td><td>−75</td></tr>
                <tr><td>150–250</td><td>100</td><td>12</td><td>200 (a)</td><td>0</td></tr>
                <tr><td>250–350</td><td>100</td><td>2</td><td>300</td><td>+100</td></tr>
                <tr><td>350–450</td><td>100</td><td>3</td><td>400</td><td>+200</td></tr>
            </tbody>
        </table>
    </div>
    <div class="bg-emerald-950/50 p-2.5 rounded-xl border border-emerald-800 font-mono text-xs text-emerald-200 font-bold">
        Σfᵢ = 45, Σ(fᵢdᵢ) = −2,120 ⇒ Mean = 200 − 2120/45 = 152.89 wickets! (Each row keeps its OWN true midpoint!)
    </div>
</div>

<script>
// Static unequal class interval breakdown complete
</script>
"""

# Simulator 6: Missing Frequency Pocket Allowance Solver — Ex 13.1 Q3
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪙</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Missing Frequency Algebra Lab (Ex 13.1 Q3: Target Mean = ₹18)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c13s6-badge">f = 20</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Slide Missing Frequency f (for class 19–21, midpoint x = 20):</span><span class="font-bold text-amber-300" id="c13s6-fv">f = 20</span></div>
        <input type="range" min="10" max="30" step="1" value="20" id="c13s6-f" oninput="updC13S6()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-cyan-300" id="c13s6-sum"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c13s6-mean"></div>
        <div class="text-amber-300" id="c13s6-match"></div>
    </div>
</div>

<script>
function updC13S6() {
    const f = parseInt(document.getElementById("c13s6-f").value, 10);
    const totalF = 44 + f;
    const sumFX = 752 + 20 * f;
    const mean = sumFX / totalF;
    document.getElementById("c13s6-fv").textContent = "f = " + f;
    document.getElementById("c13s6-badge").textContent = "f = " + f;
    document.getElementById("c13s6-sum").textContent = `Total Σf = 44 + ${f} = ${totalF}  |  Σ(fᵢxᵢ) = 752 + 20(${f}) = ${sumFX}`;
    document.getElementById("c13s6-mean").textContent = `Resulting Mean = ${sumFX} / ${totalF} = ₹${mean.toFixed(2)}`;
    document.getElementById("c13s6-match").textContent = f === 20
        ? "✓ TARGET MEAN = ₹18.00 HIT EXACTLY AT f = 20!"
        : "Slide to match target Mean = ₹18.00 (hint: 2f = 40 ⇒ f = 20)!";
}
updC13S6();
</script>
"""

# Simulator 7: Discontinuous Interval Continuity Shifter (±0.5) — Ex 13.1 Q5
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🥭</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Discontinuous Class (±0.5) Continuity Lab (Ex 13.1 Q5)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Gap = 1 ⇒ ±0.5</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC13S7(0)" id="btn-137-0" class="p-2 rounded-xl bg-rose-600 text-white font-bold text-xs">Raw Inclusive (50–52, 53–55)</button>
        <button onclick="pickC13S7(1)" id="btn-137-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Continuous (±0.5 Applied!)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5" id="c13s7-box"></div>
</div>

<script>
function pickC13S7(mode) {
    document.getElementById("btn-137-0").className = mode === 0
        ? "p-2 rounded-xl bg-rose-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-137-1").className = mode === 1
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const box = document.getElementById("c13s7-box");
    if (mode === 0) {
        box.innerHTML = `<div class="text-rose-300 font-bold">Inclusive Classes: [50–52], [53–55], [56–58] (Notice 1-unit gap 52 ↔ 53!)</div>
            <div class="text-cyan-300">Midpoints xᵢ: (50+52)/2 = 51, (53+55)/2 = 54, (56+58)/2 = 57 (h_step = 3!)</div>
            <div class="text-amber-300">Note: Valid for Mean directly, CANNOT plug raw limits into Mode/Median!</div>`;
    } else {
        box.innerHTML = `<div class="text-emerald-300 font-bold">Continuous Classes (±0.5): [49.5–52.5], [52.5–55.5], [55.5–58.5]</div>
            <div class="text-cyan-300">Midpoints xᵢ: (49.5+52.5)/2 = 51, (52.5+55.5)/2 = 54 — 100% INVARIANT!</div>
            <div class="text-amber-300 font-bold">True Class Width h = 52.5 − 49.5 = 3 (Ready for Mode & Median!)</div>`;
    }
}
pickC13S7(1);
</script>
"""

# Simulator 8: Interactive Grouped Mode Peak Sliders (Section 13.3 Example 5)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏔️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Grouped Mode Explorer (Modal Class 3–5, l = 3, h = 2)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c13s8-badge">Mode = 3.286</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
        <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
            <div class="flex justify-between"><span>Preceding f₀:</span><span class="font-bold text-cyan-300" id="c13s8-f0v">7</span></div>
            <input type="range" min="1" max="8" step="1" value="7" id="c13s8-f0" oninput="updC13S8()" class="w-full accent-cyan-400">
        </div>
        <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
            <div class="flex justify-between"><span>Modal Peak f₁:</span><span class="font-bold text-rose-300" id="c13s8-f1v">8</span></div>
            <input type="range" min="8" max="20" step="1" value="8" id="c13s8-f1" oninput="updC13S8()" class="w-full accent-rose-500">
        </div>
        <div class="bg-slate-900/90 p-2.5 rounded-xl border border-slate-800">
            <div class="flex justify-between"><span>Succeeding f₂:</span><span class="font-bold text-amber-300" id="c13s8-f2v">2</span></div>
            <input type="range" min="0" max="8" step="1" value="2" id="c13s8-f2" oninput="updC13S8()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="bg-slate-950 p-3.5 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-cyan-300" id="c13s8-f"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c13s8-ans"></div>
    </div>
</div>

<script>
function updC13S8() {
    const f0 = parseInt(document.getElementById("c13s8-f0").value, 10);
    const f1 = parseInt(document.getElementById("c13s8-f1").value, 10);
    const f2 = parseInt(document.getElementById("c13s8-f2").value, 10);
    document.getElementById("c13s8-f0v").textContent = f0;
    document.getElementById("c13s8-f1v").textContent = f1;
    document.getElementById("c13s8-f2v").textContent = f2;

    const mode = 3 + ((f1 - f0) / (2 * f1 - f0 - f2)) * 2;
    document.getElementById("c13s8-badge").textContent = "Mode = " + mode.toFixed(3);
    document.getElementById("c13s8-f").textContent = `Mode = 3 + [(${f1} − ${f0}) / (${2*f1} − ${f0} − ${f2})] × 2 = 3 + (${f1-f0}/${2*f1-f0-f2}) × 2`;
    document.getElementById("c13s8-ans").textContent = `Exact Estimated Mode = ${mode.toFixed(3)}` + (f0 === 7 && f1 === 8 && f2 === 2 ? "  [EXACT Example 5!]" : "");
}
updC13S8();
</script>
"""
