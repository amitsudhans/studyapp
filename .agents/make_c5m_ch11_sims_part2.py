# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 11: Grandmother's Quilt
Simulators 9 to 16 (HTML & SVG interactive components)
"""

simulators_part2 = {
    9: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">📏 Same Area, Different Perimeter Studio</span>
                <span id="sim9_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Fixed Area = 12 cm²</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Reconfigure 12 unit squares to observe how perimeter shrinks as the shape compacts:</p>
            <div class="flex flex-wrap gap-2 mb-2">
                <button onclick="sim9Select('strip')" id="sim9_btn_strip" class="px-2.5 py-1 rounded bg-amber-600 text-white font-semibold">1 × 12 Strip</button>
                <button onclick="sim9Select('mid')" id="sim9_btn_mid" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">2 × 6 Grid</button>
                <button onclick="sim9Select('compact')" id="sim9_btn_compact" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">3 × 4 Block</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800 overflow-hidden">
                <svg id="sim9_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <g id="sim9_tiles"></g>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-400 font-bold block mb-1">Configuration Metrics:</span>
                    <div id="sim9_dim">Dimensions: 1 cm × 12 cm</div>
                    <div class="text-cyan-300 font-bold">Area = 12 cm² (Constant)</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Border Perimeter:</span>
                    <span id="sim9_p" class="text-rose-400 font-bold text-sm">26 cm (Maximum!)</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-slate-400">Rule: Stretched shapes have large perimeters; compact shapes have small perimeters.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    10: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-emerald-400">📐 Same Perimeter, Different Area Studio</span>
                <span id="sim10_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Fixed P = 24 cm</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Adjust Length along fixed 24 cm wire boundary to find the maximum enclosed area:</p>
            <div>
                <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                    <span>Length (L):</span>
                    <span id="sim10_len_val" class="text-emerald-400 font-mono font-bold">6 cm</span>
                </div>
                <input type="range" id="sim10_len" min="1" max="11" step="1" value="6" oninput="sim10Update()" class="w-full accent-emerald-500">
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim10_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <rect id="sim10_rect" x="30" y="30" width="100" height="100" fill="#047857" stroke="#34d399" stroke-width="3" rx="3"/>
                    <text id="sim10_lbl_l" x="80" y="22" text-anchor="middle" font-size="10" fill="#34d399" font-weight="bold">L = 6 cm</text>
                    <text id="sim10_lbl_b" x="20" y="80" text-anchor="middle" font-size="10" fill="#38bdf8" font-weight="bold">B = 6 cm</text>
                    <text id="sim10_lbl_a" x="80" y="85" text-anchor="middle" font-size="12" fill="#ffffff" font-weight="bold">36 cm²</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <div id="sim10_dims">Dimensions: 6 cm × 6 cm</div>
                    <div class="text-cyan-400">Sum (L + B) = 12 cm</div>
                    <div class="text-slate-400">Perimeter = 2 × 12 = 24 cm (Constant)</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Enclosed Area:</span>
                    <span id="sim10_res_a" class="text-emerald-400 font-bold text-sm">36 cm² (Max Area!)</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-300">Optimization: A square maximizes area for any given perimeter!</span>
                </div>
            </div>
        </div>
    </div>
    """,

    11: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-blue-400">🔢 Row-Column Array Multiplier</span>
                <span id="sim11_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30">Array Active</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Set rows and columns to visualize multiplication as a geometric array of squares:</p>
            <div class="grid grid-cols-2 gap-3">
                <div>
                    <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                        <span>Rows (Height):</span>
                        <span id="sim11_row_val" class="text-blue-400 font-mono font-bold">4</span>
                    </div>
                    <input type="range" id="sim11_rows" min="1" max="6" step="1" value="4" oninput="sim11Update()" class="w-full accent-blue-500">
                </div>
                <div>
                    <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                        <span>Columns (Width):</span>
                        <span id="sim11_col_val" class="text-indigo-400 font-mono font-bold">6</span>
                    </div>
                    <input type="range" id="sim11_cols" min="1" max="8" step="1" value="6" oninput="sim11Update()" class="w-full accent-indigo-500">
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim11_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <g id="sim11_grid"></g>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-blue-400 font-bold block mb-1">Array Product:</span>
                    <div id="sim11_calc" class="text-white font-bold text-sm">4 Rows × 6 Columns = 24 cm²</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Total Unit Squares:</span>
                    <span id="sim11_res_tot" class="text-emerald-400 font-bold text-sm">24 Squares</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-slate-400">Multiplication replaces counting: Rows × Columns = Total Area!</span>
                </div>
            </div>
        </div>
    </div>
    """,

    12: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-indigo-400">📐 Rectangle Dimensions & Formula Lab</span>
                <span id="sim12_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">L = 8 cm, B = 5 cm</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Adjust length and breadth to verify both Area and Perimeter formulas:</p>
            <div class="grid grid-cols-2 gap-3">
                <div>
                    <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                        <span>Length (L):</span>
                        <span id="sim12_len_val" class="text-indigo-400 font-mono font-bold">8 cm</span>
                    </div>
                    <input type="range" id="sim12_len" min="2" max="12" step="1" value="8" oninput="sim12Update()" class="w-full accent-indigo-500">
                </div>
                <div>
                    <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                        <span>Breadth (B):</span>
                        <span id="sim12_brd_val" class="text-cyan-400 font-mono font-bold">5 cm</span>
                    </div>
                    <input type="range" id="sim12_brd" min="1" max="8" step="1" value="5" oninput="sim12Update()" class="w-full accent-cyan-500">
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim12_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <rect id="sim12_rect" x="30" y="30" width="130" height="90" fill="#312e81" stroke="#6366f1" stroke-width="3" rx="3"/>
                    <text id="sim12_top_lbl" x="95" y="22" text-anchor="middle" font-size="10" fill="#6366f1" font-weight="bold">L = 8 cm</text>
                    <text id="sim12_side_lbl" x="20" y="80" text-anchor="middle" font-size="10" fill="#38bdf8" font-weight="bold">B = 5 cm</text>
                    <text id="sim12_area_lbl" x="95" y="80" text-anchor="middle" font-size="12" fill="#ffffff" font-weight="bold">40 cm²</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <div class="flex justify-between text-indigo-300 font-bold">
                        <span>Area Formula:</span>
                        <span>L × B</span>
                    </div>
                    <div id="sim12_res_a" class="text-white font-bold text-sm mt-1">Area = 8 × 5 = 40 cm²</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <div class="flex justify-between text-rose-300 font-bold">
                        <span>Perimeter Formula:</span>
                        <span>2 × (L + B)</span>
                    </div>
                    <div id="sim12_res_p" class="text-emerald-400 font-bold text-sm mt-1">P = 2 × (8 + 5) = 26 cm</div>
                </div>
            </div>
        </div>
    </div>
    """,

    13: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-cyan-400">⬛ Square Area & Perimeter Benchmarker</span>
                <span id="sim13_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Side s = 6 cm</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Slide side length s to compute both Area = s² and Perimeter = 4s:</p>
            <div>
                <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                    <span>Side Length (s):</span>
                    <span id="sim13_side_val" class="text-cyan-400 font-mono font-bold">6 cm</span>
                </div>
                <input type="range" id="sim13_side" min="2" max="12" step="1" value="6" oninput="sim13Update()" class="w-full accent-cyan-500">
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim13_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <rect id="sim13_sq" x="45" y="25" width="105" height="105" fill="#0e7490" stroke="#22d3ee" stroke-width="3" rx="3"/>
                    <text id="sim13_top_lbl" x="97" y="18" text-anchor="middle" font-size="10" fill="#22d3ee" font-weight="bold">s = 6 cm</text>
                    <text id="sim13_inner_lbl" x="97" y="82" text-anchor="middle" font-size="12" fill="#ffffff" font-weight="bold">36 cm²</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-400 font-bold block mb-1">Square Area (s × s):</span>
                    <div id="sim13_res_a" class="text-white font-bold text-sm">6 × 6 = 36 cm²</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-teal-400 font-bold block mb-1">Square Perimeter (4 × s):</span>
                    <div id="sim13_res_p" class="text-emerald-400 font-bold text-sm">4 × 6 = 24 cm</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-slate-400">Notice: When side = 4, numerical values equal (P=16, A=16), but units differ!</span>
                </div>
            </div>
        </div>
    </div>
    """,

    14: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-purple-400">🏫 Classroom & Object Dimension Auditor</span>
                <span id="sim14_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Classroom Floor</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select real-world objects to audit their appropriate metric units and measurements:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim14Select('floor')" id="sim14_btn_floor" class="px-2 py-1 rounded bg-purple-600 text-white font-semibold">Classroom Floor</button>
                <button onclick="sim14Select('board')" id="sim14_btn_board" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Blackboard</button>
                <button onclick="sim14Select('book')" id="sim14_btn_book" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Notebook Cover</button>
                <button onclick="sim14Select('ludo')" id="sim14_btn_ludo" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Ludo Board</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim14_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <rect id="sim14_obj" x="30" y="30" width="140" height="100" fill="#581c87" stroke="#c084fc" stroke-width="3" rx="4"/>
                    <text id="sim14_lbl_title" x="100" y="80" text-anchor="middle" font-size="11" fill="#ffffff" font-weight="bold">Classroom Floor</text>
                    <text id="sim14_lbl_dims" x="100" y="98" text-anchor="middle" font-size="9" fill="#e9d5ff">8 m × 6 m</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <div class="text-purple-300 font-bold" id="sim14_unit">Standard Unit: Metres & Square Metres (m²)</div>
                    <div class="text-slate-300 mt-1" id="sim14_p">Perimeter (Skirting): 2 × (8 + 6) = 28 m</div>
                    <div class="text-amber-400 font-bold mt-1" id="sim14_a">Area (Tiling): 8 × 6 = 48 m²</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-slate-400" id="sim14_use">Use: Metres for rooms; Centimetres for desk items.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    15: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">❓ Missing Dimension Solver</span>
                <span id="sim15_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Find Breadth given Area & Length</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Given Area and Length, determine the unknown Breadth using inverse division:</p>
            <div class="grid grid-cols-2 gap-3">
                <div>
                    <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                        <span>Total Area:</span>
                        <span id="sim15_area_val" class="text-amber-400 font-mono font-bold">72 m²</span>
                    </div>
                    <input type="range" id="sim15_area" min="20" max="120" step="4" value="72" oninput="sim15Update()" class="w-full accent-amber-500">
                </div>
                <div>
                    <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                        <span>Known Length (L):</span>
                        <span id="sim15_len_val" class="text-indigo-400 font-mono font-bold">9 m</span>
                    </div>
                    <input type="range" id="sim15_len" min="4" max="15" step="1" value="9" oninput="sim15Update()" class="w-full accent-indigo-500">
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim15_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <rect id="sim15_rect" x="30" y="30" width="130" height="90" fill="#78350f" stroke="#f59e0b" stroke-width="3" rx="3"/>
                    <text id="sim15_top_lbl" x="95" y="22" text-anchor="middle" font-size="10" fill="#818cf8" font-weight="bold">L = 9 m</text>
                    <text id="sim15_side_lbl" x="18" y="80" text-anchor="middle" font-size="10" fill="#f59e0b" font-weight="bold">B = ?</text>
                    <text id="sim15_inner_lbl" x="95" y="80" text-anchor="middle" font-size="12" fill="#ffffff" font-weight="bold">72 m²</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-400 font-bold block mb-1">Inverse Formula:</span>
                    <div class="text-cyan-300">Breadth = Area ÷ Length</div>
                    <div id="sim15_calc" class="text-white font-bold mt-1">B = 72 ÷ 9 = 8.0 m</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Solved Breadth:</span>
                    <span id="sim15_res_b" class="text-emerald-400 font-bold text-sm">8.0 m</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-slate-400">Verification: 9 m × 8 m = 72 m² (Exact match!).</span>
                </div>
            </div>
        </div>
    </div>
    """,

    16: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-yellow-400">🎲 Perimeter Building Dice Game</span>
                <span id="sim16_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-yellow-500/20 text-yellow-300 border border-yellow-500/30">Target: Exact P = 24</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Roll the die, choose placement tactic (Linear or Corner), and race to perimeter 24:</p>
            <div class="flex items-center gap-2 mb-1">
                <button onclick="sim16Roll()" id="sim16_roll_btn" class="px-3 py-1.5 rounded-lg bg-yellow-500 hover:bg-yellow-400 text-slate-950 font-black shadow flex items-center gap-1.5">
                    <span>🎲</span> Roll Die (<span id="sim16_die_val">3</span>)
                </button>
                <div class="flex gap-1.5">
                    <button onclick="sim16SetMode('linear')" id="sim16_btn_lin" class="px-2 py-1 rounded bg-indigo-600 text-white font-semibold">Linear (+2/tile)</button>
                    <button onclick="sim16SetMode('corner')" id="sim16_btn_cor" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Corner (+0/tile)</button>
                    <button onclick="sim16Reset()" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300">Reset</button>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim16_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <g id="sim16_grid"></g>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Current Perimeter:</span>
                    <span id="sim16_p" class="text-cyan-400 font-bold text-sm">P = 8 units</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Total Tiles Placed:</span>
                    <span id="sim16_tiles_cnt" class="text-amber-400 font-bold">3 Tiles (Area = 3)</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim16_msg" class="text-emerald-400 font-bold">Game In Progress: Need 16 more perimeter units!</span>
                </div>
            </div>
        </div>
    </div>
    """
}
