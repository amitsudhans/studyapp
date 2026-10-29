# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Science Chapter 1: The Ever-Evolving World of Science
Simulator templates: 16 bespoke SVG/HTML interactive labs
"""

SIMULATORS = {
    # 1. Scientific Inquiry Cycle
    "inquiry_cycle": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-amber-400">Lab Simulator 1</span>
            <h3 class="text-sm font-bold text-slate-100">The Scientific Inquiry Cycle</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-amber-500/20 text-amber-300 border border-amber-500/30 font-semibold" id="cycleStepBadge">Step 1: Observation</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="cycleSvg" viewBox="0 0 500 280" class="w-full h-auto max-h-[250px]"></svg>
        </div>

        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300" id="cycleDetailBox">
          <div class="font-bold text-amber-300 mb-0.5" id="cycleStepTitle">1. Careful Observation</div>
          <div id="cycleStepDesc">Using human senses and precision instruments to observe natural phenomena without prejudice. Example: Alexander Fleming noticing clear halos around penicillium mold in a bacterial plate.</div>
        </div>

        <div class="grid grid-cols-6 gap-1 pt-1">
          <button data-step="1" class="cycleBtn px-2 py-1.5 rounded-lg bg-amber-600 text-white text-[11px] font-bold transition">1. Observe</button>
          <button data-step="2" class="cycleBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] font-bold transition">2. Question</button>
          <button data-step="3" class="cycleBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] font-bold transition">3. Hypothesize</button>
          <button data-step="4" class="cycleBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] font-bold transition">4. Experiment</button>
          <button data-step="5" class="cycleBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] font-bold transition">5. Analyze</button>
          <button data-step="6" class="cycleBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] font-bold transition">6. Refine</button>
        </div>
      </div>
    """,

    # 2. Paper Plane Aerodynamics
    "flight_aerodynamics": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-cyan-400">Lab Simulator 2</span>
            <h3 class="text-sm font-bold text-slate-100">Paper Plane Aerodynamics & Lift</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 font-semibold" id="flightStatus">Level Glide ✔</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="planeSvg" viewBox="0 0 500 260" class="w-full h-auto max-h-[240px]"></svg>
        </div>

        <div class="grid grid-cols-2 gap-3 text-xs">
          <div>
            <div class="flex justify-between text-slate-400 mb-1">
              <span>Angle of Attack:</span>
              <span id="aoaVal" class="text-amber-400 font-mono font-bold">8°</span>
            </div>
            <input type="range" id="aoaSlider" min="-5" max="30" value="8" step="1" class="w-full accent-amber-500 cursor-pointer">
          </div>
          <div>
            <div class="flex justify-between text-slate-400 mb-1">
              <span>Launch Velocity:</span>
              <span id="velVal" class="text-cyan-400 font-mono font-bold">6 m/s</span>
            </div>
            <input type="range" id="velSlider" min="2" max="12" value="6" step="0.5" class="w-full accent-cyan-500 cursor-pointer">
          </div>
        </div>

        <div class="p-2 rounded-xl bg-slate-950 border border-slate-800 flex items-center justify-between text-[11px] font-mono">
          <span class="text-emerald-400 font-bold" id="liftReadout">Lift: 0.52 N</span>
          <span class="text-amber-400 font-bold" id="weightReadout">Weight: 0.50 N</span>
          <span class="text-cyan-400 font-bold" id="thrustReadout">Thrust: 0.40 N</span>
          <span class="text-rose-400 font-bold" id="dragReadout">Drag: 0.38 N</span>
        </div>
      </div>
    """,

    # 3. Cosmic Zoom Scale
    "cosmic_scale_slider": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-purple-400">Lab Simulator 3</span>
            <h3 class="text-sm font-bold text-slate-100">Cosmic Zoom: Micro to Macro</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-purple-500/20 text-purple-300 border border-purple-500/30 font-semibold" id="scaleOrder">10^-6 m (Microscale)</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="scaleSvg" viewBox="0 0 500 260" class="w-full h-auto max-h-[240px]"></svg>
        </div>

        <div class="space-y-1">
          <div class="flex justify-between text-xs text-slate-400">
            <span>Sub-atomic (10^-10m)</span>
            <span class="text-purple-400 font-bold" id="scaleDimension">Plant Cell (~50 µm)</span>
            <span>Cosmic (10^21m)</span>
          </div>
          <input type="range" id="scaleSlider" min="0" max="6" value="2" step="1" class="w-full accent-purple-500 cursor-pointer">
        </div>

        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300" id="scaleDescription">
          Microscopic world: Optical light microscopes allow us to observe living plant and animal cells, chloroplasts generating sugars, and single-celled bacteria.
        </div>
      </div>
    """,

    # 4. Scientific Mindset Sorter
    "scientific_mindset_sorter": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-emerald-400">Lab Simulator 4</span>
            <h3 class="text-sm font-bold text-slate-100">Fact vs Opinion vs Hypothesis</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold">Mindset Lab</span>
        </div>

        <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 min-h-[90px] flex flex-col justify-center">
          <div class="text-[11px] text-slate-400 uppercase tracking-wider font-bold mb-1">Evaluate This Statement:</div>
          <div id="mindsetStatement" class="text-xs sm:text-sm font-semibold text-amber-300">"Water boils at 100°C at 1 atmosphere pressure."</div>
        </div>

        <div class="grid grid-cols-3 gap-2">
          <button data-type="fact" class="mindsetChoiceBtn px-3 py-2 rounded-xl bg-slate-800 hover:bg-emerald-950 hover:border-emerald-500 border border-slate-700 text-xs font-bold text-slate-200 transition">
            1. Scientific Fact
          </button>
          <button data-type="opinion" class="mindsetChoiceBtn px-3 py-2 rounded-xl bg-slate-800 hover:bg-amber-950 hover:border-amber-500 border border-slate-700 text-xs font-bold text-slate-200 transition">
            2. Personal Opinion
          </button>
          <button data-type="hypothesis" class="mindsetChoiceBtn px-3 py-2 rounded-xl bg-slate-800 hover:bg-cyan-950 hover:border-cyan-500 border border-slate-700 text-xs font-bold text-slate-200 transition">
            3. Testable Hypothesis
          </button>
        </div>

        <div id="mindsetFeedback" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-snug">
          Click a button above to evaluate whether this statement is a Fact, Opinion, or Hypothesis.
        </div>

        <div class="flex justify-end">
          <button id="nextStatementBtn" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 transition">
            Next Statement ➔
          </button>
        </div>
      </div>
    """,

    # 5. Question the Answer (Milk Edition)
    "question_the_answer_milk": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-amber-400">Lab Simulator 5</span>
            <h3 class="text-sm font-bold text-slate-100">Activity 1.1: Question the Answer!</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-amber-500/20 text-amber-300 border border-amber-500/30 font-semibold">Answer: "Just add some milk!"</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="milkSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-3 gap-2">
          <button data-mode="capsaicin" class="milkModeBtn px-2.5 py-1.5 rounded-lg bg-amber-600 text-white text-xs font-bold transition">1. Chili Burn (Casein)</button>
          <button data-mode="tyndall" class="milkModeBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold transition">2. Tyndall Scattering</button>
          <button data-mode="curd" class="milkModeBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold transition">3. Bacterial Curd</button>
        </div>

        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300" id="milkExplanation">
          <strong>Question:</strong> <em>Why does milk relieve hot chili burn while water fails?</em><br>
          Chili heat comes from oily capsaicin. Water cannot dissolve non-polar oil, but casein phosphoprotein in milk acts like a biological soap, binding capsaicin and stripping it from receptors!
        </div>
      </div>
    """,

    # 6. Raindrop Optics 42
    "raindrop_optics_42": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-cyan-400">Lab Simulator 6</span>
            <h3 class="text-sm font-bold text-slate-100">The 42° Geometry of Rainbows</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 font-semibold" id="rainbowAngleReadout">Exit Angle: 42.0°</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="raindropSvg" viewBox="0 0 500 250" class="w-full h-auto max-h-[230px]"></svg>
        </div>

        <div class="space-y-1">
          <div class="flex justify-between text-xs text-slate-400">
            <span>Ray Impact Parameter (h/R):</span>
            <span id="impactVal" class="text-cyan-400 font-mono font-bold">0.86 (Caustic Focus)</span>
          </div>
          <input type="range" id="impactSlider" min="0.1" max="0.95" value="0.86" step="0.01" class="w-full accent-cyan-500 cursor-pointer">
        </div>

        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 flex items-center justify-between">
          <span>Red Wavelength ($\lambda = 650\text{nm}$): <strong>42.0°</strong></span>
          <span>Violet Wavelength ($\lambda = 400\text{nm}$): <strong>40.4°</strong></span>
        </div>
      </div>
    """,

    # 7. Physical vs Chemical Reactor
    "physical_chemical_reactor": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-rose-400">Lab Simulator 7</span>
            <h3 class="text-sm font-bold text-slate-100">Physical vs Chemical Change Reactor</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold" id="reactionBadge">Chemical Change</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="reactorSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-4 gap-1.5 text-xs">
          <button data-reaction="ice" class="reactBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">1. Ice Melting</button>
          <button data-reaction="sugar" class="reactBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">2. Sugar Solution</button>
          <button data-reaction="vinegar" class="reactBtn px-2 py-1.5 rounded-lg bg-rose-600 text-white font-bold transition">3. Vinegar+Soda</button>
          <button data-reaction="rust" class="reactBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">4. Iron Rusting</button>
        </div>

        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300" id="reactionDesc">
          <strong>Vinegar + Baking Soda:</strong> Produces effervescent carbon dioxide gas ($\text{CO}_2$), water, and sodium acetate. A brand-new substance is formed with breaking and reforming of chemical bonds!
        </div>
      </div>
    """,

    # 8. DC Circuit & Electromagnet
    "dc_circuit_electromagnet": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-amber-400">Lab Simulator 8</span>
            <h3 class="text-sm font-bold text-slate-100">DC Circuit & Electromagnet Sandbox</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" id="circuitStatus">Circuit: CLOSED (ON)</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="circuitSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="flex items-center justify-between pt-1">
          <button id="toggleSwitchBtn" class="px-4 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition shadow-md shadow-amber-600/30">
            Toggle Switch (Open/Close)
          </button>
          <div class="text-xs text-slate-400 font-mono" id="compassReading">Compass Deflection: 45° E (Field Active)</div>
        </div>
      </div>
    """,

    # 9. Light, Shadows & Eclipse
    "eclipse_shadow_caster": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-indigo-400">Lab Simulator 9</span>
            <h3 class="text-sm font-bold text-slate-100">Light, Shadows & Cosmic Eclipses</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 font-semibold" id="eclipseTitle">Total Solar Eclipse</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="eclipseSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="space-y-1">
          <div class="flex justify-between text-xs text-slate-400">
            <span>Moon Position:</span>
            <span id="moonPosText" class="text-indigo-400 font-mono font-bold">Direct Alignment (Umbra on Earth)</span>
          </div>
          <input type="range" id="moonSlider" min="-80" max="80" value="0" step="2" class="w-full accent-indigo-500 cursor-pointer">
        </div>

        <div class="p-2 rounded-xl bg-slate-950 border border-slate-800 flex items-center justify-between text-[11px] text-slate-300 font-mono">
          <span class="text-amber-300">● Umbra: Total Darkness</span>
          <span class="text-slate-400">◐ Penumbra: Partial Darkness</span>
        </div>
      </div>
    """,

    # 10. Galileo Pendulum
    "galileo_pendulum_lab": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-emerald-400">Lab Simulator 10</span>
            <h3 class="text-sm font-bold text-slate-100">Galileo's Pendulum & Isochronism</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" id="pendulumPeriod">T = 2.01 s</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="pendulumSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-2 gap-3 text-xs">
          <div>
            <div class="flex justify-between text-slate-400 mb-1">
              <span>String Length (L):</span>
              <span id="lenVal" class="text-emerald-400 font-mono font-bold">1.0 m</span>
            </div>
            <input type="range" id="lenSlider" min="0.2" max="2.0" value="1.0" step="0.1" class="w-full accent-emerald-500 cursor-pointer">
          </div>
          <div>
            <div class="flex justify-between text-slate-400 mb-1">
              <span>Gravity Environment:</span>
              <span id="gravVal" class="text-cyan-400 font-mono font-bold">Earth (9.8 m/s²)</span>
            </div>
            <select id="gravSelect" class="w-full p-1.5 rounded-lg bg-slate-950 border border-slate-700 text-xs text-slate-200">
              <option value="9.8">Earth (g = 9.8 m/s²)</option>
              <option value="1.62">Moon (g = 1.62 m/s²)</option>
              <option value="24.79">Jupiter (g = 24.79 m/s²)</option>
            </select>
          </div>
        </div>

        <div class="p-2 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 text-center font-mono">
          Formula: $T = 2\pi \sqrt{L/g}$ | Isochronous (Period is independent of swing width!)
        </div>
      </div>
    """,

    # 11. Photosynthesis Rate Lab
    "photosynthesis_rate_lab": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-green-400">Lab Simulator 11</span>
            <h3 class="text-sm font-bold text-slate-100">Aquatic Plant Photosynthesis Rate</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-green-500/20 text-green-300 border border-green-500/30 font-semibold" id="bubbleRateBadge">Rate: 36 O2 bubbles/min</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="photoSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-2 gap-3 text-xs">
          <div>
            <div class="flex justify-between text-slate-400 mb-1">
              <span>Light Intensity:</span>
              <span id="lightVal" class="text-amber-400 font-mono font-bold">75%</span>
            </div>
            <input type="range" id="lightSlider" min="0" max="100" value="75" step="5" class="w-full accent-amber-500 cursor-pointer">
          </div>
          <div>
            <div class="flex justify-between text-slate-400 mb-1">
              <span>CO2 Concentration:</span>
              <span id="co2Val" class="text-green-400 font-mono font-bold">Moderate</span>
            </div>
            <input type="range" id="co2Slider" min="1" max="3" value="2" step="1" class="w-full accent-green-500 cursor-pointer">
          </div>
        </div>

        <div class="p-2 rounded-xl bg-slate-950 border border-slate-800 text-[11px] text-slate-300 text-center font-mono">
          $6\text{CO}_2 + 6\text{H}_2\text{O} \xrightarrow{\text{light}} \text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2 \uparrow$ (Bubbles collected in inverted funnel)
        </div>
      </div>
    """,

    # 12. Earth Seasons & 23.5° Tilt
    "earth_seasons_orbit": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-cyan-400">Lab Simulator 12</span>
            <h3 class="text-sm font-bold text-slate-100">Earth's 23.5° Tilt & Seasons Orbit</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 font-semibold" id="seasonBadge">June Solstice (Summer in North)</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="seasonsSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="space-y-1">
          <div class="flex justify-between text-xs text-slate-400">
            <span>Orbital Position (Year Journey):</span>
            <span id="orbitDegText" class="text-cyan-400 font-mono font-bold">Month: June (Day 172)</span>
          </div>
          <input type="range" id="orbitSlider" min="0" max="360" value="90" step="5" class="w-full accent-cyan-500 cursor-pointer">
        </div>

        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300" id="seasonDetail">
          <strong>Northern Hemisphere:</strong> Tilting toward the Sun; sun rays strike at a steep vertical angle. Longest daylight hours of the year!
        </div>
      </div>
    """,

    # 13. Sustainability Energy Dashboard
    "sustainability_energy_dashboard": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-emerald-400">Lab Simulator 13</span>
            <h3 class="text-sm font-bold text-slate-100">Clean Energy & Carbon Dashboard</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" id="climateStatus">Target < 1.5°C Achieved! ✔</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="sustainSvg" viewBox="0 0 500 230" class="w-full h-auto max-h-[210px]"></svg>
        </div>

        <div class="space-y-1">
          <div class="flex justify-between text-xs text-slate-400">
            <span>Renewable Energy Share (Solar/Wind/Hydro):</span>
            <span id="renewShareVal" class="text-emerald-400 font-mono font-bold">80% Clean</span>
          </div>
          <input type="range" id="renewSlider" min="10" max="100" value="80" step="5" class="w-full accent-emerald-500 cursor-pointer">
        </div>

        <div class="grid grid-cols-2 gap-2 text-xs font-mono">
          <div class="p-2 rounded-xl bg-slate-950 border border-slate-800 text-slate-300">
            CO2 Emissions: <span class="text-emerald-400 font-bold" id="emissionsVal">7.2 Gt/yr</span>
          </div>
          <div class="p-2 rounded-xl bg-slate-950 border border-slate-800 text-slate-300">
            Warming: <span class="text-cyan-400 font-bold" id="warmingVal">+1.4°C</span>
          </div>
        </div>
      </div>
    """,

    # 14. Precision Measurement & Parallax
    "meniscus_parallax_bench": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-blue-400">Lab Simulator 14</span>
            <h3 class="text-sm font-bold text-slate-100">Meniscus & Parallax Error Bench</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-blue-500/20 text-blue-300 border border-blue-500/30 font-semibold" id="parallaxStatus">True Eye Level (Correct!)</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="meniscusSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="space-y-1">
          <div class="flex justify-between text-xs text-slate-400">
            <span>Observer Eye Position:</span>
            <span id="eyePosText" class="text-blue-400 font-mono font-bold">Perpendicular to Meniscus (0°)</span>
          </div>
          <input type="range" id="eyeSlider" min="-30" max="30" value="0" step="2" class="w-full accent-blue-500 cursor-pointer">
        </div>

        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 flex justify-between items-center font-mono">
          <span>Actual True Volume: <strong class="text-emerald-400">50.0 mL</strong></span>
          <span>Apparent Reading: <strong class="text-amber-400" id="apparentVol">50.0 mL</strong></span>
        </div>
      </div>
    """,

    # 15. Indian Scientists Timeline
    "indian_pioneers_timeline": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-amber-400">Lab Simulator 15</span>
            <h3 class="text-sm font-bold text-slate-100">Giants of Modern Indian Science</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-amber-500/20 text-amber-300 border border-amber-500/30 font-semibold" id="pioneerBadge">Sir C.V. Raman (1930)</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="pioneerSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="grid grid-cols-4 gap-1.5 text-xs">
          <button data-pioneer="jcbose" class="pioneerBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">1. J.C. Bose</button>
          <button data-pioneer="cvraman" class="pioneerBtn px-2 py-1.5 rounded-lg bg-amber-600 text-white font-bold transition">2. C.V. Raman</button>
          <button data-pioneer="sarabhai" class="pioneerBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">3. V. Sarabhai</button>
          <button data-pioneer="kalam" class="pioneerBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition">4. A.P.J. Kalam</button>
        </div>
      </div>
    """,

    # 16. Young Scientist Constellation
    "young_scientist_constellation": r"""
      <div class="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between pb-2 border-b border-slate-800">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-wider text-cyan-400">Lab Simulator 16</span>
            <h3 class="text-sm font-bold text-slate-100">Young Scientist Constellation Map</h3>
          </div>
          <span class="px-2 py-0.5 rounded text-[11px] font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 font-semibold" id="constellationBadge">Living World</span>
        </div>

        <div class="w-full bg-slate-950 rounded-xl p-2 border border-slate-800 flex items-center justify-center">
          <svg id="constellationSvg" viewBox="0 0 500 240" class="w-full h-auto max-h-[220px]"></svg>
        </div>

        <div class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300" id="constellationDetail">
          <strong>The Living World (Biology):</strong> Photosynthesis in chloroplasts, plant vascular tissues (xylem and phloem), human respiration, and the ecology of micro-organisms.
        </div>
      </div>
    """
}

with open(".agents/class7_science_ever_evolving_world_sims.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 7 Science Chapter 1: The Ever-Evolving World of Science Simulator Templates"""\n\n')
    f.write("SIMULATORS_HTML = " + repr(SIMULATORS) + "\n")

print(f"Generated .agents/class7_science_ever_evolving_world_sims.py with {len(SIMULATORS)} simulators.")

