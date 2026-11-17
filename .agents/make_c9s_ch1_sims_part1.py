#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Science Chapter 1: Exploration: Entering the World of Secondary Science
Part 1: Simulators 1 to 8 (Slides 1 to 8)
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🔬</span> Secondary Science Inquiry Cycle Explorer
  </h3>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
    <button onclick="c9s1s1Stage(0)" id="c9s1s1B0" class="px-2 py-2 rounded-xl bg-cyan-500/20 border border-cyan-400 text-cyan-200 font-bold">1. Observation</button>
    <button onclick="c9s1s1Stage(1)" id="c9s1s1B1" class="px-2 py-2 rounded-xl bg-slate-950 border border-slate-700 text-slate-300 font-bold">2. Measurement</button>
    <button onclick="c9s1s1Stage(2)" id="c9s1s1B2" class="px-2 py-2 rounded-xl bg-slate-950 border border-slate-700 text-slate-300 font-bold">3. Math Model</button>
    <button onclick="c9s1s1Stage(3)" id="c9s1s1B3" class="px-2 py-2 rounded-xl bg-slate-950 border border-slate-700 text-slate-300 font-bold">4. Test &amp; Revise</button>
  </div>
  <div id="c9s1s1Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 space-y-2"></div>
  <div class="flex gap-2 text-xs">
    <button onclick="c9s1s1Test(true)" class="flex-1 py-2 rounded-xl bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 font-bold">Evidence Supports Model</button>
    <button onclick="c9s1s1Test(false)" class="flex-1 py-2 rounded-xl bg-rose-500/20 border border-rose-500/40 text-rose-300 font-bold">Evidence Contradicts Model</button>
  </div>
  <div id="c9s1s1Feedback" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">Select a stage or test experimental evidence above.</div>
</div>
<script>
(function(){
  const stages = [
    { name: '1. Careful Observation', color: 'text-cyan-300', desc: 'Notice patterns, anomalies, and questions in everyday nature (e.g., why stars have different colours or why a pendulum swings steadily).' },
    { name: '2. Quantitative Measurement', color: 'text-emerald-300', desc: 'Attach numbers and standardized SI units (metres, seconds, kilograms, kelvin) using calibrated instruments instead of vague adjectives.' },
    { name: '3. Mathematical Modeling', color: 'text-amber-300', desc: 'Express relationships cleanly with equations, ratios, and graphs (such as F = ma or v = d / t) by keeping essential variables.' },
    { name: '4. Testing & Revision', color: 'text-violet-300', desc: 'Compare model predictions against fresh experiments. Support builds confidence; contradiction triggers revision or replacement!' }
  ];
  window.c9s1s1Stage = function(idx){
    const s = stages[idx];
    document.getElementById('c9s1s1Out').innerHTML = `<div class="font-bold text-sm ${s.color}">${s.name}</div><p class="text-slate-300 leading-relaxed">${s.desc}</p>`;
  };
  window.c9s1s1Test = function(ok){
    const fb = document.getElementById('c9s1s1Feedback');
    if(ok){
      fb.innerHTML = '<span class="text-emerald-300 font-bold">Confidence Grows:</span> Repeated experiments match predictions, strengthening the scientific model within its domain.';
    } else {
      fb.innerHTML = '<span class="text-rose-300 font-bold">Self-Correction Triggered:</span> Scientists inspect assumptions, re-check measurements, and revise or discard the old model!';
    }
  };
  c9s1s1Stage(0);
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧭</span> Textbook Design Icons: Magnifying Glass &amp; Compass
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <button onclick="c9s1s2Mode(0)" class="py-2.5 px-3 rounded-xl bg-cyan-500/20 border border-cyan-400/50 text-cyan-200 font-bold">🔍 Magnifying Glass</button>
    <button onclick="c9s1s2Mode(1)" class="py-2.5 px-3 rounded-xl bg-amber-500/20 border border-amber-400/50 text-amber-200 font-bold">🧭 Compass</button>
  </div>
  <div id="c9s1s2Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 space-y-2"></div>
</div>
<script>
(function(){
  const modes = [
    {
      title: 'Magnifying Glass: Careful Observation',
      color: 'text-cyan-300',
      core: 'Symbolizes looking closely at reality and noticing subtle patterns, tiny anomalies, and details others overlook.',
      ex1: 'Noticing tiny spectral line differences in starlight (Meghnad Saha).',
      ex2: 'Observing exact humidity and temperature drops before rainfall.'
    },
    {
      title: 'Compass: Purpose, Direction & Limits',
      color: 'text-amber-300',
      core: 'Symbolizes choosing appropriate models, asking the right testable questions, and recognizing where an idea stops working.',
      ex1: 'Knowing short-term 2-day weather forecasts work well while 14-day forecasts blur.',
      ex2: 'Choosing point-mass models for highway travel while ignoring car paint colour.'
    }
  ];
  window.c9s1s2Mode = function(i){
    const m = modes[i];
    document.getElementById('c9s1s2Out').innerHTML = `
      <div class="font-bold text-sm ${m.color}">${m.title}</div>
      <p class="text-slate-300">${m.core}</p>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
        <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><span class="text-emerald-300 font-semibold">Example A:</span> ${m.ex1}</div>
        <div class="p-2 rounded-lg bg-slate-900 border border-slate-800"><span class="text-violet-300 font-semibold">Example B:</span> ${m.ex2}</div>
      </div>`;
  };
  c9s1s2Mode(0);
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧩</span> Scientific Modeling: What to Keep vs. Ignore
  </h3>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
    <button onclick="c9s1s3Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Physics: Car</button>
    <button onclick="c9s1s3Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Chemistry: Atom</button>
    <button onclick="c9s1s3Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Biology: Cell</button>
    <button onclick="c9s1s3Pick(3)" class="py-2 rounded-xl bg-slate-950 border border-violet-500/40 text-violet-300 font-bold">Earth: Planet</button>
  </div>
  <div id="c9s1s3Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2"></div>
</div>
<script>
(function(){
  const items = [
    { title: 'Physics: Car as a Point Mass', q: 'How long to travel 120 km between two cities?', keep: 'Total mass, average speed, highway distance', ignore: 'Paint colour, tyre tread brand, vibrating mirror' },
    { title: 'Chemistry: Atoms as Solid Spheres', q: 'How do molecules pack and collide in reactions?', keep: 'Effective radius, mass, bonding geometry', ignore: 'Complex sub-orbital wave details for basic packing' },
    { title: 'Biology: Simplified Cell Diagram', q: 'What are the major organelles and their roles?', keep: 'Nucleus, membrane, mitochondria, cytoplasm layout', ignore: 'Billions of individual water molecules and rapid thermal jiggling' },
    { title: 'Earth Science: Smooth Layered Sphere', q: 'How do gravity and seismic waves travel globally?', keep: 'Radius, core-mantle-crust layers, overall density', ignore: 'Individual trees, houses, and small hills' }
  ];
  window.c9s1s3Pick = function(i){
    const d = items[i];
    document.getElementById('c9s1s3Out').innerHTML = `
      <div class="font-bold text-sm text-cyan-300">${d.title}</div>
      <div class="text-slate-400">Question: <span class="text-slate-200">${d.q}</span></div>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
        <div class="p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30"><div class="text-emerald-300 font-bold">KEEP (Essential)</div><div class="text-slate-200 mt-1">${d.keep}</div></div>
        <div class="p-2.5 rounded-lg bg-rose-950/40 border border-rose-500/30"><div class="text-rose-300 font-bold">IGNORE (Noise)</div><div class="text-slate-200 mt-1">${d.ignore}</div></div>
      </div>`;
  };
  c9s1s3Pick(0);
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⭐</span> Meghnad Saha: Stellar Hot-Gas Ionization Explorer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Star Temperature (T):</span><span id="c9s1s4TL" class="text-amber-300 font-bold">6000 K</span></div>
      <input id="c9s1s4T" type="range" min="3000" max="18000" step="1000" value="6000" oninput="c9s1s4Up()" class="w-full accent-amber-400">
    </label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Gas Pressure (P):</span><span id="c9s1s4PL" class="text-cyan-300 font-bold">Medium</span></div>
      <input id="c9s1s4P" type="range" min="1" max="3" step="1" value="2" oninput="c9s1s4Up()" class="w-full accent-cyan-400">
    </label>
  </div>
  <div id="c9s1s4Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs flex items-center gap-4"></div>
</div>
<script>
(function(){
  window.c9s1s4Up = function(){
    const T = parseInt(document.getElementById('c9s1s4T').value, 10);
    const P = parseInt(document.getElementById('c9s1s4P').value, 10);
    document.getElementById('c9s1s4TL').textContent = T + ' K';
    const pNames = ['', 'Low', 'Medium', 'High'];
    document.getElementById('c9s1s4PL').textContent = pNames[P];
    let col = '#fbbf24', label = 'Yellow-White Star (like Sun)', ion = 'Moderate Thermal Ionization';
    if(T < 4500){ col = '#f87171'; label = 'Cool Red Star'; ion = 'Low Ionization (Neutral Atoms Dominate)'; }
    else if(T >= 10000){ col = '#60a5fa'; label = 'Hot Blue-White Star'; ion = 'High Thermal Ionization (Electrons Knocked Off)'; }
    if(P === 3 && T >= 4500 && T < 10000){ ion += ' — Higher pressure slightly suppresses ionization'; }
    document.getElementById('c9s1s4Out').innerHTML = `
      <div class="w-12 h-12 rounded-full shrink-0 shadow-lg" style="background:${col}; box-shadow:0 0 20px ${col}"></div>
      <div class="space-y-1">
        <div class="font-bold text-sm text-slate-100">${label}</div>
        <div class="text-cyan-300">Saha Model State: ${ion}</div>
        <div class="text-slate-400">Simplified stellar gas model connects star colour &amp; spectrum directly to temperature!</div>
      </div>`;
  };
  c9s1s4Up();
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏏</span> Example 1.1: Cricket Shot Boundary Simulator
  </h3>
  <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Launch Speed:</span><span id="c9s1s5VL" class="text-cyan-300 font-bold">28 m/s</span></div>
      <input id="c9s1s5V" type="range" min="15" max="38" value="28" oninput="c9s1s5Up()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Launch Angle:</span><span id="c9s1s5AL" class="text-emerald-300 font-bold">42 deg</span></div>
      <input id="c9s1s5A" type="range" min="15" max="75" value="42" oninput="c9s1s5Up()" class="w-full accent-emerald-400">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800 col-span-2 sm:col-span-1">
      <div class="flex justify-between"><span>Bat Brand (Ignored):</span><span id="c9s1s5BL" class="text-slate-400 font-bold">Pro-X</span></div>
      <select id="c9s1s5B" onchange="c9s1s5Up()" class="w-full bg-slate-900 text-slate-300 rounded mt-1 px-1 py-0.5 border border-slate-700">
        <option>Pro-X</option><option>SuperHit</option><option>ClassicWood</option>
      </select>
    </label>
  </div>
  <div id="c9s1s5Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs grid grid-cols-2 gap-2"></div>
</div>
<script>
(function(){
  window.c9s1s5Up = function(){
    const v = parseFloat(document.getElementById('c9s1s5V').value);
    const deg = parseFloat(document.getElementById('c9s1s5A').value);
    const brand = document.getElementById('c9s1s5B').value;
    document.getElementById('c9s1s5VL').textContent = v + ' m/s';
    document.getElementById('c9s1s5AL').textContent = deg + ' deg';
    document.getElementById('c9s1s5BL').textContent = brand;
    const rad = deg * Math.PI / 180;
    const range = (v * v * Math.sin(2 * rad)) / 9.8;
    const isSix = range >= 70;
    document.getElementById('c9s1s5Out').innerHTML = `
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Ideal Range (g = 9.8 m/s²)</div><div class="text-base font-bold text-cyan-300">${range.toFixed(1)} m</div></div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Boundary (70 m) Verdict</div><div class="text-base font-bold ${isSix ? 'text-emerald-300' : 'text-amber-300'}">${isSix ? 'SIX! Cleared' : 'Caught Inside'}</div></div>`;
  };
  c9s1s5Up();
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📖</span> Everyday Chat vs. Scientific Precision
  </h3>
  <div class="grid grid-cols-4 gap-2 text-xs">
    <button onclick="c9s1s6Word(0)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Work</button>
    <button onclick="c9s1s6Word(1)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Force</button>
    <button onclick="c9s1s6Word(2)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Cell</button>
    <button onclick="c9s1s6Word(3)" class="py-2 rounded-xl bg-slate-950 border border-violet-500/40 text-violet-300 font-bold">Reaction</button>
  </div>
  <div id="c9s1s6Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2"></div>
  <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs flex flex-wrap items-center justify-between gap-2">
    <span>Wall Push Test: Force = 200 N, Displacement = <input id="c9s1s6D" type="range" min="0" max="5" value="0" oninput="c9s1s6Calc()" class="w-24 align-middle accent-cyan-400"> <b id="c9s1s6DL" class="text-cyan-300">0 m</b></span>
    <span id="c9s1s6W" class="font-bold text-amber-300">Physics Work = 0 J</span>
  </div>
</div>
<script>
(function(){
  const terms = [
    { w: 'Work', casual: 'Any tiring effort, like studying or pushing a brick wall.', sci: 'Force multiplied by displacement along the force direction (W = F × d). Zero movement = 0 J work!' },
    { w: 'Force', casual: 'Strength of personality or persuasion.', sci: 'A measurable push or pull interaction between objects, measured in newtons (N).' },
    { w: 'Cell', casual: 'A small room or mobile phone.', sci: 'Biology: basic membrane-bound unit of life. Physics: electrochemical source of electric potential.' },
    { w: 'Reaction', casual: 'Someone feeling surprised or angry.', sci: 'Chemistry: rearrangement of atoms into new chemical substances with conserved mass.' }
  ];
  window.c9s1s6Word = function(i){
    const t = terms[i];
    document.getElementById('c9s1s6Out').innerHTML = `
      <div class="font-bold text-sm text-cyan-300">${t.w}</div>
      <div class="text-rose-300">Everyday Speech: <span class="text-slate-300">${t.casual}</span></div>
      <div class="text-emerald-300">Scientific Meaning: <span class="text-slate-200">${t.sci}</span></div>`;
  };
  window.c9s1s6Calc = function(){
    const d = parseInt(document.getElementById('c9s1s6D').value, 10);
    document.getElementById('c9s1s6DL').textContent = d + ' m';
    document.getElementById('c9s1s6W').textContent = 'Physics Work = ' + (200 * d) + ' J';
  };
  c9s1s6Word(0);
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚡</span> Universal Symbols &amp; Speed of Light (c)
  </h3>
  <div class="grid grid-cols-5 gap-1.5 text-xs text-center">
    <div class="p-2 rounded-lg bg-slate-950 border border-slate-800"><div class="text-cyan-300 font-bold text-sm">m</div><div class="text-slate-400">Mass</div></div>
    <div class="p-2 rounded-lg bg-slate-950 border border-slate-800"><div class="text-emerald-300 font-bold text-sm">v</div><div class="text-slate-400">Velocity</div></div>
    <div class="p-2 rounded-lg bg-slate-950 border border-slate-800"><div class="text-amber-300 font-bold text-sm">F</div><div class="text-slate-400">Force</div></div>
    <div class="p-2 rounded-lg bg-slate-950 border border-slate-800"><div class="text-violet-300 font-bold text-sm">I</div><div class="text-slate-400">Current</div></div>
    <div class="p-2 rounded-lg bg-slate-950 border border-cyan-500/40"><div class="text-rose-300 font-bold text-sm">c</div><div class="text-slate-400">Light Speed</div></div>
  </div>
  <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2">
    <div class="text-slate-300">Latin <b>celeritas</b> (speed): <span class="text-cyan-300 font-mono font-bold">c = 299,792,458 m/s</span></div>
    <div class="flex flex-wrap gap-2">
      <button onclick="c9s1s7Dist(384400, 'Earth to Moon')" class="px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-cyan-300 font-bold">Moon (384,400 km)</button>
      <button onclick="c9s1s7Dist(149600000, 'Sun to Earth')" class="px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-amber-300 font-bold">Sun (149.6M km)</button>
      <button onclick="c9s1s7Dist(3000, 'Across India')" class="px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-emerald-300 font-bold">India (3,000 km)</button>
    </div>
    <div id="c9s1s7Out" class="text-slate-200 font-semibold">Click a distance to see light travel time using math (t = d / c).</div>
  </div>
</div>
<script>
(function(){
  window.c9s1s7Dist = function(km, label){
    const t = (km * 1000) / 299792458;
    const str = t < 1 ? (t * 1000).toFixed(2) + ' milliseconds' : t.toFixed(2) + ' seconds';
    document.getElementById('c9s1s7Out').innerHTML = `<span class="text-cyan-300">${label}:</span> Light travels ${km.toLocaleString()} km in <span class="text-amber-300">${str}</span>.`;
  };
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>✈️</span> Aviation Fuel Unit Simulator (SI vs. Mixed Units)
  </h3>
  <div class="text-xs text-slate-300">Required fuel mass for flight: <b class="text-cyan-300">22,300 kg</b> (Jet fuel density ≈ 0.80 kg/L)</div>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <button onclick="c9s1s8Mode(true)" class="py-2.5 rounded-xl bg-emerald-500/20 border border-emerald-400/50 text-emerald-300 font-bold">Correct SI: kg/L (0.80)</button>
    <button onclick="c9s1s8Mode(false)" class="py-2.5 rounded-xl bg-rose-500/20 border border-rose-400/50 text-rose-300 font-bold">Unit Mix-up: lb/L (1.77)</button>
  </div>
  <div id="c9s1s8Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9s1s8Mode = function(correct){
    const out = document.getElementById('c9s1s8Out');
    if(correct){
      out.innerHTML = `
        <div class="text-emerald-300 font-bold text-sm">Safe Refuel: 27,875 Litres Loaded</div>
        <div class="text-slate-300">22,300 kg ÷ 0.80 kg/L = 27,875 L. Actual fuel mass = <b>22,300 kg (100% needed)</b>.</div>
        <div class="text-slate-400">Standardized SI units (kg, m, s) protect aviation, medicine, and everyday markets!</div>`;
    } else {
      out.innerHTML = `
        <div class="text-rose-300 font-bold text-sm">Dangerous Underfill: Only ~12,600 Litres Loaded!</div>
        <div class="text-slate-300">Using 1.77 lb/L instead of 0.80 kg/L loads <b>~10,080 kg (45% of needed fuel)</b>!</div>
        <div class="text-amber-300">Result: Plane runs out of fuel mid-flight! Standardized SI units prevent disasters.</div>`;
    }
  };
  c9s1s8Mode(true);
})();
</script>
"""
}
