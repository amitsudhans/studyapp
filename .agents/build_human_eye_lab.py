#!/usr/bin/env python3
"""
Full Generator for NCERT Class 10 Science, Chapter 10: The Human Eye and the Colourful World
Master Interactive Multimedia Lab
File: public/animations/the-human-eye-and-the-colourful-world.html
"""

import json
import os
import sys

sys.path.append(os.path.abspath('.agents'))
from human_eye_data import CONTENT_SLIDES, QUIZ_SLIDES

ALL_SLIDES = CONTENT_SLIDES + QUIZ_SLIDES

def get_simulator_markup(s_idx):
    """Generate interactive SVG laboratory simulators for all 16 content slides."""
    if s_idx == 0:
        # Slide 1: Eye Anatomy & Pupil Constriction/Dilation
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-indigo-400"></span>
                    Interactive Lab 10.1: Ocular Ray Tracer & Pupil Reflex
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300 font-semibold">Ambient Light:</label>
                    <input type="range" id="sim1-light" min="1" max="5" value="3" oninput="updateSim1Pupil(this.value)" class="w-28 sm:w-36 accent-indigo-400 cursor-pointer">
                    <span id="sim1-light-val" class="text-xs font-mono font-bold text-indigo-400">Normal</span>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center min-h-[220px]">
                <svg id="svg-sim1" viewBox="0 0 500 210" class="w-full max-w-lg h-auto">
                    <!-- Eyeball Outline (2.3 cm sphere) -->
                    <circle cx="280" cy="105" r="85" fill="#0f172a" stroke="#6366f1" stroke-width="2.5"/>
                    <!-- Cornea (Front bulge) -->
                    <path d="M 200 45 A 90 90 0 0 1 200 165 A 75 75 0 0 0 200 45 Z" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="2"/>
                    <text x="180" y="35" fill="#38bdf8" font-size="9" font-weight="bold">Cornea (Outer Bulge)</text>
                    
                    <!-- Crystalline Lens -->
                    <path id="sim1-lens" d="M 235 60 Q 248 105 235 150 Q 222 105 235 60 Z" fill="#818cf8" fill-opacity="0.5" stroke="#a5b4fc" stroke-width="2"/>
                    <text x="240" y="50" fill="#a5b4fc" font-size="9">Crystalline Lens</text>

                    <!-- Iris Upper & Lower -->
                    <rect id="sim1-iris-top" x="228" y="55" width="10" height="25" rx="3" fill="#4338ca"/>
                    <rect id="sim1-iris-bot" x="228" y="130" width="10" height="25" rx="3" fill="#4338ca"/>
                    <!-- Pupil aperture gap -->
                    <text x="215" y="108" fill="#e0e7ff" font-size="8" font-weight="bold">Pupil</text>
                    
                    <!-- Retina Back Layer -->
                    <path d="M 330 45 A 85 85 0 0 1 330 165" fill="none" stroke="#f43f5e" stroke-width="4"/>
                    <text x="375" y="105" fill="#f43f5e" font-size="9" font-weight="bold">Retina (Screen)</text>

                    <!-- Optic Nerve Exit -->
                    <path d="M 360 95 L 430 85 L 430 125 L 360 115 Z" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
                    <text x="435" y="108" fill="#94a3b8" font-size="9">To Optic Nerve</text>

                    <!-- Incoming Light Rays -->
                    <g id="sim1-rays">
                        <line x1="30" y1="80" x2="200" y2="90" stroke="#fef08a" stroke-width="2"/>
                        <line x1="200" y1="90" x2="232" y2="95" stroke="#fde047" stroke-width="2"/>
                        <line x1="232" y1="95" x2="365" y2="105" stroke="#facc15" stroke-width="2.5"/>

                        <line x1="30" y1="130" x2="200" y2="120" stroke="#fef08a" stroke-width="2"/>
                        <line x1="200" y1="120" x2="232" y2="115" stroke="#fde047" stroke-width="2"/>
                        <line x1="232" y1="115" x2="365" y2="105" stroke="#facc15" stroke-width="2.5"/>
                    </g>
                    <!-- Inverted Real Image on Retina -->
                    <polygon points="365,100 365,110 361,105" fill="#10b981"/>
                </svg>
                <div id="sim1-desc" class="text-xs text-indigo-200 mt-2 text-center font-medium">
                    Normal Ambient Light: Cornea performs ~70% of refraction, pupil aperture is medium, lens focuses sharp inverted image onto retina.
                </div>
            </div>
        </div>
        """
    elif s_idx == 1:
        # Slide 2: Power of Accommodation (Thin vs Thick lens)
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 10.2: Ciliary Muscle & Accommodation Engine
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300 font-semibold">Object Distance:</label>
                    <input type="range" id="sim2-dist" min="25" max="300" value="300" oninput="updateSim2Accommodation(this.value)" class="w-28 sm:w-36 accent-cyan-400 cursor-pointer">
                    <span id="sim2-dist-val" class="text-xs font-mono font-bold text-cyan-400">Distant (Infinity)</span>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim2" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Eyeball Reference -->
                    <path d="M 260 30 A 80 80 0 1 1 260 170" fill="none" stroke="#334155" stroke-width="2"/>
                    <path d="M 330 45 A 75 75 0 0 1 330 155" fill="none" stroke="#f43f5e" stroke-width="4"/>
                    <text x="345" y="105" fill="#f43f5e" font-size="9" font-weight="bold">Retina</text>

                    <!-- Ciliary Muscles -->
                    <circle id="sim2-ciliary-top" cx="240" cy="45" r="10" fill="#0ea5e9"/>
                    <circle id="sim2-ciliary-bot" cx="240" cy="155" r="10" fill="#0ea5e9"/>
                    <text x="240" y="30" fill="#38bdf8" font-size="8" text-anchor="middle">Ciliary Muscle</text>

                    <!-- Eye Lens (Dynamic thickness) -->
                    <path id="sim2-lens" d="M 240 55 Q 247 100 240 145 Q 233 100 240 55 Z" fill="#38bdf8" fill-opacity="0.6" stroke="#bae6fd" stroke-width="2"/>

                    <!-- Object Indicator -->
                    <g id="sim2-object-group">
                        <line id="sim2-obj-line" x1="40" y1="100" x2="40" y2="65" stroke="#10b981" stroke-width="3"/>
                        <polygon id="sim2-obj-arrow" points="40,60 36,70 44,70" fill="#10b981"/>
                        <text id="sim2-obj-text" x="40" y="52" fill="#10b981" font-size="9" text-anchor="middle" font-weight="bold">Object</text>
                    </g>

                    <!-- Rays to Lens and Retina -->
                    <g id="sim2-rays">
                        <line id="sim2-ray-top" x1="40" y1="65" x2="240" y2="75" stroke="#fef08a" stroke-width="1.8"/>
                        <line id="sim2-ray-bot" x1="40" y1="65" x2="240" y2="125" stroke="#fef08a" stroke-width="1.8"/>
                        <line x1="240" y1="75" x2="335" y2="105" stroke="#facc15" stroke-width="2"/>
                        <line x1="240" y1="125" x2="335" y2="105" stroke="#facc15" stroke-width="2"/>
                    </g>
                    <!-- Sharp Focus Spot -->
                    <circle cx="335" cy="105" r="3.5" fill="#10b981"/>
                </svg>
                <div id="sim2-status" class="text-xs text-cyan-200 mt-2 text-center font-medium">
                    Distant Object: Ciliary muscles relaxed → Lens is thin → Focal length maximum (~2.27 cm) → Clear sharp focus on retina.
                </div>
            </div>
        </div>
        """
    elif s_idx == 2:
        # Slide 3: Myopia & Concave Lens Correction
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 10.3: Myopic Eye & Concave Lens Fix
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim3Mode('defective')" id="btn-sim3-defect" class="px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition">Uncorrected Myopia</button>
                    <button onclick="setSim3Mode('corrected')" id="btn-sim3-correct" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Add Concave Lens</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim3" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Elongated Eyeball -->
                    <ellipse cx="320" cy="100" rx="90" ry="75" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
                    <!-- Retina Layer -->
                    <path d="M 390 45 A 85 85 0 0 1 390 155" fill="none" stroke="#f43f5e" stroke-width="4"/>
                    <text x="400" y="105" fill="#f43f5e" font-size="9" font-weight="bold">Retina</text>

                    <!-- Eye Lens -->
                    <ellipse cx="250" cy="100" rx="10" ry="42" fill="#818cf8" fill-opacity="0.6" stroke="#c7d2fe" stroke-width="2"/>
                    <text x="250" y="45" fill="#a5b4fc" font-size="8" text-anchor="middle">Eye Lens</text>

                    <!-- Corrective Concave Spectacle Lens (Hidden in defective mode) -->
                    <g id="sim3-spectacle" class="hidden">
                        <path d="M 160 55 Q 168 100 160 145 L 168 145 Q 160 100 168 55 Z" fill="#38bdf8" fill-opacity="0.5" stroke="#38bdf8" stroke-width="2"/>
                        <text x="164" y="45" fill="#38bdf8" font-size="8" text-anchor="middle" font-weight="bold">Concave Lens</text>
                    </g>

                    <!-- Parallel Incoming Rays from Infinity -->
                    <line x1="20" y1="75" x2="160" y2="75" stroke="#fef08a" stroke-width="2"/>
                    <line x1="20" y1="125" x2="160" y2="125" stroke="#fef08a" stroke-width="2"/>

                    <!-- Dynamic Path inside/past lens -->
                    <g id="sim3-rays-group">
                        <!-- Defective: Focuses at 330 (in front of retina at 390) -->
                        <line x1="160" y1="75" x2="250" y2="75" stroke="#fef08a" stroke-width="2"/>
                        <line x1="160" y1="125" x2="250" y2="125" stroke="#fef08a" stroke-width="2"/>
                        <line x1="250" y1="75" x2="330" y2="100" stroke="#f43f5e" stroke-width="2.2"/>
                        <line x1="250" y1="125" x2="330" y2="100" stroke="#f43f5e" stroke-width="2.2"/>
                        <!-- Diverges to retina creating blur -->
                        <line x1="330" y1="100" x2="390" y2="85" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <line x1="330" y1="100" x2="390" y2="115" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <circle cx="330" cy="100" r="4" fill="#f43f5e"/>
                        <text x="330" y="85" fill="#f43f5e" font-size="8" text-anchor="middle" font-weight="bold">Focus in Front</text>
                    </g>
                </svg>
                <div id="sim3-desc" class="text-xs text-rose-200 mt-2 text-center font-medium">
                    Uncorrected Myopic Eye: Parallel starlight converges IN FRONT of retina (at ~330px) → Distant objects appear blurred.
                </div>
            </div>
        </div>
        """
    elif s_idx == 3:
        # Slide 4: Hypermetropia & Convex Lens Correction
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 10.4: Hypermetropic Eye & Convex Converging Fix
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim4Mode('defective')" id="btn-sim4-defect" class="px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition">Uncorrected Hypermetropia</button>
                    <button onclick="setSim4Mode('corrected')" id="btn-sim4-correct" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Add Convex Lens</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim4" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Compressed Eyeball -->
                    <ellipse cx="300" cy="100" rx="75" ry="75" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
                    <!-- Retina Layer -->
                    <path d="M 365 45 A 75 75 0 0 1 365 155" fill="none" stroke="#f43f5e" stroke-width="4"/>
                    <text x="375" y="105" fill="#f43f5e" font-size="9" font-weight="bold">Retina</text>

                    <!-- Eye Lens -->
                    <ellipse cx="245" cy="100" rx="8" ry="40" fill="#818cf8" fill-opacity="0.6" stroke="#c7d2fe" stroke-width="2"/>
                    <text x="245" y="45" fill="#a5b4fc" font-size="8" text-anchor="middle">Eye Lens</text>

                    <!-- Corrective Convex Spectacle Lens (Hidden initially) -->
                    <g id="sim4-spectacle" class="hidden">
                        <path d="M 165 55 Q 173 100 165 145 Q 157 100 165 55 Z" fill="#f59e0b" fill-opacity="0.5" stroke="#f59e0b" stroke-width="2"/>
                        <text x="165" y="45" fill="#f59e0b" font-size="8" text-anchor="middle" font-weight="bold">Convex Lens</text>
                    </g>

                    <!-- Nearby Object at 25 cm -->
                    <circle cx="50" cy="100" r="4.5" fill="#10b981"/>
                    <text x="50" y="120" fill="#10b981" font-size="8" text-anchor="middle" font-weight="bold">Object (25 cm)</text>

                    <g id="sim4-rays-group">
                        <!-- Defective: Divergent rays fail to converge in time, focal point behind retina at 420 -->
                        <line x1="50" y1="100" x2="245" y2="75" stroke="#fef08a" stroke-width="1.8"/>
                        <line x1="50" y1="100" x2="245" y2="125" stroke="#fef08a" stroke-width="1.8"/>
                        <line x1="245" y1="75" x2="365" y2="90" stroke="#f59e0b" stroke-width="2"/>
                        <line x1="245" y1="125" x2="365" y2="110" stroke="#f59e0b" stroke-width="2"/>
                        <line x1="365" y1="90" x2="425" y2="100" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <line x1="365" y1="110" x2="425" y2="100" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <circle cx="425" cy="100" r="4" fill="#f59e0b"/>
                        <text x="430" y="90" fill="#f59e0b" font-size="8" text-anchor="middle" font-weight="bold">Focus Behind Retina</text>
                    </g>
                </svg>
                <div id="sim4-desc" class="text-xs text-amber-200 mt-2 text-center font-medium">
                    Uncorrected Hypermetropic Eye: Light rays from near point (25 cm) focus BEHIND retina → Reading text appears blurred.
                </div>
            </div>
        </div>
        """
    elif s_idx == 4:
        # Slide 5: Presbyopia & Bi-Focal Lenses
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-purple-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-purple-400"></span>
                    Interactive Lab 10.5: Presbyopia & Dual Bi-Focal Lens Architecture
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim5Zone('upper')" id="btn-sim5-upper" class="px-2.5 py-1 rounded text-xs font-bold bg-purple-600 text-white transition">Upper Concave (Distant)</button>
                    <button onclick="setSim5Zone('lower')" id="btn-sim5-lower" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Lower Convex (Reading)</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim5" viewBox="0 0 500 210" class="w-full max-w-lg h-auto">
                    <!-- Eyeglass Frame -->
                    <rect x="180" y="20" width="140" height="170" rx="20" fill="#0f172a" stroke="#a855f7" stroke-width="4"/>
                    
                    <!-- Upper Concave Portion -->
                    <path id="sim5-upper-zone" d="M 184 24 L 316 24 L 316 110 L 184 110 Z" fill="#38bdf8" fill-opacity="0.25" class="transition-all duration-300"/>
                    <text x="250" y="65" fill="#38bdf8" font-size="10" text-anchor="middle" font-weight="bold">Upper Lens: Concave</text>
                    <text x="250" y="80" fill="#94a3b8" font-size="8" text-anchor="middle">Corrects Myopia • Distant Vision</text>

                    <!-- Dividing Line -->
                    <line x1="184" y1="110" x2="316" y2="110" stroke="#a855f7" stroke-width="2" stroke-dasharray="4,2"/>

                    <!-- Lower Convex Portion -->
                    <path id="sim5-lower-zone" d="M 184 110 L 316 110 L 316 186 L 184 186 Z" fill="#f59e0b" fill-opacity="0.15" class="transition-all duration-300"/>
                    <text x="250" y="145" fill="#f59e0b" font-size="10" text-anchor="middle" font-weight="bold">Lower Lens: Convex</text>
                    <text x="250" y="160" fill="#94a3b8" font-size="8" text-anchor="middle">Corrects Hypermetropia • Reading Vision</text>

                    <!-- Ray Demonstration Pointer -->
                    <g id="sim5-ray-overlay">
                        <line x1="50" y1="65" x2="180" y2="65" stroke="#fef08a" stroke-width="2"/>
                        <polygon points="180,65 170,60 170,70" fill="#fef08a"/>
                        <text x="110" y="55" fill="#fef08a" font-size="8" text-anchor="middle">Distant Light Rays</text>
                    </g>
                </svg>
                <div id="sim5-desc" class="text-xs text-purple-200 mt-2 text-center font-medium">
                    Upper Zone Selected: Diverging concave lens allows the ageing patient to view distant road signs and blackboards clearly.
                </div>
            </div>
        </div>
        """
    elif s_idx == 5:
        # Slide 6: Lens Power Calculator & Eye Donation Criteria
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <!-- Optical Power Calculator -->
                <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800">
                    <div class="text-xs font-bold uppercase tracking-wider text-emerald-400 mb-2 flex items-center gap-1.5">
                        <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                        Ophthalmic Power Solver: P = 1 / f
                    </div>
                    <div class="space-y-3">
                        <div>
                            <label class="text-xs text-slate-300 font-semibold block mb-1">Defect Type:</label>
                            <select id="sim6-defect-type" onchange="calcSim6()" class="w-full bg-slate-900 border border-slate-700 text-xs rounded-lg p-2 text-white">
                                <option value="myopia">Myopia (Far Point Defect)</option>
                                <option value="hyper">Hypermetropia (Near Point Defect)</option>
                            </select>
                        </div>
                        <div>
                            <label class="text-xs text-slate-300 font-semibold block mb-1">Defective Distance (meters):</label>
                            <input type="number" id="sim6-dist" value="1.2" step="0.1" min="0.2" max="10" oninput="calcSim6()" class="w-full bg-slate-900 border border-slate-700 text-xs rounded-lg p-2 text-white">
                        </div>
                        <div class="p-3 bg-slate-900/80 rounded-lg border border-slate-800 text-xs space-y-1">
                            <div class="flex justify-between text-slate-400"><span>Required Focal Length (f):</span><span id="sim6-f-val" class="font-mono font-bold text-white">-1.20 m</span></div>
                            <div class="flex justify-between text-slate-400"><span>Prescribed Power (P):</span><span id="sim6-p-val" class="font-mono font-bold text-emerald-400 text-sm">-0.83 D</span></div>
                            <div class="flex justify-between text-slate-400"><span>Prescribed Lens:</span><span id="sim6-lens-val" class="font-bold text-rose-400">Concave Lens</span></div>
                        </div>
                    </div>
                </div>

                <!-- Eye Donation Checklist -->
                <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800">
                    <div class="text-xs font-bold uppercase tracking-wider text-rose-400 mb-2 flex items-center gap-1.5">
                        <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                        Eye Donation Eligibility Protocol
                    </div>
                    <ul class="text-xs space-y-2 text-slate-300">
                        <li class="flex items-start gap-2">
                            <span class="text-emerald-400 font-bold">✓</span>
                            <span><strong>Any Age / Sex:</strong> Spectacle wearers, cataract-operated individuals, diabetics, and asthma patients CAN donate.</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-amber-400 font-bold">⏱</span>
                            <span><strong>Critical Window:</strong> Eyes must be removed within <strong>4–6 hours</strong> after death. The procedure takes only 10–15 minutes without any disfigurement.</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-rose-400 font-bold">✕</span>
                            <span><strong>Contraindications:</strong> AIDS, Hepatitis B/C, Rabies, Tetanus, Cholera, Leukaemia, Encephalitis.</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-cyan-400 font-bold">★</span>
                            <span><strong>Noble Impact:</strong> One pair of donated eyes restores sight to up to <strong>4 corneal blind patients</strong>!</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        """
    elif s_idx == 6:
        # Slide 7: Refraction through Triangular Glass Prism (Activity 10.1)
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 10.7: Triangular Prism Goniometer & Deviation Angle
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300 font-semibold">Incident Angle (∠i):</label>
                    <input type="range" id="sim7-angle" min="30" max="65" value="48" oninput="updateSim7Prism(this.value)" class="w-28 sm:w-36 accent-amber-400 cursor-pointer">
                    <span id="sim7-angle-val" class="text-xs font-mono font-bold text-amber-400">48°</span>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim7" viewBox="0 0 500 230" class="w-full max-w-lg h-auto">
                    <!-- Triangular Prism ABC (Apex at top) -->
                    <polygon points="250,30 140,190 360,190" fill="#38bdf8" fill-opacity="0.18" stroke="#38bdf8" stroke-width="2.5"/>
                    <text x="250" y="24" fill="#38bdf8" font-size="10" text-anchor="middle" font-weight="bold">Apex A (∠A = 60°)</text>
                    <text x="130" y="205" fill="#94a3b8" font-size="9">B</text>
                    <text x="365" y="205" fill="#94a3b8" font-size="9">C</text>

                    <!-- Normal at surface AB -->
                    <line x1="130" y1="75" x2="235" y2="145" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4,4"/>
                    <text x="125" y="70" fill="#94a3b8" font-size="8">N</text>

                    <!-- Normal at surface AC -->
                    <line x1="370" y1="75" x2="265" y2="145" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4,4"/>
                    <text x="375" y="70" fill="#94a3b8" font-size="8">M</text>

                    <!-- Incident, Refracted, Emergent Rays -->
                    <g id="sim7-ray-path">
                        <!-- Incident PE -->
                        <line id="sim7-ray-pe" x1="60" y1="165" x2="185" y2="110" stroke="#fef08a" stroke-width="2.5"/>
                        <circle cx="100" cy="147" r="3" fill="#ef4444"/><text x="100" y="160" fill="#ef4444" font-size="7">P</text>
                        <circle cx="140" cy="129" r="3" fill="#ef4444"/><text x="140" y="142" fill="#ef4444" font-size="7">Q</text>
                        <!-- Refracted EF -->
                        <line id="sim7-ray-ef" x1="185" y1="110" x2="315" y2="110" stroke="#facc15" stroke-width="2.5"/>
                        <!-- Emergent FS -->
                        <line id="sim7-ray-fs" x1="315" y1="110" x2="440" y2="165" stroke="#f59e0b" stroke-width="2.5"/>
                        <circle cx="360" cy="130" r="3" fill="#10b981"/><text x="360" y="142" fill="#10b981" font-size="7">R</text>
                        <circle cx="400" cy="147" r="3" fill="#10b981"/><text x="400" y="160" fill="#10b981" font-size="7">S</text>

                        <!-- Dotted extensions meeting at G to form Angle of Deviation D -->
                        <line x1="185" y1="110" x2="310" y2="55" stroke="#fde047" stroke-width="1.2" stroke-dasharray="3,3"/>
                        <line x1="315" y1="110" x2="250" y2="82" stroke="#f59e0b" stroke-width="1.2" stroke-dasharray="3,3"/>
                    </g>
                    <!-- Deviation Angle Label -->
                    <circle cx="280" cy="70" r="3" fill="#ec4899"/>
                    <text x="280" y="62" fill="#f43f5e" font-size="8" text-anchor="middle" font-weight="bold">∠D</text>
                </svg>
                <div class="flex justify-between w-full max-w-lg mt-2 text-xs font-mono px-2 text-slate-300">
                    <div>∠i: <span id="sim7-i-val" class="text-amber-400 font-bold">48°</span></div>
                    <div>∠r: <span id="sim7-r-val" class="text-yellow-400 font-bold">29°</span></div>
                    <div>∠e: <span id="sim7-e-val" class="text-orange-400 font-bold">48°</span></div>
                    <div>∠D (Deviation): <span id="sim7-d-val" class="text-rose-400 font-bold">36°</span></div>
                </div>
            </div>
        </div>
        """
    elif s_idx == 7:
        # Slide 8: Dispersion of White Light & VIBGYOR Spectrum
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 10.8: Dispersion & The VIBGYOR Rainbow Spectrum
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim8Highlight('all')" id="btn-sim8-all" class="px-2 py-1 rounded text-xs font-bold bg-cyan-600 text-white">Full VIBGYOR</button>
                    <button onclick="setSim8Highlight('red')" id="btn-sim8-red" class="px-2 py-1 rounded text-xs font-bold bg-slate-800 text-rose-400 hover:bg-slate-700">Red (Least Bent)</button>
                    <button onclick="setSim8Highlight('violet')" id="btn-sim8-violet" class="px-2 py-1 rounded text-xs font-bold bg-slate-800 text-purple-400 hover:bg-slate-700">Violet (Most Bent)</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim8" viewBox="0 0 500 220" class="w-full max-w-lg h-auto">
                    <!-- Incident Narrow Slit White Beam -->
                    <rect x="20" y="90" width="10" height="40" fill="#64748b"/>
                    <rect x="20" y="108" width="10" height="4" fill="#0f172a"/>
                    <text x="25" y="82" fill="#94a3b8" font-size="8" text-anchor="middle">Slit</text>
                    <line x1="30" y1="110" x2="160" y2="110" stroke="#ffffff" stroke-width="3"/>
                    <text x="80" y="102" fill="#ffffff" font-size="9" font-weight="bold">White Light</text>

                    <!-- Prism -->
                    <polygon points="230,30 130,190 330,190" fill="#38bdf8" fill-opacity="0.15" stroke="#38bdf8" stroke-width="2.5"/>

                    <!-- Dispersed Rays Fan Out to Screen -->
                    <g id="sim8-spectrum">
                        <!-- Red (Bends least) -->
                        <line x1="160" y1="110" x2="210" y2="114" stroke="#ef4444" stroke-width="2"/>
                        <line x1="210" y1="114" x2="430" y2="125" stroke="#ef4444" stroke-width="2.2"/>
                        <!-- Orange -->
                        <line x1="160" y1="110" x2="210" y2="116" stroke="#f97316" stroke-width="2"/>
                        <line x1="210" y1="116" x2="430" y2="135" stroke="#f97316" stroke-width="2.2"/>
                        <!-- Yellow -->
                        <line x1="160" y1="110" x2="210" y2="118" stroke="#eab308" stroke-width="2"/>
                        <line x1="210" y1="118" x2="430" y2="145" stroke="#eab308" stroke-width="2.2"/>
                        <!-- Green -->
                        <line x1="160" y1="110" x2="210" y2="120" stroke="#22c55e" stroke-width="2"/>
                        <line x1="210" y1="120" x2="430" y2="155" stroke="#22c55e" stroke-width="2.2"/>
                        <!-- Blue -->
                        <line x1="160" y1="110" x2="210" y2="122" stroke="#06b6d4" stroke-width="2"/>
                        <line x1="210" y1="122" x2="430" y2="165" stroke="#06b6d4" stroke-width="2.2"/>
                        <!-- Indigo -->
                        <line x1="160" y1="110" x2="210" y2="124" stroke="#6366f1" stroke-width="2"/>
                        <line x1="210" y1="124" x2="430" y2="175" stroke="#6366f1" stroke-width="2.2"/>
                        <!-- Violet (Bends most) -->
                        <line x1="160" y1="110" x2="210" y2="126" stroke="#a855f7" stroke-width="2"/>
                        <line x1="210" y1="126" x2="430" y2="185" stroke="#a855f7" stroke-width="2.2"/>
                    </g>

                    <!-- White Screen on Right -->
                    <line x1="430" y1="90" x2="430" y2="210" stroke="#cbd5e1" stroke-width="5"/>
                    <text x="440" y="100" fill="#cbd5e1" font-size="8" font-weight="bold">Screen</text>
                    <text x="440" y="127" fill="#ef4444" font-size="8" font-weight="bold">R (Least bent)</text>
                    <text x="440" y="187" fill="#a855f7" font-size="8" font-weight="bold">V (Most bent)</text>
                </svg>
                <div id="sim8-desc" class="text-xs text-cyan-200 mt-2 text-center font-medium">
                    Dispersion: White light splits because each wavelength travels at a different velocity in glass ($v = c/n$). Red bends least; violet bends most.
                </div>
            </div>
        </div>
        """
    elif s_idx == 8:
        # Slide 9: Newton's Recombination Experiment
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                    Interactive Lab 10.9: Sir Isaac Newton's Recombination Experiment
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim9Mode('split')" id="btn-sim9-split" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Prism 1 Alone</button>
                    <button onclick="setSim9Mode('recombine')" id="btn-sim9-rec" class="px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition">Add Inverted Prism 2</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim9" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Incident White Beam -->
                    <line x1="20" y1="100" x2="110" y2="100" stroke="#ffffff" stroke-width="3"/>
                    <text x="50" y="90" fill="#ffffff" font-size="8" font-weight="bold">White Light</text>

                    <!-- Prism 1 (Upright) -->
                    <polygon points="170,30 100,170 240,170" fill="#38bdf8" fill-opacity="0.18" stroke="#38bdf8" stroke-width="2"/>
                    <text x="170" y="24" fill="#38bdf8" font-size="8" text-anchor="middle">Prism P1 (Apex Up)</text>

                    <!-- Spectrum Rays between Prism 1 & 2 -->
                    <line x1="120" y1="100" x2="270" y2="85" stroke="#ef4444" stroke-width="2"/>
                    <line x1="120" y1="100" x2="270" y2="115" stroke="#a855f7" stroke-width="2"/>
                    <text x="200" y="78" fill="#ef4444" font-size="8">Red</text>
                    <text x="200" y="125" fill="#a855f7" font-size="8">Violet</text>

                    <!-- Prism 2 (Inverted) -->
                    <g id="sim9-prism2">
                        <polygon points="310,170 240,30 380,30" fill="#10b981" fill-opacity="0.18" stroke="#10b981" stroke-width="2"/>
                        <text x="310" y="185" fill="#10b981" font-size="8" text-anchor="middle">Prism P2 (Inverted)</text>

                        <!-- Recombined White Beam -->
                        <line x1="335" y1="100" x2="450" y2="100" stroke="#ffffff" stroke-width="3.5" filter="drop-shadow(0 0 6px #ffffff)"/>
                        <text x="390" y="90" fill="#ffffff" font-size="9" font-weight="bold">Recombined White Light</text>
                    </g>
                    <!-- Screen -->
                    <line x1="450" y1="50" x2="450" y2="150" stroke="#cbd5e1" stroke-width="4"/>
                </svg>
                <div id="sim9-desc" class="text-xs text-emerald-200 mt-2 text-center font-medium">
                    Newton's Discovery: The second inverted prism reverses the dispersion of the first, recombining all 7 colors back into a single white beam.
                </div>
            </div>
        </div>
        """
    elif s_idx == 9:
        # Slide 10: Rainbow Formation inside Raindrop
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-rose-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                    Interactive Lab 10.10: Atmospheric Raindrop Internal Reflection
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="pulseSim10Drop()" class="px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white hover:bg-rose-500 transition">Trace Sunlight Ray</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim10" viewBox="0 0 500 220" class="w-full max-w-lg h-auto">
                    <!-- Spherical Raindrop -->
                    <circle cx="280" cy="95" r="75" fill="#0284c7" fill-opacity="0.15" stroke="#38bdf8" stroke-width="2.5"/>
                    <text x="280" y="95" fill="#38bdf8" font-size="9" text-anchor="middle" font-weight="bold">Spherical Raindrop</text>

                    <!-- Incident Sunlight -->
                    <line x1="40" y1="45" x2="225" y2="45" stroke="#ffffff" stroke-width="3"/>
                    <text x="90" y="38" fill="#ffffff" font-size="9" font-weight="bold">Sunlight (From Behind Observer)</text>

                    <!-- Point 1: Refraction + Dispersion -->
                    <circle cx="225" cy="45" r="3.5" fill="#fbbf24"/>
                    <text x="200" y="30" fill="#fbbf24" font-size="7" font-weight="bold">1. Refraction & Dispersion</text>

                    <!-- Inside Raindrop: Red and Violet paths -->
                    <line x1="225" y1="45" x2="352" y2="85" stroke="#ef4444" stroke-width="2"/>
                    <line x1="225" y1="45" x2="348" y2="105" stroke="#a855f7" stroke-width="2"/>

                    <!-- Point 2: Total Internal Reflection -->
                    <circle cx="352" cy="85" r="3.5" fill="#ef4444"/>
                    <circle cx="348" cy="105" r="3.5" fill="#a855f7"/>
                    <text x="365" y="98" fill="#fbbf24" font-size="7" font-weight="bold">2. Internal Reflection</text>

                    <!-- Reflected paths to lower left surface -->
                    <line x1="352" y1="85" x2="245" y2="155" stroke="#ef4444" stroke-width="2"/>
                    <line x1="348" y1="105" x2="235" y2="148" stroke="#a855f7" stroke-width="2"/>

                    <!-- Point 3: Refraction Out to Observer Eye -->
                    <circle cx="245" cy="155" r="3" fill="#ef4444"/>
                    <circle cx="235" cy="148" r="3" fill="#a855f7"/>

                    <!-- Emergent rays into eye -->
                    <line x1="245" y1="155" x2="70" y2="195" stroke="#ef4444" stroke-width="2.5"/>
                    <line x1="235" y1="148" x2="70" y2="210" stroke="#a855f7" stroke-width="2.5"/>
                    <text x="120" y="185" fill="#ef4444" font-size="8" font-weight="bold">Red Ray (42°)</text>
                    <text x="120" y="215" fill="#a855f7" font-size="8" font-weight="bold">Violet Ray (40°)</text>

                    <!-- Observer Eye -->
                    <circle cx="55" cy="202" r="8" fill="#475569"/>
                    <circle cx="55" cy="202" r="3" fill="#38bdf8"/>
                    <text x="55" y="218" fill="#cbd5e1" font-size="7" text-anchor="middle">Observer</text>
                </svg>
                <div id="sim10-desc" class="text-xs text-rose-200 mt-2 text-center font-medium">
                    Triple Process: Refraction & dispersion at entry → Internal reflection at back wall → Final refraction at exit (42° Red on top, 40° Violet below).
                </div>
            </div>
        </div>
        """
    elif s_idx == 10:
        # Slide 11: Atmospheric Refraction & Star Twinkling
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                    Interactive Lab 10.11: Starlight Twinkling & Apparent Position Shift
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300 font-semibold">Thermal Convection:</label>
                    <button onclick="toggleSim11Turbulence()" id="btn-sim11-turb" class="px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition">Turbulence Active</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim11" viewBox="0 0 500 220" class="w-full max-w-lg h-auto">
                    <!-- Vacuum Space (Top) -->
                    <text x="40" y="30" fill="#94a3b8" font-size="8" font-weight="bold">Space (Vacuum, n = 1.0)</text>

                    <!-- Actual Star -->
                    <g id="sim11-star-real">
                        <polygon points="400,25 403,32 410,32 405,37 407,44 400,40 393,44 395,37 390,32 397,32" fill="#facc15"/>
                        <text x="400" y="16" fill="#facc15" font-size="8" text-anchor="middle" font-weight="bold">Actual Star Position</text>
                    </g>

                    <!-- Apparent Star (Higher) -->
                    <g id="sim11-star-apparent">
                        <polygon points="435,50 438,57 445,57 440,62 442,69 435,65 428,69 430,62 425,57 432,57" fill="#38bdf8"/>
                        <text x="435" y="42" fill="#38bdf8" font-size="8" text-anchor="middle" font-weight="bold">Apparent Position (Higher)</text>
                    </g>

                    <!-- Atmospheric Layers (Refractive Index Increasing Downward) -->
                    <line x1="20" y1="70" x2="480" y2="70" stroke="#334155" stroke-dasharray="3,3"/>
                    <text x="30" y="82" fill="#64748b" font-size="7">Upper Atmosphere (Lower Density, n ≈ 1.0001)</text>

                    <line x1="20" y1="120" x2="480" y2="120" stroke="#334155" stroke-dasharray="3,3"/>
                    <text x="30" y="132" fill="#64748b" font-size="7">Middle Atmosphere</text>

                    <line x1="20" y1="170" x2="480" y2="170" stroke="#334155" stroke-dasharray="3,3"/>
                    <text x="30" y="182" fill="#64748b" font-size="7">Lower Atmosphere (Higher Density, n ≈ 1.0003)</text>

                    <!-- Curved Refracted Starlight Ray -->
                    <path id="sim11-ray" d="M 400 35 Q 360 100 120 195" fill="none" stroke="#fef08a" stroke-width="2.5"/>
                    <!-- Apparent Straight Line Sightline -->
                    <line x1="120" y1="195" x2="435" y2="60" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="3,3"/>

                    <!-- Observer on Ground -->
                    <circle cx="110" cy="195" r="7" fill="#475569"/>
                    <text x="110" y="212" fill="#cbd5e1" font-size="8" text-anchor="middle">Observer</text>
                </svg>
                <div id="sim11-desc" class="text-xs text-amber-200 mt-2 text-center font-medium">
                    Continuous Atmospheric Bending: Gradual increase in optical density bends starlight toward normal → Star appears higher and point-light flickers with atmospheric thermal swirls.
                </div>
            </div>
        </div>
        """
    elif s_idx == 11:
        # Slide 12: Why Planets Don't Twinkle & Early Sunrise / Delayed Sunset
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                    Interactive Lab 10.12: Advanced Sunrise & Solar Horizon Physics
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim12Mode('sunrise')" id="btn-sim12-sun" class="px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 text-white transition">Advance Sunrise (2 min)</button>
                    <button onclick="setSim12Mode('planets')" id="btn-sim12-planet" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">Planets vs Stars</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim12" viewBox="0 0 500 220" class="w-full max-w-lg h-auto">
                    <!-- Earth Section -->
                    <circle cx="150" cy="220" r="100" fill="#0f766e" stroke="#14b8a6" stroke-width="2"/>
                    <text x="150" y="195" fill="#ccfbf1" font-size="9" text-anchor="middle" font-weight="bold">Earth</text>
                    
                    <!-- Atmosphere Blanket -->
                    <circle cx="150" cy="220" r="125" fill="#38bdf8" fill-opacity="0.15" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,2"/>
                    <text x="60" y="125" fill="#38bdf8" font-size="8">Atmosphere</text>

                    <!-- Horizon Line of Observer at (150, 120) -->
                    <line x1="30" y1="120" x2="480" y2="120" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="4,3"/>
                    <text x="440" y="112" fill="#f43f5e" font-size="8" font-weight="bold">Observer Horizon</text>

                    <!-- Actual Sun Below Horizon -->
                    <g id="sim12-actual-sun">
                        <circle cx="440" cy="155" r="18" fill="#ea580c"/>
                        <text x="440" y="185" fill="#ea580c" font-size="8" text-anchor="middle" font-weight="bold">Actual Sun (Below)</text>
                    </g>

                    <!-- Apparent Sun Above Horizon -->
                    <g id="sim12-apparent-sun">
                        <ellipse cx="440" cy="95" rx="19" ry="14" fill="#facc15" filter="drop-shadow(0 0 6px #f59e0b)"/>
                        <text x="440" y="70" fill="#facc15" font-size="8" text-anchor="middle" font-weight="bold">Apparent Sun (Visible!)</text>
                    </g>

                    <!-- Curved ray from below horizon into eye -->
                    <path d="M 440 155 Q 260 125 150 120" fill="none" stroke="#fbbf24" stroke-width="2.5"/>
                    <line x1="150" y1="120" x2="440" y2="95" stroke="#facc15" stroke-width="1.2" stroke-dasharray="3,3"/>

                    <!-- Observer -->
                    <circle cx="150" cy="120" r="5" fill="#cbd5e1"/>
                </svg>
                <div id="sim12-desc" class="text-xs text-cyan-200 mt-2 text-center font-medium">
                    2 Minutes Early: Rays from the Sun below the horizon bend through atmospheric layers into observer's eyes, making sunrise appear 2 minutes earlier and sunset 2 minutes later!
                </div>
            </div>
        </div>
        """
    elif s_idx == 12:
        # Slide 13: Tyndall Effect & Colloidal Scattering
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                    Interactive Lab 10.13: Tyndall Effect Comparator
                </span>
                <div class="flex items-center gap-2">
                    <button onclick="setSim13Beam('both')" class="px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white">Compare Both Solutions</button>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim13" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Laser Light Source -->
                    <rect x="20" y="85" width="40" height="30" rx="4" fill="#334155"/>
                    <circle cx="60" cy="100" r="5" fill="#ef4444"/>
                    <text x="35" y="80" fill="#94a3b8" font-size="8">Torch / Laser</text>

                    <!-- Beaker 1: True Solution (Sugar / Salt Water) -->
                    <rect x="130" y="50" width="110" height="110" rx="8" fill="#38bdf8" fill-opacity="0.1" stroke="#38bdf8" stroke-width="2"/>
                    <text x="185" y="42" fill="#38bdf8" font-size="9" text-anchor="middle" font-weight="bold">True Solution</text>
                    <text x="185" y="175" fill="#64748b" font-size="7" text-anchor="middle">Molecular Size (< 1 nm)</text>
                    <text x="185" y="105" fill="#64748b" font-size="8" text-anchor="middle">Path Invisible (No Scattering)</text>

                    <!-- Beaker 2: Colloidal Solution (Milk / Smoke / Starch) -->
                    <rect x="310" y="50" width="110" height="110" rx="8" fill="#a855f7" fill-opacity="0.15" stroke="#a855f7" stroke-width="2"/>
                    <text x="365" y="42" fill="#a855f7" font-size="9" text-anchor="middle" font-weight="bold">Colloidal Solution</text>
                    <text x="365" y="175" fill="#cbd5e1" font-size="7" text-anchor="middle">Colloidal Size (1 - 1000 nm)</text>
                    
                    <!-- Luminous Beam Visible in Colloid! -->
                    <polygon points="310,95 420,90 420,110 310,105" fill="#facc15" fill-opacity="0.6" filter="drop-shadow(0 0 6px #facc15)"/>
                    <text x="365" y="104" fill="#0f172a" font-size="8" text-anchor="middle" font-weight="bold">Tyndall Cone Visible!</text>

                    <!-- Light Ray Lines -->
                    <line x1="60" y1="100" x2="130" y2="100" stroke="#facc15" stroke-width="3"/>
                    <line x1="240" y1="100" x2="310" y2="100" stroke="#facc15" stroke-width="3"/>
                    <line x1="420" y1="100" x2="480" y2="100" stroke="#facc15" stroke-width="3"/>
                </svg>
                <div id="sim13-desc" class="text-xs text-emerald-200 mt-2 text-center font-medium">
                    Tyndall Effect: Colloidal particles are sufficiently large to diffusely scatter photons, illuminating the beam path. In true solutions, molecules are too tiny to scatter.
                </div>
            </div>
        </div>
        """
    elif s_idx == 13:
        # Slide 14: Why Sky is Blue & Red Danger Signals (Rayleigh Law)
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-sky-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-sky-400"></span>
                    Interactive Lab 10.14: Rayleigh's Law Simulator: I ∝ 1/λ⁴
                </span>
                <div class="flex items-center gap-3">
                    <label class="text-xs text-slate-300 font-semibold">Wavelength (λ):</label>
                    <input type="range" id="sim14-wl" min="400" max="700" value="450" step="10" oninput="updateSim14Rayleigh(this.value)" class="w-28 sm:w-36 accent-sky-400 cursor-pointer">
                    <span id="sim14-wl-val" class="text-xs font-mono font-bold text-sky-400">450 nm (Blue)</span>
                </div>
            </div>
            <div class="relative bg-slate-950 rounded-xl p-3 border border-slate-800 flex flex-col items-center justify-center">
                <svg id="svg-sim14" viewBox="0 0 500 200" class="w-full max-w-lg h-auto">
                    <!-- Sky Dome -->
                    <path id="sim14-dome" d="M 50 180 A 200 130 0 0 1 450 180 Z" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
                    <text x="250" y="70" fill="#38bdf8" font-size="11" text-anchor="middle" font-weight="bold">Atmospheric Scattering Vault</text>

                    <!-- Atmosphere Gas Molecules (Nitrogen, Oxygen) -->
                    <circle cx="160" cy="110" r="5" fill="#94a3b8"/><text x="160" y="125" fill="#94a3b8" font-size="7" text-anchor="middle">N₂</text>
                    <circle cx="250" cy="95" r="5" fill="#94a3b8"/><text x="250" y="110" fill="#94a3b8" font-size="7" text-anchor="middle">O₂</text>
                    <circle cx="340" cy="110" r="5" fill="#94a3b8"/><text x="340" y="125" fill="#94a3b8" font-size="7" text-anchor="middle">N₂</text>

                    <!-- Scattering Rays (Dynamic) -->
                    <g id="sim14-scattering-arcs">
                        <line x1="250" y1="95" x2="210" y2="60" stroke="#38bdf8" stroke-width="2.5"/>
                        <line x1="250" y1="95" x2="290" y2="60" stroke="#38bdf8" stroke-width="2.5"/>
                        <line x1="250" y1="95" x2="200" y2="120" stroke="#38bdf8" stroke-width="2.5"/>
                        <line x1="250" y1="95" x2="300" y2="120" stroke="#38bdf8" stroke-width="2.5"/>
                    </g>
                </svg>
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 w-full max-w-lg mt-2 text-xs font-mono p-2 bg-slate-900 rounded-lg text-center">
                    <div>Wavelength: <span id="sim14-lambda" class="text-white font-bold">450 nm</span></div>
                    <div>Relative 1/λ⁴: <span id="sim14-rel" class="text-sky-400 font-bold">5.85x</span></div>
                    <div>Scattering: <span id="sim14-level" class="text-cyan-300 font-bold">Extremely High</span></div>
                    <div>Application: <span id="sim14-app" class="text-emerald-400 font-bold">Blue Daylight Sky</span></div>
                </div>
            </div>
        </div>
        """
    elif s_idx == 14:
        # Slide 15: Master Optical Comparison Matrix
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="text-xs font-bold uppercase tracking-wider text-rose-400 mb-3 flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-rose-400"></span>
                Interactive Lab 10.15: NCERT Optical Phenomena Explorer
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-5 gap-2 mb-3">
                <button onclick="setSim15Card('rainbow')" id="btn-sim15-rainbow" class="p-2 rounded-lg text-xs font-bold bg-rose-600 text-white transition text-center">Rainbow</button>
                <button onclick="setSim15Card('twinkle')" id="btn-sim15-twinkle" class="p-2 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition text-center">Twinkling</button>
                <button onclick="setSim15Card('sunrise')" id="btn-sim15-sunrise" class="p-2 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition text-center">Advance Sunrise</button>
                <button onclick="setSim15Card('bluesky')" id="btn-sim15-bluesky" class="p-2 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition text-center">Blue Sky</button>
                <button onclick="setSim15Card('tyndall')" id="btn-sim15-tyndall" class="p-2 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition text-center">Tyndall Effect</button>
            </div>
            <div id="sim15-display" class="bg-slate-950 p-4 rounded-xl border border-slate-800 min-h-[140px] flex flex-col justify-center">
                <div class="text-sm font-bold text-rose-400 mb-1">Rainbow Formation</div>
                <div class="text-xs text-slate-300 space-y-1">
                    <p><strong>Primary Cause:</strong> Dispersion of sunlight by tiny suspended raindrops acting as microscopic triangular prisms.</p>
                    <p><strong>Three Optical Steps:</strong> (1) Refraction with dispersion at raindrop entry → (2) Total internal reflection at inner rear wall → (3) Refraction upon exiting droplet.</p>
                    <p><strong>Crucial Rule:</strong> Always observed in the sky direction <em>opposite to the Sun</em> with observer's back to sunlight (42° Red, 40° Violet).</p>
                </div>
            </div>
        </div>
        """
    elif s_idx == 15:
        # Slide 16: Complete NCERT Exercises Solutions (Q1–Q12)
        return """
        <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 sm:p-5 shadow-lg">
            <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-indigo-400 flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-indigo-400"></span>
                    NCERT Exercise Interactive Solver (Q1 to Q12)
                </span>
                <span class="text-xs text-slate-400 font-mono">12 / 12 Official Solutions</span>
            </div>
            <div class="grid grid-cols-3 sm:grid-cols-6 gap-2 mb-3">
                <button onclick="loadExerciseSol(1)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q1 (Lens Focus)</button>
                <button onclick="loadExerciseSol(2)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q2 (Retina Image)</button>
                <button onclick="loadExerciseSol(3)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q3 (Near Point 25cm)</button>
                <button onclick="loadExerciseSol(4)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q4 (Ciliary Action)</button>
                <button onclick="loadExerciseSol(5)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q5 (-5.5D / +1.5D)</button>
                <button onclick="loadExerciseSol(6)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q6 (Far Point 80cm)</button>
                <button onclick="loadExerciseSol(7)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q7 (Hyper Near 1m)</button>
                <button onclick="loadExerciseSol(8)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q8 (< 25 cm Strain)</button>
                <button onclick="loadExerciseSol(9)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q9 (Image Distance)</button>
                <button onclick="loadExerciseSol(10)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q10 (Star Twinkle)</button>
                <button onclick="loadExerciseSol(11)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q11 (No Planets)</button>
                <button onclick="loadExerciseSol(12)" class="px-2 py-1.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold">Q12 (Space Dark)</button>
            </div>
            <div id="exercise-sol-box" class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs sm:text-sm text-slate-300 min-h-[130px] leading-relaxed">
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
        <button onclick="goToSlide({idx})" id="pill-{idx}" class="px-3 py-1.5 rounded-lg text-xs font-medium whitespace-nowrap transition cursor-pointer {'bg-indigo-600 text-white font-bold' if idx == 0 else 'bg-slate-800 text-slate-300 hover:bg-slate-700'}">
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
                        <span class="w-2 h-2 rounded-full bg-indigo-500"></span>
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
                        <span class="text-xs font-bold text-indigo-400">Concept Checkpoint {c_idx+1}</span>
                        <span id="feedback-{s_idx}-{c_idx}" class="text-xs font-semibold"></span>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-200 font-medium mb-3">{cp['q']}</p>
                    <div class="space-y-2 mb-3">
                        {opts_html}
                    </div>
                    <div id="sol-{s_idx}-{c_idx}" class="hidden p-3 rounded-lg bg-indigo-950/30 border border-indigo-900/50 text-xs text-slate-300 leading-relaxed">
                        <strong class="text-indigo-400">Explanation:</strong> {cp['solution']}
                    </div>
                </div>
                """

            teacher_card_html = f"""
            <!-- Person Talking: Dr. Sophia Physics Master Avatar -->
            <div class="mb-6 p-4 rounded-2xl bg-gradient-to-r from-indigo-950/40 via-slate-900 to-sky-950/20 border border-indigo-500/30 flex flex-col sm:flex-row items-center sm:items-start gap-4 shadow-xl">
                <div class="relative shrink-0 flex flex-col items-center teacher-bob">
                    <svg viewBox="0 0 120 120" class="w-20 h-20 sm:w-24 sm:h-24 drop-shadow-lg">
                        <path d="M20 115 C20 85, 45 80, 60 80 C75 80, 100 85, 100 115 Z" fill="#4f46e5" stroke="#6366f1" stroke-width="2"/>
                        <polygon points="50,80 60,105 70,80" fill="#ffffff"/>
                        <circle cx="60" cy="50" r="30" fill="#fbcfe8"/>
                        <path d="M30 45 C30 20, 90 20, 90 45 C90 30, 80 15, 60 15 C40 15, 30 30, 30 45 Z" fill="#312e81"/>
                        <rect x="42" y="42" width="14" height="10" rx="2" fill="none" stroke="#1e1b4b" stroke-width="2"/>
                        <rect x="64" y="42" width="14" height="10" rx="2" fill="none" stroke="#1e1b4b" stroke-width="2"/>
                        <line x1="56" y1="46" x2="64" y2="46" stroke="#1e1b4b" stroke-width="2"/>
                        <circle cx="49" cy="47" r="2.5" fill="#1e1b4b"/>
                        <circle cx="71" cy="47" r="2.5" fill="#1e1b4b"/>
                        <path d="M44 38 Q50 35 56 38" fill="none" stroke="#78350f" stroke-width="2"/>
                        <path d="M64 38 Q70 35 76 38" fill="none" stroke="#78350f" stroke-width="2"/>
                        <ellipse id="teacherMouth-{s_idx}" cx="60" cy="64" rx="5" ry="3" fill="#be123c"/>
                    </svg>
                    <span class="px-2 py-0.5 rounded-full text-[9px] font-extrabold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 mt-1">
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
                            <svg class="w-3 h-3 text-indigo-400" fill="currentColor" viewBox="0 0 20 20"><path d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z"/></svg>
                            Replay Audio
                        </button>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-200 leading-relaxed italic">
                        "{slide['quote']}"
                    </p>
                    <div class="mt-2 text-xs text-indigo-300/90">
                        {slide['lead']}
                    </div>
                </div>
            </div>
            """

            simulator_html = get_simulator_markup(s_idx)

            completion_banner = ""
            if s_idx == total_slides - 1:
                completion_banner = """
                <div id="lastSlideNotice" class="mt-6 p-4 rounded-xl bg-indigo-950/40 border border-indigo-500/40 text-center">
                    <div class="inline-flex items-center gap-2 text-indigo-400 font-extrabold text-sm mb-1">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        <span>You have reached the last slide of this chapter (Chapter 10: The Human Eye and the Colourful World)!</span>
                    </div>
                    <p class="text-xs text-slate-300">Congratulations! You have completed all 16 master interactive lessons and all 40 mastery challenge questions covering the entire NCERT textbook.</p>
                </div>
                """

            slide_body = f"""
            <div id="slide-{s_idx}" class="slide-container {active_class}">
                <!-- Header -->
                <div class="mb-4">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-1">
                        <span class="px-2.5 py-1 rounded-md text-xs font-bold uppercase tracking-wider bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
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
                    <h4 class="text-xs font-bold uppercase tracking-wider text-indigo-400 mb-3 flex items-center gap-2">
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
                            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
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
                        <button onclick="openQuizSolution('{q_item['id']}', '{clean_title}', '{clean_solution}')" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-indigo-600 hover:bg-indigo-500 text-white transition flex items-center gap-1.5 shadow-md cursor-pointer">
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
                <div id="lastSlideNotice" class="mt-6 p-4 rounded-xl bg-indigo-950/40 border border-indigo-500/40 text-center">
                    <div class="inline-flex items-center gap-2 text-indigo-400 font-extrabold text-sm mb-1">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        <span>You have reached the last slide of this chapter (Chapter 10: The Human Eye and the Colourful World)!</span>
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
    <title>NCERT Class 10 Science • Chapter 10: The Human Eye and the Colourful World</title>
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

        /* Subtle teacher head-bob animation */
        @keyframes teacherBob {{
            0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
            50% {{ transform: translateY(-3px) rotate(0.8deg); }}
        }}
        .teacher-bob {{
            animation: teacherBob 4s ease-in-out infinite;
        }}

        /* Talking mouth pulsing */
        @keyframes mouthMove {{
            0%, 100% {{ ry: 3; rx: 5; }}
            50% {{ ry: 6.5; rx: 4.5; }}
        }}
        .talking-mouth {{
            animation: mouthMove 0.25s infinite alternate;
        }}

        /* Modal backdrop glassmorphism */
        .modal-backdrop {{
            background: rgba(3, 7, 18, 0.85);
            backdrop-filter: blur(8px);
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between selection:bg-indigo-500 selection:text-white">

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
                    <span class="w-2.5 h-2.5 rounded-full bg-indigo-500 shadow-md shadow-indigo-500/50"></span>
                    <h1 class="text-xs sm:text-sm font-bold text-slate-100 truncate max-w-[200px] sm:max-w-md">
                        The Human Eye and the Colourful World
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
                <button onclick="navigateSlide(1)" id="nextBtn" class="px-4 py-2 rounded-xl text-xs font-bold bg-indigo-600 hover:bg-indigo-500 text-white transition flex items-center gap-1.5 shadow-md shadow-indigo-600/30 cursor-pointer">
                    Next
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </button>
            </div>

            <div class="flex items-center gap-1.5 overflow-x-auto max-w-full sm:max-w-2xl py-1 custom-scrollbar">
                {pills_html}
            </div>

            <div class="hidden md:flex items-center gap-2 text-xs text-slate-400 font-mono">
                <span>Slide</span>
                <span id="currentSlideIndicator" class="text-indigo-400 font-bold">1</span>
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
                <span class="px-2.5 py-1 rounded-md text-xs font-extrabold uppercase tracking-wider bg-indigo-500/20 text-indigo-300 border border-indigo-500/40">
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
                <button onclick="closeSolutionModal()" class="px-4 py-2 rounded-xl text-xs font-bold bg-indigo-600 hover:bg-indigo-500 text-white transition cursor-pointer">
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
                newPill.classList.add('bg-indigo-600', 'text-white', 'font-bold');
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
        function updateSim1Pupil(val) {{
            playTone(420, 'sine', 0.05);
            const v = parseInt(val);
            const top = document.getElementById('sim1-iris-top');
            const bot = document.getElementById('sim1-iris-bot');
            const desc = document.getElementById('sim1-desc');
            const lbl = document.getElementById('sim1-light-val');
            
            // Map 1..5: 1=very dark (pupil large, iris small), 5=intense sun (pupil small, iris large)
            const irisHeights = [14, 20, 26, 32, 38];
            const h = irisHeights[v-1];
            top.setAttribute('height', h);
            bot.setAttribute('height', h);
            bot.setAttribute('y', 155 - h);

            const labels = ['Pitch Dark (Max Dilated)', 'Dim Light', 'Normal Day', 'Bright Classroom', 'Direct Sunlight (Constricted)'];
            lbl.textContent = labels[v-1];
            desc.textContent = `Ambient Level ${{v}}: Iris adjusts aperture. Pupil ${{(v <= 2) ? 'DILATES to allow maximum light' : 'CONSTRICTS to protect internal photoreceptors'}} on retina.`;
        }}

        function updateSim2Accommodation(dist) {{
            playTone(450, 'sine', 0.05);
            const d = parseInt(dist);
            const lens = document.getElementById('sim2-lens');
            const objLine = document.getElementById('sim2-obj-line');
            const objArrow = document.getElementById('sim2-obj-arrow');
            const objText = document.getElementById('sim2-obj-text');
            const rTop = document.getElementById('sim2-ray-top');
            const rBot = document.getElementById('sim2-ray-bot');
            const lbl = document.getElementById('sim2-dist-val');
            const status = document.getElementById('sim2-status');

            // Object x position from 40 (far) to 180 (near 25cm)
            // Range 25..300: 25 -> x=180, 300 -> x=40
            const xObj = 180 - ((d - 25) / 275) * 140;
            objLine.setAttribute('x1', xObj);
            objLine.setAttribute('x2', xObj);
            objArrow.setAttribute('points', `${{xObj}},60 ${{xObj-4}},70 ${{xObj+4}},70`);
            objText.setAttribute('x', xObj);

            rTop.setAttribute('x1', xObj);
            rBot.setAttribute('x1', xObj);

            if (d < 50) {{
                lbl.textContent = `${{d}} cm (Near Point D = 25 cm)`;
                // Thick lens (ciliary contracted)
                lens.setAttribute('d', 'M 240 55 Q 260 100 240 145 Q 220 100 240 55 Z');
                status.textContent = 'Nearby Object (25 cm): Ciliary muscles CONTRACT → Eye lens becomes THICK & round → Focal length decreases → Rays converge sharply onto retina.';
            }} else {{
                lbl.textContent = `${{d}} cm (Distant Object)`;
                // Thin lens (ciliary relaxed)
                lens.setAttribute('d', 'M 240 55 Q 247 100 240 145 Q 233 100 240 55 Z');
                status.textContent = 'Distant Object: Ciliary muscles RELAX → Suspensory ligaments pull tight → Lens becomes THIN → Focal length increases to maximum.';
            }}
        }}

        function setSim3Mode(mode) {{
            playTone(460, 'sine', 0.08);
            const btnDef = document.getElementById('btn-sim3-defect');
            const btnCor = document.getElementById('btn-sim3-correct');
            const spec = document.getElementById('sim3-spectacle');
            const rays = document.getElementById('sim3-rays-group');
            const desc = document.getElementById('sim3-desc');

            if (mode === 'defective') {{
                btnDef.className = 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition';
                btnCor.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                spec.classList.add('hidden');
                rays.innerHTML = `
                    <line x1="160" y1="75" x2="250" y2="75" stroke="#fef08a" stroke-width="2"/>
                    <line x1="160" y1="125" x2="250" y2="125" stroke="#fef08a" stroke-width="2"/>
                    <line x1="250" y1="75" x2="330" y2="100" stroke="#f43f5e" stroke-width="2.2"/>
                    <line x1="250" y1="125" x2="330" y2="100" stroke="#f43f5e" stroke-width="2.2"/>
                    <line x1="330" y1="100" x2="390" y2="85" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <line x1="330" y1="100" x2="390" y2="115" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <circle cx="330" cy="100" r="4" fill="#f43f5e"/>
                    <text x="330" y="85" fill="#f43f5e" font-size="8" text-anchor="middle" font-weight="bold">Focus in Front</text>
                `;
                desc.textContent = 'Uncorrected Myopia: Parallel starlight converges IN FRONT of retina (at ~330px) → Distant objects appear blurred.';
            }} else {{
                btnCor.className = 'px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition';
                btnDef.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                spec.classList.remove('hidden');
                rays.innerHTML = `
                    <!-- Diverged by concave spectacle -->
                    <line x1="168" y1="75" x2="250" y2="68" stroke="#38bdf8" stroke-width="2"/>
                    <line x1="168" y1="125" x2="250" y2="132" stroke="#38bdf8" stroke-width="2"/>
                    <!-- Focused by eye lens onto retina at 390 -->
                    <line x1="250" y1="68" x2="390" y2="100" stroke="#10b981" stroke-width="2.5"/>
                    <line x1="250" y1="132" x2="390" y2="100" stroke="#10b981" stroke-width="2.5"/>
                    <circle cx="390" cy="100" r="4" fill="#10b981"/>
                    <text x="390" y="85" fill="#10b981" font-size="8" text-anchor="middle" font-weight="bold">Perfect Retina Focus</text>
                `;
                desc.textContent = 'Concave Lens Corrected: Diverging spectacle lens spreads rays so they appear from far point, focusing precisely ON the retina!';
            }}
        }}

        function setSim4Mode(mode) {{
            playTone(470, 'sine', 0.08);
            const btnDef = document.getElementById('btn-sim4-defect');
            const btnCor = document.getElementById('btn-sim4-correct');
            const spec = document.getElementById('sim4-spectacle');
            const rays = document.getElementById('sim4-rays-group');
            const desc = document.getElementById('sim4-desc');

            if (mode === 'defective') {{
                btnDef.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                btnCor.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                spec.classList.add('hidden');
                rays.innerHTML = `
                    <line x1="50" y1="100" x2="245" y2="75" stroke="#fef08a" stroke-width="1.8"/>
                    <line x1="50" y1="100" x2="245" y2="125" stroke="#fef08a" stroke-width="1.8"/>
                    <line x1="245" y1="75" x2="365" y2="90" stroke="#f59e0b" stroke-width="2"/>
                    <line x1="245" y1="125" x2="365" y2="110" stroke="#f59e0b" stroke-width="2"/>
                    <line x1="365" y1="90" x2="425" y2="100" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <line x1="365" y1="110" x2="425" y2="100" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3"/>
                    <circle cx="425" cy="100" r="4" fill="#f59e0b"/>
                    <text x="430" y="90" fill="#f59e0b" font-size="8" text-anchor="middle" font-weight="bold">Focus Behind Retina</text>
                `;
                desc.textContent = 'Uncorrected Hypermetropic Eye: Near rays converge BEHIND retina → Reading text at 25 cm is blurred.';
            }} else {{
                btnCor.className = 'px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition';
                btnDef.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                spec.classList.remove('hidden');
                rays.innerHTML = `
                    <line x1="50" y1="100" x2="165" y2="75" stroke="#fef08a" stroke-width="1.8"/>
                    <line x1="50" y1="100" x2="165" y2="125" stroke="#fef08a" stroke-width="1.8"/>
                    <!-- Additional convergence by convex spectacle -->
                    <line x1="165" y1="75" x2="245" y2="80" stroke="#f59e0b" stroke-width="2"/>
                    <line x1="165" y1="125" x2="245" y2="120" stroke="#f59e0b" stroke-width="2"/>
                    <!-- Sharp convergence onto retina at 365 -->
                    <line x1="245" y1="80" x2="365" y2="100" stroke="#10b981" stroke-width="2.5"/>
                    <line x1="245" y1="120" x2="365" y2="100" stroke="#10b981" stroke-width="2.5"/>
                    <circle cx="365" cy="100" r="4" fill="#10b981"/>
                    <text x="365" y="85" fill="#10b981" font-size="8" text-anchor="middle" font-weight="bold">Perfect Retina Focus</text>
                `;
                desc.textContent = 'Convex Lens Corrected: Extra converging power bends rays so they appear from patient shifted near point, landing sharply ON the retina!';
            }}
        }}

        function setSim5Zone(zone) {{
            playTone(480, 'sine', 0.08);
            const bUp = document.getElementById('btn-sim5-upper');
            const bLow = document.getElementById('btn-sim5-lower');
            const zUp = document.getElementById('sim5-upper-zone');
            const zLow = document.getElementById('sim5-lower-zone');
            const rayOverlay = document.getElementById('sim5-ray-overlay');
            const desc = document.getElementById('sim5-desc');

            if (zone === 'upper') {{
                bUp.className = 'px-2.5 py-1 rounded text-xs font-bold bg-purple-600 text-white transition';
                bLow.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                zUp.setAttribute('fill-opacity', '0.45');
                zLow.setAttribute('fill-opacity', '0.15');
                rayOverlay.innerHTML = `
                    <line x1="50" y1="65" x2="180" y2="65" stroke="#fef08a" stroke-width="2"/>
                    <polygon points="180,65 170,60 170,70" fill="#fef08a"/>
                    <text x="110" y="55" fill="#fef08a" font-size="8" text-anchor="middle">Distant Light Rays (Upper Concave Lens)</text>
                `;
                desc.textContent = 'Upper Zone Selected: Diverging concave lens allows the ageing patient to view distant road signs and blackboards clearly.';
            }} else {{
                bLow.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                bUp.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                zLow.setAttribute('fill-opacity', '0.45');
                zUp.setAttribute('fill-opacity', '0.15');
                rayOverlay.innerHTML = `
                    <line x1="50" y1="150" x2="180" y2="150" stroke="#f59e0b" stroke-width="2"/>
                    <polygon points="180,150 170,145 170,155" fill="#f59e0b"/>
                    <text x="110" y="140" fill="#f59e0b" font-size="8" text-anchor="middle">Near Reading Rays (Lower Convex Lens)</text>
                `;
                desc.textContent = 'Lower Zone Selected: Converging convex lens provides extra refractive power for comfortable reading at 25 cm.';
            }}
        }}

        function calcSim6() {{
            const type = document.getElementById('sim6-defect-type').value;
            const dist = parseFloat(document.getElementById('sim6-dist').value) || 1.2;
            const fVal = document.getElementById('sim6-f-val');
            const pVal = document.getElementById('sim6-p-val');
            const lVal = document.getElementById('sim6-lens-val');

            if (type === 'myopia') {{
                // u = -inf, v = -dist => f = -dist => P = 1/f = -1/dist
                const f = -dist;
                const p = 1 / f;
                fVal.textContent = `${{f.toFixed(2)}} m`;
                pVal.textContent = `${{p.toFixed(2)}} D`;
                lVal.textContent = 'Concave Lens (Diverging)';
                lVal.className = 'font-bold text-rose-400';
            }} else {{
                // u = -0.25 m, v = -dist => 1/f = 1/v - 1/u = -1/dist + 4
                const invF = (-1 / dist) + 4.0;
                const f = 1 / invF;
                fVal.textContent = `+${{f.toFixed(2)}} m (${{(f*100).toFixed(1)}} cm)`;
                pVal.textContent = `+${{invF.toFixed(2)}} D`;
                lVal.textContent = 'Convex Lens (Converging)';
                lVal.className = 'font-bold text-emerald-400';
            }}
        }}

        function updateSim7Prism(deg) {{
            playTone(490, 'sine', 0.05);
            const i = parseInt(deg);
            const A = 60;
            // n approx 1.52 -> sin(r) = sin(i)/1.52
            const sinI = Math.sin(i * Math.PI / 180);
            const sinR = sinI / 1.52;
            const rDeg = Math.asin(sinR) * 180 / Math.PI;
            const r2Deg = A - rDeg;
            const sinE = 1.52 * Math.sin(r2Deg * Math.PI / 180);
            const eDeg = (sinE <= 1.0) ? Math.asin(sinE) * 180 / Math.PI : 90;
            const dDeg = i + eDeg - A;

            document.getElementById('sim7-angle-val').textContent = `${{i}}°`;
            document.getElementById('sim7-i-val').textContent = `${{i}}°`;
            document.getElementById('sim7-r-val').textContent = `${{rDeg.toFixed(1)}}°`;
            document.getElementById('sim7-e-val').textContent = `${{eDeg.toFixed(1)}}°`;
            document.getElementById('sim7-d-val').textContent = `${{dDeg.toFixed(1)}}°`;
        }}

        function setSim8Highlight(color) {{
            playTone(510, 'sine', 0.08);
            const desc = document.getElementById('sim8-desc');
            const bAll = document.getElementById('btn-sim8-all');
            const bRed = document.getElementById('btn-sim8-red');
            const bVio = document.getElementById('btn-sim8-violet');

            bAll.className = 'px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700';
            bRed.className = 'px-2 py-1 rounded text-xs font-bold bg-slate-800 text-rose-400 hover:bg-slate-700';
            bVio.className = 'px-2 py-1 rounded text-xs font-bold bg-slate-800 text-purple-400 hover:bg-slate-700';

            if (color === 'red') {{
                bRed.className = 'px-2 py-1 rounded text-xs font-bold bg-rose-600 text-white';
                desc.textContent = 'Red Light (λ ≈ 700 nm): Longest visible wavelength, travels fastest in glass (highest v), lowest refractive index n, therefore BENDS THE LEAST.';
            }} else if (color === 'violet') {{
                bVio.className = 'px-2 py-1 rounded text-xs font-bold bg-purple-600 text-white';
                desc.textContent = 'Violet Light (λ ≈ 400 nm): Shortest visible wavelength, slowed down most in glass (lowest v), highest refractive index n, therefore BENDS THE MOST.';
            }} else {{
                bAll.className = 'px-2 py-1 rounded text-xs font-bold bg-cyan-600 text-white';
                desc.textContent = 'Full VIBGYOR Spectrum: Violet, Indigo, Blue, Green, Yellow, Orange, Red fan out along distinct paths due to wavelength-dependent speed!';
            }}
        }}

        function setSim9Mode(mode) {{
            playTone(520, 'sine', 0.08);
            const bSplit = document.getElementById('btn-sim9-split');
            const bRec = document.getElementById('btn-sim9-rec');
            const prism2 = document.getElementById('sim9-prism2');
            const desc = document.getElementById('sim9-desc');

            if (mode === 'split') {{
                bSplit.className = 'px-2.5 py-1 rounded text-xs font-bold bg-indigo-600 text-white transition';
                bRec.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                prism2.classList.add('hidden');
                desc.textContent = 'Step 1: Single glass prism disperses white sunlight into 7 spectrum colors.';
            }} else {{
                bRec.className = 'px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition';
                bSplit.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                prism2.classList.remove('hidden');
                desc.textContent = 'Step 2: Second inverted prism in contact allows all colors to recombine into an emerging beam of pure WHITE LIGHT!';
            }}
        }}

        function pulseSim10Drop() {{
            playTone(600, 'sine', 0.15);
            const desc = document.getElementById('sim10-desc');
            desc.innerHTML = '<span class="text-white font-bold animate-pulse">Tracing: Entry Refraction (Splits) → Total Internal Reflection (Back Wall) → Exit Refraction → Rainbow into Observer Eye!</span>';
            setTimeout(() => {{
                desc.textContent = 'Triple Process: Refraction & dispersion at entry → Internal reflection at back wall → Final refraction at exit (42° Red on top, 40° Violet below).';
            }}, 2400);
        }}

        let sim11Turbulent = true;
        let sim11Interval = null;
        function toggleSim11Turbulence() {{
            sim11Turbulent = !sim11Turbulent;
            const btn = document.getElementById('btn-sim11-turb');
            const star = document.getElementById('sim11-star-apparent');
            const desc = document.getElementById('sim11-desc');

            if (sim11Turbulent) {{
                btn.textContent = 'Turbulence Active';
                btn.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                desc.textContent = 'Turbulent atmosphere active: Random air convection constantly shifts optical density → Star brightness flickers rapidly (Twinkling!).';
                if (!sim11Interval) {{
                    sim11Interval = setInterval(() => {{
                        if (star) {{
                            const dx = (Math.random() - 0.5) * 6;
                            const dy = (Math.random() - 0.5) * 4;
                            star.setAttribute('transform', `translate(${{dx}}, ${{dy}})`);
                        }}
                    }}, 150);
                }}
            }} else {{
                btn.textContent = 'Turbulence Frozen';
                btn.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                desc.textContent = 'Atmosphere static: No air fluctuations → Starlight is steady (as seen above Earth atmosphere or in space).';
                clearInterval(sim11Interval);
                sim11Interval = null;
                if (star) star.removeAttribute('transform');
            }}
        }}

        function setSim12Mode(mode) {{
            playTone(530, 'sine', 0.08);
            const bSun = document.getElementById('btn-sim12-sun');
            const bPla = document.getElementById('btn-sim12-planet');
            const desc = document.getElementById('sim12-desc');

            if (mode === 'sunrise') {{
                bSun.className = 'px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 text-white transition';
                bPla.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                desc.textContent = '2 Minutes Early: Rays from Sun below the horizon bend through atmospheric layers into observer eyes, making sunrise 2 min earlier and sunset 2 min later (4 min extra day)!';
            }} else {{
                bPla.className = 'px-2.5 py-1 rounded text-xs font-bold bg-cyan-600 text-white transition';
                bSun.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                desc.textContent = 'Why Planets Do Not Twinkle: Planets are much closer to Earth, acting as extended sources (clusters of point sources). Their fluctuations average out to zero net variation!';
            }}
        }}

        function setSim13Beam(mode) {{
            playTone(540, 'sine', 0.1);
            const desc = document.getElementById('sim13-desc');
            desc.innerHTML = '<span class="text-white font-bold animate-pulse">Beaker 1: True Solution (Transparent, No Beam) vs Beaker 2: Colloid (Tyndall Scattering Visible!)</span>';
        }}

        function updateSim14Rayleigh(wl) {{
            playTone(520, 'sine', 0.04);
            const l = parseInt(wl);
            document.getElementById('sim14-wl-val').textContent = `${{l}} nm`;
            document.getElementById('sim14-lambda').textContent = `${{l}} nm`;

            // Rayleigh relative to 700 nm: (700 / l)^4
            const ratio = Math.pow(700 / l, 4);
            document.getElementById('sim14-rel').textContent = `${{ratio.toFixed(2)}}x`;

            const dome = document.getElementById('sim14-dome');
            const lvl = document.getElementById('sim14-level');
            const app = document.getElementById('sim14-app');

            if (l <= 480) {{
                dome.setAttribute('fill', '#0284c7');
                dome.setAttribute('fill-opacity', '0.45');
                lvl.textContent = 'Extremely High (~10x)';
                lvl.className = 'text-sky-400 font-bold';
                app.textContent = 'Blue Daytime Sky';
            }} else if (l <= 580) {{
                dome.setAttribute('fill', '#22c55e');
                dome.setAttribute('fill-opacity', '0.25');
                lvl.textContent = 'Moderate';
                lvl.className = 'text-yellow-400 font-bold';
                app.textContent = 'Midday Yellowish Sun';
            }} else {{
                dome.setAttribute('fill', '#ef4444');
                dome.setAttribute('fill-opacity', '0.2');
                lvl.textContent = 'Minimal (1.0x)';
                lvl.className = 'text-rose-400 font-bold';
                app.textContent = 'Red Danger Signals / Sunset';
            }}
        }}

        function setSim15Card(card) {{
            playTone(500, 'sine', 0.08);
            const btnR = document.getElementById('btn-sim15-rainbow');
            const btnT = document.getElementById('btn-sim15-twinkle');
            const btnS = document.getElementById('btn-sim15-sunrise');
            const btnB = document.getElementById('btn-sim15-bluesky');
            const btnTy = document.getElementById('btn-sim15-tyndall');
            const disp = document.getElementById('sim15-display');

            [btnR, btnT, btnS, btnB, btnTy].forEach(b => b.className = 'p-2 rounded-lg text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition text-center');

            if (card === 'rainbow') {{
                btnR.className = 'p-2 rounded-lg text-xs font-bold bg-rose-600 text-white transition text-center';
                disp.innerHTML = `
                    <div class="text-sm font-bold text-rose-400 mb-1">Rainbow Formation</div>
                    <div class="text-xs text-slate-300 space-y-1">
                        <p><strong>Primary Cause:</strong> Dispersion of sunlight by tiny suspended raindrops acting as microscopic triangular prisms.</p>
                        <p><strong>Three Optical Steps:</strong> (1) Refraction with dispersion at raindrop entry → (2) Total internal reflection at inner rear wall → (3) Refraction upon exiting droplet.</p>
                        <p><strong>Crucial Rule:</strong> Always observed in the sky direction <em>opposite to the Sun</em> with observer's back to sunlight (42° Red, 40° Violet).</p>
                    </div>
                `;
            }} else if (card === 'twinkle') {{
                btnT.className = 'p-2 rounded-lg text-xs font-bold bg-amber-600 text-white transition text-center';
                disp.innerHTML = `
                    <div class="text-sm font-bold text-amber-400 mb-1">Twinkling of Stars</div>
                    <div class="text-xs text-slate-300 space-y-1">
                        <p><strong>Primary Cause:</strong> Atmospheric refraction through continuously shifting optical density layers of turbulent air.</p>
                        <p><strong>Point Source Effect:</strong> Because stars are light-years away, they appear as point sources of light.</p>
                        <p><strong>Result:</strong> Rapid fluctuating shifts in apparent ray path cause starlight intensity to flicker (bright and faint).</p>
                    </div>
                `;
            }} else if (card === 'sunrise') {{
                btnS.className = 'p-2 rounded-lg text-xs font-bold bg-cyan-600 text-white transition text-center';
                disp.innerHTML = `
                    <div class="text-sm font-bold text-cyan-400 mb-1">Advance Sunrise & Delayed Sunset</div>
                    <div class="text-xs text-slate-300 space-y-1">
                        <p><strong>Primary Cause:</strong> Downward curvature of solar light rays entering Earth's dense atmospheric envelope.</p>
                        <p><strong>Duration Shift:</strong> Sun is visible ~2 minutes before actual horizon crossing and ~2 minutes after actual sunset.</p>
                        <p><strong>Net Effect:</strong> Total daylight period is extended by approximately 4 minutes every day; apparent flattening of solar disc.</p>
                    </div>
                `;
            }} else if (card === 'bluesky') {{
                btnB.className = 'p-2 rounded-lg text-xs font-bold bg-sky-600 text-white transition text-center';
                disp.innerHTML = `
                    <div class="text-sm font-bold text-sky-400 mb-1">Blue Colour of Clear Sky</div>
                    <div class="text-xs text-slate-300 space-y-1">
                        <p><strong>Primary Cause:</strong> Rayleigh Scattering by fine air molecules (N₂ and O₂ smaller than visible light wavelengths).</p>
                        <p><strong>Mathematical Law:</strong> Scattering intensity is inversely proportional to the 4th power of wavelength: $I \\propto 1/\\lambda^4$.</p>
                        <p><strong>Comparison:</strong> Red wavelength is ~1.8x longer than blue; hence blue light is scattered ~10.5x more strongly in all directions!</p>
                    </div>
                `;
            }} else {{
                btnTy.className = 'p-2 rounded-lg text-xs font-bold bg-emerald-600 text-white transition text-center';
                disp.innerHTML = `
                    <div class="text-sm font-bold text-emerald-400 mb-1">The Tyndall Effect</div>
                    <div class="text-xs text-slate-300 space-y-1">
                        <p><strong>Primary Cause:</strong> Diffuse scattering of light beam by colloidal particles suspended in a medium.</p>
                        <p><strong>Everyday Examples:</strong> Sunlight piercing a dark smoke-filled room through a pinhole; sunbeams streaming through misty forest canopy.</p>
                        <p><strong>Particle Criterion:</strong> True solutions have particles < 1 nm (no scattering); colloids have particles 1–1000 nm (scattering visible).</p>
                    </div>
                `;
            }}

            if (window.renderMathInElement) {{
                renderMathInElement(disp, {{
                    delimiters: [
                        {{left: '$$', right: '$$', display: true}},
                        {{left: '$', right: '$', display: false}}
                    ]
                }});
            }}
        }}

        function loadExerciseSol(num) {{
            playTone(480, 'sine', 0.08);
            const box = document.getElementById('exercise-sol-box');
            const solutions = {{
                1: "<strong>Exercise Q1:</strong> The human eye can focus on objects at different distances by adjusting the focal length of the eye lens. This is due to <strong>(b) accommodation</strong> (NCERT Page 170).",
                2: "<strong>Exercise Q2:</strong> The human eye forms the image of an object at its <strong>(d) retina</strong> (NCERT Page 170).",
                3: "<strong>Exercise Q3:</strong> The least distance of distinct vision for a young adult with normal vision is about <strong>(c) 25 cm</strong> (NCERT Page 170).",
                4: "<strong>Exercise Q4:</strong> The change in focal length of an eye lens is caused by the action of the <strong>(c) ciliary muscles</strong> (NCERT Page 170).",
                5: "<strong>Exercise Q5:</strong><br>(i) Distant vision: $P = -5.5\\text{{ D}} \\implies f = 1/P = 1/(-5.5) = -0.182\\text{{ m}} = -18.2\\text{{ cm}}$ (Concave lens).<br>(ii) Near vision: $P = +1.5\\text{{ D}} \\implies f = 1/P = 1/(+1.5) = +0.667\\text{{ m}} = +66.7\\text{{ cm}}$ (Convex lens).",
                6: "<strong>Exercise Q6:</strong> Far point $v = -80\\text{{ cm}} = -0.80\\text{{ m}}, u = -\\infty$.<br>$1/f = 1/v - 1/u = -1/0.80 - 0 \\implies f = -0.80\\text{{ m}}$.<br>Power $P = 1/f = 1/(-0.80) = -1.25\\text{{ D}}$. Corrective lens: <strong>Concave lens of power -1.25 D</strong>.",
                7: "<strong>Exercise Q7:</strong> Defective near point $v = -1\\text{{ m}} = -100\\text{{ cm}}$, normal near point $u = -25\\text{{ cm}} = -0.25\\text{{ m}}$.<br>$1/f = 1/v - 1/u = 1/(-1.0) - 1/(-0.25) = -1.0 + 4.0 = +3.0\\text{{ D}}$.<br>Focal length $f = +1/3\\text{{ m}} = +33.3\\text{{ cm}}$. Corrective lens: <strong>Convex lens of power +3.0 D</strong>.",
                8: "<strong>Exercise Q8:</strong> Ciliary muscles cannot contract beyond a biological minimum limit to increase the lens curvature further. Holding objects closer than 25 cm causes excessive ocular strain and blurred vision.",
                9: "<strong>Exercise Q9:</strong> When object distance increases, the image distance inside the eye <strong>remains constant</strong> (fixed distance between crystalline lens and retina ≈ 2.3 cm). Instead, ciliary muscles relax to increase the focal length.",
                10: "<strong>Exercise Q10:</strong> Twinkling of stars is caused by atmospheric refraction through turbulent air layers of constantly changing optical density. Because stars are distant point sources, the path shifts and intensity flickers.",
                11: "<strong>Exercise Q11:</strong> Planets are much closer to Earth and act as extended sources composed of numerous point sources. Fluctuations from individual points average out to zero net variation, nullifying any twinkling effect.",
                12: "<strong>Exercise Q12:</strong> Outer space lacks an atmosphere; in the absence of gaseous molecules and aerosol particles, no Rayleigh scattering occurs. Hence, sunlight is not scattered and the sky appears pitch black."
            }};
            box.innerHTML = solutions[num] || "Solution not found.";
            if (window.renderMathInElement) {{
                renderMathInElement(box, {{
                    delimiters: [
                        {{left: '$$', right: '$$', display: true}},
                        {{left: '$', right: '$', display: false}}
                    ]
                }});
            }}
        }}

        window.addEventListener('DOMContentLoaded', () => {{
            showSlide(0);
            toggleSim11Turbulence();
            calcSim6();
            document.body.addEventListener('click', () => initAudio(), {{ once: true }});
            document.body.addEventListener('keydown', () => initAudio(), {{ once: true }});
        }});
    </script>
</body>
</html>
"""

    os.makedirs("public/animations", exist_ok=True)
    out_path = "public/animations/the-human-eye-and-the-colourful-world.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"Successfully generated {out_path} ({len(html_template)} bytes)")

if __name__ == '__main__':
    generate_html()
