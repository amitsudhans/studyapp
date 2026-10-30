import sys

def build_sims():
    SIMULATORS = []

    # Sim 1: Idli-Vada Game Simulator
    sim1 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Idli-Vada Counter</span>
                <span id="idliVadaCallBadge" class="font-mono text-slate-300 bg-slate-900 px-2 py-0.5 rounded border border-slate-700">Call: Start at 1</span>
            </div>
            <div class="flex-1 flex flex-col items-center justify-center p-3 text-center">
                <div class="text-[10px] uppercase font-mono text-slate-400 mb-1">Current Counting Number</div>
                <div id="idliVadaNum" class="text-5xl font-black font-mono text-transparent bg-clip-text bg-gradient-to-r from-amber-300 to-cyan-300 mb-2">1</div>
                <div id="idliVadaCallText" class="text-base font-bold text-slate-300 py-1 px-4 rounded-xl bg-slate-900/80 border border-slate-800 min-h-[36px] flex items-center justify-center">
                    Counting: 1
                </div>
                <div class="grid grid-cols-3 gap-2 w-full max-w-xs mt-3 text-[11px] font-mono">
                    <div class="p-1.5 rounded bg-amber-950/40 border border-amber-500/30 text-amber-300">÷3: Idli 🥟</div>
                    <div class="p-1.5 rounded bg-cyan-950/40 border border-cyan-500/30 text-cyan-300">÷5: Vada 🥞</div>
                    <div class="p-1.5 rounded bg-emerald-950/40 border border-emerald-500/30 text-emerald-300">÷15: Both! ⭐</div>
                </div>
            </div>
            <div class="pt-2 border-t border-slate-800/80 grid grid-cols-4 gap-2 text-xs">
                <button onclick="stepIdliVada(1)" class="px-2 py-1.5 bg-amber-600 hover:bg-amber-500 text-slate-950 rounded-lg font-bold">+1 Step</button>
                <button onclick="stepIdliVada(5)" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded-lg font-bold">+5 Steps</button>
                <button onclick="jumpToNextIdliVada()" class="px-2 py-1.5 bg-cyan-800/70 hover:bg-cyan-700 text-cyan-200 rounded-lg font-bold">Next Both</button>
                <button onclick="resetIdliVada()" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-400 rounded-lg font-bold">Reset</button>
            </div>
        </div>
    """
    SIMULATORS.append(sim1.strip())

    # Sim 2: Overlapping Circles (Venn Diagram)
    sim2 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Venn Multiples Sieve</span>
                <span id="venmLcmBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">LCM(4, 6) = 12</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center overflow-hidden py-1">
                <svg id="vennSvg" class="w-full h-full max-h-[220px]" viewBox="0 0 380 200">
                    <circle cx="140" cy="100" r="85" fill="#0284c7" fill-opacity="0.25" stroke="#38bdf8" stroke-width="2"/>
                    <circle cx="240" cy="100" r="85" fill="#d97706" fill-opacity="0.25" stroke="#fbbf24" stroke-width="2"/>
                    <text id="vennLabelA" x="90" y="35" fill="#38bdf8" font-size="11" font-weight="bold">Multiples of 4</text>
                    <text id="vennLabelB" x="290" y="35" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="end">Multiples of 6</text>
                    <text x="190" y="30" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Common Multiples</text>
                    <g id="vennNumbersGroup"></g>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Presets:</span>
                <div class="flex gap-1.5">
                    <button onclick="setVennPair(3, 5)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-mono font-bold">3 & 5</button>
                    <button onclick="setVennPair(4, 6)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">4 & 6</button>
                    <button onclick="setVennPair(6, 8)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">6 & 8</button>
                    <button onclick="setVennPair(4, 7)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-violet-300 rounded font-mono font-bold">4 & 7</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim2.strip())

    # Sim 3: Jump Jackpot (Factor Jumping Game)
    sim3 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Jump Jackpot</span>
                <span id="jumpFeedbackBadge" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">Target: 18 • Choose Jump Size</span>
            </div>
            <div class="flex-1 flex flex-col justify-center py-2">
                <svg id="jumpNumberLineSvg" class="w-full h-28" viewBox="0 0 380 100">
                    <line x1="20" y1="80" x2="360" y2="80" stroke="#475569" stroke-width="2"/>
                    <g id="jumpTicksGroup"></g>
                    <g id="jumpArcsGroup"></g>
                </svg>
                <div id="jumpDiscoveredFactors" class="mt-2 p-2 rounded-lg bg-slate-900 border border-slate-800 text-xs flex items-center justify-between">
                    <span class="text-slate-400">Target 18 Factors:</span>
                    <span id="jumpFactorsList" class="font-mono text-emerald-300 font-bold">1, 2, 3, 6, 9, 18</span>
                </div>
            </div>
            <div class="pt-2 border-t border-slate-800/80 space-y-1.5 text-xs">
                <div class="flex items-center justify-between">
                    <span class="text-[11px] text-slate-400">Jump Size:</span>
                    <div class="flex gap-1 flex-wrap">
                        <button onclick="executeJump(2)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-mono font-bold">2</button>
                        <button onclick="executeJump(3)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">3</button>
                        <button onclick="executeJump(4)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-mono font-bold">4</button>
                        <button onclick="executeJump(5)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-mono font-bold">5</button>
                        <button onclick="executeJump(6)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">6</button>
                        <button onclick="executeJump(9)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-violet-300 rounded font-mono font-bold">9</button>
                    </div>
                </div>
                <div class="flex items-center justify-between">
                    <span class="text-[11px] text-slate-400">Change Target:</span>
                    <div class="flex gap-1.5">
                        <button onclick="setJumpTarget(12)" class="px-2 py-0.5 bg-slate-900 hover:bg-slate-800 text-slate-300 rounded text-[11px]">12</button>
                        <button onclick="setJumpTarget(18)" class="px-2 py-0.5 bg-slate-900 hover:bg-slate-800 text-slate-300 rounded text-[11px]">18</button>
                        <button onclick="setJumpTarget(24)" class="px-2 py-0.5 bg-slate-900 hover:bg-slate-800 text-slate-300 rounded text-[11px]">24</button>
                    </div>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim3.strip())

    # Sim 4: Perfect Number Divisor Scale
    sim4 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Perfect Number Scale</span>
                <span id="perfectScaleBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">N = 6 • PERFECT</span>
            </div>
            <div class="flex-1 flex flex-col items-center justify-center p-2 text-center">
                <div id="perfectFormulaDisplay" class="text-sm font-mono text-amber-300 font-bold mb-3">
                    Proper Divisors: 1 + 2 + 3 = 6
                </div>
                <div class="w-full max-w-xs bg-slate-900/90 rounded-xl p-3 border border-slate-800 space-y-2">
                    <div class="flex justify-between text-xs">
                        <span class="text-slate-400">Number Tested (N):</span>
                        <span id="perfectNumberVal" class="font-mono font-bold text-cyan-300">6</span>
                    </div>
                    <div class="flex justify-between text-xs">
                        <span class="text-slate-400">Sum of Proper Factors:</span>
                        <span id="perfectSumVal" class="font-mono font-bold text-emerald-400">6</span>
                    </div>
                    <div class="flex justify-between text-xs border-t border-slate-800 pt-1">
                        <span class="text-slate-400">All Factors Sum:</span>
                        <span id="perfectTotalVal" class="font-mono font-bold text-amber-300">12 (2 × N)</span>
                    </div>
                </div>
                <div id="perfectStatusText" class="mt-3 text-xs text-emerald-300 font-medium">
                    ⭐ Perfect Harmony: Sum of proper factors exactly equals the number itself!
                </div>
            </div>
            <div class="pt-2 border-t border-slate-800/80 grid grid-cols-4 gap-1.5 text-xs">
                <button onclick="testPerfectNumber(6)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">N = 6</button>
                <button onclick="testPerfectNumber(28)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">N = 28</button>
                <button onclick="testPerfectNumber(12)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">N = 12</button>
                <button onclick="testPerfectNumber(16)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-mono font-bold">N = 16</button>
            </div>
        </div>
    """
    SIMULATORS.append(sim4.strip())

    # Sim 5: Rectangular Array Fig Packer
    sim5 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Fig Packing Rectangles</span>
                <span id="figPackBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">7 Figs: PRIME</span>
            </div>
            <div class="flex-1 flex flex-col items-center justify-center p-2">
                <div id="figGridContainer" class="flex flex-wrap gap-4 items-center justify-center max-h-[170px] overflow-y-auto w-full"></div>
                <div id="figExplainText" class="mt-2 text-xs text-center text-slate-300">
                    Only 1 arrangement possible (1 × 7). 7 is a Prime number!
                </div>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Test Figs:</span>
                <div class="flex gap-1 flex-wrap">
                    <button onclick="packFigs(1)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-400 rounded font-mono font-bold">1</button>
                    <button onclick="packFigs(2)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">2</button>
                    <button onclick="packFigs(4)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">4</button>
                    <button onclick="packFigs(6)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">6</button>
                    <button onclick="packFigs(7)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">7</button>
                    <button onclick="packFigs(9)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">9</button>
                    <button onclick="packFigs(12)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">12</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim5.strip())

    # Sim 6: Sieve of Eratosthenes Interactive Grid (1 to 100)
    sim6 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-1.5 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Sieve of Eratosthenes</span>
                <span id="sieveStepBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Step 0: Grid 1 to 100</span>
            </div>
            <div class="flex-1 flex items-center justify-center py-1">
                <div id="sieveGrid" class="grid grid-cols-10 gap-1 w-full max-w-[340px] text-[9px] font-mono text-center select-none"></div>
            </div>
            <div class="pt-1.5 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <div class="flex gap-1">
                    <button onclick="advanceSieve()" class="px-2 py-1 bg-amber-600 hover:bg-amber-500 text-slate-950 rounded font-bold">Next Step →</button>
                    <button onclick="revealAllPrimes()" class="px-2 py-1 bg-emerald-800 hover:bg-emerald-700 text-emerald-200 rounded font-bold">Reveal 25 Primes</button>
                </div>
                <button onclick="resetSieve()" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-400 rounded font-bold">Reset</button>
            </div>
        </div>
    """
    SIMULATORS.append(sim6.strip())

    # Sim 7: Twin Prime Detector & Explorer
    sim7 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Twin Prime Explorer</span>
                <span id="twinFeedbackBadge" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">Selected: (11, 13)</span>
            </div>
            <div class="flex-1 flex flex-col justify-center p-2 text-center">
                <div class="flex items-center justify-center gap-3 my-2">
                    <div id="twinP1" class="w-14 h-14 rounded-2xl bg-amber-500/20 border-2 border-amber-500 flex flex-col items-center justify-center">
                        <span class="text-[9px] text-amber-300 font-mono">Prime 1</span>
                        <span class="text-xl font-bold font-mono text-amber-200">11</span>
                    </div>
                    <div class="flex flex-col items-center">
                        <span class="text-xs font-mono text-slate-400">Diff = 2</span>
                        <span id="twinMiddleEven" class="text-xs font-bold font-mono text-cyan-400 bg-slate-900 px-2 py-0.5 rounded border border-slate-700 mt-1">Mid: 12 (÷6)</span>
                    </div>
                    <div id="twinP2" class="w-14 h-14 rounded-2xl bg-amber-500/20 border-2 border-amber-500 flex flex-col items-center justify-center">
                        <span class="text-[9px] text-amber-300 font-mono">Prime 2</span>
                        <span class="text-xl font-bold font-mono text-amber-200">13</span>
                    </div>
                </div>
                <div id="twinExplainBox" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 mt-1">
                    Twin primes have difference 2. Sandwiched number 12 is a multiple of 6!
                </div>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Twin Pairs:</span>
                <div class="flex gap-1 flex-wrap">
                    <button onclick="selectTwinPair(3, 5)" class="px-1.5 py-0.5 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-mono text-[11px]">(3, 5)</button>
                    <button onclick="selectTwinPair(5, 7)" class="px-1.5 py-0.5 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-mono text-[11px]">(5, 7)</button>
                    <button onclick="selectTwinPair(11, 13)" class="px-1.5 py-0.5 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono text-[11px]">(11, 13)</button>
                    <button onclick="selectTwinPair(17, 19)" class="px-1.5 py-0.5 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono text-[11px]">(17, 19)</button>
                    <button onclick="selectTwinPair(29, 31)" class="px-1.5 py-0.5 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono text-[11px]">(29, 31)</button>
                    <button onclick="selectTwinPair(41, 43)" class="px-1.5 py-0.5 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono text-[11px]">(41, 43)</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim7.strip())

    # Sim 8: Co-prime Lock & Key Vault
    sim8 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Treasure Vault Lock</span>
                <span id="vaultStatusBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">HCF(4, 9) = 1 • UNLOCKED</span>
            </div>
            <div class="flex-1 flex flex-col items-center justify-center p-2 text-center">
                <div class="grid grid-cols-2 gap-3 w-full max-w-xs mb-2 text-xs">
                    <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                        <span id="vaultNumA" class="font-bold text-amber-300 block mb-0.5">Number A: 4</span>
                        <span id="vaultFactorsA" class="font-mono text-[11px] text-slate-300">{1, 2, 4}</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                        <span id="vaultNumB" class="font-bold text-cyan-300 block mb-0.5">Number B: 9</span>
                        <span id="vaultFactorsB" class="font-mono text-[11px] text-slate-300">{1, 3, 9}</span>
                    </div>
                </div>
                <div id="vaultGraphic" class="text-4xl my-1">🔓</div>
                <div id="vaultMessage" class="text-xs text-emerald-300 font-medium">
                    Common factor is ONLY {1}. Both numbers are CO-PRIME!
                </div>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Test Pairs:</span>
                <div class="flex gap-1.5">
                    <button onclick="testVaultPair(4, 9)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">(4, 9)</button>
                    <button onclick="testVaultPair(8, 15)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">(8, 15)</button>
                    <button onclick="testVaultPair(6, 9)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-mono font-bold">(6, 9)</button>
                    <button onclick="testVaultPair(14, 21)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-mono font-bold">(14, 21)</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim8.strip())

    # Sim 9: Circular Thread-Art Peg Star Simulator
    sim9 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Thread-Art Peg Stars</span>
                <span id="threadStarBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">N = 8, Step = 3 (Star!)</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="threadStarSvg" class="w-full h-full max-h-[200px]" viewBox="0 0 220 220">
                    <circle cx="110" cy="110" r="85" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <g id="threadLinesGroup"></g>
                    <g id="threadPegsGroup"></g>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Step k (N = 8):</span>
                <div class="flex gap-1.5">
                    <button onclick="setThreadStep(1)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono font-bold">k = 1</button>
                    <button onclick="setThreadStep(2)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-mono font-bold">k = 2 (Square)</button>
                    <button onclick="setThreadStep(3)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">k = 3 (Star!)</button>
                    <button onclick="setThreadStep(4)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-mono font-bold">k = 4 (Lines)</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim9.strip())

    # Sim 10: Co-prime LCM & Product Calculator
    sim10 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Co-prime LCM Theorem</span>
                <span id="lcmTheoremBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">LCM(5, 7) = 5 × 7 = 35</span>
            </div>
            <div class="flex-1 flex flex-col items-center justify-center p-2 text-center">
                <div class="grid grid-cols-3 gap-2 w-full max-w-xs mb-3 text-xs">
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">HCF</span>
                        <span id="theoHcfVal" class="font-mono font-bold text-amber-300 text-sm">1</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">LCM</span>
                        <span id="theoLcmVal" class="font-mono font-bold text-cyan-300 text-sm">35</span>
                    </div>
                    <div class="p-2 rounded-lg bg-slate-900 border border-slate-800">
                        <span class="text-slate-400 block text-[10px]">Product a × b</span>
                        <span id="theoProdVal" class="font-mono font-bold text-emerald-300 text-sm">35</span>
                    </div>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900/90 border border-slate-800 text-xs font-mono space-y-1">
                    <div class="text-amber-400">Formula: HCF × LCM = a × b</div>
                    <div id="theoEquation" class="text-slate-200">1 × 35 = 5 × 7</div>
                </div>
                <div id="theoCoPrimeTag" class="mt-2 text-xs text-emerald-400 font-bold">
                    ✓ Co-prime: LCM is exactly the product!
                </div>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Compare:</span>
                <div class="flex gap-1.5">
                    <button onclick="setTheoPair(5, 7)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">(5, 7)</button>
                    <button onclick="setTheoPair(4, 9)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">(4, 9)</button>
                    <button onclick="setTheoPair(6, 8)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-mono font-bold">(6, 8)</button>
                    <button onclick="setTheoPair(8, 12)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-mono font-bold">(8, 12)</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim10.strip())

    # Sim 11: Interactive Factor Tree Builder
    sim11 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Prime Factor Tree</span>
                <span id="factorTreeBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">56 = 2³ × 7</span>
            </div>
            <div class="flex-1 relative flex items-center justify-center py-1">
                <svg id="factorTreeSvg" class="w-full h-full max-h-[210px]" viewBox="0 0 320 200">
                    <g id="treeLinesGroup"></g>
                    <g id="treeNodesGroup"></g>
                </svg>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Choose Composite:</span>
                <div class="flex gap-1.5">
                    <button onclick="buildFactorTree(56)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-mono font-bold">56</button>
                    <button onclick="buildFactorTree(72)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">72</button>
                    <button onclick="buildFactorTree(84)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">84</button>
                    <button onclick="buildFactorTree(60)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-violet-300 rounded font-mono font-bold">60</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim11.strip())

    # Sim 12: Fundamental Theorem DNA Sorter
    sim12 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Prime Factor DNA</span>
                <span id="dnaNumBadge" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">Target: 36</span>
            </div>
            <div class="flex-1 flex flex-col items-center justify-center p-2 text-center">
                <div class="text-xs text-slate-400 mb-2">Prime Factor Beads:</div>
                <div id="dnaBeadsRow" class="flex gap-2 items-center justify-center my-2"></div>
                <div id="dnaProductResult" class="text-sm font-mono text-emerald-300 font-bold mt-2">
                    2 × 2 × 3 × 3 = 36
                </div>
                <p class="text-[11px] text-slate-400 mt-2">
                    Shuffle the factors in any order — the product remains uniquely 36!
                </p>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <button onclick="shuffleDnaBeads()" class="px-3 py-1.5 bg-amber-600 hover:bg-amber-500 text-slate-950 rounded-lg font-bold">🔀 Shuffle Order</button>
                <div class="flex gap-1.5">
                    <button onclick="setDnaTarget(36)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono">36</button>
                    <button onclick="setDnaTarget(90)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono">90</button>
                    <button onclick="setDnaTarget(60)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono">60</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim12.strip())

    # Sim 13: Factor Pantry Divisibility Tester
    sim13 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Prime Pantry Test</span>
                <span id="pantryResultBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">84 is divisible by 14</span>
            </div>
            <div class="flex-1 flex flex-col justify-center p-2 text-xs space-y-2">
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-amber-400 font-bold block mb-1">Target Number A = 84:</span>
                    <div id="pantryFactorsA" class="font-mono text-slate-200 flex gap-1.5 items-center">
                        <span class="px-2 py-0.5 rounded bg-slate-800 text-amber-300">2</span>
                        <span class="px-2 py-0.5 rounded bg-slate-800 text-amber-300">2</span>
                        <span class="px-2 py-0.5 rounded bg-slate-800 text-amber-300">3</span>
                        <span class="px-2 py-0.5 rounded bg-slate-800 text-amber-300">7</span>
                    </div>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                    <span class="text-cyan-400 font-bold block mb-1">Testing Divisor B = <span id="pantryDivisorLabel">14</span>:</span>
                    <div id="pantryFactorsB" class="font-mono text-slate-200 flex gap-1.5 items-center"></div>
                </div>
                <div id="pantryStatusExplanation" class="text-emerald-300 text-center font-medium">
                    ✓ Both '2' and '7' are inside 84! Divisible without remainder.
                </div>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Test Divisor B:</span>
                <div class="flex gap-1.5">
                    <button onclick="testPantryDivisor(14)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">14 (2×7)</button>
                    <button onclick="testPantryDivisor(12)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">12 (2²×3)</button>
                    <button onclick="testPantryDivisor(8)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-mono font-bold">8 (2³)</button>
                    <button onclick="testPantryDivisor(15)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-mono font-bold">15 (3×5)</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim13.strip())

    # Sim 14: Last Digit Divisibility Scanner (2, 5, 10)
    sim14 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Unit Digit Scanner</span>
                <span id="scannerInputBadge" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">Number: 3,480</span>
            </div>
            <div class="flex-1 flex flex-col items-center justify-center p-2 text-center">
                <div class="flex items-center justify-center font-mono text-3xl font-black mb-3">
                    <span id="scanPrefix" class="text-slate-400">348</span>
                    <span id="scanLastDigit" class="text-amber-400 underline decoration-amber-400 decoration-4 ml-0.5 bg-amber-500/20 px-2 py-0.5 rounded">0</span>
                </div>
                <div class="grid grid-cols-3 gap-2 w-full max-w-xs text-xs">
                    <div id="rule2Box" class="p-2 rounded-xl bg-slate-900 border border-slate-800 flex flex-col items-center">
                        <span class="text-slate-400 text-[10px]">÷ 2 (Even)</span>
                        <span id="rule2Result" class="font-bold text-emerald-400 text-sm mt-0.5">✓ Yes</span>
                    </div>
                    <div id="rule5Box" class="p-2 rounded-xl bg-slate-900 border border-slate-800 flex flex-col items-center">
                        <span class="text-slate-400 text-[10px]">÷ 5 (0 or 5)</span>
                        <span id="rule5Result" class="font-bold text-emerald-400 text-sm mt-0.5">✓ Yes</span>
                    </div>
                    <div id="rule10Box" class="p-2 rounded-xl bg-slate-900 border border-slate-800 flex flex-col items-center">
                        <span class="text-slate-400 text-[10px]">÷ 10 (Ends 0)</span>
                        <span id="rule10Result" class="font-bold text-emerald-400 text-sm mt-0.5">✓ Yes</span>
                    </div>
                </div>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Test Numbers:</span>
                <div class="flex gap-1.5">
                    <button onclick="scanNumber(3480)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono font-bold">3480</button>
                    <button onclick="scanNumber(5795)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono font-bold">5795</button>
                    <button onclick="scanNumber(8426)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono font-bold">8426</button>
                    <button onclick="scanNumber(9113)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono font-bold">9113</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim14.strip())

    # Sim 15: Last 2 & 3 Digits Scanner (4 & 8)
    sim15 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Powers of 2: Rules 4 & 8</span>
                <span id="scan48Badge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Testing: 7,536</span>
            </div>
            <div class="flex-1 flex flex-col items-center justify-center p-2 text-center space-y-2">
                <div class="font-mono text-2xl font-black">
                    <span id="scan48Thousands" class="text-slate-500">7,5</span>
                    <span id="scan48Last2" class="text-amber-400 bg-amber-500/20 px-1 rounded">36</span>
                </div>
                <div class="grid grid-cols-2 gap-2 w-full max-w-xs text-xs">
                    <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                        <span class="text-amber-300 font-bold block mb-1">Rule for 4:</span>
                        <span id="scan4Text" class="text-[11px] text-slate-300 block">Last 2 digits: 36</span>
                        <span id="scan4Result" class="font-bold text-emerald-400 mt-1 block">36 ÷ 4 = 9 (Divisible! ✓)</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                        <span class="text-cyan-300 font-bold block mb-1">Rule for 8:</span>
                        <span id="scan8Text" class="text-[11px] text-slate-300 block">Last 3 digits: 536</span>
                        <span id="scan8Result" class="font-bold text-emerald-400 mt-1 block">536 ÷ 8 = 67 (Divisible! ✓)</span>
                    </div>
                </div>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <span class="text-[11px] text-slate-400">Test Candidates:</span>
                <div class="flex gap-1.5">
                    <button onclick="scan48Number(7536)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono font-bold">7536</button>
                    <button onclick="scan48Number(98128)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono font-bold">98128</button>
                    <button onclick="scan48Number(4218)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono font-bold">4218</button>
                    <button onclick="scan48Number(12048)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-mono font-bold">12048</button>
                </div>
            </div>
        </div>
    """
    SIMULATORS.append(sim15.strip())

    # Sim 16: Prime Cross-Product Grid Puzzle
    sim16 = """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Prime Cross-Product Puzzle</span>
                <span id="puzzleStatusBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Fill 4 Cells with Primes</span>
            </div>
            <div class="flex-1 flex flex-col items-center justify-center p-2">
                <div class="grid grid-cols-3 gap-1.5 items-center justify-center text-center font-mono">
                    <div></div>
                    <div class="text-[10px] text-cyan-400 font-bold">Col 1<br>(Prod: 6)</div>
                    <div class="text-[10px] text-cyan-400 font-bold">Col 2<br>(Prod: 35)</div>

                    <div class="text-[10px] text-amber-400 font-bold text-right pr-1">Row 1<br>(15)</div>
                    <input id="puz_r1c1" type="text" maxlength="2" class="w-12 h-12 rounded-xl bg-slate-900 border border-slate-700 text-center font-bold text-lg text-emerald-300 focus:border-amber-400 outline-none" value="3" readonly>
                    <input id="puz_r1c2" type="text" maxlength="2" class="w-12 h-12 rounded-xl bg-slate-900 border border-slate-700 text-center font-bold text-lg text-emerald-300 focus:border-amber-400 outline-none" placeholder="?" oninput="checkPuzzle()">

                    <div class="text-[10px] text-amber-400 font-bold text-right pr-1">Row 2<br>(14)</div>
                    <input id="puz_r2c1" type="text" maxlength="2" class="w-12 h-12 rounded-xl bg-slate-900 border border-slate-700 text-center font-bold text-lg text-emerald-300 focus:border-amber-400 outline-none" placeholder="?" oninput="checkPuzzle()">
                    <input id="puz_r2c2" type="text" maxlength="2" class="w-12 h-12 rounded-xl bg-slate-900 border border-slate-700 text-center font-bold text-lg text-emerald-300 focus:border-amber-400 outline-none" placeholder="?" oninput="checkPuzzle()">
                </div>
                <div id="puzzleFeedbackText" class="mt-3 text-xs text-slate-300 text-center min-h-[20px]">
                    Hint: R1C1 must divide Row 1 (15) and Col 1 (6) → HCF(15, 6) = 3!
                </div>
            </div>
            <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-xs">
                <button onclick="solvePrimePuzzle()" class="px-2 py-1 bg-amber-600 hover:bg-amber-500 text-slate-950 rounded font-bold">Reveal Solution</button>
                <button onclick="resetPrimePuzzle()" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded font-bold">Clear Puzzle</button>
            </div>
        </div>
    """
    SIMULATORS.append(sim16.strip())

    code = f'''"""NCERT Class 6 Mathematics Chapter 5: Prime Time Simulators Module."""

SIMULATORS = {SIMULATORS}
'''

    # Strict check for raw LaTeX
    forbidden = ["\\text", "\\frac", "\\circ", "\\angle", "\\overleftrightarrow", "\\overline", "\\vec", "\\approx", "\\dots", "\\sqrt"]
    for word in forbidden:
        if word in code:
            raise ValueError(f"CRITICAL ERROR: Found raw LaTeX '{word}' in simulators module!")

    # Check for surrogates
    clean_chars = [ch for ch in code if not (0xD800 <= ord(ch) <= 0xDFFF)]
    clean_code = ''.join(clean_chars)

    with open(".agents/class6_math_prime_time_sims.py", "w", encoding="utf-8") as f:
        f.write(clean_code)

    print("Successfully generated .agents/class6_math_prime_time_sims.py with 16 bespoke simulators.")
    print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in simulators module!")

if __name__ == "__main__":
    build_sims()

