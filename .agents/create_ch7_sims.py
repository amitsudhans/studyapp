import json

sims = {
    # 1. Triangle Anatomy
    "sim-triangle-anatomy": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Interactive Triangle Anatomy</span>
                <div class="flex gap-2">
                    <button onclick="resetAnatomy()" class="px-2.5 py-1 text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-600">Reset</button>
                    <button onclick="toggleAnatomyLabels()" class="px-2.5 py-1 text-xs font-semibold bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 rounded border border-amber-500/40">Toggle Labels</button>
                </div>
            </div>
            <div class="relative w-full h-64 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="anatomySvg" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Infinite intersecting lines -->
                    <line id="lineAB" x1="0" y1="210" x2="500" y2="210" stroke="#334155" stroke-dasharray="4 4" stroke-width="1.5" />
                    <line id="lineAC" x1="50" y1="240" x2="350" y2="10" stroke="#334155" stroke-dasharray="4 4" stroke-width="1.5" />
                    <line id="lineBC" x1="450" y1="240" x2="150" y2="10" stroke="#334155" stroke-dasharray="4 4" stroke-width="1.5" />
                    
                    <!-- Triangle Body -->
                    <polygon id="triPoly" points="100,200 400,200 250,50" fill="rgba(245, 158, 11, 0.15)" stroke="#f59e0b" stroke-width="3" />
                    
                    <!-- Interior angle arcs -->
                    <path id="arcA" d="" fill="rgba(6, 182, 212, 0.3)" stroke="#06b6d4" stroke-width="1.5" />
                    <path id="arcB" d="" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="1.5" />
                    <path id="arcC" d="" fill="rgba(244, 63, 94, 0.3)" stroke="#f43f5e" stroke-width="1.5" />

                    <!-- Side labels -->
                    <text id="lblSideC" x="250" y="220" text-anchor="middle" fill="#f59e0b" class="text-xs font-bold font-mono">Side c (AB)</text>
                    <text id="lblSideA" x="345" y="120" text-anchor="middle" fill="#10b981" class="text-xs font-bold font-mono">Side a (BC)</text>
                    <text id="lblSideB" x="155" y="120" text-anchor="middle" fill="#06b6d4" class="text-xs font-bold font-mono">Side b (CA)</text>

                    <!-- Vertices -->
                    <circle id="vA" cx="100" cy="200" r="8" fill="#f59e0b" stroke="#fff" stroke-width="2" class="cursor-pointer" />
                    <text x="80" y="215" fill="#f59e0b" class="text-sm font-bold font-mono">A</text>
                    <circle id="vB" cx="400" cy="200" r="8" fill="#10b981" stroke="#fff" stroke-width="2" class="cursor-pointer" />
                    <text x="415" y="215" fill="#10b981" class="text-sm font-bold font-mono">B</text>
                    <circle id="vC" cx="250" cy="50" r="8" fill="#06b6d4" stroke="#fff" stroke-width="2" class="cursor-pointer" />
                    <text x="250" y="35" text-anchor="middle" fill="#06b6d4" class="text-sm font-bold font-mono">C (Apex)</text>
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-3 gap-2 text-center text-xs">
                <div class="p-2 bg-slate-800 rounded border border-slate-700">
                    <span class="text-slate-400 block">Vertex A Angle</span>
                    <span id="txtAngleA" class="text-amber-400 font-bold font-mono text-sm">63.4°</span>
                </div>
                <div class="p-2 bg-slate-800 rounded border border-slate-700">
                    <span class="text-slate-400 block">Vertex B Angle</span>
                    <span id="txtAngleB" class="text-emerald-400 font-bold font-mono text-sm">63.4°</span>
                </div>
                <div class="p-2 bg-slate-800 rounded border border-slate-700">
                    <span class="text-slate-400 block">Vertex C Angle</span>
                    <span id="txtAngleC" class="text-cyan-400 font-bold font-mono text-sm">53.2°</span>
                </div>
            </div>
            <div class="mt-2 flex items-center justify-between text-xs text-slate-400">
                <span>Drag Apex C horizontally:</span>
                <input id="apexSlider" type="range" min="120" max="380" value="250" oninput="updateAnatomyApex(this.value)" class="w-48 accent-amber-500">
            </div>
        </div>
    """,

    # 2. Equilateral Triangle Compass
    "sim-equilateral-compass": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Compass & Arc Construction</span>
                <div class="flex gap-1.5">
                    <button onclick="stepEquilateral(1)" class="px-2 py-1 text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-600">1. Base AB</button>
                    <button onclick="stepEquilateral(2)" class="px-2 py-1 text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-600">2. Arc from A</button>
                    <button onclick="stepEquilateral(3)" class="px-2 py-1 text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-600">3. Arc from B</button>
                    <button onclick="stepEquilateral(4)" class="px-2 py-1 text-xs font-semibold bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 rounded border border-amber-500/40">4. Complete</button>
                </div>
            </div>
            <div class="relative w-full h-64 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="equiSvg" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Base AB -->
                    <line id="eqBase" x1="160" y1="190" x2="340" y2="190" stroke="#f59e0b" stroke-width="3" />
                    <circle cx="160" cy="190" r="5" fill="#f59e0b" />
                    <text x="145" y="200" fill="#f59e0b" class="text-xs font-bold font-mono">A</text>
                    <circle cx="340" cy="190" r="5" fill="#f59e0b" />
                    <text x="350" y="200" fill="#f59e0b" class="text-xs font-bold font-mono">B</text>
                    <text id="eqBaseLbl" x="250" y="210" text-anchor="middle" fill="#f59e0b" class="text-xs font-mono">Base s = 180 px</text>

                    <!-- Arc from A -->
                    <path id="eqArcA" d="" fill="none" stroke="#06b6d4" stroke-width="2" stroke-dasharray="5 3" class="transition-all duration-500 opacity-0" />
                    <!-- Arc from B -->
                    <path id="eqArcB" d="" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="5 3" class="transition-all duration-500 opacity-0" />

                    <!-- Apex C -->
                    <circle id="eqApexPt" cx="250" cy="34.1" r="6" fill="#f43f5e" class="transition-all duration-500 opacity-0" />
                    <text id="eqApexLbl" x="250" y="22" text-anchor="middle" fill="#f43f5e" class="text-xs font-bold font-mono opacity-0">C (Apex)</text>

                    <!-- Side AC & BC -->
                    <line id="eqSideAC" x1="160" y1="190" x2="250" y2="34.1" stroke="#06b6d4" stroke-width="3" class="transition-all duration-500 opacity-0" />
                    <line id="eqSideBC" x1="340" y1="190" x2="250" y2="34.1" stroke="#10b981" stroke-width="3" class="transition-all duration-500 opacity-0" />

                    <!-- Angle tags -->
                    <g id="eqAngleTags" class="opacity-0 transition-opacity duration-500">
                        <text x="180" y="175" fill="#06b6d4" class="text-xs font-bold">60°</text>
                        <text x="305" y="175" fill="#10b981" class="text-xs font-bold">60°</text>
                        <text x="240" y="65" fill="#f43f5e" class="text-xs font-bold">60°</text>
                    </g>
                </svg>
            </div>
            <div id="eqStatus" class="mt-2 p-2 bg-slate-800 rounded border border-slate-700 text-xs text-slate-300">
                Step 1: Base segment $AB$ of length $s$ is drawn with a straight ruler.
            </div>
        </div>
    """,

    # 3. Triangle Inequality Tester
    "sim-triangle-inequality": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Live Triangle Inequality Tester</span>
                <div class="flex gap-1.5">
                    <button onclick="setInequalityPreset(6, 8, 10)" class="px-2 py-0.5 text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 rounded">Valid (6,8,10)</button>
                    <button onclick="setInequalityPreset(4, 5, 9)" class="px-2 py-0.5 text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 rounded">Flat Line (4,5,9)</button>
                    <button onclick="setInequalityPreset(3, 4, 9)" class="px-2 py-0.5 text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 rounded">Gap (3,4,9)</button>
                </div>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="ineqSvg" viewBox="0 0 500 220" class="w-full h-full">
                    <!-- Base C -->
                    <line id="ineqBase" x1="100" y1="180" x2="400" y2="180" stroke="#f59e0b" stroke-width="4" />
                    <text id="ineqBaseLbl" x="250" y="205" text-anchor="middle" fill="#f59e0b" class="text-xs font-bold font-mono">Base c = 10 cm</text>
                    
                    <!-- Arm A and Arm B -->
                    <line id="ineqArmA" x1="100" y1="180" x2="250" y2="80" stroke="#06b6d4" stroke-width="4" stroke-linecap="round" />
                    <line id="ineqArmB" x1="400" y1="180" x2="250" y2="80" stroke="#10b981" stroke-width="4" stroke-linecap="round" />
                    
                    <!-- Apex -->
                    <circle id="ineqApex" cx="250" cy="80" r="6" fill="#f43f5e" />
                    
                    <!-- Result badge inside SVG -->
                    <rect id="ineqBadgeRect" x="180" y="15" width="140" height="26" rx="6" fill="#10b981" opacity="0.2" />
                    <text id="ineqBadgeText" x="250" y="32" text-anchor="middle" fill="#10b981" class="text-xs font-bold font-mono">TRIANGLE FORMED</text>
                </svg>
            </div>
            <!-- Sliders for sides a, b, c -->
            <div class="mt-2 grid grid-cols-3 gap-2 text-xs">
                <div class="p-2 bg-slate-800 rounded border border-slate-700">
                    <div class="flex justify-between mb-1">
                        <span class="text-cyan-400 font-bold">Side a (Left)</span>
                        <span id="valA" class="font-mono text-cyan-300">6 cm</span>
                    </div>
                    <input id="sliderA" type="range" min="2" max="12" value="6" oninput="updateInequality()" class="w-full accent-cyan-500">
                </div>
                <div class="p-2 bg-slate-800 rounded border border-slate-700">
                    <div class="flex justify-between mb-1">
                        <span class="text-emerald-400 font-bold">Side b (Right)</span>
                        <span id="valB" class="font-mono text-emerald-300">8 cm</span>
                    </div>
                    <input id="sliderB" type="range" min="2" max="12" value="8" oninput="updateInequality()" class="w-full accent-emerald-500">
                </div>
                <div class="p-2 bg-slate-800 rounded border border-slate-700">
                    <div class="flex justify-between mb-1">
                        <span class="text-amber-400 font-bold">Base c</span>
                        <span id="valC" class="font-mono text-amber-300">10 cm</span>
                    </div>
                    <input id="sliderC" type="range" min="4" max="14" value="10" oninput="updateInequality()" class="w-full accent-amber-500">
                </div>
            </div>
            <!-- Condition checks readout -->
            <div class="mt-2 p-2 bg-slate-800/80 rounded border border-slate-700 flex justify-around text-xs font-mono">
                <span id="chk1" class="text-emerald-400">a + b > c (6+8 > 10) ✓</span>
                <span id="chk2" class="text-emerald-400">b + c > a (8+10 > 6) ✓</span>
                <span id="chk3" class="text-emerald-400">c + a > b (10+6 > 8) ✓</span>
            </div>
        </div>
    """,

    # 4. Circle Intersections
    "sim-circle-intersections": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Circle Intersection Laboratory</span>
                <span id="circCaseLabel" class="px-2 py-0.5 text-xs font-bold bg-emerald-500/20 text-emerald-300 rounded border border-emerald-500/40">2 Intersections (Triangle Exists)</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="circSvg" viewBox="0 0 500 220" class="w-full h-full">
                    <!-- Base line AB -->
                    <line x1="160" y1="110" x2="340" y2="110" stroke="#f59e0b" stroke-width="2" />
                    <circle cx="160" cy="110" r="4" fill="#f59e0b" />
                    <text x="145" y="115" fill="#f59e0b" class="text-xs font-bold">A</text>
                    <circle cx="340" cy="110" r="4" fill="#f59e0b" />
                    <text x="350" y="115" fill="#f59e0b" class="text-xs font-bold">B</text>

                    <!-- Circle A -->
                    <circle id="circA" cx="160" cy="110" r="110" fill="rgba(6, 182, 212, 0.08)" stroke="#06b6d4" stroke-width="1.5" />
                    <!-- Circle B -->
                    <circle id="circB" cx="340" cy="110" r="100" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1.5" />

                    <!-- Intersection points -->
                    <circle id="circPt1" cx="240" cy="35" r="5" fill="#f43f5e" />
                    <text id="circLbl1" x="240" y="25" text-anchor="middle" fill="#f43f5e" class="text-xs font-bold">C₁ (Top Triangle)</text>
                    <circle id="circPt2" cx="240" cy="185" r="5" fill="#f43f5e" />
                    <text id="circLbl2" x="240" y="200" text-anchor="middle" fill="#f43f5e" class="text-xs font-bold">C₂ (Mirror Triangle)</text>

                    <!-- Triangle connectors -->
                    <line id="triTop1" x1="160" y1="110" x2="240" y2="35" stroke="#06b6d4" stroke-width="2" />
                    <line id="triTop2" x1="340" y1="110" x2="240" y2="35" stroke="#10b981" stroke-width="2" />
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2 bg-slate-800 rounded border border-slate-700">
                    <div class="flex justify-between mb-1">
                        <span class="text-cyan-400">Radius $r_A$ (Compass from A)</span>
                        <span id="txtRadA" class="font-mono text-cyan-300">110 px</span>
                    </div>
                    <input id="slideRadA" type="range" min="40" max="160" value="110" oninput="updateCircleIntersections()" class="w-full accent-cyan-500">
                </div>
                <div class="p-2 bg-slate-800 rounded border border-slate-700">
                    <div class="flex justify-between mb-1">
                        <span class="text-emerald-400">Radius $r_B$ (Compass from B)</span>
                        <span id="txtRadB" class="font-mono text-emerald-300">100 px</span>
                    </div>
                    <input id="slideRadB" type="range" min="40" max="160" value="100" oninput="updateCircleIntersections()" class="w-full accent-emerald-500">
                </div>
            </div>
        </div>
    """,

    # 5. SSS Construction
    "sim-sss-construction": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">SSS Interactive Drafting Board</span>
                <div class="flex gap-1.5">
                    <button onclick="setSSSPreset('scalene')" class="px-2 py-0.5 text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 rounded">Scalene (7, 5, 4)</button>
                    <button onclick="setSSSPreset('isosceles')" class="px-2 py-0.5 text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 rounded">Isosceles (6, 6, 4)</button>
                    <button onclick="setSSSPreset('equilateral')" class="px-2 py-0.5 text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 rounded">Equilateral (5, 5, 5)</button>
                </div>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="sssSvg" viewBox="0 0 500 220" class="w-full h-full">
                    <!-- Base line -->
                    <line id="sssBase" x1="120" y1="180" x2="380" y2="180" stroke="#f59e0b" stroke-width="3" />
                    <text id="sssBaseText" x="250" y="202" text-anchor="middle" fill="#f59e0b" class="text-xs font-mono">c = 7 cm</text>
                    
                    <!-- Arc A and Arc B -->
                    <path id="sssArcA" d="" fill="none" stroke="#06b6d4" stroke-width="2" stroke-dasharray="4 3" />
                    <path id="sssArcB" d="" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4 3" />
                    
                    <!-- Apex -->
                    <circle id="sssApex" cx="210" cy="55" r="5" fill="#f43f5e" />
                    <text x="210" y="42" text-anchor="middle" fill="#f43f5e" class="text-xs font-bold">C</text>

                    <!-- Triangle sides -->
                    <line id="sssSideB" x1="120" y1="180" x2="210" y2="55" stroke="#06b6d4" stroke-width="2.5" />
                    <line id="sssSideA" x1="380" y1="180" x2="210" y2="55" stroke="#10b981" stroke-width="2.5" />
                    
                    <!-- Vertices -->
                    <circle cx="120" cy="180" r="5" fill="#f59e0b" />
                    <text x="105" y="185" fill="#f59e0b" class="text-xs font-bold">A</text>
                    <circle cx="380" cy="180" r="5" fill="#f59e0b" />
                    <text x="390" y="185" fill="#f59e0b" class="text-xs font-bold">B</text>

                    <!-- Dimension labels -->
                    <text id="sssLblB" x="150" y="110" fill="#06b6d4" class="text-xs font-mono">b = 5 cm</text>
                    <text id="sssLblA" x="310" y="110" fill="#10b981" class="text-xs font-mono">a = 4 cm</text>
                </svg>
            </div>
            <div class="mt-2 flex items-center justify-between text-xs text-slate-300">
                <span id="sssDescription">Scalene Triangle: All three sides are distinct (7 cm, 5 cm, 4 cm).</span>
                <button onclick="animateSSSConstruction()" class="px-3 py-1 bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 rounded font-semibold border border-amber-500/40">Re-play Drafting Arcs</button>
            </div>
        </div>
    """,

    # 6. SAS Construction
    "sim-sas-construction": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">SAS Included Angle Workbench</span>
                <span class="text-xs font-mono text-cyan-300" id="sasCalcSide">Side a (locked) = 5.2 cm</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="sasSvg" viewBox="0 0 500 220" class="w-full h-full">
                    <!-- Base c -->
                    <line x1="120" y1="180" x2="360" y2="180" stroke="#f59e0b" stroke-width="3" />
                    <text x="240" y="200" text-anchor="middle" fill="#f59e0b" class="text-xs font-mono">Base c = 6 cm</text>

                    <!-- Included angle arc -->
                    <path id="sasAngleArc" d="M 160 180 A 40 40 0 0 0 148 152" fill="rgba(244, 63, 94, 0.25)" stroke="#f43f5e" stroke-width="2" />
                    <text id="sasAngleText" x="175" y="165" fill="#f43f5e" class="text-xs font-bold">50°</text>

                    <!-- Ray AX and arm b -->
                    <line id="sasRay" x1="120" y1="180" x2="270" y2="40" stroke="#64748b" stroke-dasharray="4 4" stroke-width="1.5" />
                    <line id="sasSideB" x1="120" y1="180" x2="230" y2="70" stroke="#06b6d4" stroke-width="3" />
                    <text id="sasLblB" x="160" y="115" fill="#06b6d4" class="text-xs font-mono">b = 5 cm</text>

                    <!-- Third side a (frozen) -->
                    <line id="sasSideA" x1="230" y1="70" x2="360" y2="180" stroke="#10b981" stroke-width="3" />
                    <text id="sasLblA" x="310" y="115" fill="#10b981" class="text-xs font-mono">a = ?</text>

                    <!-- Vertices -->
                    <circle cx="120" cy="180" r="5" fill="#f43f5e" />
                    <text x="105" y="185" fill="#f43f5e" class="text-xs font-bold">A</text>
                    <circle cx="360" cy="180" r="5" fill="#f59e0b" />
                    <text x="370" y="185" fill="#f59e0b" class="text-xs font-bold">B</text>
                    <circle id="sasVertexC" cx="230" cy="70" r="5" fill="#06b6d4" />
                    <text id="sasTextC" x="230" y="55" text-anchor="middle" fill="#06b6d4" class="text-xs font-bold">C</text>
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2 bg-slate-800 rounded border border-slate-700">
                    <div class="flex justify-between mb-1">
                        <span class="text-rose-400 font-bold">Included Angle $\angle A$</span>
                        <span id="sasValAngle" class="font-mono text-rose-300">50°</span>
                    </div>
                    <input id="sasSliderAngle" type="range" min="25" max="130" value="50" oninput="updateSAS()" class="w-full accent-rose-500">
                </div>
                <div class="p-2 bg-slate-800 rounded border border-slate-700">
                    <div class="flex justify-between mb-1">
                        <span class="text-cyan-400 font-bold">Side $b$ Length</span>
                        <span id="sasValB" class="font-mono text-cyan-300">5.0 cm</span>
                    </div>
                    <input id="sasSliderB" type="range" min="30" max="75" value="50" oninput="updateSAS()" class="w-full accent-cyan-500">
                </div>
            </div>
        </div>
    """,

    # 7. ASA Construction
    "sim-asa-construction": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">ASA Ray Convergence Simulator</span>
                <span id="asaStatusBadge" class="px-2 py-0.5 text-xs font-bold bg-emerald-500/20 text-emerald-300 rounded border border-emerald-500/40">Convergent ($\angle B + \angle C < 180^\circ$)</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="asaSvg" viewBox="0 0 500 220" class="w-full h-full">
                    <!-- Base BC -->
                    <line x1="120" y1="180" x2="380" y2="180" stroke="#f59e0b" stroke-width="3" />
                    <circle cx="120" cy="180" r="5" fill="#f59e0b" />
                    <text x="105" y="185" fill="#f59e0b" class="text-xs font-bold">B</text>
                    <circle cx="380" cy="180" r="5" fill="#f59e0b" />
                    <text x="390" y="185" fill="#f59e0b" class="text-xs font-bold">C</text>
                    <text x="250" y="200" text-anchor="middle" fill="#f59e0b" class="text-xs font-mono">Base a = 6.5 cm</text>

                    <!-- Ray BX and Ray CY -->
                    <line id="asaRayB" x1="120" y1="180" x2="260" y2="40" stroke="#06b6d4" stroke-width="2.5" />
                    <line id="asaRayC" x1="380" y1="180" x2="260" y2="40" stroke="#10b981" stroke-width="2.5" />

                    <!-- Apex A -->
                    <circle id="asaApex" cx="260" cy="40" r="6" fill="#f43f5e" />
                    <text id="asaApexLbl" x="260" y="25" text-anchor="middle" fill="#f43f5e" class="text-xs font-bold">A (Intersection)</text>

                    <!-- Angle arcs -->
                    <path id="asaArcB" d="" fill="rgba(6, 182, 212, 0.25)" stroke="#06b6d4" stroke-width="2" />
                    <text id="asaLblB" x="155" y="165" fill="#06b6d4" class="text-xs font-bold">60°</text>
                    <path id="asaArcC" d="" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="2" />
                    <text id="asaLblC" x="335" y="165" fill="#10b981" class="text-xs font-bold">50°</text>
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-2 gap-2 text-xs">
                <div class="p-2 bg-slate-800 rounded border border-slate-700">
                    <div class="flex justify-between mb-1">
                        <span class="text-cyan-400 font-bold">Angle B</span>
                        <span id="asaValB" class="font-mono text-cyan-300">60°</span>
                    </div>
                    <input id="asaSlideB" type="range" min="20" max="110" value="60" oninput="updateASA()" class="w-full accent-cyan-500">
                </div>
                <div class="p-2 bg-slate-800 rounded border border-slate-700">
                    <div class="flex justify-between mb-1">
                        <span class="text-emerald-400 font-bold">Angle C</span>
                        <span id="asaValC" class="font-mono text-emerald-300">50°</span>
                    </div>
                    <input id="asaSlideC" type="range" min="20" max="110" value="50" oninput="updateASA()" class="w-full accent-emerald-500">
                </div>
            </div>
            <div class="mt-2 p-2 bg-slate-800/80 rounded border border-slate-700 flex justify-between text-xs font-mono">
                <span id="asaAngleSum" class="text-slate-300">Sum: 60° + 50° = 110° (< 180°)</span>
                <span id="asaAngleA" class="text-amber-300 font-bold">Calculated Angle A: 70°</span>
            </div>
        </div>
    """,

    # 8. Angle Sum Proof
    "sim-angle-sum-proof": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Angle Sum Property Proof Engine</span>
                <div class="flex gap-2">
                    <button onclick="setAngleSumMode('parallel')" id="btnSumParallel" class="px-2.5 py-1 text-xs font-semibold bg-amber-500/20 text-amber-300 rounded border border-amber-500/40">Parallel Line Proof</button>
                    <button onclick="setAngleSumMode('tearoff')" id="btnSumTearoff" class="px-2.5 py-1 text-xs font-semibold bg-slate-800 text-slate-300 rounded border border-slate-600">Paper Tear-Off Demo</button>
                </div>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="angleSumSvg" viewBox="0 0 500 220" class="w-full h-full">
                    <!-- Auxiliary Parallel Line through A -->
                    <line id="parallelLine" x1="40" y1="50" x2="460" y2="50" stroke="#f43f5e" stroke-dasharray="5 3" stroke-width="2" />
                    <text id="lblLineXY" x="430" y="42" fill="#f43f5e" class="text-xs font-mono">Line XY || BC</text>

                    <!-- Triangle ABC -->
                    <polygon id="aspPoly" points="100,180 400,180 250,50" fill="rgba(245, 158, 11, 0.12)" stroke="#f59e0b" stroke-width="2.5" />
                    
                    <!-- Base BC -->
                    <line x1="100" y1="180" x2="400" y2="180" stroke="#f59e0b" stroke-width="3" />
                    <circle cx="100" cy="180" r="5" fill="#10b981" />
                    <text x="85" y="195" fill="#10b981" class="text-xs font-bold">B (∠2)</text>
                    <circle cx="400" cy="180" r="5" fill="#06b6d4" />
                    <text x="405" y="195" fill="#06b6d4" class="text-xs font-bold">C (∠3)</text>
                    <circle cx="250" cy="50" r="5" fill="#f59e0b" />
                    <text x="250" y="35" text-anchor="middle" fill="#f59e0b" class="text-xs font-bold">A (∠1)</text>

                    <!-- Alternate Angles along line XY -->
                    <g id="alternateAngles">
                        <text x="180" y="45" fill="#10b981" class="text-xs font-bold font-mono">∠2 = ∠B</text>
                        <text x="240" y="75" fill="#f59e0b" class="text-xs font-bold font-mono">∠1</text>
                        <text x="295" y="45" fill="#06b6d4" class="text-xs font-bold font-mono">∠3 = ∠C</text>
                    </g>
                    
                    <!-- Straight Line Semi-circle -->
                    <path id="straightAngleArc" d="M 180 50 A 70 70 0 0 1 320 50" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3" />
                    <text x="250" y="20" text-anchor="middle" fill="#f43f5e" class="text-xs font-bold">Straight Angle = 180°</text>
                </svg>
            </div>
            <div id="aspExplanation" class="mt-2 p-2 bg-slate-800 rounded border border-slate-700 text-xs text-slate-300">
                Line $XY$ is parallel to base $BC$. Alternate interior angles give $\angle XAB = \angle 2$ and $\angle YAC = \angle 3$. Together on straight line $XY$: $\angle 2 + \angle 1 + \angle 3 = 180^\circ$.
            </div>
        </div>
    """,

    # 9. Exterior Angle Theorem
    "sim-exterior-angle": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Dynamic Exterior Angle Inspector</span>
                <span class="text-xs font-mono font-bold text-amber-300" id="extTheoremEq">∠ACD (120°) = ∠A (70°) + ∠B (50°)</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="extSvg" viewBox="0 0 500 220" class="w-full h-full">
                    <!-- Base line extended to D -->
                    <line x1="80" y1="170" x2="450" y2="170" stroke="#f59e0b" stroke-width="2.5" />
                    <circle cx="80" cy="170" r="4" fill="#10b981" />
                    <text x="65" y="175" fill="#10b981" class="text-xs font-bold">B</text>
                    <circle cx="320" cy="170" r="5" fill="#f43f5e" />
                    <text x="315" y="190" fill="#f43f5e" class="text-xs font-bold">C</text>
                    <text x="440" y="160" fill="#f59e0b" class="text-xs font-bold">D (Extension)</text>

                    <!-- Triangle sides -->
                    <line id="extSideAB" x1="80" y1="170" x2="220" y2="50" stroke="#10b981" stroke-width="2.5" />
                    <line id="extSideAC" x1="220" y1="50" x2="320" y2="170" stroke="#06b6d4" stroke-width="2.5" />
                    
                    <!-- Vertex A -->
                    <circle id="extVertexA" cx="220" cy="50" r="6" fill="#06b6d4" class="cursor-pointer" />
                    <text id="extLblA" x="220" y="38" text-anchor="middle" fill="#06b6d4" class="text-xs font-bold">A (70°)</text>

                    <!-- Interior angle B -->
                    <text id="extLblB" x="110" y="155" fill="#10b981" class="text-xs font-bold">50°</text>

                    <!-- Exterior angle arc at C -->
                    <path id="extAngleArc" d="M 360 170 A 40 40 0 0 0 300 146" fill="rgba(244, 63, 94, 0.3)" stroke="#f43f5e" stroke-width="2.5" />
                    <text id="extLblExt" x="350" y="145" fill="#f43f5e" class="text-xs font-bold font-mono">120° (Ext)</text>

                    <!-- Interior adjacent angle at C -->
                    <text id="extLblAdj" x="270" y="165" fill="#94a3b8" class="text-xs">60°</text>
                </svg>
            </div>
            <div class="mt-2 flex items-center justify-between text-xs text-slate-300">
                <span>Drag Apex A to test all angles:</span>
                <input id="extSliderA" type="range" min="140" max="300" value="220" oninput="updateExtAngle(this.value)" class="w-56 accent-amber-500">
            </div>
        </div>
    """,

    # 10. Altitude Definition
    "sim-altitude-definition": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Perpendicular Altitude & Area</span>
                <span id="altStats" class="text-xs font-mono text-cyan-300">Base b = 280 px | Height h = 130 px</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="altDefSvg" viewBox="0 0 500 220" class="w-full h-full">
                    <!-- Base BC -->
                    <line x1="110" y1="180" x2="390" y2="180" stroke="#f59e0b" stroke-width="3" />
                    <circle cx="110" cy="180" r="5" fill="#f59e0b" />
                    <text x="95" y="195" fill="#f59e0b" class="text-xs font-bold">B</text>
                    <circle cx="390" cy="180" r="5" fill="#f59e0b" />
                    <text x="395" y="195" fill="#f59e0b" class="text-xs font-bold">C</text>

                    <!-- Sides AB, AC -->
                    <line id="altDefAB" x1="110" y1="180" x2="240" y2="50" stroke="#38bdf8" stroke-width="2.5" />
                    <line id="altDefAC" x1="390" y1="180" x2="240" y2="50" stroke="#38bdf8" stroke-width="2.5" />

                    <!-- Apex A -->
                    <circle id="altDefApex" cx="240" cy="50" r="6" fill="#38bdf8" />
                    <text id="altDefApexLbl" x="240" y="35" text-anchor="middle" fill="#38bdf8" class="text-xs font-bold">A (Apex)</text>

                    <!-- Altitude Line (Red) -->
                    <line id="altDefLine" x1="240" y1="50" x2="240" y2="180" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="4 3" />
                    <circle id="altDefFoot" cx="240" cy="180" r="4" fill="#f43f5e" />
                    <text id="altDefFootLbl" x="240" y="200" text-anchor="middle" fill="#f43f5e" class="text-xs font-bold font-mono">D (Foot: 90°)</text>

                    <!-- Right angle corner symbol -->
                    <path id="altDefRtSymbol" d="M 240 165 L 255 165 L 255 180" fill="none" stroke="#f43f5e" stroke-width="1.5" />
                </svg>
            </div>
            <div class="mt-2 flex items-center justify-between text-xs text-slate-300">
                <span>Shift Vertex A Horizontally:</span>
                <input id="altDefSlider" type="range" min="130" max="370" value="240" oninput="updateAltDef(this.value)" class="w-56 accent-cyan-500">
            </div>
        </div>
    """,

    # 11. Drafting Altitudes with Set Square
    "sim-set-square-drafting": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Virtual Ruler & Sliding Set Square</span>
                <button onclick="snapAndDropAltitude()" class="px-2.5 py-1 text-xs font-semibold bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 rounded border border-amber-500/40">Drop Altitude</button>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="setSquareSvg" viewBox="0 0 500 220" class="w-full h-full">
                    <!-- Fixed Triangle ABC -->
                    <polygon points="120,150 380,150 250,40" fill="rgba(245, 158, 11, 0.1)" stroke="#f59e0b" stroke-width="2" />
                    <circle cx="120" cy="150" r="4" fill="#f59e0b" />
                    <text x="105" y="155" fill="#f59e0b" class="text-xs font-bold">B</text>
                    <circle cx="380" cy="150" r="4" fill="#f59e0b" />
                    <text x="390" y="155" fill="#f59e0b" class="text-xs font-bold">C</text>
                    <circle cx="250" cy="40" r="5" fill="#38bdf8" />
                    <text x="250" y="28" text-anchor="middle" fill="#38bdf8" class="text-xs font-bold">A (Target Apex)</text>

                    <!-- Stationary Ruler along Base BC -->
                    <rect x="60" y="150" width="380" height="28" fill="#334155" stroke="#64748b" stroke-width="1.5" rx="3" />
                    <text x="250" y="168" text-anchor="middle" fill="#94a3b8" class="text-xs font-mono font-bold tracking-widest">RULER GUIDE TRACK</text>

                    <!-- Dropped Altitude line (hidden until drawn) -->
                    <line id="sqAltLine" x1="250" y1="40" x2="250" y2="150" stroke="#f43f5e" stroke-width="2.5" class="opacity-0 transition-opacity duration-300" />
                    <path id="sqRtCorner" d="M 250 138 L 262 138 L 262 150" fill="none" stroke="#f43f5e" stroke-width="1.5" class="opacity-0 transition-opacity duration-300" />

                    <!-- Movable Set Square Triangle -->
                    <g id="movableSetSquare" transform="translate(160, 0)">
                        <polygon points="0,150 90,150 0,30" fill="rgba(6, 182, 212, 0.35)" stroke="#06b6d4" stroke-width="2" />
                        <path d="M 0 138 L 12 138 L 12 150" fill="none" stroke="#06b6d4" stroke-width="1.5" />
                        <text x="18" y="125" fill="#06b6d4" class="text-xs font-mono">90°</text>
                    </g>
                </svg>
            </div>
            <div class="mt-2 flex items-center justify-between text-xs text-slate-300">
                <span>Slide Set Square Along Ruler:</span>
                <input id="setSquareSlider" type="range" min="80" max="330" value="160" oninput="updateSetSquarePos(this.value)" class="w-56 accent-cyan-500">
            </div>
        </div>
    """,

    # 12. Altitudes in Special Triangles (Inside, On, Outside)
    "sim-altitude-cases": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Altitudes: Inside, On, and Outside</span>
                <div class="flex gap-1.5">
                    <button onclick="setAltCase('acute')" id="btnCaseAcute" class="px-2.5 py-1 text-xs font-semibold bg-emerald-500/20 text-emerald-300 rounded border border-emerald-500/40">1. Acute (Inside)</button>
                    <button onclick="setAltCase('right')" id="btnCaseRight" class="px-2.5 py-1 text-xs font-semibold bg-slate-800 text-slate-300 rounded border border-slate-600">2. Right (On Sides)</button>
                    <button onclick="setAltCase('obtuse')" id="btnCaseObtuse" class="px-2.5 py-1 text-xs font-semibold bg-slate-800 text-slate-300 rounded border border-slate-600">3. Obtuse (Outside)</button>
                </div>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="altCaseSvg" viewBox="0 0 500 220" class="w-full h-full">
                    <!-- Base Extension for obtuse -->
                    <line id="altCaseExt" x1="40" y1="170" x2="160" y2="170" stroke="#64748b" stroke-dasharray="4 4" stroke-width="1.5" class="opacity-0" />
                    
                    <!-- Triangle ABC -->
                    <polygon id="altCasePoly" points="140,170 380,170 240,50" fill="rgba(16, 185, 129, 0.12)" stroke="#10b981" stroke-width="2.5" />
                    
                    <!-- Altitude 1 (Red) -->
                    <line id="altCaseLine1" x1="240" y1="50" x2="240" y2="170" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4 3" />
                    <circle id="altCaseFoot1" cx="240" cy="170" r="4" fill="#f43f5e" />
                    <text id="altCaseLbl1" x="240" y="195" text-anchor="middle" fill="#f43f5e" class="text-xs font-bold font-mono">Altitude 1</text>

                    <!-- Vertices -->
                    <circle id="altCaseVA" cx="240" cy="50" r="5" fill="#38bdf8" />
                    <text id="altCaseTxtA" x="240" y="38" text-anchor="middle" fill="#38bdf8" class="text-xs font-bold">A</text>
                    <circle id="altCaseVB" cx="140" cy="170" r="5" fill="#f59e0b" />
                    <text id="altCaseTxtB" x="125" y="185" fill="#f59e0b" class="text-xs font-bold">B</text>
                    <circle id="altCaseVC" cx="380" cy="170" r="5" fill="#f59e0b" />
                    <text id="altCaseTxtC" x="390" y="185" fill="#f59e0b" class="text-xs font-bold">C</text>
                </svg>
            </div>
            <div id="altCaseDesc" class="mt-2 p-2 bg-slate-800 rounded border border-slate-700 text-xs text-slate-300">
                In an Acute Triangle, all three interior angles are $< 90^\circ$. Every altitude lands strictly INSIDE the boundary.
            </div>
        </div>
    """,

    # 13. Orthocenter Concurrency
    "sim-orthocenter-concurrency": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Orthocenter ($H$) Concurrency Tracker</span>
                <span id="orthoPositionBadge" class="px-2 py-0.5 text-xs font-bold bg-cyan-500/20 text-cyan-300 rounded border border-cyan-500/40">Orthocenter Inside (Acute)</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="orthoSvg" viewBox="0 0 500 220" class="w-full h-full">
                    <!-- Triangle ABC -->
                    <polygon id="orthoPoly" points="120,170 380,170 230,50" fill="rgba(56, 189, 248, 0.1)" stroke="#38bdf8" stroke-width="2.5" />
                    
                    <!-- 3 Altitudes -->
                    <line id="orthoAltA" x1="230" y1="50" x2="230" y2="170" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3 3" />
                    <line id="orthoAltB" x1="120" y1="170" x2="280" y2="85" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3 3" />
                    <line id="orthoAltC" x1="380" y1="170" x2="190" y2="90" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3 3" />

                    <!-- Orthocenter H -->
                    <circle id="orthoPtH" cx="230" cy="118" r="6" fill="#f59e0b" stroke="#fff" stroke-width="2" />
                    <text id="orthoLblH" x="245" y="122" fill="#f59e0b" class="text-xs font-bold font-mono">Orthocenter H</text>

                    <!-- Vertices -->
                    <circle id="orthoVA" cx="230" cy="50" r="5" fill="#38bdf8" />
                    <text x="230" y="38" text-anchor="middle" fill="#38bdf8" class="text-xs font-bold">A</text>
                    <circle cx="120" cy="170" r="5" fill="#10b981" />
                    <text x="105" y="175" fill="#10b981" class="text-xs font-bold">B</text>
                    <circle cx="380" cy="170" r="5" fill="#10b981" />
                    <text x="390" y="175" fill="#10b981" class="text-xs font-bold">C</text>
                </svg>
            </div>
            <div class="mt-2 flex items-center justify-between text-xs text-slate-300">
                <span>Morph Vertex A (Acute &harr; Right &harr; Obtuse):</span>
                <input id="orthoSliderA" type="range" min="70" max="370" value="230" oninput="updateOrthocenter(this.value)" class="w-56 accent-amber-500">
            </div>
        </div>
    """,

    # 14. Classification by Sides
    "sim-triangle-by-sides": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Side Taxonomy & Symmetry Axes</span>
                <div class="flex gap-1.5">
                    <button onclick="setSideFamily('equi')" id="btnFamEqui" class="px-2 py-0.5 text-xs bg-cyan-500/20 text-cyan-300 rounded border border-cyan-500/40">Equilateral (3 equal)</button>
                    <button onclick="setSideFamily('iso')" id="btnFamIso" class="px-2 py-0.5 text-xs bg-slate-800 text-slate-300 rounded border border-slate-600">Isosceles (2 equal)</button>
                    <button onclick="setSideFamily('scall')" id="btnFamScal" class="px-2 py-0.5 text-xs bg-slate-800 text-slate-300 rounded border border-slate-600">Scalene (0 equal)</button>
                </div>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="sideFamSvg" viewBox="0 0 500 220" class="w-full h-full">
                    <!-- Symmetry Axes (Dashed Pink) -->
                    <g id="sideSymAxes">
                        <line x1="250" y1="20" x2="250" y2="190" stroke="#f43f5e" stroke-dasharray="4 3" stroke-width="1.5" />
                        <line x1="130" y1="200" x2="350" y2="70" stroke="#f43f5e" stroke-dasharray="4 3" stroke-width="1.5" />
                        <line x1="370" y1="200" x2="150" y2="70" stroke="#f43f5e" stroke-dasharray="4 3" stroke-width="1.5" />
                    </g>
                    <!-- Polygon -->
                    <polygon id="sideFamPoly" points="160,180 340,180 250,24.1" fill="rgba(6, 182, 212, 0.15)" stroke="#06b6d4" stroke-width="3" />
                    <!-- Length labels -->
                    <text id="sideLbl1" x="250" y="200" text-anchor="middle" fill="#06b6d4" class="text-xs font-mono font-bold">18 cm</text>
                    <text id="sideLbl2" x="180" y="95" fill="#06b6d4" class="text-xs font-mono font-bold">18 cm</text>
                    <text id="sideLbl3" x="310" y="95" fill="#06b6d4" class="text-xs font-mono font-bold">18 cm</text>
                </svg>
            </div>
            <div id="sideFamInfo" class="mt-2 p-2 bg-slate-800 rounded border border-slate-700 flex justify-between text-xs text-slate-300">
                <span class="text-cyan-300 font-bold">Equilateral Triangle</span>
                <span>Lines of Symmetry: <strong>3</strong> | Angles: <strong>60°, 60°, 60°</strong></span>
            </div>
        </div>
    """,

    # 15. Classification by Angles
    "sim-triangle-by-angles": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Angle Taxonomy & Hypotenuse Gauge</span>
                <span id="angClassBadge" class="px-2 py-0.5 text-xs font-bold bg-emerald-500/20 text-emerald-300 rounded border border-emerald-500/40">Acute-Angled Triangle</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
                <svg id="angClassSvg" viewBox="0 0 500 220" class="w-full h-full">
                    <!-- Triangle -->
                    <polygon id="angPoly" points="130,170 370,170 250,45" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="3" />
                    
                    <!-- Angle readout tags -->
                    <text id="angTagA" x="250" y="32" text-anchor="middle" fill="#38bdf8" class="text-xs font-bold font-mono">∠A = 60°</text>
                    <text id="angTagB" x="100" y="175" fill="#10b981" class="text-xs font-bold font-mono">∠B = 60°</text>
                    <text id="angTagC" x="380" y="175" fill="#f59e0b" class="text-xs font-bold font-mono">∠C = 60°</text>

                    <!-- Hypotenuse line highlight (active only in Right triangle) -->
                    <line id="angHypotenuse" x1="130" y1="170" x2="370" y2="45" stroke="#f43f5e" stroke-width="4" class="opacity-0 transition-opacity duration-300" />
                    <text id="angHypLbl" x="240" y="95" fill="#f43f5e" class="text-xs font-bold font-mono opacity-0">HYPOTENUSE (c)</text>
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-3 gap-2">
                <button onclick="setAngleClass('acute')" class="py-1 text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-600">Acute (60°, 60°, 60°)</button>
                <button onclick="setAngleClass('right')" class="py-1 text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-600">Right (90°, 50°, 40°)</button>
                <button onclick="setAngleClass('obtuse')" class="py-1 text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-600">Obtuse (120°, 35°, 25°)</button>
            </div>
        </div>
    """,

    # 16. Master Matrix & Sulba Sutra Heritage
    "sim-master-matrix-sulba": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">3×3 Master Matrix & Śulba Cord Knots</span>
                <span class="text-xs font-mono text-amber-300">Baudhāyana Cord Rule: $a^2 + b^2 = c^2$</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <div class="w-full flex gap-3 h-full">
                    <!-- Mini visual preview -->
                    <div class="w-1/2 h-full bg-slate-900 rounded-lg border border-slate-800 flex flex-col items-center justify-center relative p-2">
                        <svg id="sulbaSvg" viewBox="0 0 240 180" class="w-full h-full">
                            <!-- Right Triangle 3:4:5 with knotted cord -->
                            <polygon points="40,140 160,140 40,50" fill="rgba(245, 158, 11, 0.15)" stroke="#f59e0b" stroke-width="2.5" />
                            <text x="100" y="155" fill="#f59e0b" class="text-xs font-mono">4 Knots</text>
                            <text x="15" y="95" fill="#f59e0b" class="text-xs font-mono">3 Knots</text>
                            <text x="115" y="85" fill="#06b6d4" class="text-xs font-mono font-bold">5 Knots (Cord)</text>
                            <path d="M 40 125 L 55 125 L 55 140" fill="none" stroke="#f43f5e" stroke-width="1.5" />
                            <text x="60" y="135" fill="#f43f5e" class="text-xs">90°</text>
                        </svg>
                        <span id="sulbaDesc" class="text-xs text-amber-300 font-mono text-center">Triple 3:4:5 &rarr; 9 + 16 = 25 (Exact 90°)</span>
                    </div>
                    <!-- Cord triple selectors -->
                    <div class="w-1/2 flex flex-col justify-around text-xs">
                        <span class="text-slate-400 font-bold">Select Vedic Śulba Cord Triple:</span>
                        <button onclick="setSulbaTriple(3, 4, 5)" class="p-1.5 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded border border-amber-500/30 text-left">
                            <strong>3 : 4 : 5 Triple</strong> (Sacred Fire Altar)
                        </button>
                        <button onclick="setSulbaTriple(5, 12, 13)" class="p-1.5 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded border border-cyan-500/30 text-left">
                            <strong>5 : 12 : 13 Triple</strong> (Mahavedi Trapezoid)
                        </button>
                        <button onclick="setSulbaTriple(8, 15, 17)" class="p-1.5 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded border border-emerald-500/30 text-left">
                            <strong>8 : 15 : 17 Triple</strong> (Ahavaniya Altar)
                        </button>
                    </div>
                </div>
            </div>
            <div class="mt-2 text-xs text-slate-400 text-center">
                Click any triple above to observe how Indian Vedic master-builders used knotted cords to construct exact right angles!
            </div>
        </div>
    """
}

with open('.agents/class7_math_tale_of_three_intersecting_lines_sims.py', 'w') as f:
    f.write(f"SIMULATORS = {repr(sims)}\n")

print("Created .agents/class7_math_tale_of_three_intersecting_lines_sims.py successfully!")
