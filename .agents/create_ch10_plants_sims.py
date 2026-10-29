# -*- coding: utf-8 -*-
"""
Generates the 16 bespoke SVG/HTML interactive simulators for Chapter 10: Life Processes in Plants.
Strictly zero raw LaTeX code. Clean Unicode everywhere.
"""

def generate_sims():
    sims = {}

    # Simulator 1: Autotrophic Solar Power Plant
    sims[1] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="font-bold text-sm text-emerald-300">Autotrophic Solar Energy Engine</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-emerald-900/60 text-emerald-200 border border-emerald-500/30 font-mono">Trophic Level 1: Primary Producers</span>
    </div>
    
    <div class="relative w-full h-64 bg-gradient-to-b from-sky-950/60 via-slate-900 to-emerald-950/30 rounded-lg overflow-hidden border border-slate-800/80 flex items-center justify-center">
        <svg id="sim1_svg" viewBox="0 0 600 240" class="w-full h-full select-none">
            <!-- Sky and Sun -->
            <defs>
                <radialGradient id="sunGrad" cx="50%" cy="50%" r="50%">
                    <stop offset="0%" stop-color="#fef08a" stop-opacity="1" />
                    <stop offset="60%" stop-color="#f59e0b" stop-opacity="0.8" />
                    <stop offset="100%" stop-color="#f59e0b" stop-opacity="0" />
                </radialGradient>
                <linearGradient id="leafGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#34d399" />
                    <stop offset="100%" stop-color="#065f46" />
                </linearGradient>
            </defs>
            
            <!-- Sun Source -->
            <circle id="sim1_sun" cx="80" cy="50" r="32" fill="url(#sunGrad)" />
            <circle cx="80" cy="50" r="16" fill="#fef08a" />
            
            <!-- Solar Rays -->
            <g id="sim1_rays" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,4" opacity="0.8">
                <line x1="110" y1="65" x2="220" y2="130" />
                <line x1="95" y1="80" x2="200" y2="155" />
                <line x1="80" y1="90" x2="180" y2="180" />
            </g>
            
            <!-- Plant Shoot -->
            <path d="M 220 230 Q 215 170 230 120" stroke="#059669" stroke-width="8" stroke-linecap="round" fill="none" />
            <!-- Big Leaf 1 -->
            <path id="sim1_leaf1" d="M 225 150 Q 150 120 120 140 Q 150 180 225 160 Z" fill="url(#leafGrad)" stroke="#10b981" stroke-width="1.5" />
            <!-- Big Leaf 2 -->
            <path id="sim1_leaf2" d="M 228 135 Q 290 80 340 100 Q 310 150 230 140 Z" fill="url(#leafGrad)" stroke="#10b981" stroke-width="1.5" />
            
            <!-- Soil -->
            <rect x="0" y="210" width="600" height="30" fill="#3e2723" opacity="0.8" />
            <line x1="0" y1="210" x2="600" y2="210" stroke="#795548" stroke-width="2" />
            <!-- Roots -->
            <path d="M 220 215 Q 210 235 190 240 M 220 215 Q 235 230 250 238" stroke="#d7ccc8" stroke-width="2" fill="none" />

            <!-- Chloroplast Zoom Bubble -->
            <g transform="translate(390, 30)">
                <circle cx="90" cy="70" r="60" fill="#064e3b" stroke="#10b981" stroke-width="3" opacity="0.95" />
                <text x="90" y="30" font-size="10" font-weight="bold" fill="#6ee7b7" text-anchor="middle">Chloroplast Organelle</text>
                <!-- Thylakoid Grana Discs -->
                <ellipse cx="65" cy="65" rx="18" ry="6" fill="#10b981" />
                <ellipse cx="65" cy="73" rx="18" ry="6" fill="#059669" />
                <ellipse cx="65" cy="81" rx="18" ry="6" fill="#047857" />
                <ellipse cx="115" cy="60" rx="18" ry="6" fill="#10b981" />
                <ellipse cx="115" cy="68" rx="18" ry="6" fill="#059669" />
                <ellipse cx="115" cy="76" rx="18" ry="6" fill="#047857" />
                <!-- Photons hitting grana -->
                <circle id="sim1_photon1" cx="65" cy="50" r="3" fill="#fef08a" />
                <circle id="sim1_photon2" cx="115" cy="45" r="3" fill="#fef08a" />
                <text x="90" y="105" font-size="9" fill="#a7f3d0" text-anchor="middle">Solar Energy → Glucose</text>
            </g>
            
            <!-- Output Gauges Box -->
            <g transform="translate(380, 165)">
                <rect x="0" y="0" width="200" height="40" rx="6" fill="#0f172a" stroke="#334155" />
                <text x="10" y="16" font-size="10" fill="#94a3b8">Glucose Yield:</text>
                <rect x="90" y="8" width="100" height="10" rx="3" fill="#1e293b" />
                <rect id="sim1_glucoseBar" x="90" y="8" width="75" height="10" rx="3" fill="#10b981" />
                <text id="sim1_yieldText" x="100" y="32" font-size="10" font-weight="bold" fill="#34d399">75% High Biomass</text>
            </g>
        </svg>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="text-slate-300 font-medium">Sunlight Intensity</span>
                <span id="sim1_sunVal" class="text-amber-400 font-mono font-bold">80%</span>
            </div>
            <input type="range" id="sim1_sunSlider" min="0" max="100" value="80" class="w-full accent-amber-500 cursor-pointer">
        </div>
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="text-slate-300 font-medium">Soil Moisture</span>
                <span id="sim1_waterVal" class="text-cyan-400 font-mono font-bold">75%</span>
            </div>
            <input type="range" id="sim1_waterSlider" min="0" max="100" value="75" class="w-full accent-cyan-500 cursor-pointer">
        </div>
    </div>
    
    <div id="sim1_status" class="text-xs p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30 text-emerald-200 text-center font-medium">
        Optimal autotrophic state: High photosynthetic rate generates abundant glucose and O₂ sustaining the food chain.
    </div>
</div>
"""

    # Simulator 2: The Four-Chamber Growth Laboratory (10.1)
    sims[2] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
            <span class="font-bold text-sm text-cyan-300">10.1 Controlled Seedling Growth Chamber</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-cyan-950 text-cyan-200 border border-cyan-500/30 font-mono">14-Day Botanical Assay</span>
    </div>

    <!-- Growth Chambers Grid -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
        <!-- Pot A -->
        <div class="p-2.5 rounded-lg bg-slate-900 border border-emerald-500/40 flex flex-col items-center">
            <span class="font-bold text-emerald-400 mb-1">Pot A (Sun + Water)</span>
            <div class="w-full h-36 bg-slate-950 rounded flex items-end justify-center pb-2 relative overflow-hidden">
                <div class="absolute top-1 left-1 text-[9px] text-amber-300">☀️ 💧</div>
                <!-- Plant A -->
                <svg id="sim2_potA_svg" viewBox="0 0 80 120" class="w-16 h-28">
                    <!-- Stem -->
                    <path id="sim2_stemA" d="M 40 110 Q 38 60 40 30" stroke="#10b981" stroke-width="5" stroke-linecap="round" fill="none" />
                    <!-- Leaves -->
                    <ellipse id="sim2_leafA1" cx="28" cy="45" rx="14" ry="7" fill="#10b981" transform="rotate(-30 28 45)" />
                    <ellipse id="sim2_leafA2" cx="52" cy="45" rx="14" ry="7" fill="#10b981" transform="rotate(30 52 45)" />
                    <ellipse id="sim2_leafA3" cx="30" cy="70" rx="12" ry="6" fill="#059669" transform="rotate(-20 30 70)" />
                    <ellipse id="sim2_leafA4" cx="50" cy="70" rx="12" ry="6" fill="#059669" transform="rotate(20 50 70)" />
                    <!-- Pot Base -->
                    <polygon points="20,110 60,110 52,120 28,120" fill="#b45309" />
                </svg>
            </div>
            <span id="sim2_potA_desc" class="text-[11px] text-emerald-300 font-semibold mt-1">Height: 22 cm (Vigorous)</span>
        </div>

        <!-- Pot B -->
        <div class="p-2.5 rounded-lg bg-slate-900 border border-rose-500/40 flex flex-col items-center">
            <span class="font-bold text-rose-400 mb-1">Pot B (Sun, No Water)</span>
            <div class="w-full h-36 bg-slate-950 rounded flex items-end justify-center pb-2 relative overflow-hidden">
                <div class="absolute top-1 left-1 text-[9px] text-amber-300">☀️ ❌</div>
                <!-- Plant B -->
                <svg id="sim2_potB_svg" viewBox="0 0 80 120" class="w-16 h-28">
                    <!-- Drooped Stem -->
                    <path id="sim2_stemB" d="M 40 110 Q 45 80 60 75" stroke="#84cc16" stroke-width="4" stroke-linecap="round" fill="none" />
                    <!-- Wilting Leaves -->
                    <ellipse id="sim2_leafB1" cx="62" cy="85" rx="12" ry="5" fill="#a3e635" transform="rotate(60 62 85)" />
                    <ellipse id="sim2_leafB2" cx="50" cy="88" rx="10" ry="4" fill="#a3e635" transform="rotate(70 50 88)" />
                    <!-- Pot Base -->
                    <polygon points="20,110 60,110 52,120 28,120" fill="#b45309" />
                </svg>
            </div>
            <span id="sim2_potB_desc" class="text-[11px] text-rose-300 font-semibold mt-1">Wilted / Drooping</span>
        </div>

        <!-- Pot C -->
        <div class="p-2.5 rounded-lg bg-slate-900 border border-amber-500/40 flex flex-col items-center">
            <span class="font-bold text-amber-400 mb-1">Pot C (Dark + Water)</span>
            <div class="w-full h-36 bg-slate-950 rounded flex items-end justify-center pb-2 relative overflow-hidden">
                <div class="absolute top-1 left-1 text-[9px] text-slate-400">🌑 💧</div>
                <!-- Plant C -->
                <svg id="sim2_potC_svg" viewBox="0 0 80 120" class="w-16 h-28">
                    <!-- Spindly Pale Stem -->
                    <path id="sim2_stemC" d="M 40 110 Q 36 60 38 25" stroke="#fef08a" stroke-width="2.5" stroke-linecap="round" fill="none" />
                    <!-- Tiny Yellow Leaves -->
                    <ellipse id="sim2_leafC1" cx="30" cy="30" rx="8" ry="4" fill="#fef08a" transform="rotate(-30 30 30)" />
                    <ellipse id="sim2_leafC2" cx="46" cy="30" rx="8" ry="4" fill="#fef08a" transform="rotate(30 46 30)" />
                    <!-- Pot Base -->
                    <polygon points="20,110 60,110 52,120 28,120" fill="#b45309" />
                </svg>
            </div>
            <span id="sim2_potC_desc" class="text-[11px] text-amber-300 font-semibold mt-1">Etiolated (Yellow/Thin)</span>
        </div>

        <!-- Pot D -->
        <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-700 flex flex-col items-center">
            <span class="font-bold text-slate-400 mb-1">Pot D (Dark, No Water)</span>
            <div class="w-full h-36 bg-slate-950 rounded flex items-end justify-center pb-2 relative overflow-hidden">
                <div class="absolute top-1 left-1 text-[9px] text-slate-400">🌑 ❌</div>
                <!-- Plant D -->
                <svg id="sim2_potD_svg" viewBox="0 0 80 120" class="w-16 h-28">
                    <!-- Shriveled Brown Stem -->
                    <path d="M 40 110 Q 42 95 48 90" stroke="#78350f" stroke-width="2" stroke-linecap="round" fill="none" />
                    <polygon points="20,110 60,110 52,120 28,120" fill="#b45309" />
                </svg>
            </div>
            <span id="sim2_potD_desc" class="text-[11px] text-slate-400 font-semibold mt-1">Shriveled / Dead</span>
        </div>
    </div>

    <!-- Timeline Slider -->
    <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2">
        <div class="flex justify-between text-xs">
            <span class="text-slate-300 font-medium">Elapsed Incubation Timeline</span>
            <span id="sim2_dayLabel" class="text-cyan-400 font-mono font-bold">Day 14</span>
        </div>
        <input type="range" id="sim2_daySlider" min="1" max="14" value="14" class="w-full accent-cyan-500 cursor-pointer">
        <div class="flex justify-between text-[10px] text-slate-400 font-mono">
            <span>Day 1 (Germination)</span>
            <span>Day 7 (Differentiation)</span>
            <span>Day 14 (Mature Assay)</span>
        </div>
    </div>

    <div id="sim2_summary" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-200">
        <strong class="text-cyan-300">Observation:</strong> Pot A demonstrates normal growth. Without water (Pot B), cellular turgor collapses causing wilting. Without light (Pot C), seedlings undergo etiolation, failing to synthesize chlorophyll.
    </div>
</div>
"""

    # Simulator 3: Leaf Microscopic Layer Dissector (10.2.1)
    sims[3] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="font-bold text-sm text-emerald-300">10.2.1 Microscopic Leaf Architecture</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-emerald-950 text-emerald-200 border border-emerald-500/30 font-mono">Transverse Cross-Section</span>
    </div>

    <!-- SVG Dissector Canvas -->
    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center">
        <svg id="sim3_svg" viewBox="0 0 600 240" class="w-full h-full select-none">
            <!-- Layer 1: Waxy Cuticle -->
            <rect id="sim3_cuticle" x="20" y="20" width="560" height="10" fill="#fef08a" opacity="0.6" stroke="#ca8a04" />
            <text x="30" y="28" font-size="9" fill="#854d0e" font-weight="bold">Waxy Cuticle (Waterproof)</text>

            <!-- Layer 2: Upper Epidermis -->
            <g id="sim3_upperEpidermis">
                <rect x="20" y="30" width="560" height="25" fill="#a7f3d0" opacity="0.4" stroke="#059669" />
                <!-- Epidermal Cells -->
                <path d="M 20 30 L 20 55 M 90 30 L 90 55 M 160 30 L 160 55 M 230 30 L 230 55 M 300 30 L 300 55 M 370 30 L 370 55 M 440 30 L 440 55 M 510 30 L 510 55 M 580 30 L 580 55" stroke="#059669" stroke-width="1" />
                <text x="30" y="47" font-size="10" fill="#065f46" font-weight="bold">Upper Epidermis (Transparent)</text>
            </g>

            <!-- Layer 3: Palisade Mesophyll (Chloroplast Dense) -->
            <g id="sim3_palisade">
                <rect x="20" y="55" width="560" height="65" fill="#064e3b" opacity="0.7" stroke="#047857" />
                <!-- Palisade Columns -->
                <g fill="#10b981" stroke="#065f46">
                    <rect x="30" y="58" width="22" height="58" rx="4" />
                    <rect x="60" y="58" width="22" height="58" rx="4" />
                    <rect x="90" y="58" width="22" height="58" rx="4" />
                    <rect x="120" y="58" width="22" height="58" rx="4" />
                    <rect x="150" y="58" width="22" height="58" rx="4" />
                    <rect x="180" y="58" width="22" height="58" rx="4" />
                    <rect x="210" y="58" width="22" height="58" rx="4" />
                    <rect x="240" y="58" width="22" height="58" rx="4" />
                    <rect x="270" y="58" width="22" height="58" rx="4" />
                    <rect x="300" y="58" width="22" height="58" rx="4" />
                    <rect x="330" y="58" width="22" height="58" rx="4" />
                    <rect x="360" y="58" width="22" height="58" rx="4" />
                    <rect x="390" y="58" width="22" height="58" rx="4" />
                    <rect x="420" y="58" width="22" height="58" rx="4" />
                    <rect x="450" y="58" width="22" height="58" rx="4" />
                    <rect x="480" y="58" width="22" height="58" rx="4" />
                    <rect x="510" y="58" width="22" height="58" rx="4" />
                    <rect x="540" y="58" width="22" height="58" rx="4" />
                </g>
                <text x="30" y="90" font-size="11" fill="#ecfdf5" font-weight="bold">Palisade Mesophyll (Dense Chloroplasts: Primary Photosynthesis Site)</text>
            </g>

            <!-- Layer 4: Spongy Mesophyll & Vascular Vein -->
            <g id="sim3_spongy">
                <rect x="20" y="120" width="560" height="65" fill="#022c22" opacity="0.6" stroke="#047857" />
                <!-- Spongy cells with air spaces -->
                <circle cx="50" cy="140" r="14" fill="#059669" />
                <circle cx="90" cy="160" r="16" fill="#059669" />
                <circle cx="140" cy="145" r="15" fill="#059669" />
                <circle cx="480" cy="145" r="15" fill="#059669" />
                <circle cx="525" cy="155" r="16" fill="#059669" />
                
                <!-- Vascular Bundle (Vein) in Middle -->
                <ellipse cx="300" cy="150" rx="45" ry="25" fill="#0f172a" stroke="#0284c7" stroke-width="2" />
                <!-- Xylem (Upper Red) -->
                <circle cx="285" cy="145" r="8" fill="#f87171" stroke="#dc2626" />
                <circle cx="300" cy="140" r="9" fill="#f87171" stroke="#dc2626" />
                <circle cx="315" cy="145" r="8" fill="#f87171" stroke="#dc2626" />
                <text x="300" y="132" font-size="8" fill="#fca5a5" font-weight="bold" text-anchor="middle">Xylem (H₂O)</text>
                <!-- Phloem (Lower Blue) -->
                <circle cx="290" cy="160" r="6" fill="#38bdf8" stroke="#0284c7" />
                <circle cx="305" cy="160" r="6" fill="#38bdf8" stroke="#0284c7" />
                <text x="300" y="172" font-size="8" fill="#7dd3fc" font-weight="bold" text-anchor="middle">Phloem (Food)</text>
            </g>

            <!-- Layer 5: Lower Epidermis with Stomata -->
            <g id="sim3_lowerEpidermis">
                <rect x="20" y="185" width="560" height="25" fill="#a7f3d0" opacity="0.4" stroke="#059669" />
                <!-- Stoma 1 -->
                <ellipse cx="160" cy="197" rx="8" ry="4" fill="#065f46" />
                <rect x="157" y="185" width="6" height="25" fill="#022c22" />
                <text x="160" y="222" font-size="8" fill="#34d399" text-anchor="middle">Stoma Pore</text>
                <!-- Stoma 2 -->
                <ellipse cx="440" cy="197" rx="8" ry="4" fill="#065f46" />
                <rect x="437" y="185" width="6" height="25" fill="#022c22" />
                <text x="440" y="222" font-size="8" fill="#34d399" text-anchor="middle">Stoma Pore</text>
            </g>
        </svg>
    </div>

    <!-- Layer Inspector Buttons -->
    <div class="flex flex-wrap gap-2">
        <button id="sim3_btn_all" class="px-3 py-1.5 rounded text-xs font-semibold bg-emerald-700 text-white hover:bg-emerald-600 transition">Show All Layers</button>
        <button id="sim3_btn_palisade" class="px-3 py-1.5 rounded text-xs font-semibold bg-slate-800 text-emerald-300 hover:bg-slate-700 transition">Inspect Palisade Mesophyll</button>
        <button id="sim3_btn_vein" class="px-3 py-1.5 rounded text-xs font-semibold bg-slate-800 text-cyan-300 hover:bg-slate-700 transition">Inspect Vascular Bundle</button>
        <button id="sim3_btn_stoma" class="px-3 py-1.5 rounded text-xs font-semibold bg-slate-800 text-amber-300 hover:bg-slate-700 transition">Inspect Stomatal Pores</button>
    </div>

    <div id="sim3_info" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Click any layer button to spotlight specific structural adaptations for sunlight capture, gas circulation, and vascular sap transport.
    </div>
</div>
"""

    # Simulator 4: Step-by-Step Starch Laboratory Workbench (10.2.1)
    sims[4] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
            <span class="font-bold text-sm text-amber-300">10.2.1 Virtual Starch Assay Workbench</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-amber-950 text-amber-200 border border-amber-500/30 font-mono">4-Stage Protocol</span>
    </div>

    <!-- Active Step Display -->
    <div class="relative w-full h-56 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center p-4">
        <svg id="sim4_svg" viewBox="0 0 500 200" class="w-full h-full select-none">
            <!-- Apparatus Stage 1: Boiling Water -->
            <g id="sim4_stage1">
                <rect x="180" y="60" width="140" height="90" rx="4" fill="#0284c7" opacity="0.4" stroke="#38bdf8" stroke-width="2" />
                <path d="M 210 110 Q 250 80 290 100 Q 250 130 210 110 Z" fill="#10b981" />
                <text x="250" y="80" font-size="11" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Boiling Water (100°C)</text>
                <!-- Bubbles -->
                <circle cx="210" cy="130" r="4" fill="#bae6fd" opacity="0.7" />
                <circle cx="280" cy="120" r="5" fill="#bae6fd" opacity="0.7" />
                <!-- Bunsen Burner flame -->
                <polygon points="240,175 260,175 250,152" fill="#f59e0b" />
                <polygon points="245,175 255,175 250,158" fill="#ef4444" />
            </g>

            <!-- Apparatus Stage 2: Ethanol Water Bath (hidden initially or shown) -->
            <g id="sim4_stage2" style="display:none;">
                <!-- Outer Beaker (Water bath) -->
                <rect x="170" y="60" width="160" height="90" rx="4" fill="#0284c7" opacity="0.3" stroke="#38bdf8" />
                <!-- Inner Test Tube (Alcohol) -->
                <rect x="235" y="40" width="30" height="90" rx="15" fill="#059669" opacity="0.6" stroke="#10b981" stroke-width="2" />
                <!-- Bleaching Leaf -->
                <path d="M 242 80 Q 250 70 258 75 Q 250 90 242 80 Z" fill="#d1fae5" />
                <text x="250" y="30" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">Ethanol Water Bath</text>
                <text x="250" y="165" font-size="9" fill="#94a3b8" text-anchor="middle">Chlorophyll dissolves into alcohol</text>
            </g>

            <!-- Apparatus Stage 3: Warm Water Rinse -->
            <g id="sim4_stage3" style="display:none;">
                <rect x="180" y="70" width="140" height="70" rx="8" fill="#38bdf8" opacity="0.3" stroke="#0ea5e9" stroke-width="2" />
                <path d="M 210 100 Q 250 85 290 95 Q 250 120 210 100 Z" fill="#fef3c7" stroke="#d97706" />
                <text x="250" y="55" font-size="11" font-weight="bold" fill="#bae6fd" text-anchor="middle">Warm Water Rinse</text>
                <text x="250" y="160" font-size="9" fill="#94a3b8" text-anchor="middle">Softens brittle leaf tissue</text>
            </g>

            <!-- Apparatus Stage 4: Petri Dish & Iodine -->
            <g id="sim4_stage4" style="display:none;">
                <!-- Petri Dish -->
                <ellipse cx="250" cy="110" rx="110" ry="45" fill="#1e293b" stroke="#64748b" stroke-width="2" />
                <!-- Tested Leaf -->
                <path id="sim4_testedLeaf" d="M 180 110 Q 250 80 320 105 Q 250 135 180 110 Z" fill="#1e3a8a" stroke="#172554" stroke-width="2" />
                <!-- Dropper -->
                <polygon points="248,30 252,30 251,50 249,50" fill="#78350f" />
                <circle cx="250" cy="60" r="3" fill="#b45309" />
                <text x="250" y="25" font-size="10" font-weight="bold" fill="#f59e0b" text-anchor="middle">Iodine Dropper (Amber Solution)</text>
                <text x="250" y="175" font-size="11" font-weight="bold" fill="#60a5fa" text-anchor="middle">Result: Intense Blue-Black Color (Starch Confirmed!)</text>
            </g>
        </svg>
    </div>

    <!-- Stepper Navigation -->
    <div class="flex items-center justify-between gap-2">
        <button id="sim4_prevBtn" class="px-3 py-1.5 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs font-semibold transition disabled:opacity-40" disabled>Previous Step</button>
        <span id="sim4_stepIndicator" class="text-xs font-mono font-bold text-amber-300">Step 1 of 4: Boiling Water</span>
        <button id="sim4_nextBtn" class="px-3 py-1.5 rounded bg-amber-600 text-white hover:bg-amber-500 text-xs font-semibold transition">Next Step</button>
    </div>

    <div id="sim4_stepDesc" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300 leading-relaxed">
        <strong class="text-amber-400">Step 1 (Water Boiling):</strong> The leaf is boiled in water for 2 minutes to disrupt cell membranes and halt all enzymatic activity, making the tissue permeable to reagents.
    </div>
</div>
"""

    # Simulator 5: Moll's Half-Leaf Gas Chamber Simulator (10.2.2)
    sims[5] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
            <span class="font-bold text-sm text-cyan-300">10.2.2 Moll's Half-Leaf CO₂ Chamber</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-cyan-950 text-cyan-200 border border-cyan-500/30 font-mono">CO₂ Requirement Assay</span>
    </div>

    <div class="relative w-full h-60 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center">
        <svg id="sim5_svg" viewBox="0 0 550 220" class="w-full h-full select-none">
            <!-- Glass Flask -->
            <rect x="220" y="50" width="220" height="130" rx="16" fill="#0284c7" opacity="0.15" stroke="#38bdf8" stroke-width="2" />
            <!-- Flask Neck & Cork -->
            <rect x="180" y="85" width="45" height="50" fill="#78350f" stroke="#451a03" />
            <text x="330" y="40" font-size="11" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Airtight Glass Chamber (CO₂ Free)</text>

            <!-- KOH absorbent at bottom -->
            <rect id="sim5_koh_layer" x="230" y="160" width="200" height="15" rx="3" fill="#f43f5e" opacity="0.8" />
            <text id="sim5_koh_text" x="330" y="172" font-size="9" font-weight="bold" fill="#ffe4e6" text-anchor="middle">KOH Pellets (Absorbing all CO₂)</text>

            <!-- The Experimental Leaf split across cork -->
            <!-- Outer half (left, in ambient air) -->
            <path id="sim5_leafOuter" d="M 80 110 Q 130 90 195 105 Q 130 130 80 110 Z" fill="#10b981" stroke="#059669" stroke-width="2" />
            <text x="130" y="85" font-size="9" font-weight="bold" fill="#6ee7b7" text-anchor="middle">Outer Half (Air + CO₂)</text>

            <!-- Inner half (right, inside bottle) -->
            <path id="sim5_leafInner" d="M 210 105 Q 280 90 380 110 Q 280 130 210 105 Z" fill="#10b981" stroke="#059669" stroke-width="2" />
            <text x="310" y="100" font-size="9" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Inner Half (No CO₂)</text>

            <!-- Starch Result Overlay (revealed upon clicking test) -->
            <g id="sim5_resultGroup" style="display:none;">
                <rect x="50" y="10" width="450" height="35" rx="6" fill="#090d16" stroke="#475569" />
                <text x="275" y="32" font-size="11" font-weight="bold" fill="#f8fafc" text-anchor="middle">Iodine Result: Outer = Blue-Black (Starch) | Inner = Brown (No Starch)</text>
            </g>
        </svg>
    </div>

    <div class="flex flex-wrap items-center justify-between gap-3">
        <button id="sim5_toggleKOH" class="px-3 py-1.5 rounded bg-rose-700 text-white hover:bg-rose-600 text-xs font-semibold transition">Remove KOH (Control Setup)</button>
        <button id="sim5_runTest" class="px-4 py-1.5 rounded bg-emerald-600 text-white hover:bg-emerald-500 text-xs font-bold transition">Apply Iodine Starch Test</button>
        <button id="sim5_reset" class="px-3 py-1.5 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs font-semibold transition">Reset Experiment</button>
    </div>

    <div id="sim5_feedback" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Click <strong class="text-emerald-400">'Apply Iodine Starch Test'</strong> to decolourise the leaf and reveal the sharp boundary line separating the outer CO₂-supplied half from the inner CO₂-starved half.
    </div>
</div>
"""

    # Simulator 6: Photosynthesis Molecular Reaction Engine (10.2.3)
    sims[6] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="font-bold text-sm text-emerald-300">10.2.3 Molecular Reaction Engine</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-emerald-950 text-emerald-200 border border-emerald-500/30 font-mono">6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂</span>
    </div>

    <div class="relative w-full h-60 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center p-2">
        <svg id="sim6_svg" viewBox="0 0 560 220" class="w-full h-full select-none">
            <!-- Left: Reactants Chamber -->
            <rect x="20" y="30" width="160" height="160" rx="8" fill="#0f172a" stroke="#334155" />
            <text x="100" y="50" font-size="11" font-weight="bold" fill="#94a3b8" text-anchor="middle">INPUTS (Reactants)</text>
            <text x="100" y="85" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">6 CO₂ Molecules</text>
            <text x="100" y="105" font-size="9" fill="#94a3b8" text-anchor="middle">(From Stomata Air)</text>
            <text x="100" y="145" font-size="12" font-weight="bold" fill="#06b6d4" text-anchor="middle">6 H₂O Molecules</text>
            <text x="100" y="165" font-size="9" fill="#94a3b8" text-anchor="middle">(From Xylem Roots)</text>

            <!-- Center: Chloroplast Thylakoid Core -->
            <g transform="translate(210, 40)">
                <circle cx="70" cy="70" r="60" fill="#064e3b" stroke="#10b981" stroke-width="3" />
                <text x="70" y="45" font-size="10" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Chlorophyll Core</text>
                <text id="sim6_photonState" x="70" y="70" font-size="14" font-weight="bold" fill="#fef08a" text-anchor="middle">⚡ Photons ⚡</text>
                <text x="70" y="95" font-size="9" fill="#6ee7b7" text-anchor="middle">Photolysis of H₂O</text>
            </g>

            <!-- Right: Products Chamber -->
            <rect x="380" y="30" width="160" height="160" rx="8" fill="#0f172a" stroke="#334155" />
            <text x="460" y="50" font-size="11" font-weight="bold" fill="#94a3b8" text-anchor="middle">OUTPUTS (Products)</text>
            <text x="460" y="85" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">1 C₆H₁₂O₆ (Glucose)</text>
            <text x="460" y="105" font-size="9" fill="#94a3b8" text-anchor="middle">(Hexose Sugar → Starch)</text>
            <text x="460" y="145" font-size="12" font-weight="bold" fill="#f43f5e" text-anchor="middle">6 O₂ (Oxygen Gas)</text>
            <text x="460" y="165" font-size="9" fill="#94a3b8" text-anchor="middle">(Diffuses Outward)</text>
        </svg>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="text-slate-300 font-medium">Solar Photon Flux (Light)</span>
                <span id="sim6_lightVal" class="text-amber-400 font-mono font-bold">100%</span>
            </div>
            <input type="range" id="sim6_lightSlider" min="0" max="100" value="100" class="w-full accent-amber-500 cursor-pointer">
        </div>
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="text-slate-300 font-medium">CO₂ Substrate Concentration</span>
                <span id="sim6_co2Val" class="text-cyan-400 font-mono font-bold">Normal (0.04%)</span>
            </div>
            <input type="range" id="sim6_co2Slider" min="0" max="100" value="50" class="w-full accent-cyan-500 cursor-pointer">
        </div>
    </div>

    <div id="sim6_status" class="text-xs p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30 text-emerald-200 text-center font-medium">
        Optimal stoichiometry: 6 molecules of CO₂ + 6 molecules of H₂O yield exactly 1 glucose molecule and 6 oxygen molecules.
    </div>
</div>
"""

    # Simulator 7: Ingenhousz Inverted Funnel Hydrilla Photometer (10.2.3)
    sims[7] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
            <span class="font-bold text-sm text-amber-300">10.2.3 Ingenhousz Hydrilla Oxygen Apparatus</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-amber-950 text-amber-200 border border-amber-500/30 font-mono">Glowing Splinter Confirmation</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center">
        <svg id="sim7_svg" viewBox="0 0 560 240" class="w-full h-full select-none">
            <!-- Lamp Source on Left -->
            <g id="sim7_lamp" transform="translate(60, 110)">
                <rect x="-30" y="-20" width="30" height="40" fill="#475569" rx="3" />
                <path d="M 0 -25 L 30 -40 L 30 40 L 0 25 Z" fill="#f59e0b" opacity="0.8" />
                <!-- Light Beams -->
                <polygon id="sim7_lightCone" points="30,-40 220,-20 220,180 30,40" fill="#fef08a" opacity="0.25" />
                <text x="0" y="45" font-size="9" fill="#94a3b8" text-anchor="middle">Incandescent Lamp</text>
            </g>

            <!-- Water Beaker -->
            <rect x="250" y="40" width="200" height="170" rx="6" fill="#0284c7" opacity="0.2" stroke="#38bdf8" stroke-width="2" />
            <text x="350" y="30" font-size="10" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Beaker of Water + Hydrilla</text>

            <!-- Inverted Glass Funnel -->
            <path d="M 270 190 L 335 120 L 335 80 L 365 80 L 365 120 L 430 190 Z" fill="#38bdf8" opacity="0.3" stroke="#0ea5e9" stroke-width="1.5" />
            
            <!-- Inverted Test Tube over Funnel Stem -->
            <rect x="330" y="50" width="40" height="70" rx="10" fill="#0369a1" opacity="0.4" stroke="#38bdf8" stroke-width="1.5" />
            <!-- Gas Space at Top of Test Tube -->
            <rect id="sim7_gasPocket" x="331" y="51" width="38" height="20" rx="5" fill="#f8fafc" opacity="0.8" />
            <text x="350" y="65" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">O₂ Gas</text>

            <!-- Hydrilla Twigs inside Funnel -->
            <path d="M 310 190 Q 340 160 350 140 M 390 190 Q 360 160 350 140" stroke="#10b981" stroke-width="4" stroke-linecap="round" fill="none" />
            <ellipse cx="330" cy="165" rx="10" ry="4" fill="#059669" />
            <ellipse cx="370" cy="165" rx="10" ry="4" fill="#059669" />

            <!-- Rising Oxygen Bubbles -->
            <g id="sim7_bubbles" fill="#bae6fd" opacity="0.8">
                <circle cx="348" cy="120" r="3" />
                <circle cx="352" cy="100" r="3.5" />
                <circle cx="347" cy="85" r="4" />
            </g>

            <!-- Burning Splinter Test (animated / shown on test click) -->
            <g id="sim7_splinterGroup" style="display:none;" transform="translate(340, 20)">
                <line x1="10" y1="-10" x2="10" y2="35" stroke="#78350f" stroke-width="3" />
                <polygon id="sim7_flame" points="5,35 15,35 10,15" fill="#f59e0b" />
                <polygon points="7,35 13,35 10,22" fill="#ef4444" />
                <text x="10" y="-15" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">Burst into Flame!</text>
            </g>
        </svg>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="text-slate-300 font-medium">Distance of Lamp from Beaker</span>
                <span id="sim7_distVal" class="text-amber-400 font-mono font-bold">20 cm</span>
            </div>
            <input type="range" id="sim7_distSlider" min="10" max="80" value="20" class="w-full accent-amber-500 cursor-pointer">
        </div>
        <div class="flex items-center justify-between">
            <div>
                <span class="text-xs text-slate-400 block">Rate of Bubble Evolution:</span>
                <span id="sim7_bubbleRate" class="text-base font-mono font-bold text-emerald-400">54 Bubbles / min</span>
            </div>
            <button id="sim7_igniteBtn" class="px-3 py-2 rounded bg-amber-600 text-white hover:bg-amber-500 text-xs font-bold transition">Test Glowing Splinter</button>
        </div>
    </div>

    <div id="sim7_info" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Closer lamp distance increases photon flux, elevating oxygen evolution. Testing with a glowing splinter causes it to burst into flame, confirming pure oxygen gas.
    </div>
</div>
"""

    # Simulator 8: Microscopic Guard Cell Stomatal Aperture (10.2.4)
    sims[8] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="font-bold text-sm text-emerald-300">10.2.4 Guard Cell Turgor Biomechanics</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-emerald-950 text-emerald-200 border border-emerald-500/30 font-mono">Stomatal Pore Aperture</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center">
        <svg id="sim8_svg" viewBox="0 0 500 240" class="w-full h-full select-none">
            <!-- Background Epidermal Cells -->
            <path d="M 50 40 Q 150 20 200 60 Q 250 20 350 40 Q 450 30 480 80 Q 460 180 380 200 Q 250 220 150 200 Q 40 180 50 40 Z" fill="#064e3b" opacity="0.3" stroke="#047857" stroke-width="2" />
            
            <!-- Left Guard Cell (Kidney Shaped) -->
            <path id="sim8_guardL" d="M 230 40 C 180 60 180 180 230 200 C 215 150 215 90 230 40 Z" fill="#10b981" stroke="#047857" stroke-width="3" />
            <!-- Thick Inner Wall Left -->
            <path id="sim8_innerWallL" d="M 230 40 C 215 90 215 150 230 200" stroke="#065f46" stroke-width="6" fill="none" />
            <!-- Chloroplasts in Left Guard Cell -->
            <circle cx="205" cy="80" r="5" fill="#047857" />
            <circle cx="200" cy="120" r="5" fill="#047857" />
            <circle cx="205" cy="160" r="5" fill="#047857" />

            <!-- Right Guard Cell (Kidney Shaped) -->
            <path id="sim8_guardR" d="M 270 40 C 320 60 320 180 270 200 C 285 150 285 90 270 40 Z" fill="#10b981" stroke="#047857" stroke-width="3" />
            <!-- Thick Inner Wall Right -->
            <path id="sim8_innerWallR" d="M 270 40 C 285 90 285 150 270 200" stroke="#065f46" stroke-width="6" fill="none" />
            <!-- Chloroplasts in Right Guard Cell -->
            <circle cx="295" cy="80" r="5" fill="#047857" />
            <circle cx="300" cy="120" r="5" fill="#047857" />
            <circle cx="295" cy="160" r="5" fill="#047857" />

            <!-- Stomatal Pore Gap in Center -->
            <ellipse id="sim8_pore" cx="250" cy="120" rx="20" ry="55" fill="#020617" />
            <text id="sim8_poreLabel" x="250" y="125" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">OPEN PORE</text>

            <!-- Gas Diffusion Arrows -->
            <g id="sim8_arrows">
                <!-- CO2 In -->
                <path d="M 120 120 L 220 120" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)" fill="none" />
                <text x="140" y="112" font-size="10" font-weight="bold" fill="#38bdf8">CO₂ Inflow</text>
                <!-- O2 Out -->
                <path d="M 280 100 L 380 90" stroke="#f43f5e" stroke-width="3" fill="none" />
                <text x="320" y="85" font-size="10" font-weight="bold" fill="#f43f5e">O₂ Outflow</text>
                <!-- H2O Out (Transpiration) -->
                <path d="M 280 140 L 380 150" stroke="#67e8f9" stroke-width="3" stroke-dasharray="3,3" fill="none" />
                <text x="320" y="165" font-size="10" font-weight="bold" fill="#67e8f9">H₂O Vapor Out</text>
            </g>
        </svg>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="text-slate-300 font-medium">Guard Cell Water Turgor</span>
                <span id="sim8_turgorVal" class="text-emerald-400 font-mono font-bold">100% (Turgid)</span>
            </div>
            <input type="range" id="sim8_turgorSlider" min="0" max="100" value="100" class="w-full accent-emerald-500 cursor-pointer">
        </div>
        <div class="flex items-center justify-between">
            <span class="text-xs text-slate-300">Environmental State:</span>
            <button id="sim8_toggleLight" class="px-3 py-1.5 rounded bg-amber-600 text-white text-xs font-semibold hover:bg-amber-500 transition">☀️ Daylight (Open)</button>
        </div>
    </div>

    <div id="sim8_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        <strong class="text-emerald-400">Turgid State:</strong> Water inflates guard cells; their inelastic thick inner walls resist stretching while elastic outer walls bow outward, opening the central pore for CO₂ uptake.
    </div>
</div>
"""

    # Simulator 9: Stem Cross-Section Vascular Scanner (10.3)
    sims[9] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
            <span class="font-bold text-sm text-cyan-300">10.3 Vascular Highway Architecture</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-cyan-950 text-cyan-200 border border-cyan-500/30 font-mono">Xylem vs Phloem Micro-Dissection</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <!-- Stem Cross Section Diagram -->
        <div class="h-56 bg-slate-900 rounded-lg p-2 border border-slate-800 flex items-center justify-center">
            <svg id="sim9_stem_svg" viewBox="0 0 240 220" class="w-full h-full select-none">
                <!-- Stem Outer Ring (Epidermis & Cortex) -->
                <circle cx="120" cy="110" r="95" fill="#064e3b" opacity="0.3" stroke="#047857" stroke-width="2" />
                <!-- Central Pith -->
                <circle cx="120" cy="110" r="40" fill="#0f172a" stroke="#334155" />
                <text x="120" y="114" font-size="9" fill="#94a3b8" text-anchor="middle">Central Pith</text>

                <!-- Ring of Vascular Bundles -->
                <g id="sim9_bundles">
                    <!-- Bundle Top -->
                    <circle cx="120" cy="50" r="14" fill="#0284c7" opacity="0.8" stroke="#38bdf8" />
                    <!-- Bundle Bottom -->
                    <circle cx="120" cy="170" r="14" fill="#0284c7" opacity="0.8" stroke="#38bdf8" />
                    <!-- Bundle Left -->
                    <circle cx="60" cy="110" r="14" fill="#0284c7" opacity="0.8" stroke="#38bdf8" />
                    <!-- Bundle Right -->
                    <circle cx="180" cy="110" r="14" fill="#0284c7" opacity="0.8" stroke="#38bdf8" />
                </g>
                <text x="120" y="25" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Dicot Stem Ring Layout</text>
            </svg>
        </div>

        <!-- Longitudinal Conduit Comparison -->
        <div class="h-56 bg-slate-900 rounded-lg p-3 border border-slate-800 flex flex-col justify-between text-xs">
            <!-- Xylem Box -->
            <div id="sim9_xylemBox" class="p-2.5 rounded bg-rose-950/40 border border-rose-500/40">
                <div class="flex justify-between items-center mb-1">
                    <strong class="text-rose-400">Xylem Vessel Conduit</strong>
                    <span class="text-[10px] text-rose-300 font-mono">Dead Lignified Tube</span>
                </div>
                <p class="text-slate-300 text-[11px]">Continuous hollow dead pipe with annular/spiral lignin rings. Transports water and minerals <strong class="text-rose-300">strictly upward (↑)</strong> via transpiration suction.</p>
            </div>
            <!-- Phloem Box -->
            <div id="sim9_phloemBox" class="p-2.5 rounded bg-cyan-950/40 border border-cyan-500/40">
                <div class="flex justify-between items-center mb-1">
                    <strong class="text-cyan-300">Phloem Sieve Tube</strong>
                    <span class="text-[10px] text-cyan-200 font-mono">Living Perforated Cells</span>
                </div>
                <p class="text-slate-300 text-[11px]">Living cells connected by perforated sieve plates, flanked by companion cells. Translocates sucrose and amino acids <strong class="text-cyan-200">bidirectionally (↕)</strong> from sources to sinks.</p>
            </div>
        </div>
    </div>

    <!-- Controls -->
    <div class="flex flex-wrap gap-2">
        <button id="sim9_toggleXylem" class="px-3 py-1.5 rounded bg-rose-700 text-white text-xs font-semibold hover:bg-rose-600 transition">Animate Xylem Flow (↑ Water)</button>
        <button id="sim9_togglePhloem" class="px-3 py-1.5 rounded bg-cyan-700 text-white text-xs font-semibold hover:bg-cyan-600 transition">Animate Phloem Flow (↕ Sucrose)</button>
    </div>

    <div id="sim9_info" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Xylem and phloem travel side-by-side inside vascular bundles. Xylem is unidirectional (root to leaf); phloem is bidirectional (leaf to buds, seeds, and root tubers).
    </div>
</div>
"""

    # Simulator 10: Root Hair Osmosis & Mineral Active Transport Lab (10.3.1)
    sims[10] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="font-bold text-sm text-emerald-300">10.3.1 Root Hair Osmotic Absorption</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-emerald-950 text-emerald-200 border border-emerald-500/30 font-mono">Soil-to-Root Interface</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center">
        <svg id="sim10_svg" viewBox="0 0 560 240" class="w-full h-full select-none">
            <!-- Soil Matrix on Left -->
            <rect x="0" y="0" width="220" height="240" fill="#3e2723" opacity="0.6" />
            <text x="110" y="30" font-size="11" font-weight="bold" fill="#d7ccc8" text-anchor="middle">Soil Matrix with Water Film</text>
            <!-- Soil Particles -->
            <circle cx="50" cy="70" r="18" fill="#4e342e" />
            <circle cx="120" cy="90" r="24" fill="#4e342e" />
            <circle cx="60" cy="150" r="22" fill="#4e342e" />
            <circle cx="140" cy="180" r="20" fill="#4e342e" />
            <!-- Water Droplets in Soil -->
            <g fill="#38bdf8" opacity="0.8">
                <circle cx="90" cy="65" r="4" />
                <circle cx="75" cy="115" r="5" />
                <circle cx="160" cy="130" r="4.5" />
                <circle cx="105" cy="165" r="5" />
            </g>

            <!-- Root Hair Tubular Extension -->
            <path d="M 220 70 Q 150 110 90 120 Q 150 130 220 170" fill="#065f46" stroke="#10b981" stroke-width="2" />
            <!-- Root Hair Vacuole -->
            <path d="M 215 80 Q 155 110 100 120 Q 155 130 215 160" fill="#047857" opacity="0.7" />
            <text x="175" y="125" font-size="9" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Vacuole (Cell Sap)</text>

            <!-- Root Epidermis & Cortex (Right) -->
            <rect x="220" y="0" width="340" height="240" fill="#064e3b" opacity="0.4" stroke="#047857" />
            <text x="380" y="30" font-size="11" font-weight="bold" fill="#6ee7b7" text-anchor="middle">Root Cortex → Endodermis → Xylem</text>
            
            <!-- Central Root Xylem Vessel on far right -->
            <rect x="490" y="40" width="50" height="180" fill="#0284c7" opacity="0.5" stroke="#38bdf8" stroke-width="2" />
            <text x="515" y="130" font-size="10" font-weight="bold" fill="#bae6fd" text-anchor="middle" transform="rotate(-90 515 130)">XYLEM VESSEL</text>

            <!-- Animated Water Flow Arrows -->
            <path id="sim10_flowArrow" d="M 100 120 L 220 120 L 490 120" stroke="#38bdf8" stroke-width="4" stroke-dasharray="6,4" fill="none" />
        </svg>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="text-slate-300 font-medium">Soil Water Saturation</span>
                <span id="sim10_soilWaterVal" class="text-cyan-400 font-mono font-bold">80% (Moist)</span>
            </div>
            <input type="range" id="sim10_soilWaterSlider" min="10" max="100" value="80" class="w-full accent-cyan-500 cursor-pointer">
        </div>
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="text-slate-300 font-medium">Root Sap Solute Concentration</span>
                <span id="sim10_soluteVal" class="text-emerald-400 font-mono font-bold">High (Steep Osmotic Pull)</span>
            </div>
            <input type="range" id="sim10_soluteSlider" min="1" max="5" value="4" class="w-full accent-emerald-500 cursor-pointer">
        </div>
    </div>

    <div id="sim10_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Water moves down the water potential gradient: dilute soil moisture enters concentrated root hair vacuoles via osmosis, traveling across cortex cells to charge root xylem.
    </div>
</div>
"""

    # Simulator 11: The Balsam Plant Red Ink Transpiration Column (10.3.1)
    sims[11] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-rose-400 animate-pulse"></span>
            <span class="font-bold text-sm text-rose-300">10.3.1 Balsam Plant Red Ink Transpiration Column</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-rose-950 text-rose-200 border border-rose-500/30 font-mono">Xylem Water Ascent Demonstration</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center">
        <svg id="sim11_svg" viewBox="0 0 540 240" class="w-full h-full select-none">
            <!-- Glass Beaker with Red Eosin Dye -->
            <rect x="200" y="130" width="140" height="95" rx="6" fill="#0284c7" opacity="0.1" stroke="#38bdf8" stroke-width="2" />
            <!-- Red Eosin Liquid -->
            <rect x="202" y="160" width="136" height="63" rx="4" fill="#e11d48" opacity="0.8" />
            <text x="270" y="195" font-size="10" font-weight="bold" fill="#ffe4e6" text-anchor="middle">Red Eosin Solution</text>

            <!-- Balsam Plant Stem dipping into dye -->
            <path id="sim11_stem" d="M 270 210 L 270 60" stroke="#86efac" stroke-width="12" stroke-linecap="round" fill="none" />
            <!-- Internal Xylem Dye Ascent Column -->
            <line id="sim11_dyeCol" x1="270" y1="210" x2="270" y2="100" stroke="#f43f5e" stroke-width="6" stroke-linecap="round" />

            <!-- Leaves branching from stem -->
            <!-- Leaf 1 (Left) -->
            <path d="M 270 120 Q 210 100 170 110 Q 210 135 270 125 Z" fill="#22c55e" stroke="#15803d" />
            <path id="sim11_veinL" d="M 270 122 Q 220 105 180 110" stroke="#f43f5e" stroke-width="2" fill="none" opacity="0.7" />

            <!-- Leaf 2 (Right) -->
            <path d="M 270 90 Q 330 70 370 80 Q 330 105 270 95 Z" fill="#22c55e" stroke="#15803d" />
            <path id="sim11_veinR" d="M 270 92 Q 320 75 360 80" stroke="#f43f5e" stroke-width="2" fill="none" opacity="0.7" />

            <!-- White / Pink Flower at top -->
            <circle id="sim11_flower" cx="270" cy="50" r="14" fill="#fda4af" stroke="#f43f5e" stroke-width="1.5" />
            <circle cx="270" cy="50" r="5" fill="#fef08a" />
            <text x="270" y="25" font-size="10" font-weight="bold" fill="#fda4af" text-anchor="middle">Petals Tinting Pink!</text>

            <!-- Transpiration Evaporation Wisps at Leaves -->
            <g id="sim11_wisps" stroke="#67e8f9" stroke-width="1.5" stroke-dasharray="2,2" opacity="0.8">
                <path d="M 170 105 Q 160 85 165 70" />
                <path d="M 370 75 Q 380 55 375 40" />
            </g>
        </svg>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 bg-slate-900/80 p-3 rounded-lg border border-slate-800">
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="text-slate-300 font-medium">Fan Wind Speed</span>
                <span id="sim11_windVal" class="text-cyan-400 font-mono font-bold">Medium (Speed 2)</span>
            </div>
            <input type="range" id="sim11_windSlider" min="0" max="3" value="2" class="w-full accent-cyan-500 cursor-pointer">
        </div>
        <div>
            <div class="flex justify-between text-xs mb-1">
                <span class="text-slate-300 font-medium">Ambient Temperature</span>
                <span id="sim11_tempVal" class="text-amber-400 font-mono font-bold">28°C Warm</span>
            </div>
            <input type="range" id="sim11_tempSlider" min="15" max="40" value="28" class="w-full accent-amber-500 cursor-pointer">
        </div>
    </div>

    <div id="sim11_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Higher temperature and breeze accelerate transpiration pull at leaf stomata, drawing red eosin dye up the xylem vessels to stain leaf veins and flower petals pink.
    </div>
</div>
"""

    # Simulator 12: Source-to-Sink Phloem Translocation Model (10.3.2)
    sims[12] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
            <span class="font-bold text-sm text-cyan-300">10.3.2 Source-to-Sink Phloem Translocation</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-cyan-950 text-cyan-200 border border-cyan-500/30 font-mono">Pressure-Flow Mass Transport</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center">
        <svg id="sim12_svg" viewBox="0 0 540 240" class="w-full h-full select-none">
            <!-- Source Leaf (Top Left) -->
            <g transform="translate(60, 40)">
                <path d="M 0 30 Q 50 0 100 20 Q 50 60 0 30 Z" fill="#10b981" stroke="#059669" stroke-width="2" />
                <text x="50" y="25" font-size="10" font-weight="bold" fill="#ecfdf5" text-anchor="middle">SOURCE: Leaf</text>
                <text x="50" y="45" font-size="8" fill="#d1fae5" text-anchor="middle">Sucrose Loading (ATP)</text>
            </g>

            <!-- Main Stem Phloem Highway (Center Tube) -->
            <rect x="240" y="20" width="60" height="200" rx="6" fill="#0284c7" opacity="0.3" stroke="#0284c7" stroke-width="2" />
            <text x="270" y="15" font-size="10" font-weight="bold" fill="#7dd3fc" text-anchor="middle">Phloem Sieve Tube</text>

            <!-- Girdling Ring Cutout in Middle (shown if toggled) -->
            <rect id="sim12_girdleCut" x="238" y="110" width="64" height="20" fill="#0f172a" stroke="#f43f5e" stroke-dasharray="2,2" style="display:none;" />
            <!-- Bark Swelling above girdle -->
            <path id="sim12_swelling" d="M 235 105 Q 220 110 235 115" stroke="#f59e0b" stroke-width="6" fill="none" style="display:none;" />

            <!-- Sink 1: Apical Growing Bud (Top Right) -->
            <g transform="translate(370, 30)">
                <circle cx="40" cy="30" r="22" fill="#3b82f6" opacity="0.5" stroke="#60a5fa" />
                <text x="40" y="25" font-size="9" font-weight="bold" fill="#bfdbfe" text-anchor="middle">SINK 1: Apical Bud</text>
                <text x="40" y="38" font-size="8" fill="#93c5fd" text-anchor="middle">(Upward Growth ↑)</text>
            </g>

            <!-- Sink 2: Root Storage Tuber (Bottom Right) -->
            <g transform="translate(360, 160)">
                <ellipse cx="50" cy="30" rx="40" ry="22" fill="#78350f" stroke="#b45309" stroke-width="2" />
                <text x="50" y="28" font-size="9" font-weight="bold" fill="#fef3c7" text-anchor="middle">SINK 2: Root Tuber</text>
                <text x="50" y="42" font-size="8" fill="#fde68a" text-anchor="middle">(Downward Storage ↓)</text>
            </g>

            <!-- Sugar Molecule Flow Pulses -->
            <g id="sim12_pulses" fill="#f59e0b">
                <circle cx="270" cy="60" r="4" />
                <circle cx="270" cy="90" r="4" />
                <circle cx="270" cy="140" r="4" />
                <circle cx="270" cy="180" r="4" />
            </g>
        </svg>
    </div>

    <!-- Controls -->
    <div class="flex flex-wrap items-center justify-between gap-3">
        <button id="sim12_btnSeason" class="px-3 py-1.5 rounded bg-emerald-700 text-white hover:bg-emerald-600 text-xs font-semibold transition">Mode: Summer Storage (Leaf → Tuber)</button>
        <button id="sim12_btnGirdle" class="px-3 py-1.5 rounded bg-rose-700 text-white hover:bg-rose-600 text-xs font-semibold transition">Apply Girdling Ring Cut</button>
        <button id="sim12_btnReset" class="px-3 py-1.5 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs font-semibold transition">Reset Highway</button>
    </div>

    <div id="sim12_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        In summer, photosynthetic leaves act as sources exporting sugars downward to root storage tubers. Cutting a girdle ring blocks downward phloem flow, producing visible swelling above the cut.
    </div>
</div>
"""

    # Simulator 13: 24-Hour Diurnal Gas Exchange Balance (10.4)
    sims[13] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
            <span class="font-bold text-sm text-amber-300">10.4 Diurnal Gas Exchange & Compensation Point</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-amber-950 text-amber-200 border border-amber-500/30 font-mono">24-Hour Day/Night Metabolism</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center">
        <svg id="sim13_svg" viewBox="0 0 540 240" class="w-full h-full select-none">
            <!-- Sky Background that transitions with time -->
            <rect id="sim13_sky" x="0" y="0" width="540" height="150" fill="#0284c7" opacity="0.5" />
            
            <!-- Sun or Moon -->
            <circle id="sim13_celestial" cx="270" cy="50" r="24" fill="#fef08a" />
            <text id="sim13_celestialLabel" x="270" y="90" font-size="10" font-weight="bold" fill="#fde047" text-anchor="middle">Midday Sun (Bright Light)</text>

            <!-- Plant Silhouette -->
            <g transform="translate(230, 110)">
                <path d="M 40 100 Q 38 60 40 30" stroke="#059669" stroke-width="6" fill="none" />
                <ellipse cx="25" cy="45" rx="18" ry="8" fill="#10b981" transform="rotate(-30 25 45)" />
                <ellipse cx="55" cy="45" rx="18" ry="8" fill="#10b981" transform="rotate(30 55 45)" />
            </g>

            <!-- Gas Vectors Box -->
            <g transform="translate(20, 160)">
                <rect x="0" y="0" width="220" height="70" rx="6" fill="#0f172a" stroke="#334155" />
                <text x="10" y="20" font-size="10" font-weight="bold" fill="#94a3b8">Photosynthesis Rate:</text>
                <text id="sim13_photoRate" x="150" y="20" font-size="11" font-weight="bold" fill="#10b981">100% (High)</text>
                <text x="10" y="42" font-size="10" font-weight="bold" fill="#94a3b8">Respiration Rate:</text>
                <text x="150" y="42" font-size="11" font-weight="bold" fill="#f43f5e">10% (Constant)</text>
                <text id="sim13_netGas" x="10" y="60" font-size="10" font-weight="bold" fill="#38bdf8">NET: Absorbing CO₂, Releasing O₂</text>
            </g>

            <g transform="translate(300, 160)">
                <rect x="0" y="0" width="220" height="70" rx="6" fill="#0f172a" stroke="#334155" />
                <text x="10" y="20" font-size="10" font-weight="bold" fill="#cbd5e1">Compensation Point Check:</text>
                <text id="sim13_compStatus" x="10" y="45" font-size="11" font-weight="bold" fill="#a7f3d0">Normal Sunlight Zone</text>
                <text x="10" y="60" font-size="8" fill="#94a3b8">Photosynthesis > Respiration</text>
            </g>
        </svg>
    </div>

    <!-- 24 Hour Time Slider -->
    <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2">
        <div class="flex justify-between text-xs">
            <span class="text-slate-300 font-medium">Diurnal Clock Time (24h)</span>
            <span id="sim13_timeVal" class="text-amber-400 font-mono font-bold">12:00 (Noon)</span>
        </div>
        <input type="range" id="sim13_timeSlider" min="0" max="24" value="12" class="w-full accent-amber-500 cursor-pointer">
        <div class="flex justify-between text-[10px] text-slate-400 font-mono">
            <span>00:00 (Night)</span>
            <span>06:00 (Dawn: Comp. Pt)</span>
            <span>12:00 (Midday)</span>
            <span>18:00 (Dusk: Comp. Pt)</span>
            <span>24:00 (Night)</span>
        </div>
    </div>

    <div id="sim13_feedback" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Respiration runs 24 hours a day. In bright daylight, photosynthesis vastly exceeds respiration. At dawn and dusk (compensation points), rates match with zero net gas exchange. In dark night, plants consume O₂ and release CO₂.
    </div>
</div>
"""

    # Simulator 14: Respirometer Germination Lab (10.4)
    sims[14] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
            <span class="font-bold text-sm text-cyan-300">10.4 Germinating Seeds Respirometer</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-cyan-950 text-cyan-200 border border-cyan-500/30 font-mono">O₂ Uptake, CO₂ & Heat Assay</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center">
        <svg id="sim14_svg" viewBox="0 0 540 240" class="w-full h-full select-none">
            <!-- Sealed Conical Flask (Left) -->
            <polygon points="120,70 160,70 210,180 70,180" fill="#0284c7" opacity="0.2" stroke="#38bdf8" stroke-width="2" />
            <!-- Rubber Stopper -->
            <rect x="125" y="60" width="30" height="15" fill="#475569" />

            <!-- Active Germinating Seeds inside flask -->
            <g id="sim14_seeds" fill="#d97706">
                <ellipse cx="110" cy="165" rx="10" ry="7" />
                <ellipse cx="135" cy="170" rx="9" ry="6" />
                <ellipse cx="160" cy="165" rx="10" ry="7" />
                <ellipse cx="120" cy="155" rx="8" ry="6" />
                <ellipse cx="145" cy="155" rx="8" ry="6" />
            </g>
            <text x="140" y="195" font-size="9" font-weight="bold" fill="#fde68a" text-anchor="middle">Germinating Seeds</text>

            <!-- Suspended KOH Test Tube inside flask -->
            <rect x="133" y="80" width="14" height="40" rx="6" fill="#f43f5e" opacity="0.8" stroke="#fda4af" />
            <text x="140" y="75" font-size="8" fill="#fda4af" text-anchor="middle">KOH</text>

            <!-- Delivery Tube connecting to water beaker -->
            <path d="M 140 60 L 140 35 L 360 35 L 360 170" stroke="#bae6fd" stroke-width="4" stroke-linecap="round" fill="none" />
            
            <!-- Colored Water Rising in Delivery Tube -->
            <line id="sim14_riseLine" x1="360" y1="170" x2="360" y2="100" stroke="#f43f5e" stroke-width="6" stroke-linecap="round" />

            <!-- Beaker with Colored Liquid on Right -->
            <rect x="320" y="140" width="80" height="60" rx="4" fill="#0284c7" opacity="0.2" stroke="#38bdf8" stroke-width="2" />
            <rect x="322" y="160" width="76" height="38" fill="#f43f5e" opacity="0.7" />
            <text x="360" y="215" font-size="9" fill="#94a3b8" text-anchor="middle">Colored Water Reservoir</text>

            <!-- Thermometer in Thermos Flask (Top Right Inset) -->
            <g transform="translate(430, 60)">
                <rect x="0" y="0" width="90" height="90" rx="6" fill="#0f172a" stroke="#334155" />
                <text x="45" y="18" font-size="9" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Thermos Heat Test</text>
                <text id="sim14_tempDisplay" x="45" y="45" font-size="14" font-weight="bold" fill="#f87171" text-anchor="middle">+3.5°C Rise</text>
                <text x="45" y="65" font-size="8" fill="#94a3b8" text-anchor="middle">Exothermic Energy</text>
            </g>
        </svg>
    </div>

    <!-- Controls -->
    <div class="flex flex-wrap items-center justify-between gap-3">
        <button id="sim14_btnToggleSeeds" class="px-3 py-1.5 rounded bg-emerald-700 text-white hover:bg-emerald-600 text-xs font-semibold transition">Specimen: Live Germinating Seeds</button>
        <button id="sim14_btnLimeWater" class="px-3 py-1.5 rounded bg-cyan-700 text-white hover:bg-cyan-600 text-xs font-semibold transition">Test Lime Water Turbidity</button>
        <button id="sim14_btnReset" class="px-3 py-1.5 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs font-semibold transition">Reset Respirometer</button>
    </div>

    <div id="sim14_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Germinating seeds consume oxygen. The CO₂ produced is trapped by KOH, creating partial suction that draws colored water up the tube. Cellular respiration releases measurable heat!
    </div>
</div>
"""

    # Simulator 15: Soil Aeration & Mangrove Pneumatophore Simulator (10.4)
    sims[15] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
            <span class="font-bold text-sm text-emerald-300">10.4 Soil Aeration & Mangrove Adaptations</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-emerald-950 text-emerald-200 border border-emerald-500/30 font-mono">Root Asphyxiation vs Breathing Roots</span>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <!-- Pot Houseplant Root Health -->
        <div class="h-60 bg-slate-900 rounded-lg p-3 border border-slate-800 flex flex-col justify-between">
            <span class="text-xs font-bold text-cyan-300 block mb-1">Standard Garden Plant Root System</span>
            <div class="w-full h-36 bg-slate-950 rounded flex items-center justify-center relative overflow-hidden">
                <svg id="sim15_pot_svg" viewBox="0 0 200 120" class="w-full h-full">
                    <!-- Soil and Water level -->
                    <rect x="0" y="30" width="200" height="90" fill="#3e2723" opacity="0.7" />
                    <rect id="sim15_floodWater" x="0" y="30" width="200" height="90" fill="#0284c7" opacity="0.0" />
                    <!-- Roots -->
                    <path id="sim15_roots" d="M 100 30 Q 90 70 70 100 M 100 30 Q 110 70 130 100 M 100 50 Q 80 80 50 85 M 100 50 Q 120 80 150 85" stroke="#fde047" stroke-width="3" fill="none" stroke-linecap="round" />
                    <!-- Air pockets bubbles -->
                    <g id="sim15_airPockets" fill="#bae6fd" opacity="0.6">
                        <circle cx="60" cy="50" r="3" />
                        <circle cx="140" cy="60" r="3.5" />
                        <circle cx="85" cy="85" r="3" />
                        <circle cx="115" cy="85" r="3" />
                    </g>
                </svg>
            </div>
            <span id="sim15_potDesc" class="text-[11px] text-emerald-400 font-semibold text-center">Aerated: Roots breathe soil O₂ normally</span>
        </div>

        <!-- Mangrove Pneumatophores (Sundarbans) -->
        <div class="h-60 bg-slate-900 rounded-lg p-3 border border-slate-800 flex flex-col justify-between">
            <span class="text-xs font-bold text-emerald-300 block mb-1">Mangrove Pneumatophores (Breathing Roots)</span>
            <div class="w-full h-36 bg-slate-950 rounded flex items-center justify-center relative overflow-hidden">
                <svg viewBox="0 0 200 120" class="w-full h-full">
                    <!-- Swamp mud & Saline Water -->
                    <rect x="0" y="60" width="200" height="60" fill="#1c1917" />
                    <rect x="0" y="50" width="200" height="20" fill="#0369a1" opacity="0.6" />
                    <!-- Subterranean Root cable -->
                    <path d="M 10 100 Q 100 110 190 100" stroke="#78350f" stroke-width="4" fill="none" />
                    <!-- Upward Pencil Roots (Pneumatophores) growing against gravity -->
                    <line x1="50" y1="100" x2="50" y2="25" stroke="#84cc16" stroke-width="4" stroke-linecap="round" />
                    <line x1="90" y1="105" x2="90" y2="20" stroke="#84cc16" stroke-width="4.5" stroke-linecap="round" />
                    <line x1="130" y1="103" x2="130" y2="22" stroke="#84cc16" stroke-width="4" stroke-linecap="round" />
                    <line x1="165" y1="100" x2="165" y2="30" stroke="#84cc16" stroke-width="3.5" stroke-linecap="round" />
                    <!-- Lenticels (Breathing pores) on tips -->
                    <circle cx="50" cy="30" r="1.5" fill="#fef08a" />
                    <circle cx="90" cy="25" r="1.5" fill="#fef08a" />
                    <circle cx="130" cy="27" r="1.5" fill="#fef08a" />
                    <text x="100" y="15" font-size="8" font-weight="bold" fill="#fef08a" text-anchor="middle">Lenticel Pores Inhale O₂ Above Water</text>
                </svg>
            </div>
            <span class="text-[11px] text-emerald-400 font-semibold text-center">Negatively Geotropic: Inhales air in mudflats</span>
        </div>
    </div>

    <!-- Soil Flooding Slider -->
    <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2">
        <div class="flex justify-between text-xs">
            <span class="text-slate-300 font-medium">Pot Irrigation Water Level</span>
            <span id="sim15_levelText" class="text-cyan-400 font-mono font-bold">Optimal Moisture (50%)</span>
        </div>
        <input type="range" id="sim15_floodSlider" min="0" max="100" value="50" class="w-full accent-cyan-500 cursor-pointer">
        <div class="flex justify-between text-[10px] text-slate-400 font-mono">
            <span>Dry Soil (0%)</span>
            <span>Moist Aerated (50%)</span>
            <span>Waterlogged Asphyxiation (100%)</span>
        </div>
    </div>

    <div id="sim15_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Over-watering drowns root hair air pockets, leading to anaerobic suffocation and root rot. Mangroves avoid this via erect pencil-like pneumatophores with porous lenticels.
    </div>
</div>
"""

    # Simulator 16: Bose Crescograph & Parashara Herbal Anatomy (Ancient Heritage)
    sims[16] = """
<div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-slate-100 flex flex-col gap-4">
    <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-2">
        <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
            <span class="font-bold text-sm text-amber-300">Indian Botanical Heritage: Bose & Parashara</span>
        </div>
        <span class="text-xs px-2 py-0.5 rounded bg-amber-950 text-amber-200 border border-amber-500/30 font-mono">10,000× Crescograph & Vrikshayurveda</span>
    </div>

    <div class="relative w-full h-64 bg-slate-900 rounded-lg overflow-hidden border border-slate-800 flex items-center justify-center">
        <svg id="sim16_svg" viewBox="0 0 540 240" class="w-full h-full select-none">
            <!-- Crescograph Apparatus Stage (Left) -->
            <rect x="20" y="30" width="220" height="180" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2" />
            <text x="130" y="50" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">Bose Crescograph (1910s)</text>
            
            <!-- Compound Optical Lever & Smoked Glass Drum -->
            <circle cx="130" cy="120" r="45" fill="#090d16" stroke="#64748b" stroke-width="2" />
            <!-- Rotating Recording Stylus Tracing Pulse Wave -->
            <path id="sim16_traceWave" d="M 95 120 Q 110 100 130 120 T 165 120" stroke="#38bdf8" stroke-width="2" fill="none" />
            <circle cx="165" cy="120" r="3" fill="#f43f5e" />
            <text id="sim16_magText" x="130" y="185" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Magnification: 10,000×</text>

            <!-- Ancient Palm-Leaf Scroll of Parashara (Right) -->
            <rect x="280" y="30" width="240" height="180" rx="8" fill="#451a03" opacity="0.6" stroke="#b45309" stroke-width="2" />
            <text x="400" y="50" font-size="11" font-weight="bold" fill="#fef3c7" text-anchor="middle">Maharishi Parashara: Vrikshayurveda</text>
            
            <g transform="translate(300, 70)" fill="#fde68a" font-size="9" class="space-y-1">
                <text x="0" y="10" font-weight="bold">• Syandani (Conducting Vessels)</text>
                <text x="10" y="25" fill="#cbd5e1">Ancient Sanskrit name for xylem/phloem</text>
                <text x="0" y="45" font-weight="bold">• Tejas & Ahara-Rasa</text>
                <text x="10" y="60" fill="#cbd5e1">Solar light and soil sap nourishment</text>
                <text x="0" y="80" font-weight="bold">• Leaf Venation Classification</text>
                <text x="10" y="95" fill="#cbd5e1">Cataloged parallel vs reticulate veins</text>
            </g>
        </svg>
    </div>

    <!-- Controls -->
    <div class="flex flex-wrap items-center justify-between gap-3">
        <div class="flex gap-2">
            <button id="sim16_btnStimulant" class="px-3 py-1.5 rounded bg-emerald-700 text-white text-xs font-semibold hover:bg-emerald-600 transition">Apply Warm Stimulant</button>
            <button id="sim16_btnPoison" class="px-3 py-1.5 rounded bg-rose-700 text-white text-xs font-semibold hover:bg-rose-600 transition">Apply Anesthetic (Ether)</button>
        </div>
        <button id="sim16_btnMag" class="px-3 py-1.5 rounded bg-amber-600 text-white text-xs font-bold hover:bg-amber-500 transition">Toggle Magnification (100,000×)</button>
    </div>

    <div id="sim16_status" class="text-xs p-2.5 rounded bg-slate-900 border border-slate-800 text-slate-300">
        Acharya J.C. Bose's Crescograph proved that plant cells exhibit living rhythmic electrical contractions and sensitive responses to stimuli, linking modern plant physiology with ancient botanical insights.
    </div>
</div>
"""

    with open(".agents/class7_science_plants_sims.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Auto-generated simulators file for Class 7 Science Chapter 10: Life Processes in Plants."""\n\n')
        f.write("SIMULATORS = " + repr(sims) + "\n")

    print(f"Successfully generated class7_science_plants_sims.py with {len(sims)} simulators.")

if __name__ == "__main__":
    generate_sims()

