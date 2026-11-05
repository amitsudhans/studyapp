"""Simulators 9 to 16 for Chapter 6"""
import sys

SIMS = {}

# SIM 9: Seven Sisters & Sikkim Eco-Map
SIMS[9] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Northeast India: Seven Sisters & Brother Sikkim</span>
        <p class="text-[11px] text-slate-400">Click any state to explore its capital, sacred groves, and iconic ecological heritage!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-emerald-950/20 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Northeast India Regional Map Representation -->
            <!-- Sikkim (Brother State) on West -->
            <path id="stateSikkim" d="M 60,60 L 85,55 L 90,80 L 65,85 Z" fill="#047857" stroke="#10b981" stroke-width="1.5" class="cursor-pointer hover:fill-emerald-400 transition" onclick="selectNEState('sikkim')"/>
            <text x="75" y="72" text-anchor="middle" fill="#ecfdf5" font-size="7" font-weight="bold">Sikkim</text>
            <text x="75" y="100" text-anchor="middle" fill="#6ee7b7" font-size="7">Mt. Kangchenjunga</text>

            <!-- Arunachal Pradesh (Dawn-lit mountains) -->
            <path id="stateArunachal" d="M 160,25 L 300,20 L 330,55 L 280,75 L 200,60 Z" fill="#065f46" stroke="#34d399" stroke-width="1.5" class="cursor-pointer hover:fill-emerald-400 transition" onclick="selectNEState('arunachal')"/>
            <text x="240" y="42" text-anchor="middle" fill="#ecfdf5" font-size="8" font-weight="bold">Arunachal Pradesh</text>

            <!-- Assam (Brahmaputra Valley) -->
            <path id="stateAssam" d="M 140,75 L 260,70 L 270,105 L 180,115 L 140,95 Z" fill="#047857" stroke="#34d399" stroke-width="1.5" class="cursor-pointer hover:fill-emerald-400 transition" onclick="selectNEState('assam')"/>
            <text x="200" y="92" text-anchor="middle" fill="#ffffff" font-size="9" font-weight="bold">Assam</text>

            <!-- Meghalaya (Abode of Clouds & Living Root Bridges) -->
            <path id="stateMeghalaya" d="M 140,118 L 195,115 L 190,140 L 135,140 Z" fill="#0f766e" stroke="#2dd4bf" stroke-width="1.5" class="cursor-pointer hover:fill-teal-400 transition" onclick="selectNEState('meghalaya')"/>
            <text x="165" y="130" text-anchor="middle" fill="#ccfbf1" font-size="7" font-weight="bold">Meghalaya</text>

            <!-- Nagaland -->
            <path id="stateNagaland" d="M 280,85 L 320,80 L 310,120 L 280,110 Z" fill="#115e59" stroke="#2dd4bf" stroke-width="1.5" class="cursor-pointer hover:fill-teal-400 transition" onclick="selectNEState('nagaland')"/>
            <text x="298" y="102" text-anchor="middle" fill="#ccfbf1" font-size="7" font-weight="bold">Nagaland</text>

            <!-- Manipur (Loktak Lake & Phumdis) -->
            <path id="stateManipur" d="M 275,122 L 310,122 L 300,165 L 270,160 Z" fill="#065f46" stroke="#34d399" stroke-width="1.5" class="cursor-pointer hover:fill-emerald-400 transition" onclick="selectNEState('manipur')"/>
            <text x="290" y="145" text-anchor="middle" fill="#ecfdf5" font-size="7" font-weight="bold">Manipur</text>

            <!-- Mizoram -->
            <path id="stateMizoram" d="M 245,165 L 275,165 L 265,215 L 240,210 Z" fill="#047857" stroke="#34d399" stroke-width="1.5" class="cursor-pointer hover:fill-emerald-400 transition" onclick="selectNEState('mizoram')"/>
            <text x="256" y="190" text-anchor="middle" fill="#ecfdf5" font-size="7" font-weight="bold">Mizoram</text>

            <!-- Tripura -->
            <path id="stateTripura" d="M 195,160 L 225,160 L 220,195 L 190,190 Z" fill="#0f766e" stroke="#2dd4bf" stroke-width="1.5" class="cursor-pointer hover:fill-teal-400 transition" onclick="selectNEState('tripura')"/>
            <text x="208" y="180" text-anchor="middle" fill="#ccfbf1" font-size="7" font-weight="bold">Tripura</text>

            <!-- Interactive Selected Info Floating Card -->
            <g id="stateCardGroup" transform="translate(15, 155)">
                <rect x="0" y="0" width="165" height="70" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
                <text id="cardStateName" x="10" y="18" fill="#38bdf8" font-size="10" font-weight="bold">Assam (Dispur)</text>
                <text id="cardStateEco1" x="10" y="34" fill="#cbd5e1" font-size="8">Brahmaputra Valley & Kaziranga</text>
                <text id="cardStateEco2" x="10" y="48" fill="#a7f3d0" font-size="8">Hargila Stork Sanctuary</text>
                <text id="cardStateEco3" x="10" y="62" fill="#fde047" font-size="7">Lush Tea Gardens & Wetlands</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5 text-xs">
        <button onclick="selectNEState('assam')" class="py-1 px-2 rounded-lg bg-emerald-950/60 hover:bg-emerald-900 border border-emerald-500/40 text-emerald-200">Assam</button>
        <button onclick="selectNEState('meghalaya')" class="py-1 px-2 rounded-lg bg-teal-950/60 hover:bg-teal-900 border border-teal-500/40 text-teal-200">Meghalaya</button>
        <button onclick="selectNEState('sikkim')" class="py-1 px-2 rounded-lg bg-cyan-950/60 hover:bg-cyan-900 border border-cyan-500/40 text-cyan-200">Sikkim</button>
        <button onclick="selectNEState('manipur')" class="py-1 px-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300">Manipur</button>
    </div>
    <div id="sim9Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-emerald-400 font-bold">Ecological Hotspot:</span> Northeast India holds 8 states (the Seven Sisters plus brother state Sikkim, the world's 1st 100% organic state). Their community sacred groves protect pristine forests!
    </div>
</div>
"""

# SIM 10: Hargila Stork Nesting & Conservation Heroines
SIMS[10] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Hargila Stork & Women's Conservation Army</span>
        <p class="text-[11px] text-slate-400">Dr. Purnima Devi Barman and 10,000 rural women protect Greater Adjutants with woven rescue nets!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Tall Kadamba Nesting Tree -->
            <rect x="0" y="210" width="400" height="30" fill="#1e293b"/>
            <!-- Trunk -->
            <rect x="185" y="50" width="30" height="160" fill="#582f0e"/>
            <!-- Crown Foliage -->
            <circle cx="200" cy="50" r="50" fill="#15803d" opacity="0.9"/>
            <circle cx="160" cy="60" r="35" fill="#166534"/>
            <circle cx="240" cy="60" r="35" fill="#22c55e" opacity="0.8"/>

            <!-- High Twig Nest -->
            <ellipse cx="200" cy="55" rx="35" ry="10" fill="#78350f" stroke="#451a03" stroke-width="2"/>

            <!-- Mother Hargila Stork in Nest (5 feet tall bird with yellow neck pouch) -->
            <g transform="translate(200, 40)">
                <ellipse cx="0" cy="0" rx="14" ry="10" fill="#334155"/>
                <!-- Neck & Bare Head with hanging pouch -->
                <line x1="10" y1="0" x2="18" y2="-15" stroke="#fcd34d" stroke-width="4"/>
                <circle cx="20" cy="-18" r="5" fill="#f87171"/> <!-- Bare pinkish head -->
                <!-- Big Heavy Wedge Bill -->
                <polygon points="23,-20 38,-16 23,-14" fill="#ca8a04"/>
                <!-- Neck Pouch (gular pouch) -->
                <ellipse cx="14" cy="-5" rx="4" ry="7" fill="#facc15" opacity="0.9"/>
            </g>

            <!-- Stork Chick in Nest (moves down during fall simulation) -->
            <g id="storkChick" transform="translate(185, 45)" class="transition-transform duration-700">
                <circle cx="0" cy="0" r="6" fill="#e2e8f0"/>
                <polygon points="5,-2 12,0 5,2" fill="#ca8a04"/>
                <circle cx="2" cy="-2" r="1" fill="#0f172a"/>
                <text x="0" y="-8" text-anchor="middle" fill="#fde047" font-size="7">Chick</text>
            </g>

            <!-- Safety Net under Tree (Toggled by Button) -->
            <g id="safetyNet" class="opacity-0 transition-opacity duration-300">
                <path d="M 120,160 Q 200,185 280,160" fill="none" stroke="#22c55e" stroke-width="3" stroke-dasharray="4,2"/>
                <line x1="120" y1="160" x2="115" y2="210" stroke="#94a3b8" stroke-width="2"/>
                <line x1="280" y1="160" x2="285" y2="210" stroke="#94a3b8" stroke-width="2"/>
                <text x="200" y="195" text-anchor="middle" fill="#4ade80" font-size="8" font-weight="bold">Nylon Safety Catch Net (Deployed)</text>
            </g>

            <!-- Hargila Army Rescuers on Ground -->
            <g transform="translate(100, 190)">
                <circle cx="0" cy="0" r="5" fill="#fcd34d"/>
                <rect x="-4" y="5" width="8" height="15" fill="#14b8a6"/>
                <text x="0" y="-8" text-anchor="middle" fill="#5eead4" font-size="7">Hargila Army</text>
            </g>
            <g transform="translate(295, 190)">
                <circle cx="0" cy="0" r="5" fill="#fcd34d"/>
                <rect x="-4" y="5" width="8" height="15" fill="#14b8a6"/>
            </g>

            <!-- Rescue Status Indicator -->
            <g transform="translate(15, 15)">
                <rect x="0" y="0" width="135" height="40" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="67" y="14" text-anchor="middle" fill="#94a3b8" font-size="8">Nest Status</text>
                <text id="hargilaRescueText" x="67" y="30" text-anchor="middle" fill="#38bdf8" font-size="9" font-weight="bold">Chicks Safe in Nest</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="deploySafetyNet()" id="netDeployBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition">
            <span>1. Deploy Safety Catch Net</span>
        </button>
        <button onclick="simulateChickSlip()" id="chickSlipBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition">
            <span>2. Test Chick Fall & Catch</span>
        </button>
    </div>
    <div id="sim10Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-amber-400 font-bold">Community Conservation:</span> The Greater Adjutant Stork was once considered an ugly bird of bad omen. Dr. Purnima Devi Barman transformed public sentiment into pride, creating a 10,000-strong women's protective army!
    </div>
</div>
"""

# SIM 11: Living Root Bridge Bio-Architect (Ficus elastica)
SIMS[11] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Khasi Living Root Bridge (Jingkieng Jri) Bio-Lab</span>
        <p class="text-[11px] text-slate-400">Discover indigenous bio-engineering: guiding rubber tree aerial roots through betel trunks!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950 via-teal-950/30 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Roaring Monsoon River in Chasm -->
            <path d="M 0,180 Q 100,165 200,180 T 400,175 L 400,240 L 0,240 Z" fill="#0284c7" opacity="0.8"/>
            <path d="M 0,195 Q 150,180 300,195 T 400,190" stroke="#38bdf8" stroke-width="2" fill="none" stroke-dasharray="8,4"/>
            <text x="200" y="220" text-anchor="middle" fill="#7dd3fc" font-size="8">Roaring Monsoon Torrent (Rots Steel & Wood Bridges)</text>

            <!-- Left River Bank & Rubber Fig Tree (Ficus elastica) -->
            <path d="M 0,120 L 90,120 L 70,240 L 0,240 Z" fill="#3f2e1e"/>
            <!-- Left Tree Trunk -->
            <rect x="20" y="40" width="25" height="85" fill="#713f12"/>
            <circle cx="32" cy="30" r="30" fill="#15803d"/>

            <!-- Right River Bank & Anchor Tree -->
            <path d="M 310,120 L 400,120 L 400,240 L 330,240 Z" fill="#3f2e1e"/>
            <!-- Right Tree Trunk -->
            <rect x="350" y="40" width="25" height="85" fill="#713f12"/>
            <circle cx="362" cy="30" r="30" fill="#15803d"/>

            <!-- Hollow Betel Nut Palm Trunk Guide (Areca catechu) -->
            <g id="betelGuide" class="opacity-40">
                <rect x="75" y="112" width="250" height="8" rx="2" fill="#78350f" stroke="#a16207" stroke-width="1"/>
                <text x="200" y="106" text-anchor="middle" fill="#fbbf24" font-size="7">Hollow Betel Palm Trunk Guide Tube</text>
            </g>

            <!-- Living Root Cables Spanning Across (Grows thicker through time-lapse) -->
            <g id="livingRootsGroup">
                <!-- Main Footpath Cable -->
                <path id="rootSpan1" d="M 45,115 Q 200,128 355,115" stroke="#854d0e" stroke-width="3" fill="none"/>
                <!-- Upper Handrail Cable -->
                <path id="rootSpan2" d="M 45,95 Q 200,105 355,95" stroke="#854d0e" stroke-width="2.5" fill="none"/>
                <!-- Cross-knitted Vertical Root Struts -->
                <line x1="120" y1="100" x2="120" y2="122" stroke="#854d0e" stroke-width="1.5"/>
                <line x1="170" y1="102" x2="170" y2="125" stroke="#854d0e" stroke-width="1.5"/>
                <line x1="230" y1="102" x2="230" y2="125" stroke="#854d0e" stroke-width="1.5"/>
                <line x1="280" y1="100" x2="280" y2="122" stroke="#854d0e" stroke-width="1.5"/>
            </g>

            <!-- Time Age & Strength Badge -->
            <g transform="translate(15, 12)">
                <rect x="0" y="0" width="135" height="42" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="67" y="14" text-anchor="middle" fill="#94a3b8" font-size="7">Bridge Age & Integrity</text>
                <text id="rootBridgeAgeText" x="67" y="30" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Year 15: Thin Strands</text>
            </g>
        </svg>
    </div>
    <div class="space-y-2">
        <div class="flex items-center justify-between text-xs text-slate-400">
            <span>Bridge Lifespan Growth:</span>
            <span id="bridgeYearsLabel" class="font-bold text-emerald-400">15 Years (Growing)</span>
        </div>
        <input type="range" id="bridgeAgeSlider" min="1" max="100" value="15" oninput="updateRootBridgeAge(this.value)" class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-emerald-500">
    </div>
    <div id="sim11Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-emerald-400 font-bold">Living Architecture:</span> Unlike steel or concrete bridges that rust and decay with moisture, a living root bridge grows stronger every year as secondary root wood thickens and anastomoses (merges together)!
    </div>
</div>
"""

# SIM 12: Western Ghats Endemic Wildlife Tracker
SIMS[12] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Western Ghats Endemic Wildlife Tracker</span>
        <p class="text-[11px] text-slate-400">Track the Lion-Tailed Macaque and Malabar Giant Squirrel (Shekru) in the Sahyadri canopy!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-emerald-950/40 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Mountain Slope Rainforest Silhouette -->
            <path d="M 0,80 Q 120,50 220,110 T 400,70 L 400,240 L 0,240 Z" fill="#064e3b" opacity="0.6"/>

            <!-- Giant Rainforest Trees & High Canopy -->
            <rect x="80" y="60" width="22" height="180" fill="#451a03"/>
            <circle cx="90" cy="50" r="45" fill="#15803d" opacity="0.9"/>

            <rect x="290" y="80" width="22" height="160" fill="#451a03"/>
            <circle cx="300" cy="70" r="45" fill="#166534" opacity="0.9"/>

            <!-- High Canopy Connecting Vines / Lianas -->
            <path d="M 90,50 Q 200,90 300,70" fill="none" stroke="#713f12" stroke-width="4"/>

            <!-- Endemic Animal 1: Lion-Tailed Macaque (Left Canopy) -->
            <g id="macaqueAnimal" class="cursor-pointer transition-transform hover:scale-105" transform="translate(105, 55)" onclick="selectGhatsAnimal('macaque')">
                <circle id="macaqueAura" cx="0" cy="0" r="30" fill="#facc15" opacity="0.2" class="hidden"/>
                <!-- Body (Glossy black fur) -->
                <ellipse cx="0" cy="8" rx="14" ry="18" fill="#1e293b"/>
                <!-- Silver-White Mane encircling head -->
                <circle cx="0" cy="-6" r="14" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
                <!-- Black Face within white mane -->
                <circle cx="0" cy="-6" r="7" fill="#0f172a"/>
                <circle cx="-2" cy="-7" r="1" fill="#facc15"/>
                <circle cx="2" cy="-7" r="1" fill="#facc15"/>
                <!-- Tufted Lion Tail -->
                <path d="M -12,18 Q -20,28 -18,36" fill="none" stroke="#1e293b" stroke-width="2.5"/>
                <circle cx="-18" cy="36" r="3.5" fill="#1e293b"/> <!-- Tuft -->
                <text x="0" y="-22" text-anchor="middle" fill="#f1f5f9" font-size="8" font-weight="bold">Lion-Tailed Macaque</text>
            </g>

            <!-- Endemic Animal 2: Malabar Giant Squirrel - Shekru (Right Canopy / Vine) -->
            <g id="squirrelAnimal" class="cursor-pointer transition-transform hover:scale-105" transform="translate(260, 65)" onclick="selectGhatsAnimal('squirrel')">
                <circle id="squirrelAura" cx="0" cy="0" r="30" fill="#f97316" opacity="0.2" class="hidden"/>
                <!-- Two-tone Body: Deep Maroon/Purple & Cream -->
                <ellipse cx="0" cy="6" rx="16" ry="10" fill="#701a75"/>
                <!-- Cream underbelly -->
                <path d="M -10,12 Q 0,16 10,12" stroke="#fef08a" stroke-width="2"/>
                <!-- Head with tufted ears -->
                <circle cx="16" cy="2" r="7" fill="#9d174d"/>
                <circle cx="18" cy="1" r="1.5" fill="#0f172a"/>
                <circle cx="17" cy="-5" r="2" fill="#701a75"/> <!-- Ear tuft -->
                <!-- Huge Bushy Tail (longer than body: 2 feet long) -->
                <path d="M -14,6 Q -30,0 -35,-15 Q -25,-25 -10,-10" fill="#4a044e" stroke="#701a75" stroke-width="2"/>
                <text x="0" y="-18" text-anchor="middle" fill="#f472b6" font-size="8" font-weight="bold">Shekru (Giant Squirrel)</text>
            </g>

            <!-- Info Bar -->
            <g transform="translate(15, 185)">
                <rect x="0" y="0" width="165" height="42" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text id="ghatsAnimalTitle" x="82" y="15" text-anchor="middle" fill="#38bdf8" font-size="8" font-weight="bold">Active Species Info</text>
                <text id="ghatsAnimalDesc" x="82" y="30" text-anchor="middle" fill="#cbd5e1" font-size="7">Click an animal in the canopy to inspect</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="selectGhatsAnimal('macaque')" id="macaqueBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition">
            <span>Lion-Tailed Macaque</span>
        </button>
        <button onclick="selectGhatsAnimal('squirrel')" id="squirrelBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition">
            <span>Malabar Giant Squirrel</span>
        </button>
    </div>
    <div id="sim12Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-amber-400 font-bold">Arboreal Specialists:</span> Both the Lion-Tailed Macaque and Shekru spend almost their entire lives high up in the dense evergreen canopy, rarely descending to the forest floor!
    </div>
</div>
"""

# SIM 13: Mountain River Springs & Botanical Pharmacy
SIMS[13] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1">Mountain River Springs & Botanical Pharmacy</span>
        <p class="text-[11px] text-slate-400">The Western Ghats act as a giant hydrological sponge, giving birth to India's great peninsular rivers!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Mountain Ridge Elevation Profile -->
            <path d="M 0,220 L 40,160 Q 80,70 120,60 Q 160,50 200,90 Q 240,130 300,100 Q 360,70 400,120 L 400,240 L 0,240 Z" fill="#1e293b"/>
            <!-- Moss & Forest Sponge Layer -->
            <path d="M 40,160 Q 80,70 120,60 Q 160,50 200,90 Q 240,130 300,100 Q 360,70 400,120" fill="none" stroke="#15803d" stroke-width="8"/>

            <!-- Rain Cloud Overhead raining onto ridge -->
            <g transform="translate(100, 15)">
                <ellipse cx="20" cy="15" rx="25" ry="12" fill="#64748b"/>
                <ellipse cx="40" cy="12" rx="20" ry="10" fill="#94a3b8"/>
                <!-- Rain drops soaking into mountain sponge -->
                <line x1="15" y1="28" x2="12" y2="40" stroke="#38bdf8" stroke-dasharray="2,2"/>
                <line x1="28" y1="28" x2="25" y2="42" stroke="#38bdf8" stroke-dasharray="2,2"/>
                <line x1="40" y1="26" x2="38" y2="40" stroke="#38bdf8" stroke-dasharray="2,2"/>
            </g>

            <!-- Spring 1: Godavari Origin at Trimbakeshwar (Nashik) -->
            <g class="cursor-pointer" transform="translate(125, 75)" onclick="inspectSpring('godavari')">
                <circle cx="0" cy="0" r="7" fill="#0284c7"/>
                <circle cx="0" cy="0" r="3" fill="#ffffff"/>
                <path d="M 0,0 Q 40,40 60,110" stroke="#38bdf8" stroke-width="2.5" fill="none"/>
                <text x="10" y="-5" fill="#7dd3fc" font-size="8" font-weight="bold">Trimbakeshwar (Godavari)</text>
            </g>

            <!-- Spring 2: Krishna Origin at Mahabaleshwar -->
            <g class="cursor-pointer" transform="translate(205, 95)" onclick="inspectSpring('krishna')">
                <circle cx="0" cy="0" r="7" fill="#0284c7"/>
                <circle cx="0" cy="0" r="3" fill="#ffffff"/>
                <path d="M 0,0 Q 20,40 50,100" stroke="#38bdf8" stroke-width="2" fill="none"/>
                <text x="10" y="15" fill="#7dd3fc" font-size="8" font-weight="bold">Mahabaleshwar (Krishna)</text>
            </g>

            <!-- Spring 3: Cauvery Origin at Talakaveri (Kodagu) -->
            <g class="cursor-pointer" transform="translate(305, 105)" onclick="inspectSpring('cauvery')">
                <circle cx="0" cy="0" r="7" fill="#0284c7"/>
                <circle cx="0" cy="0" r="3" fill="#ffffff"/>
                <path d="M 0,0 Q 20,40 40,90" stroke="#38bdf8" stroke-width="2" fill="none"/>
                <text x="10" y="-5" fill="#7dd3fc" font-size="8" font-weight="bold">Talakaveri (Cauvery)</text>
            </g>

            <!-- Medicinal Herb Icon -->
            <g transform="translate(25, 180)">
                <circle cx="10" cy="10" r="12" fill="#065f46" stroke="#34d399" stroke-width="1"/>
                <path d="M 10,4 Q 4,10 10,16 Q 16,10 10,4 Z" fill="#34d399"/>
                <text x="28" y="14" fill="#a7f3d0" font-size="8">4,000+ Medicinal Flora</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-1.5 text-xs">
        <button onclick="inspectSpring('godavari')" id="btnGodavari" class="py-1.5 px-2 rounded-xl font-bold bg-cyan-950/60 hover:bg-cyan-900 border border-cyan-500/40 text-cyan-200">Godavari</button>
        <button onclick="inspectSpring('krishna')" id="btnKrishna" class="py-1.5 px-2 rounded-xl font-bold bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200">Krishna</button>
        <button onclick="inspectSpring('cauvery')" id="btnCauvery" class="py-1.5 px-2 rounded-xl font-bold bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200">Cauvery</button>
    </div>
    <div id="sim13Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-cyan-400 font-bold">Hydrological Sponge:</span> Thick montane mosses, humus, and leaf litter trap heavy monsoon rains and slowly release crystal-clear freshwater throughout dry summer months!
    </div>
</div>
"""

# SIM 14: Citizen Science Mango Diversity Vault
SIMS[14] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Citizen Science Mango Diversity Vault</span>
        <p class="text-[11px] text-slate-400">Join school student researchers cataloguing over 200 heirloom wild and cultivated mango varieties!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-amber-950/30 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Vault Tray Grid -->
            <rect x="20" y="20" width="360" height="150" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>

            <!-- Variety 1: Appemidi (Western Ghats Wild Pickling Mango) -->
            <g id="mangoAppemidi" class="cursor-pointer transition-transform hover:scale-105" transform="translate(65, 85)" onclick="inspectMango('appemidi')">
                <circle id="auraAppemidi" cx="0" cy="0" r="30" fill="#22c55e" opacity="0.2" class="hidden"/>
                <!-- Small green, highly pungent pickling mango -->
                <path d="M 0,-18 C 12,-18 16,-5 14,10 C 12,22 -2,24 -8,14 C -14,4 -10,-18 0,-18 Z" fill="#15803d" stroke="#22c55e" stroke-width="1.5"/>
                <path d="M 0,-18 L -3,-24" stroke="#78350f" stroke-width="2"/>
                <text x="0" y="34" text-anchor="middle" fill="#86efac" font-size="8" font-weight="bold">Appemidi</text>
                <text x="0" y="44" text-anchor="middle" fill="#64748b" font-size="7">Wild Pickling</text>
            </g>

            <!-- Variety 2: Alphonso (Hapus - Western Coast) -->
            <g id="mangoAlphonso" class="cursor-pointer transition-transform hover:scale-105" transform="translate(155, 85)" onclick="inspectMango('alphonso')">
                <circle id="auraAlphonso" cx="0" cy="0" r="30" fill="#facc15" opacity="0.2" class="hidden"/>
                <!-- Plump golden-yellow aromatic mango -->
                <path d="M 0,-20 C 18,-20 22,-2 18,14 C 14,26 -2,28 -12,18 C -20,6 -15,-20 0,-20 Z" fill="#eab308" stroke="#ca8a04" stroke-width="1.5"/>
                <path d="M 0,-20 L 2,-26" stroke="#78350f" stroke-width="2"/>
                <text x="0" y="34" text-anchor="middle" fill="#fde047" font-size="8" font-weight="bold">Alphonso</text>
                <text x="0" y="44" text-anchor="middle" fill="#64748b" font-size="7">Sweet Dessert</text>
            </g>

            <!-- Variety 3: Totapuri (Parrot Beak) -->
            <g id="mangoTotapuri" class="cursor-pointer transition-transform hover:scale-105" transform="translate(245, 85)" onclick="inspectMango('totapuri')">
                <circle id="auraTotapuri" cx="0" cy="0" r="30" fill="#84cc16" opacity="0.2" class="hidden"/>
                <!-- Curved parrot beak shape -->
                <path d="M 0,-22 C 14,-22 18,-8 15,10 C 12,24 2,28 -16,28 C -10,18 -15,4 -10,-12 C -6,-18 -4,-22 0,-22 Z" fill="#84cc16" stroke="#65a30d" stroke-width="1.5"/>
                <path d="M 0,-22 L -2,-28" stroke="#78350f" stroke-width="2"/>
                <text x="0" y="34" text-anchor="middle" fill="#bef264" font-size="8" font-weight="bold">Totapuri</text>
                <text x="0" y="44" text-anchor="middle" fill="#64748b" font-size="7">Pointed Beak</text>
            </g>

            <!-- Variety 4: Neelam (Late Season Southern Gem) -->
            <g id="mangoNeelam" class="cursor-pointer transition-transform hover:scale-105" transform="translate(335, 85)" onclick="inspectMango('neelam')">
                <circle id="auraNeelam" cx="0" cy="0" r="30" fill="#f97316" opacity="0.2" class="hidden"/>
                <!-- Smooth oval orange-yellow -->
                <path d="M 0,-18 C 14,-18 16,-2 14,12 C 12,22 0,25 -10,16 C -18,6 -12,-18 0,-18 Z" fill="#f97316" stroke="#ea580c" stroke-width="1.5"/>
                <path d="M 0,-18 L 1,-24" stroke="#78350f" stroke-width="2"/>
                <text x="0" y="34" text-anchor="middle" fill="#fdba74" font-size="8" font-weight="bold">Neelam</text>
                <text x="0" y="44" text-anchor="middle" fill="#64748b" font-size="7">Floral Fragrance</text>
            </g>

            <!-- Citizen Science Registry Bar -->
            <g transform="translate(30, 185)">
                <rect x="0" y="0" width="340" height="40" rx="6" fill="#1e293b" stroke="#475569" stroke-width="1"/>
                <text id="mangoRegistryTitle" x="15" y="16" fill="#38bdf8" font-size="8" font-weight="bold">Student Registry: 200+ Cultivars Documented</text>
                <text id="mangoRegistryDesc" x="15" y="30" fill="#cbd5e1" font-size="7">Click any mango cultivar above to analyze taste, aroma, and geographic origin!</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5 text-xs">
        <button onclick="inspectMango('appemidi')" class="py-1 px-2 rounded-lg bg-emerald-950/60 hover:bg-emerald-900 border border-emerald-500/40 text-emerald-200">Appemidi</button>
        <button onclick="inspectMango('alphonso')" class="py-1 px-2 rounded-lg bg-amber-950/60 hover:bg-amber-900 border border-amber-500/40 text-amber-200">Alphonso</button>
        <button onclick="inspectMango('totapuri')" class="py-1 px-2 rounded-lg bg-lime-950/60 hover:bg-lime-900 border border-lime-500/40 text-lime-200">Totapuri</button>
        <button onclick="inspectMango('neelam')" class="py-1 px-2 rounded-lg bg-orange-950/60 hover:bg-orange-900 border border-orange-500/40 text-orange-200">Neelam</button>
    </div>
    <div id="sim14Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-amber-400 font-bold">Citizen Science Power:</span> School students partnering with scientists mapped wild riverine Appemidi trees before they were lost to deforestation, ensuring genetic conservation!
    </div>
</div>
"""

# SIM 15: Silent Valley Rainforest Ecosystem Monitor
SIMS[15] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Silent Valley: Absence of Cicadas & Saved River</span>
        <p class="text-[11px] text-slate-400">Discover why Silent Valley is uniquely quiet and how citizen action saved the Kunthipuzha River!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-emerald-950/40 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Rainforest Canopy Valley -->
            <path d="M 0,100 Q 100,60 200,90 Q 300,60 400,100 L 400,240 L 0,240 Z" fill="#064e3b"/>

            <!-- Kunthipuzha River Flowing Through Valley -->
            <path id="valleyRiver" d="M 200,90 Q 180,140 210,180 T 190,240" fill="none" stroke="#38bdf8" stroke-width="12" stroke-linecap="round"/>

            <!-- Dense Pristine Canopy Trees -->
            <circle cx="80" cy="110" r="40" fill="#15803d" opacity="0.9"/>
            <circle cx="140" cy="120" r="35" fill="#166534" opacity="0.9"/>
            <circle cx="270" cy="120" r="35" fill="#166534" opacity="0.9"/>
            <circle cx="330" cy="110" r="40" fill="#15803d" opacity="0.9"/>

            <!-- Threatened Dam Wall (Toggled on button click) -->
            <g id="proposedDamGroup" class="opacity-0 transition-opacity duration-300">
                <rect x="160" y="140" width="80" height="25" rx="3" fill="#64748b" stroke="#94a3b8" stroke-width="2"/>
                <text x="200" y="156" text-anchor="middle" fill="#f87171" font-size="8" font-weight="bold">Proposed Hydroelectric Dam</text>
                <!-- Flood Water Area drowning forest -->
                <rect x="50" y="90" width="300" height="50" fill="#0284c7" opacity="0.5"/>
                <text x="200" y="115" text-anchor="middle" fill="#ffffff" font-size="8" font-weight="bold">8.3 sq km Virgin Forest Submerged!</text>
            </g>

            <!-- Decibel Acoustic Sound Wave Monitor -->
            <g transform="translate(15, 15)">
                <rect x="0" y="0" width="145" height="45" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1"/>
                <text x="72" y="14" text-anchor="middle" fill="#94a3b8" font-size="7">Forest Canopy Soundscape</text>
                <text id="soundscapeLevelText" x="72" y="28" text-anchor="middle" fill="#34d399" font-size="9" font-weight="bold">Tranquil (No Cicada Screech)</text>
                <text id="soundscapeDbText" x="72" y="40" text-anchor="middle" fill="#7dd3fc" font-size="8">~ 25 dB (Gentle Breeze & Brook)</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="setValleyState('sanctuary')" id="btnValleySanctuary" class="py-2 px-3 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition">
            <span>Protected National Park (River Flows)</span>
        </button>
        <button onclick="setValleyState('dam')" id="btnValleyDam" class="py-2 px-3 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition">
            <span>Simulate Proposed Dam Impact</span>
        </button>
    </div>
    <div id="sim15Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-emerald-400 font-bold">Historical Victory:</span> The Save Silent Valley movement was India's first major environmental movement where people chose ecological preservation of biodiversity over an industrial dam!
    </div>
</div>
"""

# SIM 16: India's Unique Places Grand Expedition (Passport Journal)
SIMS[16] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1">India's Unique Places Expedition Passport</span>
        <p class="text-[11px] text-slate-400">Collect biome visa stamps from all 4 extraordinary ecological zones across India!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Open Passport Double Page -->
            <rect x="20" y="15" width="360" height="210" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2"/>
            <line x1="200" y1="15" x2="200" y2="225" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>

            <!-- Left Page: Stamp 1 (Andamans) & Stamp 2 (Sundarbans) -->
            <!-- Stamp 1: Islands -->
            <g id="stampAndaman" class="cursor-pointer" transform="translate(40, 35)" onclick="stampPassport('andaman')">
                <rect x="0" y="0" width="135" height="75" rx="6" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" stroke-dasharray="3,2"/>
                <text x="67" y="18" text-anchor="middle" fill="#38bdf8" font-size="8" font-weight="bold">ANDAMAN & NICOBAR</text>
                <text x="67" y="32" text-anchor="middle" fill="#cbd5e1" font-size="7">Indira Point & Coral Reefs</text>
                <circle id="sealAndaman" cx="67" cy="52" r="14" fill="#0284c7" opacity="0.3"/>
                <text id="sealTextAndaman" x="67" y="55" text-anchor="middle" fill="#38bdf8" font-size="7" font-weight="bold">CLICK TO STAMP</text>
            </g>

            <!-- Stamp 2: Sundarbans -->
            <g id="stampSundarbans" class="cursor-pointer" transform="translate(40, 125)" onclick="stampPassport('sundarbans')">
                <rect x="0" y="0" width="135" height="75" rx="6" fill="#0f172a" stroke="#059669" stroke-width="1.5" stroke-dasharray="3,2"/>
                <text x="67" y="18" text-anchor="middle" fill="#34d399" font-size="8" font-weight="bold">SUNDARBANS DELTA</text>
                <text x="67" y="32" text-anchor="middle" fill="#cbd5e1" font-size="7">Pneumatophores & Tigers</text>
                <circle id="sealSundarbans" cx="67" cy="52" r="14" fill="#059669" opacity="0.3"/>
                <text id="sealTextSundarbans" x="67" y="55" text-anchor="middle" fill="#34d399" font-size="7" font-weight="bold">CLICK TO STAMP</text>
            </g>

            <!-- Right Page: Stamp 3 (Northeast) & Stamp 4 (Western Ghats) -->
            <!-- Stamp 3: Northeast -->
            <g id="stampNortheast" class="cursor-pointer" transform="translate(225, 35)" onclick="stampPassport('northeast')">
                <rect x="0" y="0" width="135" height="75" rx="6" fill="#0f172a" stroke="#d97706" stroke-width="1.5" stroke-dasharray="3,2"/>
                <text x="67" y="18" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="bold">NORTHEAST INDIA</text>
                <text x="67" y="32" text-anchor="middle" fill="#cbd5e1" font-size="7">Hargila & Root Bridges</text>
                <circle id="sealNortheast" cx="67" cy="52" r="14" fill="#d97706" opacity="0.3"/>
                <text id="sealTextNortheast" x="67" y="55" text-anchor="middle" fill="#fbbf24" font-size="7" font-weight="bold">CLICK TO STAMP</text>
            </g>

            <!-- Stamp 4: Western Ghats -->
            <g id="stampGhats" class="cursor-pointer" transform="translate(225, 125)" onclick="stampPassport('ghats')">
                <rect x="0" y="0" width="135" height="75" rx="6" fill="#0f172a" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="3,2"/>
                <text x="67" y="18" text-anchor="middle" fill="#a78bfa" font-size="8" font-weight="bold">WESTERN GHATS</text>
                <text x="67" y="32" text-anchor="middle" fill="#cbd5e1" font-size="7">Silent Valley & River Sources</text>
                <circle id="sealGhats" cx="67" cy="52" r="14" fill="#7c3aed" opacity="0.3"/>
                <text id="sealTextGhats" x="67" y="55" text-anchor="middle" fill="#a78bfa" font-size="7" font-weight="bold">CLICK TO STAMP</text>
            </g>
        </svg>
    </div>
    <div class="flex items-center space-x-2">
        <button onclick="stampAllPassport()" id="btnStampAll" class="w-full py-2 rounded-xl text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white transition flex items-center justify-center space-x-1.5">
            <span>Stamp All 4 Ecoregions</span>
        </button>
    </div>
    <div id="sim16Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-cyan-400 font-bold">Expedition Badge:</span> Stamp all 4 unique ecoregions to become a certified NCERT Junior Ecological Guardian!
    </div>
</div>
"""

print("Sims 9-16 defined successfully")
