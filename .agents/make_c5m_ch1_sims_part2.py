# make_c5m_ch1_sims_part2.py
"""Simulators 9 to 16 for Class 5 Mathematics Chapter 1: We the Travellers - I."""

SIM_9_HTML = '''
<div class="space-y-4">
    <div class="bg-indigo-950/60 p-4 rounded-xl border border-indigo-500/30 text-center">
        <h4 class="text-sm font-bold text-indigo-300 uppercase tracking-wider mb-1">Dual-Rounding Milestone Analyzer</h4>
        <p class="text-xs text-slate-300">Discover fascinating numbers where rounding to the nearest 100 yields the EXACT same milestone as rounding to the nearest 1,000!</p>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setRoundingNum(2980)" class="px-3 py-2 bg-slate-800 hover:bg-indigo-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Test 2,980</button>
        <button onclick="setRoundingNum(4960)" class="px-3 py-2 bg-slate-800 hover:bg-indigo-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Test 4,960</button>
        <button onclick="setRoundingNum(7975)" class="px-3 py-2 bg-slate-800 hover:bg-indigo-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Test 7,975</button>
        <button onclick="setRoundingNum(3420)" class="px-3 py-2 bg-slate-800 hover:bg-indigo-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Test 3,420 (Differs)</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800">
        <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-semibold text-slate-400">Current Value:</span>
            <span id="currentRoundVal" class="text-xl font-bold font-mono text-amber-400">2,980</span>
        </div>
        <input type="range" id="roundSlider" min="2000" max="6000" step="10" value="2980" oninput="updateDualRounding(this.value)" class="w-full accent-indigo-500">
        <div class="flex justify-between text-[11px] text-slate-400 font-mono mt-1">
            <span>2,000</span>
            <span>4,000</span>
            <span>6,000</span>
        </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <div class="bg-slate-900/80 p-3.5 rounded-xl border border-blue-500/30">
            <div class="flex justify-between items-center mb-1">
                <span class="text-xs font-bold text-blue-300">Nearest Hundred (100s)</span>
                <span class="text-[10px] px-2 py-0.5 bg-blue-950 text-blue-400 rounded">Look at Tens digit</span>
            </div>
            <div class="text-xl font-mono font-bold text-white mt-1" id="resRound100">3,000</div>
            <p class="text-[11px] text-slate-400 mt-1" id="expRound100">Tens digit 8 &ge; 5 &rarr; Round up to 3,000</p>
        </div>
        <div class="bg-slate-900/80 p-3.5 rounded-xl border border-purple-500/30">
            <div class="flex justify-between items-center mb-1">
                <span class="text-xs font-bold text-purple-300">Nearest Thousand (1,000s)</span>
                <span class="text-[10px] px-2 py-0.5 bg-purple-950 text-purple-400 rounded">Look at Hundreds digit</span>
            </div>
            <div class="text-xl font-mono font-bold text-white mt-1" id="resRound1000">3,000</div>
            <p class="text-[11px] text-slate-400 mt-1" id="expRound1000">Hundreds digit 9 &ge; 5 &rarr; Round up to 3,000</p>
        </div>
    </div>

    <div id="dualRoundBanner" class="p-3 bg-emerald-950/60 border border-emerald-500/40 rounded-xl text-center text-xs text-emerald-300 font-medium">
        Awesome match! Both roundings land on 3,000!
    </div>
</div>
'''

SIM_10_HTML = '''
<div class="space-y-4">
    <div class="bg-cyan-950/60 p-4 rounded-xl border border-cyan-500/30 text-center">
        <h4 class="text-sm font-bold text-cyan-300 uppercase tracking-wider mb-1">Distance = Speed &times; Time Flight Deck</h4>
        <p class="text-xs text-slate-300">Compare historic and futuristic journeys across India and outer space over multiple hours.</p>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setSpeedVehicle('walk', 4)" class="px-2.5 py-2 bg-slate-800 hover:bg-cyan-600 text-xs font-medium rounded-lg text-white border border-slate-700 transition">Walking (4 km/h)</button>
        <button onclick="setSpeedVehicle('train', 120)" class="px-2.5 py-2 bg-slate-800 hover:bg-cyan-600 text-xs font-medium rounded-lg text-white border border-slate-700 transition">Train (120 km/h)</button>
        <button onclick="setSpeedVehicle('flight', 800)" class="px-2.5 py-2 bg-slate-800 hover:bg-cyan-600 text-xs font-medium rounded-lg text-white border border-slate-700 transition">Flight (800 km/h)</button>
        <button onclick="setSpeedVehicle('rocket', 28000)" class="px-2.5 py-2 bg-slate-800 hover:bg-cyan-600 text-xs font-medium rounded-lg text-white border border-slate-700 transition">Rocket (28,000 km/h)</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 space-y-3">
        <div class="flex justify-between items-center text-xs">
            <span class="text-slate-400">Selected Vehicle: <strong id="selectedVehicleName" class="text-cyan-400">Train</strong></span>
            <span class="text-slate-400">Speed: <strong id="selectedVehicleSpeed" class="text-white font-mono">120 km/h</strong></span>
        </div>
        <div>
            <div class="flex justify-between items-center text-xs mb-1">
                <span class="text-slate-400">Travel Duration:</span>
                <span class="text-amber-400 font-bold font-mono" id="hoursVal">4 hours</span>
            </div>
            <input type="range" id="timeSlider" min="1" max="12" step="1" value="4" oninput="updateSpeedCalc(this.value)" class="w-full accent-cyan-500">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono mt-1">
                <span>1 hr</span>
                <span>3 hr</span>
                <span>6 hr</span>
                <span>9 hr</span>
                <span>12 hr</span>
            </div>
        </div>
    </div>

    <div class="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 p-4 rounded-xl border border-indigo-500/30 text-center">
        <div class="text-[11px] uppercase tracking-wider text-slate-400 font-semibold mb-1">Total Distance Covered</div>
        <div class="text-2xl sm:text-3xl font-extrabold font-mono text-cyan-300" id="totalDistDisplay">480 km</div>
        <div class="text-xs text-slate-300 mt-1 font-mono" id="distFormulaDisplay">120 km/h &times; 4 h = 480 km</div>
    </div>
</div>
'''

SIM_11_HTML = '''
<div class="space-y-4">
    <div class="bg-amber-950/60 p-4 rounded-xl border border-amber-500/30 text-center">
        <h4 class="text-sm font-bold text-amber-300 uppercase tracking-wider mb-1">School Field Trip Fleet Dispatcher</h4>
        <p class="text-xs text-slate-300">Calculate how many 50-seater standard buses and 15-seater mini-vans are needed for your school excursion.</p>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800">
        <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-semibold text-slate-300">Total Students &amp; Teachers Going:</span>
            <span id="tripHeadcount" class="text-lg font-bold font-mono text-amber-400">135 Passengers</span>
        </div>
        <input type="range" id="tripSlider" min="20" max="250" step="5" value="135" oninput="updateTripFleet(this.value)" class="w-full accent-amber-500">
        <div class="flex justify-between text-[11px] text-slate-400 font-mono mt-1">
            <span>20</span>
            <span>75</span>
            <span>135</span>
            <span>200</span>
            <span>250</span>
        </div>
    </div>

    <div class="grid grid-cols-2 gap-3">
        <div class="bg-slate-900/80 p-3.5 rounded-xl border border-amber-500/30 text-center">
            <div class="text-xs text-slate-400 font-medium">Standard 50-Seater Buses</div>
            <div class="text-2xl font-mono font-bold text-amber-300 mt-1" id="bus50Count">2 Buses</div>
            <div class="text-[11px] text-slate-400 mt-0.5" id="bus50Seats">Carries 100 passengers</div>
        </div>
        <div class="bg-slate-900/80 p-3.5 rounded-xl border border-blue-500/30 text-center">
            <div class="text-xs text-slate-400 font-medium">Mini 15-Seater Vans</div>
            <div class="text-2xl font-mono font-bold text-blue-300 mt-1" id="van15Count">3 Vans</div>
            <div class="text-[11px] text-slate-400 mt-0.5" id="van15Seats">Carries remaining 35 (45 seats)</div>
        </div>
    </div>

    <div class="p-3 bg-slate-900 rounded-xl border border-slate-800 text-xs text-slate-300 space-y-1">
        <div class="flex justify-between">
            <span>Total Seats Booked:</span>
            <span class="font-mono font-bold text-emerald-400" id="totalSeatsBooked">145 seats</span>
        </div>
        <div class="flex justify-between">
            <span>Empty Spare Seats:</span>
            <span class="font-mono font-bold text-slate-400" id="emptySeatsCount">10 seats</span>
        </div>
    </div>
</div>
'''

SIM_12_HTML = '''
<div class="space-y-4">
    <div class="bg-teal-950/60 p-4 rounded-xl border border-teal-500/30 text-center">
        <h4 class="text-sm font-bold text-teal-300 uppercase tracking-wider mb-1">Real-World 5-Digit Number Scope</h4>
        <p class="text-xs text-slate-300">Tap everyday scenarios to visualize just how vast numbers between 10,000 and 100,000 really are!</p>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="setContextNumber('book', 18450, 'Words in Joyful Maths Textbook', 'TTh: 1, Th: 8, H: 4, T: 5, O: 0')" class="px-2.5 py-2 bg-slate-800 hover:bg-teal-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Book Words</button>
        <button onclick="setContextNumber('stadium', 42500, 'Spectators at Cricket Stadium', 'TTh: 4, Th: 2, H: 5, T: 0, O: 0')" class="px-2.5 py-2 bg-slate-800 hover:bg-teal-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Cricket Match</button>
        <button onclick="setContextNumber('forest', 25680, 'Trees in Forest Reserve', 'TTh: 2, Th: 5, H: 6, T: 8, O: 0')" class="px-2.5 py-2 bg-slate-800 hover:bg-teal-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Reserve Trees</button>
        <button onclick="setContextNumber('town', 68900, 'Town Population Census', 'TTh: 6, Th: 8, H: 9, T: 0, O: 0')" class="px-2.5 py-2 bg-slate-800 hover:bg-teal-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Town Census</button>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 text-center space-y-2">
        <div class="text-xs text-teal-400 font-semibold" id="contextTitle">Words in Joyful Maths Textbook</div>
        <div class="text-3xl sm:text-4xl font-extrabold font-mono text-white tracking-wider" id="contextNum">18,450</div>
        <div class="text-xs text-slate-400" id="contextWords">Eighteen thousand four hundred fifty</div>
    </div>

    <div class="bg-slate-900/80 p-3.5 rounded-xl border border-teal-500/20">
        <div class="text-xs font-semibold text-slate-400 mb-2">Place Value Breakdown:</div>
        <div class="grid grid-cols-5 gap-2 text-center text-xs font-mono" id="contextBreakdown">
            <div class="bg-teal-950/60 p-2 rounded border border-teal-500/30"><div class="text-[10px] text-teal-400">TTh</div><div class="font-bold text-white text-base">1</div><div class="text-[9px] text-slate-400">10,000</div></div>
            <div class="bg-cyan-950/60 p-2 rounded border border-cyan-500/30"><div class="text-[10px] text-cyan-400">Th</div><div class="font-bold text-white text-base">8</div><div class="text-[9px] text-slate-400">8,000</div></div>
            <div class="bg-blue-950/60 p-2 rounded border border-blue-500/30"><div class="text-[10px] text-blue-400">H</div><div class="font-bold text-white text-base">4</div><div class="text-[9px] text-slate-400">400</div></div>
            <div class="bg-indigo-950/60 p-2 rounded border border-indigo-500/30"><div class="text-[10px] text-indigo-400">T</div><div class="font-bold text-white text-base">5</div><div class="text-[9px] text-slate-400">50</div></div>
            <div class="bg-violet-950/60 p-2 rounded border border-violet-500/30"><div class="text-[10px] text-violet-400">O</div><div class="font-bold text-white text-base">0</div><div class="text-[9px] text-slate-400">0</div></div>
        </div>
    </div>
</div>
'''

SIM_13_HTML = '''
<div class="space-y-4">
    <div class="bg-emerald-950/60 p-4 rounded-xl border border-emerald-500/30 text-center">
        <h4 class="text-sm font-bold text-emerald-300 uppercase tracking-wider mb-1">River Crossing Logic Game</h4>
        <p class="text-xs text-slate-300">Help the boatman ferry the Lion, Sheep, and Grass across the river safely. The boat can carry only the boatman plus ONE passenger!</p>
    </div>

    <!-- River Scene -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800">
        <div class="grid grid-cols-3 gap-2 text-center text-xs">
            <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800">
                <div class="font-bold text-emerald-400 mb-2">Left Bank (Start)</div>
                <div id="leftBankItems" class="flex flex-wrap justify-center gap-1.5 min-h-[50px]">
                    <span class="px-2 py-1 bg-amber-900/60 border border-amber-600/40 rounded text-amber-200">🦁 Lion</span>
                    <span class="px-2 py-1 bg-blue-900/60 border border-blue-600/40 rounded text-blue-200">🐑 Sheep</span>
                    <span class="px-2 py-1 bg-green-900/60 border border-green-600/40 rounded text-green-200">🌾 Grass</span>
                </div>
            </div>

            <div class="bg-blue-950/40 p-3 rounded-lg border border-blue-500/30 flex flex-col justify-between">
                <div class="font-bold text-blue-300">River &amp; Boat</div>
                <div id="boatDisplay" class="my-auto py-2 px-1 bg-amber-950/80 rounded border border-amber-700/50">
                    <div class="text-[11px] text-amber-300 font-semibold">🚣 Boatman (Left Bank)</div>
                    <div id="boatCargo" class="text-xs text-slate-400 mt-0.5">Empty</div>
                </div>
                <div class="text-[10px] text-slate-400">Capacity: 1 item</div>
            </div>

            <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800">
                <div class="font-bold text-teal-400 mb-2">Right Bank (Goal)</div>
                <div id="rightBankItems" class="flex flex-wrap justify-center gap-1.5 min-h-[50px]">
                    <span class="text-slate-500 italic text-[11px]">None yet</span>
                </div>
            </div>
        </div>

        <div id="riverGameStatus" class="mt-3 p-2 bg-slate-950 rounded text-center text-xs text-slate-300 border border-slate-800">
            Rules: Lion eats Sheep if left alone. Sheep eats Grass if left alone.
        </div>
    </div>

    <!-- Action Controls -->
    <div class="flex flex-wrap justify-center gap-2">
        <button onclick="riverLoad('lion')" class="px-3 py-1.5 bg-amber-900/80 hover:bg-amber-700 text-amber-200 text-xs font-semibold rounded-lg border border-amber-600/40 transition">Board 🦁 Lion</button>
        <button onclick="riverLoad('sheep')" class="px-3 py-1.5 bg-blue-900/80 hover:bg-blue-700 text-blue-200 text-xs font-semibold rounded-lg border border-blue-600/40 transition">Board 🐑 Sheep</button>
        <button onclick="riverLoad('grass')" class="px-3 py-1.5 bg-green-900/80 hover:bg-green-700 text-green-200 text-xs font-semibold rounded-lg border border-green-600/40 transition">Board 🌾 Grass</button>
        <button onclick="riverRowBoat()" class="px-4 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold rounded-lg transition shadow">Row Boat &rarr;</button>
        <button onclick="riverReset()" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold rounded-lg border border-slate-700 transition">Reset</button>
        <button onclick="riverAutoSolve()" class="px-3 py-1.5 bg-emerald-700 hover:bg-emerald-600 text-white text-xs font-bold rounded-lg transition">Show Solution</button>
    </div>
</div>
'''

SIM_14_HTML = '''
<div class="space-y-4">
    <div class="bg-violet-950/60 p-4 rounded-xl border border-violet-500/30 text-center">
        <h4 class="text-sm font-bold text-violet-300 uppercase tracking-wider mb-1">Pile of Pebbles Strategy Lab</h4>
        <p class="text-xs text-slate-300">Start with 15 pebbles. Each turn, take 1, 2, or 3 pebbles. The player who takes the last pebble wins! Discover the multiple-of-4 strategy.</p>
    </div>

    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 text-center">
        <div class="text-xs text-slate-400 font-semibold mb-2">Pebbles Remaining: <span id="pebbleCountDisplay" class="text-2xl font-bold font-mono text-amber-400 ml-1">15</span></div>
        <div id="pebblesContainer" class="flex flex-wrap justify-center gap-2 min-h-[50px] p-2 bg-slate-950/70 rounded-lg border border-slate-800">
            <!-- Pebbles rendered dynamically -->
        </div>
        <div class="text-xs text-slate-400 mt-2" id="pebbleStrategyHint">Winning secret: 15 = 4 &times; 3 + 3. Leave your opponent with a multiple of 4!</div>
    </div>

    <div class="grid grid-cols-3 gap-2">
        <button onclick="playerTakePebbles(1)" class="px-3 py-2 bg-slate-800 hover:bg-violet-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">Take 1 Pebble</button>
        <button onclick="playerTakePebbles(2)" class="px-3 py-2 bg-slate-800 hover:bg-violet-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">Take 2 Pebbles</button>
        <button onclick="playerTakePebbles(3)" class="px-3 py-2 bg-slate-800 hover:bg-violet-600 text-xs font-bold text-white rounded-lg border border-slate-700 transition">Take 3 Pebbles</button>
    </div>

    <div id="pebbleGameStatus" class="p-3 bg-indigo-950/60 border border-indigo-500/30 rounded-xl text-xs text-indigo-300 text-center">
        Your turn! Pick 1, 2, or 3 pebbles.
    </div>

    <div class="flex justify-center">
        <button onclick="resetPebblesGame()" class="px-4 py-1.5 bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 rounded-lg border border-slate-700 transition">Restart Game (15 Pebbles)</button>
    </div>
</div>
'''

SIM_15_HTML = '''
<div class="space-y-4">
    <div class="bg-fuchsia-950/60 p-4 rounded-xl border border-fuchsia-500/30 text-center">
        <h4 class="text-sm font-bold text-fuchsia-300 uppercase tracking-wider mb-1">Magic 9 Digit-Difference Engine</h4>
        <p class="text-xs text-slate-300">Choose two distinct digits (a &gt; b). Reverse them to form two 2-digit numbers and subtract. The difference is ALWAYS a multiple of 9!</p>
    </div>

    <div class="grid grid-cols-2 gap-3 bg-slate-900/90 p-4 rounded-xl border border-slate-800">
        <div>
            <label class="block text-xs font-semibold text-slate-300 mb-1">Digit a (Tens):</label>
            <select id="digitASelect" onchange="calcDigitDiff()" class="w-full bg-slate-800 border border-slate-700 text-white rounded px-3 py-1.5 text-xs font-mono">
                <option value="9">9</option>
                <option value="8" selected>8</option>
                <option value="7">7</option>
                <option value="6">6</option>
                <option value="5">5</option>
            </select>
        </div>
        <div>
            <label class="block text-xs font-semibold text-slate-300 mb-1">Digit b (Ones):</label>
            <select id="digitBSelect" onchange="calcDigitDiff()" class="w-full bg-slate-800 border border-slate-700 text-white rounded px-3 py-1.5 text-xs font-mono">
                <option value="3" selected>3</option>
                <option value="2">2</option>
                <option value="1">1</option>
                <option value="0">0</option>
            </select>
        </div>
    </div>

    <div class="bg-slate-900/80 p-4 rounded-xl border border-fuchsia-500/30 space-y-2 text-center font-mono">
        <div class="text-xs text-slate-400">Step-by-Step Subtraction:</div>
        <div class="text-xl font-bold text-white" id="diffEquation">83 &minus; 38 = 45</div>
        <div class="text-xs text-fuchsia-400 font-bold" id="diffMultiple">45 = 9 &times; 5</div>
        <div class="text-[11px] text-slate-300 mt-1" id="diffProof">Notice: 9 &times; (8 &minus; 3) = 9 &times; 5 = 45!</div>
    </div>

    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-xs text-slate-300">
        <strong class="text-amber-400">Algebraic Proof:</strong> Any 2-digit number is 10a + b. Its reverse is 10b + a. Their difference is (10a + b) &minus; (10b + a) = 9a &minus; 9b = <strong>9 &times; (a &minus; b)</strong>. It is always divisible by 9!
    </div>
</div>
'''

SIM_16_HTML = '''
<div class="space-y-4">
    <div class="bg-rose-950/60 p-4 rounded-xl border border-rose-500/30 text-center">
        <h4 class="text-sm font-bold text-rose-300 uppercase tracking-wider mb-1">King's Horses Stable Trick</h4>
        <p class="text-xs text-slate-300">The King inspects his square 3&times;3 stable and demands 5 horses on each of the 4 outer sides. Can 18 horses satisfy this? Yes, using corner-sharing!</p>
    </div>

    <!-- 3x3 Stable Grid -->
    <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 max-w-xs mx-auto">
        <div class="grid grid-cols-3 gap-2 text-center font-mono">
            <!-- Top Row -->
            <div id="cellTL" class="p-3 bg-amber-950/70 border border-amber-600/40 rounded-lg">
                <div class="text-[10px] text-amber-300">Corner</div>
                <div class="text-lg font-bold text-white" id="valTL">2</div>
            </div>
            <div id="cellTM" class="p-3 bg-slate-800 border border-slate-700 rounded-lg">
                <div class="text-[10px] text-slate-400">Middle</div>
                <div class="text-lg font-bold text-white" id="valTM">1</div>
            </div>
            <div id="cellTR" class="p-3 bg-amber-950/70 border border-amber-600/40 rounded-lg">
                <div class="text-[10px] text-amber-300">Corner</div>
                <div class="text-lg font-bold text-white" id="valTR">2</div>
            </div>

            <!-- Middle Row -->
            <div id="cellML" class="p-3 bg-slate-800 border border-slate-700 rounded-lg">
                <div class="text-[10px] text-slate-400">Middle</div>
                <div class="text-lg font-bold text-white" id="valML">1</div>
            </div>
            <div class="p-3 bg-slate-950 border border-slate-800 rounded-lg flex items-center justify-center">
                <span class="text-[11px] text-slate-500 font-sans">Courtyard</span>
            </div>
            <div id="cellMR" class="p-3 bg-slate-800 border border-slate-700 rounded-lg">
                <div class="text-[10px] text-slate-400">Middle</div>
                <div class="text-lg font-bold text-white" id="valMR">1</div>
            </div>

            <!-- Bottom Row -->
            <div id="cellBL" class="p-3 bg-amber-950/70 border border-amber-600/40 rounded-lg">
                <div class="text-[10px] text-amber-300">Corner</div>
                <div class="text-lg font-bold text-white" id="valBL">0</div>
            </div>
            <div id="cellBM" class="p-3 bg-slate-800 border border-slate-700 rounded-lg">
                <div class="text-[10px] text-slate-400">Middle</div>
                <div class="text-lg font-bold text-white" id="valBM">5</div>
            </div>
            <div id="cellBR" class="p-3 bg-amber-950/70 border border-amber-600/40 rounded-lg">
                <div class="text-[10px] text-amber-300">Corner</div>
                <div class="text-lg font-bold text-white" id="valBR">0</div>
            </div>
        </div>
    </div>

    <!-- Side Sums & Total -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs font-mono">
        <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
            <span class="text-slate-400">Top Side:</span>
            <div class="text-emerald-400 font-bold" id="sumTop">5 horses &check;</div>
        </div>
        <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
            <span class="text-slate-400">Bottom Side:</span>
            <div class="text-emerald-400 font-bold" id="sumBottom">5 horses &check;</div>
        </div>
        <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
            <span class="text-slate-400">Left Side:</span>
            <div class="text-emerald-400 font-bold" id="sumLeft">5 horses &check;</div>
        </div>
        <div class="bg-slate-900 p-2 rounded-lg border border-slate-800">
            <span class="text-slate-400">Right Side:</span>
            <div class="text-emerald-400 font-bold" id="sumRight">5 horses &check;</div>
        </div>
    </div>

    <div class="flex flex-wrap justify-center gap-2">
        <button onclick="setStableConfig('all_middle')" class="px-3 py-1.5 bg-slate-800 hover:bg-rose-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Config 1: 20 Horses (0 in Corners)</button>
        <button onclick="setStableConfig('stolen_18')" class="px-3 py-1.5 bg-slate-800 hover:bg-rose-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Config 2: 18 Horses (2 in Corners)</button>
        <button onclick="setStableConfig('stolen_16')" class="px-3 py-1.5 bg-slate-800 hover:bg-rose-600 text-xs font-semibold rounded-lg text-white border border-slate-700 transition">Config 3: 16 Horses (4 in Corners)</button>
    </div>

    <div class="p-3 bg-slate-900 rounded-xl border border-slate-800 text-xs text-slate-300 text-center">
        <span class="text-amber-400 font-bold">Mathematical Formula:</span> Total Horses = 4 &times; 5 &minus; C = <strong>20 &minus; C</strong> (where C = sum of horses in 4 corners). Each corner horse is counted on TWO sides!
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

