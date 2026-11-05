"""
Script to generate .agents/class6_science_ch3_sims.py containing 16 interactive simulators
for NCERT Class 6 Science Chapter 3: Mindful Eating: A Path to a Healthy Body.
"""

simulators = []

# Sim 1: Biological Power Plant
sim1 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>⚡🧬</span>
                <span>The Biological Power Plant: What Food Does Inside Us</span>
            </h3>
            <span id="sim1-badge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-400 border border-amber-500/20">Cellular Energy</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800/80">
            <svg id="sim1-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-4 gap-2">
            <button onclick="setSim1Function('energy')" id="sim1-btn-energy" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">⚡ Energy</button>
            <button onclick="setSim1Function('growth')" id="sim1-btn-growth" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🔨 Growth</button>
            <button onclick="setSim1Function('defense')" id="sim1-btn-defense" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🛡️ Immunity</button>
            <button onclick="setSim1Function('brain')" id="sim1-btn-brain" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🧠 Mind</button>
        </div>
        <p id="sim1-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim1)

# Sim 2: India's Regional Thali Explorer
sim2 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🍛🗺️</span>
                <span>Regional Thali Explorer: Crops, Climate & Culture</span>
            </h3>
            <span id="sim2-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Punjab</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim2-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim2Region('punjab')" id="sim2-btn-punjab" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🌾 Punjab (Makki-Saag)</button>
            <button onclick="setSim2Region('karnataka')" id="sim2-btn-karnataka" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🥥 Karnataka (Ragi-Dosa)</button>
            <button onclick="setSim2Region('manipur')" id="sim2-btn-manipur" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌿 Manipur (Eromba-Uttis)</button>
        </div>
        <p id="sim2-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim2)

# Sim 3: Culinary Evolution Timeline
sim3 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🔥⚡</span>
                <span>Kitchen Evolution: Traditional vs Modern Culinary Tools</span>
            </h3>
            <span id="sim3-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Mud Chulha</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim3-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-4 gap-2">
            <button onclick="setSim3Era('chulha')" id="sim3-btn-chulha" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🪵 Clay Chulha</button>
            <button onclick="setSim3Era('silbatta')" id="sim3-btn-silbatta" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🪨 Sil-Batta</button>
            <button onclick="setSim3Era('gas')" id="sim3-btn-gas" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🔥 LPG / Induction</button>
            <button onclick="setSim3Era('blender')" id="sim3-btn-blender" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">⚡ Mixer-Grinder</button>
        </div>
        <p id="sim3-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim3)

# Sim 4: Carbohydrate Fuel Meter
sim4 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🥔📈</span>
                <span>Carbohydrate Fuel Meter: Complex Starch vs Simple Sugar</span>
            </h3>
            <span id="sim4-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Complex Starch</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim4-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim4Carb('starch')" id="sim4-btn-starch" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🥔 Starch (Potato/Rice)</button>
            <button onclick="setSim4Carb('wholegrain')" id="sim4-btn-wholegrain" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌾 Whole Grain (Roti)</button>
            <button onclick="setSim4Carb('sugar')" id="sim4-btn-sugar" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🍬 Refined Sugar Spike</button>
        </div>
        <p id="sim4-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim4)

# Sim 5: The Lipid Calorie Vault
sim5 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🧈⚖️</span>
                <span>Fats: The Concentrated Energy Vault (9 kcal vs 4 kcal)</span>
            </h3>
            <span id="sim5-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Energy Density</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim5-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim5Fat('density')" id="sim5-btn-density" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">⚖️ Calorie Vault (9 kcal/g)</button>
            <button onclick="setSim5Fat('insulation')" id="sim5-btn-insulation" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🧤 Thermal Insulation</button>
            <button onclick="setSim5Fat('vitamins')" id="sim5-btn-vitamins" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🧬 Fat-Soluble Vitamins</button>
        </div>
        <p id="sim5-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim5)

# Sim 6: Protein Muscle & Growth Builder
sim6 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>💪🧱</span>
                <span>Proteins: Structural Blocks for Growth and Muscle Repair</span>
            </h3>
            <span id="sim6-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Soyabean (Plant King)</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim6-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim6Protein('soyabean')" id="sim6-btn-soyabean" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🌱 Soyabean (36% Protein)</button>
            <button onclick="setSim6Protein('pulses')" id="sim6-btn-pulses" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🥣 Pulses & Paneer</button>
            <button onclick="setSim6Protein('repair')" id="sim6-btn-repair" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🔨 Muscle Fiber Repair</button>
        </div>
        <p id="sim6-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim6)

# Sim 7: The Vitamin Protective Shield
sim7 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🛡️👁️</span>
                <span>Vitamins: The Micro-Nutrient Protective Shield</span>
            </h3>
            <span id="sim7-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Vitamin A (Eyesight)</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim7-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-4 gap-1.5">
            <button onclick="setSim7Vitamin('A')" id="sim7-btn-A" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🥕 Vit A (Eyes)</button>
            <button onclick="setSim7Vitamin('B')" id="sim7-btn-B" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌾 Vit B1 (Nerves)</button>
            <button onclick="setSim7Vitamin('C')" id="sim7-btn-C" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🍋 Vit C (Immunity)</button>
            <button onclick="setSim7Vitamin('D')" id="sim7-btn-D" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">☀️ Vit D (Sunlight)</button>
        </div>
        <p id="sim7-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim7)

# Sim 8: Essential Mineral Core Trio
sim8 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🦴🩸</span>
                <span>Mineral Core: Calcium, Iodine & Iron Foundations</span>
            </h3>
            <span id="sim8-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Calcium (Bones)</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim8-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim8Mineral('calcium')" id="sim8-btn-calcium" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🥛 Calcium (Bones/Teeth)</button>
            <button onclick="setSim8Mineral('iodine')" id="sim8-btn-iodine" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🧂 Iodine (Thyroid/Mind)</button>
            <button onclick="setSim8Mineral('iron')" id="sim8-btn-iron" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🥬 Iron (Hemoglobin/O2)</button>
        </div>
        <p id="sim8-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim8)

# Sim 9: Fiber & Water Motility Simulator
sim9 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>💧🌾</span>
                <span>Fiber & Water: Intestinal Motility & Toxic Waste Clearance</span>
            </h3>
            <span id="sim9-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Roughage Peristalsis</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim9-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <button onclick="setSim9Mode('fiber')" id="sim9-btn-fiber" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🌾 Roughage: Smooth Peristalsis</button>
            <button onclick="setSim9Mode('water')" id="sim9-btn-water" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">💧 Water: Filtration & Toxin Flush</button>
        </div>
        <p id="sim9-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim9)

# Sim 10: Starch Iodine Lab
sim10 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🧪🥔</span>
                <span>Food Lab 1: Testing for Starch with Dilute Iodine</span>
            </h3>
            <span id="sim10-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Ready for Test</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim10-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="runSim10Test('potato')" id="sim10-btn-potato" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🥔 Raw Potato (+ Starch)</button>
            <button onclick="runSim10Test('rice')" id="sim10-btn-rice" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🍚 Boiled Rice (+ Starch)</button>
            <button onclick="runSim10Test('butter')" id="sim10-btn-butter" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🧈 Butter (− Negative)</button>
        </div>
        <p id="sim10-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim10)

# Sim 11: Fat Translucent Paper Lab
sim11 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>📄🥜</span>
                <span>Food Lab 2: Testing for Fats via Translucent Spot</span>
            </h3>
            <span id="sim11-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Groundnut Sample</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim11-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="runSim11Test('peanut')" id="sim11-btn-peanut" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🥜 Crushed Peanut</button>
            <button onclick="runSim11Test('butter')" id="sim11-btn-butter" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🧈 Butter Smear</button>
            <button onclick="runSim11Test('water')" id="sim11-btn-water" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">💧 Water Drop (Dries Clear)</button>
        </div>
        <p id="sim11-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim11)

# Sim 12: Protein Biuret Lab
sim12 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🧪🥣</span>
                <span>Food Lab 3: Testing for Proteins (Biuret Reaction)</span>
            </h3>
            <span id="sim12-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Ready for Reagents</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim12-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="runSim12Step('dal')" id="sim12-btn-dal" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🥣 Boiled Dal (+ Protein)</button>
            <button onclick="runSim12Step('soya')" id="sim12-btn-soya" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌱 Soyabean (+ Protein)</button>
            <button onclick="runSim12Step('sugar')" id="sim12-btn-sugar" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🍬 Sugar Syrup (− Negative)</button>
        </div>
        <p id="sim12-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim12)

# Sim 13: The Balanced Thali Architect
sim13 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🥗🍽️</span>
                <span>The Balanced Thali: Proportioning Our Daily Nutrients</span>
            </h3>
            <span id="sim13-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Balanced Thali</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim13-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim13Diet('balanced')" id="sim13-btn-balanced" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🥗 Balanced Indian Thali</button>
            <button onclick="setSim13Diet('junk')" id="sim13-btn-junk" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🍟 Junk Food (Empty Calories)</button>
            <button onclick="setSim13Diet('fortified')" id="sim13-btn-fortified" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🏷️ Fortified Staples (+F)</button>
        </div>
        <p id="sim13-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim13)

# Sim 14: Millet Super Grain Harvest
sim14 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🌾💧</span>
                <span>Millets: Climate-Smart Indigenous Super Grains</span>
            </h3>
            <span id="sim14-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Ragi (High Calcium)</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim14-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-4 gap-2">
            <button onclick="setSim14Millet('ragi')" id="sim14-btn-ragi" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🌾 Ragi (Calcium)</button>
            <button onclick="setSim14Millet('bajra')" id="sim14-btn-bajra" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌾 Bajra (Iron)</button>
            <button onclick="setSim14Millet('jowar')" id="sim14-btn-jowar" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌾 Jowar (Fiber)</button>
            <button onclick="setSim14Millet('water')" id="sim14-btn-water" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">💧 Water Meter</button>
        </div>
        <p id="sim14-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim14)

# Sim 15: Food Miles & Carbon Footprint
sim15 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🚜✈️</span>
                <span>Food Miles: Farm to Plate Environmental Journey</span>
            </h3>
            <span id="sim15-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Local Farm (15 km)</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim15-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <button onclick="setSim15Miles('local')" id="sim15-btn-local" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🚜 Local Produce: 15 km (Low Carbon & Fresh)</button>
            <button onclick="setSim15Miles('imported')" id="sim15-btn-imported" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">✈️ Imported Produce: 8,000 km (High Carbon)</button>
        </div>
        <p id="sim15-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim15)

# Sim 16: Nutrition Science Pioneers
sim16 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>📖🔬</span>
                <span>Field Journal: Milestones in Nutrition Science</span>
            </h3>
            <span id="sim16-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">James Lind (1746)</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim16-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim16Hero('lind')" id="sim16-btn-lind" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🍋 James Lind (Scurvy 1746)</button>
            <button onclick="setSim16Hero('goitre')" id="sim16-btn-goitre" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🧂 Agariya & Iodised Salt</button>
            <button onclick="setSim16Hero('gopalan')" id="sim16-btn-gopalan" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🍚 Dr. C. Gopalan (PM POSHAN)</button>
        </div>
        <p id="sim16-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim16)

with open(".agents/class6_science_ch3_sims.py", "w", encoding="utf-8") as f:
    f.write('"""\nNCERT Class 6 Science Chapter 3: Simulators Module\n"""\n\n')
    f.write('SIMULATORS = ' + repr(simulators) + '\n')

print(f"Generated .agents/class6_science_ch3_sims.py with {len(simulators)} simulators.")

