# -*- coding: utf-8 -*-
"""Generated Simulator Templates for Class 7 Science Chapter 7"""

SIMULATORS_HTML = {
    "conduction_wax_pins_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🔥 Conduction Wave: Wax-Attached Pins</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.1 Conduction</span>
    </div>
    <span id="conductionStatusBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-mono font-bold">Burner: OFF</span>
  </div>

  <!-- Conduction Apparatus SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Laboratory Stand (Left) -->
      <rect x="25" y="150" width="70" height="12" rx="3" fill="#334155"/>
      <rect x="55" y="40" width="8" height="110" fill="#475569"/>
      <rect x="50" y="50" width="22" height="10" rx="2" fill="#64748b"/>
      
      <!-- Horizontal Metal Strip -->
      <g id="metalStripGroup">
        <!-- Cold Base Rod -->
        <rect id="metalStrip" x="65" y="52" width="310" height="6" rx="2" fill="#64748b"/>
        <!-- Dynamic Thermal Gradient Overlay -->
        <rect id="thermalGradientOverlay" x="65" y="52" width="0" height="6" rx="2" fill="url(#heatGradient)"/>
      </g>

      <!-- SVG Gradient Definition -->
      <defs>
        <linearGradient id="heatGradient" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#ef4444"/>
          <stop offset="40%" stop-color="#f97316"/>
          <stop offset="80%" stop-color="#eab308"/>
          <stop offset="100%" stop-color="#38bdf8"/>
        </linearGradient>
      </defs>

      <!-- Spirit Lamp / Bunsen Burner (Below Left End) -->
      <g id="burnerAssembly" transform="translate(60, 85)">
        <path d="M 10,45 L 30,45 L 35,65 L 5,65 Z" fill="#475569"/>
        <rect x="17" y="32" width="6" height="13" fill="#94a3b8"/>
        <!-- Flame (Hidden initially) -->
        <g id="burnerFlame" class="hidden">
          <ellipse cx="20" cy="20" rx="6" ry="14" fill="#f59e0b" class="animate-pulse"/>
          <ellipse cx="20" cy="23" rx="3.5" ry="8" fill="#fef08a"/>
          <ellipse cx="20" cy="26" rx="2" ry="4" fill="#38bdf8"/>
        </g>
      </g>

      <!-- Wax Droplets & Hanging Brass Pins -->
      <!-- Pin 1 at x = 130 -->
      <g id="pinGroup1" transform="translate(130, 58)">
        <ellipse cx="0" cy="2" rx="4" ry="2.5" fill="#fef08a" id="wax1"/>
        <line x1="0" y1="2" x2="0" y2="35" stroke="#fbbf24" stroke-width="2" id="pinStem1" class="transition-all duration-300"/>
        <circle cx="0" cy="35" r="2.5" fill="#d97706" id="pinHead1"/>
      </g>

      <!-- Pin 2 at x = 195 -->
      <g id="pinGroup2" transform="translate(195, 58)">
        <ellipse cx="0" cy="2" rx="4" ry="2.5" fill="#fef08a" id="wax2"/>
        <line x1="0" y1="2" x2="0" y2="35" stroke="#fbbf24" stroke-width="2" id="pinStem2" class="transition-all duration-300"/>
        <circle cx="0" cy="35" r="2.5" fill="#d97706" id="pinHead2"/>
      </g>

      <!-- Pin 3 at x = 260 -->
      <g id="pinGroup3" transform="translate(260, 58)">
        <ellipse cx="0" cy="2" rx="4" ry="2.5" fill="#fef08a" id="wax3"/>
        <line x1="0" y1="2" x2="0" y2="35" stroke="#fbbf24" stroke-width="2" id="pinStem3" class="transition-all duration-300"/>
        <circle cx="0" cy="35" r="2.5" fill="#d97706" id="pinHead3"/>
      </g>

      <!-- Pin 4 at x = 325 -->
      <g id="pinGroup4" transform="translate(325, 58)">
        <ellipse cx="0" cy="2" rx="4" ry="2.5" fill="#fef08a" id="wax4"/>
        <line x1="0" y1="2" x2="0" y2="35" stroke="#fbbf24" stroke-width="2" id="pinStem4" class="transition-all duration-300"/>
        <circle cx="0" cy="35" r="2.5" fill="#d97706" id="pinHead4"/>
      </g>

      <!-- Lab Table Surface -->
      <line x1="15" y1="162" x2="425" y2="162" stroke="#334155" stroke-width="2"/>
      
      <!-- Thermal Wavefront Annotation -->
      <text id="conductionAnnotation" x="220" y="25" fill="#94a3b8" font-size="9" font-family="monospace" text-anchor="middle">Click "Ignite Burner" to observe progressive heat conduction</text>
    </svg>
  </div>

  <!-- Interactive Controls -->
  <div class="grid grid-cols-2 gap-2">
    <button id="btnIgniteBurner" class="p-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition shadow flex items-center justify-center gap-1.5 cursor-pointer">
      <span>🔥</span> Ignite Burner
    </button>
    <button id="btnResetConduction" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition flex items-center justify-center gap-1.5 cursor-pointer">
      <span>🔄</span> Cool Rod & Reset Pins
    </button>
  </div>

  <!-- Dynamic Conduction Explanation Card -->
  <div id="conductionExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    🧪 <span class="font-bold text-amber-300">Activity 7.1 Observation:</span> Solid metal particles vibrate in fixed positions. Heat conducts progressively from the flame toward the cold end. Pins drop off one by one as the conduction wave melts each wax seal!
  </div>
</div>
''',
    "conductors_insulators_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🥄 Thermal Conductivity Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.1 Materials</span>
    </div>
    <span id="materialClassificationBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold">Good Conductor</span>
  </div>

  <!-- Boiling Water Bath & Rod Testing SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Hotplate Base -->
      <rect x="80" y="150" width="160" height="20" rx="4" fill="#334155"/>
      <circle cx="100" cy="160" r="4" fill="#ef4444" class="animate-pulse"/>
      <text x="110" y="163" fill="#cbd5e1" font-size="8">95 °C Hotplate</text>

      <!-- Glass Beaker with Boiling Water -->
      <rect x="90" y="70" width="140" height="80" rx="4" fill="#0284c7" fill-opacity="0.25" stroke="#38bdf8" stroke-width="2"/>
      <!-- Water Surface Wave -->
      <path d="M 90,85 Q 125,82 160,85 T 230,85 L 230,150 L 90,150 Z" fill="#0284c7" fill-opacity="0.4"/>
      
      <!-- Tested Rod Inserted into Hot Water -->
      <g id="testedRodAssembly" transform="translate(155, 30)">
        <!-- Rod Shaft (Length 110 px) -->
        <rect id="testedRodShaft" x="-6" y="0" width="12" height="110" rx="3" fill="#f59e0b" stroke="#78350f" stroke-width="1"/>
        <!-- Upper Handle Heat Sensor Dot -->
        <circle id="handleHeatSensor" cx="0" cy="8" r="5" fill="#38bdf8" class="transition-all duration-300"/>
        <!-- Handle Temp Readout Text -->
        <text id="handleTempText" x="15" y="11" fill="#38bdf8" font-size="9" font-weight="bold">24 °C (Cool)</text>
      </g>

      <!-- Material Properties Callout Card (Right) -->
      <g transform="translate(260, 20)">
        <rect x="0" y="0" width="165" height="145" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
        <text id="cardMatName" x="82" y="22" fill="#facc15" font-size="11" font-weight="bold" text-anchor="middle">Copper Rod</text>
        <line x1="15" y1="30" x2="150" y2="30" stroke="#475569" stroke-width="1"/>
        
        <text x="15" y="48" fill="#94a3b8" font-size="8">Thermal Conductivity:</text>
        <text id="cardMatK" x="15" y="62" fill="#38bdf8" font-size="9" font-family="monospace" font-weight="bold">k ≈ 385 W/(m·K)</text>

        <text x="15" y="80" fill="#94a3b8" font-size="8">Heat Travel to Handle:</text>
        <text id="cardMatSpeed" x="15" y="94" fill="#fbbf24" font-size="9" font-weight="bold">Extremely Fast (~3s)</text>

        <text x="15" y="112" fill="#94a3b8" font-size="8">Classification:</text>
        <text id="cardMatVerdict" x="15" y="126" fill="#4ade80" font-size="9" font-weight="bold">Superior Conductor</text>
      </g>
    </svg>
  </div>

  <!-- Material Selection Pills -->
  <div class="grid grid-cols-3 sm:grid-cols-6 gap-1.5">
    <button class="mat-btn p-1.5 rounded-lg bg-amber-600 text-white font-bold text-xs" data-mat="copper">Copper</button>
    <button class="mat-btn p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs" data-mat="aluminium">Aluminium</button>
    <button class="mat-btn p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs" data-mat="iron">Iron/Steel</button>
    <button class="mat-btn p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs" data-mat="glass">Glass</button>
    <button class="mat-btn p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs" data-mat="wood">Wood</button>
    <button class="mat-btn p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs" data-mat="plastic">Plastic/Bakelite</button>
  </div>

  <div id="materialExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    ⚡ <span class="font-bold text-cyan-300">Conduction Mechanism:</span> Metals have abundant free electrons that zip through the lattice, carrying heat kinetic energy rapidly. Insulators lack free electrons, confining heat to sluggish atomic vibrations!
  </div>
</div>
''',
    "trapped_air_insulation_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🧥 Trapped Air Insulation Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.1 Insulators</span>
    </div>
    <span id="blanketInsulBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 font-bold">2 Thin Blankets Selected</span>
  </div>

  <!-- Thermal Barrier Cross-Section SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Left: Warm Body Core (37 °C) -->
      <g transform="translate(30, 20)">
        <rect x="0" y="0" width="55" height="150" rx="8" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.5"/>
        <text x="27" y="70" fill="#fecaca" font-size="9" font-weight="bold" text-anchor="middle">Warm</text>
        <text x="27" y="85" fill="#fecaca" font-size="9" font-weight="bold" text-anchor="middle">Body</text>
        <text x="27" y="105" fill="#f87171" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">37 °C</text>
      </g>

      <!-- Center: Insulating Barrier Assembly -->
      <g id="blanketAssembly" transform="translate(100, 20)">
        <!-- Layer 1: Inner Blanket (40px) -->
        <rect id="layerInner" x="0" y="0" width="40" height="150" fill="#d97706" rx="2"/>
        <text id="layerInnerTxt" x="20" y="80" fill="#fef3c7" font-size="8" text-anchor="middle">Blanket 1</text>

        <!-- Layer 2: Trapped Air Pocket (25px) -->
        <g id="trappedAirGap">
          <rect x="40" y="0" width="25" height="150" fill="#0284c7" fill-opacity="0.3"/>
          <text x="52" y="80" fill="#38bdf8" font-size="7" font-weight="bold" text-anchor="middle">Trapped Air</text>
          <text x="52" y="92" fill="#7dd3fc" font-size="6" text-anchor="middle">(k ≈ 0.026)</text>
        </g>

        <!-- Layer 3: Outer Blanket (40px) -->
        <rect id="layerOuter" x="65" y="0" width="40" height="150" fill="#d97706" rx="2"/>
        <text id="layerOuterTxt" x="85" y="80" fill="#fef3c7" font-size="8" text-anchor="middle">Blanket 2</text>
      </g>

      <!-- Right: Freezing Winter Environment (5 °C) -->
      <g transform="translate(225, 20)">
        <rect x="0" y="0" width="55" height="150" rx="8" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="27" y="70" fill="#bae6fd" font-size="9" font-weight="bold" text-anchor="middle">Winter</text>
        <text x="27" y="85" fill="#bae6fd" font-size="9" font-weight="bold" text-anchor="middle">Cold</text>
        <text x="27" y="105" fill="#38bdf8" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">5 °C</text>
      </g>

      <!-- Thermal Heat Loss Meter (Far Right) -->
      <g transform="translate(300, 25)">
        <rect x="0" y="0" width="125" height="140" rx="8" fill="#1e293b" stroke="#334155"/>
        <text x="62" y="20" fill="#e2e8f0" font-size="9" font-weight="bold" text-anchor="middle">Heat Loss Rate</text>
        
        <!-- Meter Bar Container -->
        <rect x="20" y="35" width="85" height="16" rx="4" fill="#0f172a"/>
        <rect id="heatLossBar" x="20" y="35" width="30" height="16" rx="4" fill="#22c55e" class="transition-all duration-300"/>

        <text id="heatLossVal" x="62" y="68" fill="#4ade80" font-size="11" font-family="monospace" font-weight="bold" text-anchor="middle">14 W/m²</text>
        <text id="thermalVerdict" x="62" y="95" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Excellent Warmth!</text>
        <text id="airLayerNote" x="62" y="118" fill="#94a3b8" font-size="7" text-anchor="middle">Trapped air layer blocks heat</text>
      </g>
    </svg>
  </div>

  <!-- Comparison Toggle Buttons -->
  <div class="grid grid-cols-3 gap-2">
    <button id="btnTwoThinBlankets" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs shadow">2 Thin Blankets (Air Gap)</button>
    <button id="btnOneThickBlanket" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs">1 Thick Blanket (No Gap)</button>
    <button id="btnHollowBrick" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs">Hollow Wall Brick</button>
  </div>

  <div id="trappedAirExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    🛏️ <span class="font-bold text-amber-300">Why 2 Thin > 1 Thick:</span> The narrow space between two separate blankets traps a cushion of stationary air. Because still air is an exceptionally poor conductor of heat, this extra trapped air layer keeps you significantly warmer!
  </div>
</div>
''',
    "convection_currents_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🟣 Liquid Convection: KMnO₄ Plumes</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.2 Convection</span>
    </div>
    <span id="convectionIntensityBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-purple-300 font-bold">Burner: Active</span>
  </div>

  <!-- Flask with Convection Loops SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Round-Bottom Glass Flask Assembly -->
      <g transform="translate(140, 10)">
        <!-- Flask Neck -->
        <rect x="55" y="10" width="30" height="30" fill="none" stroke="#64748b" stroke-width="2"/>
        <!-- Spherical Bulb (Radius 60) -->
        <circle cx="70" cy="90" r="55" fill="#0284c7" fill-opacity="0.15" stroke="#38bdf8" stroke-width="2"/>

        <!-- Potassium Permanganate Crystal at Bottom -->
        <circle cx="70" cy="140" r="5" fill="#9333ea" stroke="#581c87" stroke-width="1"/>
        <text x="70" y="152" fill="#c084fc" font-size="7" font-weight="bold" text-anchor="middle">KMnO₄</text>

        <!-- Upward Convective Plume (Purple) -->
        <path id="risingPlume" d="M 70,135 Q 65,90 70,45" fill="none" stroke="#a855f7" stroke-width="4" stroke-linecap="round" class="animate-pulse"/>
        
        <!-- Outward Circulation Loops -->
        <g id="convectionLoops" stroke="#c084fc" stroke-width="2.5" fill="none" stroke-linecap="round">
          <!-- Left Loop: Up center, left top, down side -->
          <path d="M 68,48 Q 30,50 25,85 T 60,135" stroke-dasharray="4,3"/>
          <polygon points="25,88 22,80 28,80" fill="#c084fc"/>

          <!-- Right Loop: Up center, right top, down side -->
          <path d="M 72,48 Q 110,50 115,85 T 80,135" stroke-dasharray="4,3"/>
          <polygon points="115,88 112,80 118,80" fill="#c084fc"/>
        </g>
      </g>

      <!-- Bunsen Burner Below Flask Center -->
      <g transform="translate(190, 155)">
        <rect x="10" y="15" width="20" height="20" rx="2" fill="#475569"/>
        <g id="liquidBurnerFlame">
          <ellipse cx="20" cy="5" rx="5" ry="10" fill="#f59e0b" class="animate-pulse"/>
          <ellipse cx="20" cy="7" rx="2.5" ry="5" fill="#fef08a"/>
        </g>
      </g>

      <!-- Legend & Physics Card (Right) -->
      <g transform="translate(305, 25)">
        <rect x="0" y="0" width="125" height="140" rx="8" fill="#1e293b" stroke="#334155"/>
        <text x="62" y="20" fill="#e2e8f0" font-size="9" font-weight="bold" text-anchor="middle">Convection Cycle</text>
        <line x1="10" y1="28" x2="115" y2="28" stroke="#475569"/>

        <circle cx="20" cy="45" r="4" fill="#a855f7"/>
        <text x="32" y="48" fill="#e2e8f0" font-size="8">1. Heated water</text>
        <text x="32" y="58" fill="#94a3b8" font-size="7">expands & rises</text>

        <circle cx="20" cy="78" r="4" fill="#38bdf8"/>
        <text x="32" y="81" fill="#e2e8f0" font-size="8">2. Cold water sinks</text>
        <text x="32" y="91" fill="#94a3b8" font-size="7">to replace it</text>

        <text x="62" y="120" fill="#facc15" font-size="8" font-weight="bold" text-anchor="middle">Continuous Loop</text>
      </g>
    </svg>
  </div>

  <!-- Heat Control Buttons -->
  <div class="grid grid-cols-2 gap-2">
    <button id="btnToggleConvectionHeat" class="p-2.5 rounded-xl bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs transition shadow cursor-pointer">
      ⚡ Toggle Flame (Fast / Slow)
    </button>
    <button id="btnAddKMnO4Crystal" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition cursor-pointer">
      🟣 Drop New KMnO₄ Crystal
    </button>
  </div>

  <div id="liquidConvectionExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    🌊 <span class="font-bold text-purple-300">Fluid Buoyancy:</span> Heated water at the bottom expands and becomes lighter (less dense), rising to the surface. Colder, denser water from the top flows down along the edges, creating a continuous convective circulation cycle!
  </div>
</div>
''',
    "gas_convection_spiral_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🌀 Air Convection: Rising Paper Spiral</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.2 Air Updraft</span>
    </div>
    <span id="spiralStatusBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold">Spiral: Rotating</span>
  </div>

  <!-- Candle & Paper Spiral SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Support Stand & Thread (Left) -->
      <line x1="120" y1="160" x2="120" y2="20" stroke="#475569" stroke-width="4"/>
      <line x1="120" y1="20" x2="220" y2="20" stroke="#475569" stroke-width="3"/>
      <!-- Hanging Thread -->
      <line x1="220" y1="20" x2="220" y2="45" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2,2"/>

      <!-- Suspended Paper Spiral (Center) -->
      <g id="paperSpiral" transform="translate(220, 70)" class="transition-transform duration-300">
        <!-- Helix Coil Shapes -->
        <path d="M 0,-25 Q 25,-15 0,0 Q -25,15 0,30 Q 20,40 0,50" fill="none" stroke="#fef08a" stroke-width="4" stroke-linecap="round"/>
        <circle cx="0" cy="-25" r="3" fill="#eab308"/>
      </g>

      <!-- Upward Hot Air Vector Arrows -->
      <g id="updraftArrows" stroke="#f97316" stroke-width="1.5" fill="#f97316">
        <path d="M 210,135 L 210,110 M 210,110 L 207,115 M 210,110 L 213,115" class="animate-bounce"/>
        <path d="M 230,135 L 230,110 M 230,110 L 227,115 M 230,110 L 233,115" class="animate-bounce"/>
      </g>

      <!-- Burning Candle Below Spiral -->
      <g transform="translate(210, 140)">
        <rect x="2" y="15" width="16" height="35" rx="2" fill="#f8fafc"/>
        <line x1="10" y1="15" x2="10" y2="8" stroke="#1e293b" stroke-width="2"/>
        <g id="candleFlameGroup">
          <ellipse cx="10" cy="2" rx="4.5" ry="9" fill="#f59e0b" class="animate-pulse"/>
          <ellipse cx="10" cy="3" rx="2" ry="5" fill="#fef08a"/>
        </g>
      </g>

      <!-- Explanation Dashboard (Right) -->
      <g transform="translate(295, 25)">
        <rect x="0" y="0" width="135" height="140" rx="8" fill="#1e293b" stroke="#334155"/>
        <text x="67" y="20" fill="#facc15" font-size="9" font-weight="bold" text-anchor="middle">Air Convection</text>
        <line x1="10" y1="28" x2="125" y2="28" stroke="#475569"/>

        <text x="12" y="45" fill="#cbd5e1" font-size="8">• Air expands over flame</text>
        <text x="12" y="60" fill="#cbd5e1" font-size="8">• Density decreases</text>
        <text x="12" y="75" fill="#cbd5e1" font-size="8">• Hot air rushes up</text>
        <text x="12" y="90" fill="#cbd5e1" font-size="8">• Kinetic lift spins spiral</text>
        <text x="12" y="105" fill="#38bdf8" font-size="8">• Cold air enters base</text>

        <text id="spiralRpmTxt" x="67" y="128" fill="#4ade80" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">Speed: 45 RPM</text>
      </g>
    </svg>
  </div>

  <!-- Interactive Controls -->
  <div class="grid grid-cols-2 gap-2">
    <button id="btnLightCandle" class="p-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition shadow cursor-pointer">
      🕯️ Light Candle Flame
    </button>
    <button id="btnBlowOutCandle" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition cursor-pointer">
      💨 Blow Out Flame
    </button>
  </div>

  <div id="gasConvectionExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    🌪️ <span class="font-bold text-amber-300">Thermal Updraft:</span> Air directly over the candle flame heats up rapidly, expands, and surges upward in a buoyant convection current. This rising air pushes against the curved blades of the spiral, causing it to spin!
  </div>
</div>
''',
    "sea_breeze_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🌊 Coastal Meteorology: Daytime Sea Breeze</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.2.1 Sea Breeze</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-bold">Time: 2:00 PM (Day)</span>
  </div>

  <!-- Day Sea Breeze Coastal Landscape SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Sky Background (Sunny Day) -->
      <rect x="0" y="0" width="440" height="130" fill="#0369a1" fill-opacity="0.3"/>
      
      <!-- Blazing Daytime Sun (Top Right) -->
      <g transform="translate(370, 35)">
        <circle cx="0" cy="0" r="16" fill="#facc15" class="animate-pulse"/>
        <!-- Sun Rays -->
        <line x1="0" y1="-25" x2="0" y2="-18" stroke="#fde047" stroke-width="2"/>
        <line x1="0" y1="25" x2="0" y2="18" stroke="#fde047" stroke-width="2"/>
        <line x1="-25" y1="0" x2="-18" y2="0" stroke="#fde047" stroke-width="2"/>
        <line x1="25" y1="0" x2="18" y2="0" stroke="#fde047" stroke-width="2"/>
      </g>

      <!-- Coastal Land (Left Half) -->
      <path d="M 0,130 Q 110,125 210,135 L 210,190 L 0,190 Z" fill="#b45309"/>
      <!-- Sand Beach Surface -->
      <path d="M 0,130 Q 110,125 210,135" fill="none" stroke="#d97706" stroke-width="4"/>

      <!-- Coastal Cottage on Land -->
      <g transform="translate(70, 95)">
        <!-- Walls -->
        <rect x="0" y="10" width="35" height="25" fill="#f8fafc"/>
        <!-- Roof -->
        <polygon points="-5,10 17,-5 40,10" fill="#dc2626"/>
        <!-- Large Window Facing Seaward (Right) -->
        <rect x="20" y="15" width="10" height="12" fill="#38bdf8"/>
        <text x="25" y="42" fill="#fef08a" font-size="6" text-anchor="middle">Window</text>
      </g>

      <!-- Ocean / Sea Water (Right Half) -->
      <rect x="210" y="135" width="230" height="55" fill="#0284c7"/>
      <!-- Ocean Waves -->
      <path d="M 210,135 Q 240,132 270,135 T 330,135 T 390,135 T 440,135" fill="none" stroke="#38bdf8" stroke-width="2"/>

      <!-- Thermal Annotations -->
      <!-- Land: Hot (36 °C), Low Pressure -->
      <g transform="translate(50, 45)">
        <rect x="0" y="0" width="80" height="38" rx="6" fill="#1e293b" fill-opacity="0.9" stroke="#ef4444"/>
        <text x="40" y="14" fill="#f87171" font-size="8" font-weight="bold" text-anchor="middle">Land: 36 °C</text>
        <text x="40" y="25" fill="#fb923c" font-size="7" text-anchor="middle">Heats up FAST!</text>
        <text x="40" y="34" fill="#facc15" font-size="7" font-weight="bold" text-anchor="middle">[LOW PRESSURE]</text>
      </g>

      <!-- Sea: Cooler (24 °C), High Pressure -->
      <g transform="translate(260, 80)">
        <rect x="0" y="0" width="85" height="38" rx="6" fill="#1e293b" fill-opacity="0.9" stroke="#38bdf8"/>
        <text x="42" y="14" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Sea: 24 °C</text>
        <text x="42" y="25" fill="#7dd3fc" font-size="7" text-anchor="middle">Heats up SLOWLY</text>
        <text x="42" y="34" fill="#4ade80" font-size="7" font-weight="bold" text-anchor="middle">[HIGH PRESSURE]</text>
      </g>

      <!-- Convection Wind Circulation Loop -->
      <!-- Rising Warm Air over Land -->
      <g stroke="#f87171" stroke-width="2.5" fill="#f87171">
        <line x1="85" y1="90" x2="85" y2="60"/>
        <polygon points="85,55 81,63 89,63"/>
      </g>

      <!-- Upper Air Return (Land to Sea) -->
      <g stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3" fill="#94a3b8">
        <line x1="100" y1="35" x2="280" y2="35"/>
        <polygon points="285,35 278,32 278,38"/>
      </g>

      <!-- Sea Breeze (Cool Low Air: Sea to Land) -->
      <g stroke="#38bdf8" stroke-width="3" fill="#38bdf8">
        <line x1="280" y1="125" x2="130" y2="125"/>
        <polygon points="125,125 133,121 133,129"/>
      </g>
      <text x="200" y="120" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">Cool Sea Breeze →</text>
    </svg>
  </div>

  <!-- Interactive Information Card -->
  <div id="seaBreezeExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    ☀️ <span class="font-bold text-cyan-300">Daytime Dynamics:</span> In sunlight, land warms roughly 5 times faster than water. Hot air above land expands and rises, creating a low-pressure area. Cool, dense air over the sea rushes inland as the refreshing <span class="text-amber-400 font-bold">Sea Breeze</span>!
  </div>
</div>
''',
    "land_breeze_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🌙 Coastal Meteorology: Night Land Breeze</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.2.1 Land Breeze</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-indigo-300 font-bold">Time: 2:00 AM (Night)</span>
  </div>

  <!-- Night Land Breeze Coastal Landscape SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Dark Night Sky -->
      <rect x="0" y="0" width="440" height="130" fill="#0f172a"/>
      
      <!-- Stars in Sky -->
      <circle cx="40" cy="25" r="1.5" fill="#f8fafc"/>
      <circle cx="120" cy="18" r="1.5" fill="#f8fafc"/>
      <circle cx="180" cy="30" r="1" fill="#f8fafc"/>
      <circle cx="310" cy="20" r="1" fill="#f8fafc"/>

      <!-- Crescent Moon (Top Right) -->
      <path d="M 370,20 A 14,14 0 0,0 385,38 A 12,12 0 1,1 370,20 Z" fill="#fef08a"/>

      <!-- Chilled Land (Left Half) -->
      <path d="M 0,130 Q 110,125 210,135 L 210,190 L 0,190 Z" fill="#3f2e1e"/>
      <path d="M 0,130 Q 110,125 210,135" fill="none" stroke="#78350f" stroke-width="4"/>

      <!-- Warmer Sea Water (Right Half) -->
      <rect x="210" y="135" width="230" height="55" fill="#0369a1"/>
      <path d="M 210,135 Q 240,132 270,135 T 330,135 T 390,135 T 440,135" fill="none" stroke="#0ea5e9" stroke-width="2"/>

      <!-- Traditional Fishing Sailboat Sailing Out (Assisted by Land Breeze) -->
      <g transform="translate(320, 118)">
        <!-- Wooden Hull -->
        <path d="M 0,15 L 35,15 L 30,22 L 5,22 Z" fill="#78350f"/>
        <!-- Mast -->
        <line x1="18" y1="15" x2="18" y2="-2" stroke="#451a03" stroke-width="2"/>
        <!-- Sail Billowing Rightward (Offshore) -->
        <path d="M 18,0 Q 30,7 18,14 Z" fill="#f8fafc" stroke="#cbd5e1"/>
      </g>

      <!-- Thermal Annotations -->
      <!-- Land: Cold (18 °C), High Pressure -->
      <g transform="translate(45, 55)">
        <rect x="0" y="0" width="85" height="38" rx="6" fill="#1e293b" fill-opacity="0.9" stroke="#38bdf8"/>
        <text x="42" y="14" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Land: 18 °C</text>
        <text x="42" y="25" fill="#7dd3fc" font-size="7" text-anchor="middle">Cools down FAST!</text>
        <text x="42" y="34" fill="#4ade80" font-size="7" font-weight="bold" text-anchor="middle">[HIGH PRESSURE]</text>
      </g>

      <!-- Sea: Warmer (23 °C), Low Pressure -->
      <g transform="translate(230, 45)">
        <rect x="0" y="0" width="85" height="38" rx="6" fill="#1e293b" fill-opacity="0.9" stroke="#f97316"/>
        <text x="42" y="14" fill="#fb923c" font-size="8" font-weight="bold" text-anchor="middle">Sea: 23 °C</text>
        <text x="42" y="25" fill="#fed7aa" font-size="7" text-anchor="middle">Retains warmth</text>
        <text x="42" y="34" fill="#f87171" font-size="7" font-weight="bold" text-anchor="middle">[LOW PRESSURE]</text>
      </g>

      <!-- Land Breeze (Cool Offshore Wind: Land to Sea) -->
      <g stroke="#38bdf8" stroke-width="3" fill="#38bdf8">
        <line x1="110" y1="125" x2="260" y2="125"/>
        <polygon points="265,125 257,121 257,129"/>
      </g>
      <text x="185" y="120" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">← Cool Land Breeze</text>

      <!-- Rising Warm Air over Sea -->
      <g stroke="#fb923c" stroke-width="2.5" fill="#fb923c">
        <line x1="272" y1="85" x2="272" y2="55"/>
        <polygon points="272,50 268,58 276,58"/>
      </g>
    </svg>
  </div>

  <div id="landBreezeExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    🌌 <span class="font-bold text-indigo-300">Nighttime Reversal:</span> At night, land loses heat rapidly while sea water stays warm. The warmer air over the sea rises, and cooler, denser air from the land blows offshore as the <span class="text-amber-400 font-bold">Land Breeze</span>, naturally carrying traditional fishing boats out to sea!
  </div>
</div>
''',
    "thermal_radiation_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">☀️ Cosmic Radiation: Heat Across Vacuum</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.3 Radiation</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 font-mono font-bold">Speed: c = 300,000 km/s</span>
  </div>

  <!-- Cosmic Vacuum Radiation SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Sun on Left Edge -->
      <g transform="translate(40, 95)">
        <circle cx="0" cy="0" r="35" fill="#f59e0b" class="animate-pulse"/>
        <circle cx="0" cy="0" r="28" fill="#facc15"/>
        <text x="0" y="4" fill="#78350f" font-size="10" font-weight="bold" text-anchor="middle">Sun</text>
        <text x="0" y="15" fill="#78350f" font-size="7" text-anchor="middle">5,500 °C</text>
      </g>

      <!-- Pure Airless Space Vacuum (Center) -->
      <g transform="translate(140, 30)">
        <rect x="0" y="0" width="160" height="130" rx="6" fill="#020617" stroke="#1e293b"/>
        <text x="80" y="25" fill="#64748b" font-size="8" font-family="monospace" text-anchor="middle">AIRLESS COSMIC VACUUM</text>
        <text x="80" y="40" fill="#475569" font-size="7" text-anchor="middle">Distance: 150 Million km</text>
        <text x="80" y="55" fill="#ef4444" font-size="7" font-weight="bold" text-anchor="middle">No Conduction • No Convection</text>
        
        <!-- Animated Infrared Radiation Waves -->
        <g stroke="#f97316" stroke-width="2" fill="none" opacity="0.8">
          <path d="M 20,70 Q 35,55 50,70 T 80,70 T 110,70 T 140,70" class="animate-pulse"/>
          <path d="M 20,90 Q 35,75 50,90 T 80,90 T 110,90 T 140,90" class="animate-pulse"/>
        </g>
        <text x="80" y="115" fill="#f59e0b" font-size="8" font-weight="bold" text-anchor="middle">Infrared Waves (Light Speed)</text>
      </g>

      <!-- Planet Earth on Right Edge -->
      <g transform="translate(370, 95)">
        <!-- Atmosphere Glow -->
        <circle cx="0" cy="0" r="25" fill="#38bdf8" fill-opacity="0.3"/>
        <!-- Earth Sphere -->
        <circle cx="0" cy="0" r="20" fill="#0284c7"/>
        <!-- Green Continents -->
        <path d="M -8,-10 Q -2,-5 -5,5 Q -8,12 -12,8 Z" fill="#22c55e"/>
        <path d="M 5,-8 Q 12,-2 10,8 Q 2,12 4,2 Z" fill="#22c55e"/>
        <text x="0" y="4" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Earth</text>
      </g>
    </svg>
  </div>

  <!-- Interactive Mode Buttons -->
  <div class="grid grid-cols-2 gap-2">
    <button id="btnPulseSolarRadiation" class="p-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition shadow cursor-pointer">
      ☀️ Pulse Solar Infrared Radiation
    </button>
    <button id="btnCampfireComparison" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition cursor-pointer">
      🔥 Campfire Radiant Heat Test
    </button>
  </div>

  <div id="radiationExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    🛰️ <span class="font-bold text-amber-300">No Medium Required:</span> Conduction and convection strictly demand particles of matter. Radiation is electromagnetic energy traveling through pure cosmic vacuum at 300,000 km/s, bringing life-giving warmth to Earth!
  </div>
</div>
''',
    "black_white_radiation_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">⬛ Radiant Heat: Black vs White Surfaces</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.3 Absorption</span>
    </div>
    <span id="radExpModeBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-400 font-bold">Mode: Solar Heating</span>
  </div>

  <!-- Two Cans Under Sun/Heat Lamp SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Heat Lamp / Sun Overhead -->
      <g id="heatSourceLamp" transform="translate(220, 25)">
        <path d="M -30,0 L 30,0 L 20,15 L -20,15 Z" fill="#64748b"/>
        <circle cx="0" cy="15" r="10" fill="#facc15" class="animate-pulse"/>
        <!-- Radiant Heat Rays Spreading to Both Cans -->
        <line x1="-15" y1="20" x2="-80" y2="65" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
        <line x1="15" y1="20" x2="80" y2="65" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
      </g>

      <!-- Can A: Matte Jet Black (Left) -->
      <g transform="translate(100, 75)">
        <!-- Can Body -->
        <rect x="0" y="0" width="70" height="75" rx="4" fill="#18181b" stroke="#3f3f46" stroke-width="2"/>
        <text x="35" y="42" fill="#e4e4e7" font-size="9" font-weight="bold" text-anchor="middle">Black Can</text>
        <text x="35" y="55" fill="#a1a1aa" font-size="7" text-anchor="middle">Matte Absorber</text>
        
        <!-- Thermometer Tube -->
        <rect x="32" y="-30" width="6" height="60" rx="3" fill="#ffffff" stroke="#94a3b8"/>
        <rect id="thermBlackLiquid" x="33" y="10" width="4" height="20" rx="2" fill="#ef4444"/>
        <!-- Temp Badge -->
        <text id="tempBlackTxt" x="35" y="-35" fill="#ef4444" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">48 °C</text>
      </g>

      <!-- Can B: Glossy White (Right) -->
      <g transform="translate(270, 75)">
        <!-- Can Body -->
        <rect x="0" y="0" width="70" height="75" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
        <text x="35" y="42" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">White Can</text>
        <text x="35" y="55" fill="#475569" font-size="7" text-anchor="middle">Shiny Reflector</text>

        <!-- Thermometer Tube -->
        <rect x="32" y="-30" width="6" height="60" rx="3" fill="#ffffff" stroke="#94a3b8"/>
        <rect id="thermWhiteLiquid" x="33" y="20" width="4" height="10" rx="2" fill="#ef4444"/>
        <!-- Temp Badge -->
        <text id="tempWhiteTxt" x="35" y="-35" fill="#38bdf8" font-size="10" font-family="monospace" font-weight="bold" text-anchor="middle">28 °C</text>
      </g>

      <!-- Table Base -->
      <line x1="40" y1="152" x2="400" y2="152" stroke="#334155" stroke-width="2"/>
      <text id="radiationDeltaTxt" x="220" y="172" fill="#facc15" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">Temperature Difference: ΔT = +20 °C in Black Can!</text>
    </svg>
  </div>

  <!-- Mode Selector Buttons -->
  <div class="grid grid-cols-2 gap-2">
    <button id="btnModeAbsorption" class="p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs shadow cursor-pointer">
      ☀️ Absorption Test (Under Sunlight)
    </button>
    <button id="btnModeEmission" class="p-2.5 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs cursor-pointer">
      ❄️ Cooling / Emission Test (In Dark)
    </button>
  </div>

  <div id="blackWhiteExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    🎯 <span class="font-bold text-amber-300">Kirchhoff's Law:</span> Dark, rough surfaces absorb almost all incident radiant heat. White surfaces reflect radiation. Crucially, <span class="text-emerald-400 font-bold">good absorbers are also good emitters</span>—the black can cools twice as fast in the dark!
  </div>
</div>
''',
    "thermos_flask_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🧊 The Thermos Flask: Tri-Mode Barrier</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.3 Engineering</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-bold">Dewar Flask Design</span>
  </div>

  <!-- Thermos Flask Cutaway SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Thermos Flask Cutaway (Center-Left) -->
      <g transform="translate(100, 10)">
        <!-- Outer Protective Plastic Casing -->
        <rect x="0" y="30" width="100" height="145" rx="12" fill="#1e293b" stroke="#475569" stroke-width="2"/>
        
        <!-- Insulating Plastic Stopper / Cork (Top) -->
        <polygon points="30,10 70,10 65,35 35,35" fill="#d97706" stroke="#92400e" stroke-width="1.5"/>
        <text x="50" y="25" fill="#fef3c7" font-size="7" font-weight="bold" text-anchor="middle">Stopper</text>

        <!-- Double-Walled Glass Vessel -->
        <rect x="15" y="42" width="70" height="120" rx="8" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>

        <!-- The Evacuated Vacuum Gap (Dark Blue) -->
        <rect x="20" y="46" width="60" height="112" rx="6" fill="#020617"/>
        <text x="50" y="70" fill="#38bdf8" font-size="7" font-weight="bold" text-anchor="middle">VACUUM GAP</text>

        <!-- Inner Glass Cylinder with Silver Mirror Coating -->
        <rect x="25" y="50" width="50" height="104" rx="4" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
        
        <!-- Hot Liquid Core (Coffee/Tea 85 °C) -->
        <rect x="28" y="55" width="44" height="95" rx="3" fill="#b45309"/>
        <text x="50" y="105" fill="#fef3c7" font-size="8" font-weight="bold" text-anchor="middle">Hot Liquid</text>
        <text x="50" y="117" fill="#fde68a" font-size="7" text-anchor="middle">85 °C</text>

        <!-- Rubber Cushion Support Pad at Base -->
        <rect x="35" y="165" width="30" height="8" rx="2" fill="#dc2626"/>
      </g>

      <!-- Annotations & Callouts (Right) -->
      <g transform="translate(230, 20)">
        <rect x="0" y="0" width="195" height="145" rx="8" fill="#1e293b" stroke="#334155"/>
        <text x="97" y="18" fill="#facc15" font-size="9" font-weight="bold" text-anchor="middle">How It Blocks All Heat Modes</text>
        <line x1="15" y1="25" x2="180" y2="25" stroke="#475569"/>

        <!-- Conduction Block -->
        <text x="12" y="42" fill="#38bdf8" font-size="8" font-weight="bold">1. Conduction Blocked:</text>
        <text x="12" y="53" fill="#cbd5e1" font-size="7">Vacuum gap lacks particles to collide</text>

        <!-- Convection Block -->
        <text x="12" y="70" fill="#a855f7" font-size="8" font-weight="bold">2. Convection Blocked:</text>
        <text x="12" y="81" fill="#cbd5e1" font-size="7">Vacuum has no fluid circulation</text>

        <!-- Radiation Block -->
        <text x="12" y="98" fill="#f97316" font-size="8" font-weight="bold">3. Radiation Blocked:</text>
        <text x="12" y="109" fill="#cbd5e1" font-size="7">Silver mirror reflects infrared waves</text>

        <!-- Stopper Function -->
        <text x="12" y="126" fill="#4ade80" font-size="8" font-weight="bold">4. Insulating Stopper:</text>
        <text x="12" y="137" fill="#cbd5e1" font-size="7">Prevents steam evaporative escape</text>
      </g>
    </svg>
  </div>

  <div id="thermosExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    🛡️ <span class="font-bold text-cyan-300">Triple Thermal Barrier:</span> The vacuum eliminates both conduction and convection, the silvered mirror surface reflects away radiant heat, and the tight stopper seals against vapor loss. Result: drinks stay piping hot or ice cold for hours!
  </div>
</div>
''',
    "water_cycle_evap_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">💧 Water Cycle: Evaporation & Transpiration</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.4 Water Cycle</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-bold font-mono">Total Water: Constant</span>
  </div>

  <!-- Water Cycle Phase 1 SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Sky Background -->
      <rect x="0" y="0" width="440" height="120" fill="#0284c7" fill-opacity="0.2"/>
      
      <!-- Radiant Sun (Center Sky) -->
      <g transform="translate(220, 30)">
        <circle cx="0" cy="0" r="18" fill="#facc15" class="animate-pulse"/>
        <!-- Radiant Heat Rays Shooting Down -->
        <g stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2,2">
          <line x1="-30" y1="15" x2="-80" y2="70"/>
          <line x1="30" y1="15" x2="80" y2="70"/>
          <line x1="0" y1="22" x2="0" y2="80"/>
        </g>
        <text x="0" y="4" fill="#78350f" font-size="7" font-weight="bold" text-anchor="middle">Solar Heat</text>
      </g>

      <!-- Ocean / Lake Reservoir (Left) -->
      <path d="M 0,115 Q 80,110 160,120 L 160,190 L 0,190 Z" fill="#0284c7"/>
      <text x="70" y="155" fill="#e0f2fe" font-size="9" font-weight="bold">Ocean (86% Evap)</text>

      <!-- Forest Canopy Land (Right) -->
      <path d="M 160,120 Q 280,110 440,115 L 440,190 L 160,190 Z" fill="#15803d"/>
      
      <!-- Forest Trees -->
      <g transform="translate(260, 85)">
        <polygon points="20,0 5,30 35,30" fill="#166534"/>
        <rect x="17" y="30" width="6" height="15" fill="#78350f"/>
      </g>
      <g transform="translate(320, 80)">
        <polygon points="25,0 8,35 42,35" fill="#14532d"/>
        <rect x="22" y="35" width="6" height="15" fill="#78350f"/>
      </g>
      <text x="320" y="155" fill="#dcfce7" font-size="9" font-weight="bold">Vegetation Canopy</text>

      <!-- Rising Vapour Particles (Evaporation from Ocean) -->
      <g stroke="#38bdf8" stroke-width="2" fill="#38bdf8">
        <path d="M 50,110 Q 55,95 50,80 T 55,50" fill="none" stroke-dasharray="3,3" class="animate-pulse"/>
        <path d="M 100,110 Q 95,95 100,80 T 95,50" fill="none" stroke-dasharray="3,3" class="animate-pulse"/>
        <text x="75" y="75" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Evaporation ↑</text>
      </g>

      <!-- Rising Vapour from Plants (Transpiration) -->
      <g stroke="#4ade80" stroke-width="2" fill="#4ade80">
        <path d="M 300,90 Q 295,75 300,60 T 295,40" fill="none" stroke-dasharray="3,3" class="animate-pulse"/>
        <path d="M 360,90 Q 365,75 360,60 T 365,40" fill="none" stroke-dasharray="3,3" class="animate-pulse"/>
        <text x="330" y="55" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">Transpiration ↑</text>
      </g>
    </svg>
  </div>

  <div id="waterCycleExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    🌍 <span class="font-bold text-cyan-300">The Upward Engine:</span> Solar radiation heats oceans, driving evaporation of pure water vapour while leaving salts behind. Concurrently, plant root water evaporates into the sky through leaf stomata (transpiration). Total water on Earth remains constant!
  </div>
</div>
''',
    "cloud_condensation_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">☁️ Atmospheric Cooling: Cloud Genesis</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.4 Condensation</span>
    </div>
    <span id="altitudeTempBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-mono font-bold">Alt: 2,000m (8 °C)</span>
  </div>

  <!-- Atmospheric Lapse Rate & Cloud Formation SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Altitude Stratification Gradient (Cold High, Warm Low) -->
      <defs>
        <linearGradient id="skyAltitudeGrad" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#0c4a6e"/>
          <stop offset="60%" stop-color="#0369a1"/>
          <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.2"/>
        </linearGradient>
      </defs>
      <rect x="0" y="0" width="440" height="190" fill="url(#skyAltitudeGrad)"/>

      <!-- Altitude Measurement Ladder (Left) -->
      <line x1="50" y1="20" x2="50" y2="170" stroke="#64748b" stroke-width="2"/>
      <line x1="45" y1="30" x2="55" y2="30" stroke="#94a3b8"/>
      <text x="40" y="33" fill="#cbd5e1" font-size="7" text-anchor="end">3,000 m (-1 °C)</text>
      
      <line x1="45" y1="80" x2="55" y2="80" stroke="#94a3b8"/>
      <text x="40" y="83" fill="#cbd5e1" font-size="7" text-anchor="end">2,000 m (8 °C)</text>

      <line x1="45" y1="130" x2="55" y2="130" stroke="#94a3b8"/>
      <text x="40" y="133" fill="#cbd5e1" font-size="7" text-anchor="end">1,000 m (17 °C)</text>

      <text x="40" y="165" fill="#facc15" font-size="7" text-anchor="end">Sea Level (26 °C)</text>

      <!-- Cloud Condensation Nuclei (CCN) Dust Particles -->
      <g id="ccnParticles" fill="#cbd5e1" opacity="0.6">
        <circle cx="160" cy="65" r="2"/>
        <circle cx="210" cy="55" r="1.5"/>
        <circle cx="260" cy="70" r="2"/>
        <circle cx="310" cy="50" r="1.5"/>
      </g>

      <!-- Puffy Cumulus Cloud Group (Top Center) -->
      <g id="formedCloud" transform="translate(160, 30)">
        <path d="M 20,45 Q 10,25 35,20 Q 50,0 80,10 Q 110,-5 130,20 Q 155,20 150,45 Q 155,65 130,65 L 20,65 Q 5,65 20,45 Z" fill="#ffffff" fill-opacity="0.95" stroke="#e2e8f0" stroke-width="2"/>
        <text x="85" y="42" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">Cumulus Cloud</text>
        <text x="85" y="54" fill="#334155" font-size="7" text-anchor="middle">Billions of Water Droplets</text>
      </g>

      <!-- Dew Point Boundary Line -->
      <line x1="60" y1="95" x2="380" y2="95" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="4,4"/>
      <text x="375" y="90" fill="#facc15" font-size="8" font-family="monospace" text-anchor="end">Dew Point Saturation Boundary (T_dew ≈ 12 °C)</text>

      <!-- Rising Air Updraft Parcel -->
      <g transform="translate(230, 150)">
        <path d="M 0,0 L 0,-40" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
        <polygon points="0,-45 -4,-38 4,-38" fill="#38bdf8"/>
        <text x="12" y="-20" fill="#bae6fd" font-size="7">Rising Warm Air</text>
      </g>
    </svg>
  </div>

  <!-- Altitude Slider -->
  <div class="flex items-center space-x-3 px-2">
    <span class="text-xs text-slate-400 font-mono">Altitude:</span>
    <input id="cloudAltSlider" type="range" min="500" max="3000" step="250" value="2000" class="flex-1 accent-cyan-500 cursor-pointer">
    <span id="cloudAltDisplay" class="text-xs font-bold text-cyan-400 font-mono w-16">2,000 m</span>
  </div>

  <div id="cloudExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    🌫️ <span class="font-bold text-cyan-300">Adiabatic Cooling:</span> As warm, moist air ascends, pressure drops and the air parcel expands, dropping ~6.5 °C per km. Reaching its dew point, moisture condenses onto microscopic dust/salt particles (CCN), giving birth to clouds!
  </div>
</div>
''',
    "precipitation_types_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🌧️ Precipitation: Rain, Snow & Hail</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.4 Precipitation</span>
    </div>
    <span id="precipTypeBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-bold">Type: Liquid Rain</span>
  </div>

  <!-- Precipitation Atmospheric Column SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Thundercloud at Top -->
      <g transform="translate(120, 15)">
        <path d="M 20,40 Q 10,15 40,15 Q 60,-5 90,5 Q 120,-10 145,15 Q 170,15 165,40 Q 175,60 145,60 L 20,60 Z" fill="#334155" stroke="#475569" stroke-width="2"/>
        <text x="95" y="38" fill="#e2e8f0" font-size="9" font-weight="bold" text-anchor="middle">Precipitation Cloud</text>
      </g>

      <!-- Falling Particles Group (Toggled by Mode) -->
      <g id="rainParticlesGroup" stroke="#38bdf8" stroke-width="2" stroke-linecap="round">
        <line x1="160" y1="80" x2="155" y2="95"/>
        <line x1="190" y1="90" x2="185" y2="105"/>
        <line x1="220" y1="75" x2="215" y2="90"/>
        <line x1="250" y1="85" x2="245" y2="100"/>
        <line x1="170" y1="110" x2="165" y2="125"/>
        <line x1="200" y1="120" x2="195" y2="135"/>
        <line x1="230" y1="105" x2="225" y2="120"/>
        <line x1="260" y1="115" x2="255" y2="130"/>
      </g>

      <!-- Landscape & Surface Runoff River (Bottom) -->
      <path d="M 0,155 Q 140,150 280,155 L 440,150 L 440,190 L 0,190 Z" fill="#15803d"/>
      <!-- River Channel (Runoff returning to ocean) -->
      <path d="M 170,155 Q 220,165 270,190 L 330,190 Q 260,165 220,155 Z" fill="#0284c7"/>
      <text x="240" y="180" fill="#e0f2fe" font-size="8" font-weight="bold">Surface Runoff →</text>

      <!-- Physics Annotation Box (Right) -->
      <g transform="translate(325, 20)">
        <rect x="0" y="0" width="105" height="120" rx="6" fill="#1e293b" stroke="#334155"/>
        <text id="precipCardTitle" x="52" y="18" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Liquid Rain</text>
        <line x1="10" y1="25" x2="95" y2="25" stroke="#475569"/>
        <text id="precipCardTemp" x="10" y="42" fill="#cbd5e1" font-size="7">Column: > 0 °C</text>
        <text id="precipCardSize" x="10" y="58" fill="#cbd5e1" font-size="7">Diameter: 0.5 - 4 mm</text>
        <text id="precipCardNote" x="10" y="74" fill="#a1a1aa" font-size="6">Coalescence causes</text>
        <text id="precipCardNote2" x="10" y="84" fill="#a1a1aa" font-size="6">droplets to fall</text>
        <text id="precipCardSpeed" x="10" y="105" fill="#4ade80" font-size="7" font-weight="bold">Fall: ~8 m/s</text>
      </g>
    </svg>
  </div>

  <!-- Precipitation Mode Selector -->
  <div class="grid grid-cols-3 gap-2">
    <button class="precip-btn p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs" data-mode="rain">🌧️ Liquid Rain</button>
    <button class="precip-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs" data-mode="snow">❄️ Snowflakes</button>
    <button class="precip-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs" data-mode="hail">🧊 Solid Hail</button>
  </div>

  <div id="precipitationExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    🌧️ <span class="font-bold text-cyan-300">Precipitation Dynamics:</span> When cloud droplets grow larger than 0.1 mm, gravity overcomes updrafts. If atmospheric columns are above 0 °C, it falls as liquid rain. At subzero temperatures, it falls as crystalline snow or layered hail!
  </div>
</div>
''',
    "soil_infiltration_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🧪 Soil Infiltration & Seepage Rate Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.4.1 Infiltration</span>
    </div>
    <span id="soilSelectedBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 font-bold">Soil: Gravel (Fastest)</span>
  </div>

  <!-- 4 Soil Percolation Columns SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- 4 Transparent Filter Tubes (Gravel, Sand, Loam, Clay) -->
      <!-- Column 1: Gravel (x = 45) -->
      <g transform="translate(45, 25)">
        <rect x="0" y="0" width="60" height="90" rx="3" fill="#334155" fill-opacity="0.3" stroke="#64748b" stroke-width="1.5"/>
        <!-- Gravel Grains -->
        <circle cx="15" cy="30" r="5" fill="#78716c"/>
        <circle cx="35" cy="25" r="6" fill="#a8a29e"/>
        <circle cx="48" cy="45" r="5" fill="#78716c"/>
        <circle cx="20" cy="60" r="6" fill="#a8a29e"/>
        <circle cx="40" cy="70" r="5" fill="#78716c"/>
        <!-- Drip Nozzle -->
        <polygon points="25,90 35,90 30,100" fill="#64748b"/>
        <!-- Beaker Below -->
        <rect x="5" y="110" width="50" height="35" rx="2" fill="none" stroke="#64748b"/>
        <rect id="beakerLevelGravel" x="6" y="125" width="48" height="20" rx="1" fill="#38bdf8" fill-opacity="0.7"/>
        <text x="30" y="155" fill="#cbd5e1" font-size="8" font-weight="bold" text-anchor="middle">Gravel</text>
        <text x="30" y="165" fill="#38bdf8" font-size="7" text-anchor="middle">Fastest Seep</text>
      </g>

      <!-- Column 2: Coarse Sand (x = 140) -->
      <g transform="translate(140, 25)">
        <rect x="0" y="0" width="60" height="90" rx="3" fill="#334155" fill-opacity="0.3" stroke="#64748b" stroke-width="1.5"/>
        <rect x="2" y="10" width="56" height="78" fill="#d97706" fill-opacity="0.5"/>
        <polygon points="25,90 35,90 30,100" fill="#64748b"/>
        <rect x="5" y="110" width="50" height="35" rx="2" fill="none" stroke="#64748b"/>
        <rect id="beakerLevelSand" x="6" y="132" width="48" height="13" rx="1" fill="#38bdf8" fill-opacity="0.7"/>
        <text x="30" y="155" fill="#cbd5e1" font-size="8" font-weight="bold" text-anchor="middle">Sand</text>
        <text x="30" y="165" fill="#fbbf24" font-size="7" text-anchor="middle">Rapid Flow</text>
      </g>

      <!-- Column 3: Loam Soil (x = 235) -->
      <g transform="translate(235, 25)">
        <rect x="0" y="0" width="60" height="90" rx="3" fill="#334155" fill-opacity="0.3" stroke="#64748b" stroke-width="1.5"/>
        <rect x="2" y="10" width="56" height="78" fill="#854d0e" fill-opacity="0.7"/>
        <polygon points="25,90 35,90 30,100" fill="#64748b"/>
        <rect x="5" y="110" width="50" height="35" rx="2" fill="none" stroke="#64748b"/>
        <rect id="beakerLevelLoam" x="6" y="138" width="48" height="7" rx="1" fill="#38bdf8" fill-opacity="0.7"/>
        <text x="30" y="155" fill="#cbd5e1" font-size="8" font-weight="bold" text-anchor="middle">Loam</text>
        <text x="30" y="165" fill="#a3e635" font-size="7" text-anchor="middle">Balanced Seep</text>
      </g>

      <!-- Column 4: Dense Clay (x = 330) -->
      <g transform="translate(330, 25)">
        <rect x="0" y="0" width="60" height="90" rx="3" fill="#334155" fill-opacity="0.3" stroke="#64748b" stroke-width="1.5"/>
        <rect x="2" y="10" width="56" height="78" fill="#713f12"/>
        <!-- Surface Water Puddle on Clay -->
        <rect x="2" y="2" width="56" height="8" rx="2" fill="#38bdf8" fill-opacity="0.9"/>
        <polygon points="25,90 35,90 30,100" fill="#64748b"/>
        <rect x="5" y="110" width="50" height="35" rx="2" fill="none" stroke="#64748b"/>
        <rect id="beakerLevelClay" x="6" y="143" width="48" height="2" rx="1" fill="#38bdf8" fill-opacity="0.7"/>
        <text x="30" y="155" fill="#cbd5e1" font-size="8" font-weight="bold" text-anchor="middle">Clay</text>
        <text x="30" y="165" fill="#f87171" font-size="7" text-anchor="middle">Slowest (Puddles)</text>
      </g>
    </svg>
  </div>

  <!-- Interactive Action Buttons -->
  <div class="grid grid-cols-2 gap-2">
    <button id="btnPour100mlWater" class="p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow cursor-pointer">
      💧 Pour 100 mL Water Through All Columns
    </button>
    <button id="btnResetInfiltration" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition cursor-pointer">
      🔄 Empty Beakers & Reset
    </button>
  </div>

  <div id="infiltrationExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    ⏳ <span class="font-bold text-amber-300">Pore Size Dictates Flow:</span> Gravel and sand have large, wide open pore channels, allowing water to infiltrate rapidly. Clay consists of tightly packed microscopic platelets that swell upon wetting, creating very low permeability and causing surface puddles!
  </div>
</div>
''',
    "aquifer_ice_stupa_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🏔️ Ladakh's Ice Stupas: High-Altitude Innovation</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">7.4.1 Aquifers</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-bold">Sonam Wangchuk's Design</span>
  </div>

  <!-- Ice Stupa & Aquifer Diagram SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- High Himalayan Mountain Backdrop -->
      <polygon points="0,110 80,40 160,110" fill="#1e293b"/>
      <polygon points="60,40 80,40 100,60" fill="#f8fafc"/>
      <polygon points="120,110 220,30 320,110" fill="#334155"/>
      <polygon points="200,30 220,30 245,50" fill="#f8fafc"/>

      <!-- Valley Floor / Cold Desert (Ladakh) -->
      <rect x="0" y="110" width="440" height="80" fill="#78350f" fill-opacity="0.4"/>

      <!-- The Ice Stupa (Conical Artificial Glacier) Center -->
      <g transform="translate(180, 50)">
        <!-- Giant Ice Cone (Pyramid / Stupa Shape) -->
        <path d="M 40,0 L 0,80 L 80,80 Z" fill="#38bdf8" fill-opacity="0.8" stroke="#bae6fd" stroke-width="2"/>
        <!-- Inner Core Structure -->
        <line x1="40" y1="0" x2="40" y2="80" stroke="#0284c7" stroke-width="2"/>
        <!-- Vertical Pipe with Fountain Water Spray (Winter Freeze) -->
        <g stroke="#ffffff" stroke-width="1.5" stroke-dasharray="2,2">
          <line x1="40" y1="0" x2="30" y2="-15"/>
          <line x1="40" y1="0" x2="50" y2="-15"/>
          <line x1="40" y1="0" x2="40" y2="-18"/>
        </g>
        <text x="40" y="55" fill="#0c4a6e" font-size="8" font-weight="bold" text-anchor="middle">Ice Stupa</text>
        <text x="40" y="67" fill="#0369a1" font-size="7" text-anchor="middle">(Min Sun Area)</text>
      </g>

      <!-- Underground Aquifer Cutaway (Right) -->
      <g transform="translate(290, 115)">
        <!-- Soil Layer -->
        <rect x="0" y="0" width="135" height="15" fill="#854d0e"/>
        <text x="67" y="10" fill="#fef08a" font-size="6" text-anchor="middle">Topsoil</text>
        <!-- Water Table Line -->
        <line x1="0" y1="15" x2="135" y2="15" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,2"/>
        <text x="130" y="24" fill="#38bdf8" font-size="6" text-anchor="end">Water Table</text>
        <!-- Saturated Aquifer Sandstone Layer -->
        <rect x="0" y="26" width="135" height="35" fill="#0284c7" fill-opacity="0.4"/>
        <text x="67" y="45" fill="#e0f2fe" font-size="8" font-weight="bold" text-anchor="middle">Permeable Aquifer</text>
        <!-- Impermeable Bedrock -->
        <rect x="0" y="61" width="135" height="14" fill="#1e293b"/>
        <text x="67" y="70" fill="#94a3b8" font-size="6" text-anchor="middle">Impermeable Bedrock</text>
      </g>

      <!-- Gravity Pipe from Mountain Stream to Stupa -->
      <path d="M 60,70 Q 120,95 220,130" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="120" y="85" fill="#7dd3fc" font-size="7" font-weight="bold">Gravity Pipe (0 Electricity)</text>
    </svg>
  </div>

  <!-- Interactive Showcase Buttons -->
  <div class="grid grid-cols-2 gap-2">
    <button id="btnWinterFreezeStupa" class="p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow cursor-pointer">
      ❄️ Winter Spray: Freeze Ice Stupa (-20 °C)
    </button>
    <button id="btnSpringMeltIrrigate" class="p-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition shadow cursor-pointer">
      🌾 Spring Melt: Irrigate Crops (May)
    </button>
  </div>

  <div id="stupaExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    🏔️ <span class="font-bold text-cyan-300">Indigenous Engineering:</span> Ladakh farmers need water in April-May for sowing, but natural glaciers don't melt until July. Sonam Wangchuk's Ice Stupa freezes unused winter water into a steep cone. The minimal surface area delays melting, providing millions of liters of spring irrigation water!
  </div>
</div>
''',
    "ancient_heritage_cooling_sim": r'''
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🏛️ Ancient Indian Thermal Heritage: Matka & Jaali</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">Heritage Science</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-400 font-bold">Passive Cooling</span>
  </div>

  <!-- Terracotta Matka & Jaali Screen SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Left: Traditional Terracotta Matka (Ghada) -->
      <g transform="translate(90, 20)">
        <!-- Earthen Pot Body (Porous Clay) -->
        <ellipse cx="40" cy="80" rx="36" ry="38" fill="#b45309" stroke="#78350f" stroke-width="2"/>
        <path d="M 22,46 L 20,30 L 60,30 L 58,46 Z" fill="#92400e" stroke="#78350f" stroke-width="2"/>
        
        <!-- Water Level Inside -->
        <ellipse cx="40" cy="80" rx="30" ry="32" fill="#0284c7" fill-opacity="0.6"/>
        <text x="40" y="80" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Water</text>
        <text x="40" y="93" fill="#bae6fd" font-size="8" font-family="monospace" text-anchor="middle">24 °C (Chilled)</text>

        <!-- Evaporating Moisture Beads at Porous Surface -->
        <g stroke="#38bdf8" stroke-width="1.5" fill="#38bdf8" stroke-dasharray="2,2">
          <line x1="5" y1="80" x2="-8" y2="75"/>
          <line x1="75" y1="80" x2="88" y2="75"/>
          <line x1="15" y1="55" x2="5" y2="45"/>
          <line x1="65" y1="55" x2="75" y2="45"/>
        </g>
        <text x="40" y="132" fill="#facc15" font-size="8" font-weight="bold" text-anchor="middle">Terracotta Matka</text>
        <text x="40" y="143" fill="#cbd5e1" font-size="7" text-anchor="middle">Latent Heat of Vaporization</text>
      </g>

      <!-- Center Divider -->
      <line x1="210" y1="20" x2="210" y2="170" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>

      <!-- Right: Rajputana Jaali Screen (Hawa Mahal Architecture) -->
      <g transform="translate(250, 20)">
        <!-- Palace Wall Aperture -->
        <rect x="0" y="10" width="140" height="130" rx="6" fill="#1e293b" stroke="#475569" stroke-width="2"/>
        
        <!-- Perforated Stone Jaali Lattice -->
        <g fill="#92400e" stroke="#d97706" stroke-width="1">
          <!-- Geometric lattice perforations -->
          <circle cx="35" cy="40" r="8" fill="#0f172a"/>
          <circle cx="70" cy="40" r="8" fill="#0f172a"/>
          <circle cx="105" cy="40" r="8" fill="#0f172a"/>

          <circle cx="35" cy="70" r="8" fill="#0f172a"/>
          <circle cx="70" cy="70" r="8" fill="#0f172a"/>
          <circle cx="105" cy="70" r="8" fill="#0f172a"/>

          <circle cx="35" cy="100" r="8" fill="#0f172a"/>
          <circle cx="70" cy="100" r="8" fill="#0f172a"/>
          <circle cx="105" cy="100" r="8" fill="#0f172a"/>
        </g>

        <!-- Accelerated Cool Air Stream Arrows (Venturi Effect) -->
        <g stroke="#38bdf8" stroke-width="2" fill="#38bdf8">
          <line x1="70" y1="15" x2="70" y2="35"/>
          <polygon points="70,38 67,32 73,32"/>
        </g>
        <text x="70" y="152" fill="#facc15" font-size="8" font-weight="bold" text-anchor="middle">Carved Stone Jaali Screen</text>
        <text x="70" y="163" fill="#cbd5e1" font-size="7" text-anchor="middle">Venturi Convective Air Cooling</text>
      </g>
    </svg>
  </div>

  <!-- Interactive Heritage Buttons -->
  <div class="grid grid-cols-2 gap-2">
    <button id="btnExploreMatkaPhysics" class="p-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition shadow cursor-pointer">
      🏺 Explore Matka Evaporative Chilling
    </button>
    <button id="btnExploreJaaliPhysics" class="p-2.5 rounded-xl bg-cyan-700 hover:bg-cyan-600 text-white font-bold text-xs transition shadow cursor-pointer">
      🏛️ Explore Jaali Venturi Wind Physics
    </button>
  </div>

  <div id="ancientHeritageExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
    🏺 <span class="font-bold text-amber-300">Porous Evaporative Chilling:</span> Clay pot pores let water seep outward. As water evaporates into dry air, it extracts latent heat from the pot, chilling water by 5–10 °C without electricity! Jaalis constrict desert wind to accelerate and cool airflow via the Venturi effect.
  </div>
</div>
''',
}
