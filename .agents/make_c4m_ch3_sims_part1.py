# -*- coding: utf-8 -*-
"""
Interactive SVG/HTML Simulators 1 to 8 for Class 4 Maths Chapter 3: Patterns Around Us
"""

def get_sims_part1():
    return {
        1: """
<div class="flex flex-col h-full bg-emerald-950/20 rounded-xl p-3 border border-emerald-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Interactive Orchard Grid</span>
      <span class="text-xs text-slate-400">Rows × Columns Array Multiplier</span>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="changeOrchardGrid(-1, 0)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded border border-slate-700 font-bold">- Row</button>
      <button onclick="changeOrchardGrid(1, 0)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded border border-slate-700 font-bold">+ Row</button>
      <button onclick="changeOrchardGrid(0, -1)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded border border-slate-700 font-bold">- Col</button>
      <button onclick="changeOrchardGrid(0, 1)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded border border-slate-700 font-bold">+ Col</button>
      <button onclick="harvestCoconuts()" id="harvestBtn" class="px-3 py-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs rounded shadow transition-all flex items-center gap-1">
        <span>🥥 Harvest 5 Each</span>
      </button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex flex-col items-center justify-center overflow-hidden">
    <div id="orchardGridSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 grid grid-cols-3 gap-2 text-center text-xs">
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Grid Dimensions</span>
      <span id="orchardDimDisplay" class="font-bold text-emerald-400 text-sm">4 Rows × 6 Columns</span>
    </div>
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Total Trees (Rows × Cols)</span>
      <span id="orchardTreeTotal" class="font-bold text-cyan-400 text-sm">24 Trees</span>
    </div>
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Harvest (Trees × 5 🥥)</span>
      <span id="orchardHarvestTotal" class="font-bold text-amber-400 text-sm">120 Coconuts</span>
    </div>
  </div>
</div>
""",
        2: """
<div class="flex flex-col h-full bg-amber-950/20 rounded-xl p-3 border border-amber-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">Pottery Workshop</span>
      <span class="text-xs text-slate-400">Vertical Cup & Plate Columns</span>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="setPotteryType('cups')" id="potteryCupsBtn" class="px-2.5 py-1 bg-amber-500 text-slate-950 font-bold text-xs rounded transition-all">Cups (Chai)</button>
      <button onclick="setPotteryType('plates')" id="potteryPlatesBtn" class="px-2.5 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded transition-all">Plates</button>
      <button onclick="changePotteryStacks(-1)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded border border-slate-700 font-bold">- Stack</button>
      <button onclick="changePotteryStacks(1)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded border border-slate-700 font-bold">+ Stack</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="potterySvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 grid grid-cols-3 gap-2 text-center text-xs">
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Stack Columns</span>
      <span id="potteryStacksDisplay" class="font-bold text-amber-300 text-sm">5 Stacks</span>
    </div>
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Items Per Stack</span>
      <span id="potteryPerStackDisplay" class="font-bold text-cyan-300 text-sm">6 Cups Each</span>
    </div>
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Total Pottery Count</span>
      <span id="potteryTotalDisplay" class="font-bold text-emerald-400 text-sm">5 × 6 = 30 Cups</span>
    </div>
  </div>
</div>
""",
        3: """
<div class="flex flex-col h-full bg-orange-950/20 rounded-xl p-3 border border-orange-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-orange-500/20 text-orange-300 border border-orange-500/30">Festive Sweet Trays</span>
      <span class="text-xs text-slate-400">Laddoo & Peda Symmetrical Layout</span>
    </div>
    <div class="flex items-center gap-2">
      <span class="text-xs text-slate-300">Tray Tiers:</span>
      <button onclick="changeSweetTiers(1)" class="w-7 h-7 bg-orange-500 hover:bg-orange-400 text-slate-950 font-bold rounded text-xs">1</button>
      <button onclick="changeSweetTiers(2)" class="w-7 h-7 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold rounded text-xs">2</button>
      <button onclick="changeSweetTiers(3)" class="w-7 h-7 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold rounded text-xs">3</button>
      <button onclick="changeSweetTiers(4)" class="w-7 h-7 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold rounded text-xs">4</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="sweetTraysSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 grid grid-cols-3 gap-2 text-center text-xs">
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Coconut Laddoos</span>
      <span id="sweetLaddoosDisplay" class="font-bold text-amber-300 text-sm">9 per tray (Total: 9)</span>
    </div>
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Milk Pedas</span>
      <span id="sweetPedasDisplay" class="font-bold text-yellow-200 text-sm">16 per tray (Total: 16)</span>
    </div>
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Combined Sweets</span>
      <span id="sweetTotalDisplay" class="font-bold text-emerald-400 text-sm">25 Sweets (1 Tray)</span>
    </div>
  </div>
</div>
""",
        4: """
<div class="flex flex-col h-full bg-cyan-950/20 rounded-xl p-3 border border-cyan-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Banknote & Coin Mandala</span>
      <span class="text-xs text-slate-400">Symmetrical Money Geometry</span>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="toggleMoneyRing('notes')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-xs font-bold text-amber-300 rounded border border-slate-700">₹10 Notes</button>
      <button onclick="toggleMoneyRing('five')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-xs font-bold text-yellow-400 rounded border border-slate-700">₹5 Coins</button>
      <button onclick="toggleMoneyRing('two')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-300 rounded border border-slate-700">₹2 Coins</button>
      <button onclick="toggleMoneyRing('one')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-xs font-bold text-emerald-400 rounded border border-slate-700">₹1 Coins</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="moneyMandalaSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 grid grid-cols-4 gap-1.5 text-center text-xs">
    <div class="bg-slate-900/90 p-1 rounded border border-slate-800">
      <span class="text-slate-400 block text-[9px]">4 × ₹10 Notes</span>
      <span id="mandalaNotesVal" class="font-bold text-amber-300">₹40</span>
    </div>
    <div class="bg-slate-900/90 p-1 rounded border border-slate-800">
      <span class="text-slate-400 block text-[9px]">4 × ₹5 Coins</span>
      <span id="mandalaFiveVal" class="font-bold text-yellow-300">₹20</span>
    </div>
    <div class="bg-slate-900/90 p-1 rounded border border-slate-800">
      <span class="text-slate-400 block text-[9px]">8 × ₹2 Coins</span>
      <span id="mandalaTwoVal" class="font-bold text-slate-300">₹16</span>
    </div>
    <div class="bg-slate-900/90 p-1 rounded border border-slate-800">
      <span class="text-slate-400 block text-[9px]">8 × ₹1 Coins</span>
      <span id="mandalaOneVal" class="font-bold text-emerald-300">₹8</span>
    </div>
  </div>
  <div class="mt-1 text-center bg-cyan-950/40 p-1 rounded border border-cyan-500/30 text-xs">
    <span class="text-slate-300">Grand Total: </span>
    <span id="mandalaGrandTotal" class="font-bold text-cyan-300 text-sm">₹40 + ₹20 + ₹16 + ₹8 = ₹84</span>
  </div>
</div>
""",
        5: """
<div class="flex flex-col h-full bg-violet-950/20 rounded-xl p-3 border border-violet-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-violet-500/20 text-violet-300 border border-violet-500/30">Target Amount Builder</span>
      <span class="text-xs text-slate-400">Combine Denominations</span>
    </div>
    <div class="flex items-center gap-1.5">
      <span class="text-xs text-slate-300">Presets:</span>
      <button onclick="setTargetAmount(36)" class="px-2 py-0.5 bg-violet-600 hover:bg-violet-500 text-white font-bold text-xs rounded">₹36</button>
      <button onclick="setTargetAmount(125)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs rounded border border-slate-700">₹125</button>
      <button onclick="setTargetAmount(183)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs rounded border border-slate-700">₹183</button>
      <button onclick="clearTargetWallet()" class="px-2 py-0.5 bg-rose-900/60 hover:bg-rose-800 text-rose-200 text-xs rounded">Reset</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 flex flex-col justify-between">
    <div class="grid grid-cols-7 gap-1 text-center">
      <button onclick="addWalletItem(100)" class="p-1.5 bg-purple-900/50 hover:bg-purple-800 border border-purple-500/40 rounded text-purple-200 font-bold text-xs">+ ₹100</button>
      <button onclick="addWalletItem(50)" class="p-1.5 bg-cyan-900/50 hover:bg-cyan-800 border border-cyan-500/40 rounded text-cyan-200 font-bold text-xs">+ ₹50</button>
      <button onclick="addWalletItem(20)" class="p-1.5 bg-amber-900/50 hover:bg-amber-800 border border-amber-500/40 rounded text-amber-200 font-bold text-xs">+ ₹20</button>
      <button onclick="addWalletItem(10)" class="p-1.5 bg-orange-900/50 hover:bg-orange-800 border border-orange-500/40 rounded text-orange-200 font-bold text-xs">+ ₹10</button>
      <button onclick="addWalletItem(5)" class="p-1.5 bg-yellow-900/50 hover:bg-yellow-800 border border-yellow-500/40 rounded text-yellow-200 font-bold text-xs">+ ₹5</button>
      <button onclick="addWalletItem(2)" class="p-1.5 bg-slate-800 hover:bg-slate-700 border border-slate-600 rounded text-slate-200 font-bold text-xs">+ ₹2</button>
      <button onclick="addWalletItem(1)" class="p-1.5 bg-emerald-900/50 hover:bg-emerald-800 border border-emerald-500/40 rounded text-emerald-200 font-bold text-xs">+ ₹1</button>
    </div>
    <div id="walletItemsContainer" class="flex-1 my-2 bg-slate-900/70 rounded p-2 border border-slate-800 flex flex-wrap gap-1.5 items-center content-center justify-center overflow-auto">
      <span class="text-xs text-slate-500 italic">Click denomination buttons above to build the target amount.</span>
    </div>
    <div class="grid grid-cols-3 gap-2 text-center text-xs">
      <div class="bg-slate-900 p-1.5 rounded border border-slate-800">
        <span class="text-slate-400 block text-[10px]">Target Amount</span>
        <span id="targetAmountDisplay" class="font-bold text-violet-400 text-sm">₹36</span>
      </div>
      <div class="bg-slate-900 p-1.5 rounded border border-slate-800">
        <span class="text-slate-400 block text-[10px]">Your Wallet Sum</span>
        <span id="walletSumDisplay" class="font-bold text-cyan-400 text-sm">₹0</span>
      </div>
      <div class="bg-slate-900 p-1.5 rounded border border-slate-800">
        <span class="text-slate-400 block text-[10px]">Status</span>
        <span id="walletStatusDisplay" class="font-bold text-amber-400 text-xs">Needs ₹36 more</span>
      </div>
    </div>
  </div>
</div>
""",
        6: """
<div class="flex flex-col h-full bg-blue-950/20 rounded-xl p-3 border border-blue-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/30">Quantity Distributions</span>
      <span class="text-xs text-slate-400">Two Geometric Perspectives</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="setDistributionMode('2x6')" id="dist2x6Btn" class="px-2 py-1 bg-blue-500 text-slate-950 font-bold text-xs rounded transition-all">2 Rows × 6</button>
      <button onclick="setDistributionMode('3x4')" id="dist3x4Btn" class="px-2 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded transition-all border border-slate-700">3 Rows × 4</button>
      <button onclick="setDistributionMode('pairs')" id="distPairsBtn" class="px-2 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded transition-all border border-slate-700">6 Pairs (2s)</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="distributionSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="distributionExplanation" class="text-blue-300 font-medium">12 Coins arranged into 2 rows of 6 coins. Each coin in the top row has a matching partner below (Splits into 2 equal halves of 6).</span>
  </div>
</div>
""",
        7: """
<div class="flex flex-col h-full bg-teal-950/20 rounded-xl p-3 border border-teal-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-teal-500/20 text-teal-300 border border-teal-500/30">The Concept of Pairs</span>
      <span class="text-xs text-slate-400">Pairing Items Two by Two</span>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="changePairCount(-1)" class="w-6 h-6 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold rounded text-xs">-</button>
      <span id="pairItemCountDisplay" class="font-bold text-teal-300 text-xs">10 Items</span>
      <button onclick="changePairCount(1)" class="w-6 h-6 bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold rounded text-xs">+</button>
      <button onclick="animatePairingAction()" class="px-3 py-1 bg-teal-500 hover:bg-teal-400 text-slate-950 font-bold text-xs rounded shadow">Group into Pairs!</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="pairingLabSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 grid grid-cols-3 gap-2 text-center text-xs">
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Complete Pairs</span>
      <span id="pairsCountDisplay" class="font-bold text-teal-300 text-sm">5 Pairs (10 Items)</span>
    </div>
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Leftover Items</span>
      <span id="leftoverCountDisplay" class="font-bold text-amber-300 text-sm">0 Leftover</span>
    </div>
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Parity Family</span>
      <span id="parityFamilyDisplay" class="font-bold text-emerald-400 text-sm">EVEN NUMBER</span>
    </div>
  </div>
</div>
""",
        8: """
<div class="flex flex-col h-full bg-emerald-950/20 rounded-xl p-3 border border-emerald-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Even Number Pairing</span>
      <span class="text-xs text-slate-400">Complete Pairing & Zero Remainder</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="setEvenNumber(6)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">6</button>
      <button onclick="setEvenNumber(8)" class="px-2 py-0.5 bg-emerald-500 text-slate-950 font-bold text-xs rounded">8</button>
      <button onclick="setEvenNumber(12)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">12</button>
      <button onclick="setEvenNumber(16)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">16</button>
      <button onclick="toggleEvenSplit()" id="splitEvenBtn" class="px-2 py-0.5 bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs rounded">Split in Half</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="evenPairingSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="evenAnalysisText" class="text-emerald-300 font-medium">8 marbles form 4 complete pairs. Both parallel rows have equal length (4 and 4). Remainder = 0. Therefore, 8 is an EVEN number.</span>
  </div>
</div>
"""
    }

if __name__ == '__main__':
    sims = get_sims_part1()
    print(f"Generated {len(sims)} simulators for part 1.")
