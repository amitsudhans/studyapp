# -*- coding: utf-8 -*-
"""Class 4 Science Chapter 1 Simulators Dictionary"""

SIMULATORS = {
    1: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">01</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Village Community Explorer</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Shared Spaces</span>
    </div>

    <!-- Landmark Selector Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="vce-btn-banyan" onclick="selectVillageLandmark('banyan')" class="p-2.5 rounded-xl border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold ring-2 ring-emerald-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🌳</span>
            <span>Banyan Tree</span>
        </button>
        <button id="vce-btn-ground" onclick="selectVillageLandmark('ground')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🏃</span>
            <span>Playground</span>
        </button>
        <button id="vce-btn-well" onclick="selectVillageLandmark('well')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">💧</span>
            <span>Village Well</span>
        </button>
        <button id="vce-btn-chopal" onclick="selectVillageLandmark('chopal')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🏛️</span>
            <span>Panchayat Hall</span>
        </button>
    </div>

    <!-- Interactive Visual Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="vce-visual-box" class="min-h-[110px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic SVG illustration rendered by JS -->
        </div>
        <div id="vce-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-emerald-950/20 border border-emerald-800/40 leading-relaxed">
            <strong class="text-emerald-400">The Grand Banyan Tree:</strong> Features vast spreading branches and aerial roots where elders congregate daily for councils, sharing wisdom, and discussing village welfare.
        </div>
    </div>
</div>
''',
    2: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">02</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Community Services Matcher</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Interdependence</span>
    </div>

    <!-- Service Cards Grid -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
        <button onclick="selectServiceCard('health')" id="srv-btn-health" class="p-3 rounded-xl border border-cyan-500 bg-cyan-950/40 text-left hover:bg-cyan-900/30 transition-all flex items-start gap-2.5 ring-2 ring-cyan-500">
            <span class="text-xl">🏥</span>
            <div>
                <span class="font-bold text-white block">Primary Health Center</span>
                <span class="text-[11px] text-cyan-300">Doctors, nurses, immunizations</span>
            </div>
        </button>

        <button onclick="selectServiceCard('police')" id="srv-btn-police" class="p-3 rounded-xl border border-slate-700 bg-slate-800 text-left hover:bg-slate-700 transition-all flex items-start gap-2.5">
            <span class="text-xl">👮</span>
            <div>
                <span class="font-bold text-white block">Police Post</span>
                <span class="text-[11px] text-slate-400">Safety, traffic, conflict resolution</span>
            </div>
        </button>

        <button onclick="selectServiceCard('school')" id="srv-btn-school" class="p-3 rounded-xl border border-slate-700 bg-slate-800 text-left hover:bg-slate-700 transition-all flex items-start gap-2.5">
            <span class="text-xl">🏫</span>
            <div>
                <span class="font-bold text-white block">Primary School</span>
                <span class="text-[11px] text-slate-400">Teachers, knowledge, civic values</span>
            </div>
        </button>

        <button onclick="selectServiceCard('grocery')" id="srv-btn-grocery" class="p-3 rounded-xl border border-slate-700 bg-slate-800 text-left hover:bg-slate-700 transition-all flex items-start gap-2.5">
            <span class="text-xl">🌾</span>
            <div>
                <span class="font-bold text-white block">Local Grocery Store</span>
                <span class="text-[11px] text-slate-400">Fresh grains, pulses, dairy & supplies</span>
            </div>
        </button>
    </div>

    <!-- Impact Details Box -->
    <div id="srv-detail-box" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
        <strong>Community Lifeline:</strong> The Health Center guarantees prompt emergency first-aid, free child immunizations, and prenatal healthcare for rural mothers.
    </div>
</div>
''',
    3: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">03</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Clean Park Stewardship</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Civic Action</span>
    </div>

    <!-- Cleanliness Progress Meter -->
    <div class="space-y-1.5">
        <div class="flex items-center justify-between text-xs">
            <span class="text-slate-300 font-medium">Public Park Cleanliness Score:</span>
            <span id="steward-score-badge" class="font-mono font-bold text-teal-400">40% Clean</span>
        </div>
        <div class="w-full bg-slate-950 h-3 rounded-full overflow-hidden border border-slate-800">
            <div id="steward-progress-bar" class="bg-gradient-to-r from-amber-500 to-teal-500 h-full transition-all duration-300" style="width: 40%"></div>
        </div>
    </div>

    <!-- Action Buttons -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
        <button id="act-btn-litter" onclick="performCleanAction('litter')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium flex items-center justify-center gap-2">
            <span>🗑️</span> Bin Litter (+20%)
        </button>
        <button id="act-btn-tap" onclick="performCleanAction('tap')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium flex items-center justify-center gap-2">
            <span>🚰</span> Fix Leaking Tap (+20%)
        </button>
        <button id="act-btn-bench" onclick="performCleanAction('bench')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium flex items-center justify-center gap-2">
            <span>🪑</span> Wipe Benches (+20%)
        </button>
    </div>

    <!-- Visual Park Status Preview -->
    <div id="steward-feedback-box" class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs text-slate-300 text-center">
        Click the civic action buttons above to clean up debris and restore the community park.
    </div>
</div>
''',
    4: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-green-500/20 text-green-300 font-bold flex items-center justify-center text-sm">04</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Van Mahotsav Species Guide</h3>
        </div>
        <span class="text-xs text-green-400 font-medium">Native Flora</span>
    </div>

    <!-- Tree Selector Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs">
        <button onclick="selectTreeSpecies('neem')" id="tree-btn-neem" class="p-2.5 rounded-xl border border-green-500 bg-green-950/40 text-green-300 font-bold ring-2 ring-green-500">🌿 Neem</button>
        <button onclick="selectTreeSpecies('peepal')" id="tree-btn-peepal" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">🍃 Sacred Peepal</button>
        <button onclick="selectTreeSpecies('banyan')" id="tree-btn-banyan" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">🌳 Banyan</button>
        <button onclick="selectTreeSpecies('gulmohar')" id="tree-btn-gulmohar" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">🌺 Gulmohar</button>
        <button onclick="selectTreeSpecies('amaltas')" id="tree-btn-amaltas" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">🌼 Golden Amaltas</button>
        <button onclick="selectTreeSpecies('jamun')" id="tree-btn-jamun" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">🍇 Jamun</button>
    </div>

    <!-- Species Profile Card -->
    <div id="tree-profile-card" class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-center gap-4">
        <div id="tree-avatar" class="text-4xl p-3 bg-green-950/30 rounded-2xl border border-green-800/40 shrink-0">🌿</div>
        <div class="space-y-1">
            <h4 id="tree-name" class="font-bold text-white text-sm sm:text-base">Neem (Azadirachta indica)</h4>
            <p id="tree-desc" class="text-xs text-slate-300 leading-relaxed">Known as the village pharmacy. Highly drought-tolerant, repels harmful insects, cleans ambient air, and provides valuable medicinal leaves and twigs.</p>
        </div>
    </div>
</div>
''',
    5: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">05</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Community Poster Designer</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Creative Outreach</span>
    </div>

    <!-- Poster Controls -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div>
            <label class="block text-slate-400 mb-1">Select Campaign Slogan:</label>
            <select id="poster-slogan-sel" onchange="updateCommunityPoster()" class="w-full p-2 bg-slate-950 border border-slate-800 rounded-lg text-amber-300 font-semibold">
                <option value="s1">"Plant a Sapling Today, Gift a Green Tomorrow!"</option>
                <option value="s2">"Clean Park, Joyful Neighborhood, Healthy Life!"</option>
                <option value="s3">"Our Hands, Our Trees, Our Living Community!"</option>
            </select>
        </div>
        <div>
            <label class="block text-slate-400 mb-1">Choose Central Illustration:</label>
            <select id="poster-art-sel" onchange="updateCommunityPoster()" class="w-full p-2 bg-slate-950 border border-slate-800 rounded-lg text-emerald-300 font-semibold">
                <option value="trees">Green Sapling & Watering Can</option>
                <option value="hands">United Hands Around Earth</option>
                <option value="park">Children & Elders in Clean Park</option>
            </select>
        </div>
    </div>

    <!-- Live Poster Preview Canvas -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex justify-center">
        <div id="poster-canvas" class="w-full max-w-sm bg-gradient-to-b from-emerald-950/80 to-slate-900 border-2 border-emerald-500/50 rounded-xl p-4 text-center space-y-2.5 shadow-xl">
            <!-- Poster contents rendered by JS -->
        </div>
    </div>
</div>
''',
    6: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">06</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Shramdaan Repair Workshop</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">Voluntary Maintenance</span>
    </div>

    <!-- Volunteer Roles Interactive Grid -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2">
            <span class="text-2xl block">🪚</span>
            <span class="font-bold text-amber-400 block">Carpenter</span>
            <button onclick="triggerRepairTask('bench')" class="w-full px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-[11px] text-slate-200">Fix Bench</button>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2">
            <span class="text-2xl block">💡</span>
            <span class="font-bold text-yellow-400 block">Electrician</span>
            <button onclick="triggerRepairTask('light')" class="w-full px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-[11px] text-slate-200">Fix Lamp</button>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2">
            <span class="text-2xl block">🌱</span>
            <span class="font-bold text-emerald-400 block">Gardener</span>
            <button onclick="triggerRepairTask('nursery')" class="w-full px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-[11px] text-slate-200">Get Saplings</button>
        </div>
        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-2">
            <span class="text-2xl block">🎋</span>
            <span class="font-bold text-cyan-400 block">Youth Volunteers</span>
            <button onclick="triggerRepairTask('guard')" class="w-full px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-[11px] text-slate-200">Build Guards</button>
        </div>
    </div>

    <!-- Active Repair Status Output -->
    <div id="shramdaan-log-box" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed font-mono">
        Status: Select a tradesperson above to initiate voluntary community repairs.
    </div>
</div>
''',
    7: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">07</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Professional Tool Kit Explorer</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">Tools of the Trade</span>
    </div>

    <!-- Occupation Tabs -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button id="trade-tab-mason" onclick="selectTradeToolKit('mason')" class="px-3 py-1.5 rounded-lg border border-blue-500 bg-blue-950/40 text-blue-300 font-bold ring-2 ring-blue-500">Mason</button>
        <button id="trade-tab-carpenter" onclick="selectTradeToolKit('carpenter')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Carpenter</button>
        <button id="trade-tab-plumber" onclick="selectTradeToolKit('plumber')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Plumber</button>
        <button id="trade-tab-electrician" onclick="selectTradeToolKit('electrician')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Electrician</button>
    </div>

    <!-- Tools Visual Display -->
    <div id="toolkit-display-box" class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <!-- Rendered by JS -->
    </div>
</div>
''',
    8: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-lime-500/20 text-lime-300 font-bold flex items-center justify-center text-sm">08</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Step-by-Step Tree Planting</h3>
        </div>
        <span class="text-xs text-lime-400 font-medium">Plantation Lab</span>
    </div>

    <!-- Step Navigator Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="plant-step-1" onclick="goToPlantStep(1)" class="p-2 rounded-lg border border-lime-500 bg-lime-950/40 text-lime-300 font-bold ring-2 ring-lime-500 text-center">1. Clear Ground</button>
        <button id="plant-step-2" onclick="goToPlantStep(2)" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium text-center">2. Dig & Compost</button>
        <button id="plant-step-3" onclick="goToPlantStep(3)" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium text-center">3. Plant Sapling</button>
        <button id="plant-step-4" onclick="goToPlantStep(4)" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium text-center">4. Water & Guard</button>
    </div>

    <!-- Interactive Graphic Stage -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[140px] space-y-2">
        <svg id="plant-stage-svg" viewBox="0 0 280 100" class="w-full max-w-[260px] h-24">
            <!-- Dynamic stage drawing rendered by JS -->
        </svg>
        <p id="plant-step-desc" class="text-xs text-slate-300 text-center font-medium">
            Step 1: Volunteers rake away plastic debris, broken stones, and thorny weeds from the planting zone.
        </p>
    </div>
</div>
''',
    9: '''
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
''',
    10: '''
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
''',
    11: '''
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
''',
    12: '''
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
''',
    13: '''
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
''',
    14: '''
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
''',
    15: '''
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
''',
    16: '''
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
''',
}
