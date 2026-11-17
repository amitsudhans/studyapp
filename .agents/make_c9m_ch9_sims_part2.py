#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 9: Propositions and their Converses
Part 2: Simulators 9 to 16 (Slides 9 to 16)
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📏</span> SSS Right-Triangle Converse Proof Simulator (Baudhāyana-Pythagoras)
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Select Side Triple (a, b, c):</span>
    <select id="c9c9s9Sel" onchange="c9c9s9Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
      <option value="3,4,5">(3, 4, 5) — Classic Pythagorean Triple</option>
      <option value="5,12,13">(5, 12, 13) — Right Triangle Triple</option>
      <option value="8,15,17">(8, 15, 17) — Right Triangle Triple</option>
      <option value="5,6,8">(5, 6, 8) — Non-Right Triangle</option>
    </select>
  </label>
  <div id="c9c9s9Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c9s9Draw = function(){
    const [a, b, c] = document.getElementById('c9c9s9Sel').value.split(',').map(Number);
    const lhs = a*a + b*b, rhs = c*c;
    const eq = lhs === rhs;
    document.getElementById('c9c9s9Out').innerHTML = `
      <div>Test: <strong>${a}² + ${b}² = ${lhs}</strong> vs <strong>${c}² = ${rhs}</strong></div>
      ${eq ? `<div class="text-emerald-300 font-bold">MATCH! Construct right △PQR (∠R = 90°, legs ${a}, ${b}) ⇒ PQ = √${lhs} = ${c}. By SSS congruence, △ABC ≅ △PQR ⇒ ∠C = 90°!</div>`
           : `<div class="text-rose-400 font-bold">MISMATCH (${lhs} ≠ ${rhs})! By the forward theorem &amp; converse, ∠C ≠ 90° (actually obtuse since ${lhs} < ${rhs}).</div>`}
    `;
  };
  setTimeout(window.c9c9s9Draw, 40);
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📝</span> Conditional Phrasing Translator &amp; Converse Builder
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Choose Alternative English Phrasing:</span>
    <select id="c9c9s10Sel" onchange="c9c9s10Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
      <option value="when">"A triangle is isosceles WHEN two sides are equal."</option>
      <option value="all">"ALL squares are rectangles."</option>
      <option value="onlyif">"A prime exceeds 2 ONLY IF it is odd."</option>
    </select>
  </label>
  <div id="c9c9s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const tr = {
    when: [
      'If two sides of a triangle are equal, then the triangle is isosceles.',
      'If a triangle is isosceles, then two of its sides are equal. (TRUE)'
    ],
    all: [
      'If a quadrilateral is a square, then it is a rectangle.',
      'If a quadrilateral is a rectangle, then it is a square. (FALSE — counterexample: 5 × 3 rectangle)'
    ],
    onlyif: [
      'If a prime number exceeds 2, then it is odd.',
      'If an odd number exceeds 2, then it is prime. (FALSE — counterexample: 9)'
    ]
  };
  window.c9c9s10Draw = function(){
    const [std, conv] = tr[document.getElementById('c9c9s10Sel').value];
    document.getElementById('c9c9s10Out').innerHTML = `
      <div><strong class="text-cyan-300">Standard Form (If X, then Y):</strong> ${std}</div>
      <div><strong class="text-amber-300">Converse (If Y, then X):</strong> ${conv}</div>
    `;
  };
  setTimeout(window.c9c9s10Draw, 40);
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔷</span> Transversal &amp; Quadrilateral Property Truth Matrix
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c9s11Show('para')" class="px-3 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-200 font-bold">Parallel &amp; Corresponding ∠</button>
    <button onclick="c9c9s11Show('eqdiag')" class="px-3 py-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 border border-amber-500/40 text-amber-200 font-bold">Square ⇒ Equal Diagonals</button>
    <button onclick="c9c9s11Show('perpdiag')" class="px-3 py-1.5 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 border border-rose-500/40 text-rose-200 font-bold">Square ⇒ 90° Bisecting Diagonals</button>
  </div>
  <div id="c9c9s11Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const items = {
    para: ['Forward: TRUE | Converse: TRUE', 'Two lines are parallel ⇔ Corresponding (or Alternate Interior) angles are equal.'],
    eqdiag: ['Forward: TRUE | Converse: FALSE', 'Counterexample to converse: A non-square rectangle (or isosceles trapezium) has equal diagonals without being a square!'],
    perpdiag: ['Forward: TRUE | Converse: FALSE', 'Counterexample to converse: A non-square rhombus (e.g., diagonals 6 and 8) has perpendicular bisecting diagonals!']
  };
  window.c9c9s11Show = function(k){
    const [badge, msg] = items[k];
    document.getElementById('c9c9s11Out').innerHTML = `
      <div class="font-bold text-cyan-300">${badge}</div>
      <div>${msg}</div>
    `;
  };
  setTimeout(function(){ window.c9c9s11Show('para'); }, 40);
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🎯</span> Angle Bisector &amp; Incentre Equidistance Explorer
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Move Point P Along Angle Bisector (Distance from Vertex B):</span>
      <span id="c9c9s12DLbl" class="text-amber-300 font-bold">BP = 120 px</span>
    </div>
    <input id="c9c9s12D" type="range" min="50" max="170" value="120" oninput="c9c9s12Draw()" class="w-full accent-amber-400">
  </label>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 items-center">
    <svg id="c9c9s12Svg" viewBox="0 0 260 150" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c9c9s12Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
  </div>
</div>
<script>
(function(){
  window.c9c9s12Draw = function(){
    const bp = parseInt(document.getElementById('c9c9s12D').value, 10);
    document.getElementById('c9c9s12DLbl').textContent = 'BP = ' + bp + ' px';
    const bx = 30, by = 120;
    const rad = 22 * Math.PI / 180;
    const px = bx + bp * Math.cos(rad), py = by - bp * Math.sin(rad);
    const foot1x = px, foot1y = by;
    const perpLen = +(bp * Math.sin(rad)).toFixed(1);
    const a2 = 44 * Math.PI / 180;
    const proj = bp * Math.cos(rad);
    const foot2x = bx + proj * Math.cos(a2), foot2y = by - proj * Math.sin(a2);
    document.getElementById('c9c9s12Svg').innerHTML = `
      <line x1="${bx}" y1="${by}" x2="240" y2="${by}" stroke="#38bdf8" stroke-width="2"/>
      <line x1="${bx}" y1="${by}" x2="${bx + 210*Math.cos(a2)}" y2="${by - 210*Math.sin(a2)}" stroke="#38bdf8" stroke-width="2"/>
      <line x1="${bx}" y1="${by}" x2="${bx + 200*Math.cos(rad)}" y2="${by - 200*Math.sin(rad)}" stroke="#fbbf24" stroke-dasharray="4 3" stroke-width="1.5"/>
      <line x1="${px}" y1="${py}" x2="${foot1x}" y2="${foot1y}" stroke="#34d399" stroke-width="2"/>
      <line x1="${px}" y1="${py}" x2="${foot2x}" y2="${foot2y}" stroke="#34d399" stroke-width="2"/>
      <circle cx="${px}" cy="${py}" r="5" fill="#fbbf24"/>
    `;
    document.getElementById('c9c9s12Out').innerHTML = `
      <div class="font-bold text-emerald-300">Perpendicular Distance to BA = Distance to BC = ${perpLen} px</div>
      <div>Both directions hold: On Bisector (AAS) ⇔ Equidistant from Arms (RHS)!</div>
      <div class="text-cyan-300">All 3 bisectors meet at the Incentre (equidistant from all 3 sides).</div>
    `;
  };
  setTimeout(window.c9c9s12Draw, 40);
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>✖️</span> Real Power Parity Explorer: x² = y² vs x³ = y³
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Value x:</span>
      <input id="c9c9s13X" type="number" value="3" oninput="c9c9s13Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Value y:</span>
      <input id="c9c9s13Y" type="number" value="-3" oninput="c9c9s13Draw()" class="w-full mt-1.5 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
  </div>
  <div id="c9c9s13Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c9s13Draw = function(){
    const x = parseFloat(document.getElementById('c9c9s13X').value || '0');
    const y = parseFloat(document.getElementById('c9c9s13Y').value || '0');
    const sqEq = x*x === y*y;
    const cuEq = x*x*x === y*y*y;
    const same = x === y;
    document.getElementById('c9c9s13Out').innerHTML = `
      <div>x² = ${x*x}, y² = ${y*y} &nbsp;(${sqEq ? 'EQUAL' : 'NOT equal'}) &nbsp;|&nbsp; x³ = ${x*x*x}, y³ = ${y*y*y} &nbsp;(${cuEq ? 'EQUAL' : 'NOT equal'})</div>
      <div class="font-bold ${sqEq && !same ? 'text-rose-400' : 'text-emerald-300'}">
        ${sqEq && !same ? `COUNTEREXAMPLE! (${x})² = (${y})² = ${x*x}, yet ${x} ≠ ${y} — disproving "x² = y² ⇒ x = y"!`
                        : (same ? 'x = y makes both x² = y² and x³ = y³ true.' : 'Try x = 3, y = −3 to trigger the squaring counterexample!')}
      </div>
      <div class="text-cyan-300">By contrast, x³ = y³ ⇔ x = y holds for ALL real numbers (odd powers preserve sign)!</div>
    `;
  };
  setTimeout(window.c9c9s13Draw, 40);
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔍</span> Divisibility Implication &amp; Counterexample Checker
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Test Integer N:</span>
    <input id="c9c9s14N" type="number" min="1" max="500" value="16" oninput="c9c9s14Draw()" class="w-full mt-1.5 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
  </label>
  <div id="c9c9s14Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c9s14Draw = function(){
    const n = Math.max(1, parseInt(document.getElementById('c9c9s14N').value || '1', 10));
    const dsum = String(n).split('').reduce((a,b)=>a+Number(b), 0);
    const div3 = n % 3 === 0;
    const div8 = n % 8 === 0;
    const div24 = n % 24 === 0;
    document.getElementById('c9c9s14Out').innerHTML = `
      <div><strong>Digit-Sum Rule for 3:</strong> Sum of digits = ${dsum} (${dsum % 3 === 0 ? '÷3' : 'not ÷3'}) ⇔ ${n} is ${div3 ? 'divisible' : 'NOT divisible'} by 3.</div>
      <div><strong>24 vs 8 Check:</strong> Divisible by 8? <strong>${div8 ? 'YES' : 'NO'}</strong> | Divisible by 24? <strong>${div24 ? 'YES' : 'NO'}</strong></div>
      <div class="${div8 && !div24 ? 'text-rose-400 font-bold' : 'text-cyan-300'}">
        ${div8 && !div24 ? `COUNTEREXAMPLE! ${n} is divisible by 8, yet NOT by 24 — disproving "÷8 ⇒ ÷24"!` : 'Try 8, 16, or 32 to see counterexamples to "÷8 ⇒ ÷24".'}
      </div>
    `;
  };
  setTimeout(window.c9c9s14Draw, 40);
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧪</span> Prime Formula Counterexample Lab
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Select Formula:</span>
      <select id="c9c9s15F" onchange="c9c9s15Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
        <option value="f1">n² + n + 11</option>
        <option value="f2">4n² + 1</option>
        <option value="f3">4ⁿ + 3</option>
        <option value="f4">2ⁿ − 1 (Mersenne-style)</option>
      </select>
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>Test Natural Number (n):</span>
        <span id="c9c9s15NLbl" class="text-amber-300 font-bold">n = 4</span>
      </div>
      <input id="c9c9s15N" type="range" min="1" max="11" value="4" oninput="c9c9s15Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9c9s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  function factor(num){
    if(num < 2) return null;
    for(let d = 2; d * d <= num; d++){
      if(num % d === 0) return d;
    }
    return null;
  }
  window.c9c9s15Draw = function(){
    const f = document.getElementById('c9c9s15F').value;
    const n = parseInt(document.getElementById('c9c9s15N').value, 10);
    document.getElementById('c9c9s15NLbl').textContent = 'n = ' + n;
    let val = 0, expr = '';
    if(f === 'f1'){ val = n*n + n + 11; expr = `${n}² + ${n} + 11`; }
    else if(f === 'f2'){ val = 4*n*n + 1; expr = `4(${n})² + 1`; }
    else if(f === 'f3'){ val = Math.pow(4, n) + 3; expr = `4^${n} + 3`; }
    else { val = Math.pow(2, n) - 1; expr = `2^${n} − 1`; }
    const div = factor(val);
    document.getElementById('c9c9s15Out').innerHTML = `
      <div class="text-sm font-bold text-cyan-300">${expr} = ${val}</div>
      ${div ? `<div class="text-rose-400 font-bold">COUNTEREXAMPLE FOUND! ${val} = ${div} × ${val/div} is COMPOSITE!</div>`
            : `<div class="text-emerald-300 font-bold">${val} is PRIME at n = ${n} — keep increasing n to find the counterexample!</div>`}
    `;
  };
  setTimeout(window.c9c9s15Draw, 40);
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📚</span> Chapter 9 Complete Logic &amp; Converse Truth Matrix
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c9s16Show('tt')" class="px-3 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-200 font-bold">Both True (T, T)</button>
    <button onclick="c9c9s16Show('tf')" class="px-3 py-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 border border-amber-500/40 text-amber-200 font-bold">One-Way (T, F)</button>
    <button onclick="c9c9s16Show('ff')" class="px-3 py-1.5 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 border border-rose-500/40 text-rose-200 font-bold">Both False (F, F)</button>
  </div>
  <div id="c9c9s16Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const cards = {
    tt: `<div class="font-bold text-emerald-300 text-sm">Both Proposition &amp; Converse TRUE (Biconditional X ⇔ Y)</div>
      <ul class="list-disc pl-4 space-y-1">
        <li>N is a perfect square ⇔ N has an odd number of positive factors</li>
        <li>a² + b² = c² in △ABC ⇔ △ABC is right-angled at C (Baudhāyana-Pythagoras)</li>
        <li>x = y ⇔ x³ = y³ (over real numbers ℝ)</li>
        <li>Divisible by 3 ⇔ Sum of digits divisible by 3</li>
      </ul>`,
    tf: `<div class="font-bold text-amber-300 text-sm">Proposition TRUE, Converse FALSE</div>
      <ul class="list-disc pl-4 space-y-1">
        <li>Rain ⇒ Wet road (Converse fails: water tanker spill)</li>
        <li>Multiple of 6 ⇒ Multiple of 3 (Converse fails: 9, 15)</li>
        <li>Congruent triangles ⇒ Equal area (Converse fails: 6×4 vs 12×2)</li>
        <li>x = y ⇒ x² = y² (Converse fails: x = 3, y = −3)</li>
      </ul>`,
    ff: `<div class="font-bold text-rose-400 text-sm">Both Proposition &amp; Converse FALSE</div>
      <ul class="list-disc pl-4 space-y-1">
        <li>"If a number is odd, it is prime" (False: 9) vs "If prime, it is odd" (False: 2)</li>
        <li>Always test both directions independently; one counterexample refutes any universal claim!</li>
      </ul>`
  };
  window.c9c9s16Show = function(k){
    document.getElementById('c9c9s16Out').innerHTML = cards[k] || cards.tt;
  };
  setTimeout(function(){ window.c9c9s16Show('tt'); }, 40);
})();
</script>
"""
}
