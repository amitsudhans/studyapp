# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 5: Sharing and Measuring
Part 2 Simulators: Slides 9 to 16
Bespoke SVG/HTML interactive simulators.
Zero human names.
"""

sim9 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-yellow-500/20 text-yellow-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Fractions of Discrete Collections</h3>
        </div>
        <span class="text-xs text-yellow-400 font-medium">Lamps & Cookies</span>
    </div>

    <!-- Collection Type Selector -->
    <div class="flex items-center justify-between gap-2 flex-wrap">
        <div class="flex items-center gap-2">
            <button onclick="setCollectionMode('lamps')" id="btn-col-lamps" class="px-3 py-1 rounded-xl bg-yellow-500 text-slate-950 font-bold text-xs shadow">8 Oil Lamps (1/4)</button>
            <button onclick="setCollectionMode('cookies')" id="btn-col-cookies" class="px-3 py-1 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700">12 Cookies</button>
        </div>
        <div id="cookieSharerControls" class="hidden flex items-center gap-1 text-xs">
            <span class="text-slate-400">Share with:</span>
            <button onclick="updateCookieShare(2)" class="px-1.5 py-0.5 rounded bg-slate-800 text-slate-200 border border-slate-700 font-bold">2</button>
            <button onclick="updateCookieShare(3)" class="px-1.5 py-0.5 rounded bg-slate-800 text-slate-200 border border-slate-700 font-bold">3</button>
            <button onclick="updateCookieShare(4)" class="px-1.5 py-0.5 rounded bg-slate-800 text-slate-200 border border-slate-700 font-bold">4</button>
            <button onclick="updateCookieShare(6)" class="px-1.5 py-0.5 rounded bg-slate-800 text-slate-200 border border-slate-700 font-bold">6</button>
        </div>
    </div>

    <!-- Collection Visual Display -->
    <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center gap-4 min-h-[220px]">
        <div id="collectionItemsContainer" class="flex flex-wrap items-center justify-center gap-3 max-w-[340px]">
            <!-- Injected dynamically in JS -->
        </div>

        <div id="collectionExplanation" class="text-xs text-center text-slate-300 font-semibold">
            8 oil lamps divided into 4 equal groups = <span class="text-yellow-400 font-bold">2 lamps per group (1/4)</span>.
        </div>
    </div>
</div>
"""

sim10 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-purple-500/20 text-purple-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Return Gifts Distribution Lab</h3>
        </div>
        <span class="text-xs text-purple-400 font-medium">Subsets of Items</span>
    </div>

    <!-- Problem Mode Selector -->
    <div class="flex items-center justify-center gap-3">
        <button onclick="setGiftMode('hairbands')" id="btn-gift-hairbands" class="px-3.5 py-1.5 rounded-xl bg-purple-600 text-white font-bold text-xs shadow">18 Hairbands (1/3 vs 2/3)</button>
        <button onclick="setGiftMode('pots')" id="btn-gift-pots" class="px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700">24 Clay Pots (1/4 vs 2/4)</button>
    </div>

    <!-- Visual Box Display -->
    <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center gap-3 min-h-[220px]">
        <div id="giftGridContainer" class="grid grid-cols-6 gap-2 max-w-[340px]">
            <!-- Injected dynamically in JS -->
        </div>

        <div id="giftSummaryText" class="text-xs text-center text-slate-300 font-semibold space-y-1">
            <!-- Summary breakdown -->
        </div>
    </div>
</div>
"""

sim11 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Everyday Fraction Explorer</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Sweet Box & Satin Ribbon</span>
    </div>

    <!-- Toggle Scenario -->
    <div class="flex items-center justify-center gap-3">
        <button onclick="setEverydayScenario('barfi')" id="btn-scen-barfi" class="px-3.5 py-1.5 rounded-xl bg-cyan-500 text-slate-950 font-bold text-xs shadow">16-Barfi Sweet Box</button>
        <button onclick="setEverydayScenario('ribbon')" id="btn-scen-ribbon" class="px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700">20 cm Satin Ribbon</button>
    </div>

    <!-- Interactive Workspace -->
    <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center gap-4 min-h-[220px]">
        <!-- Barfi Box Mode -->
        <div id="barfiContainer" class="flex flex-col items-center gap-3">
            <div class="flex items-center gap-2 text-xs">
                <span class="text-slate-400">Select shares to eat:</span>
                <button onclick="setBarfiShare(1)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-200 border border-slate-700 font-bold">1/4 (4)</button>
                <button onclick="setBarfiShare(2)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-200 border border-slate-700 font-bold">2/4 (8)</button>
                <button onclick="setBarfiShare(3)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-200 border border-slate-700 font-bold">3/4 (12)</button>
                <button onclick="setBarfiShare(4)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-200 border border-slate-700 font-bold">4/4 (16)</button>
            </div>
            <div id="barfiGrid" class="grid grid-cols-4 gap-2 w-44 h-44 bg-amber-950/40 p-2.5 rounded-2xl border-2 border-amber-600/40 shadow-inner">
                <!-- 16 barfis -->
            </div>
        </div>

        <!-- Ribbon Mode -->
        <div id="ribbonContainer" class="hidden w-full max-w-[320px] space-y-3">
            <div class="flex items-center justify-between text-xs font-semibold text-slate-300">
                <span>Total Length: 20 cm</span>
                <span class="text-cyan-400">Cut: 1/5 (4 cm)</span>
            </div>
            <div class="w-full flex h-8 rounded-lg overflow-hidden border border-slate-700">
                <div class="w-[20%] bg-rose-500/80 flex items-center justify-center text-[10px] font-bold text-white">Cut 4cm</div>
                <div class="w-[80%] bg-cyan-600/60 flex items-center justify-center text-xs font-bold text-cyan-100">Remaining 16 cm (4/5)</div>
            </div>
        </div>

        <div id="everydayDesc" class="text-xs text-center text-slate-300 font-semibold">
            Dividing 16 barfis among 4 people gives 4 barfis per 1/4 share.
        </div>
    </div>
</div>
"""

sim12 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Paper Folding Equivalence</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">1/3 = 2/6 & 1/2 = 2/4 = 4/8</span>
    </div>

    <!-- Equivalence Family Selector -->
    <div class="flex items-center justify-center gap-3">
        <button onclick="setEquivFamily('thirds')" id="btn-equiv-thirds" class="px-3.5 py-1.5 rounded-xl bg-blue-600 text-white font-bold text-xs shadow">Thirds (1/3 = 2/6)</button>
        <button onclick="setEquivFamily('halves')" id="btn-equiv-halves" class="px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700">Halves (1/2 = 2/4 = 4/8)</button>
    </div>

    <!-- Dynamic Equivalence Visualizer -->
    <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center gap-4 min-h-[220px]">
        <div id="equivStripsContainer" class="w-full max-w-[340px] space-y-3">
            <!-- Dynamically populated comparison strips -->
        </div>

        <div id="equivMathFormula" class="px-4 py-2 rounded-xl bg-blue-500/10 border border-blue-500/30 text-blue-300 text-xs font-mono font-bold text-center">
            (1 × 2) / (3 × 2) = 2/6
        </div>
    </div>
</div>
"""

sim13 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Interactive Fraction Chart Wall</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Vertical Alignment</span>
    </div>

    <!-- Align Guide Buttons -->
    <div class="flex items-center justify-between gap-2 flex-wrap">
        <span class="text-xs text-slate-400">Align Benchmark Line:</span>
        <div class="flex items-center gap-1.5">
            <button onclick="alignFractionWall(0.5)" class="px-2 py-0.5 rounded-lg bg-emerald-600 text-white font-bold text-xs">Align at 1/2</button>
            <button onclick="alignFractionWall(0.333)" class="px-2 py-0.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs hover:bg-slate-700">Align at 1/3</button>
            <button onclick="alignFractionWall(0.25)" class="px-2 py-0.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs hover:bg-slate-700">Align at 1/4</button>
            <button onclick="alignFractionWall(1.0)" class="px-2 py-0.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs hover:bg-slate-700">1 Whole</button>
        </div>
    </div>

    <!-- Fraction Wall Multi-Tiered Display -->
    <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 relative overflow-hidden min-h-[220px]">
        <!-- Alignment Red Guide Line -->
        <div id="fractionWallGuide" class="absolute top-0 bottom-0 w-0.5 bg-rose-500 z-10 transition-all duration-300 pointer-events-none" style="left: 50%;"></div>

        <div id="fractionWallTiers" class="space-y-1.5 text-[10px] font-bold">
            <!-- 1 Whole -->
            <div class="flex h-5 w-full bg-slate-800 border border-slate-600 rounded text-slate-200 items-center justify-center">1 Whole</div>
            <!-- Halves -->
            <div class="flex h-5 w-full gap-1">
                <div class="w-1/2 bg-amber-500/20 border border-amber-500/40 rounded flex items-center justify-center text-amber-300">1/2</div>
                <div class="w-1/2 bg-amber-500/20 border border-amber-500/40 rounded flex items-center justify-center text-amber-300">1/2</div>
            </div>
            <!-- Thirds -->
            <div class="flex h-5 w-full gap-1">
                <div class="w-1/3 bg-blue-500/20 border border-blue-500/40 rounded flex items-center justify-center text-blue-300">1/3</div>
                <div class="w-1/3 bg-blue-500/20 border border-blue-500/40 rounded flex items-center justify-center text-blue-300">1/3</div>
                <div class="w-1/3 bg-blue-500/20 border border-blue-500/40 rounded flex items-center justify-center text-blue-300">1/3</div>
            </div>
            <!-- Fourths -->
            <div class="flex h-5 w-full gap-1">
                <div class="w-1/4 bg-emerald-500/20 border border-emerald-500/40 rounded flex items-center justify-center text-emerald-300">1/4</div>
                <div class="w-1/4 bg-emerald-500/20 border border-emerald-500/40 rounded flex items-center justify-center text-emerald-300">1/4</div>
                <div class="w-1/4 bg-emerald-500/20 border border-emerald-500/40 rounded flex items-center justify-center text-emerald-300">1/4</div>
                <div class="w-1/4 bg-emerald-500/20 border border-emerald-500/40 rounded flex items-center justify-center text-emerald-300">1/4</div>
            </div>
            <!-- Sixths -->
            <div class="flex h-5 w-full gap-1">
                <div class="w-1/6 bg-indigo-500/20 border border-indigo-500/40 rounded flex items-center justify-center text-indigo-300">1/6</div>
                <div class="w-1/6 bg-indigo-500/20 border border-indigo-500/40 rounded flex items-center justify-center text-indigo-300">1/6</div>
                <div class="w-1/6 bg-indigo-500/20 border border-indigo-500/40 rounded flex items-center justify-center text-indigo-300">1/6</div>
                <div class="w-1/6 bg-indigo-500/20 border border-indigo-500/40 rounded flex items-center justify-center text-indigo-300">1/6</div>
                <div class="w-1/6 bg-indigo-500/20 border border-indigo-500/40 rounded flex items-center justify-center text-indigo-300">1/6</div>
                <div class="w-1/6 bg-indigo-500/20 border border-indigo-500/40 rounded flex items-center justify-center text-indigo-300">1/6</div>
            </div>
            <!-- Tenths -->
            <div class="flex h-5 w-full gap-0.5">
                <div class="w-[10%] bg-purple-500/20 border border-purple-500/40 rounded flex items-center justify-center text-purple-300 text-[9px]">1/10</div>
                <div class="w-[10%] bg-purple-500/20 border border-purple-500/40 rounded flex items-center justify-center text-purple-300 text-[9px]">1/10</div>
                <div class="w-[10%] bg-purple-500/20 border border-purple-500/40 rounded flex items-center justify-center text-purple-300 text-[9px]">1/10</div>
                <div class="w-[10%] bg-purple-500/20 border border-purple-500/40 rounded flex items-center justify-center text-purple-300 text-[9px]">1/10</div>
                <div class="w-[10%] bg-purple-500/20 border border-purple-500/40 rounded flex items-center justify-center text-purple-300 text-[9px]">1/10</div>
                <div class="w-[10%] bg-purple-500/20 border border-purple-500/40 rounded flex items-center justify-center text-purple-300 text-[9px]">1/10</div>
                <div class="w-[10%] bg-purple-500/20 border border-purple-500/40 rounded flex items-center justify-center text-purple-300 text-[9px]">1/10</div>
                <div class="w-[10%] bg-purple-500/20 border border-purple-500/40 rounded flex items-center justify-center text-purple-300 text-[9px]">1/10</div>
                <div class="w-[10%] bg-purple-500/20 border border-purple-500/40 rounded flex items-center justify-center text-purple-300 text-[9px]">1/10</div>
                <div class="w-[10%] bg-purple-500/20 border border-purple-500/40 rounded flex items-center justify-center text-purple-300 text-[9px]">1/10</div>
            </div>
        </div>

        <div id="fractionWallFeedback" class="mt-3 text-center text-xs font-semibold text-slate-300">
            Guide aligns at 1/2: Exactly equals 2/4, 3/6, and 5/10!
        </div>
    </div>
</div>
"""

sim14 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">12-Box Grid Shading Evaluator</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">Verify Claims</span>
    </div>

    <!-- Quick Presets -->
    <div class="flex items-center justify-between gap-2 flex-wrap text-xs">
        <span class="text-slate-400">Test Claim Presets:</span>
        <div class="flex items-center gap-1.5">
            <button onclick="setGridShadingPreset(4)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-bold">Claim: 1/3 (4 boxes)</button>
            <button onclick="setGridShadingPreset(3)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-bold">Claim: 1/4 (3 boxes)</button>
            <button onclick="setGridShadingPreset(6)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-bold">Claim: 1/2 (6 boxes)</button>
            <button onclick="clearGridShading()" class="px-2 py-1 rounded bg-rose-600/30 text-rose-300 border border-rose-500/40 font-bold">Clear</button>
        </div>
    </div>

    <!-- Interactive 12-Box Grid -->
    <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center gap-3 min-h-[220px]">
        <div id="grid12Boxes" class="grid grid-cols-4 gap-2 w-56 h-42">
            <!-- 12 clickable interactive boxes generated dynamically -->
        </div>

        <div class="flex items-center justify-between w-full max-w-[280px] text-xs font-bold pt-1">
            <span class="text-slate-400">Shaded Count: <span id="grid12Count" class="text-amber-400">4</span> / 12</span>
            <span id="grid12Status" class="text-emerald-400">Equals 1/3 (Valid Claim!)</span>
        </div>
    </div>
</div>
"""

sim15 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Composite Pattern Rangoli</h3>
        </div>
        <span class="text-xs text-pink-400 font-medium">16 Congruent Triangles</span>
    </div>

    <!-- Pattern Presets -->
    <div class="flex items-center justify-between gap-2 flex-wrap text-xs">
        <span class="text-slate-400">Preset Patterns:</span>
        <div class="flex items-center gap-1.5">
            <button onclick="setRangoliPreset('diamond')" class="px-2.5 py-1 rounded bg-pink-600 text-white font-bold">Center Diamond (8/16 = 1/2)</button>
            <button onclick="setRangoliPreset('corners')" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold">4 Corners (4/16 = 1/4)</button>
            <button onclick="setRangoliPreset('cross')" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold">Star Cross (12/16 = 3/4)</button>
        </div>
    </div>

    <!-- Rangoli SVG Display -->
    <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center gap-3 min-h-[220px]">
        <svg id="rangoliSvg" viewBox="0 0 160 160" class="w-40 h-40">
            <!-- 16 triangles rendered dynamically -->
        </svg>

        <div id="rangoliFractionText" class="text-xs font-bold text-center text-slate-300">
            Shaded Triangles: <span class="text-pink-400 font-black">8</span> / 16 = <span class="text-amber-400 font-black">1/2</span>
        </div>
    </div>
</div>
"""

sim16 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">18-Cell Target Shading Challenge</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Practice Precision</span>
    </div>

    <!-- Target Goal Selector -->
    <div class="flex items-center justify-between gap-2 flex-wrap text-xs">
        <span class="text-slate-400">Target Goal:</span>
        <div class="flex items-center gap-1.5">
            <button onclick="setShadeGoal(12, '2/3')" id="btn-goal-12" class="px-2.5 py-1 rounded bg-teal-600 text-white font-bold">Goal: 2/3 (12 cells)</button>
            <button onclick="setShadeGoal(6, '1/3')" id="btn-goal-6" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold">Goal: 1/3 (6 cells)</button>
            <button onclick="setShadeGoal(9, '1/2')" id="btn-goal-9" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold">Goal: 1/2 (9 cells)</button>
            <button onclick="reset18Cells()" class="px-2 py-1 rounded bg-rose-600/30 text-rose-300 border border-rose-500/40 font-bold">Reset</button>
        </div>
    </div>

    <!-- 18-Cell Clickable Grid -->
    <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center gap-3 min-h-[220px]">
        <div id="grid18Container" class="grid grid-cols-6 gap-2 w-64 h-32">
            <!-- 18 interactive cells -->
        </div>

        <div id="grid18Feedback" class="text-xs font-bold text-center text-slate-300">
            Current: <span id="grid18Count" class="text-teal-400">0</span> / 18 cells shaded. (Target: 12 cells for 2/3)
        </div>
    </div>
</div>
"""

simulators_part2 = {
    9: sim9,
    10: sim10,
    11: sim11,
    12: sim12,
    13: sim13,
    14: sim14,
    15: sim15,
    16: sim16
}

if __name__ == "__main__":
    assert len(simulators_part2) == 8
    print("Part 2 Simulators valid!")

