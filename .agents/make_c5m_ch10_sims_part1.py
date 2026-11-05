# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 10: Symmetrical Designs
Simulators 1 to 8 (HTML & SVG interactive components)
"""

simulators_part1 = {
    1: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🪞 Interactive Mirror Reflection Studio</span>
                <span id="sim1_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Vertical Axis</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select a symmetrical motif to observe how a central mirror line reflects the drawn half into a balanced whole:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim1Select('butterfly')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">🦋 Butterfly</button>
                <button onclick="sim1Select('heart')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">💖 Festive Heart</button>
                <button onclick="sim1Select('leaf')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">🍃 Peepal Leaf</button>
                <button onclick="sim1Select('star')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">⭐ 4-Point Star</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim1_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <!-- Central Mirror Line -->
                    <line x1="100" y1="10" x2="100" y2="150" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
                    <!-- Left Drawn Half -->
                    <g id="sim1_left_shape"></g>
                    <!-- Right Reflected Half -->
                    <g id="sim1_right_shape"></g>
                    <!-- Axis Label -->
                    <text x="100" y="158" text-anchor="middle" font-size="9" fill="#f59e0b" font-weight="bold">Mirror Crease</text>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-400 font-bold block mb-1">Mirror Properties:</span>
                    <span id="sim1_desc">The left wing reflects across the vertical fold into an identical right wing.</span>
                </div>
                <div class="flex gap-2">
                    <button onclick="sim1ToggleFold()" id="sim1_fold_btn" class="w-full py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold shadow text-xs">
                        📖 Fold Paper in Half
                    </button>
                </div>
            </div>
        </div>
    </div>
    """,

    2: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">✂️ Letter Cutting Simulator: Letter A vs Letter H</span>
                <span id="sim2_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">1 Fold (A)</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Choose a letter to see how folding in half (for A) or quarters (for H) cuts out the complete alphabet:</p>
            <div class="flex gap-2 mb-2">
                <button id="sim2_btn_a" onclick="sim2Choose('A')" class="px-3 py-1 rounded bg-amber-600 text-white font-bold">Letter A (1 Vertical Fold)</button>
                <button id="sim2_btn_h" onclick="sim2Choose('H')" class="px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold">Letter H (2 Perpendicular Folds)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim2_svg" viewBox="0 0 200 160" class="w-48 h-36">
                    <!-- Dynamic rendering of folded layer and cutouts -->
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim2_steps_title" class="text-amber-400 font-bold block mb-1">Cutting Strategy:</span>
                    <span id="sim2_steps_desc">Fold paper once vertically. Cut outer slant and inner triangle notch. Unfold to reveal Letter A!</span>
                </div>
                <button onclick="sim2Animate()" class="w-full py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold shadow text-xs">
                    ✨ Animate Cut & Unfold
                </button>
            </div>
        </div>
    </div>
    """,

    3: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🔤 Alphabet Symmetry Inspector</span>
                <span id="sim3_cat" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Vertical Only</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Click any capital letter to inspect its vertical, horizontal, or dual lines of symmetry:</p>
            <div class="grid grid-cols-8 gap-1 mb-2 font-mono font-bold text-center">
                <button onclick="sim3Inspect('A')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">A</button>
                <button onclick="sim3Inspect('B')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">B</button>
                <button onclick="sim3Inspect('C')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">C</button>
                <button onclick="sim3Inspect('D')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">D</button>
                <button onclick="sim3Inspect('E')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">E</button>
                <button onclick="sim3Inspect('H')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-slate-700">H</button>
                <button onclick="sim3Inspect('I')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-slate-700">I</button>
                <button onclick="sim3Inspect('M')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">M</button>
                <button onclick="sim3Inspect('N')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-400 border border-slate-700">N</button>
                <button onclick="sim3Inspect('O')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-slate-700">O</button>
                <button onclick="sim3Inspect('S')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-400 border border-slate-700">S</button>
                <button onclick="sim3Inspect('T')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">T</button>
                <button onclick="sim3Inspect('V')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">V</button>
                <button onclick="sim3Inspect('X')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-slate-700">X</button>
                <button onclick="sim3Inspect('Y')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">Y</button>
                <button onclick="sim3Inspect('Z')" class="sim3-btn p-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-400 border border-slate-700">Z</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim3_svg" viewBox="0 0 160 140" class="w-40 h-32">
                    <!-- Dynamic rendering of letter and dashed symmetry lines -->
                </svg>
            </div>
            <div class="p-2.5 rounded bg-slate-800/80 border border-slate-700 font-mono text-[11px] space-y-1">
                <div class="text-slate-300">Selected: <span id="sim3_letter" class="text-amber-400 font-bold text-sm">Letter A</span></div>
                <div id="sim3_lines" class="text-cyan-300">Lines of Symmetry: 1 (Vertical)</div>
                <div id="sim3_note" class="text-slate-400 text-[10px]">Folding left onto right creates exact overlap along the vertical axis.</div>
            </div>
        </div>
    </div>
    """,

    4: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🪔 Festive Diya Cutout Workshop</span>
                <span id="sim4_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Single Diya</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Fold paper along the vertical crease, sketch half of the clay pot and flame, and unfold into balanced art:</p>
            <div class="flex gap-2 mb-2">
                <button onclick="sim4SetMode('single')" id="sim4_single_btn" class="px-3 py-1 rounded bg-amber-600 text-white font-bold">Single Earthen Diya</button>
                <button onclick="sim4SetMode('garland')" id="sim4_garland_btn" class="px-3 py-1 rounded bg-slate-800 text-slate-300 font-bold">Accordion Garland Chain</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim4_svg" viewBox="0 0 200 140" class="w-48 h-32">
                    <!-- Dynamic rendering of folded diya or garland -->
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span class="text-amber-400 font-bold block mb-1">Craftsperson's Rule:</span>
                    <span id="sim4_desc">The base and flame tip touch the folded edge so the cutout unfolds as one united piece.</span>
                </div>
                <button onclick="sim4ToggleFold()" class="w-full py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold shadow text-xs">
                    🔄 Toggle Fold / Unfold
                </button>
            </div>
        </div>
    </div>
    """,

    5: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🌬️ Paper Firki Construction Studio</span>
                <span id="sim5_stage_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Step 1: Crease</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Step through the 4-phase craft process of turning a square sheet into a spinning paper windmill:</p>
            <div class="flex gap-1.5 mb-2">
                <button onclick="sim5Step(1)" class="sim5-step-btn px-2 py-1 rounded bg-amber-600 text-white font-bold">1. Crease</button>
                <button onclick="sim5Step(2)" class="sim5-step-btn px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold">2. Slit</button>
                <button onclick="sim5Step(3)" class="sim5-step-btn px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold">3. Bend</button>
                <button onclick="sim5Step(4)" class="sim5-step-btn px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold">4. Spin!</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim5_svg" viewBox="0 0 160 160" class="w-40 h-40">
                    <!-- Dynamic rendering of square sheet folding to completed spinning firki -->
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <span id="sim5_instruction_title" class="text-amber-400 font-bold block mb-1">Step 1: Diagonal Creases</span>
                    <span id="sim5_instruction_desc">Fold the square diagonally both ways to locate the exact center intersection.</span>
                </div>
                <div id="sim5_spin_control" class="hidden">
                    <label class="text-[10px] text-slate-400 block mb-1">Wind Speed:</label>
                    <input id="sim5_speed" type="range" min="0" max="100" value="50" oninput="sim5UpdateSpeed()" class="w-full accent-cyan-400">
                </div>
            </div>
        </div>
    </div>
    """,

    6: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🔴 4-Quadrant Turn Tracker</span>
                <span id="sim6_angle_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">0° (Start)</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Track the red dot on the top blade as the firki turns through fractional circle angles:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim6RotateTo(0)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">0° (12 o'clock)</button>
                <button onclick="sim6RotateTo(90)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">1/4 Turn (90°)</button>
                <button onclick="sim6RotateTo(180)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">1/2 Turn (180°)</button>
                <button onclick="sim6RotateTo(270)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">3/4 Turn (270°)</button>
                <button onclick="sim6RotateTo(360)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">Full Turn (360°)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg viewBox="0 0 160 160" class="w-40 h-40">
                    <circle cx="80" cy="80" r="70" fill="none" stroke="#334155" stroke-width="1" stroke-dasharray="2,2"/>
                    <!-- Cardinal Guidelines -->
                    <line x1="80" y1="10" x2="80" y2="150" stroke="#475569" stroke-width="1"/>
                    <line x1="10" y1="80" x2="150" y2="80" stroke="#475569" stroke-width="1"/>
                    <!-- Rotating Firki Group -->
                    <g id="sim6_firki" transform="rotate(0, 80, 80)" class="transition-transform duration-500 ease-out">
                        <polygon points="80,80 80,20 60,40" fill="#38bdf8"/>
                        <circle cx="70" cy="30" r="4" fill="#ef4444"/> <!-- Red Tracking Dot -->
                        <polygon points="80,80 140,80 120,60" fill="#fbbf24"/>
                        <polygon points="80,80 80,140 100,120" fill="#34d399"/>
                        <polygon points="80,80 20,80 40,100" fill="#a855f7"/>
                        <circle cx="80" cy="80" r="5" fill="#f8fafc"/>
                    </g>
                </svg>
            </div>
            <div class="space-y-1.5 font-mono text-[11px]">
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                    <div class="text-slate-400 text-[10px]">Rotation Angle:</div>
                    <div id="sim6_angle_text" class="text-cyan-300 font-bold text-sm">0° (Start)</div>
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700">
                    <div class="text-slate-400 text-[10px]">Dot Position:</div>
                    <div id="sim6_dot_pos" class="text-amber-400 font-bold text-xs">Top (12 o'clock)</div>
                </div>
                <div class="p-1.5 rounded bg-emerald-950/40 border border-emerald-800/40 text-[10px] text-emerald-300">
                    ✨ Outline looks completely identical at every 90° step!
                </div>
            </div>
        </div>
    </div>
    """,

    7: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🔄 Rotational Symmetry Tester</span>
                <span id="sim7_order_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Order 4 (Square)</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Test shapes to determine their order of rotational symmetry and matching angle steps:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim7Select('square')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">Square (Order 4)</button>
                <button onclick="sim7Select('triangle')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">Equilateral (Order 3)</button>
                <button onclick="sim7Select('rectangle')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">Rectangle (Order 2)</button>
                <button onclick="sim7Select('hexagon')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">Hexagon (Order 6)</button>
                <button onclick="sim7Select('scalene')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">Scalene (Order 1)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg viewBox="0 0 160 160" class="w-40 h-40">
                    <!-- Fixed Ghost Outline -->
                    <g id="sim7_ghost"></g>
                    <!-- Rotating Target Shape -->
                    <g id="sim7_shape" transform="rotate(0, 80, 80)"></g>
                    <circle cx="80" cy="80" r="4" fill="#f59e0b"/>
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div>
                    <label class="text-[10px] text-slate-400 flex justify-between">
                        <span>Rotate Shape:</span>
                        <span id="sim7_deg_val" class="text-amber-400 font-bold">0°</span>
                    </label>
                    <input id="sim7_slider" type="range" min="0" max="360" value="0" step="5" oninput="sim7Rotate()" class="w-full accent-amber-400">
                </div>
                <div class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300">
                    <div id="sim7_match_status" class="text-emerald-400 font-bold">✅ Matches Outline! (At 0°)</div>
                    <div id="sim7_details" class="text-[10px] text-slate-400 mt-1">Square matches at 90°, 180°, 270°, 360°.</div>
                </div>
            </div>
        </div>
    </div>
    """,

    8: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🔍 Flip vs Turn Tracing Station</span>
                <span id="sim8_badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Letter S (Rotation Only)</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Compare a Mirror Flip (Reflection) with a 180° Pivot (Rotation) to see how letters behave:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim8Select('S')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700 font-bold">Letter S</button>
                <button onclick="sim8Select('H')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-400 border border-slate-700 font-bold">Letter H</button>
                <button onclick="sim8Select('A')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700 font-bold">Letter A</button>
                <button onclick="sim8Select('N')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-purple-300 border border-slate-700 font-bold">Letter N</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex justify-center items-center bg-slate-950/80 p-2 rounded-xl border border-slate-800">
                <svg id="sim8_svg" viewBox="0 0 160 140" class="w-40 h-32">
                    <!-- Dynamic rendering of base vs transformed letter -->
                </svg>
            </div>
            <div class="space-y-2 font-mono text-[11px]">
                <div class="grid grid-cols-2 gap-1.5">
                    <button onclick="sim8Action('flip')" id="sim8_flip_btn" class="p-2 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-bold text-center">
                        🪞 Mirror Flip
                    </button>
                    <button onclick="sim8Action('turn')" id="sim8_turn_btn" class="p-2 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-bold text-center">
                        🔄 180° Turn
                    </button>
                </div>
                <div id="sim8_result" class="p-2 rounded bg-slate-800/80 border border-slate-700 text-slate-300 text-[10px]">
                    Click Flip or Turn above to test letter invariance!
                </div>
            </div>
        </div>
    </div>
    """
}

