# -*- coding: utf-8 -*-
"""
Interactive Simulators for Slides 1 to 8
Class 3 Mathematics Chapter 2: Toy Joy
Bespoke SVG/HTML5 interactive laboratory widgets.
"""

simulators_part1 = {
    # Simulator 1: Box and Bottle Crafting
    "sim_box_bottle_craft": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Recycled Container Craft Workshop</h3>
                <p class="text-xs text-slate-400">Select a discarded household container and craft animal features to discover its 3D solid shape.</p>
            </div>
            <div class="flex items-center gap-1.5 flex-wrap">
                <button onclick="selectCraftItem('carton')" id="btnCraftCarton" class="px-2.5 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition shadow">
                    📦 Biscuit Carton
                </button>
                <button onclick="selectCraftItem('can')" id="btnCraftCan" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition">
                    🥫 Tin Can
                </button>
                <button onclick="selectCraftItem('party_hat')" id="btnCraftHat" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition">
                    🎉 Party Hat
                </button>
                <button onclick="selectCraftItem('cube_box')" id="btnCraftCube" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition">
                    🎲 Chalk Box
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Craft Stage SVG -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px] flex items-center justify-center">
                <svg id="craftSvgCanvas" viewBox="0 0 460 220" class="w-full h-auto max-h-[220px]">
                    <!-- Craft Table -->
                    <rect x="20" y="180" width="420" height="25" rx="4" fill="#334155" stroke="#475569" stroke-width="2"/>
                    <line x1="60" y1="205" x2="60" y2="220" stroke="#1e293b" stroke-width="8"/>
                    <line x1="400" y1="205" x2="400" y2="220" stroke="#1e293b" stroke-width="8"/>

                    <!-- Main Dynamic Shape Display -->
                    <g id="craftDisplayGroup">
                        <!-- Populated dynamically by JS -->
                    </g>
                </svg>
            </div>

            <!-- Craft Details & Animal Decorator -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs text-slate-400 font-bold">Mathematical Shape:</span>
                    <span id="craftShapeName" class="text-xs px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 font-bold">Rectangular Cuboid</span>
                </div>
                <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 text-xs space-y-1">
                    <div class="text-slate-300 font-semibold" id="craftAnimalTitle">🐶 Puppy Face Box</div>
                    <p class="text-slate-400" id="craftShapeDesc">A rectangular biscuit carton decorated with floppy felt ears, round button eyes, and a whiskered snout.</p>
                </div>

                <div class="space-y-1.5">
                    <span class="text-[11px] text-slate-400 font-medium">Add Animal Features:</span>
                    <div class="grid grid-cols-2 gap-2">
                        <button onclick="toggleAnimalFeature('ears')" id="btnFeatureEars" class="px-2 py-1.5 rounded-lg bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 text-[11px] font-semibold text-center">
                            🐾 Ears: ON
                        </button>
                        <button onclick="toggleAnimalFeature('face')" id="btnFeatureFace" class="px-2 py-1.5 rounded-lg bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 text-[11px] font-semibold text-center">
                            👀 Eyes & Nose: ON
                        </button>
                    </div>
                </div>

                <div class="pt-1 text-[11px] text-slate-400 border-t border-slate-800/80 flex items-center justify-between">
                    <span>Base 3D Form:</span>
                    <span id="craftFormBadge" class="text-amber-400 font-mono font-bold">Cuboid</span>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 2: Anatomy of 3D
    "sim_cube_anatomy": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Interactive 3D Cube Anatomy Explorer</h3>
                <p class="text-xs text-slate-400">Click feature buttons to illuminate faces, edges, and vertices on the isometric cube.</p>
            </div>
            <div class="flex items-center gap-1.5">
                <button onclick="highlightCubePart('faces')" id="btnAnatomyFaces" class="px-2.5 py-1.5 rounded-xl bg-emerald-600 text-white font-bold text-xs transition shadow">
                    🟩 Faces (6)
                </button>
                <button onclick="highlightCubePart('edges')" id="btnAnatomyEdges" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition">
                    📏 Edges (12)
                </button>
                <button onclick="highlightCubePart('vertices')" id="btnAnatomyVertices" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition">
                    🟡 Corners (8)
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Isometric Cube SVG Canvas -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[230px] flex items-center justify-center">
                <svg id="cubeAnatomySvg" viewBox="0 0 460 220" class="w-full h-auto max-h-[220px]">
                    <!-- Isometric Grid / Ground -->
                    <ellipse cx="230" cy="195" rx="140" ry="20" fill="#0f172a" opacity="0.8"/>

                    <!-- Isometric 3D Cube Elements -->
                    <!-- Top Face -->
                    <polygon id="cubeFaceTop" points="230,35 320,80 230,125 140,80" fill="#059669" stroke="#10b981" stroke-width="2.5" opacity="0.85"/>
                    <!-- Front-Left Face -->
                    <polygon id="cubeFaceLeft" points="140,80 230,125 230,200 140,155" fill="#047857" stroke="#10b981" stroke-width="2.5" opacity="0.85"/>
                    <!-- Front-Right Face -->
                    <polygon id="cubeFaceRight" points="230,125 320,80 320,155 230,200" fill="#065f46" stroke="#10b981" stroke-width="2.5" opacity="0.85"/>

                    <!-- 12 Edges (Overlaid line segments) -->
                    <g id="cubeEdgesGroup" stroke="#38bdf8" stroke-width="5" stroke-linecap="round" opacity="0.1">
                        <!-- Top 4 -->
                        <line x1="230" y1="35" x2="320" y2="80"/>
                        <line x1="320" y1="80" x2="230" y2="125"/>
                        <line x1="230" y1="125" x2="140" y2="80"/>
                        <line x1="140" y1="80" x2="230" y2="35"/>
                        <!-- Vertical 3 visible -->
                        <line x1="140" y1="80" x2="140" y2="155"/>
                        <line x1="230" y1="125" x2="230" y2="200"/>
                        <line x1="320" y1="80" x2="320" y2="155"/>
                        <!-- Bottom 2 visible -->
                        <line x1="140" y1="155" x2="230" y2="200"/>
                        <line x1="230" y1="200" x2="320" y2="155"/>
                        <!-- Rear 3 hidden dashed edges -->
                        <line x1="230" y1="35" x2="230" y2="110" stroke-dasharray="4,4" stroke-width="3" opacity="0.7"/>
                        <line x1="140" y1="155" x2="230" y2="110" stroke-dasharray="4,4" stroke-width="3" opacity="0.7"/>
                        <line x1="320" y1="155" x2="230" y2="110" stroke-dasharray="4,4" stroke-width="3" opacity="0.7"/>
                    </g>

                    <!-- 8 Corners / Vertices -->
                    <g id="cubeVerticesGroup" fill="#fbbf24" stroke="#78350f" stroke-width="2" opacity="0.1">
                        <circle cx="230" cy="35" r="7"/>
                        <circle cx="320" cy="80" r="7"/>
                        <circle cx="230" cy="125" r="7"/>
                        <circle cx="140" cy="80" r="7"/>
                        <circle cx="140" cy="155" r="7"/>
                        <circle cx="230" cy="200" r="7"/>
                        <circle cx="320" cy="155" r="7"/>
                        <circle cx="230" cy="110" r="6" fill="#f59e0b" stroke-dasharray="2,2"/> <!-- Hidden rear vertex -->
                    </g>
                </svg>
            </div>

            <!-- Structural Property Breakdown -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="text-xs font-bold text-amber-400" id="anatomyDetailHeader">Faces Selected</div>
                <p class="text-xs text-slate-300" id="anatomyDetailText">
                    A cube has <span class="text-emerald-400 font-bold">6 flat square faces</span>. 3 are directly visible from this angle, while 3 rest on the opposite sides.
                </p>

                <div class="grid grid-cols-3 gap-2 text-center pt-2 border-t border-slate-800">
                    <div class="p-2 bg-slate-900 rounded-lg border border-emerald-900/40">
                        <div class="text-[10px] text-slate-400">Faces</div>
                        <div class="text-base font-black text-emerald-400">6</div>
                    </div>
                    <div class="p-2 bg-slate-900 rounded-lg border border-sky-900/40">
                        <div class="text-[10px] text-slate-400">Edges</div>
                        <div class="text-base font-black text-sky-400">12</div>
                    </div>
                    <div class="p-2 bg-slate-900 rounded-lg border border-amber-900/40">
                        <div class="text-[10px] text-slate-400">Corners</div>
                        <div class="text-base font-black text-amber-400">8</div>
                    </div>
                </div>

                <div class="p-2.5 bg-slate-900/80 rounded-lg border border-slate-800 text-[11px] text-slate-400">
                    💡 <span class="text-slate-200 font-semibold">Rule:</span> When edges intersect, they meet at sharp points called corners or vertices.
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 3: Rocket Shape Assembly
    "sim_rocket_assembly": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Space Rocket Geometric Assembly Dock</h3>
                <p class="text-xs text-slate-400">Assemble a spacecraft by clicking modular 3D blocks in vertical sequence from base to tip.</p>
            </div>
            <div class="flex items-center gap-1.5">
                <button onclick="resetRocketAssembly()" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition">
                    🔄 Disassemble
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Rocket Launch Silo SVG -->
            <div class="md:col-span-7 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[240px] flex items-center justify-center">
                <svg id="rocketSvgCanvas" viewBox="0 0 360 240" class="w-full h-auto max-h-[240px]">
                    <!-- Launch Pad Grid -->
                    <line x1="40" y1="210" x2="320" y2="210" stroke="#475569" stroke-width="4"/>
                    <line x1="80" y1="210" x2="70" y2="235" stroke="#334155" stroke-width="4"/>
                    <line x1="280" y1="210" x2="290" y2="235" stroke="#334155" stroke-width="4"/>

                    <!-- Stars in background -->
                    <circle cx="60" cy="40" r="1.5" fill="#fef08a" opacity="0.6"/>
                    <circle cx="300" cy="50" r="1.5" fill="#fef08a" opacity="0.6"/>
                    <circle cx="90" cy="110" r="1" fill="#fef08a" opacity="0.5"/>
                    <circle cx="280" cy="130" r="1.2" fill="#fef08a" opacity="0.5"/>

                    <!-- Rocket Components (Toggled by JS) -->
                    <!-- Tier 1: Launch Base Cuboid -->
                    <g id="rocketTierCuboid" opacity="0.2">
                        <rect x="130" y="170" width="100" height="40" rx="4" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
                        <text x="180" y="195" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Cuboid Launch Base</text>
                    </g>
                    <!-- Tier 2: Booster Cube -->
                    <g id="rocketTierCube" opacity="0.2">
                        <rect x="150" y="125" width="60" height="45" rx="3" fill="#3b82f6" stroke="#60a5fa" stroke-width="2"/>
                        <text x="180" y="152" fill="#eff6ff" font-size="9" font-weight="bold" text-anchor="middle">Cube Engine</text>
                    </g>
                    <!-- Tier 3: Fuselage Cylinder -->
                    <g id="rocketTierCylinder" opacity="0.2">
                        <rect x="155" y="70" width="50" height="55" rx="2" fill="#ec4899" stroke="#f472b6" stroke-width="2"/>
                        <ellipse cx="180" cy="70" rx="25" ry="8" fill="#db2777" stroke="#f472b6" stroke-width="1.5"/>
                        <text x="180" y="102" fill="#fff" font-size="9" font-weight="bold" text-anchor="middle">Cylinder Body</text>
                    </g>
                    <!-- Tier 4: Top Cone -->
                    <g id="rocketTierCone" opacity="0.2">
                        <polygon points="180,20 155,70 205,70" fill="#eab308" stroke="#facc15" stroke-width="2"/>
                        <text x="180" y="52" fill="#713f12" font-size="9" font-weight="bold" text-anchor="middle">Cone</text>
                    </g>
                </svg>
            </div>

            <!-- Assembly Controls & Parts Tally -->
            <div class="md:col-span-5 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="text-xs font-bold text-slate-300">Click to Install Components:</div>

                <div class="space-y-1.5">
                    <button onclick="toggleRocketPart('cuboid')" id="btnPartCuboid" class="w-full px-3 py-2 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-left text-xs flex items-center justify-between transition">
                        <span>1. 📦 Cuboid Base (Bottom)</span>
                        <span id="badgePartCuboid" class="text-[10px] px-1.5 py-0.5 rounded bg-slate-800 text-slate-400">Pending</span>
                    </button>
                    <button onclick="toggleRocketPart('cube')" id="btnPartCube" class="w-full px-3 py-2 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-left text-xs flex items-center justify-between transition">
                        <span>2. 🟦 Cube Engine (Tier 2)</span>
                        <span id="badgePartCube" class="text-[10px] px-1.5 py-0.5 rounded bg-slate-800 text-slate-400">Pending</span>
                    </button>
                    <button onclick="toggleRocketPart('cylinder')" id="btnPartCylinder" class="w-full px-3 py-2 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-left text-xs flex items-center justify-between transition">
                        <span>3. 🛢 Cylinder Body (Tier 3)</span>
                        <span id="badgePartCylinder" class="text-[10px] px-1.5 py-0.5 rounded bg-slate-800 text-slate-400">Pending</span>
                    </button>
                    <button onclick="toggleRocketPart('cone')" id="btnPartCone" class="w-full px-3 py-2 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-left text-xs flex items-center justify-between transition">
                        <span>4. 🔺 Cone Nose Tip (Top)</span>
                        <span id="badgePartCone" class="text-[10px] px-1.5 py-0.5 rounded bg-slate-800 text-slate-400">Pending</span>
                    </button>
                </div>

                <div class="p-2.5 bg-slate-900 rounded-lg border border-slate-800 text-xs flex items-center justify-between">
                    <span class="text-slate-400">Total Installed:</span>
                    <span id="rocketInstalledCount" class="font-bold text-amber-400 font-mono text-sm">0 / 4 Parts</span>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 4: Toy Engine Components
    "sim_toy_engine": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Toy Locomotive Component Inspector</h3>
                <p class="text-xs text-slate-400">Click individual components on the wooden train engine to examine their 3D shape.</p>
            </div>
            <div class="flex items-center gap-1.5">
                <span id="trainPartsInspectedBadge" class="text-xs px-2.5 py-1 rounded-xl bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30">
                    Inspecting: Boiler
                </span>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Train Engine Interactive SVG -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px] flex items-center justify-center">
                <svg id="toyEngineSvg" viewBox="0 0 460 220" class="w-full h-auto max-h-[220px]">
                    <!-- Railway Track -->
                    <line x1="20" y1="195" x2="440" y2="195" stroke="#64748b" stroke-width="4"/>
                    <line x1="40" y1="195" x2="40" y2="205" stroke="#475569" stroke-width="3"/>
                    <line x1="100" y1="195" x2="100" y2="205" stroke="#475569" stroke-width="3"/>
                    <line x1="160" y1="195" x2="160" y2="205" stroke="#475569" stroke-width="3"/>
                    <line x1="220" y1="195" x2="220" y2="205" stroke="#475569" stroke-width="3"/>
                    <line x1="280" y1="195" x2="280" y2="205" stroke="#475569" stroke-width="3"/>
                    <line x1="340" y1="195" x2="340" y2="205" stroke="#475569" stroke-width="3"/>
                    <line x1="400" y1="195" x2="400" y2="205" stroke="#475569" stroke-width="3"/>

                    <!-- 1. Driver's Cabin (Grey Cuboid) -->
                    <g onclick="selectTrainPart('cabin')" class="cursor-pointer" id="trainPartCabin">
                        <rect x="290" y="65" width="80" height="90" rx="3" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
                        <!-- Cabin Window -->
                        <rect x="310" y="80" width="40" height="30" rx="2" fill="#0284c7" stroke="#bae6fd" stroke-width="1.5"/>
                        <text x="330" y="140" fill="#f8fafc" font-size="9" font-weight="bold" text-anchor="middle">Cabin (Cuboid)</text>
                    </g>

                    <!-- 2. Coal Tender Box (Blue Cube) -->
                    <g onclick="selectTrainPart('tender')" class="cursor-pointer" id="trainPartTender">
                        <rect x="375" y="100" width="55" height="55" rx="3" fill="#2563eb" stroke="#60a5fa" stroke-width="2"/>
                        <text x="402" y="132" fill="#eff6ff" font-size="8" font-weight="bold" text-anchor="middle">Tender (Cube)</text>
                    </g>

                    <!-- 3. Boiler (Red Cylinder) -->
                    <g onclick="selectTrainPart('boiler')" class="cursor-pointer" id="trainPartBoiler">
                        <rect x="110" y="90" width="180" height="65" rx="12" fill="#dc2626" stroke="#f87171" stroke-width="3"/>
                        <ellipse cx="110" cy="122" rx="15" ry="32" fill="#b91c1c" stroke="#f87171" stroke-width="2"/>
                        <text x="200" y="127" fill="#fef2f2" font-size="10" font-weight="bold" text-anchor="middle">Boiler (Cylinder)</text>
                    </g>

                    <!-- 4. Smokestack (Yellow Cone) -->
                    <g onclick="selectTrainPart('stack')" class="cursor-pointer" id="trainPartStack">
                        <polygon points="145,45 130,90 160,90" fill="#eab308" stroke="#fde047" stroke-width="2"/>
                        <!-- Smoke Puffs -->
                        <circle cx="145" cy="35" r="6" fill="#cbd5e1" opacity="0.6"/>
                        <circle cx="150" cy="22" r="9" fill="#cbd5e1" opacity="0.4"/>
                        <text x="145" y="75" fill="#713f12" font-size="8" font-weight="bold" text-anchor="middle">Cone</text>
                    </g>

                    <!-- 5. Wheels (Flat Cylinders) -->
                    <g onclick="selectTrainPart('wheels')" class="cursor-pointer" id="trainPartWheels">
                        <!-- Front Wheels -->
                        <circle cx="140" cy="170" r="18" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>
                        <circle cx="140" cy="170" r="6" fill="#f59e0b"/>
                        <circle cx="195" cy="170" r="18" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>
                        <circle cx="195" cy="170" r="6" fill="#f59e0b"/>
                        <!-- Middle & Rear Wheels -->
                        <circle cx="250" cy="170" r="18" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>
                        <circle cx="250" cy="170" r="6" fill="#f59e0b"/>
                        <circle cx="310" cy="170" r="22" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>
                        <circle cx="310" cy="170" r="7" fill="#f59e0b"/>
                        <circle cx="360" cy="170" r="22" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>
                        <circle cx="360" cy="170" r="7" fill="#f59e0b"/>
                        <circle cx="410" cy="170" r="18" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>
                        <circle cx="410" cy="170" r="6" fill="#f59e0b"/>
                    </g>
                </svg>
            </div>

            <!-- Part Analysis Card -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="text-xs font-bold text-slate-300" id="trainPartName">Horizontal Boiler</div>
                <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 text-xs space-y-1.5">
                    <div class="flex items-center justify-between">
                        <span class="text-slate-400">3D Solid:</span>
                        <span id="trainPartShape" class="text-red-400 font-bold font-mono">Cylinder</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <span class="text-slate-400">Quantity in Train:</span>
                        <span id="trainPartQty" class="text-white font-bold font-mono">1</span>
                    </div>
                    <p class="text-slate-400 text-[11px] pt-1" id="trainPartDesc">
                        Forms the sturdy pressurized tank of the steam locomotive, holding water and steam.
                    </p>
                </div>

                <div class="grid grid-cols-2 gap-2 text-center text-xs">
                    <button onclick="selectTrainPart('boiler')" class="p-2 rounded bg-slate-900 hover:bg-slate-800 border border-slate-800 text-red-300 font-semibold text-[11px]">
                        🛢 Boiler (1)
                    </button>
                    <button onclick="selectTrainPart('stack')" class="p-2 rounded bg-slate-900 hover:bg-slate-800 border border-slate-800 text-yellow-300 font-semibold text-[11px]">
                        🔺 Smokestack (1)
                    </button>
                    <button onclick="selectTrainPart('cabin')" class="p-2 rounded bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-300 font-semibold text-[11px]">
                        📦 Cabin (1)
                    </button>
                    <button onclick="selectTrainPart('wheels')" class="p-2 rounded bg-slate-900 hover:bg-slate-800 border border-slate-800 text-amber-300 font-semibold text-[11px]">
                        ⚙ Wheels (6)
                    </button>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 5: Cube Versus Cuboid
    "sim_cube_is_cuboid": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Dimension Morphing Lab: Cube vs Cuboid</h3>
                <p class="text-xs text-slate-400">Adjust the length, width, and height sliders to prove that every cube is a special cuboid.</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="makeDimensionsEqual()" class="px-3 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition shadow flex items-center gap-1">
                    ✨ Make All Equal (Cube!)
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Dynamic 3D Box Rendering SVG -->
            <div class="md:col-span-7 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px] flex items-center justify-center">
                <svg id="cubeMorphSvg" viewBox="0 0 380 220" class="w-full h-auto max-h-[220px]">
                    <!-- Ground Ellipse -->
                    <ellipse cx="190" cy="190" rx="130" ry="18" fill="#0f172a" opacity="0.8"/>

                    <!-- Isometric Box Polygons (Redrawn dynamically by JS) -->
                    <g id="morphBoxGroup">
                        <!-- Populated by JS -->
                    </g>
                </svg>
            </div>

            <!-- Sliders & Shape Status -->
            <div class="md:col-span-5 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="flex items-center justify-between">
                    <span class="text-xs text-slate-400">Classification:</span>
                    <span id="morphClassificationBadge" class="text-xs px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 font-bold font-mono">
                        General Cuboid
                    </span>
                </div>

                <div class="space-y-2.5 text-xs">
                    <div>
                        <div class="flex justify-between text-slate-400 mb-1">
                            <span>Length (X):</span>
                            <span id="labelLen" class="font-mono text-amber-300 font-bold">120 px</span>
                        </div>
                        <input type="range" id="sliderLen" min="60" max="140" value="120" oninput="updateMorphBox()" class="w-full accent-amber-500 cursor-pointer">
                    </div>
                    <div>
                        <div class="flex justify-between text-slate-400 mb-1">
                            <span>Width (Y):</span>
                            <span id="labelWid" class="font-mono text-sky-300 font-bold">70 px</span>
                        </div>
                        <input type="range" id="sliderWid" min="60" max="140" value="70" oninput="updateMorphBox()" class="w-full accent-sky-500 cursor-pointer">
                    </div>
                    <div>
                        <div class="flex justify-between text-slate-400 mb-1">
                            <span>Height (Z):</span>
                            <span id="labelHei" class="font-mono text-emerald-300 font-bold">85 px</span>
                        </div>
                        <input type="range" id="sliderHei" min="60" max="140" value="85" oninput="updateMorphBox()" class="w-full accent-emerald-500 cursor-pointer">
                    </div>
                </div>

                <div class="p-2.5 bg-slate-900 rounded-lg border border-slate-800 text-[11px] text-slate-300" id="morphStatusSummary">
                    When length ≠ width ≠ height, the six faces are rectangular (cuboid). Equalize all three to form a cube!
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 6: Flat Curved Faces (Ramp Test)
    "sim_flat_curved_surfaces": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Inclined Ramp Motion Laboratory</h3>
                <p class="text-xs text-slate-400">Place solid shapes on an inclined ramp to discover whether they roll, slide, or do both!</p>
            </div>
            <div class="flex items-center gap-1.5 flex-wrap">
                <button onclick="selectRampShape('sphere')" id="btnRampSphere" class="px-2.5 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition shadow">
                    ⚽ Sphere
                </button>
                <button onclick="selectRampShape('cube')" id="btnRampCube" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition">
                    🧊 Cube
                </button>
                <button onclick="selectRampShape('cylinder_curved')" id="btnRampCylSide" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition">
                    🛢 Cylinder (Side)
                </button>
                <button onclick="selectRampShape('cylinder_flat')" id="btnRampCylFlat" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition">
                    🪙 Cylinder (Flat)
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Animated Ramp SVG Canvas -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px] flex items-center justify-center">
                <svg id="rampSvgCanvas" viewBox="0 0 460 220" class="w-full h-auto max-h-[220px]">
                    <!-- Inclined Ramp Triangle -->
                    <polygon points="50,60 50,190 320,190" fill="#334155" stroke="#475569" stroke-width="2"/>
                    <line x1="50" y1="60" x2="320" y2="190" stroke="#f59e0b" stroke-width="3"/>
                    <!-- Horizontal Runway -->
                    <line x1="320" y1="190" x2="430" y2="190" stroke="#475569" stroke-width="3"/>
                    <text x="180" y="140" fill="#94a3b8" font-size="11" font-weight="bold" transform="rotate(25, 180, 140)">Wooden Incline</text>

                    <!-- Moving Test Object Group -->
                    <g id="rampMovingObject" transform="translate(65, 55)">
                        <!-- Populated by JS -->
                    </g>
                </svg>
            </div>

            <!-- Motion Analysis Card -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <button onclick="releaseRampObject()" id="btnReleaseRamp" class="w-full py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition shadow flex items-center justify-center gap-1.5">
                    🚀 Release Down Ramp
                </button>

                <div class="p-3 bg-slate-900 rounded-lg border border-slate-800 text-xs space-y-1.5">
                    <div class="flex items-center justify-between">
                        <span class="text-slate-400">Motion Type:</span>
                        <span id="rampMotionType" class="text-amber-400 font-bold font-mono">Rolling</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <span class="text-slate-400">Surface in Contact:</span>
                        <span id="rampContactSurface" class="text-slate-200 font-semibold">Continuous Curved</span>
                    </div>
                    <p class="text-slate-400 text-[11px] pt-1" id="rampExplanation">
                        A sphere contacts the incline at a single point and rotates continuously down the ramp without sliding.
                    </p>
                </div>

                <div class="p-2 bg-slate-900/80 rounded border border-slate-800 text-[11px] text-slate-400">
                    💡 <span class="text-slate-200 font-semibold">Physics Principle:</span> Curved surfaces roll; flat faces slide!
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 7: Shape Mystery Descriptions
    "sim_mystery_shape_describer": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Back-to-Back Architect Challenge</h3>
                <p class="text-xs text-slate-400">Listen to the secret geometric instruction and place matching shapes in correct vertical order.</p>
            </div>
            <div class="flex items-center gap-1.5">
                <button onclick="generateNewMysteryGoal()" class="px-2.5 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition shadow flex items-center gap-1">
                    🎲 New Secret Design
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Builder Workspace SVG -->
            <div class="md:col-span-7 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px] flex items-center justify-center">
                <svg id="architectSvgCanvas" viewBox="0 0 360 220" class="w-full h-auto max-h-[220px]">
                    <line x1="40" y1="195" x2="320" y2="195" stroke="#475569" stroke-width="4"/>
                    <text x="180" y="212" fill="#64748b" font-size="10" text-anchor="middle">Building Platform</text>

                    <!-- Student Placed Shapes (Tier 1, Tier 2, Tier 3) -->
                    <g id="placedTier1"></g>
                    <g id="placedTier2"></g>
                    <g id="placedTier3"></g>
                </svg>
            </div>

            <!-- Architectural Voice Prompt & Toolbox -->
            <div class="md:col-span-5 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="p-3 bg-amber-500/10 border border-amber-500/30 rounded-xl text-xs space-y-1">
                    <div class="text-amber-400 font-bold flex items-center gap-1">
                        <span>📢</span> Architect's Voice Clue:
                    </div>
                    <p class="text-slate-200 italic" id="architectInstruction">
                        "1. Lay a flat cuboid as base. 2. Place a cylinder upright in the center. 3. Balance a cone with tip pointing up."
                    </p>
                </div>

                <div class="space-y-1">
                    <span class="text-[11px] text-slate-400 font-semibold">Select Next Shape to Stack:</span>
                    <div class="grid grid-cols-3 gap-2">
                        <button onclick="addArchitectShape('cuboid')" class="p-2 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-slate-200">
                            📦 Cuboid
                        </button>
                        <button onclick="addArchitectShape('cylinder')" class="p-2 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-slate-200">
                            🛢 Cylinder
                        </button>
                        <button onclick="addArchitectShape('cone')" class="p-2 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-700 text-xs font-bold text-slate-200">
                            🔺 Cone
                        </button>
                    </div>
                </div>

                <div class="flex items-center justify-between pt-1">
                    <button onclick="clearArchitectStack()" class="text-xs text-rose-400 hover:text-rose-300 font-semibold underline">
                        Clear Stack
                    </button>
                    <span id="architectMatchStatus" class="text-xs font-bold text-amber-400">Stack Height: 0 / 3</span>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 8: Classroom Shape Hunt
    "sim_classroom_shape_hunt": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Classroom 3D Shape Detective Safari</h3>
                <p class="text-xs text-slate-400">Click highlighted classroom items to identify their 3D geometric shapes and log them into the tally chart.</p>
            </div>
            <div class="flex items-center gap-2">
                <span id="safariFoundCount" class="text-xs px-2.5 py-1 rounded-xl bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30">
                    Found: 0 / 5 Shapes
                </span>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Classroom Scene SVG -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px] flex items-center justify-center">
                <svg id="safariSvgCanvas" viewBox="0 0 460 220" class="w-full h-auto max-h-[220px]">
                    <!-- Classroom Floor and Wall -->
                    <rect x="0" y="0" width="460" height="140" fill="#1e293b"/>
                    <rect x="0" y="140" width="460" height="80" fill="#0f172a"/>
                    <!-- Chalkboard -->
                    <rect x="140" y="20" width="180" height="90" rx="3" fill="#064e3b" stroke="#78350f" stroke-width="4"/>
                    <text x="230" y="65" fill="#a7f3d0" font-size="12" font-weight="bold" text-anchor="middle">JOYFUL MATHS</text>

                    <!-- Teacher Desk -->
                    <rect x="120" y="130" width="220" height="60" rx="4" fill="#854d0e" stroke="#a16207" stroke-width="2"/>

                    <!-- 1. Globe (Sphere) -->
                    <g onclick="clickSafariItem('globe')" class="cursor-pointer" id="safariItemGlobe">
                        <circle cx="60" cy="90" r="24" fill="#0284c7" stroke="#38bdf8" stroke-width="2.5"/>
                        <path d="M 45,85 Q 60,75 75,90 Q 65,105 45,85" fill="#22c55e" opacity="0.8"/>
                        <rect x="56" y="114" width="8" height="20" fill="#64748b"/>
                        <rect x="44" y="134" width="32" height="6" rx="2" fill="#475569"/>
                    </g>

                    <!-- 2. Chalk Box (Cuboid) -->
                    <g onclick="clickSafariItem('chalk_box')" class="cursor-pointer" id="safariItemChalk">
                        <rect x="145" y="115" width="45" height="30" rx="2" fill="#cbd5e1" stroke="#f8fafc" stroke-width="2"/>
                        <text x="167" y="134" fill="#334155" font-size="8" font-weight="bold" text-anchor="middle">CHALK</text>
                    </g>

                    <!-- 3. Water Bottle (Cylinder) -->
                    <g onclick="clickSafariItem('bottle')" class="cursor-pointer" id="safariItemBottle">
                        <rect x="230" y="105" width="22" height="40" rx="4" fill="#06b6d4" stroke="#67e8f9" stroke-width="2"/>
                        <rect x="235" y="98" width="12" height="7" rx="1" fill="#0e7490"/>
                    </g>

                    <!-- 4. Party Hat on Shelf (Cone) -->
                    <g onclick="clickSafariItem('hat')" class="cursor-pointer" id="safariItemHat">
                        <polygon points="380,50 360,95 400,95" fill="#f59e0b" stroke="#fcd34d" stroke-width="2"/>
                        <circle cx="380" cy="46" r="3" fill="#ef4444"/>
                    </g>

                    <!-- 5. Rubik's Block (Cube) -->
                    <g onclick="clickSafariItem('cube')" class="cursor-pointer" id="safariItemCube">
                        <rect x="285" y="118" width="26" height="26" rx="2" fill="#ec4899" stroke="#f472b6" stroke-width="2"/>
                        <line x1="285" y1="127" x2="311" y2="127" stroke="#831843"/>
                        <line x1="285" y1="135" x2="311" y2="135" stroke="#831843"/>
                        <line x1="294" y1="118" x2="294" y2="144" stroke="#831843"/>
                        <line x1="302" y1="118" x2="302" y2="144" stroke="#831843"/>
                    </g>
                </svg>
            </div>

            <!-- Tally Table -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-2.5">
                <div class="text-xs font-bold text-slate-300">Detective Tally Log:</div>
                <div class="space-y-1 text-xs">
                    <div id="tallyRowGlobe" class="p-2 rounded bg-slate-900 border border-slate-800 flex items-center justify-between opacity-50">
                        <span>🌍 Globe</span>
                        <span class="font-bold text-sky-400">Sphere</span>
                    </div>
                    <div id="tallyRowChalk" class="p-2 rounded bg-slate-900 border border-slate-800 flex items-center justify-between opacity-50">
                        <span>📦 Chalk Box</span>
                        <span class="font-bold text-amber-400">Cuboid</span>
                    </div>
                    <div id="tallyRowBottle" class="p-2 rounded bg-slate-900 border border-slate-800 flex items-center justify-between opacity-50">
                        <span>🛢 Water Bottle</span>
                        <span class="font-bold text-cyan-400">Cylinder</span>
                    </div>
                    <div id="tallyRowHat" class="p-2 rounded bg-slate-900 border border-slate-800 flex items-center justify-between opacity-50">
                        <span>🎉 Party Hat</span>
                        <span class="font-bold text-yellow-400">Cone</span>
                    </div>
                    <div id="tallyRowCube" class="p-2 rounded bg-slate-900 border border-slate-800 flex items-center justify-between opacity-50">
                        <span>🎲 Puzzle Cube</span>
                        <span class="font-bold text-pink-400">Cube</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
}

