# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 1: Shapes Around Us - Simulators 9 to 16
Generates HTML/SVG markup for simulators 9 to 16.
"""

simulators_part2 = {}

# Simulator 9: Angles at Intersections
simulators_part2[9] = """
<div id="sim9-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>✂️</span> Angles at Intersections & Straw Joint Lab
            </h3>
            <p class="text-xs text-slate-400">Two intersecting rays form an angle at their vertex. Turn determines angle size.</p>
        </div>
        <div class="flex gap-1.5">
            <button id="sim9-btn-straw" onclick="sim9SetMode('straw')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">Straw Joint</button>
            <button id="sim9-btn-scissors" onclick="sim9SetMode('scissors')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Scissors</button>
            <button id="sim9-btn-roof" onclick="sim9SetMode('roof')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Roof Pitch</button>
        </div>
    </div>

    <!-- Angle Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim9-svg" viewBox="0 0 380 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered dynamically by sim9Render() -->
        </svg>

        <div class="absolute top-2 left-2 bg-slate-900/90 border border-slate-700/80 rounded-lg p-2 text-xs text-slate-300">
            <div>Angle Turn: <span id="sim9-angle-disp" class="text-amber-400 font-bold text-sm">60°</span></div>
            <div>Category: <span id="sim9-type-disp" class="text-emerald-400 font-semibold">Acute (< 90°)</span></div>
        </div>
    </div>

    <!-- Controls -->
    <div class="space-y-2 bg-slate-950 p-2.5 rounded-xl border border-slate-800">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-300 font-medium">Rotate Angle Ray (15° to 165°):</span>
            <span id="sim9-slider-val" class="text-amber-400 font-bold text-sm">60°</span>
        </div>
        <input id="sim9-slider" type="range" min="15" max="165" value="60" oninput="sim9OnAngleChange(this.value)" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
        <div class="flex justify-between items-center pt-1 border-t border-slate-800 text-xs">
            <button onclick="sim9ToggleStrawLength()" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-sky-300 font-medium text-[11px] border border-slate-700 transition">
                📏 Toggle Longer Straws (Angle Stays Identical!)
            </button>
            <span class="text-slate-400 text-[11px]">Length does not affect degree turn!</span>
        </div>
    </div>
</div>
"""

# Simulator 10: Classifying Angle Types
simulators_part2[10] = """
<div id="sim10-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>📐</span> Paper-Fold Right Angle (90°) Tester
            </h3>
            <p class="text-xs text-slate-400">Fold paper twice into a 90° L-tester. Test Acute (<90°), Right (90°), and Obtuse (>90°).</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 font-medium">L-Tester</span>
    </div>

    <!-- Paper Fold Steps -->
    <div class="grid grid-cols-3 gap-2 my-2">
        <button id="sim10-fold0" onclick="sim10SetFold(0)" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">1. Flat Paper</button>
        <button id="sim10-fold1" onclick="sim10SetFold(1)" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">2. Fold Half (180°)</button>
        <button id="sim10-fold2" onclick="sim10SetFold(2)" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">3. Fold Quarter (90° L)</button>
    </div>

    <!-- Testing Canvas -->
    <div class="relative flex-1 min-h-[200px] flex items-center justify-center my-2 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim10-svg" viewBox="0 0 380 200" class="w-full h-full max-h-[200px]">
            <!-- Rendered dynamically by sim10Render() -->
        </svg>

        <div id="sim10-status-pill" class="absolute bottom-2 left-2 right-2 bg-slate-900/95 border border-slate-700/80 rounded-lg p-2 text-center text-xs text-slate-200">
            Fold twice to unlock the 90° right-angle tester!
        </div>
    </div>

    <!-- Angle Target Selectors -->
    <div class="grid grid-cols-3 sm:grid-cols-6 gap-1.5 pt-1">
        <button onclick="sim10TestTarget('acute')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-sky-600 text-slate-200 text-[11px] font-medium transition">Acute (45°)</button>
        <button onclick="sim10TestTarget('right')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-emerald-600 text-slate-200 text-[11px] font-medium transition">Right (90°)</button>
        <button onclick="sim10TestTarget('obtuse')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-rose-600 text-slate-200 text-[11px] font-medium transition">Obtuse (130°)</button>
        <button onclick="sim10TestTarget('letterV')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-amber-600 text-slate-200 text-[11px] font-medium transition">Letter 'V'</button>
        <button onclick="sim10TestTarget('letterL')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-amber-600 text-slate-200 text-[11px] font-medium transition">Letter 'L'</button>
        <button onclick="sim10TestTarget('letterA')" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-amber-600 text-slate-200 text-[11px] font-medium transition">Letter 'A'</button>
    </div>
</div>
"""

# Simulator 11: Triangle Structural Rigidity
simulators_part1_11 = """
<div id="sim11-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🌉</span> Triangle Structural Rigidity Stress Tester
            </h3>
            <p class="text-xs text-slate-400">Push corners to test rigidity. Triangles resist deformation, quadrilaterals collapse.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/10 text-amber-300 border border-amber-500/20 font-medium">Truss Physics</span>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim11-svg" viewBox="0 0 380 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered by sim11Render() -->
        </svg>

        <div id="sim11-alert" class="absolute bottom-2 left-2 right-2 bg-slate-900/90 border border-slate-700 p-2 rounded-lg text-center text-xs text-slate-300">
            Click 'Push Corner' to apply lateral force and test shape stability!
        </div>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
        <button id="sim11-btn-quad" onclick="sim11SetShape('quad')" class="px-3 py-2 rounded-lg bg-amber-500 text-slate-950 font-bold text-xs transition shadow">4-Straw Square</button>
        <button id="sim11-btn-tri" onclick="sim11SetShape('tri')" class="px-3 py-2 rounded-lg bg-slate-800 text-slate-300 hover:text-white font-medium text-xs transition border border-slate-700">3-Straw Triangle</button>
        <button id="sim11-btn-push" onclick="sim11PushForce()" class="px-3 py-2 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs transition shadow">👉 Push Corner</button>
        <button id="sim11-btn-brace" onclick="sim11ToggleBrace()" class="px-3 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition shadow">➕ Add Diagonal Brace</button>
    </div>
</div>
"""
simulators_part2[11] = simulators_part1_11

# Simulator 12: Circle Radius Diameter
simulators_part2[12] = """
<div id="sim12-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🔵</span> Circle Radius & Diameter Crease Lab
            </h3>
            <p class="text-xs text-slate-400">Fold paper disc through center: Diameter = 2 × Radius. All radii are equal.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-sky-500/10 text-sky-300 border border-sky-500/20 font-medium">D = 2 × r</span>
    </div>

    <!-- Circle Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim12-svg" viewBox="0 0 380 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered by sim12Render() -->
        </svg>

        <div class="absolute top-2 right-2 bg-slate-900/90 border border-slate-700 p-2 rounded-lg text-xs text-slate-300 space-y-1">
            <div>Radius (r): <span id="sim12-r-disp" class="text-sky-400 font-bold">5 cm</span></div>
            <div>Diameter (d): <span id="sim12-d-disp" class="text-amber-400 font-bold">10 cm</span></div>
            <div class="text-[10px] text-emerald-400 font-semibold border-t border-slate-800 pt-1">Rule: d = 2 × r</div>
        </div>
    </div>

    <!-- Controls -->
    <div class="space-y-2 bg-slate-950 p-2.5 rounded-xl border border-slate-800">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-300 font-medium">Adjust Radius (2 cm to 9 cm):</span>
            <span id="sim12-slider-val" class="text-sky-400 font-bold text-sm">5 cm</span>
        </div>
        <input id="sim12-slider" type="range" min="2" max="9" value="5" oninput="sim12OnRadiusChange(this.value)" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-sky-500">

        <div class="grid grid-cols-3 gap-2 pt-1 border-t border-slate-800">
            <button onclick="sim12ToggleLine('radius')" class="px-2 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-500 text-white font-medium text-xs transition">Show Radius</button>
            <button onclick="sim12ToggleLine('diameter')" class="px-2 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-medium text-xs transition">Show Diameter</button>
            <button onclick="sim12ToggleLine('crease')" class="px-2 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-medium text-xs transition">Paper Creases</button>
        </div>
    </div>
</div>
"""

# Simulator 13: Compass Circle Art
simulators_part2[13] = """
<div id="sim13-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🎯</span> Geometric Compass Art & Concentric Rings
            </h3>
            <p class="text-xs text-slate-400">Anchor needle at center and rotate pencil 360° to create concentric ring art.</p>
        </div>
        <div class="flex gap-1.5">
            <button onclick="sim13Preset('concentric')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">Concentric Rings</button>
            <button onclick="sim13Preset('rosette')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">6-Petal Rosette</button>
        </div>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim13-svg" viewBox="0 0 380 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered dynamically by sim13Render() -->
        </svg>

        <div id="sim13-compass-tip" class="absolute bottom-2 left-2 bg-slate-900/90 border border-slate-700 p-2 rounded-lg text-xs text-slate-300">
            Center Needle: <span class="text-rose-400 font-bold">Anchored (0,0)</span> | Radius: <span id="sim13-radius-readout" class="text-amber-400 font-bold">50 px</span>
        </div>
    </div>

    <!-- Controls -->
    <div class="space-y-2 bg-slate-950 p-2.5 rounded-xl border border-slate-800">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-300 font-medium">Compass Arm Opening (Radius: 20px to 90px):</span>
            <span id="sim13-val-disp" class="text-amber-400 font-bold text-sm">50 px</span>
        </div>
        <input id="sim13-slider" type="range" min="20" max="90" value="50" oninput="sim13OnRadiusChange(this.value)" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">

        <div class="grid grid-cols-3 gap-2 pt-1 border-t border-slate-800">
            <button onclick="sim13DrawCurrentCircle()" class="px-2 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition shadow">▶ Draw Circle</button>
            <button onclick="sim13AddStepRing()" class="px-2 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-500 text-white font-medium text-xs transition shadow">➕ Add Ring (+15px)</button>
            <button onclick="sim13Clear()" class="px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-xs transition">↺ Clear</button>
        </div>
    </div>
</div>
"""

# Simulator 14: Geometric Dissection Puzzles
simulators_part2[14] = """
<div id="sim14-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🧩</span> Geometric Dissection & 2D Shape Sorter
            </h3>
            <p class="text-xs text-slate-400">Dissect a triangle into 1 square + 2 triangles. Total area is conserved!</p>
        </div>
        <div class="flex gap-1.5">
            <button id="sim14-tab1-btn" onclick="sim14SetTab(1)" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">Triangle Dissection</button>
            <button id="sim14-tab2-btn" onclick="sim14SetTab(2)" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">2D Card Sorter</button>
        </div>
    </div>

    <!-- Tab 1: Triangle Dissection -->
    <div id="sim14-tab1" class="flex-1 flex flex-col items-center justify-center my-3 bg-slate-950 rounded-xl p-3 border border-slate-800">
        <svg id="sim14-svg" viewBox="0 0 380 180" class="w-full max-h-[170px]">
            <!-- Rendered by sim14Render() -->
        </svg>

        <div class="flex gap-2 mt-3">
            <button id="sim14-btn-original" onclick="sim14SetState('original')" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">Original Triangle</button>
            <button id="sim14-btn-dissect" onclick="sim14SetState('dissect')" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Dissect: 1 Square + 2 Triangles</button>
            <button id="sim14-btn-rearrange" onclick="sim14SetState('rearrange')" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Rearrange into Rectangle</button>
        </div>
        <div id="sim14-info" class="text-xs text-center mt-2 text-emerald-400 font-medium">Area is strictly conserved under every rearrangement!</div>
    </div>

    <!-- Tab 2: 2D Shape Card Sorter -->
    <div id="sim14-tab2" class="hidden flex-1 flex flex-col items-center justify-center my-3 bg-slate-950 rounded-xl p-3 border border-slate-800">
        <div class="text-xs text-slate-300 mb-2 text-center">Sort shape cards into polygon families by counting straight sides:</div>
        <div class="grid grid-cols-4 gap-2 w-full max-w-md mb-3 text-center text-xs">
            <div class="bg-slate-900 border border-slate-800 p-2 rounded-lg">
                <span class="text-amber-400 font-bold block mb-1">Triangles (3)</span>
                <span id="sim14-tri-cards" class="text-[11px] text-slate-300">Equilateral, Right</span>
            </div>
            <div class="bg-slate-900 border border-slate-800 p-2 rounded-lg">
                <span class="text-sky-400 font-bold block mb-1">Quadrilaterals (4)</span>
                <span id="sim14-quad-cards" class="text-[11px] text-slate-300">Square, Rectangle</span>
            </div>
            <div class="bg-slate-900 border border-slate-800 p-2 rounded-lg">
                <span class="text-emerald-400 font-bold block mb-1">Pentagons (5)</span>
                <span id="sim14-penta-cards" class="text-[11px] text-slate-300">5-sided regular</span>
            </div>
            <div class="bg-slate-900 border border-slate-800 p-2 rounded-lg">
                <span class="text-purple-400 font-bold block mb-1">Hexagons (6)</span>
                <span id="sim14-hexa-cards" class="text-[11px] text-slate-300">6-sided honeycomb</span>
            </div>
        </div>
        <div class="text-xs text-slate-400">Card classification matches: 3 sides = Triangles, 4 sides = Quads, 5 sides = Pentagons, 6 sides = Hexagons!</div>
    </div>
</div>
"""

# Simulator 15: Matchstick Shape Logic
simulators_part2[15] = """
<div id="sim15-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🔥</span> Matchstick Logic & Spiderweb Geometry Lab
            </h3>
            <p class="text-xs text-slate-400">Move matchsticks to solve geometric puzzles or trace spiderweb intersecting polygons.</p>
        </div>
        <div class="flex gap-1.5">
            <button id="sim15-tab1-btn" onclick="sim15SetTab(1)" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">Matchstick Puzzle</button>
            <button id="sim15-tab2-btn" onclick="sim15SetTab(2)" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Spiderweb Network</button>
        </div>
    </div>

    <!-- Tab 1: Matchstick Puzzle -->
    <div id="sim15-tab1" class="flex-1 flex flex-col items-center justify-center my-3 bg-slate-950 rounded-xl p-3 border border-slate-800">
        <svg id="sim15-svg" viewBox="0 0 380 180" class="w-full max-h-[170px]">
            <!-- Rendered by sim15Render() -->
        </svg>

        <div class="flex gap-2 mt-2">
            <button onclick="sim15RemoveMatches()" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-rose-600 hover:bg-rose-500 text-white transition shadow">
                Remove 2 Matches (Leave 1 Triangle)
            </button>
            <button onclick="sim15ResetMatches()" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">
                ↺ Reset
            </button>
        </div>
        <div id="sim15-match-feedback" class="text-xs text-center mt-2 text-slate-300">6 matchsticks currently form 3 contiguous triangles.</div>
    </div>

    <!-- Tab 2: Spiderweb Network -->
    <div id="sim15-tab2" class="hidden flex-1 flex flex-col items-center justify-center my-3 bg-slate-950 rounded-xl p-3 border border-slate-800">
        <svg id="sim15-web-svg" viewBox="0 0 380 180" class="w-full max-h-[170px]">
            <!-- Rendered by sim15RenderWeb() -->
        </svg>

        <div class="flex gap-2 mt-2">
            <button onclick="sim15HighlightSpokes()" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-sky-600 hover:bg-sky-500 text-white transition">Highlight 8 Radial Spokes</button>
            <button onclick="sim15HighlightPolygons()" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white transition">Count Concentric Loops</button>
        </div>
        <div id="sim15-web-feedback" class="text-xs text-center mt-2 text-slate-300">Radial lines project straight from center; spiral loops form geometric polygons!</div>
    </div>
</div>
"""

# Simulator 16: Polygon Angle Relations
simulators_part2[16] = """
<div id="sim16-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>⭐</span> Polygon Angle-Side Relation: n Sides = n Angles
            </h3>
            <p class="text-xs text-slate-400">Every closed polygon has the exact same count of straight sides and interior angles.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 font-medium">Universal Rule</span>
    </div>

    <!-- Polygon Buttons -->
    <div class="grid grid-cols-5 gap-2 my-2">
        <button id="sim16-btn-3" onclick="sim16Select(3)" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">Triangle (3)</button>
        <button id="sim16-btn-4" onclick="sim16Select(4)" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Quad (4)</button>
        <button id="sim16-btn-5" onclick="sim16Select(5)" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Pentagon (5)</button>
        <button id="sim16-btn-6" onclick="sim16Select(6)" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Hexagon (6)</button>
        <button id="sim16-btn-8" onclick="sim16Select(8)" class="px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Octagon (8)</button>
    </div>

    <!-- Polygon SVG Canvas -->
    <div class="relative flex-1 min-h-[200px] flex items-center justify-center my-2 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim16-svg" viewBox="0 0 380 200" class="w-full h-full max-h-[200px]">
            <!-- Rendered by sim16Render() -->
        </svg>
    </div>

    <!-- Angle-Side Equivalence Display -->
    <div class="grid grid-cols-4 gap-2 bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-center text-xs">
        <div class="bg-slate-900 p-1.5 rounded-lg border border-slate-800">
            <span class="text-slate-400 block text-[10px]">Straight Sides</span>
            <span id="sim16-sides" class="text-sky-400 font-bold text-sm">3 sides</span>
        </div>
        <div class="bg-slate-900 p-1.5 rounded-lg border border-slate-800">
            <span class="text-slate-400 block text-[10px]">Interior Angles</span>
            <span id="sim16-angles" class="text-amber-400 font-bold text-sm">3 angles</span>
        </div>
        <div class="bg-slate-900 p-1.5 rounded-lg border border-slate-800">
            <span class="text-slate-400 block text-[10px]">Classification</span>
            <span id="sim16-group" class="text-rose-400 font-bold text-sm">< 5 Angles</span>
        </div>
        <div class="bg-emerald-950/60 p-1.5 rounded-lg border border-emerald-500/40">
            <span class="text-emerald-400 block text-[10px] font-bold">Rule Invariant</span>
            <span class="text-emerald-300 font-extrabold text-sm">Sides = Angles</span>
        </div>
    </div>
</div>
"""

print(f"Part 2: Generated {len(simulators_part2)} simulators markup successfully!")
