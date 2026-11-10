# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 1: Living Together
Part 2 Simulators: Slides 9 to 16
Bespoke SVG/HTML interactive simulators.
Zero human names (replaced with generic roles).
Clean Unicode throughout.
"""

sim9 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-sky-500/20 text-sky-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Kanker Bamboo Bridge Simulator</h3>
        </div>
        <span class="text-xs text-sky-400 font-medium">48-Hour Rapid Build</span>
    </div>

    <!-- Timeline Progress Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="bridge-btn-0" onclick="setBridgeTimeline(0)" class="p-2 rounded-lg border border-sky-500 bg-sky-950/40 text-sky-300 font-bold ring-2 ring-sky-500 text-center">0h: Flooding</button>
        <button id="bridge-btn-12" onclick="setBridgeTimeline(12)" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium text-center">12h: Gather Bamboo</button>
        <button id="bridge-btn-24" onclick="setBridgeTimeline(24)" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium text-center">24h: Anchor Pillars</button>
        <button id="bridge-btn-48" onclick="setBridgeTimeline(48)" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium text-center">48h: Bridge Done!</button>
    </div>

    <!-- Interactive Visual Bridge River Scene -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[140px] space-y-2">
        <svg id="bridge-scene-svg" viewBox="0 0 300 100" class="w-full max-w-[280px] h-24">
            <!-- Dynamic river & bridge drawn by JS -->
        </svg>
        <div id="bridge-log-desc" class="text-xs text-slate-300 text-center leading-relaxed">
            Hour 0: Torrential rain causes the Chinar river to overflow, submerging the culvert and isolating 1,000 villagers.
        </div>
    </div>
</div>
"""

sim10 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Teamwork in Nature (Insects)</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Division of Labor</span>
    </div>

    <!-- Colony Switcher -->
    <div class="flex items-center justify-center gap-3">
        <button id="insect-tab-ant" onclick="selectInsectColony('ant')" class="px-4 py-1.5 rounded-lg border border-indigo-500 bg-indigo-950/40 text-indigo-300 font-bold ring-2 ring-indigo-500 text-xs">🐜 Ant Colony Nest</button>
        <button id="insect-tab-bee" onclick="selectInsectColony('bee')" class="px-4 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium text-xs">🐝 Honeybee Hive</button>
    </div>

    <!-- Colony Roles Interactive Display -->
    <div id="colony-display-box" class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <!-- Injected by JS -->
    </div>
</div>
"""

sim11 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Communal Feast Organizer</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Eco-Friendly Sharing</span>
    </div>

    <!-- Dish Selections -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button onclick="toggleFeastItem('rice')" id="feast-btn-rice" class="p-2 rounded-lg border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold">🍚 Steamed Rice</button>
        <button onclick="toggleFeastItem('dal')" id="feast-btn-dal" class="p-2 rounded-lg border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold">🥣 Lentil Curry</button>
        <button onclick="toggleFeastItem('veg')" id="feast-btn-veg" class="p-2 rounded-lg border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold">🥗 Mixed Greens</button>
        <button onclick="toggleFeastItem('lassi')" id="feast-btn-lassi" class="p-2 rounded-lg border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold">🥛 Buttermilk</button>
    </div>

    <!-- Banana Leaf Plate Visual Preview -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col items-center justify-center space-y-3">
        <div id="banana-leaf-plate" class="w-full max-w-xs h-28 bg-emerald-700/80 rounded-3xl border-2 border-emerald-400 p-3 shadow-inner flex flex-wrap items-center justify-center gap-2 text-xl">
            <span>🍚</span><span>🥣</span><span>🥗</span><span>🥛</span>
        </div>
        <div class="flex items-center justify-between w-full text-xs text-slate-400 px-2">
            <span>Serving Surface: <strong>Fresh Banana Leaf</strong></span>
            <span class="text-emerald-400 font-bold">Plastic Waste: 0 grams</span>
        </div>
    </div>
</div>
"""

sim12 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Organic Compost Decomposer</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Circular Ecology</span>
    </div>

    <!-- Time Slider -->
    <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2">
        <div class="flex items-center justify-between text-xs text-slate-300">
            <span>Day 1 (Fresh Leaves)</span>
            <span id="compost-week-badge" class="font-mono text-amber-400 font-bold">Week 1: Fresh Green Matter</span>
            <span>Week 8 (Rich Humus)</span>
        </div>
        <input type="range" id="compost-slider" min="1" max="8" value="1" oninput="updateCompostStage(this.value)" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
    </div>

    <!-- Layer Graphic Box -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[140px] space-y-2">
        <div id="compost-visual-box" class="w-full max-w-[280px] h-24 rounded-xl border border-slate-700 flex flex-col justify-end p-2 transition-colors">
            <!-- Layers colored by JS -->
        </div>
        <p id="compost-stage-desc" class="text-xs text-slate-300 text-center">
            Week 1: Fresh used banana leaves and vegetable scraps layered with dry leaves and soil inoculant.
        </p>
    </div>
</div>
"""

sim13 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-purple-500/20 text-purple-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Regional Traditions Showcase</h3>
        </div>
        <span class="text-xs text-purple-400 font-medium">Cultural Solidarity</span>
    </div>

    <!-- Region Selector -->
    <div class="flex items-center justify-center gap-3">
        <button id="trad-btn-assam" onclick="selectRegionalTradition('assam')" class="px-4 py-1.5 rounded-lg border border-purple-500 bg-purple-950/40 text-purple-300 font-bold ring-2 ring-purple-500 text-xs">Assam: Uruka & Bhela Ghar</button>
        <button id="trad-btn-sikkim" onclick="selectRegionalTradition('sikkim')" class="px-4 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium text-xs">Sikkim: Khetala Farming</button>
    </div>

    <!-- Regional Feature Display -->
    <div id="tradition-feature-box" class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <!-- Injected by JS -->
    </div>
</div>
"""

sim14 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-rose-500/20 text-rose-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">School Interdependence Matrix</h3>
        </div>
        <span class="text-xs text-rose-400 font-medium">Educational Team</span>
    </div>

    <!-- School Role Tabs -->
    <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs">
        <button onclick="selectSchoolRole('teacher')" id="sch-btn-teacher" class="p-2 rounded-lg border border-rose-500 bg-rose-950/40 text-rose-300 font-bold ring-2 ring-rose-500">👩‍🏫 Teachers</button>
        <button onclick="selectSchoolRole('student')" id="sch-btn-student" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">🎒 Students</button>
        <button onclick="selectSchoolRole('caretaker')" id="sch-btn-caretaker" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">🧹 Caretakers</button>
        <button onclick="selectSchoolRole('driver')" id="sch-btn-driver" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">🚌 Bus Drivers</button>
        <button onclick="selectSchoolRole('guard')" id="sch-btn-guard" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">🛡️ Security Guard</button>
        <button onclick="selectSchoolRole('principal')" id="sch-btn-principal" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">🏛️ Principal</button>
    </div>

    <!-- Role Impact Box -->
    <div id="school-role-box" class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs text-slate-300 leading-relaxed">
        <strong>Teachers:</strong> Inspire young minds, explain scientific concepts, guide ethical behavior, and encourage creative experimentation every day.
    </div>
</div>
"""

sim15 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Student Action Project Planner</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Collaborative Projects</span>
    </div>

    <!-- Action Project Tabs -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button id="proj-tab-clean" onclick="selectActionProject('clean')" class="px-3 py-1.5 rounded-lg border border-teal-500 bg-teal-950/40 text-teal-300 font-bold ring-2 ring-teal-500">Campus Cleanliness</button>
        <button id="proj-tab-garden" onclick="selectActionProject('garden')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Herbal Garden</button>
        <button id="proj-tab-craft" onclick="selectActionProject('craft')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Nature Crafts</button>
    </div>

    <!-- Project Blueprint Card -->
    <div id="action-project-card" class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <!-- Populated by JS -->
    </div>
</div>
"""

sim16 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-yellow-500/20 text-yellow-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Public Riddles & Crafts Studio</h3>
        </div>
        <span class="text-xs text-yellow-400 font-medium">Deduction & Heritage</span>
    </div>

    <!-- Riddles Grid -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button onclick="revealRiddle('bus')" class="p-2.5 rounded-xl border border-slate-800 bg-slate-950 hover:bg-slate-800 text-center">
            <span class="text-xl block">🚌</span>
            <span class="font-bold text-slate-300">Riddle 1</span>
        </button>
        <button onclick="revealRiddle('post')" class="p-2.5 rounded-xl border border-slate-800 bg-slate-950 hover:bg-slate-800 text-center">
            <span class="text-xl block">📮</span>
            <span class="font-bold text-slate-300">Riddle 2</span>
        </button>
        <button onclick="revealRiddle('market')" class="p-2.5 rounded-xl border border-slate-800 bg-slate-950 hover:bg-slate-800 text-center">
            <span class="text-xl block">🛒</span>
            <span class="font-bold text-slate-300">Riddle 3</span>
        </button>
        <button onclick="revealRiddle('park')" class="p-2.5 rounded-xl border border-slate-800 bg-slate-950 hover:bg-slate-800 text-center">
            <span class="text-xl block">🌳</span>
            <span class="font-bold text-slate-300">Riddle 4</span>
        </button>
    </div>

    <!-- Riddle & Craft Output Area -->
    <div id="riddle-output-box" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed min-h-[90px] flex flex-col justify-center">
        Click any of the riddle buttons above to reveal clues about essential public landmarks in our community!
    </div>
</div>
"""

simulators_part2 = {
    9: sim9,
    10: sim10,
    11: sim11,
    12: sim12,
    13: sim13,
    14: sim14,
    15: sim15,
    16: sim16,
}

