#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 8 Maths Chapter 11: Exploring Some Geometric Themes
Part 2: Simulators 9 to 16
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
      <span>🎪</span> Cylinder, Cone & Polyhedra Nets Gallery
    </h3>
    <div class="flex flex-wrap gap-1.5 text-xs">
      <button type="button" onclick="c11s9Show('cyl')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Cylinder</button>
      <button type="button" onclick="c11s9Show('cone')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Cone</button>
      <button type="button" onclick="c11s9Show('spyr')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">Sq Pyramid</button>
      <button type="button" onclick="c11s9Show('poly')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700">Octa / Dodeca</button>
    </div>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg id="c11s9Svg" viewBox="0 0 220 150" class="w-full max-w-[230px] mx-auto bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c11s9Info" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
  </div>
</div>
<script>
(function(){
  window.c11s9Show = function(k){
    const svg = document.getElementById('c11s9Svg');
    const info = document.getElementById('c11s9Info');
    if(!svg || !info) return;
    if(k === 'cyl'){
      svg.innerHTML = `<rect x="40" y="55" width="140" height="45" fill="#0891b2" fill-opacity="0.35" stroke="#22d3ee" stroke-width="2"/><circle cx="110" cy="34" r="19" fill="#0891b2" fill-opacity="0.35" stroke="#22d3ee" stroke-width="2"/><circle cx="110" cy="121" r="19" fill="#0891b2" fill-opacity="0.35" stroke="#22d3ee" stroke-width="2"/>`;
      info.innerHTML = `<b class="text-cyan-300">Cylinder Net:</b> 1 Rectangle (width 2πr × height h) + 2 equal circular ends!`;
    } else if(k === 'cone'){
      svg.innerHTML = `<path d="M 110 20 L 45 95 A 85 85 0 0 0 175 95 Z" fill="#d97706" fill-opacity="0.35" stroke="#fbbf24" stroke-width="2"/><circle cx="110" cy="126" r="18" fill="#d97706" fill-opacity="0.35" stroke="#fbbf24" stroke-width="2"/>`;
      info.innerHTML = `<b class="text-amber-300">Cone Net:</b> 1 Circular Sector (arc = 2πr) + 1 circular base!`;
    } else if(k === 'spyr'){
      svg.innerHTML = `<rect x="85" y="52" width="50" height="50" fill="#10b981" fill-opacity="0.35" stroke="#34d399" stroke-width="2"/><polygon points="85,52 135,52 110,15" fill="#10b981" fill-opacity="0.3" stroke="#34d399" stroke-width="1.5"/><polygon points="85,102 135,102 110,140" fill="#10b981" fill-opacity="0.3" stroke="#34d399" stroke-width="1.5"/><polygon points="85,52 85,102 48,77" fill="#10b981" fill-opacity="0.3" stroke="#34d399" stroke-width="1.5"/><polygon points="135,52 135,102 172,77" fill="#10b981" fill-opacity="0.3" stroke="#34d399" stroke-width="1.5"/>`;
      info.innerHTML = `<b class="text-emerald-300">Square Pyramid Net:</b> 1 central square + 4 triangular petals meeting at apex when folded!`;
    } else {
      svg.innerHTML = `<text x="110" y="65" text-anchor="middle" fill="#34d399" font-size="14" font-weight="bold">Octahedron = 11 Nets</text><text x="110" y="95" text-anchor="middle" fill="#fb7185" font-size="14" font-weight="bold">Dodecahedron = 43,380 Nets</text>`;
      info.innerHTML = `<b class="text-rose-300">Polyhedra Combinatorics:</b> 8-face Octahedron shares 11 nets with the Cube; 12-pentagon Dodecahedron explodes to <b>43,380</b> unique nets!`;
    }
  };
  window.c11s9Show('cyl');
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🐜</span> Ant-to-Laddu Cuboid Surface Shortest Path Lab
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <label class="text-slate-300">Length L<input id="c11s10L" type="number" value="4" min="1" max="30" oninput="c11s10Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Width W<input id="c11s10W" type="number" value="3" min="1" max="30" oninput="c11s10Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
    <label class="text-slate-300">Height H<input id="c11s10H" type="number" value="2" min="1" max="30" oninput="c11s10Calc()" class="mt-1 w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white"></label>
  </div>
  <div id="c11s10Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  window.c11s10Calc = function(){
    const L = Math.max(1, parseFloat(document.getElementById('c11s10L').value) || 4);
    const W = Math.max(1, parseFloat(document.getElementById('c11s10W').value) || 3);
    const H = Math.max(1, parseFloat(document.getElementById('c11s10H').value) || 2);
    const opts = [
      { lbl: `(${L}+${W})² + ${H}²`, sq: (L+W)*(L+W) + H*H },
      { lbl: `(${L}+${H})² + ${W}²`, sq: (L+H)*(L+H) + W*W },
      { lbl: `(${W}+${H})² + ${L}²`, sq: (W+H)*(W+H) + L*L }
    ];
    const minSq = Math.min(...opts.map(o => o.sq));
    document.getElementById('c11s10Out').innerHTML = opts.map(o => `
      <div class="flex justify-between ${o.sq===minSq?'text-emerald-300 font-bold':'text-slate-400'}">
        <span>Unfolding: √(${o.lbl}) = √${o.sq}</span>
        <span>${Math.sqrt(o.sq).toFixed(2)} ${o.sq===minSq?'← SHORTEST GEODESIC!':''}</span>
      </div>`).join('');
  };
  window.c11s10Calc();
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
      <span>👁️</span> Orthographic 3-View Projector (Front, Top & Side)
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c11s11Set('lblock')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">L-Staircase</button>
      <button type="button" onclick="c11s11Set('pyr')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Sq Pyramid</button>
    </div>
  </div>
  <div id="c11s11Views" class="grid grid-cols-3 gap-2 text-center text-xs"></div>
</div>
<script>
(function(){
  window.c11s11Set = function(kind){
    const box = document.getElementById('c11s11Views');
    if(!box) return;
    if(kind === 'lblock'){
      box.innerHTML = `
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800"><div class="text-cyan-300 font-bold mb-1">Front (Vertical)</div><svg viewBox="0 0 80 80" class="w-16 h-16 mx-auto"><rect x="15" y="15" width="24" height="24" fill="#22d3ee" stroke="#0f172a"/><rect x="15" y="39" width="24" height="24" fill="#22d3ee" stroke="#0f172a"/><rect x="39" y="39" width="24" height="24" fill="#22d3ee" stroke="#0f172a"/></svg></div>
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800"><div class="text-emerald-300 font-bold mb-1">Top (Horizontal)</div><svg viewBox="0 0 80 80" class="w-16 h-16 mx-auto"><rect x="15" y="28" width="24" height="24" fill="#34d399" stroke="#0f172a"/><rect x="39" y="28" width="24" height="24" fill="#34d399" stroke="#0f172a"/></svg></div>
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800"><div class="text-amber-300 font-bold mb-1">Side Profile</div><svg viewBox="0 0 80 80" class="w-16 h-16 mx-auto"><rect x="28" y="15" width="24" height="24" fill="#fbbf24" stroke="#0f172a"/><rect x="28" y="39" width="24" height="24" fill="#fbbf24" stroke="#0f172a"/></svg></div>`;
    } else {
      box.innerHTML = `
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800"><div class="text-cyan-300 font-bold mb-1">Front (Vertical)</div><svg viewBox="0 0 80 80" class="w-16 h-16 mx-auto"><polygon points="40,14 14,66 66,66" fill="#22d3ee"/></svg></div>
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800"><div class="text-emerald-300 font-bold mb-1">Top (Horizontal)</div><svg viewBox="0 0 80 80" class="w-16 h-16 mx-auto"><rect x="16" y="16" width="48" height="48" fill="#34d399" fill-opacity="0.3" stroke="#34d399" stroke-width="2"/><line x1="16" y1="16" x2="64" y2="64" stroke="#34d399"/><line x1="64" y1="16" x2="16" y2="64" stroke="#34d399"/></svg></div>
        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800"><div class="text-amber-300 font-bold mb-1">Side Profile</div><svg viewBox="0 0 80 80" class="w-16 h-16 mx-auto"><polygon points="40,14 14,66 66,66" fill="#fbbf24"/></svg></div>`;
    }
  };
  window.c11s11Set('lblock');
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>☀️</span> Parallel Sunlight vs Close Torch Shadow & Coin Tilt
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-cyan-300">Light Ray Geometry</div>
      <div class="flex gap-1.5">
        <button type="button" onclick="c11s12Ray('sun')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Distant Sunlight (1:1)</button>
        <button type="button" onclick="c11s12Ray('torch')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700">Close Torch (Magnified)</button>
      </div>
      <div id="c11s12RayOut" class="text-slate-300"></div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
      <div class="font-bold text-emerald-300">Tilt Circular Coin (<span id="c11s12Deg">0°</span>)</div>
      <input id="c11s12Ang" type="range" min="0" max="90" value="0" oninput="c11s12Tilt()" class="w-full accent-emerald-400">
      <div id="c11s12Shadow" class="h-10 flex items-center justify-center"></div>
    </div>
  </div>
</div>
<script>
(function(){
  window.c11s12Ray = function(mode){
    document.getElementById('c11s12RayOut').innerHTML = mode === 'sun'
      ? 'Parallel rays cast a crisp <b>1:1 true orthographic shadow</b> on a perpendicular wall!'
      : 'Diverging rays balloon the shadow <b>larger than actual object size</b> and warp angles!';
  };
  window.c11s12Tilt = function(){
    const deg = parseInt(document.getElementById('c11s12Ang').value, 10) || 0;
    document.getElementById('c11s12Deg').textContent = deg + '°';
    const w = Math.max(2, Math.cos(deg * Math.PI / 180) * 34);
    const kind = deg === 0 ? 'Full Circle' : deg === 90 ? 'Thin Line Segment' : 'Narrowing Ellipse';
    document.getElementById('c11s12Shadow').innerHTML = `<div class="bg-amber-400/80 border border-amber-200 rounded-full mr-2" style="width:${w.toFixed(1)}px;height:34px"></div><span class="text-emerald-300 font-bold">${kind}</span>`;
  };
  window.c11s12Ray('sun');
  window.c11s12Tilt();
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>⬡</span> Isometric Cube: Regular Hexagon & 120° Axes
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg viewBox="0 0 200 180" class="w-full max-w-[200px] mx-auto bg-slate-950 rounded-xl border border-slate-800">
      <polygon points="100,20 161,55 100,90 39,55" fill="#22d3ee" fill-opacity="0.45" stroke="#22d3ee" stroke-width="2"/>
      <polygon points="39,55 100,90 100,160 39,125" fill="#34d399" fill-opacity="0.4" stroke="#34d399" stroke-width="2"/>
      <polygon points="100,90 161,55 161,125 100,160" fill="#fbbf24" fill-opacity="0.4" stroke="#fbbf24" stroke-width="2"/>
      <text x="108" y="110" fill="#ffffff" font-size="10">120°</text>
    </svg>
    <div class="space-y-2 text-xs text-slate-300">
      <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800"><b class="text-cyan-300">"Iso-metric" = Equal Measure:</b> Height, Width, and Depth project at identical scale along three <b>120°-spaced axes</b>.</div>
      <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800"><b class="text-amber-300">Hexagonal Silhouette:</b> Viewed straight down a corner-balanced cube diagonal, outer edges form a symmetric <b>Regular Hexagon</b> tiled by 3 congruent rhombi!</div>
    </div>
  </div>
</div>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
      <span>🧱</span> Isometric Grid Axes (|, /, \\) Block Viewer
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c11s14Draw('unit')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Unit Cube</button>
      <button type="button" onclick="c11s14Draw('lshape')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">L-Tetris (3 cubes)</button>
    </div>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg id="c11s14Svg" viewBox="0 0 220 180" class="w-full max-w-[220px] mx-auto bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5">
      <div>• <b class="text-cyan-300">Vertical ( | ):</b> Height direction</div>
      <div>• <b class="text-emerald-300">Slant Right ( / ):</b> Depth at 30°</div>
      <div>• <b class="text-amber-300">Slant Left ( \\ ):</b> Length at 30°</div>
      <div class="text-slate-400">Parallel 3D edges stay strictly parallel on isometric dot grids!</div>
    </div>
  </div>
</div>
<script>
(function(){
  function isoCube(cx, cy, s){
    const dx = s * 0.866, dy = s * 0.5;
    return `
      <polygon points="${cx},${cy} ${cx+dx},${cy-dy} ${cx},${cy-2*dy} ${cx-dx},${cy-dy}" fill="#22d3ee" fill-opacity="0.6" stroke="#0f172a" stroke-width="1.2"/>
      <polygon points="${cx-dx},${cy-dy} ${cx},${cy} ${cx},${cy+s} ${cx-dx},${cy+s-dy}" fill="#34d399" fill-opacity="0.55" stroke="#0f172a" stroke-width="1.2"/>
      <polygon points="${cx},${cy} ${cx+dx},${cy-dy} ${cx+dx},${cy+s-dy} ${cx},${cy+s}" fill="#fbbf24" fill-opacity="0.55" stroke="#0f172a" stroke-width="1.2"/>`;
  }
  window.c11s14Draw = function(mode){
    const svg = document.getElementById('c11s14Svg');
    if(!svg) return;
    if(mode === 'unit') svg.innerHTML = isoCube(110, 90, 46);
    else svg.innerHTML = isoCube(92, 115, 34) + isoCube(92, 81, 34) + isoCube(121.4, 132, 34);
  };
  window.c11s14Draw('lshape');
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-rose-300 flex items-center gap-2">
    <span>🌀</span> Impossible Object: Penrose Triangle on Isometric Grid
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg viewBox="0 0 200 180" class="w-full max-w-[200px] mx-auto bg-slate-950 rounded-xl border border-slate-800">
      <polygon points="100,20 175,148 52,148 64,126 142,126 88,36" fill="#22d3ee" fill-opacity="0.7" stroke="#0f172a" stroke-width="1.5"/>
      <polygon points="88,36 142,126 116,126 82,66 44,132 28,132" fill="#34d399" fill-opacity="0.7" stroke="#0f172a" stroke-width="1.5"/>
      <polygon points="28,132 44,132 64,126 52,148 175,148 164,162 18,162" fill="#fbbf24" fill-opacity="0.7" stroke="#0f172a" stroke-width="1.5"/>
    </svg>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2">
      <div><b class="text-cyan-300">Why Does It Trick Our Brain?</b><br>Look at any SINGLE corner: two beams meet smoothly at a crisp 90° isometric joint!</div>
      <div><b class="text-rose-300">Global Depth Contradiction:</b><br>Tracing all 3 corners closes a triangle whose beams sit at conflicting 3D depths mapped onto matching 2D grid lines!</div>
    </div>
  </div>
</div>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>📚</span> Chapter 11 Master Geometric Themes Matrix
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-cyan-300 mb-1">1. Self-Similar Fractals</div>
      <div class="text-slate-300">Sierpinski Carpet Rₙ=8ⁿ, Hₙ=(8ⁿ−1)/7; Gasket 3ⁿ triangles; Koch 1904 perimeter ×(4/3)ⁿ; Temples/Fulani/Escher.</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-emerald-300 mb-1">2. Solids, Nets & Geodesics</div>
      <div class="text-slate-300">Cube/Octahedron: 11 nets; Tetrahedron: 2; Dodecahedron: 43,380; Shortest surface path via unfolded √(a²+b²).</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-amber-300 mb-1">3. Orthographic Views & Shadows</div>
      <div class="text-slate-300">Front (Vertical), Top (Horizontal), Side views; parallel sunlight casts 1:1 orthographic shadows vs divergent torch.</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-rose-300 mb-1">4. Isometric Grids & Illusions</div>
      <div class="text-slate-300">"Equal measure" 120° axes (|, /, \\); corner-balanced cube → regular hexagon; Penrose Triangle & perpetual loops.</div>
    </div>
  </div>
</div>
"""
}
