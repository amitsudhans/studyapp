import re

sims = [
    # Sim 1: Spark of Curiosity
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🔍</span>
                <span>The Curiosity Magnifier: Asking 'Why?' in Nature</span>
            </h3>
            <span id="sim1-badge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">The Blue Sea</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800/80">
            <svg id="sim1-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim1Target('sea')" id="sim1-btn-sea" class="px-3 py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🌊 Blue Sea (Raman)</button>
            <button onclick="setSim1Target('leaf')" id="sim1-btn-leaf" class="px-3 py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🍃 Green Leaf</button>
            <button onclick="setSim1Target('sky')" id="sim1-btn-sky" class="px-3 py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">✨ Night Stars</button>
        </div>
        <p id="sim1-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
    """,

    # Sim 2: Science Everywhere
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🍳🌍</span>
                <span>Science in Everyday Domains</span>
            </h3>
            <span id="sim2-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Kitchen Science</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim2-svg" viewBox="0 0 450 190" class="w-full h-48 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-4 gap-2">
            <button onclick="setSim2Domain('kitchen')" id="sim2-btn-kitchen" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🍳 Kitchen</button>
            <button onclick="setSim2Domain('forest')" id="sim2-btn-forest" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌲 Forest</button>
            <button onclick="setSim2Domain('ocean')" id="sim2-btn-ocean" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🤿 Ocean</button>
            <button onclick="setSim2Domain('space')" id="sim2-btn-space" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🚀 Cosmos</button>
        </div>
        <p id="sim2-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 3: The Infinite Jigsaw
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🧩</span>
                <span>The Self-Correcting Jigsaw Puzzle of Science</span>
            </h3>
            <span id="sim3-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Pieces: 3 of 6</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex items-center justify-center">
            <div id="sim3-puzzle-board" class="grid grid-cols-3 gap-2 w-72 h-48 p-2 bg-slate-900 rounded-xl border border-slate-700"></div>
        </div>
        <div class="flex items-center justify-between gap-3">
            <button onclick="addSim3Piece()" id="sim3-add-btn" class="w-1/2 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-cyan-500 to-indigo-600 text-white transition">Discover New Evidence (+ Piece)</button>
            <button onclick="resetSim3Puzzle()" class="w-1/2 py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Re-arrange Old Model</button>
        </div>
        <p id="sim3-status" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 4: Earth's Living Quilt
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🌵❄️</span>
                <span>Habitat Adaptations Across Earth</span>
            </h3>
            <span id="sim4-habitat-title" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Desert Habitat</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim4-svg" viewBox="0 0 450 190" class="w-full h-48 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-4 gap-2">
            <button onclick="setSim4Habitat('desert')" id="sim4-btn-desert" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🏜️ Desert</button>
            <button onclick="setSim4Habitat('mountain')" id="sim4-btn-mountain" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🏔️ Mountain</button>
            <button onclick="setSim4Habitat('mangrove')" id="sim4-btn-mangrove" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌿 Mangrove</button>
            <button onclick="setSim4Habitat('reef')" id="sim4-btn-reef" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🐠 Coral Reef</button>
        </div>
        <p id="sim4-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 5: Miracles of Growth
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🌱🦋</span>
                <span>Transformations of Life: Seed to Tree & Caterpillar to Butterfly</span>
            </h3>
            <span id="sim5-stage-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Stage 1 of 4</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim5-svg" viewBox="0 0 450 190" class="w-full h-48 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <button onclick="setSim5Mode('plant')" id="sim5-btn-plant" class="py-2 rounded-xl text-xs font-bold bg-cyan-500 text-slate-950 transition">🌱 Seed Germination</button>
            <button onclick="setSim5Mode('butterfly')" id="sim5-btn-butterfly" class="py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🦋 Butterfly Metamorphosis</button>
        </div>
        <div class="flex items-center space-x-3 bg-slate-950/50 p-3 rounded-xl border border-slate-800">
            <span class="text-xs text-slate-400 font-medium whitespace-nowrap">Growth Stage:</span>
            <input type="range" id="sim5-slider" min="1" max="4" value="1" oninput="updateSim5()" class="w-full accent-emerald-400">
            <span id="sim5-slider-val" class="text-xs font-bold text-emerald-300 w-16 text-right">Step 1</span>
        </div>
        <p id="sim5-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 6: Cuisines & Nutrients
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🍛🥗</span>
                <span>The Balanced Thali: Designing a Healthy Indian Meal</span>
            </h3>
            <span id="sim6-health-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Assemble Meal</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex items-center justify-center">
            <div id="sim6-plate" class="relative w-56 h-56 rounded-full border-4 border-slate-600 bg-slate-900/80 p-3 flex items-center justify-center"></div>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="toggleSim6Food('carbs')" id="sim6-btn-carbs" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌾 Roti / Rice (Carbs)</button>
            <button onclick="toggleSim6Food('protein')" id="sim6-btn-protein" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🥣 Dal / Paneer (Protein)</button>
            <button onclick="toggleSim6Food('vitamins')" id="sim6-btn-vitamins" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🥬 Sabzi / Salad (Vitamins)</button>
        </div>
        <p id="sim6-status" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 7: The Journey of Water
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>☀️🌧️</span>
                <span>The Endless Water Cycle Loop</span>
            </h3>
            <span id="sim7-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Evaporation Active</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim7-svg" viewBox="0 0 450 190" class="w-full h-48 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="triggerSim7Phase('evap')" id="sim7-btn-evap" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">1. Evaporation (Solar)</button>
            <button onclick="triggerSim7Phase('cond')" id="sim7-btn-cond" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">2. Condensation (Clouds)</button>
            <button onclick="triggerSim7Phase('rain')" id="sim7-btn-rain" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">3. Precipitation (Rain)</button>
        </div>
        <p id="sim7-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 8: Three States of Matter
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🧊💧💨</span>
                <span>Molecular States of Water</span>
            </h3>
            <span id="sim8-state-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Liquid Water (25 °C)</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim8-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="flex items-center space-x-3 bg-slate-950/50 p-3 rounded-xl border border-slate-800">
            <span class="text-xs text-slate-400 font-medium whitespace-nowrap">Temperature:</span>
            <input type="range" id="sim8-temp" min="-20" max="120" value="25" oninput="updateSim8()" class="w-full accent-cyan-400">
            <span id="sim8-temp-val" class="font-mono text-xs font-bold text-cyan-300 w-16 text-right">25 °C</span>
        </div>
        <p id="sim8-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 9: Hot or Cold?
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🌡️</span>
                <span>The Three-Bowl Thermal Illusion Experiment</span>
            </h3>
            <span id="sim9-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Step 1: Prep Hands</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim9-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <button onclick="setSim9Step(1)" id="sim9-btn-step1" class="py-2.5 rounded-xl text-xs font-bold bg-cyan-500 text-slate-950 transition">Step 1: Cold & Hot Bowls</button>
            <button onclick="setSim9Step(2)" id="sim9-btn-step2" class="py-2.5 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Step 2: Both into Lukewarm Bowl</button>
        </div>
        <p id="sim9-explanation" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
    """,

    # Sim 10: Sorting Materials
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🧲⚡</span>
                <span>Material Property Analyzer: Magnetism & Conductivity</span>
            </h3>
            <span id="sim10-mat-title" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Iron Nail</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim10-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-4 gap-2">
            <button onclick="testSim10Material('iron')" id="sim10-btn-iron" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🔩 Iron Nail</button>
            <button onclick="testSim10Material('copper')" id="sim10-btn-copper" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🪙 Copper Coin</button>
            <button onclick="testSim10Material('plastic')" id="sim10-btn-plastic" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">📏 Plastic Ruler</button>
            <button onclick="testSim10Material('wood')" id="sim10-btn-wood" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">✏️ Wooden Stick</button>
        </div>
        <p id="sim10-status" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 11: Celestial Wonders
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>☀️🌍🌕</span>
                <span>Cosmic Dance: Sun, Earth & Moon</span>
            </h3>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Orbital Motion</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim11-svg" viewBox="0 0 450 190" class="w-full h-48 mx-auto"></svg>
        </div>
        <div class="flex items-center justify-center">
            <button onclick="toggleSim11Orbit()" id="sim11-orbit-btn" class="px-6 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-cyan-500 to-indigo-600 text-white shadow-lg shadow-cyan-500/20 hover:opacity-90 transition">
                Pause Cosmic Orbit
            </button>
        </div>
        <p id="sim11-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium">Earth revolves around the Sun every 365 days; the Moon orbits Earth every 27.3 days reflecting solar radiance.</p>
    </div>
    """,

    # Sim 12: The Scientific Method
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🖊️</span>
                <span>Troubleshooting the Ballpoint Pen: Scientific Inquiry</span>
            </h3>
            <span id="sim12-step-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Pen Won't Write!</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim12-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim12Action('check_ink')" id="sim12-btn-ink" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">Test 1: Check Refill Tube</button>
            <button onclick="setSim12Action('scribble')" id="sim12-btn-scribble" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Test 2: Scribble on Rough Page</button>
            <button onclick="setSim12Action('restore')" id="sim12-btn-restore" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Result: Ink Flows!</button>
        </div>
        <p id="sim12-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 13: Observe & Question
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>👀❓</span>
                <span>The Observation & Questioning Station</span>
            </h3>
            <span id="sim13-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Case 1: Rainbow</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim13-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim13Case('rainbow')" id="sim13-btn-rainbow" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🌈 Rainbow After Rain</button>
            <button onclick="setSim13Case('rust')" id="sim13-btn-rust" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🔩 Rusted Iron Gate</button>
            <button onclick="setSim13Case('firefly')" id="sim13-btn-firefly" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">✨ Glowing Firefly</button>
        </div>
        <p id="sim13-question-box" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
    """,

    # Sim 14: Hypothesize & Test
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🌱🔬</span>
                <span>Controlled Fair Test: Testing Sunlight on Plant Growth</span>
            </h3>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Single Variable Isolated</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim14-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <div class="bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-xs">
                <span class="text-emerald-400 font-bold block mb-1">Pot A (Sunlit):</span>
                <span>Soil: Same | Water: Same | Light: <strong>Full Sunlight (Variable)</strong></span>
            </div>
            <div class="bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-xs">
                <span class="text-rose-400 font-bold block mb-1">Pot B (Control):</span>
                <span>Soil: Same | Water: Same | Light: <strong>Dark Cupboard (Variable)</strong></span>
            </div>
        </div>
        <div class="flex items-center justify-center">
            <button onclick="runSim14Days()" id="sim14-run-btn" class="px-6 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-emerald-500 to-cyan-500 text-slate-950 shadow-lg hover:opacity-90 transition">
                Advance Time (7 Days)
            </button>
        </div>
        <p id="sim14-result" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 15: Analyze & Conclude
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>📊📈</span>
                <span>Data Analysis & Hypothesis Verdict</span>
            </h3>
            <span id="sim15-verdict-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Hypothesis Supported</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim15-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <button onclick="setSim15Scenario('support')" id="sim15-btn-sup" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">Data Matches Hypothesis</button>
            <button onclick="setSim15Scenario('refute')" id="sim15-btn-ref" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Data Refutes Hypothesis</button>
        </div>
        <p id="sim15-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 16: Everyday Scientists
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🔧🚴</span>
                <span>The Everyday Scientist: Mechanics & Trouble Diagnostics</span>
            </h3>
            <span id="sim16-role-title" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Bicycle Repairer</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim16-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim16Role('mechanic')" id="sim16-btn-mech" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🚴 Bicycle Tube (Bubbles)</button>
            <button onclick="setSim16Role('cook')" id="sim16-btn-cook" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🍲 Pressure Cooker Spout</button>
            <button onclick="setSim16Role('electrician')" id="sim16-btn-elec" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">💡 Faulty Light Circuit</button>
        </div>
        <p id="sim16-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
    """
]

# Verify zero raw LaTeX and zero surrogates in simulators
raw_latex_pattern = re.compile(r'\\[a-zA-Z]+')

for idx, s in enumerate(sims):
    matches = raw_latex_pattern.findall(s)
    if matches:
        raise ValueError(f"Found raw LaTeX in Sim {idx+1}: {set(matches)}")
    surrogates = [c for c in s if 0xD800 <= ord(c) <= 0xDFFF]
    if surrogates:
        raise ValueError(f"Found surrogates in Sim {idx+1}")

print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in all 16 Simulators!")

with open(".agents/class6_science_ch1_sims.py", "w", encoding="utf-8") as f:
    f.write('"""\nNCERT Class 6 Science Chapter 1: Simulators Module\n"""\n\n')
    f.write('SIMULATORS = ' + repr(sims) + '\n')

print("Successfully wrote .agents/class6_science_ch1_sims.py")
