# -*- coding: utf-8 -*-
"""
Generator for NCERT Class 7 Mathematics - Chapter 9: Geometric Twins (Congruence) Simulators
Generates .agents/class7_math_geometric_twins_sims.py with 16 bespoke SVG simulators.
"""

sims = {
    # 1. Superposition & Rigid Motion Studio
    "sim-superposition-flipper": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Superposition & Rigid Motion Studio</span>
                <span id="supStatusBadge" class="px-2 py-0.5 text-xs font-bold rounded bg-amber-500/20 text-amber-300 border border-amber-500/40">Not Superimposed</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="supSvg" viewBox="0 0 500 200" class="w-full h-full">
                    <!-- Base Triangle T1 and Movable Triangle T2 -->
                </svg>
            </div>
            <div class="mt-2.5 grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Horizontal Shift ($X$):</span>
                        <span id="supXVal" class="text-cyan-300 font-bold font-mono">0 px</span>
                    </div>
                    <input id="supXSlider" type="range" min="0" max="220" value="0" oninput="updateSuperposition()" class="w-full accent-cyan-400">
                </div>
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Rotation Angle:</span>
                        <span id="supRotVal" class="text-amber-300 font-bold font-mono">0&deg;</span>
                    </div>
                    <input id="supRotSlider" type="range" min="0" max="360" value="0" oninput="updateSuperposition()" class="w-full accent-amber-400">
                </div>
                <div class="flex flex-col justify-around gap-1.5">
                    <button onclick="snapSuperposition()" class="py-1.5 px-3 bg-emerald-500/30 hover:bg-emerald-500/40 text-emerald-300 font-bold rounded border border-emerald-500/50 text-center">
                        &check; Snap to Exact Superposition!
                    </button>
                    <button onclick="resetSuperposition()" class="py-1 px-3 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded border border-slate-700 text-center">
                        Reset Positions
                    </button>
                </div>
            </div>
            <div id="supExplanation" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800 text-center font-mono">
                Slide the horizontal shift or click <strong>Snap to Exact Superposition</strong> to test if Triangle A covers Triangle B identically!
            </div>
        </div>
    """,

    # 2. Simple Figures Congruence
    "sim-simple-figures-congruence": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Congruence in Simple Figures</span>
                <div class="flex gap-1">
                    <button onclick="setSimpleFigureMode('lines')" id="sfLinesBtn" class="px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/30 text-amber-300 border border-amber-500/50">Lines</button>
                    <button onclick="setSimpleFigureMode('angles')" id="sfAnglesBtn" class="px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700">Angles</button>
                    <button onclick="setSimpleFigureMode('circles')" id="sfCirclesBtn" class="px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700">Circles</button>
                    <button onclick="setSimpleFigureMode('rects')" id="sfRectsBtn" class="px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700">Rectangles</button>
                </div>
            </div>
            <div class="relative w-full h-52 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="sfSvg" viewBox="0 0 500 180" class="w-full h-full">
                    <!-- Dynamic simple figures drawn by JS -->
                </svg>
            </div>
            <div class="mt-2 flex flex-wrap items-center justify-between gap-2 text-xs bg-slate-800/60 p-2 rounded border border-slate-700">
                <div id="sfControls" class="flex items-center gap-3">
                    <!-- Sliders populated dynamically by JS -->
                </div>
                <div id="sfVerdict" class="font-mono text-emerald-300 font-bold">
                    Lengths match: Congruent (AB &cong; CD)!
                </div>
            </div>
        </div>
    """,

    # 3. Triangle Vertex Correspondence Studio
    "sim-triangle-correspondence": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Vertex Correspondence & CPCTC Studio</span>
                <span class="text-xs font-mono text-cyan-300">$$\\triangle ABC \\cong \\triangle PQR$$</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="tcSvg" viewBox="0 0 500 200" class="w-full h-full">
                    <!-- Dual Triangles ABC and PQR with matched colored vertices and sides -->
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-3 gap-2 text-center text-xs">
                <button onclick="highlightCorrespondence('A')" class="p-1.5 bg-slate-800 hover:bg-slate-700 rounded border border-amber-500/40 text-amber-300">
                    Vertex $A \\leftrightarrow P$ (Red)
                </button>
                <button onclick="highlightCorrespondence('B')" class="p-1.5 bg-slate-800 hover:bg-slate-700 rounded border border-cyan-500/40 text-cyan-300">
                    Vertex $B \\leftrightarrow Q$ (Cyan)
                </button>
                <button onclick="highlightCorrespondence('C')" class="p-1.5 bg-slate-800 hover:bg-slate-700 rounded border border-emerald-500/40 text-emerald-300">
                    Vertex $C \\leftrightarrow R$ (Green)
                </button>
            </div>
            <div id="tcDetails" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800 text-center font-mono">
                Click any vertex pair above to observe matching corresponding angles and opposite side equalities!
            </div>
        </div>
    """,

    # 4. SSS Congruence Lab
    "sim-sss-congruence": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">SSS (Side-Side-Side) Rigidity Lab</span>
                <span class="text-xs font-mono text-amber-300">3 Equal Sides &rArr; Complete Rigidity</span>
            </div>
            <div class="relative w-full h-52 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="sssSvg" viewBox="0 0 500 180" class="w-full h-full">
                    <!-- Two SSS Triangles with side markers -->
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Side a ($BC = EF$):</span>
                        <span id="sssAVal" class="text-amber-300 font-bold font-mono">8 cm</span>
                    </div>
                    <input id="sssASlider" type="range" min="6" max="12" value="8" oninput="updateSSS()" class="w-full accent-amber-400">
                </div>
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Side b ($AC = DF$):</span>
                        <span id="sssBVal" class="text-cyan-300 font-bold font-mono">7 cm</span>
                    </div>
                    <input id="sssBSlider" type="range" min="5" max="10" value="7" oninput="updateSSS()" class="w-full accent-cyan-400">
                </div>
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Side c ($AB = DE$):</span>
                        <span id="sssCVal" class="text-emerald-300 font-bold font-mono">6 cm</span>
                    </div>
                    <input id="sssCSlider" type="range" min="4" max="9" value="6" oninput="updateSSS()" class="w-full accent-emerald-400">
                </div>
            </div>
            <div id="sssVerdict" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800 text-center font-mono">
                All 3 pairs of sides are identical: $AB = DE = 6$, $BC = EF = 8$, $AC = DF = 7$. Thus $\\triangle ABC \\cong \\triangle DEF$ by SSS!
            </div>
        </div>
    """,

    # 5. SAS Congruence Lab
    "sim-sas-congruence": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">SAS (Side-Angle-Side) Included Angle Lab</span>
                <span class="text-xs font-mono text-cyan-300">$$\\angle B = \\angle Q$$ (Included Angle)</span>
            </div>
            <div class="relative w-full h-52 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="sasSvg" viewBox="0 0 500 180" class="w-full h-full">
                    <!-- Two Triangles showing 2 sides and included angle arc -->
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Side 1 ($AB = PQ$):</span>
                        <span id="sasS1Val" class="text-amber-300 font-bold font-mono">6 cm</span>
                    </div>
                    <input id="sasS1Slider" type="range" min="4" max="10" value="6" oninput="updateSAS()" class="w-full accent-amber-400">
                </div>
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Included Angle $\\theta$:</span>
                        <span id="sasAngVal" class="text-rose-400 font-bold font-mono">55&deg;</span>
                    </div>
                    <input id="sasAngSlider" type="range" min="30" max="110" value="55" oninput="updateSAS()" class="w-full accent-rose-500">
                </div>
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Side 2 ($BC = QR$):</span>
                        <span id="sasS2Val" class="text-cyan-300 font-bold font-mono">8 cm</span>
                    </div>
                    <input id="sasS2Slider" type="range" min="5" max="12" value="8" oninput="updateSAS()" class="w-full accent-cyan-400">
                </div>
            </div>
            <div id="sasVerdict" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800 text-center font-mono">
                Two sides and included angle $55^\\circ$ locked &rarr; closing third side is uniquely determined!
            </div>
        </div>
    """,

    # 6. Included Angle Trap
    "sim-included-angle-trap": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">The "Included vs Non-Included" Trap</span>
                <div class="flex gap-2">
                    <button onclick="setTrapMode('included')" id="trapIncBtn" class="px-2 py-0.5 rounded text-xs font-semibold bg-emerald-500/30 text-emerald-300 border border-emerald-500/50">Included (SAS &check;)</button>
                    <button onclick="setTrapMode('non_included')" id="trapNonBtn" class="px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700">Non-Included (SSA &cross;)</button>
                </div>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="trapSvg" viewBox="0 0 500 200" class="w-full h-full">
                    <!-- Demonstration of swinging arm in SSA vs fixed arm in SAS -->
                </svg>
            </div>
            <div id="trapExplanation" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800 text-center font-mono">
                In SAS, the angle is sandwiched between the two arms, clamping the opening firmly!
            </div>
        </div>
    """,

    # 7. ASA Congruence Lab
    "sim-asa-congruence": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">ASA (Angle-Side-Angle) Baseline Ray Lab</span>
                <span class="text-xs font-mono text-cyan-300">$$\\angle B - BC - \\angle C$$</span>
            </div>
            <div class="relative w-full h-52 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="asaSvg" viewBox="0 0 500 180" class="w-full h-full">
                    <!-- Fixed baseline and two converging ray angles -->
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Angle B ($\angle B$):</span>
                        <span id="asaBVal" class="text-amber-300 font-bold font-mono">60&deg;</span>
                    </div>
                    <input id="asaBSlider" type="range" min="30" max="80" value="60" oninput="updateASA()" class="w-full accent-amber-400">
                </div>
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Included Baseline ($BC$):</span>
                        <span id="asaBaseVal" class="text-cyan-300 font-bold font-mono">10 cm</span>
                    </div>
                    <input id="asaBaseSlider" type="range" min="6" max="14" value="10" oninput="updateASA()" class="w-full accent-cyan-400">
                </div>
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Angle C ($\angle C$):</span>
                        <span id="asaCVal" class="text-emerald-300 font-bold font-mono">50&deg;</span>
                    </div>
                    <input id="asaCSlider" type="range" min="30" max="80" value="50" oninput="updateASA()" class="w-full accent-emerald-400">
                </div>
            </div>
            <div id="asaVerdict" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800 text-center font-mono">
                Ray from $B$ at $60^\\circ$ and ray from $C$ at $50^\\circ$ intersect at apex $A$ uniquely!
            </div>
        </div>
    """,

    # 8. AAS Congruence Lab
    "sim-aas-congruence": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">AAS (Angle-Angle-Side) Reduction Studio</span>
                <span id="aasThirdAngleBadge" class="text-xs font-mono text-emerald-300">$$\\angle C = 180^\\circ - (\\angle A + \\angle B)$$</span>
            </div>
            <div class="relative w-full h-52 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="aasSvg" viewBox="0 0 500 180" class="w-full h-full">
                    <!-- AAS Triangle with automated calculation of 3rd angle turning it into ASA -->
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Angle A:</span>
                        <span id="aasAVal" class="text-amber-300 font-bold font-mono">50&deg;</span>
                    </div>
                    <input id="aasASlider" type="range" min="30" max="80" value="50" oninput="updateAAS()" class="w-full accent-amber-400">
                </div>
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Angle B:</span>
                        <span id="aasBVal" class="text-cyan-300 font-bold font-mono">70&deg;</span>
                    </div>
                    <input id="aasBSlider" type="range" min="30" max="80" value="70" oninput="updateAAS()" class="w-full accent-cyan-400">
                </div>
                <div class="p-2.5 bg-slate-900 rounded border border-amber-500/40 flex flex-col justify-center text-center">
                    <span class="text-slate-400 text-[10px]">DERIVED 3RD ANGLE</span>
                    <span id="aasCComputed" class="text-emerald-400 font-bold font-mono text-sm">$$\\angle C = 60^\\circ$$</span>
                    <span class="text-slate-400 text-[10px] mt-0.5">Converts AAS to ASA!</span>
                </div>
            </div>
        </div>
    """,

    # 9. RHS Congruence Lab
    "sim-rhs-congruence": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">RHS (Right-Hypotenuse-Side) Criterion</span>
                <span class="text-xs font-mono text-amber-300">Baudhāyana Cord Rule: $$b = \\sqrt{h^2 - a^2}$$</span>
            </div>
            <div class="relative w-full h-52 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="rhsSvg" viewBox="0 0 500 180" class="w-full h-full">
                    <!-- Right triangles with 90° square symbol, hypotenuse and leg -->
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Hypotenuse ($AC = PR$):</span>
                        <span id="rhsHypVal" class="text-cyan-300 font-bold font-mono">10 cm</span>
                    </div>
                    <input id="rhsHypSlider" type="range" min="8" max="15" value="10" oninput="updateRHS()" class="w-full accent-cyan-400">
                </div>
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Known Leg ($AB = PQ$):</span>
                        <span id="rhsLegVal" class="text-amber-300 font-bold font-mono">6 cm</span>
                    </div>
                    <input id="rhsLegSlider" type="range" min="4" max="7" value="6" oninput="updateRHS()" class="w-full accent-amber-400">
                </div>
                <div class="p-2.5 bg-slate-900 rounded border border-emerald-500/40 flex flex-col justify-center text-center">
                    <span class="text-slate-400 text-[10px]">AUTOMATIC THIRD LEG</span>
                    <span id="rhsThirdLeg" class="text-emerald-400 font-bold font-mono text-sm">$$BC = \\sqrt{10^2 - 6^2} = 8\\text{ cm}$$</span>
                </div>
            </div>
        </div>
    """,

    # 10. AAA Counterexample Dilation Studio
    "sim-aaa-counterexample": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">AAA Counterexample: Same Shape, Different Size!</span>
                <span class="text-xs font-bold px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/40">Similar &ne; Congruent</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="aaaSvg" viewBox="0 0 500 200" class="w-full h-full">
                    <!-- Base triangle and scaled dilated twin with matching angles -->
                </svg>
            </div>
            <div class="mt-2 flex flex-wrap items-center justify-between gap-3 text-xs bg-slate-800/60 p-2.5 rounded border border-slate-700">
                <div class="flex items-center gap-2 flex-1">
                    <span class="text-slate-300">Dilation Scale ($k$):</span>
                    <input id="aaaScaleSlider" type="range" min="10" max="25" value="18" oninput="updateAAA()" class="w-36 accent-rose-500">
                    <span id="aaaScaleText" class="text-rose-400 font-mono font-bold">1.8&times; Scale</span>
                </div>
                <div class="text-slate-300 font-mono text-[11px]" id="aaaAngleProof">
                    Angles: $50^\circ, 60^\circ, 70^\circ$ on both &rarr; but Area is $3.24\times$ larger!
                </div>
            </div>
        </div>
    """,

    # 11. SSA Ambiguous Case
    "sim-ssa-ambiguous-case": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">SSA Ambiguous Case: The Swinging Pendulum</span>
                <span class="text-xs font-bold px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/40">2 Triangles Formed!</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="ssaSvg" viewBox="0 0 500 200" class="w-full h-full">
                    <!-- Arc swinging and hitting base line in two distinct points B1 and B2 -->
                </svg>
            </div>
            <div class="mt-2 flex flex-wrap items-center justify-between gap-2 text-xs">
                <div class="flex gap-2">
                    <button onclick="setSsaPosition('acute')" id="ssaAcuteBtn" class="px-3 py-1 bg-amber-500/30 text-amber-300 rounded border border-amber-500/50">Show Acute &triangle; ($B_1$)</button>
                    <button onclick="setSsaPosition('obtuse')" id="ssaObtuseBtn" class="px-3 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700">Show Obtuse &triangle; ($B_2$)</button>
                    <button onclick="toggleSsaSwing()" id="ssaSwingBtn" class="px-3 py-1 bg-rose-500/30 text-rose-300 rounded border border-rose-500/50">&circlearrowright; Swing Arm</button>
                </div>
                <div id="ssaStatus" class="font-mono text-slate-300 text-[11px]">
                    Side $a$ hits base at 2 distinct points!
                </div>
            </div>
        </div>
    """,

    # 12. Isosceles Base Angles Proof
    "sim-isosceles-base-angles": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Isosceles Base Angles Theorem Studio</span>
                <span class="text-xs font-mono text-amber-300">$$AB = AC \\implies \\angle B = \\angle C$$</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="isoSvg" viewBox="0 0 500 200" class="w-full h-full">
                    <!-- Isosceles triangle with altitude line splitting into ABD and ACD -->
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-slate-400">Apex Angle ($\angle A$):</span>
                        <span id="isoApexVal" class="text-amber-300 font-bold font-mono">50&deg;</span>
                    </div>
                    <input id="isoApexSlider" type="range" min="30" max="110" value="50" oninput="updateIsosceles()" class="w-full accent-amber-400">
                </div>
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700 text-center flex flex-col justify-center">
                    <span class="text-slate-400 text-[10px]">EQUAL BASE ANGLES</span>
                    <span id="isoBaseAngles" class="text-emerald-400 font-bold font-mono text-sm">$$\\angle B = \\angle C = 65^\\circ$$</span>
                </div>
                <div class="flex items-center justify-center">
                    <button onclick="foldIsosceles()" id="isoFoldBtn" class="w-full py-2 bg-cyan-500/30 hover:bg-cyan-500/40 text-cyan-200 font-bold rounded border border-cyan-500/50">
                        Fold Along Altitude $AD$
                    </button>
                </div>
            </div>
        </div>
    """,

    # 13. Equilateral 60 Degree Harmony
    "sim-equilateral-60deg": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Equilateral Triangle 60&deg; Invariance Studio</span>
                <span class="text-xs font-mono text-emerald-300">$$\\angle A = \\angle B = \\angle C = 60^\\circ$$</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="eqSvg" viewBox="0 0 500 200" class="w-full h-full">
                    <!-- Equilateral triangle with 3 symmetry axes and 60° angle badges -->
                </svg>
            </div>
            <div class="mt-2 flex flex-wrap items-center justify-between gap-3 text-xs bg-slate-800/60 p-2 rounded border border-slate-700">
                <div class="flex items-center gap-2">
                    <span class="text-slate-300">Side Length ($s$):</span>
                    <input id="eqSideSlider" type="range" min="6" max="14" value="10" oninput="updateEquilateral()" class="w-32 accent-emerald-400">
                    <span id="eqSideVal" class="text-emerald-300 font-mono font-bold">10 cm</span>
                </div>
                <button onclick="toggleEquilateralAxes()" id="eqAxesBtn" class="px-3 py-1 bg-amber-500/30 text-amber-200 rounded border border-amber-500/40 font-semibold">
                    Toggle 3 Symmetry Axes
                </button>
                <div class="text-slate-400 font-mono text-[11px]">
                    $180^\circ / 3 = 60^\circ$ (Universally invariant)
                </div>
            </div>
        </div>
    """,

    # 14. Master Criteria Sorter
    "sim-congruence-criteria-sorter": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Master 5-Criteria Decision Sorter</span>
                <span id="mcsScore" class="text-xs font-mono text-cyan-300">Score: 0 / 5</span>
            </div>
            <div class="p-4 bg-slate-950 rounded-xl border border-slate-800 flex flex-col items-center">
                <div class="text-center mb-3">
                    <span class="text-slate-400 text-xs block mb-1">Active Scenario:</span>
                    <span id="mcsScenarioText" class="text-amber-300 font-bold font-mono text-sm sm:text-base">
                        Scenario 1: Sides AB = DE, BC = EF, and included &ang;B = &ang;E.
                    </span>
                </div>
                <!-- 5 Criteria Buttons + 1 Invalid -->
                <div class="grid grid-cols-3 sm:grid-cols-6 gap-2 w-full text-xs">
                    <button onclick="answerCriteriaSort('SSS')" class="p-2 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-cyan-300 font-bold">SSS</button>
                    <button onclick="answerCriteriaSort('SAS')" class="p-2 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-cyan-300 font-bold">SAS</button>
                    <button onclick="answerCriteriaSort('ASA')" class="p-2 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-cyan-300 font-bold">ASA</button>
                    <button onclick="answerCriteriaSort('AAS')" class="p-2 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-cyan-300 font-bold">AAS</button>
                    <button onclick="answerCriteriaSort('RHS')" class="p-2 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-cyan-300 font-bold">RHS</button>
                    <button onclick="answerCriteriaSort('INVALID')" class="p-2 bg-rose-900/40 hover:bg-rose-900/60 rounded border border-rose-700 text-rose-300 font-bold">Invalid</button>
                </div>
            </div>
            <div id="mcsFeedback" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800 text-center">
                Select the correct criterion for the given scenario above!
            </div>
        </div>
    """,

    # 15. Real World Twins & Tessellations
    "sim-real-world-twins": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Real-World Congruence & Tessellations</span>
                <div class="flex gap-1.5">
                    <button onclick="setRwMode('bridge')" id="rwBridgeBtn" class="px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/30 text-amber-300 border border-amber-500/50">Truss Bridge</button>
                    <button onclick="setRwMode('butterfly')" id="rwButterflyBtn" class="px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700">Butterfly Wings</button>
                    <button onclick="setRwMode('tessellation')" id="rwTessBtn" class="px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700">Tessellation</button>
                </div>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="rwSvg" viewBox="0 0 500 200" class="w-full h-full">
                    <!-- Bridge truss or butterfly wings or tiling pattern -->
                </svg>
            </div>
            <div id="rwDescription" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800 text-center">
                Warren truss bridges use alternating congruent triangles to balance compression and tension forces across the span.
            </div>
        </div>
    """,

    # 16. Congruence Detective & CPCTC Solver
    "sim-congruence-puzzle-lab": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Congruence Detective: Solve via CPCTC</span>
                <span class="text-xs font-mono text-cyan-300">Find Unknowns $x$ and $y$</span>
            </div>
            <div class="p-4 bg-slate-950 rounded-xl border border-slate-800 flex flex-col items-center">
                <div class="flex flex-wrap items-center justify-center gap-4 font-mono text-sm">
                    <div class="p-3 bg-slate-900 rounded-lg border border-amber-500/40 text-center">
                        <span class="text-slate-400 block text-[10px]">SIDE EQUALITY (CPCTC)</span>
                        <span class="text-amber-300 font-bold">$3x - 4 = 14\\text{ cm}$</span>
                    </div>
                    <span class="text-slate-500 font-bold">&rArr;</span>
                    <div class="p-3 bg-slate-900 rounded-lg border border-cyan-500/40 text-center">
                        <span class="text-slate-400 block text-[10px]">ANGLE EQUALITY (CPCTC)</span>
                        <span class="text-cyan-300 font-bold">$2y + 10^\\circ = 80^\\circ$</span>
                    </div>
                </div>
            </div>
            <div class="mt-3 flex flex-wrap items-center justify-center gap-3 text-xs">
                <button onclick="revealCpctcStep1()" class="px-3 py-1.5 bg-amber-500/30 hover:bg-amber-500/40 text-amber-200 font-bold rounded border border-amber-500/50">
                    Step 1: Solve for $x$
                </button>
                <button onclick="revealCpctcStep2()" class="px-3 py-1.5 bg-cyan-500/30 hover:bg-cyan-500/40 text-cyan-200 font-bold rounded border border-cyan-500/50">
                    Step 2: Solve for $y$
                </button>
                <button onclick="resetCpctcPuzzle()" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded border border-slate-700">
                    New Puzzle
                </button>
            </div>
            <div id="cpctcResultBox" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800 text-center font-mono">
                Click Step 1 or Step 2 to deduce the algebraic values of $x$ and $y$ using CPCTC!
            </div>
        </div>
    """
}

with open('.agents/class7_math_geometric_twins_sims.py', 'w', encoding='utf-8') as f:
    f.write(f"SIMULATORS = {repr(sims)}\n")

print("Created .agents/class7_math_geometric_twins_sims.py successfully with 16 bespoke simulators!")

