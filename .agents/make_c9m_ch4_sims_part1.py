#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 4: Exploring Algebraic Identities
Part 1: Simulators 1 to 8
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔢</span> Consecutive Squares Invariant Explorer: (n−1)² + (n+1)² − 2n² = 2
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Middle Integer n: <strong id="c9c4s1NVal" class="text-cyan-300 text-sm">5</strong> (Consecutive trio: <span id="c9c4s1Trio" class="text-amber-300">4, 5, 6</span>)</span>
    <input type="range" id="c9c4s1N" min="2" max="25" value="5" oninput="c9c4s1Draw()" class="w-full accent-cyan-400 mt-1.5">
  </label>
  <svg id="c9c4s1Svg" viewBox="0 0 420 115" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c9c4s1Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 font-mono"></div>
</div>
<script>
(function(){
  window.c9c4s1Draw = function(){
    const n = parseInt(document.getElementById('c9c4s1N').value);
    const a = n - 1, c = n + 1;
    const sa = a*a, sn = n*n, sc = c*c;
    document.getElementById('c9c4s1NVal').textContent = n;
    document.getElementById('c9c4s1Trio').textContent = `${a}, ${n}, ${c}`;
    const maxS = sc;
    const wA = 16 + (sa/maxS)*95, wN = 16 + (sn/maxS)*95, wC = 16 + (sc/maxS)*95;
    let svg = `<rect x="20" y="${95-wA}" width="${wA}" height="${wA}" fill="#38bdf8" fill-opacity="0.28" stroke="#38bdf8" stroke-width="2"/>` +
              `<text x="${20+wA/2}" y="108" fill="#38bdf8" font-size="9" text-anchor="middle">(${a})²=${sa}</text>` +
              `<rect x="150" y="${95-wN}" width="${wN}" height="${wN}" fill="#fbbf24" fill-opacity="0.28" stroke="#fbbf24" stroke-width="2"/>` +
              `<text x="${150+wN/2}" y="108" fill="#fbbf24" font-size="9" text-anchor="middle">(${n})²=${sn}</text>` +
              `<rect x="280" y="${95-wC}" width="${wC}" height="${wC}" fill="#34d399" fill-opacity="0.28" stroke="#34d399" stroke-width="2"/>` +
              `<text x="${280+wC/2}" y="108" fill="#34d399" font-size="9" text-anchor="middle">(${c})²=${sc}</text>`;
    document.getElementById('c9c4s1Svg').innerHTML = svg;
    document.getElementById('c9c4s1Out').innerHTML = `
      <div>(${a})² + (${c})² − 2(${n})² = <span class="text-cyan-300">${sa}</span> + <span class="text-emerald-300">${sc}</span> − 2(<span class="text-amber-300">${sn}</span>) = ${sa+sc} − ${2*sn} = <strong class="text-white text-sm">2</strong></div>
      <div class="text-slate-400 mt-1">Algebraic proof: (n² − 2n + 1) + (n² + 2n + 1) − 2n² = 2 ALWAYS!</div>
    `;
  };
  c9c4s1Draw();
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🟨</span> Binomial Square Dissector (a + b)² &amp; Mental Squaring (43²)
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Part a: <strong id="c9c4s2AVal" class="text-cyan-300">40</strong></span>
      <input type="range" id="c9c4s2A" min="10" max="90" step="10" value="40" oninput="c9c4s2Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Part b: <strong id="c9c4s2BVal" class="text-amber-300">3</strong></span>
      <input type="range" id="c9c4s2B" min="1" max="9" value="3" oninput="c9c4s2Draw()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c4s2Svg" viewBox="0 0 150 150" class="w-36 h-36 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c4s2Out" class="flex-1 p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c4s2Draw = function(){
    const a = parseInt(document.getElementById('c9c4s2A').value);
    const b = parseInt(document.getElementById('c9c4s2B').value);
    document.getElementById('c9c4s2AVal').textContent = a;
    document.getElementById('c9c4s2BVal').textContent = b;
    const sum = a + b;
    const a2 = a*a, ab = a*b, b2 = b*b, tot = sum*sum;
    const sa = 75, sb = 32;
    const svg = `
      <rect x="20" y="20" width="${sa}" height="${sa}" fill="#0891b2" fill-opacity="0.35" stroke="#22d3ee" stroke-width="1.5"/>
      <text x="${20+sa/2}" y="${24+sa/2}" fill="#67e8f9" font-size="10" font-weight="bold" text-anchor="middle">a² = ${a2}</text>
      <rect x="${20+sa}" y="20" width="${sb}" height="${sa}" fill="#059669" fill-opacity="0.35" stroke="#34d399" stroke-width="1.5"/>
      <text x="${20+sa+sb/2}" y="${24+sa/2}" fill="#6ee7b7" font-size="8.5" text-anchor="middle">ab=${ab}</text>
      <rect x="20" y="${20+sa}" width="${sa}" height="${sb}" fill="#059669" fill-opacity="0.35" stroke="#34d399" stroke-width="1.5"/>
      <text x="${20+sa/2}" y="${24+sa+sb/2}" fill="#6ee7b7" font-size="9" text-anchor="middle">ab = ${ab}</text>
      <rect x="${20+sa}" y="${20+sa}" width="${sb}" height="${sb}" fill="#d97706" fill-opacity="0.4" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="${20+sa+sb/2}" y="${24+sa+sb/2}" fill="#fde68a" font-size="8.5" text-anchor="middle">b²=${b2}</text>
    `;
    document.getElementById('c9c4s2Svg').innerHTML = svg;
    document.getElementById('c9c4s2Out').innerHTML = `
      <div class="text-sm font-bold text-amber-300">(${a} + ${b})² = ${sum}² = <span class="text-white">${tot}</span></div>
      <div class="font-mono text-cyan-300">= ${a}² + 2(${a})(${b}) + ${b}² = ${a2} + ${2*ab} + ${b2} = ${tot}</div>
      <p class="text-slate-400">Notice the two rectangles <strong>2ab = ${2*ab}</strong> prevent the false shortcut a² + b² = ${a2 + b2}!</p>
    `;
  };
  c9c4s2Draw();
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-purple-300 flex items-center gap-2">
    <span>⚖️</span> Conditional Equation vs Universal Identity Live Tester
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Plug in Test Variable Value x = <strong id="c9c4s3XVal" class="text-cyan-300 text-sm">5</strong></span>
    <input type="range" id="c9c4s3X" min="-6" max="7" value="5" oninput="c9c4s3Draw()" class="w-full accent-purple-400 mt-1.5">
  </label>
  <div id="c9c4s3Out" class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs"></div>
</div>
<script>
(function(){
  window.c9c4s3Draw = function(){
    const x = parseInt(document.getElementById('c9c4s3X').value);
    document.getElementById('c9c4s3XVal').textContent = x;
    const eqL = x*x - 1, eqR = 24, eqTrue = eqL === eqR;
    const idL = (x + 3)*(x + 3), idR = x*x + 6*x + 9;
    document.getElementById('c9c4s3Out').innerHTML = `
      <div class="p-3.5 rounded-xl bg-slate-950 border ${eqTrue?'border-emerald-500/60':'border-rose-500/50'} space-y-1.5">
        <div class="font-bold text-rose-300">Conditional Equation: x² − 1 = 24</div>
        <div class="font-mono">LHS = (${x})² − 1 = <strong>${eqL}</strong> | RHS = <strong>${eqR}</strong></div>
        <div class="px-2 py-1 rounded font-bold inline-block ${eqTrue?'bg-emerald-500/20 text-emerald-300':'bg-rose-500/20 text-rose-300'}">${eqTrue ? 'TRUE ONLY AT x = ±5!' : 'FALSE AT x = ' + x}</div>
      </div>
      <div class="p-3.5 rounded-xl bg-slate-950 border border-emerald-500/60 space-y-1.5">
        <div class="font-bold text-emerald-300">Algebraic Identity: (x + 3)² = x² + 6x + 9</div>
        <div class="font-mono">LHS = (${x}+3)² = <strong>${idL}</strong> | RHS = <strong>${idR}</strong></div>
        <div class="px-2 py-1 rounded font-bold inline-block bg-emerald-500/20 text-emerald-300">ALWAYS TRUE FOR ALL x ∈ ℝ!</div>
      </div>
    `;
  };
  c9c4s3Draw();
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🔄</span> Perfect Square Reverse Factorizer &amp; Consecutive Pattern Prover
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c4s4Pick(0)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">9x² + 24x + 16</button>
    <button type="button" onclick="c9c4s4Pick(1)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">25x² − 30xy + 9y²</button>
    <button type="button" onclick="c9c4s4Pick(2)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">49a² + 14a + 1</button>
    <button type="button" onclick="c9c4s4Pick(3)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">Proof: (n−1)²+(n+1)²−2n²</button>
  </div>
  <div id="c9c4s4Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  const items = [
    { expr:'9x² + 24x + 16', a:'3x', b:'4', mid:'+2(3x)(4) = +24x', ans:'(3x + 4)²' },
    { expr:'25x² − 30xy + 9y²', a:'5x', b:'3y', mid:'−2(5x)(3y) = −30xy', ans:'(5x − 3y)²' },
    { expr:'49a² + 14a + 1', a:'7a', b:'1', mid:'+2(7a)(1) = +14a', ans:'(7a + 1)²' },
    { expr:'(n − 1)² + (n + 1)² − 2n²', a:'n² − 2n + 1', b:'n² + 2n + 1', mid:'(−2n + 2n = 0) & (2n² − 2n² = 0)', ans:'= 2 (Identically Constant!)' }
  ];
  window.c9c4s4Pick = function(i){
    const d = items[i];
    document.getElementById('c9c4s4Out').innerHTML = `
      <div class="text-cyan-300">Expression: ${d.expr}</div>
      <div class="text-amber-300">Components: ${d.a} &amp; ${d.b}</div>
      <div class="text-purple-300">Middle / Cancellation Check: ${d.mid}</div>
      <div class="text-emerald-300 font-bold text-sm">Factored / Proven Form: ${d.ans}</div>
    `;
  };
  c9c4s4Pick(0);
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-rose-300 flex items-center gap-2">
    <span>✂️</span> Border-Removal Geometry for (a − b)² = a² − 2ab + b²
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Big Side a: <strong id="c9c4s5AVal" class="text-cyan-300">10</strong></span>
      <input type="range" id="c9c4s5A" min="6" max="20" value="10" oninput="c9c4s5Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Cut Border b: <strong id="c9c4s5BVal" class="text-rose-300">2</strong></span>
      <input type="range" id="c9c4s5B" min="1" max="5" value="2" oninput="c9c4s5Draw()" class="w-full accent-rose-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c4s5Svg" viewBox="0 0 150 150" class="w-36 h-36 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c4s5Out" class="flex-1 p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c4s5Draw = function(){
    const a = parseInt(document.getElementById('c9c4s5A').value);
    const b = Math.min(a - 1, parseInt(document.getElementById('c9c4s5B').value));
    document.getElementById('c9c4s5AVal').textContent = a;
    document.getElementById('c9c4s5BVal').textContent = b;
    const rem = a - b;
    const sTot = 110, sB = Math.max(18, Math.round((b/a)*sTot)), sR = sTot - sB;
    const svg = `
      <rect x="20" y="20" width="${sR}" height="${sR}" fill="#059669" fill-opacity="0.35" stroke="#34d399" stroke-width="2"/>
      <text x="${20+sR/2}" y="${23+sR/2}" fill="#6ee7b7" font-size="9.5" font-weight="bold" text-anchor="middle">(a−b)²=${rem*rem}</text>
      <rect x="${20+sR}" y="20" width="${sB}" height="${sTot}" fill="#e11d48" fill-opacity="0.28" stroke="#fb7185" stroke-width="1.5"/>
      <text x="${20+sR+sB/2}" y="72" fill="#fda4af" font-size="8" text-anchor="middle">ab</text>
      <rect x="20" y="${20+sR}" width="${sR}" height="${sB}" fill="#d97706" fill-opacity="0.3" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="${20+sR/2}" y="${24+sR+sB/2}" fill="#fde68a" font-size="8" text-anchor="middle">b(a−b)=${b*rem}</text>
    `;
    document.getElementById('c9c4s5Svg').innerHTML = svg;
    document.getElementById('c9c4s5Out').innerHTML = `
      <div class="font-bold text-emerald-300">Target Square (${a} − ${b})² = ${rem}² = ${rem*rem}</div>
      <div class="font-mono text-cyan-300">Cut 1 (ab = ${a*b}) + Cut 2 (b(a−b) = ${b*rem}) = ${a*b + b*rem}</div>
      <div class="font-mono text-amber-300">Inclusion-Exclusion: a² − 2ab + b² = ${a*a} − ${2*a*b} + ${b*b} = ${rem*rem}</div>
    `;
  };
  c9c4s5Draw();
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧩</span> 3 × 3 Partitioned Trinomial Grid (a + b + c)²
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">a = <strong id="c9c4s6AVal" class="text-cyan-300">5</strong><input type="range" id="c9c4s6A" min="1" max="9" value="5" oninput="c9c4s6Draw()" class="w-full accent-cyan-400 mt-1"></label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">b = <strong id="c9c4s6BVal" class="text-emerald-300">3</strong><input type="range" id="c9c4s6B" min="1" max="9" value="3" oninput="c9c4s6Draw()" class="w-full accent-emerald-400 mt-1"></label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">c = <strong id="c9c4s6CVal" class="text-amber-300">2</strong><input type="range" id="c9c4s6C" min="1" max="9" value="2" oninput="c9c4s6Draw()" class="w-full accent-amber-400 mt-1"></label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c4s6Svg" viewBox="0 0 150 150" class="w-36 h-36 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c4s6Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c4s6Draw = function(){
    const a = parseInt(document.getElementById('c9c4s6A').value);
    const b = parseInt(document.getElementById('c9c4s6B').value);
    const c = parseInt(document.getElementById('c9c4s6C').value);
    document.getElementById('c9c4s6AVal').textContent = a;
    document.getElementById('c9c4s6BVal').textContent = b;
    document.getElementById('c9c4s6CVal').textContent = c;
    const vals = [a, b, c];
    const lbls = ['a', 'b', 'c'];
    const pos = [15, 65, 102, 135];
    let svg = '';
    for(let r=0;r<3;r++){
      for(let col=0;col<3;col++){
        const isDiag = r === col;
        const fill = isDiag ? '#0891b2' : '#7c3aed';
        const w = pos[col+1]-pos[col], h = pos[r+1]-pos[r];
        svg += `<rect x="${pos[col]}" y="${pos[r]}" width="${w}" height="${h}" fill="${fill}" fill-opacity="0.3" stroke="${isDiag?'#22d3ee':'#a78bfa'}" stroke-width="1"/>`;
        svg += `<text x="${pos[col]+w/2}" y="${pos[r]+h/2+3}" fill="#e2e8f0" font-size="8.5" text-anchor="middle">${vals[r]*vals[col]}</text>`;
      }
    }
    document.getElementById('c9c4s6Svg').innerHTML = svg;
    const sum = a+b+c;
    document.getElementById('c9c4s6Out').innerHTML = `
      <div class="font-bold text-cyan-300">(${a} + ${b} + ${c})² = ${sum}² = <span class="text-white">${sum*sum}</span></div>
      <div class="font-mono">3 Diagonal Squares: ${a*a} + ${b*b} + ${c*c} = ${a*a+b*b+c*c}</div>
      <div class="font-mono text-amber-300">6 Paired Rectangles: 2(${a*b}) + 2(${b*c}) + 2(${c*a}) = ${2*(a*b+b*c+c*a)}</div>
    `;
  };
  c9c4s6Draw();
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>⚡</span> Śhrīdharāchārya (750 CE) Squaring &amp; Difference of Squares Lab
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Number to Square a: <strong id="c9c4s7AVal" class="text-cyan-300">97</strong></span>
      <input type="range" id="c9c4s7A" min="15" max="99" value="97" oninput="c9c4s7Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Smart Shift b (to round base): <strong id="c9c4s7BVal" class="text-amber-300">3</strong></span>
      <input type="range" id="c9c4s7B" min="1" max="15" value="3" oninput="c9c4s7Draw()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <div id="c9c4s7Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  window.c9c4s7Draw = function(){
    const a = parseInt(document.getElementById('c9c4s7A').value);
    const b = parseInt(document.getElementById('c9c4s7B').value);
    document.getElementById('c9c4s7AVal').textContent = a;
    document.getElementById('c9c4s7BVal').textContent = b;
    const p1 = a + b, p2 = a - b, sqB = b*b, ans = p1*p2 + sqB;
    document.getElementById('c9c4s7Out').innerHTML = `
      <div class="text-cyan-300">Identity: a² = (a + b)(a − b) + b²</div>
      <div class="text-amber-300">${a}² = (${a} + ${b})(${a} − ${b}) + ${b}² = (${p1})(${p2}) + ${sqB}</div>
      <div class="text-emerald-300 font-bold text-sm">= ${p1*p2} + ${sqB} = ${ans}</div>
    `;
  };
  c9c4s7Draw();
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🧱</span> Concrete Algebra Tile Rectangle Factor Builder: (x + p)(x + q)
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Right Columns (p x-tiles): <strong id="c9c4s8PVal" class="text-cyan-300">3</strong></span>
      <input type="range" id="c9c4s8P" min="1" max="5" value="3" oninput="c9c4s8Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Bottom Rows (q x-tiles): <strong id="c9c4s8QVal" class="text-amber-300">4</strong></span>
      <input type="range" id="c9c4s8Q" min="1" max="5" value="4" oninput="c9c4s8Draw()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c4s8Svg" viewBox="0 0 175 175" class="w-40 h-40 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c4s8Out" class="flex-1 p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c4s8Draw = function(){
    const p = parseInt(document.getElementById('c9c4s8P').value);
    const q = parseInt(document.getElementById('c9c4s8Q').value);
    document.getElementById('c9c4s8PVal').textContent = p;
    document.getElementById('c9c4s8QVal').textContent = q;
    const xSz = 68, u = 14, ox = 18, oy = 18;
    let svg = `<rect x="${ox}" y="${oy}" width="${xSz}" height="${xSz}" fill="#0891b2" fill-opacity="0.35" stroke="#22d3ee" stroke-width="1.5"/>` +
              `<text x="${ox+xSz/2}" y="${oy+xSz/2+4}" fill="#67e8f9" font-size="11" font-weight="bold" text-anchor="middle">x²</text>`;
    for(let i=0;i<p;i++){
      svg += `<rect x="${ox+xSz+i*u}" y="${oy}" width="${u}" height="${xSz}" fill="#059669" fill-opacity="0.35" stroke="#34d399" stroke-width="1"/>`;
    }
    for(let j=0;j<q;j++){
      svg += `<rect x="${ox}" y="${oy+xSz+j*u}" width="${xSz}" height="${u}" fill="#059669" fill-opacity="0.35" stroke="#34d399" stroke-width="1"/>`;
    }
    for(let i=0;i<p;i++){
      for(let j=0;j<q;j++){
        svg += `<rect x="${ox+xSz+i*u}" y="${oy+xSz+j*u}" width="${u}" height="${u}" fill="#d97706" fill-opacity="0.4" stroke="#fbbf24" stroke-width="1"/>`;
      }
    }
    document.getElementById('c9c4s8Svg').innerHTML = svg;
    document.getElementById('c9c4s8Out').innerHTML = `
      <div class="text-sm font-bold text-emerald-300">Rectangle Dimensions: (x + ${p}) × (x + ${q})</div>
      <div class="font-mono text-cyan-300">Tiles Used: 1 x²-tile + (${p}+${q})=${p+q} x-tiles + (${p}×${q})=${p*q} unit tiles</div>
      <div class="font-bold text-white">Quadratic: x² + ${p+q}x + ${p*q}</div>
    `;
  };
  c9c4s8Draw();
})();
</script>
"""
}
