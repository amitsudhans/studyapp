"""
Interactive HTML/SVG Simulators for Class 6 Science Chapter 6: Materials Around Us
16 Bespoke interactive simulators (Slide 1 to 16).
Zero raw LaTeX. Pure Unicode.
"""

SIMULATORS = {
    1: """
        <!-- Simulator 1: Object Anatomy Disassembler -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🔍</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Object Anatomy Explorer</h3>
                        <p class="text-[11px] text-slate-400">Deconstruct everyday objects into their constituent materials</p>
                    </div>
                </div>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">Multi-Material</span>
            </div>

            <div class="flex items-center space-x-2">
                <button onclick="selectSim1Object('pen')" id="sim1Btn-pen" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-indigo-600 text-white transition">Ballpoint Pen</button>
                <button onclick="selectSim1Object('pencil')" id="sim1Btn-pencil" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Pencil</button>
                <button onclick="selectSim1Object('scissors')" id="sim1Btn-scissors" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Scissors</button>
                <button onclick="selectSim1Object('bottle')" id="sim1Btn-bottle" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Insulated Flask</button>
            </div>

            <!-- Interactive Stage Area -->
            <div id="sim1Stage" class="h-48 rounded-xl bg-slate-950 border border-slate-800/80 flex items-center justify-center p-4 relative overflow-hidden">
                <!-- Dynamic SVG will render here -->
            </div>

            <!-- Material Breakdown Table -->
            <div id="sim1Details" class="p-3 rounded-xl bg-slate-800/50 border border-slate-700/60 text-xs space-y-2">
                <!-- Breakdown will render here -->
            </div>
        </div>
    """,

    2: """
        <!-- Simulator 2: Harappan Terracotta Kiln Simulator -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🏺</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Harappan Terracotta Kiln</h3>
                        <p class="text-[11px] text-slate-400">Observe how ancient pyrotechnology transformed soft river clay into rock-hard ceramic</p>
                    </div>
                </div>
                <span id="sim2StatusBadge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-300 border border-amber-500/20">Raw River Clay</span>
            </div>

            <!-- Kiln & Pot Graphic Stage -->
            <div class="h-48 rounded-xl bg-slate-950 border border-slate-800/80 flex flex-col items-center justify-center relative overflow-hidden">
                <div id="sim2PotGraphic" class="transition-all duration-700 flex flex-col items-center">
                    <!-- SVG Pot -->
                    <svg width="120" height="120" viewBox="0 0 100 100">
                        <path id="sim2PotBody" d="M 30,20 Q 20,40 25,75 Q 30,90 50,90 Q 70,90 75,75 Q 80,40 70,20 Z" fill="#78716c" stroke="#57534e" stroke-width="2"/>
                        <ellipse cx="50" cy="20" rx="20" ry="6" fill="#a8a29e" stroke="#57534e" stroke-width="2"/>
                        <g id="sim2Motifs" opacity="0">
                            <line x1="32" y1="45" x2="68" y2="45" stroke="#1c1917" stroke-width="3" stroke-dasharray="3,3"/>
                            <circle cx="50" cy="60" r="8" fill="none" stroke="#1c1917" stroke-width="2"/>
                            <path d="M 45,60 Q 50,55 55,60" stroke="#1c1917" stroke-width="2" fill="none"/>
                        </g>
                    </svg>
                    <span id="sim2PotLabel" class="text-xs font-bold text-stone-400 mt-2">Soft Wet Clay (Raw Mud)</span>
                </div>
                <div id="sim2FireGlow" class="absolute inset-0 bg-gradient-to-t from-orange-600/30 via-red-600/10 to-transparent opacity-0 pointer-events-none transition-opacity duration-700"></div>
            </div>

            <!-- Controls -->
            <div class="grid grid-cols-3 gap-2">
                <button onclick="setSim2Stage('raw')" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-bold text-stone-300 border border-slate-700 transition">
                    1. Gather Clay
                </button>
                <button onclick="setSim2Stage('fire')" class="p-2 rounded-lg bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow-lg transition">
                    2. Fire in Kiln (850°C) 🔥
                </button>
                <button onclick="setSim2Stage('cool')" class="p-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow-lg transition">
                    3. Terracotta Artifact ✨
                </button>
            </div>
            <div id="sim2Explanation" class="text-xs text-slate-300 bg-slate-800/40 p-2.5 rounded-lg border border-slate-700/60 leading-relaxed">
                Raw clay contains hydrated aluminium silicates. At room temperature, it dissolves in water when wet.
            </div>
        </div>
    """,

    3: """
        <!-- Simulator 3: Material Substitution Lab (One Object, Diverse Materials) -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🥛</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Tumbler Material Swapper</h3>
                        <p class="text-[11px] text-slate-400">Compare how material choice transforms the same drinking cup</p>
                    </div>
                </div>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-300 border border-cyan-500/20">Same Object</span>
            </div>

            <!-- Material Picker -->
            <div class="grid grid-cols-4 gap-2">
                <button onclick="setSim3Material('glass')" id="sim3Btn-glass" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs transition">Glass</button>
                <button onclick="setSim3Material('steel')" id="sim3Btn-steel" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs transition">Steel</button>
                <button onclick="setSim3Material('clay')" id="sim3Btn-clay" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs transition">Clay Kulhad</button>
                <button onclick="setSim3Material('plastic')" id="sim3Btn-plastic" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs transition">Plastic</button>
            </div>

            <!-- Stage & Property Meters -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
                <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 flex flex-col items-center justify-center p-3">
                    <div id="sim3CupGraphic">
                        <!-- Rendered by JS -->
                    </div>
                    <span id="sim3MaterialName" class="text-xs font-bold text-cyan-300 mt-2">Transparent Borosilicate Glass</span>
                </div>
                <div class="space-y-2 text-xs">
                    <div>
                        <div class="flex justify-between text-[11px] text-slate-400 mb-1">
                            <span>Optical Transparency:</span>
                            <span id="sim3ValTransparency" class="font-bold text-cyan-400">100% (Transparent)</span>
                        </div>
                        <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                            <div id="sim3BarTransparency" class="bg-cyan-500 h-2 rounded-full" style="width: 100%;"></div>
                        </div>
                    </div>
                    <div>
                        <div class="flex justify-between text-[11px] text-slate-400 mb-1">
                            <span>Drop Durability:</span>
                            <span id="sim3ValDurability" class="font-bold text-rose-400">Low (Brittle Fragile)</span>
                        </div>
                        <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                            <div id="sim3BarDurability" class="bg-rose-500 h-2 rounded-full" style="width: 25%;"></div>
                        </div>
                    </div>
                    <div>
                        <div class="flex justify-between text-[11px] text-slate-400 mb-1">
                            <span>Thermal Feel:</span>
                            <span id="sim3ValThermal" class="font-bold text-amber-400">Moderate Conduction</span>
                        </div>
                        <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                            <div id="sim3BarThermal" class="bg-amber-500 h-2 rounded-full" style="width: 50%;"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """,

    4: """
        <!-- Simulator 4: Material Tree Explorer (One Material, Many Objects) -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🌳</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Material Tree Explorer</h3>
                        <p class="text-[11px] text-slate-400">Select a raw material to discover its vast family of objects</p>
                    </div>
                </div>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-300 border border-emerald-500/20">One to Many</span>
            </div>

            <!-- Material Tabs -->
            <div class="flex items-center space-x-2">
                <button onclick="setSim4Tree('wood')" id="sim4Btn-wood" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-emerald-600 text-white transition">Wood</button>
                <button onclick="setSim4Tree('steel')" id="sim4Btn-steel" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Iron & Steel</button>
                <button onclick="setSim4Tree('plastic')" id="sim4Btn-plastic" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Plastic</button>
                <button onclick="setSim4Tree('cotton')" id="sim4Btn-cotton" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Cotton</button>
            </div>

            <!-- Sprouting Objects Area -->
            <div id="sim4Canvas" class="h-48 rounded-xl bg-slate-950 border border-slate-800/80 p-3 relative flex items-center justify-around overflow-hidden">
                <!-- Rendered by JS -->
            </div>

            <div id="sim4Summary" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed">
                Wood possesses high compressive strength along its grain and easy carveability, enabling structures from furniture to boats.
            </div>
        </div>
    """,

    5: """
        <!-- Simulator 5: Interactive Sorting Station -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🗂️</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Interactive Sorting Station</h3>
                        <p class="text-[11px] text-slate-400">Classify classroom objects by geometric shape</p>
                    </div>
                </div>
                <div class="flex items-center space-x-2">
                    <span id="sim5ScoreBadge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/10 text-amber-300 border border-amber-500/20">0 / 6 Sorted</span>
                    <button onclick="resetSim5()" class="text-xs text-slate-400 hover:text-white underline">Reset</button>
                </div>
            </div>

            <!-- Item Pool -->
            <div id="sim5ItemPool" class="flex flex-wrap gap-2 p-2.5 rounded-xl bg-slate-950 border border-slate-800 min-h-12 items-center">
                <!-- 6 clickable draggable items generated by JS -->
            </div>

            <!-- Sorting Bins -->
            <div class="grid grid-cols-2 gap-3">
                <div id="sim5BinSpherical" onclick="dropSim5Item('spherical')" class="p-3 rounded-xl bg-slate-800/60 border-2 border-dashed border-indigo-500/40 hover:border-indigo-400 transition cursor-pointer min-h-28 flex flex-col">
                    <span class="text-xs font-bold text-indigo-300 flex items-center space-x-1 mb-2">
                        <span>⚽</span><span>Spherical / Round Items</span>
                    </span>
                    <div id="sim5SphericalItems" class="flex flex-wrap gap-1.5 flex-1"></div>
                </div>
                <div id="sim5BinNonSpherical" onclick="dropSim5Item('non-spherical')" class="p-3 rounded-xl bg-slate-800/60 border-2 border-dashed border-emerald-500/40 hover:border-emerald-400 transition cursor-pointer min-h-28 flex flex-col">
                    <span class="text-xs font-bold text-emerald-300 flex items-center space-x-1 mb-2">
                        <span>📦</span><span>Non-Spherical Items</span>
                    </span>
                    <div id="sim5NonSphericalItems" class="flex flex-wrap gap-1.5 flex-1"></div>
                </div>
            </div>
            <p id="sim5Prompt" class="text-xs text-center text-slate-400 italic">Click an object above, then click the correct destination bin.</p>
        </div>
    """,

    6: """
        <!-- Simulator 6: The Tumbler & Bounce Lab (Fit for Purpose) -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🎯</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Purpose & Property Testing Bench</h3>
                        <p class="text-[11px] text-slate-400">Test the cloth tumbler paradox and sports ball rebound heights</p>
                    </div>
                </div>
                <div class="flex space-x-1">
                    <button onclick="setSim6Mode('tumbler')" id="sim6Mode-tumbler" class="px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white">Tumbler Test</button>
                    <button onclick="setSim6Mode('bounce')" id="sim6Mode-bounce" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-400 hover:text-white">Ball Bounce</button>
                </div>
            </div>

            <!-- Dynamic Workspace -->
            <div id="sim6Workspace" class="h-48 rounded-xl bg-slate-950 border border-slate-800 p-4 flex flex-col items-center justify-center relative overflow-hidden">
                <!-- Rendered by JS -->
            </div>

            <!-- Action Controls & Observation -->
            <div id="sim6Controls" class="flex items-center justify-between">
                <!-- Controls rendered by JS -->
            </div>
            <div id="sim6Feedback" class="p-2.5 rounded-lg bg-slate-800/50 border border-slate-700/60 text-xs text-slate-300 leading-relaxed">
                <!-- Live insight -->
            </div>
        </div>
    """,

    7: """
        <!-- Simulator 7: Fresh Cut & Lustre Polish Station -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">✨</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Fresh Cut & Lustre Station</h3>
                        <p class="text-[11px] text-slate-400">Unmask metallic lustre by slicing through oxidized tarnish</p>
                    </div>
                </div>
                <span id="sim7Badge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-300 border border-rose-500/20">Tarnished Outer Layer</span>
            </div>

            <div class="flex items-center space-x-2">
                <button onclick="setSim7Sample('copper')" id="sim7Btn-copper" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-600 text-white transition">Copper Rod</button>
                <button onclick="setSim7Sample('iron')" id="sim7Btn-iron" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Rusted Iron</button>
                <button onclick="setSim7Sample('aluminium')" id="sim7Btn-aluminium" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Aluminium Pipe</button>
            </div>

            <!-- Rod Display Stage -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 flex flex-col items-center justify-center p-4 relative overflow-hidden">
                <div id="sim7RodGraphic" class="relative flex items-center justify-center">
                    <!-- Rod SVG rendered by JS -->
                </div>
                <div id="sim7Sparkles" class="absolute inset-0 pointer-events-none flex items-center justify-center opacity-0 transition-opacity">
                    <span class="text-3xl animate-ping">✨</span>
                </div>
            </div>

            <!-- Action Buttons -->
            <div class="flex items-center justify-between">
                <div class="space-x-2">
                    <button onclick="cutSim7Rod()" class="px-4 py-2 rounded-xl bg-gradient-to-r from-indigo-500 to-sky-600 hover:from-indigo-400 hover:to-sky-500 text-white font-bold text-xs transition shadow-lg">
                        ✂️ Slice with Hacksaw (Reveal Fresh Cut)
                    </button>
                    <button onclick="sandpaperSim7Rod()" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition">
                        🪨 Rub with Sandpaper
                    </button>
                </div>
                <button onclick="resetSim7Rod()" class="text-xs text-slate-400 hover:text-white underline">Re-oxidize</button>
            </div>
            <div id="sim7Status" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed">
                Oxidized outer crust scatters light diffusely. Slice through to observe true specular metallic reflection!
            </div>
        </div>
    """,

    8: """
        <!-- Simulator 8: Light Reflection Analyzer (Lustre vs Dull) -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🔦</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Light Reflection Analyzer</h3>
                        <p class="text-[11px] text-slate-400">Specular beam reflection (metals) vs diffuse scattering (dull non-metals)</p>
                    </div>
                </div>
                <span id="sim8ModeBadge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">Specular Beam</span>
            </div>

            <!-- Material Buttons -->
            <div class="grid grid-cols-3 gap-2">
                <button onclick="setSim8Material('gold')" id="sim8Btn-gold" class="p-2 rounded-xl bg-amber-600 text-white font-bold text-xs">Gold Leaf</button>
                <button onclick="setSim8Material('wood')" id="sim8Btn-wood" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs">Rough Wood</button>
                <button onclick="setSim8Material('varnish')" id="sim8Btn-varnish" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs">Varnished Wood</button>
            </div>

            <!-- Optical Stage -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 flex items-center justify-center p-3 relative overflow-hidden">
                <svg id="sim8Svg" width="340" height="150" viewBox="0 0 340 150">
                    <!-- Flashlight beam and sample rendered by JS -->
                </svg>
            </div>

            <div id="sim8Explanation" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed">
                Gold has an atomic lattice with free conduction electrons that reflect incoming light rays in unison, producing mirror-like metallic lustre.
            </div>
        </div>
    """,

    9: """
        <!-- Simulator 9: Hardness Compression & Scratch Gauge -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🔨</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Compressibility & Scratch Gauge</h3>
                        <p class="text-[11px] text-slate-400">Test relative hardness using mechanical pressure and scratch resistance</p>
                    </div>
                </div>
                <span id="sim9Badge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-300 border border-emerald-500/20">Soft Material</span>
            </div>

            <!-- Material Selector -->
            <div class="grid grid-cols-4 gap-2">
                <button onclick="setSim9Sample('sponge')" id="sim9Btn-sponge" class="p-1.5 rounded-lg bg-indigo-600 text-white font-bold text-xs">Sponge</button>
                <button onclick="setSim9Sample('wax')" id="sim9Btn-wax" class="p-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs">Candle Wax</button>
                <button onclick="setSim9Sample('wood')" id="sim9Btn-wood" class="p-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs">Pine Wood</button>
                <button onclick="setSim9Sample('iron')" id="sim9Btn-iron" class="p-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs">Iron Plate</button>
            </div>

            <!-- Testing Stage -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 flex items-center justify-around p-3 relative">
                <!-- Clamp Graphic -->
                <div id="sim9StageGraphic" class="flex flex-col items-center justify-center">
                    <!-- SVG sample and press rendered by JS -->
                </div>
                <!-- Measurement Readout -->
                <div class="space-y-2 text-xs w-44">
                    <div class="p-2 rounded bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">Compressibility:</span>
                        <span id="sim9CompVal" class="text-emerald-400 font-bold font-mono text-sm">85% (High)</span>
                    </div>
                    <div class="p-2 rounded bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">Scratch by Iron Nail:</span>
                        <span id="sim9ScratchVal" class="text-amber-400 font-bold text-xs">Scratched easily</span>
                    </div>
                </div>
            </div>

            <!-- Controls -->
            <div class="flex items-center space-x-2">
                <button onclick="applySim9Pressure()" class="flex-1 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition shadow-lg">
                    Compress with 50 N Force ✊
                </button>
                <button onclick="scratchSim9Nail()" class="flex-1 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition shadow-lg">
                    Scratch with Iron Nail 💅
                </button>
            </div>
        </div>
    """,

    10: """
        <!-- Simulator 10: Optical Transmission Bench (Transparent) -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🔍</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Transparent Optical Transmission</h3>
                        <p class="text-[11px] text-slate-400">Observe undisturbed, parallel light transmission through transparent media</p>
                    </div>
                </div>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-300 border border-cyan-500/20">99% Transmission</span>
            </div>

            <!-- Medium Switcher -->
            <div class="flex space-x-2">
                <button onclick="setSim10Medium('glass')" id="sim10Btn-glass" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-cyan-600 text-white">Clear Window Glass</button>
                <button onclick="setSim10Medium('water')" id="sim10Btn-water" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300">Clean Water Tank</button>
                <button onclick="setSim10Medium('cellophane')" id="sim10Btn-cellophane" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300">Cellophane Sheet</button>
            </div>

            <!-- Visual Bench -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex items-center justify-between relative overflow-hidden">
                <!-- Viewer Eye -->
                <div class="flex flex-col items-center z-10">
                    <span class="text-2xl">👁️</span>
                    <span class="text-[10px] text-slate-400 font-bold">Observer</span>
                </div>

                <!-- Transparent Barrier -->
                <div id="sim10Barrier" class="w-16 h-32 rounded-lg border-2 border-cyan-400/60 bg-cyan-400/10 backdrop-blur-[0px] flex items-center justify-center relative shadow-lg shadow-cyan-500/10 transition-all">
                    <span class="text-[9px] text-cyan-300 font-bold rotate-90 whitespace-nowrap">Glass Plate</span>
                </div>

                <!-- Object Behind Barrier -->
                <div id="sim10Target" class="flex flex-col items-center transition-all z-10">
                    <span class="text-3xl">🌻</span>
                    <span class="text-[10px] text-emerald-400 font-bold">Crystal Clear View!</span>
                </div>

                <!-- Parallel Rays SVG -->
                <svg class="absolute inset-0 w-full h-full pointer-events-none" viewBox="0 0 400 150">
                    <line x1="70" y1="75" x2="160" y2="75" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,2"/>
                    <line x1="220" y1="75" x2="330" y2="75" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,2"/>
                </svg>
            </div>

            <div class="p-2.5 rounded-lg bg-slate-800/50 border border-slate-700/60 text-xs text-slate-300">
                Light rays travel through in straight parallel paths without internal scattering. The image reaches the retina with full contrast and sharpness.
            </div>
        </div>
    """,

    11: """
        <!-- Simulator 11: Shadow Formation & Opaque Blocker -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🌑</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Opaque Blocker & Shadow Chamber</h3>
                        <p class="text-[11px] text-slate-400">Total optical blockage creates complete occlusion and sharp shadows</p>
                    </div>
                </div>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-rose-500/10 text-rose-300 border border-rose-500/20">0% Light Transmission</span>
            </div>

            <!-- Material Selector -->
            <div class="flex space-x-2">
                <button onclick="setSim11Blocker('cardboard')" id="sim11Btn-cardboard" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-rose-600 text-white">Cardboard Sheet</button>
                <button onclick="setSim11Blocker('wood')" id="sim11Btn-wood" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300">Wooden Board</button>
                <button onclick="setSim11Blocker('metal')" id="sim11Btn-metal" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300">Sheet Metal</button>
            </div>

            <!-- Stage -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex items-center justify-between relative overflow-hidden">
                <!-- Light Torch -->
                <div class="flex flex-col items-center">
                    <span class="text-2xl animate-pulse">🔦</span>
                    <span class="text-[10px] text-amber-300 font-bold">Light Source</span>
                </div>

                <!-- Opaque Barrier -->
                <div id="sim11Barrier" class="w-12 h-32 rounded bg-amber-900 border border-amber-700 shadow-2xl flex items-center justify-center">
                    <span class="text-[9px] text-white font-bold rotate-90 whitespace-nowrap">Cardboard</span>
                </div>

                <!-- Projection Screen with Shadow -->
                <div class="w-24 h-36 bg-slate-800 border-2 border-slate-700 rounded-lg flex items-center justify-center relative overflow-hidden">
                    <div id="sim11Shadow" class="w-12 h-32 bg-black rounded shadow-inner flex items-center justify-center">
                        <span class="text-[9px] text-slate-500 font-mono rotate-90">Dark Shadow</span>
                    </div>
                </div>
            </div>

            <div class="p-2.5 rounded-lg bg-slate-800/50 border border-slate-700/60 text-xs text-slate-300">
                Visible light cannot penetrate dense opaque materials. Rectilinear rays that hit the blocker are absorbed or reflected, forming a dark shadow on the screen behind.
            </div>
        </div>
    """,

    12: """
        <!-- Simulator 12: Frosted Diffuser & Oil Spot (Translucent) -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🌫️</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Translucent Light Diffuser</h3>
                        <p class="text-[11px] text-slate-400">Explore light scattering through butter paper and the classic oil-spot test</p>
                    </div>
                </div>
                <span id="sim12Badge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-300 border border-amber-500/20">Scattered Diffusion</span>
            </div>

            <div class="flex space-x-2">
                <button onclick="setSim12Material('butter')" id="sim12Btn-butter" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-600 text-white">Butter Paper</button>
                <button onclick="setSim12Material('frosted')" id="sim12Btn-frosted" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300">Frosted Glass</button>
                <button onclick="setSim12Material('oilspot')" id="sim12Btn-oilspot" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300">Oil Spot on Paper 🛢️</button>
            </div>

            <!-- View Through Barrier -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex items-center justify-between relative overflow-hidden">
                <div class="flex flex-col items-center z-10">
                    <span class="text-2xl">👁️</span>
                    <span class="text-[10px] text-slate-400 font-bold">Observer</span>
                </div>

                <!-- Translucent Sheet -->
                <div id="sim12Sheet" class="w-20 h-32 rounded-lg bg-amber-100/20 border-2 border-amber-300/40 backdrop-blur-md flex items-center justify-center transition-all">
                    <span id="sim12SheetLabel" class="text-[9px] text-amber-200 font-bold rotate-90 whitespace-nowrap">Butter Paper</span>
                </div>

                <!-- Target Image (Blurry behind sheet) -->
                <div id="sim12Target" class="flex flex-col items-center transition-all z-10 opacity-70 blur-[3px]">
                    <span class="text-3xl">🕯️</span>
                    <span class="text-[10px] text-amber-300 font-bold">Hazy Outline!</span>
                </div>
            </div>

            <!-- Blur / Diffusion Slider -->
            <div class="space-y-1">
                <div class="flex justify-between text-xs text-slate-400">
                    <span>Diffusion Scattering Level:</span>
                    <span id="sim12ScatterVal" class="text-amber-400 font-bold">Medium (Blurry)</span>
                </div>
                <input type="range" id="sim12Slider" min="1" max="10" value="5" oninput="adjustSim12Blur(this.value)" class="w-full accent-amber-500 cursor-pointer">
            </div>
        </div>
    """,

    13: """
        <!-- Simulator 13: Beaker Dissolution Lab (Soluble vs Insoluble) -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🧪</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Beaker Dissolution Lab</h3>
                        <p class="text-[11px] text-slate-400">Stir various powders into water to observe true solutions vs settling sediments</p>
                    </div>
                </div>
                <span id="sim13StatusBadge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-300 border border-emerald-500/20">Soluble Substance</span>
            </div>

            <!-- Solute Selector -->
            <div class="grid grid-cols-4 gap-2">
                <button onclick="setSim13Solute('sugar')" id="sim13Btn-sugar" class="p-1.5 rounded-lg bg-emerald-600 text-white font-bold text-xs">Sugar</button>
                <button onclick="setSim13Solute('salt')" id="sim13Btn-salt" class="p-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs">Table Salt</button>
                <button onclick="setSim13Solute('sand')" id="sim13Btn-sand" class="p-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs">River Sand</button>
                <button onclick="setSim13Solute('chalk')" id="sim13Btn-chalk" class="p-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs">Chalk Powder</button>
            </div>

            <!-- Beaker Stage -->
            <div class="h-44 rounded-xl bg-slate-950 border border-slate-800 flex items-center justify-around p-3 relative overflow-hidden">
                <div id="sim13BeakerGraphic" class="relative">
                    <!-- Beaker SVG rendered by JS -->
                </div>
                <div class="space-y-2 text-xs w-44">
                    <div class="p-2 rounded bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">Resulting Mixture:</span>
                        <span id="sim13MixType" class="text-emerald-400 font-bold">Clear Homogeneous Solution</span>
                    </div>
                    <div class="p-2 rounded bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">Sedimentation:</span>
                        <span id="sim13SedimentVal" class="text-slate-300 font-semibold">Zero (Completely Dissolved)</span>
                    </div>
                </div>
            </div>

            <button onclick="stirSim13()" id="sim13StirBtn" class="w-full py-2 rounded-xl bg-gradient-to-r from-cyan-500 to-indigo-600 hover:from-cyan-400 hover:to-indigo-500 text-white font-bold text-xs transition shadow-lg">
                🥄 Add Powder & Stir Vigorously (30 Seconds)
            </button>
        </div>
    """,

    14: """
        <!-- Simulator 14: Liquid Stratification & ORS Formulator -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🍶</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Liquid Mixing & ORS Formulator</h3>
                        <p class="text-[11px] text-slate-400">Test liquid miscibility and formulate life-saving Oral Rehydration Solution</p>
                    </div>
                </div>
                <div class="flex space-x-1">
                    <button onclick="setSim14Mode('miscible')" id="sim14Mode-miscible" class="px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white">Oil & Water</button>
                    <button onclick="setSim14Mode('ors')" id="sim14Mode-ors" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-400 hover:text-white">Prepare ORS 💧</button>
                </div>
            </div>

            <!-- Workspace -->
            <div id="sim14Workspace" class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex items-center justify-around relative">
                <!-- Rendered by JS -->
            </div>

            <!-- Controls -->
            <div id="sim14Controls" class="space-y-2">
                <!-- Rendered by JS -->
            </div>
            <div id="sim14Feedback" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed">
                Oil molecules are hydrophobic and non-polar; their lower density forces them into a separate floating layer above water.
            </div>
        </div>
    """,

    15: """
        <!-- Simulator 15: Dual-Pan Balance & Water Displacement Lab -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">⚖️</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Mass & Volume Measurement Lab</h3>
                        <p class="text-[11px] text-slate-400">Dual-pan beam balance for mass and graduated cylinder for volume</p>
                    </div>
                </div>
                <div class="flex space-x-1">
                    <button onclick="setSim15Tool('balance')" id="sim15Tool-balance" class="px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white">Dual-Pan Mass</button>
                    <button onclick="setSim15Tool('volume')" id="sim15Tool-volume" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-400 hover:text-white">Displaced Volume</button>
                </div>
            </div>

            <!-- Stage -->
            <div id="sim15Stage" class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex items-center justify-center relative overflow-hidden">
                <!-- Rendered by JS -->
            </div>

            <!-- Action Controls -->
            <div id="sim15Controls" class="flex items-center justify-between">
                <!-- Controls rendered by JS -->
            </div>
            <div id="sim15Insight" class="text-xs text-slate-300 bg-slate-800/50 p-2.5 rounded-xl border border-slate-700/60 leading-relaxed">
                Equal volumes of different materials possess vastly different masses due to intrinsic density differences.
            </div>
        </div>
    """,

    16: """
        <!-- Simulator 16: Matter Classifier & Ayurvedic Gunas Matrix -->
        <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800/80 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <span class="text-xl">🌌</span>
                    <div>
                        <h3 class="text-sm font-bold text-white">Matter Classifier & Ayurvedic Guna Matrix</h3>
                        <p class="text-[11px] text-slate-400">Sort reality into Matter vs Non-Matter and explore Ashtanga Hridaya gunas</p>
                    </div>
                </div>
                <div class="flex space-x-1">
                    <button onclick="setSim16Tab('matter')" id="sim16Tab-matter" class="px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white">Matter vs Energy</button>
                    <button onclick="setSim16Tab('gunas')" id="sim16Tab-gunas" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-400 hover:text-white">20 Gunas Matrix 📜</button>
                </div>
            </div>

            <!-- Display Area -->
            <div id="sim16Workspace" class="h-44 rounded-xl bg-slate-950 border border-slate-800 p-3 flex flex-col justify-between overflow-y-auto custom-scrollbar">
                <!-- Rendered by JS -->
            </div>

            <div id="sim16BottomBar" class="flex items-center justify-between text-xs">
                <!-- Action / status rendered by JS -->
            </div>
        </div>
    """
}

