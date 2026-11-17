#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Science Chapter 1: Exploration: Entering the World of Secondary Science
Part 2: Simulators 9 to 16 (Slides 9 to 16)
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚖️</span> Law vs. Theory vs. Principle Explorer
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s1s9Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Scientific Law</button>
    <button onclick="c9s1s9Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Scientific Theory</button>
    <button onclick="c9s1s9Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Scientific Principle</button>
  </div>
  <div id="c9s1s9Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2"></div>
</div>
<script>
(function(){
  const items = [
    { role: 'Describes WHAT Happens', color: 'text-cyan-300', def: 'A regular, repeatable pattern observed consistently across nature.', ex: 'Newton Laws of Motion: describes why passengers jerk forward when a moving bus brakes suddenly.' },
    { role: 'Explains WHY It Happens', color: 'text-emerald-300', def: 'A deeply tested, evidence-based explanatory framework (NOT a casual guess!), open to refinement with new data.', ex: 'Atomic Theory: explains why elements combine in fixed mass ratios and how molecules form.' },
    { role: 'Broad Guiding Rule', color: 'text-amber-300', def: 'A foundational rule applied to analyze wide classes of physical and chemical situations.', ex: 'Principle of Conservation of Energy: energy transforms between forms without being created or destroyed.' }
  ];
  window.c9s1s9Pick = function(i){
    const d = items[i];
    document.getElementById('c9s1s9Out').innerHTML = `
      <div class="font-bold text-sm ${d.color}">${d.role}</div>
      <div class="text-slate-200">${d.def}</div>
      <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-slate-300"><b class="text-slate-100">Example:</b> ${d.ex}</div>`;
  };
  c9s1s9Pick(0);
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🌧️</span> Example 1.2: Vague Hunch → Measurable Prediction
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Humidity:</span><span id="c9s1s10HL" class="text-cyan-300 font-bold">85%</span></div>
      <input id="c9s1s10H" type="range" min="30" max="100" value="85" oninput="c9s1s10Up()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Temp Drop:</span><span id="c9s1s10TL" class="text-emerald-300 font-bold">4 °C</span></div>
      <input id="c9s1s10T" type="range" min="0" max="10" value="4" oninput="c9s1s10Up()" class="w-full accent-emerald-400">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Wind Speed:</span><span id="c9s1s10WL" class="text-amber-300 font-bold">22 km/h</span></div>
      <input id="c9s1s10W" type="range" min="0" max="50" value="22" oninput="c9s1s10Up()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9s1s10Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9s1s10Up = function(){
    const h = parseInt(document.getElementById('c9s1s10H').value, 10);
    const t = parseInt(document.getElementById('c9s1s10T').value, 10);
    const w = parseInt(document.getElementById('c9s1s10W').value, 10);
    document.getElementById('c9s1s10HL').textContent = h + '%';
    document.getElementById('c9s1s10TL').textContent = t + ' °C';
    document.getElementById('c9s1s10WL').textContent = w + ' km/h';
    const score = Math.min(98, Math.max(5, Math.round((h - 30) * 0.9 + t * 3 + w * 0.35)));
    document.getElementById('c9s1s10Out').innerHTML = `
      <div class="flex justify-between items-center"><span class="text-slate-400">Vague: "Clouds look dark"</span><span class="font-bold text-cyan-300">Testable Rain Chance: ${score}%</span></div>
      <div class="w-full h-2.5 bg-slate-900 rounded-full overflow-hidden"><div class="h-full bg-cyan-400 transition-all" style="width:${score}%"></div></div>
      <div class="text-slate-300">Replacing subjective words with humidity, temperature drop, wind speed, and historical records enables objective testing!</div>`;
  };
  c9s1s10Up();
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🌀</span> Weather Forecast Uncertainty Horizon
  </h3>
  <label class="block bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-xs">
    <div class="flex justify-between"><span>Forecast Lead Time:</span><span id="c9s1s11DL" class="text-cyan-300 font-bold">2 Days</span></div>
    <input id="c9s1s11D" type="range" min="1" max="14" value="2" oninput="c9s1s11Up()" class="w-full accent-cyan-400">
  </label>
  <div id="c9s1s11Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2"></div>
</div>
<script>
(function(){
  window.c9s1s11Up = function(){
    const day = parseInt(document.getElementById('c9s1s11D').value, 10);
    document.getElementById('c9s1s11DL').textContent = day + (day === 1 ? ' Day' : ' Days');
    const spread = Math.min(100, Math.round(4 * Math.pow(1.26, day)));
    const acc = Math.max(15, 100 - spread);
    const col = acc >= 70 ? 'text-emerald-300' : (acc >= 45 ? 'text-amber-300' : 'text-rose-300');
    document.getElementById('c9s1s11Out').innerHTML = `
      <div class="grid grid-cols-2 gap-2">
        <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Forecast Reliability</div><div class="text-base font-bold ${col}">${acc}%</div></div>
        <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Initial Error Amplification</div><div class="text-base font-bold text-violet-300">${spread}% Spread</div></div>
      </div>
      <div class="text-slate-300">Tiny measurement uncertainties in initial temperature, pressure, and wind amplify day by day in Earth atmosphere.</div>`;
  };
  c9s1s11Up();
})();
</script>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🌒</span> Checking Viral Claims: Eclipse Food Test Lab
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s1s12Check(0)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">1. Physical Check</button>
    <button onclick="c9s1s12Check(1)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">2. Chemical Check</button>
    <button onclick="c9s1s12Check(2)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">3. Biological Check</button>
  </div>
  <div id="c9s1s12Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2"></div>
</div>
<script>
(function(){
  const checks = [
    { t: 'Physical Mechanism Test', v: 'NO HARMFUL RADIATION', d: 'An eclipse is simply a shadow event where Moon or Earth temporarily blocks ordinary sunlight. No new radiation is created!' },
    { t: 'Chemical Mechanism Test', v: 'NO CHEMICAL REACTION', d: 'Blocking sunlight for a few minutes does not alter molecular bonds in cooked rice, dal, or water.' },
    { t: 'Biological Mechanism Test', v: 'NO INSTANT TOXINS', d: 'Food spoilage depends on temperature, moisture, and time—not lunar shadows. Covered food stays just as safe!' }
  ];
  window.c9s1s12Check = function(i){
    const c = checks[i];
    document.getElementById('c9s1s12Out').innerHTML = `
      <div class="flex justify-between items-center"><span class="font-bold text-sm text-cyan-300">${c.t}</span><span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold">${c.v}</span></div>
      <p class="text-slate-300 leading-relaxed">${c.d}</p>`;
  };
  c9s1s12Check(0);
})();
</script>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🍚</span> Order-of-Magnitude Estimator: Monthly Family Rice
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Family Members:</span><span id="c9s1s13FL" class="text-cyan-300 font-bold">4</span></div>
      <input id="c9s1s13F" type="range" min="1" max="10" value="4" oninput="c9s1s13Up()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Rice/Person/Day:</span><span id="c9s1s13RL" class="text-emerald-300 font-bold">300 g</span></div>
      <input id="c9s1s13R" type="range" min="150" max="500" step="50" value="300" oninput="c9s1s13Up()" class="w-full accent-emerald-400">
    </label>
  </div>
  <div id="c9s1s13Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs grid grid-cols-3 gap-2 text-center"></div>
</div>
<script>
(function(){
  window.c9s1s13Up = function(){
    const f = parseInt(document.getElementById('c9s1s13F').value, 10);
    const r = parseInt(document.getElementById('c9s1s13R').value, 10);
    document.getElementById('c9s1s13FL').textContent = f;
    document.getElementById('c9s1s13RL').textContent = r + ' g';
    const kg = (f * r * 30) / 1000;
    document.getElementById('c9s1s13Out').innerHTML = `
      <div class="p-2 rounded bg-rose-950/30 border border-rose-500/30"><div class="text-rose-300 font-bold">100 g</div><div class="text-slate-400">Way too small!</div></div>
      <div class="p-2 rounded bg-emerald-950/40 border border-emerald-500/40"><div class="text-emerald-300 font-bold text-base">${kg.toFixed(1)} kg</div><div class="text-slate-300">Sensible 30-day estimate</div></div>
      <div class="p-2 rounded bg-rose-950/30 border border-rose-500/30"><div class="text-rose-300 font-bold">10 tonnes</div><div class="text-slate-400">Way too huge!</div></div>`;
  };
  c9s1s13Up();
})();
</script>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🫁</span> Example 1.3: Daily Inhaled Air Estimator
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Breaths / Min:</span><span id="c9s1s14BL" class="text-cyan-300 font-bold">14</span></div>
      <input id="c9s1s14B" type="range" min="10" max="24" value="14" oninput="c9s1s14Up()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-2 rounded-xl border border-slate-800">
      <div class="flex justify-between"><span>Litres / Breath:</span><span id="c9s1s14VL" class="text-emerald-300 font-bold">0.5 L</span></div>
      <input id="c9s1s14V" type="range" min="0.3" max="0.8" step="0.1" value="0.5" oninput="c9s1s14Up()" class="w-full accent-emerald-400">
    </label>
  </div>
  <div id="c9s1s14Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs grid grid-cols-2 gap-2"></div>
</div>
<script>
(function(){
  window.c9s1s14Up = function(){
    const b = parseInt(document.getElementById('c9s1s14B').value, 10);
    const v = parseFloat(document.getElementById('c9s1s14V').value);
    document.getElementById('c9s1s14BL').textContent = b;
    document.getElementById('c9s1s14VL').textContent = v.toFixed(1) + ' L';
    const bDay = b * 60 * 24;
    const airDay = Math.round(bDay * v);
    document.getElementById('c9s1s14Out').innerHTML = `
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Breaths per Day</div><div class="text-base font-bold text-cyan-300">~${bDay.toLocaleString()}</div></div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><div class="text-slate-400">Inhaled Air / Day</div><div class="text-base font-bold text-amber-300">~${airDay.toLocaleString()} L</div></div>`;
  };
  c9s1s14Up();
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>😷</span> Interdisciplinary Lab: How Does an N95 Mask Work?
  </h3>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
    <button onclick="c9s1s15Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Physics</button>
    <button onclick="c9s1s15Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Chemistry</button>
    <button onclick="c9s1s15Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Biology</button>
    <button onclick="c9s1s15Pick(3)" class="py-2 rounded-xl bg-slate-950 border border-violet-500/40 text-violet-300 font-bold">Mathematics</button>
  </div>
  <div id="c9s1s15Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const roles = [
    { name: 'Physics: Brownian Zig-Zag & Electrostatics', color: 'text-cyan-300', desc: 'Tiny aerosols zig-zag randomly into fibers, while electrostatic charges on melt-blown fibers attract and trap microscopic particles!' },
    { name: 'Chemistry: Polypropylene Polymer Fibers', color: 'text-emerald-300', desc: 'Engineered hydrophobic polypropylene polymers hold static electric charge long-term and resist moisture from exhaled breath.' },
    { name: 'Biology: Droplets & Respiratory Airways', color: 'text-amber-300', desc: 'Understanding viral sizes, respiratory droplets, and how pathogens enter lungs defines which particle sizes must be captured.' },
    { name: 'Mathematics: Airflow vs. 95% Capture', color: 'text-violet-300', desc: 'Quantitative models balance comfortable breathing resistance against 95% filtration efficiency across layered fiber density.' }
  ];
  window.c9s1s15Pick = function(i){
    const r = roles[i];
    document.getElementById('c9s1s15Out').innerHTML = `<div class="font-bold text-sm ${r.color}">${r.name}</div><p class="text-slate-300 leading-relaxed">${r.desc}</p>`;
  };
  c9s1s15Pick(0);
})();
</script>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🌐</span> Pause &amp; Ponder 3: Everyday System Mapper
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button onclick="c9s1s16Pick(0)" class="py-2 rounded-xl bg-slate-950 border border-cyan-500/40 text-cyan-300 font-bold">Pressure Cooker</button>
    <button onclick="c9s1s16Pick(1)" class="py-2 rounded-xl bg-slate-950 border border-emerald-500/40 text-emerald-300 font-bold">Mobile Phone</button>
    <button onclick="c9s1s16Pick(2)" class="py-2 rounded-xl bg-slate-950 border border-amber-500/40 text-amber-300 font-bold">Traffic Jam</button>
  </div>
  <div id="c9s1s16Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs grid grid-cols-1 sm:grid-cols-2 gap-2"></div>
</div>
<script>
(function(){
  const sys = [
    { p: 'Steam pressure raises water boiling point (~120 °C)', c: 'Faster Maillard browning & protein cooking reactions', b: 'Heat sterilizes microbes in food safely', m: 'Heat transfer & cooking time equations' },
    { p: 'Electromagnetic radio waves & semiconductor circuits', c: 'Lithium-ion battery redox chemistry & screen materials', b: 'Eye strain ergonomics & circadian blue-light biology', m: 'Signal compression & error-correcting algorithms' },
    { p: 'Braking distance, friction & vehicle momentum', c: 'Fuel combustion & exhaust pollutant chemistry', b: 'Human reaction time & respiratory air-quality impact', m: 'Queueing flow rates & signal timing optimization' }
  ];
  window.c9s1s16Pick = function(i){
    const s = sys[i];
    document.getElementById('c9s1s16Out').innerHTML = `
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><b class="text-cyan-300">Physics:</b> ${s.p}</div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><b class="text-emerald-300">Chemistry:</b> ${s.c}</div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><b class="text-amber-300">Biology:</b> ${s.b}</div>
      <div class="p-2 rounded bg-slate-900 border border-slate-800"><b class="text-violet-300">Math:</b> ${s.m}</div>`;
  };
  c9s1s16Pick(0);
})();
</script>
"""
}
