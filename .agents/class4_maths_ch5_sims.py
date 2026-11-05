# -*- coding: utf-8 -*-
"""Class 4 Mathematics Chapter 5 Simulators"""

simulators = {
    1: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">01</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Halves vs Quarters Comparison</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Interactive Paper Sheet</span>
    </div>

    <!-- Toggle Controls -->
    <div class="flex items-center justify-center gap-3">
        <button onclick="setPaperCompare('half')" id="btn-comp-half" class="px-3.5 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition shadow">1 Half (1/2)</button>
        <button onclick="setPaperCompare('two-quarters')" id="btn-comp-two-quarters" class="px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs transition border border-slate-700 hover:bg-slate-700">2 Quarters (2/4)</button>
        <button onclick="setPaperCompare('overlay')" id="btn-comp-overlay" class="px-3.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs transition border border-slate-700 hover:bg-slate-700">Overlay Side-by-Side</button>
    </div>

    <!-- Interactive SVG Display -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="paperCompareSvg" viewBox="0 0 360 180" class="w-full max-w-[340px] h-auto">
            <!-- Background Sheet -->
            <rect x="20" y="20" width="320" height="140" rx="8" fill="#1e293b" stroke="#475569" stroke-width="2"/>
            
            <!-- Half View (Default) -->
            <g id="paperHalfGroup">
                <rect x="20" y="20" width="160" height="140" rx="8" fill="#f59e0b" fill-opacity="0.35" stroke="#f59e0b" stroke-width="2"/>
                <line x1="180" y1="20" x2="180" y2="160" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 4"/>
                <text x="100" y="95" fill="#fef08a" font-size="14" font-weight="bold" text-anchor="middle">1/2 (One Half)</text>
                <text x="260" y="95" fill="#94a3b8" font-size="14" font-weight="bold" text-anchor="middle">1/2 (Unshaded)</text>
            </g>

            <!-- Two Quarters View -->
            <g id="paperQuartersGroup" class="hidden">
                <rect x="20" y="20" width="80" height="140" rx="4" fill="#38bdf8" fill-opacity="0.35" stroke="#38bdf8" stroke-width="2"/>
                <rect x="100" y="20" width="80" height="140" rx="4" fill="#38bdf8" fill-opacity="0.35" stroke="#38bdf8" stroke-width="2"/>
                <line x1="100" y1="20" x2="100" y2="160" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 3"/>
                <line x1="180" y1="20" x2="180" y2="160" stroke="#64748b" stroke-width="2"/>
                <line x1="260" y1="20" x2="260" y2="160" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3 3"/>
                <text x="60" y="95" fill="#bae6fd" font-size="12" font-weight="bold" text-anchor="middle">1/4</text>
                <text x="140" y="95" fill="#bae6fd" font-size="12" font-weight="bold" text-anchor="middle">1/4</text>
                <text x="220" y="95" fill="#64748b" font-size="12" font-weight="bold" text-anchor="middle">1/4</text>
                <text x="300" y="95" fill="#64748b" font-size="12" font-weight="bold" text-anchor="middle">1/4</text>
            </g>

            <!-- Overlay Comparison View -->
            <g id="paperOverlayGroup" class="hidden">
                <rect x="20" y="20" width="160" height="140" rx="8" fill="#f59e0b" fill-opacity="0.3" stroke="#f59e0b" stroke-width="2"/>
                <rect x="20" y="20" width="160" height="70" fill="#38bdf8" fill-opacity="0.3" stroke="#38bdf8" stroke-width="1.5"/>
                <line x1="180" y1="20" x2="180" y2="160" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 4"/>
                <text x="100" y="60" fill="#bae6fd" font-size="11" font-weight="bold" text-anchor="middle">Quarter 1 (1/4)</text>
                <text x="100" y="125" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">Quarter 2 (1/4)</text>
                <text x="260" y="95" fill="#94a3b8" font-size="13" font-weight="bold" text-anchor="middle">Equal Total Area!</text>
            </g>
        </svg>

        <div id="paperCompareDesc" class="mt-3 text-center text-xs font-semibold text-slate-300">
            One half (1/2) covers 50% of the rectangular sheet.
        </div>
    </div>
</div>
''',
    2: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">02</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Anatomy of a Fraction</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Numerator & Denominator</span>
    </div>

    <!-- Partition Selector -->
    <div class="flex items-center justify-between gap-2 flex-wrap">
        <span class="text-xs text-slate-300 font-medium">Select Denominator (Total Parts):</span>
        <div class="flex items-center gap-1.5">
            <button onclick="setFractionAnatomy(2)" id="btn-anat-2" class="px-2.5 py-1 rounded-lg bg-indigo-600 text-white font-bold text-xs">2 (Halves)</button>
            <button onclick="setFractionAnatomy(3)" id="btn-anat-3" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs hover:bg-slate-700">3 (Thirds)</button>
            <button onclick="setFractionAnatomy(4)" id="btn-anat-4" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs hover:bg-slate-700">4 (Quarters)</button>
            <button onclick="setFractionAnatomy(5)" id="btn-anat-5" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs hover:bg-slate-700">5 (Fifths)</button>
        </div>
    </div>

    <!-- Interactive Visual Representation -->
    <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center gap-4">
        <!-- Fraction Card Display -->
        <div class="flex items-center gap-6 bg-slate-900 border border-indigo-500/30 rounded-2xl px-6 py-3 shadow-inner">
            <div class="flex flex-col items-center">
                <span id="anatNumeratorText" class="text-2xl font-black text-amber-400">1</span>
                <div class="w-12 h-1 bg-slate-400 rounded-full my-1"></div>
                <span id="anatDenominatorText" class="text-2xl font-black text-indigo-400">2</span>
            </div>
            <div class="text-left space-y-1 text-xs">
                <div><span class="font-bold text-amber-400">Numerator (1):</span> <span class="text-slate-300">Shaded parts</span></div>
                <div><span class="font-bold text-indigo-400">Denominator (<span id="anatDenomLabel">2</span>):</span> <span class="text-slate-300">Total equal parts</span></div>
            </div>
        </div>

        <!-- Dynamic Strip Visualizer -->
        <div id="anatStripContainer" class="w-full max-w-[340px] flex h-14 rounded-xl overflow-hidden border-2 border-slate-700">
            <!-- Injected dynamically via setFractionAnatomy() -->
        </div>

        <p id="anatExplanation" class="text-xs text-center text-slate-300 font-medium">
            1 out of 2 equal parts is shaded, written as 1/2.
        </p>
    </div>
</div>
''',
    3: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">03</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Origami Paper Folding Lab</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Diverse Equal Folds</span>
    </div>

    <!-- Fold Pattern Selector -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setPaperFold('vertical')" id="btn-fold-vertical" class="px-2.5 py-1.5 rounded-xl bg-emerald-500 text-slate-950 font-bold text-xs shadow">Vertical (1/2)</button>
        <button onclick="setPaperFold('horizontal')" id="btn-fold-horizontal" class="px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700">Horizontal (1/2)</button>
        <button onclick="setPaperFold('diagonal')" id="btn-fold-diagonal" class="px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700">Diagonal (1/2)</button>
        <button onclick="setPaperFold('quarters')" id="btn-fold-quarters" class="px-2.5 py-1.5 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700">Grid (1/4)</button>
    </div>

    <!-- Fold Simulation SVG -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <svg id="paperFoldSvg" viewBox="0 0 340 180" class="w-full max-w-[320px] h-auto">
            <!-- Background Sheet -->
            <rect x="20" y="20" width="300" height="140" rx="6" fill="#1e293b" stroke="#475569" stroke-width="2"/>
            
            <!-- Dynamic Fold Overlay -->
            <g id="foldDisplayGroup">
                <!-- Vertical Fold (Default) -->
                <rect x="20" y="20" width="150" height="140" rx="6" fill="#10b981" fill-opacity="0.35" stroke="#10b981" stroke-width="2"/>
                <line x1="170" y1="20" x2="170" y2="160" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="5 5"/>
                <text x="95" y="95" fill="#6ee7b7" font-size="14" font-weight="bold" text-anchor="middle">1/2 Shaded</text>
                <text x="245" y="95" fill="#94a3b8" font-size="14" font-weight="bold" text-anchor="middle">1/2 Plain</text>
            </g>
        </svg>

        <div id="foldDesc" class="mt-3 text-center text-xs font-semibold text-slate-300">
            Vertical midline crease splits the rectangle into two identical tall halves.
        </div>
    </div>
</div>
''',
    4: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">04</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Steamed Dhokla Sharing Tray</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Sequential Diners</span>
    </div>

    <!-- Guest Controller -->
    <div class="flex items-center justify-between gap-3 flex-wrap">
        <div class="flex items-center gap-2">
            <span class="text-xs text-slate-300 font-medium">Guests at Table:</span>
            <span id="dhoklaGuestCount" class="px-2.5 py-0.5 rounded-md bg-amber-500/20 text-amber-300 font-black text-sm border border-amber-500/30">2</span>
        </div>
        <div class="flex items-center gap-1.5">
            <button onclick="changeDhoklaGuests(2)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs text-slate-200 font-bold border border-slate-700">2 (1/2)</button>
            <button onclick="changeDhoklaGuests(3)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs text-slate-200 font-bold border border-slate-700">3 (1/3)</button>
            <button onclick="changeDhoklaGuests(4)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs text-slate-200 font-bold border border-slate-700">4 (1/4)</button>
            <button onclick="changeDhoklaGuests(5)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs text-slate-200 font-bold border border-slate-700">5 (1/5)</button>
            <button onclick="passDhoklaShare()" id="btnPassShare" class="px-2.5 py-1 rounded bg-indigo-600 hover:bg-indigo-500 text-xs text-white font-bold transition shadow">Pass 1 Share (2/5)</button>
        </div>
    </div>

    <!-- Dhokla Tray Display -->
    <div class="bg-slate-950/80 rounded-xl p-4 flex flex-col items-center justify-center border border-slate-800 min-h-[220px]">
        <div id="dhoklaTray" class="w-full max-w-[320px] h-28 rounded-xl bg-amber-400/20 border-2 border-amber-500/40 p-2 flex gap-1.5 shadow-inner">
            <!-- Injected dynamically via changeDhoklaGuests() -->
        </div>

        <div id="dhoklaStatus" class="mt-4 text-center text-xs font-semibold text-slate-200">
            Shared equally among 2 guests. Each guest receives exactly <span class="text-amber-400 font-bold">1/2</span> of the platter.
        </div>
    </div>
</div>
''',
    5: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-rose-500/20 text-rose-300 font-bold flex items-center justify-center text-sm">05</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Inverse Sharing Law Simulator</h3>
        </div>
        <span class="text-xs text-rose-400 font-medium">Denominator vs Piece Size</span>
    </div>

    <!-- Slider Control -->
    <div class="space-y-2">
        <div class="flex items-center justify-between text-xs font-medium text-slate-300">
            <span>Divide Whole Among Diners (Denominator N):</span>
            <span id="denomSliderVal" class="text-base font-black text-rose-400">2</span>
        </div>
        <input type="range" id="denomSlider" min="2" max="10" value="2" oninput="updateDenomSlider(this.value)" class="w-full accent-rose-500 cursor-pointer">
    </div>

    <!-- Visual Comparison Display -->
    <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col sm:flex-row items-center justify-around gap-4 min-h-[200px]">
        <!-- Circular Fraction Disc -->
        <div class="flex flex-col items-center gap-2">
            <svg id="denomCircleSvg" viewBox="0 0 120 120" class="w-24 h-24">
                <!-- Dynamically drawn slice in JS -->
            </svg>
            <span class="text-[11px] font-bold text-slate-400">Circular Slice</span>
        </div>

        <!-- Linear Fraction Strip -->
        <div class="w-full sm:w-1/2 space-y-2">
            <div class="flex items-center justify-between text-xs">
                <span class="text-slate-400">Single Share Size:</span>
                <span id="denomFractionText" class="font-black text-rose-400 text-sm">1/2 (50.0%)</span>
            </div>
            <div class="w-full bg-slate-800 h-6 rounded-lg overflow-hidden border border-slate-700">
                <div id="denomProgressBar" class="bg-gradient-to-r from-rose-500 to-amber-500 h-full w-[50%] transition-all duration-200"></div>
            </div>
            <p class="text-[11px] text-slate-400 italic">Notice: Larger denominator = Smaller slice!</p>
        </div>
    </div>
</div>
''',
    6: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-300 font-bold flex items-center justify-center text-sm">06</span>
            <h3 class="font-bold text-white text-sm sm:text-base">5-Bed Flower Garden Plot</h3>
        </div>
        <span class="text-xs text-pink-400 font-medium">Combining Fifths</span>
    </div>

    <!-- Interactive Bed Planting Buttons -->
    <div class="flex items-center justify-between gap-1 flex-wrap">
        <button onclick="toggleGardenBed(0)" id="bed-btn-0" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700">🌹 1. Rose</button>
        <button onclick="toggleGardenBed(1)" id="bed-btn-1" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700">🌼 2. Mogra</button>
        <button onclick="toggleGardenBed(2)" id="bed-btn-2" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700">🌸 3. Lily</button>
        <button onclick="toggleGardenBed(3)" id="bed-btn-3" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700">🌻 4. Marigold</button>
        <button onclick="toggleGardenBed(4)" id="bed-btn-4" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 border border-slate-700">🌺 5. Jasmine</button>
    </div>

    <!-- Garden Visualizer -->
    <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center gap-3">
        <div class="w-full max-w-[340px] grid grid-cols-5 gap-2 h-24">
            <div id="garden-plot-0" class="rounded-xl border-2 border-dashed border-slate-700 flex flex-col items-center justify-center text-xs text-slate-500 font-bold transition">Bed 1<span class="text-[10px]">1/5</span></div>
            <div id="garden-plot-1" class="rounded-xl border-2 border-dashed border-slate-700 flex flex-col items-center justify-center text-xs text-slate-500 font-bold transition">Bed 2<span class="text-[10px]">1/5</span></div>
            <div id="garden-plot-2" class="rounded-xl border-2 border-dashed border-slate-700 flex flex-col items-center justify-center text-xs text-slate-500 font-bold transition">Bed 3<span class="text-[10px]">1/5</span></div>
            <div id="garden-plot-3" class="rounded-xl border-2 border-dashed border-slate-700 flex flex-col items-center justify-center text-xs text-slate-500 font-bold transition">Bed 4<span class="text-[10px]">1/5</span></div>
            <div id="garden-plot-4" class="rounded-xl border-2 border-dashed border-slate-700 flex flex-col items-center justify-center text-xs text-slate-500 font-bold transition">Bed 5<span class="text-[10px]">1/5</span></div>
        </div>

        <div class="flex items-center justify-between w-full max-w-[340px] px-2 text-xs font-bold">
            <span class="text-slate-400">Total Cultivated Fraction:</span>
            <span id="gardenFractionDisplay" class="text-pink-400 text-sm">0/5 (Empty)</span>
        </div>
    </div>
</div>
''',
    7: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">07</span>
            <h3 class="font-bold text-white text-sm sm:text-base">7-Strip Flower Garden Planner</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">Sevenths Denominator</span>
    </div>

    <!-- Strip Allocation Sliders -->
    <div class="grid grid-cols-3 gap-3 text-xs">
        <div class="space-y-1">
            <div class="flex justify-between text-rose-400 font-semibold"><span>Roses:</span><span id="stripValRoses">2/7</span></div>
            <input type="range" id="sliderRoses" min="0" max="7" value="2" oninput="updateSeventhGarden()" class="w-full accent-rose-500 cursor-pointer">
        </div>
        <div class="space-y-1">
            <div class="flex justify-between text-amber-400 font-semibold"><span>Sunflowers:</span><span id="stripValSun">3/7</span></div>
            <input type="range" id="sliderSun" min="0" max="7" value="3" oninput="updateSeventhGarden()" class="w-full accent-amber-500 cursor-pointer">
        </div>
        <div class="space-y-1">
            <div class="flex justify-between text-indigo-400 font-semibold"><span>Lavender:</span><span id="stripValLav">2/7</span></div>
            <input type="range" id="sliderLav" min="0" max="7" value="2" oninput="updateSeventhGarden()" class="w-full accent-indigo-500 cursor-pointer">
        </div>
    </div>

    <!-- 7-Strip Garden Visualizer -->
    <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center gap-3">
        <div id="seventhStripsContainer" class="w-full max-w-[340px] flex h-16 rounded-xl overflow-hidden border-2 border-slate-700">
            <!-- 7 strips generated dynamically -->
        </div>

        <div id="seventhSumText" class="text-xs font-bold text-center text-slate-300">
            2/7 (Roses) + 3/7 (Sunflowers) + 2/7 (Lavender) = <span class="text-teal-400 font-black">7/7 (1 Whole Garden)</span>
        </div>
    </div>
</div>
''',
    8: '''
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-300 font-bold flex items-center justify-center text-sm">08</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Dream Dosa Topping Designer</h3>
        </div>
        <span class="text-xs text-orange-400 font-medium">Circular Slices</span>
    </div>

    <!-- Mode Selector -->
    <div class="flex items-center justify-between gap-2 flex-wrap">
        <span class="text-xs text-slate-300 font-medium">Select Partition Mode:</span>
        <div class="flex items-center gap-2">
            <button onclick="setDosaMode(3)" id="btn-dosa-3" class="px-3 py-1 rounded-xl bg-orange-500 text-slate-950 font-bold text-xs shadow">3 Slices (Thirds)</button>
            <button onclick="setDosaMode(8)" id="btn-dosa-8" class="px-3 py-1 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-700">8 Slices (Eighths)</button>
        </div>
    </div>

    <!-- Dosa Visualizer -->
    <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex flex-col sm:flex-row items-center justify-around gap-4 min-h-[220px]">
        <svg id="dosaSvg" viewBox="0 0 160 160" class="w-36 h-36">
            <!-- Rendered dynamically in JS -->
        </svg>

        <div id="dosaLegend" class="space-y-1.5 text-xs text-slate-300">
            <!-- Injected via setDosaMode() -->
        </div>
    </div>
</div>
''',
    9: '''
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
''',
    10: '''
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
''',
    11: '''
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
''',
    12: '''
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
''',
    13: '''
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
''',
    14: '''
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
''',
    15: '''
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
''',
    16: '''
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
''',
}
