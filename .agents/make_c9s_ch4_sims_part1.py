#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sims_part1 = {
    1: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase tracking-wider">Idealized Motion Explorer</span>
    <div class="flex gap-1.5">
      <button onclick="setMotMode1('linear')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-cyan-600/30 text-cyan-200 border border-cyan-500/40 hover:bg-cyan-600/50">Linear</button>
      <button onclick="setMotMode1('circular')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-emerald-600/30 text-emerald-200 border border-emerald-500/40 hover:bg-emerald-600/50">Circular</button>
      <button onclick="setMotMode1('oscillatory')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-600/30 text-amber-200 border border-amber-500/40 hover:bg-amber-600/50">Oscillatory</button>
    </div>
  </div>
  <svg viewBox="0 0 600 260" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <defs>
      <radialGradient id="g1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.35"/>
        <stop offset="100%" stop-color="#0f172a" stop-opacity="0"/>
      </radialGradient>
    </defs>
    <rect x="0" y="0" width="600" height="260" fill="url(#g1)"/>
    <g id="sim1_linear">
      <line x1="60" y1="130" x2="540" y2="130" stroke="#334155" stroke-width="4" stroke-dasharray="8,6"/>
      <circle cx="60" cy="130" r="5" fill="#94a3b8"/>
      <circle cx="540" cy="130" r="5" fill="#94a3b8"/>
      <g id="sim1_train">
        <rect x="60" y="106" width="54" height="24" rx="6" fill="#06b6d4" stroke="#67e8f9" stroke-width="2"/>
        <circle cx="74" cy="132" r="5" fill="#e2e8f0"/><circle cx="100" cy="132" r="5" fill="#e2e8f0"/>
      </g>
      <text x="300" y="55" text-anchor="middle" fill="#67e8f9" font-size="15" font-weight="bold">Linear Motion: Straight-Line Path</text>
      <text x="300" y="195" text-anchor="middle" fill="#94a3b8" font-size="12">Idealized train / falling ball / straight-lane swimmer</text>
    </g>
    <g id="sim1_circular" style="display:none">
      <circle cx="300" cy="130" r="70" fill="none" stroke="#10b981" stroke-width="2.5" stroke-dasharray="6,5"/>
      <circle cx="300" cy="130" r="5" fill="#34d399"/>
      <line id="sim1_rad" x1="300" y1="130" x2="370" y2="130" stroke="#34d399" stroke-width="1.5"/>
      <circle id="sim1_orb" cx="370" cy="130" r="10" fill="#10b981" stroke="#a7f3d0" stroke-width="2"/>
      <text x="300" y="34" text-anchor="middle" fill="#6ee7b7" font-size="15" font-weight="bold">Circular Motion: Fixed Radius R</text>
      <text x="300" y="232" text-anchor="middle" fill="#94a3b8" font-size="12">Constant distance from centre; direction turns continuously</text>
    </g>
    <g id="sim1_oscillatory" style="display:none">
      <line x1="220" y1="36" x2="380" y2="36" stroke="#64748b" stroke-width="4"/>
      <line id="sim1_rod" x1="300" y1="36" x2="300" y2="176" stroke="#fbbf24" stroke-width="2.5"/>
      <circle id="sim1_bob" cx="300" cy="176" r="16" fill="#f59e0b" stroke="#fde68a" stroke-width="2"/>
      <text x="300" y="228" text-anchor="middle" fill="#fcd34d" font-size="14" font-weight="bold">Oscillatory Motion: To-and-Fro About Mean Position</text>
    </g>
  </svg>
  <div id="sim1_info" class="text-xs text-slate-300 bg-slate-900/70 rounded-lg px-3 py-1.5 border border-slate-800">
    Real-world motion (butterflies, ocean tides, horses) is simplified into <b>linear</b>, <b>circular</b>, and <b>oscillatory</b> models.
  </div>
</div>
<script>
(function(){
  let mode1='linear', t1=0;
  window.setMotMode1 = function(m){
    mode1=m;
    ['linear','circular','oscillatory'].forEach(k=>{
      const el=document.getElementById('sim1_'+k);
      if(el) el.style.display=(k===m?'block':'none');
    });
  };
  setInterval(function(){
    t1+=0.05;
    if(mode1==='linear'){
      const tr=document.getElementById('sim1_train');
      if(tr){
        const x = 210 * (0.5 - 0.5*Math.cos(t1));
        tr.setAttribute('transform', 'translate('+x+',0)');
      }
    } else if(mode1==='circular'){
      const orb=document.getElementById('sim1_orb'), rad=document.getElementById('sim1_rad');
      if(orb && rad){
        const x=300+70*Math.cos(t1*1.4), y=130+70*Math.sin(t1*1.4);
        orb.setAttribute('cx',x); orb.setAttribute('cy',y);
        rad.setAttribute('x2',x); rad.setAttribute('y2',y);
      }
    } else {
      const bob=document.getElementById('sim1_bob'), rod=document.getElementById('sim1_rod');
      if(bob && rod){
        const ang=0.55*Math.sin(t1*1.8);
        const x=300+140*Math.sin(ang), y=36+140*Math.cos(ang);
        bob.setAttribute('cx',x); bob.setAttribute('cy',y);
        rod.setAttribute('x2',x); rod.setAttribute('y2',y);
      }
    }
  }, 30);
})();
</script>""",

    2: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex flex-wrap items-center justify-between gap-2 bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Origin O & Sign Convention</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Position x: <b id="sim2_val" class="text-amber-300">+20 m</b></label>
      <input id="sim2_slider" type="range" min="-50" max="50" step="5" value="20" oninput="updSim2(this.value)" class="w-36 accent-cyan-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="40" y1="130" x2="560" y2="130" stroke="#475569" stroke-width="3"/>
    <line x1="300" y1="75" x2="300" y2="175" stroke="#f59e0b" stroke-width="3" stroke-dasharray="5,4"/>
    <circle cx="300" cy="130" r="6" fill="#f59e0b"/>
    <text x="300" y="65" text-anchor="middle" fill="#fbbf24" font-size="14" font-weight="bold">Origin O (0 m)</text>
    <text x="120" y="165" text-anchor="middle" fill="#f43f5e" font-size="13" font-weight="bold">Negative (-) Left</text>
    <text x="480" y="165" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">Positive (+) Right</text>
    <g fill="#94a3b8" font-size="11" text-anchor="middle">
      <text x="75" y="148">-50</text><text x="165" y="148">-30</text><text x="255" y="148">-10</text>
      <text x="345" y="148">+10</text><text x="435" y="148">+30</text><text x="525" y="148">+50</text>
    </g>
    <line id="sim2_vec" x1="300" y1="112" x2="390" y2="112" stroke="#38bdf8" stroke-width="4"/>
    <circle id="sim2_obj" cx="390" cy="112" r="12" fill="#06b6d4" stroke="#cffafe" stroke-width="2"/>
  </svg>
  <div id="sim2_msg" class="text-xs text-slate-300 bg-slate-900/70 rounded-lg px-3 py-1.5 border border-slate-800">
    Position = <b>+20 m</b> (20 m to the right of Reference Point O). Changing x over time = Motion!
  </div>
</div>
<script>
window.updSim2 = function(v){
  v = parseInt(v,10);
  const sign = v>0 ? '+' : '';
  document.getElementById('sim2_val').textContent = sign + v + ' m';
  const cx = 300 + v * 4.5;
  document.getElementById('sim2_obj').setAttribute('cx', cx);
  const vec = document.getElementById('sim2_vec');
  vec.setAttribute('x2', cx);
  vec.setAttribute('stroke', v>=0 ? '#34d399' : '#f43f5e');
  const dir = v===0 ? 'at Origin O' : (v>0 ? v+' m to the RIGHT (+) of O' : Math.abs(v)+' m to the LEFT (-) of O');
  document.getElementById('sim2_msg').innerHTML = 'Position = <b>'+sign+v+' m</b> ('+dir+').';
};
</script>""",

    3: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Activity 4.1: Vertical Ball Toss</span>
    <div class="flex gap-1.5">
      <button onclick="setBall3('O')" class="px-2 py-1 rounded bg-slate-700 text-xs text-white">Start O</button>
      <button onclick="setBall3('A')" class="px-2 py-1 rounded bg-cyan-600/40 text-xs text-cyan-200">Peak A (+10m)</button>
      <button onclick="setBall3('B')" class="px-2 py-1 rounded bg-amber-600/40 text-xs text-amber-200">Fall B (+6m)</button>
      <button onclick="setBall3('C')" class="px-2 py-1 rounded bg-rose-600/40 text-xs text-rose-200">Return C (0m)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="180" y1="205" x2="420" y2="205" stroke="#475569" stroke-width="3"/>
    <line x1="250" y1="35" x2="250" y2="205" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>
    <circle cx="250" cy="205" r="5" fill="#94a3b8"/><text x="225" y="209" fill="#cbd5e1" font-size="12">O (0 m)</text>
    <circle cx="250" cy="45" r="5" fill="#38bdf8"/><text x="190" y="49" fill="#7dd3fc" font-size="12">A (+10 m)</text>
    <circle cx="250" cy="109" r="5" fill="#fbbf24"/><text x="190" y="113" fill="#fde68a" font-size="12">B (+6 m)</text>
    <circle id="sim3_ball" cx="250" cy="45" r="12" fill="#f97316" stroke="#fed7aa" stroke-width="2"/>
    <rect x="330" y="45" width="230" height="135" rx="10" fill="#0f172a" stroke="#334155"/>
    <text x="345" y="72" fill="#94a3b8" font-size="12" font-weight="bold">ACTVITY 4.1 READOUT</text>
    <text id="sim3_dist" x="345" y="102" fill="#38bdf8" font-size="14" font-weight="bold">Distance: 10 m</text>
    <text id="sim3_disp" x="345" y="128" fill="#34d399" font-size="14" font-weight="bold">Displacement: +10 m</text>
    <text id="sim3_ineq" x="345" y="158" fill="#fbbf24" font-size="12">|Displacement| <= Distance</text>
  </svg>
</div>
<script>
window.setBall3 = function(pt){
  const map = {
    O: {y:205, d:'0 m', s:'0 m', note:'At Origin O: |s| = d = 0'},
    A: {y:45,  d:'10 m', s:'+10 m', note:'At Peak A: |s| = d = 10 m'},
    B: {y:109, d:'14 m (10+4)', s:'+6 m', note:'Falling at B: 6 m <= 14 m'},
    C: {y:205, d:'20 m (10+10)', s:'0 m', note:'Back at C: 0 m <= 20 m'}
  }[pt];
  document.getElementById('sim3_ball').setAttribute('cy', map.y);
  document.getElementById('sim3_dist').textContent = 'Distance: ' + map.d;
  document.getElementById('sim3_disp').textContent = 'Displacement: ' + map.s;
  document.getElementById('sim3_ineq').textContent = map.note;
};
</script>""",

    4: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Example 4.1: Ancient Postmen (210 Yojanas)</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Day: <b id="sim4_day" class="text-cyan-300">0</b> / 15</label>
      <input type="range" min="0" max="15" value="0" oninput="updSim4(this.value)" class="w-36 accent-amber-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="60" y1="140" x2="540" y2="140" stroke="#475569" stroke-width="4"/>
    <text x="60" y="168" text-anchor="middle" fill="#38bdf8" font-size="11">0 yojana</text>
    <text x="540" y="168" text-anchor="middle" fill="#34d399" font-size="11">210 yojanas</text>
    <circle id="sim4_p1" cx="60" cy="126" r="12" fill="#06b6d4" stroke="#cffafe" stroke-width="2"/>
    <text id="sim4_t1" x="60" y="102" text-anchor="middle" fill="#67e8f9" font-size="11" font-weight="bold">9 yoj/day (0)</text>
    <circle id="sim4_p2" cx="540" cy="126" r="12" fill="#10b981" stroke="#a7f3d0" stroke-width="2"/>
    <text id="sim4_t2" x="540" y="102" text-anchor="middle" fill="#6ee7b7" font-size="11" font-weight="bold">5 yoj/day (210)</text>
    <text id="sim4_gap" x="300" y="50" text-anchor="middle" fill="#fbbf24" font-size="15" font-weight="bold">Remaining Gap: 210 yojanas</text>
  </svg>
  <div class="text-xs text-slate-300 bg-slate-900/70 rounded-lg px-3 py-1.5 border border-slate-800">
    Combined rate = 9 + 5 = <b>14 yojanas/day</b>. Time to meet = 210 / 14 = <b>15 days</b> (Aryabhatiya / Ganitakaumudi tradition).
  </div>
</div>
<script>
window.updSim4 = function(day){
  day = parseInt(day,10);
  document.getElementById('sim4_day').textContent = day;
  const d1 = 9*day, d2 = 5*day;
  const x1 = 60 + (d1/210)*480;
  const x2 = 540 - (d2/210)*480;
  document.getElementById('sim4_p1').setAttribute('cx', x1);
  document.getElementById('sim4_t1').setAttribute('x', x1);
  document.getElementById('sim4_t1').textContent = '9/day ('+d1+')';
  document.getElementById('sim4_p2').setAttribute('cx', x2);
  document.getElementById('sim4_t2').setAttribute('x', x2);
  document.getElementById('sim4_t2').textContent = '5/day ('+(210-d2)+')';
  const rem = 210 - (d1+d2);
  document.getElementById('sim4_gap').textContent = rem===0 ? 'MEET AT 135 YOJANAS ON DAY 15!' : 'Remaining Gap: '+rem+' yojanas';
};
</script>""",

    5: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Example 4.2: 25 m Pool Round Trip (50 s)</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Time: <b id="sim5_t" class="text-amber-300">0 s</b></label>
      <input type="range" min="0" max="50" value="0" oninput="updSim5(this.value)" class="w-36 accent-cyan-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="80" y="95" width="440" height="75" rx="10" fill="#083344" stroke="#06b6d4" stroke-width="2"/>
    <text x="80" y="85" text-anchor="middle" fill="#cbd5e1" font-size="11">Start Wall (0 m)</text>
    <text x="520" y="85" text-anchor="middle" fill="#cbd5e1" font-size="11">Far Wall (25 m)</text>
    <circle id="sim5_sw" cx="80" cy="132" r="12" fill="#fbbf24" stroke="#fef3c7" stroke-width="2"/>
    <text id="sim5_spd" x="150" y="205" fill="#38bdf8" font-size="13" font-weight="bold">Avg Speed: 1.00 m/s</text>
    <text id="sim5_vel" x="360" y="205" fill="#34d399" font-size="13" font-weight="bold">Avg Velocity: 0.00 m/s</text>
    <text id="sim5_pos" x="300" y="45" text-anchor="middle" fill="#e2e8f0" font-size="14" font-weight="bold">Distance = 0 m | Displacement = 0 m</text>
  </svg>
</div>
<script>
window.updSim5 = function(t){
  t = parseInt(t,10);
  document.getElementById('sim5_t').textContent = t + ' s';
  const dist = t;
  const disp = t <= 25 ? t : (50 - t);
  const cx = 80 + (disp/25)*440;
  document.getElementById('sim5_sw').setAttribute('cx', cx);
  document.getElementById('sim5_pos').textContent = 'Distance = '+dist+' m | Displacement = +'+disp+' m';
  const avSpd = t===0 ? '0.00' : (dist/t).toFixed(2);
  const avVel = t===0 ? '0.00' : (disp/t).toFixed(2);
  document.getElementById('sim5_spd').textContent = 'Avg Speed: '+avSpd+' m/s';
  document.getElementById('sim5_vel').textContent = 'Avg Velocity: '+avVel+' m/s';
};
</script>""",

    6: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-rose-300 uppercase">Acceleration Calculator (Ex 4.3 & 4.4)</span>
    <div class="flex gap-1.5">
      <button onclick="setAcc6(10,20,20,'Bus Speeding Up (Ex 4.3)')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Bus +a</button>
      <button onclick="setAcc6(15,0,5,'Bus Braking (Ex 4.3)')" class="px-2 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">Bus Brake</button>
      <button onclick="setAcc6(0,29.4,3,'Free Fall g (Ex 4.4)')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Free Fall g</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <text id="sim6_title" x="300" y="40" text-anchor="middle" fill="#e2e8f0" font-size="15" font-weight="bold">Bus Speeding Up (Ex 4.3)</text>
    <rect x="70" y="70" width="140" height="70" rx="10" fill="#0f172a" stroke="#334155"/>
    <text x="140" y="95" text-anchor="middle" fill="#94a3b8" font-size="11">Initial Velocity (u)</text>
    <text id="sim6_u" x="140" y="122" text-anchor="middle" fill="#38bdf8" font-size="18" font-weight="bold">10 m/s</text>
    <rect x="230" y="70" width="140" height="70" rx="10" fill="#0f172a" stroke="#334155"/>
    <text x="300" y="95" text-anchor="middle" fill="#94a3b8" font-size="11">Final Velocity (v)</text>
    <text id="sim6_v" x="300" y="122" text-anchor="middle" fill="#34d399" font-size="18" font-weight="bold">20 m/s</text>
    <rect x="390" y="70" width="140" height="70" rx="10" fill="#0f172a" stroke="#334155"/>
    <text x="460" y="95" text-anchor="middle" fill="#94a3b8" font-size="11">Time Interval (t)</text>
    <text id="sim6_t" x="460" y="122" text-anchor="middle" fill="#fbbf24" font-size="18" font-weight="bold">20 s</text>
    <rect x="130" y="162" width="340" height="54" rx="12" fill="#1e293b" stroke="#06b6d4"/>
    <text id="sim6_res" x="300" y="195" text-anchor="middle" fill="#67e8f9" font-size="17" font-weight="bold">a = (20 - 10) / 20 = +0.5 m/s²</text>
  </svg>
</div>
<script>
window.setAcc6 = function(u,v,t,label){
  const a = ((v-u)/t).toFixed(1);
  const sign = a>0 ? '+' : '';
  document.getElementById('sim6_title').textContent = label;
  document.getElementById('sim6_u').textContent = u + ' m/s';
  document.getElementById('sim6_v').textContent = v + ' m/s';
  document.getElementById('sim6_t').textContent = t + ' s';
  document.getElementById('sim6_res').textContent = 'a = ('+v+' - '+u+') / '+t+' = '+sign+a+' m/s²';
};
</script>""",

    7: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Activity 4.3 & Ex 4.5: Plotting s-t Graphs</span>
    <div class="flex gap-1.5">
      <button onclick="setGraph7('uniform')" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Table 4.3 (Uniform)</button>
      <button onclick="setGraph7('accel')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Ex 4.5 (Curved)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 245" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g stroke="#1e293b" stroke-width="1">
      <line x1="80" y1="50" x2="520" y2="50"/><line x1="80" y1="90" x2="520" y2="90"/><line x1="80" y1="130" x2="520" y2="130"/><line x1="80" y1="170" x2="520" y2="170"/>
      <line x1="168" y1="30" x2="168" y2="210"/><line x1="256" y1="30" x2="256" y2="210"/><line x1="344" y1="30" x2="344" y2="210"/><line x1="432" y1="30" x2="432" y2="210"/>
    </g>
    <line x1="80" y1="210" x2="540" y2="210" stroke="#94a3b8" stroke-width="2"/>
    <line x1="80" y1="210" x2="80" y2="25" stroke="#94a3b8" stroke-width="2"/>
    <text x="535" y="226" fill="#cbd5e1" font-size="11">Time t (s)</text>
    <text x="20" y="38" fill="#cbd5e1" font-size="11">Position s (m)</text>
    <path id="sim7_path" d="M 80 210 L 168 178 L 256 146 L 344 114 L 432 82 L 520 50" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <g id="sim7_pts" fill="#fbbf24">
      <circle cx="80" cy="210" r="4"/><circle cx="168" cy="178" r="4"/><circle cx="256" cy="146" r="4"/>
      <circle cx="344" cy="114" r="4"/><circle cx="432" cy="82" r="4"/><circle cx="520" cy="50" r="4"/>
    </g>
    <text id="sim7_lbl" x="300" y="35" text-anchor="middle" fill="#67e8f9" font-size="13" font-weight="bold">Uniform Motion: Straight Line s-t Graph</text>
  </svg>
</div>
<script>
window.setGraph7 = function(kind){
  const p = document.getElementById('sim7_path');
  const g = document.getElementById('sim7_pts');
  const l = document.getElementById('sim7_lbl');
  if(kind==='uniform'){
    p.setAttribute('d','M 80 210 L 168 178 L 256 146 L 344 114 L 432 82 L 520 50');
    p.setAttribute('stroke','#38bdf8');
    const coords=[[80,210],[168,178],[256,146],[344,114],[432,82],[520,50]];
    g.innerHTML = coords.map(c=>'<circle cx="'+c[0]+'" cy="'+c[1]+'" r="4"/>').join('');
    l.textContent='Uniform Motion: Straight Line s-t Graph';
    l.setAttribute('fill','#67e8f9');
  } else {
    p.setAttribute('d','M 80 210 Q 300 205 520 40');
    p.setAttribute('stroke','#f59e0b');
    const coords=[[80,210],[168,203],[256,184],[344,151],[432,102],[520,40]];
    g.innerHTML = coords.map(c=>'<circle cx="'+c[0]+'" cy="'+c[1]+'" r="4"/>').join('');
    l.textContent='Non-Uniform Accelerated Motion (Ex 4.5): Upward Curve';
    l.setAttribute('fill','#fcd34d');
  }
};
</script>""",

    8: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Activity 4.4 & Ex 4.6–4.7: s-t Slope</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Object A Slope: <b id="sim8_v" class="text-cyan-300">4 m/s</b></label>
      <input type="range" min="0" max="8" step="1" value="4" oninput="updSim8(this.value)" class="w-36 accent-emerald-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="80" y1="205" x2="540" y2="205" stroke="#94a3b8" stroke-width="2"/>
    <line x1="80" y1="205" x2="80" y2="30" stroke="#94a3b8" stroke-width="2"/>
    <line x1="80" y1="205" x2="480" y2="145" stroke="#64748b" stroke-width="2.5" stroke-dasharray="6,4"/>
    <text x="488" y="148" fill="#94a3b8" font-size="11">Object B (2 m/s)</text>
    <line id="sim8_lineA" x1="80" y1="205" x2="480" y2="85" stroke="#34d399" stroke-width="3.5"/>
    <polygon id="sim8_tri" points="200,169 360,169 360,121" fill="#10b981" fill-opacity="0.2" stroke="#34d399" stroke-dasharray="3,3"/>
    <text id="sim8_lbl" x="300" y="35" text-anchor="middle" fill="#6ee7b7" font-size="13" font-weight="bold">Slope = (s2 - s1)/(t2 - t1) = 4 m/s (Faster than B)</text>
  </svg>
</div>
<script>
window.updSim8 = function(v){
  v = parseInt(v,10);
  document.getElementById('sim8_v').textContent = v + ' m/s';
  const yEnd = 205 - v*20;
  document.getElementById('sim8_lineA').setAttribute('y2', yEnd);
  const y1 = 205 - (v*20)*0.3;
  const y2 = 205 - (v*20)*0.7;
  document.getElementById('sim8_tri').setAttribute('points', '200,'+y1+' 360,'+y1+' 360,'+y2);
  let msg = 'Slope = '+v+' m/s ';
  if(v===0) msg = 'Horizontal Line (Slope = 0 m/s): Object at REST (Ex 4.6)';
  else if(v>2) msg += '(Steeper than B: Faster)';
  else if(v===2) msg += '(Same Slope as B)';
  else msg += '(Gentler than B: Slower)';
  document.getElementById('sim8_lbl').textContent = msg;
};
</script>"""
}
