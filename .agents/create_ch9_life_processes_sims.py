# -*- coding: utf-8 -*-
"""
Generates .agents/class7_science_life_processes_sims.py containing 16 interactive simulators
for Class 7 Science Chapter 9: Life Processes in Animals.
"""

simulators = {}

# 1. macronutrient_breakdown_sim
simulators["macronutrient_breakdown_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.1 Biochemistry</span>
      <h4 class="text-sm font-bold text-slate-100">Macronutrient Disassembly: Complex → Simple</h4>
    </div>
    <div class="flex gap-1.5" id="macroTabs">
      <button onclick="window.switchMacroTab('carb')" id="btnMacroCarb" class="px-3 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md">Carbohydrates</button>
      <button onclick="window.switchMacroTab('protein')" id="btnMacroProtein" class="px-3 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">Proteins</button>
      <button onclick="window.switchMacroTab('fat')" id="btnMacroFat" class="px-3 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">Fats</button>
    </div>
  </div>

  <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-3">
    <svg id="macroSvg" viewBox="0 0 600 240" class="w-full h-full">
      <g id="macroVisualGroup"></g>
    </svg>
    <div id="macroBadge" class="absolute bottom-2 left-3 bg-slate-900/80 border border-slate-700 text-xs px-3 py-1 rounded-lg text-amber-300 font-mono">
      Polymer: Insoluble Starch Chain
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <span id="macroExpl" class="text-slate-300">Digestive enzymes cleave long starch polymer chains into simple, soluble glucose units for cellular energy.</span>
    <div class="flex gap-2">
      <button onclick="window.animateMacroCleavage()" id="btnMacroCleave" class="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold transition">▶ Digest Molecule</button>
      <button onclick="window.resetMacro()" class="px-2.5 py-1.5 rounded-lg bg-slate-700 hover:bg-slate-600 text-slate-300 font-semibold transition">↺ Reset</button>
    </div>
  </div>
</div>
"""

# 2. alimentary_canal_map_sim
simulators["alimentary_canal_map_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.1 Human Anatomy</span>
      <h4 class="text-sm font-bold text-slate-100">The 9-Metre Alimentary Canal: Organ Roadmap</h4>
    </div>
    <span class="text-xs text-slate-400 font-mono">Click any organ to inspect!</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-12 gap-3">
    <!-- Interactive Digestive Tract SVG -->
    <div class="md:col-span-7 relative h-64 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2">
      <svg viewBox="0 0 320 250" class="w-full h-full cursor-pointer">
        <!-- Human body silhouette outline -->
        <path d="M 120,20 C 130,10 190,10 200,20 C 205,35 200,50 195,55 L 210,80 L 225,140 L 210,240 L 110,240 L 95,140 L 110,80 Z" fill="#0f172a" stroke="#334155" stroke-width="1.5" opacity="0.6"/>
        
        <!-- Mouth / Buccal Cavity -->
        <circle id="orgMouth" cx="160" cy="35" r="12" fill="#f59e0b" opacity="0.8" onclick="window.inspectOrgan('mouth')" class="hover:opacity-100"/>
        <text x="160" y="38" text-anchor="middle" fill="#020617" font-size="8" font-weight="bold" pointer-events="none">Mouth</text>

        <!-- Oesophagus -->
        <line id="orgOesoph" x1="160" y1="47" x2="160" y2="90" stroke="#f59e0b" stroke-width="6" stroke-linecap="round" onclick="window.inspectOrgan('oesophagus')"/>

        <!-- Stomach -->
        <path id="orgStomach" d="M 160,90 Q 145,100 145,115 Q 145,130 170,125 Q 185,120 180,105 Q 175,90 160,90 Z" fill="#ef4444" opacity="0.85" onclick="window.inspectOrgan('stomach')"/>
        
        <!-- Liver & Gall Bladder -->
        <path id="orgLiver" d="M 130,95 L 155,95 L 150,118 L 125,115 Z" fill="#b45309" opacity="0.85" onclick="window.inspectOrgan('liver')"/>
        <circle cx="145" cy="115" r="4" fill="#22c55e" onclick="window.inspectOrgan('liver')"/>

        <!-- Pancreas -->
        <path id="orgPancreas" d="M 155,120 Q 170,125 185,122" stroke="#fef08a" stroke-width="5" stroke-linecap="round" fill="none" onclick="window.inspectOrgan('pancreas')"/>

        <!-- Small Intestine (coiled) -->
        <g id="orgSmallInt" onclick="window.inspectOrgan('small_int')" class="cursor-pointer">
          <ellipse cx="160" cy="165" rx="28" ry="22" fill="#38bdf8" opacity="0.75"/>
          <path d="M 145,155 Q 160,150 175,155 Q 160,165 145,175 Q 160,180 175,175" fill="none" stroke="#0284c7" stroke-width="4"/>
        </g>

        <!-- Large Intestine (framing) -->
        <path id="orgLargeInt" d="M 125,185 L 125,145 Q 125,135 135,135 L 185,135 Q 195,135 195,145 L 195,190" fill="none" stroke="#a855f7" stroke-width="7" stroke-linecap="round" onclick="window.inspectOrgan('large_int')"/>

        <!-- Rectum & Anus -->
        <line id="orgRectum" x1="160" y1="195" x2="160" y2="215" stroke="#f43f5e" stroke-width="5" onclick="window.inspectOrgan('rectum')"/>
      </svg>
    </div>

    <!-- Organ Detail Card -->
    <div class="md:col-span-5 bg-slate-800/60 p-3 rounded-xl border border-slate-700/60 flex flex-col justify-between text-xs">
      <div>
        <div class="flex items-center justify-between mb-1">
          <h5 id="organName" class="text-amber-400 font-bold text-sm">Buccal Cavity (Mouth)</h5>
          <span id="organPhBadge" class="px-2 py-0.5 rounded bg-slate-900 border border-slate-700 font-mono text-[10px] text-cyan-300">pH 6.8 (Neutral)</span>
        </div>
        <p id="organDesc" class="text-slate-300 text-[11px] leading-relaxed mb-2">
          Teeth mechanically crush and grind food; saliva contains salivary amylase to break starch into simple sugars.
        </p>
        <div class="bg-slate-950 p-2 rounded-lg border border-slate-800 space-y-1 font-mono text-[11px]">
          <div class="text-slate-400">Length: <span id="organLength" class="text-slate-200">~10 cm</span></div>
          <div class="text-slate-400">Key Secretion: <span id="organSecretion" class="text-emerald-400">Saliva (Amylase)</span></div>
          <div class="text-slate-400">Primary Task: <span id="organTask" class="text-amber-300">Chewing & Starch Breakdown</span></div>
        </div>
      </div>

      <div class="flex flex-wrap gap-1 mt-2">
        <button onclick="window.inspectOrgan('stomach')" class="px-2 py-0.5 rounded bg-slate-700 hover:bg-slate-600 text-[10px]">Stomach</button>
        <button onclick="window.inspectOrgan('small_int')" class="px-2 py-0.5 rounded bg-slate-700 hover:bg-slate-600 text-[10px]">Small Intestine</button>
        <button onclick="window.inspectOrgan('liver')" class="px-2 py-0.5 rounded bg-slate-700 hover:bg-slate-600 text-[10px]">Liver / Bile</button>
        <button onclick="window.inspectOrgan('large_int')" class="px-2 py-0.5 rounded bg-slate-700 hover:bg-slate-600 text-[10px]">Large Intestine</button>
      </div>
    </div>
  </div>
</div>
"""

# 3. mouth_saliva_starch_sim
simulators["mouth_saliva_starch_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.1.1 Laboratory Test</span>
      <h4 class="text-sm font-bold text-slate-100">Iodine Starch Test: Unchewed vs. Saliva-Chewed Bread</h4>
    </div>
    <span class="text-xs font-mono text-cyan-300 bg-cyan-950/60 border border-cyan-800/80 px-2.5 py-0.5 rounded">Iodine turns Starch Blue-Black</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <!-- Test Tube A: Unchewed Bread (Starch Present) -->
    <div class="relative h-60 bg-slate-950 rounded-xl border border-slate-800 flex flex-col justify-between items-center p-3">
      <span class="text-amber-300 font-bold">Tube A: Boiled Rice / Bread (No Saliva)</span>
      <svg viewBox="0 0 100 140" class="w-24 h-32">
        <!-- Test tube outline -->
        <path d="M 30,10 L 30,110 A 20,20 0 0,0 70,110 L 70,10 Z" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
        <!-- Liquid content -->
        <path id="tubeALiquid" d="M 32,60 L 32,110 A 18,18 0 0,0 68,110 L 68,60 Z" fill="#38bdf8" opacity="0.6"/>
        <text id="tubeALabel" x="50" y="90" text-anchor="middle" fill="#fff" font-size="8">Starch</text>
      </svg>
      <div id="tubeAResult" class="bg-slate-900 p-1.5 rounded-lg border border-slate-800 text-center text-[11px] text-slate-300 w-full font-mono">
        Add Iodine Dropper → Turns Blue-Black
      </div>
    </div>

    <!-- Test Tube B: Chewed Bread with Saliva (Starch Digested) -->
    <div class="relative h-60 bg-slate-950 rounded-xl border border-slate-800 flex flex-col justify-between items-center p-3">
      <span class="text-emerald-300 font-bold">Tube B: Chewed with Saliva (3 Minutes)</span>
      <svg viewBox="0 0 100 140" class="w-24 h-32">
        <!-- Test tube outline -->
        <path d="M 30,10 L 30,110 A 20,20 0 0,0 70,110 L 70,10 Z" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
        <!-- Liquid content -->
        <path id="tubeBLiquid" d="M 32,60 L 32,110 A 18,18 0 0,0 68,110 L 68,60 Z" fill="#fef08a" opacity="0.6"/>
        <text id="tubeBLabel" x="50" y="90" text-anchor="middle" fill="#78350f" font-size="8">Maltose</text>
      </svg>
      <div id="tubeBResult" class="bg-slate-900 p-1.5 rounded-lg border border-slate-800 text-center text-[11px] text-slate-300 w-full font-mono">
        Add Iodine Dropper → Remains Brown/Yellow
      </div>
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <span class="text-slate-300">Chewing mixes food with salivary amylase, transforming insoluble starch into simple sugars that give no blue-black test.</span>
    <button onclick="window.dropIodineTest()" id="btnDropIodine" class="px-3.5 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-semibold transition">🧪 Add Iodine Drops</button>
  </div>
</div>
"""

# 4. peristalsis_wave_sim
simulators["peristalsis_wave_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.1.1 Muscle Wave</span>
      <h4 class="text-sm font-bold text-slate-100">Peristalsis: How the Food Pipe Propels Food</h4>
    </div>
    <span class="text-xs text-slate-400">Works upside-down and in zero gravity!</span>
  </div>

  <div class="relative w-full h-60 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg id="peristalsisSvg" viewBox="0 0 500 200" class="w-full h-full">
      <!-- Oesophagus walls -->
      <path id="oesophTopWall" d="M 50,60 Q 200,60 250,60 Q 300,60 450,60" fill="none" stroke="#f43f5e" stroke-width="8" stroke-linecap="round"/>
      <path id="oesophBottomWall" d="M 50,140 Q 200,140 250,140 Q 300,140 450,140" fill="none" stroke="#f43f5e" stroke-width="8" stroke-linecap="round"/>
      
      <!-- Stomach entrance on right -->
      <path d="M 450,40 Q 480,40 480,100 Q 480,160 450,160" fill="#ef4444" opacity="0.3" stroke="#ef4444" stroke-width="2"/>
      <text x="470" y="105" fill="#fca5a5" font-size="10" text-anchor="middle">Stomach</text>

      <!-- Food Bolus -->
      <ellipse id="peristalsisBolus" cx="150" cy="100" rx="24" ry="18" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
      <text id="bolusText" x="150" y="104" text-anchor="middle" fill="#78350f" font-size="9" font-weight="bold">Bolus</text>

      <!-- Force contraction arrows -->
      <g id="contractionArrows" transform="translate(110, 0)">
        <polygon points="10,40 10,55 5,50 15,50" fill="#38bdf8"/>
        <polygon points="10,160 10,145 5,150 15,150" fill="#38bdf8"/>
        <text x="10" y="32" text-anchor="middle" fill="#38bdf8" font-size="9">Circular Muscle Contracts</text>
      </g>
    </svg>
    <div id="peristalsisBadge" class="absolute bottom-2 left-3 bg-slate-900/80 border border-slate-700 text-xs px-3 py-1 rounded-lg text-amber-300 font-mono">
      Bolus Transit: Upper Oesophagus
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <div class="flex items-center gap-2 flex-1">
      <label class="text-slate-300 font-medium">Transit Position:</label>
      <input type="range" id="peristalsisSlider" min="80" max="420" value="150" class="flex-1 accent-amber-500 h-1.5 bg-slate-700 rounded-lg cursor-pointer" oninput="window.setPeristalsisPos(this.value)">
    </div>
    <div class="flex gap-2">
      <button onclick="window.autoPeristalsis()" id="btnAutoPeristalsis" class="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold transition">▶ Swallow Bolus</button>
      <button onclick="window.resetPeristalsis()" class="px-2.5 py-1.5 rounded-lg bg-slate-700 text-slate-300">↺</button>
    </div>
  </div>
</div>
"""

# 5. stomach_churning_acid_sim
simulators["stomach_churning_acid_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.1.1 Gastric Physiology</span>
      <h4 class="text-sm font-bold text-slate-100">The Gastric Reactor: Acid, Pepsin & Mucus Shield</h4>
    </div>
    <span class="text-xs font-mono text-rose-300 bg-rose-950/60 border border-rose-800/80 px-2.5 py-0.5 rounded">Gastric Acid: pH 1.5–2.0</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
    <!-- Stomach Visual Canvas -->
    <div class="md:col-span-2 relative h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
      <svg id="stomachSimSvg" viewBox="0 0 360 220" class="w-full h-full">
        <!-- Stomach J-shape muscular body -->
        <path d="M 120,20 Q 90,80 90,140 Q 90,200 170,200 Q 250,200 260,140 Q 270,90 200,80 Q 150,70 145,20 Z" fill="#991b1b" stroke="#ef4444" stroke-width="4"/>
        
        <!-- Mucus Layer (toggled) -->
        <path id="stomachMucusLayer" d="M 124,24 Q 98,80 98,138 Q 98,192 170,192 Q 242,192 252,140 Q 262,95 198,86 Q 152,76 148,24 Z" fill="none" stroke="#34d399" stroke-width="6" opacity="0.8"/>

        <!-- Acid / Chyme Pool inside -->
        <path id="stomachChymePool" d="M 104,110 Q 104,184 170,184 Q 236,184 244,130 Q 210,125 170,125 Q 130,125 104,110 Z" fill="#f59e0b" opacity="0.65"/>

        <!-- Protein Chunks dissolving -->
        <g id="stomachProteinParticles">
          <circle cx="150" cy="150" r="8" fill="#e2e8f0"/>
          <circle cx="180" cy="160" r="6" fill="#e2e8f0"/>
          <circle cx="165" cy="140" r="7" fill="#e2e8f0"/>
        </g>
        <!-- Acid droplets falling -->
        <g id="acidDrops" opacity="0.8">
          <circle cx="140" cy="60" r="3" fill="#fef08a"/>
          <circle cx="155" cy="80" r="3" fill="#fef08a"/>
          <circle cx="170" cy="65" r="3" fill="#fef08a"/>
        </g>
      </svg>
      <div id="stomachStatusBadge" class="absolute top-2 left-2 bg-slate-900/85 border border-slate-700 text-xs px-2.5 py-1 rounded text-slate-300 font-mono">
        Mucus Shield: ACTIVE • Gastric Wall Protected
      </div>
    </div>

    <!-- Controls -->
    <div class="flex flex-col justify-between gap-2 bg-slate-800/60 p-3 rounded-xl border border-slate-700/60 text-xs">
      <div>
        <h5 class="text-slate-200 font-bold mb-2">Gastric Factors:</h5>
        
        <label class="flex items-center gap-2 cursor-pointer mb-2">
          <input type="checkbox" id="chkMucus" checked class="accent-emerald-500 rounded" onchange="window.toggleStomachMucus()">
          <span class="text-emerald-300 font-medium">Mucus Shield Layer</span>
        </label>

        <label class="flex items-center gap-2 cursor-pointer mb-2">
          <input type="checkbox" id="chkAcid" checked class="accent-amber-500 rounded" onchange="window.toggleStomachAcid()">
          <span class="text-amber-300 font-medium">Hydrochloric Acid (HCl)</span>
        </label>

        <label class="flex items-center gap-2 cursor-pointer">
          <input type="checkbox" id="chkPepsin" checked class="accent-cyan-500 rounded" onchange="window.toggleStomachPepsin()">
          <span class="text-cyan-300 font-medium">Pepsin Protease Enzyme</span>
        </label>
      </div>

      <div class="p-2 bg-slate-950 rounded-lg border border-slate-800 text-[11px] leading-tight text-slate-300" id="stomachFeedback">
        HCl activates pepsin to cleave proteins; the green alkaline mucus protects the stomach from digesting itself!
      </div>

      <button onclick="window.churnStomach()" id="btnChurnStomach" class="w-full py-1.5 rounded-lg bg-rose-700 hover:bg-rose-600 text-white font-semibold transition">Vigorous Churning</button>
    </div>
  </div>
</div>
"""

# 6. liver_pancreas_bile_sim
simulators["liver_pancreas_bile_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.1.1 Emulsification</span>
      <h4 class="text-sm font-bold text-slate-100">Bile Action: Fat Emulsification & Lipase Digestion</h4>
    </div>
    <span class="text-xs font-mono text-emerald-300 bg-emerald-950/60 border border-emerald-800/80 px-2.5 py-0.5 rounded">Bile: No Enzymes, Pure Detergent Action</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <!-- Large Fat Globule (Before Bile) -->
    <div class="relative h-60 bg-slate-950 rounded-xl border border-slate-800 flex flex-col justify-between items-center p-3">
      <span class="text-rose-300 font-bold">1. Large Insoluble Fat Droplet (Low Surface Area)</span>
      <svg viewBox="0 0 160 140" class="w-40 h-32">
        <circle id="largeFatDrop" cx="80" cy="70" r="45" fill="#f59e0b" stroke="#d97706" stroke-width="3"/>
        <text x="80" y="74" text-anchor="middle" fill="#78350f" font-size="11" font-weight="bold">FAT GLOBULE</text>
      </svg>
      <div class="text-[11px] text-slate-400 text-center">Lipase enzyme cannot reach inner fat molecules</div>
    </div>

    <!-- Emulsified Micro-Droplets (After Bile) -->
    <div class="relative h-60 bg-slate-950 rounded-xl border border-slate-800 flex flex-col justify-between items-center p-3">
      <span class="text-emerald-300 font-bold">2. Emulsified Micelles (1000× Surface Area)</span>
      <svg id="micellesSvg" viewBox="0 0 160 140" class="w-40 h-32">
        <!-- Rendered dynamically -->
      </svg>
      <div id="emulsifyResultText" class="text-[11px] text-emerald-400 font-bold text-center">
        Bile salts coat micro-droplets; Lipase digests rapidly!
      </div>
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <span class="text-slate-300">Like washing greasy hands with soap: bile salts break large oil drops into microscopic droplets so lipase can digest them into fatty acids.</span>
    <button onclick="window.triggerEmulsification()" id="btnEmulsify" class="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold transition">🧪 Add Liver Bile</button>
  </div>
</div>
"""

# 7. intestinal_villi_absorption_sim
simulators["intestinal_villi_absorption_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.1.1 Microscopic Absorption</span>
      <h4 class="text-sm font-bold text-slate-100">Intestinal Villi: Blood Capillaries & Central Lacteal</h4>
    </div>
    <span class="text-xs font-mono text-cyan-300 bg-cyan-950/60 border border-cyan-800/80 px-2.5 py-0.5 rounded">Surface Area: > 250 m²</span>
  </div>

  <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg id="villiSvg" viewBox="0 0 500 220" class="w-full h-full">
      <!-- Intestinal lumen background with nutrient molecules -->
      <g id="lumenNutrients"></g>

      <!-- Three Finger-like Villi -->
      <!-- Villus 1 -->
      <path d="M 80,220 L 80,70 A 30,30 0 0,1 140,70 L 140,220 Z" fill="#1e293b" stroke="#f43f5e" stroke-width="3"/>
      <!-- Villus 2 (Focus) -->
      <path d="M 210,220 L 210,50 A 40,40 0 0,1 290,50 L 290,220 Z" fill="#0f172a" stroke="#f43f5e" stroke-width="4"/>
      <!-- Villus 3 -->
      <path d="M 360,220 L 360,70 A 30,30 0 0,1 420,70 L 420,220 Z" fill="#1e293b" stroke="#f43f5e" stroke-width="3"/>

      <!-- Inside Center Villus 2: Central Lacteal (Lymph) -->
      <path d="M 245,220 L 245,75 A 5,5 0 0,1 255,75 L 255,220 Z" fill="#fef08a" opacity="0.9"/>
      <text x="250" y="100" text-anchor="middle" fill="#78350f" font-size="8" transform="rotate(-90 250 100)">LACTEAL (Fats)</text>

      <!-- Blood Capillary Loop surrounding Lacteal -->
      <path d="M 230,220 L 230,70 Q 250,55 270,70 L 270,220" fill="none" stroke="#ef4444" stroke-width="3.5"/>
      <path d="M 235,220 L 235,80 Q 250,65 265,80 L 265,220" fill="none" stroke="#38bdf8" stroke-width="3"/>
      <text x="280" y="140" fill="#38bdf8" font-size="8">Capillaries (Sugars & Amino Acids)</text>

      <!-- Epithelial Single Cell Layer -->
      <path d="M 206,220 L 206,48 A 44,44 0 0,1 294,48 L 294,220" fill="none" stroke="#fbcfe8" stroke-width="2" stroke-dasharray="2 2"/>
    </svg>
    <div id="villiStatusBadge" class="absolute bottom-2 left-3 bg-slate-900/85 border border-slate-700 text-xs px-3 py-1 rounded-lg text-emerald-400 font-mono">
      Absorption Active: Glucose & Amino Acids → Blood; Fats → Lacteal
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <span class="text-slate-300">Each villus has a one-cell-thin wall. Sugars & amino acids cross into capillaries, while fatty acids enter the central lacteal.</span>
    <button onclick="window.pumpVilliAbsorption()" id="btnVilliAbsorb" class="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold transition">▶ Absorb Nutrients</button>
  </div>
</div>
"""

# 8. large_intestine_egestion_sim
simulators["large_intestine_egestion_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.1.1 Colon & Rectum</span>
      <h4 class="text-sm font-bold text-slate-100">Large Intestine: Water Reabsorption & Egestion</h4>
    </div>
    <span class="text-xs text-slate-400">Reclaims up to 90% of digestive water</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <!-- Colon Graphic -->
    <div class="relative h-60 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2">
      <svg viewBox="0 0 240 180" class="w-full h-full">
        <!-- Colon Frame -->
        <path d="M 40,150 L 40,50 Q 40,30 60,30 L 180,30 Q 200,30 200,50 L 200,140 Q 200,160 170,160 L 120,160 L 120,175" fill="none" stroke="#64748b" stroke-width="18" stroke-linecap="round"/>
        <!-- Moisture gradient inside -->
        <path id="colonMoisturePath" d="M 40,150 L 40,50 Q 40,30 60,30 L 180,30 Q 200,30 200,50 L 200,140" fill="none" stroke="#38bdf8" stroke-width="12" stroke-linecap="round" opacity="0.7"/>
        
        <!-- Water droplets exiting into blood -->
        <circle cx="55" cy="90" r="3" fill="#38bdf8"/>
        <circle cx="120" cy="18" r="3" fill="#38bdf8"/>
        <circle cx="215" cy="90" r="3" fill="#38bdf8"/>
        
        <!-- Rectum & Stool -->
        <ellipse cx="145" cy="160" rx="14" ry="7" fill="#78350f"/>
        <text x="145" y="163" text-anchor="middle" fill="#fde047" font-size="7">Faeces</text>
      </svg>
    </div>

    <!-- Reabsorption Metrics -->
    <div class="bg-slate-800/60 p-3 rounded-xl border border-slate-700/60 flex flex-col justify-between">
      <div>
        <h5 class="text-slate-200 font-bold mb-2">Water Balance Simulator:</h5>
        <div class="mb-2">
          <div class="flex justify-between text-slate-300 mb-1">
            <span>Water Extraction:</span>
            <span id="waterExtractVal" class="font-mono text-cyan-300 font-bold">85%</span>
          </div>
          <input type="range" id="waterExtractSlider" min="30" max="95" value="85" class="w-full accent-cyan-500 h-1.5 bg-slate-700 rounded-lg cursor-pointer" oninput="window.setWaterExtraction(this.value)">
        </div>

        <div class="bg-slate-950 p-2 rounded-lg border border-slate-800 space-y-1 font-mono text-[11px]">
          <div class="flex justify-between"><span class="text-slate-400">Incoming Chyme:</span><span class="text-sky-300">Liquid / Watery</span></div>
          <div class="flex justify-between"><span class="text-slate-400">Stool Consistency:</span><span id="stoolConsistency" class="text-amber-400 font-bold">Semi-Solid (Normal)</span></div>
          <div class="flex justify-between"><span class="text-slate-400">Final Stage:</span><span class="text-rose-400">Egestion via Anus</span></div>
        </div>
      </div>

      <p class="text-[10px] text-slate-400 mt-2">
        If infection causes the colon to expel food before absorbing water, it results in <strong>diarrhea</strong> (dehydration risk).
      </p>
    </div>
  </div>
</div>
"""

# 9. ruminant_digestion_sim
simulators["ruminant_digestion_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.1.2 Herbivore Adaptations</span>
      <h4 class="text-sm font-bold text-slate-100">Ruminant Digestion: 4 Chambers & Cud Chewing</h4>
    </div>
    <span class="text-xs font-mono text-emerald-400 bg-emerald-950/60 border border-emerald-800/80 px-2.5 py-0.5 rounded">Rumen Ferments Cellulose</span>
  </div>

  <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg id="ruminantSvg" viewBox="0 0 500 240" class="w-full h-full">
      <!-- Cow body outline -->
      <path d="M 50,110 Q 50,60 120,60 L 380,60 Q 450,60 450,140 L 450,200 L 410,200 L 400,160 L 150,160 L 140,200 L 100,200 Z" fill="#0f172a" stroke="#334155" stroke-width="2" opacity="0.6"/>
      
      <!-- Cow Head & Mouth on left -->
      <ellipse cx="60" cy="90" rx="25" ry="18" fill="#1e293b" stroke="#475569" stroke-width="2"/>
      <text x="60" y="93" text-anchor="middle" fill="#fef08a" font-size="9" font-weight="bold">Mouth</text>

      <!-- Chamber 1: Rumen (huge green sac) -->
      <ellipse id="rumenSac" cx="240" cy="110" rx="70" ry="40" fill="#166534" stroke="#22c55e" stroke-width="2" opacity="0.85"/>
      <text x="240" y="112" text-anchor="middle" fill="#dcfce7" font-size="11" font-weight="bold">1. Rumen (Ferments Grass)</text>

      <!-- Chamber 2: Reticulum (honeycomb) -->
      <ellipse cx="150" cy="120" rx="25" ry="20" fill="#854d0e" stroke="#eab308" stroke-width="2" opacity="0.85"/>
      <text x="150" y="122" text-anchor="middle" fill="#fef9c3" font-size="8" font-weight="bold">2. Reticulum</text>

      <!-- Chamber 3: Omasum -->
      <ellipse cx="320" cy="110" rx="22" ry="18" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2" opacity="0.85"/>
      <text x="320" y="113" text-anchor="middle" fill="#dbeafe" font-size="8" font-weight="bold">3. Omasum</text>

      <!-- Chamber 4: Abomasum (True Stomach) -->
      <ellipse cx="370" cy="125" rx="26" ry="18" fill="#991b1b" stroke="#ef4444" stroke-width="2" opacity="0.85"/>
      <text x="370" y="128" text-anchor="middle" fill="#fee2e2" font-size="8" font-weight="bold">4. Abomasum</text>

      <!-- Animated Cud dot -->
      <circle id="cudParticle" cx="60" cy="90" r="7" fill="#facc15" stroke="#fff" stroke-width="1.5"/>
    </svg>
    <div id="ruminantStepBadge" class="absolute bottom-2 left-3 bg-slate-900/85 border border-slate-700 text-xs px-3 py-1 rounded-lg text-amber-300 font-mono">
      Step 1: Rapidly swallow grass into Rumen for bacterial fermentation
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <div class="flex gap-1.5">
      <button onclick="window.stepRuminant(1)" id="btnRum1" class="px-2.5 py-1 rounded bg-amber-500 text-slate-950 font-semibold">1. Swallow Grass</button>
      <button onclick="window.stepRuminant(2)" id="btnRum2" class="px-2.5 py-1 rounded bg-slate-700 text-slate-300 hover:bg-slate-600">2. Chew Cud (Rumination)</button>
      <button onclick="window.stepRuminant(3)" id="btnRum3" class="px-2.5 py-1 rounded bg-slate-700 text-slate-300 hover:bg-slate-600">3. True Digestion</button>
    </div>
    <button onclick="window.resetRuminant()" class="px-2.5 py-1 rounded bg-slate-700 text-slate-300">↺</button>
  </div>
</div>
"""

# 10. bird_gizzard_mechanics_sim
simulators["bird_gizzard_mechanics_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.1.2 Avian Anatomy</span>
      <h4 class="text-sm font-bold text-slate-100">Toothless Digestion: Crop & Muscular Gizzard Mill</h4>
    </div>
    <span class="text-xs text-slate-400">Birds swallow pebbles to grind hard seeds!</span>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <!-- Bird Gizzard Mill SVG -->
    <div class="relative h-60 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2">
      <svg id="gizzardSvg" viewBox="0 0 240 180" class="w-full h-full">
        <!-- Crop pouch on top left -->
        <ellipse cx="60" cy="50" rx="30" ry="22" fill="#d97706" opacity="0.75" stroke="#f59e0b" stroke-width="2"/>
        <text x="60" y="53" text-anchor="middle" fill="#fef08a" font-size="9" font-weight="bold">Crop (Storage)</text>

        <!-- Tube to Gizzard -->
        <path d="M 85,60 Q 110,70 120,90" fill="none" stroke="#f43f5e" stroke-width="6"/>

        <!-- Gizzard with thick muscular walls -->
        <g id="gizzardBody" transform="translate(160, 110)">
          <!-- Outer muscular mantle -->
          <ellipse cx="0" cy="0" rx="55" ry="45" fill="#881337" stroke="#e11d48" stroke-width="4"/>
          <!-- Inner tough keratin lining -->
          <ellipse cx="0" cy="0" rx="40" ry="32" fill="#4c0519"/>
          <!-- Swallowed stones (gastroliths) -->
          <circle cx="-15" cy="-8" r="6" fill="#94a3b8"/>
          <circle cx="12" cy="10" r="7" fill="#64748b"/>
          <circle cx="5" cy="-14" r="5" fill="#cbd5e1"/>
          <!-- Grains being crushed -->
          <circle id="seed1" cx="-5" cy="5" r="5" fill="#facc15"/>
          <circle id="seed2" cx="15" cy="-5" r="4" fill="#facc15"/>
        </g>
        <text x="160" y="170" text-anchor="middle" fill="#fda4af" font-size="10" font-weight="bold">Muscular Gizzard (Stone Mill)</text>
      </svg>
    </div>

    <!-- Mill Mechanics Controls -->
    <div class="bg-slate-800/60 p-3 rounded-xl border border-slate-700/60 flex flex-col justify-between">
      <div>
        <h5 class="text-slate-200 font-bold mb-2">Gizzard Mill Action:</h5>
        <p class="text-slate-300 text-[11px] mb-2 leading-relaxed">
          Because birds have no heavy teeth, hard grains are softened in the <strong>crop</strong> and then pulverized against swallowed stones (gastroliths) by the gizzard's muscular contractions.
        </p>
        <div class="bg-slate-950 p-2.5 rounded-lg border border-slate-800 font-mono text-[11px] space-y-1">
          <div class="flex justify-between"><span class="text-slate-400">Swallowed Stones:</span><span class="text-cyan-300">Pebbles & Grit</span></div>
          <div class="flex justify-between"><span class="text-slate-400">Crushing Pressure:</span><span id="gizzardPressure" class="text-rose-400 font-bold">High (Muscular)</span></div>
          <div class="flex justify-between"><span class="text-slate-400">End Product:</span><span class="text-emerald-400">Finely Ground Flour</span></div>
        </div>
      </div>

      <button onclick="window.grindGizzard()" id="btnGrindGizzard" class="w-full py-1.5 rounded-lg bg-rose-700 hover:bg-rose-600 text-white font-semibold transition">▶ Contract Gizzard Muscles</button>
    </div>
  </div>
</div>
"""

# 11. cellular_respiration_sim
simulators["cellular_respiration_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.2 Cellular Engine</span>
      <h4 class="text-sm font-bold text-slate-100">Cellular Respiration: Mitochondria ATP Factory</h4>
    </div>
    <span class="text-xs font-mono text-cyan-300 bg-cyan-950/60 border border-cyan-800/80 px-2.5 py-0.5 rounded">C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP</span>
  </div>

  <div class="relative w-full h-60 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-3">
    <svg id="respireSvg" viewBox="0 0 500 200" class="w-full h-full">
      <!-- Mitochondria bean outline -->
      <ellipse cx="250" cy="100" rx="140" ry="65" fill="#78350f" stroke="#f59e0b" stroke-width="3" opacity="0.85"/>
      <!-- Inner cristae folds -->
      <path d="M 150,100 Q 180,70 190,100 T 230,100 T 270,100 T 310,100 T 350,100" fill="none" stroke="#fbbf24" stroke-width="4"/>
      <text x="250" y="55" text-anchor="middle" fill="#fef08a" font-size="11" font-weight="bold">MITOCHONDRION</text>

      <!-- Incoming Glucose & Oxygen -->
      <g transform="translate(40, 70)">
        <rect x="0" y="0" width="60" height="25" rx="4" fill="#0284c7"/>
        <text x="30" y="16" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">Glucose</text>
        <line x1="60" y1="12" x2="110" y2="25" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3 2"/>
      </g>
      <g transform="translate(40, 115)">
        <rect x="0" y="0" width="60" height="25" rx="4" fill="#059669"/>
        <text x="30" y="16" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">Oxygen (O₂)</text>
        <line x1="60" y1="12" x2="110" y2="-5" stroke="#34d399" stroke-width="2" stroke-dasharray="3 2"/>
      </g>

      <!-- Outgoing ATP Energy & Waste CO2, H2O -->
      <g transform="translate(400, 50)">
        <circle cx="20" cy="20" r="22" fill="#ea580c" filter="drop-shadow(0 0 8px rgba(234,88,12,0.9))"/>
        <text x="20" y="24" text-anchor="middle" fill="#fff" font-size="10" font-weight="black">ATP</text>
        <text x="20" y="52" text-anchor="middle" fill="#fdba74" font-size="8">Energy</text>
      </g>
      <g transform="translate(400, 130)">
        <text x="20" y="0" text-anchor="middle" fill="#94a3b8" font-size="10">CO₂ + H₂O</text>
        <text x="20" y="14" text-anchor="middle" fill="#64748b" font-size="8">By-products</text>
      </g>
    </svg>
    <div id="respireBadge" class="absolute bottom-2 left-3 bg-slate-900/85 border border-slate-700 text-xs px-3 py-1 rounded-lg text-amber-300 font-mono">
      Cellular Combustion Active: 38 ATP Produced per Glucose
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <span class="text-slate-300">Respiration is the slow biological combustion of glucose inside cells to release usable ATP chemical energy.</span>
    <button onclick="window.pulseCellularRespiration()" id="btnRespirePulse" class="px-3.5 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-semibold transition">⚡ Ignite Energy Release</button>
  </div>
</div>
"""

# 12. human_respiratory_tract_sim
simulators["human_respiratory_tract_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.2.1 Respiratory Tree</span>
      <h4 class="text-sm font-bold text-slate-100">Human Respiratory Pathway: Nostrils to Bronchioles</h4>
    </div>
    <span class="text-xs text-slate-400">Nose filters, warms, and humidifies air</span>
  </div>

  <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg id="respTractSvg" viewBox="0 0 400 240" class="w-full h-full">
      <!-- Nasal cavity & throat profile -->
      <path d="M 120,20 C 130,20 150,30 150,45 L 140,55 L 170,55 L 170,90" fill="none" stroke="#64748b" stroke-width="2"/>
      <circle cx="125" cy="40" r="5" fill="#f59e0b"/>
      <text x="100" y="42" text-anchor="end" fill="#fef08a" font-size="8">Nostrils (Hair & Mucus Filter)</text>

      <!-- Epiglottis -->
      <polygon points="165,70 180,68 175,75" fill="#ec4899"/>
      <text x="195" y="73" fill="#f472b6" font-size="8">Epiglottis</text>

      <!-- Trachea with C-rings -->
      <g id="tracheaGroup">
        <line x1="170" y1="85" x2="170" y2="140" stroke="#0284c7" stroke-width="12" stroke-linecap="round"/>
        <!-- C-shaped cartilage rings -->
        <line x1="164" y1="95" x2="176" y2="95" stroke="#e0f2fe" stroke-width="2"/>
        <line x1="164" y1="105" x2="176" y2="105" stroke="#e0f2fe" stroke-width="2"/>
        <line x1="164" y1="115" x2="176" y2="115" stroke="#e0f2fe" stroke-width="2"/>
        <line x1="164" y1="125" x2="176" y2="125" stroke="#e0f2fe" stroke-width="2"/>
      </g>
      <text x="195" y="115" fill="#38bdf8" font-size="8">Trachea (Cartilage Rings)</text>

      <!-- Left & Right Bronchi -->
      <path d="M 170,140 L 130,170" stroke="#0284c7" stroke-width="8" stroke-linecap="round"/>
      <path d="M 170,140 L 210,170" stroke="#0284c7" stroke-width="8" stroke-linecap="round"/>

      <!-- Left & Right Lungs (outlines) -->
      <path id="leftLung" d="M 100,160 Q 60,180 80,225 Q 140,230 140,175 Z" fill="#f43f5e" opacity="0.3" stroke="#f43f5e" stroke-width="2"/>
      <path id="rightLung" d="M 240,160 Q 280,180 260,225 Q 200,230 200,175 Z" fill="#f43f5e" opacity="0.3" stroke="#f43f5e" stroke-width="2"/>
      
      <!-- Air flow blue dot -->
      <circle id="airDot" cx="125" cy="40" r="4" fill="#38bdf8" filter="drop-shadow(0 0 6px #38bdf8)"/>
    </svg>
    <div id="respTractBadge" class="absolute bottom-2 right-3 bg-slate-900/85 border border-slate-700 text-xs px-3 py-1 rounded-lg text-cyan-300 font-mono">
      Pathway: Air filtered in nasal cavity
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <span class="text-slate-300">The C-shaped cartilage rings prevent the windpipe from collapsing when internal air pressure drops during inhalation.</span>
    <button onclick="window.traceAirflow()" id="btnTraceAir" class="px-3.5 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-semibold transition">▶ Inhale & Trace Airflow</button>
  </div>
</div>
"""

# 13. breathing_diaphragm_sim
simulators["breathing_diaphragm_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.2.1 Bell-Jar Model</span>
      <h4 class="text-sm font-bold text-slate-100">Breathing Physics: Diaphragm & Pressure Laws</h4>
    </div>
    <div class="flex gap-1.5">
      <button onclick="window.setBreathingAction('inhale')" id="btnInhale" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-cyan-500 text-slate-950 shadow-md">1. Inhale (Down)</button>
      <button onclick="window.setBreathingAction('exhale')" id="btnExhale" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">2. Exhale (Up)</button>
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
    <!-- Bell Jar SVG -->
    <div class="relative h-60 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-center p-2">
      <svg id="bellJarSvg" viewBox="0 0 200 200" class="w-full h-full">
        <!-- Glass Jar Outline -->
        <path d="M 40,160 L 40,50 Q 40,20 100,20 Q 160,20 160,50 L 160,160" fill="none" stroke="#64748b" stroke-width="3"/>
        
        <!-- Y-tube (Trachea & Bronchi) -->
        <line x1="100" y1="10" x2="100" y2="70" stroke="#38bdf8" stroke-width="4"/>
        <line x1="100" y1="70" x2="80" y2="90" stroke="#38bdf8" stroke-width="3"/>
        <line x1="100" y1="70" x2="120" y2="90" stroke="#38bdf8" stroke-width="3"/>

        <!-- Balloons (Lungs) -->
        <ellipse id="balloonLeft" cx="75" cy="110" rx="15" ry="20" fill="#f43f5e" opacity="0.8"/>
        <ellipse id="balloonRight" cx="125" cy="110" rx="15" ry="20" fill="#f43f5e" opacity="0.8"/>

        <!-- Rubber Sheet (Diaphragm) at bottom -->
        <path id="rubberDiaphragm" d="M 40,160 Q 100,160 160,160" fill="none" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>
        <text id="diaphragmText" x="100" y="180" text-anchor="middle" fill="#fef08a" font-size="9">Diaphragm Sheet</text>
      </svg>
    </div>

    <!-- Pressure Dynamics Readout -->
    <div class="bg-slate-800/60 p-3 rounded-xl border border-slate-700/60 flex flex-col justify-between">
      <div>
        <h5 id="breathModeTitle" class="text-cyan-400 font-bold mb-1">Inhalation (Breathing In)</h5>
        <div class="space-y-1.5 font-mono text-[11px] bg-slate-950 p-2.5 rounded-lg border border-slate-800">
          <div class="flex justify-between"><span class="text-slate-400">Diaphragm Motion:</span><span id="diaphragmState" class="text-cyan-300 font-bold">Contracts & Flattens Downward</span></div>
          <div class="flex justify-between"><span class="text-slate-400">Chest Cavity Volume:</span><span id="chestVolumeState" class="text-emerald-400 font-bold">EXPANDS</span></div>
          <div class="flex justify-between"><span class="text-slate-400">Internal Air Pressure:</span><span id="chestPressureState" class="text-rose-400 font-bold">DROPS (Negative)</span></div>
          <div class="flex justify-between"><span class="text-slate-400">Air Movement:</span><span id="airFlowState" class="text-amber-300 font-bold">Rushes into Lungs</span></div>
        </div>
      </div>

      <div class="text-[10px] text-slate-400 leading-tight">
        Lungs have no muscles of their own; they inflate purely due to atmospheric air pressure rushing in when chest cavity volume expands.
      </div>
    </div>
  </div>
</div>
"""

# 14. alveoli_gas_exchange_sim
simulators["alveoli_gas_exchange_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.2.1 Gas Exchange</span>
      <h4 class="text-sm font-bold text-slate-100">Alveolus & Capillary Junction: Oxygenation of RBCs</h4>
    </div>
    <span class="text-xs font-mono text-rose-300 bg-rose-950/60 border border-rose-800/80 px-2.5 py-0.5 rounded">Hb + 4O₂ ⇌ Hb(O₂)₄</span>
  </div>

  <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg id="alveoliSvg" viewBox="0 0 500 220" class="w-full h-full">
      <!-- Balloon-like Alveolus on left -->
      <ellipse cx="160" cy="110" rx="90" ry="75" fill="#1e293b" stroke="#94a3b8" stroke-width="2.5" opacity="0.85"/>
      <text x="160" y="70" text-anchor="middle" fill="#93c5fd" font-size="12" font-weight="bold">ALVEOLUS SAC</text>
      <text x="160" y="88" text-anchor="middle" fill="#cbd5e1" font-size="9">Inhaled Air (High O₂)</text>

      <!-- Capillary Tube wrapping around right edge -->
      <path d="M 230,20 Q 280,110 230,200" fill="none" stroke="#dc2626" stroke-width="26" opacity="0.4"/>
      
      <!-- Red Blood Cells flowing -->
      <g id="rbcFlowGroup">
        <!-- Flowing RBCs updated by JS -->
      </g>

      <!-- Oxygen diffusion arrows (Alveolus -> Capillary) -->
      <line x1="200" y1="95" x2="250" y2="95" stroke="#34d399" stroke-width="3" stroke-dasharray="3 2"/>
      <polygon points="252,95 244,91 244,99" fill="#34d399"/>
      <text x="225" y="85" text-anchor="middle" fill="#34d399" font-size="8" font-weight="bold">O₂ Enters</text>

      <!-- Carbon Dioxide diffusion arrows (Capillary -> Alveolus) -->
      <line x1="250" y1="130" x2="200" y2="130" stroke="#94a3b8" stroke-width="3" stroke-dasharray="3 2"/>
      <polygon points="198,130 206,126 206,134" fill="#94a3b8"/>
      <text x="225" y="145" text-anchor="middle" fill="#94a3b8" font-size="8" font-weight="bold">CO₂ Exits</text>
    </svg>
    <div id="alveoliBadge" class="absolute bottom-2 left-3 bg-slate-900/85 border border-slate-700 text-xs px-3 py-1 rounded-lg text-emerald-400 font-mono">
      Diffusion Active: Deoxygenated RBC (Purple) → Oxyhemoglobin (Crimson Red)
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <span class="text-slate-300">Over 300 million alveoli expand surface area to 80 m²; ultra-thin single-cell walls enable instantaneous gas diffusion into hemoglobin.</span>
    <button onclick="window.pumpAlveolarBlood()" id="btnPumpAlveoli" class="px-3.5 py-1.5 rounded-lg bg-rose-700 hover:bg-rose-600 text-white font-semibold transition">▶ Flow Blood Stream</button>
  </div>
</div>
"""

# 15. animal_respiration_diversity_sim
simulators["animal_respiration_diversity_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.2.2 Evolutionary Spectrum</span>
      <h4 class="text-sm font-bold text-slate-100">Animal Kingdom Respiration: Gills, Skin & Spiracles</h4>
    </div>
    <div class="flex gap-1.5">
      <button onclick="window.switchAnimalRespTab('fish')" id="btnRespFish" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-cyan-500 text-slate-950 shadow-md">1. Fish (Gills)</button>
      <button onclick="window.switchAnimalRespTab('earthworm')" id="btnRespWorm" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">2. Earthworm (Skin)</button>
      <button onclick="window.switchAnimalRespTab('insect')" id="btnRespInsect" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">3. Insect (Spiracles)</button>
    </div>
  </div>

  <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg id="animalRespSvg" viewBox="0 0 500 220" class="w-full h-full">
      <g id="animalRespVisualGroup"></g>
    </svg>
    <div id="animalRespBadge" class="absolute bottom-2 left-3 bg-slate-900/85 border border-slate-700 text-xs px-3 py-1 rounded-lg text-cyan-300 font-mono">
      Fish Gills: Feathery filaments lined with capillary arches
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <p id="animalRespExpl" class="text-slate-300 text-xs leading-relaxed">
      <strong>Fish Gills:</strong> Water flows in through mouth and out through gill slits; feathery lamellae extract dissolved oxygen into blood.
    </p>
    <button onclick="window.animateAnimalResp()" id="btnAnimateResp" class="px-3.5 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-semibold transition shrink-0">▶ Animate Breathing</button>
  </div>
</div>
"""

# 16. frog_metamorphosis_ayurveda_sim
simulators["frog_metamorphosis_ayurveda_sim"] = """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/80 text-white select-none">
  <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
    <div class="flex items-center gap-2">
      <span class="px-2.5 py-1 bg-amber-500/20 text-amber-300 text-xs font-bold rounded-lg border border-amber-500/30">9.2.2 & Ancient Heritage</span>
      <h4 class="text-sm font-bold text-slate-100">Amphibian Versatility & Ayurveda's Jatharagni & Prana</h4>
    </div>
    <div class="flex gap-1.5">
      <button onclick="window.switchHeritageTab('frog')" id="btnHeritFrog" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md">Frog Triple Breathing</button>
      <button onclick="window.switchHeritageTab('ayurveda')" id="btnHeritAyur" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700">Ayurveda: Agni & Prana</button>
    </div>
  </div>

  <div class="relative w-full h-64 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg id="frogAyurSvg" viewBox="0 0 500 220" class="w-full h-full">
      <g id="frogAyurVisualGroup"></g>
    </svg>
    <div id="frogAyurBadge" class="absolute bottom-2 left-3 bg-slate-900/85 border border-slate-700 text-xs px-3 py-1 rounded-lg text-emerald-400 font-mono">
      Frog Mode: Adult on Land (Pulmonary Lungs + Buccal Pumping)
    </div>
  </div>

  <div class="mt-3 flex items-center justify-between gap-3 text-xs bg-slate-800/60 p-3 rounded-xl border border-slate-700/60">
    <p id="frogAyurExpl" class="text-slate-300 text-xs leading-relaxed">
      Frogs are the ultimate respiratory shapeshifters: young tadpoles breathe via gills, underwater adults breathe via moist skin, and land adults breathe via lungs and throat pumping!
    </p>
    <button onclick="window.actionFrogAyur()" id="btnActionFrogAyur" class="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold transition shrink-0">Toggle Habitat</button>
  </div>
</div>
"""

# Write out class7_science_life_processes_sims.py
with open(".agents/class7_science_life_processes_sims.py", "w", encoding="utf-8") as f:
    f.write('# -*- coding: utf-8 -*-\n"""Simulators HTML for Class 7 Science Chapter 9: Life Processes in Animals"""\n\nSIMULATORS_HTML = {\n')
    for k, v in simulators.items():
        f.write(f'    "{k}": r\'\'\'{v}\'\'\',\n')
    f.write('}\n')

print(f"Generated .agents/class7_science_life_processes_sims.py with {len(simulators)} simulators.")
