#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 8 Maths Chapter 9: The Baudhāyana-Pythagoras Theorem
Part 2: Simulators 9 to 16
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>⚙️</span> Odd-Square Triple Generator: (n−1)² + (2n−1) = n²
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <span class="text-slate-400 self-center mr-1">Pick Odd k:</span>
    <button type="button" onclick="c9s9Gen(3)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">k=3 (9)</button>
    <button type="button" onclick="c9s9Gen(5)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">k=5 (25)</button>
    <button type="button" onclick="c9s9Gen(7)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">k=7 (49)</button>
    <button type="button" onclick="c9s9Gen(9)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700">k=9 (81)</button>
    <button type="button" onclick="c9s9Gen(11)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-indigo-300 border border-slate-700">k=11 (121)</button>
  </div>
  <div id="c9s9Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9s9Gen = function(k){
    const k2 = k * k;
    const n = (k2 + 1) / 2;
    const b = n - 1;
    document.getElementById('c9s9Out').innerHTML = `
      <div>1. Set odd square <b>2n − 1 = ${k}² = ${k2}</b></div>
      <div>2. Solve index <b>n = (${k2} + 1) ÷ 2 = ${n}</b> (so n − 1 = <b>${b}</b>)</div>
      <div>3. Identity: <b>${b}² + ${k}² = ${n}²</b> (${b*b} + ${k2} = ${n*n}) → Primitive Triple: <b class="text-emerald-300 text-sm">(${k}, ${b}, ${n})</b>!</div>`;
  };
  window.c9s9Gen(5);
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-rose-300 flex items-center gap-2">
    <span>🏛️</span> Fermat's Last Theorem Power Tester (xⁿ + yⁿ vs zⁿ)
  </h3>
  <div class="grid grid-cols-4 gap-2 text-xs">
    <label class="text-slate-300">x<input id="c9s10X" type="number" value="3" min="1" max="50" oninput="c9s10Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">y<input id="c9s10Y" type="number" value="4" min="1" max="50" oninput="c9s10Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">z<input id="c9s10Z" type="number" value="5" min="1" max="100" oninput="c9s10Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Exponent n
      <select id="c9s10N" onchange="c9s10Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white">
        <option value="2" selected>n = 2</option>
        <option value="3">n = 3</option>
        <option value="4">n = 4</option>
      </select>
    </label>
  </div>
  <div id="c9s10Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1"></div>
</div>
<script>
(function(){
  window.c9s10Calc = function(){
    const x = parseInt(document.getElementById('c9s10X').value, 10) || 3;
    const y = parseInt(document.getElementById('c9s10Y').value, 10) || 4;
    const z = parseInt(document.getElementById('c9s10Z').value, 10) || 5;
    const n = parseInt(document.getElementById('c9s10N').value, 10) || 2;
    const lhs = Math.pow(x, n) + Math.pow(y, n);
    const rhs = Math.pow(z, n);
    const eq = lhs === rhs;
    document.getElementById('c9s10Out').innerHTML = `
      <div>${x}^${n} + ${y}^${n} = <b class="text-cyan-300">${lhs}</b> vs ${z}^${n} = <b class="text-amber-300">${rhs}</b></div>
      <div class="${eq ? 'text-emerald-300' : 'text-rose-300'} font-semibold">${eq ? 'Exact Match! (Valid ONLY for n = 2!)' : `Mismatch (diff ${Math.abs(lhs-rhs)}): Andrew Wiles (1994) proved ZERO positive integer solutions exist for any n > 2!`}</div>`;
  };
  window.c9s10Calc();
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🪷</span> Bhāskarāchārya's Līlāvatī Lotus Depth Solver
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg viewBox="0 0 220 170" class="w-full max-w-[230px] mx-auto bg-slate-950 rounded-xl border border-slate-800">
      <rect x="10" y="60" width="200" height="95" fill="#0e7490" fill-opacity="0.28"/>
      <line x1="10" y1="60" x2="210" y2="60" stroke="#38bdf8" stroke-width="1.5"/>
      <line x1="70" y1="155" x2="70" y2="35" stroke="#4ade80" stroke-width="2" stroke-dasharray="3,3"/>
      <line x1="70" y1="155" x2="160" y2="60" stroke="#f472b6" stroke-width="2.5"/>
      <circle cx="160" cy="58" r="5" fill="#f472b6"/>
      <text x="58" y="110" fill="#cbd5e1" font-size="10">x</text>
      <text x="115" y="53" fill="#38bdf8" font-size="10">drift d</text>
      <text x="128" y="118" fill="#f472b6" font-size="10">x + h</text>
    </svg>
    <div class="space-y-2.5 text-xs">
      <label class="block text-slate-300">Horizontal Drift d (cubits): <input id="c9s11D" type="number" value="3" min="1" max="30" oninput="c9s11Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
      <label class="block text-slate-300">Height Above Water h: <input id="c9s11H" type="number" value="1" min="1" max="10" oninput="c9s11Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
      <div id="c9s11Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-300"></div>
    </div>
  </div>
</div>
<script>
(function(){
  window.c9s11Calc = function(){
    const d = Math.max(1, parseFloat(document.getElementById('c9s11D').value) || 3);
    const h = Math.max(0.5, parseFloat(document.getElementById('c9s11H').value) || 1);
    const depth = (d*d - h*h) / (2 * h);
    document.getElementById('c9s11Out').innerHTML = `
      Equation: ${d}² + x² = (x + ${h})²<br>
      Cancel x²: ${d*d} = ${2*h}x + ${h*h} → Lake Depth <b class="text-emerald-300">x = ${depth.toFixed(2).replace(/\\.00$/,'')} cubits</b> (stem = ${(depth+h).toFixed(2).replace(/\\.00$/,'')})`;
  };
  window.c9s11Calc();
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>💎</span> Rhombus Edge from Diagonals (24 & 70 → 37)
  </h3>
  <div class="grid grid-cols-2 gap-3 text-xs">
    <label class="text-slate-300">Diagonal d₁: <input id="c9s12D1" type="number" value="24" min="2" max="200" oninput="c9s12Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Diagonal d₂: <input id="c9s12D2" type="number" value="70" min="2" max="200" oninput="c9s12Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
  </div>
  <div id="c9s12Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1"></div>
</div>
<script>
(function(){
  window.c9s12Calc = function(){
    const d1 = Math.max(2, parseFloat(document.getElementById('c9s12D1').value) || 24);
    const d2 = Math.max(2, parseFloat(document.getElementById('c9s12D2').value) || 70);
    const h1 = d1 / 2, h2 = d2 / 2;
    const s2 = h1*h1 + h2*h2;
    const s = Math.sqrt(s2);
    const sStr = Number.isInteger(s) ? s.toString() : s.toFixed(2);
    document.getElementById('c9s12Out').innerHTML = `
      <div>Diagonals bisect at 90° → Right-triangle legs: <b class="text-cyan-300">${h1}</b> and <b class="text-amber-300">${h2}</b></div>
      <div>Side² = ${h1}² + ${h2}² = ${h1*h1} + ${h2*h2} = <b>${s2}</b> → Rhombus Edge = <b class="text-emerald-300">${sStr}</b> (Perimeter = ${(4*s).toFixed(2).replace(/\\.00$/,'')})</div>`;
  };
  window.c9s12Calc();
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🔷</span> Tilted Grid Squares & Equilateral Triangle Area
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-cyan-300">Tilted Grid Square (Δx, Δy)</div>
      <div class="grid grid-cols-2 gap-2">
        <label class="text-slate-400">Δx<input id="c9s13X" type="number" value="2" min="0" max="10" oninput="c9s13Grid()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
        <label class="text-slate-400">Δy<input id="c9s13Y" type="number" value="3" min="0" max="10" oninput="c9s13Grid()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      </div>
      <div id="c9s13GridOut" class="text-emerald-300 font-semibold"></div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-amber-300">Equilateral Triangle Altitude & Area</div>
      <label class="block text-slate-400">Side Length s: <input id="c9s13S" type="number" value="10" min="2" max="50" oninput="c9s13Tri()" class="mt-1 w-full px-2 py-1 rounded bg-slate-900 border border-slate-700 text-white"></label>
      <div id="c9s13TriOut" class="text-amber-200 font-semibold"></div>
    </div>
  </div>
</div>
<script>
(function(){
  window.c9s13Grid = function(){
    const dx = parseInt(document.getElementById('c9s13X').value, 10) || 0;
    const dy = parseInt(document.getElementById('c9s13Y').value, 10) || 0;
    const area = dx*dx + dy*dy;
    document.getElementById('c9s13GridOut').textContent = `Area = ${dx}² + ${dy}² = ${area} sq units (side = √${area})`;
  };
  window.c9s13Tri = function(){
    const s = Math.max(2, parseFloat(document.getElementById('c9s13S').value) || 10);
    const h = (Math.sqrt(3) / 2) * s;
    const area = 0.5 * s * h;
    document.getElementById('c9s13TriOut').textContent = `h = √(${s}²−${s/2}²) = ${h.toFixed(2)} | Area = ${area.toFixed(2)}`;
  };
  window.c9s13Grid();
  window.c9s13Tri();
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📏</span> Converse Right-Angle Cord Verifier (a² + b² vs c²)
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <label class="text-slate-300">Side a<input id="c9s14A" type="number" value="5" min="1" max="50" oninput="c9s14Check()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Side b<input id="c9s14B" type="number" value="12" min="1" max="50" oninput="c9s14Check()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Longest c<input id="c9s14C" type="number" value="13" min="1" max="80" oninput="c9s14Check()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
  </div>
  <div id="c9s14Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1"></div>
</div>
<script>
(function(){
  window.c9s14Check = function(){
    const a = parseFloat(document.getElementById('c9s14A').value) || 1;
    const b = parseFloat(document.getElementById('c9s14B').value) || 1;
    const c = parseFloat(document.getElementById('c9s14C').value) || 1;
    if(a + b <= c){
      document.getElementById('c9s14Out').innerHTML = '<span class="text-rose-400 font-bold">Cannot close a triangle! (a + b must exceed c)</span>';
      return;
    }
    const sum = a*a + b*b, c2 = c*c;
    let verdict = '';
    if(Math.abs(sum - c2) < 1e-9) verdict = '<span class="text-emerald-300 font-bold">EXACT 90° Right-Angled Triangle! (a² + b² = c²)</span>';
    else if(sum > c2) verdict = '<span class="text-cyan-300 font-bold">ACUTE Corner (< 90°) since a² + b² > c²</span>';
    else verdict = '<span class="text-amber-300 font-bold">OBTUSE Corner (> 90°) since a² + b² < c²</span>';
    document.getElementById('c9s14Out').innerHTML = `<div>a² + b² = ${sum} vs c² = ${c2}</div><div>${verdict}</div>`;
  };
  window.c9s14Check();
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>📚</span> Chapter 9 Formula & Proof Reference Matrix
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-cyan-300 mb-1">1. Doubling, Halving & Isosceles</div>
      <div class="text-slate-300">Diagonal square = 2× area; Midpoint PQRS = ½ area; Isosceles c² = 2a² (c = a√2).</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-emerald-300 mb-1">2. Bounds & Irrationality of √2</div>
      <div class="text-slate-300">1.414 < √2 < 1.415; terminating decimal squares end ≠ 0; Euclid 2n² = m² (odd ≠ even 2s).</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-amber-300 mb-1">3. General Law & Triples</div>
      <div class="text-slate-300">a² + b² = c² (Verse 1.12); scaled (ka, kb, kc); odd-square (n−1)² + (2n−1) = n².</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-rose-300 mb-1">4. Fermat & Applications</div>
      <div class="text-slate-300">xⁿ + yⁿ = zⁿ has zero integer solutions for n > 2 (Wiles 1994); Līlāvatī lotus & rhombus diagonals.</div>
    </div>
  </div>
</div>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>🎁</span> Find the Colours! One-Box Deduction Lab
    </h3>
    <button type="button" onclick="c9s16New()" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 text-xs border border-slate-700">New Secret Scramble</button>
  </div>
  <p class="text-xs text-slate-400">Every box label is WRONG! Open <b>ONLY ONE</b> box to see its ball, then deduce all 3 true colors:</p>
  <div id="c9s16Boxes" class="grid grid-cols-3 gap-2.5 text-center text-xs"></div>
  <div id="c9s16Deduce" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">Click any single box above to peek inside!</div>
</div>
<script>
(function(){
  const derangements = [
    { Red: 'Blue', Blue: 'Green', Green: 'Red' },
    { Red: 'Green', Blue: 'Red', Green: 'Blue' }
  ];
  let secretIdx = 0;
  let opened = null;
  function render(){
    const boxEl = document.getElementById('c9s16Boxes');
    if(!boxEl) return;
    boxEl.innerHTML = '';
    ['Red', 'Blue', 'Green'].forEach(lbl => {
      const isOpen = opened === lbl;
      const inside = derangements[secretIdx][lbl];
      const badgeColor = inside === 'Red' ? 'text-rose-400' : inside === 'Blue' ? 'text-sky-400' : 'text-emerald-400';
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = `p-3 rounded-xl border transition-all ${isOpen ? 'bg-slate-800 border-amber-400' : 'bg-slate-950 hover:bg-slate-900 border-slate-700'}`;
      btn.innerHTML = `<div class="text-[10px] uppercase text-slate-400">Label</div><div class="font-bold text-white mb-1">"${lbl}"</div><div class="text-xs ${isOpen ? badgeColor + ' font-bold' : 'text-slate-500'}">${isOpen ? 'Ball: ' + inside : 'Click to Peek (1×)'}</div>`;
      btn.onclick = () => {
        if(opened !== null) return;
        opened = lbl;
        render();
        const others = ['Red', 'Blue', 'Green'].filter(x => x !== lbl);
        const remBalls = ['Red', 'Blue', 'Green'].filter(x => x !== inside);
        const d = derangements[secretIdx];
        document.getElementById('c9s16Deduce').innerHTML = `
          <b class="text-emerald-300">Forced Unique Deduction!</b> Opened Label <b>"${lbl}"</b> → found <b class="${badgeColor}">${inside}</b>!<br>
          Remaining boxes "${others[0]}" & "${others[1]}" must hold {${remBalls[0]}, ${remBalls[1]}}. Because NO label can match its content, <b>"${others[0]}" → ${d[others[0]]}</b> and <b>"${others[1]}" → ${d[others[1]]}</b>!`;
      };
      boxEl.appendChild(btn);
    });
  }
  window.c9s16New = function(){
    secretIdx = (secretIdx + 1) % 2;
    opened = null;
    document.getElementById('c9s16Deduce').textContent = 'New all-wrong arrangement ready! Click ONLY ONE box above to deduce all 3!';
    render();
  };
  render();
})();
</script>
"""
}
