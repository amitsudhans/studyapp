"""
Script to generate .agents/class6_science_ch2_sims.py containing 16 interactive simulators
for NCERT Class 6 Science Chapter 2: Diversity in the Living World.
"""

simulators = []

# Sim 1: Nature Walk Explorer
sim1 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🌲🔍</span>
                <span>The Nature Walk Explorer (Non-Intrusive Observation)</span>
            </h3>
            <span id="sim1-badge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Birdsong Chirp</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800/80">
            <svg id="sim1-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-4 gap-2">
            <button onclick="setSim1Spot('bird')" id="sim1-btn-bird" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🐦 Birdsong</button>
            <button onclick="setSim1Spot('tree')" id="sim1-btn-tree" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌳 Old Banyan</button>
            <button onclick="setSim1Spot('monkey')" id="sim1-btn-monkey" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🐒 Monkey Troops</button>
            <button onclick="setSim1Spot('butterfly')" id="sim1-btn-butterfly" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🦋 Butterfly</button>
        </div>
        <p id="sim1-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim1)

# Sim 2: Web of Biodiversity & Interdependence
sim2 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🕸️🌱</span>
                <span>The Web of Biodiversity & Mutual Interdependence</span>
            </h3>
            <span id="sim2-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Food & Shelter</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim2-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-4 gap-2">
            <button onclick="setSim2Link('shelter')" id="sim2-btn-shelter" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🏡 Shelter & Nest</button>
            <button onclick="setSim2Link('seed')" id="sim2-btn-seed" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🍒 Seed Dispersal</button>
            <button onclick="setSim2Link('pollinate')" id="sim2-btn-pollinate" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🐝 Pollination</button>
            <button onclick="setSim2Link('soil')" id="sim2-btn-soil" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🪱 Soil Nutrient Cycle</button>
        </div>
        <p id="sim2-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim2)

# Sim 3: Organism Classification Station
sim3 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🏷️📦</span>
                <span>The Classification Sorting Station</span>
            </h3>
            <span id="sim3-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Criterion: Stem Type</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim3-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim3Criterion('stem')" id="sim3-btn-stem" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🌿 Woody vs Green</button>
            <button onclick="setSim3Criterion('mobility')" id="sim3-btn-mobility" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🐾 Mobile vs Rooted</button>
            <button onclick="setSim3Criterion('habitat')" id="sim3-btn-habitat" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌊 Aquatic vs Land</button>
        </div>
        <p id="sim3-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
'''
simulators.append(sim3)

# Sim 4: Morphology Comparator (Trees, Shrubs & Herbs)
sim4 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🌳🌿</span>
                <span>Plant Architecture: Trees vs Shrubs vs Herbs</span>
            </h3>
            <span id="sim4-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Tree Architecture</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim4-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim4Category('tree')" id="sim4-btn-tree" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🌳 Tree (Mango/Neem)</button>
            <button onclick="setSim4Category('shrub')" id="sim4-btn-shrub" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌹 Shrub (Rose/Hibiscus)</button>
            <button onclick="setSim4Category('herb')" id="sim4-btn-herb" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌱 Herb (Tomato/Mint)</button>
        </div>
        <p id="sim4-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim4)

# Sim 5: Climbers vs Creepers
sim5 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🧗🍉</span>
                <span>Weak Stems: Climber Tendrils vs Creeper Ground Sprawl</span>
            </h3>
            <span id="sim5-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Climber (Pea Plant)</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim5-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <button onclick="setSim5Type('climber')" id="sim5-btn-climber" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🧗 Climber: Coiling Tendrils</button>
            <button onclick="setSim5Type('creeper')" id="sim5-btn-creeper" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🍉 Creeper: Ground Sprawl</button>
        </div>
        <p id="sim5-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim5)

# Sim 6: Leaf Venation Microscope
sim6 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🍃🔬</span>
                <span>Leaf Venation Under the Lens</span>
            </h3>
            <span id="sim6-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Reticulate Venation</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim6-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <button onclick="setSim6Venation('reticulate')" id="sim6-btn-reticulate" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🕸️ Reticulate (Net-like Veins)</button>
            <button onclick="setSim6Venation('parallel')" id="sim6-btn-parallel" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">📏 Parallel (Side-by-Side Veins)</button>
        </div>
        <p id="sim6-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim6)

# Sim 7: Root System Excavator
sim7 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🥕🌾</span>
                <span>Sub-Soil Root System Excavator</span>
            </h3>
            <span id="sim7-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Taproot Architecture</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim7-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <button onclick="setSim7Root('taproot')" id="sim7-btn-taproot" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🥕 Taproot (Mustard / Gram)</button>
            <button onclick="setSim7Root('fibrous')" id="sim7-btn-fibrous" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌾 Fibrous Root (Wheat / Grass)</button>
        </div>
        <p id="sim7-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim7)

# Sim 8: Golden Plant Rule
sim8 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>👑🌿</span>
                <span>The Golden Plant Rule: Botanical Correlation Trilogy</span>
            </h3>
            <span id="sim8-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Dicot Trio Active</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim8-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <button onclick="setSim8Plant('dicot')" id="sim8-btn-dicot" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🌱 Dicot: Reticulate ↔ Taproot ↔ 2 Cotyledons</button>
            <button onclick="setSim8Plant('monocot')" id="sim8-btn-monocot" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌾 Monocot: Parallel ↔ Fibrous ↔ 1 Cotyledon</button>
        </div>
        <p id="sim8-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim8)

# Sim 9: Seed Dissection Lab
sim9 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🥜🔬</span>
                <span>Seed Dissection: Cotyledons & Embryo</span>
            </h3>
            <span id="sim9-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Dicotyledon (Chickpea)</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim9-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <button onclick="setSim9Seed('dicot')" id="sim9-btn-dicot" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🥜 Chickpea / Gram (2 Cotyledons)</button>
            <button onclick="setSim9Seed('monocot')" id="sim9-btn-monocot" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌽 Maize Grain (1 Cotyledon)</button>
        </div>
        <p id="sim9-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim9)

# Sim 10: Animal Locomotion & Organs
sim10 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🐆🦅</span>
                <span>Animal Locomotion Modes & Specialized Organs</span>
            </h3>
            <span id="sim10-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Running: Muscular Limbs</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim10-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-5 gap-1.5">
            <button onclick="setSim10Mode('run')" id="sim10-btn-run" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🐆 Run</button>
            <button onclick="setSim10Mode('fly')" id="sim10-btn-fly" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🦅 Fly</button>
            <button onclick="setSim10Mode('swim')" id="sim10-btn-swim" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🐟 Swim</button>
            <button onclick="setSim10Mode('crawl')" id="sim10-btn-crawl" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🐍 Crawl</button>
            <button onclick="setSim10Mode('hop')" id="sim10-btn-hop" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🐸 Hop</button>
        </div>
        <p id="sim10-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim10)

# Sim 11: Habitats of the Earth
sim11 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🌍🏞️</span>
                <span>Earth Habitats & Environmental Pressures</span>
            </h3>
            <span id="sim11-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Terrestrial Forest</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim11-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-4 gap-2">
            <button onclick="setSim11Biome('forest')" id="sim11-btn-forest" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🌲 Forest</button>
            <button onclick="setSim11Biome('desert')" id="sim11-btn-desert" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🏜️ Desert</button>
            <button onclick="setSim11Biome('mountain')" id="sim11-btn-mountain" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">⛰️ Mountain</button>
            <button onclick="setSim11Biome('ocean')" id="sim11-btn-ocean" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌊 Aquatic</button>
        </div>
        <p id="sim11-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim11)

# Sim 12: Desert Adaptations Lab
sim12 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🏜️🐪</span>
                <span>Arid Desert Adaptations: Hot vs Cold Deserts</span>
            </h3>
            <span id="sim12-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Succulent Cactus</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim12-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim12Type('cactus')" id="sim12-btn-cactus" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🌵 Cactus</button>
            <button onclick="setSim12Type('hot_camel')" id="sim12-btn-hot" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🐪 Thar Camel (1 Hump)</button>
            <button onclick="setSim12Type('cold_camel')" id="sim12-btn-cold" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🐫 Ladakh Camel (2 Humps)</button>
        </div>
        <p id="sim12-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim12)

# Sim 13: Mountain Adaptations
sim13 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>❄️🐆</span>
                <span>High Mountain & Alpine Adaptations</span>
            </h3>
            <span id="sim13-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">Conical Deodar Tree</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim13-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <button onclick="setSim13Subject('conifer')" id="sim13-btn-conifer" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🌲 Deodar Conifer (Snow-Shedding)</button>
            <button onclick="setSim13Subject('leopard')" id="sim13-btn-leopard" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🐆 Snow Leopard (Padded Snowshoes)</button>
        </div>
        <p id="sim13-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim13)

# Sim 14: Ocean Life & Fins
sim14 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🌊🐟</span>
                <span>Marine Hydrodynamics: The Streamlined Swimmer</span>
            </h3>
            <span id="sim14-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Streamlined Spindle</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim14-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-4 gap-2">
            <button onclick="setSim14Feature('streamline')" id="sim14-btn-streamline" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🐟 Streamlined</button>
            <button onclick="setSim14Feature('fins')" id="sim14-btn-fins" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🦈 Fins & Tail</button>
            <button onclick="setSim14Feature('gills')" id="sim14-btn-gills" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🫧 Gills (O₂)</button>
            <button onclick="setSim14Feature('scales')" id="sim14-btn-scales" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🛡️ Slippery Scales</button>
        </div>
        <p id="sim14-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim14)

# Sim 15: Protecting Our Wild & Sacred Groves
sim15 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🐅🌳</span>
                <span>Conservation Milestones & Sacred Groves</span>
            </h3>
            <span id="sim15-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Project Tiger (1973)</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim15-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim15Reserve('tiger')" id="sim15-btn-tiger" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🐅 Project Tiger (1973)</button>
            <button onclick="setSim15Reserve('cheetah')" id="sim15-btn-cheetah" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🐆 Cheetah (Kuno 2022)</button>
            <button onclick="setSim15Reserve('groves')" id="sim15-btn-groves" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌳 Sacred Groves (Devrais)</button>
        </div>
        <p id="sim15-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim15)

# Sim 16: Heroes of Biodiversity Field Journal
sim16 = '''
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>📖🔬</span>
                <span>Field Journal: India's Biodiversity Legends</span>
            </h3>
            <span id="sim16-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Dr. E.K. Janaki Ammal</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim16-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <button onclick="setSim16Hero('ammal')" id="sim16-btn-ammal" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🌿 Dr. E.K. Janaki Ammal (Botanist)</button>
            <button onclick="setSim16Hero('ali')" id="sim16-btn-ali" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🐦 Dr. Salim Ali (Birdman of India)</button>
        </div>
        <p id="sim16-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
'''
simulators.append(sim16)

with open(".agents/class6_science_ch2_sims.py", "w", encoding="utf-8") as f:
    f.write('"""\nNCERT Class 6 Science Chapter 2: Simulators Module\n"""\n\n')
    f.write('SIMULATORS = ' + repr(simulators) + '\n')

print(f"Generated .agents/class6_science_ch2_sims.py with {len(simulators)} simulators.")

