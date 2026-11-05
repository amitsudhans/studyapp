"""
Simulators 9 to 16 for NCERT Class 5 Science Chapter 9: Rhythms of Nature
Zero raw LaTeX! Clean Unicode symbols.
"""

SIMS = {}

# SIM 9: Sharad Autumn (Riverbank & Kash Grass)
SIMS[9] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block mb-1">Sharad Autumn Riverbank & Fragrance Lab</span>
        <p class="text-[11px] text-slate-400">Experience crystal-clear sapphire skies, waving white Kaash reeds, and nocturnal Shiuli blooms!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-sky-950 via-indigo-950 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Full Moon (Sharad Purnima) -->
            <circle id="sharadMoon" cx="330" cy="50" r="22" fill="#fef08a" opacity="0.9"/>
            <circle cx="330" cy="50" r="30" fill="none" stroke="#fef08a" stroke-width="1" opacity="0.4">
                <animate attributeName="r" values="26;34;26" dur="3s" repeatCount="indefinite"/>
            </circle>

            <!-- Calm Autumn River Surface -->
            <path d="M0,160 Q100,150 200,160 T400,160 L400,240 L0,240 Z" fill="#0369a1" opacity="0.4"/>
            <path d="M0,175 Q100,170 200,175 T400,175 L400,240 L0,240 Z" fill="#075985" opacity="0.6"/>

            <!-- Kaash Reed Cluster 1 (Left Riverbank) -->
            <g id="kaashReedsLeft">
                <!-- Stems -->
                <path d="M50,220 Q55,140 45,90" stroke="#a3e635" stroke-width="2.5" fill="none"/>
                <path d="M70,225 Q75,130 65,80" stroke="#a3e635" stroke-width="2.5" fill="none"/>
                <path d="M90,230 Q85,150 95,95" stroke="#a3e635" stroke-width="2.5" fill="none"/>
                <!-- White Fluffy Plumes -->
                <ellipse cx="45" cy="85" rx="8" ry="25" fill="#f8fafc" opacity="0.95" transform="rotate(-10 45 85)"/>
                <ellipse cx="65" cy="75" rx="9" ry="28" fill="#ffffff" opacity="0.95" transform="rotate(-5 65 75)"/>
                <ellipse cx="95" cy="90" rx="8" ry="24" fill="#f8fafc" opacity="0.95" transform="rotate(10 95 90)"/>
            </g>

            <!-- Fragrant Shiuli / Parijat Tree (Right Bank) -->
            <g id="shiuliTree">
                <!-- Trunk & Leaves -->
                <path d="M220,220 Q225,160 215,130 Q210,110 195,95" stroke="#78350f" stroke-width="7" fill="none"/>
                <path d="M215,130 Q240,115 250,90" stroke="#78350f" stroke-width="4.5" fill="none"/>
                <circle cx="190" cy="85" r="32" fill="#15803d" opacity="0.85"/>
                <circle cx="240" cy="80" r="26" fill="#16a34a" opacity="0.85"/>
                <!-- Shiuli Flowers (White petals with fiery orange stalks) -->
                <circle cx="180" cy="80" r="3" fill="#f97316"/>
                <circle cx="180" cy="80" r="6" fill="#ffffff" stroke="#ea580c" stroke-width="1" opacity="0.9"/>
                <circle cx="205" cy="90" r="3" fill="#f97316"/>
                <circle cx="205" cy="90" r="6" fill="#ffffff" stroke="#ea580c" stroke-width="1" opacity="0.9"/>
                <circle cx="235" cy="75" r="3" fill="#f97316"/>
                <circle cx="235" cy="75" r="6" fill="#ffffff" stroke="#ea580c" stroke-width="1" opacity="0.9"/>
            </g>

            <!-- Floating Fallen Flowers on Ground -->
            <g id="fallenFlowers">
                <circle cx="170" cy="215" r="4" fill="#ffffff" stroke="#ea580c" stroke-width="1"/>
                <circle cx="190" cy="222" r="4" fill="#ffffff" stroke="#ea580c" stroke-width="1"/>
                <circle cx="240" cy="218" r="4" fill="#ffffff" stroke="#ea580c" stroke-width="1"/>
            </g>

            <!-- Info Floating Pill -->
            <rect x="20" y="20" width="130" height="40" rx="6" fill="#020617" stroke="#334155" opacity="0.92"/>
            <text x="30" y="34" fill="#94a3b8" font-size="7">SHARAD ATMOSPHERE</text>
            <text id="sharadPillText" x="30" y="48" fill="#38bdf8" font-size="10" font-weight="bold">Sapphire Skies & Moon</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="swayKaashGrass()" class="p-2 bg-emerald-700 hover:bg-emerald-600 rounded-lg text-xs font-bold text-white">
            Wavering Kaash Plumes
        </button>
        <button onclick="bloomShiuliFlowers()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Release Shiuli Perfume
        </button>
    </div>
    <div id="sim9Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Sharad (Autumn):</strong> Ashvina–Kartika marks calm water, white Kaash grass swaying by riverbanks, nocturnal orange-stemmed Shiuli blossoms, and bright moonlight.
    </div>
</div>
"""

# SIM 10: Hemant Pre-Winter (Dew & Golden Harvest)
SIMS[10] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Hemant Pre-Winter Dew & Harvest Laboratory</span>
        <p class="text-[11px] text-slate-400">Witness morning mist, glittering dewdrops on blades of grass, and golden ripe paddy fields!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-amber-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Gentle Morning Sun through Mist -->
            <circle cx="80" cy="60" r="30" fill="#fde047" opacity="0.4"/>
            <circle cx="80" cy="60" r="20" fill="#fef08a" opacity="0.8"/>
            <!-- Morning Mist Layers -->
            <ellipse id="mistLayer" cx="200" cy="90" rx="190" ry="25" fill="#f1f5f9" opacity="0.25"/>

            <!-- Golden Ripened Paddy Field -->
            <rect x="0" y="140" width="400" height="100" fill="#78350f" opacity="0.8"/>
            <g id="paddyStalks">
                <path d="M30,230 Q35,160 25,130" stroke="#f59e0b" stroke-width="3" fill="none"/>
                <path d="M50,230 Q60,155 45,125" stroke="#eab308" stroke-width="3" fill="none"/>
                <path d="M70,230 Q75,150 65,120" stroke="#f59e0b" stroke-width="3" fill="none"/>
                <path d="M90,230 Q105,155 90,125" stroke="#fbbf24" stroke-width="3" fill="none"/>
                <path d="M120,230 Q130,150 115,120" stroke="#f59e0b" stroke-width="3" fill="none"/>
                <path d="M150,230 Q155,150 145,120" stroke="#eab308" stroke-width="3" fill="none"/>
                <path d="M180,230 Q190,155 175,125" stroke="#f59e0b" stroke-width="3" fill="none"/>
                <!-- Heavy Golden Grain Heads Bending Down -->
                <ellipse cx="23" cy="130" rx="8" ry="14" fill="#fbbf24" transform="rotate(30 23 130)"/>
                <ellipse cx="43" cy="125" rx="8" ry="14" fill="#f59e0b" transform="rotate(30 43 125)"/>
                <ellipse cx="63" cy="120" rx="8" ry="14" fill="#fbbf24" transform="rotate(30 63 120)"/>
                <ellipse cx="88" cy="125" rx="8" ry="14" fill="#f59e0b" transform="rotate(30 88 125)"/>
                <ellipse cx="113" cy="120" rx="8" ry="14" fill="#fbbf24" transform="rotate(30 113 120)"/>
                <ellipse cx="143" cy="120" rx="8" ry="14" fill="#f59e0b" transform="rotate(30 143 120)"/>
            </g>

            <!-- Large Grass Blade with Condensing Dewdrop (Right Stage) -->
            <g id="dewDropFeature" transform="translate(250, 80)">
                <path d="M10,140 Q40,60 120,30 Q80,90 20,150 Z" fill="#22c55e" opacity="0.9"/>
                <!-- Sparkling Dewdrop on Grass Tip -->
                <ellipse id="condensingDew" cx="118" cy="32" rx="10" ry="12" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5" opacity="0.95"/>
                <circle cx="115" cy="28" r="3" fill="#ffffff" opacity="0.9"/>
                <!-- Drip effect trail -->
                <line x1="118" y1="44" x2="118" y2="70" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.4"/>
            </g>

            <!-- Til-Gur Sweet Plate Icon -->
            <g transform="translate(300, 160)">
                <ellipse cx="40" cy="30" rx="36" ry="16" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
                <!-- Sesame Ladoos (Til-Gur) -->
                <circle cx="25" cy="25" r="9" fill="#d97706" stroke="#b45309" stroke-width="1"/>
                <circle cx="42" cy="22" r="10" fill="#b45309" stroke="#78350f" stroke-width="1"/>
                <circle cx="55" cy="26" r="8" fill="#d97706" stroke="#b45309" stroke-width="1"/>
                <text x="40" y="42" fill="#fef08a" font-size="7" font-weight="bold" text-anchor="middle">Til-Gur Sweet</text>
            </g>

            <!-- Status Indicator Card -->
            <rect x="20" y="20" width="130" height="38" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="30" y="32" fill="#94a3b8" font-size="7">PRE-WINTER PHENOMENON</text>
            <text id="hemantCardText" x="30" y="46" fill="#fbbf24" font-size="10" font-weight="bold">Dew & Golden Fields</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="sparkleDewdrops()" class="p-2 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white">
            Condense Morning Dew
        </button>
        <button onclick="tasteTilGurSweet()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Sample Til-Gur Treat
        </button>
    </div>
    <div id="sim10Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Hemant (Pre-Winter):</strong> Margashirsha–Pausha brings pleasant morning chills, glistening dewdrops on grass tips, golden paddy harvesting, and warm nourishing sesame-jaggery sweets.
    </div>
</div>
"""

# SIM 11: Shishir Winter (Winter Chill & Immunity Pantry)
SIMS[11] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1">Shishir Winter Chill & Immunity Laboratory</span>
        <p class="text-[11px] text-slate-400">Explore crisp chilly winds, bare trees, warming evening bonfires, and immunity foods!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-cyan-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Cold Frosty Sky & Distant Snowy Peaks -->
            <polygon points="40,120 100,50 160,120" fill="#334155" opacity="0.5"/>
            <polygon points="75,70 100,50 125,70" fill="#f8fafc" opacity="0.9"/>
            <polygon points="120,130 190,40 260,130" fill="#1e293b" opacity="0.6"/>
            <polygon points="165,65 190,40 215,65" fill="#ffffff" opacity="0.95"/>

            <!-- Bare Deciduous Tree (Shedding leaves to conserve water) -->
            <g id="bareWinterTree" transform="translate(60, 90)">
                <path d="M40,110 Q42,60 38,30 Q35,15 20,0" stroke="#64748b" stroke-width="5" fill="none"/>
                <path d="M38,30 Q55,20 65,5" stroke="#64748b" stroke-width="3" fill="none"/>
                <path d="M40,55 Q20,40 10,25" stroke="#64748b" stroke-width="2.5" fill="none"/>
                <path d="M40,75 Q60,60 75,45" stroke="#64748b" stroke-width="2" fill="none"/>
                <text x="40" y="125" fill="#94a3b8" font-size="8" text-anchor="middle">Bare Tree (Leaf Shedding)</text>
            </g>

            <!-- Bonfire with Flickering Flames -->
            <g id="bonfire" transform="translate(180, 150)">
                <!-- Cross Logs -->
                <line x1="5" y1="35" x2="45" y2="25" stroke="#78350f" stroke-width="6"/>
                <line x1="5" y1="25" x2="45" y2="35" stroke="#78350f" stroke-width="6"/>
                <!-- Flame Elements -->
                <path d="M25,30 Q15,10 25,-5 Q35,10 25,30 Z" fill="#f97316">
                    <animate attributeName="d" values="M25,30 Q15,10 25,-5 Q35,10 25,30 Z; M25,30 Q20,5 25,-12 Q30,5 25,30 Z; M25,30 Q15,10 25,-5 Q35,10 25,30 Z" dur="0.8s" repeatCount="indefinite"/>
                </path>
                <path d="M25,28 Q18,12 25,5 Q32,12 25,28 Z" fill="#fef08a"/>
                <text x="25" y="48" fill="#fbbf24" font-size="8" font-weight="bold" text-anchor="middle">Warm Bonfire</text>
            </g>

            <!-- Immunity Pantry Showcase (Right Stage) -->
            <g id="immunityPantry" transform="translate(270, 70)">
                <rect x="0" y="0" width="115" height="130" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5" opacity="0.95"/>
                <text x="57" y="16" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle">WINTER PANTRY</text>
                
                <!-- Sarson ka Saag Bowl -->
                <circle cx="30" cy="40" r="14" fill="#14532d" stroke="#16a34a" stroke-width="1.5"/>
                <circle cx="30" cy="40" r="4" fill="#fef08a"/>
                <text x="50" y="43" fill="#f8fafc" font-size="8">Sarson Saag</text>

                <!-- Vitamin-C Oranges -->
                <circle cx="30" cy="70" r="12" fill="#ea580c"/>
                <circle cx="30" cy="70" r="4" fill="#fb923c"/>
                <text x="50" y="73" fill="#f8fafc" font-size="8">Citrus Orange</text>

                <!-- Nutrient-Dense Amla -->
                <circle cx="30" cy="98" r="10" fill="#65a30d"/>
                <path d="M26,90 Q30,98 34,90" stroke="#365314" stroke-width="1" fill="none"/>
                <text x="50" y="101" fill="#f8fafc" font-size="8">Amla (Gooseberry)</text>
            </g>

            <!-- Thermometer Display -->
            <rect x="15" y="15" width="85" height="35" rx="5" fill="#020617" stroke="#334155" opacity="0.92"/>
            <text x="22" y="27" fill="#94a3b8" font-size="7">TEMPERATURE</text>
            <text id="shishirTemp" x="22" y="41" fill="#38bdf8" font-size="11" font-weight="bold">8°C (Chilly)</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="stokeWinterBonfire()" class="p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Stoke Fire & Warm Up
        </button>
        <button onclick="inspectImmunityFoods()" class="p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            Inspect Immunity Foods
        </button>
    </div>
    <div id="sim11Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Shishir (Winter):</strong> Magha–Phalguna brings freezing winds from the Himalayas. Trees drop leaves to preserve moisture, while citrus fruits, amla, and leafy greens boost human immunity.
    </div>
</div>
"""

# SIM 12: Regional Climatic Contrasts
SIMS[12] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider block mb-1">Pan-India Regional Climatic Contrasts</span>
        <p class="text-[11px] text-slate-400">Click regions to explore diverse climates: Himalayan snow, Thar desert, tropical coast, & monsoon rain!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Interactive Map Graphic with Highlight Pins -->
            <!-- Simplified India Map Silhouette Outline -->
            <path d="M160,20 L180,45 L200,30 L220,50 L205,75 L230,105 L260,105 L280,120 L270,140 L240,135 L220,160 L185,225 L160,180 L140,165 L130,120 L145,95 L150,55 Z" fill="#1e293b" stroke="#475569" stroke-width="1.5" opacity="0.6"/>

            <!-- Region Hotspots (Clickable Pins) -->
            <!-- 1. Kashmir / Ladakh (North) -->
            <g onclick="selectRegion('kashmir')" class="cursor-pointer" id="pinKashmir">
                <circle cx="180" cy="38" r="10" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
                <text x="180" y="41" fill="#020617" font-size="8" font-weight="bold" text-anchor="middle">1</text>
                <text x="195" y="38" fill="#bae6fd" font-size="8" font-weight="bold">Kashmir</text>
            </g>

            <!-- 2. Rajasthan Thar Desert (West) -->
            <g onclick="selectRegion('rajasthan')" class="cursor-pointer" id="pinRajasthan">
                <circle cx="140" cy="100" r="10" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
                <text x="140" y="103" fill="#020617" font-size="8" font-weight="bold" text-anchor="middle">2</text>
                <text x="95" y="103" fill="#fde68a" font-size="8" font-weight="bold">Rajasthan</text>
            </g>

            <!-- 3. Meghalaya Mawsynram (East) -->
            <g onclick="selectRegion('meghalaya')" class="cursor-pointer" id="pinMeghalaya">
                <circle cx="270" cy="115" r="10" fill="#3b82f6" stroke="#ffffff" stroke-width="2"/>
                <text x="270" y="118" fill="#020617" font-size="8" font-weight="bold" text-anchor="middle">3</text>
                <text x="285" y="118" fill="#93c5fd" font-size="8" font-weight="bold">Meghalaya</text>
            </g>

            <!-- 4. Kerala Coastal Tropics (South) -->
            <g onclick="selectRegion('kerala')" class="cursor-pointer" id="pinKerala">
                <circle cx="170" cy="195" r="10" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
                <text x="170" y="198" fill="#020617" font-size="8" font-weight="bold" text-anchor="middle">4</text>
                <text x="185" y="198" fill="#a7f3d0" font-size="8" font-weight="bold">Kerala</text>
            </g>

            <!-- Dynamic Regional Feature Preview Card (Right Box) -->
            <g id="regionFeatureCard" transform="translate(25, 140)">
                <rect x="0" y="0" width="120" height="75" rx="6" fill="#020617" stroke="#38bdf8" stroke-width="1.5" opacity="0.95"/>
                <text id="regCardTitle" x="10" y="18" fill="#38bdf8" font-size="9" font-weight="bold">Kashmir Himalayas</text>
                <text id="regCardDesc1" x="10" y="32" fill="#e2e8f0" font-size="7.5">• Sub-zero snow & ice</text>
                <text id="regCardDesc2" x="10" y="46" fill="#e2e8f0" font-size="7.5">• Pheran & Kangri pot</text>
                <text id="regCardDesc3" x="10" y="60" fill="#e2e8f0" font-size="7.5">• Wooden insulated roofs</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5">
        <button onclick="selectRegion('kashmir')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-sky-500/50 text-[10px] font-bold text-sky-300">
            1. Kashmir (Snow)
        </button>
        <button onclick="selectRegion('rajasthan')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-amber-500/50 text-[10px] font-bold text-amber-300">
            2. Desert (Heat)
        </button>
        <button onclick="selectRegion('meghalaya')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-blue-500/50 text-[10px] font-bold text-blue-300">
            3. Rain (Mawsynram)
        </button>
        <button onclick="selectRegion('kerala')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-[10px] font-bold text-emerald-300">
            4. Kerala (Coast)
        </button>
    </div>
    <div id="sim12Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Regional Contrasts:</strong> While Kashmir shivers at −5°C requiring Kangri fire pots under pherans, Kerala stays warm and humid at 28°C with coconut breezes!
    </div>
</div>
"""

# SIM 13: Seasonal Crops (Agricultural Triad)
SIMS[13] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-lime-400 uppercase tracking-wider block mb-1">Agricultural Cropping Triad (Kharif, Rabi, Zaid)</span>
        <p class="text-[11px] text-slate-400">Discover which crops grow in which season: monsoon rice, winter wheat, and summer melons!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Soil and Weather Backdrops -->
            <rect x="0" y="150" width="400" height="90" fill="#3f2e1a" opacity="0.8"/>
            <line x1="0" y1="150" x2="400" y2="150" stroke="#78350f" stroke-width="2"/>

            <!-- Dynamic Crop Visual Stage -->
            <g id="cropStageGraphic">
                <!-- Default: Kharif Paddy Field -->
                <!-- Rain Clouds above -->
                <circle cx="200" cy="40" r="22" fill="#475569"/>
                <circle cx="225" cy="35" r="26" fill="#64748b"/>
                <circle cx="175" cy="40" r="20" fill="#475569"/>
                <!-- Rain streaks -->
                <line x1="180" y1="65" x2="175" y2="85" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,3"/>
                <line x1="205" y1="68" x2="200" y2="88" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,3"/>
                <line x1="225" y1="65" x2="220" y2="85" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,3"/>

                <!-- Rice Paddy Shoots in Watery Soil -->
                <rect x="50" y="150" width="300" height="20" fill="#0284c7" opacity="0.4"/>
                <path d="M120,165 Q110,120 95,95" stroke="#22c55e" stroke-width="3" fill="none"/>
                <path d="M120,165 Q130,115 145,95" stroke="#22c55e" stroke-width="3" fill="none"/>
                <path d="M200,165 Q190,115 175,90" stroke="#16a34a" stroke-width="3" fill="none"/>
                <path d="M200,165 Q210,110 225,90" stroke="#16a34a" stroke-width="3" fill="none"/>
                <path d="M280,165 Q270,120 255,95" stroke="#22c55e" stroke-width="3" fill="none"/>
                <path d="M280,165 Q290,115 305,95" stroke="#22c55e" stroke-width="3" fill="none"/>
                <text x="200" y="195" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">Kharif: Water-Hungry Paddy & Cotton</text>
            </g>

            <!-- Sowing & Harvesting Metadata Card -->
            <rect x="20" y="15" width="135" height="46" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="28" y="28" fill="#94a3b8" font-size="7">SEASON & CROPPING CYCLE</text>
            <text id="cropTitle" x="28" y="42" fill="#4ade80" font-size="11" font-weight="bold">Kharif Season</text>
            <text id="cropTiming" x="28" y="54" fill="#cbd5e1" font-size="7.5">Sown: June | Harvest: Oct</text>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-2">
        <button onclick="selectCropPattern('kharif')" class="p-2 bg-emerald-950/80 hover:bg-emerald-900 border border-emerald-500 rounded-lg text-xs font-bold text-emerald-300">
            1. Kharif (Monsoon)
        </button>
        <button onclick="selectCropPattern('rabi')" class="p-2 bg-amber-950/80 hover:bg-amber-900 border border-amber-500 rounded-lg text-xs font-bold text-amber-300">
            2. Rabi (Winter)
        </button>
        <button onclick="selectCropPattern('zaid')" class="p-2 bg-red-950/80 hover:bg-red-900 border border-red-500 rounded-lg text-xs font-bold text-red-300">
            3. Zaid (Summer)
        </button>
    </div>
    <div id="sim13Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Kharif Crops:</strong> Planted at the onset of monsoon rains (June–July) and harvested in autumn (September–October). Examples: Rice (paddy), maize, cotton, and groundnut.
    </div>
</div>
"""

# SIM 14: Harvest Festivals
SIMS[14] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-yellow-400 uppercase tracking-wider block mb-1">Pan-Indian Harvest Festival Wheel</span>
        <p class="text-[11px] text-slate-400">Spin the wheel to explore how farmers across India thank nature for bountiful crops!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Center Rotary Festival Hub -->
            <g id="festivalWheelGroup" transform="translate(140, 120)">
                <circle cx="0" cy="0" r="80" fill="#0f172a" stroke="#475569" stroke-width="2"/>
                <!-- Segments -->
                <path d="M0,0 L0,-80 A80,80 0 0,1 76,-25 Z" fill="#b45309" opacity="0.7"/>
                <path d="M0,0 L76,-25 A80,80 0 0,1 47,65 Z" fill="#065f46" opacity="0.7"/>
                <path d="M0,0 L47,65 A80,80 0 0,1 -47,65 Z" fill="#1e40af" opacity="0.7"/>
                <path d="M0,0 L-47,65 A80,80 0 0,1 -76,-25 Z" fill="#86198f" opacity="0.7"/>
                <path d="M0,0 L-76,-25 A80,80 0 0,1 0,-80 Z" fill="#991b1b" opacity="0.7"/>
                <!-- Hub -->
                <circle cx="0" cy="0" r="28" fill="#020617" stroke="#fbbf24" stroke-width="2"/>
                <text x="0" y="4" fill="#fbbf24" font-size="8" font-weight="bold" text-anchor="middle">HARVEST</text>
            </g>

            <!-- Dynamic Selected Festival Visual (Right Side Stage) -->
            <g id="festivalDisplayStage" transform="translate(250, 40)">
                <rect x="0" y="0" width="135" height="160" rx="8" fill="#020617" stroke="#fbbf24" stroke-width="1.5" opacity="0.95"/>
                <!-- Festival Icon Graphic (Default: Makar Sankranti Kites) -->
                <g id="festGraphic">
                    <polygon points="67,25 90,50 67,75 44,50" fill="#ef4444" stroke="#fbbf24" stroke-width="1.5"/>
                    <line x1="67" y1="25" x2="67" y2="75" stroke="#ffffff" stroke-width="1"/>
                    <line x1="44" y1="50" x2="90" y2="50" stroke="#ffffff" stroke-width="1"/>
                    <path d="M67,75 Q75,90 67,100" stroke="#fbbf24" stroke-width="1" fill="none"/>
                </g>
                <text id="festName" x="67" y="115" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Makar Sankranti</text>
                <text id="festRegion" x="67" y="130" fill="#38bdf8" font-size="8" text-anchor="middle">Across India (January)</text>
                <text id="festCustom" x="67" y="145" fill="#cbd5e1" font-size="7" text-anchor="middle">Flying Kites & Til-Gur</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-4 gap-1.5">
        <button onclick="displayFestival('sankranti')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-amber-500/50 text-[10px] font-bold text-amber-300">
            Makar Sankranti
        </button>
        <button onclick="displayFestival('pongal')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-[10px] font-bold text-emerald-300">
            Pongal (Tamil Nadu)
        </button>
        <button onclick="displayFestival('lohri')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-orange-500/50 text-[10px] font-bold text-orange-300">
            Lohri (Punjab)
        </button>
        <button onclick="displayFestival('bihu')" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-indigo-500/50 text-[10px] font-bold text-indigo-300">
            Magh Bihu (Assam)
        </button>
    </div>
    <div id="sim14Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Makar Sankranti:</strong> Marks the Sun's northward journey (*Uttarayana*) and the winter harvest. Families celebrate with soaring colorful kites, sesame *chikki*, and festive prayers!
    </div>
</div>
"""

# SIM 15: Living in Rhythm (Ritucharya Lifestyle Matcher)
SIMS[15] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-teal-400 uppercase tracking-wider block mb-1">Ritucharya Seasonal Lifestyle Simulator</span>
        <p class="text-[11px] text-slate-400">Toggle between Summer and Winter to adapt clothing, hydration, and nutritional diet!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Split Environment Backdrop -->
            <g id="lifestyleBackdrop">
                <rect x="0" y="0" width="200" height="240" fill="#451a03" opacity="0.3"/>
                <rect x="200" y="0" width="200" height="240" fill="#082f49" opacity="0.3"/>
                <line x1="200" y1="0" x2="200" y2="240" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>
            </g>

            <!-- Character Model (Center) -->
            <g id="characterModel" transform="translate(170, 70)">
                <!-- Head -->
                <circle cx="30" cy="20" r="14" fill="#fed7aa"/>
                <path d="M16,16 Q30,6 44,16 Z" fill="#1e293b"/>
                <!-- Torso Clothing (Dynamic) -->
                <rect id="charTorso" x="16" y="34" width="28" height="45" rx="4" fill="#ffffff" stroke="#38bdf8" stroke-width="1.5"/>
                <!-- Legs -->
                <line x1="23" y1="79" x2="23" y2="120" stroke="#1e293b" stroke-width="4"/>
                <line x1="37" y1="79" x2="37" y2="120" stroke="#1e293b" stroke-width="4"/>
            </g>

            <!-- Summer Adaptation Gear (Left) -->
            <g id="summerGear" transform="translate(25, 40)">
                <rect x="0" y="0" width="125" height="160" rx="8" fill="#020617" stroke="#f59e0b" stroke-width="1.5" opacity="0.95"/>
                <text x="62" y="20" fill="#f59e0b" font-size="9" font-weight="bold" text-anchor="middle">SUMMER (Grishma)</text>
                <!-- Light Cotton Shirt Icon -->
                <rect x="42" y="32" width="40" height="30" rx="3" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
                <text x="62" y="52" fill="#020617" font-size="7" font-weight="bold" text-anchor="middle">Airy Cotton</text>
                <!-- Hydrating Buttermilk / Aam Panna -->
                <rect x="48" y="72" width="28" height="35" rx="3" fill="#bae6fd" stroke="#0284c7" stroke-width="1"/>
                <text x="62" y="93" fill="#0369a1" font-size="7" font-weight="bold" text-anchor="middle">Chhaachh</text>
                <text x="62" y="125" fill="#fde68a" font-size="7.5" text-anchor="middle">Cooling hydration</text>
                <text x="62" y="140" fill="#cbd5e1" font-size="7" text-anchor="middle">Rest during noon peak</text>
            </g>

            <!-- Winter Adaptation Gear (Right) -->
            <g id="winterGear" transform="translate(250, 40)">
                <rect x="0" y="0" width="125" height="160" rx="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5" opacity="0.95"/>
                <text x="62" y="20" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">WINTER (Shishir)</text>
                <!-- Heavy Woollen Sweater Icon -->
                <rect x="42" y="32" width="40" height="30" rx="3" fill="#dc2626" stroke="#991b1b" stroke-width="1"/>
                <text x="62" y="52" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Woollen Layers</text>
                <!-- Warming Bajra Roti & Ghee -->
                <circle cx="62" cy="90" r="16" fill="#b45309" stroke="#78350f" stroke-width="1"/>
                <circle cx="62" cy="90" r="5" fill="#fef08a"/>
                <text x="62" y="125" fill="#bae6fd" font-size="7.5" text-anchor="middle">Warming bajra & ghee</text>
                <text x="62" y="140" fill="#cbd5e1" font-size="7" text-anchor="middle">Warm sunshine in day</text>
            </g>
        </svg>
    </div>
    <div class="flex items-center gap-2">
        <button onclick="setLifestyleMode('summer')" class="flex-1 p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Switch to Summer Mode (Grishma)
        </button>
        <button onclick="setLifestyleMode('winter')" class="flex-1 p-2 bg-sky-600 hover:bg-sky-500 rounded-lg text-xs font-bold text-white">
            Switch to Winter Mode (Shishir)
        </button>
    </div>
    <div id="sim15Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Ritucharya Concept:</strong> Living in rhythm with nature means wearing breathable cottons and drinking buttermilk in summer, while dressing in layered woollens and eating warm bajra roti in winter.
    </div>
</div>
"""

# SIM 16: Nature's Harmony (The Eternal Cycle of Seasons)
SIMS[16] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-purple-400 uppercase tracking-wider block mb-1">The Eternal Six-Season Cosmic Wheel</span>
        <p class="text-[11px] text-slate-400">Step through the endless cyclic loop of nature's Shad Ritu and witness the harmony of change!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Center Rotating Mandala Wheel -->
            <g id="cosmicMandala" transform="translate(200, 120)">
                <!-- Outer Wheel Ring -->
                <circle cx="0" cy="0" r="95" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>
                
                <!-- 6 Season Nodes around the circle (Radius = 75) -->
                <!-- 1. Vasanta (0 deg: 75, 0) -->
                <g class="cursor-pointer" onclick="jumpToSeasonCycle(1)">
                    <circle cx="75" cy="0" r="16" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
                    <text x="75" y="4" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Vasanta</text>
                </g>
                <!-- 2. Grishma (60 deg: 37.5, 65) -->
                <g class="cursor-pointer" onclick="jumpToSeasonCycle(2)">
                    <circle cx="37.5" cy="65" r="16" fill="#b45309" stroke="#fbbf24" stroke-width="2"/>
                    <text x="37.5" y="69" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Grishma</text>
                </g>
                <!-- 3. Varsha (120 deg: -37.5, 65) -->
                <g class="cursor-pointer" onclick="jumpToSeasonCycle(3)">
                    <circle cx="-37.5" cy="65" r="16" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>
                    <text x="-37.5" y="69" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Varsha</text>
                </g>
                <!-- 4. Sharad (180 deg: -75, 0) -->
                <g class="cursor-pointer" onclick="jumpToSeasonCycle(4)">
                    <circle cx="-75" cy="0" r="16" fill="#4338ca" stroke="#818cf8" stroke-width="2"/>
                    <text x="-75" y="4" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Sharad</text>
                </g>
                <!-- 5. Hemant (240 deg: -37.5, -65) -->
                <g class="cursor-pointer" onclick="jumpToSeasonCycle(5)">
                    <circle cx="-37.5" cy="-65" r="16" fill="#d97706" stroke="#fcd34d" stroke-width="2"/>
                    <text x="-37.5" y="-61" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Hemant</text>
                </g>
                <!-- 6. Shishir (300 deg: 37.5, -65) -->
                <g class="cursor-pointer" onclick="jumpToSeasonCycle(6)">
                    <circle cx="37.5" cy="-65" r="16" fill="#0e7490" stroke="#67e8f9" stroke-width="2"/>
                    <text x="37.5" y="-61" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Shishir</text>
                </g>

                <!-- Center Golden Sun Core -->
                <circle cx="0" cy="0" r="28" fill="#f59e0b" stroke="#fef08a" stroke-width="2"/>
                <text x="0" y="3" fill="#020617" font-size="8" font-weight="bold" text-anchor="middle">HARMONY</text>
            </g>

            <!-- Flow Indicator Tag -->
            <rect x="25" y="20" width="135" height="38" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="35" y="32" fill="#94a3b8" font-size="7">THE CYCLIC HARMONY</text>
            <text id="seasonCycleName" x="35" y="46" fill="#c084fc" font-size="10" font-weight="bold">Continuous 6-Season Loop</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="stepNextSeasonCycle()" class="p-2 bg-purple-600 hover:bg-purple-500 rounded-lg text-xs font-bold text-white">
            Step to Next Season
        </button>
        <button onclick="toggleSeasonalAutoSpin()" class="p-2 bg-indigo-600 hover:bg-indigo-500 rounded-lg text-xs font-bold text-white">
            Auto-Spin Cosmic Wheel
        </button>
    </div>
    <div id="sim16Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>The Eternal Rhythm:</strong> Change is not a one-way path, but an eternal revolving cycle. Winter cold prepares seeds, Spring wakes flowers, Summer builds heat, Monsoon brings rain, and Autumn brings clarity.
    </div>
</div>
"""

print("Simulators 9 to 16 defined.")

