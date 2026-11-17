# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 9: Light - Reflection and Refraction
Simulators 1 to 8 HTML Generator
"""

import json

sims_part1 = {
    1: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>💡</span> Light Propagation & Wave-Particle Duality
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Compare straight ray rectilinear optics with nanoscale diffraction wave bending</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide1Mode('ray')" id="btnSlide1Ray" class="px-3 py-1.5 rounded-xl bg-amber-600 text-white text-xs font-semibold shadow-md transition-all">
                    Ray Optics (Macro Scale)
                </button>
                <button onclick="setSlide1Mode('diffraction')" id="btnSlide1Diff" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all">
                    Diffraction (Wave Scale)
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide1Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1 border-t border-slate-800/80">
            <div>
                <label class="block text-xs font-medium text-slate-400 mb-1">Obstacle Scale: <span id="slide1ScaleDisplay" class="text-amber-400 font-bold">Macroscopic (5 cm)</span></label>
                <input type="range" id="slide1ScaleSlider" min="1" max="2" value="1" oninput="setSlide1Scale(this.value)" class="w-full accent-amber-500 cursor-pointer">
            </div>
            <div id="slide1Stats" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 flex items-center justify-around">
                <span>Model: <strong class="text-amber-400" id="slide1Model">Straight Ray Lines</strong></span>
                <span>Shadow: <strong class="text-emerald-400" id="slide1Shadow">Sharp Boundary</strong></span>
            </div>
        </div>

        <div id="slide1Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            In macroscopic everyday environments, light travels along straight lines, producing sharp shadows. Around microscopic obstacles, wave diffraction causes light to bend around edges.
        </div>
    </div>
    """,

    2: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🪞</span> Universal Laws of Reflection & Plane Mirror Images
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Verify angle i = angle r and explore virtual, erect, laterally inverted image properties</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="toggleSlide2Lateral()" class="px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-md transition-all">
                    Show Lateral Inversion
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide2Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1 border-t border-slate-800/80">
            <div>
                <label class="block text-xs font-medium text-slate-400 mb-1">Angle of Incidence (i): <span id="slide2AngleDisplay" class="text-indigo-400 font-bold">45°</span></label>
                <input type="range" id="slide2AngleSlider" min="0" max="75" value="45" oninput="setSlide2Angle(this.value)" class="w-full accent-indigo-500 cursor-pointer">
            </div>
            <div class="flex items-center justify-between p-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                <span>Angle of Reflection (r): <strong class="text-indigo-400" id="slide2AngleR">45°</strong></span>
                <span>Coplanar: <strong class="text-emerald-400">Yes (i = r)</strong></span>
            </div>
        </div>

        <div id="slide2Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Law 1: The angle of incidence equals the angle of reflection (i = r). Law 2: Incident ray, reflected ray, and normal all lie in the same plane. Plane mirror images are virtual, erect, and laterally inverted.
        </div>
    </div>
    """,

    3: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>📐</span> Spherical Mirror Anatomy & Geometric Focal Formula
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Explore Pole (P), Focus (F), Center of Curvature (C), and the relationship R = 2f</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide3Type('concave')" id="btnSlide3Concave" class="px-3 py-1.5 rounded-xl bg-cyan-600 text-white text-xs font-semibold shadow-md transition-all">
                    Concave (Converging)
                </button>
                <button onclick="setSlide3Type('convex')" id="btnSlide3Convex" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all">
                    Convex (Diverging)
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide3Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1 border-t border-slate-800/80">
            <div>
                <label class="block text-xs font-medium text-slate-400 mb-1">Radius of Curvature (R): <span id="slide3RDisplay" class="text-cyan-400 font-bold">30 cm</span></label>
                <input type="range" id="slide3RSlider" min="16" max="40" value="30" oninput="setSlide3R(this.value)" class="w-full accent-cyan-500 cursor-pointer">
            </div>
            <div class="flex items-center justify-between p-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                <span>Focal Length (f = R/2): <strong class="text-cyan-400" id="slide3FDisplay">15 cm</strong></span>
                <span>Focus Location: <strong class="text-emerald-400" id="slide3FPos">Midway P & C</strong></span>
            </div>
        </div>

        <div id="slide3Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            The center of curvature C is the center of the sphere. The principal focus F lies exactly midway between the pole P and center C, satisfying R = 2f for mirrors of small aperture.
        </div>
    </div>
    """,

    4: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🧭</span> The 4 Standard Ray Tracing Rules for Concave Mirrors
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Observe the 4 fundamental ray trajectories used to locate optical images</p>
            </div>
            <div class="flex flex-wrap items-center gap-1.5">
                <button onclick="setSlide4Ray(1)" id="btnSlide4Ray1" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-white text-xs font-semibold">1. Parallel → F</button>
                <button onclick="setSlide4Ray(2)" id="btnSlide4Ray2" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">2. F → Parallel</button>
                <button onclick="setSlide4Ray(3)" id="btnSlide4Ray3" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">3. Through C</button>
                <button onclick="setSlide4Ray(4)" id="btnSlide4Ray4" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">4. Oblique at P</button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide4Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide4RuleDesc" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Rule 1: A ray parallel to the principal axis passes through the principal focus F after reflection from a concave mirror.
        </div>
    </div>
    """,

    5: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🕯️</span> Concave Mirror Image Formation: 6 Object Positions
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Drag object to observe real/virtual transitions, image sizes & position shifts (Table 9.1)</p>
            </div>
            <div class="flex items-center gap-2">
                <select id="slide5PresetSelect" onchange="setSlide5Preset(this.value)" class="bg-slate-900 border border-slate-700 text-xs text-slate-200 rounded-lg px-2.5 py-1 focus:ring-1 focus:ring-teal-500">
                    <option value="beyondC">Beyond C (Diminished Real)</option>
                    <option value="atC">At C (Same Size Real)</option>
                    <option value="betweenCF">Between C and F (Enlarged Real)</option>
                    <option value="atF">At F (Image at Infinity)</option>
                    <option value="betweenPF">Between P and F (Magnified Virtual)</option>
                    <option value="infinity">At Infinity (Point Image at F)</option>
                </select>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide5Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Object Position</span>
                <span id="slide5ObjPos" class="text-xs font-bold text-white">Beyond C</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Image Position</span>
                <span id="slide5ImgPos" class="text-xs font-bold text-teal-400">Between F and C</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Size</span>
                <span id="slide5ImgSize" class="text-xs font-bold text-amber-400">Diminished</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Nature</span>
                <span id="slide5ImgNature" class="text-xs font-bold text-rose-400">Real & Inverted</span>
            </div>
        </div>

        <div id="slide5Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Moving the object closer to the mirror shifts the real inverted image outward and enlarges it. Placing the object within the focal distance (between P and F) produces a magnified erect virtual image!
        </div>
    </div>
    """,

    6: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🔦</span> Practical Applications of Concave Mirrors
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Explore parallel headlight beams, dental inspection magnification & solar furnaces</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide6App('headlight')" id="btnSlide6Headlight" class="px-2.5 py-1 rounded-lg bg-amber-600 text-white text-xs font-semibold">Headlight / Torch</button>
                <button onclick="setSlide6App('dentist')" id="btnSlide6Dentist" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">Dentist Mirror</button>
                <button onclick="setSlide6App('solar')" id="btnSlide6Solar" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">Solar Furnace</button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide6Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide6Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            In vehicle headlights and searchlights, placing the bulb at focus F produces a powerful beam of parallel light rays that travels vast distances without spreading.
        </div>
    </div>
    """,

    7: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🚗</span> Convex Mirror Optics & Panoramic Field of View
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Understand why vehicle rear-view mirrors always form virtual, erect, diminished images</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="toggleSlide7FieldOfView()" id="btnSlide7Fov" class="px-3 py-1.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs font-semibold shadow-md transition-all">
                    Compare Field of View (Plane vs Convex)
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide7Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1 border-t border-slate-800/80">
            <div>
                <label class="block text-xs font-medium text-slate-400 mb-1">Trailing Vehicle Distance (u): <span id="slide7DistDisplay" class="text-blue-400 font-bold">25 m</span></label>
                <input type="range" id="slide7DistSlider" min="5" max="50" value="25" oninput="setSlide7Dist(this.value)" class="w-full accent-blue-500 cursor-pointer">
            </div>
            <div class="flex items-center justify-between p-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                <span>Image: <strong class="text-blue-400">Virtual & Erect</strong></span>
                <span>Field of View: <strong class="text-emerald-400">Wide Panoramic</strong></span>
            </div>
        </div>

        <div id="slide7Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Convex mirrors curve outwards, producing erect and diminished virtual images between P and F. This outward curvature provides drivers with a much wider panoramic view of trailing traffic than flat mirrors.
        </div>
    </div>
    """,

    8: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🧭</span> New Cartesian Sign Convention Coordinate System
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Pole P as origin, negative u, and focal length sign rules (+ for convex, - for concave)</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide8Mirror('concave')" id="btnSlide8Concave" class="px-2.5 py-1 rounded-lg bg-purple-600 text-white text-xs font-semibold">Concave (f < 0)</button>
                <button onclick="setSlide8Mirror('convex')" id="btnSlide8Convex" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">Convex (f > 0)</button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide8Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-3 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Object Distance (u)</span>
                <span class="text-xs font-mono font-bold text-rose-400">Always Negative (-u)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Focal Length (f)</span>
                <span id="slide8FocalSign" class="text-xs font-mono font-bold text-purple-400">Negative (-f)</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Height Above Axis</span>
                <span class="text-xs font-mono font-bold text-emerald-400">Positive (+h)</span>
            </div>
        </div>

        <div id="slide8Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            All distances are measured from the pole P (origin). Distances in the direction of incident light (right) are positive; distances against (left) are negative. Heights above principal axis are positive (+y).
        </div>
    </div>
    """
}

if __name__ == "__main__":
    with open(".agents/c10s_ch9_sims_part1.json", "w", encoding="utf-8") as f:
        json.dump(sims_part1, f, indent=2)
    print("Saved .agents/c10s_ch9_sims_part1.json successfully! (8 simulators)")
