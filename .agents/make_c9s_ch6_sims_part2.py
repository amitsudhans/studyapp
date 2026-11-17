#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sims_part2 = {
    9: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Worked Examples 6.4, 6.5 & 6.6</span>
    <div class="flex gap-1.5">
      <button onclick="setEx9(4)" class="px-2 py-1 rounded bg-amber-600/30 text-xs text-amber-200">Ex 6.4 Barbell</button>
      <button onclick="setEx9(5)" class="px-2 py-1 rounded bg-cyan-600/30 text-xs text-cyan-200">Ex 6.5 Box</button>
      <button onclick="setEx9(6)" class="px-2 py-1 rounded bg-emerald-600/30 text-xs text-emerald-200">Ex 6.6 Sports Car</button>
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="65" y="45" width="470" height="150" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text id="sim9_t" x="300" y="85" text-anchor="middle" fill="#fcd34d" font-size="16" font-weight="bold">Example 6.4: 30 kg Barbell Held Steady</text>
    <text id="sim9_l1" x="300" y="120" text-anchor="middle" fill="#cbd5e1" font-size="13">Downward Weight = m × g = 30 kg × 9.8 m/s² = 294 N</text>
    <text id="sim9_l2" x="300" y="152" text-anchor="middle" fill="#6ee7b7" font-size="14" font-weight="bold">Required Upward Force = 294 N</text>
  </svg>
</div>
<script>
window.setEx9 = function(n){
  const map = {
    4: ['Example 6.4: 30 kg Barbell Held Steady', 'Downward Weight = m × g = 30 kg × 9.8 m/s² = 294 N', 'Required Upward Force = 294 N'],
    5: ['Example 6.5: 25 kg Box (55 N vs 50 N Friction)', 'F_net = 5 N ⇒ a = 5 / 25 = 0.2 m/s²', 'In 2 s from rest: s = ½(0.2)(2²) = 0.4 m'],
    6: ['Example 6.6: 1500 kg Sports Car (3 Phases)', 'Accel (+2 m/s²): +3000 N east | Cruise (0): 0 N', 'Braking (-2 m/s²): -3000 N west']
  }[n];
  document.getElementById('sim9_t').textContent = map[0];
  document.getElementById('sim9_l1').textContent = map[1];
  document.getElementById('sim9_l2').textContent = map[2];
};
</script>""",

    10: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Activity 6.6: Interlocked Spring Balances</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Pull: <b id="sim10_p" class="text-cyan-300">15 N</b></label>
      <input type="range" min="5" max="30" step="5" value="15" oninput="updSim10(this.value)" class="w-32 accent-amber-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="95" y="95" width="175" height="46" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text id="sim10_a" x="182" y="123" text-anchor="middle" fill="#7dd3fc" font-size="14" font-weight="bold">Balance A: 15 N ←</text>
    <circle cx="300" cy="118" r="10" fill="none" stroke="#fbbf24" stroke-width="3"/>
    <rect x="330" y="95" width="175" height="46" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text id="sim10_b" x="417" y="123" text-anchor="middle" fill="#6ee7b7" font-size="14" font-weight="bold">→ Balance B: 15 N</text>
    <text x="300" y="55" text-anchor="middle" fill="#fde68a" font-size="14" font-weight="bold">Identical Readings in Opposite Directions</text>
    <text x="300" y="185" text-anchor="middle" fill="#cbd5e1" font-size="12">Act on TWO DIFFERENT objects ⇒ Never cancel out!</text>
  </svg>
</div>
<script>
window.updSim10 = function(v){
  document.getElementById('sim10_p').textContent = v + ' N';
  document.getElementById('sim10_a').textContent = 'Balance A: ' + v + ' N ←';
  document.getElementById('sim10_b').textContent = '→ Balance B: ' + v + ' N';
};
</script>""",

    11: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Activity 6.7: Balloon Rocket & Chandrayaan-3</span>
    <button onclick="launch11()" class="px-3 py-1 rounded-lg bg-cyan-600/30 text-cyan-200 border border-cyan-500/40 text-xs font-bold">Release Balloon</button>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="50" y1="100" x2="550" y2="100" stroke="#64748b" stroke-width="3"/>
    <g id="sim11_b">
      <rect x="95" y="94" width="55" height="12" rx="3" fill="#e2e8f0"/>
      <ellipse cx="122" cy="128" rx="42" ry="22" fill="#f43f5e" stroke="#fda4af" stroke-width="2"/>
    </g>
    <text x="300" y="45" text-anchor="middle" fill="#7dd3fc" font-size="14" font-weight="bold">Air Exhaust ←  |  Balloon Thrust →</text>
    <text x="300" y="195" text-anchor="middle" fill="#fde68a" font-size="12">Vikram Lander Retro-Firing: Exhaust Downward ⇒ Upward Braking Thrust in Vacuum!</text>
  </svg>
</div>
<script>
(function(){
  let pos=0;
  window.launch11 = function(){
    pos = (pos===0 ? 310 : 0);
    document.getElementById('sim11_b').setAttribute('transform', 'translate('+pos+',0)');
  };
})();
</script>""",

    12: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-rose-300 uppercase">Example 6.8: Gun & Bullet Recoil (F = 2 N)</span>
    <span class="text-xs text-slate-400">a = F / m</span>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="70" y="55" width="215" height="130" rx="12" fill="#0f172a" stroke="#f43f5e" stroke-width="2"/>
    <text x="177" y="90" text-anchor="middle" fill="#fda4af" font-size="15" font-weight="bold">5 kg Gun (Recoil ←)</text>
    <text x="177" y="122" text-anchor="middle" fill="#cbd5e1" font-size="12">Force = 2 N backward</text>
    <text x="177" y="155" text-anchor="middle" fill="#f43f5e" font-size="16" font-weight="bold">a = 2 / 5 = 0.4 m/s²</text>

    <rect x="315" y="55" width="215" height="130" rx="12" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
    <text x="422" y="90" text-anchor="middle" fill="#6ee7b7" font-size="15" font-weight="bold">0.1 kg Bullet (→)</text>
    <text x="422" y="122" text-anchor="middle" fill="#cbd5e1" font-size="12">Force = 2 N forward</text>
    <text x="422" y="155" text-anchor="middle" fill="#34d399" font-size="16" font-weight="bold">a = 2 / 0.1 = 20 m/s²</text>
  </svg>
</div>""",

    13: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Multi-Body System: Internal Tension Cancels</span>
    <div class="flex items-center gap-2">
      <label class="text-xs text-slate-300">Pull F: <b id="sim13_f" class="text-amber-300">30 N</b></label>
      <input type="range" min="10" max="50" step="10" value="30" oninput="updSim13(this.value)" class="w-32 accent-emerald-400">
    </div>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <line x1="50" y1="165" x2="550" y2="165" stroke="#475569" stroke-width="3"/>
    <rect x="115" y="100" width="85" height="65" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="157" y="138" text-anchor="middle" fill="#7dd3fc" font-size="13" font-weight="bold">m₂ = 6 kg</text>
    <line x1="200" y1="132" x2="285" y2="132" stroke="#fbbf24" stroke-width="3"/>
    <text x="242" y="122" text-anchor="middle" fill="#fde68a" font-size="11">Tension T</text>
    <rect x="285" y="100" width="85" height="65" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="2.5"/>
    <text x="327" y="138" text-anchor="middle" fill="#6ee7b7" font-size="13" font-weight="bold">m₁ = 4 kg</text>
    <line x1="370" y1="132" x2="465" y2="132" stroke="#f43f5e" stroke-width="4"/>
    <polygon points="472,132 458,125 458,139" fill="#f43f5e"/>
    <text id="sim13_res" x="300" y="52" text-anchor="middle" fill="#6ee7b7" font-size="16" font-weight="bold">a = 30 / (4 + 6) = 3.0 m/s²  |  T = 18 N</text>
  </svg>
</div>
<script>
window.updSim13 = function(f){
  f = parseInt(f,10);
  document.getElementById('sim13_f').textContent = f + ' N';
  const a = (f/10).toFixed(1);
  const T = (6*(f/10)).toFixed(0);
  document.getElementById('sim13_res').textContent = 'a = '+f+' / (4 + 6) = '+a+' m/s²  |  T = '+T+' N';
};
</script>""",

    14: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-cyan-300 uppercase">Friction Engineering & Capstan Effect</span>
    <span class="text-xs text-slate-400">Principia (1687)</span>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="45" y="40" width="245" height="160" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="167" y="72" text-anchor="middle" fill="#7dd3fc" font-size="14" font-weight="bold">Minimizing Friction</text>
    <text x="167" y="104" text-anchor="middle" fill="#cbd5e1" font-size="12">• Ball Bearings (Rolling)</text>
    <text x="167" y="132" text-anchor="middle" fill="#cbd5e1" font-size="12">• Oil Lubricants</text>
    <text x="167" y="160" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">• Maglev Trains (No Contact!)</text>

    <rect x="310" y="40" width="245" height="160" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="432" y="72" text-anchor="middle" fill="#fcd34d" font-size="14" font-weight="bold">Capstan Rope Effect</text>
    <text x="432" y="108" text-anchor="middle" fill="#cbd5e1" font-size="12">Wrapping rope around a post</text>
    <text x="432" y="132" text-anchor="middle" fill="#cbd5e1" font-size="12">multiplies friction exponentially,</text>
    <text x="432" y="156" text-anchor="middle" fill="#fde68a" font-size="12" font-weight="bold">holding huge ships easily!</text>
  </svg>
</div>""",

    15: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-amber-300 uppercase">Applied Scenarios: Revise, Reflect, Refine</span>
    <span class="text-xs text-slate-400">Force Diagrams</span>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="35" y="30" width="255" height="82" rx="10" fill="#0f172a" stroke="#06b6d4"/>
    <text x="162" y="60" text-anchor="middle" fill="#67e8f9" font-size="13" font-weight="bold">Sailor Jump & Boat</text>
    <text x="162" y="84" text-anchor="middle" fill="#cbd5e1" font-size="11">Sailor → Forward | Boat ← Backward</text>

    <rect x="310" y="30" width="255" height="82" rx="10" fill="#0f172a" stroke="#10b981"/>
    <text x="437" y="60" text-anchor="middle" fill="#6ee7b7" font-size="13" font-weight="bold">Football Kick Contact</text>
    <text x="437" y="84" text-anchor="middle" fill="#cbd5e1" font-size="11">F = Δp / Δt = mv / Δt</text>

    <rect x="35" y="128" width="255" height="82" rx="10" fill="#0f172a" stroke="#f59e0b"/>
    <text x="162" y="158" text-anchor="middle" fill="#fcd34d" font-size="13" font-weight="bold">Bullet Penetration</text>
    <text x="162" y="182" text-anchor="middle" fill="#cbd5e1" font-size="11">v² = u² + 2as ⇒ F_resist = ma</text>

    <rect x="310" y="128" width="255" height="82" rx="10" fill="#0f172a" stroke="#a78bfa"/>
    <text x="437" y="158" text-anchor="middle" fill="#ddd6fe" font-size="13" font-weight="bold">Compass Needle</text>
    <text x="437" y="182" text-anchor="middle" fill="#cbd5e1" font-size="11">Non-contact magnetic pair</text>
  </svg>
</div>""",

    16: """<div class="w-full h-full flex flex-col justify-between gap-2 p-2">
  <div class="flex items-center justify-between bg-slate-900/80 border border-slate-700/60 rounded-xl px-3 py-2">
    <span class="text-xs font-bold text-emerald-300 uppercase">Chapter 6 At a Glance: Newton's Laws</span>
    <span class="text-xs text-slate-400">Ready for Quizzes 17–20</span>
  </div>
  <svg viewBox="0 0 600 240" class="w-full flex-1 bg-slate-950/60 rounded-xl border border-slate-800">
    <rect x="30" y="25" width="170" height="105" rx="10" fill="#0f172a" stroke="#06b6d4"/>
    <text x="115" y="54" text-anchor="middle" fill="#67e8f9" font-size="13" font-weight="bold">First Law</text>
    <text x="115" y="80" text-anchor="middle" fill="#cbd5e1" font-size="11">Inertia (Mass)</text>
    <text x="115" y="102" text-anchor="middle" fill="#cbd5e1" font-size="11">F_net = 0 ⇒ v const</text>

    <rect x="215" y="25" width="170" height="105" rx="10" fill="#0f172a" stroke="#10b981"/>
    <text x="300" y="54" text-anchor="middle" fill="#6ee7b7" font-size="13" font-weight="bold">Second Law</text>
    <text x="300" y="80" text-anchor="middle" fill="#cbd5e1" font-size="12" font-weight="bold">F = ma = Δp/Δt</text>
    <text x="300" y="102" text-anchor="middle" fill="#cbd5e1" font-size="11">1 N = 1 kg m s⁻²</text>

    <rect x="400" y="25" width="170" height="105" rx="10" fill="#0f172a" stroke="#f59e0b"/>
    <text x="485" y="54" text-anchor="middle" fill="#fcd34d" font-size="13" font-weight="bold">Third Law</text>
    <text x="485" y="80" text-anchor="middle" fill="#cbd5e1" font-size="11">Action = -Reaction</text>
    <text x="485" y="102" text-anchor="middle" fill="#cbd5e1" font-size="11">2 different bodies</text>

    <rect x="55" y="148" width="490" height="68" rx="12" fill="#1e293b" stroke="#38bdf8"/>
    <text x="300" y="186" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">Systems: a = F / (m₁ + m₂)  |  Proceed to Silent Mastery Quizzes!</text>
  </svg>
</div>"""
}
