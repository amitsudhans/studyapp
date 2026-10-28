import json

sims = {
    # 1. Fraction Anatomy Studio
    "sim-fraction-visualizer": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Fraction Anatomy Studio</span>
                <span id="fvTypeBadge" class="px-2 py-0.5 text-xs font-bold rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">Proper Fraction</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 items-center">
                <!-- SVG Canvas -->
                <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                    <svg id="fvSvg" viewBox="0 0 240 200" class="w-full h-full">
                        <!-- Dynamic pie / bar drawn by JS -->
                    </svg>
                </div>
                <!-- Controls & Stats -->
                <div class="flex flex-col gap-2.5 text-xs">
                    <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
                        <div class="flex justify-between items-center mb-1">
                            <span class="text-slate-400">Numerator (Parts Chosen, $a$):</span>
                            <span id="fvNumVal" class="text-amber-400 font-bold font-mono text-sm">3</span>
                        </div>
                        <input id="fvNumSlider" type="range" min="1" max="12" value="3" oninput="updateFractionVisualizer()" class="w-full accent-amber-500">
                    </div>
                    <div class="bg-slate-800/80 p-2.5 rounded-lg border border-slate-700">
                        <div class="flex justify-between items-center mb-1">
                            <span class="text-slate-400">Denominator (Total Equal Parts, $b$):</span>
                            <span id="fvDenVal" class="text-cyan-400 font-bold font-mono text-sm">4</span>
                        </div>
                        <input id="fvDenSlider" type="range" min="1" max="12" value="4" oninput="updateFractionVisualizer()" class="w-full accent-cyan-500">
                    </div>
                    <div class="grid grid-cols-2 gap-2 text-center">
                        <div class="p-2 bg-slate-800/60 rounded border border-slate-700">
                            <span class="text-slate-400 block text-[10px]">FRACTION</span>
                            <span id="fvFractionDisp" class="text-amber-300 font-bold font-mono text-base">3 / 4</span>
                        </div>
                        <div class="p-2 bg-slate-800/60 rounded border border-slate-700">
                            <span class="text-slate-400 block text-[10px]">DECIMAL VALUE</span>
                            <span id="fvDecimalDisp" class="text-cyan-300 font-bold font-mono text-base">0.75</span>
                        </div>
                    </div>
                    <div class="flex gap-2">
                        <button onclick="setFvView('pie')" id="fvPieBtn" class="flex-1 py-1 font-semibold rounded bg-amber-500/30 text-amber-200 border border-amber-500/50">Circle / Pie</button>
                        <button onclick="setFvView('bar')" id="fvBarBtn" class="flex-1 py-1 font-semibold rounded bg-slate-800 text-slate-300 border border-slate-700">Strip / Bar</button>
                    </div>
                </div>
            </div>
            <div id="fvNarration" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800">
                Numerator 3 represents 3 shaded parts out of 4 total equal divisions. Since $3 < 4$, this is a <strong>Proper Fraction</strong> ($< 1$).
            </div>
        </div>
    """,

    # 2. Repeated Addition
    "sim-repeated-addition": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Whole Number &times; Fraction via Repeated Jumps</span>
                <span class="text-xs font-mono text-amber-300">$n \times \\frac{a}{b} = \\frac{n \times a}{b}$</span>
            </div>
            <div class="relative w-full h-52 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="raSvg" viewBox="0 0 520 180" class="w-full h-full">
                    <!-- Dynamic jumps on number line drawn by JS -->
                </svg>
            </div>
            <div class="mt-3 grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                <div class="flex flex-col gap-2">
                    <div class="flex items-center justify-between">
                        <span class="text-slate-300 font-medium">Multiplier Whole Number ($n$):</span>
                        <span id="raNVal" class="text-amber-400 font-bold font-mono text-sm">3</span>
                    </div>
                    <input id="raNSlider" type="range" min="1" max="6" value="3" oninput="updateRepeatedAddition()" class="w-full accent-amber-500">
                    <div class="flex items-center justify-between">
                        <span class="text-slate-300 font-medium">Fraction Step Size ($\\frac{a}{b}$):</span>
                        <div class="flex gap-1.5">
                            <button onclick="setRaFraction(1, 4)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-700">1/4</button>
                            <button onclick="setRaFraction(2, 5)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-700">2/5</button>
                            <button onclick="setRaFraction(3, 8)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-700">3/8</button>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 bg-slate-800/80 rounded-lg border border-slate-700 flex flex-col justify-center">
                    <div class="text-slate-300 text-xs">
                        Repeated Addition: <span id="raSumExpr" class="text-amber-300 font-mono font-bold">2/5 + 2/5 + 2/5</span>
                    </div>
                    <div class="mt-1 text-sm font-bold text-cyan-300 font-mono">
                        Product: <span id="raProductExpr">3 &times; (2/5) = 6/5 = 1 1/5</span>
                    </div>
                    <div class="mt-1 text-[11px] text-slate-400" id="raTip">
                        Each jump advances 2 fifths. 3 jumps land at 6 fifths!
                    </div>
                </div>
            </div>
        </div>
    """,

    # 3. Fraction of a Fraction
    "sim-fraction-of-fraction": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">The "Of" Operator: Fraction of a Fraction</span>
                <span class="text-xs font-mono text-cyan-300">$\\frac{1}{2}\\text{ of }\\frac{3}{4} = \\frac{1 \\times 3}{2 \\times 4} = \\frac{3}{8}$</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 items-center">
                <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                    <svg id="fofSvg" viewBox="0 0 240 200" class="w-full h-full">
                        <!-- 2-Stage visual partition -->
                    </svg>
                </div>
                <div class="flex flex-col gap-2.5 text-xs">
                    <div class="p-2 bg-slate-800/70 rounded border border-slate-700">
                        <span class="text-slate-400 block text-[11px] mb-1 font-bold">Step 1: Base Fraction (Horizontal Slices)</span>
                        <div class="flex gap-2">
                            <button onclick="setFofBase(1, 2)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-200 border border-slate-600">1/2</button>
                            <button onclick="setFofBase(3, 4)" class="px-2 py-1 bg-amber-500/30 text-amber-300 rounded border border-amber-500/50">3/4</button>
                            <button onclick="setFofBase(2, 3)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-200 border border-slate-600">2/3</button>
                            <button onclick="setFofBase(4, 5)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-200 border border-slate-600">4/5</button>
                        </div>
                    </div>
                    <div class="p-2 bg-slate-800/70 rounded border border-slate-700">
                        <span class="text-slate-400 block text-[11px] mb-1 font-bold">Step 2: Take Portion "Of" It (Vertical Cut)</span>
                        <div class="flex gap-2">
                            <button onclick="setFofPortion(1, 2)" class="px-2 py-1 bg-cyan-500/30 text-cyan-300 rounded border border-cyan-500/50">1/2 of it</button>
                            <button onclick="setFofPortion(1, 3)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-200 border border-slate-600">1/3 of it</button>
                            <button onclick="setFofPortion(2, 3)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-slate-200 border border-slate-600">2/3 of it</button>
                        </div>
                    </div>
                    <div class="p-2 bg-slate-900 rounded border border-amber-500/40 text-center">
                        <span class="text-slate-400 text-[10px] block">INTERSECTING OVERLAP REGION</span>
                        <span id="fofResult" class="text-amber-300 font-bold font-mono text-sm">1/2 of 3/4 = 3/8</span>
                    </div>
                </div>
            </div>
            <div id="fofDesc" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800">
                Notice how taking a fraction <em>of</em> an existing fraction creates smaller double-cut cells!
            </div>
        </div>
    """,

    # 4. Unit Square Grid Area Model
    "sim-unit-square-grid": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Unit Square Area Model</span>
                <span class="text-xs font-mono text-amber-300">Area = Length &times; Breadth</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 items-center">
                <div class="relative w-full h-60 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                    <svg id="usgSvg" viewBox="0 0 240 220" class="w-full h-full">
                        <!-- Unit square 1x1 with dynamic grid -->
                    </svg>
                </div>
                <div class="flex flex-col gap-2.5 text-xs">
                    <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                        <div class="flex justify-between items-center mb-1">
                            <span class="text-cyan-300">Length ($a/b$):</span>
                            <span id="usgLenTxt" class="font-bold font-mono text-cyan-300">2 / 3</span>
                        </div>
                        <div class="flex gap-2">
                            <input id="usgASlider" type="range" min="1" max="5" value="2" oninput="updateUnitSquareGrid()" class="w-1/2 accent-cyan-400" title="Numerator a">
                            <input id="usgBSlider" type="range" min="2" max="6" value="3" oninput="updateUnitSquareGrid()" class="w-1/2 accent-cyan-600" title="Denominator b">
                        </div>
                    </div>
                    <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                        <div class="flex justify-between items-center mb-1">
                            <span class="text-amber-300">Breadth ($c/d$):</span>
                            <span id="usgBrdTxt" class="font-bold font-mono text-amber-300">3 / 5</span>
                        </div>
                        <div class="flex gap-2">
                            <input id="usgCSlider" type="range" min="1" max="5" value="3" oninput="updateUnitSquareGrid()" class="w-1/2 accent-amber-400" title="Numerator c">
                            <input id="usgDSlider" type="range" min="2" max="6" value="5" oninput="updateUnitSquareGrid()" class="w-1/2 accent-amber-600" title="Denominator d">
                        </div>
                    </div>
                    <div class="p-2.5 bg-slate-900 rounded border border-amber-500/40">
                        <div class="text-slate-400 text-[10px]">TOTAL EQUAL CELLS: <span id="usgTotalCells" class="text-slate-200 font-bold font-mono">15</span></div>
                        <div class="text-slate-400 text-[10px]">SHADED RECTANGLE CELLS: <span id="usgShadedCells" class="text-emerald-400 font-bold font-mono">6</span></div>
                        <div class="mt-1 text-sm font-bold text-amber-300 font-mono" id="usgAreaFormula">
                            Area = (2&times;3) / (3&times;5) = 6/15 = 2/5
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """,

    # 5. Brahmagupta's Product Formula
    "sim-brahmagupta-product": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Brahmagupta's Product Law Engine (c. 628 CE)</span>
                <span class="text-xs font-mono text-amber-300">$\\frac{a}{b} \\times \\frac{c}{d} = \\frac{a \\times c}{b \\times d}$</span>
            </div>
            <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col items-center justify-center">
                <!-- Dynamic Equation Display -->
                <div class="flex items-center gap-3 sm:gap-6 font-mono text-base sm:text-xl">
                    <!-- Fraction 1 -->
                    <div class="flex flex-col items-center">
                        <input id="bgNum1" type="number" min="1" max="30" value="3" oninput="calcBrahmaguptaProduct()" class="w-12 sm:w-16 bg-slate-800 text-amber-300 font-bold text-center rounded border border-slate-700 p-1">
                        <div class="w-full h-0.5 bg-amber-400 my-1"></div>
                        <input id="bgDen1" type="number" min="1" max="30" value="4" oninput="calcBrahmaguptaProduct()" class="w-12 sm:w-16 bg-slate-800 text-amber-300 font-bold text-center rounded border border-slate-700 p-1">
                    </div>
                    <span class="text-slate-400 font-bold text-2xl">&times;</span>
                    <!-- Fraction 2 -->
                    <div class="flex flex-col items-center">
                        <input id="bgNum2" type="number" min="1" max="30" value="5" oninput="calcBrahmaguptaProduct()" class="w-12 sm:w-16 bg-cyan-300 font-bold text-center rounded border border-slate-700 p-1">
                        <div class="w-full h-0.5 bg-cyan-400 my-1"></div>
                        <input id="bgDen2" type="number" min="1" max="30" value="7" oninput="calcBrahmaguptaProduct()" class="w-12 sm:w-16 bg-cyan-300 font-bold text-center rounded border border-slate-700 p-1">
                    </div>
                    <span class="text-slate-400 font-bold text-2xl">=</span>
                    <!-- Unsimplified Product -->
                    <div class="flex flex-col items-center text-slate-200">
                        <span id="bgProdNum" class="font-bold text-amber-400">15</span>
                        <div class="w-full h-0.5 bg-slate-500 my-1"></div>
                        <span id="bgProdDen" class="font-bold text-cyan-400">28</span>
                    </div>
                    <span class="text-slate-400 font-bold text-2xl" id="bgEqSym">=</span>
                    <!-- Simplified Product -->
                    <div class="flex flex-col items-center p-2 bg-amber-500/10 rounded-lg border border-amber-500/40">
                        <span id="bgSimpNum" class="font-bold text-emerald-400">15</span>
                        <div class="w-full h-0.5 bg-emerald-400 my-1"></div>
                        <span id="bgSimpDen" class="font-bold text-emerald-400">28</span>
                    </div>
                </div>
            </div>
            <div class="mt-3 grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
                <button onclick="setBgPreset(2, 3, 3, 4)" class="p-2 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-slate-200">
                    Try 2/3 &times; 3/4 (Simplifies!)
                </button>
                <button onclick="setBgPreset(5, 6, 9, 10)" class="p-2 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-slate-200">
                    Try 5/6 &times; 9/10 (Common Factors)
                </button>
                <button onclick="setBgPreset(7, 2, 4, 21)" class="p-2 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-slate-200">
                    Try 7/2 &times; 4/21 (Improper &times; Proper)
                </button>
            </div>
            <div id="bgExplanation" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800">
                Brahmagupta's Rule: Multiply numerators together ($3 \times 5 = 15$) and denominators together ($4 \times 7 = 28$).
            </div>
        </div>
    """,

    # 6. Cross-Cancelling Studio
    "sim-cross-cancelling": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Cross-Cancelling Factor Slasher</span>
                <span class="text-xs font-mono text-cyan-300">Simplify BEFORE you multiply!</span>
            </div>
            <div class="p-4 bg-slate-950 rounded-xl border border-slate-800 flex flex-col items-center">
                <!-- Visual Cross Canvas -->
                <div class="flex items-center gap-6 font-mono text-xl relative">
                    <!-- Fraction A -->
                    <div class="flex flex-col items-center">
                        <div class="relative">
                            <span id="ccA1" class="text-amber-300 font-bold text-2xl">3</span>
                            <span id="ccSlashA1" class="hidden absolute inset-0 text-rose-500 font-bold text-2xl line-through">/</span>
                            <span id="ccSubA1" class="hidden text-xs text-emerald-400 block font-bold">1</span>
                        </div>
                        <div class="w-12 h-0.5 bg-slate-600 my-1"></div>
                        <div class="relative">
                            <span id="ccB1" class="text-slate-300 font-bold text-2xl">8</span>
                            <span id="ccSlashB1" class="hidden absolute inset-0 text-rose-500 font-bold text-2xl line-through">/</span>
                            <span id="ccSubB1" class="hidden text-xs text-emerald-400 block font-bold">2</span>
                        </div>
                    </div>
                    <span class="text-slate-500 font-bold text-2xl">&times;</span>
                    <!-- Fraction B -->
                    <div class="flex flex-col items-center">
                        <div class="relative">
                            <span id="ccA2" class="text-slate-300 font-bold text-2xl">4</span>
                            <span id="ccSlashA2" class="hidden absolute inset-0 text-rose-500 font-bold text-2xl line-through">/</span>
                            <span id="ccSubA2" class="hidden text-xs text-emerald-400 block font-bold">1</span>
                        </div>
                        <div class="w-12 h-0.5 bg-slate-600 my-1"></div>
                        <div class="relative">
                            <span id="ccB2" class="text-cyan-300 font-bold text-2xl">9</span>
                            <span id="ccSlashB2" class="hidden absolute inset-0 text-rose-500 font-bold text-2xl line-through">/</span>
                            <span id="ccSubB2" class="hidden text-xs text-emerald-400 block font-bold">3</span>
                        </div>
                    </div>
                    <span class="text-slate-500 font-bold text-2xl">&rarr;</span>
                    <!-- Product Result -->
                    <div class="flex flex-col items-center p-2 bg-emerald-500/10 rounded-lg border border-emerald-500/40">
                        <span id="ccResNum" class="text-emerald-400 font-bold text-2xl">1</span>
                        <div class="w-10 h-0.5 bg-emerald-400 my-1"></div>
                        <span id="ccResDen" class="text-emerald-400 font-bold text-2xl">6</span>
                    </div>
                </div>
            </div>
            <div class="mt-3 flex flex-wrap gap-2 justify-center text-xs">
                <button onclick="setCcProblem(3, 8, 4, 9)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-slate-200">
                    Example 1: 3/8 &times; 4/9
                </button>
                <button onclick="setCcProblem(5, 12, 4, 15)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-slate-200">
                    Example 2: 5/12 &times; 4/15
                </button>
                <button onclick="setCcProblem(7, 10, 5, 14)" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-slate-200">
                    Example 3: 7/10 &times; 5/14
                </button>
                <button onclick="animateCrossCancel()" class="px-4 py-1.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded shadow">
                    &check; Slash Common Factors!
                </button>
            </div>
            <div id="ccStatusText" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800 text-center">
                Click <strong>Slash Common Factors</strong> to see GCD cancellations along diagonals (3 with 9, 4 with 8)!
            </div>
        </div>
    """,

    # 7. Product Size Comparator
    "sim-product-size-comparator": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Product Size vs Factor Scale</span>
                <span id="pscCategoryBadge" class="text-xs font-bold px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/40">Proper &times; Proper</span>
            </div>
            <div class="relative w-full h-52 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="pscSvg" viewBox="0 0 500 180" class="w-full h-full">
                    <!-- Balance scale and comparison rods -->
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-1 md:grid-cols-3 gap-2 text-xs">
                <button onclick="setPscCase('proper_proper')" class="p-2 bg-slate-800 hover:bg-slate-700 text-left rounded border border-slate-700">
                    <span class="font-bold text-amber-300 block">Case 1: Proper &times; Proper</span>
                    <span class="text-slate-400 text-[10px]">Product is LESS than BOTH factors! (e.g. 1/2 &times; 3/4 = 3/8)</span>
                </button>
                <button onclick="setPscCase('proper_improper')" class="p-2 bg-slate-800 hover:bg-slate-700 text-left rounded border border-slate-700">
                    <span class="font-bold text-cyan-300 block">Case 2: Proper &times; Improper</span>
                    <span class="text-slate-400 text-[10px]">Product is in BETWEEN the two factors! (e.g. 2/3 &times; 5/2 = 5/3)</span>
                </button>
                <button onclick="setPscCase('improper_improper')" class="p-2 bg-slate-800 hover:bg-slate-700 text-left rounded border border-slate-700">
                    <span class="font-bold text-emerald-300 block">Case 3: Improper &times; Improper</span>
                    <span class="text-slate-400 text-[10px]">Product is GREATER than BOTH factors! (e.g. 3/2 &times; 4/3 = 2)</span>
                </button>
            </div>
            <div id="pscVerdict" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800 text-center font-mono">
                $3/8 < 1/2$ and $3/8 < 3/4$. Multiplication by a fraction $< 1$ shrinks the value!
            </div>
        </div>
    """,

    # 8. Commutativity Rotator
    "sim-commutativity-rotator": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Commutative Property: $90^\\circ$ Rotation Studio</span>
                <span class="text-xs font-mono text-amber-300">$\\frac{a}{b} \\times \\frac{c}{d} = \\frac{c}{d} \\times \\frac{a}{b}$</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="crSvg" viewBox="0 0 460 200" class="w-full h-full">
                    <!-- Dual grid or rotating grid showing commutativity -->
                </svg>
            </div>
            <div class="mt-2 flex flex-wrap items-center justify-between gap-2 text-xs">
                <div class="flex items-center gap-2">
                    <button onclick="rotateCommutativity()" class="px-3 py-1.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded shadow flex items-center gap-1">
                        <span>&#x21bb;</span> Rotate 90&deg;
                    </button>
                    <span id="crAngleLabel" class="text-slate-400 font-mono">Rotation: 0&deg;</span>
                </div>
                <div class="p-1.5 bg-slate-800 rounded border border-slate-700 font-mono text-amber-300" id="crFormulaText">
                    (2/3) &times; (3/4) = 6/12 = 1/2
                </div>
            </div>
            <div class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800">
                Whether you take 2 thirds of 3 fourths or 3 fourths of 2 thirds, the area of the overlapping shaded region remains identically $6/12$ of the square!
            </div>
        </div>
    """,

    # 9. Reciprocal Multiplicative Inverse
    "sim-reciprocal-flip": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Reciprocal & Multiplicative Inverse Flipper</span>
                <span class="text-xs font-mono text-amber-300">$\\frac{a}{b} \\times \\frac{b}{a} = 1$</span>
            </div>
            <div class="p-4 bg-slate-950 rounded-xl border border-slate-800 flex flex-col items-center">
                <!-- Visual Flipper Box -->
                <div class="flex items-center gap-4 sm:gap-8 font-mono">
                    <!-- Original Fraction -->
                    <div id="rfBoxOrig" class="flex flex-col items-center p-3 bg-slate-800 rounded-xl border border-amber-500/40 transition-transform duration-500">
                        <span id="rfNum" class="text-2xl font-bold text-amber-300">3</span>
                        <div class="w-12 h-0.5 bg-slate-500 my-1"></div>
                        <span id="rfDen" class="text-2xl font-bold text-cyan-300">7</span>
                    </div>
                    <span class="text-slate-500 font-bold text-2xl">&times;</span>
                    <!-- Inverted Fraction -->
                    <div id="rfBoxFlip" class="flex flex-col items-center p-3 bg-slate-800 rounded-xl border border-cyan-500/40 transition-transform duration-500">
                        <span id="rfInvNum" class="text-2xl font-bold text-cyan-300">7</span>
                        <div class="w-12 h-0.5 bg-slate-500 my-1"></div>
                        <span id="rfInvDen" class="text-2xl font-bold text-amber-300">3</span>
                    </div>
                    <span class="text-slate-500 font-bold text-2xl">=</span>
                    <!-- 1.0 Fulcrum -->
                    <div class="flex flex-col items-center p-3 bg-emerald-500/20 rounded-xl border border-emerald-500/50">
                        <span class="text-3xl font-extrabold text-emerald-300">1</span>
                        <span class="text-[10px] text-emerald-400 mt-0.5">PERFECT BALANCE</span>
                    </div>
                </div>
            </div>
            <div class="mt-3 grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
                <button onclick="setReciprocalFraction(3, 7)" class="p-1.5 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-slate-200">
                    3/7 &rarr; 7/3
                </button>
                <button onclick="setReciprocalFraction(1, 5)" class="p-1.5 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-slate-200">
                    1/5 &rarr; 5/1 (5)
                </button>
                <button onclick="setReciprocalFraction(9, 1)" class="p-1.5 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-slate-200">
                    9 &rarr; 1/9
                </button>
                <button onclick="triggerZeroReciprocalWarning()" class="p-1.5 bg-rose-900/30 hover:bg-rose-900/50 text-rose-300 rounded border border-rose-700">
                    What about 0?
                </button>
            </div>
            <div id="rfNotice" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800">
                Multiplying any non-zero number by its reciprocal yields <strong>1</strong>. Zero has no reciprocal because $1/0$ is undefined!
            </div>
        </div>
    """,

    # 10. Fraction Division as Grouping
    "sim-division-grouping": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Division as Equal Sharing & Grouping</span>
                <span class="text-xs font-mono text-cyan-300">"How many portions fit inside?"</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="dgSvg" viewBox="0 0 500 200" class="w-full h-full">
                    <!-- Cakes or strip divided into fractional pieces -->
                </svg>
            </div>
            <div class="mt-3 grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs">
                <button onclick="setDgScenario(2, 0.5, '2 ÷ (1/2)')" class="p-2 bg-slate-800 hover:bg-slate-700 text-left rounded border border-slate-700">
                    <span class="font-bold text-amber-300 block">2 &divide; 1/2</span>
                    <span class="text-slate-400 text-[10px]">How many half-cakes in 2 cakes? &rarr; 4 halves</span>
                </button>
                <button onclick="setDgScenario(3, 0.75, '3 ÷ (3/4)')" class="p-2 bg-slate-800 hover:bg-slate-700 text-left rounded border border-slate-700">
                    <span class="font-bold text-cyan-300 block">3 &divide; 3/4</span>
                    <span class="text-slate-400 text-[10px]">How many 3/4-cups in 3 cups? &rarr; 4 portions</span>
                </button>
                <button onclick="setDgScenario(1.5, 0.25, '(3/2) ÷ (1/4)')" class="p-2 bg-slate-800 hover:bg-slate-700 text-left rounded border border-slate-700">
                    <span class="font-bold text-emerald-300 block">1 1/2 &divide; 1/4</span>
                    <span class="text-slate-400 text-[10px]">How many quarters in 1.5 strips? &rarr; 6 slices</span>
                </button>
            </div>
            <div id="dgExplanation" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800 text-center font-mono">
                $2 \div (1/2) = 4$. Notice that dividing by a fraction smaller than 1 creates MORE pieces!
            </div>
        </div>
    """,

    # 11. Division Inverter Transformer
    "sim-division-inverter": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Brahmagupta's "Invert & Multiply" Transformer</span>
                <span class="text-xs font-mono text-amber-300">$\\frac{a}{b} \\div \\frac{c}{d} = \\frac{a}{b} \\times \\frac{d}{c}$</span>
            </div>
            <div class="p-4 bg-slate-950 rounded-xl border border-slate-800 flex flex-col items-center">
                <!-- Interactive Stage Display -->
                <div class="flex items-center gap-3 sm:gap-6 font-mono text-lg sm:text-xl">
                    <!-- Dividend -->
                    <div class="flex flex-col items-center p-2 bg-slate-900 rounded border border-amber-500/30">
                        <span id="diNum1" class="text-amber-300 font-bold">5</span>
                        <div class="w-10 h-0.5 bg-slate-600 my-1"></div>
                        <span id="diDen1" class="text-amber-300 font-bold">6</span>
                    </div>
                    <!-- Operation Symbol -->
                    <div id="diOpBadge" class="p-2 rounded bg-rose-500/20 text-rose-300 font-bold border border-rose-500/40 text-xl transition-all duration-300">
                        &divide;
                    </div>
                    <!-- Divisor -->
                    <div id="diDivisorBox" class="flex flex-col items-center p-2 bg-slate-900 rounded border border-cyan-500/30 transition-transform duration-500">
                        <span id="diNum2" class="text-cyan-300 font-bold">2</span>
                        <div class="w-10 h-0.5 bg-slate-600 my-1"></div>
                        <span id="diDen2" class="text-cyan-300 font-bold">3</span>
                    </div>
                    <span class="text-slate-500 font-bold">&rarr;</span>
                    <!-- Final Product -->
                    <div class="flex flex-col items-center p-2 bg-emerald-500/20 rounded border border-emerald-500/50">
                        <span id="diResNum" class="text-emerald-300 font-bold">5</span>
                        <div class="w-10 h-0.5 bg-emerald-400 my-1"></div>
                        <span id="diResDen" class="text-emerald-300 font-bold">4</span>
                        <span id="diMixed" class="text-[10px] text-emerald-400 mt-1">= 1 1/4</span>
                    </div>
                </div>
            </div>
            <div class="mt-3 flex flex-wrap gap-2 justify-center text-xs">
                <button onclick="setDiProblem(5, 6, 2, 3)" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-slate-200">
                    5/6 &divide; 2/3
                </button>
                <button onclick="setDiProblem(7, 4, 7, 8)" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-slate-200">
                    7/4 &divide; 7/8
                </button>
                <button onclick="setDiProblem(3, 10, 9, 20)" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-slate-200">
                    3/10 &divide; 9/20
                </button>
                <button onclick="toggleInvertStep()" id="diActionBtn" class="px-4 py-1 bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold rounded shadow">
                    &circlearrowright; Step: Invert Divisor!
                </button>
            </div>
            <div id="diHelp" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800 text-center font-mono">
                Click <strong>Invert Divisor</strong> to see the reciprocal flip and transform division into multiplication!
            </div>
        </div>
    """,

    # 12. Quotient Behavior Dial
    "sim-quotient-magnifier": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Quotient Behavior Dial: Magnify vs Shrink</span>
                <span id="qmEffectBadge" class="text-xs font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">Quotient Expands!</span>
            </div>
            <div class="relative w-full h-52 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="qmSvg" viewBox="0 0 500 180" class="w-full h-full">
                    <!-- Gauge dial and dividend vs quotient comparison bar -->
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                <div class="flex flex-col gap-2">
                    <div class="flex justify-between">
                        <span class="text-slate-300">Dividend ($N$): <strong class="text-amber-400 font-mono">6</strong></span>
                        <span class="text-slate-300">Divisor ($D$): <strong id="qmDivisorText" class="text-cyan-400 font-mono">1/2 (0.50)</strong></span>
                    </div>
                    <input id="qmDivisorSlider" type="range" min="1" max="30" value="5" oninput="updateQuotientMagnifier()" class="w-full accent-cyan-400">
                    <div class="flex justify-between text-[10px] text-slate-400">
                        <span>0.1 (Tiny fraction)</span>
                        <span>1.0 (Neutral)</span>
                        <span>3.0 (Large divisor)</span>
                    </div>
                </div>
                <div class="p-2.5 bg-slate-800/80 rounded border border-slate-700 flex flex-col justify-center">
                    <div class="font-mono text-sm font-bold text-amber-300" id="qmCalculation">
                        6 &divide; (1/2) = 12
                    </div>
                    <div class="mt-1 text-[11px] text-slate-300" id="qmRuleExplanation">
                        Since divisor $0.5 < 1$, dividing expands 6 into 12!
                    </div>
                </div>
            </div>
        </div>
    """,

    # 13. Practical Rates & Speed/Milk
    "sim-milk-sharing-speed": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Everyday Fractions: Milk Cups & Speed Rates</span>
                <div class="flex gap-1.5">
                    <button onclick="setPrMode('milk')" id="prMilkBtn" class="px-2 py-0.5 rounded text-xs font-semibold bg-amber-500/30 text-amber-300 border border-amber-500/50">Milk Sharing</button>
                    <button onclick="setPrMode('speed')" id="prSpeedBtn" class="px-2 py-0.5 rounded text-xs font-semibold bg-slate-800 text-slate-300 border border-slate-700">Speed = d / t</button>
                </div>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="prSvg" viewBox="0 0 500 200" class="w-full h-full">
                    <!-- Milk jug & cups or distance line -->
                </svg>
            </div>
            <div class="mt-2 text-xs flex flex-wrap items-center justify-between gap-2 bg-slate-800/60 p-2 rounded border border-slate-700">
                <div id="prControls" class="flex items-center gap-2">
                    <!-- Dynamic slider/inputs by JS -->
                </div>
                <div id="prResultSummary" class="font-mono text-amber-300 font-bold">
                    Total cups filled = (3/4) &divide; (1/8) = 6 cups
                </div>
            </div>
        </div>
    """,

    # 14. Sulbasutra Bricklaying
    "sim-sulbasutra-bricks": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Vedic Śulbasūtra Brick-Layer Altar</span>
                <span class="text-xs font-mono text-amber-300">Baudhāyana & Āpastamba Heritage</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 items-center">
                <div class="relative w-full h-60 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                    <svg id="sbSvg" viewBox="0 0 240 220" class="w-full h-full">
                        <!-- Sacred Altar Grid with Fractional Bricks -->
                    </svg>
                </div>
                <div class="flex flex-col gap-2.5 text-xs">
                    <div class="p-2 bg-slate-800/80 rounded border border-slate-700">
                        <span class="text-slate-300 font-bold block mb-1">Brick Fraction Size:</span>
                        <div class="flex gap-2">
                            <button onclick="setSbBrick('half')" id="sbBtnHalf" class="flex-1 py-1 bg-amber-500/20 text-amber-300 rounded border border-amber-500/40">1/2 Brick</button>
                            <button onclick="setSbBrick('quarter')" id="sbBtnQuarter" class="flex-1 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700">1/4 Brick</button>
                            <button onclick="setSbBrick('eighth')" id="sbBtnEighth" class="flex-1 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700">1/8 Brick</button>
                        </div>
                    </div>
                    <div class="p-2.5 bg-slate-900 rounded border border-amber-500/30">
                        <div class="text-slate-400 text-[10px]">TOTAL ALTAR AREA: <span class="text-slate-200 font-bold font-mono">1 Square Puruṣa</span></div>
                        <div class="text-slate-400 text-[10px] mt-0.5">BRICKS REQUIRED: <span id="sbBrickCount" class="text-amber-400 font-bold font-mono text-sm">4 Bricks</span></div>
                        <div class="mt-1 text-[11px] text-cyan-300 font-mono" id="sbFormula">
                            1 &divide; (1/4) = 1 &times; (4/1) = 4 Bricks
                        </div>
                    </div>
                    <div class="text-[11px] text-slate-400">
                        Śulbasūtras specify exact fractional bricks so altars could be built layer by layer without breaking stones.
                    </div>
                </div>
            </div>
        </div>
    """,

    # 15. Cistern Fountain Filling Rates
    "sim-cistern-fountain": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Chaturveda Pṛthūdakasvāmī's Cistern (c. 860 CE)</span>
                <span class="text-xs font-mono text-cyan-300">Rate = $\\frac{1}{t_1} + \\frac{1}{t_2} + \\frac{1}{t_3}$</span>
            </div>
            <div class="relative w-full h-56 bg-slate-950 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center p-2">
                <svg id="cfSvg" viewBox="0 0 500 200" class="w-full h-full">
                    <!-- Cistern tank with 3 pouring fountains and rising water level -->
                </svg>
            </div>
            <div class="mt-2 grid grid-cols-1 sm:grid-cols-4 gap-2 text-xs">
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700 flex flex-col justify-between">
                    <span class="text-amber-300 font-bold">Fountain 1 ($t_1$)</span>
                    <span class="text-slate-400 text-[11px]">Takes 2 hours alone</span>
                    <span class="text-cyan-300 font-mono text-xs">Rate: 1/2 tank/hr</span>
                </div>
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700 flex flex-col justify-between">
                    <span class="text-amber-300 font-bold">Fountain 2 ($t_2$)</span>
                    <span class="text-slate-400 text-[11px]">Takes 3 hours alone</span>
                    <span class="text-cyan-300 font-mono text-xs">Rate: 1/3 tank/hr</span>
                </div>
                <div class="p-2 bg-slate-800/80 rounded border border-slate-700 flex flex-col justify-between">
                    <span class="text-amber-300 font-bold">Fountain 3 ($t_3$)</span>
                    <span class="text-slate-400 text-[11px]">Takes 6 hours alone</span>
                    <span class="text-cyan-300 font-mono text-xs">Rate: 1/6 tank/hr</span>
                </div>
                <div class="p-2 bg-slate-900 rounded border border-amber-500/40 flex flex-col justify-center text-center">
                    <span class="text-slate-400 text-[10px]">COMBINED RATE</span>
                    <span class="text-emerald-400 font-bold font-mono text-sm">1/2 + 1/3 + 1/6 = 1</span>
                    <span class="text-amber-300 font-bold text-xs mt-0.5">&rarr; 1 Full Hour!</span>
                </div>
            </div>
            <div class="mt-2 flex justify-between items-center text-xs">
                <button onclick="toggleCisternFlow()" id="cfFlowBtn" class="px-4 py-1.5 bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold rounded shadow">
                    &blacktriangleright; Open All Fountains!
                </button>
                <span id="cfStatus" class="text-slate-400 font-mono">Status: Ready</span>
            </div>
        </div>
    """,

    # 16. Lilavati Donation Riddle
    "sim-lilavati-donation": """
        <div class="p-3 bg-slate-900/90 rounded-2xl border border-amber-500/30">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-700">
                <span class="text-xs font-bold text-amber-300 uppercase tracking-wider">Bhāskarāchārya's Līlāvatī Alms Riddle (c. 1150 CE)</span>
                <span class="text-xs font-mono text-amber-300">Working Backwards (Viparīta-vidhi)</span>
            </div>
            <div class="p-4 bg-slate-950 rounded-xl border border-slate-800 flex flex-col items-center">
                <!-- Coin Purse Flow Diagram -->
                <div class="flex flex-wrap items-center justify-center gap-3 font-mono text-xs sm:text-sm">
                    <!-- Total Purse -->
                    <div class="p-2.5 bg-slate-900 rounded-lg border border-amber-500/40 text-center">
                        <span class="text-slate-400 block text-[10px]">INITIAL PURSE ($x$)</span>
                        <span id="lvInitCoins" class="text-amber-300 font-bold text-lg">? Coins</span>
                    </div>
                    <span class="text-slate-500 font-bold">&rarr; -1/2 &rarr;</span>
                    <!-- After Temple 1 -->
                    <div class="p-2 bg-slate-900 rounded border border-slate-700 text-center">
                        <span class="text-slate-400 block text-[10px]">REMAINDER 1</span>
                        <span id="lvRem1" class="text-cyan-300 font-bold">1/2 of $x$</span>
                    </div>
                    <span class="text-slate-500 font-bold">&rarr; -1/3 of rem &rarr;</span>
                    <!-- After Temple 2 -->
                    <div class="p-2 bg-slate-900 rounded border border-slate-700 text-center">
                        <span class="text-slate-400 block text-[10px]">REMAINDER 2</span>
                        <span id="lvRem2" class="text-cyan-300 font-bold">1/3 of $x$</span>
                    </div>
                    <span class="text-slate-500 font-bold">&rarr; Final Left &rarr;</span>
                    <!-- Final Coin Balance -->
                    <div class="p-2.5 bg-emerald-500/20 rounded-lg border border-emerald-500/50 text-center">
                        <span class="text-emerald-400 block text-[10px]">FINAL BALANCE</span>
                        <span id="lvFinalCoins" class="text-emerald-300 font-bold text-lg">20 Coins</span>
                    </div>
                </div>
            </div>
            <div class="mt-3 flex flex-wrap items-center justify-between gap-2 text-xs">
                <div class="flex items-center gap-2">
                    <span class="text-slate-300">Remaining coins:</span>
                    <input id="lvFinalInput" type="number" min="5" max="100" value="20" oninput="updateLilavatiRiddle()" class="w-16 bg-slate-800 text-emerald-300 font-bold text-center rounded border border-slate-700 p-1">
                </div>
                <button onclick="revealLilavatiSolution()" class="px-4 py-1.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded shadow">
                    &star; Reveal Brahmagupta / Bhāskara Deduction!
                </button>
            </div>
            <div id="lvDeductionBox" class="mt-2 text-xs text-slate-300 bg-slate-800/40 p-2 rounded border border-slate-800">
                Bhāskara II's Viparīta: If $1/3$ of the original purse remains, and that equals 20 coins, then the original purse must be $20 \div (1/3) = 20 \times 3 = \mathbf{60\text{ coins}}$!
            </div>
        </div>
    """
}

with open('.agents/class7_math_working_with_fractions_sims.py', 'w') as f:
    f.write(f"SIMULATORS = {repr(sims)}\n")

print("Created .agents/class7_math_working_with_fractions_sims.py successfully with 16 simulators!")

