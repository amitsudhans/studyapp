"""
Simulators 9 to 16 for Class 5 Mathematics Chapter 2: Fractions.
Zero raw LaTeX! Clean Unicode symbols throughout.
"""

SIM_9_HTML = '''
<div class="space-y-4">
    <div class="bg-indigo-950/60 p-4 rounded-xl border border-indigo-500/30 text-center">
        <h4 class="text-sm font-bold text-indigo-300 uppercase tracking-wider mb-1">Same Numerator Slice Comparator</h4>
        <p class="text-xs text-slate-300">Compare fractions with the same numerator: fewer cuts mean larger slices!</p>
    </div>

    <!-- Paratha Slice Comparisons -->
    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-4 rounded-xl border border-slate-800 text-center font-mono text-xs">
        <div class="p-3 bg-slate-950 rounded-lg border border-slate-800">
            <span class="text-sky-400 font-bold block mb-1">4/6 of Paratha</span>
            <div class="text-[11px] text-slate-400 mb-2">Each slice = 1/6 (6 slices)</div>
            <div class="w-full h-6 bg-slate-800 rounded-full overflow-hidden p-0.5">
                <div class="h-full bg-sky-500 rounded-full" style="width: 66.6%;"></div>
            </div>
            <span class="text-xs text-white font-bold block mt-2">4 small slices (66.6%)</span>
        </div>

        <div class="p-3 bg-slate-950 rounded-lg border border-slate-800">
            <span class="text-amber-400 font-bold block mb-1">4/5 of Paratha</span>
            <div class="text-[11px] text-slate-400 mb-2">Each slice = 1/5 (5 slices)</div>
            <div class="w-full h-6 bg-slate-800 rounded-full overflow-hidden p-0.5">
                <div class="h-full bg-amber-500 rounded-full" style="width: 80%;"></div>
            </div>
            <span class="text-xs text-white font-bold block mt-2">4 large slices (80%)</span>
        </div>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="setSameNumCompare(4, 6, 5)" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">4/6 vs 4/5</button>
        <button onclick="setSameNumCompare(3, 8, 4)" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">3/8 vs 3/4</button>
        <button onclick="setSameNumCompare(2, 5, 3)" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">2/5 vs 2/3</button>
    </div>

    <div id="sameNumResultDisplay" class="p-3 bg-emerald-950/60 border border-emerald-500/40 rounded-xl text-center font-mono text-sm font-bold text-emerald-300">
        4/6 &lt; 4/5 (Since 1/6 &lt; 1/5, 4 fifths is greater!)
    </div>
</div>
'''

SIM_10_HTML = '''
<div class="space-y-4">
    <div class="bg-amber-950/60 p-4 rounded-xl border border-amber-500/30 text-center">
        <h4 class="text-sm font-bold text-amber-300 uppercase tracking-wider mb-1">Improper Paratha Bundler</h4>
        <p class="text-xs text-slate-300">Assemble 5 half-parathas into whole parathas to see why 5/2 = 2 1/2!</p>
    </div>

    <!-- Bundling Visualizer -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 text-center space-y-3 font-mono">
        <div class="text-xs text-slate-400">Total Slices: <span id="improperCountDisplay" class="text-lg font-bold text-amber-400">5 halves (5/2)</span></div>
        <div id="parathaBundleContainer" class="flex flex-wrap justify-center gap-3 min-h-[60px] items-center">
            <!-- Assembled wholes rendered dynamically -->
        </div>
        <div class="text-sm font-bold text-emerald-400" id="mixedNumberDisplay">5/2 = 2 Wholes and 1/2 (2 1/2)</div>
    </div>

    <div class="grid grid-cols-4 gap-2">
        <button onclick="setImproperSlices(3, 2)" class="p-2 bg-slate-800 hover:bg-amber-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">3/2 (1 1/2)</button>
        <button onclick="setImproperSlices(5, 2)" class="p-2 bg-slate-800 hover:bg-amber-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">5/2 (2 1/2)</button>
        <button onclick="setImproperSlices(7, 2)" class="p-2 bg-slate-800 hover:bg-amber-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">7/2 (3 1/2)</button>
        <button onclick="setImproperSlices(9, 4)" class="p-2 bg-slate-800 hover:bg-amber-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">9/4 (2 1/4)</button>
    </div>

    <div class="p-3 bg-slate-900 rounded-xl border border-slate-800 text-xs text-slate-300 text-center">
        Every 2 halves bundle into 1 whole paratha. The leftover fraction stays as the remainder!
    </div>
</div>
'''

SIM_11_HTML = '''
<div class="space-y-4">
    <div class="bg-cyan-950/60 p-4 rounded-xl border border-cyan-500/30 text-center">
        <h4 class="text-sm font-bold text-cyan-300 uppercase tracking-wider mb-1">Number Line Mixed Number Plotter</h4>
        <p class="text-xs text-slate-300">Plot improper fractions on the number line to see their exact mixed number position.</p>
    </div>

    <!-- Number Line SVG -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800">
        <svg viewBox="0 0 400 90" class="w-full">
            <!-- Main Axis -->
            <line x1="20" y1="50" x2="380" y2="50" stroke="#475569" stroke-width="3"/>
            <!-- Ticks 0, 1, 2, 3, 4 -->
            <line x1="40" y1="40" x2="40" y2="60" stroke="#94a3b8" stroke-width="2"/>
            <text x="40" y="75" fill="#94a3b8" font-size="12" font-family="monospace" text-anchor="middle">0</text>
            <line x1="120" y1="40" x2="120" y2="60" stroke="#94a3b8" stroke-width="2"/>
            <text x="120" y="75" fill="#94a3b8" font-size="12" font-family="monospace" text-anchor="middle">1</text>
            <line x1="200" y1="40" x2="200" y2="60" stroke="#94a3b8" stroke-width="2"/>
            <text x="200" y="75" fill="#94a3b8" font-size="12" font-family="monospace" text-anchor="middle">2</text>
            <line x1="280" y1="40" x2="280" y2="60" stroke="#94a3b8" stroke-width="2"/>
            <text x="280" y="75" fill="#94a3b8" font-size="12" font-family="monospace" text-anchor="middle">3</text>
            <line x1="360" y1="40" x2="360" y2="60" stroke="#94a3b8" stroke-width="2"/>
            <text x="360" y="75" fill="#94a3b8" font-size="12" font-family="monospace" text-anchor="middle">4</text>

            <!-- Plot Pin -->
            <g id="linePlotPin" transform="translate(220, 0)">
                <circle cx="0" cy="50" r="7" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
                <polygon points="0,40 -6,26 6,26" fill="#38bdf8"/>
                <rect x="-24" y="8" width="48" height="18" rx="4" fill="#0284c7"/>
                <text id="pinLabel" x="0" y="21" fill="#ffffff" font-size="10" font-weight="bold" font-family="monospace" text-anchor="middle">9/4</text>
            </g>
        </svg>

        <div class="mt-2 text-center font-mono">
            <span class="text-xs text-slate-400">Position: </span>
            <span id="plotMixedText" class="text-base font-bold text-cyan-300">9/4 = 2 1/4 (Between 2 and 3)</span>
        </div>
    </div>

    <div class="grid grid-cols-4 gap-2">
        <button onclick="plotOnLine(5, 2, '5/2', '2 1/2', 200 + 40)" class="p-2 bg-slate-800 hover:bg-cyan-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">5/2 (2 1/2)</button>
        <button onclick="plotOnLine(9, 4, '9/4', '2 1/4', 200 + 20)" class="p-2 bg-slate-800 hover:bg-cyan-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">9/4 (2 1/4)</button>
        <button onclick="plotOnLine(7, 2, '7/2', '3 1/2', 280 + 40)" class="p-2 bg-slate-800 hover:bg-cyan-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">7/2 (3 1/2)</button>
        <button onclick="plotOnLine(3, 2, '3/2', '1 1/2', 120 + 40)" class="p-2 bg-slate-800 hover:bg-cyan-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">3/2 (1 1/2)</button>
    </div>
</div>
'''

SIM_12_HTML = '''
<div class="space-y-4">
    <div class="bg-emerald-950/60 p-4 rounded-xl border border-emerald-500/30 text-center">
        <h4 class="text-sm font-bold text-emerald-300 uppercase tracking-wider mb-1">Benchmark 1 Balance Scale</h4>
        <p class="text-xs text-slate-300">Compare fractions instantly by seeing whether they are less than or greater than 1 Whole!</p>
    </div>

    <!-- Balance Scale Display -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 font-mono text-center space-y-3">
        <div class="grid grid-cols-3 gap-2 items-center">
            <div class="p-3 bg-rose-950/60 border border-rose-500/40 rounded-xl">
                <span class="text-xs text-rose-300 block mb-1">Fraction A</span>
                <span id="benchAFraction" class="text-lg font-bold text-white">7/8</span>
                <span id="benchAVerdict" class="text-[10px] text-rose-400 block mt-1">&lt; 1 (Needs 1/8)</span>
            </div>
            <div class="p-2 bg-slate-950 rounded-xl border border-slate-700">
                <span class="text-[10px] text-slate-400 block">Benchmark</span>
                <span class="text-xl font-bold text-amber-400">1 Whole</span>
            </div>
            <div class="p-3 bg-emerald-950/60 border border-emerald-500/40 rounded-xl">
                <span class="text-xs text-emerald-300 block mb-1">Fraction B</span>
                <span id="benchBFraction" class="text-lg font-bold text-white">8/6</span>
                <span id="benchBVerdict" class="text-[10px] text-emerald-400 block mt-1">&gt; 1 (Equals 1 2/6)</span>
            </div>
        </div>

        <div id="benchmarkComparisonResult" class="p-2.5 bg-slate-950 rounded-lg border border-slate-800 text-xs text-emerald-300 font-bold">
            Conclusion: 7/8 &lt; 1 &lt; 8/6, therefore 7/8 &lt; 8/6!
        </div>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="setBenchmark1('7/8', '8/6', '<')" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">7/8 vs 8/6</button>
        <button onclick="setBenchmark1('5/6', '7/5', '<')" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">5/6 vs 7/5</button>
        <button onclick="setBenchmark1('9/7', '3/4', '>')" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">9/7 vs 3/4</button>
    </div>
</div>
'''

SIM_13_HTML = '''
<div class="space-y-4">
    <div class="bg-teal-950/60 p-4 rounded-xl border border-teal-500/30 text-center">
        <h4 class="text-sm font-bold text-teal-300 uppercase tracking-wider mb-1">Benchmark 1/2 Gauge</h4>
        <p class="text-xs text-slate-300">Test any fraction against 1/2 by checking if its numerator is less than, equal to, or greater than half its denominator.</p>
    </div>

    <!-- Gauge Display -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 text-center font-mono space-y-3">
        <div>
            <span class="text-xs text-slate-400">Current Fraction: </span>
            <span id="halfGaugeFraction" class="text-2xl font-bold text-amber-400">5/8</span>
        </div>
        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-xs space-y-1">
            <div class="text-slate-300">Denominator = 8 &rarr; Half of denominator = <strong class="text-teal-400">4</strong></div>
            <div class="text-slate-300">Numerator = 5 &rarr; 5 is <strong class="text-emerald-400">greater than 4</strong></div>
        </div>
        <div id="halfGaugeBadge" class="p-2.5 bg-emerald-950/60 border border-emerald-500/40 rounded-lg text-xs font-bold text-emerald-300">
            Verdict: 5/8 is GREATER THAN 1/2 (&gt; 1/2)
        </div>
    </div>

    <div class="grid grid-cols-4 gap-2">
        <button onclick="testHalfBenchmark(5, 8, '5/8')" class="p-2 bg-slate-800 hover:bg-teal-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">5/8 (> 1/2)</button>
        <button onclick="testHalfBenchmark(3, 6, '3/6')" class="p-2 bg-slate-800 hover:bg-teal-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">3/6 (= 1/2)</button>
        <button onclick="testHalfBenchmark(2, 6, '2/6')" class="p-2 bg-slate-800 hover:bg-teal-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">2/6 (< 1/2)</button>
        <button onclick="testHalfBenchmark(7, 10, '7/10')" class="p-2 bg-slate-800 hover:bg-teal-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">7/10 (> 1/2)</button>
    </div>
</div>
'''

SIM_14_HTML = '''
<div class="space-y-4">
    <div class="bg-amber-950/60 p-4 rounded-xl border border-amber-500/30 text-center">
        <h4 class="text-sm font-bold text-amber-300 uppercase tracking-wider mb-1">Ant Parade Ruler March</h4>
        <p class="text-xs text-slate-300">Watch 16 tiny ants (1/4 cm each) march along the centimetre ruler: 16 &times; 1/4 = 4 cm!</p>
    </div>

    <!-- Centimetre Ruler with Ants -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 overflow-x-auto">
        <div class="min-w-[320px] p-2">
            <!-- Ruler Marks (0 to 5 cm) -->
            <div class="relative h-12 bg-amber-900/30 border-2 border-amber-600/50 rounded-lg flex items-end px-2 font-mono text-[10px] text-amber-300">
                <div class="absolute left-2 bottom-1">0 cm</div>
                <div class="absolute left-1/5 bottom-1" style="left: 20%;">1 cm</div>
                <div class="absolute left-2/5 bottom-1" style="left: 40%;">2 cm</div>
                <div class="absolute left-3/5 bottom-1" style="left: 60%;">3 cm</div>
                <div class="absolute left-4/5 bottom-1" style="left: 80%;">4 cm</div>
                <div class="absolute right-2 bottom-1">5 cm</div>
            </div>

            <!-- Marching Ants Track -->
            <div id="antTrack" class="flex flex-wrap gap-1 mt-3 min-h-[36px] items-center p-2 bg-slate-950 rounded-lg border border-slate-800">
                <!-- Ants rendered dynamically -->
            </div>
        </div>

        <div class="mt-3 text-center font-mono text-xs text-slate-300">
            Total Ants: <span id="antCountDisplay" class="font-bold text-amber-400">16 ants</span> | Total Length: <span id="antTotalLength" class="font-bold text-emerald-400">16 &times; 1/4 = 4 cm</span>
        </div>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="setAntCount(8)" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">8 Ants (2 cm)</button>
        <button onclick="setAntCount(12)" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">12 Ants (3 cm)</button>
        <button onclick="setAntCount(16)" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-emerald-300 border border-emerald-500/30 transition">16 Ants (4 cm)</button>
    </div>
</div>
'''

SIM_15_HTML = '''
<div class="space-y-4">
    <div class="bg-purple-950/60 p-4 rounded-xl border border-purple-500/30 text-center">
        <h4 class="text-sm font-bold text-purple-300 uppercase tracking-wider mb-1">Family Riddle Deduction Tree</h4>
        <p class="text-xs text-slate-300">Step through the logic riddle: “The only brother of your father's sister had a child...”</p>
    </div>

    <!-- Step Tree -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 space-y-2.5 font-mono text-xs">
        <div id="riddleStep1" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 transition">
            <span class="text-purple-400 font-bold">1. Clue: "Your father's sister"</span>
            <div class="text-slate-300 text-[11px] mt-0.5">&rarr; In kinship, your father's sister is your <strong>Aunt (Bua)</strong>.</div>
        </div>

        <div id="riddleStep2" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 transition">
            <span class="text-purple-400 font-bold">2. Clue: "The ONLY brother of your aunt"</span>
            <div class="text-slate-300 text-[11px] mt-0.5">&rarr; Since she has only one brother, that must be <strong>YOUR FATHER</strong>!</div>
        </div>

        <div id="riddleStep3" class="p-2.5 rounded-lg bg-slate-950 border border-slate-800 transition">
            <span class="text-purple-400 font-bold">3. Clue: "Had a child..."</span>
            <div class="text-slate-300 text-[11px] mt-0.5">&rarr; Your father's child is <strong>YOU, your brother, or your sister (sibling)</strong>!</div>
        </div>
    </div>

    <div class="flex justify-center space-x-2">
        <button onclick="revealRiddleStep(1)" class="px-3 py-1.5 bg-slate-800 hover:bg-purple-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Step 1</button>
        <button onclick="revealRiddleStep(2)" class="px-3 py-1.5 bg-slate-800 hover:bg-purple-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Step 2</button>
        <button onclick="revealRiddleStep(3)" class="px-3 py-1.5 bg-slate-800 hover:bg-purple-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Step 3 (Solve!)</button>
        <button onclick="resetRiddleSteps()" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-slate-400 border border-slate-700 transition">Reset</button>
    </div>

    <div id="riddleSolutionBanner" class="hidden p-3 bg-emerald-950/80 border border-emerald-500/50 rounded-xl text-center text-xs font-bold text-emerald-300">
        🎉 Riddle Solved: The child is your sibling (or yourself)!
    </div>
</div>
'''

SIM_16_HTML = '''
<div class="space-y-4">
    <div class="bg-rose-950/60 p-4 rounded-xl border border-rose-500/30 text-center">
        <h4 class="text-sm font-bold text-rose-300 uppercase tracking-wider mb-1">All-in-One Fraction Laboratory</h4>
        <p class="text-xs text-slate-300">Interactive workshop: adjust numerator and denominator to see visual area, mixed number, and benchmark status!</p>
    </div>

    <!-- Interactive Fraction Controls -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 space-y-3 font-mono">
        <div class="grid grid-cols-2 gap-3 text-center">
            <div>
                <label class="block text-xs text-slate-400 mb-1">Numerator: <strong id="labNumVal" class="text-amber-400 text-base">3</strong></label>
                <input type="range" id="labNumSlider" min="1" max="12" value="3" oninput="updateLabFraction()" class="w-full accent-amber-500">
            </div>
            <div>
                <label class="block text-xs text-slate-400 mb-1">Denominator: <strong id="labDenVal" class="text-sky-400 text-base">4</strong></label>
                <input type="range" id="labDenSlider" min="2" max="12" value="4" oninput="updateLabFraction()" class="w-full accent-sky-500">
            </div>
        </div>

        <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center space-y-2">
            <div class="text-3xl font-extrabold text-white" id="labFractionDisplay">3 / 4</div>
            <div class="text-xs text-slate-300" id="labTypeDisplay">Type: Proper Fraction (&lt; 1)</div>
            <div class="text-xs text-slate-300" id="labHalfStatus">Comparison to 1/2: 3/4 &gt; 1/2</div>
        </div>
    </div>

    <!-- Visual Pie/Bar Preview -->
    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 flex justify-center">
        <div class="w-full max-w-xs h-8 bg-slate-950 rounded-lg border border-slate-700 overflow-hidden p-0.5">
            <div id="labBarFill" class="h-full bg-gradient-to-r from-amber-500 to-rose-500 rounded transition-all duration-300" style="width: 75%;"></div>
        </div>
    </div>
</div>
'''

SIMS_PART2 = {
    9: SIM_9_HTML,
    10: SIM_10_HTML,
    11: SIM_11_HTML,
    12: SIM_12_HTML,
    13: SIM_13_HTML,
    14: SIM_14_HTML,
    15: SIM_15_HTML,
    16: SIM_16_HTML,
}

print("Simulators 9 to 16 defined successfully.")

