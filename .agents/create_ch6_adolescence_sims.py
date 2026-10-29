# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Science Chapter 6 Simulators HTML templates
Outputs .agents/class7_science_adolescence_sims.py
"""

import json

SIMULATORS_HTML = {
    # Sim 1: Growth Spurt & Epiphyseal Cartilage Explorer
    "growth_spurt_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">📈 Pubertal Growth Spurt Simulator</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.1 Growth</span>
    </div>
    <span id="growthAgeBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-mono font-bold">Age: 14 Years</span>
  </div>

  <!-- Growth Spurt SVG Visualization -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Height Measurement Grid / Stadiometer -->
      <line x1="50" y1="20" x2="50" y2="170" stroke="#475569" stroke-width="2"/>
      <line x1="45" y1="30" x2="50" y2="30" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="40" y="33" fill="#64748b" font-size="7" text-anchor="end">180 cm</text>
      <line x1="45" y1="70" x2="50" y2="70" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="40" y="73" fill="#64748b" font-size="7" text-anchor="end">150 cm</text>
      <line x1="45" y1="120" x2="50" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="40" y="123" fill="#64748b" font-size="7" text-anchor="end">120 cm</text>

      <!-- Male Silhouette Figure (Left) -->
      <g id="figureBoy" transform="translate(100, 40)" class="transition-all duration-300">
        <circle cx="20" cy="15" r="10" fill="#38bdf8"/>
        <!-- Torso & Limbs -->
        <path id="boyBodyPath" d="M 12,25 L 28,25 L 24,75 L 16,75 Z" fill="#0284c7"/>
        <line x1="17" y1="75" x2="15" y2="130" stroke="#0284c7" stroke-width="5" stroke-linecap="round"/>
        <line x1="23" y1="75" x2="25" y2="130" stroke="#0284c7" stroke-width="5" stroke-linecap="round"/>
        <text x="20" y="145" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">Boy</text>
        <text id="boyHeightTxt" x="20" y="156" fill="#94a3b8" font-size="8" text-anchor="middle">162 cm</text>
      </g>

      <!-- Female Silhouette Figure (Center) -->
      <g id="figureGirl" transform="translate(180, 45)" class="transition-all duration-300">
        <circle cx="20" cy="15" r="10" fill="#f43f5e"/>
        <!-- Torso & Limbs -->
        <path id="girlBodyPath" d="M 14,25 L 26,25 L 30,75 L 10,75 Z" fill="#e11d48"/>
        <line x1="17" y1="75" x2="16" y2="125" stroke="#e11d48" stroke-width="4.5" stroke-linecap="round"/>
        <line x1="23" y1="75" x2="24" y2="125" stroke="#e11d48" stroke-width="4.5" stroke-linecap="round"/>
        <text x="20" y="145" fill="#f43f5e" font-size="9" font-weight="bold" text-anchor="middle">Girl</text>
        <text id="girlHeightTxt" x="20" y="156" fill="#94a3b8" font-size="8" text-anchor="middle">158 cm</text>
      </g>

      <!-- Epiphyseal Growth Plate Long Bone Inset (Right) -->
      <g transform="translate(290, 25)">
        <rect x="0" y="0" width="130" height="145" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
        <text x="65" y="18" fill="#facc15" font-size="9" font-weight="bold" text-anchor="middle">Long Bone Anatomy</text>
        <!-- Femur bone head -->
        <path d="M 40,30 Q 65,22 90,30 L 75,70 L 55,70 Z" fill="#f1f5f9" stroke="#cbd5e1"/>
        <!-- Active Epiphyseal Cartilage Plate (Glowing blue) -->
        <rect id="growthPlateGlow" x="48" y="45" width="34" height="6" rx="2" fill="#38bdf8" class="animate-pulse"/>
        <text x="65" y="60" fill="#38bdf8" font-size="7" font-weight="bold" text-anchor="middle">Growth Plate</text>
        <!-- Bone shaft (Diaphysis) -->
        <rect x="55" y="70" width="20" height="60" fill="#f8fafc" stroke="#cbd5e1"/>
        <text x="65" y="138" fill="#94a3b8" font-size="7" text-anchor="middle">Epiphyseal Cartilage</text>
      </g>
    </svg>
  </div>

  <!-- Age Slider Controls -->
  <div class="flex items-center space-x-3">
    <span class="text-xs text-slate-400 font-mono">Select Age:</span>
    <input id="growthAgeSlider" type="range" min="10" max="19" value="14" class="flex-1 accent-amber-500 cursor-pointer"/>
    <span id="sliderValueDisplay" class="text-xs font-bold text-amber-400 font-mono w-14">14 Yrs</span>
  </div>

  <div id="growthInsightText" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    📈 <span class="font-bold text-amber-300">Growth Spurt Dynamics:</span> Girls typically start rapid height growth around age 10–12; boys accelerate around 12–14 and often surpass girls in height by age 18!
  </div>
</div>
""",

    # Sim 2: Secondary Sexual Characteristics Scanner
    "secondary_traits_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🧬 Secondary Sexual Characteristics</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.1 Somatic</span>
    </div>
    <span id="genderSelectBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-bold">Adolescent Male (♂)</span>
  </div>

  <!-- Somatic Scanner SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Interactive Figure Display -->
      <g id="figureContainer" transform="translate(180, 20)">
        <!-- Head -->
        <circle cx="40" cy="22" r="16" fill="#334155" stroke="#64748b"/>
        <!-- Facial Hair (Mustache) - shown for boy -->
        <path id="facialHair" d="M 32,25 Q 40,28 48,25" fill="none" stroke="#0f172a" stroke-width="2.5" class="transition-opacity duration-300"/>

        <!-- Neck & Adam's Apple protrusion -->
        <line x1="36" y1="38" x2="36" y2="48" stroke="#334155" stroke-width="3"/>
        <line x1="44" y1="38" x2="44" y2="48" stroke="#334155" stroke-width="3"/>
        <circle id="neckAdamsApple" cx="40" cy="43" r="3.5" fill="#38bdf8" class="transition-opacity duration-300"/>

        <!-- Torso & Shoulders -->
        <!-- Male Broad Shoulders Path -->
        <path id="maleTorso" d="M 10,48 L 70,48 L 56,115 L 24,115 Z" fill="#0284c7" class="transition-all duration-300"/>
        <!-- Female Broad Hips Path (hidden initially) -->
        <path id="femaleTorso" d="M 22,48 L 58,48 L 70,115 L 10,115 Z" fill="#e11d48" class="hidden transition-all duration-300"/>

        <!-- Breasts (Female only) -->
        <g id="femaleBreasts" class="hidden">
          <circle cx="30" cy="65" r="7" fill="#f43f5e"/>
          <circle cx="50" cy="65" r="7" fill="#f43f5e"/>
        </g>
      </g>

      <!-- Trait Checklist Callout Card (Right) -->
      <g id="traitCalloutCard" transform="translate(290, 25)">
        <rect x="0" y="0" width="135" height="140" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
        <text id="traitCardTitle" x="67" y="20" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Male Characteristics</text>
        <text id="trait1" x="10" y="42" fill="#cbd5e1" font-size="8">• Broad shoulders & chest</text>
        <text id="trait2" x="10" y="62" fill="#cbd5e1" font-size="8">• Protruding Adam's apple</text>
        <text id="trait3" x="10" y="82" fill="#cbd5e1" font-size="8">• Deepening voice pitch</text>
        <text id="trait4" x="10" y="102" fill="#cbd5e1" font-size="8">• Facial & underarm hair</text>
        <text id="trait5" x="10" y="122" fill="#cbd5e1" font-size="8">• Lean muscle mass surge</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2">
    <button id="btnSelectMaleTraits" class="p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>♂️ Adolescent Male Traits</span>
    </button>
    <button id="btnSelectFemaleTraits" class="p-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>♀️ Adolescent Female Traits</span>
    </button>
  </div>

  <div id="secondaryTraitsExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🧬 <span class="font-bold text-amber-300">Secondary Characteristics:</span> Distinguish the biological sexes without being direct reproductive organs. Driven by testosterone in boys and estrogen in girls!
  </div>
</div>
""",

    # Sim 3: Adam's Apple & Voice Acoustic Simulator
    "adams_apple_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🎙️ Larynx Expansion & Voice Pitch Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.1 Larynx</span>
    </div>
    <span id="voicePitchBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-mono font-bold">Pitch: 120 Hz (Baritone)</span>
  </div>

  <!-- Larynx Anatomical SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Neck Contour Outline -->
      <path d="M 120,20 Q 150,80 150,160 L 290,160 Q 290,80 320,20 Z" fill="#0f172a" stroke="#334155" stroke-width="2"/>

      <!-- Thyroid Cartilage Protrusion (Adam's Apple) -->
      <!-- Enlarges as slider moves -->
      <g id="larynxAssembly" transform="translate(195, 55)">
        <path id="thyroidCartilage" d="M 25,10 Q 45,25 25,60 Q -5,60 -5,25 Z" fill="#334155" stroke="#38bdf8" stroke-width="2" class="transition-all duration-300"/>
        
        <!-- Vocal Cords (Inside Larynx) -->
        <line id="vocalCordLeft" x1="10" y1="30" x2="25" y2="40" stroke="#f43f5e" stroke-width="3" class="transition-all duration-300"/>
        <line id="vocalCordRight" x1="10" y1="50" x2="25" y2="40" stroke="#f43f5e" stroke-width="3" class="transition-all duration-300"/>
        
        <text x="50" y="38" fill="#38bdf8" font-size="8" font-weight="bold">Adam's Apple</text>
      </g>

      <!-- Acoustic Oscilloscope Sound Wave (Bottom Right) -->
      <g transform="translate(270, 115)">
        <rect x="0" y="0" width="150" height="50" rx="6" fill="#020617" stroke="#1e293b"/>
        <path id="voiceWaveform" d="M 10,25 Q 25,5 40,25 T 70,25 T 100,25 T 130,25" fill="none" stroke="#22c55e" stroke-width="2"/>
        <text x="75" y="12" fill="#64748b" font-size="7" font-family="monospace" text-anchor="middle">ACOUSTIC FREQUENCY</text>
      </g>
    </svg>
  </div>

  <!-- Controls -->
  <div class="flex items-center space-x-3">
    <span class="text-xs text-slate-400 font-mono">Larynx Size:</span>
    <input id="larynxSizeSlider" type="range" min="1" max="5" value="4" class="flex-1 accent-amber-500 cursor-pointer"/>
    <button id="btnPlayVocalNote" class="px-3 py-1.5 rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition flex items-center space-x-1">
      <span>🔊 Test Voice Pitch</span>
    </button>
  </div>

  <div id="voiceExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🎙️ <span class="font-bold text-amber-300">Acoustic Physics:</span> As the larynx enlarges, vocal cords grow longer and thicker. Like thick cello strings, they vibrate at lower frequencies, producing a deeper adult voice!
  </div>
</div>
""",

    # Sim 4: Skin, Sweat & Sebaceous Gland Lab
    "skin_acne_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🔬 Skin Glands & Acne Genesis Lab</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.1 Cutaneous</span>
    </div>
    <span id="skinPoreStatusBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold">Clean Unclogged Pore</span>
  </div>

  <!-- Skin Cross Section SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Skin Layers: Epidermis (Top) & Dermis (Bottom) -->
      <rect x="40" y="40" width="360" height="25" fill="#fbcfe8" stroke="#f472b6" stroke-width="1.5"/>
      <text x="50" y="55" fill="#9d174d" font-size="8" font-weight="bold">Epidermis</text>
      <rect x="40" y="65" width="360" height="105" fill="#fed7aa" stroke="#fb923c" stroke-width="1.5"/>
      <text x="50" y="80" fill="#9a3412" font-size="8" font-weight="bold">Dermis</text>

      <!-- Central Hair Follicle Channel -->
      <path d="M 210,40 L 210,135 Q 220,150 230,135 L 230,40" fill="#fdf2f8" stroke="#ec4899" stroke-width="1.5"/>
      <!-- Hair Shaft emerging -->
      <line x1="220" y1="140" x2="220" y2="10" stroke="#1e293b" stroke-width="3"/>

      <!-- Sebaceous (Oil) Gland attached to follicle -->
      <path d="M 180,95 Q 165,115 185,125 Q 210,120 210,105 Z" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
      <text x="185" y="115" fill="#854d0e" font-size="7" font-weight="bold" text-anchor="middle">Oil Gland</text>

      <!-- Sudoriferous (Sweat) Gland Coiled Duct (Right) -->
      <path d="M 320,145 Q 310,125 325,115 Q 340,130 330,145 Z" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5"/>
      <path d="M 325,115 L 325,40" fill="none" stroke="#0284c7" stroke-width="2"/>
      <text x="325" y="160" fill="#0369a1" font-size="7" font-weight="bold" text-anchor="middle">Sweat Gland</text>

      <!-- Sebum Plug / Pimple Formation (Red inflamed swelling) -->
      <g id="pimpleInflammation" class="hidden">
        <!-- Inflamed bump on skin surface -->
        <ellipse cx="220" cy="40" rx="25" ry="12" fill="#ef4444" opacity="0.8"/>
        <!-- Yellow Sebum/Pus Core -->
        <circle cx="220" cy="42" r="5" fill="#facc15"/>
        <text x="220" y="28" fill="#ef4444" font-size="9" font-weight="bold" text-anchor="middle">PIMPLE / ACNE</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2">
    <button id="btnSurgeHormoneSebum" class="p-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>⚡ Pubertal Sebum Surge (Clog Pore)</span>
    </button>
    <button id="btnCleanseFace" class="p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>🧼 Wash Gently with Soap & Water</span>
    </button>
  </div>

  <div id="skinAcneExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🔬 <span class="font-bold text-amber-300">Sebum Dynamics:</span> Hormones trigger sebaceous glands to overproduce oil. When pores plug with sebum and dead cells, acne forms. Never squeeze pimples; gentle washing cleans pores safely!
  </div>
</div>
""",

    # Sim 5: Menstrual Cycle Biological Clock (28-Day Cadence)
    "menstrual_cycle_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🗓️ The 28-Day Menstrual Cycle Clock</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.2 Reproduction</span>
    </div>
    <span id="cyclePhaseBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-rose-400 font-mono font-bold">Days 1–5: Menstruation</span>
  </div>

  <!-- 28-Day Cycle Dial & Uterus SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- 28-Day Circular Clock Dial (Left) -->
      <g transform="translate(120, 95)">
        <!-- Outer Track Circle -->
        <circle cx="0" cy="0" r="65" fill="#0f172a" stroke="#334155" stroke-width="4"/>
        
        <!-- Phase Wedges: Days 1-5 (Menstruation - Red) -->
        <path d="M 0,0 L 0,-65 A 65,65 0 0,1 58,-30 Z" fill="#ef4444" opacity="0.6"/>
        <text x="25" y="-45" fill="#fecaca" font-size="7" font-weight="bold">Days 1-5</text>

        <!-- Days 6-13 (Follicular - Blue) -->
        <path d="M 0,0 L 58,-30 A 65,65 0 0,1 64,10 Z" fill="#38bdf8" opacity="0.5"/>
        <text x="50" y="-5" fill="#bae6fd" font-size="7" font-weight="bold">6-13</text>

        <!-- Day 14 (Ovulation - Gold Star) -->
        <circle cx="64" cy="15" r="5" fill="#facc15" stroke="#eab308"/>
        <text x="50" y="30" fill="#fde047" font-size="8" font-weight="bold">Day 14 Ovulation</text>

        <!-- Days 15-28 (Luteal Phase - Purple) -->
        <path d="M 0,0 L 64,15 A 65,65 0 0,1 0,-65 Z" fill="#a855f7" opacity="0.4"/>
        
        <!-- Rotating Hand Arrow indicating Day -->
        <line id="cycleHand" x1="0" y1="0" x2="0" y2="-55" stroke="#f8fafc" stroke-width="3" stroke-linecap="round" class="transition-transform duration-500 origin-center"/>
        <circle cx="0" cy="0" r="5" fill="#f8fafc"/>
      </g>

      <!-- Uterine Endometrium Thickness Display (Right) -->
      <g transform="translate(250, 30)">
        <rect x="0" y="0" width="160" height="130" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
        <text x="80" y="20" fill="#f43f5e" font-size="10" font-weight="bold" text-anchor="middle">Uterine Lining (Endometrium)</text>
        
        <!-- Uterine Wall Muscle Base -->
        <rect x="15" y="40" width="130" height="15" fill="#7f1d1d"/>
        <text x="80" y="52" fill="#fca5a5" font-size="7" text-anchor="middle">Myometrium Muscle</text>

        <!-- Spongy Endometrium Layer (Height changes with phase) -->
        <rect id="endometriumLining" x="15" y="55" width="130" height="12" fill="#f43f5e" class="transition-all duration-500"/>
        
        <!-- Status Label Inside Display -->
        <text id="endometriumDesc" x="80" y="95" fill="#cbd5e1" font-size="8" text-anchor="middle">Lining sheds during menstruation</text>
        <text id="ovumStatus" x="80" y="115" fill="#facc15" font-size="8" font-weight="bold" text-anchor="middle">Ovum maturing in ovary</text>
      </g>
    </svg>
  </div>

  <!-- Day Selection Buttons -->
  <div class="grid grid-cols-4 gap-1.5 text-xs">
    <button class="cycle-day-btn p-2 rounded-xl bg-rose-600 text-white font-bold" data-phase="menstruation">Days 1–5: Menstruation</button>
    <button class="cycle-day-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-phase="follicular">Days 6–13: Follicular</button>
    <button class="cycle-day-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-phase="ovulation">Day 14: Ovulation</button>
    <button class="cycle-day-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-phase="luteal">Days 15–28: Luteal</button>
  </div>

  <div id="cycleExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🗓️ <span class="font-bold text-amber-300">Menarche & Biological Health:</span> Menstruation is an indicator of healthy reproductive maturation. The uterine lining prepares for potential pregnancy every month and naturally sheds when unfertilized!
  </div>
</div>
""",

    # Sim 6: Myth-Buster: Breaking Taboos Around Menstruation
    "myth_buster_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">💡 Myth-Buster: Science vs Taboos</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.2 Social Dignity</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold">Fact vs Fiction</span>
  </div>

  <!-- Interactive Myth Card Flip Chamber -->
  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 bg-slate-950 p-3 rounded-xl border border-slate-800 min-h-44">
    <!-- Myth Card (Left) -->
    <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/40 flex flex-col justify-between">
      <div>
        <div class="flex items-center space-x-1.5 text-xs font-bold text-rose-400 mb-2">
          <span>❌</span> <span>Superstitious Social Myth</span>
        </div>
        <p id="mythText" class="text-xs text-rose-200 font-semibold leading-relaxed">
          "Menstruating girls are 'impure' and will spoil food or pickles if they enter the kitchen."
        </p>
      </div>
      <span class="text-[10px] text-rose-400/80 font-mono mt-2">DEBUNKED BY BIOLOGY</span>
    </div>

    <!-- Science Truth Card (Right) -->
    <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-500/40 flex flex-col justify-between">
      <div>
        <div class="flex items-center space-x-1.5 text-xs font-bold text-emerald-400 mb-2">
          <span>✅</span> <span>Proven Scientific Truth</span>
        </div>
        <p id="truthText" class="text-xs text-emerald-200 font-semibold leading-relaxed">
          Menstrual fluid is clean blood and shed uterine tissue—identical to blood circulating through veins. Food spoilage is caused strictly by micro-organisms, never by human touch!
        </p>
      </div>
      <span class="text-[10px] text-emerald-400/80 font-mono mt-2">MEDICAL CONSENSUS</span>
    </div>
  </div>

  <!-- Myth Navigation Buttons -->
  <div class="grid grid-cols-3 gap-2 text-xs">
    <button class="myth-select-btn p-2 rounded-xl bg-amber-600 text-white font-bold" data-idx="0">1. Touching Food</button>
    <button class="myth-select-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-idx="1">2. Playing Sports</button>
    <button class="myth-select-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-idx="2">3. Social Isolation</button>
  </div>

  <div id="mythBusterNote" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🌟 <span class="font-bold text-amber-300">Dignity & Science:</span> Breaking taboos requires education, empathy, and open conversation. Girls can study, play, cook, and thrive during their periods!
  </div>
</div>
""",

    # Sim 7: Emotional Landscape & Mood Regulation Simulator
    "emotional_landscape_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🧠 Teen Brain & Mood Regulation</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.3 Psychology</span>
    </div>
    <span id="brainStateBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 font-bold">Emotion Surge (Amygdala)</span>
  </div>

  <!-- Teen Brain Anatomy SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Human Head Profile Contour -->
      <path d="M 120,170 L 120,110 Q 110,60 160,30 Q 220,15 280,30 Q 320,60 320,110 Q 315,140 330,150 L 320,170" fill="none" stroke="#475569" stroke-width="2"/>

      <!-- Brain Cerebrum Contour -->
      <path d="M 145,110 Q 140,50 190,35 Q 260,30 295,60 Q 310,95 295,125 Q 260,135 220,135 Q 160,140 145,110 Z" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>

      <!-- Prefrontal Cortex (Frontal Lobe - Rational Thought - Blue) -->
      <path id="pfcZone" d="M 148,105 Q 145,60 185,45 L 185,125 Z" fill="#38bdf8" opacity="0.3" class="transition-opacity duration-500"/>
      <text x="165" y="85" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Prefrontal Cortex</text>
      <text x="165" y="96" fill="#94a3b8" font-size="6" text-anchor="middle">(Maturing)</text>

      <!-- Amygdala (Emotional Core - Red/Orange) -->
      <circle id="amygdalaGlow" cx="225" cy="100" r="14" fill="#f43f5e" opacity="0.8" class="animate-pulse"/>
      <text x="225" y="103" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Amygdala</text>
      <text x="225" y="125" fill="#f43f5e" font-size="7" font-weight="bold" text-anchor="middle">Emotion Hub</text>

      <!-- Scenario Box (Right) -->
      <g transform="translate(260, 45)">
        <rect x="0" y="0" width="165" height="100" rx="6" fill="#0f172a" stroke="#334155"/>
        <text id="scenarioTitle" x="82" y="20" fill="#facc15" font-size="9" font-weight="bold" text-anchor="middle">Conflict Scenario</text>
        <text id="scenarioText" x="10" y="40" fill="#cbd5e1" font-size="8">Friend teased your hair in public.</text>
        <text id="scenarioReaction" x="10" y="65" fill="#f43f5e" font-size="8">Impulsive: Shout & slam door!</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2">
    <button id="btnReactImpulsive" class="p-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>⚡ Impulsive Reaction (Amygdala)</span>
    </button>
    <button id="btnPauseReflect" class="p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow flex items-center justify-center space-x-1">
      <span>⏸️ Pause & Reflect (Prefrontal Cortex)</span>
    </button>
  </div>

  <div id="emotionalInsight" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🧠 <span class="font-bold text-amber-300">Neuroscience of Teens:</span> The amygdala (emotion hub) reacts quickly, while the prefrontal cortex (planning and self-control) is still developing. Pausing for 5 seconds helps rational thinking take over!
  </div>
</div>
""",

    # Sim 8: Nutritional MyPlate Builder
    "nutrition_plate_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🥗 Adolescent Nutrition: Balanced MyPlate</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.4.1 Diet</span>
    </div>
    <span id="plateBalanceBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 font-bold">Plate Status: Empty</span>
  </div>

  <!-- Interactive Plate SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Round Dinner Plate Rim -->
      <circle cx="160" cy="95" r="75" fill="#1e293b" stroke="#475569" stroke-width="4"/>
      <circle cx="160" cy="95" r="70" fill="#0f172a"/>

      <!-- Plate Quadrants (Toggled by user) -->
      <!-- Quadrant 1: Complex Carbs (Top-Left - Gold) -->
      <path id="quadCarbs" d="M 160,95 L 90,95 A 70,70 0 0,1 160,25 Z" fill="#f59e0b" class="opacity-0 transition-opacity duration-300"/>
      <text x="130" y="65" fill="#fef3c7" font-size="8" font-weight="bold" text-anchor="middle">Carbs</text>

      <!-- Quadrant 2: Proteins (Top-Right - Purple) -->
      <path id="quadProteins" d="M 160,95 L 160,25 A 70,70 0 0,1 230,95 Z" fill="#a855f7" class="opacity-0 transition-opacity duration-300"/>
      <text x="190" y="65" fill="#f3e8ff" font-size="8" font-weight="bold" text-anchor="middle">Protein</text>

      <!-- Quadrant 3: Leafy Greens & Iron (Bottom-Left - Emerald) -->
      <path id="quadGreens" d="M 160,95 L 90,95 A 70,70 0 0,0 160,165 Z" fill="#10b981" class="opacity-0 transition-opacity duration-300"/>
      <text x="130" y="135" fill="#d1fae5" font-size="8" font-weight="bold" text-anchor="middle">Greens (Fe)</text>

      <!-- Quadrant 4: Dairy / Calcium & Fruits (Bottom-Right - Cyan) -->
      <path id="quadDairy" d="M 160,95 L 230,95 A 70,70 0 0,1 160,165 Z" fill="#06b6d4" class="opacity-0 transition-opacity duration-300"/>
      <text x="190" y="135" fill="#cffafe" font-size="8" font-weight="bold" text-anchor="middle">Dairy (Ca)</text>

      <!-- Nutrient Score Card (Right) -->
      <g transform="translate(260, 25)">
        <rect x="0" y="0" width="165" height="140" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
        <text x="82" y="20" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">Nutrient Check</text>
        <text id="nutriProtein" x="15" y="45" fill="#64748b" font-size="8">❌ Proteins (Tissue Growth)</text>
        <text id="nutriIron" x="15" y="65" fill="#64748b" font-size="8">❌ Iron (Hemoglobin/Blood)</text>
        <text id="nutriCalcium" x="15" y="85" fill="#64748b" font-size="8">❌ Calcium (Peak Bone Mass)</text>
        <text id="nutriCarbs" x="15" y="105" fill="#64748b" font-size="8">❌ Complex Carbohydrates</text>
        <text id="nutriVerdict" x="82" y="128" fill="#ef4444" font-size="8" font-weight="bold" text-anchor="middle">Incomplete Nutrition</text>
      </g>
    </svg>
  </div>

  <!-- Food Addition Pills -->
  <div class="grid grid-cols-4 gap-1.5 text-xs">
    <button class="nutri-add-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-food="carbs">🌾 Roti/Rice</button>
    <button class="nutri-add-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-food="protein">🫘 Dal/Eggs</button>
    <button class="nutri-add-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-food="greens">🥬 Spinach (Fe)</button>
    <button class="nutri-add-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-food="dairy">🥛 Milk/Curd (Ca)</button>
  </div>

  <div id="nutritionExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🥗 <span class="font-bold text-amber-300">Adolescent Fuel:</span> Rapid growth demands proteins for tissue repair, calcium for bone density, and dietary iron to synthesize hemoglobin and prevent anemia!
  </div>
</div>
""",

    # Sim 9: Personal & Menstrual Hygiene Protocol
    "hygiene_protocol_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🧼 Personal & Menstrual Hygiene Protocol</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.4.2 Hygiene</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold">Health Protocols</span>
  </div>

  <!-- Hygiene Checklist Station SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Step 1: Daily Bathing -->
      <g transform="translate(40, 30)">
        <rect x="0" y="0" width="105" height="135" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="52" y="20" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">1. Daily Bathing</text>
        <circle cx="52" cy="50" r="18" fill="#0284c7"/>
        <text x="52" y="55" fill="#ffffff" font-size="14" text-anchor="middle">🚿</text>
        <text x="10" y="85" fill="#cbd5e1" font-size="7">• Cleans hyperactive sweat</text>
        <text x="10" y="98" fill="#cbd5e1" font-size="7">• Washes excess sebum oil</text>
        <text x="10" y="112" fill="#cbd5e1" font-size="7">• Eliminates body odor</text>
      </g>

      <!-- Step 2: Sanitary Pad Frequency -->
      <g transform="translate(165, 30)">
        <rect x="0" y="0" width="110" height="135" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
        <text x="55" y="20" fill="#f43f5e" font-size="9" font-weight="bold" text-anchor="middle">2. Pad Exchange</text>
        <circle cx="55" cy="50" r="18" fill="#be123c"/>
        <text x="55" y="55" fill="#ffffff" font-size="14" text-anchor="middle">⏱️</text>
        <text x="10" y="85" fill="#cbd5e1" font-size="7">• Change every 4–6 hrs</text>
        <text x="10" y="98" fill="#cbd5e1" font-size="7">• Prevents bacterial growth</text>
        <text x="10" y="112" fill="#cbd5e1" font-size="7">• Protects from infections</text>
      </g>

      <!-- Step 3: Proper Disposal -->
      <g transform="translate(295, 30)">
        <rect x="0" y="0" width="105" height="135" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
        <text x="52" y="20" fill="#10b981" font-size="9" font-weight="bold" text-anchor="middle">3. Paper Disposal</text>
        <circle cx="52" cy="50" r="18" fill="#047857"/>
        <text x="52" y="55" fill="#ffffff" font-size="14" text-anchor="middle">🗑️</text>
        <text x="10" y="85" fill="#cbd5e1" font-size="7">• Wrap securely in paper</text>
        <text x="10" y="98" fill="#cbd5e1" font-size="7">• Discard in waste bin</text>
        <text x="10" y="112" fill="#cbd5e1" font-size="7">• NEVER flush in toilets!</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2 text-xs">
    <button id="btnGovtSchemes" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-300 font-bold border border-slate-700 transition">
      🏛️ Learn about MHS & RKSK Schemes
    </button>
    <button id="btnDisposalRules" class="p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-cyan-300 font-bold border border-slate-700 transition">
      🚯 Why Never Flush Sanitary Pads?
    </button>
  </div>

  <div id="hygieneExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🧼 <span class="font-bold text-amber-300">Hygiene Safeguards:</span> Changing pads every 4 to 6 hours and wrapping them in paper prevents reproductive tract infections and protects environmental sanitation!
  </div>
</div>
""",

    # Sim 10: Physical Activity, Fitness & Endorphin Surge
    "physical_activity_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🏃 Physical Fitness & Endorphin Surge</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.4.3 Stamina</span>
    </div>
    <span id="endorphinBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-bold">Resting State</span>
  </div>

  <!-- Fitness SVG Dashboard -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Activity Character (Left) -->
      <g id="runnerAthlete" transform="translate(90, 40)" class="transition-transform duration-300">
        <!-- Head -->
        <circle cx="30" cy="20" r="12" fill="#f59e0b"/>
        <!-- Dynamic Running Body -->
        <path d="M 30,32 L 35,70 L 15,100" fill="none" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
        <line x1="35" y1="70" x2="55" y2="100" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
        <!-- Arms in motion -->
        <line x1="30" y1="40" x2="10" y2="60" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
        <line x1="30" y1="40" x2="50" y2="55" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
        <text x="30" y="130" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">60 Mins Activity</text>
      </g>

      <!-- Biochemical Endorphin & Heart Rate Graph (Right) -->
      <g transform="translate(200, 30)">
        <rect x="0" y="0" width="210" height="135" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
        <text x="105" y="20" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">Neurotransmitter & Vigor Gauge</text>
        
        <!-- Stamina Meter Bar -->
        <text x="15" y="45" fill="#cbd5e1" font-size="8">Cardiovascular Stamina</text>
        <rect x="15" y="52" width="180" height="10" rx="3" fill="#334155"/>
        <rect id="staminaBar" x="15" y="52" width="50" height="10" rx="3" fill="#10b981" class="transition-all duration-500"/>

        <!-- Endorphin Happiness Surge Bar -->
        <text x="15" y="80" fill="#cbd5e1" font-size="8">Brain Endorphin Level (Mood Boost)</text>
        <rect x="15" y="87" width="180" height="10" rx="3" fill="#334155"/>
        <rect id="endorphinBar" x="15" y="87" width="40" height="10" rx="3" fill="#f43f5e" class="transition-all duration-500"/>

        <!-- Bone Mineralization Bar -->
        <text x="15" y="115" fill="#cbd5e1" font-size="8">Peak Bone Mineralization (Calcium)</text>
        <rect x="15" y="122" width="180" height="10" rx="3" fill="#334155"/>
        <rect id="boneBar" x="15" y="122" width="60" height="10" rx="3" fill="#38bdf8" class="transition-all duration-500"/>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-3 gap-2 text-xs">
    <button class="activity-btn p-2 rounded-xl bg-amber-600 text-white font-bold" data-level="run">🏃 Brisk Sports (60m)</button>
    <button class="activity-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-level="yoga">🧘 Yoga & Asanas</button>
    <button class="activity-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-level="sedentary">🛋️ Sedentary Screens</button>
  </div>

  <div id="activityExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🏃 <span class="font-bold text-amber-300">Endorphin Rush:</span> 60 minutes of active sports builds peak bone mass, trains the heart muscle, and stimulates the brain to release natural mood-elevating endorphins!
  </div>
</div>
""",

    # Sim 11: Balanced Social Life & Cyber Safety Shield
    "digital_safety_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🛡️ Cyber Safety & Digital Boundaries</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.4.4 Social</span>
    </div>
    <span id="privacyStatusBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold">Privacy Shield: ACTIVE</span>
  </div>

  <!-- Interactive Cyber Safety Terminal SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Smartphone Screen Frame -->
      <g transform="translate(60, 15)">
        <rect x="0" y="0" width="95" height="160" rx="12" fill="#1e293b" stroke="#475569" stroke-width="3"/>
        <rect x="5" y="10" width="85" height="140" rx="6" fill="#020617"/>
        <circle cx="47" cy="6" r="2" fill="#94a3b8"/>
        <!-- Social Message Bubbles on Phone -->
        <rect x="10" y="25" width="65" height="18" rx="4" fill="#0284c7"/>
        <text x="42" y="37" fill="#ffffff" font-size="7" text-anchor="middle">Friend message</text>
        <rect id="bullyMessageBubble" x="10" y="55" width="75" height="22" rx="4" fill="#be123c" class="hidden animate-pulse"/>
        <text id="bullyText" x="47" y="69" fill="#fecaca" font-size="6" font-weight="bold" text-anchor="middle" class="hidden">Teasing / Mockery!</text>
      </g>

      <!-- Cyber Shield Wall (Center-Right) -->
      <g transform="translate(200, 25)">
        <rect x="0" y="0" width="200" height="140" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="100" y="20" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Safety Protocol Checklist</text>
        <text x="15" y="45" fill="#cbd5e1" font-size="8">🔒 Keep profile strictly private</text>
        <text x="15" y="68" fill="#cbd5e1" font-size="8">🚫 Never share passwords or home address</text>
        <text x="15" y="91" fill="#cbd5e1" font-size="8">🛑 Block bullies & take screenshots</text>
        <text x="15" y="114" fill="#cbd5e1" font-size="8">🗣️ Tell trusted parents/teachers immediately</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2 text-xs">
    <button id="btnSimulateCyberThreat" class="p-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold transition shadow flex items-center justify-center space-x-1">
      <span>⚠️ Simulate Cyberbullying Threat</span>
    </button>
    <button id="btnDeploySafetyShield" class="p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold transition shadow flex items-center justify-center space-x-1">
      <span>🛡️ Block, Preserve Evidence & Report</span>
    </button>
  </div>

  <div id="cyberSafetyExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🛡️ <span class="font-bold text-amber-300">Digital Armor:</span> Never suffer in silence. If anyone harasses you online, never retaliate aggressively; screenshot the evidence, block the sender, and inform a trusted adult immediately!
  </div>
</div>
""",

    # Sim 12: Say NO! Peer Pressure Assertiveness Simulator
    "say_no_assertiveness_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🛑 Peer Pressure: Learn to Say 'NO!'</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.4.5 Assertiveness</span>
    </div>
    <span id="assertivenessBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 font-bold">Scenario Encounter</span>
  </div>

  <!-- Peer Encounter Dialogue Tree SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Peer Offering Cigarette / Vape (Left) -->
      <g transform="translate(80, 50)">
        <circle cx="20" cy="15" r="12" fill="#64748b"/>
        <line x1="20" y1="27" x2="20" y2="80" stroke="#64748b" stroke-width="4"/>
        <line x1="20" y1="45" x2="50" y2="55" stroke="#64748b" stroke-width="3"/>
        <!-- Cigarette in hand -->
        <line x1="50" y1="55" x2="65" y2="52" stroke="#f8fafc" stroke-width="2"/>
        <circle cx="65" cy="52" r="1.5" fill="#ef4444"/>
        <text x="20" y="105" fill="#94a3b8" font-size="8" text-anchor="middle">Pressuring Peer</text>
      </g>

      <!-- Speech Bubble from Peer -->
      <g transform="translate(140, 25)">
        <rect x="0" y="0" width="130" height="40" rx="6" fill="#1e293b" stroke="#f43f5e"/>
        <text x="65" y="16" fill="#fecaca" font-size="7" font-weight="bold" text-anchor="middle">"Just take one puff!"</text>
        <text x="65" y="28" fill="#fca5a5" font-size="7" text-anchor="middle">"Don't be a baby, everyone does it."</text>
      </g>

      <!-- Empowered Adolescent Standing Firm (Right) -->
      <g id="empoweredAdolescent" transform="translate(320, 50)">
        <circle cx="20" cy="15" r="12" fill="#38bdf8"/>
        <line x1="20" y1="27" x2="20" y2="80" stroke="#0284c7" stroke-width="4"/>
        <!-- Hand held up in 'Stop' gesture -->
        <line x1="20" y1="40" x2="-5" y2="35" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
        <line x1="-5" y1="35" x2="-5" y2="25" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
        <text x="20" y="105" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">YOU (Empowered)</text>
      </g>

      <!-- Response Speech Bubble from You -->
      <g id="responseBubble" transform="translate(230, 115)" class="hidden">
        <rect x="0" y="0" width="180" height="35" rx="6" fill="#065f46" stroke="#10b981"/>
        <text id="responseText" x="90" y="16" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">"No thanks, I care about my health."</text>
        <text x="90" y="28" fill="#a7f3d0" font-size="7" text-anchor="middle">Firm eye contact • Walk away</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-3 gap-1.5 text-xs">
    <button class="refuse-btn p-2 rounded-xl bg-emerald-600 text-white font-bold" data-action="firm_no">1. Firm 'No Thanks'</button>
    <button class="refuse-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-action="reason">2. Give Health Reason</button>
    <button class="refuse-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-action="walk_away">3. Walk Away Calmly</button>
  </div>

  <div id="sayNoExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🛑 <span class="font-bold text-amber-300">Refusal Power:</span> You never owe anyone an excuse for protecting your body. True friends will always respect your boundaries!
  </div>
</div>
""",

    # Sim 13: Physiological Havoc: Tobacco, Alcohol & Drugs Scanner
    "body_damage_scanner_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🩻 Substance Abuse Pathology Scanner</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.4.5 Pathology</span>
    </div>
    <span id="toxinScanBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-rose-400 font-bold">Tobacco (Tar & Nicotine)</span>
  </div>

  <!-- Internal Organ Pathology SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Human Body Silhouette -->
      <g transform="translate(90, 20)">
        <circle cx="40" cy="18" r="14" fill="#334155"/>
        <path d="M 26,34 L 54,34 L 48,110 L 32,110 Z" fill="#475569"/>
        
        <!-- Lungs (Affected by Tobacco) -->
        <ellipse id="scanLungLeft" cx="33" cy="55" rx="8" ry="14" fill="#0f172a" stroke="#ef4444" stroke-width="1.5" class="transition-all duration-300"/>
        <ellipse id="scanLungRight" cx="47" cy="55" rx="8" ry="14" fill="#0f172a" stroke="#ef4444" stroke-width="1.5" class="transition-all duration-300"/>

        <!-- Liver (Affected by Alcohol) -->
        <path id="scanLiver" d="M 33,78 Q 45,74 52,82 Q 40,88 33,78 Z" fill="#7f1d1d" stroke="#ef4444" class="opacity-30 transition-all duration-300"/>

        <!-- Brain Reward Circuit (Affected by Drugs) -->
        <circle id="scanBrain" cx="40" cy="18" r="6" fill="#a855f7" class="opacity-30 transition-all duration-300"/>
      </g>

      <!-- Organ Damage Description Card (Right) -->
      <g transform="translate(190, 25)">
        <rect x="0" y="0" width="220" height="140" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
        <text id="organScanTitle" x="110" y="22" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">Tobacco Smoke Pathology</text>
        <text id="organDmg1" x="15" y="45" fill="#fca5a5" font-size="8">• 7,000+ toxic chemicals coat lung alveoli</text>
        <text id="organDmg2" x="15" y="65" fill="#fca5a5" font-size="8">• Black carcinogenic tar destroys elasticity</text>
        <text id="organDmg3" x="15" y="85" fill="#fca5a5" font-size="8">• Nicotine addiction traps brain dopamine</text>
        <text id="organDmg4" x="15" y="105" fill="#fca5a5" font-size="8">• Triggers chronic bronchitis & lung cancer</text>
        <text id="organRecovery" x="110" y="128" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">Zero Consumption = 100% Clean Organs</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-3 gap-2 text-xs">
    <button class="toxin-btn p-2 rounded-xl bg-rose-600 text-white font-bold" data-toxin="tobacco">🚬 Tobacco (Lungs)</button>
    <button class="toxin-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-toxin="alcohol">🍷 Alcohol (Liver)</button>
    <button class="toxin-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700" data-toxin="drugs">💊 Narcotics (Brain)</button>
  </div>

  <div id="pathologyExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🩻 <span class="font-bold text-amber-300">Internal Truth:</span> Tobacco tar physically blackens alveoli air sacs, permanently reducing oxygen transfer. Staying completely substance-free preserves vibrant, peak organ function!
  </div>
</div>
""",

    # Sim 14: The Endocrine Master Switchboard: Pituitary Gland & Hormones
    "pituitary_endocrine_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🧠 The Endocrine Master Switchboard</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.5 Hormones</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-400 font-bold">Pituitary Signals</span>
  </div>

  <!-- Endocrine Switchboard SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Master Gland (Pituitary) in Brain (Top Center) -->
      <g transform="translate(180, 20)">
        <rect x="0" y="0" width="80" height="35" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
        <text x="40" y="15" fill="#facc15" font-size="8" font-weight="bold" text-anchor="middle">Pituitary Gland</text>
        <text x="40" y="26" fill="#94a3b8" font-size="7" text-anchor="middle">(Master Gland)</text>
      </g>

      <!-- Bloodstream Arterial Pathways (Pulsing Arrows) -->
      <!-- Left Pathway to Testes / Adrenals -->
      <path d="M 190,55 L 100,105 L 100,135" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4 2"/>
      <!-- Right Pathway to Ovaries / Thyroid -->
      <path d="M 250,55 L 340,105 L 340,135" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4 2"/>

      <!-- Target 1: Male Testes (Left) -->
      <g transform="translate(60, 135)">
        <rect x="0" y="0" width="80" height="40" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="40" y="16" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">Testes (♂)</text>
        <text x="40" y="30" fill="#cbd5e1" font-size="7" text-anchor="middle">Testosterone</text>
      </g>

      <!-- Target 2: Female Ovaries (Right) -->
      <g transform="translate(300, 135)">
        <rect x="0" y="0" width="80" height="40" rx="6" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
        <text x="40" y="16" fill="#f43f5e" font-size="8" font-weight="bold" text-anchor="middle">Ovaries (♀)</text>
        <text x="40" y="30" fill="#cbd5e1" font-size="7" text-anchor="middle">Estrogen</text>
      </g>

      <!-- Central Blood Vessel Stream Animation -->
      <g id="circulatingHormoneDots">
        <circle cx="150" cy="75" r="3" fill="#facc15" class="animate-ping"/>
        <circle cx="290" cy="75" r="3" fill="#facc15" class="animate-ping"/>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2 text-xs">
    <button id="btnReleaseLH_FSH" class="p-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold transition shadow">
      ⚡ Pulse Pituitary Gonadotropins (LH / FSH)
    </button>
    <button id="btnReleaseGH" class="p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold transition shadow">
      🦴 Pulse Growth Hormone (GH Elongation)
    </button>
  </div>

  <div id="pituitaryExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🧠 <span class="font-bold text-amber-300">Ductless Glands:</span> Endocrine glands lack pipes or ducts. They pour biochemical messengers (hormones) directly into the bloodstream, reaching precise target cell receptors across the body!
  </div>
</div>
""",

    # Sim 15: Hormone Feedback Loops: Testosterone & Estrogen
    "hormone_feedback_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🔄 Sex Hormone Biological Feedback Dial</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">6.5 Gonadal</span>
    </div>
    <span id="feedbackDialBadge" class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-400 font-bold">Active Hormone: Testosterone</span>
  </div>

  <!-- Feedback Loop Dashboard SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- Dial Gauge Arc (Left) -->
      <g transform="translate(130, 110)">
        <path d="M -60,0 A 60,60 0 0,1 60,0" fill="none" stroke="#334155" stroke-width="12"/>
        <path id="dialArcActive" d="M -60,0 A 60,60 0 0,1 20,-56" fill="none" stroke="#38bdf8" stroke-width="12" class="transition-all duration-500"/>
        
        <!-- Needle Indicator -->
        <line id="dialNeedle" x1="0" y1="0" x2="20" y2="-45" stroke="#f8fafc" stroke-width="3" stroke-linecap="round" class="transition-all duration-500"/>
        <circle cx="0" cy="0" r="6" fill="#f8fafc"/>
        <text x="0" y="20" fill="#94a3b8" font-size="8" text-anchor="middle">Hormone Concentration</text>
      </g>

      <!-- Target Organ Response Card (Right) -->
      <g transform="translate(230, 25)">
        <rect x="0" y="0" width="190" height="140" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
        <text id="respCardTitle" x="95" y="20" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">Testosterone Biological Impact</text>
        <text id="resp1" x="15" y="45" fill="#cbd5e1" font-size="8">• Stimulates testicular sperm production</text>
        <text id="resp2" x="15" y="65" fill="#cbd5e1" font-size="8">• Enforces voice deepening via larynx</text>
        <text id="resp3" x="15" y="85" fill="#cbd5e1" font-size="8">• Drives facial, chest & pubic hair growth</text>
        <text id="resp4" x="15" y="105" fill="#cbd5e1" font-size="8">• Enhances protein synthesis in muscles</text>
        <text id="resp5" x="15" y="125" fill="#38bdf8" font-size="8" font-weight="bold">• Negative feedback regulates pituitary</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2 text-xs">
    <button id="btnSwitchTestosterone" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold transition shadow">
      ♂️ Testosterone Feedback Loop
    </button>
    <button id="btnSwitchEstrogen" class="p-2.5 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold transition border border-slate-700">
      ♀️ Estrogen & Progesterone Loop
    </button>
  </div>

  <div id="feedbackExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    🔄 <span class="font-bold text-amber-300">Feedback Loop:</span> When sex hormone levels rise in the blood, they signal the pituitary gland to reduce gonadotropin secretion, maintaining healthy homeostasis!
  </div>
</div>
""",

    # Sim 16: Ancient Indian Heritage: Ayurveda & Kishoravastha
    "ayurveda_heritage_sim": r"""
<div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col space-y-3">
  <div class="flex items-center justify-between">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">🏛️ Ancient Indian Heritage: Kishoravastha</span>
      <span class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">Ayurveda</span>
    </div>
    <span class="text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-400 font-bold">Sapta Dhatu Science</span>
  </div>

  <!-- Sapta Dhatu Evolutionary Ladder SVG -->
  <div class="relative w-full h-52 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
    <svg viewBox="0 0 440 190" class="w-full h-full">
      <!-- 7 Sequential Dhatu Vessels / Steps -->
      <!-- 1. Rasa (Plasma) -->
      <g transform="translate(20, 110)">
        <circle cx="20" cy="20" r="16" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="20" y="24" fill="#38bdf8" font-size="7" font-weight="bold" text-anchor="middle">Rasa</text>
        <text x="20" y="48" fill="#94a3b8" font-size="6" text-anchor="middle">Plasma</text>
      </g>
      <line x1="56" y1="130" x2="74" y2="130" stroke="#f59e0b" stroke-width="2"/>

      <!-- 2. Rakta (Blood) -->
      <g transform="translate(80, 110)">
        <circle cx="20" cy="20" r="16" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
        <text x="20" y="24" fill="#ef4444" font-size="7" font-weight="bold" text-anchor="middle">Rakta</text>
        <text x="20" y="48" fill="#94a3b8" font-size="6" text-anchor="middle">Blood</text>
      </g>
      <line x1="116" y1="130" x2="134" y2="130" stroke="#f59e0b" stroke-width="2"/>

      <!-- 3. Mamsa (Muscle) -->
      <g transform="translate(140, 110)">
        <circle cx="20" cy="20" r="16" fill="#1e293b" stroke="#f97316" stroke-width="1.5"/>
        <text x="20" y="24" fill="#f97316" font-size="7" font-weight="bold" text-anchor="middle">Mamsa</text>
        <text x="20" y="48" fill="#94a3b8" font-size="6" text-anchor="middle">Muscle</text>
      </g>
      <line x1="176" y1="130" x2="194" y2="130" stroke="#f59e0b" stroke-width="2"/>

      <!-- 4. Meda (Adipose) -->
      <g transform="translate(200, 110)">
        <circle cx="20" cy="20" r="16" fill="#1e293b" stroke="#eab308" stroke-width="1.5"/>
        <text x="20" y="24" fill="#eab308" font-size="7" font-weight="bold" text-anchor="middle">Meda</text>
        <text x="20" y="48" fill="#94a3b8" font-size="6" text-anchor="middle">Fat</text>
      </g>
      <line x1="236" y1="130" x2="254" y2="130" stroke="#f59e0b" stroke-width="2"/>

      <!-- 5. Asthi (Bone) -->
      <g transform="translate(260, 110)">
        <circle cx="20" cy="20" r="16" fill="#1e293b" stroke="#f8fafc" stroke-width="1.5"/>
        <text x="20" y="24" fill="#f8fafc" font-size="7" font-weight="bold" text-anchor="middle">Asthi</text>
        <text x="20" y="48" fill="#94a3b8" font-size="6" text-anchor="middle">Bone</text>
      </g>
      <line x1="296" y1="130" x2="314" y2="130" stroke="#f59e0b" stroke-width="2"/>

      <!-- 6. Majja (Marrow) -->
      <g transform="translate(320, 110)">
        <circle cx="20" cy="20" r="16" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
        <text x="20" y="24" fill="#a855f7" font-size="7" font-weight="bold" text-anchor="middle">Majja</text>
        <text x="20" y="48" fill="#94a3b8" font-size="6" text-anchor="middle">Marrow</text>
      </g>
      <line x1="356" y1="130" x2="374" y2="130" stroke="#f59e0b" stroke-width="2"/>

      <!-- 7. Shukra / Artava (Reproductive) -->
      <g transform="translate(380, 110)">
        <circle cx="20" cy="20" r="18" fill="#831843" stroke="#f43f5e" stroke-width="2"/>
        <text x="20" y="24" fill="#fbcfe8" font-size="7" font-weight="bold" text-anchor="middle">Shukra/Artava</text>
        <text x="20" y="50" fill="#f43f5e" font-size="6" font-weight="bold" text-anchor="middle">Reproductive</text>
      </g>

      <!-- Classical Inscription Header (Top) -->
      <g transform="translate(80, 20)">
        <rect x="0" y="0" width="280" height="60" rx="8" fill="#1e293b" stroke="#d97706" stroke-width="1.5"/>
        <text x="140" y="22" fill="#facc15" font-size="11" font-weight="bold" text-anchor="middle">Sushruta Samhita & Charaka Samhita</text>
        <text x="140" y="38" fill="#cbd5e1" font-size="8" text-anchor="middle">Kishoravastha: The Golden Transition to Adulthood</text>
        <text x="140" y="50" fill="#38bdf8" font-size="7" text-anchor="middle">Balanced Dinacharya (Daily Routine) + Ahara (Nutrition) + Yoga</text>
      </g>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2 text-xs">
    <button id="btnDinacharyaRules" class="p-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold transition shadow">
      🧘 Ayurvedic Dinacharya (Daily Lifestyle)
    </button>
    <button id="btnArtavaDignity" class="p-2.5 rounded-xl bg-rose-700 hover:bg-rose-600 text-white font-bold transition shadow">
      🌸 Artava Pravritti (Menstrual Honor)
    </button>
  </div>

  <div id="ayurvedaExplanation" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300">
    📜 <span class="font-bold text-amber-300">Ancient Medical Wisdom:</span> Classical Indian texts honored adolescence as the culmination of the Sapta Dhatus, celebrating menstruation (*Artava Pravritti*) as the natural foundation of human health!
  </div>
</div>
"""
}

with open(".agents/class7_science_adolescence_sims.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 7 Science Chapter 6 Simulators HTML Dictionary"""\n\n')
    f.write("SIMULATORS_HTML = " + repr(SIMULATORS_HTML) + "\n")

print("Generated .agents/class7_science_adolescence_sims.py successfully.")

