# make_c4s_ch6_sims_part1.py
# Generates interactive simulators 1 to 8 for Chapter 6: Happy and Healthy Living

simulators_part1 = {}

# SIM 1: Farm-to-Plate Grain Conveyor
simulators_part1["sim-1"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-emerald-300">Farm-to-Plate Grain Cycle Simulator</h4>
            </div>
            <span class="text-xs bg-emerald-500/20 text-emerald-300 px-2.5 py-1 rounded-full font-medium border border-emerald-500/30">Interactive 6 Stages</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2">
            <button onclick="window.selectFarmStage(0)" class="farm-stage-btn active p-2.5 rounded-xl border border-emerald-500/50 bg-emerald-950/40 hover:bg-emerald-900/50 transition-all text-center flex flex-col items-center gap-1">
                <span class="text-xl">🚜</span>
                <span class="text-xs font-semibold">1. Ploughing</span>
            </button>
            <button onclick="window.selectFarmStage(1)" class="farm-stage-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-center flex flex-col items-center gap-1">
                <span class="text-xl">🌱</span>
                <span class="text-xs font-semibold">2. Sowing</span>
            </button>
            <button onclick="window.selectFarmStage(2)" class="farm-stage-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-center flex flex-col items-center gap-1">
                <span class="text-xl">🌾</span>
                <span class="text-xs font-semibold">3. Harvest</span>
            </button>
            <button onclick="window.selectFarmStage(3)" class="farm-stage-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-center flex flex-col items-center gap-1">
                <span class="text-xl">🏬</span>
                <span class="text-xs font-semibold">4. Storage</span>
            </button>
            <button onclick="window.selectFarmStage(4)" class="farm-stage-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-center flex flex-col items-center gap-1">
                <span class="text-xl">🚚</span>
                <span class="text-xs font-semibold">5. Logistics</span>
            </button>
            <button onclick="window.selectFarmStage(5)" class="farm-stage-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-center flex flex-col items-center gap-1">
                <span class="text-xl">🫓</span>
                <span class="text-xs font-semibold">6. Kitchen</span>
            </button>
        </div>

        <div class="relative bg-slate-950/80 rounded-xl p-4 border border-slate-800 min-h-[180px] flex flex-col justify-between">
            <div id="farmStageDisplay" class="flex flex-col sm:flex-row items-center gap-4">
                <div class="w-20 h-20 rounded-2xl bg-emerald-950/60 border border-emerald-500/40 flex items-center justify-center text-4xl shrink-0 shadow-lg shadow-emerald-950/50" id="farmStageIcon">
                    🚜
                </div>
                <div class="flex-1 space-y-1 text-center sm:text-left">
                    <div class="flex items-center gap-2 justify-center sm:justify-start">
                        <span id="farmStageNumber" class="text-xs font-bold uppercase tracking-wider text-emerald-400 bg-emerald-950 px-2 py-0.5 rounded">Stage 1 of 6</span>
                        <h5 id="farmStageName" class="text-base font-bold text-white">Soil Preparation & Aeration</h5>
                    </div>
                    <p id="farmStageDesc" class="text-xs text-slate-300 leading-relaxed">
                        Farmers till and loosen the earth with ploughs. This loosens dense soil clods, allows air and moisture to circulate freely, and prepares a fertile seedbed for planting.
                    </p>
                    <div class="flex flex-wrap gap-2 pt-2 justify-center sm:justify-start">
                        <span id="farmStageMeta" class="text-[11px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded border border-slate-700">Tools: Tractor & Steel Plough</span>
                        <span id="farmStageFact" class="text-[11px] bg-emerald-900/40 text-emerald-300 px-2 py-0.5 rounded border border-emerald-700/50">Scientific Goal: Increases soil pore volume for root oxygenation</span>
                    </div>
                </div>
            </div>

            <div class="w-full bg-slate-800 h-2 rounded-full mt-4 overflow-hidden">
                <div id="farmProgressBar" class="bg-gradient-to-r from-emerald-500 to-teal-400 h-full w-1/6 transition-all duration-300"></div>
            </div>
        </div>

        <div class="flex justify-between items-center text-xs text-slate-400">
            <button onclick="window.prevFarmStage()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition-all">← Previous Stage</button>
            <span class="text-[11px]">Click any stage or step through</span>
            <button onclick="window.nextFarmStage()" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white transition-all">Next Stage →</button>
        </div>
    </div>
"""

# SIM 2: Food Ecosystem Contributor Network
simulators_part1["sim-2"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-amber-300">Food Web Contributors Explorer</h4>
            </div>
            <span class="text-xs bg-amber-500/20 text-amber-300 px-2.5 py-1 rounded-full font-medium border border-amber-500/30">Click Any Contributor</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
            <button onclick="window.selectContributor('sun')" class="contrib-btn active p-2.5 rounded-xl border border-amber-500/50 bg-amber-950/40 hover:bg-amber-900/50 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">☀️</span>
                <div>
                    <div class="text-xs font-bold text-white">Sunlight</div>
                    <div class="text-[10px] text-amber-300">Solar Energy</div>
                </div>
            </button>
            <button onclick="window.selectContributor('earthworm')" class="contrib-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">🪱</span>
                <div>
                    <div class="text-xs font-bold text-white">Earthworm</div>
                    <div class="text-[10px] text-emerald-300">Soil Aerator</div>
                </div>
            </button>
            <button onclick="window.selectContributor('farmer')" class="contrib-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">👨‍🌾</span>
                <div>
                    <div class="text-xs font-bold text-white">Farmer</div>
                    <div class="text-[10px] text-cyan-300">Crop Cultivator</div>
                </div>
            </button>
            <button onclick="window.selectContributor('transporter')" class="contrib-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">🚛</span>
                <div>
                    <div class="text-xs font-bold text-white">Transporter</div>
                    <div class="text-[10px] text-purple-300">Logistics Link</div>
                </div>
            </button>
            <button onclick="window.selectContributor('shopkeeper')" class="contrib-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">🏪</span>
                <div>
                    <div class="text-xs font-bold text-white">Shopkeeper</div>
                    <div class="text-[10px] text-blue-300">Community Hub</div>
                </div>
            </button>
            <button onclick="window.selectContributor('cook')" class="contrib-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">👩‍🍳</span>
                <div>
                    <div class="text-xs font-bold text-white">Home Cook</div>
                    <div class="text-[10px] text-rose-300">Nourishing Meals</div>
                </div>
            </button>
            <button onclick="window.selectContributor('rain')" class="contrib-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">🌧️</span>
                <div>
                    <div class="text-xs font-bold text-white">Monsoon Rain</div>
                    <div class="text-[10px] text-sky-300">Fresh Hydration</div>
                </div>
            </button>
            <button onclick="window.selectContributor('soil')" class="contrib-btn p-2.5 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all text-left flex items-center gap-2">
                <span class="text-2xl">🌱</span>
                <div>
                    <div class="text-xs font-bold text-white">Mother Soil</div>
                    <div class="text-[10px] text-amber-500">Mineral Bed</div>
                </div>
            </button>
        </div>

        <div id="contribDetailBox" class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 space-y-2">
            <div class="flex items-center gap-2">
                <span id="contribIcon" class="text-3xl">☀️</span>
                <div>
                    <h5 id="contribTitle" class="text-sm font-bold text-amber-300">Solar Energy & Radiance</h5>
                    <span id="contribRole" class="text-[11px] text-slate-400">Primary Natural Contributor (Abiotic Power)</span>
                </div>
            </div>
            <p id="contribDesc" class="text-xs text-slate-300 leading-relaxed">
                Sunlight provides the vital radiant photons that chlorophyll molecules inside green leaves capture to split water and convert carbon dioxide into rich carbohydrates through photosynthesis.
            </p>
            <div class="flex flex-wrap gap-2 pt-1 text-[11px]">
                <span class="bg-amber-950/60 text-amber-300 px-2.5 py-1 rounded border border-amber-800/50" id="contribImpact">Impact: Fuels 100% of global plant biomass</span>
                <span class="bg-slate-800 text-slate-300 px-2.5 py-1 rounded" id="contribGratitude">Gratitude: Honored during Makar Sankranti & Chhath Puja</span>
            </div>
        </div>
    </div>
"""

# SIM 3: Gratitude Letter Workshop
simulators_part1["sim-3"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-rose-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-rose-300">Harvest Gratitude Workshop</h4>
            </div>
            <span class="text-xs bg-rose-500/20 text-rose-300 px-2.5 py-1 rounded-full font-medium border border-rose-500/30">Activity 3: Express Thanks</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="space-y-3">
                <label class="block text-xs font-semibold text-slate-300">1. Select Recipient to Thank:</label>
                <div class="grid grid-cols-2 gap-2">
                    <button onclick="window.setGratitudeRecipient('Farmer', '🌾')" class="grat-recip-btn active p-2 rounded-lg bg-rose-950/40 border border-rose-500/50 text-left text-xs font-medium flex items-center gap-2">
                        <span>🌾</span> Hardworking Farmer
                    </button>
                    <button onclick="window.setGratitudeRecipient('Earthworm', '🪱')" class="grat-recip-btn p-2 rounded-lg bg-slate-800/60 border border-slate-700 text-left text-xs font-medium flex items-center gap-2">
                        <span>🪱</span> Humble Earthworm
                    </button>
                    <button onclick="window.setGratitudeRecipient('Mother Nature', '🌍')" class="grat-recip-btn p-2 rounded-lg bg-slate-800/60 border border-slate-700 text-left text-xs font-medium flex items-center gap-2">
                        <span>🌍</span> Mother Nature & Sun
                    </button>
                    <button onclick="window.setGratitudeRecipient('Family Cook', '🍲')" class="grat-recip-btn p-2 rounded-lg bg-slate-800/60 border border-slate-700 text-left text-xs font-medium flex items-center gap-2">
                        <span>🍲</span> Loving Family Cook
                    </button>
                </div>

                <label class="block text-xs font-semibold text-slate-300">2. Select Your Heartfelt Sentiment:</label>
                <select id="gratitudeSentiment" onchange="window.updateGratitudeLetter()" class="w-full bg-slate-800 border border-slate-700 rounded-lg p-2 text-xs text-slate-200 focus:outline-none focus:border-rose-500">
                    <option value="toil">Thank you for toiling under hot sun and cold rains to feed our families.</option>
                    <option value="soil">Thank you for quietly aerating the soil and making the earth fertile.</option>
                    <option value="nourish">Thank you for transforming raw ingredients into warm, nourishing meals with love.</option>
                    <option value="sunshine">Thank you for radiant sunshine and monsoon rains that bring crops to life.</option>
                </select>

                <button onclick="window.dispatchGratitude()" class="w-full py-2.5 rounded-xl bg-gradient-to-r from-rose-600 to-pink-600 text-white font-semibold text-xs shadow-lg shadow-rose-950/50 hover:from-rose-500 hover:to-pink-500 transition-all flex items-center justify-center gap-2">
                    <span>💌</span> Seal & Send Gratitude Card
                </button>
            </div>

            <div class="relative bg-amber-50/95 text-slate-900 rounded-xl p-4 shadow-xl border-2 border-amber-300 flex flex-col justify-between font-serif">
                <div class="border-b border-amber-200 pb-2 flex items-center justify-between">
                    <span class="text-xs font-bold uppercase tracking-wider text-amber-900">Official Gratitude Certificate</span>
                    <span id="cardIcon" class="text-2xl">🌾</span>
                </div>
                <div class="my-3 space-y-2 text-xs leading-relaxed">
                    <p class="font-bold text-amber-950" id="letterTo">Dearest Hardworking Farmer,</p>
                    <p class="italic text-slate-800" id="letterBody">"Thank you for toiling under hot sun and cold rains to feed our families every single day. Every grain on our plate represents your unwavering dedication."</p>
                    <p class="text-right text-[11px] font-semibold text-amber-900">— From a Mindful, Grateful Class 4 Student</p>
                </div>
                <div class="flex items-center justify-between pt-2 border-t border-amber-200 text-[10px] text-amber-800">
                    <span>NEP 2020 Curiosity Class 4</span>
                    <span id="stampStatus" class="font-bold text-rose-600 uppercase tracking-widest bg-rose-100 px-2 py-0.5 rounded border border-rose-300">★ Ready to Seal</span>
                </div>
            </div>
        </div>
    </div>
"""

# SIM 4: Pan-Indian Harvest Festival Explorer
simulators_part1["sim-4"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-cyan-300">Pan-Indian Harvest Festival Explorer</h4>
            </div>
            <span class="text-xs bg-cyan-500/20 text-cyan-300 px-2.5 py-1 rounded-full font-medium border border-cyan-500/30">Regional Celebrations</span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2">
            <button onclick="window.selectFestival('sankranti')" class="fest-btn active p-2 rounded-xl border border-cyan-500/50 bg-cyan-950/40 text-center hover:bg-cyan-900/50 transition-all flex flex-col items-center gap-1">
                <span class="text-xl">🪁</span>
                <span class="text-xs font-bold text-white">Makar Sankranti</span>
                <span class="text-[10px] text-cyan-300">Pan-India</span>
            </button>
            <button onclick="window.selectFestival('onam')" class="fest-btn p-2 rounded-xl border border-slate-700 bg-slate-800/50 text-center hover:bg-slate-800 transition-all flex flex-col items-center gap-1">
                <span class="text-xl">🛶</span>
                <span class="text-xs font-bold text-white">Onam</span>
                <span class="text-[10px] text-emerald-300">Kerala</span>
            </button>
            <button onclick="window.selectFestival('lohri')" class="fest-btn p-2 rounded-xl border border-slate-700 bg-slate-800/50 text-center hover:bg-slate-800 transition-all flex flex-col items-center gap-1">
                <span class="text-xl">🔥</span>
                <span class="text-xs font-bold text-white">Lohri</span>
                <span class="text-[10px] text-amber-300">Punjab</span>
            </button>
            <button onclick="window.selectFestival('raja')" class="fest-btn p-2 rounded-xl border border-slate-700 bg-slate-800/50 text-center hover:bg-slate-800 transition-all flex flex-col items-center gap-1">
                <span class="text-xl">🪘</span>
                <span class="text-xs font-bold text-white">Raja Utsav</span>
                <span class="text-[10px] text-rose-300">Odisha</span>
            </button>
            <button onclick="window.selectFestival('akshaya')" class="fest-btn p-2 rounded-xl border border-slate-700 bg-slate-800/50 text-center hover:bg-slate-800 transition-all flex flex-col items-center gap-1">
                <span class="text-xl">🪙</span>
                <span class="text-xs font-bold text-white">Akshay Tritya</span>
                <span class="text-[10px] text-yellow-300">National</span>
            </button>
            <button onclick="window.selectFestival('bihu')" class="fest-btn p-2 rounded-xl border border-slate-700 bg-slate-800/50 text-center hover:bg-slate-800 transition-all flex flex-col items-center gap-1">
                <span class="text-xl">🥁</span>
                <span class="text-xs font-bold text-white">Magh Bihu</span>
                <span class="text-[10px] text-purple-300">Assam</span>
            </button>
        </div>

        <div id="festInfoCard" class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="space-y-1">
                <div class="flex items-center gap-2">
                    <span id="festIcon" class="text-3xl">🪁</span>
                    <div>
                        <h5 id="festName" class="text-sm font-bold text-cyan-300">Makar Sankranti</h5>
                        <span id="festRegion" class="text-xs text-slate-400">Celebrated Pan-India (January 14/15)</span>
                    </div>
                </div>
                <div class="pt-2 text-xs text-slate-300 leading-relaxed" id="festSignificance">
                    Celebrates the sun entering Makara (Capricorn) and honors the first winter harvest of sesame, jaggery, sugarcane, and fresh rice.
                </div>
            </div>

            <div class="space-y-2 border-t md:border-t-0 md:border-l border-slate-800 pt-3 md:pt-0 md:pl-4">
                <span class="text-xs font-bold text-amber-300 block">Traditional Harvest Foods:</span>
                <p id="festFoods" class="text-xs text-slate-300">Til-gur laddus, khichdi, rewri, sugarcane chunks, fresh roasted peanut chikki.</p>
                <span class="text-xs font-bold text-emerald-300 block pt-1">Cultural Ritual:</span>
                <p id="festRitual" class="text-xs text-slate-300">Flying colorful kites to absorb healthy winter vitamin D from the sun and singing thanksgiving folk tunes.</p>
            </div>

            <div class="bg-slate-900 rounded-lg p-3 border border-slate-800 flex flex-col justify-between">
                <div>
                    <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Eco-Lesson</span>
                    <p id="festEcoLesson" class="text-xs text-cyan-200 mt-1">Honoring solar energy that nurtured the crops through winter months.</p>
                </div>
                <div class="mt-2 text-[10px] bg-cyan-950/60 text-cyan-300 p-1.5 rounded border border-cyan-800/40" id="festTag">
                    Key Value: Community sharing of newly harvested grains
                </div>
            </div>
        </div>
    </div>
"""

# SIM 5: Peanut Sensory Awareness Chamber
simulators_part1["sim-5"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-yellow-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-yellow-300">Peanut 5-Senses Laboratory</h4>
            </div>
            <span class="text-xs bg-yellow-500/20 text-yellow-300 px-2.5 py-1 rounded-full font-medium border border-yellow-500/30">Mindful Sensory Protocol</span>
        </div>

        <div class="grid grid-cols-5 gap-2 text-center">
            <button onclick="window.inspectSense('touch')" class="sense-btn active p-2 rounded-xl border border-yellow-500/50 bg-yellow-950/40 hover:bg-yellow-900/50 transition-all flex flex-col items-center gap-1">
                <span class="text-2xl">🖐️</span>
                <span class="text-xs font-semibold">Touch</span>
            </button>
            <button onclick="window.inspectSense('sight')" class="sense-btn p-2 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all flex flex-col items-center gap-1">
                <span class="text-2xl">👁️</span>
                <span class="text-xs font-semibold">Sight</span>
            </button>
            <button onclick="window.inspectSense('smell')" class="sense-btn p-2 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all flex flex-col items-center gap-1">
                <span class="text-2xl">👃</span>
                <span class="text-xs font-semibold">Smell</span>
            </button>
            <button onclick="window.inspectSense('sound')" class="sense-btn p-2 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all flex flex-col items-center gap-1">
                <span class="text-2xl">👂</span>
                <span class="text-xs font-semibold">Sound</span>
            </button>
            <button onclick="window.inspectSense('taste')" class="sense-btn p-2 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-800 transition-all flex flex-col items-center gap-1">
                <span class="text-2xl">👅</span>
                <span class="text-xs font-semibold">Taste</span>
            </button>
        </div>

        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col sm:flex-row items-center gap-4">
            <div class="w-24 h-24 rounded-2xl bg-amber-950/40 border border-amber-600/40 flex items-center justify-center text-5xl shrink-0 shadow-lg" id="senseVisual">
                🥜
            </div>
            <div class="flex-1 space-y-2 text-center sm:text-left">
                <div class="flex items-center gap-2 justify-center sm:justify-start">
                    <span id="senseBadge" class="text-xs font-bold uppercase tracking-wider text-yellow-400 bg-yellow-950 px-2 py-0.5 rounded">Sense 1: Tactile Touch</span>
                    <h5 id="senseTitle" class="text-sm font-bold text-white">Feel the Ridged Shell & Smooth Seed</h5>
                </div>
                <p id="senseDetail" class="text-xs text-slate-300 leading-relaxed">
                    Roll the peanut gently between your fingertips. Notice the hard fibrous outer pod with its rough textured ridges, followed by the silky smooth red skin protecting the twin seed halves inside.
                </p>
                <div class="flex flex-wrap gap-2 pt-1 justify-center sm:justify-start text-[11px]">
                    <span class="bg-slate-800 text-slate-300 px-2 py-0.5 rounded" id="senseReceptor">Receptor: Mechanoreceptors in fingertip skin</span>
                    <span class="bg-yellow-900/40 text-yellow-300 px-2 py-0.5 rounded border border-yellow-700/50" id="senseMindfulness">Mindful Insight: Physical touch grounds focus in the present moment</span>
                </div>
            </div>
        </div>
    </div>
"""

# SIM 6: Salivary Mastication Engine
simulators_part1["sim-6"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-blue-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-blue-300">Salivary Mastication & Starch Breakdown Engine</h4>
            </div>
            <span class="text-xs bg-blue-500/20 text-blue-300 px-2.5 py-1 rounded-full font-medium border border-blue-500/30">Chewing Physics & Chemistry</span>
        </div>

        <div class="space-y-3">
            <div class="flex items-center justify-between">
                <label for="chewSlider" class="text-xs font-bold text-slate-300 flex items-center gap-2">
                    <span>🦷 Chew Count Meter:</span>
                    <span id="chewCountVal" class="text-emerald-400 text-base font-extrabold bg-slate-800 px-2.5 py-0.5 rounded border border-slate-700">10 Chews</span>
                </label>
                <span id="chewTargetStatus" class="text-xs font-semibold text-amber-400">Target: 32 Chews for Smooth Bolus</span>
            </div>
            <input type="range" id="chewSlider" min="1" max="35" value="10" oninput="window.updateChewSim(this.value)" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-blue-500">
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 space-y-1">
                <span class="text-[11px] text-slate-400 uppercase font-semibold">Particle Size & Texture</span>
                <div class="text-sm font-bold text-white flex items-center gap-2" id="chewTexture">
                    <span>🥖</span> Coarse Grain Chunks
                </div>
                <p class="text-[11px] text-slate-400" id="chewTextureDesc">Food particles remain large, requiring high stomach acid workload.</p>
            </div>

            <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 space-y-1">
                <span class="text-[11px] text-slate-400 uppercase font-semibold">Salivary Amylase Reaction</span>
                <div class="text-sm font-bold text-cyan-300 flex items-center gap-2" id="chewSugarStatus">
                    <span>🧪</span> Partial Hydrolysis
                </div>
                <p class="text-[11px] text-slate-400" id="chewSugarDesc">Some starch converted to maltose; mild sweetness emerging.</p>
            </div>

            <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 space-y-1">
                <span class="text-[11px] text-slate-400 uppercase font-semibold">Stomach Digestion Ease</span>
                <div class="text-sm font-bold text-amber-300 flex items-center gap-2" id="chewEaseStatus">
                    <span>⚠️</span> Moderate Strain
                </div>
                <p class="text-[11px] text-slate-400" id="chewEaseDesc">Gastric juices need 40% more churning energy.</p>
            </div>
        </div>

        <div class="bg-slate-950 rounded-lg p-2.5 border border-slate-800 flex items-center justify-between text-xs">
            <span class="text-slate-300">Scientific rule: Chew your liquids, drink your solids.</span>
            <button onclick="window.setChewsTo32()" class="px-2.5 py-1 rounded bg-blue-600 hover:bg-blue-500 text-white font-medium transition-all">Set to Ideal 32 Chews</button>
        </div>
    </div>
"""

# SIM 7: Food Waste & Resource Impact Calculator
simulators_part1["sim-7"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-emerald-300">Food Waste & Virtual Resource Footprint</h4>
            </div>
            <span class="text-xs bg-emerald-500/20 text-emerald-300 px-2.5 py-1 rounded-full font-medium border border-emerald-500/30">Ecological Economics</span>
        </div>

        <div class="space-y-3">
            <div class="flex items-center justify-between">
                <label for="wasteSlider" class="text-xs font-bold text-slate-300 flex items-center gap-2">
                    <span>🗑️ Wasted Food Quantity:</span>
                    <span id="wasteQuantityVal" class="text-rose-400 text-base font-extrabold bg-slate-800 px-2.5 py-0.5 rounded border border-slate-700">2 Chapatis / 1 Bowl Rice</span>
                </label>
                <span class="text-xs text-slate-400">Slide to see lost resources</span>
            </div>
            <input type="range" id="wasteSlider" min="1" max="10" value="2" oninput="window.updateWasteSim(this.value)" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-rose-500">
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 flex items-center gap-3">
                <span class="text-3xl">💧</span>
                <div>
                    <span class="text-[11px] text-slate-400 block font-semibold">Virtual Water Squandered</span>
                    <span id="lostWaterVal" class="text-base font-extrabold text-sky-400">300 Litres</span>
                    <span class="text-[10px] text-slate-400 block">Equals 2 full bathtubs of pure water</span>
                </div>
            </div>

            <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 flex items-center gap-3">
                <span class="text-3xl">🚜</span>
                <div>
                    <span class="text-[11px] text-slate-400 block font-semibold">Diesel Fuel & Tractor Power</span>
                    <span id="lostDieselVal" class="text-base font-extrabold text-amber-400">120 Millilitres</span>
                    <span class="text-[10px] text-slate-400 block">Carbon emission: 320g CO2</span>
                </div>
            </div>

            <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 flex items-center gap-3">
                <span class="text-3xl">⏳</span>
                <div>
                    <span class="text-[11px] text-slate-400 block font-semibold">Farmer Working Hours</span>
                    <span id="lostLaborVal" class="text-base font-extrabold text-emerald-400">45 Minutes</span>
                    <span class="text-[10px] text-slate-400 block">Hard manual tilling and weeding lost</span>
                </div>
            </div>
        </div>

        <div class="bg-emerald-950/30 rounded-xl p-3 border border-emerald-800/40 flex items-center justify-between text-xs">
            <div class="flex items-center gap-2">
                <span class="text-emerald-400 text-lg">💡</span>
                <span class="text-slate-200">Zero-Waste Rule: Take small initial portions. Only take second helpings if still hungry!</span>
            </div>
            <button onclick="window.zeroWasteCommitment()" class="px-2.5 py-1 rounded bg-emerald-600 hover:bg-emerald-500 text-white font-medium shrink-0 ml-2">Commit to Clean Plate</button>
        </div>
    </div>
"""

# SIM 8: Mindful Meal Pacing Log & Weekly Diary
simulators_part1["sim-8"] = """
    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 text-slate-100 flex flex-col gap-4">
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
            <div class="flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-indigo-400 animate-pulse"></span>
                <h4 class="font-bold text-base text-indigo-300">Weekly Mindful Food Diary & Habit Tracker</h4>
            </div>
            <span class="text-xs bg-indigo-500/20 text-indigo-300 px-2.5 py-1 rounded-full font-medium border border-indigo-500/30">7-Day Reflection</span>
        </div>

        <div class="flex items-center justify-between gap-1 overflow-x-auto pb-1">
            <button onclick="window.selectDiaryDay('Mon')" class="diary-day-btn active px-3 py-1.5 rounded-lg border border-indigo-500/50 bg-indigo-950/40 text-xs font-semibold text-white">Mon</button>
            <button onclick="window.selectDiaryDay('Tue')" class="diary-day-btn px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800/50 text-xs font-semibold text-slate-300">Tue</button>
            <button onclick="window.selectDiaryDay('Wed')" class="diary-day-btn px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800/50 text-xs font-semibold text-slate-300">Wed</button>
            <button onclick="window.selectDiaryDay('Thu')" class="diary-day-btn px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800/50 text-xs font-semibold text-slate-300">Thu</button>
            <button onclick="window.selectDiaryDay('Fri')" class="diary-day-btn px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800/50 text-xs font-semibold text-slate-300">Fri</button>
            <button onclick="window.selectDiaryDay('Sat')" class="diary-day-btn px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800/50 text-xs font-semibold text-slate-300">Sat</button>
            <button onclick="window.selectDiaryDay('Sun')" class="diary-day-btn px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800/50 text-xs font-semibold text-slate-300">Sun</button>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-4 gap-3 bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <div class="space-y-1">
                <span class="text-[11px] text-slate-400 font-semibold uppercase">Chewing Pacing</span>
                <div class="text-sm font-bold text-emerald-400 flex items-center gap-1.5" id="diaryChew">
                    <span>⏱️</span> 28 Chews / bite
                </div>
                <span class="text-[10px] text-slate-400">Paced & unhurried</span>
            </div>

            <div class="space-y-1">
                <span class="text-[11px] text-slate-400 font-semibold uppercase">Rainbow Foods</span>
                <div class="text-sm font-bold text-amber-300 flex items-center gap-1.5" id="diaryColors">
                    <span>🥗</span> 4 Natural Colors
                </div>
                <span class="text-[10px] text-slate-400">Green, orange, yellow, white</span>
            </div>

            <div class="space-y-1">
                <span class="text-[11px] text-slate-400 font-semibold uppercase">Zero-Waste Status</span>
                <div class="text-sm font-bold text-cyan-300 flex items-center gap-1.5" id="diaryClean">
                    <span>✨</span> 100% Clean Plate
                </div>
                <span class="text-[10px] text-slate-400">Zero food discarded</span>
            </div>

            <div class="space-y-1">
                <span class="text-[11px] text-slate-400 font-semibold uppercase">Gratitude Feeling</span>
                <div class="text-sm font-bold text-pink-300 flex items-center gap-1.5" id="diaryGrat">
                    <span>🙏</span> Deeply Grateful
                </div>
                <span class="text-[10px] text-slate-400">Paused to thank nature</span>
            </div>
        </div>

        <div class="flex items-center justify-between text-xs text-slate-400">
            <span>Weekly Habit Score: <strong class="text-emerald-400" id="diaryScore">94% Excellent</strong></span>
            <button onclick="window.logTodayMeal()" class="px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-medium transition-all">+ Log Current Meal Check</button>
        </div>
    </div>
"""

print(f"Part 1 simulators written: {len(simulators_part1)}")

