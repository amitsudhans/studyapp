# -*- coding: utf-8 -*-
"""
Interactive SVG/HTML Simulators 9 to 16 for Class 4 Maths Chapter 3: Patterns Around Us
"""

def get_sims_part2():
    return {
        9: """
<div class="flex flex-col h-full bg-rose-950/20 rounded-xl p-3 border border-rose-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/30">Odd Number Remainder</span>
      <span class="text-xs text-slate-400">The Signature Leftover of 1</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="setOddNumber(5)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">5</button>
      <button onclick="setOddNumber(7)" class="px-2 py-0.5 bg-rose-500 text-slate-950 font-bold text-xs rounded">7</button>
      <button onclick="setOddNumber(9)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">9</button>
      <button onclick="setOddNumber(13)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">13</button>
      <button onclick="highlightOddRemainder()" class="px-2.5 py-0.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs rounded">Highlight Remainder</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="oddPairingSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="oddAnalysisText" class="text-rose-300 font-medium">7 items form 3 complete pairs (6 items), leaving exactly 1 lonely remainder item! (7 = 2 × 3 + 1). Therefore, 7 is an ODD number.</span>
  </div>
</div>
""",
        10: """
<div class="flex flex-col h-full bg-indigo-950/20 rounded-xl p-3 border border-indigo-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Numbers 1 to 20</span>
      <span class="text-xs text-slate-400">Rhythmic Parity Alternation</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="filterNumbersMode('all')" id="filterAllBtn" class="px-2 py-0.5 bg-indigo-600 text-white font-bold text-xs rounded">All (1-20)</button>
      <button onclick="filterNumbersMode('evens')" id="filterEvensBtn" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">2× Table (Evens)</button>
      <button onclick="filterNumbersMode('odds')" id="filterOddsBtn" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">Odds (Remainders)</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 flex flex-col justify-center overflow-hidden">
    <div id="numbers1to20Grid" class="grid grid-cols-10 gap-1.5 p-2"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="numbers20Summary" class="text-indigo-300 font-medium">Every multiple of 2 (2, 4, 6, 8, 10, 12, 14, 16, 18, 20) is an EVEN number. Even and odd numbers alternate strictly!</span>
  </div>
</div>
""",
        11: """
<div class="flex flex-col h-full bg-purple-950/20 rounded-xl p-3 border border-purple-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-purple-500/20 text-purple-300 border border-purple-500/30">Crayon Number Grid (1–50)</span>
      <span class="text-xs text-slate-400">Vertical Parity Stripes</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="toggleCrayonMarks('odds')" id="crayonCircleOddsBtn" class="px-2 py-0.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs rounded">⭕ Circle Odds</button>
      <button onclick="toggleCrayonMarks('evens')" id="crayonSquareEvensBtn" class="px-2 py-0.5 bg-blue-500 hover:bg-blue-400 text-slate-950 font-bold text-xs rounded">⏹️ Box Evens</button>
      <button onclick="resetCrayonGrid()" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">Reset</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 overflow-auto flex flex-col justify-center">
    <div id="crayonGridContainer" class="grid grid-cols-10 gap-1 text-center font-mono"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="crayonGridNote" class="text-purple-300 font-medium">Observe columns: columns ending in 1, 3, 5, 7, 9 are all ODD. Columns ending in 2, 4, 6, 8, 0 are all EVEN!</span>
  </div>
</div>
""",
        12: """
<div class="flex flex-col h-full bg-amber-950/20 rounded-xl p-3 border border-amber-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">Open Book Page Parity</span>
      <span class="text-xs text-slate-400">Left Page Even • Right Page Odd</span>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="turnBookPage(-1)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded border border-slate-700 font-bold">◀ Previous Spread</button>
      <button onclick="turnBookPage(1)" class="px-2.5 py-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs rounded shadow">Next Spread ▶</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-3 border border-slate-800 flex items-center justify-center">
    <div class="w-full max-w-md bg-amber-100 dark:bg-stone-900 rounded-lg shadow-2xl border-4 border-amber-900/40 p-4 flex gap-4 relative">
      <div class="absolute inset-y-0 left-1/2 w-1 bg-stone-700/40 -translate-x-1/2"></div>
      <div class="flex-1 flex flex-col justify-between items-center bg-stone-100 dark:bg-stone-800/90 p-3 rounded shadow-inner text-center">
        <span class="text-[10px] font-bold text-cyan-600 dark:text-cyan-400 uppercase tracking-widest">Left Page (Even)</span>
        <div class="my-4">
          <span id="bookLeftPageNum" class="text-4xl font-black text-slate-800 dark:text-slate-100 font-mono">42</span>
          <span class="block text-xs font-bold text-emerald-600 dark:text-emerald-400 mt-1">EVEN NUMBER</span>
        </div>
        <span class="text-[9px] text-slate-500">Divisible by 2 with 0 remainder</span>
      </div>
      <div class="flex-1 flex flex-col justify-between items-center bg-stone-100 dark:bg-stone-800/90 p-3 rounded shadow-inner text-center">
        <span class="text-[10px] font-bold text-amber-600 dark:text-amber-400 uppercase tracking-widest">Right Page (Odd)</span>
        <div class="my-4">
          <span id="bookRightPageNum" class="text-4xl font-black text-slate-800 dark:text-slate-100 font-mono">43</span>
          <span class="block text-xs font-bold text-amber-600 dark:text-amber-400 mt-1">ODD NUMBER</span>
        </div>
        <span class="text-[9px] text-slate-500">Leaves remainder of 1</span>
      </div>
    </div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span class="text-slate-400">Spread Sum: </span>
    <span id="bookSpreadSumText" class="font-bold text-amber-300">Page 42 (Even) + Page 43 (Odd) = 85 (Always ODD!)</span>
  </div>
</div>
""",
        13: """
<div class="flex flex-col h-full bg-cyan-950/20 rounded-xl p-3 border border-cyan-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Multi-Digit Parity Rule</span>
      <span class="text-xs text-slate-400">Only the Ones Digit Matters!</span>
    </div>
    <div class="flex items-center gap-1.5">
      <span class="text-xs text-slate-300">Test:</span>
      <button onclick="scanMultiDigit(30)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">30</button>
      <button onclick="scanMultiDigit(46)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">46</button>
      <button onclick="scanMultiDigit(67)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">67</button>
      <button onclick="scanMultiDigit(154)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">154</button>
      <button onclick="scanMultiDigit(415)" class="px-2 py-0.5 bg-cyan-600 text-white font-bold text-xs rounded">415</button>
      <button onclick="scanMultiDigit(300)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">300</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-3 border border-slate-800 flex flex-col items-center justify-center">
    <div id="digitBreakdownDisplay" class="flex items-center gap-3"></div>
    <div class="mt-4 flex items-center gap-2">
      <span class="text-xs text-slate-400">Tens & Hundreds (Multiples of 10):</span>
      <span class="text-xs font-bold text-emerald-400 px-2 py-0.5 bg-emerald-950/50 rounded border border-emerald-500/30">Always Even Pairs</span>
    </div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="multiDigitExplanation" class="text-cyan-300 font-medium">In 415, the ones digit is 5. Since 5 is an odd digit, the entire number 415 is ODD!</span>
  </div>
</div>
""",
        14: """
<div class="flex flex-col h-full bg-fuchsia-950/20 rounded-xl p-3 border border-fuchsia-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-fuchsia-500/20 text-fuchsia-300 border border-fuchsia-500/30">Digit Permutation Parity</span>
      <span class="text-xs text-slate-400">Swapping Positions Alters Parity</span>
    </div>
    <div class="flex items-center gap-1.5">
      <span class="text-xs text-slate-300">Pairs:</span>
      <button onclick="loadPermutationPair(1, 6)" class="px-2 py-0.5 bg-fuchsia-600 text-white font-bold text-xs rounded">1 & 6</button>
      <button onclick="loadPermutationPair(2, 7)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">2 & 7</button>
      <button onclick="loadPermutationPair(3, 8)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">3 & 8</button>
      <button onclick="loadPermutationPair(4, 5)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">4 & 5</button>
      <button onclick="swapDigitCards()" class="px-3 py-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs rounded shadow ml-2">🔀 Swap Digits</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-3 border border-slate-800 flex items-center justify-center">
    <div class="flex items-center gap-6">
      <div id="tensCardWrap" class="flex flex-col items-center">
        <span class="text-[10px] text-slate-400 uppercase tracking-widest mb-1">Tens Place</span>
        <div id="tensCard" class="w-16 h-20 bg-slate-800 border-2 border-slate-600 rounded-lg flex items-center justify-center text-3xl font-black text-slate-200 font-mono shadow-lg transition-transform">1</div>
      </div>
      <div id="onesCardWrap" class="flex flex-col items-center">
        <span class="text-[10px] text-fuchsia-400 font-bold uppercase tracking-widest mb-1">Ones Place (Decides!)</span>
        <div id="onesCard" class="w-16 h-20 bg-fuchsia-950/80 border-2 border-fuchsia-500 rounded-lg flex items-center justify-center text-3xl font-black text-fuchsia-300 font-mono shadow-lg ring-4 ring-fuchsia-500/20 transition-transform">6</div>
      </div>
    </div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="permutationAnalysisText" class="text-fuchsia-300 font-medium">Assembled Number: 16. Ones digit is 6 (Even) -> 16 is an EVEN number.</span>
  </div>
</div>
""",
        15: """
<div class="flex flex-col h-full bg-emerald-950/20 rounded-xl p-3 border border-emerald-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Consecutive Alternation</span>
      <span class="text-xs text-slate-400">Strict Neighbor Relationships</span>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="shiftConsecutiveWindow(-5)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded border border-slate-700 font-bold">◀ Slide Left</button>
      <button onclick="shiftConsecutiveWindow(5)" class="px-2 py-1 bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs rounded font-bold shadow">Slide Right ▶</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 flex flex-col justify-center overflow-hidden">
    <div id="consecutiveStripContainer" class="flex items-center justify-center gap-2"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="consecutiveNeighborText" class="text-emerald-300 font-medium">Every odd number is cushioned between two even neighbors. Every even number is cushioned between two odd neighbors!</span>
  </div>
</div>
""",
        16: """
<div class="flex flex-col h-full bg-teal-950/20 rounded-xl p-3 border border-teal-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-teal-500/20 text-teal-300 border border-teal-500/30">Range Parity Balance</span>
      <span class="text-xs text-slate-400">1 to 100 Balanced Scale</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="setBalanceRange(20)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">1–20</button>
      <button onclick="setBalanceRange(50)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">1–50</button>
      <button onclick="setBalanceRange(100)" class="px-2 py-0.5 bg-teal-500 text-slate-950 font-bold text-xs rounded shadow">1–100</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="balanceScaleSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 grid grid-cols-3 gap-1.5 text-center text-xs">
    <div class="bg-slate-900/90 p-1 rounded border border-slate-800">
      <span class="text-slate-400 block text-[9px]">Even + Even</span>
      <span class="font-bold text-emerald-400 text-xs">Always EVEN</span>
    </div>
    <div class="bg-slate-900/90 p-1 rounded border border-slate-800">
      <span class="text-slate-400 block text-[9px]">Odd + Odd</span>
      <span class="font-bold text-cyan-400 text-xs">Always EVEN (1+1=2)</span>
    </div>
    <div class="bg-slate-900/90 p-1 rounded border border-slate-800">
      <span class="text-slate-400 block text-[9px]">Even + Odd</span>
      <span class="font-bold text-amber-400 text-xs">Always ODD</span>
    </div>
  </div>
</div>
"""
    }

if __name__ == '__main__':
    sims = get_sims_part2()
    print(f"Generated {len(sims)} simulators for part 2.")
