# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 10: Symmetrical Designs
Simulators 9 to 16 (HTML & SVG interactive components)
"""

simulators_part2 = {
    9: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🔢 Digit Symmetry Lab</span>
                <span id="sim9_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Digit 8 (Dual)</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Click any single digit 0-9 to test its reflection lines and 180° rotational transformation:</p>
            <div class="grid grid-cols-10 gap-1 mb-2 font-mono font-bold text-center">
                <button onclick="sim9Inspect('0')" class="sim9-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-slate-700">0</button>
                <button onclick="sim9Inspect('1')" class="sim9-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-slate-700">1</button>
                <button onclick="sim9Inspect('2')" class="sim9-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-rose-400 border border-slate-700">2</button>
                <button onclick="sim9Inspect('3')" class="sim9-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">3</button>
                <button onclick="sim9Inspect('4')" class="sim9-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-rose-400 border border-slate-700">4</button>
                <button onclick="sim9Inspect('5')" class="sim9-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-rose-400 border border-slate-700">5</button>
                <button onclick="sim9Inspect('6')" class="sim9-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-purple-300 border border-slate-700">6</button>
                <button onclick="sim9Inspect('7')" class="sim9-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-rose-400 border border-slate-700">7</button>
                <button onclick="sim9Inspect('8')" class="sim9-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-slate-700">8</button>
                <button onclick="sim9Inspect('9')" class="sim9-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-purple-300 border border-slate-700">9</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim9_svg" viewBox="0 0 160 140" class="w-40 h-32">
                    <!-- Dynamic rendering of digit and dashed symmetry lines -->
                </svg>
            </div>
            <div class="p-2.5 rounded bg-slate-800/80 border border-slate-700 font-mono text-[11px] space-y-1">
                <div class="text-slate-300">Digit: <span id="sim9_digit_name" class="text-amber-400 font-bold text-base">8</span></div>
                <div id="sim9_ref_text" class="text-emerald-400">Reflection: 2 lines (V + H)</div>
                <div id="sim9_rot_text" class="text-cyan-300">180° Rotation: Invariant (Order 2)</div>
                <div id="sim9_note" class="text-slate-400 text-[10px]">Looks identical upside down and when folded.</div>
            </div>
        </div>
    </div>
    """,

    10: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🔄 Rotational Number Generator</span>
                <span id="sim10_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Invariant!</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Test multi-digit numbers to observe how they read when turned upside down (180° turn):</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim10Set('88')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">88 (2-digit)</button>
                <button onclick="sim10Set('69')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">69 (2-digit)</button>
                <button onclick="sim10Set('181')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">181 (3-digit)</button>
                <button onclick="sim10Set('808')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">808 (3-digit)</button>
                <button onclick="sim10Set('1001')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">1001 (4-digit)</button>
                <button onclick="sim10Set('8888')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">8888 (4-digit)</button>
                <button onclick="sim10Set('6996')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">6996 (4-digit)</button>
                <button onclick="sim10Set('1234')" class="px-2 py-1 rounded bg-rose-950/40 hover:bg-rose-900 text-rose-300 border border-rose-800/40">1234 (Fails!)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex flex-col items-center justify-center bg-slate-950/80 p-3 rounded-xl border border-slate-800 font-mono">
                <div class="text-[10px] text-slate-400 mb-1">Upright View:</div>
                <div id="sim10_upright" class="text-2xl font-bold text-amber-400 mb-2">808</div>
                <div class="text-[10px] text-slate-400 mb-1">Rotated 180° View:</div>
                <div id="sim10_rotated" class="text-2xl font-bold text-emerald-400 transform rotate-180 transition-all duration-300">808</div>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim10_verdict" class="text-emerald-400 font-bold block mb-1">✅ Rotational Invariant!</span>
                    <span id="sim10_analysis">Reading 808 upside down gives exactly 808.</span>
                </div>
                <button onclick="sim10FlipCard()" class="w-full py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold shadow text-xs">
                    🔄 Spin Card 180°
                </button>
            </div>
        </div>
    </div>
    """,

    11: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">✨ Symmetrical Design Modifier</span>
                <span id="sim11_symmetry_type" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">1/4 Turn (Order 4)</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Choose an element and symmetry mode to clone it systematically across the quadrants:</p>
            <div class="grid grid-cols-2 gap-2 mb-2 font-mono">
                <div>
                    <label class="text-[10px] text-slate-400 block mb-1">Choose Shape Motif:</label>
                    <select id="sim11_motif" onchange="sim11Update()" class="w-full p-1.5 rounded bg-slate-800 border border-slate-700 text-slate-200">
                        <option value="triangle">▲ Pointed Triangle</option>
                        <option value="circle">● Colored Disc</option>
                        <option value="star">★ 5-Point Star</option>
                    </select>
                </div>
                <div>
                    <label class="text-[10px] text-slate-400 block mb-1">Symmetry Goal:</label>
                    <select id="sim11_mode" onchange="sim11Update()" class="w-full p-1.5 rounded bg-slate-800 border border-slate-700 text-slate-200">
                        <option value="order4">Order 4 (1/4 Turn: 4 Quadrants)</option>
                        <option value="order2">Order 2 (1/2 Turn: Opposite Pair)</option>
                    </select>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim11_svg" viewBox="0 0 160 160" class="w-40 h-40">
                    <!-- Quadrant Grid Guides -->
                    <rect x="10" y="10" width="140" height="140" fill="none" stroke="#334155" stroke-width="1"/>
                    <line x1="80" y1="10" x2="80" y2="150" stroke="#475569" stroke-width="1" stroke-dasharray="2,2"/>
                    <line x1="10" y1="80" x2="150" y2="80" stroke="#475569" stroke-width="1" stroke-dasharray="2,2"/>
                    <!-- Cloned Motifs -->
                    <g id="sim11_canvas"></g>
                    <circle cx="80" cy="80" r="4" fill="#f59e0b"/>
                </svg>
            </div>
            <div class="p-2.5 rounded bg-slate-800/80 border border-slate-700 font-mono text-[11px] space-y-1">
                <div class="text-amber-400 font-bold">Mathematical Clone Rule:</div>
                <div id="sim11_rule_desc" class="text-slate-300">4 copies placed at 90° intervals around center.</div>
                <div class="text-emerald-400 font-bold mt-1">Invariance: 90°, 180°, 270°, 360°</div>
            </div>
        </div>
    </div>
    """,

    12: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🎨 4-Quadrant Grid Coloring Studio</span>
                <span id="sim12_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">1/4 Turn Invariant</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Click any grid cell to toggle colors; the 1/4 Turn rule automatically synchronizes all 4 cyclic orbits:</p>
            <div class="flex gap-2 mb-2 font-mono">
                <button onclick="sim12Reset('checker')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">Preset: Pinwheel</button>
                <button onclick="sim12Reset('cross')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">Preset: Greek Cross</button>
                <button onclick="sim12Clear()" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-400 border border-slate-700">Clear All</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-3 rounded-xl border border-slate-800">
                <div id="sim12_grid" class="grid grid-cols-4 gap-1 w-36 h-36">
                    <!-- 16 Interactive grid cells populated dynamically -->
                </div>
            </div>
            <div class="space-y-1.5 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-cyan-300 font-bold block mb-1">Rotational Orbits:</span>
                    <span>Painting 1 cell updates all 4 rotated copies (0°, 90°, 180°, 270°) to guarantee order 4 rotational symmetry.</span>
                </div>
                <button onclick="sim12SpinTest()" class="w-full py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold shadow text-xs">
                    🔄 Spin Grid 90° (Verify Match)
                </button>
            </div>
        </div>
    </div>
    """,

    13: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">⭐ Composite Polygon Star Builder</span>
                <span id="sim13_poly_order" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Order 4 (Star)</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Attach 4 equilateral triangles to the sides of a central square to create an 8-pointed star:</p>
            <div class="flex gap-2 mb-2 font-mono">
                <button onclick="sim13ToggleTriangles()" id="sim13_toggle_btn" class="px-3 py-1 rounded bg-amber-600 text-white font-bold">Detach Triangles</button>
                <button onclick="sim13RotateStar()" class="px-3 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 font-bold">Rotate 90° ▶</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg viewBox="0 0 160 160" class="w-40 h-40">
                    <!-- Central Square and 4 Attachments -->
                    <g id="sim13_group" transform="rotate(0, 80, 80)" class="transition-transform duration-500">
                        <rect x="60" y="60" width="40" height="40" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
                        <!-- Top Triangle -->
                        <polygon id="sim13_t_top" points="60,60 100,60 80,25" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
                        <!-- Right Triangle -->
                        <polygon id="sim13_t_right" points="100,60 100,100 135,80" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
                        <!-- Bottom Triangle -->
                        <polygon id="sim13_t_bottom" points="100,100 60,100 80,135" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
                        <!-- Left Triangle -->
                        <polygon id="sim13_t_left" points="60,100 60,60 25,80" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
                    </g>
                    <!-- Center Point -->
                    <circle cx="80" cy="80" r="3" fill="#ffffff"/>
                </svg>
            </div>
            <div class="p-2.5 rounded bg-slate-800/80 border border-slate-700 font-mono text-[11px] space-y-1">
                <div class="text-amber-400 font-bold">Composite Symmetries:</div>
                <div>• Reflection: 4 lines of symmetry</div>
                <div>• Rotational Order: Order 4 (every 90°)</div>
                <div class="text-slate-400 text-[10px] mt-1">Four identical triangles share the square's 4-fold rotational symmetry.</div>
            </div>
        </div>
    </div>
    """,

    14: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🪵 Rajasthani Wood Block Printing Press</span>
                <span id="sim14_dye_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Indigo Blue</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select a natural dye color, dip the carved teak block, and stamp repetitive textile borders:</p>
            <div class="flex gap-2 mb-2 font-mono">
                <button onclick="sim14SetDye('#38bdf8', 'Indigo Blue')" class="px-2.5 py-1 rounded bg-cyan-700 text-white font-bold">💙 Indigo</button>
                <button onclick="sim14SetDye('#f87171', 'Madder Red')" class="px-2.5 py-1 rounded bg-red-700 text-white font-bold">❤️ Madder</button>
                <button onclick="sim14SetDye('#fbbf24', 'Turmeric Gold')" class="px-2.5 py-1 rounded bg-amber-700 text-white font-bold">💛 Turmeric</button>
                <button onclick="sim14Clear()" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-400 border border-slate-700">Reset Fabric</button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div class="bg-amber-50/10 p-2.5 rounded-lg border border-amber-900/40 min-h-[70px] overflow-x-auto flex items-center gap-3">
                <span class="text-[10px] text-slate-400 font-mono">Fabric:</span>
                <div id="sim14_fabric" class="flex gap-2">
                    <!-- Stamped block impressions appended here -->
                </div>
            </div>
            <div class="flex justify-between items-center">
                <button onclick="sim14Stamp()" class="px-4 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold shadow text-xs">
                    👊 Stamp Next Block (+ Translation)
                </button>
                <span id="sim14_count" class="font-mono text-cyan-300 text-[11px]">Stamped: 0 blocks</span>
            </div>
        </div>
    </div>
    """,

    15: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🏵️ 4-Step Rotational Block Rosette</span>
                <span id="sim15_step_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Step 1 of 4</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Stamp a single 90° corner block four times with consecutive 90° clockwise turns to build a medallion:</p>
            <div class="flex gap-2 mb-2 font-mono">
                <button onclick="sim15StampNext()" class="px-3 py-1.5 rounded bg-indigo-600 hover:bg-indigo-500 text-white font-bold shadow text-xs">
                    🔄 Stamp Next Quarter (90° Turn)
                </button>
                <button onclick="sim15Reset()" class="px-3 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-400 border border-slate-700">
                    Reset Rosette
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim15_svg" viewBox="0 0 160 160" class="w-40 h-40">
                    <circle cx="80" cy="80" r="70" fill="none" stroke="#334155" stroke-width="1" stroke-dasharray="2,2"/>
                    <!-- 4 Quadrant Prints -->
                    <g id="sim15_q1" opacity="0"></g>
                    <g id="sim15_q2" opacity="0"></g>
                    <g id="sim15_q3" opacity="0"></g>
                    <g id="sim15_q4" opacity="0"></g>
                    <circle cx="80" cy="80" r="4" fill="#fbbf24"/>
                </svg>
            </div>
            <div class="p-2.5 rounded bg-slate-800/80 border border-slate-700 font-mono text-[11px] space-y-1">
                <div class="text-amber-400 font-bold">Printing Progress:</div>
                <div id="sim15_desc">Quadrant 1 (Top-Left) stamped at 0°.</div>
                <div id="sim15_symmetry_msg" class="text-emerald-400 font-bold mt-1">Keep stamping to complete order 4 rosette!</div>
            </div>
        </div>
    </div>
    """,

    16: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🥒 Botanical Vegetable Stamping Studio</span>
                <span id="sim16_stamp_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Okra (Order 5)</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select a vegetable stamp, pick poster paint, and stamp nature's organic geometry on canvas:</p>
            <div class="flex flex-wrap gap-1.5 mb-2 font-mono">
                <button onclick="sim16SetVeg('okra')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-slate-700 font-bold">⭐ Okra / Bhindi (Order 5)</button>
                <button onclick="sim16SetVeg('onion')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-purple-300 border border-slate-700 font-bold">🧅 Sliced Onion (Circular)</button>
                <button onclick="sim16SetVeg('potato')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700 font-bold">🥔 Carved Potato (Order 3)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim16_svg" viewBox="0 0 160 160" class="w-40 h-40">
                    <!-- Dynamic rendering of selected vegetable stamp -->
                </svg>
            </div>
            <div class="p-2.5 rounded bg-slate-800/80 border border-slate-700 font-mono text-[11px] space-y-1">
                <div class="text-amber-400 font-bold">Natural Geometry:</div>
                <div id="sim16_desc">Okra cross-section has 5 seed pods forming a 5-pointed star.</div>
                <div id="sim16_angle" class="text-cyan-300">Rotational Angle: 72° (360° ÷ 5)</div>
                <button onclick="sim16RotateStamp()" class="w-full mt-2 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold shadow text-xs">
                    🔄 Spin Stamp 72°
                </button>
            </div>
        </div>
    </div>
    """
}

