# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 8: Weight and Capacity
Simulators 9 to 16 (HTML & SVG interactive components)
"""

simulators_part2 = {
    9: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🥔 Proportional Weight Scaler</span>
                <span class="text-[10px] text-cyan-300 font-mono">1 Sack = 2 kg 350 g</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select the number of potato sacks to scale the total mass:</p>
            <div class="flex gap-1.5 mb-2">
                <button onclick="sim9Scale(1)" class="sim9-btn flex-1 py-1 rounded bg-slate-800 text-slate-200 border border-slate-700">1 Sack</button>
                <button onclick="sim9Scale(2)" class="sim9-btn flex-1 py-1 rounded bg-slate-800 text-slate-200 border border-slate-700">2 Sacks</button>
                <button onclick="sim9Scale(3)" class="sim9-btn flex-1 py-1 rounded bg-slate-800 text-slate-200 border border-slate-700">3 Sacks</button>
                <button onclick="sim9Scale(4)" class="sim9-btn flex-1 py-1 rounded bg-cyan-700 font-bold text-slate-950 border border-cyan-600">4 Sacks</button>
                <button onclick="sim9Scale(5)" class="sim9-btn flex-1 py-1 rounded bg-slate-800 text-slate-200 border border-slate-700">5 Sacks</button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div class="grid grid-cols-2 gap-2 text-xs">
                <div class="p-2 rounded bg-slate-950 border border-slate-800">
                    <div class="text-[10px] text-slate-400 uppercase font-mono">Method 1: Unit by Unit</div>
                    <div id="sim9_m1_kg" class="text-cyan-300 font-mono mt-1">4 × 2 kg = 8 kg</div>
                    <div id="sim9_m1_g" class="text-amber-300 font-mono">4 × 350 g = 1,400 g</div>
                    <div class="text-[10px] text-slate-400 mt-0.5">Regroup: 1,400 g = 1 kg 400 g</div>
                </div>
                <div class="p-2 rounded bg-slate-950 border border-slate-800">
                    <div class="text-[10px] text-slate-400 uppercase font-mono">Method 2: Convert to Grams</div>
                    <div id="sim9_m2_conv" class="text-cyan-300 font-mono mt-1">2 kg 350 g = 2,350 g</div>
                    <div id="sim9_m2_calc" class="text-amber-300 font-mono">2,350 g × 4 = 9,400 g</div>
                    <div class="text-[10px] text-slate-400 mt-0.5">Reconvert: 9 kg 400 g</div>
                </div>
            </div>
            <div class="p-2 rounded-lg bg-emerald-950/60 border border-emerald-700/60 text-center font-mono font-bold text-emerald-300 text-sm">
                Total Scaled Weight = <span id="sim9_final">9 kg 400 g</span> (9,400 g)
            </div>
        </div>
    </div>
    """,

    10: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🥜 Equal Sharing & Scrap Dealer Ledger</span>
                <span class="text-[10px] text-emerald-300 font-mono">Total ÷ Count</span>
            </div>
            <div class="grid grid-cols-2 gap-2 mb-1">
                <div>
                    <label class="text-[11px] text-slate-300 block mb-1">Divide 7.5 kg Cashews into:</label>
                    <select id="sim10_parts" onchange="sim10Divide()" class="w-full bg-slate-800 border border-slate-700 rounded p-1 text-slate-200">
                        <option value="2">2 Packets</option>
                        <option value="3">3 Packets</option>
                        <option value="4">4 Packets</option>
                        <option value="5">5 Packets</option>
                        <option value="6" selected>6 Packets</option>
                        <option value="8">8 Packets</option>
                    </select>
                </div>
                <div>
                    <label class="text-[11px] text-slate-300 block mb-1">Scrap Material (Rate/kg):</label>
                    <select id="sim10_scrap" onchange="sim10Scrap()" class="w-full bg-slate-800 border border-slate-700 rounded p-1 text-slate-200">
                        <option value="14">🗞️ Old Newspaper (₹14/kg)</option>
                        <option value="28" selected>🔩 Scrap Iron (₹28/kg)</option>
                        <option value="12">🥤 Plastic Scrap (₹12/kg)</option>
                    </select>
                </div>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div class="p-2.5 rounded bg-slate-950 border border-slate-800 font-mono text-xs">
                <div class="flex justify-between text-slate-400">
                    <span>Cashew Division (7,500 g):</span>
                    <span id="sim10_res_div" class="text-cyan-300 font-bold">1,250 g per packet</span>
                </div>
                <div class="flex justify-between text-slate-400 mt-1">
                    <span>In Compound Units:</span>
                    <span id="sim10_res_unit" class="text-emerald-400 font-bold">1 kg 250 g</span>
                </div>
            </div>

            <div class="p-2.5 rounded bg-slate-950 border border-slate-800 font-mono text-xs">
                <div class="flex items-center justify-between mb-1">
                    <span class="text-slate-400">Scrap Weight:</span>
                    <div class="flex items-center gap-2">
                        <input id="sim10_kg_slider" type="range" min="1" max="25" value="5" oninput="sim10Scrap()" class="w-24 accent-amber-400">
                        <span id="sim10_kg_val" class="text-amber-300 font-bold">5 kg</span>
                    </div>
                </div>
                <div class="flex justify-between text-emerald-400 font-bold border-t border-slate-800 pt-1">
                    <span>Total Cash Paid:</span>
                    <span id="sim10_cash">5 kg × ₹28 = ₹140</span>
                </div>
            </div>
        </div>
    </div>
    """,

    11: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">💧 Virtual Liquid Measuring Lab</span>
                <span class="text-[10px] text-cyan-300 font-mono">1 L = 1,000 mL</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select a household vessel to inspect its metric capacity:</p>
            <div class="grid grid-cols-3 gap-1.5 mb-1">
                <button onclick="sim11Select('spoon')" class="p-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-left">🥄 Spoon (5 mL)</button>
                <button onclick="sim11Select('cup')" class="p-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-left">☕ Cup (150 mL)</button>
                <button onclick="sim11Select('glass')" class="p-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-left">🥛 Glass (250 mL)</button>
                <button onclick="sim11Select('carton')" class="p-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-left">🧃 Carton (1 L)</button>
                <button onclick="sim11Select('bucket')" class="p-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-left">🪣 Bucket (18 L)</button>
                <button onclick="sim11Select('tank')" class="p-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-left">🏠 Tank (750 L)</button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 flex flex-col items-center">
            <div class="flex items-center gap-4 w-full">
                <div class="flex-1 text-center font-mono">
                    <div id="sim11_icon" class="text-4xl mb-1">🥛</div>
                    <div id="sim11_name" class="font-bold text-slate-200 text-xs">Standard Drinking Glass</div>
                    <div id="sim11_cap" class="text-cyan-400 font-black text-sm mt-0.5">250 mL (1/4 Litre)</div>
                </div>
                <div class="flex-1 space-y-1.5 text-xs">
                    <div class="text-[11px] text-slate-400">Capacity Bar:</div>
                    <div class="w-full bg-slate-800 rounded-full h-4 overflow-hidden border border-slate-700">
                        <div id="sim11_bar" class="bg-cyan-500 h-full transition-all duration-300" style="width: 25%;"></div>
                    </div>
                    <div id="sim11_rel" class="text-[11px] text-slate-300">
                        4 glasses make exactly 1 full litre (1,000 mL).
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,

    12: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🧪 Graduated Cylinder & Meniscus Zoom</span>
                <span class="text-[10px] text-slate-400 font-mono">0 to 500 mL</span>
            </div>
            <div class="flex items-center gap-3 mb-2">
                <span class="text-[11px] text-slate-300">Water Level:</span>
                <input id="sim12_slider" type="range" min="50" max="500" step="10" value="260" oninput="sim12Update(parseInt(this.value))" class="w-full accent-cyan-400">
                <span id="sim12_val" class="font-mono text-cyan-300 font-bold min-w-[50px] text-right">260 mL</span>
            </div>
            <div class="flex gap-1.5">
                <button onclick="sim12Angle('high')" class="flex-1 py-1 rounded bg-slate-800 text-slate-300 text-[11px] border border-slate-700">Looking Down (Over)</button>
                <button onclick="sim12Angle('eye')" class="flex-1 py-1 rounded bg-emerald-700 font-bold text-slate-950 text-[11px] border border-emerald-600">Eye Level (Accurate)</button>
                <button onclick="sim12Angle('low')" class="flex-1 py-1 rounded bg-slate-800 text-slate-300 text-[11px] border border-slate-700">Looking Up (Under)</button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 flex items-center justify-between gap-3">
            <svg id="sim12_svg" viewBox="0 0 100 130" class="w-24 h-32">
                <!-- Cylinder Body -->
                <rect x="25" y="10" width="50" height="110" rx="3" fill="#0f172a" stroke="#475569" stroke-width="2"/>
                <!-- Liquid Fill -->
                <rect id="sim12_liquid" x="27" y="60" width="46" height="58" fill="#0284c7" opacity="0.6"/>
                <!-- Meniscus Curve -->
                <path id="sim12_meniscus" d="M 27 60 Q 50 64 73 60" fill="none" stroke="#38bdf8" stroke-width="2"/>
                <!-- Tick Marks -->
                <line x1="25" y1="20" x2="35" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
                <line x1="25" y1="40" x2="35" y2="40" stroke="#94a3b8" stroke-width="1.5"/>
                <line x1="25" y1="60" x2="35" y2="60" stroke="#94a3b8" stroke-width="1.5"/>
                <line x1="25" y1="80" x2="35" y2="80" stroke="#94a3b8" stroke-width="1.5"/>
                <line x1="25" y1="100" x2="35" y2="100" stroke="#94a3b8" stroke-width="1.5"/>
                <!-- Eye Marker -->
                <text id="sim12_eye_icon" x="80" y="64" font-size="14">👁️</text>
            </svg>

            <div class="flex-1 space-y-1.5 font-mono text-xs">
                <div class="p-2 rounded bg-slate-950 border border-slate-800">
                    <span class="text-[10px] text-slate-400 block font-sans">Apparent Observer Reading:</span>
                    <span id="sim12_reading" class="text-base font-bold text-emerald-400">260 mL (Accurate)</span>
                </div>
                <div id="sim12_note" class="text-[11px] font-sans text-slate-300">
                    At eye level with the bottom of the curved meniscus, no parallax error occurs.
                </div>
            </div>
        </div>
    </div>
    """,

    13: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🥛 Khayal Chacha's Brass Ladle Counter</span>
                <span class="text-[10px] text-slate-400">Click ladles to dispense milk</span>
            </div>
            <div class="flex gap-2 mb-2">
                <button onclick="sim13Add(500)" class="flex-1 py-1.5 rounded bg-amber-900/60 hover:bg-amber-800 text-amber-200 border border-amber-700 font-mono">+500 mL Ladle</button>
                <button onclick="sim13Add(200)" class="flex-1 py-1.5 rounded bg-amber-900/60 hover:bg-amber-800 text-amber-200 border border-amber-700 font-mono">+200 mL Ladle</button>
                <button onclick="sim13Add(100)" class="flex-1 py-1.5 rounded bg-amber-900/60 hover:bg-amber-800 text-amber-200 border border-amber-700 font-mono">+100 mL Ladle</button>
                <button onclick="sim13Reset()" class="px-2 py-1.5 rounded bg-slate-800 text-slate-400 border border-slate-700">Reset</button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 font-mono text-xs space-y-2">
            <div class="p-2.5 rounded bg-slate-950 border border-slate-800 text-center">
                <div class="text-[10px] text-slate-400 uppercase font-sans">Total Milk Poured in Pot</div>
                <div id="sim13_tot_ml" class="text-2xl font-black text-cyan-300 mt-1">0 mL</div>
                <div id="sim13_tot_l" class="text-xs text-amber-300">= 0 L 0 mL</div>
            </div>
            <div id="sim13_breakdown" class="text-[11px] font-sans text-slate-300 text-center">
                Click ladles above to measure milk for a customer order!
            </div>
        </div>
    </div>
    """,

    14: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🚰 Aarav's Hydration Goal (2,500 mL)</span>
                <span id="sim14_goal_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">In Progress</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Add water intake across daily schedule (250 mL per glass):</p>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 mb-1">
                <button onclick="sim14Add(250)" class="p-1 rounded bg-blue-900/50 hover:bg-blue-800 text-blue-200 border border-blue-700 text-left">🌅 Morning (+250)</button>
                <button onclick="sim14Add(500)" class="p-1 rounded bg-blue-900/50 hover:bg-blue-800 text-blue-200 border border-blue-700 text-left">🥪 Lunch (+500)</button>
                <button onclick="sim14Add(750)" class="p-1 rounded bg-blue-900/50 hover:bg-blue-800 text-blue-200 border border-blue-700 text-left">🏠 Afternoon (+750)</button>
                <button onclick="sim14Add(500)" class="p-1 rounded bg-blue-900/50 hover:bg-blue-800 text-blue-200 border border-blue-700 text-left">⚽ Sports (+500)</button>
            </div>
            <button onclick="sim14Reset()" class="w-full mt-1 py-0.5 rounded bg-slate-800 text-slate-400 text-[11px]">Reset Hydration Tracker</button>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div class="flex justify-between items-center text-xs font-mono">
                <span class="text-slate-300">Progress to 2.5 L:</span>
                <span id="sim14_text" class="text-cyan-300 font-bold">0 / 2,500 mL (0.00 L)</span>
            </div>
            <div class="w-full bg-slate-800 rounded-full h-4 overflow-hidden border border-slate-700">
                <div id="sim14_bar" class="bg-cyan-500 h-full transition-all duration-300" style="width: 0%;"></div>
            </div>
            <div id="sim14_msg" class="p-2 rounded bg-slate-950 text-[11px] text-slate-300 font-sans">
                Aarav hasn't started drinking water yet today. Click an activity above!
            </div>
        </div>
    </div>
    """,

    15: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">⛽ Petrol Bunk Fuel Dispenser</span>
                <span class="text-[10px] text-cyan-300 font-mono">₹96 / Litre</span>
            </div>
            <div class="grid grid-cols-2 gap-2 mb-2">
                <div>
                    <label class="text-[11px] text-slate-300 block mb-1">Select Vehicle:</label>
                    <select id="sim15_veh" onchange="sim15Select()" class="w-full bg-slate-800 border border-slate-700 rounded p-1 text-slate-200">
                        <option value="12">🛵 Motorcycle (12 L Tank)</option>
                        <option value="15">🛺 Auto-Rickshaw (15 L Tank)</option>
                        <option value="45" selected>🚗 Family Car (45 L Tank)</option>
                        <option value="200">🚌 Tour Bus (200 L Tank)</option>
                        <option value="350">🚛 Freight Truck (350 L Tank)</option>
                    </select>
                </div>
                <div>
                    <label class="text-[11px] text-slate-300 block mb-1">Current Fuel in Tank (L):</label>
                    <input id="sim15_curr" type="number" min="0" max="45" value="12.5" step="0.5" oninput="sim15Calc()" class="w-full bg-slate-800 border border-slate-700 rounded p-1 text-cyan-300 font-mono">
                </div>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 font-mono text-xs space-y-2">
            <div class="grid grid-cols-2 gap-2 text-center">
                <div class="p-2 rounded bg-slate-950 border border-slate-800">
                    <span class="text-[10px] text-slate-400 block font-sans">Fuel Needed to Top-Up</span>
                    <span id="sim15_needed" class="text-base font-bold text-emerald-400">32 L 500 mL</span>
                </div>
                <div class="p-2 rounded bg-slate-950 border border-slate-800">
                    <span class="text-[10px] text-slate-400 block font-sans">Cost to Full Tank (₹96/L)</span>
                    <span id="sim15_cost" class="text-base font-bold text-amber-300">₹3,120</span>
                </div>
            </div>
            <div id="sim15_expl" class="p-2 rounded bg-slate-950 font-sans text-[11px] text-slate-300">
                Tank Capacity: 45 L - Current: 12 L 500 mL = 32 L 500 mL needed to fill.
            </div>
        </div>
    </div>
    """,

    16: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🥤 Multi-Stage Commercial Packaging</span>
                <span class="text-[10px] text-emerald-300 font-mono">3-Stage Pipeline</span>
            </div>
            <div class="grid grid-cols-2 gap-2 mb-2">
                <button onclick="sim16Scenario('juice')" class="p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-left">
                    <div class="font-bold text-amber-300">🥤 Sugarcane Stall</div>
                    <div class="text-[10px] text-slate-400">10 L in 200 mL cups @ ₹15</div>
                </button>
                <button onclick="sim16Scenario('oil')" class="p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-left">
                    <div class="font-bold text-cyan-300">🧴 Mustard Oil Drum</div>
                    <div class="text-[10px] text-slate-400">15 L in 750 mL bottles @ ₹130</div>
                </button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 font-mono text-xs space-y-2">
            <div class="p-2.5 rounded bg-slate-950 border border-slate-800 space-y-1">
                <div class="flex justify-between text-slate-400">
                    <span>1. Unit Conversion:</span>
                    <span id="sim16_step1" class="text-cyan-300 font-bold">10 L = 10,000 mL</span>
                </div>
                <div class="flex justify-between text-slate-400">
                    <span>2. Number of Containers:</span>
                    <span id="sim16_step2" class="text-amber-300 font-bold">10,000 ÷ 200 = 50 Cups</span>
                </div>
                <div class="flex justify-between text-emerald-400 font-bold border-t border-slate-800 pt-1 text-sm">
                    <span>3. Total Revenue:</span>
                    <span id="sim16_step3">50 × ₹15 = ₹750</span>
                </div>
            </div>
            <div id="sim16_note" class="p-2 rounded bg-indigo-950/40 border border-indigo-800/40 font-sans text-[11px] text-indigo-200">
                Converting total litres to millilitres first makes container partition simple and accurate.
            </div>
        </div>
    </div>
    """
}

