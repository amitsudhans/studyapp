import re

sims = [
    # Sim 1: Number Evolution
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🌱</span>
                <span>The Number Ray Expands into the Mirror Realm</span>
            </h3>
            <span id="sim1-badge" class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">Counting Numbers</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800/80">
            <svg id="sim1-svg" viewBox="0 0 500 160" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim1Stage('natural')" id="sim1-btn-natural" class="px-3 py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">1. Counting (1, 2, 3...)</button>
            <button onclick="setSim1Stage('whole')" id="sim1-btn-whole" class="px-3 py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">2. Zero Arrives (0)</button>
            <button onclick="setSim1Stage('integers')" id="sim1-btn-integers" class="px-3 py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">3. Complete Line (Integers)</button>
        </div>
        <p id="sim1-desc" class="text-xs text-slate-300 bg-slate-950/50 p-3 rounded-xl border border-slate-800/60 leading-relaxed"></p>
    </div>
    """,

    # Sim 2: Bela's Fun Elevator
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🛗</span>
                <span>Bela's Ice Cream Elevator Cabin</span>
            </h3>
            <span id="sim2-floor-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Floor 0 (Ground)</span>
        </div>
        <div class="grid grid-cols-12 gap-4">
            <!-- Shaft Display -->
            <div class="col-span-8 bg-slate-950/80 rounded-xl p-3 border border-slate-800 flex items-center justify-center">
                <svg id="sim2-svg" viewBox="0 0 280 260" class="w-full h-56 mx-auto"></svg>
            </div>
            <!-- Lift Buttons -->
            <div class="col-span-4 flex flex-col justify-between py-1 space-y-1.5">
                <span class="text-[10px] font-bold text-slate-400 uppercase text-center">Press Floor Button</span>
                <button onclick="sim2GoTo(3)" class="w-full py-1.5 rounded-lg text-xs font-bold bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 border border-emerald-500/30">+3 Roof Terrace</button>
                <button onclick="sim2GoTo(2)" class="w-full py-1.5 rounded-lg text-xs font-bold bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 border border-emerald-500/30">+2 Sundae Parlor</button>
                <button onclick="sim2GoTo(1)" class="w-full py-1.5 rounded-lg text-xs font-bold bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 border border-emerald-500/30">+1 Cone Bakery</button>
                <button onclick="sim2GoTo(0)" class="w-full py-1.5 rounded-lg text-xs font-bold bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/30">0 Ground Lobby</button>
                <button onclick="sim2GoTo(-1)" class="w-full py-1.5 rounded-lg text-xs font-bold bg-rose-500/20 hover:bg-rose-500/30 text-rose-300 border border-rose-500/30">−1 Cold Storage</button>
                <button onclick="sim2GoTo(-2)" class="w-full py-1.5 rounded-lg text-xs font-bold bg-rose-500/20 hover:bg-rose-500/30 text-rose-300 border border-rose-500/30">−2 Chocolate Vault</button>
                <button onclick="sim2GoTo(-3)" class="w-full py-1.5 rounded-lg text-xs font-bold bg-rose-500/20 hover:bg-rose-500/30 text-rose-300 border border-rose-500/30">−3 Deep Freeze</button>
            </div>
        </div>
        <p id="sim2-status" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 3: Signs & Direction
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🧭</span>
                <span>Positive (+) vs Negative (−) Motion Vector</span>
            </h3>
            <span id="sim3-badge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Upward Motion (+)</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim3-svg" viewBox="0 0 400 200" class="w-full h-48 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <button onclick="setSim3Dir(1)" id="sim3-btn-up" class="py-2.5 rounded-xl text-xs font-bold bg-emerald-500 text-slate-950 transition flex items-center justify-center space-x-1.5">
                <span>⬆️</span><span>Move Up (+ Positive)</span>
            </button>
            <button onclick="setSim3Dir(-1)" id="sim3-btn-down" class="py-2.5 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition flex items-center justify-center space-x-1.5">
                <span>⬇️</span><span>Move Down (− Negative)</span>
            </button>
        </div>
        <div class="flex items-center space-x-3 bg-slate-950/50 p-3 rounded-xl border border-slate-800">
            <span class="text-xs text-slate-400 font-medium whitespace-nowrap">Distance:</span>
            <input type="range" id="sim3-dist" min="1" max="5" value="3" oninput="updateSim3()" class="w-full accent-cyan-400">
            <span id="sim3-dist-val" class="text-xs font-bold text-cyan-300 w-16 text-right">3 Floors</span>
        </div>
    </div>
    """,

    # Sim 4: Tracking Movement
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>📊</span>
                <span>Starting Floor + Movement = Target Floor</span>
            </h3>
            <span id="sim4-eq-badge" class="font-mono text-xs font-bold text-amber-300 bg-amber-500/10 px-2.5 py-1 rounded-lg border border-amber-500/20">(+1) + (+2) = +3</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim4-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div class="bg-slate-950/50 p-3 rounded-xl border border-slate-800 space-y-1.5">
                <div class="flex justify-between text-xs">
                    <span class="text-slate-400">Starting Floor:</span>
                    <span id="sim4-start-val" class="font-bold text-cyan-300">+1</span>
                </div>
                <input type="range" id="sim4-start" min="-3" max="3" value="1" oninput="updateSim4()" class="w-full accent-cyan-400">
            </div>
            <div class="bg-slate-950/50 p-3 rounded-xl border border-slate-800 space-y-1.5">
                <div class="flex justify-between text-xs">
                    <span class="text-slate-400">Movement Jump:</span>
                    <span id="sim4-move-val" class="font-bold text-amber-300">+2 (Up)</span>
                </div>
                <input type="range" id="sim4-move" min="-4" max="4" value="2" oninput="updateSim4()" class="w-full accent-amber-400">
            </div>
        </div>
        <p id="sim4-info" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 5: Additive Inverses
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>⚖️</span>
                <span>The Additive Inverse: Returning to Zero</span>
            </h3>
            <span class="font-mono text-xs font-bold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-lg border border-emerald-500/20">(+a) + (−a) = 0</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim5-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="flex items-center justify-between gap-3">
            <div class="flex items-center space-x-2 w-2/3">
                <span class="text-xs text-slate-400 whitespace-nowrap">Choose Value a:</span>
                <input type="range" id="sim5-val" min="1" max="6" value="4" oninput="updateSim5()" class="w-full accent-indigo-400">
                <span id="sim5-val-display" class="font-bold text-indigo-300 text-xs w-8 text-right">4</span>
            </div>
            <button onclick="triggerSim5Inverse()" id="sim5-inverse-btn" class="w-1/3 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-amber-500 to-orange-500 text-slate-950 hover:opacity-90 transition">
                Apply Inverse (−a)
            </button>
        </div>
        <p id="sim5-status" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 6: Floor Heights Comparison
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>📏</span>
                <span>Comparing Floor Depths: Higher > Lower</span>
            </h3>
            <span id="sim6-comp-badge" class="font-mono text-xs font-bold text-cyan-400 bg-cyan-500/10 px-2.5 py-1 rounded-lg border border-cyan-500/20">−2 > −5</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim6-svg" viewBox="0 0 450 200" class="w-full h-48 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <div class="bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 space-y-1">
                <div class="flex justify-between text-xs">
                    <span class="text-emerald-400 font-semibold">Elevator A (Green):</span>
                    <span id="sim6-val-a" class="font-bold text-emerald-300 font-mono">+1</span>
                </div>
                <input type="range" id="sim6-slider-a" min="-6" max="6" value="1" oninput="updateSim6()" class="w-full accent-emerald-400">
            </div>
            <div class="bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 space-y-1">
                <div class="flex justify-between text-xs">
                    <span class="text-rose-400 font-semibold">Elevator B (Red):</span>
                    <span id="sim6-val-b" class="font-bold text-rose-300 font-mono">−4</span>
                </div>
                <input type="range" id="sim6-slider-b" min="-6" max="6" value="-4" oninput="updateSim6()" class="w-full accent-rose-400">
            </div>
        </div>
        <p id="sim6-conclusion" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 7: Finding the Shift
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🔄</span>
                <span>Target − Start = Movement Needed</span>
            </h3>
            <span id="sim7-badge" class="font-mono text-xs font-bold text-amber-300 bg-amber-500/10 px-2.5 py-1 rounded-lg border border-amber-500/20">(+3) − (−2) = +5</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim7-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-2 gap-3">
            <div class="bg-slate-950/50 p-2.5 rounded-xl border border-slate-800">
                <div class="flex justify-between text-xs mb-1">
                    <span class="text-slate-400">Starting Floor:</span>
                    <span id="sim7-start-txt" class="font-bold text-cyan-300">−2</span>
                </div>
                <input type="range" id="sim7-start" min="-4" max="4" value="-2" oninput="updateSim7()" class="w-full accent-cyan-400">
            </div>
            <div class="bg-slate-950/50 p-2.5 rounded-xl border border-slate-800">
                <div class="flex justify-between text-xs mb-1">
                    <span class="text-slate-400">Target Floor:</span>
                    <span id="sim7-target-txt" class="font-bold text-amber-300">+3</span>
                </div>
                <input type="range" id="sim7-target" min="-4" max="4" value="3" oninput="updateSim7()" class="w-full accent-amber-400">
            </div>
        </div>
        <p id="sim7-explanation" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 8: Mine Shafts & Scales
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>⛏️</span>
                <span>Deep Mine Shaft & Mountain Lookout</span>
            </h3>
            <span id="sim8-badge" class="text-xs font-bold text-cyan-400 bg-cyan-500/10 px-2.5 py-1 rounded-lg border border-cyan-500/20">Scale: −500 m to +500 m</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim8-svg" viewBox="0 0 450 200" class="w-full h-48 mx-auto"></svg>
        </div>
        <div class="flex items-center space-x-3 bg-slate-950/50 p-3 rounded-xl border border-slate-800">
            <span class="text-xs text-slate-400 whitespace-nowrap">Miner Elevation:</span>
            <input type="range" id="sim8-slider" min="-450" max="400" step="25" value="-200" oninput="updateSim8()" class="w-full accent-amber-400">
            <span id="sim8-elevation-val" class="font-mono text-xs font-bold text-amber-300 w-24 text-right">−200 m</span>
        </div>
        <p id="sim8-text" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 9: Double Negative Visualizer
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>✨</span>
                <span>The Double Negative Rule: a − (−b) = a + b</span>
            </h3>
            <span class="font-mono text-xs font-bold text-emerald-300 bg-emerald-500/10 px-2.5 py-1 rounded-lg border border-emerald-500/20">Subtracting Debt = Adding Wealth</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim9-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="flex items-center justify-between gap-3">
            <button onclick="setSim9Scenario('debt')" id="sim9-btn-debt" class="w-1/2 py-2 rounded-xl text-xs font-bold bg-cyan-500 text-slate-950 transition">Bank Debt Removal</button>
            <button onclick="setSim9Scenario('walker')" id="sim9-btn-walker" class="w-1/2 py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Walking Backwards in Reverse</button>
        </div>
        <p id="sim9-msg" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium leading-relaxed"></p>
    </div>
    """,

    # Sim 10: Horizontal Shift
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🔄</span>
                <span>90° Elevator Rotation into the Number Line</span>
            </h3>
            <span id="sim10-badge" class="text-xs font-bold text-indigo-300 bg-indigo-500/10 px-2.5 py-1 rounded-lg border border-indigo-500/20">Vertical Shaft Mode</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim10-svg" viewBox="0 0 450 200" class="w-full h-48 mx-auto"></svg>
        </div>
        <div class="flex items-center justify-center">
            <button onclick="toggleSim10Rotation()" id="sim10-rotate-btn" class="px-5 py-2.5 rounded-xl text-xs font-bold bg-gradient-to-r from-cyan-500 to-indigo-600 text-white shadow-lg shadow-cyan-500/20 hover:opacity-90 transition flex items-center space-x-2">
                <span>↻ Rotate 90° (Vertical ⇄ Horizontal)</span>
            </button>
        </div>
        <p id="sim10-status" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 11: The Unmarked Line
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>〰️</span>
                <span>The Unmarked Line: Mental Arithmetic via Zero Bridge</span>
            </h3>
            <span id="sim11-badge" class="font-mono text-xs font-bold text-amber-300 bg-amber-500/10 px-2.5 py-1 rounded-lg border border-amber-500/20">(−35) + (+50) = +15</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim11-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim11Problem(1)" id="sim11-p1" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">(−35) + (+50)</button>
            <button onclick="setSim11Problem(2)" id="sim11-p2" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">(+18) + (−30)</button>
            <button onclick="setSim11Problem(3)" id="sim11-p3" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">(−120) − (−150)</button>
        </div>
        <p id="sim11-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 12: The Token Model
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🟢🔴</span>
                <span>The Token Model: Green (+1) & Red (−1) Counters</span>
            </h3>
            <span id="sim12-sum-badge" class="font-mono text-xs font-bold text-cyan-300 bg-cyan-500/10 px-2.5 py-1 rounded-lg border border-cyan-500/20">Net Value: +2</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 min-h-[160px] flex items-center justify-center">
            <div id="sim12-token-tray" class="flex flex-wrap gap-2 items-center justify-center max-w-sm"></div>
        </div>
        <div class="grid grid-cols-4 gap-2">
            <button onclick="addSim12Token('pos')" class="py-2 rounded-xl text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 hover:bg-emerald-500/30">+1 Green</button>
            <button onclick="addSim12Token('neg')" class="py-2 rounded-xl text-xs font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 hover:bg-rose-500/30">−1 Red</button>
            <button onclick="pairSim12ZeroPairs()" class="py-2 rounded-xl text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 hover:bg-amber-500/30">Pair Zero Pairs</button>
            <button onclick="clearSim12Tokens()" class="py-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Clear Tray</button>
        </div>
        <p id="sim12-status" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 13: Token Subtraction
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🧪</span>
                <span>Zero-Pair Injection Subtraction Lab</span>
            </h3>
            <span id="sim13-eq-badge" class="font-mono text-xs font-bold text-amber-300 bg-amber-500/10 px-2.5 py-1 rounded-lg border border-amber-500/20">(+2) − (−3) = +5</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 min-h-[160px] flex items-center justify-center">
            <div id="sim13-token-display" class="space-y-3 w-full"></div>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim13Step(1)" id="sim13-step1" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">Step 1: Start with +2</button>
            <button onclick="setSim13Step(2)" id="sim13-step2" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Step 2: Add 3 Zero Pairs</button>
            <button onclick="setSim13Step(3)" id="sim13-step3" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Step 3: Remove 3 Red</button>
        </div>
        <p id="sim13-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 14: Real-World Balances
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🌍</span>
                <span>Real-World Tri-Gauge: Bank, Sea & Temperature</span>
            </h3>
            <span id="sim14-gauge-title" class="text-xs font-bold text-cyan-400 bg-cyan-500/10 px-2.5 py-1 rounded-lg border border-cyan-500/20">Bank Balance</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800">
            <svg id="sim14-svg" viewBox="0 0 450 180" class="w-full h-44 mx-auto"></svg>
        </div>
        <div class="grid grid-cols-3 gap-2">
            <button onclick="setSim14Mode('bank')" id="sim14-btn-bank" class="py-2 rounded-xl text-xs font-semibold bg-cyan-500 text-slate-950 transition">🏦 Bank Ledger</button>
            <button onclick="setSim14Mode('sea')" id="sim14-btn-sea" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌊 Sea Altitude</button>
            <button onclick="setSim14Mode('temp')" id="sim14-btn-temp" class="py-2 rounded-xl text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">🌡️ Thermometer</button>
        </div>
        <p id="sim14-desc" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 15: Magic Border Grids
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>🧩</span>
                <span>Hollow 3×3 Integer Grid Symmetry</span>
            </h3>
            <span id="sim15-badge" class="font-mono text-xs font-bold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-lg border border-emerald-500/20">Target Side Sum: 0</span>
        </div>
        <div class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 flex items-center justify-center">
            <div id="sim15-grid-board" class="grid grid-cols-3 gap-2 w-64 h-64 p-2 bg-slate-900 rounded-xl border border-slate-700"></div>
        </div>
        <div class="flex justify-between items-center text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800">
            <span>Top: <strong id="sim15-top-sum" class="text-cyan-300">0</strong></span>
            <span>Bottom: <strong id="sim15-bot-sum" class="text-cyan-300">0</strong></span>
            <span>Left: <strong id="sim15-left-sum" class="text-cyan-300">0</strong></span>
            <span>Right: <strong id="sim15-right-sum" class="text-cyan-300">0</strong></span>
        </div>
        <p id="sim15-status" class="text-xs text-slate-300 bg-slate-950/50 p-2.5 rounded-xl border border-slate-800 text-center font-medium"></p>
    </div>
    """,

    # Sim 16: Brahmagupta's Laws Table
    """
    <div class="p-5 rounded-2xl bg-slate-900/90 border border-slate-800 shadow-xl space-y-4">
        <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center space-x-2">
                <span>📜</span>
                <span>Brahmagupta's Brāhmasphuṭasiddhānta (628 CE) Laws Matrix</span>
            </h3>
            <span class="text-xs font-bold text-amber-400 bg-amber-500/10 px-2.5 py-1 rounded-lg border border-amber-500/20">Universal Algebra</span>
        </div>
        <div class="grid grid-cols-2 gap-2 text-xs">
            <button onclick="showSim16Rule('ff')" id="sim16-btn-ff" class="p-3 rounded-xl border border-slate-700 bg-cyan-500 text-slate-950 font-bold text-left transition">Fortune + Fortune = Fortune</button>
            <button onclick="showSim16Rule('dd')" id="sim16-btn-dd" class="p-3 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 font-semibold text-left transition">Debt + Debt = Debt</button>
            <button onclick="showSim16Rule('fd')" id="sim16-btn-fd" class="p-3 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 font-semibold text-left transition">Fortune + Debt = Difference</button>
            <button onclick="showSim16Rule('sub')" id="sim16-btn-sub" class="p-3 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 font-semibold text-left transition">Zero − Debt = Fortune</button>
        </div>
        <div id="sim16-detail-box" class="bg-slate-950/80 rounded-xl p-4 border border-slate-800 space-y-2"></div>
    </div>
    """
]

# Verify zero raw LaTeX and zero surrogates in simulators
raw_latex_pattern = re.compile(r'\\[a-zA-Z]+')

for idx, s in enumerate(sims):
    matches = raw_latex_pattern.findall(s)
    if matches:
        raise ValueError(f"Found raw LaTeX in Sim {idx+1}: {set(matches)}")
    surrogates = [c for c in s if 0xD800 <= ord(c) <= 0xDFFF]
    if surrogates:
        raise ValueError(f"Found surrogates in Sim {idx+1}")

print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in all 16 Simulators!")

with open(".agents/class6_math_integers_sims.py", "w", encoding="utf-8") as f:
    f.write('"""\nNCERT Class 6 Mathematics Chapter 10: Integers Simulators Module\n"""\n\n')
    f.write('SIMULATORS = ' + repr(sims) + '\n')

print("Successfully wrote .agents/class6_math_integers_sims.py")
