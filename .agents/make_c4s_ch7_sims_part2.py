# make_c4s_ch7_sims_part2.py
# Bespoke interactive simulators 9 to 16 for Chapter 7: How Things Work

simulators_part2 = {}

# SIM 9: Shape Affects Flotation
simulators_part2["sim-9"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-cyan-300">Clay & Foil Shape Flotation Lab</h4>
            </div>
            <span class="text-xs bg-cyan-500/20 text-cyan-300 px-2.5 py-1 rounded-full font-medium border border-cyan-500/30">Volume & Geometry</span>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.setClayShape('ball')" id="clay-ball-btn" class="clay-shape-btn active p-2.5 rounded-xl border border-cyan-500/60 bg-cyan-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">⚪</span>
                <span class="text-xs font-semibold text-cyan-200">1. Solid Clay Ball</span>
                <span class="text-[10px] text-slate-400">Dense & Compact</span>
            </button>
            <button onclick="window.setClayShape('boat')" id="clay-boat-btn" class="clay-shape-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🥣</span>
                <span class="text-xs font-semibold text-slate-300">2. Hollow Clay Boat</span>
                <span class="text-[10px] text-slate-400">Wide Air Pocket</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="clayTankSvg" class="w-full max-w-md h-48 rounded-lg" viewBox="0 0 320 180">
                <!-- Tank -->
                <rect x="20" y="20" width="280" height="150" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="2" />
                <rect x="22" y="60" width="276" height="108" fill="#0369a1" fill-opacity="0.35" />
                <line x1="22" y1="60" x2="298" y2="60" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2" />
                <text x="30" y="52" fill="#7dd3fc" font-size="10" font-weight="bold">Water Surface</text>

                <!-- Dynamic Clay/Foil Item -->
                <g id="clayItemElement" style="transition: transform 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);">
                    <!-- Default Ball at bottom -->
                    <circle cx="160" cy="150" r="16" fill="#ea580c" stroke="#fed7aa" stroke-width="2" />
                </g>
            </svg>
            <div id="clayStatusReadout" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-rose-950/80 text-rose-300 border border-rose-800/60">
                Solid Ball Sinks: Small volume displaces very little water; gravitational pull exceeds buoyant force.
            </div>
        </div>

        <div class="p-3 bg-slate-950/50 rounded-xl border border-slate-800 text-xs text-slate-300">
            <p><strong class="text-cyan-300">Key Principle:</strong> Reshaping identical clay mass from a compact ball into a wide hollow bowl increases water displacement, providing enough buoyant force to float!</p>
        </div>
    </div>
"""

# SIM 10: Displacement And Buoyancy (Archimedes Overflow Can)
simulators_part2["sim-10"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-emerald-300">Displacement & Archimedes Overflow Lab</h4>
            </div>
            <span class="text-xs bg-emerald-500/20 text-emerald-300 px-2.5 py-1 rounded-full font-medium border border-emerald-500/30">Eureka Principle</span>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[240px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="overflowCanSvg" class="w-full max-w-md h-56" viewBox="0 0 320 220">
                <!-- Overflow Can on Left -->
                <rect x="50" y="70" width="100" height="130" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="2" />
                <!-- Spout -->
                <path d="M150,90 L180,110 L180,116 L150,96 Z" fill="#10b981" />
                <rect id="overflowCanWater" x="52" y="90" width="96" height="108" fill="#059669" fill-opacity="0.35" />

                <!-- Measuring Cylinder on Right under spout -->
                <rect x="190" y="115" width="50" height="85" rx="3" fill="#0f172a" stroke="#6ee7b7" stroke-width="1.5" />
                <!-- Graduated markings -->
                <line x1="190" y1="135" x2="200" y2="135" stroke="#a7f3d0" stroke-width="1" />
                <line x1="190" y1="155" x2="205" y2="155" stroke="#a7f3d0" stroke-width="1" />
                <line x1="190" y1="175" x2="200" y2="175" stroke="#a7f3d0" stroke-width="1" />
                <rect id="cylinderDisplacedWater" x="192" y="198" width="46" height="0" fill="#059669" fill-opacity="0.6" style="transition: all 0.8s ease-out;" />

                <!-- Submerging Object suspended on string -->
                <g id="archimedesObject" style="transition: transform 0.8s ease-in-out;">
                    <line x1="100" y1="10" x2="100" y2="50" stroke="#f8fafc" stroke-width="1.5" />
                    <rect x="85" y="50" width="30" height="30" rx="4" fill="#64748b" stroke="#cbd5e1" stroke-width="2" />
                    <text x="92" y="70" fill="#ffffff" font-size="10" font-weight="bold">80g</text>
                </g>

                <!-- Water Spout Stream Animation (hidden by default) -->
                <path id="waterStream" d="M180,113 Q195,130 215,190" stroke="#6ee7b7" stroke-width="2" fill="none" stroke-dasharray="4 2" opacity="0" />
            </svg>

            <div class="grid grid-cols-2 gap-3 w-full max-w-md mt-2 text-xs font-semibold">
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-center">
                    <span class="text-slate-400 block">Object Air Weight:</span>
                    <span class="text-amber-300 font-bold">80 g</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-center">
                    <span class="text-slate-400 block">Displaced Water:</span>
                    <span id="displacedWaterVal" class="text-emerald-300 font-bold">0 mL (0 g)</span>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.lowerArchimedesObject()" id="lowerArchimedesBtn" class="py-2.5 px-4 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm flex items-center justify-center gap-2">
                <span>⬇️</span> Submerge Metal Cube
            </button>
            <button onclick="window.resetArchimedes()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Reset
            </button>
        </div>
    </div>
"""

# SIM 11: Crafting Model Boats
simulators_part2["sim-11"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-blue-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-blue-300">Model Boat Materials Workshop</h4>
            </div>
            <span class="text-xs bg-blue-500/20 text-blue-300 px-2.5 py-1 rounded-full font-medium border border-blue-500/30">Materials & Waterproofing</span>
        </div>

        <div class="grid grid-cols-3 gap-2">
            <button onclick="window.selectBoatMaterial('plain')" id="mat-plain" class="boat-mat-btn active p-2.5 rounded-xl border border-blue-500/60 bg-blue-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">📄</span>
                <span class="text-xs font-semibold text-blue-200">Plain Paper</span>
                <span class="text-[10px] text-slate-400">Porous Cellulose</span>
            </button>
            <button onclick="window.selectBoatMaterial('waxed')" id="mat-waxed" class="boat-mat-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">🕯️</span>
                <span class="text-xs font-semibold text-slate-300">Waxed Paper</span>
                <span class="text-[10px] text-slate-400">Hydrophobic Wax</span>
            </button>
            <button onclick="window.selectBoatMaterial('wood')" id="mat-wood" class="boat-mat-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">🪵</span>
                <span class="text-xs font-semibold text-slate-300">Twig Raft</span>
                <span class="text-[10px] text-slate-400">Buoyant Wood</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="boatWorkshopSvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <rect x="20" y="80" width="280" height="90" fill="#0284c7" fill-opacity="0.3" rx="4" />
                <path d="M20,80 Q90,76 160,80 T300,80" stroke="#38bdf8" stroke-width="2" fill="none" />

                <!-- Boat Graphic in Puddle -->
                <g id="modelBoatGraphic" style="transform-origin: 160px 80px; transition: all 0.6s ease-in-out;">
                    <polygon id="boatHullShape" points="110,80 210,80 185,105 135,105" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" />
                    <!-- Sail / Flag -->
                    <polygon id="boatSailShape" points="160,80 160,40 190,60" fill="#ef4444" />
                    <line x1="160" y1="80" x2="160" y2="38" stroke="#64748b" stroke-width="2" />
                </g>
            </svg>

            <!-- Soak / Durability Progress Bar -->
            <div class="w-full max-w-md mt-2">
                <div class="flex justify-between text-xs mb-1">
                    <span class="text-slate-400">Water Saturation / Soggy Level:</span>
                    <span id="soakPercentLabel" class="font-bold text-rose-400">0%</span>
                </div>
                <div class="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
                    <div id="soakProgressBar" class="h-full bg-rose-500 transition-all duration-300" style="width: 0%;"></div>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.testBoatInWater()" class="py-2.5 px-4 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm flex items-center justify-center gap-2">
                <span>⏱</span> Float in Water Stream
            </button>
            <button onclick="window.resetBoatMaterial()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Reset
            </button>
        </div>
    </div>
"""

# SIM 12: Natural Shell Vessels
simulators_part2["sim-12"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-amber-300">Natural Shell Vessels Lab</h4>
            </div>
            <span class="text-xs bg-amber-500/20 text-amber-300 px-2.5 py-1 rounded-full font-medium border border-amber-500/30">Nature's Boats</span>
        </div>

        <div class="grid grid-cols-3 gap-2">
            <button onclick="window.setShellVessel('coconut')" id="vessel-coconut" class="shell-btn active p-2.5 rounded-xl border border-amber-500/60 bg-amber-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🥥</span>
                <span class="text-xs font-semibold text-amber-200">Coconut Shell</span>
                <span class="text-[10px] text-slate-400">High Capacity</span>
            </button>
            <button onclick="window.setShellVessel('walnut')" id="vessel-walnut" class="shell-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🌰</span>
                <span class="text-xs font-semibold text-slate-300">Walnut Half</span>
                <span class="text-[10px] text-slate-400">Light & Buoyant</span>
            </button>
            <button onclick="window.setShellVessel('leaf')" id="vessel-leaf" class="shell-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-2xl">🍃</span>
                <span class="text-xs font-semibold text-slate-300">Banyan Leaf Boat</span>
                <span class="text-[10px] text-slate-400">Folded Canoe</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[200px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="shellVesselSvg" class="w-full max-w-md h-44" viewBox="0 0 320 160">
                <rect x="20" y="70" width="280" height="80" fill="#0284c7" fill-opacity="0.35" rx="4" />
                <path d="M20,70 Q90,66 160,70 T300,70" stroke="#38bdf8" stroke-width="2" fill="none" />

                <!-- Vessel Graphic -->
                <g id="shellGraphicGroup" style="transform-origin: 160px 70px; transition: transform 0.4s ease;">
                    <!-- Coconut bowl shape by default -->
                    <path id="shellBody" d="M110,65 Q160,115 210,65 Z" fill="#78350f" stroke="#b45309" stroke-width="3" />
                    <!-- Cargo marbles counter group -->
                    <g id="shellCargoGroup"></g>
                </g>
            </svg>
            <div id="shellCargoStatus" class="mt-1 text-xs font-semibold px-3 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700">
                Pebble Cargo: 0 / Max Safe: 12
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.addShellCargo()" class="py-2.5 px-4 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm flex items-center justify-center gap-2">
                <span>➕</span> Add Pebble Cargo
            </button>
            <button onclick="window.resetShellVessel()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Unload Cargo
            </button>
        </div>
    </div>
"""

# SIM 13: Boat Stability Dynamics
simulators_part2["sim-13"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-violet-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-violet-300">Boat Stability & Righting Moment Lab</h4>
            </div>
            <span class="text-xs bg-violet-500/20 text-violet-300 px-2.5 py-1 rounded-full font-medium border border-violet-500/30">Center of Gravity vs Buoyancy</span>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.setHullType('wide')" id="hull-wide" class="hull-type-btn active p-2.5 rounded-xl border border-violet-500/60 bg-violet-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">🛶</span>
                <span class="text-xs font-semibold text-violet-200">Wide Flat-Bottom Hull</span>
                <span class="text-[10px] text-emerald-400">Self-Righting Stable</span>
            </button>
            <button onclick="window.setHullType('tall')" id="hull-tall" class="hull-type-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">⛵</span>
                <span class="text-xs font-semibold text-slate-300">Top-Heavy Tall Mast Hull</span>
                <span class="text-[10px] text-rose-400">High Center of Gravity</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="stabilitySvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <rect x="20" y="80" width="280" height="90" fill="#0284c7" fill-opacity="0.35" rx="4" />
                <line x1="20" y1="80" x2="300" y2="80" stroke="#38bdf8" stroke-width="2" />

                <!-- Tilting Boat Group -->
                <g id="tiltingBoatGroup" style="transform-origin: 160px 80px; transition: transform 0.2s ease-out;">
                    <!-- Boat Hull -->
                    <polygon id="hullPolygon" points="90,75 230,75 200,115 120,115" fill="#3b82f6" stroke="#93c5fd" stroke-width="2" />
                    <!-- Mast & weight -->
                    <line id="hullMastLine" x1="160" y1="75" x2="160" y2="25" stroke="#e2e8f0" stroke-width="3" />
                    <circle id="hullMastWeight" cx="160" cy="25" r="8" fill="#f59e0b" />

                    <!-- Center of Gravity indicator (G) -->
                    <circle id="cgMarker" cx="160" cy="85" r="5" fill="#ef4444" stroke="#ffffff" stroke-width="1.5" />
                    <text id="cgLabel" x="170" y="88" fill="#fca5a5" font-size="9" font-weight="bold">G</text>

                    <!-- Center of Buoyancy indicator (B) -->
                    <circle id="cbMarker" cx="160" cy="98" r="5" fill="#10b981" stroke="#ffffff" stroke-width="1.5" />
                    <text id="cbLabel" x="170" y="101" fill="#6ee7b7" font-size="9" font-weight="bold">B</text>
                </g>
            </svg>

            <div id="stabilityStatus" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-700/60">
                Stable Equilibrium: Wide hull generates strong righting torque to restore upright balance.
            </div>
        </div>

        <div class="flex flex-col gap-2">
            <div class="flex items-center justify-between text-xs text-slate-400">
                <span>Simulated Wave Tilt Angle:</span>
                <span id="tiltDegreeLabel" class="font-bold text-violet-300">0°</span>
            </div>
            <input type="range" id="tiltSlider" min="-45" max="45" value="0" oninput="window.updateTiltAngle(this.value)" class="w-full accent-violet-400 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-500">
                <span>-45° (Port Tilt)</span>
                <span>0° (Upright)</span>
                <span>+45° (Starboard Tilt)</span>
            </div>
        </div>
    </div>
"""

# SIM 14: Load Capacity Testing
simulators_part2["sim-14"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-amber-300">Load Capacity & Plimsoll Waterline Lab</h4>
            </div>
            <span class="text-xs bg-amber-500/20 text-amber-300 px-2.5 py-1 rounded-full font-medium border border-amber-500/30">Safe Cargo Loading</span>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="loadCapacitySvg" class="w-full max-w-md h-48" viewBox="0 0 320 180">
                <!-- Water -->
                <rect x="20" y="70" width="280" height="95" fill="#0284c7" fill-opacity="0.35" rx="4" />
                <line x1="20" y1="70" x2="300" y2="70" stroke="#38bdf8" stroke-width="2" />
                <text x="30" y="62" fill="#7dd3fc" font-size="10" font-weight="bold">Waterline</text>

                <!-- Floating Cargo Barge -->
                <g id="cargoBargeGroup" style="transform: translateY(0px); transition: transform 0.4s ease;">
                    <polygon points="80,55 240,55 210,105 110,105" fill="#334155" stroke="#94a3b8" stroke-width="2" />
                    <!-- Plimsoll Line (Red danger line) -->
                    <line x1="75" y1="62" x2="245" y2="62" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="6 3" />
                    <text x="250" y="65" fill="#f87171" font-size="9" font-weight="bold">Max Draft</text>

                    <!-- Stack of cargo containers/coins -->
                    <g id="bargeCoinsGroup"></g>
                </g>
            </svg>

            <div class="flex items-center justify-between w-full max-w-md mt-2 text-xs font-semibold px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800">
                <span class="text-slate-300">Cargo Coins: <span id="coinCountVal" class="text-amber-400 font-bold">0</span></span>
                <span class="text-slate-300">Freeboard Remaining: <span id="freeboardVal" class="text-emerald-400 font-bold">15 mm</span></span>
                <span id="overloadBadge" class="text-emerald-300 font-bold">SAFE</span>
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.addBargeCoin()" class="py-2.5 px-4 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm flex items-center justify-center gap-2">
                <span>🪙</span> Add Metal Coin (+10g)
            </button>
            <button onclick="window.resetBargeLoad()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Unload Cargo
            </button>
        </div>
    </div>
"""

# SIM 15: Modifying Object Buoyancy (Ballast Chamber / Submarine)
simulators_part2["sim-15"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-cyan-300">Submarine Ballast & Buoyancy Control Lab</h4>
            </div>
            <span class="text-xs bg-cyan-500/20 text-cyan-300 px-2.5 py-1 rounded-full font-medium border border-cyan-500/30">Variable Density Tank</span>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[240px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="ballastSvg" class="w-full max-w-md h-52" viewBox="0 0 320 200">
                <!-- Deep Water Tank -->
                <rect x="30" y="20" width="260" height="170" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="2" />
                <rect x="32" y="50" width="256" height="138" fill="#0369a1" fill-opacity="0.35" />
                <line x1="32" y1="50" x2="288" y2="50" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2" />
                <text x="40" y="42" fill="#7dd3fc" font-size="10" font-weight="bold">Water Surface</text>

                <!-- Submarine / Cartesian Diver Vessel -->
                <g id="subVesselGroup" style="transform: translateY(0px); transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);">
                    <!-- Submarine Hull -->
                    <rect x="110" y="55" width="100" height="40" rx="20" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
                    <!-- Conning Tower -->
                    <rect x="145" y="42" width="24" height="15" rx="3" fill="#334155" stroke="#38bdf8" stroke-width="1.5" />
                    <!-- Periscope -->
                    <line x1="157" y1="42" x2="157" y2="30" stroke="#94a3b8" stroke-width="2" />
                    <line x1="157" y1="30" x2="165" y2="30" stroke="#94a3b8" stroke-width="2" />

                    <!-- Internal Ballast Water level -->
                    <rect id="subBallastWater" x="120" y="80" width="80" height="10" rx="4" fill="#0284c7" fill-opacity="0.8" style="transition: all 0.4s ease;" />
                    <text x="135" y="75" fill="#f8fafc" font-size="9" font-weight="bold">Ballast Tank</text>
                </g>
            </svg>

            <div class="flex items-center justify-between w-full max-w-md mt-2 text-xs font-semibold px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800">
                <span class="text-slate-300">Ballast State: <span id="ballastStateText" class="text-cyan-300">Air Filled (Floating)</span></span>
                <span class="text-slate-300">Average Density: <span id="avgDensityText" class="text-emerald-400">0.45 g/cm³</span></span>
            </div>
        </div>

        <div class="grid grid-cols-3 gap-2">
            <button onclick="window.setBallastState('surface')" id="ballast-surface" class="ballast-btn active py-2 px-2.5 rounded-xl border border-cyan-500/60 bg-cyan-950/40 text-xs font-semibold text-cyan-200">
                ⬆️ Blow Ballast (Float)
            </button>
            <button onclick="window.setBallastState('neutral')" id="ballast-neutral" class="ballast-btn py-2 px-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-xs font-semibold text-slate-300">
                ⚖️ Neutral Hover
            </button>
            <button onclick="window.setBallastState('dive')" id="ballast-dive" class="ballast-btn py-2 px-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-xs font-semibold text-slate-300">
                ⬇️ Flood Ballast (Dive)
            </button>
        </div>
    </div>
"""

# SIM 16: Balanced Mobile Structures
simulators_part2["sim-16"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-emerald-300">Balancing Bird & Center of Gravity Mobile Lab</h4>
            </div>
            <span class="text-xs bg-emerald-500/20 text-emerald-300 px-2.5 py-1 rounded-full font-medium border border-emerald-500/30">Stable Equilibrium</span>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.setBalanceMode('weighted')" id="bal-weighted" class="bal-mode-btn active p-2.5 rounded-xl border border-emerald-500/60 bg-emerald-950/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">🦅</span>
                <span class="text-xs font-semibold text-emerald-200">Wingtip Weights Below Beak</span>
                <span class="text-[10px] text-emerald-400">Ultra Stable (Low CG)</span>
            </button>
            <button onclick="window.setBalanceMode('unweighted')" id="bal-unweighted" class="bal-mode-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/40 text-center flex flex-col items-center gap-1">
                <span class="text-xl">❌</span>
                <span class="text-xs font-semibold text-slate-300">Weights Removed</span>
                <span class="text-[10px] text-rose-400">Top-Heavy (Tips Over)</span>
            </button>
        </div>

        <div class="relative bg-slate-950/90 rounded-xl p-4 border border-slate-800 min-h-[220px] flex flex-col items-center justify-center overflow-hidden">
            <svg id="balancingBirdSvg" class="w-full max-w-md h-52" viewBox="0 0 320 200">
                <!-- Pedestal / Fingertip Stand -->
                <rect x="156" y="100" width="8" height="90" fill="#475569" />
                <polygon points="140,190 180,190 160,180" fill="#334155" />
                <!-- Sharp pivot point on top of stand -->
                <polygon points="156,100 164,100 160,94" fill="#94a3b8" />

                <!-- Balancing Bird Mobile Assembly (Pivot at 160, 94) -->
                <g id="birdAssemblyGroup" style="transform-origin: 160px 94px; transition: transform 0.4s ease-out;">
                    <!-- Bird Beak tip resting on point -->
                    <polygon points="157,94 163,94 160,88" fill="#f59e0b" />
                    <!-- Bird Head & Body -->
                    <ellipse cx="160" cy="80" rx="16" ry="12" fill="#10b981" />
                    <circle cx="155" cy="78" r="2.5" fill="#ffffff" />
                    <circle cx="155" cy="78" r="1.2" fill="#0f172a" />

                    <!-- Arched Forward Swept Wings dipping BELOW the beak -->
                    <path id="leftWingPath" d="M148,82 C120,86 90,110 80,135" stroke="#059669" stroke-width="8" stroke-linecap="round" fill="none" />
                    <path id="rightWingPath" d="M172,82 C200,86 230,110 240,135" stroke="#059669" stroke-width="8" stroke-linecap="round" fill="none" />

                    <!-- Lead/Metal weights embedded at wing tips -->
                    <circle id="leftWingWeight" cx="80" cy="135" r="9" fill="#ef4444" stroke="#ffffff" stroke-width="2" />
                    <circle id="rightWingWeight" cx="240" cy="135" r="9" fill="#ef4444" stroke="#ffffff" stroke-width="2" />

                    <!-- Combined Center of Gravity indicator (hanging below pivot) -->
                    <g id="birdCgIndicator">
                        <line x1="160" y1="94" x2="160" y2="125" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 2" />
                        <circle cx="160" cy="125" r="5" fill="#f59e0b" stroke="#ffffff" stroke-width="1.5" />
                        <text x="170" y="129" fill="#fef08a" font-size="9" font-weight="bold">CG Below Pivot</text>
                    </g>
                </g>
            </svg>

            <div id="balanceBirdStatus" class="mt-2 text-xs font-semibold px-3 py-1 rounded-full bg-emerald-950/80 text-emerald-300 border border-emerald-700/60">
                Stable Equilibrium: Wing weights pull overall Center of Gravity well below the beak pivot!
            </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
            <button onclick="window.nudgeBalancingBird()" class="py-2.5 px-4 bg-emerald-600 hover:bg-emerald-500 text-white font-bold rounded-xl shadow-lg transition-all text-sm flex items-center justify-center gap-2">
                <span>👋</span> Tap & Nudge Bird Wing
            </button>
            <button onclick="window.resetBalancingBird()" class="py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-sm font-medium">
                Reset
            </button>
        </div>
    </div>
"""

