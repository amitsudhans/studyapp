# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Science Chapter 5 Simulators HTML templates
Outputs .agents/class7_science_changes_sims.py
"""

import json

SIMULATORS_HTML = {
    # Sim 1: Physical Changes Explorer (Paper, Balloon, Chalk)
    "physical_changes_explorer_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">📐 Physical Changes Explorer</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">5.1 Shape & State</span>
    </div>
    <span id="physModeBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-bold">Paper Airplane</span>
  </div>

  <!-- SVG Workspace -->
  <div class="relative w-full h-48 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 180" class="w-full h-full">
      <!-- 1. Paper Mode View -->
      <g id="paperWorkspace" class="transition-all duration-300">
        <!-- Flat sheet (hidden when folded) -->
        <rect id="flatPaperSheet" x="140" y="30" width="160" height="110" rx="2" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" class="hidden"/>
        <!-- Folded Plane -->
        <g id="foldedPlane" transform="translate(170, 30)">
          <polygon points="0,90 50,0 100,90" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.5"/>
          <line x1="50" y1="0" x2="50" y2="90" stroke="#94a3b8" stroke-width="2"/>
          <polygon points="50,0 30,90 70,90" fill="#e2e8f0"/>
          <text x="50" y="115" fill="#94a3b8" font-size="9" text-anchor="middle">Paper Airplane</text>
        </g>
        <!-- Shredded paper pieces -->
        <g id="shreddedPaper" class="hidden">
          <polygon points="130,50 160,40 150,70" fill="#f8fafc" stroke="#94a3b8"/>
          <polygon points="175,60 210,50 195,85" fill="#f1f5f9" stroke="#94a3b8"/>
          <polygon points="230,45 260,65 240,80" fill="#e2e8f0" stroke="#94a3b8"/>
          <polygon points="275,55 310,45 295,75" fill="#f8fafc" stroke="#94a3b8"/>
          <text x="220" y="125" fill="#94a3b8" font-size="9" text-anchor="middle">Cut Paper Strips</text>
        </g>
      </g>

      <!-- 2. Balloon Mode View (hidden by default) -->
      <g id="balloonWorkspace" class="hidden transition-all duration-300" transform="translate(160, 20)">
        <!-- Inflated Balloon -->
        <g id="inflatedBalloon">
          <ellipse id="balloonOval" cx="60" cy="65" rx="45" ry="55" fill="#ef4444" stroke="#dc2626" stroke-width="2"/>
          <polygon points="55,120 65,120 60,128" fill="#b91c1c"/>
          <path d="M 60,128 Q 65,145 55,155" fill="none" stroke="#f8fafc" stroke-width="1.5"/>
          <!-- Highlight -->
          <ellipse cx="45" cy="45" rx="10" ry="16" fill="#fca5a5" opacity="0.6"/>
        </g>
        <!-- Popped Balloon Pieces -->
        <g id="poppedBalloon" class="hidden">
          <path d="M 30,60 Q 50,40 40,80 Q 20,70 30,60 Z" fill="#ef4444"/>
          <path d="M 80,60 Q 95,45 90,75 Q 70,85 80,60 Z" fill="#ef4444"/>
          <text x="60" y="100" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">POPPED! Still Latex</text>
        </g>
      </g>

      <!-- 3. Chalk Mode View (hidden by default) -->
      <g id="chalkWorkspace" class="hidden transition-all duration-300" transform="translate(150, 40)">
        <!-- Solid Chalk Stick -->
        <g id="solidChalk">
          <rect x="20" y="30" width="100" height="25" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
          <ellipse cx="20" cy="42" rx="4" ry="12" fill="#e2e8f0"/>
          <text x="70" y="80" fill="#94a3b8" font-size="9" text-anchor="middle">Solid Chalk Stick (CaCO₃)</text>
        </g>
        <!-- Crushed Chalk Powder -->
        <g id="crushedChalk" class="hidden">
          <ellipse cx="70" cy="55" rx="45" ry="15" fill="#f8fafc" stroke="#cbd5e1"/>
          <circle cx="50" cy="52" r="2" fill="#cbd5e1"/>
          <circle cx="75" cy="50" r="2" fill="#cbd5e1"/>
          <circle cx="90" cy="54" r="1.5" fill="#94a3b8"/>
          <text x="70" y="85" fill="#94a3b8" font-size="9" text-anchor="middle">Powdered Chalk (Still CaCO₃)</text>
        </g>
      </g>
    </svg>
  </div>

  <!-- Mode Selector Buttons -->
  <div class="grid grid-cols-3 gap-2">
    <button class="phys-obj-btn p-2 rounded-xl bg-amber-600 text-white font-bold text-xs" data-mode="paper">📄 Paper Sheet</button>
    <button class="phys-obj-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs" data-mode="balloon">🎈 Rubber Balloon</button>
    <button class="phys-obj-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs" data-mode="chalk">🖍️ Chalk Stick</button>
  </div>

  <!-- Interactive Action Buttons -->
  <div class="flex space-x-2">
    <button id="btnTransformPhys" class="flex-1 py-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>✨ Alter Physical Form</span>
    </button>
    <button id="btnResetPhys" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs border border-slate-700 transition">
      Reset
    </button>
  </div>

  <div id="physExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    📐 <span class="font-bold text-amber-300">Physical Principle:</span> Folding paper into an airplane or cutting it into strips changes shape and size, but the cellulose molecules remain 100% paper!
  </div>
</div>
""",

    # Sim 2: State Transformations of Matter (Ice, Water, Steam, Condensation)
    "state_transformations_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">💧 Phase Transitions & Condensation Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">5.1 Phase Change</span>
    </div>
    <span id="waterPhaseBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-mono font-bold">Solid Ice (0°C)</span>
  </div>

  <!-- Beaker & Burner SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Bunsen Burner -->
      <g transform="translate(195, 130)">
        <rect x="15" y="30" width="20" height="25" fill="#475569"/>
        <rect x="5" y="52" width="40" height="8" rx="2" fill="#334155"/>
        <!-- Flame -->
        <path id="phaseFlame" d="M 25,30 Q 15,10 25,-5 Q 35,10 25,30 Z" fill="#38bdf8" class="opacity-0 transition-opacity duration-300"/>
      </g>

      <!-- Tripod Stand -->
      <line x1="160" y1="130" x2="280" y2="130" stroke="#64748b" stroke-width="4"/>
      <line x1="170" y1="130" x2="155" y2="175" stroke="#475569" stroke-width="3"/>
      <line x1="270" y1="130" x2="285" y2="175" stroke="#475569" stroke-width="3"/>

      <!-- Glass Beaker -->
      <g transform="translate(180, 45)">
        <rect x="0" y="0" width="80" height="85" rx="4" fill="#0f172a" fill-opacity="0.3" stroke="#94a3b8" stroke-width="2"/>
        <!-- Liquid Water Level -->
        <rect id="liquidWater" x="3" y="45" width="74" height="38" rx="2" fill="#0284c7" fill-opacity="0.4" class="opacity-0 transition-all duration-500"/>
        
        <!-- Ice Cubes inside Beaker -->
        <g id="iceCubesGroup" class="transition-all duration-500">
          <rect x="15" y="50" width="18" height="18" rx="2" fill="#bae6fd" stroke="#7dd3fc" stroke-width="1.5"/>
          <rect x="42" y="48" width="20" height="20" rx="2" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="1.5"/>
          <rect x="30" y="62" width="16" height="16" rx="2" fill="#bae6fd" stroke="#7dd3fc" stroke-width="1.5"/>
        </g>

        <!-- Rising Steam / Water Vapor -->
        <g id="steamFumes" class="opacity-0 transition-opacity duration-500">
          <path d="M 25,30 Q 15,15 25,0" fill="none" stroke="#f8fafc" stroke-width="2" opacity="0.6"/>
          <path d="M 40,25 Q 50,10 40,-5" fill="none" stroke="#f8fafc" stroke-width="2.5" opacity="0.7"/>
          <path d="M 55,30 Q 65,15 55,0" fill="none" stroke="#f8fafc" stroke-width="2" opacity="0.6"/>
        </g>
      </g>

      <!-- Cold Condensation Pan / Lid with Droplets (Above Beaker) -->
      <g id="condensationPan" transform="translate(160, 15)">
        <rect x="0" y="0" width="120" height="12" rx="3" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
        <text x="60" y="-3" fill="#94a3b8" font-size="8" text-anchor="middle">Cold Metal Lid (Ice on top)</text>
        <!-- Condensing Droplets falling -->
        <g id="condensedDrops" class="opacity-0 transition-opacity duration-300">
          <circle cx="45" cy="18" r="2.5" fill="#38bdf8"/>
          <circle cx="75" cy="22" r="3" fill="#38bdf8"/>
          <circle cx="60" cy="28" r="2.5" fill="#38bdf8"/>
        </g>
      </g>
    </svg>
  </div>

  <!-- Heat / Cool Controls -->
  <div class="grid grid-cols-3 gap-2">
    <button id="btnHeatWater" class="p-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>🔥 Heat (Melt & Boil)</span>
    </button>
    <button id="btnCondenseSteam" class="p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>❄️ Apply Cold Lid</span>
    </button>
    <button id="btnResetPhase" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs border border-slate-700 transition">
      ↺ Reset Ice
    </button>
  </div>

  <div id="phaseExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    💧 <span class="font-bold text-amber-300">Reversible Cycle:</span> Solid Ice (0°C) ⇌ Liquid Water ⇌ Gaseous Steam (100°C). Every molecule remains H₂O throughout all phase transitions!
  </div>
</div>
""",

    # Sim 3: Chemical Changes Lab: Vinegar + Baking Soda
    "vinegar_baking_soda_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🧪 Vinegar & Baking Soda Reaction Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">5.2 Effervescence</span>
    </div>
    <span id="reactionStatusBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 font-bold">Unmixed</span>
  </div>

  <!-- Conical Flask & Balloon SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Conical Flask (Erlenmeyer) -->
      <g transform="translate(180, 40)">
        <!-- Flask Neck & Body -->
        <path d="M 25,20 L 25,50 L 0,110 Q -5,125 15,125 L 65,125 Q 85,125 80,110 L 55,50 L 55,20 Z" fill="#0f172a" fill-opacity="0.3" stroke="#64748b" stroke-width="2"/>
        
        <!-- Vinegar Liquid at Bottom -->
        <path id="vinegarLiquid" d="M 5,100 L 0,110 Q -5,125 15,125 L 65,125 Q 85,125 80,110 L 75,100 Z" fill="#fef08a" fill-opacity="0.3"/>

        <!-- Baking Soda Powder Pile -->
        <ellipse id="bakingSodaPile" cx="40" cy="120" rx="18" ry="4" fill="#f8fafc" class="hidden"/>

        <!-- Effervescent Bubbles (CO2 generation) -->
        <g id="bubbleGroup" class="hidden">
          <circle cx="20" cy="110" r="3" fill="#f8fafc" opacity="0.8" class="animate-bounce"/>
          <circle cx="35" cy="100" r="4" fill="#f8fafc" opacity="0.8"/>
          <circle cx="50" cy="105" r="2.5" fill="#f8fafc" opacity="0.8"/>
          <circle cx="40" cy="85" r="3.5" fill="#f8fafc" opacity="0.8"/>
          <circle cx="30" cy="70" r="3" fill="#f8fafc" opacity="0.8"/>
          <circle cx="48" cy="65" r="2" fill="#f8fafc" opacity="0.8"/>
        </g>

        <!-- Rubber Balloon Attached to Flask Neck -->
        <!-- Deflated Balloon -->
        <path id="deflatedBalloon" d="M 25,20 Q 15,5 30,-5 Q 40,-12 50,-5 Q 65,5 55,20 Z" fill="#3b82f6" stroke="#2563eb" stroke-width="1.5"/>
        <!-- Inflated Balloon (shown when CO2 fills it) -->
        <g id="inflatedBalloonCO2" class="hidden">
          <ellipse cx="40" cy="-25" rx="35" ry="40" fill="#3b82f6" stroke="#2563eb" stroke-width="2"/>
          <text x="40" y="-22" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">CO₂ Gas</text>
        </g>
      </g>

      <!-- Spatula Holding Baking Soda (Right) -->
      <g id="spatulaTool" transform="translate(290, 45)" class="cursor-pointer transition-transform duration-500">
        <line x1="0" y1="20" x2="60" y2="0" stroke="#94a3b8" stroke-width="3"/>
        <path d="M 0,15 Q -10,20 0,25 Q 10,20 0,15 Z" fill="#cbd5e1"/>
        <ellipse cx="-2" cy="19" rx="5" ry="3" fill="#f8fafc"/>
        <text x="30" y="32" fill="#94a3b8" font-size="8">Spatula (NaHCO₃)</text>
      </g>
    </svg>
  </div>

  <div class="flex space-x-2">
    <button id="btnAddBakingSoda" class="flex-1 py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>🥄 Add Baking Soda to Vinegar</span>
    </button>
    <button id="btnResetReaction" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs border border-slate-700 transition">
      Reset
    </button>
  </div>

  <div id="vinegarReactionFormula" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 font-mono">
    CH₃COOH (Vinegar) + NaHCO₃ (Baking Soda) ➔ CH₃COONa + H₂O + CO₂↑ (Inflates Balloon!)
  </div>
</div>
""",

    # Sim 4: Lime Water Testing Lab (Exhaling CO2 & Milky CaCO3)
    "lime_water_test_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🥛 Lime Water & CO₂ Diagnostic Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">5.2 Carbon Dioxide</span>
    </div>
    <span id="limeWaterClarityBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold">Clear Ca(OH)₂</span>
  </div>

  <!-- Boiling Tube with Straw SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Test Tube Rack -->
      <rect x="140" y="160" width="160" height="15" rx="3" fill="#334155" stroke="#475569"/>

      <!-- Boiling Test Tube -->
      <g transform="translate(195, 20)">
        <rect x="0" y="0" width="50" height="145" rx="8" fill="#0f172a" fill-opacity="0.3" stroke="#64748b" stroke-width="2"/>
        <!-- Solution Volume -->
        <rect id="limeLiquidBody" x="2" y="65" width="46" height="76" rx="6" fill="#38bdf8" fill-opacity="0.2" class="transition-all duration-700"/>

        <!-- Straw inserted into tube -->
        <g id="blowingStraw" transform="translate(20, -10)">
          <line x1="0" y1="0" x2="0" y2="135" stroke="#f43f5e" stroke-width="4"/>
          <!-- Exhaled breath bubbles -->
          <g id="breathBubbles" class="hidden">
            <circle cx="-5" cy="120" r="3" fill="#ffffff" class="animate-ping"/>
            <circle cx="5" cy="105" r="2.5" fill="#ffffff"/>
            <circle cx="-3" cy="90" r="3.5" fill="#ffffff"/>
          </g>
        </g>
      </g>

      <!-- Annotation Callout Left -->
      <g transform="translate(50, 60)">
        <text x="60" y="0" fill="#facc15" font-size="11" font-weight="bold" text-anchor="middle">Exhaled Breath (CO₂)</text>
        <text x="60" y="15" fill="#94a3b8" font-size="8" text-anchor="middle">Cellular Respiration Product</text>
        <path d="M 120,5 Q 160,5 190,15" fill="none" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3 2"/>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2">
    <button id="btnBlowBreath" class="p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>🌬️ Exhale CO₂ through Straw (10s)</span>
    </button>
    <button id="btnExcessCO2" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 font-bold text-xs transition border border-slate-700">
      <span>🫧 Blow Excess CO₂ (Dissolves)</span>
    </button>
  </div>

  <div id="limeReactionFormula" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 font-mono">
    Ca(OH)₂ (Lime Water) + CO₂ ➔ CaCO₃↓ (Milky White Precipitate) + H₂O
  </div>
</div>
""",

    # Sim 5: Rusting Chemical Change (Mass Increase & Magnetism Test)
    "rusting_chemical_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🔩 Rusting of Iron: Chemical Oxidation Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">5.3.1 Rusting</span>
    </div>
    <span id="rustMassBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-400 font-mono font-bold">Mass: 10.00 g (Shiny Fe)</span>
  </div>

  <!-- Rusting Lab Chamber SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Digital Precision Scale Platform -->
      <rect x="130" y="145" width="180" height="25" rx="4" fill="#1e293b" stroke="#475569"/>
      <rect x="160" y="152" width="120" height="12" rx="2" fill="#020617"/>
      <text id="digitalScaleReadout" x="220" y="161" fill="#22c55e" font-size="10" font-family="monospace" text-anchor="middle">10.00 g</text>

      <!-- Glass Moisture Bell Jar -->
      <path d="M 145,145 L 145,45 Q 220,15 295,45 L 295,145 Z" fill="#0f172a" fill-opacity="0.3" stroke="#64748b" stroke-width="1.5"/>

      <!-- Iron Nail on Scale Pan -->
      <g id="ironNailAssembly" transform="translate(180, 110)">
        <!-- Shiny Base Nail -->
        <rect id="baseShinyNail" x="0" y="10" width="80" height="14" rx="2" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.5"/>
        <!-- Nail Head -->
        <rect x="-6" y="6" width="8" height="22" rx="1" fill="#94a3b8"/>
        <!-- Flaky Rust Crust Overlay -->
        <rect id="rustFlakesOverlay" x="0" y="8" width="80" height="18" rx="3" fill="#b45309" class="opacity-0 transition-opacity duration-700"/>
      </g>

      <!-- Handheld Bar Magnet Tool (Right) -->
      <g id="magnetTool" transform="translate(340, 60)" class="cursor-pointer transition-transform duration-300">
        <rect x="0" y="0" width="20" height="25" fill="#ef4444"/>
        <text x="10" y="17" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">N</text>
        <rect x="0" y="25" width="20" height="25" fill="#3b82f6"/>
        <text x="10" y="42" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">S</text>
        <text x="10" y="62" fill="#94a3b8" font-size="8" text-anchor="middle">Magnet</text>
      </g>
    </svg>
  </div>

  <div class="flex items-center space-x-3">
    <span class="text-xs text-slate-400 font-mono">Expose to Moist Air:</span>
    <input id="rustExposureSlider" type="range" min="0" max="10" value="0" class="flex-1 accent-amber-500 cursor-pointer"/>
    <button id="btnTestMagnet" class="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition">
      🧲 Test Magnetism
    </button>
  </div>

  <div id="rustExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 font-mono">
    4Fe (Iron) + 3O₂ + 2xH₂O ➔ 2Fe₂O₃·xH₂O (Mass increases as O₂ & H₂O atoms bond!)
  </div>
</div>
""",

    # Sim 6: Combustion Reactions Lab (Magnesium Ribbon & Candle Flame)
    "combustion_reactions_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🔥 Combustion & Oxide Formation Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">5.3.2 Combustion</span>
    </div>
    <span id="combustionStatusBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 font-bold">Unignited</span>
  </div>

  <!-- Combustion Chamber SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <defs>
        <radialGradient id="mgBlindingBurst" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#ffffff"/>
          <stop offset="40%" stop-color="#fef08a" stop-opacity="0.9"/>
          <stop offset="80%" stop-color="#38bdf8" stop-opacity="0.4"/>
          <stop offset="100%" stop-color="#0284c7" stop-opacity="0"/>
        </radialGradient>
      </defs>

      <!-- Bunsen Burner on Left -->
      <g transform="translate(60, 90)">
        <rect x="20" y="45" width="20" height="35" fill="#475569"/>
        <rect x="10" y="75" width="40" height="12" rx="3" fill="#334155"/>
        <path id="combustionBurnerFlame" d="M 30,45 Q 20,20 30,0 Q 40,20 30,45 Z" fill="#38bdf8"/>
      </g>

      <!-- Tongs Holding Magnesium Ribbon -->
      <g id="combustionTongs" transform="translate(100, 35)">
        <line x1="160" y1="20" x2="30" y2="55" stroke="#94a3b8" stroke-width="4"/>
        <line x1="160" y1="35" x2="30" y2="59" stroke="#94a3b8" stroke-width="4"/>
        <!-- Magnesium Ribbon -->
        <rect id="combustionMgRibbon" x="0" y="52" width="35" height="6" rx="1" fill="#e2e8f0" stroke="#cbd5e1"/>
      </g>

      <!-- Blinding White Flare Flare Burst -->
      <circle id="mgFlareBurst" cx="105" cy="90" r="65" fill="url(#mgBlindingBurst)" class="hidden animate-pulse"/>

      <!-- Watch Glass for Collecting Ash (Right) -->
      <g transform="translate(260, 120)">
        <path d="M 10,25 Q 40,40 70,25 Q 40,15 10,25 Z" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
        <ellipse id="mgWhiteAsh" cx="40" cy="27" rx="14" ry="5" fill="#f8fafc" class="hidden"/>
        <text x="40" y="48" fill="#94a3b8" font-size="8" text-anchor="middle">White Ash (MgO)</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2">
    <button id="btnIgniteRibbon" class="p-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>🔥 Ignite Magnesium in Flame</span>
    </button>
    <button id="btnDissolveAshMgO" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-cyan-300 font-bold text-xs transition border border-slate-700" disabled>
      <span>🧪 Dissolve Ash in Water (Litmus)</span>
    </button>
  </div>

  <div id="combustionReactionText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 font-mono">
    2Mg + O₂ ➔ 2MgO (Dazzling white light!) | MgO + H₂O ➔ Mg(OH)₂ (Basic: Red litmus turns BLUE)
  </div>
</div>
""",

    # Sim 7: The Fire Triangle & Extinguishing Principles
    "fire_triangle_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🔺 The Fire Triangle & Extinguishment</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">5.3.2 Fire Science</span>
    </div>
    <span id="fireStatusBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-300 font-bold animate-pulse">FLAME BURNING</span>
  </div>

  <!-- Interactive Fire Triangle SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Triangle Perimeter Lines -->
      <line id="edgeFuel" x1="220" y1="30" x2="130" y2="150" stroke="#f59e0b" stroke-width="5" class="transition-all duration-300"/>
      <line id="edgeOxygen" x1="220" y1="30" x2="310" y2="150" stroke="#38bdf8" stroke-width="5" class="transition-all duration-300"/>
      <line id="edgeHeat" x1="130" y1="150" x2="310" y2="150" stroke="#ef4444" stroke-width="5" class="transition-all duration-300"/>

      <!-- Central Sustained Flame -->
      <g id="centerFlame" transform="translate(220, 110)">
        <path d="M 0,-35 Q -20,-10 0,15 Q 20,-10 0,-35 Z" fill="#f97316"/>
        <path d="M 0,-20 Q -10,0 0,15 Q 10,0 0,-20 Z" fill="#fde047"/>
      </g>
      <!-- Smoke plume when extinguished -->
      <g id="extinguishedSmoke" class="hidden">
        <path d="M 220,110 Q 210,80 225,50" fill="none" stroke="#64748b" stroke-width="3" opacity="0.6"/>
        <text x="220" y="115" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">EXTINGUISHED</text>
      </g>

      <!-- Vertex Labels -->
      <!-- Top: Fuel -->
      <circle cx="220" cy="30" r="14" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
      <text x="220" y="34" fill="#f59e0b" font-size="9" font-weight="bold" text-anchor="middle">FUEL</text>

      <!-- Bottom-Left: Oxygen -->
      <circle cx="130" cy="150" r="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
      <text x="130" y="154" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">O₂</text>

      <!-- Bottom-Right: Heat -->
      <circle cx="310" cy="150" r="14" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
      <text x="310" y="154" fill="#ef4444" font-size="9" font-weight="bold" text-anchor="middle">HEAT</text>
    </svg>
  </div>

  <!-- Toggle Buttons for Removing Components -->
  <div class="grid grid-cols-3 gap-2">
    <button id="btnCutOxygen" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-cyan-300 font-bold text-xs transition border border-slate-700">
      <span>💨 Smother O₂ (Blanket)</span>
    </button>
    <button id="btnCoolHeat" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-rose-300 font-bold text-xs transition border border-slate-700">
      <span>💧 Spray Water (Cool)</span>
    </button>
    <button id="btnRemoveFuel" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 font-bold text-xs transition border border-slate-700">
      <span>🪵 Cut Fuel Source</span>
    </button>
  </div>

  <div id="fireTriangleExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🔺 <span class="font-bold text-amber-300">Firefighting Science:</span> A fire cannot survive if any one of the three components is removed. Break any link to extinguish the flame!
  </div>
</div>
""",

    # Sim 8: Dual Changes: Physical & Chemical in a Burning Candle
    "candle_dual_changes_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🕯️ Candle Anatomy: Physical vs Chemical</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">5.4 Dual Changes</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-400 font-bold">Interactive Cross-Section</span>
  </div>

  <!-- Burning Candle Cross Section SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Candle Cylinder Pillar -->
      <g transform="translate(180, 80)">
        <rect x="0" y="0" width="80" height="90" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
        <!-- Melted Liquid Wax Pool at Top -->
        <ellipse cx="40" cy="5" rx="35" ry="8" fill="#fef08a" opacity="0.8"/>
        <!-- Molten wax dribbling down flank -->
        <path d="M 75,5 Q 78,25 74,40 Q 72,55 76,70" fill="none" stroke="#fef08a" stroke-width="3"/>
        
        <!-- Braided Cotton Wick -->
        <line x1="40" y1="5" x2="40" y2="-20" stroke="#475569" stroke-width="3"/>
      </g>

      <!-- Flame Architecture -->
      <g id="candleFlameGroup" transform="translate(220, 50)">
        <!-- Outer Luminous Yellow Zone -->
        <path d="M 0,-45 Q -18,-15 0,10 Q 18,-15 0,-45 Z" fill="#f59e0b" opacity="0.9"/>
        <!-- Middle Blue Outer Edge -->
        <path d="M -8,5 Q 0,12 8,5 Q 12,0 8,-10 Q -8,-10 -8,5 Z" fill="#38bdf8" opacity="0.7"/>
        <!-- Inner Dark Non-Combustion Zone (Wax Vapor) -->
        <ellipse cx="0" cy="0" rx="6" ry="10" fill="#1e293b" opacity="0.8"/>
      </g>

      <!-- Annotation Left: Physical Changes -->
      <g transform="translate(30, 80)">
        <rect x="0" y="0" width="130" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="65" y="16" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Physical Changes</text>
        <text x="10" y="32" fill="#cbd5e1" font-size="8">• Wax melting (solid ➔ liquid)</text>
        <text x="10" y="45" fill="#cbd5e1" font-size="8">• Wax vaporization into gas</text>
      </g>

      <!-- Annotation Right: Chemical Change -->
      <g transform="translate(280, 80)">
        <rect x="0" y="0" width="135" height="55" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="67" y="16" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">Chemical Change</text>
        <text x="10" y="32" fill="#cbd5e1" font-size="8">• Vapor + O₂ combustion</text>
        <text x="10" y="45" fill="#cbd5e1" font-size="8">• Yields CO₂ + H₂O + Light</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2">
    <button id="btnFocusPhysicalCandle" class="p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow">
      💧 Highlight Physical Changes (Wax)
    </button>
    <button id="btnFocusChemicalCandle" class="p-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition shadow">
      🔥 Highlight Chemical Change (Flame)
    </button>
  </div>

  <div id="candleInsightText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🕯️ <span class="font-bold text-amber-300">Dual Symphony:</span> Melting and vaporization of wax are reversible physical changes; combustion of wax vapor into carbon dioxide and water is an irreversible chemical change!
  </div>
</div>
""",

    # Sim 9: Permanence & Reversibility Classifier
    "reversibility_classifier_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">⚖️ Reversible vs Irreversible Classifier</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">5.5 Permanence</span>
    </div>
    <span id="reversibilityScoreBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold">Tested: 0 / 6</span>
  </div>

  <!-- Interactive Sorting Board -->
  <div class="grid grid-cols-2 gap-3 bg-slate-950 p-3 rounded-xl border border-slate-800 min-h-44 text-xs">
    <!-- Reversible Tray -->
    <div id="trayReversible" class="p-2 rounded-lg bg-emerald-950/30 border border-emerald-500/40 flex flex-col space-y-1.5">
      <div class="font-bold text-emerald-400 text-center pb-1 border-b border-emerald-500/20">🔄 Reversible Changes</div>
      <div id="listReversible" class="space-y-1 flex-1"></div>
    </div>
    <!-- Irreversible Tray -->
    <div id="trayIrreversible" class="p-2 rounded-lg bg-rose-950/30 border border-rose-500/40 flex flex-col space-y-1.5">
      <div class="font-bold text-rose-400 text-center pb-1 border-b border-rose-500/20">⛔ Irreversible Changes</div>
      <div id="listIrreversible" class="space-y-1 flex-1"></div>
    </div>
  </div>

  <!-- Item to Classify -->
  <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-between">
    <span id="currentSampleName" class="text-xs font-bold text-amber-300">Melting Ice into Water</span>
    <div class="flex space-x-2">
      <button class="btn-classify px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs" data-choice="reversible">
        Reversible
      </button>
      <button class="btn-classify px-3 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs" data-choice="irreversible">
        Irreversible
      </button>
    </div>
  </div>

  <div id="classifierFeedback" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    💡 Classify everyday changes based on whether reversing experimental conditions restores original substances!
  </div>
</div>
""",

    # Sim 10: Desirable vs Undesirable Changes Matrix
    "desirable_undesirable_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🍎 Desirable vs Undesirable Transformations</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">5.6 Human Impact</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 font-bold">Societal Evaluation</span>
  </div>

  <!-- Interactive Comparison Table -->
  <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-950 max-h-52">
    <table class="w-full text-left text-xs border-collapse">
      <thead>
        <tr class="bg-slate-900 border-b border-slate-800 text-slate-300">
          <th class="p-2.5 font-bold">Category</th>
          <th class="p-2.5 font-bold text-emerald-400">Desirable (Beneficial)</th>
          <th class="p-2.5 font-bold text-rose-400">Undesirable (Harmful)</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-800/60 font-sans text-slate-300">
        <tr class="hover:bg-slate-900/40">
          <td class="p-2 font-medium">1. Food & Cooking</td>
          <td class="p-2 text-emerald-300">Milk ➔ Curd (Lactobacillus); Baking bread</td>
          <td class="p-2 text-rose-300">Milk souring/rotting; Bread mold decay</td>
        </tr>
        <tr class="hover:bg-slate-900/40">
          <td class="p-2 font-medium">2. Agriculture & Botany</td>
          <td class="p-2 text-emerald-300">Fruit ripening; Seed germination</td>
          <td class="p-2 text-rose-300">Crop rotting in floods; Weed invasion</td>
        </tr>
        <tr class="hover:bg-slate-900/40">
          <td class="p-2 font-medium">3. Metals & Tools</td>
          <td class="p-2 text-emerald-300">Forging iron into blades; Alloying bronze</td>
          <td class="p-2 text-rose-300">Rusting of iron bridges & vehicle chassis</td>
        </tr>
        <tr class="hover:bg-slate-900/40">
          <td class="p-2 font-medium">4. Environment</td>
          <td class="p-2 text-emerald-300">Fallen leaf composting into rich humus</td>
          <td class="p-2 text-rose-300">Combustion emissions forming toxic smog & acid rain</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="grid grid-cols-4 gap-1.5 text-xs">
    <button class="impact-btn p-2 rounded-xl bg-amber-600 text-white font-bold" data-item="curd">🥛 Milk to Curd</button>
    <button class="impact-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-item="rust">🔩 Bridge Rusting</button>
    <button class="impact-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-item="fruit">🥭 Fruit Ripening</button>
    <button class="impact-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-item="smog">🏭 Vehicle Smog</button>
  </div>

  <div id="impactExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    ✨ <span class="font-bold text-amber-300">Milk to Curd:</span> Probiotic lactic acid bacteria convert lactose sugar into lactic acid, coagulating proteins into nutritious, easily digestible curd!
  </div>
</div>
""",

    # Sim 11: Physical Weathering of Rocks (Thermal Stress & Frost Wedging)
    "physical_weathering_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🪨 Physical Weathering: Frost Wedging Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">5.7.1 Mechanical</span>
    </div>
    <span id="weatheringStateBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-bold">Intact Granite</span>
  </div>

  <!-- Rock Fracture SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Ground Bedrock Base -->
      <rect x="80" y="150" width="280" height="25" rx="3" fill="#334155" stroke="#475569"/>

      <!-- Massive Granite Boulder (Left Half) -->
      <path id="boulderHalfLeft" d="M 120,150 L 140,60 Q 180,40 215,45 L 215,150 Z" fill="#64748b" stroke="#475569" stroke-width="2" class="transition-transform duration-500"/>
      <!-- Massive Granite Boulder (Right Half) -->
      <path id="boulderHalfRight" d="M 225,45 Q 260,40 300,60 L 320,150 L 225,150 Z" fill="#64748b" stroke="#475569" stroke-width="2" class="transition-transform duration-500"/>

      <!-- Fissure Crack Gap -->
      <g id="fissureGap" transform="translate(215, 45)">
        <!-- Seeping Water (Liquid Phase) -->
        <rect id="seepingWater" x="0" y="0" width="10" height="105" fill="#38bdf8" fill-opacity="0.6" class="hidden"/>
        <!-- Freezing Expanding Ice (+9% Volume Wedge) -->
        <g id="frostWedgeIce" class="hidden">
          <rect x="-3" y="0" width="16" height="105" rx="2" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.5"/>
          <text x="5" y="55" fill="#0284c7" font-size="8" font-weight="bold" text-anchor="middle" transform="rotate(-90 5 55)">ICE (+9% VOL)</text>
        </g>
      </g>

      <!-- Thermal Sun / Freezing Snow Icons -->
      <g id="weatherEffect" class="opacity-0 transition-opacity duration-300">
        <circle cx="60" cy="40" r="15" fill="#f59e0b"/>
        <text x="60" y="65" fill="#f59e0b" font-size="8" text-anchor="middle">Heat</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-3 gap-2">
    <button id="btnRainInfiltrate" class="p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>🌧️ 1. Rain Seeps in</span>
    </button>
    <button id="btnFreezeWater" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-cyan-300 font-bold text-xs transition border border-slate-700" disabled>
      <span>❄️ 2. Freeze to Ice (-5°C)</span>
    </button>
    <button id="btnThermalCycle" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 font-bold text-xs transition border border-slate-700">
      <span>☀️ Day/Night Heat Stress</span>
    </button>
  </div>

  <div id="weatheringExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🪨 <span class="font-bold text-amber-300">Frost Wedging:</span> Water expands by approximately 9% upon freezing. Trapped inside rock fissures, crystalline ice generates hundreds of atmospheres of outward force, splitting bedrock!
  </div>
</div>
""",

    # Sim 12: Chemical Weathering of Rocks (Oxidation & Carbonic Acid Caves)
    "chemical_weathering_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🏛️ Chemical Weathering: Caves & Oxidation</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">5.7.1 Chemical</span>
    </div>
    <span id="chemWeatheringBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 font-bold">Limestone Bedrock</span>
  </div>

  <!-- Chemical Weathering SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Limestone Cliff Surface -->
      <g id="limestoneCliff">
        <path d="M 40,30 L 400,30 L 400,165 L 40,165 Z" fill="#475569" stroke="#334155" stroke-width="2"/>
        <!-- Carbonic Acid Rain Infiltration -->
        <g id="acidRaindrops" class="opacity-60">
          <line x1="120" y1="10" x2="120" y2="28" stroke="#38bdf8" stroke-width="1.5"/>
          <line x1="220" y1="10" x2="220" y2="28" stroke="#38bdf8" stroke-width="1.5"/>
          <line x1="320" y1="10" x2="320" y2="28" stroke="#38bdf8" stroke-width="1.5"/>
        </g>
        <!-- Carved Subterranean Cave Hollow (Formed by Acid) -->
        <path id="caveHollow" d="M 120,165 Q 150,70 220,70 Q 290,70 320,165 Z" fill="#020617" class="opacity-0 transition-opacity duration-700"/>

        <!-- Stalactites hanging from ceiling -->
        <g id="stalactites" class="opacity-0 transition-opacity duration-700">
          <polygon points="180,72 186,105 192,72" fill="#cbd5e1"/>
          <polygon points="215,70 220,120 225,70" fill="#f8fafc"/>
          <polygon points="250,73 255,100 260,73" fill="#cbd5e1"/>
        </g>

        <!-- Red Iron Oxide Soil Horizon (when oxidation mode selected) -->
        <rect id="redOxideStain" x="40" y="30" width="360" height="25" fill="#ea580c" class="opacity-0 transition-opacity duration-700"/>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2">
    <button id="btnCarbonicAcidCave" class="p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow">
      💧 Carbonic Acid (H₂CO₃ Caves)
    </button>
    <button id="btnOxidiseIronRock" class="p-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition shadow">
      🪨 Iron Oxidation (Red Sediment)
    </button>
  </div>

  <div id="chemWeatheringFormula" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 font-mono">
    CaCO₃ (Limestone) + H₂CO₃ (Acid Rain) ➔ Ca(HCO₃)₂ (Soluble, Carves Giant Caves!)
  </div>
</div>
""",

    # Sim 13: Soil Genesis & Erosion Dynamics
    "soil_erosion_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🏞️ Soil Horizons & Erosion Dynamics</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">5.7.2 Erosion</span>
    </div>
    <span id="vegetationStatusBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-rose-400 font-bold">Bare Slope (Deforested)</span>
  </div>

  <!-- Hillside Slope SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Hillside Profile -->
      <path d="M 30,165 L 410,165 L 410,50 Q 250,90 30,165 Z" fill="#78350f" stroke="#451a03"/>
      
      <!-- Topsoil Layer (Vulnerable to erosion) -->
      <path id="topsoilLayer" d="M 30,165 L 410,165 L 410,50 Q 250,85 30,158 Z" fill="#451a03"/>

      <!-- Trees & Vegetation Roots (Hidden in bare mode) -->
      <g id="plantedVegetation" class="hidden">
        <!-- Tree 1 -->
        <g transform="translate(140, 105)">
          <rect x="0" y="0" width="8" height="20" fill="#78350f"/>
          <circle cx="4" cy="-10" r="16" fill="#15803d"/>
        </g>
        <!-- Tree 2 -->
        <g transform="translate(240, 75)">
          <rect x="0" y="0" width="8" height="22" fill="#78350f"/>
          <circle cx="4" cy="-12" r="18" fill="#16a34a"/>
        </g>
        <!-- Tree 3 -->
        <g transform="translate(330, 48)">
          <rect x="0" y="0" width="8" height="20" fill="#78350f"/>
          <circle cx="4" cy="-10" r="15" fill="#15803d"/>
        </g>
      </g>

      <!-- Torrential Rain Runoff Flow -->
      <g id="muddyRunoff" class="opacity-0 transition-opacity duration-300">
        <path d="M 380,65 Q 260,110 50,170" fill="none" stroke="#ca8a04" stroke-width="6" stroke-linecap="round"/>
        <text x="120" y="150" fill="#eab308" font-size="9" font-weight="bold">Muddy Runoff (Topsoil Lost)</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2">
    <button id="btnPlantForest" class="p-2.5 rounded-xl bg-emerald-700 hover:bg-emerald-600 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>🌳 Plant Vegetative Forest Canopy</span>
    </button>
    <button id="btnTriggerMonsoon" class="p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>🌧️ Unleash Monsoon Downpour</span>
    </button>
  </div>

  <div id="erosionExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🏞️ <span class="font-bold text-amber-300">Erosion Dynamics:</span> Weathering disintegrates rock in-situ, while erosion kinetically transports soil away. Plant roots bind topsoil, preventing devastating soil loss!
  </div>
</div>
""",

    # Sim 14: Energy Dynamics: Exothermic vs Endothermic Changes
    "energy_dynamics_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🌡️ Thermochemistry: Exo vs Endo Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">Energy Flow</span>
    </div>
    <span id="thermometerTempBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-400 font-mono font-bold">Temp: 25.0°C</span>
  </div>

  <!-- Thermochemistry Beaker SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Laboratory Beaker -->
      <g transform="translate(170, 45)">
        <rect x="0" y="0" width="100" height="110" rx="4" fill="#0f172a" fill-opacity="0.3" stroke="#64748b" stroke-width="2"/>
        <!-- Solution liquid -->
        <rect id="thermoSolution" x="3" y="45" width="94" height="62" rx="3" fill="#38bdf8" fill-opacity="0.3" class="transition-all duration-500"/>

        <!-- Frost Crystals (Endothermic indicator) -->
        <g id="frostCrystals" class="hidden">
          <text x="50" y="75" fill="#bae6fd" font-size="20" text-anchor="middle">❄️</text>
        </g>
        <!-- Boiling Bubbles & Steam (Exothermic indicator) -->
        <g id="boilingBubbles" class="hidden">
          <circle cx="30" cy="80" r="4" fill="#facc15" opacity="0.8" class="animate-bounce"/>
          <circle cx="65" cy="70" r="5" fill="#facc15" opacity="0.8"/>
          <circle cx="50" cy="55" r="3.5" fill="#facc15" opacity="0.8"/>
          <path d="M 50,40 Q 40,20 50,0" fill="none" stroke="#ef4444" stroke-width="2"/>
        </g>
      </g>

      <!-- Digital Thermometer Probe inserted into Beaker -->
      <g transform="translate(230, 20)">
        <rect x="0" y="0" width="8" height="110" rx="3" fill="#e2e8f0" stroke="#94a3b8"/>
        <!-- Red Mercury / Alcohol Column -->
        <rect id="thermoLiquidColumn" x="2" y="55" width="4" height="52" fill="#ef4444" class="transition-all duration-500"/>
        <circle cx="4" cy="110" r="6" fill="#ef4444"/>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2">
    <button id="btnTestQuicklimeExo" class="p-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs transition shadow">
      🔥 Quicklime + Water (Exothermic CaO)
    </button>
    <button id="btnTestGlucoseEndo" class="p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow">
      ❄️ Glucose in Water (Endothermic Chill)
    </button>
  </div>

  <div id="thermoReactionFormula" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 font-mono">
    CaO (Quicklime) + H₂O ➔ Ca(OH)₂ + Heat (Boiling hot, ΔT > 0!)
  </div>
</div>
""",

    # Sim 15: The Law of Conservation of Mass in a Closed Vessel
    "conservation_of_mass_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">⚖️ Law of Conservation of Mass</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">Lavoisier 1789</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-mono font-bold">Balance: EXACT 250.00 g</span>
  </div>

  <!-- Sealed Flask on Digital Balance SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Digital Weighing Scale -->
      <rect x="120" y="145" width="200" height="25" rx="4" fill="#1e293b" stroke="#475569"/>
      <rect x="160" y="152" width="120" height="12" rx="2" fill="#020617"/>
      <text id="massDisplay" x="220" y="161" fill="#22c55e" font-size="10" font-family="monospace" text-anchor="middle">250.00 g</text>

      <!-- Sealed Conical Flask -->
      <g transform="translate(180, 35)">
        <!-- Rubber Stopper on Top -->
        <polygon points="20,-8 60,-8 52,10 28,10" fill="#475569"/>
        <!-- Glass Flask -->
        <path d="M 25,10 L 25,45 L 0,105 Q -5,115 15,115 L 65,115 Q 85,115 80,105 L 55,45 L 55,10 Z" fill="#0f172a" fill-opacity="0.3" stroke="#64748b" stroke-width="2"/>
        
        <!-- Vinegar in Main Flask -->
        <path d="M 8,95 L 0,105 Q -5,115 15,115 L 65,115 Q 85,115 80,105 L 72,95 Z" fill="#fef08a" fill-opacity="0.35"/>

        <!-- Small Internal Test Tube Holding Baking Soda (Tilted to mix) -->
        <g id="internalIgnitionTube" transform="translate(25, 45) rotate(20)" class="transition-transform duration-500">
          <rect x="0" y="0" width="12" height="50" rx="3" fill="#cbd5e1" stroke="#94a3b8"/>
          <!-- Powder inside -->
          <rect x="2" y="25" width="8" height="22" rx="1" fill="#f8fafc"/>
        </g>

        <!-- Effervescence Bubbles when mixed -->
        <g id="massBubbles" class="hidden">
          <circle cx="30" cy="100" r="3" fill="#ffffff" class="animate-ping"/>
          <circle cx="50" cy="95" r="2.5" fill="#ffffff"/>
        </g>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2">
    <button id="btnTiltFlaskToReact" class="p-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition shadow">
      🧪 Tilt Flask & Mix Reactants
    </button>
    <button id="btnResetMassExp" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition border border-slate-700">
      Reset Scale
    </button>
  </div>

  <div id="massExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    ⚖️ <span class="font-bold text-amber-300">Conservation Principle:</span> Total Mass Before Reaction = Total Mass After Reaction (250.00 g). Trapped CO₂ gas cannot escape the hermetically sealed stopper!
  </div>
</div>
""",

    # Sim 16: Ancient Indian Philosophy: Acharya Kanada's Vaisheshika Heritage
    "kanada_heritage_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🏛️ Acharya Kanada: Pilupaka vs Pitharapaka</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">600 BCE Heritage</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-400 font-bold">Vaisheshika Sutras</span>
  </div>

  <!-- Heritage Ceramic Potter & Kiln SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- View 1: Pitharapaka (Potter's Wheel - Physical Shaping) -->
      <g id="pitharapakaView">
        <!-- Potter's Spinning Wheel Base -->
        <ellipse cx="140" cy="140" rx="60" ry="15" fill="#334155" stroke="#475569" stroke-width="2"/>
        <rect x="135" y="140" width="10" height="25" fill="#1e293b"/>
        <!-- Raw Gray Wet Clay Pot being shaped -->
        <path id="rawClayPot" d="M 120,80 Q 110,110 120,135 L 160,135 Q 170,110 160,80 Z" fill="#94a3b8" stroke="#64748b" stroke-width="2"/>
        <text x="140" y="65" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Pitharapaka</text>
        <text x="140" y="165" fill="#94a3b8" font-size="8" text-anchor="middle">Physical Shaping (Wet Gray Clay)</text>
      </g>

      <!-- View 2: Pilupaka (High Heat Kiln - Chemical Metamorphosis) -->
      <g id="pilupakaView" transform="translate(160, 0)">
        <!-- Kiln Brick Oven -->
        <path d="M 120,165 L 120,70 Q 160,40 200,70 L 200,165 Z" fill="#1e293b" stroke="#78350f" stroke-width="2"/>
        <ellipse cx="160" cy="165" rx="40" ry="10" fill="#0f172a"/>
        <!-- Kiln Fire Glow (Tejas) -->
        <circle id="kilnHeatTejas" cx="160" cy="130" r="30" fill="#f97316" opacity="0.6"/>
        <!-- Baked Red Terracotta Pot -->
        <path id="bakedTerracottaPot" d="M 145,95 Q 135,120 145,145 L 175,145 Q 185,120 175,95 Z" fill="#c2410c" stroke="#9a3412" stroke-width="2"/>
        <text x="160" y="60" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">Pilupaka (Tejas)</text>
        <text x="160" y="175" fill="#ea580c" font-size="8" text-anchor="middle">Chemical Transformation (Red Terracotta)</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2">
    <button id="btnPitharapakaDemo" class="p-2.5 rounded-xl bg-cyan-700 hover:bg-cyan-600 text-white font-bold text-xs transition shadow">
      🌀 Pitharapaka: Physical Shaping (Wheel)
    </button>
    <button id="btnPilupakaDemo" class="p-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition shadow">
      🔥 Pilupaka: Chemical Change by Tejas (Kiln)
    </button>
  </div>

  <div id="kanadaHeritageExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    📜 <span class="font-bold text-amber-300">Acharya Kanada's Philosophy:</span> In <span class="italic text-amber-200">Vaisheshika Sutras</span> (~600 BCE), Kanada distinguished <span class="text-cyan-300 font-bold">Pitharapaka</span> (physical change of shape) from <span class="text-amber-400 font-bold">Pilupaka</span> (chemical bond cleavage induced by heat energy 'tejas')!
  </div>
</div>
"""
}

with open(".agents/class7_science_changes_sims.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 7 Science Chapter 5 Simulators HTML Dictionary"""\n\n')
    f.write("SIMULATORS_HTML = " + repr(SIMULATORS_HTML) + "\n")

print("Generated .agents/class7_science_changes_sims.py successfully.")

