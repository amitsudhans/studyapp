#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 4: Exploring Algebraic Identities
Part 2: Simulators 9 to 16
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-indigo-300 flex items-center gap-2">
    <span>✂️</span> Middle-Term Coefficient Splitter: x² + (a + b)x + ab
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c4s9Pick(11,24)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">x² + 11x + 24</button>
    <button type="button" onclick="c9c4s9Pick(9,14)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">x² + 9x + 14</button>
    <button type="button" onclick="c9c4s9Pick(13,36)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">x² + 13x + 36</button>
    <button type="button" onclick="c9c4s9Pick(15,54)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">x² + 15x + 54</button>
  </div>
  <div id="c9c4s9Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  window.c9c4s9Pick = function(B, C){
    let a=1, b=C;
    for(let i=1;i<=C;i++){ if(C%i===0 && i + C/i === B){ a=i; b=C/i; break; } }
    document.getElementById('c9c4s9Out').innerHTML = `
      <div class="text-cyan-300">Target Polynomial: x² + ${B}x + ${C}</div>
      <div class="text-amber-300">Product-Sum Pair: a·b = ${C} and a + b = ${B} ⇒ (${a}, ${b})</div>
      <div>Grouping: x² + ${a}x + ${b}x + ${C} = x(x + ${a}) + ${b}(x + ${a})</div>
      <div class="text-emerald-300 font-bold text-sm">Factored Product: (x + ${a})(x + ${b})</div>
    `;
  };
  c9c4s9Pick(11, 24);
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>➕➖</span> Signed Middle-Term Splitting Sign Logic Lab
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c4s10Pick(0)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">x² − 10x + 21</button>
    <button type="button" onclick="c9c4s10Pick(1)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">x² + 2x − 15</button>
    <button type="button" onclick="c9c4s10Pick(2)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">x² − 3x − 28</button>
    <button type="button" onclick="c9c4s10Pick(3)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">x² − 13x + 40</button>
  </div>
  <div id="c9c4s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  const cases = [
    { q:'x² − 10x + 21', rule:'Product (+21) > 0 & Sum (−10) < 0 ⇒ BOTH factors NEGATIVE!', pair:'(−3) and (−7)', ans:'(x − 3)(x − 7)' },
    { q:'x² + 2x − 15', rule:'Product (−15) < 0 ⇒ OPPOSITE SIGNS; Sum (+2) > 0 ⇒ larger gets +!', pair:'(+5) and (−3)', ans:'(x + 5)(x − 3)' },
    { q:'x² − 3x − 28', rule:'Product (−28) < 0 ⇒ OPPOSITE SIGNS; Sum (−3) < 0 ⇒ larger gets −!', pair:'(−7) and (+4)', ans:'(x − 7)(x + 4)' },
    { q:'x² − 13x + 40', rule:'Product (+40) > 0 & Sum (−13) < 0 ⇒ BOTH factors NEGATIVE!', pair:'(−5) and (−8)', ans:'(x − 5)(x − 8)' }
  ];
  window.c9c4s10Pick = function(i){
    const d = cases[i];
    document.getElementById('c9c4s10Out').innerHTML = `
      <div class="font-bold text-cyan-300 text-sm">${d.q}</div>
      <div class="text-amber-300">Sign Rule: ${d.rule}</div>
      <div class="font-mono">Chosen Roots: ${d.pair}</div>
      <div class="text-emerald-300 font-bold text-sm font-mono">Factored Result: ${d.ans}</div>
    `;
  };
  c9c4s10Pick(0);
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-purple-300 flex items-center gap-2">
    <span>🧊</span> 3D Cube Decomposition Explorer: (a + b)³ = a³ + 3a²b + 3ab² + b³
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Edge a: <strong id="c9c4s11AVal" class="text-cyan-300">4</strong></span>
      <input type="range" id="c9c4s11A" min="2" max="10" value="4" oninput="c9c4s11Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Edge b: <strong id="c9c4s11BVal" class="text-amber-300">2</strong></span>
      <input type="range" id="c9c4s11B" min="1" max="6" value="2" oninput="c9c4s11Draw()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <div id="c9c4s11Out" class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs"></div>
  <div id="c9c4s11Sum" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs font-mono text-emerald-300"></div>
</div>
<script>
(function(){
  window.c9c4s11Draw = function(){
    const a = parseInt(document.getElementById('c9c4s11A').value);
    const b = parseInt(document.getElementById('c9c4s11B').value);
    document.getElementById('c9c4s11AVal').textContent = a;
    document.getElementById('c9c4s11BVal').textContent = b;
    const v1 = a*a*a, v2 = 3*a*a*b, v3 = 3*a*b*b, v4 = b*b*b, tot = Math.pow(a+b, 3);
    const cards = [
      { n:'1 Big Cube (a³)', v:v1, c:'cyan' },
      { n:'3 Slabs (3a²b)', v:v2, c:'emerald' },
      { n:'3 Bars (3ab²)', v:v3, c:'purple' },
      { n:'1 Corner Cube (b³)', v:v4, c:'amber' }
    ];
    document.getElementById('c9c4s11Out').innerHTML = cards.map(x => `
      <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-center">
        <div class="text-${x.c}-300 font-bold">${x.n}</div>
        <div class="text-base font-mono text-white mt-1">${x.v}</div>
      </div>
    `).join('');
    document.getElementById('c9c4s11Sum').textContent = `8 Solids Total Volume: (${a} + ${b})³ = ${v1} + ${v2} + ${v3} + ${v4} = ${tot}`;
  };
  c9c4s11Draw();
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-rose-300 flex items-center gap-2">
    <span>📦</span> Derived Cubic &amp; Factor Identities Switcher: (a − b)³ and x³ ± y³
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c4s12Pick(0)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">(a − b)³ Expansion</button>
    <button type="button" onclick="c9c4s12Pick(1)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">x³ − y³ Factoring</button>
    <button type="button" onclick="c9c4s12Pick(2)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">x³ + y³ Factoring</button>
    <button type="button" onclick="c9c4s12Pick(3)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">27m³ − 64n³ Example</button>
  </div>
  <div id="c9c4s12Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  const list = [
    { f:'(a − b)³ = a³ − 3a²b + 3ab² − b³ = a³ − b³ − 3ab(a − b)', ex:'Replacing +b with (−b): odd powers keep (−), even powers turn (+)! Example: (x − 2)³ = x³ − 6x² + 12x − 8.' },
    { f:'x³ − y³ = (x − y)(x² + xy + y²)', ex:'Linear factor keeps (−), quadratic factor stays ALL (+) so cross terms cancel cleanly.' },
    { f:'x³ + y³ = (x + y)(x² − xy + y²)', ex:'Linear factor keeps (+), middle quadratic term switches to (−xy) to cancel cross products!' },
    { f:'27m³ − 64n³ = (3m)³ − (4n)³ = (3m − 4n)(9m² + 12mn + 16n²)', ex:'Direct application of x³ − y³ using x = 3m and y = 4n.' }
  ];
  window.c9c4s12Pick = function(i){
    const d = list[i];
    document.getElementById('c9c4s12Out').innerHTML = `
      <div class="text-rose-300 font-bold text-sm">${d.f}</div>
      <div class="text-slate-300 font-sans pt-1">${d.ex}</div>
    `;
  };
  c9c4s12Pick(1);
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>✨</span> Master Cubic Identity Tester: x³ + y³ + z³ − 3xyz &amp; Zero-Sum Shortcut
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">x: <strong id="c9c4s13XVal" class="text-cyan-300">-12</strong><input type="range" id="c9c4s13X" min="-12" max="12" value="-12" oninput="c9c4s13Draw()" class="w-full accent-cyan-400 mt-1"></label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">y: <strong id="c9c4s13YVal" class="text-emerald-300">7</strong><input type="range" id="c9c4s13Y" min="-10" max="10" value="7" oninput="c9c4s13Draw()" class="w-full accent-emerald-400 mt-1"></label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">z: <strong id="c9c4s13ZVal" class="text-amber-300">5</strong><input type="range" id="c9c4s13Z" min="-10" max="10" value="5" oninput="c9c4s13Draw()" class="w-full accent-amber-400 mt-1"></label>
  </div>
  <div id="c9c4s13Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  window.c9c4s13Draw = function(){
    const x = parseInt(document.getElementById('c9c4s13X').value);
    const y = parseInt(document.getElementById('c9c4s13Y').value);
    const z = parseInt(document.getElementById('c9c4s13Z').value);
    document.getElementById('c9c4s13XVal').textContent = x;
    document.getElementById('c9c4s13YVal').textContent = y;
    document.getElementById('c9c4s13ZVal').textContent = z;
    const sum = x + y + z;
    const cubes = x*x*x + y*y*y + z*z*z;
    const tx = 3*x*y*z;
    const lhs = cubes - tx;
    document.getElementById('c9c4s13Out').innerHTML = `
      <div>x + y + z = (${x}) + (${y}) + (${z}) = <strong class="${sum===0?'text-emerald-300':'text-amber-300'}">${sum}</strong></div>
      <div>x³ + y³ + z³ = <strong>${cubes}</strong> vs 3xyz = <strong>${tx}</strong></div>
      <div class="pt-1 font-bold ${sum===0?'text-emerald-300':'text-cyan-300'}">${sum===0 ? 'ZERO SUM COROLLARY ACTIVE! x³+y³+z³ = 3xyz directly!' : 'Identity Difference x³+y³+z³−3xyz = ' + lhs}</div>
    `;
  };
  c9c4s13Draw();
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚗️</span> Rational Expression P(x)/Q(x) Factor &amp; Cancel Pipeline
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c4s14Pick(0)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">(x² − 9) / (x² + 7x + 12)</button>
    <button type="button" onclick="c9c4s14Pick(1)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">(x² − 16) / (x² + 9x + 20)</button>
    <button type="button" onclick="c9c4s14Pick(2)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">(x³ + 8) / (x² − 2x + 4)</button>
    <button type="button" onclick="c9c4s14Pick(3)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">(2x² − 18) / (x² + 5x + 6)</button>
  </div>
  <div id="c9c4s14Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  const ex = [
    { orig:'(x² − 9) / (x² + 7x + 12)', fac:'[(x − 3)(x + 3)] / [(x + 3)(x + 4)]', dom:'x ≠ −3, −4', simp:'(x − 3) / (x + 4)' },
    { orig:'(x² − 16) / (x² + 9x + 20)', fac:'[(x − 4)(x + 4)] / [(x + 4)(x + 5)]', dom:'x ≠ −4, −5', simp:'(x − 4) / (x + 5)' },
    { orig:'(x³ + 8) / (x² − 2x + 4)', fac:'[(x + 2)(x² − 2x + 4)] / (x² − 2x + 4)', dom:'All x ∈ ℝ (den > 0)', simp:'x + 2' },
    { orig:'(2x² − 18) / (x² + 5x + 6)', fac:'[2(x − 3)(x + 3)] / [(x + 2)(x + 3)]', dom:'x ≠ −2, −3', simp:'2(x − 3) / (x + 2)' }
  ];
  window.c9c4s14Pick = function(i){
    const d = ex[i];
    document.getElementById('c9c4s14Out').innerHTML = `
      <div class="text-cyan-300">1. Original P(x)/Q(x): ${d.orig}</div>
      <div class="text-amber-300">2. Factor Top &amp; Bottom: ${d.fac}</div>
      <div class="text-rose-300">3. Domain Exclusions: ${d.dom}</div>
      <div class="text-emerald-300 font-bold text-sm">4. Cancel Common Factor → ${d.simp}</div>
    `;
  };
  c9c4s14Pick(0);
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🏊</span> Real-World Pool &amp; Land Area Dimension Solver
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Dimension Variable x (metres): <strong id="c9c4s15XVal" class="text-cyan-300">6 m</strong></span>
    <input type="range" id="c9c4s15X" min="2" max="15" value="6" oninput="c9c4s15Draw()" class="w-full accent-emerald-400 mt-1.5">
  </label>
  <div id="c9c4s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c4s15Draw = function(){
    const x = parseInt(document.getElementById('c9c4s15X').value);
    document.getElementById('c9c4s15XVal').textContent = `${x} m`;
    const area = x*x + 11*x + 28, width = x + 4, length = x + 7, perim = 4*x + 22;
    document.getElementById('c9c4s15Out').innerHTML = `
      <div class="text-cyan-300 font-bold">Park Pool Area = (x² + 11x + 28) m² | Known Width = (x + 4) m</div>
      <div class="font-mono">Factor Area: (x + 4)(x + 7) ⇒ Length = Area / Width = <strong class="text-emerald-300">(x + 7) m = ${length} m</strong></div>
      <div class="font-mono text-amber-300">At x = ${x}: Width = ${width} m, Length = ${length} m, Area = ${width}×${length} = ${area} m², Perimeter = ${perim} m</div>
    `;
  };
  c9c4s15Draw();
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>📚</span> Reference Atlas: All 11 Core Algebraic Identities of Chapter 4
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c4s16Filter('all')" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">All 11 Identities</button>
    <button type="button" onclick="c9c4s16Filter('quad')" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Quadratic (1–6)</button>
    <button type="button" onclick="c9c4s16Filter('cube')" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Cubic (7–11)</button>
  </div>
  <div id="c9c4s16Out" class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px] font-mono max-h-56 overflow-y-auto custom-scrollbar pr-1"></div>
</div>
<script>
(function(){
  const ids = [
    { id:1, cat:'quad', txt:'(a + b)² = a² + 2ab + b²', col:'cyan' },
    { id:2, cat:'quad', txt:'(a − b)² = a² − 2ab + b²', col:'cyan' },
    { id:3, cat:'quad', txt:'a² − b² = (a + b)(a − b)', col:'amber' },
    { id:4, cat:'quad', txt:'a² = (a + b)(a − b) + b² (Śhrīdharāchārya)', col:'amber' },
    { id:5, cat:'quad', txt:'(x + a)(x + b) = x² + (a + b)x + ab', col:'emerald' },
    { id:6, cat:'quad', txt:'(a + b + c)² = a² + b² + c² + 2ab + 2bc + 2ca', col:'emerald' },
    { id:7, cat:'cube', txt:'(a + b)³ = a³ + 3a²b + 3ab² + b³', col:'purple' },
    { id:8, cat:'cube', txt:'(a − b)³ = a³ − 3a²b + 3ab² − b³', col:'purple' },
    { id:9, cat:'cube', txt:'x³ − y³ = (x − y)(x² + xy + y²)', col:'rose' },
    { id:10, cat:'cube', txt:'x³ + y³ = (x + y)(x² − xy + y²)', col:'rose' },
    { id:11, cat:'cube', txt:'x³ + y³ + z³ − 3xyz = (x + y + z)(x² + y² + z² − xy − yz − zx)', col:'yellow' }
  ];
  window.c9c4s16Filter = function(cat){
    const list = cat==='all' ? ids : ids.filter(d => d.cat===cat);
    document.getElementById('c9c4s16Out').innerHTML = list.map(d => `
      <div class="p-2 rounded bg-slate-950 border border-slate-800 ${d.id===11?'sm:col-span-2':''}"><span class="text-${d.col}-300 font-bold">${d.id}.</span> ${d.txt}</div>
    `).join('');
  };
  c9c4s16Filter('all');
})();
</script>
"""
}
