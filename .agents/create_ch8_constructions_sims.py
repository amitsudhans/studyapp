# -*- coding: utf-8 -*-
"""
Interactive SVG/HTML Simulators for NCERT Class 6 Mathematics Chapter 8: Constructions
Strict constraint: STRICTLY ZERO raw LaTeX code or math commands (\frac, \text, \circ, etc.).
All math rendered in clean Unicode (°, •, ², ³, ⁿ, ₁, ₂, ×, ÷, +, −, =, ≠, ≤, ≥, √, π, →, 1/2, 3/4).
"""

SIMULATORS = [
    # Sim 1: Ruler & Compass Precision Lab
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>📐</span> Ruler & Compass Laboratory
            </span>
            <span id="sim1_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">Mode: Straightedge</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-2 relative">
            <svg id="sim1_svg" viewBox="0 0 240 160" class="w-full h-36 drop-shadow-md bg-slate-950 rounded-xl border border-slate-800">
                <!-- Injected via JS -->
            </svg>
            <div id="sim1_readout" class="mt-2 text-xs font-mono font-bold text-center text-cyan-300">
                Segment AB = 6.0 cm
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-2">
            <div class="flex gap-2">
                <button onclick="setSim1Mode('ruler')" id="sim1_btn_ruler" class="flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs">Ruler Segment</button>
                <button onclick="setSim1Mode('compass')" id="sim1_btn_compass" class="flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs">Compass Arc</button>
            </div>
            <div class="flex items-center justify-between text-xs text-slate-300">
                <span id="sim1_slider_label">Length:</span>
                <span id="sim1_val" class="font-bold font-mono text-amber-400">6.0 cm</span>
            </div>
            <input type="range" id="sim1_slider" min="30" max="90" value="60" oninput="updateSim1()"
                   class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
        </div>
    </div>
    """,

    # Sim 2: Circle Radius & Boundary Explorer
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>⭕</span> Circle & Radius Explorer
            </span>
            <span id="sim2_status" class="text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">On Boundary (d = r)</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1 relative">
            <svg id="sim2_svg" viewBox="0 0 200 160" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Center P, circle radius r, test point Q -->
            </svg>
            <div id="sim2_readout" class="mt-1 text-xs font-mono text-center text-slate-300">
                Radius r = 4.0 cm | Distance PQ = 4.0 cm
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-2 gap-3 text-xs">
            <div>
                <label class="text-slate-400 block mb-1">Radius (r): <span id="sim2_r_val" class="text-amber-300 font-bold font-mono">4.0 cm</span></label>
                <input type="range" id="sim2_r" min="20" max="60" value="40" oninput="updateSim2()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
            </div>
            <div>
                <label class="text-slate-400 block mb-1">Point Q Distance: <span id="sim2_d_val" class="text-cyan-300 font-bold font-mono">4.0 cm</span></label>
                <input type="range" id="sim2_d" min="10" max="75" value="40" oninput="updateSim2()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
            </div>
        </div>
    </div>
    """,

    # Sim 3: Wave & Eye Motif Studio
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🌊</span> Wave & Eye Motif Studio
            </span>
            <span id="sim3_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Alternating Wave</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim3_svg" viewBox="0 0 240 140" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Dynamic waves or eye motif -->
            </svg>
            <div id="sim3_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Baseline AB = 8 cm | 4 Alternating Semicircles
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between gap-2 text-xs">
            <button onclick="setSim3Mode('wave')" id="sim3_btn_wave" class="flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs">
                Wavy Wave
            </button>
            <button onclick="setSim3Mode('eye')" id="sim3_btn_eye" class="flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs">
                Symmetrical Eye
            </button>
        </div>
    </div>
    """,

    # Sim 4: Rectangles & Squares Property Inspector
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>📐</span> Shape Classifier
            </span>
            <span id="sim4_badge" class="text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">Rectangle</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1 space-y-2">
            <svg id="sim4_svg" viewBox="0 0 200 130" class="w-48 h-32 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Injected rectangle/square -->
            </svg>
            <div id="sim4_checklist" class="grid grid-cols-2 gap-1.5 w-full text-[11px] font-mono">
                <div class="p-1 rounded bg-slate-800/80 border border-slate-700 text-emerald-300">✓ Opposite equal (R1)</div>
                <div class="p-1 rounded bg-slate-800/80 border border-slate-700 text-emerald-300">✓ All angles 90° (R2)</div>
                <div id="sim4_s1" class="p-1 rounded bg-slate-800/80 border border-slate-700 text-slate-400">✗ All sides equal (S1)</div>
                <div class="p-1 rounded bg-slate-800/80 border border-slate-700 text-emerald-300">✓ 4 Right angles (S2)</div>
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-2 gap-3 text-xs">
            <div>
                <label class="text-slate-400 block mb-1">Length (l): <span id="sim4_l_val" class="text-cyan-300 font-bold font-mono">6 cm</span></label>
                <input type="range" id="sim4_l" min="3" max="8" value="6" oninput="updateSim4()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
            </div>
            <div>
                <label class="text-slate-400 block mb-1">Breadth (b): <span id="sim4_b_val" class="text-amber-400 font-bold font-mono">4 cm</span></label>
                <input type="range" id="sim4_b" min="3" max="8" value="4" oninput="updateSim4()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
            </div>
        </div>
    </div>
    """,

    # Sim 5: Cyclical Vertex Naming Checker
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🔤</span> Cyclical Vertex Naming Checker
            </span>
            <span id="sim5_badge" class="text-[11px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">VALID: ABCD</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1 space-y-2">
            <svg id="sim5_svg" viewBox="0 0 200 140" class="w-48 h-32 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Interactive 4 corners and drawn path -->
            </svg>
            <div id="sim5_readout" class="p-2 rounded bg-slate-800/80 border border-slate-700 text-xs font-mono text-center text-slate-200 w-full">
                Sequence: A → B → C → D (Consecutive perimeter walk!)
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between text-xs">
            <span class="text-slate-400">Click preset:</span>
            <div class="flex gap-1.5">
                <button onclick="testSim5('ABCD')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 font-mono text-[11px] border border-slate-700">ABCD (Valid)</button>
                <button onclick="testSim5('BCDA')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 font-mono text-[11px] border border-slate-700">BCDA (Valid)</button>
                <button onclick="testSim5('ABDC')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 font-mono text-[11px] border border-slate-700">ABDC (Invalid!)</button>
            </div>
        </div>
    </div>
    """,

    # Sim 6: Rotated Shapes on Dot Grid
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🔄</span> Rotated Shape Invariance
            </span>
            <span class="text-[11px] font-mono px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">Always a Square!</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim6_svg" viewBox="0 0 200 150" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Dot grid background and rotating square -->
            </svg>
            <div id="sim6_text" class="mt-1 text-xs font-mono text-center text-cyan-300">
                Rotation: 0° | All 4 sides equal | All 4 corners = 90°
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-1.5 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-300">Rotation Angle:</span>
                <span id="sim6_deg" class="font-bold font-mono text-amber-400">0°</span>
            </div>
            <input type="range" id="sim6_slider" min="0" max="90" value="0" oninput="updateSim6()"
                   class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
        </div>
    </div>
    """,

    # Sim 7: Constructing Squares Stepper
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>📐</span> Square Construction Stepper (6 cm)
            </span>
            <span id="sim7_step_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Step 1 of 4</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1 space-y-2">
            <svg id="sim7_svg" viewBox="0 0 220 150" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Step by step construction elements -->
            </svg>
            <div id="sim7_desc" class="p-2 rounded bg-slate-800/80 border border-slate-700 text-xs font-mono text-center text-slate-200 w-full">
                Step 1: Draw horizontal baseline segment AB = 6 cm.
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between gap-1.5 text-xs">
            <button onclick="setSim7Step(1)" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 font-mono text-[11px] border border-slate-700">1. Base</button>
            <button onclick="setSim7Step(2)" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 font-mono text-[11px] border border-slate-700">2. 90° Rays</button>
            <button onclick="setSim7Step(3)" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 font-mono text-[11px] border border-slate-700">3. Arcs</button>
            <button onclick="setSim7Step(4)" class="flex-1 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 font-mono text-[11px] border border-slate-700">4. Close</button>
        </div>
    </div>
    """,

    # Sim 8: Constructing Rectangles
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>📐</span> Rectangle Construction Lab
            </span>
            <span id="sim8_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">6 cm × 4 cm</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim8_svg" viewBox="0 0 240 140" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Construction of rectangle -->
            </svg>
            <div id="sim8_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Base AB = 6 cm | Perpendiculars AD = BC = 4 cm | CD = 6 cm
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-2 gap-3 text-xs">
            <div>
                <label class="text-slate-400 block mb-1">Length: <span id="sim8_l_val" class="text-cyan-300 font-bold font-mono">6 cm</span></label>
                <input type="range" id="sim8_l" min="4" max="8" value="6" oninput="updateSim8()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
            </div>
            <div>
                <label class="text-slate-400 block mb-1">Breadth: <span id="sim8_b_val" class="text-amber-400 font-bold font-mono">4 cm</span></label>
                <input type="range" id="sim8_b" min="2" max="5" value="4" oninput="updateSim8()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
            </div>
        </div>
    </div>
    """,

    # Sim 9: Point-to-Point Distance
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>📏</span> Dynamic Point Distance (XY)
            </span>
            <span id="sim9_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">XY = 4.0 cm (Min)</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim9_svg" viewBox="0 0 240 140" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800">
                <!-- 7x4 rectangle with sliding X and Y -->
            </svg>
            <div id="sim9_readout" class="mt-1 text-xs font-mono text-center text-slate-300">
                Min: 4.0 cm (Breadth) | Max: 8.06 cm (Diagonal)
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-2 gap-3 text-xs">
            <div>
                <label class="text-slate-400 block mb-1">Position of X (Top):</label>
                <input type="range" id="sim9_x" min="0" max="100" value="0" oninput="updateSim9()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
            </div>
            <div>
                <label class="text-slate-400 block mb-1">Position of Y (Bottom):</label>
                <input type="range" id="sim9_y" min="0" max="100" value="0" oninput="updateSim9()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
            </div>
        </div>
    </div>
    """,

    # Sim 10: Rectangles from Squares
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🔲</span> Rectangles from Squares
            </span>
            <span id="sim10_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">2 Congruent Squares</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim10_svg" viewBox="0 0 240 130" class="w-full h-34 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Partitioned rectangle -->
            </svg>
            <div id="sim10_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                8 cm × 4 cm = Two 4 cm × 4 cm Squares
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between text-xs">
            <span class="text-slate-400">Partition Mode:</span>
            <div class="flex gap-2">
                <button onclick="setSim10Count(2)" class="px-3 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 font-bold border border-slate-700 text-xs">2 Squares (8×4)</button>
                <button onclick="setSim10Count(3)" class="px-3 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 font-bold border border-slate-700 text-xs">3 Squares (12×4)</button>
            </div>
        </div>
    </div>
    """,

    # Sim 11: Nested Shapes & Holes
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🎯</span> Nested Shapes & Circular Holes
            </span>
            <span id="sim11_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Circular Hole</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim11_svg" viewBox="0 0 160 140" class="w-40 h-34 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Square with diagonals and inner cut -->
            </svg>
            <div id="sim11_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Diagonal intersection pinpoints exact center!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between gap-2 text-xs">
            <button onclick="setSim11Mode('hole')" class="flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs">Circular Hole</button>
            <button onclick="setSim11Mode('nested')" class="flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs">Inner Square</button>
        </div>
    </div>
    """,

    # Sim 12: Diagonals of Quadrilaterals
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>✕</span> Rectangular Diagonals Inspector
            </span>
            <span id="sim12_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">AC = BD = 7.21 cm</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim12_svg" viewBox="0 0 220 130" class="w-full h-34 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Rectangle with diagonals AC and BD and intersection M -->
            </svg>
            <div id="sim12_readout" class="mt-1 text-xs font-mono text-center text-slate-300">
                Diagonals bisect at M: AM = MC = BM = MD = 3.61 cm
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-2 gap-3 text-xs">
            <div>
                <label class="text-slate-400 block mb-1">Length: <span id="sim12_l_val" class="text-cyan-300 font-mono font-bold">6 cm</span></label>
                <input type="range" id="sim12_l" min="4" max="8" value="6" oninput="updateSim12()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
            </div>
            <div>
                <label class="text-slate-400 block mb-1">Breadth: <span id="sim12_b_val" class="text-amber-400 font-mono font-bold">4 cm</span></label>
                <input type="range" id="sim12_b" min="2" max="6" value="4" oninput="updateSim12()"
                       class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
            </div>
        </div>
    </div>
    """,

    # Sim 13: Diagonal Angle Splits
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>📐</span> Diagonal Angle Split Comparator
            </span>
            <span id="sim13_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Unequal Split</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim13_svg" viewBox="0 0 200 130" class="w-full h-34 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Angle arcs at corner A -->
            </svg>
            <div id="sim13_text" class="mt-1 text-xs font-mono text-center text-slate-300">
                Rectangle: 56.3° and 33.7° (Sum = 90°, not bisected!)
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex items-center justify-between gap-2 text-xs">
            <button onclick="setSim13Mode('rectangle')" id="sim13_btn_rect" class="flex-1 py-1 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30 text-xs">Rectangle (Unequal)</button>
            <button onclick="setSim13Mode('square')" id="sim13_btn_sq" class="flex-1 py-1 rounded bg-slate-800 text-slate-400 font-bold border border-slate-700 text-xs">Square (Exact 45°/45°)</button>
        </div>
    </div>
    """,

    # Sim 14: Constructing from Diagonals
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🎯</span> Side & Diagonal Arc Intersection
            </span>
            <span id="sim14_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Vertex C Found!</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim14_svg" viewBox="0 0 240 140" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Base AB, ray BX, arc from A, intersection C -->
            </svg>
            <div id="sim14_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Base AB = 5 cm | Diagonal AC = 7 cm | Breadth BC = 4.9 cm
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-1 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-300">Diagonal Length (AC):</span>
                <span id="sim14_diag_val" class="font-bold font-mono text-amber-400">7.0 cm</span>
            </div>
            <input type="range" id="sim14_diag" min="55" max="85" value="70" oninput="updateSim14()"
                   class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
        </div>
    </div>
    """,

    # Sim 15: Equidistant Points (Dual Arc Intersection)
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>📍</span> Equidistant Dual Arc Finder
            </span>
            <span id="sim15_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Point A Located (AB = AC)</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim15_svg" viewBox="0 0 240 140" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800">
                <!-- Points B, C and intersecting arcs to point A -->
            </svg>
            <div id="sim15_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                BC = 6 cm | Arc Radii = 5.0 cm → Isosceles Triangle ABC!
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 space-y-1 text-xs">
            <div class="flex items-center justify-between">
                <span class="text-slate-300">Compass Radius (r):</span>
                <span id="sim15_r_val" class="font-bold font-mono text-amber-400">5.0 cm</span>
            </div>
            <input type="range" id="sim15_r" min="25" max="65" value="50" oninput="updateSim15()"
                   class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
        </div>
    </div>
    """,

    # Sim 16: The Composite House Blueprint Builder
    """
    <div class="h-full flex flex-col justify-between p-3 bg-slate-900/90 border border-slate-800 rounded-xl">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
            <span class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                <span>🏠</span> Composite Blueprint Builder
            </span>
            <span id="sim16_badge" class="text-[11px] font-mono px-2 py-0.5 rounded bg-purple-500/20 text-purple-300 border border-purple-500/30">Complete House</span>
        </div>

        <div class="flex-1 flex flex-col items-center justify-center py-1">
            <svg id="sim16_svg" viewBox="0 0 200 150" class="w-48 h-36 bg-slate-950 rounded-xl border border-slate-800">
                <!-- House layers: square body, door, curved eave, triangular roof -->
            </svg>
            <div id="sim16_desc" class="mt-1 text-xs font-mono text-center text-slate-300">
                Square Foundation + Door + Eave + Triangular Pitch Roof
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 grid grid-cols-4 gap-1 text-[10px] font-mono">
            <button onclick="toggleSim16('walls')" id="sim16_b1" class="py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">1. Body</button>
            <button onclick="toggleSim16('door')" id="sim16_b2" class="py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">2. Door</button>
            <button onclick="toggleSim16('eave')" id="sim16_b3" class="py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">3. Eave</button>
            <button onclick="toggleSim16('roof')" id="sim16_b4" class="py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">4. Roof</button>
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
    with open(".agents/class6_math_constructions_sims.py", "w", encoding="utf-8") as f:
        with open(".agents/create_ch8_constructions_sims.py", "r", encoding="utf-8") as src:
            f.write(src.read())
    print("Successfully wrote .agents/class6_math_constructions_sims.py")

