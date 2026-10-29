# -*- coding: utf-8 -*-
"""
Interactive SVG/HTML simulator templates for Class 7 Chapter 6: Constructions and Tilings
"""

SIMULATORS_HTML = {
    "vesica_piscis_eye_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
      <h4 class="font-bold text-amber-300 text-sm sm:text-base">Simulator 1: The Symmetrical Eye (Vesica Piscis) & Equal Radii</h4>
    </div>
    <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Equilateral Rhombus</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Two identical circles of radius <span class="font-bold text-amber-300">r</span> centered at <span class="text-sky-300 font-bold">A</span> and <span class="text-emerald-300 font-bold">B</span> ($AB = r$). The overlapping region forms the symmetric eye where $AX = AY = BX = BY = r$, proving $XY \\perp AB$!</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="vesicaSvg" viewBox="0 0 500 300" class="w-full h-full select-none"></svg>
  </div>

  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-3">
    <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800">
      <label class="block text-xs font-semibold text-slate-300 mb-1 flex justify-between">
        <span>Radius r (Separation AB = r):</span>
        <span id="vesicaRadiusVal" class="text-amber-400 font-bold">90 px</span>
      </label>
      <input type="range" id="vesicaRadiusSlider" min="50" max="120" value="90" class="w-full accent-amber-500 cursor-pointer">
    </div>
    <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800 flex flex-col justify-center space-y-1 text-xs">
      <div class="flex justify-between text-slate-300">
        <span>Radii Equality:</span>
        <span class="text-emerald-400 font-bold font-mono">AX = AY = BX = BY = r</span>
      </div>
      <div class="flex justify-between text-slate-300">
        <span>Intersection Angle:</span>
        <span class="text-cyan-400 font-bold font-mono">∠(AB, XY) = 90.0°</span>
      </div>
    </div>
  </div>
</div>
""",

    "perp_bisector_stepper_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
      <h4 class="font-bold text-cyan-300 text-sm sm:text-base">Simulator 2: Step-by-Step Perpendicular Bisector Constructor</h4>
    </div>
    <span id="perpStepBadge" class="px-2 py-0.5 rounded text-[11px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Step 1 of 4</span>
  </div>
  <p class="text-xs text-slate-300 mb-3" id="perpStepDesc">Step 1: Baseline line segment AB is placed on the drawing plane.</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="perpBisectorSvg" viewBox="0 0 500 300" class="w-full h-full select-none"></svg>
  </div>

  <div class="flex flex-wrap items-center justify-between gap-2 mt-3">
    <div class="flex items-center space-x-2">
      <button id="perpPrevBtn" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 transition">◀ Previous</button>
      <button id="perpNextBtn" class="px-3 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-xs font-semibold text-white transition">Next Step ▶</button>
      <button id="perpResetBtn" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-400 transition">↺ Reset</button>
    </div>
    <div class="text-xs font-mono text-cyan-300 bg-slate-950/80 px-3 py-1.5 rounded-lg border border-slate-800">
      AM = <span id="perpAMVal">100</span>px | MB = <span id="perpMBVal">100</span>px | ∠ = 90°
    </div>
  </div>
</div>
""",

    "erect_90_point_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
      <h4 class="font-bold text-emerald-300 text-sm sm:text-base">Simulator 3: Erecting a 90° Right Angle at a Given Point P</h4>
    </div>
    <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Ray PC ⊥ Line L</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Drag point <span class="font-bold text-amber-300">P</span> anywhere along line $L$. The compass marks symmetric points $A, B$ ($AP=PB$) and strikes intersecting arcs above to erect perpendicular ray $PC$!</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="erect90Svg" viewBox="0 0 500 300" class="w-full h-full select-none cursor-ew-resize"></svg>
  </div>

  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-3">
    <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800 flex items-center justify-between">
      <span class="text-xs text-slate-300">Position of P:</span>
      <span id="erectPPos" class="text-emerald-400 font-bold font-mono text-xs">x = 250 px</span>
    </div>
    <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800 flex items-center justify-between">
      <span class="text-xs text-slate-300">Constructed Angle ∠(L, PC):</span>
      <span class="text-amber-300 font-bold font-mono text-xs">90.0° (Exact Right Angle)</span>
    </div>
  </div>
</div>
""",

    "sulba_sutra_altar_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-amber-500 animate-pulse"></span>
      <h4 class="font-bold text-amber-400 text-sm sm:text-base">Simulator 4: Kātyāyana Śulba-Sūtra Altar & Cord Geometry</h4>
    </div>
    <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Vedic Rope Geometry</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Ancient Indian cord geometry: Tying cords at pegs $A$ and $B$ along the solar East-West <span class="font-bold text-amber-300">Prācī</span>, pulling a central knot to construct the North-South meridian and sacred altar outlines!</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="sulbaSvg" viewBox="0 0 500 300" class="w-full h-full select-none"></svg>
  </div>

  <div class="flex flex-wrap items-center justify-between gap-2 mt-3">
    <div class="flex items-center space-x-2">
      <button id="sulbaAltarBtn1" class="px-3 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-xs font-semibold text-white transition">Āhavanīya (Square)</button>
      <button id="sulbaAltarBtn2" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 transition">Gārhapatya (Circle)</button>
      <button id="sulbaAnimateBtn" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-300 transition">▶ Stretch Cord</button>
    </div>
    <div class="text-xs text-slate-300">
      Cardinal Axis: <span class="text-amber-400 font-bold">East-West Prācī ⇄ North-South Meridian</span>
    </div>
  </div>
</div>
""",

    "angle_bisector_studio_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-violet-400 animate-pulse"></span>
      <h4 class="font-bold text-violet-300 text-sm sm:text-base">Simulator 5: Angle Bisector Studio with Dynamic Protractor</h4>
    </div>
    <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-violet-500/20 text-violet-300 border border-violet-500/30">SSS Congruence</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Adjust the opening angle of $\\angle AOB$. The compass strikes equal arcs on both arms and intersecting arcs inside to generate the exact angle bisector ray $OC$!</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="bisectorSvg" viewBox="0 0 500 300" class="w-full h-full select-none"></svg>
  </div>

  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-3">
    <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800">
      <label class="block text-xs font-semibold text-slate-300 mb-1 flex justify-between">
        <span>Angle ∠AOB:</span>
        <span id="bisectorAngleVal" class="text-violet-400 font-bold font-mono">70°</span>
      </label>
      <input type="range" id="bisectorAngleSlider" min="20" max="150" value="70" class="w-full accent-violet-500 cursor-pointer">
    </div>
    <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800 flex items-center justify-between text-xs">
      <div>
        <div class="text-slate-400">Bisected Halves:</div>
        <div class="text-emerald-400 font-bold font-mono text-sm" id="bisectorHalfVal">∠AOC = ∠BOC = 35.0°</div>
      </div>
      <div class="text-right text-[11px] text-slate-400">
        Proof: △OPC ≅ △OQC (SSS)
      </div>
    </div>
  </div>
</div>
""",

    "mandala_rosette_generator_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-rose-400 animate-pulse"></span>
      <h4 class="font-bold text-rose-300 text-sm sm:text-base">Simulator 6: Multi-Petalled Floral Rosette & Mandala Generator</h4>
    </div>
    <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">Kolam & Rangoli Geometry</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Repeated angle bisection ($360° \\to 180° \\to 90° \\to 45° \\to 22.5°$) generates radial symmetry axes for drawing traditional Indian flower rosettes and Yantras with compass arcs!</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="mandalaSvg" viewBox="0 0 500 300" class="w-full h-full select-none"></svg>
  </div>

  <div class="flex flex-wrap items-center justify-between gap-2 mt-3">
    <div class="flex items-center space-x-2">
      <span class="text-xs text-slate-300">Petals:</span>
      <button class="mandalaPetalBtn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-rose-900/40 text-xs font-bold text-slate-200 transition" data-petals="6">6</button>
      <button class="mandalaPetalBtn px-2.5 py-1 rounded-lg bg-rose-600 text-xs font-bold text-white transition" data-petals="8">8</button>
      <button class="mandalaPetalBtn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-rose-900/40 text-xs font-bold text-slate-200 transition" data-petals="12">12</button>
      <button class="mandalaPetalBtn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-rose-900/40 text-xs font-bold text-slate-200 transition" data-petals="16">16</button>
    </div>
    <label class="flex items-center space-x-2 text-xs text-slate-300 cursor-pointer">
      <input type="checkbox" id="mandalaGuidesToggle" checked class="accent-rose-500">
      <span>Show Compass Construction Arcs</span>
    </label>
  </div>
</div>
""",

    "angle_copier_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-teal-400 animate-pulse"></span>
      <h4 class="font-bold text-teal-300 text-sm sm:text-base">Simulator 7: Copying an Angle via Congruent Isosceles Triangles</h4>
    </div>
    <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30">Angle Duplicator</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Copying angle $\\angle O$ from the left to vertex $P$ on the right. Capturing the chord distance $XY$ transfers the exact angle measure without using a protractor!</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="angleCopierSvg" viewBox="0 0 500 300" class="w-full h-full select-none"></svg>
  </div>

  <div class="flex flex-wrap items-center justify-between gap-2 mt-3">
    <div class="flex items-center space-x-2">
      <button id="copyAngleStepBtn" class="px-3 py-1.5 rounded-lg bg-teal-600 hover:bg-teal-500 text-xs font-semibold text-white transition">Next Construction Arc ▶</button>
      <button id="copyAngleResetBtn" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-400 transition">↺ Reset</button>
    </div>
    <div class="text-xs font-mono text-teal-300">
      Original: <span id="copyOriginalAngle">52°</span> | Copied: <span id="copyCopiedAngle">52°</span> (SSS Match)
    </div>
  </div>
</div>
""",

    "parallel_line_transversal_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-blue-400 animate-pulse"></span>
      <h4 class="font-bold text-blue-300 text-sm sm:text-base">Simulator 8: Parallel Line Constructor via Corresponding Angles</h4>
    </div>
    <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30">Line m ∥ Line L</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Drag point <span class="font-bold text-amber-300">P</span> vertically or adjust the transversal angle. Equal corresponding angles $\\angle 1 = \\angle 2$ ensure line $m$ stays strictly parallel to line $L$!</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="parallelSvg" viewBox="0 0 500 300" class="w-full h-full select-none cursor-ns-resize"></svg>
  </div>

  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-3">
    <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800">
      <label class="block text-xs font-semibold text-slate-300 mb-1 flex justify-between">
        <span>Transversal Angle θ:</span>
        <span id="parallelAngleVal" class="text-blue-400 font-bold font-mono">55°</span>
      </label>
      <input type="range" id="parallelAngleSlider" min="30" max="80" value="55" class="w-full accent-blue-500 cursor-pointer">
    </div>
    <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800 flex items-center justify-between text-xs">
      <span class="text-slate-300">Corresponding Angles:</span>
      <span class="text-emerald-400 font-bold font-mono">∠1 = ∠2 = <span id="parallelAngleMatch">55.0°</span> (m ∥ L)</span>
    </div>
  </div>
</div>
""",

    "historic_arch_architect_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
      <h4 class="font-bold text-amber-300 text-sm sm:text-base">Simulator 9: Historic Arch Geometry: Trefoil & Pointed Arches</h4>
    </div>
    <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Red Fort Diwan-i-Aam</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Deconstruct heritage arches into their underlying compass circles, center vertices, and intersecting arc radii:</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="archSvg" viewBox="0 0 500 300" class="w-full h-full select-none"></svg>
  </div>

  <div class="flex flex-wrap items-center justify-between gap-2 mt-3">
    <div class="flex items-center space-x-2">
      <button class="archTypeBtn px-3 py-1.5 rounded-lg bg-amber-600 text-xs font-semibold text-white transition" data-type="trefoil">Trefoil (3-Lobe) Arch</button>
      <button class="archTypeBtn px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 transition" data-type="pointed">Equilateral Pointed Arch</button>
      <button class="archTypeBtn px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 transition" data-type="ogee">Ogee (S-Curve) Arch</button>
    </div>
    <label class="flex items-center space-x-2 text-xs text-slate-300 cursor-pointer">
      <input type="checkbox" id="archCentersToggle" checked class="accent-amber-500">
      <span>Show Arc Centers & Radii</span>
    </label>
  </div>
</div>
""",

    "equilateral_60_constructor_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
      <h4 class="font-bold text-emerald-300 text-sm sm:text-base">Simulator 10: Constructing a 60° Angle & Equilateral Triangle</h4>
    </div>
    <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Side = Radius (r)</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Striking an arc of radius $r$ from $O$, then striking an intersecting arc of the <em>same radius</em> $r$ from $A$ yields vertex $B$. All sides equal $r$, guaranteeing $\\angle AOB = 60.0°$!</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="equilateral60Svg" viewBox="0 0 500 300" class="w-full h-full select-none"></svg>
  </div>

  <div class="flex flex-wrap items-center justify-between gap-2 mt-3">
    <div class="flex items-center space-x-2">
      <button id="eq60StepBtn" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-xs font-semibold text-white transition">Next Construction Step ▶</button>
      <button id="eq60ResetBtn" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-400 transition">↺ Reset</button>
    </div>
    <div class="text-xs font-mono text-emerald-300 bg-slate-950/80 px-3 py-1.5 rounded-lg border border-slate-800">
      Sides: OA = AB = OB = r | Angles: 60° - 60° - 60°
    </div>
  </div>
</div>
""",

    "angle_hierarchy_shatkona_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-purple-400 animate-pulse"></span>
      <h4 class="font-bold text-purple-300 text-sm sm:text-base">Simulator 11: Angle Hierarchy & Shatkona (6-Pointed Star)</h4>
    </div>
    <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">Hexagram Geometry</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Explore constructible angles ($15°, 30°, 45°, 60°, 75°, 90°, 105°$) or superimpose two inverted equilateral triangles to construct the ancient 6-pointed Shatkona!</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="shatkonaSvg" viewBox="0 0 500 300" class="w-full h-full select-none"></svg>
  </div>

  <div class="flex flex-wrap items-center justify-between gap-2 mt-3">
    <div class="flex items-center space-x-1.5">
      <button class="angleChoiceBtn px-2 py-1 rounded bg-slate-800 hover:bg-purple-900/40 text-xs font-mono text-slate-200 transition" data-deg="15">15°</button>
      <button class="angleChoiceBtn px-2 py-1 rounded bg-slate-800 hover:bg-purple-900/40 text-xs font-mono text-slate-200 transition" data-deg="30">30°</button>
      <button class="angleChoiceBtn px-2 py-1 rounded bg-slate-800 hover:bg-purple-900/40 text-xs font-mono text-slate-200 transition" data-deg="45">45°</button>
      <button class="angleChoiceBtn px-2 py-1 rounded bg-slate-800 hover:bg-purple-900/40 text-xs font-mono text-slate-200 transition" data-deg="60">60°</button>
      <button class="angleChoiceBtn px-2 py-1 rounded bg-slate-800 hover:bg-purple-900/40 text-xs font-mono text-slate-200 transition" data-deg="75">75°</button>
      <button class="angleChoiceBtn px-2 py-1 rounded bg-slate-800 hover:bg-purple-900/40 text-xs font-mono text-slate-200 transition" data-deg="105">105°</button>
    </div>
    <button id="toggleShatkonaStarBtn" class="px-3 py-1.5 rounded-lg bg-purple-600 hover:bg-purple-500 text-xs font-semibold text-white transition">★ Shatkona Star</button>
  </div>
</div>
""",

    "regular_hexagon_stepper_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-cyan-400 animate-pulse"></span>
      <h4 class="font-bold text-cyan-300 text-sm sm:text-base">Simulator 12: Regular Hexagon: Stepping the Radius (6 × 60° = 360°)</h4>
    </div>
    <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">6 Equilateral Triangles</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Step the compass around the circle circumference with radius $r$. Exactly 6 steps close the circle, proving that six equilateral triangles meet around center $O$ without gaps!</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="hexagonSvg" viewBox="0 0 500 300" class="w-full h-full select-none"></svg>
  </div>

  <div class="flex flex-wrap items-center justify-between gap-2 mt-3">
    <div class="flex items-center space-x-2">
      <button id="hexStepBtn" class="px-3 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-xs font-semibold text-white transition">Step Radius Arc ▶</button>
      <button id="hexResetBtn" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-400 transition">↺ Reset</button>
    </div>
    <div class="text-xs font-mono text-cyan-300">
      Steps: <span id="hexStepCount">0</span>/6 | Central Angle: <span id="hexAngleSum">0°</span>/360°
    </div>
  </div>
</div>
""",

    "tangram_tessellation_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-indigo-400 animate-pulse"></span>
      <h4 class="font-bold text-indigo-300 text-sm sm:text-base">Simulator 13: 7-Piece Tangram Tiling & Conservation of Area</h4>
    </div>
    <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Total Area = 1.0</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Assemble the 7 pieces into a Square, a Candle, or a Swan. Notice how area is strictly conserved under rigid rotations and translations!</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="tangramSvg" viewBox="0 0 500 300" class="w-full h-full select-none"></svg>
  </div>

  <div class="flex flex-wrap items-center justify-between gap-2 mt-3">
    <div class="flex items-center space-x-2">
      <button class="tangramShapeBtn px-3 py-1.5 rounded-lg bg-indigo-600 text-xs font-semibold text-white transition" data-shape="square">Square</button>
      <button class="tangramShapeBtn px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 transition" data-shape="candle">Candle</button>
      <button class="tangramShapeBtn px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 transition" data-shape="swan">Swan</button>
    </div>
    <div class="text-xs text-slate-300 font-mono">
      Pieces: 5 Triangles + 1 Square + 1 Parallelogram = Area 100%
    </div>
  </div>
</div>
""",

    "domino_grid_tiling_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
      <h4 class="font-bold text-emerald-300 text-sm sm:text-base">Simulator 14: Grid Tiling with 2×1 Dominoes & Area Parity</h4>
    </div>
    <span id="dominoParityBadge" class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Tilable (Area Even)</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Adjust grid dimensions $m \\times n$. Each domino covers 2 squares. If total area $m \\times n$ is odd, tiling is mathematically impossible!</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="dominoSvg" viewBox="0 0 500 300" class="w-full h-full select-none"></svg>
  </div>

  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-3">
    <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800 flex items-center space-x-4">
      <div class="flex-1">
        <label class="block text-xs font-semibold text-slate-300 mb-1">Rows m: <span id="dominoRowsVal" class="text-emerald-400 font-bold">4</span></label>
        <input type="range" id="dominoRowsSlider" min="2" max="6" value="4" class="w-full accent-emerald-500 cursor-pointer">
      </div>
      <div class="flex-1">
        <label class="block text-xs font-semibold text-slate-300 mb-1">Cols n: <span id="dominoColsVal" class="text-emerald-400 font-bold">6</span></label>
        <input type="range" id="dominoColsSlider" min="2" max="6" value="6" class="w-full accent-emerald-500 cursor-pointer">
      </div>
    </div>
    <div class="bg-slate-950/70 p-2.5 rounded-xl border border-slate-800 flex flex-col justify-center text-xs space-y-1">
      <div class="flex justify-between text-slate-300">
        <span>Total Cells:</span>
        <span id="dominoTotalCells" class="font-bold text-amber-300 font-mono">24 cells</span>
      </div>
      <div class="flex justify-between text-slate-300">
        <span>Tiling Status:</span>
        <span id="dominoStatusText" class="font-bold text-emerald-400 font-mono">Possible (12 dominoes)</span>
      </div>
    </div>
  </div>
</div>
""",

    "mutilated_chessboard_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-rose-400 animate-pulse"></span>
      <h4 class="font-bold text-rose-300 text-sm sm:text-base">Simulator 15: The Mutilated Chessboard & Coloring Invariant</h4>
    </div>
    <span id="chessboardBadge" class="px-2 py-0.5 rounded text-[11px] font-bold bg-slate-700 text-slate-300 border border-slate-600">Full 8×8 Board</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Every $2 \\times 1$ domino covers 1 white and 1 black square. Toggle "Remove Opposite Corners" to see why a 62-square board can NEVER be tiled!</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="chessboardSvg" viewBox="0 0 500 300" class="w-full h-full select-none"></svg>
  </div>

  <div class="flex flex-wrap items-center justify-between gap-2 mt-3">
    <button id="toggleMutilatedBtn" class="px-3.5 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-500 text-xs font-semibold text-white transition">✂ Cut Diagonally Opposite Corners</button>
    <div class="flex items-center space-x-3 text-xs font-mono">
      <span class="text-slate-100">White: <strong id="whiteCellCount" class="text-slate-100">32</strong></span>
      <span class="text-slate-400">Black: <strong id="blackCellCount" class="text-amber-400">32</strong></span>
      <span id="parityVerdict" class="text-emerald-400 font-bold">Balanced (32W = 32B)</span>
    </div>
  </div>
</div>
""",

    "master_tessellation_studio_sim": """
<div class="p-4 bg-slate-900/90 rounded-2xl border border-slate-700/60 shadow-xl text-slate-100">
  <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-700/60">
    <div class="flex items-center space-x-2">
      <span class="w-3 h-3 rounded-full bg-amber-400 animate-pulse"></span>
      <h4 class="font-bold text-amber-300 text-sm sm:text-base">Simulator 16: Master Tessellation Studio: Triangles, Squares, Hexagons & Honeycomb</h4>
    </div>
    <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">Vertex Angle = 360°</span>
  </div>
  <p class="text-xs text-slate-300 mb-3">Only three regular polygons tile the Euclidean plane. Test why pentagons leave a 36° gap, and compare perimeter efficiency (Honeycomb Theorem)!</p>
  
  <div class="relative w-full h-64 sm:h-72 bg-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center">
    <svg id="tessellationSvg" viewBox="0 0 500 300" class="w-full h-full select-none"></svg>
  </div>

  <div class="flex flex-wrap items-center justify-between gap-2 mt-3">
    <div class="flex items-center space-x-1.5">
      <button class="tessTypeBtn px-2.5 py-1.5 rounded-lg bg-amber-600 text-xs font-semibold text-white transition" data-type="hex">Hexagons (3×120°)</button>
      <button class="tessTypeBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 transition" data-type="square">Squares (4×90°)</button>
      <button class="tessTypeBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 transition" data-type="triangle">Triangles (6×60°)</button>
      <button class="tessTypeBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-rose-900/40 text-xs font-semibold text-rose-300 transition" data-type="pentagon">Pentagons (Fail!)</button>
    </div>
    <div class="text-xs font-mono text-amber-300" id="tessAngleReadout">
      3 × 120° = 360° (0° gap) | Honeycomb Optimal
    </div>
  </div>
</div>
"""
}

if __name__ == "__main__":
    with open(".agents/class7_math_constructions_sims.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Class 7 Mathematics Chapter 6: Constructions and Tilings Simulators"""\n\n')
        f.write("SIMULATORS_HTML = " + repr(SIMULATORS_HTML) + "\n")
    print(f"Generated .agents/class7_math_constructions_sims.py with {len(SIMULATORS_HTML)} simulators.")

