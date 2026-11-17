#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 1: Orienting Yourself: The Use of Coordinates
Part 2: Simulators 9 to 16
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📐</span> Baudhāyana-Pythagoras Right Triangle Distance Builder
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9s9Set(1,1,4,5)" class="px-2 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold">3-4-5 Triple (1,1)→(4,5)</button>
    <button type="button" onclick="c9s9Set(-2,-1,3,11)" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">5-12-13 Triple (-2,-1)→(3,11)</button>
    <button type="button" onclick="c9s9Set(-3,4,3,-4)" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">6-8-10 Across Quadrants</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9s9Svg" viewBox="0 0 210 180" class="w-56 h-44 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9s9Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9s9Set = function(x1,y1,x2,y2){
    const sc = 8, ox = 105, oy = 110;
    const px = ox + x1*sc, py = oy - y1*sc, qx = ox + x2*sc, qy = oy - y2*sc;
    const rx = qx, ry = py;
    const dx = Math.abs(x2-x1), dy = Math.abs(y2-y1);
    const dist = Math.hypot(dx, dy);
    let s = '';
    s += `<line x1="15" y1="${oy}" x2="195" y2="${oy}" stroke="#475569" stroke-width="1.2"/>`;
    s += `<line x1="${ox}" y1="10" x2="${ox}" y2="170" stroke="#475569" stroke-width="1.2"/>`;
    s += `<polygon points="${px},${py} ${rx},${ry} ${qx},${qy}" fill="#0891b2" fill-opacity="0.2" stroke="none"/>`;
    s += `<line x1="${px}" y1="${py}" x2="${rx}" y2="${ry}" stroke="#22d3ee" stroke-width="2.2"/>`;
    s += `<line x1="${rx}" y1="${ry}" x2="${qx}" y2="${qy}" stroke="#fbbf24" stroke-width="2.2"/>`;
    s += `<line x1="${px}" y1="${py}" x2="${qx}" y2="${qy}" stroke="#34d399" stroke-width="2.6"/>`;
    s += `<circle cx="${px}" cy="${py}" r="4" fill="#fff"/><circle cx="${qx}" cy="${qy}" r="4" fill="#34d399"/><circle cx="${rx}" cy="${ry}" r="3.5" fill="#fbbf24"/>`;
    s += `<text x="${px}" y="${py+12}" fill="#e2e8f0" font-size="8" text-anchor="middle">P(${x1},${y1})</text>`;
    s += `<text x="${qx}" y="${qy-8}" fill="#34d399" font-size="8" text-anchor="middle">Q(${x2},${y2})</text>`;
    s += `<text x="${rx+6}" y="${ry+4}" fill="#fbbf24" font-size="8">R(${x2},${y1}) 90°</text>`;
    document.getElementById('c9s9Svg').innerHTML = s;
    document.getElementById('c9s9Out').innerHTML = `<div class="font-bold text-emerald-300">Right Triangle ΔPRQ Derivation</div><p>Horizontal Leg PR = |${x2} − (${x1})| = <strong>${dx}</strong></p><p>Vertical Leg RQ = |${y2} − (${y1})| = <strong>${dy}</strong></p><p class="text-cyan-300 font-semibold">PQ² = ${dx}² + ${dy}² = ${dx*dx} + ${dy*dy} = ${dx*dx+dy*dy} ⇒ PQ = <strong>${Number.isInteger(dist)?dist:dist.toFixed(2)} units</strong></p>`;
  };
  c9s9Set(1,1,4,5);
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🧮</span> Live Distance Formula &amp; Origin Radius Calculator
  </h3>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">x₁: <input type="number" id="c9s10x1" value="-2" min="-9" max="9" oninput="c9s10Calc()" class="w-14 bg-slate-900 border border-slate-700 rounded px-1.5 py-0.5 text-cyan-300 font-bold"></label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">y₁: <input type="number" id="c9s10y1" value="1" min="-9" max="9" oninput="c9s10Calc()" class="w-14 bg-slate-900 border border-slate-700 rounded px-1.5 py-0.5 text-cyan-300 font-bold"></label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">x₂: <input type="number" id="c9s10x2" value="4" min="-9" max="9" oninput="c9s10Calc()" class="w-14 bg-slate-900 border border-slate-700 rounded px-1.5 py-0.5 text-amber-300 font-bold"></label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">y₂: <input type="number" id="c9s10y2" value="9" min="-9" max="9" oninput="c9s10Calc()" class="w-14 bg-slate-900 border border-slate-700 rounded px-1.5 py-0.5 text-amber-300 font-bold"></label>
  </div>
  <div id="c9s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9s10Calc = function(){
    const x1 = parseFloat(document.getElementById('c9s10x1').value) || 0;
    const y1 = parseFloat(document.getElementById('c9s10y1').value) || 0;
    const x2 = parseFloat(document.getElementById('c9s10x2').value) || 0;
    const y2 = parseFloat(document.getElementById('c9s10y2').value) || 0;
    const dx = x2 - x1, dy = y2 - y1;
    const sq = dx*dx + dy*dy;
    const d = Math.sqrt(sq);
    const oq = Math.sqrt(x2*x2 + y2*y2);
    document.getElementById('c9s10Out').innerHTML = `
      <div class="font-bold text-cyan-300">P(${x1}, ${y1}) to Q(${x2}, ${y2})</div>
      <div>Δx = (${x2}) − (${x1}) = <strong>${dx}</strong> → (Δx)² = <strong>${dx*dx}</strong></div>
      <div>Δy = (${y2}) − (${y1}) = <strong>${dy}</strong> → (Δy)² = <strong>${dy*dy}</strong></div>
      <div class="text-emerald-300 font-bold">PQ = √(${dx*dx} + ${dy*dy}) = √${sq} ≈ ${Number.isInteger(d)?d:d.toFixed(3)} units</div>
      <div class="text-[11px] text-amber-300">Distance from Origin O(0,0) to Q(${x2}, ${y2}) = √(${x2}² + ${y2}²) = √${x2*x2+y2*y2} ≈ ${oq.toFixed(2)} units.</div>
    `;
  };
  c9s10Calc();
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-purple-300 flex items-center gap-2">
    <span>🪞</span> Axis Reflection &amp; Distance Isometry Inspector
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9s11Reflect('x')" id="c9s11bx" class="px-2.5 py-1 rounded bg-purple-500/20 text-purple-300 border border-purple-500/40 font-semibold">Across x-axis: (x, -y)</button>
    <button type="button" onclick="c9s11Reflect('y')" id="c9s11by" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Across y-axis: (-x, y)</button>
    <button type="button" onclick="c9s11Reflect('o')" id="c9s11bo" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Through Origin: (-x, -y)</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9s11Svg" viewBox="0 0 200 200" class="w-48 h-48 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9s11Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  const tri = [[1,1],[5,1],[5,4]];
  window.c9s11Reflect = function(axis){
    ['x','y','o'].forEach(a => {
      const b = document.getElementById('c9s11b'+a);
      if(b) b.className = a===axis ? 'px-2.5 py-1 rounded bg-purple-500/20 text-purple-300 border border-purple-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    const img = tri.map(([x,y]) => axis==='x'?[x,-y]:(axis==='y'?[-x,y]:[-x,-y]));
    const pts = a => a.map(([x,y])=>`${100+x*14},${100-y*14}`).join(' ');
    let s = '';
    s += `<line x1="15" y1="100" x2="185" y2="100" stroke="${axis==='x'?'#fbbf24':'#64748b'}" stroke-width="${axis==='x'?2.4:1.4}"/>`;
    s += `<line x1="100" y1="15" x2="100" y2="185" stroke="${axis==='y'?'#fbbf24':'#64748b'}" stroke-width="${axis==='y'?2.4:1.4}"/>`;
    s += `<polygon points="${pts(tri)}" fill="#0891b2" fill-opacity="0.35" stroke="#22d3ee" stroke-width="2"/>`;
    s += `<polygon points="${pts(img)}" fill="#a855f7" fill-opacity="0.35" stroke="#c084fc" stroke-width="2"/>`;
    s += `<text x="142" y="42" fill="#22d3ee" font-size="8.5" font-weight="bold">ΔABC</text>`;
    s += `<text x="58" y="160" fill="#c084fc" font-size="8.5" font-weight="bold">ΔA'B'C'</text>`;
    document.getElementById('c9s11Svg').innerHTML = s;
    const rule = axis==='x'?'(x, y) ↦ (x, -y)':(axis==='y'?'(x, y) ↦ (-x, y)':'(x, y) ↦ (-x, -y)');
    document.getElementById('c9s11Out').innerHTML = `<div class="font-bold text-purple-300">Reflection Rule: ${rule}</div><p>Pre-image ΔABC sides: AB = 4, BC = 3, AC = 5.</p><p class="text-emerald-300 font-semibold">Reflected ΔA'B'C' sides: A'B' = 4, B'C' = 3, A'C' = 5 → Exact Isometry!</p><p class="text-[11px] text-slate-400">Image vertices: (${img[0]}), (${img[1]}), (${img[2]}).</p>`;
  };
  c9s11Reflect('x');
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚖️</span> Midpoint &amp; Equidistant Axis Intercept Verifier
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9s12Show(-4,7,8,-3)" class="px-2 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold">P(-4,7) &amp; Q(8,-3)</button>
    <button type="button" onclick="c9s12Show(0,6,8,0)" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Axes Intercepts (0,6) &amp; (8,0)</button>
    <button type="button" onclick="c9s12Show(3,-5,3,7)" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Crosses x-axis at (3,0)</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9s12Svg" viewBox="0 0 210 180" class="w-56 h-44 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9s12Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9s12Show = function(x1,y1,x2,y2){
    const mx = (x1+x2)/2, my = (y1+y2)/2;
    const sc = 9, ox = 105, oy = 90;
    const px = ox + x1*sc, py = oy - y1*sc, qx = ox + x2*sc, qy = oy - y2*sc, rx = ox + mx*sc, ry = oy - my*sc;
    const pm = Math.hypot(mx-x1, my-y1).toFixed(2);
    let s = '';
    s += `<line x1="15" y1="${oy}" x2="195" y2="${oy}" stroke="#64748b" stroke-width="1.4"/>`;
    s += `<line x1="${ox}" y1="10" x2="${ox}" y2="170" stroke="#64748b" stroke-width="1.4"/>`;
    s += `<line x1="${px}" y1="${py}" x2="${qx}" y2="${qy}" stroke="#22d3ee" stroke-width="2.2"/>`;
    s += `<circle cx="${px}" cy="${py}" r="4" fill="#fff"/><circle cx="${qx}" cy="${qy}" r="4" fill="#fff"/>`;
    s += `<circle cx="${rx}" cy="${ry}" r="5" fill="#fbbf24" stroke="#fff" stroke-width="1.2"/>`;
    s += `<text x="${rx+6}" y="${ry-6}" fill="#fbbf24" font-size="8.5" font-weight="bold">M(${mx}, ${my})</text>`;
    document.getElementById('c9s12Svg').innerHTML = s;
    document.getElementById('c9s12Out').innerHTML = `<div class="font-bold text-amber-300">Midpoint M = ((${x1}+${x2})/2, (${y1}+${y2})/2) = (${mx}, ${my})</div><p>Check Equidistance via Distance Formula: PM = <strong>${pm}</strong> units and MQ = <strong>${pm}</strong> units!</p><p class="text-[11px] text-cyan-300">${y1*y2<=0?'Notice y changes sign or hits 0, so the segment crosses the x-axis (y=0)!':'Notice midpoint averages both endpoints linearly.'}</p>`;
  };
  c9s12Show(-4,7,8,-3);
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>⭕</span> Collinearity (AB + BC = AC) &amp; Origin Circle Boundary Tester
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9s13Mode('col1')" class="px-2 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">Collinear: (0,1),(3,5),(6,9)</button>
    <button type="button" onclick="c9s13Mode('col2')" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Non-Collinear Triangle</button>
    <button type="button" onclick="c9s13Mode('cirIn')" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Circle r=5: Inside (2,3)</button>
    <button type="button" onclick="c9s13Mode('cirOn')" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Circle r=5: On (-3,4)</button>
    <button type="button" onclick="c9s13Mode('cirOut')" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Circle r=5: Outside (4,4)</button>
  </div>
  <div id="c9s13Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  const cases = {
    col1: ['Collinear Test: A(0,1), B(3,5), C(6,9)', 'AB = √(3²+4²) = 5, BC = √(3²+4²) = 5, AC = √(6²+8²) = 10.', 'Exact equality AB + BC = 5 + 5 = 10 = AC proves A, B, C are COLLINEAR!'],
    col2: ['Non-Collinear Test: A(0,0), B(3,4), C(6,2)', 'AB = 5, BC = √(3²+(-2)²) ≈ 3.61, AC = √(6²+2²) ≈ 6.32.', 'AB + BC ≈ 8.61 > 6.32 = AC → Strict Triangle Inequality, NOT collinear!'],
    cirIn: ['Origin Circle r = 5: Test Point P(2, 3)', 'OP = √(2² + 3²) = √13 ≈ 3.61 units.', 'Since OP ≈ 3.61 < 5 (13 < 25), point P lies strictly INSIDE the circle!'],
    cirOn: ['Origin Circle r = 5: Test Point P(-3, 4)', 'OP = √((-3)² + 4²) = √25 = 5 units.', 'Since OP = 5 = r exactly, point P sits ON the circle boundary!'],
    cirOut: ['Origin Circle r = 5: Test Point P(4, 4)', 'OP = √(4² + 4²) = √32 ≈ 5.66 units.', 'Since OP ≈ 5.66 > 5 (32 > 25), point P lies strictly OUTSIDE the circle!']
  };
  window.c9s13Mode = function(k){
    const c = cases[k];
    document.getElementById('c9s13Out').innerHTML = `<div class="font-bold text-emerald-300">${c[0]}</div><p>${c[1]}</p><p class="text-cyan-300 font-semibold">${c[2]}</p>`;
  };
  c9s13Mode('col1');
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🖥️</span> Dual Coordinate Models: City Street Grid vs Screen Pixel (0, 0)
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9s14View('city')" id="c9s14bcity" class="px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold">City Grid Streets (2,1)→(6,4)</button>
    <button type="button" onclick="c9s14View('pixel')" id="c9s14bpixel" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Computer Screen Pixels (Top-Left 0,0)</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9s14Svg" viewBox="0 0 210 155" class="w-56 h-40 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9s14Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9s14View = function(v){
    ['city','pixel'].forEach(k => {
      const b = document.getElementById('c9s14b'+k);
      if(b) b.className = k===v ? 'px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    let s = '';
    if(v==='city'){
      for(let x=25;x<=185;x+=26){ s += `<line x1="${x}" y1="15" x2="${x}" y2="140" stroke="#1e293b" stroke-width="2"/>`; }
      for(let y=15;y<=140;y+=25){ s += `<line x1="25" y1="${y}" x2="185" y2="${y}" stroke="#1e293b" stroke-width="2"/>`; }
      s += `<polyline points="51,115 155,115 155,40" fill="none" stroke="#fbbf24" stroke-width="2.6"/>`;
      s += `<line x1="51" y1="115" x2="155" y2="40" stroke="#22d3ee" stroke-width="2.2" stroke-dasharray="4 2"/>`;
      s += `<circle cx="51" cy="115" r="4.5" fill="#fff"/><circle cx="155" cy="40" r="4.5" fill="#34d399"/>`;
      s += `<text x="55" y="128" fill="#cbd5e1" font-size="8">(2,1)</text><text x="158" y="36" fill="#34d399" font-size="8">(6,4)</text>`;
      document.getElementById('c9s14Out').innerHTML = `<div class="font-bold text-cyan-300">City Street Grid: (2, 1) to (6, 4)</div><p class="text-amber-300">Street Walk Path (yellow): |6−2| + |4−1| = 4 + 3 = <strong>7 blocks</strong>.</p><p class="text-cyan-300">Aerial Distance Formula (cyan): √(4² + 3²) = <strong>5 blocks</strong>.</p>`;
    } else {
      s += `<rect x="20" y="18" width="170" height="118" rx="6" fill="#0f172a" stroke="#475569" stroke-width="2"/>`;
      s += `<circle cx="20" cy="18" r="5" fill="#fbbf24"/><text x="27" y="30" fill="#fbbf24" font-size="8.5" font-weight="bold">Origin (0, 0) Top-Left</text>`;
      s += `<line x1="20" y1="18" x2="160" y2="18" stroke="#22d3ee" stroke-width="2"/><text x="163" y="21" fill="#22d3ee" font-size="8">+x</text>`;
      s += `<line x1="20" y1="18" x2="20" y2="128" stroke="#34d399" stroke-width="2"/><text x="24" y="128" fill="#34d399" font-size="8">+y Down</text>`;
      s += `<rect x="85" y="55" width="70" height="45" fill="#0891b2" fill-opacity="0.3" stroke="#38bdf8"/>`;
      s += `<text x="120" y="80" fill="#fff" font-size="8" text-anchor="middle">Box (100,80)</text>`;
      document.getElementById('c9s14Out').innerHTML = `<div class="font-bold text-emerald-300">Computer Screen Pixel Coordinates</div><p>Origin <strong>(0, 0)</strong> sits at the <strong>TOP-LEFT</strong> pixel!</p><p>Moving right increases <strong>+x</strong>; moving <strong>DOWNWARD</strong> increases <strong>+y</strong> (inverted compared to upward Cartesian y-axis).</p>`;
    }
    document.getElementById('c9s14Svg').innerHTML = s;
  };
  c9s14View('city');
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>📐</span> Coordinate Polygon &amp; Triangle Area Calculator
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9s15Shape('rect')" id="c9s15brect" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Rectangle PQRS</button>
    <button type="button" onclick="c9s15Shape('tri')" id="c9s15btri" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Axis Triangle ΔOAB</button>
    <button type="button" onclick="c9s15Shape('right')" id="c9s15bright" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Right Triangle ΔPQR</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c9s15Svg" viewBox="0 0 200 175" class="w-52 h-44 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c9s15Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5 w-full"></div>
  </div>
</div>
<script>
(function(){
  window.c9s15Shape = function(sh){
    ['rect','tri','right'].forEach(k => {
      const b = document.getElementById('c9s15b'+k);
      if(b) b.className = k===sh ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    let s = `<line x1="15" y1="120" x2="185" y2="120" stroke="#64748b" stroke-width="1.3"/><line x1="65" y1="15" x2="65" y2="160" stroke="#64748b" stroke-width="1.3"/>`;
    if(sh==='rect'){
      s += `<rect x="41" y="60" width="96" height="72" fill="#d97706" fill-opacity="0.28" stroke="#fbbf24" stroke-width="2"/>`;
      s += `<text x="89" y="100" fill="#fbbf24" font-size="9" text-anchor="middle" font-weight="bold">7 × 5 = 35 sq u</text>`;
      document.getElementById('c9s15Out').innerHTML = `<div class="font-bold text-amber-300">Rectangle P(-2,-1), Q(5,-1), R(5,4), S(-2,4)</div><p>Width = |5 − (−2)| = <strong>7 units</strong>; Height = |4 − (−1)| = <strong>5 units</strong>.</p><p class="text-emerald-300 font-bold">Area = 7 × 5 = 35 square units.</p>`;
    } else if(sh==='tri'){
      s += `<polygon points="65,120 161,120 101,48" fill="#0891b2" fill-opacity="0.3" stroke="#22d3ee" stroke-width="2"/>`;
      s += `<line x1="101" y1="48" x2="101" y2="120" stroke="#fbbf24" stroke-width="1.6" stroke-dasharray="3 2"/>`;
      s += `<text x="113" y="96" fill="#22d3ee" font-size="9" font-weight="bold">Area = 20</text>`;
      document.getElementById('c9s15Out').innerHTML = `<div class="font-bold text-cyan-300">Triangle O(0,0), A(8,0), B(3,5)</div><p>Base along x-axis OA = <strong>8 units</strong>; Altitude to x-axis = |y_B| = <strong>5 units</strong>.</p><p class="text-emerald-300 font-bold">Area = ½ × 8 × 5 = 20 square units.</p>`;
    } else {
      s += `<polygon points="65,120 113,120 65,56" fill="#059669" fill-opacity="0.3" stroke="#34d399" stroke-width="2"/>`;
      s += `<text x="83" y="106" fill="#34d399" font-size="8.5" font-weight="bold">Area = 6</text>`;
      document.getElementById('c9s15Out').innerHTML = `<div class="font-bold text-emerald-300">Right Triangle P(0,0), Q(3,0), R(0,4)</div><p>Legs along axes: PQ = 3, PR = 4, Hypotenuse QR = √(3²+4²) = 5.</p><p class="text-amber-300 font-bold">Area = ½ × 3 × 4 = 6 square units.</p>`;
    }
    document.getElementById('c9s15Svg').innerHTML = s;
  };
  c9s15Shape('rect');
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🗂️</span> Chapter 1 Complete Formula &amp; Concept Synthesis Matrix
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c9s16Tab(0)" id="c9s16t0" class="px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold">1. History &amp; Tactile</button>
    <button type="button" onclick="c9s16Tab(1)" id="c9s16t1" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">2. Axes &amp; Quadrants</button>
    <button type="button" onclick="c9s16Tab(2)" id="c9s16t2" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">3. Distance &amp; Reflections</button>
    <button type="button" onclick="c9s16Tab(3)" id="c9s16t3" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">4. Exercises Toolkit</button>
  </div>
  <div id="c9s16Body" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  const tabs = [
    ['Historical & Practical Origins', [
      '• Sindhu-Sarasvatī ~10 m perpendicular street grids & Baudhāyana orthogonal cords',
      '• Ujjayinī central zero-longitude prime meridian in Indian astronomy',
      '• Hipparchus, Ptolemy, Āryabhaṭa, Al-Bīrūnī, Omar Khayyām → Brahmagupta (0 & negatives) → Fermat & René Descartes (2D Cartesian axes)',
      '• Tactile pin-and-thread floor maps (scale 1 cm : 1 foot) for spatial accessibility'
    ]],
    ['2D Cartesian Plane & Rules', [
      '• Perpendicular x-axis & y-axis intersect at Origin O(0, 0)',
      '• Counter-clockwise Quadrants: QI (+,+), QII (-,+), QIII (-,-), QIV (+,-)',
      '• Axis Points: (x, 0) on x-axis; (0, y) on y-axis (not in any quadrant)',
      '• Distance to y-axis = |x|; Distance to x-axis = |y|; (x, y) = (y, x) ⇔ x = y'
    ]],
    ['Distance Formula & Isometries', [
      '• Right-triangle legs |x₂ − x₁| and |y₂ − y₁| via Baudhāyana-Pythagoras',
      '• Distance Formula: d = √((x₂ − x₁)² + (y₂ − y₁)²) = √((x₁ − x₂)² + (y₁ − y₂)²)',
      '• Origin Distance: OP = √(x² + y²)',
      '• Reflections across x-axis (x, -y), y-axis (-x, y), Origin (-x, -y) preserve all lengths'
    ]],
    ['Applications & Exercise Checks', [
      '• Midpoint M = ((x₁ + x₂)/2, (y₁ + y₂)/2); Equidistance solved via PA² = PB²',
      '• Collinearity: sum of two smaller distances equals largest (AB + BC = AC)',
      '• Origin Circle radius r: d < r (inside), d = r (on circle), d > r (outside)',
      '• City grids (|Δx|+|Δy| vs √(Δx²+Δy²)), Screen pixels top-left (0,0), Polygon areas'
    ]]
  ];
  window.c9s16Tab = function(idx){
    [0,1,2,3].forEach(i => {
      const b = document.getElementById('c9s16t'+i);
      if(b) b.className = i===idx ? 'px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    const [head, lines] = tabs[idx];
    document.getElementById('c9s16Body').innerHTML = `<div class="font-bold text-cyan-300 text-sm">${head}</div>` + lines.map(l => `<div>${l}</div>`).join('');
  };
  c9s16Tab(0);
})();
</script>
"""
}
