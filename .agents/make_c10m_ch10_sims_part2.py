#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 10: Circles
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Example 3 Tangent-Chord Triangle (TP = 20/3 cm)
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📐</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Example 3 Solver: Radius 5, Chord 8 -> Tangent TP = 20/3 cm</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">AA Similarity: △TRP ~ △TPO</span>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 130" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <circle cx="65" cy="65" r="42" fill="rgba(56,189,248,0.12)" stroke="#38bdf8" stroke-width="2" />
            <line x1="88" y1="30" x2="88" y2="100" stroke="#fbbf24" stroke-width="2.5" />
            <line x1="88" y1="30" x2="195" y2="65" stroke="#34d399" stroke-width="2" />
            <line x1="88" y1="100" x2="195" y2="65" stroke="#34d399" stroke-width="2" />
            <line x1="65" y1="65" x2="195" y2="65" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3,2" />
            <line x1="65" y1="65" x2="88" y2="30" stroke="#f43f5e" stroke-width="1.5" />
            <text x="54" y="68" fill="#fff" font-size="9">O</text>
            <text x="93" y="61" fill="#fcd34d" font-size="9">R</text>
            <text x="88" y="22" fill="#6ee7b7" font-size="9">P</text>
            <text x="200" y="68" fill="#6ee7b7" font-size="9">T</text>
            <text x="64" y="47" fill="#fda4af" font-size="8.5">5</text>
        </svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
            <div class="text-cyan-300">1) OT bisects chord PQ=8 -> PR = 4 cm</div>
            <div class="text-amber-300">2) Inner right △ORP: OR = sqrt(5² - 4²) = 3 cm</div>
            <div class="text-emerald-300 font-bold text-sm">3) △TRP ~ △TPO: TP / 5 = 4 / 3  =>  TP = 20/3 cm!</div>
        </div>
    </div>
</div>
"""

# Simulator 10: Kite Quadrilateral Supplementary Angles (∠AOB + ∠APB = 180°)
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪁</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Kite Angle Shortcut: ∠AOB + ∠APB = 180° (Ex 10.2 Q2, Q3, Q10)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c10s10-badge">∠POA = 50°</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Adjust External Angle Between Tangents ∠APB (Ex Q3 = 80°):</span><span class="font-bold text-amber-300" id="c10s10-d">∠APB = 80°</span></div>
        <input type="range" min="20" max="160" step="10" value="80" id="c10s10-ang" oninput="calcKite10()" class="w-full accent-cyan-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c10s10-aob">Central Angle ∠AOB = 180° - 80° = 100°</div>
        <div class="text-emerald-300 font-bold text-sm" id="c10s10-poa">Half Central Angle ∠POA = 100° / 2 = 50°!  [∠A + ∠B = 180°]</div>
    </div>
</div>

<script>
function calcKite10() {
    const apb = parseInt(document.getElementById("c10s10-ang").value, 10);
    const aob = 180 - apb;
    const poa = aob / 2;
    document.getElementById("c10s10-d").textContent = "∠APB = " + apb + "°";
    document.getElementById("c10s10-badge").textContent = "∠POA = " + poa + "°";
    document.getElementById("c10s10-aob").textContent = `Opposite Kite Angles Supplementary: Central ∠AOB = 180° - ${apb}° = ${aob}°`;
    document.getElementById("c10s10-poa").textContent = `Because OP bisects ∠AOB: ∠POA = ${aob}° / 2 = ${poa}°!`;
}
calcKite10();
</script>
"""

# Simulator 11: Parallel Diameter Endpoint Tangents (Ex 10.2 Q4 & Q5)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📏</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Diameter Endpoint Parallel Tangents & Center Normal Proof (Q4-5)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">PQ ∥ RS</span>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-2xl border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 220 130" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <circle cx="110" cy="65" r="38" fill="rgba(56,189,248,0.12)" stroke="#38bdf8" stroke-width="2" />
            <line x1="110" y1="27" x2="110" y2="103" stroke="#fbbf24" stroke-width="2" />
            <line x1="35" y1="27" x2="185" y2="27" stroke="#34d399" stroke-width="2.5" />
            <line x1="35" y1="103" x2="185" y2="103" stroke="#34d399" stroke-width="2.5" />
            <text x="115" y="68" fill="#fff" font-size="9">O</text>
            <text x="116" y="22" fill="#6ee7b7" font-size="9">P — 90° — Q (Top Tangent A)</text>
            <text x="116" y="116" fill="#6ee7b7" font-size="9">R — 90° — S (Bottom B)</text>
        </svg>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2 text-xs font-mono">
            <div class="text-amber-300 font-bold">Q4: Diameter AB connects endpoints A & B through center O:</div>
            <div class="text-cyan-300">Theorem 10.1 makes ∠PAB = 90° and ∠ABS = 90°.</div>
            <div class="text-emerald-300 font-bold">Equal Alternate Interior Z-Angles -> PQ || RS! Proved!</div>
        </div>
    </div>
</div>
"""

# Simulator 12: Circumscribed Quadrilateral AB + CD = AD + BC Calculator (Ex 10.2 Q8)
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🟪</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Circumscribed Quadrilateral Law: AB + CD = AD + BC (Ex 10.2 Q8)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c10s12-badge">AD = 3 cm</span>
    </div>

    <div class="grid grid-cols-3 gap-2 text-xs">
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800"><span class="text-slate-400">AB (cm):</span><input type="number" value="6" id="c10q8-ab" oninput="calcQ8()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800"><span class="text-slate-400">BC (cm):</span><input type="number" value="7" id="c10q8-bc" oninput="calcQ8()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
        <div class="bg-slate-900 p-2 rounded-xl border border-slate-800"><span class="text-slate-400">CD (cm):</span><input type="number" value="4" id="c10q8-cd" oninput="calcQ8()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300">AP = AS,  BP = BQ,  CR = CQ,  DR = DS  =>  Add vertically!</div>
        <div class="text-emerald-300 font-bold text-sm" id="c10s12-res">AB (6) + CD (4) = AD + BC (7)  =>  AD = 10 - 7 = 3 cm!</div>
    </div>
</div>

<script>
function calcQ8() {
    const ab = parseFloat(document.getElementById("c10q8-ab").value) || 0;
    const bc = parseFloat(document.getElementById("c10q8-bc").value) || 0;
    const cd = parseFloat(document.getElementById("c10q8-cd").value) || 0;
    const ad = ab + cd - bc;
    document.getElementById("c10s12-badge").textContent = `AD = ${ad} cm`;
    document.getElementById("c10s12-res").textContent = `AB (${ab}) + CD (${cd}) = AD + BC (${bc})  =>  AD = ${ab + cd} - ${bc} = ${ad} cm!`;
}
calcQ8();
</script>
"""

# Simulator 13: Circumscribed Parallelogram -> Rhombus (Q11) & Parallel Cuts ∠AOB = 90° (Q9)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">♦️</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Ex 10.2 Proofs: Parallelogram = Rhombus (Q11) & ∠AOB = 90° (Q9)</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800">Q11 & Q9</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="tab13('q11')" id="btn-1013-11" class="p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500">Q11: Parallelogram -> Rhombus</button>
        <button onclick="tab13('q9')" id="btn-1013-9" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Q9: Parallel Cut ∠AOB = 90°</button>
    </div>

    <div id="p1013-q11" class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Given: Parallelogram ABCD circumscribes a circle.</div>
        <div class="text-cyan-300">1) Parallelogram opposite sides: AB = CD  and  AD = BC.</div>
        <div class="text-cyan-300">2) Circumscribed Law (Q8): AB + CD = AD + BC  =>  2 AB = 2 AD  =>  AB = AD!</div>
        <div class="text-emerald-300 font-bold">All 4 edges AB = BC = CD = DA equal  =>  ABCD is a RHOMBUS! Proved!</div>
    </div>

    <div id="p1013-q9" class="hidden bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Given: Parallel tangents XY (P) & X'Y' (Q) cut by tangent AB (C):</div>
        <div class="text-cyan-300">1) OA bisects ∠PAC and OB bisects ∠QBC (Theorem 10.2 / RHS).</div>
        <div class="text-cyan-300">2) Co-interior ∠PAC + ∠QBC = 180°  =>  ∠OAB + ∠OBA = 90°.</div>
        <div class="text-emerald-300 font-bold">In △AOB: ∠AOB = 180° - 90° = 90°! Proved!</div>
    </div>
</div>

<script>
function tab13(t) {
    document.getElementById("p1013-q11").classList.toggle("hidden", t !== "q11");
    document.getElementById("p1013-q9").classList.toggle("hidden", t !== "q9");
    document.getElementById("btn-1013-11").className = (t === "q11")
        ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-1013-9").className = (t === "q9")
        ? "p-2 rounded-xl bg-purple-600 text-white font-bold text-xs border border-purple-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
}
</script>
"""

# Simulator 14: Supplementary Central Angles Proof (Ex 10.2 Q13)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🕒</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Ex 10.2 Q13: Opposite Sides Subtend Supplementary Central Angles</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c10s14-badge">115° + 65° = 180°</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Adjust Central Angle ∠AOB Subtended by Side AB:</span><span class="font-bold text-amber-300" id="c10s14-d">∠AOB = 115°</span></div>
        <input type="range" min="40" max="140" step="5" value="115" id="c10s14-aob" oninput="calcQ13()" class="w-full accent-cyan-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300">8 Vertex Sectors Pair Around Center O: ∠1=∠8, ∠2=∠3, ∠4=∠5, ∠6=∠7</div>
        <div class="text-emerald-300 font-bold text-sm" id="c10s14-res">2(∠1+∠2+∠5+∠6) = 360°  =>  ∠AOB (115°) + Opposite ∠COD (65°) = 180°!</div>
    </div>
</div>

<script>
function calcQ13() {
    const aob = parseInt(document.getElementById("c10s14-aob").value, 10);
    const cod = 180 - aob;
    document.getElementById("c10s14-d").textContent = "∠AOB = " + aob + "°";
    document.getElementById("c10s14-badge").textContent = `${aob}° + ${cod}° = 180°`;
    document.getElementById("c10s14-res").textContent = `2(∠AOB + ∠COD) = 360°  =>  ∠AOB (${aob}°) + ∠COD (${cod}°) = 180°!`;
}
calcQ13();
</script>
"""

# Simulator 15: Flagship Inscribed Circle Triangle (Ex 10.2 Q12: BD=8, DC=6, r=4 -> x=7 -> 13, 15)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏆</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Ex 10.2 Q12 Flagship: Heron Area == s·r Solver (r=4, BD=8, DC=6)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c10s15-badge">x = 7 => AB=15, AC=13</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Test Unknown Top Tangent Length x = AF = AE (Match Area²!):</span><span class="font-bold text-amber-300" id="c10s15-x-d">x = 7 cm</span></div>
        <input type="range" min="3" max="12" step="1" value="7" id="c10s15-x" oninput="testQ12()" class="w-full accent-rose-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c10s15-sides">Sides: BC = 14 cm  |  AB = x + 8 = 15 cm  |  AC = x + 6 = 13 cm</div>
        <div class="text-amber-300" id="c10s15-area">Heron Area = sqrt(48 * 7 * 21) = 84.00 cm²   |   Sub-triangles s*r = 21 * 4 = 84.00 cm²</div>
        <div class="font-bold text-sm" id="c10s15-ver">EXACT MATCH AT x = 7 cm! Thus AB = 15 cm and AC = 13 cm!</div>
    </div>
</div>

<script>
function testQ12() {
    const x = parseInt(document.getElementById("c10s15-x").value, 10);
    const ab = x + 8, ac = x + 6, s = x + 14;
    const heron = Math.sqrt(48 * x * s);
    const sr = 4 * s;
    document.getElementById("c10s15-x-d").textContent = "x = " + x + " cm";
    document.getElementById("c10s15-sides").textContent = `Sides: BC = 14 cm  |  AB = ${ab} cm  |  AC = ${ac} cm  (s = ${s})`;
    document.getElementById("c10s15-area").textContent = `Heron Area = ${heron.toFixed(2)} cm²   |   Three-Subtriangle s*r = ${sr.toFixed(2)} cm²`;
    const v = document.getElementById("c10s15-ver");
    if (x === 7) {
        v.textContent = "EXACT EQUALITY (84 == 84) AT x = 7 cm! AB = 15 cm and AC = 13 cm!";
        v.className = "font-bold text-sm text-emerald-300";
    } else {
        v.textContent = `Mismatch (${heron.toFixed(1)} vs ${sr.toFixed(1)}) — Slide to x = 7 cm!`;
        v.className = "font-bold text-sm text-rose-400";
    }
}
testQ12();
</script>
"""

# Simulator 16: Chapter 10 Master Formula Vault & Right-Triangle Inradius Solver
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📘</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Chapter 10 Theorem Vault & Quick Right-Triangle Inradius Solver</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Ready for Quiz!</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-mono">
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-amber-300 font-bold mb-1">1. Theorem 10.1 & Normal</div>
            <div class="text-slate-300">Tangent ⊥ Radius OP at contact point P (PQ = √(OQ² - r²)).</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-cyan-300 font-bold mb-1">2. Theorem 10.2 & Kite</div>
            <div class="text-slate-300">PQ = PR | ∠AOB + ∠APB = 180° | ∠PTQ = 2 ∠OPQ.</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-emerald-300 font-bold mb-1">3. Concentric & Parallel</div>
            <div class="text-slate-300">Chord = 2√(R² - r²) | Max 2 parallel tangents.</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-purple-300 font-bold mb-1">4. Inscribed Polygons</div>
            <div class="text-slate-300">AB + CD = AD + BC | Right △ Inradius r = (a + b - c) / 2.</div>
        </div>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2 text-xs">
        <div class="font-bold text-amber-300">Quick Right Triangle Inradius (r = (a + b - c) / 2):</div>
        <div class="grid grid-cols-2 gap-2">
            <div><span class="text-slate-400">Leg a:</span><input type="number" min="1" value="6" id="s16-a" oninput="calcVault1016()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
            <div><span class="text-slate-400">Leg b:</span><input type="number" min="1" value="8" id="s16-b" oninput="calcVault1016()" class="w-full bg-slate-950 text-white p-1.5 rounded border border-slate-700 font-mono"></div>
        </div>
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-emerald-300 font-mono font-bold text-center" id="s16-out">
            Hypotenuse c = 10.00   |   Inradius r = (6 + 8 - 10) / 2 = 2.00 cm
        </div>
    </div>
</div>

<script>
function calcVault1016() {
    const a = Math.max(1, parseFloat(document.getElementById("s16-a").value) || 6);
    const b = Math.max(1, parseFloat(document.getElementById("s16-b").value) || 8);
    const c = Math.sqrt(a*a + b*b);
    const r = (a + b - c) / 2;
    document.getElementById("s16-out").textContent = `Hypotenuse c = ${c.toFixed(2)}   |   Inradius r = (${a} + ${b} - ${c.toFixed(2)}) / 2 = ${r.toFixed(2)} cm`;
}
</script>
"""
