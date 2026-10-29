#!/usr/bin/env python3
"""
Generates the 16 interactive SVG/HTML laboratory simulator templates for:
NCERT Class 7 Mathematics - Chapter 5: Connecting the Dots...
"""

SIMULATORS = {
    # 1. Statistical Questions Classifier
    "sim-questions-classifier": """
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Lab 1 • Question Classifier</span>
      <span id="qc-score-pill" class="px-2.5 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 font-mono text-xs font-bold">Score: 0 / 6</span>
    </div>
    <p class="text-xs text-slate-300 mb-3">Does the question anticipate variability across a population, or does it have a single fixed factual answer?</p>

    <!-- Card to classify -->
    <div class="p-4 bg-slate-800/80 rounded-xl border border-slate-700 text-center mb-4 min-h-[75px] flex flex-col items-center justify-center">
      <div id="qc-card-text" class="text-sm font-semibold text-amber-200">"How many books did each student in your class read this summer?"</div>
      <div id="qc-card-hint" class="text-[11px] text-slate-400 mt-1">Consider: Will the answer vary from student to student?</div>
    </div>

    <!-- Drop/Click Zones -->
    <div class="grid grid-cols-2 gap-3 mb-3">
      <button id="qc-btn-nonstat" class="p-3 rounded-xl border border-rose-500/40 bg-rose-950/20 hover:bg-rose-900/30 text-rose-300 text-xs font-bold flex flex-col items-center justify-center gap-1 transition-all">
        <span class="text-base">❌</span>
        <span>Non-Statistical</span>
        <span class="text-[10px] text-slate-400 font-normal">Single fixed fact</span>
      </button>

      <button id="qc-btn-stat" class="p-3 rounded-xl border border-emerald-500/40 bg-emerald-950/20 hover:bg-emerald-900/30 text-emerald-300 text-xs font-bold flex flex-col items-center justify-center gap-1 transition-all">
        <span class="text-base">✓</span>
        <span>Statistical</span>
        <span class="text-[10px] text-slate-400 font-normal">Expects variability</span>
      </button>
    </div>

    <div id="qc-feedback" class="p-2 rounded-lg text-xs text-center min-h-[36px] flex items-center justify-center bg-slate-950/60 border border-slate-800 text-slate-300">
      Click a category above to classify the displayed question.
    </div>
  </div>

  <div class="flex justify-between items-center pt-2 border-t border-slate-800 text-[11px] text-slate-400">
    <span>Question <span id="qc-idx" class="font-bold text-indigo-300">1</span> of 6</span>
    <button id="qc-btn-next" class="px-3 py-1 rounded bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs">Next Card →</button>
  </div>
</div>
""",

    # 2. Statistical Statements Analyzer
    "sim-statements-analyzer": """
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider">Lab 2 • Statement Detective</span>
      <span class="text-[11px] text-slate-400 font-mono">Sample Size Effect</span>
    </div>
    <p class="text-xs text-slate-300 mb-3">Adjust the sample size of surveyed families and observe how reliable the statistical claim becomes.</p>

    <div class="p-3 bg-slate-800/80 rounded-xl border border-slate-700 mb-3">
      <div class="text-xs font-bold text-cyan-300 mb-1">Claim: "60% of Households in Town X Own a Solar Water Heater"</div>
      <div class="flex items-center justify-between text-xs text-slate-300 mt-2">
        <span>Survey Sample Size ($n$):</span>
        <span id="sa-sample-val" class="font-bold font-mono text-amber-300 text-sm">20 households</span>
      </div>
      <input id="sa-sample-slider" type="range" min="5" max="500" step="5" value="20" class="w-full mt-2 accent-cyan-400">
      <div class="flex justify-between text-[10px] text-slate-500">
        <span>5 (Tiny)</span>
        <span>50 (Moderate)</span>
        <span>250 (Strong)</span>
        <span>500 (Robust)</span>
      </div>
    </div>

    <!-- Visual Representation of Survey Reliability -->
    <div class="p-3 bg-slate-950/60 rounded-xl border border-slate-800 text-xs">
      <div class="flex justify-between items-center mb-1">
        <span class="text-slate-400">Margin of Error (Uncertainty):</span>
        <span id="sa-error-val" class="font-mono font-bold text-rose-400">±22.4%</span>
      </div>
      <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden mb-2">
        <div id="sa-error-bar" class="bg-rose-500 h-full" style="width: 75%;"></div>
      </div>
      <div class="flex justify-between items-center">
        <span class="text-slate-400">Credibility Verdict:</span>
        <span id="sa-verdict" class="font-bold text-amber-400">Unreliable (Tiny sample can swing widely)</span>
      </div>
    </div>
  </div>

  <div class="p-2.5 bg-cyan-950/20 border border-cyan-800/40 rounded-xl text-[11px] text-slate-300">
    💡 <b>Rule of Sample Sizes:</b> As sample size grows from $5$ to $500$, random errors cancel out, narrowing the margin of error and anchoring the claim to reality.
  </div>
</div>
""",

    # 3. Fair-Share Balancer (Samamiti / Samīkaraṇa)
    "sim-fair-share-balancer": r"""
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Lab 3 • The Fair-Share Equaliser (Samamiti)</span>
      <button id="fs-btn-reset" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]">Reset</button>
    </div>
    <p class="text-xs text-slate-300 mb-2">Four friends have unequal stacks of blocks. Click "Level Shares" to see how the arithmetic mean balances them all!</p>

    <!-- Visual Columns of Blocks -->
    <div class="h-44 bg-slate-950/80 rounded-xl border border-slate-800 p-3 flex items-end justify-around relative mb-3">
      <!-- Target Mean Line -->
      <div id="fs-mean-line" class="absolute left-0 right-0 border-b-2 border-dashed border-amber-400 z-10 transition-all duration-500" style="bottom: 50%;">
        <span class="absolute right-2 -top-4 text-[10px] font-bold text-amber-300 font-mono">Mean = 10</span>
      </div>

      <!-- Column A -->
      <div class="flex flex-col items-center gap-1 z-20">
        <span id="fs-val-a" class="text-xs font-bold font-mono text-cyan-300">14</span>
        <div id="fs-col-a" class="w-12 bg-cyan-500/80 border border-cyan-300 rounded-t transition-all duration-500 flex items-center justify-center font-bold text-[11px] text-slate-950" style="height: 112px;"></div>
        <span class="text-[10px] text-slate-400">Anu</span>
      </div>

      <!-- Column B -->
      <div class="flex flex-col items-center gap-1 z-20">
        <span id="fs-val-b" class="text-xs font-bold font-mono text-purple-300">6</span>
        <div id="fs-col-b" class="w-12 bg-purple-500/80 border border-purple-300 rounded-t transition-all duration-500 flex items-center justify-center font-bold text-[11px] text-slate-950" style="height: 48px;"></div>
        <span class="text-[10px] text-slate-400">Biku</span>
      </div>

      <!-- Column C -->
      <div class="flex flex-col items-center gap-1 z-20">
        <span id="fs-val-c" class="text-xs font-bold font-mono text-emerald-300">12</span>
        <div id="fs-col-c" class="w-12 bg-emerald-500/80 border border-emerald-300 rounded-t transition-all duration-500 flex items-center justify-center font-bold text-[11px] text-slate-950" style="height: 96px;"></div>
        <span class="text-[10px] text-slate-400">Chetan</span>
      </div>

      <!-- Column D -->
      <div class="flex flex-col items-center gap-1 z-20">
        <span id="fs-val-d" class="text-xs font-bold font-mono text-rose-300">8</span>
        <div id="fs-col-d" class="w-12 bg-rose-500/80 border border-rose-300 rounded-t transition-all duration-500 flex items-center justify-center font-bold text-[11px] text-slate-950" style="height: 64px;"></div>
        <span class="text-[10px] text-slate-400">Divya</span>
      </div>
    </div>

    <!-- Math Calculation Box -->
    <div id="fs-math-box" class="p-2.5 bg-slate-800/80 rounded-xl border border-slate-700 text-xs font-mono text-center text-amber-200">
      Total Blocks = $14 + 6 + 12 + 8 = 40$ blocks | $\text{Mean} = \frac{40}{4} = \mathbf{10}$
    </div>
  </div>

  <div class="flex gap-2 mt-2">
    <button id="fs-btn-step" class="flex-1 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold">Transfer Surplus ➜</button>
    <button id="fs-btn-level" class="flex-1 py-2 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 text-xs font-black shadow-lg shadow-amber-500/20">⚖️ Level All Shares (Samīkaraṇa)</button>
  </div>
</div>
""",

    # 4. Mean Balance Beam (Fulcrum seesaw)
    "sim-mean-balance-beam": r"""
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Lab 4 • Fulcrum Balance Beam</span>
      <span class="text-[11px] text-slate-400 font-mono">Center of Gravity</span>
    </div>
    <p class="text-xs text-slate-300 mb-2">Click anywhere on the ruler to add or remove weights. Watch the fulcrum automatically slide to the Arithmetic Mean to keep the beam in perfect balance!</p>

    <!-- Interactive SVG Seesaw -->
    <div class="bg-slate-950/80 rounded-xl border border-slate-800 p-2 my-2 flex items-center justify-center">
      <svg id="bb-svg" width="340" height="150" viewBox="0 0 340 150">
        <!-- Defined in JS -->
      </svg>
    </div>

    <!-- Current Data Items & Status -->
    <div class="grid grid-cols-2 gap-2 text-xs mb-2">
      <div class="p-2 bg-slate-800/60 rounded border border-slate-700/60">
        <span class="text-slate-400">Current Weights:</span>
        <div id="bb-weights-list" class="font-mono text-cyan-300 font-bold mt-0.5">[4, 8, 12, 16]</div>
      </div>
      <div class="p-2 bg-slate-800/60 rounded border border-slate-700/60">
        <span class="text-slate-400">Balance Fulcrum (Mean):</span>
        <div id="bb-mean-display" class="font-mono text-emerald-400 font-bold text-sm mt-0.5">Mean = 10.0</div>
      </div>
    </div>
  </div>

  <div class="flex justify-between items-center pt-2 border-t border-slate-800 text-[11px] text-slate-400">
    <span>$\sum (x_i - \text{Mean}) = 0$ (Left torques = Right torques)</span>
    <button id="bb-btn-clear" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 text-xs font-semibold">Clear Weights</button>
  </div>
</div>
""",

    # 5. Know Your Onions! Town Comparator
    "sim-onion-comparator": """
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-purple-400 uppercase tracking-wider">Lab 5 • "Know Your Onions!" Comparator</span>
      <span class="text-[11px] text-amber-300 font-bold font-mono">Town A vs Town B</span>
    </div>
    <p class="text-xs text-slate-300 mb-2">Compare monthly onion retail prices per kg over a 6-month period across two towns.</p>

    <!-- Table of Monthly Prices -->
    <div class="overflow-x-auto rounded-xl border border-slate-800 mb-3">
      <table class="w-full text-xs text-center font-mono">
        <thead class="bg-slate-800/90 text-slate-300 text-[11px]">
          <tr>
            <th class="p-1.5 text-left font-sans">Month</th>
            <th class="p-1.5">Jan</th>
            <th class="p-1.5">Feb</th>
            <th class="p-1.5">Mar</th>
            <th class="p-1.5">Apr</th>
            <th class="p-1.5">May</th>
            <th class="p-1.5">Jun</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-800/60 bg-slate-900/60 text-slate-200">
          <tr>
            <td class="p-1.5 text-left font-sans font-bold text-blue-400">Town A</td>
            <td class="p-1.5">₹28</td>
            <td class="p-1.5">₹30</td>
            <td class="p-1.5">₹32</td>
            <td class="p-1.5">₹29</td>
            <td class="p-1.5">₹31</td>
            <td class="p-1.5">₹30</td>
          </tr>
          <tr>
            <td class="p-1.5 text-left font-sans font-bold text-amber-400">Town B</td>
            <td class="p-1.5">₹10</td>
            <td class="p-1.5">₹15</td>
            <td class="p-1.5">₹20</td>
            <td class="p-1.5">₹45</td>
            <td class="p-1.5">₹60</td>
            <td class="p-1.5">₹30</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Comparative Metrics Grid -->
    <div class="grid grid-cols-2 gap-2 text-xs mb-2">
      <div class="p-2.5 bg-blue-950/20 border border-blue-800/40 rounded-xl space-y-1">
        <b class="text-blue-300">Town A Summary</b>
        <div class="flex justify-between text-slate-300"><span>Min:</span> <span class="font-mono">₹28</span></div>
        <div class="flex justify-between text-slate-300"><span>Max:</span> <span class="font-mono">₹32</span></div>
        <div class="flex justify-between text-slate-300 font-bold"><span>Range:</span> <span class="font-mono text-cyan-300">₹4</span></div>
        <div class="flex justify-between text-slate-300 font-bold"><span>Mean:</span> <span class="font-mono text-emerald-400">₹30.00</span></div>
      </div>

      <div class="p-2.5 bg-amber-950/20 border border-amber-800/40 rounded-xl space-y-1">
        <b class="text-amber-300">Town B Summary</b>
        <div class="flex justify-between text-slate-300"><span>Min:</span> <span class="font-mono">₹10</span></div>
        <div class="flex justify-between text-slate-300"><span>Max:</span> <span class="font-mono">₹60</span></div>
        <div class="flex justify-between text-slate-300 font-bold"><span>Range:</span> <span class="font-mono text-amber-300">₹50</span></div>
        <div class="flex justify-between text-slate-300 font-bold"><span>Mean:</span> <span class="font-mono text-emerald-400">₹30.00</span></div>
      </div>
    </div>
  </div>

  <div class="p-2.5 bg-purple-950/20 border border-purple-800/40 rounded-xl text-[11px] text-slate-300">
    🎯 <b>Conclusion:</b> Both towns share the exact same mean ($\text{Rs. } 30$), but Town B has $12.5\times$ greater price spread ($\text{Range } 50\text{ vs } 4$).
  </div>
</div>
""",

    # 6. Dot Plot Frequency Generator
    "sim-dot-plot-generator": """
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-teal-400 uppercase tracking-wider">Lab 6 • Dot Plot Frequency Generator</span>
      <button id="dp-btn-sample" class="px-2 py-0.5 rounded bg-teal-600/30 text-teal-300 hover:bg-teal-600/50 text-[11px]">Load Sample</button>
    </div>
    <p class="text-xs text-slate-300 mb-2">Click on any number along the scale to drop a dot. Dots stack vertically to reveal clusters, gaps, and the mode.</p>

    <!-- Canvas / SVG Area for Dot Plot -->
    <div class="bg-slate-950/80 rounded-xl border border-slate-800 p-2 my-2 flex items-center justify-center">
      <svg id="dp-svg" width="340" height="150" viewBox="0 0 340 150">
        <!-- Rendered by JS -->
      </svg>
    </div>

    <!-- Metrics Bar -->
    <div class="grid grid-cols-4 gap-1.5 text-center text-xs">
      <div class="p-1.5 bg-slate-800/60 rounded border border-slate-700">
        <span class="text-[10px] text-slate-400 block">Total Dots</span>
        <span id="dp-count" class="font-mono font-bold text-cyan-300">0</span>
      </div>
      <div class="p-1.5 bg-slate-800/60 rounded border border-slate-700">
        <span class="text-[10px] text-slate-400 block">Range</span>
        <span id="dp-range" class="font-mono font-bold text-amber-300">-</span>
      </div>
      <div class="p-1.5 bg-slate-800/60 rounded border border-slate-700">
        <span class="text-[10px] text-slate-400 block">Mean</span>
        <span id="dp-mean" class="font-mono font-bold text-emerald-300">-</span>
      </div>
      <div class="p-1.5 bg-slate-800/60 rounded border border-slate-700">
        <span class="text-[10px] text-slate-400 block">Mode</span>
        <span id="dp-mode" class="font-mono font-bold text-purple-300">-</span>
      </div>
    </div>
  </div>

  <div class="flex justify-between items-center pt-2 border-t border-slate-800 text-[11px] text-slate-400">
    <span>Click scale to add dots; click a dot to remove it.</span>
    <button id="dp-btn-reset" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 text-xs">Reset Plot</button>
  </div>
</div>
""",

    # 7. Outlier Disruption Simulator
    "sim-outlier-disrupter": """
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Lab 7 • Outlier Shock Simulator</span>
      <span class="text-[11px] text-slate-400 font-mono">Mean vs Median Resistance</span>
    </div>
    <p class="text-xs text-slate-300 mb-2">Notice the five typical salaries: ₹10k, ₹11k, ₹12k, ₹10k, ₹11k. Now drag the slider to inject an extreme executive bonus!</p>

    <!-- Outlier Slider -->
    <div class="p-3 bg-slate-800/80 rounded-xl border border-slate-700 mb-3">
      <div class="flex justify-between items-center text-xs">
        <span class="text-slate-300">Executive Outlier Salary:</span>
        <span id="od-outlier-val" class="font-mono font-bold text-rose-300 text-sm">₹12,000 (No Outlier)</span>
      </div>
      <input id="od-slider" type="range" min="12" max="250" step="2" value="12" class="w-full mt-2 accent-rose-500">
      <div class="flex justify-between text-[10px] text-slate-500">
        <span>₹12k (Normal)</span>
        <span>₹100k</span>
        <span>₹180k</span>
        <span>₹250k (Extreme)</span>
      </div>
    </div>

    <!-- Duel Display: Mean vs Median -->
    <div class="grid grid-cols-2 gap-3 mb-2">
      <div class="p-3 bg-rose-950/20 border border-rose-800/40 rounded-xl text-center">
        <span class="text-xs text-slate-400 block mb-1">Arithmetic Mean</span>
        <div id="od-mean-val" class="font-mono font-black text-rose-400 text-lg">₹10,800</div>
        <span id="od-mean-shift" class="text-[10px] text-rose-300 block mt-1">+0% distorted</span>
      </div>

      <div class="p-3 bg-emerald-950/20 border border-emerald-800/40 rounded-xl text-center">
        <span class="text-xs text-slate-400 block mb-1">Median (Middle)</span>
        <div id="od-median-val" class="font-mono font-black text-emerald-400 text-lg">₹11,000</div>
        <span id="od-median-shift" class="text-[10px] text-emerald-300 block mt-1">Unmoved (Robust)</span>
      </div>
    </div>
  </div>

  <div class="p-2.5 bg-slate-950/60 border border-slate-800 rounded-xl text-[11px] text-slate-300">
    🛡️ <b>Statistical Insight:</b> The mean is held hostage by extreme values, whereas the median remains rock-steady.
  </div>
</div>
""",

    # 8. Median Finder (Sort & Find Middle)
    "sim-median-finder": """
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Lab 8 • The Median Finder</span>
      <div class="flex gap-1">
        <button id="mf-btn-odd" class="px-2 py-0.5 rounded bg-emerald-600 text-white font-bold text-[11px]">Odd (n=7)</button>
        <button id="mf-btn-even" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]">Even (n=6)</button>
      </div>
    </div>
    <p class="text-xs text-slate-300 mb-2">Watch the step-by-step procedure: sorting values and isolating the exact positional midpoint.</p>

    <!-- Cards Container -->
    <div id="mf-cards-container" class="flex flex-wrap gap-2 justify-center my-3 min-h-[50px] items-center">
      <!-- Injected by JS -->
    </div>

    <!-- Stepper Controls -->
    <div class="flex gap-2 mb-3">
      <button id="mf-btn-sort" class="flex-1 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs">1. Sort Ascending ↕</button>
      <button id="mf-btn-locate" class="flex-1 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs" disabled>2. Locate Median 📍</button>
    </div>

    <!-- Explanation Box -->
    <div id="mf-explanation" class="p-2.5 bg-slate-950/80 border border-slate-800 rounded-xl text-xs text-center font-mono text-slate-300">
      Click "1. Sort Ascending" to arrange the cards in numerical order.
    </div>
  </div>

  <div class="text-[11px] text-slate-400 text-center pt-2 border-t border-slate-800">
    Odd $n$: middle is $\frac{n+1}{2}$; Even $n$: average of middle two items.
  </div>
</div>
""",

    # 9. Classroom Height Distribution
    "sim-height-distribution": """
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-teal-400 uppercase tracking-wider">Lab 9 • Classroom Height Distribution</span>
      <span class="text-[11px] text-slate-400 font-mono">Class of 20 Students</span>
    </div>
    <p class="text-xs text-slate-300 mb-2">Explore the height histogram of Class 7 students. Adjust the distribution parameters to see how the mean and median respond.</p>

    <!-- Interactive Histogram SVG -->
    <div class="bg-slate-950/80 rounded-xl border border-slate-800 p-2 my-2 flex items-center justify-center">
      <svg id="hd-svg" width="340" height="140" viewBox="0 0 340 140">
        <!-- Rendered by JS -->
      </svg>
    </div>

    <div class="grid grid-cols-3 gap-2 text-xs text-center mb-2">
      <div class="p-1.5 bg-slate-800/60 rounded border border-slate-700">
        <span class="text-[10px] text-slate-400 block">Shortest / Tallest</span>
        <span class="font-mono font-bold text-cyan-300">132 / 158 cm</span>
      </div>
      <div class="p-1.5 bg-slate-800/60 rounded border border-slate-700">
        <span class="text-[10px] text-slate-400 block">Height Range</span>
        <span class="font-mono font-bold text-amber-300">26 cm</span>
      </div>
      <div class="p-1.5 bg-slate-800/60 rounded border border-slate-700">
        <span class="text-[10px] text-slate-400 block">Mean / Median</span>
        <span class="font-mono font-bold text-emerald-300">144.5 / 144 cm</span>
      </div>
    </div>
  </div>

  <div class="p-2 bg-slate-950/60 border border-slate-800 rounded-xl text-[11px] text-slate-400 text-center">
    Natural human physical characteristics cluster bell-like around the center with minimal skewness.
  </div>
</div>
""",

    # 10. Time Estimation Experiment
    "sim-time-estimator": """
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Lab 10 • 30-Second Silent Reaction</span>
      <span class="text-[11px] text-slate-400 font-mono">Perception vs Reality</span>
    </div>
    <p class="text-xs text-slate-300 mb-2">Click "Start", close your eyes, and click "STOP" when you think exactly 30 seconds have passed!</p>

    <!-- Stopwatch Visual -->
    <div class="p-4 bg-slate-950/90 rounded-xl border border-slate-800 text-center my-2">
      <div id="te-timer-display" class="font-mono font-black text-3xl text-amber-400 tracking-wider">00.0s</div>
      <div id="te-prompt-text" class="text-xs text-slate-400 mt-1">Press Start to begin the silent test...</div>
    </div>

    <!-- Action Buttons -->
    <div class="flex gap-2 mb-3">
      <button id="te-btn-start" class="flex-1 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs">Start Stopwatch ⏱️</button>
      <button id="te-btn-stop" class="flex-1 py-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs" disabled>STOP! (30s Elapsed)</button>
    </div>

    <!-- Live Classroom Aggregates -->
    <div class="p-2.5 bg-slate-800/60 rounded-xl border border-slate-700 text-xs">
      <div class="flex justify-between items-center mb-1">
        <span class="text-slate-400">Class Trials Recorded:</span>
        <span id="te-trial-count" class="font-mono font-bold text-cyan-300">12 trials</span>
      </div>
      <div class="flex justify-between items-center">
        <span class="text-slate-400">Class Average Estimate:</span>
        <span id="te-class-mean" class="font-mono font-bold text-emerald-400">28.4 seconds</span>
      </div>
    </div>
  </div>

  <div class="text-[11px] text-slate-400 text-center pt-2 border-t border-slate-800">
    Wisdom of the crowd: Individual guesses err widely, but their collective mean zeroes in on truth.
  </div>
</div>
""",

    # 11. Graph Type Selector
    "sim-graph-type-selector": """
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-purple-400 uppercase tracking-wider">Lab 11 • Single vs Clustered Columns</span>
      <div class="flex gap-1">
        <button id="gt-btn-single" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]">Single Bar</button>
        <button id="gt-btn-double" class="px-2 py-0.5 rounded bg-purple-600 text-white font-bold text-[11px]">Double Bar</button>
      </div>
    </div>
    <p class="text-xs text-slate-300 mb-2">Toggle between a single bar graph and a clustered double bar graph comparing Quarterly Sports signups.</p>

    <!-- Graph Rendering Canvas -->
    <div class="bg-slate-950/80 rounded-xl border border-slate-800 p-2 my-2 flex items-center justify-center">
      <svg id="gt-svg" width="340" height="150" viewBox="0 0 340 150">
        <!-- Rendered by JS -->
      </svg>
    </div>

    <!-- Legend & Mode Description -->
    <div id="gt-info-box" class="p-2.5 bg-slate-800/80 rounded-xl border border-slate-700 text-xs">
      <div class="font-bold text-purple-300 mb-1">Clustered Column Graph Active</div>
      <p class="text-slate-300 text-[11px]">Shows Term 1 (Blue) and Term 2 (Amber) side-by-side for each subject. Enables instant comparison of progress.</p>
    </div>
  </div>

  <div class="text-[11px] text-slate-400 text-center pt-2 border-t border-slate-800">
    Double bar graphs encode two dimensions of comparison simultaneously.
  </div>
</div>
""",

    # 12. Double Bar Graph Builder
    "sim-double-bar-builder": """
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-blue-400 uppercase tracking-wider">Lab 12 • Interactive Double Bar Builder</span>
      <span class="text-[11px] text-slate-400 font-mono">Scale = 1 cm : 10 units</span>
    </div>
    <p class="text-xs text-slate-300 mb-2">Modify the category values using the inputs below. Watch the bars render with consistent widths, uniform gaps, and scaled axes.</p>

    <!-- SVG Double Bar Graph -->
    <div class="bg-slate-950/80 rounded-xl border border-slate-800 p-2 my-2 flex items-center justify-center">
      <svg id="db-svg" width="340" height="145" viewBox="0 0 340 145">
        <!-- Rendered by JS -->
      </svg>
    </div>

    <!-- Inputs Grid -->
    <div class="grid grid-cols-3 gap-2 text-xs">
      <div class="p-1.5 bg-slate-800/60 rounded border border-slate-700">
        <span class="text-[10px] text-slate-400 block">Maths (T1/T2)</span>
        <div class="flex gap-1 mt-1">
          <input id="db-in-m1" type="number" min="0" max="100" value="60" class="w-1/2 p-1 bg-slate-900 rounded border border-blue-500/40 text-blue-300 font-mono text-center">
          <input id="db-in-m2" type="number" min="0" max="100" value="85" class="w-1/2 p-1 bg-slate-900 rounded border border-amber-500/40 text-amber-300 font-mono text-center">
        </div>
      </div>

      <div class="p-1.5 bg-slate-800/60 rounded border border-slate-700">
        <span class="text-[10px] text-slate-400 block">Science (T1/T2)</span>
        <div class="flex gap-1 mt-1">
          <input id="db-in-s1" type="number" min="0" max="100" value="70" class="w-1/2 p-1 bg-slate-900 rounded border border-blue-500/40 text-blue-300 font-mono text-center">
          <input id="db-in-s2" type="number" min="0" max="100" value="75" class="w-1/2 p-1 bg-slate-900 rounded border border-amber-500/40 text-amber-300 font-mono text-center">
        </div>
      </div>

      <div class="p-1.5 bg-slate-800/60 rounded border border-slate-700">
        <span class="text-[10px] text-slate-400 block">English (T1/T2)</span>
        <div class="flex gap-1 mt-1">
          <input id="db-in-e1" type="number" min="0" max="100" value="80" class="w-1/2 p-1 bg-slate-900 rounded border border-blue-500/40 text-blue-300 font-mono text-center">
          <input id="db-in-e2" type="number" min="0" max="100" value="70" class="w-1/2 p-1 bg-slate-900 rounded border border-amber-500/40 text-amber-300 font-mono text-center">
        </div>
      </div>
    </div>
  </div>

  <div class="flex justify-between items-center pt-2 border-t border-slate-800 text-[11px] text-slate-400">
    <span class="flex items-center gap-1.5">
      <span class="w-2.5 h-2.5 rounded-sm bg-blue-500 inline-block"></span> Term 1
      <span class="w-2.5 h-2.5 rounded-sm bg-amber-500 inline-block ml-2"></span> Term 2
    </span>
    <button id="db-btn-update" class="px-3 py-1 rounded bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs">Update Graph</button>
  </div>
</div>
""",

    # 13. Multi-Step Data Extractor
    "sim-multistep-extractor": r"""
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-teal-400 uppercase tracking-wider">Lab 13 • Multi-Step Data Extractor</span>
      <span class="text-[11px] text-slate-400 font-mono">Query Engine</span>
    </div>
    <p class="text-xs text-slate-300 mb-2">Ask complex questions to the data graph and watch the mathematical derivations light up.</p>

    <!-- Query Selector Buttons -->
    <div class="grid grid-cols-3 gap-1.5 mb-3">
      <button id="me-btn-q1" class="p-2 rounded-lg bg-teal-600 text-white font-bold text-[11px] text-center">Max Improvement</button>
      <button id="me-btn-q2" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] text-center">Total Production</button>
      <button id="me-btn-q3" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] text-center">Performance Drop</button>
    </div>

    <!-- Active Query Result Card -->
    <div id="me-result-card" class="p-3 bg-slate-950/80 rounded-xl border border-slate-800 text-xs space-y-2">
      <div class="font-bold text-teal-300">Question: Which subject showed the largest numerical improvement?</div>
      <div class="text-slate-300 font-mono text-[11px] leading-relaxed">
        • Maths: $85 - 60 = \mathbf{+25\text{ marks}}$<br>
        • Science: $75 - 70 = +5\text{ marks}$<br>
        • English: $70 - 80 = -10\text{ marks}$ (Drop!)
      </div>
      <div class="p-2 bg-emerald-950/30 rounded border border-emerald-800/50 text-emerald-300 font-bold">
        🎉 Answer: Mathematics with a spectacular $+25$ mark surge!
      </div>
    </div>
  </div>

  <div class="text-[11px] text-slate-400 text-center pt-2 border-t border-slate-800">
    Multi-step analytics requires subtracting pairs and comparing the resulting differences.
  </div>
</div>
""",

    # 14. Growth Trends Across Decades
    "sim-growth-trends-tracker": """
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Lab 14 • Child Growth Over Decades</span>
      <span class="text-[11px] text-amber-300 font-bold font-mono">Secular Trend</span>
    </div>
    <p class="text-xs text-slate-300 mb-2">Drag the timeline slider from 1920 to 2025 to see how average height at age 12 shifted with global nutrition.</p>

    <!-- Interactive Decade Slider -->
    <div class="p-3 bg-slate-800/80 rounded-xl border border-slate-700 mb-3">
      <div class="flex justify-between items-center text-xs">
        <span class="text-slate-300">Survey Year:</span>
        <span id="gt-year-val" class="font-mono font-bold text-cyan-300 text-base">Year 1960</span>
      </div>
      <input id="gt-year-slider" type="range" min="1920" max="2025" step="5" value="1960" class="w-full mt-2 accent-emerald-400">
      <div class="flex justify-between text-[10px] text-slate-500">
        <span>1920</span>
        <span>1960</span>
        <span>2000</span>
        <span>2025</span>
      </div>
    </div>

    <!-- Height & Drivers Card -->
    <div class="grid grid-cols-2 gap-2 text-xs mb-2">
      <div class="p-2.5 bg-slate-950/60 rounded-xl border border-slate-800 text-center">
        <span class="text-[10px] text-slate-400 block mb-1">Average Height (Age 12)</span>
        <div id="gt-height-val" class="font-mono font-black text-emerald-400 text-xl">141.0 cm</div>
        <span id="gt-diff-val" class="text-[10px] text-cyan-300 block mt-1">+6.0 cm since 1920</span>
      </div>

      <div class="p-2.5 bg-slate-950/60 rounded-xl border border-slate-800">
        <span class="text-[10px] text-slate-400 block mb-1">Primary Driver:</span>
        <div id="gt-driver-val" class="font-bold text-amber-300 text-[11px]">Mid-Century Antibiotics & Clean Water Expansion</div>
      </div>
    </div>
  </div>

  <div class="p-2 bg-emerald-950/20 border border-emerald-800/40 rounded-xl text-[11px] text-slate-300">
    📈 <b>Data Detective Conclusion:</b> Over a century, human height grew by $+15\text{ cm}$ ($1.5\text{ cm/decade}$) driven by public health.
  </div>
</div>
""",

    # 15. Misleading Graph Buster
    "sim-misleading-graph-buster": r"""
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-rose-400 uppercase tracking-wider">Lab 15 • Misleading Graph Buster</span>
      <div class="flex gap-1">
        <button id="mg-btn-truncated" class="px-2 py-0.5 rounded bg-rose-600 text-white font-bold text-[11px]">Truncated Y-Axis</button>
        <button id="mg-btn-honest" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px]">Honest 0-Baseline</button>
      </div>
    </div>
    <p class="text-xs text-slate-300 mb-2">Compare Brand A ($98\%$) vs Brand B ($99\%$). See how truncating the Y-axis makes a tiny $1\%$ difference look like a $500\%$ difference!</p>

    <!-- Graph Rendering Area -->
    <div class="bg-slate-950/80 rounded-xl border border-slate-800 p-2 my-2 flex items-center justify-center">
      <svg id="mg-svg" width="340" height="145" viewBox="0 0 340 145">
        <!-- Rendered by JS -->
      </svg>
    </div>

    <!-- Alert / Explanation -->
    <div id="mg-explanation" class="p-2.5 bg-rose-950/30 border border-rose-800/50 rounded-xl text-xs text-rose-200">
      <b>⚠️ Optical Deception Active:</b> Baseline starts at $95\%$. The $99\%$ bar appears TRIPLE the height of the $98\%$ bar!
    </div>
  </div>

  <div class="text-[11px] text-slate-400 text-center pt-2 border-t border-slate-800">
    Always demand to see the zero-baseline on bar graphs before believing claims.
  </div>
</div>
""",

    # 16. Data Detective Master Lab
    "sim-data-detective-hub": """
<div class="h-full flex flex-col justify-between p-4 bg-slate-900/90 rounded-2xl border border-slate-800 text-slate-100">
  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Lab 16 • Data Detective Master Console</span>
      <span class="text-[11px] text-slate-400 font-mono">Prof. Mahalanobis Hub</span>
    </div>
    <p class="text-xs text-slate-300 mb-2">Input your own comma-separated dataset to instantly compute all statistical measures and generate a live dot plot.</p>

    <!-- Input Bar -->
    <div class="flex gap-2 mb-3">
      <input id="dd-input-data" type="text" value="12, 15, 14, 18, 15, 20, 16, 50" class="flex-1 p-2 bg-slate-950 rounded-lg border border-slate-700 text-xs font-mono text-cyan-300">
      <button id="dd-btn-analyze" class="px-4 py-2 rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs">Analyze 🚀</button>
    </div>

    <!-- Results Grid -->
    <div class="grid grid-cols-4 gap-2 text-center text-xs mb-3">
      <div class="p-2 bg-slate-800/60 rounded-xl border border-slate-700">
        <span class="text-[10px] text-slate-400 block">Mean ($\bar{x}$)</span>
        <span id="dd-out-mean" class="font-mono font-bold text-rose-400 text-sm">20.0</span>
      </div>
      <div class="p-2 bg-slate-800/60 rounded-xl border border-slate-700">
        <span class="text-[10px] text-slate-400 block">Median</span>
        <span id="dd-out-median" class="font-mono font-bold text-emerald-400 text-sm">15.5</span>
      </div>
      <div class="p-2 bg-slate-800/60 rounded-xl border border-slate-700">
        <span class="text-[10px] text-slate-400 block">Range</span>
        <span id="dd-out-range" class="font-mono font-bold text-amber-400 text-sm">38</span>
      </div>
      <div class="p-2 bg-slate-800/60 rounded-xl border border-slate-700">
        <span class="text-[10px] text-slate-400 block">Outlier?</span>
        <span id="dd-out-outlier" class="font-mono font-bold text-purple-400 text-sm">50</span>
      </div>
    </div>

    <!-- Mini Dot Plot SVG -->
    <div class="bg-slate-950/80 rounded-xl border border-slate-800 p-2 flex items-center justify-center">
      <svg id="dd-svg" width="340" height="85" viewBox="0 0 340 85">
        <!-- Rendered by JS -->
      </svg>
    </div>
  </div>

  <div class="p-2 bg-slate-950/60 border border-slate-800 rounded-xl text-[11px] text-slate-400 text-center">
    Notice: The outlier (50) pulls the Mean to 20.0, but the Median stays grounded at 15.5.
  </div>
</div>
"""
}

# Write to .agents/class7_math_connecting_the_dots_sims.py
output_path = ".agents/class7_math_connecting_the_dots_sims.py"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("# Generated Simulators for NCERT Class 7 Mathematics - Chapter 5: Connecting the Dots...\n\n")
    f.write(f"SIMULATORS = {repr(SIMULATORS)}\n")

print(f"Generated {output_path} successfully with {len(SIMULATORS)} simulators!")
