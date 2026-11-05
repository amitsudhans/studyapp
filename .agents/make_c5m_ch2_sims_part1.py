"""
Simulators 1 to 8 for Class 5 Mathematics Chapter 2: Fractions.
Zero raw LaTeX! Clean Unicode symbols throughout.
"""

SIM_1_HTML = '''
<div class="space-y-4">
    <div class="bg-amber-950/60 p-4 rounded-xl border border-amber-500/30 text-center">
        <h4 class="text-sm font-bold text-amber-300 uppercase tracking-wider mb-1">Identical Wholes Visualizer</h4>
        <p class="text-xs text-slate-300">See why 1/2 of a small paratha is NOT the same as 1/2 of a large family paratha!</p>
    </div>

    <!-- Parathas Display -->
    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-4 rounded-xl border border-slate-800 text-center">
        <div class="flex flex-col items-center">
            <span class="text-xs font-bold text-amber-400 mb-2">Small Paratha (100g)</span>
            <div id="parathaSmall" class="relative w-24 h-24 rounded-full bg-amber-700/60 border-2 border-amber-500/80 flex items-center justify-center overflow-hidden transition-all duration-300">
                <div class="absolute left-0 top-0 bottom-0 w-1/2 bg-amber-500/50 border-r-2 border-amber-300"></div>
                <span class="relative z-10 text-xs font-bold font-mono text-white">1/2</span>
            </div>
            <span class="text-[11px] text-slate-400 mt-2 font-mono" id="weightSmall">50 grams of food</span>
        </div>

        <div class="flex flex-col items-center">
            <span class="text-xs font-bold text-sky-400 mb-2">Mega Paratha (300g)</span>
            <div id="parathaLarge" class="relative w-36 h-36 rounded-full bg-amber-700/60 border-2 border-sky-400 flex items-center justify-center overflow-hidden transition-all duration-300">
                <div class="absolute left-0 top-0 bottom-0 w-1/2 bg-sky-500/50 border-r-2 border-sky-300"></div>
                <span class="relative z-10 text-xs font-bold font-mono text-white">1/2</span>
            </div>
            <span class="text-[11px] text-slate-400 mt-2 font-mono" id="weightLarge">150 grams of food</span>
        </div>
    </div>

    <div class="grid grid-cols-2 gap-2">
        <button onclick="setParathaSizes(100, 300)" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Small vs Mega Paratha</button>
        <button onclick="setParathaSizes(200, 200)" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-emerald-300 border border-emerald-500/30 transition">Identical Wholes (200g each)</button>
    </div>

    <div id="sim1Status" class="p-3 bg-slate-900 rounded-xl border border-slate-800 text-xs text-slate-300 text-center">
        Both eat 1/2 of their paratha, but 150g is <strong>3 times more</strong> than 50g! Wholes must be identical to compare fractions fairly.
    </div>
</div>
'''

SIM_2_HTML = '''
<div class="space-y-4">
    <div class="bg-indigo-950/60 p-4 rounded-xl border border-indigo-500/30 text-center">
        <h4 class="text-sm font-bold text-indigo-300 uppercase tracking-wider mb-1">Square Grid Painter</h4>
        <p class="text-xs text-slate-300">Click squares to shade fractional parts and observe the live fraction counter!</p>
    </div>

    <!-- Grid Selection Tabs -->
    <div class="flex justify-center space-x-2">
        <button onclick="switchGrid('A')" id="tabGridA" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-indigo-600 text-white">Grid A (16 Sq)</button>
        <button onclick="switchGrid('B')" id="tabGridB" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300">Grid B (24 Sq)</button>
        <button onclick="switchGrid('C')" id="tabGridC" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300">Grid C (36 Sq)</button>
    </div>

    <!-- Grid Canvas -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 flex justify-center">
        <div id="gridCanvas" class="grid gap-1 p-2 bg-slate-950 rounded-lg border border-slate-800">
            <!-- Squares rendered dynamically -->
        </div>
    </div>

    <!-- Readout -->
    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 flex items-center justify-between text-xs">
        <div>
            <span class="text-slate-400">Shaded Squares: </span>
            <span id="shadedCountDisplay" class="font-mono font-bold text-amber-400">0</span>
            <span class="text-slate-400"> / </span>
            <span id="totalSquaresDisplay" class="font-mono font-bold text-white">16</span>
        </div>
        <div>
            <span class="text-slate-400">Fraction: </span>
            <span id="gridFractionDisplay" class="font-mono font-bold text-emerald-400 text-sm">0/16 = 0</span>
        </div>
    </div>

    <div class="flex justify-center space-x-2">
        <button onclick="presetShade(2)" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 text-xs font-medium text-slate-300 rounded border border-slate-700">Shade 1/8</button>
        <button onclick="presetShade(4)" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 text-xs font-medium text-slate-300 rounded border border-slate-700">Shade 1/4</button>
        <button onclick="presetShade(8)" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 text-xs font-medium text-slate-300 rounded border border-slate-700">Shade 1/2</button>
        <button onclick="clearGridShading()" class="px-3 py-1 bg-rose-950/60 hover:bg-rose-900 text-xs font-medium text-rose-300 rounded border border-rose-800/40">Reset</button>
    </div>
</div>
'''

SIM_3_HTML = '''
<div class="space-y-4">
    <div class="bg-blue-950/60 p-4 rounded-xl border border-blue-500/30 text-center">
        <h4 class="text-sm font-bold text-blue-300 uppercase tracking-wider mb-1">Fraction Strip Kit</h4>
        <p class="text-xs text-slate-300">Add colorful fraction pieces to discover how smaller parts construct 1 Whole strip.</p>
    </div>

    <!-- Whole Reference Strip -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 space-y-3">
        <div>
            <div class="text-[11px] text-slate-400 mb-1 font-semibold">1 Whole Strip:</div>
            <div class="w-full h-8 bg-amber-500/20 border-2 border-amber-500/50 rounded-lg flex items-center justify-center font-mono font-bold text-amber-300 text-xs">
                1 Whole (100%)
            </div>
        </div>

        <div>
            <div class="flex justify-between items-center text-[11px] text-slate-400 mb-1 font-semibold">
                <span>Your Assembled Strip:</span>
                <span id="kitFillPercent" class="font-mono text-emerald-400 font-bold">0% Filled</span>
            </div>
            <div id="kitWorkbench" class="w-full h-8 bg-slate-950 border-2 border-slate-700 rounded-lg flex overflow-hidden">
                <!-- Pieces dynamically placed here -->
            </div>
        </div>
    </div>

    <!-- Piece Selector Buttons -->
    <div class="grid grid-cols-4 gap-2 text-center">
        <button onclick="addKitPiece('1/2', 50, 'bg-blue-500/60 text-blue-200 border-blue-400')" class="p-2 bg-blue-950/70 border border-blue-500/40 hover:bg-blue-900 rounded-lg text-xs font-bold text-blue-300">+ 1/2</button>
        <button onclick="addKitPiece('1/4', 25, 'bg-emerald-500/60 text-emerald-200 border-emerald-400')" class="p-2 bg-emerald-950/70 border border-emerald-500/40 hover:bg-emerald-900 rounded-lg text-xs font-bold text-emerald-300">+ 1/4</button>
        <button onclick="addKitPiece('1/8', 12.5, 'bg-purple-500/60 text-purple-200 border-purple-400')" class="p-2 bg-purple-950/70 border border-purple-500/40 hover:bg-purple-900 rounded-lg text-xs font-bold text-purple-300">+ 1/8</button>
        <button onclick="addKitPiece('1/16', 6.25, 'bg-pink-500/60 text-pink-200 border-pink-400')" class="p-2 bg-pink-950/70 border border-pink-500/40 hover:bg-pink-900 rounded-lg text-xs font-bold text-pink-300">+ 1/16</button>
    </div>

    <div class="flex justify-between items-center text-xs">
        <span id="kitStatusText" class="text-slate-300">Click pieces above to build up to 1 Whole!</span>
        <button onclick="resetKit()" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded border border-slate-700 text-xs">Reset Strip</button>
    </div>
</div>
'''

SIM_4_HTML = '''
<div class="space-y-4">
    <div class="bg-emerald-950/60 p-4 rounded-xl border border-emerald-500/30 text-center">
        <h4 class="text-sm font-bold text-emerald-300 uppercase tracking-wider mb-1">Piece Relationships Bench</h4>
        <p class="text-xs text-slate-300">Highlight how two fourths equal one half, and four eighths equal one half!</p>
    </div>

    <!-- Comparative Strip Stack -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 space-y-2 font-mono text-xs text-center">
        <!-- 1 Whole -->
        <div class="p-2 rounded bg-amber-500/20 border border-amber-500/40 text-amber-300 font-bold">1 Whole</div>
        <!-- Halves -->
        <div class="grid grid-cols-2 gap-1">
            <div id="benchHalf1" class="p-2 rounded bg-blue-500/20 border border-blue-500/40 text-blue-300 font-bold transition">1/2</div>
            <div class="p-2 rounded bg-blue-500/10 border border-blue-500/20 text-slate-500">1/2</div>
        </div>
        <!-- Fourths -->
        <div class="grid grid-cols-4 gap-1">
            <div id="benchFourth1" class="p-2 rounded bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 font-bold transition">1/4</div>
            <div id="benchFourth2" class="p-2 rounded bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 font-bold transition">1/4</div>
            <div class="p-2 rounded bg-emerald-500/10 border border-emerald-500/20 text-slate-500">1/4</div>
            <div class="p-2 rounded bg-emerald-500/10 border border-emerald-500/20 text-slate-500">1/4</div>
        </div>
        <!-- Eighths -->
        <div class="grid grid-cols-8 gap-0.5 text-[10px]">
            <div id="benchEighth1" class="p-1.5 rounded bg-purple-500/20 border border-purple-500/40 text-purple-300 font-bold transition">1/8</div>
            <div id="benchEighth2" class="p-1.5 rounded bg-purple-500/20 border border-purple-500/40 text-purple-300 font-bold transition">1/8</div>
            <div id="benchEighth3" class="p-1.5 rounded bg-purple-500/20 border border-purple-500/40 text-purple-300 font-bold transition">1/8</div>
            <div id="benchEighth4" class="p-1.5 rounded bg-purple-500/20 border border-purple-500/40 text-purple-300 font-bold transition">1/8</div>
            <div class="p-1.5 rounded bg-purple-500/10 border border-purple-500/20 text-slate-600">1/8</div>
            <div class="p-1.5 rounded bg-purple-500/10 border border-purple-500/20 text-slate-600">1/8</div>
            <div class="p-1.5 rounded bg-purple-500/10 border border-purple-500/20 text-slate-600">1/8</div>
            <div class="p-1.5 rounded bg-purple-500/10 border border-purple-500/20 text-slate-600">1/8</div>
        </div>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="highlightRelation('two_fourths')" class="p-2 bg-slate-800 hover:bg-emerald-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Two 1/4 = 1/2</button>
        <button onclick="highlightRelation('four_eighths')" class="p-2 bg-slate-800 hover:bg-purple-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Four 1/8 = 1/2</button>
        <button onclick="highlightRelation('two_eighths')" class="p-2 bg-slate-800 hover:bg-blue-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Two 1/8 = 1/4</button>
    </div>

    <div id="benchRelationStatus" class="p-3 bg-slate-900 rounded-xl border border-slate-800 text-xs text-slate-300 text-center">
        Click a relationship button above to highlight the visual alignment!
    </div>
</div>
'''

SIM_5_HTML = '''
<div class="space-y-4">
    <div class="bg-violet-950/60 p-4 rounded-xl border border-violet-500/30 text-center">
        <h4 class="text-sm font-bold text-violet-300 uppercase tracking-wider mb-1">Whole-Building Puzzle Box</h4>
        <p class="text-xs text-slate-300">Combine different fraction pieces to hit exactly 1 Whole (100%) without overflowing!</p>
    </div>

    <!-- Progress Meter -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 space-y-2">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-400 font-semibold">Total Progress:</span>
            <span id="wholeBuildProgressText" class="font-mono font-bold text-amber-400">0 / 12 (0%)</span>
        </div>
        <div class="w-full h-6 bg-slate-950 rounded-full border border-slate-700 overflow-hidden p-0.5">
            <div id="wholeBuildProgressBar" class="h-full bg-gradient-to-r from-amber-500 to-emerald-400 rounded-full transition-all duration-300" style="width: 0%;"></div>
        </div>
    </div>

    <!-- Piece Buttons (In twelfths) -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="addWholeBuildPart(6, '1/2')" class="p-2 bg-slate-800 hover:bg-blue-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">+ 1/2 (6/12)</button>
        <button onclick="addWholeBuildPart(4, '1/3')" class="p-2 bg-slate-800 hover:bg-emerald-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">+ 1/3 (4/12)</button>
        <button onclick="addWholeBuildPart(3, '1/4')" class="p-2 bg-slate-800 hover:bg-amber-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">+ 1/4 (3/12)</button>
        <button onclick="addWholeBuildPart(2, '1/6')" class="p-2 bg-slate-800 hover:bg-purple-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">+ 1/6 (2/12)</button>
    </div>

    <div id="wholeBuildStatus" class="p-3 bg-slate-900 rounded-xl border border-slate-800 text-xs text-slate-300 text-center">
        Try: 1/2 + 1/4 + 1/4 = 1 Whole, or 1/3 + 1/3 + 1/3 = 1 Whole!
    </div>

    <div class="flex justify-center">
        <button onclick="resetWholeBuild()" class="px-4 py-1.5 bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 rounded-lg border border-slate-700 transition">Reset Puzzle</button>
    </div>
</div>
'''

SIM_6_HTML = '''
<div class="space-y-4">
    <div class="bg-cyan-950/60 p-4 rounded-xl border border-cyan-500/30 text-center">
        <h4 class="text-sm font-bold text-cyan-300 uppercase tracking-wider mb-1">Equivalent Fractions Slicer</h4>
        <p class="text-xs text-slate-300">Slice the rectangle horizontally to see 1/3 transform into 2/6, 3/9, and 4/12!</p>
    </div>

    <!-- Slicing Canvas -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 flex flex-col items-center">
        <div id="equivSliceBox" class="relative w-64 h-32 bg-slate-950 border-2 border-slate-700 rounded-lg overflow-hidden grid grid-cols-3">
            <!-- 3 Columns (1st column shaded) -->
            <div id="col1" class="bg-cyan-500/40 border-r border-slate-600 relative"></div>
            <div id="col2" class="border-r border-slate-600"></div>
            <div id="col3"></div>
        </div>
        <div class="mt-3 text-center">
            <span class="text-xs text-slate-400">Equivalent Fraction: </span>
            <span id="equivFractionText" class="text-xl font-bold font-mono text-cyan-300">1/3</span>
            <div class="text-[11px] text-slate-400 mt-0.5" id="equivSliceFormula">1 column out of 3 columns</div>
        </div>
    </div>

    <div class="grid grid-cols-4 gap-2">
        <button onclick="setEquivRows(1)" class="p-2 bg-slate-800 hover:bg-cyan-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">1 Row (1/3)</button>
        <button onclick="setEquivRows(2)" class="p-2 bg-slate-800 hover:bg-cyan-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">2 Rows (2/6)</button>
        <button onclick="setEquivRows(3)" class="p-2 bg-slate-800 hover:bg-cyan-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">3 Rows (3/9)</button>
        <button onclick="setEquivRows(4)" class="p-2 bg-slate-800 hover:bg-cyan-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">4 Rows (4/12)</button>
    </div>

    <div class="p-3 bg-slate-900 rounded-xl border border-slate-800 text-xs text-slate-300 text-center">
        <strong class="text-amber-400">Key Insight:</strong> The blue shaded region never grew or shrank! We only divided it into smaller pieces.
    </div>
</div>
'''

SIM_7_HTML = '''
<div class="space-y-4">
    <div class="bg-teal-950/60 p-4 rounded-xl border border-teal-500/30 text-center">
        <h4 class="text-sm font-bold text-teal-300 uppercase tracking-wider mb-1">Equivalence Scale &amp; Missing Terms</h4>
        <p class="text-xs text-slate-300">Find the missing numerator or denominator connecting equivalent fraction pairs.</p>
    </div>

    <!-- Interactive Scale -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 text-center space-y-3 font-mono">
        <div class="flex items-center justify-center space-x-4 text-xl font-bold">
            <div class="p-3 bg-teal-950/80 border border-teal-500/40 rounded-xl text-teal-300" id="scaleFracLeft">2 / 5</div>
            <div class="text-amber-400 text-2xl">=</div>
            <div class="p-3 bg-slate-950 border border-amber-500/40 rounded-xl text-amber-300" id="scaleFracRight">? / 10</div>
        </div>
        <div class="text-xs text-slate-300" id="scaleExplanation">Multiplier: 5 &times; 2 = 10, so 2 &times; 2 = <strong>4</strong></div>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setScalePair('2/5', '?/10', 4, 'num', 2)" class="p-2 bg-slate-800 hover:bg-teal-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">2/5 = ?/10</button>
        <button onclick="setScalePair('3/4', '9/?', 12, 'den', 3)" class="p-2 bg-slate-800 hover:bg-teal-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">3/4 = 9/?</button>
        <button onclick="setScalePair('3/7', '?/21', 9, 'num', 3)" class="p-2 bg-slate-800 hover:bg-teal-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">3/7 = ?/21</button>
        <button onclick="setScalePair('5/8', '25/?', 40, 'den', 5)" class="p-2 bg-slate-800 hover:bg-teal-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">5/8 = 25/?</button>
    </div>

    <div id="scaleResultBanner" class="p-3 bg-emerald-950/60 border border-emerald-500/40 rounded-xl text-center text-xs text-emerald-300 font-medium">
        Cross-Multiplication Check: 2 &times; 10 = 20, and 5 &times; 4 = 20 &check;
    </div>
</div>
'''

SIM_8_HTML = '''
<div class="space-y-4">
    <div class="bg-rose-950/60 p-4 rounded-xl border border-rose-500/30 text-center">
        <h4 class="text-sm font-bold text-rose-300 uppercase tracking-wider mb-1">Same Denominator Chikki Slices</h4>
        <p class="text-xs text-slate-300">Compare fractions sharing the same denominator: more slices of equal size win!</p>
    </div>

    <!-- Chikki Bars -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 space-y-3 font-mono">
        <div>
            <div class="flex justify-between items-center text-xs mb-1">
                <span class="text-amber-400 font-bold">Aarav: <span id="numAaravDisplay">1</span>/3 of Chikki</span>
                <span class="text-slate-400 text-[10px]">1 slice</span>
            </div>
            <div class="w-full h-8 bg-slate-950 rounded-lg border border-slate-700 flex overflow-hidden p-0.5">
                <div id="barAarav" class="h-full bg-amber-500 rounded transition-all duration-300" style="width: 33.3%;"></div>
            </div>
        </div>

        <div>
            <div class="flex justify-between items-center text-xs mb-1">
                <span class="text-emerald-400 font-bold">Meera: <span id="numMeeraDisplay">2</span>/3 of Chikki</span>
                <span class="text-slate-400 text-[10px]">2 slices</span>
            </div>
            <div class="w-full h-8 bg-slate-950 rounded-lg border border-slate-700 flex overflow-hidden p-0.5">
                <div id="barMeera" class="h-full bg-emerald-500 rounded transition-all duration-300" style="width: 66.6%;"></div>
            </div>
        </div>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="setChikkiComparison(1, 2, 3)" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">1/3 vs 2/3</button>
        <button onclick="setChikkiComparison(3, 5, 8)" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">3/8 vs 5/8</button>
        <button onclick="setChikkiComparison(4, 7, 10)" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">4/10 vs 7/10</button>
    </div>

    <div id="chikkiInequalityDisplay" class="p-3 bg-slate-900 rounded-xl border border-slate-800 text-center font-mono text-base font-bold text-emerald-400">
        1/3 &lt; 2/3 (Meera has more chikki!)
    </div>
</div>
'''

SIMS_PART1 = {
    1: SIM_1_HTML,
    2: SIM_2_HTML,
    3: SIM_3_HTML,
    4: SIM_4_HTML,
    5: SIM_5_HTML,
    6: SIM_6_HTML,
    7: SIM_7_HTML,
    8: SIM_8_HTML,
}

print("Simulators 1 to 8 defined successfully.")

