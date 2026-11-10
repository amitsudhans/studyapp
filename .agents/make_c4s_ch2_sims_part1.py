# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 2: Exploring Our Neighbourhood
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
            <h3 class="font-bold text-white text-sm sm:text-base">Neighbourhood Route Explorer</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Safe Journey</span>
    </div>

    <!-- Landmark Waypoint Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="nre-btn-school" onclick="selectRouteWaypoint('school')" class="p-2.5 rounded-xl border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold ring-2 ring-emerald-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🏫</span>
            <span>School Gate</span>
        </button>
        <button id="nre-btn-market" onclick="selectRouteWaypoint('market')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🍎</span>
            <span>Produce Market</span>
        </button>
        <button id="nre-btn-crossing" onclick="selectRouteWaypoint('crossing')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🦓</span>
            <span>Zebra Crossing</span>
        </button>
        <button id="nre-btn-busstop" onclick="selectRouteWaypoint('busstop')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🚏</span>
            <span>Bus Stop</span>
        </button>
    </div>

    <!-- Interactive Visual Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="nre-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic SVG illustration rendered by JS -->
        </div>
        <div id="nre-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-emerald-950/20 border border-emerald-800/40 leading-relaxed">
            <strong class="text-emerald-400">School Gate:</strong> Students begin their homeward walk safely on marked pedestrian footpaths, staying attentive to surrounding road traffic and bicycle bells.
        </div>
    </div>
</div>
"""

sim2 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">02</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Communication Timeline</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Historical Evolution</span>
    </div>

    <!-- Era Selector -->
    <div class="grid grid-cols-2 sm:grid-cols-5 gap-1.5 text-xs">
        <button id="ctl-btn-ancient" onclick="selectCommEra('ancient')" class="p-2 rounded-lg border border-cyan-500 bg-cyan-950/40 text-cyan-300 font-bold ring-2 ring-cyan-500 transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🥁</span>
            <span>Drums & Smoke</span>
        </button>
        <button id="ctl-btn-pigeon" onclick="selectCommEra('pigeon')" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">🕊️</span>
            <span>Homing Pigeon</span>
        </button>
        <button id="ctl-btn-postal" onclick="selectCommEra('postal')" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">📮</span>
            <span>Postal Mail</span>
        </button>
        <button id="ctl-btn-telecom" onclick="selectCommEra('telecom')" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">☎️</span>
            <span>Landline Phone</span>
        </button>
        <button id="ctl-btn-digital" onclick="selectCommEra('digital')" class="p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-lg">📱</span>
            <span>Digital Internet</span>
        </button>
    </div>

    <!-- Visual Exhibit -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="ctl-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic SVG rendered by JS -->
        </div>
        <div id="ctl-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-cyan-950/20 border border-cyan-800/40 leading-relaxed">
            <strong class="text-cyan-400">Ancient Acoustic & Visual Signals:</strong> Deep rhythmic drumbeats and towering smoke plumes transmitted alerts across hills and valleys before electrical wires were invented.
        </div>
    </div>
</div>
"""

sim3 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-rose-500/20 text-rose-300 font-bold flex items-center justify-center text-sm">03</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Postal Mail Journey</h3>
        </div>
        <span class="text-xs text-rose-400 font-medium">5-Stage Tracker</span>
    </div>

    <!-- Stepper Controls -->
    <div class="flex items-center justify-between bg-slate-950 p-2.5 rounded-xl border border-slate-800 text-xs">
        <span id="pmj-step-label" class="text-rose-400 font-bold">Stage 1: Posting in Letterbox</span>
        <div class="flex gap-2">
            <button onclick="prevPostalStep()" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-white rounded font-medium transition">← Prev</button>
            <button onclick="nextPostalStep()" class="px-2.5 py-1 bg-rose-600 hover:bg-rose-500 text-white rounded font-bold transition">Next →</button>
        </div>
    </div>

    <!-- Postal Process Illustration -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="pmj-visual-box" class="min-h-[130px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic postal step SVG -->
        </div>
        <div id="pmj-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-rose-950/20 border border-rose-800/40 leading-relaxed">
            <strong class="text-rose-400">Step 1 - Letterbox Deposit:</strong> The sender addresses an envelope with a six-digit PIN code, affixes a postage stamp, and drops it into the neighborhood red letterbox.
        </div>
    </div>
</div>
"""

sim4 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">04</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Modern Urban Transit</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">Infrastructure Comparison</span>
    </div>

    <!-- Transit Mode Buttons -->
    <div class="grid grid-cols-3 gap-2 text-xs">
        <button id="mut-btn-ground" onclick="selectTransitMode('ground')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🚗</span>
            <span>Surface Traffic</span>
        </button>
        <button id="mut-btn-flyover" onclick="selectTransitMode('flyover')" class="p-2.5 rounded-xl border border-blue-500 bg-blue-950/40 text-blue-300 font-bold ring-2 ring-blue-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🌉</span>
            <span>Elevated Flyover</span>
        </button>
        <button id="mut-btn-metro" onclick="selectTransitMode('metro')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🚇</span>
            <span>Electric Metro</span>
        </button>
    </div>

    <!-- Comparative Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="mut-visual-box" class="min-h-[130px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic transit SVG -->
        </div>
        <div id="mut-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-blue-950/20 border border-blue-800/40 leading-relaxed">
            <strong class="text-blue-400">Elevated Flyover:</strong> Bypasses busy ground-level crossroads, eliminating signal waiting times and preventing vehicle exhaust buildup at intersections.
        </div>
    </div>
</div>
"""

sim5 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-lime-500/20 text-lime-300 font-bold flex items-center justify-center text-sm">05</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Green Infrastructure Balancer</h3>
        </div>
        <span class="text-xs text-lime-400 font-medium">Eco Balance</span>
    </div>

    <!-- Action Controls -->
    <div class="flex flex-wrap items-center justify-between gap-2 bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs">
        <div class="flex items-center gap-3">
            <span class="text-slate-400">Saplings Planted: <strong id="gib-tree-count" class="text-lime-400 font-bold text-sm">4</strong></span>
            <span class="text-slate-400">Eco Score: <strong id="gib-eco-score" class="text-emerald-400 font-bold text-sm">80%</strong></span>
        </div>
        <div class="flex gap-2">
            <button onclick="addSapling()" class="px-3 py-1.5 bg-lime-700 hover:bg-lime-600 text-white rounded-lg font-bold transition flex items-center gap-1">
                <span>🌱</span> Plant Tree
            </button>
            <button onclick="resetEcoBalance()" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg font-medium transition">Reset</button>
        </div>
    </div>

    <!-- Visual Interactive Area -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="gib-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Eco-Avenue SVG -->
        </div>
        <div id="gib-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-lime-950/20 border border-lime-800/40 leading-relaxed">
            <strong class="text-lime-400">Compensatory Planting:</strong> When road widening trims mature trees, planting multiple native avenue trees (Neem, Peepal, Banyan) restores wildlife habitat and purifies air.
        </div>
    </div>
</div>
"""

sim6 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">06</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Community Health Clinic</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Healthcare Services</span>
    </div>

    <!-- Clinic Section Tabs -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="chc-btn-eye" onclick="selectClinicSection('eye')" class="p-2.5 rounded-xl border border-teal-500 bg-teal-950/40 text-teal-300 font-bold ring-2 ring-teal-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">👁️</span>
            <span>Eye Camp</span>
        </button>
        <button id="chc-btn-vaccine" onclick="selectClinicSection('vaccine')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">💉</span>
            <span>Vaccination</span>
        </button>
        <button id="chc-btn-opd" onclick="selectClinicSection('opd')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🩺</span>
            <span>Doctor OPD</span>
        </button>
        <button id="chc-btn-pharma" onclick="selectClinicSection('pharma')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">💊</span>
            <span>Pharmacy</span>
        </button>
    </div>

    <!-- Interactive Clinical Station -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="chc-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Clinic SVG -->
        </div>
        <div id="chc-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-teal-950/20 border border-teal-800/40 leading-relaxed">
            <strong class="text-teal-400">Community Eye Check-up Camp:</strong> Specialists test visual acuity with Snellen charts, check intraocular pressure, and provide free corrective spectacles for schoolchildren and elders.
        </div>
    </div>
</div>
"""

sim7 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">07</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Medical Roles Explorer</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Healthcare Team</span>
    </div>

    <!-- Medical Specialist Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <button id="mre-btn-doc" onclick="selectMedicalRole('doc')" class="p-2.5 rounded-xl border border-indigo-500 bg-indigo-950/40 text-indigo-300 font-bold ring-2 ring-indigo-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">👨‍⚕️</span>
            <span>Physician</span>
        </button>
        <button id="mre-btn-nurse" onclick="selectMedicalRole('nurse')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">👩‍⚕️</span>
            <span>Staff Nurse</span>
        </button>
        <button id="mre-btn-lab" onclick="selectMedicalRole('lab')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">🔬</span>
            <span>Lab Technician</span>
        </button>
        <button id="mre-btn-pharm" onclick="selectMedicalRole('pharm')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">💊</span>
            <span>Pharmacist</span>
        </button>
    </div>

    <!-- Role Explanation Exhibit -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="mre-visual-box" class="min-h-[120px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic Specialist SVG -->
        </div>
        <div id="mre-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-indigo-950/20 border border-indigo-800/40 leading-relaxed">
            <strong class="text-indigo-400">Physician / Doctor:</strong> Listens to chest and heart sounds using a stethoscope, identifies the illness through careful clinical diagnosis, and prescribes treatment.
        </div>
    </div>
</div>
"""

sim8 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">08</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Virtual ATM & Bank Vault</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Safe Banking</span>
    </div>

    <!-- Virtual ATM Actions -->
    <div class="grid grid-cols-3 gap-2 text-xs">
        <button id="atm-btn-balance" onclick="doAtmAction('balance')" class="p-2.5 rounded-xl border border-amber-500 bg-amber-950/40 text-amber-300 font-bold ring-2 ring-amber-500 transition-all flex flex-col items-center gap-1">
            <span class="text-xl">📜</span>
            <span>Check Balance</span>
        </button>
        <button id="atm-btn-withdraw" onclick="doAtmAction('withdraw')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">💵</span>
            <span>Withdraw ₹500</span>
        </button>
        <button id="atm-btn-deposit" onclick="doAtmAction('deposit')" class="p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1">
            <span class="text-xl">📥</span>
            <span>Deposit ₹1,000</span>
        </button>
    </div>

    <!-- ATM Screen & Vault Simulation -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="atm-visual-box" class="min-h-[130px] flex items-center justify-center p-3 bg-slate-900 rounded-lg">
            <!-- Dynamic ATM SVG -->
        </div>
        <div id="atm-info-box" class="text-xs text-slate-300 p-3 rounded-lg bg-amber-950/20 border border-amber-800/40 leading-relaxed">
            <strong class="text-amber-400">Account Inquiry:</strong> Verified with secret 4-digit PIN. Current Savings Balance: ₹12,500. Banks safeguard funds and pay interest on deposits.
        </div>
    </div>
</div>
"""

sims_part1 = {
    1: sim1,
    2: sim2,
    3: sim3,
    4: sim4,
    5: sim5,
    6: sim6,
    7: sim7,
    8: sim8,
}

