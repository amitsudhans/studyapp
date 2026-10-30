import sys

def generate_simulators():
    simulators = [
        # Sim 1: Line of Friends Puzzle (Reconstructing Heights from Clues)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Line of Friends Simulator</span>
                <span id="friendsStatusBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">5 Friends in Order</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center p-2">
                <svg id="friendsSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <line x1="20" y1="200" x2="380" y2="200" stroke="#475569" stroke-width="2"/>
                    <!-- 5 Friends rendered as vertical bars with reported clues -->
                    <g id="friendsGroup"></g>
                </svg>
            </div>
            <div class="grid grid-cols-3 gap-2 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setFriendsPattern('pyramid')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold transition">Mountain Height</button>
                <button onclick="setFriendsPattern('valley')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold transition">Valley Height</button>
                <button onclick="setFriendsPattern('ascending')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold transition">Ascending Line</button>
            </div>
        </div>
        """,

        # Sim 2: Supercells in Grids (Interactive 3x3 Grid Supercell Hunter)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">3 × 3 Supercell Grid Lab</span>
                <span id="supercellCountBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Supercells Found: 5</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center p-3">
                <div id="gridSupercellContainer" class="grid grid-cols-3 gap-2 w-64 h-64">
                    <!-- 9 interactive cells -->
                </div>
            </div>
            <div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setSupercellPreset('max5')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold transition">Max 5 Supercells ('X')</button>
                <button onclick="setSupercellPreset('random')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold transition">Shuffle Numbers (1–9)</button>
            </div>
        </div>
        """,

        # Sim 3: Number Line Patterns (Scalable Interval Detective)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Number Line Scale Scanner</span>
                <span id="numLineStepBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Step Size = +10</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="numLineSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <line x1="20" y1="120" x2="380" y2="120" stroke="#0ea5e9" stroke-width="3" marker-end="url(#arrowR)" marker-start="url(#arrowL)"/>
                    <g id="numLineTicksGroup"></g>
                    <!-- Mystery marker -->
                    <circle id="mysteryPt" cx="260" cy="120" r="7" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
                    <text id="mysteryLabel" x="250" y="95" fill="#fde047" font-size="14" font-weight="bold" font-family="monospace">? = 40</text>
                </svg>
            </div>
            <div class="grid grid-cols-4 gap-1.5 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setNumberLineScale(2)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold">Steps of 2</button>
                <button onclick="setNumberLineScale(5)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Steps of 5</button>
                <button onclick="setNumberLineScale(10)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold">Steps of 10</button>
                <button onclick="setNumberLineScale(25)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-violet-300 rounded font-bold">Steps of 25</button>
            </div>
        </div>
        """,

        # Sim 4: Digit Counts (Powers of 10 Exponential Explorer)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Digit Count Powers Lab</span>
                <span id="digitCountBadge" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">3 Digits: 900 Numbers</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col items-center justify-center p-4">
                <div id="digitCountVisual" class="w-full flex flex-col items-center justify-center space-y-3">
                    <div class="text-3xl font-black font-mono text-cyan-300" id="digitCountFormula">9 × 10² = 900</div>
                    <div class="text-xs text-slate-300 font-mono" id="digitCountRange">Range: 100 to 999 (999 − 100 + 1 = 900)</div>
                    <div class="w-full bg-slate-800 rounded-full h-4 overflow-hidden mt-2">
                        <div id="digitCountBar" class="h-full bg-gradient-to-r from-amber-500 to-cyan-400 transition-all duration-300" style="width: 50%;"></div>
                    </div>
                </div>
            </div>
            <div class="grid grid-cols-5 gap-1 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setDigitCountSim(1)" class="px-1 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-bold">1 Digit</button>
                <button onclick="setDigitCountSim(2)" class="px-1 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-bold">2 Digits</button>
                <button onclick="setDigitCountSim(3)" class="px-1 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">3 Digits</button>
                <button onclick="setDigitCountSim(4)" class="px-1 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold">4 Digits</button>
                <button onclick="setDigitCountSim(5)" class="px-1 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold">5 Digits</button>
            </div>
        </div>
        """,

        # Sim 5: Digit Sums & The 7-Detective
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Digit Detective Sieve</span>
                <span id="detectiveBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Digit 7 appears: 20 times (1–100)</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col items-center justify-center p-3">
                <div id="detectiveDisplay" class="grid grid-cols-10 gap-1 text-[10px] font-mono text-slate-400 max-h-48 overflow-y-auto w-full text-center">
                    <!-- 100 numbers injected dynamically -->
                </div>
            </div>
            <div class="grid grid-cols-3 gap-2 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="highlightDigitInChart(7)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold">Find '7's (20x)</button>
                <button onclick="highlightDigitSumInChart(14)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Digit Sum = 14</button>
                <button onclick="highlightDigitSumInChart(9)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold">Digit Sum = 9</button>
            </div>
        </div>
        """,

        # Sim 6: Palindromic Number Generator & Mirror
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Palindrome Mirror Lab</span>
                <span id="palMirrorBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">575 is a Palindrome!</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col items-center justify-center p-4">
                <div class="flex items-center gap-4 text-3xl sm:text-4xl font-black font-mono">
                    <span id="palOriginal" class="text-amber-300 bg-slate-950 px-3 py-2 rounded-xl border border-amber-500/30">575</span>
                    <span class="text-slate-600 text-xl font-sans">⇄</span>
                    <span id="palReversed" class="text-cyan-300 bg-slate-950 px-3 py-2 rounded-xl border border-cyan-500/30">575</span>
                </div>
                <div id="palVerdictText" class="mt-4 text-xs font-bold text-emerald-400 font-mono">✓ Reads identically in both directions!</div>
            </div>
            <div class="grid grid-cols-4 gap-1.5 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="testPalindromeInput('66')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono font-bold">66</button>
                <button onclick="testPalindromeInput('848')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">848</button>
                <button onclick="testPalindromeInput('1221')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-mono font-bold">1221</button>
                <button onclick="testPalindromeInput('345')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-mono font-bold">345 (No)</button>
            </div>
        </div>
        """,

        # Sim 7: Reverse-and-Add Machine
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Reverse-and-Add Palindrome Engine</span>
                <span id="revAddStepsBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Reached Palindrome in 2 Steps</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col justify-center p-3 overflow-y-auto">
                <div id="revAddStepsContainer" class="space-y-2 font-mono text-xs text-slate-200">
                    <!-- Iterative steps rendered here -->
                </div>
            </div>
            <div class="grid grid-cols-4 gap-1.5 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="runReverseAndAdd(34)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono font-bold">Start 34</button>
                <button onclick="runReverseAndAdd(57)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">Start 57</button>
                <button onclick="runReverseAndAdd(68)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-mono font-bold">Start 68</button>
                <button onclick="runReverseAndAdd(89)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">Start 89</button>
            </div>
        </div>
        """,

        # Sim 8: Kaprekar's Magic Constant 6174 (Interactive Black Hole Routine)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Kaprekar's 6174 Black Hole</span>
                <span id="kaprekarStepsBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Steps to 6174: 3 Steps</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col justify-center p-3 overflow-y-auto">
                <div id="kaprekarStepsContainer" class="space-y-2 font-mono text-xs text-slate-200">
                    <!-- Iterative Kaprekar subtraction steps rendered here -->
                </div>
            </div>
            <div class="grid grid-cols-4 gap-1.5 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="runKaprekarRoutine(3524)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded font-mono font-bold">3524</button>
                <button onclick="runKaprekarRoutine(9831)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">9831</button>
                <button onclick="runKaprekarRoutine(2002)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-mono font-bold">2002</button>
                <button onclick="runKaprekarRoutine(6174)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">6174</button>
            </div>
        </div>
        """,

        # Sim 9: Clock & Calendar Symmetric Displays
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Symmetric Clock & Calendar Lab</span>
                <span id="clockTypeBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Palindrome Time: 12:21</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col items-center justify-center p-4">
                <!-- Digital Clock Face -->
                <div class="bg-black/80 px-6 py-3 rounded-2xl border-2 border-cyan-500/40 shadow-lg shadow-cyan-500/20 text-center">
                    <span id="digitalClockDisplay" class="text-4xl sm:text-5xl font-black font-mono text-cyan-300 tracking-wider">12:21</span>
                </div>
                <div id="clockDetailsText" class="mt-4 text-xs font-mono text-slate-300 text-center">
                    Reads 1-2-2-1 in reverse • Perfect 4-digit palindrome!
                </div>
            </div>
            <div class="grid grid-cols-4 gap-1.5 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setClockDisplay('12:21', 'Palindrome Time')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">12:21</button>
                <button onclick="setClockDisplay('10:10', 'Repeated Pair')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-mono font-bold">10:10</button>
                <button onclick="setClockDisplay('11:11', 'Repunit Time')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">11:11</button>
                <button onclick="setClockDisplay('04:40', 'Symmetric Mirror')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-violet-300 rounded font-mono font-bold">04:40</button>
            </div>
        </div>
        """,

        # Sim 10: Mental Math Pool Solver (Reaching Targets)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Target Pool Combiner</span>
                <span id="targetStatusBadge" class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">Target = 11</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col items-center justify-center p-4">
                <div class="text-xs text-slate-400 mb-2">Available Pool: [ 2, 3, 5, 7 ]</div>
                <div class="text-2xl sm:text-3xl font-black font-mono text-emerald-300 bg-slate-950 px-4 py-2 rounded-xl border border-emerald-500/30" id="mentalMathExpr">
                    7 + 5 + 2 − 3 = 11
                </div>
                <div class="text-[11px] text-slate-300 mt-3" id="mentalMathExplanation">
                    Shortcut: 7 + 5 = 12, then + 2 = 14, then − 3 = 11!
                </div>
            </div>
            <div class="grid grid-cols-4 gap-1.5 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setMentalTarget(11, '7 + 5 + 2 − 3 = 11')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-mono font-bold">Target 11</button>
                <button onclick="setMentalTarget(13, '7 + 5 + 3 − 2 = 13')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">Target 13</button>
                <button onclick="setMentalTarget(17, '7 + 5 + 3 + 2 = 17')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">Target 17</button>
                <button onclick="setMentalTarget(7, '5 + 3 + 2 − 3 = 7')" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-violet-300 rounded font-mono font-bold">Target 7</button>
            </div>
        </div>
        """,

        # Sim 11: Efficient Sums (Gauss Rainbow Pairing Animator)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Gauss Rainbow Pairing</span>
                <span id="gaussSumBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Sum 1 to 10 = 55</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="gaussSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Gauss rainbow arcs rendered dynamically -->
                    <g id="gaussArcsGroup"></g>
                    <g id="gaussNumbersGroup"></g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setGaussRange(10)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold">Sum 1 to 10 (5 × 11 = 55)</button>
                <button onclick="setGaussRange(20)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Sum 1 to 20 (10 × 21 = 210)</button>
            </div>
        </div>
        """,

        # Sim 12: Collatz Conjecture (Hailstone Rollercoaster Graph)
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Collatz Hailstone Trajectory</span>
                <span id="collatzPeakBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Start 7: Peak 52, Steps 16</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center">
                <svg id="collatzSvg" class="w-full h-full" viewBox="0 0 400 240">
                    <line x1="30" y1="210" x2="380" y2="210" stroke="#475569" stroke-width="1.5"/>
                    <line x1="30" y1="20" x2="30" y2="210" stroke="#475569" stroke-width="1.5"/>
                    <path id="collatzPath" d="" fill="none" stroke="#f59e0b" stroke-width="3"/>
                    <g id="collatzDotsGroup"></g>
                    <text x="35" y="30" fill="#94a3b8" font-size="10">Value</text>
                    <text x="340" y="225" fill="#94a3b8" font-size="10">Steps →</text>
                </svg>
            </div>
            <div class="grid grid-cols-4 gap-1.5 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="runCollatzGraph(7)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-mono font-bold">Start 7</button>
                <button onclick="runCollatzGraph(9)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-mono font-bold">Start 9</button>
                <button onclick="runCollatzGraph(11)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-mono font-bold">Start 11</button>
                <button onclick="runCollatzGraph(15)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-violet-300 rounded font-mono font-bold">Start 15</button>
            </div>
        </div>
        """,

        # Sim 13: Simple Estimation Calculator
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Order-of-Magnitude Estimator</span>
                <span id="estContextBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Daily Steps Estimation</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col items-center justify-center p-4">
                <div class="text-xs text-slate-400 mb-1" id="estScenarioTitle">How many steps do you take in 1 year?</div>
                <div class="text-xl sm:text-2xl font-black font-mono text-amber-300 text-center my-2" id="estFormulaText">
                    8,000 steps/day × 365 days ≈ 3,000,000 steps
                </div>
                <div class="text-xs font-mono text-cyan-300 bg-slate-950 px-3 py-1.5 rounded-lg border border-cyan-800/40 mt-2" id="estComparisonText">
                    Distance: 3,000,000 × 0.6 m ≈ 1,800 kilometers!
                </div>
            </div>
            <div class="grid grid-cols-3 gap-2 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="setEstimationScenario('steps')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold">Yearly Steps</button>
                <button onclick="setEstimationScenario('heartbeats')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">Heartbeats</button>
                <button onclick="setEstimationScenario('books')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold">Book Costs</button>
            </div>
        </div>
        """,

        # Sim 14: Game of 21 Strategy Board
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Game of 21 Strategy Simulator</span>
                <span id="game21TurnBadge" class="font-mono text-cyan-300 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/40">Current Total: 0</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col items-center justify-center p-3">
                <div class="text-center mb-2">
                    <span class="text-xs text-slate-400">Milestones to win: </span>
                    <span class="text-xs font-mono font-bold text-amber-300">4, 8, 12, 16, 20</span>
                </div>
                <div class="text-3xl font-black font-mono text-emerald-300 bg-slate-950 px-5 py-2.5 rounded-2xl border border-emerald-500/30" id="game21CurrentNumber">
                    0
                </div>
                <div id="game21AdviceText" class="mt-2 text-xs font-mono text-amber-300">
                    Your Turn: Pick 1, 2, or 3 numbers!
                </div>
            </div>
            <div class="grid grid-cols-4 gap-1.5 pt-2 border-t border-slate-800 text-center text-xs">
                <button onclick="playGame21Move(1)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-amber-300 rounded font-bold">+1 Number</button>
                <button onclick="playGame21Move(2)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-cyan-300 rounded font-bold">+2 Numbers</button>
                <button onclick="playGame21Move(3)" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-300 rounded font-bold">+3 Numbers</button>
                <button onclick="resetGame21()" class="px-1.5 py-1 bg-slate-800 hover:bg-slate-700 text-rose-300 rounded font-bold">Reset</button>
            </div>
        </div>
        """,

        # Sim 15: Race to 99 Strategy Board
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Race to 99 Simulator</span>
                <span id="race99ScoreBadge" class="font-mono text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-800/40">Current Score: 0</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex flex-col items-center justify-center p-3">
                <div class="text-xs text-slate-400 mb-1">Target Highway: 11, 22, 33, 44, 55, 66, 77, 88, 99!</div>
                <div class="text-3xl font-black font-mono text-cyan-300 bg-slate-950 px-6 py-2 rounded-2xl border border-cyan-500/30 my-2" id="race99CurrentTotal">
                    0 / 99
                </div>
                <div class="w-full bg-slate-800 rounded-full h-3 overflow-hidden max-w-xs">
                    <div id="race99Progress" class="h-full bg-gradient-to-r from-cyan-500 to-emerald-400 transition-all duration-300" style="width: 0%;"></div>
                </div>
            </div>
            <div class="space-y-2 pt-2 border-t border-slate-800">
                <div class="flex items-center justify-between text-xs text-slate-300">
                    <span>Add Number (1 to 10):</span>
                    <span id="raceSliderVal" class="font-mono text-cyan-300 font-bold">+5</span>
                </div>
                <div class="flex items-center gap-2">
                    <input type="range" id="raceSlider" min="1" max="10" value="5" oninput="document.getElementById('raceSliderVal').innerText = '+' + this.value" class="w-full accent-cyan-500 cursor-pointer">
                    <button onclick="playRace99Move(parseInt(document.getElementById('raceSlider').value))" class="px-3 py-1 bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-bold rounded text-xs transition">Add</button>
                    <button onclick="resetRace99()" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold rounded text-xs transition">Reset</button>
                </div>
            </div>
        </div>
        """,

        # Sim 16: Grand Synthesis Interactive Concept Map
        """
        <div class="h-full flex flex-col justify-between p-3 bg-slate-950/70 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
                <span class="font-bold text-amber-300 uppercase tracking-wider">Number Play Synthesis Map</span>
                <span class="font-mono text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">All 12 Modules Integrated</span>
            </div>
            <div class="relative flex-1 my-2 bg-slate-900/90 rounded-lg border border-slate-800/80 overflow-hidden flex items-center justify-center p-2">
                <svg class="w-full h-full" viewBox="0 0 400 240">
                    <!-- Central Hub -->
                    <circle cx="200" cy="120" r="40" fill="#0284c7" fill-opacity="0.2" stroke="#0ea5e9" stroke-width="2"/>
                    <text x="165" y="125" fill="#38bdf8" font-size="12" font-weight="bold">Number Play</text>
                    <!-- Satellites -->
                    <line x1="200" y1="80" x2="200" y2="35" stroke="#475569" stroke-width="2"/>
                    <rect x="140" y="15" width="120" height="25" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
                    <text x="155" y="32" fill="#fde047" font-size="10" font-weight="bold">Kaprekar's 6174</text>

                    <line x1="235" y1="140" x2="310" y2="180" stroke="#475569" stroke-width="2"/>
                    <rect x="270" y="175" width="120" height="25" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
                    <text x="285" y="192" fill="#34d399" font-size="10" font-weight="bold">Gauss 5050 Sum</text>

                    <line x1="165" y1="140" x2="90" y2="180" stroke="#475569" stroke-width="2"/>
                    <rect x="30" y="175" width="120" height="25" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
                    <text x="45" y="192" fill="#c084fc" font-size="10" font-weight="bold">Collatz 3n + 1</text>

                    <line x1="160" y1="120" x2="70" y2="120" stroke="#475569" stroke-width="2"/>
                    <rect x="15" y="105" width="100" height="25" rx="6" fill="#1e293b" stroke="#06b6d4" stroke-width="1.5"/>
                    <text x="25" y="122" fill="#22d3ee" font-size="10" font-weight="bold">Palindromes</text>

                    <line x1="240" y1="120" x2="330" y2="120" stroke="#475569" stroke-width="2"/>
                    <rect x="285" y="105" width="105" height="25" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
                    <text x="295" y="122" fill="#f472b6" font-size="10" font-weight="bold">Game of 21 & 99</text>
                </svg>
            </div>
            <div class="p-2 bg-slate-900/60 rounded text-center text-xs text-slate-300 border border-slate-800">
                Mathematics is a game of recognizing patterns, exploiting invariants, and having fun!
            </div>
        </div>
        """
    ]

    code = f'''"""NCERT Class 6 Mathematics Chapter 3: Number Play Simulators."""

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

    with open(".agents/class6_math_number_play_sims.py", "w", encoding="utf-8") as f:
        f.write(clean_code)

    print("Successfully generated .agents/class6_math_number_play_sims.py with 16 bespoke simulators.")
    print("VERIFIED PASS: Zero raw LaTeX and zero surrogates in simulators module!")

if __name__ == "__main__":
    generate_simulators()
