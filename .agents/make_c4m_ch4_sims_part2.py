# -*- coding: utf-8 -*-
"""
Interactive SVG/HTML Simulators 9 to 16 for Class 4 Maths Chapter 4: Thousands Around Us
"""

def get_sims_part2():
    return {
        9: """
<div class="flex flex-col h-full bg-orange-950/20 rounded-xl p-3 border border-orange-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-orange-500/20 text-orange-300 border border-orange-500/30">Decomposing 1,000</span>
      <span class="text-xs text-slate-400">Orange Slice Complements</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="selectOrangeSlice(0)" class="px-2 py-0.5 bg-orange-500 text-slate-950 font-bold text-xs rounded">900 + 100</button>
      <button onclick="selectOrangeSlice(1)" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">850 + 150</button>
      <button onclick="selectOrangeSlice(2)" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">670 + 330</button>
      <button onclick="selectOrangeSlice(3)" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">497 + 503</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="orangeSliceSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="orangeEquationText" class="text-orange-300 font-bold text-sm">900 + 100 = 1,000 (Complementary Pair)</span>
  </div>
</div>
""",
        10: """
<div class="flex flex-col h-full bg-emerald-950/20 rounded-xl p-3 border border-emerald-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Place-Value Regrouping</span>
      <span class="text-xs text-slate-400">Bundling Loose Units</span>
    </div>
    <div class="flex items-center gap-1">
      <button onclick="loadRegroupCase(1)" id="rgCase1Btn" class="px-2 py-0.5 bg-emerald-600 text-white font-bold text-xs rounded">1T + 27O</button>
      <button onclick="loadRegroupCase(2)" id="rgCase2Btn" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">10T + 6O</button>
      <button onclick="loadRegroupCase(3)" id="rgCase3Btn" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">11T + 14O</button>
      <button onclick="loadRegroupCase(4)" id="rgCase4Btn" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">35 Tens</button>
      <button onclick="loadRegroupCase(5)" id="rgCase5Btn" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">2H+13T+7O</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-3 border border-slate-800 flex flex-col justify-center items-center">
    <div id="regroupAnimationContainer" class="flex items-center gap-4"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="regroupExplanationText" class="text-emerald-300 font-medium">1 Ten + 27 Ones: 27 Ones bundles into 2 Tens + 7 Ones. 1 Ten + 2 Tens = 3 Tens. Total = 37!</span>
  </div>
</div>
""",
        11: """
<div class="flex flex-col h-full bg-blue-950/20 rounded-xl p-3 border border-blue-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/30">Color-Coded Token Model</span>
      <span class="text-xs text-slate-400">Thousands, Hundreds, Tens, Ones</span>
    </div>
    <div class="flex items-center gap-1.5">
      <span class="text-xs text-slate-300">Preset:</span>
      <button onclick="setTokenNumber(3019)" class="px-2 py-0.5 bg-blue-600 text-white font-bold text-xs rounded">3019</button>
      <button onclick="setTokenNumber(4508)" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">4508</button>
      <button onclick="setTokenNumber(2008)" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">2008</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="tokenModelSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 grid grid-cols-2 gap-2 text-center text-xs">
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Expanded Addition</span>
      <span id="tokenExpandedDisplay" class="font-bold text-cyan-300 text-xs font-mono">3000 + 0 + 10 + 9</span>
    </div>
    <div class="bg-slate-900/90 p-1.5 rounded border border-slate-800">
      <span class="text-slate-400 block text-[10px]">Number Name</span>
      <span id="tokenWordsDisplay" class="font-bold text-amber-300 text-xs">Three thousand nineteen</span>
    </div>
  </div>
</div>
""",
        12: """
<div class="flex flex-col h-full bg-violet-950/20 rounded-xl p-3 border border-violet-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-violet-500/20 text-violet-300 border border-violet-500/30">Place Value Slider</span>
      <span class="text-xs text-slate-400">Sliding Mechanism & Placeholder Zero</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="applySliderOffset('ones', 1)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded border border-slate-700 font-bold">+1 Ones</button>
      <button onclick="applySliderOffset('tens', 2)" class="px-2 py-0.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded border border-slate-700 font-bold">+20 Tens</button>
      <button onclick="togglePlaceholderTrap()" id="btnZeroTrap" class="px-2 py-0.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs rounded shadow">Zero Trap (7024)</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 flex items-center justify-center">
    <div class="flex items-center gap-3">
      <div class="flex flex-col items-center">
        <button onclick="stepSliderCol('th', 1)" class="text-xs text-slate-400 hover:text-white mb-1">▲</button>
        <div id="slideThBox" class="w-14 h-18 bg-violet-900/80 border-2 border-violet-500 rounded-lg flex items-center justify-center text-3xl font-black text-violet-200 font-mono shadow-lg">1</div>
        <button onclick="stepSliderCol('th', -1)" class="text-xs text-slate-400 hover:text-white mt-1">▼</button>
        <span class="text-[9px] text-slate-400 mt-1 uppercase">Th</span>
      </div>
      <div class="flex flex-col items-center">
        <button onclick="stepSliderCol('h', 1)" class="text-xs text-slate-400 hover:text-white mb-1">▲</button>
        <div id="slideHBox" class="w-14 h-18 bg-indigo-900/80 border-2 border-indigo-500 rounded-lg flex items-center justify-center text-3xl font-black text-indigo-200 font-mono shadow-lg">8</div>
        <button onclick="stepSliderCol('h', -1)" class="text-xs text-slate-400 hover:text-white mt-1">▼</button>
        <span class="text-[9px] text-slate-400 mt-1 uppercase">H</span>
      </div>
      <div class="flex flex-col items-center">
        <button onclick="stepSliderCol('t', 1)" class="text-xs text-slate-400 hover:text-white mb-1">▲</button>
        <div id="slideTBox" class="w-14 h-18 bg-cyan-900/80 border-2 border-cyan-500 rounded-lg flex items-center justify-center text-3xl font-black text-cyan-200 font-mono shadow-lg">9</div>
        <button onclick="stepSliderCol('t', -1)" class="text-xs text-slate-400 hover:text-white mt-1">▼</button>
        <span class="text-[9px] text-slate-400 mt-1 uppercase">T</span>
      </div>
      <div class="flex flex-col items-center">
        <button onclick="stepSliderCol('o', 1)" class="text-xs text-slate-400 hover:text-white mb-1">▲</button>
        <div id="slideOBox" class="w-14 h-18 bg-emerald-900/80 border-2 border-emerald-500 rounded-lg flex items-center justify-center text-3xl font-black text-emerald-200 font-mono shadow-lg">5</div>
        <button onclick="stepSliderCol('o', -1)" class="text-xs text-slate-400 hover:text-white mt-1">▼</button>
        <span class="text-[9px] text-slate-400 mt-1 uppercase">O</span>
      </div>
    </div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="sliderExplanationText" class="text-violet-300 font-medium">Current Slider Number: 1895. Use arrows or buttons above to slide values.</span>
  </div>
</div>
""",
        13: """
<div class="flex flex-col h-full bg-teal-950/20 rounded-xl p-3 border border-teal-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-teal-500/20 text-teal-300 border border-teal-500/30">4-Digit Number Scale</span>
      <span class="text-xs text-slate-400">Calibrated Multi-Scale Ranges</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="setScaleRange(1)" id="scaleBtn1" class="px-2 py-0.5 bg-teal-600 text-white font-bold text-xs rounded">1000–1100</button>
      <button onclick="setScaleRange(2)" id="scaleBtn2" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">2000–2500</button>
      <button onclick="setScaleRange(3)" id="scaleBtn3" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">5500–5700</button>
      <button onclick="setScaleRange(4)" id="scaleBtn4" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">Filter (2226-3226)</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="fourDigitScaleSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="scaleExplanationText" class="text-teal-300 font-medium">Scale 1000 to 1100: Divided into 10 tick marks of 10 units each. Midpoint sits at 1050.</span>
  </div>
</div>
""",
        14: """
<div class="flex flex-col h-full bg-fuchsia-950/20 rounded-xl p-3 border border-fuchsia-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-fuchsia-500/20 text-fuchsia-300 border border-fuchsia-500/30">Arrow Card Workshop</span>
      <span class="text-xs text-slate-400">Layering & Deconstruction</span>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="setArrowCardMode('assembled')" id="arrowAssembledBtn" class="px-2.5 py-1 bg-fuchsia-600 text-white font-bold text-xs rounded shadow">Assemble (3452)</button>
      <button onclick="setArrowCardMode('expanded')" id="arrowExpandedBtn" class="px-2.5 py-1 bg-slate-800 text-slate-300 font-bold text-xs rounded border border-slate-700">Pull Apart (Expand)</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="arrowCardSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="arrowCardText" class="text-fuchsia-300 font-medium">Assembled Arrow Cards: 3000 + 400 + 50 + 2 overlap to display the standard 4-digit numeral 3452!</span>
  </div>
</div>
""",
        15: """
<div class="flex flex-col h-full bg-cyan-950/20 rounded-xl p-3 border border-cyan-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">Left-to-Right Comparison</span>
      <span class="text-xs text-slate-400">Thousands Column Priority</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="comparePair(1)" id="cmpPair1Btn" class="px-2 py-0.5 bg-cyan-600 text-white font-bold text-xs rounded">1213 vs 2121</button>
      <button onclick="comparePair(2)" id="cmpPair2Btn" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">1300 vs 2300</button>
      <button onclick="comparePair(3)" id="cmpPair3Btn" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">3425 vs 3452</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 relative flex items-center justify-center overflow-hidden">
    <div id="compareBalanceSvgWrap" class="w-full h-full flex items-center justify-center"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="compareExplanationText" class="text-cyan-300 font-medium">Comparing 1213 vs 2121: 1 Thousand &lt; 2 Thousands. Thus, 1213 &lt; 2121!</span>
  </div>
</div>
""",
        16: """
<div class="flex flex-col h-full bg-emerald-950/20 rounded-xl p-3 border border-emerald-500/30">
  <div class="flex items-center justify-between mb-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Ordering Real-World Records</span>
      <span class="text-xs text-slate-400">Mountains, Cricket & Prices</span>
    </div>
    <div class="flex items-center gap-1.5">
      <button onclick="loadOrderingTheme('mountains')" id="themeMtnBtn" class="px-2 py-0.5 bg-emerald-600 text-white font-bold text-xs rounded">Himalayas (m)</button>
      <button onclick="loadOrderingTheme('prices')" id="themePricesBtn" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">Prices (₹)</button>
      <button onclick="loadOrderingTheme('cricket')" id="themeCricketBtn" class="px-2 py-0.5 bg-slate-800 text-slate-300 text-xs rounded border border-slate-700">Cricket Runs</button>
    </div>
  </div>
  <div class="flex-1 bg-slate-950/80 rounded-lg p-2 border border-slate-800 overflow-auto flex flex-col justify-center">
    <div id="orderingRecordsContainer" class="space-y-2 p-2"></div>
  </div>
  <div class="mt-2 bg-slate-900/90 p-2 rounded border border-slate-800 text-center text-xs">
    <span id="orderingSummaryText" class="text-emerald-300 font-medium">Himalayan Peaks in Decreasing Order: Kangchenjunga (8586 m) > Nanda Devi (7816 m) > Chaukhamba (7138 m).</span>
  </div>
</div>
"""
    }

if __name__ == '__main__':
    sims = get_sims_part2()
    print(f"Generated {len(sims)} simulators for part 2.")
