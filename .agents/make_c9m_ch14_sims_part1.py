#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 14: Math of Space: Surface Area and Volume
Part 1: Simulators 1 to 8 (Slides 1 to 8)
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📦</span> Cuboid TSA &amp; Card-Stack Volume Explorer
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Length l:</span><span id="c9c14s1LL" class="text-cyan-300 font-bold">5</span></div>
      <input id="c9c14s1L" type="range" min="2" max="10" value="5" oninput="c9c14s1Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Width w:</span><span id="c9c14s1WL" class="text-emerald-300 font-bold">4</span></div>
      <input id="c9c14s1W" type="range" min="2" max="10" value="4" oninput="c9c14s1Draw()" class="w-full accent-emerald-400">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Height h:</span><span id="c9c14s1HL" class="text-amber-300 font-bold">3</span></div>
      <input id="c9c14s1H" type="range" min="2" max="10" value="3" oninput="c9c14s1Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9c14s1Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 grid grid-cols-2 gap-2"></div>
</div>
<script>
(function(){
  window.c9c14s1Draw = function(){
    const l = parseInt(document.getElementById('c9c14s1L').value, 10);
    const w = parseInt(document.getElementById('c9c14s1W').value, 10);
    const h = parseInt(document.getElementById('c9c14s1H').value, 10);
    document.getElementById('c9c14s1LL').textContent = l + ' cm';
    document.getElementById('c9c14s1WL').textContent = w + ' cm';
    document.getElementById('c9c14s1HL').textContent = h + ' cm';
    const tsa = 2*(w*l + h*l + h*w);
    const vol = l*w*h;
    document.getElementById('c9c14s1Out').innerHTML = `
      <div class="p-2.5 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">TSA = 2(wl + hl + hw)</div><div class="text-lg font-bold text-cyan-300">${tsa} cm²</div></div>
      <div class="p-2.5 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Volume = l × w × h</div><div class="text-lg font-bold text-amber-300">${vol} cm³</div></div>`;
  };
  c9c14s1Draw();
})();
</script>""",

    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧊</span> Cube Special Case &amp; Cube Numbers
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Cube Edge Side a:</span>
      <span id="c9c14s2AL" class="text-amber-300 font-bold">a = 3 cm</span>
    </div>
    <input id="c9c14s2A" type="range" min="1" max="6" value="3" oninput="c9c14s2Draw()" class="w-full accent-amber-400">
  </label>
  <div id="c9c14s2Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c14s2Draw = function(){
    const a = parseInt(document.getElementById('c9c14s2A').value, 10);
    document.getElementById('c9c14s2AL').textContent = 'a = ' + a + ' cm';
    document.getElementById('c9c14s2Out').innerHTML = `
      <div class="grid grid-cols-3 gap-2">
        <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Closed TSA (6a²)</div><div class="font-bold text-cyan-300">${6*a*a} cm²</div></div>
        <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Open TSA (5a²)</div><div class="font-bold text-emerald-300">${5*a*a} cm²</div></div>
        <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Volume (a³)</div><div class="font-bold text-amber-300">${a*a*a} cm³</div></div>
      </div>
      <div class="text-slate-400">Cube Numbers: <span class="text-amber-300 font-bold">1, 8, 27, 64, 125, 216</span></div>`;
  };
  c9c14s2Draw();
})();
</script>""",

    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🩻</span> Cylinder Types &amp; MRI Cross-Section Slicer
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button onclick="c9c14s3Set('right')" class="px-2.5 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold">Right Cylinder (90°)</button>
    <button onclick="c9c14s3Set('oblique')" class="px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Oblique Cylinder</button>
    <button onclick="c9c14s3Set('horiz')" class="px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Horizontal Slice (Circle)</button>
    <button onclick="c9c14s3Set('vert')" class="px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Vertical Slice (Rectangle)</button>
  </div>
  <svg id="c9c14s3Svg" viewBox="0 0 360 180" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  window.c9c14s3Set = function(m){
    const svg = document.getElementById('c9c14s3Svg');
    if (m === 'right') {
      svg.innerHTML = `<ellipse cx="180" cy="45" rx="55" ry="14" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2.5"/><line x1="125" y1="45" x2="125" y2="135" stroke="#38bdf8" stroke-width="2.5"/><line x1="235" y1="45" x2="235" y2="135" stroke="#38bdf8" stroke-width="2.5"/><ellipse cx="180" cy="135" rx="55" ry="14" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2.5"/><line x1="180" y1="45" x2="180" y2="135" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3"/><text x="180" y="170" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Central axis is perpendicular (90°) to circular bases</text>`;
    } else if (m === 'oblique') {
      svg.innerHTML = `<ellipse cx="215" cy="45" rx="55" ry="14" fill="rgba(244,63,94,0.2)" stroke="#fb7185" stroke-width="2.5"/><line x1="160" y1="45" x2="100" y2="135" stroke="#fb7185" stroke-width="2.5"/><line x1="270" y1="45" x2="210" y2="135" stroke="#fb7185" stroke-width="2.5"/><ellipse cx="155" cy="135" rx="55" ry="14" fill="rgba(244,63,94,0.2)" stroke="#fb7185" stroke-width="2.5"/><line x1="215" y1="45" x2="155" y2="135" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,3"/><text x="180" y="170" text-anchor="middle" fill="#fb7185" font-size="11" font-weight="bold">Oblique Cylinder: slanted axis (not 90° to bases)</text>`;
    } else if (m === 'horiz') {
      svg.innerHTML = `<ellipse cx="130" cy="90" rx="50" ry="13" fill="rgba(16,185,129,0.35)" stroke="#34d399" stroke-width="2.5"/><circle cx="265" cy="90" r="42" fill="rgba(16,185,129,0.25)" stroke="#34d399" stroke-width="3"/><text x="180" y="170" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Slice parallel to base ⇒ Circular Cross-Section (MRI Slice)</text>`;
    } else {
      svg.innerHTML = `<rect x="135" y="40" width="90" height="100" fill="rgba(245,158,11,0.25)" stroke="#fbbf24" stroke-width="3"/><text x="180" y="170" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">Slice parallel to axis ⇒ Rectangular Cross-Section (2r × h)</text>`;
    }
  };
  c9c14s3Set('right');
})();
</script>""",

    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🥫</span> Cylinder Area &amp; Khakhra-Stack Volume Calculator
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Radius r (cm):</span><span id="c9c14s4RL" class="text-cyan-300 font-bold">7</span></div>
      <input id="c9c14s4R" type="range" min="3.5" max="14" step="3.5" value="7" oninput="c9c14s4Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Height h (cm):</span><span id="c9c14s4HL" class="text-amber-300 font-bold">10</span></div>
      <input id="c9c14s4H" type="range" min="4" max="20" step="2" value="10" oninput="c9c14s4Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9c14s4Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 grid grid-cols-2 gap-2"></div>
</div>
<script>
(function(){
  window.c9c14s4Draw = function(){
    const r = parseFloat(document.getElementById('c9c14s4R').value);
    const h = parseFloat(document.getElementById('c9c14s4H').value);
    document.getElementById('c9c14s4RL').textContent = r + ' cm';
    document.getElementById('c9c14s4HL').textContent = h + ' cm';
    const pi = 22/7;
    const csa = (2*pi*r*h).toFixed(1);
    const tsa = (2*pi*r*(h+r)).toFixed(1);
    const openTsa = (pi*r*(2*h+r)).toFixed(1);
    const vol = (pi*r*r*h).toFixed(1);
    document.getElementById('c9c14s4Out').innerHTML = `
      <div class="p-2 rounded bg-slate-900 border border-slate-800">CSA (2πrh): <span class="text-cyan-300 font-bold">${csa} cm²</span></div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800">Closed TSA: <span class="text-emerald-300 font-bold">${tsa} cm²</span></div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800">Open-Top TSA: <span class="text-amber-300 font-bold">${openTsa} cm²</span></div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800">Volume (πr²h): <span class="text-rose-300 font-bold">${vol} cm³</span></div>`;
  };
  c9c14s4Draw();
})();
</script>""",

    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📐</span> Cone Slant Height Lab: l² = h² + r²
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Radius r:</span><span id="c9c14s5RL" class="text-cyan-300 font-bold">6 cm</span></div>
      <input id="c9c14s5R" type="range" min="3" max="12" value="6" oninput="c9c14s5Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Height h:</span><span id="c9c14s5HL" class="text-amber-300 font-bold">8 cm</span></div>
      <input id="c9c14s5H" type="range" min="4" max="16" value="8" oninput="c9c14s5Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <svg id="c9c14s5Svg" viewBox="0 0 360 180" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  window.c9c14s5Draw = function(){
    const r = parseFloat(document.getElementById('c9c14s5R').value);
    const h = parseFloat(document.getElementById('c9c14s5H').value);
    document.getElementById('c9c14s5RL').textContent = r + ' cm';
    document.getElementById('c9c14s5HL').textContent = h + ' cm';
    const l = Math.sqrt(h*h + r*r).toFixed(2);
    const rx = r * 7, hy = h * 6.5, cy = 140, ay = cy - hy;
    document.getElementById('c9c14s5Svg').innerHTML = `
      <ellipse cx="180" cy="${cy}" rx="${rx}" ry="12" fill="rgba(56,189,248,0.18)" stroke="#38bdf8" stroke-width="2"/>
      <line x1="${180-rx}" y1="${cy}" x2="180" y2="${ay}" stroke="#38bdf8" stroke-width="2.5"/>
      <line x1="${180+rx}" y1="${cy}" x2="180" y2="${ay}" stroke="#fbbf24" stroke-width="3"/>
      <line x1="180" y1="${cy}" x2="180" y2="${ay}" stroke="#34d399" stroke-width="2" stroke-dasharray="4,3"/>
      <line x1="180" y1="${cy}" x2="${180+rx}" y2="${cy}" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
      <text x="180" y="172" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">l = √(${h}² + ${r}²) = ${l} cm</text>`;
  };
  c9c14s5Draw();
})();
</script>""",

    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⏳</span> 3:1 Cone-to-Cylinder Salt Pouring Experiment
  </h3>
  <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block text-xs">
    <div class="flex justify-between font-semibold text-slate-300 mb-1">
      <span>Cones Poured into Equal Cylinder:</span>
      <span id="c9c14s6Lbl" class="text-amber-300 font-bold">1 / 3 Full (33.3%)</span>
    </div>
    <input id="c9c14s6P" type="range" min="0" max="3" value="1" oninput="c9c14s6Draw()" class="w-full accent-amber-400">
  </label>
  <svg id="c9c14s6Svg" viewBox="0 0 360 180" class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800"></svg>
</div>
<script>
(function(){
  window.c9c14s6Draw = function(){
    const p = parseInt(document.getElementById('c9c14s6P').value, 10);
    document.getElementById('c9c14s6Lbl').textContent = p + ' / 3 Full (' + Math.round(p*100/3) + '%)';
    const fillH = p * 32, topY = 140 - fillH;
    document.getElementById('c9c14s6Svg').innerHTML = `
      <polygon points="65,140 125,140 95,44" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="95" y="160" text-anchor="middle" fill="#cbd5e1" font-size="11">Cone (⅓πr²h)</text>
      <rect x="200" y="44" width="80" height="96" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      ${p>0 ? `<rect x="201" y="${topY}" width="78" height="${fillH}" fill="rgba(245,158,11,0.45)"/>` : ''}
      <text x="240" y="160" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">Cylinder: ${p}/3 Filled</text>`;
  };
  c9c14s6Draw();
})();
</script>""",

    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔺</span> Pyramidal Shapes Explorer
  </h3>
  <div class="flex flex-wrap gap-2 text-xs">
    <button onclick="c9c14s7Set(0)" class="px-3 py-1.5 rounded-lg bg-cyan-600 text-white font-semibold">Triangular Pyramid (Tetrahedron)</button>
    <button onclick="c9c14s7Set(1)" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Square Pyramid (Egypt / Shivling)</button>
    <button onclick="c9c14s7Set(2)" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-semibold">Pentagonal Pyramid</button>
  </div>
  <div id="c9c14s7Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  const shapes = [
    { name:'Triangular Pyramid (Tetrahedron)', faces:'4 (1 triangle base + 3 triangular walls)', edges:'6', vert:'4', ex:'Erno Rubik Pyraminx puzzle' },
    { name:'Square Pyramid', faces:'5 (1 square base + 4 triangular walls)', edges:'8', vert:'5', ex:'Great Pyramids of Egypt, Shivling Peak (Uttarakhand), Matterhorn (Alps)' },
    { name:'Pentagonal Pyramid', faces:'6 (1 pentagon base + 5 triangular walls)', edges:'10', vert:'6', ex:'Architectural domes & crystals' }
  ];
  window.c9c14s7Set = function(i){
    const d = shapes[i];
    document.getElementById('c9c14s7Out').innerHTML = `
      <div class="text-amber-300 font-bold text-sm">${d.name}</div>
      <div><span class="text-slate-400">Faces:</span> <span class="text-cyan-300 font-semibold">${d.faces}</span></div>
      <div><span class="text-slate-400">Edges / Vertices:</span> ${d.edges} edges, ${d.vert} vertices</div>
      <div><span class="text-slate-400">Real-World Example:</span> <span class="text-emerald-300">${d.ex}</span></div>`;
  };
  c9c14s7Set(0);
})();
</script>""",

    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏛️</span> Universal Pyramid Volume: V = ⅓ × Base Area × h
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Base Area B (cm²):</span><span id="c9c14s8BL" class="text-cyan-300 font-bold">36</span></div>
      <input id="c9c14s8B" type="range" min="12" max="90" step="6" value="36" oninput="c9c14s8Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Height h (cm):</span><span id="c9c14s8HL" class="text-amber-300 font-bold">10</span></div>
      <input id="c9c14s8H" type="range" min="3" max="18" step="3" value="10" oninput="c9c14s8Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9c14s8Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c9c14s8Draw = function(){
    const B = parseInt(document.getElementById('c9c14s8B').value, 10);
    const h = parseInt(document.getElementById('c9c14s8H').value, 10);
    document.getElementById('c9c14s8BL').textContent = B + ' cm²';
    document.getElementById('c9c14s8HL').textContent = h + ' cm';
    const v = (B*h/3).toFixed(1);
    document.getElementById('c9c14s8Out').innerHTML =
      'Universal Formula: <span class="text-cyan-300 font-bold">V = ⅓ × ' + B + ' × ' + h + ' = ' + v + ' cm³</span>. For a circular base B = πr², this becomes V = ⅓πr²h (a cone)!';
  };
  c9c14s8Draw();
})();
</script>""",
}
