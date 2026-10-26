# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 2
UNIT II: ALGEBRA (66 Periods, Competencies CG-3, C-3.2, CG-9)
Introduction to Polynomials & Linear Functions
Generates public/animations/class9-polynomials.html with:
- 16 Rich Content Slides covering all curriculum concepts.
- 32 In-Slide Checkpoint Questions with instant teacher feedback.
- 4 Dedicated Mastery Quiz Challenge Slides (40 questions total) with popup solution modals.
- 16 Bespoke Interactive SVG Laboratory Simulators.
- Animated Teacher Avatar (Senior Professor Dr. Sophia) with talking mouth synced to audio narration.
- Web Audio API sound synthesizer and Web Speech API narration (en-US).
- Last Slide Notice with strict unit test compatibility.
"""

import json
import os
import sys

# Ensure data script can be imported
sys.path.append(os.path.dirname(__file__))
from class9_polynomials_data import CONTENT_SLIDES, QUIZ_SLIDES


def generate_interactive_simulator(s_idx):
    """Returns bespoke interactive SVG simulator HTML for each content slide (1-16)."""
    if s_idx == 1:
        # Simulator 1: Expression Anatomy & Polynomial Filter
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.1: Expression Anatomy & Polynomial Filter</span>
                </div>
                <div class="flex flex-wrap items-center gap-1.5">
                    <button onclick="setSim1Expr('poly1')" id="sim1-btn-p1" class="px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white transition">3x² - 5x + 7</button>
                    <button onclick="setSim1Expr('non1')" id="sim1-btn-n1" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">2/x + 4</button>
                    <button onclick="setSim1Expr('non2')" id="sim1-btn-n2" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">5√x - 3</button>
                    <button onclick="setSim1Expr('poly2')" id="sim1-btn-p2" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">√3 x³ + 9</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <svg id="sim1-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Central Large Expression Display -->
                    <rect x="30" y="30" width="440" height="90" rx="14" fill="#0f172a" stroke="#475569" stroke-width="2"/>
                    <text id="sim1-display-expr" x="250" y="75" fill="#facc15" font-size="24" font-weight="black" font-family="monospace" text-anchor="middle">
                        3x² - 5x + 7
                    </text>
                    <text id="sim1-term-breakdown" x="250" y="105" fill="#94a3b8" font-size="10" text-anchor="middle">
                        Terms: [3x²], [-5x], [+7] | Coefficients: [3, -5, 7]
                    </text>

                    <!-- Evaluation Badge Box -->
                    <rect id="sim1-status-box" x="80" y="140" width="340" height="50" rx="10" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
                    <text id="sim1-status-text" x="250" y="162" fill="#6ee7b7" font-size="12" font-weight="black" text-anchor="middle">
                        ✓ VALID POLYNOMIAL IN ONE VARIABLE
                    </text>
                    <text id="sim1-status-sub" x="250" y="178" fill="#d1fae5" font-size="9.5" text-anchor="middle">
                        All exponents of x are whole numbers: 2, 1, 0 ∈ 𝕎
                    </text>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim1-caption">Polynomial Criterion:</span>
                    <span id="sim1-desc">To be a polynomial, every exponent of the variable x must belong to the whole numbers {0, 1, 2, 3, ...}. Real coefficients (including roots) are completely allowed!</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 2:
        # Simulator 2: Degree & Classification Matrix
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.2: Degree & Polynomial Classifier Matrix</span>
                </div>
                <div class="flex flex-wrap items-center gap-1.5 text-xs">
                    <button onclick="setSim2Poly('zero')" id="sim2-btn-zero" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300">0</button>
                    <button onclick="setSim2Poly('const')" id="sim2-btn-const" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300">7</button>
                    <button onclick="setSim2Poly('linear')" id="sim2-btn-linear" class="px-2 py-0.5 rounded font-bold bg-indigo-600 text-white">4x - 9</button>
                    <button onclick="setSim2Poly('quad')" id="sim2-btn-quad" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300">x² + 5x + 6</button>
                    <button onclick="setSim2Poly('cubic')" id="sim2-btn-cubic" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300">2x³ - x</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center h-full">
                    <div class="p-4 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-center">
                        <span class="text-xs font-bold text-slate-400">Selected Polynomial P(x):</span>
                        <div class="text-xl font-mono font-black text-amber-300" id="sim2-poly-str">P(x) = 4x - 9</div>
                        <div class="text-xs text-sky-300">
                            <strong>Terms count:</strong> <span id="sim2-term-count" class="font-mono text-emerald-400">2 (Binomial)</span>
                        </div>
                    </div>

                    <div class="p-4 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                        <div class="flex justify-between items-center text-xs">
                            <span class="text-slate-400">Degree (Highest Power):</span>
                            <span class="font-bold text-amber-400 text-sm font-mono" id="sim2-deg-val">1 (Linear)</span>
                        </div>
                        <div class="flex justify-between items-center text-xs">
                            <span class="text-slate-400">Leading Coefficient:</span>
                            <span class="font-bold text-sky-400 font-mono" id="sim2-lead-coef">4</span>
                        </div>
                        <div class="flex justify-between items-center text-xs">
                            <span class="text-slate-400">Geometric Graph Type:</span>
                            <span class="font-bold text-emerald-400" id="sim2-graph-type">Straight Line</span>
                        </div>
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">Classification Insight:</span>
                    <span id="sim2-insight">A polynomial of degree 1 is a Linear polynomial. When graphed on the Cartesian plane, it produces a continuous straight line.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 3:
        # Simulator 3: Zero of a Linear Polynomial (x = -b/a)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.3: Zero of Linear Polynomial ($x = -b/a$)</span>
                </div>
                <div class="flex items-center gap-2 text-xs">
                    <span class="text-slate-400">Preset:</span>
                    <button onclick="setSim3Preset(2, -6)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">2x - 6</button>
                    <button onclick="setSim3Preset(3, 9)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">3x + 9</button>
                    <button onclick="setSim3Preset(-2, 4)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">-2x + 4</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <!-- Controls Grid -->
                <div class="grid grid-cols-2 gap-4 mb-2">
                    <div class="bg-slate-900/80 p-2.5 rounded-xl border border-slate-800">
                        <div class="flex justify-between text-xs font-bold mb-1">
                            <span class="text-amber-400">Slope ($a \neq 0$):</span>
                            <span id="sim3-val-a" class="font-mono text-amber-300">2</span>
                        </div>
                        <input type="range" id="sim3-slider-a" min="-5" max="5" value="2" oninput="updateSim3()" class="w-full accent-amber-500 cursor-pointer">
                    </div>
                    <div class="bg-slate-900/80 p-2.5 rounded-xl border border-slate-800">
                        <div class="flex justify-between text-xs font-bold mb-1">
                            <span class="text-sky-400">Constant ($b$):</span>
                            <span id="sim3-val-b" class="font-mono text-sky-300">-6</span>
                        </div>
                        <input type="range" id="sim3-slider-b" min="-10" max="10" value="-6" oninput="updateSim3()" class="w-full accent-sky-500 cursor-pointer">
                    </div>
                </div>

                <svg id="sim3-canvas" viewBox="0 0 500 120" class="w-full">
                    <!-- Horizontal Number Line -->
                    <line x1="30" y1="60" x2="470" y2="60" stroke="#64748b" stroke-width="3"/>
                    <line x1="250" y1="45" x2="250" y2="75" stroke="#f59e0b" stroke-width="2.5"/>
                    <text x="250" y="95" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">0</text>

                    <!-- Dynamic Zero Marker -->
                    <g id="sim3-root-marker">
                        <circle cx="340" cy="60" r="7" fill="#10b981" stroke="#fff" stroke-width="2"/>
                        <rect x="300" y="10" width="80" height="25" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
                        <text id="sim3-root-text" x="340" y="27" fill="#a7f3d0" font-size="10" font-weight="black" text-anchor="middle">x = 3</text>
                    </g>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2 rounded-lg text-xs text-slate-200 mt-1">
                    <span class="font-bold text-amber-400">Root Derivation:</span>
                    <span id="sim3-derivation">Set 2x - 6 = 0 ➔ 2x = 6 ➔ x = 6/2 = 3.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 4:
        # Simulator 4: Arithmetic Sequence & Function Machine
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.4: Arithmetic Sequence & Function Machine</span>
                </div>
                <div class="flex items-center gap-1.5 text-xs">
                    <button onclick="setSim4Pattern('3n+1')" id="sim4-btn-1" class="px-2 py-0.5 rounded font-bold bg-indigo-600 text-white">4, 7, 10, 13</button>
                    <button onclick="setSim4Pattern('5n-2')" id="sim4-btn-2" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300">3, 8, 13, 18</button>
                    <button onclick="setSim4Pattern('-2n+10')" id="sim4-btn-3" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300">8, 6, 4, 2</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="grid grid-cols-4 gap-2 text-center font-mono text-xs my-auto">
                    <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                        <span class="text-[10px] text-slate-400 block">n = 1</span>
                        <span class="text-base font-bold text-amber-300" id="sim4-val-1">4</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                        <span class="text-[10px] text-slate-400 block">n = 2</span>
                        <span class="text-base font-bold text-amber-300" id="sim4-val-2">7</span>
                        <span class="text-[9px] text-emerald-400 block mt-0.5" id="sim4-diff-1">Δ = +3</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                        <span class="text-[10px] text-slate-400 block">n = 3</span>
                        <span class="text-base font-bold text-amber-300" id="sim4-val-3">10</span>
                        <span class="text-[9px] text-emerald-400 block mt-0.5" id="sim4-diff-2">Δ = +3</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                        <span class="text-[10px] text-slate-400 block">n = 4</span>
                        <span class="text-base font-bold text-amber-300" id="sim4-val-4">13</span>
                        <span class="text-[9px] text-emerald-400 block mt-0.5" id="sim4-diff-3">Δ = +3</span>
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim4-formula">Linear Rule: f(n) = 3n + 1</span>
                    <span id="sim4-desc">The first difference is constant (+3), proving that arithmetic sequences are direct physical implementations of linear polynomials!</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 5:
        # Simulator 5: Linear Growth Simulator (Taxi Fare)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.5: Linear Growth Engine (Taxi Meter Model)</span>
                </div>
                <div class="flex items-center gap-2 text-xs">
                    <span class="text-slate-400">Distance traveled:</span>
                    <span id="sim5-dist-val" class="font-mono text-amber-300 font-bold">5 km</span>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
                    <div class="space-y-3 bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                        <div>
                            <span class="text-xs font-bold text-slate-300">Move Distance Slider:</span>
                            <input type="range" id="sim5-slider-dist" min="0" max="20" value="5" oninput="updateSim5()" class="w-full accent-emerald-500 cursor-pointer mt-1">
                        </div>
                        <div class="text-[11px] text-slate-400 font-mono">
                            Base Fare: ₹50<br>
                            Rate: ₹12 per km<br>
                            Formula: F(d) = 12d + 50
                        </div>
                    </div>

                    <div class="p-4 rounded-xl bg-emerald-950/80 border border-emerald-500 text-center space-y-1">
                        <span class="text-[10px] font-bold text-emerald-300 uppercase tracking-widest">Total Fare Payable</span>
                        <div class="text-3xl font-black text-white" id="sim5-fare-total">₹110</div>
                        <p class="text-[10px] text-emerald-300 font-mono" id="sim5-calc-breakdown">
                            12 × 5 km + ₹50 = ₹110
                        </p>
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-emerald-400">Linear Growth Characteristics:</span>
                    <span id="sim5-summary">Slope a = +12 (positive rate of change). Every additional kilometer costs exactly ₹12 more.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 6:
        # Simulator 6: Linear Decay Simulator (Water Reservoir Drainage)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.6: Linear Decay Engine (Reservoir Drainage)</span>
                </div>
                <div class="flex items-center gap-2 text-xs">
                    <span class="text-slate-400">Time elapsed:</span>
                    <span id="sim6-time-val" class="font-mono text-rose-300 font-bold">10 min</span>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
                    <div class="space-y-3 bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                        <div>
                            <span class="text-xs font-bold text-slate-300">Drain Time Slider (minutes):</span>
                            <input type="range" id="sim6-slider-time" min="0" max="40" value="10" oninput="updateSim6()" class="w-full accent-rose-500 cursor-pointer mt-1">
                        </div>
                        <div class="text-[11px] text-slate-400 font-mono">
                            Initial Volume: 1000 L<br>
                            Drain Rate: -25 L/min<br>
                            Model: V(t) = -25t + 1000
                        </div>
                    </div>

                    <div class="p-4 rounded-xl bg-rose-950/80 border border-rose-500 text-center space-y-1">
                        <span class="text-[10px] font-bold text-rose-300 uppercase tracking-widest">Remaining Water</span>
                        <div class="text-3xl font-black text-white" id="sim6-vol-total">750 L</div>
                        <p class="text-[10px] text-rose-300 font-mono" id="sim6-time-to-empty">
                            Empties completely at t = 40 min
                        </p>
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-rose-400">Linear Decay Characteristics:</span>
                    <span id="sim6-summary">Slope a = -25 (negative rate). The reservoir volume decreases by exactly 25 liters every minute.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 7:
        # Simulator 7: Two-Variable Table & Coordinate Plotter
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.7: Two-Variable Function Table Engine</span>
                </div>
                <div class="flex items-center gap-1.5 text-xs">
                    <button onclick="setSim7Eq('2x-1')" id="sim7-btn-1" class="px-2 py-0.5 rounded font-bold bg-indigo-600 text-white">y = 2x - 1</button>
                    <button onclick="setSim7Eq('-x+3')" id="sim7-btn-2" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300">y = -x + 3</button>
                    <button onclick="setSim7Eq('3x')" id="sim7-btn-3" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300">y = 3x</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="overflow-x-auto my-auto">
                    <table class="w-full text-center border-collapse border border-slate-800 font-mono text-xs">
                        <thead>
                            <tr class="bg-slate-900 text-sky-400">
                                <th class="p-2 border border-slate-800">Input (x)</th>
                                <th class="p-2 border border-slate-800">-2</th>
                                <th class="p-2 border border-slate-800">-1</th>
                                <th class="p-2 border border-slate-800">0</th>
                                <th class="p-2 border border-slate-800">1</th>
                                <th class="p-2 border border-slate-800">2</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800">
                            <tr>
                                <td class="p-2 font-bold text-amber-400">Output (y)</td>
                                <td class="p-2 text-white" id="sim7-y-m2">-5</td>
                                <td class="p-2 text-white" id="sim7-y-m1">-3</td>
                                <td class="p-2 text-white" id="sim7-y-0">-1</td>
                                <td class="p-2 text-white" id="sim7-y-p1">1</td>
                                <td class="p-2 text-white" id="sim7-y-p2">3</td>
                            </tr>
                            <tr class="bg-slate-900/60 text-emerald-400 text-[10px]">
                                <td class="p-2 text-slate-400 font-bold">Ordered Pair (x, y)</td>
                                <td class="p-2" id="sim7-pt-m2">(-2, -5)</td>
                                <td class="p-2" id="sim7-pt-m1">(-1, -3)</td>
                                <td class="p-2" id="sim7-pt-0">(0, -1)</td>
                                <td class="p-2" id="sim7-pt-p1">(1, 1)</td>
                                <td class="p-2" id="sim7-pt-p2">(2, 3)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim7-caption">Equation: y = 2x - 1</span>
                    <span id="sim7-desc">Each pair of numbers (x, y) represents a geometric point on the Cartesian plane that lies on the straight line.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 8:
        # Simulator 8: Interactive Cartesian Coordinate Plane Grapher
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.8: Cartesian Coordinate Plane Grapher</span>
                </div>
                <div class="flex items-center gap-2 text-xs">
                    <button onclick="setSim8Line(1, 0)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">y = x</button>
                    <button onclick="setSim8Line(2, -1)" class="px-2 py-0.5 rounded bg-indigo-600 text-white font-bold">y = 2x - 1</button>
                    <button onclick="setSim8Line(-1, 2)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">y = -x + 2</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <svg id="sim8-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Grid Lines -->
                    <g stroke="#1e293b" stroke-width="1">
                        <line x1="50" y1="0" x2="50" y2="240"/>
                        <line x1="150" y1="0" x2="150" y2="240"/>
                        <line x1="250" y1="0" x2="250" y2="240"/>
                        <line x1="350" y1="0" x2="350" y2="240"/>
                        <line x1="450" y1="0" x2="450" y2="240"/>
                        <line x1="0" y1="40" x2="500" y2="40"/>
                        <line x1="0" y1="120" x2="500" y2="120"/>
                        <line x1="0" y1="200" x2="500" y2="200"/>
                    </g>

                    <!-- Coordinate Axes -->
                    <line x1="0" y1="120" x2="500" y2="120" stroke="#94a3b8" stroke-width="2.5"/>
                    <line x1="250" y1="0" x2="250" y2="240" stroke="#94a3b8" stroke-width="2.5"/>
                    <text x="490" y="115" fill="#94a3b8" font-size="10" font-weight="bold">X</text>
                    <text x="255" y="15" fill="#94a3b8" font-size="10" font-weight="bold">Y</text>

                    <!-- The Line Graph (origin at 250, 120; scale 40px per unit) -->
                    <line id="sim8-line" x1="50" y1="240" x2="350" y2="0" stroke="#f59e0b" stroke-width="3.5" stroke-linecap="round"/>

                    <!-- Intercept Points -->
                    <circle id="sim8-yint-pt" cx="250" cy="160" r="5" fill="#ec4899"/>
                    <text id="sim8-yint-lbl" x="260" y="165" fill="#f472b6" font-size="9" font-weight="bold">(0, -1)</text>

                    <circle id="sim8-xint-pt" cx="270" cy="120" r="5" fill="#10b981"/>
                    <text id="sim8-xint-lbl" x="270" y="110" fill="#6ee7b7" font-size="9" font-weight="bold">(0.5, 0)</text>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim8-eqn-title">Graph of y = 2x - 1:</span>
                    <span id="sim8-eqn-desc">A straight line crossing the y-axis at (0, -1) and the x-axis at (0.5, 0).</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 9:
        # Simulator 9: Slope Dynamic Lever (Rise / Run)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.9: Slope Dynamic Lever (Rise / Run)</span>
                </div>
                <div class="flex items-center gap-2 text-xs">
                    <span class="text-slate-400">Slope ($m$):</span>
                    <span id="sim9-m-val" class="font-mono text-amber-300 font-bold">1.5</span>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="flex items-center gap-3 bg-slate-900/80 p-2 rounded-xl border border-slate-800 mb-2">
                    <span class="text-xs font-bold text-slate-300">Adjust Slope:</span>
                    <input type="range" id="sim9-m-slider" min="-3" max="3" step="0.5" value="1.5" oninput="updateSim9()" class="w-full accent-amber-500 cursor-pointer">
                </div>

                <svg id="sim9-canvas" viewBox="0 0 500 160" class="w-full">
                    <!-- Base horizontal run -->
                    <line x1="150" y1="120" x2="350" y2="120" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,2"/>
                    <text x="250" y="135" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Run (Δx = 2)</text>

                    <!-- Vertical rise -->
                    <line id="sim9-rise-line" x1="350" y1="120" x2="350" y2="45" stroke="#ec4899" stroke-width="2.5" stroke-dasharray="4,2"/>
                    <text id="sim9-rise-text" x="365" y="85" fill="#ec4899" font-size="10" font-weight="bold">Rise (Δy = 3)</text>

                    <!-- The Hypotenuse Line -->
                    <line id="sim9-hyp-line" x1="100" y1="140" x2="400" y2="25" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2 rounded-lg text-xs text-slate-200 mt-1">
                    <span class="font-bold text-amber-400" id="sim9-status">Slope m = Rise / Run = 3 / 2 = 1.5</span>
                    <span id="sim9-dir">Positive slope: The line ascends from left to right.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 10:
        # Simulator 10: y-Intercept and x-Intercept Hunter
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.10: Intercept Hunter Engine</span>
                </div>
                <div class="flex items-center gap-1.5 text-xs">
                    <button onclick="setSim10Line(3, -6)" class="px-2 py-0.5 rounded font-bold bg-indigo-600 text-white">3x - 6</button>
                    <button onclick="setSim10Line(-2, 8)" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300"> -2x + 8</button>
                    <button onclick="setSim10Line(1, 4)" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300">x + 4</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="grid grid-cols-2 gap-3 my-auto">
                    <div class="p-3.5 rounded-xl bg-slate-900 border border-amber-500/40 text-center space-y-1">
                        <span class="text-[10px] uppercase font-bold text-amber-400">y-Intercept (x = 0)</span>
                        <div class="text-xl font-mono font-black text-amber-300" id="sim10-yint-val">(0, -6)</div>
                        <p class="text-[10px] text-slate-400">Starting point on vertical axis</p>
                    </div>

                    <div class="p-3.5 rounded-xl bg-slate-900 border border-emerald-500/40 text-center space-y-1">
                        <span class="text-[10px] uppercase font-bold text-emerald-400">x-Intercept (y = 0)</span>
                        <div class="text-xl font-mono font-black text-emerald-300" id="sim10-xint-val">(2, 0)</div>
                        <p class="text-[10px] text-slate-400">Zero of the polynomial</p>
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim10-formula">Line: y = 3x - 6</span>
                    <span id="sim10-desc">Setting x = 0 gives y = -6 (y-intercept); setting y = 0 gives 3x = 6 ➔ x = 2 (x-intercept).</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 11:
        # Simulator 11: 3-Point Graphing Verification Algorithm
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.11: 3-Point Collinearity Verification</span>
                </div>
                <button onclick="testCollinearSim11()" id="sim11-test-btn" class="px-3 py-1 rounded text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition cursor-pointer">
                    Check Collinearity ➔
                </button>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <svg id="sim11-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Grid background -->
                    <line x1="0" y1="120" x2="500" y2="120" stroke="#334155" stroke-width="1.5"/>
                    <line x1="250" y1="0" x2="250" y2="240" stroke="#334155" stroke-width="1.5"/>

                    <!-- Point 1 (y-intercept) -->
                    <circle cx="250" cy="180" r="6" fill="#38bdf8"/>
                    <text x="260" y="185" fill="#7dd3fc" font-size="10" font-weight="bold">P1(0, -1)</text>

                    <!-- Point 2 (x-intercept) -->
                    <circle cx="310" cy="120" r="6" fill="#38bdf8"/>
                    <text x="310" y="110" fill="#7dd3fc" font-size="10" font-weight="bold">P2(1.5, 0)</text>

                    <!-- Point 3 (test point) -->
                    <circle cx="370" cy="60" r="6" fill="#f59e0b"/>
                    <text x="370" y="50" fill="#fef08a" font-size="10" font-weight="bold">P3(3, 1)</text>

                    <!-- Connecting ruler line -->
                    <line id="sim11-ruler" x1="190" y1="240" x2="430" y2="0" stroke="#10b981" stroke-width="3" stroke-dasharray="6,3" class="hidden"/>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim11-status">Collinearity Test:</span>
                    <span id="sim11-desc">Click 'Check Collinearity' to verify that all three points lie on the exact same straight line.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 12:
        # Simulator 12: Direct Variation vs Affine (y = kx vs y = kx + c)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.12: Proportional (y = kx) vs Affine (y = ax + b)</span>
                </div>
                <div class="flex items-center gap-2 text-xs">
                    <button onclick="toggleSim12('direct')" id="sim12-btn-dir" class="px-2.5 py-1 rounded font-bold bg-cyan-600 text-white">Direct (y = 2x)</button>
                    <button onclick="toggleSim12('affine')" id="sim12-btn-aff" class="px-2.5 py-1 rounded font-bold bg-slate-800 text-slate-300">Affine (y = 2x + 3)</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <svg id="sim12-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <line x1="0" y1="180" x2="500" y2="180" stroke="#475569" stroke-width="2"/>
                    <line x1="100" y1="0" x2="100" y2="240" stroke="#475569" stroke-width="2"/>
                    <circle cx="100" cy="180" r="5" fill="#f59e0b"/>
                    <text x="90" y="195" fill="#fef08a" font-size="10" font-weight="bold">(0,0)</text>

                    <!-- Direct line passes through (100, 180) -->
                    <line id="sim12-line" x1="100" y1="180" x2="400" y2="40" stroke="#06b6d4" stroke-width="4"/>
                    <circle id="sim12-start-pt" cx="100" cy="180" r="6" fill="#06b6d4"/>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-cyan-400" id="sim12-title">Direct Proportionality (y = 2x):</span>
                    <span id="sim12-desc">Passes directly through the origin (0, 0). Doubling x exactly doubles y.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 13:
        # Simulator 13: Computational Inverse Pattern Discovery Algorithm
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.13: Algorithmic Equation Extractor</span>
                </div>
                <button onclick="solveSim13Pattern()" id="sim13-solve-btn" class="px-3 py-1 rounded text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition cursor-pointer">
                    Extract Formula ➔
                </button>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="bg-slate-900/90 border border-slate-700 p-3 rounded-xl flex-1 flex flex-col justify-center space-y-2 font-mono text-xs">
                    <div class="text-slate-400">
                        Input Dataset: (x1, y1) = (2, 7),  (x2, y2) = (5, 16)
                    </div>
                    <div class="text-amber-400 font-bold" id="sim13-step1">
                        Step 1: Compute Slope a = (16 - 7) / (5 - 2) = 9 / 3 = 3
                    </div>
                    <div class="text-sky-300 font-bold" id="sim13-step2">
                        Step 2: Solve Intercept b = y1 - a(x1) = 7 - 3(2) = 1
                    </div>
                    <div class="text-emerald-400 font-bold text-sm bg-slate-950 p-2 rounded-lg border border-slate-800" id="sim13-result">
                        Discovered Formula: y = 3x + 1  | Prediction for x = 10: y = 31
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">Algorithmic Automation:</span>
                    <span id="sim13-desc">This 4-step logic is the exact algorithm modern data analysis tools use to fit linear regression models to empirical measurements.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 14:
        # Simulator 14: Linear Physics Motion (d = vt + d0)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.14: Linear Kinematics Simulator ($d = vt + d_0$)</span>
                </div>
                <div class="flex items-center gap-2 text-xs">
                    <span class="text-slate-400">Speed (v):</span>
                    <span id="sim14-v-val" class="font-mono text-amber-300 font-bold">20 m/s</span>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="grid grid-cols-2 gap-3 mb-2">
                    <div class="bg-slate-900/80 p-2 rounded-xl border border-slate-800">
                        <span class="text-xs font-bold text-slate-300">Speed Slider (m/s):</span>
                        <input type="range" id="sim14-speed-slider" min="5" max="40" value="20" oninput="updateSim14()" class="w-full accent-amber-500 cursor-pointer mt-1">
                    </div>
                    <div class="bg-slate-900/80 p-2 rounded-xl border border-slate-800">
                        <span class="text-xs font-bold text-slate-300">Initial Pos $d_0$ (m):</span>
                        <input type="range" id="sim14-d0-slider" min="0" max="100" value="50" oninput="updateSim14()" class="w-full accent-sky-500 cursor-pointer mt-1">
                    </div>
                </div>

                <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800 text-center font-mono space-y-1">
                    <span class="text-xs font-bold text-slate-400">Kinematic Distance Equation:</span>
                    <div class="text-xl font-bold text-emerald-400" id="sim14-eqn-display">d(t) = 20t + 50</div>
                    <p class="text-[11px] text-slate-300" id="sim14-after-5s">At t = 5 seconds: d(5) = 20(5) + 50 = 150 meters</p>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">Physics Connection:</span>
                    <span id="sim14-desc">Speed v is the slope (rate of change of distance with respect to time). Initial position d0 is the y-intercept.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 15:
        # Simulator 15: Break-Even Economics Simulator
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.15: Break-Even Economics Solver</span>
                </div>
                <div class="flex items-center gap-2 text-xs">
                    <span class="text-slate-400">Units produced ($x$):</span>
                    <span id="sim15-units-val" class="font-mono text-amber-300 font-bold">20 units</span>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="bg-slate-900/80 p-2 rounded-xl border border-slate-800 mb-2">
                    <input type="range" id="sim15-slider-units" min="0" max="40" value="20" oninput="updateSim15()" class="w-full accent-amber-500 cursor-pointer">
                </div>

                <div class="grid grid-cols-3 gap-2 text-center text-xs">
                    <div class="p-2.5 rounded-xl bg-rose-950/60 border border-rose-500/40">
                        <span class="text-[10px] text-rose-300 block">Total Cost C(x)</span>
                        <span class="font-bold text-sm text-white" id="sim15-cost-disp">₹1200</span>
                        <span class="text-[9px] text-slate-400 block mt-0.5">20x + 800</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-emerald-950/60 border border-emerald-500/40">
                        <span class="text-[10px] text-emerald-300 block">Total Revenue R(x)</span>
                        <span class="font-bold text-sm text-white" id="sim15-rev-disp">₹1200</span>
                        <span class="text-[9px] text-slate-400 block mt-0.5">60x</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-indigo-950/60 border border-indigo-500/40">
                        <span class="text-[10px] text-indigo-300 block">Net Profit / Loss</span>
                        <span class="font-bold text-sm text-amber-300" id="sim15-net-disp">₹0 (Break-Even)</span>
                        <span class="text-[9px] text-slate-400 block mt-0.5">R(x) - C(x)</span>
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim15-status-title">Break-Even Point: x* = 20 units</span>
                    <span id="sim15-status-desc">Cost and Revenue curves intersect at x = 20. Producing fewer than 20 units results in loss; producing more yields net profit!</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 16:
        # Simulator 16: Interactive Linear Polynomial Sandbox
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 2.16: Linear Polynomial Sandbox & Diagnostic Suite</span>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="grid grid-cols-2 gap-3 mb-2">
                    <div class="bg-slate-900/80 p-2 rounded-xl border border-slate-800">
                        <div class="flex justify-between text-xs font-bold mb-1">
                            <span class="text-amber-400">Slope ($a$):</span>
                            <span id="sim16-val-a" class="font-mono text-amber-300">1</span>
                        </div>
                        <input type="range" id="sim16-slider-a" min="-4" max="4" value="1" oninput="updateSim16()" class="w-full accent-amber-500 cursor-pointer">
                    </div>
                    <div class="bg-slate-900/80 p-2 rounded-xl border border-slate-800">
                        <div class="flex justify-between text-xs font-bold mb-1">
                            <span class="text-sky-400">Intercept ($b$):</span>
                            <span id="sim16-val-b" class="font-mono text-sky-300">2</span>
                        </div>
                        <input type="range" id="sim16-slider-b" min="-6" max="6" value="2" oninput="updateSim16()" class="w-full accent-sky-500 cursor-pointer">
                    </div>
                </div>

                <div class="p-3 rounded-xl bg-slate-900/90 border border-slate-800 text-center font-mono space-y-1">
                    <div class="text-lg font-bold text-amber-300" id="sim16-poly-display">y = 1x + 2</div>
                    <div class="flex justify-around text-xs text-slate-300 pt-1">
                        <span>Root: <strong class="text-emerald-400" id="sim16-diag-root">x = -2</strong></span>
                        <span>y-Intercept: <strong class="text-sky-400" id="sim16-diag-yint">(0, 2)</strong></span>
                        <span>Behavior: <strong class="text-purple-400" id="sim16-diag-beh">Linear Growth</strong></span>
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">Comprehensive Synthesis:</span>
                    <span id="sim16-desc">Linear polynomials form the core building blocks of mathematical modelling, rate estimation, and computational thinking across all science and commerce disciplines.</span>
                </div>
            </div>
        </div>
        """

    return ""


def build_full_html():
    """Compiles the master HTML for Class 9 Maths Chapter 2: Introduction to Polynomials & Linear Functions."""

    all_slides = []

    # Process 16 Content Slides
    for s_idx_0, slide in enumerate(CONTENT_SLIDES):
        s_idx = s_idx_0 + 1

        simulator_html = generate_interactive_simulator(s_idx)

        # 2 In-slide checkpoints
        checkpoints_html = ""
        for c_idx, cp in enumerate(slide["checkpoints"]):
            opts_html = ""
            for o_idx, opt in enumerate(cp["options"]):
                opts_html += f"""
                <button onclick="checkOption({s_idx}, {c_idx}, {o_idx}, {cp['ans']})" id="opt-{s_idx}-{c_idx}-{o_idx}" class="w-full text-left p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs text-slate-300 transition flex items-center justify-between cursor-pointer">
                    <span>{opt}</span>
                    <span id="mark-{s_idx}-{c_idx}-{o_idx}" class="text-xs font-bold"></span>
                </button>
                """

            checkpoints_html += f"""
            <div class="p-4 rounded-2xl bg-slate-950/80 border border-slate-800 space-y-2 mb-3">
                <span class="px-2 py-0.5 rounded text-[10px] font-extrabold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                    Checkpoint {c_idx + 1}
                </span>
                <p class="text-xs font-bold text-slate-200 mt-1">{cp['question']}</p>
                <div class="space-y-1.5 mt-2">
                    {opts_html}
                </div>
                <div id="feedback-{s_idx}-{c_idx}" class="hidden p-2 rounded-lg text-xs mt-2 bg-slate-900 border border-slate-800 text-slate-300">
                    <span class="font-bold text-amber-400">Professor Sophia's Insight:</span> {cp['explanation']}
                </div>
            </div>
            """

        teacher_card_html = f"""
        <!-- Person Talking: Dr. Sophia Senior Mathematics Professor Avatar -->
        <div class="mb-6 p-4 rounded-2xl bg-gradient-to-r from-indigo-950/40 via-slate-900 to-cyan-950/20 border border-indigo-500/30 flex flex-col sm:flex-row items-center sm:items-start gap-4 shadow-xl">
            <div class="relative shrink-0 flex flex-col items-center teacher-bob">
                <svg viewBox="0 0 120 120" class="w-20 h-20 sm:w-24 sm:h-24 drop-shadow-lg">
                    <!-- Academic Blazer in Royal Indigo -->
                    <path d="M20 115 C20 85, 45 80, 60 80 C75 80, 100 85, 100 115 Z" fill="#1e1b4b" stroke="#4338ca" stroke-width="2"/>
                    <!-- Crisp White Shirt Collar & Coral Tie -->
                    <polygon points="50,80 60,95 70,80 60,82" fill="#ffffff"/>
                    <polygon points="58,83 62,83 64,115 56,115" fill="#f43f5e"/>
                    <!-- Neck -->
                    <rect x="52" y="68" width="16" height="15" fill="#fed7aa" rx="2"/>
                    <!-- Face -->
                    <ellipse cx="60" cy="50" rx="24" ry="26" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
                    <!-- Glasses -->
                    <rect x="42" y="44" width="15" height="10" rx="3" fill="none" stroke="#0f172a" stroke-width="2"/>
                    <rect x="63" y="44" width="15" height="10" rx="3" fill="none" stroke="#0f172a" stroke-width="2"/>
                    <line x1="57" y1="48" x2="63" y2="48" stroke="#0f172a" stroke-width="2"/>
                    <!-- Eyes behind glasses -->
                    <circle cx="49.5" cy="49" r="2.5" fill="#0f172a"/>
                    <circle cx="70.5" cy="49" r="2.5" fill="#0f172a"/>
                    <circle cx="50.5" cy="48" r="0.8" fill="#ffffff"/>
                    <circle cx="71.5" cy="48" r="0.8" fill="#ffffff"/>
                    <!-- Eyebrows -->
                    <path d="M43 40 Q49 37 55 40" fill="none" stroke="#451a03" stroke-width="2"/>
                    <path d="M65 40 Q71 37 77 40" fill="none" stroke="#451a03" stroke-width="2"/>
                    <!-- Animated Talking Mouth -->
                    <ellipse id="teacherMouth-{s_idx}" cx="60" cy="63" rx="5" ry="3" fill="#be123c"/>
                    <!-- Hair -->
                    <path d="M35 50 Q30 20 60 18 Q90 20 85 50 Q75 14 60 16 Q45 14 35 50 Z" fill="#292524"/>
                </svg>
                <span class="px-2 py-0.5 rounded-full text-[9px] font-extrabold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 mt-1">
                    Prof. Sophia • Math Lead
                </span>
            </div>

            <div class="flex-1 bg-slate-950 p-3.5 rounded-2xl border border-slate-800 relative">
                <div class="hidden sm:block absolute -left-2 top-6 w-3 h-3 bg-slate-950 border-l border-b border-slate-800 transform rotate-45"></div>
                <div class="flex items-center justify-between mb-1.5">
                    <span class="text-xs font-bold text-indigo-400 flex items-center gap-1.5">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 100-6 3 3 0 000 6z"/></svg>
                        Professor Sophia's Audio Walkthrough (Algebra & Modeling)
                    </span>
                    <button onclick="speakSlideNarration({s_idx})" class="px-2.5 py-1 rounded-lg text-xs font-bold bg-indigo-600 hover:bg-indigo-500 text-white transition flex items-center gap-1 cursor-pointer">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/></svg>
                        Listen (Prof. Sophia)
                    </button>
                </div>
                <p class="text-xs text-slate-300 leading-relaxed italic" id="speech-bubble-{s_idx}">
                    "{slide['narration']}"
                </p>
            </div>
        </div>
        """

        slide_html = f"""
        <!-- Slide {s_idx}: {slide['title']} -->
        <section id="slide-{s_idx}" class="slide-section hidden w-full max-w-5xl mx-auto px-4 py-6">
            <div class="mb-4 flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
                <div>
                    <span class="px-2.5 py-1 rounded-full text-xs font-extrabold bg-indigo-500/20 text-indigo-400 border border-indigo-500/30">
                        Slide {s_idx} / 20 • NCERT Class 9 Mathematics
                    </span>
                    <h2 class="text-xl sm:text-2xl font-black text-white mt-1 tracking-tight">{slide['title']}</h2>
                    <p class="text-xs text-indigo-300 font-medium">{slide['subtitle']}</p>
                </div>
                <div class="flex items-center gap-2">
                    <span class="px-2.5 py-1 rounded-lg text-xs font-mono bg-slate-900 text-indigo-400 border border-indigo-500/30">
                        Unit II • Algebra: Polynomials (66 Periods)
                    </span>
                </div>
            </div>

            {teacher_card_html}
            {simulator_html}

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                <!-- Theory & Detailed Concept Notes -->
                <div class="lg:col-span-7 bg-slate-950 p-5 rounded-2xl border border-slate-800 shadow-xl">
                    <div class="flex items-center gap-2 mb-3 border-b border-slate-800 pb-2">
                        <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                        <h3 class="font-bold text-xs uppercase tracking-wider text-indigo-400">Curriculum Concepts, Models & Computational Thinking</h3>
                    </div>
                    {slide['theory']}
                </div>

                <!-- 2 Checkpoints for this slide -->
                <div class="lg:col-span-5 bg-slate-950 p-5 rounded-2xl border border-slate-800 shadow-xl flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-2 mb-3 border-b border-slate-800 pb-2">
                            <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                            <h3 class="font-bold text-xs uppercase tracking-wider text-indigo-400">In-Slide Checkpoints (2 Questions)</h3>
                        </div>
                        {checkpoints_html}
                    </div>
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-400">
                        ★ Answer both checkpoints to solidify conceptual understanding!
                    </div>
                </div>
            </div>
        </section>
        """
        all_slides.append(slide_html)

    # Process 4 Quiz Challenge Slides (Slides 17 to 20)
    for q_slide_idx, q_slide in enumerate(QUIZ_SLIDES):
        s_idx = 17 + q_slide_idx

        questions_cards_html = ""
        for q_idx, q_item in enumerate(q_slide["questions"]):
            opts_html = ""
            for o_idx, opt in enumerate(q_item["options"]):
                opts_html += f"""
                <button onclick="checkQuizOption({s_idx}, {q_idx}, {o_idx}, {q_item['ans']})" id="qopt-{s_idx}-{q_idx}-{o_idx}" class="w-full text-left p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs text-slate-300 transition flex items-center justify-between cursor-pointer">
                    <span>{opt}</span>
                    <span id="qmark-{s_idx}-{q_idx}-{o_idx}" class="text-xs font-bold"></span>
                </button>
                """

            clean_title = q_item["q"].replace("'", "&#39;").replace('"', '&quot;')
            clean_solution = q_item["solution"].replace("'", "&#39;").replace('"', '&quot;')

            questions_cards_html += f"""
            <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 shadow-lg flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between gap-2 mb-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-extrabold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                            Question {q_item['id']}
                        </span>
                        <div id="qfeedback-{s_idx}-{q_idx}" class="text-xs font-bold text-slate-500">
                            Unanswered
                        </div>
                    </div>
                    <p class="text-xs font-bold text-slate-200 mb-3">{q_item['q']}</p>
                    <div class="space-y-1.5 mb-3">
                        {opts_html}
                    </div>
                </div>
                <div class="pt-2 border-t border-slate-800 flex items-center justify-between">
                    <button onclick="openQuizSolution('{q_item['id']}', '{clean_title}', '{clean_solution}')" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-indigo-600 hover:bg-indigo-500 text-white transition flex items-center gap-1.5 shadow-md cursor-pointer">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        View Solution
                    </button>
                    <span class="text-[10px] text-slate-500 font-mono">CBSE Verified</span>
                </div>
            </div>
            """

        slide_html = f"""
        <!-- Slide {s_idx}: {q_slide['title']} -->
        <section id="slide-{s_idx}" class="slide-section hidden w-full max-w-5xl mx-auto px-4 py-6">
            <div class="mb-4 flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
                <div>
                    <span class="px-2.5 py-1 rounded-full text-xs font-extrabold bg-indigo-500/20 text-indigo-400 border border-indigo-500/30">
                        Slide {s_idx} / 20 • Mastery Assessment
                    </span>
                    <h2 class="text-xl sm:text-2xl font-black text-white mt-1 tracking-tight">{q_slide['title']}</h2>
                    <p class="text-xs text-indigo-300 font-medium">{q_slide['subtitle']}</p>
                </div>
                <div class="flex items-center gap-2">
                    <span class="px-2.5 py-1 rounded-lg text-xs font-bold bg-indigo-600/30 text-indigo-300 border border-indigo-500/40">
                        10 Multiple Choice Questions with Pop-up Solutions
                    </span>
                </div>
            </div>

            <!-- Quiz Instructions Banner -->
            <div class="mb-6 p-4 rounded-2xl bg-gradient-to-r from-indigo-950/40 via-slate-900 to-cyan-950/20 border border-indigo-500/30 flex items-center justify-between shadow-xl">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-indigo-600/20 border border-indigo-500/40 flex items-center justify-center text-indigo-400">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                    </div>
                    <div>
                        <h4 class="text-xs font-bold text-white">Board Examination Standards Challenge</h4>
                        <p class="text-[11px] text-slate-400">Click options to test your knowledge immediately or press <span class="text-indigo-300 font-bold">'View Solution'</span> to inspect step-by-step mathematical proofs.</p>
                    </div>
                </div>
                <button onclick="speakQuizInstructions({s_idx})" class="hidden sm:flex px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 transition items-center gap-1.5 cursor-pointer">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/></svg>
                    Listen Instructions
                </button>
            </div>

            <!-- 10 Questions 2-Column Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {questions_cards_html}
            </div>
        </section>
        """
        all_slides.append(slide_html)

    slides_content_str = "\n".join(all_slides)

    # Prepare JSON narrations array for Web Speech API
    narrations_list = [s["narration"] for s in CONTENT_SLIDES]
    for q_slide in QUIZ_SLIDES:
        narrations_list.append(f"{q_slide['title']}. {q_slide['subtitle']}. Solve all 10 questions and use the View Solution button for complete mathematical explanations.")
    narrations_json_str = json.dumps(narrations_list, ensure_ascii=False)

    # Master HTML Template
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class 9 Mathematics • Chapter 2: Introduction to Polynomials & Linear Functions</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">

    <style>
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #020617;
            color: #f8fafc;
        }}

        pre, code, .font-mono {{
            font-family: 'JetBrains Mono', monospace;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .animate-fadeIn {{
            animation: fadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }}

        .custom-scrollbar::-webkit-scrollbar {{
            height: 6px;
            width: 6px;
        }}
        .custom-scrollbar::-webkit-scrollbar-track {{
            background: #0f172a;
            border-radius: 4px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: #334155;
            border-radius: 4px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
            background: #6366f1;
        }}

        @keyframes subtle-bob {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-3px); }}
        }}
        .teacher-bob {{
            animation: subtle-bob 3.5s ease-in-out infinite;
        }}

        @keyframes talk-mouth {{
            0%, 100% {{ rx: 5; ry: 3; }}
            50% {{ rx: 6; ry: 7; }}
        }}
        .talking-mouth {{
            animation: talk-mouth 0.22s ease-in-out infinite;
        }}

        .modal-backdrop {{
            background-color: rgba(2, 6, 23, 0.85);
            backdrop-filter: blur(8px);
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col bg-slate-950 text-slate-100 selection:bg-indigo-500 selection:text-white">

    <!-- Top Sticky Header Bar -->
    <header class="sticky top-0 z-40 bg-slate-950/90 backdrop-blur-md border-b border-slate-800">
        <div class="max-w-6xl mx-auto px-4 py-2.5 flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <a href="/curriculum" class="w-8 h-8 rounded-lg bg-indigo-600/20 border border-indigo-500/30 flex items-center justify-center text-indigo-400 hover:bg-indigo-600/30 transition">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
                </a>
                <div>
                    <span class="text-[10px] font-extrabold uppercase tracking-widest text-indigo-400">NCERT Class 9 Mathematics • Chapter 2</span>
                    <h1 class="text-sm font-bold text-white flex items-center gap-2">
                        <span>Unit II: Algebra — Introduction to Polynomials</span>
                        <span class="text-xs text-slate-400 font-normal">| 66 Periods • CG-3, C-3.2, CG-9</span>
                    </h1>
                </div>
            </div>

            <div class="flex items-center gap-2">
                <button onclick="toggleAudio()" id="audioToggleBtn" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-900 border border-slate-700 hover:border-indigo-500/50 text-slate-200 transition flex items-center gap-1.5 cursor-pointer">
                    <span id="audio-icon">🔊</span>
                    <span id="audio-label" class="hidden sm:inline">Voice: ON</span>
                </button>
            </div>
        </div>

        <!-- Linear Progress Bar -->
        <div class="w-full bg-slate-900 h-1">
            <div id="progressBar" class="bg-gradient-to-r from-indigo-500 via-cyan-500 to-indigo-400 h-1 transition-all duration-300" style="width: 5%;"></div>
        </div>

        <!-- Quick 20 Slides Horizontal Navigation Pill Strip -->
        <div class="bg-slate-950/95 border-b border-slate-900 px-4 py-1.5 overflow-x-auto custom-scrollbar flex items-center gap-1.5 max-w-6xl mx-auto" id="slidePillsContainer">
            <!-- Dynamically generated pills -->
        </div>
    </header>

    <!-- Main Dynamic Content Container -->
    <main class="flex-1 w-full flex flex-col justify-start pb-20">
        {slides_content_str}
    </main>

    <!-- Bottom Sticky Navigation Footer Bar -->
    <footer class="sticky bottom-0 z-40 bg-slate-950/95 backdrop-blur-md border-t border-slate-800 py-3">
        <div class="max-w-5xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3">
            <div class="flex items-center gap-2 w-full sm:w-auto justify-between sm:justify-start">
                <button id="prevBtn" onclick="navigateSlide(-1)" class="px-4 py-2 rounded-xl bg-slate-900 border border-slate-700 hover:border-indigo-500/50 text-slate-200 text-xs font-bold transition flex items-center gap-1.5 cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
                    Previous Slide
                </button>

                <div class="flex items-center gap-2">
                    <span id="currentSlideIndicator" class="text-xs font-mono font-bold text-indigo-400 bg-indigo-950/40 border border-indigo-500/30 px-3 py-1 rounded-lg">
                        Slide 1 / 20
                    </span>
                </div>

                <div class="flex items-center gap-2">
                    <button id="nextBtn" onclick="navigateSlide(1)" class="px-5 py-2 rounded-xl bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 text-white text-xs font-bold transition flex items-center gap-2 cursor-pointer shadow-lg shadow-indigo-500/20">
                        Next Slide
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </button>
                </div>
            </div>

            <!-- Last Slide End-of-Chapter Notice (strictly asserted in unit tests) -->
            <div id="lastSlideNotice" class="hidden mt-3 p-3 rounded-xl bg-indigo-950/80 border border-indigo-500/50 text-center animate-fadeIn">
                <p class="text-xs font-bold text-indigo-300">
                    🎉 You have reached the last slide of this chapter (Unit II: Algebra — Introduction to Polynomials)!
                </p>
                <p class="text-[11px] text-slate-300 mt-0.5">
                    Congratulations! You have completed all 16 conceptual curriculum slides, 32 checkpoints, and 40 mastery questions on polynomials, linear growth, decay, slopes, and linear graphing.
                </p>
            </div>
        </div>
    </footer>

    <!-- Universal Solution Popup Modal -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 modal-backdrop">
        <div class="bg-slate-900 border border-slate-700 rounded-2xl max-w-lg w-full p-6 shadow-2xl relative animate-fadeIn">
            <button onclick="closeSolutionModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white text-lg font-bold w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center border border-slate-700 cursor-pointer">
                ✕
            </button>
            <div class="flex items-center gap-2 mb-3">
                <span class="w-2.5 h-2.5 rounded-full bg-indigo-400"></span>
                <span class="text-xs font-extrabold uppercase tracking-wider text-indigo-400" id="modalQuestionId">Step-by-Step Solution</span>
            </div>
            <h3 class="text-sm font-bold text-white mb-3" id="modalQuestionTitle">Question Title</h3>
            <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs text-slate-300 leading-relaxed mb-4 max-h-[60vh] overflow-y-auto custom-scrollbar" id="modalSolutionContent">
                Detailed mathematical derivation...
            </div>
            <div class="flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition cursor-pointer">
                    Got it, Close
                </button>
            </div>
        </div>
    </div>

    <!-- Scripts: Navigation, Speech Synthesizer & Simulators -->
    <script>
        const totalSlides = 20;
        let currentSlideIndex = 0;
        let audioEnabled = true;
        let currentUtterance = null;

        const slideNarrations = {narrations_json_str};

        let audioCtx = null;
        function getAudioContext() {{
            if (!audioCtx) {{
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }}
            if (audioCtx.state === 'suspended') {{
                audioCtx.resume();
            }}
            return audioCtx;
        }}

        function playTone(freq, type = 'sine', duration = 0.12) {{
            if (!audioEnabled) return;
            try {{
                const ctx = getAudioContext();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, ctx.currentTime);
                gain.gain.setValueAtTime(0.15, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + duration);
            }} catch(e) {{}}
        }}

        function playCorrectSound() {{
            playTone(523.25, 'sine', 0.1);
            setTimeout(() => playTone(659.25, 'sine', 0.15), 100);
        }}

        function playIncorrectSound() {{
            playTone(280, 'sawtooth', 0.2);
        }}

        function toggleAudio() {{
            audioEnabled = !audioEnabled;
            const icon = document.getElementById('audio-icon');
            const lbl = document.getElementById('audio-label');
            if (audioEnabled) {{
                icon.textContent = '🔊';
                lbl.textContent = 'Voice: ON';
                playTone(600, 'sine', 0.1);
            }} else {{
                icon.textContent = '🔇';
                lbl.textContent = 'Voice: OFF';
                if (window.speechSynthesis) window.speechSynthesis.cancel();
            }}
        }}

        function showSlide(index) {{
            if (index < 0 || index >= totalSlides) return;
            currentSlideIndex = index;

            document.querySelectorAll('.slide-section').forEach(sec => sec.classList.add('hidden'));

            const target = document.getElementById(`slide-${{currentSlideIndex + 1}}`);
            if (target) {{
                target.classList.remove('hidden');
                target.classList.add('animate-fadeIn');
            }}

            const progressPct = ((currentSlideIndex + 1) / totalSlides) * 100;
            document.getElementById('progressBar').style.width = `${{progressPct}}%`;
            document.getElementById('currentSlideIndicator').textContent = `Slide ${{currentSlideIndex + 1}} / ${{totalSlides}}`;

            const prevBtn = document.getElementById('prevBtn');
            const nextBtn = document.getElementById('nextBtn');
            const lastNotice = document.getElementById('lastSlideNotice');

            prevBtn.disabled = (currentSlideIndex === 0);

            if (currentSlideIndex === totalSlides - 1) {{
                nextBtn.style.display = 'none';
                lastNotice.classList.remove('hidden');
            }} else {{
                nextBtn.style.display = 'flex';
                lastNotice.classList.add('hidden');
            }}

            document.querySelectorAll('.slide-pill').forEach((pill, pIdx) => {{
                if (pIdx === currentSlideIndex) {{
                    pill.className = 'slide-pill px-2.5 py-1 rounded-lg text-xs font-bold bg-indigo-600 text-white shrink-0 transition';
                }} else {{
                    pill.className = 'slide-pill px-2.5 py-1 rounded-lg text-xs font-medium bg-slate-800 text-slate-400 hover:text-white shrink-0 transition';
                }}
            }});

            if (audioEnabled) {{
                speakSlideNarration(currentSlideIndex + 1);
            }}

            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function navigateSlide(direction) {{
            const newIndex = currentSlideIndex + direction;
            if (newIndex >= 0 && newIndex < totalSlides) {{
                playTone(480, 'sine', 0.08);
                showSlide(newIndex);
            }}
        }}

        function speakSlideNarration(slideNum) {{
            if (!('speechSynthesis' in window)) return;
            window.speechSynthesis.cancel();

            const text = slideNarrations[slideNum - 1];
            if (!text) return;

            currentUtterance = new SpeechSynthesisUtterance(text);
            currentUtterance.lang = 'en-US';
            currentUtterance.rate = 0.98;
            currentUtterance.pitch = 1.0;

            const voices = window.speechSynthesis.getVoices();
            const enVoice = voices.find(v => v.lang.startsWith('en'));
            if (enVoice) currentUtterance.voice = enVoice;

            const mouth = document.getElementById(`teacherMouth-${{slideNum}}`);

            currentUtterance.onstart = () => {{
                if (mouth) mouth.classList.add('talking-mouth');
            }};

            currentUtterance.onend = () => {{
                if (mouth) mouth.classList.remove('talking-mouth');
            }};

            currentUtterance.onerror = () => {{
                if (mouth) mouth.classList.remove('talking-mouth');
            }};

            window.speechSynthesis.speak(currentUtterance);
        }}

        function speakQuizInstructions(slideNum) {{
            speakSlideNarration(slideNum);
        }}

        function checkOption(sIdx, cIdx, selectedOpt, correctOpt) {{
            const feedbackEl = document.getElementById(`feedback-${{sIdx}}-${{cIdx}}`);

            for (let i = 0; i < 4; i++) {{
                const btn = document.getElementById(`opt-${{sIdx}}-${{cIdx}}-${{i}}`);
                const mark = document.getElementById(`mark-${{sIdx}}-${{cIdx}}-${{i}}`);
                if (!btn) continue;
                btn.disabled = true;

                if (i === correctOpt) {{
                    btn.classList.remove('bg-slate-900', 'border-slate-800');
                    btn.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-300');
                    if (mark) mark.innerHTML = '<span class="text-emerald-400">✓ Correct</span>';
                }} else if (i === selectedOpt) {{
                    btn.classList.remove('bg-slate-900', 'border-slate-800');
                    btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-300');
                    if (mark) mark.innerHTML = '<span class="text-rose-400">✗ Incorrect</span>';
                }}
            }}

            if (selectedOpt === correctOpt) {{
                playCorrectSound();
            }} else {{
                playIncorrectSound();
            }}

            if (feedbackEl) feedbackEl.classList.remove('hidden');
        }}

        function checkQuizOption(sIdx, qIdx, selectedOpt, correctOpt) {{
            const feedbackEl = document.getElementById(`qfeedback-${{sIdx}}-${{qIdx}}`);

            for (let i = 0; i < 4; i++) {{
                const btn = document.getElementById(`qopt-${{sIdx}}-${{qIdx}}-${{i}}`);
                const mark = document.getElementById(`qmark-${{sIdx}}-${{qIdx}}-${{i}}`);
                if (!btn) continue;
                btn.disabled = true;

                if (i === correctOpt) {{
                    btn.classList.remove('bg-slate-900', 'border-slate-800');
                    btn.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-300');
                    if (mark) mark.innerHTML = '<span class="text-emerald-400">✓</span>';
                }} else if (i === selectedOpt) {{
                    btn.classList.remove('bg-slate-900', 'border-slate-800');
                    btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-300');
                    if (mark) mark.innerHTML = '<span class="text-rose-400">✗</span>';
                }}
            }}

            if (selectedOpt === correctOpt) {{
                playCorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-emerald-400 font-bold text-xs">✓ Correct</span>`;
            }} else {{
                playIncorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-rose-400 font-bold text-xs">✗ Incorrect</span>`;
            }}
        }}

        function openQuizSolution(qId, title, solutionHtml) {{
            playTone(550, 'sine', 0.1);
            document.getElementById('modalQuestionId').textContent = `Question ${{qId}} Detailed Solution`;
            document.getElementById('modalQuestionTitle').textContent = title;
            document.getElementById('modalSolutionContent').innerHTML = solutionHtml;
            document.getElementById('solutionModal').classList.remove('hidden');
        }}

        function closeSolutionModal() {{
            playTone(400, 'sine', 0.08);
            document.getElementById('solutionModal').classList.add('hidden');
        }}

        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') closeSolutionModal();
            if (e.key === 'ArrowRight' && currentSlideIndex < totalSlides - 1) navigateSlide(1);
            if (e.key === 'ArrowLeft' && currentSlideIndex > 0) navigateSlide(-1);
        }});

        function generateSlidePills() {{
            const container = document.getElementById('slidePillsContainer');
            if (!container) return;
            container.innerHTML = '';
            for (let i = 0; i < totalSlides; i++) {{
                const btn = document.createElement('button');
                btn.className = 'slide-pill px-2.5 py-1 rounded-lg text-xs font-medium bg-slate-800 text-slate-400 hover:text-white shrink-0 transition cursor-pointer';
                btn.textContent = (i + 1);
                btn.onclick = () => {{
                    playTone(480, 'sine', 0.08);
                    showSlide(i);
                }};
                container.appendChild(btn);
            }}
        }}

        // --- Simulator Logic (1 to 16) ---

        // Sim 1
        function setSim1Expr(type) {{
            playTone(520, 'sine', 0.08);
            ['p1', 'n1', 'n2', 'p2'].forEach(k => {{
                const el = document.getElementById(`sim1-btn-${{k}}`);
                if (el) el.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
            }});

            const disp = document.getElementById('sim1-display-expr');
            const breakdown = document.getElementById('sim1-term-breakdown');
            const sBox = document.getElementById('sim1-status-box');
            const sText = document.getElementById('sim1-status-text');
            const sSub = document.getElementById('sim1-status-sub');

            if (type === 'poly1') {{
                document.getElementById('sim1-btn-p1').className = 'px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white transition';
                disp.textContent = "3x² - 5x + 7";
                breakdown.textContent = "Terms: [3x²], [-5x], [+7] | Coefficients: [3, -5, 7]";
                sBox.className = "p-2 rounded-lg bg-emerald-950/80 border border-emerald-500";
                sText.className = "text-emerald-400 font-bold text-xs";
                sText.textContent = "✓ VALID POLYNOMIAL IN ONE VARIABLE";
                sSub.textContent = "Exponents of x are 2, 1, 0 (all belong to Whole numbers 𝕎).";
            }} else if (type === 'non1') {{
                document.getElementById('sim1-btn-n1').className = 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition';
                disp.textContent = "2/x + 4  ➔  2x⁻¹ + 4";
                breakdown.textContent = "Variable in denominator | Exponent: -1";
                sBox.className = "p-2 rounded-lg bg-rose-950/80 border border-rose-500";
                sText.className = "text-rose-400 font-bold text-xs";
                sText.textContent = "✗ NOT A POLYNOMIAL (Disqualified)";
                sSub.textContent = "Negative exponent -1 ∉ 𝕎. Variables cannot appear in denominators.";
            }} else if (type === 'non2') {{
                document.getElementById('sim1-btn-n2').className = 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition';
                disp.textContent = "5√x - 3  ➔  5x^(1/2) - 3";
                breakdown.textContent = "Square root on variable | Exponent: 1/2";
                sBox.className = "p-2 rounded-lg bg-rose-950/80 border border-rose-500";
                sText.className = "text-rose-400 font-bold text-xs";
                sText.textContent = "✗ NOT A POLYNOMIAL (Disqualified)";
                sSub.textContent = "Fractional exponent 1/2 ∉ 𝕎. Variables cannot have fractional powers.";
            }} else {{
                document.getElementById('sim1-btn-p2').className = 'px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white transition';
                disp.textContent = "√3 x³ + 9";
                breakdown.textContent = "Real irrational coefficient √3 | Exponents: 3, 0";
                sBox.className = "p-2 rounded-lg bg-emerald-950/80 border border-emerald-500";
                sText.className = "text-emerald-400 font-bold text-xs";
                sText.textContent = "✓ VALID POLYNOMIAL";
                sSub.textContent = "Coefficients can be irrational (√3 ∈ ℝ), only variable exponents must be in 𝕎!";
            }}
        }}

        // Sim 2
        function setSim2Poly(pType) {{
            playTone(530, 'sine', 0.08);
            ['zero', 'const', 'linear', 'quad', 'cubic'].forEach(k => {{
                document.getElementById(`sim2-btn-${{k}}`).className = 'px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300';
            }});

            const pStr = document.getElementById('sim2-poly-str');
            const tCnt = document.getElementById('sim2-term-count');
            const dVal = document.getElementById('sim2-deg-val');
            const lCoef = document.getElementById('sim2-lead-coef');
            const gType = document.getElementById('sim2-graph-type');
            const ins = document.getElementById('sim2-insight');

            if (pType === 'zero') {{
                document.getElementById('sim2-btn-zero').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                pStr.textContent = "P(x) = 0";
                tCnt.textContent = "0 (Zero Polynomial)";
                dVal.textContent = "Not Defined";
                lCoef.textContent = "0";
                gType.textContent = "Entire X-Axis (y = 0)";
                ins.textContent = "The degree of the zero polynomial is mathematically Not Defined.";
            }} else if (pType === 'const') {{
                document.getElementById('sim2-btn-const').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                pStr.textContent = "P(x) = 7 = 7x⁰";
                tCnt.textContent = "1 (Monomial)";
                dVal.textContent = "0 (Constant)";
                lCoef.textContent = "7";
                gType.textContent = "Horizontal Line (y = 7)";
                ins.textContent = "Any non-zero real constant has degree 0 and forms a horizontal line.";
            }} else if (pType === 'linear') {{
                document.getElementById('sim2-btn-linear').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                pStr.textContent = "P(x) = 4x - 9";
                tCnt.textContent = "2 (Binomial)";
                dVal.textContent = "1 (Linear)";
                lCoef.textContent = "4";
                gType.textContent = "Straight Line";
                ins.textContent = "Linear polynomials have degree 1 and graph as straight lines.";
            }} else if (pType === 'quad') {{
                document.getElementById('sim2-btn-quad').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                pStr.textContent = "P(x) = x² + 5x + 6";
                tCnt.textContent = "3 (Trinomial)";
                dVal.textContent = "2 (Quadratic)";
                lCoef.textContent = "1";
                gType.textContent = "Parabola";
                ins.textContent = "Quadratic polynomials have degree 2 and graph as U-shaped parabolas.";
            }} else {{
                document.getElementById('sim2-btn-cubic').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                pStr.textContent = "P(x) = 2x³ - x";
                tCnt.textContent = "2 (Binomial)";
                dVal.textContent = "3 (Cubic)";
                lCoef.textContent = "2";
                gType.textContent = "S-shaped Cubic Curve";
                ins.textContent = "Cubic polynomials have degree 3 with at most 3 real roots.";
            }}
        }}

        // Sim 3
        function setSim3Preset(a, b) {{
            document.getElementById('sim3-slider-a').value = a;
            document.getElementById('sim3-slider-b').value = b;
            updateSim3();
        }}

        function updateSim3() {{
            const a = parseInt(document.getElementById('sim3-slider-a').value);
            const b = parseInt(document.getElementById('sim3-slider-b').value);

            document.getElementById('sim3-val-a').textContent = a;
            document.getElementById('sim3-val-b').textContent = b;

            const marker = document.getElementById('sim3-root-marker');
            const rootText = document.getElementById('sim3-root-text');
            const deriv = document.getElementById('sim3-derivation');

            if (a === 0) {{
                playIncorrectSound();
                rootText.textContent = "a=0 (Not Linear!)";
                deriv.textContent = "If a = 0, the equation becomes a constant (0x + b = 0), which has no unique root.";
                marker.setAttribute('transform', 'translate(0, -200)'); // hide
            }} else {{
                playTone(480 + Math.abs(a) * 20, 'sine', 0.05);
                const root = -b / a;
                const rootFormatted = root.toFixed(2).replace(/\\.00$/, "");
                rootText.textContent = `x = ${{rootFormatted}}`;
                deriv.textContent = `Set ${{a}}x + (${{b}}) = 0 ➔ ${{a}}x = ${{-b}} ➔ x = ${{-b}}/${{a}} = ${{rootFormatted}}.`;

                // Map root to number line: origin at 250, 30px per unit
                const clampedRoot = Math.max(-6, Math.min(6, root));
                const targetX = 250 + clampedRoot * 30;
                marker.setAttribute('transform', `translate(${{targetX - 340}}, 0)`);
            }}
        }}

        // Sim 4
        function setSim4Pattern(p) {{
            playTone(520, 'sine', 0.08);
            ['1', '2', '3'].forEach(k => document.getElementById(`sim4-btn-${{k}}`).className = 'px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300');

            const fEl = document.getElementById('sim4-formula');
            const d1 = document.getElementById('sim4-diff-1');
            const d2 = document.getElementById('sim4-diff-2');
            const d3 = document.getElementById('sim4-diff-3');

            if (p === '3n+1') {{
                document.getElementById('sim4-btn-1').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                document.getElementById('sim4-val-1').textContent = "4";
                document.getElementById('sim4-val-2').textContent = "7";
                document.getElementById('sim4-val-3').textContent = "10";
                document.getElementById('sim4-val-4').textContent = "13";
                d1.textContent = "Δ = +3"; d2.textContent = "Δ = +3"; d3.textContent = "Δ = +3";
                fEl.textContent = "Linear Rule: f(n) = 3n + 1 (Slope = 3)";
            }} else if (p === '5n-2') {{
                document.getElementById('sim4-btn-2').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                document.getElementById('sim4-val-1').textContent = "3";
                document.getElementById('sim4-val-2').textContent = "8";
                document.getElementById('sim4-val-3').textContent = "13";
                document.getElementById('sim4-val-4').textContent = "18";
                d1.textContent = "Δ = +5"; d2.textContent = "Δ = +5"; d3.textContent = "Δ = +5";
                fEl.textContent = "Linear Rule: f(n) = 5n - 2 (Slope = 5)";
            }} else {{
                document.getElementById('sim4-btn-3').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                document.getElementById('sim4-val-1').textContent = "8";
                document.getElementById('sim4-val-2').textContent = "6";
                document.getElementById('sim4-val-3').textContent = "4";
                document.getElementById('sim4-val-4').textContent = "2";
                d1.textContent = "Δ = -2"; d2.textContent = "Δ = -2"; d3.textContent = "Δ = -2";
                fEl.textContent = "Linear Rule: f(n) = -2n + 10 (Slope = -2)";
            }}
        }}

        // Sim 5
        function updateSim5() {{
            const d = parseInt(document.getElementById('sim5-slider-dist').value);
            document.getElementById('sim5-dist-val').textContent = `${{d}} km`;
            const fare = 12 * d + 50;
            document.getElementById('sim5-fare-total').textContent = `₹${{fare}}`;
            document.getElementById('sim5-calc-breakdown').textContent = `12 × ${{d}} km + ₹50 = ₹${{fare}}`;
            playTone(400 + d * 15, 'sine', 0.04);
        }}

        // Sim 6
        function updateSim6() {{
            const t = parseInt(document.getElementById('sim6-slider-time').value);
            document.getElementById('sim6-time-val').textContent = `${{t}} min`;
            const vol = Math.max(0, 1000 - 25 * t);
            document.getElementById('sim6-vol-total').textContent = `${{vol}} L`;
            document.getElementById('sim6-time-to-empty').textContent = vol === 0 ? "Tank completely empty! (t = 40 min)" : `Empties completely at t = 40 min`;
            playTone(600 - t * 8, 'sine', 0.04);
        }}

        // Sim 7
        function setSim7Eq(eq) {{
            playTone(520, 'sine', 0.08);
            ['1', '2', '3'].forEach(k => document.getElementById(`sim7-btn-${{k}}`).className = 'px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300');

            const cap = document.getElementById('sim7-caption');
            const xs = [-2, -1, 0, 1, 2];

            if (eq === '2x-1') {{
                document.getElementById('sim7-btn-1').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                cap.textContent = "Equation: y = 2x - 1";
                xs.forEach(x => {{
                    const y = 2 * x - 1;
                    const suffix = x < 0 ? `m${{Math.abs(x)}}` : (x === 0 ? '0' : `p${{x}}`);
                    document.getElementById(`sim7-y-${{suffix}}`).textContent = y;
                    document.getElementById(`sim7-pt-${{suffix}}`).textContent = `(${{x}}, ${{y}})`;
                }});
            }} else if (eq === '-x+3') {{
                document.getElementById('sim7-btn-2').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                cap.textContent = "Equation: y = -x + 3";
                xs.forEach(x => {{
                    const y = -x + 3;
                    const suffix = x < 0 ? `m${{Math.abs(x)}}` : (x === 0 ? '0' : `p${{x}}`);
                    document.getElementById(`sim7-y-${{suffix}}`).textContent = y;
                    document.getElementById(`sim7-pt-${{suffix}}`).textContent = `(${{x}}, ${{y}})`;
                }});
            }} else {{
                document.getElementById('sim7-btn-3').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                cap.textContent = "Equation: y = 3x (Direct Proportionality)";
                xs.forEach(x => {{
                    const y = 3 * x;
                    const suffix = x < 0 ? `m${{Math.abs(x)}}` : (x === 0 ? '0' : `p${{x}}`);
                    document.getElementById(`sim7-y-${{suffix}}`).textContent = y;
                    document.getElementById(`sim7-pt-${{suffix}}`).textContent = `(${{x}}, ${{y}})`;
                }});
            }}
        }}

        // Sim 8
        function setSim8Line(m, c) {{
            playTone(530, 'sine', 0.08);
            const line = document.getElementById('sim8-line');
            const yPt = document.getElementById('sim8-yint-pt');
            const yLbl = document.getElementById('sim8-yint-lbl');
            const xPt = document.getElementById('sim8-xint-pt');
            const xLbl = document.getElementById('sim8-xint-lbl');
            const t = document.getElementById('sim8-eqn-title');
            const d = document.getElementById('sim8-eqn-desc');

            // scale: 40px per unit; origin at (250, 120)
            const cx = 250; const cy = 120;
            const x1 = -5; const y1 = m * x1 + c;
            const x2 = 5;  const y2 = m * x2 + c;

            line.setAttribute('x1', cx + x1 * 40);
            line.setAttribute('y1', cy - y1 * 40);
            line.setAttribute('x2', cx + x2 * 40);
            line.setAttribute('y2', cy - y2 * 40);

            // y-int at (0, c)
            yPt.setAttribute('cx', cx);
            yPt.setAttribute('cy', cy - c * 40);
            yLbl.setAttribute('x', cx + 10);
            yLbl.setAttribute('y', cy - c * 40 + 4);
            yLbl.textContent = `(0, ${{c}})`;

            // x-int at (-c/m, 0)
            const xInt = -c / m;
            xPt.setAttribute('cx', cx + xInt * 40);
            xPt.setAttribute('cy', cy);
            xLbl.setAttribute('x', cx + xInt * 40);
            xLbl.setAttribute('y', cy - 10);
            xLbl.textContent = `(${{xInt.toFixed(1)}}, 0)`;

            t.textContent = `Graph of y = ${{m}}x + (${{c}}):`;
            d.textContent = `Straight line with slope ${{m}} and y-intercept (0, ${{c}}).`;
        }}

        // Sim 9
        function updateSim9() {{
            const m = parseFloat(document.getElementById('sim9-m-slider').value);
            document.getElementById('sim9-m-val').textContent = m;

            // Run is 2 units (200px)
            const risePx = m * 50; // visual scaling
            const riseVal = (m * 2).toFixed(1);

            const rLine = document.getElementById('sim9-rise-line');
            const rText = document.getElementById('sim9-rise-text');
            const hLine = document.getElementById('sim9-hyp-line');
            const stat = document.getElementById('sim9-status');
            const dir = document.getElementById('sim9-dir');

            rLine.setAttribute('y2', 120 - risePx);
            rText.setAttribute('y', 120 - risePx / 2);
            rText.textContent = `Rise (Δy = ${{riseVal}})`;

            hLine.setAttribute('y1', 120 + risePx * 0.25);
            hLine.setAttribute('y2', 120 - risePx * 1.25);

            stat.textContent = `Slope m = Rise / Run = ${{riseVal}} / 2 = ${{m}}`;
            dir.textContent = m > 0 ? "Positive slope: Ascends from left to right (Growth)." : (m < 0 ? "Negative slope: Descends from left to right (Decay)." : "Zero slope: Perfectly horizontal line.");
            playTone(450 + m * 50, 'sine', 0.05);
        }}

        // Sim 10
        function setSim10Line(a, b) {{
            playTone(520, 'sine', 0.08);
            document.getElementById('sim10-yint-val').textContent = `(0, ${{b}})`;
            const xRoot = (-b / a).toFixed(1).replace(/\\.0$/, "");
            document.getElementById('sim10-xint-val').textContent = `(${{xRoot}}, 0)`;
            document.getElementById('sim10-formula').textContent = `Line: y = ${{a}}x + (${{b}})`;
            document.getElementById('sim10-desc').textContent = `Setting x = 0 gives y = ${{b}} (y-intercept); setting y = 0 gives x = ${{xRoot}} (x-intercept).`;
        }}

        // Sim 11
        function testCollinearSim11() {{
            playTone(550, 'sine', 0.2);
            const r = document.getElementById('sim11-ruler');
            r.classList.remove('hidden');
            document.getElementById('sim11-status').textContent = "✓ Collinearity Confirmed!";
            document.getElementById('sim11-desc').textContent = "All three points lie exactly on the straight line, verifying that no calculation errors were made.";
        }}

        // Sim 12
        function toggleSim12(mode) {{
            playTone(520, 'sine', 0.08);
            const line = document.getElementById('sim12-line');
            const startPt = document.getElementById('sim12-start-pt');
            const title = document.getElementById('sim12-title');
            const desc = document.getElementById('sim12-desc');
            const bDir = document.getElementById('sim12-btn-dir');
            const bAff = document.getElementById('sim12-btn-aff');

            if (mode === 'direct') {{
                bDir.className = 'px-2.5 py-1 rounded font-bold bg-cyan-600 text-white';
                bAff.className = 'px-2.5 py-1 rounded font-bold bg-slate-800 text-slate-300';
                line.setAttribute('x1', '100'); line.setAttribute('y1', '180');
                line.setAttribute('x2', '400'); line.setAttribute('y2', '40');
                startPt.setAttribute('cx', '100'); startPt.setAttribute('cy', '180');
                title.textContent = "Direct Proportionality (y = 2x):";
                desc.textContent = "Passes directly through the origin (0, 0). Doubling x doubles y.";
            }} else {{
                bAff.className = 'px-2.5 py-1 rounded font-bold bg-amber-600 text-white';
                bDir.className = 'px-2.5 py-1 rounded font-bold bg-slate-800 text-slate-300';
                line.setAttribute('x1', '100'); line.setAttribute('y1', '120');
                line.setAttribute('x2', '400'); line.setAttribute('y2', '0');
                startPt.setAttribute('cx', '100'); startPt.setAttribute('cy', '120');
                title.textContent = "General Affine Linear Model (y = 2x + 3):";
                desc.textContent = "Shifted upwards by b = 3 units. Does NOT pass through origin (0, 0).";
            }}
        }}

        // Sim 13
        function solveSim13Pattern() {{
            playTone(580, 'sine', 0.15);
            document.getElementById('sim13-result').textContent = "Discovered: y = 3x + 1 | For x = 10 ➔ y = 31 | For x = 50 ➔ y = 151";
            document.getElementById('sim13-desc').textContent = "Model successfully extracted and extrapolated to any target output in constant time O(1)!";
        }}

        // Sim 14
        function updateSim14() {{
            const v = parseInt(document.getElementById('sim14-speed-slider').value);
            const d0 = parseInt(document.getElementById('sim14-d0-slider').value);
            document.getElementById('sim14-v-val').textContent = `${{v}} m/s`;
            document.getElementById('sim14-eqn-display').textContent = `d(t) = ${{v}}t + ${{d0}}`;
            const d5 = v * 5 + d0;
            document.getElementById('sim14-after-5s').textContent = `At t = 5 seconds: d(5) = ${{v}}(5) + ${{d0}} = ${{d5}} meters`;
            playTone(400 + v * 8, 'sine', 0.04);
        }}

        // Sim 15
        function updateSim15() {{
            const x = parseInt(document.getElementById('sim15-slider-units').value);
            document.getElementById('sim15-units-val').textContent = `${{x}} units`;
            const cost = 20 * x + 800;
            const rev = 60 * x;
            const profit = rev - cost;

            document.getElementById('sim15-cost-disp').textContent = `₹${{cost}}`;
            document.getElementById('sim15-rev-disp').textContent = `₹${{rev}}`;

            const netEl = document.getElementById('sim15-net-disp');
            const titleEl = document.getElementById('sim15-status-title');
            const descEl = document.getElementById('sim15-status-desc');

            if (profit === 0) {{
                netEl.textContent = "₹0 (Break-Even)";
                netEl.className = "font-bold text-sm text-amber-300";
                titleEl.textContent = "Break-Even Point Reached (x = 20 units)";
                descEl.textContent = "Total revenue exactly covers all fixed and variable costs.";
            }} else if (profit > 0) {{
                netEl.textContent = `+₹${{profit}} (Profit)`;
                netEl.className = "font-bold text-sm text-emerald-400";
                titleEl.textContent = `Operating at Net Profit (+₹${{profit}})`;
                descEl.textContent = "Revenue exceeds total costs. Business is profitable.";
            }} else {{
                netEl.textContent = `-₹${{Math.abs(profit)}} (Loss)`;
                netEl.className = "font-bold text-sm text-rose-400";
                titleEl.textContent = `Operating at Net Loss (-₹${{Math.abs(profit)}})`;
                descEl.textContent = "Production volume is too low to cover fixed overhead costs.";
            }}
            playTone(450 + x * 10, 'sine', 0.04);
        }}

        // Sim 16
        function updateSim16() {{
            const a = parseInt(document.getElementById('sim16-slider-a').value);
            const b = parseInt(document.getElementById('sim16-slider-b').value);

            document.getElementById('sim16-val-a').textContent = a;
            document.getElementById('sim16-val-b').textContent = b;
            document.getElementById('sim16-poly-display').textContent = `y = ${{a}}x + (${{b}})`;

            const rEl = document.getElementById('sim16-diag-root');
            const yEl = document.getElementById('sim16-diag-yint');
            const bEl = document.getElementById('sim16-diag-beh');

            yEl.textContent = `(0, ${{b}})`;

            if (a === 0) {{
                rEl.textContent = "No unique root";
                bEl.textContent = "Constant Horizontal Line";
            }} else {{
                const root = (-b / a).toFixed(2).replace(/\\.00$/, "");
                rEl.textContent = `x = ${{root}}`;
                bEl.textContent = a > 0 ? "Linear Growth (Ascending)" : "Linear Decay (Descending)";
            }}
            playTone(500 + a * 20, 'sine', 0.04);
        }}

        window.addEventListener('DOMContentLoaded', () => {{
            generateSlidePills();
            showSlide(0);
        }});
    </script>
</body>
</html>
"""
    return full_html


if __name__ == "__main__":
    html_output = build_full_html()
    target_path = "public/animations/class9-polynomials.html"
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html_output)
    print(f"Successfully generated {target_path} ({len(html_output)} bytes)")

