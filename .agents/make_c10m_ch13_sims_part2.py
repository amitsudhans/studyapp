#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 13: Statistics
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Ex 13.2 Applied Mode vs Mean Comparison (Q1 Hospital, Q2 Bulbs, Q4 Schools)
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏥</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Ex 13.2 Solver: Mode Calculations & Meaning vs Mean</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">NCERT Ex 13.2</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickC13S9(1)" id="btn-139-1" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs">Q1: Hospital (36.8)</button>
        <button onclick="pickC13S9(2)" id="btn-139-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Q2: Bulbs (65.625)</button>
        <button onclick="pickC13S9(4)" id="btn-139-4" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Q4: Schools (30.6)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2" id="c13s9-box"></div>
</div>

<script>
function pickC13S9(q) {
    for (const k of [1, 2, 4]) {
        document.getElementById("btn-139-" + k).className = k === q
            ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const box = document.getElementById("c13s9-box");
    if (q === 1) {
        box.innerHTML = `<div class="text-cyan-300 font-bold">Ex 13.2 Q1: Hospital Patient Ages (35–45 modal: l=35, f₁=23, f₀=21, f₂=14, h=10)</div>
            <div class="text-emerald-300 font-bold">Mode = 35 + [(23−21)/(46−21−14)]×10 = 35 + 20/11 = 36.8 years (Most common patient age!)</div>
            <div class="text-amber-300">Mean = 35.37 years (Overall average patient age across all wards)</div>`;
    } else if (q === 2) {
        box.innerHTML = `<div class="text-cyan-300 font-bold">Ex 13.2 Q2: 225 Components Lifetime (60–80 modal: l=60, f₁=61, f₀=52, f₂=38, h=20)</div>
            <div class="text-slate-200">Mode = 60 + [(61 − 52) / (122 − 52 − 38)] × 20 = 60 + (9/32)×20</div>
            <div class="text-emerald-300 font-bold">Modal Lifetime = 65.625 hours!</div>`;
    } else {
        box.innerHTML = `<div class="text-cyan-300 font-bold">Ex 13.2 Q4: Students/Teacher (30–35 modal: l=30, f₁=10, f₀=9, f₂=3, h=5)</div>
            <div class="text-emerald-300 font-bold">Mode = 30 + (1/8)×5 = 30.625 ≈ 30.6 (Most states fall around 30.6 students/teacher)</div>
            <div class="text-amber-300">Mean = 29.2 students per teacher across all surveyed regions.</div>`;
    }
}
pickC13S9(1);
</script>
"""

# Simulator 10: Less Than Cumulative Converter & Reverser (Ex 13.3 Q3)
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📈</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">'Less Than' Cumulative Builder & Ex 13.3 Q3 Reverser</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Uses Upper Limits</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC13S10(0)" id="btn-1310-0" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs">Forward: fᵢ → Less Than cf</button>
        <button onclick="pickC13S10(1)" id="btn-1310-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Reverse: Ex 13.3 Q3 (cf → fᵢ)</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs" id="c13s10-box"></div>
</div>

<script>
function pickC13S10(m) {
    document.getElementById("btn-1310-0").className = m === 0
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-1310-1").className = m === 1
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const box = document.getElementById("c13s10-box");
    if (m === 0) {
        box.innerHTML = `<div class="text-cyan-300 font-bold mb-1">Forward Rule: Pair Upper Class Limits & Add Downward!</div>
            <div class="text-slate-200">0–10 (f=5) ⇒ Less than 10: cf = 5</div>
            <div class="text-slate-200">10–20 (f=3) ⇒ Less than 20: cf = 5 + 3 = 8</div>
            <div class="text-emerald-300 font-bold">20–30 (f=4) ⇒ Less than 30: cf = 8 + 4 = 12  (Strictly increasing!)</div>`;
    } else {
        box.innerHTML = `<div class="text-amber-300 font-bold mb-1">Reverse Policy Holders (Ex 13.3 Q3): Subtract Consecutive cf!</div>
            <div class="text-slate-200">Below 20: 2  ⇒ Class &lt;20 has f = 2</div>
            <div class="text-slate-200">Below 25: 6  ⇒ Class 20–25 has f = 6 − 2 = 4</div>
            <div class="text-emerald-300 font-bold">Below 30: 24 ⇒ Class 25–30 has f = 24 − 6 = 18! (Median = 35.76 yr)</div>`;
    }
}
pickC13S10(1);
</script>
"""

# Simulator 11: Dual Ogive Plotter ("Less Than" & "More Than" Intersection at Median)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📉</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">'Less Than' vs 'More Than' Ogive Intersection Lab</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">Crosses at (Median, n/2)</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 200 130" class="w-full max-h-36 bg-slate-950 rounded-xl border border-slate-800">
            <line x1="25" y1="10" x2="25" y2="110" stroke="#64748b" stroke-width="1.5"/>
            <line x1="25" y1="110" x2="190" y2="110" stroke="#64748b" stroke-width="1.5"/>
            <polyline points="25,110 60,92 100,60 145,25 180,15" fill="none" stroke="#34d399" stroke-width="2.5"/>
            <polyline points="25,15 60,30 100,60 145,95 180,110" fill="none" stroke="#fbbf24" stroke-width="2.5"/>
            <line x1="100" y1="60" x2="100" y2="110" stroke="#f43f5e" stroke-dasharray="3 2" stroke-width="2"/>
            <line x1="25" y1="60" x2="100" y2="60" stroke="#f43f5e" stroke-dasharray="3 2" stroke-width="1.5"/>
            <circle cx="100" cy="60" r="4.5" fill="#f43f5e" stroke="#fff" stroke-width="1.5"/>
            <text x="100" y="123" fill="#fda4af" font-size="9" text-anchor="middle" font-weight="bold">Median</text>
            <text x="12" y="63" fill="#fda4af" font-size="8.5" text-anchor="middle">n/2</text>
        </svg>
        <div class="font-mono text-xs space-y-1.5">
            <div class="text-emerald-300 font-bold">Green Rising Curve: 'Less Than' Ogive (Upper Limits, 0 → n)</div>
            <div class="text-amber-300 font-bold">Amber Falling Curve: 'More Than' Ogive (Lower Limits, n → 0)</div>
            <div class="text-rose-300 font-bold">Intersection Crosshair: Exact (Median, n/2)!</div>
        </div>
    </div>
</div>

<script>
// Dual ogive diagram ready
</script>
"""

# Simulator 12: Grouped Median Step-by-Step Formula & Preceding cf Guard
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📏</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Median Class & Preceding-cf Guard (Girls Heights n = 51)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">n/2 = 25.5</span>
    </div>

    <div class="overflow-x-auto bg-slate-950 rounded-xl border border-slate-800 p-2 font-mono text-[11px]">
        <table class="w-full text-center">
            <thead><tr class="text-cyan-300 border-b border-slate-800"><th>Height (cm)</th><th>f</th><th>Less Than cf</th><th>Formula Role</th></tr></thead>
            <tbody class="text-slate-200">
                <tr><td>Below 140</td><td>4</td><td>4</td><td>—</td></tr>
                <tr class="text-amber-300 font-bold"><td>140–145</td><td>7</td><td>11</td><td>Preceding cf = 11!</td></tr>
                <tr class="bg-emerald-950/50 text-emerald-300 font-bold"><td>145–150</td><td>18</td><td>29 (≥ 25.5)</td><td>MEDIAN CLASS (l=145, f=18)</td></tr>
                <tr><td>150–155</td><td>11</td><td>40</td><td>—</td></tr>
                <tr><td>155–165</td><td>11</td><td>51 (= n)</td><td>—</td></tr>
            </tbody>
        </table>
    </div>
    <div class="bg-emerald-950/50 p-2.5 rounded-xl border border-emerald-800 font-mono text-xs text-emerald-200 font-bold">
        Median = 145 + [(25.5 − 11) / 18] × 5 = 145 + 72.5/18 = 149.03 cm! (NEVER put 29 instead of 11!)
    </div>
</div>

<script>
// Median class guard display ready
</script>
"""

# Simulator 13: Dual Missing Frequencies (x, y) Solver — Ex 13.3 Q2
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔍</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Dual Missing Unknowns (x, y) Solver (Ex 13.3 Q2: Median = 28.5)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c13s13-badge">x=8, y=7</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Slide Unknown x in 10–20 (Constraint n = 60 enforces y = 15 − x):</span><span class="font-bold text-amber-300" id="c13s13-xv">x = 8, y = 7</span></div>
        <input type="range" min="3" max="12" step="1" value="8" id="c13s13-x" oninput="updC13S13()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-cyan-300" id="c13s13-cf"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c13s13-med"></div>
        <div class="text-amber-300" id="c13s13-stat"></div>
    </div>
</div>

<script>
function updC13S13() {
    const x = parseInt(document.getElementById("c13s13-x").value, 10);
    const y = 15 - x;
    const prevCf = 5 + x;
    const med = 20 + ((30 - prevCf) / 20) * 10;
    document.getElementById("c13s13-xv").textContent = `x = ${x}, y = ${y}`;
    document.getElementById("c13s13-badge").textContent = `x=${x}, y=${y}`;
    document.getElementById("c13s13-cf").textContent = `Preceding cf (below 20–30) = 5 + ${x} = ${prevCf} | Median = 20 + [(30 − ${prevCf})/20] × 10`;
    document.getElementById("c13s13-med").textContent = `Resulting Median = ${med.toFixed(1)}`;
    document.getElementById("c13s13-stat").textContent = x === 8
        ? "✓ EXACT TARGET MEDIAN = 28.5 HIT AT (x = 8, y = 7)!"
        : "Slide to hit target Median = 28.5 (solve 17 = 25 − x)!";
}
updC13S13();
</script>
"""

# Simulator 14: Outlier Sensitivity Demo (Mean vs Median vs Mode Selection)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚖️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Outlier Distortion Simulator: Why Median Beats Mean</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">9 Staff @ ₹20k + 1 Founder</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Founder Monthly Salary (₹ Lakhs):</span><span class="font-bold text-rose-300" id="c13s14-fv">₹50 Lakhs</span></div>
        <input type="range" min="1" max="50" step="1" value="50" id="c13s14-f" oninput="updC13S14()" class="w-full accent-rose-500">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 font-mono text-xs">
        <div class="bg-slate-950 p-3 rounded-xl border border-rose-800 text-rose-200 font-bold" id="c13s14-mean"></div>
        <div class="bg-slate-950 p-3 rounded-xl border border-emerald-800 text-emerald-200 font-bold">Median = ₹20,000 (Immune!)</div>
        <div class="bg-slate-950 p-3 rounded-xl border border-cyan-800 text-cyan-200 font-bold">Mode = ₹20,000 (9 of 10!)</div>
    </div>
</div>

<script>
function updC13S14() {
    const fLakhs = parseInt(document.getElementById("c13s14-f").value, 10);
    document.getElementById("c13s14-fv").textContent = "₹" + fLakhs + (fLakhs === 1 ? " Lakh" : " Lakhs");
    const total = 9 * 20000 + fLakhs * 100000;
    const mean = total / 10;
    document.getElementById("c13s14-mean").textContent = `Mean = ₹${Math.round(mean).toLocaleString()} (Distorted!)`;
}
updC13S14();
</script>
"""

# Simulator 15: Empirical Relation Solver (3 Median = Mode + 2 Mean)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔗</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Empirical Relation Live Calculator (3 Median = Mode + 2 Mean)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">Skewed Law</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Given Mean (x̄):</span><span class="font-bold text-cyan-300" id="c13s15-mv">24</span></div>
            <input type="range" min="10" max="60" step="1" value="24" id="c13s15-m" oninput="updC13S15()" class="w-full accent-cyan-400">
        </div>
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Given Median (M):</span><span class="font-bold text-emerald-300" id="c13s15-mdv">26</span></div>
            <input type="range" min="10" max="60" step="1" value="26" id="c13s15-md" oninput="updC13S15()" class="w-full accent-emerald-400">
        </div>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-purple-300" id="c13s15-eq"></div>
        <div class="text-amber-300 font-bold text-sm" id="c13s15-mode"></div>
        <div class="text-slate-400 text-[11px]">Ex 13.3 Q1 Check: Mean 137.05, Median 137 ⇒ 3(137) = 411 ≈ Mode (135.76) + 2(137.05) = 409.86!</div>
    </div>
</div>

<script>
function updC13S15() {
    const mean = parseInt(document.getElementById("c13s15-m").value, 10);
    const med = parseInt(document.getElementById("c13s15-md").value, 10);
    const mode = 3 * med - 2 * mean;
    document.getElementById("c13s15-mv").textContent = mean;
    document.getElementById("c13s15-mdv").textContent = med;
    document.getElementById("c13s15-eq").textContent = `Mode = 3 Median − 2 Mean = 3(${med}) − 2(${mean}) = ${3*med} − ${2*mean}`;
    document.getElementById("c13s15-mode").textContent = `Estimated Mode = ${mode}` + (mean === med ? "  (Perfectly Symmetric Distribution!)" : "");
}
updC13S15();
</script>
"""

# Simulator 16: Section 13.5 Master All-In-One 4-Class Grouped Analyzer
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏆</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Section 13.5 Live Mean + Mode + Median Calculator</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Classes 0–10 to 30–40</span>
    </div>

    <div class="grid grid-cols-4 gap-2 text-xs">
        <div class="bg-slate-900/90 p-2 rounded-xl border border-slate-800 text-center">
            <div class="text-slate-400">0–10 f₁</div>
            <input type="number" min="1" max="50" value="5" id="c13s16-f0" oninput="updC13S16()" class="w-full mt-1 bg-slate-950 text-center text-cyan-300 font-bold rounded border border-slate-700 p-1">
        </div>
        <div class="bg-slate-900/90 p-2 rounded-xl border border-slate-800 text-center">
            <div class="text-slate-400">10–20 f₂</div>
            <input type="number" min="1" max="50" value="12" id="c13s16-f1" oninput="updC13S16()" class="w-full mt-1 bg-slate-950 text-center text-cyan-300 font-bold rounded border border-slate-700 p-1">
        </div>
        <div class="bg-slate-900/90 p-2 rounded-xl border border-slate-800 text-center">
            <div class="text-slate-400">20–30 f₃</div>
            <input type="number" min="1" max="50" value="8" id="c13s16-f2" oninput="updC13S16()" class="w-full mt-1 bg-slate-950 text-center text-cyan-300 font-bold rounded border border-slate-700 p-1">
        </div>
        <div class="bg-slate-900/90 p-2 rounded-xl border border-slate-800 text-center">
            <div class="text-slate-400">30–40 f₄</div>
            <input type="number" min="1" max="50" value="5" id="c13s16-f3" oninput="updC13S16()" class="w-full mt-1 bg-slate-950 text-center text-cyan-300 font-bold rounded border border-slate-700 p-1">
        </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 font-mono text-xs">
        <div class="bg-slate-950 p-2.5 rounded-xl border border-cyan-800 text-cyan-200 font-bold" id="c13s16-mean"></div>
        <div class="bg-slate-950 p-2.5 rounded-xl border border-rose-800 text-rose-200 font-bold" id="c13s16-mode"></div>
        <div class="bg-slate-950 p-2.5 rounded-xl border border-emerald-800 text-emerald-200 font-bold" id="c13s16-med"></div>
    </div>
</div>

<script>
function updC13S16() {
    const fs = [0, 1, 2, 3].map(i => Math.max(1, parseInt(document.getElementById("c13s16-f" + i).value, 10) || 1));
    const xs = [5, 15, 25, 35];
    const n = fs.reduce((a, b) => a + b, 0);
    const mean = fs.reduce((s, f, i) => s + f * xs[i], 0) / n;

    let mIdx = 0;
    for (let i = 1; i < 4; i++) { if (fs[i] > fs[mIdx]) mIdx = i; }
    const f1 = fs[mIdx], f0 = mIdx > 0 ? fs[mIdx - 1] : 0, f2 = mIdx < 3 ? fs[mIdx + 1] : 0;
    const mode = (mIdx * 10) + ((f1 - f0) / Math.max(1, 2 * f1 - f0 - f2)) * 10;

    let cf = 0, medIdx = 0, prevCf = 0;
    for (let i = 0; i < 4; i++) {
        if (cf + fs[i] >= n / 2) { medIdx = i; prevCf = cf; break; }
        cf += fs[i];
    }
    const med = (medIdx * 10) + ((n / 2 - prevCf) / fs[medIdx]) * 10;

    document.getElementById("c13s16-mean").textContent = `Mean x̄ = ${mean.toFixed(2)}`;
    document.getElementById("c13s16-mode").textContent = `Mode Z = ${mode.toFixed(2)}`;
    document.getElementById("c13s16-med").textContent = `Median M = ${med.toFixed(2)} (n=${n})`;
}
updC13S16();
</script>
"""
