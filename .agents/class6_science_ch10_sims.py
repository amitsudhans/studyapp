"""
Class 6 Science Chapter 10: Living Creatures: Exploring their Characteristics
16 Bespoke Interactive SVG/HTML Simulators
Zero raw LaTeX. Pure clean Unicode.
"""

SIMULATORS = {
    1: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Snail Shell vs. Living Snail Explorer</span>
            <span id="sim1-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-300">Viewing: Empty Shell</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg id="sim1-svg" class="w-full h-full" viewBox="0 0 320 200">
                <defs>
                    <radialGradient id="shellGrad" cx="40%" cy="40%" r="60%">
                        <stop offset="0%" stop-color="#d97706" />
                        <stop offset="50%" stop-color="#b45309" />
                        <stop offset="100%" stop-color="#78350f" />
                    </radialGradient>
                    <linearGradient id="snailBodyGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#a3e635" />
                        <stop offset="100%" stop-color="#65a30d" />
                    </linearGradient>
                </defs>
                <!-- Garden Soil & Blade of Grass -->
                <rect x="0" y="160" width="320" height="40" fill="#292524" />
                <path d="M 30,160 Q 40,120 60,110 Q 50,135 45,160 Z" fill="#15803d" opacity="0.6" />
                <path d="M 270,160 Q 260,130 240,120 Q 255,140 260,160 Z" fill="#16a34a" opacity="0.6" />

                <!-- Living Snail Body (Initially Hidden) -->
                <g id="sim1-snail-body" style="opacity: 0; transition: all 0.5s ease;">
                    <!-- Slime trail -->
                    <path d="M 60,162 L 200,162" stroke="#67e8f9" stroke-width="4" stroke-linecap="round" opacity="0.5" />
                    <!-- Muscular Foot -->
                    <path d="M 90,160 Q 150,150 210,160 Q 220,162 215,155 Q 200,140 180,140 Q 140,145 100,145 Q 85,150 90,160 Z" fill="url(#snailBodyGrad)" />
                    <!-- Head & Eye Tentacles -->
                    <path d="M 180,140 Q 205,120 215,110" stroke="#84cc16" stroke-width="5" stroke-linecap="round" fill="none" />
                    <circle cx="215" cy="110" r="4" fill="#1e293b" />
                    <circle cx="216" cy="109" r="1.5" fill="#ffffff" />
                    <!-- Lower sensory tentacles -->
                    <path d="M 190,143 Q 205,135 212,130" stroke="#84cc16" stroke-width="3" stroke-linecap="round" fill="none" />
                    <circle cx="212" cy="130" r="2.5" fill="#1e293b" />
                </g>

                <!-- Spiral Shell -->
                <g id="sim1-shell" transform="translate(130, 125)">
                    <!-- Outer spiral whorls -->
                    <ellipse cx="0" cy="0" rx="42" ry="32" fill="url(#shellGrad)" stroke="#451a03" stroke-width="2" />
                    <ellipse cx="-5" cy="-2" rx="30" ry="22" fill="#d97706" opacity="0.7" stroke="#451a03" stroke-width="1.5" />
                    <ellipse cx="-10" cy="-4" rx="18" ry="13" fill="#f59e0b" opacity="0.8" stroke="#451a03" stroke-width="1" />
                    <circle cx="-14" cy="-5" r="7" fill="#fbbf24" stroke="#451a03" stroke-width="1" />
                    <!-- Texture ribs -->
                    <path d="M 10,-25 Q 18,0 12,25" stroke="#78350f" stroke-width="1.5" fill="none" opacity="0.6" />
                    <path d="M -8,-20 Q -2,0 -6,18" stroke="#78350f" stroke-width="1.5" fill="none" opacity="0.6" />
                </g>

                <!-- Status Text Badge Inside SVG -->
                <rect x="15" y="15" width="160" height="32" rx="8" fill="#0f172a" fill-opacity="0.85" stroke="#334155" />
                <text id="sim1-svg-text" x="25" y="36" fill="#94a3b8" font-size="11" font-weight="bold">Empty Shell: Lifeless</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setSnailState('empty')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700 transition">
                🐚 Empty Shell (Non-Living)
            </button>
            <button onclick="setSnailState('living')" class="p-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-bold text-white shadow transition">
                🐌 Living Snail (Awakens)
            </button>
        </div>
        <div id="sim1-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Click <strong>Living Snail</strong> to watch the organism emerge from its protective shell, extend sensory eye tentacles, and crawl forward.
        </div>
    </div>
    """,

    2: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Drosera Sundew Carnivorous Trap</span>
            <span id="sim2-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Trap Primed</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg id="sim2-svg" class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                <!-- Leaf Base -->
                <path d="M 40,150 Q 160,170 280,150 Q 200,120 40,150 Z" fill="#14532d" stroke="#166534" stroke-width="2" />
                
                <!-- Glandular Tentacles Left -->
                <g id="tentacles-left" style="transition: all 0.6s ease; transform-origin: 100px 140px;">
                    <path d="M 80,140 Q 60,100 70,80" stroke="#dc2626" stroke-width="3" fill="none" />
                    <circle cx="70" cy="80" r="5" fill="#f43f5e" opacity="0.9" />
                    <circle cx="70" cy="80" r="2" fill="#ffffff" />
                    <path d="M 105,140 Q 90,95 100,70" stroke="#dc2626" stroke-width="3" fill="none" />
                    <circle cx="100" cy="70" r="5" fill="#f43f5e" opacity="0.9" />
                    <circle cx="100" cy="70" r="2" fill="#ffffff" />
                </g>

                <!-- Center Glands -->
                <path d="M 140,140 Q 140,90 145,65" stroke="#dc2626" stroke-width="3" fill="none" />
                <circle cx="145" cy="65" r="5" fill="#f43f5e" opacity="0.9" />
                <circle cx="145" cy="65" r="2" fill="#ffffff" />

                <path d="M 175,140 Q 180,90 175,65" stroke="#dc2626" stroke-width="3" fill="none" />
                <circle cx="175" cy="65" r="5" fill="#f43f5e" opacity="0.9" />
                <circle cx="175" cy="65" r="2" fill="#ffffff" />

                <!-- Glandular Tentacles Right -->
                <g id="tentacles-right" style="transition: all 0.6s ease; transform-origin: 220px 140px;">
                    <path d="M 215,140 Q 230,95 220,70" stroke="#dc2626" stroke-width="3" fill="none" />
                    <circle cx="220" cy="70" r="5" fill="#f43f5e" opacity="0.9" />
                    <circle cx="220" cy="70" r="2" fill="#ffffff" />
                    <path d="M 240,140 Q 260,100 250,80" stroke="#dc2626" stroke-width="3" fill="none" />
                    <circle cx="250" cy="80" r="5" fill="#f43f5e" opacity="0.9" />
                    <circle cx="250" cy="80" r="2" fill="#ffffff" />
                </g>

                <!-- Flying Insect (Fly) -->
                <g id="sim2-fly" style="transition: all 0.7s cubic-bezier(0.25, 1, 0.5, 1); transform: translate(160px, 20px);">
                    <!-- Insect Body -->
                    <ellipse cx="0" cy="0" rx="8" ry="5" fill="#1e293b" />
                    <circle cx="6" cy="-1" r="3" fill="#0f172a" />
                    <circle cx="7" cy="-2" r="1.5" fill="#ef4444" />
                    <!-- Wings -->
                    <ellipse cx="-2" cy="-6" rx="9" ry="3.5" fill="#93c5fd" opacity="0.6" transform="rotate(-20)" />
                    <ellipse cx="-2" cy="6" rx="9" ry="3.5" fill="#93c5fd" opacity="0.6" transform="rotate(20)" />
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="triggerDroseraTrap()" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                🪰 Insect Lands on Leaf
            </button>
            <button onclick="resetDroseraTrap()" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700 transition">
                🔄 Reset Trap
            </button>
        </div>
        <div id="sim2-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Click <strong>Insect Lands</strong> to see the fly adhere to sticky glandular mucilage, triggering rapid inward curling of sensory tentacles.
        </div>
    </div>
    """,

    3: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Microscopic Leaf Stoma Simulator</span>
            <span id="sim3-status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Day: Stoma Open</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg id="sim3-svg" class="w-full h-full" viewBox="0 0 320 200">
                <!-- Epidermal Cells Background -->
                <rect x="0" y="0" width="320" height="200" fill="#052e16" />
                <path d="M 0,40 Q 60,30 110,50 L 110,150 Q 50,170 0,160 Z" fill="#14532d" stroke="#166534" stroke-width="2" />
                <path d="M 210,50 Q 260,30 320,40 L 320,160 Q 270,170 210,150 Z" fill="#14532d" stroke="#166534" stroke-width="2" />
                
                <!-- Left Guard Cell -->
                <path id="guard-left" d="M 160,35 C 110,40 100,160 160,165 C 130,140 130,60 160,35 Z" fill="#22c55e" stroke="#15803d" stroke-width="3" style="transition: all 0.5s ease;" />
                <!-- Right Guard Cell -->
                <path id="guard-right" d="M 160,35 C 210,40 220,160 160,165 C 190,140 190,60 160,35 Z" fill="#22c55e" stroke="#15803d" stroke-width="3" style="transition: all 0.5s ease;" />

                <!-- Chloroplasts inside Guard Cells -->
                <circle cx="125" cy="80" r="4" fill="#15803d" />
                <circle cx="120" cy="110" r="4" fill="#15803d" />
                <circle cx="130" cy="135" r="4" fill="#15803d" />
                <circle cx="195" cy="80" r="4" fill="#15803d" />
                <circle cx="200" cy="110" r="4" fill="#15803d" />
                <circle cx="190" cy="135" r="4" fill="#15803d" />

                <!-- Stomatal Aperture (The Pore) -->
                <ellipse id="stoma-pore" cx="160" cy="100" rx="18" ry="45" fill="#022c22" stroke="#064e3b" stroke-width="2" style="transition: all 0.5s ease;" />

                <!-- Gas Molecules Arrows (O2 / CO2) -->
                <g id="gas-arrows" style="transition: opacity 0.5s ease; opacity: 1;">
                    <path d="M 160,70 L 160,40 M 156,48 L 160,40 L 164,48" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" />
                    <text x="170" y="55" fill="#38bdf8" font-size="10" font-weight="bold">O₂</text>
                    <path d="M 160,130 L 160,160 M 156,152 L 160,160 L 164,152" stroke="#a78bfa" stroke-width="2" stroke-linecap="round" />
                    <text x="170" y="150" fill="#a78bfa" font-size="10" font-weight="bold">CO₂</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setStomaState(true)" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                ☀️ Daytime (High Turgor / Open)
            </button>
            <button onclick="setStomaState(false)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700 transition">
                🌙 Night (Low Turgor / Closed)
            </button>
        </div>
        <div id="sim3-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Kidney-shaped guard cells swell with water to open the central pore for O₂ and CO₂ exchange, and shrink to close it, preventing water loss.
        </div>
    </div>
    """,

    4: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Plant Guttation Excretion Simulator</span>
            <span id="sim4-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Early Dawn: Guttation Active</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#040d1a" />
                <!-- Strawberry/Rose Leaf Silhouette -->
                <path d="M 160,180 C 120,160 50,130 60,70 C 80,40 130,50 160,25 C 190,50 240,40 260,70 C 270,130 200,160 160,180 Z" fill="#15803d" stroke="#22c55e" stroke-width="2" />
                <!-- Leaf Central Vein -->
                <path d="M 160,180 Q 160,90 160,25" stroke="#86efac" stroke-width="3" fill="none" opacity="0.7" />
                <path d="M 160,130 Q 120,110 85,100" stroke="#86efac" stroke-width="1.5" fill="none" opacity="0.6" />
                <path d="M 160,130 Q 200,110 235,100" stroke="#86efac" stroke-width="1.5" fill="none" opacity="0.6" />
                <path d="M 160,85 Q 120,65 95,55" stroke="#86efac" stroke-width="1.5" fill="none" opacity="0.6" />
                <path d="M 160,85 Q 200,65 225,55" stroke="#86efac" stroke-width="1.5" fill="none" opacity="0.6" />

                <!-- Guttation Droplets at Leaf Margin Hydathodes -->
                <g id="sim4-droplets" style="transition: all 0.5s ease; opacity: 1;">
                    <circle cx="160" cy="22" r="5" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" />
                    <circle cx="85" cy="52" r="4.5" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" />
                    <circle cx="235" cy="52" r="4.5" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" />
                    <circle cx="62" cy="85" r="4" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" />
                    <circle cx="258" cy="85" r="4" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" />
                    <circle cx="80" cy="125" r="4.5" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" />
                    <circle cx="240" cy="125" r="4.5" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" />
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="toggleGuttation(true)" class="p-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-xs font-bold text-white shadow transition">
                💧 High Root Pressure (Dawn Guttation)
            </button>
            <button onclick="toggleGuttation(false)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700 transition">
                ☀️ Midday Heat (Transpiration Only)
            </button>
        </div>
        <div id="sim4-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            During humid dawn hours, root pressure forces excess water and dissolved mineral salts out through leaf hydathodes as glistening guttation droplets.
        </div>
    </div>
    """,

    5: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Touch-Me-Not (Mimosa pudica) Stimulus Lab</span>
            <span id="sim5-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Leaflets Open</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden cursor-pointer" onclick="touchMimosa()">
            <svg id="sim5-svg" class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                <!-- Stem & Pulvinus Base -->
                <path d="M 40,160 Q 100,150 140,135" stroke="#15803d" stroke-width="4" fill="none" />
                <!-- Swollen Pulvinus Hinge -->
                <ellipse id="sim5-pulvinus" cx="140" cy="135" rx="8" ry="6" fill="#84cc16" stroke="#4d7c0f" stroke-width="1.5" />
                
                <!-- Main Rachis Stalk (Droops on Touch) -->
                <g id="sim5-branch" style="transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); transform-origin: 140px 135px; transform: rotate(0deg);">
                    <path d="M 140,135 L 260,110" stroke="#16a34a" stroke-width="3" fill="none" />
                    
                    <!-- Left Leaflets Pair 1 -->
                    <g class="mimosa-pair" style="transition: all 0.3s ease; transform-origin: 170px 128px;">
                        <ellipse class="m-leaf-top" cx="165" cy="115" rx="12" ry="4" fill="#22c55e" stroke="#15803d" stroke-width="1" transform="rotate(-30 165 115)" />
                        <ellipse class="m-leaf-bot" cx="172" cy="140" rx="12" ry="4" fill="#22c55e" stroke="#15803d" stroke-width="1" transform="rotate(30 172 140)" />
                    </g>
                    <!-- Leaflets Pair 2 -->
                    <g class="mimosa-pair" style="transition: all 0.3s ease; transform-origin: 200px 122px;">
                        <ellipse class="m-leaf-top" cx="195" cy="110" rx="12" ry="4" fill="#22c55e" stroke="#15803d" stroke-width="1" transform="rotate(-30 195 110)" />
                        <ellipse class="m-leaf-bot" cx="202" cy="135" rx="12" ry="4" fill="#22c55e" stroke="#15803d" stroke-width="1" transform="rotate(30 202 135)" />
                    </g>
                    <!-- Leaflets Pair 3 -->
                    <g class="mimosa-pair" style="transition: all 0.3s ease; transform-origin: 230px 116px;">
                        <ellipse class="m-leaf-top" cx="225" cy="103" rx="12" ry="4" fill="#22c55e" stroke="#15803d" stroke-width="1" transform="rotate(-30 225 103)" />
                        <ellipse class="m-leaf-bot" cx="232" cy="128" rx="12" ry="4" fill="#22c55e" stroke="#15803d" stroke-width="1" transform="rotate(30 232 128)" />
                    </g>
                </g>

                <!-- Touch Indicator Finger -->
                <text x="20" y="30" fill="#94a3b8" font-size="11" font-weight="bold">👉 Tap anywhere on the leaf to touch it!</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="touchMimosa()" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                👆 Touch Leaf (Trigger Stimulus)
            </button>
            <button onclick="recoverMimosa()" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700 transition">
                🌱 Restore Turgor (10 mins later)
            </button>
        </div>
        <div id="sim5-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Physical touch triggers sudden potassium efflux and water discharge from pulvinus cells, collapsing turgor and folding the leaflets together.
        </div>
    </div>
    """,

    6: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Reproduction & Continuity of Life</span>
            <span id="sim6-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Mode: Seed to Plant</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg id="sim6-svg" class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                <!-- Stage 1 (Parent Generation) -->
                <g id="sim6-parent" transform="translate(60, 100)">
                    <circle cx="0" cy="0" r="30" fill="#1e293b" stroke="#3b82f6" stroke-width="2" />
                    <text id="sim6-p-icon" x="-12" y="8" font-size="24">🌳</text>
                    <text id="sim6-p-label" x="0" y="45" fill="#94a3b8" font-size="10" text-anchor="middle" font-weight="bold">Parent Tree</text>
                </g>

                <!-- Flow Arrow -->
                <path d="M 105,100 L 145,100 M 138,94 L 145,100 L 138,106" stroke="#6366f1" stroke-width="3" stroke-linecap="round" />

                <!-- Stage 2 (Reproductive Vehicle: Seed / Egg / Fetus) -->
                <g id="sim6-vehicle" transform="translate(180, 100)">
                    <circle cx="0" cy="0" r="22" fill="#1e293b" stroke="#f59e0b" stroke-width="2" />
                    <text id="sim6-v-icon" x="-9" y="7" font-size="18">🌰</text>
                    <text id="sim6-v-label" x="0" y="38" fill="#f59e0b" font-size="10" text-anchor="middle" font-weight="bold">Fruit Seed</text>
                </g>

                <!-- Flow Arrow -->
                <path d="M 215,100 L 245,100 M 238,94 L 245,100 L 238,106" stroke="#6366f1" stroke-width="3" stroke-linecap="round" />

                <!-- Stage 3 (Offspring Generation) -->
                <g id="sim6-child" transform="translate(280, 100)">
                    <circle cx="0" cy="0" r="26" fill="#1e293b" stroke="#10b981" stroke-width="2" />
                    <text id="sim6-c-icon" x="-11" y="8" font-size="20">🌱</text>
                    <text id="sim6-c-label" x="0" y="42" fill="#10b981" font-size="10" text-anchor="middle" font-weight="bold">Sapling</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="setReproMode('plant')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-200 border border-slate-700 transition">
                🌲 Plant (Seeds)
            </button>
            <button onclick="setReproMode('bird')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-200 border border-slate-700 transition">
                🦅 Bird (Eggs)
            </button>
            <button onclick="setReproMode('mammal')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-200 border border-slate-700 transition">
                🐘 Mammal (Birth)
            </button>
        </div>
        <div id="sim6-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Reproduction ensures that as individuals reach their natural lifespan and perish, the species continues across generations.
        </div>
    </div>
    """,

    7: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Activity 10.2: Seed Germination Incubator</span>
            <span id="sim7-status-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Conditions Incomplete</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <!-- Petri Dish Base -->
                <ellipse cx="160" cy="140" rx="100" ry="40" fill="#1e293b" stroke="#334155" stroke-width="3" />
                <ellipse id="sim7-water-layer" cx="160" cy="140" rx="94" ry="36" fill="#0284c7" opacity="0" style="transition: opacity 0.5s ease;" />
                
                <!-- Gram Seed -->
                <g id="sim7-seed" transform="translate(160, 130)" style="transition: all 0.5s ease;">
                    <ellipse cx="0" cy="0" rx="18" ry="14" fill="#92400e" stroke="#78350f" stroke-width="2" />
                    <circle cx="-5" cy="-2" r="2.5" fill="#fde68a" />
                    <!-- Radicle Sprout (Hidden Initially) -->
                    <path id="sim7-radicle" d="M -5,-2 Q -15,10 -18,28" stroke="#fef08a" stroke-width="4" stroke-linecap="round" fill="none" opacity="0" style="transition: opacity 0.5s ease;" />
                    <path id="sim7-plumule" d="M -5,-2 Q 5,-20 8,-35" stroke="#4ade80" stroke-width="3.5" stroke-linecap="round" fill="none" opacity="0" style="transition: opacity 0.5s ease;" />
                </g>

                <!-- Status Overlay Text -->
                <rect x="20" y="15" width="280" height="28" rx="6" fill="#0f172a" fill-opacity="0.85" stroke="#334155" />
                <text id="sim7-overlay-text" x="160" y="33" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">Missing Water & Warmth</text>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button id="sim7-btn-water" onclick="toggleSim7Condition('water')" class="p-1.5 rounded-lg bg-slate-900 border border-slate-700 text-[11px] font-bold text-slate-300">
                💧 Water: OFF
            </button>
            <button id="sim7-btn-air" onclick="toggleSim7Condition('air')" class="p-1.5 rounded-lg bg-emerald-950 border border-emerald-500/50 text-[11px] font-bold text-emerald-300">
                💨 Air: ON
            </button>
            <button id="sim7-btn-temp" onclick="toggleSim7Condition('temp')" class="p-1.5 rounded-lg bg-slate-900 border border-slate-700 text-[11px] font-bold text-slate-300">
                🌡️ Warmth: OFF
            </button>
        </div>
        <div id="sim7-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Toggle all 3 essential parameters (Water, Air, and Warmth) to ON to activate enzymatic respiration and sprout the bean seed!
        </div>
    </div>
    """,

    8: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Water Imbibition & Seed Coat Rupture</span>
            <span id="sim8-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-800 text-slate-300">Dry Dormant Seed</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <!-- Water Beaker -->
                <path d="M 90,40 L 90,170 Q 90,180 100,180 L 220,180 Q 230,180 230,170 L 230,40" stroke="#475569" stroke-width="3" fill="#0f172a" />
                <rect id="sim8-water-fill" x="92" y="100" width="136" height="78" fill="#0284c7" opacity="0.3" style="transition: all 0.6s ease;" />
                
                <!-- Swelling Seed -->
                <g id="sim8-seed-scale" transform="translate(160, 140) scale(1)" style="transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);">
                    <!-- Testa (Seed Coat) -->
                    <ellipse cx="0" cy="0" rx="20" ry="15" fill="#78350f" stroke="#451a03" stroke-width="2" />
                    <!-- Cotyledon visible inside crack -->
                    <path id="sim8-crack" d="M -5,-15 Q 0,0 8,15" stroke="#fef08a" stroke-width="3" opacity="0" style="transition: opacity 0.5s ease;" />
                    <!-- Micropyle -->
                    <circle cx="-12" cy="0" r="2" fill="#ffffff" />
                </g>
                <text x="160" y="25" fill="#94a3b8" font-size="11" font-weight="bold" text-anchor="middle">Water Absorption via Micropyle</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="soakSeed(true)" class="p-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-xs font-bold text-white shadow transition">
                💧 Soak Seed Overnight
            </button>
            <button onclick="soakSeed(false)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700 transition">
                🏜️ Keep Dry
            </button>
        </div>
        <div id="sim8-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Water enters through the micropyle, swelling hydrophilic starch colloids, doubling volume, and splitting the tough testa to liberate the embryo.
        </div>
    </div>
    """,

    9: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Soil Aeration vs. Waterlogging Hazard</span>
            <span id="sim9-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Soil Well-Aerated</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#1c1917" />
                
                <!-- Soil Particles -->
                <circle cx="50" cy="60" r="24" fill="#44403c" />
                <circle cx="100" cy="50" r="28" fill="#57534e" />
                <circle cx="160" cy="65" r="25" fill="#44403c" />
                <circle cx="220" cy="55" r="27" fill="#57534e" />
                <circle cx="270" cy="65" r="22" fill="#44403c" />

                <circle cx="60" cy="140" r="26" fill="#57534e" />
                <circle cx="120" cy="150" r="25" fill="#44403c" />
                <circle cx="180" cy="140" r="29" fill="#57534e" />
                <circle cx="240" cy="150" r="24" fill="#44403c" />

                <!-- Waterlogged Layer (Hidden in Aerated Mode) -->
                <rect id="sim9-flood" x="0" y="0" width="320" height="200" fill="#0369a1" opacity="0" style="transition: opacity 0.6s ease;" />

                <!-- Plant Root Growing into Soil Pore -->
                <path d="M 160,0 Q 155,50 145,95 Q 140,125 150,170" stroke="#fde047" stroke-width="4.5" fill="none" />
                <path d="M 145,95 Q 110,110 80,120" stroke="#fde047" stroke-width="2.5" fill="none" />
                <path d="M 148,130 Q 185,145 210,155" stroke="#fde047" stroke-width="2.5" fill="none" />

                <!-- Air Pockets with O2 Indicators -->
                <g id="sim9-air-bubbles" style="transition: opacity 0.5s ease; opacity: 1;">
                    <circle cx="110" cy="100" r="12" fill="#0284c7" opacity="0.4" stroke="#38bdf8" stroke-width="1.5" />
                    <text x="110" y="104" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">O₂</text>
                    <circle cx="190" cy="100" r="12" fill="#0284c7" opacity="0.4" stroke="#38bdf8" stroke-width="1.5" />
                    <text x="190" y="104" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">O₂</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setSoilAeration(true)" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow transition">
                💨 Loose Aerated Soil (Oxygen Rich)
            </button>
            <button onclick="setSoilAeration(false)" class="p-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-xs font-bold text-white shadow transition">
                🌊 Flood Soil (Waterlogged / Hypoxia)
            </button>
        </div>
        <div id="sim9-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Oxygen trapped in soil pores sustains root cellular respiration. Flooding displaces this oxygen, suffocating the root system.
        </div>
    </div>
    """,

    10: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Light vs. Dark Seedling Development</span>
            <span id="sim10-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Sunlit Window: Healthy</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <!-- Background Chamber (Light or Dark) -->
                <rect id="sim10-bg" x="0" y="0" width="320" height="200" fill="#0f172a" style="transition: fill 0.5s ease;" />
                
                <!-- Sun Icon in Light Mode -->
                <g id="sim10-sun" transform="translate(260, 40)" style="transition: opacity 0.5s ease; opacity: 1;">
                    <circle cx="0" cy="0" r="16" fill="#f59e0b" />
                    <path d="M 0,-24 L 0,-18 M 0,24 L 0,18 M -24,0 L -18,0 M 24,0 L 18,0" stroke="#fbbf24" stroke-width="2" />
                </g>

                <!-- Soil Pot -->
                <path d="M 120,150 L 130,195 L 190,195 L 200,150 Z" fill="#78350f" stroke="#451a03" stroke-width="2" />
                <ellipse cx="160" cy="150" rx="40" ry="8" fill="#451a03" />

                <!-- Sprouted Seedling (Altered by Environment) -->
                <!-- Healthy Stem -->
                <path id="sim10-stem" d="M 160,145 Q 160,110 160,85" stroke="#16a34a" stroke-width="5" stroke-linecap="round" fill="none" style="transition: all 0.5s ease;" />
                <!-- Leaves -->
                <g id="sim10-leaves" transform="translate(160, 85)" style="transition: all 0.5s ease;">
                    <ellipse id="sim10-leaf-l" cx="-14" cy="-5" rx="14" ry="7" fill="#22c55e" stroke="#15803d" stroke-width="1.5" transform="rotate(-20 -14 -5)" />
                    <ellipse id="sim10-leaf-r" cx="14" cy="-5" rx="14" ry="7" fill="#22c55e" stroke="#15803d" stroke-width="1.5" transform="rotate(20 14 -5)" />
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="setLightEnvironment(true)" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                ☀️ Sunlit Window (Photosynthesis Active)
            </button>
            <button onclick="setLightEnvironment(false)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700 transition">
                📦 Dark Cupboard (Etiolated & Pale)
            </button>
        </div>
        <div id="sim10-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            In total darkness, seedlings germinate but grow pale, spindly, and etiolated; sunlight is essential to trigger chlorophyll synthesis and self-sustaining growth.
        </div>
    </div>
    """,

    11: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Activity 10.3: Geotropism & Phototropism</span>
            <span id="sim11-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Orientation: Upright</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                
                <!-- Sun Light Source Top Right -->
                <circle cx="280" cy="30" r="14" fill="#eab308" />
                <path d="M 280,30 L 220,70" stroke="#fef08a" stroke-width="1" stroke-dasharray="3,3" />

                <!-- Plant & Pot Assembly -->
                <g id="sim11-plant-group" style="transition: transform 0.6s ease; transform-origin: 160px 150px; transform: rotate(0deg);">
                    <!-- The Pot -->
                    <path d="M 130,120 L 140,165 L 180,165 L 190,120 Z" fill="#b45309" stroke="#78350f" stroke-width="2" />
                    <!-- Roots (Positive Geotropism) -->
                    <path id="sim11-root" d="M 160,160 Q 160,180 160,195" stroke="#fde047" stroke-width="3.5" stroke-linecap="round" fill="none" style="transition: all 0.6s ease;" />
                    <!-- Shoot (Positive Phototropism) -->
                    <path id="sim11-shoot" d="M 160,120 Q 160,80 160,50" stroke="#22c55e" stroke-width="4.5" stroke-linecap="round" fill="none" style="transition: all 0.6s ease;" />
                    <!-- Leaves -->
                    <ellipse id="sim11-leaf1" cx="150" cy="50" rx="10" ry="5" fill="#4ade80" />
                    <ellipse id="sim11-leaf2" cx="170" cy="50" rx="10" ry="5" fill="#4ade80" />
                </g>
                <text x="20" y="25" fill="#94a3b8" font-size="11" font-weight="bold">Gravity Pull: ⬇ Down</text>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="tiltPlantPot(false)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700 transition">
                🪴 Upright Position
            </button>
            <button onclick="tiltPlantPot(true)" class="p-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-bold text-white shadow transition">
                🔄 Turn Pot Sideways (90°)
            </button>
        </div>
        <div id="sim11-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            When turned on its side, the root curves downward toward gravity (positive geotropism) while the shoot curves upward toward the sun (positive phototropism).
        </div>
    </div>
    """,

    12: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Sir J.C. Bose's Crescograph Simulator</span>
            <span id="sim12-status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Magnification: 10,000×</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#030712" />
                
                <!-- Smoked Glass Recording Plate Screen -->
                <rect x="20" y="20" width="180" height="160" rx="8" fill="#0f172a" stroke="#334155" stroke-width="2" />
                <path d="M 20,100 L 200,100" stroke="#1e293b" stroke-width="1" stroke-dasharray="2,2" />
                
                <!-- Real-time Oscillating Wave Trace Line -->
                <path id="sim12-trace-wave" d="M 20,100 Q 50,90 80,100 T 140,100 T 200,100" stroke="#38bdf8" stroke-width="2.5" fill="none" style="transition: all 0.4s ease;" />

                <!-- Optical Needle Pointer Dial -->
                <g transform="translate(260, 100)">
                    <circle cx="0" cy="0" r="42" fill="#1e293b" stroke="#6366f1" stroke-width="2.5" />
                    <!-- Dial Ticks -->
                    <path d="M 0,-36 L 0,-30 M 0,36 L 0,30 M -36,0 L -30,0 M 36,0 L 30,0" stroke="#94a3b8" stroke-width="1.5" />
                    <!-- Rotating Needle -->
                    <line id="sim12-needle" x1="0" y1="0" x2="0" y2="-32" stroke="#ef4444" stroke-width="2.5" stroke-linecap="round" style="transition: transform 0.5s ease; transform-origin: 0 0; transform: rotate(15deg);" />
                    <circle cx="0" cy="0" r="4" fill="#ffffff" />
                </g>
                <text x="260" y="160" fill="#a5b4fc" font-size="10" font-weight="bold" text-anchor="middle">Micron Pulse</text>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="applyBoseStimulus('normal')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700 transition">
                🌱 Normal Growth
            </button>
            <button onclick="applyBoseStimulus('electric')" class="p-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-[11px] font-bold text-white shadow transition">
                ⚡ Electric Shock
            </button>
            <button onclick="applyBoseStimulus('anesthetic')" class="p-1.5 rounded-lg bg-purple-600 hover:bg-purple-500 text-[11px] font-bold text-white shadow transition">
                🧪 Chloroform Mist
            </button>
        </div>
        <div id="sim12-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            J.C. Bose's crescograph magnifies plant tissue growth 10,000 times, revealing electrical pulses and reversible fatigue under anesthetics.
        </div>
    </div>
    """,

    13: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Flowering Plant Life Cycle Wheel</span>
            <span id="sim13-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Step 1: Dormant Seed</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                
                <!-- Central Display Card -->
                <circle cx="160" cy="100" r="50" fill="#1e293b" stroke="#6366f1" stroke-width="2" />
                <text id="sim13-icon" x="160" y="105" font-size="34" text-anchor="middle" dominant-baseline="middle">🌰</text>
                <text id="sim13-title" x="160" y="175" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">1. Seed in Soil</text>

                <!-- Step Orbit Indicator Dots -->
                <circle id="dot-1" cx="95" cy="50" r="6" fill="#6366f1" />
                <circle id="dot-2" cx="160" cy="30" r="5" fill="#334155" />
                <circle id="dot-3" cx="225" cy="50" r="5" fill="#334155" />
                <circle id="dot-4" cx="245" cy="105" r="5" fill="#334155" />
                <circle id="dot-5" cx="205" cy="155" r="5" fill="#334155" />
                <circle id="dot-6" cx="115" cy="155" r="5" fill="#334155" />
            </svg>
        </div>
        <div class="flex items-center justify-between space-x-2">
            <button onclick="stepPlantCycle(-1)" class="w-1/2 p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700 transition">
                ← Previous Stage
            </button>
            <button onclick="stepPlantCycle(1)" class="w-1/2 p-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-xs font-bold text-white shadow transition">
                Next Stage →
            </button>
        </div>
        <div id="sim13-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Follow the 6 stages: Seed ➔ Seedling ➔ Vegetative Plant ➔ Bloom Flower ➔ Fruit & Pod ➔ Seed Dispersal.
        </div>
    </div>
    """,

    14: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Mosquito Siphon & Oil Film Control</span>
            <span id="sim14-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Larvae Breathing: Normal</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <!-- Stagnant Pond Water -->
                <rect x="0" y="40" width="320" height="160" fill="#082f49" />
                <!-- Water Surface Line -->
                <line x1="0" y1="40" x2="320" y2="40" stroke="#38bdf8" stroke-width="2" />
                
                <!-- Kerosene Oil Film (Initially Transparent) -->
                <rect id="sim14-oil-film" x="0" y="38" width="320" height="6" fill="#f59e0b" opacity="0" style="transition: opacity 0.5s ease;" />

                <!-- Mosquito Larva (Wriggler) Hanging Inverted -->
                <g id="sim14-larva" transform="translate(160, 40)" style="transition: all 0.5s ease;">
                    <!-- Breathing Siphon piercing surface -->
                    <path d="M 0,0 L 5,20" stroke="#ea580c" stroke-width="3" stroke-linecap="round" />
                    <!-- Larval Body Segmentation -->
                    <path d="M 5,20 Q 20,40 10,70 Q 0,90 5,110" stroke="#64748b" stroke-width="5" stroke-linecap="round" fill="none" />
                    <!-- Mouth Brushes -->
                    <circle cx="5" cy="112" r="5" fill="#334155" />
                    <line x1="2" y1="117" x2="-3" y2="123" stroke="#94a3b8" stroke-width="1.5" />
                    <line x1="8" y1="117" x2="13" y2="123" stroke="#94a3b8" stroke-width="1.5" />
                </g>

                <!-- Air Inflow Indicators -->
                <g id="sim14-air" style="transition: opacity 0.5s ease; opacity: 1;">
                    <path d="M 160,20 L 160,35 M 157,28 L 160,35 L 163,28" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" />
                    <text x="170" y="28" fill="#38bdf8" font-size="10" font-weight="bold">Air Inflow</text>
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-2 gap-2">
            <button onclick="sprayKeroseneFilm(true)" class="p-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white shadow transition">
                🛢️ Spray Kerosene Film (Suffocation)
            </button>
            <button onclick="sprayKeroseneFilm(false)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-xs font-bold text-slate-300 border border-slate-700 transition">
                💧 Clean Water (Normal Breathing)
            </button>
        </div>
        <div id="sim14-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Wrigglers breathe through a posterior siphon tube piercing the water surface. An oil slick seals the surface film, suffocating larvae and tumblers.
        </div>
    </div>
    """,

    15: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Silk Moth Metamorphosis & Cocoon Lab</span>
            <span id="sim15-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Stage: Silkworm on Mulberry</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <rect x="0" y="0" width="320" height="200" fill="#090d16" />
                
                <!-- Mulberry Leaf -->
                <path d="M 40,150 C 60,60 160,40 280,70 C 270,160 140,180 40,150 Z" fill="#15803d" stroke="#166534" stroke-width="2" />
                <path d="M 40,150 Q 160,110 280,70" stroke="#86efac" stroke-width="2.5" fill="none" opacity="0.6" />

                <!-- Silkworm Caterpillar (Visible in Stage 1 & 2) -->
                <g id="sim15-caterpillar" style="transition: all 0.5s ease; opacity: 1;">
                    <ellipse cx="140" cy="115" rx="35" ry="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" />
                    <!-- Head & Legs -->
                    <circle cx="178" cy="112" r="8" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5" />
                    <circle cx="182" cy="110" r="2" fill="#1e293b" />
                    <!-- Body Segments -->
                    <line x1="125" y1="104" x2="125" y2="126" stroke="#94a3b8" stroke-width="1.5" />
                    <line x1="145" y1="103" x2="145" y2="127" stroke="#94a3b8" stroke-width="1.5" />
                    <line x1="165" y1="105" x2="165" y2="125" stroke="#94a3b8" stroke-width="1.5" />
                </g>

                <!-- Spun Silk Cocoon (Visible in Stage 3) -->
                <g id="sim15-cocoon" style="transition: all 0.5s ease; opacity: 0;" transform="translate(160, 110)">
                    <ellipse cx="0" cy="0" rx="36" ry="24" fill="#fef08a" stroke="#eab308" stroke-width="2.5" />
                    <!-- Woven Silk Filaments -->
                    <path d="M -25,-10 Q 0,-25 25,-10 Q 30,10 0,20 Q -30,10 -25,-10" stroke="#ca8a04" stroke-width="1" fill="none" />
                    <text x="0" y="4" fill="#854d0e" font-size="9" font-weight="bold" text-anchor="middle">Silk Thread</text>
                </g>

                <!-- Adult Silk Moth (Visible in Stage 4) -->
                <g id="sim15-moth" style="transition: all 0.5s ease; opacity: 0;" transform="translate(160, 95)">
                    <!-- Wings -->
                    <ellipse cx="-20" cy="-10" rx="25" ry="15" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2" transform="rotate(-25 -20 -10)" />
                    <ellipse cx="20" cy="-10" rx="25" ry="15" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2" transform="rotate(25 20 -10)" />
                    <!-- Furry Body -->
                    <ellipse cx="0" cy="0" rx="8" ry="18" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5" />
                    <circle cx="0" cy="-18" r="6" fill="#cbd5e1" />
                    <!-- Feathery Antennae -->
                    <line x1="-3" y1="-22" x2="-14" y2="-32" stroke="#64748b" stroke-width="2" />
                    <line x1="3" y1="-22" x2="14" y2="-32" stroke="#64748b" stroke-width="2" />
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
            <button onclick="setSilkStage('larva')" class="p-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-slate-300 border border-slate-700 transition">
                🐛 Silkworm Larva
            </button>
            <button onclick="setSilkStage('cocoon')" class="p-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-[11px] font-bold text-white shadow transition">
                🧶 Spun Cocoon
            </button>
            <button onclick="setSilkStage('moth')" class="p-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-[11px] font-bold text-white shadow transition">
                🦋 Adult Silk Moth
            </button>
        </div>
        <div id="sim15-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            The caterpillar weaves a continuous 1,000-meter silk filament around itself to form a cocoon, transforming into a pupa and emerging as an adult moth.
        </div>
    </div>
    """,

    16: """
    <div class="space-y-3">
        <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-indigo-300">Amphibian Metamorphosis Timeline</span>
            <span id="sim16-badge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Stage 1: Jelly Spawn</span>
        </div>
        <div class="h-52 rounded-xl bg-slate-950 border border-slate-800 relative flex items-center justify-center overflow-hidden">
            <svg class="w-full h-full" viewBox="0 0 320 200">
                <!-- Pond Water Environment -->
                <rect x="0" y="0" width="320" height="200" fill="#032030" />
                <path d="M 0,160 Q 80,150 160,170 T 320,160 L 320,200 L 0,200 Z" fill="#042f2e" />

                <!-- Stage 1: Frog Spawn (Jelly Eggs) -->
                <g id="sim16-spawn" style="transition: opacity 0.4s ease; opacity: 1;">
                    <circle cx="140" cy="100" r="14" fill="#0284c7" opacity="0.4" stroke="#38bdf8" stroke-width="1.5" />
                    <circle cx="140" cy="100" r="5" fill="#0f172a" />
                    <circle cx="165" cy="95" r="14" fill="#0284c7" opacity="0.4" stroke="#38bdf8" stroke-width="1.5" />
                    <circle cx="165" cy="95" r="5" fill="#0f172a" />
                    <circle cx="155" cy="115" r="14" fill="#0284c7" opacity="0.4" stroke="#38bdf8" stroke-width="1.5" />
                    <circle cx="155" cy="115" r="5" fill="#0f172a" />
                </g>

                <!-- Stage 2: Aquatic Tadpole with Gills & Tail -->
                <g id="sim16-tadpole" style="transition: opacity 0.4s ease; opacity: 0;">
                    <!-- Body -->
                    <ellipse cx="130" cy="100" rx="18" ry="12" fill="#334155" stroke="#475569" stroke-width="1.5" />
                    <circle cx="120" cy="97" r="2.5" fill="#f8fafc" />
                    <circle cx="120" cy="97" r="1.2" fill="#0f172a" />
                    <!-- Feathered Gills -->
                    <path d="M 135,92 Q 142,85 145,90 M 136,95 Q 145,92 147,96" stroke="#f43f5e" stroke-width="1.5" />
                    <!-- Propulsive Swimming Tail -->
                    <path d="M 148,100 Q 185,90 220,100 Q 185,110 148,100 Z" fill="#475569" opacity="0.7" />
                </g>

                <!-- Stage 3: Froglet (Legs Sprouting & Tail Reabsorbing) -->
                <g id="sim16-froglet" style="transition: opacity 0.4s ease; opacity: 0;">
                    <!-- Body -->
                    <ellipse cx="145" cy="95" rx="20" ry="14" fill="#15803d" stroke="#166534" stroke-width="2" />
                    <circle cx="135" cy="90" r="3" fill="#fde047" />
                    <circle cx="135" cy="90" r="1.5" fill="#0f172a" />
                    <!-- Hind Leg -->
                    <path d="M 155,100 L 175,115 L 185,125" stroke="#15803d" stroke-width="3" stroke-linecap="round" fill="none" />
                    <!-- Shortened Reabsorbing Tail -->
                    <path d="M 165,95 Q 185,95 200,95 Q 185,100 165,95 Z" fill="#166534" opacity="0.6" />
                </g>

                <!-- Stage 4: Adult Leaping Frog -->
                <g id="sim16-adult" style="transition: opacity 0.4s ease; opacity: 0;" transform="translate(160, 95)">
                    <!-- Tailless Body -->
                    <ellipse cx="0" cy="0" rx="28" ry="20" fill="#22c55e" stroke="#15803d" stroke-width="2.5" />
                    <!-- Big Bulging Eyes -->
                    <circle cx="-14" cy="-16" r="6" fill="#fde047" stroke="#15803d" stroke-width="1.5" />
                    <circle cx="-14" cy="-16" r="2.5" fill="#0f172a" />
                    <circle cx="14" cy="-16" r="6" fill="#fde047" stroke="#15803d" stroke-width="1.5" />
                    <circle cx="14" cy="-16" r="2.5" fill="#0f172a" />
                    <!-- Muscular Jumping Hind Legs -->
                    <path d="M -20,5 Q -38,10 -35,25 Q -32,32 -20,30" stroke="#16a34a" stroke-width="4" fill="none" stroke-linecap="round" />
                    <path d="M 20,5 Q 38,10 35,25 Q 32,32 20,30" stroke="#16a34a" stroke-width="4" fill="none" stroke-linecap="round" />
                    <!-- Front Arms -->
                    <path d="M -12,12 L -18,26" stroke="#16a34a" stroke-width="3" stroke-linecap="round" />
                    <path d="M 12,12 L 18,26" stroke="#16a34a" stroke-width="3" stroke-linecap="round" />
                </g>
            </svg>
        </div>
        <div class="grid grid-cols-4 gap-1">
            <button onclick="setFrogStage(1)" class="p-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-slate-300 border border-slate-700">
                1. Spawn
            </button>
            <button onclick="setFrogStage(2)" class="p-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-slate-300 border border-slate-700">
                2. Tadpole
            </button>
            <button onclick="setFrogStage(3)" class="p-1 rounded-lg bg-slate-900 hover:bg-slate-800 text-[10px] font-bold text-slate-300 border border-slate-700">
                3. Froglet
            </button>
            <button onclick="setFrogStage(4)" class="p-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-[10px] font-bold text-white shadow">
                4. Adult
            </button>
        </div>
        <div id="sim16-desc" class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300">
            Metamorphosis transforms the swimming gill-breathing tadpole into a four-limbed adult frog breathing through lungs and moist vascular skin.
        </div>
    </div>
    """
}

