# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 11: Grandmother's Quilt
Simulators 1 to 8 (HTML & SVG interactive components)
"""

simulators_part1 = {
    1: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🧵 Quilt Lace Border Calculator</span>
                <span id="sim1_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Grandmother's Quilt</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Adjust the length and breadth of the quilt to calculate the total lace ribbon border needed:</p>
            <div class="grid grid-cols-2 gap-3">
                <div>
                    <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                        <span>Length (L):</span>
                        <span id="sim1_len_val" class="text-amber-400 font-mono font-bold">2.0 m</span>
                    </div>
                    <input type="range" id="sim1_len" min="1.0" max="4.0" step="0.5" value="2.0" oninput="sim1Update()" class="w-full accent-amber-500">
                </div>
                <div>
                    <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                        <span>Breadth (B):</span>
                        <span id="sim1_brd_val" class="text-cyan-400 font-mono font-bold">1.5 m</span>
                    </div>
                    <input type="range" id="sim1_brd" min="1.0" max="3.0" step="0.5" value="1.5" oninput="sim1Update()" class="w-full accent-cyan-500">
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim1_svg" viewBox="0 0 220 160" class="w-48 h-36">
                    <!-- Quilt Background & Patchwork -->
                    <rect id="sim1_rect" x="30" y="25" width="160" height="110" rx="4" fill="#312e81" stroke="#f59e0b" stroke-width="4" stroke-dasharray="6,4"/>
                    <!-- Inner Patchwork Pattern -->
                    <g id="sim1_patches"></g>
                    <!-- Dimension Labels -->
                    <text id="sim1_top_lbl" x="110" y="18" text-anchor="middle" font-size="10" fill="#f59e0b" font-weight="bold">L = 2.0 m</text>
                    <text id="sim1_side_lbl" x="22" y="85" text-anchor="middle" font-size="10" fill="#38bdf8" font-weight="bold" transform="rotate(-90 22 85)">B = 1.5 m</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-400 font-bold block mb-1">Formula Calculation:</span>
                    <div id="sim1_calc" class="text-cyan-300">P = 2 × (2.0 + 1.5) = 7.0 m</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Lace Ribbon Needed:</span>
                    <span id="sim1_res_p" class="text-emerald-400 font-bold text-sm">7.0 m</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Cost @ ₹15/m:</span>
                    <span id="sim1_res_cost" class="text-amber-400 font-bold">₹105</span>
                </div>
            </div>
        </div>
    </div>
    """,

    2: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-cyan-400">🔷 Regular Polygon Perimeter Studio</span>
                <span id="sim2_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Equilateral (All Sides Equal)</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select a regular polygon and adjust side length s to compute P = n × s:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim2SetShape('triangle')" id="sim2_btn_tri" class="px-2 py-1 rounded bg-indigo-600 text-white font-semibold">Triangle (n=3)</button>
                <button onclick="sim2SetShape('square')" id="sim2_btn_sq" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Square (n=4)</button>
                <button onclick="sim2SetShape('pentagon')" id="sim2_btn_pen" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Pentagon (n=5)</button>
                <button onclick="sim2SetShape('hexagon')" id="sim2_btn_hex" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Hexagon (n=6)</button>
                <button onclick="sim2SetShape('octagon')" id="sim2_btn_oct" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Octagon (n=8)</button>
            </div>
            <div>
                <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                    <span>Side Length (s):</span>
                    <span id="sim2_side_val" class="text-cyan-400 font-mono font-bold">6 cm</span>
                </div>
                <input type="range" id="sim2_side" min="2" max="15" step="1" value="6" oninput="sim2Update()" class="w-full accent-cyan-500">
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim2_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <polygon id="sim2_poly" points="100,25 160,135 40,135" fill="#0f766e" stroke="#2dd4bf" stroke-width="3"/>
                    <text id="sim2_poly_lbl" x="100" y="152" text-anchor="middle" font-size="10" fill="#2dd4bf" font-weight="bold">s = 6 cm</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-teal-400 font-bold block mb-1">Formula & Substitution:</span>
                    <div id="sim2_calc">P = 3 × 6 = 18 cm</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Total Perimeter:</span>
                    <span id="sim2_res_p" class="text-emerald-400 font-bold text-sm">18 cm</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-slate-400">Rule: For any regular polygon, P = n × s.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    3: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-indigo-400">📐 Fixed Perimeter Rectangle Generator</span>
                <span id="sim3_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">P = 26 cm</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Choose target perimeter, then slide Length to discover valid partner Breadths:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim3SetP(26)" id="sim3_btn_26" class="px-2.5 py-1 rounded bg-indigo-600 text-white font-semibold">Target P = 26 cm (L+B=13)</button>
                <button onclick="sim3SetP(18)" id="sim3_btn_18" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">Target P = 18 cm (L+B=9)</button>
            </div>
            <div>
                <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                    <span>Length (L):</span>
                    <span id="sim3_len_val" class="text-indigo-400 font-mono font-bold">8 cm</span>
                </div>
                <input type="range" id="sim3_len" min="1" max="12" step="1" value="8" oninput="sim3Update()" class="w-full accent-indigo-500">
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim3_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <rect id="sim3_rect" x="30" y="30" width="140" height="90" fill="#4338ca" stroke="#818cf8" stroke-width="3" rx="3"/>
                    <text id="sim3_top_lbl" x="100" y="22" text-anchor="middle" font-size="10" fill="#818cf8" font-weight="bold">L = 8 cm</text>
                    <text id="sim3_side_lbl" x="20" y="80" text-anchor="middle" font-size="10" fill="#38bdf8" font-weight="bold">B = 5 cm</text>
                    <text id="sim3_area_lbl" x="100" y="80" text-anchor="middle" font-size="11" fill="#f8fafc" font-weight="bold">Area = 40 cm²</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-indigo-300 font-bold block mb-1">Dimensions Check:</span>
                    <div id="sim3_calc">L = 8 cm, B = 5 cm (Sum = 13 cm)</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Perimeter:</span>
                    <span id="sim3_res_p" class="text-emerald-400 font-bold">2 × (8 + 5) = 26 cm</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Enclosed Area:</span>
                    <span id="sim3_res_a" class="text-amber-400 font-bold">8 × 5 = 40 cm²</span>
                </div>
            </div>
        </div>
    </div>
    """,

    4: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-emerald-400">🧩 Tessellation & Gaps Lab</span>
                <span id="sim4_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Seamless (0% Gaps)</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Test different geometric shapes to see which ones tile a plane completely:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim4Set('squares')" id="sim4_btn_sq" class="px-2 py-1 rounded bg-emerald-600 text-white font-semibold">Squares</button>
                <button onclick="sim4Set('triangles')" id="sim4_btn_tri" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Triangles</button>
                <button onclick="sim4Set('hexagons')" id="sim4_btn_hex" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Hexagons</button>
                <button onclick="sim4Set('circles')" id="sim4_btn_cir" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Circles (Test!)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim4_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <g id="sim4_grid"></g>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-emerald-400 font-bold block mb-1">Tessellation Result:</span>
                    <span id="sim4_desc">Squares tile edge-to-edge seamlessly with zero empty gaps!</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Uncovered Gaps:</span>
                    <span id="sim4_gaps" class="text-emerald-400 font-bold">0% (Completely Covered)</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-slate-400">Why Squares? Squares fit perfectly without gaps, making them the ideal universal area unit.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    5: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">📚 Non-Standard Desk Covering Studio</span>
                <span id="sim5_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Maths Textbooks</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Cover the classroom desk with non-standard objects and composite tiles:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim5Set('books')" id="sim5_btn_books" class="px-2 py-1 rounded bg-amber-600 text-white font-semibold">Textbooks (6×4)</button>
                <button onclick="sim5Set('boxes')" id="sim5_btn_boxes" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Pencil Boxes (8×5)</button>
                <button onclick="sim5Set('triangles')" id="sim5_btn_tri" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Composite Triangles</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim5_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <rect x="20" y="20" width="160" height="120" fill="#1e293b" stroke="#64748b" stroke-width="3" rx="4"/>
                    <g id="sim5_items"></g>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-400 font-bold block mb-1">Coverage Count:</span>
                    <span id="sim5_desc">24 Mathematics textbooks completely cover the desk.</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Equivalence Rule:</span>
                    <span id="sim5_rule" class="text-cyan-300">2 Half-Triangles = 1 Square</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-slate-400">Limitation: Non-standard units vary by maker, necessitating standard cm² grids!</span>
                </div>
            </div>
        </div>
    </div>
    """,

    6: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-teal-400">📏 1 cm² Grid Overlay Tool</span>
                <span id="sim6_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30">Grid Active</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Estimate area using whole, half, and >1/2 square counting conventions:</p>
            <div class="flex flex-wrap gap-2 mb-2">
                <button onclick="sim6Toggle('whole')" id="sim6_btn_w" class="px-2 py-1 rounded bg-teal-600 text-white font-semibold">Toggle Full (1.0)</button>
                <button onclick="sim6Toggle('half')" id="sim6_btn_h" class="px-2 py-1 rounded bg-cyan-700 text-white font-semibold">Toggle Half (0.5)</button>
                <button onclick="sim6Toggle('more')" id="sim6_btn_m" class="px-2 py-1 rounded bg-indigo-700 text-white font-semibold">Toggle >1/2 (1.0)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim6_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <g id="sim6_grid_lines"></g>
                    <path id="sim6_shape" d="M 50,50 L 150,40 L 160,110 L 80,130 L 40,90 Z" fill="#0d9488" fill-opacity="0.3" stroke="#2dd4bf" stroke-width="2"/>
                    <g id="sim6_markers"></g>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 space-y-1">
                    <div class="flex justify-between"><span>Full Squares (×1):</span><span id="sim6_cnt_w" class="text-teal-400 font-bold">12</span></div>
                    <div class="flex justify-between"><span>Half Squares (×0.5):</span><span id="sim6_cnt_h" class="text-cyan-400 font-bold">6 (➔ 3.0)</span></div>
                    <div class="flex justify-between"><span>> Half Squares (×1):</span><span id="sim6_cnt_m" class="text-indigo-400 font-bold">4</span></div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Total Estimated Area:</span>
                    <span id="sim6_res_a" class="text-emerald-400 font-bold text-sm">19 cm²</span>
                </div>
            </div>
        </div>
    </div>
    """,

    7: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-rose-400">✋ Palm Tracing Simulator</span>
                <span id="sim7_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Adrit's Handprint</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Compare handprints on 1 cm² grid to determine whose palm covers greater area:</p>
            <div class="flex flex-wrap gap-2 mb-2">
                <button onclick="sim7Select('adrit')" id="sim7_btn_adrit" class="px-2.5 py-1 rounded bg-rose-600 text-white font-semibold">Adrit (52 cm²)</button>
                <button onclick="sim7Select('preetha')" id="sim7_btn_preetha" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">Preetha (46 cm²)</button>
                <button onclick="sim7Select('dadi')" id="sim7_btn_dadi" class="px-2.5 py-1 rounded bg-slate-800 text-slate-200">Grandmother (72 cm²)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim7_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <g id="sim7_grid"></g>
                    <path id="sim7_hand" d="" fill="#f43f5e" fill-opacity="0.35" stroke="#fb7185" stroke-width="2"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-rose-400 font-bold block mb-1">Handprint Statistics:</span>
                    <span id="sim7_desc">Adrit's palm covers 52 square centimetres.</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Comparison:</span>
                    <span id="sim7_comp" class="text-amber-300 font-bold">Adrit > Preetha (+6 cm²)</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-slate-400">Irregular outlines are estimated accurately by summing full + half squares.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    8: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-emerald-400">🍃 Garden Leaf Surface Ranker</span>
                <span id="sim8_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Peepal Leaf</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select fallen garden leaves to measure surface area and rank them botanically:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim8Select('coriander')" id="sim8_btn_cor" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Coriander (~3 cm²)</button>
                <button onclick="sim8Select('neem')" id="sim8_btn_neem" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Neem (~8 cm²)</button>
                <button onclick="sim8Select('mango')" id="sim8_btn_mango" class="px-2 py-1 rounded bg-slate-800 text-slate-200">Mango (~32 cm²)</button>
                <button onclick="sim8Select('peepal')" id="sim8_btn_peepal" class="px-2 py-1 rounded bg-emerald-600 text-white font-semibold">Peepal (~70 cm²)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim8_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <g id="sim8_grid"></g>
                    <path id="sim8_leaf" d="" fill="#10b981" fill-opacity="0.4" stroke="#34d399" stroke-width="2"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-emerald-400 font-bold block mb-1">Leaf Surface Area:</span>
                    <span id="sim8_desc">Peepal leaf spans ~70 cm² of surface area.</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 flex justify-between items-center">
                    <span>Botanical Rank:</span>
                    <span id="sim8_rank" class="text-amber-400 font-bold">Largest (Rank 4 of 4)</span>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-slate-400">Photosynthesis: Greater surface area absorbs more sunlight for making food.</span>
                </div>
            </div>
        </div>
    </div>
    """
}
