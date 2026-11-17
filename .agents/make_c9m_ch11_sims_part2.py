#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 11: The World of Algorithms
Part 2: Simulators 9 to 16 (Slides 9 to 16)
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📈</span> Numerical Value (10<sup>d</sup>) vs Digit Count (d) Scaling Explorer
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Input Digit Length (d):</span>
      <span id="c9c11s9DLbl" class="text-amber-300 font-bold">d = 9 digits</span>
    </div>
    <input id="c9c11s9D" type="range" min="2" max="15" value="9" oninput="c9c11s9Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c11s9Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c11s9Draw = function(){
    const d = parseInt(document.getElementById('c9c11s9D').value, 10);
    document.getElementById('c9c11s9DLbl').textContent = 'd = ' + d + ' digits';
    const valScan = Math.pow(10, d).toLocaleString();
    const modSteps = 5 * d;
    document.getElementById('c9c11s9Out').innerHTML = `
      <div><strong>1-to-min(m,n) Linear Value Scan:</strong> <span class="text-rose-400 font-bold">~${valScan} operations</span></div>
      <div><strong>Digit-Scaling (Āryabhaṭa Division):</strong> <span class="text-emerald-300 font-bold">≤ ${modSteps} operations</span></div>
      <div class="text-cyan-300">Adding 1 digit multiplies value-scan time by 10×, while digit-scaling adds only ~5 steps!</div>
    `;
  };
  setTimeout(window.c9c11s9Draw, 40);
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📐</span> Euclid Subtraction &amp; Block-Tiling Tracer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">m:</span><input id="c9c11s10M" type="number" min="1" max="500" value="24" oninput="c9c11s10Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">n:</span><input id="c9c11s10N" type="number" min="1" max="500" value="9" oninput="c9c11s10Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c11s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c11s10Draw = function(){
    let a = Math.max(1, Math.min(500, parseInt(document.getElementById('c9c11s10M').value || '1', 10)));
    let b = Math.max(1, Math.min(500, parseInt(document.getElementById('c9c11s10N').value || '1', 10)));
    const trace = [`(${a}, ${b})`];
    let steps = 0;
    while(a !== b && steps < 120){
      if(a > b) a -= b; else b -= a;
      trace.push(`(${a}, ${b})`);
      steps++;
    }
    document.getElementById('c9c11s10Out').innerHTML = `
      <div class="font-bold text-emerald-300">GCD = ${a} in ${steps} subtractions</div>
      <div class="text-slate-300 break-words">Trace: ${trace.slice(0, 14).join(' → ')}${trace.length > 14 ? ' → ...' : ''}</div>
    `;
  };
  setTimeout(window.c9c11s10Draw, 40);
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚡</span> Āryabhaṭa Division vs Euclid Subtraction Race
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">m:</span><input id="c9c11s11M" type="number" min="1" max="1000000" value="20001" oninput="c9c11s11Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">n:</span><input id="c9c11s11N" type="number" min="1" max="1000000" value="2" oninput="c9c11s11Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c11s11Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c11s11Draw = function(){
    const m = Math.max(1, parseInt(document.getElementById('c9c11s11M').value || '1', 10));
    const n = Math.max(1, parseInt(document.getElementById('c9c11s11N').value || '1', 10));
    let a = m, b = n, modSteps = 0;
    const trace = [`(${a}, ${b})`];
    while(b !== 0){
      const r = a % b;
      a = b; b = r;
      trace.push(`(${a}, ${b})`);
      modSteps++;
    }
    let sa = m, sb = n, subSteps = 0;
    while(sa !== sb && subSteps < 2000000){
      if(sa > sb){ const q = Math.floor((sa - sb) / sb) || 1; sa -= q*sb; subSteps += q; }
      else { const q = Math.floor((sb - sa) / sa) || 1; sb -= q*sa; subSteps += q; }
    }
    document.getElementById('c9c11s11Out').innerHTML = `
      <div class="font-bold text-emerald-300">Āryabhaṭa Division: GCD = ${a} in ${modSteps} steps!</div>
      <div>Euclid Subtraction: <strong class="text-rose-400">${subSteps.toLocaleString()} steps</strong></div>
      <div class="text-cyan-300">Modulo Trace: ${trace.join(' → ')}</div>
    `;
  };
  setTimeout(window.c9c11s11Draw, 40);
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📜</span> Historical Algorithm Timeline &amp; Etymology Explorer
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c11s12Show('euc')" class="px-3 py-1.5 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 border border-cyan-500/40 text-cyan-200 font-bold">c. 300 BCE: Euclid</button>
    <button onclick="c9c11s12Show('ary')" class="px-3 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-200 font-bold">499 CE: Āryabhaṭa</button>
    <button onclick="c9c11s12Show('alk')" class="px-3 py-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 border border-amber-500/40 text-amber-200 font-bold">c. 825 CE: Al-Khwārizmī</button>
  </div>
  <div id="c9c11s12Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const era = {
    euc: ['Euclid (Elements, c. 300 BCE)', 'Formulated geometric subtraction reduction gcd(m, n) = gcd(n, m − n) via line/tile measurement.'],
    ary: ['Āryabhaṭa (Āryabhaṭīya, 499 CE)', 'Presented the remainder-based division GCD / kuttaka algorithm scaling proportionally to digit count!'],
    alk: ['Al-Khwārizmī (Baghdad, c. 825 CE)', 'Explained Indian base-10 numerals and place-value arithmetic; Latinized as "Liber Algorismi", giving us the word "algorithm"!']
  };
  window.c9c11s12Show = function(k){
    const [t, d] = era[k];
    document.getElementById('c9c11s12Out').innerHTML = `<div class="font-bold text-cyan-300">${t}</div><div>${d}</div>`;
  };
  setTimeout(function(){ window.c9c11s12Show('alk'); }, 40);
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔁</span> Reverse Early-Exit GCD &amp; Fast LCM Calculator
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">m:</span><input id="c9c11s13M" type="number" min="1" max="10000" value="24" oninput="c9c11s13Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">n:</span><input id="c9c11s13N" type="number" min="1" max="10000" value="36" oninput="c9c11s13Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c11s13Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  function g(a,b){ while(b){ [a,b]=[b,a%b]; } return a; }
  window.c9c11s13Draw = function(){
    const m = Math.max(1, parseInt(document.getElementById('c9c11s13M').value || '1', 10));
    const n = Math.max(1, parseInt(document.getElementById('c9c11s13N').value || '1', 10));
    const d = g(m, n);
    const lcm = (m / d) * n;
    const revChecks = Math.min(m, n) - d + 1;
    document.getElementById('c9c11s13Out').innerHTML = `
      <div class="font-bold text-emerald-300">gcd(${m}, ${n}) = ${d} &nbsp;|&nbsp; lcm(${m}, ${n}) = (${m}/${d}) × ${n} = ${lcm}</div>
      <div>Reverse downward scan from ${Math.min(m,n)} hits ${d} in ${revChecks} checks (worst-case if gcd = 1).</div>
    `;
  };
  setTimeout(window.c9c11s13Draw, 40);
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔬</span> prime(n) Trial Division (2..n−1 vs 2..√n) Simulator
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Test Integer n (2 to 10,000):</span>
    <input id="c9c11s14N" type="number" min="2" max="10000" value="197" oninput="c9c11s14Draw()" class="w-full mt-1.5 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
  </label>
  <div id="c9c11s14Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c11s14Draw = function(){
    const n = Math.max(2, parseInt(document.getElementById('c9c11s14N').value || '2', 10));
    const lim = Math.floor(Math.sqrt(n));
    let factor = null, checks = 0;
    for(let d = 2; d <= lim; d++){
      checks++;
      if(n % d === 0){ factor = d; break; }
    }
    document.getElementById('c9c11s14Out').innerHTML = `
      <div class="font-bold ${factor ? 'text-rose-400' : 'text-emerald-300'} text-sm">
        ${factor ? `COMPOSITE: ${n} = ${factor} × ${n/factor}` : `PRIME! No factor found up to ⌊√${n}⌋ = ${lim}`}
      </div>
      <div>Optimized √n checks performed: <strong>${checks}</strong> (vs up to ${n - 2} naive checks!)</div>
    `;
  };
  setTimeout(window.c9c11s14Draw, 40);
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📋</span> Āryabhaṭa Modulo Step-by-Step Table Builder
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">m:</span><input id="c9c11s15M" type="number" min="1" max="100000" value="1071" oninput="c9c11s15Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">n:</span><input id="c9c11s15N" type="number" min="1" max="100000" value="462" oninput="c9c11s15Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c11s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c11s15Draw = function(){
    let a = Math.max(1, parseInt(document.getElementById('c9c11s15M').value || '1', 10));
    let b = Math.max(1, parseInt(document.getElementById('c9c11s15N').value || '1', 10));
    const rows = [];
    let step = 1;
    while(b !== 0){
      const q = Math.floor(a / b), r = a % b;
      rows.push(`Step ${step++}: ${a} = ${q} × ${b} + <strong>${r}</strong> &nbsp;⇒&nbsp; (${b}, ${r})`);
      a = b; b = r;
    }
    document.getElementById('c9c11s15Out').innerHTML = `
      <div class="font-bold text-emerald-300">Returned GCD = ${a} (Terminated at remainder 0!)</div>
      <div class="space-y-0.5">${rows.join('<br>')}</div>
    `;
  };
  setTimeout(window.c9c11s15Draw, 40);
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📚</span> Chapter 11 Algorithm Complexity &amp; Correctness Matrix
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c11s16Show('scale')" class="px-3 py-1.5 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 border border-cyan-500/40 text-cyan-200 font-bold">Scaling Comparison</button>
    <button onclick="c9c11s16Show('proof')" class="px-3 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-200 font-bold">Correctness Checklist</button>
  </div>
  <div id="c9c11s16Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const cards = {
    scale: `<div class="font-bold text-cyan-300 text-sm">Algorithm Scaling Summary</div>
      <ul class="list-disc pl-4 space-y-1">
        <li><strong>Digit-Count Scaling O(d):</strong> Base-10 Column Addition, Āryabhaṭa's Division GCD</li>
        <li><strong>Root Scaling O(√n):</strong> Optimized prime(n) checking d = 2..⌊√n⌋</li>
        <li><strong>Value-Magnitude Scaling O(10^d):</strong> Dot counting, 1-to-min(m,n) GCD scan, Euclid subtraction on (2k+1, 2)</li>
      </ul>`,
    proof: `<div class="font-bold text-emerald-300 text-sm">Formal Proof of Correctness</div>
      <ul class="list-disc pl-4 space-y-1">
        <li><strong>1. Termination:</strong> Loop counter or non-negative remainder strictly approaches stopping condition (r = 0)</li>
        <li><strong>2. Loop Invariant:</strong> gcd(m, n) = gcd(n, m mod n) holds at every iteration</li>
        <li><strong>3. Base Case:</strong> gcd(d, 0) = d returns the exact invariant value!</li>
      </ul>`
  };
  window.c9c11s16Show = function(k){
    document.getElementById('c9c11s16Out').innerHTML = cards[k] || cards.scale;
  };
  setTimeout(function(){ window.c9c11s16Show('scale'); }, 40);
})();
</script>
"""
}
