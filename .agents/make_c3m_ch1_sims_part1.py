# -*- coding: utf-8 -*-
"""
Interactive Simulators for Slides 1 to 8
Class 3 Mathematics Chapter 1: What's in a Name?
Bespoke SVG/HTML5 interactive laboratory widgets.
"""

simulators_part1 = {
    # Simulator 1: Pre-Numerical Counting
    "sim_prenum_cattle": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Ancient One-to-One Correspondence Corral</h3>
                <p class="text-xs text-slate-400">Dispatch cattle to meadow and match each animal with a river pebble in the clay pot.</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="dispatchCowToPasture()" id="btnDispatchCow" class="px-3 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition shadow flex items-center gap-1">
                    <span>🐄 ➔</span> Release Cow
                </button>
                <button onclick="returnCowToCorral()" id="btnReturnCow" class="px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition shadow flex items-center gap-1">
                    <span>⬅ 🏡</span> Return Cow
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Meadow & Corral SVG -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px]">
                <svg viewBox="0 0 500 220" class="w-full h-auto">
                    <!-- Pasture Field -->
                    <rect x="0" y="0" width="320" height="220" fill="#064e3b" opacity="0.3"/>
                    <rect x="320" y="0" width="180" height="220" fill="#78350f" opacity="0.25"/>
                    <line x1="320" y1="0" x2="320" y2="220" stroke="#d97706" stroke-width="3" stroke-dasharray="6,4"/>
                    <text x="140" y="24" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">🌿 Open Pasture Meadow</text>
                    <text x="410" y="24" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">🛖 Village Corral Shed</text>

                    <!-- Cattle Group in Meadow -->
                    <g id="meadowCattleGroup">
                        <!-- Populated by JS -->
                    </g>

                    <!-- Gate Marker -->
                    <rect x="315" y="90" width="10" height="40" fill="#f59e0b" rx="2"/>
                    <text x="320" y="145" fill="#f59e0b" font-size="9" text-anchor="middle">GATE</text>
                </svg>
            </div>

            <!-- Clay Pot Token Box -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
                <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                    <span class="text-xs font-bold text-amber-300">🏺 Cowherd's Clay Pot</span>
                    <span id="pebbleCountBadge" class="text-xs px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30 font-bold">0 Pebbles</span>
                </div>
                <!-- Pebble Display Container -->
                <div id="pebbleJarDisplay" class="h-28 bg-slate-900 rounded-lg border border-slate-800 p-2 flex flex-wrap gap-1.5 content-start overflow-y-auto">
                    <!-- Pebbles inserted here -->
                </div>
                <div class="p-2 rounded-lg bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
                    <p id="correspondenceStatus"> Corral is full. Tap <b>Release Cow</b> to start one-to-one pebble pairing.</p>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 2: Wall Mark Tallying
    "sim_wall_tally": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Clay Wall Scratch Tally Simulator</h3>
                <p class="text-xs text-slate-400">Scratch vertical chalk lines for departing cattle; strike through diagonally as they return.</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="addWallScratch()" class="px-2.5 py-1 text-xs rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold transition">
                    ➕ Scratch Mark
                </button>
                <button onclick="strikeWallScratch()" class="px-2.5 py-1 text-xs rounded-lg bg-orange-600 hover:bg-orange-500 text-white font-bold transition">
                    ❌ Strike Return
                </button>
                <button onclick="resetWallTally()" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">
                    🔄 Reset Wall
                </button>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Clay Wall SVG Display -->
            <div class="md:col-span-8 bg-amber-950/40 rounded-xl p-4 border-2 border-amber-800/60 relative min-h-[220px] flex items-center justify-center">
                <svg id="wallSvgCanvas" viewBox="0 0 450 180" class="w-full h-auto">
                    <!-- Clay Wall Background Texture -->
                    <rect x="0" y="0" width="450" height="180" fill="#451a03" rx="8" opacity="0.6"/>
                    <g id="wallMarksGroup">
                        <!-- Vertical & Struck strokes injected by JS -->
                    </g>
                </svg>
            </div>

            <!-- Tally Status Counters -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-2.5 text-xs">
                <div class="flex justify-between items-center p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400">Out in Pasture:</span>
                    <span id="wallOutCount" class="font-bold text-amber-300 text-sm">0</span>
                </div>
                <div class="flex justify-between items-center p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400">Returned Safely:</span>
                    <span id="wallReturnedCount" class="font-bold text-emerald-400 text-sm">0</span>
                </div>
                <div class="flex justify-between items-center p-2 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400">Uncancelled Marks:</span>
                    <span id="wallUncancelledCount" class="font-bold text-rose-400 text-sm">0</span>
                </div>
                <p id="wallStatusMsg" class="p-2 rounded bg-slate-900/60 text-[11px] text-slate-300 border border-slate-800">
                    Clay wall is blank. Scratch a mark for each departing cow.
                </p>
            </div>
        </div>
    </div>
    """,

    # Simulator 3: Tracking Missing Cattle
    "sim_missing_cattle": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-rose-300">Missing Cattle Alert & Lantern Search Party</h3>
                <p class="text-xs text-slate-400">Identify uncancelled marks, dispatch lanterns to the river bamboo grove, and rescue lost cows.</p>
            </div>
            <button onclick="launchSearchParty()" id="btnSearchParty" class="px-3 py-1.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs transition flex items-center gap-1.5 shadow">
                <span>🏮</span> Dispatch Lantern Search Party
            </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Night Pasture Canvas -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px]">
                <svg viewBox="0 0 500 220" class="w-full h-auto">
                    <!-- Night Background -->
                    <rect x="0" y="0" width="500" height="220" fill="#020617"/>
                    <!-- Moon -->
                    <circle cx="450" cy="35" r="15" fill="#fef08a" opacity="0.8"/>
                    <!-- Bamboo Grove -->
                    <rect x="40" y="100" width="120" height="100" fill="#064e3b" opacity="0.5" rx="10"/>
                    <text x="100" y="125" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">🎋 Bamboo Grove</text>

                    <!-- Lost Cows in Grove (Hidden until search) -->
                    <g id="lostCowsGroup" opacity="0.2">
                        <text x="70" y="165" font-size="28">🐄</text>
                        <text x="110" y="165" font-size="28">🐄</text>
                    </g>

                    <!-- Lantern Beam Effect -->
                    <polygon id="lanternBeamCone" points="360,140 100,120 100,190" fill="#fef08a" opacity="0"/>

                    <!-- Search Party with Lantern -->
                    <g id="searchPartyGroup" transform="translate(350, 130)">
                        <text x="0" y="0" font-size="24">🏮</text>
                    </g>
                </svg>
            </div>

            <!-- Investigation Panel -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3 text-xs">
                <div class="flex items-center justify-between pb-2 border-b border-slate-800">
                    <span class="font-bold text-amber-300">Wall Status:</span>
                    <span class="px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/30 font-bold">2 Uncancelled Marks</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1">
                    <div class="flex justify-between text-slate-400"><span>Departed:</span><b class="text-white">10 cows</b></div>
                    <div class="flex justify-between text-slate-400"><span>Returned:</span><b class="text-emerald-400">8 cows</b></div>
                    <div class="flex justify-between text-slate-400"><span>Discrepancy:</span><b class="text-rose-400">2 cows missing</b></div>
                </div>
                <p id="searchRescueStatus" class="p-2 rounded bg-rose-950/40 border border-rose-800/40 text-[11px] text-rose-200">
                    ⚠️ 2 marks remain uncrossed! Tap the button to launch a search party toward the riverside pasture.
                </p>
            </div>
        </div>
    </div>
    """,

    # Simulator 4: Modern Tally Marks
    "sim_five_bundle_tally": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Modern 5-Bundle Tally Generator</h3>
                <p class="text-xs text-slate-400">Slide to any number from 1 to 30 to see automatic five-bundling and skip-counting breakdown.</p>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400">Number: <b id="tallySliderNum" class="text-cyan-300 text-sm">17</b></span>
                <input type="range" id="tallyRangeInput" min="1" max="30" value="17" oninput="updateTallyBundles(this.value)" class="w-28 sm:w-36 accent-cyan-500">
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <!-- Visual Tally Bundles Container -->
            <div class="md:col-span-8 bg-slate-950 rounded-xl p-4 border border-slate-800 relative min-h-[220px] flex items-center justify-center overflow-x-auto">
                <div id="tallyBundlesGrid" class="flex flex-wrap items-center gap-4 p-2 justify-center">
                    <!-- Bundles injected by JS -->
                </div>
            </div>

            <!-- Mathematical Breakdown Card -->
            <div class="md:col-span-4 bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3 text-xs">
                <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                    <span class="font-bold text-cyan-300">Skip-Count Equation:</span>
                </div>
                <div id="tallyEquationBox" class="p-3 rounded-lg bg-slate-900 border border-slate-800 text-cyan-300 font-mono text-sm font-bold text-center">
                    5 + 5 + 5 + 2 = 17
                </div>
                <div class="p-2 rounded-lg bg-slate-900 border border-slate-800 space-y-1 text-slate-300 text-[11px]">
                    <div class="flex justify-between"><span>Complete Bundles:</span><b id="numBundlesText" class="text-emerald-400">3 bundles (15)</b></div>
                    <div class="flex justify-between"><span>Loose Single Strokes:</span><b id="numLooseText" class="text-amber-400">2 strokes</b></div>
                </div>
            </div>
        </div>
    </div>
    """,

    # Simulator 5: Letter Count Teams
    "sim_animal_letter_teams": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Forest Tournament: Animal Letter Count Teams</h3>
                <p class="text-xs text-slate-400">Filter animals by name length to assemble Team Short (≤4 letters) and Team Long (≥5 letters).</p>
            </div>
            <div class="flex gap-1.5 flex-wrap">
                <button onclick="filterAnimalTeams('all')" id="btnTeamAll" class="px-2.5 py-1 text-xs rounded-lg bg-amber-500 text-slate-950 font-bold transition">All Animals</button>
                <button onclick="filterAnimalTeams('short')" id="btnTeamShort" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">Team Short (≤4 Letters)</button>
                <button onclick="filterAnimalTeams('long')" id="btnTeamLong" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">Team Long (≥5 Letters)</button>
            </div>
        </div>

        <!-- Animal Cards Grid -->
        <div id="animalCardsGrid" class="grid grid-cols-2 sm:grid-cols-5 gap-2.5">
            <!-- Animal Cards rendered by JS -->
        </div>

        <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs flex flex-col sm:flex-row items-center justify-between gap-2">
            <span id="teamSummaryText" class="text-slate-300">Displaying all 10 forest animals sorted by name letter count.</span>
            <span id="teamCountBadge" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30 font-bold shrink-0">10 Animals</span>
        </div>
    </div>
    """,

    # Simulator 6: Name Length Analysis
    "sim_name_length_ruler": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-cyan-300">Character Length Measurement Ruler</h3>
                <p class="text-xs text-slate-400">Choose a name or type a custom word to measure its exact letter length on the calibrated ruler.</p>
            </div>
            <div class="flex items-center gap-2">
                <select id="presetNameSelect" onchange="measurePresetName(this.value)" class="bg-slate-950 border border-slate-700 text-xs rounded-lg px-2.5 py-1 text-slate-200 outline-none">
                    <option value="OM">OM (2 letters)</option>
                    <option value="JOY">JOY (3 letters)</option>
                    <option value="AMAN">AMAN (4 letters)</option>
                    <option value="PRIYA" selected>PRIYA (5 letters)</option>
                    <option value="SHRINATHAN">SHRINATHAN (10 letters)</option>
                </select>
            </div>
        </div>

        <div class="bg-slate-950 rounded-xl p-5 border border-slate-800 flex flex-col items-center justify-center space-y-4 min-h-[190px]">
            <!-- Letter Boxes on Calibrated Grid -->
            <div id="rulerBoxesContainer" class="flex items-center gap-1.5 flex-wrap justify-center">
                <!-- Injected by JS -->
            </div>

            <!-- Calibrated Visual Ruler -->
            <div class="w-full max-w-lg border-t-2 border-cyan-500/60 pt-1 flex justify-between text-[10px] text-cyan-400 font-mono">
                <span>0</span><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span><span>10</span>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs text-center">
            <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800">
                <span class="text-slate-400 block text-[11px]">Selected Name:</span>
                <b id="measuredNameText" class="text-white text-sm font-bold">PRIYA</b>
            </div>
            <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800">
                <span class="text-slate-400 block text-[11px]">Letter Length:</span>
                <b id="measuredLengthBadge" class="text-cyan-300 text-sm font-bold">5 Units</b>
            </div>
            <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800">
                <span class="text-slate-400 block text-[11px]">Comparison:</span>
                <span id="measuredComparisonText" class="text-amber-300 font-semibold text-[11px]">3 letters longer than OM</span>
            </div>
        </div>
    </div>
    """,

    # Simulator 7: Alphabet Letter Frequencies
    "sim_letter_frequency_sorter": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-emerald-300">Classroom Registry Alphabet Frequency Sorter</h3>
                <p class="text-xs text-slate-400">Analyze starting letters, vowel counts, and find the statistical mode in classroom names.</p>
            </div>
            <div class="flex gap-1.5">
                <button onclick="sortLetterFreq('initial')" id="btnFreqInit" class="px-2.5 py-1 text-xs rounded-lg bg-emerald-600 text-white font-bold transition">Starting Letters</button>
                <button onclick="sortLetterFreq('vowels')" id="btnFreqVowel" class="px-2.5 py-1 text-xs rounded-lg bg-slate-800 text-slate-300 hover:text-white font-bold transition">Vowel Counts</button>
            </div>
        </div>

        <!-- Frequency Distribution Bars -->
        <div id="freqDistributionContainer" class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-2.5 min-h-[200px]">
            <!-- Injected by JS -->
        </div>

        <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 flex items-center justify-between text-xs">
            <span id="freqInsightText" class="text-slate-300">Letter <b>A</b> is the statistical mode, starting 4 out of 10 student names!</span>
            <span class="px-2.5 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold">Mode = A</span>
        </div>
    </div>
    """,

    # Simulator 8: Number Name Cards
    "sim_number_name_cards": """
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm font-bold text-amber-300">Word Cards: Value vs Letter Count Paradox</h3>
                <p class="text-xs text-slate-400">Click different number cards to compare their numerical value against their written word length.</p>
            </div>
        </div>

        <!-- Word Cards Grid -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <button onclick="inspectNumberCard('10', 'TEN', 3)" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 hover:border-amber-400 text-left transition space-y-1">
                <div class="text-lg font-bold text-white">10</div>
                <div class="text-xs font-semibold text-amber-300">"TEN"</div>
                <div class="text-[11px] text-slate-400">3 letters</div>
            </button>
            <button onclick="inspectNumberCard('17', 'SEVENTEEN', 9)" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 hover:border-amber-400 text-left transition space-y-1">
                <div class="text-lg font-bold text-white">17</div>
                <div class="text-xs font-semibold text-amber-300">"SEVENTEEN"</div>
                <div class="text-[11px] text-slate-400">9 letters</div>
            </button>
            <button onclick="inspectNumberCard('70', 'SEVENTY', 7)" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 hover:border-amber-400 text-left transition space-y-1">
                <div class="text-lg font-bold text-white">70</div>
                <div class="text-xs font-semibold text-amber-300">"SEVENTY"</div>
                <div class="text-[11px] text-slate-400">7 letters</div>
            </button>
            <button onclick="inspectNumberCard('100', 'ONE HUNDRED', 10)" class="p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 hover:border-amber-400 text-left transition space-y-1">
                <div class="text-lg font-bold text-white">100</div>
                <div class="text-xs font-semibold text-amber-300">"ONE HUNDRED"</div>
                <div class="text-[11px] text-slate-400">10 letters</div>
            </button>
        </div>

        <!-- Inspection Result Card -->
        <div id="numberCardInspectBox" class="p-4 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2">
            <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                <span class="font-bold text-amber-300 text-sm">Paradox Investigation: 17 vs 70</span>
                <span class="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30 font-bold">Surprising Finding!</span>
            </div>
            <p id="cardInspectDetail" class="text-slate-300">
                Number <b>70</b> is vastly greater in numerical value than <b>17</b>, yet 'SEVENTY' has only <b>7 letters</b> while 'SEVENTEEN' has <b>9 letters</b>! Numerical magnitude does not dictate word spelling length.
            </p>
        </div>
    </div>
    """
}

