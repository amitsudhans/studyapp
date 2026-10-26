#!/usr/bin/env python3
"""
Full Generator for NCERT Class 10 Science, Chapter 12: Magnetic Effects of Electric Current
Master Interactive Multimedia Lab
File: public/animations/magnetic-effects-of-electric-current.html
"""

import json
import os
import sys

sys.path.append(os.path.abspath('.agents'))
from magnetic_effects_data import CONTENT_SLIDES, QUIZ_SLIDES

ALL_SLIDES = CONTENT_SLIDES + QUIZ_SLIDES

def get_simulator_markup(s_idx):
    """Generate interactive SVG laboratory simulators for all 16 content slides."""
    if s_idx == 0:
        # Slide 1: Oersted's Needle Deflection
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 12.1: Oersted's Compass Deflection Experiment
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="toggleSim1Current()" id="btn-sim1-power" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition flex items-center gap-1.5">
                        <span id="sim1-power-dot" class="w-2 h-2 rounded-full bg-white animate-pulse"></span>
                        <span id="sim1-power-text">Current: ON (Needle Deflected)</span>
                    </button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <svg id="svg-sim1" viewBox="0 0 500 220" class="w-full max-w-lg h-auto">
                    <!-- Circuit Wires -->
                    <rect x="70" y="30" width="360" height="150" rx="10" fill="none" stroke="#475569" stroke-width="4"/>
                    
                    <!-- Straight Thick Copper Wire XY at Top -->
                    <line x1="160" y1="30" x2="340" y2="30" stroke="#f59e0b" stroke-width="6"/>
                    <text x="150" y="22" fill="#f59e0b" font-size="10" font-weight="bold">X</text>
                    <text x="345" y="22" fill="#f59e0b" font-size="10" font-weight="bold">Y</text>
                    <text x="250" y="18" fill="#fbbf24" font-size="9" text-anchor="middle" font-weight="bold">Thick Copper Conductor XY</text>

                    <!-- Battery at Bottom -->
                    <g transform="translate(250, 180)">
                        <rect x="-25" y="-8" width="50" height="20" fill="#0f172a"/>
                        <line x1="-10" y1="-10" x2="-10" y2="10" stroke="#f59e0b" stroke-width="4"/>
                        <line x1="10" y1="-6" x2="10" y2="6" stroke="#64748b" stroke-width="6"/>
                        <text x="-16" y="2" fill="#f59e0b" font-size="9" font-weight="bold">+</text>
                        <text x="16" y="2" fill="#94a3b8" font-size="9" font-weight="bold">-</text>
                    </g>

                    <!-- Resistor & Key -->
                    <path d="M 90 100 L 96 90 L 108 110 L 120 90 L 132 110 L 138 100" fill="none" stroke="#94a3b8" stroke-width="2.5"/>
                    <circle cx="410" cy="100" r="4" fill="#38bdf8"/>
                    <text x="410" y="120" fill="#38bdf8" font-size="8" text-anchor="middle">Key (K)</text>

                    <!-- Compass placed directly under wire XY (250, 75) -->
                    <g id="sim1-compass" transform="translate(250, 75)">
                        <circle cx="0" cy="0" r="34" fill="#0f172a" stroke="#64748b" stroke-width="2.5"/>
                        <circle cx="0" cy="0" r="3" fill="#cbd5e1"/>
                        <text x="0" y="-22" fill="#94a3b8" font-size="7" text-anchor="middle">N</text>
                        <text x="0" y="28" fill="#94a3b8" font-size="7" text-anchor="middle">S</text>
                        <text x="26" y="3" fill="#94a3b8" font-size="7" text-anchor="middle">E</text>
                        <text x="-26" y="3" fill="#94a3b8" font-size="7" text-anchor="middle">W</text>
                        <!-- Compass Needle (Rotatable) -->
                        <g id="sim1-needle" transform="rotate(38)" class="transition-transform duration-500 ease-out">
                            <polygon points="0,-24 5,0 -5,0" fill="#ef4444"/>
                            <polygon points="0,24 5,0 -5,0" fill="#38bdf8"/>
                        </g>
                    </g>
                </svg>
                <div id="sim1-desc" class="text-xs text-amber-200 mt-2 text-center font-medium">
                    Current ON: Magnetic field produced by the current in wire XY exerts a torque on the compass needle, deflecting it away from the North-South line!
                </div>
            </div>
        </div>
        """
    elif s_idx == 1:
        # Slide 2: Magnetic Field & Iron Filings Pattern
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 12.2: Bar Magnet Field Lines & Iron Filings Pattern
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="tapSim2Board()" id="btn-sim2-tap" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white transition flex items-center gap-1.5">
                        <span>Tap Board (Align Filings)</span>
                    </button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <svg id="svg-sim2" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Drawing Board Outline -->
                    <rect x="30" y="15" width="440" height="170" rx="8" fill="#0f172a" stroke="#334155" stroke-width="2"/>
                    
                    <!-- Field Line Curves (Initially faint, brightens on tap) -->
                    <g id="sim2-field-curves" stroke="#38bdf8" fill="none" stroke-width="1.5" stroke-dasharray="4,2" opacity="0.3" class="transition-opacity duration-700">
                        <path d="M 210 100 C 170 30, 90 40, 60 100 C 90 160, 170 170, 210 100"/>
                        <path d="M 290 100 C 330 30, 410 40, 440 100 C 410 160, 330 170, 290 100"/>
                        <path d="M 210 90 C 150 10, 350 10, 290 90"/>
                        <path d="M 210 110 C 150 190, 350 190, 290 110"/>
                    </g>

                    <!-- Iron filings particles -->
                    <g id="sim2-filings" fill="#94a3b8" class="transition-all duration-700">
                        <circle cx="160" cy="80" r="1.5"/><circle cx="170" cy="65" r="1.5"/><circle cx="190" cy="55" r="1.5"/>
                        <circle cx="340" cy="80" r="1.5"/><circle cx="330" cy="65" r="1.5"/><circle cx="310" cy="55" r="1.5"/>
                        <circle cx="160" cy="120" r="1.5"/><circle cx="170" cy="135" r="1.5"/><circle cx="190" cy="145" r="1.5"/>
                        <circle cx="340" cy="120" r="1.5"/><circle cx="330" cy="135" r="1.5"/><circle cx="310" cy="145" r="1.5"/>
                        <circle cx="250" cy="40" r="1.5"/><circle cx="250" cy="160" r="1.5"/>
                    </g>

                    <!-- Permanent Bar Magnet in Center (250, 100) -->
                    <g transform="translate(190, 85)">
                        <!-- North Pole (Red) -->
                        <rect x="0" y="0" width="60" height="30" fill="#ef4444"/>
                        <text x="30" y="19" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">N</text>
                        <!-- South Pole (Blue) -->
                        <rect x="60" y="0" width="60" height="30" fill="#0284c7"/>
                        <text x="90" y="19" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">S</text>
                    </g>
                </svg>
                <div id="sim2-desc" class="text-xs text-cyan-200 mt-2 text-center font-medium">
                    Activity 12.2: Sprinkled iron filings experience magnetic forces and align into curved patterns that reveal the invisible magnetic field lines!
                </div>
            </div>
        </div>
        """
    elif s_idx == 2:
        # Slide 3: Compass Plotting & Continuous Closed Curves
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 12.3: Compass Step-by-Step Field Line Tracer
                </span>
                <button onclick="advanceSim3Compass()" id="btn-sim3-step" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition">
                    Advance Plotting Compass
                </button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <svg id="svg-sim3" viewBox="0 0 500 210" class="w-full max-w-lg h-auto">
                    <!-- Traced Path -->
                    <path id="sim3-traced-line" d="M 200 90 C 170 30, 330 30, 300 90" fill="none" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="2,2"/>
                    
                    <!-- Bar Magnet -->
                    <g transform="translate(190, 95)">
                        <rect x="0" y="0" width="60" height="28" fill="#ef4444"/>
                        <text x="30" y="18" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">N</text>
                        <rect x="60" y="0" width="60" height="28" fill="#0284c7"/>
                        <text x="90" y="18" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">S</text>
                    </g>

                    <!-- Step Markers -->
                    <circle cx="200" cy="70" r="3" fill="#fbbf24"/>
                    <circle cx="225" cy="45" r="3" fill="#fbbf24"/>
                    <circle cx="250" cy="35" r="3" fill="#fbbf24"/>
                    <circle cx="275" cy="45" r="3" fill="#fbbf24"/>
                    <circle cx="300" cy="70" r="3" fill="#fbbf24"/>

                    <!-- Animated Plotting Compass -->
                    <g id="sim3-compass" transform="translate(200, 70)" class="transition-all duration-500">
                        <circle cx="0" cy="0" r="14" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5"/>
                        <polygon points="0,-10 3,0 -3,0" fill="#ef4444"/>
                        <polygon points="0,10 3,0 -3,0" fill="#38bdf8"/>
                    </g>
                </svg>
                <div id="sim3-desc" class="text-xs text-rose-200 mt-2 text-center font-medium">
                    Step 1: Compass placed near North pole. Its South needle tip points to magnet N, while its North tip points along the curved field line towards South.
                </div>
            </div>
        </div>
        """
    elif s_idx == 3:
        # Slide 4: Properties & Non-Intersection Proof
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-purple-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-purple-400"></span>
                    Interactive Lab 12.4: Non-Intersection Proof & Field Crowding
                </span>
                <button onclick="toggleSim4Paradox()" id="btn-sim4-paradox" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-purple-600 hover:bg-purple-500 text-white transition">
                    Test Hypothetical Intersection
                </button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <svg id="svg-sim4" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Normal Non-Intersecting Field Lines -->
                    <g id="sim4-normal-lines" stroke="#818cf8" fill="none" stroke-width="2">
                        <path d="M 50 140 Q 250 20 450 140"/>
                        <path d="M 90 140 Q 250 50 410 140"/>
                        <path d="M 130 140 Q 250 80 370 140"/>
                    </g>
                    <!-- Crowded Pole Indicators -->
                    <circle cx="50" cy="140" r="16" fill="#ef4444" fill-opacity="0.2"/>
                    <circle cx="450" cy="140" r="16" fill="#0284c7" fill-opacity="0.2"/>
                    <text x="50" y="145" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">N</text>
                    <text x="450" y="145" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">S</text>

                    <!-- Hypothetical Intersection (Hidden initially) -->
                    <g id="sim4-paradox-group" class="hidden">
                        <line x1="200" y1="40" x2="300" y2="100" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="3,3"/>
                        <line x1="200" y1="100" x2="300" y2="40" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="3,3"/>
                        <circle cx="250" cy="70" r="6" fill="#f43f5e"/>
                        <text x="250" y="55" fill="#f43f5e" font-size="9" font-weight="bold" text-anchor="middle">Intersection Point P</text>
                        <!-- Two diverging needle pointers -->
                        <line x1="250" y1="70" x2="280" y2="52" stroke="#fbbf24" stroke-width="2.5"/>
                        <polygon points="283,50 274,50 278,57" fill="#fbbf24"/>
                        <line x1="250" y1="70" x2="280" y2="88" stroke="#fbbf24" stroke-width="2.5"/>
                        <polygon points="283,90 278,83 274,90" fill="#fbbf24"/>
                    </g>
                </svg>
                <div id="sim4-desc" class="text-xs text-purple-200 mt-2 text-center font-medium">
                    Crowded lines at poles demonstrate high field strength. Field lines never intersect! Click button to explore the two-direction paradox.
                </div>
            </div>
        </div>
        """
    elif s_idx == 4:
        # Slide 5: Straight Conductor & Current Reversal
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 12.5: Straight Wire Current Reversal (Activity 12.4)
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim5Dir('north_south')" id="btn-sim5-ns" class="px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition">Current: N → S (East Deflection)</button>
                    <button onclick="setSim5Dir('south_north')" id="btn-sim5-sn" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Current: S → N (West Deflection)</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <svg id="svg-sim5" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Circuit Wires -->
                    <rect x="60" y="30" width="380" height="140" rx="8" fill="none" stroke="#475569" stroke-width="3"/>
                    <!-- Straight Conductor Wire over compass -->
                    <line x1="160" y1="30" x2="340" y2="30" stroke="#f59e0b" stroke-width="5"/>
                    <text x="170" y="22" fill="#94a3b8" font-size="8">North</text>
                    <text x="320" y="22" fill="#94a3b8" font-size="8">South</text>

                    <!-- Current Flow Arrow on Wire -->
                    <polygon id="sim5-flow-arrow" points="260,30 245,25 245,35" fill="#fef08a"/>

                    <!-- Compass Under Wire (250, 75) -->
                    <g transform="translate(250, 75)">
                        <circle cx="0" cy="0" r="32" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
                        <text x="0" y="-20" fill="#94a3b8" font-size="7" text-anchor="middle">N</text>
                        <text x="0" y="25" fill="#94a3b8" font-size="7" text-anchor="middle">S</text>
                        <text x="24" y="3" fill="#94a3b8" font-size="7" text-anchor="middle">E</text>
                        <text x="-24" y="3" fill="#94a3b8" font-size="7" text-anchor="middle">W</text>
                        <!-- Deflecting needle -->
                        <g id="sim5-needle" transform="rotate(40)" class="transition-transform duration-500">
                            <polygon points="0,-22 4,0 -4,0" fill="#ef4444"/>
                            <polygon points="0,22 4,0 -4,0" fill="#38bdf8"/>
                        </g>
                    </g>
                </svg>
                <div id="sim5-desc" class="text-xs text-amber-200 mt-2 text-center font-medium">
                    Fig 12.5(a): Current flows North to South over needle → North pole of compass deflects towards the EAST!
                </div>
            </div>
        </div>
        """
    elif s_idx == 5:
        # Slide 6: Concentric Circles & Inverse Distance Law
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                    Interactive Lab 12.6: Concentric Circles & B ∝ I / r
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300 font-semibold">Current (I):</label>
                    <input type="range" id="sim6-curr" min="1" max="5" value="3" oninput="updateSim6Field()" class="w-24 sm:w-32 accent-emerald-400 cursor-pointer">
                    <span id="sim6-curr-val" class="text-xs font-mono font-bold text-emerald-400">3.0 A</span>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <svg id="svg-sim6" viewBox="0 0 500 210" class="w-full max-w-lg h-auto">
                    <!-- Horizontal Cardboard in Perspective -->
                    <polygon points="100,160 400,160 460,70 160,70" fill="#1e293b" fill-opacity="0.8" stroke="#475569" stroke-width="2"/>
                    <text x="150" y="85" fill="#94a3b8" font-size="8">Horizontal Cardboard</text>

                    <!-- Concentric Circles on Cardboard -->
                    <g id="sim6-circles" stroke="#38bdf8" fill="none" stroke-width="2" class="transition-all duration-300">
                        <ellipse cx="280" cy="115" rx="35" ry="16"/>
                        <ellipse cx="280" cy="115" rx="70" ry="32"/>
                        <ellipse cx="280" cy="115" rx="105" ry="48"/>
                    </g>

                    <!-- Vertical Conductor Wire passing normal through cardboard -->
                    <line x1="280" y1="15" x2="280" y2="195" stroke="#f59e0b" stroke-width="5"/>
                    <polygon points="280,25 275,38 285,38" fill="#fef08a"/>
                    <text x="290" y="30" fill="#f59e0b" font-size="9" font-weight="bold">I (Upward)</text>

                    <!-- Compass at Point P (near) vs Point Q (far) -->
                    <circle cx="280" cy="115" r="4" fill="#ef4444"/>
                    <circle cx="350" cy="115" r="3" fill="#fbbf24"/>
                    <text x="350" y="128" fill="#fbbf24" font-size="8" text-anchor="middle">Point P</text>
                </svg>
                <div id="sim6-desc" class="text-xs text-emerald-200 mt-2 text-center font-medium">
                    Concentric circles widen with distance. As distance r increases, magnetic field B decreases (B ∝ 1/r). Increasing current increases field strength (B ∝ I).
                </div>
            </div>
        </div>
        """
    elif s_idx == 6:
        # Slide 7: Right-Hand Thumb Rule & Example 12.1
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 12.7: Right-Hand Thumb & Corkscrew Simulator
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim7Thumb('up')" id="btn-sim7-up" class="px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 text-white transition">Current Up (Anticlockwise)</button>
                    <button onclick="setSim7Thumb('down')" id="btn-sim7-down" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Current Down (Clockwise)</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <svg id="svg-sim7" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Vertical Conductor Wire -->
                    <line x1="250" y1="20" x2="250" y2="180" stroke="#f59e0b" stroke-width="6"/>
                    
                    <!-- Right-Hand Stylized Representation -->
                    <rect x="225" y="70" width="50" height="60" rx="12" fill="#d97706" fill-opacity="0.3" stroke="#f59e0b" stroke-width="2"/>
                    
                    <!-- Thumb pointing direction -->
                    <g id="sim7-thumb-arrow">
                        <line x1="250" y1="65" x2="250" y2="35" stroke="#ef4444" stroke-width="4"/>
                        <polygon points="250,30 244,42 256,42" fill="#ef4444"/>
                        <text x="262" y="45" fill="#ef4444" font-size="9" font-weight="bold">Thumb: Current (I)</text>
                    </g>

                    <!-- Circular Wrapping Magnetic Field Lines with direction arrows -->
                    <g id="sim7-field-arrows" stroke="#38bdf8" fill="none" stroke-width="2.5">
                        <ellipse cx="250" cy="100" rx="80" ry="24"/>
                        <!-- Arrowhead indicating anticlockwise -->
                        <polygon id="sim7-arrow-front" points="250,124 240,118 240,130" fill="#38bdf8"/>
                        <text x="250" y="142" fill="#38bdf8" font-size="9" text-anchor="middle" font-weight="bold">Curled Fingers: Magnetic Field (B)</text>
                    </g>
                </svg>
                <div id="sim7-desc" class="text-xs text-cyan-200 mt-2 text-center font-medium">
                    Thumb points along upward current → Curled fingers wrap anticlockwise when viewed from above (Maxwell's Corkscrew Rule).
                </div>
            </div>
        </div>
        """
    elif s_idx == 7:
        # Slide 8: Circular Current Loop Magnetic Field
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 12.8: Circular Current Loop & Center Straight Line Field
                </span>
                <span class="text-xs font-mono text-slate-400">Figure 12.8</span>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <svg id="svg-sim8" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Circular Loop (Perspective Ellipse) -->
                    <ellipse cx="250" cy="100" rx="90" ry="70" fill="none" stroke="#f59e0b" stroke-width="4"/>
                    <polygon points="250,30 240,25 240,35" fill="#f59e0b"/>
                    <text x="250" y="22" fill="#f59e0b" font-size="8" text-anchor="middle">Clockwise Current</text>

                    <!-- Magnetic Field Lines (Straight at center, curved at edges) -->
                    <!-- Central straight line -->
                    <line x1="250" y1="20" x2="250" y2="180" stroke="#38bdf8" stroke-width="3"/>
                    <polygon points="250,185 245,172 255,172" fill="#38bdf8"/>
                    <text x="250" y="196" fill="#38bdf8" font-size="8" text-anchor="middle" font-weight="bold">Straight Line at Center</text>

                    <!-- Expanding arcs on left and right -->
                    <path d="M 220 25 C 200 60, 200 140, 220 175" fill="none" stroke="#38bdf8" stroke-width="2"/>
                    <path d="M 280 25 C 300 60, 300 140, 280 175" fill="none" stroke="#38bdf8" stroke-width="2"/>
                    <ellipse cx="160" cy="100" rx="20" ry="12" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
                    <ellipse cx="340" cy="100" rx="20" ry="12" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
                </svg>
                <div id="sim8-desc" class="text-xs text-rose-200 mt-2 text-center font-medium">
                    At the center of the circular loop, the magnetic field lines from all segments combine in the same direction, appearing as uniform parallel straight lines!
                </div>
            </div>
        </div>
        """
    elif s_idx == 8:
        # Slide 9: Circular Coil with N Turns
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-purple-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-purple-400"></span>
                    Interactive Lab 12.9: N-Turn Magnetic Multiplier (B = n · B₁)
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300 font-semibold">Turns (n):</label>
                    <input type="range" id="sim9-turns" min="1" max="50" value="10" oninput="updateSim9Turns()" class="w-24 sm:w-32 accent-purple-400 cursor-pointer">
                    <span id="sim9-turns-val" class="text-xs font-mono font-bold text-purple-400">10 Turns</span>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <div class="grid grid-cols-2 gap-4 w-full max-w-lg mb-2 text-center">
                    <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
                        <span class="text-[10px] text-slate-400 uppercase block">Single Turn Field (B₁)</span>
                        <span class="text-base font-mono font-bold text-white">0.20 mT</span>
                    </div>
                    <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
                        <span class="text-[10px] text-slate-400 uppercase block">N-Turn Resultant Field (B_total)</span>
                        <span id="sim9-btot-val" class="text-base font-mono font-extrabold text-purple-300">2.00 mT (10×)</span>
                    </div>
                </div>
                <div id="sim9-desc" class="text-xs text-purple-200 text-center font-medium">
                    Because current in each turn flows in the exact same direction, their individual magnetic fields add together algebraically: B = n · B₁!
                </div>
            </div>
        </div>
        """
    elif s_idx == 9:
        # Slide 10: The Solenoid & Electromagnet
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                    Interactive Lab 12.10: Solenoid & Soft Iron Electromagnet (Fig 12.10 / 12.11)
                </span>
                <button onclick="toggleSim10Core()" id="btn-sim10-core" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">
                    Insert Soft Iron Core
                </button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <svg id="svg-sim10" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Soft Iron Core (Hidden initially) -->
                    <rect id="sim10-core" x="140" y="88" width="220" height="24" rx="4" fill="#64748b" class="hidden transition-all"/>

                    <!-- Solenoid Helical Coil Turns -->
                    <g id="sim10-solenoid-coils" stroke="#f59e0b" fill="none" stroke-width="4">
                        <path d="M 150 75 Q 160 125 170 75"/>
                        <path d="M 170 75 Q 180 125 190 75"/>
                        <path d="M 190 75 Q 200 125 210 75"/>
                        <path d="M 210 75 Q 220 125 230 75"/>
                        <path d="M 230 75 Q 240 125 250 75"/>
                        <path d="M 250 75 Q 260 125 270 75"/>
                        <path d="M 270 75 Q 280 125 290 75"/>
                        <path d="M 290 75 Q 300 125 310 75"/>
                        <path d="M 310 75 Q 320 125 330 75"/>
                        <path d="M 330 75 Q 340 125 350 75"/>
                    </g>

                    <!-- Uniform Internal Parallel Field Lines -->
                    <g stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,2">
                        <line x1="130" y1="92" x2="370" y2="92"/>
                        <line x1="130" y1="100" x2="370" y2="100"/>
                        <line x1="130" y1="108" x2="370" y2="108"/>
                    </g>
                    <!-- External Bar Magnet-like curves -->
                    <path d="M 130 92 C 80 40, 420 40, 370 92" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,3"/>
                    <path d="M 130 108 C 80 160, 420 160, 370 108" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,3"/>
                    <text x="120" y="104" fill="#ef4444" font-size="10" font-weight="bold">N</text>
                    <text x="380" y="104" fill="#38bdf8" font-size="10" font-weight="bold">S</text>
                </svg>
                <div id="sim10-desc" class="text-xs text-emerald-200 mt-2 text-center font-medium">
                    Solenoid: Parallel straight lines inside indicate a uniform magnetic field. Click button to insert soft iron core and create an electromagnet!
                </div>
            </div>
        </div>
        """
    elif s_idx == 10:
        # Slide 11: Magnetic Force on Conductor (Activity 12.7)
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 12.11: The Kicking Aluminium Rod (Activity 12.7)
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="toggleSim11Current()" id="btn-sim11-dir" class="px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition">Current: B → A (Displaces Left)</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <svg id="svg-sim11" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Horseshoe Magnet Poles -->
                    <!-- Lower North Pole -->
                    <rect x="210" y="130" width="80" height="40" fill="#ef4444" rx="3"/>
                    <text x="250" y="155" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">N</text>
                    <!-- Upper South Pole -->
                    <rect x="210" y="30" width="80" height="40" fill="#0284c7" rx="3"/>
                    <text x="250" y="55" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">S</text>
                    
                    <!-- Upward Magnetic Field Lines -->
                    <g stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="2,2">
                        <line x1="230" y1="130" x2="230" y2="70"/><line x1="250" y1="130" x2="250" y2="70"/><line x1="270" y1="130" x2="270" y2="70"/>
                    </g>
                    <text x="200" y="105" fill="#38bdf8" font-size="8">B (Upward)</text>

                    <!-- Suspended Aluminium Rod AB (Horizontal) -->
                    <g id="sim11-rod" transform="translate(0, 0)" class="transition-transform duration-500">
                        <!-- Suspension wires -->
                        <line x1="220" y1="10" x2="220" y2="100" stroke="#94a3b8" stroke-width="1.5"/>
                        <line x1="280" y1="10" x2="280" y2="100" stroke="#94a3b8" stroke-width="1.5"/>
                        <!-- Rod AB -->
                        <line x1="180" y1="100" x2="320" y2="100" stroke="#f59e0b" stroke-width="6"/>
                        <text x="170" y="104" fill="#f59e0b" font-size="9" font-weight="bold">A</text>
                        <text x="325" y="104" fill="#f59e0b" font-size="9" font-weight="bold">B</text>
                    </g>
                </svg>
                <div id="sim11-desc" class="text-xs text-amber-200 mt-2 text-center font-medium">
                    Current flows B to A; magnetic field is vertically upward. By Fleming's Left-Hand Rule, force pushes rod towards the LEFT!
                </div>
            </div>
        </div>
        """
    elif s_idx == 11:
        # Slide 12: Fleming's Left-Hand Rule
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 12.12: Fleming's Left-Hand Rule 3D Orthogonal Engine
                </span>
                <span class="text-xs font-mono text-slate-400">FBI / Father-Mother-Child</span>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 w-full max-w-lg mb-2 text-center">
                <div class="p-3 bg-slate-900 rounded-xl border border-rose-500/30">
                    <span class="text-[10px] text-rose-400 font-bold block uppercase">Thumb</span>
                    <span class="text-sm font-bold text-white">Motion / Force (F)</span>
                </div>
                <div class="p-3 bg-slate-900 rounded-xl border border-cyan-500/30">
                    <span class="text-[10px] text-cyan-400 font-bold block uppercase">Forefinger</span>
                    <span class="text-sm font-bold text-white">Magnetic Field (B)</span>
                </div>
                <div class="p-3 bg-slate-900 rounded-xl border border-amber-500/30">
                    <span class="text-[10px] text-amber-400 font-bold block uppercase">Middle Finger</span>
                    <span class="text-sm font-bold text-white">Current (I)</span>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 w-full max-w-lg text-center">
                <div class="text-xs font-bold text-white mb-1">Example 12.2 Electron Beam Solver:</div>
                <div class="text-xs text-slate-300">
                    Electron moves downwards $\\implies$ Current is <strong>UPWARDS</strong>. Magnetic field is to the <strong>RIGHT</strong>.<br>
                    Applying Fleming's Left-Hand Rule directs the force <strong>INTO THE PAGE</strong>!
                </div>
            </div>
        </div>
        """
    elif s_idx == 12:
        # Slide 13: Magnetism in Medicine & MRI
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 12.13: Bio-Magnetism & Magnetic Resonance Imaging (MRI)
                </span>
                <span class="text-xs font-mono text-slate-400">10⁻⁹ Earth Field</span>
            </div>
            <div class="grid grid-cols-2 gap-3 w-full max-w-lg mb-2 text-center">
                <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span class="text-xs font-bold text-rose-400 block mb-1">Human Heart</span>
                    <span class="text-[11px] text-slate-300">Cardiac muscle pacemaker currents generate periodic magnetic pulses.</span>
                </div>
                <div class="p-3 bg-slate-900 rounded-xl border border-slate-800">
                    <span class="text-xs font-bold text-purple-400 block mb-1">Human Brain</span>
                    <span class="text-[11px] text-slate-300">Billions of synaptic ion channels establish diagnostic neural magnetic signals.</span>
                </div>
            </div>
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-xs text-slate-300 text-center">
                <strong>MRI Technology:</strong> Non-invasive imaging detecting proton spin resonance in body water and fat molecules under high magnetic fields.
            </div>
        </div>
        """
    elif s_idx == 13:
        # Slide 14: Domestic Electric Circuits & Earthing
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                    Interactive Lab 12.14: Domestic Wiring & Safety Earth Wire (220 V, 50 Hz)
                </span>
                <button onclick="toggleSim14Fault()" id="btn-sim14-fault" class="px-2.5 py-1 rounded text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition">
                    Simulate Live Wire Touching Metal Body
                </button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <svg id="svg-sim14" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Three Mains Supply Lines at Left -->
                    <!-- Live Wire (Red) -->
                    <line x1="30" y1="40" x2="350" y2="40" stroke="#ef4444" stroke-width="3"/>
                    <text x="35" y="32" fill="#ef4444" font-size="8" font-weight="bold">Live Wire (Red, 220 V)</text>

                    <!-- Neutral Wire (Black) -->
                    <line x1="30" y1="90" x2="350" y2="90" stroke="#64748b" stroke-width="3"/>
                    <text x="35" y="82" fill="#94a3b8" font-size="8" font-weight="bold">Neutral Wire (Black, 0 V)</text>

                    <!-- Earth Wire (Green) -->
                    <line x1="30" y1="140" x2="350" y2="140" stroke="#22c55e" stroke-width="3"/>
                    <text x="35" y="132" fill="#22c55e" font-size="8" font-weight="bold">Earth Wire (Green, Grounded)</text>

                    <!-- Metallic Appliance (e.g. Electric Press / Toaster) at Right (380, 80) -->
                    <rect x="350" y="30" width="100" height="120" rx="10" fill="#1e293b" stroke="#cbd5e1" stroke-width="2"/>
                    <text x="400" y="55" fill="#ffffff" font-size="9" text-anchor="middle" font-weight="bold">Metallic Appliance</text>
                    
                    <!-- Fault indicator arrow to ground -->
                    <line id="sim14-fault-path" x1="400" y1="140" x2="400" y2="175" stroke="#22c55e" stroke-width="3"/>
                    <path d="M 390 175 L 410 175 M 394 180 L 406 180 M 398 185 L 402 185" stroke="#22c55e" stroke-width="2"/>
                    <text x="400" y="196" fill="#22c55e" font-size="7" text-anchor="middle">Earth Plate in Ground</text>
                </svg>
                <div id="sim14-desc" class="text-xs text-emerald-200 mt-2 text-center font-medium">
                    Green Earth wire connects appliance metal casing directly to deep earth plate, providing zero-potential shock protection!
                </div>
            </div>
        </div>
        """
    elif s_idx == 14:
        # Slide 15: Overloading, Short-Circuiting & Safety Fuse
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 12.15: Short-Circuit & 2 kW Oven Fuse Breaker
                </span>
                <button onclick="resetSim15Circuit()" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 transition">
                    Reset Circuit & Fuse
                </button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <div class="grid grid-cols-2 gap-3 w-full max-w-lg mb-3">
                    <button onclick="triggerSim15Event('short')" class="p-2.5 rounded-xl text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition text-center">
                        Simulate Short-Circuit (Live-Neutral Contact)
                    </button>
                    <button onclick="triggerSim15Event('oven')" class="p-2.5 rounded-xl text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition text-center">
                        2 kW Oven on 5 A Line (9.09 A)
                    </button>
                </div>
                <!-- Circuit Display Box -->
                <div id="sim15-output" class="p-3 bg-slate-900 rounded-xl border border-slate-800 w-full max-w-lg text-center text-xs leading-relaxed text-slate-300">
                    Normal operating condition: Current is within safe parameters. Click an overload or short-circuit event above to witness fuse protection!
                </div>
            </div>
        </div>
        """
    elif s_idx == 15:
        # Slide 16: Complete NCERT Exercises Solutions (Q1 to Q9)
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-indigo-400"></span>
                    NCERT Exercise Interactive Solver (Q1 to Q9)
                </span>
                <span class="text-xs text-slate-400 font-mono">Official Verified Solutions</span>
            </div>
            <div class="grid grid-cols-3 sm:grid-cols-5 gap-2 mb-3">
                <button onclick="loadExerciseCh12(1)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q1 (Concentric Circles)</button>
                <button onclick="loadExerciseCh12(2)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q2 (Short Circuit I)</button>
                <button onclick="loadExerciseCh12(3)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q3 (True / False)</button>
                <button onclick="loadExerciseCh12(4)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q4 (2 Field Methods)</button>
                <button onclick="loadExerciseCh12(5)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q5 (Max Force 90°)</button>
                <button onclick="loadExerciseCh12(6)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q6 (Downward Field)</button>
                <button onclick="loadExerciseCh12(7)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q7 (State Rules)</button>
                <button onclick="loadExerciseCh12(8)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q8 (Short Circuit)</button>
                <button onclick="loadExerciseCh12(9)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q9 (Earth Wire Role)</button>
            </div>
            <div id="exercise-sol-box12" class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs sm:text-sm text-slate-300 min-h-[130px] leading-relaxed">
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
                        <span>You have reached the last slide of this chapter (Chapter 12: Magnetic Effects of Electric Current)!</span>
                    </div>
                    <p class="text-xs text-slate-300">Congratulations! You have completed all 16 master interactive lessons and all 40 mastery challenge questions covering the entire NCERT textbook.</p>
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
                        <span>You have reached the last slide of this chapter (Chapter 12: Magnetic Effects of Electric Current)!</span>
                    </div>
                    <p class="text-xs text-slate-300">Congratulations! You have completed all 16 master interactive lessons and all 40 mastery challenge questions covering the entire NCERT textbook.</p>
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
    <title>NCERT Class 10 Science • Chapter 12: Magnetic Effects of Electric Current</title>
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
                        NCERT Class 10 Science • Chapter 12: Magnetic Effects of Electric Current
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
        let sim1CurrentOn = true;
        function toggleSim1Current() {{
            sim1CurrentOn = !sim1CurrentOn;
            playTone(470, 'sine', 0.08);
            const btnText = document.getElementById('sim1-power-text');
            const btnDot = document.getElementById('sim1-power-dot');
            const needle = document.getElementById('sim1-needle');
            const desc = document.getElementById('sim1-desc');

            if (sim1CurrentOn) {{
                btnText.textContent = 'Current: ON (Needle Deflected)';
                btnDot.className = 'w-2 h-2 rounded-full bg-white animate-pulse';
                needle.setAttribute('transform', 'rotate(38)');
                desc.textContent = 'Current ON: Magnetic field produced by wire XY exerts a torque on the compass needle, deflecting it away from the North-South line!';
            }} else {{
                btnText.textContent = 'Current: OFF (North-South Aligned)';
                btnDot.className = 'w-2 h-2 rounded-full bg-slate-500';
                needle.setAttribute('transform', 'rotate(0)');
                desc.textContent = 'Current OFF: Magnetic field collapses. The compass needle returns to its natural geographic North-South alignment.';
            }}
        }}

        function tapSim2Board() {{
            playTone(520, 'sine', 0.1);
            const curves = document.getElementById('sim2-field-curves');
            curves.setAttribute('opacity', '0.9');
            const desc = document.getElementById('sim2-desc');
            desc.innerHTML = '<span class="text-white font-bold animate-pulse">Board tapped! Iron filings align cleanly along closed magnetic field curves.</span>';
        }}

        let sim3Step = 0;
        const sim3Coordinates = [
            {{ x: 200, y: 70, rot: -30, text: "Step 1: Compass near North pole; needle points along emerging field line." }},
            {{ x: 225, y: 45, rot: 15, text: "Step 2: Compass moved along arc; needle aligns with curve tangent." }},
            {{ x: 250, y: 35, rot: 90, text: "Step 3: Midpoint of magnetic field line; field is horizontal." }},
            {{ x: 275, y: 45, rot: 165, text: "Step 4: Nearing South pole; needle turns toward South end." }},
            {{ x: 300, y: 70, rot: 210, text: "Step 5: Arrived at South pole! Proving magnetic field lines are continuous closed curves." }}
        ];
        function advanceSim3Compass() {{
            sim3Step = (sim3Step + 1) % sim3Coordinates.length;
            playTone(450 + sim3Step * 30, 'sine', 0.08);
            const c = sim3Coordinates[sim3Step];
            const comp = document.getElementById('sim3-compass');
            if (comp) {{
                comp.setAttribute('transform', `translate(${{c.x}}, ${{c.y}}) rotate(${{c.rot}})`);
            }}
            document.getElementById('sim3-desc').textContent = c.text;
        }}

        let sim4ParadoxActive = false;
        function toggleSim4Paradox() {{
            sim4ParadoxActive = !sim4ParadoxActive;
            playTone(sim4ParadoxActive ? 320 : 500, 'square', 0.1);
            const grp = document.getElementById('sim4-paradox-group');
            const desc = document.getElementById('sim4-desc');
            if (sim4ParadoxActive) {{
                grp.classList.remove('hidden');
                desc.innerHTML = '<span class="text-rose-400 font-bold">PARADOX SHOWN: If two field lines crossed at P, a compass needle would have to point in TWO directions at once! This physical impossibility proves field lines NEVER intersect.</span>';
            }} else {{
                grp.classList.add('hidden');
                desc.textContent = 'Crowded lines at poles demonstrate high field strength. Field lines never intersect! Click button to explore the two-direction paradox.';
            }}
        }}

        function setSim5Dir(dir) {{
            playTone(490, 'sine', 0.06);
            const bNS = document.getElementById('btn-sim5-ns');
            const bSN = document.getElementById('btn-sim5-sn');
            const needle = document.getElementById('sim5-needle');
            const arrow = document.getElementById('sim5-flow-arrow');
            const desc = document.getElementById('sim5-desc');

            if (dir === 'north_south') {{
                bNS.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                bSN.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                needle.setAttribute('transform', 'rotate(40)');
                arrow.setAttribute('points', '260,30 245,25 245,35');
                desc.textContent = 'Fig 12.5(a): Current flows North to South over needle → North pole of compass deflects towards the EAST!';
            }} else {{
                bSN.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                bNS.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                needle.setAttribute('transform', 'rotate(-40)');
                arrow.setAttribute('points', '240,30 255,25 255,35');
                desc.textContent = 'Fig 12.5(b): Current reversed from South to North over needle → North pole of compass deflects towards the WEST!';
            }}
        }}

        function updateSim6Field() {{
            const I = parseFloat(document.getElementById('sim6-curr').value);
            document.getElementById('sim6-curr-val').textContent = `${{I.toFixed(1)}} A`;
            const circs = document.getElementById('sim6-circles');
            if (circs) {{
                const op = 0.4 + (I / 5.0) * 0.6;
                circs.setAttribute('stroke-width', (1.5 + (I / 5.0) * 1.5).toFixed(1));
                circs.setAttribute('opacity', op.toFixed(2));
            }}
            playTone(450 + I * 20, 'sine', 0.04);
        }}

        function setSim7Thumb(dir) {{
            playTone(510, 'sine', 0.08);
            const bUp = document.getElementById('btn-sim7-up');
            const bDown = document.getElementById('btn-sim7-down');
            const arrow = document.getElementById('sim7-arrow-front');
            const thumb = document.getElementById('sim7-thumb-arrow');
            const desc = document.getElementById('sim7-desc');

            if (dir === 'up') {{
                bUp.className = 'px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 text-white transition';
                bDown.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                arrow.setAttribute('points', '250,124 240,118 240,130');
                thumb.innerHTML = '<line x1="250" y1="65" x2="250" y2="35" stroke="#ef4444" stroke-width="4"/><polygon points="250,30 244,42 256,42" fill="#ef4444"/><text x="262" y="45" fill="#ef4444" font-size="9" font-weight="bold">Thumb: Current (I) Up</text>';
                desc.textContent = "Thumb points along upward current → Curled fingers wrap anticlockwise when viewed from above (Maxwell's Corkscrew Rule).";
            }} else {{
                bDown.className = 'px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 text-white transition';
                bUp.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                arrow.setAttribute('points', '250,124 260,118 260,130');
                thumb.innerHTML = '<line x1="250" y1="135" x2="250" y2="165" stroke="#ef4444" stroke-width="4"/><polygon points="250,170 244,158 256,158" fill="#ef4444"/><text x="262" y="160" fill="#ef4444" font-size="9" font-weight="bold">Thumb: Current (I) Down</text>';
                desc.textContent = 'Thumb points along downward current → Curled fingers wrap clockwise when viewed from above.';
            }}
        }}

        function updateSim9Turns() {{
            const n = parseInt(document.getElementById('sim9-turns').value);
            document.getElementById('sim9-turns-val').textContent = `${{n}} Turns`;
            const bTot = (0.2 * n).toFixed(2);
            document.getElementById('sim9-btot-val').textContent = `${{bTot}} mT (${{n}}×)`;
            playTone(420 + n * 5, 'sine', 0.04);
        }}

        let sim10CoreInserted = false;
        function toggleSim10Core() {{
            sim10CoreInserted = !sim10CoreInserted;
            playTone(sim10CoreInserted ? 580 : 440, 'sine', 0.1);
            const core = document.getElementById('sim10-core');
            const btn = document.getElementById('btn-sim10-core');
            const desc = document.getElementById('sim10-desc');

            if (sim10CoreInserted) {{
                core.classList.remove('hidden');
                btn.textContent = 'Remove Soft Iron Core';
                btn.className = 'px-3 py-1.5 rounded-lg text-xs font-bold bg-emerald-600 text-white transition';
                desc.innerHTML = '<span class="text-white font-bold animate-pulse">ELECTROMAGNET ACTIVE! Soft iron core placed inside the solenoid gains intense magnetism, multiplying field strength hundreds of times!</span>';
            }} else {{
                core.classList.add('hidden');
                btn.textContent = 'Insert Soft Iron Core';
                btn.className = 'px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                desc.textContent = 'Solenoid: Parallel straight lines inside indicate a uniform magnetic field. Click button to insert soft iron core and create an electromagnet!';
            }}
        }}

        let sim11Left = true;
        function toggleSim11Current() {{
            sim11Left = !sim11Left;
            playTone(500, 'sine', 0.08);
            const rod = document.getElementById('sim11-rod');
            const btn = document.getElementById('btn-sim11-dir');
            const desc = document.getElementById('sim11-desc');

            if (sim11Left) {{
                rod.setAttribute('transform', 'translate(-25, 0)');
                btn.textContent = 'Current: B → A (Displaces Left)';
                desc.textContent = "Current flows B to A; field is vertically upward. By Fleming's Left-Hand Rule, force pushes rod towards the LEFT!";
            }} else {{
                rod.setAttribute('transform', 'translate(25, 0)');
                btn.textContent = 'Current: A → B (Displaces Right)';
                desc.textContent = 'Current reversed (A to B); field remains upward. Force reverses and kicks rod towards the RIGHT!';
            }}
        }}

        let sim14Fault = false;
        function toggleSim14Fault() {{
            sim14Fault = !sim14Fault;
            playTone(sim14Fault ? 320 : 540, 'sine', 0.1);
            const btn = document.getElementById('btn-sim14-fault');
            const desc = document.getElementById('sim14-desc');

            if (sim14Fault) {{
                btn.textContent = 'Fault Active: Live Touches Metal Casing';
                btn.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                desc.innerHTML = '<span class="text-emerald-300 font-bold">PROTECTED: Fault current rushes through green earth wire into the ground! User touching the appliance feels NO electric shock because metal potential stays at 0 V.</span>';
            }} else {{
                btn.textContent = 'Simulate Live Wire Touching Metal Body';
                btn.className = 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition';
                desc.textContent = 'Green Earth wire connects appliance metal casing directly to deep earth plate, providing zero-potential shock protection!';
            }}
        }}

        function triggerSim15Event(type) {{
            playTone(300, 'sawtooth', 0.2);
            const out = document.getElementById('sim15-output');
            if (type === 'short') {{
                out.innerHTML = '<span class="text-rose-400 font-bold">SHORT-CIRCUIT DETECTED! Live and neutral wires made direct contact. Circuit resistance dropped to 0 Ω and current surged to > 50 A. The 5 A fuse melted instantaneously via Joule heating, interrupting the fire hazard!</span>';
            }} else {{
                out.innerHTML = '<span class="text-amber-400 font-bold">OVERLOADING OCCURRED! 2 kW oven on 220 V draws I = P/V = 2000/220 = 9.09 A. Since 9.09 A exceeds the 5 A line rating, the fuse wire overheated and safely melted to protect household wiring!</span>';
            }}
        }}

        function resetSim15Circuit() {{
            playTone(550, 'sine', 0.08);
            document.getElementById('sim15-output').textContent = 'Normal operating condition: Current is within safe parameters. Click an overload or short-circuit event above to witness fuse protection!';
        }}

        function loadExerciseCh12(num) {{
            playTone(480, 'sine', 0.08);
            const box = document.getElementById('exercise-sol-box12');
            const solutions = {{
                1: "<strong>Exercise Q1:</strong> The magnetic field near a long straight current-carrying wire consists of <strong>(d) concentric circles centred on the wire</strong> (NCERT Page 207).",
                2: "<strong>Exercise Q2:</strong> At the time of a short-circuit, the circuit resistance drops to near zero, so the electric current in the circuit <strong>(c) increases heavily</strong> (NCERT Page 207).",
                3: "<strong>Exercise Q3: State True or False:</strong><br>(a) The field at the centre of a long circular coil carrying current will be parallel straight lines: <strong>TRUE</strong>.<br>(b) A wire with green insulation is usually the live wire: <strong>FALSE</strong> (Green is the Earth wire; Live wire is red).",
                4: "<strong>Exercise Q4: Two Methods of Producing Magnetic Fields:</strong><br>1. Using a permanent magnet (e.g. bar magnet, horseshoe magnet).<br>2. Passing an electric current through a conductor (straight wire, circular loop, or solenoid).",
                5: "<strong>Exercise Q5: When Force is Largest:</strong><br>The force experienced by a current-carrying conductor in a magnetic field is largest when the direction of current is <strong>perpendicular (at an angle of 90°)</strong> to the direction of the magnetic field (NCERT Page 203).",
                6: "<strong>Exercise Q6: Electron Beam in Chamber:</strong><br>The electron beam travels from back wall towards front wall, so conventional electric current is directed from <strong>front wall towards back wall</strong>. The deflection (Force) is towards your right. By Fleming's Left-Hand Rule, the <strong>magnetic field is directed vertically DOWNWARD</strong> (NCERT Page 207).",
                7: "<strong>Exercise Q7: State Rules:</strong><br>(i) Direction of magnetic field around straight conductor: <strong>Right-Hand Thumb Rule</strong>.<br>(ii) Force experienced by current-carrying conductor in magnetic field: <strong>Fleming's Left-Hand Rule</strong>.<br>(iii) Current induced in rotating coil: <strong>Fleming's Right-Hand Rule</strong>.",
                8: "<strong>Exercise Q8: When Does Short Circuit Occur?</strong><br>A short circuit occurs when the live wire and neutral wire come into direct physical contact due to faulty/damaged insulation or an appliance malfunction. Circuit resistance drops near zero and current surges dramatically.",
                9: "<strong>Exercise Q9: Function of Earth Wire:</strong><br>The earth wire provides a very low-resistance conducting path to the ground for any leakage current. It ensures that the metallic casing of appliances (electric press, toaster, refrigerator) remains at zero potential, preventing lethal electric shocks to users."
            }};
            box.innerHTML = solutions[num] || "Solution not found.";
        }}

        window.addEventListener('DOMContentLoaded', () => {{
            showSlide(0);
            document.body.addEventListener('click', () => initAudio(), {{ once: true }});
            document.body.addEventListener('keydown', () => initAudio(), {{ once: true }});
        }});
    </script>
</body>
</html>
"""

    os.makedirs("public/animations", exist_ok=True)
    out_path = "public/animations/magnetic-effects-of-electric-current.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"Successfully generated {out_path} ({len(html_template)} bytes)")

if __name__ == '__main__':
    generate_html()
