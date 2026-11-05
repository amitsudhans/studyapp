# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 7: Simulators 1 to 8
"""

SIMULATORS_PART1 = {
    "sim_slide_1": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-indigo-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-400">Paper Weaving Grid Studio</span>
                <span class="text-xs text-slate-400 font-mono" id="sim1_weave_mode">Plain Weave (1 Over, 1 Under)</span>
            </div>
            <div class="flex flex-wrap gap-2 justify-center text-xs">
                <button onclick="setSim1Weave('plain')" id="sim1_b_plain" class="px-3 py-1 bg-indigo-600 rounded font-bold">Plain Weave (1×1)</button>
                <button onclick="setSim1Weave('twill')" id="sim1_b_twill" class="px-3 py-1 bg-slate-700 rounded font-bold">Twill Weave (2×1)</button>
                <button onclick="setSim1Weave('basket')" id="sim1_b_basket" class="px-3 py-1 bg-slate-700 rounded font-bold">Basket Weave (2×2)</button>
            </div>
            <!-- SVG Weaving Mat Display -->
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center">
                <svg id="sim1_svg" viewBox="0 0 320 180" class="w-full max-h-44"></svg>
                <div id="sim1_desc" class="text-xs font-mono text-emerald-300 font-bold mt-2 text-center">
                    Row 1: Over-Under-Over-Under | Row 2: Under-Over-Under-Over (Interlocking Tension)
                </div>
            </div>
        </div>
    """,

    "sim_slide_2": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-emerald-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">360° Vertex Tessellation Tester</span>
                <span class="text-xs text-slate-400 font-mono" id="sim2_angle_dial">Current Angle: 0° / 360°</span>
            </div>
            <div class="flex flex-wrap gap-2 justify-center text-xs">
                <button onclick="setSim2Tile('square')" id="sim2_b_sq" class="px-3 py-1 bg-emerald-600 rounded font-bold">Square (90°)</button>
                <button onclick="setSim2Tile('triangle')" id="sim2_b_tri" class="px-3 py-1 bg-slate-700 rounded font-bold">Triangle (60°)</button>
                <button onclick="setSim2Tile('hexagon')" id="sim2_b_hex" class="px-3 py-1 bg-slate-700 rounded font-bold">Hexagon (120°)</button>
                <button onclick="addSim2Tile()" class="px-3 py-1 bg-amber-600 hover:bg-amber-500 rounded font-bold flex items-center gap-1">
                    <span>+ Add Tile to Vertex</span>
                </button>
            </div>
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center">
                <svg id="sim2_svg" viewBox="0 0 240 180" class="w-full max-h-40"></svg>
                <div id="sim2_result" class="text-xs font-mono text-amber-300 font-bold mt-2">
                    Click '+ Add Tile to Vertex' to fit shapes around the central vertex!
                </div>
            </div>
        </div>
    """,

    "sim_slide_3": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-rose-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Pentagon Gap vs Octagon-Square Tile</span>
                <span class="text-xs text-slate-400 font-mono">Angle Deficit Analyzer</span>
            </div>
            <div class="flex gap-2 justify-center text-xs">
                <button onclick="setSim3Mode('pentagon')" id="sim3_b_pent" class="px-3 py-1 bg-rose-600 rounded font-bold">3 Pentagons (108°)</button>
                <button onclick="setSim3Mode('octsq')" id="sim3_b_oct" class="px-3 py-1 bg-slate-700 rounded font-bold">2 Octagons + 1 Square</button>
            </div>
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[160px]">
                <svg id="sim3_svg" viewBox="0 0 260 170" class="w-full max-h-40"></svg>
                <div id="sim3_text" class="text-xs font-mono text-rose-300 font-bold mt-2 text-center">
                    3 × 108° = 324°. Remaining Gap = 36° (Cannot fit 4th pentagon without overlap!)
                </div>
            </div>
        </div>
    """,

    "sim_slide_4": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-cyan-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400">Rhombus Dissection & Triangle Lab</span>
                <span class="text-xs text-slate-400 font-mono">Angle & Side Symmetry</span>
            </div>
            <div class="flex flex-wrap gap-2 justify-center text-xs">
                <button onclick="setSim4Type('equilateral')" id="sim4_b_eq" class="px-3 py-1 bg-cyan-600 rounded font-bold">Equilateral (60°-60°-60°)</button>
                <button onclick="setSim4Type('isosceles')" id="sim4_b_iso" class="px-3 py-1 bg-slate-700 rounded font-bold">Isosceles (Fold Symmetry)</button>
                <button onclick="setSim4Type('scalene')" id="sim4_b_sca" class="px-3 py-1 bg-slate-700 rounded font-bold">Scalene (All 3 Different)</button>
                <button onclick="toggleSim4Rhombus()" id="sim4_b_rhomb" class="px-3 py-1 bg-amber-600 rounded font-bold">Rhombus 4-Tri Dissection</button>
            </div>
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[160px]">
                <svg id="sim4_svg" viewBox="0 0 260 160" class="w-full max-h-40"></svg>
                <div id="sim4_text" class="text-xs font-mono text-emerald-300 font-bold mt-2 text-center">
                    Equilateral: 3 equal sides, 3 equal angles = 60°, 3 lines of symmetry.
                </div>
            </div>
        </div>
    """,

    "sim_slide_5": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-amber-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Kite Geometry & Aerodynamic Struts</span>
                <span class="text-xs text-slate-400 font-mono" id="sim5_stat">Adjacent Sides Equal | 90° Diagonals</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs bg-slate-800/80 p-3 rounded-xl border border-slate-700">
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <span>Top Wings ($AB = AD$): <strong id="sim5_top_val" class="text-amber-400">6 cm</strong></span>
                    </div>
                    <input type="range" id="sim5_top" min="4" max="10" value="6" oninput="updateSim5()" class="w-full accent-amber-400">
                </div>
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <span>Tail Wings ($CB = CD$): <strong id="sim5_tail_val" class="text-cyan-400">14 cm</strong></span>
                    </div>
                    <input type="range" id="sim5_tail" min="8" max="20" value="14" oninput="updateSim5()" class="w-full accent-cyan-400">
                </div>
            </div>
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center">
                <svg id="sim5_svg" viewBox="0 0 260 170" class="w-full max-h-44"></svg>
                <div id="sim5_desc" class="text-xs font-mono text-amber-300 font-bold mt-1 text-center">
                    Main diagonal bisects cross-diagonal at a 90° perpendicular intersection.
                </div>
            </div>
        </div>
    """,

    "sim_slide_6": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-indigo-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-400">Quadrilateral Morphing Machine</span>
                <span class="text-xs text-slate-400 font-mono" id="sim6_shape_name">Parallelogram</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs bg-slate-800/80 p-3 rounded-xl border border-slate-700">
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <span>Corner Slant Angle: <strong id="sim6_ang_val" class="text-indigo-400">65°</strong></span>
                    </div>
                    <input type="range" id="sim6_ang" min="40" max="90" value="65" oninput="updateSim6()" class="w-full accent-indigo-400">
                </div>
                <div>
                    <div class="flex justify-between items-center mb-1">
                        <span>Side Ratio: <strong id="sim6_rat_val" class="text-emerald-400">1.5 : 1</strong></span>
                    </div>
                    <input type="range" id="sim6_rat" min="10" max="20" value="15" oninput="updateSim6()" class="w-full accent-emerald-400">
                </div>
            </div>
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[140px]">
                <svg id="sim6_svg" viewBox="0 0 260 140" class="w-full max-h-36"></svg>
                <div id="sim6_rule" class="text-xs font-mono text-indigo-300 font-bold mt-2 text-center">
                    Slanted angles + Unequal sides = Parallelogram (Opposite sides equal)
                </div>
            </div>
        </div>
    """,

    "sim_slide_7": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-violet-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-violet-400">7-Piece Tangram Dissection Sandbox</span>
                <span class="text-xs text-slate-400 font-mono" id="sim7_mode_tag">Square Assembly</span>
            </div>
            <div class="flex flex-wrap gap-2 justify-center text-xs">
                <button onclick="setSim7Shape('square')" id="sim7_b_sq" class="px-3 py-1 bg-violet-600 rounded font-bold">7-Tan Whole Square</button>
                <button onclick="setSim7Shape('small_sq')" id="sim7_b_ssq" class="px-3 py-1 bg-slate-700 rounded font-bold">2 Small Tris ➔ Square</button>
                <button onclick="setSim7Shape('med_tri')" id="sim7_b_mtri" class="px-3 py-1 bg-slate-700 rounded font-bold">2 Small Tris ➔ Med Tri</button>
                <button onclick="setSim7Shape('para')" id="sim7_b_para" class="px-3 py-1 bg-slate-700 rounded font-bold">2 Small Tris ➔ Parallelogram</button>
            </div>
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center">
                <svg id="sim7_svg" viewBox="0 0 200 160" class="w-full max-h-40"></svg>
                <div id="sim7_desc" class="text-xs font-mono text-teal-300 font-bold mt-2 text-center">
                    7 Tans combine into 1 Big Square with zero overlaps and zero gaps.
                </div>
            </div>
        </div>
    """,

    "sim_slide_8": """
        <div class="p-4 bg-slate-900/90 rounded-2xl border border-rose-500/30 text-white space-y-4">
            <div class="flex items-center justify-between border-b border-slate-700/60 pb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Which Shape Am I? Mystery Box</span>
                <span class="text-xs text-slate-400 font-mono" id="sim8_riddle_tag">Riddle 1 of 4</span>
            </div>
            <div class="flex gap-2 justify-center text-xs">
                <button onclick="setSim8Riddle(1)" id="sim8_b_r1" class="px-2.5 py-1 bg-rose-600 rounded font-bold">Riddle 1</button>
                <button onclick="setSim8Riddle(2)" id="sim8_b_r2" class="px-2.5 py-1 bg-slate-700 rounded font-bold">Riddle 2</button>
                <button onclick="setSim8Riddle(3)" id="sim8_b_r3" class="px-2.5 py-1 bg-slate-700 rounded font-bold">Riddle 3</button>
                <button onclick="setSim8Riddle(4)" id="sim8_b_r4" class="px-2.5 py-1 bg-slate-700 rounded font-bold">Riddle 4</button>
            </div>
            <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 font-mono text-center space-y-2">
                <div id="sim8_clue_box" class="text-xs text-amber-300 italic min-h-[36px] flex items-center justify-center"></div>
                <div class="flex flex-wrap gap-2 justify-center pt-2 border-t border-slate-800">
                    <button onclick="guessSim8('Square')" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded text-xs font-bold">Square</button>
                    <button onclick="guessSim8('Rectangle')" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded text-xs font-bold">Rectangle</button>
                    <button onclick="guessSim8('Rhombus')" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded text-xs font-bold">Rhombus</button>
                    <button onclick="guessSim8('Kite')" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded text-xs font-bold">Kite</button>
                    <button onclick="guessSim8('Parallelogram')" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 border border-slate-700 rounded text-xs font-bold">Parallelogram</button>
                </div>
                <div id="sim8_feedback" class="text-xs font-bold mt-2 min-h-[20px]"></div>
            </div>
        </div>
    """
}

