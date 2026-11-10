# -*- coding: utf-8 -*-
"""
Interactive Simulators for Slides 9 to 16
Class 3 Mathematics Chapter 1: What's in a Name?
Bespoke SVG/HTML5 interactive laboratory widgets.
"""

simulators_part2 = {
    # Simulator 9: Extreme Place Names
    "sim_extreme_names_map": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">India's Extreme Place Names Map</h3>
                <p class="text-xs text-slate-400">Select railway towns across India to compare character lengths from 2 letters to 28 letters.</p>
            </div>
            <div class="flex gap-1.5 flex-wrap">
                <button onclick="selectExtremePlace('longest')" id="btnPlaceLong" class="px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition">Longest Name (28 Letters)</button>
                <button onclick="selectExtremePlace('shortest_ib')" id="btnPlaceIb" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">Shortest: Ib (2 Letters)</button>
                <button onclick="selectExtremePlace('shortest_od')" id="btnPlaceOd" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">Shortest: Od (2 Letters)</button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- India Geographic Map Display -->
            <div class="md:col-span-7 bg-slate-950 rounded-xl p-3 border border-slate-800 relative min-h-[220px] flex items-center justify-center">
                <svg viewBox="0 0 360 220" class="w-full h-auto">
                    <!-- India Outline Path (Stylized) -->
                    <path d="M 140,20 L 190,40 L 220,70 L 290,75 L 310,100 L 270,110 L 230,110 L 220,150 L 180,200 L 160,210 L 150,170 L 110,130 L 90,100 L 110,60 Z" fill="#1e293b" stroke="#334155" stroke-width="2"/>
                    
                    <!-- Location Markers -->
                    <!-- Venkatanarasimharajuvaripeta (Andhra Pradesh) -->
                    <circle id="markerVenkata" cx="170" cy="180" r="7" fill="#f59e0b" class="animate-pulse"/>
                    <text x="180" y="184" fill="#fbbf24" font-size="9" font-weight="bold">Andhra Pradesh (28)</text>

                    <!-- Ib (Odisha) -->
                    <circle id="markerIb" cx="215" cy="120" r="5" fill="#38bdf8"/>
                    <text x="225" y="123" fill="#38bdf8" font-size="9" font-weight="bold">Ib, Odisha (2)</text>

                    <!-- Od (Gujarat) -->
                    <circle id="markerOd" cx="115" cy="115" r="5" fill="#34d399"/>
                    <text x="75" y="118" fill="#34d399" font-size="9" font-weight="bold">Od, Gujarat (2)</text>
                </svg>
            </div>

            <!-- Place Details & Subtraction Card -->
            <div class="md:col-span-5 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-2.5 text-xs">
                <div class="border-b border-slate-800 pb-2">
                    <span class="text-slate-400 block text-[11px]">Selected Station Name:</span>
                    <b id="placeNameDisplay" class="text-amber-300 text-sm font-bold break-all">Venkatanarasimharajuvaripeta</b>
                </div>
                <div class="flex justify-between items-center p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400">Total Letters:</span>
                    <b id="placeLetterCount" class="text-white text-sm font-bold">28 Letters</b>
                </div>
                <div class="p-2.5 rounded bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
                    <span class="text-cyan-400 font-bold block mb-1">Difference Calculation:</span>
                    <span id="placeDiffCalculation">28 letters (Andhra Pradesh) - 2 letters (Ib/Od) = <b>26 letters difference!</b></span>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 10: Number Word Riddles
    "sim_number_word_riddles": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Number Detective: Linguistic & Arithmetic Riddle Solver</h3>
                <p class="text-xs text-slate-400">Riddle: 2-digit number, two 5-letter words, digits add up to 7. Test candidate numbers!</p>
            </div>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
            <button onclick="testRiddleCandidate(43, 'FORTY THREE', 5, 5, 7)" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 text-left transition space-y-1">
                <div class="text-base font-bold text-white">43</div>
                <div class="text-[11px] text-cyan-300">"FORTY THREE"</div>
            </button>
            <button onclick="testRiddleCandidate(52, 'FIFTY TWO', 5, 3, 7)" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 text-left transition space-y-1">
                <div class="text-base font-bold text-white">52</div>
                <div class="text-[11px] text-slate-400">"FIFTY TWO"</div>
            </button>
            <button onclick="testRiddleCandidate(34, 'THIRTY FOUR', 6, 4, 7)" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 text-left transition space-y-1">
                <div class="text-base font-bold text-white">34</div>
                <div class="text-[11px] text-slate-400">"THIRTY FOUR"</div>
            </button>
            <button onclick="testRiddleCandidate(25, 'TWENTY FIVE', 6, 4, 7)" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 text-left transition space-y-1">
                <div class="text-base font-bold text-white">25</div>
                <div class="text-[11px] text-slate-400">"TWENTY FIVE"</div>
            </button>
        </div>

        <!-- Verification Checklist -->
        <div id="riddleVerificationCard" class="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-2 text-xs">
            <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                <span class="font-bold text-cyan-300">Candidate Evaluation: <span id="riddleCandName" class="text-white">43 ("FORTY THREE")</span></span>
                <span id="riddleStatusTag" class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold">✅ Solves All Clues!</span>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-[11px]">
                <div class="p-2 rounded bg-slate-900 border border-slate-800"><span class="text-slate-400">Word 1:</span> <b id="riddleW1" class="text-white">FORTY (5 letters) ✅</b></div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800"><span class="text-slate-400">Word 2:</span> <b id="riddleW2" class="text-white">THREE (5 letters) ✅</b></div>
                <div class="p-2 rounded bg-slate-900 border border-slate-800"><span class="text-slate-400">Digit Sum:</span> <b id="riddleSum" class="text-emerald-400">4 + 3 = 7 ✅</b></div>
            </div>
        </div>
    </div>
    """,

    # Simulator 11: Proximity To Hundred
    "sim_hundred_proximity_line": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Number Line Symmetry: Proximity to 100</h3>
                <p class="text-xs text-slate-400">Adjust the step distance from 100 to reveal symmetrical paired numbers on the number line.</p>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400">Distance: <b id="distSliderVal" class="text-amber-300 text-sm">4 Units</b></span>
                <input type="range" id="proximityRange" min="1" max="15" value="4" oninput="updateProximityDistance(this.value)" class="w-28 sm:w-36 accent-amber-500">
            </div>
        </div>

        <div class="bg-slate-950 rounded-xl p-5 border border-slate-800 flex flex-col items-center justify-center space-y-4 min-h-[190px]">
            <!-- Symmetrical Number Line SVG -->
            <svg viewBox="0 0 500 130" class="w-full h-auto">
                <!-- Base Axis -->
                <line x1="30" y1="70" x2="470" y2="70" stroke="#475569" stroke-width="3"/>

                <!-- Benchmark 100 Center -->
                <circle cx="250" cy="70" r="8" fill="#f59e0b"/>
                <line x1="250" y1="50" x2="250" y2="90" stroke="#f59e0b" stroke-width="2"/>
                <text x="250" y="40" fill="#f59e0b" font-size="14" font-weight="bold" text-anchor="middle">100</text>

                <!-- Left Point (100 - d) -->
                <circle id="proxLeftCircle" cx="190" cy="70" r="7" fill="#38bdf8"/>
                <text id="proxLeftText" x="190" y="105" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">96</text>
                <!-- Arc Left -->
                <path id="proxLeftArc" d="M 250,70 Q 220,30 190,70" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>

                <!-- Right Point (100 + d) -->
                <circle id="proxRightCircle" cx="310" cy="70" r="7" fill="#34d399"/>
                <text id="proxRightText" x="310" y="105" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">104</text>
                <!-- Arc Right -->
                <path id="proxRightArc" d="M 250,70 Q 280,30 310,70" fill="none" stroke="#34d399" stroke-width="2" stroke-dasharray="4,3"/>
            </svg>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
            <div class="p-3 rounded-lg bg-slate-950 border border-slate-800 flex justify-between items-center">
                <span class="text-slate-400">Step Backward:</span>
                <span id="proxEqLeft" class="font-bold text-cyan-300">100 - 4 = 96</span>
            </div>
            <div class="p-3 rounded-lg bg-slate-950 border border-slate-800 flex justify-between items-center">
                <span class="text-slate-400">Step Forward:</span>
                <span id="proxEqRight" class="font-bold text-emerald-400">100 + 4 = 104</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 12: Living Things Classification
    "sim_living_eats_sorter": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-emerald-300">Biological Classification: "Things That Eat Food"</h3>
                <p class="text-xs text-slate-400">Filter cards to separate living organisms that consume food from non-living artifacts.</p>
            </div>
            <div class="flex gap-1.5 flex-wrap">
                <button onclick="filterLivingCards('all')" id="btnLivAll" class="px-2.5 py-1 text-xs rounded-lg bg-emerald-600 text-white font-bold transition">All 8 Cards</button>
                <button onclick="filterLivingCards('living')" id="btnLivEat" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">Eats Food (Living)</button>
                <button onclick="filterLivingCards('nonliving')" id="btnLivNo" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">Does Not Eat (Non-living)</button>
            </div>
        </div>

        <!-- 8 Sorting Cards Grid -->
        <div id="livingCardsGrid" class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
            <!-- Cards rendered by JS -->
        </div>

        <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs flex justify-between items-center">
            <span id="livingCategorySummary" class="text-slate-300">Displaying all 8 items categorized by biological nourishment.</span>
            <span id="livingCategoryBadge" class="px-2.5 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold shrink-0">8 Items</span>
        </div>
    </div>
    """,

    # Simulator 13: Electric Appliance Sorting
    "sim_electric_manual_sorter": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Household Appliance Sorting: Electric vs Manual</h3>
                <p class="text-xs text-slate-400">Classify home items based on whether they require electrical power or manual muscle force.</p>
            </div>
            <div class="flex gap-1.5 flex-wrap">
                <button onclick="filterApplianceCards('all')" id="btnAppAll" class="px-2.5 py-1 text-xs rounded-lg bg-cyan-600 text-white font-bold transition">All 8 Tools</button>
                <button onclick="filterApplianceCards('electric')" id="btnAppElec" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">⚡ Electric Appliances</button>
                <button onclick="filterApplianceCards('manual')" id="btnAppMan" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">🛠️ Manual Tools</button>
            </div>
        </div>

        <!-- 8 Appliance Cards Grid -->
        <div id="applianceCardsGrid" class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
            <!-- Injected by JS -->
        </div>

        <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs flex justify-between items-center">
            <span id="applianceSummaryText" class="text-slate-300">Showing all 8 household tools categorized by operating energy.</span>
            <span id="applianceBadgeText" class="px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 font-bold shrink-0">8 Items</span>
        </div>
    </div>
    """,

    # Simulator 14: Hairstyle Data Collection
    "sim_hairstyle_collector": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Live Classroom Hairstyle Survey Tracker</h3>
                <p class="text-xs text-slate-400">Click a hairstyle avatar to record an observational tally mark in the classroom survey log.</p>
            </div>
            <button onclick="resetHairstyleSurvey()" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">
                🔄 Clear Survey
            </button>
        </div>

        <!-- Avatar Survey Clickers -->
        <div class="grid grid-cols-2 sm:grid-cols-5 gap-2.5">
            <button onclick="recordHairstyleVote('ponytails')" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 hover:border-amber-400 text-center transition space-y-1">
                <span class="text-2xl">👧</span>
                <div class="text-xs font-bold text-white">Two Ponytails</div>
                <div id="countPonytails" class="text-[11px] font-bold text-amber-300">0 Recorded</div>
            </button>
            <button onclick="recordHairstyleVote('single_pony')" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 hover:border-amber-400 text-center transition space-y-1">
                <span class="text-2xl">👱‍♀️</span>
                <div class="text-xs font-bold text-white">Single Ponytail</div>
                <div id="countSinglePony" class="text-[11px] font-bold text-amber-300">0 Recorded</div>
            </button>
            <button onclick="recordHairstyleVote('braids')" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 hover:border-amber-400 text-center transition space-y-1">
                <span class="text-2xl">🧕</span>
                <div class="text-xs font-bold text-white">Braided Hair</div>
                <div id="countBraids" class="text-[11px] font-bold text-amber-300">0 Recorded</div>
            </button>
            <button onclick="recordHairstyleVote('short')" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 hover:border-amber-400 text-center transition space-y-1">
                <span class="text-2xl">👦</span>
                <div class="text-xs font-bold text-white">Short Hair</div>
                <div id="countShort" class="text-[11px] font-bold text-amber-300">0 Recorded</div>
            </button>
            <button onclick="recordHairstyleVote('curls')" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 hover:border-amber-400 text-center transition space-y-1">
                <span class="text-2xl">🧑‍🦱</span>
                <div class="text-xs font-bold text-white">Curly Hair</div>
                <div id="countCurls" class="text-[11px] font-bold text-amber-300">0 Recorded</div>
            </button>
        </div>

        <!-- Survey Tally Log Box -->
        <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-2 text-xs">
            <span class="text-slate-300">Total Surveyed Classmates: <b id="totalSurveyCount" class="text-white">0 Students</b></span>
            <span class="text-[11px] text-amber-300 italic">Tap any hairstyle to add real-time survey observations.</span>
        </div>
    </div>
    """,

    # Simulator 15: Hairstyle Frequency Table
    "sim_hairstyle_tally_table": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Classroom Hairstyle Frequency Synthesis Table</h3>
                <p class="text-xs text-slate-400">Structured tally bundles and frequency digits summarizing a full survey of 25 students.</p>
            </div>
            <span class="px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 font-bold text-xs">N = 25 Students</span>
        </div>

        <div class="overflow-x-auto">
            <table class="w-full text-left text-xs text-slate-300 border-collapse">
                <thead>
                    <tr class="border-b border-slate-800 text-[11px] text-slate-400 uppercase bg-slate-950">
                        <th class="p-2.5">Hairstyle Category</th>
                        <th class="p-2.5 text-amber-400">Tally Mark Bundles</th>
                        <th class="p-2.5 text-cyan-400">Numerical Frequency</th>
                        <th class="p-2.5 text-emerald-400">Statistical Analysis</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-800/60 font-mono">
                    <tr class="hover:bg-slate-800/40">
                        <td class="p-2.5 font-sans font-bold text-white flex items-center gap-1.5"><span>👦</span> Short Hair</td>
                        <td class="p-2.5 text-amber-300">卌 |||</td>
                        <td class="p-2.5 font-bold text-cyan-300">8</td>
                        <td class="p-2.5 font-sans text-emerald-400 font-semibold">🌟 Statistical Mode (Most Popular)</td>
                    </tr>
                    <tr class="hover:bg-slate-800/40">
                        <td class="p-2.5 font-sans font-bold text-white flex items-center gap-1.5"><span>👧</span> Two Ponytails</td>
                        <td class="p-2.5 text-amber-300">卌 |</td>
                        <td class="p-2.5 font-bold text-cyan-300">6</td>
                        <td class="p-2.5 font-sans text-slate-400">Second Most Frequent</td>
                    </tr>
                    <tr class="hover:bg-slate-800/40">
                        <td class="p-2.5 font-sans font-bold text-white flex items-center gap-1.5"><span>🧕</span> Braids</td>
                        <td class="p-2.5 text-amber-300">卌</td>
                        <td class="p-2.5 font-bold text-cyan-300">5</td>
                        <td class="p-2.5 font-sans text-slate-400">Exactly One 5-Bundle</td>
                    </tr>
                    <tr class="hover:bg-slate-800/40">
                        <td class="p-2.5 font-sans font-bold text-white flex items-center gap-1.5"><span>👱‍♀️</span> Single Ponytail</td>
                        <td class="p-2.5 text-amber-300">||||</td>
                        <td class="p-2.5 font-bold text-cyan-300">4</td>
                        <td class="p-2.5 font-sans text-slate-400">Four Loose Vertical Strokes</td>
                    </tr>
                    <tr class="hover:bg-slate-800/40">
                        <td class="p-2.5 font-sans font-bold text-white flex items-center gap-1.5"><span>🧑‍🦱</span> Curly Hair</td>
                        <td class="p-2.5 text-amber-300">||</td>
                        <td class="p-2.5 font-bold text-cyan-300">2</td>
                        <td class="p-2.5 font-sans text-rose-400 font-semibold">Least Frequent Style</td>
                    </tr>
                </tbody>
                <tfoot>
                    <tr class="bg-slate-950 font-bold border-t-2 border-slate-800 text-xs">
                        <td class="p-2.5 text-amber-400 font-sans">Total Survey Sample</td>
                        <td class="p-2.5 text-amber-300 font-mono">4 Bundles + 5 Loose</td>
                        <td class="p-2.5 text-emerald-400 text-sm">25</td>
                        <td class="p-2.5 text-slate-400 font-sans">100% of Class Accounted For</td>
                    </tr>
                </tfoot>
            </table>
        </div>
    </div>
    """,

    # Simulator 16: Pictograph Data Displays
    "sim_pictograph_chart_builder": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Visual Pictograph Chart Generator</h3>
                <p class="text-xs text-slate-400">Toggle pictograph scale key to see visual icon representation of the classroom survey.</p>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400">Key:</span>
                <select id="pictoScaleSelect" onchange="updatePictographScale(this.value)" class="bg-slate-950 border border-slate-700 text-xs rounded-lg px-2.5 py-1 text-slate-200 outline-none">
                    <option value="1" selected>😊 = 1 Student</option>
                    <option value="2">😊 = 2 Students</option>
                </select>
            </div>
        </div>

        <!-- Pictograph Rows Container -->
        <div id="pictographRowsContainer" class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3 min-h-[220px]">
            <!-- Injected by JS -->
        </div>

        <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs flex justify-between items-center">
            <span id="pictoSummaryText" class="text-slate-300">Key: 1 smiling face (😊) = 1 student. Short hair has the longest row (8 icons).</span>
            <span class="px-2.5 py-1 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 font-bold shrink-0">Visual Data Display</span>
        </div>
    </div>
    """
}

