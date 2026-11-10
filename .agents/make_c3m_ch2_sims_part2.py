# -*- coding: utf-8 -*-
"""
Interactive Simulators for Slides 9 to 16
Class 3 Mathematics Chapter 2: Toy Joy
Bespoke SVG/HTML5 interactive laboratory widgets.
"""

simulators_part2 = {
    # Simulator 9: Sorting Solid Shapes
    "sim_shape_property_sorter": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Mechanical Motion Sorting Laboratory</h3>
                <p class="text-xs text-slate-400">Classify solid shapes into bins based on whether they roll only, slide only, or do both!</p>
            </div>
            <div class="flex items-center gap-1.5">
                <button onclick="resetMotionSorter()" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition">
                    🔄 Reset Bins
                </button>
            </div>
        </div>

        <!-- Draggable / Clickable Shape Tray -->
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 flex items-center justify-between gap-2 flex-wrap">
            <span class="text-xs text-slate-400 font-bold">Select Shape:</span>
            <div class="flex items-center gap-2 flex-wrap" id="sorterShapePool">
                <button onclick="selectSorterShape('sphere')" id="poolSphere" class="px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-amber-300">
                    ⚽ Cricket Ball (Sphere)
                </button>
                <button onclick="selectSorterShape('cube')" id="poolCube" class="px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-sky-300">
                    🧊 Wooden Cube
                </button>
                <button onclick="selectSorterShape('cuboid')" id="poolCuboid" class="px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-emerald-300">
                    📦 Book (Cuboid)
                </button>
                <button onclick="selectSorterShape('cylinder')" id="poolCylinder" class="px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-cyan-300">
                    🛢 Water Bottle (Cylinder)
                </button>
                <button onclick="selectSorterShape('cone')" id="poolCone" class="px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-yellow-300">
                    🎉 Party Hat (Cone)
                </button>
            </div>
        </div>

        <!-- 3 Sorting Target Bins -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
            <!-- Bin 1: Rolls Only -->
            <div onclick="dropIntoBin('roll')" class="cursor-pointer bg-slate-950 p-3.5 rounded-xl border-2 border-dashed border-amber-500/40 hover:border-amber-400 transition min-h-[140px] flex flex-col justify-between">
                <div>
                    <div class="text-xs font-bold text-amber-400 flex items-center justify-between">
                        <span>🔄 Rolls Only</span>
                        <span class="text-[10px] text-slate-500">Curved only</span>
                    </div>
                    <div class="mt-2 space-y-1" id="binRollContent">
                        <!-- Populated by JS -->
                    </div>
                </div>
                <div class="text-[10px] text-slate-500 text-center pt-2">Click to place here</div>
            </div>

            <!-- Bin 2: Slides Only -->
            <div onclick="dropIntoBin('slide')" class="cursor-pointer bg-slate-950 p-3.5 rounded-xl border-2 border-dashed border-sky-500/40 hover:border-sky-400 transition min-h-[140px] flex flex-col justify-between">
                <div>
                    <div class="text-xs font-bold text-sky-400 flex items-center justify-between">
                        <span>🛝 Slides Only</span>
                        <span class="text-[10px] text-slate-500">Flat faces only</span>
                    </div>
                    <div class="mt-2 space-y-1" id="binSlideContent">
                        <!-- Populated by JS -->
                    </div>
                </div>
                <div class="text-[10px] text-slate-500 text-center pt-2">Click to place here</div>
            </div>

            <!-- Bin 3: Both Rolls & Slides -->
            <div onclick="dropIntoBin('both')" class="cursor-pointer bg-slate-950 p-3.5 rounded-xl border-2 border-dashed border-emerald-500/40 hover:border-emerald-400 transition min-h-[140px] flex flex-col justify-between">
                <div>
                    <div class="text-xs font-bold text-emerald-400 flex items-center justify-between">
                        <span>⚡ Both Roll & Slide</span>
                        <span class="text-[10px] text-slate-500">Flat & curved</span>
                    </div>
                    <div class="mt-2 space-y-1" id="binBothContent">
                        <!-- Populated by JS -->
                    </div>
                </div>
                <div class="text-[10px] text-slate-500 text-center pt-2">Click to place here</div>
            </div>
        </div>
    </div>
    """,

    # Simulator 10: Clay Stick Skeletons
    "sim_clay_stick_builder": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Clay Ball & Matchstick Skeleton Workbench</h3>
                <p class="text-xs text-slate-400">Assemble wireframe models using clay balls for corners and wooden sticks for straight edges.</p>
            </div>
            <div class="flex items-center gap-1.5">
                <button onclick="selectSkeletonShape('cube')" id="btnSkelCube" class="px-2.5 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition shadow">
                    🎲 Cube
                </button>
                <button onclick="selectSkeletonShape('cuboid')" id="btnSkelCuboid" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition">
                    📦 Cuboid
                </button>
                <button onclick="selectSkeletonShape('pyramid')" id="btnSkelPyramid" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition">
                    ⛺ Square Pyramid
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Skeleton Model Display SVG -->
            <div class="md:col-span-7 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px] flex items-center justify-center">
                <svg id="skeletonSvgCanvas" viewBox="0 0 380 220" class="w-full h-auto max-h-[220px]">
                    <g id="skeletonDrawingGroup">
                        <!-- Populated dynamically by JS -->
                    </g>
                </svg>
            </div>

            <!-- Material Requirements & Assembly Counter -->
            <div class="md:col-span-5 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="text-xs font-bold text-slate-300" id="skeletonShapeTitle">Cube Skeleton</div>

                <div class="grid grid-cols-2 gap-2 text-center">
                    <div class="p-3 bg-slate-900 rounded-lg border border-amber-900/40">
                        <div class="text-[10px] text-slate-400">Clay Balls (Corners)</div>
                        <div class="text-xl font-black text-amber-400 font-mono" id="countClayBalls">8</div>
                    </div>
                    <div class="p-3 bg-slate-900 rounded-lg border border-sky-900/40">
                        <div class="text-[10px] text-slate-400">Matchsticks (Edges)</div>
                        <div class="text-xl font-black text-sky-400 font-mono" id="countMatchsticks">12</div>
                    </div>
                </div>

                <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 text-xs space-y-1">
                    <div class="text-slate-300 font-semibold">Assembly Breakdown:</div>
                    <p class="text-slate-400 text-[11px]" id="skeletonAssemblyDesc">
                        4 sticks form the square base, 4 sticks stand upright as pillars, and 4 sticks join the top corners.
                    </p>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 11: Toy Joy Board
    "sim_toy_joy_board_game": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Toy Joy Geometric Board Game</h3>
                <p class="text-xs text-slate-400">Roll the dotted die to advance your player token along the 20-tile mathematical path.</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="rollGameBoardDie()" id="btnRollBoardDie" class="px-3 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition shadow flex items-center gap-1">
                    🎲 Roll Die
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Board Track SVG Canvas -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px] flex items-center justify-center">
                <svg id="boardGameSvg" viewBox="0 0 460 220" class="w-full h-auto max-h-[220px]">
                    <!-- Winding Pathway of 20 Tiles (4 rows x 5 cols serpentine) -->
                    <g id="boardTilesGroup">
                        <!-- Populated by JS -->
                    </g>
                    <!-- Player Token Pin -->
                    <g id="playerTokenGroup" transform="translate(45, 45)">
                        <circle cx="0" cy="0" r="10" fill="#f59e0b" stroke="#fff" stroke-width="2.5"/>
                        <circle cx="0" cy="0" r="4" fill="#78350f"/>
                    </g>
                </svg>
            </div>

            <!-- Turn Status & Tile Question Card -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs text-slate-400">Die Result:</span>
                    <span id="boardDieRollResult" class="text-base font-black text-amber-400 font-mono">Roll to Start</span>
                </div>

                <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 text-xs space-y-1.5">
                    <div class="flex items-center justify-between">
                        <span class="text-slate-400">Current Tile:</span>
                        <span id="boardCurrentTileNum" class="font-bold text-white font-mono">Tile 1 (Start)</span>
                    </div>
                    <div class="text-amber-300 font-semibold" id="boardTileTitle">Toy Workshop Gate</div>
                    <p class="text-slate-400 text-[11px]" id="boardTileText">
                        Begin your journey! Every step reinforces 3D geometric shape properties.
                    </p>
                </div>

                <div class="flex items-center justify-between text-xs text-slate-400 pt-1">
                    <span>Target:</span>
                    <span class="text-emerald-400 font-bold">Tile 20 (Toy Crown)</span>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 12: Standard Dice Dots (Opposite Faces)
    "sim_dice_opposite_faces": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Standard Dice Opposite Sum Explorer</h3>
                <p class="text-xs text-slate-400">Click any visible face on the die to reveal its opposite partner and verify that they sum to 7.</p>
            </div>
            <div class="flex items-center gap-1.5">
                <button onclick="selectDieFace(1)" id="btnDieFace1" class="px-2 py-1 rounded bg-amber-500 text-slate-950 font-bold text-xs">1</button>
                <button onclick="selectDieFace(2)" id="btnDieFace2" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs">2</button>
                <button onclick="selectDieFace(3)" id="btnDieFace3" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs">3</button>
                <button onclick="selectDieFace(4)" id="btnDieFace4" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs">4</button>
                <button onclick="selectDieFace(5)" id="btnDieFace5" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs">5</button>
                <button onclick="selectDieFace(6)" id="btnDieFace6" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs">6</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Two Opposite Faces Comparison SVG -->
            <div class="md:col-span-7 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px] flex items-center justify-center">
                <svg id="diceOppositeSvg" viewBox="0 0 380 220" class="w-full h-auto max-h-[220px]">
                    <!-- Selected Front Face -->
                    <rect x="50" y="50" width="110" height="110" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="4"/>
                    <text x="105" y="190" fill="#94a3b8" font-size="11" font-weight="bold" text-anchor="middle">Selected Face</text>
                    <g id="diceDotsFrontGroup">
                        <!-- Populated by JS -->
                    </g>

                    <!-- Plus Symbol & Arrow -->
                    <text x="190" y="112" fill="#f59e0b" font-size="28" font-weight="black" text-anchor="middle">➕</text>

                    <!-- Opposite Back Face -->
                    <rect x="220" y="50" width="110" height="110" rx="14" fill="#fef08a" stroke="#facc15" stroke-width="4"/>
                    <text x="275" y="190" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Opposite Face</text>
                    <g id="diceDotsBackGroup">
                        <!-- Populated by JS -->
                    </g>
                </svg>
            </div>

            <!-- Arithmetic Deduction Card -->
            <div class="md:col-span-5 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 text-xs space-y-2">
                    <div class="flex items-center justify-between text-slate-300">
                        <span>Selected Face Value:</span>
                        <span id="dieSelectedVal" class="text-base font-bold text-white font-mono">1</span>
                    </div>
                    <div class="flex items-center justify-between text-slate-300">
                        <span>Hidden Opposite Face:</span>
                        <span id="dieOppositeVal" class="text-base font-bold text-yellow-400 font-mono">7 - 1 = 6</span>
                    </div>
                    <div class="pt-2 border-t border-slate-800 flex items-center justify-between">
                        <span class="text-slate-400 font-semibold">Universal Sum:</span>
                        <span id="dieSumVal" class="text-lg font-black text-emerald-400 font-mono">1 + 6 = 7</span>
                    </div>
                </div>

                <div class="p-2.5 bg-amber-500/10 border border-amber-500/20 rounded-lg text-[11px] text-amber-300">
                    💡 <span class="font-bold">Mental Math Secret:</span> To deduce the hidden number on the bottom of any standard die, simply subtract the top number from 7!
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 13: Joining Identical Cubes
    "sim_two_cubes_join": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Twin Cube Fusion Laboratory</h3>
                <p class="text-xs text-slate-400">Join two identical wooden cubes face-to-face to create a new rectangular cuboid.</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="toggleJoinTwoCubes()" id="btnJoinCubes" class="px-3 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition shadow flex items-center gap-1">
                    🔗 Join Face-to-Face
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Cubes Joining SVG Canvas -->
            <div class="md:col-span-7 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px] flex items-center justify-center">
                <svg id="joinCubesSvg" viewBox="0 0 380 220" class="w-full h-auto max-h-[220px]">
                    <ellipse cx="190" cy="190" rx="140" ry="16" fill="#0f172a" opacity="0.8"/>
                    <g id="joinCubesDisplayGroup">
                        <!-- Rendered by JS: Separate or Fused -->
                    </g>
                </svg>
            </div>

            <!-- Dimensional & Face Tally Card -->
            <div class="md:col-span-5 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs text-slate-400">Composite Shape:</span>
                    <span id="joinShapeStatus" class="text-xs px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 font-bold font-mono">
                        Two Separate Cubes
                    </span>
                </div>

                <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 text-xs space-y-1.5">
                    <div class="flex items-center justify-between">
                        <span class="text-slate-400">Dimensions:</span>
                        <span id="joinDimensions" class="font-mono text-white font-bold">5cm × 5cm each</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <span class="text-slate-400">Faces Hidden in Seam:</span>
                        <span id="joinHiddenFaces" class="font-mono text-amber-400 font-bold">0 faces</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <span class="text-slate-400">Exposed Outer Faces:</span>
                        <span id="joinExposedFaces" class="font-mono text-emerald-400 font-bold">12 faces total</span>
                    </div>
                </div>

                <div class="p-2.5 bg-slate-900/80 rounded border border-slate-800 text-[11px] text-slate-400" id="joinAnalysisNote">
                    Click 'Join Face-to-Face' to fuse the two cubes and watch length double while 2 faces disappear into the seam!
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 14: Three Cube Arrangements
    "sim_three_cube_variations": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Tri-Cube Architecture Configurations</h3>
                <p class="text-xs text-slate-400">Compare straight-line elongated cuboids against right-angled L-shaped corner solids.</p>
            </div>
            <div class="flex items-center gap-1.5">
                <button onclick="setTriCubeLayout('line')" id="btnTriLine" class="px-2.5 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition shadow">
                    ➖ Straight Bar (3×1×1)
                </button>
                <button onclick="setTriCubeLayout('corner')" id="btnTriCorner" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition">
                    📐 L-Shaped Corner
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- 3D Configuration View SVG Canvas -->
            <div class="md:col-span-7 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px] flex items-center justify-center">
                <svg id="triCubeSvg" viewBox="0 0 380 220" class="w-full h-auto max-h-[220px]">
                    <g id="triCubeRenderGroup">
                        <!-- Populated by JS -->
                    </g>
                </svg>
            </div>

            <!-- Property Comparison Card -->
            <div class="md:col-span-5 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="text-xs font-bold text-slate-300" id="triConfigTitle">Configuration: Straight Bar</div>

                <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 text-xs space-y-1.5">
                    <div class="flex items-center justify-between">
                        <span class="text-slate-400">Total Unit Cubes:</span>
                        <span class="text-white font-bold font-mono">3 unit cubes</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <span class="text-slate-400">Geometric Solid:</span>
                        <span id="triSolidClassification" class="text-amber-400 font-bold font-mono">Rectangular Cuboid</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <span class="text-slate-400">Exposed Unit Faces:</span>
                        <span id="triExposedCount" class="text-emerald-400 font-bold font-mono">14 unit squares</span>
                    </div>
                </div>

                <div class="p-2.5 bg-slate-900/80 rounded border border-slate-800 text-[11px] text-slate-400" id="triConfigNote">
                    Three cubes in a row form an elongated cuboid. Rearranging into an L-shape keeps volume constant but creates concave inner corners!
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 15: Composite Model Stacks (Hidden Block Counter)
    "sim_cube_block_counter": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Multi-Tier Block Stack & Staircase Inspector</h3>
                <p class="text-xs text-slate-400">Deduce hidden foundation cubes beneath upper tiers using X-ray transparency mode.</p>
            </div>
            <div class="flex items-center gap-1.5">
                <button onclick="toggleBlockStackXray()" id="btnBlockXray" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-cyan-500/40 font-bold text-xs transition shadow flex items-center gap-1">
                    🔍 Toggle X-Ray View
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Isometric Staircase SVG Canvas -->
            <div class="md:col-span-7 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px] flex items-center justify-center">
                <svg id="staircaseSvg" viewBox="0 0 380 220" class="w-full h-auto max-h-[220px]">
                    <ellipse cx="190" cy="195" rx="140" ry="18" fill="#0f172a" opacity="0.8"/>
                    <g id="staircaseCubesGroup">
                        <!-- Populated by JS -->
                    </g>
                </svg>
            </div>

            <!-- Column Counting Deduction Box -->
            <div class="md:col-span-5 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="text-xs font-bold text-slate-300">Column Height Breakdown:</div>

                <div class="space-y-1.5 text-xs">
                    <div class="p-2 rounded bg-slate-900 border border-slate-800 flex items-center justify-between">
                        <span class="text-slate-400">Column 1 (Front Step):</span>
                        <span class="text-amber-400 font-bold font-mono">1 cube</span>
                    </div>
                    <div class="p-2 rounded bg-slate-900 border border-slate-800 flex items-center justify-between">
                        <span class="text-slate-400">Column 2 (Middle Step):</span>
                        <span class="text-amber-400 font-bold font-mono">2 cubes (1 hidden base)</span>
                    </div>
                    <div class="p-2 rounded bg-slate-900 border border-slate-800 flex items-center justify-between">
                        <span class="text-slate-400">Column 3 (Top Step):</span>
                        <span class="text-amber-400 font-bold font-mono">3 cubes (2 hidden base)</span>
                    </div>
                </div>

                <div class="p-3 bg-emerald-950/40 border border-emerald-500/40 rounded-lg flex items-center justify-between text-xs">
                    <span class="text-emerald-300 font-semibold">Total Unit Cubes:</span>
                    <span class="text-base font-black text-emerald-400 font-mono">1 + 2 + 3 = 6</span>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 16: Master Geometry Matrix
    "sim_master_geometry_table": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Master 3D Solid Geometry Matrix</h3>
                <p class="text-xs text-slate-400">Synthesize and compare Cube, Cuboid, Cylinder, Cone, and Sphere across all mathematical properties.</p>
            </div>
            <div class="flex items-center gap-1.5 flex-wrap">
                <button onclick="filterMatrixShape('all')" class="px-2 py-1 rounded bg-amber-500 text-slate-950 font-bold text-xs">All</button>
                <button onclick="filterMatrixShape('cube')" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs">Cube</button>
                <button onclick="filterMatrixShape('cuboid')" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs">Cuboid</button>
                <button onclick="filterMatrixShape('cylinder')" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs">Cylinder</button>
                <button onclick="filterMatrixShape('cone')" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs">Cone</button>
                <button onclick="filterMatrixShape('sphere')" class="px-2 py-1 rounded bg-slate-800 text-slate-300 font-bold text-xs">Sphere</button>
            </div>
        </div>

        <!-- Master Matrix Interactive Table -->
        <div class="overflow-x-auto rounded-xl border border-slate-800 bg-slate-950">
            <table class="w-full text-left text-xs">
                <thead class="bg-slate-900 text-slate-400 font-semibold border-b border-slate-800">
                    <tr>
                        <th class="p-2.5">Solid Shape</th>
                        <th class="p-2.5">Flat Faces</th>
                        <th class="p-2.5">Curved Surfaces</th>
                        <th class="p-2.5">Edges</th>
                        <th class="p-2.5">Corners</th>
                        <th class="p-2.5">Motion</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-800/60 font-mono text-slate-300" id="matrixTableBody">
                    <tr id="rowMatrixCube" class="hover:bg-slate-900/50 transition">
                        <td class="p-2.5 font-bold text-white flex items-center gap-1.5"><span>🎲</span> Cube</td>
                        <td class="p-2.5 text-emerald-400">6 (Equal Squares)</td>
                        <td class="p-2.5 text-slate-500">0</td>
                        <td class="p-2.5 text-sky-400">12 (Straight)</td>
                        <td class="p-2.5 text-amber-400">8</td>
                        <td class="p-2.5 text-emerald-300 font-sans">Slides & Stacks</td>
                    </tr>
                    <tr id="rowMatrixCuboid" class="hover:bg-slate-900/50 transition">
                        <td class="p-2.5 font-bold text-white flex items-center gap-1.5"><span>📦</span> Cuboid</td>
                        <td class="p-2.5 text-emerald-400">6 (Rectangles)</td>
                        <td class="p-2.5 text-slate-500">0</td>
                        <td class="p-2.5 text-sky-400">12 (Straight)</td>
                        <td class="p-2.5 text-amber-400">8</td>
                        <td class="p-2.5 text-emerald-300 font-sans">Slides & Stacks</td>
                    </tr>
                    <tr id="rowMatrixCylinder" class="hover:bg-slate-900/50 transition">
                        <td class="p-2.5 font-bold text-white flex items-center gap-1.5"><span>🛢</span> Cylinder</td>
                        <td class="p-2.5 text-emerald-400">2 (Circles)</td>
                        <td class="p-2.5 text-yellow-400">1</td>
                        <td class="p-2.5 text-sky-400">2 (Curved)</td>
                        <td class="p-2.5 text-slate-500">0</td>
                        <td class="p-2.5 text-cyan-300 font-sans">Rolls, Slides, Stacks</td>
                    </tr>
                    <tr id="rowMatrixCone" class="hover:bg-slate-900/50 transition">
                        <td class="p-2.5 font-bold text-white flex items-center gap-1.5"><span>🔺</span> Cone</td>
                        <td class="p-2.5 text-emerald-400">1 (Circle)</td>
                        <td class="p-2.5 text-yellow-400">1</td>
                        <td class="p-2.5 text-sky-400">1 (Curved)</td>
                        <td class="p-2.5 text-amber-400">1 (Apex)</td>
                        <td class="p-2.5 text-cyan-300 font-sans">Rolls (arc) & Slides</td>
                    </tr>
                    <tr id="rowMatrixSphere" class="hover:bg-slate-900/50 transition">
                        <td class="p-2.5 font-bold text-white flex items-center gap-1.5"><span>⚽</span> Sphere</td>
                        <td class="p-2.5 text-slate-500">0</td>
                        <td class="p-2.5 text-yellow-400">1 (Continuous)</td>
                        <td class="p-2.5 text-slate-500">0</td>
                        <td class="p-2.5 text-slate-500">0</td>
                        <td class="p-2.5 text-amber-300 font-sans">Rolls freely in all directions</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    """
}

