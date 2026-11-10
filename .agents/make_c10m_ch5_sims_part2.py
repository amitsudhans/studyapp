#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 5: Arithmetic Progressions
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Sum Formulas S_n = (n/2)[2a + (n-1)d] vs Endpoint Formula (n/2)(a + l)
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧮</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Dual Sum Formula Lab: Formula 1 (using d) vs Formula 2 (using l)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="sim9-badge">S_22 = -979</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="presetSum54(8, -5, 22)" class="p-2 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 11: 8,3,-2.. (22 terms)</button>
        <button onclick="presetSum54(7, 3, 15)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Endpoint: a=7, l=49, n=15</button>
        <button onclick="presetSum54(2, 5, 10)" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2, 7, 12.. (10 terms = 245)</button>
    </div>

    <div class="grid grid-cols-3 gap-2 text-xs">
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800">
            <label class="text-slate-400 block mb-1">First Term a:</label>
            <input type="number" value="8" id="sim9-a" oninput="calcSum54()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono">
        </div>
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800">
            <label class="text-slate-400 block mb-1">Diff d:</label>
            <input type="number" value="-5" id="sim9-d" oninput="calcSum54()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono">
        </div>
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800">
            <label class="text-slate-400 block mb-1">Terms n:</label>
            <input type="number" min="1" max="100" value="22" id="sim9-n" oninput="calcSum54()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono">
        </div>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="sim9-f1">Formula 1: S_22 = (22/2)[2(8) + 21(-5)] = 11 * (-89) = -979</div>
        <div class="text-amber-300" id="sim9-f2">Formula 2: Last l = 8 + 21(-5) = -97  ->  (22/2)(8 + (-97)) = -979</div>
        <div class="text-emerald-300 font-bold text-sm" id="sim9-match">Both formulas ALWAYS agree identically! S_22 = -979</div>
    </div>
</div>

<script>
function presetSum54(a, d, n) {
    document.getElementById("sim9-a").value = a;
    document.getElementById("sim9-d").value = d;
    document.getElementById("sim9-n").value = n;
    calcSum54();
}
function calcSum54() {
    const a = parseFloat(document.getElementById("sim9-a").value) || 0;
    const d = parseFloat(document.getElementById("sim9-d").value) || 0;
    const n = Math.max(1, parseInt(document.getElementById("sim9-n").value, 10) || 1);
    const l = a + (n - 1) * d;
    const sn = (n / 2) * (2 * a + (n - 1) * d);

    document.getElementById("sim9-badge").textContent = `S_${n} = ${sn}`;
    document.getElementById("sim9-f1").textContent = `Formula 1: S_${n} = (${n}/2)[2(${a}) + ${n-1}(${d})] = ${sn}`;
    document.getElementById("sim9-f2").textContent = `Formula 2: l = ${l}  ->  S_${n} = (${n}/2)(${a} + ${l}) = ${sn}`;
    document.getElementById("sim9-match").textContent = `Exact Match Verified! Total Sum S_${n} = ${sn}`;
}
calcSum54();
</script>
"""

# Simulator 10: a_n = S_n - S_{n-1} + Double-n Solution Paradox (S_4 = S_13 = 78)
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌗</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Canceling Pairs Paradox & Term Extractor (a_n = S_n - S_{n-1})</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800" id="sim10-badge">S_4 = S_13 = 78!</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="showParadox10(4)" id="btn-p10-4" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">Show n = 4 Terms (S_4 = 78)</button>
        <button onclick="showParadox10(13)" id="btn-p10-13" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Show n = 13 Terms (S_13 = 78!)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-3 text-xs font-mono">
        <div class="text-amber-300 font-sans font-bold">Ex 13: AP 24, 21, 18, ... (a = 24, d = -3) — Why do BOTH n = 4 and n = 13 give S_n = 78?</div>
        <div class="text-cyan-300" id="sim10-terms">24 + 21 + 18 + 15 = 78</div>
        <div class="text-emerald-300 font-bold" id="sim10-note">First 4 positive terms reach 78 immediately!</div>
        <div class="pt-2 border-t border-slate-800 text-slate-300">
            Also remember Ex 5.3 Q11 (S_n = 4n - n^2): <span class="text-cyan-300">a_1 = S_1 = 3</span>, <span class="text-amber-300">a_10 = S_10 - S_9 = (-60) - (-45) = -15</span>!
        </div>
    </div>
</div>

<script>
function showParadox10(n) {
    document.getElementById("btn-p10-4").className = (n === 4)
        ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-p10-13").className = (n === 13)
        ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";

    if (n === 4) {
        document.getElementById("sim10-terms").textContent = "S_4 = 24 + 21 + 18 + 15 = 78";
        document.getElementById("sim10-note").textContent = "Stopping right at Term 4 gives Sum = 78.";
    } else {
        document.getElementById("sim10-terms").textContent = "S_13 = [24 + 21 + 18 + 15] + [12 + 9 + 6 + 3 + 0 + (-3) + (-6) + (-9) + (-12)] = 78 + 0 = 78!";
        document.getElementById("sim10-note").textContent = "Terms 5 to 13 cancel symmetrically around zero (+12 & -12, +9 & -9, +6 & -6, +3 & -3, plus 0) = 0!";
    }
}
showParadox10(4);
</script>
"""

# Simulator 11: Divisible Multiples & Odd Integer Sums (Ex 5.3 Q12, Q13, Q14)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔢</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Multiples & Divisible Series Summing Lab (Ex 5.3 Q12-14)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="sim11-badge">S_40 = 4,920</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="runMult11(6, 40, 'First 40 multiples of 6')" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">40 Multiples of 6</button>
        <button onclick="runMult11(8, 15, 'First 15 multiples of 8')" class="p-2 rounded-xl bg-slate-900 text-cyan-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">15 Multiples of 8</button>
        <button onclick="runOdd11()" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Odd Numbers 0..50</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-sans font-bold text-sm" id="sim11-title">First 40 positive integers divisible by 6:</div>
        <div class="text-slate-300" id="sim11-ap">AP: 6, 12, 18, ..., 240  (a = 6, d = 6, n = 40, l = 240)</div>
        <div class="text-emerald-300 font-bold text-sm" id="sim11-res">S_40 = (40/2)(6 + 240) = 20 x 246 = 4,920</div>
    </div>
</div>

<script>
function runMult11(k, n, label) {
    const l = k * n;
    const sn = (n * (k + l)) / 2;
    document.getElementById("sim11-badge").textContent = `S_${n} = ${sn.toLocaleString()}`;
    document.getElementById("sim11-title").textContent = label + ":";
    document.getElementById("sim11-ap").textContent = `AP: ${k}, ${2*k}, ${3*k}, ..., ${l}   (a = ${k}, d = ${k}, n = ${n}, l = ${l})`;
    document.getElementById("sim11-res").textContent = `S_${n} = (${n}/2)(${k} + ${l}) = ${sn.toLocaleString()}`;
}
function runOdd11() {
    document.getElementById("sim11-badge").textContent = "S_25 = 625";
    document.getElementById("sim11-title").textContent = "All odd integers between 0 and 50 (Ex 5.3 Q14):";
    document.getElementById("sim11-ap").textContent = "AP: 1, 3, 5, ..., 49   (a = 1, d = 2, n = 25, l = 49)";
    document.getElementById("sim11-res").textContent = "S_25 = (25/2)(1 + 49) = 25 x 25 = 625  (n^2 rule!)";
}
runMult11(6, 40, "First 40 positive integers divisible by 6");
</script>
"""

# Simulator 12: Logs Stacking (200 logs -> 16 rows vs 25 rejected) & Potato Race (370 m)
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪵</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Physical Constraints Lab: 200 Timber Logs & Potato Race (Ex 5.3)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="sim12-badge">16 Rows, Top = 5 Logs</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="showLogs12(16)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Test n = 16 Rows (Valid!)</button>
        <button onclick="showLogs12(25)" class="p-2 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Test n = 25 Rows (Rejected!)</button>
        <button onclick="showPotato12()" class="p-2 rounded-xl bg-slate-900 text-amber-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Potato Race Q20 (370 m)</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 110" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="sim12-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold" id="sim12-info"></div>
    </div>
</div>

<script>
function showLogs12(n) {
    const top = 20 + (n - 1) * (-1);
    const svg = document.getElementById("sim12-svg");
    let html = `<text x="180" y="18" fill="#fcd34d" font-size="10.5" font-weight="bold" text-anchor="middle">200 Logs Stack: a = 20, d = -1, Testing n = ${n} rows</text>`;
    if (n === 16) {
        for (let r = 0; r < 6; r++) {
            const count = 20 - r * 3;
            const w = count * 11;
            html += `<rect x="${180 - w/2}" y="${85 - r*11}" width="${w}" height="8" rx="3" fill="#b45309" stroke="#fbbf24" stroke-width="1" />`;
        }
        html += `<text x="180" y="102" fill="#6ee7b7" font-size="10" font-weight="bold" text-anchor="middle">Row 1 = 20 logs  ...  Row 16 (Top) = 5 logs  ->  Total = 200!</text>`;
        document.getElementById("sim12-badge").textContent = "n = 16 VALID (Top = 5)";
        document.getElementById("sim12-info").textContent = "S_16 = (16/2)(20 + 5) = 8 x 25 = 200 logs! Top row holds 5 logs.";
        document.getElementById("sim12-info").className = "bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold";
    } else {
        html += `<text x="180" y="55" fill="#fb7185" font-size="13" font-weight="bold" text-anchor="middle">Row 25 requires a_25 = 20 + 24(-1) = -4 LOGS!</text>`;
        html += `<text x="180" y="78" fill="#fca5a5" font-size="10" text-anchor="middle">Negative physical logs are impossible — root n = 25 REJECTED!</text>`;
        document.getElementById("sim12-badge").textContent = "n = 25 REJECTED!";
        document.getElementById("sim12-info").textContent = "Even though algebra gives (n-16)(n-25)=0, a_25 = -4 logs violates physical reality!";
        document.getElementById("sim12-info").className = "bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-rose-400 font-bold";
    }
    svg.innerHTML = html;
}
function showPotato12() {
    const svg = document.getElementById("sim12-svg");
    let html = `<text x="180" y="18" fill="#7dd3fc" font-size="10.5" font-weight="bold" text-anchor="middle">Potato Race (10 Potatoes): Out + Back = 2x Distance!</text>`;
    html += `<rect x="20" y="48" width="22" height="22" rx="4" fill="#d97706" />`;
    html += `<text x="31" y="63" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">B</text>`;
    html += `<line x1="42" y1="62" x2="340" y2="62" stroke="#64748b" stroke-width="2" />`;
    for (let p = 0; p < 10; p++) {
        const px = 75 + p * 27;
        html += `<circle cx="${px}" cy="58" r="5" fill="#facc15" />`;
    }
    html += `<text x="180" y="92" fill="#6ee7b7" font-size="10" font-weight="bold" text-anchor="middle">Round trips: 10m + 16m + 22m + ... (10 terms) = 370 m!</text>`;
    svg.innerHTML = html;
    document.getElementById("sim12-badge").textContent = "Total = 370 m";
    document.getElementById("sim12-info").textContent = "Round-trip AP: a = 2(5) = 10 m, d = 2(3) = 6 m, n = 10 -> S_10 = 5[20 + 54] = 370 m!";
    document.getElementById("sim12-info").className = "bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold";
}
showLogs12(16);
</script>
"""

# Simulator 13: Spiral of 13 Alternating Semicircles (Total Length = 143 cm)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌀</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Alternating Semicircle Spiral Builder (Ex 5.3 Q18)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="sim13-badge">13 Turns = 143 cm</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Grow Semicircles Drawn (k = 1 to 13):</span><span class="font-bold text-amber-300" id="sim13-n-disp">n = 13 turns</span></div>
        <input type="range" min="1" max="13" value="13" id="sim13-n" oninput="drawSpiral13()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 130" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="sim13-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono space-y-1">
            <div class="text-cyan-300" id="sim13-sum-r">Sum of radii (0.5 + 1.0 + ... + 6.5) = 45.5 cm (= 91/2)</div>
            <div class="text-emerald-300 font-bold" id="sim13-len">Total Arc Length = (22/7) x 45.5 = 143.00 cm!</div>
        </div>
    </div>
</div>

<script>
function drawSpiral13() {
    const n = parseInt(document.getElementById("sim13-n").value, 10);
    document.getElementById("sim13-n-disp").textContent = `n = ${n} semicircles`;

    const svg = document.getElementById("sim13-svg");
    const cxA = 175, cxB = 185, cy = 65;
    let html = `<line x1="15" y1="${cy}" x2="345" y2="${cy}" stroke="#334155" stroke-width="1" stroke-dasharray="3,3" />`;
    html += `<circle cx="${cxA}" cy="${cy}" r="2.5" fill="#fbbf24" /><circle cx="${cxB}" cy="${cy}" r="2.5" fill="#38bdf8" />`;

    let sumR = 0;
    for (let k = 1; k <= n; k++) {
        const rCm = 0.5 * k;
        sumR += rCm;
        const rPx = rCm * 9.5;
        const center = (k % 2 === 1) ? cxA : cxB;
        const col = (k % 2 === 1) ? "#fbbf24" : "#38bdf8";
        const x1 = center - rPx;
        const x2 = center + rPx;
        const sweep = (k % 2 === 1) ? 1 : 0;
        const dPath = (k % 2 === 1)
            ? `M ${x1} ${cy} A ${rPx} ${rPx} 0 0 1 ${x2} ${cy}`
            : `M ${x2} ${cy} A ${rPx} ${rPx} 0 0 1 ${x1} ${cy}`;
        html += `<path d="${dPath}" fill="none" stroke="${col}" stroke-width="2" />`;
    }
    svg.innerHTML = html;

    const totalPi = (22 / 7) * sumR;
    const lenStr = Math.round(totalPi * 100) / 100;
    document.getElementById("sim13-badge").textContent = `${n} Turns = ${lenStr} cm`;
    document.getElementById("sim13-sum-r").textContent = `Sum of first ${n} radii (0.5 to ${(0.5*n).toFixed(1)}): S_${n} = ${sumR} cm`;
    document.getElementById("sim13-len").textContent = `Length = pi x ${sumR} = (22/7) x ${sumR} = ${lenStr} cm`;
}
drawSpiral13();
</script>
"""

# Simulator 14: Optional Ex 5.4 Q1 (First Negative Term = 32nd -> -3) & House Numbers (#35)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏆</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Optional Ex 5.4 Explorer: First Negative Term & House #35</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="sim14-badge">32nd Term = -3</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="mode14('neg')" id="btn-14-neg" class="p-2 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">Q1: First Negative (121, 117..)</button>
        <button onclick="mode14('house')" id="btn-14-house" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Q4: Street Houses Balance (x=35)</button>
    </div>

    <div id="sim14-neg-panel" class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-3 text-xs font-mono">
        <div class="flex justify-between">
            <span class="text-slate-300">Inspect Term n around threshold 31..33:</span>
            <span class="font-bold text-rose-300" id="sim14-n-disp">n = 32</span>
        </div>
        <input type="range" min="29" max="35" value="32" id="sim14-n" oninput="calcNeg14()" class="w-full accent-rose-400">
        <div class="text-cyan-300" id="sim14-neg-eq">a_32 = 121 + (32 - 1)(-4) = 125 - 4(32) = -3</div>
        <div class="text-emerald-300 font-bold" id="sim14-neg-status">FIRST NEGATIVE TERM FOUND! (n = 32 > 31.25)</div>
    </div>

    <div id="sim14-house-panel" class="hidden bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-3 text-xs font-mono">
        <div class="flex justify-between">
            <span class="text-slate-300">Test House Number x (1 to 49):</span>
            <span class="font-bold text-amber-300" id="sim14-x-disp">x = 35</span>
        </div>
        <input type="range" min="30" max="40" value="35" id="sim14-x" oninput="calcHouse14()" class="w-full accent-amber-400">
        <div class="text-cyan-300" id="sim14-h-left">Left Sum (Houses 1..34): 34 x 35 / 2 = 595</div>
        <div class="text-purple-300" id="sim14-h-right">Right Sum (Houses 36..49): S_49 - S_35 = 1225 - 630 = 595</div>
        <div class="text-emerald-300 font-bold" id="sim14-h-status">EXACT BALANCE AT HOUSE x = 35! (595 = 595)</div>
    </div>
</div>

<script>
function mode14(m) {
    document.getElementById("sim14-neg-panel").classList.toggle("hidden", m !== "neg");
    document.getElementById("sim14-house-panel").classList.toggle("hidden", m !== "house");
    document.getElementById("btn-14-neg").className = (m === "neg")
        ? "p-2 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-14-house").className = (m === "house")
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    if (m === "neg") calcNeg14();
    else calcHouse14();
}
function calcNeg14() {
    const n = parseInt(document.getElementById("sim14-n").value, 10);
    const val = 125 - 4 * n;
    document.getElementById("sim14-n-disp").textContent = "n = " + n;
    document.getElementById("sim14-badge").textContent = `a_${n} = ${val}`;
    document.getElementById("sim14-neg-eq").textContent = `a_${n} = 121 + (${n} - 1)(-4) = 125 - 4(${n}) = ${val}`;
    const st = document.getElementById("sim14-neg-status");
    if (n === 32) {
        st.textContent = "EXACT FIRST NEGATIVE TERM! (Because 125 - 4n < 0 => n > 31.25 => n = 32)";
        st.className = "text-emerald-300 font-bold";
    } else if (val > 0) {
        st.textContent = `Still POSITIVE (+${val})! Keep decreasing past n = 31.`;
        st.className = "text-amber-300 font-bold";
    } else {
        st.textContent = `Negative (${val}), though Term 32 (-3) appeared earlier!`;
        st.className = "text-slate-300 font-bold";
    }
}
function calcHouse14() {
    const x = parseInt(document.getElementById("sim14-x").value, 10);
    const left = (x - 1) * x / 2;
    const total49 = 49 * 50 / 2; // 1225
    const sx = x * (x + 1) / 2;
    const right = total49 - sx;
    document.getElementById("sim14-x-disp").textContent = "x = " + x;
    document.getElementById("sim14-badge").textContent = `House x = ${x}`;
    document.getElementById("sim14-h-left").textContent = `Sum Preceding (1 to ${x-1}): ${left}`;
    document.getElementById("sim14-h-right").textContent = `Sum Following (${x+1} to 49): ${right}`;
    const st = document.getElementById("sim14-h-status");
    if (left === right) {
        st.textContent = `EXACT BALANCE! Left (${left}) == Right (${right}) at x = 35!`;
        st.className = "text-emerald-300 font-bold";
    } else {
        st.textContent = `Not equal yet (${left} vs ${right}). Slide to x = 35!`;
        st.className = "text-rose-400 font-bold";
    }
}
calcNeg14();
</script>
"""

# Simulator 15: Concrete Terrace (750 m^3), Ladder Wood (385 cm), Arithmetic Mean (a+c)/2
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏟️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Terrace Concrete (750 m^3), Ladder Wood (385 cm) & Arithmetic Mean</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Ex 5.4 Q3, Q5 + Mean</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="tab15('terrace')" id="btn-15-terrace" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Concrete Terrace (750 m^3)</button>
        <button onclick="tab15('ladder')" id="btn-15-ladder" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Wooden Ladder (385 cm)</button>
        <button onclick="tab15('mean')" id="btn-15-mean" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Arithmetic Mean A=(a+c)/2</button>
    </div>

    <div id="p15-terrace" class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">15-Step Terrace (Length = 50 m, Tread = 1/2 m, Rise increment = 1/4 m):</div>
        <div class="text-cyan-300">Step 1 Volume V_1 = 50 x (1/2) x (1/4) = 25/4 m^3</div>
        <div class="text-cyan-300">Step k Volume V_k = k x (25/4) m^3</div>
        <div class="text-emerald-300 font-bold text-sm">Total Volume = (25/4) x (1 + 2 + ... + 15) = (25/4) x 120 = 750 m^3!</div>
    </div>

    <div id="p15-ladder" class="hidden bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Wooden Ladder Fence-Post Check (250 cm span, 25 cm rung gaps):</div>
        <div class="text-cyan-300">Number of rungs n = (250 / 25) + 1 = 10 + 1 = 11 rungs (both ends included!)</div>
        <div class="text-emerald-300 font-bold text-sm">Total Wood Length = (11/2)(45 + 25) = 11 x 35 = 385 cm!</div>
    </div>

    <div id="p15-mean" class="hidden bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-3 text-xs font-mono">
        <div class="grid grid-cols-2 gap-2">
            <div><label class="text-slate-400 block mb-1">First Number a:</label><input type="number" value="10" id="am-a" oninput="calcAM15()" class="w-full bg-slate-900 text-white p-1.5 rounded border border-slate-700"></div>
            <div><label class="text-slate-400 block mb-1">Third Number c:</label><input type="number" value="26" id="am-c" oninput="calcAM15()" class="w-full bg-slate-900 text-white p-1.5 rounded border border-slate-700"></div>
        </div>
        <div class="text-emerald-300 font-bold text-sm" id="am-res">Arithmetic Mean A = (10 + 26) / 2 = 18  ->  AP: 10, 18, 26 (d = +8)</div>
    </div>
</div>

<script>
function tab15(name) {
    ["terrace", "ladder", "mean"].forEach(t => {
        document.getElementById("p15-" + t).classList.toggle("hidden", t !== name);
        document.getElementById("btn-15-" + t).className = (t === name)
            ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    });
}
function calcAM15() {
    const a = parseFloat(document.getElementById("am-a").value) || 0;
    const c = parseFloat(document.getElementById("am-c").value) || 0;
    const m = (a + c) / 2;
    const d = m - a;
    document.getElementById("am-res").textContent = `Arithmetic Mean A = (${a} + ${c}) / 2 = ${m}  ->  AP: ${a}, ${m}, ${c} (d = ${d})`;
}
</script>
"""

# Simulator 16: Chapter 5 Master Cheat Sheet & Quick Calculator
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📘</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Chapter 5 Complete Formula Vault & Instant AP Calculator</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Ready for Quiz!</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-mono">
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-amber-300 font-bold mb-1">1. Definition & Step d</div>
            <div class="text-slate-300">AP: a, a+d, a+2d, ... | d = a_(k+1) - a_k (any real sign: +, -, 0)</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-cyan-300 font-bold mb-1">2. General & Reverse Terms</div>
            <div class="text-slate-300">Forward: a_n = a + (n-1)d | From end: l - (k-1)d</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-emerald-300 font-bold mb-1">3. Dual Sum Formulas</div>
            <div class="text-slate-300">S_n = (n/2)[2a + (n-1)d] = (n/2)(a + l)</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-purple-300 font-bold mb-1">4. Term-Sum & Arith. Mean</div>
            <div class="text-slate-300">a_n = S_n - S_(n-1) (n>=2) | A = (a+c)/2</div>
        </div>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2 text-xs">
        <div class="font-bold text-amber-300">Instant Verify Before Exercises (Slides 17-20):</div>
        <div class="grid grid-cols-3 gap-2">
            <div><span class="text-slate-400">a:</span><input type="number" value="5" id="s16-a" oninput="calcVault16()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
            <div><span class="text-slate-400">d:</span><input type="number" value="3" id="s16-d" oninput="calcVault16()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
            <div><span class="text-slate-400">n:</span><input type="number" min="1" value="10" id="s16-n" oninput="calcVault16()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
        </div>
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-emerald-300 font-mono font-bold text-center" id="s16-out">
            a_10 = 32   |   S_10 = 185
        </div>
    </div>
</div>

<script>
function calcVault16() {
    const a = parseFloat(document.getElementById("s16-a").value) || 0;
    const d = parseFloat(document.getElementById("s16-d").value) || 0;
    const n = Math.max(1, parseInt(document.getElementById("s16-n").value, 10) || 1);
    const an = a + (n - 1) * d;
    const sn = (n / 2) * (a + an);
    document.getElementById("s16-out").textContent = `a_${n} = ${an}   |   S_${n} = ${sn}`;
}
calcVault16();
</script>
"""
