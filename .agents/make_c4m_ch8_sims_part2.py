# -*- coding: utf-8 -*-
"""
Class 4 Mathematics Chapter 8: Weigh It, Pour It
Part 2 Simulators: Slides 9 to 16
Bespoke SVG/HTML interactive simulators.
Zero human names (Shrinathan, Mirabai, Raghav, etc. replaced with generic roles).
Clean Unicode throughout.
"""

sim9 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-300 font-bold flex items-center justify-center text-sm">09</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Litres And Millilitres</h3>
        </div>
        <span class="text-xs text-blue-400 font-medium">1 L = 1000 ml Measuring Cylinder</span>
    </div>

    <!-- Presets -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setLiquidPreset(150, 'Teacup')" class="lq-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">Teacup (150 ml)</button>
        <button onclick="setLiquidPreset(250, 'Glass')" class="lq-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">Glass Tumbler (250 ml)</button>
        <button onclick="setLiquidPreset(500, 'Milk Pouch')" class="lq-btn px-2.5 py-1 rounded-lg bg-blue-500 text-slate-950 text-xs font-bold shadow">Milk Pouch (500 ml)</button>
        <button onclick="setLiquidPreset(1000, 'Water Bottle')" class="lq-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">Bottle (1000 ml = 1 L)</button>
    </div>

    <!-- Interactive Cylinder SVG & Slider -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center bg-slate-950 rounded-xl p-4 border border-slate-800">
        <div class="flex justify-center">
            <svg id="liquidCylinderSvg" viewBox="0 0 140 220" class="w-28 h-auto">
                <defs>
                    <linearGradient id="waterGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#0284c7" />
                        <stop offset="100%" stop-color="#38bdf8" />
                    </linearGradient>
                </defs>
                <!-- Glass Cylinder Outline -->
                <rect x="35" y="20" width="70" height="180" rx="4" fill="#0f172a" stroke="#475569" stroke-width="2"/>
                <!-- Liquid Fill Rect (Height 170 max) -->
                <rect id="liquidFillRect" x="37" y="115" width="66" height="83" rx="2" fill="url(#waterGrad)" class="transition-all duration-300"/>
                
                <!-- Graduation Marks -->
                <!-- 1000ml (y=30) -->
                <line x1="35" y1="30" x2="50" y2="30" stroke="#94a3b8" stroke-width="1.5"/>
                <text x="55" y="33" fill="#cbd5e1" font-size="8" font-family="monospace">1000ml (1L)</text>
                <!-- 750ml (y=72.5) -->
                <line x1="35" y1="72.5" x2="47" y2="72.5" stroke="#94a3b8" stroke-width="1"/>
                <text x="52" y="75" fill="#cbd5e1" font-size="7" font-family="monospace">750ml</text>
                <!-- 500ml (y=115) -->
                <line x1="35" y1="115" x2="50" y2="115" stroke="#94a3b8" stroke-width="1.5"/>
                <text x="55" y="118" fill="#38bdf8" font-size="8" font-weight="bold" font-family="monospace">500ml (1/2L)</text>
                <!-- 250ml (y=157.5) -->
                <line x1="35" y1="157.5" x2="47" y2="157.5" stroke="#94a3b8" stroke-width="1"/>
                <text x="52" y="160" fill="#cbd5e1" font-size="7" font-family="monospace">250ml</text>
                <!-- 0ml base -->
                <line x1="35" y1="200" x2="105" y2="200" stroke="#64748b" stroke-width="3"/>
            </svg>
        </div>

        <div class="space-y-3">
            <div class="space-y-1">
                <div class="flex justify-between text-xs text-slate-400">
                    <span>Selected Volume:</span>
                    <strong id="cylinderVolumeLabel" class="text-blue-400 text-sm">500 ml</strong>
                </div>
                <input type="range" id="cylinderSlider" min="0" max="1000" step="25" value="500" oninput="updateCylinderSlider(this.value)" class="w-full accent-blue-500 cursor-pointer">
            </div>
            <div class="bg-slate-900 p-2.5 rounded-lg border border-slate-800 text-xs text-slate-300 space-y-1">
                <div>Container: <strong id="containerNameLabel" class="text-white">Milk Pouch</strong></div>
                <div>Fraction of 1 L: <strong id="cylinderFractionLabel" class="text-blue-300">1/2 Litre</strong></div>
            </div>
        </div>
    </div>

    <div class="text-xs text-slate-300 bg-blue-950/30 p-2.5 rounded-lg border border-blue-800/40">
        <strong>Metric Rule:</strong> 1 Litre (L) = 1,000 Millilitres (ml). Small volumes are measured in ml, larger household volumes in L!
    </div>
</div>
"""

sim10 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-teal-500/20 text-teal-300 font-bold flex items-center justify-center text-sm">10</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Fractional Litre Measures</h3>
        </div>
        <span class="text-xs text-teal-400 font-medium">1/4 L, 1/2 L, 3/4 L Subdivisions</span>
    </div>

    <!-- Fraction Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
        <button onclick="setFractionLitre(250)" id="fl-btn-250" class="fl-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            1/4 L (250 ml)
        </button>
        <button onclick="setFractionLitre(500)" id="fl-btn-500" class="fl-btn p-2 rounded-xl bg-teal-500 text-slate-950 font-bold shadow transition">
            1/2 L (500 ml)
        </button>
        <button onclick="setFractionLitre(750)" id="fl-btn-750" class="fl-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            3/4 L (750 ml)
        </button>
        <button onclick="setFractionLitre(1000)" id="fl-btn-1000" class="fl-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            1 L (1000 ml)
        </button>
    </div>

    <!-- 4 Quarter Blocks Visualization -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="flex justify-between text-xs text-slate-400 font-semibold">
            <span>Modular 250ml Quarter Segments:</span>
            <span id="activeFractionText" class="text-teal-400 font-bold">2 of 4 Quarters Filled (500 ml)</span>
        </div>
        <div class="grid grid-cols-4 gap-2">
            <div id="qblock-1" class="h-14 rounded-lg bg-teal-500 flex flex-col items-center justify-center text-slate-950 font-bold text-xs transition">
                <span>1/4 L</span>
                <span class="text-[10px] font-mono">250 ml</span>
            </div>
            <div id="qblock-2" class="h-14 rounded-lg bg-teal-500 flex flex-col items-center justify-center text-slate-950 font-bold text-xs transition">
                <span>1/4 L</span>
                <span class="text-[10px] font-mono">250 ml</span>
            </div>
            <div id="qblock-3" class="h-14 rounded-lg bg-slate-800 border border-slate-700 flex flex-col items-center justify-center text-slate-400 font-bold text-xs transition">
                <span>1/4 L</span>
                <span class="text-[10px] font-mono">250 ml</span>
            </div>
            <div id="qblock-4" class="h-14 rounded-lg bg-slate-800 border border-slate-700 flex flex-col items-center justify-center text-slate-400 font-bold text-xs transition">
                <span>1/4 L</span>
                <span class="text-[10px] font-mono">250 ml</span>
            </div>
        </div>
    </div>

    <div class="bg-teal-950/40 p-3 rounded-xl border border-teal-800/40 text-xs text-teal-200">
        <strong>Mathematical Identity:</strong> 250 ml + 250 ml = 500 ml (half litre). 500 ml + 250 ml = 750 ml (three-quarters litre). Four 250 ml blocks make 1 full litre!
    </div>
</div>
"""

sim11 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-sm">11</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Droppers And Spoons</h3>
        </div>
        <span class="text-xs text-indigo-400 font-medium">Miniature Medical Doses</span>
    </div>

    <!-- Medicine Dispenser Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
        <button onclick="setDispenser(1, 'Eye Dropper')" class="md-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            Dropper (1 ml)
        </button>
        <button onclick="setDispenser(5, 'Medicine Spoon')" class="md-btn p-2 rounded-xl bg-indigo-500 text-slate-950 font-bold shadow transition">
            Teaspoon (5 ml)
        </button>
        <button onclick="setDispenser(10, 'Dosing Cup')" class="md-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            Dosing Cup (10 ml)
        </button>
        <button onclick="setDispenser(15, 'Oral Syringe')" class="md-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            Syringe (15 ml)
        </button>
    </div>

    <!-- Interactive Dose Accumulator -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-400">Total Dosed: <strong id="totalDoseDisplay" class="text-white text-sm">5 ml</strong></span>
            <div class="flex gap-2">
                <button onclick="addDose()" class="px-3 py-1 bg-indigo-600 hover:bg-indigo-500 text-white rounded font-bold text-xs">+ Dispense Dose</button>
                <button onclick="resetDose()" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-400 rounded text-xs">Reset</button>
            </div>
        </div>

        <div class="bg-slate-900 p-3 rounded-lg border border-slate-800 space-y-2 text-xs">
            <div class="flex justify-between">
                <span class="text-slate-400">Standard 100 ml Syrup Bottle:</span>
                <span id="bottleRemainingLabel" class="text-indigo-400 font-bold">95 ml remaining</span>
            </div>
            <div class="w-full h-3 bg-slate-800 rounded-full overflow-hidden">
                <div id="bottleProgressBar" class="h-full bg-indigo-500 transition-all duration-300" style="width: 5%;"></div>
            </div>
            <div class="text-[11px] text-slate-400 text-right" id="daysLastText">
                At 10 ml/day (5ml twice daily), bottle lasts 10 days!
            </div>
        </div>
    </div>

    <div class="text-xs text-slate-300 bg-slate-800/40 p-2.5 rounded-lg border border-slate-700/40">
        <strong>Clinical Insight:</strong> About 20 drops from an eyedropper equal 1 ml. Accurate millilitre measurement prevents medicinal underdosing or overdosing!
    </div>
</div>
"""

sim12 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-pink-500/20 text-pink-300 font-bold flex items-center justify-center text-sm">12</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Perfumed Oil Bottles</h3>
        </div>
        <span class="text-xs text-pink-400 font-medium">1000 ml Artisan Packaging</span>
    </div>

    <!-- Retail Bottle Size Selectors -->
    <div class="flex flex-wrap items-center justify-center gap-2">
        <button onclick="setOilBottleSize(50)" id="ob-btn-50" class="ob-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">50 ml Vials</button>
        <button onclick="setOilBottleSize(100)" id="ob-btn-100" class="ob-btn px-2.5 py-1 rounded-lg bg-pink-500 text-slate-950 text-xs font-bold shadow">100 ml Bottles</button>
        <button onclick="setOilBottleSize(200)" id="ob-btn-200" class="ob-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">200 ml Bottles</button>
        <button onclick="setOilBottleSize(250)" id="ob-btn-250" class="ob-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700">250 ml Bottles</button>
    </div>

    <!-- Dynamic Bottle Yield Visualizer -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 min-h-[170px] flex flex-col justify-center items-center space-y-3">
        <div class="text-xs text-pink-300 font-bold" id="oilEquationText">
            1000 ml ÷ 100 ml = 10 Bottles Filled
        </div>
        <div id="oilBottlesGrid" class="flex flex-wrap gap-2 justify-center max-w-[320px] max-h-[140px] overflow-y-auto p-1">
            <!-- Dynamically generated bottles -->
        </div>
    </div>

    <div class="bg-pink-950/40 p-3 rounded-xl border border-pink-800/40 text-xs text-pink-200">
        <strong>Packaging Logic:</strong> 1 Litre master batch (1000 ml) divided into 50 ml bottles yields 20 bottles. Dividing into 200 ml bottles yields 5 bottles!
    </div>
</div>
"""

sim13 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-300 font-bold flex items-center justify-center text-sm">13</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Milk Measuring Cans</h3>
        </div>
        <span class="text-xs text-amber-400 font-medium">Standard Dairy Scoops</span>
    </div>

    <!-- Target Milk Order Selector -->
    <div class="flex items-center justify-between text-xs bg-slate-950 p-2.5 rounded-xl border border-slate-800">
        <span class="text-slate-400">Customer Order Target:</span>
        <div class="flex gap-1.5">
            <button onclick="setMilkOrder(750)" id="mo-btn-750" class="mo-btn px-2 py-1 rounded bg-amber-500 text-slate-950 font-bold text-xs">750 ml</button>
            <button onclick="setMilkOrder(1200)" id="mo-btn-1200" class="mo-btn px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700 text-xs">1200 ml</button>
            <button onclick="setMilkOrder(1500)" id="mo-btn-1500" class="mo-btn px-2 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700 text-xs">1500 ml</button>
        </div>
    </div>

    <!-- Dairy Scoops Clicker -->
    <div class="space-y-2">
        <span class="text-xs font-semibold text-slate-400 block">Click Cans to Pour Milk:</span>
        <div class="grid grid-cols-5 gap-1.5 text-center text-xs">
            <button onclick="pourMilkScoop(50)" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 font-bold">+50ml</button>
            <button onclick="pourMilkScoop(100)" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 font-bold">+100ml</button>
            <button onclick="pourMilkScoop(200)" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 font-bold">+200ml</button>
            <button onclick="pourMilkScoop(500)" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 font-bold">+500ml</button>
            <button onclick="pourMilkScoop(1000)" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 font-bold">+1 L</button>
        </div>
    </div>

    <!-- Poured Milk Jug Status -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-2">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-400">Total Milk Poured:</span>
            <strong id="pouredMilkTotal" class="text-amber-400 text-base font-black">0 ml</strong>
        </div>
        <div id="milkPourFeedback" class="text-xs p-2 rounded-lg bg-slate-900 border border-slate-800 text-slate-300 flex justify-between items-center">
            <span>Target: 750 ml (Need 750 ml more)</span>
            <button onclick="resetMilkJug()" class="text-[10px] text-slate-400 underline">Clear Jug</button>
        </div>
    </div>
</div>
"""

sim14 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-cyan-500/20 text-cyan-300 font-bold flex items-center justify-center text-sm">14</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Daily Water Consumption</h3>
        </div>
        <span class="text-xs text-cyan-400 font-medium">Household Audit (4 Members)</span>
    </div>

    <!-- Domestic Activity Sliders / Breakdown -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3 text-xs">
        <div class="space-y-2">
            <div class="flex justify-between text-slate-300">
                <span>Drinking & Cooking:</span>
                <span class="text-cyan-400 font-bold">30 Litres</span>
            </div>
            <div class="w-full h-2.5 bg-slate-800 rounded-full overflow-hidden">
                <div class="h-full bg-cyan-500" style="width: 12%;"></div>
            </div>

            <div class="flex justify-between text-slate-300">
                <span>Dishes & Cleaning:</span>
                <span class="text-cyan-400 font-bold">50 Litres</span>
            </div>
            <div class="w-full h-2.5 bg-slate-800 rounded-full overflow-hidden">
                <div class="h-full bg-blue-500" style="width: 20%;"></div>
            </div>

            <div class="flex justify-between text-slate-300">
                <span>Washing Laundry:</span>
                <span class="text-cyan-400 font-bold">50 Litres</span>
            </div>
            <div class="w-full h-2.5 bg-slate-800 rounded-full overflow-hidden">
                <div class="h-full bg-indigo-500" style="width: 20%;"></div>
            </div>

            <div class="flex justify-between text-slate-300">
                <span>Baths (4 Bucket Baths @ 30L):</span>
                <span class="text-cyan-400 font-bold">120 Litres</span>
            </div>
            <div class="w-full h-2.5 bg-slate-800 rounded-full overflow-hidden">
                <div class="h-full bg-sky-400" style="width: 48%;"></div>
            </div>
        </div>

        <div class="pt-2 border-t border-slate-800 flex justify-between items-center text-xs">
            <span class="font-bold text-slate-200">Total Family Daily Water:</span>
            <span class="text-base font-black text-cyan-300">250 Litres / Day</span>
        </div>
    </div>

    <div class="text-xs text-slate-400 bg-slate-800/40 p-2.5 rounded-lg border border-slate-700/40">
        <strong>Observation:</strong> Personal hygiene and laundry consume over 65% of total domestic water. Mindful conservation in these activities produces immediate substantial savings!
    </div>
</div>
"""

sim15 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-red-500/20 text-red-300 font-bold flex items-center justify-center text-sm">15</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Leaking Tap Investigation</h3>
        </div>
        <span class="text-xs text-red-400 font-medium">Cumulative Drip Wastage</span>
    </div>

    <!-- Time Horizon Selectors -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 text-center text-xs">
        <button onclick="setLeakTime('hour')" id="lt-btn-hour" class="lt-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            1 Hour
        </button>
        <button onclick="setLeakTime('day')" id="lt-btn-day" class="lt-btn p-2 rounded-xl bg-red-500 text-slate-950 font-bold shadow transition">
            1 Day (24h)
        </button>
        <button onclick="setLeakTime('week')" id="lt-btn-week" class="lt-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            1 Week (7d)
        </button>
        <button onclick="setLeakTime('month')" id="lt-btn-month" class="lt-btn p-2 rounded-xl bg-slate-800 text-slate-300 font-bold border border-slate-700 hover:bg-slate-700 transition">
            1 Month (30d)
        </button>
    </div>

    <!-- Animated Faucet & Bucket SVG -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center space-y-2">
        <svg viewBox="0 0 200 120" class="w-48 h-auto">
            <!-- Pipe & Faucet -->
            <path d="M 40 20 L 100 20 L 100 45 L 90 45 L 90 30 L 40 30 Z" fill="#64748b"/>
            <!-- Valve handle -->
            <rect x="92" y="10" width="16" height="6" rx="2" fill="#ef4444"/>
            <rect x="98" y="16" width="4" height="6" fill="#94a3b8"/>
            <!-- Dripping Water droplet -->
            <circle cx="95" cy="60" r="3.5" fill="#38bdf8" opacity="0.9">
                <animate attributeName="cy" values="45;85" dur="1.2s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="1;0.2" dur="1.2s" repeatCount="indefinite" />
            </circle>
            <!-- Water Bucket -->
            <polygon points="75,85 115,85 110,115 80,115" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
            <!-- Water inside bucket -->
            <polygon id="bucketWaterFill" points="76,95 114,95 110,115 80,115" fill="#0284c7"/>
        </svg>

        <div class="text-center space-y-1">
            <span class="text-xs text-slate-400 font-semibold" id="leakFormulaLabel">1 L/hour × 24 hours</span>
            <div id="leakVolumeDisplay" class="text-2xl font-black text-red-400 font-mono">
                24 Litres Lost!
            </div>
        </div>
    </div>

    <div class="bg-red-950/40 p-3 rounded-xl border border-red-800/40 text-xs text-red-200">
        <strong>Shocking Fact:</strong> A single tap dripping 1 drop every second wastes 24 L daily, 168 L weekly, and 720 L every month!
    </div>
</div>
"""

sim16 = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4 shadow-lg">
    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-2">
            <span class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-300 font-bold flex items-center justify-center text-sm">16</span>
            <h3 class="font-bold text-white text-sm sm:text-base">Conservation Volume Math</h3>
        </div>
        <span class="text-xs text-emerald-400 font-medium">Multiplied School Savings</span>
    </div>

    <!-- Student Population Slider -->
    <div class="space-y-1.5 px-2">
        <div class="flex justify-between text-xs text-slate-400 font-medium">
            <span>School Enrollment (Students):</span>
            <span id="studentCountLabel" class="text-emerald-400 font-bold text-sm">500 Students</span>
        </div>
        <input type="range" id="studentSlider" min="50" max="1000" step="50" value="500" oninput="updateConservationMath(this.value)" class="w-full accent-emerald-500 cursor-pointer">
    </div>

    <!-- Multiplied Conservation Impact Display -->
    <div class="bg-slate-950 rounded-xl p-4 border border-slate-800 space-y-3">
        <div class="grid grid-cols-2 gap-3 text-center">
            <div class="bg-slate-900 p-3 rounded-lg border border-slate-800">
                <span class="block text-[11px] text-slate-400">Daily Water Saved:</span>
                <strong id="dailySchoolSavings" class="text-emerald-400 text-lg font-black font-mono">9,500 L</strong>
                <span class="block text-[10px] text-slate-500">(@ 19 L per student)</span>
            </div>
            <div class="bg-slate-900 p-3 rounded-lg border border-slate-800">
                <span class="block text-[11px] text-slate-400">Monthly School Saved:</span>
                <strong id="monthlySchoolSavings" class="text-teal-400 text-lg font-black font-mono">285,000 L</strong>
                <span class="block text-[10px] text-slate-500">(30 school days)</span>
            </div>
        </div>

        <!-- Equivalent Water Tankers -->
        <div class="bg-slate-900/60 p-2.5 rounded-lg border border-slate-800 flex justify-between items-center text-xs text-slate-300">
            <span>Equivalent Water Tankers Saved:</span>
            <strong id="tankerEquivLabel" class="text-emerald-300">~28 Large Tankers (10,000L each)</strong>
        </div>
    </div>

    <div class="text-xs text-slate-300 bg-emerald-950/30 p-2.5 rounded-lg border border-emerald-800/40">
        <strong>Community Power:</strong> Simply turning off running taps while brushing saves 19 litres daily per person. Scaled across schools and neighborhoods, millions of litres are conserved!
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
    16: sim16,
}

if __name__ == "__main__":
    print(f"Loaded {len(simulators_part2)} simulators for Part 2.")
    for k, v in simulators_part2.items():
        print(f"Sim {k}: {len(v)} chars")

