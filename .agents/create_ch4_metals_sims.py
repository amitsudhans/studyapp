# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Science Chapter 4 Simulators HTML templates
Outputs .agents/class7_science_metals_sims.py
"""

import json

SIMULATORS_HTML = {
    # Sim 1: Craftsperson Forge & Traditional Metallurgy
    "craftsperson_forge_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🔨 Blacksmith Forge & Shaping Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.1 Observation</span>
    </div>
    <span id="forgeTempBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 font-bold font-mono">25°C (Cold)</span>
  </div>

  <!-- Interactive Forge SVG -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 180" class="w-full h-full">
      <defs>
        <radialGradient id="fireGlow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#ff7700" stop-opacity="0.9"/>
          <stop offset="60%" stop-color="#ff2200" stop-opacity="0.4"/>
          <stop offset="100%" stop-color="#990000" stop-opacity="0"/>
        </radialGradient>
        <linearGradient id="metalHeatGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop id="heatStop1" offset="0%" stop-color="#94a3b8"/>
          <stop id="heatStop2" offset="50%" stop-color="#64748b"/>
          <stop id="heatStop3" offset="100%" stop-color="#475569"/>
        </linearGradient>
      </defs>

      <!-- Forge Hearth Fire Pit -->
      <path d="M 40,150 L 140,150 L 130,95 L 50,95 Z" fill="#1e293b" stroke="#475569" stroke-width="2"/>
      <ellipse cx="90" cy="95" rx="40" ry="12" fill="#0f172a" stroke="#334155"/>
      <circle id="forgeFireEffect" cx="90" cy="85" r="35" fill="url(#fireGlow)" class="opacity-0 transition-opacity duration-500"/>
      <!-- Glowing Embers -->
      <path id="emberFlames" d="M 70,95 Q 90,60 90,75 Q 100,50 110,95 Z" fill="#f59e0b" class="opacity-0 transition-opacity duration-300"/>

      <!-- Bellows -->
      <path d="M 15,140 L 40,130 L 40,145 Z" fill="#b45309" stroke="#78350f" stroke-width="1.5"/>
      <rect x="5" y="132" width="10" height="18" rx="2" fill="#d97706"/>

      <!-- Heavy Steel Anvil -->
      <path d="M 240,160 L 340,160 L 330,125 L 355,100 L 290,100 L 270,100 L 230,100 L 250,125 Z" fill="#334155" stroke="#64748b" stroke-width="2"/>
      <rect x="245" y="100" width="80" height="8" fill="#94a3b8"/>
      <!-- Anvil horn -->
      <path d="M 230,100 Q 210,102 205,104 Q 215,108 230,108 Z" fill="#64748b"/>

      <!-- Workpiece on Anvil -->
      <rect id="forgeWorkpiece" x="255" y="94" width="55" height="12" rx="2" fill="url(#metalHeatGrad)" stroke="#38bdf8" stroke-width="1.5" class="transition-all duration-300"/>

      <!-- Hammer (hits on strike) -->
      <g id="hammerGroup" transform="translate(285, 30) rotate(-25)" class="transition-transform duration-150 origin-bottom-right cursor-pointer">
        <rect x="0" y="0" width="12" height="50" rx="3" fill="#b45309" stroke="#78350f"/>
        <rect x="-14" y="-12" width="40" height="20" rx="3" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
      </g>

      <!-- Spark particles -->
      <g id="sparkContainer" class="opacity-0">
        <circle cx="280" cy="90" r="2" fill="#fde047"/>
        <circle cx="295" cy="85" r="1.5" fill="#fb923c"/>
        <circle cx="270" cy="82" r="2" fill="#ef4444"/>
        <circle cx="305" cy="92" r="1" fill="#fde047"/>
      </g>
    </svg>
  </div>

  <!-- Controls Grid -->
  <div class="grid grid-cols-3 gap-2">
    <button id="btnPumpBellows" class="p-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs flex flex-col items-center justify-center transition shadow-md">
      <span>💨 Pump Bellows</span>
      <span class="text-[10px] font-normal text-amber-200">Heat to 900°C</span>
    </button>
    <button id="btnHammerStrike" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-cyan-300 font-bold text-xs flex flex-col items-center justify-center transition border border-slate-700">
      <span>🔨 Hammer Strike</span>
      <span class="text-[10px] font-normal text-slate-400">Forge into Blade</span>
    </button>
    <button id="btnSwitchMaterialForge" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs flex flex-col items-center justify-center transition border border-slate-700">
      <span>🔄 Switch Material</span>
      <span id="forgeMatName" class="text-[10px] font-normal text-amber-400">Iron (Metal)</span>
    </button>
  </div>

  <div id="forgeFeedback" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    💡 <span class="font-bold text-amber-300">Observation:</span> Metals like iron soften at high temperatures without breaking, enabling craftspersons to forge knives, sickles, and plows!
  </div>
</div>
""",

    # Sim 2: Malleability Mechanical Drop Hammer Lab
    "malleability_lab_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">💥 Malleability Impact Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.1.1 Sheets</span>
    </div>
    <span id="malleabilityResultBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold">Intact</span>
  </div>

  <!-- SVG Drop Hammer Tester -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 420 180" class="w-full h-full">
      <!-- Guide Rails -->
      <line x1="180" y1="15" x2="180" y2="140" stroke="#475569" stroke-width="4" stroke-dasharray="4 2"/>
      <line x1="240" y1="15" x2="240" y2="140" stroke="#475569" stroke-width="4" stroke-dasharray="4 2"/>
      <!-- Base Anvil Plate -->
      <rect x="140" y="145" width="140" height="25" rx="4" fill="#334155" stroke="#64748b" stroke-width="2"/>

      <!-- Drop Hammer Block -->
      <g id="dropHammerHead" transform="translate(0, 0)" class="transition-transform duration-200">
        <rect x="170" y="30" width="80" height="40" rx="4" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
        <rect x="195" y="10" width="30" height="20" fill="#64748b"/>
        <text x="210" y="55" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">50 kg</text>
      </g>

      <!-- Specimen Sample on Base -->
      <g id="specimenDisplay">
        <rect id="specimenShape" x="195" y="130" width="30" height="15" rx="3" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.5" class="transition-all duration-300"/>
        <!-- Crumbled pieces (hidden initially) -->
        <g id="crumblePieces" class="hidden">
          <circle cx="190" cy="142" r="3" fill="#334155"/>
          <circle cx="198" cy="140" r="2.5" fill="#475569"/>
          <circle cx="208" cy="143" r="4" fill="#334155"/>
          <circle cx="218" cy="141" r="3" fill="#1e293b"/>
          <circle cx="228" cy="142" r="2" fill="#475569"/>
        </g>
      </g>
    </svg>
  </div>

  <!-- Material Selection Pills -->
  <div class="flex items-center space-x-1.5 overflow-x-auto pb-1 text-xs">
    <button class="mat-select-btn px-2.5 py-1.5 rounded-lg bg-amber-600 text-white font-bold" data-mat="iron">Iron Nail</button>
    <button class="mat-select-btn px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="aluminium">Aluminium</button>
    <button class="mat-select-btn px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="copper">Copper Block</button>
    <button class="mat-select-btn px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="coal">Coal Lump</button>
    <button class="mat-select-btn px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="sulfur">Sulfur Roll</button>
    <button class="mat-select-btn px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="pencil">Pencil Lead</button>
  </div>

  <div class="flex space-x-2">
    <button id="btnReleaseHammer" class="flex-1 py-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>🔨 Strike with 50 kg Impact</span>
    </button>
    <button id="btnResetMalleability" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition border border-slate-700">
      Reset
    </button>
  </div>

  <div id="malleabilityExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    <span class="text-amber-400 font-bold">Malleability:</span> Metals deform under compressive stress into ultra-thin foil without cracking. Non-metals are brittle and fracture into powder.
  </div>
</div>
""",

    # Sim 3: Ductility Wire Drawing Bench
    "ductility_wire_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🧵 Ductility & Wire Drawing Bench</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.1.2 Wires</span>
    </div>
    <span id="wireLengthBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-400 font-mono font-bold">Length: 10 mm</span>
  </div>

  <!-- Drawing Die SVG -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 180" class="w-full h-full">
      <!-- Tungsten Carbide Die Wall -->
      <rect x="150" y="20" width="25" height="55" fill="#334155" stroke="#64748b" stroke-width="2"/>
      <rect x="150" y="105" width="25" height="55" fill="#334155" stroke="#64748b" stroke-width="2"/>
      <polygon points="150,75 175,82 175,98 150,105" fill="#1e293b"/>
      <text x="162" y="45" fill="#94a3b8" font-size="9" text-anchor="middle">DIE</text>

      <!-- Ingoing Thick Ingot (Left) -->
      <rect id="ductilityIngot" x="50" y="75" width="100" height="30" rx="3" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>

      <!-- Drawn Thin Wire (Right) -->
      <path id="drawnWire" d="M 175,90 L 220,90" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>

      <!-- Tension Pulling Winch Clamps -->
      <g id="winchClamp" transform="translate(220, 70)" class="transition-transform duration-100">
        <rect x="0" y="5" width="35" height="30" rx="4" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
        <line x1="35" y1="20" x2="70" y2="20" stroke="#94a3b8" stroke-width="3"/>
        <!-- Tension arrow -->
        <polygon points="70,16 82,20 70,24" fill="#38bdf8"/>
        <text x="18" y="24" fill="#f8fafc" font-size="9" font-weight="bold" text-anchor="middle">PULL</text>
      </g>

      <!-- Snapped Wire FX -->
      <g id="snapEffect" class="hidden">
        <line x1="200" y1="80" x2="205" y2="100" stroke="#ef4444" stroke-width="3"/>
        <text x="210" y="70" fill="#ef4444" font-size="12" font-weight="bold">SNAP! Brittle</text>
      </g>
    </svg>
  </div>

  <!-- Controls -->
  <div class="flex items-center space-x-2">
    <select id="ductilityMatSelect" class="flex-1 p-2 rounded-xl bg-slate-950 border border-slate-700 text-xs text-slate-200">
      <option value="copper">Copper (High Ductility - Household Wiring)</option>
      <option value="gold">Gold (Supreme Ductility - 1g draws 2 km wire!)</option>
      <option value="aluminium">Aluminium (Overhead Power Lines)</option>
      <option value="iron">Iron (Fencing & Nails)</option>
      <option value="coal">Coal Lump (Non-metal: Zero Ductility)</option>
      <option value="sulfur">Sulfur Rod (Non-metal: Snaps instantly)</option>
    </select>
  </div>

  <div class="flex items-center space-x-3">
    <span class="text-xs text-slate-400 font-mono">Tension Force:</span>
    <input id="ductilityTensionSlider" type="range" min="0" max="100" value="15" class="flex-1 accent-amber-500 cursor-pointer"/>
    <span id="tensionValueDisplay" class="text-xs font-bold text-amber-400 font-mono w-14">15 MPa</span>
  </div>

  <div id="ductilityStatusText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    ⚡ <span class="font-bold text-amber-300">Observation:</span> Metals like copper and gold allow continuous tensile elongation into ultra-thin wires without fracture.
  </div>
</div>
""",

    # Sim 4: Sonority Acoustic Resonance Chamber
    "sonority_chamber_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🔔 Sonority & Acoustic Resonance Chamber</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.1.3 Sound</span>
    </div>
    <span id="sonorityDecibelBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-400 font-mono font-bold">0 dB</span>
  </div>

  <!-- Acoustic Chamber SVG -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 180" class="w-full h-full">
      <!-- Hanging Frame -->
      <line x1="80" y1="20" x2="360" y2="20" stroke="#475569" stroke-width="4"/>
      <!-- Suspension Wire -->
      <line x1="170" y1="20" x2="170" y2="70" stroke="#94a3b8" stroke-width="2"/>

      <!-- Hanging Object: Temple Bell / Plate / Wood / Coal -->
      <g id="sonorousObject" class="origin-top cursor-pointer">
        <!-- Default: Temple Bell -->
        <path id="sonorousShape" d="M 140,70 Q 170,60 200,70 L 210,120 Q 170,135 130,120 Z" fill="#d97706" stroke="#f59e0b" stroke-width="2"/>
        <circle id="bellClapperTip" cx="170" cy="125" r="6" fill="#78350f"/>
      </g>

      <!-- Striker Mallet -->
      <g id="strikerMallet" transform="translate(280, 80) rotate(-20)" class="transition-transform duration-100 origin-bottom-right">
        <rect x="0" y="0" width="8" height="60" rx="2" fill="#78350f"/>
        <rect x="-15" y="-12" width="38" height="24" rx="4" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
      </g>

      <!-- Animated Sound Wave Rings -->
      <g id="soundWaveRings" class="opacity-0">
        <ellipse cx="170" cy="100" rx="35" ry="30" fill="none" stroke="#f59e0b" stroke-width="2" class="animate-ping"/>
        <ellipse cx="170" cy="100" rx="55" ry="45" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
        <ellipse cx="170" cy="100" rx="80" ry="65" fill="none" stroke="#a855f7" stroke-width="1"/>
      </g>

      <!-- Acoustic Waveform Display (Oscilloscope at bottom) -->
      <rect x="250" y="125" width="170" height="45" rx="6" fill="#020617" stroke="#1e293b"/>
      <path id="oscilloscopeTrace" d="M 260,147 L 410,147" fill="none" stroke="#22c55e" stroke-width="2"/>
      <text x="260" y="137" fill="#64748b" font-size="8" font-family="monospace">RESONANCE SPECTRUM</text>
    </svg>
  </div>

  <!-- Selector Grid -->
  <div class="grid grid-cols-4 gap-1.5 text-xs">
    <button class="sono-mat-btn p-2 rounded-xl bg-amber-600 text-white font-bold" data-mat="bronze">Brass Bell</button>
    <button class="sono-mat-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="iron_plate">Iron Plate</button>
    <button class="sono-mat-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="wood_log">Wooden Block</button>
    <button class="sono-mat-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="sulfur_block">Sulfur Chunk</button>
  </div>

  <button id="btnStrikeBell" class="w-full py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition shadow flex items-center justify-center space-x-2">
    <span>🎵 Strike Mallet & Listen to Acoustic Echo</span>
  </button>

  <div id="sonorityFeedback" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🔔 <span class="font-bold text-amber-300">Ringing Echo:</span> Metals produce a deep, reverberating musical ringing sound because crystal grain boundaries sustain acoustic vibrations!
  </div>
</div>
""",

    # Sim 5: Thermal Conduction Bench with Melting Wax Pins
    "thermal_conduction_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🔥 Thermal Conduction & Wax Pin Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.1.4 Heat</span>
    </div>
    <span id="pinFallCounterBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-rose-400 font-bold">Pins Fallen: 0 / 4</span>
  </div>

  <!-- Thermal Conduction SVG -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 180" class="w-full h-full">
      <defs>
        <linearGradient id="heatFlowGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#ef4444"/>
          <stop offset="30%" stop-color="#f59e0b"/>
          <stop offset="70%" stop-color="#38bdf8"/>
          <stop offset="100%" stop-color="#64748b"/>
        </linearGradient>
      </defs>

      <!-- Retort Stand Clamping Rod -->
      <rect x="360" y="20" width="15" height="130" fill="#475569"/>
      <rect x="330" y="145" width="75" height="15" rx="3" fill="#334155"/>
      <rect x="335" y="70" width="35" height="12" fill="#64748b"/>

      <!-- Metal/Insulator Rod -->
      <rect id="conductionRod" x="80" y="72" width="260" height="10" rx="3" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.5"/>

      <!-- Bunsen Burner heating Left End -->
      <g id="bunsenBurner" transform="translate(60, 85)">
        <rect x="15" y="45" width="20" height="30" fill="#64748b"/>
        <rect x="5" y="70" width="40" height="10" rx="2" fill="#334155"/>
        <!-- Flame -->
        <path id="bunsenFlame" d="M 25,45 Q 15,20 25,0 Q 35,20 25,45 Z" fill="#38bdf8" class="opacity-0 transition-opacity duration-300"/>
        <path id="innerFlame" d="M 25,45 Q 20,30 25,15 Q 30,30 25,45 Z" fill="#facc15" class="opacity-0 transition-opacity duration-300"/>
      </g>

      <!-- 4 Wax Attached Thumb Pins -->
      <!-- Pin 1 -->
      <g id="waxPin1" class="transition-transform duration-300">
        <circle cx="130" cy="85" r="4" fill="#fef08a" stroke="#ca8a04"/>
        <line x1="130" y1="89" x2="130" y2="105" stroke="#94a3b8" stroke-width="2"/>
      </g>
      <!-- Pin 2 -->
      <g id="waxPin2" class="transition-transform duration-300">
        <circle cx="180" cy="85" r="4" fill="#fef08a" stroke="#ca8a04"/>
        <line x1="180" y1="89" x2="180" y2="105" stroke="#94a3b8" stroke-width="2"/>
      </g>
      <!-- Pin 3 -->
      <g id="waxPin3" class="transition-transform duration-300">
        <circle cx="230" cy="85" r="4" fill="#fef08a" stroke="#ca8a04"/>
        <line x1="230" y1="89" x2="230" y2="105" stroke="#94a3b8" stroke-width="2"/>
      </g>
      <!-- Pin 4 -->
      <g id="waxPin4" class="transition-transform duration-300">
        <circle cx="280" cy="85" r="4" fill="#fef08a" stroke="#ca8a04"/>
        <line x1="280" y1="89" x2="280" y2="105" stroke="#94a3b8" stroke-width="2"/>
      </g>

      <!-- Temperature Heat gradient bar indicator -->
      <rect id="heatSpreadOverlay" x="80" y="72" width="0" height="10" rx="2" fill="url(#heatFlowGrad)" class="transition-all duration-500 opacity-80"/>
    </svg>
  </div>

  <!-- Rod Selector -->
  <div class="flex items-center space-x-2">
    <button class="rod-select-btn flex-1 py-1.5 rounded-lg bg-amber-600 text-white font-bold text-xs" data-rod="copper">Copper Rod (Fast)</button>
    <button class="rod-select-btn flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs" data-rod="iron">Iron Rod (Medium)</button>
    <button class="rod-select-btn flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs" data-rod="glass">Glass Rod (Poor)</button>
    <button class="rod-select-btn flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs" data-rod="wood">Wood (Zero Heat)</button>
  </div>

  <div class="flex space-x-2">
    <button id="btnIgniteBurner" class="flex-1 py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition shadow">
      🔥 Ignite Flame & Heat Rod
    </button>
    <button id="btnResetThermal" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs border border-slate-700">
      Reset
    </button>
  </div>

  <div id="thermalExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    ♨️ <span class="font-bold text-amber-300">Conduction Mechanism:</span> Kinetic energy travels through free delocalised electrons and lattice vibrations from the hotter end to the colder end.
  </div>
</div>
""",

    # Sim 6: Electrical Conduction Circuit Tester
    "electrical_conduction_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">💡 Circuit Tester & Free Electrons</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.1.5 Circuit</span>
    </div>
    <span id="circuitContinuityBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-rose-400 font-bold">OPEN CIRCUIT</span>
  </div>

  <!-- Circuit Tester SVG -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 180" class="w-full h-full">
      <defs>
        <radialGradient id="electricBulbGlow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#ffffff"/>
          <stop offset="50%" stop-color="#facc15" stop-opacity="0.8"/>
          <stop offset="100%" stop-color="#ca8a04" stop-opacity="0"/>
        </radialGradient>
      </defs>

      <!-- Battery / Cell (Top Center) -->
      <g transform="translate(180, 20)">
        <rect x="0" y="5" width="50" height="25" rx="3" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
        <rect x="50" y="12" width="6" height="11" rx="1" fill="#cbd5e1"/>
        <text x="12" y="22" fill="#ef4444" font-weight="bold" font-size="12">+</text>
        <text x="35" y="22" fill="#38bdf8" font-weight="bold" font-size="12">−</text>
        <text x="25" y="38" fill="#94a3b8" font-size="8" text-anchor="middle">1.5V Cell</text>
      </g>

      <!-- Incandescent Lamp / Bulb (Left) -->
      <g transform="translate(60, 70)">
        <circle id="circuitBulbHalo" cx="20" cy="20" r="30" fill="url(#electricBulbGlow)" class="opacity-0 transition-opacity duration-300"/>
        <circle cx="20" cy="20" r="14" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
        <path id="circuitFilament" d="M 14,23 Q 20,12 26,23" fill="none" stroke="#64748b" stroke-width="2"/>
        <rect x="13" y="32" width="14" height="12" rx="2" fill="#64748b"/>
      </g>

      <!-- Circuit Wiring Loop -->
      <path d="M 180,32 L 80,32 L 80,70" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <path d="M 80,102 L 80,140 L 160,140" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <path d="M 236,32 L 360,32 L 360,140 L 280,140" fill="none" stroke="#ef4444" stroke-width="2.5"/>

      <!-- Crocodile Clips at Gap -->
      <!-- Left Clip -->
      <path d="M 160,135 L 180,138 L 180,142 L 160,145 Z" fill="#94a3b8" stroke="#475569"/>
      <!-- Right Clip -->
      <path d="M 280,135 L 260,138 L 260,142 L 280,145 Z" fill="#94a3b8" stroke="#475569"/>

      <!-- Test Sample Inserted Between Clips -->
      <g id="circuitTestSample">
        <rect id="sampleBar" x="178" y="133" width="84" height="14" rx="3" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.5"/>
        <text id="sampleText" x="220" y="144" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">Iron Nail</text>
      </g>

      <!-- Animated Electron Particles -->
      <g id="electronDots" class="opacity-0">
        <circle cx="120" cy="32" r="2.5" fill="#facc15"/>
        <circle cx="80" cy="120" r="2.5" fill="#facc15"/>
        <circle cx="360" cy="80" r="2.5" fill="#facc15"/>
        <circle cx="320" cy="140" r="2.5" fill="#facc15"/>
      </g>
    </svg>
  </div>

  <!-- Material Selection -->
  <div class="grid grid-cols-4 gap-1.5 text-xs">
    <button class="elec-mat-btn p-2 rounded-xl bg-amber-600 text-white font-bold" data-mat="iron_nail">Iron Nail</button>
    <button class="elec-mat-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="copper_wire">Copper Wire</button>
    <button class="elec-mat-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="graphite">Pencil Graphite</button>
    <button class="elec-mat-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="sulfur">Sulfur Lump</button>
    <button class="elec-mat-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="rubber">Rubber Eraser</button>
    <button class="elec-mat-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="plastic">Plastic Ruler</button>
    <button class="elec-mat-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="aluminium">Al Foil</button>
    <button class="elec-mat-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-mat="glass">Glass Rod</button>
  </div>

  <div id="electricalExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    ⚡ <span class="font-bold text-amber-300">Exception Highlight:</span> Graphite (pencil core) is a non-metal form of pure carbon that conducts electricity because of free delocalised pi-electrons between its hexagonal layers!
  </div>
</div>
""",

    # Sim 7: Rusting of Iron - The Three Bottles Experiment
    "rusting_three_bottles_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🧪 Rusting of Iron: 3-Test-Tube Experiment</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.2 Air + Water</span>
    </div>
    <span id="rustDayDisplay" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-400 font-mono font-bold">Day 0 (Fresh)</span>
  </div>

  <!-- 3 Test Tubes SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 200" class="w-full h-full">
      <!-- Tube Rack Base -->
      <rect x="20" y="170" width="400" height="20" rx="4" fill="#334155" stroke="#475569"/>

      <!-- TUBE A: Air + Tap Water -->
      <g transform="translate(60, 20)">
        <!-- Glass Tube Outline -->
        <rect x="0" y="0" width="50" height="150" rx="8" fill="#0f172a" fill-opacity="0.3" stroke="#64748b" stroke-width="2"/>
        <!-- Tap Water (half filled) -->
        <rect x="2" y="80" width="46" height="66" rx="4" fill="#38bdf8" fill-opacity="0.35"/>
        <!-- Iron Nail partially submerged -->
        <rect id="nailA" x="22" y="60" width="6" height="75" rx="1" fill="#cbd5e1" stroke="#64748b"/>
        <!-- Rust coating on Nail A -->
        <rect id="rustCoatingA" x="20" y="65" width="10" height="65" rx="2" fill="#b45309" class="opacity-0 transition-opacity duration-500"/>
        <!-- Label -->
        <text x="25" y="165" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Tube A</text>
        <text x="25" y="15" fill="#38bdf8" font-size="8" text-anchor="middle">Air + Water</text>
      </g>

      <!-- TUBE B: Boiled Distilled Water + Oil Seal (No Oxygen) -->
      <g transform="translate(195, 20)">
        <rect x="0" y="0" width="50" height="150" rx="8" fill="#0f172a" fill-opacity="0.3" stroke="#64748b" stroke-width="2"/>
        <!-- Rubber Stopper on Top -->
        <polygon points="10,-5 40,-5 36,15 14,15" fill="#475569"/>
        <!-- Boiled Water -->
        <rect x="2" y="75" width="46" height="71" rx="4" fill="#0ea5e9" fill-opacity="0.25"/>
        <!-- Oil Layer Barrier -->
        <rect x="2" y="65" width="46" height="12" fill="#eab308" fill-opacity="0.7"/>
        <text x="25" y="73" fill="#422006" font-size="7" font-weight="bold" text-anchor="middle">OIL SEAL</text>
        <!-- Iron Nail completely submerged -->
        <rect id="nailB" x="22" y="75" width="6" height="65" rx="1" fill="#cbd5e1" stroke="#64748b"/>
        <!-- Label -->
        <text x="25" y="165" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Tube B</text>
        <text x="25" y="25" fill="#eab308" font-size="8" text-anchor="middle">Water ONLY</text>
      </g>

      <!-- TUBE C: Dry Air + Anhydrous CaCl2 (No Moisture) -->
      <g transform="translate(330, 20)">
        <rect x="0" y="0" width="50" height="150" rx="8" fill="#0f172a" fill-opacity="0.3" stroke="#64748b" stroke-width="2"/>
        <!-- Rubber Stopper on Top -->
        <polygon points="10,-5 40,-5 36,15 14,15" fill="#475569"/>
        <!-- Dry Air (Clear) -->
        <!-- Anhydrous Calcium Chloride drying pellets at bottom -->
        <g transform="translate(10, 130)">
          <circle cx="5" cy="5" r="4" fill="#f1f5f9"/>
          <circle cx="15" cy="4" r="5" fill="#e2e8f0"/>
          <circle cx="25" cy="6" r="4" fill="#f8fafc"/>
          <circle cx="10" cy="12" r="4.5" fill="#cbd5e1"/>
          <circle cx="20" cy="11" r="5" fill="#f1f5f9"/>
        </g>
        <text x="25" y="125" fill="#94a3b8" font-size="7" text-anchor="middle">CaCl₂ (Dry)</text>
        <!-- Iron Nail suspended in dry air -->
        <rect id="nailC" x="22" y="35" width="6" height="75" rx="1" fill="#cbd5e1" stroke="#64748b"/>
        <!-- Label -->
        <text x="25" y="165" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Tube C</text>
        <text x="25" y="25" fill="#a855f7" font-size="8" text-anchor="middle">Air ONLY</text>
      </g>
    </svg>
  </div>

  <!-- Time Slider -->
  <div class="flex items-center space-x-3">
    <span class="text-xs text-slate-400 font-mono">Simulate Days:</span>
    <input id="rustDaySlider" type="range" min="0" max="7" value="0" class="flex-1 accent-amber-500 cursor-pointer"/>
    <button id="btnAdvanceWeek" class="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition">
      + 7 Days
    </button>
  </div>

  <div id="rustingConclusion" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🔬 <span class="font-bold text-amber-300">Scientific Proof:</span> Rust only forms in <span class="text-rose-400 font-bold">Tube A</span> where BOTH oxygen (air) and water are simultaneously present!
  </div>
</div>
""",

    # Sim 8: Rust Prevention - Barrier Coatings, Galvanisation & Alloys
    "rust_prevention_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🛡️ Corrosion Protection Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.2 Prevention</span>
    </div>
    <span id="protectionEfficacyBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold">Protected</span>
  </div>

  <!-- Protection Cross-Section SVG -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 180" class="w-full h-full">
      <!-- Atmospheric Spray / Salt Fog (Right) -->
      <g id="corrosiveSpray" class="opacity-70">
        <circle cx="390" cy="50" r="3" fill="#38bdf8"/>
        <circle cx="410" cy="70" r="2.5" fill="#38bdf8"/>
        <circle cx="380" cy="90" r="3.5" fill="#38bdf8"/>
        <circle cx="420" cy="110" r="2" fill="#38bdf8"/>
        <text x="400" y="30" fill="#38bdf8" font-size="9" text-anchor="middle">Moist Air + O₂</text>
      </g>

      <!-- Main Iron Substrate Bar -->
      <rect x="60" y="65" width="280" height="50" rx="4" fill="#64748b" stroke="#475569" stroke-width="2"/>
      <text x="200" y="95" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Iron Substrate (Fe)</text>

      <!-- Protective Outer Layer (Changes with mode) -->
      <!-- Top Layer -->
      <rect id="protectLayerTop" x="55" y="55" width="290" height="10" rx="3" fill="#cbd5e1" class="transition-all duration-300"/>
      <!-- Bottom Layer -->
      <rect id="protectLayerBottom" x="55" y="115" width="290" height="10" rx="3" fill="#cbd5e1" class="transition-all duration-300"/>

      <!-- Scratch in Layer -->
      <path id="scratchCut" d="M 180,52 L 185,67 L 195,52" fill="none" stroke="#ef4444" stroke-width="2.5" class="hidden"/>
      <text id="scratchText" x="190" y="45" fill="#ef4444" font-size="8" font-weight="bold" text-anchor="middle" class="hidden">SCRATCH</text>

      <!-- Rust Blister (shown if unprotected) -->
      <g id="rustBlisters" class="hidden">
        <circle cx="120" cy="65" r="8" fill="#b45309"/>
        <circle cx="260" cy="65" r="10" fill="#9a3412"/>
        <circle cx="200" cy="65" r="7" fill="#b45309"/>
      </g>
    </svg>
  </div>

  <!-- Method Selection Pills -->
  <div class="grid grid-cols-4 gap-1.5 text-xs">
    <button class="shield-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-mode="bare">Bare Iron (None)</button>
    <button class="shield-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-mode="paint">Enamel Paint</button>
    <button class="shield-btn p-2 rounded-xl bg-amber-600 text-white font-bold" data-mode="galvanise">Galvanised (Zinc)</button>
    <button class="shield-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-mode="stainless">Stainless Steel</button>
  </div>

  <div class="flex space-x-2">
    <button id="btnScratchSurface" class="flex-1 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-rose-300 font-bold text-xs border border-slate-700 transition">
      🔪 Scratch Protective Surface
    </button>
    <button id="btnSimulateExposure" class="flex-1 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition">
      🌧️ Expose to Harsh Salt Spray
    </button>
  </div>

  <div id="protectionNote" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🛡️ <span class="font-bold text-amber-300">Sacrificial Protection:</span> In galvanised iron, zinc oxidises sacrificially before iron even when scratched because zinc is more electrochemically reactive!
  </div>
</div>
""",

    # Sim 9: Burning Magnesium Ribbon & Basic Oxide Litmus Test
    "burning_magnesium_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">✨ Burning Magnesium & Basic Oxide</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.3 Metal Oxides</span>
    </div>
    <span id="litmusResultBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 font-bold">Unignited</span>
  </div>

  <!-- Burning Magnesium SVG -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 180" class="w-full h-full">
      <defs>
        <radialGradient id="blindingMgFlash" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#ffffff"/>
          <stop offset="35%" stop-color="#e0f2fe" stop-opacity="0.95"/>
          <stop offset="70%" stop-color="#38bdf8" stop-opacity="0.5"/>
          <stop offset="100%" stop-color="#0284c7" stop-opacity="0"/>
        </radialGradient>
      </defs>

      <!-- Bunsen Burner on Left -->
      <g transform="translate(60, 80)">
        <rect x="20" y="45" width="20" height="35" fill="#475569"/>
        <rect x="10" y="75" width="40" height="12" rx="3" fill="#334155"/>
        <path id="mgBurnerFlame" d="M 30,45 Q 20,20 30,0 Q 40,20 30,45 Z" fill="#38bdf8"/>
      </g>

      <!-- Tongs Holding Magnesium Ribbon -->
      <g id="mgTongs" transform="translate(90, 30)">
        <!-- Tongs scissor arms -->
        <line x1="180" y1="20" x2="30" y2="48" stroke="#94a3b8" stroke-width="4"/>
        <line x1="180" y1="35" x2="30" y2="52" stroke="#94a3b8" stroke-width="4"/>
        <!-- Magnesium Ribbon Strip -->
        <rect id="mgRibbon" x="0" y="46" width="35" height="6" rx="1" fill="#e2e8f0" stroke="#cbd5e1"/>
      </g>

      <!-- Blinding White Light Burst Flare -->
      <circle id="mgFlashBurst" cx="95" cy="80" r="60" fill="url(#blindingMgFlash)" class="hidden animate-pulse"/>

      <!-- Watch Glass for Collecting Ash (Right) -->
      <g transform="translate(260, 110)">
        <path d="M 10,25 Q 40,40 70,25 Q 40,15 10,25 Z" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
        <ellipse id="whiteAshHeap" cx="40" cy="27" rx="14" ry="5" fill="#f8fafc" class="hidden"/>
        <text x="40" y="50" fill="#94a3b8" font-size="8" text-anchor="middle">Watch Glass (MgO)</text>
      </g>

      <!-- Beaker with Water & Litmus Dip -->
      <g id="litmusTestingStation" transform="translate(340, 60)" class="hidden">
        <rect x="10" y="20" width="50" height="60" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
        <rect x="12" y="40" width="46" height="38" rx="2" fill="#38bdf8" fill-opacity="0.3"/>
        <!-- Red Litmus Paper turning Blue at tip -->
        <rect x="30" y="10" width="10" height="50" fill="#f43f5e"/>
        <rect id="litmusBlueTip" x="30" y="40" width="10" height="20" fill="#2563eb" class="hidden transition-all duration-300"/>
        <text x="35" y="88" fill="#f8fafc" font-size="7" text-anchor="middle">Litmus Test</text>
      </g>
    </svg>
  </div>

  <!-- Stepper Buttons -->
  <div class="grid grid-cols-3 gap-2">
    <button id="btnIgniteMg" class="p-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition shadow">
      1. 🔥 Ignite in Flame
    </button>
    <button id="btnDissolveAsh" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-cyan-300 font-bold text-xs transition border border-slate-700" disabled>
      2. 💧 Dissolve Ash
    </button>
    <button id="btnDipLitmusMg" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-rose-300 font-bold text-xs transition border border-slate-700" disabled>
      3. 🧪 Dip Red Litmus
    </button>
  </div>

  <div id="mgReactionFormula" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 font-mono">
    2Mg + O₂ ➔ 2MgO (Dazzling white ash) | MgO + H₂O ➔ Mg(OH)₂ (Red litmus turns BLUE)
  </div>
</div>
""",

    # Sim 10: Copper Weathering in Moist Air & Restoration
    "copper_patina_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🏺 Copper Patina & Lemon Cleanse</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.3 Copper</span>
    </div>
    <span id="copperLusterBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-500 font-bold">Shiny Metallic</span>
  </div>

  <!-- Copper Vessel SVG -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 180" class="w-full h-full">
      <defs>
        <radialGradient id="copperShinyGrad" cx="40%" cy="40%" r="60%">
          <stop offset="0%" stop-color="#fed7aa"/>
          <stop offset="40%" stop-color="#ea580c"/>
          <stop offset="100%" stop-color="#9a3412"/>
        </radialGradient>
        <linearGradient id="greenPatinaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#10b981"/>
          <stop offset="60%" stop-color="#059669"/>
          <stop offset="100%" stop-color="#047857"/>
        </linearGradient>
      </defs>

      <!-- Traditional Copper Pot / Lota -->
      <g transform="translate(140, 20)">
        <!-- Rim -->
        <ellipse cx="80" cy="20" rx="35" ry="8" fill="#c2410c" stroke="#9a3412" stroke-width="1.5"/>
        <ellipse cx="80" cy="20" rx="28" ry="5" fill="#7c2d12"/>
        <!-- Pot Belly -->
        <path id="copperPotBody" d="M 50,23 Q 20,60 20,95 Q 20,135 80,135 Q 140,135 140,95 Q 140,60 110,23 Z" fill="url(#copperShinyGrad)" stroke="#7c2d12" stroke-width="2" class="transition-all duration-700"/>

        <!-- Green Patina Crust Layer -->
        <path id="greenPatinaLayer" d="M 50,23 Q 20,60 20,95 Q 20,135 80,135 Q 140,135 140,95 Q 140,60 110,23 Z" fill="url(#greenPatinaGrad)" class="opacity-0 transition-opacity duration-700"/>

        <!-- Highlighting Sheen -->
        <path d="M 45,55 Q 35,80 35,100" fill="none" stroke="#fff7ed" stroke-width="4" stroke-linecap="round" opacity="0.4"/>
      </g>

      <!-- Lemon Slice Tool (Right) -->
      <g id="lemonTool" transform="translate(330, 70)" class="cursor-pointer transition-transform duration-300">
        <circle cx="25" cy="25" r="24" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>
        <circle cx="25" cy="25" r="20" fill="#fef08a"/>
        <!-- Segments -->
        <line x1="25" y1="5" x2="25" y2="45" stroke="#eab308" stroke-width="1.5"/>
        <line x1="5" y1="25" x2="45" y2="25" stroke="#eab308" stroke-width="1.5"/>
        <text x="25" y="62" fill="#facc15" font-size="8" font-weight="bold" text-anchor="middle">Lemon (Acid)</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2">
    <button id="btnWeatherCopper" class="p-2.5 rounded-xl bg-emerald-700 hover:bg-emerald-600 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>🌧️ Expose to Moist Air (Weeks)</span>
    </button>
    <button id="btnCleanWithLemon" class="p-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>🍋 Rub with Lemon Juice</span>
    </button>
  </div>

  <div id="copperReactionText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 font-mono">
    2Cu + H₂O + CO₂ + O₂ ➔ CuCO₃·Cu(OH)₂ (Green Patina) | Cleaned by citric/tartaric acid!
  </div>
</div>
""",

    # Sim 11: Burning Sulfur & Acidic Non-metal Oxide
    "burning_sulfur_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🧪 Burning Sulfur & Acidic Gas Jar</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.4 Acidic Oxides</span>
    </div>
    <span id="sulfurLitmusBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-400 font-bold">Blue Litmus Ready</span>
  </div>

  <!-- Sulfur Deflagrating Spoon & Gas Jar SVG -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 180" class="w-full h-full">
      <!-- Gas Jar Outline -->
      <g transform="translate(180, 20)">
        <rect x="0" y="10" width="80" height="130" rx="8" fill="#0f172a" fill-opacity="0.3" stroke="#64748b" stroke-width="2"/>
        <!-- Glass lid on top -->
        <rect id="gasJarLid" x="-5" y="6" width="90" height="8" rx="2" fill="#94a3b8" stroke="#cbd5e1"/>

        <!-- Gas Fumes (SO2) inside Jar -->
        <rect id="sulfurGasFumes" x="2" y="14" width="76" height="124" rx="6" fill="#fef08a" class="opacity-0 transition-opacity duration-500"/>

        <!-- Water at bottom for dissolving -->
        <rect id="jarWaterLevel" x="2" y="110" width="76" height="28" rx="4" fill="#38bdf8" fill-opacity="0.3"/>

        <!-- Litmus Paper Strip dipped in water -->
        <g id="sulfurLitmusStrip" class="hidden">
          <rect x="35" y="90" width="10" height="42" fill="#2563eb"/>
          <rect id="litmusTurnedRed" x="35" y="110" width="10" height="22" fill="#e11d48" class="hidden"/>
        </g>
      </g>

      <!-- Deflagrating Spoon with Sulfur Powder -->
      <g id="deflagratingSpoon" transform="translate(100, 40)" class="transition-transform duration-500">
        <!-- Vertical handle bent into cup -->
        <path d="M 0,-10 L 0,80 Q 0,95 20,95 L 35,95" fill="none" stroke="#94a3b8" stroke-width="3"/>
        <path d="M 35,88 Q 45,88 50,95 Q 45,102 35,102 Z" fill="#64748b"/>
        <!-- Yellow Sulfur powder -->
        <ellipse id="sulfurPowder" cx="42" cy="94" rx="6" ry="3" fill="#eab308"/>
        <!-- Blue Flame of burning sulfur -->
        <path id="sulfurBlueFlame" d="M 42,92 Q 38,75 42,65 Q 46,75 42,92 Z" fill="#3b82f6" class="hidden animate-pulse"/>
      </g>

      <!-- Bunsen Burner on Far Left -->
      <g transform="translate(40, 80)">
        <rect x="20" y="45" width="20" height="35" fill="#475569"/>
        <rect x="10" y="75" width="40" height="12" rx="3" fill="#334155"/>
        <path d="M 30,45 Q 20,25 30,5 Q 40,25 30,45 Z" fill="#f59e0b"/>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-3 gap-2">
    <button id="btnIgniteSulfur" class="p-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition shadow">
      1. 🔥 Heat Sulfur
    </button>
    <button id="btnInsertGasJar" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-cyan-300 font-bold text-xs border border-slate-700" disabled>
      2. 🏺 Lower into Jar
    </button>
    <button id="btnTestAcidicLitmus" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-rose-300 font-bold text-xs border border-slate-700" disabled>
      3. 🧪 Dip Blue Litmus
    </button>
  </div>

  <div id="sulfurReactionFormula" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 font-mono">
    S + O₂ ➔ SO₂ (Pungent gas) | SO₂ + H₂O ➔ H₂SO₃ (Sulfurous acid: Blue litmus turns RED!)
  </div>
</div>
""",

    # Sim 12: Hyper-reactive Non-metals - Why Phosphorus is Stored Under Water
    "phosphorus_storage_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">💧 White Phosphorus Storage Simulator</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.4 Hyper-reactive</span>
    </div>
    <span id="phosphorusSafetyBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold">Submerged & Safe</span>
  </div>

  <!-- Phosphorus Jar SVG -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 180" class="w-full h-full">
      <defs>
        <radialGradient id="smokeFumesGrad" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#ffffff" stop-opacity="0.9"/>
          <stop offset="60%" stop-color="#cbd5e1" stop-opacity="0.5"/>
          <stop offset="100%" stop-color="#94a3b8" stop-opacity="0"/>
        </radialGradient>
      </defs>

      <!-- Glass Storage Bottle -->
      <g transform="translate(160, 20)">
        <rect x="0" y="20" width="120" height="130" rx="10" fill="#0f172a" fill-opacity="0.4" stroke="#64748b" stroke-width="2"/>
        <rect x="25" y="0" width="70" height="20" fill="#334155" stroke="#64748b"/>

        <!-- Water level inside bottle -->
        <rect id="storageWater" x="3" y="45" width="114" height="102" rx="6" fill="#0284c7" fill-opacity="0.35"/>

        <!-- Phosphorus Chunk -->
        <g id="phosphorusChunk" transform="translate(45, 105)" class="transition-transform duration-500">
          <polygon points="0,15 15,0 35,5 30,25 10,28" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
          <text x="17" y="16" fill="#713f12" font-size="8" font-weight="bold" text-anchor="middle">P₄</text>
        </g>

        <!-- Spontaneous Fire & Dense White Fumes in Air -->
        <g id="phosphorusFumes" class="hidden">
          <circle cx="60" cy="30" r="35" fill="url(#smokeFumesGrad)"/>
          <circle cx="85" cy="15" r="25" fill="url(#smokeFumesGrad)"/>
          <polygon points="50,40 60,10 70,40" fill="#f97316" class="animate-ping"/>
          <text x="60" y="-10" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">FIRE! P₄O₁₀</text>
        </g>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2">
    <button id="btnKeepSubmerged" class="p-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition shadow">
      💧 Submerge Under Water (Isolated from O₂)
    </button>
    <button id="btnExposeToAir" class="p-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs transition shadow">
      💨 Lift Out into Open Air (30°C)
    </button>
  </div>

  <div id="phosphorusExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    ⚠️ <span class="font-bold text-amber-300">Spontaneous Ignition:</span> White phosphorus has an extremely low ignition temperature (~30°C). Water serves as a physical barrier preventing atmospheric oxygen from touching it!
  </div>
</div>
""",

    # Sim 13: Metals vs Non-Metals Grand Property Matrix
    "property_matrix_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">📊 Grand Property Comparison Matrix</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.4 Classification</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 font-bold">Interactive Table</span>
  </div>

  <!-- Interactive Comparison Table -->
  <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-950 max-h-56">
    <table class="w-full text-left text-xs border-collapse">
      <thead>
        <tr class="bg-slate-900 border-b border-slate-800 text-slate-300">
          <th class="p-2.5 font-bold">Property</th>
          <th class="p-2.5 font-bold text-amber-400">Metals (Typical)</th>
          <th class="p-2.5 font-bold text-cyan-400">Non-Metals (Typical)</th>
          <th class="p-2.5 font-bold text-rose-400">Famous Exceptions</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800/60 font-sans text-slate-300">
        <tr class="hover:bg-slate-900/40">
          <td class="p-2 font-medium">1. Physical State</td>
          <td class="p-2 text-emerald-400">Solid, hard, dense</td>
          <td class="p-2 text-cyan-300">Solids, gases, liquids</td>
          <td class="p-2 text-rose-300">Mercury is liquid metal; Bromine is liquid non-metal</td>
        </tr>
        <tr class="hover:bg-slate-900/40">
          <td class="p-2 font-medium">2. Malleability</td>
          <td class="p-2 text-emerald-400">Malleable (thin sheets)</td>
          <td class="p-2 text-cyan-300">Brittle (shatters to powder)</td>
          <td class="p-2 text-rose-300">Gold/Silver beat into micron foil</td>
        </tr>
        <tr class="hover:bg-slate-900/40">
          <td class="p-2 font-medium">3. Ductility</td>
          <td class="p-2 text-emerald-400">Ductile (stretches to wires)</td>
          <td class="p-2 text-cyan-300">Non-ductile (snaps)</td>
          <td class="p-2 text-rose-300">1 g gold = 2 km wire!</td>
        </tr>
        <tr class="hover:bg-slate-900/40">
          <td class="p-2 font-medium">4. Sonority</td>
          <td class="p-2 text-emerald-400">Sonorous (ringing chime)</td>
          <td class="p-2 text-cyan-300">Non-sonorous (dull thud)</td>
          <td class="p-2 text-rose-300">Temple bells, bronze gongs</td>
        </tr>
        <tr class="hover:bg-slate-900/40">
          <td class="p-2 font-medium">5. Heat Conduction</td>
          <td class="p-2 text-emerald-400">Excellent conductors</td>
          <td class="p-2 text-cyan-300">Insulators / poor</td>
          <td class="p-2 text-rose-300">Diamond (carbon) conducts heat superbly!</td>
        </tr>
        <tr class="hover:bg-slate-900/40">
          <td class="p-2 font-medium">6. Electricity</td>
          <td class="p-2 text-emerald-400">Excellent conductors</td>
          <td class="p-2 text-cyan-300">Insulators (no free e⁻)</td>
          <td class="p-2 text-rose-300">Graphite conducts electricity!</td>
        </tr>
        <tr class="hover:bg-slate-900/40">
          <td class="p-2 font-medium">7. Oxide Nature</td>
          <td class="p-2 text-emerald-400">Basic (Red litmus ➔ Blue)</td>
          <td class="p-2 text-cyan-300">Acidic (Blue litmus ➔ Red)</td>
          <td class="p-2 text-rose-300">Neutral oxides: H₂O, CO, NO</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Exception Highlight Filters -->
  <div class="flex items-center space-x-2 text-xs">
    <button class="exception-filter-btn px-2.5 py-1.5 rounded-lg bg-amber-600 text-white font-bold" data-filter="all">All Properties</button>
    <button class="exception-filter-btn px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700" data-filter="mercury">Liquid Mercury</button>
    <button class="exception-filter-btn px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700" data-filter="sodium">Soft Sodium/Potassium</button>
    <button class="exception-filter-btn px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700" data-filter="graphite">Conductive Graphite</button>
  </div>
</div>
""",

    # Sim 14: Chemical Elements - The Fundamental Building Blocks
    "element_building_blocks_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">⚛️ 118 Elements Building Blocks</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.4 Elements</span>
    </div>
    <span id="elementFamilyBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-400 font-bold">Metals (>80%)</span>
  </div>

  <!-- Interactive Periodic Block Breakdown SVG -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 180" class="w-full h-full">
      <!-- Pie Distribution Chart (Left) -->
      <g transform="translate(100, 90)">
        <!-- Metals Wedge (>80% = ~290 deg) -->
        <path d="M 0,0 L 0,-60 A 60,60 0 1,1 -55,-25 Z" fill="#d97706" stroke="#f59e0b" stroke-width="1.5"/>
        <!-- Non-Metals Wedge (~15% = 55 deg) -->
        <path d="M 0,0 L -55,-25 A 60,60 0 0,1 -20,-56 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
        <!-- Metalloids Wedge (~5% = 15 deg) -->
        <path d="M 0,0 L -20,-56 A 60,60 0 0,1 0,-60 Z" fill="#7c3aed" stroke="#a855f7" stroke-width="1.5"/>
        <text x="15" y="10" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">93 Metals</text>
        <text x="-40" y="-35" fill="#bae6fd" font-size="8" text-anchor="middle">18 Non-M</text>
      </g>

      <!-- Element Tile Card Preview (Right) -->
      <g id="elementCardPreview" transform="translate(260, 25)">
        <rect x="0" y="0" width="140" height="130" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <text id="elemNum" x="15" y="25" fill="#94a3b8" font-size="11" font-family="monospace">26</text>
        <text id="elemSymbol" x="70" y="70" fill="#f59e0b" font-size="34" font-weight="bold" text-anchor="middle">Fe</text>
        <text id="elemName" x="70" y="95" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Iron (Ferrum)</text>
        <text id="elemType" x="70" y="115" fill="#38bdf8" font-size="9" text-anchor="middle">Transition Metal • Malleable</text>
      </g>
    </svg>
  </div>

  <!-- Category Toggles -->
  <div class="grid grid-cols-3 gap-2">
    <button class="elem-group-btn p-2 rounded-xl bg-amber-600 text-white font-bold text-xs" data-group="metals">
      🥇 Metals (93 Elements)
    </button>
    <button class="elem-group-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs" data-group="nonmetals">
      💨 Non-Metals (18 Elements)
    </button>
    <button class="elem-group-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs" data-group="metalloids">
      ⚡ Metalloids (7 Elements)
    </button>
  </div>

  <div id="elementDefinition" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🔬 <span class="font-bold text-amber-300">Core Definition:</span> An element cannot be broken down further by any chemical reaction. Elements consist of identical atoms with uniform proton counts!
  </div>
</div>
""",

    # Sim 15: Essential Non-metals in Daily Life & Biology
    "nonmetals_life_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🌱 Life-Sustaining Non-metals Explorer</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">4.5 Biology</span>
    </div>
    <span id="selectedNonmetalRole" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-bold">Oxygen: Respiration</span>
  </div>

  <!-- Interactive Human Body & Ecosystem SVG -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 180" class="w-full h-full">
      <!-- Human Body Silhouette (Left) -->
      <g transform="translate(60, 20)">
        <!-- Head -->
        <circle cx="40" cy="20" r="14" fill="#334155"/>
        <!-- Torso -->
        <path d="M 26,36 L 54,36 L 48,100 L 32,100 Z" fill="#475569"/>
        <!-- Lungs / Heart Glow -->
        <ellipse id="organLungs" cx="40" cy="52" rx="10" ry="8" fill="#38bdf8" opacity="0.8"/>
        <!-- Limbs -->
        <line x1="26" y1="40" x2="10" y2="85" stroke="#334155" stroke-width="5" stroke-linecap="round"/>
        <line x1="54" y1="40" x2="70" y2="85" stroke="#334155" stroke-width="5" stroke-linecap="round"/>
        <line x1="34" y1="100" x2="28" y2="150" stroke="#475569" stroke-width="6" stroke-linecap="round"/>
        <line x1="46" y1="100" x2="52" y2="150" stroke="#475569" stroke-width="6" stroke-linecap="round"/>
      </g>

      <!-- Life Application Scene (Right) -->
      <g id="lifeSceneDisplay" transform="translate(180, 25)">
        <!-- Card Frame -->
        <rect x="0" y="0" width="220" height="130" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
        <text id="lifeElementName" x="110" y="28" fill="#facc15" font-size="14" font-weight="bold" text-anchor="middle">Oxygen (O₂)</text>
        <text id="lifeElementBodyPct" x="110" y="48" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">65% of Human Body Mass</text>
        <text id="lifeElementDesc1" x="15" y="75" fill="#f8fafc" font-size="10">• Cellular Respiration (ATP)</text>
        <text id="lifeElementDesc2" x="15" y="95" fill="#cbd5e1" font-size="10">• Fuel Combustion & Rocket Oxidiser</text>
        <text id="lifeElementDesc3" x="15" y="115" fill="#94a3b8" font-size="10">• Ozone Layer (O₃) Shield</text>
      </g>
    </svg>
  </div>

  <!-- Non-metal Buttons -->
  <div class="grid grid-cols-6 gap-1 text-xs">
    <button class="life-nm-btn p-1.5 rounded-lg bg-amber-600 text-white font-bold text-center" data-elem="oxygen">Oxygen</button>
    <button class="life-nm-btn p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-center" data-elem="carbon">Carbon</button>
    <button class="life-nm-btn p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-center" data-elem="nitrogen">Nitrogen</button>
    <button class="life-nm-btn p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-center" data-elem="chlorine">Chlorine</button>
    <button class="life-nm-btn p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-center" data-elem="iodine">Iodine</button>
    <button class="life-nm-btn p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-center" data-elem="sulfur">Sulfur</button>
  </div>

  <div id="lifeNonmetalInsight" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🧬 <span class="font-bold text-amber-300">Biological Fact:</span> While metals build our machines and tools, non-metals (C, H, O, N) construct 96% of all living biomass and the DNA of every living cell!
  </div>
</div>
""",

    # Sim 16: Ancient Indian Metallurgy - Acharya Nagarjuna & The Delhi Iron Pillar
    "nagarjuna_heritage_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🏛️ Ancient Indian Metallurgy: Nagarjuna & Delhi Pillar</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">Heritage</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-400 font-bold">1600+ Years Rust-Free</span>
  </div>

  <!-- Heritage SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 200" class="w-full h-full">
      <!-- Tab 1: The Rustless Delhi Iron Pillar -->
      <g id="heritagePillarView">
        <!-- Stone plinth / platform -->
        <rect x="180" y="160" width="80" height="20" rx="3" fill="#64748b" stroke="#475569"/>
        <!-- 7-meter Wrought Iron Pillar -->
        <path d="M 205,40 L 235,40 L 230,160 L 210,160 Z" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
        <!-- Decorative Capital Top -->
        <path d="M 200,40 L 240,40 L 235,30 L 245,25 L 195,25 L 205,30 Z" fill="#475569" stroke="#64748b"/>
        <!-- Passive Protective Film (Misawite delta-FeOOH) Glow -->
        <rect x="207" y="45" width="26" height="110" fill="#38bdf8" opacity="0.15"/>
        <text x="220" y="105" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle" transform="rotate(-90 220 105)">MISAWITE δ-FeOOH</text>
        <!-- Annotation Left -->
        <text x="120" y="70" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">Iron Pillar of Delhi</text>
        <text x="120" y="85" fill="#94a3b8" font-size="8" text-anchor="middle">Gupta Dynasty (~400 CE)</text>
        <text x="120" y="100" fill="#38bdf8" font-size="8" text-anchor="middle">Weight: 6+ Tonnes</text>
        <!-- Annotation Right -->
        <text x="330" y="70" fill="#4ade80" font-size="10" font-weight="bold" text-anchor="middle">Why It Never Rusts?</text>
        <text x="330" y="88" fill="#cbd5e1" font-size="8" text-anchor="middle">High Phosphorus (0.25%)</text>
        <text x="330" y="102" fill="#cbd5e1" font-size="8" text-anchor="middle">+ Slag Inclusions creates</text>
        <text x="330" y="116" fill="#cbd5e1" font-size="8" text-anchor="middle">self-healing passive film!</text>
      </g>

      <!-- Tab 2: Acharya Nagarjuna Zinc Retort Furnace (hidden by default) -->
      <g id="heritageRetortView" class="hidden">
        <!-- Downward Distillation Furnace (Mūṣā & Koṣṭhī) at Zawar -->
        <rect x="150" y="40" width="140" height="110" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <text x="220" y="65" fill="#facc15" font-size="11" font-weight="bold" text-anchor="middle">Zawar Zinc Retort</text>
        <text x="220" y="82" fill="#cbd5e1" font-size="8" text-anchor="middle">Downward Distillation Condenser</text>
        <!-- Retort tubes -->
        <line x1="190" y1="90" x2="190" y2="135" stroke="#94a3b8" stroke-width="4"/>
        <line x1="250" y1="90" x2="250" y2="135" stroke="#94a3b8" stroke-width="4"/>
        <!-- Zinc droplets collecting -->
        <circle cx="190" cy="140" r="3" fill="#38bdf8"/>
        <circle cx="250" cy="140" r="3" fill="#38bdf8"/>
        <text x="220" y="165" fill="#38bdf8" font-size="8" text-anchor="middle">World's 1st Industrial Zinc (Centuries before Europe)</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2">
    <button id="btnViewDelhiPillar" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs transition shadow">
      🏛️ Iron Pillar of Delhi (1600+ Yrs)
    </button>
    <button id="btnViewNagarjunaRetort" class="p-2.5 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs transition border border-slate-700">
      ⚗️ Acharya Nagarjuna & Zawar Retort
    </button>
  </div>

  <div id="heritageDescription" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    📜 <span class="font-bold text-amber-300">Historical Legacy:</span> Acharya Nagarjuna's classic treatise <span class="italic text-amber-200">Rasaratnākara</span> pioneered distillation techniques for zinc, lead, and mercury, making ancient India the world capital of advanced metallurgy!
  </div>
</div>
"""
}

with open(".agents/class7_science_metals_sims.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 7 Science Chapter 4 Simulators HTML Dictionary"""\n\n')
    f.write("SIMULATORS_HTML = " + repr(SIMULATORS_HTML) + "\n")

print("Generated .agents/class7_science_metals_sims.py successfully.")

