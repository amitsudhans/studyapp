# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 1: Shapes Around Us - Simulators 1 to 8
Generates HTML/SVG markup for simulators 1 to 8.
"""

simulators_part1 = {}

# Simulator 1: Building Monument Models
simulators_part1[1] = """
<div id="sim1-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🏛️</span> India Gate Monument Block Builder
            </h3>
            <p class="text-xs text-slate-400">Assemble 3D geometric blocks: foundation cuboids, pillars, arch, and roof slab.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/10 text-amber-300 border border-amber-500/20 font-medium">3D Architecture</span>
    </div>

    <!-- Monument Canvas -->
    <div class="relative flex-1 min-h-[260px] flex items-center justify-center my-3 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800/80 overflow-hidden">
        <svg id="sim1-svg" viewBox="0 0 460 280" class="w-full h-full max-h-[270px]">
            <!-- Ground Line -->
            <line x1="20" y1="250" x2="440" y2="250" stroke="#475569" stroke-width="3" stroke-dasharray="6,4"/>
            <text x="30" y="270" fill="#64748b" font-size="11" font-family="sans-serif">Ground Baseline</text>

            <!-- Foundation Base (Cuboid) -->
            <g id="sim1-base" class="transition-all duration-500 opacity-0 transform translate-y-4">
                <!-- Base bottom face -->
                <polygon points="60,250 400,250 420,235 80,235" fill="#b45309" stroke="#d97706" stroke-width="1.5"/>
                <!-- Base front face -->
                <rect x="60" y="235" width="340" height="15" fill="#d97706" stroke="#f59e0b" stroke-width="1.5"/>
                <!-- Base top face -->
                <polygon points="60,235 400,235 420,220 80,220" fill="#f59e0b" stroke="#fbbf24" stroke-width="1.5"/>
                <text x="230" y="246" text-anchor="middle" fill="#1e1e24" font-size="10" font-weight="bold">Base Foundation: Wide Cuboid</text>
            </g>

            <!-- Left Pillar (Vertical Cuboid) -->
            <g id="sim1-pillar-left" class="transition-all duration-500 opacity-0 transform -translate-y-4">
                <!-- Front face -->
                <rect x="110" y="90" width="75" height="130" fill="#ea580c" stroke="#f97316" stroke-width="1.5"/>
                <!-- Side face -->
                <polygon points="185,90 200,80 200,210 185,220" fill="#c2410c" stroke="#ea580c" stroke-width="1.5"/>
                <!-- Top face -->
                <polygon points="110,90 185,90 200,80 125,80" fill="#fb923c" stroke="#fdba74" stroke-width="1.5"/>
                <text x="147" y="160" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">Pillar 1</text>
            </g>

            <!-- Right Pillar (Vertical Cuboid) -->
            <g id="sim1-pillar-right" class="transition-all duration-500 opacity-0 transform -translate-y-4">
                <!-- Front face -->
                <rect x="275" y="90" width="75" height="130" fill="#ea580c" stroke="#f97316" stroke-width="1.5"/>
                <!-- Side face -->
                <polygon points="350,90 365,80 365,210 350,220" fill="#c2410c" stroke="#ea580c" stroke-width="1.5"/>
                <!-- Top face -->
                <polygon points="275,90 350,90 365,80 290,80" fill="#fb923c" stroke="#fdba74" stroke-width="1.5"/>
                <text x="312" y="160" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">Pillar 2</text>
            </g>

            <!-- Central Gateway Arch -->
            <g id="sim1-arch" class="transition-all duration-500 opacity-0">
                <path d="M 185,220 L 185,150 Q 230,105 275,150 L 275,220 Z" fill="#334155" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
                <path d="M 185,150 Q 230,105 275,150" fill="none" stroke="#38bdf8" stroke-width="3"/>
                <text x="230" y="170" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Curved Arch Portal</text>
            </g>

            <!-- Roof Beam / Cornice Slab (Cuboid) -->
            <g id="sim1-roof" class="transition-all duration-500 opacity-0 transform -translate-y-6">
                <!-- Front face -->
                <rect x="80" y="55" width="300" height="35" fill="#f59e0b" stroke="#fbbf24" stroke-width="1.5"/>
                <!-- Side face -->
                <polygon points="380,55 400,45 400,80 380,90" fill="#d97706" stroke="#b45309" stroke-width="1.5"/>
                <!-- Top face -->
                <polygon points="80,55 380,55 400,45 100,45" fill="#fde68a" stroke="#fef3c7" stroke-width="1.5"/>
                <!-- Attic pediment -->
                <rect x="130" y="30" width="200" height="25" fill="#d97706" stroke="#b45309" stroke-width="1.5"/>
                <polygon points="330,30 345,22 345,47 330,55" fill="#b45309"/>
                <polygon points="130,30 330,30 345,22 145,22" fill="#fbbf24"/>
                <text x="230" y="77" text-anchor="middle" fill="#78350f" font-size="12" font-weight="extrabold">INDIA GATE CORNICE SLAB</text>
            </g>
        </svg>

        <div id="sim1-info" class="absolute bottom-2 left-3 right-3 bg-slate-900/90 backdrop-blur px-3 py-1.5 rounded-lg border border-slate-700/80 text-xs text-center text-slate-300">
            Click step buttons below to assemble India Gate piece by piece!
        </div>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-2 sm:grid-cols-5 gap-2 pt-1">
        <button id="sim1-btn-base" onclick="sim1Step(1)" class="px-3 py-2 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-medium text-xs transition shadow-md">1. Add Base</button>
        <button id="sim1-btn-pillars" onclick="sim1Step(2)" class="px-3 py-2 rounded-lg bg-orange-600 hover:bg-orange-500 text-white font-medium text-xs transition shadow-md">2. Add Pillars</button>
        <button id="sim1-btn-arch" onclick="sim1Step(3)" class="px-3 py-2 rounded-lg bg-sky-600 hover:bg-sky-500 text-white font-medium text-xs transition shadow-md">3. Add Arch</button>
        <button id="sim1-btn-roof" onclick="sim1Step(4)" class="px-3 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-medium text-xs transition shadow-md">4. Add Roof</button>
        <button id="sim1-btn-reset" onclick="sim1Step(0)" class="col-span-2 sm:col-span-1 px-3 py-2 rounded-lg bg-slate-700 hover:bg-slate-600 text-slate-200 font-medium text-xs transition shadow-md">↺ Reset</button>
    </div>
</div>
"""

# Simulator 2: Historic Brick Architecture
simulators_part1[2] = """
<div id="sim2-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🧱</span> Qutub Minar Storeys & Brick Bond Lab
            </h3>
            <p class="text-xs text-slate-400">Explore Qutub Minar's 5 storeys and test interlocking brick bond strength.</p>
        </div>
        <div class="flex gap-1.5">
            <button id="sim2-tab1-btn" onclick="sim2SetTab(1)" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">Minar Storeys</button>
            <button id="sim2-tab2-btn" onclick="sim2SetTab(2)" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Brick Bond Test</button>
        </div>
    </div>

    <!-- Tab 1: Qutub Minar Storeys -->
    <div id="sim2-tab1" class="flex-1 flex flex-col sm:flex-row gap-4 items-center justify-center my-3 bg-slate-950 rounded-xl p-3 border border-slate-800">
        <svg viewBox="0 0 200 260" class="h-60 w-44 shrink-0">
            <!-- Storey 1 (Base) -->
            <polygon id="sim2-s1" points="40,250 160,250 150,195 50,195" fill="#dc2626" stroke="#b91c1c" stroke-width="1.5" class="cursor-pointer transition hover:opacity-90" onclick="sim2SelectStorey(1)"/>
            <text x="100" y="225" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">Storey 1</text>

            <!-- Storey 2 -->
            <polygon id="sim2-s2" points="50,195 150,195 142,145 58,145" fill="#ea580c" stroke="#c2410c" stroke-width="1.5" class="cursor-pointer transition hover:opacity-90" onclick="sim2SelectStorey(2)"/>
            <text x="100" y="173" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">Storey 2</text>

            <!-- Storey 3 -->
            <polygon id="sim2-s3" points="58,145 142,145 135,100 65,100" fill="#f59e0b" stroke="#d97706" stroke-width="1.5" class="cursor-pointer transition hover:opacity-90" onclick="sim2SelectStorey(3)"/>
            <text x="100" y="125" text-anchor="middle" fill="#1e1e24" font-size="10" font-weight="bold">Storey 3</text>

            <!-- Storey 4 -->
            <polygon id="sim2-s4" points="65,100 135,100 128,60 72,60" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="1.5" class="cursor-pointer transition hover:opacity-90" onclick="sim2SelectStorey(4)"/>
            <text x="100" y="83" text-anchor="middle" fill="#1e293b" font-size="9" font-weight="bold">Storey 4 (Marble)</text>

            <!-- Storey 5 (Top) -->
            <polygon id="sim2-s5" points="72,60 128,60 122,25 78,25" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" class="cursor-pointer transition hover:opacity-90" onclick="sim2SelectStorey(5)"/>
            <text x="100" y="45" text-anchor="middle" fill="#1e293b" font-size="9" font-weight="bold">Storey 5</text>

            <!-- Balconies brackets -->
            <line x1="48" y1="195" x2="152" y2="195" stroke="#facc15" stroke-width="3"/>
            <line x1="56" y1="145" x2="144" y2="145" stroke="#facc15" stroke-width="3"/>
            <line x1="63" y1="100" x2="137" y2="100" stroke="#facc15" stroke-width="3"/>
            <line x1="70" y1="60" x2="130" y2="60" stroke="#facc15" stroke-width="3"/>
        </svg>

        <div class="flex-1 space-y-2 text-xs bg-slate-900/90 p-3 rounded-lg border border-slate-700/60 w-full">
            <div id="sim2-storey-title" class="text-sm font-bold text-amber-400">Total Minar: 5 Storeys (72.5 m)</div>
            <div id="sim2-storey-desc" class="text-slate-300 leading-relaxed">
                The Qutub Minar is the world's tallest brick minaret. It has 5 storeys and 379 spiral stone stairs climbing to the top.
            </div>
            <div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-800 text-[11px]">
                <div class="bg-slate-800/80 p-2 rounded">
                    <span class="text-slate-400 block">Total Height:</span>
                    <span class="text-emerald-400 font-bold">72.5 meters</span>
                </div>
                <div class="bg-slate-800/80 p-2 rounded">
                    <span class="text-slate-400 block">Total Stairs:</span>
                    <span class="text-sky-400 font-bold">379 stone steps</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Tab 2: Brick Masonry Running Bond vs Stack Bond -->
    <div id="sim2-tab2" class="hidden flex-1 flex flex-col items-center justify-center my-3 bg-slate-950 rounded-xl p-3 border border-slate-800">
        <div class="flex gap-3 mb-2">
            <button id="sim2-bond-running" onclick="sim2SetBond('running')" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600 text-white shadow">Running Bond (Interlocking)</button>
            <button id="sim2-bond-stack" onclick="sim2SetBond('stack')" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white">Stack Bond (Aligned)</button>
        </div>

        <svg id="sim2-brick-svg" viewBox="0 0 360 160" class="w-full max-w-[340px] h-36">
            <!-- Will be dynamically redrawn via JS -->
        </svg>

        <div id="sim2-bond-verdict" class="text-xs text-center mt-2 px-3 py-1 rounded bg-slate-900 text-slate-300 border border-slate-700">
            Running bond staggers vertical seams, spreading load across multiple bricks without continuous cracks!
        </div>
    </div>
</div>
"""

# Simulator 3: Prisms and Pyramids
simulators_part1[3] = """
<div id="sim3-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>📦</span> 3D Polyhedra Net Folder Studio
            </h3>
            <p class="text-xs text-slate-400">Fold 2D flat nets into 3D prisms and pyramids.</p>
        </div>
        <div class="flex gap-1.5">
            <button id="sim3-shape-prism" onclick="sim3SetShape('prism')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-indigo-600 text-white transition">Triangular Prism</button>
            <button id="sim3-shape-pyramid" onclick="sim3SetShape('pyramid')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Square Pyramid</button>
        </div>
    </div>

    <!-- 3D Net Canvas -->
    <div class="relative flex-1 min-h-[240px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim3-svg" viewBox="0 0 400 240" class="w-full h-full max-h-[240px]">
            <!-- Dynamic 3D net elements drawn by sim3Render() -->
        </svg>

        <div id="sim3-props-pill" class="absolute top-2 right-2 bg-slate-900/90 border border-slate-700/80 rounded-lg p-2 text-[11px] text-slate-300 shadow">
            <div class="font-bold text-amber-300 mb-1" id="sim3-prop-name">Triangular Prism</div>
            <div>Bases: <span class="text-sky-400 font-semibold" id="sim3-prop-bases">2 Triangles</span></div>
            <div>Sides: <span class="text-emerald-400 font-semibold" id="sim3-prop-sides">3 Rectangles</span></div>
            <div>Total Faces: <span class="text-amber-400 font-bold" id="sim3-prop-faces">5 Faces</span></div>
        </div>
    </div>

    <!-- Fold Slider Control -->
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-300 font-medium">Fold Progress (0% Flat Net ➔ 100% Closed Solid):</span>
            <span id="sim3-fold-val" class="text-amber-400 font-bold text-sm">0%</span>
        </div>
        <input id="sim3-slider" type="range" min="0" max="100" value="0" oninput="sim3OnFold(this.value)" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
    </div>
</div>
"""

# Simulator 4: Euler Formula Table
simulators_part1[4] = """
<div id="sim4-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🧪</span> Euler's Formula Calculator: F + V - E = 2
            </h3>
            <p class="text-xs text-slate-400">Straws = Edges, Clay Balls = Vertices. Verify Euler's rule on 3D skeletons.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 font-medium">Euler Invariant</span>
    </div>

    <!-- Shape Selector Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-2">
        <button id="sim4-btn-cube" onclick="sim4SelectShape('cube')" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">Cube</button>
        <button id="sim4-btn-triprism" onclick="sim4SelectShape('triprism')" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Triangular Prism</button>
        <button id="sim4-btn-sqpyr" onclick="sim4SelectShape('sqpyr')" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Square Pyramid</button>
        <button id="sim4-btn-pentpyr" onclick="sim4SelectShape('pentpyr')" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Pentagonal Pyramid</button>
    </div>

    <!-- 3D Wireframe Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim4-svg" viewBox="0 0 380 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered by sim4Render() -->
        </svg>
    </div>

    <!-- Euler Formula Verification Card -->
    <div class="grid grid-cols-4 gap-2 bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-center text-xs">
        <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
            <span class="text-slate-400 block text-[10px]">Faces (F)</span>
            <span id="sim4-f" class="text-amber-400 font-bold text-base">6</span>
        </div>
        <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
            <span class="text-slate-400 block text-[10px]">Vertices (V)</span>
            <span id="sim4-v" class="text-sky-400 font-bold text-base">8</span>
        </div>
        <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
            <span class="text-slate-400 block text-[10px]">Edges (E)</span>
            <span id="sim4-e" class="text-rose-400 font-bold text-base">12</span>
        </div>
        <div class="bg-emerald-950/60 p-2 rounded-lg border border-emerald-500/40">
            <span class="text-emerald-400 block text-[10px] font-bold">F + V - E</span>
            <span id="sim4-result" class="text-emerald-300 font-extrabold text-base">6 + 8 - 12 = 2</span>
        </div>
    </div>
</div>
"""

# Simulator 5: Cube Face Views
simulators_part1[5] = """
<div id="sim5-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🎲</span> Cube Face Views & Dice Opposites Lab
            </h3>
            <p class="text-xs text-slate-400">Dice rule: opposite pips sum to 7. Deduce hidden colors from 3 views.</p>
        </div>
        <div class="flex gap-1.5">
            <button id="sim5-tab1-btn" onclick="sim5SetTab(1)" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">Dice Opposites</button>
            <button id="sim5-tab2-btn" onclick="sim5SetTab(2)" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">3-View Color Puzzle</button>
        </div>
    </div>

    <!-- Tab 1: Dice Opposites Sum to 7 -->
    <div id="sim5-tab1" class="flex-1 flex flex-col items-center justify-center my-3 bg-slate-950 rounded-xl p-3 border border-slate-800">
        <div class="text-xs text-slate-300 mb-3 text-center">
            Click any face of the die to illuminate its opposite face across the cube:
        </div>
        <div class="grid grid-cols-6 gap-2 mb-4">
            <button onclick="sim5SelectDieFace(1)" class="w-10 h-10 rounded-lg bg-slate-800 hover:bg-amber-600 text-white font-bold text-base transition border border-slate-700 flex items-center justify-center">1</button>
            <button onclick="sim5SelectDieFace(2)" class="w-10 h-10 rounded-lg bg-slate-800 hover:bg-amber-600 text-white font-bold text-base transition border border-slate-700 flex items-center justify-center">2</button>
            <button onclick="sim5SelectDieFace(3)" class="w-10 h-10 rounded-lg bg-slate-800 hover:bg-amber-600 text-white font-bold text-base transition border border-slate-700 flex items-center justify-center">3</button>
            <button onclick="sim5SelectDieFace(4)" class="w-10 h-10 rounded-lg bg-slate-800 hover:bg-amber-600 text-white font-bold text-base transition border border-slate-700 flex items-center justify-center">4</button>
            <button onclick="sim5SelectDieFace(5)" class="w-10 h-10 rounded-lg bg-slate-800 hover:bg-amber-600 text-white font-bold text-base transition border border-slate-700 flex items-center justify-center">5</button>
            <button onclick="sim5SelectDieFace(6)" class="w-10 h-10 rounded-lg bg-slate-800 hover:bg-amber-600 text-white font-bold text-base transition border border-slate-700 flex items-center justify-center">6</button>
        </div>

        <div id="sim5-die-result" class="bg-slate-900 border border-slate-700 p-3 rounded-xl text-center text-xs space-y-1 w-full max-w-sm">
            <span class="text-amber-400 font-bold text-sm">Face 1 Selected</span>
            <div class="text-emerald-400 font-semibold text-sm">Opposite Face is 6 (1 + 6 = 7)</div>
            <p class="text-slate-400 text-[11px]">Opposite faces are parallel and never share an edge!</p>
        </div>
    </div>

    <!-- Tab 2: 3-View Color Puzzle -->
    <div id="sim5-tab2" class="hidden flex-1 flex flex-col items-center justify-center my-3 bg-slate-950 rounded-xl p-3 border border-slate-800">
        <div class="text-xs text-slate-300 mb-2 text-center">Three camera views of the same colored cube:</div>
        <div class="grid grid-cols-3 gap-3 mb-3 w-full max-w-md">
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800 text-center text-[10px]">
                <span class="text-amber-400 font-bold block mb-1">View 1</span>
                <span class="block text-rose-400">Top: Red</span>
                <span class="block text-sky-400">Front: Blue</span>
                <span class="block text-emerald-400">Right: Green</span>
            </div>
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800 text-center text-[10px]">
                <span class="text-amber-400 font-bold block mb-1">View 2</span>
                <span class="block text-rose-400">Top: Red</span>
                <span class="block text-emerald-400">Front: Green</span>
                <span class="block text-amber-300">Right: Yellow</span>
            </div>
            <div class="bg-slate-900 p-2 rounded-lg border border-slate-800 text-center text-[10px]">
                <span class="text-amber-400 font-bold block mb-1">View 3</span>
                <span class="block text-sky-400">Front: Blue</span>
                <span class="block text-emerald-400">Right: Green</span>
                <span class="block text-purple-400">Bottom: Purple</span>
            </div>
        </div>
        <button onclick="sim5SolveColorPuzzle()" class="px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition shadow">
            🔍 Deduce: What Color is Opposite Green?
        </button>
        <div id="sim5-color-verdict" class="text-xs text-center mt-2 text-slate-300"></div>
    </div>
</div>
"""

# Simulator 6: Sorting Shape Properties
simulators_part1[6] = """
<div id="sim6-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>⭕</span> 3D Solids Venn Diagram Sorter
            </h3>
            <p class="text-xs text-slate-400">Sort shapes by face properties. Triangular prism sits in the intersection!</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 font-medium">Venn Logic</span>
    </div>

    <!-- Venn Diagram Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim6-svg" viewBox="0 0 440 220" class="w-full h-full max-h-[220px]">
            <!-- Circle 1: Has Rectangular Faces -->
            <circle cx="170" cy="110" r="95" fill="#1e3a8a" fill-opacity="0.35" stroke="#3b82f6" stroke-width="2"/>
            <text x="120" y="40" fill="#60a5fa" font-size="11" font-weight="bold">Has Rectangular Faces</text>

            <!-- Circle 2: Has Triangular Faces -->
            <circle cx="270" cy="110" r="95" fill="#854d0e" fill-opacity="0.35" stroke="#eab308" stroke-width="2"/>
            <text x="320" y="40" text-anchor="end" fill="#fde047" font-size="11" font-weight="bold">Has Triangular Faces</text>

            <!-- Intersection Label -->
            <text x="220" y="105" text-anchor="middle" fill="#34d399" font-size="10" font-weight="extrabold">BOTH</text>
            <text x="220" y="120" text-anchor="middle" fill="#a7f3d0" font-size="9">Triangular</text>
            <text x="220" y="132" text-anchor="middle" fill="#a7f3d0" font-size="9">Prism</text>

            <!-- Placed Shapes will be updated dynamically -->
            <g id="sim6-placed-shapes"></g>
        </svg>
    </div>

    <!-- Shape Cards to Click / Sort -->
    <div class="grid grid-cols-3 sm:grid-cols-6 gap-1.5 pt-1">
        <button onclick="sim6PlaceShape('cube')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-blue-600 text-slate-200 text-[11px] font-medium transition">Cube</button>
        <button onclick="sim6PlaceShape('triprism')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-emerald-600 text-slate-200 text-[11px] font-medium transition">Tri Prism</button>
        <button onclick="sim6PlaceShape('sqpyr')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-amber-600 text-slate-200 text-[11px] font-medium transition">Sq Pyramid</button>
        <button onclick="sim6PlaceShape('cylinder')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-purple-600 text-slate-200 text-[11px] font-medium transition">Cylinder</button>
        <button onclick="sim6PlaceShape('cone')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-purple-600 text-slate-200 text-[11px] font-medium transition">Cone</button>
        <button onclick="sim6PlaceShape('sphere')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-purple-600 text-slate-200 text-[11px] font-medium transition">Sphere</button>
    </div>
    <div id="sim6-feedback" class="text-xs text-center mt-2 text-slate-300">Click a shape above to classify its position in the Venn Diagram!</div>
</div>
"""

# Simulator 7: Cube Tower Counting
simulators_part1[7] = """
<div id="sim7-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🏗️</span> Cube Tower Counting & Layer Slicer
            </h3>
            <p class="text-xs text-slate-400">Count visible and hidden cubes layer by layer or by column heights.</p>
        </div>
        <div class="flex gap-1.5">
            <button id="sim7-view-all" onclick="sim7SetView('all')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">Full Tower</button>
            <button id="sim7-view-layers" onclick="sim7SetView('layers')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Layer Slices</button>
        </div>
    </div>

    <!-- Isometric Tower Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim7-svg" viewBox="0 0 380 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered by sim7Render() -->
        </svg>

        <div id="sim7-overlay-info" class="absolute top-2 left-2 bg-slate-900/90 border border-slate-700/80 rounded-lg p-2 text-xs text-slate-300">
            <span class="text-amber-400 font-bold block">3-Tier Stepped Tower</span>
            <span id="sim7-layer-text">Bottom: 9 | Middle: 4 | Top: 1</span>
        </div>
    </div>

    <!-- Layer breakdown & total -->
    <div class="grid grid-cols-4 gap-2 bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-center text-xs">
        <div class="bg-slate-900 p-1.5 rounded-lg border border-slate-800">
            <span class="text-slate-400 block text-[10px]">Tier 3 (Top)</span>
            <span class="text-sky-400 font-bold">1 cube</span>
        </div>
        <div class="bg-slate-900 p-1.5 rounded-lg border border-slate-800">
            <span class="text-slate-400 block text-[10px]">Tier 2 (Mid)</span>
            <span class="text-amber-400 font-bold">4 cubes</span>
        </div>
        <div class="bg-slate-900 p-1.5 rounded-lg border border-slate-800">
            <span class="text-slate-400 block text-[10px]">Tier 1 (Base)</span>
            <span class="text-rose-400 font-bold">9 cubes</span>
        </div>
        <div class="bg-emerald-950/60 p-1.5 rounded-lg border border-emerald-500/40">
            <span class="text-emerald-400 block text-[10px] font-bold">Total Volume</span>
            <span class="text-emerald-300 font-extrabold text-sm">14 Cubes</span>
        </div>
    </div>
</div>
"""

# Simulator 8: Isometric Net Matching
simulators_part1[8] = """
<div id="sim8-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>📐</span> Isometric Net Matching & Fold Puzzles
            </h3>
            <p class="text-xs text-slate-400">Test flat nets of 6 squares to discover which fold into a true cube.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-sky-500/10 text-sky-300 border border-sky-500/20 font-medium">11 Valid Nets</span>
    </div>

    <!-- Net selection grid -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 my-2">
        <button id="sim8-btn-net1" onclick="sim8SelectNet(1)" class="p-2 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition border border-amber-400 flex flex-col items-center">
            <span>Net A: Latin Cross</span>
            <span class="text-[10px] font-normal">Classic T-shape</span>
        </button>
        <button id="sim8-btn-net2" onclick="sim8SelectNet(2)" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:text-white font-medium text-xs transition border border-slate-700 flex flex-col items-center">
            <span>Net B: Stair Step</span>
            <span class="text-[10px] font-normal">2-2-2 Stair</span>
        </button>
        <button id="sim8-btn-net3" onclick="sim8SelectNet(3)" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:text-white font-medium text-xs transition border border-slate-700 flex flex-col items-center">
            <span>Net C: Overlapping</span>
            <span class="text-[10px] font-normal">Same side flaps</span>
        </button>
        <button id="sim8-btn-net4" onclick="sim8SelectNet(4)" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:text-white font-medium text-xs transition border border-slate-700 flex flex-col items-center">
            <span>Net D: Long Strip</span>
            <span class="text-[10px] font-normal">5 in a row</span>
        </button>
    </div>

    <!-- Visual Canvas -->
    <div class="relative flex-1 min-h-[200px] flex items-center justify-center my-2 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim8-svg" viewBox="0 0 380 200" class="w-full h-full max-h-[200px]">
            <!-- Rendered by sim8Render() -->
        </svg>
    </div>

    <div class="flex items-center justify-between bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-xs">
        <div id="sim8-status" class="text-slate-300 font-medium">Net A selected: Folds into a closed cube!</div>
        <button onclick="sim8TestFold()" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition shadow">
            ▶ Test Fold Animation
        </button>
    </div>
</div>
"""

print(f"Part 1: Generated {len(simulators_part1)} simulators markup successfully!")
