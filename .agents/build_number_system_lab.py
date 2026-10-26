# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 1: Number System
Unit 1: Number System (12 Periods, Competencies CG-1, C-1.1, CG-9)
Generates public/animations/number-system.html with:
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
from number_system_data import CONTENT_SLIDES, QUIZ_SLIDES


def generate_interactive_simulator(s_idx):
    """Returns bespoke interactive SVG simulator HTML for each content slide (1-16)."""
    if s_idx == 1:
        # Simulator 1: Number Universe Nested Sets Explorer
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.1: Number Universe Nested Sets Explorer</span>
                </div>
                <div class="flex flex-wrap items-center gap-1.5">
                    <button onclick="setSim1Set('N')" id="sim1-btn-N" class="px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition">Natural (ℕ)</button>
                    <button onclick="setSim1Set('W')" id="sim1-btn-W" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Whole (𝕎)</button>
                    <button onclick="setSim1Set('Z')" id="sim1-btn-Z" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Integers (ℤ)</button>
                    <button onclick="setSim1Set('Q')" id="sim1-btn-Q" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Rational (ℚ)</button>
                    <button onclick="setSim1Set('I')" id="sim1-btn-I" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Irrational (𝕀)</button>
                    <button onclick="setSim1Set('R')" id="sim1-btn-R" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Real (ℝ)</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <svg id="sim1-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Real Numbers Outer Boundary -->
                    <rect id="sim1-rect-R" x="15" y="15" width="470" height="210" rx="20" fill="#0f172a" stroke="#6366f1" stroke-width="2.5" opacity="0.6"/>
                    <text x="35" y="40" fill="#818cf8" font-size="12" font-weight="bold">Real Numbers (ℝ)</text>

                    <!-- Left: Nested Rational Numbers Group -->
                    <rect id="sim1-rect-Q" x="35" y="55" width="300" height="155" rx="15" fill="#1e293b" stroke="#38bdf8" stroke-width="2" opacity="0.7"/>
                    <text x="50" y="78" fill="#38bdf8" font-size="11" font-weight="bold">Rational Numbers (ℚ)</text>
                    <text x="270" y="78" fill="#94a3b8" font-size="9">1/2, -3/4, 0.75, 0.333...</text>

                    <!-- Integers (Z) -->
                    <rect id="sim1-rect-Z" x="50" y="90" width="220" height="105" rx="12" fill="#0c4a6e" stroke="#0ea5e9" stroke-width="2" opacity="0.8"/>
                    <text x="65" y="112" fill="#7dd3fc" font-size="10" font-weight="bold">Integers (ℤ)</text>
                    <text x="210" y="112" fill="#bae6fd" font-size="9">-5, -2, -1</text>

                    <!-- Whole Numbers (W) -->
                    <rect id="sim1-rect-W" x="65" y="122" width="150" height="63" rx="10" fill="#065f46" stroke="#10b981" stroke-width="2" opacity="0.9"/>
                    <text x="75" y="142" fill="#6ee7b7" font-size="10" font-weight="bold">Whole (𝕎)</text>
                    <text x="175" y="142" fill="#a7f3d0" font-size="9">0</text>

                    <!-- Natural Numbers (N) -->
                    <rect id="sim1-rect-N" x="80" y="150" width="90" height="28" rx="6" fill="#b45309" stroke="#f59e0b" stroke-width="2"/>
                    <text x="125" y="168" fill="#fef08a" font-size="10" font-weight="black" text-anchor="middle">Natural ℕ {1, 2, 3..}</text>

                    <!-- Right: Disjoint Irrational Numbers Box -->
                    <rect id="sim1-rect-I" x="350" y="55" width="120" height="155" rx="15" fill="#4c0519" stroke="#f43f5e" stroke-width="2" opacity="0.7"/>
                    <text x="410" y="80" fill="#fda4af" font-size="11" font-weight="bold" text-anchor="middle">Irrational (𝕀)</text>
                    <text x="410" y="110" fill="#fecdd3" font-size="10" font-weight="bold" text-anchor="middle">√2 ≈ 1.414...</text>
                    <text x="410" y="135" fill="#fecdd3" font-size="10" font-weight="bold" text-anchor="middle">√3 ≈ 1.732...</text>
                    <text x="410" y="160" fill="#fecdd3" font-size="10" font-weight="bold" text-anchor="middle">π ≈ 3.1415...</text>
                    <text x="410" y="185" fill="#fecdd3" font-size="9" text-anchor="middle">0.1010010001...</text>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim1-info-title">Natural Numbers (ℕ):</span>
                    <span id="sim1-info-desc">Counting numbers {1, 2, 3, 4, ...}. They are the core inner subset of all whole numbers, integers, rational numbers, and real numbers: ℕ ⊂ 𝕎 ⊂ ℤ ⊂ ℚ ⊂ ℝ.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 2:
        # Simulator 2: Dynamic Rational Number Builder (p/q)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.2: Dynamic Rational Fraction Engine ($p/q$)</span>
                </div>
                <div class="flex items-center gap-2 text-xs">
                    <button onclick="setSim2Preset(3, 4)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 hover:bg-slate-700">3/4</button>
                    <button onclick="setSim2Preset(-5, 2)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 hover:bg-slate-700">-5/2</button>
                    <button onclick="setSim2Preset(0, 5)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 hover:bg-slate-700">0/5</button>
                    <button onclick="setSim2Preset(4, 0)" class="px-2 py-0.5 rounded bg-rose-900/50 text-rose-300 border border-rose-500/30 hover:bg-rose-800">4/0 (Error!)</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
                    <!-- Controls -->
                    <div class="space-y-3 bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                        <div>
                            <div class="flex justify-between text-xs font-bold mb-1">
                                <span class="text-amber-400">Numerator ($p$):</span>
                                <span id="sim2-val-p" class="font-mono text-amber-300">3</span>
                            </div>
                            <input type="range" id="sim2-range-p" min="-10" max="10" value="3" oninput="updateSim2()" class="w-full accent-amber-500 cursor-pointer">
                        </div>
                        <div>
                            <div class="flex justify-between text-xs font-bold mb-1">
                                <span class="text-sky-400">Denominator ($q$):</span>
                                <span id="sim2-val-q" class="font-mono text-sky-300">4</span>
                            </div>
                            <input type="range" id="sim2-range-q" min="-10" max="10" value="4" oninput="updateSim2()" class="w-full accent-sky-500 cursor-pointer">
                        </div>
                    </div>

                    <!-- Output Card -->
                    <div class="p-4 rounded-xl bg-slate-900/90 border border-slate-800 flex flex-col items-center justify-center min-h-[140px] text-center">
                        <div id="sim2-fraction-view" class="flex flex-col items-center">
                            <span id="sim2-display-p" class="text-xl font-black text-amber-400">3</span>
                            <div class="w-16 h-0.5 bg-slate-400 my-1"></div>
                            <span id="sim2-display-q" class="text-xl font-black text-sky-400">4</span>
                        </div>
                        <div id="sim2-result" class="mt-2 text-xs font-bold text-emerald-400">
                            = 0.75 (Rational Number)
                        </div>
                        <div id="sim2-coprime-badge" class="mt-1 text-[10px] px-2 py-0.5 rounded bg-emerald-950 border border-emerald-500/40 text-emerald-300">
                            Simplest Form: gcd(3, 4) = 1
                        </div>
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">Rational Definition Inspector:</span>
                    <span id="sim2-analysis">p is an integer, q is a non-zero integer. The fraction is fully defined, valid, and represents a distinct point on the number line.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 3:
        # Simulator 3: Number Line Subdivider & Plotter
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.3: Number Line Subdivider & Fraction Mapper</span>
                </div>
                <div class="flex items-center gap-2">
                    <span class="text-xs text-slate-400">Denominator $q$:</span>
                    <select id="sim3-sel-q" onchange="updateSim3()" class="bg-slate-900 border border-slate-700 text-xs text-amber-300 rounded px-2 py-1">
                        <option value="2">2 (Halves)</option>
                        <option value="3">3 (Thirds)</option>
                        <option value="4" selected>4 (Quarters)</option>
                        <option value="5">5 (Fifths)</option>
                        <option value="8">8 (Eighths)</option>
                    </select>
                    <span class="text-xs text-slate-400 ml-2">Numerator $p$:</span>
                    <input type="number" id="sim3-inp-p" value="3" min="-8" max="8" onchange="updateSim3()" class="w-14 bg-slate-900 border border-slate-700 text-xs text-sky-300 rounded px-2 py-1 text-center font-bold">
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <svg id="sim3-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Horizontal Number Line -->
                    <line x1="30" y1="140" x2="470" y2="140" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
                    <!-- Arrows -->
                    <polygon points="475,140 465,135 465,145" fill="#94a3b8"/>
                    <polygon points="25,140 35,135 35,145" fill="#94a3b8"/>

                    <!-- Main Integer Ticks (-2, -1, 0, 1, 2) -->
                    <!-- -2 at 70, -1 at 160, 0 at 250, 1 at 340, 2 at 430 (Distance = 90px per unit) -->
                    <g id="sim3-integer-ticks">
                        <line x1="70" y1="125" x2="70" y2="155" stroke="#f8fafc" stroke-width="2.5"/>
                        <text x="70" y="175" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">-2</text>

                        <line x1="160" y1="125" x2="160" y2="155" stroke="#f8fafc" stroke-width="2.5"/>
                        <text x="160" y="175" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">-1</text>

                        <line x1="250" y1="120" x2="250" y2="160" stroke="#f59e0b" stroke-width="3"/>
                        <text x="250" y="175" fill="#f59e0b" font-size="12" font-weight="black" text-anchor="middle">0 (Origin)</text>

                        <line x1="340" y1="125" x2="340" y2="155" stroke="#f8fafc" stroke-width="2.5"/>
                        <text x="340" y="175" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">+1</text>

                        <line x1="430" y1="125" x2="430" y2="155" stroke="#f8fafc" stroke-width="2.5"/>
                        <text x="430" y="175" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">+2</text>
                    </g>

                    <!-- Dynamic Sub-ticks container -->
                    <g id="sim3-subticks"></g>

                    <!-- Glowing Target Point Marker -->
                    <g id="sim3-marker" class="transition-transform duration-500">
                        <circle cx="317.5" cy="140" r="7" fill="#ec4899" stroke="#fbcfe8" stroke-width="2"/>
                        <path d="M 317.5 70 L 317.5 130" stroke="#ec4899" stroke-width="2" stroke-dasharray="3,2"/>
                        <rect x="290" y="45" width="55" height="24" rx="6" fill="#831843" stroke="#f472b6" stroke-width="1.5"/>
                        <text id="sim3-marker-label" x="317.5" y="61" fill="#fdf2f8" font-size="10" font-weight="black" text-anchor="middle">3/4 = 0.75</text>
                    </g>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim3-caption">Plotting p/q:</span>
                    <span id="sim3-desc">Unit intervals are partitioned into 4 equal segments of width 1/4 (0.25). Starting from 0, stepping 3 units to the right locates 3/4.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 4:
        # Simulator 4: Field Axioms Interactive Demonstrator
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.4: Algebraic Field Axioms Demonstrator</span>
                </div>
                <div class="flex flex-wrap items-center gap-1.5">
                    <button onclick="setSim4Axiom('comm')" id="sim4-btn-comm" class="px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white transition">Commutative</button>
                    <button onclick="setSim4Axiom('assoc')" id="sim4-btn-assoc" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Associative</button>
                    <button onclick="setSim4Axiom('dist')" id="sim4-btn-dist" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Distributive</button>
                    <button onclick="setSim4Axiom('inv')" id="sim4-btn-inv" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Inverses</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <svg id="sim4-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Left Side Box -->
                    <rect x="30" y="40" width="190" height="120" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
                    <text x="125" y="65" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Left Hand Side (LHS)</text>
                    <text id="sim4-lhs-expr" x="125" y="105" fill="#fef08a" font-size="13" font-weight="black" text-anchor="middle">1/2 + 2/3</text>
                    <text id="sim4-lhs-val" x="125" y="135" fill="#86efac" font-size="12" font-weight="bold" text-anchor="middle">= 7/6 ≈ 1.166...</text>

                    <!-- Center Equals Sign -->
                    <circle cx="250" cy="100" r="20" fill="#312e81" stroke="#818cf8" stroke-width="2"/>
                    <text x="250" y="107" fill="#ffffff" font-size="20" font-weight="black" text-anchor="middle">=</text>

                    <!-- Right Side Box -->
                    <rect x="280" y="40" width="190" height="120" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
                    <text x="375" y="65" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Right Hand Side (RHS)</text>
                    <text id="sim4-rhs-expr" x="375" y="105" fill="#fef08a" font-size="13" font-weight="black" text-anchor="middle">2/3 + 1/2</text>
                    <text id="sim4-rhs-val" x="375" y="135" fill="#86efac" font-size="12" font-weight="bold" text-anchor="middle">= 7/6 ≈ 1.166...</text>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim4-title">Commutative Property:</span>
                    <span id="sim4-desc">Order of operands does not change the result: a + b = b + a and a × b = b × a. Subtraction and division do not hold this property.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 5:
        # Simulator 5: Rational Density Zoom Magnifier
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.5: Rational Density Zoom Magnifier</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="zoomSim5()" id="sim5-zoom-btn" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 text-white shadow-lg transition cursor-pointer">
                        🔍 Zoom & Find Midpoint
                    </button>
                    <button onclick="resetSim5()" class="px-2.5 py-1.5 rounded-lg text-xs font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition">
                        Reset
                    </button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <svg id="sim5-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Dynamic Zoom Level text -->
                    <text id="sim5-level" x="250" y="30" fill="#a78bfa" font-size="11" font-weight="bold" text-anchor="middle">Iteration Level: 1 (Between 0 and 1)</text>

                    <!-- Base Number line -->
                    <line x1="50" y1="120" x2="450" y2="120" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>

                    <!-- Left bound A -->
                    <line x1="50" y1="100" x2="50" y2="140" stroke="#f59e0b" stroke-width="3"/>
                    <text id="sim5-label-a" x="50" y="165" fill="#fef08a" font-size="12" font-weight="black" text-anchor="middle">a = 0</text>

                    <!-- Right bound B -->
                    <line x1="450" y1="100" x2="450" y2="140" stroke="#f59e0b" stroke-width="3"/>
                    <text id="sim5-label-b" x="450" y="165" fill="#fef08a" font-size="12" font-weight="black" text-anchor="middle">b = 1</text>

                    <!-- Midpoint M -->
                    <g id="sim5-midpoint-group" class="transition-all duration-500">
                        <line x1="250" y1="95" x2="250" y2="145" stroke="#10b981" stroke-width="3"/>
                        <circle cx="250" cy="120" r="6" fill="#10b981"/>
                        <rect x="200" y="55" width="100" height="25" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
                        <text id="sim5-label-m" x="250" y="72" fill="#a7f3d0" font-size="10" font-weight="black" text-anchor="middle">m = 1/2 = 0.5</text>
                    </g>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">Density Proof Principle:</span>
                    <span id="sim5-desc">The midpoint (a + b)/2 is strictly between a and b. We can repeat this bisection infinitely many times, proving that infinite rational numbers reside in any interval.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 6:
        # Simulator 6: Algorithmic n-Rationals Generator (d = (b - a)/(n + 1))
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.6: Algorithmic n-Rationals Generator ($d = \\frac{b-a}{n+1}$)</span>
                </div>
                <div class="flex items-center gap-2">
                    <span class="text-xs text-slate-400">Choose $n$:</span>
                    <button onclick="setSim6Count(3)" id="sim6-btn-3" class="px-2 py-0.5 rounded text-xs font-bold bg-slate-800 text-slate-300">n=3</button>
                    <button onclick="setSim6Count(5)" id="sim6-btn-5" class="px-2 py-0.5 rounded text-xs font-bold bg-indigo-600 text-white">n=5</button>
                    <button onclick="setSim6Count(7)" id="sim6-btn-7" class="px-2 py-0.5 rounded text-xs font-bold bg-slate-800 text-slate-300">n=7</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <svg id="sim6-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <text x="250" y="30" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">
                        Interval [a, b] = [1, 2] | Step Size: d = (2 - 1) / (n + 1)
                    </text>

                    <!-- Main Line -->
                    <line x1="50" y1="120" x2="450" y2="120" stroke="#64748b" stroke-width="4" stroke-linecap="round"/>

                    <!-- Boundary A = 1 -->
                    <line x1="50" y1="100" x2="50" y2="140" stroke="#f59e0b" stroke-width="3"/>
                    <text x="50" y="165" fill="#fef08a" font-size="12" font-weight="black" text-anchor="middle">a = 1</text>

                    <!-- Boundary B = 2 -->
                    <line x1="450" y1="100" x2="450" y2="140" stroke="#f59e0b" stroke-width="3"/>
                    <text x="450" y="165" fill="#fef08a" font-size="12" font-weight="black" text-anchor="middle">b = 2</text>

                    <!-- Dynamic Computed Points -->
                    <g id="sim6-points"></g>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">Step-Size Algorithm:</span>
                    <span id="sim6-desc">For n = 5, step size d = (2 - 1)/(5 + 1) = 1/6. The 5 rational numbers are 7/6, 8/6, 9/6, 10/6, and 11/6.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 7:
        # Simulator 7: Terminating Decimal Factoriser Engine (q = 2^m 5^n)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.7: Denominator Factoriser ($q = 2^m 5^n$)</span>
                </div>
                <div class="flex items-center gap-1.5 text-xs">
                    <button onclick="testSim7(8)" class="px-2 py-0.5 rounded bg-indigo-600 text-white font-bold">q=8</button>
                    <button onclick="testSim7(25)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 hover:bg-slate-700">q=25</button>
                    <button onclick="testSim7(80)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 hover:bg-slate-700">q=80</button>
                    <button onclick="testSim7(14)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 hover:bg-slate-700">q=14</button>
                    <button onclick="testSim7(75)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 hover:bg-slate-700">q=75</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
                    <div class="p-4 rounded-xl bg-slate-900 border border-slate-800 space-y-2">
                        <span class="text-xs font-bold text-slate-400">Fraction Under Inspection:</span>
                        <div class="text-lg font-mono font-bold text-amber-300" id="sim7-fraction-str">3 / 8</div>
                        <div class="text-xs text-sky-300">
                            <strong>Denominator:</strong> <span id="sim7-q-val">q = 8</span><br>
                            <strong>Prime Factors:</strong> <span id="sim7-factors" class="font-mono text-emerald-400">2³ × 5⁰</span>
                        </div>
                    </div>

                    <div id="sim7-badge-card" class="p-4 rounded-xl bg-emerald-950/80 border border-emerald-500 text-center space-y-2">
                        <span id="sim7-badge-status" class="px-2.5 py-1 rounded text-xs font-black bg-emerald-600 text-white uppercase tracking-wider">
                            ✓ TERMINATING DECIMAL
                        </span>
                        <p id="sim7-badge-places" class="text-xs text-emerald-300 font-bold">
                            Terminates after max(3, 0) = 3 decimal places
                        </p>
                        <p id="sim7-badge-val" class="font-mono text-sm text-white font-bold">
                            3 / 8 = 0.375
                        </p>
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">Prime Factorisation Rule:</span>
                    <span id="sim7-rule-desc">Since q contains only powers of 2, the division leaves a remainder of 0 after 3 steps.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 8:
        # Simulator 8: Long Division Remainder Loop Visualizer (1/7 = 0.142857...)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.8: Long Division Remainder Loop Engine ($1/7$)</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="stepSim8Division()" id="sim8-step-btn" class="px-3 py-1 rounded text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition cursor-pointer">
                        Step Division ➔
                    </button>
                    <button onclick="resetSim8()" class="px-2 py-1 rounded text-xs font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition">
                        Reset
                    </button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <svg id="sim8-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Long Division Layout -->
                    <text x="50" y="40" fill="#38bdf8" font-size="12" font-weight="bold">Long Division: 1 ÷ 7</text>
                    <text id="sim8-quotient" x="180" y="40" fill="#facc15" font-size="14" font-weight="black" font-family="monospace">0.</text>

                    <!-- Remainder cycle nodes in a circle -->
                    <g transform="translate(370, 110)">
                        <circle cx="0" cy="0" r="75" fill="none" stroke="#334155" stroke-dasharray="4,4"/>
                        <text x="0" y="-85" fill="#a78bfa" font-size="9" font-weight="bold" text-anchor="middle">Remainder Cycle (Max 6)</text>

                        <!-- Remainder points (3, 2, 6, 4, 5, 1) -->
                        <circle id="sim8-node-3" cx="0" cy="-60" r="14" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
                        <text x="0" y="-56" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">3</text>

                        <circle id="sim8-node-2" cx="52" cy="-30" r="14" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
                        <text x="52" y="-26" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">2</text>

                        <circle id="sim8-node-6" cx="52" cy="30" r="14" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
                        <text x="52" y="34" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">6</text>

                        <circle id="sim8-node-4" cx="0" cy="60" r="14" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
                        <text x="0" y="64" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">4</text>

                        <circle id="sim8-node-5" cx="-52" cy="30" r="14" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
                        <text x="-52" y="34" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">5</text>

                        <circle id="sim8-node-1" cx="-52" cy="-30" r="14" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
                        <text x="-52" y="-26" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">1</text>
                    </g>

                    <!-- Division step box left -->
                    <rect x="30" y="60" width="230" height="110" rx="8" fill="#0f172a" stroke="#475569"/>
                    <text id="sim8-step-text" x="45" y="85" fill="#e2e8f0" font-size="10" font-family="monospace">
                        Step 0: Press 'Step Division' to begin.
                    </text>
                    <text id="sim8-rem-text" x="45" y="110" fill="#38bdf8" font-size="10" font-family="monospace">
                        Current Remainder: None
                    </text>
                    <text id="sim8-status-text" x="45" y="135" fill="#a7f3d0" font-size="10" font-weight="bold">
                        Periodicity counter: 0 / 6
                    </text>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">Pigeonhole Principle Demonstration:</span>
                    <span id="sim8-exp">Dividing by 7 allows only 6 non-zero remainders {1, 2, 3, 4, 5, 6}. Once a remainder repeats, the quotient repeats forever!</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 9:
        # Simulator 9: Recurring Decimal to p/q Algebraic Solver
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.9: Recurring Decimal to $p/q$ Algebraic Solver</span>
                </div>
                <div class="flex items-center gap-1.5 text-xs">
                    <button onclick="setSim9Example('0.3bar')" id="sim9-btn-03" class="px-2 py-0.5 rounded font-bold bg-indigo-600 text-white">0.3̅</button>
                    <button onclick="setSim9Example('0.47bar')" id="sim9-btn-047" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">0.47̅</button>
                    <button onclick="setSim9Example('0.27bar')" id="sim9-btn-027" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">0.27̅</button>
                    <button onclick="setSim9Example('0.9bar')" id="sim9-btn-09" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">0.9̅ (= 1)</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="bg-slate-900/90 border border-slate-700 p-3 rounded-xl flex-1 flex flex-col justify-center space-y-2 font-mono text-xs">
                    <div class="text-amber-400 font-bold" id="sim9-step1">
                        Step 1: Let x = 0.3333...  (Equation 1)
                    </div>
                    <div class="text-sky-300 font-bold" id="sim9-step2">
                        Step 2: Multiply by 10¹ = 10 ➔ 10x = 3.3333...  (Equation 2)
                    </div>
                    <div class="text-purple-300 font-bold" id="sim9-step3">
                        Step 3: Subtract Eq (1) from Eq (2) ➔ 10x - x = 3.333... - 0.333...
                    </div>
                    <div class="text-emerald-400 font-bold text-sm bg-slate-950 p-2 rounded-lg border border-slate-800" id="sim9-step4">
                        Result: 9x = 3 ➔ x = 3/9 = 1/3 (Rational!)
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">Algebraic Principle:</span>
                    <span id="sim9-summary">Multiplying by 10^k perfectly shifts one cycle to the left of the decimal, allowing the infinite tails to cancel out!</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 10:
        # Simulator 10: Rational vs Irrational Interactive Sorter
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.10: Rational vs Irrational Sorter</span>
                </div>
                <button onclick="resetSim10()" class="px-2.5 py-1 rounded text-xs font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition">
                    Reset Items
                </button>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <!-- Clickable Number Tokens -->
                <div class="flex flex-wrap items-center justify-center gap-2 mb-2" id="sim10-tokens">
                    <button onclick="sortSim10('pi', 'irrational')" id="s10-pi" class="px-2.5 py-1 rounded-lg bg-slate-800 border border-slate-700 text-xs font-bold text-white hover:border-amber-400">π</button>
                    <button onclick="sortSim10('22/7', 'rational')" id="s10-227" class="px-2.5 py-1 rounded-lg bg-slate-800 border border-slate-700 text-xs font-bold text-white hover:border-amber-400">22/7</button>
                    <button onclick="sortSim10('sqrt2', 'irrational')" id="s10-sqrt2" class="px-2.5 py-1 rounded-lg bg-slate-800 border border-slate-700 text-xs font-bold text-white hover:border-amber-400">√2</button>
                    <button onclick="sortSim10('sqrt25', 'rational')" id="s10-sqrt25" class="px-2.5 py-1 rounded-lg bg-slate-800 border border-slate-700 text-xs font-bold text-white hover:border-amber-400">√25 (=5)</button>
                    <button onclick="sortSim10('0.3bar', 'rational')" id="s10-03bar" class="px-2.5 py-1 rounded-lg bg-slate-800 border border-slate-700 text-xs font-bold text-white hover:border-amber-400">0.333...</button>
                    <button onclick="sortSim10('nonrec', 'irrational')" id="s10-nonrec" class="px-2.5 py-1 rounded-lg bg-slate-800 border border-slate-700 text-xs font-bold text-white hover:border-amber-400">0.101001...</button>
                </div>

                <!-- Drop Target Boxes -->
                <div class="grid grid-cols-2 gap-3 flex-1 items-stretch">
                    <div class="p-3 rounded-xl bg-sky-950/40 border border-sky-500/40 flex flex-col justify-between">
                        <span class="text-xs font-black text-sky-400 uppercase tracking-wider text-center">Rational (ℚ)</span>
                        <div id="sim10-box-rational" class="flex flex-wrap gap-1.5 justify-center py-2 min-h-[50px]"></div>
                        <span class="text-[10px] text-sky-300/70 text-center">Terminating or Repeating</span>
                    </div>

                    <div class="p-3 rounded-xl bg-rose-950/40 border border-rose-500/40 flex flex-col justify-between">
                        <span class="text-xs font-black text-rose-400 uppercase tracking-wider text-center">Irrational (𝕀)</span>
                        <div id="sim10-box-irrational" class="flex flex-wrap gap-1.5 justify-center py-2 min-h-[50px]"></div>
                        <span class="text-[10px] text-rose-300/70 text-center">Non-Terminating & Non-Repeating</span>
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2 rounded-lg text-[11px] text-slate-200 mt-2 text-center" id="sim10-feedback">
                    Click each number above to classify it into Rational or Irrational!
                </div>
            </div>
        </div>
        """

    elif s_idx == 11:
        # Simulator 11: Proof by Contradiction Tree for √2
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.11: Proof Tree for Irrationality of $\\sqrt{2}$</span>
                </div>
                <button onclick="advanceSim11()" id="sim11-next-btn" class="px-3 py-1 rounded text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition cursor-pointer">
                    Next Logical Step ➔
                </button>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="grid grid-cols-4 gap-2 text-center font-mono text-[11px] h-full items-center">
                    <!-- Step 1 -->
                    <div id="sim11-step-1" class="p-2 rounded-lg bg-slate-900 border border-amber-500 text-amber-300">
                        <span class="font-bold text-[9px] block text-slate-400">STEP 1</span>
                        Assume $\\sqrt{2} = \\frac{a}{b}$<br>
                        <span class="text-[9px] text-emerald-400">gcd(a, b) = 1</span>
                    </div>

                    <!-- Step 2 -->
                    <div id="sim11-step-2" class="p-2 rounded-lg bg-slate-900/40 border border-slate-800 text-slate-500">
                        <span class="font-bold text-[9px] block">STEP 2</span>
                        $a^2 = 2b^2$<br>
                        <span class="text-[9px]">2 divides $a$ (even)</span>
                    </div>

                    <!-- Step 3 -->
                    <div id="sim11-step-3" class="p-2 rounded-lg bg-slate-900/40 border border-slate-800 text-slate-500">
                        <span class="font-bold text-[9px] block">STEP 3</span>
                        $b^2 = 2k^2$<br>
                        <span class="text-[9px]">2 divides $b$ (even)</span>
                    </div>

                    <!-- Step 4 -->
                    <div id="sim11-step-4" class="p-2 rounded-lg bg-slate-900/40 border border-slate-800 text-slate-500">
                        <span class="font-bold text-[9px] block">CONCLUSION</span>
                        <span class="text-rose-400 font-bold">CONTRADICTION!</span><br>
                        $\\sqrt{2} \\notin \\mathbb{Q}$ (Irrational)
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim11-title">Logical Deduction:</span>
                    <span id="sim11-desc">We assume √2 is rational and can be written in irreducible co-prime form gcd(a, b) = 1. Click 'Next Logical Step' to advance the proof.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 12:
        # Simulator 12: Proof by Contradiction Tree for √3
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.12: Proof Tree for Irrationality of $\\sqrt{3}$</span>
                </div>
                <button onclick="advanceSim12()" id="sim12-next-btn" class="px-3 py-1 rounded text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition cursor-pointer">
                    Next Logical Step ➔
                </button>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="grid grid-cols-4 gap-2 text-center font-mono text-[11px] h-full items-center">
                    <div id="sim12-step-1" class="p-2 rounded-lg bg-slate-900 border border-amber-500 text-amber-300">
                        <span class="font-bold text-[9px] block text-slate-400">STEP 1</span>
                        Assume $\\sqrt{3} = \\frac{a}{b}$<br>
                        <span class="text-[9px] text-emerald-400">gcd(a, b) = 1</span>
                    </div>
                    <div id="sim12-step-2" class="p-2 rounded-lg bg-slate-900/40 border border-slate-800 text-slate-500">
                        <span class="font-bold text-[9px] block">STEP 2</span>
                        $a^2 = 3b^2$<br>
                        <span class="text-[9px]">3 divides $a$ ($a=3m$)</span>
                    </div>
                    <div id="sim12-step-3" class="p-2 rounded-lg bg-slate-900/40 border border-slate-800 text-slate-500">
                        <span class="font-bold text-[9px] block">STEP 3</span>
                        $b^2 = 3m^2$<br>
                        <span class="text-[9px]">3 divides $b$</span>
                    </div>
                    <div id="sim12-step-4" class="p-2 rounded-lg bg-slate-900/40 border border-slate-800 text-slate-500">
                        <span class="font-bold text-[9px] block">CONCLUSION</span>
                        <span class="text-rose-400 font-bold">CONTRADICTION!</span><br>
                        $\\sqrt{3} \\notin \\mathbb{Q}$ (Irrational)
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim12-title">Generalised Non-Square Rule:</span>
                    <span id="sim12-desc">Since 3 is not a perfect square, √3 is irrational. If a² = 3b², 3 divides a. Substituting a = 3m shows 3 divides b, violating co-primality.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 13:
        # Simulator 13: Pythagorean Compass Construction on Number Line
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.13: Compass Arc Construction for $\\sqrt{2}$</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="animateSim13Compass()" id="sim13-arc-btn" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-gradient-to-r from-amber-600 to-rose-600 hover:from-amber-500 hover:to-rose-500 text-white shadow-lg transition cursor-pointer">
                        📐 Swing Compass Arc to Line
                    </button>
                    <button onclick="resetSim13()" class="px-2.5 py-1.5 rounded-lg text-xs font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition">
                        Reset
                    </button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <svg id="sim13-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Number line -->
                    <line x1="40" y1="180" x2="460" y2="180" stroke="#94a3b8" stroke-width="3"/>
                    <line x1="120" y1="170" x2="120" y2="190" stroke="#f8fafc" stroke-width="2"/>
                    <text x="120" y="210" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">O (0)</text>

                    <line x1="240" y1="170" x2="240" y2="190" stroke="#f8fafc" stroke-width="2"/>
                    <text x="240" y="210" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">A (1)</text>

                    <line x1="360" y1="170" x2="360" y2="190" stroke="#f8fafc" stroke-width="2"/>
                    <text x="360" y="210" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">2</text>

                    <!-- Right triangle OAB (OA = 120px, AB = 120px) -->
                    <!-- Hypotenuse OB = sqrt(120^2 + 120^2) = 169.7px, intersects line at 120 + 169.7 = 289.7px (sqrt(2) = 1.414) -->
                    <line x1="240" y1="180" x2="240" y2="60" stroke="#38bdf8" stroke-width="3"/>
                    <text x="255" y="120" fill="#38bdf8" font-size="10" font-weight="bold">AB = 1</text>
                    <text x="180" y="195" fill="#e2e8f0" font-size="10" font-weight="bold">OA = 1</text>

                    <!-- Right angle marker -->
                    <rect x="230" y="170" width="10" height="10" fill="none" stroke="#38bdf8" stroke-width="1.5"/>

                    <!-- Hypotenuse OB -->
                    <line x1="120" y1="180" x2="240" y2="60" stroke="#f59e0b" stroke-width="3"/>
                    <text x="160" y="110" fill="#fbbf24" font-size="11" font-weight="black">OB = √2</text>

                    <!-- Compass Arc (initially hidden) -->
                    <path id="sim13-arc" d="M 240 60 A 169.7 169.7 0 0 1 289.7 180" fill="none" stroke="#ec4899" stroke-width="3" stroke-dasharray="5,3" class="hidden"/>

                    <!-- Point P on line (initially hidden) -->
                    <g id="sim13-point-p" class="hidden">
                        <circle cx="289.7" cy="180" r="6" fill="#ec4899" stroke="#fff" stroke-width="2"/>
                        <text x="289.7" y="215" fill="#f472b6" font-size="12" font-weight="black" text-anchor="middle">P (√2 ≈ 1.414)</text>
                    </g>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim13-status">Pythagorean Construction:</span>
                    <span id="sim13-desc">Right triangle with base 1 and height 1 produces hypotenuse √2. Swinging compass centered at origin transfers this exact length onto the number line.</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 14:
        # Simulator 14: Dynamic Square Root Spiral (Theodorus Spiral)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.14: Theodorus Square Root Spiral Generator</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="addSpiralStep()" id="sim14-add-btn" class="px-3 py-1 rounded text-xs font-bold bg-indigo-600 hover:bg-indigo-500 text-white transition cursor-pointer">
                        + Next Root (√n)
                    </button>
                    <button onclick="resetSpiral()" class="px-2 py-1 rounded text-xs font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition">
                        Reset
                    </button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <svg id="sim14-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Origin O -->
                    <circle cx="250" cy="120" r="5" fill="#f59e0b"/>
                    <text x="250" y="135" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">O (Origin)</text>

                    <!-- Spiral Triangles Container -->
                    <g id="sim14-spiral-group"></g>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">Theodorus Spiral Construction:</span>
                    <span id="sim14-caption">Currently showing roots up to √2. Each new right triangle takes the previous hypotenuse as base and adds a perpendicular of 1 unit!</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 15:
        # Simulator 15: Conjugate Denominator Rationaliser
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.15: Conjugate Denominator Rationaliser</span>
                </div>
                <div class="flex items-center gap-1.5 text-xs">
                    <button onclick="setSim15Expr(1)" id="sim15-btn-1" class="px-2 py-0.5 rounded font-bold bg-indigo-600 text-white">1 / (√7 - 2)</button>
                    <button onclick="setSim15Expr(2)" id="sim15-btn-2" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">1 / (√5 + √2)</button>
                    <button onclick="setSim15Expr(3)" id="sim15-btn-3" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">1 / √3</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="bg-slate-900/90 border border-slate-700 p-3 rounded-xl flex-1 flex flex-col justify-center space-y-2 font-mono text-xs">
                    <div class="text-amber-300 font-bold" id="sim15-original">
                        Original Fraction: 1 / (√7 - 2)
                    </div>
                    <div class="text-sky-300 font-bold" id="sim15-step1">
                        Multiply Numerator & Denominator by Conjugate (√7 + 2):<br>
                        [1 × (√7 + 2)] / [(√7 - 2)(√7 + 2)]
                    </div>
                    <div class="text-purple-300 font-bold" id="sim15-step2">
                        Apply Difference of Squares: (√7)² - 2² = 7 - 4 = 3
                    </div>
                    <div class="text-emerald-400 font-bold text-sm bg-slate-950 p-2 rounded-lg border border-slate-800" id="sim15-result">
                        Rationalised Result: (√7 + 2) / 3
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">Rationalisation Rule:</span>
                    <span id="sim15-desc">Using conjugate (a ∓ √b) turns the irrational denominator into an integer using (x+y)(x-y) = x² - y².</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 16:
        # Simulator 16: Laws of Exponents Power Calculator & Rule Switcher
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-indigo-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-indigo-400">Interactive Lab 1.16: Laws of Exponents Algorithmic Engine</span>
                </div>
                <div class="flex flex-wrap items-center gap-1.5 text-xs">
                    <button onclick="setSim16Rule('prod')" id="sim16-btn-prod" class="px-2 py-0.5 rounded font-bold bg-indigo-600 text-white">Product Rule</button>
                    <button onclick="setSim16Rule('quot')" id="sim16-btn-quot" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Quotient Rule</button>
                    <button onclick="setSim16Rule('pow')" id="sim16-btn-pow" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Power of Power</button>
                    <button onclick="setSim16Rule('frac')" id="sim16-btn-frac" class="px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Fractional Power</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-indigo-950/20 to-slate-950 rounded-xl overflow-hidden border border-indigo-500/30 p-4 flex flex-col justify-between">
                <div class="bg-slate-900/90 border border-slate-700 p-3 rounded-xl flex-1 flex flex-col justify-center space-y-2 font-mono text-xs">
                    <div class="text-amber-300 font-bold text-sm" id="sim16-rule-name">
                        Law 1: Product with Same Base: a^m × a^n = a^(m + n)
                    </div>
                    <div class="text-sky-300" id="sim16-calc">
                        Example: 2^(2/3) × 2^(1/3) = 2^(2/3 + 1/3) = 2^(3/3)
                    </div>
                    <div class="text-emerald-400 font-bold text-sm bg-slate-950 p-2 rounded-lg border border-slate-800" id="sim16-output">
                        Simplified Evaluated Value: 2¹ = 2
                    </div>
                </div>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">Computational Thinking:</span>
                    <span id="sim16-desc">Exponent rules allow logarithmic reduction of computational complexity from exponential products to simple addition of fractions.</span>
                </div>
            </div>
        </div>
        """

    return ""


def build_full_html():
    """Compiles the master HTML for Class 9 Maths Chapter 1: Number System."""

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
                    <!-- Academic Blazer / Coat in Deep Royal Blue -->
                    <path d="M20 115 C20 85, 45 80, 60 80 C75 80, 100 85, 100 115 Z" fill="#1e1b4b" stroke="#4338ca" stroke-width="2"/>
                    <!-- Crisp White Shirt Collar & Turquoise Tie -->
                    <polygon points="50,80 60,95 70,80 60,82" fill="#ffffff"/>
                    <polygon points="58,83 62,83 64,115 56,115" fill="#06b6d4"/>
                    <!-- Neck -->
                    <rect x="52" y="68" width="16" height="15" fill="#fed7aa" rx="2"/>
                    <!-- Face -->
                    <ellipse cx="60" cy="50" rx="24" ry="26" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
                    <!-- Modern Glasses -->
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
                    <!-- Sleek Hair Cut -->
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
                        Professor Sophia's Audio Walkthrough (Speech & Concepts)
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
                        Unit 1 • Number System (12 Periods)
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
                        <h3 class="font-bold text-xs uppercase tracking-wider text-indigo-400">Curriculum Concepts, Proofs & Computational Thinking</h3>
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
    <title>Class 9 Mathematics • Chapter 1: Number System (Interactive Multimedia Lab)</title>
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

        /* Avatar gentle breathing / talking animation */
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
                    <span class="text-[10px] font-extrabold uppercase tracking-widest text-indigo-400">NCERT Class 9 Mathematics • Chapter 1</span>
                    <h1 class="text-sm font-bold text-white flex items-center gap-2">
                        <span>Unit 1: Number System</span>
                        <span class="text-xs text-slate-400 font-normal">| 12 Periods • CG-1, C-1.1, CG-9</span>
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
                    🎉 You have reached the last slide of this chapter (Unit 1: Number System)!
                </p>
                <p class="text-[11px] text-slate-300 mt-0.5">
                    Congratulations! You have completed all 16 conceptual curriculum slides, 32 checkpoints, and 40 mastery questions on rational and irrational numbers.
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
        function setSim1Set(setName) {{
            playTone(520, 'sine', 0.08);
            const title = document.getElementById('sim1-info-title');
            const desc = document.getElementById('sim1-info-desc');
            const btns = ['N', 'W', 'Z', 'Q', 'I', 'R'];
            btns.forEach(b => {{
                const el = document.getElementById(`sim1-btn-${{b}}`);
                if (el) el.className = (b === setName) ? 'px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white transition' : 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
            }});

            if (setName === 'N') {{
                title.textContent = "Natural Numbers (ℕ):";
                desc.textContent = "The set {1, 2, 3, 4, ...}. Used for counting. ℕ is a strict subset of 𝕎, ℤ, ℚ, and ℝ.";
            }} else if (setName === 'W') {{
                title.textContent = "Whole Numbers (𝕎):";
                desc.textContent = "Natural numbers plus zero: {0, 1, 2, 3, ...}. Zero provides the additive identity (a + 0 = a).";
            }} else if (setName === 'Z') {{
                title.textContent = "Integers (ℤ):";
                desc.textContent = "Negative integers, zero, and positive integers: {..., -3, -2, -1, 0, 1, 2, 3, ...}. Closed under subtraction.";
            }} else if (setName === 'Q') {{
                title.textContent = "Rational Numbers (ℚ):";
                desc.textContent = "Numbers expressible as p/q where p, q are integers and q ≠ 0. Includes all fractions, terminating decimals, and repeating decimals.";
            }} else if (setName === 'I') {{
                title.textContent = "Irrational Numbers (𝕀):";
                desc.textContent = "Numbers that CANNOT be written as p/q. Their decimal representations are non-terminating and non-recurring (e.g. √2, √3, π).";
            }} else {{
                title.textContent = "Real Numbers (ℝ):";
                desc.textContent = "The complete continuum of Rational and Irrational numbers combined (ℝ = ℚ ∪ 𝕀). Every real number corresponds to a point on the number line.";
            }}
        }}

        // Sim 2
        function gcd(a, b) {{
            a = Math.abs(a); b = Math.abs(b);
            while (b) {{ let t = b; b = a % b; a = t; }}
            return a;
        }}

        function setSim2Preset(p, q) {{
            document.getElementById('sim2-range-p').value = p;
            document.getElementById('sim2-range-q').value = q;
            updateSim2();
        }}

        function updateSim2() {{
            const p = parseInt(document.getElementById('sim2-range-p').value);
            const q = parseInt(document.getElementById('sim2-range-q').value);
            document.getElementById('sim2-val-p').textContent = p;
            document.getElementById('sim2-val-q').textContent = q;
            document.getElementById('sim2-display-p').textContent = p;
            document.getElementById('sim2-display-q').textContent = q;

            const resEl = document.getElementById('sim2-result');
            const badgeEl = document.getElementById('sim2-coprime-badge');
            const analysisEl = document.getElementById('sim2-analysis');

            if (q === 0) {{
                playIncorrectSound();
                resEl.textContent = "⚠️ UNDEFINED! (Division by zero)";
                resEl.className = "mt-2 text-xs font-bold text-rose-400";
                badgeEl.textContent = "q = 0 is forbidden in mathematics";
                badgeEl.className = "mt-1 text-[10px] px-2 py-0.5 rounded bg-rose-950 border border-rose-500/40 text-rose-300";
                analysisEl.textContent = "Division by zero is undefined because no real number k satisfies k × 0 = p for p ≠ 0, and for p = 0 any number satisfies it (indeterminate).";
            }} else {{
                playTone(450 + Math.abs(p) * 15, 'sine', 0.05);
                const val = (p / q).toFixed(4).replace(/\\.?0+$/, "");
                resEl.textContent = `= ${{val}} (Rational Number)`;
                resEl.className = "mt-2 text-xs font-bold text-emerald-400";

                const g = gcd(p, q);
                if (g === 1) {{
                    badgeEl.textContent = `Simplest Form: gcd(${{p}}, ${{q}}) = 1`;
                    badgeEl.className = "mt-1 text-[10px] px-2 py-0.5 rounded bg-emerald-950 border border-emerald-500/40 text-emerald-300";
                }} else {{
                    const simpP = p / g;
                    const simpQ = q / g;
                    badgeEl.textContent = `Equivalent Fraction: Simplifies to ${{simpP}}/${{simpQ}} (gcd=${{g}})`;
                    badgeEl.className = "mt-1 text-[10px] px-2 py-0.5 rounded bg-amber-950 border border-amber-500/40 text-amber-300";
                }}
                analysisEl.textContent = `Valid rational fraction p/q where p=${{p}} and q=${{q}} (q ≠ 0).`;
            }}
        }}

        // Sim 3
        function updateSim3() {{
            playTone(500, 'sine', 0.08);
            const q = parseInt(document.getElementById('sim3-sel-q').value);
            const p = parseInt(document.getElementById('sim3-inp-p').value);

            const subticksGroup = document.getElementById('sim3-subticks');
            subticksGroup.innerHTML = '';

            const unitPx = 90; // 90px per unit
            const originX = 250;

            // Draw sub-ticks from -2 to +2
            for (let u = -2; u < 2; u++) {{
                for (let k = 1; k < q; k++) {{
                    const x = originX + (u + k / q) * unitPx;
                    const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                    line.setAttribute('x1', x);
                    line.setAttribute('y1', 132);
                    line.setAttribute('x2', x);
                    line.setAttribute('y2', 148);
                    line.setAttribute('stroke', '#38bdf8');
                    line.setAttribute('stroke-width', '1.5');
                    subticksGroup.appendChild(line);
                }}
            }}

            const targetX = originX + (p / q) * unitPx;
            const marker = document.getElementById('sim3-marker');
            marker.setAttribute('transform', `translate(${{targetX - 317.5}}, 0)`);
            document.getElementById('sim3-marker-label').textContent = `${{p}}/${{q}} = ${{ (p / q).toFixed(2) }}`;
            document.getElementById('sim3-desc').textContent = `Unit intervals partitioned into ${{q}} equal segments of width 1/${{q}}. Stepping ${{p}} sub-units from 0 positions ${{p}}/${{q}}.`;
        }}

        // Sim 4
        function setSim4Axiom(ax) {{
            playTone(530, 'sine', 0.08);
            const bC = document.getElementById('sim4-btn-comm');
            const bA = document.getElementById('sim4-btn-assoc');
            const bD = document.getElementById('sim4-btn-dist');
            const bI = document.getElementById('sim4-btn-inv');

            [bC, bA, bD, bI].forEach(b => b.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition');

            const lEx = document.getElementById('sim4-lhs-expr');
            const lVal = document.getElementById('sim4-lhs-val');
            const rEx = document.getElementById('sim4-rhs-expr');
            const rVal = document.getElementById('sim4-rhs-val');
            const t = document.getElementById('sim4-title');
            const d = document.getElementById('sim4-desc');

            if (ax === 'comm') {{
                bC.className = 'px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white transition';
                lEx.textContent = "1/2 + 2/3";
                lVal.textContent = "= 7/6 ≈ 1.166...";
                rEx.textContent = "2/3 + 1/2";
                rVal.textContent = "= 7/6 ≈ 1.166...";
                t.textContent = "Commutative Property (a + b = b + a):";
                d.textContent = "The order of addition or multiplication does not change the result.";
            }} else if (ax === 'assoc') {{
                bA.className = 'px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white transition';
                lEx.textContent = "(1/2 + 1/3) + 1/4";
                lVal.textContent = "5/6 + 1/4 = 13/12";
                rEx.textContent = "1/2 + (1/3 + 1/4)";
                rVal.textContent = "1/2 + 7/12 = 13/12";
                t.textContent = "Associative Property ((a + b) + c = a + (b + c)):";
                d.textContent = "Grouping of numbers does not alter the sum or product.";
            }} else if (ax === 'dist') {{
                bD.className = 'px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white transition';
                lEx.textContent = "2 × (1/3 + 1/4)";
                lVal.textContent = "2 × (7/12) = 7/6";
                rEx.textContent = "(2 × 1/3) + (2 × 1/4)";
                rVal.textContent = "2/3 + 1/2 = 7/6";
                t.textContent = "Distributive Property (a(b + c) = ab + ac):";
                d.textContent = "Multiplication distributes smoothly over addition.";
            }} else {{
                bI.className = 'px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white transition';
                lEx.textContent = "3/4 + (-3/4)";
                lVal.textContent = "= 0 (Additive Identity)";
                rEx.textContent = "3/4 × (4/3)";
                rVal.textContent = "= 1 (Mult. Identity)";
                t.textContent = "Identity & Inverse Elements:";
                d.textContent = "Additive inverse gives 0; multiplicative inverse (reciprocal) gives 1.";
            }}
        }}

        // Sim 5
        let sim5Step = 0;
        function zoomSim5() {{
            sim5Step = (sim5Step + 1) % 4;
            playTone(400 + sim5Step * 70, 'sine', 0.1);
            const lblL = document.getElementById('sim5-level');
            const lblA = document.getElementById('sim5-label-a');
            const lblB = document.getElementById('sim5-label-b');
            const lblM = document.getElementById('sim5-label-m');

            if (sim5Step === 0) {{
                lblL.textContent = "Iteration Level: 1 (Between 0 and 1)";
                lblA.textContent = "a = 0";
                lblB.textContent = "b = 1";
                lblM.textContent = "m = 1/2 = 0.5";
            }} else if (sim5Step === 1) {{
                lblL.textContent = "Iteration Level: 2 (Zoomed between 0.5 and 1)";
                lblA.textContent = "a = 1/2 (0.5)";
                lblB.textContent = "b = 1 (1.0)";
                lblM.textContent = "m = 3/4 = 0.75";
            }} else if (sim5Step === 2) {{
                lblL.textContent = "Iteration Level: 3 (Zoomed between 0.75 and 1)";
                lblA.textContent = "a = 3/4 (0.75)";
                lblB.textContent = "b = 1 (1.0)";
                lblM.textContent = "m = 7/8 = 0.875";
            }} else {{
                lblL.textContent = "Iteration Level: 4 (Zoomed between 0.875 and 1)";
                lblA.textContent = "a = 7/8 (0.875)";
                lblB.textContent = "b = 1 (1.0)";
                lblM.textContent = "m = 15/16 = 0.9375";
            }}
        }}

        function resetSim5() {{
            sim5Step = -1;
            zoomSim5();
        }}

        // Sim 6
        function setSim6Count(n) {{
            playTone(520, 'sine', 0.08);
            ['3', '5', '7'].forEach(c => {{
                document.getElementById(`sim6-btn-${{c}}`).className = (c == n) ? 'px-2 py-0.5 rounded text-xs font-bold bg-indigo-600 text-white' : 'px-2 py-0.5 rounded text-xs font-bold bg-slate-800 text-slate-300';
            }});

            const ptsGroup = document.getElementById('sim6-points');
            ptsGroup.innerHTML = '';

            const startX = 50;
            const endX = 450;
            const stepPx = (endX - startX) / (n + 1);

            let descTxt = `For n = ${{n}}, step size d = (2 - 1)/(${{n}} + 1) = 1/${{n + 1}}. Generated numbers: `;
            const numList = [];

            for (let i = 1; i <= n; i++) {{
                const x = startX + i * stepPx;
                const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                circle.setAttribute('cx', x);
                circle.setAttribute('cy', 120);
                circle.setAttribute('r', 5);
                circle.setAttribute('fill', '#38bdf8');
                ptsGroup.appendChild(circle);

                const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                text.setAttribute('x', x);
                text.setAttribute('y', 95);
                text.setAttribute('fill', '#7dd3fc');
                text.setAttribute('font-size', '9');
                text.setAttribute('font-weight', 'bold');
                text.setAttribute('text-anchor', 'middle');
                text.textContent = `${{n + 1 + i}}/${{n + 1}}`;
                ptsGroup.appendChild(text);

                numList.push(`${{n + 1 + i}}/${{n + 1}}`);
            }}

            document.getElementById('sim6-desc').textContent = descTxt + numList.join(', ') + '.';
        }}

        // Sim 7
        function testSim7(q) {{
            playTone(530, 'sine', 0.08);
            const strEl = document.getElementById('sim7-fraction-str');
            const qEl = document.getElementById('sim7-q-val');
            const facEl = document.getElementById('sim7-factors');
            const badgeCard = document.getElementById('sim7-badge-card');
            const statusEl = document.getElementById('sim7-badge-status');
            const placesEl = document.getElementById('sim7-badge-places');
            const valEl = document.getElementById('sim7-badge-val');
            const ruleEl = document.getElementById('sim7-rule-desc');

            qEl.textContent = `q = ${{q}}`;

            if (q === 8) {{
                strEl.textContent = "3 / 8";
                facEl.textContent = "2³ × 5⁰";
                badgeCard.className = "p-4 rounded-xl bg-emerald-950/80 border border-emerald-500 text-center space-y-2";
                statusEl.className = "px-2.5 py-1 rounded text-xs font-black bg-emerald-600 text-white uppercase tracking-wider";
                statusEl.textContent = "✓ TERMINATING DECIMAL";
                placesEl.textContent = "Terminates after max(3, 0) = 3 decimal places";
                valEl.textContent = "3 / 8 = 0.375";
                ruleEl.textContent = "Denominator contains only factor 2. Hence terminates!";
            }} else if (q === 25) {{
                strEl.textContent = "7 / 25";
                facEl.textContent = "2⁰ × 5²";
                badgeCard.className = "p-4 rounded-xl bg-emerald-950/80 border border-emerald-500 text-center space-y-2";
                statusEl.className = "px-2.5 py-1 rounded text-xs font-black bg-emerald-600 text-white uppercase tracking-wider";
                statusEl.textContent = "✓ TERMINATING DECIMAL";
                placesEl.textContent = "Terminates after max(0, 2) = 2 decimal places";
                valEl.textContent = "7 / 25 = 0.28";
                ruleEl.textContent = "Denominator contains only factor 5. Hence terminates!";
            }} else if (q === 80) {{
                strEl.textContent = "13 / 80";
                facEl.textContent = "2⁴ × 5¹";
                badgeCard.className = "p-4 rounded-xl bg-emerald-950/80 border border-emerald-500 text-center space-y-2";
                statusEl.className = "px-2.5 py-1 rounded text-xs font-black bg-emerald-600 text-white uppercase tracking-wider";
                statusEl.textContent = "✓ TERMINATING DECIMAL";
                placesEl.textContent = "Terminates after max(4, 1) = 4 decimal places";
                valEl.textContent = "13 / 80 = 0.1625";
                ruleEl.textContent = "Denominator contains both 2 and 5. Hence terminates!";
            }} else if (q === 14) {{
                strEl.textContent = "5 / 14";
                facEl.textContent = "2¹ × 7¹ (Contains prime 7!)";
                badgeCard.className = "p-4 rounded-xl bg-rose-950/80 border border-rose-500 text-center space-y-2";
                statusEl.className = "px-2.5 py-1 rounded text-xs font-black bg-rose-600 text-white uppercase tracking-wider";
                statusEl.textContent = "✗ NON-TERMINATING RECURRING";
                placesEl.textContent = "Prime 7 ≠ 2 and ≠ 5 prevents remainder from becoming zero";
                valEl.textContent = "5 / 14 = 0.3571428...";
                ruleEl.textContent = "Prime factor 7 produces an infinite periodic repeating cycle!";
            }} else {{
                strEl.textContent = "7 / 75";
                facEl.textContent = "3¹ × 5² (Contains prime 3!)";
                badgeCard.className = "p-4 rounded-xl bg-rose-950/80 border border-rose-500 text-center space-y-2";
                statusEl.className = "px-2.5 py-1 rounded text-xs font-black bg-rose-600 text-white uppercase tracking-wider";
                statusEl.textContent = "✗ NON-TERMINATING RECURRING";
                placesEl.textContent = "Prime 3 ≠ 2 and ≠ 5 prevents terminating";
                valEl.textContent = "7 / 75 = 0.09333...";
                ruleEl.textContent = "Prime factor 3 creates an infinite recurring decimal 0.093̅.";
            }}
        }}

        // Sim 8
        const sim8Steps = [
            {{ q: "0.", step: "Step 0: 1 ÷ 7 (dividend 10)", rem: "1", node: "1" }},
            {{ q: "0.1", step: "10 ÷ 7 = 1, remainder = 3", rem: "3", node: "3" }},
            {{ q: "0.14", step: "30 ÷ 7 = 4, remainder = 2", rem: "2", node: "2" }},
            {{ q: "0.142", step: "20 ÷ 7 = 2, remainder = 6", rem: "6", node: "6" }},
            {{ q: "0.1428", step: "60 ÷ 7 = 8, remainder = 4", rem: "4", node: "4" }},
            {{ q: "0.14285", step: "40 ÷ 7 = 5, remainder = 5", rem: "5", node: "5" }},
            {{ q: "0.142857", step: "50 ÷ 7 = 7, remainder = 1 (Repeats!)", rem: "1", node: "1" }},
            {{ q: "0.1428571...", step: "Cycle repeats forever! Periodicity = 6", rem: "3", node: "3" }}
        ];
        let sim8Idx = 0;

        function stepSim8Division() {{
            sim8Idx = (sim8Idx + 1) % sim8Steps.length;
            playTone(450 + sim8Idx * 40, 'sine', 0.08);
            const cur = sim8Steps[sim8Idx];

            document.getElementById('sim8-quotient').textContent = cur.q;
            document.getElementById('sim8-step-text').textContent = cur.step;
            document.getElementById('sim8-rem-text').textContent = `Current Remainder: ${{cur.rem}}`;
            document.getElementById('sim8-status-text').textContent = `Periodicity counter: ${{Math.min(sim8Idx, 6)}} / 6`;

            ['3', '2', '6', '4', '5', '1'].forEach(id => {{
                const el = document.getElementById(`sim8-node-${{id}}`);
                if (el) {{
                    if (id === cur.node) {{
                        el.setAttribute('fill', '#f59e0b');
                        el.setAttribute('stroke', '#fde68a');
                    }} else {{
                        el.setAttribute('fill', '#1e293b');
                        el.setAttribute('stroke', '#64748b');
                    }}
                }}
            }});
        }}

        function resetSim8() {{
            sim8Idx = -1;
            stepSim8Division();
        }}

        // Sim 9
        function setSim9Example(ex) {{
            playTone(520, 'sine', 0.08);
            ['03', '047', '027', '09'].forEach(k => {{
                document.getElementById(`sim9-btn-${{k}}`).className = 'px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300 hover:bg-slate-700';
            }});

            const s1 = document.getElementById('sim9-step1');
            const s2 = document.getElementById('sim9-step2');
            const s3 = document.getElementById('sim9-step3');
            const s4 = document.getElementById('sim9-step4');

            if (ex === '0.3bar') {{
                document.getElementById('sim9-btn-03').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                s1.textContent = "Step 1: Let x = 0.3333...  (Eq 1)";
                s2.textContent = "Step 2: Multiply by 10 ➔ 10x = 3.3333...  (Eq 2)";
                s3.textContent = "Step 3: 10x - x = 3.333... - 0.333... ➔ 9x = 3";
                s4.textContent = "Result: x = 3/9 = 1/3 (Rational!)";
            }} else if (ex === '0.47bar') {{
                document.getElementById('sim9-btn-047').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                s1.textContent = "Step 1: Let x = 0.474747...  (Eq 1)";
                s2.textContent = "Step 2: Multiply by 100 ➔ 100x = 47.4747...  (Eq 2)";
                s3.textContent = "Step 3: 100x - x = 47.4747... - 0.4747... ➔ 99x = 47";
                s4.textContent = "Result: x = 47/99 (Rational!)";
            }} else if (ex === '0.27bar') {{
                document.getElementById('sim9-btn-027').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                s1.textContent = "Step 1: Let x = 0.2777...  (Eq 1)";
                s2.textContent = "Step 2: 10x = 2.777... and 100x = 27.777...";
                s3.textContent = "Step 3: 100x - 10x = 27 - 2 ➔ 90x = 25";
                s4.textContent = "Result: x = 25/90 = 5/18 (Rational!)";
            }} else {{
                document.getElementById('sim9-btn-09').className = 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white';
                s1.textContent = "Step 1: Let x = 0.9999...  (Eq 1)";
                s2.textContent = "Step 2: Multiply by 10 ➔ 10x = 9.9999...  (Eq 2)";
                s3.textContent = "Step 3: 10x - x = 9.999... - 0.999... ➔ 9x = 9";
                s4.textContent = "Result: x = 9/9 = 1 (Exactly 1!)";
            }}
        }}

        // Sim 10
        function sortSim10(id, target) {{
            const btn = document.getElementById(`s10-${{id}}`);
            if (!btn) return;
            playCorrectSound();
            btn.classList.add('hidden');

            const pill = document.createElement('span');
            pill.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-slate-900 border text-slate-200";

            if (target === 'rational') {{
                pill.classList.add('border-sky-500');
                pill.textContent = btn.textContent;
                document.getElementById('sim10-box-rational').appendChild(pill);
            }} else {{
                pill.classList.add('border-rose-500');
                pill.textContent = btn.textContent;
                document.getElementById('sim10-box-irrational').appendChild(pill);
            }}

            document.getElementById('sim10-feedback').textContent = `Correct! ${{btn.textContent}} belongs in ${{target.toUpperCase()}}.`;
        }}

        function resetSim10() {{
            playTone(400, 'sine', 0.08);
            document.querySelectorAll('#sim10-tokens button').forEach(b => b.classList.remove('hidden'));
            document.getElementById('sim10-box-rational').innerHTML = '';
            document.getElementById('sim10-box-irrational').innerHTML = '';
            document.getElementById('sim10-feedback').textContent = "Click each number above to classify it!";
        }}

        // Sim 11
        let sim11Step = 1;
        function advanceSim11() {{
            sim11Step = (sim11Step % 4) + 1;
            playTone(450 + sim11Step * 40, 'sine', 0.1);

            for (let i = 1; i <= 4; i++) {{
                const el = document.getElementById(`sim11-step-${{i}}`);
                if (i <= sim11Step) {{
                    el.className = "p-2 rounded-lg bg-slate-900 border border-amber-500 text-amber-300";
                }} else {{
                    el.className = "p-2 rounded-lg bg-slate-900/40 border border-slate-800 text-slate-500";
                }}
            }}

            const t = document.getElementById('sim11-title');
            const d = document.getElementById('sim11-desc');
            if (sim11Step === 1) {{
                t.textContent = "Step 1: Assumption";
                d.textContent = "Assume √2 = a/b where gcd(a, b) = 1 (co-prime).";
            }} else if (sim11Step === 2) {{
                t.textContent = "Step 2: Squaring";
                d.textContent = "2b² = a² implies a² is even, hence a is even: a = 2k.";
            }} else if (sim11Step === 3) {{
                t.textContent = "Step 3: Substitution";
                d.textContent = "2b² = (2k)² = 4k² implies b² = 2k², so b is also even!";
            }} else {{
                t.textContent = "Step 4: Contradiction & Conclusion";
                d.textContent = "Both a and b are even, so 2 divides both. This contradicts gcd(a, b) = 1. Therefore √2 is irrational!";
            }}
        }}

        // Sim 12
        let sim12Step = 1;
        function advanceSim12() {{
            sim12Step = (sim12Step % 4) + 1;
            playTone(480 + sim12Step * 40, 'sine', 0.1);

            for (let i = 1; i <= 4; i++) {{
                const el = document.getElementById(`sim12-step-${{i}}`);
                if (i <= sim12Step) {{
                    el.className = "p-2 rounded-lg bg-slate-900 border border-amber-500 text-amber-300";
                }} else {{
                    el.className = "p-2 rounded-lg bg-slate-900/40 border border-slate-800 text-slate-500";
                }}
            }}

            const t = document.getElementById('sim12-title');
            const d = document.getElementById('sim12-desc');
            if (sim12Step === 1) {{
                t.textContent = "Step 1: Assumption";
                d.textContent = "Assume √3 = a/b with gcd(a, b) = 1 (co-prime).";
            }} else if (sim12Step === 2) {{
                t.textContent = "Step 2: Divisibility by 3";
                d.textContent = "3b² = a² implies 3 divides a. Substitute a = 3m.";
            }} else if (sim12Step === 3) {{
                t.textContent = "Step 3: Second Divisibility";
                d.textContent = "3b² = 9m² implies b² = 3m², so 3 divides b.";
            }} else {{
                t.textContent = "Step 4: Contradiction & Conclusion";
                d.textContent = "3 divides both a and b, contradicting co-primality. Hence √3 is irrational!";
            }}
        }}

        // Sim 13
        function animateSim13Compass() {{
            playTone(300, 'sawtooth', 0.25);
            setTimeout(() => playTone(550, 'sine', 0.15), 300);

            document.getElementById('sim13-arc').classList.remove('hidden');
            document.getElementById('sim13-point-p').classList.remove('hidden');

            document.getElementById('sim13-status').textContent = "Compass Arc Constructed:";
            document.getElementById('sim13-desc').textContent = "Point P is marked at distance √2 ≈ 1.414 from origin O on the real number line!";
        }}

        function resetSim13() {{
            playTone(400, 'sine', 0.08);
            document.getElementById('sim13-arc').classList.add('hidden');
            document.getElementById('sim13-point-p').classList.add('hidden');
            document.getElementById('sim13-status').textContent = "Pythagorean Construction:";
            document.getElementById('sim13-desc').textContent = "Right triangle with base 1 and height 1 produces hypotenuse √2. Ready to swing compass.";
        }}

        // Sim 14
        let spiralRoot = 2;
        function addSpiralStep() {{
            if (spiralRoot >= 10) return;
            spiralRoot++;
            playTone(400 + spiralRoot * 35, 'sine', 0.08);
            renderSpiral();
        }}

        function resetSpiral() {{
            spiralRoot = 2;
            playTone(400, 'sine', 0.08);
            renderSpiral();
        }}

        function renderSpiral() {{
            const group = document.getElementById('sim14-spiral-group');
            group.innerHTML = '';

            const cx = 250;
            const cy = 120;
            const unitLen = 45;

            let prevX = cx + unitLen;
            let prevY = cy;

            // Initial unit leg
            const baseLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            baseLine.setAttribute('x1', cx); baseLine.setAttribute('y1', cy);
            baseLine.setAttribute('x2', prevX); baseLine.setAttribute('y2', prevY);
            baseLine.setAttribute('stroke', '#64748b'); baseLine.setAttribute('stroke-width', '2');
            group.appendChild(baseLine);

            for (let n = 1; n < spiralRoot; n++) {{
                const currentAngle = Math.atan2(prevY - cy, prevX - cx);
                const perpAngle = currentAngle + Math.PI / 2;

                const nextX = prevX + unitLen * Math.cos(perpAngle);
                const nextY = prevY + unitLen * Math.sin(perpAngle);

                // Perpendicular leg
                const perp = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                perp.setAttribute('x1', prevX); perp.setAttribute('y1', prevY);
                perp.setAttribute('x2', nextX); perp.setAttribute('y2', nextY);
                perp.setAttribute('stroke', '#38bdf8'); perp.setAttribute('stroke-width', '2');
                group.appendChild(perp);

                // Hypotenuse
                const hyp = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                hyp.setAttribute('x1', cx); hyp.setAttribute('y1', cy);
                hyp.setAttribute('x2', nextX); hyp.setAttribute('y2', nextY);
                hyp.setAttribute('stroke', '#f59e0b'); hyp.setAttribute('stroke-width', '2');
                group.appendChild(hyp);

                // Label
                const lbl = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                lbl.setAttribute('x', nextX + 5);
                lbl.setAttribute('y', nextY);
                lbl.setAttribute('fill', '#fef08a');
                lbl.setAttribute('font-size', '9');
                lbl.setAttribute('font-weight', 'bold');
                lbl.textContent = `√${{n + 1}}`;
                group.appendChild(lbl);

                prevX = nextX;
                prevY = nextY;
            }}

            document.getElementById('sim14-caption').textContent = `Currently showing ${{spiralRoot - 1}} connected right triangles up to √${{spiralRoot}}!`;
        }}

        // Sim 15
        function setSim15Expr(type) {{
            playTone(520, 'sine', 0.08);
            [1, 2, 3].forEach(i => {{
                document.getElementById(`sim15-btn-${{i}}`).className = (i === type) ? 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white' : 'px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300 hover:bg-slate-700';
            }});

            const o = document.getElementById('sim15-original');
            const s1 = document.getElementById('sim15-step1');
            const s2 = document.getElementById('sim15-step2');
            const res = document.getElementById('sim15-result');

            if (type === 1) {{
                o.textContent = "Original Fraction: 1 / (√7 - 2)";
                s1.textContent = "Multiply by conjugate (√7 + 2): [1 × (√7 + 2)] / [(√7 - 2)(√7 + 2)]";
                s2.textContent = "Difference of squares in denominator: (√7)² - 2² = 7 - 4 = 3";
                res.textContent = "Rationalised Result: (√7 + 2) / 3";
            }} else if (type === 2) {{
                o.textContent = "Original Fraction: 1 / (√5 + √2)";
                s1.textContent = "Multiply by conjugate (√5 - √2): [1 × (√5 - √2)] / [(√5 + √2)(√5 - √2)]";
                s2.textContent = "Difference of squares: (√5)² - (√2)² = 5 - 2 = 3";
                res.textContent = "Rationalised Result: (√5 - √2) / 3";
            }} else {{
                o.textContent = "Original Fraction: 1 / √3";
                s1.textContent = "Multiply numerator and denominator by √3: (1 × √3) / (√3 × √3)";
                s2.textContent = "Denominator becomes: (√3)² = 3";
                res.textContent = "Rationalised Result: √3 / 3";
            }}
        }}

        // Sim 16
        function setSim16Rule(r) {{
            playTone(540, 'sine', 0.08);
            ['prod', 'quot', 'pow', 'frac'].forEach(k => {{
                document.getElementById(`sim16-btn-${{k}}`).className = (k === r) ? 'px-2 py-0.5 rounded font-bold bg-indigo-600 text-white' : 'px-2 py-0.5 rounded font-bold bg-slate-800 text-slate-300 hover:bg-slate-700';
            }});

            const nm = document.getElementById('sim16-rule-name');
            const cl = document.getElementById('sim16-calc');
            const out = document.getElementById('sim16-output');

            if (r === 'prod') {{
                nm.textContent = "Product with Same Base: a^m × a^n = a^(m + n)";
                cl.textContent = "Example: 2^(2/3) × 2^(1/3) = 2^(2/3 + 1/3) = 2^(3/3)";
                out.textContent = "Simplified Value: 2¹ = 2";
            }} else if (r === 'quot') {{
                nm.textContent = "Quotient with Same Base: a^m / a^n = a^(m - n)";
                cl.textContent = "Example: 11^(1/2) / 11^(1/4) = 11^(2/4 - 1/4) = 11^(1/4)";
                out.textContent = "Simplified Value: 11^(1/4) = ⁴√11";
            }} else if (r === 'pow') {{
                nm.textContent = "Power of a Power: (a^m)^n = a^(m × n)";
                cl.textContent = "Example: (3^(1/5))^4 = 3^(1/5 × 4) = 3^(4/5)";
                out.textContent = "Simplified Value: ⁵√(3⁴) = ⁵√81";
            }} else {{
                nm.textContent = "Fractional Exponent Definition: a^(m/n) = ⁿ√(a^m)";
                cl.textContent = "Example: 125^(-1/3) = 1 / (125^(1/3)) = 1 / ³√125";
                out.textContent = "Simplified Value: 1 / 5 = 0.2";
            }}
        }}

        window.addEventListener('DOMContentLoaded', () => {{
            generateSlidePills();
            showSlide(0);
            updateSim3();
            renderSpiral();
        }});
    </script>
</body>
</html>
"""
    return full_html


if __name__ == "__main__":
    html_output = build_full_html()
    target_path = "public/animations/number-system.html"
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html_output)
    print(f"Successfully generated {target_path} ({len(html_output)} bytes)")
