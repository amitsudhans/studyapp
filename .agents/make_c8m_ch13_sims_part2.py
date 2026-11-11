#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 8 Maths Chapter 13: Algebra Play
Part 2: Simulators 9 to 16
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🏆</span> Largest Product (□□ × □) Permutation Tester
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <div><span class="text-slate-400">Smallest (p)</span><input id="c13s9p" type="number" min="1" max="7" value="2" oninput="c13s9Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-cyan-300"></div>
    <div><span class="text-slate-400">Middle (q)</span><input id="c13s9q" type="number" min="2" max="8" value="5" oninput="c13s9Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-amber-300"></div>
    <div><span class="text-slate-400">Largest (r)</span><input id="c13s9r" type="number" min="3" max="9" value="8" oninput="c13s9Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-emerald-300"></div>
  </div>
  <div id="c13s9Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1"></div>
</div>
<script>
(function(){
  window.c13s9Draw = function(){
    const raw = [
      parseInt(document.getElementById('c13s9p').value,10)||1,
      parseInt(document.getElementById('c13s9q').value,10)||5,
      parseInt(document.getElementById('c13s9r').value,10)||8
    ].map(n => Math.max(1, Math.min(9, n))).sort((a,b)=>a-b);
    const [p,q,r] = raw;
    const perms = [
      [q,p,r], [r,p,q], [p,q,r], [r,q,p], [p,r,q], [q,r,p]
    ].map(([a,b,c]) => ({ label: `${a}${b} × ${c}`, val: (10*a+b)*c, win: a===q && b===p && c===r }))
     .sort((x,y) => y.val - x.val);
    document.getElementById('c13s9Out').innerHTML =
      `<div class="text-slate-400 mb-1">Sorted digits p=${p} &lt; q=${q} &lt; r=${r} — All 6 Arrangements:</div>` +
      perms.map((it, idx) => `<div class="flex justify-between px-2 py-0.5 rounded ${idx===0?'bg-emerald-500/20 text-emerald-300 font-bold':'text-slate-300'}"><span>${idx+1}. ${it.label} ${idx===0?'(qp × r WINNER!)':''}</span><span>${it.val}</span></div>`).join('');
  };
  window.c13s9Draw();
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📐</span> Place-Value Proof: 10qr + pr vs 10rq + pq
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <div><span class="text-slate-400">p</span><input id="c13s10p" type="number" min="1" max="7" value="2" oninput="c13s10Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-cyan-300"></div>
    <div><span class="text-slate-400">q</span><input id="c13s10q" type="number" min="2" max="8" value="5" oninput="c13s10Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-amber-300"></div>
    <div><span class="text-slate-400">r</span><input id="c13s10r" type="number" min="3" max="9" value="8" oninput="c13s10Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-emerald-300"></div>
  </div>
  <div id="c13s10Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  window.c13s10Draw = function(){
    const [p,q,r] = [
      parseInt(document.getElementById('c13s10p').value,10)||2,
      parseInt(document.getElementById('c13s10q').value,10)||5,
      parseInt(document.getElementById('c13s10r').value,10)||8
    ].map(n => Math.max(1, Math.min(9, n))).sort((a,b)=>a-b);
    const shared = 10*q*r, pr = p*r, pq = p*q;
    document.getElementById('c13s10Out').innerHTML = `
      <div class="text-emerald-300"><b>qp × r</b> = (10·${q} + ${p})·${r} = <span class="text-slate-300">${shared}</span> + <b class="text-emerald-300">${pr}</b> = <b>${shared+pr}</b></div>
      <div class="text-amber-300"><b>rp × q</b> = (10·${r} + ${p})·${q} = <span class="text-slate-300">${shared}</span> + <b class="text-amber-300">${pq}</b> = <b>${shared+pq}</b></div>
      <div class="p-2 rounded bg-slate-900 border border-slate-700 text-slate-200">
        Cancel identical <b>10qr = ${shared}</b>! Remaining margin: <b>pr − pq = p(r − q) = ${p}(${r} − ${q}) = <span class="text-cyan-300">${pr - pq}</span></b>!
      </div>`;
  };
  window.c13s10Draw();
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🔁</span> Two-Digit Reversals: Mod 9 & Mod 11 Verifier
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <div>
      <div class="flex justify-between text-slate-300"><span>Tens Digit a:</span><b id="c13s11Av" class="text-cyan-300">7</b></div>
      <input id="c13s11a" type="range" min="1" max="9" value="7" oninput="c13s11Draw()" class="w-full accent-cyan-400">
    </div>
    <div>
      <div class="flex justify-between text-slate-300"><span>Units Digit b:</span><b id="c13s11Bv" class="text-amber-300">2</b></div>
      <input id="c13s11b" type="range" min="1" max="9" value="2" oninput="c13s11Draw()" class="w-full accent-amber-400">
    </div>
  </div>
  <div id="c13s11Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  window.c13s11Draw = function(){
    const a = parseInt(document.getElementById('c13s11a').value,10)||7;
    const b = parseInt(document.getElementById('c13s11b').value,10)||2;
    document.getElementById('c13s11Av').textContent = a;
    document.getElementById('c13s11Bv').textContent = b;
    const ab = 10*a + b, ba = 10*b + a;
    const diff = Math.abs(ab - ba), dabs = Math.abs(a - b);
    const sum = ab + ba;
    document.getElementById('c13s11Out').innerHTML = `
      <div>Original <b>ab = ${ab}</b> (10·${a}+${b}) &nbsp;|&nbsp; Reversed <b>ba = ${ba}</b> (10·${b}+${a})</div>
      <div class="text-emerald-300"><b>|ab − ba| = ${diff}</b> = <b>9 × |${a} − ${b}| = 9 × ${dabs}</b> → Always divisible by <b>9</b>!</div>
      <div class="text-cyan-300"><b>ab + ba = ${sum}</b> = <b>11 × (${a} + ${b}) = 11 × ${a+b}</b> → Always divisible by <b>11</b>!</div>`;
  };
  window.c13s11Draw();
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🌀</span> 3-Digit Cyclic (÷37) & 6-Digit Repeat (÷1001)
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <div><span class="text-slate-400">Digit a (1–9)</span><input id="c13s12a" type="number" min="1" max="9" value="2" oninput="c13s12Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-cyan-300"></div>
    <div><span class="text-slate-400">Digit b (0–9)</span><input id="c13s12b" type="number" min="0" max="9" value="5" oninput="c13s12Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-amber-300"></div>
    <div><span class="text-slate-400">Digit c (0–9)</span><input id="c13s12c" type="number" min="0" max="9" value="4" oninput="c13s12Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-emerald-300"></div>
  </div>
  <div id="c13s12Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  window.c13s12Draw = function(){
    const a = Math.max(1, Math.min(9, parseInt(document.getElementById('c13s12a').value,10)||2));
    const b = Math.max(0, Math.min(9, parseInt(document.getElementById('c13s12b').value,10)||5));
    const c = Math.max(0, Math.min(9, parseInt(document.getElementById('c13s12c').value,10)||4));
    const n1 = 100*a+10*b+c, n2 = 100*b+10*c+a, n3 = 100*c+10*a+b;
    const cyc = n1+n2+n3;
    const rep = n1*1001;
    document.getElementById('c13s12Out').innerHTML = `
      <div><b class="text-amber-300">Cyclic Sum:</b> ${n1} + ${String(n2).padStart(3,'0')} + ${String(n3).padStart(3,'0')} = <b>${cyc}</b> = 111×(${a+b+c}) = <b>37 × ${3*(a+b+c)}</b> (Rem ÷37 = ${cyc%37})</div>
      <div><b class="text-emerald-300">6-Digit Repeat:</b> ${rep.toLocaleString()} = <b>1001 × ${n1}</b> = <b>7 × 11 × 13 × ${n1}</b></div>
      <div class="text-slate-300">Div Checks: ÷7 = <b>${rep/7}</b> &nbsp;|&nbsp; ÷11 = <b>${rep/11}</b> &nbsp;|&nbsp; ÷13 = <b>${rep/13}</b></div>`;
  };
  window.c13s12Draw();
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>🌺</span> Shrine Flowers & Genie Coin-Doubling Backtracker
    </h3>
    <button type="button" onclick="c13s13Toggle()" id="c13s13Btn" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 text-xs border border-slate-700">Switch to 2-Round Genie</button>
  </div>
  <div class="space-y-2 text-xs">
    <div class="flex justify-between text-slate-300"><span>Fixed Offering / Fee (f):</span><b id="c13s13Fval" class="text-emerald-300">8</b></div>
    <input id="c13s13F" type="range" min="4" max="24" step="4" value="8" oninput="c13s13Draw()" class="w-full accent-emerald-400">
    <div id="c13s13Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-1.5"></div>
  </div>
</div>
<script>
(function(){
  let rounds = 3;
  window.c13s13Toggle = function(){
    rounds = rounds === 3 ? 2 : 3;
    document.getElementById('c13s13Btn').textContent = rounds===3 ? 'Switch to 2-Round Genie' : 'Switch to 3-Shrine Flowers';
    window.c13s13Draw();
  };
  window.c13s13Draw = function(){
    const f = parseInt(document.getElementById('c13s13F').value,10)||8;
    document.getElementById('c13s13Fval').textContent = f;
    const mult = rounds===3 ? 8 : 4;
    const sub = rounds===3 ? 7*f : 3*f;
    const x = sub / mult;
    let cur = x, steps = [];
    for(let i=1;i<=rounds;i++){
      const doubled = cur * 2;
      cur = doubled - f;
      steps.push(`Round ${i}: Double → ${doubled}, deduct ${f} → <b>${cur}</b>`);
    }
    document.getElementById('c13s13Out').innerHTML = `
      <div><b class="text-cyan-300">${rounds===3?'3-Shrine Flowers':'2-Round Traveler & Genie'} Equation:</b> ${mult}x − ${sub} = 0 → Start <b>x = ${x}</b></div>
      <div class="text-slate-300 font-mono text-[11px]">${steps.join('<br>')}</div>`;
  };
  window.c13s13Draw();
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🐎</span> Barnyard Heads-Legs & Age Ratio Solver
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <div><span class="text-slate-400">Total Heads (H)</span><input id="c13s14H" type="number" min="2" max="50" value="20" oninput="c13s14Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-cyan-300"></div>
    <div><span class="text-slate-400">Extra Legs Pair Check</span><input id="c13s14Horses" type="range" min="0" max="20" value="8" oninput="c13s14Draw()" class="w-full accent-amber-400 mt-2"></div>
  </div>
  <div id="c13s14Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  window.c13s14Draw = function(){
    const H = Math.max(2, Math.min(50, parseInt(document.getElementById('c13s14H').value,10)||20));
    const sl = document.getElementById('c13s14Horses');
    sl.max = H;
    const x = Math.min(H, parseInt(sl.value,10)||0);
    const hens = H - x;
    const legs = 4*x + 2*hens;
    document.getElementById('c13s14Out').innerHTML = `
      <div>Target Equation: <b class="text-amber-300">4x + 2(${H} − x) = ${legs}</b> → 2x + ${2*H} = ${legs}</div>
      <div class="text-emerald-300 font-semibold">Solved: Horses (x) = <b>${x}</b> (${4*x} legs) &nbsp;|&nbsp; Hens (${H}−x) = <b>${hens}</b> (${2*hens} legs)</div>
      <div class="text-slate-400 border-t border-slate-800 pt-1.5">Mother-Daughter Example: 4x + 6 = 3(x + 6) → Daughter x = <b>12 yrs</b>, Mother = <b>48 yrs</b></div>`;
  };
  window.c13s14Draw();
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🥞</span> Dosa Cart Break-Even Point (35n = 600 + 15n)
  </h3>
  <div class="space-y-2 text-xs">
    <div class="flex justify-between text-slate-300"><span>Dosas Sold Today (n):</span><b id="c13s15Nval" class="text-cyan-300">30 dosas</b></div>
    <input id="c13s15Sl" type="range" min="0" max="60" value="30" oninput="c13s15Draw()" class="w-full accent-amber-400">
    <div id="c13s15Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-1.5"></div>
  </div>
</div>
<script>
(function(){
  window.c13s15Draw = function(){
    const n = parseInt(document.getElementById('c13s15Sl').value,10)||0;
    document.getElementById('c13s15Nval').textContent = `${n} dosas`;
    const cost = 600 + 15*n, rev = 35*n, net = rev - cost;
    document.getElementById('c13s15Out').innerHTML = `
      <div class="grid grid-cols-2 gap-2">
        <div class="p-2 rounded bg-slate-900 border border-slate-800">Total Cost (600 + 15n): <b class="text-rose-300">₹${cost}</b></div>
        <div class="p-2 rounded bg-slate-900 border border-slate-800">Revenue (35n): <b class="text-cyan-300">₹${rev}</b></div>
      </div>
      <div class="font-bold ${net===0?'text-amber-300':net>0?'text-emerald-300':'text-rose-300'}">
        Net Status: ${net===0 ? 'EXACT BREAK-EVEN (35n = 600 + 15n → n = 30)!' : net>0 ? `PURE PROFIT = +₹${net}` : `STILL IN LOSS = −₹${-net}`}
      </div>
      <div class="text-slate-400">Nested Fraction Law: x/2 + x/4 + x/8 + 12 = x → (1/8)x = 12 → <b>x = 96</b></div>`;
  };
  window.c13s15Draw();
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🎓</span> Chapter 13 Master Algebraic Proofs Matrix
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c13s16Tab(0)" id="c13s16t0" class="px-2 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-semibold">Tricks (6.2)</button>
    <button type="button" onclick="c13s16Tab(1)" id="c13s16t1" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Pyramids & Grids</button>
    <button type="button" onclick="c13s16Tab(2)" id="c13s16t2" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Products & Mod</button>
    <button type="button" onclick="c13s16Tab(3)" id="c13s16t3" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Word Solvers</button>
  </div>
  <div id="c13s16Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5 text-slate-300"></div>
</div>
<script>
(function(){
  const tabs = [
    `<div class="text-amber-300 font-bold">Section 6.2 Tricks & Birthdays</div><div>• Think-of-a-Number: (2x + 4)/2 − x = <b>x + 2 − x = 2</b></div><div>• Birthday Decoder: ((5M+6)×4+9)×5+D = <b>100M + 165 + D</b> (subtract 165)</div>`,
    `<div class="text-cyan-300 font-bold">Sections 6.3 & 6.4 Pyramids & Grids</div><div>• 3-Row Peak: <b>a + 2b + c</b> &nbsp;|&nbsp; 4-Row Peak: <b>a + 3b + 3c + d</b></div><div>• Virahāṅka-Fibonacci: 1, 2, 3, 5, 8, 13, 21... shifts upward each row</div><div>• Calendar 2×2: <b>S = 4a + 16</b> → a = (S−16)/4</div>`,
    `<div class="text-emerald-300 font-bold">Sections 6.5 & 6.6 Optimization & Divisibility</div><div>• Max Product (p&lt;q&lt;r): <b>qp × r</b> beats rp × q by <b>p(r − q)</b></div><div>• 2-Digit Reversal: <b>ba−ab = 9(b−a)</b>; <b>ab+ba = 11(a+b)</b></div><div>• Cyclic 3-Digit: <b>111(a+b+c) = 37×3(a+b+c)</b> &nbsp;|&nbsp; Repeat: <b>abcabc = 7×11×13×abc</b></div>`,
    `<div class="text-rose-300 font-bold">Section 6.6 Linear Word Equations</div><div>• 3 Shrines: <b>8x − 7f = 0</b> &nbsp;|&nbsp; 2-Round Genie: <b>4x − 3f = 0</b></div><div>• Barnyard Legs: <b>4x + 2(H−x) = L</b> &nbsp;|&nbsp; Break-Even: <b>35n = 600 + 15n</b></div><div>• Fraction Series: <b>x/2 + x/4 + x/8 + R = x</b> → (1/8)x = R</div>`
  ];
  window.c13s16Tab = function(i){
    [0,1,2,3].forEach(k => {
      const b = document.getElementById('c13s16t'+k);
      if(b) b.className = k===i ? 'px-2 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-semibold' : 'px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    document.getElementById('c13s16Out').innerHTML = tabs[i];
  };
  window.c13s16Tab(0);
})();
</script>
"""
}
