#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 8 Maths Chapter 11: Exploring Some Geometric Themes
Part 1: Simulators 1 to 8
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🌿</span> Natural Self-Similar Fractal Tree Generator
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg id="c11s1Svg" viewBox="0 0 220 180" class="w-full max-w-[230px] mx-auto bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div class="space-y-3 text-xs">
      <label class="block text-slate-300">Branching Depth Level: <span id="c11s1Lvl" class="font-bold text-emerald-300">5</span>
        <input id="c11s1D" type="range" min="1" max="7" value="5" oninput="c11s1Draw()" class="mt-2 w-full accent-emerald-400">
      </label>
      <div id="c11s1Info" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-slate-300"></div>
    </div>
  </div>
</div>
<script>
(function(){
  function branch(x1, y1, len, ang, depth, paths){
    if(depth === 0) return;
    const x2 = x1 + len * Math.cos(ang);
    const y2 = y1 - len * Math.sin(ang);
    const stroke = depth <= 2 ? '#34d399' : '#22d3ee';
    paths.push(`<line x1="${x1.toFixed(1)}" y1="${y1.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}" stroke="${stroke}" stroke-width="${Math.max(1, depth*0.7)}" stroke-linecap="round"/>`);
    branch(x2, y2, len * 0.72, ang + 0.45, depth - 1, paths);
    branch(x2, y2, len * 0.72, ang - 0.45, depth - 1, paths);
  }
  window.c11s1Draw = function(){
    const d = parseInt(document.getElementById('c11s1D').value, 10) || 5;
    document.getElementById('c11s1Lvl').textContent = d;
    const paths = [];
    branch(110, 170, 42, Math.PI / 2, d, paths);
    const svg = document.getElementById('c11s1Svg');
    if(svg) svg.innerHTML = paths.join('');
    const segs = Math.pow(2, d) - 1;
    document.getElementById('c11s1Info').innerHTML = `Every forked twig echoes the whole tree silhouette (self-similarity!). Total segments at depth ${d}: <b class="text-amber-300">${segs}</b>.`;
  };
  window.c11s1Draw();
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
      <span>🔲</span> Sierpinski Carpet Explorer (Rₙ = 8ⁿ)
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c11s2Step(0)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">Step 0</button>
      <button type="button" onclick="c11s2Step(1)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Step 1</button>
      <button type="button" onclick="c11s2Step(2)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">Step 2</button>
      <button type="button" onclick="c11s2Step(3)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Step 3</button>
    </div>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg id="c11s2Svg" viewBox="0 0 180 180" class="w-full max-w-[200px] mx-auto bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c11s2Stats" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
  </div>
</div>
<script>
(function(){
  function drawCarpet(x, y, s, depth, rects){
    if(depth === 0){
      rects.push(`<rect x="${x.toFixed(1)}" y="${y.toFixed(1)}" width="${s.toFixed(1)}" height="${s.toFixed(1)}" fill="#22d3ee"/>`);
      return;
    }
    const ns = s / 3;
    for(let r = 0; r < 3; r++){
      for(let c = 0; c < 3; c++){
        if(r === 1 && c === 1) continue;
        drawCarpet(x + c*ns, y + r*ns, ns, depth - 1, rects);
      }
    }
  }
  window.c11s2Step = function(n){
    const rects = [];
    drawCarpet(10, 10, 160, n, rects);
    const svg = document.getElementById('c11s2Svg');
    if(svg) svg.innerHTML = rects.join('');
    const rem = Math.pow(8, n);
    const holes = (rem - 1) / 7;
    document.getElementById('c11s2Stats').innerHTML = `
      <div>Step <b>n = ${n}</b></div>
      <div>Remaining Solid Squares (Rₙ = 8ⁿ): <b class="text-cyan-300">${rem}</b></div>
      <div>Cumulative Holes Punched (Hₙ): <b class="text-amber-300">${holes}</b></div>
      <div>Remaining Area Fraction: <b class="text-emerald-300">(8/9)^${n} = ${(Math.pow(8/9, n)*100).toFixed(1)}%</b></div>`;
  };
  window.c11s2Step(2);
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>🔺</span> Sierpinski Gasket Builder (3ⁿ Triangles)
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c11s3Step(0)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">Step 0</button>
      <button type="button" onclick="c11s3Step(1)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Step 1</button>
      <button type="button" onclick="c11s3Step(2)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">Step 2</button>
      <button type="button" onclick="c11s3Step(3)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Step 3</button>
    </div>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg id="c11s3Svg" viewBox="0 0 200 180" class="w-full max-w-[220px] mx-auto bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c11s3Stats" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
  </div>
</div>
<script>
(function(){
  function gasket(ax, ay, bx, by, cx, cy, depth, polys){
    if(depth === 0){
      polys.push(`<polygon points="${ax.toFixed(1)},${ay.toFixed(1)} ${bx.toFixed(1)},${by.toFixed(1)} ${cx.toFixed(1)},${cy.toFixed(1)}" fill="#fbbf24"/>`);
      return;
    }
    const abx = (ax+bx)/2, aby = (ay+by)/2;
    const bcx = (bx+cx)/2, bcy = (by+cy)/2;
    const cax = (cx+ax)/2, cay = (cy+ay)/2;
    gasket(ax, ay, abx, aby, cax, cay, depth - 1, polys);
    gasket(abx, aby, bx, by, bcx, bcy, depth - 1, polys);
    gasket(cax, cay, bcx, bcy, cx, cy, depth - 1, polys);
  }
  window.c11s3Step = function(n){
    const polys = [];
    gasket(100, 15, 20, 160, 180, 160, n, polys);
    const svg = document.getElementById('c11s3Svg');
    if(svg) svg.innerHTML = polys.join('');
    document.getElementById('c11s3Stats').innerHTML = `
      <div>Step <b>n = ${n}</b></div>
      <div>Shaded Triangles (3ⁿ): <b class="text-amber-300">${Math.pow(3, n)}</b></div>
      <div>Side Scale: <b class="text-cyan-300">1/${Math.pow(2, n)}</b> | Area: <b class="text-emerald-300">(3/4)^${n} = ${(Math.pow(0.75, n)*100).toFixed(1)}%</b></div>`;
  };
  window.c11s3Step(2);
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
      <span>❄️</span> Helge von Koch (1904) Snowflake Builder
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c11s4Step(0)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">Step 0</button>
      <button type="button" onclick="c11s4Step(1)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Step 1</button>
      <button type="button" onclick="c11s4Step(2)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">Step 2</button>
      <button type="button" onclick="c11s4Step(3)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Step 3</button>
    </div>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg id="c11s4Svg" viewBox="0 0 200 200" class="w-full max-w-[210px] mx-auto bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c11s4Stats" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
  </div>
</div>
<script>
(function(){
  function kochPts(p1, p2, depth, out){
    if(depth === 0){ out.push(p1); return; }
    const dx = (p2[0] - p1[0]) / 3, dy = (p2[1] - p1[1]) / 3;
    const a = [p1[0] + dx, p1[1] + dy];
    const b = [p1[0] + 2*dx, p1[1] + 2*dy];
    const cos60 = 0.5, sin60 = Math.sqrt(3) / 2;
    const peak = [a[0] + dx*cos60 + dy*sin60, a[1] - dx*sin60 + dy*cos60];
    kochPts(p1, a, depth - 1, out);
    kochPts(a, peak, depth - 1, out);
    kochPts(peak, b, depth - 1, out);
    kochPts(b, p2, depth - 1, out);
  }
  window.c11s4Step = function(n){
    const tri = [[100, 22], [170, 145], [30, 145]];
    const pts = [];
    for(let i = 0; i < 3; i++) kochPts(tri[i], tri[(i+1)%3], n, pts);
    const poly = pts.map(p => p[0].toFixed(1) + ',' + p[1].toFixed(1)).join(' ');
    const svg = document.getElementById('c11s4Svg');
    if(svg) svg.innerHTML = `<polygon points="${poly}" fill="#0ea5e9" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1.8"/>`;
    const edges = 3 * Math.pow(4, n);
    document.getElementById('c11s4Stats').innerHTML = `
      <div>Step <b>n = ${n}</b></div>
      <div>Outer Straight Edges (3×4ⁿ): <b class="text-cyan-300">${edges}</b></div>
      <div>Perimeter Multiplier: <b class="text-amber-300">(4/3)^${n} = ${(Math.pow(4/3, n)*100).toFixed(0)}%</b> of Step 0 (grows infinitely!)</div>`;
  };
  window.c11s4Step(2);
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>🛕</span> Fractals in Architecture, Textiles & Art
    </h3>
    <div class="flex flex-wrap gap-1.5 text-xs">
      <button type="button" onclick="c11s5Show('temple')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Temple Spires</button>
      <button type="button" onclick="c11s5Show('fulani')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Fulani Blanket</button>
      <button type="button" onclick="c11s5Show('escher')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">Escher Nesting</button>
    </div>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg id="c11s5Svg" viewBox="0 0 200 170" class="w-full max-w-[210px] mx-auto bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c11s5Desc" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
  </div>
</div>
<script>
(function(){
  window.c11s5Show = function(kind){
    const svg = document.getElementById('c11s5Svg');
    const desc = document.getElementById('c11s5Desc');
    if(!svg || !desc) return;
    if(kind === 'temple'){
      svg.innerHTML = `
        <polygon points="100,15 70,150 130,150" fill="#d97706" fill-opacity="0.35" stroke="#fbbf24" stroke-width="2"/>
        <polygon points="62,75 46,150 78,150" fill="#d97706" fill-opacity="0.3" stroke="#fbbf24" stroke-width="1.5"/>
        <polygon points="138,75 122,150 154,150" fill="#d97706" fill-opacity="0.3" stroke="#fbbf24" stroke-width="1.5"/>
        <polygon points="40,115 30,150 50,150" fill="#f59e0b" fill-opacity="0.3" stroke="#fcd34d" stroke-width="1"/>
        <polygon points="160,115 150,150 170,150" fill="#f59e0b" fill-opacity="0.3" stroke="#fcd34d" stroke-width="1"/>`;
      desc.innerHTML = `<b class="text-amber-300">Indian Temple Shikharas:</b><br>Kandariya Mahadev (Khajuraho) & Madurai/Hampi/Rameswaram towers nest smaller identical spires around one main tower!`;
    } else if(kind === 'fulani'){
      let d = '';
      [75, 55, 36, 18].forEach((r, idx) => {
        d += `<polygon points="100,${85-r} ${100+r},85 100,${85+r} ${100-r},85" fill="none" stroke="${idx%2===0?'#38bdf8':'#fbbf24'}" stroke-width="2"/>`;
      });
      svg.innerHTML = d;
      desc.innerHTML = `<b class="text-cyan-300">Nigerian Fulani Wedding Blankets:</b><br>Traditional geometric weaving layers nested rhombic motifs shrinking recursively inward!`;
    } else {
      let rings = '';
      [70, 48, 32, 20, 11].forEach((rad, i) => {
        rings += `<circle cx="100" cy="85" r="${rad}" fill="none" stroke="${i%2===0?'#34d399':'#a78bfa'}" stroke-width="2" stroke-dasharray="6,4"/>`;
      });
      svg.innerHTML = rings;
      desc.innerHTML = `<b class="text-emerald-300">M.C. Escher — 'Smaller and Smaller':</b><br>Interlocking creatures tile in diminishing scaled rings converging continuously inward toward the center!`;
    }
  };
  window.c11s5Show('temple');
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧠</span> Spatial Imagination: Corner Slicing & Angle Profiles
  </h3>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg id="c11s6Svg" viewBox="0 0 180 180" class="w-full max-w-[190px] mx-auto bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div class="space-y-3 text-xs">
      <label class="block text-slate-300">Square Corners Sliced Off: <span id="c11s6Cnt" class="font-bold text-amber-300">1 corner</span>
        <input id="c11s6Sl" type="range" min="0" max="4" value="1" oninput="c11s6Draw()" class="mt-2 w-full accent-amber-400">
      </label>
      <div id="c11s6Info" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-slate-300"></div>
    </div>
  </div>
</div>
<script>
(function(){
  const shapes = [
    [[35,35],[145,35],[145,145],[35,145]],
    [[60,35],[145,35],[145,145],[35,145],[35,60]],
    [[60,35],[120,35],[145,60],[145,145],[35,145],[35,60]],
    [[60,35],[120,35],[145,60],[145,120],[120,145],[35,145],[35,60]],
    [[60,35],[120,35],[145,60],[145,120],[120,145],[60,145],[35,120],[35,60]]
  ];
  const names = ['Square (4 corners)', 'Pentagon (5 corners!)', 'Hexagon (6 corners)', 'Heptagon (7 corners)', 'Octagon (8 corners!)'];
  window.c11s6Draw = function(){
    const c = parseInt(document.getElementById('c11s6Sl').value, 10) || 0;
    document.getElementById('c11s6Cnt').textContent = c + ' corner' + (c === 1 ? '' : 's');
    const pts = shapes[c].map(p => p.join(',')).join(' ');
    const svg = document.getElementById('c11s6Svg');
    if(svg) svg.innerHTML = `<polygon points="${pts}" fill="#0891b2" fill-opacity="0.35" stroke="#22d3ee" stroke-width="2.5"/>`;
    document.getElementById('c11s6Info').innerHTML = `Resulting Shape: <b class="text-emerald-300">${names[c]}</b>.<br>Each cut removes 1 vertex and adds 2 fresh vertices (+1 net edge per cut)!`;
  };
  window.c11s6Draw();
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
      <span>🧊</span> Polyhedra Analyzer: Faces, Edges & Vertices
    </h3>
    <div class="flex flex-wrap gap-1.5 text-xs">
      <button type="button" onclick="c11s7Show('cube')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Cube</button>
      <button type="button" onclick="c11s7Show('tprism')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">Tri Prism</button>
      <button type="button" onclick="c11s7Show('tetra')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Tetrahedron</button>
      <button type="button" onclick="c11s7Show('spyr')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700">Square Pyramid</button>
    </div>
  </div>
  <div id="c11s7Out" class="grid grid-cols-3 gap-2 text-center text-xs"></div>
  <div id="c11s7Desc" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  const solids = {
    cube:   { f: 6, e: 12, v: 8, text: '<b>Cube (Square Prism):</b> 2 congruent square bases + 4 square side faces.' },
    tprism: { f: 5, e: 9,  v: 6, text: '<b>Triangular Prism:</b> 2 parallel triangular bases joined by 3 rectangular faces.' },
    tetra:  { f: 4, e: 6,  v: 4, text: '<b>Tetrahedron (Triangular Pyramid):</b> 1 triangular base + 3 triangular walls converging at 1 apex.' },
    spyr:   { f: 5, e: 8,  v: 5, text: '<b>Square Pyramid:</b> 1 square base + 4 triangular walls rising cleanly to 1 apex.' }
  };
  window.c11s7Show = function(k){
    const s = solids[k] || solids.cube;
    document.getElementById('c11s7Out').innerHTML = `
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800"><div class="text-slate-400">Faces (F)</div><div class="text-lg font-bold text-cyan-300">${s.f}</div></div>
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800"><div class="text-slate-400">Edges (E)</div><div class="text-lg font-bold text-amber-300">${s.e}</div></div>
      <div class="p-3 rounded-xl bg-slate-950 border border-slate-800"><div class="text-slate-400">Vertices (V)</div><div class="text-lg font-bold text-emerald-300">${s.v}</div></div>`;
    document.getElementById('c11s7Desc').innerHTML = s.text;
  };
  window.c11s7Show('tetra');
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>📦</span> Cube (11 Nets) & Tetrahedron (2 Nets) Checker
    </h3>
    <div class="flex flex-wrap gap-1.5 text-xs">
      <button type="button" onclick="c11s8Show('cross')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">Cube Cross ✓</button>
      <button type="button" onclick="c11s8Show('rect23')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700">2×3 Strip ✗</button>
      <button type="button" onclick="c11s8Show('tetTri')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Tetra Net 1 ✓</button>
      <button type="button" onclick="c11s8Show('tetPara')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Tetra Net 2 ✓</button>
    </div>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
    <svg id="c11s8Svg" viewBox="0 0 200 160" class="w-full max-w-[210px] mx-auto bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c11s8Desc" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
  </div>
</div>
<script>
(function(){
  window.c11s8Show = function(kind){
    const svg = document.getElementById('c11s8Svg');
    const desc = document.getElementById('c11s8Desc');
    if(!svg || !desc) return;
    if(kind === 'cross'){
      const sqs = [[1,0],[0,1],[1,1],[2,1],[1,2],[1,3]].map(([c,r]) => `<rect x="${45+c*30}" y="${15+r*30}" width="28" height="28" fill="#10b981" fill-opacity="0.4" stroke="#34d399" stroke-width="2"/>`).join('');
      svg.innerHTML = sqs;
      desc.innerHTML = `<b class="text-emerald-300">Valid Cube Net (1 of 11):</b><br>Classic T-Cross folds cleanly along 5 crease lines without any two faces crashing!`;
    } else if(kind === 'rect23'){
      const sqs = [[0,0],[1,0],[2,0],[0,1],[1,1],[2,1]].map(([c,r]) => `<rect x="${50+c*32}" y="${45+r*32}" width="30" height="30" fill="#e11d48" fill-opacity="0.35" stroke="#fb7185" stroke-width="2"/>`).join('');
      svg.innerHTML = sqs;
      desc.innerHTML = `<b class="text-rose-300">Invalid Cube Net (Fails!):</b><br>A 2 × 3 grid contains 2 × 2 square blocks causing faces to collide onto the same side!`;
    } else if(kind === 'tetTri'){
      svg.innerHTML = `
        <polygon points="100,20 40,125 160,125" fill="#0891b2" fill-opacity="0.35" stroke="#22d3ee" stroke-width="2"/>
        <line x1="70" y1="72" x2="130" y2="72" stroke="#22d3ee" stroke-width="1.5" stroke-dasharray="3,2"/>
        <line x1="70" y1="72" x2="100" y2="125" stroke="#22d3ee" stroke-width="1.5" stroke-dasharray="3,2"/>
        <line x1="130" y1="72" x2="100" y2="125" stroke="#22d3ee" stroke-width="1.5" stroke-dasharray="3,2"/>`;
      desc.innerHTML = `<b class="text-cyan-300">Tetrahedron Net #1 (Large Triangle):</b><br>1 central triangle with 3 outer triangles folds smoothly into a 4-face Tetrahedron!`;
    } else {
      svg.innerHTML = `
        <polygon points="40,110 70,55 100,110" fill="#d97706" fill-opacity="0.35" stroke="#fbbf24" stroke-width="2"/>
        <polygon points="70,55 130,55 100,110" fill="#d97706" fill-opacity="0.35" stroke="#fbbf24" stroke-width="2"/>
        <polygon points="100,110 130,55 160,110" fill="#d97706" fill-opacity="0.35" stroke="#fbbf24" stroke-width="2"/>
        <polygon points="130,55 190,55 160,110" fill="#d97706" fill-opacity="0.35" stroke="#fbbf24" stroke-width="2"/>`;
      desc.innerHTML = `<b class="text-amber-300">Tetrahedron Net #2 (Parallelogram Strip):</b><br>Four alternating equilateral triangles wrap around neatly into the ONLY other Tetrahedron net!`;
    }
  };
  window.c11s8Show('cross');
})();
</script>
"""
}
