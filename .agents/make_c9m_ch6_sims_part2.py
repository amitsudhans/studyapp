#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 6: Measuring Space: Perimeter and Area
Part 2: Simulators 9 to 16 (Slides 9 to 16)
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📐</span> Triangle Doubling (½bh) &amp; Equal-Area Median Simulator
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Move Top Apex A Horizontally: <strong id="c9c6s9AxVal" class="text-amber-300">x = 75</strong></span>
      <input type="range" id="c9c6s9Ax" min="25" max="175" value="75" oninput="c9c6s9Draw()" class="w-full accent-amber-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 flex items-center gap-2 cursor-pointer">
      <input type="checkbox" id="c9c6s9Clone" onchange="c9c6s9Draw()" class="accent-cyan-400 w-4 h-4">
      <span class="text-cyan-300 font-semibold">Show Congruent Cloned Δ (Parallelogram bh)</span>
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c6s9Svg" viewBox="0 0 210 120" class="w-52 h-28 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c6s9Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c6s9Draw = function(){
    const ax = parseInt(document.getElementById('c9c6s9Ax').value);
    const clone = document.getElementById('c9c6s9Clone').checked;
    document.getElementById('c9c6s9AxVal').textContent = `x = ${ax}`;
    const bx = 40, cx = 160, yBot = 98, ay = 24;
    const dx = (bx + cx) / 2;
    let cloneSvg = '';
    if(clone){
      const px = ax + (cx - bx);
      cloneSvg = `<polygon points="${ax},${ay} ${px},${ay} ${cx},${yBot}" fill="#818cf8" fill-opacity="0.22" stroke="#a78bfa" stroke-width="1.5" stroke-dasharray="3 2"/>`;
    }
    document.getElementById('c9c6s9Svg').innerHTML = `
      <line x1="15" y1="${ay}" x2="195" y2="${ay}" stroke="#334155" stroke-dasharray="3 2"/>
      ${cloneSvg}
      <polygon points="${ax},${ay} ${bx},${yBot} ${dx},${yBot}" fill="#0ea5e9" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1.8"/>
      <polygon points="${ax},${ay} ${dx},${yBot} ${cx},${yBot}" fill="#10b981" fill-opacity="0.25" stroke="#34d399" stroke-width="1.8"/>
      <line x1="${ax}" y1="${ay}" x2="${dx}" y2="${yBot}" stroke="#fbbf24" stroke-width="2.2"/>
      <line x1="${ax}" y1="${ay}" x2="${ax}" y2="${yBot}" stroke="#f472b6" stroke-width="1.2" stroke-dasharray="2 2"/>
      <text x="${ax}" y="${ay-5}" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">A</text>
      <text x="${bx-6}" y="${yBot+11}" fill="#38bdf8" font-size="9">B</text>
      <text x="${dx}" y="${yBot+11}" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">D (Midpoint)</text>
      <text x="${cx+4}" y="${yBot+11}" fill="#34d399" font-size="9">C</text>
    `;
    document.getElementById('c9c6s9Out').innerHTML = `
      <div class="font-bold text-cyan-300">Base BC = 12 cm (BD = DC = 6 cm), Altitude h = 8 cm</div>
      <div class="font-mono text-sky-300">Area(ΔABD) = ½ × 6 × 8 = 24 cm²</div>
      <div class="font-mono text-emerald-300">Area(ΔACD) = ½ × 6 × 8 = 24 cm² (Always 100% EQUAL!)</div>
      <div class="text-[11px] text-amber-300 font-semibold">Even when ΔABD looks skewed and ΔACD looks acute, Median AD shares height h &amp; equal bases BD = DC!</div>
    `;
  };
  c9c6s9Draw();
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🧮</span> Heron's Formula Interactive Calculator: √[s(s − a)(s − b)(s − c)]
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Side a: <strong id="c9c6s10AVal" class="text-cyan-300">13</strong></span>
      <input type="range" id="c9c6s10A" min="3" max="25" value="13" oninput="c9c6s10Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Side b: <strong id="c9c6s10BVal" class="text-emerald-300">14</strong></span>
      <input type="range" id="c9c6s10B" min="3" max="25" value="14" oninput="c9c6s10Draw()" class="w-full accent-emerald-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Side c: <strong id="c9c6s10CVal" class="text-amber-300">15</strong></span>
      <input type="range" id="c9c6s10C" min="3" max="25" value="15" oninput="c9c6s10Draw()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <div id="c9c6s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c6s10Draw = function(){
    const a = parseInt(document.getElementById('c9c6s10A').value);
    const b = parseInt(document.getElementById('c9c6s10B').value);
    const c = parseInt(document.getElementById('c9c6s10C').value);
    document.getElementById('c9c6s10AVal').textContent = `${a} cm`;
    document.getElementById('c9c6s10BVal').textContent = `${b} cm`;
    document.getElementById('c9c6s10CVal').textContent = `${c} cm`;
    const out = document.getElementById('c9c6s10Out');
    if(a + b <= c || a + c <= b || b + c <= a){
      out.innerHTML = `<div class="text-rose-400 font-bold">Invalid Triangle: Sum of two sides must exceed third side (Triangle Inequality)!</div>`;
      return;
    }
    const s = (a + b + c) / 2;
    const prod = s * (s - a) * (s - b) * (s - c);
    const area = Math.sqrt(prod);
    out.innerHTML = `
      <div class="font-bold text-cyan-300">Step 1: Semi-perimeter s = (${a} + ${b} + ${c}) / 2 = ${s} cm</div>
      <div class="font-mono text-emerald-300">Step 2: s(s−a)(s−b)(s−c) = ${s} × ${(s-a).toFixed(1)} × ${(s-b).toFixed(1)} × ${(s-c).toFixed(1)} = ${prod.toFixed(2)}</div>
      <div class="font-mono text-amber-300 font-bold text-sm">Area = √(${prod.toFixed(2)}) = ${area.toFixed(3)} cm²</div>
      <div class="text-[11px] text-slate-400">Zero perpendicular altitude needed—sides alone completely lock triangle area!</div>
    `;
  };
  c9c6s10Draw();
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>⭕</span> Circle Radii (R &amp; r) &amp; Brahmagupta Cyclic Quad Explorer
  </h3>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Side a: <strong id="c9c6s11AVal" class="text-cyan-300">4</strong></span>
      <input type="range" id="c9c6s11A" min="2" max="12" value="4" oninput="c9c6s11Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Side b: <strong id="c9c6s11BVal" class="text-emerald-300">5</strong></span>
      <input type="range" id="c9c6s11B" min="2" max="12" value="5" oninput="c9c6s11Draw()" class="w-full accent-emerald-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Side c: <strong id="c9c6s11CVal" class="text-amber-300">6</strong></span>
      <input type="range" id="c9c6s11C" min="2" max="12" value="6" oninput="c9c6s11Draw()" class="w-full accent-amber-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Side d (set 0 ⇒ Δ!): <strong id="c9c6s11DVal" class="text-pink-300">7</strong></span>
      <input type="range" id="c9c6s11D" min="0" max="12" value="7" oninput="c9c6s11Draw()" class="w-full accent-pink-400 mt-1">
    </label>
  </div>
  <div id="c9c6s11Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c6s11Draw = function(){
    const a = parseInt(document.getElementById('c9c6s11A').value);
    const b = parseInt(document.getElementById('c9c6s11B').value);
    const c = parseInt(document.getElementById('c9c6s11C').value);
    const d = parseInt(document.getElementById('c9c6s11D').value);
    document.getElementById('c9c6s11AVal').textContent = a;
    document.getElementById('c9c6s11BVal').textContent = b;
    document.getElementById('c9c6s11CVal').textContent = c;
    document.getElementById('c9c6s11DVal').textContent = d;
    const s = (a + b + c + d) / 2;
    const p = (s - a) * (s - b) * (s - c) * (s - d);
    const out = document.getElementById('c9c6s11Out');
    if(p <= 0){
      out.innerHTML = `<div class="text-rose-400 font-bold">Longest side must be strictly smaller than the sum of the other sides to form a closed cyclic figure!</div>`;
      return;
    }
    const area = Math.sqrt(p);
    let extra = '';
    if(d === 0){
      const rIn = area / s;
      const Rcirc = (a * b * c) / (4 * area);
      extra = `<div class="font-mono text-cyan-300">Collapsed to Triangle! Inradius r = Area/s = ${rIn.toFixed(3)} | Circumradius R = abc/(4·Area) = ${Rcirc.toFixed(3)}</div>`;
    }
    out.innerHTML = `
      <div class="font-bold text-amber-300">Brahmagupta's Cyclic Formula (s = ${s}): √[(s−a)(s−b)(s−c)(s−d)] = √(${p.toFixed(2)}) = <span class="text-emerald-300 text-sm">${area.toFixed(3)} units²</span></div>
      ${extra}
      <div class="text-[11px] text-slate-300">Try sliding side <strong>d down to 0</strong>: factor (s − d) turns into (s − 0) = s, directly recovering Heron's Triangle Formula &amp; R, r circle relations!</div>
    `;
  };
  c9c6s11Draw();
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-violet-300 flex items-center gap-2">
    <span>🏛️</span> Baudhāyana's Śhulbasūtra (c. 800 BCE): Squaring a Rectangle
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Length a: <strong id="c9c6s12AVal" class="text-cyan-300">9 cm</strong></span>
      <input type="range" id="c9c6s12A" min="5" max="16" value="9" oninput="c9c6s12Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Breadth b: <strong id="c9c6s12BVal" class="text-emerald-300">4 cm</strong></span>
      <input type="range" id="c9c6s12B" min="2" max="10" value="4" oninput="c9c6s12Draw()" class="w-full accent-emerald-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Construction Stage: <strong id="c9c6s12StVal" class="text-amber-300">Step 1</strong></span>
      <input type="range" id="c9c6s12St" min="1" max="4" value="1" oninput="c9c6s12Draw()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <div id="c9c6s12Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c6s12Draw = function(){
    let a = parseInt(document.getElementById('c9c6s12A').value);
    let b = parseInt(document.getElementById('c9c6s12B').value);
    if(b >= a) a = b + 1;
    const st = parseInt(document.getElementById('c9c6s12St').value);
    document.getElementById('c9c6s12AVal').textContent = `${a} cm`;
    document.getElementById('c9c6s12BVal').textContent = `${b} cm`;
    document.getElementById('c9c6s12StVal').textContent = `Step ${st}`;
    const big = (a + b) / 2, small = (a - b) / 2, sqSide = Math.sqrt(a * b);
    const steps = {
      1: `Start with ${a} × ${b} Rectangle of Area = ab = ${a*b} cm². Cut off inner b×b (${b}×${b} = ${b*b}) square, leaving (${a}−${b})×${b} strip.`,
      2: `Bisect leftover width (${a}−${b}) into two half-strips of width (a−b)/2 = ${small.toFixed(1)} cm, placing one along the bottom to form an L-gnomon.`,
      3: `Fill tiny corner (${small.toFixed(1)}²) virtually to complete large square of side (a+b)/2 = ${big.toFixed(1)} cm (Area = ${(big*big).toFixed(2)} cm²).`,
      4: `Subtract corner square via Baudhāyana-Pythagoras right triangle (hyp=${big.toFixed(1)}, leg=${small.toFixed(1)}): Equal-area Square Side = √(${a}×${b}) = ${sqSide.toFixed(3)} cm!`
    };
    document.getElementById('c9c6s12Out').innerHTML = `
      <div class="font-bold text-amber-300">Identity: [(a + b)/2]² − [(a − b)/2]² = ${big.toFixed(1)}² − ${small.toFixed(1)}² = ${a*b} cm² = Area(${a} × ${b})</div>
      <div class="text-cyan-200 font-semibold">${steps[st]}</div>
      <div class="font-mono text-emerald-300 font-bold">Constructed Square Side = √(ab) = √(${a*b}) = ${sqSide.toFixed(3)} cm ⇒ Square Area = ${a*b} cm²</div>
    `;
  };
  c9c6s12Draw();
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🍕</span> Nilakantha Somayājī's Circle Slice-Rearrangement Proof (Area = πr²)
  </h3>
  <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Number of Equal Wedge Slices N: <strong id="c9c6s13NVal" class="text-amber-300">16 slices</strong></span>
    <input type="range" id="c9c6s13N" min="8" max="48" step="4" value="16" oninput="c9c6s13Draw()" class="w-full accent-amber-400 mt-1">
  </label>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c6s13Svg" viewBox="0 0 260 110" class="w-60 h-28 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c6s13Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c6s13Draw = function(){
    const N = parseInt(document.getElementById('c9c6s13N').value);
    document.getElementById('c9c6s13NVal').textContent = `${N} slices`;
    const cx = 50, cy = 55, r = 38;
    let wheel = '';
    for(let i=0; i<N; i++){
      const a1 = (2*Math.PI*i)/N, a2 = (2*Math.PI*(i+1))/N;
      const x1 = cx + r*Math.cos(a1), y1 = cy + r*Math.sin(a1);
      const x2 = cx + r*Math.cos(a2), y2 = cy + r*Math.sin(a2);
      const col = i%2===0 ? '#22d3ee' : '#f472b6';
      wheel += `<path d="M ${cx} ${cy} L ${x1.toFixed(1)} ${y1.toFixed(1)} A ${r} ${r} 0 0 1 ${x2.toFixed(1)} ${y2.toFixed(1)} Z" fill="${col}" fill-opacity="0.4" stroke="#0f172a" stroke-width="0.6"/>`;
    }
    const baseW = 120, step = baseW / (N/2), xStart = 115, yTop = 36, yBot = 74;
    let strip = '';
    for(let i=0; i<N/2; i++){
      const sx = xStart + i*step;
      strip += `<polygon points="${sx},${yBot} ${sx+step/2},${yTop} ${sx+step},${yBot}" fill="#22d3ee" fill-opacity="0.55" stroke="#0f172a" stroke-width="0.5"/>`;
      strip += `<polygon points="${sx+step/2},${yTop} ${sx+1.5*step},${yTop} ${sx+step},${yBot}" fill="#f472b6" fill-opacity="0.55" stroke="#0f172a" stroke-width="0.5"/>`;
    }
    document.getElementById('c9c6s13Svg').innerHTML = wheel + strip + `
      <text x="${xStart+baseW/2}" y="${yBot+15}" fill="#34d399" font-size="8.5" font-weight="bold" text-anchor="middle">Base ≈ ½ Circumference = πr</text>
      <text x="108" y="${(yTop+yBot)/2}" fill="#fbbf24" font-size="8.5" font-weight="bold" text-anchor="end">r</text>
    `;
    document.getElementById('c9c6s13Out').innerHTML = `
      <div class="font-bold text-cyan-300">Interleaved ${N/2} Cyan + ${N/2} Pink Wedges</div>
      <div class="font-mono text-emerald-300">Parallelogram Base = Half of Circle Crust = ½(2πr) = πr</div>
      <div class="font-mono text-amber-300 font-bold">Height = Radius r ⇒ Area = Base × Height = (πr)(r) = πr²!</div>
      <div class="text-[11px] text-slate-400">More slices flatten scalloped edges smoothly into an exact πr × r rectangle!</div>
    `;
  };
  c9c6s13Draw();
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-pink-300 flex items-center gap-2">
    <span>🍰</span> Sector (πr²·θ°/360°) &amp; Chord-Bounded Circular Segment Explorer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Central Angle θ°: <strong id="c9c6s14AngVal" class="text-cyan-300">90°</strong></span>
      <input type="range" id="c9c6s14Ang" min="30" max="180" step="15" value="90" oninput="c9c6s14Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Radius r: <strong id="c9c6s14RVal" class="text-emerald-300">14 cm</strong></span>
      <input type="range" id="c9c6s14R" min="7" max="21" step="7" value="14" oninput="c9c6s14Draw()" class="w-full accent-emerald-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c6s14Svg" viewBox="0 0 160 150" class="w-40 h-36 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c6s14Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c6s14Draw = function(){
    const deg = parseInt(document.getElementById('c9c6s14Ang').value);
    const r = parseInt(document.getElementById('c9c6s14R').value);
    document.getElementById('c9c6s14AngVal').textContent = `${deg}°`;
    document.getElementById('c9c6s14RVal').textContent = `${r} cm`;
    const cx = 80, cy = 80, pxR = 52;
    const rad = deg * Math.PI / 180;
    const x1 = cx - pxR*Math.sin(rad/2), y1 = cy - pxR*Math.cos(rad/2);
    const x2 = cx + pxR*Math.sin(rad/2), y2 = cy - pxR*Math.cos(rad/2);
    const sector = Math.PI * r * r * deg / 360;
    const tri = 0.5 * r * r * Math.sin(rad);
    const seg = sector - tri;
    document.getElementById('c9c6s14Svg').innerHTML = `
      <circle cx="${cx}" cy="${cy}" r="${pxR}" fill="none" stroke="#334155" stroke-width="1.5"/>
      <path d="M ${cx} ${cy} L ${x1} ${y1} A ${pxR} ${pxR} 0 0 1 ${x2} ${y2} Z" fill="#0ea5e9" fill-opacity="0.22" stroke="#38bdf8" stroke-width="2"/>
      <path d="M ${x1} ${y1} A ${pxR} ${pxR} 0 0 1 ${x2} ${y2} Z" fill="#f472b6" fill-opacity="0.45"/>
      <line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#fbbf24" stroke-width="2"/>
      <text x="${cx}" y="${cy+12}" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle">O</text>
      <text x="${cx}" y="${y1-6}" fill="#f472b6" font-size="8" font-weight="bold" text-anchor="middle">Segment Cap</text>
    `;
    document.getElementById('c9c6s14Out').innerHTML = `
      <div class="font-bold text-cyan-300">Sector Area OAB = π(${r}²)(${deg}°/360°) = ${sector.toFixed(2)} cm²</div>
      <div class="font-mono text-amber-300">Central ΔOAB = ½ r² sin(${deg}°) = ${tri.toFixed(2)} cm²</div>
      <div class="font-mono text-pink-300 font-bold">Minor Segment (Pink Cap) = Sector − ΔOAB = ${seg.toFixed(2)} cm²</div>
    `;
  };
  c9c6s14Draw();
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🎡</span> Rolling Wheel Revolutions &amp; Ring Difference (R² − r²) Calculator
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Wheel Radius r (cm): <strong id="c9c6s15WVal" class="text-cyan-300">35 cm</strong></span>
      <input type="range" id="c9c6s15W" min="14" max="70" step="7" value="35" oninput="c9c6s15Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Distance (km): <strong id="c9c6s15DVal" class="text-emerald-300">1.1 km</strong></span>
      <input type="range" id="c9c6s15D" min="0.55" max="3.3" step="0.55" value="1.1" oninput="c9c6s15Draw()" class="w-full accent-emerald-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800 block">
      <span class="text-slate-300">Track Outer Radius R (m): <strong id="c9c6s15RVal" class="text-amber-300">21 m</strong></span>
      <input type="range" id="c9c6s15R" min="16" max="30" value="21" oninput="c9c6s15Draw()" class="w-full accent-amber-400 mt-1">
    </label>
  </div>
  <div id="c9c6s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c6s15Draw = function(){
    const r = parseInt(document.getElementById('c9c6s15W').value);
    const dKm = parseFloat(document.getElementById('c9c6s15D').value);
    const R = parseInt(document.getElementById('c9c6s15R').value);
    document.getElementById('c9c6s15WVal').textContent = `${r} cm`;
    document.getElementById('c9c6s15DVal').textContent = `${dKm.toFixed(2)} km`;
    document.getElementById('c9c6s15RVal').textContent = `${R} m`;
    const C = 2 * (22/7) * r;
    const distCm = dKm * 100000;
    const revs = distCm / C;
    const innerR = 14;
    const ringArea = (22/7) * (R + innerR) * (R - innerR);
    document.getElementById('c9c6s15Out').innerHTML = `
      <div class="font-bold text-cyan-300">Wheel Circumference = 2 × (22/7) × ${r} = ${C.toFixed(0)} cm | Distance = ${distCm.toLocaleString()} cm</div>
      <div class="font-mono text-emerald-300 font-bold">Complete Revolutions = Distance / Circumference = ${revs.toFixed(1)} turns</div>
      <div class="font-mono text-amber-300">Algebraic Ring (R=${R}m, r=14m): π(R+r)(R−r) = (22/7)(${R+14})(${R-14}) = ${ringArea.toFixed(2)} m²</div>
    `;
  };
  c9c6s15Draw();
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏆</span> Chapter 6 Complete Formula &amp; Proof Reference Matrix
  </h3>
  <select id="c9c6s16Filter" onchange="c9c6s16Draw()" class="w-full sm:w-72 bg-slate-950 text-cyan-300 font-bold border border-slate-700 rounded-xl px-3 py-1.5 text-xs">
    <option value="all">All Chapter 6 Pillars (6.1–6.10.1)</option>
    <option value="peri">Perimeters, π History &amp; Arcs (6.1–6.5)</option>
    <option value="poly">Rectangles, Parallelograms &amp; Triangles (6.6–6.8)</option>
    <option value="adv">Heron, Brahmagupta &amp; Baudhāyana (6.8.1–6.9)</option>
    <option value="circ">Circle Area, Sectors &amp; Segments (6.10–6.10.1)</option>
  </select>
  <div id="c9c6s16Out" class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs"></div>
</div>
<script>
(function(){
  const cards = [
    {g:'peri', title:'Polygons &amp; Circle C/D = π', body:'Square 4a, Eq. Δ 3a, Rect 2(a+b); Circle C = πD = 2πr. Lambert (1761): π irrational; 22/7 &amp; 355/113 are rational ≈.'},
    {g:'peri', title:'Arcs &amp; 400m Track Stagger', body:'Arc = 2πr(θ°/360°). Semicircle closed P = πr + 2r. Track lane stagger = 2πw per lane.'},
    {g:'poly', title:'Rectangle &amp; Parallelogram', body:'Rect Area = ab. Parallelogram Area = b × h (never slant side! Holds for oblique shapes via shear).'},
    {g:'poly', title:'Triangle &amp; Median Split', body:'Triangle Area = ½bh (via rectangle or parallelogram doubling). Any median splits triangle into 2 equal-area halves.'},
    {g:'adv', title:'Heron &amp; Circle Connections', body:'s = (a+b+c)/2; Area = √[s(s−a)(s−b)(s−c)] = rs = abc/(4R). Brahmagupta cyclic quad: √[(s−a)(s−b)(s−c)(s−d)].'},
    {g:'adv', title:'Baudhāyana Squaring (~800 BCE)', body:'Equal-area square side √(ab) via gnomon identity [(a+b)/2]² − [(a−b)/2]² = ab.'},
    {g:'circ', title:'Circle Area Proofs (πr²)', body:'Archimedes (n-gon triangle limit ½·P·h → πr²) &amp; Nilakantha Somayājī (interleaved slice parallelogram base πr × height r).'},
    {g:'circ', title:'Sectors, Segments &amp; Wheels', body:'Sector = πr²(θ°/360°); Minor Segment = Sector − ΔOAB; Wheel turns = Distance / (2πr).'}
  ];
  window.c9c6s16Draw = function(){
    const f = document.getElementById('c9c6s16Filter').value;
    const shown = f === 'all' ? cards : cards.filter(c => c.g === f);
    document.getElementById('c9c6s16Out').innerHTML = shown.map(c => `
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-1">
        <div class="font-bold text-amber-300">${c.title}</div>
        <div class="text-slate-300 leading-relaxed">${c.body}</div>
      </div>
    `).join('');
  };
  c9c6s16Draw();
})();
</script>
"""
}
