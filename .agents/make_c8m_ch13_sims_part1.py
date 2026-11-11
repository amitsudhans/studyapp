#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive Simulators for NCERT Class 8 Maths Chapter 13: Algebra Play
Part 1: Simulators 1 to 8
"""

simulators_part1 = {
    1: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🧩</span> Universal Variable Blueprint Machine
  </h3>
  <div class="flex flex-wrap gap-1.5 text-xs">
    <button type="button" onclick="c13s1Mode(0)" id="c13s1b0" class="px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold">3x − 7</button>
    <button type="button" onclick="c13s1Mode(1)" id="c13s1b1" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">2(x + 4)</button>
    <button type="button" onclick="c13s1Mode(2)" id="c13s1b2" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700">x² + 2x + 1</button>
  </div>
  <div class="space-y-2 text-xs">
    <div class="flex justify-between text-slate-300">
      <span>Test Any Input Variable <b class="text-cyan-300">x</b>:</span>
      <span>x = <b id="c13s1Val" class="text-cyan-300 text-sm">5</b></span>
    </div>
    <input id="c13s1Sl" type="range" min="-5" max="25" step="1" value="5" oninput="c13s1Draw()" class="w-full accent-cyan-400">
    <svg id="c13s1Svg" viewBox="0 0 340 86" class="w-full h-24 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c13s1Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-300 leading-relaxed"></div>
  </div>
</div>
<script>
(function(){
  let mode = 0;
  const rules = [
    { expr: '3x − 7', words: 'Triple x, then subtract 7', fn: x => 3*x - 7, detail: x => `3(${x}) − 7 = ${3*x} − 7 = ${3*x-7}` },
    { expr: '2(x + 4)', words: 'Add 4 to x, then double (distributes to 2x + 8)', fn: x => 2*(x + 4), detail: x => `2(${x} + 4) = 2(${x+4}) = ${2*(x+4)}  [Also 2x + 8 = ${2*x} + 8]` },
    { expr: '(x + 1)²', words: 'Square (x + 1), identically x² + 2x + 1', fn: x => (x+1)*(x+1), detail: x => `(${x} + 1)² = ${x*x} + ${2*x} + 1 = ${(x+1)*(x+1)}` }
  ];
  window.c13s1Mode = function(m){
    mode = m;
    [0,1,2].forEach(i => {
      const b = document.getElementById('c13s1b'+i);
      if(b) b.className = i===m ? 'px-2.5 py-1 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-semibold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300 border border-slate-700';
    });
    window.c13s1Draw();
  };
  window.c13s1Draw = function(){
    const x = parseInt(document.getElementById('c13s1Sl').value, 10) || 0;
    document.getElementById('c13s1Val').textContent = x;
    const r = rules[mode];
    const y = r.fn(x);
    const svg = document.getElementById('c13s1Svg');
    if(svg){
      svg.innerHTML = `
        <rect x="14" y="20" width="66" height="44" rx="10" fill="#0f172a" stroke="#22d3ee" stroke-width="2"/>
        <text x="47" y="38" text-anchor="middle" fill="#94a3b8" font-size="9">INPUT x</text>
        <text x="47" y="55" text-anchor="middle" fill="#22d3ee" font-size="14" font-weight="bold">${x}</text>
        <line x1="80" y1="42" x2="108" y2="42" stroke="#64748b" stroke-width="2"/>
        <polygon points="108,37 116,42 108,47" fill="#fbbf24"/>
        <rect x="118" y="14" width="110" height="56" rx="12" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
        <text x="173" y="34" text-anchor="middle" fill="#fde68a" font-size="9">ALGEBRA RULE</text>
        <text x="173" y="53" text-anchor="middle" fill="#fbbf24" font-size="13" font-weight="bold">${r.expr}</text>
        <line x1="228" y1="42" x2="254" y2="42" stroke="#64748b" stroke-width="2"/>
        <polygon points="254,37 262,42 254,47" fill="#34d399"/>
        <rect x="264" y="20" width="64" height="44" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="2"/>
        <text x="296" y="38" text-anchor="middle" fill="#94a3b8" font-size="9">OUTPUT</text>
        <text x="296" y="55" text-anchor="middle" fill="#34d399" font-size="14" font-weight="bold">${y}</text>`;
    }
    document.getElementById('c13s1Out').innerHTML = `
      <div><b class="text-amber-300">Verbal Pattern:</b> ${r.words}</div>
      <div><b class="text-emerald-300">Instant Check at x = ${x}:</b> ${r.detail(x)}</div>`;
  };
  window.c13s1Draw();
})();
</script>
""",
    2: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>🪄</span> Think-of-a-Number Variable Canceller
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <div>
      <div class="flex justify-between text-slate-300 mb-1"><span>Secret x:</span><b id="c13s2XVal" class="text-cyan-300">19</b></div>
      <input id="c13s2X" type="range" min="1" max="100" value="19" oninput="c13s2Draw()" class="w-full accent-cyan-400">
    </div>
    <div>
      <div class="flex justify-between text-slate-300 mb-1"><span>Add Constant (2k):</span><b id="c13s2KVal" class="text-amber-300">4</b></div>
      <input id="c13s2K" type="range" min="2" max="20" step="2" value="4" oninput="c13s2Draw()" class="w-full accent-amber-400">
    </div>
  </div>
  <div id="c13s2Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  window.c13s2Draw = function(){
    const x = parseInt(document.getElementById('c13s2X').value, 10) || 1;
    const add = parseInt(document.getElementById('c13s2K').value, 10) || 4;
    const k = add / 2;
    document.getElementById('c13s2XVal').textContent = x;
    document.getElementById('c13s2KVal').textContent = add;
    const s2 = 2*x, s3 = 2*x + add, s4 = x + k, s5 = s4 - x;
    document.getElementById('c13s2Out').innerHTML = `
      <div class="grid grid-cols-2 gap-1 font-mono text-[11px] bg-slate-900/70 p-2 rounded-lg">
        <span class="text-slate-400">1. Pick secret number</span><span class="text-cyan-300">x = <b>${x}</b></span>
        <span class="text-slate-400">2. Double it</span><span class="text-slate-200">2x = <b>${s2}</b></span>
        <span class="text-slate-400">3. Add ${add}</span><span class="text-slate-200">2x + ${add} = <b>${s3}</b></span>
        <span class="text-slate-400">4. Divide by 2</span><span class="text-amber-300">x + ${k} = <b>${s4}</b></span>
        <span class="text-slate-400">5. Subtract secret x</span><span class="text-emerald-300">(x + ${k}) − x = <b>${s5}</b></span>
      </div>
      <div class="text-emerald-300 font-semibold pt-1">Proof: <span class="text-cyan-300">+x</span> and <span class="text-rose-300">−x</span> cancel to 0! Output ALWAYS locks at <b>${k}</b>!</div>`;
  };
  window.c13s2Draw();
})();
</script>
""",
    3: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🎂</span> 100M + 165 + D Birthday Decoder
  </h3>
  <div class="grid grid-cols-2 gap-2 text-xs">
    <div>
      <label class="text-slate-400 block mb-1">Birth Month (M: 1–12)</label>
      <input id="c13s3M" type="number" min="1" max="12" value="10" oninput="c13s3Draw()" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-cyan-300 font-bold">
    </div>
    <div>
      <label class="text-slate-400 block mb-1">Birth Day (D: 1–31)</label>
      <input id="c13s3D" type="number" min="1" max="31" value="24" oninput="c13s3Draw()" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-emerald-300 font-bold">
    </div>
  </div>
  <div id="c13s3Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  const months = ['','January','February','March','April','May','June','July','August','September','October','November','December'];
  window.c13s3Draw = function(){
    const m = Math.max(1, Math.min(12, parseInt(document.getElementById('c13s3M').value, 10) || 1));
    const d = Math.max(1, Math.min(31, parseInt(document.getElementById('c13s3D').value, 10) || 1));
    const a1 = m * 5, a2 = a1 + 6, a3 = a2 * 4, a4 = a3 + 9, a5 = a4 * 5, tot = a5 + d;
    const dec = tot - 165;
    const recM = Math.floor(dec / 100), recD = dec % 100;
    document.getElementById('c13s3Out').innerHTML = `
      <div class="text-slate-300">Pipeline: (${m}×5+6)×4+9 = <b>${a4}</b> → ×5 = <b>${a5}</b> → +${d} = <b class="text-amber-300 text-sm">${tot}</b></div>
      <div class="text-cyan-300">Algebra Form: 100(${m}) + 165 + ${d} = <b>${100*m} + 165 + ${d} = ${tot}</b></div>
      <div class="p-2 rounded-lg bg-slate-900 border border-emerald-500/30 text-emerald-300 font-semibold">
        Decode Step: ${tot} − 165 = <span class="text-white">${dec}</span> → Month <b>${recM} (${months[recM]})</b>, Day <b>${recD}</b>!
      </div>`;
  };
  window.c13s3Draw();
})();
</script>
""",
    4: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
      <span>🔺</span> Addition Pyramid Builder (3 & 4 Rows)
    </h3>
    <button type="button" onclick="c13s4Toggle()" id="c13s4Btn" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 text-xs border border-slate-700">Switch to 4-Row (a,b,c,d)</button>
  </div>
  <div class="grid grid-cols-4 gap-2 text-xs">
    <div><span class="text-slate-400">a</span><input id="c13s4a" type="number" value="4" oninput="c13s4Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-cyan-300"></div>
    <div><span class="text-slate-400">b</span><input id="c13s4b" type="number" value="7" oninput="c13s4Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-amber-300"></div>
    <div><span class="text-slate-400">c</span><input id="c13s4c" type="number" value="2" oninput="c13s4Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-emerald-300"></div>
    <div id="c13s4dWrap" class="hidden"><span class="text-slate-400">d</span><input id="c13s4d" type="number" value="5" oninput="c13s4Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-rose-300"></div>
  </div>
  <svg id="c13s4Svg" viewBox="0 0 340 135" class="w-full h-36 bg-slate-950 rounded-xl border border-slate-800"></svg>
  <div id="c13s4Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  let rows = 3;
  function box(x,y,w,h,val,stroke,txt='#e2e8f0'){
    return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="6" fill="#0f172a" stroke="${stroke}" stroke-width="1.8"/><text x="${x+w/2}" y="${y+h/2+4}" text-anchor="middle" fill="${txt}" font-size="12" font-weight="bold">${val}</text>`;
  }
  window.c13s4Toggle = function(){
    rows = rows === 3 ? 4 : 3;
    document.getElementById('c13s4dWrap').classList.toggle('hidden', rows===3);
    document.getElementById('c13s4Btn').textContent = rows===3 ? 'Switch to 4-Row (a,b,c,d)' : 'Switch to 3-Row (a,b,c)';
    window.c13s4Draw();
  };
  window.c13s4Draw = function(){
    const a = parseInt(document.getElementById('c13s4a').value,10)||0;
    const b = parseInt(document.getElementById('c13s4b').value,10)||0;
    const c = parseInt(document.getElementById('c13s4c').value,10)||0;
    const d = parseInt(document.getElementById('c13s4d').value,10)||0;
    const svg = document.getElementById('c13s4Svg');
    if(rows===3){
      const m1=a+b, m2=b+c, top=m1+m2;
      if(svg) svg.innerHTML =
        box(135,12,70,30,top,'#34d399','#34d399') +
        box(95,50,70,30,m1,'#fbbf24','#fde68a') + box(175,50,70,30,m2,'#fbbf24','#fde68a') +
        box(55,88,70,30,a,'#22d3ee') + box(135,88,70,30,b,'#22d3ee') + box(215,88,70,30,c,'#22d3ee');
      document.getElementById('c13s4Out').innerHTML = `Algebraic Law: <b class="text-emerald-300">a + 2b + c</b> = ${a} + 2(${b}) + ${c} = <b class="text-white">${top}</b>`;
    } else {
      const r2=[a+b,b+c,c+d], r3=[r2[0]+r2[1], r2[1]+r2[2]], top=r3[0]+r3[1];
      if(svg) svg.innerHTML =
        box(142,6,56,24,top,'#34d399','#34d399') +
        box(110,36,56,24,r3[0],'#fbbf24') + box(174,36,56,24,r3[1],'#fbbf24') +
        box(78,66,56,24,r2[0],'#38bdf8') + box(142,66,56,24,r2[1],'#38bdf8') + box(206,66,56,24,r2[2],'#38bdf8') +
        box(46,96,56,24,a,'#22d3ee') + box(110,96,56,24,b,'#22d3ee') + box(174,96,56,24,c,'#22d3ee') + box(238,96,56,24,d,'#22d3ee');
      document.getElementById('c13s4Out').innerHTML = `4-Row Law: <b class="text-emerald-300">a + 3b + 3c + d</b> = ${a} + 3(${b}) + 3(${c}) + ${d} = <b class="text-white">${top}</b>`;
    }
  };
  window.c13s4Draw();
})();
</script>
""",
    5: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
    <span>🔎</span> Missing-Brick Linear Equation Solver
  </h3>
  <div class="grid grid-cols-3 gap-2 text-xs">
    <div><span class="text-slate-400">Left Base (a)</span><input id="c13s5a" type="number" value="5" oninput="c13s5Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-cyan-300"></div>
    <div><span class="text-slate-400">Right Base (c)</span><input id="c13s5c" type="number" value="9" oninput="c13s5Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-cyan-300"></div>
    <div><span class="text-slate-400">Top Peak (T)</span><input id="c13s5t" type="number" value="34" oninput="c13s5Draw()" class="w-full bg-slate-950 border border-slate-700 rounded px-2 py-1 text-emerald-300"></div>
  </div>
  <div id="c13s5Out" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1.5"></div>
</div>
<script>
(function(){
  window.c13s5Draw = function(){
    const a = parseInt(document.getElementById('c13s5a').value,10)||0;
    const c = parseInt(document.getElementById('c13s5c').value,10)||0;
    const T = parseInt(document.getElementById('c13s5t').value,10)||0;
    const rhs = T - a - c;
    const x = rhs / 2;
    const m1 = a + x, m2 = x + c;
    const fmt = v => Number.isInteger(v) ? v : v.toFixed(1);
    document.getElementById('c13s5Out').innerHTML = `
      <div>Equation: <b class="text-amber-300">${a} + 2x + ${c} = ${T}</b> → 2x + ${a+c} = ${T} → 2x = ${rhs}</div>
      <div class="text-emerald-300 font-bold text-sm">Solved Unknown Base Brick: x = ${fmt(x)}</div>
      <div class="text-slate-300">Verify Upward: Middle bricks = [${fmt(m1)}, ${fmt(m2)}] → Top = ${fmt(m1)} + ${fmt(m2)} = <b class="text-white">${fmt(m1+m2)}</b> ✓</div>`;
  };
  window.c13s5Draw();
})();
</script>
""",
    6: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-emerald-300 flex items-center gap-2">
    <span>🐚</span> Virahāṅka-Fibonacci Pyramid Generator
  </h3>
  <div class="space-y-2 text-xs">
    <div class="flex justify-between text-slate-300"><span>Start Index along [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]:</span><b id="c13s6Idx" class="text-amber-300">Term #1 (Base starts at 1)</b></div>
    <input id="c13s6Sl" type="range" min="0" max="4" value="0" oninput="c13s6Draw()" class="w-full accent-emerald-400">
    <svg id="c13s6Svg" viewBox="0 0 340 120" class="w-full h-32 bg-slate-950 rounded-xl border border-slate-800"></svg>
    <div id="c13s6Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-300"></div>
  </div>
</div>
<script>
(function(){
  const vf = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144];
  function cell(x,y,v,col){
    return `<rect x="${x}" y="${y}" width="58" height="22" rx="5" fill="#0f172a" stroke="${col}" stroke-width="1.6"/><text x="${x+29}" y="${y+15}" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="bold">${v}</text>`;
  }
  window.c13s6Draw = function(){
    const k = parseInt(document.getElementById('c13s6Sl').value, 10)||0;
    const b = [vf[k], vf[k+1], vf[k+2], vf[k+3]];
    const r2 = [b[0]+b[1], b[1]+b[2], b[2]+b[3]];
    const r3 = [r2[0]+r2[1], r2[1]+r2[2]];
    const top = r3[0]+r3[1];
    document.getElementById('c13s6Idx').textContent = `Base [${b.join(', ')}]`;
    const svg = document.getElementById('c13s6Svg');
    if(svg) svg.innerHTML =
      cell(141,6,top,'#34d399') +
      cell(109,34,r3[0],'#fbbf24') + cell(173,34,r3[1],'#fbbf24') +
      cell(77,62,r2[0],'#38bdf8') + cell(141,62,r2[1],'#38bdf8') + cell(205,62,r2[2],'#38bdf8') +
      cell(45,90,b[0],'#22d3ee') + cell(109,90,b[1],'#22d3ee') + cell(173,90,b[2],'#22d3ee') + cell(237,90,b[3],'#22d3ee');
    document.getElementById('c13s6Out').innerHTML = `Every upward row produces the exact next Virahāṅka-Fibonacci terms! Top Peak = <b class="text-emerald-300">${top}</b> = ${b[0]} + 3(${b[1]}) + 3(${b[2]}) + ${b[3]}`;
  };
  window.c13s6Draw();
})();
</script>
""",
    7: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <h3 class="text-sm sm:text-base font-bold text-cyan-300 flex items-center gap-2">
    <span>📅</span> Monthly 2×2 Calendar Grid Magic (4a + 16 = S)
  </h3>
  <div id="c13s7Grid" class="grid grid-cols-7 gap-1 text-center text-[11px] font-mono bg-slate-950 p-2.5 rounded-xl border border-slate-800"></div>
  <div id="c13s7Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs space-y-1"></div>
</div>
<script>
(function(){
  let topLeft = 9;
  window.c13s7Pick = function(d){
    const col = (d - 1) % 7;
    if(col === 6) d -= 1;
    if(d + 8 > 31) d = Math.max(1, d - 7);
    topLeft = d;
    render();
  };
  function render(){
    const box = new Set([topLeft, topLeft+1, topLeft+7, topLeft+8]);
    let html = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].map(w=>`<div class="text-slate-500 font-bold pb-1">${w}</div>`).join('');
    for(let d=1; d<=31; d++){
      const hi = box.has(d);
      html += `<button type="button" onclick="c13s7Pick(${d})" class="py-1 rounded ${hi?'bg-amber-500/30 text-amber-200 border border-amber-400 font-bold':'bg-slate-900 text-slate-300 hover:bg-slate-800'}">${d}</button>`;
    }
    document.getElementById('c13s7Grid').innerHTML = html;
    const S = 4*topLeft + 16;
    document.getElementById('c13s7Out').innerHTML = `
      <div>2×2 Box: <b class="text-amber-300">[${topLeft}, ${topLeft+1}] & [${topLeft+7}, ${topLeft+8}]</b> → Sum S = <b>${S}</b></div>
      <div class="text-emerald-300">Decode: a = (${S} − 16) ÷ 4 = <b>${topLeft}</b> &nbsp;|&nbsp; Equal Diagonals: ${topLeft}+${topLeft+8} = ${topLeft+1}+${topLeft+7} = <b>${2*topLeft+8}</b></div>`;
  }
  render();
})();
</script>
""",
    8: """
<div class="bg-slate-900/90 border border-slate-700/80 rounded-2xl p-4 sm:p-5 shadow-2xl space-y-3">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <h3 class="text-sm sm:text-base font-bold text-amber-300 flex items-center gap-2">
      <span>🔷</span> Picture-Symbol Algebra Grid Solver
    </h3>
    <button type="button" onclick="c13s8Cycle()" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300 text-xs border border-slate-700">New Grid Puzzle</button>
  </div>
  <div class="grid grid-cols-4 gap-1.5 text-center text-xs bg-slate-950 p-3 rounded-xl border border-slate-800" id="c13s8Grid"></div>
  <div class="flex gap-2 text-xs">
    <button type="button" onclick="c13s8Reveal()" class="px-3 py-1 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-semibold">Solve Step-by-Step</button>
  </div>
  <div id="c13s8Out" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300"></div>
</div>
<script>
(function(){
  const puzzles = [
    { t: 8, s: 6, c: 9 },
    { t: 7, s: 11, c: 5 },
    { t: 12, s: 4, c: 10 }
  ];
  let idx = 0, step = 0;
  function render(){
    const p = puzzles[idx];
    const r1 = 3*p.t, r2 = p.t + 2*p.s, r3 = p.s + 2*p.c;
    const c1 = p.t + p.t + p.s, c2 = p.t + p.s + p.c, c3 = p.t + p.s + p.c;
    const cell = (sym, col) => `<div class="py-1.5 rounded bg-slate-900 ${col} text-sm">${sym}</div>`;
    const sumCell = v => `<div class="py-1.5 rounded bg-slate-800 text-amber-300 font-bold">${v}</div>`;
    document.getElementById('c13s8Grid').innerHTML =
      cell('△','text-cyan-300') + cell('△','text-cyan-300') + cell('△','text-cyan-300') + sumCell('= '+r1) +
      cell('△','text-cyan-300') + cell('□','text-emerald-300') + cell('□','text-emerald-300') + sumCell('= '+r2) +
      cell('□','text-emerald-300') + cell('○','text-rose-300') + cell('○','text-rose-300') + sumCell('= '+r3) +
      sumCell('↓ '+c1) + sumCell('↓ '+c2) + sumCell('↓ '+c3) + `<div class="py-1.5 text-slate-500">Sums</div>`;
    const lines = [
      `Step 1 (Row 1): 3△ = ${r1} → <b class="text-cyan-300">△ = ${p.t}</b>`,
      `Step 2 (Row 2): ${p.t} + 2□ = ${r2} → 2□ = ${r2-p.t} → <b class="text-emerald-300">□ = ${p.s}</b>`,
      `Step 3 (Row 3): ${p.s} + 2○ = ${r3} → 2○ = ${r3-p.s} → <b class="text-rose-300">○ = ${p.c}</b> ✓`
    ];
    document.getElementById('c13s8Out').innerHTML = step===0 ? 'Click <b>Solve Step-by-Step</b> to unlock △, □, ○!' : lines.slice(0, step).join('<br>');
  }
  window.c13s8Reveal = function(){ step = step >= 3 ? 1 : step + 1; render(); };
  window.c13s8Cycle = function(){ idx = (idx+1)%puzzles.length; step = 0; render(); };
  render();
})();
</script>
"""
}
