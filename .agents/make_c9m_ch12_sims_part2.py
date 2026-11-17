#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 12: Quadrilaterals
Part 2: Simulators 9 to 16 (Slides 9 to 16)
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🎯</span> Theorem 8: Centroid Concurrency (2 : 1 Ratio)
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Move Apex A Horizontally:</span>
      <span class="text-amber-300 font-bold">AG : GD = BG : GE = CG : GF = 2 : 1</span>
    </div>
    <input id="c9c12s9Ax" type="range" min="80" max="280" value="150" oninput="c9c12s9Draw()" class="w-full accent-amber-400">
  </label>
  <svg id="c9c12s9Svg" viewBox="0 0 360 185" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  window.c9c12s9Draw = function(){
    const ax = parseFloat(document.getElementById('c9c12s9Ax').value);
    const A = [ax, 25], B = [60, 155], C = [300, 155];
    const D = [(B[0]+C[0])/2, (B[1]+C[1])/2];
    const E = [(A[0]+C[0])/2, (A[1]+C[1])/2];
    const F = [(A[0]+B[0])/2, (A[1]+B[1])/2];
    const G = [(A[0]+B[0]+C[0])/3, (A[1]+B[1]+C[1])/3];
    const P = [(B[0]+G[0])/2, (B[1]+G[1])/2];
    const Q = [(C[0]+G[0])/2, (C[1]+G[1])/2];
    document.getElementById('c9c12s9Svg').innerHTML = `
      <polygon points="${A[0]},${A[1]} ${B[0]},${B[1]} ${C[0]},${C[1]}" fill="rgba(56,189,248,0.1)" stroke="#38bdf8" stroke-width="2.5"/>
      <polygon points="${F[0]},${F[1]} ${E[0]},${E[1]} ${Q[0]},${Q[1]} ${P[0]},${P[1]}" fill="rgba(16,185,129,0.22)" stroke="#34d399" stroke-width="2"/>
      <line x1="${A[0]}" y1="${A[1]}" x2="${D[0]}" y2="${D[1]}" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="4,3"/>
      <line x1="${B[0]}" y1="${B[1]}" x2="${E[0]}" y2="${E[1]}" stroke="#fbbf24" stroke-width="2"/>
      <line x1="${C[0]}" y1="${C[1]}" x2="${F[0]}" y2="${F[1]}" stroke="#fbbf24" stroke-width="2"/>
      <circle cx="${G[0]}" cy="${G[1]}" r="5.5" fill="#f43f5e"/>
      <text x="${G[0]+8}" y="${G[1]-4}" fill="#f43f5e" font-size="12" font-weight="bold">G</text>
      <text x="180" y="176" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Parallelogram FEQP proves PG = GE &amp; QG = GF ⇒ 2 : 1</text>`;
  };
  c9c12s9Draw();
})();
</script>""",

    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔷</span> Theorem 9: Varignon Parallelogram Universal Lab
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button onclick="c9c12s10Set('general')" class="px-2.5 py-1 rounded-lg bg-cyan-600 text-white font-semibold">General</button>
    <button onclick="c9c12s10Set('dart')" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold">Non-Convex Dart</button>
    <button onclick="c9c12s10Set('rect')" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold">Rectangle → Rhombus</button>
    <button onclick="c9c12s10Set('rhomb')" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-semibold">Rhombus → Rectangle</button>
  </div>
  <svg id="c9c12s10Svg" viewBox="0 0 360 185" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c9c12s10Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  const presets = {
    general: { pts: [[70,150],[285,140],[245,35],[95,55]], msg: 'Any planar 4-gon: Varignon PQRS is ALWAYS a parallelogram with Area(PQRS) = ½ Area(ABCD).' },
    dart:    { pts: [[65,155],[180,108],[295,155],[180,30]], msg: 'Even a NON-CONVEX dart produces a convex Varignon parallelogram PQRS!' },
    rect:    { pts: [[80,150],[280,150],[280,45],[80,45]], msg: 'Equal diagonals (AC = BD) force all 4 Varignon sides equal ⇒ RHOMBUS!' },
    rhomb:   { pts: [[180,160],[285,95],[180,30],[75,95]], msg: 'Perpendicular diagonals (AC ⊥ BD) force 90° Varignon corners ⇒ RECTANGLE!' }
  };
  window.c9c12s10Set = function(k){
    const p = presets[k].pts;
    const mid = (a,b) => [(a[0]+b[0])/2, (a[1]+b[1])/2];
    const P = mid(p[0],p[1]), Q = mid(p[1],p[2]), R = mid(p[2],p[3]), S = mid(p[3],p[0]);
    document.getElementById('c9c12s10Svg').innerHTML = `
      <polygon points="${p.map(x=>x.join(',')).join(' ')}" fill="rgba(56,189,248,0.12)" stroke="#38bdf8" stroke-width="2.5"/>
      <line x1="${p[0][0]}" y1="${p[0][1]}" x2="${p[2][0]}" y2="${p[2][1]}" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,3"/>
      <line x1="${p[1][0]}" y1="${p[1][1]}" x2="${p[3][0]}" y2="${p[3][1]}" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,3"/>
      <polygon points="${[P,Q,R,S].map(x=>x.join(',')).join(' ')}" fill="rgba(16,185,129,0.28)" stroke="#34d399" stroke-width="3"/>
      <text x="${P[0]}" y="${P[1]+13}" fill="#34d399" font-size="11" font-weight="bold">P</text>
      <text x="${Q[0]+6}" y="${Q[1]}" fill="#34d399" font-size="11" font-weight="bold">Q</text>
      <text x="${R[0]}" y="${R[1]-6}" fill="#34d399" font-size="11" font-weight="bold">R</text>
      <text x="${S[0]-13}" y="${S[1]}" fill="#34d399" font-size="11" font-weight="bold">S</text>`;
    document.getElementById('c9c12s10Out').innerHTML = '<span class="text-emerald-400 font-bold">VARIGNON RESULT:</span> ' + presets[k].msg;
  };
  c9c12s10Set('general');
})();
</script>""",

    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧩</span> Method 1: 180° Edge-Midpoint Plane Tiling
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Grow Tiles Around Central Vertex (180° Midpoint Rotations):</span>
      <span id="c9c12s11Lbl" class="text-amber-300 font-bold">4 Tiles (360° Complete)</span>
    </div>
    <input id="c9c12s11Step" type="range" min="1" max="4" value="4" oninput="c9c12s11Draw()" class="w-full accent-amber-400">
  </label>
  <svg id="c9c12s11Svg" viewBox="0 0 360 190" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  const rot180 = (pt, m) => [2*m[0]-pt[0], 2*m[1]-pt[1]];
  window.c9c12s11Draw = function(){
    const k = parseInt(document.getElementById('c9c12s11Step').value, 10);
    document.getElementById('c9c12s11Lbl').textContent = k + ' Tile' + (k>1?'s':'') + (k===4?' (360° Complete)':'');
    const A=[180,95], B=[245,105], C=[225,45], D=[165,55];
    const mAB=[(A[0]+B[0])/2,(A[1]+B[1])/2], mAD=[(A[0]+D[0])/2,(A[1]+D[1])/2];
    const t1 = [A,B,C,D];
    const t2 = t1.map(p => rot180(p, mAB));
    const t3 = t1.map(p => rot180(p, mAD));
    const m2BC = [(t2[1][0]+t2[2][0])/2, (t2[1][1]+t2[2][1])/2];
    const m2AD = [(t2[0][0]+t2[3][0])/2, (t2[0][1]+t2[3][1])/2];
    const t4 = t2.map(p => rot180(p, m2AD));
    const tiles = [
      {pts:t1, fill:'rgba(56,189,248,0.35)', stroke:'#38bdf8'},
      {pts:t2, fill:'rgba(16,185,129,0.35)', stroke:'#34d399'},
      {pts:t3, fill:'rgba(245,158,11,0.35)', stroke:'#fbbf24'},
      {pts:t4, fill:'rgba(168,85,247,0.35)', stroke:'#c084fc'}
    ];
    let html = '';
    for (let i=0; i<k; i++){
      html += `<polygon points="${tiles[i].pts.map(x=>x.join(',')).join(' ')}" fill="${tiles[i].fill}" stroke="${tiles[i].stroke}" stroke-width="2"/>`;
    }
    html += `<circle cx="${A[0]}" cy="${A[1]}" r="5" fill="#f43f5e"/>`;
    html += `<text x="180" y="178" text-anchor="middle" fill="#cbd5e1" font-size="11" font-weight="bold">Around red vertex: ∠A + ∠B + ∠C + ∠D = 360° (Zero Gaps!)</text>`;
    document.getElementById('c9c12s11Svg').innerHTML = html;
  };
  c9c12s11Draw();
})();
</script>""",

    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔬</span> Method 2 (Varignon Grid) &amp; Aperiodic Discovery
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c12s12Mode('grid')" id="c9c12s12B_grid" class="px-3 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold">Varignon Translation Grid</button>
    <button onclick="c9c12s12Mode('aperiodic')" id="c9c12s12B_aperiodic" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Quasicrystals &amp; Hat Monotile</button>
  </div>
  <svg id="c9c12s12Svg" viewBox="0 0 360 180" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c9c12s12Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c9c12s12Mode = function(m){
    document.getElementById('c9c12s12B_grid').className = m === 'grid' ? 'px-3 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold' : 'px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold';
    document.getElementById('c9c12s12B_aperiodic').className = m === 'aperiodic' ? 'px-3 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold' : 'px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold';
    const svg = document.getElementById('c9c12s12Svg');
    const out = document.getElementById('c9c12s12Out');
    if (m === 'grid') {
      let html = '';
      for (let r=0; r<3; r++){
        for (let c=0; c<4; c++){
          const x = 45 + c*65 + r*15, y = 30 + r*45;
          html += `<polygon points="${x},${y} ${x+65},${y} ${x+80},${y+45} ${x+15},${y+45}" fill="rgba(56,189,248,0.16)" stroke="#38bdf8" stroke-width="1.8"/>`;
          html += `<polygon points="${x+32},${y} ${x+72},${y+22} ${x+47},${y+45} ${x+7},${y+22}" fill="rgba(16,185,129,0.28)" stroke="#34d399" stroke-width="1.5"/>`;
        }
      }
      svg.innerHTML = html;
      out.innerHTML = '<span class="text-emerald-400 font-bold">PERIODIC VARIGNON GRID:</span> Every 4-gon tiling repeats periodically by translation with unit cell area = 2 × Area(Varignon PQRS).';
    } else {
      let html = '<g transform="translate(180,90)">';
      for (let i=0; i<10; i++){
        const a = i * 36 * Math.PI / 180, a2 = (i+1)*36*Math.PI/180;
        const r1 = 35, r2 = 68;
        html += `<polygon points="0,0 ${r1*Math.cos(a)},${r1*Math.sin(a)} ${r2*Math.cos((a+a2)/2)},${r2*Math.sin((a+a2)/2)} ${r1*Math.cos(a2)},${r1*Math.sin(a2)}" fill="${i%2?'rgba(245,158,11,0.3)':'rgba(168,85,247,0.3)'}" stroke="#fbbf24" stroke-width="1.8"/>`;
      }
      html += '</g><text x="180" y="172" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">5-Fold Quasicrystal Symmetry (Never Repeats Periodically!)</text>';
      svg.innerHTML = html;
      out.innerHTML = '<span class="text-amber-300 font-bold">APERIODIC ORDER:</span> Dan Shechtman (2011 Nobel Prize) found 5-fold quasicrystals in alloys, and the 2023 13-sided Hat Monotile tiles the plane ONLY aperiodically.';
    }
  };
  c9c12s12Mode('grid');
})();
</script>""",

    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔧</span> 4-Bar Linkage Flexing &amp; Angle Bisector Rectangle
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Flex Parallelogram Tilt Angle (θ):</span>
      <span id="c9c12s13Lbl" class="text-amber-300 font-bold">θ = 65° (Bisector Box = Rectangle 90°)</span>
    </div>
    <input id="c9c12s13T" type="range" min="35" max="145" value="65" oninput="c9c12s13Draw()" class="w-full accent-amber-400">
  </label>
  <svg id="c9c12s13Svg" viewBox="0 0 360 185" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  window.c9c12s13Draw = function(){
    const th = parseFloat(document.getElementById('c9c12s13T').value);
    const rad = th * Math.PI / 180;
    const A = [85, 150], B = [245, 150], L = 105;
    const D = [A[0] + L*Math.cos(rad), A[1] - L*Math.sin(rad)];
    const C = [B[0] + L*Math.cos(rad), B[1] - L*Math.sin(rad)];
    const mid1 = [(A[0]+C[0])/2, (A[1]+C[1])/2];
    const u = [Math.cos(rad/2), -Math.sin(rad/2)];
    const v = [-Math.sin(rad/2), -Math.cos(rad/2)];
    const d1 = 36, d2 = 22;
    const P = [mid1[0]-d1*u[0], mid1[1]-d1*u[1]];
    const R = [mid1[0]+d1*u[0], mid1[1]+d1*u[1]];
    const Q = [mid1[0]+d2*v[0], mid1[1]+d2*v[1]];
    const S = [mid1[0]-d2*v[0], mid1[1]-d2*v[1]];
    document.getElementById('c9c12s13Svg').innerHTML = `
      <polygon points="${A[0]},${A[1]} ${B[0]},${B[1]} ${C[0]},${C[1]} ${D[0]},${D[1]}" fill="rgba(56,189,248,0.12)" stroke="#38bdf8" stroke-width="3"/>
      <polygon points="${P[0]},${P[1]} ${Q[0]},${Q[1]} ${R[0]},${R[1]} ${S[0]},${S[1]}" fill="rgba(16,185,129,0.28)" stroke="#34d399" stroke-width="2.5"/>
      <text x="180" y="22" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">½∠A + ½∠B = 90° ⇒ Inner Bisectors Form a 90° Rectangle!</text>`;
  };
  c9c12s13Draw();
})();
</script>""",

    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>✂️</span> Scissors Congruence: Cut Midline &amp; Rotate 180°
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Rotate Top △ADE Around E:</span>
      <span id="c9c12s14Lbl" class="text-amber-300 font-bold">0°</span>
    </div>
    <input id="c9c12s14Rot" type="range" min="0" max="180" value="0" oninput="c9c12s14Draw()" class="w-full accent-amber-400">
  </label>
  <svg id="c9c12s14Svg" viewBox="0 0 360 185" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  window.c9c12s14Draw = function(){
    const deg = parseFloat(document.getElementById('c9c12s14Rot').value);
    document.getElementById('c9c12s14Lbl').textContent = deg + '°' + (deg===180 ? ' (Parallelogram Complete!)' : '');
    const A=[150,30], B=[65,155], C=[255,155];
    const D=[(A[0]+B[0])/2,(A[1]+B[1])/2], E=[(A[0]+C[0])/2,(A[1]+C[1])/2];
    document.getElementById('c9c12s14Svg').innerHTML = `
      <polygon points="${D[0]},${D[1]} ${B[0]},${B[1]} ${C[0]},${C[1]} ${E[0]},${E[1]}" fill="rgba(56,189,248,0.22)" stroke="#38bdf8" stroke-width="2.5"/>
      <g transform="rotate(${deg}, ${E[0]}, ${E[1]})">
        <polygon points="${A[0]},${A[1]} ${D[0]},${D[1]} ${E[0]},${E[1]}" fill="rgba(16,185,129,0.35)" stroke="#34d399" stroke-width="2.5"/>
      </g>
      <circle cx="${E[0]}" cy="${E[1]}" r="4.5" fill="#fbbf24"/>
      <text x="180" y="176" text-anchor="middle" fill="#cbd5e1" font-size="11" font-weight="bold">Area(△ABC) = Area(Parallelogram) by 180° Midpoint Rotation</text>`;
  };
  c9c12s14Draw();
})();
</script>""",

    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📊</span> Trapezium Midsegment &amp; Polygon Diagonals Calculator
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Base a:</span><span id="c9c12s15AL" class="text-cyan-300 font-bold">10</span></div>
      <input id="c9c12s15A" type="range" min="4" max="20" value="10" oninput="c9c12s15Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Base b:</span><span id="c9c12s15BL" class="text-emerald-300 font-bold">18</span></div>
      <input id="c9c12s15B" type="range" min="8" max="26" value="18" oninput="c9c12s15Draw()" class="w-full accent-emerald-400">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>n-gon sides:</span><span id="c9c12s15NL" class="text-amber-300 font-bold">6</span></div>
      <input id="c9c12s15N" type="range" min="4" max="10" value="6" oninput="c9c12s15Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9c12s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c12s15Draw = function(){
    const a = parseInt(document.getElementById('c9c12s15A').value, 10);
    const b = parseInt(document.getElementById('c9c12s15B').value, 10);
    const n = parseInt(document.getElementById('c9c12s15N').value, 10);
    document.getElementById('c9c12s15AL').textContent = a + ' cm';
    document.getElementById('c9c12s15BL').textContent = b + ' cm';
    document.getElementById('c9c12s15NL').textContent = n;
    const m = ((a+b)/2).toFixed(1);
    const diag = n * (n - 3) / 2;
    document.getElementById('c9c12s15Out').innerHTML = `
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
        <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
          <div class="text-slate-400">Trapezium Midsegment m = ½(a + b)</div>
          <div class="text-lg font-bold text-cyan-300">${m} cm</div>
        </div>
        <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800">
          <div class="text-slate-400">Diagonals of ${n}-gon = n(n−3)/2</div>
          <div class="text-lg font-bold text-amber-300">${diag} diagonals</div>
        </div>
      </div>
      <div class="text-rose-300 font-semibold">Skew 4-Gon Reminder: Folding a planar 4-gon out of its plane reduces Σ∠ strictly below 360°.</div>`;
  };
  c9c12s15Draw();
})();
</script>""",

    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏆</span> Chapter 12 Theorem &amp; Parallelogram Test Verifier
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <button onclick="c9c12s16Check(0)" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-left font-semibold text-slate-200">1. AB = CD &amp; BC = DA</button>
    <button onclick="c9c12s16Check(1)" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-left font-semibold text-slate-200">2. ∠A = ∠C &amp; ∠B = ∠D</button>
    <button onclick="c9c12s16Check(2)" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-left font-semibold text-slate-200">3. OA = OC &amp; OB = OD</button>
    <button onclick="c9c12s16Check(3)" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-left font-semibold text-slate-200">4. AB = CD &amp; AB ∥ CD</button>
    <button onclick="c9c12s16Check(4)" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-left font-semibold text-slate-200">5. AB ∥ CD &amp; BC = DA</button>
    <button onclick="c9c12s16Check(5)" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-left font-semibold text-slate-200">6. Midpoints PQRS (Any 4-gon)</button>
  </div>
  <div id="c9c12s16Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  const items = [
    '<span class="text-emerald-400 font-bold">SUFFICIENT (Theorem 2 — SSS):</span> Both pairs of opposite sides equal ⇒ Parallelogram.',
    '<span class="text-emerald-400 font-bold">SUFFICIENT (Theorem 3 — Algebra):</span> Both pairs of opposite angles equal ⇒ ∠A + ∠B = 180° ⇒ Parallelogram.',
    '<span class="text-emerald-400 font-bold">SUFFICIENT (Theorem 4 — SAS):</span> Diagonals bisect each other ⇒ ΔAOB ≅ ΔCOD ⇒ Parallelogram.',
    '<span class="text-emerald-400 font-bold">SUFFICIENT (Theorem 5 — SAS):</span> One pair of opposite sides is BOTH equal and parallel ⇒ Parallelogram.',
    '<span class="text-rose-400 font-bold">NOT SUFFICIENT (Counterexample):</span> One pair parallel and the OTHER pair equal allows an isosceles trapezium!',
    '<span class="text-cyan-300 font-bold">UNIVERSAL (Theorem 9 — Varignon):</span> Midpoints of ANY planar 4-gon (even non-convex) always form a parallelogram!'
  ];
  window.c9c12s16Check = function(i){
    document.getElementById('c9c12s16Out').innerHTML = items[i];
  };
  c9c12s16Check(0);
})();
</script>""",
}
