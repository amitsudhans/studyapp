#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 3: The World of Numbers
Part 2: Simulators 9 to 16
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🥧</span> Mādhava Infinite π Series &amp; Āryabhaṭa Rational Checker
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Mādhava Series Terms (N): <strong id="c9c3s9NVal" class="text-amber-300">25</strong></span>
      <input type="range" id="c9c3s9N" min="1" max="200" value="25" oninput="c9c3s9Draw()" class="w-full accent-amber-400 mt-1.5">
    </label>
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-1">
      <div class="text-cyan-300 font-semibold">Āryabhaṭa (499 CE) Rational Milestone</div>
      <div class="font-mono text-slate-300">62832 / 20000 = <strong class="text-emerald-300">3927/1250 = 3.1416</strong></div>
    </div>
  </div>
  <div id="c9c3s9Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c3s9Draw = function(){
    const N = parseInt(document.getElementById('c9c3s9N').value);
    document.getElementById('c9c3s9NVal').textContent = N;
    let sum = 0;
    const preview = [];
    for(let k=0;k<N;k++){
      const sign = k%2===0 ? 1 : -1;
      const denom = 2*k + 1;
      sum += sign / denom;
      if(k < 5) preview.push((k===0?'1':(sign>0?' + ':' − ') + '1/' + denom));
    }
    const approx = 4 * sum;
    const err = Math.abs(Math.PI - approx);
    document.getElementById('c9c3s9Out').innerHTML = `
      <div class="font-mono text-cyan-300">π ≈ 4 × (${preview.join('')}${N>5?' + ...':''})</div>
      <div class="grid grid-cols-3 gap-2 pt-1">
        <div class="p-2 rounded bg-slate-900 border border-slate-800">Series (${N} terms): <strong class="text-amber-300">${approx.toFixed(6)}</strong></div>
        <div class="p-2 rounded bg-slate-900 border border-slate-800">Exact π: <strong class="text-emerald-300">${Math.PI.toFixed(6)}...</strong></div>
        <div class="p-2 rounded bg-slate-900 border border-slate-800">|Error|: <strong class="text-rose-300">${err.toFixed(5)}</strong></div>
      </div>
      <p class="text-slate-400">Johann Lambert proved in 1761 that π is strictly irrational — its digits never terminate or cycle!</p>
    `;
  };
  c9c3s9Draw();
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔍</span> Denominator Prime-Factor Predictor (q = 2ᵐ · 5ⁿ)
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c3s10Pick(3,8)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">3/8</button>
    <button type="button" onclick="c9c3s10Pick(13,40)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">13/40</button>
    <button type="button" onclick="c9c3s10Pick(21,30)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">21/30 (check reduce!)</button>
    <button type="button" onclick="c9c3s10Pick(7,30)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">7/30</button>
    <button type="button" onclick="c9c3s10Pick(5,21)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">5/21</button>
  </div>
  <div id="c9c3s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  function gcd(a,b){ while(b){ const t=a%b; a=b; b=t; } return a; }
  function factors(n){
    const res = [];
    let d = 2, x = n;
    while(x > 1 && d*d <= x){
      while(x % d === 0){ res.push(d); x /= d; }
      d++;
    }
    if(x > 1) res.push(x);
    return res;
  }
  window.c9c3s10Pick = function(p, q){
    const g = gcd(p, q);
    const rp = p/g, rq = q/g;
    const pf = factors(rq);
    const term = pf.every(f => f === 2 || f === 5);
    const dec = (rp / rq).toFixed(6).replace(/0+$/, '');
    document.getElementById('c9c3s10Out').innerHTML = `
      <div class="flex flex-wrap justify-between items-center gap-2">
        <div>Input: <strong class="text-cyan-300">${p}/${q}</strong> → Reduced Co-Prime Form: <strong class="text-amber-300">${rp}/${rq}</strong></div>
        <span class="px-2.5 py-1 rounded font-bold ${term?'bg-emerald-500/20 text-emerald-300':'bg-rose-500/20 text-rose-300'}">${term?'TERMINATING DECIMAL':'NON-TERMINATING REPEATING'}</span>
      </div>
      <div>Prime factorization of reduced denominator ${rq}: <strong class="font-mono text-white">${pf.join(' × ') || '1'}</strong></div>
      <div class="text-slate-400">Decimal preview: <span class="font-mono text-cyan-300">${term ? rp/rq : (rp/rq).toFixed(8) + '...'}</span></div>
    `;
  };
  c9c3s10Pick(13, 40);
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-indigo-300 flex items-center gap-2">
    <span>🔄</span> Repeating Decimal → Exact p/q Algebraic Stepper
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c3s11Pick(0)" id="c9c3s11b0" class="px-2.5 py-1 rounded bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 font-semibold">Pure: 0.6̄</button>
    <button type="button" onclick="c9c3s11Pick(1)" id="c9c3s11b1" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Mixed: 0.16̄</button>
    <button type="button" onclick="c9c3s11Pick(2)" id="c9c3s11b2" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Mixed: 2.357̄</button>
    <button type="button" onclick="c9c3s11Pick(3)" id="c9c3s11b3" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Pure: 0.27̄ (2-digit)</button>
  </div>
  <div id="c9c3s11Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 font-mono"></div>
</div>
<script>
(function(){
  const cases = [
    { lbl:'x = 0.666...', s1:'10x = 6.666...', s2:'10x − x = 6', s3:'9x = 6 ⇒ x = 6/9 = 2/3' },
    { lbl:'x = 0.1666...', s1:'10x = 1.666... & 100x = 16.666...', s2:'100x − 10x = 16.6̄ − 1.6̄ = 15', s3:'90x = 15 ⇒ x = 15/90 = 1/6' },
    { lbl:'x = 2.35777...', s1:'100x = 235.777... & 1000x = 2357.777...', s2:'1000x − 100x = 2357.7̄ − 235.7̄ = 2122', s3:'900x = 2122 ⇒ x = 2122/900 = 1061/450' },
    { lbl:'x = 0.272727...', s1:'100x = 27.2727...', s2:'100x − x = 27', s3:'99x = 27 ⇒ x = 27/99 = 3/11' }
  ];
  window.c9c3s11Pick = function(i){
    [0,1,2,3].forEach(k => {
      const b = document.getElementById('c9c3s11b'+k);
      if(b) b.className = k===i ? 'px-2.5 py-1 rounded bg-indigo-500/20 text-indigo-300 border border-indigo-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    const d = cases[i];
    document.getElementById('c9c3s11Out').innerHTML = `
      <div class="text-cyan-300">1. Let ${d.lbl}</div>
      <div class="text-amber-300">2. Align bar tails: ${d.s1}</div>
      <div class="text-purple-300">3. Subtract to cancel tail: ${d.s2}</div>
      <div class="text-emerald-300 font-bold text-sm pt-1">4. Exact Rational Fraction: ${d.s3}</div>
    `;
  };
  c9c3s11Pick(0);
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🎡</span> Magic Cyclic Wheel of 1/7 (0.142857̄) Rotator
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Select Multiplier k (for k × 142857 &amp; k/7): <strong id="c9c3s12KVal" class="text-emerald-300 text-sm">k = 1</strong></span>
    <input type="range" id="c9c3s12K" min="1" max="7" value="1" oninput="c9c3s12Draw()" class="w-full accent-emerald-400 mt-1.5">
  </label>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c3s12Svg" viewBox="0 0 150 150" class="w-36 h-36 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c3s12Out" class="flex-1 p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2 w-full"></div>
  </div>
</div>
<script>
(function(){
  const ring = [1, 4, 2, 8, 5, 7];
  const starts = { 1:0, 3:1, 2:2, 6:3, 4:4, 5:5 };
  window.c9c3s12Draw = function(){
    const k = parseInt(document.getElementById('c9c3s12K').value);
    document.getElementById('c9c3s12KVal').textContent = `k = ${k}`;
    const startIdx = starts[k] !== undefined ? starts[k] : 0;
    let svg = `<circle cx="75" cy="75" r="46" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="4 3"/>`;
    ring.forEach((digit, idx) => {
      const ang = -Math.PI/2 + idx * (Math.PI/3);
      const x = 75 + 46 * Math.cos(ang), y = 75 + 46 * Math.sin(ang);
      const active = k <= 6 && idx === startIdx;
      svg += `<circle cx="${x}" cy="${y}" r="13" fill="${active?'#10b981':'#0f172a'}" stroke="${active?'#6ee7b7':'#38bdf8'}" stroke-width="2"/>`;
      svg += `<text x="${x}" y="${y+4}" fill="${active?'#022c22':'#e2e8f0'}" font-size="11" font-weight="bold" text-anchor="middle">${digit}</text>`;
    });
    document.getElementById('c9c3s12Svg').innerHTML = svg;
    const prod = k * 142857;
    document.getElementById('c9c3s12Out').innerHTML = k <= 6
      ? `<div class="text-sm font-bold text-emerald-300 font-mono">${k} × 142857 = ${prod}</div>
         <div class="font-mono text-cyan-300">${k}/7 = 0.${String(prod).padStart(6,'0')}... (cyclic bar!)</div>
         <p class="text-slate-400">Same circular sequence <strong class="text-white">1 → 4 → 2 → 8 → 5 → 7</strong> starting at digit <strong class="text-emerald-300">${ring[startIdx]}</strong>!</p>`
      : `<div class="text-sm font-bold text-amber-300 font-mono">7 × 142857 = 999999!</div>
         <div class="font-mono text-cyan-300">7/7 = 0.999999... = 1</div>
         <p class="text-slate-400">Completing the full divisor loop yields all nines (0.9̄ = 1)!</p>`;
  };
  c9c3s12Draw();
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-rose-300 flex items-center gap-2">
    <span>♾️</span> Rational Clockwork vs Irrational Decimal Chaos Comparator
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c3s13Pick(0)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">√2 (Irrational)</button>
    <button type="button" onclick="c9c3s13Pick(1)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">π (Irrational)</button>
    <button type="button" onclick="c9c3s13Pick(2)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">0.1010010001... (Constructed)</button>
    <button type="button" onclick="c9c3s13Pick(3)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">1/7 = 0.142857̄ (Rational Contrast)</button>
  </div>
  <div id="c9c3s13Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const list = [
    { name:'√2 ≈ 1.414213562373095048801688724209698...', type:'Irrational ℝ \\ ℚ', why:'Non-terminating & NEVER periodically repeating across billions of computed digits.' },
    { name:'π ≈ 3.141592653589793238462643383279502...', type:'Irrational ℝ \\ ℚ', why:'Lambert proved irrational; trillions of digits show zero repeating period block.' },
    { name:'0.1010010001000010000010000001...', type:'Irrational (Constructed)', why:'Number of zeros between 1s increases (+1, +2, +3, +4...), making fixed-period repetition mathematically impossible.' },
    { name:'1/7 = 0.142857142857142857142857...', type:'Rational ℚ (Period 6)', why:'Even though infinite, exact 6-digit block 142857 repeats cleanly forever!' }
  ];
  window.c9c3s13Pick = function(i){
    const d = list[i];
    const irr = i < 3;
    document.getElementById('c9c3s13Out').innerHTML = `
      <div class="flex justify-between items-center">
        <strong class="${irr?'text-rose-300':'text-emerald-300'}">${d.type}</strong>
        <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-400">Infinite Digit Stream</span>
      </div>
      <div class="p-2 rounded bg-slate-900 font-mono text-cyan-300 break-all">${d.name}</div>
      <p>${d.why}</p>
    `;
  };
  c9c3s13Pick(2);
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-purple-300 flex items-center gap-2">
    <span>🌌</span> Nested Number Universe (ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ) &amp; Imaginary Frontier i
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c3s14Pick(0)" class="px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40">ℕ (Counting)</button>
    <button type="button" onclick="c9c3s14Pick(1)" class="px-2.5 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">ℤ (Integers)</button>
    <button type="button" onclick="c9c3s14Pick(2)" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40">ℚ (Rationals)</button>
    <button type="button" onclick="c9c3s14Pick(3)" class="px-2.5 py-1 rounded bg-rose-500/20 text-rose-300 border border-rose-500/40">ℝ (Real Line)</button>
    <button type="button" onclick="c9c3s14Pick(4)" class="px-2.5 py-1 rounded bg-purple-500/20 text-purple-300 border border-purple-500/40">i = √(−1) Frontier</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg viewBox="0 0 180 120" class="w-44 h-28 bg-slate-950 rounded-xl border border-slate-800 shrink-0">
      <rect x="8" y="8" width="164" height="104" rx="14" fill="#e11d48" fill-opacity="0.14" stroke="#fb7185" stroke-width="1.5"/>
      <rect x="20" y="18" width="140" height="84" rx="12" fill="#d97706" fill-opacity="0.16" stroke="#fbbf24" stroke-width="1.5"/>
      <rect x="34" y="28" width="112" height="64" rx="10" fill="#059669" fill-opacity="0.18" stroke="#34d399" stroke-width="1.5"/>
      <rect x="52" y="40" width="76" height="40" rx="8" fill="#0891b2" fill-opacity="0.25" stroke="#22d3ee" stroke-width="1.5"/>
      <text x="90" y="64" fill="#cffafe" font-size="11" font-weight="bold" text-anchor="middle">ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ</text>
    </svg>
    <div id="c9c3s14Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 w-full"></div>
  </div>
</div>
<script>
(function(){
  const info = [
    { t:'Natural Numbers ℕ = {1, 2, 3, ...}', e:'Origin: Counting livestock, tallies.', b:'Cannot solve x + 5 = 2 inside ℕ!' },
    { t:'Integers ℤ = {..., -2, -1, 0, 1, 2, ...}', e:'Includes Śhūnya (0) & Riṇa Debts (−).', b:'Cannot solve 3x = 2 inside ℤ!' },
    { t:'Rational Numbers ℚ = {p/q : q ≠ 0}', e:'Dense fractions & repeating decimals.', b:'Cannot solve x² = 2 inside ℚ!' },
    { t:'Real Numbers ℝ = ℚ ∪ Irrationals', e:'Continuous line covering √2, √5, π.', b:'Cannot solve x² + 1 = 0 inside ℝ!' },
    { t:'Imaginary Unit i = √(−1)', e:'Since r² ≥ 0 for all r ∈ ℝ, solving x² = −1 launches Complex Numbers a + bi!', b:'Next Mathematical Horizon beyond ℝ.' }
  ];
  window.c9c3s14Pick = function(i){
    const d = info[i];
    document.getElementById('c9c3s14Out').innerHTML = `
      <div class="font-bold text-cyan-300 text-sm">${d.t}</div>
      <p class="mt-1">${d.e}</p>
      <p class="mt-1 text-amber-300 font-semibold">Equation Barrier: ${d.b}</p>
    `;
  };
  c9c3s14Pick(0);
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🌀</span> Radical Identity Canceller (√a + √b)(√a − √b) &amp; √5 Spiral Lab
  </h3>
  <div class="grid grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Parameter a: <strong id="c9c3s15AVal" class="text-cyan-300">7</strong></span>
      <input type="range" id="c9c3s15A" min="2" max="15" value="7" oninput="c9c3s15Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Parameter b: <strong id="c9c3s15BVal" class="text-amber-300">3</strong></span>
      <input type="range" id="c9c3s15B" min="1" max="12" value="3" oninput="c9c3s15Draw()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <div id="c9c3s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c3s15Draw = function(){
    const a = parseInt(document.getElementById('c9c3s15A').value);
    const b = parseInt(document.getElementById('c9c3s15B').value);
    document.getElementById('c9c3s15AVal').textContent = a;
    document.getElementById('c9c3s15BVal').textContent = b;
    const sumSq = a + b, prod = a * b, diff = a - b;
    document.getElementById('c9c3s15Out').innerHTML = `
      <div class="p-2 rounded bg-slate-900 border border-slate-800 font-mono">
        (√${a} + √${b})(√${a} − √${b}) = (√${a})² − (√${b})² = ${a} − ${b} = <strong class="text-emerald-300 text-sm">${diff}</strong> (Pure Rational Integer!)
      </div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800 font-mono">
        (√${a} + √${b})² = ${a} + 2√(${prod}) + ${b} = <strong class="text-amber-300">${sumSq} + 2√${prod}</strong>
      </div>
      <div class="text-slate-400">√5 Contradiction Recap: If √5 = p/q ⇒ p² = 5q² ⇒ prime 5 divides both p &amp; q, contradicting co-prime lowest terms!</div>
    `;
  };
  c9c3s15Draw();
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🏆</span> Chapter 3 Complete Number Classifier &amp; Milestone Matrix
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9c3s16Pick(0)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">13/40</button>
    <button type="button" onclick="c9c3s16Pick(1)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">0.142857̄</button>
    <button type="button" onclick="c9c3s16Pick(2)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">-√9</button>
    <button type="button" onclick="c9c3s16Pick(3)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">√5</button>
    <button type="button" onclick="c9c3s16Pick(4)" class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700">3927/1250</button>
  </div>
  <div id="c9c3s16Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  const items = [
    { v:'13/40', sets:'ℚ, ℝ', dec:'Terminating (40 = 2³·5) = 0.325', hist:'Reduced denominator prime factors strictly 2 & 5.' },
    { v:'0.142857̄', sets:'ℚ, ℝ', dec:'Non-terminating cyclic repeating (= 1/7)', hist:'Multiples 1..6 cyclically permute digits 1-4-2-8-5-7.' },
    { v:'-√9 = -3', sets:'ℤ, ℚ, ℝ', dec:'Terminating exact negative integer -3', hist:'Wait for the trap! √9 simplifies to 3; −3 ∈ ℤ (Riṇa debt).' },
    { v:'√5', sets:'Irrational (ℝ \\ ℚ)', dec:'2.2360679... (Non-terminating non-repeating)', hist:'Constructible via legs 2 & 1; irrational by prime-5 contradiction.' },
    { v:'3927/1250', sets:'ℚ, ℝ', dec:'Terminating = 3.1416 (1250 = 2¹·5⁴)', hist:'Āryabhaṭa (499 CE) rational approximation for irrational π!' }
  ];
  window.c9c3s16Pick = function(i){
    const d = items[i];
    document.getElementById('c9c3s16Out').innerHTML = `
      <div class="text-sm font-bold text-cyan-300">Value: ${d.v}</div>
      <div>Belongs to Sets: <strong class="text-emerald-300">${d.sets}</strong></div>
      <div>Decimal Type: <strong class="text-amber-300">${d.dec}</strong></div>
      <div class="text-slate-400">Milestone Note: ${d.hist}</div>
    `;
  };
  c9c3s16Pick(0);
})();
</script>
"""
}
