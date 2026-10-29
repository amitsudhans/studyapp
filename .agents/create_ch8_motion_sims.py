# -*- coding: utf-8 -*-
"""
Generates .agents/class7_science_time_motion_sims.py containing 16 interactive simulators
for Class 7 Science Chapter 8: Measurement of Time and Motion.
"""

simulators = {}

# 1. natural_time_cycles_sim
simulators["natural_time_cycles_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">8.1 Astronomy Lab</span>
      <h4 class="text-sm font-bold text-slate-100">Celestial Rhythms: Solar Day, Lunar Month & Solar Year</h4>
    </div>
    <div class="flex gap-1.5" id="cycleTabs">
      <button onclick="window.switchCycleTab('day')" id="btnCycleDay" class="px-3 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md">1. Solar Day</button>
      <button onclick="window.switchCycleTab('month')" id="btnCycleMonth" class="px-3 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">2. Lunar Month</button>
      <button onclick="window.switchCycleTab('year')" id="btnCycleYear" class="px-3 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">3. Solar Year</button>
    </div>
  </div>

  <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="celestialSvg" viewBox="0 0 600 240" class="w-full h-full">
      <!-- Stars background -->
      <g opacity="0.6">
        <circle cx="45" cy="30" r="1" fill="#fff"/>
        <circle cx="120" cy="70" r="1.5" fill="#fef08a"/>
        <circle cx="200" cy="25" r="1" fill="#fff"/>
        <circle cx="340" cy="40" r="1.2" fill="#fff"/>
        <circle cx="480" cy="65" r="1.5" fill="#fef08a"/>
        <circle cx="550" cy="30" r="1" fill="#fff"/>
        <circle cx="80" cy="180" r="1.2" fill="#fff"/>
        <circle cx="280" cy="210" r="1" fill="#fff"/>
        <circle cx="450" cy="195" r="1.5" fill="#fff"/>
        <circle cx="530" cy="170" r="1" fill="#fef08a"/>
      </g>

      <!-- View Container dynamically updated by JS -->
      <g id="celestialVisualGroup">
        <!-- Default Day View: Earth Rotating with Day/Night line -->
      </g>
    </svg>
    <div id="cycleOverlayBadge" class="absolute bottom-2 left-3 bg-slate-900/80 border border-slate-700 text-xs px-3 py-1 rounded-lg text-amber-300 font-mono">
      Earth Rotation: 12.0 h (Noon)
    </div>
  </div>

  <div class="mt-3 flex flex-wrap items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <div class="flex items-center gap-2 flex-1 min-w-[200px]">
      <label id="cycleSliderLabel" class="text-slate-300 font-medium">Rotation Angle:</label>
      <input type="range" id="cycleSlider" min="0" max="360" value="180" class="flex-1 accent-amber-500 h-1.5 bg-slate-700 rounded-lg cursor-pointer" oninput="window.updateCelestialCycle(this.value)">
      <span id="cycleSliderValue" class="font-mono text-amber-300 w-12 text-right">180°</span>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="window.toggleCelestialAuto()" id="btnCycleAuto" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold transition">▶ Animate Cycle</button>
      <button onclick="window.resetCelestialCycle()" class="px-2.5 py-1.5 rounded-lg bg-slate-700 hover:bg-slate-600 text-slate-300 font-semibold transition">↺ Reset</button>
    </div>
  </div>
  <p id="cycleExplanation" class="mt-2 text-xs text-slate-400 leading-relaxed">
    <strong>Solar Day:</strong> Caused by Earth's axial rotation (360° every 24 hours). Sunrise to sunrise = 1 day.
  </p>
</div>
"""

# 2. ancient_clocks_sim
simulators["ancient_clocks_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">8.1 Early Clocks</span>
      <h4 class="text-sm font-bold text-slate-100">Sundials, Clepsydrae & Sand Hourglasses</h4>
    </div>
    <div class="flex gap-1.5" id="ancientClockTabs">
      <button onclick="window.switchAncientTab('sundial')" id="btnTabSundial" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md">Sundial</button>
      <button onclick="window.switchAncientTab('water')" id="btnTabWater" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">Water Clock</button>
      <button onclick="window.switchAncientTab('sand')" id="btnTabSand" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">Hourglass</button>
    </div>
  </div>

  <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="ancientClockSvg" viewBox="0 0 600 240" class="w-full h-full">
      <g id="ancientClockGroup"></g>
    </svg>
    <div id="ancientStatusBadge" class="absolute top-2 right-3 bg-slate-900/85 border border-slate-700 text-xs px-3 py-1 rounded-lg text-amber-300 font-mono">
      Time: 12:00 PM (Solar Noon)
    </div>
  </div>

  <div class="mt-3 flex flex-wrap items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <div class="flex items-center gap-2 flex-1 min-w-[200px]" id="ancientControlContainer">
      <label id="ancientControlLabel" class="text-slate-300 font-medium">Sun Position:</label>
      <input type="range" id="ancientSlider" min="6" max="18" step="0.25" value="12" class="flex-1 accent-amber-500 h-1.5 bg-slate-700 rounded-lg cursor-pointer" oninput="window.updateAncientClock(this.value)">
      <span id="ancientControlValue" class="font-mono text-amber-300 w-16 text-right">12:00 PM</span>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="window.toggleAncientAction()" id="btnAncientAction" class="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-semibold transition">▶ Advance Sun</button>
      <button onclick="window.resetAncientClock()" class="px-2.5 py-1.5 rounded-lg bg-slate-700 hover:bg-slate-600 text-slate-300 font-semibold transition">↺ Reset</button>
    </div>
  </div>
  <p id="ancientDescription" class="mt-2 text-xs text-slate-400 leading-relaxed">
    <strong>Sundial:</strong> Triangular gnomon casts a shadow across a circular calibrated dial plate as the Sun traverses the sky.
  </p>
</div>
"""

# 3. clock_evolution_sim
simulators["clock_evolution_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-cyan-500/20 text-cyan-300 text-xs font-bold rounded-lg border border-cyan-500/30">8.1 Precision Evolution</span>
      <h4 class="text-sm font-bold text-slate-100">Mechanical Escapement → Quartz Crystal → Cesium Atomic</h4>
    </div>
    <div class="flex gap-1.5">
      <button onclick="window.switchEvoTab('mechanical')" id="btnEvoMech" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-cyan-500 text-slate-950 shadow-md">Mechanical</button>
      <button onclick="window.switchEvoTab('quartz')" id="btnEvoQuartz" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">Quartz (32 kHz)</button>
      <button onclick="window.switchEvoTab('atomic')" id="btnEvoAtomic" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">Cesium-133</button>
    </div>
  </div>

  <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="evoSvg" viewBox="0 0 600 240" class="w-full h-full">
      <g id="evoVisualGroup"></g>
    </svg>
    <div id="evoMetricsBadge" class="absolute bottom-2 right-3 bg-slate-900/90 border border-slate-700 text-xs px-3 py-1 rounded-lg text-cyan-300 font-mono">
      Frequency: 1.0 Hz • Accuracy: ±15 s/day
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <div class="flex items-center gap-3">
      <span class="text-slate-300 font-medium">Mechanism State:</span>
      <span id="evoStateText" class="px-2.5 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-mono font-bold">Oscillating</span>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="window.toggleEvoRun()" id="btnEvoRun" class="px-3 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-semibold transition">⏸ Pause</button>
      <button onclick="window.pulseEvo()" class="px-2.5 py-1.5 rounded-lg bg-slate-700 hover:bg-slate-600 text-slate-300 font-semibold transition">Single Step</button>
    </div>
  </div>
  <p id="evoExplanation" class="mt-2 text-xs text-slate-400 leading-relaxed">
    <strong>Mechanical Escapement:</strong> Escapement wheel regulated by swinging balance wheel or pendulum releases gears one tooth per second.
  </p>
</div>
"""

# 4. pendulum_anatomy_sim
simulators["pendulum_anatomy_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">8.1.1 Anatomy</span>
      <h4 class="text-sm font-bold text-slate-100">Anatomy of a Simple Pendulum: Equilibrium & Extreme Points</h4>
    </div>
    <div class="flex items-center gap-2 text-xs">
      <span class="text-slate-400">Length (L):</span>
      <span id="pendulumLengthDisplay" class="font-mono text-amber-300 font-bold">80 cm</span>
    </div>
  </div>

  <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="pendulumAnatomySvg" viewBox="0 0 600 240" class="w-full h-full">
      <!-- Grid lines -->
      <line x1="300" y1="20" x2="300" y2="230" stroke="#334155" stroke-dasharray="4 4" stroke-width="1"/>
      <line x1="100" y1="200" x2="500" y2="200" stroke="#1e293b" stroke-width="1"/>

      <!-- Rigid Support -->
      <rect x="250" y="12" width="100" height="12" rx="3" fill="#64748b"/>
      <polygon points="245,12 355,12 345,6 255,6" fill="#475569"/>
      <circle cx="300" cy="24" r="4" fill="#f59e0b"/>

      <!-- Trajectory Arc -->
      <path id="anatomyArc" d="M 210,185 Q 300,205 390,185" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 3" opacity="0.6"/>

      <!-- Pendulum String & Bob (animated) -->
      <g id="anatomyPendulumArm">
        <line id="anatomyString" x1="300" y1="24" x2="300" y2="195" stroke="#94a3b8" stroke-width="2"/>
        <circle id="anatomyBob" cx="300" cy="195" r="14" fill="url(#metalGrad)" stroke="#cbd5e1" stroke-width="1.5"/>
        <circle cx="300" cy="195" r="3" fill="#f8fafc"/>
      </g>

      <!-- Gradients -->
      <defs>
        <radialGradient id="metalGrad" cx="35%" cy="35%" r="65%">
          <stop offset="0%" stop-color="#fef08a"/>
          <stop offset="50%" stop-color="#f59e0b"/>
          <stop offset="100%" stop-color="#78350f"/>
        </radialGradient>
      </defs>

      <!-- Labels -->
      <text x="300" y="222" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">O (Mean / Equilibrium)</text>
      <text x="210" y="170" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">A (Left Extreme)</text>
      <text x="390" y="170" text-anchor="middle" fill="#4ade80" font-size="11" font-weight="bold">B (Right Extreme)</text>
    </svg>

    <div class="absolute top-2 left-3 bg-slate-900/80 border border-slate-700 text-xs px-3 py-1 rounded-lg text-slate-300">
      Displacement: <span id="anatomyAngleBadge" class="font-mono text-amber-300 font-bold">0.0°</span>
    </div>
    <div class="absolute top-2 right-3 bg-slate-900/80 border border-slate-700 text-xs px-3 py-1 rounded-lg text-slate-300">
      1 Oscillation = <span class="text-amber-300 font-mono font-bold">O → A → O → B → O</span>
    </div>
  </div>

  <div class="mt-3 flex flex-wrap items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <div class="flex items-center gap-2 flex-1 min-w-[200px]">
      <label class="text-slate-300 font-medium">Drag / Tilt Angle:</label>
      <input type="range" id="anatomyAngleSlider" min="-30" max="30" value="0" class="flex-1 accent-amber-500 h-1.5 bg-slate-700 rounded-lg cursor-pointer" oninput="window.setAnatomyAngle(this.value)">
      <span id="anatomyAngleText" class="font-mono text-amber-300 w-12 text-right">0°</span>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="window.startAnatomyOscillation()" id="btnAnatomyOscillate" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold transition">▶ Release to Swing</button>
      <button onclick="window.resetAnatomy()" class="px-2.5 py-1.5 rounded-lg bg-slate-700 hover:bg-slate-600 text-slate-300 font-semibold transition">↺ Center</button>
    </div>
  </div>
  <p class="mt-2 text-xs text-slate-400 leading-relaxed">
    When released from an extreme position (A or B), the bob accelerates toward the mean position O due to gravity, overshoots toward the opposite extreme, and repeats periodically.
  </p>
</div>
"""

# 5. pendulum_isochronism_sim
simulators["pendulum_isochronism_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">8.1.1 Galileo's Law</span>
      <h4 class="text-sm font-bold text-slate-100">Galileo's Isochronism: Mass & Amplitude Independence</h4>
    </div>
    <span class="text-xs font-mono text-emerald-400 bg-emerald-950/60 border border-emerald-800/80 px-2.5 py-0.5 rounded">T = 2π √(L / g)</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
    <!-- Visual Canvas -->
    <div class="md:col-span-2 relative h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
      <svg id="isoSvg" viewBox="0 0 400 240" class="w-full h-full">
        <line x1="200" y1="15" x2="200" y2="235" stroke="#334155" stroke-dasharray="3 3"/>
        <rect x="150" y="10" width="100" height="8" rx="2" fill="#64748b"/>
        <circle cx="200" cy="18" r="3" fill="#f59e0b"/>

        <!-- Oscillating String and Bob -->
        <g id="isoArm">
          <line id="isoLine" x1="200" y1="18" x2="200" y2="180" stroke="#e2e8f0" stroke-width="2"/>
          <circle id="isoBob" cx="200" cy="180" r="16" fill="#f59e0b" stroke="#fff" stroke-width="1.5"/>
        </g>
      </svg>
      <div class="absolute top-2 left-2 bg-slate-900/80 border border-slate-700 text-xs px-2.5 py-1 rounded text-slate-300">
        Oscillations: <span id="isoCount" class="text-amber-300 font-mono font-bold">0 / 20</span>
      </div>
      <div class="absolute top-2 right-2 bg-slate-900/80 border border-slate-700 text-xs px-2.5 py-1 rounded text-slate-300">
        Time: <span id="isoStopwatch" class="text-cyan-300 font-mono font-bold">0.00 s</span>
      </div>
      <div class="absolute bottom-2 left-2 right-2 bg-slate-900/85 border border-slate-700 text-xs p-1.5 rounded flex justify-between items-center font-mono">
        <span class="text-slate-300">Calculated Time Period T:</span>
        <span id="isoPeriodResult" class="text-amber-300 font-bold text-sm">-- s</span>
      </div>
    </div>

    <!-- Controls Panel -->
    <div class="flex flex-col justify-between gap-2 bg-slate-800/60 p-3 rounded-xl border border-slate-700/60 text-xs">
      <div>
        <div class="flex justify-between items-center mb-1">
          <label class="text-slate-300 font-medium">String Length (L):</label>
          <span id="isoLenText" class="font-mono text-amber-300 font-bold">100 cm</span>
        </div>
        <input type="range" id="isoLenSlider" min="25" max="100" step="25" value="100" class="w-full accent-amber-500 h-1.5 bg-slate-700 rounded-lg cursor-pointer" oninput="window.updateIsoParams()">
        <div class="flex justify-between text-[10px] text-slate-400 mt-0.5">
          <span>25 cm (1.0 s)</span><span>50 cm (1.4 s)</span><span>100 cm (2.0 s)</span>
        </div>
      </div>

      <div>
        <div class="flex justify-between items-center mb-1">
          <label class="text-slate-300 font-medium">Bob Mass (m):</label>
          <span id="isoMassText" class="font-mono text-cyan-300 font-bold">100 g (Brass)</span>
        </div>
        <select id="isoMassSelect" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-2 py-1 text-slate-200 cursor-pointer" onchange="window.updateIsoParams()">
          <option value="20">20 g (Light Wood)</option>
          <option value="100" selected>100 g (Brass Bob)</option>
          <option value="300">300 g (Heavy Lead)</option>
        </select>
      </div>

      <div>
        <div class="flex justify-between items-center mb-1">
          <label class="text-slate-300 font-medium">Swing Amplitude (θ):</label>
          <span id="isoAmpText" class="font-mono text-purple-300 font-bold">15°</span>
        </div>
        <input type="range" id="isoAmpSlider" min="5" max="25" step="5" value="15" class="w-full accent-purple-500 h-1.5 bg-slate-700 rounded-lg cursor-pointer" oninput="window.updateIsoParams()">
      </div>

      <div class="flex gap-2 pt-1 border-t border-slate-700">
        <button onclick="window.runIsoExperiment()" id="btnIsoRun" class="flex-1 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold transition">▶ Time 20 Swings</button>
        <button onclick="window.resetIso()" class="px-2.5 py-1.5 rounded-lg bg-slate-700 hover:bg-slate-600 text-slate-300 font-semibold transition">↺</button>
      </div>
    </div>
  </div>
  <p class="mt-2 text-xs text-slate-400 leading-relaxed">
    Notice: Changing the mass or angle leaves the time period <strong>strictly unchanged</strong>! Only changing the length changes the period.
  </p>
</div>
"""

# 6. si_time_units_formatter_sim
simulators["si_time_units_formatter_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">8.1.2 SI Grammar</span>
      <h4 class="text-sm font-bold text-slate-100">SI Units of Time & International Syntax Validator</h4>
    </div>
    <span class="text-xs font-mono text-cyan-300 bg-cyan-950/60 border border-cyan-800/80 px-2.5 py-0.5 rounded">SI Base Unit: second (s)</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <!-- Converter Box -->
    <div class="bg-slate-800/60 p-3.5 rounded-xl border border-slate-700/60 flex flex-col justify-between">
      <div>
        <h5 class="text-slate-200 font-bold mb-2 flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-amber-400"></span>Time Unit Converter
        </h5>
        <div class="flex gap-2 mb-2">
          <input type="number" id="timeConvertInput" value="1" min="0" step="any" class="w-24 bg-slate-900 border border-slate-700 rounded-lg px-2 py-1 text-slate-100 font-mono text-sm" oninput="window.calcTimeUnits()">
          <select id="timeConvertUnit" class="flex-1 bg-slate-900 border border-slate-700 rounded-lg px-2 py-1 text-slate-100 text-xs" onchange="window.calcTimeUnits()">
            <option value="d">Days (d)</option>
            <option value="h">Hours (h)</option>
            <option value="min">Minutes (min)</option>
            <option value="s">Seconds (s)</option>
          </select>
        </div>
      </div>

      <div class="space-y-1.5 font-mono text-xs bg-slate-950/60 p-2.5 rounded-lg border border-slate-800">
        <div class="flex justify-between"><span class="text-slate-400">Seconds (s):</span><span id="resSec" class="text-amber-300 font-bold">86,400 s</span></div>
        <div class="flex justify-between"><span class="text-slate-400">Minutes (min):</span><span id="resMin" class="text-cyan-300">1,440 min</span></div>
        <div class="flex justify-between"><span class="text-slate-400">Hours (h):</span><span id="resHour" class="text-emerald-300">24 h</span></div>
        <div class="flex justify-between"><span class="text-slate-400">Days (d):</span><span id="resDay" class="text-purple-300">1.0 d</span></div>
      </div>
    </div>

    <!-- Syntax Validator -->
    <div class="bg-slate-800/60 p-3.5 rounded-xl border border-slate-700/60 flex flex-col justify-between">
      <div>
        <h5 class="text-slate-200 font-bold mb-2 flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-cyan-400"></span>Scientific SI Notation Checker
        </h5>
        <p class="text-slate-400 mb-2">Test how you write time units. Is it valid scientific notation?</p>
        <div class="flex gap-2 mb-2">
          <input type="text" id="siGrammarInput" value="25 s" placeholder="e.g. 25 s, 25 secs, 25 s." class="flex-1 bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1 text-slate-100 font-mono text-sm" oninput="window.validateSIGrammar(this.value)">
        </div>
      </div>

      <div id="siGrammarFeedback" class="p-2.5 rounded-lg border bg-emerald-950/50 border-emerald-700/70 text-emerald-300">
        <div class="flex items-center gap-1.5 font-bold"><span class="text-base">✓</span> Correct SI Notation!</div>
        <p class="text-[11px] mt-1 text-emerald-200/90 leading-tight">Symbol is strictly lowercase 's', separated by a space, never pluralized, and has no period.</p>
      </div>

      <div class="flex flex-wrap gap-1.5 mt-2">
        <button onclick="window.setSIExample('10 s')" class="px-2 py-0.5 rounded bg-slate-700 hover:bg-slate-600 text-[10px] text-slate-300">10 s</button>
        <button onclick="window.setSIExample('10 secs')" class="px-2 py-0.5 rounded bg-slate-700 hover:bg-slate-600 text-[10px] text-slate-300">10 secs</button>
        <button onclick="window.setSIExample('10 s.')" class="px-2 py-0.5 rounded bg-slate-700 hover:bg-slate-600 text-[10px] text-slate-300">10 s.</button>
        <button onclick="window.setSIExample('10 SEC')" class="px-2 py-0.5 rounded bg-slate-700 hover:bg-slate-600 text-[10px] text-slate-300">10 SEC</button>
      </div>
    </div>
  </div>
</div>
"""

# 7. slow_or_fast_sim
simulators["slow_or_fast_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">8.2 Comparative Motion</span>
      <h4 class="text-sm font-bold text-slate-100">Comparing Motion: Equal Time vs. Equal Distance</h4>
    </div>
    <div class="flex gap-1.5">
      <button onclick="window.setSlowFastMode('equal_time')" id="btnModeEqTime" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md">Equal Time (10 s)</button>
      <button onclick="window.setSlowFastMode('equal_dist')" id="btnModeEqDist" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">Equal Distance (200 m)</button>
    </div>
  </div>

  <div class="relative w-full h-56 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden p-3 flex flex-col justify-around">
    <!-- Lane 1: Cheetah / Red Racer -->
    <div class="relative">
      <div class="flex justify-between text-xs text-rose-300 font-semibold mb-1">
        <span>Lane A: Cheetah (Speed: 25 m/s)</span>
        <span id="laneADist" class="font-mono">d = 0 m</span>
      </div>
      <div class="relative h-8 bg-slate-900 rounded-lg border border-slate-700 overflow-hidden">
        <div class="absolute inset-y-0 right-4 w-1 bg-amber-400 opacity-60 border-r border-dashed border-amber-200"></div>
        <div id="laneAIcon" class="absolute top-1 left-2 flex items-center gap-1 text-xs px-2 py-0.5 rounded bg-rose-600 text-white transition-all duration-75">
          🐆 <span>Racer A</span>
        </div>
      </div>
    </div>

    <!-- Lane 2: Elephant / Blue Cruiser -->
    <div class="relative">
      <div class="flex justify-between text-xs text-sky-300 font-semibold mb-1">
        <span>Lane B: Elephant (Speed: 10 m/s)</span>
        <span id="laneBDist" class="font-mono">d = 0 m</span>
      </div>
      <div class="relative h-8 bg-slate-900 rounded-lg border border-slate-700 overflow-hidden">
        <div class="absolute inset-y-0 right-4 w-1 bg-amber-400 opacity-60 border-r border-dashed border-amber-200"></div>
        <div id="laneBIcon" class="absolute top-1 left-2 flex items-center gap-1 text-xs px-2 py-0.5 rounded bg-sky-600 text-white transition-all duration-75">
          🐘 <span>Racer B</span>
        </div>
      </div>
    </div>

    <!-- Stopwatch & Analytics -->
    <div class="flex justify-between items-center text-xs bg-slate-900/90 px-3 py-1.5 rounded-lg border border-slate-800">
      <span class="text-slate-400">Elapsed Time: <strong id="slowFastTimer" class="font-mono text-amber-300 text-sm">0.0 s</strong></span>
      <span id="slowFastVerdict" class="text-emerald-400 font-bold">Ready to Start Race</span>
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <span id="slowFastInstruction" class="text-slate-300">In equal time (10 s), the object covering greater distance is faster.</span>
    <div class="flex gap-2">
      <button onclick="window.startSlowFastRace()" id="btnSlowFastStart" class="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold transition">▶ Start Race</button>
      <button onclick="window.resetSlowFast()" class="px-2.5 py-1.5 rounded-lg bg-slate-700 hover:bg-slate-600 text-slate-300 font-semibold transition">↺ Reset</button>
    </div>
  </div>
</div>
"""

# 8. speed_definition_sim
simulators["speed_definition_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">8.3 Core Formula</span>
      <h4 class="text-sm font-bold text-slate-100">Speed Definition: Distance Covered per Unit Time</h4>
    </div>
    <span class="text-xs font-mono text-amber-400 bg-amber-950/60 border border-amber-800/80 px-2.5 py-0.5 rounded">Speed = Distance / Time</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
    <!-- Live Gauge -->
    <div class="relative h-60 bg-slate-950 rounded-xl border border-slate-800 flex flex-col items-center justify-center p-3">
      <svg viewBox="0 0 200 130" class="w-48 h-32">
        <path d="M 20,110 A 80,80 0 0,1 180,110" fill="none" stroke="#334155" stroke-width="14" stroke-linecap="round"/>
        <path id="gaugeSpeedArc" d="M 20,110 A 80,80 0 0,1 100,30" fill="none" stroke="#f59e0b" stroke-width="14" stroke-linecap="round"/>
        <!-- Needle -->
        <g id="gaugeNeedleGroup" transform="rotate(45, 100, 110)">
          <line x1="100" y1="110" x2="100" y2="40" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
          <circle cx="100" cy="110" r="7" fill="#f8fafc"/>
        </g>
        <text x="100" y="100" text-anchor="middle" fill="#94a3b8" font-size="10">SPEED</text>
      </svg>
      <div class="text-center mt-1">
        <div id="gaugeSpeedText" class="text-2xl font-mono font-black text-amber-400">20.0 m/s</div>
        <div id="gaugeKmhText" class="text-xs font-mono text-slate-400">72.0 km/h</div>
      </div>
    </div>

    <!-- Sliders and Benchmarks -->
    <div class="md:col-span-2 flex flex-col justify-between gap-2.5 bg-slate-800/60 p-3 rounded-xl border border-slate-700/60 text-xs">
      <div>
        <div class="flex justify-between items-center mb-1">
          <label class="text-slate-300 font-medium">Total Distance Covered (d):</label>
          <span id="speedDistText" class="font-mono text-amber-300 font-bold">400 m</span>
        </div>
        <input type="range" id="speedDistSlider" min="50" max="1000" step="10" value="400" class="w-full accent-amber-500 h-1.5 bg-slate-700 rounded-lg cursor-pointer" oninput="window.calcSpeedDef()">
      </div>

      <div>
        <div class="flex justify-between items-center mb-1">
          <label class="text-slate-300 font-medium">Total Time Taken (t):</label>
          <span id="speedTimeText" class="font-mono text-cyan-300 font-bold">20 s</span>
        </div>
        <input type="range" id="speedTimeSlider" min="2" max="60" step="1" value="20" class="w-full accent-cyan-500 h-1.5 bg-slate-700 rounded-lg cursor-pointer" oninput="window.calcSpeedDef()">
      </div>

      <div class="pt-2 border-t border-slate-700">
        <span class="text-slate-400 font-medium block mb-1">Nature's Speed Benchmarks:</span>
        <div class="flex flex-wrap gap-1.5">
          <button onclick="window.setSpeedPreset(1.4, 'Walking Human')" class="px-2 py-1 rounded bg-slate-700 hover:bg-slate-600 text-slate-200">🚶 Human (1.4 m/s)</button>
          <button onclick="window.setSpeedPreset(10.4, 'Usain Bolt')" class="px-2 py-1 rounded bg-slate-700 hover:bg-slate-600 text-slate-200">🏃 Sprinter (10.4 m/s)</button>
          <button onclick="window.setSpeedPreset(30, 'Cheetah')" class="px-2 py-1 rounded bg-slate-700 hover:bg-slate-600 text-slate-200">🐆 Cheetah (30 m/s)</button>
          <button onclick="window.setSpeedPreset(340, 'Speed of Sound')" class="px-2 py-1 rounded bg-slate-700 hover:bg-slate-600 text-slate-200">⚡ Sound (340 m/s)</button>
        </div>
      </div>
    </div>
  </div>
</div>
"""

# 9. speed_unit_converter_sim
simulators["speed_unit_converter_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">8.3 Unit Multipliers</span>
      <h4 class="text-sm font-bold text-slate-100">Speed Unit Converter: × (5/18) vs × (18/5)</h4>
    </div>
    <div class="flex gap-1.5">
      <button onclick="window.setConvDirection('kmh_to_ms')" id="btnDirKmhToMs" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md">km/h → m/s [× 5/18]</button>
      <button onclick="window.setConvDirection('ms_to_kmh')" id="btnDirMsToKmh" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">m/s → km/h [× 18/5]</button>
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
    <!-- Math Step-by-Step Card -->
    <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 flex flex-col justify-around text-xs font-mono">
      <div class="text-slate-400 text-[11px] mb-1">Mathematical Derivation:</div>
      <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800 space-y-1">
        <div class="text-amber-300 font-bold">1 km/h = 1000 m / 3600 s</div>
        <div class="text-slate-300">= 10 / 36 m/s</div>
        <div class="text-emerald-400 font-bold text-sm">= 5 / 18 m/s ≈ 0.2778 m/s</div>
      </div>
      <div class="mt-2 text-slate-400 text-[11px]">Reverse Multiplier:</div>
      <div class="bg-slate-900 p-2 rounded-lg border border-slate-800 text-cyan-300 font-bold">
        1 m/s = 3600 / 1000 km/h = 18 / 5 km/h = 3.6 km/h
      </div>
    </div>

    <!-- Interactive Transformer -->
    <div class="bg-slate-800/60 p-3.5 rounded-xl border border-slate-700/60 flex flex-col justify-between text-xs">
      <div>
        <div class="flex justify-between items-center mb-1">
          <label id="convInputLabel" class="text-slate-300 font-medium">Input Speed in km/h:</label>
          <span id="convInputValue" class="font-mono text-amber-300 font-bold text-sm">72 km/h</span>
        </div>
        <input type="range" id="convSlider" min="0" max="180" step="18" value="72" class="w-full accent-amber-500 h-1.5 bg-slate-700 rounded-lg cursor-pointer" oninput="window.updateSpeedConv(this.value)">
        <div class="flex justify-between text-[10px] text-slate-400 mt-0.5">
          <span>0</span><span>36</span><span>72</span><span>108</span><span>144</span><span>180</span>
        </div>
      </div>

      <div class="my-3 text-center bg-slate-900/90 p-3 rounded-xl border border-slate-700">
        <div class="text-slate-400 text-[11px] mb-0.5">Calculated Result:</div>
        <div id="convResultValue" class="text-2xl font-mono font-black text-emerald-400">20.0 m/s</div>
        <div id="convFormulaStep" class="text-xs font-mono text-slate-400 mt-1">72 × (5/18) = 4 × 5 = 20 m/s</div>
      </div>

      <div class="flex gap-1.5">
        <button onclick="window.setPresetConv(36)" class="flex-1 py-1 rounded bg-slate-700 hover:bg-slate-600 text-slate-200">36 km/h</button>
        <button onclick="window.setPresetConv(72)" class="flex-1 py-1 rounded bg-slate-700 hover:bg-slate-600 text-slate-200">72 km/h</button>
        <button onclick="window.setPresetConv(90)" class="flex-1 py-1 rounded bg-slate-700 hover:bg-slate-600 text-slate-200">90 km/h</button>
        <button onclick="window.setPresetConv(126)" class="flex-1 py-1 rounded bg-slate-700 hover:bg-slate-600 text-slate-200">126 km/h</button>
      </div>
    </div>
  </div>
</div>
"""

# 10. speed_triangle_sim
simulators["speed_triangle_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">8.3.1 Magic Triangle</span>
      <h4 class="text-sm font-bold text-slate-100">Speed-Distance-Time Formula Triangle</h4>
    </div>
    <span class="text-xs text-slate-400">Click any sector to solve for it!</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
    <!-- Interactive Triangle SVG -->
    <div class="relative h-60 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2">
      <svg viewBox="0 0 240 200" class="w-56 h-48 cursor-pointer">
        <!-- Triangle Base -->
        <polygon points="120,20 20,180 220,180" fill="#1e293b" stroke="#475569" stroke-width="2"/>
        
        <!-- Divider lines -->
        <line x1="70" y1="100" x2="170" y2="100" stroke="#f59e0b" stroke-width="3"/>
        <line x1="120" y1="100" x2="120" y2="180" stroke="#f59e0b" stroke-width="3"/>

        <!-- Top Sector: Distance (D) -->
        <polygon id="triDistSector" points="120,25 75,95 165,95" fill="#f59e0b" opacity="0.25" onclick="window.selectTriangleVar('D')" class="hover:opacity-40 transition"/>
        <text x="120" y="70" text-anchor="middle" fill="#fbbf24" font-size="22" font-weight="black" pointer-events="none">D</text>
        <text x="120" y="85" text-anchor="middle" fill="#fef08a" font-size="9" pointer-events="none">DISTANCE</text>

        <!-- Bottom Left: Speed (S) -->
        <polygon id="triSpeedSector" points="25,175 70,105 115,105 115,175" fill="#38bdf8" opacity="0.25" onclick="window.selectTriangleVar('S')" class="hover:opacity-40 transition"/>
        <text x="70" y="145" text-anchor="middle" fill="#38bdf8" font-size="22" font-weight="black" pointer-events="none">S</text>
        <text x="70" y="160" text-anchor="middle" fill="#bae6fd" font-size="9" pointer-events="none">SPEED</text>

        <!-- Bottom Right: Time (T) -->
        <polygon id="triTimeSector" points="125,105 170,105 215,175 125,175" fill="#4ade80" opacity="0.25" onclick="window.selectTriangleVar('T')" class="hover:opacity-40 transition"/>
        <text x="170" y="145" text-anchor="middle" fill="#4ade80" font-size="22" font-weight="black" pointer-events="none">T</text>
        <text x="170" y="160" text-anchor="middle" fill="#bbf7d0" font-size="9" pointer-events="none">TIME</text>
      </svg>
    </div>

    <!-- Active Formula & Live Problem Solver -->
    <div class="bg-slate-800/60 p-3.5 rounded-xl border border-slate-700/60 flex flex-col justify-between text-xs">
      <div>
        <div class="flex items-center justify-between mb-2">
          <span class="text-slate-400">Target Variable:</span>
          <span id="triTargetBadge" class="px-2.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-bold font-mono">Distance (D)</span>
        </div>
        <div id="triFormulaBox" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-center font-mono font-bold text-amber-300 text-sm mb-3">
          Distance = Speed × Time
        </div>

        <!-- Inputs container -->
        <div id="triInputsContainer" class="space-y-2">
          <!-- Dynamically populated inputs -->
        </div>
      </div>

      <div class="mt-3 p-2 rounded-lg bg-slate-900 border border-slate-700 flex justify-between items-center font-mono">
        <span class="text-slate-400">Calculated Value:</span>
        <span id="triResultText" class="text-emerald-400 font-bold text-base">300 m</span>
      </div>
    </div>
  </div>
</div>
"""

# 11. average_vs_instantaneous_sim
simulators["average_vs_instantaneous_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">8.3.1 Reality vs Formula</span>
      <h4 class="text-sm font-bold text-slate-100">Average Speed vs. Instantaneous Speed</h4>
    </div>
    <span class="text-xs font-mono text-cyan-300 bg-cyan-950/60 border border-cyan-800/80 px-2.5 py-0.5 rounded">Avg Speed = Total Dist / Total Time</span>
  </div>

  <div class="relative w-full h-56 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden p-3 flex flex-col justify-between">
    <!-- Journey Road Map -->
    <div class="relative mt-2">
      <div class="h-10 bg-slate-900 rounded-lg border border-slate-700 relative overflow-hidden flex">
        <div class="w-1/4 border-r border-dashed border-slate-600 bg-rose-950/20 flex items-center justify-center text-[10px] text-rose-300">City Traffic (20 km/h)</div>
        <div class="w-2/4 border-r border-dashed border-slate-600 bg-emerald-950/20 flex items-center justify-center text-[10px] text-emerald-300">Expressway Cruise (100 km/h)</div>
        <div class="w-1/4 bg-amber-950/20 flex items-center justify-center text-[10px] text-amber-300">Rest Stop (0 km/h)</div>
      </div>
      <div id="journeyCar" class="absolute -top-1 left-2 transition-all duration-100 text-lg">
        🚗
      </div>
    </div>

    <!-- Live Instruments Readout -->
    <div class="grid grid-cols-3 gap-2 text-center text-xs">
      <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
        <div class="text-slate-400 text-[10px]">Instantaneous Speed</div>
        <div id="instSpeedDisplay" class="font-mono text-rose-400 font-bold text-sm">20 km/h</div>
      </div>
      <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
        <div class="text-slate-400 text-[10px]">Cumulative Distance</div>
        <div id="cumDistDisplay" class="font-mono text-cyan-300 font-bold text-sm">0 km</div>
      </div>
      <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
        <div class="text-slate-400 text-[10px]">Overall Average Speed</div>
        <div id="avgSpeedDisplay" class="font-mono text-amber-300 font-bold text-sm">-- km/h</div>
      </div>
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <span class="text-slate-300">A vehicle rarely maintains a uniform speed; school physics speed calculations yield the <strong>average speed</strong>.</span>
    <div class="flex gap-2">
      <button onclick="window.startJourneySim()" id="btnJourneyStart" class="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold transition">▶ Drive Highway</button>
      <button onclick="window.resetJourneySim()" class="px-2.5 py-1.5 rounded-lg bg-slate-700 hover:bg-slate-600 text-slate-300 font-semibold transition">↺</button>
    </div>
  </div>
</div>
"""

# 12. speedo_odometer_sim
simulators["speedo_odometer_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">8.3.1 Vehicle Dashboard</span>
      <h4 class="text-sm font-bold text-slate-100">Speedometer (km/h) & Rolling Drum Odometer (km)</h4>
    </div>
    <span class="text-xs text-slate-400">Two vital instruments on every motor vehicle dashboard</span>
  </div>

  <div class="relative w-full h-60 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-around p-3">
    <!-- Speedometer Dial -->
    <div class="flex flex-col items-center">
      <svg viewBox="0 0 160 110" class="w-40 h-28">
        <path d="M 20,95 A 60,60 0 0,1 140,95" fill="none" stroke="#334155" stroke-width="10" stroke-linecap="round"/>
        <path id="dashSpeedArc" d="M 20,95 A 60,60 0 0,1 80,35" fill="none" stroke="#38bdf8" stroke-width="10" stroke-linecap="round"/>
        <!-- Needle -->
        <g id="dashNeedle" transform="rotate(30, 80, 95)">
          <line x1="80" y1="95" x2="80" y2="45" stroke="#f87171" stroke-width="2.5" stroke-linecap="round"/>
          <circle cx="80" cy="95" r="5" fill="#f8fafc"/>
        </g>
        <text x="80" y="85" text-anchor="middle" fill="#94a3b8" font-size="8">km / h</text>
      </svg>
      <div class="text-center">
        <span class="text-[10px] text-slate-400 uppercase tracking-wider block">Speedometer</span>
        <span id="dashSpeedNum" class="text-lg font-mono font-bold text-sky-400">40 km/h</span>
      </div>
    </div>

    <!-- Odometer Drum -->
    <div class="flex flex-col items-center">
      <div class="bg-black p-2.5 rounded-lg border-2 border-slate-700 shadow-inner flex items-center gap-1 font-mono text-base font-bold text-white tracking-widest">
        <span class="bg-slate-900 px-1.5 py-0.5 rounded border border-slate-800">0</span>
        <span class="bg-slate-900 px-1.5 py-0.5 rounded border border-slate-800">4</span>
        <span class="bg-slate-900 px-1.5 py-0.5 rounded border border-slate-800">5</span>
        <span class="bg-slate-900 px-1.5 py-0.5 rounded border border-slate-800">8</span>
        <span id="odoTenth" class="bg-amber-600 px-1.5 py-0.5 rounded text-slate-950">2</span>
        <span class="text-xs text-slate-400 ml-1">km</span>
      </div>
      <div class="text-center mt-2">
        <span class="text-[10px] text-slate-400 uppercase tracking-wider block">Odometer</span>
        <span class="text-xs text-amber-300 font-mono">Measures Total Distance</span>
      </div>
      <button onclick="window.resetTripOdo()" class="mt-1 px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[10px] text-slate-400">Reset Trip</button>
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <div class="flex items-center gap-2 flex-1">
      <label class="text-slate-300 font-medium">Throttle / Accelerator:</label>
      <input type="range" id="dashThrottle" min="0" max="140" step="5" value="40" class="flex-1 accent-sky-500 h-1.5 bg-slate-700 rounded-lg cursor-pointer" oninput="window.setDashSpeed(this.value)">
      <span id="dashThrottleVal" class="font-mono text-sky-300 w-14 text-right">40 km/h</span>
    </div>
    <button onclick="window.pulseBrake()" class="px-3 py-1.5 rounded-lg bg-rose-700 hover:bg-rose-600 text-white font-semibold transition">Brake</button>
  </div>
</div>
"""

# 13. uniform_linear_motion_sim
simulators["uniform_linear_motion_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">8.4 Uniform Motion</span>
      <h4 class="text-sm font-bold text-slate-100">Uniform Linear Motion: Constant Speed & Straight d-t Line</h4>
    </div>
    <span class="text-xs font-mono text-emerald-400 bg-emerald-950/60 border border-emerald-800/80 px-2.5 py-0.5 rounded">Speed = Constant (20 m/s)</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
    <!-- Straight Track Canvas -->
    <div class="relative h-60 bg-slate-950 rounded-xl border border-slate-800 flex flex-col justify-around p-3">
      <div class="text-xs text-slate-400 flex justify-between">
        <span>Straight Linear Track</span>
        <span id="uniTrackStatus" class="text-emerald-400 font-mono">Cruise Active</span>
      </div>
      <div class="relative h-12 bg-slate-900 rounded-lg border border-slate-700 overflow-hidden flex items-center">
        <!-- Distance markers -->
        <div class="absolute inset-x-0 h-0.5 bg-slate-700"></div>
        <div class="absolute left-[20%] h-3 w-0.5 bg-slate-500"></div>
        <div class="absolute left-[40%] h-3 w-0.5 bg-slate-500"></div>
        <div class="absolute left-[60%] h-3 w-0.5 bg-slate-500"></div>
        <div class="absolute left-[80%] h-3 w-0.5 bg-slate-500"></div>
        <div id="uniCar" class="absolute left-2 transition-all duration-75 text-xl">
          🚙
        </div>
      </div>
      <div class="flex justify-between text-[11px] font-mono text-slate-400">
        <span>0 m</span><span>40 m</span><span>80 m</span><span>120 m</span><span>160 m</span><span>200 m</span>
      </div>
      <div class="bg-slate-900 p-2 rounded-lg border border-slate-800 flex justify-between text-xs">
        <span class="text-slate-400">Equal time (2 s):</span>
        <span class="text-amber-300 font-mono font-bold">Equal distances (40 m every 2 s)</span>
      </div>
    </div>

    <!-- Live Graph Plotter -->
    <div class="relative h-60 bg-slate-950 rounded-xl border border-slate-800 p-2 flex flex-col justify-between">
      <div class="text-[11px] text-slate-400 flex justify-between px-1">
        <span>Distance-Time Graph</span>
        <span class="text-amber-300 font-mono">Straight Line (Linear)</span>
      </div>
      <svg id="uniGraphSvg" viewBox="0 0 200 140" class="w-full h-36">
        <!-- Axes -->
        <line x1="25" y1="120" x2="190" y2="120" stroke="#64748b" stroke-width="1.5"/>
        <line x1="25" y1="120" x2="25" y2="10" stroke="#64748b" stroke-width="1.5"/>
        <text x="190" y="132" fill="#94a3b8" font-size="8" text-anchor="end">Time (s)</text>
        <text x="15" y="15" fill="#94a3b8" font-size="8" text-anchor="start">Dist (m)</text>
        
        <!-- Straight line -->
        <line id="uniGraphLine" x1="25" y1="120" x2="175" y2="25" stroke="#10b981" stroke-width="2.5"/>
        <circle id="uniGraphDot" cx="25" cy="120" r="4" fill="#fbbf24"/>
      </svg>
      <div class="flex justify-between items-center text-xs px-2">
        <button onclick="window.runUniformSim()" id="btnUniSim" class="px-3 py-1 rounded bg-emerald-600 hover:bg-emerald-500 text-white font-semibold">▶ Start Cruise</button>
        <button onclick="window.resetUniformSim()" class="px-2 py-1 rounded bg-slate-700 text-slate-300">↺ Reset</button>
      </div>
    </div>
  </div>
</div>
"""

# 14. non_uniform_motion_sim
simulators["non_uniform_motion_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">8.4 Non-Uniform</span>
      <h4 class="text-sm font-bold text-slate-100">Non-Uniform Motion: Changing Speed & Curved d-t Line</h4>
    </div>
    <span class="text-xs font-mono text-purple-400 bg-purple-950/60 border border-purple-800/80 px-2.5 py-0.5 rounded">Speed = Variable (Accelerating / Braking)</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
    <!-- Non-uniform track -->
    <div class="relative h-60 bg-slate-950 rounded-xl border border-slate-800 flex flex-col justify-around p-3">
      <div class="text-xs text-slate-400 flex justify-between">
        <span>City Street with Traffic & Signals</span>
        <span id="nonUniStatus" class="text-purple-400 font-mono">Idle at Stop</span>
      </div>
      <div class="relative h-12 bg-slate-900 rounded-lg border border-slate-700 overflow-hidden flex items-center">
        <div id="nonUniCar" class="absolute left-2 transition-all duration-75 text-xl">
          🚗
        </div>
      </div>
      <div class="flex justify-between text-[11px] font-mono text-slate-400">
        <span>0 m</span><span>50 m</span><span>120 m</span><span>150 m</span><span>220 m</span>
      </div>
      <div class="bg-slate-900 p-2 rounded-lg border border-slate-800 flex justify-between text-xs">
        <span class="text-slate-400">Unequal distances:</span>
        <span class="text-purple-300 font-mono font-bold">Varying speed in equal time intervals</span>
      </div>
    </div>

    <!-- Curved Graph Plotter -->
    <div class="relative h-60 bg-slate-950 rounded-xl border border-slate-800 p-2 flex flex-col justify-between">
      <div class="text-[11px] text-slate-400 flex justify-between px-1">
        <span>Distance-Time Graph</span>
        <span class="text-purple-300 font-mono">Curved Line (Non-Linear)</span>
      </div>
      <svg id="nonUniGraphSvg" viewBox="0 0 200 140" class="w-full h-36">
        <!-- Axes -->
        <line x1="25" y1="120" x2="190" y2="120" stroke="#64748b" stroke-width="1.5"/>
        <line x1="25" y1="120" x2="25" y2="10" stroke="#64748b" stroke-width="1.5"/>
        <text x="190" y="132" fill="#94a3b8" font-size="8" text-anchor="end">Time (s)</text>
        <text x="15" y="15" fill="#94a3b8" font-size="8" text-anchor="start">Dist (m)</text>
        
        <!-- Curved path -->
        <path id="nonUniCurve" d="M 25,120 Q 80,115 110,70 T 175,25" fill="none" stroke="#a855f7" stroke-width="2.5"/>
        <circle id="nonUniGraphDot" cx="25" cy="120" r="4" fill="#fbbf24"/>
      </svg>
      <div class="flex justify-between items-center text-xs px-2">
        <button onclick="window.runNonUniformSim()" id="btnNonUniSim" class="px-3 py-1 rounded bg-purple-600 hover:bg-purple-500 text-white font-semibold">▶ Drive City Track</button>
        <button onclick="window.resetNonUniformSim()" class="px-2 py-1 rounded bg-slate-700 text-slate-300">↺ Reset</button>
      </div>
    </div>
  </div>
</div>
"""

# 15. distance_time_graph_sim
simulators["distance_time_graph_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">8.4 Slope Analysis</span>
      <h4 class="text-sm font-bold text-slate-100">Distance-Time Graphs: Slope = Speed (Rise / Run)</h4>
    </div>
    <div class="flex gap-1.5">
      <button onclick="window.selectGraphLine('fast')" id="btnGraphFast" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-emerald-500 text-slate-950 shadow-md">Steep (Fast)</button>
      <button onclick="window.selectGraphLine('slow')" id="btnGraphSlow" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">Gentle (Slow)</button>
      <button onclick="window.selectGraphLine('rest')" id="btnGraphRest" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">Horizontal (At Rest)</button>
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
    <!-- Interactive Graph Canvas -->
    <div class="md:col-span-2 relative h-64 bg-slate-950 rounded-xl border border-slate-800 p-3 flex items-center justify-center">
      <svg id="interactiveDtGraph" viewBox="0 0 360 220" class="w-full h-full">
        <!-- Grid -->
        <g stroke="#1e293b" stroke-width="1">
          <line x1="40" y1="40" x2="340" y2="40"/><line x1="40" y1="80" x2="340" y2="80"/>
          <line x1="40" y1="120" x2="340" y2="120"/><line x1="40" y1="160" x2="340" y2="160"/>
          <line x1="100" y1="20" x2="100" y2="190"/><line x1="160" y1="20" x2="160" y2="190"/>
          <line x1="220" y1="20" x2="220" y2="190"/><line x1="280" y1="20" x2="280" y2="190"/>
        </g>
        <!-- Axes -->
        <line x1="40" y1="190" x2="340" y2="190" stroke="#94a3b8" stroke-width="2"/>
        <line x1="40" y1="190" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
        <text x="340" y="205" fill="#cbd5e1" font-size="10" text-anchor="end">Time t (s)</text>
        <text x="30" y="25" fill="#cbd5e1" font-size="10" text-anchor="end">Dist d (m)</text>

        <!-- Dynamic Graph Lines -->
        <line id="dtLineFast" x1="40" y1="190" x2="200" y2="30" stroke="#10b981" stroke-width="3"/>
        <line id="dtLineSlow" x1="40" y1="190" x2="320" y2="90" stroke="#38bdf8" stroke-width="3" opacity="0.3"/>
        <line id="dtLineRest" x1="40" y1="100" x2="330" y2="100" stroke="#f87171" stroke-width="3" stroke-dasharray="4 4" opacity="0.3"/>

        <!-- Slope triangle for active line -->
        <g id="slopeTriangleGroup">
          <polygon points="120,110 200,110 200,30" fill="#10b981" opacity="0.15"/>
          <line x1="120" y1="110" x2="200" y2="110" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3 3"/>
          <line x1="200" y1="110" x2="200" y2="30" stroke="#ef4444" stroke-width="2" stroke-dasharray="3 3"/>
          <text x="160" y="125" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">Δt = 4 s</text>
          <text x="215" y="70" fill="#ef4444" font-size="10" font-weight="bold">Δd = 80 m</text>
        </g>
      </svg>
    </div>

    <!-- Analytics & Calculation Panel -->
    <div class="bg-slate-800/60 p-3.5 rounded-xl border border-slate-700/60 flex flex-col justify-between text-xs">
      <div>
        <h5 id="graphAnalyTitle" class="text-emerald-400 font-bold mb-1">Steep Line (High Speed)</h5>
        <p id="graphAnalyDesc" class="text-slate-300 text-[11px] leading-relaxed mb-3">
          Steeper upward slope means more distance is covered per unit time. Object is moving rapidly.
        </p>

        <div class="bg-slate-950 p-2.5 rounded-lg border border-slate-800 space-y-1 font-mono text-xs">
          <div class="text-slate-400">Slope Calculation:</div>
          <div class="text-amber-300 font-bold">Rise (Δd) = <span id="slopeRise">80 m</span></div>
          <div class="text-cyan-300 font-bold">Run (Δt) = <span id="slopeRun">4 s</span></div>
          <div class="pt-1 border-t border-slate-800 text-emerald-400 font-bold text-sm">
            Speed = <span id="slopeSpeed">20 m/s</span>
          </div>
        </div>
      </div>

      <div class="mt-2 p-2 rounded bg-slate-900 border border-slate-700 text-[11px] text-slate-300">
        <strong>Golden Rule:</strong> A flat horizontal line parallel to the time axis means distance does not change: <strong>Speed = 0 (At Rest)</strong>.
      </div>
    </div>
  </div>
</div>
"""

# 16. indian_time_heritage_sim
simulators["indian_time_heritage_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">Ancient Indian Heritage</span>
      <h4 class="text-sm font-bold text-slate-100">Jantar Mantar Samrat Yantra & Ghatika Yantra</h4>
    </div>
    <div class="flex gap-1.5">
      <button onclick="window.switchHeritageTab('jaipur')" id="btnHeritJaipur" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md">Brihat Samrat Yantra</button>
      <button onclick="window.switchHeritageTab('ghatika')" id="btnHeritGhatika" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">Ghatika Yantra (24m)</button>
    </div>
  </div>

  <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="heritageSvg" viewBox="0 0 600 240" class="w-full h-full">
      <g id="heritageVisualGroup"></g>
    </svg>
    <div id="heritageBadge" class="absolute top-2 right-3 bg-slate-900/85 border border-slate-700 text-xs px-3 py-1 rounded-lg text-amber-300 font-mono">
      Jaipur Samrat Yantra: Precision 2 Seconds
    </div>
  </div>

  <div class="mt-3 flex flex-wrap items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <div class="flex items-center gap-2 flex-1 min-w-[200px]" id="heritageControlContainer">
      <label id="heritageControlLabel" class="text-slate-300 font-medium">Solar Time of Day:</label>
      <input type="range" id="heritageSlider" min="6" max="18" step="0.1" value="12" class="flex-1 accent-amber-500 h-1.5 bg-slate-700 rounded-lg cursor-pointer" oninput="window.updateHeritage(this.value)">
      <span id="heritageControlValue" class="font-mono text-amber-300 w-16 text-right">12:00 PM</span>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="window.actionHeritage()" id="btnHeritageAction" class="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-semibold transition">▶ Advance Shadow</button>
      <button onclick="window.resetHeritage()" class="px-2.5 py-1.5 rounded-lg bg-slate-700 hover:bg-slate-600 text-slate-300 font-semibold transition">↺ Reset</button>
    </div>
  </div>
  <p id="heritageNote" class="mt-2 text-xs text-slate-400 leading-relaxed">
    <strong>Brihat Samrat Yantra (Jaipur, 1734):</strong> Built by Maharaja Sawai Jai Singh II. The massive 27-meter tall gnomon casts a shadow moving at 1 mm per second across calibrated marble quadrants, measuring local time to 2 seconds precision!
  </p>
</div>
"""

# Write out class7_science_time_motion_sims.py
with open(".agents/class7_science_time_motion_sims.py", "w", encoding="utf-8") as f:
    f.write('# -*- coding: utf-8 -*-\n"""Simulators HTML for Class 7 Science Chapter 8"""\n\nSIMULATORS_HTML = {\n')
    for k, v in simulators.items():
        f.write(f'    "{k}": r\'\'\'{v}\'\'\',\n')
    f.write('}\n')

print(f"Generated .agents/class7_science_time_motion_sims.py with {len(simulators)} simulators.")
