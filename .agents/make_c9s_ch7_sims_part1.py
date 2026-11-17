#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sims_part1 = {
    1: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Wheat Bags &amp; F-s Graph (W = F &times; s)</span>
    <div class="flex items-center gap-3">
      <label class="text-xs text-slate-300">Bags (50 N ea): <b id="c7s1_b" class="text-amber-300">3</b></label>
      <input type="range" min="1" max="5" step="1" value="3" oninput="updC7S1()" id="c7s1_bags" class="w-20 accent-amber-400">
      <label class="text-xs text-slate-300">Height s: <b id="c7s1_h" class="text-cyan-300">2 m</b></label>
      <input type="range" min="1" max="4" step="1" value="2" oninput="updC7S1()" id="c7s1_dist" class="w-20 accent-cyan-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="60" y1="200" x2="270" y2="200" stroke="#64748b" stroke-width="2"/>
    <g id="c7s1_stack">
      <rect x="115" y="130" width="90" height="24" rx="4" fill="#d97706" stroke="#fde68a"/>
      <text x="160" y="146" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">5 kg (50 N)</text>
    </g>
    <line x1="90" y1="200" x2="90" y2="110" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
    <text id="c7s1_s_lbl" x="78" y="155" text-anchor="end" fill="#7dd3fc" font-size="11">s = 2 m</text>
    <line x1="330" y1="190" x2="560" y2="190" stroke="#94a3b8" stroke-width="2"/>
    <line x1="330" y1="190" x2="330" y2="35" stroke="#94a3b8" stroke-width="2"/>
    <text x="445" y="210" text-anchor="middle" fill="#94a3b8" font-size="11">Displacement s (m)</text>
    <text x="318" y="115" text-anchor="middle" fill="#94a3b8" font-size="11" transform="rotate(-90 318 115)">Force F (N)</text>
    <rect id="c7s1_area" x="330" y="100" width="90" height="90" fill="rgba(56,189,248,0.28)" stroke="#38bdf8" stroke-width="2"/>
    <text id="c7s1_w_lbl" x="445" y="60" text-anchor="middle" fill="#34d399" font-size="15" font-weight="bold">Area = W = 300 J</text>
    <text x="445" y="80" text-anchor="middle" fill="#cbd5e1" font-size="11">1 Joule = 1 N &middot; m (Scalar)</text>
  </svg>
</div>
<script>
window.updC7S1 = function(){
  const b = parseInt(document.getElementById('c7s1_bags').value,10);
  const s = parseInt(document.getElementById('c7s1_dist').value,10);
  const F = b * 50;
  const W = F * s;
  document.getElementById('c7s1_b').textContent = b + ' (' + F + ' N)';
  document.getElementById('c7s1_h').textContent = s + ' m';
  document.getElementById('c7s1_s_lbl').textContent = 's = ' + s + ' m';
  document.getElementById('c7s1_w_lbl').textContent = 'Area = W = ' + W + ' J';
  const hPx = Math.min(130, b * 24);
  const wPx = s * 45;
  const r = document.getElementById('c7s1_area');
  r.setAttribute('y', 190 - hPx);
  r.setAttribute('height', hPx);
  r.setAttribute('width', wPx);
  const yLift = 185 - s * 28;
  const stk = document.getElementById('c7s1_stack');
  stk.setAttribute('transform', 'translate(0,' + (yLift - 130) + ')');
};
</script>""",

    2: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-amber-300 uppercase">Sign of Work Done</span>
    <div class="flex gap-1.5 flex-wrap">
      <button onclick="setC7S2('wall')" class="px-2 py-1 rounded bg-slate-700 text-xs text-slate-200 border border-slate-500">Wall (s=0)</button>
      <button onclick="setC7S2('carry')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">90&deg; Carry</button>
      <button onclick="setC7S2('lift')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Lift (+W)</button>
      <button onclick="setC7S2('keeper')" class="px-2 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">Keeper (-30 J)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="c7s2_wall">
      <rect x="370" y="45" width="35" height="150" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
      <circle cx="230" cy="120" r="22" fill="#38bdf8"/>
      <line x1="255" y1="120" x2="360" y2="120" stroke="#fbbf24" stroke-width="4"/>
      <polygon points="366,120 352,113 352,127" fill="#fbbf24"/>
      <text x="300" y="32" text-anchor="middle" fill="#cbd5e1" font-size="14" font-weight="bold">Pushing Rigid Wall: s = 0 m &rArr; W = 0 J</text>
      <text x="300" y="220" text-anchor="middle" fill="#94a3b8" font-size="12">Zero displacement means zero scientific work</text>
    </g>
    <g id="c7s2_carry" style="display:none">
      <rect x="260" y="110" width="80" height="45" rx="6" fill="#0ea5e9" stroke="#bae6fd" stroke-width="2"/>
      <line x1="300" y1="110" x2="300" y2="48" stroke="#34d399" stroke-width="4"/>
      <polygon points="300,40 293,54 307,54" fill="#34d399"/>
      <text x="315" y="65" fill="#6ee7b7" font-size="12" font-weight="bold">F (upward)</text>
      <line x1="345" y1="132" x2="455" y2="132" stroke="#fbbf24" stroke-width="4"/>
      <polygon points="463,132 449,125 449,139" fill="#fbbf24"/>
      <text x="410" y="155" text-anchor="middle" fill="#fde047" font-size="12" font-weight="bold">s (horizontal)</text>
      <text x="300" y="210" text-anchor="middle" fill="#7dd3fc" font-size="14" font-weight="bold">Angle = 90&deg; (Perpendicular) &rArr; W = 0 J</text>
    </g>
    <g id="c7s2_lift" style="display:none">
      <rect x="270" y="125" width="60" height="30" rx="6" fill="#10b981" stroke="#a7f3d0" stroke-width="2"/>
      <line x1="250" y1="155" x2="250" y2="65" stroke="#34d399" stroke-width="4"/>
      <polygon points="250,56 243,70 257,70" fill="#34d399"/>
      <line x1="350" y1="155" x2="350" y2="65" stroke="#fbbf24" stroke-width="4"/>
      <polygon points="350,56 343,70 357,70" fill="#fbbf24"/>
      <text x="235" y="110" text-anchor="end" fill="#6ee7b7" font-size="12">F (up)</text>
      <text x="365" y="110" text-anchor="start" fill="#fde047" font-size="12">s (up)</text>
      <text x="300" y="205" text-anchor="middle" fill="#34d399" font-size="14" font-weight="bold">Same Direction (Ex 7.1 Lift): Positive Work (+W)</text>
    </g>
    <g id="c7s2_keeper" style="display:none">
      <circle cx="220" cy="120" r="24" fill="#f8fafc" stroke="#94a3b8" stroke-width="3"/>
      <line x1="250" y1="100" x2="360" y2="100" stroke="#fbbf24" stroke-width="4"/>
      <polygon points="368,100 354,93 354,107" fill="#fbbf24"/>
      <text x="305" y="88" text-anchor="middle" fill="#fde047" font-size="12">s = +0.15 m (forward)</text>
      <line x1="360" y1="145" x2="250" y2="145" stroke="#f43f5e" stroke-width="4"/>
      <polygon points="242,145 256,138 256,152" fill="#f43f5e"/>
      <text x="305" y="168" text-anchor="middle" fill="#fda4af" font-size="12">F = 200 N (opposite)</text>
      <text x="300" y="210" text-anchor="middle" fill="#fb7185" font-size="14" font-weight="bold">Ex 7.2: W = 200 &times; (-0.15) = -30 J (Negative Work)</text>
    </g>
  </svg>
</div>
<script>
window.setC7S2 = function(m){
  ['wall','carry','lift','keeper'].forEach(k=>{
    document.getElementById('c7s2_'+k).style.display=(k===m?'block':'none');
  });
};
</script>""",

    3: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Ex 7.3 Carrom Collision &amp; Work-Energy Theorem</span>
    <div class="flex gap-2">
      <button onclick="setC7S3(1)" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">1. Flick Striker</button>
      <button onclick="setC7S3(2)" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">2. Hit White</button>
      <button onclick="setC7S3(3)" class="px-2.5 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">3. Hit Black</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="60" y="35" width="480" height="145" rx="14" fill="#1e293b" stroke="#b45309" stroke-width="5"/>
    <circle id="c7s3_st" cx="140" cy="108" r="20" fill="#ef4444" stroke="#fecaca" stroke-width="2"/>
    <circle id="c7s3_wh" cx="300" cy="108" r="16" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
    <circle id="c7s3_bk" cx="445" cy="108" r="16" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
    <text id="c7s3_msg" x="300" y="205" text-anchor="middle" fill="#6ee7b7" font-size="13" font-weight="bold">Work Done = &Delta;Energy | Hand transfers energy to Striker</text>
    <text x="300" y="225" text-anchor="middle" fill="#94a3b8" font-size="11">James Prescott Joule proved mechanical work &amp; heat energy are interchangeable (SI unit: J)</text>
  </svg>
</div>
<script>
window.setC7S3 = function(step){
  const st = document.getElementById('c7s3_st');
  const wh = document.getElementById('c7s3_wh');
  const bk = document.getElementById('c7s3_bk');
  const msg = document.getElementById('c7s3_msg');
  if(step===1){
    st.setAttribute('cx', 210); wh.setAttribute('cx', 300); bk.setAttribute('cx', 445);
    msg.textContent = 'Step 1: Finger does +W on Striker -> Striker gains Kinetic Energy!';
  } else if(step===2){
    st.setAttribute('cx', 265); wh.setAttribute('cx', 395); bk.setAttribute('cx', 445);
    msg.textContent = 'Step 2: Striker does +W on White coin -> White coin accelerates!';
  } else {
    st.setAttribute('cx', 265); wh.setAttribute('cx', 412); bk.setAttribute('cx', 505);
    msg.textContent = 'Step 3: White coin does +W on Black coin -> Energy flows down the chain!';
  }
};
</script>""",

    4: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Kinetic Energy K = &frac12;mv&sup2;</span>
    <div class="flex gap-1.5">
      <button onclick="presetC7S4(0.16,48.07,'Cricket Ball (Ex 7.5)')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Ex 7.5 Ball</button>
      <button onclick="presetC7S4(10000,70,'Landing Jet (Ex 7.6)')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Ex 7.6 Jet</button>
      <button onclick="presetC7S4(2,10,'2 kg @ 10 m/s')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">2x Speed Test</button>
    </div>
  </div>
  <div class="flex items-center justify-around bg-slate-900/60 rounded-lg px-3 py-1.5 text-xs text-slate-300">
    <label>Mass m (kg): <input id="c7s4_m" type="number" value="2" step="0.1" oninput="calcC7S4()" class="w-20 bg-slate-800 border border-slate-600 rounded px-1.5 py-0.5 text-cyan-300"></label>
    <label>Speed v (m/s): <input id="c7s4_v" type="number" value="5" step="0.5" oninput="calcC7S4()" class="w-20 bg-slate-800 border border-slate-600 rounded px-1.5 py-0.5 text-amber-300"></label>
    <span id="c7s4_lbl" class="font-bold text-emerald-300">Custom</span>
  </div>
  <svg viewBox="0 0 600 185" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="60" y="60" width="480" height="32" rx="8" fill="#1e293b" stroke="#475569"/>
    <rect id="c7s4_bar" x="60" y="60" width="120" height="32" rx="8" fill="#38bdf8"/>
    <text id="c7s4_res" x="300" y="38" text-anchor="middle" fill="#6ee7b7" font-size="16" font-weight="bold">K = 25.0 J</text>
    <text id="c7s4_2v" x="300" y="135" text-anchor="middle" fill="#fde047" font-size="13">If speed doubles (2v), Kinetic Energy quadruples (4K = 100.0 J)!</text>
    <text x="300" y="160" text-anchor="middle" fill="#94a3b8" font-size="11">Convert km/h to m/s by multiplying by 5/18 (252 km/h = 70 m/s)</text>
  </svg>
</div>
<script>
window.presetC7S4 = function(m, v, name){
  document.getElementById('c7s4_m').value = m;
  document.getElementById('c7s4_v').value = v;
  document.getElementById('c7s4_lbl').textContent = name;
  calcC7S4();
};
window.calcC7S4 = function(){
  const m = Math.max(0, parseFloat(document.getElementById('c7s4_m').value)||0);
  const v = Math.max(0, parseFloat(document.getElementById('c7s4_v').value)||0);
  const K = 0.5 * m * v * v;
  const fmt = K >= 1e6 ? (K/1e6).toFixed(2)+' MJ' : K.toFixed(1)+' J';
  document.getElementById('c7s4_res').textContent = 'K = 0.5 x ' + m + ' x ' + v + '^2 = ' + fmt;
  const K4 = 4 * K;
  const fmt4 = K4 >= 1e6 ? (K4/1e6).toFixed(2)+' MJ' : K4.toFixed(1)+' J';
  document.getElementById('c7s4_2v').textContent = 'Doubling speed to ' + (2*v) + ' m/s quadruples K to ' + fmt4 + '!';
  document.getElementById('c7s4_bar').setAttribute('width', Math.min(480, Math.max(12, Math.log10(K+1)*70)));
};
</script>""",

    5: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Activity 7.1 Sand Drop &amp; U = mgh</span>
    <div class="flex items-center gap-3">
      <label class="text-xs text-slate-300">Mass m: <b id="c7s5_m_lbl" class="text-cyan-300">0.2 kg</b></label>
      <input type="range" min="0.2" max="2.0" step="0.2" value="0.2" id="c7s5_m" oninput="updC7S5()" class="w-20 accent-cyan-400">
      <label class="text-xs text-slate-300">Height h: <b id="c7s5_h_lbl" class="text-amber-300">10 m</b></label>
      <input type="range" min="1" max="10" step="1" value="10" id="c7s5_h" oninput="updC7S5()" class="w-24 accent-amber-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="120" y="180" width="360" height="36" rx="6" fill="#ca8a04" stroke="#fde047" stroke-width="2"/>
    <ellipse id="c7s5_crater" cx="300" cy="182" rx="34" ry="12" fill="#713f12"/>
    <circle id="c7s5_ball" cx="300" cy="45" r="18" fill="#38bdf8" stroke="#bae6fd" stroke-width="2"/>
    <line x1="210" y1="45" x2="210" y2="180" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4,3"/>
    <text id="c7s5_u_lbl" x="300" y="25" text-anchor="middle" fill="#6ee7b7" font-size="15" font-weight="bold">Ex 7.7: U = 0.2 x 10 x 10 = 20.0 J</text>
    <text id="c7s5_dent" x="300" y="204" text-anchor="middle" fill="#fef08a" font-size="12" font-weight="bold">Sand Crater Depth: Deep Impact (20.0 J)</text>
  </svg>
</div>
<script>
window.updC7S5 = function(){
  const m = parseFloat(document.getElementById('c7s5_m').value);
  const h = parseInt(document.getElementById('c7s5_h').value,10);
  const U = m * 10 * h;
  document.getElementById('c7s5_m_lbl').textContent = m.toFixed(1) + ' kg';
  document.getElementById('c7s5_h_lbl').textContent = h + ' m';
  document.getElementById('c7s5_u_lbl').textContent = 'U = ' + m.toFixed(1) + ' x 10 x ' + h + ' = ' + U.toFixed(1) + ' J (g = 10 m/s^2)';
  document.getElementById('c7s5_ball').setAttribute('cy', 160 - h * 11.5);
  document.getElementById('c7s5_crater').setAttribute('rx', Math.min(85, 16 + U * 0.6));
  document.getElementById('c7s5_crater').setAttribute('ry', Math.min(18, 5 + U * 0.12));
  document.getElementById('c7s5_dent').textContent = 'Higher h or larger m stores more U -> deeper sand dent!';
};
</script>""",

    6: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Activity 7.2 Pendulum &amp; Free Fall ME = K + U</span>
    <div class="flex gap-1.5">
      <button onclick="setC7S6('P')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Point P (Max U)</button>
      <button onclick="setC7S6('Q')" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Point Q (Max K)</button>
      <button onclick="setC7S6('R')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Point R (Max U)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="120" y1="25" x2="260" y2="25" stroke="#94a3b8" stroke-width="4"/>
    <path d="M 105 130 Q 190 195 275 130" fill="none" stroke="#475569" stroke-width="2" stroke-dasharray="5,4"/>
    <line id="c7s6_rod" x1="190" y1="25" x2="190" y2="165" stroke="#cbd5e1" stroke-width="2"/>
    <circle id="c7s6_bob" cx="190" cy="165" r="16" fill="#38bdf8" stroke="#bae6fd" stroke-width="2"/>
    <text x="100" y="125" fill="#fbbf24" font-size="12" font-weight="bold">P</text>
    <text x="190" y="198" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">Q</text>
    <text x="278" y="125" fill="#fbbf24" font-size="12" font-weight="bold">R</text>
    <text x="370" y="45" fill="#cbd5e1" font-size="12" font-weight="bold">Mechanical Energy Bars (Total = 100 J)</text>
    <rect x="370" y="65" width="38" height="120" fill="#1e293b" stroke="#475569"/>
    <rect id="c7s6_kbar" x="370" y="65" width="38" height="120" fill="#38bdf8"/>
    <text x="389" y="202" text-anchor="middle" fill="#7dd3fc" font-size="12">K</text>
    <rect x="440" y="65" width="38" height="120" fill="#1e293b" stroke="#475569"/>
    <rect id="c7s6_ubar" x="440" y="185" width="38" height="0" fill="#fbbf24"/>
    <text x="459" y="202" text-anchor="middle" fill="#fde047" font-size="12">U</text>
    <rect x="510" y="65" width="38" height="120" fill="#34d399" stroke="#a7f3d0"/>
    <text x="529" y="202" text-anchor="middle" fill="#6ee7b7" font-size="12">ME</text>
    <text id="c7s6_txt" x="300" y="228" text-anchor="middle" fill="#6ee7b7" font-size="12" font-weight="bold">At Q (lowest point): K = 100%, U = 0%, Total ME = K + U constant!</text>
  </svg>
</div>
<script>
window.setC7S6 = function(pt){
  const rod = document.getElementById('c7s6_rod');
  const bob = document.getElementById('c7s6_bob');
  const kb = document.getElementById('c7s6_kbar');
  const ub = document.getElementById('c7s6_ubar');
  const txt = document.getElementById('c7s6_txt');
  if(pt==='P'){
    rod.setAttribute('x2',115); rod.setAttribute('y2',135);
    bob.setAttribute('cx',115); bob.setAttribute('cy',135);
    kb.setAttribute('y',185); kb.setAttribute('height',0);
    ub.setAttribute('y',65); ub.setAttribute('height',120);
    txt.textContent = 'At extreme P: v = 0 (K = 0 J), height max (U = 100 J), ME = 100 J!';
  } else if(pt==='R'){
    rod.setAttribute('x2',265); rod.setAttribute('y2',135);
    bob.setAttribute('cx',265); bob.setAttribute('cy',135);
    kb.setAttribute('y',185); kb.setAttribute('height',0);
    ub.setAttribute('y',65); ub.setAttribute('height',120);
    txt.textContent = 'At extreme R: v = 0 (K = 0 J), height max (U = 100 J), ME = 100 J!';
  } else {
    rod.setAttribute('x2',190); rod.setAttribute('y2',165);
    bob.setAttribute('cx',190); bob.setAttribute('cy',165);
    kb.setAttribute('y',65); kb.setAttribute('height',120);
    ub.setAttribute('y',185); ub.setAttribute('height',0);
    txt.textContent = 'At Q (lowest point): K = 100 J (fastest!), U = 0 J, ME = 100 J!';
  }
};
</script>""",

    7: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-rose-300 uppercase">Ex 7.8 Slide &amp; Ex 7.9 Runaway Truck Escape Ramp</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Truck Speed v: <b id="c7s7_v_lbl" class="text-amber-300">20 m/s</b></label>
      <input type="range" min="10" max="30" step="5" value="20" id="c7s7_v" oninput="updC7S7()" class="w-24 accent-rose-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <polygon points="80,190 520,190 520,75" fill="rgba(217,119,6,0.22)" stroke="#f59e0b" stroke-width="2"/>
    <line x1="80" y1="190" x2="520" y2="75" stroke="#fbbf24" stroke-width="4" stroke-dasharray="6,4"/>
    <rect x="255" y="118" width="52" height="24" rx="4" fill="#ef4444" stroke="#fecaca" transform="rotate(-14.6 281 130)"/>
    <text x="150" y="178" fill="#fde047" font-size="12" font-weight="bold">30&deg; Sand Ramp</text>
    <text id="c7s7_ke" x="300" y="34" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="bold">Initial KE = 2,000,000 J (10,000 kg @ 20 m/s = 72 km/h)</text>
    <text id="c7s7_len" x="300" y="56" text-anchor="middle" fill="#6ee7b7" font-size="14" font-weight="bold">Min Stopping Ramp L = 20.0 m (Sand Drag 50 kN + Gravity PE)</text>
    <text x="300" y="218" text-anchor="middle" fill="#cbd5e1" font-size="11">Ex 7.8 Frictionless Slide: v = &radic;(2gh) &mdash; independent of mass &amp; slide curve shape!</text>
  </svg>
</div>
<script>
window.updC7S7 = function(){
  const v = parseInt(document.getElementById('c7s7_v').value,10);
  const KE = 0.5 * 10000 * v * v;
  const L = KE / 100000;
  document.getElementById('c7s7_v_lbl').textContent = v + ' m/s (' + Math.round(v*3.6) + ' km/h)';
  document.getElementById('c7s7_ke').textContent = 'Initial KE = ' + KE.toLocaleString() + ' J (10,000 kg @ ' + v + ' m/s)';
  document.getElementById('c7s7_len').textContent = 'Min Stopping Ramp L = ' + L.toFixed(1) + ' m (KE = 50,000L + 50,000L)';
};
</script>""",

    8: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Power P = W / t &amp; Horsepower (1 hp = 746 W)</span>
    <div class="flex gap-1.5">
      <button onclick="setC7S8(1500,5,'Ex 7.10 Barbell (75 kg, 2 m, 5 s)')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Ex 7.10 (300 W)</button>
      <button onclick="setC7S8(200000,10,'Ex 7.11 Car (1000 kg -> 20 m/s in 10 s)')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Ex 7.11 (20 kW)</button>
    </div>
  </div>
  <div class="flex items-center justify-around bg-slate-900/60 rounded-lg px-3 py-1.5 text-xs text-slate-300">
    <label>Work W (J): <input id="c7s8_w" type="number" value="1500" oninput="calcC7S8()" class="w-24 bg-slate-800 border border-slate-600 rounded px-1.5 py-0.5 text-cyan-300"></label>
    <label>Time t (s): <input id="c7s8_t" type="number" value="5" min="1" oninput="calcC7S8()" class="w-16 bg-slate-800 border border-slate-600 rounded px-1.5 py-0.5 text-amber-300"></label>
    <span id="c7s8_tag" class="font-bold text-emerald-300">Ex 7.10 Barbell</span>
  </div>
  <svg viewBox="0 0 600 185" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <text id="c7s8_p" x="300" y="55" text-anchor="middle" fill="#fbbf24" font-size="22" font-weight="bold">P = 300.0 W (0.40 hp)</text>
    <text x="300" y="95" text-anchor="middle" fill="#cbd5e1" font-size="13">1 Watt = 1 Joule / second | Faster work in less time = Higher Power</text>
    <text x="300" y="135" text-anchor="middle" fill="#7dd3fc" font-size="12">James Watt improved steam engines and defined 1 hp = 746 W</text>
  </svg>
</div>
<script>
window.setC7S8 = function(w,t,lbl){
  document.getElementById('c7s8_w').value = w;
  document.getElementById('c7s8_t').value = t;
  document.getElementById('c7s8_tag').textContent = lbl;
  calcC7S8();
};
window.calcC7S8 = function(){
  const w = Math.max(0, parseFloat(document.getElementById('c7s8_w').value)||0);
  const t = Math.max(0.1, parseFloat(document.getElementById('c7s8_t').value)||1);
  const P = w / t;
  const hp = P / 746;
  document.getElementById('c7s8_p').textContent = 'P = ' + P.toFixed(1) + ' W (' + hp.toFixed(2) + ' hp)';
};
</script>"""
}
