# -*- coding: utf-8 -*-
"""Class 4 Mathematics Chapter 14 Simulators Dictionary"""

SIMULATORS = {
    1: '''
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
''',
    2: '''
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
''',
    3: '''
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
''',
    4: '''
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
''',
    5: '''
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
''',
    6: '''
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
''',
    7: '''
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
''',
    8: '''
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
''',
    9: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Bal Mela Food Pictograph</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">1 Plate Icon = 5 Portions</span>
    </div>

    <!-- Day Filter Tabs -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button id="bm-tab-fri" onclick="showBalMelaDay('fri')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Friday</button>
        <button id="bm-tab-sat" onclick="showBalMelaDay('sat')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Saturday (Peak)</button>
        <button id="bm-tab-sun" onclick="showBalMelaDay('sun')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Sunday</button>
        <button id="bm-tab-all" onclick="showBalMelaDay('all')" class="px-3 py-1.5 rounded-lg border border-orange-500 bg-orange-950/40 text-orange-300 font-bold ring-2 ring-orange-500">All 3 Days</button>
    </div>

    <!-- Pictograph Rows -->
    <div class="space-y-3 bg-slate-950 p-4 rounded-xl border border-slate-800">
        <!-- Fruit Chaat -->
        <div>
            <div class="flex items-center justify-between text-xs font-semibold mb-1.5">
                <span class="text-emerald-400">🥗 Fruit Chaat</span>
                <span id="bm-chaat-stat" class="font-mono text-slate-300">18 plates = 90 portions</span>
            </div>
            <div id="bm-chaat-icons" class="flex flex-wrap gap-1.5 p-2 bg-slate-900 rounded-lg min-h-[40px] items-center">
                <!-- Plate SVGs injected by JS -->
            </div>
        </div>

        <!-- Sandwiches -->
        <div>
            <div class="flex items-center justify-between text-xs font-semibold mb-1.5">
                <span class="text-amber-400">🥪 Sandwiches</span>
                <span id="bm-sand-stat" class="font-mono text-slate-300">24 plates = 120 portions</span>
            </div>
            <div id="bm-sand-icons" class="flex flex-wrap gap-1.5 p-2 bg-slate-900 rounded-lg min-h-[40px] items-center">
                <!-- Plate SVGs injected by JS -->
            </div>
        </div>
    </div>

    <div class="flex items-center justify-between text-xs text-slate-400 px-1">
        <span>Scale Key: 🍽️ = 5 Servings</span>
        <span id="bm-day-total" class="font-bold text-orange-400">Total Weekend Sales: 210 Portions</span>
    </div>
</div>
''',
    10: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-red-500/20 text-red-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Food Sales Trend & Revenue</h3>
        </div>
        <span class="text-xs text-red-400 font-medium">Comparative Analysis</span>
    </div>

    <!-- Analytical Query Buttons -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button onclick="analyzeFoodSales('peak')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium">Highlight Peak Day</button>
        <button onclick="analyzeFoodSales('diff')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium">Item Difference (120 vs 90)</button>
        <button onclick="analyzeFoodSales('revenue')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium">Total Revenue (₹)</button>
    </div>

    <!-- Multi-Day Sales Comparison Table -->
    <div class="overflow-x-auto">
        <table class="w-full text-center text-xs border-collapse">
            <thead>
                <tr class="bg-slate-950 text-slate-300 border-b border-slate-800 font-semibold">
                    <th class="p-2.5 text-left">Festive Day</th>
                    <th class="p-2.5 text-emerald-400">Fruit Chaat (₹10)</th>
                    <th class="p-2.5 text-amber-400">Sandwiches (₹15)</th>
                    <th class="p-2.5 text-white">Daily Volume</th>
                    <th class="p-2.5 text-red-400 border-l border-slate-800">Daily Revenue</th>
                </tr>
            </thead>
            <tbody id="food-sales-body" class="divide-y divide-slate-800 font-mono">
                <tr id="row-fri" class="hover:bg-slate-950/40">
                    <td class="p-2.5 text-left font-sans text-slate-300 font-bold">Friday</td>
                    <td class="p-2.5 text-emerald-300">20</td>
                    <td class="p-2.5 text-amber-300">30</td>
                    <td class="p-2.5 text-white font-bold">50</td>
                    <td class="p-2.5 text-red-300 border-l border-slate-800">₹650</td>
                </tr>
                <tr id="row-sat" class="hover:bg-slate-950/40 bg-red-950/20">
                    <td class="p-2.5 text-left font-sans text-slate-300 font-bold">Saturday (Peak)</td>
                    <td class="p-2.5 text-emerald-300">40</td>
                    <td class="p-2.5 text-amber-300">50</td>
                    <td class="p-2.5 text-white font-bold">90</td>
                    <td class="p-2.5 text-red-300 border-l border-slate-800">₹1,150</td>
                </tr>
                <tr id="row-sun" class="hover:bg-slate-950/40">
                    <td class="p-2.5 text-left font-sans text-slate-300 font-bold">Sunday</td>
                    <td class="p-2.5 text-emerald-300">30</td>
                    <td class="p-2.5 text-amber-300">40</td>
                    <td class="p-2.5 text-white font-bold">70</td>
                    <td class="p-2.5 text-red-300 border-l border-slate-800">₹900</td>
                </tr>
            </tbody>
            <tfoot>
                <tr class="bg-slate-950/90 font-bold border-t-2 border-red-500 font-mono">
                    <td class="p-2.5 text-left font-sans text-red-400">Total Weekend</td>
                    <td class="p-2.5 text-emerald-400">90</td>
                    <td class="p-2.5 text-amber-400">120</td>
                    <td class="p-2.5 text-white text-sm">210</td>
                    <td class="p-2.5 text-emerald-400 border-l border-slate-800 text-sm">₹2,700</td>
                </tr>
            </tfoot>
        </table>
    </div>

    <!-- Spotlight Explanation Box -->
    <div id="food-analysis-box" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-relaxed">
        <strong>Peak Sales Insight:</strong> Saturday generated 90 snack sales and ₹1,150 revenue, making it the most profitable day due to heavy weekend crowd footfall.
    </div>
</div>
''',
    11: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-yellow-500/20 text-yellow-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Geometric Base-Ten Dienes Blocks</h3>
        </div>
        <span class="text-xs text-yellow-400 font-medium">Place-Value Manipulatives</span>
    </div>

    <!-- Block Controls -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 space-y-1.5">
            <span class="text-amber-400 font-bold block">Thousands (1,000)</span>
            <div class="flex items-center justify-center gap-2">
                <button onclick="adjustDienes('th', -1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">-</button>
                <span id="dienes-val-th" class="font-mono font-bold text-white w-4">1</span>
                <button onclick="adjustDienes('th', 1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">+</button>
            </div>
        </div>

        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 space-y-1.5">
            <span class="text-blue-400 font-bold block">Hundreds Flat (100)</span>
            <div class="flex items-center justify-center gap-2">
                <button onclick="adjustDienes('h', -1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">-</button>
                <span id="dienes-val-h" class="font-mono font-bold text-white w-4">2</span>
                <button onclick="adjustDienes('h', 1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">+</button>
            </div>
        </div>

        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 space-y-1.5">
            <span class="text-emerald-400 font-bold block">Tens Rod (10)</span>
            <div class="flex items-center justify-center gap-2">
                <button onclick="adjustDienes('t', -1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">-</button>
                <span id="dienes-val-t" class="font-mono font-bold text-white w-4">3</span>
                <button onclick="adjustDienes('t', 1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">+</button>
            </div>
        </div>

        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 space-y-1.5">
            <span class="text-rose-400 font-bold block">Unit Cube (1)</span>
            <div class="flex items-center justify-center gap-2">
                <button onclick="adjustDienes('u', -1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">-</button>
                <span id="dienes-val-u" class="font-mono font-bold text-white w-4">4</span>
                <button onclick="adjustDienes('u', 1)" class="w-6 h-6 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold">+</button>
            </div>
        </div>
    </div>

    <!-- Visual Canvas & Assembled Quantity -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div id="dienes-canvas" class="min-h-[90px] flex flex-wrap items-center justify-center gap-3 p-3 bg-slate-900 rounded-lg">
            <!-- SVG shapes rendered by JS -->
        </div>

        <div class="flex flex-col sm:flex-row items-center justify-between gap-2 border-t border-slate-800 pt-3 text-xs">
            <div id="dienes-expanded" class="font-mono text-slate-300">
                1,000 + 200 + 30 + 4
            </div>
            <div class="flex items-center gap-2 font-mono">
                <span class="text-slate-400">Total Numeral:</span>
                <span id="dienes-total" class="text-lg font-black text-yellow-400">1,234</span>
            </div>
        </div>
    </div>
</div>
''',
    12: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Folding Three-Dimensional Nets</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Spatial Unfolding Studio</span>
    </div>

    <!-- Shape Selection Tabs -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button id="net-btn-cube" onclick="selectNetShape('cube')" class="px-3 py-1.5 rounded-lg border border-teal-500 bg-teal-950/40 text-teal-300 font-bold ring-2 ring-teal-500">Cube (6 Squares)</button>
        <button id="net-btn-cuboid" onclick="selectNetShape('cuboid')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Cuboid (6 Rectangles)</button>
        <button id="net-btn-prism" onclick="selectNetShape('prism')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Triangular Prism</button>
        <button id="net-btn-pyramid" onclick="selectNetShape('pyramid')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Square Pyramid</button>
    </div>

    <!-- Interactive Fold Slider -->
    <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2">
        <div class="flex items-center justify-between text-xs text-slate-300">
            <span>2D Flat Net (0°)</span>
            <span id="net-angle-badge" class="font-mono text-teal-400 font-bold">Fold Angle: 0° (Flat)</span>
            <span>Folded 3D Solid (90°)</span>
        </div>
        <input type="range" id="net-fold-slider" min="0" max="90" value="0" oninput="updateNetFold(this.value)" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-teal-500">
    </div>

    <!-- SVG Net Visual Canvas -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col items-center justify-center min-h-[160px]">
        <svg id="net-svg-display" viewBox="0 0 300 160" class="w-full max-w-[280px] h-36">
            <!-- Dynamic 2D/3D net rendered by JS -->
        </svg>
        <p id="net-description" class="text-xs text-slate-300 text-center mt-2">
            A cube unfolds into 6 equal square faces meeting along shared edges.
        </p>
    </div>
</div>
''',
    13: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-sky-500/20 text-sky-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Place Value Arrow Cards</h3>
        </div>
        <span class="text-xs text-sky-400 font-medium">Expanded vs Compact Numeral</span>
    </div>

    <!-- Place Value Selectors -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
        <div>
            <label class="block text-slate-400 mb-1 text-[11px]">Thousands</label>
            <select id="ac-th" onchange="updateArrowCards()" class="w-full p-2 bg-slate-950 border border-slate-800 rounded-lg text-amber-400 font-mono font-bold">
                <option value="4000">4,000</option>
                <option value="2000">2,000</option>
                <option value="5000">5,000</option>
                <option value="7000">7,000</option>
            </select>
        </div>
        <div>
            <label class="block text-slate-400 mb-1 text-[11px]">Hundreds</label>
            <select id="ac-h" onchange="updateArrowCards()" class="w-full p-2 bg-slate-950 border border-slate-800 rounded-lg text-blue-400 font-mono font-bold">
                <option value="300">300</option>
                <option value="500">500</option>
                <option value="800">800</option>
                <option value="0">0 (None)</option>
            </select>
        </div>
        <div>
            <label class="block text-slate-400 mb-1 text-[11px]">Tens</label>
            <select id="ac-t" onchange="updateArrowCards()" class="w-full p-2 bg-slate-950 border border-slate-800 rounded-lg text-emerald-400 font-mono font-bold">
                <option value="20">20</option>
                <option value="40">40</option>
                <option value="70">70</option>
                <option value="0">0 (None)</option>
            </select>
        </div>
        <div>
            <label class="block text-slate-400 mb-1 text-[11px]">Ones</label>
            <select id="ac-u" onchange="updateArrowCards()" class="w-full p-2 bg-slate-950 border border-slate-800 rounded-lg text-rose-400 font-mono font-bold">
                <option value="5">5</option>
                <option value="2">2</option>
                <option value="8">8</option>
                <option value="9">9</option>
            </select>
        </div>
    </div>

    <!-- Toggle Action -->
    <div class="flex items-center justify-center gap-3">
        <button id="ac-btn-stack" onclick="setArrowCardMode('stacked')" class="px-4 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs transition-colors shadow">
            Stack Arrow Cards (Compact)
        </button>
        <button id="ac-btn-expand" onclick="setArrowCardMode('expanded')" class="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium text-xs transition-colors">
            Deconstruct (Expanded Form)
        </button>
    </div>

    <!-- Cards Display Box -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex items-center justify-center min-h-[100px] overflow-x-auto">
        <div id="arrow-cards-visual" class="flex items-center gap-2 font-mono font-bold text-sm">
            <!-- Dynamic arrow cards rendered by JS -->
        </div>
    </div>
</div>
''',
    14: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-purple-500/20 text-purple-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Fraction Strip Kit Comparator</h3>
        </div>
        <span class="text-xs text-purple-400 font-medium">24 cm Unit Benchmark</span>
    </div>

    <!-- Quick Equivalence Buttons -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button onclick="highlightFractionEquiv('half')" class="px-3 py-1 rounded bg-purple-950/60 hover:bg-purple-900 border border-purple-700 text-purple-200 font-medium">Show 1/2 = 2/4 = 4/8</button>
        <button onclick="highlightFractionEquiv('third')" class="px-3 py-1 rounded bg-purple-950/60 hover:bg-purple-900 border border-purple-700 text-purple-200 font-medium">Show 1/3 = 2/6 = 4/12</button>
        <button onclick="highlightFractionEquiv('quarter')" class="px-3 py-1 rounded bg-purple-950/60 hover:bg-purple-900 border border-purple-700 text-purple-200 font-medium">Show 1/4 = 2/8</button>
        <button onclick="resetFractionHighlights()" class="px-3 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs ml-auto">Reset</button>
    </div>

    <!-- Fraction Strips Stack -->
    <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-2 text-[11px] font-mono">
        <!-- 1 Whole -->
        <div class="flex items-center gap-2">
            <span class="w-10 text-slate-400 shrink-0">1 Whole</span>
            <div id="fs-row-1" class="flex-1 h-6 rounded bg-slate-700 flex items-center justify-center text-white font-bold border border-slate-600">1 (24 cm)</div>
        </div>

        <!-- 1/2 Strips -->
        <div class="flex items-center gap-2">
            <span class="w-10 text-slate-400 shrink-0">1/2</span>
            <div class="flex-1 flex gap-1 h-6">
                <div id="fs-half-1" class="flex-1 rounded bg-blue-700/80 flex items-center justify-center text-white font-bold border border-blue-500">1/2 (12 cm)</div>
                <div id="fs-half-2" class="flex-1 rounded bg-blue-700/80 flex items-center justify-center text-white font-bold border border-blue-500">1/2 (12 cm)</div>
            </div>
        </div>

        <!-- 1/4 Strips -->
        <div class="flex items-center gap-2">
            <span class="w-10 text-slate-400 shrink-0">1/4</span>
            <div class="flex-1 flex gap-1 h-6">
                <div id="fs-q-1" class="flex-1 rounded bg-emerald-700/80 flex items-center justify-center text-white font-bold border border-emerald-500">1/4</div>
                <div id="fs-q-2" class="flex-1 rounded bg-emerald-700/80 flex items-center justify-center text-white font-bold border border-emerald-500">1/4</div>
                <div id="fs-q-3" class="flex-1 rounded bg-emerald-700/80 flex items-center justify-center text-white font-bold border border-emerald-500">1/4</div>
                <div id="fs-q-4" class="flex-1 rounded bg-emerald-700/80 flex items-center justify-center text-white font-bold border border-emerald-500">1/4</div>
            </div>
        </div>

        <!-- 1/8 Strips -->
        <div class="flex items-center gap-2">
            <span class="w-10 text-slate-400 shrink-0">1/8</span>
            <div class="flex-1 flex gap-0.5 h-6">
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
                <div class="fs-oct flex-1 rounded bg-amber-700/80 flex items-center justify-center text-[10px] text-white font-bold border border-amber-500">1/8</div>
            </div>
        </div>
    </div>

    <!-- Comparison Feedback -->
    <div id="fraction-feedback-box" class="text-xs text-center text-purple-300 p-2.5 rounded-lg bg-purple-950/30 border border-purple-800/40">
        Equivalence Proof: Two 1/4 segments (6 cm + 6 cm = 12 cm) equal one 1/2 segment (12 cm).
    </div>
</div>
''',
    15: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-green-500/20 text-green-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Word Problem Bar Models</h3>
        </div>
        <span class="text-xs text-green-400 font-medium">Box Diagram Schematics</span>
    </div>

    <!-- Model Type Tabs -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button id="wp-tab-combine" onclick="selectWordProblemModel('combine')" class="px-3 py-1.5 rounded-lg border border-green-500 bg-green-950/40 text-green-300 font-bold ring-2 ring-green-500">Combine Model (Add)</button>
        <button id="wp-tab-compare" onclick="selectWordProblemModel('compare')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Compare Model (Difference)</button>
        <button id="wp-tab-change" onclick="selectWordProblemModel('change')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Change Model (Subtract)</button>
    </div>

    <!-- Interactive Schematic Display -->
    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-4">
        <div id="wp-problem-text" class="text-xs text-slate-300 font-medium bg-slate-900 p-3 rounded-lg border border-slate-800 leading-relaxed">
            In our class survey, 24 boys and 24 girls participated. What is the total number of students surveyed?
        </div>

        <!-- Visual Bar Diagram Container -->
        <div id="wp-diagram-container" class="space-y-2 py-2">
            <!-- Dynamic SVG or Flex bars rendered by JS -->
        </div>

        <!-- Equation and Operation Solution -->
        <div class="flex items-center justify-between border-t border-slate-800 pt-3 text-xs">
            <div id="wp-equation" class="font-mono text-emerald-400 font-bold text-sm">
                24 + 24 = 48 Students
            </div>
            <div id="wp-operation-badge" class="px-2.5 py-1 rounded bg-green-900/40 border border-green-700 text-green-300 font-bold">
                Operation: Addition
            </div>
        </div>
    </div>
</div>
''',
    16: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Comprehensive Statistical Dashboard</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Unified Studio</span>
    </div>

    <!-- Multi-View Navigator Tabs -->
    <div class="flex flex-wrap gap-2 text-xs">
        <button id="dash-tab-overview" onclick="switchDashboardView('overview')" class="px-3 py-1.5 rounded-lg border border-indigo-500 bg-indigo-950/40 text-indigo-300 font-bold ring-2 ring-indigo-500">Summary Cards</button>
        <button id="dash-tab-table" onclick="switchDashboardView('table')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Frequency Table</button>
        <button id="dash-tab-picto" onclick="switchDashboardView('picto')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Food Pictograph</button>
        <button id="dash-tab-matrix" onclick="switchDashboardView('matrix')" class="px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium">Two-Way Matrix</button>
    </div>

    <!-- Active View Display Area -->
    <div id="dashboard-view-content" class="bg-slate-950 p-4 rounded-xl border border-slate-800 min-h-[160px] text-xs">
        <!-- Default: Summary Cards -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <div class="p-3 bg-slate-900 rounded-xl border border-blue-900/40 text-center space-y-1">
                <span class="text-[10px] uppercase font-bold text-slate-400">Class Survey</span>
                <div class="text-xl font-bold font-mono text-blue-400">45 Students</div>
                <span class="text-[10px] text-slate-500">Top: Math (14)</span>
            </div>
            <div class="p-3 bg-slate-900 rounded-xl border border-orange-900/40 text-center space-y-1">
                <span class="text-[10px] uppercase font-bold text-slate-400">Bal Mela Sales</span>
                <div class="text-xl font-bold font-mono text-orange-400">210 Portions</div>
                <span class="text-[10px] text-slate-500">Peak: Sat (90)</span>
            </div>
            <div class="p-3 bg-slate-900 rounded-xl border border-teal-900/40 text-center space-y-1">
                <span class="text-[10px] uppercase font-bold text-slate-400">Sports Matrix</span>
                <div class="text-xl font-bold font-mono text-teal-400">48 Students</div>
                <span class="text-[10px] text-slate-500">Both: 11 (23%)</span>
            </div>
            <div class="p-3 bg-slate-900 rounded-xl border border-purple-900/40 text-center space-y-1">
                <span class="text-[10px] uppercase font-bold text-slate-400">Total Revenue</span>
                <div class="text-xl font-bold font-mono text-purple-400">₹2,700</div>
                <span class="text-[10px] text-slate-500">120 Sand + 90 Chaat</span>
            </div>
        </div>
    </div>

    <div class="text-xs text-slate-400 text-center">
        Data Handling enables structured observation, accurate recording, graphical communication, and evidence-based decision making.
    </div>
</div>
''',
}
