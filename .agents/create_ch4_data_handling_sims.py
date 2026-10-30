import sys

def generate_simulators():
    simulators = [
        # Sim 1: Data Collection & Sports Survey Tracker
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Class Sports Survey Studio</span>
                <span id="surveyTotalBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Total Responses: 30</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col justify-center p-3">
                <div class="space-y-2 text-xs font-mono" id="sportsVoteBars">
                    <!-- Dynamic vote progress bars -->
                </div>
            </div>
            <div class="grid grid-cols-4 gap-1.5 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="castSportVote('Cricket')" class="px-1 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold">+Cricket</button>
                <button onclick="castSportVote('Football')" class="px-1 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">+Football</button>
                <button onclick="castSportVote('Badminton')" class="px-1 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold">+Badminton</button>
                <button onclick="resetSportsSurvey()" class="px-1 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-bold">Reset</button>
            </div>
        </div>
        """,

        # Sim 2: Interactive Tally Mark Generator
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Tally Mark Bundler</span>
                <span id="tallyCountBadge" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">Count = 13 (2 Bundles + 3)</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center p-4">
                <div id="tallyDisplay" class="flex flex-wrap items-center justify-center gap-4">
                    <!-- SVG Tally bundles injected dynamically -->
                </div>
            </div>
            <div class="space-y-2 pt-2 border-t border-slate-800">
                <div class="flex items-center justify-between text-xs text-slate-300">
                    <span>Adjust Survey Count:</span>
                    <span id="tallySliderVal" class="font-mono text-cyan-300 font-bold">13</span>
                </div>
                <input type="range" id="tallySlider" min="1" max="25" value="13" oninput="updateTallySim(parseInt(this.value))" class="w-full accent-amber-500 cursor-pointer">
            </div>
        </div>
        """,

        # Sim 3: Shoe Size Sorter & Letter Frequency Sieve
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Ascending Sorter & Frequency</span>
                <span id="sortStatusBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Mode: Sorted (Size 5 = 7x)</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col justify-center p-3">
                <div class="text-xs text-slate-400 mb-1">Class Shoe Sizes (20 students):</div>
                <div id="shoeSizesList" class="flex flex-wrap gap-1.5 font-mono text-xs">
                    <!-- Shoe sizes injected dynamically -->
                </div>
                <div class="mt-3 p-2 bg-slate-950/60 rounded border border-slate-800 text-[11px] font-mono text-slate-300" id="shoeStatsSummary">
                    Min: 4 | Max: 8 | Most Frequent (Mode): Size 5 (Count: 7)
                </div>
            </div>
            <div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="toggleShoeSort(false)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold">Raw Unsorted List</button>
                <button onclick="toggleShoeSort(true)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Sort Ascending</button>
            </div>
        </div>
        """,

        # Sim 4: Pictograph Studio with Scalable Key
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Dynamic Pictograph Studio</span>
                <span id="pictoKeyBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Key: 1 🚲 = 10 Bicycles</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col justify-center p-3 overflow-y-auto">
                <div id="pictographRows" class="space-y-3 font-mono text-xs">
                    <!-- Pictograph rows with bicycle icons -->
                </div>
            </div>
            <div class="grid grid-cols-3 gap-2 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setPictoScale(5)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold">Key: 1 = 5</button>
                <button onclick="setPictoScale(10)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Key: 1 = 10</button>
                <button onclick="setPictoScale(20)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold">Key: 1 = 20</button>
            </div>
        </div>
        """,

        # Sim 5: Partial Symbol Demonstration Lab
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Partial Symbol Precision Lab</span>
                <span id="partialSymbolBadge" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">Representing 25 Units</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col items-center justify-center p-3">
                <div class="text-xs text-slate-400 mb-2">Key: 1 Full Star = 10 Units | 1/2 Star = 5 Units</div>
                <div class="flex items-center gap-3 text-3xl my-2" id="partialStarIcons">
                    <span>⭐</span><span>⭐</span><span class="opacity-40">⭐</span>
                </div>
                <div class="text-xs font-mono text-cyan-300 bg-slate-950 px-3 py-1.5 rounded-lg border border-cyan-800/40 mt-2" id="partialExplainText">
                    2 Full Stars (20) + 1 Half Star (5) = 25 Units!
                </div>
            </div>
            <div class="grid grid-cols-4 gap-1.5 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setPartialTarget(15)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono font-bold">15</button>
                <button onclick="setPartialTarget(20)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">20</button>
                <button onclick="setPartialTarget(25)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-mono font-bold">25</button>
                <button onclick="setPartialTarget(35)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">35</button>
            </div>
        </div>
        """,

        # Sim 6: Interactive Vertical Bar Graph Builder
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Bar Graph Structure Lab</span>
                <span id="barGraphScaleBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Scale: 1 unit = 10 items</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="vBarSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Axes -->
                    <line x1="50" y1="200" x2="380" y2="200" stroke="#64748b" stroke-width="2"/>
                    <line x1="50" y1="20" x2="50" y2="200" stroke="#64748b" stroke-width="2"/>
                    <!-- Grid Lines & Scale Ticks -->
                    <g id="vBarGridGroup"></g>
                    <!-- Bars -->
                    <g id="vBarsGroup"></g>
                </svg>
            </div>
            <div class="grid grid-cols-3 gap-2 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setVBarDataset('sports')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold">Sports Votes</button>
                <button onclick="setVBarDataset('fruits')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Fruit Sales</button>
                <button onclick="setVBarDataset('traffic')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold">Hourly Traffic</button>
            </div>
        </div>
        """,

        # Sim 7: Bar Graph Crosshair Interpreter
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Bar Graph Reader & Crosshair</span>
                <span id="crosshairReadout" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">Hover over any bar to read</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center cursor-pointer">
                <svg id="readerSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <line x1="50" y1="200" x2="380" y2="200" stroke="#475569" stroke-width="2"/>
                    <line x1="50" y1="20" x2="50" y2="200" stroke="#475569" stroke-width="2"/>
                    <!-- Ticks -->
                    <g id="readerGridTicks"></g>
                    <!-- Bars -->
                    <g id="readerBarsGroup"></g>
                    <!-- Dynamic alignment crosshair -->
                    <line id="readerCrosshairLine" x1="50" y1="0" x2="380" y2="0" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3" opacity="0"/>
                </svg>
            </div>
            <div class="p-2 bg-slate-900/60 rounded text-center text-xs text-slate-300 border border-slate-800">
                Click any bar above to project its horizontal alignment line directly to the Y-axis!
            </div>
        </div>
        """,

        # Sim 8: Step-by-Step Graph Construction Drafter
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Graph Drafting Sequence</span>
                <span id="draftingStepBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Step 1: Perpendicular Axes</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="stepDraftSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Step 1: Axes -->
                    <g id="draftStepAxes">
                        <line x1="50" y1="200" x2="370" y2="200" stroke="#38bdf8" stroke-width="3"/>
                        <line x1="50" y1="30" x2="50" y2="200" stroke="#38bdf8" stroke-width="3"/>
                        <circle cx="50" cy="200" r="4" fill="#ef4444"/>
                        <text x="35" y="215" fill="#f87171" font-size="11" font-bold>0</text>
                    </g>
                    <!-- Step 2: Scale Numbers -->
                    <g id="draftStepScale" opacity="0">
                        <text x="25" y="155" fill="#94a3b8" font-size="10">20</text>
                        <line x1="45" y1="150" x2="50" y2="150" stroke="#94a3b8" stroke-width="2"/>
                        <text x="25" y="105" fill="#94a3b8" font-size="10">40</text>
                        <line x1="45" y1="100" x2="50" y2="100" stroke="#94a3b8" stroke-width="2"/>
                        <text x="25" y="55" fill="#94a3b8" font-size="10">60</text>
                        <line x1="45" y1="50" x2="50" y2="50" stroke="#94a3b8" stroke-width="2"/>
                    </g>
                    <!-- Step 3: Category Labels -->
                    <g id="draftStepCategories" opacity="0">
                        <text x="100" y="218" fill="#38bdf8" font-size="10" text-anchor="middle">Maths</text>
                        <text x="180" y="218" fill="#38bdf8" font-size="10" text-anchor="middle">Science</text>
                        <text x="260" y="218" fill="#38bdf8" font-size="10" text-anchor="middle">English</text>
                        <text x="340" y="218" fill="#38bdf8" font-size="10" text-anchor="middle">Hindi</text>
                    </g>
                    <!-- Step 4: Finished Bars -->
                    <g id="draftStepBars" opacity="0">
                        <rect x="80" y="75" width="40" height="125" rx="3" fill="#f59e0b" fill-opacity="0.8"/>
                        <rect x="160" y="50" width="40" height="150" rx="3" fill="#06b6d4" fill-opacity="0.8"/>
                        <rect x="240" y="112" width="40" height="88" rx="3" fill="#10b981" fill-opacity="0.8"/>
                        <rect x="320" y="88" width="40" height="112" rx="3" fill="#a855f7" fill-opacity="0.8"/>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-4 gap-1.5 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setDraftProtocolStep(1)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Step 1: Axes</button>
                <button onclick="setDraftProtocolStep(2)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Step 2: Scale</button>
                <button onclick="setDraftProtocolStep(3)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Step 3: Labels</button>
                <button onclick="setDraftProtocolStep(4)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold">Step 4: Bars</button>
            </div>
        </div>
        """,

        # Sim 9: Case Study Switcher (Sweets, Cricket, Household Budget)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Real-World Case Explorer</span>
                <span id="caseTitleBadge" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">Case: School Sweet Preferences</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center p-2">
                <svg id="caseSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <line x1="50" y1="200" x2="380" y2="200" stroke="#475569" stroke-width="2"/>
                    <line x1="50" y1="20" x2="50" y2="200" stroke="#475569" stroke-width="2"/>
                    <g id="caseBarsGroup"></g>
                </svg>
            </div>
            <div class="grid grid-cols-3 gap-2 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="loadCaseStudy('sweets')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold">Sweets Survey</button>
                <button onclick="loadCaseStudy('cricket')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Cricket Runs</button>
                <button onclick="loadCaseStudy('budget')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold">Family Budget</button>
            </div>
        </div>
        """,

        # Sim 10: Orientation Flipper (Vertical Columns vs Horizontal Bars)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Orientation Flipper Studio</span>
                <span id="orientationBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Orientation: Vertical Columns</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="orientSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <g id="orientGraphGroup"></g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setOrientation('vertical')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold">Vertical (Mountain Heights 🏔️)</button>
                <button onclick="setOrientation('horizontal')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Horizontal (River Lengths 🌊)</button>
            </div>
        </div>
        """,

        # Sim 11: Infographic Visual Enhancer
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Infographic Storyteller</span>
                <span class="font-mono text-violet-300 bg-violet-950/60 px-2 py-0.5 rounded border border-violet-800/40">Florence Nightingale Style</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col items-center justify-center p-3">
                <div class="w-full grid grid-cols-3 gap-2 text-center">
                    <div class="p-3 rounded-xl bg-slate-950 border border-cyan-500/30">
                        <div class="text-2xl mb-1">💧</div>
                        <div class="text-lg font-black font-mono text-cyan-300">140 L</div>
                        <div class="text-[10px] text-slate-400">Daily Water Use</div>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-950 border border-emerald-500/30">
                        <div class="text-2xl mb-1">🌲</div>
                        <div class="text-lg font-black font-mono text-emerald-300">24 %</div>
                        <div class="text-[10px] text-slate-400">Forest Cover</div>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-950 border border-amber-500/30">
                        <div class="text-2xl mb-1">⚡</div>
                        <div class="text-lg font-black font-mono text-amber-300">42 GW</div>
                        <div class="text-[10px] text-slate-400">Solar Energy</div>
                    </div>
                </div>
                <div class="mt-3 text-xs text-slate-300 text-center font-sans">
                    Infographics combine bold stats, meaningful icons, and color to explain information 5x faster than plain text!
                </div>
            </div>
            <div class="p-2 bg-slate-900/60 rounded text-center text-xs text-slate-300 border border-slate-800">
                Visual appeal must never distort numerical truth!
            </div>
        </div>
        """,

        # Sim 12: Misleading Graph Detector (Area Trap & Truncated Axis)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Misleading Graph Detector</span>
                <span id="misleadBadge" class="font-mono text-rose-300 bg-rose-950/60 px-2 py-0.5 rounded border border-rose-800/40">Showing: Deceptive Graph!</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center p-2">
                <svg id="misleadSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <g id="misleadGraphGroup"></g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="toggleMisleadGraph('deceptive')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-bold">Deceptive Truncated Axis</button>
                <button onclick="toggleMisleadGraph('honest')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold">Honest Axis (Starts at 0)</button>
            </div>
        </div>
        """,

        # Sim 13: Pictograph vs Bar Graph Side-by-Side Sieve
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Side-by-Side Sieve</span>
                <span id="compareModeBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Comparing Same Data</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center p-3">
                <div class="grid grid-cols-2 gap-3 w-full h-full">
                    <!-- Left: Mini Pictograph -->
                    <div class="bg-slate-950/80 p-2 rounded-xl border border-slate-800 flex flex-col justify-between">
                        <div class="text-[11px] font-bold text-amber-300 border-b border-slate-800 pb-1">Pictograph (1 🍎 = 10)</div>
                        <div class="text-xs font-mono space-y-1">
                            <div>A: 🍎🍎 (20)</div>
                            <div>B: 🍎🍎🍎 (30)</div>
                            <div>C: 🍎 (10)</div>
                        </div>
                        <div class="text-[10px] text-slate-400">Appealing & intuitive</div>
                    </div>
                    <!-- Right: Mini Bar Graph -->
                    <div class="bg-slate-950/80 p-2 rounded-xl border border-slate-800 flex flex-col justify-between">
                        <div class="text-[11px] font-bold text-cyan-300 border-b border-slate-800 pb-1">Bar Graph (Scale = 10)</div>
                        <div class="flex items-end gap-3 h-20 pt-2 border-b border-slate-700">
                            <div class="w-6 bg-cyan-500 rounded-t" style="height: 66%;"></div>
                            <div class="w-6 bg-cyan-500 rounded-t" style="height: 100%;"></div>
                            <div class="w-6 bg-cyan-500 rounded-t" style="height: 33%;"></div>
                        </div>
                        <div class="text-[10px] text-slate-400">Exact & scalable</div>
                    </div>
                </div>
            </div>
            <div class="p-2 bg-slate-900/60 rounded text-center text-xs text-slate-300 border border-slate-800">
                Use pictographs for engaging visual summaries; use bar graphs for mathematical precision!
            </div>
        </div>
        """,

        # Sim 14: Scale Selection Simulator (Squashed vs Optimal vs Overflow)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Scale Selection Simulator</span>
                <span id="scaleFeedbackBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Scale: 1 unit = 10 (Optimal!)</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="scaleSelectSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <line x1="50" y1="200" x2="380" y2="200" stroke="#475569" stroke-width="2"/>
                    <line x1="50" y1="20" x2="50" y2="200" stroke="#475569" stroke-width="2"/>
                    <g id="scaleSelectGraphGroup"></g>
                </svg>
            </div>
            <div class="grid grid-cols-3 gap-2 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="testScaleChoice('small')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-bold">Scale = 2 (Overflow!)</button>
                <button onclick="testScaleChoice('optimal')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold">Scale = 10 (Optimal)</button>
                <button onclick="testScaleChoice('large')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold">Scale = 50 (Squashed)</button>
            </div>
        </div>
        """,

        # Sim 15: Comparative Decade Population Graph
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Decade Population Growth</span>
                <span class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Growth 1990–2020: +45 Lakhs</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg class="w-full h-full" viewBox="0 0 400 240">
                    <line x1="60" y1="200" x2="380" y2="200" stroke="#64748b" stroke-width="2"/>
                    <line x1="60" y1="20" x2="60" y2="200" stroke="#64748b" stroke-width="2"/>
                    <!-- Ticks (Lakhs) -->
                    <text x="35" y="165" fill="#94a3b8" font-size="10">20L</text>
                    <text x="35" y="125" fill="#94a3b8" font-size="10">40L</text>
                    <text x="35" y="85" fill="#94a3b8" font-size="10">60L</text>
                    <text x="35" y="45" fill="#94a3b8" font-size="10">80L</text>
                    <!-- Bars for decades -->
                    <rect x="90" y="150" width="45" height="50" rx="3" fill="#0284c7"/>
                    <text x="112" y="218" fill="#38bdf8" font-size="10" text-anchor="middle">1990</text>
                    <rect x="160" y="120" width="45" height="80" rx="3" fill="#0284c7"/>
                    <text x="182" y="218" fill="#38bdf8" font-size="10" text-anchor="middle">2000</text>
                    <rect x="230" y="80" width="45" height="120" rx="3" fill="#0ea5e9"/>
                    <text x="252" y="218" fill="#38bdf8" font-size="10" text-anchor="middle">2010</text>
                    <rect x="300" y="40" width="45" height="160" rx="3" fill="#38bdf8"/>
                    <text x="322" y="218" fill="#38bdf8" font-size="10" text-anchor="middle">2020</text>
                </svg>
            </div>
            <div class="p-2 bg-slate-900/60 rounded text-center text-xs text-slate-300 border border-slate-800">
                Notice the upward staircase profile: visual proof of steady population expansion!
            </div>
        </div>
        """,

        # Sim 16: Grand Synthesis: Data Life Cycle Interactive Wheel
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">5-Stage Data Cycle Map</span>
                <span class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Complete Statistical Journey</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center p-2">
                <svg class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Central Hub -->
                    <circle cx="200" cy="120" r="35" fill="#0284c7" fill-opacity="0.2" stroke="#0ea5e9" stroke-width="2"/>
                    <text x="175" y="125" fill="#38bdf8" font-size="11" font-weight="bold">Data Cycle</text>
                    <!-- 5 Cyclic nodes -->
                    <!-- Node 1: Collect -->
                    <circle cx="200" cy="40" r="22" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                    <text x="180" y="44" fill="#fde047" font-size="9" font-weight="bold">1. Collect</text>
                    <!-- Node 2: Organize -->
                    <circle cx="280" cy="85" r="22" fill="#1e293b" stroke="#06b6d4" stroke-width="2"/>
                    <text x="257" y="89" fill="#22d3ee" font-size="9" font-weight="bold">2. Tally</text>
                    <!-- Node 3: Display -->
                    <circle cx="250" cy="180" r="22" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
                    <text x="228" y="184" fill="#34d399" font-size="9" font-weight="bold">3. Display</text>
                    <!-- Node 4: Format -->
                    <circle cx="150" cy="180" r="22" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
                    <text x="127" y="184" fill="#c084fc" font-size="9" font-weight="bold">4. Format</text>
                    <!-- Node 5: Infer -->
                    <circle cx="120" cy="85" r="22" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
                    <text x="100" y="89" fill="#f472b6" font-size="9" font-weight="bold">5. Infer</text>
                </svg>
            </div>
            <div class="p-2 bg-slate-900/60 rounded text-center text-xs text-slate-300 border border-slate-800">
                Collect → Tally → Display → Format → Infer: The universal process of statistical discovery!
            </div>
        </div>
        """
    ]

    code = f'''"""NCERT Class 6 Mathematics Chapter 4: Data Handling and Presentation Simulators."""

SIMULATORS = {simulators}
'''

    # Strict check for zero raw LaTeX
    forbidden = ["\\text", "\\frac", "\\circ", "\\angle", "\\overleftrightarrow", "\\overline", "\\vec", "\\approx", "\\dots", "\\sqrt"]
    for word in forbidden:
        if word in code:
            raise ValueError(f"CRITICAL ERROR: Found raw LaTeX '{word}' in simulators module!")

    # Check for surrogates
    clean_chars = [ch for ch in code if not (0xD800 <= ord(ch) <= 0xDFFF)]
    clean_code = ''.join(clean_chars)

    with open(".agents/class6_math_data_handling_sims.py", "w", encoding="utf-8") as f:
        f.write(clean_code)

    print("Successfully generated .agents/class6_math_data_handling_sims.py with 16 bespoke simulators.")
    print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in simulators module!")

if __name__ == "__main__":
    generate_simulators()
