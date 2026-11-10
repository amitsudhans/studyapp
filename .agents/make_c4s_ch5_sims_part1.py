# -*- coding: utf-8 -*-
"""Class 4 Science Chapter 5: Food for Health - Simulators 1-8"""

sims_part1 = {
    "sim-1": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">🇮🇳 Pan-Indian Regional Food Explorer</h4>
                <p class="text-xs text-slate-400">Select an Indian region to examine traditional dishes, local crops, and health benefits</p>
            </div>
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" id="sim1-badge">Western India</span>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="setRegionalDish('west')" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-amber-300 transition text-center">Western India</button>
            <button onclick="setRegionalDish('north')" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-emerald-300 transition text-center">Northern India</button>
            <button onclick="setRegionalDish('east')" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-cyan-300 transition text-center">Eastern India</button>
            <button onclick="setRegionalDish('south')" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-rose-300 transition text-center">Southern India</button>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col sm:flex-row items-center gap-4">
            <div id="sim1-dish-icon" class="text-5xl sm:text-6xl p-4 bg-slate-900 rounded-2xl border border-slate-700 shadow-inner flex items-center justify-center">🧆</div>
            <div class="flex-1 space-y-1.5 text-center sm:text-left">
                <div class="flex items-center justify-center sm:justify-start gap-2">
                    <span id="sim1-dish-name" class="text-base font-bold text-white">Steamed Dhokla</span>
                    <span id="sim1-state" class="text-xs text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20 font-medium">Gujarat</span>
                </div>
                <p id="sim1-dish-ingredients" class="text-xs text-slate-300">Fermented gram flour (besan), ginger, turmeric, and light mustard tempering.</p>
                <div class="pt-2 flex flex-wrap items-center justify-center sm:justify-start gap-2 text-[11px]">
                    <span class="bg-emerald-950 text-emerald-300 border border-emerald-800 px-2 py-0.5 rounded">Nutritional Highlight:</span>
                    <span id="sim1-benefit" class="text-slate-300">Light, easily digestible plant protein enriched by fermentation.</span>
                </div>
            </div>
        </div>
    </div>
    """,

    "sim-2": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">🥣 Ugadi Pachadi Multi-Taste Blender</h4>
                <p class="text-xs text-slate-400">Click ingredients to blend all six distinct tastes into the festive bowl</p>
            </div>
            <button onclick="resetPachadi()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-300 border border-slate-700">Reset Bowl</button>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
            <button onclick="addPachadiIngredient('neem')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-left flex items-center gap-2 text-xs">
                <span class="text-lg">🌿</span>
                <div><div class="font-bold text-emerald-400">Neem Flowers</div><div class="text-[10px] text-slate-400">Bitter (Tikta)</div></div>
            </button>
            <button onclick="addPachadiIngredient('jaggery')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-left flex items-center gap-2 text-xs">
                <span class="text-lg">🍯</span>
                <div><div class="font-bold text-amber-400">Jaggery</div><div class="text-[10px] text-slate-400">Sweet (Madhura)</div></div>
            </button>
            <button onclick="addPachadiIngredient('mango')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-left flex items-center gap-2 text-xs">
                <span class="text-lg">🥭</span>
                <div><div class="font-bold text-lime-400">Raw Mango</div><div class="text-[10px] text-slate-400">Astringent & Sour</div></div>
            </button>
            <button onclick="addPachadiIngredient('tamarind')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-left flex items-center gap-2 text-xs">
                <span class="text-lg">🫒</span>
                <div><div class="font-bold text-yellow-500">Tamarind Juice</div><div class="text-[10px] text-slate-400">Sour (Amla)</div></div>
            </button>
            <button onclick="addPachadiIngredient('salt')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-left flex items-center gap-2 text-xs">
                <span class="text-lg">🧂</span>
                <div><div class="font-bold text-cyan-400">Rock Salt</div><div class="text-[10px] text-slate-400">Salty (Lavana)</div></div>
            </button>
            <button onclick="addPachadiIngredient('chili')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-left flex items-center gap-2 text-xs">
                <span class="text-lg">🌶️</span>
                <div><div class="font-bold text-rose-400">Green Chili</div><div class="text-[10px] text-slate-400">Pungent (Katu)</div></div>
            </button>
        </div>
        <div class="bg-slate-950/90 rounded-xl p-3 border border-slate-800 flex flex-col gap-2">
            <div class="flex items-center justify-between text-xs font-semibold">
                <span>Flavor Harmony: <span id="sim2-count" class="text-amber-400">0 of 6 Tastes Added</span></span>
                <span id="sim2-status" class="text-slate-400">Bowl is Empty</span>
            </div>
            <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                <div id="sim2-progress" class="bg-gradient-to-r from-emerald-500 via-amber-500 to-rose-500 h-2 w-0 transition-all duration-300"></div>
            </div>
            <div id="sim2-bowl-tags" class="flex flex-wrap gap-1.5 pt-1 min-h-[26px]">
                <span class="text-[10px] text-slate-500 italic">No ingredients mixed yet.</span>
            </div>
        </div>
    </div>
    """,

    "sim-3": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">☸️ Ayurvedic Shad Rasa Taste Wheel</h4>
                <p class="text-xs text-slate-400">Explore the six classical tastes and their physiological health actions</p>
            </div>
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 font-semibold" id="sim3-badge">Madhura (Sweet)</span>
        </div>
        <div class="grid grid-cols-3 sm:grid-cols-6 gap-1.5">
            <button onclick="selectRasa('sweet')" class="px-2 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-center text-xs font-bold text-amber-300">Sweet</button>
            <button onclick="selectRasa('sour')" class="px-2 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-center text-xs font-bold text-lime-300">Sour</button>
            <button onclick="selectRasa('salty')" class="px-2 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-center text-xs font-bold text-cyan-300">Salty</button>
            <button onclick="selectRasa('pungent')" class="px-2 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-center text-xs font-bold text-rose-300">Pungent</button>
            <button onclick="selectRasa('bitter')" class="px-2 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-center text-xs font-bold text-emerald-300">Bitter</button>
            <button onclick="selectRasa('astringent')" class="px-2 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-center text-xs font-bold text-purple-300">Astringent</button>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col sm:flex-row items-center gap-4">
            <div id="sim3-icon" class="text-5xl p-3 bg-slate-900 rounded-2xl border border-slate-700 shadow-inner flex items-center justify-center">🍯</div>
            <div class="flex-1 space-y-1.5 text-center sm:text-left">
                <div class="flex items-center justify-center sm:justify-start gap-2">
                    <span id="sim3-sanskrit" class="text-base font-bold text-white">Madhura Rasa</span>
                    <span id="sim3-action-tag" class="text-xs text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20 font-medium">Energy & Tissue Growth</span>
                </div>
                <div class="text-xs text-slate-300"><strong>Natural Sources:</strong> <span id="sim3-sources">Ripe fruits, pure honey, whole grains, sugarcane, sweet potato.</span></div>
                <div class="text-xs text-slate-400"><strong>Physiological Role:</strong> <span id="sim3-role">Builds bodily tissues, supplies sustained cellular energy, and calms nerve excitement.</span></div>
            </div>
        </div>
    </div>
    """,

    "sim-4": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">🌾 Climate-Smart Millet Superfood Analyzer</h4>
                <p class="text-xs text-slate-400">Inspect the mineral density and climate resilience of ancient Indian millets</p>
            </div>
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" id="sim4-badge">Ragi (Finger Millet)</span>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="inspectMillet('ragi')" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-amber-300 text-center">Ragi (Finger Millet)</button>
            <button onclick="inspectMillet('bajra')" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-emerald-300 text-center">Bajra (Pearl Millet)</button>
            <button onclick="inspectMillet('jowar')" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-cyan-300 text-center">Jowar (Sorghum)</button>
            <button onclick="inspectMillet('barley')" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-purple-300 text-center">Barley (Jau)</button>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div class="space-y-1">
                <span class="text-xs text-slate-400 font-semibold">Calcium (Bone Mineral):</span>
                <div class="w-full bg-slate-800 h-2.5 rounded-full overflow-hidden">
                    <div id="sim4-bar-calcium" class="bg-amber-400 h-2.5 w-[95%] transition-all duration-300"></div>
                </div>
                <span id="sim4-val-calcium" class="text-[11px] text-amber-300 font-bold">344 mg / 100g (Highest)</span>
            </div>
            <div class="space-y-1">
                <span class="text-xs text-slate-400 font-semibold">Iron (Blood Oxygen):</span>
                <div class="w-full bg-slate-800 h-2.5 rounded-full overflow-hidden">
                    <div id="sim4-bar-iron" class="bg-rose-400 h-2.5 w-[60%] transition-all duration-300"></div>
                </div>
                <span id="sim4-val-iron" class="text-[11px] text-rose-300 font-bold">3.9 mg / 100g</span>
            </div>
            <div class="space-y-1">
                <span class="text-xs text-slate-400 font-semibold">Dietary Fiber (Digestion):</span>
                <div class="w-full bg-slate-800 h-2.5 rounded-full overflow-hidden">
                    <div id="sim4-bar-fiber" class="bg-emerald-400 h-2.5 w-[85%] transition-all duration-300"></div>
                </div>
                <span id="sim4-val-fiber" class="text-[11px] text-emerald-300 font-bold">11.5 g / 100g</span>
            </div>
        </div>
        <div class="text-xs text-slate-300 bg-slate-950 p-2.5 rounded-xl border border-slate-800">
            <strong>Traditional Delicacy:</strong> <span id="sim4-dish">Steamed Ragi Laddu and Ragi Mudde with vegetable stew.</span>
        </div>
    </div>
    """,

    "sim-5": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">🧬 Nutrient Synergy Biological Engine</h4>
                <p class="text-xs text-slate-400">Click a nutrient to observe how it activates specific biological organ systems</p>
            </div>
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" id="sim5-badge">Synergy Active</span>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-5 gap-2">
            <button onclick="activateSynergy('carbs')" class="px-2 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-amber-300 text-center">Carbohydrates</button>
            <button onclick="activateSynergy('protein')" class="px-2 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-emerald-300 text-center">Proteins</button>
            <button onclick="activateSynergy('fat')" class="px-2 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-cyan-300 text-center">Healthy Fats</button>
            <button onclick="activateSynergy('vitamins')" class="px-2 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-rose-300 text-center">Vitamins</button>
            <button onclick="activateSynergy('minerals')" class="px-2 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-purple-300 text-center">Minerals</button>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex items-center gap-4">
            <div id="sim5-icon" class="text-4xl p-3 bg-slate-900 rounded-xl border border-slate-700">⚡</div>
            <div class="space-y-1">
                <div class="text-sm font-bold text-white" id="sim5-organ">Brain & Muscle Cellular Fuel</div>
                <p class="text-xs text-slate-300" id="sim5-desc">Breaks down into circulating blood glucose, powering cognitive focus in class and active sprinting on the playground.</p>
                <div class="text-[11px] text-amber-400" id="sim5-example">Top Sources: Brown rice, whole wheat rotis, sweet potatoes, and millets.</div>
            </div>
        </div>
    </div>
    """,

    "sim-6": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">🔥 Metabolic Energy Calorie Meter</h4>
                <p class="text-xs text-slate-400">Compare energy density between carbohydrates and fats per gram</p>
            </div>
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30 font-semibold">4 kcal vs 9 kcal</span>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <div onclick="selectCalorieFuel('carb')" class="cursor-pointer p-3 rounded-xl bg-slate-950/80 border border-slate-800 hover:border-amber-500/50 transition">
                <div class="flex items-center justify-between mb-2">
                    <span class="font-bold text-xs text-amber-300">🍞 1g Carbohydrate</span>
                    <span class="text-xs text-slate-400">4 kcal</span>
                </div>
                <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                    <div class="bg-amber-400 h-2 w-[44%]"></div>
                </div>
                <p class="text-[11px] text-slate-400 mt-2">Fast, clean-burning glucose for daily study and playtime.</p>
            </div>
            <div onclick="selectCalorieFuel('fat')" class="cursor-pointer p-3 rounded-xl bg-slate-950/80 border border-slate-800 hover:border-rose-500/50 transition">
                <div class="flex items-center justify-between mb-2">
                    <span class="font-bold text-xs text-rose-300">🧈 1g Healthy Fat</span>
                    <span class="text-xs text-slate-400">9 kcal</span>
                </div>
                <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                    <div class="bg-rose-400 h-2 w-[100%]"></div>
                </div>
                <p class="text-[11px] text-slate-400 mt-2">More than 2x concentrated energy reserve and organ insulation.</p>
            </div>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs text-slate-300 flex items-center justify-between">
            <span id="sim6-readout">Click a nutrient tile above to test kinetic fuel release.</span>
            <span id="sim6-gauge" class="text-amber-400 font-bold">⚡ Ready</span>
        </div>
    </div>
    """,

    "sim-7": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">💪 Protein Cellular Muscle Builder</h4>
                <p class="text-xs text-slate-400">Simulate microscopic muscle fiber repair after physical activity</p>
            </div>
            <button onclick="repairMuscleFiber()" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white transition">Supply Protein</button>
        </div>
        <div class="bg-slate-950/90 rounded-xl p-4 border border-slate-800 flex flex-col items-center gap-3">
            <div class="w-full flex items-center justify-around">
                <div class="text-center">
                    <div id="sim7-fiber1" class="w-20 h-3 bg-rose-500 rounded transition-all duration-300"></div>
                    <span class="text-[10px] text-slate-400 mt-1 block">Muscle Strand A</span>
                </div>
                <div class="text-2xl" id="sim7-bridge">⚡</div>
                <div class="text-center">
                    <div id="sim7-fiber2" class="w-20 h-3 bg-rose-500 rounded transition-all duration-300"></div>
                    <span class="text-[10px] text-slate-400 mt-1 block">Muscle Strand B</span>
                </div>
            </div>
            <div class="w-full bg-slate-900 rounded-lg p-2.5 border border-slate-800 text-xs text-center">
                <span id="sim7-status" class="text-amber-300 font-semibold">Tissues fatigued after sports play. Click 'Supply Protein' to weave new fibers!</span>
            </div>
            <div class="flex items-center gap-2 text-[11px] text-slate-400">
                <span>Top Protein Sources:</span>
                <span class="text-emerald-300 font-semibold">Soybeans (Highest) • Dal Lentils • Paneer • Milk • Eggs</span>
            </div>
        </div>
    </div>
    """,

    "sim-8": """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div>
                <h4 class="text-sm font-bold text-amber-300">🛡️ Immune Shield Vitamin Defender</h4>
                <p class="text-xs text-slate-400">Deploy protective fruits and vegetables to ward off invading pathogens</p>
            </div>
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" id="sim8-score">Shield: 100%</span>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="deployShield('amla')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-center text-xs">
                <div class="text-2xl mb-1">🍈</div>
                <div class="font-bold text-emerald-300">Amla (Vit C)</div>
                <div class="text-[10px] text-slate-400">White Blood Cells</div>
            </button>
            <button onclick="deployShield('carrot')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-center text-xs">
                <div class="text-2xl mb-1">🥕</div>
                <div class="font-bold text-amber-300">Carrot (Vit A)</div>
                <div class="text-[10px] text-slate-400">Vision & Skin</div>
            </button>
            <button onclick="deployShield('spinach')" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-center text-xs">
                <div class="text-2xl mb-1">🥬</div>
                <div class="font-bold text-lime-300">Spinach (Iron)</div>
                <div class="text-[10px] text-slate-400">Red Blood Cells</div>
            </button>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 text-xs flex items-center justify-between">
            <span id="sim8-msg">Click a protective food above to reinforce internal immune defenses!</span>
            <span id="sim8-badge" class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold">Protected</span>
        </div>
    </div>
    """
}

