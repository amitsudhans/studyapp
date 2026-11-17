#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sims_part2 = {
    9: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Amplitude &amp; Intensity (Energy &prop; A&sup2; &amp; I &prop; 1/r&sup2;)</span>
    <div class="flex items-center gap-3">
      <label class="text-xs text-slate-300">Amplitude A: <b id="c10s9_a_lbl" class="text-cyan-300">2x</b></label>
      <input type="range" min="1" max="4" step="1" value="2" id="c10s9_sl" oninput="updC10S9()" class="w-24 accent-cyan-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="60" y1="120" x2="540" y2="120" stroke="#64748b" stroke-width="2" stroke-dasharray="6,4"/>
    <path id="c10s9_wave" d="M 60 120 Q 120 40 180 120 Q 240 200 300 120 Q 360 40 420 120 Q 480 200 540 120" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <text id="c10s9_en" x="300" y="35" text-anchor="middle" fill="#6ee7b7" font-size="16" font-weight="bold">Amplitude = 2 &rarr; Wave Energy = 2&sup2; = 4x (Energy &prop; A&sup2;)</text>
    <text x="300" y="215" text-anchor="middle" fill="#fde047" font-size="12">Spherical Spreading: Sound intensity drops with distance square (I &prop; 1/r&sup2;)</text>
  </svg>
</div>
<script>
window.updC10S9 = function(){
  const a = parseInt(document.getElementById('c10s9_sl').value, 10);
  const dy = a * 25;
  document.getElementById('c10s9_a_lbl').textContent = a + 'x';
  const p = 'M 60 120 Q 120 '+(120-dy)+' 180 120 Q 240 '+(120+dy)+' 300 120 Q 360 '+(120-dy)+' 420 120 Q 480 '+(120+dy)+' 540 120';
  document.getElementById('c10s9_wave').setAttribute('d', p);
  document.getElementById('c10s9_en').textContent = 'Amplitude = ' + a + 'x -> Wave Energy = ' + (a*a) + 'x (Energy &prop; A&sup2;)';
};
</script>""",

    10: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-cyan-300 uppercase">Speed of Sound: v = &lambda;&nu; &amp; Lightning Calculator</span>
    <div class="flex gap-1.5">
      <button onclick="setC10S10('ex2')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Ex 10.2 Wavelengths</button>
      <button onclick="setC10S10('ex3')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Ex 10.3 Lightning</button>
      <button onclick="setC10S10('ex4')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Ex 10.4 Steel Rod</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="145" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text id="c10s10_h" x="300" y="90" text-anchor="middle" fill="#fbbf24" font-size="20" font-weight="bold">Ex 10.2: Human Hearing Limits (v = 344 m/s)</text>
    <text id="c10s10_b1" x="300" y="128" text-anchor="middle" fill="#cbd5e1" font-size="13">20 Hz &rarr; &lambda; = 344 / 20 = 17.2 m  |  20 kHz &rarr; &lambda; = 1.72 cm</text>
    <text id="c10s10_b2" x="300" y="158" text-anchor="middle" fill="#6ee7b7" font-size="13">Speed in media: Air ~344 m/s &lt; Water ~1530 m/s &lt; Steel ~5000 m/s</text>
  </svg>
</div>
<script>
window.setC10S10 = function(k){
  const m = {
    ex2: ['Ex 10.2: Human Hearing Limits (v = 344 m/s)', '20 Hz -> &lambda; = 344 / 20 = 17.2 m  |  20 kHz -> &lambda; = 1.72 cm', 'Speed in media: Air ~344 m/s < Water ~1530 m/s < Steel ~5000 m/s'],
    ex3: ['Ex 10.3: Thunder Delay (t = 5 s, v = 340 m/s)', 'Distance = v x t = 340 m/s x 5 s = 1700 m = 1.7 km', 'Light travels at 3x10^8 m/s (instant flash); sound follows!'],
    ex4: ['Ex 10.4: Sound in Steel Rod (v = 5000 m/s, &lambda; = 50 m)', 'Frequency &nu; = v / &lambda; = 5000 / 50 = 100 Hz', 'Time period T = 1 / &nu; = 1 / 100 = 0.01 s']
  };
  document.getElementById('c10s10_h').textContent = m[k][0];
  document.getElementById('c10s10_b1').textContent = m[k][1];
  document.getElementById('c10s10_b2').textContent = m[k][2];
};
</script>""",

    11: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-emerald-300 uppercase">Perception &amp; C. V. Raman's Acoustics</span>
    <div class="flex gap-1.5">
      <button onclick="setC10S11('pitch')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Pitch vs Loudness</button>
      <button onclick="setC10S11('ear')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Human Ear Anatomy</button>
      <button onclick="setC10S11('raman')" class="px-2 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">C. V. Raman Tabla</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="145" rx="14" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text id="c10s11_h" x="300" y="90" text-anchor="middle" fill="#fbbf24" font-size="20" font-weight="bold">Pitch = Frequency | Loudness = Amplitude (dB)</text>
    <text id="c10s11_b1" x="300" y="128" text-anchor="middle" fill="#cbd5e1" font-size="13">High pitch = shrill sound (whistle); Low pitch = deep bass (drum)</text>
    <text id="c10s11_b2" x="300" y="158" text-anchor="middle" fill="#6ee7b7" font-size="13">Audible range: 20 Hz to 20,000 Hz | Timbre = harmonic overtone quality</text>
  </svg>
</div>
<script>
window.setC10S11 = function(k){
  const m = {
    pitch: ['Pitch = Frequency | Loudness = Amplitude (dB)', 'High pitch = shrill sound (whistle); Low pitch = deep bass (drum)', 'Audible range: 20 Hz to 20,000 Hz | Timbre = harmonic overtone quality'],
    ear: ['Human Ear: Eardrum &rarr; Ossicles &rarr; Cochlea', 'Hammer, Anvil, Stirrup amplify vibrations by ~20x into liquid cochlea', 'Auditory nerve sends electrical neural impulses to brain'],
    raman: ['C. V. Raman: Indian Percussion Acoustics', 'Black composite syaahi patch on tabla/mridangam tunes overtones', 'Proved Indian drums produce uniquely pure musical harmonics!']
  };
  document.getElementById('c10s11_h').textContent = m[k][0];
  document.getElementById('c10s11_b1').textContent = m[k][1];
  document.getElementById('c10s11_b2').textContent = m[k][2];
};
</script>""",

    12: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Echo Simulator: 0.1 s Persistence &amp; 17 m Rule</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Distance d: <b id="c10s12_d_lbl" class="text-cyan-300">85 m</b></label>
      <input type="range" min="10" max="170" step="10" value="85" id="c10s12_sl" oninput="updC10S12()" class="w-28 accent-amber-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <circle cx="120" cy="115" r="24" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="120" y="119" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">Source</text>
    <rect x="480" y="45" width="20" height="140" fill="#78350f" stroke="#fde68a" stroke-width="2"/>
    <text x="490" y="205" text-anchor="middle" fill="#fde047" font-size="11">Reflecting Wall</text>
    <line x1="150" y1="100" x2="475" y2="100" stroke="#34d399" stroke-width="3"/>
    <line x1="475" y1="130" x2="150" y2="130" stroke="#fbbf24" stroke-width="3" stroke-dasharray="6,4"/>
    <text id="c10s12_res" x="300" y="45" text-anchor="middle" fill="#6ee7b7" font-size="16" font-weight="bold">Ex 10.5: t = (2 &times; 85) / 340 = 0.50 s &rarr; Distinct Echo Heard!</text>
    <text x="300" y="222" text-anchor="middle" fill="#cbd5e1" font-size="11">Persistence of hearing = 0.1 s &rArr; Minimum distance in air = 17 m (v = 340 m/s)</text>
  </svg>
</div>
<script>
window.updC10S12 = function(){
  const d = parseInt(document.getElementById('c10s12_sl').value, 10);
  const t = (2 * d) / 340;
  document.getElementById('c10s12_d_lbl').textContent = d + ' m';
  const r = document.getElementById('c10s12_res');
  if(d < 17){
    r.textContent = 'd = ' + d + ' m (<17 m): t = ' + t.toFixed(2) + ' s (<0.1 s) &rarr; NO separate echo!';
    r.setAttribute('fill','#fda4af');
  } else {
    r.textContent = 'd = ' + d + ' m (&ge;17 m): t = ' + t.toFixed(2) + ' s (&ge;0.1 s) &rarr; Distinct Echo Heard!';
    r.setAttribute('fill','#6ee7b7');
  }
};
</script>""",

    13: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-rose-300 uppercase">Section 10.7.2: Reverberation &amp; Whispering Gallery</span>
    <div class="flex gap-2">
      <button onclick="setC10S13('rev')" class="px-2.5 py-1 rounded bg-rose-600/30 text-xs text-rose-200 border border-rose-500/40">Reverberation</button>
      <button onclick="setC10S13('gumbaz')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Gol Gumbaz Gallery</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="c10s13_rev">
      <rect x="80" y="55" width="440" height="120" fill="none" stroke="#64748b" stroke-width="4"/>
      <path d="M 120 150 L 220 58 L 380 172 L 490 60 L 515 150" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="5,4"/>
      <text x="300" y="40" text-anchor="middle" fill="#fda4af" font-size="14" font-weight="bold">Multiple Reflections &lt; 0.05 s &rarr; Confused Drone of Sound</text>
      <text x="300" y="205" text-anchor="middle" fill="#cbd5e1" font-size="12">Control: Sound-absorbing fiberboard panels, heavy drapery &amp; upholstered seats</text>
    </g>
    <g id="c10s13_gumbaz" style="display:none">
      <path d="M 150 170 Q 300 35 450 170" fill="none" stroke="#f59e0b" stroke-width="6"/>
      <text x="300" y="100" text-anchor="middle" fill="#fde047" font-size="16" font-weight="bold">Gol Gumbaz Whispering Gallery (Bijapur, 1656)</text>
      <text x="300" y="135" text-anchor="middle" fill="#cbd5e1" font-size="13">Curved dome masonry reflects whispers across 60 m over 10 times!</text>
    </g>
  </svg>
</div>
<script>
window.setC10S13 = function(m){
  document.getElementById('c10s13_rev').style.display = (m==='rev'?'block':'none');
  document.getElementById('c10s13_gumbaz').style.display = (m==='gumbaz'?'block':'none');
};
</script>""",

    14: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-cyan-300 uppercase">Infrasound (&lt;20 Hz) vs Ultrasound (&gt;20 kHz)</span>
    <div class="flex gap-1.5 flex-wrap">
      <button onclick="setC10S14('infra')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Infrasound (&lt;20 Hz)</button>
      <button onclick="setC10S14('ultra')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Ultrasound (&gt;20 kHz)</button>
      <button onclick="setC10S14('litho')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Kidney Lithotripsy</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="145" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text id="c10s14_h" x="300" y="92" text-anchor="middle" fill="#fbbf24" font-size="20" font-weight="bold">Infrasound: Waves below 20 Hz</text>
    <text id="c10s14_b1" x="300" y="128" text-anchor="middle" fill="#cbd5e1" font-size="13">Earthquake seismic shocks, volcanic eruptions, elephants &amp; whales</text>
    <text id="c10s14_b2" x="300" y="158" text-anchor="middle" fill="#6ee7b7" font-size="13">Propagates vast distances through the Earth and oceans</text>
  </svg>
</div>
<script>
window.setC10S14 = function(k){
  const m = {
    infra: ['Infrasound: Waves below 20 Hz', 'Earthquake seismic shocks, volcanic eruptions, elephants & whales', 'Propagates vast distances through the Earth and oceans'],
    ultra: ['Ultrasound: Waves above 20,000 Hz (20 kHz)', 'Medical ultrasonography imaging (hearts, fetuses, organs)', 'Non-destructive metal defect testing & industrial spiral cleaning'],
    litho: ['Medical Ultrasound Lithotripsy', 'High-energy focused ultrasound pulses pulverize hard kidney stones', 'Converts stones into fine sand that passes naturally without surgery']
  };
  document.getElementById('c10s14_h').textContent = m[k][0];
  document.getElementById('c10s14_b1').textContent = m[k][1];
  document.getElementById('c10s14_b2').textContent = m[k][2];
};
</script>""",

    15: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Echolocation &amp; SONAR: 2d = v &times; t</span>
    <div class="flex gap-2">
      <button onclick="setC10S15('bat')" class="px-2.5 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Bat Echolocation</button>
      <button onclick="setC10S15('sonar')" class="px-2.5 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Ship SONAR</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <g id="c10s15_vis">
      <rect x="220" y="35" width="160" height="40" rx="6" fill="#0284c7" stroke="#7dd3fc" stroke-width="2"/>
      <text x="300" y="60" text-anchor="middle" fill="#fff" font-size="14" font-weight="bold">Ship Transmitter / Receiver</text>
      <line x1="270" y1="75" x2="270" y2="165" stroke="#38bdf8" stroke-width="3"/>
      <line x1="330" y1="165" x2="330" y2="75" stroke="#fbbf24" stroke-width="3" stroke-dasharray="6,4"/>
      <rect x="200" y="165" width="200" height="25" rx="4" fill="#334155" stroke="#94a3b8"/>
      <text x="300" y="182" text-anchor="middle" fill="#fde047" font-size="12" font-weight="bold">Ocean Seabed / Reef</text>
    </g>
    <text id="c10s15_calc" x="300" y="215" text-anchor="middle" fill="#6ee7b7" font-size="14" font-weight="bold">Ex 10.6: d = (1530 m/s &times; 0.90 s) / 2 = 688.5 m</text>
  </svg>
</div>
<script>
window.setC10S15 = function(m){
  const c = document.getElementById('c10s15_calc');
  if(m==='bat'){
    c.textContent = 'Bat Echolocation: Ultrasonic pulses bounce off moths & branches in the dark!';
  } else {
    c.textContent = 'Ex 10.6 (SONAR): 2d = v x t &rArr; d = (1530 m/s x 0.90 s) / 2 = 688.5 m';
  }
};
</script>""",

    16: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2 flex-wrap gap-1.5">
    <span class="text-xs font-bold text-emerald-300 uppercase">At a Glance: Chapter 10 Wave Toolkit</span>
    <div class="flex gap-1.5 flex-wrap">
      <button onclick="setC10S16('gen')" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200 border border-cyan-500/40">Generation</button>
      <button onclick="setC10S16('wave')" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200 border border-emerald-500/40">Wave Laws</button>
      <button onclick="setC10S16('perc')" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200 border border-amber-500/40">Perception</button>
      <button onclick="setC10S16('app')" class="px-2 py-1 rounded bg-purple-600/30 text-xs text-purple-200 border border-purple-500/40">Echo &amp; Sonar</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="145" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text id="c10s16_h" x="300" y="88" text-anchor="middle" fill="#fbbf24" font-size="20" font-weight="bold">Sound = Mechanical Longitudinal Wave</text>
    <text id="c10s16_b1" x="300" y="124" text-anchor="middle" fill="#cbd5e1" font-size="13">Produced strictly by vibrating bodies | Requires material medium (no vacuum!)</text>
    <text id="c10s16_b2" x="300" y="154" text-anchor="middle" fill="#6ee7b7" font-size="13">Transfers energy via compressions (C) &amp; rarefactions (R)</text>
  </svg>
</div>
<script>
window.setC10S16 = function(k){
  const m = {
    gen: ['Sound = Mechanical Longitudinal Wave', 'Produced strictly by vibrating bodies | Requires material medium (no vacuum!)', 'Transfers energy via compressions (C) & rarefactions (R)'],
    wave: ['Universal Wave Equation: v = &lambda; &times; &nu;  |  &nu; = 1 / T', 'Speed: Air (~344 m/s) < Water (~1530 m/s) < Steel (~5000 m/s)', 'Energy &prop; A&sup2; (square of amplitude) | Intensity drops as 1/r&sup2;'],
    perc: ['Human Hearing: 20 Hz to 20,000 Hz (20 kHz)', 'Pitch = Frequency | Loudness = Amplitude (dB) | Timbre = Wave quality', 'Middle ear ossicles: Hammer, Anvil, Stirrup amplify into Cochlea'],
    app: ['Echo: Minimum 17 m in air (0.1 s delay) | Reverberation control', 'Infrasound (<20 Hz): Earthquakes | Ultrasound (>20 kHz): Imaging', 'SONAR & Bats: 2d = v &times; t (round-trip echolocation)']
  };
  document.getElementById('c10s16_h').textContent = m[k][0];
  document.getElementById('c10s16_b1').textContent = m[k][1];
  document.getElementById('c10s16_b2').textContent = m[k][2];
};
</script>"""
}
