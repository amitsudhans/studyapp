#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 8 Maths Chapter 14: Area
Part 1: Simulators 1 to 8
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🟧</span> Four-Way Equal-Area Square Divider (64 cm²)
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c14s1Mode(0)" id="c14s1b0" class="px-2 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">4 Strips</button>
    <button type="button" onclick="c14s1Mode(1)" id="c14s1b1" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">2×2 Squares</button>
    <button type="button" onclick="c14s1Mode(2)" id="c14s1b2" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">4 Diagonals</button>
    <button type="button" onclick="c14s1Mode(3)" id="c14s1b3" class="px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">Mixed Non-Congruent</button>
  </div>
  <div class="flex flex-col sm:flex-row gap-3 items-center">
    <svg id="c14s1Svg" viewBox="0 0 160 160" class="w-40 h-40 bg-slate-950 rounded-xl border border-slate-800 shrink-0"></svg>
    <div id="c14s1Out" class="flex-1 p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
  </div>
</div>
<script>
(function(){
  const info = [
    ['4 Vertical Strips (2×8 cm)', 'Each strip covers 2 × 8 = 16 cm² (1/4 of 64 cm²).'],
    ['2×2 Quadrant Squares (4×4 cm)', 'Each corner square covers 4 × 4 = 16 cm².'],
    ['4 Diagonal Triangles', 'Intersecting diagonals slice 4 congruent right triangles of 16 cm² each.'],
    ['Mixed Non-Congruent Quarters', 'Top half splits into two 4×4 squares (16 cm² each); bottom half splits along a diagonal into two 8×4 right triangles (16 cm² each)!']
  ];
  window.c14s1Mode = function(m){
    [0,1,2,3].forEach(i => {
      const b = document.getElementById('c14s1b'+i);
      if(b) b.className = i===m ? 'px-2 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    const svg = document.getElementById('c14s1Svg');
    let shapes = '';
    if(m===0){
      shapes = `<rect x="16" y="16" width="32" height="128" fill="#0891b2" fill-opacity="0.35" stroke="#22d3ee"/><rect x="48" y="16" width="32" height="128" fill="#d97706" fill-opacity="0.35" stroke="#fbbf24"/><rect x="80" y="16" width="32" height="128" fill="#059669" fill-opacity="0.35" stroke="#34d399"/><rect x="112" y="16" width="32" height="128" fill="#e11d48" fill-opacity="0.35" stroke="#fb7185"/>`;
    } else if(m===1){
      shapes = `<rect x="16" y="16" width="64" height="64" fill="#0891b2" fill-opacity="0.35" stroke="#22d3ee"/><rect x="80" y="16" width="64" height="64" fill="#d97706" fill-opacity="0.35" stroke="#fbbf24"/><rect x="16" y="80" width="64" height="64" fill="#059669" fill-opacity="0.35" stroke="#34d399"/><rect x="80" y="80" width="64" height="64" fill="#e11d48" fill-opacity="0.35" stroke="#fb7185"/>`;
    } else if(m===2){
      shapes = `<polygon points="16,16 144,16 80,80" fill="#0891b2" fill-opacity="0.35" stroke="#22d3ee"/><polygon points="144,16 144,144 80,80" fill="#d97706" fill-opacity="0.35" stroke="#fbbf24"/><polygon points="144,144 16,144 80,80" fill="#059669" fill-opacity="0.35" stroke="#34d399"/><polygon points="16,144 16,16 80,80" fill="#e11d48" fill-opacity="0.35" stroke="#fb7185"/>`;
    } else {
      shapes = `<rect x="16" y="16" width="64" height="64" fill="#0891b2" fill-opacity="0.35" stroke="#22d3ee"/><rect x="80" y="16" width="64" height="64" fill="#d97706" fill-opacity="0.35" stroke="#fbbf24"/><polygon points="16,80 144,80 16,144" fill="#059669" fill-opacity="0.35" stroke="#34d399"/><polygon points="144,80 144,144 16,144" fill="#e11d48" fill-opacity="0.35" stroke="#fb7185"/>`;
    }
    if(svg) svg.innerHTML = shapes + `<rect x="16" y="16" width="128" height="128" fill="none" stroke="#f8fafc" stroke-width="2"/>`;
    document.getElementById('c14s1Out').innerHTML = `
      <div class="text-amber-300 font-bold">${info[m][0]}</div>
      <div>${info[m][1]}</div>
      <div class="text-emerald-300">Edge Rule: compressing width ×1/2 and expanding height ×2 keeps area invariant at <b>16 cm²</b> per quarter!</div>`;
  };
  window.c14s1Mode(0);
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
      <span>🧱</span> Unit-Square Packer & Diagonal Bisector
    </h3>
    <button type="button" onclick="c14s2Tog()" id="c14s2Btn" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 text-xs border border-slate-700">Toggle Diagonal Cut</button>
  </div>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <div><span class="text-slate-400">Length (cm): <b id="c14s2Lv" class="text-cyan-300">6</b></span><input id="c14s2L" type="range" min="2" max="8" value="6" oninput="c14s2Draw()" class="w-full accent-cyan-400"></div>
    <div><span class="text-slate-400">Width (cm): <b id="c14s2Wv" class="text-amber-300">4</b></span><input id="c14s2W" type="range" min="2" max="6" value="4" oninput="c14s2Draw()" class="w-full accent-amber-400"></div>
  </div>
  <svg id="c14s2Svg" viewBox="0 0 280 155" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c14s2Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  let diag = true;
  window.c14s2Tog = function(){ diag = !diag; window.c14s2Draw(); };
  window.c14s2Draw = function(){
    const l = parseInt(document.getElementById('c14s2L').value,10)||6;
    const w = parseInt(document.getElementById('c14s2W').value,10)||4;
    document.getElementById('c14s2Lv').textContent = l;
    document.getElementById('c14s2Wv').textContent = w;
    const cell = 20, x0 = 140 - (l*cell)/2, y0 = 76 - (w*cell)/2;
    let grid = '';
    for(let r=0;r<w;r++){
      for(let c=0;c<l;c++){
        grid += `<rect x="${x0+c*cell}" y="${y0+r*cell}" width="${cell}" height="${cell}" fill="#0891b2" fill-opacity="0.18" stroke="#334155"/>`;
      }
    }
    let overlay = '';
    if(diag){
      overlay = `<polygon points="${x0},${y0} ${x0+l*cell},${y0+w*cell} ${x0},${y0+w*cell}" fill="#34d399" fill-opacity="0.28"/><line x1="${x0}" y1="${y0}" x2="${x0+l*cell}" y2="${y0+w*cell}" stroke="#fbbf24" stroke-width="2.5"/>`;
    }
    const svg = document.getElementById('c14s2Svg');
    if(svg) svg.innerHTML = grid + `<rect x="${x0}" y="${y0}" width="${l*cell}" height="${w*cell}" fill="none" stroke="#22d3ee" stroke-width="2"/>` + overlay;
    document.getElementById('c14s2Out').innerHTML = `Total Unit Squares = ${l} × ${w} = <b class="text-cyan-300">${l*w} cm²</b> &nbsp;|&nbsp; Congruent Diagonal Halves (SSS): <b class="text-emerald-300">${(l*w)/2} cm²</b> each!`;
  };
  window.c14s2Draw();
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-rose-300 flex items-center gap-2">
    <span>📏</span> Same Perimeter (24 m), Wildly Different Areas!
  </h3>
  <div class="space-y-2 text-xs">
    <div class="flex justify-between text-slate-300"><span>Adjust Width w (Length auto-adjusts L = 12 − w to lock P = 24 m):</span><b id="c14s3Dim" class="text-amber-300">6 m × 6 m</b></div>
    <input id="c14s3Sl" type="range" min="1" max="6" value="6" oninput="c14s3Draw()" class="w-full accent-rose-400">
    <svg id="c14s3Svg" viewBox="0 0 320 110" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c14s3Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-300"></div>
  </div>
</div>
<script>
(function(){
  window.c14s3Draw = function(){
    const w = parseInt(document.getElementById('c14s3Sl').value,10)||6;
    const l = 12 - w;
    document.getElementById('c14s3Dim').textContent = `${l} m × ${w} m`;
    const area = l * w;
    const rw = l * 22, rh = w * 13;
    const x0 = 160 - rw/2, y0 = 55 - rh/2;
    const svg = document.getElementById('c14s3Svg');
    if(svg) svg.innerHTML = `<rect x="${x0}" y="${y0}" width="${rw}" height="${rh}" fill="#fb7185" fill-opacity="0.28" stroke="#fb7185" stroke-width="2"/><text x="160" y="59" text-anchor="middle" fill="#f8fafc" font-size="12" font-weight="bold">Area = ${area} m² (P = 24 m)</text>`;
    document.getElementById('c14s3Out').innerHTML = `Perimeter = 2(${l} + ${w}) = <b class="text-cyan-300">24 m (FIXED)</b>, yet Enclosed Area = <b class="text-emerald-300">${area} m²</b>! (Carving inward notches drops area even further while INCREASING perimeter!)`;
  };
  window.c14s3Draw();
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>📐</span> Sliding Apex Inside Rectangle PQRS (14 × 8)
  </h3>
  <div class="space-y-2 text-xs">
    <div class="flex justify-between text-slate-300"><span>Slide Apex T horizontally along Top Edge SR:</span><b id="c14s4Pos" class="text-amber-300">T at x = 7 cm</b></div>
    <input id="c14s4Sl" type="range" min="1" max="13" step="0.5" value="7" oninput="c14s4Draw()" class="w-full accent-emerald-400">
    <svg id="c14s4Svg" viewBox="0 0 320 130" class="w-full h-32 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c14s4Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-300"></div>
  </div>
</div>
<script>
(function(){
  window.c14s4Draw = function(){
    const t = parseFloat(document.getElementById('c14s4Sl').value)||7;
    document.getElementById('c14s4Pos').textContent = `T at x = ${t} cm from left`;
    const tx = 40 + (t/14)*240;
    const svg = document.getElementById('c14s4Svg');
    if(svg) svg.innerHTML = `
      <rect x="40" y="18" width="240" height="90" fill="none" stroke="#64748b" stroke-width="2"/>
      <polygon points="40,108 280,108 ${tx.toFixed(1)},18" fill="#10b981" fill-opacity="0.32" stroke="#34d399" stroke-width="2.2"/>
      <line x1="${tx.toFixed(1)}" y1="18" x2="${tx.toFixed(1)}" y2="108" stroke="#fbbf24" stroke-dasharray="4 3" stroke-width="1.8"/>
      <circle cx="${tx.toFixed(1)}" cy="18" r="4.5" fill="#fbbf24"/>
      <text x="${tx.toFixed(1)}" y="12" text-anchor="middle" fill="#fde68a" font-size="10">T</text>
      <text x="160" y="124" text-anchor="middle" fill="#94a3b8" font-size="10">Base PQ = 14 cm, Height h = 8 cm</text>`;
    const leftA = (0.5 * t * 8).toFixed(1), rightA = (0.5 * (14-t) * 8).toFixed(1);
    document.getElementById('c14s4Out').innerHTML = `Left Half-Box = <b class="text-cyan-300">${leftA} cm²</b> + Right Half-Box = <b class="text-amber-300">${rightA} cm²</b> → Total Area(ΔPQT) = <b class="text-emerald-300">56.0 cm² (Always Half of 112 cm²!)</b>`;
  };
  window.c14s4Draw();
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🔺</span> Obtuse Overhang Subtraction Proof (AB = 10, h = 6)
  </h3>
  <div class="space-y-2 text-xs">
    <div class="flex justify-between text-slate-300"><span>Overhang Extension BD (x):</span><b id="c14s5Val" class="text-cyan-300">x = 5 cm</b></div>
    <input id="c14s5Sl" type="range" min="1" max="8" value="5" oninput="c14s5Draw()" class="w-full accent-amber-400">
    <svg id="c14s5Svg" viewBox="0 0 330 125" class="w-full h-32 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c14s5Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-300"></div>
  </div>
</div>
<script>
(function(){
  window.c14s5Draw = function(){
    const x = parseInt(document.getElementById('c14s5Sl').value,10)||5;
    document.getElementById('c14s5Val').textContent = `x = ${x} cm outside B`;
    const cx = 175 + x * 14;
    const svg = document.getElementById('c14s5Svg');
    if(svg) svg.innerHTML = `
      <polygon points="175,98 ${cx},98 ${cx},22" fill="#e11d48" fill-opacity="0.18" stroke="#fb7185" stroke-dasharray="4 3"/>
      <polygon points="35,98 175,98 ${cx},22" fill="#0ea5e9" fill-opacity="0.34" stroke="#38bdf8" stroke-width="2.2"/>
      <line x1="${cx}" y1="22" x2="${cx}" y2="98" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4 2"/>
      <text x="105" y="114" text-anchor="middle" fill="#cbd5e1" font-size="10">b = 10</text>
      <text x="${(175+cx)/2}" y="114" text-anchor="middle" fill="#fda4af" font-size="10">x = ${x}</text>
      <text x="${cx+10}" y="62" fill="#fde68a" font-size="10">h=6</text>`;
    const big = 0.5*(10+x)*6, small = 0.5*x*6;
    document.getElementById('c14s5Out').innerHTML = `Big ΔADC (<b>${big}</b>) − White ΔBDC (<b>${small}</b>) = <b class="text-emerald-300">${big - small} cm²</b>! Notice ½xh cancels out completely!`;
  };
  window.c14s5Draw();
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📏</span> Dual Base-Altitude Law (b₁h₁ = b₂h₂)
  </h3>
  <div class="space-y-2 text-xs">
    <div class="text-slate-300">Fixed Triangle Area = <b>72 cm²</b> (since b₁ = 16 cm, h₁ = 9 cm → b₁h₁ = 144)</div>
    <div class="flex justify-between text-slate-300"><span>Choose Second Side Base (b₂):</span><b id="c14s6Val" class="text-amber-300">b₂ = 12 cm</b></div>
    <input id="c14s6Sl" type="range" min="6" max="24" step="1" value="12" oninput="c14s6Draw()" class="w-full accent-cyan-400">
    <div id="c14s6Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 space-y-1"></div>
  </div>
</div>
<script>
(function(){
  window.c14s6Draw = function(){
    const b2 = parseInt(document.getElementById('c14s6Sl').value,10)||12;
    document.getElementById('c14s6Val').textContent = `b₂ = ${b2} cm`;
    const h2 = 144 / b2;
    document.getElementById('c14s6Out').innerHTML = `
      <div>Equate areas: 1/2 × 16 × 9 = 1/2 × ${b2} × h₂ → <b>144 = ${b2} × h₂</b></div>
      <div class="text-emerald-300 font-bold text-sm">Corresponding Altitude h₂ = ${h2.toFixed(2).replace(/\\.00$/,'')} cm</div>
      <div class="text-slate-400">Inverse Rule: shorter base side always pairs with a taller perpendicular altitude!</div>`;
  };
  window.c14s6Draw();
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>⚖️</span> Median Bisects Any Triangle's Area (Total = 84 cm²)
  </h3>
  <div class="space-y-2 text-xs">
    <div class="flex justify-between text-slate-300"><span>Slide Base Divider Point P along BC (Total BC = 12 cm):</span><b id="c14s7Val" class="text-amber-300">BP = 6 cm (MIDPOINT M!)</b></div>
    <input id="c14s7Sl" type="range" min="1" max="11" value="6" oninput="c14s7Draw()" class="w-full accent-emerald-400">
    <svg id="c14s7Svg" viewBox="0 0 320 120" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c14s7Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-300"></div>
  </div>
</div>
<script>
(function(){
  window.c14s7Draw = function(){
    const bp = parseInt(document.getElementById('c14s7Sl').value,10)||6;
    const pc = 12 - bp;
    const isMed = bp === 6;
    document.getElementById('c14s7Val').textContent = isMed ? 'BP = 6 cm (MIDPOINT M — MEDIAN!)' : `BP = ${bp} cm, PC = ${pc} cm`;
    const px = 40 + (bp/12)*240;
    const svg = document.getElementById('c14s7Svg');
    if(svg) svg.innerHTML = `
      <polygon points="40,100 ${px},100 130,20" fill="#06b6d4" fill-opacity="0.32" stroke="#22d3ee"/>
      <polygon points="${px},100 280,100 130,20" fill="#f59e0b" fill-opacity="0.28" stroke="#fbbf24"/>
      <line x1="130" y1="20" x2="130" y2="100" stroke="#94a3b8" stroke-dasharray="3 3"/>
      <circle cx="${px}" cy="100" r="4.5" fill="#34d399"/>
      <text x="130" y="14" text-anchor="middle" fill="#cbd5e1" font-size="10">Shared Height h</text>`;
    const a1 = (84 * bp / 12).toFixed(0), a2 = (84 * pc / 12).toFixed(0);
    document.getElementById('c14s7Out').innerHTML = `Left ΔABP = <b class="text-cyan-300">${a1} cm²</b> &nbsp;|&nbsp; Right ΔAPC = <b class="text-amber-300">${a2} cm²</b> → ${isMed?'<b class="text-emerald-300">EXACT 50% / 50% EQUAL AREAS AT MEDIAN!</b>':'Slide P to 6 cm to verify equal median halves!'}`;
  };
  window.c14s7Draw();
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🪞</span> Parallel-Track Triangles & Reflection Min-Perimeter
  </h3>
  <div class="space-y-2 text-xs">
    <div class="flex justify-between text-slate-300"><span>Slide Apex P along Parallel Mirror Line m (A=0, B=10, h=6):</span><b id="c14s8Val" class="text-cyan-300">x = 5.0 (MIN!)</b></div>
    <input id="c14s8Sl" type="range" min="-2" max="12" step="0.5" value="5" oninput="c14s8Draw()" class="w-full accent-amber-400">
    <svg id="c14s8Svg" viewBox="0 0 320 135" class="w-full h-32 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c14s8Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-300"></div>
  </div>
</div>
<script>
(function(){
  window.c14s8Draw = function(){
    const x = parseFloat(document.getElementById('c14s8Sl').value);
    const toPx = u => 70 + u * 18;
    const ax = toPx(0), bx = toPx(10), px = toPx(x);
    const ap = Math.hypot(x, 6), pb = Math.hypot(10-x, 6);
    const perim = 10 + ap + pb;
    const isMin = Math.abs(x - 5) < 0.01;
    document.getElementById('c14s8Val').textContent = isMin ? 'x = 5.0 (SHORTEST STRAIGHT AB′ PATH!)' : `x = ${x.toFixed(1)}`;
    const svg = document.getElementById('c14s8Svg');
    if(svg) svg.innerHTML = `
      <line x1="20" y1="62" x2="300" y2="62" stroke="#64748b" stroke-dasharray="4 3"/>
      <line x1="20" y1="112" x2="300" y2="112" stroke="#64748b"/>
      <line x1="${ax}" y1="112" x2="${bx}" y2="12" stroke="#f43f5e" stroke-dasharray="3 3"/>
      <polygon points="${ax},112 ${bx},112 ${px},62" fill="#22d3ee" fill-opacity="0.28" stroke="#22d3ee" stroke-width="2"/>
      <line x1="${px}" y1="62" x2="${bx}" y2="12" stroke="#fbbf24" stroke-dasharray="3 3"/>
      <circle cx="${bx}" cy="12" r="3.5" fill="#fb7185"/><text x="${bx+8}" y="16" fill="#fda4af" font-size="9">B′ Mirror</text>
      <circle cx="${px}" cy="62" r="4" fill="#fbbf24"/><text x="${px}" y="54" text-anchor="middle" fill="#fde68a" font-size="9">P</text>`;
    document.getElementById('c14s8Out').innerHTML = `Area = <b class="text-emerald-300">30.0 sq units (CONSTANT!)</b> &nbsp;|&nbsp; Perimeter = <b class="${isMin?'text-emerald-300':'text-amber-300'}">${perim.toFixed(2)} units</b> ${isMin?'★ MINIMUM AT SYMMETRIC x=5!':'(Slide to x=5 for straight AB′ minimum!)'}`;
  };
  window.c14s8Draw();
})();
</script>
"""
}
