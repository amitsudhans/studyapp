#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 8: Predicting What Comes Next: Exploring Sequences and Progressions
Part 2: Simulators 9 to 16 (Slides 9 to 16)
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚖️</span> Gauss Reversal Pairing Visualizer
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Sum Natural Numbers up to n:</span>
      <span id="c9c8s9NLbl" class="text-amber-300 font-bold">n = 8</span>
    </div>
    <input id="c9c8s9N" type="range" min="4" max="12" value="8" oninput="c9c8s9Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c8s9Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c8s9Draw = function(){
    const n = parseInt(document.getElementById('c9c8s9N').value, 10);
    document.getElementById('c9c8s9NLbl').textContent = 'n = ' + n;
    const cols = [];
    for(let i = 1; i <= n; i++){
      cols.push(`<div class="px-2 py-1 rounded bg-slate-900 border border-slate-700 text-center min-w-[30px]">
        <div class="text-cyan-300 font-bold">${i}</div>
        <div class="text-amber-300 font-bold">${n + 1 - i}</div>
        <div class="text-[10px] text-emerald-300 border-t border-slate-700 mt-0.5 pt-0.5">${n + 1}</div>
      </div>`);
    }
    const sn = n * (n + 1) / 2;
    document.getElementById('c9c8s9Out').innerHTML = `
      <div class="flex flex-wrap gap-1.5">${cols.join('')}</div>
      <div class="pt-1 border-t border-slate-800 text-emerald-300 font-bold">
        2·S<sub>${n}</sub> = ${n} × (${n} + 1) = ${n*(n+1)} &nbsp;⇒&nbsp; S<sub>${n}</sub> = ${n} × ${n+1} / 2 = ${sn}
      </div>
    `;
  };
  setTimeout(window.c9c8s9Draw, 40);
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧮</span> Āryabhaṭa n × (n + 1) Grid &amp; Range Sum Calculator
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Start Integer (a):</span>
      <input id="c9c8s10A" type="number" min="1" max="500" value="51" oninput="c9c8s10Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">End Integer (b):</span>
      <input id="c9c8s10B" type="number" min="1" max="1000" value="100" oninput="c9c8s10Draw()" class="w-full mt-1.5 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
  </div>
  <div id="c9c8s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c8s10Draw = function(){
    const a = Math.max(1, parseInt(document.getElementById('c9c8s10A').value || '1', 10));
    const b = Math.max(a, parseInt(document.getElementById('c9c8s10B').value || String(a), 10));
    const sb = b * (b + 1) / 2;
    const saPrev = (a - 1) * a / 2;
    const diff = sb - saPrev;
    document.getElementById('c9c8s10Out').innerHTML = `
      <div>S<sub>${b}</sub> = ${b}(${b+1})/2 = <strong class="text-amber-300">${sb}</strong></div>
      <div>S<sub>${a-1}</sub> = ${a-1}(${a})/2 = <strong class="text-cyan-300">${saPrev}</strong></div>
      <div class="pt-1 border-t border-slate-800 text-emerald-300 font-bold text-sm">
        Sum from ${a} to ${b} = S<sub>${b}</sub> − S<sub>${a-1}</sub> = ${diff}
      </div>
    `;
  };
  setTimeout(window.c9c8s10Draw, 40);
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>✖️</span> Geometric Progression Common Ratio Explorer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">First Term (a):</span>
      <input id="c9c8s11A" type="number" value="4" oninput="c9c8s11Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Common Ratio (r):</span>
      <select id="c9c8s11R" onchange="c9c8s11Draw()" class="w-full mt-1.5 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
        <option value="3">r = 3 (Rapid Exponential Growth)</option>
        <option value="2">r = 2 (Doubling Every Step)</option>
        <option value="0.5">r = 1/2 (Smooth Halving Decay)</option>
        <option value="-2">r = −2 (Alternating Sign Explosion)</option>
        <option value="1">r = 1 (Constant Non-Zero Sequence)</option>
      </select>
    </label>
  </div>
  <div id="c9c8s11Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c8s11Draw = function(){
    const a = parseFloat(document.getElementById('c9c8s11A').value || '1');
    const r = parseFloat(document.getElementById('c9c8s11R').value);
    const terms = Array.from({length:6}, (_,i)=>+(a * Math.pow(r, i)).toFixed(4));
    const pills = terms.map((v,i)=>`<div class="px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-center">
      <div class="text-[10px] text-slate-400">t<sub>${i+1}</sub></div>
      <div class="font-bold text-sm text-white">${v}</div>
    </div>`).join(`<span class="text-amber-400 font-bold">×${r}</span>`);
    const desc = r > 1 ? 'EXPLOSIVE GROWTH (r > 1)' : (r > 0 && r < 1) ? 'EXPONENTIAL DECAY TOWARD 0 (0 < r < 1)' : r < 0 ? 'ALTERNATING SIGNS (r < 0)' : 'CONSTANT GP &amp; AP (r = 1)';
    document.getElementById('c9c8s11Out').innerHTML = `
      <div class="font-bold text-emerald-300">${desc}</div>
      <div class="flex flex-wrap items-center gap-1.5 pt-1">${pills}</div>
    `;
  };
  setTimeout(window.c9c8s11Draw, 40);
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🚀</span> GP n<sup>th</sup>-Term Calculator: t<sub>n</sub> = a · r<sup>n−1</sup>
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">First Term (a):</span>
      <input id="c9c8s12A" type="number" value="3" oninput="c9c8s12Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Common Ratio (r):</span>
      <input id="c9c8s12R" type="number" step="0.5" value="2" oninput="c9c8s12Draw()" class="w-full mt-1.5 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Position (n):</span>
      <input id="c9c8s12N" type="number" min="1" max="20" value="8" oninput="c9c8s12Draw()" class="w-full mt-1.5 bg-slate-900 text-emerald-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
  </div>
  <div id="c9c8s12Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c8s12Draw = function(){
    const a = parseFloat(document.getElementById('c9c8s12A').value || '1');
    const r = parseFloat(document.getElementById('c9c8s12R').value || '1');
    const n = Math.max(1, Math.min(20, parseInt(document.getElementById('c9c8s12N').value || '1', 10)));
    const pow = Math.pow(r, n - 1);
    const val = a * pow;
    document.getElementById('c9c8s12Out').innerHTML = `
      <div class="text-sm font-bold text-emerald-300">t<sub>${n}</sub> = ${a} × (${r})<sup>${n-1}</sup> = ${a} × ${+pow.toFixed(6)} = ${+val.toFixed(6)}</div>
      <div class="text-slate-300">Why exponent <strong>n − 1</strong>? Because t<sub>1</sub> = a·r<sup>0</sup> = a, and reaching t<sub>${n}</sub> requires <strong>${n-1}</strong> multiplications by r.</div>
    `;
  };
  setTimeout(window.c9c8s12Draw, 40);
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>❄️</span> Sierpiński Triangle &amp; Carpet Fractal Stage Simulator
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Fractal Shape:</span>
      <select id="c9c8s13Type" onchange="c9c8s13Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
        <option value="tri">Sierpiński Triangle (Count 3ⁿ, Area (3/4)ⁿ)</option>
        <option value="carp">Sierpiński Carpet (Count 8ⁿ, Area (8/9)ⁿ)</option>
      </select>
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>Iteration Stage (n):</span>
        <span id="c9c8s13NLbl" class="text-amber-300 font-bold">Stage 2</span>
      </div>
      <input id="c9c8s13N" type="range" min="0" max="4" value="2" oninput="c9c8s13Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 items-center">
    <svg id="c9c8s13Svg" viewBox="0 0 220 180" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c9c8s13Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
  </div>
</div>
<script>
(function(){
  function drawTri(ax,ay,bx,by,cx,cy,d,out){
    if(d === 0){
      out.push(`<polygon points="${ax},${ay} ${bx},${by} ${cx},${cy}" fill="#22d3ee" stroke="#0f172a" stroke-width="0.6"/>`);
      return;
    }
    const abx=(ax+bx)/2, aby=(ay+by)/2, bcx=(bx+cx)/2, bcy=(by+cy)/2, cax=(cx+ax)/2, cay=(cy+ay)/2;
    drawTri(ax,ay,abx,aby,cax,cay,d-1,out);
    drawTri(abx,aby,bx,by,bcx,bcy,d-1,out);
    drawTri(cax,cay,bcx,bcy,cx,cy,d-1,out);
  }
  function drawCarp(x,y,s,d,out){
    if(d === 0){
      out.push(`<rect x="${x}" y="${y}" width="${s}" height="${s}" fill="#34d399" stroke="#0f172a" stroke-width="0.4"/>`);
      return;
    }
    const sub = s / 3;
    for(let r=0;r<3;r++){
      for(let c=0;c<3;c++){
        if(r===1 && c===1) continue;
        drawCarp(x+c*sub, y+r*sub, sub, d-1, out);
      }
    }
  }
  window.c9c8s13Draw = function(){
    const type = document.getElementById('c9c8s13Type').value;
    const n = parseInt(document.getElementById('c9c8s13N').value, 10);
    document.getElementById('c9c8s13NLbl').textContent = 'Stage ' + n;
    const out = [];
    if(type === 'tri'){
      drawTri(110, 14, 24, 166, 196, 166, n, out);
      const cnt = Math.pow(3, n);
      const num = Math.pow(3, n), den = Math.pow(4, n);
      document.getElementById('c9c8s13Out').innerHTML = `
        <div class="font-bold text-cyan-300">Stage ${n} Sierpiński Triangle</div>
        <div>Shaded Sub-Triangles: <strong class="text-white">3<sup>${n}</sup> = ${cnt}</strong></div>
        <div>Remaining Shaded Area: <strong class="text-emerald-300">(3/4)<sup>${n}</sup> = ${num}/${den} ≈ ${(num/den).toFixed(4)}</strong></div>
      `;
    } else {
      const cap = Math.min(n, 3);
      drawCarp(35, 15, 150, cap, out);
      const cnt = Math.pow(8, n);
      const num = Math.pow(8, n), den = Math.pow(9, n);
      document.getElementById('c9c8s13Out').innerHTML = `
        <div class="font-bold text-emerald-300">Stage ${n} Sierpiński Carpet</div>
        <div>Shaded Sub-Squares: <strong class="text-white">8<sup>${n}</sup> = ${cnt}</strong></div>
        <div>Remaining Shaded Area: <strong class="text-amber-300">(8/9)<sup>${n}</sup> = ${num}/${den} ≈ ${(num/den).toFixed(4)}</strong></div>
      `;
    }
    document.getElementById('c9c8s13Svg').innerHTML = out.join('');
  };
  setTimeout(window.c9c8s13Draw, 40);
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏀</span> Exponential GP Curve vs AP Line &amp; Bouncing Ball Simulator
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>Initial Drop Height h<sub>0</sub> (cm):</span>
        <span id="c9c8s14HLbl" class="text-cyan-300 font-bold">160 cm</span>
      </div>
      <input id="c9c8s14H" type="range" min="80" max="200" step="20" value="160" oninput="c9c8s14Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>Rebound Ratio (r):</span>
        <span id="c9c8s14RLbl" class="text-amber-300 font-bold">r = 0.75</span>
      </div>
      <input id="c9c8s14R" type="range" min="0.4" max="0.9" step="0.05" value="0.75" oninput="c9c8s14Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 items-center">
    <svg id="c9c8s14Svg" viewBox="0 0 280 180" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c9c8s14Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
  </div>
</div>
<script>
(function(){
  window.c9c8s14Draw = function(){
    const h0 = parseFloat(document.getElementById('c9c8s14H').value);
    const r = parseFloat(document.getElementById('c9c8s14R').value);
    document.getElementById('c9c8s14HLbl').textContent = h0 + ' cm';
    document.getElementById('c9c8s14RLbl').textContent = 'r = ' + r.toFixed(2);
    const base = 160, ox = 28, dx = 36, scale = 135 / 200;
    let svg = `<line x1="16" y1="${base}" x2="268" y2="${base}" stroke="#475569" stroke-width="1.5"/>`;
    let pathD = '';
    const heights = [];
    for(let b = 0; b <= 6; b++){
      const h = h0 * Math.pow(r, b);
      heights.push(+h.toFixed(1));
      const x = ox + b * dx;
      const y = base - h * scale;
      pathD += (b === 0 ? `M ${x} ${y}` : ` L ${x} ${y}`);
      svg += `<line x1="${x}" y1="${base}" x2="${x}" y2="${y}" stroke="#334155" stroke-width="2"/>`;
      svg += `<circle cx="${x}" cy="${y}" r="5" fill="#fbbf24" stroke="#0f172a" stroke-width="1.5"/>`;
      svg += `<text x="${x}" y="${base+12}" text-anchor="middle" fill="#94a3b8" font-size="9">b=${b}</text>`;
    }
    svg = `<path d="${pathD}" fill="none" stroke="#22d3ee" stroke-width="2" stroke-dasharray="4 3"/>` + svg;
    document.getElementById('c9c8s14Svg').innerHTML = svg;
    document.getElementById('c9c8s14Out').innerHTML = `
      <div class="font-bold text-cyan-300">Exponential Decay Curve: h<sub>n</sub> = ${h0} · (${r.toFixed(2)})<sup>n</sup></div>
      <div>Bounce heights (cm): <strong class="text-white">${heights.join(', ')}</strong></div>
      <div class="text-emerald-300">Notice the curve bends smoothly rather than forming a straight AP line!</div>
    `;
  };
  setTimeout(window.c9c8s14Draw, 40);
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🛠️</span> AP Linear System &amp; Wage / Bacteria Growth Solver
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Given Term t<sub>3</sub> = a + 2d:</span>
      <input id="c9c8s15T3" type="number" value="14" oninput="c9c8s15Draw()" class="w-full mt-1.5 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Given Term t<sub>7</sub> = a + 6d:</span>
      <input id="c9c8s15T7" type="number" value="30" oninput="c9c8s15Draw()" class="w-full mt-1.5 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded-lg px-2.5 py-1.5">
    </label>
  </div>
  <div id="c9c8s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c8s15Draw = function(){
    const t3 = parseFloat(document.getElementById('c9c8s15T3').value || '0');
    const t7 = parseFloat(document.getElementById('c9c8s15T7').value || '0');
    const d = (t7 - t3) / 4;
    const a = t3 - 2 * d;
    document.getElementById('c9c8s15Out').innerHTML = `
      <div>Step 1 (Subtract Equations): (a + 6d) − (a + 2d) = ${t7} − ${t3} ⇒ 4d = ${t7 - t3} ⇒ <strong class="text-amber-300">d = ${d}</strong></div>
      <div>Step 2 (Substitute Back): a + 2(${d}) = ${t3} ⇒ <strong class="text-cyan-300">a = ${a}</strong></div>
      <div class="pt-1 border-t border-slate-800 text-emerald-300 font-bold">
        Explicit Rule: t<sub>n</sub> = ${a} + (n − 1)(${d}) &nbsp;|&nbsp; Recursive: t<sub>1</sub> = ${a}, t<sub>n</sub> = t<sub>n−1</sub> + (${d})
      </div>
    `;
  };
  setTimeout(window.c9c8s15Draw, 40);
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📚</span> Chapter 8 Complete Reference Matrix: AP vs GP vs Special Sequences
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c8s16Show('ap')" class="px-3 py-1.5 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 border border-cyan-500/40 text-cyan-200 font-bold">AP Summary</button>
    <button onclick="c9c8s16Show('gp')" class="px-3 py-1.5 rounded-lg bg-amber-600/30 hover:bg-amber-600/50 border border-amber-500/40 text-amber-200 font-bold">GP Summary</button>
    <button onclick="c9c8s16Show('spec')" class="px-3 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 border border-emerald-500/40 text-emerald-200 font-bold">Sums &amp; Virahānka</button>
  </div>
  <div id="c9c8s16Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const cards = {
    ap: `
      <div class="font-bold text-cyan-300 text-sm">Arithmetic Progression (AP)</div>
      <ul class="list-disc pl-4 space-y-1">
        <li><strong>Constant Common Difference:</strong> d = t<sub>n</sub> − t<sub>n−1</sub></li>
        <li><strong>Explicit Rule:</strong> t<sub>n</sub> = a + (n − 1)d</li>
        <li><strong>Recursive Rule:</strong> t<sub>1</sub> = a, t<sub>n</sub> = t<sub>n−1</sub> + d</li>
        <li><strong>Graph (n, t<sub>n</sub>):</strong> Collinear points along a straight line of slope d</li>
      </ul>`,
    gp: `
      <div class="font-bold text-amber-300 text-sm">Geometric Progression (GP)</div>
      <ul class="list-disc pl-4 space-y-1">
        <li><strong>Constant Common Ratio:</strong> r = t<sub>n</sub> / t<sub>n−1</sub> (a ≠ 0, r ≠ 0)</li>
        <li><strong>Explicit Rule:</strong> t<sub>n</sub> = a · r<sup>n−1</sup></li>
        <li><strong>Recursive Rule:</strong> t<sub>1</sub> = a, t<sub>n</sub> = r · t<sub>n−1</sub></li>
        <li><strong>Fractals &amp; Graph:</strong> Exponential curve; Sierpiński count 3<sup>n</sup>, area (3/4)<sup>n</sup></li>
      </ul>`,
    spec: `
      <div class="font-bold text-emerald-300 text-sm">Special Sequences &amp; Classical Sums</div>
      <ul class="list-disc pl-4 space-y-1">
        <li><strong>Sum of First n Naturals (Gauss / Āryabhaṭa):</strong> S<sub>n</sub> = n(n + 1)/2</li>
        <li><strong>Triangular Numbers:</strong> T<sub>n</sub> = n(n + 1)/2; T<sub>n−1</sub> + T<sub>n</sub> = n²</li>
        <li><strong>Square Numbers:</strong> 1 + 3 + 5 + ... + (2n − 1) = n²</li>
        <li><strong>Virahānka-Fibonacci:</strong> V<sub>1</sub> = 1, V<sub>2</sub> = 2, V<sub>n</sub> = V<sub>n−1</sub> + V<sub>n−2</sub></li>
      </ul>`
  };
  window.c9c8s16Show = function(key){
    document.getElementById('c9c8s16Out').innerHTML = cards[key] || cards.ap;
  };
  setTimeout(function(){ window.c9c8s16Show('ap'); }, 40);
})();
</script>
"""
}
