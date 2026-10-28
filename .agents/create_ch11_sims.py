# -*- coding: utf-8 -*-
"""
Script to create .agents/class7_math_finding_common_ground_sims.py
Defines the HTML/SVG markup for all 16 simulators.
"""

SIMS = {}

# 1. sim-floor-tiler
SIMS["sim-floor-tiler"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-amber-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-amber-300">🏠 Room Floor Tiling Simulator (HCF)</div>
    <div class="text-[11px] font-bold text-slate-300" id="tilerStatus">Tile fits perfectly! (Common Factor)</div>
  </div>

  <div class="grid grid-cols-3 gap-2 bg-slate-950/60 p-2 rounded-lg border border-slate-800 text-xs">
    <div>
      <label class="text-slate-300 flex justify-between"><span>Length L:</span> <span id="tilerValL" class="font-bold text-sky-400">12 m</span></label>
      <input id="tilerSliderL" type="range" min="6" max="24" step="2" value="12" class="w-full h-1.5 bg-slate-700 rounded accent-sky-400 cursor-pointer" oninput="updateFloorTiler()">
    </div>
    <div>
      <label class="text-slate-300 flex justify-between"><span>Width W:</span> <span id="tilerValW" class="font-bold text-emerald-400">18 m</span></label>
      <input id="tilerSliderW" type="range" min="6" max="24" step="2" value="18" class="w-full h-1.5 bg-slate-700 rounded accent-emerald-400 cursor-pointer" oninput="updateFloorTiler()">
    </div>
    <div>
      <label class="text-slate-300 flex justify-between"><span>Tile Side S:</span> <span id="tilerValS" class="font-bold text-amber-400">6 m</span></label>
      <input id="tilerSliderS" type="range" min="1" max="8" step="1" value="6" class="w-full h-1.5 bg-slate-700 rounded accent-amber-400 cursor-pointer" oninput="updateFloorTiler()">
    </div>
  </div>

  <!-- SVG Floor Grid View -->
  <div class="bg-slate-950/80 p-2 rounded-lg border border-slate-800 flex flex-col items-center justify-center">
    <svg id="tilerSvg" viewBox="0 0 320 160" class="w-full h-36">
      <rect id="tilerRoomOutline" x="20" y="10" width="280" height="140" fill="#0f172a" stroke="#64748b" stroke-width="2" rx="4"/>
      <g id="tilerGridGroup"></g>
    </svg>
    <div id="tilerSummary" class="text-xs font-mono text-center text-slate-300 mt-1">
      Room 12m × 18m paved with 6m square tiles: 2 × 3 = 6 tiles (Zero cuts, Largest size = HCF)!
    </div>
  </div>
</div>
"""

# 2. sim-factor-venn
SIMS["sim-factor-venn"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-sky-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-sky-300">⭕ Two-Circle Factor Venn Diagram & HCF</div>
    <div class="text-xs font-bold text-amber-300 font-mono" id="vennHcfText">HCF(24, 36) = 12</div>
  </div>

  <!-- Input pair -->
  <div class="flex items-center justify-between gap-3 bg-slate-950/60 p-2 rounded-lg border border-slate-800 text-xs">
    <div class="flex items-center gap-2">
      <span class="text-slate-300">Number A:</span>
      <input id="vennInputA" type="number" min="4" max="100" value="24" class="w-16 px-2 py-0.5 rounded bg-slate-900 border border-slate-700 font-bold text-sky-400 font-mono" onchange="updateFactorVenn()">
    </div>
    <div class="flex items-center gap-2">
      <span class="text-slate-300">Number B:</span>
      <input id="vennInputB" type="number" min="4" max="100" value="36" class="w-16 px-2 py-0.5 rounded bg-slate-900 border border-slate-700 font-bold text-emerald-400 font-mono" onchange="updateFactorVenn()">
    </div>
    <button class="px-3 py-1 rounded bg-sky-600 hover:bg-sky-500 text-white font-bold" onclick="updateFactorVenn()">Analyze Sets</button>
  </div>

  <!-- SVG Venn Diagram -->
  <div class="bg-slate-950/80 p-2 rounded-lg border border-slate-800 flex flex-col items-center">
    <svg id="vennSvg" viewBox="0 0 360 160" class="w-full h-40">
      <!-- Circle A -->
      <circle cx="140" cy="80" r="70" fill="rgba(56,189,248,0.2)" stroke="#38bdf8" stroke-width="2"/>
      <text x="100" y="25" fill="#38bdf8" font-size="11" font-weight="bold">Factors of A</text>
      <!-- Circle B -->
      <circle cx="220" cy="80" r="70" fill="rgba(16,185,129,0.2)" stroke="#10b981" stroke-width="2"/>
      <text x="260" y="25" fill="#10b981" font-size="11" font-weight="bold">Factors of B</text>
      
      <!-- Factors text nodes -->
      <g id="vennOnlyA" font-size="10" fill="#94a3b8" text-anchor="middle" font-family="monospace"></g>
      <g id="vennCommon" font-size="10" fill="#fbbf24" font-weight="bold" text-anchor="middle" font-family="monospace"></g>
      <g id="vennOnlyB" font-size="10" fill="#94a3b8" text-anchor="middle" font-family="monospace"></g>
    </svg>
    <div id="vennDesc" class="text-xs text-center font-mono text-slate-300 mt-1">
      Common Factors in intersection: {1, 2, 3, 4, 6, 12}. The greatest is 12!
    </div>
  </div>
</div>
"""

# 3. sim-prime-factor-tree
SIMS["sim-prime-factor-tree"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-emerald-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-emerald-300">🌳 Prime Factor Tree Builder (Atomic Primes)</div>
    <div class="flex gap-1.5">
      <button class="px-2 py-0.5 rounded bg-emerald-600/40 hover:bg-emerald-600 text-emerald-200 text-xs font-bold" onclick="loadTreeNumber(60)">60</button>
      <button class="px-2 py-0.5 rounded bg-emerald-600/40 hover:bg-emerald-600 text-emerald-200 text-xs font-bold" onclick="loadTreeNumber(72)">72</button>
      <button class="px-2 py-0.5 rounded bg-emerald-600/40 hover:bg-emerald-600 text-emerald-200 text-xs font-bold" onclick="loadTreeNumber(90)">90</button>
    </div>
  </div>

  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 min-h-[160px] flex flex-col items-center justify-center">
    <div id="treeContainer" class="flex flex-col items-center gap-3 w-full">
      <!-- Tree nodes rendered by JS -->
    </div>
  </div>

  <div id="treePrimeLeaves" class="text-xs text-center font-mono text-emerald-300 bg-slate-950 p-2 rounded border border-slate-800">
    Prime Factorisation: 60 = 2² × 3 × 5 (Unique up to order!)
  </div>
</div>
"""

# 4. sim-hcf-prime-powers
SIMS["sim-hcf-prime-powers"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-cyan-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-cyan-300">📊 HCF by Prime Powers: Minimum Exponent Overlap</div>
    <span class="text-xs font-mono font-bold text-amber-300" id="hcfPrimeResult">HCF = 24</span>
  </div>

  <!-- Number Selector -->
  <div class="grid grid-cols-2 gap-3 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800 text-xs">
    <div class="p-2 rounded bg-slate-900 border border-slate-800">
      <div class="font-bold text-sky-400 mb-1">Number A: 72 = 2³ × 3²</div>
      <div class="text-[11px] text-slate-400">Primes: Base 2 (pow 3), Base 3 (pow 2)</div>
    </div>
    <div class="p-2 rounded bg-slate-900 border border-slate-800">
      <div class="font-bold text-emerald-400 mb-1">Number B: 120 = 2³ × 3¹ × 5¹</div>
      <div class="text-[11px] text-slate-400">Primes: Base 2 (pow 3), Base 3 (pow 1), Base 5 (pow 1)</div>
    </div>
  </div>

  <!-- Power Comparison Columns -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex justify-around items-center text-xs font-mono">
    <div class="p-2 rounded bg-slate-900 border border-slate-700 flex flex-col items-center min-w-[70px]">
      <span class="text-slate-400 font-bold">Base 2</span>
      <span class="text-slate-300 text-[11px]">min(3, 3)</span>
      <span class="text-amber-400 font-bold text-sm mt-1">2³ = 8</span>
    </div>
    <div class="text-slate-500 font-bold text-lg">×</div>
    <div class="p-2 rounded bg-slate-900 border border-slate-700 flex flex-col items-center min-w-[70px]">
      <span class="text-slate-400 font-bold">Base 3</span>
      <span class="text-slate-300 text-[11px]">min(2, 1)</span>
      <span class="text-amber-400 font-bold text-sm mt-1">3¹ = 3</span>
    </div>
    <div class="text-slate-500 font-bold text-lg">×</div>
    <div class="p-2 rounded bg-slate-900 border border-slate-700 flex flex-col items-center min-w-[70px]">
      <span class="text-slate-400 font-bold">Base 5</span>
      <span class="text-slate-300 text-[11px]">min(0, 1)</span>
      <span class="text-slate-500 font-bold text-sm mt-1">5⁰ = 1</span>
    </div>
  </div>

  <div class="text-xs text-center font-mono text-emerald-300 bg-slate-900 p-2 rounded border border-slate-800">
    HCF extracts the minimum common power: 2³ × 3¹ = 8 × 3 = 24!
  </div>
</div>
"""

# 5. sim-conjecture-tester
SIMS["sim-conjecture-tester"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-rose-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-rose-300">🕵️ Conjecture & Counterexample Detective Lab</div>
    <span class="text-[11px] text-slate-400">Test Number Theory Claims</span>
  </div>

  <div class="flex flex-col gap-2 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800 text-xs">
    <label class="text-slate-300 font-semibold">Select a Conjecture to Investigate:</label>
    <div class="flex flex-col gap-1.5">
      <button class="p-2 rounded bg-slate-900 hover:bg-slate-800 text-left border border-slate-700 text-slate-200" onclick="testConjecture(1)">
        1. "The HCF of any two even numbers is always 2."
      </button>
      <button class="p-2 rounded bg-slate-900 hover:bg-slate-800 text-left border border-slate-700 text-slate-200" onclick="testConjecture(2)">
        2. "If HCF(a, b) = 1, then both a and b must be prime numbers."
      </button>
      <button class="p-2 rounded bg-slate-900 hover:bg-slate-800 text-left border border-slate-700 text-slate-200" onclick="testConjecture(3)">
        3. "The LCM of two numbers is always greater than both numbers."
      </button>
    </div>
  </div>

  <div id="conjectureResultBox" class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-1.5 text-xs font-mono">
    <div class="text-amber-300 font-bold">Click a conjecture above to hunt for counterexamples!</div>
    <div class="text-slate-400">Discover how a single counterexample shatters an unproven claim.</div>
  </div>
</div>
"""

# 6. sim-toran-strip-aligner
SIMS["sim-toran-strip-aligner"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-teal-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-teal-300">🎊 Toran Cloth Strips Synchronizer (LCM)</div>
    <span class="text-xs font-mono font-bold text-amber-300" id="toranLcmText">LCM(6, 8) = 24 cm</span>
  </div>

  <div class="grid grid-cols-2 gap-3 bg-slate-950/60 p-2 rounded-lg border border-slate-800 text-xs">
    <div class="flex items-center justify-between">
      <span>Strip A Length: <strong class="text-sky-400">6 cm</strong></span>
      <button class="px-2.5 py-1 rounded bg-sky-600 hover:bg-sky-500 text-white font-bold" onclick="addToranStrip('A')">+ Add Strip A</button>
    </div>
    <div class="flex items-center justify-between">
      <span>Strip B Length: <strong class="text-emerald-400">8 cm</strong></span>
      <button class="px-2.5 py-1 rounded bg-emerald-600 hover:bg-emerald-500 text-white font-bold" onclick="addToranStrip('B')">+ Add Strip B</button>
    </div>
  </div>

  <!-- Toran Track Display -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-3">
    <div>
      <div class="text-[10px] text-sky-400 font-bold mb-1">Row A Total: <span id="rowLenA" class="font-mono">0 cm</span></div>
      <div id="toranTrackA" class="flex gap-1 h-6 items-center bg-slate-900 rounded p-1 border border-slate-800 overflow-x-auto"></div>
    </div>
    <div>
      <div class="text-[10px] text-emerald-400 font-bold mb-1">Row B Total: <span id="rowLenB" class="font-mono">0 cm</span></div>
      <div id="toranTrackB" class="flex gap-1 h-6 items-center bg-slate-900 rounded p-1 border border-slate-800 overflow-x-auto"></div>
    </div>
  </div>

  <div class="flex items-center justify-between text-xs">
    <div id="toranMatchStatus" class="font-mono text-slate-400">Add strips until both rows align at the same total length!</div>
    <button class="px-3 py-1 rounded bg-slate-700 hover:bg-slate-600 text-slate-200" onclick="resetToran()">Reset</button>
  </div>
</div>
"""

# 7. sim-lcm-multiples-stepper
SIMS["sim-lcm-multiples-stepper"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-indigo-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-indigo-300">🏃 Dual-Track Stepper: First Shared Locus (LCM)</div>
    <span class="text-xs font-mono font-bold text-amber-300" id="stepperLcmBanner">LCM(4, 6) = 12</span>
  </div>

  <div class="flex items-center justify-between bg-slate-950/60 p-2 rounded-lg border border-slate-800 text-xs">
    <div class="flex items-center gap-2">
      <span class="text-slate-300">Leap A:</span>
      <button class="px-2 py-0.5 rounded bg-sky-600/40 text-sky-300 font-bold" onclick="setStepperLeap(3, 4)">3 & 4</button>
      <button class="px-2 py-0.5 rounded bg-sky-600/40 text-sky-300 font-bold" onclick="setStepperLeap(4, 6)">4 & 6</button>
      <button class="px-2 py-0.5 rounded bg-sky-600/40 text-sky-300 font-bold" onclick="setStepperLeap(5, 7)">5 & 7</button>
    </div>
    <button class="px-3 py-1 rounded bg-indigo-600 hover:bg-indigo-500 text-white font-bold" onclick="stepBothRunners()">
      ▶ Step Runners
    </button>
  </div>

  <!-- Stepper Track SVG -->
  <div class="bg-slate-950/80 p-2 rounded-lg border border-slate-800 flex flex-col items-center">
    <svg id="stepperSvg" viewBox="0 0 340 100" class="w-full h-28">
      <line x1="20" y1="40" x2="320" y2="40" stroke="#334155" stroke-width="2"/>
      <line x1="20" y1="75" x2="320" y2="75" stroke="#334155" stroke-width="2"/>
      <g id="stepperMarksGroup"></g>
      <!-- Runners -->
      <circle id="runnerA" cx="20" cy="40" r="7" fill="#38bdf8"/>
      <circle id="runnerB" cx="20" cy="75" r="7" fill="#10b981"/>
    </svg>
    <div id="stepperLog" class="text-xs font-mono text-center text-slate-300 mt-1">
      Runner A leaps by 4, Runner B leaps by 6. Click 'Step Runners' to trace footprints!
    </div>
  </div>
</div>
"""

# 8. sim-lcm-prime-union
SIMS["sim-lcm-prime-union"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-violet-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-violet-300">📈 LCM by Prime Powers: Maximum Exponent Union</div>
    <span class="text-xs font-mono font-bold text-emerald-400" id="lcmPrimeResult">LCM = 360</span>
  </div>

  <div class="grid grid-cols-2 gap-3 bg-slate-950/60 p-2 rounded-lg border border-slate-800 text-xs">
    <div class="p-2 rounded bg-slate-900 border border-slate-800">
      <div class="font-bold text-sky-400 mb-0.5">Number A: 72 = 2³ × 3²</div>
      <div class="text-[11px] text-slate-400">Exponents: 2³ and 3²</div>
    </div>
    <div class="p-2 rounded bg-slate-900 border border-slate-800">
      <div class="font-bold text-emerald-400 mb-0.5">Number B: 120 = 2³ × 3¹ × 5¹</div>
      <div class="text-[11px] text-slate-400">Exponents: 2³, 3¹, 5¹</div>
    </div>
  </div>

  <!-- Max Power Extraction Boxes -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex justify-around items-center text-xs font-mono">
    <div class="p-2 rounded bg-slate-900 border border-slate-700 flex flex-col items-center min-w-[70px]">
      <span class="text-slate-400 font-bold">Base 2</span>
      <span class="text-slate-300 text-[11px]">max(3, 3)</span>
      <span class="text-emerald-400 font-bold text-sm mt-1">2³ = 8</span>
    </div>
    <div class="text-slate-500 font-bold text-lg">×</div>
    <div class="p-2 rounded bg-slate-900 border border-slate-700 flex flex-col items-center min-w-[70px]">
      <span class="text-slate-400 font-bold">Base 3</span>
      <span class="text-slate-300 text-[11px]">max(2, 1)</span>
      <span class="text-emerald-400 font-bold text-sm mt-1">3² = 9</span>
    </div>
    <div class="text-slate-500 font-bold text-lg">×</div>
    <div class="p-2 rounded bg-slate-900 border border-slate-700 flex flex-col items-center min-w-[70px]">
      <span class="text-slate-400 font-bold">Base 5</span>
      <span class="text-slate-300 text-[11px]">max(0, 1)</span>
      <span class="text-emerald-400 font-bold text-sm mt-1">5¹ = 5</span>
    </div>
  </div>

  <div class="text-xs text-center font-mono text-emerald-300 bg-slate-900 p-2 rounded border border-slate-800">
    LCM unites the maximum prime exponents: 2³ × 3² × 5¹ = 8 × 9 × 5 = 360!
  </div>
</div>
"""

# 9. sim-algebraic-multiples-grid
SIMS["sim-algebraic-multiples-grid"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-blue-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-blue-300">🔢 Multiples Grid (1 to 50): Algebraic Filters</div>
    <span class="text-[11px] text-slate-400 font-mono">Observe Simultaneous Divisibility</span>
  </div>

  <!-- Filter buttons -->
  <div class="flex flex-wrap items-center gap-2 bg-slate-950/60 p-2 rounded-lg border border-slate-800 text-xs">
    <span class="text-slate-300 font-semibold">Active Filter:</span>
    <button class="px-2.5 py-1 rounded bg-sky-600/40 hover:bg-sky-600 text-sky-200 font-bold" onclick="filterMultiplesGrid(2)">2n (Evens)</button>
    <button class="px-2.5 py-1 rounded bg-emerald-600/40 hover:bg-emerald-600 text-emerald-200 font-bold" onclick="filterMultiplesGrid(3)">3n (Threes)</button>
    <button class="px-2.5 py-1 rounded bg-amber-600/40 hover:bg-amber-600 text-amber-200 font-bold" onclick="filterMultiplesGrid(5)">5n (Fives)</button>
    <button class="px-2.5 py-1 rounded bg-purple-600/40 hover:bg-purple-600 text-purple-200 font-bold" onclick="filterMultiplesGrid(6)">6n (LCM 2 & 3)</button>
  </div>

  <!-- Number Grid -->
  <div id="multiplesGrid50" class="grid grid-cols-10 gap-1 bg-slate-950/80 p-2.5 rounded-lg border border-slate-800 max-h-40 overflow-y-auto font-mono text-center text-[10px]">
    <!-- Cells 1 to 50 injected by JS -->
  </div>

  <div id="gridFilterDesc" class="text-xs font-mono text-center text-slate-300 bg-slate-900 p-1.5 rounded border border-slate-800">
    Showing multiples of 2n (all even numbers).
  </div>
</div>
"""

# 10. sim-nested-multiple-rule
SIMS["sim-nested-multiple-rule"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-amber-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-amber-300">📦 Multiple Rule: When One Number Divides the Other</div>
    <span class="text-xs font-mono font-bold text-amber-300" id="nestedRuleBanner">a | b ➔ HCF = a, LCM = b</span>
  </div>

  <!-- Preset Pairs -->
  <div class="flex items-center justify-between gap-2 bg-slate-950/60 p-2 rounded-lg border border-slate-800 text-xs">
    <span class="text-slate-300 font-semibold">Test Pair:</span>
    <button class="px-2.5 py-1 rounded bg-amber-600/40 hover:bg-amber-600 text-amber-200 font-bold" onclick="setNestedPair(6, 24)">6 & 24</button>
    <button class="px-2.5 py-1 rounded bg-amber-600/40 hover:bg-amber-600 text-amber-200 font-bold" onclick="setNestedPair(7, 35)">7 & 35</button>
    <button class="px-2.5 py-1 rounded bg-amber-600/40 hover:bg-amber-600 text-amber-200 font-bold" onclick="setNestedPair(8, 72)">8 & 72</button>
    <button class="px-2.5 py-1 rounded bg-sky-600/40 hover:bg-sky-600 text-sky-200 font-bold" onclick="setNestedPair(8, 9)">8 & 9 (Co-prime)</button>
  </div>

  <!-- Visual Container Display -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex items-center justify-around font-mono">
    <div class="p-3 rounded bg-amber-950/40 border border-amber-500/40 text-center min-w-[130px]">
      <div class="text-[10px] text-amber-300 uppercase tracking-wider font-bold">Highest Common Factor</div>
      <div class="text-xl font-bold text-amber-400 mt-1" id="nestedHcfVal">HCF = 6</div>
      <div class="text-[10px] text-slate-400 mt-0.5">(Smaller number)</div>
    </div>
    <div class="text-2xl font-bold text-slate-600">⚖️</div>
    <div class="p-3 rounded bg-emerald-950/40 border border-emerald-500/40 text-center min-w-[130px]">
      <div class="text-[10px] text-emerald-300 uppercase tracking-wider font-bold">Lowest Common Multiple</div>
      <div class="text-xl font-bold text-emerald-400 mt-1" id="nestedLcmVal">LCM = 24</div>
      <div class="text-[10px] text-slate-400 mt-0.5">(Larger number)</div>
    </div>
  </div>

  <div id="nestedSummaryText" class="text-xs font-mono text-center text-slate-300 bg-slate-900 p-2 rounded border border-slate-800">
    Since 24 is an exact multiple of 6 (6 × 4 = 24), HCF = 6 and LCM = 24 instantly!
  </div>
</div>
"""

# 11. sim-scaling-magnifier
SIMS["sim-scaling-magnifier"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-sky-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-sky-300">🔍 Scaling Magnifier: Multiplying Both Numbers by k</div>
    <div class="text-xs font-mono font-bold text-sky-300">Scale Factor: <span id="scaleKVal" class="text-amber-400">1</span>×</div>
  </div>

  <!-- Scale Slider -->
  <div class="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800 flex items-center gap-3 text-xs">
    <span class="text-slate-300 font-semibold">Scale Factor k:</span>
    <input id="scaleSliderK" type="range" min="1" max="10" value="1" class="flex-1 h-1.5 bg-slate-700 rounded accent-sky-400 cursor-pointer" oninput="updateScalingSim()">
    <span class="text-xs font-mono font-bold text-amber-300 w-8" id="scaleBadge">k=1</span>
  </div>

  <!-- Values Grid -->
  <div class="grid grid-cols-2 gap-3 bg-slate-950/80 p-3 rounded-lg border border-slate-800 font-mono text-xs">
    <div class="p-2 rounded bg-slate-900 border border-slate-700">
      <div class="text-slate-400 text-[10px]">Scaled Numbers:</div>
      <div class="text-sm font-bold text-sky-400 mt-1" id="scaleNumDisplay">6 and 8</div>
    </div>
    <div class="p-2 rounded bg-slate-900 border border-slate-700">
      <div class="text-slate-400 text-[10px]">HCF & LCM Results:</div>
      <div class="text-sm font-bold text-emerald-400 mt-1" id="scaleResultDisplay">HCF = 2, LCM = 24</div>
    </div>
  </div>

  <div id="scaleProofText" class="text-xs text-center font-mono text-slate-300 bg-slate-900 p-2 rounded border border-slate-800">
    At k=1: HCF(6, 8) = 2 and LCM(6, 8) = 24.
  </div>
</div>
"""

# 12. sim-simultaneous-ladder
SIMS["sim-simultaneous-ladder"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-emerald-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-emerald-300">🪜 Simultaneous Division Ladder / Cake Method</div>
    <button class="px-2.5 py-1 rounded bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold" onclick="stepLadderDivision()">
      ▶ Next Division Step
    </button>
  </div>

  <div class="flex items-center justify-between gap-3 bg-slate-950/60 p-2 rounded-lg border border-slate-800 text-xs">
    <span class="text-slate-300">Numbers:</span>
    <button class="px-2 py-0.5 rounded bg-emerald-600/40 text-emerald-200 font-bold" onclick="resetLadder(24, 36)">24 & 36</button>
    <button class="px-2 py-0.5 rounded bg-emerald-600/40 text-emerald-200 font-bold" onclick="resetLadder(20, 28)">20 & 28</button>
    <button class="px-2 py-0.5 rounded bg-emerald-600/40 text-emerald-200 font-bold" onclick="resetLadder(30, 45)">30 & 45</button>
  </div>

  <!-- Ladder Visualization -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 min-h-[140px] flex flex-col items-center justify-center font-mono text-xs">
    <div id="ladderRowsContainer" class="flex flex-col gap-1 w-full max-w-xs">
      <!-- Injected ladder steps -->
    </div>
  </div>

  <div id="ladderSummary" class="text-xs font-mono text-slate-300 bg-slate-900 p-2 rounded border border-slate-800 flex justify-between">
    <span>Left Column (HCF): <strong id="ladderHcfText" class="text-amber-400">...</strong></span>
    <span>L-Shape (LCM): <strong id="ladderLcmText" class="text-emerald-400">...</strong></span>
  </div>
</div>
"""

# 13. sim-shortcut-factor-extractor
SIMS["sim-shortcut-factor-extractor"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-purple-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-purple-300">⚡ Large Common Factor Slasher Shortcut</div>
    <span class="text-xs font-mono text-amber-300">Fast Mental Math</span>
  </div>

  <div class="flex items-center justify-between gap-2 bg-slate-950/60 p-2 rounded-lg border border-slate-800 text-xs">
    <span class="text-slate-300">Problem:</span>
    <button class="px-2.5 py-1 rounded bg-purple-600/40 hover:bg-purple-600 text-purple-200 font-bold" onclick="setShortcutProblem(120, 180, 60)">120 & 180 (Slash 60)</button>
    <button class="px-2.5 py-1 rounded bg-purple-600/40 hover:bg-purple-600 text-purple-200 font-bold" onclick="setShortcutProblem(300, 450, 150)">300 & 450 (Slash 150)</button>
    <button class="px-2.5 py-1 rounded bg-purple-600/40 hover:bg-purple-600 text-purple-200 font-bold" onclick="setShortcutProblem(80, 120, 40)">80 & 120 (Slash 40)</button>
  </div>

  <!-- Visual Slasher Breakdown -->
  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2 font-mono text-xs">
    <div class="flex items-center justify-around text-center">
      <div class="p-2 rounded bg-slate-900 border border-slate-700 min-w-[130px]">
        <div class="text-[10px] text-slate-400">Original Numbers</div>
        <div id="scOrigNums" class="text-sm font-bold text-sky-400 mt-1">120 and 180</div>
      </div>
      <div class="text-lg font-bold text-purple-400">➔ Slash Factor ➔</div>
      <div class="p-2 rounded bg-purple-950/40 border border-purple-500/40 min-w-[130px]">
        <div class="text-[10px] text-purple-300">Extracted GCD</div>
        <div id="scExtractedFactor" class="text-sm font-bold text-purple-300 mt-1">60 × (2 & 3)</div>
      </div>
    </div>

    <div id="scStepsExplanation" class="p-2.5 rounded bg-slate-900 text-slate-300 leading-relaxed border border-slate-800">
      1. Divide out 60: 120 / 60 = 2, and 180 / 60 = 3.<br>
      2. 2 and 3 are co-prime (HCF = 1, LCM = 6).<br>
      3. Total HCF = 60 × 1 = 60; Total LCM = 60 × 6 = 360!
    </div>
  </div>
</div>
"""

# 14. sim-master-product-balance
SIMS["sim-master-product-balance"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-amber-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-amber-300">⚖️ Master Formula Balance: HCF × LCM = a × b</div>
    <span class="text-xs font-mono font-bold text-emerald-400" id="balanceMatchText">Balanced!</span>
  </div>

  <!-- Sliders for a and b -->
  <div class="grid grid-cols-2 gap-3 bg-slate-950/60 p-2.5 rounded-lg border border-slate-800 text-xs">
    <div>
      <label class="text-slate-300 flex justify-between"><span>Number a:</span> <span id="masterNumA" class="font-bold text-sky-400">18</span></label>
      <input id="masterSliderA" type="range" min="6" max="48" step="2" value="18" class="w-full h-1.5 bg-slate-700 rounded accent-sky-400 cursor-pointer" oninput="updateMasterBalance()">
    </div>
    <div>
      <label class="text-slate-300 flex justify-between"><span>Number b:</span> <span id="masterNumB" class="font-bold text-emerald-400">24</span></label>
      <input id="masterSliderB" type="range" min="6" max="48" step="2" value="24" class="w-full h-1.5 bg-slate-700 rounded accent-emerald-400 cursor-pointer" oninput="updateMasterBalance()">
    </div>
  </div>

  <!-- Two-Pan Balance SVG -->
  <div class="bg-slate-950/80 p-2.5 rounded-lg border border-slate-800 flex flex-col items-center font-mono">
    <div class="flex items-center justify-around w-full text-center">
      <div class="p-2.5 rounded bg-sky-950/40 border border-sky-500/40 min-w-[130px]">
        <div class="text-[10px] text-sky-300 font-bold uppercase">Left Pan (a × b)</div>
        <div id="leftPanProductExpr" class="text-xs text-slate-300 mt-1">18 × 24</div>
        <div id="leftPanProductVal" class="text-lg font-extrabold text-sky-400 mt-0.5">432</div>
      </div>
      <div class="text-2xl font-bold text-amber-400">=</div>
      <div class="p-2.5 rounded bg-emerald-950/40 border border-emerald-500/40 min-w-[130px]">
        <div class="text-[10px] text-emerald-300 font-bold uppercase">Right Pan (HCF × LCM)</div>
        <div id="rightPanHcfLcmExpr" class="text-xs text-slate-300 mt-1">6 × 72</div>
        <div id="rightPanHcfLcmVal" class="text-lg font-extrabold text-emerald-400 mt-0.5">432</div>
      </div>
    </div>
    <div id="masterIdentityProof" class="text-xs text-center text-emerald-300 mt-2">
      ✓ Universal Equality: HCF(18, 24) = 6, LCM(18, 24) = 72. 6 × 72 = 432 = 18 × 24!
    </div>
  </div>
</div>
"""

# 15. sim-three-number-engine
SIMS["sim-three-number-engine"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-rose-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-rose-300">⚠️ The 3-Number Formula Trap Lab</div>
    <span class="text-xs font-mono font-bold text-rose-400">HCF × LCM ≠ a × b × c</span>
  </div>

  <div class="flex items-center justify-between gap-2 bg-slate-950/60 p-2 rounded-lg border border-slate-800 text-xs">
    <span class="text-slate-300">Choose 3 Numbers:</span>
    <button class="px-2.5 py-1 rounded bg-rose-600/40 hover:bg-rose-600 text-rose-200 font-bold" onclick="setThreeNums(4, 6, 8)">4, 6, 8</button>
    <button class="px-2.5 py-1 rounded bg-rose-600/40 hover:bg-rose-600 text-rose-200 font-bold" onclick="setThreeNums(6, 8, 12)">6, 8, 12</button>
    <button class="px-2.5 py-1 rounded bg-rose-600/40 hover:bg-rose-600 text-rose-200 font-bold" onclick="setThreeNums(10, 15, 20)">10, 15, 20</button>
  </div>

  <div class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2 font-mono text-xs">
    <div class="flex items-center justify-around text-center">
      <div class="p-2.5 rounded bg-slate-900 border border-slate-700 min-w-[130px]">
        <div class="text-[10px] text-slate-400">HCF × LCM</div>
        <div id="threeNumsHcfLcm" class="text-base font-bold text-amber-400 mt-1">2 × 24 = 48</div>
      </div>
      <div class="text-2xl font-bold text-rose-500">≠</div>
      <div class="p-2.5 rounded bg-slate-900 border border-slate-700 min-w-[130px]">
        <div class="text-[10px] text-slate-400">Product (a × b × c)</div>
        <div id="threeNumsProduct" class="text-base font-bold text-rose-400 mt-1">4 × 6 × 8 = 192</div>
      </div>
    </div>
    <div id="threeNumsTrapReason" class="text-xs text-rose-300 text-center p-2 rounded bg-rose-950/40 border border-rose-500/30">
      48 ≠ 192! Pairwise common prime factors duplicate inside the product a × b × c!
    </div>
  </div>
</div>
"""

# 16. sim-heritage-kuttaka
SIMS["sim-heritage-kuttaka"] = r"""
<div class="sim-wrapper flex flex-col gap-3 p-3 bg-slate-900/80 rounded-xl border border-amber-500/30">
  <div class="flex items-center justify-between">
    <div class="text-xs font-bold text-amber-300">📜 Heritage: Āryabhaṭa's Kuṭṭaka & Mahāvīra's Niruddha</div>
    <span class="text-[10px] text-amber-400 font-serif italic">499 CE & 850 CE</span>
  </div>

  <div class="flex gap-2 bg-slate-950/60 p-2 rounded-lg border border-slate-800 text-xs">
    <button class="flex-1 py-1 rounded bg-amber-600/40 hover:bg-amber-600 text-amber-200 font-bold" onclick="setHeritageTab('kuttaka')">
      Āryabhaṭa's Kuṭṭaka (Pulverizer GCD)
    </button>
    <button class="flex-1 py-1 rounded bg-emerald-600/40 hover:bg-emerald-600 text-emerald-200 font-bold" onclick="setHeritageTab('niruddha')">
      Mahāvīra's Niruddha (LCM Fractions)
    </button>
  </div>

  <div id="heritageContentBox" class="bg-slate-950/80 p-3 rounded-lg border border-slate-800 flex flex-col gap-2 font-mono text-xs">
    <!-- Heritage details rendered by JS -->
  </div>
</div>
"""

code = f'''# -*- coding: utf-8 -*-
"""
Class 7 Mathematics - Chapter 11: Finding Common Ground (HCF & LCM) Simulators
Contains 16 bespoke SVG simulator templates.
"""

SIMULATORS = {repr(SIMS)}
'''

with open('.agents/class7_math_finding_common_ground_sims.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Generated .agents/class7_math_finding_common_ground_sims.py successfully!")

