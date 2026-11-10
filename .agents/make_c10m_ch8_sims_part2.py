#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 10 Mathematics - Chapter 8: Introduction to Trigonometry
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Interactive Table 8.1 Master Values & √n / 2 Pattern
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📊</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Table 8.1 Explorer: The √n / 2 Finger Pattern (0° to 90°)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8s9-badge">Angle: 30°</span>
    </div>

    <div class="grid grid-cols-5 gap-1.5">
        <button onclick="pickTab89(0)" id="btn-89-0" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">0°</button>
        <button onclick="pickTab89(1)" id="btn-89-1" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">30°</button>
        <button onclick="pickTab89(2)" id="btn-89-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">45°</button>
        <button onclick="pickTab89(3)" id="btn-89-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">60°</button>
        <button onclick="pickTab89(4)" id="btn-89-4" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">90°</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-3 text-xs font-mono">
        <div class="text-cyan-300 font-bold" id="c8s9-trick">Sine Pattern: √(1/4) = 1/2</div>
        <div class="grid grid-cols-3 gap-2 text-center" id="c8s9-grid"></div>
        <div class="text-slate-400 font-sans">Trend check: sin θ climbs 0 -> 1 while cos θ drops 1 -> 0! Equality sin θ = cos θ occurs ONLY at 45°.</div>
    </div>
</div>

<script>
const tab89 = [
    { deg: "0°", trick: "sin 0° = √(0/4) = 0", sin: "0", cos: "1", tan: "0", csc: "Not Defined", sec: "1", cot: "Not Defined" },
    { deg: "30°", trick: "sin 30° = √(1/4) = 1/2", sin: "1/2", cos: "√3/2", tan: "1/√3", csc: "2", sec: "2/√3", cot: "√3" },
    { deg: "45°", trick: "sin 45° = √(2/4) = 1/√2", sin: "1/√2", cos: "1/√2", tan: "1", csc: "√2", sec: "√2", cot: "1" },
    { deg: "60°", trick: "sin 60° = √(3/4) = √3/2", sin: "√3/2", cos: "1/2", tan: "√3", csc: "2/√3", sec: "2", cot: "1/√3" },
    { deg: "90°", trick: "sin 90° = √(4/4) = 1", sin: "1", cos: "0", tan: "Not Defined", csc: "1", sec: "Not Defined", cot: "0" }
];
function pickTab89(idx) {
    for (let k = 0; k < 5; k++) {
        document.getElementById("btn-89-" + k).className = (k === idx)
            ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    }
    const r = tab89[idx];
    document.getElementById("c8s9-badge").textContent = "Angle: " + r.deg;
    document.getElementById("c8s9-trick").textContent = "Pattern: " + r.trick;
    const boxes = [
        ["sin", r.sin, "text-amber-300"], ["cos", r.cos, "text-cyan-300"], ["tan", r.tan, "text-emerald-300"],
        ["cosec", r.csc, "text-amber-200"], ["sec", r.sec, "text-cyan-200"], ["cot", r.cot, "text-emerald-200"]
    ];
    document.getElementById("c8s9-grid").innerHTML = boxes.map(b =>
        `<div class="bg-slate-900 p-2 rounded-xl border border-slate-800"><div class="text-[10px] text-slate-400">${b[0]} ${r.deg}</div><div class="text-sm font-bold ${b[2]}">${b[1]}</div></div>`
    ).join("");
}
pickTab89(1);
</script>
"""

# Simulator 10: Unknown Triangle Sides (Example 6) & Simultaneous Angle System (Ex 8.2 Q3)
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📏</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Ex 8.2 Solver: Missing Triangle Sides (Ex 6) & tan(A±B) Equations</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Ex 6 & Ex 8.2 Q3</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="tab10('side')" id="btn-810-s" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Ex 6: AB=5, ∠C=30° -> BC, AC</button>
        <button onclick="tab10('ang')" id="btn-810-a" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 8.2 Q3: tan(A±B) System</button>
    </div>

    <div id="p810-side" class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Right △ABC (∠B=90°), Known: Wall AB = 5 cm and Elevation ∠C = 30°</div>
        <div class="text-cyan-300">1) Find Base BC: tan 30° = 5 / BC  =>  1/√3 = 5 / BC  =>  BC = 5√3 cm!</div>
        <div class="text-emerald-300 font-bold text-sm">2) Find Hypotenuse AC: sin 30° = 5 / AC  =>  1/2 = 5 / AC  =>  AC = 10 cm!</div>
    </div>

    <div id="p810-ang" class="hidden bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Given: tan(A + B) = √3   and   tan(A - B) = 1/√3</div>
        <div class="text-cyan-300">Table 8.1 match:  A + B = 60°   and   A - B = 30°</div>
        <div class="text-emerald-300 font-bold text-sm">Add equations: 2A = 90°  =>  A = 45°  and  B = 15°!</div>
    </div>
</div>

<script>
function tab10(t) {
    document.getElementById("p810-side").classList.toggle("hidden", t !== "side");
    document.getElementById("p810-ang").classList.toggle("hidden", t !== "ang");
    document.getElementById("btn-810-s").className = (t === "side")
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-810-a").className = (t === "ang")
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
}
</script>
"""

# Simulator 11: Primary Identity Verifier (cos^2 A + sin^2 A = 1)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔥</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Identity 1 Verifier: cos² A + sin² A = 1 (0° ≤ A ≤ 90°)</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">SUM ALWAYS = 1.000</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Test ANY angle A from 0° to 90°:</span><span class="font-bold text-amber-300" id="c8s11-deg-disp">A = 35°</span></div>
        <input type="range" min="0" max="90" step="1" value="35" id="c8s11-deg" oninput="verifyId11()" class="w-full accent-emerald-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-cyan-300" id="c8s11-vals">cos(35°) = 0.8192  |  sin(35°) = 0.5736</div>
        <div class="text-emerald-300 font-bold text-sm" id="c8s11-sum">cos²(35°) + sin²(35°) = 0.6710 + 0.3290 = 1.0000 ALWAYS!</div>
        <div class="text-slate-400 pt-1 border-t border-slate-800">Proof: Divide Pythagoras (AB² + BC² = AC²) on both sides by AC² -> (AB/AC)² + (BC/AC)² = 1!</div>
    </div>
</div>

<script>
function verifyId11() {
    const deg = parseInt(document.getElementById("c8s11-deg").value, 10);
    const rad = deg * Math.PI / 180;
    const c = Math.cos(rad), s = Math.sin(rad);
    const c2 = c * c, s2 = s * s;
    document.getElementById("c8s11-deg-disp").textContent = "A = " + deg + "°";
    document.getElementById("c8s11-vals").textContent = `cos(${deg}°) = ${c.toFixed(4)}   |   sin(${deg}°) = ${s.toFixed(4)}`;
    document.getElementById("c8s11-sum").textContent = `cos²(${deg}°) + sin²(${deg}°) = ${c2.toFixed(4)} + ${s2.toFixed(4)} = ${(c2 + s2).toFixed(4)}  (EXACT 1!)`;
}
verifyId11();
</script>
"""

# Simulator 12: Secondary Identities & Difference-of-Squares Explorer
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚙️</span>
            <h3 class="text-sm sm:text-base font-bold text-purple-300">Identities 2 & 3 Explorer: sec² − tan² = 1 & cosec² − cot² = 1</h3>
        </div>
        <span class="text-[11px] bg-purple-950/80 text-purple-300 px-2.5 py-1 rounded-full border border-purple-800" id="c8s12-badge">A = 37°</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-1 text-xs">
        <div class="flex justify-between"><span class="text-slate-300">Slide Acute Angle A (1° to 89°):</span><span class="font-bold text-purple-300" id="c8s12-d">A = 37°</span></div>
        <input type="range" min="1" max="89" step="1" value="37" id="c8s12-ang" oninput="verifyId12()" class="w-full accent-purple-400">
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300" id="c8s12-i2">1 + tan²(37°) = 1.5678  ==  sec²(37°) = 1.5678  (Valid 0° ≤ A < 90°)</div>
        <div class="text-cyan-300" id="c8s12-i3">1 + cot²(37°) = 2.7611  ==  cosec²(37°) = 2.7611  (Valid 0° < A ≤ 90°)</div>
        <div class="text-emerald-300 font-bold" id="c8s12-diff">(sec A + tan A)(sec A - tan A) = 1.0000 ALWAYS!</div>
    </div>
</div>

<script>
function verifyId12() {
    const deg = parseInt(document.getElementById("c8s12-ang").value, 10);
    const rad = deg * Math.PI / 180;
    const t = Math.tan(rad), sec = 1 / Math.cos(rad);
    const cot = 1 / t, csc = 1 / Math.sin(rad);
    document.getElementById("c8s12-badge").textContent = "A = " + deg + "°";
    document.getElementById("c8s12-d").textContent = "A = " + deg + "°";
    document.getElementById("c8s12-i2").textContent = `1 + tan²(${deg}°) = ${(1 + t*t).toFixed(4)}  ==  sec²(${deg}°) = ${(sec*sec).toFixed(4)}`;
    document.getElementById("c8s12-i3").textContent = `1 + cot²(${deg}°) = ${(1 + cot*cot).toFixed(4)}  ==  cosec²(${deg}°) = ${(csc*csc).toFixed(4)}`;
    document.getElementById("c8s12-diff").textContent = `(sec + tan)*(sec - tan) = ${((sec + t)*(sec - t)).toFixed(4)}  (EXACT 1!)`;
}
verifyId12();
</script>
"""

# Simulator 13: Expressing All Ratios in Terms of One Ratio (Example 9 & Ex 8.3 Q1)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔄</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Trig Ratio Converter: Express All Ratios in One Target (Ex 8.3 Q1-2)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800">Conversion Chain</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="showConv13('sin')" id="btn-813-sin" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500">All in terms of sin A</button>
        <button onclick="showConv13('cot')" id="btn-813-cot" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Ex 8.3 Q1: in terms of cot A</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="c8s13-l1"></div>
        <div class="text-cyan-300" id="c8s13-l2"></div>
        <div class="text-emerald-300 font-bold" id="c8s13-l3"></div>
    </div>
</div>

<script>
function showConv13(mode) {
    document.getElementById("btn-813-sin").className = (mode === "sin")
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-813-cot").className = (mode === "cot")
        ? "p-2 rounded-xl bg-amber-600 text-white font-bold text-xs border border-amber-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";

    if (mode === "sin") {
        document.getElementById("c8s13-l1").textContent = "1) cos A = sqrt(1 - sin² A)   [via cos² A + sin² A = 1]";
        document.getElementById("c8s13-l2").textContent = "2) tan A = sin A / sqrt(1 - sin² A)   |   cot A = sqrt(1 - sin² A) / sin A";
        document.getElementById("c8s13-l3").textContent = "3) sec A = 1 / sqrt(1 - sin² A)   |   cosec A = 1 / sin A";
    } else {
        document.getElementById("c8s13-l1").textContent = "1) sin A = 1 / cosec A = 1 / sqrt(1 + cot² A)";
        document.getElementById("c8s13-l2").textContent = "2) tan A = 1 / cot A";
        document.getElementById("c8s13-l3").textContent = "3) sec A = sqrt(1 + tan² A) = sqrt(cot² A + 1) / cot A!";
    }
}
showConv13("sin");
</script>
"""

# Simulator 14: Radical Conjugate & Sin/Cos Rationalization Proof Explorer (Ex 8.3 Q4 vi & Q3 ii)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧪</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Conjugate Radical Proof & Sin/Cos Converter (Ex 8.3)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Strategy I</span>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="showStrat14(0)" id="btn-814-0" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">Q4(vi): √[(1+sin)/(1-sin)]</button>
        <button onclick="showStrat14(1)" id="btn-814-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Q3(ii): (1+tan+sec)(1+cot-csc)</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold" id="c8s14-s1"></div>
        <div class="text-cyan-300" id="c8s14-s2"></div>
        <div class="text-emerald-300 font-bold text-sm" id="c8s14-s3"></div>
    </div>
</div>

<script>
function showStrat14(i) {
    document.getElementById("btn-814-0").className = (i === 0)
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    document.getElementById("btn-814-1").className = (i === 1)
        ? "p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500"
        : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";

    if (i === 0) {
        document.getElementById("c8s14-s1").textContent = "Step 1: Multiply top & bottom inside root by conjugate (1 + sin A):";
        document.getElementById("c8s14-s2").textContent = "Step 2: sqrt[ (1 + sin A)^2 / (1 - sin² A) ] = sqrt[ (1 + sin A)^2 / cos² A ] = (1 + sin A) / cos A";
        document.getElementById("c8s14-s3").textContent = "Step 3: Split fraction -> (1 / cos A) + (sin A / cos A) = sec A + tan A! Proved!";
    } else {
        document.getElementById("c8s14-s1").textContent = "Step 1: Convert to sin/cos: [(cos+sin+1)/cos] * [(sin+cos-1)/sin]";
        document.getElementById("c8s14-s2").textContent = "Step 2: [(sin + cos)² - 1] / (sin cos) = [1 + 2 sin cos - 1] / (sin cos)";
        document.getElementById("c8s14-s3").textContent = "Step 3: (2 sin cos) / (sin cos) = EXACTLY 2!";
    }
}
showStrat14(0);
</script>
"""

# Simulator 15: Difference of Squares Proof Stepper (Ex 8.3 Q4 v & Q4 x)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏆</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Board Challenge Proof Stepper: Ex 8.3 Q4(v) & Q4(x)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Strategy II</span>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="step15(1)" id="btn-815-1" class="p-2 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">Step 1: ÷ sin A</button>
        <button onclick="step15(2)" id="btn-815-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Step 2: Replace 1</button>
        <button onclick="step15(3)" id="btn-815-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Step 3: Cancel Bracket</button>
    </div>

    <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 space-y-2 text-xs font-mono">
        <div class="text-amber-300 font-bold">Target: Prove (cos A - sin A + 1) / (cos A + sin A - 1) = cosec A + cot A</div>
        <div class="text-emerald-300 font-bold text-sm" id="c8s15-msg"></div>
    </div>
</div>

<script>
function step15(s) {
    for (let k = 1; k <= 3; k++) {
        document.getElementById("btn-815-" + k).className = (k === s)
            ? "p-2 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500"
            : "p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800";
    }
    const msgs = {
        1: "Divide every term top & bottom by sin A -> [(cot A + cosec A) - 1] / [cot A + 1 - cosec A]",
        2: "Replace NUMERATOR's '1' ONLY with (cosec² A - cot² A) = (cosec A + cot A)(cosec A - cot A)!",
        3: "Factor out (cosec A + cot A): [(cosec A + cot A)(1 - cosec A + cot A)] / [cot A + 1 - cosec A] = cosec A + cot A! Proved!"
    };
    document.getElementById("c8s15-msg").textContent = msgs[s];
}
step15(1);
</script>
"""

# Simulator 16: Chapter 8 Master Formula Vault & Live Calculator
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📘</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Chapter 8 Formula Vault & Instant Angle Evaluator</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Ready for Quiz!</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs font-mono">
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-amber-300 font-bold mb-1">1. Six Ratios & Quotients</div>
            <div class="text-slate-300">sin=O/H, cos=A/H, tan=O/A | tan=sin/cos, cot=cos/sin</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-cyan-300 font-bold mb-1">2. Invariance & Bounds</div>
            <div class="text-slate-300">AA Similarity -> Scale invariant | sin A <= 1, cos A <= 1</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-emerald-300 font-bold mb-1">3. Identity 1 & Identity 2</div>
            <div class="text-slate-300">cos² A + sin² A = 1  |  1 + tan² A = sec² A</div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
            <div class="text-purple-300 font-bold mb-1">4. Identity 3 & Standard Values</div>
            <div class="text-slate-300">1 + cot² A = cosec² A | sin(0..90) = √0/2..√4/2</div>
        </div>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-2xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between"><span class="font-bold text-amber-300">Quick Angle Check θ (1° to 89°):</span><span class="font-bold text-cyan-300" id="s16-ang-disp">45°</span></div>
        <input type="range" min="1" max="89" value="45" id="s16-ang" oninput="calcVault816()" class="w-full accent-emerald-400">
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-emerald-300 font-mono font-bold text-center" id="s16-out">
            sin = 0.7071 | cos = 0.7071 | tan = 1.0000 | sin² + cos² = 1.0000
        </div>
    </div>
</div>

<script>
function calcVault816() {
    const d = parseInt(document.getElementById("s16-ang").value, 10);
    const r = d * Math.PI / 180;
    const s = Math.sin(r), c = Math.cos(r), t = Math.tan(r);
    document.getElementById("s16-ang-disp").textContent = d + "°";
    document.getElementById("s16-out").textContent = `sin = ${s.toFixed(4)} | cos = ${c.toFixed(4)} | tan = ${t.toFixed(4)} | sin²+cos² = ${(s*s + c*c).toFixed(4)}`;
}
</script>
"""
