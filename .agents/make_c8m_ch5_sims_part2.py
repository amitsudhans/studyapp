#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 8 Mathematics - Chapter 5: Number Play
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Divisibility By Nine (Remainder-1 Powers Decomposition)
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">9️⃣</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Algebraic Divisibility-by-9 Proof (10ⁿ = 99...9 + 1)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c5s9-badge">N = 4,788</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Test Any 4-Digit Number (1,000 to 9,999):</span>
            <span class="font-bold text-amber-300 font-mono" id="c8c5s9-nv">4,788</span>
        </div>
        <input type="range" min="1000" max="9999" step="1" value="4788" id="c8c5s9-n" oninput="updC8C5S9()" class="w-full accent-amber-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-cyan-200" id="c8c5s9-decomp"></div>
        <div class="font-bold text-sm" id="c8c5s9-res"></div>
    </div>
</div>

<script>
function updC8C5S9() {
    const N = parseInt(document.getElementById("c8c5s9-n").value);
    const digits = String(N).split("").map(Number);
    const dsum = digits.reduce((a, b) => a + b, 0);
    const rem = N % 9;
    document.getElementById("c8c5s9-nv").textContent = N.toLocaleString("en-IN");
    document.getElementById("c8c5s9-badge").textContent = "N = " + N.toLocaleString("en-IN");
    document.getElementById("c8c5s9-decomp").textContent = N + " = (999×" + digits[0] + " + 99×" + digits[1] + " + 9×" + digits[2] + ") + (" + digits.join(" + ") + ")";
    const el = document.getElementById("c8c5s9-res");
    el.className = "font-bold text-sm " + (rem === 0 ? "text-emerald-300" : "text-amber-300");
    el.textContent = "Digit Sum = " + dsum + " → Exact Remainder mod 9 = " + rem + (rem === 0 ? " (DIVISIBLE BY 9 ✓)" : " (Not divisible by 9 ✗)");
}
updC8C5S9();
</script>
"""

# Simulator 10: Divisibility By Three (3 vs 9 Subset Venn Explorer)
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">3️⃣</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Multiples of 9 vs Multiples of 3 Scanner (52x64)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c5s10-badge">x = 1</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Pick Missing Digit x (0 to 9) inside 52x64:</span>
            <span class="font-bold text-cyan-300 font-mono" id="c8c5s10-xv">x = 1 (52,164)</span>
        </div>
        <input type="range" min="0" max="9" step="1" value="1" id="c8c5s10-x" oninput="updC8C5S10()" class="w-full accent-cyan-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-amber-300 font-bold" id="c8c5s10-sum"></div>
        <div class="font-bold text-sm" id="c8c5s10-venn"></div>
    </div>
</div>

<script>
function updC8C5S10() {
    const x = parseInt(document.getElementById("c8c5s10-x").value);
    const num = 52064 + x * 100;
    const sum = 17 + x;
    const d3 = sum % 3 === 0, d9 = sum % 9 === 0;
    document.getElementById("c8c5s10-xv").textContent = "x = " + x + " (" + num.toLocaleString("en-IN") + ")";
    document.getElementById("c8c5s10-badge").textContent = "Sum = " + sum;
    document.getElementById("c8c5s10-sum").textContent = "Digit Sum = 5 + 2 + " + x + " + 6 + 4 = " + sum;
    const el = document.getElementById("c8c5s10-venn");
    if (d9) { el.className = "font-bold text-sm text-emerald-300"; el.textContent = "Divisible by BOTH 9 AND 3! (Lives inside inner M₉ ⊂ M₃)"; }
    else if (d3) { el.className = "font-bold text-sm text-cyan-300"; el.textContent = "Divisible by 3 ONLY, NOT by 9! (Lives inside M₃ \\ M₉)"; }
    else { el.className = "font-bold text-sm text-rose-300"; el.textContent = "Divisible by NEITHER 3 nor 9 (rem mod 3 = " + (sum % 3) + ")"; }
}
updC8C5S10();
</script>
"""

# Simulator 11: Divisibility By Eleven (Alternating +1 / -1 Power Weights)
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚖️</span>
            <h3 class="text-sm sm:text-base font-bold text-indigo-300">Divisibility-by-11 Alternating (+1 / −1) Digit Balance</h3>
        </div>
        <span class="text-[11px] bg-indigo-950/80 text-indigo-300 px-2.5 py-1 rounded-full border border-indigo-800" id="c8c5s11-badge">6y53</span>
    </div>

    <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
        <div class="flex justify-between">
            <span class="text-slate-300">Pick Hundreds Digit y (0 to 9) in 6y53:</span>
            <span class="font-bold text-indigo-300 font-mono" id="c8c5s11-yv">y = 8 (6,853)</span>
        </div>
        <input type="range" min="0" max="9" step="1" value="8" id="c8c5s11-y" oninput="updC8C5S11()" class="w-full accent-indigo-400">
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-cyan-200" id="c8c5s11-alt"></div>
        <div class="font-bold text-sm" id="c8c5s11-res"></div>
    </div>
</div>

<script>
function updC8C5S11() {
    const y = parseInt(document.getElementById("c8c5s11-y").value);
    const num = 6053 + y * 100;
    const oddSum = 3 + y;
    const evenSum = 5 + 6;
    const diff = oddSum - evenSum;
    const ok = diff % 11 === 0;
    document.getElementById("c8c5s11-yv").textContent = "y = " + y + " (" + num.toLocaleString("en-IN") + ")";
    document.getElementById("c8c5s11-badge").textContent = num.toLocaleString("en-IN");
    document.getElementById("c8c5s11-alt").textContent = "Odd positions (10⁰,10²): (3 + " + y + ") = " + oddSum + "  |  Even positions (10¹,10³): (5 + 6) = " + evenSum;
    const el = document.getElementById("c8c5s11-res");
    el.className = "font-bold text-sm " + (ok ? "text-emerald-300" : "text-rose-300");
    el.textContent = "Difference = " + oddSum + " − " + evenSum + " = " + diff + (ok ? " → Multiple of 11 (DIVISIBLE BY 11 ✓)" : " → NOT a multiple of 11 ✗");
}
updC8C5S11();
</script>
"""

# Simulator 12: Coprime Factor Rules (Why 24 Needs 3×8 Rather Than Trap 4×6)
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🛡️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Coprime Composite Trap Tester (24 = 3×8 ✓ vs 4×6 ✗)</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800" id="c8c5s12-badge">N = 36</span>
    </div>

    <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <button onclick="testCoprimeS12(36)" class="px-2.5 py-1 rounded-lg bg-rose-700 text-white font-bold">Test Trap N = 36</button>
        <button onclick="testCoprimeS12(12)" class="px-2.5 py-1 rounded-lg bg-amber-700 text-white font-bold">Test Trap N = 12</button>
        <button onclick="testCoprimeS12(72)" class="px-2.5 py-1 rounded-lg bg-emerald-700 text-white font-bold">Test Valid N = 72</button>
        <button onclick="testCoprimeS12(120)" class="px-2.5 py-1 rounded-lg bg-cyan-700 text-white font-bold">Test Valid N = 120</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-cyan-200" id="c8c5s12-non"></div>
        <div class="font-bold text-sm" id="c8c5s12-cop"></div>
    </div>
</div>

<script>
function testCoprimeS12(N) {
    const p46 = N % 4 === 0 && N % 6 === 0;
    const p38 = N % 3 === 0 && N % 8 === 0;
    const p24 = N % 24 === 0;
    document.getElementById("c8c5s12-badge").textContent = "N = " + N;
    document.getElementById("c8c5s12-non").textContent = "Non-Coprime Pair (4 & 6): " + (p46 ? "Passes BOTH 4 and 6 ✓" : "Fails") + "   |   Actual 24-check: " + (p24 ? "DIVISIBLE BY 24 ✓" : "FAILS 24 ✗ (LCM(4,6)=12!)");
    const el = document.getElementById("c8c5s12-cop");
    el.className = "font-bold text-sm " + (p38 === p24 ? "text-emerald-300" : "text-rose-300");
    el.textContent = "Coprime Pair (3 & 8, HCF=1): " + (p38 ? "Passes 3 & 8 → GUARANTEED ÷24 ✓" : "Fails 3 or 8 → Correctly rejects " + N + "!");
}
testCoprimeS12(36);
</script>
"""

# Simulator 13: Digital Roots History (Aryabhata II's Mahāsiddhānta Multiplication Check)
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌀</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Digital Root Calculator &amp; Aryabhata II Product Verifier</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800" id="c8c5s13-badge">DR(1692) = 9</span>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Factor A:</span><span class="font-bold text-cyan-300" id="c8c5s13-av">47</span></div>
            <input type="range" min="11" max="99" step="1" value="47" id="c8c5s13-a" oninput="updC8C5S13()" class="w-full accent-cyan-400">
        </div>
        <div>
            <div class="flex justify-between mb-1"><span class="text-slate-300">Factor B:</span><span class="font-bold text-amber-300" id="c8c5s13-bv">36</span></div>
            <input type="range" min="11" max="99" step="1" value="36" id="c8c5s13-b" oninput="updC8C5S13()" class="w-full accent-amber-400">
        </div>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-cyan-200" id="c8c5s13-prod"></div>
        <div class="text-emerald-300 font-bold" id="c8c5s13-match"></div>
    </div>
</div>

<script>
function drS13(n) { return n === 0 ? 0 : (1 + ((n - 1) % 9)); }
function updC8C5S13() {
    const a = parseInt(document.getElementById("c8c5s13-a").value);
    const b = parseInt(document.getElementById("c8c5s13-b").value);
    const p = a * b;
    const da = drS13(a), db = drS13(b), dp = drS13(p), dMul = drS13(da * db);
    document.getElementById("c8c5s13-av").textContent = a + " (DR=" + da + ")";
    document.getElementById("c8c5s13-bv").textContent = b + " (DR=" + db + ")";
    document.getElementById("c8c5s13-badge").textContent = "DR(" + p + ") = " + dp;
    document.getElementById("c8c5s13-prod").textContent = a + " × " + b + " = " + p.toLocaleString("en-IN") + "   |   DR(" + p + ") = " + dp + "   (rem mod 9 = " + (p % 9) + ")";
    document.getElementById("c8c5s13-match").textContent = "Mahāsiddhānta Check: DR(DR(" + a + ") × DR(" + b + ")) = DR(" + da + " × " + db + ") = " + dMul + " === DR(" + p + ") ✓";
}
updC8C5S13();
</script>
"""

# Simulator 14: Cryptarithm Logic Puzzles (UT×3=PUT, BYE×6=RAY, JK×6=KKK)
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🔐</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Cryptarithm Step-by-Step Decoder (Section 5.3)</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c5s14-badge">UT × 3 = PUT</span>
    </div>

    <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <button onclick="setCryS14(0)" class="px-2.5 py-1 rounded-lg bg-amber-700 text-white font-bold">UT × 3 = PUT</button>
        <button onclick="setCryS14(1)" class="px-2.5 py-1 rounded-lg bg-cyan-700 text-white font-bold">BYE × 6 = RAY</button>
        <button onclick="setCryS14(2)" class="px-2.5 py-1 rounded-lg bg-emerald-700 text-white font-bold">JK × 6 = KKK</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5">
        <div class="text-emerald-300 font-bold text-sm" id="c8c5s14-sol"></div>
        <div class="text-cyan-200" id="c8c5s14-steps"></div>
    </div>
</div>

<script>
const cryList = [
    { b: "UT × 3 = PUT", s: "50 × 3 = 150   (P = 1, U = 5, T = 0)", d: "Algebra: 3×UT = 100P + UT → 2×UT = 100P → UT = 50P! Since UT < 100, P MUST be 1 → UT = 50." },
    { b: "BYE × 6 = RAY", s: "105 × 6 = 630   (B = 1, Y = 0, E = 5, R = 6, A = 3)", d: "6 × BYE < 1000 forces B = 1! Units E × 6 ends in even Y; E = 5 sets Y = 0 → 105 × 6 = 630 (all 5 unique!)." },
    { b: "JK × 6 = KKK", s: "74 × 6 = 444   (J = 7, K = 4)", d: "KKK = 111K = 3×37K → JK = 37K/2! Try even K: K=2 gives 37 (7≠2); K=4 gives 74 (4=4 ✓)!" }
];
function setCryS14(i) {
    document.getElementById("c8c5s14-badge").textContent = cryList[i].b;
    document.getElementById("c8c5s14-sol").textContent = cryList[i].s;
    document.getElementById("c8c5s14-steps").textContent = cryList[i].d;
}
setCryS14(0);
</script>
"""

# Simulator 15: Multi Digit Constraints (48a23b ÷ 18 & 3p7q8 ÷ 44)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🗝️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Multi-Digit Divisibility Lock Solver (48a23b ÷ 18)</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800" id="c8c5s15-badge">b = 4 → a = 6</span>
    </div>

    <div class="flex flex-wrap items-center gap-2 bg-slate-900/90 p-3 rounded-xl border border-slate-800 text-xs">
        <span class="text-slate-300 font-bold">Pick Even b (for ÷2):</span>
        <button onclick="solve18S15(0)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-cyan-300 font-bold border border-slate-700">b = 0</button>
        <button onclick="solve18S15(2)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-cyan-300 font-bold border border-slate-700">b = 2</button>
        <button onclick="solve18S15(4)" class="px-2.5 py-1 rounded-lg bg-cyan-700 text-white font-bold">b = 4</button>
        <button onclick="solve18S15(6)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-cyan-300 font-bold border border-slate-700">b = 6</button>
        <button onclick="solve18S15(8)" class="px-2.5 py-1 rounded-lg bg-slate-800 text-cyan-300 font-bold border border-slate-700">b = 8</button>
    </div>

    <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800 font-mono text-xs space-y-1.5 text-center">
        <div class="text-emerald-300 font-bold text-sm" id="c8c5s15-out"></div>
        <div class="text-amber-200">Check 44 = 4 × 11 on 3p7q8: even q ∈ {0,2,4,6,8} (for q8 ÷ 4) + 11-rule → 35,728 = 44 × 812!</div>
    </div>
</div>

<script>
function solve18S15(b) {
    const baseSum = 4 + 8 + 2 + 3 + b;
    let sols = [];
    for (let a = 0; a <= 9; a++) {
        if ((baseSum + a) % 9 === 0) {
            const num = 480230 + a * 1000 + b;
            sols.push("a=" + a + " (" + num.toLocaleString("en-IN") + " = 18×" + (num / 18) + ")");
        }
    }
    document.getElementById("c8c5s15-badge").textContent = "b = " + b;
    document.getElementById("c8c5s15-out").textContent = "Known Sum (17+" + b + "=" + baseSum + ") → Valid for ÷18: " + sols.join("  OR  ");
}
solve18S15(4);
</script>
"""

# Simulator 16: Navakankari (Nine Men's Morris 3-Concentric-Squares SVG Board)
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">♟️</span>
            <h3 class="text-sm sm:text-base font-bold text-amber-300">Navakankari (Sālu Mane Aṭa / Nine Men's Morris) Mill Arena</h3>
        </div>
        <span class="text-[11px] bg-amber-950/80 text-amber-300 px-2.5 py-1 rounded-full border border-amber-800" id="c8c5s16-badge">9 Pawns Each</span>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center bg-slate-900/90 p-3 rounded-2xl border border-slate-800">
        <svg viewBox="0 0 120 120" class="w-full max-h-32 bg-slate-950 rounded-xl border border-slate-800">
            <rect x="12" y="12" width="96" height="96" fill="none" stroke="#64748b" stroke-width="1.5"/>
            <rect x="28" y="28" width="64" height="64" fill="none" stroke="#64748b" stroke-width="1.5"/>
            <rect x="44" y="44" width="32" height="32" fill="none" stroke="#64748b" stroke-width="1.5"/>
            <line x1="60" y1="12" x2="60" y2="44" stroke="#64748b" stroke-width="1.5"/>
            <line x1="60" y1="76" x2="60" y2="108" stroke="#64748b" stroke-width="1.5"/>
            <line x1="12" y1="60" x2="44" y2="60" stroke="#64748b" stroke-width="1.5"/>
            <line x1="76" y1="60" x2="108" y2="60" stroke="#64748b" stroke-width="1.5"/>
            <circle cx="12" cy="12" r="4.5" fill="#fbbf24"/>
            <circle cx="60" cy="12" r="4.5" fill="#fbbf24"/>
            <circle cx="108" cy="12" r="4.5" fill="#fbbf24"/>
            <line x1="12" y1="12" x2="108" y2="12" stroke="#fbbf24" stroke-width="2.5"/>
            <circle cx="28" cy="60" r="4" fill="#38bdf8"/>
            <circle cx="60" cy="76" r="4" fill="#38bdf8"/>
        </svg>
        <div class="font-mono text-xs space-y-2">
            <div class="p-2 bg-slate-950 rounded-lg border border-amber-700/50 text-amber-300 font-bold">Phase 1 &amp; 2: Place 9 pawns each → Slide along lines!</div>
            <div class="p-2 bg-slate-950 rounded-lg border border-emerald-700/50 text-emerald-300 font-bold">3-in-a-Row Mill (Gold Line) = Capture 1 rival piece until ≤ 2 remain!</div>
        </div>
    </div>
</div>
"""

if __name__ == "__main__":
    print(f"Prepared {len(simulators_part2)} interactive simulators (Part 2).")
