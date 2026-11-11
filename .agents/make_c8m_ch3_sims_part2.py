#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 3: A Story of Numbers
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Idea Of Base (Custom Base-n Powers Explorer: Base 4 & Base 5)
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧱</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Custom Base-n Explorer (Base 5 &amp; Base 4 Landmarks)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c3s9-badge">43 = 133₅</span>
    </div>

    <div class="flex flex-wrap items-center justify-between gap-2 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div class="flex gap-2">
            <button onclick="setBaseS9(5)" id="c8c3s9-b5" class="px-3 py-1 rounded-lg bg-cyan-600 text-white font-bold">Base 5 (1,5,25,125)</button>
            <button onclick="setBaseS9(4)" id="c8c3s9-b4" class="px-3 py-1 rounded-lg bg-slate-800 text-slate-300 font-bold border border-slate-700">Base 4 (1,4,16,64)</button>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-slate-300">Decimal:</span>
            <input type="range" min="1" max="120" step="1" value="43" id="c8c3s9-n" oninput="updC8C3S9()" class="w-28 accent-amber-400">
            <span class="font-bold text-amber-300 font-mono" id="c8c3s9-nv">43</span>
        </div>
    </div>

    <div class="grid grid-cols-4 gap-2 text-center font-mono text-xs" id="c8c3s9-cols"></div>
    <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 font-mono text-xs text-emerald-300 font-bold text-center" id="c8c3s9-sum"></div>
</div>

<script>
let baseValS9 = 5;
function setBaseS9(b) {
    baseValS9 = b;
    document.getElementById("c8c3s9-b5").className = b === 5 ? "px-3 py-1 rounded-lg bg-cyan-600 text-white font-bold" : "px-3 py-1 rounded-lg bg-slate-800 text-slate-300 font-bold border border-slate-700";
    document.getElementById("c8c3s9-b4").className = b === 4 ? "px-3 py-1 rounded-lg bg-cyan-600 text-white font-bold" : "px-3 py-1 rounded-lg bg-slate-800 text-slate-300 font-bold border border-slate-700";
    updC8C3S9();
}
function updC8C3S9() {
    let rem = parseInt(document.getElementById("c8c3s9-n").value);
    const orig = rem;
    const weights = [Math.pow(baseValS9, 3), Math.pow(baseValS9, 2), baseValS9, 1];
    let html = "";
    let digits = [];
    let terms = [];
    for (let i = 0; i < 4; i++) {
        const w = weights[i];
        const d = Math.floor(rem / w);
        rem %= w;
        digits.push(d);
        terms.push("(" + d + "×" + w + ")");
        html += `<div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
            <div class="text-[10px] text-slate-400">${baseValS9}^${3 - i} = ${w}</div>
            <div class="text-lg font-black text-amber-300 mt-0.5">${d}</div>
        </div>`;
    }
    const compact = digits.join("").replace(/^0+/, "") || "0";
    document.getElementById("c8c3s9-nv").textContent = orig;
    document.getElementById("c8c3s9-badge").textContent = orig + " = " + compact + "_" + baseValS9;
    document.getElementById("c8c3s9-cols").innerHTML = html;
    document.getElementById("c8c3s9-sum").textContent = orig + "₁₀ = " + terms.join(" + ") + " = " + compact + " (Base " + baseValS9 + ")";
}
updC8C3S9();
</script>
"""

# Simulator 10: Base System Advantages (Exponent Product Landmarks & Decimal Abacus Board)
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧮</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">11th-Century Decimal Abacus &amp; Landmark Exponent Law</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c3s10-badge">Total: 258</span>
    </div>

    <div class="grid grid-cols-3 gap-2 text-center font-mono text-xs bg-slate-900/90 p-3 rounded-xl border border-slate-800">
        <div class="p-2 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
            <div class="text-amber-300 font-bold">10² (100s Line)</div>
            <div class="text-base text-cyan-300 font-black" id="c8c3s10-h">●● (2)</div>
            <button onclick="addBeadS10(100)" class="w-full py-1 rounded bg-cyan-700 hover:bg-cyan-600 text-white font-bold">+100</button>
        </div>
        <div class="p-2 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
            <div class="text-amber-300 font-bold">10¹ (10s Line)</div>
            <div class="text-base text-amber-300 font-black" id="c8c3s10-t">●●●●● (5)</div>
            <button onclick="addBeadS10(10)" class="w-full py-1 rounded bg-amber-600 hover:bg-amber-500 text-white font-bold">+10 (Carry @10)</button>
        </div>
        <div class="p-2 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
            <div class="text-amber-300 font-bold">10⁰ (1s Line)</div>
            <div class="text-base text-emerald-300 font-black" id="c8c3s10-u">●●●●●●●● (8)</div>
            <button onclick="addBeadS10(1)" class="w-full py-1 rounded bg-emerald-600 hover:bg-emerald-500 text-white font-bold">+1 (Carry @10)</button>
        </div>
    </div>

    <div class="flex items-center justify-between gap-2 bg-slate-950 p-2.5 rounded-xl border border-slate-800 font-mono text-xs">
        <span class="text-cyan-200 font-bold">Landmark Product Law: nᵃ × nᵇ = nᵃ⁺ᵇ (e.g. 5¹ × 5² = 5³ = 125)</span>
        <button onclick="resetAbacusS10()" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200 font-bold border border-slate-700">Reset (258)</button>
    </div>
</div>

<script>
let abValS10 = 258;
function renderAbacusS10() {
    const h = Math.floor(abValS10 / 100);
    const t = Math.floor((abValS10 % 100) / 10);
    const u = abValS10 % 10;
    document.getElementById("c8c3s10-h").textContent = ("●".repeat(h) || "—") + " (" + h + ")";
    document.getElementById("c8c3s10-t").textContent = ("●".repeat(t) || "—") + " (" + t + ")";
    document.getElementById("c8c3s10-u").textContent = ("●".repeat(u) || "—") + " (" + u + ")";
    document.getElementById("c8c3s10-badge").textContent = "Total: " + abValS10;
}
function addBeadS10(delta) {
    abValS10 = (abValS10 + delta) % 1000;
    renderAbacusS10();
}
function resetAbacusS10() {
    abValS10 = 258;
    renderAbacusS10();
}
renderAbacusS10();
</script>
"""

# Simulator 11: Egyptian System Limits (Symbol Repetition Bloat vs Positional Place Value)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚠️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Why Egyptian Numerals Fail: Symbol Repetition vs Place Value</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c8c3s11-badge">999 → 27 Glyphs</span>
    </div>

    <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <button onclick="setLimitS11(0)" class="px-2.5 py-1 rounded-lg bg-amber-700 text-white font-bold">Compare 999</button>
        <button onclick="setLimitS11(1)" class="px-2.5 py-1 rounded-lg bg-rose-700 text-white font-bold">Compare 9,99,999</button>
        <button onclick="setLimitS11(2)" class="px-2.5 py-1 rounded-lg bg-indigo-700 text-white font-bold">Try 10²³ (Cosmic Wall!)</button>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-2xl border border-slate-800 font-mono text-xs">
        <div class="p-3 bg-slate-950 rounded-xl border border-rose-700/60 space-y-1">
            <div class="text-rose-400 font-bold">Egyptian Additive System</div>
            <div class="text-rose-200 font-bold" id="c8c3s11-egy"></div>
        </div>
        <div class="p-3 bg-slate-950 rounded-xl border border-emerald-700/60 space-y-1">
            <div class="text-emerald-400 font-bold">Hindu Positional Place Value</div>
            <div class="text-emerald-200 font-bold" id="c8c3s11-hin"></div>
        </div>
    </div>
</div>

<script>
const limitCases = [
    { b: "999 → 27 Glyphs", e: "9 Coils + 9 Heels + 9 Staffs = 27 drawn symbols!", h: "999 = just 3 digits reusing ONE symbol '9' across 3 places!" },
    { b: "9,99,999 → 54 Glyphs", e: "9 Frogs + 9 Fingers + 9 Lotuses + 9 Coils + 9 Heels + 9 Staffs = 54 glyphs!", h: "9,99,999 = compact 6-digit string with ZERO symbol explosion!" },
    { b: "10²³ → Symbol Overflow!", e: "IMPOSSIBLE without inventing 17 brand-new symbols past Astonished Man (10⁶)!", h: "100,000,000,000,000,000,000,000 uses ONLY digits '1' and '0'!" }
];
function setLimitS11(i) {
    document.getElementById("c8c3s11-badge").textContent = limitCases[i].b;
    document.getElementById("c8c3s11-egy").textContent = limitCases[i].e;
    document.getElementById("c8c3s11-hin").textContent = limitCases[i].h;
}
setLimitS11(0);
</script>
"""

# Simulator 12: Mesopotamian Base Sixty (Sexagesimal Wedge Builder: Y=1, <=10)
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏺</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Mesopotamian Base-60 Clay Tablet (&lt; = 10, Y = 1)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c3s12-badge">1,392 = [23, 12]₆₀</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">60¹ Column (Sixties):</span><span class="font-bold text-amber-300" id="c8c3s12-av">23</span></div>
            <input type="range" min="0" max="59" step="1" value="23" id="c8c3s12-a" oninput="updC8C3S12()" class="w-full accent-amber-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">60⁰ Column (Units):</span><span class="font-bold text-cyan-300" id="c8c3s12-bv">12</span></div>
            <input type="range" min="0" max="59" step="1" value="12" id="c8c3s12-b" oninput="updC8C3S12()" class="w-full accent-cyan-400">
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-sm font-black text-amber-200 tracking-wider" id="c8c3s12-wedges"></div>
        <div class="text-emerald-300 font-bold" id="c8c3s12-val"></div>
    </div>
</div>

<script>
function wedgeStr(v) {
    if (v === 0) return "[blank / ⑊ spacer]";
    const tens = Math.floor(v / 10);
    const ones = v % 10;
    return "<".repeat(tens) + (tens && ones ? " " : "") + "Y".repeat(ones);
}
function updC8C3S12() {
    const a = parseInt(document.getElementById("c8c3s12-a").value);
    const b = parseInt(document.getElementById("c8c3s12-b").value);
    const total = a * 60 + b;
    document.getElementById("c8c3s12-av").textContent = a;
    document.getElementById("c8c3s12-bv").textContent = b;
    document.getElementById("c8c3s12-badge").textContent = total.toLocaleString("en-IN") + " = [" + a + ", " + b + "]₆₀";
    document.getElementById("c8c3s12-wedges").textContent = "60¹: [ " + wedgeStr(a) + " ]   |   60⁰: [ " + wedgeStr(b) + " ]";
    document.getElementById("c8c3s12-val").textContent = "Decimal Value: (" + a + " × 60) + (" + b + " × 1) = " + total.toLocaleString("en-IN");
}
updC8C3S12();
</script>
"""

# Simulator 13: Mayan Vertical Scale (Dots=1, Bars=5, Seashell=0 on 1, 20, 360)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🐚</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Mayan Vertical Stela Decoder (Scale: 360, 20, 1)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c3s13-badge">728</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Decimal Number (0 to 1,800):</span>
            <span class="font-bold text-cyan-300 font-mono" id="c8c3s13-nv">728</span>
        </div>
        <input type="range" min="0" max="1800" step="1" value="728" id="c8c3s13-n" oninput="updC8C3S13()" class="w-full accent-cyan-400">
    </div>

    <div class="grid grid-cols-3 gap-2 text-center font-mono text-xs" id="c8c3s13-tiers"></div>
    <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 font-mono text-xs text-amber-300 font-bold text-center" id="c8c3s13-sum"></div>
</div>

<script>
function mayanGlyph(v) {
    if (v === 0) return "🐚 (Seashell 0)";
    const bars = Math.floor(v / 5);
    const dots = v % 5;
    return ("●".repeat(dots) || "") + (dots && bars ? " / " : "") + ("▬".repeat(bars) || "") + " (" + v + ")";
}
function updC8C3S13() {
    let rem = parseInt(document.getElementById("c8c3s13-n").value);
    const orig = rem;
    const t360 = Math.floor(rem / 360);
    rem %= 360;
    const t20 = Math.floor(rem / 20);
    const t1 = rem % 20;

    document.getElementById("c8c3s13-nv").textContent = orig;
    document.getElementById("c8c3s13-badge").textContent = orig;
    document.getElementById("c8c3s13-tiers").innerHTML = `
        <div class="p-2 rounded-xl bg-slate-900 border border-slate-800"><div class="text-[10px] text-slate-400">Top (×360)</div><div class="font-bold text-amber-300 mt-1">${mayanGlyph(t360)}</div></div>
        <div class="p-2 rounded-xl bg-slate-900 border border-slate-800"><div class="text-[10px] text-slate-400">Mid (×20)</div><div class="font-bold text-cyan-300 mt-1">${mayanGlyph(t20)}</div></div>
        <div class="p-2 rounded-xl bg-slate-900 border border-slate-800"><div class="text-[10px] text-slate-400">Bottom (×1)</div><div class="font-bold text-emerald-300 mt-1">${mayanGlyph(t1)}</div></div>
    `;
    document.getElementById("c8c3s13-sum").textContent = "Vertical Sum: (" + t360 + "×360) + (" + t20 + "×20) + (" + t1 + "×1) = " + orig;
}
updC8C3S13();
</script>
"""

# Simulator 14: Chinese Rod Numerals (Alternating Zong Vertical & Heng Horizontal Rods)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🥢</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Chinese Alternating Zong / Heng Counting Rods</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c8c3s14-badge">4,083</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Encode Number (1 to 9,999):</span>
            <span class="font-bold text-rose-300 font-mono" id="c8c3s14-nv">4,083</span>
        </div>
        <input type="range" min="1" max="9999" step="1" value="4083" id="c8c3s14-n" oninput="updC8C3S14()" class="w-full accent-rose-400">
    </div>

    <div class="grid grid-cols-4 gap-2 text-center font-mono text-xs" id="c8c3s14-grid"></div>
    <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 font-mono text-xs text-cyan-300 text-center">
        Rule: Units (10⁰) &amp; Hundreds (10²) use Vertical (Zong); Tens (10¹) &amp; Thousands (10³) use Horizontal (Heng)!
    </div>
</div>

<script>
function rodGlyph(d, isZong) {
    if (d === 0) return "[blank]";
    const bar5 = Math.floor(d / 5);
    const units = d % 5;
    if (isZong) return (bar5 ? "― + " : "") + "|".repeat(units || 0);
    return (bar5 ? "| + " : "") + "―".repeat(units || 0);
}
function updC8C3S14() {
    const n = parseInt(document.getElementById("c8c3s14-n").value);
    const s = String(n).padStart(4, "0");
    const labels = ["10³ (Heng)", "10² (Zong)", "10¹ (Heng)", "10⁰ (Zong)"];
    const zongs = [false, true, false, true];
    let html = "";
    for (let i = 0; i < 4; i++) {
        const d = parseInt(s[i]);
        html += `<div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
            <div class="text-[10px] text-slate-400">${labels[i]}</div>
            <div class="text-sm font-black text-amber-300 mt-1">${rodGlyph(d, zongs[i])}</div>
            <div class="text-[10px] text-emerald-300">digit ${d}</div>
        </div>`;
    }
    document.getElementById("c8c3s14-nv").textContent = n.toLocaleString("en-IN");
    document.getElementById("c8c3s14-badge").textContent = n.toLocaleString("en-IN");
    document.getElementById("c8c3s14-grid").innerHTML = html;
}
updC8C3S14();
</script>
"""

# Simulator 15: Hindu Decimal Zero (Placeholder Role vs Full Number Rules of Brahmagupta)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌞</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Hindu Place-Value Zero: Aryabhata (499 CE) &amp; Brahmagupta (628 CE)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c3s15-badge">502 ≠ 52</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-2xl border border-slate-800 font-mono text-xs">
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-2">
            <div class="text-amber-300 font-bold">Role 1: Zero as Positional Placeholder</div>
            <div class="flex items-center justify-between bg-slate-900 p-2 rounded-lg">
                <span>Toggle Tens Zero:</span>
                <button onclick="toggleZeroS15()" id="c8c3s15-btn" class="px-3 py-1 rounded bg-emerald-600 text-white font-bold">502 (With 0)</button>
            </div>
            <div class="text-cyan-300 font-bold" id="c8c3s15-place"></div>
        </div>
        <div class="p-3 bg-slate-950 rounded-xl border border-emerald-700/50 space-y-1.5">
            <div class="text-emerald-300 font-bold">Role 2: Zero as a Full Number (628 CE)</div>
            <div class="text-slate-300">Pick integer a = <span class="text-amber-300 font-bold" id="c8c3s15-av">7</span>:
                <input type="range" min="1" max="15" value="7" id="c8c3s15-a" oninput="updZeroLawS15()" class="w-24 align-middle accent-emerald-400">
            </div>
            <div class="text-cyan-200 font-bold" id="c8c3s15-laws"></div>
        </div>
    </div>
</div>

<script>
let withZeroS15 = false;
function toggleZeroS15() {
    withZeroS15 = !withZeroS15;
    const btn = document.getElementById("c8c3s15-btn");
    btn.textContent = withZeroS15 ? "502 (With 0)" : "52 (Without 0)";
    document.getElementById("c8c3s15-badge").textContent = withZeroS15 ? "502 ≠ 52" : "52 = 5×10 + 2";
    document.getElementById("c8c3s15-place").textContent = withZeroS15
        ? "5×10² + 0×10¹ + 2×10⁰ = 502 (Unambiguous!)"
        : "5×10¹ + 2×10⁰ = 52 (Shifted 10× smaller!)";
}
function updZeroLawS15() {
    const a = parseInt(document.getElementById("c8c3s15-a").value);
    document.getElementById("c8c3s15-av").textContent = a;
    document.getElementById("c8c3s15-laws").textContent = a + " + 0 = " + a + "  |  " + a + " − 0 = " + a + "  |  " + a + " × 0 = 0";
}
toggleZeroS15();
updZeroLawS15();
</script>
"""

# Simulator 16: Chapter Three Summary (Base 10 -> Base 2, Base 5, Base 8 Converter)
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">💻</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">Universal Multi-Base Converter (Base-10 → Base-2, Base-5, Base-8)</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c3s16-badge">29₁₀</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Slide Decimal Number (1 to 150):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c3s16-nv">29</span>
        </div>
        <input type="range" min="1" max="150" step="1" value="29" id="c8c3s16-n" oninput="updC8C3S16()" class="w-full accent-indigo-400">
    </div>

    <div class="grid grid-cols-3 gap-2 text-center font-mono text-xs">
        <div class="p-3 rounded-xl bg-slate-950 border border-cyan-700/60">
            <div class="text-[10px] text-cyan-400 font-bold">Base-2 (Binary)</div>
            <div class="text-base font-black text-cyan-200 mt-1" id="c8c3s16-b2"></div>
        </div>
        <div class="p-3 rounded-xl bg-slate-950 border border-emerald-700/60">
            <div class="text-[10px] text-emerald-400 font-bold">Base-5 (Quinary)</div>
            <div class="text-base font-black text-emerald-200 mt-1" id="c8c3s16-b5"></div>
        </div>
        <div class="p-3 rounded-xl bg-slate-950 border border-amber-700/60">
            <div class="text-[10px] text-amber-400 font-bold">Base-8 (8 Fingers!)</div>
            <div class="text-base font-black text-amber-200 mt-1" id="c8c3s16-b8"></div>
        </div>
    </div>
</div>

<script>
function updC8C3S16() {
    const n = parseInt(document.getElementById("c8c3s16-n").value);
    document.getElementById("c8c3s16-nv").textContent = n;
    document.getElementById("c8c3s16-badge").textContent = n + "₁₀";
    document.getElementById("c8c3s16-b2").textContent = n.toString(2) + "₂";
    document.getElementById("c8c3s16-b5").textContent = n.toString(5) + "₅";
    document.getElementById("c8c3s16-b8").textContent = n.toString(8) + "₈";
}
updC8C3S16();
</script>
"""

if __name__ == "__main__":
    print(f"Prepared {len(simulators_part2)} interactive simulators (Part 2).")
