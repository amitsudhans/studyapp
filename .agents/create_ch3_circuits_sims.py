# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Science Chapter 3 Simulators HTML templates
Outputs .agents/class7_science_circuits_sims.py
"""

import json

SIMULATORS_HTML = {
    # Sim 1: Torchlight Anatomy & Safety
    "torchlight_anatomy_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🔦 Torchlight Anatomy Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">3.1 Safety</span>
    </div>
    <span id="torchStatusBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 font-bold">OFF</span>
  </div>

  <!-- Interactive Torchlight SVG -->
  <div class="relative w-full h-44 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 400 160" class="w-full h-full">
      <defs>
        <!-- Beam Gradient -->
        <linearGradient id="torchBeam" x1="0%" y1="50%" x2="100%" y2="50%">
          <stop offset="0%" stop-color="#fef08a" stop-opacity="0.85"/>
          <stop offset="50%" stop-color="#fde047" stop-opacity="0.35"/>
          <stop offset="100%" stop-color="#eab308" stop-opacity="0.0"/>
        </linearGradient>
        <radialGradient id="bulbGlow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#ffffff"/>
          <stop offset="60%" stop-color="#facc15"/>
          <stop offset="100%" stop-color="#ca8a04" stop-opacity="0"/>
        </radialGradient>
      </defs>

      <!-- Ray beam cone (shown when ON) -->
      <polygon id="torchBeamCone" points="90,80 390,20 390,140" fill="url(#torchBeam)" class="hidden transition-opacity duration-300"/>

      <!-- Parabolic Reflector Housing -->
      <path d="M 50,45 Q 90,45 95,30 L 95,130 Q 90,115 50,115 Z" fill="#334155" stroke="#64748b" stroke-width="2"/>
      <path d="M 55,55 Q 85,55 90,40 L 90,120 Q 85,105 55,105 Z" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1"/>

      <!-- Bulb inside reflector -->
      <circle id="torchBulb" cx="68" cy="80" r="10" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
      <circle id="torchBulbGlow" cx="68" cy="80" r="22" fill="url(#bulbGlow)" class="hidden"/>

      <!-- Main Cylindrical Body Casing -->
      <rect x="95" y="45" width="220" height="70" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2"/>

      <!-- Cell 1 (Left: 1.5V) -->
      <rect x="110" y="55" width="85" height="50" rx="4" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="97" y="72" width="13" height="16" rx="2" fill="#e2e8f0"/>
      <text x="152" y="84" font-size="11" font-family="monospace" fill="#e0f2fe" text-anchor="middle" font-weight="bold">Cell 1 (1.5V)</text>
      <text x="104" y="84" font-size="10" font-family="sans-serif" fill="#0f172a" text-anchor="middle" font-weight="bold">+</text>
      <text x="190" y="84" font-size="12" font-family="sans-serif" fill="#ffffff" text-anchor="middle" font-weight="bold">-</text>

      <!-- Cell 2 (Right: 1.5V) in series -->
      <rect x="210" y="55" width="85" height="50" rx="4" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="197" y="72" width="13" height="16" rx="2" fill="#e2e8f0"/>
      <text x="252" y="84" font-size="11" font-family="monospace" fill="#e0f2fe" text-anchor="middle" font-weight="bold">Cell 2 (1.5V)</text>
      <text x="204" y="84" font-size="10" font-family="sans-serif" fill="#0f172a" text-anchor="middle" font-weight="bold">+</text>
      <text x="290" y="84" font-size="12" font-family="sans-serif" fill="#ffffff" text-anchor="middle" font-weight="bold">-</text>

      <!-- Base Helical Spring -->
      <path d="M 295,80 Q 300,65 305,80 T 315,80" fill="none" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>

      <!-- Slide Switch on top casing -->
      <rect x="175" y="38" width="55" height="10" rx="4" fill="#0f172a" stroke="#64748b"/>
      <rect id="switchSliderBtn" x="177" y="34" width="22" height="18" rx="3" fill="#ef4444" stroke="#fca5a5" class="cursor-pointer transition-all duration-200"/>

      <!-- Metal Strip Connecting Switch to Bulb -->
      <line id="metalStrip" x1="90" y1="42" x2="185" y2="42" stroke="#64748b" stroke-width="3" stroke-dasharray="4,2"/>
    </svg>
  </div>

  <!-- Interactive Controls -->
  <div class="grid grid-cols-2 gap-2">
    <button id="toggleTorchBtn" class="px-3 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition shadow-md shadow-amber-600/30 flex items-center justify-center gap-1.5 cursor-pointer">
      <span>💡</span> <span id="torchBtnLabel">Slide Switch ON</span>
    </button>
    <button id="inspectTorchPartsBtn" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold text-xs transition flex items-center justify-center gap-1.5 cursor-pointer">
      <span>🔍</span> <span>Inspect Anatomy</span>
    </button>
  </div>

  <div id="torchInfoBox" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
    <strong class="text-amber-400">Torch Mechanism:</strong> Sliding the switch pushes a metallic contact strip forward, closing the circuit from the cells through the reflector bulb and base spring.
  </div>

  <!-- Safety Warning Banner -->
  <div class="p-2 rounded-lg bg-rose-950/40 border border-rose-500/30 flex items-center space-x-2 text-[10px] text-rose-300">
    <span class="text-base">⚠️</span>
    <span><strong>Safety Commandment:</strong> Only use 1.5V dry cells! Never connect student circuits to 230V domestic AC wall sockets or generators.</span>
  </div>
</div>
""",

    # Sim 2: Anatomy of an Electric Cell
    "cell_anatomy_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-cyan-400 font-bold text-sm">🔋 Electric Cell Anatomy</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-mono">3.2.1 Cell</span>
    </div>
    <span class="text-[11px] font-mono text-emerald-400 font-bold">1.5 V DC</span>
  </div>

  <!-- Cell Cutaway Graphic -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2">
    <svg viewBox="0 0 320 180" class="w-full h-full">
      <!-- Outer Zinc Canister (- electrode) -->
      <rect x="110" y="30" width="100" height="125" rx="6" fill="#475569" stroke="#94a3b8" stroke-width="2" class="cell-part cursor-pointer" data-part="zinc"/>
      
      <!-- Chemical Electrolyte Paste (MnO2 + NH4Cl) -->
      <rect x="118" y="38" width="84" height="110" fill="#334155" stroke="#64748b" stroke-width="1" class="cell-part cursor-pointer" data-part="paste"/>

      <!-- Central Carbon (Graphite) Rod -->
      <rect x="153" y="24" width="14" height="116" rx="2" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" class="cell-part cursor-pointer" data-part="carbon"/>

      <!-- Positive Terminal Metal Cap (+) -->
      <rect x="150" y="14" width="20" height="12" rx="3" fill="#e2e8f0" stroke="#f8fafc" stroke-width="1.5" class="cell-part cursor-pointer" data-part="cap"/>
      <text x="160" y="23" font-size="10" font-family="sans-serif" fill="#0f172a" text-anchor="middle" font-weight="extrabold">+</text>

      <!-- Negative Terminal Flat Base Disc (-) -->
      <rect x="114" y="152" width="92" height="10" rx="3" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1" class="cell-part cursor-pointer" data-part="base"/>
      <text x="160" y="160" font-size="10" font-family="sans-serif" fill="#0f172a" text-anchor="middle" font-weight="extrabold">-</text>

      <!-- Callout Labels -->
      <g class="text-[9px] font-sans fill-slate-300">
        <text x="50" y="22" text-anchor="end" fill="#38bdf8">Metal Cap (+)</text>
        <line x1="55" y1="20" x2="148" y2="20" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2,2"/>

        <text x="50" y="65" text-anchor="end" fill="#e2e8f0">Carbon Rod</text>
        <line x1="55" y1="63" x2="151" y2="63" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="2,2"/>

        <text x="270" y="70" text-anchor="start" fill="#a78bfa">Electrolyte Paste</text>
        <line x1="204" y1="68" x2="265" y2="68" stroke="#a78bfa" stroke-width="1" stroke-dasharray="2,2"/>

        <text x="270" y="115" text-anchor="start" fill="#94a3b8">Zinc Can (-)</text>
        <line x1="212" y1="113" x2="265" y2="113" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2,2"/>

        <text x="50" y="158" text-anchor="end" fill="#f43f5e">Flat Base (-)</text>
        <line x1="55" y1="156" x2="112" y2="156" stroke="#f43f5e" stroke-width="1" stroke-dasharray="2,2"/>
      </g>
    </svg>
  </div>

  <!-- Interactive Part Selector -->
  <div class="grid grid-cols-3 gap-1.5 text-[10px]">
    <button class="cell-select-btn px-2 py-1.5 rounded-lg bg-cyan-950 border border-cyan-500/40 text-cyan-200 font-semibold" data-part="cap">Metal Cap (+)</button>
    <button class="cell-select-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-part="carbon">Carbon Rod</button>
    <button class="cell-select-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-part="paste">Chemical Paste</button>
    <button class="cell-select-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-part="zinc">Zinc Can</button>
    <button class="cell-select-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-part="base">Flat Base (-)</button>
    <button id="probeTestBtn" class="px-2 py-1.5 rounded-lg bg-emerald-700 hover:bg-emerald-600 text-white font-bold">Probe Voltage</button>
  </div>

  <div id="cellInfoText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
    <strong class="text-cyan-400">Metal Cap (+):</strong> The positive terminal connected to the inner carbon electrode rod. Chemical reactions create an excess positive potential at this terminal.
  </div>
</div>
""",

    # Sim 3: Battery Series Cell Combinations & Voltage Addition
    "battery_series_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-purple-400 font-bold text-sm">⚡ Series Battery Builder</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-purple-500/20 text-purple-300 font-mono">3.2.2 Battery</span>
    </div>
    <div class="text-right">
      <span class="text-[10px] text-slate-400">Net Voltage: </span>
      <span id="seriesVoltsDisplay" class="text-xs font-mono font-extrabold text-amber-400">3.0 V</span>
    </div>
  </div>

  <!-- Battery & Lamp Circuit SVG -->
  <div class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2">
    <svg viewBox="0 0 380 150" class="w-full h-full">
      <!-- Battery Holder Base -->
      <rect x="25" y="35" width="220" height="80" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2"/>
      
      <!-- Cell 1 Slot -->
      <g id="slot1Group">
        <rect x="35" y="45" width="95" height="60" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
        <rect id="slot1Cap" x="127" y="65" width="10" height="20" rx="2" fill="#e2e8f0"/>
        <text x="82" y="80" font-size="11" font-family="monospace" fill="#ffffff" text-anchor="middle" font-weight="bold">1.5V Cell 1</text>
        <text id="slot1LabelLeft" x="43" y="80" font-size="12" font-family="sans-serif" fill="#ffffff" text-anchor="middle" font-weight="bold">-</text>
        <text id="slot1LabelRight" x="123" y="80" font-size="12" font-family="sans-serif" fill="#ffffff" text-anchor="middle" font-weight="bold">+</text>
      </g>

      <!-- Cell 2 Slot -->
      <g id="slot2Group">
        <rect x="140" y="45" width="95" height="60" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
        <rect id="slot2Cap" x="232" y="65" width="10" height="20" rx="2" fill="#e2e8f0"/>
        <text x="187" y="80" font-size="11" font-family="monospace" fill="#ffffff" text-anchor="middle" font-weight="bold">1.5V Cell 2</text>
        <text id="slot2LabelLeft" x="148" y="80" font-size="12" font-family="sans-serif" fill="#ffffff" text-anchor="middle" font-weight="bold">-</text>
        <text id="slot2LabelRight" x="228" y="80" font-size="12" font-family="sans-serif" fill="#ffffff" text-anchor="middle" font-weight="bold">+</text>
      </g>

      <!-- Connecting Circuit Wires -->
      <path d="M 242,75 L 310,75 L 310,50" fill="none" stroke="#eab308" stroke-width="2.5"/>
      <path d="M 35,75 L 15,75 L 15,130 L 330,130 L 330,50" fill="none" stroke="#38bdf8" stroke-width="2.5"/>

      <!-- Lamp -->
      <circle id="batteryBulbHalo" cx="320" cy="40" r="28" fill="#fef08a" opacity="0.6"/>
      <circle id="batteryBulb" cx="320" cy="40" r="14" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>
      <path d="M 314,44 Q 320,30 326,44" fill="none" stroke="#713f12" stroke-width="1.5"/>
      <rect x="313" y="52" width="14" height="10" fill="#64748b"/>
    </svg>
  </div>

  <!-- Controls -->
  <div class="grid grid-cols-2 gap-2 text-xs">
    <button id="addCellCountBtn" class="px-3 py-2 rounded-xl bg-purple-600 hover:bg-purple-500 text-white font-bold transition flex items-center justify-center gap-1 cursor-pointer">
      <span>➕</span> <span id="cellCountLabel">Cells: 2 (3.0V)</span>
    </button>
    <button id="flipCellPolarityBtn" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold transition flex items-center justify-center gap-1 cursor-pointer">
      <span>🔄</span> <span>Flip Cell 2 (+ to +)</span>
    </button>
  </div>

  <div id="batteryStatusMsg" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
    <strong class="text-emerald-400">Correct Series Connection:</strong> Negative (-) of Cell 1 touches Positive (+) of Cell 2. Voltages add constructively: 1.5 V + 1.5 V = 3.0 V. Bulb shines brightly!
  </div>
</div>
""",

    # Sim 4: Incandescent Lamp vs Modern LED Anatomy
    "lamp_vs_led_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">💡 Lamp vs Solid-State LED</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">3.2.3 Emitter</span>
    </div>
    <div class="flex items-center space-x-1">
      <button id="showBulbTabBtn" class="px-2 py-0.5 rounded bg-amber-500 text-slate-950 font-bold text-[10px]">Tungsten Bulb</button>
      <button id="showLedTabBtn" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-semibold text-[10px]">Modern LED</button>
    </div>
  </div>

  <!-- Anatomy Viewport SVG -->
  <div class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2 relative">
    
    <!-- View 1: Incandescent Bulb View -->
    <svg id="bulbAnatomySvg" viewBox="0 0 300 150" class="w-full h-full">
      <!-- Glass Envelope -->
      <path d="M 125,90 C 105,70 100,35 150,20 C 200,35 195,70 175,90 Z" fill="#334155" stroke="#94a3b8" stroke-width="1.5" opacity="0.8"/>
      
      <!-- Thick Support Posts -->
      <line x1="140" y1="90" x2="140" y2="48" stroke="#cbd5e1" stroke-width="2"/>
      <line x1="160" y1="90" x2="160" y2="48" stroke="#cbd5e1" stroke-width="2"/>

      <!-- Coiled Tungsten Filament -->
      <path id="tungstenFilamentPath" d="M 140,48 Q 145,38 150,48 T 160,48" fill="none" stroke="#f59e0b" stroke-width="2.5"/>

      <!-- Metal Screw Casing (Terminal 1) -->
      <rect x="135" y="90" width="30" height="24" rx="2" fill="#64748b" stroke="#cbd5e1"/>
      <line x1="135" y1="96" x2="165" y2="96" stroke="#475569" stroke-width="2"/>
      <line x1="135" y1="104" x2="165" y2="104" stroke="#475569" stroke-width="2"/>

      <!-- Insulating Ring -->
      <rect x="138" y="114" width="24" height="4" fill="#0f172a"/>

      <!-- Metal Tip Contact (Terminal 2) -->
      <path d="M 140,118 L 160,118 L 155,126 L 145,126 Z" fill="#94a3b8"/>

      <!-- Labels -->
      <text x="210" y="42" font-size="9" font-family="sans-serif" fill="#f59e0b">Tungsten (3422°C)</text>
      <text x="210" y="70" font-size="9" font-family="sans-serif" fill="#cbd5e1">Support Wires</text>
      <text x="210" y="102" font-size="9" font-family="sans-serif" fill="#94a3b8">Terminal 1 (Base)</text>
      <text x="210" y="124" font-size="9" font-family="sans-serif" fill="#94a3b8">Terminal 2 (Tip)</text>
    </svg>

    <!-- View 2: LED View (Hidden initially) -->
    <svg id="ledAnatomySvg" viewBox="0 0 300 150" class="w-full h-full hidden">
      <!-- Epoxy Lens Dome -->
      <path d="M 130,70 L 130,40 A 20,20 0 0,1 170,40 L 170,70 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" opacity="0.85"/>
      <rect x="127" y="70" width="46" height="6" rx="2" fill="#0369a1"/>

      <!-- Semiconductor Die / Anvil & Post -->
      <path d="M 142,66 L 142,50 L 148,46 L 152,46" fill="none" stroke="#e2e8f0" stroke-width="2"/>
      <line x1="158" y1="66" x2="158" y2="48" stroke="#e2e8f0" stroke-width="2"/>
      <!-- Tiny Semiconductor Chip -->
      <rect x="148" y="44" width="5" height="5" fill="#facc15"/>

      <!-- Anode Lead (Longer, +) -->
      <line x1="142" y1="76" x2="142" y2="135" stroke="#cbd5e1" stroke-width="2.5"/>
      <!-- Cathode Lead (Shorter, -) -->
      <line x1="158" y1="76" x2="158" y2="115" stroke="#cbd5e1" stroke-width="2.5"/>

      <!-- Polarity Callouts -->
      <text x="135" y="142" font-size="10" font-family="monospace" fill="#22c55e" font-weight="bold">+ Anode (Long)</text>
      <text x="165" y="122" font-size="10" font-family="monospace" fill="#f43f5e" font-weight="bold">- Cathode (Short)</text>
      <text x="220" y="48" font-size="9" font-family="sans-serif" fill="#38bdf8">Semiconductor P-N</text>
      <text x="220" y="62" font-size="9" font-family="sans-serif" fill="#94a3b8">No Filament!</text>
    </svg>
  </div>

  <!-- Comparison Specs -->
  <div class="grid grid-cols-2 gap-2 text-[11px] p-2 rounded-xl bg-slate-950 border border-slate-800">
    <div id="techCard1">
      <div class="font-bold text-amber-400">Incandescent Bulb</div>
      <div class="text-slate-400 text-[10px]">Efficiency: ~10% light (90% heat)</div>
      <div class="text-slate-400 text-[10px]">Polarity: None (works either way)</div>
    </div>
    <div id="techCard2">
      <div class="font-bold text-cyan-400">Light Emitting Diode</div>
      <div class="text-slate-400 text-[10px]">Efficiency: ~90% light (cool!)</div>
      <div class="text-slate-400 text-[10px]">Polarity: Strict (+ to long leg)</div>
    </div>
  </div>
</div>
""",

    # Sim 5: Circuit Loop Construction Lab
    "circuit_loop_lab_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-emerald-400 font-bold text-sm">🔬 Circuit Loop Construction</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-mono">3.2.4 Lab</span>
    </div>
    <span id="loopResultBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-300 border border-emerald-500/40 font-bold">Closed Loop (GLOWS)</span>
  </div>

  <!-- Interactive Workbench SVG -->
  <div class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2">
    <svg id="loopWorkbenchSvg" viewBox="0 0 340 150" class="w-full h-full">
      <!-- Dry Cell -->
      <rect x="50" y="40" width="80" height="70" rx="6" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
      <rect x="40" y="65" width="10" height="20" rx="2" fill="#f8fafc"/>
      <text x="90" y="80" font-size="12" font-family="monospace" fill="#ffffff" text-anchor="middle" font-weight="bold">1.5V</text>
      <text x="45" y="78" font-size="11" font-family="sans-serif" fill="#0f172a" text-anchor="middle" font-weight="bold">+</text>
      <text x="122" y="78" font-size="14" font-family="sans-serif" fill="#ffffff" text-anchor="middle" font-weight="bold">-</text>

      <!-- Light Bulb -->
      <circle id="loopBulbHalo" cx="260" cy="75" r="28" fill="#fef08a" opacity="0.6"/>
      <circle id="loopBulb" cx="260" cy="75" r="14" fill="#facc15" stroke="#ca8a04" stroke-width="2"/>
      <rect x="254" y="87" width="12" height="12" fill="#64748b"/>
      <path d="M 255,75 Q 260,65 265,75" fill="none" stroke="#713f12" stroke-width="1.5"/>

      <!-- Dynamic Connecting Wires -->
      <!-- Wire 1 (Top / Lead 1) -->
      <path id="wire1Path" d="M 40,75 C 40,20 254,20 254,87" fill="none" stroke="#ef4444" stroke-width="3"/>
      <!-- Wire 2 (Bottom / Lead 2) -->
      <path id="wire2Path" d="M 130,75 C 130,135 260,135 260,99" fill="none" stroke="#3b82f6" stroke-width="3"/>
    </svg>
  </div>

  <!-- 4 Presets Selection -->
  <div class="grid grid-cols-4 gap-1.5 text-[10px]">
    <button class="loop-preset-btn px-2 py-1.5 rounded-lg bg-emerald-950 border border-emerald-500/40 text-emerald-200 font-bold" data-setup="A">Setup A (Ideal)</button>
    <button class="loop-preset-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-setup="B">Setup B (Cut Top)</button>
    <button class="loop-preset-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-setup="C">Setup C (Cut Bot)</button>
    <button class="loop-preset-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-setup="D">Setup D (Short)</button>
  </div>

  <div id="loopExplanationText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
    <strong class="text-emerald-400">Setup A:</strong> Complete continuous loop! Wire 1 connects cell (+) to bulb casing; Wire 2 connects cell (-) to bulb base tip. Current circulates freely and the bulb glows.
  </div>
</div>
""",

    # Sim 6: Conventional Current vs Electron Flow
    "current_flow_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-cyan-400 font-bold text-sm">🔄 Conventional Current Flow</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-mono">3.2.5 Loop</span>
    </div>
    <button id="toggleCurrentModeBtn" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-[10px] text-cyan-300 font-mono">
      Mode: Conventional (+ to -)
    </button>
  </div>

  <!-- Animated Circuit Loop -->
  <div class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2 relative overflow-hidden">
    <svg viewBox="0 0 340 150" class="w-full h-full">
      <!-- Circuit Wire Rectangle -->
      <rect x="40" y="30" width="260" height="90" rx="8" fill="none" stroke="#334155" stroke-width="4"/>

      <!-- Dry Cell on Left Branch -->
      <rect x="25" y="55" width="30" height="40" rx="3" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="35" y="48" width="10" height="8" rx="1" fill="#f8fafc"/>
      <text x="40" y="54" font-size="8" font-family="sans-serif" fill="#0f172a" text-anchor="middle" font-weight="bold">+</text>
      <text x="40" y="99" font-size="10" font-family="sans-serif" fill="#ffffff" text-anchor="middle" font-weight="bold">-</text>

      <!-- Bulb on Right Branch -->
      <circle id="flowBulbHalo" cx="300" cy="75" r="24" fill="#fef08a" opacity="0.6"/>
      <circle id="flowBulb" cx="300" cy="75" r="12" fill="#facc15" stroke="#ca8a04" stroke-width="1.5"/>
      <rect x="295" y="85" width="10" height="10" fill="#64748b"/>

      <!-- Direction Arrow Indicators (Animated) -->
      <!-- Top Wire Arrow (Left to Right) -->
      <g id="arrowTop" transform="translate(170, 30)">
        <polygon points="-8,-4 0,0 -8,4" fill="#ef4444"/>
      </g>
      <!-- Bottom Wire Arrow (Right to Left) -->
      <g id="arrowBottom" transform="translate(170, 120)">
        <polygon points="8,-4 0,0 8,4" fill="#ef4444"/>
      </g>

      <!-- Flowing particle markers -->
      <circle id="particle1" cx="80" cy="30" r="3" fill="#ef4444"/>
      <circle id="particle2" cx="160" cy="30" r="3" fill="#ef4444"/>
      <circle id="particle3" cx="240" cy="30" r="3" fill="#ef4444"/>
      <circle id="particle4" cx="240" cy="120" r="3" fill="#ef4444"/>
      <circle id="particle5" cx="160" cy="120" r="3" fill="#ef4444"/>
      <circle id="particle6" cx="80" cy="120" r="3" fill="#ef4444"/>
    </svg>
  </div>

  <div class="flex items-center justify-between text-xs">
    <button id="toggleCircuitPowerBtn" class="px-3 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold transition flex items-center gap-1">
      <span>⏹</span> <span id="powerBtnLabel">Pause Current</span>
    </button>
    <span class="text-[11px] text-slate-400">Current Speed: <strong id="speedLabel" class="text-cyan-400">1.0x</strong></span>
  </div>

  <div id="flowExplText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
    <strong class="text-cyan-400">Conventional Current:</strong> Flows outward from the positive (+) terminal through the external circuit and returns to the negative (-) terminal.
  </div>
</div>
""",

    # Sim 7: Fused Lamp Diagnostics
    "fused_bulb_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-rose-400 font-bold text-sm">🔍 Fused Bulb Diagnostics</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-rose-500/20 text-rose-300 font-mono">3.2.5 Diagnostics</span>
    </div>
    <span id="multimeterDisplay" class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-950 border border-slate-800 text-emerald-400">2.5 Ω (OK)</span>
  </div>

  <!-- Microscope Zoom View of Filament -->
  <div class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2 relative">
    <svg viewBox="0 0 320 150" class="w-full h-full">
      <!-- Microscope Lens Reticle Circle -->
      <circle cx="160" cy="75" r="65" fill="#0f172a" stroke="#475569" stroke-width="2"/>
      <line x1="95" y1="75" x2="225" y2="75" stroke="#334155" stroke-dasharray="2,2"/>
      <line x1="160" y1="10" x2="160" y2="140" stroke="#334155" stroke-dasharray="2,2"/>

      <!-- Support Posts -->
      <line x1="125" y1="130" x2="125" y2="65" stroke="#94a3b8" stroke-width="3"/>
      <line x1="195" y1="130" x2="195" y2="65" stroke="#94a3b8" stroke-width="3"/>

      <!-- Filament Graphic (Normal vs Fused) -->
      <!-- Good Filament Path -->
      <path id="goodFilamentSvg" d="M 125,65 Q 140,45 160,65 T 195,65" fill="none" stroke="#f59e0b" stroke-width="3"/>
      
      <!-- Fused Filament Paths (Hidden initially) -->
      <g id="fusedFilamentSvg" class="hidden">
        <path d="M 125,65 Q 135,50 148,60" fill="none" stroke="#ef4444" stroke-width="3"/>
        <path d="M 172,60 Q 185,50 195,65" fill="none" stroke="#ef4444" stroke-width="3"/>
        <!-- Broken Air Gap marker -->
        <circle cx="160" cy="60" r="8" fill="none" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="2,2"/>
        <text x="160" y="38" font-size="9" font-family="sans-serif" fill="#f43f5e" text-anchor="middle" font-weight="bold">AIR GAP (I = 0)</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2 text-xs">
    <button id="setBulbGoodBtn" class="px-3 py-2 rounded-xl bg-emerald-700 hover:bg-emerald-600 text-white font-bold transition flex items-center justify-center gap-1">
      <span>✓</span> <span>Intact Bulb (Working)</span>
    </button>
    <button id="setBulbFusedBtn" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold transition flex items-center justify-center gap-1">
      <span>⚡</span> <span>Snap Filament (Fused)</span>
    </button>
  </div>

  <div id="fusedInfoBox" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
    <strong class="text-emerald-400">Intact Filament:</strong> The coiled tungsten wire forms an unbroken bridge between the support wires. Multimeter registers low resistance ($2.5\,Ω$). Circuit remains closed!
  </div>
</div>
""",

    # Sim 8: LED Polarity & Forward Bias Tester
    "led_polarity_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-cyan-400 font-bold text-sm">💡 LED Polarity Tester</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-mono">3.2.5 Bias</span>
    </div>
    <span id="biasStateBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-300 border border-emerald-500/40 font-bold">Forward Bias (GLOWS)</span>
  </div>

  <!-- LED Circuit SVG -->
  <div class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2 relative">
    <svg viewBox="0 0 340 150" class="w-full h-full">
      <!-- 3V Battery on Left -->
      <rect x="30" y="50" width="60" height="50" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="22" y="65" width="8" height="20" rx="2" fill="#e2e8f0"/>
      <text x="60" y="80" font-size="11" font-family="monospace" fill="#ffffff" text-anchor="middle" font-weight="bold">3V Battery</text>
      <text x="26" y="78" font-size="11" font-family="sans-serif" fill="#0f172a" text-anchor="middle" font-weight="bold">+</text>
      <text x="83" y="78" font-size="13" font-family="sans-serif" fill="#ffffff" text-anchor="middle" font-weight="bold">-</text>

      <!-- Wires -->
      <path id="ledWireTop" d="M 22,75 C 22,25 240,25 240,65" fill="none" stroke="#22c55e" stroke-width="2.5"/>
      <path id="ledWireBottom" d="M 90,75 C 90,125 270,125 270,75" fill="none" stroke="#f43f5e" stroke-width="2.5"/>

      <!-- LED Component -->
      <circle id="ledGlowHalo" cx="255" cy="45" r="26" fill="#22c55e" opacity="0.6"/>
      <!-- LED Dome -->
      <path id="ledDomeSvg" d="M 240,55 L 240,35 A 15,15 0 0,1 270,35 L 270,55 Z" fill="#15803d" stroke="#4ade80" stroke-width="1.5"/>
      <!-- Leads -->
      <line id="leadLong" x1="245" y1="55" x2="245" y2="85" stroke="#cbd5e1" stroke-width="2"/>
      <line id="leadShort" x1="265" y1="55" x2="265" y2="75" stroke="#cbd5e1" stroke-width="2"/>
      
      <!-- Lead Labels -->
      <text id="anodeLabel" x="245" y="100" font-size="9" font-family="monospace" fill="#22c55e" text-anchor="middle">Long (+)</text>
      <text id="cathodeLabel" x="270" y="90" font-size="9" font-family="monospace" fill="#f43f5e" text-anchor="middle">Short (-)</text>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2 text-xs">
    <button id="setForwardBiasBtn" class="px-3 py-2 rounded-xl bg-emerald-700 hover:bg-emerald-600 text-white font-bold transition flex items-center justify-center gap-1">
      <span>✓</span> <span>Forward Bias (+ to Long)</span>
    </button>
    <button id="setReverseBiasBtn" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold transition flex items-center justify-center gap-1">
      <span>🔄</span> <span>Reverse Bias (- to Long)</span>
    </button>
  </div>

  <div id="ledBiasInfoText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
    <strong class="text-emerald-400">Forward Bias:</strong> Cell positive (+) connects to the longer Anode lead. Electrons and holes cross the semiconductor barrier, recombine, and emit brilliant green photons!
  </div>
</div>
""",

    # Sim 9: DIY Safety Pin Switch Builder
    "switch_mechanism_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🧷 DIY Safety Pin Switch</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">3.2.6 Switch</span>
    </div>
    <span id="diySwitchStatusBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 font-bold">OFF (Open Air Gap)</span>
  </div>

  <!-- Interactive Workbench SVG -->
  <div class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2 relative">
    <svg viewBox="0 0 360 150" class="w-full h-full">
      <!-- Thermocol / Cardboard Base Board -->
      <rect x="20" y="30" width="220" height="90" rx="8" fill="#d97706" opacity="0.3" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="35" y="46" font-size="9" font-family="sans-serif" fill="#f59e0b">Cardboard Base</text>

      <!-- Brass Drawing Pin 1 (Pivot) -->
      <circle cx="80" cy="75" r="10" fill="#eab308" stroke="#ca8a04" stroke-width="2"/>
      <circle cx="80" cy="75" r="4" fill="#a16207"/>

      <!-- Brass Drawing Pin 2 (Contact) -->
      <circle cx="180" cy="75" r="10" fill="#eab308" stroke="#ca8a04" stroke-width="2"/>
      <circle cx="180" cy="75" r="4" fill="#a16207"/>

      <!-- Safety Pin (Rotatable Metallic Arm) -->
      <g id="safetyPinArm" transform="rotate(-30, 80, 75)" class="cursor-pointer transition-transform duration-300">
        <!-- Safety Pin Loop Around Pin 1 -->
        <circle cx="80" cy="75" r="7" fill="none" stroke="#cbd5e1" stroke-width="3"/>
        <!-- Safety Pin Body Shaft -->
        <line x1="80" y1="75" x2="180" y2="75" stroke="#e2e8f0" stroke-width="4" stroke-linecap="round"/>
        <!-- Pin Head Clasp -->
        <rect x="175" y="70" width="14" height="10" rx="3" fill="#94a3b8"/>
      </g>

      <!-- Bulb in Circuit -->
      <circle id="switchBulbHalo" cx="300" cy="75" r="26" fill="#fef08a" opacity="0" class="transition-opacity duration-200"/>
      <circle id="switchBulb" cx="300" cy="75" r="13" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
      <rect x="295" y="87" width="10" height="10" fill="#475569"/>

      <!-- Wires -->
      <path d="M 80,75 L 80,135 L 300,135 L 300,97" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <path d="M 180,75 L 180,20 L 300,20 L 300,62" fill="none" stroke="#eab308" stroke-width="2.5"/>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2 text-xs">
    <button id="toggleDiySwitchBtn" class="px-3 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold transition flex items-center justify-center gap-1 cursor-pointer">
      <span>🧷</span> <span id="diyBtnText">Rotate Pin: Close Switch (ON)</span>
    </button>
    <button id="showAirGapExplBtn" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold transition flex items-center justify-center gap-1">
      <span>💨</span> <span>Air Gap Physics</span>
    </button>
  </div>

  <div id="switchExplText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
    <strong class="text-rose-400">Switch OFF (Open):</strong> The safety pin does not touch the second drawing pin. An air gap breaks the conducting path. Air is an insulator, so current cannot jump the gap!
  </div>
</div>
""",

    # Sim 10: Circuit Symbols Rosetta Stone
    "symbols_rosetta_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-purple-400 font-bold text-sm">📜 Circuit Symbols Rosetta Stone</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-purple-500/20 text-purple-300 font-mono">3.3 Symbols</span>
    </div>
    <span class="text-[11px] text-slate-400">Click a component below</span>
  </div>

  <!-- Side-by-Side Comparison Display -->
  <div class="grid grid-cols-2 gap-3 bg-slate-950 p-3 rounded-xl border border-slate-800 h-40">
    <!-- Left: Realistic Graphic -->
    <div class="flex flex-col items-center justify-center border-r border-slate-800/80 pr-2">
      <div class="text-[10px] text-slate-400 uppercase tracking-wider mb-1 font-bold">Realistic Object</div>
      <div id="symbolRealGraphic" class="w-full flex-1 flex items-center justify-center text-4xl">
        🔋
      </div>
      <div id="symbolRealName" class="text-xs font-bold text-cyan-300">Dry Electric Cell</div>
    </div>

    <!-- Right: Universal Schematic Symbol -->
    <div class="flex flex-col items-center justify-center pl-2">
      <div class="text-[10px] text-slate-400 uppercase tracking-wider mb-1 font-bold">Engineering Schematic Symbol</div>
      <div id="symbolSchematicGraphic" class="w-full flex-1 flex items-center justify-center">
        <!-- SVG Symbol injected via JS -->
        <svg viewBox="0 0 100 60" class="w-24 h-16">
          <line x1="10" y1="30" x2="45" y2="30" stroke="#38bdf8" stroke-width="2"/>
          <line x1="45" y1="12" x2="45" y2="48" stroke="#38bdf8" stroke-width="1.5"/>
          <line x1="55" y1="20" x2="55" y2="40" stroke="#f43f5e" stroke-width="4"/>
          <line x1="55" y1="30" x2="90" y2="30" stroke="#f43f5e" stroke-width="2"/>
          <text x="43" y="10" font-size="8" fill="#38bdf8" text-anchor="middle">+</text>
          <text x="56" y="16" font-size="9" fill="#f43f5e" text-anchor="middle">-</text>
        </svg>
      </div>
      <div id="symbolSymbolRule" class="text-[10px] font-mono text-purple-300">Long Thin (+) & Short Thick (-)</div>
    </div>
  </div>

  <!-- Component Buttons Grid -->
  <div class="grid grid-cols-3 sm:grid-cols-6 gap-1.5 text-[10px]">
    <button class="symbol-btn px-2 py-1.5 rounded-lg bg-purple-950 border border-purple-500/40 text-purple-200 font-bold" data-comp="cell">Cell</button>
    <button class="symbol-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-comp="battery">Battery</button>
    <button class="symbol-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-comp="bulb">Bulb</button>
    <button class="symbol-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-comp="switch_on">Switch ON</button>
    <button class="symbol-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-comp="switch_off">Switch OFF</button>
    <button class="symbol-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-comp="wire">Wire</button>
  </div>

  <div id="symbolExplBox" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
    <strong class="text-purple-400">Electric Cell:</strong> Long thin line represents the positive terminal (+); shorter, thicker line represents the negative terminal (-).
  </div>
</div>
""",

    # Sim 11: Schematic vs Pictorial Circuit Designer
    "schematic_designer_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-cyan-400 font-bold text-sm">📐 Schematic vs Pictorial View</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-mono">3.3 Translation</span>
    </div>
    <div class="flex items-center space-x-1">
      <button id="viewPictorialBtn" class="px-2 py-0.5 rounded bg-cyan-600 text-white font-bold text-[10px]">Realistic View</button>
      <button id="viewSchematicBtn" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-semibold text-[10px]">Schematic View</button>
    </div>
  </div>

  <!-- Dynamic Circuit Canvas -->
  <div class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2 relative overflow-hidden">
    <!-- View A: Pictorial -->
    <svg id="canvasPictorialSvg" viewBox="0 0 340 150" class="w-full h-full">
      <!-- 3D style Cell -->
      <rect x="40" y="50" width="70" height="50" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
      <rect x="32" y="65" width="8" height="20" rx="2" fill="#e2e8f0"/>
      <text x="75" y="80" font-size="10" font-family="monospace" fill="#ffffff" text-anchor="middle">Cell</text>
      
      <!-- Safety Pin Switch -->
      <rect x="140" y="25" width="60" height="30" rx="4" fill="#78350f" opacity="0.4"/>
      <circle cx="155" cy="40" r="5" fill="#eab308"/>
      <circle cx="185" cy="40" r="5" fill="#eab308"/>
      <line id="pictSwitchLine" x1="155" y1="40" x2="185" y2="40" stroke="#cbd5e1" stroke-width="3"/>

      <!-- Bulb -->
      <circle id="pictBulbGlow" cx="280" cy="75" r="24" fill="#fef08a" opacity="0.6"/>
      <circle id="pictBulb" cx="280" cy="75" r="13" fill="#facc15" stroke="#ca8a04" stroke-width="1.5"/>
      <rect x="275" y="87" width="10" height="10" fill="#64748b"/>

      <!-- Wires -->
      <path d="M 32,75 L 15,75 L 15,40 L 155,40" fill="none" stroke="#ef4444" stroke-width="2.5"/>
      <path d="M 185,40 L 280,40 L 280,62" fill="none" stroke="#ef4444" stroke-width="2.5"/>
      <path d="M 110,75 L 280,75 L 280,97" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
    </svg>

    <!-- View B: Schematic Blueprint (Clean Straight Lines) -->
    <svg id="canvasSchematicSvg" viewBox="0 0 340 150" class="w-full h-full hidden">
      <!-- Rectangular Wires -->
      <rect x="50" y="30" width="240" height="90" fill="none" stroke="#64748b" stroke-width="2"/>

      <!-- Cell Symbol on Left -->
      <rect x="42" y="60" width="16" height="30" fill="#0f172a"/>
      <line x1="40" y1="63" x2="60" y2="63" stroke="#38bdf8" stroke-width="1.5"/>
      <line x1="45" y1="83" x2="55" y2="83" stroke="#f43f5e" stroke-width="3.5"/>
      <text x="65" y="66" font-size="9" fill="#38bdf8" font-family="sans-serif">+</text>
      <text x="65" y="86" font-size="10" fill="#f43f5e" font-family="sans-serif">-</text>

      <!-- Switch Symbol on Top -->
      <rect x="150" y="24" width="40" height="12" fill="#0f172a"/>
      <circle cx="155" cy="30" r="3" fill="#38bdf8"/>
      <circle cx="185" cy="30" r="3" fill="#38bdf8"/>
      <line id="schemSwitchLine" x1="155" y1="30" x2="185" y2="30" stroke="#38bdf8" stroke-width="2"/>

      <!-- Bulb Symbol on Right -->
      <rect x="282" y="63" width="16" height="24" fill="#0f172a"/>
      <circle id="schemBulbGlow" cx="290" cy="75" r="18" fill="#fef08a" opacity="0.6"/>
      <circle cx="290" cy="75" r="10" fill="#0f172a" stroke="#facc15" stroke-width="1.5"/>
      <path d="M 285,75 Q 290,68 295,75" fill="none" stroke="#facc15" stroke-width="1.5"/>
    </svg>
  </div>

  <div class="flex items-center justify-between text-xs">
    <button id="toggleSchemSwitchBtn" class="px-3 py-1.5 rounded-lg bg-cyan-700 hover:bg-cyan-600 text-white font-bold transition flex items-center gap-1 cursor-pointer">
      <span>🔘</span> <span id="schemSwitchLabel">Switch: ON</span>
    </button>
    <span class="text-[11px] text-slate-400">Status: <strong class="text-emerald-400">Closed Circuit</strong></span>
  </div>

  <div id="schemExplText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
    <strong class="text-cyan-400">Engineering Standard:</strong> Schematics replace complex physical shapes with clean lines and universal symbols, allowing anyone in the world to understand the circuit blueprint.
  </div>
</div>
""",

    # Sim 12: Series vs Parallel Circuit Preview
    "series_parallel_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">💡💡 Series vs Parallel Architectures</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">3.3 Architectures</span>
    </div>
    <div class="flex items-center space-x-1">
      <button id="modeSeriesBtn" class="px-2 py-0.5 rounded bg-amber-500 text-slate-950 font-bold text-[10px]">Series (1 Loop)</button>
      <button id="modeParallelBtn" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-semibold text-[10px]">Parallel (Branches)</button>
    </div>
  </div>

  <!-- Comparison Circuit Canvas -->
  <div class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2 relative">
    <!-- View A: Series Circuit -->
    <svg id="circuitSeriesSvg" viewBox="0 0 340 150" class="w-full h-full">
      <!-- Wires -->
      <rect x="40" y="30" width="260" height="90" fill="none" stroke="#475569" stroke-width="2.5"/>

      <!-- Cell on Left -->
      <rect x="30" y="60" width="20" height="30" fill="#0284c7"/>
      <text x="40" y="78" font-size="8" fill="#ffffff" text-anchor="middle">3V</text>

      <!-- Bulb 1 on Top -->
      <circle id="serBulb1Halo" cx="130" cy="30" r="16" fill="#fef08a" opacity="0.4"/>
      <circle id="serBulb1" cx="130" cy="30" r="10" fill="#facc15" stroke="#ca8a04" stroke-width="1.5" class="cursor-pointer" title="Click to unscrew"/>
      <text x="130" y="55" font-size="9" fill="#94a3b8" text-anchor="middle">Bulb 1</text>

      <!-- Bulb 2 on Top -->
      <circle id="serBulb2Halo" cx="210" cy="30" r="16" fill="#fef08a" opacity="0.4"/>
      <circle id="serBulb2" cx="210" cy="30" r="10" fill="#facc15" stroke="#ca8a04" stroke-width="1.5" class="cursor-pointer" title="Click to unscrew"/>
      <text x="210" y="55" font-size="9" fill="#94a3b8" text-anchor="middle">Bulb 2</text>
    </svg>

    <!-- View B: Parallel Circuit (Hidden initially) -->
    <svg id="circuitParallelSvg" viewBox="0 0 340 150" class="w-full h-full hidden">
      <!-- Main Bus Wires -->
      <line x1="60" y1="40" x2="280" y2="40" stroke="#475569" stroke-width="2.5"/>
      <line x1="60" y1="110" x2="280" y2="110" stroke="#475569" stroke-width="2.5"/>
      <line x1="60" y1="40" x2="60" y2="110" stroke="#475569" stroke-width="2.5"/>

      <!-- Cell on Left -->
      <rect x="50" y="65" width="20" height="20" fill="#0284c7"/>

      <!-- Branch 1: Bulb 1 -->
      <line x1="160" y1="40" x2="160" y2="110" stroke="#475569" stroke-width="2"/>
      <circle id="parBulb1Halo" cx="160" cy="75" r="20" fill="#fef08a" opacity="0.6"/>
      <circle id="parBulb1" cx="160" cy="75" r="11" fill="#facc15" stroke="#ca8a04" stroke-width="1.5" class="cursor-pointer"/>
      <text x="160" y="100" font-size="9" fill="#94a3b8" text-anchor="middle">Bulb 1</text>

      <!-- Branch 2: Bulb 2 -->
      <line x1="250" y1="40" x2="250" y2="110" stroke="#475569" stroke-width="2"/>
      <circle id="parBulb2Halo" cx="250" cy="75" r="20" fill="#fef08a" opacity="0.6"/>
      <circle id="parBulb2" cx="250" cy="75" r="11" fill="#facc15" stroke="#ca8a04" stroke-width="1.5" class="cursor-pointer"/>
      <text x="250" y="100" font-size="9" fill="#94a3b8" text-anchor="middle">Bulb 2</text>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2 text-xs">
    <button id="toggleBulb1UnscrewBtn" class="px-3 py-1.5 rounded-lg bg-rose-700 hover:bg-rose-600 text-white font-bold transition flex items-center justify-center gap-1 cursor-pointer">
      <span>💡</span> <span id="unscrewBtnLabel">Unscrew Bulb 1</span>
    </button>
    <div id="archSummaryText" class="p-1.5 rounded-lg bg-slate-950 border border-slate-800 text-[10px] text-slate-300 flex items-center">
      Series: Unscrewing Bulb 1 breaks the single loop! Bulb 2 goes dark.
    </div>
  </div>
</div>
""",

    # Sim 13: Conduction Tester Laboratory
    "conduction_tester_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-emerald-400 font-bold text-sm">🧪 Conduction Tester Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-mono">3.4 Tester</span>
    </div>
    <span id="conductionResultBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-300 border border-emerald-500/40 font-bold">CONDUCTOR (Glows!)</span>
  </div>

  <!-- Testing Stage Graphic -->
  <div class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2 relative">
    <svg viewBox="0 0 340 150" class="w-full h-full">
      <!-- Battery and Bulb Circuit -->
      <rect x="40" y="45" width="50" height="60" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="65" y="78" font-size="10" font-family="monospace" fill="#ffffff" text-anchor="middle">1.5V Cell</text>

      <circle id="testerBulbHalo" cx="300" cy="75" r="26" fill="#fef08a" opacity="0.6"/>
      <circle id="testerBulb" cx="300" cy="75" r="13" fill="#facc15" stroke="#ca8a04" stroke-width="1.5"/>
      <rect x="295" y="87" width="10" height="10" fill="#64748b"/>

      <!-- Wires with open probe gap -->
      <path d="M 65,45 L 65,25 L 140,25" fill="none" stroke="#eab308" stroke-width="2.5"/>
      <path d="M 65,105 L 65,125 L 300,125 L 300,97" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <path d="M 300,25 L 200,25" fill="none" stroke="#eab308" stroke-width="2.5"/>

      <!-- Probe A (Left) -->
      <circle cx="140" cy="25" r="4" fill="#ef4444"/>
      <text x="135" y="18" font-size="9" fill="#ef4444" font-family="monospace" font-weight="bold">Probe A</text>

      <!-- Probe B (Right) -->
      <circle cx="200" cy="25" r="4" fill="#3b82f6"/>
      <text x="205" y="18" font-size="9" fill="#3b82f6" font-family="monospace" font-weight="bold">Probe B</text>

      <!-- Test Object Placed Across Probes -->
      <g id="testObjectGraphic" transform="translate(140, 18)">
        <!-- Default: Copper Wire Strip -->
        <rect id="objShape" x="0" y="2" width="60" height="10" rx="3" fill="#b45309" stroke="#f59e0b" stroke-width="1.5"/>
        <text id="objLabel" x="30" y="10" font-size="8" font-family="sans-serif" fill="#ffffff" text-anchor="middle" font-weight="bold">Copper Strip</text>
      </g>
    </svg>
  </div>

  <!-- Material Selectors (8 items) -->
  <div class="grid grid-cols-4 gap-1.5 text-[10px]">
    <button class="mat-test-btn px-2 py-1.5 rounded-lg bg-emerald-950 border border-emerald-500/40 text-emerald-200 font-bold" data-mat="copper">Copper Wire</button>
    <button class="mat-test-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-mat="iron">Iron Nail</button>
    <button class="mat-test-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-mat="graphite">Pencil Graphite</button>
    <button class="mat-test-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-mat="lemon">Lemon Juice</button>
    <button class="mat-test-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-mat="plastic">Plastic Ruler</button>
    <button class="mat-test-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-mat="rubber">Rubber Eraser</button>
    <button class="mat-test-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-mat="wood">Dry Toothpick</button>
    <button class="mat-test-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300" data-mat="glass">Glass Rod</button>
  </div>

  <div id="conductionExplText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
    <strong class="text-emerald-400">Copper Wire (Good Conductor):</strong> Copper contains sea of mobile free electrons that carry electric charges effortlessly. Circuit loop closes; bulb glows brilliantly!
  </div>
</div>
""",

    # Sim 14: Engineering Wire Insulation & Short Circuits
    "wire_insulation_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-cyan-400 font-bold text-sm">🛡️ Wire Insulation & Safety</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-mono">3.4 Insulation</span>
    </div>
    <span class="text-[11px] font-mono text-emerald-400 font-bold">100% Insulated</span>
  </div>

  <!-- Cutaway Wire Graphic -->
  <div class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2 relative">
    <svg viewBox="0 0 340 150" class="w-full h-full">
      <!-- Outer PVC Insulation Layer (Orange) -->
      <rect id="pvcSleeve" x="50" y="55" width="180" height="40" rx="8" fill="#ea580c" stroke="#f97316" stroke-width="2"/>
      <text x="130" y="78" font-size="10" font-family="sans-serif" fill="#ffffff" font-weight="bold">PVC Plastic Insulation (Insulator)</text>

      <!-- Stripped Bare Copper Core extending right -->
      <rect x="220" y="65" width="80" height="20" rx="4" fill="#b45309" stroke="#f59e0b" stroke-width="2"/>
      <!-- Multi-strand lines -->
      <line x1="225" y1="70" x2="295" y2="70" stroke="#fbbf24" stroke-width="1.5"/>
      <line x1="225" y1="75" x2="295" y2="75" stroke="#fbbf24" stroke-width="1.5"/>
      <line x1="225" y1="80" x2="295" y2="80" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="260" y="98" font-size="9" font-family="sans-serif" fill="#f59e0b" font-weight="bold" text-anchor="middle">Bare Copper (Conductor)</text>

      <!-- Callouts -->
      <line x1="120" y1="40" x2="120" y2="53" stroke="#f97316" stroke-width="1.5"/>
      <text x="120" y="35" font-size="9" font-family="sans-serif" fill="#fdba74" text-anchor="middle">Touch Safe (No Shock!)</text>

      <line x1="260" y1="45" x2="260" y2="63" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="260" y="40" font-size="9" font-family="sans-serif" fill="#fcd34d" text-anchor="middle">Live Conductor (Shock Risk)</text>
    </svg>
  </div>

  <!-- Interactive Controls -->
  <div class="grid grid-cols-2 gap-2 text-xs">
    <button id="touchPvcBtn" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold transition flex items-center justify-center gap-1 cursor-pointer">
      <span>✋</span> <span>Touch PVC Sheath</span>
    </button>
    <button id="touchCopperBtn" class="px-3 py-2 rounded-xl bg-amber-700 hover:bg-amber-600 text-white font-bold transition flex items-center justify-center gap-1 cursor-pointer">
      <span>⚠️</span> <span>Touch Bare Copper</span>
    </button>
  </div>

  <div id="insulationInfoText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
    <strong class="text-cyan-400">Engineering Synergy:</strong> Copper provides ultra-low electrical resistance for seamless transmission; PVC jacket provides high dielectric strength to protect human lives and prevent fires.
  </div>
</div>
""",

    # Sim 15: Electrician Safety & Human Body Conduction
    "electrician_safety_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-rose-400 font-bold text-sm">⚡ Human Body & PPE Safety</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-rose-500/20 text-rose-300 font-mono">3.4 Safety</span>
    </div>
    <span id="resistanceBadge" class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-950 border border-slate-800 text-cyan-400">R = 100,000 Ω (Dry Skin)</span>
  </div>

  <!-- Safety Workbench Graphic -->
  <div class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2 relative">
    <svg viewBox="0 0 340 150" class="w-full h-full">
      <!-- Ground / Floor -->
      <line x1="20" y1="135" x2="320" y2="135" stroke="#475569" stroke-width="3"/>
      
      <!-- Electrician Figure -->
      <circle cx="170" cy="40" r="14" fill="#fed7aa" stroke="#fb923c"/>
      <line x1="170" y1="54" x2="170" y2="95" stroke="#3b82f6" stroke-width="4"/>
      
      <!-- Arms -->
      <line x1="170" y1="65" x2="120" y2="80" stroke="#3b82f6" stroke-width="3"/>
      <!-- Screwdriver with Rubber Grip in Hand -->
      <rect id="toolHandle" x="110" y="76" width="16" height="8" rx="2" fill="#ef4444" stroke="#f87171"/>
      <line x1="110" y1="80" x2="90" y2="80" stroke="#cbd5e1" stroke-width="2"/>

      <!-- Legs & Rubber Boots -->
      <line x1="170" y1="95" x2="155" y2="125" stroke="#1e3a8a" stroke-width="3"/>
      <line x1="170" y1="95" x2="185" y2="125" stroke="#1e3a8a" stroke-width="3"/>
      <rect id="bootLeft" x="145" y="125" width="18" height="10" rx="3" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
      <rect id="bootRight" x="177" y="125" width="18" height="10" rx="3" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>

      <!-- Live Electrical Terminal Board -->
      <rect x="50" y="65" width="35" height="40" rx="4" fill="#334155" stroke="#64748b"/>
      <circle cx="68" cy="80" r="6" fill="#f59e0b"/>
      <text x="68" y="100" font-size="8" fill="#f59e0b" text-anchor="middle" font-family="monospace">230V LIVE</text>
    </svg>
  </div>

  <!-- Interactive Controls -->
  <div class="grid grid-cols-2 gap-2 text-xs">
    <button id="toggleWetSkinBtn" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold transition flex items-center justify-center gap-1 cursor-pointer">
      <span>💧</span> <span id="skinMoistureLabel">Mode: Dry Skin</span>
    </button>
    <button id="togglePpeBootsBtn" class="px-3 py-2 rounded-xl bg-emerald-700 hover:bg-emerald-600 text-white font-bold transition flex items-center justify-center gap-1 cursor-pointer">
      <span>🥾</span> <span id="ppeLabel">Rubber Boots: ON</span>
    </button>
  </div>

  <div id="safetyHazardText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
    <strong class="text-emerald-400">Protected with Rubber Boots:</strong> Rubber has massive electrical resistance ($> 10^{12}\,Ω$). It breaks the circuit to the ground, preventing current from passing through the technician.
  </div>
</div>
""",

    # Sim 16: Heritage of Indian Electrical Science: Acharya J.C. Bose
    "jc_bose_heritage_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🇮🇳 Acharya J.C. Bose Historic Lab (1895)</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">Heritage</span>
    </div>
    <span id="bellStatusBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 font-bold">Bell Silent</span>
  </div>

  <!-- Kolkata Town Hall Demonstration Graphic -->
  <div class="w-full h-44 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2 relative overflow-hidden">
    <svg viewBox="0 0 360 150" class="w-full h-full">
      <!-- Solid Brick Wall in Center -->
      <rect x="160" y="10" width="40" height="130" fill="#78350f" stroke="#b45309" stroke-width="1.5"/>
      <text x="180" y="75" font-size="9" fill="#fde68a" text-anchor="middle" font-family="sans-serif" transform="rotate(-90, 180, 75)">Solid Brick Wall</text>

      <!-- J.C. Bose Microwave Spark Transmitter (Left Side) -->
      <rect x="30" y="45" width="60" height="60" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
      <path d="M 90,65 L 115,50 L 115,100 L 90,85 Z" fill="#334155" stroke="#38bdf8"/>
      <circle id="sparkPoint" cx="60" cy="75" r="4" fill="#38bdf8"/>
      <text x="60" y="40" font-size="9" fill="#38bdf8" text-anchor="middle" font-weight="bold">60 GHz Horn</text>

      <!-- Animated 5mm Microwave Arcs (Hidden initially) -->
      <g id="microwaveWaves" class="hidden">
        <path d="M 120,60 A 15,15 0 0,1 120,90" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <path d="M 135,50 A 30,30 0 0,1 135,100" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <path d="M 150,40 A 45,45 0 0,1 150,110" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <!-- Through wall -->
        <path d="M 210,40 A 45,45 0 0,1 210,110" fill="none" stroke="#a78bfa" stroke-width="2"/>
        <path d="M 230,50 A 30,30 0 0,1 230,100" fill="none" stroke="#a78bfa" stroke-width="2"/>
      </g>

      <!-- Galena Semiconductor Crystal Receiver (Right Side) -->
      <rect x="250" y="55" width="70" height="50" rx="4" fill="#1e293b" stroke="#a78bfa" stroke-width="1.5"/>
      <polygon points="265,70 275,65 275,75" fill="#a78bfa"/>
      <text x="285" y="80" font-size="9" fill="#a78bfa" text-anchor="middle" font-weight="bold">Galena Diode</text>

      <!-- Brass Electric Bell -->
      <circle id="heritageBell" cx="295" cy="35" r="12" fill="#ca8a04" stroke="#eab308" stroke-width="1.5"/>
      <line id="bellHammer" x1="280" y1="35" x2="285" y2="35" stroke="#e2e8f0" stroke-width="2"/>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2 text-xs">
    <button id="transmitSignalBtn" class="px-3 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold transition flex items-center justify-center gap-1 cursor-pointer">
      <span>📡</span> <span>Transmit 5mm Microwaves</span>
    </button>
    <button id="inspectGalenaBtn" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold transition flex items-center justify-center gap-1 cursor-pointer">
      <span>💎</span> <span>Galena Crystal (First Diode)</span>
    </button>
  </div>

  <div id="boseHeritageText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 leading-relaxed">
    <strong class="text-amber-400">Kolkata Town Hall (1895):</strong> Acharya J.C. Bose beamed 5mm electromagnetic waves through closed walls, detected by his galena crystal semiconductor diode to ring a bell wirelessly!
  </div>
</div>
"""
}

if __name__ == "__main__":
    with open(".agents/class7_science_circuits_sims.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Class 7 Science Chapter 3: Electricity: Circuits and their Components Simulators HTML"""\n\n')
        f.write("SIMULATORS_HTML = " + json.dumps(SIMULATORS_HTML, indent=2, ensure_ascii=False) + "\n")
    print("Generated .agents/class7_science_circuits_sims.py successfully.")

