import sys

def generate_simulators():
    simulators = [
        # Sim 1: The Point (Precision Locator & Coordinates)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Point Locator Canvas</span>
                <span id="pointCoordinates" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Point P at (200, 140)</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center cursor-crosshair" id="pointCanvasContainer">
                <svg id="pointSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <defs>
                        <pattern id="gridPattern" width="20" height="20" patternUnits="userSpaceOnUse">
                            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1e293b" stroke-width="0.75" />
                        </pattern>
                    </defs>
                    <rect width="400" height="240" fill="url(#gridPattern)" />
                    <!-- Origin Crosshairs -->
                    <line id="crossH" x1="0" y1="140" x2="400" y2="140" stroke="#0ea5e9" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>
                    <line id="crossV" x1="200" y1="0" x2="200" y2="240" stroke="#0ea5e9" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>
                    <circle id="pointCircle" cx="200" cy="140" r="5" fill="#f59e0b" stroke="#ffffff" stroke-width="2" class="transition-all duration-75 shadow-lg shadow-amber-500/50"/>
                    <text id="pointLabel" x="212" y="135" fill="#fde047" font-size="14" font-weight="bold" font-family="monospace">Point P</text>
                    <text x="10" y="225" fill="#94a3b8" font-size="10">Click anywhere to move Point P (Zero Dimension, Exact Location)</text>
                </svg>
            </div>
            <div class="grid grid-cols-4 gap-2 pt-2 border-t border-slate-800 text-center">
                <button onclick="setSimPoint(100, 60, 'P')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded text-xs font-mono font-bold transition">Point P</button>
                <button onclick="setSimPoint(300, 70, 'Q')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded text-xs font-mono font-bold transition">Point Q</button>
                <button onclick="setSimPoint(150, 190, 'Z')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded text-xs font-mono font-bold transition">Point Z</button>
                <button onclick="setSimPoint(280, 180, 'T')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-violet-300 rounded text-xs font-mono font-bold transition">Point T</button>
            </div>
        </div>
        """,

        # Sim 2: Line Segment (Shortest Distance & Ruler)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Line Segment Measurer</span>
                <span id="segmentLengthBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Length AB = 6.0 cm</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="segmentSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <line x1="50" y1="120" x2="350" y2="120" stroke="#334155" stroke-width="1" stroke-dasharray="4,4"/>
                    <!-- Curved comparison path -->
                    <path id="curvedPath" d="M 80 120 Q 200 40 320 120" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3" opacity="0.6"/>
                    <text x="175" y="65" fill="#f43f5e" font-size="10">Curved Path (Longer!)</text>
                    <!-- Straight Line Segment -->
                    <line id="segmentLine" x1="80" y1="120" x2="320" y2="120" stroke="#10b981" stroke-width="5" stroke-linecap="round"/>
                    <!-- Endpoints -->
                    <circle id="segPtA" cx="80" cy="120" r="7" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
                    <text id="segTextA" x="72" y="145" fill="#38bdf8" font-size="13" font-weight="bold" font-family="monospace">A</text>
                    <circle id="segPtB" cx="320" cy="120" r="7" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
                    <text id="segTextB" x="315" y="145" fill="#38bdf8" font-size="13" font-weight="bold" font-family="monospace">B</text>
                    <!-- Ruler indicator bar -->
                    <rect x="80" y="155" width="240" height="20" fill="#1e293b" rx="3" stroke="#475569" stroke-width="1"/>
                    <text x="160" y="169" fill="#94a3b8" font-size="10">Ruler: 2 fixed ends AB</text>
                </svg>
            </div>
            <div class="space-y-2 pt-2 border-t border-slate-800">
                <div class="flex items-center justify-between text-xs text-slate-300">
                    <span>Adjust Segment Length:</span>
                    <span id="segSliderVal" class="font-mono text-cyan-300 font-bold">240 px (6.0 cm)</span>
                </div>
                <input type="range" id="segmentLengthSlider" min="100" max="300" value="240" step="10" oninput="updateSegmentSim(this.value)" class="w-full accent-emerald-500 cursor-pointer">
            </div>
        </div>
        """,

        # Sim 3: The Line (Endless Arrows & Slope)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Line Infinity Lab</span>
                <span class="font-mono text-rose-300 bg-rose-950/60 px-2 py-0.5 rounded border border-rose-800/40">Line l (No Endpoints)</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="lineSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <defs>
                        <marker id="arrowL" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 0 L 10 5 L 0 10 z" fill="#f43f5e"/>
                        </marker>
                        <marker id="arrowR" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto">
                            <path d="M 0 0 L 10 5 L 0 10 z" fill="#f43f5e"/>
                        </marker>
                    </defs>
                    <!-- Extended Line with double arrowheads -->
                    <line id="infiniteLine" x1="20" y1="120" x2="380" y2="120" stroke="#f43f5e" stroke-width="4" marker-start="url(#arrowL)" marker-end="url(#arrowR)"/>
                    <!-- Determined Points A and B on line -->
                    <circle cx="130" cy="120" r="6" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
                    <text x="123" y="145" fill="#38bdf8" font-size="12" font-weight="bold" font-family="monospace">Point A</text>
                    <circle cx="270" cy="120" r="6" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
                    <text x="263" y="145" fill="#38bdf8" font-size="12" font-weight="bold" font-family="monospace">Point B</text>
                    <text id="lineLabelTxt" x="355" y="105" fill="#f43f5e" font-size="13" font-weight="bold" font-family="monospace">Line l</text>
                    <!-- Infinity badges -->
                    <text x="30" y="105" fill="#94a3b8" font-size="10">← Extends forever</text>
                    <text x="270" y="105" fill="#94a3b8" font-size="10">Extends forever →</text>
                </svg>
            </div>
            <div class="grid grid-cols-3 gap-2 pt-2 border-t border-slate-800 text-center">
                <button onclick="rotateSimLine(0)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded text-xs font-bold transition">Horizontal</button>
                <button onclick="rotateSimLine(-25)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded text-xs font-bold transition">Slanted (+25°)</button>
                <button onclick="rotateSimLine(90)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded text-xs font-bold transition">Vertical</button>
            </div>
        </div>
        """,

        # Sim 4: The Ray (Torch / Initial Point & Direction)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Ray Beam Simulator</span>
                <span id="rayLabelBadge" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">Ray AP (Start at A)</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="raySvg" class="w-full h-full" viewBox="0 0 400 240">
                    <defs>
                        <radialGradient id="torchGlow" cx="20%" cy="50%" r="80%">
                            <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.5"/>
                            <stop offset="100%" stop-color="#f59e0b" stop-opacity="0"/>
                        </radialGradient>
                        <marker id="rayArrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto">
                            <path d="M 0 0 L 10 5 L 0 10 z" fill="#f59e0b"/>
                        </marker>
                    </defs>
                    <!-- Torch Light Glow Cone -->
                    <polygon id="torchCone" points="80,120 380,50 380,190" fill="url(#torchGlow)"/>
                    <!-- The Ray -->
                    <line id="simRayLine" x1="80" y1="120" x2="380" y2="120" stroke="#f59e0b" stroke-width="4" marker-end="url(#rayArrow)"/>
                    <!-- Initial Point A -->
                    <circle id="rayOriginPt" cx="80" cy="120" r="7" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
                    <text id="rayOriginTxt" x="55" y="145" fill="#f87171" font-size="12" font-weight="bold" font-family="monospace">A (Start)</text>
                    <!-- Direction point P -->
                    <circle id="rayDirPt" cx="240" cy="120" r="5" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
                    <text id="rayDirTxt" x="235" y="145" fill="#38bdf8" font-size="12" font-weight="bold" font-family="monospace">P</text>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-800 text-center">
                <button onclick="setRayDirection('right')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded text-xs font-bold transition">Ray AP (Points Right →)</button>
                <button onclick="setRayDirection('left')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded text-xs font-bold transition">Ray PA (Points Left ←)</button>
            </div>
        </div>
        """,

        # Sim 5: Geometric Primitives Interactive Sieve
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Primitives Comparison Sieve</span>
                <span id="sieveSelected" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Showing: All 4 Primitives</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center p-2">
                <svg class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Point -->
                    <g id="gPoint" class="transition-opacity duration-200">
                        <circle cx="80" cy="60" r="6" fill="#f59e0b" stroke="#fff" stroke-width="2"/>
                        <text x="100" y="65" fill="#fde047" font-size="12" font-weight="bold">Point P: 0 Ends, 0D (Location)</text>
                    </g>
                    <!-- Line Segment -->
                    <g id="gSegment" class="transition-opacity duration-200">
                        <line x1="60" y1="110" x2="220" y2="110" stroke="#10b981" stroke-width="4" stroke-linecap="round"/>
                        <circle cx="60" cy="110" r="5" fill="#0284c7" stroke="#fff" stroke-width="1.5"/>
                        <circle cx="220" cy="110" r="5" fill="#0284c7" stroke="#fff" stroke-width="1.5"/>
                        <text x="235" y="115" fill="#34d399" font-size="12" font-weight="bold">Segment AB: 2 Ends (Measurable)</text>
                    </g>
                    <!-- Line -->
                    <g id="gLine" class="transition-opacity duration-200">
                        <line x1="40" y1="160" x2="220" y2="160" stroke="#f43f5e" stroke-width="3" marker-start="url(#arrowL)" marker-end="url(#arrowR)"/>
                        <text x="235" y="165" fill="#fb7185" font-size="12" font-weight="bold">Line l: 0 Ends (Infinite both ways)</text>
                    </g>
                    <!-- Ray -->
                    <g id="gRay" class="transition-opacity duration-200">
                        <line x1="60" y1="210" x2="220" y2="210" stroke="#a855f7" stroke-width="3" marker-end="url(#rayArrow)"/>
                        <circle cx="60" cy="210" r="5" fill="#ef4444" stroke="#fff" stroke-width="1.5"/>
                        <text x="235" y="215" fill="#c084fc" font-size="12" font-weight="bold">Ray AP: 1 End (Endless one way)</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-4 gap-1.5 pt-2 border-t border-slate-800 text-center">
                <button onclick="highlightPrimitive('all')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded text-xs font-bold">All</button>
                <button onclick="highlightPrimitive('seg')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded text-xs font-bold">Segment</button>
                <button onclick="highlightPrimitive('line')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded text-xs font-bold">Line</button>
                <button onclick="highlightPrimitive('ray')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-violet-300 rounded text-xs font-bold">Ray</button>
            </div>
        </div>
        """,

        # Sim 6: Angle Formation & Naming (Vertex in Center)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Angle & Vertex Explorer</span>
                <span id="angleNameBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">∠DBE or ∠EBD (Vertex B)</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="angleSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Interior Shading -->
                    <path id="angleInterior" d="M 120 180 L 320 180 A 100 100 0 0 0 250 80 Z" fill="#0284c7" fill-opacity="0.2"/>
                    <!-- Base Arm BD -->
                    <line x1="120" y1="180" x2="330" y2="180" stroke="#38bdf8" stroke-width="4" marker-end="url(#rayArrow)"/>
                    <circle cx="280" cy="180" r="5" fill="#38bdf8"/>
                    <text x="275" y="205" fill="#38bdf8" font-size="12" font-weight="bold">D</text>
                    <!-- Rotating Arm BE -->
                    <line id="angleArm2" x1="120" y1="180" x2="270" y2="70" stroke="#f59e0b" stroke-width="4" marker-end="url(#rayArrow)"/>
                    <circle id="ptE" cx="250" cy="85" r="5" fill="#f59e0b"/>
                    <text id="txtE" x="255" y="75" fill="#f59e0b" font-size="12" font-weight="bold">E</text>
                    <!-- Vertex B -->
                    <circle cx="120" cy="180" r="7" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
                    <text x="95" y="195" fill="#f87171" font-size="14" font-weight="bold">B (Vertex)</text>
                    <!-- Angle Arc -->
                    <path id="angleArc" d="M 170 180 A 50 50 0 0 0 152 143" fill="none" stroke="#facc15" stroke-width="2.5"/>
                    <text id="angleDegreesTxt" x="180" y="160" fill="#fde047" font-size="13" font-weight="bold">45°</text>
                </svg>
            </div>
            <div class="space-y-2 pt-2 border-t border-slate-800">
                <div class="flex items-center justify-between text-xs text-slate-300">
                    <span>Rotate Arm BE:</span>
                    <span id="angleSliderVal" class="font-mono text-amber-300 font-bold">45°</span>
                </div>
                <input type="range" id="angleRotateSlider" min="15" max="165" value="45" step="5" oninput="updateAngleSim(this.value)" class="w-full accent-amber-500 cursor-pointer">
            </div>
        </div>
        """,

        # Sim 7: Rotation vs Arm Length (Invariant Size)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Arm Length Invariance Lab</span>
                <span class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Angle Measure = 40° (Fixed)</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="invarianceSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Base Arm -->
                    <line id="invBaseLine" x1="100" y1="180" x2="260" y2="180" stroke="#38bdf8" stroke-width="4"/>
                    <!-- Rotated Arm at 40° -->
                    <line id="invRotLine" x1="100" y1="180" x2="222" y2="77" stroke="#f59e0b" stroke-width="4"/>
                    <!-- Vertex -->
                    <circle cx="100" cy="180" r="6" fill="#ef4444" stroke="#fff" stroke-width="2"/>
                    <!-- Fixed Arc -->
                    <path d="M 150 180 A 50 50 0 0 0 138 147" fill="none" stroke="#fde047" stroke-width="2.5"/>
                    <text x="160" y="165" fill="#fde047" font-size="13" font-weight="bold">40°</text>
                    <text x="100" y="220" fill="#94a3b8" font-size="11">Notice: Extending the arms does NOT change the 40° opening!</text>
                </svg>
            </div>
            <div class="space-y-2 pt-2 border-t border-slate-800">
                <div class="flex items-center justify-between text-xs text-slate-300">
                    <span>Change Drawn Arm Length:</span>
                    <span id="armLengthTxt" class="font-mono text-cyan-300 font-bold">Medium (160 px)</span>
                </div>
                <input type="range" id="armLengthSlider" min="90" max="230" value="160" step="10" oninput="updateArmLengthSim(this.value)" class="w-full accent-cyan-500 cursor-pointer">
            </div>
        </div>
        """,

        # Sim 8: Superimposition (Trace & Overlay)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Superimposition Overlay Lab</span>
                <span id="superResultBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Status: Separate Angles</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="superSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Target Angle DEF (55°) -->
                    <g id="targetAngle">
                        <line x1="220" y1="180" x2="360" y2="180" stroke="#0284c7" stroke-width="4"/>
                        <line x1="220" y1="180" x2="300" y2="65" stroke="#0284c7" stroke-width="4"/>
                        <circle cx="220" cy="180" r="6" fill="#0284c7"/>
                        <text x="210" y="205" fill="#38bdf8" font-size="12" font-bold>E (∠DEF = 55°)</text>
                    </g>
                    <!-- Movable Tracing Angle ABC (35°) -->
                    <g id="movableAngle" transform="translate(0, 0)" class="transition-transform duration-700">
                        <line x1="60" y1="180" x2="180" y2="180" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4,2"/>
                        <line x1="60" y1="180" x2="158" y2="111" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4,2"/>
                        <circle cx="60" cy="180" r="5" fill="#f59e0b"/>
                        <text x="50" y="205" fill="#fbbf24" font-size="12" font-bold>B (∠ABC = 35°)</text>
                    </g>
                    <text id="superVerdict" x="120" y="40" fill="#fde047" font-size="12" font-weight="bold" opacity="0">Arm BA falls inside ∠DEF → ∠ABC &lt; ∠DEF!</text>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-800 text-center">
                <button onclick="superimposeAngles(true)" class="px-2 py-1 bg-amber-600 hover:bg-amber-500 text-slate-900 font-bold rounded text-xs transition">Superimpose Tracing</button>
                <button onclick="superimposeAngles(false)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-xs font-bold transition">Reset Positions</button>
            </div>
        </div>
        """,

        # Sim 9: Circular Arc Template (Equal Radius Comparison)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Arc Template Comparison</span>
                <span class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Equal Radius R = 50px</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Angle 1: 30° -->
                    <g transform="translate(30, 0)">
                        <line x1="70" y1="180" x2="160" y2="180" stroke="#64748b" stroke-width="3"/>
                        <line x1="70" y1="180" x2="148" y2="135" stroke="#64748b" stroke-width="3"/>
                        <circle cx="70" cy="180" r="5" fill="#ef4444"/>
                        <!-- Arc of R=50 -->
                        <path d="M 120 180 A 50 50 0 0 0 113 155" fill="none" stroke="#f59e0b" stroke-width="4"/>
                        <text x="50" y="205" fill="#fde047" font-size="11">Angle 1: Arc = 26 px</text>
                    </g>
                    <!-- Angle 2: 60° -->
                    <g transform="translate(200, 0)">
                        <line x1="70" y1="180" x2="160" y2="180" stroke="#64748b" stroke-width="3"/>
                        <line x1="70" y1="180" x2="115" y2="102" stroke="#64748b" stroke-width="3"/>
                        <circle cx="70" cy="180" r="5" fill="#ef4444"/>
                        <!-- Arc of R=50 -->
                        <path d="M 120 180 A 50 50 0 0 0 95 137" fill="none" stroke="#10b981" stroke-width="4"/>
                        <text x="50" y="205" fill="#34d399" font-size="11">Angle 2: Arc = 52 px</text>
                    </g>
                    <text x="90" y="50" fill="#e2e8f0" font-size="12" font-weight="bold">Longer Arc (52px > 26px) → Angle 2 is Twice as Large!</text>
                </svg>
            </div>
            <div class="p-2 bg-slate-900/60 rounded text-center text-xs text-slate-300 border border-slate-800">
                Formula: Arc Length = Radius × Turn Angle. When Radius is identical, Arc directly measures Angle!
            </div>
        </div>
        """,

        # Sim 10: Slit-Passing Activity (Straw Rotator vs V-Slit)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Slit-Passing Straw Lab</span>
                <span id="slitPassStatus" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Status: Fits Through!</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="slitSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Fixed 40° Cardboard Slit -->
                    <polygon points="120,0 280,0 200,120" fill="#334155" opacity="0.6"/>
                    <line x1="120" y1="0" x2="200" y2="120" stroke="#facc15" stroke-width="3"/>
                    <line x1="280" y1="0" x2="200" y2="120" stroke="#facc15" stroke-width="3"/>
                    <text x="180" y="30" fill="#fde047" font-size="11" font-weight="bold">40° Slit</text>
                    <!-- Movable Straws -->
                    <g id="strawGroup" transform="translate(0, 0)">
                        <line id="strawLeft" x1="200" y1="180" x2="160" y2="60" stroke="#ef4444" stroke-width="6" stroke-linecap="round"/>
                        <line id="strawRight" x1="200" y1="180" x2="240" y2="60" stroke="#3b82f6" stroke-width="6" stroke-linecap="round"/>
                        <circle cx="200" cy="180" r="7" fill="#fbbf24" stroke="#fff" stroke-width="2"/>
                    </g>
                    <text id="strawAngleTxt" x="165" y="215" fill="#38bdf8" font-size="12" font-weight="bold">Straw Opening: 35°</text>
                </svg>
            </div>
            <div class="space-y-2 pt-2 border-t border-slate-800">
                <div class="flex items-center justify-between text-xs text-slate-300">
                    <span>Adjust Straw Opening Angle:</span>
                    <span id="strawAngleVal" class="font-mono text-amber-300 font-bold">35° (Passes)</span>
                </div>
                <input type="range" id="strawSlider" min="20" max="65" value="35" step="5" oninput="updateSlitSim(this.value)" class="w-full accent-amber-500 cursor-pointer">
            </div>
        </div>
        """,

        # Sim 11: Straight & Right Angle (Bisector)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Straight Angle Bisector</span>
                <span id="bisectBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Two Right Angles: 90° + 90°</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Straight Line (180°) -->
                    <line x1="50" y1="160" x2="350" y2="160" stroke="#f59e0b" stroke-width="4"/>
                    <!-- Vertex O -->
                    <circle cx="200" cy="160" r="6" fill="#ef4444" stroke="#fff" stroke-width="2"/>
                    <text x="195" y="185" fill="#f87171" font-size="12" font-bold>O</text>
                    <text x="45" y="185" fill="#fbbf24" font-size="12" font-bold>A</text>
                    <text x="345" y="185" fill="#fbbf24" font-size="12" font-bold>B</text>
                    <!-- Perpendicular Bisector Line (90°) -->
                    <line id="bisectRay" x1="200" y1="160" x2="200" y2="40" stroke="#06b6d4" stroke-width="4" stroke-dasharray="0" marker-end="url(#rayArrow)"/>
                    <text x="210" y="55" fill="#22d3ee" font-size="12" font-bold>C</text>
                    <!-- Square Right Angle Symbol -->
                    <rect x="200" y="140" width="20" height="20" fill="none" stroke="#22d3ee" stroke-width="2"/>
                    <rect x="180" y="140" width="20" height="20" fill="none" stroke="#22d3ee" stroke-width="2"/>
                    <text x="130" y="125" fill="#22d3ee" font-size="12" font-bold>90°</text>
                    <text x="235" y="125" fill="#22d3ee" font-size="12" font-bold>90°</text>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-800 text-center">
                <button onclick="toggleBisector('straight')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded text-xs font-bold transition">View Straight (180°)</button>
                <button onclick="toggleBisector('right')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded text-xs font-bold transition">View 2 Rights (90° ⊥ 90°)</button>
            </div>
        </div>
        """,

        # Sim 12: 360° Circle & Divisibility Wheel
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">360° Divisibility Wheel</span>
                <span id="divWheelBadge" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">Fractions of 360°</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="wheelSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <circle cx="200" cy="120" r="90" fill="#0f172a" stroke="#334155" stroke-width="2"/>
                    <!-- Interactive Slices will be dynamically injected or rotated -->
                    <g id="wheelSlicesGroup"></g>
                    <circle cx="200" cy="120" r="4" fill="#f59e0b"/>
                </svg>
            </div>
            <div class="grid grid-cols-4 gap-1.5 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setWheelDivision(2)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold font-mono">1/2 (180°)</button>
                <button onclick="setWheelDivision(3)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold font-mono">1/3 (120°)</button>
                <button onclick="setWheelDivision(4)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold font-mono">1/4 (90°)</button>
                <button onclick="setWheelDivision(6)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-violet-300 rounded font-bold font-mono">1/6 (60°)</button>
            </div>
        </div>
        """,

        # Sim 13: Protractor Dual-Scale Simulator
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Dual-Scale Protractor Lab</span>
                <span id="protractorReadout" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Inner: 50° | Outer: 130°</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="protSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Protractor Body -->
                    <path d="M 60 190 A 140 140 0 0 1 340 190 Z" fill="#0284c7" fill-opacity="0.15" stroke="#0284c7" stroke-width="2"/>
                    <line x1="60" y1="190" x2="340" y2="190" stroke="#0284c7" stroke-width="2"/>
                    <!-- Center mark -->
                    <circle cx="200" cy="190" r="4" fill="#ef4444"/>
                    <line x1="200" y1="180" x2="200" y2="200" stroke="#ef4444" stroke-width="1.5"/>
                    <!-- Base Ray pointing right (0° on inner) -->
                    <line x1="200" y1="190" x2="340" y2="190" stroke="#38bdf8" stroke-width="3"/>
                    <!-- Target Measurable Arm -->
                    <line id="protArm" x1="200" y1="190" x2="290" y2="82" stroke="#f59e0b" stroke-width="3" marker-end="url(#rayArrow)"/>
                    <text x="315" y="185" fill="#38bdf8" font-size="10" font-mono>0° Inner</text>
                    <text x="65" y="185" fill="#f43f5e" font-size="10" font-mono>180° Inner</text>
                </svg>
            </div>
            <div class="space-y-2 pt-2 border-t border-slate-800">
                <div class="flex items-center justify-between text-xs text-slate-300">
                    <span>Rotate Angle Ray:</span>
                    <span id="protAngleVal" class="font-mono text-amber-300 font-bold">50°</span>
                </div>
                <input type="range" id="protSlider" min="10" max="170" value="50" step="5" oninput="updateProtractorSim(this.value)" class="w-full accent-amber-500 cursor-pointer">
            </div>
        </div>
        """,

        # Sim 14: Step-by-Step Angle Drafter
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Angle Construction Studio</span>
                <span id="draftStepBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Step 1: Reference Ray</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="draftSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Step 1: Base Ray IT -->
                    <g id="draftStep1">
                        <line x1="100" y1="180" x2="300" y2="180" stroke="#38bdf8" stroke-width="4" marker-end="url(#rayArrow)"/>
                        <circle cx="100" cy="180" r="6" fill="#ef4444"/>
                        <text x="85" y="200" fill="#f87171" font-size="12" font-bold>I</text>
                        <text x="290" y="200" fill="#38bdf8" font-size="12" font-bold>T</text>
                    </g>
                    <!-- Step 2: Ghost Protractor Overlay -->
                    <path id="draftStep2" d="M 20 180 A 120 120 0 0 1 260 180 Z" fill="#0284c7" fill-opacity="0.1" stroke="#0284c7" stroke-width="1.5" stroke-dasharray="3,3" opacity="0"/>
                    <!-- Step 3: Pencil Mark at 30° -->
                    <g id="draftStep3" opacity="0">
                        <circle cx="204" cy="120" r="4" fill="#f59e0b"/>
                        <text x="215" y="115" fill="#fde047" font-size="12" font-bold>N (30° Mark)</text>
                    </g>
                    <!-- Step 4: Finished Ray IN -->
                    <g id="draftStep4" opacity="0">
                        <line x1="100" y1="180" x2="240" y2="99" stroke="#10b981" stroke-width="4" marker-end="url(#rayArrow)"/>
                        <text x="140" y="165" fill="#34d399" font-size="12" font-bold>30°</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-4 gap-1.5 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setDraftStep(1)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Step 1</button>
                <button onclick="setDraftStep(2)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Step 2</button>
                <button onclick="setDraftStep(3)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Step 3</button>
                <button onclick="setDraftStep(4)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold">Step 4</button>
            </div>
        </div>
        """,

        # Sim 15: Acute, Right & Obtuse Classifier
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Angle Family Classifier</span>
                <span id="classTypeBadge" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">Acute Angle (45°)</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="classSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Base Ray -->
                    <line x1="180" y1="180" x2="340" y2="180" stroke="#38bdf8" stroke-width="4" marker-end="url(#rayArrow)"/>
                    <!-- 90° Benchmark Ghost Line -->
                    <line x1="180" y1="180" x2="180" y2="40" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>
                    <text x="185" y="55" fill="#64748b" font-size="10">90° Right Angle Benchmark</text>
                    <!-- Movable Classified Arm -->
                    <line id="classArm" x1="180" y1="180" x2="265" y2="95" stroke="#f59e0b" stroke-width="4" marker-end="url(#rayArrow)"/>
                    <circle cx="180" cy="180" r="6" fill="#ef4444"/>
                    <!-- Arc -->
                    <path id="classArc" d="M 230 180 A 50 50 0 0 0 215 145" fill="none" stroke="#fde047" stroke-width="3"/>
                    <text id="classAngleText" x="235" y="160" fill="#fde047" font-size="14" font-weight="bold">45°</text>
                </svg>
            </div>
            <div class="space-y-2 pt-2 border-t border-slate-800">
                <div class="flex items-center justify-between text-xs text-slate-300">
                    <span>Angle Value:</span>
                    <span id="classAngleSliderVal" class="font-mono text-cyan-300 font-bold">45°</span>
                </div>
                <input type="range" id="classifierSlider" min="10" max="170" value="45" step="5" oninput="updateClassifierSim(this.value)" class="w-full accent-cyan-500 cursor-pointer">
            </div>
        </div>
        """,

        # Sim 16: Straight & Reflex Angle Visualiser
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Reflex & Full Turn Lab</span>
                <span id="reflexTypeBadge" class="font-mono text-violet-300 bg-violet-950/60 px-2 py-0.5 rounded border border-violet-800/40">Reflex Angle: 240°</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="reflexSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Base Ray pointing right -->
                    <line x1="200" y1="120" x2="330" y2="120" stroke="#38bdf8" stroke-width="4" marker-end="url(#rayArrow)"/>
                    <!-- Rotating Reflex Arm -->
                    <line id="reflexArm" x1="200" y1="120" x2="135" y2="232" stroke="#a855f7" stroke-width="4" marker-end="url(#rayArrow)"/>
                    <circle cx="200" cy="120" r="6" fill="#ef4444"/>
                    <!-- Reflex Arc sweeping outer angle -->
                    <path id="reflexArc" d="M 250 120 A 50 50 0 1 1 168 177" fill="none" stroke="#c084fc" stroke-width="3.5"/>
                    <text id="reflexDegreeText" x="210" y="80" fill="#e9d5ff" font-size="14" font-weight="bold">240°</text>
                    <text id="innerComplementText" x="145" y="150" fill="#94a3b8" font-size="10">Inner: 120°</text>
                </svg>
            </div>
            <div class="space-y-2 pt-2 border-t border-slate-800">
                <div class="flex items-center justify-between text-xs text-slate-300">
                    <span>Rotation Angle:</span>
                    <span id="reflexSliderVal" class="font-mono text-violet-300 font-bold">240° (Reflex)</span>
                </div>
                <input type="range" id="reflexSlider" min="180" max="360" value="240" step="5" oninput="updateReflexSim(this.value)" class="w-full accent-violet-500 cursor-pointer">
            </div>
        </div>
        """
    ]

    code = f'''"""NCERT Class 6 Mathematics Chapter 2: Lines and Angles Simulators."""

SIMULATORS = {simulators}
'''

    # Strict check for zero raw LaTeX
    forbidden = ["\\text", "\\frac", "\\circ", "\\angle", "\\overleftrightarrow", "\\overline", "\\vec", "\\approx", "\\dots", "\\sqrt"]
    for word in forbidden:
        if word in code:
            raise ValueError(f"CRITICAL ERROR: Found raw LaTeX '{word}' in simulators module!")

    with open(".agents/class6_math_lines_angles_sims.py", "w", encoding="utf-8") as f:
        f.write(code)

    print("Successfully generated .agents/class6_math_lines_angles_sims.py with 16 bespoke simulators.")
    print("VERIFIED PASS: Zero raw LaTeX in simulators module!")

if __name__ == "__main__":
    generate_simulators()
