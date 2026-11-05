# -*- coding: utf-8 -*-
"""Class 4 Mathematics Chapter 11 Simulators Dictionary"""

SIMULATORS = {
    1: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-300 font-bold flex items-center justify-center text-sm">01</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Ink Blot Symmetry Studio</h3>
        </div>
        <span class="text-xs text-pink-400 font-medium">Fold & Press Bilateral Mirroring</span>
    </div>

    <!-- Paper Canvas Simulation -->
    <div class="flex justify-center">
        <div id="ink-paper" class="relative w-72 h-44 bg-slate-950 border border-slate-700 rounded-xl overflow-hidden shadow-inner flex">
            <!-- Left Half (Paint Zone) -->
            <div id="ink-left-half" class="relative w-1/2 h-full bg-slate-900/60 border-r-2 border-dashed border-pink-500/80 cursor-crosshair" onclick="addInkDrop(event)">
                <div class="absolute top-1 left-2 text-[10px] text-slate-500 font-mono">Click to drop ink</div>
                <div id="ink-left-drops" class="absolute inset-0"></div>
            </div>
            <!-- Right Half (Mirror Impression Zone) -->
            <div id="ink-right-half" class="relative w-1/2 h-full bg-slate-900/40">
                <div class="absolute top-1 right-2 text-[10px] text-slate-500 font-mono">Mirror half</div>
                <div id="ink-right-drops" class="absolute inset-0 opacity-0 transition-opacity duration-700"></div>
            </div>
        </div>
    </div>

    <!-- Color Palette & Action Buttons -->
    <div class="flex flex-wrap items-center justify-center gap-2 text-xs">
        <span class="text-slate-400 text-[11px] mr-1">Ink Color:</span>
        <button onclick="setInkColor('#ec4899')" class="ink-c-btn w-6 h-6 rounded-full bg-pink-500 ring-2 ring-white transition"></button>
        <button onclick="setInkColor('#06b6d4')" class="ink-c-btn w-6 h-6 rounded-full bg-cyan-500 transition"></button>
        <button onclick="setInkColor('#f59e0b')" class="ink-c-btn w-6 h-6 rounded-full bg-amber-500 transition"></button>
        <button onclick="setInkColor('#10b981')" class="ink-c-btn w-6 h-6 rounded-full bg-emerald-500 transition"></button>
        <button onclick="foldAndPressInk()" id="ink-fold-btn" class="ml-2 px-3 py-1.5 rounded-xl bg-pink-600 hover:bg-pink-500 text-white font-bold transition shadow">Fold & Press</button>
        <button onclick="clearInkBlot()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium transition">Clear</button>
    </div>

    <div id="ink-status" class="text-center text-xs text-slate-400">
        Click anywhere on the left half to deposit wet ink drops, then press <strong>Fold & Press</strong>.
    </div>
</div>
''',
    2: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">02</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Paper Airplane Aerodynamics</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Symmetric vs Asymmetric Glider</span>
    </div>

    <!-- Flight Simulator Sky Box -->
    <div class="relative w-full h-44 bg-slate-950 border border-slate-800 rounded-xl overflow-hidden p-3 flex flex-col justify-between">
        <div class="flex items-center justify-between text-[11px] font-mono text-slate-400">
            <span>Airway Test Tunnel</span>
            <span id="glider-mode-label" class="text-emerald-400 font-bold">Mode: Balanced Symmetrical Glider</span>
        </div>

        <!-- Runway / Flight Path Track -->
        <div class="relative h-20 w-full flex items-center">
            <div class="w-full h-0.5 border-t border-dashed border-slate-800"></div>
            <!-- Airplane SVG Icon -->
            <div id="plane-avatar" class="absolute left-2 transition-all duration-1000 ease-out text-3xl">
                ✈️
            </div>
        </div>

        <div id="flight-telemetry" class="text-xs text-center font-mono text-slate-300 bg-slate-900/80 py-1.5 px-3 rounded-lg border border-slate-800">
            Lift Balance: Left Wing 100% | Right Wing 100% &bull; Stable Linear Glide
        </div>
    </div>

    <!-- Glider Controls -->
    <div class="flex items-center justify-center gap-2 text-xs">
        <button onclick="setPlaneMode('symmetric')" id="plane-sym-btn" class="px-3 py-1.5 rounded-xl bg-cyan-600 text-white font-bold transition">Symmetric Fold</button>
        <button onclick="setPlaneMode('asymmetric')" id="plane-asym-btn" class="px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300 transition">Asymmetric Fold (Bent Wing)</button>
        <button onclick="launchGlider()" class="px-4 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold transition shadow">Launch Flight 🚀</button>
    </div>
</div>
''',
    3: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">03</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Holes and Cuts Unfolding Lab</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Predict 4-Quadrant Unfolding</span>
    </div>

    <!-- Cut Selection -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <span class="text-slate-400 text-[11px] mr-1">Choose Cut:</span>
        <button onclick="setPaperCut('corner_diamond')" class="cut-btn px-2.5 py-1 rounded-lg bg-amber-500 text-slate-950 font-bold">Corner Apex Notch</button>
        <button onclick="setPaperCut('edge_circle')" class="cut-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Outer Edge Hole</button>
        <button onclick="setPaperCut('side_triangle')" class="cut-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Mid-Fold Triangles</button>
    </div>

    <!-- Folded State vs Unfolded Visualizer -->
    <div class="grid grid-cols-2 gap-3 text-center text-xs font-mono">
        <div class="bg-slate-950/70 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center space-y-2">
            <div class="text-slate-400 text-[11px]">Folded State (4 Layers)</div>
            <div id="folded-preview" class="w-20 h-20 bg-amber-500/20 border-2 border-amber-500 rounded-tl-lg relative flex items-center justify-center shadow">
                <!-- Injected via JS -->
            </div>
            <div class="text-[10px] text-slate-500">Corner fold at top-left</div>
        </div>

        <div class="bg-slate-950/70 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center space-y-2">
            <div class="text-slate-400 text-[11px]">Unfolded Full Sheet</div>
            <div id="unfolded-preview" class="w-28 h-28 bg-slate-900 border border-slate-700 relative grid grid-cols-2 grid-rows-2 shadow">
                <!-- Injected 4 quadrants via JS -->
            </div>
            <div id="unfolded-cut-count" class="text-[10px] text-emerald-400 font-bold">1 Center Diamond Cutout</div>
        </div>
    </div>
</div>
''',
    4: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">04</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Dot Grid Symmetry Canvas</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Automatic Reflection Drawing</span>
    </div>

    <!-- Presets -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <span class="text-slate-400 text-[11px] mr-1">Presets:</span>
        <button onclick="loadDotPreset('butterfly')" class="dot-btn px-2.5 py-1 rounded-lg bg-indigo-600 text-white font-bold">Butterfly Wing</button>
        <button onclick="loadDotPreset('vase')" class="dot-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Vase Profile</button>
        <button onclick="loadDotPreset('arrow')" class="dot-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Arrowhead</button>
        <button onclick="loadDotPreset('tree')" class="dot-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Pine Tree</button>
    </div>

    <!-- 7x7 Interactive Dot Grid -->
    <div class="flex justify-center">
        <div class="relative bg-slate-950 p-3 rounded-xl border border-slate-800">
            <!-- Center Red Mirror Line -->
            <div class="absolute top-2 bottom-2 left-1/2 w-0.5 bg-rose-500 -translate-x-1/2 z-10 shadow-[0_0_8px_rgba(244,63,94,0.6)]"></div>
            <div id="dot-grid-board" class="grid grid-cols-7 gap-3 w-56 h-48 place-items-center">
                <!-- 49 dots generated via JS -->
            </div>
        </div>
    </div>

    <div class="text-center text-xs text-slate-400">
        Red vertical axis indicates the line of symmetry. Left dots reflect automatically across to the right.
    </div>
</div>
''',
    5: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">05</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Border Shape Symmetry Tester</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Symmetrical vs Asymmetrical</span>
    </div>

    <!-- Shape Selectors -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <button onclick="testBorderShape('star')" class="bsh-btn px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-bold">Star</button>
        <button onclick="testBorderShape('oval')" class="bsh-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Oval</button>
        <button onclick="testBorderShape('heart')" class="bsh-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Heart</button>
        <button onclick="testBorderShape('arrow')" class="bsh-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Arrow</button>
        <button onclick="testBorderShape('paisley')" class="bsh-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Paisley Motif</button>
    </div>

    <!-- Shape Display with Mirror Line -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-4 flex flex-col items-center justify-center space-y-3">
        <div id="border-shape-view" class="relative w-40 h-28 flex items-center justify-center text-5xl">
            ⭐
        </div>
        <div id="border-shape-analysis" class="text-xs font-mono text-center space-y-1">
            <div class="text-emerald-400 font-bold">5 Lines of Symmetry (Regular 5-Pointed Star)</div>
            <div class="text-slate-400 text-[11px]">Folds symmetrically through each apex vertex to the opposite notch.</div>
        </div>
    </div>
</div>
''',
    6: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-purple-500/20 text-purple-300 font-bold flex items-center justify-center text-sm">06</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Mirror Reflection Digit Lab</h3>
        </div>
        <span class="text-xs text-purple-400 font-medium">Virtual Mirror Invariance</span>
    </div>

    <!-- Presets for Digits & Numbers -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <button onclick="setMirrorDigit('181')" class="mir-btn px-2.5 py-1 rounded-lg bg-purple-600 text-white font-bold">181 (Identical)</button>
        <button onclick="setMirrorDigit('808')" class="mir-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">808 (Identical)</button>
        <button onclick="setMirrorDigit('686')" class="mir-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">686 (Reversed)</button>
        <button onclick="setMirrorDigit('252')" class="mir-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">252 (Reversed)</button>
    </div>

    <!-- Mirror Stand Visualizer -->
    <div class="grid grid-cols-2 gap-3 text-center font-mono">
        <div class="bg-slate-950/70 p-3 rounded-xl border border-slate-800">
            <div class="text-slate-400 text-[11px] mb-1">Direct Viewing</div>
            <div id="direct-num-view" class="text-3xl font-black text-cyan-400">181</div>
            <div class="text-[10px] text-slate-500 mt-1">Normal view</div>
        </div>
        <div class="bg-slate-950/70 p-3 rounded-xl border-r-4 border-r-purple-500 border border-slate-800">
            <div class="text-slate-400 text-[11px] mb-1">Mirror Reflection</div>
            <div id="reflected-num-view" class="text-3xl font-black text-purple-400 inline-block scale-x-[-1]">181</div>
            <div id="mirror-verdict" class="text-[10px] text-emerald-400 font-bold mt-1">Reflects Identically!</div>
        </div>
    </div>
</div>
''',
    7: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-red-500/20 text-red-300 font-bold flex items-center justify-center text-sm">07</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Ambulance Hood Word Mirror</h3>
        </div>
        <span class="text-xs text-red-400 font-medium">Rear-View Mirror Reflection</span>
    </div>

    <!-- Word Presets -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <button onclick="setAmbulanceWord('AMBULANCE')" class="amb-btn px-2.5 py-1 rounded-lg bg-red-600 text-white font-bold">AMBULANCE</button>
        <button onclick="setAmbulanceWord('MOM')" class="amb-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">MOM</button>
        <button onclick="setAmbulanceWord('WOW')" class="amb-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">WOW</button>
        <button onclick="setAmbulanceWord('POLICE')" class="amb-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">POLICE</button>
    </div>

    <!-- Hood View vs Rear-View Mirror -->
    <div class="space-y-2 font-mono text-center">
        <div class="bg-slate-950/80 p-3 rounded-xl border border-slate-800">
            <div class="text-[11px] text-slate-400 mb-1">Painted on Emergency Vehicle Hood (Reversed)</div>
            <div id="amb-hood-text" class="text-xl sm:text-2xl font-black tracking-widest text-red-400 scale-x-[-1] inline-block">AMBULANCE</div>
        </div>

        <div class="bg-slate-900/90 p-3 rounded-xl border-2 border-cyan-500/60 shadow-lg">
            <div class="text-[11px] text-cyan-400 font-bold mb-1">Seen in Driver Rear-View Mirror (Readable!)</div>
            <div id="amb-mirror-text" class="text-xl sm:text-2xl font-black tracking-widest text-emerald-400">AMBULANCE</div>
        </div>
    </div>
</div>
''',
    8: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">08</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Completing Symmetrical Drawings</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Coordinate Mirror Transfer</span>
    </div>

    <!-- Figure Selectors -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <button onclick="setPartialFig('butterfly')" class="pfig-btn px-2.5 py-1 rounded-lg bg-teal-600 text-white font-bold">Butterfly</button>
        <button onclick="setPartialFig('teapot')" class="pfig-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Teapot</button>
        <button onclick="setPartialFig('star')" class="pfig-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Star</button>
    </div>

    <!-- Drawing Board Half & Complete -->
    <div class="flex justify-center">
        <div class="relative w-64 h-36 bg-slate-950 border border-slate-700 rounded-xl overflow-hidden flex">
            <!-- Left Drawn Half -->
            <div id="pfig-left" class="w-1/2 h-full flex items-center justify-end pr-2 border-r-2 border-teal-500 text-4xl">
                🦋
            </div>
            <!-- Right Ghost / Completed Half -->
            <div id="pfig-right" class="w-1/2 h-full flex items-center justify-start pl-2 scale-x-[-1] text-4xl opacity-20 transition-opacity duration-500">
                🦋
            </div>
        </div>
    </div>

    <div class="flex items-center justify-center gap-2">
        <button onclick="revealCompleteFigure()" class="px-4 py-2 rounded-xl bg-teal-600 hover:bg-teal-500 text-white font-bold text-xs transition shadow">Complete Figure</button>
        <button onclick="resetPartialFigure()" class="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs transition">Hide Right Half</button>
    </div>
</div>
''',
    9: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Polygon Symmetry Line Explorer</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">Regular vs Irregular Polygons</span>
    </div>

    <!-- Polygon Selectors -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <button onclick="setPolygonSymmetry('eq_triangle')" class="poly-btn px-2.5 py-1 rounded-lg bg-blue-600 text-white font-bold">Equilateral (3)</button>
        <button onclick="setPolygonSymmetry('iso_triangle')" class="poly-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Isosceles (1)</button>
        <button onclick="setPolygonSymmetry('sca_triangle')" class="poly-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Scalene (0)</button>
        <button onclick="setPolygonSymmetry('square')" class="poly-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Square (4)</button>
        <button onclick="setPolygonSymmetry('rectangle')" class="poly-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Rectangle (2)</button>
        <button onclick="setPolygonSymmetry('hexagon')" class="poly-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Hexagon (6)</button>
    </div>

    <!-- Visual Polygon Canvas -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-4 flex flex-col items-center justify-center space-y-3">
        <div id="polygon-svg-container" class="w-36 h-36 flex items-center justify-center relative">
            <!-- Rendered SVG polygon via JS -->
        </div>
        <div id="polygon-info" class="text-xs font-mono text-center space-y-0.5">
            <div class="text-blue-400 font-bold">Equilateral Triangle: 3 Lines of Symmetry</div>
            <div class="text-slate-400 text-[11px]">3 equal sides &bull; 3 equal 60° angles &bull; Lines bisect each vertex</div>
        </div>
    </div>
</div>
''',
    10: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-yellow-500/20 text-yellow-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Tessellation Angle Laboratory</h3>
        </div>
        <span class="text-xs text-yellow-400 font-medium">360° Vertex Law</span>
    </div>

    <!-- Shape Candidates -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <button onclick="testTessellationShape('square')" class="tess-btn px-2.5 py-1 rounded-lg bg-yellow-500 text-slate-950 font-bold">Square (90°)</button>
        <button onclick="testTessellationShape('triangle')" class="tess-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Triangle (60°)</button>
        <button onclick="testTessellationShape('hexagon')" class="tess-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Hexagon (120°)</button>
        <button onclick="testTessellationShape('pentagon')" class="tess-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Pentagon (108°)</button>
    </div>

    <!-- Vertex Angle Visualizer -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-4 text-center space-y-2 font-mono">
        <div class="text-xs text-slate-400">Corner Meeting Calculation at Vertex:</div>
        <div id="tess-calc" class="text-xl sm:text-2xl font-black text-amber-400">4 × 90° = 360°</div>
        <div id="tess-verdict" class="text-xs text-emerald-400 font-bold bg-emerald-950/40 py-1 px-3 rounded-lg inline-block border border-emerald-800/60">
            Tessellates Seamlessly! No gaps or overlaps.
        </div>
    </div>
</div>
''',
    11: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-lime-500/20 text-lime-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Tile Motion & Transformation</h3>
        </div>
        <span class="text-xs text-lime-400 font-medium">Slides, Flips & Rotations</span>
    </div>

    <!-- Motion Buttons -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <button onclick="applyTileMotion('slide')" class="mot-btn px-2.5 py-1 rounded-lg bg-lime-600 text-white font-bold">Slide (Translate)</button>
        <button onclick="applyTileMotion('flip')" class="mot-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Flip (Reflect)</button>
        <button onclick="applyTileMotion('rotate')" class="mot-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Rotate 90° (Turn)</button>
        <button onclick="applyTileMotion('orientation')" class="mot-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Standing vs Sleeping</button>
    </div>

    <!-- Animated Canvas -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-4 flex flex-col items-center justify-center h-36">
        <div id="animated-tile" class="w-20 h-12 bg-lime-500/20 border-2 border-lime-400 rounded-lg flex items-center justify-center font-bold text-lime-300 text-sm shadow transition-all duration-500">
            Tile A ➔
        </div>
    </div>

    <div id="mot-explanation" class="text-center text-xs text-slate-300 font-mono">
        Slide (Translation): Shifts tile smoothly without turning or flipping.
    </div>
</div>
''',
    12: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Custom Interlocking Tile Studio</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Area Conservation Geometry</span>
    </div>

    <!-- Step Visualizer -->
    <div class="grid grid-cols-3 gap-2 text-center text-xs font-mono">
        <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800">
            <div class="text-slate-400 text-[10px] mb-1">Step 1: Square</div>
            <div class="w-14 h-14 mx-auto bg-amber-500/20 border border-amber-500 rounded"></div>
            <div class="text-[10px] text-slate-500 mt-1">Area = 100 cm²</div>
        </div>
        <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800">
            <div class="text-slate-400 text-[10px] mb-1">Step 2: Cut Edge</div>
            <div class="w-14 h-14 mx-auto bg-amber-500/20 border border-dashed border-amber-500 rounded relative">
                <span class="text-rose-400 absolute left-0 text-xs">-Δ</span>
            </div>
            <div class="text-[10px] text-rose-400 mt-1">Left notch removed</div>
        </div>
        <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800">
            <div class="text-slate-400 text-[10px] mb-1">Step 3: Tape Right</div>
            <div class="w-14 h-14 mx-auto bg-amber-500/30 border border-amber-400 rounded relative">
                <span class="text-emerald-400 absolute -right-2 text-xs">+Δ</span>
            </div>
            <div class="text-[10px] text-emerald-400 mt-1">Area = 100 cm²!</div>
        </div>
    </div>

    <div class="text-center text-xs text-slate-300">
        Removed area on the left is taped to the right. Area is conserved, and two tiles lock together seamlessly!
    </div>
</div>
''',
    13: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Seamless Floor Pattern Designer</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">Bond Strengths & Grout Lines</span>
    </div>

    <!-- Pattern Mode Toggle -->
    <div class="flex justify-center gap-2 text-xs">
        <button onclick="setFloorPattern('stacked')" id="fl-pat-stacked" class="fl-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300">Stacked Grid</button>
        <button onclick="setFloorPattern('running')" id="fl-pat-running" class="fl-btn px-3 py-1.5 rounded-xl bg-orange-600 text-white font-bold">Staggered Running Bond</button>
        <button onclick="setFloorPattern('herringbone')" id="fl-pat-herring" class="fl-btn px-3 py-1.5 rounded-xl bg-slate-800 text-slate-300">Herringbone</button>
    </div>

    <!-- Pavement Canvas -->
    <div class="flex justify-center">
        <div id="floor-canvas" class="w-64 h-28 bg-slate-950 border border-slate-800 rounded-xl p-2 overflow-hidden flex flex-col justify-center">
            <!-- Dynamically rendered floor rows via JS -->
        </div>
    </div>

    <div id="floor-note" class="text-center text-xs text-slate-300">
        Running bond staggers vertical seams by 50%, distributing loads and preventing continuous crack propagation.
    </div>
</div>
''',
    14: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-rose-500/20 text-rose-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Catty Wall Tessellation Craft</h3>
        </div>
        <span class="text-xs text-rose-400 font-medium">Interlocking Cat-Head Tiles</span>
    </div>

    <!-- Visual Catty Wall Grid (2x3 Interlocking Tiles) -->
    <div class="flex justify-center">
        <div class="grid grid-cols-3 gap-1 bg-slate-950 p-2 rounded-xl border border-slate-800 text-center font-mono">
            <div class="cat-tile p-2 rounded-t-xl rounded-b-lg bg-rose-500/20 border border-rose-500/50 text-xs font-bold text-rose-300">🐱 1</div>
            <div class="cat-tile p-2 rounded-t-xl rounded-b-lg bg-rose-500/30 border border-rose-500/60 text-xs font-bold text-rose-200">🐱 2</div>
            <div class="cat-tile p-2 rounded-t-xl rounded-b-lg bg-rose-500/20 border border-rose-500/50 text-xs font-bold text-rose-300">🐱 3</div>
            <div class="cat-tile p-2 rounded-t-xl rounded-b-lg bg-rose-500/30 border border-rose-500/60 text-xs font-bold text-rose-200">🐱 4</div>
            <div class="cat-tile p-2 rounded-t-xl rounded-b-lg bg-rose-500/20 border border-rose-500/50 text-xs font-bold text-rose-300">🐱 5</div>
            <div class="cat-tile p-2 rounded-t-xl rounded-b-lg bg-rose-500/30 border border-rose-500/60 text-xs font-bold text-rose-200">🐱 6</div>
        </div>
    </div>

    <div class="text-center text-xs text-slate-300 space-y-1">
        <div>Top crescent cut translates to bottom chin &bull; Left whisker notch translates to right cheek.</div>
        <div class="text-rose-400 font-semibold">Every cat chin nests between ears of the cat below with zero gaps!</div>
    </div>
</div>
''',
    15: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Nature Walk Symmetry Explorer</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Botanical & Biological Symmetry</span>
    </div>

    <!-- Specimen Selectors -->
    <div class="flex flex-wrap items-center justify-center gap-1.5 text-xs">
        <button onclick="setNatureSpecimen('butterfly')" class="nat-btn px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-bold">Butterfly</button>
        <button onclick="setNatureSpecimen('peepal')" class="nat-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Peepal Leaf</button>
        <button onclick="setNatureSpecimen('flower')" class="nat-btn px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">Marigold Flower</button>
    </div>

    <!-- Specimen Display -->
    <div class="bg-slate-950/70 border border-slate-800 rounded-xl p-4 flex flex-col items-center justify-center space-y-2">
        <div id="nature-icon" class="relative text-6xl">
            🦋
            <div id="nature-mirror-line" class="absolute top-0 bottom-0 left-1/2 w-0.5 bg-emerald-400 -translate-x-1/2 shadow-[0_0_8px_rgba(52,211,153,0.8)]"></div>
        </div>
        <div id="nature-desc" class="text-xs font-mono text-center text-slate-300">
            <span class="font-bold text-emerald-400">Bilateral Wing Symmetry:</span> Left and right wings exhibit identical contours and mirrored spot markings.
        </div>
    </div>
</div>
''',
    16: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Leaf Imprint Symmetry Studio</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Bilateral Botanical Printing</span>
    </div>

    <!-- Leaf Studio Controls -->
    <div class="flex flex-wrap items-center justify-center gap-2 text-xs">
        <span class="text-slate-400 text-[11px] mr-1">Paint Color:</span>
        <button onclick="setLeafPaint('#10b981')" class="leaf-c-btn w-6 h-6 rounded-full bg-emerald-500 ring-2 ring-white transition"></button>
        <button onclick="setLeafPaint('#f59e0b')" class="leaf-c-btn w-6 h-6 rounded-full bg-amber-500 transition"></button>
        <button onclick="setLeafPaint('#ec4899')" class="leaf-c-btn w-6 h-6 rounded-full bg-pink-500 transition"></button>
        <button onclick="stampLeafImprint()" class="ml-2 px-3 py-1.5 rounded-xl bg-teal-600 hover:bg-teal-500 text-white font-bold transition shadow">Stamp & Fold Imprint</button>
        <button onclick="clearLeafImprint()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium transition">Clear</button>
    </div>

    <!-- Paper Imprint Canvas -->
    <div class="flex justify-center">
        <div class="relative w-72 h-36 bg-slate-950 border border-slate-700 rounded-xl overflow-hidden flex">
            <!-- Left Half (Original Leaf Stamp) -->
            <div id="leaf-canvas-left" class="w-1/2 h-full flex items-center justify-center border-r-2 border-dashed border-teal-500 text-4xl">
                🍃
            </div>
            <!-- Right Half (Mirror Stamped Leaf) -->
            <div id="leaf-canvas-right" class="w-1/2 h-full flex items-center justify-center scale-x-[-1] text-4xl opacity-0 transition-opacity duration-700">
                🍃
            </div>
        </div>
    </div>

    <div id="leaf-studio-status" class="text-center text-xs text-slate-400">
        Choose paint color and press <strong>Stamp & Fold Imprint</strong> to generate a bilateral botanical print.
    </div>
</div>
''',
}
