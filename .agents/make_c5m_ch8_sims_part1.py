# -*- coding: utf-8 -*-
"""
Class 5 Mathematics Chapter 8: Weight and Capacity
Simulators 1 to 8 (HTML & SVG interactive components)
"""

simulators_part1 = {
    1: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">⚖️ Interactive Weighing Station</span>
                <span id="sim1_status" class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Ready</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Select an item to place it on the scale pan and test its reasonableness:</p>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5 mb-2">
                <button onclick="sim1Select('almirah')" class="sim1-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-left">🚪 Almirah</button>
                <button onclick="sim1Select('bed')" class="sim1-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-left">🛏️ Wooden Bed</button>
                <button onclick="sim1Select('rice')" class="sim1-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-left">🌾 Rice Sack</button>
                <button onclick="sim1Select('sofa')" class="sim1-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-left">🛋️ Sofa</button>
                <button onclick="sim1Select('water')" class="sim1-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-left">💧 Water Bottle</button>
                <button onclick="sim1Select('bucket')" class="sim1-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-left">🪣 Empty Bucket</button>
                <button onclick="sim1Select('fridge')" class="sim1-btn p-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-left">🧊 Refrigerator</button>
                <button onclick="sim1Select('absurd')" class="sim1-btn p-1.5 rounded bg-rose-950/60 hover:bg-rose-900/80 text-rose-300 border border-rose-700/60 text-left">⚠️ 50 kg Bottle?!</button>
            </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 bg-slate-900/60 p-3 rounded-xl border border-slate-700 items-center">
            <div class="flex flex-col items-center">
                <svg id="sim1_svg" viewBox="0 0 200 160" class="w-44 h-36">
                    <!-- Base and Pan -->
                    <rect x="30" y="140" width="140" height="15" rx="3" fill="#334155"/>
                    <rect x="95" y="100" width="10" height="40" fill="#475569"/>
                    <!-- Scale Pan -->
                    <ellipse cx="100" cy="100" rx="60" ry="10" fill="#64748b"/>
                    <!-- Item on Pan -->
                    <g id="sim1_item_icon" transform="translate(100, 75)">
                        <text x="0" y="0" text-anchor="middle" font-size="28">🌾</text>
                    </g>
                    <!-- Dial Scale Housing -->
                    <circle cx="100" cy="130" r="24" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
                    <!-- Needle -->
                    <line id="sim1_needle" x1="100" y1="130" x2="100" y2="110" stroke="#f43f5e" stroke-width="2.5" stroke-linecap="round"/>
                    <circle cx="100" cy="130" r="3" fill="#f43f5e"/>
                </svg>
                <div class="text-[11px] text-slate-400 font-mono">Analog Dial Scale</div>
            </div>

            <div class="space-y-2">
                <div class="p-2.5 rounded-lg bg-slate-950 border border-cyan-800/60 font-mono text-center">
                    <div class="text-[10px] text-cyan-400 tracking-wider uppercase">Digital Load Cell Readout</div>
                    <div id="sim1_digital" class="text-2xl font-black text-cyan-300 mt-1">25.00 kg</div>
                    <div id="sim1_grams" class="text-xs text-slate-400">= 25,000 g</div>
                </div>
                <div id="sim1_verdict" class="p-2.5 rounded-lg bg-emerald-950/60 border border-emerald-700/60 text-[11px] text-emerald-200 leading-tight">
                    ✅ <strong>Reasonable:</strong> 25 kg is a standard mass for a wholesale grocery sack of grain.
                </div>
            </div>
        </div>
    </div>
    """,

    2: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-1">
                <span class="font-bold text-amber-400">📏 Synchronized Double Number Line</span>
                <span class="text-[11px] text-cyan-300 font-mono">1 kg = 1,000 g</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Drag the slider or click standard fraction benchmarks to observe kg and g equivalence:</p>
            <div class="flex flex-wrap gap-1.5 mb-2">
                <button onclick="sim2Set(0.25)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">1/4 kg (250 g)</button>
                <button onclick="sim2Set(0.5)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">1/2 kg (500 g)</button>
                <button onclick="sim2Set(0.75)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">3/4 kg (750 g)</button>
                <button onclick="sim2Set(1.0)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">1 kg (1,000 g)</button>
                <button onclick="sim2Set(1.5)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">1 1/2 kg (1,500 g)</button>
                <button onclick="sim2Set(2.25)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">2 1/4 kg (2,250 g)</button>
            </div>
            <div class="flex items-center gap-3">
                <input id="sim2_slider" type="range" min="0" max="3" step="0.25" value="1" oninput="sim2Update(parseFloat(this.value))" class="w-full accent-cyan-400">
                <span id="sim2_slider_val" class="font-mono text-cyan-300 font-bold min-w-[60px] text-right">1.00 kg</span>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 flex flex-col items-center">
            <svg id="sim2_svg" viewBox="0 0 460 130" class="w-full max-w-lg h-32">
                <!-- Kilogram Axis (Top) -->
                <line x1="40" y1="35" x2="420" y2="35" stroke="#38bdf8" stroke-width="3"/>
                <text x="25" y="38" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="end">kg</text>
                <!-- Gram Axis (Bottom) -->
                <line x1="40" y1="85" x2="420" y2="85" stroke="#34d399" stroke-width="3"/>
                <text x="25" y="88" fill="#34d399" font-size="11" font-weight="bold" text-anchor="end">g</text>

                <!-- Ticks for kg: 0, 0.5, 1, 1.5, 2, 2.5, 3 -->
                <!-- x positions: 0->40, 1->166.6, 2->293.3, 3->420 -->
                <g font-size="10" fill="#94a3b8" text-anchor="middle">
                    <line x1="40" y1="28" x2="40" y2="42" stroke="#38bdf8" stroke-width="2"/>
                    <text x="40" y="24">0</text>
                    <line x1="103" y1="30" x2="103" y2="40" stroke="#38bdf8" stroke-width="1.5"/>
                    <text x="103" y="24">0.5</text>
                    <line x1="166" y1="28" x2="166" y2="42" stroke="#38bdf8" stroke-width="2"/>
                    <text x="166" y="24">1.0</text>
                    <line x1="230" y1="30" x2="230" y2="40" stroke="#38bdf8" stroke-width="1.5"/>
                    <text x="230" y="24">1.5</text>
                    <line x1="293" y1="28" x2="293" y2="42" stroke="#38bdf8" stroke-width="2"/>
                    <text x="293" y="24">2.0</text>
                    <line x1="356" y1="30" x2="356" y2="40" stroke="#38bdf8" stroke-width="1.5"/>
                    <text x="356" y="24">2.5</text>
                    <line x1="420" y1="28" x2="420" y2="42" stroke="#38bdf8" stroke-width="2"/>
                    <text x="420" y="24">3.0</text>

                    <!-- Ticks for grams -->
                    <line x1="40" y1="78" x2="40" y2="92" stroke="#34d399" stroke-width="2"/>
                    <text x="40" y="104">0</text>
                    <line x1="103" y1="80" x2="103" y2="90" stroke="#34d399" stroke-width="1.5"/>
                    <text x="103" y="104">500</text>
                    <line x1="166" y1="78" x2="166" y2="92" stroke="#34d399" stroke-width="2"/>
                    <text x="166" y="104">1,000</text>
                    <line x1="230" y1="80" x2="230" y2="90" stroke="#34d399" stroke-width="1.5"/>
                    <text x="230" y="104">1,500</text>
                    <line x1="293" y1="78" x2="293" y2="92" stroke="#34d399" stroke-width="2"/>
                    <text x="293" y="104">2,000</text>
                    <line x1="356" y1="80" x2="356" y2="90" stroke="#34d399" stroke-width="1.5"/>
                    <text x="356" y="104">2,500</text>
                    <line x1="420" y1="78" x2="420" y2="92" stroke="#34d399" stroke-width="2"/>
                    <text x="420" y="104">3,000</text>
                </g>

                <!-- Indicator Line connecting both axes -->
                <line id="sim2_cursor" x1="166" y1="18" x2="166" y2="108" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="3 3"/>
                <circle id="sim2_dot_top" cx="166" cy="35" r="5" fill="#f59e0b"/>
                <circle id="sim2_dot_bot" cx="166" cy="85" r="5" fill="#f59e0b"/>
            </svg>
            <div id="sim2_display" class="font-mono text-xs font-bold text-amber-300 mt-1">
                1.00 kg = 1,000 g
            </div>
        </div>
    </div>
    """,

    3: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🔄 Step-by-Step Unit Converter</span>
                <span class="text-[10px] text-cyan-300 font-mono">3-Digit Placeholder Rule</span>
            </div>
            <div class="grid grid-cols-2 gap-3 mb-2">
                <div>
                    <label class="text-[11px] text-slate-300 block mb-1">Kilograms (kg):</label>
                    <input id="sim3_kg" type="number" min="0" max="99" value="4" oninput="sim3Calc()" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-cyan-300 font-mono text-sm">
                </div>
                <div>
                    <label class="text-[11px] text-slate-300 block mb-1">Grams (g):</label>
                    <input id="sim3_g" type="number" min="0" max="999" value="75" oninput="sim3Calc()" class="w-full bg-slate-800 border border-slate-700 rounded p-1.5 text-cyan-300 font-mono text-sm">
                </div>
            </div>
            <div class="flex flex-wrap gap-1.5">
                <button onclick="sim3Preset(4, 75)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-200 border border-slate-700 text-[11px]">4 kg 75 g</button>
                <button onclick="sim3Preset(3, 500)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-200 border border-slate-700 text-[11px]">3 kg 500 g</button>
                <button onclick="sim3Preset(6, 8)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-200 border border-slate-700 text-[11px]">6 kg 8 g</button>
                <button onclick="sim3Preset(9, 40)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-200 border border-slate-700 text-[11px]">9 kg 40 g</button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div class="p-2 rounded bg-slate-950 border border-slate-800 font-mono text-xs space-y-1">
                <div class="flex justify-between text-slate-400">
                    <span>1. Kilograms to Grams:</span>
                    <span id="sim3_step1" class="text-cyan-300">4 × 1,000 = 4,000 g</span>
                </div>
                <div class="flex justify-between text-slate-400">
                    <span>2. Add Grams (with leading zeros):</span>
                    <span id="sim3_step2" class="text-amber-300">+ 075 g</span>
                </div>
                <div class="flex justify-between text-emerald-400 font-bold border-t border-slate-800 pt-1 text-sm">
                    <span>Total Mass:</span>
                    <span id="sim3_total">4,075 g</span>
                </div>
            </div>

            <div id="sim3_warning" class="p-2 rounded-lg bg-amber-950/50 border border-amber-700/50 text-[11px] text-amber-200 leading-tight">
                ⚠️ <strong>Leading Zero Alert:</strong> 75 g has no hundreds, so write as <strong>075</strong>. Never write 4,750 g!
            </div>
        </div>
    </div>
    """,

    4: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🍉 Picnic Fruit Comparator</span>
                <span class="text-[10px] text-slate-400">Select any 2 fruits to compare</span>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <div>
                    <label class="text-[11px] text-slate-300 block mb-1">Pan A (Left):</label>
                    <select id="sim4_left" onchange="sim4Compare()" class="w-full bg-slate-800 border border-slate-700 rounded p-1 text-slate-200">
                        <option value="3200">🍉 Watermelon (3 kg 200 g)</option>
                        <option value="2500">🍎 Apples (2 kg 500 g)</option>
                        <option value="1800">🍍 Pineapple (1 kg 800 g)</option>
                        <option value="1250">🥭 Mangoes (1 kg 250 g)</option>
                    </select>
                </div>
                <div>
                    <label class="text-[11px] text-slate-300 block mb-1">Pan B (Right):</label>
                    <select id="sim4_right" onchange="sim4Compare()" class="w-full bg-slate-800 border border-slate-700 rounded p-1 text-slate-200">
                        <option value="2500">🍎 Apples (2 kg 500 g)</option>
                        <option value="3200">🍉 Watermelon (3 kg 200 g)</option>
                        <option value="1800">🍍 Pineapple (1 kg 800 g)</option>
                        <option value="1250">🥭 Mangoes (1 kg 250 g)</option>
                    </select>
                </div>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 flex flex-col items-center">
            <svg id="sim4_svg" viewBox="0 0 280 120" class="w-full max-w-xs h-28">
                <!-- Fulcrum Base -->
                <polygon points="140,70 125,110 155,110" fill="#475569"/>
                <!-- Balance Beam -->
                <g id="sim4_beam" transform="rotate(-6, 140, 70)">
                    <rect x="20" y="67" width="240" height="6" rx="2" fill="#94a3b8"/>
                    <!-- Left Pan Strings & Pan -->
                    <line x1="40" y1="73" x2="25" y2="95" stroke="#cbd5e1" stroke-width="1.5"/>
                    <line x1="40" y1="73" x2="55" y2="95" stroke="#cbd5e1" stroke-width="1.5"/>
                    <ellipse cx="40" cy="95" rx="20" ry="4" fill="#64748b"/>
                    <text id="sim4_icon_l" x="40" y="90" text-anchor="middle" font-size="16">🍉</text>
                    <!-- Right Pan Strings & Pan -->
                    <line x1="240" y1="73" x2="225" y2="95" stroke="#cbd5e1" stroke-width="1.5"/>
                    <line x1="240" y1="73" x2="255" y2="95" stroke="#cbd5e1" stroke-width="1.5"/>
                    <ellipse cx="240" cy="95" rx="20" ry="4" fill="#64748b"/>
                    <text id="sim4_icon_r" x="240" y="90" text-anchor="middle" font-size="16">🍎</text>
                </g>
            </svg>
            <div id="sim4_statement" class="p-2 rounded bg-slate-950 font-mono text-center font-bold text-xs text-amber-300 w-full mt-1">
                3,200 g > 2,500 g (Watermelon is heavier by 700 g)
            </div>
        </div>
    </div>
    """,

    5: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🔬 Precision Digital Micro-Balance</span>
                <span class="text-[10px] text-emerald-300 font-mono">1 g = 1,000 mg</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Toggle micro-objects to stack them on the micro-balance pan:</p>
            <div class="grid grid-cols-3 gap-1.5 mb-2">
                <button id="sim5_b1" onclick="sim5Toggle(1)" class="p-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-left">🐜 Ant (5 mg)</button>
                <button id="sim5_b2" onclick="sim5Toggle(2)" class="p-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-left">🧂 Salt (1 mg)</button>
                <button id="sim5_b3" onclick="sim5Toggle(3)" class="p-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-left">💊 Pill (500 mg)</button>
                <button id="sim5_b4" onclick="sim5Toggle(4)" class="p-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-left">🪶 Feather (15 mg)</button>
                <button id="sim5_b5" onclick="sim5Toggle(5)" class="p-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-left">💍 Ring (4,000 mg)</button>
                <button id="sim5_b6" onclick="sim5Toggle(6)" class="p-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-left">☕ Sugar (5,000 mg)</button>
            </div>
            <button onclick="sim5Reset()" class="w-full py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-400 text-[11px]">Clear Pan</button>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 space-y-2">
            <div class="p-3 rounded-xl bg-slate-950 border border-emerald-800/60 font-mono text-center">
                <div class="text-[10px] text-slate-400 uppercase">Total Micro-Mass Display</div>
                <div id="sim5_display_mg" class="text-2xl font-black text-emerald-400 mt-1">0 mg</div>
                <div id="sim5_display_g" class="text-xs text-cyan-300">= 0.000 g</div>
            </div>
            <div id="sim5_notes" class="p-2 rounded bg-slate-800/80 text-[11px] text-slate-300">
                Pan is empty. Click any item above to weigh it on the micro-scale!
            </div>
        </div>
    </div>
    """,

    6: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🚢 The King's Elephant Boat Lab</span>
                <span class="text-[10px] text-cyan-300 font-mono">1 t = 10 q = 1,000 kg</span>
            </div>
            <p class="text-[11px] text-slate-300 mb-2">Simulate Archimedes' boat displacement to weigh an elephant using 50 kg stone bags:</p>
            <div class="flex gap-2">
                <button id="sim6_btn_ele" onclick="sim6ToggleElephant()" class="flex-1 py-1.5 rounded bg-indigo-900/80 hover:bg-indigo-800 text-indigo-200 border border-indigo-700 font-semibold">Load Elephant</button>
                <button onclick="sim6AddStones(10)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700">+10 Stone Bags</button>
                <button onclick="sim6Reset()" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-400 border border-slate-700">Reset</button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 flex flex-col items-center">
            <svg id="sim6_svg" viewBox="0 0 320 130" class="w-full max-w-sm h-32">
                <!-- Water Area -->
                <rect x="0" y="75" width="320" height="55" fill="#0284c7" opacity="0.4"/>
                <line x1="0" y1="75" x2="320" y2="75" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
                <!-- Boat Hull -->
                <g id="sim6_boat" transform="translate(0, 0)">
                    <polygon points="50,70 80,105 240,105 270,70" fill="#78350f" stroke="#b45309" stroke-width="2"/>
                    <!-- Chalk Line on Hull -->
                    <line id="sim6_waterline" x1="60" y1="85" x2="260" y2="85" stroke="#fbbf24" stroke-width="2" stroke-dasharray="2 2"/>
                    <!-- Cargo (Elephant or Stones) -->
                    <text id="sim6_cargo_icon" x="160" y="65" text-anchor="middle" font-size="32">⛵</text>
                </g>
            </svg>
            <div class="grid grid-cols-3 gap-2 w-full mt-2 font-mono text-center text-xs">
                <div class="p-1.5 rounded bg-slate-950 border border-slate-800">
                    <span class="text-[10px] text-slate-400 block">Kilograms</span>
                    <span id="sim6_kg" class="font-bold text-emerald-400">0 kg</span>
                </div>
                <div class="p-1.5 rounded bg-slate-950 border border-slate-800">
                    <span class="text-[10px] text-slate-400 block">Quintals (100 kg)</span>
                    <span id="sim6_q" class="font-bold text-amber-300">0 q</span>
                </div>
                <div class="p-1.5 rounded bg-slate-950 border border-slate-800">
                    <span class="text-[10px] text-slate-400 block">Metric Tonnes</span>
                    <span id="sim6_t" class="font-bold text-cyan-300">0.0 t</span>
                </div>
            </div>
        </div>
    </div>
    """,

    7: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🛒 Column Addition Workshop</span>
                <span class="text-[10px] text-emerald-300 font-mono">Base-1,000 Regrouping</span>
            </div>
            <div class="flex gap-2 mb-2">
                <button onclick="sim7Preset(45, 750, 38, 650)" class="flex-1 py-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-[11px]">Wedding Feast</button>
                <button onclick="sim7Preset(16, 450, 23, 800)" class="flex-1 py-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-[11px]">Vegetable Mart</button>
            </div>
            <div class="flex gap-2">
                <button id="sim7_step_btn" onclick="sim7NextStep()" class="w-full py-1.5 rounded bg-emerald-600 hover:bg-emerald-500 font-bold text-slate-950 text-xs">Execute Next Step ▶</button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 font-mono text-xs">
            <div class="grid grid-cols-3 text-slate-400 border-b border-slate-700 pb-1 mb-1">
                <span>ITEM</span>
                <span class="text-right">KILOGRAMS</span>
                <span class="text-right">GRAMS</span>
            </div>
            <div class="grid grid-cols-3 text-amber-400 text-[11px] mb-1">
                <span>Carry:</span>
                <span id="sim7_carry_kg" class="text-right">-</span>
                <span class="text-right">-</span>
            </div>
            <div class="grid grid-cols-3 text-slate-200 py-1">
                <span id="sim7_name1">Basmati Rice</span>
                <span id="sim7_kg1" class="text-right font-bold">45</span>
                <span id="sim7_g1" class="text-right font-bold">750</span>
            </div>
            <div class="grid grid-cols-3 text-slate-200 py-1 border-b border-slate-700">
                <span id="sim7_name2">Wheat Flour</span>
                <span id="sim7_kg2" class="text-right font-bold">38</span>
                <span id="sim7_g2" class="text-right font-bold">650</span>
            </div>
            <div class="grid grid-cols-3 text-emerald-400 font-black text-sm pt-2">
                <span>TOTAL:</span>
                <span id="sim7_tot_kg" class="text-right">-</span>
                <span id="sim7_tot_g" class="text-right">-</span>
            </div>
            <div id="sim7_expl" class="mt-2 p-2 rounded bg-slate-950 text-[11px] font-sans text-slate-300">
                Click 'Execute Next Step' to start column addition!
            </div>
        </div>
    </div>
    """,

    8: """
    <div class="flex flex-col h-full justify-between gap-3 text-xs">
        <div class="bg-slate-900/90 p-3 rounded-xl border border-slate-700">
            <div class="flex items-center justify-between mb-2">
                <span class="font-bold text-amber-400">🧅 Column Subtraction Workshop</span>
                <span class="text-[10px] text-cyan-300 font-mono">Base-1,000 Borrowing</span>
            </div>
            <div class="flex gap-2 mb-2">
                <button onclick="sim8Preset(50, 200, 27, 650)" class="flex-1 py-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-[11px]">Restaurant Onions</button>
                <button onclick="sim8Preset(15, 100, 3, 750)" class="flex-1 py-1 rounded bg-slate-800 text-slate-200 border border-slate-700 text-[11px]">Leaking Sandbag</button>
            </div>
            <div class="flex gap-2">
                <button id="sim8_step_btn" onclick="sim8NextStep()" class="w-full py-1.5 rounded bg-cyan-600 hover:bg-cyan-500 font-bold text-slate-950 text-xs">Execute Next Step ▶</button>
            </div>
        </div>

        <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-700 font-mono text-xs">
            <div class="grid grid-cols-3 text-slate-400 border-b border-slate-700 pb-1 mb-1">
                <span>STAGE</span>
                <span class="text-right">KILOGRAMS</span>
                <span class="text-right">GRAMS</span>
            </div>
            <div class="grid grid-cols-3 text-cyan-400 text-[11px] mb-1">
                <span>Borrowed State:</span>
                <span id="sim8_borrow_kg" class="text-right">-</span>
                <span id="sim8_borrow_g" class="text-right">-</span>
            </div>
            <div class="grid grid-cols-3 text-slate-200 py-1">
                <span>Original Stock:</span>
                <span id="sim8_kg1" class="text-right font-bold">50</span>
                <span id="sim8_g1" class="text-right font-bold">200</span>
            </div>
            <div class="grid grid-cols-3 text-slate-200 py-1 border-b border-slate-700">
                <span>Used / Leaked:</span>
                <span id="sim8_kg2" class="text-right font-bold">- 27</span>
                <span id="sim8_g2" class="text-right font-bold">- 650</span>
            </div>
            <div class="grid grid-cols-3 text-emerald-400 font-black text-sm pt-2">
                <span>REMAINING:</span>
                <span id="sim8_tot_kg" class="text-right">-</span>
                <span id="sim8_tot_g" class="text-right">-</span>
            </div>
            <div id="sim8_expl" class="mt-2 p-2 rounded bg-slate-950 text-[11px] font-sans text-slate-300">
                Click 'Execute Next Step' to see 1 kg borrowed and transformed into +1,000 g!
            </div>
        </div>
    </div>
    """
}

