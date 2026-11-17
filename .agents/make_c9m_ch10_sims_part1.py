#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 9 Maths Chapter 10: How Quantities Combine: Understanding Data
Part 1: Simulators 1 to 8 (Slides 1 to 8)
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⚖️</span> Simple Mean vs Weighted Mean Intro Explorer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>Weight W₁ on Value x₁ = 60:</span>
        <span id="c9c10s1W1Lbl" class="text-cyan-300 font-bold">W₁ = 1</span>
      </div>
      <input id="c9c10s1W1" type="range" min="1" max="10" value="1" oninput="c9c10s1Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>Weight W₂ on Value x₂ = 90:</span>
        <span id="c9c10s1W2Lbl" class="text-amber-300 font-bold">W₂ = 4</span>
      </div>
      <input id="c9c10s1W2" type="range" min="1" max="10" value="4" oninput="c9c10s1Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9c10s1Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c10s1Draw = function(){
    const w1 = parseInt(document.getElementById('c9c10s1W1').value, 10);
    const w2 = parseInt(document.getElementById('c9c10s1W2').value, 10);
    document.getElementById('c9c10s1W1Lbl').textContent = 'W₁ = ' + w1;
    document.getElementById('c9c10s1W2Lbl').textContent = 'W₂ = ' + w2;
    const simple = (60 + 90) / 2;
    const weighted = ((w1 * 60 + w2 * 90) / (w1 + w2)).toFixed(2);
    document.getElementById('c9c10s1Out').innerHTML = `
      <div class="flex flex-wrap justify-between gap-2">
        <span>Naive Simple Mean (60+90)/2: <strong class="text-slate-400">${simple.toFixed(2)}</strong></span>
        <span>True Weighted Mean: <strong class="text-emerald-300 text-sm">${weighted}</strong></span>
      </div>
      <div class="text-cyan-300">${w1 === w2 ? 'Equal weights (W₁ = W₂) make Weighted Mean = Simple Mean!' : 'Unequal weights pull the mean toward the heavier-weighted value!'}</div>
    `;
  };
  setTimeout(window.c9c10s1Draw, 40);
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🏀</span> Group Size Imbalance &amp; Academy Height Bias Visualizer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>Group A Count (avg 180 cm):</span>
        <span id="c9c10s2NLbl" class="text-cyan-300 font-bold">n = 4</span>
      </div>
      <input id="c9c10s2N" type="range" min="2" max="20" value="4" oninput="c9c10s2Draw()" class="w-full accent-cyan-400">
    </label>
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>Group B Count (avg 140 cm):</span>
        <span id="c9c10s2MLbl" class="text-amber-300 font-bold">m = 16</span>
      </div>
      <input id="c9c10s2M" type="range" min="2" max="20" value="16" oninput="c9c10s2Draw()" class="w-full accent-amber-400">
    </label>
  </div>
  <div id="c9c10s2Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-2"></div>
</div>
<script>
(function(){
  window.c9c10s2Draw = function(){
    const n = parseInt(document.getElementById('c9c10s2N').value, 10);
    const m = parseInt(document.getElementById('c9c10s2M').value, 10);
    document.getElementById('c9c10s2NLbl').textContent = 'n = ' + n;
    document.getElementById('c9c10s2MLbl').textContent = 'm = ' + m;
    const avg = (180*n + 140*m) / (n + m);
    const bias = +(avg - 160).toFixed(2);
    document.getElementById('c9c10s2Out').innerHTML = `
      <div class="font-bold text-emerald-300 text-sm">True Combined Height = ${avg.toFixed(2)} cm (Naive Average = 160 cm)</div>
      <div>Total Sum = 180(${n}) + 140(${m}) = ${180*n + 140*m} cm across ${n + m} athletes.</div>
      <div class="text-amber-300">Error of "Average of Averages": ${bias === 0 ? '0 cm (only because n = m!)' : Math.abs(bias) + ' cm off!'}</div>
    `;
  };
  setTimeout(window.c9c10s2Draw, 40);
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧮</span> Combined Average (an + bm) / (n + m) Live Calculator
  </h3>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Avg a:</span><input id="c9c10s3A" type="number" value="75" oninput="c9c10s3Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Size n:</span><input id="c9c10s3N" type="number" min="1" value="20" oninput="c9c10s3Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Avg b:</span><input id="c9c10s3B" type="number" value="85" oninput="c9c10s3Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Size m:</span><input id="c9c10s3M" type="number" min="1" value="30" oninput="c9c10s3Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c10s3Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c10s3Draw = function(){
    const a = parseFloat(document.getElementById('c9c10s3A').value || '0');
    const n = Math.max(1, parseFloat(document.getElementById('c9c10s3N').value || '1'));
    const b = parseFloat(document.getElementById('c9c10s3B').value || '0');
    const m = Math.max(1, parseFloat(document.getElementById('c9c10s3M').value || '1'));
    const comb = (a*n + b*m) / (n + m);
    const simp = (a + b) / 2;
    document.getElementById('c9c10s3Out').innerHTML = `
      <div class="font-bold text-emerald-300 text-sm">Combined Average = (${a}×${n} + ${b}×${m}) / (${n} + ${m}) = ${comb.toFixed(2)}</div>
      <div>Simple Average (a + b)/2 = ${simp.toFixed(2)} &nbsp;•&nbsp; Match? <strong class="text-amber-300">${n === m || a === b ? 'YES (since ' + (n === m ? 'n = m' : 'a = b') + ')' : 'NO (n ≠ m and a ≠ b)'}</strong></div>
    `;
  };
  setTimeout(window.c9c10s3Draw, 40);
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🧪</span> Two-Batch Mixture Concentration Blender
  </h3>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Batch 1 Vol (L):</span><input id="c9c10s4V1" type="number" min="1" value="2" oninput="c9c10s4Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Batch 1 (%):</span><input id="c9c10s4C1" type="number" min="0" max="100" value="10" oninput="c9c10s4Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Batch 2 Vol (L):</span><input id="c9c10s4V2" type="number" min="1" value="3" oninput="c9c10s4Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Batch 2 (%):</span><input id="c9c10s4C2" type="number" min="0" max="100" value="20" oninput="c9c10s4Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c10s4Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c10s4Draw = function(){
    const v1 = Math.max(0.1, parseFloat(document.getElementById('c9c10s4V1').value || '1'));
    const c1 = parseFloat(document.getElementById('c9c10s4C1').value || '0');
    const v2 = Math.max(0.1, parseFloat(document.getElementById('c9c10s4V2').value || '1'));
    const c2 = parseFloat(document.getElementById('c9c10s4C2').value || '0');
    const solute = v1*(c1/100) + v2*(c2/100);
    const totalV = v1 + v2;
    const pct = (solute / totalV) * 100;
    document.getElementById('c9c10s4Out').innerHTML = `
      <div class="font-bold text-emerald-300 text-sm">Final Concentration = ${pct.toFixed(2)}%</div>
      <div>Total Pure Solute = ${(v1*c1/100).toFixed(3)} L + ${(v2*c2/100).toFixed(3)} L = <strong>${solute.toFixed(3)} L</strong> in <strong>${totalV} L</strong> total.</div>
    `;
  };
  setTimeout(window.c9c10s4Draw, 40);
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🪙</span> Brahmagupta-Śrīdharācārya Karat/Varna Gold Alloy Calculator
  </h3>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Piece 1 (g):</span><input id="c9c10s5W1" type="number" min="1" value="10" oninput="c9c10s5Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Piece 1 Karat:</span><input id="c9c10s5K1" type="number" min="1" max="24" value="18" oninput="c9c10s5Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Piece 2 (g):</span><input id="c9c10s5W2" type="number" min="1" value="20" oninput="c9c10s5Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Piece 2 Karat:</span><input id="c9c10s5K2" type="number" min="1" max="24" value="24" oninput="c9c10s5Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c10s5Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c10s5Draw = function(){
    const w1 = Math.max(0.1, parseFloat(document.getElementById('c9c10s5W1').value || '1'));
    const k1 = parseFloat(document.getElementById('c9c10s5K1').value || '0');
    const w2 = Math.max(0.1, parseFloat(document.getElementById('c9c10s5W2').value || '1'));
    const k2 = parseFloat(document.getElementById('c9c10s5K2').value || '0');
    const karat = (w1*k1 + w2*k2) / (w1 + w2);
    const pct = (karat / 24) * 100;
    document.getElementById('c9c10s5Out').innerHTML = `
      <div class="font-bold text-amber-300 text-sm">Melted Ingot Purity = ${karat.toFixed(2)} Karats (${pct.toFixed(1)}% pure gold)</div>
      <div>Formula: (${w1}×${k1} + ${w2}×${k2}) / (${w1} + ${w2}) = ${(w1*k1 + w2*k2).toFixed(1)} / ${(w1 + w2).toFixed(1)}</div>
    `;
  };
  setTimeout(window.c9c10s5Draw, 40);
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📊</span> Multi-Component Weighted Mean Engine
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
    <label class="bg-slate-950 p-3 rounded-xl border border-slate-800 block">
      <div class="flex justify-between font-semibold text-slate-300 mb-1">
        <span>Scale All Weights by Factor (k):</span>
        <span id="c9c10s6KLbl" class="text-amber-300 font-bold">k = 1×</span>
      </div>
      <input id="c9c10s6K" type="range" min="1" max="5" value="1" oninput="c9c10s6Draw()" class="w-full accent-amber-400">
    </label>
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-slate-300">
      Base Values: <strong>x = (10, 20, 30)</strong><br>Base Weights: <strong>W = (2, 3, 5)</strong>
    </div>
  </div>
  <div id="c9c10s6Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c10s6Draw = function(){
    const k = parseInt(document.getElementById('c9c10s6K').value, 10);
    document.getElementById('c9c10s6KLbl').textContent = 'k = ' + k + '×';
    const w = [2*k, 3*k, 5*k];
    const x = [10, 20, 30];
    const num = w[0]*x[0] + w[1]*x[1] + w[2]*x[2];
    const den = w[0] + w[1] + w[2];
    document.getElementById('c9c10s6Out').innerHTML = `
      <div>Scaled Weights: <strong>(${w.join(', ')})</strong></div>
      <div class="font-bold text-emerald-300 text-sm">x̄ = ${num} / ${den} = ${(num/den).toFixed(2)} (Always invariant under scaling!)</div>
      <div class="text-cyan-300">Bounded strictly inside [min(x) = 10, max(x) = 30].</div>
    `;
  };
  setTimeout(window.c9c10s6Draw, 40);
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🎓</span> Academic Grading Weight &amp; Final Score Simulator
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Internals (20%):</span><input id="c9c10s7I" type="number" min="0" max="100" value="90" oninput="c9c10s7Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Project (30%):</span><input id="c9c10s7P" type="number" min="0" max="100" value="80" oninput="c9c10s7Draw()" class="w-full mt-1 bg-slate-900 text-emerald-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Final Exam (50%):</span><input id="c9c10s7F" type="number" min="0" max="100" value="60" oninput="c9c10s7Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c10s7Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c10s7Draw = function(){
    const i = parseFloat(document.getElementById('c9c10s7I').value || '0');
    const p = parseFloat(document.getElementById('c9c10s7P').value || '0');
    const f = parseFloat(document.getElementById('c9c10s7F').value || '0');
    const wScore = 0.2*i + 0.3*p + 0.5*f;
    const simp = (i + p + f) / 3;
    document.getElementById('c9c10s7Out').innerHTML = `
      <div class="font-bold text-emerald-300 text-sm">Weighted Course Grade = ${(0.2*i).toFixed(1)} + ${(0.3*p).toFixed(1)} + ${(0.5*f).toFixed(1)} = ${wScore.toFixed(1)}%</div>
      <div>Unweighted Simple Average would be ${simp.toFixed(1)}%.</div>
    `;
  };
  setTimeout(window.c9c10s7Draw, 40);
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⭐</span> Restaurant &amp; Review Recency Weighted Scorer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-xs">
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Food (Wt 5):</span><input id="c9c10s8F" type="number" step="0.1" min="1" max="5" value="4.8" oninput="c9c10s8Draw()" class="w-full mt-1 bg-slate-900 text-cyan-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Service (Wt 3):</span><input id="c9c10s8S" type="number" step="0.1" min="1" max="5" value="4.0" oninput="c9c10s8Draw()" class="w-full mt-1 bg-slate-900 text-emerald-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
    <label class="bg-slate-950 p-2.5 rounded-xl border border-slate-800 block"><span class="text-slate-400">Ambience (Wt 2):</span><input id="c9c10s8A" type="number" step="0.1" min="1" max="5" value="3.0" oninput="c9c10s8Draw()" class="w-full mt-1 bg-slate-900 text-amber-300 font-bold border border-slate-700 rounded px-2 py-1"></label>
  </div>
  <div id="c9c10s8Out" class="p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 space-y-1.5"></div>
</div>
<script>
(function(){
  window.c9c10s8Draw = function(){
    const f = parseFloat(document.getElementById('c9c10s8F').value || '4');
    const s = parseFloat(document.getElementById('c9c10s8S').value || '4');
    const a = parseFloat(document.getElementById('c9c10s8A').value || '3');
    const w = (5*f + 3*s + 2*a) / 10;
    document.getElementById('c9c10s8Out').innerHTML = `
      <div class="font-bold text-amber-300 text-sm">Weighted Rating = (5×${f} + 3×${s} + 2×${a}) / 10 = ${w.toFixed(2)} ★</div>
      <div>Food carries 50% of total importance, Service 30%, Ambience 20%.</div>
    `;
  };
  setTimeout(window.c9c10s8Draw, 40);
})();
</script>
"""
}
