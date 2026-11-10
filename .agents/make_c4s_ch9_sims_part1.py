# -*- coding: utf-8 -*-
"""
Interactive Simulators for Slides 1 to 8
Class 4 Science Chapter 9: Different Lands, Different Lives
Bespoke SVG/HTML5 interactive laboratory widgets.
"""

simulators_part1 = {
    # Simulator 1: Diverse Indian Landforms
    "sim_landforms_map": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Interactive Map: Four Physical Landforms of India</h3>
                <p class="text-xs text-slate-400">Click a regional landform zone to inspect its environmental metrics, terrain profile, and human adaptations.</p>
            </div>
            <div class="flex gap-1.5 flex-wrap">
                <button onclick="selectLandform('plains')" class="landform-btn px-2.5 py-1 text-xs rounded-lg bg-emerald-600/30 text-emerald-300 border border-emerald-500/40 font-semibold transition" id="lf-btn-plains">🌾 Plains</button>
                <button onclick="selectLandform('desert')" class="landform-btn px-2.5 py-1 text-xs rounded-lg bg-amber-600/30 text-amber-300 border border-amber-500/40 font-semibold transition" id="lf-btn-desert">🏜️ Desert</button>
                <button onclick="selectLandform('coast')" class="landform-btn px-2.5 py-1 text-xs rounded-lg bg-cyan-600/30 text-cyan-300 border border-cyan-500/40 font-semibold transition" id="lf-btn-coast">🏖️ Coast</button>
                <button onclick="selectLandform('mountains')" class="landform-btn px-2.5 py-1 text-xs rounded-lg bg-indigo-600/30 text-indigo-300 border border-indigo-500/40 font-semibold transition" id="lf-btn-mountains">🏔️ Mountains</button>
            </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 items-center">
            <!-- SVG Map Graphic -->
            <div class="lg:col-span-7 bg-slate-950 rounded-xl p-3 border border-slate-800 flex justify-center items-center relative overflow-hidden min-h-[260px]">
                <svg id="indiaLandformSvg" viewBox="0 0 400 320" class="w-full max-w-[380px] h-auto drop-shadow-md">
                    <!-- Himalayan Mountain Zone (North) -->
                    <path id="mapZoneMountains" onclick="selectLandform('mountains')" class="cursor-pointer transition duration-300 hover:opacity-90" d="M120,40 Q180,20 240,40 Q290,55 330,70 L300,95 Q230,80 160,75 Z" fill="#6366f1" opacity="0.85" stroke="#a5b4fc" stroke-width="2"/>
                    <text x="210" y="55" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle" pointer-events="none">🏔️ Himalayas (Sikkim)</text>

                    <!-- Northern Plains Zone -->
                    <path id="mapZonePlains" onclick="selectLandform('plains')" class="cursor-pointer transition duration-300 hover:opacity-90" d="M120,80 Q200,85 280,105 L270,140 Q190,125 110,120 Z" fill="#10b981" opacity="0.85" stroke="#6ee7b7" stroke-width="2"/>
                    <text x="180" y="105" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle" pointer-events="none">🌾 Northern Plains (Punjab)</text>

                    <!-- Thar Desert Zone (West) -->
                    <path id="mapZoneDesert" onclick="selectLandform('desert')" class="cursor-pointer transition duration-300 hover:opacity-90" d="M70,100 Q120,110 115,160 L65,170 Q55,130 70,100 Z" fill="#f59e0b" opacity="0.85" stroke="#fcd34d" stroke-width="2"/>
                    <text x="85" y="135" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle" pointer-events="none">🏜️ Thar Desert</text>

                    <!-- Coastal Peninsula Zone (East Coast - Odisha) -->
                    <path id="mapZoneCoast" onclick="selectLandform('coast')" class="cursor-pointer transition duration-300 hover:opacity-90" d="M230,150 Q260,170 280,210 L255,225 Q235,185 210,165 Z" fill="#06b6d4" opacity="0.85" stroke="#67e8f9" stroke-width="2"/>
                    <text x="260" y="185" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle" pointer-events="none">🏖️ Puri Coast</text>

                    <!-- Central Plateau Context Outline -->
                    <path d="M110,170 L220,165 L200,260 L145,210 Z" fill="#1e293b" stroke="#334155" stroke-dasharray="3,3" stroke-width="1.5" opacity="0.6"/>
                    <text x="160" y="210" fill="#64748b" font-size="9" text-anchor="middle">Deccan Plateau</text>
                </svg>

                <div id="landformMapTooltip" class="absolute bottom-2 left-2 bg-slate-900/90 border border-slate-700 px-2.5 py-1 rounded text-[11px] text-cyan-300 font-semibold">
                    Click a landform region to view environmental parameters
                </div>
            </div>

            <!-- Environmental Metrics Panel -->
            <div class="lg:col-span-5 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="flex items-center justify-between">
                    <span id="lfDetailTitle" class="text-sm font-bold text-emerald-400">🌾 Northern Agricultural Plains</span>
                    <span id="lfDetailBadge" class="text-[10px] px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Punjab Basin</span>
                </div>
                <p id="lfDetailDesc" class="text-xs text-slate-300 leading-relaxed">
                    Expansive flat lowlands formed by Himalayan river silt deposits. Ideal for intensive farming of wheat and rice with extensive canal networks.
                </p>

                <!-- Environmental Gauges -->
                <div class="space-y-2 pt-1 border-t border-slate-800">
                    <div>
                        <div class="flex justify-between text-[11px] text-slate-400">
                            <span>Soil Fertility</span>
                            <span id="lfSoilVal" class="text-emerald-400 font-bold">Very High (Alluvial)</span>
                        </div>
                        <div class="w-full bg-slate-800 h-1.5 rounded-full mt-1">
                            <div id="lfSoilBar" class="bg-emerald-500 h-1.5 rounded-full" style="width: 95%;"></div>
                        </div>
                    </div>

                    <div>
                        <div class="flex justify-between text-[11px] text-slate-400">
                            <span>Annual Rainfall</span>
                            <span id="lfRainVal" class="text-blue-400 font-bold">Moderate (650 mm)</span>
                        </div>
                        <div class="w-full bg-slate-800 h-1.5 rounded-full mt-1">
                            <div id="lfRainBar" class="bg-blue-500 h-1.5 rounded-full" style="width: 60%;"></div>
                        </div>
                    </div>

                    <div>
                        <div class="flex justify-between text-[11px] text-slate-400">
                            <span>Terrain Flatness</span>
                            <span id="lfFlatVal" class="text-amber-400 font-bold">Level Flatland (180 m)</span>
                        </div>
                        <div class="w-full bg-slate-800 h-1.5 rounded-full mt-1">
                            <div id="lfFlatBar" class="bg-amber-500 h-1.5 rounded-full" style="width: 90%;"></div>
                        </div>
                    </div>
                </div>

                <div class="bg-slate-900 rounded-lg p-2.5 border border-slate-800 text-[11px] text-slate-300">
                    <span class="text-cyan-400 font-bold">Core Human Adaptation:</span>
                    <span id="lfAdaptText" class="ml-1">Tractor-plowed large fields, draft cattle, canal irrigation networks, and wheat granaries.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 2: Fertile Agricultural Plains
    "sim_punjab_plains": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-emerald-300">Plains Farming & Crop Rotation Simulator</h3>
                <p class="text-xs text-slate-400">Simulate seasonal cycles in Punjab: toggle winter (Rabi) vs monsoon (Kharif) and irrigate fields.</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setPlainsSeason('rabi')" id="btnPlainsRabi" class="px-3 py-1 rounded-xl bg-amber-500 text-slate-950 text-xs font-bold transition">❄️ Winter (Rabi)</button>
                <button onclick="setPlainsSeason('kharif')" id="btnPlainsKharif" class="px-3 py-1 rounded-xl bg-slate-800 text-slate-300 hover:text-white text-xs font-bold transition">🌧️ Monsoon (Kharif)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Animated Crop Field Canvas/SVG -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px]">
                <svg viewBox="0 0 500 240" class="w-full h-auto">
                    <!-- Distant Horizon & River -->
                    <rect x="0" y="0" width="500" height="90" fill="#0f172a"/>
                    <!-- Himalayan snow peaks in background -->
                    <polygon points="40,90 90,40 140,90" fill="#334155" opacity="0.6"/>
                    <polygon points="120,90 180,30 240,90" fill="#475569" opacity="0.6"/>
                    <polygon points="160,40 180,30 200,40" fill="#ffffff" opacity="0.9"/>
                    <polygon points="220,90 280,45 340,90" fill="#334155" opacity="0.6"/>
                    
                    <!-- Meandering Silt River -->
                    <path d="M0,85 Q150,75 260,90 T500,85 L500,105 Q320,115 180,100 T0,105 Z" fill="#38bdf8" opacity="0.8"/>
                    <text x="250" y="100" fill="#0369a1" font-size="9" font-weight="bold" text-anchor="middle">River Silt Transport Deposit</text>

                    <!-- Agricultural Soil Bed -->
                    <rect x="0" y="105" width="500" height="135" fill="#3f2e18"/>

                    <!-- Crop Rows (Dynamic based on season) -->
                    <g id="plainsCropRows">
                        <!-- Default: Golden Wheat -->
                        <line x1="20" y1="130" x2="480" y2="130" stroke="#78552b" stroke-width="2"/>
                        <line x1="20" y1="165" x2="480" y2="165" stroke="#78552b" stroke-width="2"/>
                        <line x1="20" y1="200" x2="480" y2="200" stroke="#78552b" stroke-width="2"/>
                    </g>

                    <!-- Interactive Tractor -->
                    <g id="tractorSvgGroup" transform="translate(60, 135)" class="cursor-pointer" onclick="drivePlainsTractor()">
                        <rect x="0" y="15" width="45" height="25" rx="4" fill="#dc2626"/>
                        <rect x="25" y="0" width="25" height="25" rx="3" fill="#1e293b"/>
                        <rect x="28" y="3" width="18" height="12" rx="2" fill="#38bdf8" opacity="0.7"/>
                        <!-- Big rear wheel -->
                        <circle cx="12" cy="40" r="14" fill="#0f172a" stroke="#64748b" stroke-width="3"/>
                        <circle cx="12" cy="40" r="6" fill="#cbd5e1"/>
                        <!-- Small front wheel -->
                        <circle cx="48" cy="44" r="8" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
                        <!-- Exhaust pipe -->
                        <rect x="42" y="-5" width="3" height="10" fill="#94a3b8"/>
                    </g>

                    <!-- Tube Well Water Pump -->
                    <g transform="translate(420, 115)" class="cursor-pointer" onclick="toggleTubeWell()">
                        <rect x="0" y="0" width="30" height="25" fill="#475569" rx="3"/>
                        <circle cx="15" cy="12" r="6" fill="#38bdf8"/>
                        <path d="M-15,15 L0,15" stroke="#0284c7" stroke-width="6"/>
                        <circle id="waterSprayDot" cx="-20" cy="18" r="4" fill="#38bdf8" class="animate-ping"/>
                    </g>
                </svg>

                <div class="flex items-center justify-between text-[11px] text-slate-400 mt-2">
                    <span id="plainsStatusText">🌾 Active Season: Rabi (Winter Wheat & Mustard)</span>
                    <button onclick="drivePlainsTractor()" class="text-cyan-400 hover:text-cyan-300 font-bold">🚜 Drive Tractor</button>
                </div>
            </div>

            <!-- Plains Agronomy Data -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <h4 class="text-xs font-bold text-emerald-400 uppercase tracking-wide">Plains Ecosystem Data</h4>
                <div class="space-y-2 text-xs">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">CURRENT STAPLE CROP</span>
                        <span id="plainsCropName" class="font-bold text-amber-300 text-sm">Golden Wheat (Kanak)</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">SOIL PROFILE</span>
                        <span class="font-semibold text-slate-200">River Alluvium (Rich in Potash & Phosphoric Acid)</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">IRRIGATION SOURCE</span>
                        <span class="font-semibold text-cyan-300">Canal Networks + Electric Tube Wells</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 3: Plains Harvest Cuisine
    "sim_plains_nutrition": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Farm-to-Table Nutrition Analyzer: Northern Plains Feast</h3>
                <p class="text-xs text-slate-400">Assemble traditional winter dishes on the brass plate to view energy, protein, and probiotic levels.</p>
            </div>
            <button onclick="resetPlainsThali()" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold transition">Reset Plate</button>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 items-center">
            <!-- Interactive Brass Thali -->
            <div class="lg:col-span-7 bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center min-h-[250px]">
                <div class="relative w-56 h-56 rounded-full bg-gradient-to-br from-amber-600 via-amber-700 to-amber-900 p-3 shadow-2xl border-4 border-amber-500/40 flex items-center justify-center">
                    <!-- Circular Platter -->
                    <div class="w-full h-full rounded-full bg-slate-900/90 border border-amber-500/20 relative flex items-center justify-center overflow-hidden">
                        <!-- Makki Di Roti -->
                        <div id="thaliItemRoti" class="absolute left-6 top-10 w-20 h-20 rounded-full bg-amber-400/90 border-2 border-amber-300 shadow-md flex items-center justify-center cursor-pointer transition hover:scale-105" onclick="toggleThaliFood('roti')">
                            <span class="text-[10px] font-bold text-amber-950 text-center leading-tight">🌽 Makki Roti</span>
                        </div>

                        <!-- Sarson Da Saag -->
                        <div id="thaliItemSaag" class="absolute right-6 top-8 w-20 h-20 rounded-full bg-emerald-700 border-2 border-emerald-400 shadow-md flex items-center justify-center cursor-pointer transition hover:scale-105" onclick="toggleThaliFood('saag')">
                            <span class="text-[10px] font-bold text-emerald-100 text-center leading-tight">🥬 Sarson Saag</span>
                        </div>

                        <!-- Churned White Butter (Makhan) -->
                        <div id="thaliItemMakhan" class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-yellow-100 border border-yellow-200 shadow-sm flex items-center justify-center cursor-pointer" onclick="toggleThaliFood('makhan')">
                            <span class="text-[9px] font-bold text-slate-800">🧈</span>
                        </div>

                        <!-- Lassi Glass -->
                        <div id="thaliItemLassi" class="absolute bottom-4 w-24 h-12 rounded-xl bg-cyan-900/60 border border-cyan-400 flex items-center justify-center cursor-pointer transition hover:scale-105" onclick="toggleThaliFood('lassi')">
                            <span class="text-[10px] font-bold text-cyan-200">🥛 Frothy Lassi</span>
                        </div>
                    </div>
                </div>
                <span class="text-[11px] text-slate-400 mt-3">Click any food item on the brass plate to add or remove it</span>
            </div>

            <!-- Nutritional Metrics Panel -->
            <div class="lg:col-span-5 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <h4 class="text-xs font-bold text-amber-400 uppercase tracking-wide">Nutritional Breakdown</h4>
                
                <div class="space-y-2.5">
                    <div>
                        <div class="flex justify-between text-xs">
                            <span class="text-slate-400">Slow-Release Energy (Carbohydrates)</span>
                            <span id="nutriCarbs" class="text-amber-400 font-bold">78%</span>
                        </div>
                        <div class="w-full bg-slate-800 h-2 rounded-full mt-1">
                            <div id="barCarbs" class="bg-amber-500 h-2 rounded-full transition-all duration-300" style="width: 78%;"></div>
                        </div>
                    </div>

                    <div>
                        <div class="flex justify-between text-xs">
                            <span class="text-slate-400">Immunity Vitamins (A, C, Iron)</span>
                            <span id="nutriVitamins" class="text-emerald-400 font-bold">92%</span>
                        </div>
                        <div class="w-full bg-slate-800 h-2 rounded-full mt-1">
                            <div id="barVitamins" class="bg-emerald-500 h-2 rounded-full transition-all duration-300" style="width: 92%;"></div>
                        </div>
                    </div>

                    <div>
                        <div class="flex justify-between text-xs">
                            <span class="text-slate-400">Probiotics & Calcium (Gut Health)</span>
                            <span id="nutriProbiotics" class="text-cyan-400 font-bold">85%</span>
                        </div>
                        <div class="w-full bg-slate-800 h-2 rounded-full mt-1">
                            <div id="barProbiotics" class="bg-cyan-500 h-2 rounded-full transition-all duration-300" style="width: 85%;"></div>
                        </div>
                    </div>
                </div>

                <div class="bg-slate-900 rounded-lg p-2.5 border border-slate-800 text-[11px] text-slate-300">
                    <span class="text-amber-400 font-bold">Health Impact:</span>
                    <span id="nutriSummary">Yellow maize provides sustained stamina for outdoor farming; mustard greens supply essential iron and winter immunity.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 4: Golden Temple Langar
    "sim_langar_kitchen": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Sri Harmandir Sahib: Community Langar Logistics</h3>
                <p class="text-xs text-slate-400">Explore the world's largest free community kitchen: operate the automated roti maker and observe equal communal dining.</p>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-xs font-bold text-cyan-300 bg-slate-800 px-2.5 py-1 rounded-lg border border-slate-700">Meals Served Today: <span id="langarCount">104,250</span></span>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
            <!-- Stage 1: Roti Machine -->
            <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col justify-between space-y-3">
                <div>
                    <div class="flex items-center justify-between mb-2">
                        <span class="text-xs font-bold text-amber-400">1. Automated Roti Maker</span>
                        <span class="text-[10px] px-2 py-0.5 rounded bg-amber-500/20 text-amber-300">12,000/hr</span>
                    </div>
                    <div class="h-28 bg-slate-900 rounded-lg border border-slate-800 flex items-center justify-center relative overflow-hidden">
                        <!-- Conveyor Belt Animation -->
                        <div class="w-full h-8 bg-slate-800 border-y border-slate-700 flex items-center justify-around overflow-hidden">
                            <div class="w-6 h-6 rounded-full bg-amber-400 animate-pulse"></div>
                            <div class="w-6 h-6 rounded-full bg-amber-300"></div>
                            <div class="w-6 h-6 rounded-full bg-amber-200"></div>
                        </div>
                    </div>
                </div>
                <button onclick="operateRotiMachine()" class="w-full py-1.5 rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition">Bake Roti Batch (+50)</button>
            </div>

            <!-- Stage 2: Dal Cauldron -->
            <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col justify-between space-y-3">
                <div>
                    <div class="flex items-center justify-between mb-2">
                        <span class="text-xs font-bold text-yellow-400">2. Dal Cauldrons (Degs)</span>
                        <span class="text-[10px] px-2 py-0.5 rounded bg-yellow-500/20 text-yellow-300">7 Quintals</span>
                    </div>
                    <div class="h-28 bg-slate-900 rounded-lg border border-slate-800 flex flex-col items-center justify-center p-2 text-center">
                        <span class="text-3xl animate-bounce">🍲</span>
                        <span class="text-[11px] text-slate-300 mt-1">Slow-cooking nutritious lentil dal with turmeric and ginger in giant iron pots.</span>
                    </div>
                </div>
                <button onclick="stirDalCauldron()" class="w-full py-1.5 rounded-lg bg-yellow-600 hover:bg-yellow-500 text-white font-bold text-xs transition">Stir Cauldron (Sewa)</button>
            </div>

            <!-- Stage 3: Pangat Equality Hall -->
            <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col justify-between space-y-3">
                <div>
                    <div class="flex items-center justify-between mb-2">
                        <span class="text-xs font-bold text-cyan-400">3. Equal Seated Dining</span>
                        <span class="text-[10px] px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300">Universal Pangat</span>
                    </div>
                    <div class="h-28 bg-slate-900 rounded-lg border border-slate-800 flex items-center justify-around px-2">
                        <span class="text-xl">🧑‍🤝‍🧑</span>
                        <span class="text-xl">🧑‍🤝‍🧑</span>
                        <span class="text-xl">🧑‍🤝‍🧑</span>
                    </div>
                </div>
                <div class="text-[11px] text-slate-400 text-center py-1">
                    Sitting side by side on floor mats, completely erasing social divisions.
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 5: Arid Desert Ecosystem
    "sim_desert_ecology": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Thar Desert Xerophyte & Camel Adaptations</h3>
                <p class="text-xs text-slate-400">Investigate how camels walk on dunes and how desert plants survive severe drought conditions.</p>
            </div>
            <div class="flex gap-1.5">
                <button onclick="toggleDesertFeature('camel')" id="btnDesCamel" class="px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition">🐪 Camel</button>
                <button onclick="toggleDesertFeature('khejri')" id="btnDesKhejri" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">🌳 Khejri Tree</button>
                <button onclick="toggleDesertFeature('cactus')" id="btnDesCactus" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">🌵 Cactus Spines</button>
            </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 items-center">
            <!-- Desert Landscape SVG -->
            <div class="lg:col-span-7 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[240px]">
                <svg viewBox="0 0 450 220" class="w-full h-auto">
                    <!-- Sun and Sky -->
                    <rect x="0" y="0" width="450" height="110" fill="#78350f" opacity="0.4"/>
                    <circle cx="390" cy="40" r="28" fill="#fbbf24" opacity="0.9"/>
                    
                    <!-- Sand Dunes -->
                    <path d="M0,110 Q120,60 230,120 T450,90 L450,220 L0,220 Z" fill="#d97706"/>
                    <path d="M0,140 Q150,110 300,160 T450,130 L450,220 L0,220 Z" fill="#b45309"/>

                    <!-- Camel Figure -->
                    <g id="desertCamelSvg" transform="translate(100, 70)" class="transition-all duration-300">
                        <!-- Body and Hump -->
                        <ellipse cx="60" cy="55" rx="35" ry="20" fill="#92400e"/>
                        <path d="M45,40 Q60,15 75,40 Z" fill="#78350f"/> <!-- Hump -->
                        <text x="60" y="32" fill="#fef3c7" font-size="8" text-anchor="middle" font-weight="bold">Fat Reserve</text>
                        <!-- Neck and Head -->
                        <path d="M90,55 Q105,30 110,15 L125,20 L115,45 Z" fill="#92400e"/>
                        <circle cx="120" cy="18" r="7" fill="#78350f"/>
                        <!-- Legs and Padded Feet -->
                        <line x1="40" y1="70" x2="35" y2="115" stroke="#78350f" stroke-width="5"/>
                        <ellipse cx="33" cy="116" rx="8" ry="3" fill="#451a03"/> <!-- Wide Pad -->
                        <line x1="75" y1="70" x2="80" y2="115" stroke="#78350f" stroke-width="5"/>
                        <ellipse cx="82" cy="116" rx="8" ry="3" fill="#451a03"/> <!-- Wide Pad -->
                        <text x="40" y="130" fill="#fef3c7" font-size="8">Wide Padded Feet</text>
                    </g>

                    <!-- Khejri Tree -->
                    <g id="desertKhejriSvg" transform="translate(280, 50)" class="hidden transition-all duration-300">
                        <line x1="40" y1="40" x2="40" y2="120" stroke="#78350f" stroke-width="8"/>
                        <!-- Foliage -->
                        <circle cx="40" cy="30" r="30" fill="#15803d" opacity="0.9"/>
                        <circle cx="20" cy="35" r="20" fill="#166534" opacity="0.9"/>
                        <circle cx="60" cy="35" r="20" fill="#166534" opacity="0.9"/>
                        <!-- Deep Taproot subterranean -->
                        <path d="M40,120 Q35,160 40,210" stroke="#451a03" stroke-width="4" stroke-dasharray="2,2"/>
                        <text x="45" y="180" fill="#fef3c7" font-size="8">Deep Taproot (30m)</text>
                    </g>
                </svg>
            </div>

            <!-- Detail Metrics Panel -->
            <div class="lg:col-span-5 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="flex items-center justify-between">
                    <span id="desFeatureTitle" class="text-sm font-bold text-amber-400">🐪 Camel (Ship of the Desert)</span>
                </div>
                <p id="desFeatureDesc" class="text-xs text-slate-300 leading-relaxed">
                    Wide padded feet spread the camel's body mass over a large area, preventing sinking in loose dunes. The hump stores fat that metabolizes into energy and water.
                </p>

                <div class="space-y-2 pt-2 border-t border-slate-800 text-xs">
                    <div class="flex justify-between">
                        <span class="text-slate-400">Ground Pressure:</span>
                        <span id="desPressureVal" class="text-emerald-400 font-semibold">Low (Wide surface contact)</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-slate-400">Transpiration Loss:</span>
                        <span id="desTranspVal" class="text-cyan-400 font-semibold">Near Zero (Spines/Waxy)</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-slate-400">Active Survival Mechanism:</span>
                        <span id="desAdaptVal" class="text-amber-300 font-semibold">Fat metabolism & Nocturnal rest</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 6: Desert Culture Attire
    "sim_desert_culture": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Rajasthani Textiles & Folk Acoustics</h3>
                <p class="text-xs text-slate-400">Test cotton turban insulation and play the wooden khartal clappers and sarangi strings.</p>
            </div>
            <div class="flex gap-2">
                <button onclick="playKhartalSound()" class="px-3 py-1 rounded-xl bg-amber-600 hover:bg-amber-500 text-white text-xs font-bold transition">🎵 Click Khartal</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Turban Thermal Insulation Test -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wide">Multi-Fold Cotton Turban (Pagri)</span>
                <p class="text-xs text-slate-300">The pagri uses up to 20 metres of fine cotton cloth. Dense air layers between folds block scorching solar heat.</p>
                
                <div class="space-y-2">
                    <div class="flex justify-between text-xs">
                        <span class="text-slate-400">Outdoor Desert Air:</span>
                        <span class="text-red-400 font-bold">46°C</span>
                    </div>
                    <div class="flex justify-between text-xs">
                        <span class="text-slate-400">Underneath Turban Folds:</span>
                        <span class="text-emerald-400 font-bold">34°C (-12°C cooler!)</span>
                    </div>
                    <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                        <div class="bg-gradient-to-r from-emerald-500 to-amber-500 h-2" style="width: 74%;"></div>
                    </div>
                </div>
                <div class="text-[11px] text-slate-400 italic">
                    Bonus functions: Unwrapped to filter sandstorm dust, pull water buckets, or serve as an emergency pillow.
                </div>
            </div>

            <!-- Bandhini Tie-Dye Art -->
            <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">Bandhini Tie-Dye Geometry</span>
                <p class="text-xs text-slate-300">Thousands of tiny knots tied with thread before dip-dyeing in natural indigo, turmeric, and madder.</p>
                
                <div class="h-24 bg-gradient-to-r from-red-600 via-amber-500 to-pink-600 rounded-lg p-2 flex items-center justify-around border border-slate-700">
                    <div class="w-8 h-8 rounded-full border-2 border-white flex items-center justify-center text-[10px] font-bold text-white">●</div>
                    <div class="w-8 h-8 rounded-full border-2 border-white flex items-center justify-center text-[10px] font-bold text-white">●</div>
                    <div class="w-8 h-8 rounded-full border-2 border-white flex items-center justify-center text-[10px] font-bold text-white">●</div>
                    <div class="w-8 h-8 rounded-full border-2 border-white flex items-center justify-center text-[10px] font-bold text-white">●</div>
                </div>
                <button onclick="cycleBandhiniPattern()" class="w-full py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition">Generate New Pattern</button>
            </div>
        </div>
    </div>
    """,

    # Simulator 7: Desert Water Tankas
    "sim_tanka_system": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Underground Desert Tanka (Rainwater Harvesting)</h3>
                <p class="text-xs text-slate-400">Trigger rare desert rain and observe how sloping paved courtyards channel filtered water into sealed underground cisterns.</p>
            </div>
            <button onclick="triggerTankaRain()" class="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold transition flex items-center gap-1.5">
                <span>🌧️</span> Start Desert Rain
            </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Tanka Cutaway Cross-section SVG -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[240px]">
                <svg viewBox="0 0 500 240" class="w-full h-auto">
                    <!-- Ground level line -->
                    <line x1="0" y1="80" x2="500" y2="80" stroke="#94a3b8" stroke-width="2"/>
                    <text x="20" y="70" fill="#94a3b8" font-size="10">Ground Level</text>

                    <!-- Sloping Paved Courtyard (Agor) Catchment -->
                    <path d="M0,80 L200,80 L230,85 L200,90 L0,90 Z" fill="#64748b"/>
                    <text x="100" y="75" fill="#f8fafc" font-size="9" font-weight="bold">Sloping Paved Courtyard</text>

                    <!-- Filtration Silt Trap Pit -->
                    <rect x="200" y="80" width="30" height="40" fill="#334155" stroke="#475569"/>
                    <text x="215" y="105" fill="#cbd5e1" font-size="7" text-anchor="middle">Filter Pit</text>

                    <!-- Inflow Pipe -->
                    <path d="M230,105 L260,115" stroke="#38bdf8" stroke-width="5"/>

                    <!-- Underground Cistern (Tanka) -->
                    <rect x="250" y="90" width="180" height="135" rx="8" fill="#1e293b" stroke="#0284c7" stroke-width="3"/>
                    <text x="340" y="110" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Underground Tanka (Sealed)</text>

                    <!-- Water Level in Tanka -->
                    <rect id="tankaWaterRect" x="252" y="160" width="176" height="63" fill="#0284c7" opacity="0.8"/>
                    <text id="tankaWaterText" x="340" y="195" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Water: 15,000 Litres</text>

                    <!-- Protective Cover / Cap -->
                    <rect x="320" y="85" width="40" height="10" fill="#475569" stroke="#94a3b8"/>
                    <text x="340" y="82" fill="#94a3b8" font-size="8" text-anchor="middle">Airtight Cover</text>

                    <!-- Rain Droplets Animation Group -->
                    <g id="tankaRainGroup" class="hidden">
                        <line x1="80" y1="20" x2="70" y2="50" stroke="#38bdf8" stroke-width="2"/>
                        <line x1="120" y1="10" x2="110" y2="40" stroke="#38bdf8" stroke-width="2"/>
                        <line x1="160" y1="25" x2="150" y2="55" stroke="#38bdf8" stroke-width="2"/>
                    </g>
                </svg>
            </div>

            <!-- Tanka Engineering Metrics -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <h4 class="text-xs font-bold text-cyan-400 uppercase tracking-wide">Tanka Specifications</h4>
                <div class="space-y-2 text-xs">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">EVAPORATION LOSS</span>
                        <span class="font-bold text-emerald-400">0% (Completely Underground)</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">STORAGE DURATION</span>
                        <span class="font-bold text-amber-300">8 to 10 Months (Entire Dry Season)</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">FILTRATION MEDIA</span>
                        <span class="font-semibold text-slate-200">Gravel + Clean Sand + Charcoal</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 8: Golden Sandstone Fort
    "sim_jaisalmer_fort": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Jaisalmer Fort: Passive Cooling & Stone Jalis</h3>
                <p class="text-xs text-slate-400">Adjust the sun angle slider to observe shade in narrow streets and the Venturi effect through stone lattice screens.</p>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400">Sun Position:</span>
                <input type="range" id="sunSlider" min="0" max="100" value="50" oninput="updateFortSun(this.value)" class="w-24 sm:w-32 accent-amber-500">
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Street Shade Cross-section -->
            <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 space-y-2">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wide">Narrow Street Shading (Alleys)</span>
                <div class="h-32 bg-slate-900 rounded-lg border border-slate-800 relative flex justify-between px-6 pt-3 overflow-hidden">
                    <!-- Left Tall Building -->
                    <div class="w-16 h-full bg-amber-600/80 border-r-2 border-amber-400/60 relative">
                        <div class="text-[9px] text-amber-200 p-1">Jharokha</div>
                    </div>
                    <!-- Walkway Shade Box -->
                    <div id="fortAlleyShade" class="flex-1 h-full bg-black/50 transition-opacity flex items-end justify-center pb-2">
                        <span class="text-[10px] text-cyan-300 font-bold bg-slate-900/80 px-2 py-0.5 rounded">Walkway Shaded (32°C)</span>
                    </div>
                    <!-- Right Tall Building -->
                    <div class="w-16 h-full bg-amber-600/80 border-l-2 border-amber-400/60 relative">
                        <div class="text-[9px] text-amber-200 p-1 text-right">Facade</div>
                    </div>
                </div>
                <p class="text-[11px] text-slate-400">High building height-to-width ratio ensures streets remain cast in shadow during peak sun hours.</p>
            </div>

            <!-- Jali Screen Venturi Effect -->
            <div class="bg-slate-950 rounded-xl p-3 border border-slate-800 space-y-2">
                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wide">Stone Jali Venturi Acceleration</span>
                <div class="h-32 bg-slate-900 rounded-lg border border-slate-800 flex items-center justify-around px-3">
                    <div class="text-center">
                        <span class="text-[10px] text-slate-400 block">HOT OUTSIDE AIR</span>
                        <span class="text-sm font-bold text-red-400">45°C</span>
                        <span class="text-[10px] text-slate-500 block">Low velocity (2 m/s)</span>
                    </div>
                    <div class="w-10 h-20 bg-amber-500/30 border-2 border-amber-400/80 rounded flex flex-col justify-around items-center p-1">
                        <div class="w-2 h-2 rounded-full bg-cyan-400"></div>
                        <div class="w-2 h-2 rounded-full bg-cyan-400"></div>
                        <div class="w-2 h-2 rounded-full bg-cyan-400"></div>
                    </div>
                    <div class="text-center">
                        <span class="text-[10px] text-slate-400 block">COOLED INTERIOR AIR</span>
                        <span class="text-sm font-bold text-emerald-400">33°C</span>
                        <span class="text-[10px] text-cyan-300 font-bold block">Fast Breeze (6 m/s)</span>
                    </div>
                </div>
                <p class="text-[11px] text-slate-400">Narrow apertures force air to accelerate and expand, dropping ambient temperature naturally.</p>
            </div>
        </div>
    </div>
    """
}

