# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 2: Hide and Seek - Simulators 1 to 8
Generates HTML/SVG markup for simulators 1 to 8.
"""

simulators_part1 = {}

# Simulator 1: Vantage Point Perspectives
simulators_part1[1] = """
<div id="sim1-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🌳</span> Line-of-Sight & Vantage Point Simulator
            </h3>
            <p class="text-xs text-slate-400">Compare Ground Seeker perspective vs Tree Observer elevated line of sight.</p>
        </div>
        <div class="flex gap-1.5">
            <button id="sim1-view-ground" onclick="sim1SetView('ground')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">Ground Level</button>
            <button id="sim1-view-tree" onclick="sim1SetView('tree')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Tree Perch (Elevated)</button>
        </div>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[240px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim1-svg" viewBox="0 0 420 240" class="w-full h-full max-h-[240px]">
            <!-- Rendered dynamically by sim1Render() -->
        </svg>

        <div id="sim1-info" class="absolute bottom-2 left-2 right-2 bg-slate-900/90 border border-slate-700 p-2 rounded-lg text-center text-xs text-slate-300">
            Ground Level View: The solid brick wall blocks straight line-of-sight!
        </div>
    </div>

    <!-- Toggle Controls -->
    <div class="grid grid-cols-2 gap-2 pt-1">
        <button onclick="sim1SetView('ground')" class="px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-amber-300 font-semibold text-xs border border-slate-700 transition">
            👁️ Seeker at Tree Trunk (Ground Blind Spot)
        </button>
        <button onclick="sim1SetView('tree')" class="px-3 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition shadow">
            🦅 Observer High in Tree (Clear Overhead View)
        </button>
    </div>
</div>
"""

# Simulator 2: Object View Angles
simulators_part1[2] = """
<div id="sim2-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🧱</span> 3D Brick Orthogonal Views Studio
            </h3>
            <p class="text-xs text-slate-400">Compare Top View, Front View, Side View, and 3D Isometric View of a brick.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/10 text-amber-300 border border-amber-500/20 font-medium">3D Projection</span>
    </div>

    <!-- Projection Selector Tabs -->
    <div class="grid grid-cols-4 gap-1.5 my-2">
        <button id="sim2-btn-iso" onclick="sim2SetView('iso')" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">3D Solid</button>
        <button id="sim2-btn-top" onclick="sim2SetView('top')" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Top View</button>
        <button id="sim2-btn-front" onclick="sim2SetView('front')" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Front View</button>
        <button id="sim2-btn-side" onclick="sim2SetView('side')" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Side View</button>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-2 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim2-svg" viewBox="0 0 380 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered by sim2Render() -->
        </svg>

        <div id="sim2-desc-pill" class="absolute bottom-2 left-2 right-2 bg-slate-900/90 border border-slate-700 p-2 rounded-lg text-xs text-center text-slate-300">
            3D Isometric View: Showing Top, Front, and Side faces together in solid space.
        </div>
    </div>
</div>
"""

# Simulator 3: Identifying Common Views
simulators_part1[3] = """
<div id="sim3-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🔍</span> Everyday Objects View Identifier
            </h3>
            <p class="text-xs text-slate-400">Classify the view shown (Top, Front, or Side) for everyday items.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-sky-500/10 text-sky-300 border border-sky-500/20 font-medium">Visual Deduction</span>
    </div>

    <!-- Object Selectors -->
    <div class="grid grid-cols-3 sm:grid-cols-6 gap-1.5 my-2">
        <button id="sim3-btn-bus" onclick="sim3SelectObj('bus')" class="px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-amber-500 text-slate-950 transition">School Bus</button>
        <button id="sim3-btn-tv" onclick="sim3SelectObj('tv')" class="px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Television</button>
        <button id="sim3-btn-sofa" onclick="sim3SelectObj('sofa')" class="px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Sofa</button>
        <button id="sim3-btn-helmet" onclick="sim3SelectObj('helmet')" class="px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Helmet</button>
        <button id="sim3-btn-pencil" onclick="sim3SelectObj('pencil')" class="px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Pencil Top</button>
        <button id="sim3-btn-cutter" onclick="sim3SelectObj('cutter')" class="px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Pizza Cutter</button>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[200px] flex items-center justify-center my-2 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim3-svg" viewBox="0 0 380 200" class="w-full h-full max-h-[200px]">
            <!-- Rendered by sim3Render() -->
        </svg>
    </div>

    <!-- View Classification Buttons -->
    <div class="grid grid-cols-3 gap-2">
        <button onclick="sim3CheckAnswer('top')" class="px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-sky-400 font-bold text-xs border border-slate-700 transition">Top View</button>
        <button onclick="sim3CheckAnswer('front')" class="px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-emerald-400 font-bold text-xs border border-slate-700 transition">Front View</button>
        <button onclick="sim3CheckAnswer('side')" class="px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-amber-400 font-bold text-xs border border-slate-700 transition">Side View</button>
    </div>
    <div id="sim3-feedback" class="text-xs text-center mt-2 text-slate-300 font-medium">Which view of the object is shown above? Click a view button!</div>
</div>
"""

# Simulator 4: Matching Geometric Views
simulators_part1[4] = """
<div id="sim4-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>📐</span> 3D Solids to 2D Projections Matcher
            </h3>
            <p class="text-xs text-slate-400">Match 3D geometric polyhedra to their Top, Front, and Side orthogonal profiles.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 font-medium">Orthogonal Projections</span>
    </div>

    <!-- Solid Selection Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 my-2">
        <button id="sim4-btn-cube" onclick="sim4SelectSolid('cube')" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">Cube</button>
        <button id="sim4-btn-triprism" onclick="sim4SelectSolid('triprism')" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Triangular Prism</button>
        <button id="sim4-btn-sqpyr" onclick="sim4SelectSolid('sqpyr')" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Square Pyramid</button>
        <button id="sim4-btn-cylinder" onclick="sim4SelectSolid('cylinder')" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Cylinder</button>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-2 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim4-svg" viewBox="0 0 420 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered by sim4Render() -->
        </svg>
    </div>

    <div id="sim4-summary" class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-xs text-center text-slate-300">
        Cube: Top = Square, Front = Square, Side = Square (All 3 projections are identical!).
    </div>
</div>
"""

# Simulator 5: Matchbox Block Buildings
simulators_part1[5] = """
<div id="sim5-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🏰</span> Matchbox Architectural Tower Builder
            </h3>
            <p class="text-xs text-slate-400">Stack modular matchbox cuboids into stable multi-tiered stepped towers.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/10 text-amber-300 border border-amber-500/20 font-medium">Modular Cuboids</span>
    </div>

    <!-- 3D Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim5-svg" viewBox="0 0 380 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered by sim5Render() -->
        </svg>

        <div id="sim5-status-pill" class="absolute top-2 left-2 bg-slate-900/90 border border-slate-700 p-2 rounded-lg text-xs text-slate-300">
            Total Blocks: <span id="sim5-block-count" class="text-amber-400 font-bold">4 Matchboxes</span> | Foundation: <span class="text-emerald-400 font-bold">2×2 Base</span>
        </div>
    </div>

    <!-- Construction Controls -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
        <button id="sim5-btn-base" onclick="sim5SetTier(1)" class="px-2.5 py-2 rounded-lg bg-amber-500 text-slate-950 font-bold text-xs transition">1. Base (2×2 = 4)</button>
        <button id="sim5-btn-t2" onclick="sim5SetTier(2)" class="px-2.5 py-2 rounded-lg bg-slate-800 text-slate-300 hover:text-white font-medium text-xs transition border border-slate-700">2. Add Tier 2 (+2)</button>
        <button id="sim5-btn-t3" onclick="sim5SetTier(3)" class="px-2.5 py-2 rounded-lg bg-slate-800 text-slate-300 hover:text-white font-medium text-xs transition border border-slate-700">3. Add Tower (+1)</button>
        <button onclick="sim5Reset()" class="px-2.5 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-rose-300 font-medium text-xs transition border border-slate-700">↺ Reset</button>
    </div>
</div>
"""

# Simulator 6: Multi-Angle Building Views
simulators_part1[6] = """
<div id="sim6-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🔄</span> Multi-Angle Elevation & Plan Studio
            </h3>
            <p class="text-xs text-slate-400">Front elevation, back elevation, side elevation, and top plan view of a block tower.</p>
        </div>
        <div class="flex gap-1">
            <button id="sim6-btn-front" onclick="sim6SetView('front')" class="px-2 py-1 rounded text-xs font-semibold bg-amber-500 text-slate-950 transition">Front</button>
            <button id="sim6-btn-back" onclick="sim6SetView('back')" class="px-2 py-1 rounded text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Back</button>
            <button id="sim6-btn-side" onclick="sim6SetView('side')" class="px-2 py-1 rounded text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Side</button>
            <button id="sim6-btn-top" onclick="sim6SetView('top')" class="px-2 py-1 rounded text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Top Plan</button>
        </div>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim6-svg" viewBox="0 0 380 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered by sim6Render() -->
        </svg>

        <div id="sim6-note" class="absolute bottom-2 left-2 right-2 bg-slate-900/90 border border-slate-700 p-2 rounded-lg text-xs text-center text-slate-300">
            Front View: Left column has 3 blocks, Middle has 2 blocks, Right has 1 block.
        </div>
    </div>
</div>
"""

# Simulator 7: Classroom Spatial Mapping
simulators_part1[7] = """
<div id="sim7-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🐱</span> Cat on Window Sill Classroom Floor Plan
            </h3>
            <p class="text-xs text-slate-400">Translate a 3D classroom into a structured 2D overhead floor plan.</p>
        </div>
        <div class="flex gap-1.5">
            <button id="sim7-btn-3d" onclick="sim7SetMode('3d')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">3D Window View</button>
            <button id="sim7-btn-2d" onclick="sim7SetMode('2d')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">2D Floor Plan</button>
        </div>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim7-svg" viewBox="0 0 400 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered by sim7Render() -->
        </svg>

        <div id="sim7-desc" class="absolute bottom-2 left-2 right-2 bg-slate-900/90 border border-slate-700 p-2 rounded-lg text-xs text-center text-slate-300">
            The cat looks in through the open window sill, observing rows of desks below!
        </div>
    </div>
</div>
"""

# Simulator 8: Desk Positional Terms
simulators_part1[8] = """
<div id="sim8-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🪑</span> Classroom Desk Positional Navigator
            </h3>
            <p class="text-xs text-slate-400">Identify exact desk locations using row and column positional terms.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 font-medium">Positional Terms</span>
    </div>

    <!-- Desk Selection Targets -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 my-2">
        <button id="sim8-btn-1" onclick="sim8SelectDesk(1, 3)" class="px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-amber-500 text-slate-950 transition">3rd Desk, Row 1</button>
        <button id="sim8-btn-2" onclick="sim8SelectDesk(2, 2)" class="px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Middle Desk, Row 2</button>
        <button id="sim8-btn-3" onclick="sim8SelectDesk(3, 1)" class="px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-slate-800 text-slate-300 hover:text-white transition">1st Desk, Row 3</button>
        <button id="sim8-btn-4" onclick="sim8SelectDesk(3, 4)" class="px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Back-Right Corner</button>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[200px] flex items-center justify-center my-2 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim8-svg" viewBox="0 0 380 200" class="w-full h-full max-h-[200px]">
            <!-- Rendered by sim8Render() -->
        </svg>
    </div>

    <div id="sim8-verdict" class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-xs text-center text-slate-300 font-medium">
        Target: Third desk in the first row (Front row nearest the chalkboard, 3rd from left).
    </div>
</div>
"""

print(f"Part 1: Generated {len(simulators_part1)} simulators markup successfully!")
