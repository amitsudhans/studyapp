#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 6: Triangles
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Why Three Criteria (Criterion Selector & Vertex Matching Game)
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🗝️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Minimum Similarity Criterion Selector: Valid vs Trap Checks</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c6s9-badge">AA / AAA Valid</span>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="pickCrit69(0)" id="btn-c69-0" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">AAA / AA</button>
        <button onclick="pickCrit69(1)" id="btn-c69-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">SSS (Ratios)</button>
        <button onclick="pickCrit69(2)" id="btn-c69-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">SAS (Included)</button>
        <button onclick="pickCrit69(3)" id="btn-c69-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Non-Included SSA?</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300 font-bold" id="c6s9-req"></div>
        <div class="font-bold" id="c6s9-ver"></div>
    </div>
</div>

<script>
const critList69 = [
    {
        badge: "AAA / AA Valid!",
        req: "Check ONLY 2 pairs of equal angles (3rd matches via 180° angle sum).",
        ver: "VALID (Theorem 6.3)! Automatically forces all three side ratios equal!",
        ok: true
    },
    {
        badge: "SSS Ratio Valid!",
        req: "Check all 3 corresponding side ratios: AB/DE = BC/EF = AC/DF.",
        ver: "VALID (Theorem 6.4)! Note: ratios are equal, side lengths need NOT be equal!",
        ok: true
    },
    {
        badge: "SAS Included Valid!",
        req: "Check 1 equal angle AND the two sides touching that angle (e.g. ∠B=∠E & AB/DE = BC/EF).",
        ver: "VALID (Theorem 6.5)! Guarantees remaining angles and third side ratio match!",
        ok: true
    },
    {
        badge: "SSA TRAP! Invalid!",
        req: "Suppose ∠A = ∠D and ratios AB/DE = BC/EF (∠A is NOT between AB and BC!).",
        ver: "INVALID IN GENERAL! Two distinct triangles can match SSA unless ∠A = 90° (RHS)!",
        ok: false
    }
];
function pickCrit69(idx) {
    for (let i = 0; i < 4; i++) {
        const b = document.getElementById("btn-c69-" + i);
        if (b) {
            b.className = (i === idx)
                ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
                : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
        }
    }
    const c = critList69[idx];
    document.getElementById("c6s9-badge").textContent = c.badge;
    document.getElementById("c6s9-req").textContent = "Minimum Check: " + c.req;
    const v = document.getElementById("c6s9-ver");
    v.textContent = c.ver;
    v.className = c.ok ? "font-bold text-emerald-300" : "font-bold text-rose-400";
}
pickCrit69(0);
</script>
"""

# Simulator 10: Theorem 6.3 AAA & AA Cut-and-Place Visual Proof
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">✂️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Theorem 6.3 (AAA / AA) Cut-and-Place Step Proof Animator</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c6s10-badge">Step 1 of 3</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="stepAAA10(1)" id="btn-10-1" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">1. Cut DP=AB, DQ=AC</button>
        <button onclick="stepAAA10(2)" id="btn-10-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. △ABC ≅ △DPQ -> PQ||EF</button>
        <button onclick="stepAAA10(3)" id="btn-10-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. Apply BPT Corollary</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 120" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <polygon points="75,20 35,95 115,95" fill="rgba(56,189,248,0.18)" stroke="#38bdf8" stroke-width="2" />
            <text x="75" y="13" fill="#7dd3fc" font-size="10" text-anchor="middle">A</text>
            <text x="27" y="102" fill="#7dd3fc" font-size="10">B</text>
            <text x="119" y="102" fill="#7dd3fc" font-size="10">C</text>
            <polygon points="245,10 175,112 315,112" fill="rgba(16,185,129,0.14)" stroke="#94a3b8" stroke-width="2" />
            <line x1="205" y1="68" x2="285" y2="68" stroke="#fbbf24" stroke-width="2.5" id="svg10-pq" />
            <text x="245" y="10" fill="#fff" font-size="10" text-anchor="middle">D</text>
            <text x="165" y="114" fill="#fff" font-size="10">E</text>
            <text x="320" y="114" fill="#fff" font-size="10">F</text>
            <text x="193" y="69" fill="#fcd34d" font-size="10" font-weight="bold">P</text>
            <text x="291" y="69" fill="#fcd34d" font-size="10" font-weight="bold">Q</text>
        </svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold" id="c6s10-info"></div>
    </div>
</div>

<script>
function stepAAA10(s) {
    for (let i = 1; i <= 3; i++) {
        const b = document.getElementById("btn-10-" + i);
        if (b) {
            b.className = (i === s)
                ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
                : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
        }
    }
    document.getElementById("c6s10-badge").textContent = `Step ${s} of 3`;
    const msgs = {
        1: "Given ∠A=∠D, ∠B=∠E, ∠C=∠F: Cut P on DE and Q on DF such that DP = AB and DQ = AC, then join PQ.",
        2: "By SAS Congruence, △ABC ≅ △DPQ -> ∠DPQ = ∠B = ∠E! Equal corresponding angles force PQ || EF!",
        3: "Since PQ || EF, BPT corollary gives DP/DE = DQ/DF -> AB/DE = AC/DF (similarly = BC/EF)! Hence △ABC ~ △DEF!"
    };
    document.getElementById("c6s10-info").textContent = msgs[s];
}
stepAAA10(1);
</script>
"""

# Simulator 11: Theorem 6.4 (SSS Similarity) Proportional Scaler
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📏</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Theorem 6.4 (SSS Similarity): Proportional Side Ratio Tester</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c6s11-badge">Ratio = 1 : 2</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="testSSS11(2,3,2.5, 4,6,5)" class="p-2 rounded-xl bg-slate-900 text-emerald-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2, 3, 2.5 & 4, 6, 5</button>
        <button onclick="testSSS11(3,4,5, 9,12,15)" class="p-2 rounded-xl bg-slate-900 text-cyan-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3, 4, 5 & 9, 12, 15</button>
        <button onclick="testSSS11(2.7,3,2, 5,6,4)" class="p-2 rounded-xl bg-slate-900 text-rose-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2, 3, 2.7 & 4, 6, 5 (Trap)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c6s11-ratios">Ratios: 2/4 = 0.50  |  3/6 = 0.50  |  2.5/5 = 0.50</div>
        <div class="font-bold text-sm" id="c6s11-ver">ALL THREE RATIOS EQUAL (0.50)! By Theorem 6.4 (SSS), Triangles ARE Similar!</div>
    </div>
</div>

<script>
function testSSS11(a,b,c, d,e,f) {
    const r1 = (a/d).toFixed(3), r2 = (b/e).toFixed(3), r3 = (c/f).toFixed(3);
    const same = Math.abs(a/d - b/e) < 0.001 && Math.abs(b/e - c/f) < 0.001;
    document.getElementById("c6s11-ratios").textContent = `Ratios: ${a}/${d} = ${r1}  |  ${b}/${e} = ${r2}  |  ${c}/${f} = ${r3}`;
    const v = document.getElementById("c6s11-ver");
    const badge = document.getElementById("c6s11-badge");
    if (same) {
        badge.textContent = "SSS SIMILAR!";
        badge.className = "text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-700";
        v.textContent = `CONSTANT RATIO (${r1}) -> Converse of BPT + Congruence guarantees equal angles -> SSS Similar!`;
        v.className = "font-bold text-sm text-emerald-300";
    } else {
        badge.textContent = "NOT Similar";
        badge.className = "text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-700";
        v.textContent = `RATIOS DIFFER (${r1} vs ${r2} vs ${r3}) -> FAILS SSS Similarity!`;
        v.className = "font-bold text-sm text-rose-400";
    }
}
testSSS11(2,3,2.5, 4,6,5);
</script>
"""

# Simulator 12: Theorem 6.5 (SAS Similarity) Included Angle Check
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚠️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Theorem 6.5 (SAS): Included Angle Requirement Checker (Ex 6.3 Q2 iv/vi)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c6s12-badge">Included = VALID</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="checkSAS12(true)" id="btn-12-ok" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">Included ∠M=∠Q=70°, Ratios 1:2</button>
        <button onclick="checkSAS12(false)" id="btn-12-trap" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Non-Included ∠A=80° (Ex 6.3 Trap)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c6s12-sides"></div>
        <div class="font-bold text-sm" id="c6s12-res"></div>
    </div>
</div>

<script>
function checkSAS12(ok) {
    document.getElementById("btn-12-ok").className = ok
        ? "p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-12-trap").className = !ok
        ? "p-2 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";

    const badge = document.getElementById("c6s12-badge");
    const r = document.getElementById("c6s12-res");
    if (ok) {
        badge.textContent = "SAS VALID!";
        badge.className = "text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-700";
        document.getElementById("c6s12-sides").textContent = "Angle M (70°) sits BETWEEN MN (2.5) and ML (5); Angle Q (70°) sits BETWEEN QP (5) and QR (10). Ratio 2.5/5 = 5/10 = 1/2!";
        r.textContent = "SIMILAR by SAS (Theorem 6.5)! △NML ~ △PQR cleanly!";
        r.className = "font-bold text-sm text-emerald-300";
    } else {
        badge.textContent = "SAS FAILS!";
        badge.className = "text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-700";
        document.getElementById("c6s12-sides").textContent = "△ABC has AB=2.5, BC=3, ∠A=80° while △DEF has DE=5, EF=6, ∠F=80° -> Proportional sides do NOT flank ∠A & ∠F!";
        r.textContent = "NOT SIMILAR! Equal angles are NOT included between the proportional side pairs!";
        r.className = "font-bold text-sm text-rose-400";
    }
}
checkSAS12(true);
</script>
"""

# Simulator 13: Lamp-Post Shadow & Tower Shadow Models (Interactive Time Slider)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">💡</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Lamp-Post Shadow Simulator (Example 7: 3.6 m Lamp, 0.9 m Walker)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c6s13-badge">Shadow = 1.60 m</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Walking Time t at 1.2 m/s (Example 7 uses t = 4 s):</span><span class="font-bold text-amber-300" id="c6s13-t-disp">t = 4.0 s (Walked d = 4.8 m)</span></div>
        <input type="range" min="1" max="8" step="0.5" value="4" id="c6s13-t" oninput="drawShadow13()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 space-y-3">
        <svg viewBox="0 0 360 120" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800" id="c6s13-svg"></svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-mono text-emerald-300 font-bold" id="c6s13-eq"></div>
    </div>
</div>

<script>
function drawShadow13() {
    const t = parseFloat(document.getElementById("c6s13-t").value);
    const d = 1.2 * t;
    const shadow = d / 3; // since (d+x)/x = 3.6/0.9 = 4 => 3x = d
    document.getElementById("c6s13-t-disp").textContent = `t = ${t.toFixed(1)} s  (Distance BD = ${d.toFixed(2)} m)`;
    document.getElementById("c6s13-badge").textContent = `Shadow DE = ${shadow.toFixed(2)} m`;

    const bx = 35, by = 100, ay = 20;
    const scaleX = 22;
    const dx = Math.min(265, bx + d * scaleX);
    const ex = Math.min(340, dx + shadow * scaleX);
    const cy = 80;

    document.getElementById("c6s13-svg").innerHTML = `
        <line x1="15" y1="${by}" x2="350" y2="${by}" stroke="#475569" stroke-width="2" />
        <line x1="${bx}" y1="${by}" x2="${bx}" y2="${ay}" stroke="#fbbf24" stroke-width="4" />
        <circle cx="${bx}" cy="${ay}" r="5" fill="#fef08a" />
        <line x1="${dx}" y1="${by}" x2="${dx}" y2="${cy}" stroke="#38bdf8" stroke-width="3" />
        <line x1="${bx}" y1="${ay}" x2="${ex}" y2="${by}" stroke="#fde047" stroke-width="1.5" stroke-dasharray="4,3" />
        <line x1="${dx}" y1="${by}" x2="${ex}" y2="${by}" stroke="#f43f5e" stroke-width="3.5" />
        <text x="${bx}" y="114" fill="#fcd34d" font-size="9.5" text-anchor="middle">B (Lamp 3.6m)</text>
        <text x="${dx}" y="114" fill="#7dd3fc" font-size="9.5" text-anchor="middle">D (0.9m)</text>
        <text x="${ex}" y="114" fill="#fda4af" font-size="9.5" text-anchor="middle">E (Tip)</text>
    `;
    document.getElementById("c6s13-eq").textContent =
        `AA Similarity △ABE ~ △CDE: (${d.toFixed(2)} + x)/x = 3.6 / 0.9 = 4  =>  3x = ${d.toFixed(2)}  =>  Shadow x = ${shadow.toFixed(2)} m!`;
}
drawShadow13();
</script>
"""

# Simulator 14: Median Proportionality & Perimeter Ratio Proof Explorer (Ex 6.3 Q12 & Q16)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧩</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Exercise 6.3 Proof Builder: Medians, Overlapping Triangles & Perimeters</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">Ex 6.3 Q12-16</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="showEx14(0)" id="btn-14-0" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">Q12: Medians AB,BC,AD</button>
        <button onclick="showEx14(1)" id="btn-14-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Q13: CA^2 = CB x CD</button>
        <button onclick="showEx14(2)" id="btn-14-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Q16: Perimeter Ratio</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="c6s14-l1"></div>
        <div class="text-cyan-300" id="c6s14-l2"></div>
        <div class="text-emerald-300 font-bold" id="c6s14-l3"></div>
    </div>
</div>

<script>
const p614 = [
    {
        l1: "Given AB/PQ = BC/QR = AD/PM (AD, PM are medians bisecting BC, QR):",
        l2: "Step 1: Replace BC = 2 BD and QR = 2 QM -> AB/PQ = BD/QM = AD/PM -> △ABD ~ △PQM (SSS) -> ∠B = ∠Q!",
        l3: "Step 2: Now use AB/PQ = BC/QR AND ∠B = ∠Q -> △ABC ~ △PQR cleanly by SAS Similarity!"
    },
    {
        l1: "Given D on side BC with ∠ADC = ∠BAC:",
        l2: "Compare △BAC and △ADC: ∠BAC = ∠ADC (given) and ∠C = ∠C (common angle) -> AA Similarity!",
        l3: "Therefore CA / CD = CB / CA  =>  Cross-multiply to get CA^2 = CB x CD! Proved!"
    },
    {
        l1: "Given △ABC ~ △PQR with scale factor k = AB / PQ:",
        l2: "Each side scales by k: AB = k*PQ, BC = k*QR, AC = k*PR (and median AD = k*PM by SAS).",
        l3: "Sum sides: (AB + BC + AC) / (PQ + QR + PR) = k = AB / PQ = AD / PM!"
    }
];
function showEx14(i) {
    for (let k = 0; k < 3; k++) {
        document.getElementById("btn-14-" + k).className = (k === i)
            ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    }
    document.getElementById("c6s14-l1").textContent = p614[i].l1;
    document.getElementById("c6s14-l2").textContent = p614[i].l2;
    document.getElementById("c6s14-l3").textContent = p614[i].l3;
}
showEx14(0);
</script>
"""

# Simulator 15: RHS Similarity Criterion & Right-Triangle Altitude Split (CD^2 = AD x BD)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Supplementary RHS Criterion & Right-Triangle Altitude Split</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">RHS + △ABC ~ △ACD ~ △CBD</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="tab15('rhs')" id="btn-c15-rhs" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">RHS Similarity Criterion</button>
        <button onclick="tab15('alt')" id="btn-c15-alt" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Altitude Split Calculator (CD^2=AD·BD)</button>
    </div>

    <div id="p15-rhs" class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Right △ABC (∠B=90°) & Right △PQR (∠Q=90°): Hypotenuse AC/PR = Leg AB/PQ = k</div>
        <div class="text-cyan-300">By Pythagoras: BC = sqrt(AC^2 - AB^2) = k * sqrt(PR^2 - PQ^2) = k * QR -> BC / QR = k!</div>
        <div class="text-emerald-300 font-bold">All 3 side ratios match (k) -> △ABC ~ △PQR by RHS (reducing cleanly to SSS)!</div>
    </div>

    <div id="p15-alt" class="hidden bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-3 text-xs font-mono">
        <div class="grid grid-cols-2 gap-2">
            <div><label class="text-slate-400 block mb-1">Segment AD (cm):</label><input type="number" min="1" value="4" id="alt-ad" oninput="calcAlt15()" class="w-full bg-slate-900 text-white p-1.5 rounded border border-slate-700"></div>
            <div><label class="text-slate-400 block mb-1">Segment BD (cm):</label><input type="number" min="1" value="9" id="alt-bd" oninput="calcAlt15()" class="w-full bg-slate-900 text-white p-1.5 rounded border border-slate-700"></div>
        </div>
        <div class="text-emerald-300 font-bold text-sm" id="alt-res">△ACD ~ △CBD  =>  Altitude CD = sqrt(4 x 9) = 6.00 cm!</div>
    </div>
</div>

<script>
function tab15(name) {
    document.getElementById("p15-rhs").classList.toggle("hidden", name !== "rhs");
    document.getElementById("p15-alt").classList.toggle("hidden", name !== "alt");
    document.getElementById("btn-c15-rhs").className = (name === "rhs")
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-c15-alt").className = (name === "alt")
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
}
function calcAlt15() {
    const ad = Math.max(0.5, parseFloat(document.getElementById("alt-ad").value) || 1);
    const bd = Math.max(0.5, parseFloat(document.getElementById("alt-bd").value) || 1);
    const cd = Math.sqrt(ad * bd).toFixed(2);
    document.getElementById("alt-res").textContent = `△ACD ~ △CBD  =>  CD^2 = ${ad} x ${bd} = ${(ad*bd).toFixed(2)}  =>  CD = ${cd} cm!`;
}
</script>
"""

# Simulator 16: Chapter 6 Master Cheat Sheet & Live Proportion Solver
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📘</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Chapter 6 Complete Theorem Vault & Quick BPT / Scale Solver</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Ready for Exercises!</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-mono">
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-amber-300 font-bold mb-1">1. Polygons & Shapes (6.2)</div>
            <div class="text-slate-300">All Circles, Squares & Equilateral △ ALWAYS similar. Equal angles + Proportional sides.</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-cyan-300 font-bold mb-1">2. Thales BPT & Converse (6.1-6.2)</div>
            <div class="text-slate-300">DE || BC <=> AD/DB = AE/EC (plus whole ratios AD/AB = AE/AC).</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-emerald-300 font-bold mb-1">3. Similarity Criteria (6.3-6.5)</div>
            <div class="text-slate-300">AAA / AA | SSS (all 3 ratios) | SAS (included angle!)</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-purple-300 font-bold mb-1">4. Supplementary RHS & Ratios</div>
            <div class="text-slate-300">Right △: Hypotenuse & Leg ratio (RHS). Perimeters & Medians scale by k!</div>
        </div>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2 text-xs">
        <div class="font-bold text-amber-300">Instant BPT Segment Solver (DE || BC -> Find EC = DB x AE / AD):</div>
        <div class="grid grid-cols-3 gap-2">
            <div><span class="text-slate-400">AD:</span><input type="number" step="0.1" value="1.5" id="s16-ad" oninput="calcVault16()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
            <div><span class="text-slate-400">DB:</span><input type="number" step="0.1" value="3.0" id="s16-db" oninput="calcVault16()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
            <div><span class="text-slate-400">AE:</span><input type="number" step="0.1" value="1.0" id="s16-ae" oninput="calcVault16()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
        </div>
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-emerald-300 font-mono font-bold text-center" id="s16-out">
            EC = (3.0 x 1.0) / 1.5 = 2.00 cm
        </div>
    </div>
</div>

<script>
function calcVault16() {
    const ad = Math.max(0.1, parseFloat(document.getElementById("s16-ad").value) || 1);
    const db = parseFloat(document.getElementById("s16-db").value) || 0;
    const ae = parseFloat(document.getElementById("s16-ae").value) || 0;
    const ec = (db * ae) / ad;
    document.getElementById("s16-out").textContent = `EC = (${db} x ${ae}) / ${ad} = ${ec.toFixed(2)} cm`;
}
</script>
"""
