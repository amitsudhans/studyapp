#!/usr/bin/env python3
"""
Full Generator for NCERT Class 10 Science, Chapter 9: Light - Reflection and Refraction
Master Interactive Multimedia Lab
File: public/animations/light-reflection-and-refraction.html
"""

import json
import os
import sys

# Add .agents to sys.path
sys.path.append(os.path.abspath('.agents'))
from light_optics_data import CONTENT_SLIDES, QUIZ_SLIDES

ALL_SLIDES = CONTENT_SLIDES + QUIZ_SLIDES

def get_simulator_markup(s_idx):
    """Generate high-yield interactive SVG laboratory simulators for all 21 content slides."""
    if s_idx == 0:
        # Slide 1: Rectilinear Ray vs Wave Diffraction
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 9.1: Rectilinear Rays vs Nanoscale Diffraction
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim1Mode('ray')" id="btn-sim1-ray" class="px-2.5 py-1 rounded text-xs font-bold bg-amber-500 text-slate-950 transition">Ray Optics (Macro)</button>
                    <button onclick="setSim1Mode('wave')" id="btn-sim1-wave" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Diffraction (Micro)</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <svg id="svg-sim1" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Light source -->
                    <circle cx="40" cy="100" r="14" fill="#fbbf24" filter="drop-shadow(0 0 8px #f59e0b)"/>
                    <text x="40" y="130" fill="#fcd34d" font-size="10" text-anchor="middle" font-weight="bold">Light Source</text>
                    
                    <!-- Rays mode (default) -->
                    <g id="sim1-rays-group">
                        <line x1="55" y1="90" x2="240" y2="60" stroke="#fef08a" stroke-width="2" stroke-dasharray="4,2"/>
                        <line x1="55" y1="100" x2="240" y2="100" stroke="#fef08a" stroke-width="2"/>
                        <line x1="55" y1="110" x2="240" y2="140" stroke="#fef08a" stroke-width="2" stroke-dasharray="4,2"/>
                        
                        <!-- Opaque macro obstacle -->
                        <rect x="240" y="60" width="16" height="80" rx="2" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
                        <text x="248" y="155" fill="#94a3b8" font-size="9" text-anchor="middle">Opaque Obstacle</text>
                        
                        <!-- Shadows beyond obstacle -->
                        <line x1="256" y1="60" x2="440" y2="30" stroke="#fef08a" stroke-width="2" stroke-opacity="0.8"/>
                        <line x1="256" y1="140" x2="440" y2="170" stroke="#fef08a" stroke-width="2" stroke-opacity="0.8"/>
                        
                        <!-- Screen -->
                        <line x1="440" y1="20" x2="440" y2="180" stroke="#475569" stroke-width="4"/>
                        <rect x="438" y="50" width="6" height="100" fill="#0f172a"/>
                        <text x="445" y="105" fill="#f43f5e" font-size="10" font-weight="bold">Sharp Shadow</text>
                    </g>
                    
                    <!-- Diffraction mode (hidden initially) -->
                    <g id="sim1-waves-group" class="hidden">
                        <!-- Slit barrier -->
                        <rect x="220" y="20" width="12" height="75" fill="#64748b"/>
                        <rect x="220" y="105" width="12" height="75" fill="#64748b"/>
                        <text x="226" y="100" fill="#38bdf8" font-size="8" text-anchor="middle">Micro Slit</text>
                        
                        <!-- Incoming wavefronts -->
                        <line x1="90" y1="40" x2="90" y2="160" stroke="#38bdf8" stroke-width="2" stroke-opacity="0.7"/>
                        <line x1="130" y1="40" x2="130" y2="160" stroke="#38bdf8" stroke-width="2" stroke-opacity="0.7"/>
                        <line x1="170" y1="40" x2="170" y2="160" stroke="#38bdf8" stroke-width="2" stroke-opacity="0.7"/>
                        
                        <!-- Diffracted curved wavefronts -->
                        <path d="M 235 90 A 20 20 0 0 1 235 110" fill="none" stroke="#38bdf8" stroke-width="2"/>
                        <path d="M 255 75 A 40 40 0 0 1 255 125" fill="none" stroke="#38bdf8" stroke-width="2"/>
                        <path d="M 285 55 A 70 70 0 0 1 285 145" fill="none" stroke="#38bdf8" stroke-width="2"/>
                        <path d="M 325 35 A 110 110 0 0 1 325 165" fill="none" stroke="#38bdf8" stroke-width="2"/>
                        
                        <text x="350" y="105" fill="#38bdf8" font-size="10" font-weight="bold">Wave Bending Around Edges</text>
                    </g>
                </svg>
                <div id="sim1-desc" class="text-xs text-amber-200 mt-2 text-center font-medium">
                    Rectilinear Propagation: Light travels along straight lines, casting crisp shadows behind macroscopic objects.
                </div>
            </div>
        </div>
        """
    elif s_idx == 1:
        # Slide 2: Laws of Reflection Laser Goniometer
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 9.2: Precision Laser Goniometer (∠i = ∠r)
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300 font-semibold">Incident Angle (i):</label>
                    <input type="range" id="sim2-angle" min="0" max="75" value="40" oninput="updateSim2(this.value)" class="w-28 sm:w-36 accent-cyan-400 cursor-pointer">
                    <span id="sim2-angle-val" class="text-xs font-mono font-bold text-cyan-400">40°</span>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim2" viewBox="0 0 460 210" class="w-full max-w-lg h-auto">
                    <!-- Flat Plane Mirror -->
                    <line x1="30" y1="180" x2="430" y2="180" stroke="#38bdf8" stroke-width="4"/>
                    <!-- Hatching underneath -->
                    <g stroke="#64748b" stroke-width="1.5">
                        <line x1="50" y1="180" x2="40" y2="195"/><line x1="90" y1="180" x2="80" y2="195"/>
                        <line x1="130" y1="180" x2="120" y2="195"/><line x1="170" y1="180" x2="160" y2="195"/>
                        <line x1="210" y1="180" x2="200" y2="195"/><line x1="250" y1="180" x2="240" y2="195"/>
                        <line x1="290" y1="180" x2="280" y2="195"/><line x1="330" y1="180" x2="320" y2="195"/>
                        <line x1="370" y1="180" x2="360" y2="195"/><line x1="410" y1="180" x2="400" y2="195"/>
                    </g>
                    <!-- Normal line at Point of Incidence O (230, 180) -->
                    <line x1="230" y1="20" x2="230" y2="180" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
                    <text x="235" y="35" fill="#94a3b8" font-size="10" font-weight="bold">Normal (N)</text>
                    <circle cx="230" cy="180" r="4" fill="#38bdf8"/>
                    <text x="230" y="200" fill="#38bdf8" font-size="9" text-anchor="middle" font-weight="bold">Point of Incidence (O)</text>
                    
                    <!-- Incident and Reflected Rays (Dynamic) -->
                    <line id="sim2-incident-ray" x1="100" y1="50" x2="230" y2="180" stroke="#f43f5e" stroke-width="3"/>
                    <line id="sim2-reflected-ray" x1="230" y1="180" x2="360" y2="50" stroke="#10b981" stroke-width="3"/>
                    
                    <!-- Protractor Arc -->
                    <path d="M 180 180 A 50 50 0 0 1 280 180" fill="none" stroke="#475569" stroke-width="1"/>
                </svg>
                <div class="grid grid-cols-2 gap-4 w-full max-w-sm mt-2 text-center text-xs">
                    <div class="bg-rose-950/40 border border-rose-500/30 p-2 rounded-lg text-rose-300">
                        Incident Angle: <span id="sim2-i-display" class="font-mono font-bold">∠i = 40°</span>
                    </div>
                    <div class="bg-emerald-950/40 border border-emerald-500/30 p-2 rounded-lg text-emerald-300">
                        Reflected Angle: <span id="sim2-r-display" class="font-mono font-bold">∠r = 40°</span>
                    </div>
                </div>
            </div>
        </div>
        """
    elif s_idx == 2:
        # Slide 3: Spherical Mirror Anatomy Explorer
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 9.3: Spherical Mirror Anatomy & Curvature
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim3Type('concave')" id="btn-sim3-concave" class="px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition">Concave Mirror</button>
                    <button onclick="setSim3Type('convex')" id="btn-sim3-convex" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Convex Mirror</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim3" viewBox="0 0 480 200" class="w-full max-w-lg h-auto">
                    <!-- Principal Axis -->
                    <line x1="20" y1="100" x2="460" y2="100" stroke="#475569" stroke-width="1.5"/>
                    <text x="30" y="90" fill="#64748b" font-size="9">Principal Axis (X'X)</text>
                    
                    <!-- Mirror Arc -->
                    <path id="sim3-mirror-path" d="M 380 25 A 150 150 0 0 0 380 175" fill="none" stroke="#f43f5e" stroke-width="4"/>
                    
                    <!-- Landmarks -->
                    <!-- Pole P -->
                    <circle id="sim3-pole" cx="370" cy="100" r="5" fill="#38bdf8"/>
                    <text id="sim3-pole-label" x="375" y="118" fill="#38bdf8" font-size="10" font-weight="bold">Pole (P)</text>
                    
                    <!-- Focus F -->
                    <circle id="sim3-focus" cx="245" cy="100" r="4.5" fill="#fbbf24"/>
                    <text id="sim3-focus-label" x="245" y="118" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Focus (F)</text>
                    
                    <!-- Centre of Curvature C -->
                    <circle id="sim3-centre" cx="120" cy="100" r="4.5" fill="#a855f7"/>
                    <text id="sim3-centre-label" x="120" y="118" fill="#a855f7" font-size="10" font-weight="bold" text-anchor="middle">Centre (C)</text>
                    
                    <!-- Dimension lines -->
                    <line x1="245" y1="75" x2="370" y2="75" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <text x="307" y="70" fill="#fbbf24" font-size="9" text-anchor="middle">focal length (f)</text>
                    
                    <line x1="120" y1="50" x2="370" y2="50" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <text x="245" y="45" fill="#a855f7" font-size="9" text-anchor="middle">Radius of Curvature (R = 2f)</text>
                </svg>
                <div id="sim3-info" class="text-xs text-slate-300 mt-2 text-center">
                    Concave Mirror: Reflecting surface curves <strong>inward</strong>. $C$ and $F$ lie <strong>in front</strong> of the mirror. $R = 2f$.
                </div>
            </div>
        </div>
        """
    elif s_idx == 3:
        # Slide 4: Activity 9.2 Solar Ignition Lab
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 9.4: Activity 9.2 Solar Ignition at Focus
                </span>
                <button onclick="triggerSolarIgnition()" id="btn-ignite" class="px-3 py-1 rounded-lg text-xs font-bold bg-gradient-to-r from-amber-500 to-rose-500 text-slate-950 hover:brightness-110 transition flex items-center gap-1">
                    🔥 Concentrate Solar Heat
                </button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim4" viewBox="0 0 480 200" class="w-full max-w-lg h-auto">
                    <!-- Solar rays from sun at infinity -->
                    <g stroke="#fde047" stroke-width="2">
                        <line x1="20" y1="40" x2="370" y2="40"/>
                        <line x1="20" y1="70" x2="360" y2="70"/>
                        <line x1="20" y1="100" x2="350" y2="100"/>
                        <line x1="20" y1="130" x2="360" y2="130"/>
                        <line x1="20" y1="160" x2="370" y2="160"/>
                    </g>
                    <!-- Concave Mirror -->
                    <path d="M 370 20 A 150 150 0 0 0 370 180" fill="none" stroke="#f43f5e" stroke-width="4"/>
                    
                    <!-- Converging reflected rays meeting at F (200, 100) -->
                    <g stroke="#f59e0b" stroke-width="2.5">
                        <line x1="370" y1="40" x2="200" y2="100"/>
                        <line x1="360" y1="70" x2="200" y2="100"/>
                        <line x1="360" y1="130" x2="200" y2="100"/>
                        <line x1="370" y1="160" x2="200" y2="100"/>
                    </g>
                    
                    <!-- Paper sheet at focus F -->
                    <line x1="200" y1="70" x2="200" y2="130" stroke="#e2e8f0" stroke-width="4"/>
                    <text x="200" y="60" fill="#e2e8f0" font-size="9" text-anchor="middle" font-weight="bold">Paper Sheet at F</text>
                    
                    <!-- Focal Hot Spot & Smoke Animation (Hidden initially) -->
                    <circle id="sim4-hotspot" cx="200" cy="100" r="5" fill="#facc15" filter="drop-shadow(0 0 6px #ea580c)"/>
                    <g id="sim4-flame" class="hidden">
                        <circle cx="200" cy="98" r="8" fill="#ef4444" opacity="0.8"/>
                        <circle cx="200" cy="95" r="5" fill="#f59e0b" opacity="0.9"/>
                        <circle cx="200" cy="90" r="3" fill="#ffffff"/>
                        <text x="200" y="145" fill="#f43f5e" font-size="10" font-weight="extrabold" text-anchor="middle">PAPER IGNITES! 🔥</text>
                    </g>
                </svg>
                <div class="text-xs text-amber-200 mt-2 text-center">
                    Parallel rays from the distant sun converge at Focus F, concentrating immense radiant energy into a sharp spot that ignites the paper.
                </div>
            </div>
        </div>
        """
    elif s_idx == 4:
        # Slide 5: 4 Ray Rules Interactive Selector
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 9.5: The 4 Fundamental Ray Tracing Rules
                </span>
            </div>
            <div class="flex flex-wrap gap-1.5 mb-3">
                <button onclick="setSim5Rule(1)" id="btn-rule-1" class="px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white">Rule 1: Parallel → F</button>
                <button onclick="setSim5Rule(2)" id="btn-rule-2" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Rule 2: Through F → Parallel</button>
                <button onclick="setSim5Rule(3)" id="btn-rule-3" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Rule 3: Through C → Retraced</button>
                <button onclick="setSim5Rule(4)" id="btn-rule-4" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Rule 4: Oblique at P</button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim5" viewBox="0 0 460 180" class="w-full max-w-lg h-auto">
                    <line x1="20" y1="90" x2="440" y2="90" stroke="#475569" stroke-width="1.5"/>
                    <path d="M 360 20 A 130 130 0 0 0 360 160" fill="none" stroke="#f43f5e" stroke-width="4"/>
                    <circle cx="350" cy="90" r="4" fill="#38bdf8"/><text x="355" y="105" fill="#38bdf8" font-size="9">P</text>
                    <circle cx="240" cy="90" r="4" fill="#fbbf24"/><text x="240" y="105" fill="#fbbf24" font-size="9" text-anchor="middle">F</text>
                    <circle cx="130" cy="90" r="4" fill="#a855f7"/><text x="130" y="105" fill="#a855f7" font-size="9" text-anchor="middle">C</text>
                    
                    <!-- Dynamic Rule Rays -->
                    <g id="sim5-ray-group">
                        <!-- Rule 1 default: parallel -> F -->
                        <line x1="60" y1="40" x2="355" y2="40" stroke="#38bdf8" stroke-width="2.5"/>
                        <line x1="355" y1="40" x2="160" y2="125" stroke="#f43f5e" stroke-width="2.5"/>
                    </g>
                </svg>
                <div id="sim5-text" class="text-xs text-slate-300 mt-2 text-center font-medium">
                    Rule 1: A ray incident parallel to the principal axis passes through the principal focus F after reflection (Fig 9.3a).
                </div>
            </div>
        </div>
        """
    elif s_idx == 5:
        # Slide 6: Concave Mirror Positions 1 to 3
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 9.6: Concave Mirror Real Images (Cases 1, 2, 3)
                </span>
            </div>
            <div class="flex flex-wrap gap-2 mb-3">
                <button onclick="setSim6Case(1)" id="btn-case-1" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Case 1: At Infinity</button>
                <button onclick="setSim6Case(2)" id="btn-case-2" class="px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white">Case 2: Beyond C</button>
                <button onclick="setSim6Case(3)" id="btn-case-3" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Case 3: At C (Same Size!)</button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim6" viewBox="0 0 460 200" class="w-full max-w-lg h-auto">
                    <line x1="20" y1="100" x2="440" y2="100" stroke="#475569" stroke-width="1.5"/>
                    <path d="M 370 20 A 140 140 0 0 0 370 180" fill="none" stroke="#f43f5e" stroke-width="4"/>
                    <circle cx="360" cy="100" r="4" fill="#38bdf8"/><text x="365" y="115" fill="#38bdf8" font-size="9">P</text>
                    <circle cx="260" cy="100" r="4" fill="#fbbf24"/><text x="260" y="115" fill="#fbbf24" font-size="9" text-anchor="middle">F</text>
                    <circle cx="160" cy="100" r="4" fill="#a855f7"/><text x="160" y="115" fill="#a855f7" font-size="9" text-anchor="middle">C</text>
                    
                    <!-- Dynamic Object & Image for Case 2 (Beyond C) -->
                    <g id="sim6-art">
                        <!-- Object AB (x=90, height=45) -->
                        <line x1="90" y1="100" x2="90" y2="55" stroke="#38bdf8" stroke-width="3"/>
                        <polygon points="90,50 86,58 94,58" fill="#38bdf8"/>
                        <text x="90" y="45" fill="#38bdf8" font-size="9" text-anchor="middle" font-weight="bold">Object (A)</text>
                        
                        <!-- Ray 1: Parallel -> F -->
                        <line x1="90" y1="55" x2="365" y2="55" stroke="#facc15" stroke-width="2"/>
                        <line x1="365" y1="55" x2="190" y2="140" stroke="#facc15" stroke-width="2"/>
                        
                        <!-- Ray 2: Through C -->
                        <line x1="90" y1="55" x2="368" y2="140" stroke="#ec4899" stroke-width="2"/>
                        
                        <!-- Image A'B' between F and C (x=205, height=25, inverted) -->
                        <line x1="205" y1="100" x2="205" y2="125" stroke="#10b981" stroke-width="3"/>
                        <polygon points="205,130 201,122 209,122" fill="#10b981"/>
                        <text x="205" y="145" fill="#10b981" font-size="9" text-anchor="middle" font-weight="bold">Image (A')</text>
                    </g>
                </svg>
                <div id="sim6-status" class="text-xs text-emerald-300 mt-2 text-center font-semibold">
                    Case 2: Object Beyond C → Image formed between F and C. Nature: Real, Inverted & Diminished.
                </div>
            </div>
        </div>
        """
    elif s_idx == 6:
        # Slide 7: Concave Mirror Positions 4 to 6 & Uses
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 9.7: Magnified Images & Practical Optical Tools
                </span>
            </div>
            <div class="flex flex-wrap gap-2 mb-3">
                <button onclick="setSim7Case(4)" id="btn-case-4" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Between C & F</button>
                <button onclick="setSim7Case(5)" id="btn-case-5" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">At F (Headlight Beam)</button>
                <button onclick="setSim7Case(6)" id="btn-case-6" class="px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white">Between P & F (Dentist/Shaving)</button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim7" viewBox="0 0 460 200" class="w-full max-w-lg h-auto">
                    <line x1="20" y1="100" x2="440" y2="100" stroke="#475569" stroke-width="1.5"/>
                    <path d="M 330 20 A 140 140 0 0 0 330 180" fill="none" stroke="#f43f5e" stroke-width="4"/>
                    <circle cx="320" cy="100" r="4" fill="#38bdf8"/><text x="325" y="115" fill="#38bdf8" font-size="9">P</text>
                    <circle cx="220" cy="100" r="4" fill="#fbbf24"/><text x="220" y="115" fill="#fbbf24" font-size="9" text-anchor="middle">F</text>
                    <circle cx="120" cy="100" r="4" fill="#a855f7"/><text x="120" y="115" fill="#a855f7" font-size="9" text-anchor="middle">C</text>
                    
                    <!-- Case 6 (Inside F): Virtual Erect Magnified Image behind mirror -->
                    <g id="sim7-art">
                        <!-- Object between P and F (x=270, h=30) -->
                        <line x1="270" y1="100" x2="270" y2="70" stroke="#38bdf8" stroke-width="3"/>
                        <polygon points="270,65 266,73 274,73" fill="#38bdf8"/>
                        <text x="270" y="60" fill="#38bdf8" font-size="9" text-anchor="middle">Tooth</text>
                        
                        <!-- Rays diverging in front -->
                        <line x1="270" y1="70" x2="325" y2="70" stroke="#facc15" stroke-width="2"/>
                        <line x1="325" y1="70" x2="160" y2="145" stroke="#facc15" stroke-width="2"/>
                        
                        <!-- Backward dotted rays meeting behind mirror -->
                        <line x1="325" y1="70" x2="410" y2="35" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <line x1="325" y1="100" x2="410" y2="35" stroke="#ec4899" stroke-width="1.5" stroke-dasharray="3,3"/>
                        
                        <!-- Virtual Image behind mirror (x=410, h=65, erect!) -->
                        <line x1="410" y1="100" x2="410" y2="35" stroke="#10b981" stroke-width="3.5" stroke-dasharray="4,2"/>
                        <polygon points="410,30 405,40 415,40" fill="#10b981"/>
                        <text x="410" y="25" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Virtual Magnified Image</text>
                    </g>
                </svg>
                <div id="sim7-status" class="text-xs text-rose-300 mt-2 text-center font-semibold">
                    Case 6: Object inside F → Reflected rays diverge in front; backward extensions form an enlarged, virtual, and erect image behind the mirror.
                </div>
            </div>
        </div>
        """
    elif s_idx == 7:
        # Slide 8: Convex Mirror Automotive Lab
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 9.8: Convex Mirror Rear-View & Wide Field
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300 font-semibold">Vehicle Distance:</label>
                    <input type="range" id="sim8-dist" min="50" max="250" value="150" oninput="updateSim8(this.value)" class="w-28 sm:w-36 accent-cyan-400 cursor-pointer">
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim8" viewBox="0 0 460 200" class="w-full max-w-lg h-auto">
                    <line x1="20" y1="100" x2="440" y2="100" stroke="#475569" stroke-width="1.5"/>
                    <!-- Convex mirror (bulging towards left) -->
                    <path d="M 230 25 A 140 140 0 0 1 230 175" fill="none" stroke="#38bdf8" stroke-width="4"/>
                    <!-- Hatching behind (on right) -->
                    <g stroke="#64748b" stroke-width="1">
                        <line x1="230" y1="40" x2="242" y2="35"/><line x1="235" y1="70" x2="247" y2="65"/>
                        <line x1="238" y1="100" x2="250" y2="95"/><line x1="235" y1="130" x2="247" y2="125"/>
                        <line x1="230" y1="160" x2="242" y2="155"/>
                    </g>
                    <!-- Behind mirror points -->
                    <circle cx="310" cy="100" r="4" fill="#fbbf24"/><text x="310" y="115" fill="#fbbf24" font-size="9" text-anchor="middle">F</text>
                    <circle cx="390" cy="100" r="4" fill="#a855f7"/><text x="390" y="115" fill="#a855f7" font-size="9" text-anchor="middle">C</text>
                    
                    <!-- Dynamic Vehicle Object and Virtual Image -->
                    <g id="sim8-vehicle">
                        <rect id="sim8-car" x="70" y="55" width="25" height="45" fill="#f43f5e" rx="3"/>
                        <text id="sim8-car-label" x="82" y="48" fill="#f43f5e" font-size="9" text-anchor="middle" font-weight="bold">Bus</text>
                    </g>
                    
                    <!-- Virtual Image between P and F -->
                    <g id="sim8-image">
                        <rect id="sim8-img-rect" x="260" y="80" width="10" height="20" fill="#10b981" rx="2" stroke="#34d399" stroke-dasharray="2,2"/>
                        <text x="265" y="75" fill="#10b981" font-size="8" text-anchor="middle">Erect Diminished</text>
                    </g>
                    
                    <!-- Wide field of view cone -->
                    <polygon points="238,100 20,30 20,170" fill="#38bdf8" opacity="0.08"/>
                    <text x="80" y="165" fill="#38bdf8" font-size="9">Expansive Field of View</text>
                </svg>
                <div class="text-xs text-slate-300 mt-2 text-center">
                    Convex mirrors form strictly <strong>virtual, erect, and diminished</strong> images between P and F, allowing drivers to view wide highway spans.
                </div>
            </div>
        </div>
        """
    elif s_idx == 8:
        # Slide 9: Cartesian Sign Convention Coordinate Plane
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 9.9: New Cartesian Coordinate Sign Plane
                </span>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg viewBox="0 0 460 200" class="w-full max-w-lg h-auto">
                    <!-- Axes -->
                    <line x1="20" y1="100" x2="440" y2="100" stroke="#94a3b8" stroke-width="2"/>
                    <line x1="280" y1="20" x2="280" y2="180" stroke="#94a3b8" stroke-width="2"/>
                    <text x="445" y="103" fill="#94a3b8" font-size="10">+x</text>
                    <text x="15" y="103" fill="#94a3b8" font-size="10">-x</text>
                    <text x="283" y="18" fill="#94a3b8" font-size="10">+y</text>
                    <text x="283" y="195" fill="#94a3b8" font-size="10">-y</text>
                    
                    <!-- Mirror at Origin P(280, 100) -->
                    <path d="M 280 40 A 100 100 0 0 0 280 160" fill="none" stroke="#f43f5e" stroke-width="4"/>
                    <circle cx="280" cy="100" r="5" fill="#38bdf8"/>
                    <text x="290" y="115" fill="#38bdf8" font-size="10" font-weight="bold">Pole P (0, 0)</text>
                    
                    <!-- Direction of incident light -->
                    <line x1="60" y1="35" x2="220" y2="35" stroke="#facc15" stroke-width="2"/>
                    <polygon points="225,35 215,30 215,40" fill="#facc15"/>
                    <text x="140" y="28" fill="#facc15" font-size="9" text-anchor="middle">Direction of Incident Light →</text>
                    
                    <!-- Sign regions -->
                    <rect x="70" y="125" width="150" height="25" rx="4" fill="#ef4444" opacity="0.15" stroke="#ef4444" stroke-width="1"/>
                    <text x="145" y="141" fill="#fca5a5" font-size="9" text-anchor="middle" font-weight="bold">Distances to Left: NEGATIVE (-)</text>
                    
                    <rect x="295" y="125" width="145" height="25" rx="4" fill="#10b981" opacity="0.15" stroke="#10b981" stroke-width="1"/>
                    <text x="367" y="141" fill="#86efac" font-size="9" text-anchor="middle" font-weight="bold">Distances to Right: POSITIVE (+)</text>
                </svg>
                <div class="text-xs text-slate-300 mt-2 text-center">
                    Object distance $u$ is universally negative. Concave focal length $f < 0$; Convex focal length $f > 0$. Upward heights $+h$; downward heights $-h'$.
                </div>
            </div>
        </div>
        """
    elif s_idx == 9:
        # Slide 10: Interactive Mirror Formula & Magnification Calculator
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-3 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 9.10: Mirror Formula Solver (1/v + 1/u = 1/f)
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300">Object Dist (u):</label>
                    <input type="range" id="sim10-u" min="10" max="60" value="25" oninput="calcMirrorFormula()" class="w-28 accent-amber-400 cursor-pointer">
                    <span id="sim10-u-val" class="text-xs font-mono font-bold text-amber-400">-25 cm</span>
                </div>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-3 text-center text-xs">
                <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                    <div class="text-slate-400">Focal Length (f)</div>
                    <div class="text-rose-400 font-mono font-bold text-sm">-15.0 cm (Concave)</div>
                </div>
                <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                    <div class="text-slate-400">Calculated Image Dist (v)</div>
                    <div id="sim10-v-res" class="text-emerald-400 font-mono font-bold text-sm">-37.5 cm</div>
                </div>
                <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                    <div class="text-slate-400">Magnification (m = -v/u)</div>
                    <div id="sim10-m-res" class="text-cyan-400 font-mono font-bold text-sm">-1.50 (Real, Inverted)</div>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 text-center text-xs text-slate-300">
                Formula applied: <span class="text-rose-400 font-mono">1/v = 1/f - 1/u</span>. Linear Magnification: <span class="text-amber-400 font-mono">m = -v/u</span>.
            </div>
        </div>
        """
    elif s_idx == 10:
        # Slide 11: Apparent Depth & Magic Coin Simulator
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 9.11: Apparent Depth & Reappearing Coin (Activity 9.8)
                </span>
                <button onclick="toggleWaterCoin()" id="btn-water-coin" class="px-3 py-1 rounded-lg text-xs font-bold bg-cyan-500 text-slate-950 hover:bg-cyan-400 transition flex items-center gap-1">
                    💧 Pour Water into Bowl
                </button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim11" viewBox="0 0 460 200" class="w-full max-w-lg h-auto">
                    <!-- Observer's Eye -->
                    <circle cx="60" cy="40" r="12" fill="none" stroke="#38bdf8" stroke-width="2"/>
                    <circle cx="60" cy="40" r="5" fill="#38bdf8"/>
                    <text x="60" y="20" fill="#38bdf8" font-size="9" text-anchor="middle" font-weight="bold">Observer</text>
                    
                    <!-- Bowl -->
                    <path d="M 120 70 L 150 170 L 350 170 L 380 70" fill="none" stroke="#94a3b8" stroke-width="3"/>
                    
                    <!-- Water layer (animated height) -->
                    <rect id="sim11-water" x="135" y="100" width="230" height="70" fill="#0284c7" opacity="0.1" stroke="#38bdf8" stroke-dasharray="2,2"/>
                    
                    <!-- Real Coin at bottom (250, 165) -->
                    <ellipse cx="250" cy="165" rx="14" ry="4" fill="#eab308" stroke="#ca8a04"/>
                    <text x="250" y="185" fill="#eab308" font-size="9" text-anchor="middle">Real Coin (Blocked by Rim)</text>
                    
                    <!-- Apparent Coin (hidden initially) -->
                    <g id="sim11-apparent-coin" class="hidden">
                        <ellipse cx="250" cy="130" rx="14" ry="4" fill="#fde047" stroke="#ca8a04" opacity="0.9" stroke-dasharray="2,2"/>
                        <text x="250" y="122" fill="#fde047" font-size="8" text-anchor="middle">Apparent Raised Coin</text>
                        <!-- Refracted ray to eye -->
                        <line x1="250" y1="165" x2="210" y2="100" stroke="#facc15" stroke-width="2"/>
                        <line x1="210" y1="100" x2="72" y2="42" stroke="#facc15" stroke-width="2"/>
                    </g>
                    <!-- Straight blocked line of sight (Dry bowl) -->
                    <line id="sim11-dry-sight" x1="60" y1="40" x2="120" y2="70" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3"/>
                </svg>
                <div id="sim11-status" class="text-xs text-slate-300 mt-2 text-center">
                    Dry Bowl: The bowl rim blocks the straight line of sight to the coin. Pour water to bend light and reveal the coin!
                </div>
            </div>
        </div>
        """
    elif s_idx == 11:
        # Slide 12: Glass Slab & Lateral Shift Lab
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 9.12: Glass Slab Refraction & Lateral Shift
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300">Angle (i):</label>
                    <input type="range" id="sim12-angle" min="10" max="65" value="45" oninput="updateSim12(this.value)" class="w-24 sm:w-32 accent-cyan-400 cursor-pointer">
                    <span id="sim12-angle-val" class="text-xs font-mono font-bold text-cyan-400">45°</span>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim12" viewBox="0 0 460 210" class="w-full max-w-lg h-auto">
                    <!-- Glass Slab ABCD -->
                    <rect x="100" y="70" width="260" height="70" fill="#0284c7" opacity="0.2" stroke="#38bdf8" stroke-width="2"/>
                    <text x="110" y="85" fill="#38bdf8" font-size="9" font-weight="bold">Glass Slab (n = 1.52)</text>
                    <text x="35" y="85" fill="#94a3b8" font-size="9">Air</text>
                    <text x="35" y="160" fill="#94a3b8" font-size="9">Air</text>
                    
                    <!-- Normal lines at AB and CD -->
                    <line x1="180" y1="40" x2="180" y2="100" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <line x1="225" y1="110" x2="225" y2="170" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3"/>
                    
                    <!-- Incident ray, refracted ray, emergent ray -->
                    <line id="sim12-inc" x1="110" y1="20" x2="180" y2="70" stroke="#f43f5e" stroke-width="2.5"/>
                    <line id="sim12-refr" x1="180" y1="70" x2="225" y2="140" stroke="#facc15" stroke-width="2.5"/>
                    <line id="sim12-emerg" x1="225" y1="140" x2="295" y2="190" stroke="#10b981" stroke-width="2.5"/>
                    
                    <!-- Original unbent incident path produced -->
                    <line id="sim12-prod" x1="180" y1="70" x2="330" y2="177" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="4,3"/>
                    
                    <!-- Lateral Shift bracket -->
                    <line x1="260" y1="165" x2="277" y2="140" stroke="#ec4899" stroke-width="2"/>
                    <text x="285" y="155" fill="#ec4899" font-size="9" font-weight="bold">Lateral Shift (d)</text>
                </svg>
                <div class="text-xs text-slate-300 mt-2 text-center">
                    Equal and opposite bending at parallel faces ensures the emergent ray is strictly <strong>parallel</strong> to the incident ray, offset by lateral displacement $d$.
                </div>
            </div>
        </div>
        """
    elif s_idx == 12:
        # Slide 13: Snell's Law Calculator
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 9.13: Snell's Law Refractometer (sin i / sin r = n)
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim13Medium('water')" id="btn-med-water" class="px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300">Water (1.33)</button>
                    <button onclick="setSim13Medium('glass')" id="btn-med-glass" class="px-2 py-1 rounded text-xs font-bold bg-rose-600 text-white">Crown Glass (1.52)</button>
                    <button onclick="setSim13Medium('diamond')" id="btn-med-diamond" class="px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300">Diamond (2.42)</button>
                </div>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 mb-3 text-center text-xs">
                <div class="bg-slate-950 p-2 rounded-xl border border-slate-800">
                    <div class="text-slate-400">Angle of Incidence (i)</div>
                    <div class="text-amber-400 font-mono font-bold text-sm">45.0°</div>
                </div>
                <div class="bg-slate-950 p-2 rounded-xl border border-slate-800">
                    <div class="text-slate-400">Refractive Index (n)</div>
                    <div id="sim13-n-display" class="text-rose-400 font-mono font-bold text-sm">1.52</div>
                </div>
                <div class="bg-slate-950 p-2 rounded-xl border border-slate-800">
                    <div class="text-slate-400">sin(i) / n = sin(r)</div>
                    <div id="sim13-sin-display" class="text-cyan-400 font-mono font-bold text-sm">0.707 / 1.52 = 0.465</div>
                </div>
                <div class="bg-slate-950 p-2 rounded-xl border border-slate-800">
                    <div class="text-slate-400">Angle of Refraction (r)</div>
                    <div id="sim13-r-display" class="text-emerald-400 font-mono font-bold text-sm">27.7°</div>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 text-center text-xs text-slate-300">
                Notice: Higher optical density causes greater bending towards the normal, sharply reducing the angle of refraction $r$!
            </div>
        </div>
        """
    elif s_idx == 13:
        # Slide 14: Speed of Light & The Kerosene Paradox
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 9.14: Cosmic Light Speeds & The Kerosene Paradox
                </span>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 mb-3 text-center text-xs">
                <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                    <div class="text-slate-400 font-bold">Vacuum / Air</div>
                    <div class="text-amber-400 font-mono font-bold text-sm mt-1">300,000 km/s</div>
                    <div class="text-[10px] text-slate-500">n = 1.0003 (Fastest)</div>
                </div>
                <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                    <div class="text-slate-400 font-bold">Water</div>
                    <div class="text-sky-400 font-mono font-bold text-sm mt-1">225,564 km/s</div>
                    <div class="text-[10px] text-slate-500">n = 1.33</div>
                </div>
                <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                    <div class="text-slate-400 font-bold">Crown Glass</div>
                    <div class="text-emerald-400 font-mono font-bold text-sm mt-1">197,368 km/s</div>
                    <div class="text-[10px] text-slate-500">n = 1.52</div>
                </div>
                <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                    <div class="text-slate-400 font-bold">Diamond</div>
                    <div class="text-rose-400 font-mono font-bold text-sm mt-1">123,967 km/s</div>
                    <div class="text-[10px] text-slate-500">n = 2.42 (Slowest)</div>
                </div>
            </div>
            <div class="bg-amber-950/30 border border-amber-500/30 rounded-xl p-3 text-xs text-slate-200">
                <span class="font-bold text-amber-400">The Kerosene Paradox (NCERT Page 149):</span> Kerosene ($n = 1.44$) is <strong>optically denser</strong> than water ($n = 1.33$), bending light more strongly. Yet kerosene floats on water because its <em>physical mass density</em> is lower!
            </div>
        </div>
        """
    elif s_idx == 14:
        # Slide 15: Spherical Lens Dual Foci & Undeviated Ray O
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 9.15: Dual Foci & Undeviated Optical Centre (O)
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim15Lens('convex')" id="btn-sim15-cvx" class="px-2.5 py-1 rounded text-xs font-bold bg-cyan-500 text-slate-950">Convex (Converging)</button>
                    <button onclick="setSim15Lens('concave')" id="btn-sim15-ccv" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">Concave (Diverging)</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim15" viewBox="0 0 460 200" class="w-full max-w-lg h-auto">
                    <line x1="20" y1="100" x2="440" y2="100" stroke="#475569" stroke-width="1.5"/>
                    <!-- Lens Body (Convex default) -->
                    <path id="sim15-lens-shape" d="M 230 20 Q 250 100 230 180 Q 210 100 230 20 Z" fill="#0284c7" fill-opacity="0.25" stroke="#38bdf8" stroke-width="2.5"/>
                    
                    <!-- Optical Centre O -->
                    <circle cx="230" cy="100" r="4.5" fill="#f43f5e"/>
                    <text x="230" y="118" fill="#f43f5e" font-size="9" text-anchor="middle" font-weight="bold">O</text>
                    
                    <!-- Foci F1 and F2 -->
                    <circle cx="150" cy="100" r="4" fill="#fbbf24"/><text x="150" y="118" fill="#fbbf24" font-size="9" text-anchor="middle">F1</text>
                    <circle cx="310" cy="100" r="4" fill="#fbbf24"/><text x="310" y="118" fill="#fbbf24" font-size="9" text-anchor="middle">F2</text>
                    <circle cx="70" cy="100" r="4" fill="#a855f7"/><text x="70" y="118" fill="#a855f7" font-size="9" text-anchor="middle">2F1</text>
                    <circle cx="390" cy="100" r="4" fill="#a855f7"/><text x="390" y="118" fill="#a855f7" font-size="9" text-anchor="middle">2F2</text>
                    
                    <!-- Undeviated central ray -->
                    <line x1="60" y1="30" x2="400" y2="170" stroke="#ec4899" stroke-width="2"/>
                    <text x="360" y="185" fill="#ec4899" font-size="8">Undeviated Ray through O</text>
                </svg>
                <div class="text-xs text-slate-300 mt-2 text-center">
                    Every lens has dual foci ($F_1$ and $F_2$). A light ray traversing the <strong>optical centre ($O$)</strong> emerges without experiencing any deviation!
                </div>
            </div>
        </div>
        """
    elif s_idx == 15:
        # Slide 16: Convex Lens All 6 Image Positions Studio
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 9.16: Convex Lens All 6 Image Positions (Activity 9.12)
                </span>
            </div>
            <div class="flex flex-wrap gap-1.5 mb-3">
                <button onclick="setSim16Case(1)" id="btn-lcase-1" class="px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">1. At Infinity</button>
                <button onclick="setSim16Case(2)" id="btn-lcase-2" class="px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">2. Beyond 2F1</button>
                <button onclick="setSim16Case(3)" id="btn-lcase-3" class="px-2 py-1 rounded text-xs font-bold bg-rose-600 text-white">3. At 2F1 (Same Size!)</button>
                <button onclick="setSim16Case(4)" id="btn-lcase-4" class="px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">4. Between F1 & 2F1</button>
                <button onclick="setSim16Case(5)" id="btn-lcase-5" class="px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">5. At F1</button>
                <button onclick="setSim16Case(6)" id="btn-lcase-6" class="px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700">6. Inside F1 (Magnifier)</button>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim16" viewBox="0 0 460 200" class="w-full max-w-lg h-auto">
                    <line x1="20" y1="100" x2="440" y2="100" stroke="#475569" stroke-width="1.5"/>
                    <path d="M 230 20 Q 248 100 230 180 Q 212 100 230 20 Z" fill="#0284c7" fill-opacity="0.25" stroke="#38bdf8" stroke-width="2.5"/>
                    <circle cx="230" cy="100" r="4" fill="#f43f5e"/><text x="230" y="115" fill="#f43f5e" font-size="8" text-anchor="middle">O</text>
                    <circle cx="150" cy="100" r="3.5" fill="#fbbf24"/><text x="150" y="115" fill="#fbbf24" font-size="8" text-anchor="middle">F1</text>
                    <circle cx="310" cy="100" r="3.5" fill="#fbbf24"/><text x="310" y="115" fill="#fbbf24" font-size="8" text-anchor="middle">F2</text>
                    <circle cx="70" cy="100" r="3.5" fill="#a855f7"/><text x="70" y="115" fill="#a855f7" font-size="8" text-anchor="middle">2F1</text>
                    <circle cx="390" cy="100" r="3.5" fill="#a855f7"/><text x="390" y="115" fill="#a855f7" font-size="8" text-anchor="middle">2F2</text>
                    
                    <!-- Dynamic Case 3 default (At 2F1) -->
                    <g id="sim16-art">
                        <!-- Object at 2F1 (70, 100 to 70, 50) -->
                        <line x1="70" y1="100" x2="70" y2="50" stroke="#38bdf8" stroke-width="3"/>
                        <polygon points="70,45 66,54 74,54" fill="#38bdf8"/>
                        <text x="70" y="40" fill="#38bdf8" font-size="8" text-anchor="middle">Object at 2F1</text>
                        
                        <!-- Ray parallel -> F2 -->
                        <line x1="70" y1="50" x2="230" y2="50" stroke="#facc15" stroke-width="2"/>
                        <line x1="230" y1="50" x2="390" y2="150" stroke="#facc15" stroke-width="2"/>
                        
                        <!-- Ray through O -->
                        <line x1="70" y1="50" x2="390" y2="150" stroke="#ec4899" stroke-width="2"/>
                        
                        <!-- Inverted Image at 2F2 (390, 100 to 390, 150) -->
                        <line x1="390" y1="100" x2="390" y2="150" stroke="#10b981" stroke-width="3"/>
                        <polygon points="390,155 386,146 394,146" fill="#10b981"/>
                        <text x="390" y="170" fill="#10b981" font-size="8" text-anchor="middle">Image at 2F2 (Same Size)</text>
                    </g>
                </svg>
                <div id="sim16-status" class="text-xs text-emerald-300 mt-2 text-center font-semibold">
                    Position 3: Object at $2F_1$ → Image formed at $2F_2$. Nature: Real, Inverted & Same Size ($m = -1$).
                </div>
            </div>
        </div>
        """
    elif s_idx == 16:
        # Slide 17: Concave Lens Divergence Lab
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 9.17: Concave Lens Virtual Shrunken Image (Table 9.5)
                </span>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg viewBox="0 0 460 200" class="w-full max-w-lg h-auto">
                    <line x1="20" y1="100" x2="440" y2="100" stroke="#475569" stroke-width="1.5"/>
                    <!-- Concave lens shape -->
                    <path d="M 230 20 Q 215 100 230 180 L 236 180 Q 221 100 236 20 Z" fill="#0284c7" fill-opacity="0.25" stroke="#38bdf8" stroke-width="2.5"/>
                    <circle cx="233" cy="100" r="4" fill="#f43f5e"/><text x="233" y="115" fill="#f43f5e" font-size="8" text-anchor="middle">O</text>
                    <circle cx="150" cy="100" r="3.5" fill="#fbbf24"/><text x="150" y="115" fill="#fbbf24" font-size="8" text-anchor="middle">F1</text>
                    <circle cx="310" cy="100" r="3.5" fill="#fbbf24"/><text x="310" y="115" fill="#fbbf24" font-size="8" text-anchor="middle">F2</text>
                    
                    <!-- Object AB (80, 100 to 80, 40) -->
                    <line x1="80" y1="100" x2="80" y2="40" stroke="#38bdf8" stroke-width="3"/>
                    <polygon points="80,35 76,43 84,43" fill="#38bdf8"/>
                    
                    <!-- Diverging Ray 1 -->
                    <line x1="80" y1="40" x2="230" y2="40" stroke="#facc15" stroke-width="2"/>
                    <line x1="230" y1="40" x2="350" y2="10" stroke="#facc15" stroke-width="2"/>
                    <line x1="230" y1="40" x2="150" y2="100" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,3"/>
                    
                    <!-- Undeviated Ray 2 through O -->
                    <line x1="80" y1="40" x2="350" y2="148" stroke="#ec4899" stroke-width="2"/>
                    
                    <!-- Virtual Image between F1 and O (175, 100 to 175, 78) -->
                    <line x1="175" y1="100" x2="175" y2="78" stroke="#10b981" stroke-width="2.5"/>
                    <polygon points="175,74 171,82 179,82" fill="#10b981"/>
                    <text x="175" y="70" fill="#10b981" font-size="8" text-anchor="middle" font-weight="bold">Virtual Diminished Image</text>
                </svg>
                <div class="text-xs text-slate-300 mt-2 text-center">
                    A concave lens <strong>always</strong> forms a virtual, erect, and diminished image positioned between the optical centre $O$ and focus $F_1$.
                </div>
            </div>
        </div>
        """
    elif s_idx == 17:
        # Slide 18: Lens Formula & Magnification Solver
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-3 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 9.18: Lens Formula Calculator (1/v - 1/u = 1/f)
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300">Object Dist (u):</label>
                    <input type="range" id="sim18-u" min="12" max="50" value="15" oninput="calcLensFormula()" class="w-28 accent-rose-400 cursor-pointer">
                    <span id="sim18-u-val" class="text-xs font-mono font-bold text-rose-400">-15 cm</span>
                </div>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-3 text-center text-xs">
                <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                    <div class="text-slate-400">Focal Length (f)</div>
                    <div class="text-cyan-400 font-mono font-bold text-sm">+10.0 cm (Convex)</div>
                </div>
                <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                    <div class="text-slate-400">Calculated Image Dist (v)</div>
                    <div id="sim18-v-res" class="text-emerald-400 font-mono font-bold text-sm">+30.0 cm</div>
                </div>
                <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800">
                    <div class="text-slate-400">Magnification (m = +v/u)</div>
                    <div id="sim18-m-res" class="text-amber-400 font-mono font-bold text-sm">-2.00 (Real, 2x Enlarged)</div>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 text-center text-xs text-slate-300">
                Notice: In lenses, linear magnification is <span class="text-rose-400 font-mono">m = +v/u</span> (no negative sign!), while the lens formula features <span class="text-cyan-400 font-mono">1/v - 1/u = 1/f</span>.
            </div>
        </div>
        """
    elif s_idx == 18:
        # Slide 19: Lens Power & Optician Trial Frame Dial
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-3 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 9.19: Lens Power (P = 1/f) & Optician Frame Adder
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300">Focal Length f (m):</label>
                    <input type="range" id="sim19-f" min="20" max="200" value="50" oninput="updateSim19Power(this.value)" class="w-28 accent-amber-400 cursor-pointer">
                    <span id="sim19-f-val" class="text-xs font-mono font-bold text-amber-400">+0.50 m</span>
                </div>
            </div>
            <div class="grid grid-cols-2 gap-3 mb-3 text-center text-xs">
                <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
                    <div class="text-slate-400">Calculated Power (P = 1/f)</div>
                    <div id="sim19-power-res" class="text-emerald-400 font-mono font-bold text-base mt-1">+2.00 D</div>
                    <div class="text-[10px] text-slate-500">Converging Convex Lens</div>
                </div>
                <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
                    <div class="text-slate-400">Combination: P1 (+2.0D) + P2 (+0.25D)</div>
                    <div class="text-cyan-400 font-mono font-bold text-base mt-1">+2.25 D</div>
                    <div class="text-[10px] text-slate-500">Algebraic Addition for Eye Testing</div>
                </div>
            </div>
            <div class="text-xs text-slate-300 text-center">
                The SI unit of optical power is the <strong>dioptre (D)</strong>. Short focal length bends light through sharper angles, yielding greater dioptric power!
            </div>
        </div>
        """
    elif s_idx == 19:
        # Slide 20: Summary Master Comparison Matrix
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5 mb-3">
                <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                Interactive Lab 9.20: Master Optics Formula Matrix
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div class="bg-slate-950 p-3 rounded-xl border border-rose-500/30">
                    <div class="font-bold text-rose-400 mb-1">Spherical Mirrors (Reflection)</div>
                    <ul class="space-y-1 text-slate-300">
                        <li>• Formula: <span class="font-mono text-rose-300">1/v + 1/u = 1/f</span></li>
                        <li>• Magnification: <span class="font-mono text-rose-300">m = -v/u = h'/h</span></li>
                        <li>• Concave: <span class="text-rose-400 font-semibold">f < 0</span> | Convex: <span class="text-emerald-400 font-semibold">f > 0</span></li>
                    </ul>
                </div>
                <div class="bg-slate-950 p-3 rounded-xl border border-cyan-500/30">
                    <div class="font-bold text-cyan-400 mb-1">Spherical Lenses (Refraction)</div>
                    <ul class="space-y-1 text-slate-300">
                        <li>• Formula: <span class="font-mono text-cyan-300">1/v - 1/u = 1/f</span></li>
                        <li>• Magnification: <span class="font-mono text-cyan-300">m = +v/u = h'/h</span></li>
                        <li>• Concave: <span class="text-rose-400 font-semibold">f < 0, P < 0</span> | Convex: <span class="text-emerald-400 font-semibold">f > 0, P > 0</span></li>
                    </ul>
                </div>
            </div>
        </div>
        """
    elif s_idx == 20:
        # Slide 21: Full Exercises Hub Q1-Q17
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 9.21: Complete NCERT Solutions Hub (Q1 to Q17)
                </span>
                <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">
                    17 Exercises Solved
                </span>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                <div class="bg-slate-950 p-2 rounded-lg border border-slate-800">
                    <div class="text-slate-400">Q4: f = -15 cm</div>
                    <div class="text-rose-400 font-bold mt-0.5">Both Concave</div>
                </div>
                <div class="bg-slate-950 p-2 rounded-lg border border-slate-800">
                    <div class="text-slate-400">Q10: Convex Lens</div>
                    <div class="text-emerald-400 font-bold mt-0.5">v = +16.7 cm</div>
                </div>
                <div class="bg-slate-950 p-2 rounded-lg border border-slate-800">
                    <div class="text-slate-400">Q15: Concave Mirror</div>
                    <div class="text-cyan-400 font-bold mt-0.5">v = -54 cm</div>
                </div>
                <div class="bg-slate-950 p-2 rounded-lg border border-slate-800">
                    <div class="text-slate-400">Q16: P = -2.0 D</div>
                    <div class="text-amber-400 font-bold mt-0.5">f = -0.5 m (Concave)</div>
                </div>
            </div>
        </div>
        """
    return ""


def generate_html():
    print("Generating public/animations/light-reflection-and-refraction.html...")

    slides_html_list = []

    for s_idx, slide in enumerate(ALL_SLIDES):
        is_quiz = (s_idx >= 21)
        slide_num = s_idx + 1
        total_slides = len(ALL_SLIDES)

        if not is_quiz:
            theory_blocks_html = ""
            for tb in slide["theory_blocks"]:
                title = tb.get("title", tb.get("heading", ""))
                theory_blocks_html += f"""
                <div class="bg-slate-900/80 border border-slate-800/80 rounded-xl p-4 hover:border-slate-700 transition">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-rose-400 mb-1.5 flex items-center gap-1.5">
                        <span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
                        {title}
                    </h4>
                    <div class="text-xs sm:text-sm text-slate-300 leading-relaxed space-y-1.5">
                        {tb['content']}
                    </div>
                </div>
            """

            checkpoints_html = ""
            for q_idx, cp in enumerate(slide["checkpoints"]):
                options_html = ""
                for o_idx, opt in enumerate(cp["options"]):
                    options_html += f"""
                    <label class="flex items-start gap-2.5 p-2 rounded-lg bg-slate-950/70 border border-slate-800 hover:border-slate-700 cursor-pointer text-xs transition">
                        <input type="radio" name="chk-{s_idx}-{q_idx}" value="{o_idx}" onchange="checkCheckpointAnswer({s_idx}, {q_idx}, {o_idx}, {cp['ans']}, 'chk-sol-{s_idx}-{q_idx}')" class="mt-0.5 text-rose-600 focus:ring-rose-500 bg-slate-900 border-slate-700">
                        <span class="text-slate-300">{opt}</span>
                    </label>
                """

                cp_q_esc = cp['q'].replace("'", "\\'").replace('"', '&quot;')
                cp_sol_esc = cp['solution'].replace("'", "\\'").replace('"', '&quot;')

                checkpoints_html += f"""
                <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-4 mb-3">
                    <div class="flex items-center justify-between gap-2 mb-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Checkpoint {q_idx + 1} of 2</span>
                        <div class="flex items-center gap-2">
                            <div id="feedback-{s_idx}-{q_idx}"></div>
                            <button onclick="openQuizSolution('Slide {s_idx + 1} Checkpoint {q_idx + 1}', '{cp_q_esc}', '{cp_sol_esc}')" class="px-2.5 py-1 rounded-md bg-rose-600/30 hover:bg-rose-600/50 border border-rose-500/40 text-rose-300 text-xs font-bold transition flex items-center gap-1 cursor-pointer">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                <span>Solution</span>
                            </button>
                        </div>
                    </div>
                    <p class="text-xs sm:text-sm font-semibold text-white mb-2.5">{cp['q']}</p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-2">
                        {options_html}
                    </div>
                    <div id="chk-sol-{s_idx}-{q_idx}" class="hidden mt-2.5 p-3 rounded-lg bg-rose-950/30 border border-rose-500/30 text-xs text-slate-200">
                        <span class="font-bold text-rose-400">Step-by-Step Teacher Explanation:</span><br>
                        {cp['solution']}
                    </div>
                </div>
            """

            teacher_card_html = f"""
            <!-- Person Talking: Dr. Sophia Physics Master Avatar -->
            <div class="mb-6 p-4 rounded-2xl bg-gradient-to-r from-rose-950/40 via-slate-900 to-amber-950/20 border border-rose-500/30 flex flex-col sm:flex-row items-center sm:items-start gap-4 shadow-xl">
                <div class="relative shrink-0 flex flex-col items-center teacher-bob">
                    <svg viewBox="0 0 120 120" class="w-20 h-20 sm:w-24 sm:h-24 drop-shadow-lg">
                        <path d="M20 115 C20 85, 45 80, 60 80 C75 80, 100 85, 100 115 Z" fill="#e11d48" stroke="#f43f5e" stroke-width="2"/>
                        <polygon points="50,80 60,105 70,80" fill="#ffffff"/>
                        <circle cx="60" cy="50" r="26" fill="#fed7aa" stroke="#f97316" stroke-width="1.5"/>
                        <path d="M34 50 C34 25, 86 25, 86 50 C86 35, 75 22, 60 22 C45 22, 34 35, 34 50 Z" fill="#1e1b4b"/>
                        <circle cx="50" cy="48" r="7" fill="none" stroke="#be123c" stroke-width="2"/>
                        <circle cx="70" cy="48" r="7" fill="none" stroke="#be123c" stroke-width="2"/>
                        <line x1="57" y1="48" x2="63" y2="48" stroke="#be123c" stroke-width="2"/>
                        <circle cx="50" cy="48" r="2.5" fill="#1e293b"/>
                        <circle cx="70" cy="48" r="2.5" fill="#1e293b"/>
                        <path d="M44 38 Q50 35 56 38" fill="none" stroke="#78350f" stroke-width="2"/>
                        <path d="M64 38 Q70 35 76 38" fill="none" stroke="#78350f" stroke-width="2"/>
                        <ellipse id="teacherMouth-{s_idx}" cx="60" cy="64" rx="5" ry="3" fill="#be123c"/>
                    </svg>
                    <span class="px-2 py-0.5 rounded-full text-[9px] font-extrabold bg-rose-500/20 text-rose-300 border border-rose-500/30 mt-1">
                        Dr. Sophia • Physics Educator
                    </span>
                </div>

                <div class="flex-1 bg-slate-950 p-3.5 rounded-2xl border border-slate-800 relative">
                    <div class="hidden sm:block absolute -left-2 top-6 w-3 h-3 bg-slate-950 border-l border-b border-slate-800 transform rotate-45"></div>
                    <div class="flex items-center justify-between mb-1">
                        <span class="text-xs font-bold text-rose-400 flex items-center gap-1.5">
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                            Teacher's Live Audio Commentary
                        </span>
                        <span class="text-[10px] text-slate-500 font-mono">Web Speech Narration</span>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-300 italic leading-relaxed">
                        "{slide['narration']}"
                    </p>
                </div>
            </div>
            """

            simulator_html = get_simulator_markup(s_idx)

            slide_markup = f"""
            <div id="slide-{s_idx}" class="slide-container">
                <div class="bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 mb-6 shadow-xl relative overflow-hidden">
                    <div class="absolute right-0 top-0 bottom-0 w-1/3 bg-gradient-to-l from-rose-500/10 to-transparent pointer-events-none"></div>
                    <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
                        <span class="px-2.5 py-1 rounded-md text-xs font-extrabold uppercase tracking-wider bg-rose-500/20 text-rose-300 border border-rose-500/40">
                            {slide['tag']}
                        </span>
                        <span class="text-xs font-mono font-semibold text-slate-400">Slide {slide_num} of {total_slides}</span>
                    </div>
                    <h2 class="text-xl sm:text-2xl font-black text-white tracking-tight mb-1">{slide['title']}</h2>
                    <p class="text-xs sm:text-sm text-rose-400 font-medium mb-3">{slide['subtitle']}</p>
                    <p class="text-xs sm:text-sm text-slate-300 border-l-2 border-rose-500 pl-3 italic mb-4">{slide['lead']}</p>
                    
                    <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800/80 mb-6">
                        <div class="text-[11px] font-bold text-amber-400 uppercase tracking-wider mb-1">Key Takeaway</div>
                        <div class="text-xs text-slate-300">{slide['quote']}</div>
                    </div>

                    {teacher_card_html}

                    <div class="space-y-6">
                        <div>{simulator_html}</div>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">{theory_blocks_html}</div>
                        <div class="pt-2">
                            <h3 class="text-sm font-bold text-white uppercase tracking-wider mb-3 flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                                Slide Checkpoint Questions & Step-by-Step Solutions
                            </h3>
                            {checkpoints_html}
                        </div>
                    </div>
                </div>
            </div>
            """
        else:
            # Quiz slide (Slides 22 to 25, index 21 to 24)
            questions_html = ""
            for q in slide["questions"]:
                q_id = q["id"]
                options_html = ""
                for o_idx, opt in enumerate(q["options"]):
                    options_html += f"""
                    <label class="flex items-start gap-2.5 p-2 rounded-lg bg-slate-950/70 border border-slate-800 hover:border-slate-700 cursor-pointer text-xs transition">
                        <input type="radio" name="quiz-{s_idx}-{q_id}" value="{o_idx}" onchange="checkCheckpointAnswer({s_idx}, {q_id}, {o_idx}, {q['ans']}, 'quiz-feedback-{q_id}')" class="mt-0.5 text-rose-600 focus:ring-rose-500 bg-slate-900 border-slate-700">
                        <span class="text-slate-300">{opt}</span>
                    </label>
                """

                q_title_esc = q['q'].replace("'", "\\'").replace('"', '&quot;')
                q_sol_esc = q['solution'].replace("'", "\\'").replace('"', '&quot;')

                questions_html += f"""
                <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-4 shadow">
                    <div class="flex items-center justify-between gap-2 mb-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Question {q_id}</span>
                        <div class="flex items-center gap-2">
                            <div id="quiz-feedback-{q_id}"></div>
                            <button onclick="openQuizSolution({q_id}, '{q_title_esc}', '{q_sol_esc}')" class="px-2.5 py-1 rounded-md bg-rose-600/30 hover:bg-rose-600/50 border border-rose-500/40 text-rose-300 text-xs font-bold transition flex items-center gap-1 cursor-pointer">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                <span>Solution</span>
                            </button>
                        </div>
                    </div>
                    <p class="text-xs sm:text-sm font-semibold text-white mb-2.5">{q['q']}</p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-2">
                        {options_html}
                    </div>
                </div>
                """

            completion_banner = ""
            if s_idx == total_slides - 1:
                completion_banner = """
                <div id="lastSlideNotice" class="mt-6 p-4 rounded-xl bg-rose-950/40 border border-rose-500/40 text-center">
                    <div class="inline-flex items-center gap-2 text-rose-400 font-extrabold text-sm mb-1">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        <span>You have reached the last slide of this chapter (Chapter 9: Light – Reflection and Refraction)!</span>
                    </div>
                    <p class="text-xs text-slate-300">Congratulations! You have completed all 21 master interactive lessons and all 40 mastery challenge questions covering the entire NCERT textbook.</p>
                </div>
                """

            slide_markup = f"""
            <div id="slide-{s_idx}" class="slide-container">
                <div class="bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 mb-6 shadow-xl">
                    <div class="flex flex-wrap items-center justify-between gap-3 mb-2">
                        <span class="px-2.5 py-1 rounded-md text-xs font-extrabold uppercase tracking-wider bg-rose-500/20 text-rose-300 border border-rose-500/40">
                            {slide['tag']}
                        </span>
                        <span class="text-xs font-mono font-semibold text-slate-400">Slide {slide_num} of {total_slides}</span>
                    </div>
                    <h2 class="text-xl sm:text-2xl font-black text-white tracking-tight mb-1">{slide['title']}</h2>
                    <p class="text-xs sm:text-sm text-rose-400 font-medium mb-4">{slide['subtitle']}</p>

                    <div class="space-y-4">
                        {questions_html}
                    </div>
                    {completion_banner}
                </div>
            </div>
            """

        slides_html_list.append(slide_markup)

    slides_body_content = "\n".join(slides_html_list)

    # Topic Navigation Pills
    pills = []
    for idx, slide in enumerate(ALL_SLIDES):
        short_title = slide["title"]
        if "•" in short_title:
            short_title = short_title.split("•")[0].strip()
        elif ":" in short_title:
            short_title = short_title.split(":")[0].strip()
        pills.append(f"""
            <button onclick="goToSlide({idx})" id="pill-{idx}" class="px-3 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap transition cursor-pointer { 'bg-rose-600 text-white font-bold' if idx == 0 else 'bg-slate-800 text-slate-300 hover:bg-slate-700' }">
                {idx + 1}. {short_title[:24]}
            </button>
        """)
    pills_html = "\n".join(pills)

    # Slides data JSON for navigation and voiceover
    slides_metadata = []
    for s_idx, slide in enumerate(ALL_SLIDES):
        slides_metadata.append({
            "index": s_idx,
            "title": slide["title"],
            "narration": slide.get("narration", f"Mastery quiz challenge questions {s_idx - 20} covering NCERT Chapter 9."),
            "isQuiz": (s_idx >= 21)
        })
    slides_json_str = json.dumps(slides_metadata)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 10 Science • Chapter 9: Light - Reflection and Refraction Master Lab</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- KaTeX for crisp formulas -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
    
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        slate: {{
                            850: '#111827',
                            950: '#030712'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600;700&display=swap');
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
            transition: opacity 0.3s ease-in-out;
        }}
        .slide-container.active {{
            display: block;
            opacity: 1;
        }}
        .custom-scrollbar::-webkit-scrollbar {{
            height: 6px;
        }}
        .custom-scrollbar::-webkit-scrollbar-track {{
            background: #0f172a;
            border-radius: 4px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: #e11d48;
            border-radius: 4px;
        }}
        @keyframes teacherBob {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-3px); }}
        }}
        .teacher-bob {{
            animation: teacherBob 3s ease-in-out infinite;
        }}
        @keyframes mouthTalk {{
            0%, 100% {{ ry: 2; rx: 4; }}
            50% {{ ry: 6; rx: 5; }}
        }}
        .talking-mouth {{
            animation: mouthTalk 0.25s infinite;
        }}
        .modal-backdrop {{
            background-color: rgba(3, 7, 18, 0.85);
            backdrop-filter: blur(8px);
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col bg-slate-950 text-slate-100 antialiased selection:bg-rose-500 selection:text-white">

    <!-- Top Header Bar -->
    <header class="bg-slate-900 border-b border-slate-800 sticky top-0 z-40 px-4 py-3 sm:px-6 shadow-xl backdrop-blur-md bg-slate-900/90">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <a href="/multimedia?syllabus=ncert&subject=science&class=class10" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition flex items-center justify-center border border-slate-700" title="Back to Curriculum Tree">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
                </a>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-extrabold uppercase tracking-wider bg-rose-500/20 text-rose-300 border border-rose-500/30">Class 10 Science</span>
                        <span class="text-xs text-slate-400 font-semibold hidden sm:inline">Chapter 9</span>
                    </div>
                    <h1 class="text-sm sm:text-base font-extrabold text-white tracking-tight flex items-center gap-2">
                        <span>Light – Reflection and Refraction</span>
                        <span class="text-xs text-rose-400 font-normal hidden md:inline">• Master Interactive Lab</span>
                    </h1>
                </div>
            </div>

            <!-- Voiceover & Audio Controls -->
            <div class="flex items-center gap-2">
                <button id="voiceToggleBtn" onclick="toggleVoice()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 text-xs font-bold transition flex items-center gap-1.5 cursor-pointer">
                    <svg id="voiceIconOn" class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/></svg>
                    <svg id="voiceIconOff" class="w-4 h-4 text-rose-400 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2"/></svg>
                    <span id="voiceStatusText">Voice On</span>
                </button>
                <button onclick="replayVoice()" class="p-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-300 hover:text-white transition flex items-center justify-center cursor-pointer" title="Replay Teacher Audio">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 flex flex-col justify-between">
        <div id="slidesViewport">
            {slides_body_content}
        </div>
    </main>

    <!-- Bottom Navigation Footer & Topic Pills -->
    <footer class="bg-slate-900 border-t border-slate-800 sticky bottom-0 z-30 px-4 py-3 sm:px-6 shadow-2xl">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
            <div class="flex items-center gap-2 w-full sm:w-auto justify-between sm:justify-start">
                <button id="prevBtn" onclick="navigateSlide(-1)" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold transition flex items-center gap-1.5 disabled:opacity-40 disabled:cursor-not-allowed border border-slate-700 cursor-pointer">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
                    <span>Previous</span>
                </button>
                <button id="nextBtn" onclick="navigateSlide(1)" class="px-5 py-2 rounded-xl bg-gradient-to-r from-rose-600 to-amber-500 hover:from-rose-500 hover:to-amber-400 text-white text-xs font-bold transition flex items-center gap-1.5 shadow-lg shadow-rose-600/30 cursor-pointer">
                    <span>Next Slide</span>
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </button>
            </div>

            <div class="flex items-center gap-1.5 overflow-x-auto max-w-full sm:max-w-2xl py-1 custom-scrollbar">
                {pills_html}
            </div>

            <div class="hidden md:flex items-center gap-2 text-xs text-slate-400 font-mono">
                <span>Slide</span>
                <span id="currentSlideIndicator" class="text-rose-400 font-bold">1</span>
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
                <span class="px-2.5 py-1 rounded-md text-xs font-extrabold uppercase tracking-wider bg-rose-500/20 text-rose-300 border border-rose-500/40">
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
                <button onclick="closeSolutionModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-white transition cursor-pointer">
                    Got it, Close
                </button>
            </div>
        </div>
    </div>

    <!-- JavaScript Engine -->
    <script>
        const slidesData = {slides_json_str};
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
                newPill.classList.add('bg-rose-600', 'text-white', 'font-bold');
                newPill.scrollIntoView({{ behavior: 'smooth', inline: 'center', block: 'nearest' }});
            }}

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
                currentSlideIndex = newIdx;
                showSlide(currentSlideIndex);
                playTone(440, 'sine', 0.08);
            }}
        }}

        function goToSlide(index) {{
            if (index >= 0 && index < slidesData.length) {{
                currentSlideIndex = index;
                showSlide(currentSlideIndex);
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

            speechSynth.speak(currentUtterance);
        }}

        function checkCheckpointAnswer(slideIdx, qIdx, selectedOption, correctOption, solutionId) {{
            const solEl = document.getElementById(solutionId);
            let feedbackEl = document.getElementById(`feedback-${{slideIdx}}-${{qIdx}}`);
            if (!feedbackEl && solEl && solEl.id && solEl.id.startsWith('quiz-feedback')) {{
                feedbackEl = solEl;
            }}
            
            if (selectedOption === correctOption) {{
                playCorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-emerald-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Correct! Excellent</span>`;
                if (solEl && solEl !== feedbackEl) solEl.classList.remove('hidden');
            }} else {{
                playIncorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-rose-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg> Incorrect. Click Solution</span>`;
                if (solEl && solEl !== feedbackEl) solEl.classList.remove('hidden');
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
        function setSim1Mode(mode) {{
            playTone(480, 'sine', 0.08);
            const raysGroup = document.getElementById('sim1-rays-group');
            const wavesGroup = document.getElementById('sim1-waves-group');
            const desc = document.getElementById('sim1-desc');
            const btnRay = document.getElementById('btn-sim1-ray');
            const btnWave = document.getElementById('btn-sim1-wave');
            if (mode === 'ray') {{
                raysGroup.classList.remove('hidden');
                wavesGroup.classList.add('hidden');
                btnRay.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-500 text-slate-950 transition';
                btnWave.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                desc.textContent = "Rectilinear Propagation: Light travels along straight lines, casting crisp shadows behind macroscopic objects.";
            }} else {{
                raysGroup.classList.add('hidden');
                wavesGroup.classList.remove('hidden');
                btnWave.className = 'px-2.5 py-1 rounded text-xs font-bold bg-cyan-500 text-slate-950 transition';
                btnRay.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                desc.textContent = "Diffraction: Around microscopic obstacles, rectilinear ray optics fails and light behaves as a bending wave.";
            }}
        }}

        function updateSim2(angleDeg) {{
            const deg = parseFloat(angleDeg);
            document.getElementById('sim2-angle-val').textContent = `${{deg}}°`;
            document.getElementById('sim2-i-display').textContent = `∠i = ${{deg}}°`;
            document.getElementById('sim2-r-display').textContent = `∠r = ${{deg}}°`;
            
            const rad = (deg * Math.PI) / 180;
            const L = 160;
            const incX = 230 - L * Math.sin(rad);
            const incY = 180 - L * Math.cos(rad);
            const refX = 230 + L * Math.sin(rad);
            const refY = 180 - L * Math.cos(rad);
            
            const incLine = document.getElementById('sim2-incident-ray');
            const refLine = document.getElementById('sim2-reflected-ray');
            if (incLine && refLine) {{
                incLine.setAttribute('x1', incX);
                incLine.setAttribute('y1', incY);
                refLine.setAttribute('x2', refX);
                refLine.setAttribute('y2', refY);
            }}
        }}

        function setSim3Type(type) {{
            playTone(450, 'sine', 0.08);
            const path = document.getElementById('sim3-mirror-path');
            const info = document.getElementById('sim3-info');
            const btnConc = document.getElementById('btn-sim3-concave');
            const btnConv = document.getElementById('btn-sim3-convex');
            if (type === 'concave') {{
                path.setAttribute('d', 'M 380 25 A 150 150 0 0 0 380 175');
                info.innerHTML = 'Concave Mirror: Reflecting surface curves <strong>inward</strong>. $C$ and $F$ lie <strong>in front</strong> of the mirror. $R = 2f$.';
                btnConc.className = 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition';
                btnConv.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
            }} else {{
                path.setAttribute('d', 'M 350 25 A 150 150 0 0 1 350 175');
                info.innerHTML = 'Convex Mirror: Reflecting surface bulges <strong>outward</strong>. $C$ and $F$ lie <strong>behind</strong> the reflecting mirror.';
                btnConv.className = 'px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 text-white transition';
                btnConc.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
            }}
            if (window.renderMathInElement) renderMathInElement(info);
        }}

        function triggerSolarIgnition() {{
            playTone(600, 'sawtooth', 0.2);
            const flame = document.getElementById('sim4-flame');
            if (flame) {{
                flame.classList.remove('hidden');
                setTimeout(() => {{
                    playTone(800, 'sine', 0.3);
                }}, 200);
            }}
        }}

        function setSim5Rule(ruleNum) {{
            playTone(460, 'sine', 0.08);
            for (let i = 1; i <= 4; i++) {{
                const btn = document.getElementById(`btn-rule-${{i}}`);
                if (btn) btn.className = (i === ruleNum) ? 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white' : 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700';
            }}
            const grp = document.getElementById('sim5-ray-group');
            const txt = document.getElementById('sim5-text');
            if (ruleNum === 1) {{
                grp.innerHTML = '<line x1="60" y1="40" x2="355" y2="40" stroke="#38bdf8" stroke-width="2.5"/><line x1="355" y1="40" x2="160" y2="125" stroke="#f43f5e" stroke-width="2.5"/>';
                txt.textContent = "Rule 1: A ray incident parallel to the principal axis passes through the principal focus F after reflection (Fig 9.3a).";
            }} else if (ruleNum === 2) {{
                grp.innerHTML = '<line x1="160" y1="35" x2="355" y2="135" stroke="#38bdf8" stroke-width="2.5"/><line x1="355" y1="135" x2="60" y2="135" stroke="#f43f5e" stroke-width="2.5"/>';
                txt.textContent = "Rule 2: A ray passing through the principal focus F emerges strictly parallel to the principal axis after reflection (Fig 9.4a).";
            }} else if (ruleNum === 3) {{
                grp.innerHTML = '<line x1="60" y1="20" x2="355" y2="155" stroke="#38bdf8" stroke-width="2.5"/><line x1="355" y1="155" x2="60" y2="20" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="4,4"/>';
                txt.textContent = "Rule 3: A ray passing through the centre of curvature C hits along the normal line and retraces its exact path backwards (Fig 9.5a).";
            }} else if (ruleNum === 4) {{
                grp.innerHTML = '<line x1="180" y1="30" x2="350" y2="90" stroke="#38bdf8" stroke-width="2.5"/><line x1="350" y1="90" x2="180" y2="150" stroke="#f43f5e" stroke-width="2.5"/>';
                txt.textContent = "Rule 4: A ray incident obliquely at the pole P reflects symmetrically on the other side such that the principal axis acts as normal (Fig 9.6a).";
            }}
        }}

        function setSim6Case(cNum) {{
            playTone(470, 'sine', 0.08);
            for (let i = 1; i <= 3; i++) {{
                const b = document.getElementById(`btn-case-${{i}}`);
                if (b) b.className = (i === cNum) ? 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white' : 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700';
            }}
            const art = document.getElementById('sim6-art');
            const st = document.getElementById('sim6-status');
            if (cNum === 1) {{
                art.innerHTML = '<line x1="40" y1="40" x2="368" y2="40" stroke="#facc15" stroke-width="2"/><line x1="368" y1="40" x2="260" y2="100" stroke="#facc15" stroke-width="2"/><line x1="40" y1="160" x2="368" y2="160" stroke="#facc15" stroke-width="2"/><line x1="368" y1="160" x2="260" y2="100" stroke="#facc15" stroke-width="2"/><circle cx="260" cy="100" r="4.5" fill="#10b981"/><text x="260" y="85" fill="#10b981" font-size="9" text-anchor="middle" font-weight="bold">Point Image at F</text>';
                st.textContent = "Case 1: Object at Infinity → Real, inverted, highly diminished (point-sized) image formed at Focus F.";
            }} else if (cNum === 2) {{
                art.innerHTML = '<line x1="90" y1="100" x2="90" y2="55" stroke="#38bdf8" stroke-width="3"/><polygon points="90,50 86,58 94,58" fill="#38bdf8"/><text x="90" y="45" fill="#38bdf8" font-size="9" text-anchor="middle">Object Beyond C</text><line x1="90" y1="55" x2="365" y2="55" stroke="#facc15" stroke-width="2"/><line x1="365" y1="55" x2="190" y2="140" stroke="#facc15" stroke-width="2"/><line x1="90" y1="55" x2="368" y2="140" stroke="#ec4899" stroke-width="2"/><line x1="205" y1="100" x2="205" y2="125" stroke="#10b981" stroke-width="3"/><polygon points="205,130 201,122 209,122" fill="#10b981"/><text x="205" y="145" fill="#10b981" font-size="9" text-anchor="middle">Diminished Image</text>';
                st.textContent = "Case 2: Object Beyond C → Real, inverted, diminished image formed between F and C.";
            }} else if (cNum === 3) {{
                art.innerHTML = '<line x1="160" y1="100" x2="160" y2="55" stroke="#38bdf8" stroke-width="3"/><polygon points="160,50 156,58 164,58" fill="#38bdf8"/><text x="160" y="45" fill="#38bdf8" font-size="9" text-anchor="middle">Object at C</text><line x1="160" y1="55" x2="365" y2="55" stroke="#facc15" stroke-width="2"/><line x1="365" y1="55" x2="160" y2="145" stroke="#facc15" stroke-width="2"/><line x1="160" y1="100" x2="160" y2="145" stroke="#10b981" stroke-width="3"/><polygon points="160,150 156,142 164,142" fill="#10b981"/><text x="160" y="165" fill="#10b981" font-size="9" text-anchor="middle" font-weight="bold">Image at C (Same Size! m = -1)</text>';
                st.textContent = "Case 3: Object directly at C → Real, inverted image formed right at C with exact same dimensions ($m = -1$).";
            }}
        }}

        function setSim7Case(cNum) {{
            playTone(480, 'sine', 0.08);
            for (let i = 4; i <= 6; i++) {{
                const b = document.getElementById(`btn-case-${{i}}`);
                if (b) b.className = (i === cNum) ? 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white' : 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700';
            }}
            const art = document.getElementById('sim7-art');
            const st = document.getElementById('sim7-status');
            if (cNum === 4) {{
                art.innerHTML = '<line x1="170" y1="100" x2="170" y2="65" stroke="#38bdf8" stroke-width="3"/><polygon points="170,60 166,68 174,68" fill="#38bdf8"/><line x1="170" y1="65" x2="330" y2="65" stroke="#facc15" stroke-width="2"/><line x1="330" y1="65" x2="70" y2="160" stroke="#facc15" stroke-width="2"/><line x1="70" y1="100" x2="70" y2="160" stroke="#10b981" stroke-width="4"/><polygon points="70,166 65,156 75,156" fill="#10b981"/><text x="70" y="180" fill="#10b981" font-size="9" text-anchor="middle" font-weight="bold">Enlarged Image Beyond C</text>';
                st.textContent = "Case 4: Object between C and F → Real, inverted, and magnified image formed beyond C.";
            }} else if (cNum === 5) {{
                art.innerHTML = '<circle cx="220" cy="100" r="5" fill="#facc15"/><text x="220" y="90" fill="#facc15" font-size="9" text-anchor="middle">Bulb at Focus F</text><line x1="220" y1="100" x2="330" y2="35" stroke="#facc15" stroke-width="2.5"/><line x1="330" y1="35" x2="20" y2="35" stroke="#fde047" stroke-width="3"/><line x1="220" y1="100" x2="330" y2="165" stroke="#facc15" stroke-width="2.5"/><line x1="330" y1="165" x2="20" y2="165" stroke="#fde047" stroke-width="3"/><text x="100" y="30" fill="#fde047" font-size="9" font-weight="bold">Parallel Beam to Infinity →</text>';
                st.textContent = "Case 5: Bulb placed at Focus F → Reflected rays emerge parallel to infinity (Headlights & searchlights).";
            }} else if (cNum === 6) {{
                art.innerHTML = '<line x1="270" y1="100" x2="270" y2="70" stroke="#38bdf8" stroke-width="3"/><polygon points="270,65 266,73 274,73" fill="#38bdf8"/><text x="270" y="60" fill="#38bdf8" font-size="9" text-anchor="middle">Tooth</text><line x1="270" y1="70" x2="325" y2="70" stroke="#facc15" stroke-width="2"/><line x1="325" y1="70" x2="160" y2="145" stroke="#facc15" stroke-width="2"/><line x1="325" y1="70" x2="410" y2="35" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,3"/><line x1="325" y1="100" x2="410" y2="35" stroke="#ec4899" stroke-width="1.5" stroke-dasharray="3,3"/><line x1="410" y1="100" x2="410" y2="35" stroke="#10b981" stroke-width="3.5" stroke-dasharray="4,2"/><polygon points="410,30 405,40 415,40" fill="#10b981"/><text x="410" y="25" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Virtual Magnified Image</text>';
                st.textContent = "Case 6: Object inside F → Reflected rays diverge; backward extensions form an erect, magnified virtual image.";
            }}
        }}

        function updateSim8(dist) {{
            const d = parseFloat(dist);
            const car = document.getElementById('sim8-car');
            const carLabel = document.getElementById('sim8-car-label');
            const img = document.getElementById('sim8-img-rect');
            if (car && img) {{
                const carX = 230 - d;
                car.setAttribute('x', carX);
                carLabel.setAttribute('x', carX + 12);
                
                // image moves from F(310) towards P(230) as car moves closer
                const imgX = 230 + (d * 80) / (d + 60);
                const imgH = 45 * (60 / (d + 60));
                const imgY = 100 - imgH;
                img.setAttribute('x', imgX);
                img.setAttribute('y', imgY);
                img.setAttribute('height', imgH);
            }}
        }}

        function calcMirrorFormula() {{
            const uVal = -parseFloat(document.getElementById('sim10-u').value);
            document.getElementById('sim10-u-val').textContent = `${{uVal}} cm`;
            const f = -15.0; // concave
            
            // 1/v = 1/f - 1/u
            const invV = (1 / f) - (1 / uVal);
            const v = 1 / invV;
            const m = -v / uVal;
            
            document.getElementById('sim10-v-res').textContent = `${{v.toFixed(1)}} cm`;
            const mText = (m > 0) ? `+${{m.toFixed(2)}} (Virtual, Erect)` : `${{m.toFixed(2)}} (Real, Inverted)`;
            document.getElementById('sim10-m-res').textContent = mText;
        }}

        function toggleWaterCoin() {{
            playTone(520, 'sine', 0.15);
            const water = document.getElementById('sim11-water');
            const appCoin = document.getElementById('sim11-apparent-coin');
            const drySight = document.getElementById('sim11-dry-sight');
            const st = document.getElementById('sim11-status');
            
            if (appCoin.classList.contains('hidden')) {{
                water.setAttribute('opacity', '0.45');
                appCoin.classList.remove('hidden');
                drySight.classList.add('hidden');
                st.innerHTML = '<span class="text-emerald-400 font-bold">Water Poured!</span> Light bends away from the normal upon exiting into air, elevating the apparent coin over the rim!';
            }} else {{
                water.setAttribute('opacity', '0.1');
                appCoin.classList.add('hidden');
                drySight.classList.remove('hidden');
                st.textContent = "Dry Bowl: The bowl rim blocks the straight line of sight to the coin. Pour water to bend light and reveal the coin!";
            }}
        }}

        function updateSim12(angle) {{
            const deg = parseFloat(angle);
            document.getElementById('sim12-angle-val').textContent = `${{deg}}°`;
            
            // Snell law: sin r = sin i / 1.52
            const radI = (deg * Math.PI) / 180;
            const sinR = Math.sin(radI) / 1.52;
            const radR = Math.asin(sinR);
            
            const xO = 180;
            const slabThick = 70;
            const dx = slabThick * Math.tan(radR);
            const xOp = xO + dx;
            
            const refr = document.getElementById('sim12-refr');
            const emerg = document.getElementById('sim12-emerg');
            if (refr && emerg) {{
                refr.setAttribute('x2', xOp);
                emerg.setAttribute('x1', xOp);
                emerg.setAttribute('x2', xOp + 70);
            }}
        }}

        function setSim13Medium(med) {{
            playTone(500, 'sine', 0.08);
            const bWater = document.getElementById('btn-med-water');
            const bGlass = document.getElementById('btn-med-glass');
            const bDiamond = document.getElementById('btn-med-diamond');
            
            let n = 1.52;
            bWater.className = 'px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300';
            bGlass.className = 'px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300';
            bDiamond.className = 'px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300';
            
            if (med === 'water') {{
                n = 1.33;
                bWater.className = 'px-2 py-1 rounded text-xs font-bold bg-rose-600 text-white';
            }} else if (med === 'glass') {{
                n = 1.52;
                bGlass.className = 'px-2 py-1 rounded text-xs font-bold bg-rose-600 text-white';
            }} else {{
                n = 2.42;
                bDiamond.className = 'px-2 py-1 rounded text-xs font-bold bg-rose-600 text-white';
            }}
            
            const sinI = Math.sin(45 * Math.PI / 180);
            const sinR = sinI / n;
            const rDeg = (Math.asin(sinR) * 180 / Math.PI).toFixed(1);
            
            document.getElementById('sim13-n-display').textContent = n.toFixed(2);
            document.getElementById('sim13-sin-display').textContent = `0.707 / ${{n}} = ${{sinR.toFixed(3)}}`;
            document.getElementById('sim13-r-display').textContent = `${{rDeg}}°`;
        }}

        function setSim15Lens(type) {{
            playTone(460, 'sine', 0.08);
            const bCvx = document.getElementById('btn-sim15-cvx');
            const bCcv = document.getElementById('btn-sim15-ccv');
            const path = document.getElementById('sim15-lens-shape');
            if (type === 'convex') {{
                path.setAttribute('d', 'M 230 20 Q 250 100 230 180 Q 210 100 230 20 Z');
                bCvx.className = 'px-2.5 py-1 rounded text-xs font-bold bg-cyan-500 text-slate-950';
                bCcv.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700';
            }} else {{
                path.setAttribute('d', 'M 230 20 Q 215 100 230 180 L 236 180 Q 221 100 236 20 Z');
                bCcv.className = 'px-2.5 py-1 rounded text-xs font-bold bg-cyan-500 text-slate-950';
                bCvx.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700';
            }}
        }}

        function setSim16Case(cNum) {{
            playTone(470, 'sine', 0.08);
            for (let i = 1; i <= 6; i++) {{
                const b = document.getElementById(`btn-lcase-${{i}}`);
                if (b) b.className = (i === cNum) ? 'px-2 py-1 rounded text-xs font-bold bg-rose-600 text-white' : 'px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700';
            }}
            const art = document.getElementById('sim16-art');
            const st = document.getElementById('sim16-status');
            if (cNum === 1) {{
                art.innerHTML = '<circle cx="310" cy="100" r="4.5" fill="#10b981"/><text x="310" y="85" fill="#10b981" font-size="8" text-anchor="middle" font-weight="bold">Point Image at F2</text>';
                st.textContent = "Position 1: Object at Infinity → Real, inverted, highly diminished image formed at Focus F2.";
            }} else if (cNum === 2) {{
                art.innerHTML = '<line x1="40" y1="100" x2="40" y2="50" stroke="#38bdf8" stroke-width="3"/><polygon points="40,45 36,54 44,54" fill="#38bdf8"/><line x1="350" y1="100" x2="350" y2="135" stroke="#10b981" stroke-width="2.5"/><polygon points="350,140 346,132 354,132" fill="#10b981"/><text x="350" y="155" fill="#10b981" font-size="8" text-anchor="middle">Diminished Image</text>';
                st.textContent = "Position 2: Object Beyond 2F1 → Real, inverted, diminished image between F2 and 2F2.";
            }} else if (cNum === 3) {{
                art.innerHTML = '<line x1="70" y1="100" x2="70" y2="50" stroke="#38bdf8" stroke-width="3"/><polygon points="70,45 66,54 74,54" fill="#38bdf8"/><line x1="390" y1="100" x2="390" y2="150" stroke="#10b981" stroke-width="3"/><polygon points="390,155 386,146 394,146" fill="#10b981"/><text x="390" y="170" fill="#10b981" font-size="8" text-anchor="middle" font-weight="bold">Image at 2F2 (Same Size)</text>';
                st.textContent = "Position 3: Object at 2F1 → Real, inverted, same-size image formed at 2F2 ($m = -1$).";
            }} else if (cNum === 4) {{
                art.innerHTML = '<line x1="110" y1="100" x2="110" y2="60" stroke="#38bdf8" stroke-width="3"/><polygon points="110,55 106,64 114,64" fill="#38bdf8"/><line x1="420" y1="100" x2="420" y2="165" stroke="#10b981" stroke-width="3.5"/><polygon points="420,170 416,162 424,162" fill="#10b981"/><text x="420" y="185" fill="#10b981" font-size="8" text-anchor="middle" font-weight="bold">Enlarged Beyond 2F2</text>';
                st.textContent = "Position 4: Object between F1 and 2F1 → Real, inverted, enlarged image beyond 2F2.";
            }} else if (cNum === 5) {{
                art.innerHTML = '<circle cx="150" cy="100" r="4.5" fill="#facc15"/><text x="150" y="85" fill="#facc15" font-size="8" text-anchor="middle">Object at F1</text><line x1="230" y1="50" x2="430" y2="50" stroke="#fde047" stroke-width="2.5"/><line x1="230" y1="150" x2="430" y2="150" stroke="#fde047" stroke-width="2.5"/><text x="330" y="42" fill="#fde047" font-size="8">Parallel Rays to Infinity →</text>';
                st.textContent = "Position 5: Object at F1 → Refracted rays emerge parallel to infinity (Searchlights).";
            }} else if (cNum === 6) {{
                art.innerHTML = '<line x1="190" y1="100" x2="190" y2="70" stroke="#38bdf8" stroke-width="3"/><polygon points="190,65 186,73 194,73" fill="#38bdf8"/><text x="190" y="60" fill="#38bdf8" font-size="8" text-anchor="middle">Text</text><line x1="110" y1="100" x2="110" y2="40" stroke="#10b981" stroke-width="3.5" stroke-dasharray="3,3"/><polygon points="110,35 106,43 114,43" fill="#10b981"/><text x="110" y="25" fill="#10b981" font-size="8" text-anchor="middle" font-weight="bold">Virtual Erect Magnified</text>';
                st.textContent = "Position 6: Object inside F1 → Virtual, erect, magnified image on same side (Magnifying Glass!).";
            }}
        }}

        function calcLensFormula() {{
            const uVal = -parseFloat(document.getElementById('sim18-u').value);
            document.getElementById('sim18-u-val').textContent = `${{uVal}} cm`;
            const f = 10.0; // convex
            
            // 1/v = 1/u + 1/f
            const invV = (1 / uVal) + (1 / f);
            const v = 1 / invV;
            const m = v / uVal;
            
            document.getElementById('sim18-v-res').textContent = `${{v.toFixed(1)}} cm`;
            const mText = (m > 0) ? `+${{m.toFixed(2)}} (Virtual, Erect)` : `${{m.toFixed(2)}} (Real, Inverted)`;
            document.getElementById('sim18-m-res').textContent = mText;
        }}

        function updateSim19Power(fValCm) {{
            const fM = parseFloat(fValCm) / 100;
            document.getElementById('sim19-f-val').textContent = `+${{fM.toFixed(2)}} m`;
            const p = 1 / fM;
            document.getElementById('sim19-power-res').textContent = `+${{p.toFixed(2)}} D`;
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
    out_path = "public/animations/light-reflection-and-refraction.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"Successfully generated {out_path} ({len(html_template)} bytes)")

if __name__ == '__main__':
    generate_html()

