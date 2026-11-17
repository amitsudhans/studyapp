#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions
Part 1: Simulators 1 to 8 (Slides 1 to 8)
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔢</span> Sequence Term Explorer: Finite vs Infinite Patterns
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Select Sequence Family:</span>
      <select id="c9c8s1Seq" onchange="c9c8s1Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
        <option value="nat">Natural Numbers: 1, 2, 3, 4, ... (Infinite)</option>
        <option value="odd">Odd Numbers: 1, 3, 5, 7, ... (Infinite)</option>
        <option value="even">Even Numbers: 2, 4, 6, 8, ... (Infinite)</option>
        <option value="tri">Triangular Numbers: 1, 3, 6, 10, ... (Infinite)</option>
        <option value="sq">Square Numbers: 1, 4, 9, 16, ... (Infinite)</option>
        <option value="fin">Months Days (Non-Leap): 31, 28, ..., 31 (Finite, 12 terms)</option>
      </select>
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>Highlight Position (n):</span>
        <span id="c9c8s1NLbl" class="text-amber-300 font-bold">n = 5</span>
      </div>
      <input id="c9c8s1N" type="range" min="1" max="10" value="5" oninput="c9c8s1Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9c8s1Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2.5"></div>
</div>
<script>
(function(){
  const months = [31,28,31,30,31,30,31,31,30,31,30,31];
  window.c9c8s1Draw = function(){
    const type = document.getElementById('c9c8s1Seq').value;
    const n = parseInt(document.getElementById('c9c8s1N').value, 10);
    document.getElementById('c9c8s1NLbl').textContent = 'n = ' + n;
    const terms = [];
    const maxShow = type === 'fin' ? 12 : 10;
    for(let i = 1; i <= maxShow; i++){
      if(type === 'nat') terms.push(i);
      else if(type === 'odd') terms.push(2*i - 1);
      else if(type === 'even') terms.push(2*i);
      else if(type === 'tri') terms.push(i*(i+1)/2);
      else if(type === 'sq') terms.push(i*i);
      else terms.push(months[i-1]);
    }
    const kind = type === 'fin' ? 'FINITE SEQUENCE (Ends at t₁₂ = 31)' : 'INFINITE SEQUENCE (Continues without end ...)';
    const pills = terms.map((val, idx) => {
      const pos = idx + 1;
      const active = pos === n;
      return `<div class="px-2.5 py-1.5 rounded-lg border text-center ${active ? 'bg-amber-500/20 border-amber-400 text-amber-200 scale-105' : 'bg-slate-900 border-slate-700 text-slate-300'}">
        <div class="text-[10px] text-slate-400">t<sub>${pos}</sub></div>
        <div class="font-bold text-sm">${val}</div>
      </div>`;
    }).join('');
    const chosen = terms[n - 1];
    document.getElementById('c9c8s1Out').innerHTML = `
      <div class="flex flex-wrap justify-between items-center gap-2">
        <span class="px-2 py-0.5 rounded bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 font-bold">${kind}</span>
        <span class="font-bold text-amber-300">Selected Term: t<sub>${n}</sub> = ${chosen}</span>
      </div>
      <div class="flex flex-wrap gap-2 pt-1">${pills}${type !== 'fin' ? '<div class="px-2.5 py-2 text-slate-400 font-bold">...</div>' : ''}</div>
    `;
  };
  setTimeout(window.c9c8s1Draw, 40);
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔺</span> Triangular &amp; Square Dot Grid Visualizer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Dot Pattern Mode:</span>
      <select id="c9c8s2Mode" onchange="c9c8s2Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
        <option value="tri">Triangular Numbers (Tₙ = 1 + 2 + ... + n)</option>
        <option value="sq">Square Numbers (n² = 1 + 3 + ... + (2n−1))</option>
      </select>
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>Order (n):</span>
        <span id="c9c8s2NLbl" class="text-emerald-300 font-bold">n = 4</span>
      </div>
      <input id="c9c8s2N" type="range" min="1" max="6" value="4" oninput="c9c8s2Draw()" class="w-full accent-emerald-400">
    </label>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 items-center">
    <svg id="c9c8s2Svg" viewBox="0 0 260 180" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c9c8s2Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
  </div>
</div>
<script>
(function(){
  const palette = ['#22d3ee','#34d399','#fbbf24','#f472b6','#a78bfa','#fb7185'];
  window.c9c8s2Draw = function(){
    const mode = document.getElementById('c9c8s2Mode').value;
    const n = parseInt(document.getElementById('c9c8s2N').value, 10);
    document.getElementById('c9c8s2NLbl').textContent = 'n = ' + n;
    let dots = '';
    if(mode === 'tri'){
      const dy = 24, dx = 26, topY = 26;
      for(let r = 1; r <= n; r++){
        const startX = 130 - ((r - 1) * dx) / 2;
        const y = topY + (r - 1) * dy;
        for(let c = 0; c < r; c++){
          dots += `<circle cx="${startX + c*dx}" cy="${y}" r="8" fill="${palette[(r-1)%palette.length]}" stroke="#0f172a" stroke-width="1.5"/>`;
        }
      }
      const sumTerms = Array.from({length:n}, (_,i)=>i+1).join(' + ');
      const total = n*(n+1)/2;
      const prevTri = (n-1)*n/2;
      document.getElementById('c9c8s2Out').innerHTML = `
        <div class="font-bold text-cyan-300 text-sm">T<sub>${n}</sub> = ${total} dots</div>
        <div>Row-by-row sum: <span class="text-white font-semibold">${sumTerms} = ${total}</span></div>
        <div class="text-emerald-300">T<sub>${n-1}</sub> + T<sub>${n}</sub> = ${prevTri} + ${total} = ${prevTri + total} = ${n}² (Perfect Square!)</div>
      `;
    } else {
      const step = 24, startX = 130 - ((n - 1)*step)/2, startY = 90 - ((n - 1)*step)/2;
      for(let r = 0; r < n; r++){
        for(let c = 0; c < n; c++){
          const layer = Math.max(r, c);
          dots += `<circle cx="${startX + c*step}" cy="${startY + r*step}" r="8" fill="${palette[layer%palette.length]}" stroke="#0f172a" stroke-width="1.5"/>`;
        }
      }
      const oddTerms = Array.from({length:n}, (_,i)=>2*i+1).join(' + ');
      document.getElementById('c9c8s2Out').innerHTML = `
        <div class="font-bold text-emerald-300 text-sm">${n}² = ${n*n} dots</div>
        <div>L-border sum of first ${n} odds: <span class="text-white font-semibold">${oddTerms} = ${n*n}</span></div>
        <div class="text-amber-300">Each colour band adds the next odd number (+${2*n-1} on outer L-layer).</div>
      `;
    }
    document.getElementById('c9c8s2Svg').innerHTML = dots;
  };
  setTimeout(window.c9c8s2Draw, 40);
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚡</span> Explicit Rule Jump &amp; Membership Tester
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Explicit Formula t<sub>n</sub>:</span>
      <select id="c9c8s3Rule" onchange="c9c8s3Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
        <option value="2n-1">uₙ = 2n − 1 (Odd Numbers)</option>
        <option value="3n+2">tₙ = 3n + 2 (Linear Rule)</option>
        <option value="n2">sₙ = n² (Square Numbers)</option>
        <option value="tri">Tₙ = n(n + 1)/2 (Triangular)</option>
      </select>
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Jump Directly to Position n:</span>
      <input id="c9c8s3N" type="number" min="1" max="500" value="53" oninput="c9c8s3Draw()" class="w-full mt-1.5 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Test Membership Value x:</span>
      <input id="c9c8s3X" type="number" min="1" max="5000" value="95" oninput="c9c8s3Draw()" class="w-full mt-1.5 bg-slate-900 text-emerald-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
  </div>
  <div id="c9c8s3Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c8s3Draw = function(){
    const rule = document.getElementById('c9c8s3Rule').value;
    const n = Math.max(1, parseInt(document.getElementById('c9c8s3N').value || '1', 10));
    const x = parseInt(document.getElementById('c9c8s3X').value || '1', 10);
    let val = 0, expr = '', memHtml = '';
    if(rule === '2n-1'){
      val = 2*n - 1;
      expr = `2(${n}) − 1 = ${val}`;
      const k = (x + 1) / 2;
      const ok = Number.isInteger(k) && k >= 1;
      memHtml = ok ? `<span class="text-emerald-300 font-bold">YES!</span> 2n − 1 = ${x} ⇒ n = ${k} (Positive integer, so ${x} = u<sub>${k}</sub>)`
                   : `<span class="text-rose-400 font-bold">NO!</span> 2n − 1 = ${x} ⇒ n = ${k} (Not a positive integer)`;
    } else if(rule === '3n+2'){
      val = 3*n + 2;
      expr = `3(${n}) + 2 = ${val}`;
      const k = (x - 2) / 3;
      const ok = Number.isInteger(k) && k >= 1;
      memHtml = ok ? `<span class="text-emerald-300 font-bold">YES!</span> 3n + 2 = ${x} ⇒ n = ${k} (so ${x} = t<sub>${k}</sub>)`
                   : `<span class="text-rose-400 font-bold">NO!</span> 3n + 2 = ${x} ⇒ n = ${k.toFixed(2)} (Not a positive integer)`;
    } else if(rule === 'n2'){
      val = n*n;
      expr = `${n}² = ${val}`;
      const k = Math.sqrt(x);
      const ok = x >= 1 && Number.isInteger(k);
      memHtml = ok ? `<span class="text-emerald-300 font-bold">YES!</span> n² = ${x} ⇒ n = ${k} (so ${x} = s<sub>${k}</sub>)`
                   : `<span class="text-rose-400 font-bold">NO!</span> √${x} ≈ ${k.toFixed(3)} (Not a positive integer)`;
    } else {
      val = n*(n+1)/2;
      expr = `${n}(${n+1})/2 = ${val}`;
      const disc = 1 + 8*x;
      const rt = Math.sqrt(disc);
      const ok = x >= 1 && Number.isInteger(rt) && ((-1 + rt) % 2 === 0);
      const k = (-1 + rt) / 2;
      memHtml = ok ? `<span class="text-emerald-300 font-bold">YES!</span> n(n+1)/2 = ${x} ⇒ n = ${k} (so ${x} = T<sub>${k}</sub>)`
                   : `<span class="text-rose-400 font-bold">NO!</span> 1 + 8(${x}) = ${disc} does not give a positive integer n.`;
    }
    document.getElementById('c9c8s3Out').innerHTML = `
      <div class="flex flex-wrap justify-between gap-2">
        <span>Instant Jump: <strong class="text-amber-300">${expr}</strong> (No earlier terms needed!)</span>
      </div>
      <div class="pt-1 border-t border-slate-800">Membership Test for <strong>${x}</strong>: ${memHtml}</div>
    `;
  };
  setTimeout(window.c9c8s3Draw, 40);
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔗</span> Recursive Step Chain Builder
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Anchor Term t₁:</span>
      <input id="c9c8s4T1" type="number" min="-20" max="50" value="1" oninput="c9c8s4Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Recurrence Rule:</span>
      <select id="c9c8s4Op" onchange="c9c8s4Draw()" class="w-full mt-1.5 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
        <option value="add3">tₙ = tₙ₋₁ + 3</option>
        <option value="mul2add1">tₙ = 2·tₙ₋₁ + 1</option>
        <option value="mul2sub1">tₙ = 2·tₙ₋₁ − 1</option>
        <option value="addn">tₙ = tₙ₋₁ + n</option>
      </select>
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>Chain Length:</span>
        <span id="c9c8s4LenLbl" class="text-emerald-300 font-bold">6 terms</span>
      </div>
      <input id="c9c8s4Len" type="range" min="3" max="8" value="6" oninput="c9c8s4Draw()" class="w-full accent-emerald-400">
    </label>
  </div>
  <div id="c9c8s4Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c8s4Draw = function(){
    const t1 = parseInt(document.getElementById('c9c8s4T1').value || '1', 10);
    const op = document.getElementById('c9c8s4Op').value;
    const len = parseInt(document.getElementById('c9c8s4Len').value, 10);
    document.getElementById('c9c8s4LenLbl').textContent = len + ' terms';
    const arr = [t1];
    const steps = [`t₁ = ${t1} (Anchor)`];
    for(let n = 2; n <= len; n++){
      const prev = arr[arr.length - 1];
      let next = prev;
      if(op === 'add3'){ next = prev + 3; steps.push(`t<sub>${n}</sub> = ${prev} + 3 = ${next}`); }
      else if(op === 'mul2add1'){ next = 2*prev + 1; steps.push(`t<sub>${n}</sub> = 2(${prev}) + 1 = ${next}`); }
      else if(op === 'mul2sub1'){ next = 2*prev - 1; steps.push(`t<sub>${n}</sub> = 2(${prev}) − 1 = ${next}`); }
      else { next = prev + n; steps.push(`t<sub>${n}</sub> = ${prev} + ${n} = ${next}`); }
      arr.push(next);
    }
    const chain = arr.map((v,i)=>`<span class="px-2.5 py-1 rounded-lg bg-slate-900 border border-slate-700 font-bold text-cyan-300">t<sub>${i+1}</sub>=${v}</span>`).join('<span class="text-amber-400 font-bold">→</span>');
    document.getElementById('c9c8s4Out').innerHTML = `
      <div class="flex flex-wrap items-center gap-1.5">${chain}</div>
      <div class="text-slate-400 pt-1 border-t border-slate-800">Step trace: ${steps.join(' &nbsp;|&nbsp; ')}</div>
    `;
  };
  setTimeout(window.c9c8s4Draw, 40);
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🎵</span> Virahānka-Fibonacci 1-Beat &amp; 2-Beat Meter Counter
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Select Total Poetic Beats (n):</span>
      <span id="c9c8s5NLbl" class="text-amber-300 font-bold">n = 5 beats</span>
    </div>
    <input id="c9c8s5N" type="range" min="1" max="7" value="5" oninput="c9c8s5Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c8s5Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  function patterns(n){
    if(n === 0) return [''];
    if(n < 0) return [];
    const res = [];
    for(const p of patterns(n - 1)) res.push('S' + (p ? ' ' + p : ''));
    for(const p of patterns(n - 2)) res.push('L' + (p ? ' ' + p : ''));
    return res;
  }
  window.c9c8s5Draw = function(){
    const n = parseInt(document.getElementById('c9c8s5N').value, 10);
    document.getElementById('c9c8s5NLbl').textContent = `n = ${n} beats`;
    const list = patterns(n);
    const vPrev1 = n > 1 ? patterns(n - 1).length : 0;
    const vPrev2 = n > 2 ? patterns(n - 2).length : (n === 2 ? 1 : 0);
    const chips = list.map(item => `<span class="px-2 py-1 rounded bg-slate-900 border border-slate-700 font-mono text-[11px] text-cyan-200">${item}</span>`).join('');
    document.getElementById('c9c8s5Out').innerHTML = `
      <div class="flex flex-wrap justify-between items-center gap-2">
        <span class="font-bold text-emerald-300 text-sm">V<sub>${n}</sub> = ${list.length} rhythmic combinations</span>
        <span class="text-amber-300 font-semibold">${n >= 3 ? `V<sub>${n}</sub> = V<sub>${n-1}</sub> + V<sub>${n-2}</sub> = ${vPrev1} + ${vPrev2}` : 'Base Case Anchor'}</span>
      </div>
      <div class="text-[11px] text-slate-400">Legend: <strong>S</strong> = Short (1 beat), <strong>L</strong> = Long (2 beats)</div>
      <div class="flex flex-wrap gap-1.5 pt-1 max-h-28 overflow-y-auto">${chips}</div>
    `;
  };
  setTimeout(window.c9c8s5Draw, 40);
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>➕</span> Arithmetic Progression Common Difference Explorer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>First Term (a):</span>
        <span id="c9c8s6ALbl" class="text-cyan-300 font-bold">a = 5</span>
      </div>
      <input id="c9c8s6A" type="range" min="-10" max="25" value="5" oninput="c9c8s6Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>Common Difference (d):</span>
        <span id="c9c8s6DLbl" class="text-amber-300 font-bold">d = 4</span>
      </div>
      <input id="c9c8s6D" type="range" min="-8" max="8" value="4" oninput="c9c8s6Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9c8s6Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c8s6Draw = function(){
    const a = parseInt(document.getElementById('c9c8s6A').value, 10);
    const d = parseInt(document.getElementById('c9c8s6D').value, 10);
    document.getElementById('c9c8s6ALbl').textContent = 'a = ' + a;
    document.getElementById('c9c8s6DLbl').textContent = 'd = ' + d;
    const terms = Array.from({length:6}, (_,i)=>a + i*d);
    const trend = d > 0 ? 'STRICTLY INCREASING AP (d > 0)' : d < 0 ? 'STRICTLY DECREASING AP (d < 0)' : 'CONSTANT AP (d = 0)';
    const signD = d >= 0 ? `+${d}` : `${d}`;
    const boxes = terms.map((v,i)=>`
      <div class="flex items-center gap-1.5">
        <div class="px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-center">
          <div class="text-[10px] text-slate-400">t<sub>${i+1}</sub></div>
          <div class="font-bold text-sm text-white">${v}</div>
        </div>
        ${i < 5 ? `<span class="text-amber-400 font-bold text-[11px]">${signD}</span>` : ''}
      </div>
    `).join('');
    document.getElementById('c9c8s6Out').innerHTML = `
      <div class="flex flex-wrap justify-between items-center gap-2">
        <span class="px-2 py-0.5 rounded bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 font-bold">${trend}</span>
        <span class="text-slate-400">General form: a, a+d, a+2d, ...</span>
      </div>
      <div class="flex flex-wrap items-center gap-1.5 pt-1">${boxes}</div>
    `;
  };
  setTimeout(window.c9c8s6Draw, 40);
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🎯</span> AP n<sup>th</sup>-Term Finder &amp; Index Solver
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">First Term (a):</span>
      <input id="c9c8s7A" type="number" value="7" oninput="c9c8s7Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Common Difference (d):</span>
      <input id="c9c8s7D" type="number" value="4" oninput="c9c8s7Draw()" class="w-full mt-1.5 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Position (n):</span>
      <input id="c9c8s7N" type="number" min="1" max="1000" value="25" oninput="c9c8s7Draw()" class="w-full mt-1.5 bg-slate-900 text-emerald-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
  </div>
  <div id="c9c8s7Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c8s7Draw = function(){
    const a = parseFloat(document.getElementById('c9c8s7A').value || '0');
    const d = parseFloat(document.getElementById('c9c8s7D').value || '0');
    const n = Math.max(1, parseInt(document.getElementById('c9c8s7N').value || '1', 10));
    const tn = a + (n - 1) * d;
    document.getElementById('c9c8s7Out').innerHTML = `
      <div class="text-sm font-bold text-emerald-300">t<sub>${n}</sub> = ${a} + (${n} − 1)(${d}) = ${a} + ${(n-1)*d} = ${tn}</div>
      <div class="text-slate-300">Notice why it is <strong>(n − 1)</strong> steps of d: moving from t<sub>1</sub> to t<sub>${n}</sub> takes exactly <strong>${n-1}</strong> jumps!</div>
      <div class="text-cyan-300">Reverse Check: n = (t<sub>n</sub> − a)/d + 1 = (${tn} − ${a})/${d || 1} + 1 ${d !== 0 ? '= ' + n : '(d = 0 constant)'}</div>
    `;
  };
  setTimeout(window.c9c8s7Draw, 40);
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📈</span> Linear Coordinate Graph (n, t<sub>n</sub>) Plotter
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>First Term (a):</span>
        <span id="c9c8s8ALbl" class="text-cyan-300 font-bold">a = 2</span>
      </div>
      <input id="c9c8s8A" type="range" min="-4" max="8" value="2" oninput="c9c8s8Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>Slope / Common Diff (d):</span>
        <span id="c9c8s8DLbl" class="text-amber-300 font-bold">d = 3</span>
      </div>
      <input id="c9c8s8D" type="range" min="-3" max="4" value="3" oninput="c9c8s8Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 items-center">
    <svg id="c9c8s8Svg" viewBox="0 0 280 190" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c9c8s8Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
  </div>
</div>
<script>
(function(){
  window.c9c8s8Draw = function(){
    const a = parseInt(document.getElementById('c9c8s8A').value, 10);
    const d = parseInt(document.getElementById('c9c8s8D').value, 10);
    document.getElementById('c9c8s8ALbl').textContent = 'a = ' + a;
    document.getElementById('c9c8s8DLbl').textContent = 'd = ' + d;
    const ox = 34, oy = 115, sx = 38, sy = 5.5;
    let svg = `<line x1="20" y1="${oy}" x2="265" y2="${oy}" stroke="#475569" stroke-width="1.5"/>`;
    svg += `<line x1="${ox}" y1="12" x2="${ox}" y2="178" stroke="#475569" stroke-width="1.5"/>`;
    const pts = [];
    for(let n = 1; n <= 5; n++){
      const tn = a + (n - 1)*d;
      const px = ox + n*sx;
      const py = oy - tn*sy;
      pts.push({n, tn, px, py});
    }
    svg += `<line x1="${pts[0].px}" y1="${pts[0].py}" x2="${pts[4].px}" y2="${pts[4].py}" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>`;
    for(const p of pts){
      svg += `<circle cx="${p.px}" cy="${p.py}" r="4.5" fill="#fbbf24" stroke="#0f172a" stroke-width="1.5"/>`;
      svg += `<text x="${p.px}" y="${oy + 12}" text-anchor="middle" fill="#94a3b8" font-size="9">${p.n}</text>`;
      svg += `<text x="${p.px + 6}" y="${p.py - 5}" fill="#e2e8f0" font-size="8.5">(${p.n},${p.tn})</text>`;
    }
    document.getElementById('c9c8s8Svg').innerHTML = svg;
    document.getElementById('c9c8s8Out').innerHTML = `
      <div class="font-bold text-cyan-300">Linear Equation: t<sub>n</sub> = ${d}n + (${a - d})</div>
      <div>Every +1 step horizontally shifts vertically by constant slope <strong>d = ${d}</strong>.</div>
      <div class="text-emerald-300">All 5 ordered pairs lie strictly on one straight line!</div>
    `;
  };
  setTimeout(window.c9c8s8Draw, 40);
})();
</script>
"""
}
