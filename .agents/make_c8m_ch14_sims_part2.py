#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 8 Maths Chapter 14: Area
Part 2: Simulators 9 to 16
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔷</span> Polygon Triangulation Explorer ((n − 2) Triangles)
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c14s9Set(4)" id="c14s9b4" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">4-gon (2 Δ)</button>
    <button type="button" onclick="c14s9Set(5)" id="c14s9b5" class="px-2 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold">5-gon Pentagon (3 Δ)</button>
    <button type="button" onclick="c14s9Set(6)" id="c14s9b6" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">6-gon Hexagon (4 Δ)</button>
    <button type="button" onclick="c14s9Set(7)" id="c14s9b7" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">7-gon Heptagon (5 Δ)</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c14s9Svg" viewBox="0 0 180 145" class="w-44 h-36 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c14s9Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
  </div>
</div>
<script>
(function(){
  const cols = ['#0891b2','#d97706','#059669','#e11d48','#7c3aed'];
  window.c14s9Set = function(n){
    [4,5,6,7].forEach(k => {
      const b = document.getElementById('c14s9b'+k);
      if(b) b.className = k===n ? 'px-2 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-semibold' : 'px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    const pts = [];
    for(let i=0;i<n;i++){
      const ang = -Math.PI/2 + (2*Math.PI*i)/n;
      pts.push([90 + 54*Math.cos(ang), 74 + 54*Math.sin(ang)]);
    }
    let tris = '';
    for(let i=1;i<n-1;i++){
      tris += `<polygon points="${pts[0][0].toFixed(1)},${pts[0][1].toFixed(1)} ${pts[i][0].toFixed(1)},${pts[i][1].toFixed(1)} ${pts[i+1][0].toFixed(1)},${pts[i+1][1].toFixed(1)}" fill="${cols[i-1]}" fill-opacity="0.32" stroke="#e2e8f0" stroke-width="1.4"/>`;
    }
    const svg = document.getElementById('c14s9Svg');
    if(svg) svg.innerHTML = tris + `<circle cx="${pts[0][0].toFixed(1)}" cy="${pts[0][1].toFixed(1)}" r="4" fill="#fbbf24"/>`;
    document.getElementById('c14s9Out').innerHTML = `
      <div>Sides <b class="text-cyan-300">n = ${n}</b> → Diagonals from Vertex A: <b>${n-3}</b> → Component Triangles: <b class="text-emerald-300">${n-2}</b>!</div>
      <div>Quadrilateral Shortcut: Diagonal d with offsets h₁, h₂ yields <b>Area = 1/2 × d × (h₁ + h₂)</b>.</div>`;
  };
  window.c14s9Set(5);
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>✂️</span> Parallelogram-to-Rectangle RHS Shift Animator
  </h3>
  <div class="space-y-2 text-xs">
    <div class="flex justify-between text-slate-300"><span>Slide Left Triangle ΔAED Rightward to Edge BC:</span><b id="c14s10Pct" class="text-emerald-300">0%</b></div>
    <input id="c14s10Sl" type="range" min="0" max="100" value="0" oninput="c14s10Draw()" class="w-full accent-amber-400">
    <svg id="c14s10Svg" viewBox="0 0 330 115" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c14s10Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-300"></div>
  </div>
</div>
<script>
(function(){
  window.c14s10Draw = function(){
    const p = parseInt(document.getElementById('c14s10Sl').value,10)||0;
    document.getElementById('c14s10Pct').textContent = `${p}% shifted`;
    const shift = (p / 100) * 160;
    const svg = document.getElementById('c14s10Svg');
    if(svg) svg.innerHTML = `
      <polygon points="95,92 215,92 255,22 95,22" fill="#0891b2" fill-opacity="0.32" stroke="#22d3ee" stroke-width="1.8"/>
      <polygon points="${55+shift},92 ${95+shift},92 ${95+shift},22" fill="#f59e0b" fill-opacity="0.45" stroke="#fbbf24" stroke-width="1.8"/>
      <line x1="95" y1="22" x2="95" y2="92" stroke="#94a3b8" stroke-dasharray="3 3"/>
      <text x="160" y="108" text-anchor="middle" fill="#cbd5e1" font-size="10">Base b = 10, Perpendicular Height h = 6</text>`;
    document.getElementById('c14s10Out').innerHTML = p === 100
      ? '<b class="text-emerald-300">PERFECT RECTANGLE EFCD!</b> ΔAED ≅ ΔBFC by RHS (90°, AD = BC, DE = CF = h) → Area = b × h!'
      : 'Slide to <b>100%</b> to watch ΔAED snap cleanly onto ΔBFC by RHS congruence!';
  };
  window.c14s10Draw();
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📏</span> Dual Height & Shear Explorer (Area = Base × Height)
  </h3>
  <div class="space-y-2 text-xs">
    <div class="text-slate-300">Fixed Parallelogram Area = <b>120 cm²</b> (Base₁ = 15 cm, Height₁ = 8 cm)</div>
    <div class="flex justify-between text-slate-300"><span>Adjust Adjacent Side Length (Base₂):</span><b id="c14s11Val" class="text-amber-300">10 cm</b></div>
    <input id="c14s11Sl" type="range" min="8" max="20" value="10" oninput="c14s11Draw()" class="w-full accent-cyan-400">
    <div id="c14s11Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-1"></div>
  </div>
</div>
<script>
(function(){
  window.c14s11Draw = function(){
    const b2 = parseInt(document.getElementById('c14s11Sl').value,10)||10;
    document.getElementById('c14s11Val').textContent = `${b2} cm`;
    const h2 = 120 / b2;
    document.getElementById('c14s11Out').innerHTML = `
      <div>Equate areas: 15 × 8 = ${b2} × h₂ → <b>120 = ${b2} × h₂</b></div>
      <div class="text-emerald-300 font-bold text-sm">Corresponding Height onto Base₂ = ${h2.toFixed(2).replace(/\\.00$/,'')} cm</div>
      <div class="text-rose-300">Remember: Area uses PERPENDICULAR height, NEVER slant side length (${b2} × 15 ≠ 120)!</div>`;
  };
  window.c14s11Draw();
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>💠</span> Rhombus Diagonal Box & Side Theorem (½ d₁ d₂)
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <div><span class="text-slate-400">Diagonal d₁: <b id="c14s12d1v" class="text-cyan-300">24</b> cm</span><input id="c14s12d1" type="range" min="6" max="26" step="2" value="24" oninput="c14s12Draw()" class="w-full accent-cyan-400"></div>
    <div><span class="text-slate-400">Diagonal d₂: <b id="c14s12d2v" class="text-amber-300">10</b> cm</span><input id="c14s12d2" type="range" min="6" max="22" step="2" value="10" oninput="c14s12Draw()" class="w-full accent-amber-400"></div>
  </div>
  <svg id="c14s12Svg" viewBox="0 0 300 120" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c14s12Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c14s12Draw = function(){
    const d1 = parseInt(document.getElementById('c14s12d1').value,10)||24;
    const d2 = parseInt(document.getElementById('c14s12d2').value,10)||10;
    document.getElementById('c14s12d1v').textContent = d1;
    document.getElementById('c14s12d2v').textContent = d2;
    const w = d1*8, h = d2*3.8;
    const cx = 150, cy = 60;
    const svg = document.getElementById('c14s12Svg');
    if(svg) svg.innerHTML = `
      <rect x="${cx-w/2}" y="${cy-h/2}" width="${w}" height="${h}" fill="none" stroke="#475569" stroke-dasharray="4 3"/>
      <polygon points="${cx},${cy-h/2} ${cx+w/2},${cy} ${cx},${cy+h/2} ${cx-w/2},${cy}" fill="#10b981" fill-opacity="0.32" stroke="#34d399" stroke-width="2"/>
      <line x1="${cx-w/2}" y1="${cy}" x2="${cx+w/2}" y2="${cy}" stroke="#22d3ee" stroke-dasharray="3 2"/>
      <line x1="${cx}" y1="${cy-h/2}" x2="${cx}" y2="${cy+h/2}" stroke="#fbbf24" stroke-dasharray="3 2"/>`;
    const area = 0.5*d1*d2;
    const side = Math.hypot(d1/2, d2/2);
    document.getElementById('c14s12Out').innerHTML = `Bounding Box = ${d1}×${d2} = <b>${d1*d2} cm²</b> → Rhombus Area = ½ × ${d1} × ${d2} = <b class="text-emerald-300">${area} cm²</b> &nbsp;|&nbsp; Side = <b class="text-amber-300">${side.toFixed(2).replace(/\\.00$/,'')} cm</b>`;
  };
  window.c14s12Draw();
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>🧩</span> Trapezium Splitting Lab (a = 12, b = 20, h = 7)
    </h3>
    <button type="button" onclick="c14s13Tog()" id="c14s13Btn" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 text-xs border border-slate-700">Switch to Diagonal Split</button>
  </div>
  <svg id="c14s13Svg" viewBox="0 0 320 120" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c14s13Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  let diag = false;
  window.c14s13Tog = function(){ diag = !diag; window.c14s13Draw(); };
  window.c14s13Draw = function(){
    document.getElementById('c14s13Btn').textContent = diag ? 'Switch to Vertical Wings Split' : 'Switch to Diagonal Split';
    const svg = document.getElementById('c14s13Svg');
    if(!diag){
      if(svg) svg.innerHTML = `
        <polygon points="50,98 100,98 100,24" fill="#f59e0b" fill-opacity="0.35" stroke="#fbbf24"/>
        <rect x="100" y="24" width="120" height="74" fill="#0891b2" fill-opacity="0.32" stroke="#22d3ee"/>
        <polygon points="220,98 270,98 220,24" fill="#10b981" fill-opacity="0.35" stroke="#34d399"/>
        <text x="160" y="16" text-anchor="middle" fill="#e2e8f0" font-size="10">Top a = 12</text>
        <text x="160" y="113" text-anchor="middle" fill="#cbd5e1" font-size="10">Bottom b = 20 (Wings total x + y = 8)</text>`;
      document.getElementById('c14s13Out').innerHTML = `Central Rectangle (12×7 = <b class="text-cyan-300">84</b>) + Flanking Wings (½×8×7 = <b class="text-emerald-300">28</b>) = <b class="text-amber-300">112 cm²</b>!`;
    } else {
      if(svg) svg.innerHTML = `
        <polygon points="50,98 270,98 220,24" fill="#0891b2" fill-opacity="0.32" stroke="#22d3ee"/>
        <polygon points="50,98 100,24 220,24" fill="#10b981" fill-opacity="0.32" stroke="#34d399"/>
        <line x1="50" y1="98" x2="220" y2="24" stroke="#fbbf24" stroke-width="2.2"/>`;
      document.getElementById('c14s13Out').innerHTML = `Bottom Triangle (½×20×7 = <b class="text-cyan-300">70</b>) + Inverted Top Triangle (½×12×7 = <b class="text-emerald-300">42</b>) = <b class="text-amber-300">112 cm²</b>!`;
    }
  };
  window.c14s13Draw();
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔄</span> Congruent Two-Copy Trapezium Proof (½ h (a + b))
  </h3>
  <div class="space-y-2 text-xs">
    <div class="flex justify-between text-slate-300"><span>Rotate Twin Copy 180° & Snap Against Slanted Edge:</span><b id="c14s14Ang" class="text-amber-300">0°</b></div>
    <input id="c14s14Sl" type="range" min="0" max="180" step="15" value="180" oninput="c14s14Draw()" class="w-full accent-cyan-400">
    <svg id="c14s14Svg" viewBox="0 0 320 115" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c14s14Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-300"></div>
  </div>
</div>
<script>
(function(){
  window.c14s14Draw = function(){
    const deg = parseInt(document.getElementById('c14s14Sl').value,10)||0;
    document.getElementById('c14s14Ang').textContent = `${deg}° rotated`;
    const svg = document.getElementById('c14s14Svg');
    if(svg) svg.innerHTML = `
      <polygon points="40,92 160,92 135,24 65,24" fill="#0891b2" fill-opacity="0.38" stroke="#22d3ee" stroke-width="2"/>
      <g transform="rotate(${deg}, 147.5, 58)">
        <polygon points="135,24 160,92 260,92 235,24" fill="none" stroke="none"/>
        <polygon points="135,92 255,92 230,24 160,24" fill="#f59e0b" fill-opacity="0.32" stroke="#fbbf24" stroke-width="2" transform="translate(-95,0)"/>
      </g>
      <text x="160" y="109" text-anchor="middle" fill="#cbd5e1" font-size="10">Giant Parallelogram Base = (a + b), Height = h</text>`;
    document.getElementById('c14s14Out').innerHTML = deg === 180
      ? `Two Congruent Trapeziums = Giant Parallelogram of Area <b class="text-amber-300">(a + b) × h</b> → Single Trapezium = <b class="text-emerald-300">½ × h × (a + b)</b>!`
      : `Rotate slider to <b>180°</b> to fuse both trapeziums into a single parallelogram!`;
  };
  window.c14s14Draw();
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🗺️</span> Real-Life Metric, Imperial & Indian Land Units
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <div><span class="text-slate-400">Enter Square Meters (m²):</span><input id="c14s15M" type="number" min="1" max="100000" value="100" oninput="c14s15Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2.5 py-1.5 text-cyan-300 font-bold"></div>
    <div class="p-2 rounded bg-slate-950 border border-slate-800 text-[11px] text-slate-300">Exact Link: <b>1 in = 2.54 cm</b><br>1 ft² = 144 in² ≈ <b>929 cm²</b></div>
  </div>
  <div id="c14s15Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1 text-slate-300"></div>
</div>
<script>
(function(){
  window.c14s15Draw = function(){
    const m2 = Math.max(0.1, parseFloat(document.getElementById('c14s15M').value)||100);
    const cm2 = m2 * 10000;
    const sqft = m2 / 0.09290304;
    const gaj = m2 / 0.836127;
    const cents = m2 / 40.4686;
    document.getElementById('c14s15Out').innerHTML = `
      <div>• <b class="text-cyan-300">Metric:</b> ${m2.toLocaleString()} m² = <b>${cm2.toLocaleString()} cm²</b> = ${(m2/10000).toFixed(4)} hectares</div>
      <div>• <b class="text-amber-300">Imperial:</b> ≈ <b>${sqft.toFixed(1)} ft²</b> (and 1 in² = (2.54)² = <b>6.4516 cm²</b>)</div>
      <div>• <b class="text-emerald-300">Indian Local Units:</b> ≈ <b>${gaj.toFixed(1)} gaj</b> (sq yd) ≈ <b>${cents.toFixed(2)} cents</b> (also <b>bigha, katha, dhur, ankanam</b> across states!)</div>`;
  };
  window.c14s15Draw();
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🎓</span> Chapter 14 Complete Area Formula Synthesis
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c14s16Tab(0)" id="c14s16t0" class="px-2 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">Rectangles & Triangles</button>
    <button type="button" onclick="c14s16Tab(1)" id="c14s16t1" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Medians & Parallels</button>
    <button type="button" onclick="c14s16Tab(2)" id="c14s16t2" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Quads & Polygons</button>
    <button type="button" onclick="c14s16Tab(3)" id="c14s16t3" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Real-Life Units</button>
  </div>
  <div id="c14s16Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5 text-slate-300"></div>
</div>
<script>
(function(){
  const tabs = [
    `<div class="text-cyan-300 font-bold">7.1 Rectangles, Squares & General Triangles</div><div>• Rectangle = <b>l × w</b> &nbsp;|&nbsp; Square = <b>s²</b> &nbsp;|&nbsp; Equal Perimeter does NOT determine Area!</div><div>• Diagonal cuts rectangle into 2 congruent triangles (SSS, half area each).</div><div>• Acute/Right/Obtuse Triangle = <b>1/2 × base × height</b>.</div>`,
    `<div class="text-emerald-300 font-bold">Altitudes, Medians & Parallel Lines</div><div>• Dual Heights: <b>b₁ × h₁ = b₂ × h₂</b>.</div><div>• Any Median splits a triangle into <b>two equal-area halves</b>.</div><div>• Common base between parallel tracks: <b>constant area</b>; min perimeter via reflection <b>AB′</b> (isosceles peak).</div>`,
    `<div class="text-amber-300 font-bold">Polygons, Parallelograms, Rhombuses & Trapeziums</div><div>• n-gon Triangulation: <b>(n − 2) triangles</b> (Quad diagonal: <b>½ d(h₁+h₂)</b>).</div><div>• Parallelogram = <b>base × height</b> (RHS wedge shift).</div><div>• Rhombus = <b>½ × d₁ × d₂</b> &nbsp;|&nbsp; Trapezium = <b>½ × h × (a + b)</b>.</div>`,
    `<div class="text-rose-300 font-bold">Real-Life Conversions & Local Land Units</div><div>• Standard: <b>1 m² = 10,000 cm²</b>, <b>1 km² = 10⁶ m² = 100 ha</b>, <b>1 in = 2.54 cm</b>.</div><div>• Indian Traditional Units: <b>bigha, gaj, katha, dhur, cent, ankanam</b>.</div>`
  ];
  window.c14s16Tab = function(i){
    [0,1,2,3].forEach(k => {
      const b = document.getElementById('c14s16t'+k);
      if(b) b.className = k===i ? 'px-2 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    document.getElementById('c14s16Out').innerHTML = tabs[i];
  };
  window.c14s16Tab(0);
})();
</script>
"""
}
