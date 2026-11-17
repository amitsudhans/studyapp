#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 11: The World of Algorithms
Part 1: Simulators 1 to 8 (Slides 1 to 8)
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚡</span> Dot Counting vs Place-Value Addition Step Counter
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Number of Decimal Digits (d):</span>
      <span id="c9c11s1DLbl" class="text-amber-300 font-bold">d = 6 digits</span>
    </div>
    <input id="c9c11s1D" type="range" min="1" max="10" value="6" oninput="c9c11s1Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c11s1Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c11s1Draw = function(){
    const d = parseInt(document.getElementById('c9c11s1D').value, 10);
    document.getElementById('c9c11s1DLbl').textContent = 'd = ' + d + ' digits';
    const dotSteps = Math.pow(10, d).toLocaleString();
    document.getElementById('c9c11s1Out').innerHTML = `
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
        <div class="p-2.5 rounded-lg bg-rose-500/10 border border-rose-500/30"><span class="text-[10px] uppercase text-rose-300 font-bold block">Primitive Dot Counting</span><strong class="text-white text-sm">~${dotSteps} steps</strong></div>
        <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30"><span class="text-[10px] uppercase text-emerald-300 font-bold block">Base-10 Column Addition</span><strong class="text-white text-sm">${d} column steps</strong></div>
      </div>
      <div class="text-cyan-300">Place-value scales linearly with digit count <strong>d</strong> rather than exponential magnitude 10<sup>d</sup>!</div>
    `;
  };
  setTimeout(window.c9c11s1Draw, 40);
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>➕</span> 5-Step Column Addition Tracer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">First Integer (a):</span><input id="c9c11s2A" type="number" min="1" max="99999" value="786" oninput="c9c11s2Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Second Integer (b):</span><input id="c9c11s2B" type="number" min="1" max="99999" value="459" oninput="c9c11s2Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c11s2Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c11s2Draw = function(){
    const a = String(Math.max(0, parseInt(document.getElementById('c9c11s2A').value || '0', 10)));
    const b = String(Math.max(0, parseInt(document.getElementById('c9c11s2B').value || '0', 10)));
    const len = Math.max(a.length, b.length);
    const pa = a.padStart(len, '0'), pb = b.padStart(len, '0');
    let carry = 0;
    const cols = [];
    for(let i = len - 1; i >= 0; i--){
      const da = Number(pa[i]), db = Number(pb[i]);
      const s = da + db + carry;
      const wr = s % 10;
      const nc = s >= 10 ? 1 : 0;
      cols.push(`Col ${len - i}: ${da}+${db}+c(${carry})=${s} → write <strong>${wr}</strong>, carry=${nc}`);
      carry = nc;
    }
    const sum = Number(a) + Number(b);
    document.getElementById('c9c11s2Out').innerHTML = `
      <div class="font-bold text-emerald-300 text-sm">${a} + ${b} = ${sum} (Zero-padded: ${pa} + ${pb})</div>
      <div class="text-slate-300 space-y-0.5">${cols.join('<br>')}</div>
    `;
  };
  setTimeout(window.c9c11s2Draw, 40);
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧩</span> GCD Problem Decomposition Explorer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Integer m (1 to 100):</span><input id="c9c11s3M" type="number" min="1" max="100" value="24" oninput="c9c11s3Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Integer n (1 to 100):</span><input id="c9c11s3N" type="number" min="1" max="100" value="36" oninput="c9c11s3Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c11s3Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  function divs(k){ const r=[]; for(let i=1;i<=k;i++) if(k%i===0) r.push(i); return r; }
  window.c9c11s3Draw = function(){
    const m = Math.max(1, Math.min(100, parseInt(document.getElementById('c9c11s3M').value || '1', 10)));
    const n = Math.max(1, Math.min(100, parseInt(document.getElementById('c9c11s3N').value || '1', 10)));
    const dm = divs(m), dn = divs(n);
    const comm = dm.filter(x => dn.includes(x));
    document.getElementById('c9c11s3Out').innerHTML = `
      <div><strong>1. D<sub>${m}</sub>:</strong> [${dm.join(', ')}]</div>
      <div><strong>2. D<sub>${n}</sub>:</strong> [${dn.join(', ')}]</div>
      <div><strong>3. Common List C:</strong> [${comm.join(', ')}] &nbsp;⇒&nbsp; <strong class="text-emerald-300">GCD = ${comm[comm.length-1]}</strong></div>
    `;
  };
  setTimeout(window.c9c11s3Draw, 40);
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📋</span> Ordered Divisor Generator (1 to n)
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Target Positive Integer (n):</span>
      <span id="c9c11s4NLbl" class="text-amber-300 font-bold">n = 12</span>
    </div>
    <input id="c9c11s4N" type="range" min="2" max="36" value="12" oninput="c9c11s4Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c11s4Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c11s4Draw = function(){
    const n = parseInt(document.getElementById('c9c11s4N').value, 10);
    document.getElementById('c9c11s4NLbl').textContent = 'n = ' + n;
    const cells = [], list = [];
    for(let i = 1; i <= n; i++){
      const ok = n % i === 0;
      if(ok) list.push(i);
      cells.push(`<span class="px-1.5 py-0.5 rounded text-[11px] border ${ok ? 'bg-emerald-500/20 border-emerald-400 text-emerald-200 font-bold' : 'bg-slate-900 border-slate-800 text-slate-500'}">${i}</span>`);
    }
    document.getElementById('c9c11s4Out').innerHTML = `
      <div class="flex flex-wrap gap-1">${cells.join('')}</div>
      <div class="text-cyan-300 font-bold">Ordered Divisors D = [${list.join(', ')}] (${n} remainder checks performed)</div>
    `;
  };
  setTimeout(window.c9c11s4Draw, 40);
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔎</span> Two-List Common Divisor Matcher
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Scan Direction on Sorted List A:</span>
    <select id="c9c11s5Dir" onchange="c9c11s5Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
      <option value="rtl">Right-to-Left (Largest to Smallest — Early Exit!)</option>
      <option value="ltr">Left-to-Right (Smallest to Largest — Full Scan)</option>
    </select>
  </label>
  <div id="c9c11s5Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const A = [1, 2, 3, 6, 9, 18], B = [1, 2, 3, 4, 6, 8, 12, 24];
  window.c9c11s5Draw = function(){
    const dir = document.getElementById('c9c11s5Dir').value;
    if(dir === 'rtl'){
      document.getElementById('c9c11s5Out').innerHTML = `
        <div><strong>List A (18):</strong> [1, 2, 3, 6, 9, 18] &nbsp;|&nbsp; <strong>List B (24):</strong> [1, 2, 3, 4, 6, 8, 12, 24]</div>
        <div class="text-emerald-300 font-bold">Right-to-Left Check: 18 (no) → 9 (no) → 6 (MATCH! Stop immediately ⇒ GCD = 6 in 3 checks!)</div>
      `;
    } else {
      document.getElementById('c9c11s5Out').innerHTML = `
        <div><strong>List A (18):</strong> [1, 2, 3, 6, 9, 18] &nbsp;|&nbsp; <strong>List B (24):</strong> [1, 2, 3, 4, 6, 8, 12, 24]</div>
        <div class="text-amber-300 font-bold">Left-to-Right Check: Builds C = [1, 2, 3, 6] across all 6 elements of A, then picks last element 6.</div>
      `;
    }
  };
  setTimeout(window.c9c11s5Draw, 40);
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧮</span> Naive Two-List GCD Step-Count Visualizer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">m:</span><input id="c9c11s6M" type="number" min="1" max="10000" value="120" oninput="c9c11s6Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">n:</span><input id="c9c11s6N" type="number" min="1" max="10000" value="180" oninput="c9c11s6Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c11s6Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  function g(a,b){ while(b){ [a,b]=[b,a%b]; } return a; }
  window.c9c11s6Draw = function(){
    const m = Math.max(1, parseInt(document.getElementById('c9c11s6M').value || '1', 10));
    const n = Math.max(1, parseInt(document.getElementById('c9c11s6N').value || '1', 10));
    document.getElementById('c9c11s6Out').innerHTML = `
      <div class="font-bold text-emerald-300">gcd(${m}, ${n}) = ${g(m, n)}</div>
      <div>Naive Two-List Divisor Checks = m + n = <strong class="text-rose-400">${m + n} checks</strong> (plus list comparison)!</div>
    `;
  };
  setTimeout(window.c9c11s6Draw, 40);
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>💾</span> Data Structure Memory Comparison
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c11s7Show('3lists')" class="px-3 py-1.5 rounded-lg bg-rose-600/30 hover:bg-rose-600/50 border border-rose-500/40 text-rose-200 font-bold">3 Ordered Lists</button>
    <button onclick="c9c11s7Show('1list')" class="px-3 py-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 border border-amber-500/40 text-amber-200 font-bold">1 Common List</button>
    <button onclick="c9c11s7Show('1var')" class="px-3 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-200 font-bold">1 Variable (best_gcd)</button>
  </div>
  <div id="c9c11s7Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const info = {
    '3lists': ['Naive Approach: D_m, D_n, and C', 'Stores all divisors of m, all divisors of n, and all common divisors in memory.'],
    '1list': ['Stage 2 Approach: Single Common List C', 'Drops D_m and D_n; only stores common divisors up to min(m, n).'],
    '1var': ['Stage 3 Approach: Single Integer Variable best_gcd', 'Zero lists! Uses constant O(1) memory regardless of how large m and n are!']
  };
  window.c9c11s7Show = function(k){
    const [t, d] = info[k];
    document.getElementById('c9c11s7Out').innerHTML = `<div class="font-bold text-cyan-300">${t}</div><div>${d}</div>`;
  };
  setTimeout(function(){ window.c9c11s7Show('1var'); }, 40);
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🚀</span> 3-Stage GCD Optimization Benchmark
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">m:</span><input id="c9c11s8M" type="number" min="1" max="10000" value="48" oninput="c9c11s8Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">n:</span><input id="c9c11s8N" type="number" min="1" max="10000" value="180" oninput="c9c11s8Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c11s8Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c11s8Draw = function(){
    const m = Math.max(1, parseInt(document.getElementById('c9c11s8M').value || '1', 10));
    const n = Math.max(1, parseInt(document.getElementById('c9c11s8N').value || '1', 10));
    const mx = Math.max(m, n), mn = Math.min(m, n);
    document.getElementById('c9c11s8Out').innerHTML = `
      <div><strong>Stage 1 (1 to max(m,n)):</strong> ${mx} iterations (2 lists)</div>
      <div><strong>Stage 2 (1 to min(m,n)):</strong> ${mn} iterations (1 common list)</div>
      <div class="text-emerald-300 font-bold"><strong>Stage 3 (1 to min(m,n), best_gcd):</strong> ${mn} iterations &amp; ZERO lists!</div>
    `;
  };
  setTimeout(window.c9c11s8Draw, 40);
})();
</script>
"""
}
