# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 7: Simulators 9 to 16
"""

SIMULATORS_PART2 = {
    "sim_slide_9": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-amber-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Origami Kite Folding Stepper</span>
                <span class="text-xs text-slate-400 font-mono" id="sim9_step_tag">Step 1: Square Paper</span>
            </div>
            <div class="flex gap-2 justify-center text-xs">
                <button onclick="setSim9Step(1)" id="sim9_b_s1" class="px-2.5 py-1 bg-amber-600 rounded font-bold">1: Square</button>
                <button onclick="setSim9Step(2)" id="sim9_b_s2" class="px-2.5 py-1 bg-slate-700 rounded font-bold">2: Diagonal Crease</button>
                <button onclick="setSim9Step(3)" id="sim9_b_s3" class="px-2.5 py-1 bg-slate-700 rounded font-bold">3: Left Wing Fold</button>
                <button onclick="setSim9Step(4)" id="sim9_b_s4" class="px-2.5 py-1 bg-slate-700 rounded font-bold">4: Right Wing Fold</button>
            </div>
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[160px]">
                <svg id="sim9_svg" viewBox="0 0 240 180" class="w-full max-h-44"></svg>
                <div id="sim9_desc" class="text-xs font-mono text-amber-300 font-bold mt-2 text-center">
                    Start with a flat square paper with 4 equal sides and 90° right angles.
                </div>
            </div>
        </div>
    """,

    "sim_slide_10": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-cyan-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400">Inscribed Quadrilateral Constructor</span>
                <span class="text-xs text-slate-400 font-mono" id="sim10_inscribed_tag">Inscribed Rectangle</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs bg-slate-800/80 p-3 rounded-xl border border-slate-700">
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <span>Angle Between Diameters: <strong id="sim10_ang_val" class="text-cyan-400">60°</strong></span>
                    </div>
                    <input type="range" id="sim10_ang" min="30" max="90" step="5" value="60" oninput="updateSim10()" class="w-full accent-cyan-400">
                </div>
                <div class="flex items-center justify-center">
                    <button onclick="setSim10Angle(90)" class="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 rounded font-bold text-xs">
                        Snap to 90° (Make Square!)
                    </button>
                </div>
            </div>
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[160px]">
                <svg id="sim10_svg" viewBox="0 0 240 180" class="w-full max-h-44"></svg>
                <div id="sim10_desc" class="text-xs font-mono text-emerald-300 font-bold mt-2 text-center">
                    At 60°: Diagonals equal and bisecting ➔ Rectangle!
                </div>
            </div>
        </div>
    """,

    "sim_slide_11": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-violet-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-violet-400">24-Point String Art Designer</span>
                <span class="text-xs text-slate-400 font-mono" id="sim11_rule_tag">Step Jump: +5</span>
            </div>
            <div class="flex flex-wrap items-center justify-between gap-3 text-xs">
                <div class="flex items-center gap-2">
                    <span>Step Jump (k): <strong id="sim11_k_val" class="text-violet-400">5</strong></span>
                    <input type="range" id="sim11_k" min="2" max="11" value="5" oninput="updateSim11()" class="w-28 accent-violet-400">
                </div>
                <div class="flex gap-1.5">
                    <button onclick="setSim11Preset('star5')" class="px-2 py-1 bg-slate-700 hover:bg-slate-600 rounded text-[11px] font-mono">Star (Step 5)</button>
                    <button onclick="setSim11Preset('star7')" class="px-2 py-1 bg-slate-700 hover:bg-slate-600 rounded text-[11px] font-mono">Star (Step 7)</button>
                    <button onclick="setSim11Preset('cardioid')" class="px-2 py-1 bg-rose-600 hover:bg-rose-500 rounded text-[11px] font-mono">Cardioid (×2)</button>
                </div>
            </div>
            <div class="bg-slate-950 p-2 rounded-xl border border-slate-800 flex flex-col items-center justify-center">
                <svg id="sim11_svg" viewBox="0 0 240 200" class="w-full max-h-48"></svg>
            </div>
        </div>
    """,

    "sim_slide_12": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-indigo-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-400">3D Cube Net Unfolder & Inspector</span>
                <span class="text-xs text-slate-400 font-mono" id="sim12_net_tag">Latin Cross T-Net</span>
            </div>
            <div class="flex flex-wrap gap-2 justify-center text-xs">
                <button onclick="setSim12Net('cross')" id="sim12_b_cross" class="px-2.5 py-1 bg-indigo-600 rounded font-bold">T-Cross Net</button>
                <button onclick="setSim12Net('stair')" id="sim12_b_stair" class="px-2.5 py-1 bg-slate-700 rounded font-bold">Staircase Net</button>
                <button onclick="setSim12Net('znet')" id="sim12_b_znet" class="px-2.5 py-1 bg-slate-700 rounded font-bold">Z-Net</button>
                <button onclick="setSim12Net('illegal')" id="sim12_b_illegal" class="px-2.5 py-1 bg-rose-700 rounded font-bold">6-in-a-Line (Illegal!)</button>
            </div>
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[160px]">
                <svg id="sim12_svg" viewBox="0 0 240 180" class="w-full max-h-44"></svg>
                <div id="sim12_desc" class="text-xs font-mono text-emerald-300 font-bold mt-2 text-center">
                    Valid Net: 6 connected squares with 1 intervening space between opposite faces.
                </div>
            </div>
        </div>
    """,

    "sim_slide_13": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-rose-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400">3×3×3 Painted Cube Dissector</span>
                <span class="text-xs text-slate-400 font-mono">27 Total Small Cubes</span>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs font-mono text-center">
                <button onclick="setSim13Filter(3)" id="sim13_b_3" class="p-2 bg-rose-600 rounded-lg font-bold">3 Painted: 8 Corners</button>
                <button onclick="setSim13Filter(2)" id="sim13_b_2" class="p-2 bg-slate-700 rounded-lg font-bold">2 Painted: 12 Edges</button>
                <button onclick="setSim13Filter(1)" id="sim13_b_1" class="p-2 bg-slate-700 rounded-lg font-bold">1 Painted: 6 Faces</button>
                <button onclick="setSim13Filter(0)" id="sim13_b_0" class="p-2 bg-slate-700 rounded-lg font-bold">0 Painted: 1 Core</button>
            </div>
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[160px]">
                <svg id="sim13_svg" viewBox="0 0 240 170" class="w-full max-h-44"></svg>
                <div id="sim13_desc" class="text-xs font-mono text-rose-300 font-bold mt-2 text-center">
                    8 Corner Cubes: Exposed on 3 outer faces (Top, Front, Side).
                </div>
            </div>
        </div>
    """,

    "sim_slide_14": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-indigo-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-400">Shape Pedestal Deduction Game</span>
                <span class="text-xs text-slate-400 font-mono">5 Pedestals Puzzle</span>
            </div>
            <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-3">
                <div class="grid grid-cols-5 gap-2 text-center text-xs font-mono">
                    <div class="p-2 bg-slate-900 rounded border border-slate-700">
                        <span class="text-slate-400 block text-[10px]">Pos 1</span>
                        <div id="sim14_slot_1" class="text-xl mt-1">⭕</div>
                    </div>
                    <div class="p-2 bg-slate-900 rounded border border-slate-700">
                        <span class="text-slate-400 block text-[10px]">Pos 2</span>
                        <div id="sim14_slot_2" class="text-xl mt-1">🔺</div>
                    </div>
                    <div class="p-2 bg-slate-900 rounded border border-indigo-500/40">
                        <span class="text-indigo-400 block text-[10px]">Pos 3</span>
                        <div id="sim14_slot_3" class="text-xl mt-1">⬡</div>
                    </div>
                    <div class="p-2 bg-slate-900 rounded border border-slate-700">
                        <span class="text-slate-400 block text-[10px]">Pos 4</span>
                        <div id="sim14_slot_4" class="text-xl mt-1">🟦</div>
                    </div>
                    <div class="p-2 bg-slate-900 rounded border border-slate-700">
                        <span class="text-slate-400 block text-[10px]">Pos 5</span>
                        <div id="sim14_slot_5" class="text-xl mt-1">▭</div>
                    </div>
                </div>
                <div class="flex justify-center gap-2">
                    <button onclick="swapSim14(2, 4)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded text-xs">Swap Pos 2 & 4</button>
                    <button onclick="swapSim14(4, 5)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded text-xs">Swap Pos 4 & 5</button>
                    <button onclick="checkSim14()" class="px-3 py-1 bg-emerald-600 hover:bg-emerald-500 rounded text-xs font-bold">Check Solution ✓</button>
                </div>
                <div id="sim14_feedback" class="text-xs text-center font-mono text-emerald-400 font-bold min-h-[20px]">
                    All 4 clues verified! Circle at 1, Hexagon at 3, Square between Triangle and Rectangle.
                </div>
            </div>
        </div>
    """,

    "sim_slide_15": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-indigo-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-400">Platonic Solids Dual Explorer</span>
                <span class="text-xs text-slate-400 font-mono">Euler: V - E + F = 2</span>
            </div>
            <div class="flex gap-2 justify-center text-xs">
                <button onclick="setSim15Solid('icosa')" id="sim15_b_ico" class="px-3 py-1 bg-indigo-600 rounded font-bold">Icosahedron (20 Triangles)</button>
                <button onclick="setSim15Solid('dodeca')" id="sim15_b_dod" class="px-3 py-1 bg-slate-700 rounded font-bold">Dodecahedron (12 Pentagons)</button>
            </div>
            <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[160px]">
                <svg id="sim15_svg" viewBox="0 0 240 160" class="w-full max-h-40"></svg>
                <div id="sim15_stats" class="text-xs font-mono text-amber-300 font-bold mt-2 text-center">
                    Faces: 20 (Equilateral Triangles) | Vertices: 12 | Edges: 30 ➔ 12 - 30 + 20 = 2 ✓
                </div>
            </div>
        </div>
    """,

    "sim_slide_16": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-teal-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-teal-400">Straw & Clay Structural Rigidity Lab</span>
                <span class="text-xs text-slate-400 font-mono" id="sim16_model_tag">Square Frame</span>
            </div>
            <div class="flex flex-wrap gap-2 justify-center text-xs">
                <button onclick="setSim16Model('square')" id="sim16_b_sq" class="px-2.5 py-1 bg-teal-600 rounded font-bold">Square (4 Straws)</button>
                <button onclick="setSim16Model('triangulated')" id="sim16_b_tri" class="px-2.5 py-1 bg-slate-700 rounded font-bold">Braced (5 Straws)</button>
                <button onclick="setSim16Model('tetra')" id="sim16_b_tetra" class="px-2.5 py-1 bg-slate-700 rounded font-bold">Tetrahedron (3D)</button>
                <button onclick="applySim16Force()" id="sim16_b_force" class="px-3 py-1 bg-rose-600 hover:bg-rose-500 rounded font-bold flex items-center gap-1">
                    <span>⚡ Push / Apply Force</span>
                </button>
            </div>
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[160px]">
                <svg id="sim16_svg" viewBox="0 0 240 160" class="w-full max-h-40"></svg>
                <div id="sim16_desc" class="text-xs font-mono text-rose-300 font-bold mt-2 text-center">
                    Unbraced Square: Angles shift into a rhombus under load! (Unstable)
                </div>
            </div>
        </div>
    """
}

