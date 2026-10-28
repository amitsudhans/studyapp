# -*- coding: utf-8 -*-
"""
Script to create .agents/class7_math_operations_with_integers_sims.py
Defines the HTML/SVG markup for all 16 simulators.
"""

SIMS = {}

# 1. sim-integer-puzzle
SIMS["sim-integer-puzzle"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-sky-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-sky-300">🧩 Integer Pair Sum & Difference Puzzle</div>
    <div class="flex gap-1.5">
      <button class="px-2 py-1 rounded bg-sky-600/40 hover:bg-sky-600/60 text-sky-200 text-[11px] font-bold" onclick="setPuzzleTarget(-5, 'sum')">Sum = -5</button>
      <button class="px-2 py-1 rounded bg-amber-600/40 hover:bg-amber-600/60 text-amber-200 text-[11px] font-bold" onclick="setPuzzleTarget(4, 'diff')">Diff = +4</button>
      <button class="px-2 py-1 rounded bg-emerald-600/40 hover:bg-emerald-600/60 text-emerald-200 text-[11px] font-bold" onclick="setPuzzleTarget(0, 'sum')">Sum = 0</button>
    </div>
  </div>

  <div class="grid grid-cols-2 gap-3 bg-slate-950/60 p-3 rounded-lg border border-slate-800">
    <div>
      <label class="text-[11px] font-semibold text-slate-300 flex justify-between">
        <span>Integer A:</span>
        <span id="puzzleValA" class="font-bold text-amber-400">3</span>
      </label>
      <input id="puzzleSliderA" type="range" min="-10" max="10" value="3" class="w-full h-1.5 bg-slate-700 rounded-lg accent-amber-400 cursor-pointer" oninput="updateIntegerPuzzle()">
    </div>
    <div>
      <label class="text-[11px] font-semibold text-slate-300 flex justify-between">
        <span>Integer B:</span>
        <span id="puzzleValB" class="font-bold text-sky-400">-8</span>
      </label>
      <input id="puzzleSliderB" type="range" min="-10" max="10" value="-8" class="w-full h-1.5 bg-slate-700 rounded-lg accent-sky-400 cursor-pointer" oninput="updateIntegerPuzzle()">
    </div>
  </div>

  <!-- Live Visual Display -->
  <div class="flex flex-col items-center justify-center p-3 bg-slate-950/80 rounded-lg border border-slate-800 gap-2">
    <div class="flex items-center gap-6">
      <div class="flex flex-col items-center p-2 rounded bg-sky-950/40 border border-sky-500/30 min-w-[120px]">
        <span class="text-[10px] text-sky-300 font-bold uppercase tracking-wider">Sum (A + B)</span>
        <span id="puzzleSumExpr" class="text-xs text-slate-300 font-mono">3 + (-8)</span>
        <span id="puzzleSumResult" class="text-xl font-extrabold text-amber-400 font-mono mt-1">-5</span>
      </div>
      <div class="flex flex-col items-center p-2 rounded bg-purple-950/40 border border-purple-500/30 min-w-[120px]">
        <span class="text-[10px] text-purple-300 font-bold uppercase tracking-wider">Difference (A - B)</span>
        <span id="puzzleDiffExpr" class="text-xs text-slate-300 font-mono">3 - (-8)</span>
        <span id="puzzleDiffResult" class="text-xl font-extrabold text-emerald-400 font-mono mt-1">+11</span>
      </div>
    </div>
    <div id="puzzleFeedback" class="text-xs font-bold text-emerald-400 mt-1">🎯 Target matched! 3 + (-8) = -5!</div>
  </div>
</div>
"""

# 2. sim-carrom-number-line
SIMS["sim-carrom-number-line"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-emerald-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-emerald-300">⚪ Carrom Coin Striker Track (-10 to +10)</div>
    <div class="text-[11px] font-bold text-slate-300">Position: <span id="coinPosText" class="text-amber-400 text-sm font-mono">0</span></div>
  </div>

  <!-- SVG Number Line & Animated Coin -->
  <div class="w-full bg-slate-950/90 rounded-lg p-3 border border-slate-800 flex flex-col items-center">
    <svg id="carromSvg" viewBox="-320 -60 640 120" class="w-full h-36">
      <!-- Main Track Axis -->
      <line x1="-300" y1="0" x2="300" y2="0" stroke="#475569" stroke-width="3" stroke-linecap="round"/>
      <polygon points="305,0 295,-5 295,5" fill="#475569"/>
      <polygon points="-305,0 -295,-5 -295,5" fill="#475569"/>
      
      <!-- Graduation Ticks and Numbers -->
      <!-- Ticks generated in JS -->
      <g id="carromTicksGroup"></g>
      
      <!-- Trajectory Arrow -->
      <path id="coinTrajectory" d="" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 4" opacity="0.8"/>
      
      <!-- Carrom Coin Puck -->
      <g id="carromPuck" transform="translate(0, 0)" class="transition-transform duration-500 ease-out cursor-pointer">
        <circle cx="0" cy="0" r="16" fill="url(#puckGrad)" stroke="#f59e0b" stroke-width="2.5" filter="drop-shadow(0 0 8px rgba(245,158,11,0.6))"/>
        <circle cx="0" cy="0" r="8" fill="#1e293b" opacity="0.6"/>
        <text id="puckText" x="0" y="4" text-anchor="middle" font-size="11" font-weight="bold" fill="#ffffff" font-family="monospace">0</text>
      </g>

      <defs>
        <radialGradient id="puckGrad" cx="30%" cy="30%">
          <stop offset="0%" stop-color="#fbbf24"/>
          <stop offset="100%" stop-color="#b45309"/>
        </radialGradient>
      </defs>
    </svg>
  </div>

  <!-- Vector Strike Controls -->
  <div class="flex flex-wrap items-center justify-between gap-1.5 pt-1">
    <div class="flex items-center gap-1.5">
      <span class="text-[11px] text-slate-400 font-semibold">Strike Vector:</span>
      <button class="px-2.5 py-1 rounded bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 font-bold text-xs" onclick="strikeCarrom(3)">+3 ➔</button>
      <button class="px-2.5 py-1 rounded bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 font-bold text-xs" onclick="strikeCarrom(5)">+5 ➔</button>
      <button class="px-2.5 py-1 rounded bg-rose-600/30 hover:bg-rose-600/50 text-rose-300 font-bold text-xs" onclick="strikeCarrom(-4)">⬅ -4</button>
      <button class="px-2.5 py-1 rounded bg-rose-600/30 hover:bg-rose-600/50 text-rose-300 font-bold text-xs" onclick="strikeCarrom(-6)">⬅ -6</button>
    </div>
    <button class="px-3 py-1 rounded bg-slate-700 hover:bg-slate-600 text-slate-200 text-xs font-bold" onclick="resetCarrom()">Reset Origin (0)</button>
  </div>
  <div id="carromActionMsg" class="text-[11px] text-center text-slate-300 font-mono">Puck resting at Origin (0). Click a strike vector!</div>
</div>
"""

# 3. sim-zero-pair-tokens
SIMS["sim-zero-pair-tokens"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-cyan-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-cyan-300">🟡 Token Model & Zero Pair Annihilation</div>
    <div class="text-[11px] font-bold text-slate-300">Net Value: <span id="tokenNetVal" class="text-emerald-400 text-sm font-mono font-extrabold">0</span></div>
  </div>

  <!-- Token Arena -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 min-h-[160px] flex flex-col items-center justify-center">
    <div class="flex justify-between w-full text-[11px] text-slate-400 font-semibold mb-2 px-2">
      <span>Green Gains (+1): <span id="countGreen" class="text-emerald-400 font-bold">0</span></span>
      <span>Zero Pairs Neutralized: <span id="countZeroPairs" class="text-amber-400 font-bold">0</span></span>
      <span>Red Debts (-1): <span id="countRed" class="text-rose-400 font-bold">0</span></span>
    </div>
    <div id="tokenGrid" class="flex flex-wrap gap-2 justify-center items-center p-2 min-h-[100px] w-full">
      <!-- Injected tokens -->
    </div>
  </div>

  <!-- Actions -->
  <div class="flex flex-wrap items-center justify-between gap-2">
    <div class="flex gap-2">
      <button class="px-3 py-1.5 rounded bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs flex items-center gap-1 shadow" onclick="addToken(1)">
        <span>+ Add Green (+1)</span>
      </button>
      <button class="px-3 py-1.5 rounded bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs flex items-center gap-1 shadow" onclick="addToken(-1)">
        <span>+ Add Red (-1)</span>
      </button>
    </div>
    <div class="flex gap-2">
      <button class="px-3 py-1.5 rounded bg-amber-600 hover:bg-amber-500 text-black font-bold text-xs shadow" onclick="annihilateZeroPairs()">
        ⚡ Form Zero Pairs
      </button>
      <button class="px-3 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs" onclick="resetTokens()">
        Clear Board
      </button>
    </div>
  </div>
</div>
"""

# 4. sim-subtraction-inverse
SIMS["sim-subtraction-inverse"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-purple-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-purple-300">🔄 Subtraction Transformer: Adding the Additive Inverse</div>
    <span class="text-[11px] text-amber-300 font-mono font-bold">$a - b = a + (-b)$</span>
  </div>

  <!-- Problem Selector -->
  <div class="flex flex-wrap items-center justify-between gap-2 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800">
    <div class="flex items-center gap-2 text-xs">
      <span class="text-slate-300 font-semibold">Select Case:</span>
      <button class="px-2.5 py-1 rounded bg-purple-600/40 hover:bg-purple-600 text-purple-200 text-xs font-bold" onclick="setSubCase(2, 5)">(+2) - (+5)</button>
      <button class="px-2.5 py-1 rounded bg-purple-600/40 hover:bg-purple-600 text-purple-200 text-xs font-bold" onclick="setSubCase(3, -4)">(+3) - (-4)</button>
      <button class="px-2.5 py-1 rounded bg-purple-600/40 hover:bg-purple-600 text-purple-200 text-xs font-bold" onclick="setSubCase(-2, -6)">(-2) - (-6)</button>
      <button class="px-2.5 py-1 rounded bg-purple-600/40 hover:bg-purple-600 text-purple-200 text-xs font-bold" onclick="setSubCase(-4, 3)">(-4) - (+3)</button>
    </div>
  </div>

  <!-- Transformation Stages Visualizer -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-3">
    <div class="flex items-center justify-around text-center">
      <div class="p-2 rounded bg-slate-900 border border-slate-700 min-w-[130px]">
        <div class="text-[10px] uppercase tracking-wider text-slate-400 font-bold">Original Subtraction</div>
        <div id="subOrigExpr" class="text-sm font-mono font-bold text-rose-400 mt-1">(+3) - (-4)</div>
      </div>
      <div class="text-lg font-bold text-amber-400">➔ Equivalent To ➔</div>
      <div class="p-2 rounded bg-emerald-950/40 border border-emerald-500/40 min-w-[130px]">
        <div class="text-[10px] uppercase tracking-wider text-emerald-300 font-bold">Adding Inverse</div>
        <div id="subInvExpr" class="text-sm font-mono font-bold text-emerald-300 mt-1">(+3) + (+4)</div>
      </div>
    </div>

    <!-- Explanatory Token Stage Box -->
    <div id="subStepBox" class="p-2.5 rounded bg-slate-900 text-xs text-slate-300 leading-relaxed border border-slate-800 font-mono">
      Loading transformation steps...
    </div>
  </div>
</div>
"""

# 5. sim-pos-times-neg
SIMS["sim-pos-times-neg"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-rose-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-rose-300">🔴 Positive × Negative: Repeated Addition of Debt Groups</div>
    <div class="text-xs font-bold text-amber-300 font-mono" id="ptnExpr">3 × (-4) = -12</div>
  </div>

  <div class="grid grid-cols-2 gap-3 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800">
    <div>
      <label class="text-[11px] font-semibold text-slate-300 flex justify-between">
        <span>Multiplier (Number of Groups):</span>
        <span id="ptnGroupsVal" class="text-emerald-400 font-bold">3</span>
      </label>
      <input id="ptnSliderGroups" type="range" min="1" max="5" value="3" class="w-full h-1.5 bg-slate-700 rounded-lg accent-emerald-400 cursor-pointer" oninput="updatePosTimesNeg()">
    </div>
    <div>
      <label class="text-[11px] font-semibold text-slate-300 flex justify-between">
        <span>Group Value (Red Tokens per Group):</span>
        <span id="ptnSizeVal" class="text-rose-400 font-bold">-4</span>
      </label>
      <input id="ptnSliderSize" type="range" min="1" max="5" value="4" class="w-full h-1.5 bg-slate-700 rounded-lg accent-rose-400 cursor-pointer" oninput="updatePosTimesNeg()">
    </div>
  </div>

  <!-- Groups Tray Display -->
  <div id="ptnTray" class="flex flex-wrap gap-2 justify-center items-center bg-slate-950/80 p-3 rounded-lg border border-slate-800 min-h-[100px]">
    <!-- Groups injected by JS -->
  </div>

  <div id="ptnSummary" class="text-xs text-center text-slate-300 font-mono bg-slate-900 p-2 rounded border border-slate-800">
    3 groups of (-4) = (-4) + (-4) + (-4) = -12 tokens!
  </div>
</div>
"""

# 6. sim-neg-times-pos
SIMS["sim-neg-times-pos"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-amber-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-amber-300">🏦 Negative × Positive: Removing Positive Tokens from Zero Bank</div>
    <div class="text-xs font-bold text-rose-400 font-mono" id="ntpExpr">(-3) × (+4) = -12</div>
  </div>

  <!-- Simulation Control Bar -->
  <div class="flex items-center justify-between bg-slate-950/60 p-2.5 rounded-lg border border-slate-800">
    <div class="text-xs text-slate-300">
      Problem: <span class="text-amber-400 font-bold">(-3) groups of (+4)</span>
    </div>
    <div class="flex gap-2">
      <button id="btnNtpStep" class="px-3 py-1 rounded bg-amber-600 hover:bg-amber-500 text-black font-bold text-xs" onclick="stepNtpRemoval()">
        1. Populate Neutral Bank (12 Zero Pairs)
      </button>
      <button class="px-2.5 py-1 rounded bg-slate-700 hover:bg-slate-600 text-slate-200 text-xs" onclick="resetNtp()">
        Reset
      </button>
    </div>
  </div>

  <!-- Visual Bank -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 min-h-[140px] flex flex-col items-center justify-center">
    <div id="ntpBankTitle" class="text-[11px] text-slate-400 mb-2 font-mono">Bank State: Empty (0)</div>
    <div id="ntpBankGrid" class="flex flex-wrap gap-2 justify-center items-center">
      <!-- Pairs injected here -->
    </div>
  </div>

  <div id="ntpExplanation" class="text-xs text-slate-300 font-mono bg-slate-900 p-2.5 rounded border border-slate-800 leading-relaxed">
    Click 'Populate Neutral Bank' to create 12 zero pairs with net value 0.
  </div>
</div>
"""

# 7. sim-neg-times-neg-tokens
SIMS["sim-neg-times-neg-tokens"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-emerald-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-emerald-300">✨ Negative × Negative: Debt Extraction Reveals Pure Wealth</div>
    <div class="text-xs font-bold text-emerald-400 font-mono" id="ntnExpr">(-3) × (-4) = +12</div>
  </div>

  <div class="flex items-center justify-between bg-slate-950/60 p-2.5 rounded-lg border border-slate-800">
    <div class="text-xs text-slate-300">
      Scenario: <span class="text-rose-400 font-bold">Remove 3 debts of (-4)</span>
    </div>
    <div class="flex gap-2">
      <button id="btnNtnAction" class="px-3 py-1 rounded bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs" onclick="stepNtnSimulation()">
        1. Place 12 Zero Pairs (Net Value 0)
      </button>
      <button class="px-2.5 py-1 rounded bg-slate-700 hover:bg-slate-600 text-slate-200 text-xs" onclick="resetNtn()">
        Reset
      </button>
    </div>
  </div>

  <!-- Visual Bank Arena -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 min-h-[140px] flex flex-col items-center justify-center">
    <div id="ntnBankStatus" class="text-[11px] text-slate-400 mb-2 font-mono">Bank Value: 0</div>
    <div id="ntnBankGrid" class="flex flex-wrap gap-2 justify-center items-center">
      <!-- Pairs injected here -->
    </div>
  </div>

  <div id="ntnDesc" class="text-xs text-slate-300 font-mono bg-slate-900 p-2.5 rounded border border-slate-800 leading-relaxed">
    Click step 1 to place 12 zero pairs (12 green $+$, 12 red $-$). Net value is exactly 0.
  </div>
</div>
"""

# 8. sim-multiplication-patterns
SIMS["sim-multiplication-patterns"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-sky-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-sky-300">🪜 Pattern Staircase: Decreasing Multiplier by 1</div>
    <div class="text-[11px] text-amber-300 font-mono">Fixed Multiplicand: <span id="mpFixedVal" class="font-bold">-3</span></div>
  </div>

  <!-- Multiplicand Chooser -->
  <div class="flex items-center gap-2 text-xs bg-slate-950/60 p-2 rounded-lg border border-slate-800">
    <span class="text-slate-300">Choose Multiplicand:</span>
    <button class="px-2.5 py-1 rounded bg-sky-600/40 hover:bg-sky-600 text-sky-200 font-bold" onclick="setPatternMultiplicand(-2)">× (-2)</button>
    <button class="px-2.5 py-1 rounded bg-sky-600/40 hover:bg-sky-600 text-sky-200 font-bold" onclick="setPatternMultiplicand(-3)">× (-3)</button>
    <button class="px-2.5 py-1 rounded bg-sky-600/40 hover:bg-sky-600 text-sky-200 font-bold" onclick="setPatternMultiplicand(-4)">× (-4)</button>
    <button class="px-2.5 py-1 rounded bg-sky-600/40 hover:bg-sky-600 text-sky-200 font-bold" onclick="setPatternMultiplicand(-5)">× (-5)</button>
  </div>

  <!-- Animated Staircase Table -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-1 font-mono text-xs" id="patternRowsContainer">
    <!-- Rows dynamically generated -->
  </div>
</div>
"""

# 9. sim-sign-rules-matrix
SIMS["sim-sign-rules-matrix"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-indigo-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-indigo-300">🧭 4-Quadrant Sign Rules & The -1 Inverter</div>
    <span class="text-[11px] text-slate-400 font-mono">Interactive Sign Explorer</span>
  </div>

  <!-- 4-Quadrant Grid -->
  <div class="grid grid-cols-2 gap-2.5">
    <div class="p-3 rounded-lg bg-emerald-950/30 border border-emerald-500/40 cursor-pointer hover:bg-emerald-900/30 transition-all" onclick="selectSignQuad('pp')">
      <div class="flex items-center justify-between text-xs font-bold text-emerald-400 mb-1">
        <span>(+) × (+)</span>
        <span>= (+) Positive</span>
      </div>
      <div class="text-[11px] text-slate-300 font-mono">Like Signs: $(+5) \times (+4) = +20$</div>
    </div>

    <div class="p-3 rounded-lg bg-rose-950/30 border border-rose-500/40 cursor-pointer hover:bg-rose-900/30 transition-all" onclick="selectSignQuad('pn')">
      <div class="flex items-center justify-between text-xs font-bold text-rose-400 mb-1">
        <span>(+) × (-)</span>
        <span>= (-) Negative</span>
      </div>
      <div class="text-[11px] text-slate-300 font-mono">Unlike Signs: $(+5) \times (-4) = -20$</div>
    </div>

    <div class="p-3 rounded-lg bg-rose-950/30 border border-rose-500/40 cursor-pointer hover:bg-rose-900/30 transition-all" onclick="selectSignQuad('np')">
      <div class="flex items-center justify-between text-xs font-bold text-rose-400 mb-1">
        <span>(-) × (+)</span>
        <span>= (-) Negative</span>
      </div>
      <div class="text-[11px] text-slate-300 font-mono">Unlike Signs: $(-5) \times (+4) = -20$</div>
    </div>

    <div class="p-3 rounded-lg bg-emerald-950/30 border border-emerald-500/40 cursor-pointer hover:bg-emerald-900/30 transition-all" onclick="selectSignQuad('nn')">
      <div class="flex items-center justify-between text-xs font-bold text-emerald-400 mb-1">
        <span>(-) × (-)</span>
        <span>= (+) Positive</span>
      </div>
      <div class="text-[11px] text-slate-300 font-mono">Like Signs: $(-5) \times (-4) = +20$</div>
    </div>
  </div>

  <!-- Special Multipliers Tester -->
  <div class="bg-slate-950/80 p-2.5 rounded-lg border border-slate-800 flex items-center justify-between text-xs">
    <div class="flex items-center gap-2">
      <span class="text-slate-300">Test Number:</span>
      <input id="signTestInput" type="number" value="17" class="w-16 px-2 py-0.5 rounded bg-slate-900 border border-slate-700 text-center font-bold text-amber-300 font-mono">
    </div>
    <div class="flex gap-2 font-mono">
      <button class="px-2 py-1 rounded bg-sky-600/40 hover:bg-sky-600 text-sky-200 text-xs font-bold" onclick="testSpecialMultiplier(1)">× 1 (Identity)</button>
      <button class="px-2 py-1 rounded bg-purple-600/40 hover:bg-purple-600 text-purple-200 text-xs font-bold" onclick="testSpecialMultiplier(-1)">× (-1) (Invert)</button>
      <button class="px-2 py-1 rounded bg-slate-700 hover:bg-slate-600 text-slate-200 text-xs font-bold" onclick="testSpecialMultiplier(0)">× 0 (Annihilate)</button>
    </div>
  </div>
  <div id="signTestResult" class="text-xs text-center text-emerald-300 font-mono">Select a quadrant or test special multipliers above!</div>
</div>
"""

# 10. sim-brahmagupta-scroll
SIMS["sim-brahmagupta-scroll"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-amber-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-amber-300">📜 Acharya Brahmagupta's Ledger & Balance (628 CE)</div>
    <span class="text-[10px] text-amber-400 font-serif italic">Brāhmasphuṭasiddhānta • Chapter 18</span>
  </div>

  <!-- Ancient Merchant Balance Scale SVG -->
  <div class="bg-slate-950/90 rounded-lg p-2 border border-slate-800 flex flex-col items-center">
    <svg id="brahmaScaleSvg" viewBox="0 0 400 160" class="w-full h-36">
      <!-- Fulcrum Pillar -->
      <polygon points="200,60 185,140 215,140" fill="#78350f" stroke="#d97706" stroke-width="2"/>
      <circle cx="200" cy="60" r="6" fill="#fde047"/>

      <!-- Lever Beam (Pivots with angle) -->
      <g id="scaleBeam" transform="rotate(0, 200, 60)">
        <line x1="80" y1="60" x2="320" y2="60" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
        <!-- Left Pan Strings & Pan (Dhana - Gold Fortunes) -->
        <line x1="100" y1="60" x2="80" y2="110" stroke="#94a3b8" stroke-width="1.5"/>
        <line x1="100" y1="60" x2="120" y2="110" stroke="#94a3b8" stroke-width="1.5"/>
        <path d="M 70,110 Q 100,125 130,110 Z" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="100" y="138" font-size="10" fill="#38bdf8" text-anchor="middle" font-weight="bold">Dhana (Fortune)</text>
        <g id="leftPanTokens" transform="translate(100, 105)"></g>

        <!-- Right Pan Strings & Pan (Rna - Promissory Debts) -->
        <line x1="300" y1="60" x2="280" y2="110" stroke="#94a3b8" stroke-width="1.5"/>
        <line x1="300" y1="60" x2="320" y2="110" stroke="#94a3b8" stroke-width="1.5"/>
        <path d="M 270,110 Q 300,125 330,110 Z" fill="#881337" stroke="#f43f5e" stroke-width="1.5"/>
        <text x="300" y="138" font-size="10" fill="#f43f5e" text-anchor="middle" font-weight="bold">Ṛṇa (Debt)</text>
        <g id="rightPanTokens" transform="translate(300, 105)"></g>
      </g>
    </svg>
  </div>

  <!-- Interactive Shloka Rules -->
  <div class="grid grid-cols-3 gap-2">
    <button class="p-2 rounded bg-amber-950/40 border border-amber-500/30 hover:bg-amber-900/50 text-left text-xs" onclick="demonstrateBrahmaguptaRule('dhana_dhana')">
      <div class="text-amber-300 font-bold">1. Dhana × Dhana</div>
      <div class="text-[10px] text-slate-300">Fortune × Fortune = Fortune</div>
    </button>
    <button class="p-2 rounded bg-amber-950/40 border border-amber-500/30 hover:bg-amber-900/50 text-left text-xs" onclick="demonstrateBrahmaguptaRule('rna_rna')">
      <div class="text-amber-300 font-bold">2. Ṛṇa × Ṛṇa</div>
      <div class="text-[10px] text-emerald-300">Debt × Debt = Fortune!</div>
    </button>
    <button class="p-2 rounded bg-amber-950/40 border border-amber-500/30 hover:bg-amber-900/50 text-left text-xs" onclick="demonstrateBrahmaguptaRule('dhana_rna')">
      <div class="text-amber-300 font-bold">3. Dhana × Ṛṇa</div>
      <div class="text-[10px] text-rose-300">Fortune × Debt = Debt</div>
    </button>
  </div>
  <div id="brahmaTextDisplay" class="text-xs text-amber-200 font-mono bg-slate-950 p-2 rounded border border-slate-800">
    Select a rule above to observe Brahmagupta's ancient ledger balance in action!
  </div>
</div>
"""

# 11. sim-real-world-integers
SIMS["sim-real-world-integers"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-teal-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-teal-300">🌍 Real-World Scenarios: Elevators & Exam Scores</div>
    <div class="flex gap-1.5 text-xs">
      <button class="px-2.5 py-1 rounded bg-teal-600/40 hover:bg-teal-600 text-teal-200 font-bold" onclick="setRwTab('elevator')">🏗️ Mine Elevator</button>
      <button class="px-2.5 py-1 rounded bg-teal-600/40 hover:bg-teal-600 text-teal-200 font-bold" onclick="setRwTab('quiz')">📝 Exam Scoring</button>
    </div>
  </div>

  <!-- Elevator View -->
  <div id="rwElevatorView" class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2">
    <div class="flex items-center justify-between text-xs">
      <span class="text-slate-300">Starting Position: <strong class="text-amber-400">+10 m</strong> above ground</span>
      <span class="text-slate-300">Descent Rate: <strong class="text-rose-400">-6 m / minute</strong></span>
    </div>
    <div class="flex items-center gap-3">
      <label class="text-xs text-slate-400">Time Elapsed:</label>
      <input id="elevatorTimeSlider" type="range" min="0" max="60" value="35" class="flex-1 h-1.5 bg-slate-700 rounded-lg accent-teal-400 cursor-pointer" oninput="updateElevatorSim()">
      <span id="elevatorTimeVal" class="text-xs font-mono font-bold text-teal-300 w-16">35 min</span>
    </div>
    <div class="p-2.5 rounded bg-slate-900 text-xs font-mono flex items-center justify-between">
      <span id="elevatorCalc">Position = 10 + [35 × (-6)] = 10 - 210</span>
      <span id="elevatorDepthResult" class="font-extrabold text-amber-400 text-sm">-200 m (Depth)</span>
    </div>
  </div>

  <!-- Exam Scoring View -->
  <div id="rwQuizView" class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2" style="display:none;">
    <div class="grid grid-cols-2 gap-3 text-xs">
      <div>
        <label class="text-slate-300 flex justify-between"><span>Correct Answers (+4 ea):</span> <span id="quizCorrVal" class="font-bold text-emerald-400">12</span></label>
        <input id="quizCorrSlider" type="range" min="0" max="20" value="12" class="w-full h-1.5 bg-slate-700 rounded accent-emerald-400 cursor-pointer" oninput="updateQuizSim()">
      </div>
      <div>
        <label class="text-slate-300 flex justify-between"><span>Wrong Answers (-2 ea):</span> <span id="quizWrongVal" class="font-bold text-rose-400">5</span></label>
        <input id="quizWrongSlider" type="range" min="0" max="20" value="5" class="w-full h-1.5 bg-slate-700 rounded accent-rose-400 cursor-pointer" oninput="updateQuizSim()">
      </div>
    </div>
    <div class="p-2.5 rounded bg-slate-900 text-xs font-mono flex items-center justify-between">
      <span id="quizCalcExpr">(12 × 4) + [5 × (-2)] = 48 - 10</span>
      <span id="quizTotalResult" class="font-extrabold text-emerald-400 text-sm">38 Marks</span>
    </div>
  </div>
</div>
"""

# 12. sim-comm-assoc-engine
SIMS["sim-comm-assoc-engine"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-blue-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-blue-300">⚖️ Commutative & Associative Law Laboratory</div>
    <div class="flex gap-1.5 text-xs">
      <button class="px-2.5 py-1 rounded bg-blue-600/40 hover:bg-blue-600 text-blue-200 font-bold" onclick="setPropTab('comm')">Commutative</button>
      <button class="px-2.5 py-1 rounded bg-blue-600/40 hover:bg-blue-600 text-blue-200 font-bold" onclick="setPropTab('assoc')">Associative</button>
    </div>
  </div>

  <div id="propCommView" class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-3">
    <div class="flex items-center justify-around font-mono text-center">
      <div class="p-2 rounded bg-slate-900 border border-slate-700 min-w-[120px]">
        <div class="text-[10px] text-slate-400">Order 1 (a × b)</div>
        <div id="commExpr1" class="text-sm font-bold text-sky-400 mt-1">(-6) × 4 = -24</div>
      </div>
      <div class="text-xl font-bold text-amber-400">=</div>
      <div class="p-2 rounded bg-slate-900 border border-slate-700 min-w-[120px]">
        <div class="text-[10px] text-slate-400">Order 2 (b × a)</div>
        <div id="commExpr2" class="text-sm font-bold text-emerald-400 mt-1">4 × (-6) = -24</div>
      </div>
    </div>
    <button class="w-full py-1.5 rounded bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs shadow" onclick="swapCommutativeOrder()">
      🔄 Swap Order of Factors ($a \leftrightarrow b$)
    </button>
  </div>

  <div id="propAssocView" class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-3" style="display:none;">
    <div class="flex items-center justify-around font-mono text-center">
      <div class="p-2 rounded bg-slate-900 border border-slate-700 min-w-[140px]">
        <div class="text-[10px] text-slate-400">Grouping 1: [a × b] × c</div>
        <div id="assocExpr1" class="text-xs font-bold text-sky-400 mt-1">[(-3) × 4] × (-5)</div>
        <div class="text-emerald-400 font-bold text-sm">= +60</div>
      </div>
      <div class="text-xl font-bold text-amber-400">=</div>
      <div class="p-2 rounded bg-slate-900 border border-slate-700 min-w-[140px]">
        <div class="text-[10px] text-slate-400">Grouping 2: a × [b × c]</div>
        <div id="assocExpr2" class="text-xs font-bold text-purple-400 mt-1">(-3) × [4 × (-5)]</div>
        <div class="text-emerald-400 font-bold text-sm">= +60</div>
      </div>
    </div>
    <button class="w-full py-1.5 rounded bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow" onclick="shiftAssociativeBrackets()">
      📦 Shift Grouping Brackets
    </button>
  </div>
</div>
"""

# 13. sim-distributive-grid
SIMS["sim-distributive-grid"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-emerald-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-emerald-300">📐 Distributive Property: Split-Rectangle Array</div>
    <div class="text-xs font-bold text-amber-300 font-mono" id="distribTitleExpr">a × (b + c) = ab + ac</div>
  </div>

  <!-- Sliders -->
  <div class="grid grid-cols-3 gap-2 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800 text-xs">
    <div>
      <label class="text-slate-300 flex justify-between"><span>Height a:</span> <span id="distValA" class="font-bold text-amber-400">-4</span></label>
      <input id="distSliderA" type="range" min="-6" max="-1" value="-4" class="w-full h-1.5 bg-slate-700 rounded accent-amber-400 cursor-pointer" oninput="updateDistributiveGrid()">
    </div>
    <div>
      <label class="text-slate-300 flex justify-between"><span>Width b:</span> <span id="distValB" class="font-bold text-sky-400">6</span></label>
      <input id="distSliderB" type="range" min="2" max="8" value="6" class="w-full h-1.5 bg-slate-700 rounded accent-sky-400 cursor-pointer" oninput="updateDistributiveGrid()">
    </div>
    <div>
      <label class="text-slate-300 flex justify-between"><span>Width c:</span> <span id="distValC" class="font-bold text-emerald-400">4</span></label>
      <input id="distSliderC" type="range" min="2" max="8" value="4" class="w-full h-1.5 bg-slate-700 rounded accent-emerald-400 cursor-pointer" oninput="updateDistributiveGrid()">
    </div>
  </div>

  <!-- SVG Visual Split Rectangle -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col items-center justify-center">
    <svg id="distribSvg" viewBox="0 0 360 120" class="w-full h-32">
      <!-- Left Sub-Rectangle (a x b) -->
      <rect id="rectLeft" x="20" y="20" width="180" height="70" fill="rgba(56,189,248,0.25)" stroke="#38bdf8" stroke-width="2" rx="4"/>
      <text id="rectLeftText" x="110" y="60" text-anchor="middle" font-size="12" font-weight="bold" fill="#38bdf8" font-family="monospace">(-4) × 6 = -24</text>
      
      <!-- Right Sub-Rectangle (a x c) -->
      <rect id="rectRight" x="205" y="20" width="130" height="70" fill="rgba(16,185,129,0.25)" stroke="#10b981" stroke-width="2" rx="4"/>
      <text id="rectRightText" x="270" y="60" text-anchor="middle" font-size="12" font-weight="bold" fill="#10b981" font-family="monospace">(-4) × 4 = -16</text>
    </svg>
    <div id="distribEvalSummary" class="text-xs font-mono text-center text-slate-200 mt-1">
      (-4) × (6 + 4) = (-4) × 10 = -40 = [(-24) + (-16)]!
    </div>
  </div>
</div>
"""

# 14. sim-multiple-integers-parity
SIMS["sim-multiple-integers-parity"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-violet-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-violet-300">🔗 Sign Parity Chain: Counting Negative Factors</div>
    <div class="text-xs font-mono font-bold text-amber-300" id="parityCountBadge">Negatives: 3 (ODD)</div>
  </div>

  <!-- Interactive Factors Chain -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-3">
    <div id="factorsChainList" class="flex flex-wrap items-center justify-center gap-2">
      <!-- 5 Factor chips injected by JS -->
    </div>

    <!-- Pairwise Cancellation Graphic Display -->
    <div id="pairwiseCancellationBox" class="p-2.5 rounded bg-slate-900 border border-slate-800 min-h-[50px] flex items-center justify-center gap-4 text-xs font-mono">
      <!-- Cancelled pairs shown here -->
    </div>
  </div>

  <div class="flex items-center justify-between text-xs">
    <button class="px-3 py-1.5 rounded bg-violet-600 hover:bg-violet-500 text-white font-bold shadow" onclick="randomizeFactorsChain()">
      🎲 Randomize Factors
    </button>
    <div id="parityResultMsg" class="font-mono font-bold text-rose-400 text-sm">
      Result: NEGATIVE (-)
    </div>
  </div>
</div>
"""

# 15. sim-division-missing-factor
SIMS["sim-division-missing-factor"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-cyan-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-cyan-300">⚖️ Missing Factor: Division as Multiplication in Reverse</div>
    <span class="text-xs font-mono text-amber-300">$a \div b = ? \iff b \times ? = a$</span>
  </div>

  <!-- Input Problem -->
  <div class="flex flex-wrap items-center justify-between gap-2 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800 text-xs">
    <span class="text-slate-300 font-semibold">Try Example:</span>
    <button class="px-2.5 py-1 rounded bg-cyan-600/40 hover:bg-cyan-600 text-cyan-200 font-bold" onclick="setDivExample(-24, 6)">(-24) ÷ 6</button>
    <button class="px-2.5 py-1 rounded bg-cyan-600/40 hover:bg-cyan-600 text-cyan-200 font-bold" onclick="setDivExample(-24, -4)">(-24) ÷ (-4)</button>
    <button class="px-2.5 py-1 rounded bg-cyan-600/40 hover:bg-cyan-600 text-cyan-200 font-bold" onclick="setDivExample(35, -5)">35 ÷ (-5)</button>
    <button class="px-2.5 py-1 rounded bg-rose-600/40 hover:bg-rose-600 text-rose-200 font-bold" onclick="setDivExample(-15, 0)">(-15) ÷ 0 (Undefined)</button>
  </div>

  <!-- Visual Inversion Board -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-3 items-center">
    <div class="flex items-center justify-around w-full font-mono text-center">
      <div class="p-2 rounded bg-slate-900 border border-slate-700 min-w-[130px]">
        <div class="text-[10px] text-slate-400">Division Task</div>
        <div id="divTaskExpr" class="text-base font-bold text-cyan-400 mt-1">(-24) ÷ 6 = ?</div>
      </div>
      <div class="text-xl font-bold text-amber-400">⟺</div>
      <div class="p-2 rounded bg-slate-900 border border-slate-700 min-w-[130px]">
        <div class="text-[10px] text-slate-400">Missing Factor Equation</div>
        <div id="divEqExpr" class="text-base font-bold text-emerald-400 mt-1">6 × ? = -24</div>
      </div>
    </div>

    <div id="divSolutionBox" class="p-2 rounded bg-emerald-950/40 border border-emerald-500/30 text-xs font-mono text-emerald-300 w-full text-center">
      Since $6 \times (-4) = -24$, the missing factor $? = -4$! Thus $(-24) \div 6 = -4$.
    </div>
  </div>
</div>
"""

# 16. sim-division-rules-lab
SIMS["sim-division-rules-lab"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-pink-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-pink-300">🚫 Division Rule Diagnostic: Commutative Failure Test</div>
    <span class="text-[11px] text-rose-400 font-mono font-bold">$a \div b \neq b \div a$</span>
  </div>

  <!-- Commutativity Tester Inputs -->
  <div class="grid grid-cols-2 gap-3 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800 text-xs">
    <div>
      <label class="text-slate-300 flex justify-between"><span>Dividend a:</span> <span id="divNonCommValA" class="font-bold text-amber-400">-20</span></label>
      <input id="divSliderA" type="range" min="-30" max="30" value="-20" class="w-full h-1.5 bg-slate-700 rounded accent-amber-400 cursor-pointer" oninput="updateDivisionDiagnostic()">
    </div>
    <div>
      <label class="text-slate-300 flex justify-between"><span>Divisor b:</span> <span id="divNonCommValB" class="font-bold text-sky-400">5</span></label>
      <input id="divSliderB" type="range" min="-10" max="10" value="5" class="w-full h-1.5 bg-slate-700 rounded accent-sky-400 cursor-pointer" oninput="updateDivisionDiagnostic()">
    </div>
  </div>

  <!-- Comparison Displays -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2">
    <div class="flex items-center justify-around font-mono text-center">
      <div class="p-2 rounded bg-slate-900 border border-slate-700 min-w-[130px]">
        <div class="text-[10px] text-slate-400">Case 1: a ÷ b</div>
        <div id="divDiagRes1" class="text-sm font-bold text-amber-400 mt-1">(-20) ÷ 5 = -4</div>
      </div>
      <div class="text-xl font-bold text-rose-500">≠</div>
      <div class="p-2 rounded bg-slate-900 border border-slate-700 min-w-[130px]">
        <div class="text-[10px] text-slate-400">Case 2: b ÷ a</div>
        <div id="divDiagRes2" class="text-sm font-bold text-sky-400 mt-1">5 ÷ (-20) = -0.25</div>
      </div>
    </div>
    <div id="divDiagVerdict" class="text-xs text-center text-rose-300 font-mono mt-1">
      ❌ $-4 \neq -0.25$. Integer division is strictly NOT commutative!
    </div>
  </div>
</div>
"""

code = f'''# -*- coding: utf-8 -*-
"""
Class 7 Mathematics - Chapter 10: Operations with Integers Simulators
Contains 16 bespoke SVG simulator templates.
"""

SIMULATORS = {repr(SIMS)}
'''

with open('.agents/class7_math_operations_with_integers_sims.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Generated .agents/class7_math_operations_with_integers_sims.py successfully!")

