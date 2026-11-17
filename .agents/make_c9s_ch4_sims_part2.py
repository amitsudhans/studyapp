#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sims_part2 = {
    9: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">v-t Graph: Slope = a & Area = s</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Final v: <b id="sim9_v" class="text-amber-300">20 m/s</b></label>
      <input type="range" min="10" max="30" step="5" value="20" oninput="updSim9(this.value)" class="w-36 accent-cyan-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="80" y1="200" x2="540" y2="200" stroke="#94a3b8" stroke-width="2"/>
    <line x1="80" y1="200" x2="80" y2="30" stroke="#94a3b8" stroke-width="2"/>
    <polygon id="sim9_area" points="80,200 80,150 480,100 480,200" fill="#06b6d4" fill-opacity="0.25" stroke="#22d3ee" stroke-width="1"/>
    <line id="sim9_line" x1="80" y1="150" x2="480" y2="100" stroke="#fbbf24" stroke-width="3.5"/>
    <text x="55" y="154" fill="#cbd5e1" font-size="11">10</text>
    <text x="480" y="218" text-anchor="middle" fill="#cbd5e1" font-size="11">t = 10 s</text>
    <text id="sim9_res" x="300" y="38" text-anchor="middle" fill="#67e8f9" font-size="13" font-weight="bold">Slope a = +1.0 m/s² | Area s = 150 m</text>
  </svg>
</div>
<script>
window.updSim9 = function(v){
  v = parseInt(v,10);
  document.getElementById('sim9_v').textContent = v + ' m/s';
  const yEnd = 200 - v*5;
  document.getElementById('sim9_line').setAttribute('y2', yEnd);
  document.getElementById('sim9_area').setAttribute('points', '80,200 80,150 480,'+yEnd+' 480,200');
  const a = ((v-10)/10).toFixed(1);
  const s = ((10+v)/2)*10;
  document.getElementById('sim9_res').textContent = 'Slope a = +' + a + ' m/s² | Area s = ' + s + ' m';
};
</script>""",

    10: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">First Equation: v = u + at</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Time t: <b id="sim10_t" class="text-cyan-300">4 s</b></label>
      <input type="range" min="1" max="8" value="4" oninput="updSim10(this.value)" class="w-36 accent-amber-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="80" y1="200" x2="540" y2="200" stroke="#94a3b8" stroke-width="2"/>
    <line x1="80" y1="200" x2="80" y2="30" stroke="#94a3b8" stroke-width="2"/>
    <line x1="80" y1="160" x2="480" y2="160" stroke="#475569" stroke-dasharray="4,4"/>
    <line id="sim10_line" x1="80" y1="160" x2="280" y2="112" stroke="#34d399" stroke-width="3.5"/>
    <text x="52" y="164" fill="#cbd5e1" font-size="11">u=5</text>
    <text id="sim10_eq" x="300" y="42" text-anchor="middle" fill="#6ee7b7" font-size="15" font-weight="bold">v = 5 + (3 × 4) = 17 m/s (a = 3 m/s²)</text>
    <text x="300" y="226" text-anchor="middle" fill="#94a3b8" font-size="12">Rise (v - u) = a × t added on top of initial velocity u</text>
  </svg>
</div>
<script>
window.updSim10 = function(t){
  t = parseInt(t,10);
  document.getElementById('sim10_t').textContent = t + ' s';
  const v = 5 + 3*t;
  const x = 80 + t*50;
  const y = 160 - (3*t)*4;
  const line = document.getElementById('sim10_line');
  line.setAttribute('x2', x);
  line.setAttribute('y2', y);
  document.getElementById('sim10_eq').textContent = 'v = 5 + (3 × '+t+') = '+v+' m/s (a = 3 m/s²)';
};
</script>""",

    11: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Area Split: s = ut + ½at²</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">t: <b id="sim11_t" class="text-amber-300">5 s</b></label>
      <input type="range" min="1" max="8" value="5" oninput="updSim11(this.value)" class="w-36 accent-cyan-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="80" y1="200" x2="540" y2="200" stroke="#94a3b8" stroke-width="2"/>
    <line x1="80" y1="200" x2="80" y2="30" stroke="#94a3b8" stroke-width="2"/>
    <rect id="sim11_rect" x="80" y="150" width="250" height="50" fill="#06b6d4" fill-opacity="0.3" stroke="#22d3ee"/>
    <polygon id="sim11_tri" points="80,150 330,150 330,100" fill="#f59e0b" fill-opacity="0.35" stroke="#fbbf24"/>
    <text id="sim11_rtxt" x="205" y="180" text-anchor="middle" fill="#67e8f9" font-size="12" font-weight="bold">ut = 50 m</text>
    <text id="sim11_ttxt" x="260" y="138" text-anchor="middle" fill="#fde68a" font-size="12" font-weight="bold">½at² = 25 m</text>
    <text id="sim11_tot" x="300" y="38" text-anchor="middle" fill="#34d399" font-size="14" font-weight="bold">Total s = 50 + 25 = 75 m (u=10, a=2)</text>
  </svg>
</div>
<script>
window.updSim11 = function(t){
  t = parseInt(t,10);
  document.getElementById('sim11_t').textContent = t + ' s';
  const w = t*50;
  const hTri = t*10;
  document.getElementById('sim11_rect').setAttribute('width', w);
  document.getElementById('sim11_tri').setAttribute('points', '80,150 '+(80+w)+',150 '+(80+w)+','+(150-hTri));
  const ut = 10*t, halfAt2 = t*t;
  document.getElementById('sim11_rtxt').setAttribute('x', 80 + w/2);
  document.getElementById('sim11_rtxt').textContent = 'ut = '+ut+' m';
  document.getElementById('sim11_ttxt').setAttribute('x', 80 + w*0.68);
  document.getElementById('sim11_ttxt').textContent = '½at² = '+halfAt2+' m';
  document.getElementById('sim11_tot').textContent = 'Total s = '+ut+' + '+halfAt2+' = '+(ut+halfAt2)+' m (u=10, a=2)';
};
</script>""",

    12: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-rose-300 uppercase">Example 4.8: Speed vs Stopping Distance</span>
    <div class="flex gap-1.5">
      <button onclick="setCar12(54,15,28.1)" class="px-2.5 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">54 km/h (15 m/s)</button>
      <button onclick="setCar12(108,30,112.5)" class="px-2.5 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">108 km/h (30 m/s)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="50" y="130" width="500" height="40" rx="6" fill="#1e293b"/>
    <line x1="70" y1="150" x2="530" y2="150" stroke="#94a3b8" stroke-dasharray="12,10" stroke-width="2"/>
    <rect id="sim12_bar" x="70" y="114" width="110" height="12" rx="4" fill="#34d399"/>
    <rect x="65" y="138" width="38" height="22" rx="5" fill="#38bdf8" stroke="#bae6fd" stroke-width="1.5"/>
    <text id="sim12_txt" x="300" y="55" text-anchor="middle" fill="#6ee7b7" font-size="16" font-weight="bold">54 km/h (15 m/s) ⇒ Stopping Distance s = 28.1 m</text>
    <text x="300" y="85" text-anchor="middle" fill="#cbd5e1" font-size="12">Braking Deceleration a = -4 m/s² | V2V Alerts Cut Reaction Delay</text>
  </svg>
</div>
<script>
window.setCar12 = function(kmh, ms, s){
  const bar = document.getElementById('sim12_bar');
  const txt = document.getElementById('sim12_txt');
  bar.setAttribute('width', kmh===54 ? 110 : 440);
  bar.setAttribute('fill', kmh===54 ? '#34d399' : '#f43f5e');
  txt.setAttribute('fill', kmh===54 ? '#6ee7b7' : '#fda4af');
  txt.textContent = kmh+' km/h ('+ms+' m/s) ⇒ Stopping Distance s = '+s+' m ('+(kmh===108?'4× Longer!':'1× Base')+')';
};
</script>""",

    13: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">1D vs 2D Plane vs 3D Space</span>
    <div class="flex gap-1.5">
      <button onclick="setDim13('1d')" class="px-2.5 py-1 rounded bg-slate-700 text-xs text-white">1D Line</button>
      <button onclick="setDim13('2d')" class="px-2.5 py-1 rounded bg-cyan-600/40 text-xs text-cyan-200">2D Projectile</button>
      <button onclick="setDim13('3d')" class="px-2.5 py-1 rounded bg-amber-600/40 text-xs text-amber-200">3D Aircraft</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="sim13_1d" style="display:none">
      <line x1="80" y1="130" x2="520" y2="130" stroke="#38bdf8" stroke-width="3"/>
      <circle cx="300" cy="130" r="12" fill="#38bdf8"/>
      <text x="300" y="65" text-anchor="middle" fill="#7dd3fc" font-size="15" font-weight="bold">1D Motion: Single Straight Axis (X only)</text>
    </g>
    <g id="sim13_2d">
      <line x1="80" y1="195" x2="520" y2="195" stroke="#475569" stroke-width="2"/>
      <line x1="80" y1="195" x2="80" y2="45" stroke="#475569" stroke-width="2"/>
      <path d="M 90 190 Q 300 35 500 190" fill="none" stroke="#34d399" stroke-width="3" stroke-dasharray="6,5"/>
      <circle cx="300" cy="112" r="11" fill="#10b981" stroke="#a7f3d0" stroke-width="2"/>
      <text x="300" y="38" text-anchor="middle" fill="#6ee7b7" font-size="15" font-weight="bold">2D Motion in a Plane: Horizontal X + Vertical Y</text>
    </g>
    <g id="sim13_3d" style="display:none">
      <line x1="160" y1="185" x2="480" y2="185" stroke="#64748b" stroke-width="2"/>
      <line x1="160" y1="185" x2="160" y2="45" stroke="#64748b" stroke-width="2"/>
      <line x1="160" y1="185" x2="80" y2="225" stroke="#64748b" stroke-width="2"/>
      <path d="M 140 195 C 220 150, 320 90, 440 70" fill="none" stroke="#fbbf24" stroke-width="3"/>
      <polygon points="440,70 422,64 426,80" fill="#f59e0b"/>
      <text x="320" y="38" text-anchor="middle" fill="#fcd34d" font-size="15" font-weight="bold">3D Space Motion: X, Y & Altitude Z</text>
    </g>
  </svg>
</div>
<script>
window.setDim13 = function(d){
  ['1d','2d','3d'].forEach(k=>{
    document.getElementById('sim13_'+k).style.display=(k===d?'block':'none');
  });
};
</script>""",

    14: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Activity 4.5: Uniform Circular Motion & Tangent</span>
    <button onclick="releaseMarble14()" class="px-3 py-1 rounded-lg bg-amber-500/30 text-amber-200 border border-amber-400/50 text-xs font-bold hover:bg-amber-500/50">Lift Ring / Reset</button>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <circle id="sim14_ring" cx="240" cy="125" r="72" fill="none" stroke="#38bdf8" stroke-width="4" stroke-dasharray="8,4"/>
    <circle cx="240" cy="125" r="4" fill="#94a3b8"/>
    <line id="sim14_tan" x1="240" y1="53" x2="430" y2="53" stroke="#fbbf24" stroke-width="2" stroke-dasharray="5,4"/>
    <circle id="sim14_m" cx="240" cy="53" r="10" fill="#f97316" stroke="#fed7aa" stroke-width="2"/>
    <text x="455" y="105" text-anchor="middle" fill="#67e8f9" font-size="13" font-weight="bold">v_av = 2πR / T</text>
    <text x="455" y="130" text-anchor="middle" fill="#fde68a" font-size="12">Tangent velocity direction</text>
    <text x="455" y="150" text-anchor="middle" fill="#fde68a" font-size="12">changes continuously!</text>
  </svg>
</div>
<script>
(function(){
  let ang=0, released=false, tx=240, ty=53;
  window.releaseMarble14 = function(){
    if(!released){ released=true; tx=240+72*Math.cos(ang); ty=125+72*Math.sin(ang); }
    else { released=false; }
    document.getElementById('sim14_ring').setAttribute('stroke-opacity', released?'0.25':'1');
  };
  setInterval(function(){
    const m=document.getElementById('sim14_m'), tan=document.getElementById('sim14_tan');
    if(!m || !tan) return;
    if(!released){
      ang+=0.05;
      const x=240+72*Math.cos(ang), y=125+72*Math.sin(ang);
      m.setAttribute('cx',x); m.setAttribute('cy',y);
      const dx=-Math.sin(ang)*65, dy=Math.cos(ang)*65;
      tan.setAttribute('x1',x); tan.setAttribute('y1',y);
      tan.setAttribute('x2',x+dx); tan.setAttribute('y2',y+dy);
    } else {
      tx += -Math.sin(ang)*3.5; ty += Math.cos(ang)*3.5;
      if(tx>580||tx<20||ty>230||ty<10){ released=false; document.getElementById('sim14_ring').setAttribute('stroke-opacity','1'); }
      m.setAttribute('cx',tx); m.setAttribute('cy',ty);
    }
  }, 30);
})();
</script>""",

    15: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Phyphox Elevator Accelerometer Lab</span>
    <div class="flex gap-1.5">
      <button onclick="setElev15('start')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200">1. Start Up (+a)</button>
      <button onclick="setElev15('cruise')" class="px-2 py-1 rounded bg-slate-700 text-xs text-slate-200">2. Cruise (a=0)</button>
      <button onclick="setElev15('stop')" class="px-2 py-1 rounded bg-rose-600/30 text-xs text-rose-200">3. Slow/Stop (-a)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="70" y1="125" x2="540" y2="125" stroke="#475569" stroke-width="2" stroke-dasharray="4,4"/>
    <line x1="70" y1="40" x2="70" y2="210" stroke="#94a3b8" stroke-width="2"/>
    <path d="M 70 125 L 130 60 L 190 125 L 380 125 L 440 190 L 500 125" fill="none" stroke="#38bdf8" stroke-width="3.5"/>
    <circle id="sim15_dot" cx="130" cy="60" r="9" fill="#34d399" stroke="#ecfdf5" stroke-width="2"/>
    <text id="sim15_lbl" x="300" y="34" text-anchor="middle" fill="#6ee7b7" font-size="14" font-weight="bold">Starting Upward: Positive Acceleration Peak (+a)</text>
    <text x="300" y="226" text-anchor="middle" fill="#94a3b8" font-size="12">Alternate forms: s = vt - ½at²  |  s = [(u + v)/2] × t</text>
  </svg>
</div>
<script>
window.setElev15 = function(phase){
  const map = {
    start:  {x:130, y:60,  c:'#34d399', t:'Starting Upward: Positive Acceleration Peak (+a)'},
    cruise: {x:285, y:125, c:'#38bdf8', t:'Steady Cruise: Constant Velocity ⇒ Zero Acceleration (a = 0)'},
    stop:   {x:440, y:190, c:'#f43f5e', t:'Slowing to Floor: Negative Deceleration Dip (-a)'}
  }[phase];
  const d = document.getElementById('sim15_dot');
  d.setAttribute('cx', map.x); d.setAttribute('cy', map.y); d.setAttribute('fill', map.c);
  document.getElementById('sim15_lbl').textContent = map.t;
};
</script>""",

    16: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Chapter 4 At a Glance: Kinematics Map</span>
    <span class="text-xs text-slate-400">All Core Equations</span>
  </div>
  <svg viewBox="0 0 600 245" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="25" y="20" width="175" height="92" rx="10" fill="#0f172a" stroke="#06b6d4"/>
    <text x="112" y="44" text-anchor="middle" fill="#67e8f9" font-size="12" font-weight="bold">Scalars vs Vectors</text>
    <text x="112" y="66" text-anchor="middle" fill="#cbd5e1" font-size="11">Distance ≥ |Displacement|</text>
    <text x="112" y="86" text-anchor="middle" fill="#cbd5e1" font-size="11">Speed vs Velocity (m/s)</text>
    <text x="112" y="102" text-anchor="middle" fill="#94a3b8" font-size="10">a = (v - u)/t (m/s²)</text>

    <rect x="212" y="20" width="175" height="92" rx="10" fill="#0f172a" stroke="#10b981"/>
    <text x="300" y="44" text-anchor="middle" fill="#6ee7b7" font-size="12" font-weight="bold">Motion Graphs</text>
    <text x="300" y="66" text-anchor="middle" fill="#cbd5e1" font-size="11">s-t slope = velocity</text>
    <text x="300" y="86" text-anchor="middle" fill="#cbd5e1" font-size="11">v-t slope = acceleration</text>
    <text x="300" y="102" text-anchor="middle" fill="#94a3b8" font-size="10">v-t area = displacement</text>

    <rect x="400" y="20" width="175" height="92" rx="10" fill="#0f172a" stroke="#f59e0b"/>
    <text x="487" y="44" text-anchor="middle" fill="#fcd34d" font-size="12" font-weight="bold">Uniform Circular</text>
    <text x="487" y="66" text-anchor="middle" fill="#cbd5e1" font-size="11">v_av = 2πR / T</text>
    <text x="487" y="86" text-anchor="middle" fill="#cbd5e1" font-size="11">1 lap disp = 0 m</text>
    <text x="487" y="102" text-anchor="middle" fill="#94a3b8" font-size="10">Tangent velocity turns</text>

    <rect x="55" y="132" width="490" height="92" rx="12" fill="#1e293b" stroke="#38bdf8"/>
    <text x="300" y="156" text-anchor="middle" fill="#7dd3fc" font-size="13" font-weight="bold">Three Constant-Acceleration Kinematic Equations</text>
    <text x="300" y="182" text-anchor="middle" fill="#ffffff" font-size="15" font-weight="bold">v = u + at   |   s = ut + ½at²   |   v² = u² + 2as</text>
    <text x="300" y="208" text-anchor="middle" fill="#cbd5e1" font-size="11">Ready for the 4 Silent Mastery Quizzes (Slides 17–20)!</text>
  </svg>
</div>"""
}
