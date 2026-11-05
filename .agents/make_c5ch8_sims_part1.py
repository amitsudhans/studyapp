"""
Simulators 1 to 8 for NCERT Class 5 Science Chapter 8: Clothes - How Things are Made
Zero raw LaTeX! Clean Unicode symbols.
"""

import sys

SIMS = {}

# SIM 1: Baya Weaver Hanging Nest Architect
SIMS[1] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Baya Weaver Nest Simulator</span>
        <p class="text-[11px] text-slate-400">Observe how the male weaverbird weaves grass ribbons into a pendulous pouch nest with an entrance tube.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Tree Branch overhead -->
            <path d="M 40,25 Q 180,45 360,20" stroke="#78350f" stroke-width="12" stroke-linecap="round" fill="none"/>
            <path d="M 120,35 Q 100,60 80,75" stroke="#92400e" stroke-width="5" stroke-linecap="round" fill="none"/>
            <!-- Leaves on branch -->
            <ellipse cx="60" cy="20" rx="14" ry="6" fill="#15803d" transform="rotate(-15 60 20)"/>
            <ellipse cx="140" cy="40" rx="16" ry="7" fill="#16a34a" transform="rotate(20 140 40)"/>
            <ellipse cx="320" cy="22" rx="15" ry="6" fill="#15803d" transform="rotate(-10 320 22)"/>

            <!-- Suspended Nest Anchor Loop -->
            <path id="nestAnchor" d="M 190,38 Q 200,65 200,80 Q 210,65 210,38" stroke="#ca8a04" stroke-width="4" fill="none"/>

            <!-- Main Nest Chamber -->
            <g id="nestChamberGroup">
                <ellipse id="nestBody" cx="200" cy="115" rx="38" ry="42" fill="#854d0e" stroke="#eab308" stroke-width="2" opacity="0.85"/>
                <!-- Woven Texture Lines -->
                <path id="wovenGrid1" d="M 170,95 Q 200,85 230,95 M 165,110 Q 200,100 235,110 M 168,125 Q 200,115 232,125 M 175,140 Q 200,130 225,140" stroke="#fef08a" stroke-width="1.2" fill="none" opacity="0.7"/>
                <path id="wovenGrid2" d="M 180,85 Q 175,115 185,145 M 195,80 Q 195,115 198,150 M 210,80 Q 212,115 210,150 M 222,85 Q 226,115 220,145" stroke="#facc15" stroke-width="1.2" fill="none" opacity="0.6"/>
            </g>

            <!-- Downward Entrance Tube (Stage 3) -->
            <g id="nestTubeGroup" class="transition-opacity duration-300">
                <path id="nestTube" d="M 185,145 C 185,185 190,210 195,220 C 205,220 215,220 220,210 C 220,185 222,150 222,145" fill="#713f12" stroke="#eab308" stroke-width="2"/>
                <!-- Tube mouth opening -->
                <ellipse cx="205" cy="216" rx="12" ry="5" fill="#0f172a" stroke="#ca8a04" stroke-width="1.5"/>
            </g>

            <!-- Animated Weaver Bird -->
            <g id="bayaBird" transform="translate(240, 100)">
                <ellipse cx="20" cy="15" rx="16" ry="11" fill="#eab308"/>
                <circle cx="32" cy="10" r="8" fill="#ca8a04"/>
                <circle cx="35" cy="9" r="2" fill="#0f172a"/>
                <polygon points="38,10 49,12 38,15" fill="#f97316"/>
                <!-- Bird wing -->
                <path d="M 10,15 Q 18,7 28,15 Q 18,22 10,15" fill="#a16207"/>
                <!-- Blade of grass in beak -->
                <path id="grassBlade" d="M 46,12 Q 55,20 62,35" stroke="#22c55e" stroke-width="2" fill="none">
                    <animate attributeName="stroke" values="#22c55e;#84cc16;#22c55e" dur="2s" repeatCount="indefinite"/>
                </path>
            </g>

            <!-- Status readout -->
            <rect x="15" y="195" width="160" height="36" rx="6" fill="#020617" stroke="#334155" opacity="0.9"/>
            <text x="25" y="210" fill="#94a3b8" font-size="9">Architect Stage:</text>
            <text id="sim1StageLabel" x="25" y="223" fill="#38bdf8" font-size="10" font-weight="bold">Stage 1: Branch Loop</text>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-2">
        <button onclick="setSim1Stage(1)" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-slate-700 text-xs font-semibold text-slate-200">1. Suspended Loop</button>
        <button onclick="setSim1Stage(2)" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-slate-700 text-xs font-semibold text-slate-200">2. Interlaced Egg Chamber</button>
        <button onclick="setSim1Stage(3)" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-slate-700 text-xs font-semibold text-slate-200">3. Downward Tube</button>
    </div>
    <div id="sim1Explanation" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        The male baya weaver strips tough, fibrous grass and ties it around a drooping twig to create an anchored vertical loop.
    </div>
</div>
"""

# SIM 2: Warp and Weft Loom Grid (Activity 1)
SIMS[2] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block mb-1">Loom Weaving: Warp & Weft Simulator</span>
        <p class="text-[11px] text-slate-400">Discover how vertical warp (tana) and horizontal weft (bana) interlock to create solid cloth.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg id="sim2LoomSvg" viewBox="0 0 400 240" class="w-full h-full">
            <!-- Loom wooden frame -->
            <rect x="50" y="20" width="300" height="200" rx="8" fill="none" stroke="#78350f" stroke-width="10"/>
            <rect x="55" y="25" width="290" height="190" fill="#0f172a"/>

            <!-- Longitudinal Warp Threads (Vertical - Blue) -->
            <g id="sim2WarpGroup" stroke="#38bdf8" stroke-width="3" stroke-linecap="round">
                <line x1="90" y1="25" x2="90" y2="215"/>
                <line x1="120" y1="25" x2="120" y2="215"/>
                <line x1="150" y1="25" x2="150" y2="215"/>
                <line x1="180" y1="25" x2="180" y2="215"/>
                <line x1="210" y1="25" x2="210" y2="215"/>
                <line x1="240" y1="25" x2="240" y2="215"/>
                <line x1="270" y1="25" x2="270" y2="215"/>
                <line x1="300" y1="25" x2="300" y2="215"/>
            </g>

            <!-- Weft Threads (Horizontal - Amber/Orange) -->
            <g id="sim2WeftGroup">
                <!-- Row 1: Over-Under pattern (y=60) -->
                <path d="M 70,60 L 320,60" stroke="#f59e0b" stroke-width="6" stroke-linecap="round" stroke-dasharray="15,15"/>
                <!-- Row 2: Under-Over pattern (y=90) -->
                <path d="M 70,90 L 320,90" stroke="#f59e0b" stroke-width="6" stroke-linecap="round" stroke-dashoffset="15" stroke-dasharray="15,15"/>
                <!-- Row 3: Over-Under pattern (y=120) -->
                <path d="M 70,120 L 320,120" stroke="#f59e0b" stroke-width="6" stroke-linecap="round" stroke-dasharray="15,15"/>
            </g>

            <!-- Moving Shuttle with Active Yarn (Row 4, y=150) -->
            <g id="sim2Shuttle" transform="translate(100, 150)">
                <ellipse cx="0" cy="0" rx="28" ry="8" fill="#ca8a04" stroke="#fef08a" stroke-width="1.5"/>
                <circle cx="0" cy="0" r="4" fill="#f97316"/>
                <path d="M -15,0 L 15,0" stroke="#ef4444" stroke-width="2"/>
            </g>

            <!-- Labels -->
            <text x="90" y="16" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">Warp (Tana) ↑</text>
            <text x="360" y="153" fill="#f59e0b" font-size="9" font-weight="bold">Weft (Bana) →</text>
        </svg>
    </div>
    <div class="flex items-center justify-between gap-2">
        <button onclick="stepSim2Weave()" class="flex-1 p-2 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white transition-colors">
            Throw Shuttle (Insert Next Weft Row)
        </button>
        <button onclick="resetSim2Loom()" class="p-2 bg-slate-800 hover:bg-slate-700 rounded-lg text-xs font-semibold text-slate-300">
            Reset Loom
        </button>
    </div>
    <div id="sim2Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        Row 1 to 3 woven: Notice how the weft alternates over and under each warp thread, locking the structure securely.
    </div>
</div>
"""

# SIM 3: India's 4,000-Year Handloom Heritage Atlas
SIMS[3] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">India's Handloom Heritage Atlas</span>
        <p class="text-[11px] text-slate-400">Explore three legendary Indian handloom traditions: Kanjeevaram silk, Kashmiri Pashmina, and Odisha/Gujarat Ikat.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Simplified India Map Outline Contour -->
            <path d="M 180,25 C 200,20 220,35 220,55 C 230,70 250,85 240,110 C 260,120 280,140 250,150 C 230,170 210,210 200,230 C 190,210 170,170 150,150 C 120,140 140,120 150,100 C 145,80 160,50 180,25 Z" fill="#1e293b" stroke="#475569" stroke-width="1.5" opacity="0.6"/>

            <!-- Region 1: Kashmir (Pashmina) -->
            <g id="pinPashmina" class="cursor-pointer" onclick="selectHandloom('pashmina')">
                <circle cx="195" cy="45" r="10" fill="#ec4899" stroke="#fbcfe8" stroke-width="2">
                    <animate attributeName="r" values="8;12;8" dur="2s" repeatCount="indefinite"/>
                </circle>
                <text x="212" y="49" fill="#f472b6" font-size="10" font-weight="bold">Kashmir (Pashmina)</text>
            </g>

            <!-- Region 2: Gujarat / Odisha (Ikat) -->
            <g id="pinIkat" class="cursor-pointer" onclick="selectHandloom('ikat')">
                <circle cx="160" cy="115" r="9" fill="#06b6d4" stroke="#a5f3fc" stroke-width="2"/>
                <circle cx="235" cy="130" r="9" fill="#06b6d4" stroke="#a5f3fc" stroke-width="2"/>
                <text x="140" y="132" fill="#22d3ee" font-size="9" font-weight="bold" text-anchor="end">Gujarat</text>
                <text x="248" y="134" fill="#22d3ee" font-size="9" font-weight="bold">Odisha (Ikat)</text>
            </g>

            <!-- Region 3: Tamil Nadu (Kanjeevaram) -->
            <g id="pinKanjeevaram" class="cursor-pointer" onclick="selectHandloom('kanjeevaram')">
                <circle cx="190" cy="195" r="10" fill="#eab308" stroke="#fef08a" stroke-width="2">
                    <animate attributeName="r" values="8;12;8" dur="2s" repeatCount="indefinite"/>
                </circle>
                <text x="208" y="199" fill="#facc15" font-size="10" font-weight="bold">Tamil Nadu (Kanjeevaram)</text>
            </g>

            <!-- Interactive Swatch Display Panel -->
            <rect x="20" y="20" width="105" height="85" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="26" y="34" fill="#94a3b8" font-size="8" font-weight="bold">TEXTILE PROFILE</text>
            <text id="swatchTitle" x="26" y="48" fill="#eab308" font-size="9" font-weight="bold">Kanjeevaram</text>
            <text id="swatchOrigin" x="26" y="60" fill="#cbd5e1" font-size="7.5">Kanchipuram, TN</text>
            <text id="swatchFibre" x="26" y="72" fill="#94a3b8" font-size="7.5">Mulberry Silk + Zari</text>
            <text id="swatchFeature" x="26" y="84" fill="#38bdf8" font-size="7.5">Temple Borders</text>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-2">
        <button onclick="selectHandloom('kanjeevaram')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-amber-500/50 text-xs font-semibold text-amber-300">Kanjeevaram Silk</button>
        <button onclick="selectHandloom('pashmina')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-pink-500/50 text-xs font-semibold text-pink-300">Pashmina Wool</button>
        <button onclick="selectHandloom('ikat')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-cyan-500/50 text-xs font-semibold text-cyan-300">Ikat Tie-Dye</button>
    </div>
    <div id="sim3Details" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Kanjeevaram Silk (Tamil Nadu):</strong> Handwoven using three-ply mulberry silk and pure silver/gold zari, featuring iconic interlocking temple borders.
    </div>
</div>
"""

# SIM 4: Charkha Spinning & Twist Physics
SIMS[4] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Charkha Spinning & Twist Physics</span>
        <p class="text-[11px] text-slate-400">See how drawing and spinning raw cotton creates surface friction, converting weak fluff into strong yarn.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Wooden Base Frame -->
            <rect x="50" y="190" width="300" height="12" rx="3" fill="#78350f" stroke="#b45309" stroke-width="1.5"/>
            <rect x="110" y="120" width="10" height="70" fill="#92400e"/>
            <rect x="310" y="150" width="8" height="40" fill="#92400e"/>

            <!-- Large Drive Wheel (Charkha Wheel) -->
            <g id="charkhaWheel" transform="translate(115, 120)">
                <circle cx="0" cy="0" r="60" fill="none" stroke="#d97706" stroke-width="4"/>
                <circle cx="0" cy="0" r="5" fill="#f59e0b"/>
                <!-- 8 Spokes -->
                <line x1="0" y1="-60" x2="0" y2="60" stroke="#b45309" stroke-width="2"/>
                <line x1="-60" y1="0" x2="60" y2="0" stroke="#b45309" stroke-width="2"/>
                <line x1="-42" y1="-42" x2="42" y2="42" stroke="#b45309" stroke-width="2"/>
                <line x1="-42" y1="42" x2="42" y2="-42" stroke="#b45309" stroke-width="2"/>
            </g>

            <!-- Drive Cord from Wheel to Spindle -->
            <path d="M 115,60 L 314,146 M 115,180 L 314,154" stroke="#fde047" stroke-width="1.5" stroke-dasharray="4,2"/>

            <!-- Spindle (Takli / Spindle Point) -->
            <line x1="290" y1="150" x2="340" y2="150" stroke="#94a3b8" stroke-width="3"/>
            <polygon points="340,150 334,146 334,154" fill="#cbd5e1"/>

            <!-- Raw Cotton Sliver being Drawn and Twisted -->
            <g id="cottonSliver">
                <!-- Fluffy cloud of raw cotton -->
                <ellipse cx="210" cy="150" rx="22" ry="14" fill="#ffffff" opacity="0.9"/>
                <ellipse cx="200" cy="146" rx="16" ry="10" fill="#f8fafc" opacity="0.95"/>
                <!-- Tapering twisted yarn leading into spindle -->
                <path d="M 225,150 Q 260,150 325,150" stroke="#f1f5f9" stroke-width="3" stroke-dasharray="3,1" id="spinningYarnPath"/>
            </g>

            <!-- Tensile Strength Gauge -->
            <rect x="25" y="25" width="130" height="42" rx="6" fill="#020617" stroke="#334155" opacity="0.9"/>
            <text x="35" y="40" fill="#94a3b8" font-size="8">YARN TENSILE STRENGTH</text>
            <rect x="35" y="46" width="110" height="10" rx="3" fill="#1e293b"/>
            <rect id="gaugeBar" x="35" y="46" width="75" height="10" rx="3" fill="#22c55e"/>
            <text id="gaugeText" x="90" y="54" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">70% Tensile</text>
        </svg>
    </div>
    <div class="flex items-center gap-3">
        <label class="text-xs text-slate-300 font-semibold whitespace-nowrap">Charkha Speed:</label>
        <input type="range" id="charkhaSlider" min="0" max="100" value="50" oninput="updateCharkhaSpeed(this.value)" class="w-full accent-amber-500">
        <span id="speedDisplay" class="text-xs font-bold text-amber-400 w-12 text-right">50 rpm</span>
    </div>
    <div id="sim4Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        As the wheel turns, the spindle spins rapidly. The twist packs parallel cotton fibres together, increasing frictional interlocking and tensile strength.
    </div>
</div>
"""

# SIM 5: Natural Fibre Microscope & Breathability
SIMS[5] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-teal-400 uppercase tracking-wider block mb-1">Natural Fibre Micro-Lab</span>
        <p class="text-[11px] text-slate-400">Magnify plant and animal fibres to reveal the microscopic structures that give each fabric unique qualities.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Circular Microscope Field of View -->
            <circle cx="200" cy="120" r="95" fill="#020617" stroke="#0ea5e9" stroke-width="4"/>
            <circle cx="200" cy="120" r="92" fill="#0f172a"/>

            <!-- Microscopic Fibre Visualizer -->
            <g id="microscopeFibreView">
                <!-- Default: Cotton (Twisted ribbon with lumen) -->
                <path d="M 125,60 Q 155,90 145,120 Q 135,150 165,180" stroke="#f8fafc" stroke-width="14" stroke-linecap="round" fill="none"/>
                <path d="M 125,60 Q 155,90 145,120 Q 135,150 165,180" stroke="#cbd5e1" stroke-width="4" stroke-dasharray="10,8" fill="none"/>
                <path d="M 235,60 Q 255,90 245,130 Q 235,160 265,180" stroke="#f8fafc" stroke-width="12" stroke-linecap="round" fill="none"/>
            </g>

            <!-- Crosshairs -->
            <line x1="200" y1="28" x2="200" y2="212" stroke="#38bdf8" stroke-width="0.75" stroke-dasharray="4,4" opacity="0.4"/>
            <line x1="108" y1="120" x2="292" y2="120" stroke="#38bdf8" stroke-width="0.75" stroke-dasharray="4,4" opacity="0.4"/>

            <!-- Magnification badge -->
            <rect x="25" y="25" width="85" height="28" rx="6" fill="#020617" stroke="#334155" opacity="0.9"/>
            <text x="35" y="42" fill="#38bdf8" font-size="10" font-weight="bold">400× ZOOM</text>

            <!-- Fibre Info Overlay -->
            <rect x="25" y="175" width="130" height="42" rx="6" fill="#020617" stroke="#334155" opacity="0.9"/>
            <text id="fibreNameTag" x="35" y="190" fill="#2dd4bf" font-size="9" font-weight="bold">Cotton Fibre</text>
            <text id="fibreOriginTag" x="35" y="202" fill="#94a3b8" font-size="7.5">Plant Seed Pod (Cellulose)</text>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5">
        <button onclick="viewFibre('cotton')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-slate-700 text-xs font-semibold text-slate-200">Cotton</button>
        <button onclick="viewFibre('linen')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-slate-700 text-xs font-semibold text-slate-200">Linen/Flax</button>
        <button onclick="viewFibre('wool')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-slate-700 text-xs font-semibold text-slate-200">Wool</button>
        <button onclick="viewFibre('silk')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-slate-700 text-xs font-semibold text-slate-200">Silk</button>
    </div>
    <div id="sim5Explanation" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Cotton:</strong> Under magnification, cotton appears like a flat, twisted ribbon with natural spirals that provide air channels for high breathability and sweat absorption.
    </div>
</div>
"""

# SIM 6: Silkworm Metamorphosis & Cocoon Lab
SIMS[6] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Silkworm Metamorphosis & Cocoon Lab</span>
        <p class="text-[11px] text-slate-400">Step through the 4 life stages of Bombyx mori and see how a single cocoon yields up to 1,000 metres of silk.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Central Stage Display Stage Canvas -->
            <g id="silkwormStageCanvas">
                <!-- Stage 2 default: Caterpillar on Mulberry Leaf -->
                <path d="M 60,190 Q 200,60 340,190 Q 200,240 60,190" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
                <path d="M 60,190 Q 200,125 340,190" stroke="#16a34a" stroke-width="3" fill="none"/>
                <!-- Caterpillar Segments -->
                <g id="caterpillarBody" transform="translate(130, 115)">
                    <circle cx="20" cy="20" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
                    <circle cx="42" cy="22" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
                    <circle cx="64" cy="20" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
                    <circle cx="86" cy="18" r="14" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
                    <circle cx="108" cy="15" r="12" fill="#eab308" stroke="#ca8a04" stroke-width="1.5"/>
                    <!-- Head & eye -->
                    <circle cx="112" cy="13" r="2.5" fill="#0f172a"/>
                </g>
            </g>

            <!-- Reeled Silk Filament Counter (Top Right) -->
            <rect x="250" y="20" width="135" height="42" rx="6" fill="#020617" stroke="#334155" opacity="0.9"/>
            <text x="260" y="34" fill="#94a3b8" font-size="8">SINGLE COCOON FILAMENT</text>
            <text id="filamentLengthText" x="260" y="52" fill="#fbbf24" font-size="12" font-weight="bold">850 Metres</text>

            <!-- Current Stage Indicator -->
            <rect x="20" y="20" width="145" height="42" rx="6" fill="#020617" stroke="#334155" opacity="0.9"/>
            <text x="30" y="34" fill="#94a3b8" font-size="8">CURRENT STAGE</text>
            <text id="silkStageTitle" x="30" y="52" fill="#38bdf8" font-size="11" font-weight="bold">2. Voracious Larva</text>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5">
        <button onclick="setSilkStage(1)" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-slate-700 text-xs font-semibold text-slate-200">1. Tiny Egg</button>
        <button onclick="setSilkStage(2)" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-slate-700 text-xs font-semibold text-slate-200">2. Caterpillar</button>
        <button onclick="setSilkStage(3)" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-slate-700 text-xs font-semibold text-slate-200">3. Silk Cocoon</button>
        <button onclick="setSilkStage(4)" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-slate-700 text-xs font-semibold text-slate-200">4. Adult Moth</button>
    </div>
    <div id="sim6Description" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        Stage 2: The caterpillar feeds continuously on fresh mulberry leaves for about 30 days, growing rapidly before preparing to pupate.
    </div>
</div>
"""

# SIM 7: Synthetic vs Natural Thermal Safety Duel
SIMS[7] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-rose-400 uppercase tracking-wider block mb-1">Thermal Flame Safety Duel</span>
        <p class="text-[11px] text-slate-400">Discover why 100% cotton is life-saving around kitchen flames and firecrackers, while synthetic polymers melt dangerously.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Left Side: Pure Natural Cotton -->
            <g id="cottonSafetySide">
                <rect x="30" y="25" width="160" height="190" rx="8" fill="#0f172a" stroke="#22c55e" stroke-width="1.5"/>
                <text x="110" y="45" fill="#4ade80" font-size="10" font-weight="bold" text-anchor="middle">100% NATURAL COTTON</text>
                <!-- Fabric swatch -->
                <rect x="70" y="60" width="80" height="70" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
                <!-- Flame animation (safe ash) -->
                <path d="M 110,150 Q 100,135 110,120 Q 120,135 110,150" fill="#f97316">
                    <animate attributeName="d" values="M 110,150 Q 100,135 110,120 Q 120,135 110,150; M 110,150 Q 95,130 110,115 Q 125,130 110,150; M 110,150 Q 100,135 110,120 Q 120,135 110,150" dur="1.2s" repeatCount="indefinite"/>
                </path>
                <text x="110" y="172" fill="#cbd5e1" font-size="9" text-anchor="middle">Chars cleanly to soft ash</text>
                <text x="110" y="195" fill="#4ade80" font-size="9" font-weight="bold" text-anchor="middle">✓ SAFE FOR KITCHEN</text>
            </g>

            <!-- Right Side: Synthetic Polyester -->
            <g id="syntheticSafetySide">
                <rect x="210" y="25" width="160" height="190" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
                <text x="290" y="45" fill="#f87171" font-size="10" font-weight="bold" text-anchor="middle">SYNTHETIC POLYESTER</text>
                <!-- Fabric swatch -->
                <rect x="250" y="60" width="80" height="70" rx="4" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
                <!-- Molten dripping plastic bead -->
                <circle cx="290" cy="130" r="12" fill="#dc2626"/>
                <path d="M 288,142 Q 290,165 290,175" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>
                <circle cx="290" cy="178" r="4" fill="#ef4444"/>
                <text x="290" y="192" fill="#fca5a5" font-size="8.5" text-anchor="middle">Melts into sticky hot molten plastic</text>
                <text x="290" y="206" fill="#ef4444" font-size="9" font-weight="bold" text-anchor="middle">⚠ SEVERE BURN HAZARD</text>
            </g>
        </svg>
    </div>
    <div class="flex items-center justify-between gap-2">
        <button onclick="testSafetyReaction('cotton')" class="flex-1 p-2 bg-emerald-700 hover:bg-emerald-600 rounded-lg text-xs font-bold text-white">Inspect Cotton Reaction</button>
        <button onclick="testSafetyReaction('synthetic')" class="flex-1 p-2 bg-rose-700 hover:bg-rose-600 rounded-lg text-xs font-bold text-white">Inspect Synthetic Reaction</button>
    </div>
    <div id="sim7Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        When exposed to fire, cotton chars into harmless powdery ash. Synthetic polyester melts into boiling plastic that sticks to human skin, causing disastrous burns.
    </div>
</div>
"""

# SIM 8: Common Tailorbird Leaf Stitcher
SIMS[8] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Tailorbird Leaf Stitching Simulator</span>
        <p class="text-[11px] text-slate-400">Watch the tailorbird pierce eyelet holes and knot plant fibres like rivets to create an enclosed cradle nest.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Two Overlapping Broad Green Leaves -->
            <path d="M 80,40 Q 160,110 130,210 Q 70,140 80,40" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
            <path d="M 220,40 Q 140,110 170,210 Q 230,140 220,40" fill="#16a34a" stroke="#4ade80" stroke-width="2"/>

            <!-- Central Seam where leaves overlap -->
            <g id="leafStitchLine">
                <!-- Eyelet Holes & Thread Stitches -->
                <circle cx="150" cy="70" r="3" fill="#020617" stroke="#ca8a04"/>
                <circle cx="150" cy="100" r="3" fill="#020617" stroke="#ca8a04"/>
                <circle cx="150" cy="130" r="3" fill="#020617" stroke="#ca8a04"/>
                <circle cx="150" cy="160" r="3" fill="#020617" stroke="#ca8a04"/>
                <circle cx="150" cy="190" r="3" fill="#020617" stroke="#ca8a04"/>

                <!-- Thread connecting eyelets -->
                <path d="M 150,70 L 150,190" stroke="#fef08a" stroke-width="2" stroke-dasharray="8,6"/>

                <!-- Tangled Thread Rivet Knots on outside -->
                <circle cx="147" cy="70" r="4" fill="#fef08a"/>
                <circle cx="147" cy="100" r="4" fill="#fef08a"/>
                <circle cx="147" cy="130" r="4" fill="#fef08a"/>
                <circle cx="147" cy="160" r="4" fill="#fef08a"/>
                <circle cx="147" cy="190" r="4" fill="#fef08a"/>
            </g>

            <!-- Tailorbird with Needle-like Beak -->
            <g id="tailorBird" transform="translate(190, 80)">
                <ellipse cx="40" cy="30" rx="20" ry="14" fill="#65a30d"/>
                <circle cx="56" cy="22" r="10" fill="#84cc16"/>
                <circle cx="60" cy="20" r="2" fill="#0f172a"/>
                <!-- Long slender needle beak -->
                <polygon points="65,22 92,23 65,26" fill="#78350f"/>
                <!-- Spider silk fibre in beak -->
                <path d="M 90,23 Q 110,40 120,60" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="2,2" fill="none"/>
            </g>

            <!-- Readout panel -->
            <rect x="250" y="160" width="135" height="60" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="260" y="178" fill="#4ade80" font-size="9" font-weight="bold">RIVET STITCHING</text>
            <text x="260" y="192" fill="#cbd5e1" font-size="7.5">Thread: Spider Silk / Lint</text>
            <text x="260" y="204" fill="#94a3b8" font-size="7.5">Knots: Fluffed exterior stops</text>
        </svg>
    </div>
    <div class="flex items-center gap-2">
        <button onclick="addTailorbirdStitch()" class="flex-1 p-2 bg-lime-700 hover:bg-lime-600 rounded-lg text-xs font-bold text-white">
            Pierce Eyelet & Thread Stitch
        </button>
        <button onclick="resetTailorbirdStitches()" class="p-2 bg-slate-800 hover:bg-slate-700 rounded-lg text-xs font-semibold text-slate-300">
            Reset Leaves
        </button>
    </div>
    <div id="sim8Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        The tailorbird uses its sharp bill like a sewing needle, piercing matching holes and tangling thread ends into knots so they cannot slip back through.
    </div>
</div>
"""

print("Simulators 1 to 8 defined.")

