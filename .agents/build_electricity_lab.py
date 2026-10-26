#!/usr/bin/env python3
"""
Full Generator for NCERT Class 10 Science, Chapter 11: Electricity
Master Interactive Multimedia Lab
File: public/animations/electricity.html
"""

import json
import os
import sys

sys.path.append(os.path.abspath('.agents'))
from electricity_data import CONTENT_SLIDES, QUIZ_SLIDES

ALL_SLIDES = CONTENT_SLIDES + QUIZ_SLIDES

def get_simulator_markup(s_idx):
    """Generate high-yield interactive SVG laboratory simulators for all 18 content slides."""
    if s_idx == 0:
        # Slide 1: Electric Circuit & Marching Electron Flow
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 11.1: Closed Circuit & Charge Carrier Flow
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="toggleSim1Switch()" id="btn-sim1-switch" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition flex items-center gap-1.5">
                        <span id="sim1-switch-dot" class="w-2 h-2 rounded-full bg-white animate-pulse"></span>
                        <span id="sim1-switch-text">Switch: CLOSED (Current ON)</span>
                    </button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <svg id="svg-sim1" viewBox="0 0 500 220" class="w-full max-w-lg h-auto">
                    <!-- Circuit Loop Wire Path -->
                    <rect x="70" y="30" width="360" height="150" rx="14" fill="none" stroke="#475569" stroke-width="4"/>
                    
                    <!-- Battery / Cell at Bottom (250, 180) -->
                    <g transform="translate(230, 165)">
                        <rect x="-30" y="-8" width="60" height="30" fill="#0f172a" stroke="#0f172a"/>
                        <!-- Long positive plate -->
                        <line x1="-8" y1="-5" x2="-8" y2="25" stroke="#f59e0b" stroke-width="4"/>
                        <text x="-16" y="5" fill="#f59e0b" font-size="10" font-weight="bold">+</text>
                        <!-- Short thick negative plate -->
                        <line x1="8" y1="0" x2="8" y2="20" stroke="#94a3b8" stroke-width="6"/>
                        <text x="16" y="5" fill="#94a3b8" font-size="10" font-weight="bold">-</text>
                        <text x="0" y="34" fill="#cbd5e1" font-size="9" text-anchor="middle">Cell (1.5 V)</text>
                    </g>

                    <!-- Switch Key at Right (430, 105) -->
                    <g id="sim1-key-group" transform="translate(430, 105)">
                        <rect x="-10" y="-20" width="20" height="40" fill="#0f172a"/>
                        <circle cx="0" cy="-12" r="3.5" fill="#38bdf8"/>
                        <circle cx="0" cy="12" r="3.5" fill="#38bdf8"/>
                        <line id="sim1-key-blade" x1="0" y1="-12" x2="0" y2="12" stroke="#38bdf8" stroke-width="3"/>
                        <text x="14" y="4" fill="#38bdf8" font-size="8">Key (K)</text>
                    </g>

                    <!-- Electric Bulb at Top (250, 30) -->
                    <g id="sim1-bulb-group" transform="translate(250, 30)">
                        <circle id="sim1-bulb-glow" cx="0" cy="0" r="22" fill="#fbbf24" fill-opacity="0.35" filter="drop-shadow(0 0 12px #f59e0b)"/>
                        <circle cx="0" cy="0" r="14" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                        <!-- Filament -->
                        <path id="sim1-filament" d="M -6 4 Q 0 -10 6 4" fill="none" stroke="#fef08a" stroke-width="2.5"/>
                        <text x="0" y="-18" fill="#fef08a" font-size="8" text-anchor="middle" font-weight="bold">Electric Bulb</text>
                    </g>

                    <!-- Ammeter on Left (70, 105) -->
                    <g transform="translate(70, 105)">
                        <circle cx="0" cy="0" r="16" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
                        <text x="0" y="4" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">A</text>
                        <text x="-25" y="4" fill="#ec4899" font-size="8" text-anchor="middle">Ammeter</text>
                    </g>

                    <!-- Current Direction Arrows (Conventional: + to - clockwise) -->
                    <g id="sim1-conv-arrows">
                        <polygon points="170,180 160,175 160,185" fill="#f59e0b"/>
                        <polygon points="70,70 65,80 75,80" fill="#f59e0b"/>
                        <polygon points="340,30 350,25 350,35" fill="#f59e0b"/>
                        <polygon points="430,140 435,130 425,130" fill="#f59e0b"/>
                        <text x="340" y="46" fill="#f59e0b" font-size="8" font-weight="bold">Conventional Current (I) →</text>
                    </g>

                    <!-- Electrons (Drifting opposite: - to + counter-clockwise) -->
                    <g id="sim1-electrons">
                        <circle cx="120" cy="30" r="3" fill="#38bdf8"/>
                        <circle cx="180" cy="30" r="3" fill="#38bdf8"/>
                        <circle cx="310" cy="30" r="3" fill="#38bdf8"/>
                        <circle cx="390" cy="30" r="3" fill="#38bdf8"/>
                        <circle cx="430" cy="65" r="3" fill="#38bdf8"/>
                        <circle cx="430" cy="155" r="3" fill="#38bdf8"/>
                        <circle cx="350" cy="180" r="3" fill="#38bdf8"/>
                        <circle cx="140" cy="180" r="3" fill="#38bdf8"/>
                        <circle cx="70" cy="145" r="3" fill="#38bdf8"/>
                        <circle cx="70" cy="60" r="3" fill="#38bdf8"/>
                    </g>
                </svg>
                <div id="sim1-desc" class="text-xs text-amber-200 mt-2 text-center font-medium">
                    Continuous closed circuit: Electrons drift counter-clockwise from negative to positive terminal; conventional current flows clockwise from positive to negative. Bulb glows!
                </div>
            </div>
        </div>
        """
    elif s_idx == 1:
        # Slide 2: Coulomb, Ampere & Ammeter in Series
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 11.2: Charge Flow & Coulomb Engine (Q = I × t)
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300 font-semibold">Current (I):</label>
                    <input type="range" id="sim2-current" min="0.1" max="2.0" step="0.1" value="0.5" oninput="updateSim2Charge()" class="w-24 sm:w-32 accent-cyan-400 cursor-pointer">
                    <span id="sim2-curr-val" class="text-xs font-mono font-bold text-cyan-400">0.5 A</span>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 w-full max-w-lg mb-3">
                    <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-center">
                        <span class="text-[10px] text-slate-400 block uppercase">Time Duration (t)</span>
                        <input type="range" id="sim2-time" min="60" max="1200" step="60" value="600" oninput="updateSim2Charge()" class="w-full accent-indigo-400 cursor-pointer mt-1">
                        <span id="sim2-time-val" class="text-xs font-mono font-bold text-indigo-300">10 min (600 s)</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-center">
                        <span class="text-[10px] text-slate-400 block uppercase">Net Charge (Q = It)</span>
                        <span id="sim2-q-val" class="text-sm sm:text-base font-mono font-bold text-amber-400">300 C</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-center col-span-2">
                        <span class="text-[10px] text-slate-400 block uppercase">Number of Electrons (n = Q/e)</span>
                        <span id="sim2-n-val" class="text-xs sm:text-sm font-mono font-bold text-emerald-400">1.88 × 10²¹ electrons</span>
                    </div>
                </div>
                <!-- Interactive Digital Ammeter Face -->
                <div class="flex items-center gap-4 bg-slate-900 px-6 py-3 rounded-2xl border border-cyan-500/30">
                    <div class="w-10 h-10 rounded-full bg-cyan-500/20 border border-cyan-500 flex items-center justify-center font-bold text-cyan-400">A</div>
                    <div>
                        <div class="text-[10px] text-slate-400 uppercase tracking-wider font-semibold">Series Ammeter Reading</div>
                        <div id="sim2-ammeter-display" class="text-xl sm:text-2xl font-mono font-extrabold text-cyan-300">0.50 A</div>
                    </div>
                </div>
                <div id="sim2-desc" class="text-xs text-cyan-200 mt-2 text-center font-medium">
                    Example 11.1 parameters: 0.5 A for 10 minutes (600 seconds) drives 300 Coulombs of charge, equivalent to 1.88 × 10²¹ electrons flowing in series!
                </div>
            </div>
        </div>
        """
    elif s_idx == 2:
        # Slide 3: Potential Difference (V = W/Q) & Water Analogy
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 11.3: Electric Pressure & Work Done (V = W / Q)
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300 font-semibold">Potential Diff (V):</label>
                    <input type="range" id="sim3-volt" min="1.5" max="24" step="1.5" value="12" oninput="updateSim3Potential()" class="w-24 sm:w-32 accent-rose-400 cursor-pointer">
                    <span id="sim3-volt-val" class="text-xs font-mono font-bold text-rose-400">12 V</span>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full max-w-lg mb-2">
                    <!-- Hydraulic Analogy Visual -->
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center">
                        <span class="text-[10px] text-sky-400 uppercase font-bold mb-1">Water Pressure Analogy</span>
                        <svg viewBox="0 0 200 110" class="w-full h-auto">
                            <!-- Elevated Tank -->
                            <rect x="20" y="15" width="45" height="50" rx="3" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
                            <rect id="sim3-water-level" x="22" y="25" width="41" height="38" fill="#38bdf8" fill-opacity="0.7"/>
                            <text x="42" y="45" fill="#ffffff" font-size="7" text-anchor="middle">Water Tank</text>
                            <!-- Pipe with flow -->
                            <path d="M 65 60 L 150 60 L 150 90" fill="none" stroke="#38bdf8" stroke-width="4"/>
                            <polygon points="150,92 146,84 154,84" fill="#38bdf8"/>
                            <text x="110" y="52" fill="#94a3b8" font-size="7">Pressure Head (ΔP)</text>
                        </svg>
                        <span class="text-[10px] text-slate-400 text-center">Height difference drives water flow</span>
                    </div>

                    <!-- Work Done Calculator -->
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 flex flex-col justify-center space-y-2">
                        <div class="flex justify-between text-xs text-slate-300">
                            <span>Charge to Move (Q):</span>
                            <div class="flex items-center gap-1">
                                <input type="number" id="sim3-charge" value="2" min="1" max="10" oninput="updateSim3Potential()" class="w-14 bg-slate-950 border border-slate-700 text-center rounded text-xs font-mono text-white p-0.5">
                                <span>C</span>
                            </div>
                        </div>
                        <div class="flex justify-between text-xs text-slate-300">
                            <span>Formula:</span>
                            <span class="font-mono text-cyan-400 font-bold">W = V × Q</span>
                        </div>
                        <div class="p-2.5 rounded-lg bg-rose-950/40 border border-rose-500/30 text-center">
                            <span class="text-[10px] text-slate-400 block uppercase">Work Done (W)</span>
                            <span id="sim3-work-val" class="text-lg font-mono font-extrabold text-rose-300">24 Joules</span>
                        </div>
                    </div>
                </div>
                <div id="sim3-desc" class="text-xs text-rose-200 mt-1 text-center font-medium">
                    Example 11.2: Moving a 2 C charge across a 12 V potential difference requires W = 12 V × 2 C = 24 Joules of electrical work!
                </div>
            </div>
        </div>
        """
    elif s_idx == 3:
        # Slide 4: Interactive Circuit Schematic Symbols
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-purple-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-purple-400"></span>
                    Interactive Lab 11.4: Universal Circuit Schematic Symbol Palette
                </span>
                <span class="text-[10px] text-slate-400 font-mono">NCERT Table 11.1</span>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 mb-3">
                <button onclick="setSim4Symbol('cell')" id="btn-sym-cell" class="p-2 rounded-xl text-xs font-bold bg-purple-600 text-white transition">Cell / Battery</button>
                <button onclick="setSim4Symbol('key')" id="btn-sym-key" class="p-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Plug Key</button>
                <button onclick="setSim4Symbol('res')" id="btn-sym-res" class="p-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Resistor / Rheostat</button>
                <button onclick="setSim4Symbol('meters')" id="btn-sym-meters" class="p-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Meters (A / V)</button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-4 border border-slate-800 min-h-[140px] flex items-center justify-center">
                <div id="sim4-preview" class="w-full flex flex-col items-center">
                    <svg viewBox="0 0 340 70" class="w-full max-w-sm h-auto">
                        <!-- Electric Cell -->
                        <line x1="40" y1="35" x2="100" y2="35" stroke="#94a3b8" stroke-width="2"/>
                        <line x1="100" y1="15" x2="100" y2="55" stroke="#f59e0b" stroke-width="4"/>
                        <line x1="115" y1="22" x2="115" y2="48" stroke="#64748b" stroke-width="6"/>
                        <line x1="115" y1="35" x2="175" y2="35" stroke="#94a3b8" stroke-width="2"/>
                        <text x="94" y="25" fill="#f59e0b" font-size="9" font-weight="bold">+</text>
                        <text x="122" y="25" fill="#94a3b8" font-size="9" font-weight="bold">-</text>
                        <!-- Battery -->
                        <line x1="185" y1="35" x2="215" y2="35" stroke="#94a3b8" stroke-width="2"/>
                        <line x1="215" y1="15" x2="215" y2="55" stroke="#f59e0b" stroke-width="3"/>
                        <line x1="225" y1="22" x2="225" y2="48" stroke="#64748b" stroke-width="5"/>
                        <line x1="235" y1="15" x2="235" y2="55" stroke="#f59e0b" stroke-width="3"/>
                        <line x1="245" y1="22" x2="245" y2="48" stroke="#64748b" stroke-width="5"/>
                        <line x1="245" y1="35" x2="300" y2="35" stroke="#94a3b8" stroke-width="2"/>
                    </svg>
                    <span class="text-xs text-purple-200 mt-2 font-medium">Single Electric Cell (Left) vs Multi-cell Battery (Right)</span>
                </div>
            </div>
        </div>
        """
    elif s_idx == 4:
        # Slide 5: Ohm's Law & V–I Slope Simulator
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                    Interactive Lab 11.5: Ohm's Law V–I Characteristic Plotter
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300 font-semibold">Voltage (V):</label>
                    <input type="range" id="sim5-volt" min="0" max="15" step="0.5" value="6.0" oninput="updateSim5Ohm()" class="w-24 sm:w-32 accent-emerald-400 cursor-pointer">
                    <span id="sim5-volt-val" class="text-xs font-mono font-bold text-emerald-400">6.0 V</span>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full max-w-lg mb-2">
                    <!-- Dynamic V-I Graph -->
                    <div class="bg-slate-900 p-2 rounded-xl border border-slate-800 flex flex-col items-center">
                        <svg id="svg-sim5-graph" viewBox="0 0 200 160" class="w-full h-auto">
                            <!-- Axes -->
                            <line x1="30" y1="130" x2="190" y2="130" stroke="#64748b" stroke-width="1.5"/>
                            <text x="185" y="145" fill="#94a3b8" font-size="8">I (A)</text>
                            <line x1="30" y1="130" x2="30" y2="15" stroke="#64748b" stroke-width="1.5"/>
                            <text x="12" y="20" fill="#94a3b8" font-size="8">V (V)</text>
                            <!-- Origin -->
                            <text x="22" y="142" fill="#64748b" font-size="7">0</text>
                            <!-- Linear Slope Line -->
                            <line x1="30" y1="130" x2="180" y2="25" stroke="#10b981" stroke-width="2" stroke-dasharray="3,3"/>
                            <!-- Active Operating Point -->
                            <circle id="sim5-point" cx="105" cy="77" r="4.5" fill="#f59e0b" filter="drop-shadow(0 0 6px #f59e0b)"/>
                            <line id="sim5-v-proj" x1="30" y1="77" x2="105" y2="77" stroke="#f59e0b" stroke-width="1" stroke-dasharray="2,2"/>
                            <line id="sim5-i-proj" x1="105" y1="77" x2="105" y2="130" stroke="#f59e0b" stroke-width="1" stroke-dasharray="2,2"/>
                        </svg>
                        <span class="text-[10px] text-slate-400">Straight line passing through (0, 0)</span>
                    </div>

                    <!-- Readings Panel -->
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 flex flex-col justify-center space-y-2.5">
                        <div class="flex justify-between items-center text-xs text-slate-300">
                            <span>Resistance (R):</span>
                            <div class="flex items-center gap-1.5">
                                <input type="range" id="sim5-res" min="2" max="10" step="1" value="4" oninput="updateSim5Ohm()" class="w-20 accent-amber-400">
                                <span id="sim5-res-val" class="font-mono text-amber-400 font-bold">4.0 Ω</span>
                            </div>
                        </div>
                        <div class="flex justify-between text-xs text-slate-300">
                            <span>Calculated Current (I = V/R):</span>
                            <span id="sim5-curr-val" class="font-mono text-emerald-400 font-bold text-sm">1.50 A</span>
                        </div>
                        <div class="p-2 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-xs text-center font-mono">
                            Slope = ΔV / ΔI = <span id="sim5-slope-val" class="font-bold text-white">4.00 Ω</span> (Constant)
                        </div>
                    </div>
                </div>
                <div id="sim5-desc" class="text-xs text-emerald-200 mt-1 text-center font-medium">
                    Linear V–I Relationship: As voltage increases, current increases proportionally. The slope of the line equals the resistance R.
                </div>
            </div>
        </div>
        """
    elif s_idx == 5:
        # Slide 6: Microscopic Resistance & Atomic Collisions
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-sky-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-sky-400"></span>
                    Interactive Lab 11.6: Microscopic Electron Scattering Simulator
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim6Material('conductor')" id="btn-sim6-cond" class="px-2.5 py-1 rounded text-xs font-bold bg-sky-600 text-white transition">Good Conductor (Cu)</button>
                    <button onclick="setSim6Material('resistor')" id="btn-sim6-res" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Resistor (Nichrome)</button>
                    <button onclick="setSim6Material('insulator')" id="btn-sim6-ins" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Insulator (Rubber)</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim6" viewBox="0 0 480 160" class="w-full max-w-lg h-auto">
                    <!-- Metal Lattice Tube -->
                    <rect x="30" y="20" width="420" height="120" rx="8" fill="#0f172a" stroke="#475569" stroke-width="2"/>
                    <!-- Lattice positive ions -->
                    <g id="sim6-lattice-ions" fill="#64748b">
                        <circle cx="80" cy="50" r="10"/><circle cx="160" cy="50" r="10"/><circle cx="240" cy="50" r="10"/><circle cx="320" cy="50" r="10"/><circle cx="400" cy="50" r="10"/>
                        <circle cx="80" cy="110" r="10"/><circle cx="160" cy="110" r="10"/><circle cx="240" cy="110" r="10"/><circle cx="320" cy="110" r="10"/><circle cx="400" cy="110" r="10"/>
                    </g>
                    <!-- Electron drift path -->
                    <path id="sim6-electron-path" d="M 40 80 Q 80 70 120 85 T 200 75 T 280 85 T 360 75 L 440 80" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,2"/>
                    <circle cx="440" cy="80" r="4" fill="#38bdf8"/>
                    <text x="440" y="98" fill="#38bdf8" font-size="8" text-anchor="middle">e⁻ Drift</text>
                </svg>
                <div id="sim6-desc" class="text-xs text-sky-200 mt-2 text-center font-medium">
                    Good Conductor (Copper): Low atomic collision rate allows high drift velocity and effortless charge flow.
                </div>
            </div>
        </div>
        """
    elif s_idx == 6:
        # Slide 7: Conductor Resistance Factors (Length l & Area A)
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 11.7: Geometry Engine: R = ρ · (l / A)
                </span>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-mono font-bold text-amber-400">Activity 11.3</span>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full max-w-lg mb-2">
                    <!-- Controls -->
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 space-y-3">
                        <div>
                            <div class="flex justify-between text-xs text-slate-300 font-semibold mb-1">
                                <span>Conductor Length (l):</span>
                                <span id="sim7-l-val" class="text-amber-400 font-mono">1.0 m</span>
                            </div>
                            <input type="range" id="sim7-len" min="0.5" max="3.0" step="0.5" value="1.0" oninput="updateSim7Wire()" class="w-full accent-amber-400 cursor-pointer">
                        </div>
                        <div>
                            <div class="flex justify-between text-xs text-slate-300 font-semibold mb-1">
                                <span>Diameter / Thickness (d):</span>
                                <span id="sim7-d-val" class="text-cyan-400 font-mono">0.5 mm</span>
                            </div>
                            <input type="range" id="sim7-dia" min="0.2" max="1.0" step="0.1" value="0.5" oninput="updateSim7Wire()" class="w-full accent-cyan-400 cursor-pointer">
                        </div>
                    </div>

                    <!-- Live Graphical Wire & Resistance Output -->
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 flex flex-col items-center justify-center">
                        <svg viewBox="0 0 200 70" class="w-full h-auto mb-2">
                            <rect id="sim7-wire-rect" x="30" y="28" width="140" height="14" rx="3" fill="#f59e0b" stroke="#fcd34d" stroke-width="1.5"/>
                            <text x="100" y="40" fill="#0f172a" font-size="8" text-anchor="middle" font-weight="bold">Wire Geometry</text>
                        </svg>
                        <div class="text-center">
                            <span class="text-[10px] text-slate-400 block uppercase">Calculated Resistance (R)</span>
                            <span id="sim7-r-val" class="text-lg font-mono font-extrabold text-amber-300">5.09 Ω</span>
                        </div>
                    </div>
                </div>
                <div id="sim7-desc" class="text-xs text-amber-200 mt-1 text-center font-medium">
                    R ∝ l and R ∝ 1/A: Doubling length doubles resistance; doubling diameter increases area by 4× and quarters resistance!
                </div>
            </div>
        </div>
        """
    elif s_idx == 7:
        # Slide 8: Resistivity Spectrum: Conductors, Alloys & Insulators
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 11.8: Resistivity Spectrum & High-Temp Alloy Heating
                </span>
                <span class="text-[10px] text-slate-400 font-mono">NCERT Table 11.2</span>
            </div>
            <div class="grid grid-cols-3 sm:grid-cols-6 gap-2 mb-3">
                <button onclick="setSim8Mat('silver')" id="btn-mat-silver" class="p-2 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Silver</button>
                <button onclick="setSim8Mat('copper')" id="btn-mat-copper" class="p-2 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Copper</button>
                <button onclick="setSim8Mat('tungsten')" id="btn-mat-tungsten" class="p-2 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Tungsten</button>
                <button onclick="setSim8Mat('nichrome')" id="btn-mat-nichrome" class="p-2 rounded-lg text-xs font-bold bg-rose-600 text-white">Nichrome</button>
                <button onclick="setSim8Mat('glass')" id="btn-mat-glass" class="p-2 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Glass</button>
                <button onclick="setSim8Mat('rubber')" id="btn-mat-rubber" class="p-2 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Rubber</button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center">
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 w-full max-w-lg text-center mb-2">
                    <div class="p-2 bg-slate-900 rounded-lg">
                        <span class="text-[10px] text-slate-400 block uppercase">Resistivity (ρ)</span>
                        <span id="sim8-rho-val" class="text-xs font-mono font-bold text-rose-400">100 × 10⁻⁶ Ω·m</span>
                    </div>
                    <div class="p-2 bg-slate-900 rounded-lg">
                        <span class="text-[10px] text-slate-400 block uppercase">Classification</span>
                        <span id="sim8-class-val" class="text-xs font-bold text-amber-300">High-Resistivity Alloy</span>
                    </div>
                    <div class="p-2 bg-slate-900 rounded-lg">
                        <span class="text-[10px] text-slate-400 block uppercase">Primary Application</span>
                        <span id="sim8-app-val" class="text-xs font-bold text-emerald-400">Toasters & Irons</span>
                    </div>
                </div>
                <div id="sim8-desc" class="text-xs text-rose-200 mt-1 text-center font-medium">
                    Nichrome Alloy: High resistivity and resists oxidation at red-hot temperatures—ideal for heating coils!
                </div>
            </div>
        </div>
        """
    elif s_idx == 8:
        # Slide 9: Resistance & Resistivity Numerical Solvers
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 11.9: Examples 11.3 & 11.6 Interactive Solvers
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim9Tab('ex113')" id="btn-sim9-ex113" class="px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 text-white">Example 11.3 (220 V)</button>
                    <button onclick="setSim9Tab('ex116')" id="btn-sim9-ex116" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Example 11.6 (Wire Cut)</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-4 border border-slate-800 flex flex-col items-center justify-center">
                <div id="sim9-content" class="w-full max-w-lg">
                    <!-- Example 11.3 display -->
                    <div class="grid grid-cols-2 gap-3 text-center">
                        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
                            <span class="text-xs font-bold text-amber-400 block mb-1">Electric Bulb Filament</span>
                            <div class="text-[11px] text-slate-300">R = 1200 Ω, V = 220 V</div>
                            <div class="text-base font-mono font-extrabold text-white mt-1">I = 0.18 A</div>
                            <span class="text-[10px] text-slate-500">Draws tiny current</span>
                        </div>
                        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
                            <span class="text-xs font-bold text-rose-400 block mb-1">Electric Heater Coil</span>
                            <div class="text-[11px] text-slate-300">R = 100 Ω, V = 220 V</div>
                            <div class="text-base font-mono font-extrabold text-rose-300 mt-1">I = 2.20 A</div>
                            <span class="text-[10px] text-slate-500">Draws 12× more current!</span>
                        </div>
                    </div>
                </div>
                <div id="sim9-desc" class="text-xs text-cyan-200 mt-3 text-center font-medium">
                    Same 220 V source: Bulb draws only 0.18 A due to high filament resistance, while heater coil draws 2.2 A.
                </div>
            </div>
        </div>
        """
    elif s_idx == 9:
        # Slide 10: Resistors in Series: Derivation & Uniform Current
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                    Interactive Lab 11.10: Series Resistor Chain (Rs = R1 + R2 + R3)
                </span>
                <span class="text-[10px] text-slate-400 font-mono">Activities 11.4 & 11.5</span>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <!-- 3 Series Resistors Circuit Diagram -->
                <svg viewBox="0 0 480 140" class="w-full max-w-lg h-auto mb-2">
                    <!-- Wire Loop -->
                    <path d="M 50 70 L 100 70 M 160 70 L 220 70 M 280 70 L 340 70 M 400 70 L 440 70 L 440 120 L 50 120 Z" fill="none" stroke="#64748b" stroke-width="3"/>
                    <!-- Resistor 1 (100..160) -->
                    <path d="M 100 70 L 108 58 L 120 82 L 132 58 L 144 82 L 152 70" fill="none" stroke="#f59e0b" stroke-width="3"/>
                    <text x="126" y="52" fill="#f59e0b" font-size="9" text-anchor="middle" font-weight="bold">R₁</text>
                    <!-- Resistor 2 (220..280) -->
                    <path d="M 220 70 L 228 58 L 240 82 L 252 58 L 264 82 L 272 70" fill="none" stroke="#38bdf8" stroke-width="3"/>
                    <text x="246" y="52" fill="#38bdf8" font-size="9" text-anchor="middle" font-weight="bold">R₂</text>
                    <!-- Resistor 3 (340..400) -->
                    <path d="M 340 70 L 348 58 L 360 82 L 372 58 L 384 82 L 392 70" fill="none" stroke="#a855f7" stroke-width="3"/>
                    <text x="366" y="52" fill="#a855f7" font-size="9" text-anchor="middle" font-weight="bold">R₃</text>
                    <!-- Battery at Bottom -->
                    <g transform="translate(245, 120)">
                        <line x1="-10" y1="-8" x2="-10" y2="8" stroke="#10b981" stroke-width="4"/>
                        <line x1="10" y1="-5" x2="10" y2="5" stroke="#64748b" stroke-width="6"/>
                        <text x="0" y="20" fill="#cbd5e1" font-size="8" text-anchor="middle">V = 12 V</text>
                    </g>
                    <!-- Ammeter on left -->
                    <circle cx="50" cy="95" r="12" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
                    <text x="50" y="99" fill="#ec4899" font-size="9" text-anchor="middle" font-weight="bold">A</text>
                </svg>
                <!-- Controls for R1, R2, R3 -->
                <div class="grid grid-cols-3 gap-2 w-full max-w-lg mb-2">
                    <div class="p-2 bg-slate-900 rounded-lg text-center">
                        <span class="text-[10px] text-amber-400 font-bold block">R₁: 2.0 Ω</span>
                        <span id="sim10-v1" class="text-xs font-mono text-slate-300">V₁ = 2.4 V</span>
                    </div>
                    <div class="p-2 bg-slate-900 rounded-lg text-center">
                        <span class="text-[10px] text-cyan-400 font-bold block">R₂: 3.0 Ω</span>
                        <span id="sim10-v2" class="text-xs font-mono text-slate-300">V₂ = 3.6 V</span>
                    </div>
                    <div class="p-2 bg-slate-900 rounded-lg text-center">
                        <span class="text-[10px] text-purple-400 font-bold block">R₃: 5.0 Ω</span>
                        <span id="sim10-v3" class="text-xs font-mono text-slate-300">V₃ = 6.0 V</span>
                    </div>
                </div>
                <div id="sim10-desc" class="text-xs text-emerald-200 text-center font-medium">
                    Total Resistance Rs = 2 + 3 + 5 = 10.0 Ω. Uniform Current I = 12/10 = 1.20 A. Voltages sum: 2.4 + 3.6 + 6.0 = 12.0 V!
                </div>
            </div>
        </div>
        """
    elif s_idx == 10:
        # Slide 11: Series Failure & Fairy Lights Broken String
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 11.11: Series Failure & Fairy Lights Vulnerability
                </span>
                <button onclick="toggleSim11Bulb()" id="btn-sim11-fuse" class="px-3 py-1 rounded-lg text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition">
                    Fuse / Break Bulb #2
                </button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg viewBox="0 0 460 130" class="w-full max-w-lg h-auto mb-2">
                    <!-- Circuit wire -->
                    <path d="M 40 60 L 90 60 M 130 60 L 190 60 M 230 60 L 290 60 M 330 60 L 420 60 L 420 110 L 40 110 Z" fill="none" stroke="#475569" stroke-width="3"/>
                    <!-- Bulb 1 -->
                    <circle id="sim11-b1" cx="110" cy="60" r="14" fill="#fbbf24" fill-opacity="0.4" stroke="#f59e0b" stroke-width="2"/>
                    <text x="110" y="38" fill="#cbd5e1" font-size="8" text-anchor="middle">Bulb 1</text>
                    <!-- Bulb 2 (Breakable) -->
                    <circle id="sim11-b2" cx="210" cy="60" r="14" fill="#fbbf24" fill-opacity="0.4" stroke="#f59e0b" stroke-width="2"/>
                    <text x="210" y="38" fill="#f43f5e" font-size="8" text-anchor="middle" font-weight="bold">Bulb 2</text>
                    <!-- Bulb 3 -->
                    <circle id="sim11-b3" cx="310" cy="60" r="14" fill="#fbbf24" fill-opacity="0.4" stroke="#f59e0b" stroke-width="2"/>
                    <text x="310" y="38" fill="#cbd5e1" font-size="8" text-anchor="middle">Bulb 3</text>
                    <!-- Battery -->
                    <text x="230" y="122" fill="#cbd5e1" font-size="8" text-anchor="middle">Battery (12 V)</text>
                </svg>
                <div id="sim11-desc" class="text-xs text-rose-200 text-center font-medium">
                    All bulbs glowing in series. Click "Fuse / Break Bulb #2" to witness single-point failure shutting down the entire circuit!
                </div>
            </div>
        </div>
        """
    elif s_idx == 11:
        # Slide 12: Resistors in Parallel: Constant Voltage & Current Division
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 11.12: Parallel Resistor Branching: 1/Rp = 1/R1 + 1/R2 + 1/R3
                </span>
                <span class="text-[10px] text-slate-400 font-mono">Activity 11.6</span>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg viewBox="0 0 460 160" class="w-full max-w-lg h-auto mb-2">
                    <!-- Main bus wires -->
                    <line x1="40" y1="80" x2="130" y2="80" stroke="#64748b" stroke-width="3"/>
                    <line x1="330" y1="80" x2="420" y2="80" stroke="#64748b" stroke-width="3"/>
                    <line x1="420" y1="80" x2="420" y2="140" stroke="#64748b" stroke-width="3"/>
                    <line x1="420" y1="140" x2="40" y2="140" stroke="#64748b" stroke-width="3"/>
                    <line x1="40" y1="140" x2="40" y2="80" stroke="#64748b" stroke-width="3"/>
                    <!-- Parallel vertical splits at X (130) and Y (330) -->
                    <line x1="130" y1="30" x2="130" y2="130" stroke="#64748b" stroke-width="3"/>
                    <line x1="330" y1="30" x2="330" y2="130" stroke="#64748b" stroke-width="3"/>
                    <!-- Branch 1 (top, y=30) -->
                    <line x1="130" y1="30" x2="190" y2="30" stroke="#f59e0b" stroke-width="2.5"/>
                    <path d="M 190 30 L 198 22 L 208 38 L 218 22 L 228 38 L 236 30" fill="none" stroke="#f59e0b" stroke-width="3"/>
                    <line x1="236" y1="30" x2="330" y2="30" stroke="#f59e0b" stroke-width="2.5"/>
                    <text x="215" y="16" fill="#f59e0b" font-size="8" text-anchor="middle" font-weight="bold">R₁ = 5 Ω (I₁ = 2.4 A)</text>
                    <!-- Branch 2 (mid, y=80) -->
                    <line x1="130" y1="80" x2="190" y2="80" stroke="#38bdf8" stroke-width="2.5"/>
                    <path d="M 190 80 L 198 72 L 208 88 L 218 72 L 228 88 L 236 80" fill="none" stroke="#38bdf8" stroke-width="3"/>
                    <line x1="236" y1="80" x2="330" y2="80" stroke="#38bdf8" stroke-width="2.5"/>
                    <text x="215" y="66" fill="#38bdf8" font-size="8" text-anchor="middle" font-weight="bold">R₂ = 10 Ω (I₂ = 1.2 A)</text>
                    <!-- Branch 3 (bot, y=130) -->
                    <line x1="130" y1="130" x2="190" y2="130" stroke="#a855f7" stroke-width="2.5"/>
                    <path d="M 190 130 L 198 122 L 208 138 L 218 122 L 228 138 L 236 130" fill="none" stroke="#a855f7" stroke-width="3"/>
                    <line x1="236" y1="130" x2="330" y2="130" stroke="#a855f7" stroke-width="2.5"/>
                    <text x="215" y="116" fill="#a855f7" font-size="8" text-anchor="middle" font-weight="bold">R₃ = 30 Ω (I₃ = 0.4 A)</text>
                </svg>
                <div class="flex justify-between w-full max-w-lg text-xs font-mono p-2 bg-slate-900 rounded-lg text-slate-300">
                    <div>Mains: <span class="text-white font-bold">12 V</span></div>
                    <div>Branch Currents: <span class="text-cyan-400">2.4 + 1.2 + 0.4 = 4.0 A</span></div>
                    <div>Equivalent Rp: <span class="text-emerald-400 font-bold">3.0 Ω</span></div>
                </div>
            </div>
        </div>
        """
    elif s_idx == 12:
        # Slide 13: Parallel Circuit Domestic Fault Tolerance
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                    Interactive Lab 11.13: Independent Domestic Branch Switching
                </span>
                <span class="text-xs font-mono text-slate-400">220 V Mains Supply</span>
            </div>
            <div class="grid grid-cols-3 gap-3 max-w-lg w-full mb-3">
                <button onclick="toggleSim13App(1)" id="btn-app-1" class="p-2.5 rounded-xl text-xs font-bold bg-amber-600 text-white transition text-center">
                    <div>Bulb (0.18 A)</div>
                    <span class="text-[10px] text-amber-200">ON</span>
                </button>
                <button onclick="toggleSim13App(2)" id="btn-app-2" class="p-2.5 rounded-xl text-xs font-bold bg-sky-600 text-white transition text-center">
                    <div>Ceiling Fan (0.35 A)</div>
                    <span class="text-[10px] text-sky-200">ON</span>
                </button>
                <button onclick="toggleSim13App(3)" id="btn-app-3" class="p-2.5 rounded-xl text-xs font-bold bg-rose-600 text-white transition text-center">
                    <div>Heater (4.50 A)</div>
                    <span class="text-[10px] text-rose-200">ON</span>
                </button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 w-full max-w-lg text-center">
                <div class="text-xs text-slate-400 uppercase">Total Mains Current Drawn</div>
                <div id="sim13-total-current" class="text-xl font-mono font-extrabold text-emerald-400 my-1">5.03 A</div>
                <div id="sim13-desc" class="text-xs text-slate-300">
                    Parallel Advantage: Each appliance operates at full 220 V with its own switch; turning off one device leaves all others fully functional!
                </div>
            </div>
        </div>
        """
    elif s_idx == 13:
        # Slide 14: Joule’s Heating Effect (H = I²Rt)
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 11.14: Joule Heating Calorimeter (H = I² · R · t)
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300 font-semibold">Current (I):</label>
                    <input type="range" id="sim14-curr" min="1" max="8" step="0.5" value="5" oninput="updateSim14Heat()" class="w-24 sm:w-32 accent-rose-400 cursor-pointer">
                    <span id="sim14-curr-val" class="text-xs font-mono font-bold text-rose-400">5.0 A</span>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 w-full max-w-lg mb-2">
                    <!-- Glowing Coil SVG -->
                    <div class="bg-slate-900 p-2 rounded-xl border border-slate-800 flex flex-col items-center justify-center">
                        <svg viewBox="0 0 180 90" class="w-full h-auto">
                            <!-- Nichrome heating coil -->
                            <path id="sim14-coil" d="M 20 45 Q 35 15 50 45 Q 65 75 80 45 Q 95 15 110 45 Q 125 75 140 45 L 160 45" fill="none" stroke="#ea580c" stroke-width="4" filter="drop-shadow(0 0 8px #ea580c)"/>
                        </svg>
                        <span id="sim14-temp-status" class="text-[10px] text-amber-300 font-bold mt-1">Coil: Red Hot (~450°C)</span>
                    </div>

                    <!-- Readings -->
                    <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
                        <div class="flex justify-between text-slate-300"><span>Resistance (R):</span><span class="font-mono font-bold text-white">20 Ω</span></div>
                        <div class="flex justify-between text-slate-300"><span>Time Duration (t):</span><span class="font-mono font-bold text-white">30 s</span></div>
                        <div class="p-2 rounded bg-rose-950/40 border border-rose-500/30 text-center">
                            <span class="text-[10px] text-slate-400 block uppercase">Heat Produced (H = I²Rt)</span>
                            <span id="sim14-heat-val" class="text-base font-mono font-extrabold text-rose-300">15,000 J (15 kJ)</span>
                        </div>
                    </div>
                </div>
                <div id="sim14-desc" class="text-xs text-rose-200 text-center font-medium">
                    Quadratic I² dependence: Doubling current from 2.5 A to 5.0 A quadruples heat output from 3.75 kJ to 15 kJ!
                </div>
            </div>
        </div>
        """
    elif s_idx == 14:
        # Slide 15: Practical Applications & Safety Fuse Trip
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 11.15: Safety Fuse Trip & Overcurrent Breaker
                </span>
                <button onclick="resetSim15Fuse()" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 transition">
                    Replace Fuse
                </button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <div class="flex items-center gap-3 w-full max-w-lg mb-3">
                    <label class="text-xs text-slate-300 font-semibold">Circuit Current Load:</label>
                    <input type="range" id="sim15-load" min="1" max="10" step="0.5" value="4" oninput="updateSim15Fuse()" class="w-full accent-amber-400 cursor-pointer">
                    <span id="sim15-load-val" class="text-xs font-mono font-bold text-amber-400">4.0 A</span>
                </div>
                <!-- Fuse Cartridge SVG -->
                <svg viewBox="0 0 340 90" class="w-full max-w-sm h-auto mb-2">
                    <!-- Glass / porcelain cartridge -->
                    <rect x="70" y="25" width="200" height="40" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
                    <rect x="55" y="20" width="25" height="50" rx="3" fill="#94a3b8"/>
                    <rect x="260" y="20" width="25" height="50" rx="3" fill="#94a3b8"/>
                    <!-- Fuse Wire inside -->
                    <line id="sim15-wire" x1="75" y1="45" x2="265" y2="45" stroke="#38bdf8" stroke-width="3"/>
                    <text x="170" y="58" fill="#94a3b8" font-size="9" text-anchor="middle">5 A Rated Fuse Wire</text>
                </svg>
                <div id="sim15-desc" class="text-xs text-emerald-300 text-center font-medium">
                    Current (4.0 A) is below 5 A rating: Fuse wire is intact and conducting safely. Increase load past 5 A to trigger thermal trip!
                </div>
            </div>
        </div>
        """
    elif s_idx == 15:
        # Slide 16: Electric Power & Commercial Meter Billing
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 11.16: Electric Power & Monthly kWh Energy Bill
                </span>
                <span class="text-xs text-slate-400 font-mono">1 kWh = 3.6 × 10⁶ J</span>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 w-full max-w-lg mb-2">
                <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 space-y-2">
                    <div>
                        <label class="text-[10px] text-slate-400 uppercase block font-semibold">Appliance Rating (Watts):</label>
                        <select id="sim16-app" onchange="calcSim16Bill()" class="w-full bg-slate-950 border border-slate-700 text-xs rounded p-1.5 text-white mt-1">
                            <option value="400">Refrigerator (400 W) - Example 11.13</option>
                            <option value="250">Television (250 W)</option>
                            <option value="1200">Electric Toaster (1200 W)</option>
                            <option value="100">Incandescent Bulb (100 W)</option>
                            <option value="1500">Water Geyser (1500 W)</option>
                        </select>
                    </div>
                    <div>
                        <div class="flex justify-between text-xs text-slate-300">
                            <span>Hours per Day:</span>
                            <span id="sim16-hrs-val" class="font-mono text-cyan-400 font-bold">8 hrs/day</span>
                        </div>
                        <input type="range" id="sim16-hrs" min="1" max="24" value="8" oninput="calcSim16Bill()" class="w-full accent-cyan-400 cursor-pointer">
                    </div>
                </div>

                <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 flex flex-col justify-center space-y-1 text-center">
                    <span class="text-[10px] text-slate-400 uppercase">Monthly Consumption (30 Days)</span>
                    <span id="sim16-kwh-val" class="text-lg font-mono font-extrabold text-white">96.0 kW·h (Units)</span>
                    <span class="text-[10px] text-slate-400 uppercase mt-1">Cost @ Rs 3.00 per unit</span>
                    <span id="sim16-cost-val" class="text-lg font-mono font-extrabold text-emerald-400">Rs 288.00</span>
                </div>
            </div>
            <div id="sim16-desc" class="text-xs text-cyan-200 mt-1 text-center font-medium">
                Example 11.13: 400 W for 8 hours/day over 30 days consumes 96 kWh, costing exactly Rs 288.00!
            </div>
        </div>
        """
    elif s_idx == 16:
        # Slide 17: Complete NCERT Exercises Solutions (Q1 to Q9)
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-indigo-400"></span>
                    NCERT Exercise Interactive Solver (Q1 to Q9)
                </span>
                <span class="text-xs text-slate-400 font-mono">Part 1 • Questions 1–9</span>
            </div>
            <div class="grid grid-cols-3 sm:grid-cols-5 gap-2 mb-3">
                <button onclick="loadExercisePart1(1)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q1 (R/R' = 25)</button>
                <button onclick="loadExercisePart1(2)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q2 (Not Power: IR²)</button>
                <button onclick="loadExercisePart1(3)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q3 (110V Bulb: 25W)</button>
                <button onclick="loadExercisePart1(4)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q4 (Heat Ratio 1:4)</button>
                <button onclick="loadExercisePart1(5)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q5 (Voltmeter)</button>
                <button onclick="loadExercisePart1(6)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q6 (Length 122.7m)</button>
                <button onclick="loadExercisePart1(7)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q7 (Graph Slope)</button>
                <button onclick="loadExercisePart1(8)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q8 (4.8 kΩ Resistor)</button>
                <button onclick="loadExercisePart1(9)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q9 (9V Series 0.67A)</button>
            </div>
            <div id="exercise-sol-box1" class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs sm:text-sm text-slate-300 min-h-[130px] leading-relaxed">
                Click any exercise button above to display the verified step-by-step textbook derivation!
            </div>
        </div>
        """
    elif s_idx == 17:
        # Slide 18: Complete NCERT Exercises Solutions (Q10 to Q18)
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    NCERT Exercise Interactive Solver (Q10 to Q18)
                </span>
                <span class="text-xs text-slate-400 font-mono">Part 2 • Questions 10–18</span>
            </div>
            <div class="grid grid-cols-3 sm:grid-cols-5 gap-2 mb-3">
                <button onclick="loadExercisePart2(10)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-rose-600 text-slate-200 text-xs font-bold">Q10 (4 Resistors)</button>
                <button onclick="loadExercisePart2(11)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-rose-600 text-slate-200 text-xs font-bold">Q11 (6Ω into 9Ω/4Ω)</button>
                <button onclick="loadExercisePart2(12)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-rose-600 text-slate-200 text-xs font-bold">Q12 (110 Lamps)</button>
                <button onclick="loadExercisePart2(13)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-rose-600 text-slate-200 text-xs font-bold">Q13 (Hot Plate)</button>
                <button onclick="loadExercisePart2(14)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-rose-600 text-slate-200 text-xs font-bold">Q14 (8W in 2Ω)</button>
                <button onclick="loadExercisePart2(15)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-rose-600 text-slate-200 text-xs font-bold">Q15 (0.73A Mains)</button>
                <button onclick="loadExercisePart2(16)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-rose-600 text-slate-200 text-xs font-bold">Q16 (TV vs Toaster)</button>
                <button onclick="loadExercisePart2(17)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-rose-600 text-slate-200 text-xs font-bold">Q17 (1100 W Heat)</button>
                <button onclick="loadExercisePart2(18)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-rose-600 text-slate-200 text-xs font-bold">Q18 (Explanations)</button>
            </div>
            <div id="exercise-sol-box2" class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs sm:text-sm text-slate-300 min-h-[130px] leading-relaxed">
                Click any exercise button above to display the verified step-by-step textbook answer!
            </div>
        </div>
        """
    return ""

def generate_html():
    total_slides = len(ALL_SLIDES)
    
    # Generate navigation pills
    pills_html = ""
    for idx, slide in enumerate(ALL_SLIDES):
        short_title = f"{idx+1}"
        if idx >= len(CONTENT_SLIDES):
            short_title = f"Q{idx - len(CONTENT_SLIDES) + 1}"
        pills_html += f"""
        <button onclick="goToSlide({idx})" id="pill-{idx}" class="px-3 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap transition cursor-pointer {'bg-amber-600 text-white font-bold' if idx == 0 else 'bg-slate-800 text-slate-300 hover:bg-slate-700'}">
            {short_title}
        </button>
        """

    # Generate slides HTML
    slides_html = ""
    for s_idx, slide in enumerate(ALL_SLIDES):
        is_quiz = (s_idx >= len(CONTENT_SLIDES))
        active_class = "active" if s_idx == 0 else ""

        if not is_quiz:
            # Content Slide
            theory_cards_html = ""
            for block in slide["theory_blocks"]:
                theory_cards_html += f"""
                <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-md">
                    <h4 class="text-sm sm:text-base font-bold text-white mb-2.5 flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-amber-500"></span>
                        {block['title']}
                    </h4>
                    <div class="text-xs sm:text-sm leading-relaxed text-slate-300">
                        {block['content']}
                    </div>
                </div>
                """

            checkpoints_html = ""
            for c_idx, cp in enumerate(slide["checkpoints"]):
                opts_html = ""
                for o_idx, opt in enumerate(cp["options"]):
                    opts_html += f"""
                    <button onclick="checkOption({s_idx}, {c_idx}, {o_idx}, {cp['ans']})" id="opt-{s_idx}-{c_idx}-{o_idx}" class="w-full text-left p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs text-slate-300 transition flex items-center justify-between cursor-pointer">
                        <span>{opt}</span>
                        <span class="indicator w-4 h-4 rounded-full border border-slate-600 flex items-center justify-center text-[10px]"></span>
                    </button>
                    """

                checkpoints_html += f"""
                <div class="bg-slate-950 p-4 rounded-xl border border-slate-800/80">
                    <div class="flex items-center justify-between mb-2">
                        <span class="text-xs font-bold text-amber-400">Concept Checkpoint {c_idx+1}</span>
                        <span id="feedback-{s_idx}-{c_idx}" class="text-xs font-semibold"></span>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-200 font-medium mb-3">{cp['q']}</p>
                    <div class="space-y-2 mb-3">
                        {opts_html}
                    </div>
                    <div id="sol-{s_idx}-{c_idx}" class="hidden p-3 rounded-lg bg-amber-950/30 border border-amber-900/50 text-xs text-slate-300 leading-relaxed">
                        <strong class="text-amber-400">Explanation:</strong> {cp['solution']}
                    </div>
                </div>
                """

            teacher_card_html = f"""
            <!-- Person Talking: Dr. Sophia Physics Master Avatar -->
            <div class="mb-6 p-4 rounded-2xl bg-gradient-to-r from-amber-950/40 via-slate-900 to-indigo-950/20 border border-amber-500/30 flex flex-col sm:flex-row items-center sm:items-start gap-4 shadow-xl">
                <div class="relative shrink-0 flex flex-col items-center teacher-bob">
                    <svg viewBox="0 0 120 120" class="w-20 h-20 sm:w-24 sm:h-24 drop-shadow-lg">
                        <path d="M20 115 C20 85, 45 80, 60 80 C75 80, 100 85, 100 115 Z" fill="#d97706" stroke="#f59e0b" stroke-width="2"/>
                        <polygon points="50,80 60,105 70,80" fill="#ffffff"/>
                        <circle cx="60" cy="50" r="30" fill="#fbcfe8"/>
                        <path d="M30 45 C30 20, 90 20, 90 45 C90 30, 80 15, 60 15 C40 15, 30 30, 30 45 Z" fill="#451a03"/>
                        <rect x="42" y="42" width="14" height="10" rx="2" fill="none" stroke="#1e1b4b" stroke-width="2"/>
                        <rect x="64" y="42" width="14" height="10" rx="2" fill="none" stroke="#1e1b4b" stroke-width="2"/>
                        <line x1="56" y1="46" x2="64" y2="46" stroke="#1e1b4b" stroke-width="2"/>
                        <circle cx="49" cy="47" r="2.5" fill="#1e1b4b"/>
                        <circle cx="71" cy="47" r="2.5" fill="#1e1b4b"/>
                        <path d="M44 38 Q50 35 56 38" fill="none" stroke="#78350f" stroke-width="2"/>
                        <path d="M64 38 Q70 35 76 38" fill="none" stroke="#78350f" stroke-width="2"/>
                        <ellipse id="teacherMouth-{s_idx}" cx="60" cy="64" rx="5" ry="3" fill="#be123c"/>
                    </svg>
                    <span class="px-2 py-0.5 rounded-full text-[9px] font-extrabold bg-amber-500/20 text-amber-300 border border-amber-500/30 mt-1">
                        Dr. Sophia • Physics Educator
                    </span>
                </div>

                <div class="flex-1 bg-slate-950 p-3.5 rounded-2xl border border-slate-800 relative">
                    <div class="hidden sm:block absolute -left-2 top-6 w-3 h-3 bg-slate-950 border-l border-b border-slate-800 transform rotate-45"></div>
                    <div class="flex items-center justify-between mb-1.5">
                        <span class="text-xs font-bold text-amber-400 flex items-center gap-1.5">
                            <span class="w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
                            Teacher's Interactive Audio Commentary
                        </span>
                        <button onclick="replayVoice()" class="text-[10px] text-slate-400 hover:text-white px-2 py-0.5 rounded bg-slate-900 border border-slate-800 hover:border-slate-700 cursor-pointer flex items-center gap-1">
                            <svg class="w-3 h-3 text-amber-400" fill="currentColor" viewBox="0 0 20 20"><path d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z"/></svg>
                            Replay Audio
                        </button>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-200 leading-relaxed italic">
                        "{slide['quote']}"
                    </p>
                    <div class="mt-2 text-xs text-amber-300/90">
                        {slide['lead']}
                    </div>
                </div>
            </div>
            """

            simulator_html = get_simulator_markup(s_idx)

            completion_banner = ""
            if s_idx == total_slides - 1:
                completion_banner = """
                <div id="lastSlideNotice" class="mt-6 p-4 rounded-xl bg-amber-950/40 border border-amber-500/40 text-center">
                    <div class="inline-flex items-center gap-2 text-amber-400 font-extrabold text-sm mb-1">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        <span>You have reached the last slide of this chapter (Chapter 11: Electricity)!</span>
                    </div>
                    <p class="text-xs text-slate-300">Congratulations! You have completed all 18 master interactive lessons and all 40 mastery challenge questions covering the entire NCERT textbook.</p>
                </div>
                """

            slide_body = f"""
            <div id="slide-{s_idx}" class="slide-container {active_class}">
                <!-- Header -->
                <div class="mb-4">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-1">
                        <span class="px-2.5 py-1 rounded-md text-xs font-bold uppercase tracking-wider bg-amber-500/20 text-amber-300 border border-amber-500/30">
                            {slide['tag']}
                        </span>
                        <span class="text-xs font-semibold text-slate-400">{slide['subtitle']}</span>
                    </div>
                    <h2 class="text-xl sm:text-2xl font-extrabold text-white tracking-tight">{slide['title']}</h2>
                </div>

                {teacher_card_html}

                <!-- Interactive Simulator Component -->
                <div class="mb-6">
                    {simulator_html}
                </div>

                <!-- Theory Cards Grid -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                    {theory_cards_html}
                </div>

                <!-- Slide Checkpoints -->
                <div class="bg-slate-900/60 border border-slate-800 rounded-2xl p-4 sm:p-5">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-amber-400 mb-3 flex items-center gap-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                        Slide Interactive Checkpoints
                    </h4>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {checkpoints_html}
                    </div>
                </div>

                {completion_banner}
            </div>
            """
            slides_html += slide_body

        else:
            # Quiz Challenge Slide
            quiz_idx = s_idx - len(CONTENT_SLIDES)
            quiz_cards_html = ""
            for q_idx, q_item in enumerate(slide["questions"]):
                clean_solution = q_item['solution'].replace('"', '&quot;').replace("'", "&#39;")
                clean_title = q_item['q'].replace('"', '&quot;').replace("'", "&#39;")
                opts_html = ""
                for o_idx, opt in enumerate(q_item["options"]):
                    opts_html += f"""
                    <button onclick="checkQuizOption({s_idx}, {q_idx}, {o_idx}, {q_item['ans']})" id="qopt-{s_idx}-{q_idx}-{o_idx}" class="w-full text-left p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs text-slate-300 transition flex items-center justify-between cursor-pointer">
                        <span>{opt}</span>
                        <span class="indicator w-4 h-4 rounded-full border border-slate-600 flex items-center justify-center text-[10px]"></span>
                    </button>
                    """

                quiz_cards_html += f"""
                <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-4 shadow-lg flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">
                                Question {q_item['id']}
                            </span>
                            <span id="qfeedback-{s_idx}-{q_idx}" class="text-xs font-semibold"></span>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-200 font-semibold mb-3 leading-snug">{q_item['q']}</p>
                        <div class="space-y-1.5 mb-3">
                            {opts_html}
                        </div>
                    </div>
                    <div class="pt-2 border-t border-slate-800 flex items-center justify-between">
                        <button onclick="openQuizSolution('{q_item['id']}', '{clean_title}', '{clean_solution}')" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition flex items-center gap-1.5 shadow-md cursor-pointer">
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                            View Solution
                        </button>
                        <span class="text-[10px] text-slate-500 font-mono">NCERT Verified</span>
                    </div>
                </div>
                """

            completion_banner = ""
            if s_idx == total_slides - 1:
                completion_banner = """
                <div id="lastSlideNotice" class="mt-6 p-4 rounded-xl bg-amber-950/40 border border-amber-500/40 text-center">
                    <div class="inline-flex items-center gap-2 text-amber-400 font-extrabold text-sm mb-1">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        <span>You have reached the last slide of this chapter (Chapter 11: Electricity)!</span>
                    </div>
                    <p class="text-xs text-slate-300">Congratulations! You have completed all 18 master interactive lessons and all 40 mastery challenge questions covering the entire NCERT textbook.</p>
                </div>
                """

            slide_body = f"""
            <div id="slide-{s_idx}" class="slide-container {active_class}">
                <!-- Header -->
                <div class="mb-4">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-1">
                        <span class="px-2.5 py-1 rounded-md text-xs font-bold uppercase tracking-wider bg-rose-500/20 text-rose-300 border border-rose-500/30">
                            Mastery Challenge Quiz {quiz_idx+1} of 4
                        </span>
                        <span class="text-xs font-semibold text-slate-400">{slide['subtitle']}</span>
                    </div>
                    <h2 class="text-xl sm:text-2xl font-extrabold text-white tracking-tight">{slide['title']}</h2>
                    <p class="text-xs text-slate-400 mt-1">{slide.get('lead', 'Test your conceptual understanding and numerical accuracy with 10 board-level challenge questions. Click View Solution for full step-by-step teacher explanations.')}</p>
                </div>

                <!-- 10 Quiz Questions Grid -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                    {quiz_cards_html}
                </div>

                {completion_banner}
            </div>
            """
            slides_html += slide_body

    slides_json = json.dumps(ALL_SLIDES)

    html_template = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 10 Science • Chapter 11: Electricity</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- KaTeX for crisp LaTeX formatting -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');
        
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #030712;
            color: #f8fafc;
        }}

        .font-mono {{
            font-family: 'JetBrains Mono', monospace;
        }}

        .slide-container {{
            display: none;
            opacity: 0;
            transform: translateY(10px);
            transition: opacity 0.35s ease, transform 0.35s ease;
        }}

        .slide-container.active {{
            display: block;
            opacity: 1;
            transform: translateY(0);
        }}

        .custom-scrollbar::-webkit-scrollbar {{
            height: 6px;
            width: 6px;
        }}
        .custom-scrollbar::-webkit-scrollbar-track {{
            background: #0f172a;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: #334155;
            border-radius: 9999px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
            background: #475569;
        }}

        @keyframes teacherBob {{
            0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
            50% {{ transform: translateY(-3px) rotate(0.8deg); }}
        }}
        .teacher-bob {{
            animation: teacherBob 4s ease-in-out infinite;
        }}

        @keyframes mouthMove {{
            0%, 100% {{ ry: 3; rx: 5; }}
            50% {{ ry: 6.5; rx: 4.5; }}
        }}
        .talking-mouth {{
            animation: mouthMove 0.25s infinite alternate;
        }}

        .modal-backdrop {{
            background: rgba(3, 7, 18, 0.85);
            backdrop-filter: blur(8px);
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between selection:bg-amber-500 selection:text-slate-950">

    <!-- Top Navigation Bar -->
    <header class="sticky top-0 z-40 bg-slate-950/90 backdrop-blur-md border-b border-slate-800/80 px-4 py-3">
        <div class="max-w-6xl mx-auto flex items-center justify-between">
            <div class="flex items-center gap-3">
                <a href="/multimedia?syllabus=ncert&subject=science&class=class10" class="text-slate-400 hover:text-white transition flex items-center gap-1.5 text-xs font-semibold">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
                    <span>Curriculum</span>
                </a>
                <div class="h-4 w-px bg-slate-800"></div>
                <div class="flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-amber-500 shadow-md shadow-amber-500/50"></span>
                    <h1 class="text-xs sm:text-sm font-bold text-slate-100 truncate max-w-[200px] sm:max-w-md">
                        NCERT Class 10 Science • Chapter 11: Electricity
                    </h1>
                </div>
            </div>

            <!-- Voice Narration Controller -->
            <div class="flex items-center gap-2">
                <button onclick="toggleVoice()" id="voiceToggleBtn" class="px-2.5 py-1.5 rounded-xl text-xs font-semibold bg-slate-900 border border-slate-800 hover:border-slate-700 text-slate-300 hover:text-white flex items-center gap-1.5 cursor-pointer transition">
                    <svg id="voiceIconOn" class="w-3.5 h-3.5 text-emerald-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M9.383 3.076A1 1 0 0110 4v12a1 1 0 01-1.707.707L4.586 13H2a1 1 0 01-1-1V8a1 1 0 011-1h2.586l3.707-3.707a1 1 0 011.09-.217zM14.657 2.929a1 1 0 011.414 0A9.972 9.972 0 0119 10a9.972 9.972 0 01-2.929 7.071 1 1 0 01-1.414-1.414A7.971 7.971 0 0017 10c0-2.21-.894-4.208-2.343-5.657a1 1 0 010-1.414zm-2.829 2.828a1 1 0 011.415 0A5.983 5.983 0 0115 10a5.984 5.984 0 01-1.757 4.243 1 1 0 01-1.415-1.415A3.984 3.984 0 0013 10a3.983 3.983 0 00-1.172-2.828 1 1 0 010-1.415z" clip-rule="evenodd"/></svg>
                    <svg id="voiceIconOff" class="w-3.5 h-3.5 text-slate-500 hidden" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M9.383 3.076A1 1 0 0110 4v12a1 1 0 01-1.707.707L4.586 13H2a1 1 0 01-1-1V8a1 1 0 011-1h2.586l3.707-3.707a1 1 0 011.09-.217zM12.293 7.293a1 1 0 011.414 0L15 8.586l1.293-1.293a1 1 0 111.414 1.414L16.414 10l1.293 1.293a1 1 0 01-1.414 1.414L15 11.414l-1.293 1.293a1 1 0 01-1.414-1.414L13.586 10l-1.293-1.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                    <span id="voiceStatusText">Voice On</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="max-w-5xl mx-auto w-full px-4 py-6 flex-1">
        {slides_html}
    </main>

    <!-- Sticky Bottom Navigation Bar -->
    <footer class="sticky bottom-0 z-40 bg-slate-950/95 backdrop-blur-md border-t border-slate-800 px-4 py-3">
        <div class="max-w-5xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
            <div class="flex items-center gap-2 w-full sm:w-auto justify-between sm:justify-start">
                <button onclick="navigateSlide(-1)" id="prevBtn" class="px-4 py-2 rounded-xl text-xs font-bold bg-slate-900 border border-slate-800 hover:bg-slate-800 text-slate-200 transition disabled:opacity-40 disabled:pointer-events-none flex items-center gap-1.5 cursor-pointer">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
                    Previous
                </button>
                <button onclick="navigateSlide(1)" id="nextBtn" class="px-4 py-2 rounded-xl text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition flex items-center gap-1.5 shadow-md shadow-amber-600/30 cursor-pointer">
                    Next
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </button>
            </div>

            <div class="flex items-center gap-1.5 overflow-x-auto max-w-full sm:max-w-2xl py-1 custom-scrollbar">
                {pills_html}
            </div>

            <div class="hidden md:flex items-center gap-2 text-xs text-slate-400 font-mono">
                <span>Slide</span>
                <span id="currentSlideIndicator" class="text-amber-400 font-bold">1</span>
                <span>/</span>
                <span>{len(ALL_SLIDES)}</span>
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
                <span class="px-2.5 py-1 rounded-md text-xs font-extrabold uppercase tracking-wider bg-amber-500/20 text-amber-300 border border-amber-500/40">
                    Verified Solution
                </span>
                <span id="modalQuestionId" class="text-xs text-slate-400 font-mono"></span>
            </div>
            <h3 id="modalQuestionTitle" class="text-sm font-bold text-white mb-3"></h3>
            <div class="p-4 rounded-xl bg-slate-950 border border-slate-800 mb-4">
                <div class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-1">Step-by-Step Teacher Explanation:</div>
                <div id="modalSolutionContent" class="text-xs sm:text-sm text-slate-300 leading-relaxed"></div>
            </div>
            <div class="flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-2 rounded-xl text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition cursor-pointer">
                    Got It, Close Solution
                </button>
            </div>
        </div>
    </div>

    <!-- Master Laboratory Script -->
    <script>
        const slidesData = {slides_json};
        let currentSlideIndex = 0;
        let voiceEnabled = true;
        let audioCtx = null;
        let speechSynth = window.speechSynthesis;
        let currentUtterance = null;

        function initAudio() {{
            if (!audioCtx) {{
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }}
            if (audioCtx.state === 'suspended') {{
                audioCtx.resume();
            }}
        }}

        function playTone(freq, type, duration) {{
            try {{
                initAudio();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = type || 'sine';
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + duration);
            }} catch(e) {{}}
        }}

        function playCorrectSound() {{
            playTone(523.25, 'sine', 0.12);
            setTimeout(() => playTone(659.25, 'sine', 0.12), 100);
            setTimeout(() => playTone(783.99, 'sine', 0.2), 200);
        }}

        function playIncorrectSound() {{
            playTone(330, 'square', 0.12);
            setTimeout(() => playTone(260, 'square', 0.2), 120);
        }}

        function showSlide(index) {{
            document.querySelectorAll('.slide-container').forEach(el => el.classList.remove('active'));
            const newEl = document.getElementById(`slide-${{index}}`);
            if (newEl) newEl.classList.add('active');

            const oldPill = document.getElementById(`pill-${{currentSlideIndex}}`);
            if (oldPill) {{
                oldPill.className = 'px-3 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap transition cursor-pointer bg-slate-800 text-slate-300 hover:bg-slate-700';
            }}
            const newPill = document.getElementById(`pill-${{index}}`);
            if (newPill) {{
                newPill.classList.remove('bg-slate-800', 'text-slate-300', 'hover:bg-slate-700');
                newPill.classList.add('bg-amber-600', 'text-white', 'font-bold');
                newPill.scrollIntoView({{ behavior: 'smooth', inline: 'center', block: 'nearest' }});
            }}

            currentSlideIndex = index;
            document.getElementById('currentSlideIndicator').textContent = currentSlideIndex + 1;
            document.getElementById('prevBtn').disabled = (currentSlideIndex === 0);

            // Hide next button on last slide
            const nextBtn = document.getElementById('nextBtn');
            if (currentSlideIndex === slidesData.length - 1) {{
                nextBtn.style.display = 'none';
            }} else {{
                nextBtn.style.display = 'flex';
            }}

            replayVoice();

            if (window.renderMathInElement) {{
                renderMathInElement(newEl, {{
                    delimiters: [
                        {{left: '$$', right: '$$', display: true}},
                        {{left: '$', right: '$', display: false}}
                    ]
                }});
            }}
        }}

        function navigateSlide(direction) {{
            const newIdx = currentSlideIndex + direction;
            if (newIdx >= 0 && newIdx < slidesData.length) {{
                showSlide(newIdx);
                playTone(440, 'sine', 0.08);
            }}
        }}

        function goToSlide(index) {{
            if (index >= 0 && index < slidesData.length) {{
                showSlide(index);
                playTone(480, 'sine', 0.08);
            }}
        }}

        function toggleVoice() {{
            voiceEnabled = !voiceEnabled;
            const onIcon = document.getElementById('voiceIconOn');
            const offIcon = document.getElementById('voiceIconOff');
            const text = document.getElementById('voiceStatusText');

            if (voiceEnabled) {{
                onIcon.classList.remove('hidden');
                offIcon.classList.add('hidden');
                text.textContent = 'Voice On';
                replayVoice();
            }} else {{
                onIcon.classList.add('hidden');
                offIcon.classList.remove('hidden');
                text.textContent = 'Voice Off';
                stopSpeaking();
            }}
        }}

        function stopSpeaking() {{
            if (speechSynth && speechSynth.speaking) {{
                speechSynth.cancel();
            }}
            setMouthAnimation(false);
        }}

        function setMouthAnimation(talking) {{
            const mouth = document.getElementById(`teacherMouth-${{currentSlideIndex}}`);
            if (mouth) {{
                if (talking) mouth.classList.add('talking-mouth');
                else mouth.classList.remove('talking-mouth');
            }}
        }}

        function replayVoice() {{
            stopSpeaking();
            if (!voiceEnabled || !speechSynth) return;

            const current = slidesData[currentSlideIndex];
            if (!current || !current.narration) return;

            currentUtterance = new SpeechSynthesisUtterance(current.narration);
            currentUtterance.rate = 0.98;
            currentUtterance.pitch = 1.05;

            currentUtterance.onstart = () => setMouthAnimation(true);
            currentUtterance.onend = () => setMouthAnimation(false);
            currentUtterance.onerror = () => setMouthAnimation(false);

            try {{
                speechSynth.speak(currentUtterance);
            }} catch(e) {{
                setMouthAnimation(false);
            }}
        }}

        function checkOption(sIdx, cIdx, selectedOpt, correctOpt) {{
            const feedbackEl = document.getElementById(`feedback-${{sIdx}}-${{cIdx}}`);
            const solEl = document.getElementById(`sol-${{sIdx}}-${{cIdx}}`);
            
            for (let i = 0; i < 4; i++) {{
                const btn = document.getElementById(`opt-${{sIdx}}-${{cIdx}}-${{i}}`);
                if (!btn) continue;
                btn.classList.remove('border-emerald-500', 'bg-emerald-950/40', 'border-rose-500', 'bg-rose-950/40');
                if (i === correctOpt) {{
                    btn.classList.add('border-emerald-500', 'bg-emerald-950/40');
                    btn.querySelector('.indicator').innerHTML = '✓';
                    btn.querySelector('.indicator').className = 'indicator w-4 h-4 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-[10px]';
                }} else if (i === selectedOpt) {{
                    btn.classList.add('border-rose-500', 'bg-rose-950/40');
                    btn.querySelector('.indicator').innerHTML = '✕';
                    btn.querySelector('.indicator').className = 'indicator w-4 h-4 rounded-full bg-rose-500 text-white font-bold flex items-center justify-center text-[10px]';
                }}
            }}

            if (selectedOpt === correctOpt) {{
                playCorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-emerald-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Correct!</span>`;
                if (solEl) solEl.classList.remove('hidden');
            }} else {{
                playIncorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-rose-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg> Review Solution Below</span>`;
                if (solEl) solEl.classList.remove('hidden');
            }}

            if (solEl && window.renderMathInElement) {{
                renderMathInElement(solEl, {{
                    delimiters: [
                        {{left: '$$', right: '$$', display: true}},
                        {{left: '$', right: '$', display: false}}
                    ]
                }});
            }}
        }}

        function checkQuizOption(sIdx, qIdx, selectedOpt, correctOpt) {{
            const feedbackEl = document.getElementById(`qfeedback-${{sIdx}}-${{qIdx}}`);
            for (let i = 0; i < 4; i++) {{
                const btn = document.getElementById(`qopt-${{sIdx}}-${{qIdx}}-${{i}}`);
                if (!btn) continue;
                btn.classList.remove('border-emerald-500', 'bg-emerald-950/40', 'border-rose-500', 'bg-rose-950/40');
                if (i === correctOpt) {{
                    btn.classList.add('border-emerald-500', 'bg-emerald-950/40');
                    btn.querySelector('.indicator').innerHTML = '✓';
                    btn.querySelector('.indicator').className = 'indicator w-4 h-4 rounded-full bg-emerald-500 text-slate-950 font-bold flex items-center justify-center text-[10px]';
                }} else if (i === selectedOpt) {{
                    btn.classList.add('border-rose-500', 'bg-rose-950/40');
                    btn.querySelector('.indicator').innerHTML = '✕';
                    btn.querySelector('.indicator').className = 'indicator w-4 h-4 rounded-full bg-rose-500 text-white font-bold flex items-center justify-center text-[10px]';
                }}
            }}

            if (selectedOpt === correctOpt) {{
                playCorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-emerald-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Correct!</span>`;
            }} else {{
                playIncorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-rose-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg> Click Solution</span>`;
            }}
        }}

        function openQuizSolution(qId, title, solutionHtml) {{
            playTone(550, 'sine', 0.1);
            document.getElementById('modalQuestionId').textContent = `Question ${{qId}} Solution`;
            document.getElementById('modalQuestionTitle').textContent = title;
            const solEl = document.getElementById('modalSolutionContent');
            solEl.innerHTML = solutionHtml;
            document.getElementById('solutionModal').classList.remove('hidden');

            if (window.renderMathInElement) {{
                renderMathInElement(solEl, {{
                    delimiters: [
                        {{left: '$$', right: '$$', display: true}},
                        {{left: '$', right: '$', display: false}}
                    ]
                }});
            }}
        }}

        function closeSolutionModal() {{
            playTone(400, 'sine', 0.08);
            document.getElementById('solutionModal').classList.add('hidden');
        }}

        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') closeSolutionModal();
            if (e.key === 'ArrowRight' && currentSlideIndex < slidesData.length - 1) navigateSlide(1);
            if (e.key === 'ArrowLeft' && currentSlideIndex > 0) navigateSlide(-1);
        }});

        // ================= SIMULATOR CONTROLLERS =================
        let sim1Closed = true;
        function toggleSim1Switch() {{
            sim1Closed = !sim1Closed;
            playTone(450, 'sine', 0.08);
            const btnText = document.getElementById('sim1-switch-text');
            const btnDot = document.getElementById('sim1-switch-dot');
            const blade = document.getElementById('sim1-key-blade');
            const bulb = document.getElementById('sim1-bulb-glow');
            const fil = document.getElementById('sim1-filament');
            const electrons = document.getElementById('sim1-electrons');
            const conv = document.getElementById('sim1-conv-arrows');
            const desc = document.getElementById('sim1-desc');

            if (sim1Closed) {{
                btnText.textContent = 'Switch: CLOSED (Current ON)';
                btnDot.className = 'w-2 h-2 rounded-full bg-white animate-pulse';
                blade.setAttribute('x2', '0');
                blade.setAttribute('y2', '12');
                bulb.setAttribute('fill-opacity', '0.35');
                fil.setAttribute('stroke', '#fef08a');
                electrons.classList.remove('hidden');
                conv.classList.remove('hidden');
                desc.textContent = 'Continuous closed circuit: Electrons drift counter-clockwise from negative to positive terminal; conventional current flows clockwise from positive to negative. Bulb glows!';
            }} else {{
                btnText.textContent = 'Switch: OPEN (Current OFF)';
                btnDot.className = 'w-2 h-2 rounded-full bg-rose-400';
                blade.setAttribute('x2', '-10');
                blade.setAttribute('y2', '4');
                bulb.setAttribute('fill-opacity', '0');
                fil.setAttribute('stroke', '#475569');
                electrons.classList.add('hidden');
                conv.classList.add('hidden');
                desc.textContent = 'Open circuit: Conducting path broken at the switch. Current drops to zero instantly, and the bulb does not glow!';
            }}
        }}

        function updateSim2Charge() {{
            const I = parseFloat(document.getElementById('sim2-current').value);
            const t = parseFloat(document.getElementById('sim2-time').value);
            const Q = I * t;
            const n = Q / (1.6e-19);

            document.getElementById('sim2-curr-val').textContent = `${{I.toFixed(1)}} A`;
            document.getElementById('sim2-time-val').textContent = `${{(t/60).toFixed(0)}} min (${{t}} s)`;
            document.getElementById('sim2-q-val').textContent = `${{Q.toFixed(1)}} C`;
            document.getElementById('sim2-n-val').textContent = `${{n.toExponential(2)}} electrons`;
            document.getElementById('sim2-ammeter-display').textContent = `${{I.toFixed(2)}} A`;
            playTone(480, 'sine', 0.04);
        }}

        function updateSim3Potential() {{
            const V = parseFloat(document.getElementById('sim3-volt').value);
            const Q = parseFloat(document.getElementById('sim3-charge').value) || 2;
            const W = V * Q;
            document.getElementById('sim3-volt-val').textContent = `${{V.toFixed(1)}} V`;
            document.getElementById('sim3-work-val').textContent = `${{W.toFixed(1)}} Joules`;

            // Adjust water tank level visual
            const h = Math.min(48, 15 + (V / 24) * 33);
            const wLevel = document.getElementById('sim3-water-level');
            if (wLevel) {{
                wLevel.setAttribute('height', h);
                wLevel.setAttribute('y', 63 - h);
            }}
            playTone(460, 'sine', 0.04);
        }}

        function setSim4Symbol(type) {{
            playTone(490, 'sine', 0.06);
            const prev = document.getElementById('sim4-preview');
            ['cell', 'key', 'res', 'meters'].forEach(t => {{
                const b = document.getElementById(`btn-sym-${{t}}`);
                if (b) b.className = (t === type) ? 'p-2 rounded-xl text-xs font-bold bg-purple-600 text-white transition' : 'p-2 rounded-xl text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
            }});

            if (type === 'cell') {{
                prev.innerHTML = `
                    <svg viewBox="0 0 340 70" class="w-full max-w-sm h-auto">
                        <line x1="40" y1="35" x2="100" y2="35" stroke="#94a3b8" stroke-width="2"/>
                        <line x1="100" y1="15" x2="100" y2="55" stroke="#f59e0b" stroke-width="4"/>
                        <line x1="115" y1="22" x2="115" y2="48" stroke="#64748b" stroke-width="6"/>
                        <line x1="115" y1="35" x2="175" y2="35" stroke="#94a3b8" stroke-width="2"/>
                        <text x="94" y="25" fill="#f59e0b" font-size="9" font-weight="bold">+</text>
                        <text x="122" y="25" fill="#94a3b8" font-size="9" font-weight="bold">-</text>
                        <line x1="185" y1="35" x2="215" y2="35" stroke="#94a3b8" stroke-width="2"/>
                        <line x1="215" y1="15" x2="215" y2="55" stroke="#f59e0b" stroke-width="3"/>
                        <line x1="225" y1="22" x2="225" y2="48" stroke="#64748b" stroke-width="5"/>
                        <line x1="235" y1="15" x2="235" y2="55" stroke="#f59e0b" stroke-width="3"/>
                        <line x1="245" y1="22" x2="245" y2="48" stroke="#64748b" stroke-width="5"/>
                        <line x1="245" y1="35" x2="300" y2="35" stroke="#94a3b8" stroke-width="2"/>
                    </svg>
                    <span class="text-xs text-purple-200 mt-2 font-medium">Single Electric Cell (Left) vs Combination Battery (Right)</span>
                `;
            }} else if (type === 'key') {{
                prev.innerHTML = `
                    <svg viewBox="0 0 340 70" class="w-full max-w-sm h-auto">
                        <!-- Open key ( ) -->
                        <line x1="40" y1="35" x2="80" y2="35" stroke="#38bdf8" stroke-width="2"/>
                        <path d="M 80 20 A 15 15 0 0 1 80 50" fill="none" stroke="#38bdf8" stroke-width="2"/>
                        <path d="M 120 20 A 15 15 0 0 0 120 50" fill="none" stroke="#38bdf8" stroke-width="2"/>
                        <line x1="120" y1="35" x2="160" y2="35" stroke="#38bdf8" stroke-width="2"/>
                        <text x="100" y="65" fill="#94a3b8" font-size="8" text-anchor="middle">Open Key ( )</text>
                        <!-- Closed key ( • ) -->
                        <line x1="180" y1="35" x2="220" y2="35" stroke="#38bdf8" stroke-width="2"/>
                        <path d="M 220 20 A 15 15 0 0 1 220 50" fill="none" stroke="#38bdf8" stroke-width="2"/>
                        <circle cx="240" cy="35" r="3.5" fill="#38bdf8"/>
                        <path d="M 260 20 A 15 15 0 0 0 260 50" fill="none" stroke="#38bdf8" stroke-width="2"/>
                        <line x1="260" y1="35" x2="300" y2="35" stroke="#38bdf8" stroke-width="2"/>
                        <text x="240" y="65" fill="#38bdf8" font-size="8" text-anchor="middle" font-weight="bold">Closed Key ( • )</text>
                    </svg>
                    <span class="text-xs text-purple-200 mt-2 font-medium">Plug Key (Open: No Current) vs Plug Key (Closed: Circuit Complete)</span>
                `;
            }} else if (type === 'res') {{
                prev.innerHTML = `
                    <svg viewBox="0 0 340 70" class="w-full max-w-sm h-auto">
                        <!-- Fixed resistor -->
                        <line x1="20" y1="35" x2="50" y2="35" stroke="#f59e0b" stroke-width="2"/>
                        <path d="M 50 35 L 60 20 L 75 50 L 90 20 L 105 50 L 115 35" fill="none" stroke="#f59e0b" stroke-width="3"/>
                        <line x1="115" y1="35" x2="145" y2="35" stroke="#f59e0b" stroke-width="2"/>
                        <text x="82" y="65" fill="#f59e0b" font-size="8" text-anchor="middle">Fixed Resistor R</text>
                        <!-- Rheostat / Variable -->
                        <line x1="180" y1="35" x2="210" y2="35" stroke="#ec4899" stroke-width="2"/>
                        <path d="M 210 35 L 220 20 L 235 50 L 250 20 L 265 50 L 275 35" fill="none" stroke="#ec4899" stroke-width="3"/>
                        <line x1="275" y1="35" x2="305" y2="35" stroke="#ec4899" stroke-width="2"/>
                        <line x1="215" y1="58" x2="270" y2="12" stroke="#ec4899" stroke-width="2"/>
                        <polygon points="274,8 266,13 273,19" fill="#ec4899"/>
                        <text x="242" y="65" fill="#ec4899" font-size="8" text-anchor="middle">Variable Rheostat</text>
                    </svg>
                    <span class="text-xs text-purple-200 mt-2 font-medium">Fixed Resistance (Zigzag) vs Rheostat (Zigzag with Slanted Arrow)</span>
                `;
            }} else {{
                prev.innerHTML = `
                    <svg viewBox="0 0 340 70" class="w-full max-w-sm h-auto">
                        <line x1="40" y1="35" x2="80" y2="35" stroke="#38bdf8" stroke-width="2"/>
                        <circle cx="105" cy="35" r="18" fill="#0f172a" stroke="#ec4899" stroke-width="2"/>
                        <text x="105" y="40" fill="#ec4899" font-size="12" font-weight="bold" text-anchor="middle">A</text>
                        <line x1="130" y1="35" x2="170" y2="35" stroke="#38bdf8" stroke-width="2"/>
                        <text x="105" y="65" fill="#ec4899" font-size="8" text-anchor="middle">Ammeter (In Series)</text>

                        <line x1="180" y1="35" x2="220" y2="35" stroke="#38bdf8" stroke-width="2"/>
                        <circle cx="245" cy="35" r="18" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
                        <text x="245" y="40" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">V</text>
                        <line x1="270" y1="35" x2="310" y2="35" stroke="#38bdf8" stroke-width="2"/>
                        <text x="245" y="65" fill="#38bdf8" font-size="8" text-anchor="middle">Voltmeter (In Parallel)</text>
                    </svg>
                    <span class="text-xs text-purple-200 mt-2 font-medium">Ammeter (Measures Current in Series) vs Voltmeter (Measures Voltage in Parallel)</span>
                `;
            }}
        }}

        function updateSim5Ohm() {{
            const V = parseFloat(document.getElementById('sim5-volt').value);
            const R = parseFloat(document.getElementById('sim5-res').value);
            const I = V / R;

            document.getElementById('sim5-volt-val').textContent = `${{V.toFixed(1)}} V`;
            document.getElementById('sim5-res-val').textContent = `${{R.toFixed(1)}} Ω`;
            document.getElementById('sim5-curr-val').textContent = `${{I.toFixed(2)}} A`;
            document.getElementById('sim5-slope-val').textContent = `${{R.toFixed(2)}} Ω`;

            // Plot operating point: range V 0..15 -> y 130..25, I 0..3.75 -> x 30..180
            const x = 30 + (I / 3.75) * 150;
            const y = 130 - (V / 15) * 105;
            const pt = document.getElementById('sim5-point');
            const vProj = document.getElementById('sim5-v-proj');
            const iProj = document.getElementById('sim5-i-proj');
            if (pt) {{
                pt.setAttribute('cx', Math.min(185, Math.max(30, x)));
                pt.setAttribute('cy', Math.min(130, Math.max(25, y)));
            }}
            if (vProj) {{
                vProj.setAttribute('y1', y);
                vProj.setAttribute('y2', y);
                vProj.setAttribute('x2', x);
            }}
            if (iProj) {{
                iProj.setAttribute('x1', x);
                iProj.setAttribute('x2', x);
                iProj.setAttribute('y1', y);
            }}
            playTone(450 + V * 10, 'sine', 0.04);
        }}

        function setSim6Material(mat) {{
            playTone(510, 'sine', 0.08);
            const bC = document.getElementById('btn-sim6-cond');
            const bR = document.getElementById('btn-sim6-res');
            const bI = document.getElementById('btn-sim6-ins');
            const path = document.getElementById('sim6-electron-path');
            const desc = document.getElementById('sim6-desc');

            [bC, bR, bI].forEach(b => b.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition');

            if (mat === 'conductor') {{
                bC.className = 'px-2.5 py-1 rounded text-xs font-bold bg-sky-600 text-white transition';
                path.setAttribute('d', 'M 40 80 Q 80 70 120 85 T 200 75 T 280 85 T 360 75 L 440 80');
                desc.textContent = 'Good Conductor (Copper): Low atomic lattice collision rate allows high drift velocity and effortless charge flow.';
            }} else if (mat === 'resistor') {{
                bR.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                path.setAttribute('d', 'M 40 80 L 80 45 L 120 115 L 160 50 L 200 110 L 240 50 L 280 110 L 320 50 L 360 110 L 400 50 L 440 80');
                desc.textContent = 'Resistor (Nichrome): Strong electron-ion collisions retard forward drift, converting electrical energy into thermal lattice vibrations.';
            }} else {{
                bI.className = 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition';
                path.setAttribute('d', 'M 40 80 L 70 80');
                desc.textContent = 'Insulator (Rubber): Electrons are tightly bound to atoms. Zero free drift occurs under ordinary electric fields.';
            }}
        }}

        function updateSim7Wire() {{
            const l = parseFloat(document.getElementById('sim7-len').value);
            const dMm = parseFloat(document.getElementById('sim7-dia').value);
            const d = dMm * 1e-3;
            const A = (Math.PI * d * d) / 4;
            const rho = 1e-6; // nichrome
            const R = (rho * l) / A;

            document.getElementById('sim7-l-val').textContent = `${{l.toFixed(1)}} m`;
            document.getElementById('sim7-d-val').textContent = `${{dMm.toFixed(1)}} mm`;
            document.getElementById('sim7-r-val').textContent = `${{R.toFixed(2)}} Ω`;

            const wireRect = document.getElementById('sim7-wire-rect');
            if (wireRect) {{
                const w = 60 + (l / 3.0) * 110;
                const h = 6 + (dMm / 1.0) * 18;
                wireRect.setAttribute('width', w);
                wireRect.setAttribute('height', h);
                wireRect.setAttribute('y', 40 - h/2);
            }}
            playTone(470, 'sine', 0.04);
        }}

        function setSim8Mat(mat) {{
            playTone(520, 'sine', 0.08);
            const data = {{
                silver: {{ rho: '1.60 × 10⁻⁸ Ω·m', cls: 'Best Conductor', app: 'Precision Contacts', color: 'bg-cyan-600', desc: 'Silver has the lowest resistivity of any known metal at 20°C!' }},
                copper: {{ rho: '1.62 × 10⁻⁸ Ω·m', cls: 'Excellent Conductor', app: 'Transmission Cables', color: 'bg-amber-600', desc: 'Copper combines outstanding conductivity with flexibility and affordability.' }},
                tungsten: {{ rho: '5.20 × 10⁻⁸ Ω·m', cls: 'Refractory Metal', app: 'Bulb Filaments', color: 'bg-yellow-600', desc: 'Tungsten withstands 3380°C incandescence without melting!' }},
                nichrome: {{ rho: '100 × 10⁻⁶ Ω·m', cls: 'High-Resistivity Alloy', app: 'Toasters & Irons', color: 'bg-rose-600', desc: 'Nichrome alloy does not burn or oxidise even at red-hot temperatures.' }},
                glass: {{ rho: '10¹⁰ – 10¹⁴ Ω·m', cls: 'Solid Insulator', app: 'Pylon Bushings', color: 'bg-slate-700', desc: 'Glass offers immense electrical resistance to block current leakage.' }},
                rubber: {{ rho: '10¹³ – 10¹⁶ Ω·m', cls: 'Flexible Insulator', app: 'Cable Sheathing', color: 'bg-slate-700', desc: 'Rubber coats high-voltage cables for touch safety.' }}
            }};

            const m = data[mat] || data.nichrome;
            document.getElementById('sim8-rho-val').textContent = m.rho;
            document.getElementById('sim8-class-val').textContent = m.cls;
            document.getElementById('sim8-app-val').textContent = m.app;
            document.getElementById('sim8-desc').textContent = m.desc;

            ['silver', 'copper', 'tungsten', 'nichrome', 'glass', 'rubber'].forEach(key => {{
                const b = document.getElementById(`btn-mat-${{key}}`);
                if (b) b.className = (key === mat) ? `p-2 rounded-lg text-xs font-bold text-white ${{m.color}}` : 'p-2 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700';
            }});
        }}

        function setSim9Tab(tab) {{
            playTone(480, 'sine', 0.06);
            const b1 = document.getElementById('btn-sim9-ex113');
            const b2 = document.getElementById('btn-sim9-ex116');
            const content = document.getElementById('sim9-content');
            const desc = document.getElementById('sim9-desc');

            if (tab === 'ex113') {{
                b1.className = 'px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 text-white';
                b2.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700';
                content.innerHTML = `
                    <div class="grid grid-cols-2 gap-3 text-center">
                        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
                            <span class="text-xs font-bold text-amber-400 block mb-1">Electric Bulb Filament</span>
                            <div class="text-[11px] text-slate-300">R = 1200 Ω, V = 220 V</div>
                            <div class="text-base font-mono font-extrabold text-white mt-1">I = 0.18 A</div>
                            <span class="text-[10px] text-slate-500">Draws tiny current</span>
                        </div>
                        <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
                            <span class="text-xs font-bold text-rose-400 block mb-1">Electric Heater Coil</span>
                            <div class="text-[11px] text-slate-300">R = 100 Ω, V = 220 V</div>
                            <div class="text-base font-mono font-extrabold text-rose-300 mt-1">I = 2.20 A</div>
                            <span class="text-[10px] text-slate-500">Draws 12× more current!</span>
                        </div>
                    </div>
                `;
                desc.textContent = 'Same 220 V source: Bulb draws only 0.18 A due to high filament resistance, while heater coil draws 2.2 A.';
            }} else {{
                b2.className = 'px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 text-white';
                b1.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700';
                content.innerHTML = `
                    <div class="p-3 bg-slate-900 rounded-xl border border-slate-800 text-center space-y-1">
                        <span class="text-xs font-bold text-emerald-400 block">Example 11.6 Wire Geometry Variation</span>
                        <div class="text-xs text-slate-300">Original wire: R₁ = ρ(l/A) = 4.0 Ω</div>
                        <div class="text-xs text-slate-300">Modified wire: Length l/2 and Cross-sectional area 2A</div>
                        <div class="text-sm font-mono font-bold text-amber-300 my-1">R₂ = ρ(l/2)/(2A) = (1/4) R₁ = (1/4)(4.0 Ω) = 1.0 Ω</div>
                        <span class="text-[11px] text-slate-400">Quartering length-to-area ratio reduces resistance to exactly 1 Ω!</span>
                    </div>
                `;
                desc.textContent = 'Example 11.6: Halving length and doubling cross-section reduces resistance to exactly one-fourth (1 Ω).';
            }}
        }}

        let sim11BulbBroken = false;
        function toggleSim11Bulb() {{
            sim11BulbBroken = !sim11BulbBroken;
            playTone(sim11BulbBroken ? 300 : 600, 'square', 0.12);
            const b1 = document.getElementById('sim11-b1');
            const b2 = document.getElementById('sim11-b2');
            const b3 = document.getElementById('sim11-b3');
            const btn = document.getElementById('btn-sim11-fuse');
            const desc = document.getElementById('sim11-desc');

            if (sim11BulbBroken) {{
                btn.textContent = 'Replace Broken Bulb #2';
                btn.className = 'px-3 py-1 rounded-lg text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition';
                b2.setAttribute('fill-opacity', '0');
                b2.setAttribute('stroke', '#475569');
                b1.setAttribute('fill-opacity', '0');
                b1.setAttribute('stroke', '#475569');
                b3.setAttribute('fill-opacity', '0');
                b3.setAttribute('stroke', '#475569');
                desc.textContent = 'CIRCUIT OPEN: Bulb #2 fused. Since all components share one single path in series, current drops to 0.00 A and all bulbs go dark!';
            }} else {{
                btn.textContent = 'Fuse / Break Bulb #2';
                btn.className = 'px-3 py-1 rounded-lg text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition';
                b1.setAttribute('fill-opacity', '0.4');
                b1.setAttribute('stroke', '#f59e0b');
                b2.setAttribute('fill-opacity', '0.4');
                b2.setAttribute('stroke', '#f59e0b');
                b3.setAttribute('fill-opacity', '0.4');
                b3.setAttribute('stroke', '#f59e0b');
                desc.textContent = 'All bulbs glowing in series. Click "Fuse / Break Bulb #2" to witness single-point failure shutting down the entire circuit!';
            }}
        }}

        const sim13States = {{ 1: true, 2: true, 3: true }};
        function toggleSim13App(id) {{
            sim13States[id] = !sim13States[id];
            playTone(500, 'sine', 0.06);
            const b = document.getElementById(`btn-app-${{id}}`);
            if (b) {{
                const st = sim13States[id];
                b.querySelector('span').textContent = st ? 'ON' : 'OFF';
                b.className = st ? b.className.replace('opacity-40', '') : b.className + ' opacity-40';
            }}
            let tot = 0;
            if (sim13States[1]) tot += 0.18;
            if (sim13States[2]) tot += 0.35;
            if (sim13States[3]) tot += 4.50;
            document.getElementById('sim13-total-current').textContent = `${{tot.toFixed(2)}} A`;
        }}

        function updateSim14Heat() {{
            const I = parseFloat(document.getElementById('sim14-curr').value);
            const R = 20.0;
            const t = 30.0;
            const H = I * I * R * t;

            document.getElementById('sim14-curr-val').textContent = `${{I.toFixed(1)}} A`;
            document.getElementById('sim14-heat-val').textContent = `${{H.toLocaleString()}} J (${{(H/1000).toFixed(1)}} kJ)`;

            const coil = document.getElementById('sim14-coil');
            const st = document.getElementById('sim14-temp-status');
            if (I >= 6.5) {{
                coil.setAttribute('stroke', '#fef08a');
                coil.setAttribute('filter', 'drop-shadow(0 0 16px #facc15)');
                st.textContent = 'Coil: White Incandescent Hot (~1100°C)';
                st.className = 'text-[10px] text-yellow-300 font-bold mt-1';
            }} else if (I >= 4.0) {{
                coil.setAttribute('stroke', '#f97316');
                coil.setAttribute('filter', 'drop-shadow(0 0 10px #ea580c)');
                st.textContent = 'Coil: Red Radiant Hot (~550°C)';
                st.className = 'text-[10px] text-amber-400 font-bold mt-1';
            }} else {{
                coil.setAttribute('stroke', '#78350f');
                coil.setAttribute('filter', 'none');
                st.textContent = 'Coil: Warm (~120°C)';
                st.className = 'text-[10px] text-slate-400 font-bold mt-1';
            }}
            playTone(450 + I * 15, 'sine', 0.04);
        }}

        let sim15Tripped = false;
        function updateSim15Fuse() {{
            if (sim15Tripped) return;
            const I = parseFloat(document.getElementById('sim15-load').value);
            document.getElementById('sim15-load-val').textContent = `${{I.toFixed(1)}} A`;
            const wire = document.getElementById('sim15-wire');
            const desc = document.getElementById('sim15-desc');

            if (I > 5.0) {{
                sim15Tripped = true;
                playTone(280, 'sawtooth', 0.25);
                wire.setAttribute('stroke', '#ef4444');
                setTimeout(() => {{
                    wire.setAttribute('stroke', 'none');
                    desc.innerHTML = '<span class="text-rose-400 font-bold">FUSE BLOWN! Current exceeded 5 A rating. Wire melted and safely interrupted the short circuit!</span>';
                }}, 300);
            }} else {{
                wire.setAttribute('stroke', '#38bdf8');
                desc.textContent = `Current (${{I.toFixed(1)}} A) is below 5 A rating: Fuse wire is conducting safely without overheating.`;
                playTone(460, 'sine', 0.04);
            }}
        }}

        function resetSim15Fuse() {{
            sim15Tripped = false;
            playTone(600, 'sine', 0.08);
            document.getElementById('sim15-load').value = '4';
            document.getElementById('sim15-load-val').textContent = '4.0 A';
            const wire = document.getElementById('sim15-wire');
            wire.setAttribute('stroke', '#38bdf8');
            document.getElementById('sim15-desc').textContent = 'Fuse replaced! Circuit conducting normally under 5 A limit.';
        }}

        function calcSim16Bill() {{
            const pWatts = parseFloat(document.getElementById('sim16-app').value);
            const hrs = parseFloat(document.getElementById('sim16-hrs').value);
            document.getElementById('sim16-hrs-val').textContent = `${{hrs}} hrs/day`;

            const kwh = (pWatts * hrs * 30) / 1000;
            const cost = kwh * 3.00;

            document.getElementById('sim16-kwh-val').textContent = `${{kwh.toFixed(1)}} kW·h (Units)`;
            document.getElementById('sim16-cost-val').textContent = `Rs ${{cost.toFixed(2)}}`;
            playTone(470, 'sine', 0.04);
        }}

        function loadExercisePart1(num) {{
            playTone(480, 'sine', 0.08);
            const box = document.getElementById('exercise-sol-box1');
            const solutions = {{
                1: "<strong>Exercise Q1:</strong> A wire of resistance R cut into 5 equal parts gives each part resistance r = R/5. Connected in parallel: 1/R' = 5/r = 5/(R/5) = 25/R ⇒ R' = R/25. Therefore, the ratio <strong>R/R' = 25</strong> (Option d) (NCERT Page 193).",
                2: "<strong>Exercise Q2:</strong> Electric power P = VI = I²R = V²/R. Therefore, the term <strong>IR²</strong> does NOT represent electrical power (Option b) (NCERT Page 193).",
                3: "<strong>Exercise Q3:</strong> Bulb rated 220 V, 100 W. Resistance R = V²/P = 220²/100 = 484 Ω. When operated at V' = 110 V, power consumed is P' = V'²/R = 110²/484 = 12100/484 = <strong>25 W</strong> (Option d) (NCERT Page 193).",
                4: "<strong>Exercise Q4:</strong> In series: Rs = 2R ⇒ Hs = V²t / (2R). In parallel: Rp = R/2 ⇒ Hp = V²t / (R/2) = 2V²t/R. Ratio Hs/Hp = (1/2)/2 = <strong>1:4</strong> (Option c) (NCERT Page 193).",
                5: "<strong>Exercise Q5:</strong> A voltmeter is always connected in <strong>parallel</strong> across the two points between which potential difference is to be measured, because it has very high resistance and draws negligible current (NCERT Page 193).",
                6: "<strong>Exercise Q6:</strong> d = 0.5 mm = 5 × 10⁻⁴ m, ρ = 1.6 × 10⁻⁸ Ω·m, R = 10 Ω.<br>Area A = π d² / 4 = π (5 × 10⁻⁴)² / 4 = 1.963 × 10⁻⁷ m².<br>Length l = RA / ρ = (10 × 1.963 × 10⁻⁷) / (1.6 × 10⁻⁸) = <strong>122.7 m</strong>.<br>If diameter is doubled, cross-sectional area increases 4 times, so resistance becomes <strong>one-fourth: 10 / 4 = 2.5 Ω</strong>.",
                7: "<strong>Exercise Q7:</strong> Plotting V vs I gives a straight line through the origin. Resistance R = ΔV / ΔI = (13.2 - 1.6) / (4.0 - 0.5) = 11.6 / 3.5 ≈ <strong>3.3 Ω</strong> (NCERT Page 193).",
                8: "<strong>Exercise Q8:</strong> V = 12 V, I = 2.5 mA = 2.5 × 10⁻³ A.<br>Resistance R = V / I = 12 / (2.5 × 10⁻³) = <strong>4800 Ω = 4.8 kΩ</strong> (NCERT Page 193).",
                9: "<strong>Exercise Q9:</strong> Resistors 0.2, 0.3, 0.4, 0.5, 12 Ω in series with a 9 V battery.<br>Total resistance Rs = 0.2 + 0.3 + 0.4 + 0.5 + 12 = 13.4 Ω.<br>Current I = V / Rs = 9 / 13.4 = <strong>0.67 A</strong>. In a series circuit, the identical current of <strong>0.67 A</strong> flows through all resistors, including the 12 Ω resistor!"
            }};
            box.innerHTML = solutions[num] || "Solution not found.";
        }}

        function loadExercisePart2(num) {{
            playTone(490, 'sine', 0.08);
            const box = document.getElementById('exercise-sol-box2');
            const solutions = {{
                10: "<strong>Exercise Q10:</strong> Let n resistors of 176 Ω be connected in parallel. Total resistance Rp = V/I = 220/5 = 44 Ω.<br>Since Rp = R/n ⇒ 44 = 176/n ⇒ n = 176/44 = <strong>4 resistors</strong> (NCERT Page 193).",
                11: "<strong>Exercise Q11:</strong> Three resistors of 6 Ω each:<br>(i) For 9 Ω: Connect two in parallel (6 ∥ 6 = 3 Ω) in series with the third (3 + 6 = <strong>9 Ω</strong>).<br>(ii) For 4 Ω: Connect two in series (6 + 6 = 12 Ω) in parallel with the third (12 ∥ 6 = (12 × 6)/(18) = <strong>4 Ω</strong>).",
                12: "<strong>Exercise Q12:</strong> Max allowable current I = 5 A on 220 V. Max power P = VI = 220 × 5 = 1100 W.<br>Each lamp is 10 W. Number of lamps n = 1100 / 10 = <strong>110 lamps</strong> (NCERT Page 193).",
                13: "<strong>Exercise Q13:</strong> Two coils of 24 Ω each on 220 V:<br>(a) Separately: I = 220 / 24 = <strong>9.17 A</strong>.<br>(b) In series (R = 48 Ω): I = 220 / 48 = <strong>4.58 A</strong>.<br>(c) In parallel (R = 12 Ω): I = 220 / 12 = <strong>18.33 A</strong>.",
                14: "<strong>Exercise Q14:</strong> Power in 2 Ω resistor:<br>(i) 6 V with 1 Ω, 2 Ω in series: I = 6/(1+2) = 2 A ⇒ P = I²R = 2² × 2 = <strong>8 W</strong>.<br>(ii) 4 V with 12 Ω, 2 Ω in parallel: Voltage across 2 Ω is 4 V ⇒ P = V²/R = 4² / 2 = <strong>8 W</strong>.<br><em>Result:</em> Both circuits consume the exact same power (8 W) in the 2 Ω resistor!",
                15: "<strong>Exercise Q15:</strong> Two lamps (100 W & 60 W at 220 V) in parallel.<br>Current I₁ = 100/220 = 0.455 A, I₂ = 60/220 = 0.273 A.<br>Total line current I = I₁ + I₂ = 0.455 + 0.273 = <strong>0.727 A ≈ 0.73 A</strong>.",
                16: "<strong>Exercise Q16:</strong> Energy comparison:<br>• TV (250 W, 1 h): E = 250 × 3600 = <strong>9.0 × 10⁵ J</strong> (250 Wh).<br>• Toaster (1200 W, 10 min): E = 1200 × 600 = <strong>7.2 × 10⁵ J</strong> (200 Wh).<br>The <strong>250 W TV set consumes more energy</strong>!",
                17: "<strong>Exercise Q17:</strong> Heater with R = 44 Ω, I = 5 A.<br>Rate of heat development is Power: P = I²R = 5² × 44 = 25 × 44 = <strong>1100 J/s = 1100 W</strong>.",
                18: "<strong>Exercise Q18:</strong> (a) Tungsten has high melting point (3380°C) and retains intense heat to emit light.<br>(b) Alloys have higher resistivity and do not oxidise (burn) at red-hot temperatures.<br>(c) In series, current is uniform; failure of one device breaks the entire circuit for all other appliances.<br>(d) Resistance is inversely proportional to cross-sectional area (R ∝ 1/A).<br>(e) Copper and aluminium have extremely low resistivity, minimizing power losses during transmission."
            }};
            box.innerHTML = solutions[num] || "Solution not found.";
        }}

        window.addEventListener('DOMContentLoaded', () => {{
            showSlide(0);
            updateSim2Charge();
            updateSim3Potential();
            updateSim5Ohm();
            updateSim7Wire();
            updateSim14Heat();
            calcSim16Bill();
            document.body.addEventListener('click', () => initAudio(), {{ once: true }});
            document.body.addEventListener('keydown', () => initAudio(), {{ once: true }});
        }});
    </script>
</body>
</html>
"""

    os.makedirs("public/animations", exist_ok=True)
    out_path = "public/animations/electricity.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"Successfully generated {out_path} ({len(html_template)} bytes)")

if __name__ == '__main__':
    generate_html()
