#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 11: Areas Related to Circles
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Horse Grazing in a 15m Square Field (5m -> 10m Rope) — Ex 11.1 Q8
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🐎</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Square Grass Field Grazing Explorer (Ex 11.1 Q8)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c11s9-badge">Rope = 10 m</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Slide Rope Length From 5 m to 10 m (15 m × 15 m Square Field):</span><span class="font-bold text-amber-300" id="c11s9-rv">10 m</span></div>
        <input type="range" min="5" max="10" step="1" value="10" id="c11s9-r" oninput="updC11S9()" class="w-full accent-emerald-400">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 150 150" class="w-full max-h-36 bg-slate-950 rounded-xl border border-slate-800" id="c11s9-svg"></svg>
        <div class="space-y-2 font-mono text-xs">
            <div class="bg-slate-950 p-2 rounded-lg border border-slate-800 text-cyan-300" id="c11s9-base">5 m Rope = ¼×3.14×25 = 19.625 m²</div>
            <div class="bg-emerald-950/60 p-2 rounded-lg border border-emerald-800 text-emerald-200 font-bold" id="c11s9-cur"></div>
            <div class="bg-amber-950/60 p-2 rounded-lg border border-amber-800 text-amber-200 font-bold" id="c11s9-inc"></div>
        </div>
    </div>
</div>

<script>
function updC11S9() {
    const r = parseInt(document.getElementById("c11s9-r").value, 10);
    document.getElementById("c11s9-rv").textContent = r + " m";
    document.getElementById("c11s9-badge").textContent = "Rope = " + r + " m";

    const base = 0.25 * 3.14 * 25;
    const cur = 0.25 * 3.14 * r * r;
    const inc = cur - base;

    document.getElementById("c11s9-cur").textContent = `${r} m Rope Grazing Area = ${cur.toFixed(3)} m²`;
    document.getElementById("c11s9-inc").textContent = `Increase over 5 m = +${inc.toFixed(3)} m²`;

    const sx = 20, sy = 130, box = 105;
    const rBasePx = (5 / 15) * box;
    const rCurPx = (r / 15) * box;

    document.getElementById("c11s9-svg").innerHTML = `
        <rect x="${sx}" y="${sy-box}" width="${box}" height="${box}" fill="rgba(22,163,74,0.12)" stroke="#4ade80" stroke-width="2"/>
        <path d="M ${sx} ${sy} L ${sx+rCurPx} ${sy} A ${rCurPx} ${rCurPx} 0 0 0 ${sx} ${sy-rCurPx} Z" fill="rgba(251,191,36,0.38)" stroke="#fbbf24" stroke-width="2"/>
        <path d="M ${sx} ${sy} L ${sx+rBasePx} ${sy} A ${rBasePx} ${rBasePx} 0 0 0 ${sx} ${sy-rBasePx} Z" fill="rgba(6,182,212,0.55)" stroke="#22d3ee" stroke-width="1.5"/>
        <circle cx="${sx}" cy="${sy}" r="3.5" fill="#fff"/>
        <text x="${sx+box/2}" y="${sy-box-5}" fill="#86efac" font-size="9" text-anchor="middle">15 m × 15 m Field</text>
    `;
}
updC11S9();
</script>
"""

# Simulator 10: Silver Wire Brooch (5 Diameters + 10 Equal Sectors) — Ex 11.1 Q9
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">💠</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Silver Wire Brooch Lab (Ex 11.1 Q9: d = 35 mm)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">5 Diameters → 10 Sectors</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC11S10(1)" id="btn-1110-1" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">(i) Total Wire = 285 mm</button>
        <button onclick="pickC11S10(2)" id="btn-1110-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">(ii) 1 Sector = 385/4 mm²</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 150 140" class="w-full max-h-36 bg-slate-950 rounded-xl border border-slate-800" id="c11s10-svg"></svg>
        <div class="font-mono text-xs space-y-2" id="c11s10-info"></div>
    </div>
</div>

<script>
function pickC11S10(part) {
    document.getElementById("btn-1110-1").className = part === 1
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-1110-2").className = part === 2
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const cx = 75, cy = 70, r = 52;
    let lines = "";
    for (let i = 0; i < 5; i++) {
        const a = (i * 36) * Math.PI / 180;
        const x1 = cx + r * Math.cos(a), y1 = cy + r * Math.sin(a);
        const x2 = cx - r * Math.cos(a), y2 = cy - r * Math.sin(a);
        lines += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${part === 1 ? '#fde047' : '#64748b'}" stroke-width="1.6"/>`;
    }
    let wedge = "";
    if (part === 2) {
        const x1 = cx + r, y1 = cy;
        const x2 = cx + r * Math.cos(36 * Math.PI / 180), y2 = cy - r * Math.sin(36 * Math.PI / 180);
        wedge = `<path d="M ${cx} ${cy} L ${x1} ${y1} A ${r} ${r} 0 0 0 ${x2} ${y2} Z" fill="rgba(16,185,129,0.6)" stroke="#34d399" stroke-width="2"/>`;
    }
    document.getElementById("c11s10-svg").innerHTML = `
        <circle cx="${cx}" cy="${cy}" r="${r}" fill="rgba(56,189,248,0.12)" stroke="${part === 1 ? '#22d3ee' : '#475569'}" stroke-width="2.5"/>
        ${lines}${wedge}<circle cx="${cx}" cy="${cy}" r="3" fill="#fff"/>
    `;

    const info = document.getElementById("c11s10-info");
    if (part === 1) {
        info.innerHTML = `<div class="text-cyan-300 font-bold">Diameter d = 35 mm, π = 22/7</div>
            <div class="text-slate-200">Rim Circumference = πd = (22/7)×35 = 110 mm</div>
            <div class="text-amber-300">5 Straight Diameters = 5×35 = 175 mm</div>
            <div class="text-emerald-300 font-bold text-sm">Total Wire = 110 + 175 = 285 mm!</div>`;
    } else {
        info.innerHTML = `<div class="text-emerald-300 font-bold">10 Equal Sectors ⇒ θ = 360°/10 = 36°, r = 35/2 mm</div>
            <div class="text-slate-200">Area = (1/10) × (22/7) × (35/2) × (35/2)</div>
            <div class="text-white font-bold text-sm">Exact = 385 / 4 mm² (= 96.25 mm²)!</div>`;
    }
}
pickC11S10(1);
</script>
"""

# Simulator 11: Umbrella Ribs (Q10) & Twin Non-Overlapping Car Wipers (Q11)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">☂️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Everyday Sectors: Umbrella & Twin Car Wipers (Ex 11.1 Q10-11)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">π = 22/7 Mode</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="pickC11S11(10)" id="btn-1111-10" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs">Ex 11.1 Q10: 8-Rib Umbrella</button>
        <button onclick="pickC11S11(11)" id="btn-1111-11" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">Ex 11.1 Q11: 2 Car Wipers</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2" id="c11s11-box"></div>
</div>

<script>
function pickC11S11(q) {
    document.getElementById("btn-1111-10").className = q === 10
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    document.getElementById("btn-1111-11").className = q === 11
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";

    const box = document.getElementById("c11s11-box");
    if (q === 10) {
        box.innerHTML = `
            <div class="text-amber-300 font-bold">Ex 11.1 Q10: Open Umbrella (r = 45 cm, 8 Equally Spaced Ribs)</div>
            <div class="text-slate-200">Angle between two consecutive ribs = 360° / 8 = 45° (1/8 of circle)</div>
            <div class="text-cyan-300">Area = (1/8) × (22/7) × 45 × 45 = (11 × 2025) / (4 × 7)</div>
            <div class="text-emerald-300 font-bold text-sm">Exact Result = 22,275 / 28 cm² (≈ 795.54 cm²)</div>
        `;
    } else {
        box.innerHTML = `
            <div class="text-amber-300 font-bold">Ex 11.1 Q11: Two Non-Overlapping Car Wipers (r = 25 cm, θ = 115°)</div>
            <div class="text-slate-200">1 Wiper Area = (115/360) × (22/7) × 25 × 25 = 158,125 / 252 cm²</div>
            <div class="text-cyan-300">Total Area (2 blades) = 2 × (158,125 / 252)</div>
            <div class="text-emerald-300 font-bold text-sm">Exact Combined Area = 158,125 / 126 cm² (≈ 1254.96 cm²)</div>
        `;
    }
}
pickC11S11(10);
</script>
"""

# Simulator 12: Coastal Lighthouse Warning Sector (80°, 16.5 km) — Ex 11.1 Q12
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🚨</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Lighthouse Sea Warning Sector (Ex 11.1 Q12)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">π = 3.14 Specified</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Adjust Warning Sector Angle θ (Ex 11.1 Q12 sets 80°, r = 16.5 km):</span><span class="font-bold text-rose-300" id="c11s12-thv">80°</span></div>
        <input type="range" min="20" max="160" step="10" value="80" id="c11s12-th" oninput="updC11S12()" class="w-full accent-rose-500">
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 180 120" class="w-full max-h-32 bg-slate-950 rounded-xl border border-slate-800" id="c11s12-svg"></svg>
        <div class="font-mono text-xs space-y-1.5">
            <div class="text-cyan-300" id="c11s12-step1"></div>
            <div class="text-amber-300" id="c11s12-step2"></div>
            <div class="text-emerald-300 font-bold text-sm" id="c11s12-ans"></div>
        </div>
    </div>
</div>

<script>
function updC11S12() {
    const th = parseInt(document.getElementById("c11s12-th").value, 10);
    document.getElementById("c11s12-thv").textContent = th + "°";
    const r = 16.5;
    const area = (th / 360) * 3.14 * r * r;

    document.getElementById("c11s12-step1").textContent = `Formula: (${th}/360) × 3.14 × 16.5 × 16.5`;
    document.getElementById("c11s12-step2").textContent = th === 80
        ? "Clean Cancel: (2/9) × 3.14 × (16.5)² = 2 × 3.14 × 5.5 × 5.5!"
        : `Angle Fraction = ${(th/360).toFixed(4)} × 854.865`;
    document.getElementById("c11s12-ans").textContent = `Warned Sea Area = ${area.toFixed(2)} km²`;

    const lx = 25, ly = 60, sr = 120;
    const h = (th / 2) * Math.PI / 180;
    const x1 = lx + sr * Math.cos(-h), y1 = ly + sr * Math.sin(-h);
    const x2 = lx + sr * Math.cos(h), y2 = ly + sr * Math.sin(h);
    document.getElementById("c11s12-svg").innerHTML = `
        <path d="M ${lx} ${ly} L ${x1} ${y1} A ${sr} ${sr} 0 0 1 ${x2} ${y2} Z" fill="rgba(244,63,94,0.38)" stroke="#fb7185" stroke-width="2"/>
        <circle cx="${lx}" cy="${ly}" r="5" fill="#fde047"/>
        <text x="${lx+8}" y="${ly+4}" fill="#fde047" font-size="9" font-weight="bold">${th}°</text>
        <text x="${lx+80}" y="${ly+4}" fill="#fda4af" font-size="9">16.5 km beam</text>
    `;
}
updC11S12();
</script>
"""

# Simulator 13: Round Table Cover 6 Hexagonal Segments & Cost — Ex 11.1 Q13
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⬡</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Round Table Cover 6-Segment Cost Lab (Ex 11.1 Q13)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">r = 28 cm, ₹0.35/cm²</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickC11S13(0)" id="btn-1113-0" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs">1. Full Circle (2464)</button>
        <button onclick="pickC11S13(1)" id="btn-1113-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">2. Minus 6△ (1999.2)</button>
        <button onclick="pickC11S13(2)" id="btn-1113-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">3. Cost ₹162.68!</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 150 140" class="w-full max-h-36 bg-slate-950 rounded-xl border border-slate-800" id="c11s13-svg"></svg>
        <div class="font-mono text-xs space-y-1.5" id="c11s13-info"></div>
    </div>
</div>

<script>
function pickC11S13(st) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-1113-" + k).className = k === st
            ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const cx = 75, cy = 70, r = 54;
    let pts = [];
    let spokes = "";
    for (let i = 0; i < 6; i++) {
        const a = (i * 60 - 90) * Math.PI / 180;
        const x = cx + r * Math.cos(a), y = cy + r * Math.sin(a);
        pts.push(`${x.toFixed(1)},${y.toFixed(1)}`);
        spokes += `<line x1="${cx}" y1="${cy}" x2="${x.toFixed(1)}" y2="${y.toFixed(1)}" stroke="#64748b" stroke-dasharray="3 2" stroke-width="1"/>`;
    }
    const polyPts = pts.join(" ");
    const info = document.getElementById("c11s13-info");
    if (st === 0) {
        document.getElementById("c11s13-svg").innerHTML = `<circle cx="${cx}" cy="${cy}" r="${r}" fill="rgba(6,182,212,0.45)" stroke="#22d3ee" stroke-width="2"/>${spokes}`;
        info.innerHTML = `<div class="text-cyan-300 font-bold">Full Table Cover Circle (r = 28 cm)</div>
            <div class="text-slate-200">Area = (22/7) × 28 × 28 = 22 × 4 × 28</div>
            <div class="text-emerald-300 font-bold">= 2,464 cm²</div>`;
    } else if (st === 1) {
        document.getElementById("c11s13-svg").innerHTML = `<circle cx="${cx}" cy="${cy}" r="${r}" fill="rgba(6,182,212,0.2)" stroke="#22d3ee" stroke-width="1.5"/>
            <polygon points="${polyPts}" fill="rgba(244,63,94,0.5)" stroke="#fb7185" stroke-width="2"/>${spokes}`;
        info.innerHTML = `<div class="text-rose-300 font-bold">Inscribed Hexagon = 6 × 60° Equilateral △s</div>
            <div class="text-slate-200">6 × (1.7/4) × 28 × 28 = 6 × 1.7 × 7 × 28</div>
            <div class="text-rose-200 font-bold">= 1,999.2 cm² (subtract from circle!)</div>`;
    } else {
        document.getElementById("c11s13-svg").innerHTML = `<circle cx="${cx}" cy="${cy}" r="${r}" fill="rgba(16,185,129,0.55)" stroke="#34d399" stroke-width="2"/>
            <polygon points="${polyPts}" fill="#0f172a" stroke="#94a3b8" stroke-width="1.5"/>`;
        info.innerHTML = `<div class="text-emerald-300 font-bold">6 Outer Designs = 2,464 − 1,999.2 = 464.8 cm²</div>
            <div class="text-amber-300">Rate = ₹0.35 / cm²</div>
            <div class="text-white font-bold text-sm">Total Cost = 464.8 × 0.35 = ₹162.68!</div>`;
    }
}
pickC11S13(2);
</script>
"""

# Simulator 14: Scaling Effects (r vs θ) & Ex 11.1 Q14 Formula Check (p/720 × 2πR²)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔍</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Radius vs Angle Scaling & Ex 11.1 Q14 Dimension Check</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">l ∝ r vs A ∝ r²</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Radius Scale Factor (k_r):</span><span class="font-bold text-cyan-300" id="c11s14-krv">2×</span></div>
            <input type="range" min="1" max="4" step="1" value="2" id="c11s14-kr" oninput="updC11S14()" class="w-full accent-cyan-400">
        </div>
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Angle Scale Factor (k_θ):</span><span class="font-bold text-amber-300" id="c11s14-ktv">1×</span></div>
            <input type="range" min="1" max="4" step="1" value="1" id="c11s14-kt" oninput="updC11S14()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 font-mono text-xs">
        <div class="bg-slate-950 p-3 rounded-xl border border-cyan-800 text-cyan-200" id="c11s14-arc"></div>
        <div class="bg-slate-950 p-3 rounded-xl border border-purple-800 text-purple-200 font-bold" id="c11s14-area"></div>
    </div>
    <div class="bg-emerald-950/50 p-2.5 rounded-xl border border-emerald-800 font-mono text-xs text-emerald-200 font-bold">
        Ex 11.1 Q14 Check: (p / 720°) × 2πR² cancels 2/720 → (p / 360°) × πR² (Dimension R² = Area!)
    </div>
</div>

<script>
function updC11S14() {
    const kr = parseInt(document.getElementById("c11s14-kr").value, 10);
    const kt = parseInt(document.getElementById("c11s14-kt").value, 10);
    document.getElementById("c11s14-krv").textContent = kr + "×";
    document.getElementById("c11s14-ktv").textContent = kt + "×";

    document.getElementById("c11s14-arc").textContent = `Arc Length Scales By: k_θ × k_r = ${kt} × ${kr} = ${kt * kr}×`;
    document.getElementById("c11s14-area").textContent = `Sector Area Scales By: k_θ × (k_r)² = ${kt} × ${kr}² = ${kt * kr * kr}×`;
}
updC11S14();
</script>
"""

# Simulator 15: Universal ½r²sinθ, Concentric Ring & Wheel Revolutions
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚡</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Three Master Shortcuts: ½r²sinθ, Rings & Wheel Revolutions</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">High-Speed Board Tools</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="pickC11S15(1)" id="btn-1115-1" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs">1. ½ r² sin θ</button>
        <button onclick="pickC11S15(2)" id="btn-1115-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">2. Ring π(R²−r²)</button>
        <button onclick="pickC11S15(3)" id="btn-1115-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700">3. Wheel Rolls</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 font-mono text-xs space-y-2" id="c11s15-box"></div>
</div>

<script>
function pickC11S15(m) {
    for (let k = 1; k <= 3; k++) {
        document.getElementById("btn-1115-" + k).className = k === m
            ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700";
    }
    const box = document.getElementById("c11s15-box");
    if (m === 1) {
        box.innerHTML = `<div class="text-cyan-300 font-bold">Universal Chord Triangle Area: Area(△OAB) = ½ r² sin θ</div>
            <div class="text-slate-200">• θ = 90°: ½ r² sin 90° = ½ r² (Ex 11.1 Q4)</div>
            <div class="text-amber-300">• θ = 60°: ½ r² (√3/2) = (√3/4) r² (Ex 11.1 Q5 & Q6)</div>
            <div class="text-emerald-300 font-bold">• θ = 120°: ½ r² sin 120° = ½ r² (√3/2) = (√3/4) r² (Ex 11.1 Q7!)</div>`;
    } else if (m === 2) {
        box.innerHTML = `<div class="text-purple-300 font-bold">Concentric Circular Ring: Area = π(R² − r²) = π(R + r)(R − r)</div>
            <div class="text-slate-200">Example: Outer R = 10 cm, Inner r = 6 cm</div>
            <div class="text-emerald-300 font-bold">Ring Area = π(10+6)(10−6) = π × 16 × 4 = 64π cm²!</div>`;
    } else {
        box.innerHTML = `<div class="text-amber-300 font-bold">Rolling Wheel Revolutions = Total Distance ÷ (2πr)</div>
            <div class="text-slate-200">Example: Wheel r = 35 cm travelling 11 km (11,000 m), π = 22/7</div>
            <div class="text-cyan-300">1 Revolution = 2×(22/7)×35 = 220 cm = 2.2 m</div>
            <div class="text-emerald-300 font-bold">Revolutions = 11,000 m ÷ 2.2 m = 5,000 Complete Turns!</div>`;
    }
}
pickC11S15(1);
</script>
"""

# Simulator 16: Section 11.2 Master Summary & All-In-One Formula Calculator
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏆</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Section 11.2 Master Formula Vault & Live Solver</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">All 5 Formulas Live</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Central Angle θ:</span><span class="font-bold text-cyan-300" id="c11s16-thv">60°</span></div>
            <input type="range" min="30" max="150" step="30" value="60" id="c11s16-th" oninput="updC11S16()" class="w-full accent-cyan-400">
        </div>
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1">
            <div class="flex justify-between"><span class="text-slate-300">Radius r (cm):</span><span class="font-bold text-emerald-300" id="c11s16-rv">14 cm</span></div>
            <input type="range" min="7" max="28" step="7" value="14" id="c11s16-r" oninput="updC11S16()" class="w-full accent-emerald-400">
        </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 font-mono text-xs">
        <div class="bg-slate-950 p-2.5 rounded-xl border border-cyan-800 text-cyan-200" id="c11s16-f1"></div>
        <div class="bg-slate-950 p-2.5 rounded-xl border border-amber-800 text-amber-200" id="c11s16-f2"></div>
        <div class="bg-slate-950 p-2.5 rounded-xl border border-emerald-800 text-emerald-200 font-bold" id="c11s16-f3"></div>
        <div class="bg-slate-950 p-2.5 rounded-xl border border-purple-800 text-purple-200 font-bold" id="c11s16-f4"></div>
    </div>
</div>

<script>
function updC11S16() {
    const th = parseInt(document.getElementById("c11s16-th").value, 10);
    const r = parseInt(document.getElementById("c11s16-r").value, 10);
    document.getElementById("c11s16-thv").textContent = th + "°";
    document.getElementById("c11s16-rv").textContent = r + " cm";

    const pi = 22 / 7;
    const l = (th / 360) * 2 * pi * r;
    const sec = (th / 360) * pi * r * r;
    const per = l + 2 * r;
    const tri = 0.5 * r * r * Math.sin(th * Math.PI / 180);
    const minSeg = sec - tri;
    const majSeg = pi * r * r - minSeg;

    document.getElementById("c11s16-f1").textContent = `Arc l = ${l.toFixed(2)} cm | Perimeter l+2r = ${per.toFixed(2)} cm`;
    document.getElementById("c11s16-f2").textContent = `Sector = ${sec.toFixed(2)} cm² | △OAB = ${tri.toFixed(2)} cm²`;
    document.getElementById("c11s16-f3").textContent = `Minor Segment = ${minSeg.toFixed(2)} cm²`;
    document.getElementById("c11s16-f4").textContent = `Major Segment = ${majSeg.toFixed(2)} cm²`;
}
updC11S16();
</script>
"""
