# -*- coding: utf-8 -*-
"""Class 4 Science Chapter 5: Food for Health - Simulators 9-16"""

sims_part2 = {
    "sim-9": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">⚖️ Healthy Home Snack vs Ultra-Processed Junk</h4>
                <p class="text-xs text-slate-400">Compare nutrient density and health indicators between common snack choices</p>
            </div>
            <span class="text-xs px-2.5 py-1 rounded-full bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold" id="sim9-badge">Junk Warning</span>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <button onclick="compareSnack('junk')" class="p-3 rounded-xl bg-slate-950/80 border border-slate-800 hover:border-rose-500/50 text-left transition">
                <div class="flex items-center gap-2 mb-1">
                    <span class="text-xl">🍟</span>
                    <span class="font-bold text-xs text-rose-300">Potato Chips & Soda</span>
                </div>
                <div class="text-[11px] text-slate-400">Refined sugars, trans fats, excessive chemical sodium, empty calories.</div>
            </button>
            <button onclick="compareSnack('healthy')" class="p-3 rounded-xl bg-slate-950/80 border border-slate-800 hover:border-emerald-500/50 text-left transition">
                <div class="flex items-center gap-2 mb-1">
                    <span class="text-xl">🌰</span>
                    <span class="font-bold text-xs text-emerald-300">Roasted Makhana & Fruit</span>
                </div>
                <div class="text-[11px] text-slate-400">Dietary fiber, plant protein, minerals, zero synthetic additives.</div>
            </button>
        </div>
        <div class="bg-slate-950/90 rounded-xl p-3 border border-slate-800 space-y-2">
            <div class="flex items-center justify-between text-xs">
                <span>Vitamins & Minerals:</span>
                <span id="sim9-vit" class="text-rose-400 font-bold">Almost Zero (Stripped)</span>
            </div>
            <div class="flex items-center justify-between text-xs">
                <span>Trans Fat & Sodium Risk:</span>
                <span id="sim9-risk" class="text-rose-400 font-bold">Extremely High</span>
            </div>
            <div class="flex items-center justify-between text-xs border-t border-slate-800 pt-1.5">
                <span>Health Recommendation:</span>
                <span id="sim9-rec" class="text-slate-300">Choose fresh home-cooked snacks to protect dental enamel and heart wellness.</span>
            </div>
        </div>
    </div>
    """,

    "sim-10": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">🍽️ Balanced Plate Nutrition Visualizer</h4>
                <p class="text-xs text-slate-400">Explore ideal visual plate proportions for daily lunches and dinners</p>
            </div>
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold">100% Balanced</span>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-center">
            <div class="p-3 rounded-xl bg-emerald-950/40 border border-emerald-800/40 space-y-1">
                <span class="text-2xl">🥦 🍎</span>
                <div class="text-xs font-bold text-emerald-300">50% Protective Foods</div>
                <div class="text-[10px] text-slate-300">Half of plate: Colorful vegetables, leafy saag, and fresh fruits for vitamins and fiber.</div>
            </div>
            <div class="p-3 rounded-xl bg-amber-950/40 border border-amber-800/40 space-y-1">
                <span class="text-2xl">🫘 🧀</span>
                <div class="text-xs font-bold text-amber-300">25% Body-Building Foods</div>
                <div class="text-[10px] text-slate-300">Quarter of plate: Lentil dal, chickpeas, paneer, curd, or eggs for muscle construction.</div>
            </div>
            <div class="p-3 rounded-xl bg-cyan-950/40 border border-cyan-800/40 space-y-1">
                <span class="text-2xl">🌾 🍚</span>
                <div class="text-xs font-bold text-cyan-300">25% Energy Foods</div>
                <div class="text-[10px] text-slate-300">Quarter of plate: Brown rice, whole wheat rotis, or millets for sustained stamina.</div>
            </div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs text-slate-300 flex items-center justify-between">
            <span>Essential Companions:</span>
            <span class="text-amber-400 font-semibold">💧 Clean Drinking Water • 🧈 1 tsp Ghee (for Vitamin A, D, E, K uptake)</span>
        </div>
    </div>
    """,

    "sim-11": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">🍛 Interactive Pan-Indian Thali Builder</h4>
                <p class="text-xs text-slate-400">Toggle regional Indian thalis to inspect how traditional platters balance all nutrients</p>
            </div>
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 font-semibold" id="sim11-badge">Gujarati Thali</span>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="buildThali('gujarat')" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-amber-300">Gujarat Thali</button>
            <button onclick="buildThali('rajasthan')" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-rose-300">Rajasthan Thali</button>
            <button onclick="buildThali('south')" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-emerald-300">Southern Thali</button>
            <button onclick="buildThali('bengal')" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-cyan-300">Eastern Thali</button>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 space-y-2">
            <div class="flex items-center justify-between">
                <span id="sim11-title" class="text-sm font-bold text-white">Traditional Gujarati Thali</span>
                <span id="sim11-tastes" class="text-xs text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20">6 Tastes Present</span>
            </div>
            <div id="sim11-items" class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1 text-xs">
                <div class="p-2 rounded-lg bg-slate-900 border border-slate-800 text-center"><div class="text-lg">🫓</div><div class="font-bold text-slate-200">Rotli / Bhakri</div><div class="text-[10px] text-slate-400">Energy Grains</div></div>
                <div class="p-2 rounded-lg bg-slate-900 border border-slate-800 text-center"><div class="text-lg">🥣</div><div class="font-bold text-slate-200">Sweet-Tart Dal</div><div class="text-[10px] text-slate-400">Protein & Spices</div></div>
                <div class="p-2 rounded-lg bg-slate-900 border border-slate-800 text-center"><div class="text-lg">🥬</div><div class="font-bold text-slate-200">Shaak (Greens)</div><div class="text-[10px] text-slate-400">Protective Veg</div></div>
                <div class="p-2 rounded-lg bg-slate-900 border border-slate-800 text-center"><div class="text-lg">🥛</div><div class="font-bold text-slate-200">Chhaas (Buttermilk)</div><div class="text-[10px] text-slate-400">Gut Probiotics</div></div>
            </div>
        </div>
    </div>
    """,

    "sim-12": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">💧 Physiological Hydration Chamber</h4>
                <p class="text-xs text-slate-400">Simulate body water balance and explore the vital functions of hydration</p>
            </div>
            <button onclick="hydrateBody()" class="px-3 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white transition">Drink Water 🥤</button>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800 text-center space-y-1">
                <span class="text-xl">🌡️</span>
                <div class="text-xs font-bold text-amber-300">Temperature Control</div>
                <div class="text-[10px] text-slate-400" id="sim12-temp">Sweating cools skin during sports</div>
            </div>
            <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800 text-center space-y-1">
                <span class="text-xl">🫘</span>
                <div class="text-xs font-bold text-emerald-300">Kidney Waste Flush</div>
                <div class="text-[10px] text-slate-400" id="sim12-kidney">Eliminates urea smoothly in urine</div>
            </div>
            <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800 text-center space-y-1">
                <span class="text-xl">🍉</span>
                <div class="text-xs font-bold text-cyan-300">Hydrating Foods</div>
                <div class="text-[10px] text-slate-400">Watermelon (>90%), Cucumber, Coconut water</div>
            </div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-between text-xs">
            <span>Body Fluid Level: <span id="sim12-level" class="text-cyan-400 font-bold">70% (Optimal Hydration)</span></span>
            <span id="sim12-status" class="text-emerald-400 font-semibold">✨ Alert & Energetic</span>
        </div>
    </div>
    """,

    "sim-13": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">🍳 Cooking Method & Nutrient Preservation Lab</h4>
                <p class="text-xs text-slate-400">Compare how different cooking techniques impact delicate vitamins and digestibility</p>
            </div>
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" id="sim13-badge">Steaming (Best)</span>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="testCookingMethod('steaming')" class="px-2.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-emerald-300">Steaming</button>
            <button onclick="testCookingMethod('boiling')" class="px-2.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-cyan-300">Boiling</button>
            <button onclick="testCookingMethod('roasting')" class="px-2.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-amber-300">Roasting</button>
            <button onclick="testCookingMethod('frying')" class="px-2.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-rose-300">Deep Frying</button>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 space-y-2">
            <div class="flex items-center justify-between text-xs font-semibold">
                <span id="sim13-method-name">Steaming (Idli / Dhokla)</span>
                <span id="sim13-retention" class="text-emerald-400">Vitamin Retention: 95%</span>
            </div>
            <div class="w-full bg-slate-800 h-2.5 rounded-full overflow-hidden">
                <div id="sim13-bar" class="bg-emerald-400 h-2.5 w-[95%] transition-all duration-300"></div>
            </div>
            <p id="sim13-desc" class="text-xs text-slate-300 pt-1">Gentle steam vapor softens tough cellulose without leaching water-soluble vitamins into discard water.</p>
        </div>
    </div>
    """,

    "sim-14": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">☀️ Solar Thermal Box Cooker Harness</h4>
                <p class="text-xs text-slate-400">Examine how sunlight and the greenhouse effect cook food without fire or smoke</p>
            </div>
            <button onclick="boostSunlight()" class="px-3 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-xs font-bold text-white transition">Harness Sun ☀️</button>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800 space-y-1 text-center">
                <span class="text-xl">🪞</span>
                <div class="text-xs font-bold text-amber-300">Reflecting Mirror</div>
                <div class="text-[10px] text-slate-400">Directs parallel sunlight into the glass-covered cooker box.</div>
            </div>
            <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800 space-y-1 text-center">
                <span class="text-xl">🪟</span>
                <div class="text-xs font-bold text-cyan-300">Double-Glass Lid</div>
                <div class="text-[10px] text-slate-400">Traps infrared heat via greenhouse effect, preventing heat loss.</div>
            </div>
            <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800 space-y-1 text-center">
                <span class="text-xl">🥘</span>
                <div class="text-xs font-bold text-emerald-300">Black Metal Pots</div>
                <div class="text-[10px] text-slate-400">Absorbs 98% of thermal radiation to cook lentils and rice slowly.</div>
            </div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-between text-xs">
            <span>Chamber Temperature: <span id="sim14-temp" class="text-amber-400 font-bold">115°C (Cooking Active)</span></span>
            <span class="text-emerald-400 font-semibold">🌱 0% Smoke • 100% Free Solar Energy</span>
        </div>
    </div>
    """,

    "sim-15": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">🔍 Packaged Food Label Detective</h4>
                <p class="text-xs text-slate-400">Click highlighted label zones to decode consumer safety and nutritional facts</p>
            </div>
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" id="sim15-badge">Safe To Buy</span>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="inspectLabel('expiry')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-amber-300 text-center">Expiry Date</button>
            <button onclick="inspectLabel('ingredients')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-emerald-300 text-center">Ingredient List</button>
            <button onclick="inspectLabel('vegdot')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-cyan-300 text-center">Veg/Non-Veg Dot</button>
            <button onclick="inspectLabel('nutrition')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-purple-300 text-center">Nutrition Facts</button>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 space-y-1.5">
            <div class="flex items-center justify-between">
                <span id="sim15-title" class="text-sm font-bold text-white">📅 Expiry / Best Before Date Check</span>
                <span id="sim15-indicator" class="text-xs text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">Mfg: 10/2026 | Exp: 04/2027</span>
            </div>
            <p id="sim15-info" class="text-xs text-slate-300">Always check before purchase! Consuming food past its expiry date risks severe bacterial contamination and food poisoning.</p>
        </div>
    </div>
    """,

    "sim-16": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">🎪 School Food Festival Stall Planner</h4>
                <p class="text-xs text-slate-400">Toggle event checklist items to ensure hygiene, diversity, and zero waste</p>
            </div>
            <span class="text-xs px-2.5 py-1 rounded-full bg-slate-800 text-slate-400 border border-slate-700 font-bold" id="sim16-score">Score: 0 / 100</span>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
            <label class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 flex items-center gap-2.5 cursor-pointer">
                <input type="checkbox" id="sim16-chk-wash" onchange="updateSim16Score()" class="w-4 h-4 rounded text-emerald-500 bg-slate-900 border-slate-700 focus:ring-emerald-500">
                <span>Handwashing station with clean water & soap</span>
            </label>
            <label class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 flex items-center gap-2.5 cursor-pointer">
                <input type="checkbox" id="sim16-chk-cover" onchange="updateSim16Score()" class="w-4 h-4 rounded text-emerald-500 bg-slate-900 border-slate-700 focus:ring-emerald-500">
                <span>Mesh netting over all food trays to ward off flies</span>
            </label>
            <label class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 flex items-center gap-2.5 cursor-pointer">
                <input type="checkbox" id="sim16-chk-millet" onchange="updateSim16Score()" class="w-4 h-4 rounded text-emerald-500 bg-slate-900 border-slate-700 focus:ring-emerald-500">
                <span>Stalls featuring regional millets (ragi, bajra, jowar)</span>
            </label>
            <label class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 flex items-center gap-2.5 cursor-pointer">
                <input type="checkbox" id="sim16-chk-eco" onchange="updateSim16Score()" class="w-4 h-4 rounded text-emerald-500 bg-slate-900 border-slate-700 focus:ring-emerald-500">
                <span>Compostable leaf plates (pattals) & zero plastic</span>
            </label>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex items-center justify-between text-xs">
            <span id="sim16-status" class="text-slate-400">Complete all checklist items to open the school festival!</span>
            <span id="sim16-badge" class="px-2.5 py-0.5 rounded bg-slate-800 text-slate-400 border border-slate-700 font-bold">Planning Stage</span>
        </div>
    </div>
    """
}

