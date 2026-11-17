#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sims_part1 = {
    1: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Acoustic Energy &amp; Spacewalk Inquiry</span>
    <div class="flex gap-2">
      <button onclick="setC10S1('earth')" class="px-2.5 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Earth (Air Medium)</button>
      <button onclick="setC10S1('space')" class="px-2.5 py-1 rounded bg-purple-600/30 text-xs text-purple-200 border border-purple-500/40">Space (Vacuum)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="c10s1_earth">
      <circle cx="160" cy="115" r="32" fill="#0284c7" stroke="#7dd3fc" stroke-width="2"/>
      <text x="160" y="120" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold">Source</text>
      <circle cx="230" cy="115" r="50" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6,4"/>
      <circle cx="280" cy="115" r="80" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6,4"/>
      <circle cx="330" cy="115" r="110" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6,4"/>
      <circle cx="440" cy="115" r="32" fill="#059669" stroke="#a7f3d0" stroke-width="2"/>
      <text x="440" y="120" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold">Listener</text>
      <text x="300" y="200" text-anchor="middle" fill="#6ee7b7" font-size="14" font-weight="bold">Air Medium Present: Sound waves propagate via particle collisions!</text>
    </g>
    <g id="c10s1_space" style="display:none">
      <circle cx="160" cy="115" r="32" fill="#6366f1" stroke="#c7d2fe" stroke-width="2"/>
      <text x="160" y="120" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">Astronaut 1</text>
      <line x1="220" y1="115" x2="380" y2="115" stroke="#f43f5e" stroke-width="3" stroke-dasharray="4,4"/>
      <circle cx="300" cy="115" r="24" fill="none" stroke="#f43f5e" stroke-width="3"/>
      <line x1="283" y1="98" x2="317" y2="132" stroke="#f43f5e" stroke-width="3"/>
      <circle cx="440" cy="115" r="32" fill="#6366f1" stroke="#c7d2fe" stroke-width="2"/>
      <text x="440" y="120" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">Astronaut 2</text>
      <text x="300" y="200" text-anchor="middle" fill="#fda4af" font-size="14" font-weight="bold">Vacuum in Space: No matter particles &rarr; Complete acoustic silence!</text>
    </g>
  </svg>
</div>
<script>
window.setC10S1 = function(m){
  document.getElementById('c10s1_earth').style.display = (m==='earth'?'block':'none');
  document.getElementById('c10s1_space').style.display = (m==='space'?'block':'none');
};
</script>""",

    2: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Activity 10.1: Plucked Rubber Band Tension</span>
    <div class="flex items-center gap-3">
      <label class="text-xs text-slate-300">Tension: <b id="c10s2_lbl" class="text-amber-300">Medium</b></label>
      <input type="range" min="1" max="3" step="1" value="2" id="c10s2_sl" oninput="updC10S2()" class="w-24 accent-amber-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="180" y="80" width="240" height="90" rx="8" fill="#78350f" stroke="#fde68a" stroke-width="2"/>
    <path id="c10s2_band" d="M 180 125 Q 300 100 420 125" fill="none" stroke="#38bdf8" stroke-width="4"/>
    <text id="c10s2_freq" x="300" y="55" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="bold">Vibrating Band &rarr; Producing Audible Humming Note</text>
    <text x="300" y="205" text-anchor="middle" fill="#cbd5e1" font-size="12">Sound is produced strictly by vibrating bodies (strings, vocal cords, membranes)</text>
  </svg>
</div>
<script>
window.updC10S2 = function(){
  const v = parseInt(document.getElementById('c10s2_sl').value, 10);
  const band = document.getElementById('c10s2_band');
  const lbl = document.getElementById('c10s2_lbl');
  const fr = document.getElementById('c10s2_freq');
  if(v===1){
    lbl.textContent = 'Low (Loose)';
    band.setAttribute('d', 'M 180 125 Q 300 90 420 125');
    fr.textContent = 'Low Tension: Slower vibration &rarr; Deeper bass sound';
  } else if(v===2){
    lbl.textContent = 'Medium';
    band.setAttribute('d', 'M 180 125 Q 300 105 420 125');
    fr.textContent = 'Medium Tension: Standard hum note';
  } else {
    lbl.textContent = 'High (Tight)';
    band.setAttribute('d', 'M 180 125 Q 300 115 420 125');
    fr.textContent = 'High Tension: Rapid vibration &rarr; High pitch note!';
  }
};
</script>""",

    3: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Activity 10.2: Tuning Fork &amp; Water Splashes</span>
    <div class="flex gap-2">
      <button onclick="setC10S3('rest')" class="px-2.5 py-1 rounded bg-slate-700 text-xs text-slate-200 border border-slate-500">Tuning Fork Rest</button>
      <button onclick="setC10S3('splash')" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Strike &amp; Touch Water</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <path d="M 270 50 L 270 120 Q 270 145 300 145 Q 330 145 330 120 L 330 50" fill="none" stroke="#94a3b8" stroke-width="8"/>
    <line x1="300" y1="145" x2="300" y2="195" stroke="#94a3b8" stroke-width="8"/>
    <rect x="200" y="140" width="200" height="60" rx="8" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2"/>
    <g id="c10s3_spr" style="display:none">
      <circle cx="260" cy="130" r="5" fill="#38bdf8"/>
      <circle cx="340" cy="130" r="5" fill="#38bdf8"/>
      <circle cx="240" cy="115" r="4" fill="#38bdf8"/>
      <circle cx="360" cy="115" r="4" fill="#38bdf8"/>
      <ellipse cx="300" cy="140" rx="80" ry="12" fill="none" stroke="#7dd3fc" stroke-width="2"/>
    </g>
    <text id="c10s3_txt" x="300" y="32" text-anchor="middle" fill="#7dd3fc" font-size="14" font-weight="bold">Standard Tuning Fork: 2 Parallel Prongs (Tines) + Stem</text>
    <text x="300" y="222" text-anchor="middle" fill="#cbd5e1" font-size="11">Jingrwai Iawbei in Kongthong (Meghalaya): Whistled tune names echo across hills</text>
  </svg>
</div>
<script>
window.setC10S3 = function(m){
  const spr = document.getElementById('c10s3_spr');
  const txt = document.getElementById('c10s3_txt');
  if(m==='splash'){
    spr.style.display = 'block';
    txt.textContent = 'Prong Vibrations Transfer Kinetic Energy &rarr; Water Splashes Outward!';
  } else {
    spr.style.display = 'none';
    txt.textContent = 'Standard Tuning Fork: 2 Parallel Prongs (Tines) + Stem';
  }
};
</script>""",

    4: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Bell Jar: Sound Cannot Propagate in a Vacuum</span>
    <div class="flex gap-2">
      <button onclick="setC10S4('air')" class="px-2.5 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Air Inside (Normal)</button>
      <button onclick="setC10S4('vac')" class="px-2.5 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">Evacuate Air (Vacuum)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <path d="M 230 190 L 230 90 Q 230 40 300 40 Q 370 40 370 90 L 370 190" fill="none" stroke="#64748b" stroke-width="4"/>
    <line x1="200" y1="190" x2="400" y2="190" stroke="#94a3b8" stroke-width="6"/>
    <circle cx="300" cy="110" r="18" fill="#fbbf24"/>
    <g id="c10s4_waves">
      <circle cx="300" cy="110" r="34" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
      <circle cx="300" cy="110" r="50" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
    </g>
    <text id="c10s4_stat" x="300" y="215" text-anchor="middle" fill="#6ee7b7" font-size="14" font-weight="bold">Air Present: Bell Ringing Heard Clearly (Mechanical Wave Propagates)</text>
  </svg>
</div>
<script>
window.setC10S4 = function(m){
  const w = document.getElementById('c10s4_waves');
  const s = document.getElementById('c10s4_stat');
  if(m==='vac'){
    w.style.display = 'none';
    s.textContent = 'Vacuum Pump ON: Air Removed &rarr; Complete Silence (No Sound in Vacuum!)';
    s.setAttribute('fill','#fda4af');
  } else {
    w.style.display = 'block';
    s.textContent = 'Air Present: Bell Ringing Heard Clearly (Mechanical Wave Propagates)';
    s.setAttribute('fill','#6ee7b7');
  }
};
</script>""",

    5: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Longitudinal Sound Wave: Compressions &amp; Rarefactions</span>
    <div class="flex gap-2">
      <button onclick="setC10S5('step1')" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Piston Forward (C)</button>
      <button onclick="setC10S5('step2')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Piston Backward (R)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="80" y="70" width="460" height="90" fill="none" stroke="#64748b" stroke-width="2"/>
    <rect id="c10s5_pist" x="80" y="66" width="18" height="98" fill="#f43f5e"/>
    <g id="c10s5_dots">
      <line x1="130" y1="75" x2="130" y2="155" stroke="#38bdf8" stroke-width="6"/>
      <line x1="140" y1="75" x2="140" y2="155" stroke="#38bdf8" stroke-width="6"/>
      <line x1="150" y1="75" x2="150" y2="155" stroke="#38bdf8" stroke-width="6"/>
      <line x1="210" y1="75" x2="210" y2="155" stroke="#64748b" stroke-width="2"/>
      <line x1="270" y1="75" x2="270" y2="155" stroke="#64748b" stroke-width="2"/>
      <line x1="330" y1="75" x2="330" y2="155" stroke="#38bdf8" stroke-width="6"/>
      <line x1="340" y1="75" x2="340" y2="155" stroke="#38bdf8" stroke-width="6"/>
      <line x1="350" y1="75" x2="350" y2="155" stroke="#38bdf8" stroke-width="6"/>
      <line x1="410" y1="75" x2="410" y2="155" stroke="#64748b" stroke-width="2"/>
      <line x1="470" y1="75" x2="470" y2="155" stroke="#38bdf8" stroke-width="6"/>
    </g>
    <text x="140" y="55" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="bold">Compression (C)</text>
    <text x="240" y="55" text-anchor="middle" fill="#94a3b8" font-size="14">Rarefaction (R)</text>
    <text x="340" y="55" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="bold">Compression (C)</text>
    <text x="300" y="200" text-anchor="middle" fill="#fde047" font-size="13" font-weight="bold">Longitudinal: Medium particles oscillate parallel to wave motion axis</text>
  </svg>
</div>
<script>
window.setC10S5 = function(st){
  const p = document.getElementById('c10s5_pist');
  if(st==='step1'){
    p.setAttribute('x','100');
  } else {
    p.setAttribute('x','70');
  }
};
</script>""",

    6: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Activity 10.6: Acoustic Energy &amp; Jumping Rice Grains</span>
    <div class="flex gap-2">
      <button onclick="setC10S6(false)" class="px-2.5 py-1 rounded bg-slate-700 text-xs text-slate-200 border border-slate-500">Quiet</button>
      <button onclick="setC10S6(true)" class="px-2.5 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Loud Strike (Spoon &amp; Tray)</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="220" y="110" width="160" height="70" rx="4" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <ellipse cx="300" cy="110" rx="80" ry="16" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <g id="c10s6_grains">
      <circle cx="280" cy="108" r="3" fill="#f8fafc"/><circle cx="300" cy="106" r="3" fill="#f8fafc"/><circle cx="320" cy="109" r="3" fill="#f8fafc"/>
      <circle cx="260" cy="110" r="3" fill="#f8fafc"/><circle cx="340" cy="110" r="3" fill="#f8fafc"/>
    </g>
    <text id="c10s6_st" x="300" y="60" text-anchor="middle" fill="#cbd5e1" font-size="14">Rice grains at rest on stretched rubber membrane</text>
    <text x="300" y="210" text-anchor="middle" fill="#6ee7b7" font-size="12">Microphones convert sound &rarr; electricity | Speakers convert electricity &rarr; sound</text>
  </svg>
</div>
<script>
window.setC10S6 = function(loud){
  const g = document.getElementById('c10s6_grains');
  const s = document.getElementById('c10s6_st');
  if(loud){
    g.setAttribute('transform', 'translate(0, -26)');
    s.textContent = 'Loud Sound Wave Strikes: Rice grains jump vigorously via kinetic energy transfer!';
    s.setAttribute('fill', '#fde047');
  } else {
    g.setAttribute('transform', 'translate(0, 0)');
    s.textContent = 'Quiet: Rice grains at rest on stretched rubber membrane';
    s.setAttribute('fill', '#cbd5e1');
  }
};
</script>""",

    7: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Section 10.5 Density-Distance Graph of Sound Wave</span>
    <span class="text-xs text-slate-400">Spatial Waveform Model</span>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="60" y1="120" x2="540" y2="120" stroke="#64748b" stroke-width="2" stroke-dasharray="6,4"/>
    <text x="545" y="124" fill="#94a3b8" font-size="11">Average Density</text>
    <path d="M 60 120 Q 120 40 180 120 Q 240 200 300 120 Q 360 40 420 120 Q 480 200 540 120" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <circle cx="120" cy="40" r="6" fill="#fbbf24"/>
    <text x="120" y="28" text-anchor="middle" fill="#fde047" font-size="12" font-weight="bold">Crest (Compression)</text>
    <circle cx="240" cy="200" r="6" fill="#f43f5e"/>
    <text x="240" y="222" text-anchor="middle" fill="#fda4af" font-size="12" font-weight="bold">Trough (Rarefaction)</text>
    <line x1="120" y1="40" x2="360" y2="40" stroke="#34d399" stroke-width="2"/>
    <text x="240" y="34" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">Wavelength (&lambda;)</text>
  </svg>
</div>""",

    8: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Wavelength &lambda;, Frequency &nu; = 1/T &amp; Time Period T</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Oscillations: <b id="c10s8_n" class="text-cyan-300">10</b></label>
      <input type="range" min="4" max="20" step="2" value="10" id="c10s8_sl" oninput="updC10S8()" class="w-24 accent-amber-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <text id="c10s8_fr" x="300" y="70" text-anchor="middle" fill="#6ee7b7" font-size="22" font-weight="bold">Example 10.1: &nu; = 10 / 2 s = 5.0 Hz</text>
    <text id="c10s8_tp" x="300" y="115" text-anchor="middle" fill="#fbbf24" font-size="20" font-weight="bold">Time Period T = 1 / &nu; = 0.20 s</text>
    <text x="300" y="165" text-anchor="middle" fill="#cbd5e1" font-size="13">Activity 10.7 (Phyphox): Analyzing Indian vocal scale frequencies (Sa, Re, Ga, Ma...)</text>
    <text x="300" y="195" text-anchor="middle" fill="#94a3b8" font-size="11">Frequency SI Unit: Hertz (Hz = s&#8315;&sup1;) | Time Period SI Unit: Second (s)</text>
  </svg>
</div>
<script>
window.updC10S8 = function(){
  const n = parseInt(document.getElementById('c10s8_sl').value, 10);
  const nu = n / 2;
  const t = 1 / nu;
  document.getElementById('c10s8_n').textContent = n;
  document.getElementById('c10s8_fr').textContent = 'Frequency &nu; = ' + n + ' / 2 s = ' + nu.toFixed(1) + ' Hz';
  document.getElementById('c10s8_tp').textContent = 'Time Period T = 1 / &nu; = ' + t.toFixed(2) + ' s';
};
</script>"""
}
