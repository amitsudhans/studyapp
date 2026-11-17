#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sims_part2 = {
    9: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Pulley Systems (MA = Load / Effort)</span>
    <div class="flex gap-2">
      <button onclick="setC7S9('fixed')" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Fixed Pulley (MA = 1)</button>
      <button onclick="setC7S9('movable')" class="px-2.5 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Movable Pulley (MA = 2)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="c7s9_fixed">
      <line x1="220" y1="25" x2="380" y2="25" stroke="#94a3b8" stroke-width="5"/>
      <line x1="300" y1="25" x2="300" y2="65" stroke="#94a3b8" stroke-width="3"/>
      <circle cx="300" cy="65" r="26" fill="#334155" stroke="#38bdf8" stroke-width="3"/>
      <line x1="274" y1="65" x2="274" y2="145" stroke="#fbbf24" stroke-width="3"/>
      <rect x="250" y="145" width="48" height="34" rx="4" fill="#0ea5e9" stroke="#bae6fd"/>
      <text x="274" y="166" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">100 N</text>
      <line x1="326" y1="65" x2="326" y2="165" stroke="#fbbf24" stroke-width="3"/>
      <polygon points="326,175 319,161 333,161" fill="#34d399"/>
      <text x="342" y="135" fill="#6ee7b7" font-size="12" font-weight="bold">Effort = 100 N (Down)</text>
      <text x="300" y="215" text-anchor="middle" fill="#7dd3fc" font-size="13" font-weight="bold">Fixed Pulley: Changes direction only (MA = 100 / 100 = 1)</text>
    </g>
    <g id="c7s9_movable" style="display:none">
      <line x1="220" y1="25" x2="380" y2="25" stroke="#94a3b8" stroke-width="5"/>
      <line x1="274" y1="25" x2="274" y2="115" stroke="#fbbf24" stroke-width="3"/>
      <circle cx="300" cy="115" r="26" fill="#334155" stroke="#34d399" stroke-width="3"/>
      <line x1="326" y1="115" x2="326" y2="42" stroke="#fbbf24" stroke-width="3"/>
      <polygon points="326,34 319,48 333,48" fill="#34d399"/>
      <rect x="276" y="148" width="48" height="34" rx="4" fill="#10b981" stroke="#a7f3d0"/>
      <text x="300" y="169" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">100 N</text>
      <text x="345" y="75" fill="#6ee7b7" font-size="12" font-weight="bold">Effort = 50 N (Up)</text>
      <text x="300" y="215" text-anchor="middle" fill="#34d399" font-size="13" font-weight="bold">Movable Pulley: Two ropes share load (MA = 100 / 50 = 2 &gt; 1)</text>
    </g>
  </svg>
</div>
<script>
window.setC7S9 = function(t){
  document.getElementById('c7s9_fixed').style.display = (t==='fixed'?'block':'none');
  document.getElementById('c7s9_movable').style.display = (t==='movable'?'block':'none');
};
</script>""",

    10: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Activity 7.3 &amp; Ex 7.12 Inclined Plane (MA = L / h)</span>
    <div class="flex items-center gap-3">
      <label class="text-xs text-slate-300">Length L: <b id="c7s10_l_lbl" class="text-cyan-300">50 cm</b></label>
      <input type="range" min="35" max="90" step="5" value="50" id="c7s10_l" oninput="updC7S10()" class="w-24 accent-cyan-400">
      <label class="text-xs text-slate-300">Height h: <b id="c7s10_h_lbl" class="text-amber-300">30 cm</b></label>
      <input type="range" min="15" max="35" step="5" value="30" id="c7s10_h" oninput="updC7S10()" class="w-20 accent-amber-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <polygon id="c7s10_tri" points="140,185 440,185 440,95" fill="rgba(56,189,248,0.22)" stroke="#38bdf8" stroke-width="3"/>
    <text id="c7s10_ma" x="300" y="42" text-anchor="middle" fill="#6ee7b7" font-size="17" font-weight="bold">Ex 7.12: MA = L / h = 50 / 30 = 1.67</text>
    <text id="c7s10_eff" x="300" y="65" text-anchor="middle" fill="#fde047" font-size="13">Gentler slope = longer ramp L = smaller pulling Effort!</text>
    <text x="300" y="216" text-anchor="middle" fill="#94a3b8" font-size="11">Ideal Work: Effort &times; L = Load &times; h (Work is conserved)</text>
  </svg>
</div>
<script>
window.updC7S10 = function(){
  let L = parseInt(document.getElementById('c7s10_l').value,10);
  const h = parseInt(document.getElementById('c7s10_h').value,10);
  if(L <= h) L = h + 5;
  const ma = L / h;
  document.getElementById('c7s10_l_lbl').textContent = L + ' cm';
  document.getElementById('c7s10_h_lbl').textContent = h + ' cm';
  document.getElementById('c7s10_ma').textContent = 'MA = L / h = ' + L + ' / ' + h + ' = ' + ma.toFixed(2);
  const base = Math.sqrt(L*L - h*h) * 4.2;
  const xStart = Math.max(70, 460 - base);
  const yTop = 185 - h * 3;
  document.getElementById('c7s10_tri').setAttribute('points', xStart+',185 460,185 460,'+yTop);
};
</script>""",

    11: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Ex 7.13 Seesaw &amp; Principle of Moments (F&#8321;d&#8321; = F&#8322;d&#8322;)</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">15 kg child d&#8321;: <b id="c7s11_d" class="text-amber-300">2.0 m</b></label>
      <input type="range" min="0.5" max="3.0" step="0.5" value="2.0" id="c7s11_sl" oninput="updC7S11()" class="w-28 accent-amber-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <polygon points="300,145 275,185 325,185" fill="#f59e0b" stroke="#fde68a" stroke-width="2"/>
    <g id="c7s11_bar" transform="rotate(0 300 145)">
      <rect x="110" y="136" width="380" height="10" rx="4" fill="#38bdf8"/>
      <rect x="215" y="106" width="34" height="30" rx="4" fill="#ef4444" stroke="#fecaca"/>
      <text x="232" y="125" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">30kg</text>
      <rect id="c7s11_c2" x="430" y="112" width="28" height="24" rx="4" fill="#10b981" stroke="#a7f3d0"/>
      <text id="c7s11_c2t" x="444" y="128" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">15kg</text>
    </g>
    <text id="c7s11_stat" x="300" y="45" text-anchor="middle" fill="#6ee7b7" font-size="16" font-weight="bold">BALANCED! 30 kg &times; 1.0 m = 15 kg &times; 2.0 m</text>
    <text x="300" y="216" text-anchor="middle" fill="#94a3b8" font-size="12">Mechanical Advantage of Lever: MA = Effort Arm (L&#8321;) / Load Arm (L&#8322;)</text>
  </svg>
</div>
<script>
window.updC7S11 = function(){
  const d1 = parseFloat(document.getElementById('c7s11_sl').value);
  document.getElementById('c7s11_d').textContent = d1.toFixed(1) + ' m';
  const x2 = 300 + d1 * 65 - 14;
  document.getElementById('c7s11_c2').setAttribute('x', x2);
  document.getElementById('c7s11_c2t').setAttribute('x', x2 + 14);
  const diff = (15 * d1) - (30 * 1.0);
  const ang = Math.max(-12, Math.min(12, diff * 0.6));
  document.getElementById('c7s11_bar').setAttribute('transform', 'rotate(' + ang + ' 300 145)');
  const st = document.getElementById('c7s11_stat');
  if(Math.abs(diff) < 0.1){
    st.textContent = 'BALANCED! 30 kg x 1.0 m = 15 kg x 2.0 m (MA = 2)';
    st.setAttribute('fill','#6ee7b7');
  } else {
    st.textContent = 'UNBALANCED: 30x1 = 30 vs 15x' + d1.toFixed(1) + ' = ' + (15*d1).toFixed(1);
    st.setAttribute('fill','#fbbf24');
  }
};
</script>""",

    12: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-cyan-300 uppercase">Table 7.2 Classes of Levers (Mnemonic: F - L - E)</span>
    <div class="flex gap-1.5">
      <button onclick="setC7S12(1)" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Class I (F mid)</button>
      <button onclick="setC7S12(2)" class="px-2.5 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Class II (L mid)</button>
      <button onclick="setC7S12(3)" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Class III (E mid)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="90" y="115" width="420" height="10" rx="4" fill="#94a3b8"/>
    <circle id="c7s12_f" cx="300" cy="120" r="14" fill="#f59e0b"/>
    <text id="c7s12_ft" x="300" y="124" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="bold">F</text>
    <circle id="c7s12_l" cx="140" cy="120" r="14" fill="#ef4444"/>
    <text id="c7s12_lt" x="140" y="124" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold">L</text>
    <circle id="c7s12_e" cx="460" cy="120" r="14" fill="#10b981"/>
    <text id="c7s12_et" x="460" y="124" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold">E</text>
    <text id="c7s12_title" x="300" y="55" text-anchor="middle" fill="#fde047" font-size="17" font-weight="bold">Class I Lever: Fulcrum (F) in the Middle</text>
    <text id="c7s12_ex" x="300" y="175" text-anchor="middle" fill="#cbd5e1" font-size="13">Examples: Seesaw, Crowbar, Scissors, Pliers</text>
    <text id="c7s12_ma" x="300" y="202" text-anchor="middle" fill="#7dd3fc" font-size="12" font-weight="bold">MA can be &lt; 1, = 1, or &gt; 1 depending on fulcrum position</text>
  </svg>
</div>
<script>
window.setC7S12 = function(cls){
  const pos = cls===1 ? {f:300,l:140,e:460} : (cls===2 ? {f:140,l:300,e:460} : {f:140,e:300,l:460});
  document.getElementById('c7s12_f').setAttribute('cx',pos.f); document.getElementById('c7s12_ft').setAttribute('x',pos.f);
  document.getElementById('c7s12_l').setAttribute('cx',pos.l); document.getElementById('c7s12_lt').setAttribute('x',pos.l);
  document.getElementById('c7s12_e').setAttribute('cx',pos.e); document.getElementById('c7s12_et').setAttribute('x',pos.e);
  if(cls===1){
    document.getElementById('c7s12_title').textContent='Class I Lever: Fulcrum (F) in the Middle';
    document.getElementById('c7s12_ex').textContent='Examples: Seesaw, Crowbar, Scissors, Pliers';
    document.getElementById('c7s12_ma').textContent='MA can be < 1, = 1, or > 1 depending on fulcrum position';
  } else if(cls===2){
    document.getElementById('c7s12_title').textContent='Class II Lever: Load (L) in the Middle';
    document.getElementById('c7s12_ex').textContent='Examples: Wheelbarrow, Lemon Squeezer, Bottle Opener';
    document.getElementById('c7s12_ma').textContent='Effort Arm > Load Arm ALWAYS -> MA is ALWAYS > 1';
  } else {
    document.getElementById('c7s12_title').textContent='Class III Lever: Effort (E) in the Middle';
    document.getElementById('c7s12_ex').textContent='Examples: Kitchen Tongs, Tweezers, Broom, Boat Oar';
    document.getElementById('c7s12_ma').textContent='Effort Arm < Load Arm ALWAYS -> MA < 1 (Gains Speed & Precision)';
  }
};
</script>""",

    13: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Himalayan Gharat (Panchakki) &amp; Hydroelectric Dam</span>
    <div class="flex gap-2">
      <button onclick="setC7S13('gharat')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Traditional Gharat</button>
      <button onclick="setC7S13('dam')" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Hydroelectric Dam</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="50" y="65" width="130" height="55" rx="8" fill="#0284c7" stroke="#7dd3fc" stroke-width="2"/>
    <text x="115" y="90" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold">Elevated Water</text>
    <text x="115" y="106" text-anchor="middle" fill="#bae6fd" font-size="11">High U = mgh</text>
    <line x1="185" y1="95" x2="275" y2="140" stroke="#38bdf8" stroke-width="6"/>
    <circle cx="305" cy="145" r="28" fill="#334155" stroke="#fbbf24" stroke-width="3"/>
    <text x="305" y="149" text-anchor="middle" fill="#fde047" font-size="11" font-weight="bold">Wheel</text>
    <line x1="305" y1="115" x2="305" y2="70" stroke="#cbd5e1" stroke-width="4"/>
    <rect id="c7s13_top" x="265" y="40" width="80" height="30" rx="6" fill="#d97706" stroke="#fde68a"/>
    <text id="c7s13_toplbl" x="305" y="59" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">Millstone</text>
    <text id="c7s13_chain" x="300" y="208" text-anchor="middle" fill="#6ee7b7" font-size="13" font-weight="bold">Gharat: Stream U (mgh) -> Chute K -> Wheel +W -> Grinds Wheat &amp; Spices!</text>
  </svg>
</div>
<script>
window.setC7S13 = function(mode){
  if(mode==='gharat'){
    document.getElementById('c7s13_toplbl').textContent = 'Millstone';
    document.getElementById('c7s13_chain').textContent = 'Gharat: Stream U (mgh) -> Chute K -> Wheel +W -> Grinds Wheat & Spices!';
  } else {
    document.getElementById('c7s13_toplbl').textContent = 'Generator';
    document.getElementById('c7s13_chain').textContent = 'Hydro Dam: Reservoir U -> Penstock K -> Steel Turbine -> Clean Electricity!';
  }
};
</script>""",

    14: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-purple-300 uppercase">DIY Launcher &amp; Cosmic Dark Energy</span>
    <div class="flex gap-2">
      <button onclick="setC7S14('diy')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">DIY Pen Launcher</button>
      <button onclick="setC7S14('cos')" class="px-2.5 py-1 rounded bg-purple-600/30 text-xs text-purple-200 border border-purple-500/40">Cosmic Dark Energy</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="c7s14_diy">
      <rect x="100" y="105" width="90" height="30" rx="6" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
      <path d="M 110 120 L 125 110 L 140 130 L 155 110 L 170 130 L 185 120" fill="none" stroke="#fbbf24" stroke-width="3"/>
      <line x1="210" y1="120" x2="430" y2="120" stroke="#38bdf8" stroke-width="4" stroke-dasharray="6,4"/>
      <polygon points="445,120 420,112 420,128" fill="#38bdf8"/>
      <text x="300" y="55" text-anchor="middle" fill="#fde047" font-size="16" font-weight="bold">DIY Pen-Refill Launcher: Elastic U -&gt; Kinetic K</text>
      <text x="300" y="185" text-anchor="middle" fill="#cbd5e1" font-size="12">Explore PhET Energy Skate Park to track K, U &amp; Thermal energy bars live!</text>
    </g>
    <g id="c7s14_cos" style="display:none">
      <circle cx="300" cy="120" r="24" fill="#a855f7" stroke="#e9d5ff" stroke-width="2"/>
      <circle cx="150" cy="95" r="14" fill="#38bdf8"/>
      <circle cx="450" cy="145" r="14" fill="#38bdf8"/>
      <line x1="260" y1="115" x2="175" y2="100" stroke="#c084fc" stroke-width="3"/>
      <polygon points="168,99 182,95 180,108" fill="#c084fc"/>
      <line x1="340" y1="125" x2="425" y2="140" stroke="#c084fc" stroke-width="3"/>
      <polygon points="432,141 418,145 420,132" fill="#c084fc"/>
      <text x="300" y="45" text-anchor="middle" fill="#d8b4fe" font-size="16" font-weight="bold">The Quest Continues: Accelerating Cosmic Expansion</text>
      <text x="300" y="198" text-anchor="middle" fill="#cbd5e1" font-size="12">Galaxies accelerate apart instead of slowing down &mdash; attributed to Dark Energy!</text>
    </g>
  </svg>
</div>
<script>
window.setC7S14 = function(m){
  document.getElementById('c7s14_diy').style.display = (m==='diy'?'block':'none');
  document.getElementById('c7s14_cos').style.display = (m==='cos'?'block':'none');
};
</script>""",

    15: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Revise, Reflect, Refine: Path Independence &amp; Triangle F-s</span>
    <div class="flex gap-2">
      <button onclick="setC7S15('path')" class="px-2.5 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Path Independence</button>
      <button onclick="setC7S15('tri')" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Spring Triangle Area</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="c7s15_path">
      <line x1="170" y1="180" x2="170" y2="65" stroke="#38bdf8" stroke-width="5"/>
      <text x="155" y="125" text-anchor="end" fill="#7dd3fc" font-size="12">4 m Ladder</text>
      <polyline points="350,180 390,150 430,120 470,90 510,65" fill="none" stroke="#fbbf24" stroke-width="4"/>
      <text x="455" y="145" fill="#fde047" font-size="12">12 m Winding Stairs</text>
      <line x1="130" y1="65" x2="530" y2="65" stroke="#34d399" stroke-width="2" stroke-dasharray="5,4"/>
      <text x="300" y="38" text-anchor="middle" fill="#6ee7b7" font-size="15" font-weight="bold">Gravitational Work W = mgh = 5 &times; 10 &times; 4 = 200 J (Both Paths!)</text>
      <text x="300" y="214" text-anchor="middle" fill="#cbd5e1" font-size="12">Depends ONLY on vertical height h, NOT path length!</text>
    </g>
    <g id="c7s15_tri" style="display:none">
      <line x1="160" y1="180" x2="460" y2="180" stroke="#94a3b8" stroke-width="2"/>
      <line x1="160" y1="180" x2="160" y2="55" stroke="#94a3b8" stroke-width="2"/>
      <polygon points="160,180 410,180 410,70" fill="rgba(56,189,248,0.3)" stroke="#38bdf8" stroke-width="3"/>
      <text x="285" y="202" text-anchor="middle" fill="#cbd5e1" font-size="12">s = 6 m</text>
      <text x="425" y="125" fill="#fde047" font-size="12">F = 20 N</text>
      <text x="300" y="38" text-anchor="middle" fill="#6ee7b7" font-size="15" font-weight="bold">Triangle Area = &frac12; &times; 6 m &times; 20 N = 60 J</text>
    </g>
  </svg>
</div>
<script>
window.setC7S15 = function(m){
  document.getElementById('c7s15_path').style.display = (m==='path'?'block':'none');
  document.getElementById('c7s15_tri').style.display = (m==='tri'?'block':'none');
};
</script>""",

    16: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-emerald-300 uppercase">At a Glance: Chapter 7 Formula Toolkit</span>
    <div class="flex gap-1.5 flex-wrap">
      <button onclick="setC7S16('work')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Work</button>
      <button onclick="setC7S16('energy')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Energy</button>
      <button onclick="setC7S16('power')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Power</button>
      <button onclick="setC7S16('mach')" class="px-2 py-1 rounded bg-purple-600/30 text-xs text-purple-200 border border-purple-500/40">Machines</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="145" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text id="c7s16_h" x="300" y="88" text-anchor="middle" fill="#fbbf24" font-size="20" font-weight="bold">W = F &times; s (SI Unit: Joule, 1 J = 1 N&middot;m)</text>
    <text id="c7s16_b1" x="300" y="124" text-anchor="middle" fill="#cbd5e1" font-size="13">Zero Work: F = 0, s = 0, or Force &perp; Displacement (90&deg;)</text>
    <text id="c7s16_b2" x="300" y="152" text-anchor="middle" fill="#6ee7b7" font-size="13">Work-Energy Theorem: Net Work Done = &Delta;Energy</text>
  </svg>
</div>
<script>
window.setC7S16 = function(k){
  const h = document.getElementById('c7s16_h');
  const b1 = document.getElementById('c7s16_b1');
  const b2 = document.getElementById('c7s16_b2');
  if(k==='work'){
    h.textContent = 'W = F x s (SI Unit: Joule, 1 J = 1 N.m)';
    b1.textContent = 'Zero Work: F = 0, s = 0, or Force perpendicular (90 deg)';
    b2.textContent = 'Work-Energy Theorem: Net Work Done = Change in Energy';
  } else if(k==='energy'){
    h.textContent = 'K = 1/2 m v^2  |  U = m g h  |  ME = K + U';
    b1.textContent = 'Conservative forces conserve total Mechanical Energy ME';
    b2.textContent = 'Pendulum & Free Fall: loss in U equals gain in K';
  } else if(k==='power'){
    h.textContent = 'P = W / t (SI Unit: Watt, 1 W = 1 J/s)';
    b1.textContent = '1 Horsepower (hp) = 746 Watts (James Watt)';
    b2.textContent = 'Power measures how fast work is done or energy transfers';
  } else {
    h.textContent = 'MA = Load / Effort (Simple Machines)';
    b1.textContent = 'Fixed Pulley MA = 1 | Movable MA > 1 | Inclined Plane MA = L/h';
    b2.textContent = 'Levers: F1 d1 = F2 d2 | Classes I (F), II (L), III (E)';
  }
};
</script>"""
}
