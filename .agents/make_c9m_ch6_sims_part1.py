#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 6: Measuring Space: Perimeter and Area
Part 1: Simulators 1 to 8 (Slides 1 to 8)
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📏</span> Polygon &amp; Circle Border Perimeter Explorer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Shape Type</span>
      <select id="c9c6s1Shape" onchange="c9c6s1Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded-lg px-2 py-1">
        <option value="rect">Rectangle 2(a + b)</option>
        <option value="sq">Square 4a</option>
        <option value="tri">Equilateral Δ 3a</option>
        <option value="circ">Circle 2πr</option>
      </select>
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Side / Radius a (or r): <strong id="c9c6s1AVal" class="text-cyan-300">8 cm</strong></span>
      <input type="range" id="c9c6s1A" min="3" max="14" value="8" oninput="c9c6s1Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block" id="c9c6s1BWrap">
      <span class="text-slate-300 font-semibold">Breadth b: <strong id="c9c6s1BVal" class="text-emerald-300">5 cm</strong></span>
      <input type="range" id="c9c6s1B" min="3" max="12" value="5" oninput="c9c6s1Draw()" class="w-full accent-emerald-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c6s1Svg" viewBox="0 0 180 140" class="w-44 h-36 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c6s1Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c6s1Draw = function(){
    const sh = document.getElementById('c9c6s1Shape').value;
    const a = parseInt(document.getElementById('c9c6s1A').value);
    const b = parseInt(document.getElementById('c9c6s1B').value);
    document.getElementById('c9c6s1AVal').textContent = `${a} cm`;
    document.getElementById('c9c6s1BVal').textContent = `${b} cm`;
    document.getElementById('c9c6s1BWrap').style.opacity = (sh === 'rect') ? '1' : '0.4';
    let svg = '', formula = '', peri = '', area = '';
    if(sh === 'rect'){
      const w = a * 9, h = b * 8;
      const x = 90 - w/2, y = 70 - h/2;
      svg = `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="#0891b2" fill-opacity="0.18" stroke="#22d3ee" stroke-width="2.5"/>
             <text x="90" y="${y-5}" fill="#22d3ee" font-size="9" text-anchor="middle" font-weight="bold">a = ${a} cm</text>
             <text x="${x-6}" y="73" fill="#34d399" font-size="9" text-anchor="end" font-weight="bold">b=${b}</text>`;
      formula = `2(a + b) = 2(${a} + ${b})`;
      peri = `${2*(a+b)} cm`;
      area = `${a*b} cm²`;
    } else if(sh === 'sq'){
      const s = a * 7;
      const x = 90 - s/2, y = 70 - s/2;
      svg = `<rect x="${x}" y="${y}" width="${s}" height="${s}" fill="#10b981" fill-opacity="0.18" stroke="#34d399" stroke-width="2.5"/>
             <text x="90" y="${y-5}" fill="#34d399" font-size="9" text-anchor="middle" font-weight="bold">a = ${a} cm</text>`;
      formula = `4a = 4 × ${a}`;
      peri = `${4*a} cm`;
      area = `${a*a} cm²`;
    } else if(sh === 'tri'){
      const s = a * 8, h = s * 0.866;
      const p1 = `${90},${70 - h*0.55}`, p2 = `${90 - s/2},${70 + h*0.45}`, p3 = `${90 + s/2},${70 + h*0.45}`;
      svg = `<polygon points="${p1} ${p2} ${p3}" fill="#f59e0b" fill-opacity="0.18" stroke="#fbbf24" stroke-width="2.5"/>
             <text x="90" y="${70 + h*0.45 + 12}" fill="#fbbf24" font-size="9" text-anchor="middle" font-weight="bold">a = ${a} cm (each edge)</text>`;
      formula = `3a = 3 × ${a}`;
      peri = `${3*a} cm`;
      area = `${(0.433*a*a).toFixed(2)} cm²`;
    } else {
      const r = a * 3.8;
      svg = `<circle cx="90" cy="70" r="${r}" fill="#818cf8" fill-opacity="0.18" stroke="#a78bfa" stroke-width="2.5"/>
             <line x1="90" y1="70" x2="${90+r}" y2="70" stroke="#fbbf24" stroke-width="1.8"/>
             <circle cx="90" cy="70" r="3" fill="#fbbf24"/>
             <text x="${90+r/2}" y="64" fill="#fbbf24" font-size="9" text-anchor="middle" font-weight="bold">r=${a}</text>`;
      formula = `2πr = 2π(${a}) ≈ ${(2*Math.PI*a).toFixed(2)}`;
      peri = `${(2*Math.PI*a).toFixed(2)} cm (Circumference)`;
      area = `${(Math.PI*a*a).toFixed(2)} cm²`;
    }
    document.getElementById('c9c6s1Svg').innerHTML = svg;
    document.getElementById('c9c6s1Out').innerHTML = `
      <div class="font-bold text-cyan-300">Formula: ${formula}</div>
      <div class="font-mono text-emerald-300 font-bold text-sm">Perimeter (1D Border) = ${peri}</div>
      <div class="text-amber-300">Enclosed 2D Area = ${area}</div>
      <div class="text-[11px] text-slate-400">Straight edges use rulers cleanly; circular curves unlock the constant π = C/D!</div>
    `;
  };
  c9c6s1Draw();
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>⬡</span> Archimedes' 96-Gon Sandwich: Trapping π = C / D
  </h3>
  <div class="flex flex-wrap gap-2 text-xs items-center">
    <span class="text-slate-300 font-semibold">Polygon Sides n:</span>
    <button onclick="c9c6s2Set(6)" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-cyan-700 text-cyan-200 font-bold border border-slate-700">6 (Hexagon)</button>
    <button onclick="c9c6s2Set(12)" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-cyan-700 text-cyan-200 font-bold border border-slate-700">12</button>
    <button onclick="c9c6s2Set(24)" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-cyan-700 text-cyan-200 font-bold border border-slate-700">24</button>
    <button onclick="c9c6s2Set(48)" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-cyan-700 text-cyan-200 font-bold border border-slate-700">48</button>
    <button onclick="c9c6s2Set(96)" class="px-2.5 py-1 rounded-lg bg-amber-600 hover:bg-amber-500 text-slate-950 font-extrabold">96 (Archimedes)</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c6s2Svg" viewBox="0 0 160 150" class="w-40 h-36 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c6s2Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  let sides = 6;
  window.c9c6s2Set = function(n){ sides = n; c9c6s2Draw(); };
  window.c9c6s2Draw = function(){
    const cx = 80, cy = 75, r = 50;
    const drawN = Math.min(sides, 48);
    let inPts = [], outPts = [];
    const rOut = r / Math.cos(Math.PI / sides);
    for(let i=0; i<drawN; i++){
      const ang = (2 * Math.PI * i) / drawN - Math.PI/2;
      inPts.push(`${(cx + r*Math.cos(ang)).toFixed(1)},${(cy + r*Math.sin(ang)).toFixed(1)}`);
      outPts.push(`${(cx + rOut*Math.cos(ang)).toFixed(1)},${(cy + rOut*Math.sin(ang)).toFixed(1)}`);
    }
    const lower = (sides * Math.sin(Math.PI / sides)).toFixed(6);
    const upper = (sides * Math.tan(Math.PI / sides)).toFixed(6);
    document.getElementById('c9c6s2Svg').innerHTML = `
      <polygon points="${outPts.join(' ')}" fill="none" stroke="#f472b6" stroke-width="1.6" stroke-dasharray="3 2"/>
      <circle cx="${cx}" cy="${cy}" r="${r}" fill="#0891b2" fill-opacity="0.16" stroke="#22d3ee" stroke-width="2.5"/>
      <polygon points="${inPts.join(' ')}" fill="none" stroke="#34d399" stroke-width="1.8"/>
      <text x="${cx}" y="${cy+4}" fill="#fbbf24" font-size="10" text-anchor="middle" font-weight="bold">n = ${sides}</text>
    `;
    document.getElementById('c9c6s2Out').innerHTML = `
      <div class="font-bold text-amber-300">n = ${sides}-Sided Inscribed (green) &amp; Circumscribed (pink) Polygons</div>
      <div class="font-mono text-emerald-300">Lower Bound (Inscribed): ${lower} &lt; π</div>
      <div class="font-mono text-pink-300">Upper Bound (Circumscribed): π &lt; ${upper}</div>
      <div class="text-cyan-300 font-semibold">${sides===6 ? 'Mesopotamia (~1900 BCE) started with n=6 hexagon (3.0) and refined to 3.125 (3 1/8)!' : sides===96 ? 'Archimedes (250 BCE) proved: 3 10/71 (3.140845) < π < 3 1/7 (3.142857)!' : 'Increasing polygon sides squeezes lower and upper bounds tighter around π ≈ 3.141593!'}</div>
    `;
  };
  c9c6s2Draw();
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🌏</span> Global π Scholars &amp; Mādhava's Infinite Series Convergence
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Historical Milestone</span>
      <select id="c9c6s3Scholar" onchange="c9c6s3Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded-lg px-2 py-1">
        <option value="meso">Mesopotamia (~1900 BCE): 25/8 = 3.125</option>
        <option value="arch">Archimedes (250 BCE): 223/71 &lt; π &lt; 22/7</option>
        <option value="arya">Āryabhaṭa (499 CE): 62832/20000 = 3.1416</option>
        <option value="brah">Brahmagupta (628 CE): √10 ≈ 3.162278</option>
        <option value="zu">Zu Chongzhi (480 CE): 355/113 ≈ 3.1415929</option>
      </select>
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Mādhava Series Terms N (4·Σ(-1)^k/(2k+1)): <strong id="c9c6s3NVal" class="text-cyan-300">10</strong></span>
      <input type="range" id="c9c6s3N" min="1" max="50" value="10" oninput="c9c6s3Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c6s3Svg" viewBox="0 0 210 110" class="w-52 h-28 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c6s3Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1 w-full"></div>
  </div>
</div>
<script>
(function(){
  const info = {
    meso: {val: 3.125, err: Math.abs(3.125-Math.PI).toFixed(6), note: 'Clay tablet scribes used inscribed hexagon (3) refined by 25/8.'},
    arch: {val: 22/7, err: Math.abs(22/7-Math.PI).toFixed(6), note: '96-gon upper bound 22/7 ≈ 3.142857 & lower 223/71 ≈ 3.140845.'},
    arya: {val: 3.1416, err: Math.abs(3.1416-Math.PI).toFixed(6), note: 'Āryabhaṭīya stated 62832/20000 = 3.1416 (accurate to 4 decimals).'},
    brah: {val: Math.sqrt(10), err: Math.abs(Math.sqrt(10)-Math.PI).toFixed(6), note: 'Quick radical surrogate √10 used cleanly in astronomical verses.'},
    zu: {val: 355/113, err: Math.abs(355/113-Math.PI).toFixed(7), note: '24,576-gon Milü fraction 355/113 stays accurate to 6 decimal places!'}
  };
  window.c9c6s3Draw = function(){
    const key = document.getElementById('c9c6s3Scholar').value;
    const N = parseInt(document.getElementById('c9c6s3N').value);
    document.getElementById('c9c6s3NVal').textContent = N;
    let sum = 0, pts = [];
    for(let k=0; k<N; k++){
      sum += (k%2===0 ? 1 : -1) / (2*k + 1);
      const approx = 4 * sum;
      const x = 12 + (k / Math.max(N-1,1)) * 186;
      const y = 55 - (approx - Math.PI) * 35;
      pts.push(`${x.toFixed(1)},${Math.max(10, Math.min(100, y)).toFixed(1)}`);
    }
    const mApprox = 4 * sum;
    const d = info[key];
    document.getElementById('c9c6s3Svg').innerHTML = `
      <line x1="10" y1="55" x2="200" y2="55" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="4 3"/>
      <text x="14" y="51" fill="#fbbf24" font-size="8" font-weight="bold">True π = 3.14159...</text>
      <polyline points="${pts.join(' ')}" fill="none" stroke="#22d3ee" stroke-width="2"/>
    `;
    document.getElementById('c9c6s3Out').innerHTML = `
      <div class="font-bold text-amber-300">Selected Estimate: ≈ ${d.val.toFixed(6)} (Error: ${d.err})</div>
      <div class="text-[11px] text-slate-300">${d.note}</div>
      <div class="font-mono text-cyan-300 font-bold">Mādhava π (N=${N} terms): 4(1 - 1/3 + ...) ≈ ${mApprox.toFixed(5)}</div>
      <div class="text-[11px] text-emerald-300">Notice oscillating zigzag narrowing cleanly around π! (Nilakantha's series converges even faster.)</div>
    `;
  };
  c9c6s3Draw();
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-pink-300 flex items-center gap-2">
    <span>♾️</span> Why π is Irrational (Lambert 1761): Exact π vs ≈ Approximations
  </h3>
  <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block text-xs">
    <span class="text-slate-300 font-semibold">Circle Radius r for Circumference Comparison: <strong id="c9c6s4RVal" class="text-cyan-300">50 m</strong></span>
    <input type="range" id="c9c6s4R" min="7" max="140" step="7" value="49" oninput="c9c6s4Draw()" class="w-full accent-pink-400 mt-1">
  </label>
  <div id="c9c6s4Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c6s4Draw = function(){
    const r = parseInt(document.getElementById('c9c6s4R').value);
    document.getElementById('c9c6s4RVal').textContent = `${r} m`;
    const cExact = 2 * Math.PI * r;
    const c22_7 = 2 * (22/7) * r;
    const c314 = 2 * 3.14 * r;
    const c355 = 2 * (355/113) * r;
    document.getElementById('c9c6s4Out').innerHTML = `
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
        <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
          <div class="text-amber-300 font-bold">Irrational True π</div>
          <div class="font-mono text-white text-[11px]">3.141592653589793... (Never ends, never repeats!)</div>
          <div class="text-cyan-300 font-mono mt-1">Exact C = 2π(${r}) ≈ ${cExact.toFixed(4)} m</div>
        </div>
        <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
          <div class="text-pink-300 font-bold">Rational 22/7 (Pi Approx Day: July 22)</div>
          <div class="font-mono text-slate-200 text-[11px]">3.<span class="underline decoration-pink-400">142857</span>142857... (Repeats every 6 digits)</div>
          <div class="text-pink-300 font-mono mt-1">2(22/7)(${r}) = ${c22_7.toFixed(4)} m (Δ = +${(c22_7-cExact).toFixed(4)} m)</div>
        </div>
        <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
          <div class="text-emerald-300 font-bold">Decimal 3.14 (Pi Day: March 14)</div>
          <div class="font-mono text-slate-200 text-[11px]">3.140000... (Terminates at hundredths)</div>
          <div class="text-emerald-300 font-mono mt-1">2(3.14)(${r}) = ${c314.toFixed(4)} m (Δ = ${(c314-cExact).toFixed(4)} m)</div>
        </div>
        <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
          <div class="text-indigo-300 font-bold">Zu Chongzhi 355/113</div>
          <div class="font-mono text-slate-200 text-[11px]">3.1415929203... (6 correct digits!)</div>
          <div class="text-indigo-300 font-mono mt-1">2(355/113)(${r}) = ${c355.toFixed(6)} m (Δ = +${(c355-cExact).toFixed(6)} m)</div>
        </div>
      </div>
      <div class="text-[11px] text-amber-200 font-semibold">Remember: Johann Lambert (1761) proved π ≠ p/q! Always treat 22/7 and 3.14 as approximations (≈).</div>
    `;
  };
  c9c6s4Draw();
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏟️</span> Arc Length &amp; 400 m Olympic Track Stagger Simulator
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Sector Angle θ°: <strong id="c9c6s5AngVal" class="text-cyan-300">90°</strong></span>
      <input type="range" id="c9c6s5Ang" min="30" max="360" step="15" value="90" oninput="c9c6s5Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Lane Number (1–6): <strong id="c9c6s5LaneVal" class="text-amber-300">Lane 2</strong></span>
      <input type="range" id="c9c6s5Lane" min="1" max="6" value="2" oninput="c9c6s5Draw()" class="w-full accent-amber-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Lane Width w (m): <strong id="c9c6s5WVal" class="text-emerald-300">1.22 m</strong></span>
      <input type="range" id="c9c6s5W" min="1.0" max="1.5" step="0.02" value="1.22" oninput="c9c6s5Draw()" class="w-full accent-emerald-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c6s5Svg" viewBox="0 0 200 120" class="w-48 h-28 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c6s5Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c6s5Draw = function(){
    const ang = parseInt(document.getElementById('c9c6s5Ang').value);
    const lane = parseInt(document.getElementById('c9c6s5Lane').value);
    const w = parseFloat(document.getElementById('c9c6s5W').value);
    document.getElementById('c9c6s5AngVal').textContent = `${ang}°`;
    document.getElementById('c9c6s5LaneVal').textContent = `Lane ${lane}`;
    document.getElementById('c9c6s5WVal').textContent = `${w.toFixed(2)} m`;
    const r = 14, arc = 2 * Math.PI * r * ang / 360;
    const stagger = 2 * Math.PI * w * (lane - 1);
    const tracks = [1,2,3,4,5,6].map(k => {
      const pad = (k-1)*3.5;
      const stroke = k === lane ? '#fbbf24' : '#334155';
      const sw = k === lane ? '2' : '1';
      return `<rect x="${30-pad}" y="${25-pad}" width="${140+2*pad}" height="${70+2*pad}" rx="${35+pad}" fill="none" stroke="${stroke}" stroke-width="${sw}"/>`;
    }).join('');
    document.getElementById('c9c6s5Svg').innerHTML = tracks + `
      <text x="100" y="56" fill="#22d3ee" font-size="9" text-anchor="middle" font-weight="bold">84.39 m straights (equal)</text>
      <text x="100" y="70" fill="#fbbf24" font-size="9" text-anchor="middle" font-weight="bold">Stagger = +${stagger.toFixed(2)} m</text>
    `;
    document.getElementById('c9c6s5Out').innerHTML = `
      <div class="font-bold text-cyan-300">Arc Length (r=14 cm, θ=${ang}°): 2πr(${ang}/360) = ${arc.toFixed(2)} cm</div>
      <div class="font-mono text-amber-300 font-bold">Lane ${lane} Stagger Ahead of Lane 1 = 2πw(${lane-1}) = +${stagger.toFixed(2)} m</div>
      <div class="text-[11px] text-slate-300">Why? Two straights (2×84.39 m) stay identical, while two outer semicircular bends add ΔC = 2π(w×${lane-1})!</div>
    `;
  };
  c9c6s5Draw();
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-violet-300 flex items-center gap-2">
    <span>🌸</span> Semicircle Path Paradox &amp; 4-Petal Flower Border Explorer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Mode</span>
      <select id="c9c6s6Mode" onchange="c9c6s6Draw()" class="w-full mt-1 bg-slate-900 text-violet-300 font-bold border border-slate-700 rounded-lg px-2 py-1">
        <option value="semi">Semicircle Chain Paradox (D = 20 cm)</option>
        <option value="petal">4-Petal Flower Inside Square (a = 14 cm)</option>
      </select>
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Small Semicircles Count N (for Chain): <strong id="c9c6s6NVal" class="text-cyan-300">4</strong></span>
      <input type="range" id="c9c6s6N" min="2" max="6" value="4" oninput="c9c6s6Draw()" class="w-full accent-violet-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c6s6Svg" viewBox="0 0 200 120" class="w-48 h-28 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c6s6Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c6s6Draw = function(){
    const mode = document.getElementById('c9c6s6Mode').value;
    const n = parseInt(document.getElementById('c9c6s6N').value);
    document.getElementById('c9c6s6NVal').textContent = n;
    if(mode === 'semi'){
      const x0 = 20, x1 = 180, span = x1 - x0, y = 75;
      const d = span / n, r = d / 2;
      let chain = '';
      for(let i=0; i<n; i++){
        const sx = x0 + i*d, ex = sx + d;
        chain += `<path d="M ${sx} ${y} A ${r} ${r} 0 0 0 ${ex} ${y}" fill="none" stroke="#34d399" stroke-width="2.5"/>`;
      }
      document.getElementById('c9c6s6Svg').innerHTML = `
        <line x1="${x0}" y1="${y}" x2="${x1}" y2="${y}" stroke="#475569" stroke-width="1" stroke-dasharray="3 2"/>
        <path d="M ${x0} ${y} A ${span/2} ${span/2} 0 0 1 ${x1} ${y}" fill="none" stroke="#22d3ee" stroke-width="2.5"/>
        ${chain}
      `;
      document.getElementById('c9c6s6Out').innerHTML = `
        <div class="font-bold text-cyan-300">Big Semicircle (Cyan, D = 20 cm): Length = π(20)/2 = 10π ≈ ${(10*Math.PI).toFixed(2)} cm</div>
        <div class="font-bold text-emerald-300">${n} Small Semicircles (Green, d = ${(20/n).toFixed(2)} cm each): ${n} × (π·${(20/n).toFixed(2)}/2) = 10π ≈ ${(10*Math.PI).toFixed(2)} cm</div>
        <div class="text-amber-300 font-semibold">Paradox Solved: Distributivity (π/2)(d₁ + ... + dₙ) = (π/2)D makes BOTH curves 100% EQUAL!</div>
      `;
    } else {
      const x = 60, y = 20, s = 80, r = 40;
      document.getElementById('c9c6s6Svg').innerHTML = `
        <rect x="${x}" y="${y}" width="${s}" height="${s}" fill="none" stroke="#64748b" stroke-width="1.5"/>
        <path d="M ${x} ${y} A ${r} ${r} 0 0 0 ${x+s} ${y}" fill="#a78bfa" fill-opacity="0.2" stroke="#a78bfa" stroke-width="2"/>
        <path d="M ${x} ${y+s} A ${r} ${r} 0 0 1 ${x+s} ${y+s}" fill="#a78bfa" fill-opacity="0.2" stroke="#a78bfa" stroke-width="2"/>
        <path d="M ${x} ${y} A ${r} ${r} 0 0 1 ${x} ${y+s}" fill="#a78bfa" fill-opacity="0.2" stroke="#a78bfa" stroke-width="2"/>
        <path d="M ${x+s} ${y} A ${r} ${r} 0 0 0 ${x+s} ${y+s}" fill="#a78bfa" fill-opacity="0.2" stroke="#a78bfa" stroke-width="2"/>
      `;
      document.getElementById('c9c6s6Out').innerHTML = `
        <div class="font-bold text-violet-300">4-Petal Flower Inside 14 cm × 14 cm Square</div>
        <div class="font-mono text-emerald-300">Curved Petal Border = 4 inward semicircles (D = 14 cm)</div>
        <div class="font-mono text-cyan-300 font-bold">= 2 full circles = 2 × (22/7 × 14) = 88 cm!</div>
      `;
    }
  };
  c9c6s6Draw();
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🟦</span> Unit Square Packing Grid: Area of Rectangle A = a × b
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Height Rows a: <strong id="c9c6s7AVal" class="text-cyan-300">4 units</strong></span>
      <input type="range" id="c9c6s7A" min="1" max="7" value="4" oninput="c9c6s7Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Width Columns b: <strong id="c9c6s7BVal" class="text-emerald-300">6 units</strong></span>
      <input type="range" id="c9c6s7B" min="1" max="10" value="6" oninput="c9c6s7Draw()" class="w-full accent-emerald-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c6s7Svg" viewBox="0 0 210 140" class="w-52 h-36 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c6s7Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c6s7Draw = function(){
    const a = parseInt(document.getElementById('c9c6s7A').value);
    const b = parseInt(document.getElementById('c9c6s7B').value);
    document.getElementById('c9c6s7AVal').textContent = `${a} units`;
    document.getElementById('c9c6s7BVal').textContent = `${b} units`;
    const cell = 17, ox = (210 - b*cell)/2, oy = (140 - a*cell)/2;
    let tiles = '';
    for(let r=0; r<a; r++){
      for(let c=0; c<b; c++){
        const fill = (r+c)%2===0 ? '#0ea5e9' : '#10b981';
        tiles += `<rect x="${ox+c*cell}" y="${oy+r*cell}" width="${cell-1}" height="${cell-1}" fill="${fill}" fill-opacity="0.35" stroke="#22d3ee" stroke-width="1"/>`;
      }
    }
    document.getElementById('c9c6s7Svg').innerHTML = tiles + `<rect x="${ox}" y="${oy}" width="${b*cell-1}" height="${a*cell-1}" fill="none" stroke="#fbbf24" stroke-width="2"/>`;
    document.getElementById('c9c6s7Out').innerHTML = `
      <div class="font-bold text-cyan-300">${a} rows × ${b} columns of 1×1 unit squares</div>
      <div class="font-mono text-emerald-300 font-bold text-sm">Enclosed Area A = a × b = ${a} × ${b} = ${a*b} unit²</div>
      <div class="font-mono text-amber-300">Boundary Perimeter P = 2(a + b) = 2(${a} + ${b}) = ${2*(a+b)} units</div>
      <div class="text-[11px] text-slate-400">Same perimeter does NOT lock area: e.g., 1×9 rectangle (P=20, A=9) vs 5×5 square (P=20, A=25)!</div>
    `;
  };
  c9c6s7Draw();
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>▱</span> Parallelogram Cut/Shear &amp; Extreme Oblique Altitude Explorer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Horizontal Tilt Shift (dx): <strong id="c9c6s8DxVal" class="text-amber-300">25</strong></span>
      <input type="range" id="c9c6s8Dx" min="10" max="95" value="25" oninput="c9c6s8Draw()" class="w-full accent-amber-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Slide Cut Triangle (%): <strong id="c9c6s8SlideVal" class="text-cyan-300">0%</strong></span>
      <input type="range" id="c9c6s8Slide" min="0" max="100" value="0" oninput="c9c6s8Draw()" class="w-full accent-cyan-400 mt-1">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block">
      <span class="text-slate-300 font-semibold">Height h (cm): <strong id="c9c6s8HVal" class="text-emerald-300">6 cm</strong></span>
      <input type="range" id="c9c6s8H" min="3" max="8" value="6" oninput="c9c6s8Draw()" class="w-full accent-emerald-400 mt-1">
    </label>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9c6s8Svg" viewBox="0 0 220 120" class="w-52 h-28 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9c6s8Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9c6s8Draw = function(){
    const dx = parseInt(document.getElementById('c9c6s8Dx').value);
    const slide = parseInt(document.getElementById('c9c6s8Slide').value) / 100;
    const hCm = parseInt(document.getElementById('c9c6s8H').value);
    document.getElementById('c9c6s8DxVal').textContent = dx > 70 ? `${dx} (OBLIQUE!)` : dx;
    document.getElementById('c9c6s8SlideVal').textContent = `${Math.round(slide*100)}%`;
    document.getElementById('c9c6s8HVal').textContent = `${hCm} cm`;
    const basePx = 70, yBot = 95, yTop = yBot - hCm * 9, x0 = 35;
    const shiftPx = dx > 70 ? 0 : basePx * slide;
    const slantCm = Math.hypot(dx/10, hCm).toFixed(2);
    document.getElementById('c9c6s8Svg').innerHTML = `
      <line x1="15" y1="${yBot}" x2="210" y2="${yBot}" stroke="#334155" stroke-width="1" stroke-dasharray="3 2"/>
      <polygon points="${x0+dx},${yTop} ${x0+dx+basePx},${yTop} ${x0+basePx},${yBot} ${x0},${yBot}" fill="#0ea5e9" fill-opacity="0.18" stroke="#38bdf8" stroke-width="2"/>
      <polygon points="${x0+shiftPx},${yBot} ${x0+dx+shiftPx},${yTop} ${x0+dx+shiftPx},${yBot}" fill="#f59e0b" fill-opacity="0.4" stroke="#fbbf24" stroke-width="1.5"/>
      <line x1="${x0+dx+basePx}" y1="${yTop}" x2="${x0+dx+basePx}" y2="${yBot}" stroke="#34d399" stroke-width="1.8" stroke-dasharray="3 2"/>
      <text x="${x0+dx+basePx+4}" y="${(yTop+yBot)/2}" fill="#34d399" font-size="9" font-weight="bold">h=${hCm}</text>
      <text x="${x0+basePx/2}" y="${yBot+12}" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">base b = 10 cm</text>
    `;
    document.getElementById('c9c6s8Out').innerHTML = `
      <div class="font-bold text-cyan-300">True Area = b × h = 10 × ${hCm} = ${10*hCm} cm² (Invariant!)</div>
      <div class="text-rose-300">Wrong Slant Multiplication (10 × ${slantCm}) = ${(10*parseFloat(slantCm)).toFixed(1)} cm² ❌</div>
      <div class="text-[11px] text-amber-300 font-semibold">${dx > 70 ? 'EXTREME OBLIQUE CASE: Altitude drops completely OUTSIDE base segment AB, yet shear strips STILL preserve exact Area = bh!' : 'Slide Cut Triangle to 100% to snap it into an upright b × h rectangle!'}</div>
    `;
  };
  c9c6s8Draw();
})();
</script>
"""
}
