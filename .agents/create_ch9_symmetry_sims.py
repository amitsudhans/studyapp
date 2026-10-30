# -*- coding: utf-8 -*-
"""
Interactive SVG/HTML Simulators for NCERT Class 6 Mathematics Chapter 9: Symmetry
Strict constraint: STRICTLY ZERO raw LaTeX code or math commands (\frac, \text, \circ, etc.).
All math rendered in clean Unicode (°, •, ², ³, ⁿ, ₁, ₂, ×, ÷, +, −, =, ≠, ≤, ≥, √, π, →, 1/2, 3/4).
"""

SIMULATORS = [
    # Sim 1: Nature's Balance Viewer
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🦋</span> Nature's Balance Viewer
            </span>
            <span id="sim1_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Bilateral Symmetry</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim1_svg" viewBox="0 0 200 140" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Butterfly, Taj Mahal, or Cloud -->
            </svg>
            <div id="sim1_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Butterfly: Left wing is the exact mirror reflection of right wing!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between gap-1.5 text-xs">
            <button onclick="setSim1Object('butterfly')" id="sim1_b1" class="flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs">Butterfly</button>
            <button onclick="setSim1Object('taj')" id="sim1_b2" class="flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs">Taj Mahal</button>
            <button onclick="setSim1Object('cloud')" id="sim1_b3" class="flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs">Cloud (Asym)</button>
        </div>
    </div>
    """,

    # Sim 2: Paper Folding Along Axis
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>📄</span> Paper Folding Along Axis
            </span>
            <span id="sim2_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">Fold Progress: 0%</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim2_svg" viewBox="0 0 200 130" class="w-full h-34 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Symmetrical shape with folding animation -->
            </svg>
            <div id="sim2_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Fold along vertical axis: Both halves coincide perfectly!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-1 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-300">Fold Crease Angle:</span>
                <span id="sim2_val" class="font-bold font-mono text-cyan-300">Flat (0°)</span>
            </div>
            <input type="range" id="sim2_slider" min="0" max="180" value="0" oninput="updateSim2()"
                   class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
        </div>
    </div>
    """,

    # Sim 3: Squares vs Rectangles Fold Demonstrator
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>📐</span> Square vs Rectangle Fold Test
            </span>
            <span id="sim3_badge" class="text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Square: 4 Lines</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim3_svg" viewBox="0 0 200 130" class="w-full h-34 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Folding demonstration -->
            </svg>
            <div id="sim3_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Square Diagonal Fold: Both triangles match and edges overlap!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-2 gap-2 text-xs">
            <button onclick="setSim3Shape('square')" id="sim3_btn_sq" class="py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs">Square (4 Lines)</button>
            <button onclick="setSim3Shape('rect')" id="sim3_btn_rect" class="py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs">Rectangle (2 Lines)</button>
        </div>
    </div>
    """,

    # Sim 4: Regular Polygons & Snowflake Explorer
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>❄️</span> Regular Polygons & Snowflakes
            </span>
            <span id="sim4_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">n = 6 Lines</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim4_svg" viewBox="0 0 160 130" class="w-40 h-32 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Regular polygon with n lines of symmetry -->
            </svg>
            <div id="sim4_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Regular Hexagon: 6 sides = exactly 6 lines of symmetry!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-1 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-300">Sides (n):</span>
                <span id="sim4_n_val" class="font-bold font-mono text-amber-400">6 (Hexagon / Snowflake)</span>
            </div>
            <input type="range" id="sim4_slider" min="3" max="8" value="6" oninput="updateSim4()"
                   class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
        </div>
    </div>
    """,

    # Sim 5: Mirror Reflection Workbench
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🪞</span> Mirror Reflection Workbench
            </span>
            <span id="sim5_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Distance d = 4.0 cm</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim5_svg" viewBox="0 0 220 130" class="w-full h-34 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Mirror line, point P, reflected P' -->
            </svg>
            <div id="sim5_readout" class="mt-1 text-xs font-mono text-center text-slate-300">
                Dist(P, Mirror) = 4.0 cm | Dist(P', Mirror) = 4.0 cm (Perpendicular!)
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-1 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-300">Object Distance from Mirror:</span>
                <span id="sim5_d_val" class="font-bold font-mono text-cyan-300">4.0 cm</span>
            </div>
            <input type="range" id="sim5_slider" min="15" max="75" value="40" oninput="updateSim5()"
                   class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
        </div>
    </div>
    """,

    # Sim 6: Interactive Ink Blot Creator
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🎨</span> Ink Blot Symmetry Studio
            </span>
            <span id="sim6_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Click to add ink</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim6_svg" viewBox="0 0 200 130" class="w-full h-34 bg-slate-950 rounded-xl border border-slate-800 cursor-crosshair" onclick="addSim6Ink(event)">
                <!-- Left page ink drops, crease line, reflected ink drops -->
            </svg>
            <div id="sim6_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Click on the left half to drop ink, then click "Fold Paper"!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between gap-2 text-xs">
            <button onclick="foldSim6Ink()" class="flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs">
                Fold & Press
            </button>
            <button onclick="resetSim6Ink()" class="px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold border border-slate-700 text-xs">
                Clear
            </button>
        </div>
    </div>
    """,

    # Sim 7: Paper Folding & Cuts (Kirigami)
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>✂️</span> Kirigami Paper Cutout Studio
            </span>
            <span id="sim7_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">1 Vertical Line</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim7_svg" viewBox="0 0 200 130" class="w-full h-34 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Cutout shape revealed -->
            </svg>
            <div id="sim7_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Single Fold: Profile cut along crease unfolds into symmetrical heart!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between gap-1.5 text-xs">
            <button onclick="setSim7Cut('heart')" class="flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-[11px]">Heart (1 Fold)</button>
            <button onclick="setSim7Cut('tree')" class="flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-[11px]">Tree (1 Fold)</button>
            <button onclick="setSim7Cut('star')" class="flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-[11px]">Star (2 Folds)</button>
        </div>
    </div>
    """,

    # Sim 8: The Punching Game
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🎯</span> The Punching Game Detective
            </span>
            <span id="sim8_badge" class="text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">2 Holes Symmetrical</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim8_svg" viewBox="0 0 160 130" class="w-40 h-32 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Square paper with punched holes and fold axis -->
            </svg>
            <div id="sim8_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Punched in vertical fold → 2 holes equidistant from center crease!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between gap-1.5 text-xs">
            <button onclick="setSim8Fold('vertical')" class="flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-mono text-[11px] border border-amber-500/30">Vertical</button>
            <button onclick="setSim8Fold('horizontal')" class="flex-1 py-1 rounded bg-slate-800 text-slate-400 font-mono text-[11px] border border-slate-700">Horizontal</button>
            <button onclick="setSim8Fold('diagonal')" class="flex-1 py-1 rounded bg-slate-800 text-slate-400 font-mono text-[11px] border border-slate-700">Diagonal</button>
        </div>
    </div>
    """,

    # Sim 9: Rotational Center & Windmill
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🔄</span> Rotational Symmetry Pinwheel
            </span>
            <span id="sim9_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-purple-500/20 text-purple-300 border border-purple-500/30">Rotation: 0°</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim9_svg" viewBox="0 0 160 130" class="w-40 h-32 bg-slate-950 rounded-xl border border-slate-800">
                <!-- 4 blade curved pinwheel rotating -->
            </svg>
            <div id="sim9_desc" class="mt-1 text-xs font-mono text-center text-cyan-300">
                Zero lines of symmetry, but looks identical every 90° turn!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-1 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-300">Spin Angle:</span>
                <span id="sim9_deg" class="font-bold font-mono text-amber-400">0°</span>
            </div>
            <input type="range" id="sim9_slider" min="0" max="360" value="0" oninput="updateSim9()"
                   class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
        </div>
    </div>
    """,

    # Sim 10: Angle of Symmetry Wheel
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🎡</span> Angle of Symmetry Wheel
            </span>
            <span id="sim10_status" class="text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">MATCH! (0°)</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim10_svg" viewBox="0 0 160 130" class="w-40 h-32 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Shape rotating over transparent outline -->
            </svg>
            <div id="sim10_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Smallest Angle of Symmetry = 90° | Multiples: 90°, 180°, 270°, 360°
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-1 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-300">Current Angle:</span>
                <span id="sim10_deg" class="font-bold font-mono text-cyan-300">0°</span>
            </div>
            <input type="range" id="sim10_slider" min="0" max="360" value="0" oninput="updateSim10()"
                   class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
        </div>
    </div>
    """,

    # Sim 11: Radial Arm Windmill Calculator
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>⚙️</span> Radial Windmill Calculator (360° / n)
            </span>
            <span id="sim11_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">360° ÷ 4 = 90°</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim11_svg" viewBox="0 0 160 130" class="w-40 h-32 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Radial arms radiating -->
            </svg>
            <div id="sim11_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                4 Arms → Smallest Angle = 360° / 4 = 90°
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-1 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-300">Number of Radial Arms (n):</span>
                <span id="sim11_n_val" class="font-bold font-mono text-amber-400">4</span>
            </div>
            <input type="range" id="sim11_slider" min="2" max="8" value="4" oninput="updateSim11()"
                   class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
        </div>
    </div>
    """,

    # Sim 12: Order of Rotation Counter
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🔢</span> Order of Rotation Counter
            </span>
            <span id="sim12_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Order = 4</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim12_svg" viewBox="0 0 160 130" class="w-40 h-32 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Square rotating with match counter -->
            </svg>
            <div id="sim12_readout" class="mt-1 text-xs font-mono text-center text-cyan-300">
                Matches during 360° turn: 90°, 180°, 270°, 360° (4 times!)
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between gap-2 text-xs">
            <button onclick="stepSim12()" class="flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs">
                Step 90° Turn
            </button>
            <button onclick="resetSim12()" class="px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold border border-slate-700 text-xs">
                Reset
            </button>
        </div>
    </div>
    """,

    # Sim 13: Symmetries of a Circle
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>⭕</span> Symmetries of a Circle
            </span>
            <span class="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Infinite Symmetries</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim13_svg" viewBox="0 0 160 130" class="w-40 h-32 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Circle with rotating diameter axis -->
            </svg>
            <div id="sim13_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Every diameter is a line of symmetry | Any angle is an angle of symmetry!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-1 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-300">Diameter Angle:</span>
                <span id="sim13_deg" class="font-bold font-mono text-cyan-300">0°</span>
            </div>
            <input type="range" id="sim13_slider" min="0" max="180" value="0" oninput="updateSim13()"
                   class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
        </div>
    </div>
    """,

    # Sim 14: Tile Symmetry Studio
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🔲</span> Tile Symmetry Studio
            </span>
            <span id="sim14_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">2 Symmetry Axes</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <div id="sim14_grid" class="grid grid-cols-4 gap-1 p-2 bg-slate-950 rounded-xl border border-slate-800">
                <!-- 4x4 clickable tile grid -->
            </div>
            <div id="sim14_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Click any cell: Automatically mirrors across vertical & horizontal axes!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between gap-2 text-xs">
            <button onclick="setSim14Mode(1)" id="sim14_b1" class="flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs">1 Axis</button>
            <button onclick="setSim14Mode(2)" id="sim14_b2" class="flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs">2 Axes</button>
            <button onclick="clearSim14()" class="px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold border border-slate-700 text-xs">Clear</button>
        </div>
    </div>
    """,

    # Sim 15: The Symmetry Grid Game
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🎮</span> 6×6 Symmetry Strategy Game
            </span>
            <span id="sim15_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Your Turn (Player 1)</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim15_svg" viewBox="0 0 160 130" class="w-40 h-32 bg-slate-950 rounded-xl border border-slate-800">
                <!-- 6x6 dot grid and played line segments -->
            </svg>
            <div id="sim15_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Player 2 mirrors your move through the center to guarantee a response!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between gap-2 text-xs">
            <button onclick="playRandomSim15Move()" class="flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs">
                Draw Segment
            </button>
            <button onclick="resetSim15()" class="px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold border border-slate-700 text-xs">
                Reset Board
            </button>
        </div>
    </div>
    """,

    # Sim 16: The Symmetry Matrix
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>📊</span> The 4-Way Symmetry Matrix
            </span>
            <span id="sim16_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Both: Square</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim16_svg" viewBox="0 0 200 120" class="w-full h-32 bg-slate-950 rounded-xl border border-slate-800">
                <!-- 2x2 matrix with active highlight -->
            </svg>
            <div id="sim16_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Square: 4 Lines of Symmetry + Rotational Order 4
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-4 gap-1 text-[10px] font-mono">
            <button onclick="setSim16Category('both')" class="py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">1. Both</button>
            <button onclick="setSim16Category('rot')" class="py-1 rounded bg-slate-800 text-slate-400 border border-slate-700">2. Rot Only</button>
            <button onclick="setSim16Category('line')" class="py-1 rounded bg-slate-800 text-slate-400 border border-slate-700">3. Line Only</button>
            <button onclick="setSim16Category('none')" class="py-1 rounded bg-slate-800 text-slate-400 border border-slate-700">4. Neither</button>
        </div>
    </div>
    """
]

def verify_sims():
    forbidden = ["\\text", "\\frac", "\\circ", "\\angle", "\\overleftrightarrow", "\\overline", "\\vec", "\\approx", "\\dots", "\\sqrt"]
    for idx, s in enumerate(SIMULATORS):
        for word in forbidden:
            if word in s:
                raise ValueError(f"Found forbidden LaTeX token in Sim {idx+1}: {word}")
        for ch in s:
            if 0xD800 <= ord(ch) <= 0xDFFF:
                raise ValueError(f"Found surrogate in Sim {idx+1}: {ch}")
    print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in all 16 Simulators!")

if __name__ == "__main__":
    verify_sims()
    with open(".agents/class6_math_symmetry_sims.py", "w", encoding="utf-8") as f:
        with open(".agents/create_ch9_symmetry_sims.py", "r", encoding="utf-8") as src:
            f.write(src.read())
    print("Successfully wrote .agents/class6_math_symmetry_sims.py")

