# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 14: Data Handling
Part 1 Simulators: Slides 1 to 8
Bespoke SVG/HTML interactive simulators.
Zero human names (replaced with generic roles).
Clean Unicode throughout.
"""

sim1 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-sky-500/20 text-sky-300 font-bold flex items-center justify-center text-sm">01</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Survey Question Evaluator</h3>
        </div>
        <span class="text-xs text-sky-400 font-medium">Question Design Laboratory</span>
    </div>

    <!-- Question Comparison Selector -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <button id="sq-btn-open" onclick="selectSurveyQuestion('open')" class="p-3.5 rounded-xl border border-rose-500/50 bg-rose-950/20 text-left hover:bg-rose-900/30 transition-all flex flex-col gap-1">
            <div class="flex items-center justify-between">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400">Question A (Open-Ended)</span>
                <span class="text-xs px-2 py-0.5 rounded bg-rose-500/20 text-rose-300">Ambiguous</span>
            </div>
            <p class="text-sm font-semibold text-white">"Which subjects do you like in school?"</p>
        </button>

        <button id="sq-btn-spec" onclick="selectSurveyQuestion('specific')" class="p-3.5 rounded-xl border border-emerald-500/50 bg-emerald-950/30 text-left hover:bg-emerald-900/30 transition-all flex flex-col gap-1 ring-2 ring-emerald-500">
            <div class="flex items-center justify-between">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Question B (Specific)</span>
                <span class="text-xs px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300">Recommended</span>
            </div>
            <p class="text-sm font-semibold text-white">"Which single subject do you like the most?"</p>
        </button>
    </div>

    <!-- Simulated Classmate Responses Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div class="flex items-center justify-between text-xs text-slate-400 border-b border-slate-800 pb-2">
            <span class="font-semibold text-slate-300">Simulated Student Poll Results (3 Sample Children)</span>
            <span id="sq-data-status" class="text-emerald-400 font-medium">Clean Single-Choice Data</span>
        </div>

        <div id="sq-responses-box" class="space-y-2 text-xs font-mono">
            <!-- Dynamic responses will be populated here -->
        </div>
    </div>

    <!-- Pedagogical Assessment Card -->
    <div id="sq-analysis-card" class="bg-emerald-950/20 border border-emerald-800/40 p-3 rounded-xl text-xs text-emerald-300 leading-relaxed">
        <strong>Survey Design Insight:</strong> Asking for the single most favorite subject produces exactly one category per student, allowing fast, unambiguous tallying and direct frequency tabulation.
    </div>
</div>
"""

sim2 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">02</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Student Response Stream Recorder</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Raw Letter-Code Log</span>
    </div>

    <!-- Action Toolbar -->
    <div class="flex flex-wrap items-center justify-between gap-2">
        <div class="flex items-center gap-1.5 text-xs text-slate-400">
            <span>Progress:</span>
            <span id="stream-count-badge" class="font-bold text-indigo-400 bg-indigo-950/50 px-2.5 py-1 rounded-md border border-indigo-800 font-mono">45 / 45 Recorded</span>
        </div>
        <div class="flex items-center gap-2">
            <button onclick="generateFullStream()" class="px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs transition-colors shadow">
                Generate Full 45
            </button>
            <button onclick="clearStreamLog()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs transition-colors">
                Reset
            </button>
        </div>
    </div>

    <!-- Legend -->
    <div class="flex flex-wrap gap-2 text-[11px] text-slate-300 bg-slate-950 p-2.5 rounded-lg border border-slate-800">
        <span class="flex items-center gap-1"><span class="w-3 h-3 rounded bg-blue-500 inline-block"></span> M: Math</span>
        <span class="flex items-center gap-1"><span class="w-3 h-3 rounded bg-emerald-500 inline-block"></span> L: Languages</span>
        <span class="flex items-center gap-1"><span class="w-3 h-3 rounded bg-purple-500 inline-block"></span> T: World Around Us</span>
        <span class="flex items-center gap-1"><span class="w-3 h-3 rounded bg-amber-500 inline-block"></span> A: Arts</span>
        <span class="flex items-center gap-1"><span class="w-3 h-3 rounded bg-rose-500 inline-block"></span> P.E.: Physical Ed</span>
    </div>

    <!-- 45-Student Raw Stream Grid -->
    <div id="stream-grid-container" class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 max-h-48 overflow-y-auto">
        <div id="stream-chips-grid" class="grid grid-cols-5 sm:grid-cols-9 gap-1.5 text-center font-mono font-bold text-xs">
            <!-- 45 chips populated by JS -->
        </div>
    </div>

    <div class="text-xs text-slate-400 text-center">
        Raw observational data preserves the authentic voice of all 45 classmates in compact letter notation.
    </div>
</div>
"""

sim3 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">03</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Interactive Frequency Table Builder</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Raw to Table Tabulator</span>
    </div>

    <!-- Step Buttons -->
    <div class="flex flex-wrap items-center gap-2">
        <button onclick="tabulateCategory('M')" class="px-2.5 py-1 rounded bg-blue-900/50 hover:bg-blue-800 text-blue-200 border border-blue-700 text-xs font-semibold">Tally Math (14)</button>
        <button onclick="tabulateCategory('L')" class="px-2.5 py-1 rounded bg-emerald-900/50 hover:bg-emerald-800 text-emerald-200 border border-emerald-700 text-xs font-semibold">Tally Lang (9)</button>
        <button onclick="tabulateCategory('T')" class="px-2.5 py-1 rounded bg-purple-900/50 hover:bg-purple-800 text-purple-200 border border-purple-700 text-xs font-semibold">Tally World (7)</button>
        <button onclick="tabulateCategory('A')" class="px-2.5 py-1 rounded bg-amber-900/50 hover:bg-amber-800 text-amber-200 border border-amber-700 text-xs font-semibold">Tally Arts (5)</button>
        <button onclick="tabulateCategory('PE')" class="px-2.5 py-1 rounded bg-rose-900/50 hover:bg-rose-800 text-rose-200 border border-rose-700 text-xs font-semibold">Tally P.E. (10)</button>
        <button onclick="tabulateAllCategories()" class="px-3 py-1 rounded bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold ml-auto">Tabulate All</button>
    </div>

    <!-- Structured Frequency Table -->
    <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border-collapse">
            <thead>
                <tr class="bg-slate-950 text-slate-300 border-b border-slate-800">
                    <th class="py-2.5 px-3 font-semibold">Favorite Subject</th>
                    <th class="py-2.5 px-3 font-semibold">Code</th>
                    <th class="py-2.5 px-3 font-semibold">Tally Visual</th>
                    <th class="py-2.5 px-3 font-semibold text-right">Number of Children</th>
                </tr>
            </thead>
            <tbody id="freq-table-body" class="divide-y divide-slate-800 font-mono">
                <!-- Rows populated by JS -->
            </tbody>
            <tfoot>
                <tr class="bg-slate-950/80 font-bold text-white border-t-2 border-emerald-500">
                    <td colspan="3" class="py-2.5 px-3">Total Children Counted</td>
                    <td id="freq-grand-total" class="py-2.5 px-3 text-right text-emerald-400 font-mono">0 / 45</td>
                </tr>
            </tfoot>
        </table>
    </div>

    <div id="freq-sum-verification" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 text-xs text-center text-slate-400">
        Verification: 14 + 9 + 7 + 5 + 10 = <span class="text-emerald-400 font-bold">45</span> (Exact match with surveyed class size)
    </div>
</div>
"""

sim4 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-purple-500/20 text-purple-300 font-bold flex items-center justify-center text-sm">04</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Data Table Analyzer</h3>
        </div>
        <span class="text-xs text-purple-400 font-medium">Statistical Insights Studio</span>
    </div>

    <!-- Query Trigger Buttons -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button onclick="analyzeTableMetric('most')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium">Most Popular</button>
        <button onclick="analyzeTableMetric('least')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium">Least Popular</button>
        <button onclick="analyzeTableMetric('diff')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium">Margin (M vs Arts)</button>
        <button onclick="analyzeTableMetric('stem')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium">M + T Combined</button>
        <button onclick="analyzeTableMetric('pe_ratio')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium">P.E. Share</button>
    </div>

    <!-- Active Metric Spotlight Display -->
    <div id="analyzer-card" class="bg-slate-950 p-4 rounded-xl border border-purple-900/40 flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="space-y-1">
            <div id="analyzer-badge" class="inline-block text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-purple-500/20 text-purple-300">Overview</div>
            <h4 id="analyzer-title" class="text-base font-bold text-white">Class Survey Analytics</h4>
            <p id="analyzer-desc" class="text-xs text-slate-300 leading-relaxed">Select any query button above to analyze specific frequencies, comparisons, and proportions.</p>
        </div>
        <div id="analyzer-stat" class="text-3xl font-black font-mono text-purple-400 shrink-0 bg-purple-950/40 px-5 py-3 rounded-xl border border-purple-800/50">
            45
        </div>
    </div>

    <!-- Comparative Mini Bar Preview -->
    <div class="space-y-1.5 text-xs">
        <div class="flex items-center justify-between text-slate-400 text-[11px]">
            <span>Mathematics (14)</span>
            <span>31.1%</span>
        </div>
        <div class="w-full bg-slate-950 h-2.5 rounded-full overflow-hidden">
            <div class="bg-blue-500 h-full rounded-full" style="width: 31.1%"></div>
        </div>
        <div class="flex items-center justify-between text-slate-400 text-[11px] pt-1">
            <span>Physical Education (10)</span>
            <span>22.2%</span>
        </div>
        <div class="w-full bg-slate-950 h-2.5 rounded-full overflow-hidden">
            <div class="bg-rose-500 h-full rounded-full" style="width: 22.2%"></div>
        </div>
    </div>
</div>
"""

sim5 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">05</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Ice Gola Tally Counter</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Five-Bundle Notation</span>
    </div>

    <!-- Flavor Tally Controls & Display -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <!-- Kala Khatta -->
        <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2">
            <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-purple-400">🍇 Kala Khatta</span>
                <div class="flex items-center gap-1.5">
                    <button onclick="adjustTally('kk', -1)" class="w-6 h-6 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 flex items-center justify-center font-bold text-xs">-</button>
                    <span id="tally-count-kk" class="font-mono font-bold text-sm text-white w-6 text-center">13</span>
                    <button onclick="adjustTally('kk', 1)" class="w-6 h-6 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 flex items-center justify-center font-bold text-xs">+</button>
                </div>
            </div>
            <div id="tally-svg-kk" class="h-10 bg-slate-900/80 rounded-lg p-1.5 flex items-center overflow-x-auto gap-2"></div>
        </div>

        <!-- Orange -->
        <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2">
            <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-amber-400">🍊 Orange Treat</span>
                <div class="flex items-center gap-1.5">
                    <button onclick="adjustTally('or', -1)" class="w-6 h-6 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 flex items-center justify-center font-bold text-xs">-</button>
                    <span id="tally-count-or" class="font-mono font-bold text-sm text-white w-6 text-center">18</span>
                    <button onclick="adjustTally('or', 1)" class="w-6 h-6 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 flex items-center justify-center font-bold text-xs">+</button>
                </div>
            </div>
            <div id="tally-svg-or" class="h-10 bg-slate-900/80 rounded-lg p-1.5 flex items-center overflow-x-auto gap-2"></div>
        </div>

        <!-- Rose -->
        <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2">
            <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-rose-400">🌹 Sweet Rose</span>
                <div class="flex items-center gap-1.5">
                    <button onclick="adjustTally('rs', -1)" class="w-6 h-6 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 flex items-center justify-center font-bold text-xs">-</button>
                    <span id="tally-count-rs" class="font-mono font-bold text-sm text-white w-6 text-center">9</span>
                    <button onclick="adjustTally('rs', 1)" class="w-6 h-6 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 flex items-center justify-center font-bold text-xs">+</button>
                </div>
            </div>
            <div id="tally-svg-rs" class="h-10 bg-slate-900/80 rounded-lg p-1.5 flex items-center overflow-x-auto gap-2"></div>
        </div>

        <!-- Mango -->
        <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2">
            <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-yellow-400">🥭 Ripe Mango</span>
                <div class="flex items-center gap-1.5">
                    <button onclick="adjustTally('mg', -1)" class="w-6 h-6 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 flex items-center justify-center font-bold text-xs">-</button>
                    <span id="tally-count-mg" class="font-mono font-bold text-sm text-white w-6 text-center">15</span>
                    <button onclick="adjustTally('mg', 1)" class="w-6 h-6 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 flex items-center justify-center font-bold text-xs">+</button>
                </div>
            </div>
            <div id="tally-svg-mg" class="h-10 bg-slate-900/80 rounded-lg p-1.5 flex items-center overflow-x-auto gap-2"></div>
        </div>
    </div>

    <div class="text-xs text-amber-300/80 bg-amber-950/20 p-2.5 rounded-lg border border-amber-900/30 text-center">
        Tally Mark Rule: Four vertical strokes are bundled together by the 5th diagonal slash.
    </div>
</div>
"""

sim6 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-300 font-bold flex items-center justify-center text-sm">06</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Ice Gola Pictograph Studio</h3>
        </div>
        <span class="text-xs text-pink-400 font-medium">Scaled Pictograph Engine</span>
    </div>

    <!-- Scale Key Selector -->
    <div class="flex items-center justify-between bg-slate-950 p-3 rounded-xl border border-slate-800">
        <span class="text-xs font-semibold text-slate-300">Choose Scale Key:</span>
        <div class="flex items-center gap-2">
            <button id="picto-scale-2" onclick="setPictoScale(2)" class="px-3 py-1 rounded-md text-xs font-bold border border-slate-700 bg-slate-800 text-slate-300">1 Cup = 2 Golas</button>
            <button id="picto-scale-4" onclick="setPictoScale(4)" class="px-3 py-1 rounded-md text-xs font-bold border border-pink-500 bg-pink-900/40 text-pink-300 ring-2 ring-pink-500">1 Cup = 4 Golas</button>
        </div>
    </div>

    <!-- Pictograph Rows -->
    <div class="space-y-2.5 bg-slate-950 p-3.5 rounded-xl border border-slate-800 text-xs">
        <!-- Kala Khatta: 28 -->
        <div class="flex items-center justify-between gap-3 border-b border-slate-800/80 pb-2">
            <span class="w-24 font-bold text-purple-400 shrink-0">Kala Khatta (28)</span>
            <div id="picto-row-kk" class="flex flex-wrap gap-1 items-center flex-1"></div>
            <span id="picto-badge-kk" class="font-mono text-slate-400 text-[11px] shrink-0">7 cups</span>
        </div>

        <!-- Orange: 36 -->
        <div class="flex items-center justify-between gap-3 border-b border-slate-800/80 pb-2">
            <span class="w-24 font-bold text-amber-400 shrink-0">Orange (36)</span>
            <div id="picto-row-or" class="flex flex-wrap gap-1 items-center flex-1"></div>
            <span id="picto-badge-or" class="font-mono text-slate-400 text-[11px] shrink-0">9 cups</span>
        </div>

        <!-- Rose: 20 -->
        <div class="flex items-center justify-between gap-3 border-b border-slate-800/80 pb-2">
            <span class="w-24 font-bold text-rose-400 shrink-0">Rose (20)</span>
            <div id="picto-row-rs" class="flex flex-wrap gap-1 items-center flex-1"></div>
            <span id="picto-badge-rs" class="font-mono text-slate-400 text-[11px] shrink-0">5 cups</span>
        </div>

        <!-- Mango: 24 -->
        <div class="flex items-center justify-between gap-3">
            <span class="w-24 font-bold text-yellow-400 shrink-0">Mango (24)</span>
            <div id="picto-row-mg" class="flex flex-wrap gap-1 items-center flex-1"></div>
            <span id="picto-badge-mg" class="font-mono text-slate-400 text-[11px] shrink-0">6 cups</span>
        </div>
    </div>

    <div class="text-[11px] text-slate-400 text-center">
        Scale Key Formula: Number of drawn icons = Total quantity ÷ Scale key value.
    </div>
</div>
"""

sim7 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">07</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Two-Variable Classification Matrix</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Cross-Tabulation Matrix</span>
    </div>

    <!-- 2x2 Matrix Grid Display -->
    <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 overflow-x-auto">
        <div class="min-w-[320px] grid grid-cols-3 gap-2 text-center text-xs">
            <div class="p-2 font-bold text-slate-400 bg-slate-900 rounded-lg">Participation</div>
            <div class="p-2 font-bold text-amber-400 bg-amber-950/40 rounded-lg border border-amber-800/40">Plays Cricket</div>
            <div class="p-2 font-bold text-slate-400 bg-slate-900 rounded-lg">No Cricket</div>

            <div class="p-2 font-bold text-blue-400 bg-blue-950/40 rounded-lg border border-blue-800/40 flex items-center justify-center">Plays Chess</div>
            <button onclick="highlightMatrixCell('both')" class="p-3 bg-indigo-950/40 hover:bg-indigo-900/50 rounded-lg border border-indigo-700/50 text-indigo-300 font-mono font-bold transition-all">
                Both Sports<br><span class="text-lg text-white">11</span>
            </button>
            <button onclick="highlightMatrixCell('only_chess')" class="p-3 bg-blue-950/30 hover:bg-blue-900/40 rounded-lg border border-blue-800/40 text-blue-300 font-mono font-bold transition-all">
                Only Chess<br><span class="text-lg text-white">11</span>
            </button>

            <div class="p-2 font-bold text-slate-400 bg-slate-900 rounded-lg flex items-center justify-center">No Chess</div>
            <button onclick="highlightMatrixCell('only_cricket')" class="p-3 bg-amber-950/30 hover:bg-amber-900/40 rounded-lg border border-amber-800/40 text-amber-300 font-mono font-bold transition-all">
                Only Cricket<br><span class="text-lg text-white">20</span>
            </button>
            <button onclick="highlightMatrixCell('neither')" class="p-3 bg-slate-900 hover:bg-slate-800 rounded-lg border border-slate-700 text-slate-400 font-mono font-bold transition-all">
                Neither Sport<br><span class="text-lg text-white">6</span>
            </button>
        </div>
    </div>

    <!-- Active Cell Descriptor -->
    <div id="matrix-info-box" class="p-3 rounded-xl bg-teal-950/30 border border-teal-800/40 text-xs text-teal-300 leading-relaxed">
        <strong>Cross-Tabulation Note:</strong> Every student in the class is placed in exactly one of the four non-overlapping boxes: Both (11) + Only Chess (11) + Only Cricket (20) + Neither (6) = <strong>48 Total Students</strong>.
    </div>
</div>
"""

sim8 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">08</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Contingency Table Totals Solver</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Row & Column Balance</span>
    </div>

    <!-- Complete 2-Way Contingency Table -->
    <div class="overflow-x-auto">
        <table class="w-full text-center text-xs border-collapse">
            <thead>
                <tr class="bg-slate-950 text-slate-300 border-b border-slate-800">
                    <th class="p-2.5 text-left font-semibold">Group</th>
                    <th class="p-2.5 font-semibold text-blue-400">Only Chess</th>
                    <th class="p-2.5 font-semibold text-amber-400">Only Cricket</th>
                    <th class="p-2.5 font-semibold text-indigo-400">Both Sports</th>
                    <th class="p-2.5 font-semibold text-slate-400">Neither</th>
                    <th class="p-2.5 font-semibold text-cyan-400 bg-cyan-950/30 border-l border-slate-800">Row Total</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-800 font-mono">
                <!-- Boys Row -->
                <tr class="hover:bg-slate-950/50">
                    <td class="p-2.5 text-left font-sans font-bold text-slate-300">Boys</td>
                    <td class="p-2.5 text-white">4</td>
                    <td class="p-2.5 text-white">12</td>
                    <td class="p-2.5 text-white">6</td>
                    <td class="p-2.5 text-slate-400">2</td>
                    <td class="p-2.5 font-bold text-cyan-300 bg-cyan-950/20 border-l border-slate-800">24</td>
                </tr>
                <!-- Girls Row -->
                <tr class="hover:bg-slate-950/50">
                    <td class="p-2.5 text-left font-sans font-bold text-slate-300">Girls</td>
                    <td class="p-2.5 text-white">7</td>
                    <td class="p-2.5 text-white">8</td>
                    <td class="p-2.5 text-white">5</td>
                    <td class="p-2.5 text-slate-400">4</td>
                    <td class="p-2.5 font-bold text-cyan-300 bg-cyan-950/20 border-l border-slate-800">24</td>
                </tr>
            </tbody>
            <tfoot>
                <!-- Column Totals -->
                <tr class="bg-slate-950/90 font-bold border-t-2 border-cyan-500 font-mono">
                    <td class="p-2.5 text-left font-sans text-cyan-400">Column Total</td>
                    <td class="p-2.5 text-blue-400">11</td>
                    <td class="p-2.5 text-amber-400">20</td>
                    <td class="p-2.5 text-indigo-400">11</td>
                    <td class="p-2.5 text-slate-300">6</td>
                    <td class="p-2.5 text-emerald-400 bg-cyan-950/50 border-l border-slate-800 text-sm">48</td>
                </tr>
            </tfoot>
        </table>
    </div>

    <!-- Verification Checks -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-[11px] font-mono text-slate-400">
        <div class="p-2 rounded bg-slate-950 border border-slate-800">
            Horizontal Row Sum: 24 (Boys) + 24 (Girls) = <strong class="text-emerald-400">48</strong>
        </div>
        <div class="p-2 rounded bg-slate-950 border border-slate-800">
            Vertical Col Sum: 11 + 20 + 11 + 6 = <strong class="text-emerald-400">48</strong>
        </div>
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
