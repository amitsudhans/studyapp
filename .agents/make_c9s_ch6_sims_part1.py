#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sims_part1 = {
    1: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Effects of Force (Vector in N)</span>
    <div class="flex gap-1.5">
      <button onclick="setEff1('kick')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Kick Ball</button>
      <button onclick="setEff1('bat')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Cricket Bat</button>
      <button onclick="setEff1('lemon')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Squeeze Lemon</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="sim1_kick">
      <circle cx="170" cy="135" r="26" fill="#38bdf8" stroke="#bae6fd" stroke-width="2"/>
      <line x1="205" y1="135" x2="345" y2="135" stroke="#fbbf24" stroke-width="4"/>
      <polygon points="355,135 340,127 340,143" fill="#fbbf24"/>
      <text x="300" y="65" text-anchor="middle" fill="#7dd3fc" font-size="15" font-weight="bold">Sets Stationary Object in Motion</text>
      <text x="300" y="195" text-anchor="middle" fill="#cbd5e1" font-size="12">Force has Magnitude + Direction | SI Unit: Newton (N)</text>
    </g>
    <g id="sim1_bat" style="display:none">
      <line x1="120" y1="95" x2="290" y2="135" stroke="#94a3b8" stroke-width="3" stroke-dasharray="5,4"/>
      <rect x="295" y="100" width="16" height="75" rx="4" fill="#d97706" stroke="#fde68a"/>
      <line x1="315" y1="135" x2="475" y2="75" stroke="#34d399" stroke-width="4"/>
      <polygon points="482,72 465,70 471,85" fill="#34d399"/>
      <text x="300" y="48" text-anchor="middle" fill="#6ee7b7" font-size="15" font-weight="bold">Changes Speed & Direction</text>
    </g>
    <g id="sim1_lemon" style="display:none">
      <ellipse cx="300" cy="130" rx="58" ry="26" fill="#eab308" stroke="#fef08a" stroke-width="2"/>
      <line x1="300" y1="65" x2="300" y2="98" stroke="#f43f5e" stroke-width="4"/>
      <polygon points="300,104 293,92 307,92" fill="#f43f5e"/>
      <line x1="300" y1="195" x2="300" y2="162" stroke="#f43f5e" stroke-width="4"/>
      <polygon points="300,156 293,168 307,168" fill="#f43f5e"/>
      <text x="300" y="42" text-anchor="middle" fill="#fde047" font-size="15" font-weight="bold">Changes Object's Shape</text>
    </g>
  </svg>
</div>
<script>
window.setEff1 = function(m){
  ['kick','bat','lemon'].forEach(k=>{
    document.getElementById('sim1_'+k).style.display=(k===m?'block':'none');
  });
};
</script>""",

    2: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Spring Balance Weight & Force Meter</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Mass: <b id="sim2_m" class="text-cyan-300">2 kg</b></label>
      <input type="range" min="1" max="5" step="1" value="2" oninput="updSim2(this.value)" class="w-32 accent-amber-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="275" y="20" width="50" height="100" rx="6" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
    <line id="sim2_spr" x1="300" y1="35" x2="300" y2="135" stroke="#fbbf24" stroke-width="3" stroke-dasharray="4,3"/>
    <rect id="sim2_blk" x="276" y="135" width="48" height="40" rx="6" fill="#06b6d4" stroke="#cffafe" stroke-width="2"/>
    <text id="sim2_wt" x="300" y="160" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">19.6 N</text>
    <text x="140" y="95" text-anchor="middle" fill="#cbd5e1" font-size="12" font-weight="bold">Human Touch Threshold:</text>
    <text x="140" y="115" text-anchor="middle" fill="#7dd3fc" font-size="13">~10⁻³ N (1 mN)</text>
    <text x="465" y="95" text-anchor="middle" fill="#cbd5e1" font-size="12" font-weight="bold">Extreme Lab Limit:</text>
    <text x="465" y="115" text-anchor="middle" fill="#6ee7b7" font-size="13">~10⁻²⁴ N (Yoctonewton)</text>
  </svg>
</div>
<script>
window.updSim2 = function(m){
  m = parseInt(m,10);
  document.getElementById('sim2_m').textContent = m + ' kg';
  const y = 115 + m*12;
  document.getElementById('sim2_spr').setAttribute('y2', y);
  document.getElementById('sim2_blk').setAttribute('y', y);
  document.getElementById('sim2_wt').setAttribute('y', y+24);
  document.getElementById('sim2_wt').textContent = (m*9.8).toFixed(1) + ' N';
};
</script>""",

    3: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Example 6.1: Net Force Combiner</span>
    <div class="flex gap-1.5">
      <button onclick="setNet3('same')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200">10 N → + 6 N →</button>
      <button onclick="setNet3('oppR')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200">10 N → vs ← 6 N</button>
      <button onclick="setNet3('oppL')" class="px-2 py-1 rounded bg-rose-600/30 text-xs text-rose-200">6 N → vs ← 10 N</button>
      <button onclick="setNet3('bal')" class="px-2 py-1 rounded bg-slate-700 text-xs text-slate-200">10 N → vs ← 10 N</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="60" y1="175" x2="540" y2="175" stroke="#475569" stroke-width="3"/>
    <rect x="255" y="105" width="90" height="70" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="300" y="145" text-anchor="middle" fill="#e2e8f0" font-size="13" font-weight="bold">Block</text>
    <text id="sim3_res" x="300" y="55" text-anchor="middle" fill="#6ee7b7" font-size="18" font-weight="bold">Net Force = 16 N Right (Unbalanced)</text>
    <text id="sim3_sub" x="300" y="82" text-anchor="middle" fill="#cbd5e1" font-size="12">10 N + 6 N in same direction | Couples (equal opposite parallel) cause rotation</text>
  </svg>
</div>
<script>
window.setNet3 = function(c){
  const map = {
    same: {t:'Net Force = 16 N Right (Unbalanced)', c:'#6ee7b7'},
    oppR: {t:'Net Force = 4 N Right (10 - 6)', c:'#7dd3fc'},
    oppL: {t:'Net Force = 4 N Left (10 - 6)', c:'#fda4af'},
    bal:  {t:'Net Force = 0 N (Balanced: No Motion Change)', c:'#fde68a'}
  }[c];
  const el = document.getElementById('sim3_res');
  el.textContent = map.t; el.setAttribute('fill', map.c);
};
</script>""",

    4: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Activities 6.1 & 6.2: Surface Friction</span>
    <div class="flex gap-1.5">
      <button onclick="setSurf4('wood')" class="px-2 py-1 rounded bg-amber-700/40 text-xs text-amber-200">Wood Table</button>
      <button onclick="setSurf4('lam')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200">Laminate</button>
      <button onclick="setSurf4('marble')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200">Polished Marble</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="50" y="160" width="500" height="18" rx="4" fill="#334155"/>
    <circle id="sim4_coin" cx="220" cy="145" r="14" fill="#f59e0b" stroke="#fef08a" stroke-width="2"/>
    <text id="sim4_t" x="300" y="55" text-anchor="middle" fill="#fde68a" font-size="15" font-weight="bold">Rough Wood: High Friction (Spring Pull: 4.5 N) | Short Glide</text>
    <text x="300" y="88" text-anchor="middle" fill="#cbd5e1" font-size="12">Galileo's Thought Experiment: Remove all friction ⇒ Constant velocity forever!</text>
  </svg>
</div>
<script>
window.setSurf4 = function(s){
  const map = {
    wood:   {x:200, t:'Rough Wood: High Friction (Spring Pull: 4.5 N) | Short Glide'},
    lam:    {x:340, t:'Laminated Top: Medium Friction (Spring Pull: 2.5 N) | Medium Glide'},
    marble: {x:490, t:'Polished Marble: Lowest Friction (Spring Pull: 1.0 N) | Longest Glide!'}
  }[s];
  document.getElementById('sim4_coin').setAttribute('cx', map.x);
  document.getElementById('sim4_t').textContent = map.t;
};
</script>""",

    5: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Example 6.3: Zero Net Force Graphs</span>
    <div class="flex gap-1.5">
      <button onclick="setF5('rest')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200">At Rest (v = 0)</button>
      <button onclick="setF5('unif')" class="px-2.5 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200">Uniform Motion (F_net = 0)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="60" y1="185" x2="260" y2="185" stroke="#94a3b8" stroke-width="2"/>
    <line x1="60" y1="185" x2="60" y2="55" stroke="#94a3b8" stroke-width="2"/>
    <text x="160" y="42" text-anchor="middle" fill="#7dd3fc" font-size="13" font-weight="bold">Position-Time (s-t)</text>
    <line id="sim5_st" x1="60" y1="115" x2="250" y2="115" stroke="#fbbf24" stroke-width="3.5"/>

    <line x1="340" y1="185" x2="540" y2="185" stroke="#94a3b8" stroke-width="2"/>
    <line x1="340" y1="185" x2="340" y2="55" stroke="#94a3b8" stroke-width="2"/>
    <text x="440" y="42" text-anchor="middle" fill="#6ee7b7" font-size="13" font-weight="bold">Velocity-Time (v-t)</text>
    <line id="sim5_vt" x1="340" y1="185" x2="530" y2="185" stroke="#34d399" stroke-width="3.5"/>
    <text id="sim5_msg" x="300" y="220" text-anchor="middle" fill="#e2e8f0" font-size="12" font-weight="bold">At Rest: Horizontal s-t line, v = 0 line (Inertia of Rest)</text>
  </svg>
</div>
<script>
window.setF5 = function(m){
  const st = document.getElementById('sim5_st');
  const vt = document.getElementById('sim5_vt');
  const msg = document.getElementById('sim5_msg');
  if(m==='rest'){
    st.setAttribute('y1',115); st.setAttribute('y2',115);
    vt.setAttribute('y1',185); vt.setAttribute('y2',185);
    msg.textContent = 'At Rest: Horizontal s-t line, v = 0 line (Inertia of Rest)';
  } else {
    st.setAttribute('y1',180); st.setAttribute('y2',70);
    vt.setAttribute('y1',115); vt.setAttribute('y2',115);
    msg.textContent = 'Uniform Motion (Ex 6.2/6.3): Push = Friction ⇒ Sloped s-t, Horizontal v-t';
  }
};
</script>""",

    6: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Activities 6.3 & 6.4: Pulley-Cart Lab</span>
    <div class="flex gap-1.5">
      <button onclick="setCart6(1,1)" class="px-2 py-1 rounded bg-slate-700 text-xs text-white">1F, 1m</button>
      <button onclick="setCart6(2,1)" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200">2F, 1m (Act 6.3)</button>
      <button onclick="setCart6(1,2)" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200">1F, 2m (Act 6.4)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="60" y="130" width="380" height="14" fill="#334155"/>
    <circle cx="445" cy="130" r="14" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
    <rect x="130" y="92" width="76" height="38" rx="6" fill="#06b6d4" stroke="#cffafe" stroke-width="2"/>
    <line x1="206" y1="112" x2="445" y2="116" stroke="#cbd5e1" stroke-width="2"/>
    <line x1="459" y1="130" x2="459" y2="185" stroke="#cbd5e1" stroke-width="2"/>
    <rect x="442" y="185" width="34" height="30" rx="4" fill="#f59e0b"/>
    <text id="sim6_res" x="300" y="48" text-anchor="middle" fill="#67e8f9" font-size="16" font-weight="bold">Baseline: Force = 1F, Mass = 1m ⇒ Acceleration = 1a</text>
    <text x="300" y="74" text-anchor="middle" fill="#cbd5e1" font-size="12">Measured via s = ½aT² using slow-motion video</text>
  </svg>
</div>
<script>
window.setCart6 = function(f,m){
  const ratio = (f/m).toFixed(1);
  document.getElementById('sim6_res').textContent = 'Force = '+f+'F, Mass = '+m+'m ⇒ Acceleration = '+ratio+'a';
};
</script>""",

    7: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">F = ma & Momentum (p = mv)</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Mass m: <b id="sim7_m" class="text-amber-300">10 kg</b></label>
      <input type="range" min="2" max="20" step="2" value="10" oninput="updSim7(this.value)" class="w-32 accent-cyan-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="45" y="40" width="245" height="160" rx="12" fill="#0f172a" stroke="#06b6d4" stroke-width="2"/>
    <text x="167" y="70" text-anchor="middle" fill="#67e8f9" font-size="14" font-weight="bold">Newton's 2nd Law & Weight</text>
    <text id="sim7_f" x="167" y="108" text-anchor="middle" fill="#34d399" font-size="16" font-weight="bold">For a = 2 m/s²: F = 20 N</text>
    <text id="sim7_w" x="167" y="142" text-anchor="middle" fill="#fbbf24" font-size="15" font-weight="bold">Weight (mg): 98.0 N</text>
    <text x="167" y="176" text-anchor="middle" fill="#94a3b8" font-size="11">1 N = 1 kg m s⁻²</text>

    <rect x="310" y="40" width="245" height="160" rx="12" fill="#0f172a" stroke="#a78bfa" stroke-width="2"/>
    <text x="432" y="70" text-anchor="middle" fill="#ddd6fe" font-size="14" font-weight="bold">Momentum Formulation</text>
    <text id="sim7_p" x="432" y="110" text-anchor="middle" fill="#c4b5fd" font-size="16" font-weight="bold">At v = 5 m/s: p = 50 kg·m/s</text>
    <text x="432" y="148" text-anchor="middle" fill="#cbd5e1" font-size="13">F = Δp / Δt = m(v - u) / t</text>
  </svg>
</div>
<script>
window.updSim7 = function(m){
  m = parseInt(m,10);
  document.getElementById('sim7_m').textContent = m + ' kg';
  document.getElementById('sim7_f').textContent = 'For a = 2 m/s²: F = ' + (m*2) + ' N';
  document.getElementById('sim7_w').textContent = 'Weight (mg): ' + (m*9.8).toFixed(1) + ' N';
  document.getElementById('sim7_p').textContent = 'At v = 5 m/s: p = ' + (m*5) + ' kg·m/s';
};
</script>""",

    8: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-rose-300 uppercase">F = Δp / Δt: Stopping Time & Impact Force</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Impact Time Δt: <b id="sim8_t" class="text-amber-300">0.20 s</b></label>
      <input type="range" min="0.02" max="0.50" step="0.02" value="0.20" oninput="updSim8(this.value)" class="w-32 accent-rose-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <text x="300" y="45" text-anchor="middle" fill="#cbd5e1" font-size="13">Fixed Momentum Change Δp = 4.0 kg·m/s (Cricket Catch / Airbag vs Coconut Strike)</text>
    <rect x="90" y="95" width="420" height="32" rx="8" fill="#1e293b"/>
    <rect id="sim8_bar" x="90" y="95" width="60" height="32" rx="8" fill="#34d399"/>
    <text id="sim8_f" x="300" y="168" text-anchor="middle" fill="#6ee7b7" font-size="20" font-weight="bold">Average Impact Force F = 20 N</text>
    <text id="sim8_note" x="300" y="200" text-anchor="middle" fill="#94a3b8" font-size="12">Longer Δt (pulling hands back / airbag) ⇒ Safe low force!</text>
  </svg>
</div>
<script>
window.updSim8 = function(dt){
  dt = parseFloat(dt);
  document.getElementById('sim8_t').textContent = dt.toFixed(2) + ' s';
  const f = Math.round(4.0 / dt);
  document.getElementById('sim8_f').textContent = 'Average Impact Force F = ' + f + ' N';
  const bar = document.getElementById('sim8_bar');
  bar.setAttribute('width', Math.min(420, f*2));
  bar.setAttribute('fill', f > 80 ? '#f43f5e' : '#34d399');
  document.getElementById('sim8_note').textContent = f > 80 ? 'Tiny Δt (hard strike) ⇒ Huge shattering force (cracking coconut)!' : 'Longer Δt (pulling hands back / airbag) ⇒ Safe low force!';
};
</script>"""
}
