import sys

def build_sims():
    SIMULATORS = []

    # Sim 1: Boundary Walk Simulator
    sim1 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Boundary Walk Simulator</span>
                <span id="walkPerimeterBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Perimeter: 32 cm</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="walkSvg" class="w-full h-full max-h-[210px]" viewBox="0 0 320 200">
                    <polygon id="walkPolygon" points="60,160 260,160 260,60 60,60" fill="#0284c7" fill-opacity="0.15" stroke="#38bdf8" stroke-width="2.5"/>
                    <g id="walkSideLabels"></g>
                    <circle id="walkAntDot" cx="60" cy="160" r="6" fill="#f59e0b" stroke="#fef08a" stroke-width="2"/>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <button onclick="startBoundaryWalk()" class="px-3 py-1.5 bg-amber-600 hover:bg-amber-500 text-slate-950 rounded-lg font-bold flex items-center gap-1.5">
                    <span>🚶</span> Walk Boundary
                </button>
                <div class="flex gap-1.5">
                    <button onclick="setWalkShape('rect')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-bold text-[11px]">Rectangle</button>
                    <button onclick="setWalkShape('tri')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-bold text-[11px]">Triangle</button>
                    <button onclick="setWalkShape('pent')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-bold text-[11px]">Polygon</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim1.strip())

    # Sim 2: Dynamic Rectangle & Square Perimeter Calculator
    sim2 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Formula Sandbox</span>
                <span id="rectFormulaBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">2(8 + 5) = 26 cm</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="rectScaleSvg" class="w-full h-full max-h-[170px]" viewBox="0 0 320 180">
                    <g id="rectShapeGroup"></g>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 space-y-2 text-xs">
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <div class="flex justify-between text-[11px] mb-0.5">
                            <span class="text-slate-400">Length (l):</span>
                            <span id="sliderLenVal" class="font-mono text-amber-300 font-bold">8 cm</span>
                        </div>
                        <input id="sliderLength" type="range" min="2" max="14" value="8" oninput="updateRectFormula()" class="w-full accent-amber-500">
                    </div>
                    <div>
                        <div class="flex justify-between text-[11px] mb-0.5">
                            <span class="text-slate-400">Breadth (b):</span>
                            <span id="sliderBrdVal" class="font-mono text-cyan-300 font-bold">5 cm</span>
                        </div>
                        <input id="sliderBreadth" type="range" min="1" max="10" value="5" oninput="updateRectFormula()" class="w-full accent-cyan-500">
                    </div>
                </div>
                <div class="flex items-center justify-between">
                    <label class="flex items-center gap-1.5 cursor-pointer text-slate-300 text-[11px]">
                        <input id="lockSquareCheck" type="checkbox" onchange="toggleSquareLock()" class="rounded accent-emerald-500">
                        <span>Lock as Square (l = b)</span>
                    </label>
                    <span id="rectPResult" class="font-mono font-bold text-emerald-400">Perimeter = 26 cm</span>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim2.strip())

    # Sim 3: Regular Polygon Perimeter Lab
    sim3 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Regular Polygon Lab</span>
                <span id="regPolyBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Hexagon: 6 × 6 = 36 cm</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="regPolySvg" class="w-full h-full max-h-[180px]" viewBox="0 0 240 180">
                    <polygon id="regPolygonPath" points="" fill="#10b981" fill-opacity="0.2" stroke="#34d399" stroke-width="2.5"/>
                    <g id="regPolyLabels"></g>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 space-y-1.5 text-xs">
                <div class="flex items-center justify-between">
                    <span class="text-[11px] text-slate-400">Side (s): <span id="regSideVal" class="font-mono text-amber-300 font-bold">6 cm</span></span>
                    <input id="regSideSlider" type="range" min="2" max="10" value="6" oninput="updateRegPoly()" class="w-36 accent-amber-500">
                </div>
                <div class="flex items-center justify-between">
                    <span class="text-[11px] text-slate-400">Sides (n):</span>
                    <div class="flex gap-1">
                        <button onclick="setRegPolySides(3)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono font-bold text-[11px]">3 (Tri)</button>
                        <button onclick="setRegPolySides(4)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono font-bold text-[11px]">4 (Sq)</button>
                        <button onclick="setRegPolySides(5)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono font-bold text-[11px]">5 (Pent)</button>
                        <button onclick="setRegPolySides(6)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono font-bold text-[11px]">6 (Hex)</button>
                        <button onclick="setRegPolySides(8)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono font-bold text-[11px]">8 (Oct)</button>
                    </div>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim3.strip())

    # Sim 4: Concentric Race Track Stagger Simulator
    sim4 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Race Track Stagger</span>
                <span id="staggerFeedbackBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Lane 2 is 8m longer</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="trackSvg" class="w-full h-full max-h-[190px]" viewBox="0 0 320 190">
                    <!-- Outer Lane -->
                    <rect x="40" y="25" width="240" height="140" rx="30" fill="none" stroke="#f59e0b" stroke-width="3"/>
                    <!-- Inner Lane -->
                    <rect x="65" y="45" width="190" height="100" rx="20" fill="none" stroke="#38bdf8" stroke-width="3"/>
                    <!-- Finish Line -->
                    <line x1="160" y1="20" x2="160" y2="50" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="3,2"/>
                    <text x="160" y="14" fill="#f43f5e" font-size="9" font-weight="bold" text-anchor="middle">FINISH</text>
                    <!-- Runners -->
                    <circle id="runnerInner" cx="160" cy="45" r="5" fill="#38bdf8"/>
                    <circle id="runnerOuter" cx="160" cy="25" r="5" fill="#f59e0b"/>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <button onclick="applyFairStagger()" class="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-slate-950 rounded-lg font-bold">
                    Apply Fair Stagger
                </button>
                <button onclick="resetTrack()" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg font-bold">
                    Reset Starts
                </button>
            </div>
        </div>
    """
    SIMULATORS.append(sim4.strip())

    # Sim 5: Dot Grid Perimeter Explorer
    sim5 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Dot Grid Perimeter</span>
                <span id="dotPerimeterBadge" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">Perimeter: 6s + 4d</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="dotGridSvg" class="w-full h-full max-h-[190px]" viewBox="0 0 240 190">
                    <g id="dotGridDotsGroup"></g>
                    <g id="dotGridLinesGroup"></g>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Presets:</span>
                <div class="flex gap-1.5">
                    <button onclick="loadDotShape('arrow')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold text-[11px]">Arrow (6s+2d)</button>
                    <button onclick="loadDotShape('crown')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold text-[11px]">Crown (6s+4d)</button>
                    <button onclick="loadDotShape('diamond')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold text-[11px]">Diamond (0s+4d)</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim5.strip())

    # Sim 6: Split & Rejoin Paradox Lab
    sim6 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Split & Rejoin Paradox</span>
                <span id="splitParadoxBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Area = 16 cm² (Constant!)</span>
            </div>
            <div class="flex-1 flex flex-col items-center justify-center p-2 text-center">
                <div id="splitShapeContainer" class="flex items-center justify-center min-h-[130px] my-1"></div>
                <div class="grid grid-cols-2 gap-2 w-full max-w-xs text-xs mt-1">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 text-[10px] block">Surface Area</span>
                        <span id="splitAreaVal" class="font-mono font-bold text-emerald-400 text-sm">16 cm²</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 text-[10px] block">Perimeter</span>
                        <span id="splitPerimeterVal" class="font-mono font-bold text-amber-400 text-sm">16 cm</span>
                    </div>
                </div>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Configurations:</span>
                <div class="flex gap-1.5">
                    <button onclick="setSplitConfig('square')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-bold text-[11px]">Square (4×4)</button>
                    <button onclick="setSplitConfig('rect')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold text-[11px]">Rect (8×2)</button>
                    <button onclick="setSplitConfig('strip')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-bold text-[11px]">Strip (16×1)</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim6.strip())

    # Sim 7: Why Squares Tile (Tessellation Comparison)
    sim7 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Why Square Units?</span>
                <span id="tileCompareBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Square Tiles: Zero Gaps!</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="tessellationSvg" class="w-full h-full max-h-[190px]" viewBox="0 0 240 180">
                    <g id="tessellationGroup"></g>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <div class="flex gap-1.5">
                    <button onclick="setTessellationMode('squares')" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold">Square Tiles (Clean)</button>
                    <button onclick="setTessellationMode('circles')" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-bold">Circular Coins (Gaps!)</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim7.strip())

    # Sim 8: Room & Carpet Area Subtraction
    sim8 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Floor & Carpet Subtraction</span>
                <span id="carpetResultBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Uncarpeted = 11 m²</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="carpetSvg" class="w-full h-full max-h-[180px]" viewBox="0 0 260 170">
                    <rect x="30" y="25" width="200" height="120" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
                    <rect id="carpetPatch" x="70" y="45" width="120" height="80" fill="#b45309" fill-opacity="0.6" stroke="#f59e0b" stroke-width="2"/>
                    <text x="130" y="20" fill="#94a3b8" font-size="10" text-anchor="middle">Floor: 5m × 4m (20 m²)</text>
                    <text x="130" y="90" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">Carpet: 3m × 3m (9 m²)</text>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Presets:</span>
                <div class="flex gap-1.5">
                    <button onclick="setCarpetPreset(5, 4, 3, 3)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold text-[11px]">Room 20 / Carpet 9</button>
                    <button onclick="setCarpetPreset(6, 5, 4, 3)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold text-[11px]">Room 30 / Carpet 12</button>
                    <button onclick="setCarpetPreset(7, 5, 5, 4)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold text-[11px]">Room 35 / Carpet 20</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim8.strip())

    # Sim 9: Tangram Dissection & Relative Units
    sim9 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Tangram Relative Areas</span>
                <span id="tangramTotalBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Total Square = 16 units</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="tangramSvg" class="w-full h-full max-h-[190px]" viewBox="0 0 200 200">
                    <!-- Large Triangle 1 (4 units) -->
                    <polygon points="0,0 200,0 100,100" fill="#3b82f6" fill-opacity="0.8" stroke="#1e293b" stroke-width="2" onclick="selectTangramPiece('Large Triangle 1', 4)"/>
                    <!-- Large Triangle 2 (4 units) -->
                    <polygon points="0,0 0,200 100,100" fill="#6366f1" fill-opacity="0.8" stroke="#1e293b" stroke-width="2" onclick="selectTangramPiece('Large Triangle 2', 4)"/>
                    <!-- Small Triangle 1 (1 unit) -->
                    <polygon points="100,100 150,50 150,150" fill="#10b981" fill-opacity="0.8" stroke="#1e293b" stroke-width="2" onclick="selectTangramPiece('Small Triangle 1', 1)"/>
                    <!-- Tangram Square (2 units) -->
                    <polygon points="100,100 50,150 100,200 150,150" fill="#f59e0b" fill-opacity="0.8" stroke="#1e293b" stroke-width="2" onclick="selectTangramPiece('Square Piece', 2)"/>
                    <!-- Medium Triangle (2 units) -->
                    <polygon points="200,0 200,200 100,200" fill="#ec4899" fill-opacity="0.8" stroke="#1e293b" stroke-width="2" onclick="selectTangramPiece('Medium Triangle', 2)"/>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span id="tangramPieceInfo" class="text-slate-300 text-[11px]">Click any piece to inspect relative area</span>
                <button onclick="resetTangramInspect()" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-400 rounded text-[11px]">Reset</button>
            </div>
        </div>
    """
    SIMULATORS.append(sim9.strip())

    # Sim 10: Grid Area Estimator (4-Step Protocol)
    sim10 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Grid Area Estimator</span>
                <span id="leafEstimateBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Area ≈ 17 sq units</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="leafGridSvg" class="w-full h-full max-h-[190px]" viewBox="0 0 200 180">
                    <g id="leafGridBack"></g>
                    <path id="leafPathOutline" d="M 100,20 C 160,50 170,130 100,165 C 30,130 40,50 100,20 Z" fill="#10b981" fill-opacity="0.25" stroke="#34d399" stroke-width="2"/>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 grid grid-cols-4 gap-1 text-center text-[10px] font-mono">
                <div class="p-1 rounded bg-slate-900 border border-slate-800 text-emerald-400">Full: 10</div>
                <div class="p-1 rounded bg-slate-900 border border-slate-800 text-cyan-400">>0.5: 5</div>
                <div class="p-1 rounded bg-slate-900 border border-slate-800 text-amber-400">0.5: 4</div>
                <div class="p-1 rounded bg-slate-900 border border-slate-800 text-slate-500"><0.5: 0</div>
            </div>
        </div>
    """
    SIMULATORS.append(sim10.strip())

    # Sim 11: Same Area, Varied Perimeters Lab
    sim11 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Fixed Area = 24 cm²</span>
                <span id="varyPBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">4 × 6: Perimeter = 20 cm</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="varySvg" class="w-full h-full max-h-[180px]" viewBox="0 0 320 180">
                    <g id="varyRectGroup"></g>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Dimensions:</span>
                <div class="flex gap-1.5">
                    <button onclick="setVaryDimensions(4, 6)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold text-[11px]">4×6 (P=20)</button>
                    <button onclick="setVaryDimensions(3, 8)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold text-[11px]">3×8 (P=22)</button>
                    <button onclick="setVaryDimensions(2, 12)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold text-[11px]">2×12 (P=28)</button>
                    <button onclick="setVaryDimensions(1, 24)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-bold text-[11px]">1×24 (P=50)</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim11.strip())

    # Sim 12: Making It More or Less (Unit Square Surgery)
    sim12 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Perimeter Surgery</span>
                <span id="surgeryBadge" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">Base Shape: P = 12</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="surgerySvg" class="w-full h-full max-h-[180px]" viewBox="0 0 240 180">
                    <g id="surgeryBaseGroup"></g>
                    <g id="surgeryAddedGroup"></g>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Attach Square:</span>
                <div class="flex gap-1.5">
                    <button onclick="attachSquare('edge')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold text-[11px]">Edge (+2)</button>
                    <button onclick="attachSquare('corner')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold text-[11px]">Corner (+0)</button>
                    <button onclick="attachSquare('pocket')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-bold text-[11px]">Pocket (−2)</button>
                    <button onclick="attachSquare('reset')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-400 rounded text-[11px]">Reset</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim12.strip())

    # Sim 13: Architectural Floor Plan Navigator
    sim13 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">House Floor Plan</span>
                <span id="floorTotalBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Total Area: 45 m²</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="housePlanSvg" class="w-full h-full max-h-[190px]" viewBox="0 0 280 180">
                    <!-- Living Room 6m x 4m (24m2) -->
                    <rect class="cursor-pointer hover:brightness-125 transition" x="30" y="20" width="140" height="90" fill="#0284c7" fill-opacity="0.6" stroke="#38bdf8" stroke-width="2" onclick="inspectRoom('Living Room', 6, 4, 24)"/>
                    <text x="100" y="70" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Living Room (24m²)</text>
                    <!-- Bedroom 4m x 3m (12m2) -->
                    <rect class="cursor-pointer hover:brightness-125 transition" x="170" y="20" width="80" height="90" fill="#d97706" fill-opacity="0.6" stroke="#f59e0b" stroke-width="2" onclick="inspectRoom('Bedroom', 4, 3, 12)"/>
                    <text x="210" y="70" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Bed (12m²)</text>
                    <!-- Kitchen 3m x 3m (9m2) -->
                    <rect class="cursor-pointer hover:brightness-125 transition" x="30" y="110" width="90" height="50" fill="#059669" fill-opacity="0.6" stroke="#10b981" stroke-width="2" onclick="inspectRoom('Kitchen', 3, 3, 9)"/>
                    <text x="75" y="140" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Kitchen (9m²)</text>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span id="roomInspectInfo" class="text-slate-300 text-[11px]">Click any room to view dimensions</span>
            </div>
        </div>
    """
    SIMULATORS.append(sim13.strip())

    # Sim 14: Area Maze Logic Puzzle (Menseki Meiro)
    sim14 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Area Maze Logic (Menseki Meiro)</span>
                <span id="mazeStatusBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Find Missing '?'</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="mazeSvg" class="w-full h-full max-h-[190px]" viewBox="0 0 260 170">
                    <!-- Left Box: Area 18 cm2, Width 3 cm -> Height 6 cm -->
                    <rect x="30" y="25" width="80" height="120" fill="#0284c7" fill-opacity="0.4" stroke="#38bdf8" stroke-width="2"/>
                    <text x="70" y="80" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">18 cm²</text>
                    <text x="70" y="160" fill="#cbd5e1" font-size="10" text-anchor="middle">3 cm</text>
                    <!-- Right Box: Area 24 cm2, Height 6 cm -> Width 4 cm -->
                    <rect x="110" y="25" width="110" height="120" fill="#059669" fill-opacity="0.4" stroke="#10b981" stroke-width="2"/>
                    <text x="165" y="80" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">24 cm²</text>
                    <text id="mazeQuestionMark" x="165" y="160" fill="#f59e0b" font-size="12" font-weight="black" text-anchor="middle">? cm</text>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <button onclick="revealMazeStep()" class="px-3 py-1.5 bg-amber-600 hover:bg-amber-500 text-slate-950 rounded font-bold">
                    Deduce Step-by-Step
                </button>
                <span id="mazeDeductionText" class="text-[11px] text-slate-300 font-mono">18 ÷ 3 = Height 6 cm</span>
            </div>
        </div>
    """
    SIMULATORS.append(sim14.strip())

    # Sim 15: Triangle Diagonal Split Lab
    sim15 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Triangle Area Derivation</span>
                <span id="triDeriveBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Area = 1/2 × b × h</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="triSplitSvg" class="w-full h-full max-h-[190px]" viewBox="0 0 280 180">
                    <!-- Base Rectangle -->
                    <rect x="40" y="30" width="200" height="120" fill="#1e293b" stroke="#475569" stroke-width="2"/>
                    <!-- Diagonal -->
                    <line x1="40" y1="150" x2="240" y2="30" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,3"/>
                    <!-- Highlighted Triangle -->
                    <polygon id="triHighlightPoly" points="40,150 240,150 240,30" fill="#10b981" fill-opacity="0.4" stroke="#34d399" stroke-width="2"/>
                    <text x="140" y="165" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">Base (b = 10 cm)</text>
                    <text x="255" y="95" fill="#cbd5e1" font-size="10" font-weight="bold">Height (h = 6 cm)</text>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-300 font-mono">Triangle = (10 × 6) ÷ 2 = <strong>30 cm²</strong></span>
                <button onclick="toggleTriangleHighlight()" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold text-[11px]">
                    Flip Triangle
                </button>
            </div>
        </div>
    """
    SIMULATORS.append(sim15.strip())

    # Sim 16: Composite Grid Shape Decomposer
    sim16 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Composite Grid Decomposer</span>
                <span id="compositeTotalBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Total Area = 21 sq units</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="compositeSvg" class="w-full h-full max-h-[190px]" viewBox="0 0 280 180">
                    <g id="compositeGridBg"></g>
                    <!-- Arrow: Shaft (Rectangle 6x2 = 12) + Head (Triangle base 6, height 3 = 9) -->
                    <rect id="compShaft" x="50" y="70" width="120" height="40" fill="#0284c7" fill-opacity="0.6" stroke="#38bdf8" stroke-width="2"/>
                    <polygon id="compHead" points="170,40 230,90 170,140" fill="#d97706" fill-opacity="0.6" stroke="#f59e0b" stroke-width="2"/>
                    <text x="110" y="95" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">Rect: 12</text>
                    <text x="190" y="95" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">Tri: 9</text>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <button onclick="toggleCompositeDecompose()" class="px-3 py-1.5 bg-amber-600 hover:bg-amber-500 text-slate-950 rounded font-bold">
                    Decompose / Merge
                </button>
                <span id="compFormulaExplain" class="text-[11px] text-slate-300 font-mono">12 (Shaft) + 9 (Head) = 21</span>
            </div>
        </div>
    """
    SIMULATORS.append(sim16.strip())

    code = f'''"""NCERT Class 6 Mathematics Chapter 6: Perimeter and Area Simulators Module."""

SIMULATORS = {SIMULATORS}
'''

    # Strict check for raw LaTeX
    forbidden = ["\\text", "\\frac", "\\circ", "\\angle", "\\overleftrightarrow", "\\overline", "\\vec", "\\approx", "\\dots", "\\sqrt"]
    for word in forbidden:
        if word in code:
            raise ValueError(f"CRITICAL ERROR: Found raw LaTeX '{word}' in simulators module!")

    # Check for surrogates
    clean_chars = [ch for ch in code if not (0xD800 <= ord(ch) <= 0xDFFF)]
    clean_code = ''.join(clean_chars)

    with open(".agents/class6_math_perimeter_area_sims.py", "w", encoding="utf-8") as f:
        f.write(clean_code)

    print("Successfully generated .agents/class6_math_perimeter_area_sims.py with 16 bespoke simulators.")
    print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in simulators module!")

if __name__ == "__main__":
    build_sims()

