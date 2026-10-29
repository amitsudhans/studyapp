# -*- coding: utf-8 -*-
"""
Script to generate .agents/class7_math_another_peek_beyond_the_point_sims.py
Contains all 16 bespoke interactive SVG simulators for Chapter 12: Another Peek Beyond the Point.
"""

simulators = {
    "sim-place-value-matrix": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
      <span>🏛️</span> Decimal Place Value Matrix & Symmetrical Scales
    </div>
    <span class="text-[10px] bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded border border-amber-500/30">Interactive Place Value Matrix</span>
  </div>
  
  <div class="grid grid-cols-6 gap-1 mb-3 text-center text-xs">
    <div class="p-1.5 bg-slate-800 rounded border border-slate-700">
      <div class="text-[10px] text-slate-400">Hundreds</div>
      <div class="font-bold text-sky-400 text-sm" id="mat-h">3</div>
      <div class="text-[9px] text-slate-500">×100</div>
    </div>
    <div class="p-1.5 bg-slate-800 rounded border border-slate-700">
      <div class="text-[10px] text-slate-400">Tens</div>
      <div class="font-bold text-sky-300 text-sm" id="mat-t">4</div>
      <div class="text-[9px] text-slate-500">×10</div>
    </div>
    <div class="p-1.5 bg-slate-800 rounded border border-slate-700">
      <div class="text-[10px] text-slate-400">Ones</div>
      <div class="font-bold text-emerald-400 text-sm" id="mat-o">7</div>
      <div class="text-[9px] text-slate-500">×1</div>
    </div>
    <div class="p-1.5 bg-amber-950/40 rounded border border-amber-700/50">
      <div class="text-[10px] text-amber-400">Tenths</div>
      <div class="font-bold text-amber-300 text-sm" id="mat-th">8</div>
      <div class="text-[9px] text-amber-500">÷10 (0.1)</div>
    </div>
    <div class="p-1.5 bg-amber-950/40 rounded border border-amber-700/50">
      <div class="text-[10px] text-amber-400">Hundredths</div>
      <div class="font-bold text-amber-300 text-sm" id="mat-hth">2</div>
      <div class="text-[9px] text-amber-500">÷100 (0.01)</div>
    </div>
    <div class="p-1.5 bg-amber-950/40 rounded border border-amber-700/50">
      <div class="text-[10px] text-amber-400">Thousandths</div>
      <div class="font-bold text-amber-300 text-sm" id="mat-tth">5</div>
      <div class="text-[9px] text-amber-500">÷1000 (0.001)</div>
    </div>
  </div>

  <div class="flex items-center justify-center gap-2 mb-3 bg-slate-950/60 p-2 rounded-lg border border-slate-800">
    <span class="text-xs text-slate-400">Compiled Number:</span>
    <span class="font-mono font-bold text-base text-amber-300" id="mat-full-num">347.825</span>
  </div>

  <div class="space-y-2 text-xs">
    <div class="flex items-center gap-2">
      <label class="w-24 text-[11px] text-slate-400">Tenths (0–9):</label>
      <input type="range" min="0" max="9" value="8" id="mat-slide-th" class="flex-1 accent-amber-500">
      <span class="w-6 text-right font-mono text-amber-300" id="val-th">8</span>
    </div>
    <div class="flex items-center gap-2">
      <label class="w-24 text-[11px] text-slate-400">Hundredths:</label>
      <input type="range" min="0" max="9" value="2" id="mat-slide-hth" class="flex-1 accent-amber-500">
      <span class="w-6 text-right font-mono text-amber-300" id="val-hth">2</span>
    </div>
    <div class="flex items-center gap-2">
      <label class="w-24 text-[11px] text-slate-400">Thousandths:</label>
      <input type="range" min="0" max="9" value="5" id="mat-slide-tth" class="flex-1 accent-amber-500">
      <span class="w-6 text-right font-mono text-amber-300" id="val-tth">5</span>
    </div>
  </div>

  <div class="mt-3 p-2 bg-slate-950/80 rounded border border-slate-800 text-[11px] text-slate-300 text-center font-mono" id="mat-expanded-preview">
    $347.825 = 300 + 40 + 7 + \frac{8}{10} + \frac{2}{100} + \frac{5}{1000}$
  </div>
</div>
""",

    "sim-expanded-deconstructor": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-indigo-300 flex items-center gap-1.5">
      <span>🧩</span> Decimal Expanded Form Deconstructor
    </div>
    <span class="text-[10px] bg-indigo-500/20 text-indigo-300 px-2 py-0.5 rounded border border-indigo-500/30">Component Slicer</span>
  </div>

  <div class="flex flex-wrap gap-1.5 mb-3 justify-center">
    <button class="px-2.5 py-1 text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 rounded border border-slate-700 btn-decon" data-val="23.456">23.456</button>
    <button class="px-2.5 py-1 text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 rounded border border-slate-700 btn-decon" data-val="7.042">7.042</button>
    <button class="px-2.5 py-1 text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 rounded border border-slate-700 btn-decon" data-val="405.309">405.309</button>
    <button class="px-2.5 py-1 text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 rounded border border-slate-700 btn-decon" data-val="0.075">0.075</button>
  </div>

  <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 mb-3 space-y-2 text-xs">
    <div class="flex items-center justify-between border-b border-slate-800 pb-1.5">
      <span class="text-slate-400">Active Decimal:</span>
      <span class="font-mono font-bold text-sm text-cyan-300" id="decon-target">23.456</span>
    </div>
    <div class="space-y-1.5" id="decon-slices">
      <!-- Slices generated by JS -->
    </div>
  </div>

  <div class="p-2 bg-indigo-950/30 border border-indigo-500/30 rounded text-center text-xs text-indigo-200 font-mono" id="decon-total-formula">
    $23.456 = 20 + 3 + 0.4 + 0.05 + 0.006$
  </div>
</div>
""",

    "sim-fraction-decimal-bridge": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-cyan-300 flex items-center gap-1.5">
      <span>🌉</span> Power-of-10 Fraction & Decimal Visual Bridge
    </div>
    <span class="text-[10px] bg-cyan-500/20 text-cyan-300 px-2 py-0.5 rounded border border-cyan-500/30">Dynamic Gauge</span>
  </div>

  <div class="grid grid-cols-3 gap-2 mb-3 text-center">
    <button class="p-1.5 bg-cyan-950/40 hover:bg-cyan-900/50 rounded border border-cyan-700/50 text-xs btn-bridge-den" data-den="10">Denominator: 10</button>
    <button class="p-1.5 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-xs btn-bridge-den" data-den="100">Denominator: 100</button>
    <button class="p-1.5 bg-slate-800 hover:bg-slate-700 rounded border border-slate-700 text-xs btn-bridge-den" data-den="1000">Denominator: 1000</button>
  </div>

  <div class="space-y-2 mb-3 text-xs">
    <div class="flex items-center gap-2">
      <label class="w-20 text-[11px] text-slate-400">Numerator:</label>
      <input type="range" min="1" max="10" value="7" id="bridge-num-slider" class="flex-1 accent-cyan-400">
      <span class="w-8 text-right font-mono text-cyan-300" id="bridge-num-display">7</span>
    </div>
  </div>

  <!-- SVG Visualization -->
  <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 mb-2">
    <svg viewBox="0 0 400 70" class="w-full h-auto">
      <!-- Background Track -->
      <rect x="20" y="20" width="360" height="25" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1.5" />
      <!-- Fill Level -->
      <rect x="20" y="20" width="252" height="25" rx="6" fill="url(#bridgeGrad)" id="bridge-fill-bar" />
      <defs>
        <linearGradient id="bridgeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#06b6d4" />
          <stop offset="100%" stop-color="#3b82f6" />
        </linearGradient>
      </defs>
      <!-- Gauge markers -->
      <line x1="20" y1="15" x2="20" y2="50" stroke="#64748b" stroke-width="1" />
      <text x="20" y="62" fill="#94a3b8" font-size="9" text-anchor="middle">0</text>
      <line x1="200" y1="15" x2="200" y2="50" stroke="#64748b" stroke-width="1" stroke-dasharray="2,2" />
      <text x="200" y="62" fill="#94a3b8" font-size="9" text-anchor="middle">0.5</text>
      <line x1="380" y1="15" x2="380" y2="50" stroke="#64748b" stroke-width="1" />
      <text x="380" y="62" fill="#94a3b8" font-size="9" text-anchor="middle">1.0</text>
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2 text-center text-xs font-mono">
    <div class="p-2 bg-slate-950/60 rounded border border-slate-800">
      <span class="text-slate-400 text-[10px]">Fraction:</span><br>
      <span class="text-cyan-300 font-bold text-sm" id="bridge-frac-text">$\frac{7}{10}$</span>
    </div>
    <div class="p-2 bg-slate-950/60 rounded border border-slate-800">
      <span class="text-slate-400 text-[10px]">Decimal:</span><br>
      <span class="text-emerald-300 font-bold text-sm" id="bridge-dec-text">$\mathbf{0.7}$</span>
    </div>
  </div>
</div>
""",

    "sim-friendly-multiplier-scaler": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-emerald-300 flex items-center gap-1.5">
      <span>🎯</span> Denominator Scaling Laboratory (Powers of 10)
    </div>
    <span class="text-[10px] bg-emerald-500/20 text-emerald-300 px-2 py-0.5 rounded border border-emerald-500/30">Factor Scaler</span>
  </div>

  <div class="text-xs text-slate-400 mb-2">Choose a fraction with prime factors of 2 and 5 in the denominator:</div>
  
  <div class="flex flex-wrap gap-1.5 mb-3 justify-center">
    <button class="px-2.5 py-1 text-xs bg-emerald-950/40 text-emerald-300 rounded border border-emerald-700/50 btn-scaler" data-num="1" data-den="2">1/2</button>
    <button class="px-2.5 py-1 text-xs bg-slate-800 text-slate-300 rounded border border-slate-700 btn-scaler" data-num="3" data-den="4">3/4</button>
    <button class="px-2.5 py-1 text-xs bg-slate-800 text-slate-300 rounded border border-slate-700 btn-scaler" data-num="3" data-den="5">3/5</button>
    <button class="px-2.5 py-1 text-xs bg-slate-800 text-slate-300 rounded border border-slate-700 btn-scaler" data-num="1" data-den="8">1/8</button>
    <button class="px-2.5 py-1 text-xs bg-slate-800 text-slate-300 rounded border border-slate-700 btn-scaler" data-num="7" data-den="25">7/25</button>
    <button class="px-2.5 py-1 text-xs bg-slate-800 text-slate-300 rounded border border-slate-700 btn-scaler" data-num="9" data-den="20">9/20</button>
  </div>

  <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 text-xs space-y-2 mb-2 font-mono">
    <div class="flex items-center justify-between text-slate-300">
      <span>1. Target Denominator Power:</span>
      <span class="font-bold text-amber-300" id="scaler-target-power">10</span>
    </div>
    <div class="flex items-center justify-between text-slate-300">
      <span>2. Complementary Multiplier:</span>
      <span class="font-bold text-emerald-400" id="scaler-multiplier">× 5</span>
    </div>
    <div class="p-2 bg-slate-900 rounded border border-slate-800 text-center text-cyan-200" id="scaler-equation">
      $\frac{1}{2} = \frac{1 \times 5}{2 \times 5} = \frac{5}{10} = \mathbf{0.5}$
    </div>
  </div>

  <div class="p-2 bg-slate-950/90 rounded border border-slate-800 text-[11px] text-slate-400 text-center">
    💡 Notice: Trailing zeroes invariance ensures $0.5 = 0.50 = 0.500$.
  </div>
</div>
""",

    "sim-whole-decimal-multiplier": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-blue-300 flex items-center gap-1.5">
      <span>🚶</span> Decimal Number Line Stepper (Whole × Decimal)
    </div>
    <span class="text-[10px] bg-blue-500/20 text-blue-300 px-2 py-0.5 rounded border border-blue-500/30">Repeated Addition</span>
  </div>

  <div class="grid grid-cols-2 gap-3 mb-3 text-xs">
    <div>
      <label class="text-[11px] text-slate-400 block mb-1">Step Size (Decimal):</label>
      <div class="flex items-center gap-2">
        <input type="range" min="1" max="8" value="3" id="step-size-slider" class="flex-1 accent-blue-500">
        <span class="w-8 font-mono text-blue-300 font-bold" id="step-size-val">0.3</span>
      </div>
    </div>
    <div>
      <label class="text-[11px] text-slate-400 block mb-1">Number of Hops ($k$):</label>
      <div class="flex items-center gap-2">
        <input type="range" min="1" max="6" value="4" id="step-count-slider" class="flex-1 accent-blue-500">
        <span class="w-6 font-mono text-blue-300 font-bold" id="step-count-val">4</span>
      </div>
    </div>
  </div>

  <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 mb-2">
    <svg viewBox="0 0 400 90" class="w-full h-auto" id="stepper-svg">
      <!-- Drawn dynamically by JS -->
    </svg>
  </div>

  <div class="p-2 bg-blue-950/40 rounded border border-blue-500/30 text-center text-xs font-mono text-cyan-200" id="stepper-equation">
    $0.3 \times 4 = 0.3 + 0.3 + 0.3 + 0.3 = \mathbf{1.2}$
  </div>
</div>
""",

    "sim-grid-multiplication-area": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-violet-300 flex items-center gap-1.5">
      <span>🟩</span> 100-Square Unit Area Multiplication Model
    </div>
    <span class="text-[10px] bg-violet-500/20 text-violet-300 px-2 py-0.5 rounded border border-violet-500/30">10×10 Overlap</span>
  </div>

  <div class="grid grid-cols-2 gap-3 mb-2 text-xs">
    <div>
      <label class="text-[11px] text-sky-400 block mb-0.5">Factor 1 (Rows / Blue):</label>
      <div class="flex items-center gap-1.5">
        <input type="range" min="1" max="9" value="7" id="grid-f1-slider" class="flex-1 accent-sky-400">
        <span class="font-mono text-sky-300 font-bold w-6" id="grid-f1-val">0.7</span>
      </div>
    </div>
    <div>
      <label class="text-[11px] text-amber-400 block mb-0.5">Factor 2 (Cols / Yellow):</label>
      <div class="flex items-center gap-1.5">
        <input type="range" min="1" max="9" value="4" id="grid-f2-slider" class="flex-1 accent-amber-400">
        <span class="font-mono text-amber-300 font-bold w-6" id="grid-f2-val">0.4</span>
      </div>
    </div>
  </div>

  <div class="flex justify-center mb-2">
    <svg viewBox="0 0 200 200" class="w-48 h-48 bg-slate-950 border border-slate-700 rounded-lg" id="unit-grid-svg">
      <!-- 10x10 squares drawn by JS -->
    </svg>
  </div>

  <div class="p-2 bg-slate-950/80 rounded border border-slate-800 text-center text-xs font-mono text-emerald-300" id="grid-result-text">
    $0.7 \times 0.4 = \frac{7}{10} \times \frac{4}{10} = \frac{28}{100} = \mathbf{0.28}$ (28 hundredths)
  </div>
</div>
""",

    "sim-multiplication-algorithm-stepper": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-fuchsia-300 flex items-center gap-1.5">
      <span>⚙️</span> The 3-Step Decimal Multiplication Pipeline
    </div>
    <span class="text-[10px] bg-fuchsia-500/20 text-fuchsia-300 px-2 py-0.5 rounded border border-fuchsia-500/30">Algorithm Engine</span>
  </div>

  <div class="flex flex-wrap gap-1.5 mb-3 justify-center text-xs">
    <button class="px-2 py-1 bg-fuchsia-950/40 text-fuchsia-300 rounded border border-fuchsia-700/50 btn-alg-sample" data-a="0.12" data-b="0.4">0.12 × 0.4</button>
    <button class="px-2 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-alg-sample" data-a="0.05" data-b="0.07">0.05 × 0.07</button>
    <button class="px-2 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-alg-sample" data-a="2.5" data-b="1.4">2.5 × 1.4</button>
    <button class="px-2 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-alg-sample" data-a="0.003" data-b="0.8">0.003 × 0.8</button>
  </div>

  <div class="space-y-2 mb-3 text-xs">
    <div class="p-2 bg-slate-950/70 rounded border border-slate-800 flex items-center justify-between">
      <span class="text-slate-400">Step 1: Ignore points & multiply:</span>
      <span class="font-mono text-cyan-300 font-bold" id="alg-step1">12 × 4 = 48</span>
    </div>
    <div class="p-2 bg-slate-950/70 rounded border border-slate-800 flex items-center justify-between">
      <span class="text-slate-400">Step 2: Total decimal places ($m + n$):</span>
      <span class="font-mono text-amber-300 font-bold" id="alg-step2">2 + 1 = 3 places</span>
    </div>
    <div class="p-2 bg-slate-950/70 rounded border border-slate-800 flex items-center justify-between">
      <span class="text-slate-400">Step 3: Insert point (leading zeroes):</span>
      <span class="font-mono text-emerald-300 font-bold" id="alg-step3">0.048</span>
    </div>
  </div>

  <div class="p-2 bg-fuchsia-950/30 rounded border border-fuchsia-500/30 text-center text-xs font-mono text-fuchsia-200" id="alg-final-eq">
    $\mathbf{0.12 \times 0.4 = 0.048}$
  </div>
</div>
""",

    "sim-magnitude-paradox-scale": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
      <span>⚖️</span> The Magnitude Paradox Balance
    </div>
    <span class="text-[10px] bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded border border-amber-500/30">Growth vs Shrinkage</span>
  </div>

  <div class="grid grid-cols-2 gap-3 mb-2 text-xs">
    <div>
      <label class="text-[11px] text-slate-400 block mb-0.5">Base Number ($A$):</label>
      <input type="range" min="1" max="10" value="6" id="scale-base-slider" class="w-full accent-amber-500">
      <span class="font-mono text-amber-300 font-bold" id="scale-base-val">6</span>
    </div>
    <div>
      <label class="text-[11px] text-slate-400 block mb-0.5">Multiplier Factor ($B$):</label>
      <input type="range" min="1" max="25" value="5" id="scale-factor-slider" class="w-full accent-amber-500">
      <span class="font-mono text-amber-300 font-bold" id="scale-factor-val">0.5</span>
    </div>
  </div>

  <!-- Balance SVG -->
  <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 mb-2">
    <svg viewBox="0 0 400 90" class="w-full h-auto" id="scale-beam-svg">
      <!-- Fulcrum and beam drawn by JS -->
    </svg>
  </div>

  <div class="p-2 bg-slate-950/80 rounded border border-slate-800 text-center text-xs font-mono" id="scale-verdict">
    $6 \times 0.5 = \mathbf{3} < 6$ (Multiplier $< 1 \implies$ Product shrunk!)
  </div>
</div>
""",

    "sim-power10-shift-slider": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-teal-300 flex items-center gap-1.5">
      <span>⬅️</span> Power-of-10 Decimal Division Shifter
    </div>
    <span class="text-[10px] bg-teal-500/20 text-teal-300 px-2 py-0.5 rounded border border-teal-500/30">Leftward Drift</span>
  </div>

  <div class="flex items-center justify-between gap-2 mb-3 bg-slate-950/60 p-2 rounded-lg border border-slate-800 text-xs">
    <span class="text-slate-400">Starting Number:</span>
    <span class="font-mono font-bold text-sm text-cyan-300" id="shift-start-num">73.8</span>
    <div class="flex gap-1">
      <button class="px-2 py-0.5 bg-slate-800 rounded border border-slate-700 text-[10px] btn-shift-preset" data-val="73.8">73.8</button>
      <button class="px-2 py-0.5 bg-slate-800 rounded border border-slate-700 text-[10px] btn-shift-preset" data-val="4.5">4.5</button>
      <button class="px-2 py-0.5 bg-slate-800 rounded border border-slate-700 text-[10px] btn-shift-preset" data-val="250.0">250.0</button>
    </div>
  </div>

  <div class="grid grid-cols-4 gap-1.5 mb-3 text-xs text-center">
    <button class="p-1.5 bg-teal-950/40 text-teal-300 rounded border border-teal-700/50 btn-shift-div" data-div="1">÷ 1 (No shift)</button>
    <button class="p-1.5 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-shift-div" data-div="10">÷ 10 (1 Left)</button>
    <button class="p-1.5 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-shift-div" data-div="100">÷ 100 (2 Left)</button>
    <button class="p-1.5 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-shift-div" data-div="1000">÷ 1000 (3 Left)</button>
  </div>

  <div class="p-3 bg-slate-950/80 rounded-xl border border-slate-800 text-center font-mono space-y-1">
    <div class="text-xs text-slate-400">Mathematical Result:</div>
    <div class="text-base font-bold text-teal-300" id="shift-result-num">73.8 ÷ 1 = 73.8</div>
    <div class="text-[10px] text-slate-500" id="shift-explanation">Decimal point remains in place.</div>
  </div>
</div>
""",

    "sim-place-value-regroup-division": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-indigo-300 flex items-center gap-1.5">
      <span>🔄</span> Long Division Place-Value Regrouping Tray
    </div>
    <span class="text-[10px] bg-indigo-500/20 text-indigo-300 px-2 py-0.5 rounded border border-indigo-500/30">Remainder Dissolver</span>
  </div>

  <div class="flex flex-wrap gap-1.5 mb-3 justify-center text-xs">
    <button class="px-2.5 py-1 bg-indigo-950/40 text-indigo-300 rounded border border-indigo-700/50 btn-regroup-sample" data-div="15.6" data-by="4">15.6 ÷ 4</button>
    <button class="px-2.5 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-regroup-sample" data-div="7.0" data-by="2">7 ÷ 2</button>
    <button class="px-2.5 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-regroup-sample" data-div="7.0" data-by="4">7 ÷ 4</button>
    <button class="px-2.5 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-regroup-sample" data-div="18.6" data-by="3">18.6 ÷ 3</button>
  </div>

  <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2 text-xs mb-2">
    <div class="flex justify-between items-center text-slate-400 border-b border-slate-800 pb-1">
      <span>Problem: <b class="text-cyan-300 font-mono" id="regroup-problem">15.6 ÷ 4</b></span>
      <span>Quotient: <b class="text-emerald-300 font-mono text-sm" id="regroup-quotient">3.9</b></span>
    </div>
    <div class="space-y-1 font-mono text-[11px]" id="regroup-steps">
      <!-- Steps filled by JS -->
    </div>
  </div>

  <div class="p-2 bg-indigo-950/30 rounded border border-indigo-500/30 text-center text-xs font-mono text-indigo-200">
    💡 Notice how the decimal point in the quotient directly aligns with the dividend point!
  </div>
</div>
""",

    "sim-decimal-divisor-transformer": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-purple-300 flex items-center gap-1.5">
      <span>🔑</span> Golden Ratio Divisor Integer-Transformer
    </div>
    <span class="text-[10px] bg-purple-500/20 text-purple-300 px-2 py-0.5 rounded border border-purple-500/30">Point Clearing</span>
  </div>

  <div class="flex flex-wrap gap-1.5 mb-3 justify-center text-xs">
    <button class="px-2 py-1 bg-purple-950/40 text-purple-300 rounded border border-purple-700/50 btn-trans-sample" data-num="4.5" data-den="0.15">4.5 ÷ 0.15</button>
    <button class="px-2 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-trans-sample" data-num="2.4" data-den="0.08">2.4 ÷ 0.08</button>
    <button class="px-2 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-trans-sample" data-num="6.25" data-den="0.5">6.25 ÷ 0.5</button>
    <button class="px-2 py-1 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-trans-sample" data-num="0.36" data-den="0.6">0.36 ÷ 0.6</button>
  </div>

  <div class="p-3 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2 text-xs mb-2">
    <div class="flex items-center justify-between text-slate-300">
      <span>Original Division:</span>
      <span class="font-mono font-bold text-amber-300 text-sm" id="trans-orig">4.5 ÷ 0.15</span>
    </div>
    <div class="flex items-center justify-between text-slate-300">
      <span>Required Scaling Factor:</span>
      <span class="font-mono font-bold text-purple-400" id="trans-factor">× 100</span>
    </div>
    <div class="flex items-center justify-between text-slate-300">
      <span>Transformed Integer Divisor:</span>
      <span class="font-mono font-bold text-cyan-300 text-sm" id="trans-transformed">450 ÷ 15</span>
    </div>
  </div>

  <div class="p-2 bg-purple-950/40 rounded border border-purple-500/30 text-center text-xs font-mono text-purple-200" id="trans-result">
    $\frac{4.5}{0.15} = \frac{450}{15} = \mathbf{30}$ (Magnification: quotient &gt; dividend!)
  </div>
</div>
""",

    "sim-cyclic-wheel-142857": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-pink-300 flex items-center gap-1.5">
      <span>🎡</span> The Celestial Cyclic Wheel of 142857 (1/7 to 6/7)
    </div>
    <span class="text-[10px] bg-pink-500/20 text-pink-300 px-2 py-0.5 rounded border border-pink-500/30">Infinite Cycle</span>
  </div>

  <div class="grid grid-cols-6 gap-1 mb-2 text-xs text-center">
    <button class="p-1 bg-pink-950/40 text-pink-300 rounded border border-pink-700/50 btn-cyclic" data-k="1">1/7</button>
    <button class="p-1 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-cyclic" data-k="2">2/7</button>
    <button class="p-1 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-cyclic" data-k="3">3/7</button>
    <button class="p-1 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-cyclic" data-k="4">4/7</button>
    <button class="p-1 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-cyclic" data-k="5">5/7</button>
    <button class="p-1 bg-slate-800 text-slate-300 rounded border border-slate-700 btn-cyclic" data-k="6">6/7</button>
  </div>

  <!-- Interactive SVG Dial -->
  <div class="flex justify-center mb-2">
    <svg viewBox="0 0 200 200" class="w-44 h-44" id="cyclic-wheel-svg">
      <!-- Wheel drawn by JS -->
    </svg>
  </div>

  <div class="p-2 bg-slate-950/80 rounded border border-slate-800 text-center text-xs font-mono text-pink-200" id="cyclic-display">
    $\frac{1}{7} = 0.\overline{\mathbf{142857}}$ (Cycle starting at 1)
  </div>
</div>
""",

    "sim-earth-orbit-drift": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
      <span>🌍</span> Earth's Tropical Year Orbital Simulator (365.2422 Days)
    </div>
    <span class="text-[10px] bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded border border-amber-500/30">Cosmic Clock</span>
  </div>

  <div class="flex items-center justify-between gap-2 mb-2 text-xs">
    <label class="text-[11px] text-slate-400">Years Elapsed:</label>
    <input type="range" min="1" max="400" value="4" id="orbit-years-slider" class="flex-1 accent-amber-500">
    <span class="font-mono text-amber-300 font-bold w-12 text-right" id="orbit-years-val">4 yrs</span>
  </div>

  <!-- Orbital SVG -->
  <div class="bg-slate-950 rounded-lg p-2 border border-slate-800 mb-2">
    <svg viewBox="0 0 400 100" class="w-full h-auto" id="orbit-svg">
      <!-- Sun, orbit, Earth position drawn by JS -->
    </svg>
  </div>

  <div class="grid grid-cols-2 gap-2 text-center text-xs font-mono">
    <div class="p-2 bg-slate-950/60 rounded border border-slate-800">
      <span class="text-slate-400 text-[10px]">Accumulated Extra Time:</span><br>
      <span class="text-cyan-300 font-bold" id="orbit-extra-days">0.9688 days</span>
    </div>
    <div class="p-2 bg-slate-950/60 rounded border border-slate-800">
      <span class="text-slate-400 text-[10px]">Unadjusted Calendar Slip:</span><br>
      <span class="text-rose-400 font-bold" id="orbit-slip-status">~1 day late</span>
    </div>
  </div>
</div>
""",

    "sim-leap-year-decision-tree": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-cyan-300 flex items-center gap-1.5">
      <span>🏛️</span> 3-Tier Leap Year Decision Logic Tree
    </div>
    <span class="text-[10px] bg-cyan-500/20 text-cyan-300 px-2 py-0.5 rounded border border-cyan-500/30">Divisibility Rules</span>
  </div>

  <div class="flex items-center gap-2 mb-3 text-xs">
    <label class="text-[11px] text-slate-400">Enter Year:</label>
    <input type="number" value="2024" id="leap-input-year" class="px-2 py-1 bg-slate-800 border border-slate-700 rounded text-amber-300 font-mono w-24">
    <button class="px-3 py-1 bg-cyan-600 hover:bg-cyan-500 text-white rounded font-bold" id="btn-test-leap">Evaluate</button>
    <div class="flex gap-1 ml-auto">
      <button class="px-1.5 py-0.5 bg-slate-800 rounded border border-slate-700 text-[10px] btn-year-quick" data-y="1900">1900</button>
      <button class="px-1.5 py-0.5 bg-slate-800 rounded border border-slate-700 text-[10px] btn-year-quick" data-y="2000">2000</button>
      <button class="px-1.5 py-0.5 bg-slate-800 rounded border border-slate-700 text-[10px] btn-year-quick" data-y="2024">2024</button>
      <button class="px-1.5 py-0.5 bg-slate-800 rounded border border-slate-700 text-[10px] btn-year-quick" data-y="2100">2100</button>
    </div>
  </div>

  <div class="space-y-1.5 text-xs mb-3 font-mono">
    <div class="p-2 rounded border transition-colors" id="leap-gate-4">
      <span class="text-slate-400">Gate 1:</span> Divisible by 4? <span class="font-bold" id="gate-4-ans">Yes (2024 ÷ 4 = 506)</span>
    </div>
    <div class="p-2 rounded border transition-colors" id="leap-gate-100">
      <span class="text-slate-400">Gate 2:</span> Divisible by 100? <span class="font-bold" id="gate-100-ans">No (Not a century)</span>
    </div>
    <div class="p-2 rounded border transition-colors" id="leap-gate-400">
      <span class="text-slate-400">Gate 3:</span> Divisible by 400? <span class="font-bold" id="gate-400-ans">N/A</span>
    </div>
  </div>

  <div class="p-2.5 rounded-xl border text-center font-bold text-sm" id="leap-final-verdict">
    🎉 2024 IS A LEAP YEAR (366 Days, Feb 29 exists)
  </div>
</div>
""",

    "sim-hidato-grid-puzzle": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-indigo-300 flex items-center gap-1.5">
      <span>🧩</span> Playable Hidato Number Path Grid
    </div>
    <span class="text-[10px] bg-indigo-500/20 text-indigo-300 px-2 py-0.5 rounded border border-indigo-500/30">Consecutive Paths</span>
  </div>

  <div class="flex items-center justify-between mb-2 text-xs">
    <div class="text-[11px] text-slate-400">Connect consecutive numbers 1 to 16 with King's moves:</div>
    <div class="flex gap-1.5">
      <button class="px-2 py-0.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded text-[10px] font-bold" id="btn-hidato-hint">Hint</button>
      <button class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-[10px] border border-slate-700" id="btn-hidato-solve">Solve</button>
      <button class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-[10px] border border-slate-700" id="btn-hidato-reset">Reset</button>
    </div>
  </div>

  <div class="flex justify-center mb-2">
    <div class="grid grid-cols-4 gap-1 p-2 bg-slate-950 rounded-xl border border-slate-800 w-52 h-52" id="hidato-board">
      <!-- 16 cells drawn by JS -->
    </div>
  </div>

  <div class="p-2 bg-slate-950/80 rounded border border-slate-800 text-center text-xs font-mono text-cyan-300" id="hidato-status">
    Click empty cells to enter numbers in sequence. Next number to place: <b id="hidato-next-val">2</b>
  </div>
</div>
""",

    "sim-madhava-decimal-series": r"""
<div class="p-3 bg-slate-900/80 rounded-xl border border-slate-700/70 text-slate-200">
  <div class="flex items-center justify-between mb-2">
    <div class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
      <span>📜</span> Madhava's Infinite Precision Series Accumulator
    </div>
    <span class="text-[10px] bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded border border-amber-500/30">Decimal Pi Convergence</span>
  </div>

  <div class="flex items-center justify-between gap-2 mb-2 text-xs">
    <label class="text-[11px] text-slate-400">Number of Series Terms:</label>
    <input type="range" min="1" max="50" value="8" id="madhava-terms-slider" class="flex-1 accent-amber-500">
    <span class="font-mono text-amber-300 font-bold w-8 text-right" id="madhava-terms-val">8</span>
  </div>

  <div class="p-2.5 bg-slate-950/70 rounded-xl border border-slate-800 mb-2 font-mono text-xs space-y-1">
    <div class="text-slate-400 text-[10px]">Madhava-Leibniz Formula: $\pi = 4 \sum_{k=0}^{N-1} \frac{(-1)^k}{2k+1}$</div>
    <div class="flex items-center justify-between pt-1 border-t border-slate-800">
      <span class="text-slate-300">Approximated $\pi$:</span>
      <span class="text-emerald-300 font-bold text-sm tracking-wider" id="madhava-pi-approx">3.14159...</span>
    </div>
    <div class="flex items-center justify-between">
      <span class="text-slate-300">Exact 11-digit $\pi$:</span>
      <span class="text-amber-300 font-bold">3.14159265359</span>
    </div>
  </div>

  <div class="p-2 bg-amber-950/30 rounded border border-amber-500/30 text-center text-[11px] text-amber-200 font-mono" id="madhava-status">
    Locking in decimal digits term by term with Kerala School expansions!
  </div>
</div>
"""
}

output_path = '.agents/class7_math_another_peek_beyond_the_point_sims.py'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nSimulators for Class 7 Mathematics - Another Peek Beyond the Point\n"""\n\n')
    f.write("SIMULATORS = " + repr(simulators) + "\n")

print(f"Generated {output_path} successfully! Total simulators: {len(simulators)}")

