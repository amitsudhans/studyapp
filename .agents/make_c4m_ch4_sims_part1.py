# -*- coding: utf-8 -*-
"""
Interactive SVG/HTML Simulators 1 to 8 for Class 4 Maths Chapter 4: Thousands Around Us
"""

def get_sims_part1():
    return {
        1: """
<div class="flex flex-col h-full bg-amber-950/20 rounded-xl p-3 border border-amber-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">Pantry Donation Inventory</span>
      <span class="text-xs text-slate-400">Place Values & Expanded Expressions</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="selectPantryItem('rice')" id="pantryRiceBtn" class="px-2 py-1 bg-amber-500 text-slate-950 font-bold text-xs rounded transition-all">Rice (68 kg)</button>
      <button onclick="selectPantryItem('flour')" id="pantryFlourBtn" class="px-2 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded transition-all border border-slate-700">Flour (45 kg)</button>
      <button onclick="selectPantryItem('oil')" id="pantryOilBtn" class="px-2 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded transition-all border border-slate-700">Oil (32 L)</button>
      <button onclick="selectPantryItem('veggies')" id="pantryVegBtn" class="px-2 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded transition-all border border-slate-700">Veg (240 kg)</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="pantrySvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 grid grid-cols-3 gap-2 text-center text-xs">
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Standard Value</span>
      <span id="pantryItemDisplay" class="font-bold text-amber-300 text-sm">68 kg (Rice)</span>
    </div>
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Place Value Breakdown</span>
      <span id="pantryPlaceBreakdown" class="font-bold text-cyan-300 text-sm">6 Tens + 8 Ones</span>
    </div>
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Expanded Form</span>
      <span id="pantryExpandedDisplay" class="font-bold text-emerald-400 text-sm">60 + 8</span>
    </div>
  </div>
</div>
""",
        2: """
<div class="flex flex-col h-full bg-blue-950/20 rounded-xl p-3 border border-blue-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/30">Dining Attendance Tracker</span>
      <span class="text-xs text-slate-400">Hundreds, Tens & Ones Blocks</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="setAttendanceSlot(1)" id="slot1Btn" class="px-2 py-1 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700 font-bold">11:00 (52)</button>
      <button onclick="setAttendanceSlot(2)" id="slot2Btn" class="px-2 py-1 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700 font-bold">12:00 (325)</button>
      <button onclick="setAttendanceSlot(3)" id="slot3Btn" class="px-2 py-1 bg-blue-500 text-slate-950 text-xs rounded font-bold shadow">13:00 (508★)</button>
      <button onclick="setAttendanceSlot(4)" id="slot4Btn" class="px-2 py-1 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700 font-bold">14:00 (145)</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="attendanceSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="attendanceExplanation" class="text-blue-300 font-medium">1:00 PM Slot: 508 Diners (Peak Attendance!). Represented as 5 Hundreds (500) + 0 Tens + 8 Ones. Notice the 0 tens placeholder!</span>
  </div>
</div>
""",
        3: """
<div class="flex flex-col h-full bg-violet-950/20 rounded-xl p-3 border border-violet-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-violet-500/20 text-violet-300 border border-violet-500/30">Digit Manipulation Lab</span>
      <span class="text-xs text-slate-400">Cards: [3] [7] [5] [0] [8]</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="presetDigitChallenge('largest')" id="btnLargest3d" class="px-2 py-0.5 bg-violet-600 text-white font-bold text-xs rounded">Largest (875)</button>
      <button onclick="presetDigitChallenge('smallest')" id="btnSmallest3d" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">Smallest (305)</button>
      <button onclick="presetDigitChallenge('under550')" id="btnUnder550" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded border border-slate-700">&lt; 550 (537)</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-3 border border-slate-800 flex flex-col justify-between items-center">
    <div class="flex items-center gap-4">
      <div class="flex flex-col items-center">
        <span class="text-[10px] text-slate-400 font-bold uppercase tracking-wider mb-1">Hundreds</span>
        <div id="cardHundredsSlot" class="w-16 h-20 bg-violet-900/80 border-2 border-violet-500 rounded-xl flex items-center justify-center text-3xl font-black text-violet-200 font-mono shadow-lg">8</div>
      </div>
      <div class="flex flex-col items-center">
        <span class="text-[10px] text-slate-400 font-bold uppercase tracking-wider mb-1">Tens</span>
        <div id="cardTensSlot" class="w-16 h-20 bg-indigo-900/80 border-2 border-indigo-500 rounded-xl flex items-center justify-center text-3xl font-black text-indigo-200 font-mono shadow-lg">7</div>
      </div>
      <div class="flex flex-col items-center">
        <span class="text-[10px] text-slate-400 font-bold uppercase tracking-wider mb-1">Ones</span>
        <div id="cardOnesSlot" class="w-16 h-20 bg-cyan-900/80 border-2 border-cyan-500 rounded-xl flex items-center justify-center text-3xl font-black text-cyan-200 font-mono shadow-lg">5</div>
      </div>
    </div>
    <div class="flex items-center gap-2 mt-2">
      <span class="text-xs text-slate-400">Available Cards:</span>
      <span class="px-2 py-1 bg-slate-800 rounded font-mono font-bold text-xs text-amber-300 border border-slate-700">3</span>
      <span class="px-2 py-1 bg-slate-800 rounded font-mono font-bold text-xs text-amber-300 border border-slate-700">7</span>
      <span class="px-2 py-1 bg-slate-800 rounded font-mono font-bold text-xs text-amber-300 border border-slate-700">5</span>
      <span class="px-2 py-1 bg-slate-800 rounded font-mono font-bold text-xs text-amber-300 border border-slate-700">0</span>
      <span class="px-2 py-1 bg-slate-800 rounded font-mono font-bold text-xs text-amber-300 border border-slate-700">8</span>
    </div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="digitCardExplanation" class="text-violet-300 font-medium">Largest 3-Digit Number: 875. Placing largest digits in highest place value positions maximizes the number's magnitude!</span>
  </div>
</div>
""",
        4: """
<div class="flex flex-col h-full bg-teal-950/20 rounded-xl p-3 border border-teal-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-teal-500/20 text-teal-300 border border-teal-500/30">Number Line Skip Counter</span>
      <span class="text-xs text-slate-400">Scale: 200 to 600</span>
    </div>
    <div class="flex items-center gap-1">
      <button onclick="skipNumberLine(-10)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded border border-slate-700 font-bold">-10</button>
      <button onclick="skipNumberLine(-1)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded border border-slate-700 font-bold">-1</button>
      <button onclick="skipNumberLine(1)" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded border border-slate-700 font-bold">+1</button>
      <button onclick="skipNumberLine(10)" class="px-2 py-1 bg-teal-500 hover:bg-teal-400 text-slate-950 font-bold text-xs rounded shadow">+10</button>
      <button onclick="resetNumberLine(340)" class="px-2 py-1 bg-slate-800 text-slate-400 text-xs rounded border border-slate-700">Reset</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="numberLineSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 grid grid-cols-3 gap-2 text-center text-xs">
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Current Value</span>
      <span id="numberLineCurrentVal" class="font-bold text-teal-300 text-sm font-mono">340</span>
    </div>
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Previous (-10)</span>
      <span id="numberLinePrevVal" class="font-bold text-slate-400 text-sm font-mono">330</span>
    </div>
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Next (+10)</span>
      <span id="numberLineNextVal" class="font-bold text-amber-400 text-sm font-mono">350</span>
    </div>
  </div>
</div>
""",
        5: """
<div class="flex flex-col h-full bg-indigo-950/20 rounded-xl p-3 border border-indigo-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">Indian Base-10 System</span>
      <span class="text-xs text-slate-400">Tenfold Multiplicative Position</span>
    </div>
    <div class="flex items-center gap-1.5">
      <span class="text-xs text-slate-300">Test Digit:</span>
      <button onclick="setIndianSystemDigit(5)" class="w-7 h-7 bg-indigo-600 text-white font-bold rounded text-xs">5</button>
      <button onclick="setIndianSystemDigit(7)" class="w-7 h-7 bg-slate-800 text-slate-300 font-bold rounded text-xs border border-slate-700">7</button>
      <button onclick="setIndianSystemDigit(9)" class="w-7 h-7 bg-slate-800 text-slate-300 font-bold rounded text-xs border border-slate-700">9</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="indianSystemSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="indianSystemText" class="text-indigo-300 font-medium">Each shift to the left multiplies the digit's value by 10: 5 in Ones = 5, in Tens = 50, in Hundreds = 500, in Thousands = 5,000!</span>
  </div>
</div>
""",
        6: """
<div class="flex flex-col h-full bg-emerald-950/20 rounded-xl p-3 border border-emerald-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Threshold to 1,000</span>
      <span class="text-xs text-slate-400">Sequential Counter 995 to 1005</span>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="stepThresholdCounter(-1)" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded border border-slate-700 font-bold">- 1</button>
      <button onclick="stepThresholdCounter(1)" class="px-3 py-1 bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs rounded font-bold shadow">+ 1 Step</button>
      <button onclick="resetThresholdCounter(999)" class="px-2 py-1 bg-slate-800 text-slate-400 text-xs rounded border border-slate-700">Set 999</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-3 border border-slate-800 flex flex-col justify-center items-center">
    <div id="thresholdOdometerDisplay" class="flex items-center gap-2 font-mono"></div>
    <div id="thresholdMilestoneBadge" class="mt-3 px-3 py-1 bg-amber-500/20 border border-amber-500/40 rounded-full text-amber-300 text-xs font-bold animate-pulse">
      Largest 3-Digit Number
    </div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="thresholdExplanation" class="text-emerald-300 font-medium">At 999, adding 1 unit triggers full regrouping: 10 ones -> 1 ten, 10 tens -> 1 hundred, 10 hundreds -> 1 THOUSAND (1000)!</span>
  </div>
</div>
""",
        7: """
<div class="flex flex-col h-full bg-orange-950/20 rounded-xl p-3 border border-orange-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-orange-500/20 text-orange-300 border border-orange-500/30">Real-World Thousands</span>
      <span class="text-xs text-slate-400">Indian Heritage & Conservation</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="selectHeritageFact('temple')" id="factTempleBtn" class="px-2 py-1 bg-orange-500 text-slate-950 font-bold text-xs rounded">1000 Pillars</button>
      <button onclick="selectHeritageFact('rhino')" id="factRhinoBtn" class="px-2 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded border border-slate-700">Rhino (4000)</button>
      <button onclick="selectHeritageFact('coast')" id="factCoastBtn" class="px-2 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded border border-slate-700">Coast (7500 km)</button>
      <button onclick="selectHeritageFact('districts')" id="factDistBtn" class="px-2 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded border border-slate-700">Districts (788)</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="heritageSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="heritageDescriptionText" class="text-orange-300 font-medium">Saavira Kambada Basadi (Moodubidiri, Karnataka): Built in the 1500s, this historic Jain shrine is supported by exactly 1,000 carved granite stone pillars!</span>
  </div>
</div>
""",
        8: """
<div class="flex flex-col h-full bg-cyan-950/20 rounded-xl p-3 border border-cyan-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Base-Ten Block Builder</span>
      <span class="text-xs text-slate-400">From 1 Unit to 1,000 Cube</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="setBaseTenStage(1)" id="btnStage1" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">1 Unit</button>
      <button onclick="setBaseTenStage(2)" id="btnStage2" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">10 (Rod)</button>
      <button onclick="setBaseTenStage(3)" id="btnStage3" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">100 (Flat)</button>
      <button onclick="setBaseTenStage(4)" id="btnStage4" class="px-2 py-0.5 bg-cyan-500 text-slate-950 font-bold text-xs rounded shadow">1000 (Cube)</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="baseTenSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="baseTenExplanation" class="text-cyan-300 font-medium">1 Thousand-Cube = 10 Hundred-Flats = 100 Ten-Rods = 1,000 Individual Unit Cubes!</span>
  </div>
</div>
"""
    }

if __name__ == '__main__':
    sims = get_sims_part1()
    print(f"Generated {len(sims)} simulators for part 1.")
