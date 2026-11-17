# -*- coding: utf-8 -*-
"""
Class 10 Science Chapter 9: Light - Reflection and Refraction
Simulators 9 to 16 HTML Generator
"""

import json

sims_part2 = {
    9: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🧮</span> Mirror Formula & Magnification Solver (1/v + 1/u = 1/f)
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Solve for image distance v and linear magnification m = -v/u with textbook worked examples</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="loadSlide9Example('ex91')" id="btnSlide9Ex1" class="px-2.5 py-1 rounded-lg bg-blue-600 text-white text-xs font-semibold">Ex 9.1 (Convex Rear-View)</button>
                <button onclick="loadSlide9Example('ex92')" id="btnSlide9Ex2" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">Ex 9.2 (Concave Screen)</button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide9Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Object Distance (u)</span>
                <span id="slide9UVal" class="text-xs font-mono font-bold text-rose-400">-5.00 m</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Focal Length (f)</span>
                <span id="slide9FVal" class="text-xs font-mono font-bold text-purple-400">+1.50 m</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Image Distance (v)</span>
                <span id="slide9VVal" class="text-xs font-mono font-bold text-cyan-400">+1.15 m</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Magnification (m)</span>
                <span id="slide9MVal" class="text-xs font-mono font-bold text-emerald-400">+0.23 (Virtual)</span>
            </div>
        </div>

        <div id="slide9Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Mirror formula: 1/v = 1/f - 1/u. For a convex mirror, f > 0 and u < 0, giving a positive v (virtual image behind mirror) with positive fractional magnification m = -v/u.
        </div>
    </div>
    """,

    10: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🌊</span> Refraction of Light & Everyday Optical Phenomena
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Explore bent pencils, raised water tank floors & the reappearing coin in bowl (Activity 9.8)</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide10Demo('pencil')" id="btnSlide10Pencil" class="px-2.5 py-1 rounded-lg bg-cyan-600 text-white text-xs font-semibold">Bent Pencil</button>
                <button onclick="setSlide10Demo('coin')" id="btnSlide10Coin" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">Reappearing Coin</button>
                <button onclick="setSlide10Demo('tank')" id="btnSlide10Tank" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">Raised Tank Floor</button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide10Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div id="slide10Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Light travels slower in water than in air. When light rays travel obliquely from water into air, they bend away from the normal, causing the submerged object to appear raised and shifted upward.
        </div>
    </div>
    """,

    11: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🧱</span> Refraction through Rectangular Glass Slab & Lateral Shift
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Trace refraction at parallel boundaries, verify Snell's Law and measure lateral shift</p>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400">Angle of Incidence:</span>
                <span id="slide11AngleDisp" class="text-xs font-mono font-bold text-emerald-400">45°</span>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide11Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1 border-t border-slate-800/80">
            <div>
                <label class="block text-xs font-medium text-slate-400 mb-1">Adjust Angle of Incidence (i):</label>
                <input type="range" id="slide11Slider" min="10" max="75" value="45" oninput="setSlide11Angle(this.value)" class="w-full accent-emerald-500 cursor-pointer">
            </div>
            <div class="flex items-center justify-between p-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                <span>Angle of Emergence (e): <strong class="text-emerald-400" id="slide11Emerg">45° (e = i)</strong></span>
                <span>Lateral Shift: <strong class="text-amber-400" id="slide11Shift">Parallel Ray</strong></span>
            </div>
        </div>

        <div id="slide11Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Light bends toward the normal upon entering glass and away from the normal upon exiting into air. Because opposite faces are parallel, the emergent ray is strictly parallel to the incident ray, shifted by a lateral displacement.
        </div>
    </div>
    """,

    12: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>⚡</span> Absolute Refractive Index & The Kerosene Paradox
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Speed of light in media (n = c/v) and resolving optical density vs mass density</p>
            </div>
            <div class="flex items-center gap-2">
                <select id="slide12MediumSelect" onchange="setSlide12Medium(this.value)" class="bg-slate-900 border border-slate-700 text-xs text-slate-200 rounded-lg px-2.5 py-1 focus:ring-1 focus:ring-amber-500">
                    <option value="water">Water (n = 1.33)</option>
                    <option value="kerosene">Kerosene (n = 1.44)</option>
                    <option value="glass">Crown Glass (n = 1.52)</option>
                    <option value="diamond">Diamond (n = 2.42)</option>
                </select>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide12Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-3 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Refractive Index (n)</span>
                <span id="slide12IndexDisp" class="text-xs font-mono font-bold text-amber-400">1.33</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Speed of Light (v = c/n)</span>
                <span id="slide12SpeedDisp" class="text-xs font-mono font-bold text-cyan-400">2.25 × 10⁸ m/s</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Optical Density</span>
                <span id="slide12DensityDisp" class="text-xs font-bold text-emerald-400">Medium</span>
            </div>
        </div>

        <div id="slide12Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            The kerosene paradox: Kerosene has a higher refractive index (1.44) than water (1.33), making it optically denser. However, its mass density is lower (0.8 g/cm³), so it floats on water.
        </div>
    </div>
    """,

    13: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🔍</span> Spherical Lens Geometry & Dual Foci (F1, F2)
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Double convex (converging) vs double concave (diverging) and undeviated rays through O</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide13Lens('convex')" id="btnSlide13Convex" class="px-3 py-1.5 rounded-xl bg-teal-600 text-white text-xs font-semibold shadow-md transition-all">
                    Double Convex (Converging)
                </button>
                <button onclick="setSlide13Lens('concave')" id="btnSlide13Concave" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-all">
                    Double Concave (Diverging)
                </button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide13Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-3 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Lens Profile</span>
                <span id="slide13Profile" class="text-xs font-bold text-teal-400">Thicker in Middle</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Action on Parallel Rays</span>
                <span id="slide13Action" class="text-xs font-bold text-emerald-400">Converges at F2</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Optical Center (O)</span>
                <span class="text-xs font-bold text-white">Undeviated Passage</span>
            </div>
        </div>

        <div id="slide13Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            A convex lens converges parallel rays to a real focus at F2 on the right side. A concave lens diverges incoming parallel rays, appearing to emanate from a virtual focus at F1.
        </div>
    </div>
    """,

    14: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>🔬</span> Convex Lens Image Formations: 6 Scenarios (Table 9.4)
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Explore real inverted images, projection at 2F2 & magnifying reading glass mode</p>
            </div>
            <div class="flex items-center gap-2">
                <select id="slide14PresetSelect" onchange="setSlide14Preset(this.value)" class="bg-slate-900 border border-slate-700 text-xs text-slate-200 rounded-lg px-2.5 py-1 focus:ring-1 focus:ring-emerald-500">
                    <option value="beyond2F">Beyond 2F1 (Diminished Real)</option>
                    <option value="at2F">At 2F1 (Same Size Real at 2F2)</option>
                    <option value="betweenF2F">Between F1 and 2F1 (Enlarged Real)</option>
                    <option value="atF">At F1 (Image at Infinity)</option>
                    <option value="betweenOF">Between O and F1 (Magnifying Glass)</option>
                    <option value="concave">Concave Lens (Virtual Diminished)</option>
                </select>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide14Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Object Position</span>
                <span id="slide14ObjPos" class="text-xs font-bold text-white">Beyond 2F1</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Image Position</span>
                <span id="slide14ImgPos" class="text-xs font-bold text-emerald-400">Between F2 & 2F2</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Size</span>
                <span id="slide14ImgSize" class="text-xs font-bold text-amber-400">Diminished</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Nature</span>
                <span id="slide14ImgNature" class="text-xs font-bold text-cyan-400">Real & Inverted</span>
            </div>
        </div>

        <div id="slide14Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Placing an object within the focal length (between O and F1) turns a convex lens into a magnifying glass, producing an erect, magnified virtual image on the same side as the object.
        </div>
    </div>
    """,

    15: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>📏</span> Lens Formula & Magnification Solver (1/v - 1/u = 1/f)
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Calculate image position and magnification m = +v/u with textbook worked examples</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="loadSlide15Example('ex93')" id="btnSlide15Ex3" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-white text-xs font-semibold">Ex 9.3 (Concave Lens)</button>
                <button onclick="loadSlide15Example('ex94')" id="btnSlide15Ex4" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">Ex 9.4 (Convex Lens)</button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide15Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1 border-t border-slate-800/80 text-center">
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Object Distance (u)</span>
                <span id="slide15UVal" class="text-xs font-mono font-bold text-rose-400">-30.0 cm</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Focal Length (f)</span>
                <span id="slide15FVal" class="text-xs font-mono font-bold text-purple-400">-15.0 cm</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Image Distance (v)</span>
                <span id="slide15VVal" class="text-xs font-mono font-bold text-cyan-400">-10.0 cm</span>
            </div>
            <div class="p-2 rounded-xl bg-slate-900 border border-slate-800">
                <span class="block text-[10px] text-slate-400">Magnification (m = +v/u)</span>
                <span id="slide15MVal" class="text-xs font-mono font-bold text-emerald-400">+0.33 (Virtual)</span>
            </div>
        </div>

        <div id="slide15Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Lens formula: 1/v - 1/u = 1/f. Notice the minus sign between 1/v and 1/u. Unlike mirrors, lens magnification is positive v/u, where positive m denotes an erect virtual image.
        </div>
    </div>
    """,

    16: """
    <div class="bg-slate-950/80 border border-slate-800 rounded-2xl p-4 sm:p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
                <h3 class="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                    <span>👓</span> Optical Power (P = 1/f in Dioptres) & Lens Combinations
                </h3>
                <p class="text-xs text-slate-400 mt-0.5">Determine dioptres (D), corrective eyeglass prescriptions & net power (P = P1 + P2)</p>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="setSlide16EyeType('hypermetropia')" id="btnSlide16Hyp" class="px-2.5 py-1 rounded-lg bg-teal-600 text-white text-xs font-semibold">Farsighted (+2.0 D)</button>
                <button onclick="setSlide16EyeType('myopia')" id="btnSlide16Myo" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300 text-xs hover:bg-slate-700">Nearsighted (-2.5 D)</button>
            </div>
        </div>

        <div class="relative w-full aspect-[16/9] max-h-[340px] bg-slate-900/90 rounded-xl overflow-hidden border border-slate-800 flex items-center justify-center">
            <canvas id="slide16Canvas" width="600" height="340" class="w-full h-full object-contain"></canvas>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1 border-t border-slate-800/80">
            <div>
                <label class="block text-xs font-medium text-slate-400 mb-1">Focal Length (f in meters): <span id="slide16FDisplay" class="text-teal-400 font-bold">+0.50 m (+50 cm)</span></label>
                <input type="range" id="slide16Slider" min="20" max="200" value="50" oninput="setSlide16FocalSlider(this.value)" class="w-full accent-teal-500 cursor-pointer">
            </div>
            <div class="flex items-center justify-between p-2 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300">
                <span>Power (P = 1/f): <strong class="text-teal-400" id="slide16PowerDisp">+2.00 D</strong></span>
                <span>Lens Type: <strong class="text-white" id="slide16TypeDisp">Convex (Converging)</strong></span>
            </div>
        </div>

        <div id="slide16Status" class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 leading-relaxed">
            Power P = 1 / f (in meters) measured in Dioptres (D). Convex lenses have positive power (+P); concave lenses have negative power (-P). Thin lenses in contact add algebraically: P = P1 + P2.
        </div>
    </div>
    """
}

if __name__ == "__main__":
    with open(".agents/c10s_ch9_sims_part2.json", "w", encoding="utf-8") as f:
        json.dump(sims_part2, f, indent=2)
    print("Saved .agents/c10s_ch9_sims_part2.json successfully! (8 simulators)")
