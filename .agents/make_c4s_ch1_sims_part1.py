# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 1: Living Together
Part 1 Simulators: Slides 1 to 8
Bespoke SVG/HTML interactive simulators.
Zero human names (replaced with generic roles).
Clean Unicode throughout.
"""

sim1 = """
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
"""

sim2 = """
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
"""

sim3 = """
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
"""

sim4 = """
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
"""

sim5 = """
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
"""

sim6 = """
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
"""

sim7 = """
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
"""

sim8 = """
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
"""

simulators_part1 = {
    1: sim1,
    2: sim2,
    3: sim3,
    4: sim4,
    5: sim5,
    6: sim6,
    7: sim7,
    8: sim8,
}

