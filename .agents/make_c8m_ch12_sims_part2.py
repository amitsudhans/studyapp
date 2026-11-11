#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 8 Maths Chapter 12: Tales by Dots and Lines
Part 2: Simulators 9 to 16
"""

simulators_part2 = {
    9: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
      <span>🔍</span> 2-Step Line Graph Slope & Trend Inspector
    </h3>
    <div class="flex gap-1.5 text-xs">
      <button type="button" onclick="c12s9Step(1)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">Step 1: Axes & Slopes</button>
      <button type="button" onclick="c12s9Step(2)" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">Step 2: Peaks & Troughs</button>
    </div>
  </div>
  <svg viewBox="0 0 340 120" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800">
    <polyline points="25,95 90,35 165,35 230,85 310,25" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
    <circle cx="90" cy="35" r="4" fill="#fbbf24"/><circle cx="230" cy="85" r="4" fill="#fb7185"/><circle cx="310" cy="25" r="4" fill="#34d399"/>
    <text x="128" y="28" text-anchor="middle" fill="#cbd5e1" font-size="9">Flat (0 slope)</text>
    <text x="230" y="102" text-anchor="middle" fill="#fb7185" font-size="9">Trough</text>
    <text x="295" y="16" text-anchor="middle" fill="#34d399" font-size="9">Global Peak</text>
  </svg>
  <div id="c12s9Desc" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c12s9Step = function(s){
    document.getElementById('c12s9Desc').innerHTML = s === 1
      ? '<b class="text-cyan-300">Step 1 (Read Skeleton):</b> Inspect axis units, check if y-axis begins at 0, identify legend markers, and classify slopes (rising ↑, horizontal 0-change →, falling ↓).'
      : '<b class="text-emerald-300">Step 2 (Infer Story):</b> Spot maximum Peaks, minimum Troughs, total vertical range, and explain real-world events driving each trend!';
  };
  window.c12s9Step(1);
})();
</script>
""",
    10: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
      <span>🛰️</span> Real-World Line Datasets: Space, Monsoon & Births
    </h3>
    <div class="flex flex-wrap gap-1.5 text-xs">
      <button type="button" onclick="c12s10Show('space')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 border border-slate-700">UN Space Launches</button>
      <button type="button" onclick="c12s10Show('rain')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700">East/West Rainfall</button>
      <button type="button" onclick="c12s10Show('births')" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-300 border border-slate-700">Live Birth Waves</button>
    </div>
  </div>
  <svg id="c12s10Svg" viewBox="0 0 340 120" class="w-full h-28 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c12s10Info" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  window.c12s10Show = function(k){
    const svg = document.getElementById('c12s10Svg');
    const info = document.getElementById('c12s10Info');
    if(!svg || !info) return;
    if(k === 'space'){
      svg.innerHTML = `<polyline points="20,102 100,98 180,95 230,85 270,50 320,14" fill="none" stroke="#22d3ee" stroke-width="3"/>`;
      info.innerHTML = `<b class="text-cyan-300">UN Space Objects Launched:</b> Long steady plateau explodes upward into a massive modern spike driven by small-satellite constellations!`;
    } else if(k === 'rain'){
      svg.innerHTML = `<polyline points="20,105 90,100 150,20 200,25 250,90 320,105" fill="none" stroke="#38bdf8" stroke-width="2.5"/><polyline points="20,100 90,98 150,82 200,75 265,24 315,65" fill="none" stroke="#fbbf24" stroke-width="2.5"/>`;
      info.innerHTML = `<b class="text-amber-300">West vs East Coast Rainfall:</b> Blue (West Coast) peaks June–Sept (SW Monsoon); Gold (Chennai East Coast) peaks Oct–Dec (NE Monsoon)!`;
    } else {
      svg.innerHTML = `<polyline points="20,80 60,72 100,88 150,60 210,38 260,55 320,76" fill="none" stroke="#34d399" stroke-width="2.5"/>`;
      info.innerHTML = `<b class="text-emerald-300">Monthly Live Births:</b> Seasonal waves reveal predictable spring troughs followed by late-summer / autumn birth peaks across years.`;
    }
  };
  window.c12s10Show('rain');
})();
</script>
""",
    11: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🌾</span> India Rice vs Wheat Dietary Infographic Explorer
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-xs">
    <div class="p-3 rounded-xl bg-amber-500/15 border border-amber-400/40">
      <div class="font-bold text-amber-300 mb-1">North & Northwest Plains</div>
      <div class="text-slate-200">Punjab, Haryana, Rajasthan, UP, MP</div>
      <div class="mt-2 font-bold text-amber-200">🌾 Dominant: WHEAT</div>
    </div>
    <div class="p-3 rounded-xl bg-cyan-500/15 border border-cyan-400/40">
      <div class="font-bold text-cyan-300 mb-1">Central Transition Belt</div>
      <div class="text-slate-200">Maharashtra, Gujarat, Chhattisgarh borders</div>
      <div class="mt-2 font-bold text-cyan-200">⚖️ Mixed Rice & Wheat</div>
    </div>
    <div class="p-3 rounded-xl bg-emerald-500/15 border border-emerald-400/40">
      <div class="font-bold text-emerald-300 mb-1">South, East & Coastal States</div>
      <div class="text-slate-200">Kerala, TN, AP, Odisha, WB, Assam</div>
      <div class="mt-2 font-bold text-emerald-200">🍚 Dominant: RICE</div>
    </div>
  </div>
</div>
""",
    12: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>⏱️</span> What Can a Strip Say? 24-Hour (48 × 30-min Block) Routine Strips
  </h3>
  <div class="space-y-2 text-xs">
    <div>
      <div class="flex justify-between text-slate-300 mb-1"><span><b>Student Weekday:</b> 8h Sleep | 6h School | 3h Meals/Chores | 4h Play/Study | 3h Night Sleep</span><span>48 blocks (24h)</span></div>
      <div class="flex h-6 rounded-lg overflow-hidden border border-slate-700">
        <div class="bg-indigo-600" style="width:25%" title="Sleep 6h"></div><div class="bg-emerald-500" style="width:8%" title="Prep"></div><div class="bg-amber-500" style="width:25%" title="School 6h"></div><div class="bg-cyan-500" style="width:25%" title="Play/Study 6h"></div><div class="bg-indigo-600" style="width:17%" title="Night Sleep"></div>
      </div>
    </div>
    <div>
      <div class="flex justify-between text-slate-300 mb-1"><span><b>Student Weekend:</b> Extra Morning Sleep + Expanded Play (Zero School!)</span><span>48 blocks (24h)</span></div>
      <div class="flex h-6 rounded-lg overflow-hidden border border-slate-700">
        <div class="bg-indigo-600" style="width:33%" title="Longer Sleep"></div><div class="bg-emerald-500" style="width:10%" title="Breakfast"></div><div class="bg-cyan-500" style="width:40%" title="Outdoor Play & Leisure"></div><div class="bg-indigo-600" style="width:17%" title="Night Sleep"></div>
      </div>
    </div>
  </div>
  <div class="flex flex-wrap gap-3 text-[11px] text-slate-400">
    <span class="text-indigo-300">■ Sleep</span><span class="text-amber-300">■ School/Work</span><span class="text-cyan-300">■ Play/Leisure</span><span class="text-emerald-300">■ Meals/Chores</span>
  </div>
</div>
""",
    13: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>😴</span> Sleepy-Deepy Lifespan Curve (Ages 6 to 75 Years)
  </h3>
  <svg viewBox="0 0 360 130" class="w-full h-32 bg-slate-950 rounded-xl border border-slate-800">
    <path d="M 25 22 Q 95 62 175 78 Q 255 82 335 58" fill="none" stroke="#34d399" stroke-width="3"/>
    <circle cx="25" cy="22" r="4" fill="#fbbf24"/><circle cx="175" cy="78" r="4" fill="#38bdf8"/><circle cx="335" cy="58" r="4" fill="#a78bfa"/>
    <text x="58" y="18" fill="#fbbf24" font-size="9">Age 6 (~9.8 hrs)</text>
    <text x="175" y="96" text-anchor="middle" fill="#38bdf8" font-size="9">Mid-Adulthood (~7.5 hrs)</text>
    <text x="305" y="48" text-anchor="middle" fill="#a78bfa" font-size="9">Age 75 (~8.3 hrs)</text>
  </svg>
  <p class="text-xs text-slate-300">Smooth multi-point curves cleanly summarize 70 dense age points without creating a cluttered 70-bar picket fence!</p>
</div>
""",
    14: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>🏘️</span> Street Income Outlier Test: Mean vs Median
    </h3>
    <button type="button" onclick="c12s14Toggle()" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 text-xs border border-slate-700" id="c12s14Btn">+ Add ₹50L Billionaire Outlier</button>
  </div>
  <div id="c12s14Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-2"></div>
</div>
<script>
(function(){
  let hasOutlier = false;
  function render(){
    const base = [20, 22, 24, 25, 29];
    const arr = hasOutlier ? base.concat([5000]) : base;
    const mean = arr.reduce((a,b) => a+b, 0) / arr.length;
    const med = hasOutlier ? 24.5 : 24;
    document.getElementById('c12s14Btn').textContent = hasOutlier ? 'Remove Outlier' : '+ Add ₹50L Billionaire Outlier';
    document.getElementById('c12s14Out').innerHTML = `
      <div>Incomes (in ₹ Thousands): <b>[${arr.join(', ')}]</b></div>
      <div class="grid grid-cols-2 gap-2 text-center">
        <div class="p-2 rounded bg-slate-900 border border-rose-500/40"><div class="text-slate-400">Mean</div><div class="text-base font-bold text-rose-300">₹${mean.toFixed(1)}k</div></div>
        <div class="p-2 rounded bg-slate-900 border border-emerald-500/40"><div class="text-slate-400">Median</div><div class="text-base font-bold text-emerald-300">₹${med}k</div></div>
      </div>`;
  }
  window.c12s14Toggle = function(){ hasOutlier = !hasOutlier; render(); };
  render();
})();
</script>
""",
    15: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📚</span> Chapter 12 Master Data Summary Matrix
  </h3>
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs">
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-amber-300 mb-1">1. Mean Fulcrum & Data Changes</div>
      <div class="text-slate-300">LHS Distances = RHS Distances; adding +c shifts ±c; multiplying ×k scales ×k; Sum = Mean × n.</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-cyan-300 mb-1">2. Median, Frequencies & Spreadsheets</div>
      <div class="text-slate-300">Outlier-resistant Median; weighted mean Σ(fᵢxᵢ)/Σfᵢ; Calc/Excel =SUM(B3:G3) & =AVERAGE(B3:G3).</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-emerald-300 mb-1">3. 2-Step Line Graphs & Sleepy-Deepy</div>
      <div class="text-slate-300">Step 1: scales, axes, slopes; Step 2: peaks, troughs, trends; smooth curves across ages 6–75.</div>
    </div>
    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800">
      <div class="font-bold text-rose-300 mb-1">4. Infographics, 48-Block Strips & Hex</div>
      <div class="text-slate-300">Rice vs Wheat maps; 24-hr (48 × 30-min) routine strips; 11 × 11 Game of Hex (No-Tie Theorem).</div>
    </div>
  </div>
</div>
""",
    16: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>⬡</span> It's Puzzle Time! 11 × 11 Game of Hex
    </h3>
    <div class="flex items-center gap-2 text-xs">
      <span id="c12s16Turn" class="font-bold text-amber-300">Turn: Amber (Top ↔ Bottom)</span>
      <button type="button" onclick="c12s16Reset()" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">Reset 121 Grid</button>
    </div>
  </div>
  <svg id="c12s16Svg" viewBox="0 0 380 230" class="w-full bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c12s16Msg" class="text-xs text-slate-300">Amber connects <b>Top Edge ↔ Bottom Edge</b>; Cyan connects <b>Left Edge ↔ Right Edge</b>. Click any hexagon!</div>
</div>
<script>
(function(){
  const N = 11;
  let board = Array.from({length: N}, () => Array(N).fill(0));
  let turn = 1;
  let winner = 0;
  function checkWin(p){
    const vis = Array.from({length: N}, () => Array(N).fill(false));
    const q = [];
    for(let i = 0; i < N; i++){
      const r = p === 1 ? 0 : i, c = p === 1 ? i : 0;
      if(board[r][c] === p){ vis[r][c] = true; q.push([r, c]); }
    }
    const dirs = [[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0]];
    while(q.length){
      const [r, c] = q.shift();
      if((p === 1 && r === N - 1) || (p === 2 && c === N - 1)) return true;
      for(const [dr, dc] of dirs){
        const nr = r + dr, nc = c + dc;
        if(nr>=0 && nr<N && nc>=0 && nc<N && !vis[nr][nc] && board[nr][nc] === p){
          vis[nr][nc] = true;
          q.push([nr, nc]);
        }
      }
    }
    return false;
  }
  function render(){
    const svg = document.getElementById('c12s16Svg');
    if(!svg) return;
    const rad = 10.5, dx = rad * Math.sqrt(3), dy = rad * 1.5;
    let html = '';
    for(let r = 0; r < N; r++){
      for(let c = 0; c < N; c++){
        const cx = 30 + c * dx + r * (dx * 0.5);
        const cy = 28 + r * dy;
        const pts = [];
        for(let a = 0; a < 6; a++){
          const ang = (Math.PI / 180) * (60 * a - 30);
          pts.push((cx + rad * Math.cos(ang)).toFixed(1) + ',' + (cy + rad * Math.sin(ang)).toFixed(1));
        }
        const v = board[r][c];
        const fill = v === 1 ? '#f59e0b' : v === 2 ? '#22d3ee' : '#1e293b';
        const stroke = r === 0 || r === N - 1 ? '#f59e0b' : (c === 0 || c === N - 1 ? '#22d3ee' : '#475569');
        html += `<polygon points="${pts.join(' ')}" fill="${fill}" stroke="${stroke}" stroke-width="1.2" class="cursor-pointer" onclick="c12s16Play(${r},${c})"/>`;
      }
    }
    svg.innerHTML = html;
    const tEl = document.getElementById('c12s16Turn');
    if(winner){
      tEl.textContent = winner === 1 ? 'Amber Wins (Top↔Bottom Connected)!' : 'Cyan Wins (Left↔Right Connected)!';
      tEl.className = winner === 1 ? 'font-bold text-amber-300' : 'font-bold text-cyan-300';
    } else {
      tEl.textContent = turn === 1 ? 'Turn: Amber (Top ↔ Bottom)' : 'Turn: Cyan (Left ↔ Right)';
      tEl.className = turn === 1 ? 'font-bold text-amber-300' : 'font-bold text-cyan-300';
    }
  }
  window.c12s16Play = function(r, c){
    if(winner || board[r][c] !== 0) return;
    board[r][c] = turn;
    if(checkWin(turn)) winner = turn;
    else turn = turn === 1 ? 2 : 1;
    render();
  };
  window.c12s16Reset = function(){
    board = Array.from({length: N}, () => Array(N).fill(0));
    turn = 1; winner = 0; render();
  };
  render();
})();
</script>
"""
}
