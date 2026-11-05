# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 2: Hide and Seek - Simulators 9 to 16
Generates HTML/SVG markup for simulators 9 to 16.
"""

simulators_part2 = {}

# Simulator 9: Grid System Navigation
simulators_part2[9] = """
<div id="sim9-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🔢</span> 3×3 Grid Matrix Navigator
            </h3>
            <p class="text-xs text-slate-400">Rows (1 to 3) meet Columns (1 to 3) at 9 unique intersection cells.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 font-medium">9 Cells</span>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim9-svg" viewBox="0 0 380 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered dynamically by sim9Render() -->
        </svg>

        <div id="sim9-status" class="absolute bottom-2 left-2 right-2 bg-slate-900/90 border border-slate-700 p-2 rounded-lg text-xs text-center text-slate-300">
            Click any cell on the grid to reveal its exact Row and Column address!
        </div>
    </div>
</div>
"""

# Simulator 10: Locating Grid Coordinates
simulators_part2[10] = """
<div id="sim10-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🎯</span> Coordinate Drawing & Placement Game
            </h3>
            <p class="text-xs text-slate-400">Follow coordinate clues to place items into designated grid compartments.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-sky-500/10 text-sky-300 border border-sky-500/20 font-medium">Coordinates</span>
    </div>

    <!-- Clue Selection -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 my-2">
        <button id="sim10-btn-ball" onclick="sim10PlaceItem('ball', 1, 1)" class="px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-amber-500 text-slate-950 transition">⚽ Ball (Row 1, Col 1)</button>
        <button id="sim10-btn-apple" onclick="sim10PlaceItem('apple', 2, 2)" class="px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-slate-800 text-slate-300 hover:text-white transition">🍎 Apple (Center 2,2)</button>
        <button id="sim10-btn-flower" onclick="sim10PlaceItem('flower', 3, 2)" class="px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-slate-800 text-slate-300 hover:text-white transition">🌸 Flower (Row 3, Col 2)</button>
        <button id="sim10-btn-book" onclick="sim10PlaceItem('book', 1, 3)" class="px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-slate-800 text-slate-300 hover:text-white transition">📖 Book (Row 1, Col 3)</button>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[200px] flex items-center justify-center my-2 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim10-svg" viewBox="0 0 380 200" class="w-full h-full max-h-[200px]">
            <!-- Rendered by sim10Render() -->
        </svg>
    </div>

    <div id="sim10-feedback" class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-xs text-center text-slate-300 font-medium">
        Click a clue above to place that item at its exact coordinate cell!
    </div>
</div>
"""

# Simulator 11: Treasure Hunt Grid
simulators_part2[11] = """
<div id="sim11-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🗺️</span> 4×4 Island Treasure Hunt Lab
            </h3>
            <p class="text-xs text-slate-400">Navigate orthogonally (Up, Down, Left, Right). No diagonal leaps allowed!</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/10 text-amber-300 border border-amber-500/20 font-medium">16 Cells</span>
    </div>

    <div class="flex-1 flex flex-col sm:flex-row gap-3 items-center justify-center my-2 bg-slate-950 p-2 rounded-xl border border-slate-800">
        <!-- 4x4 Grid Canvas -->
        <svg id="sim11-svg" viewBox="0 0 240 240" class="w-56 h-56 shrink-0">
            <!-- Rendered by sim11Render() -->
        </svg>

        <!-- Directional D-Pad Controls -->
        <div class="flex flex-col items-center justify-center gap-1.5 bg-slate-900/90 p-3 rounded-xl border border-slate-800 w-full sm:w-auto">
            <span class="text-[11px] text-slate-400 font-medium mb-1">Directional Controls</span>
            <button onclick="sim11Move('up')" class="w-10 h-10 rounded-lg bg-slate-800 hover:bg-amber-500 hover:text-slate-950 text-white font-bold text-base transition border border-slate-700 flex items-center justify-center">▲</button>
            <div class="flex gap-2">
                <button onclick="sim11Move('left')" class="w-10 h-10 rounded-lg bg-slate-800 hover:bg-amber-500 hover:text-slate-950 text-white font-bold text-base transition border border-slate-700 flex items-center justify-center">◀</button>
                <button onclick="sim11Reset()" class="w-10 h-10 rounded-lg bg-rose-900/60 hover:bg-rose-800 text-rose-300 font-bold text-xs transition border border-rose-700/60 flex items-center justify-center">↺</button>
                <button onclick="sim11Move('right')" class="w-10 h-10 rounded-lg bg-slate-800 hover:bg-amber-500 hover:text-slate-950 text-white font-bold text-base transition border border-slate-700 flex items-center justify-center">▶</button>
            </div>
            <button onclick="sim11Move('down')" class="w-10 h-10 rounded-lg bg-slate-800 hover:bg-amber-500 hover:text-slate-950 text-white font-bold text-base transition border border-slate-700 flex items-center justify-center">▼</button>
        </div>
    </div>

    <div id="sim11-info" class="bg-slate-950 p-2 rounded-xl border border-slate-800 text-xs text-center text-slate-300">
        Start at Bottom-Left (Row 4, Col 1). Use directional buttons to reach hidden treasures!
    </div>
</div>
"""

# Simulator 12: Path Step Counting
simulators_part2[12] = """
<div id="sim12-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>📏</span> Manhattan Distance & Step Counter Lab
            </h3>
            <p class="text-xs text-slate-400">Compare Path A (Up first) vs Path B (Right first). Both sum to 5 steps!</p>
        </div>
        <div class="flex gap-1.5">
            <button id="sim12-btn-p1" onclick="sim12SetPath(1)" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition">Path 1 (Up ➔ Right)</button>
            <button id="sim12-btn-p2" onclick="sim12SetPath(2)" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Path 2 (Right ➔ Up)</button>
        </div>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim12-svg" viewBox="0 0 380 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered by sim12Render() -->
        </svg>

        <div class="absolute top-2 right-2 bg-slate-900/90 border border-slate-700 p-2 rounded-lg text-xs text-slate-300 space-y-1">
            <div>Vertical: <span id="sim12-vert" class="text-sky-400 font-bold">3 steps Up</span></div>
            <div>Horizontal: <span id="sim12-horiz" class="text-amber-400 font-bold">2 steps Right</span></div>
            <div class="border-t border-slate-800 pt-1 text-emerald-400 font-extrabold text-sm">Total: 5 steps</div>
        </div>
    </div>

    <div id="sim12-desc" class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-xs text-center text-slate-300 font-medium">
        Order of turns does not alter total distance: 3 + 2 = 2 + 3 = 5 steps!
    </div>
</div>
"""

# Simulator 13: Drone Aerial Views
simulators_part2[13] = """
<div id="sim13-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🚁</span> Drone Altitude & 3D-to-2D View Morphing
            </h3>
            <p class="text-xs text-slate-400">Ascend from Ground Level (0m) to Drone Altitude (100m) to flatten 3D into 2D maps.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-sky-500/10 text-sky-300 border border-sky-500/20 font-medium">Aerial Morph</span>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim13-svg" viewBox="0 0 380 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered by sim13Render() -->
        </svg>

        <div class="absolute top-2 left-2 bg-slate-900/90 border border-slate-700 p-2 rounded-lg text-xs text-slate-300">
            Drone Altitude: <span id="sim13-alt-disp" class="text-amber-400 font-bold text-sm">0 m</span>
        </div>
    </div>

    <!-- Altitude Slider -->
    <div class="space-y-2 bg-slate-950 p-2.5 rounded-xl border border-slate-800">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-300 font-medium">Fly Drone Upward (0m Ground ➔ 100m Overhead Map):</span>
            <span id="sim13-val" class="text-amber-400 font-bold text-sm">0m</span>
        </div>
        <input id="sim13-slider" type="range" min="0" max="100" value="0" oninput="sim13OnAltChange(this.value)" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
    </div>
</div>
"""

# Simulator 14: School Campus Blueprint
simulators_part2[14] = """
<div id="sim14-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🏫</span> School Campus Blueprint Navigator
            </h3>
            <p class="text-xs text-slate-400">Click facilities to inspect relative positions across the 2D site map.</p>
        </div>
        <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 font-medium">Campus Map</span>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim14-svg" viewBox="0 0 400 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered by sim14Render() -->
        </svg>

        <div id="sim14-inspect-pill" class="absolute bottom-2 left-2 right-2 bg-slate-900/90 border border-slate-700 p-2 rounded-lg text-xs text-center text-slate-300">
            Click on any labeled campus building to inspect its location!
        </div>
    </div>
</div>
"""

# Simulator 15: Shortest Route Navigation
simulators_part2[15] = """
<div id="sim15-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🚶</span> Campus Shortest Route Pathfinding
            </h3>
            <p class="text-xs text-slate-400">From Class 4 Classroom to Assembly Stage: Indoor Corridor vs Playground Route.</p>
        </div>
        <div class="flex gap-1.5">
            <button id="sim15-btn-ra" onclick="sim15SetRoute('A')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-emerald-600 text-white transition">Route A (Indoor: 60m)</button>
            <button id="sim15-btn-rb" onclick="sim15SetRoute('B')" class="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition">Route B (Playground: 95m)</button>
        </div>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim15-svg" viewBox="0 0 380 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered by sim15Render() -->
        </svg>
    </div>

    <div id="sim15-comparison" class="grid grid-cols-3 gap-2 bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-center text-xs">
        <div class="bg-slate-900 p-1.5 rounded-lg border border-slate-800">
            <span class="text-slate-400 block text-[10px]">Route A Length</span>
            <span class="text-emerald-400 font-bold">60 meters</span>
        </div>
        <div class="bg-slate-900 p-1.5 rounded-lg border border-slate-800">
            <span class="text-slate-400 block text-[10px]">Route B Length</span>
            <span class="text-rose-400 font-bold">95 meters</span>
        </div>
        <div class="bg-emerald-950/60 p-1.5 rounded-lg border border-emerald-500/40">
            <span class="text-emerald-400 block text-[10px] font-bold">Shortest Route</span>
            <span class="text-emerald-300 font-extrabold">Route A saves 35m!</span>
        </div>
    </div>
</div>
"""

# Simulator 16: Campus Sight Mapping
simulators_part2[16] = """
<div id="sim16-container" class="bg-slate-900 border border-slate-700/80 rounded-2xl p-4 sm:p-5 flex flex-col h-full text-slate-200">
    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
        <div>
            <h3 class="font-bold text-amber-400 text-base sm:text-lg flex items-center gap-2">
                <span>🗺️</span> Personal Campus Sight Map Walkthrough
            </h3>
            <p class="text-xs text-slate-400">Step sequentially from Main Gate to Classroom Desk along the landmark trail.</p>
        </div>
        <button onclick="sim16StepNext()" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-500 hover:bg-amber-400 text-slate-950 transition shadow">
            Next Waypoint ➔
        </button>
    </div>

    <!-- Canvas -->
    <div class="relative flex-1 min-h-[220px] flex items-center justify-center my-3 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden">
        <svg id="sim16-svg" viewBox="0 0 380 220" class="w-full h-full max-h-[220px]">
            <!-- Rendered by sim16Render() -->
        </svg>

        <div id="sim16-waypoint-pill" class="absolute bottom-2 left-2 right-2 bg-slate-900/90 border border-slate-700 p-2 rounded-lg text-xs text-center text-slate-300 font-medium">
            Waypoint 1: Start at the Main Security Entrance Gate.
        </div>
    </div>
</div>
"""

print(f"Part 2: Generated {len(simulators_part2)} simulators markup successfully!")
