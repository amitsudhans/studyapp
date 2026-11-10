# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 2: Exploring Our Neighbourhood
Part 2 Simulators: Slides 9 to 16
Bespoke SVG/HTML interactive simulators.
Zero human names (replaced with generic roles).
Clean Unicode throughout.
"""

sim9 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-yellow-500/20 text-yellow-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Evolution Of Money Exhibit</h3>
        </div>
        <span class="text-xs text-yellow-400 font-medium">Historical Currency</span>
    </div>

    <!-- Stage Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-5 gap-1.5 text-xs">
        <button id="eom-btn-commodity" onclick="selectMoneyStage('commodity')" class="p-2 rounded-lg border border-yellow-500 bg-yellow-950/40 text-yellow-300 font-bold ring-2 ring-yellow-500 transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🌾</span>
            <span>Commodities</span>
        </button>
        <button id="eom-btn-shell" onclick="selectMoneyStage('shell')" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🐚</span>
            <span>Cowrie Shells</span>
        </button>
        <button id="eom-btn-coin" onclick="selectMoneyStage('coin')" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🪙</span>
            <span>Metal Coins</span>
        </button>
        <button id="eom-btn-paper" onclick="selectMoneyStage('paper')" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">💵</span>
            <span>Paper Notes</span>
        </button>
        <button id="eom-btn-digital" onclick="selectMoneyStage('digital')" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">📱</span>
            <span>Digital UPI</span>
        </button>
    </div>

    <!-- Interactive Visual Exhibit -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="eom-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic SVG illustration rendered by JS -->
        </div>
        <div id="eom-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-yellow-950/20 border border-yellow-800/40 leading-relaxed">
            <strong class="text-yellow-400">Commodity Trade:</strong> Early farming communities exchanged cattle, sheep, wheat grains, and salt blocks directly before coins existed.
        </div>
    </div>
</div>
"""

sim10 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Barter vs Money Simulator</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">Trade Efficiency</span>
    </div>

    <!-- Mode Selector -->
    <div class="grid grid-cols-2 gap-2 text-xs">
        <button id="bvm-btn-barter" onclick="selectTradeMode('barter')" class="p-2.5 rounded-xl border border-orange-500 bg-orange-950/40 text-orange-300 font-bold ring-2 ring-orange-500 transition-all flex items-center justify-center gap-2">
            <span class="text-lg">🔄</span>
            <span>Direct Barter System</span>
        </button>
        <button id="bvm-btn-money" onclick="selectTradeMode('money')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex items-center justify-center gap-2">
            <span class="text-lg">💰</span>
            <span>Standard Money System</span>
        </button>
    </div>

    <!-- Trade Interaction Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="bvm-visual-box" class="min-h-[130px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Trade SVG -->
        </div>
        <div id="bvm-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-orange-950/20 border border-orange-800/40 leading-relaxed">
            <strong class="text-orange-400">Barter Bottleneck:</strong> The potter has pots and desires mangoes, but the fruit seller needs cloth! Trade fails without a double coincidence of wants.
        </div>
    </div>
</div>
"""

sim11 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Passbook & Budget Planner</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Financial Literacy</span>
    </div>

    <!-- Interactive Budget View Toggle -->
    <div class="grid grid-cols-2 gap-2 text-xs">
        <button id="pab-btn-passbook" onclick="selectBudgetTab('passbook')" class="p-2 rounded-lg border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold ring-2 ring-emerald-500 transition-all">
            📖 Bank Passbook Table
        </button>
        <button id="pab-btn-budget" onclick="selectBudgetTab('budget')" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all">
            📊 Monthly Family Budget
        </button>
    </div>

    <!-- Display Area -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="pab-visual-box" class="min-h-[140px] flex items-center justify-center p-2 bg-slate-900 rounded-lg overflow-x-auto">
            <!-- Dynamic passbook or budget pie chart -->
        </div>
        <div id="pab-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-emerald-950/20 border border-emerald-800/40 leading-relaxed">
            <strong class="text-emerald-400">Passbook Ledger:</strong> Shows transaction dates, withdrawal (debit), deposit (credit), and running balance. Prudent budgeters prioritize essentials over luxuries.
        </div>
    </div>
</div>
"""

sim12 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-sky-500/20 text-sky-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Essential Public Services Hub</h3>
        </div>
        <span class="text-xs text-sky-400 font-medium">Community Utilities</span>
    </div>

    <!-- Service Icons Grid -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="eps-btn-police" onclick="selectPublicService('police')" class="p-2 rounded-xl border border-sky-500 bg-sky-950/40 text-sky-300 font-bold ring-2 ring-sky-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">👮</span>
            <span>Police (112)</span>
        </button>
        <button id="eps-btn-fire" onclick="selectPublicService('fire')" class="p-2 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🚒</span>
            <span>Fire Brigade (101)</span>
        </button>
        <button id="eps-btn-hospital" onclick="selectPublicService('hospital')" class="p-2 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🏥</span>
            <span>Hospital (102)</span>
        </button>
        <button id="eps-btn-library" onclick="selectPublicService('library')" class="p-2 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">📚</span>
            <span>Public Library</span>
        </button>
    </div>

    <!-- Interactive Service Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="eps-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Service SVG -->
        </div>
        <div id="eps-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-sky-950/20 border border-sky-800/40 leading-relaxed">
            <strong class="text-sky-400">Police Station (Dial 112):</strong> Protects citizens, investigates crimes, maintains neighbourhood order, and assists vulnerable residents during emergencies.
        </div>
    </div>
</div>
"""

sim13 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-fuchsia-500/20 text-fuchsia-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Sun & Cardinal Directions</h3>
        </div>
        <span class="text-xs text-fuchsia-400 font-medium">Compass Orientation</span>
    </div>

    <!-- Facing Direction Selector -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="scd-btn-east" onclick="orientCompass('east')" class="p-2 rounded-xl border border-fuchsia-500 bg-fuchsia-950/40 text-fuchsia-300 font-bold ring-2 ring-fuchsia-500 transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🌅</span>
            <span>Facing East (Sunrise)</span>
        </button>
        <button id="scd-btn-west" onclick="orientCompass('west')" class="p-2 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🌇</span>
            <span>Facing West (Sunset)</span>
        </button>
        <button id="scd-btn-north" onclick="orientCompass('north')" class="p-2 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🧭</span>
            <span>Facing North (Top)</span>
        </button>
        <button id="scd-btn-south" onclick="orientCompass('south')" class="p-2 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🧭</span>
            <span>Facing South (Bottom)</span>
        </button>
    </div>

    <!-- Visual Compass Orientation -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="scd-visual-box" class="min-h-[130px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Compass SVG -->
        </div>
        <div id="scd-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-fuchsia-950/20 border border-fuchsia-800/40 leading-relaxed">
            <strong class="text-fuchsia-400">Facing East:</strong> Early morning rising sun is ahead. Your back points West, your left hand points North, and your right hand points South!
        </div>
    </div>
</div>
"""

sim14 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-violet-500/20 text-violet-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Neighbourhood Map Navigator</h3>
        </div>
        <span class="text-xs text-violet-400 font-medium">Spatial Grid</span>
    </div>

    <!-- Destination Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="nmn-btn-hospital" onclick="navigateToBuilding('hospital')" class="p-2 rounded-xl border border-violet-500 bg-violet-950/40 text-violet-300 font-bold ring-2 ring-violet-500 transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🏥</span>
            <span>To Hospital (North)</span>
        </button>
        <button id="nmn-btn-library" onclick="navigateToBuilding('library')" class="p-2 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">📚</span>
            <span>To Library (East)</span>
        </button>
        <button id="nmn-btn-park" onclick="navigateToBuilding('park')" class="p-2 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🌳</span>
            <span>To Park (South)</span>
        </button>
        <button id="nmn-btn-postoffice" onclick="navigateToBuilding('postoffice')" class="p-2 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">📮</span>
            <span>To Post Office (West)</span>
        </button>
    </div>

    <!-- Interactive Grid Map Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="nmn-visual-box" class="min-h-[140px] flex items-center justify-center p-2 bg-slate-900 rounded-lg">
            <!-- Dynamic Grid Map SVG -->
        </div>
        <div id="nmn-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-violet-950/20 border border-violet-800/40 leading-relaxed">
            <strong class="text-violet-400">Route to Hospital:</strong> From central School, proceed North (upward on map) along Main Road, then turn left into Clinic Lane.
        </div>
    </div>
</div>
"""

sim15 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Frontline Heroes Tribute</h3>
        </div>
        <span class="text-xs text-pink-400 font-medium">Community Champions</span>
    </div>

    <!-- Hero Selection Grid -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="fht-btn-sanitation" onclick="selectFrontlineHero('sanitation')" class="p-2.5 rounded-xl border border-pink-500 bg-pink-950/40 text-pink-300 font-bold ring-2 ring-pink-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🧹</span>
            <span>Sanitation Worker</span>
        </button>
        <button id="fht-btn-medical" onclick="selectFrontlineHero('medical')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">👩‍⚕️</span>
            <span>Nurse & Doctor</span>
        </button>
        <button id="fht-btn-grocery" onclick="selectFrontlineHero('grocery')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🥦</span>
            <span>Grocery Provider</span>
        </button>
        <button id="fht-btn-utility" onclick="selectFrontlineHero('utility')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">⚡</span>
            <span>Utility Worker</span>
        </button>
    </div>

    <!-- Tribute Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="fht-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Hero Illustration SVG -->
        </div>
        <div id="fht-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-pink-950/20 border border-pink-800/40 leading-relaxed">
            <strong class="text-pink-400">Sanitation Worker:</strong> Arrives at dawn to sweep streets, clear refuse bins, and sanitize lanes, preventing dangerous disease vectors and keeping our neighbourhood clean.
        </div>
    </div>
</div>
"""

sim16 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-red-500/20 text-red-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Emergency Vehicle Dispatcher</h3>
        </div>
        <span class="text-xs text-red-400 font-medium">Service Network</span>
    </div>

    <!-- Incident Dispatch Scenarios -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="evd-btn-fire" onclick="dispatchEmergencyVehicle('fire')" class="p-2.5 rounded-xl border border-red-500 bg-red-950/40 text-red-300 font-bold ring-2 ring-red-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🔥</span>
            <span>Fire Emergency</span>
        </button>
        <button id="evd-btn-ambulance" onclick="dispatchEmergencyVehicle('ambulance')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🚑</span>
            <span>Medical Crisis</span>
        </button>
        <button id="evd-btn-police" onclick="dispatchEmergencyVehicle('police')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🚓</span>
            <span>Police Assistance</span>
        </button>
        <button id="evd-btn-bookmobile" onclick="dispatchEmergencyVehicle('bookmobile')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🚐</span>
            <span>Mobile Library</span>
        </button>
    </div>

    <!-- Dynamic Dispatch Visual -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="evd-visual-box" class="min-h-[130px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Dispatch Vehicle SVG -->
        </div>
        <div id="evd-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-red-950/20 border border-red-800/40 leading-relaxed">
            <strong class="text-red-400">Fire Engine Dispatched (Dial 101):</strong> Red truck equipped with water hoses, foam extinguishers, and hydraulic ladders races to the scene to protect lives and property.
        </div>
    </div>
</div>
"""

sims_part2 = {
    9: sim9,
    10: sim10,
    11: sim11,
    12: sim12,
    13: sim13,
    14: sim14,
    15: sim15,
    16: sim16,
}

