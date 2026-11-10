# make_c4s_ch7_sims_part1.py
# Bespoke interactive simulators 1 to 8 for Chapter 7: How Things Work

simulators_part1 = {}

# SIM 1: Spinning Objects Motion Lab
simulators_part1["sim-1"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-cyan-300">Spinning Objects Motion Lab</h4>
            </div>
            <span class="text-xs bg-cyan-500/20 text-cyan-300 px-2.5 py-1 rounded-full font-medium border border-cyan-500/30">Rotational Dynamics</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="window.setSpinObject('coin')" id="spin-obj-coin" class="spin-obj-btn active p-2.5 rounded-xl border border-cyan-500/50 bg-cyan-950/40 hover:bg-cyan-900/50 transition-all text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🪙</span>
                <span class="text-xs font-semibold">1. Round Coin</span>
            </button>
            <button onclick="window.setSpinObject('bangle')" id="spin-obj-bangle" class="spin-obj-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-center flex flex-col items-center gap-1">
                <span class="text-2xl">⭕</span>
                <span class="text-xs font-semibold">2. Glass Bangle</span>
            </button>
            <button onclick="window.setSpinObject('top')" id="spin-obj-top" class="spin-obj-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🌀</span>
                <span class="text-xs font-semibold">3. Wooden Top</span>
            </button>
            <button onclick="window.setSpinObject('eraser')" id="spin-obj-eraser" class="spin-obj-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🧽</span>
                <span class="text-xs font-semibold">4. Flat Eraser</span>
            </button>
        </div>

        <div class="relative bg-slate-950/80 rounded-xl p-4 border border-slate-800/80 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <div id="spinCanvasContainer" class="relative w-48 h-48 flex items-center justify-center">
                <!-- SVG spinning visual -->
                <svg id="spinVisualSvg" class="w-40 h-40 transition-transform duration-300" viewBox="0 0 160 160">
                    <circle cx="80" cy="80" r="70" fill="#0f172a" stroke="#38bdf8" stroke-width="4" stroke-dasharray="12 6" />
                    <circle cx="80" cy="80" r="16" fill="#0284c7" />
                    <line x1="80" y1="10" x2="80" y2="150" stroke="#bae6fd" stroke-width="3" stroke-linecap="round" />
                    <line x1="10" y1="80" x2="150" y2="80" stroke="#bae6fd" stroke-width="3" stroke-linecap="round" />
                    <circle cx="80" cy="80" r="5" fill="#f8fafc" />
                </svg>
            </div>
            <div id="spinStatusBadge" class="mt-2 text-xs font-medium text-slate-300 bg-slate-800/90 px-3 py-1 rounded-full border border-slate-700">
                Ready to spin. Select object and launch!
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 items-center">
            <div class="flex flex-col gap-1">
                <label class="text-xs text-slate-400 font-medium">Initial Spin Force</label>
                <input type="range" id="spinForceSlider" min="20" max="100" value="70" class="accent-cyan-400 cursor-pointer w-full">
            </div>
            <button onclick="window.launchSpin()" class="w-full py-2.5 px-4 bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white font-bold rounded-xl shadow-lg transition-all flex items-center justify-center gap-2 text-sm">
                <span>🔄</span> Launch Spin Test
            </button>
            <button onclick="window.stopSpin()" class="w-full py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium rounded-xl border border-slate-700 transition-all text-sm">
                ⏹ Reset
            </button>
        </div>

        <div id="spinReadout" class="p-3 bg-cyan-950/30 border border-cyan-800/40 rounded-xl text-xs text-cyan-200 flex flex-col gap-1">
            <div class="font-bold flex items-center justify-between">
                <span>Object: <span id="spinObjName">Round Coin</span></span>
                <span>Stability: <span id="spinStability">High Symmetry</span></span>
            </div>
            <p id="spinObjDesc">Coins spin smoothly on their edge when flicked with balanced torque, gradually wobbling into a ringing chatter as rotational speed decreases.</p>
        </div>
    </div>
"""

# SIM 2: Rotational Pivot Center Lab
simulators_part1["sim-2"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-amber-300">Rotational Pivot Center Lab</h4>
            </div>
            <span class="text-xs bg-amber-500/20 text-amber-300 px-2.5 py-1 rounded-full font-medium border border-amber-500/30">Axis & Center of Gravity</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div class="bg-slate-950/60 p-3 rounded-xl border border-slate-800 flex flex-col gap-2">
                <label class="text-xs font-semibold text-slate-300">1. Select Cardboard Shape:</label>
                <div class="grid grid-cols-3 gap-2">
                    <button onclick="window.setPivotShape('square')" id="shape-square" class="pivot-shape-btn active py-2 rounded-lg border border-amber-500/60 bg-amber-950/40 text-xs font-medium text-amber-200">Square</button>
                    <button onclick="window.setPivotShape('circle')" id="shape-circle" class="pivot-shape-btn py-2 rounded-lg border border-slate-700 bg-slate-800/40 text-xs font-medium text-slate-300">Circle</button>
                    <button onclick="window.setPivotShape('triangle')" id="shape-triangle" class="pivot-shape-btn py-2 rounded-lg border border-slate-700 bg-slate-800/40 text-xs font-medium text-slate-300">Triangle</button>
                </div>
            </div>

            <div class="bg-slate-950/60 p-3 rounded-xl border border-slate-800 flex flex-col gap-2">
                <label class="text-xs font-semibold text-slate-300">2. Toothpick Pivot Hole Location:</label>
                <div class="grid grid-cols-2 gap-2">
                    <button onclick="window.setPivotLocation('center')" id="pivot-center" class="pivot-loc-btn active py-2 rounded-lg border border-emerald-500/60 bg-emerald-950/40 text-xs font-medium text-emerald-200">🎯 Exact Center</button>
                    <button onclick="window.setPivotLocation('offcenter')" id="pivot-offcenter" class="pivot-loc-btn py-2 rounded-lg border border-slate-700 bg-slate-800/40 text-xs font-medium text-slate-300">⚠️ Off-Center Edge</button>
                </div>
            </div>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <div id="pivotCanvasArea" class="relative w-48 h-48 flex items-center justify-center">
                <svg id="pivotSvg" class="w-44 h-44 transition-all duration-300" viewBox="0 0 160 160">
                    <!-- Square shape by default -->
                    <rect id="pivotShapeElem" x="30" y="30" width="100" height="100" rx="8" fill="#d97706" fill-opacity="0.25" stroke="#f59e0b" stroke-width="3" />
                    <!-- Pin indicator -->
                    <circle id="pivotPinElem" cx="80" cy="80" r="7" fill="#ef4444" stroke="#ffffff" stroke-width="2" />
                    <circle cx="80" cy="80" r="2" fill="#ffffff" />
                </svg>
            </div>
            <div id="pivotOutcomeText" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-700/60">
                Centered Pivot: Symmetrical mass distribution ensures smooth, stable rotation!
            </div>
        </div>

        <div class="flex gap-2">
            <button onclick="window.testPivotSpin()" class="flex-1 py-2.5 px-4 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm">
                🔄 Spin Cardboard Spinner
            </button>
            <button onclick="window.resetPivotTest()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Reset
            </button>
        </div>
    </div>
"""

# SIM 3: Persistence of Vision & Optical Illusions
simulators_part1["sim-3"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-indigo-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-indigo-300">Persistence of Vision & Optical Illusion Lab</h4>
            </div>
            <span class="text-xs bg-indigo-500/20 text-indigo-300 px-2.5 py-1 rounded-full font-medium border border-indigo-500/30">Sensory Integration</span>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.setOpticMode('newton')" id="optic-mode-newton" class="optic-btn active py-2.5 px-3 rounded-xl border border-indigo-500/60 bg-indigo-950/40 text-xs font-semibold text-indigo-200 flex items-center justify-center gap-2">
                <span>🌈</span> Newton's 7-Color Disc
            </button>
            <button onclick="window.setOpticMode('squareblur')" id="optic-mode-squareblur" class="optic-btn py-2.5 px-3 rounded-xl border border-slate-700 bg-slate-800/40 text-xs font-semibold text-slate-300 flex items-center justify-center gap-2">
                <span>🔲</span> Square Turns Circular
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <div id="opticContainer" class="relative w-48 h-48 flex items-center justify-center">
                <!-- Newton Color Disc SVG -->
                <svg id="opticSvg" class="w-44 h-44 transition-all duration-300" viewBox="0 0 160 160">
                    <g id="newtonSectors">
                        <!-- 7 rainbow wedges -->
                        <path d="M80,80 L80,10 A70,70 0 0,1 140.6,45 Z" fill="#ef4444" />
                        <path d="M80,80 L140.6,45 A70,70 0 0,1 150,80 Z" fill="#f97316" />
                        <path d="M80,80 L150,80 A70,70 0 0,1 130,135 Z" fill="#eab308" />
                        <path d="M80,80 L130,135 A70,70 0 0,1 80,150 Z" fill="#22c55e" />
                        <path d="M80,80 L80,150 A70,70 0 0,1 30,135 Z" fill="#06b6d4" />
                        <path d="M80,80 L30,135 A70,70 0 0,1 10,80 Z" fill="#3b82f6" />
                        <path d="M80,80 L10,80 A70,70 0 0,1 80,10 Z" fill="#8b5cf6" />
                    </g>
                    <!-- Blending Overlay circle simulating retinal fusion -->
                    <circle id="opticBlendOverlay" cx="80" cy="80" r="70" fill="#f8fafc" opacity="0" />
                    <circle cx="80" cy="80" r="8" fill="#1e293b" stroke="#ffffff" stroke-width="2" />
                </svg>
            </div>
            <div id="opticFpsReadout" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700">
                Speed: 0 RPM | Eye Perception: Distinct Individual Colors
            </div>
        </div>

        <div class="flex flex-col gap-2">
            <div class="flex items-center justify-between text-xs text-slate-400">
                <span>Rotation Velocity</span>
                <span id="rpmLabel" class="font-bold text-indigo-300">0 RPM</span>
            </div>
            <input type="range" id="opticRpmSlider" min="0" max="1200" step="50" value="0" oninput="window.updateOpticSpeed(this.value)" class="w-full accent-indigo-400 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-500">
                <span>0 (Static)</span>
                <span>300 (Threshold)</span>
                <span>800+ (Full Retinal Fusion)</span>
            </div>
        </div>
    </div>
"""

# SIM 4: Traditional Indian Lattu Lab
simulators_part1["sim-4"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-orange-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-orange-300">Traditional Indian Lattu Lab</h4>
            </div>
            <span class="text-xs bg-orange-500/20 text-orange-300 px-2.5 py-1 rounded-full font-medium border border-orange-500/30">Torque & Angular Momentum</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
            <button onclick="window.setLattuStringWraps(3)" id="wrap-3" class="lattu-wrap-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-xs font-semibold text-slate-300">
                🧵 3 Wraps (Low Torque)
            </button>
            <button onclick="window.setLattuStringWraps(6)" id="wrap-6" class="lattu-wrap-btn active p-2.5 rounded-xl border border-orange-500/60 bg-orange-950/40 text-xs font-semibold text-orange-200">
                🧵 6 Wraps (Optimal)
            </button>
            <button onclick="window.setLattuStringWraps(9)" id="wrap-9" class="lattu-wrap-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-xs font-semibold text-slate-300">
                🧵 9 Wraps (Maximum)
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <div id="lattuContainer" class="relative w-48 h-48 flex items-center justify-center">
                <svg id="lattuSvg" class="w-40 h-44 transition-all duration-300" viewBox="0 0 160 180">
                    <!-- Traditional wooden lattu shape -->
                    <!-- Top knob -->
                    <circle cx="80" cy="20" r="8" fill="#d97706" />
                    <!-- Crown -->
                    <ellipse cx="80" cy="40" rx="36" ry="12" fill="#b45309" stroke="#f59e0b" stroke-width="2" />
                    <!-- Conical Body with traditional painted bands -->
                    <path d="M44,40 C44,90 75,145 80,155 C85,145 116,90 116,40 Z" fill="#d97706" stroke="#92400e" stroke-width="2" />
                    <!-- Colorful traditional bands -->
                    <path d="M52,65 Q80,75 108,65" stroke="#ef4444" stroke-width="5" fill="none" />
                    <path d="M58,85 Q80,95 102,85" stroke="#10b981" stroke-width="5" fill="none" />
                    <path d="M64,105 Q80,113 96,105" stroke="#3b82f6" stroke-width="5" fill="none" />
                    <!-- String coils indicator -->
                    <g id="lattuCoilsGroup">
                        <line x1="56" y1="95" x2="104" y2="95" stroke="#fef08a" stroke-width="3" stroke-dasharray="4 2" />
                        <line x1="60" y1="105" x2="100" y2="105" stroke="#fef08a" stroke-width="3" stroke-dasharray="4 2" />
                    </g>
                    <!-- Hardened steel pivot nail at bottom tip -->
                    <polygon points="77,155 83,155 80,172" fill="#cbd5e1" stroke="#475569" stroke-width="1.5" />
                </svg>
            </div>
            <div id="lattuStatusText" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700">
                Lattu wound with 6 string coils. Ready to release!
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.launchLattu()" class="py-2.5 px-4 bg-orange-600 hover:bg-orange-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm flex items-center justify-center gap-2">
                <span>⚡</span> Pull String & Release Lattu
            </button>
            <button onclick="window.resetLattu()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Rewind String
            </button>
        </div>
    </div>
"""

# SIM 5: Historic Charkha Pulley Ratio Lab
simulators_part1["sim-5"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-500 animate-pulse"></span>
                <h4 class="font-bold text-base text-amber-300">The Historic Charkha Mechanism Lab</h4>
            </div>
            <span class="text-xs bg-amber-500/20 text-amber-300 px-2.5 py-1 rounded-full font-medium border border-amber-500/30">Speed Ratio Multiplication</span>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <!-- Charkha SVG with Large Wheel + Belt + Small Spindle (Takli) -->
            <svg id="charkhaSvg" class="w-full max-w-md h-48" viewBox="0 0 320 160">
                <!-- Wooden Base Board -->
                <rect x="20" y="140" width="280" height="12" rx="4" fill="#78350f" />
                <rect x="60" y="80" width="12" height="60" fill="#92400e" />
                <rect x="250" y="100" width="8" height="40" fill="#92400e" />

                <!-- Connecting Cord Belt -->
                <line x1="66" y1="30" x2="254" y2="92" stroke="#fef08a" stroke-width="2" stroke-dasharray="4 2" />
                <line x1="66" y1="130" x2="254" y2="108" stroke="#fef08a" stroke-width="2" stroke-dasharray="4 2" />

                <!-- Large Drive Wheel (Radius 50) -->
                <g id="charkhaBigWheel" style="transform-origin: 66px 80px;">
                    <circle cx="66" cy="80" r="50" fill="none" stroke="#d97706" stroke-width="6" />
                    <!-- 8 wooden spokes -->
                    <line x1="66" y1="30" x2="66" y2="130" stroke="#b45309" stroke-width="3" />
                    <line x1="16" y1="80" x2="116" y2="80" stroke="#b45309" stroke-width="3" />
                    <line x1="31" y1="45" x2="101" y2="115" stroke="#b45309" stroke-width="3" />
                    <line x1="31" y1="115" x2="101" y2="45" stroke="#b45309" stroke-width="3" />
                    <circle cx="66" cy="80" r="8" fill="#451a03" />
                    <!-- Hand Crank Handle -->
                    <circle cx="66" cy="45" r="5" fill="#ef4444" stroke="#ffffff" stroke-width="1.5" />
                </g>

                <!-- Tiny Spindle / Takli (Radius 8, 20x faster) -->
                <g id="charkhaSpindle" style="transform-origin: 254px 100px;">
                    <line x1="230" y1="100" x2="295" y2="100" stroke="#e2e8f0" stroke-width="3" stroke-linecap="round" />
                    <circle cx="254" cy="100" r="8" fill="#d97706" stroke="#fbbf24" stroke-width="2" />
                </g>

                <!-- Cotton fiber being twisted into yarn -->
                <path id="yarnLine" d="M295,100 Q310,95 315,90" stroke="#f8fafc" stroke-width="2" fill="none" stroke-linecap="round" />
            </svg>

            <div class="flex items-center justify-between w-full max-w-md mt-2 text-xs font-semibold px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800">
                <span class="text-amber-300">Big Wheel: <span id="charkhaBigSpeed">0</span> RPM</span>
                <span class="text-slate-400">➡️ 20:1 Gear Ratio ➡️</span>
                <span class="text-emerald-400">Spindle: <span id="charkhaSpindleSpeed">0</span> RPM</span>
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.crankCharkha()" class="py-2.5 px-4 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm flex items-center justify-center gap-2">
                <span>🔄</span> Turn Hand Crank Handle
            </button>
            <button onclick="window.stopCharkha()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Stop Wheel
            </button>
        </div>
    </div>
"""

# SIM 6: Surface Friction & Spin Duration Lab
simulators_part1["sim-6"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-rose-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-rose-300">Surface Friction & Spin Duration Lab</h4>
            </div>
            <span class="text-xs bg-rose-500/20 text-rose-300 px-2.5 py-1 rounded-full font-medium border border-rose-500/30">Frictional Dissipation</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="window.setFrictionSurface('glass')" id="fric-glass" class="fric-btn active p-2.5 rounded-xl border border-rose-500/60 bg-rose-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">🪟</span>
                <span class="text-xs font-semibold text-rose-200">Polished Glass</span>
                <span class="text-[10px] text-slate-400">μ = 0.05</span>
            </button>
            <button onclick="window.setFrictionSurface('wood')" id="fric-wood" class="fric-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">🪵</span>
                <span class="text-xs font-semibold text-slate-300">Smooth Wood</span>
                <span class="text-[10px] text-slate-400">μ = 0.20</span>
            </button>
            <button onclick="window.setFrictionSurface('paper')" id="fric-paper" class="fric-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">📄</span>
                <span class="text-xs font-semibold text-slate-300">Paper Sheet</span>
                <span class="text-[10px] text-slate-400">μ = 0.45</span>
            </button>
            <button onclick="window.setFrictionSurface('carpet')" id="fric-carpet" class="fric-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">🧶</span>
                <span class="text-xs font-semibold text-slate-300">Rough Carpet</span>
                <span class="text-[10px] text-slate-400">μ = 0.85</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[200px] flex flex-col items-center justify-center overflow-hidden">
            <div id="fricSurfaceVisual" class="w-full max-w-sm h-36 rounded-xl border border-slate-700 flex flex-col items-center justify-center relative overflow-hidden bg-sky-950/30">
                <svg id="fricSpinSvg" class="w-24 h-24 transition-transform duration-100" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="42" fill="#e11d48" stroke="#fecdd3" stroke-width="4" stroke-dasharray="8 4" />
                    <circle cx="50" cy="50" r="10" fill="#ffffff" />
                    <line x1="50" y1="8" x2="50" y2="92" stroke="#ffffff" stroke-width="2" />
                </svg>
                <div id="fricSurfaceTexture" class="absolute bottom-0 w-full h-8 bg-sky-400/20 border-t border-sky-400/40 flex items-center justify-center text-[10px] text-sky-200">
                    Slick Smooth Glass Surface
                </div>
            </div>
            <div class="flex items-center gap-4 mt-3 text-xs font-semibold">
                <span class="text-slate-300">Time Elapsed: <span id="fricTimerText" class="text-rose-400 font-mono text-sm">0.0s</span></span>
                <span class="text-slate-300">Status: <span id="fricStatusText" class="text-emerald-400">Ready</span></span>
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.startFrictionTest()" class="py-2.5 px-4 bg-rose-600 hover:bg-rose-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm flex items-center justify-center gap-2">
                <span>⏱</span> Launch Spin & Time Test
            </button>
            <button onclick="window.resetFrictionTest()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Reset
            </button>
        </div>
    </div>
"""

# SIM 7: Floating Versus Sinking Basin
simulators_part1["sim-7"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-blue-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-blue-300">Classroom Float vs Sink Basin</h4>
            </div>
            <span class="text-xs bg-blue-500/20 text-blue-300 px-2.5 py-1 rounded-full font-medium border border-blue-500/30">Investigative Testing</span>
        </div>

        <div class="grid grid-cols-3 sm:grid-cols-6 gap-2">
            <button onclick="window.testFloatSinkItem('leaf')" id="fsi-leaf" class="fsi-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1 hover:border-blue-400">
                <span class="text-xl">🍃</span>
                <span class="text-[11px] font-semibold text-slate-200">Dry Leaf</span>
            </button>
            <button onclick="window.testFloatSinkItem('nail')" id="fsi-nail" class="fsi-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1 hover:border-blue-400">
                <span class="text-xl">🔩</span>
                <span class="text-[11px] font-semibold text-slate-200">Iron Nail</span>
            </button>
            <button onclick="window.testFloatSinkItem('bowl')" id="fsi-bowl" class="fsi-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1 hover:border-blue-400">
                <span class="text-xl">🥣</span>
                <span class="text-[11px] font-semibold text-slate-200">Steel Bowl</span>
            </button>
            <button onclick="window.testFloatSinkItem('stone')" id="fsi-stone" class="fsi-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1 hover:border-blue-400">
                <span class="text-xl">🪨</span>
                <span class="text-[11px] font-semibold text-slate-200">Pebble</span>
            </button>
            <button onclick="window.testFloatSinkItem('bottle')" id="fsi-bottle" class="fsi-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1 hover:border-blue-400">
                <span class="text-xl">🍾</span>
                <span class="text-[11px] font-semibold text-slate-200">Plastic Bottle</span>
            </button>
            <button onclick="window.testFloatSinkItem('wood')" id="fsi-wood" class="fsi-btn p-2 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1 hover:border-blue-400">
                <span class="text-xl">🪵</span>
                <span class="text-[11px] font-semibold text-slate-200">Wood Block</span>
            </button>
        </div>

        <!-- Water Tank Graphic -->
        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="waterTankSvg" class="w-full max-w-md h-48 rounded-lg" viewBox="0 0 320 180">
                <!-- Tank glass border -->
                <rect x="20" y="20" width="280" height="150" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2" />
                <!-- Water level (starts at y=60) -->
                <rect x="22" y="60" width="276" height="108" fill="#0284c7" fill-opacity="0.35" />
                <path d="M22,60 Q90,56 160,60 T300,60" stroke="#38bdf8" stroke-width="2" fill="none" />
                <text x="30" y="52" fill="#7dd3fc" font-size="10" font-weight="bold">Water Surface</text>

                <!-- Floating items zone (y=50-65) -->
                <g id="floatingItemsGroup"></g>
                <!-- Sunk items zone (y=150) -->
                <g id="sunkItemsGroup"></g>
            </svg>
            <div id="floatSinkSummary" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700">
                Click any item above to drop it into the water tank!
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.dropAllFloatSink()" class="py-2.5 px-4 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm">
                🌊 Drop All Items
            </button>
            <button onclick="window.resetFloatSinkTank()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Empty Tank
            </button>
        </div>
    </div>
"""

# SIM 8: Investigating Water Buoyancy
simulators_part1["sim-8"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-teal-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-teal-300">Water Buoyancy & Spring Balance Lab</h4>
            </div>
            <span class="text-xs bg-teal-500/20 text-teal-300 px-2.5 py-1 rounded-full font-medium border border-teal-500/30">Upward Force Measurement</span>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[240px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="buoyancySpringSvg" class="w-full max-w-md h-56" viewBox="0 0 320 220">
                <!-- Water Beaker on right -->
                <rect x="140" y="90" width="150" height="120" rx="6" fill="#0f172a" stroke="#0ea5e9" stroke-width="2" />
                <rect id="beakerWater" x="142" y="120" width="146" height="88" fill="#0284c7" fill-opacity="0.35" />
                <text x="150" y="112" fill="#38bdf8" font-size="10" font-weight="bold">Water Beaker</text>

                <!-- Retort Stand on left -->
                <rect x="30" y="200" width="80" height="12" fill="#475569" />
                <rect x="50" y="20" width="8" height="180" fill="#64748b" />
                <rect x="50" y="20" width="130" height="6" fill="#64748b" />

                <!-- Spring Balance Hanging Assembly -->
                <g id="springBalanceAssembly" style="transition: transform 0.6s ease-in-out;">
                    <!-- Hook -->
                    <circle cx="170" cy="26" r="4" fill="none" stroke="#e2e8f0" stroke-width="2" />
                    <!-- Balance body -->
                    <rect x="160" y="32" width="20" height="50" rx="3" fill="#334155" stroke="#94a3b8" stroke-width="1.5" />
                    <line x1="170" y1="36" x2="170" y2="76" stroke="#f8fafc" stroke-width="2" stroke-dasharray="3 2" />
                    <!-- Indicator needle -->
                    <line id="balanceNeedle" x1="162" y1="65" x2="178" y2="65" stroke="#ef4444" stroke-width="2.5" />
                    <!-- Hanging String & Stone -->
                    <line id="balanceString" x1="170" y1="82" x2="170" y2="130" stroke="#f8fafc" stroke-width="1.5" />
                    <circle id="balanceStone" cx="170" cy="142" r="14" fill="#64748b" stroke="#94a3b8" stroke-width="2" />

                    <!-- Upward Buoyancy Vector Arrow (shows when submerged) -->
                    <g id="buoyancyVector" opacity="0">
                        <line x1="170" y1="162" x2="170" y2="135" stroke="#10b981" stroke-width="3" marker-end="url(#arrow)" />
                        <text x="182" y="150" fill="#34d399" font-size="10" font-weight="bold">Upthrust (180g)</text>
                    </g>
                </g>
            </svg>

            <div class="grid grid-cols-2 gap-3 w-full max-w-md mt-2 text-xs font-semibold">
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-center">
                    <span class="text-slate-400 block">Air Weight:</span>
                    <span class="text-amber-300 text-sm font-bold">500 grams</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-center">
                    <span class="text-slate-400 block">Apparent Water Weight:</span>
                    <span id="apparentWeightVal" class="text-teal-300 text-sm font-bold">500 grams</span>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.submergeStone()" id="submergeBtn" class="py-2.5 px-4 bg-teal-600 hover:bg-teal-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm flex items-center justify-center gap-2">
                <span>⬇️</span> Submerge Stone in Water
            </button>
            <button onclick="window.liftStone()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Lift Out of Water
            </button>
        </div>
    </div>
"""

