"""
Simulators 9 to 16 for NCERT Class 5 Science Chapter 10: Earth - Our Shared Home
Zero raw LaTeX! Clean Unicode symbols.
"""

SIMS = {}

# SIM 9: Cows in Brazil (Zebu Adaptation Lab)
SIMS[9] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Indian Cattle in Brazil (Zebu Adaptation Lab)</span>
        <p class="text-[11px] text-slate-400">Discover why Gir, Kankrej, and Ongole cattle from India thrive under Brazil's tropical sun!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Tropical Blistering Sun Overhead -->
            <circle cx="200" cy="40" r="24" fill="#f59e0b" opacity="0.9"/>
            <circle cx="200" cy="40" r="32" fill="none" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.5"/>

            <!-- Center Stage: Indian Zebu Cow Model (Gir / Ongole) -->
            <g id="zebuCattleGraphic" transform="translate(130, 80)">
                <!-- Body with Prominent Hump -->
                <path d="M40,65 Q35,30 55,25 Q70,40 100,45 Q120,45 125,75 Q125,95 110,95 L40,95 Z" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5"/>
                <!-- Prominent Hump -->
                <ellipse cx="60" cy="28" rx="14" ry="10" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
                <!-- Neck & Dewlap (Loose Skin for Heat Dissipation) -->
                <path d="M40,65 Q30,85 45,95" stroke="#94a3b8" stroke-width="4" fill="none"/>
                <!-- Head & Sweeping Horns -->
                <circle cx="30" cy="50" r="12" fill="#e2e8f0"/>
                <path d="M28,40 Q25,25 35,20" stroke="#475569" stroke-width="2.5" fill="none"/>
                <!-- Legs -->
                <line x1="48" y1="95" x2="48" y2="135" stroke="#94a3b8" stroke-width="4"/>
                <line x1="65" y1="95" x2="65" y2="135" stroke="#94a3b8" stroke-width="4"/>
                <line x1="95" y1="95" x2="95" y2="135" stroke="#94a3b8" stroke-width="4"/>
                <line x1="112" y1="95" x2="112" y2="135" stroke="#94a3b8" stroke-width="4"/>
            </g>

            <!-- Adaptation Advantage Card (Left) -->
            <g transform="translate(20, 45)">
                <rect x="0" y="0" width="105" height="135" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5" opacity="0.95"/>
                <text x="52" y="18" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">SUPER ADAPTATIONS</text>
                <text x="10" y="38" fill="#e2e8f0" font-size="7.5">• Prominent Hump</text>
                <text x="10" y="58" fill="#e2e8f0" font-size="7.5">• Large Cool Dewlap</text>
                <text x="10" y="78" fill="#e2e8f0" font-size="7.5">• Abundant Sweat Glands</text>
                <text x="10" y="98" fill="#e2e8f0" font-size="7.5">• Tick & Heat Immunity</text>
                <text x="52" y="122" fill="#4ade80" font-size="7" font-weight="bold" text-anchor="middle">Thrives at 42°C</text>
            </g>

            <!-- Brazilian Dairy Share Badge (Right) -->
            <g transform="translate(275, 45)">
                <rect x="0" y="0" width="105" height="135" rx="8" fill="#020617" stroke="#22c55e" stroke-width="1.5" opacity="0.95"/>
                <text x="52" y="18" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">BRAZIL LIVESTOCK</text>
                <circle cx="52" cy="60" r="30" fill="#14532d"/>
                <text x="52" y="58" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">>75%</text>
                <text x="52" y="72" fill="#86efac" font-size="7" text-anchor="middle">Indian Lineage</text>
                <text x="52" y="105" fill="#e2e8f0" font-size="7" text-anchor="middle">Nelore (Ongole)</text>
                <text x="52" y="120" fill="#e2e8f0" font-size="7" text-anchor="middle">Gir Leiteiro</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="testHeatTolerance()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Test Tropical Heat Resistance
        </button>
        <button onclick="inspectBrazilianStamp()" class="p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            View Brazil Postage Stamp
        </button>
    </div>
    <div id="sim9Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Indian Lineage in Brazil:</strong> Over three-quarters of Brazil's cattle carry Indian Zebu genetics. Their sweat glands, loose dewlap, and natural tick resistance made them the kings of South American pasturelands!
    </div>
</div>
"""

# SIM 10: Web of Life (Interconnected Planetary Food & Energy Web)
SIMS[10] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Web of Life: The Planetary Interconnectedness Network</span>
        <p class="text-[11px] text-slate-400">Trace how solar energy, green plants, pollinators, birds, animals, and humans are bound in one web!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Interconnecting Radiant Web Strands -->
            <line x1="200" y1="40" x2="100" y2="100" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>
            <line x1="200" y1="40" x2="300" y2="100" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>
            <line x1="100" y1="100" x2="140" y2="180" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>
            <line x1="300" y1="100" x2="260" y2="180" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>
            <line x1="140" y1="180" x2="260" y2="180" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>
            <line x1="200" y1="40" x2="200" y2="120" stroke="#fde047" stroke-width="2" opacity="0.7"/>

            <!-- Node 1: Sun Energy (Top) -->
            <g class="cursor-pointer" onclick="selectWebNode('sun')">
                <circle cx="200" cy="40" r="22" fill="#f59e0b" stroke="#fef08a" stroke-width="2"/>
                <text x="200" y="44" fill="#020617" font-size="7.5" font-weight="bold" text-anchor="middle">Sun Energy</text>
            </g>

            <!-- Node 2: Producers (Green Plants & Trees) -->
            <g class="cursor-pointer" onclick="selectWebNode('plants')">
                <circle cx="100" cy="100" r="22" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
                <text x="100" y="104" fill="#ffffff" font-size="7.5" font-weight="bold" text-anchor="middle">Producers</text>
            </g>

            <!-- Node 3: Pollinators & Birds -->
            <g class="cursor-pointer" onclick="selectWebNode('pollinators')">
                <circle cx="300" cy="100" r="22" fill="#ea580c" stroke="#fbbf24" stroke-width="2"/>
                <text x="300" y="104" fill="#ffffff" font-size="7.5" font-weight="bold" text-anchor="middle">Pollinators</text>
            </g>

            <!-- Node 4: Humans & Animals -->
            <g class="cursor-pointer" onclick="selectWebNode('herbivores')">
                <circle cx="140" cy="180" r="22" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                <text x="140" y="184" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Humans & Herd</text>
            </g>

            <!-- Node 5: Soil Decomposers & Microbes -->
            <g class="cursor-pointer" onclick="selectWebNode('decomposers')">
                <circle cx="260" cy="180" r="22" fill="#78350f" stroke="#d97706" stroke-width="2"/>
                <text x="260" y="184" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Decomposers</text>
            </g>

            <!-- Center Core: Harmony of the Web -->
            <circle cx="200" cy="120" r="16" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="200" y="123" fill="#38bdf8" font-size="7" font-weight="bold" text-anchor="middle">WEB</text>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-2">
        <button onclick="selectWebNode('plants')" class="p-2 bg-emerald-950/80 hover:bg-emerald-900 border border-emerald-500 rounded-lg text-xs font-bold text-emerald-300">
            Plants (Producers)
        </button>
        <button onclick="selectWebNode('pollinators')" class="p-2 bg-amber-950/80 hover:bg-amber-900 border border-amber-500 rounded-lg text-xs font-bold text-amber-300">
            Birds & Bees
        </button>
        <button onclick="selectWebNode('decomposers')" class="p-2 bg-slate-900 hover:bg-slate-800 border border-slate-700 rounded-lg text-xs font-bold text-slate-200">
            Soil Decomposers
        </button>
    </div>
    <div id="sim10Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>The Web of Life:</strong> Every organism plays an irreplaceable role. Green plants capture sunlight, pollinators fertilize crops, starlings eat pests, and soil microbes recycle vital nutrients!
    </div>
</div>
"""

# SIM 11: World Family (Vasudhaiva Kutumbakam Cosmic Wheel)
SIMS[11] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-purple-400 uppercase tracking-wider block mb-1">Vasudhaiva Kutumbakam: Planetary Family Wheel</span>
        <p class="text-[11px] text-slate-400">Celebrate the timeless Sanskrit philosophy: humans, animals, plants, rivers, & sky form one family!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-purple-950/30 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Outer Rotary Family Ring -->
            <g id="familyMandalaGroup" transform="translate(200, 120)">
                <circle cx="0" cy="0" r="88" fill="none" stroke="#6b21a8" stroke-width="2" stroke-dasharray="4,4"/>
                
                <!-- 5 Family Segments around the circle -->
                <!-- 1. All Humanity (0 deg: 70, 0) -->
                <circle cx="70" cy="0" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                <text x="70" y="4" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">Humanity</text>

                <!-- 2. Animal Kingdom (72 deg: 21.6, 66.5) -->
                <circle cx="21.6" cy="66.5" r="16" fill="#ea580c" stroke="#fbbf24" stroke-width="2"/>
                <text x="21.6" y="70" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">Animals</text>

                <!-- 3. Trees & Forests (144 deg: -56.6, 41.1) -->
                <circle cx="-56.6" cy="41.1" r="16" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
                <text x="-56.6" y="45" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">Forests</text>

                <!-- 4. Rivers & Oceans (216 deg: -56.6, -41.1) -->
                <circle cx="-56.6" cy="-41.1" r="16" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
                <text x="-56.6" y="-37" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">Rivers</text>

                <!-- 5. Atmosphere & Sky (288 deg: 21.6, -66.5) -->
                <circle cx="21.6" cy="-66.5" r="16" fill="#7c3aed" stroke="#c084fc" stroke-width="2"/>
                <text x="21.6" y="-62.5" fill="#ffffff" font-size="6.5" font-weight="bold" text-anchor="middle">Atmosphere</text>

                <!-- Center Core: Vasudhaiva Kutumbakam -->
                <circle cx="0" cy="0" r="32" fill="#f59e0b" stroke="#fde047" stroke-width="2"/>
                <text x="0" y="-3" fill="#020617" font-size="7" font-weight="bold" text-anchor="middle">ONE EARTH</text>
                <text x="0" y="9" fill="#020617" font-size="6.5" font-weight="bold" text-anchor="middle">ONE FAMILY</text>
            </g>

            <!-- Sanskrit Wisdom Pill -->
            <rect x="25" y="15" width="135" height="42" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="35" y="28" fill="#94a3b8" font-size="7">MAHA UPANISHAD</text>
            <text x="35" y="42" fill="#c084fc" font-size="9" font-weight="bold">वसुधैव कुटुम्बकम्</text>
            <text x="35" y="52" fill="#cbd5e1" font-size="7">The World is One Family</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="rotateFamilyWheel()" class="p-2 bg-purple-600 hover:bg-purple-500 rounded-lg text-xs font-bold text-white">
            Spin Planetary Family Wheel
        </button>
        <button onclick="reciteUniversalMotto()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Recite Sanskrit Shloka
        </button>
    </div>
    <div id="sim11Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Universal Kinship:</strong> To a noble mind, the entire Earth is one single household. We share one sky, one water cycle, and one destiny with all living beings!
    </div>
</div>
"""

# SIM 12: Nature Protects (Prakriti Rakshati Rakshita Shield)
SIMS[12] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Prakriti Rakshati Rakshita (Reciprocal Bio-Shield)</span>
        <p class="text-[11px] text-slate-400">Discover how protecting mangrove forests shields coastal villages from cyclonic sea surges!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Fierce Ocean Wave Surge (Left) -->
            <path id="cycloneSurgeWave" d="M0,180 Q60,110 110,140 Q130,160 160,180 L0,240 Z" fill="#0284c7" opacity="0.8"/>
            <path d="M0,195 Q70,140 130,170 L0,240 Z" fill="#0369a1" opacity="0.6"/>

            <!-- Mangrove Bio-Shield Buffer (Center: Stilt Roots & Dense Foliage) -->
            <g id="mangroveShieldGroup" transform="translate(170, 100)">
                <!-- Interlocking Stilt Roots -->
                <path d="M25,50 Q10,75 0,90" stroke="#78350f" stroke-width="4" fill="none"/>
                <path d="M25,50 Q40,75 50,90" stroke="#78350f" stroke-width="4" fill="none"/>
                <path d="M25,50 Q30,70 25,90" stroke="#78350f" stroke-width="3.5" fill="none"/>
                <!-- Dense Green Canopy -->
                <circle cx="25" cy="35" r="28" fill="#15803d" stroke="#22c55e" stroke-width="1.5" opacity="0.95"/>
                <circle cx="10" cy="30" r="18" fill="#16a34a" opacity="0.9"/>
                <circle cx="40" cy="30" r="18" fill="#16a34a" opacity="0.9"/>
                <text x="25" y="105" fill="#86efac" font-size="7.5" font-weight="bold" text-anchor="middle">Mangrove Shield</text>
            </g>

            <!-- Protected Coastal Village (Right) -->
            <g id="safeVillage" transform="translate(290, 120)">
                <!-- House 1 -->
                <polygon points="25,20 5,40 45,40" fill="#b45309"/>
                <rect x="10" y="40" width="30" height="25" fill="#fed7aa" stroke="#78350f" stroke-width="1"/>
                <!-- Green Tree -->
                <circle cx="65" cy="35" r="16" fill="#15803d"/>
                <rect x="62" y="50" width="6" height="15" fill="#78350f"/>
                <text x="35" y="80" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Safe Coastal Village</text>
            </g>

            <!-- MoEFCC Motto Banner -->
            <rect x="25" y="20" width="150" height="40" rx="6" fill="#020617" stroke="#22c55e" stroke-width="1.5" opacity="0.95"/>
            <text x="35" y="34" fill="#4ade80" font-size="8.5" font-weight="bold">प्रकृतिः रक्षति रक्षिता</text>
            <text x="35" y="48" fill="#e2e8f0" font-size="7">Nature Protects if Protected</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="launchCycloneSurge()" class="p-2 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white">
            Simulate Cyclone Storm Surge
        </button>
        <button onclick="reinforceMangroves()" class="p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            Nurture Mangrove Buffer
        </button>
    </div>
    <div id="sim12Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Reciprocal Guardianship:</strong> When coastal communities protect mangrove forests, the tangled roots break high waves, safeguarding homes and human lives during tropical cyclones.
    </div>
</div>
"""

# SIM 13: Global Travelers (The World In Your Lunchbox)
SIMS[13] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Global Travelers: The World Inside Your Lunchbox</span>
        <p class="text-[11px] text-slate-400">Click everyday foods and stationery to uncover their incredible geographic birthplaces!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Center Lunchbox Graphic -->
            <g id="lunchboxContainer" transform="translate(130, 45)">
                <rect x="0" y="0" width="140" height="110" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
                <line x1="0" y1="55" x2="140" y2="55" stroke="#334155" stroke-width="1.5"/>
                <line x1="70" y1="55" x2="70" y2="110" stroke="#334155" stroke-width="1.5"/>

                <!-- Compartment 1: Aloo Paratha (Potatoes) -->
                <g class="cursor-pointer" onclick="inspectLunchItem('potato')">
                    <circle cx="35" cy="28" r="16" fill="#d97706"/>
                    <text x="35" y="31" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Potato</text>
                </g>

                <!-- Compartment 2: Tomato & Chilli Salad -->
                <g class="cursor-pointer" onclick="inspectLunchItem('tomato')">
                    <circle cx="105" cy="28" r="16" fill="#dc2626"/>
                    <text x="105" y="31" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Tomato</text>
                </g>

                <!-- Compartment 3: Sweet Rice Kheer (Rice & Sugar) -->
                <g class="cursor-pointer" onclick="inspectLunchItem('rice')">
                    <ellipse cx="35" cy="82" rx="20" ry="14" fill="#f8fafc"/>
                    <text x="35" y="85" fill="#020617" font-size="7" font-weight="bold" text-anchor="middle">Rice/Sugar</text>
                </g>

                <!-- Compartment 4: Notebook & Pen (Paper) -->
                <g class="cursor-pointer" onclick="inspectLunchItem('paper')">
                    <rect x="85" y="68" width="35" height="28" rx="2" fill="#3b82f6"/>
                    <text x="102" y="85" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Paper</text>
                </g>
            </g>

            <!-- Dynamic Origin Card (Right Stage) -->
            <g id="itemOriginCard" transform="translate(290, 35)">
                <rect x="0" y="0" width="100" height="130" rx="8" fill="#020617" stroke="#fbbf24" stroke-width="1.5" opacity="0.95"/>
                <text id="lunchItemTitle" x="50" y="18" fill="#fde047" font-size="8.5" font-weight="bold" text-anchor="middle">Potato Origin</text>
                <text id="lunchItemRegion" x="50" y="36" fill="#38bdf8" font-size="7.5" text-anchor="middle">Andes Mountains</text>
                <text id="lunchItemCountry" x="50" y="52" fill="#cbd5e1" font-size="7" text-anchor="middle">(Peru / Bolivia)</text>
                <text id="lunchItemDate" x="50" y="75" fill="#e2e8f0" font-size="7" text-anchor="middle">Arrived in India:</text>
                <text id="lunchItemAge" x="50" y="90" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">~400 Years Ago</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5">
        <button onclick="inspectLunchItem('potato')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-amber-500/50 text-[10px] font-bold text-amber-300">
            Potato
        </button>
        <button onclick="inspectLunchItem('tomato')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-rose-500/50 text-[10px] font-bold text-rose-300">
            Tomato/Chilli
        </button>
        <button onclick="inspectLunchItem('rice')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-[10px] font-bold text-emerald-300">
            Rice/Sugar
        </button>
        <button onclick="inspectLunchItem('paper')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-blue-500/50 text-[10px] font-bold text-blue-300">
            Paper
        </button>
    </div>
    <div id="sim13Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>The Global Meal:</strong> Potatoes and tomatoes originated in the South American Andes; rice and sugarcane sugar came from ancient India; and paper was invented in China!
    </div>
</div>
"""

# SIM 14: Earth Guardians (Daily Action Checklist)
SIMS[14] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-teal-400 uppercase tracking-wider block mb-1">Earth Guardians: Daily Environmental Impact Dashboard</span>
        <p class="text-[11px] text-slate-400">Toggle daily mindful actions to see your real-time environmental score and water/energy savings!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Central Eco-Badge Gauge -->
            <g id="ecoGaugeGroup" transform="translate(200, 100)">
                <circle cx="0" cy="0" r="60" fill="#0f172a" stroke="#334155" stroke-width="4"/>
                <circle id="ecoMeterArc" cx="0" cy="0" r="60" fill="none" stroke="#22c55e" stroke-width="5" stroke-dasharray="377" stroke-dashoffset="180"/>
                <text x="0" y="-8" fill="#94a3b8" font-size="8" text-anchor="middle">PLANET IMPACT</text>
                <text id="ecoScoreText" x="0" y="16" fill="#4ade80" font-size="20" font-weight="bold" text-anchor="middle">75%</text>
                <text x="0" y="32" fill="#fde047" font-size="8" font-weight="bold" text-anchor="middle">Guardian Level</text>
            </g>

            <!-- Metrics Panel Left -->
            <g transform="translate(25, 45)">
                <rect x="0" y="0" width="105" height="135" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5" opacity="0.95"/>
                <text x="52" y="18" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">WATER SAVED</text>
                <text id="waterSavedMetric" x="52" y="45" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">24 Litres</text>
                <text x="52" y="60" fill="#94a3b8" font-size="7" text-anchor="middle">per day</text>
                <line x1="10" y1="72" x2="95" y2="72" stroke="#334155" stroke-width="1"/>
                <text x="52" y="90" fill="#fbbf24" font-size="8" font-weight="bold" text-anchor="middle">COAL SAVED</text>
                <text id="energySavedMetric" x="52" y="112" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">1.2 kWh</text>
            </g>

            <!-- Metrics Panel Right -->
            <g transform="translate(275, 45)">
                <rect x="0" y="0" width="105" height="135" rx="8" fill="#020617" stroke="#22c55e" stroke-width="1.5" opacity="0.95"/>
                <text x="52" y="18" fill="#4ade80" font-size="8" font-weight="bold" text-anchor="middle">PLASTIC AVOIDED</text>
                <text id="plasticAvoidedMetric" x="52" y="45" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">4 Bags</text>
                <text x="52" y="60" fill="#94a3b8" font-size="7" text-anchor="middle">cloth upcycled</text>
                <line x1="10" y1="72" x2="95" y2="72" stroke="#334155" stroke-width="1"/>
                <text x="52" y="90" fill="#c084fc" font-size="8" font-weight="bold" text-anchor="middle">TREES NURTURED</text>
                <text id="treesPlantedMetric" x="52" y="112" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">1 Neem Sapling</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5">
        <button onclick="toggleAction('tap')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-sky-500/50 text-[10px] font-bold text-sky-300">
            Fix Leaking Tap
        </button>
        <button onclick="toggleAction('power')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-amber-500/50 text-[10px] font-bold text-amber-300">
            Turn Off Fan/Light
        </button>
        <button onclick="toggleAction('plastic')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-[10px] font-bold text-emerald-300">
            Refuse Plastic Bag
        </button>
        <button onclick="toggleAction('tree')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-purple-500/50 text-[10px] font-bold text-purple-300">
            Plant Neem Tree
        </button>
    </div>
    <div id="sim14Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Daily Stewardship:</strong> Closing taps while brushing saves up to 10 litres of water daily. Turning off unused fans cuts coal burning. Small daily choices protect our shared planet!
    </div>
</div>
"""

# SIM 15: Seasons Across Borders (Opposite Hemispheres Clock)
SIMS[15] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider block mb-1">Seasons Across Borders: Hemispheric Clock</span>
        <p class="text-[11px] text-slate-400">Discover how Earth's 23.5° axial tilt creates opposite seasons across Northern & Southern Hemispheres!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Sun Rays Coming from Left -->
            <circle cx="20" cy="120" r="35" fill="#f59e0b" opacity="0.8"/>
            <line x1="55" y1="80" x2="130" y2="80" stroke="#fde047" stroke-width="1.5" stroke-dasharray="3,3"/>
            <line x1="55" y1="120" x2="130" y2="120" stroke="#fde047" stroke-width="2"/>
            <line x1="55" y1="160" x2="130" y2="160" stroke="#fde047" stroke-width="1.5" stroke-dasharray="3,3"/>

            <!-- Tilted Earth Globe (Center) -->
            <g id="tiltedEarthGlobe" transform="translate(190, 120)">
                <!-- Earth Sphere -->
                <circle cx="0" cy="0" r="60" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
                <!-- Tilted Axis Line (23.5 deg) -->
                <line x1="-25" y1="-75" x2="25" y2="75" stroke="#ffffff" stroke-width="2" stroke-dasharray="4,3"/>
                <!-- Equator Line -->
                <line x1="-60" y1="20" x2="60" y2="-20" stroke="#fbbf24" stroke-width="1.5"/>

                <!-- Northern Hemisphere (India - Tilted Toward Sun) -->
                <circle cx="-15" cy="-25" r="7" fill="#15803d"/>
                <text x="-15" y="-12" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">India</text>

                <!-- Southern Hemisphere (Australia - Tilted Away) -->
                <circle cx="25" cy="30" r="7" fill="#b45309"/>
                <text x="25" y="44" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Australia</text>
            </g>

            <!-- Hemisphere Contrast Cards (Right Side) -->
            <g transform="translate(275, 45)">
                <rect x="0" y="0" width="110" height="135" rx="8" fill="#020617" stroke="#334155" opacity="0.95"/>
                <text x="55" y="18" fill="#f59e0b" font-size="8" font-weight="bold" text-anchor="middle">JUNE SOLSTICE</text>
                
                <!-- North Status -->
                <rect x="8" y="30" width="94" height="42" rx="4" fill="#14532d"/>
                <text x="55" y="44" fill="#4ade80" font-size="7.5" font-weight="bold" text-anchor="middle">Northern Hemisphere</text>
                <text x="55" y="58" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">SUMMER (India)</text>

                <!-- South Status -->
                <rect x="8" y="80" width="94" height="42" rx="4" fill="#082f49"/>
                <text x="55" y="94" fill="#38bdf8" font-size="7.5" font-weight="bold" text-anchor="middle">Southern Hemisphere</text>
                <text x="55" y="108" fill="#bae6fd" font-size="9" font-weight="bold" text-anchor="middle">WINTER (Australia)</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="setSolsticeSeason('june')" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            June: Summer (North) / Winter (South)
        </button>
        <button onclick="setSolsticeSeason('december')" class="p-2 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white">
            December: Winter (North) / Summer (South)
        </button>
    </div>
    <div id="sim15Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Hemispheric Harmony:</strong> When children in India celebrate summer vacation in June, children in Australia and Argentina are wearing woollens during winter! Migrating animals use these opposite cycles to travel and thrive.
    </div>
</div>
"""

# SIM 16: Our Living Earth (The Planetary Synthesis Studio)
SIMS[16] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block mb-1">Our Living Earth: Four Planetary Spheres Laboratory</span>
        <p class="text-[11px] text-slate-400">Interact with the four interconnected spheres: Atmosphere, Hydrosphere, Biosphere, and Geosphere!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Center Earth with 4 Concentric Spheres -->
            <g id="planetarySpheresGraphic" transform="translate(160, 120)">
                <!-- 1. Geosphere (Solid Core/Crust) -->
                <circle cx="0" cy="0" r="40" fill="#78350f" stroke="#b45309" stroke-width="2"/>
                <text x="0" y="4" fill="#fde68a" font-size="7" font-weight="bold" text-anchor="middle">Geosphere</text>

                <!-- 2. Hydrosphere (Water Layer) -->
                <circle id="hydroRing" cx="0" cy="0" r="56" fill="none" stroke="#0284c7" stroke-width="3" opacity="0.8"/>

                <!-- 3. Biosphere (Life Layer) -->
                <circle id="bioRing" cx="0" cy="0" r="70" fill="none" stroke="#22c55e" stroke-width="3" stroke-dasharray="4,4" opacity="0.9"/>

                <!-- 4. Atmosphere (Air Shield) -->
                <circle id="atmoRing" cx="0" cy="0" r="84" fill="none" stroke="#38bdf8" stroke-width="2.5" opacity="0.6"/>
            </g>

            <!-- Layer Information Card (Right Stage) -->
            <g transform="translate(265, 40)">
                <rect x="0" y="0" width="120" height="145" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5" opacity="0.95"/>
                <text id="sphereTitle" x="60" y="18" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle">Atmosphere (Air)</text>
                <text id="sphereDesc1" x="10" y="40" fill="#e2e8f0" font-size="7">• 78% Nitrogen, 21% O₂</text>
                <text id="sphereDesc2" x="10" y="60" fill="#e2e8f0" font-size="7">• Shields UV with Ozone</text>
                <text id="sphereDesc3" x="10" y="80" fill="#e2e8f0" font-size="7">• Circulates rainclouds</text>
                <text id="sphereDesc4" x="10" y="100" fill="#e2e8f0" font-size="7">• Traps warmth (Greenhouse)</text>
                <rect x="10" y="115" width="100" height="20" rx="3" fill="#0369a1"/>
                <text x="60" y="128" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Common Heritage</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5">
        <button onclick="inspectSphere('atmosphere')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-sky-500/50 text-[10px] font-bold text-sky-300">
            Atmosphere
        </button>
        <button onclick="inspectSphere('hydrosphere')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-blue-500/50 text-[10px] font-bold text-blue-300">
            Hydrosphere
        </button>
        <button onclick="inspectSphere('biosphere')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-[10px] font-bold text-emerald-300">
            Biosphere
        </button>
        <button onclick="inspectSphere('geosphere')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-amber-500/50 text-[10px] font-bold text-amber-300">
            Geosphere
        </button>
    </div>
    <div id="sim16Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Our Living Earth:</strong> All four spheres—air, water, living creatures, and soil—interact seamlessly. We are proud custodians of this miracle planet. Vasudhaiva Kutumbakam!
    </div>
</div>
"""

print("Simulators 9 to 16 defined.")

