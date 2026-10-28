# -*- coding: utf-8 -*-
"""
Interactive SVG Simulators for NCERT Class 7 Mathematics - Chapter 1: Large Numbers Around Us
Simulators 1 to 16
"""

SIMULATORS_JS = r"""
    // ==========================================
    // 16 BESPOKE INTERACTIVE SVG SIMULATORS (Ch 1)
    // ==========================================

    // Slide 1: Rice Varieties & Large Number Visualizer
    function simRiceVarietiesScale() {
      simHeaderTitle.textContent = "A Lakh Varieties of Rice: Lifetime Consumption Simulator";
      let dailyBowls = 1;

      simCanvas.innerHTML = `
        <svg id="riceSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <defs>
            <radialGradient id="riceBgGrad" cx="50%" cy="50%" r="75%">
              <stop offset="0%" stop-color="#0f291e"/>
              <stop offset="100%" stop-color="#02140d"/>
            </radialGradient>
            <radialGradient id="bowlGrad" cx="50%" cy="40%" r="60%">
              <stop offset="0%" stop-color="#fef08a"/>
              <stop offset="70%" stop-color="#eab308"/>
              <stop offset="100%" stop-color="#854d0e"/>
            </radialGradient>
          </defs>

          <rect x="0" y="0" width="540" height="330" fill="url(#riceBgGrad)"/>

          <!-- Golden Rice Field & Granary Graphic -->
          <g transform="translate(30, 30)">
            <rect x="0" y="0" width="230" height="260" rx="12" fill="rgba(6, 78, 59, 0.4)" stroke="#10b981" stroke-width="1.5"/>
            <text x="115" y="24" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">India's Traditional Rice Heritage</text>
            <line x1="12" y1="32" x2="218" y2="32" stroke="rgba(52, 211, 153, 0.3)"/>

            <!-- Rice Stalks & Grains Array -->
            <g id="riceGrainsGroup" transform="translate(15, 45)">
              <!-- Visual cluster of rice varieties -->
              <text x="10" y="20" font-size="20">🌾</text>
              <text x="60" y="20" font-size="20">🌾</text>
              <text x="110" y="20" font-size="20">🌾</text>
              <text x="160" y="20" font-size="20">🌾</text>

              <text x="20" y="55" fill="#fde047" font-size="9" font-weight="700">Basmati (Aromatic)</text>
              <text x="115" y="55" fill="#fde047" font-size="9" font-weight="700">Navara (Medicinal)</text>

              <text x="10" y="85" font-size="20">🌾</text>
              <text x="60" y="85" font-size="20">🌾</text>
              <text x="110" y="85" font-size="20">🌾</text>
              <text x="160" y="85" font-size="20">🌾</text>

              <text x="20" y="120" fill="#fde047" font-size="9" font-weight="700">Gobindobhog (Sweet)</text>
              <text x="115" y="120" fill="#fde047" font-size="9" font-weight="700">Kalanamak (Buddha Rice)</text>

              <rect x="10" y="135" width="180" height="70" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1"/>
              <text x="100" y="155" fill="#38bdf8" font-size="10" font-weight="800" text-anchor="middle">Total Indigenous Varieties</text>
              <text x="100" y="180" fill="#f8fafc" font-size="16" font-weight="900" text-anchor="middle">1,00,000</text>
              <text x="100" y="196" fill="#4ade80" font-size="9" font-weight="700" text-anchor="middle">ONE LAKH VARIETIES</text>
            </g>
          </g>

          <!-- Interactive Calculation Card -->
          <g transform="translate(280, 30)">
            <rect x="0" y="0" width="230" height="260" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#fbbf24" stroke-width="1.5"/>
            <text x="115" y="24" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">Tasting All Varieties Timeline</text>
            <line x1="12" y1="32" x2="218" y2="32" stroke="rgba(251, 191, 36, 0.3)"/>

            <text x="15" y="55" fill="#94a3b8" font-size="9.5">Consumption Rate:</text>
            <text id="lblRateText" x="15" y="72" fill="#38bdf8" font-size="10" font-weight="700">1 new variety per day (365/yr)</text>

            <text x="15" y="100" fill="#94a3b8" font-size="9.5">In 10 Years Tasted:</text>
            <text id="lblTenYears" x="15" y="116" fill="#f8fafc" font-size="10" font-weight="700">3,650 varieties (3.65%)</text>

            <text x="15" y="142" fill="#94a3b8" font-size="9.5">In 80-Year Lifetime Tasted:</text>
            <text id="lblLifetime" x="15" y="158" fill="#4ade80" font-size="10" font-weight="700">29,200 varieties (29.2%)</text>

            <text x="15" y="184" fill="#94a3b8" font-size="9.5">Time to Taste All 1 Lakh:</text>
            <text id="lblTotalTime" x="15" y="204" fill="#f59e0b" font-size="14" font-weight="900">273.97 Years!</text>

            <rect x="10" y="218" width="210" height="32" rx="6" fill="rgba(245, 158, 11, 0.15)" stroke="#f59e0b" stroke-width="1"/>
            <text id="lblTipText" x="115" y="238" fill="#fde047" font-size="8" font-weight="700" text-anchor="middle">Requires nearly 3 full human lifespans!</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Tasting Rate:</span>
          <button class="sim-btn active" id="btnRate1">1 variety / day</button>
          <button class="sim-btn" id="btnRate2">2 varieties / day</button>
          <button class="sim-btn" id="btnRate3">3 varieties / day</button>
          <button class="sim-btn" id="btnRate5">5 varieties / day</button>
        </div>
      `;

      function updateRate(rate) {
        dailyBowls = rate;
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));

        const perYear = rate * 365;
        const in10 = perYear * 10;
        const in80 = perYear * 80;
        const yearsTo1Lakh = (100000 / perYear).toFixed(1);

        document.getElementById('lblRateText').textContent = `${rate} new variety/day (${perYear.toLocaleString()}/yr)`;
        document.getElementById('lblTenYears').textContent = `${in10.toLocaleString()} varieties (${((in10/100000)*100).toFixed(1)}%)`;
        document.getElementById('lblLifetime').textContent = `${in80.toLocaleString()} varieties (${((in80/100000)*100).toFixed(1)}%)`;
        document.getElementById('lblTotalTime').textContent = `${yearsTo1Lakh} Years!`;

        const tip = document.getElementById('lblTipText');
        if (rate === 1) tip.textContent = "Requires nearly 3 full human lifespans!";
        else if (rate === 2) tip.textContent = "Even at 2 a day, it takes over 136 years!";
        else if (rate === 3) tip.textContent = "At 3 a day, it takes over 91 years!";
        else tip.textContent = "At 5 a day, it still takes nearly 55 continuous years!";
        sfx.playClick();
      }

      document.getElementById('btnRate1').addEventListener('click', (e) => { e.target.classList.add('active'); updateRate(1); });
      document.getElementById('btnRate2').addEventListener('click', (e) => { e.target.classList.add('active'); updateRate(2); });
      document.getElementById('btnRate3').addEventListener('click', (e) => { e.target.classList.add('active'); updateRate(3); });
      document.getElementById('btnRate5').addEventListener('click', (e) => { e.target.classList.add('active'); updateRate(5); });
    }

    // Slide 2: Comparative Height & Scale Explorer
    function simHeightMeasurementScale() {
      simHeaderTitle.textContent = "Vertical Monument Scale: Human Stacking Explorer";

      const landmarks = {
        human: { name: "1-Metre Student", height: 1, color: "#38bdf8", desc: "Fundamental Baseline Unit" },
        qutub: { name: "Qutub Minar (Delhi)", height: 73, color: "#f97316", desc: "73 stacked students" },
        statue: { name: "Statue of Unity (Gujarat)", height: 180, color: "#fbbf24", desc: "180 stacked students (World's Tallest)" },
        kunchikal: { name: "Kunchikal Falls (Karnataka)", height: 450, color: "#06b6d4", desc: "450 stacked students (Highest Waterfall)" },
        burj: { name: "Burj Khalifa (Dubai)", height: 828, color: "#a855f7", desc: "828 stacked students (Tallest Building)" },
        everest: { name: "Mount Everest", height: 8848, color: "#ec4899", desc: "8,848 stacked students (Earth's Summit)" },
        lakhChain: { name: "1 Lakh Students Line", height: 100000, color: "#10b981", desc: "1,00,000 m = 100 km (Reaches Space!)" }
      };

      simCanvas.innerHTML = `
        <svg id="heightSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#030712"/>

          <!-- Sky & Horizon Line at Bottom -->
          <line x1="20" y1="280" x2="520" y2="280" stroke="#334155" stroke-width="2"/>
          <text x="270" y="300" fill="#64748b" font-size="9" font-weight="700" text-anchor="middle">Ground Baseline (0 Metres)</text>

          <!-- Monument Comparison Bars -->
          <!-- 1m Human -->
          <g transform="translate(60, 275)">
            <line x1="0" y1="0" x2="0" y2="-5" stroke="#38bdf8" stroke-width="3"/>
            <text x="0" y="-12" fill="#38bdf8" font-size="8" text-anchor="middle">1 m</text>
            <text x="0" y="16" fill="#94a3b8" font-size="8" text-anchor="middle">Human</text>
          </g>

          <!-- Qutub Minar 73m -->
          <g transform="translate(130, 280)">
            <rect x="-8" y="-45" width="16" height="45" fill="#f97316" rx="2"/>
            <text x="0" y="-52" fill="#f97316" font-size="8" font-weight="700" text-anchor="middle">73 m</text>
            <text x="0" y="16" fill="#94a3b8" font-size="8" text-anchor="middle">Qutub</text>
          </g>

          <!-- Statue of Unity 180m -->
          <g transform="translate(210, 280)">
            <rect x="-10" y="-95" width="20" height="95" fill="#fbbf24" rx="2"/>
            <text x="0" y="-102" fill="#fbbf24" font-size="8.5" font-weight="800" text-anchor="middle">180 m</text>
            <text x="0" y="16" fill="#94a3b8" font-size="8" text-anchor="middle">Unity</text>
          </g>

          <!-- Kunchikal Falls 450m -->
          <g transform="translate(290, 280)">
            <rect x="-12" y="-170" width="24" height="170" fill="#06b6d4" rx="2"/>
            <text x="0" y="-178" fill="#06b6d4" font-size="8.5" font-weight="800" text-anchor="middle">450 m</text>
            <text x="0" y="16" fill="#94a3b8" font-size="8" text-anchor="middle">Kunchikal</text>
          </g>

          <!-- Burj Khalifa 828m -->
          <g transform="translate(370, 280)">
            <rect x="-14" y="-245" width="28" height="245" fill="#a855f7" rx="3"/>
            <polygon points="-14,-245 0,-265 14,-245" fill="#c084fc"/>
            <text x="0" y="-270" fill="#a855f7" font-size="9" font-weight="900" text-anchor="middle">828 m</text>
            <text x="0" y="16" fill="#94a3b8" font-size="8" text-anchor="middle">Burj</text>
          </g>

          <!-- 1 Lakh Students Callout (100 km) -->
          <g transform="translate(425, 30)">
            <rect x="0" y="0" width="105" height="150" rx="8" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="1.5"/>
            <text x="52" y="20" fill="#34d399" font-size="9" font-weight="800" text-anchor="middle">1 Lakh Students</text>
            <line x1="8" y1="26" x2="97" y2="26" stroke="rgba(52, 211, 153, 0.3)"/>
            <text x="8" y="44" fill="#f8fafc" font-size="8.5">• 1,00,000 metres</text>
            <text x="8" y="62" fill="#38bdf8" font-size="8.5">• = 100 km long!</text>
            <text x="8" y="80" fill="#cbd5e1" font-size="8">• 11× Mount Everest</text>
            <text x="8" y="98" fill="#fde047" font-size="8">• Crosses Karman</text>
            <text x="8" y="112" fill="#fde047" font-size="8">  Line into space!</text>
            <rect x="6" y="122" width="93" height="20" rx="3" fill="rgba(16, 185, 129, 0.3)"/>
            <text x="52" y="136" fill="#a7f3d0" font-size="7.5" font-weight="800" text-anchor="middle">REACHES SPACE</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.4rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Inspect Monument:</span>
          <button class="sim-btn" id="btnHUnity">Statue of Unity (180m)</button>
          <button class="sim-btn" id="btnHKunchikal">Kunchikal Falls (450m)</button>
          <button class="sim-btn" id="btnHBurj">Burj Khalifa (828m)</button>
          <button class="sim-btn active" id="btnHLakh">1 Lakh People (100 km)</button>
        </div>
      `;

      document.getElementById('btnHUnity').addEventListener('click', () => sfx.playClick());
      document.getElementById('btnHKunchikal').addEventListener('click', () => sfx.playClick());
      document.getElementById('btnHBurj').addEventListener('click', () => sfx.playClick());
      document.getElementById('btnHLakh').addEventListener('click', () => sfx.playCorrect());
    }

    // Slide 3: Is One Lakh Big or Small? Contextual Comparison
    function simIsOneLakhBig() {
      simHeaderTitle.textContent = "Is 1 Lakh Big or Small? Contextual Perspective Explorer";

      simCanvas.innerHTML = `
        <svg id="oneLakhContextSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#020617"/>

          <!-- Dynamic Context Graphics Group -->
          <g id="lakhContextDisplayGroup">
            <!-- Populated via script -->
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnCtxStadium">🏟️ Context 1: Cricket Stadium (GIGANTIC)</button>
          <button class="sim-btn" id="btnCtxHair">🧑 Context 2: Human Scalp Hair (ORDINARY)</button>
          <button class="sim-btn" id="btnCtxFish">🐟 Context 3: Fish Spawning Eggs (TINY)</button>
        </div>
      `;

      function renderContext(ctx) {
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        const g = document.getElementById('lakhContextDisplayGroup');

        if (ctx === 'stadium') {
          document.getElementById('btnCtxStadium').classList.add('active');
          g.innerHTML = `
            <text x="270" y="30" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Scenario A: Narendra Modi Stadium (Capacity: 1,32,000)</text>
            
            <!-- Stadium Oval Illustration -->
            <ellipse cx="270" cy="140" rx="190" ry="85" fill="#065f46" stroke="#10b981" stroke-width="3"/>
            <ellipse cx="270" cy="140" rx="120" ry="50" fill="#047857"/>
            <rect x="260" y="130" width="20" height="20" fill="#fde047" rx="2"/>
            <text x="270" y="144" fill="#78350f" font-size="8" font-weight="900" text-anchor="middle">Pitch</text>

            <!-- Crowd speckles -->
            <g opacity="0.7">
              <circle cx="120" cy="140" r="3" fill="#f8fafc"/>
              <circle cx="150" cy="110" r="3" fill="#fde047"/>
              <circle cx="200" cy="80" r="3" fill="#38bdf8"/>
              <circle cx="340" cy="80" r="3" fill="#f8fafc"/>
              <circle cx="390" cy="110" r="3" fill="#fde047"/>
              <circle cx="420" cy="140" r="3" fill="#38bdf8"/>
              <circle cx="380" cy="180" r="3" fill="#f8fafc"/>
              <circle cx="160" cy="180" r="3" fill="#fde047"/>
            </g>

            <rect x="50" y="245" width="440" height="60" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.2"/>
            <text x="270" y="268" fill="#f8fafc" font-size="10.5" font-weight="700" text-anchor="middle">Here, 1 Lakh represents an ENORMOUS, deafening sea of humanity!</text>
            <text x="270" y="288" fill="#4ade80" font-size="9" text-anchor="middle">Largest sports venue on Earth — filling it requires the entire population of a whole town.</text>
          `;
        } else if (ctx === 'hair') {
          document.getElementById('btnCtxHair').classList.add('active');
          g.innerHTML = `
            <text x="270" y="30" fill="#fbbf24" font-size="13" font-weight="800" text-anchor="middle">Scenario B: Strands of Hair on a Human Head (1,00,000 to 1,50,000)</text>
            
            <!-- Human Head Profile with Hair Follicles -->
            <g transform="translate(200, 60)">
              <circle cx="70" cy="80" r="60" fill="#fed7aa"/>
              <!-- Hair array -->
              <path d="M 10,70 Q 20,10 70,15 Q 120,10 130,70 Q 140,40 100,5 Q 50,0 5,50 Z" fill="#1e293b"/>
              <path d="M 20,40 Q 70,-10 120,40" stroke="#334155" stroke-width="4" fill="none"/>
              <text x="70" y="90" font-size="16">🙂</text>
            </g>

            <rect x="50" y="245" width="440" height="60" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#fbbf24" stroke-width="1.2"/>
            <text x="270" y="268" fill="#f8fafc" font-size="10.5" font-weight="700" text-anchor="middle">Here, 1 Lakh is ORDINARY and compact enough to fit on your own head!</text>
            <text x="270" y="288" fill="#fde047" font-size="9" text-anchor="middle">Because each strand is only 0.07 mm thick, 1,00,000 strands nestle comfortably in your hand.</text>
          `;
        } else if (ctx === 'fish') {
          document.getElementById('btnCtxFish').classList.add('active');
          g.innerHTML = `
            <text x="270" y="30" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Scenario C: Female Codfish Spawning Clutch (40,00,000 Eggs)</text>
            
            <!-- Underwater Scene with Fish and Millions of Eggs -->
            <rect x="50" y="60" width="440" height="165" rx="10" fill="#0c4a6e" opacity="0.6"/>
            <text x="140" y="140" font-size="32">🐟</text>

            <!-- Egg cloud -->
            <g transform="translate(220, 80)">
              <circle cx="20" cy="30" r="3" fill="#fed7aa" opacity="0.8"/>
              <circle cx="35" cy="45" r="2.5" fill="#fed7aa" opacity="0.8"/>
              <circle cx="50" cy="25" r="3" fill="#fed7aa" opacity="0.8"/>
              <circle cx="70" cy="40" r="2.5" fill="#fed7aa" opacity="0.8"/>
              <circle cx="90" cy="30" r="3" fill="#fed7aa" opacity="0.8"/>
              <circle cx="110" cy="50" r="2.5" fill="#fed7aa" opacity="0.8"/>
              <circle cx="130" cy="35" r="3" fill="#fed7aa" opacity="0.8"/>
              <text x="75" y="80" fill="#bae6fd" font-size="10" font-weight="700" text-anchor="middle">40,00,000 Eggs (40 Lakhs!)</text>
            </g>

            <rect x="50" y="245" width="440" height="60" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.2"/>
            <text x="270" y="268" fill="#f8fafc" font-size="10.5" font-weight="700" text-anchor="middle">Here, 1 Lakh is a TINY, negligible drop in the ocean!</text>
            <text x="270" y="288" fill="#38bdf8" font-size="9" text-anchor="middle">One lakh eggs represents merely 2.5% of what a single codfish releases in one season.</text>
          `;
        }
        sfx.playClick();
      }

      document.getElementById('btnCtxStadium').addEventListener('click', () => renderContext('stadium'));
      document.getElementById('btnCtxHair').addEventListener('click', () => renderContext('hair'));
      document.getElementById('btnCtxFish').addEventListener('click', () => renderContext('fish'));

      renderContext('stadium');
    }

    // Slide 4: Indian Place Value Chart & Comma Placement
    function simIndianPlaceValue() {
      simHeaderTitle.textContent = "Indian Place Value Chart & 3-2-2 Comma Grouping Tool";
      let currentNum = 458926;

      simCanvas.innerHTML = `
        <svg id="placeValueSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

          <!-- Period Header Banners (3-2-2) -->
          <!-- Crores Period (col 1-2) -->
          <rect x="25" y="25" width="115" height="28" rx="4" fill="#7c2d12"/>
          <text x="82" y="43" fill="#fed7aa" font-size="10" font-weight="800" text-anchor="middle">Crores Period</text>

          <!-- Lakhs Period (col 3-4) -->
          <rect x="145" y="25" width="115" height="28" rx="4" fill="#065f46"/>
          <text x="202" y="43" fill="#a7f3d0" font-size="10" font-weight="800" text-anchor="middle">Lakhs Period</text>

          <!-- Thousands Period (col 5-6) -->
          <rect x="265" y="25" width="115" height="28" rx="4" fill="#0369a1"/>
          <text x="322" y="43" fill="#bae6fd" font-size="10" font-weight="800" text-anchor="middle">Thousands Period</text>

          <!-- Ones Period (col 7-9) -->
          <rect x="385" y="25" width="130" height="28" rx="4" fill="#4338ca"/>
          <text x="450" y="43" fill="#c7d2fe" font-size="10" font-weight="800" text-anchor="middle">Ones Period (3 Digits)</text>

          <!-- Grid Columns for 8 Places: TC, C, TL, L, TTh, Th, H, T, O -->
          <g id="placeValueGrid">
            <!-- Dynamically populated -->
          </g>

          <!-- Standard Numeral Display with Commas -->
          <g transform="translate(40, 150)">
            <rect x="0" y="0" width="460" height="65" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="20" y="24" fill="#94a3b8" font-size="10" font-weight="700">Standard Indian Numeral:</text>
            <text id="lblIndianFormatted" x="20" y="52" fill="#38bdf8" font-size="20" font-weight="900">4,58,926</text>
          </g>

          <!-- Number in Words -->
          <g transform="translate(40, 230)">
            <rect x="0" y="0" width="460" height="75" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#fbbf24" stroke-width="1.2"/>
            <text x="20" y="22" fill="#fbbf24" font-size="10" font-weight="800">Read in Words:</text>
            <text id="lblNumberInWords" x="20" y="44" fill="#f8fafc" font-size="11" font-weight="700">Four lakh fifty-eight thousand nine hundred twenty-six</text>
            <text id="lblExpandedForm" x="20" y="64" fill="#4ade80" font-size="9">4×10⁵ + 5×10⁴ + 8×10³ + 9×10² + 2×10¹ + 6×10⁰</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnNum1">4,58,926</button>
          <button class="sim-btn" id="btnNum2">6,04,020</button>
          <button class="sim-btn" id="btnNum3">2,45,80,000</button>
          <button class="sim-btn" id="btnNum4">1,00,00,000 (1 Cr)</button>
        </div>
      `;

      function renderNumber(num, words, expanded) {
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        
        // Format with Indian commas
        const str = num.toString();
        let last3 = str.slice(-3);
        let rest = str.slice(0, -3);
        if (rest !== '') last3 = ',' + last3;
        const formatted = rest.replace(/\B(?=(\d{2})+(?!\d))/g, ",") + last3;

        document.getElementById('lblIndianFormatted').textContent = formatted;
        document.getElementById('lblNumberInWords').textContent = words;
        document.getElementById('lblExpandedForm').textContent = expanded;

        // Render grid cells
        const g = document.getElementById('placeValueGrid');
        g.innerHTML = '';
        const places = ["TC (10⁷)", "C (10⁷)", "TL (10⁶)", "L (10⁵)", "TTh (10⁴)", "Th (10³)", "H (10²)", "T (10¹)", "O (10⁰)"];
        const padded = str.padStart(9, '0');

        for (let i = 0; i < 9; i++) {
          const x = 25 + i * 55;
          const digit = padded[i];
          const hasVal = digit !== '0' || padded.slice(0, i).replace(/0/g, '') !== '';
          g.innerHTML += `
            <rect x="${x}" y="60" width="50" height="70" rx="6" fill="${hasVal ? 'rgba(30, 41, 59, 0.9)' : 'rgba(15, 23, 42, 0.4)'}" stroke="${hasVal ? '#38bdf8' : '#334155'}" stroke-width="1"/>
            <text x="${x + 25}" y="78" fill="#94a3b8" font-size="7.5" text-anchor="middle">${places[i].split(' ')[0]}</text>
            <text x="${x + 25}" y="108" fill="${hasVal ? '#f8fafc' : '#475569'}" font-size="16" font-weight="900" text-anchor="middle">${digit}</text>
          `;
        }
        sfx.playClick();
      }

      document.getElementById('btnNum1').addEventListener('click', (e) => {
        e.target.classList.add('active');
        renderNumber(458926, "Four lakh fifty-eight thousand nine hundred twenty-six", "4×10⁵ + 5×10⁴ + 8×10³ + 9×10² + 2×10¹ + 6×10⁰");
      });

      document.getElementById('btnNum2').addEventListener('click', (e) => {
        e.target.classList.add('active');
        renderNumber(604020, "Six lakh four thousand twenty", "6×10⁵ + 0×10⁴ + 4×10³ + 0×10² + 2×10¹ + 0×10⁰");
      });

      document.getElementById('btnNum3').addEventListener('click', (e) => {
        e.target.classList.add('active');
        renderNumber(24580000, "Two crore forty-five lakh eighty thousand", "2×10⁷ + 4×10⁶ + 5×10⁵ + 8×10⁴");
      });

      document.getElementById('btnNum4').addEventListener('click', (e) => {
        e.target.classList.add('active');
        renderNumber(10000000, "One crore (100 Lakhs)", "1×10⁷");
      });

      renderNumber(458926, "Four lakh fifty-eight thousand nine hundred twenty-six", "4×10⁵ + 5×10⁴ + 8×10³ + 9×10² + 2×10¹ + 6×10⁰");
    }

    // Slide 5: The "Land of Tens" Single-Button Calculator Game
    function simLandOfTensCalc() {
      simHeaderTitle.textContent = "The Land of Tens: Additive Number Construction Puzzle";
      let currentVal = 0;
      let targetVal = 3425;
      let clicks = 0;

      simCanvas.innerHTML = `
        <svg id="calcSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#020617"/>

          <!-- Calculator Frame -->
          <g transform="translate(100, 20)">
            <rect x="0" y="0" width="340" height="280" rx="16" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="2"/>
            
            <!-- LCD Screen -->
            <rect x="20" y="20" width="300" height="75" rx="8" fill="#0f172a" stroke="#1e293b" stroke-width="2"/>
            <text x="35" y="42" fill="#94a3b8" font-size="9" font-weight="700">TARGET: <tspan id="calcTarget" fill="#fbbf24" font-weight="800">3,425</tspan></text>
            <text x="210" y="42" fill="#94a3b8" font-size="9" font-weight="700">CLICKS: <tspan id="calcClicks" fill="#4ade80" font-weight="800">0</tspan></text>
            <text id="calcDisplay" x="305" y="80" fill="#38bdf8" font-size="28" font-weight="900" text-anchor="end">0</text>

            <!-- Buttons Grid -->
            <!-- Row 1: +1000, +100, +10, +1 -->
            <!-- Injected dynamically in controls -->

            <!-- Optimal Solved Notification -->
            <rect id="calcSolvedBox" x="20" y="235" width="300" height="30" rx="6" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="1" style="display:none;"/>
            <text id="calcSolvedText" x="170" y="254" fill="#34d399" font-size="10" font-weight="800" text-anchor="middle" style="display:none;">🎉 TARGET REACHED!</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:0.5rem; align-items:center; width:100%;">
          <div style="display:flex; flex-wrap:wrap; gap:0.4rem; justify-content:center;">
            <button class="sim-btn" id="btnPlus10000">+10,000</button>
            <button class="sim-btn" id="btnPlus1000">+1,000</button>
            <button class="sim-btn" id="btnPlus100">+100</button>
            <button class="sim-btn" id="btnPlus10">+10</button>
            <button class="sim-btn" id="btnPlus1">+1</button>
            <button class="sim-btn" id="btnCalcReset" style="background:#7f1d1d; border-color:#ef4444;">Reset (0)</button>
          </div>
          <div style="display:flex; gap:0.5rem; justify-content:center;">
            <button class="sim-btn" id="btnSetTarget3425">Target: 3,425</button>
            <button class="sim-btn" id="btnSetTarget5208">Target: 5,208</button>
            <button class="sim-btn" id="btnSetTarget10000">Target: 10,000</button>
          </div>
        </div>
      `;

      function updateCalc() {
        document.getElementById('calcDisplay').textContent = currentVal.toLocaleString('en-IN');
        document.getElementById('calcClicks').textContent = clicks;

        const solvedBox = document.getElementById('calcSolvedBox');
        const solvedText = document.getElementById('calcSolvedText');

        if (currentVal === targetVal) {
          solvedBox.style.display = 'block';
          solvedText.style.display = 'block';
          solvedText.textContent = `🎉 TARGET REACHED IN ${clicks} CLICKS!`;
          sfx.playCorrect();
        } else if (currentVal > targetVal) {
          solvedBox.style.display = 'block';
          solvedBox.setAttribute('fill', 'rgba(239, 68, 68, 0.25)');
          solvedBox.setAttribute('stroke', '#ef4444');
          solvedText.style.display = 'block';
          solvedText.setAttribute('fill', '#f87171');
          solvedText.textContent = `⚠️ EXCEEDED TARGET! Press Reset`;
          sfx.playIncorrect();
        } else {
          solvedBox.style.display = 'none';
          solvedText.style.display = 'none';
        }
      }

      function addInc(inc) {
        currentVal += inc;
        clicks++;
        sfx.playClick();
        updateCalc();
      }

      document.getElementById('btnPlus10000').addEventListener('click', () => addInc(10000));
      document.getElementById('btnPlus1000').addEventListener('click', () => addInc(1000));
      document.getElementById('btnPlus100').addEventListener('click', () => addInc(100));
      document.getElementById('btnPlus10').addEventListener('click', () => addInc(10));
      document.getElementById('btnPlus1').addEventListener('click', () => addInc(1));

      document.getElementById('btnCalcReset').addEventListener('click', () => {
        currentVal = 0;
        clicks = 0;
        sfx.playClick();
        updateCalc();
      });

      document.getElementById('btnSetTarget3425').addEventListener('click', () => {
        targetVal = 3425;
        currentVal = 0;
        clicks = 0;
        document.getElementById('calcTarget').textContent = "3,425";
        sfx.playClick();
        updateCalc();
      });

      document.getElementById('btnSetTarget5208').addEventListener('click', () => {
        targetVal = 5208;
        currentVal = 0;
        clicks = 0;
        document.getElementById('calcTarget').textContent = "5,208";
        sfx.playClick();
        updateCalc();
      });

      document.getElementById('btnSetTarget10000').addEventListener('click', () => {
        targetVal = 10000;
        currentVal = 0;
        clicks = 0;
        document.getElementById('calcTarget').textContent = "10,000";
        sfx.playClick();
        updateCalc();
      });
    }

    // Slide 6: Of Crores and Arabs (Cosmic Scales)
    function simCroresAndArabs() {
      simHeaderTitle.textContent = "Powers of Ten & Sanskrit Scale Ladder: From One to Arab";

      simCanvas.innerHTML = `
        <svg id="croresSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#020617"/>

          <!-- Logarithmic Stepping Ladder Graphic -->
          <g id="ladderGroup" transform="translate(40, 25)">
            <!-- 10^3: Thousand -->
            <rect x="0" y="0" width="140" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
            <text x="12" y="18" fill="#38bdf8" font-size="9" font-weight="800">Thousand (10³)</text>
            <text x="12" y="32" fill="#f8fafc" font-size="10">1,000 (Sahasra)</text>

            <!-- 10^4: Ten Thousand -->
            <rect x="0" y="50" width="180" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
            <text x="12" y="68" fill="#38bdf8" font-size="9" font-weight="800">Ten Thousand (10⁴)</text>
            <text x="12" y="82" fill="#f8fafc" font-size="10">10,000 (Ayuta)</text>

            <!-- 10^5: Lakh -->
            <rect x="0" y="100" width="230" height="40" rx="6" fill="rgba(6, 78, 59, 0.7)" stroke="#10b981" stroke-width="1.5"/>
            <text x="12" y="118" fill="#34d399" font-size="9" font-weight="800">One Lakh (10⁵)</text>
            <text x="12" y="132" fill="#f8fafc" font-size="10">1,00,000 (Laksha)</text>

            <!-- 10^6: Ten Lakhs (1 Million) -->
            <rect x="0" y="150" width="280" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
            <text x="12" y="168" fill="#38bdf8" font-size="9" font-weight="800">Ten Lakhs / 1 Million (10⁶)</text>
            <text x="12" y="182" fill="#f8fafc" font-size="10">10,00,000 (Prayuta)</text>

            <!-- 10^7: One Crore -->
            <rect x="0" y="200" width="340" height="40" rx="6" fill="rgba(124, 45, 18, 0.7)" stroke="#f97316" stroke-width="1.5"/>
            <text x="12" y="218" fill="#fb923c" font-size="9" font-weight="800">One Crore (10⁷)</text>
            <text x="12" y="232" fill="#f8fafc" font-size="10">1,00,00,000 (Koṭi)</text>

            <!-- 10^9: One Arab (1 Billion) -->
            <rect x="0" y="250" width="450" height="40" rx="6" fill="rgba(112, 26, 117, 0.7)" stroke="#d946ef" stroke-width="1.5"/>
            <text x="12" y="268" fill="#e879f9" font-size="9" font-weight="800">One Arab / 1 Billion (10⁹ = 100 Crores)</text>
            <text x="12" y="282" fill="#f8fafc" font-size="10">1,00,00,00,000 (Arvuda)</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn" id="btnExplainLakh">🌟 1 Lakh ($10^5$)</button>
          <button class="sim-btn" id="btnExplainCrore">🚀 1 Crore ($10^7$)</button>
          <button class="sim-btn" id="btnExplainArab">🌌 1 Arab ($10^9$)</button>
        </div>
      `;

      document.getElementById('btnExplainLakh').addEventListener('click', () => sfx.playClick());
      document.getElementById('btnExplainCrore').addEventListener('click', () => sfx.playClick());
      document.getElementById('btnExplainArab').addEventListener('click', () => sfx.playCorrect());
    }

    // Slide 7: Indian vs. International System Converter
    function simIndianVsInternational() {
      simHeaderTitle.textContent = "Indian (3:2:2) vs. International (3:3:3) Dual Converter";
      let testVal = 25000000;

      simCanvas.innerHTML = `
        <svg id="convertSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

          <!-- Indian System Card on Left -->
          <g transform="translate(30, 30)">
            <rect x="0" y="0" width="230" height="200" rx="12" fill="rgba(6, 78, 59, 0.5)" stroke="#10b981" stroke-width="1.5"/>
            <text x="115" y="26" fill="#34d399" font-size="13" font-weight="800" text-anchor="middle">Indian System (3:2:2)</text>
            <line x1="12" y1="36" x2="218" y2="36" stroke="rgba(52, 211, 153, 0.3)"/>

            <text x="15" y="62" fill="#94a3b8" font-size="9.5">Grouping Syntax:</text>
            <text x="15" y="78" fill="#f8fafc" font-size="10" font-weight="700">3 then pairs of 2s (..., 2, 2, 3)</text>

            <text x="15" y="105" fill="#94a3b8" font-size="9.5">Formatted Numeral:</text>
            <text id="lblDualIndian" x="15" y="125" fill="#34d399" font-size="18" font-weight="900">2,50,00,000</text>

            <text x="15" y="152" fill="#94a3b8" font-size="9.5">In Words:</text>
            <text id="lblDualIndianWords" x="15" y="172" fill="#a7f3d0" font-size="10" font-weight="700">Two Crore Fifty Lakhs</text>
          </g>

          <!-- International System Card on Right -->
          <g transform="translate(280, 30)">
            <rect x="0" y="0" width="230" height="200" rx="12" fill="rgba(2, 132, 199, 0.5)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="115" y="26" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">International System (3:3:3)</text>
            <line x1="12" y1="36" x2="218" y2="36" stroke="rgba(56, 189, 248, 0.3)"/>

            <text x="15" y="62" fill="#94a3b8" font-size="9.5">Grouping Syntax:</text>
            <text x="15" y="78" fill="#f8fafc" font-size="10" font-weight="700">Strict triads of 3s (..., 3, 3, 3)</text>

            <text x="15" y="105" fill="#94a3b8" font-size="9.5">Formatted Numeral:</text>
            <text id="lblDualIntl" x="15" y="125" fill="#38bdf8" font-size="18" font-weight="900">25,000,000</text>

            <text x="15" y="152" fill="#94a3b8" font-size="9.5">In Words:</text>
            <text id="lblDualIntlWords" x="15" y="172" fill="#bae6fd" font-size="10" font-weight="700">Twenty-Five Million</text>
          </g>

          <!-- Equivalence Formula Strip at Bottom -->
          <g transform="translate(30, 245)">
            <rect x="0" y="0" width="480" height="55" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#fbbf24" stroke-width="1"/>
            <text x="240" y="22" fill="#fbbf24" font-size="10" font-weight="800" text-anchor="middle">Key Conversion Formulas:</text>
            <text x="240" y="42" fill="#f8fafc" font-size="9.5" text-anchor="middle">100 Thousand = 1 Lakh • 1 Million = 10 Lakhs • 10 Million = 1 Crore • 1 Billion = 100 Crores</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn" id="btnConv100K">100,000 (1 Lakh)</button>
          <button class="sim-btn" id="btnConv1M">1,000,000 (10 Lakhs)</button>
          <button class="sim-btn active" id="btnConv25M">25,000,000 (2.5 Cr)</button>
          <button class="sim-btn" id="btnConv100M">100,000,000 (10 Cr)</button>
          <button class="sim-btn" id="btnConv1B">1,000,000,000 (1 Arab)</button>
        </div>
      `;

      function setConversion(val, indStr, indWords, intStr, intWords) {
        document.getElementById('lblDualIndian').textContent = indStr;
        document.getElementById('lblDualIndianWords').textContent = indWords;
        document.getElementById('lblDualIntl').textContent = intStr;
        document.getElementById('lblDualIntlWords').textContent = intWords;
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        sfx.playClick();
      }

      document.getElementById('btnConv100K').addEventListener('click', (e) => {
        e.target.classList.add('active');
        setConversion(100000, "1,00,000", "One Lakh", "100,000", "One Hundred Thousand");
      });

      document.getElementById('btnConv1M').addEventListener('click', (e) => {
        e.target.classList.add('active');
        setConversion(1000000, "10,00,000", "Ten Lakhs", "1,000,000", "One Million");
      });

      document.getElementById('btnConv25M').addEventListener('click', (e) => {
        e.target.classList.add('active');
        setConversion(25000000, "2,50,00,000", "Two Crore Fifty Lakhs", "25,000,000", "Twenty-Five Million");
      });

      document.getElementById('btnConv100M').addEventListener('click', (e) => {
        e.target.classList.add('active');
        setConversion(100000000, "10,00,00,000", "Ten Crores", "100,000,000", "One Hundred Million");
      });

      document.getElementById('btnConv1B').addEventListener('click', (e) => {
        e.target.classList.add('active');
        setConversion(1000000000, "1,00,00,00,000", "One Arab (100 Crores)", "1,000,000,000", "One Billion");
      });
    }

    // Slide 8: Exact vs. Approximate Values & Practical Estimation
    function simExactVsApprox() {
      simHeaderTitle.textContent = "Exact vs. Approximate Values: Practical Scenario Classifier";

      const scenarios = [
        { title: "Bank Account Transfer", type: "exact", reason: "Financial regulations require exact accuracy down to 1 paisa." },
        { title: "National Census Population", type: "approx", reason: "Births and deaths change the number every few seconds." },
        { title: "Rocket Trajectory to Moon", type: "exact", reason: "A 0.01% error causes spacecraft to miss lunar gravitational capture." },
        { title: "Spectators at Football Game", type: "approx", reason: "Approximations like '60,000 fans' convey the crowd size effectively." },
        { title: "Doctor's Chemotherapy Dosage", type: "exact", reason: "Overdose is toxic; underdose fails to treat disease." },
        { title: "Distance between Delhi & Mumbai", type: "approx", reason: "Road distance varies by route (about 1,400 km is sufficient)." }
      ];

      let currentScenIdx = 0;

      simCanvas.innerHTML = `
        <svg id="exactSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#020617"/>

          <!-- Interactive Question Card -->
          <g transform="translate(70, 30)">
            <rect x="0" y="0" width="400" height="150" rx="14" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="200" y="28" fill="#94a3b8" font-size="10" font-weight="700" text-anchor="middle">SCENARIO CLASSIFICATION</text>
            <text id="scenTitle" x="200" y="65" fill="#f8fafc" font-size="15" font-weight="800" text-anchor="middle">Bank Account Transfer</text>
            
            <rect x="30" y="85" width="340" height="45" rx="6" fill="rgba(30, 41, 59, 0.6)"/>
            <text x="200" y="112" fill="#cbd5e1" font-size="10" text-anchor="middle">Is an EXACT number required, or is an APPROXIMATION better?</text>
          </g>

          <!-- Feedback Box -->
          <g transform="translate(70, 200)">
            <rect id="fbBox" x="0" y="0" width="400" height="90" rx="10" fill="rgba(30, 41, 59, 0.7)" stroke="#475569" stroke-width="1"/>
            <text id="fbTitle" x="200" y="32" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Choose an option below</text>
            <text id="fbDesc" x="200" y="58" fill="#94a3b8" font-size="9.5" text-anchor="middle">Test your understanding of practical precision!</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:0.5rem; align-items:center; width:100%;">
          <div style="display:flex; gap:0.6rem; justify-content:center;">
            <button class="sim-btn" id="btnAnsExact" style="background:#065f46; border-color:#10b981;">🎯 Strictly EXACT</button>
            <button class="sim-btn" id="btnAnsApprox" style="background:#0369a1; border-color:#38bdf8;">📊 Best as APPROXIMATION</button>
          </div>
          <button class="sim-btn" id="btnNextScen">Next Scenario ➔</button>
        </div>
      `;

      function checkAnswer(chosen) {
        const item = scenarios[currentScenIdx];
        const fbBox = document.getElementById('fbBox');
        const fbTitle = document.getElementById('fbTitle');
        const fbDesc = document.getElementById('fbDesc');

        if (chosen === item.type) {
          fbBox.setAttribute('fill', 'rgba(16, 185, 129, 0.2)');
          fbBox.setAttribute('stroke', '#10b981');
          fbTitle.textContent = "✓ Correct Decision!";
          fbTitle.setAttribute('fill', '#34d399');
          fbDesc.textContent = item.reason;
          sfx.playCorrect();
        } else {
          fbBox.setAttribute('fill', 'rgba(239, 68, 68, 0.25)');
          fbBox.setAttribute('stroke', '#ef4444');
          fbTitle.textContent = "✕ Not Quite!";
          fbTitle.setAttribute('fill', '#f87171');
          fbDesc.textContent = item.reason;
          sfx.playIncorrect();
        }
      }

      document.getElementById('btnAnsExact').addEventListener('click', () => checkAnswer('exact'));
      document.getElementById('btnAnsApprox').addEventListener('click', () => checkAnswer('approx'));

      document.getElementById('btnNextScen').addEventListener('click', () => {
        currentScenIdx = (currentScenIdx + 1) % scenarios.length;
        document.getElementById('scenTitle').textContent = scenarios[currentScenIdx].title;
        document.getElementById('fbBox').setAttribute('fill', 'rgba(30, 41, 59, 0.7)');
        document.getElementById('fbBox').setAttribute('stroke', '#475569');
        document.getElementById('fbTitle').textContent = "Choose an option below";
        document.getElementById('fbTitle').setAttribute('fill', '#38bdf8');
        document.getElementById('fbDesc').textContent = "Test your understanding of practical precision!";
        sfx.playClick();
      });
    }

    // Slide 9: "Nearest Neighbours" Number Line Rounding
    function simNearestNeighboursRounding() {
      simHeaderTitle.textContent = "Nearest Neighbours: Interactive Number Line Rounding";
      let val = 47825;
      let roundPlace = 'thousand'; // 'thousand' or 'lakh'

      simCanvas.innerHTML = `
        <svg id="roundLineSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

          <!-- Top Infocard -->
          <g transform="translate(50, 20)">
            <rect x="0" y="0" width="440" height="65" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.2"/>
            <text x="20" y="24" fill="#94a3b8" font-size="9.5">Current Number:</text>
            <text id="lblCurrentNum" x="20" y="50" fill="#f8fafc" font-size="18" font-weight="900">47,825</text>
            <text id="lblRoundRule" x="220" y="38" fill="#4ade80" font-size="10" font-weight="700">Rounding to Nearest Thousand (8 ≥ 5 → Round UP)</text>
          </g>

          <!-- Number Line Axis (y = 170) -->
          <line x1="50" y1="170" x2="490" y2="170" stroke="#64748b" stroke-width="4" stroke-linecap="round"/>

          <!-- Lower Landmark (e.g. 47,000) -->
          <g transform="translate(80, 170)">
            <line x1="0" y1="-15" x2="0" y2="15" stroke="#38bdf8" stroke-width="3"/>
            <circle cx="0" cy="0" r="6" fill="#0284c7"/>
            <text id="lblLowLandmark" x="0" y="35" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">47,000</text>
            <text x="0" y="50" fill="#94a3b8" font-size="8" text-anchor="middle">Lower Landmark</text>
          </g>

          <!-- Exact Halfway Point (e.g. 47,500) -->
          <g transform="translate(270, 170)">
            <line x1="0" y1="-20" x2="0" y2="20" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3,3"/>
            <circle cx="0" cy="0" r="5" fill="#f59e0b"/>
            <text id="lblMidPoint" x="0" y="-28" fill="#fbbf24" font-size="10" font-weight="800" text-anchor="middle">47,500 (Halfway)</text>
          </g>

          <!-- Upper Landmark (e.g. 48,000) -->
          <g transform="translate(460, 170)">
            <line x1="0" y1="-15" x2="0" y2="15" stroke="#10b981" stroke-width="3"/>
            <circle cx="0" cy="0" r="6" fill="#059669"/>
            <text id="lblHighLandmark" x="0" y="35" fill="#10b981" font-size="11" font-weight="800" text-anchor="middle">48,000</text>
            <text x="0" y="50" fill="#94a3b8" font-size="8" text-anchor="middle">Upper Landmark</text>
          </g>

          <!-- The Active Point Marker -->
          <g id="activePointMarker" transform="translate(393, 170)">
            <circle cx="0" cy="0" r="9" fill="#ef4444" stroke="#ffffff" stroke-width="2"/>
            <polygon points="-8,-14 8,-14 0,-4" fill="#ef4444"/>
            <text id="lblPointTag" x="0" y="-18" fill="#f87171" font-size="9" font-weight="900" text-anchor="middle">47,825</text>
          </g>

          <!-- Bottom Rounded Verdict Card -->
          <g transform="translate(50, 245)">
            <rect id="roundVerdictCard" x="0" y="0" width="440" height="55" rx="8" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="1.5"/>
            <text id="lblVerdictText" x="220" y="24" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">47,825 is closer to 48,000 ➔ Rounds to 48,000</text>
            <text id="lblVerdictSub" x="220" y="42" fill="#cbd5e1" font-size="9" text-anchor="middle">Distance to 48,000 is 175; Distance to 47,000 is 825.</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.4rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnR1">47,825 ➔ Nearest 1,000</button>
          <button class="sim-btn" id="btnR2">74,499 ➔ Nearest 1,000</button>
          <button class="sim-btn" id="btnR3">3,42,890 ➔ Nearest Lakh</button>
          <button class="sim-btn" id="btnR4">8,64,320 ➔ Nearest Lakh</button>
        </div>
      `;

      function setRounding(n, low, mid, high, place, rounded, rule, sub) {
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        document.getElementById('lblCurrentNum').textContent = n.toLocaleString('en-IN');
        document.getElementById('lblLowLandmark').textContent = low.toLocaleString('en-IN');
        document.getElementById('lblMidPoint').textContent = mid.toLocaleString('en-IN') + ' (Halfway)';
        document.getElementById('lblHighLandmark').textContent = high.toLocaleString('en-IN');
        document.getElementById('lblRoundRule').textContent = rule;
        document.getElementById('lblPointTag').textContent = n.toLocaleString('en-IN');

        // Scale marker x between 80 and 460
        const pct = (n - low) / (high - low);
        const newX = 80 + pct * 380;
        document.getElementById('activePointMarker').setAttribute('transform', `translate(${newX}, 170)`);

        document.getElementById('lblVerdictText').textContent = `${n.toLocaleString('en-IN')} ➔ Rounds to ${rounded.toLocaleString('en-IN')}`;
        document.getElementById('lblVerdictSub').textContent = sub;
        sfx.playClick();
      }

      document.getElementById('btnR1').addEventListener('click', (e) => {
        e.target.classList.add('active');
        setRounding(47825, 47000, 47500, 48000, 'thousand', 48000, "Hundreds digit 8 ≥ 5 → Round UP", "Distance to 48,000 is 175; Distance to 47,000 is 825.");
      });

      document.getElementById('btnR2').addEventListener('click', (e) => {
        e.target.classList.add('active');
        setRounding(74499, 74000, 74500, 75000, 'thousand', 74000, "Hundreds digit 4 < 5 → Round DOWN", "Distance to 74,000 is 499; Distance to 75,000 is 501.");
      });

      document.getElementById('btnR3').addEventListener('click', (e) => {
        e.target.classList.add('active');
        setRounding(342890, 300000, 350000, 400000, 'lakh', 300000, "Ten-thousands digit 4 < 5 → Round DOWN", "Distance to 3 Lakh is 42,890; Distance to 4 Lakh is 57,110.");
      });

      document.getElementById('btnR4').addEventListener('click', (e) => {
        e.target.classList.add('active');
        setRounding(864320, 800000, 850000, 900000, 'lakh', 900000, "Ten-thousands digit 6 ≥ 5 → Round UP", "Distance to 9 Lakh is 35,680; Distance to 8 Lakh is 64,320.");
      });
    }

    // Slide 10: Population Dynamics of Major Indian Cities
    function simCityPopulationsData() {
      simHeaderTitle.textContent = "Census Data Explorer: Major Indian Metropolitan Growth";

      const cityData = {
        mumbai: { name: "Mumbai", p2001: 11978450, p2011: 12442373, growth: 463923, pct: "+3.9%", col: "#f59e0b" },
        delhi: { name: "Delhi", p2001: 9817439, p2011: 11034555, growth: 1217116, pct: "+12.4%", col: "#38bdf8" },
        bengaluru: { name: "Bengaluru", p2001: 4301326, p2011: 8443675, growth: 4142349, pct: "+96.3% (Doubled)", col: "#10b981" }
      };

      simCanvas.innerHTML = `
        <svg id="citySvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#020617"/>

          <!-- City Details Card -->
          <g transform="translate(30, 25)">
            <rect x="0" y="0" width="480" height="120" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5"/>
            <text id="cityCardName" x="25" y="32" fill="#38bdf8" font-size="16" font-weight="900">Mumbai Metropolitan Region</text>
            
            <text x="25" y="62" fill="#94a3b8" font-size="10">2001 Census Count:</text>
            <text id="cPop01" x="25" y="82" fill="#f8fafc" font-size="14" font-weight="800">1,19,78,450 (~1.20 Crore)</text>

            <text x="260" y="62" fill="#94a3b8" font-size="10">2011 Census Count:</text>
            <text id="cPop11" x="260" y="82" fill="#4ade80" font-size="14" font-weight="800">1,24,42,373 (~1.24 Crore)</text>

            <line x1="25" y1="95" x2="455" y2="95" stroke="rgba(255,255,255,0.1)"/>
            <text x="25" y="110" fill="#fbbf24" font-size="9.5" font-weight="700">Decadal Net Increase: <tspan id="cIncrease">4,63,923 citizens (+3.9%)</tspan></text>
          </g>

          <!-- Comparative Population Bar Chart -->
          <g transform="translate(30, 160)">
            <rect x="0" y="0" width="480" height="145" rx="10" fill="rgba(15, 23, 42, 0.85)" stroke="#334155" stroke-width="1"/>
            <text x="240" y="22" fill="#cbd5e1" font-size="10" font-weight="800" text-anchor="middle">Population Scale Comparison (Crores)</text>

            <!-- Bars -->
            <!-- 2001 Bar -->
            <rect x="60" y="45" width="20" height="70" fill="#64748b" rx="2" id="bar01"/>
            <text x="70" y="130" fill="#94a3b8" font-size="9" text-anchor="middle">2001</text>
            <text id="lblBar01Val" x="70" y="40" fill="#cbd5e1" font-size="9" font-weight="700" text-anchor="middle">1.20 Cr</text>

            <!-- 2011 Bar -->
            <rect x="140" y="40" width="20" height="75" fill="#f59e0b" rx="2" id="bar11"/>
            <text x="150" y="130" fill="#fde047" font-size="9" text-anchor="middle">2011</text>
            <text id="lblBar11Val" x="150" y="35" fill="#fbbf24" font-size="9" font-weight="800" text-anchor="middle">1.24 Cr</text>

            <!-- Growth Analysis Box on right -->
            <rect x="230" y="40" width="230" height="85" rx="6" fill="rgba(30, 41, 59, 0.6)"/>
            <text id="lblGrowthFact1" x="240" y="60" fill="#f8fafc" font-size="9" font-weight="700">Largest Mega-City in India (2011)</text>
            <text id="lblGrowthFact2" x="240" y="80" fill="#cbd5e1" font-size="8.5">• Surpassed 1.2 Crore mark</text>
            <text id="lblGrowthFact3" x="240" y="100" fill="#cbd5e1" font-size="8.5">• Requires 1.5 Lakh buses to seat all!</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnCityMumbai">Mumbai (1.24 Cr)</button>
          <button class="sim-btn" id="btnCityDelhi">Delhi (1.10 Cr)</button>
          <button class="sim-btn" id="btnCityBengaluru">Bengaluru (84.4 Lakhs - Doubled!)</button>
        </div>
      `;

      function selectCity(key) {
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        const d = cityData[key];

        document.getElementById('cityCardName').textContent = `${d.name} Metropolitan Region`;
        document.getElementById('cPop01').textContent = `${d.p2001.toLocaleString('en-IN')} (~${(d.p2001/10000000).toFixed(2)} Cr)`;
        document.getElementById('cPop11').textContent = `${d.p2011.toLocaleString('en-IN')} (~${(d.p2011/10000000).toFixed(2)} Cr)`;
        document.getElementById('cIncrease').textContent = `${d.growth.toLocaleString('en-IN')} citizens (${d.pct})`;

        const b01 = document.getElementById('bar01');
        const b11 = document.getElementById('bar11');
        const h01 = (d.p2001 / 13000000) * 80;
        const h11 = (d.p2011 / 13000000) * 80;

        b01.setAttribute('height', h01);
        b01.setAttribute('y', 115 - h01);
        b11.setAttribute('height', h11);
        b11.setAttribute('y', 115 - h11);
        b11.setAttribute('fill', d.col);

        document.getElementById('lblBar01Val').textContent = (d.p2001/10000000).toFixed(2) + ' Cr';
        document.getElementById('lblBar01Val').setAttribute('y', 110 - h01);
        document.getElementById('lblBar11Val').textContent = (d.p2011/10000000).toFixed(2) + ' Cr';
        document.getElementById('lblBar11Val').setAttribute('y', 110 - h11);

        if (key === 'mumbai') {
          document.getElementById('lblGrowthFact1').textContent = "Largest Mega-City in India (2011)";
          document.getElementById('lblGrowthFact2').textContent = "• Surpassed 1.24 Crore mark";
          document.getElementById('lblGrowthFact3').textContent = "• High density coastal peninsula";
        } else if (key === 'delhi') {
          document.getElementById('lblGrowthFact1').textContent = "Crossed 1-Crore Milestone!";
          document.getElementById('lblGrowthFact2').textContent = "• Surged from 98 Lakhs to 1.10 Crore";
          document.getElementById('lblGrowthFact3').textContent = "• +12.1 Lakhs net influx";
        } else {
          document.getElementById('lblGrowthFact1').textContent = "Near 100% Decade Surge (+96.3%)";
          document.getElementById('lblGrowthFact2').textContent = "• Nearly doubled from 43L to 84L";
          document.getElementById('lblGrowthFact3').textContent = "• Tech hub boom added ~4L/year";
        }
        sfx.playClick();
      }

      document.getElementById('btnCityMumbai').addEventListener('click', (e) => { e.target.classList.add('active'); selectCity('mumbai'); });
      document.getElementById('btnCityDelhi').addEventListener('click', (e) => { e.target.classList.add('active'); selectCity('delhi'); });
      document.getElementById('btnCityBengaluru').addEventListener('click', (e) => { e.target.classList.add('active'); selectCity('bengaluru'); });
    }

    // Slide 11: Mental Math Shortcut: Multiplying by 5, 25, 50
    function simMultiplyByFiveShortcut() {
      simHeaderTitle.textContent = "Mental Math Shortcuts: Multiplying by 5, 25, and 50";

      simCanvas.innerHTML = `
        <svg id="multShortcutSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

          <!-- Formula Transformation Box -->
          <g transform="translate(40, 25)">
            <rect x="0" y="0" width="460" height="90" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="230" y="26" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Algebraic Shortcut Principle</text>
            <text id="lblFormulaMain" x="230" y="58" fill="#fbbf24" font-size="16" font-weight="900" text-anchor="middle">N × 5 = (N ÷ 2) × 10</text>
            <text id="lblFormulaSub" x="230" y="78" fill="#94a3b8" font-size="9.5" text-anchor="middle">Halve the number, then append a zero!</text>
          </g>

          <!-- Step-by-Step Execution Visualizer -->
          <g transform="translate(40, 130)">
            <rect x="0" y="0" width="460" height="155" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5"/>
            
            <text id="lblStep1" x="25" y="35" fill="#f8fafc" font-size="13" font-weight="800">Problem: 84 × 5</text>
            
            <line x1="25" y1="48" x2="435" y2="48" stroke="rgba(255,255,255,0.1)"/>

            <text id="lblStep2" x="25" y="75" fill="#38bdf8" font-size="11" font-weight="700">Step 1: Divide by 2 ➔ 84 ÷ 2 = 42</text>
            <text id="lblStep3" x="25" y="105" fill="#fbbf24" font-size="11" font-weight="700">Step 2: Multiply by 10 ➔ 42 × 10 = 420</text>
            
            <rect x="25" y="118" width="410" height="28" rx="6" fill="rgba(16, 185, 129, 0.25)"/>
            <text id="lblFinalAnswer" x="230" y="137" fill="#34d399" font-size="13" font-weight="900" text-anchor="middle">FINAL ANSWER = 420</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.4rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnS_84x5">84 × 5</button>
          <button class="sim-btn" id="btnS_164x5">164 × 5</button>
          <button class="sim-btn" id="btnS_36x25">36 × 25</button>
          <button class="sim-btn" id="btnS_64x25">64 × 25</button>
          <button class="sim-btn" id="btnS_86x50">86 × 50</button>
        </div>
      `;

      function renderShortcut(fMain, fSub, s1, s2, s3, ans) {
        document.getElementById('lblFormulaMain').textContent = fMain;
        document.getElementById('lblFormulaSub').textContent = fSub;
        document.getElementById('lblStep1').textContent = s1;
        document.getElementById('lblStep2').textContent = s2;
        document.getElementById('lblStep3').textContent = s3;
        document.getElementById('lblFinalAnswer').textContent = ans;
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        sfx.playCorrect();
      }

      document.getElementById('btnS_84x5').addEventListener('click', (e) => {
        e.target.classList.add('active');
        renderShortcut("N × 5 = (N ÷ 2) × 10", "Halve the number, then append a zero!", "Problem: 84 × 5", "Step 1: Divide by 2 ➔ 84 ÷ 2 = 42", "Step 2: Multiply by 10 ➔ 42 × 10 = 420", "FINAL ANSWER = 420");
      });

      document.getElementById('btnS_164x5').addEventListener('click', (e) => {
        e.target.classList.add('active');
        renderShortcut("N × 5 = (N ÷ 2) × 10", "Halve the number, then append a zero!", "Problem: 164 × 5", "Step 1: Divide by 2 ➔ 164 ÷ 2 = 82", "Step 2: Multiply by 10 ➔ 82 × 10 = 820", "FINAL ANSWER = 820");
      });

      document.getElementById('btnS_36x25').addEventListener('click', (e) => {
        e.target.classList.add('active');
        renderShortcut("N × 25 = (N ÷ 4) × 100", "Divide by 4, then append two zeroes!", "Problem: 36 × 25", "Step 1: Divide by 4 ➔ 36 ÷ 4 = 9", "Step 2: Multiply by 100 ➔ 9 × 100 = 900", "FINAL ANSWER = 900");
      });

      document.getElementById('btnS_64x25').addEventListener('click', (e) => {
        e.target.classList.add('active');
        renderShortcut("N × 25 = (N ÷ 4) × 100", "Divide by 4, then append two zeroes!", "Problem: 64 × 25", "Step 1: Divide by 4 ➔ 64 ÷ 4 = 16", "Step 2: Multiply by 100 ➔ 16 × 100 = 1,600", "FINAL ANSWER = 1,600");
      });

      document.getElementById('btnS_86x50').addEventListener('click', (e) => {
        e.target.classList.add('active');
        renderShortcut("N × 50 = (N ÷ 2) × 100", "Halve the number, then append two zeroes!", "Problem: 86 × 50", "Step 1: Divide by 2 ➔ 86 ÷ 2 = 43", "Step 2: Multiply by 100 ➔ 43 × 100 = 4,300", "FINAL ANSWER = 4,300");
      });
    }

    // Slide 12: Grouped Factorisation Multiplication Shortcuts
    function simGroupedFactorisation() {
      simHeaderTitle.textContent = "Grouped Factorisation: Regrouping to Create 10s and 100s";

      simCanvas.innerHTML = `
        <svg id="factorSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#020617"/>

          <!-- Header Problem Display -->
          <g transform="translate(50, 20)">
            <rect x="0" y="0" width="440" height="50" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#fbbf24" stroke-width="1.2"/>
            <text id="lblFactorProblem" x="220" y="32" fill="#fbbf24" font-size="16" font-weight="900" text-anchor="middle">Calculate: 18 × 35</text>
          </g>

          <!-- Factorisation Decomposition Tiles (Row 1) -->
          <g transform="translate(50, 85)">
            <!-- 18 Tile -->
            <rect x="30" y="0" width="150" height="45" rx="8" fill="rgba(2, 132, 199, 0.3)" stroke="#38bdf8" stroke-width="1.5"/>
            <text id="lblTile18" x="105" y="28" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">18 = 9 × 2</text>

            <text x="210" y="30" fill="#f8fafc" font-size="20">×</text>

            <!-- 35 Tile -->
            <rect x="240" y="0" width="150" height="45" rx="8" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="1.5"/>
            <text id="lblTile35" x="315" y="28" fill="#34d399" font-size="13" font-weight="800" text-anchor="middle">35 = 5 × 7</text>
          </g>

          <!-- Animated Regrouping Arrow -->
          <text x="270" y="160" fill="#cbd5e1" font-size="16" text-anchor="middle">⬇ Regroup Friendly Factors (2 × 5) ⬇</text>

          <!-- Regrouped Row (Row 2) -->
          <g transform="translate(50, 180)">
            <rect x="30" y="0" width="150" height="45" rx="8" fill="rgba(245, 158, 11, 0.25)" stroke="#f59e0b" stroke-width="1.5"/>
            <text id="lblRegroupLeft" x="105" y="28" fill="#fbbf24" font-size="13" font-weight="800" text-anchor="middle">(9 × 7) = 63</text>

            <text x="210" y="30" fill="#f8fafc" font-size="20">×</text>

            <rect x="240" y="0" width="150" height="45" rx="8" fill="rgba(234, 88, 12, 0.25)" stroke="#f97316" stroke-width="1.5"/>
            <text id="lblRegroupRight" x="315" y="28" fill="#fb923c" font-size="13" font-weight="800" text-anchor="middle">(2 × 5) = 10</text>
          </g>

          <!-- Final Product Box -->
          <g transform="translate(50, 245)">
            <rect x="0" y="0" width="440" height="50" rx="10" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="1.5"/>
            <text id="lblFactorFinal" x="220" y="32" fill="#34d399" font-size="15" font-weight="900" text-anchor="middle">63 × 10 = 630 (Solved in 2 seconds!)</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnGF_18x35">18 × 35</button>
          <button class="sim-btn" id="btnGF_16x45">16 × 45</button>
          <button class="sim-btn" id="btnGF_24x75">24 × 75</button>
          <button class="sim-btn" id="btnGF_28x25">28 × 25</button>
        </div>
      `;

      function renderFactor(prob, t1, t2, rLeft, rRight, finalAns) {
        document.getElementById('lblFactorProblem').textContent = prob;
        document.getElementById('lblTile18').textContent = t1;
        document.getElementById('lblTile35').textContent = t2;
        document.getElementById('lblRegroupLeft').textContent = rLeft;
        document.getElementById('lblRegroupRight').textContent = rRight;
        document.getElementById('lblFactorFinal').textContent = finalAns;
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        sfx.playCorrect();
      }

      document.getElementById('btnGF_18x35').addEventListener('click', (e) => {
        e.target.classList.add('active');
        renderFactor("Calculate: 18 × 35", "18 = 9 × 2", "35 = 5 × 7", "(9 × 7) = 63", "(2 × 5) = 10", "63 × 10 = 630 (Solved in 2 seconds!)");
      });

      document.getElementById('btnGF_16x45').addEventListener('click', (e) => {
        e.target.classList.add('active');
        renderFactor("Calculate: 16 × 45", "16 = 8 × 2", "45 = 5 × 9", "(8 × 9) = 72", "(2 × 5) = 10", "72 × 10 = 720 (Solved in 2 seconds!)");
      });

      document.getElementById('btnGF_24x75').addEventListener('click', (e) => {
        e.target.classList.add('active');
        renderFactor("Calculate: 24 × 75", "24 = 6 × 4", "75 = 25 × 3", "(6 × 3) = 18", "(4 × 25) = 100", "18 × 100 = 1,800 (Solved in 2 seconds!)");
      });

      document.getElementById('btnGF_28x25').addEventListener('click', (e) => {
        e.target.classList.add('active');
        renderFactor("Calculate: 28 × 25", "28 = 7 × 4", "25 = 25", "7", "(4 × 25) = 100", "7 × 100 = 700 (Solved in 2 seconds!)");
      });
    }

    // Slide 13: "How Long is the Product?" Digit Length Invariant Predictor
    function simHowLongIsProduct() {
      simHeaderTitle.textContent = "Product Digit Length Invariant: Minimum vs. Maximum Digits";
      let m = 3;
      let n = 4;

      simCanvas.innerHTML = `
        <svg id="digitLenSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

          <!-- Theorem Card -->
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="460" height="75" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="230" y="24" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Product Digit Length Invariant Theorem</text>
            <text x="230" y="46" fill="#fbbf24" font-size="13" font-weight="900" text-anchor="middle">(m-digit number) × (n-digit number) has EITHER:</text>
            <text x="230" y="66" fill="#4ade80" font-size="12" font-weight="800" text-anchor="middle">(m + n - 1) digits  OR  (m + n) digits</text>
          </g>

          <!-- Current Parameters Display -->
          <g transform="translate(40, 105)">
            <rect x="0" y="0" width="460" height="195" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5"/>
            
            <text id="lblCurrentMN" x="25" y="32" fill="#38bdf8" font-size="14" font-weight="900">Current Test: m = 3 digits, n = 4 digits</text>
            <line x1="25" y1="44" x2="435" y2="44" stroke="rgba(255,255,255,0.1)"/>

            <text x="25" y="70" fill="#cbd5e1" font-size="11" font-weight="700">Possible Lengths: <tspan id="lblPossibleLengths" fill="#fbbf24" font-weight="900">6 or 7 digits</tspan></text>
            <text x="25" y="92" fill="#94a3b8" font-size="9.5">• Minimum: m + n - 1 = 3 + 4 - 1 = 6 digits</text>
            <text x="25" y="110" fill="#94a3b8" font-size="9.5">• Maximum: m + n = 3 + 4 = 7 digits</text>

            <rect x="25" y="125" width="410" height="55" rx="8" fill="rgba(30, 41, 59, 0.7)"/>
            <text id="lblSmallestEx" x="35" y="145" fill="#bae6fd" font-size="9.5">Smallest Case: 100 × 1,000 = 1,00,000 (6 digits)</text>
            <text id="lblLargestEx" x="35" y="165" fill="#fde047" font-size="9.5">Largest Case: 999 × 9,999 = 99,89,001 (7 digits)</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.4rem; justify-content:center; align-items:center;">
          <button class="sim-btn" id="btnMN_2x3">2-digit × 3-digit</button>
          <button class="sim-btn active" id="btnMN_3x4">3-digit × 4-digit</button>
          <button class="sim-btn" id="btnMN_3x3">3-digit × 3-digit</button>
          <button class="sim-btn" id="btnMN_5x5">5-digit × 5-digit</button>
        </div>
      `;

      function updateMN(newM, newN, smallEx, largeEx) {
        m = newM;
        n = newN;
        document.getElementById('lblCurrentMN').textContent = `Current Test: m = ${m} digits, n = ${n} digits`;
        document.getElementById('lblPossibleLengths').textContent = `${m + n - 1} or ${m + n} digits`;
        document.getElementById('lblSmallestEx').textContent = smallEx;
        document.getElementById('lblLargestEx').textContent = largeEx;
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        sfx.playClick();
      }

      document.getElementById('btnMN_2x3').addEventListener('click', (e) => {
        e.target.classList.add('active');
        updateMN(2, 3, "Smallest: 10 × 100 = 1,000 (4 digits)", "Largest: 99 × 999 = 98,901 (5 digits)");
      });

      document.getElementById('btnMN_3x4').addEventListener('click', (e) => {
        e.target.classList.add('active');
        updateMN(3, 4, "Smallest: 100 × 1,000 = 1,00,000 (6 digits)", "Largest: 999 × 9,999 = 99,89,001 (7 digits)");
      });

      document.getElementById('btnMN_3x3').addEventListener('click', (e) => {
        e.target.classList.add('active');
        updateMN(3, 3, "Smallest: 100 × 100 = 10,000 (5 digits)", "Largest: 999 × 999 = 9,98,001 (6 digits)");
      });

      document.getElementById('btnMN_5x5').addEventListener('click', (e) => {
        e.target.classList.add('active');
        updateMN(5, 5, "Smallest: 10,000 × 10,000 = 10,00,00,000 (9 digits)", "Largest: 99,999 × 99,999 = 9,99,98,00,001 (10 digits)");
      });
    }

    // Slide 14: Fascinating Large Number Trivia
    function simLargeNumbersTrivia() {
      simHeaderTitle.textContent = "Fascinating Large Number Trivia: River Discharge & Cosmic Distances";

      simCanvas.innerHTML = `
        <svg id="triviaSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#020617"/>

          <!-- Dynamic Trivia Group -->
          <g id="triviaDisplayGroup">
            <!-- Populated via script -->
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnTrivPurandara">🎵 Purandaradāsa (4.75 Lakh Songs)</button>
          <button class="sim-btn" id="btnTrivAmazon">🌊 Amazon River Discharge (2 Lakh m³/s)</button>
          <button class="sim-btn" id="btnTrivSun">☀️ Sunlight Travel (15 Crore km)</button>
        </div>
      `;

      function renderTrivia(topic) {
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        const g = document.getElementById('triviaDisplayGroup');

        if (topic === 'purandara') {
          document.getElementById('btnTrivPurandara').classList.add('active');
          g.innerHTML = `
            <text x="270" y="30" fill="#fbbf24" font-size="13" font-weight="800" text-anchor="middle">Saint Purandaradāsa's 4,75,000 Kirtanas</text>
            
            <g transform="translate(40, 55)">
              <rect x="0" y="0" width="460" height="230" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#fbbf24" stroke-width="1.5"/>
              <text x="230" y="30" font-size="28" text-anchor="middle">🪕 📜</text>
              <text x="230" y="65" fill="#f8fafc" font-size="12" font-weight="800" text-anchor="middle">Four Lakh Seventy-Five Thousand Devotional Compositions</text>
              <line x1="20" y1="78" x2="440" y2="78" stroke="rgba(255,255,255,0.1)"/>
              
              <text x="30" y="105" fill="#38bdf8" font-size="10" font-weight="700">• If you sing 10 kirtanas every day without missing a single day:</text>
              <text x="50" y="125" fill="#f8fafc" font-size="10">Days required: 4,75,000 ÷ 10 = 47,500 days!</text>
              
              <text x="30" y="155" fill="#38bdf8" font-size="10" font-weight="700">• In terms of years:</text>
              <text x="50" y="175" fill="#4ade80" font-size="13" font-weight="900">47,500 ÷ 365 = 130.1 Years!</text>

              <rect x="20" y="190" width="420" height="28" rx="6" fill="rgba(245, 158, 11, 0.2)"/>
              <text x="230" y="208" fill="#fde047" font-size="9" font-weight="700" text-anchor="middle">Singing all his songs takes longer than an entire 100-year human life!</text>
            </g>
          `;
        } else if (topic === 'amazon') {
          document.getElementById('btnTrivAmazon').classList.add('active');
          g.innerHTML = `
            <text x="270" y="30" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Amazon River: 2,00,000 m³ of Water Every Single Second</text>
            
            <g transform="translate(40, 55)">
              <rect x="0" y="0" width="460" height="230" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="230" y="30" font-size="28" text-anchor="middle">🌊 🚢</text>
              <text x="230" y="65" fill="#f8fafc" font-size="12" font-weight="800" text-anchor="middle">World's Greatest River Discharge</text>
              <line x1="20" y1="78" x2="440" y2="78" stroke="rgba(255,255,255,0.1)"/>

              <text x="30" y="105" fill="#38bdf8" font-size="10" font-weight="700">• Discharge in 10 seconds: 2,00,000 × 10 = 20,00,000 m³ (20 Lakh m³)</text>
              <text x="30" y="135" fill="#38bdf8" font-size="10" font-weight="700">• Discharge in 1 minute (60 seconds):</text>
              <text x="50" y="155" fill="#4ade80" font-size="13" font-weight="900">2,00,000 × 60 = 1,20,00,000 m³ (1.2 Crore m³!)</text>

              <rect x="20" y="180" width="420" height="38" rx="6" fill="rgba(2, 132, 199, 0.2)"/>
              <text x="230" y="198" fill="#bae6fd" font-size="9" font-weight="700" text-anchor="middle">In just 10 minutes, the Amazon pours 12 Crore cubic metres of fresh water,</text>
              <text x="230" y="211" fill="#bae6fd" font-size="8.5" text-anchor="middle">diluting ocean salinity for over 100 kilometres out into the Atlantic!</text>
            </g>
          `;
        } else if (topic === 'sun') {
          document.getElementById('btnTrivSun').classList.add('active');
          g.innerHTML = `
            <text x="270" y="30" fill="#f59e0b" font-size="13" font-weight="800" text-anchor="middle">Sunlight Travel Time Across 15 Crore Kilometres</text>
            
            <g transform="translate(40, 55)">
              <rect x="0" y="0" width="460" height="230" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#f59e0b" stroke-width="1.5"/>
              <text x="230" y="30" font-size="28" text-anchor="middle">☀️ ⚡ 🌍</text>
              <text x="230" y="65" fill="#f8fafc" font-size="12" font-weight="800" text-anchor="middle">Distance = 14,96,00,000 km (~15 Crore km)</text>
              <line x1="20" y1="78" x2="440" y2="78" stroke="rgba(255,255,255,0.1)"/>

              <text x="30" y="105" fill="#38bdf8" font-size="10" font-weight="700">• Speed of Light: 3,00,000 km/second (3 Lakh km/s)</text>
              <text x="30" y="130" fill="#38bdf8" font-size="10" font-weight="700">• Time = Distance ÷ Speed:</text>
              <text x="50" y="152" fill="#4ade80" font-size="12" font-weight="800">15,00,00,000 ÷ 3,00,000 = 500 seconds</text>

              <rect x="20" y="175" width="420" height="40" rx="6" fill="rgba(245, 158, 11, 0.25)"/>
              <text x="230" y="195" fill="#fde047" font-size="12" font-weight="900" text-anchor="middle">500 seconds = 8 minutes and 20 seconds!</text>
              <text x="230" y="209" fill="#cbd5e1" font-size="8.5" text-anchor="middle">When you look at sunlight, you are seeing photons that left the Sun 8.3 minutes ago!</text>
            </g>
          `;
        }
        sfx.playClick();
      }

      document.getElementById('btnTrivPurandara').addEventListener('click', () => renderTrivia('purandara'));
      document.getElementById('btnTrivAmazon').addEventListener('click', () => renderTrivia('amazon'));
      document.getElementById('btnTrivSun').addEventListener('click', () => renderTrivia('sun'));

      renderTrivia('purandara');
    }

    // Slide 15: Thought Experiment: Fitting Mumbai's Population
    function simMumbaiPopulationBuses() {
      simHeaderTitle.textContent = "Urban Thought Experiment: Transporting 1.25 Crore Citizens";
      const totalPop = 12500000;

      simCanvas.innerHTML = `
        <svg id="busSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

          <!-- Thought Experiment Header -->
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="460" height="60" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.2"/>
            <text x="230" y="24" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">Mumbai Total Population: 1,25,00,000 (1.25 Crore)</text>
            <text id="lblVehicleMode" x="230" y="46" fill="#fbbf24" font-size="12" font-weight="900" text-anchor="middle">Mode: Double-Decker Buses (80 Passengers Each)</text>
          </g>

          <!-- Fleet Calculation Card -->
          <g transform="translate(40, 95)">
            <rect x="0" y="0" width="460" height="200" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5"/>
            
            <text x="25" y="32" fill="#94a3b8" font-size="10" font-weight="700">Fleet Size Required:</text>
            <text id="lblFleetCount" x="25" y="60" fill="#4ade80" font-size="22" font-weight="900">1,56,250 Buses</text>

            <line x1="25" y1="75" x2="435" y2="75" stroke="rgba(255,255,255,0.1)"/>

            <text x="25" y="100" fill="#94a3b8" font-size="10" font-weight="700">Bumper-to-Bumper Convoy Length (at 12m per bus):</text>
            <text id="lblConvoyLength" x="25" y="125" fill="#f8fafc" font-size="15" font-weight="800">1,875 Kilometres!</text>

            <rect x="25" y="140" width="410" height="45" rx="6" fill="rgba(16, 185, 129, 0.2)"/>
            <text id="lblConvoyDesc" x="230" y="160" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">A single line of buses would stretch from Mumbai, through Gujarat & Delhi,</text>
            <text id="lblConvoyDesc2" x="230" y="174" fill="#34d399" font-size="8.5" text-anchor="middle">all the way to the foothills of the Himalayas!</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnVehBus">🚌 Double-Decker Bus (80 pax)</button>
          <button class="sim-btn" id="btnVehTrain">🚆 Suburban Local Train (4,000 pax)</button>
          <button class="sim-btn" id="btnVehShip">🚢 Mega Cruise Liner (3,000 pax)</button>
        </div>
      `;

      function setVehicle(name, cap, desc1, desc2) {
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        const count = Math.ceil(totalPop / cap);
        document.getElementById('lblVehicleMode').textContent = `Mode: ${name} (${cap.toLocaleString()} Passengers Each)`;
        document.getElementById('lblFleetCount').textContent = `${count.toLocaleString('en-IN')} Vehicles`;
        
        if (cap === 80) {
          const km = Math.round(count * 0.012);
          document.getElementById('lblConvoyLength').textContent = `${km.toLocaleString()} Kilometres!`;
        } else if (cap === 4000) {
          const km = Math.round(count * 0.25);
          document.getElementById('lblConvoyLength').textContent = `${km.toLocaleString()} Kilometres of Rail Line!`;
        } else {
          document.getElementById('lblConvoyLength').textContent = `${count.toLocaleString()} Mega-Vessels Required`;
        }

        document.getElementById('lblConvoyDesc').textContent = desc1;
        document.getElementById('lblConvoyDesc2').textContent = desc2;
        sfx.playClick();
      }

      document.getElementById('btnVehBus').addEventListener('click', (e) => {
        e.target.classList.add('active');
        setVehicle("Double-Decker Buses", 80, "A single line of buses would stretch from Mumbai, through Gujarat & Delhi,", "all the way to the foothills of the Himalayas!");
      });

      document.getElementById('btnVehTrain').addEventListener('click', (e) => {
        e.target.classList.add('active');
        setVehicle("Suburban Local 12-Car Trains", 4000, "Mumbai would require 3,125 full 12-car local trains at once!", "The bumper-to-bumper train line would stretch over 780 km.");
      });

      document.getElementById('btnVehShip').addEventListener('click', (e) => {
        e.target.classList.add('active');
        setVehicle("Mega Cruise Liners", 3000, "Requires 4,167 luxury ocean liners holding 3,000 passengers each!", "That is more cruise liners than exist on the entire planet Earth!");
      });
    }

    // Slide 16: Thought Experiment: Journey to the Moon and Sun
    function simJourneyToSunMoon() {
      simHeaderTitle.textContent = "Cosmic Travel Time Calculator: Moon vs. Sun at Different Speeds";
      let destDist = 384400; // Moon
      let destName = "The Moon (3,84,400 km)";

      simCanvas.innerHTML = `
        <svg id="journeySvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#020617"/>

          <!-- Destination Card -->
          <g transform="translate(40, 20)">
            <rect x="0" y="0" width="460" height="55" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.2"/>
            <text id="lblJourneyDest" x="230" y="26" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Destination: The Moon (3,84,400 km)</text>
            <text id="lblTransportSelected" x="230" y="44" fill="#fbbf24" font-size="10" font-weight="700" text-anchor="middle">Transport: Walking (5 km/h)</text>
          </g>

          <!-- Travel Time Results -->
          <g transform="translate(40, 90)">
            <rect x="0" y="0" width="460" height="205" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5"/>
            
            <text x="25" y="32" fill="#94a3b8" font-size="10" font-weight="700">Formula: Time = Distance ÷ Speed</text>
            <line x1="25" y1="42" x2="435" y2="42" stroke="rgba(255,255,255,0.1)"/>

            <text x="25" y="68" fill="#94a3b8" font-size="10">Total Hours Required:</text>
            <text id="lblTimeHours" x="25" y="92" fill="#38bdf8" font-size="18" font-weight="900">76,880 Hours</text>

            <text x="250" y="68" fill="#94a3b8" font-size="10">Total Days Required:</text>
            <text id="lblTimeDays" x="250" y="92" fill="#4ade80" font-size="18" font-weight="900">3,203 Days</text>

            <text x="25" y="125" fill="#94a3b8" font-size="10">Total Years Required:</text>
            <text id="lblTimeYears" x="25" y="155" fill="#f59e0b" font-size="24" font-weight="900">8.78 Years!</text>

            <rect x="25" y="165" width="410" height="30" rx="6" fill="rgba(245, 158, 11, 0.2)"/>
            <text id="lblJourneyNote" x="230" y="184" fill="#fde047" font-size="8.5" font-weight="700" text-anchor="middle">Walking non-stop day and night without stopping to sleep!</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:0.5rem; align-items:center; width:100%;">
          <div style="display:flex; gap:0.6rem; justify-content:center;">
            <button class="sim-btn active" id="btnDestMoon">🌕 Moon (3.84 Lakh km)</button>
            <button class="sim-btn" id="btnDestSun">☀️ Sun (15 Crore km)</button>
          </div>
          <div style="display:flex; flex-wrap:wrap; gap:0.4rem; justify-content:center;">
            <button class="sim-btn active" id="btnSpdWalk">🚶 Walk (5 km/h)</button>
            <button class="sim-btn" id="btnSpdCar">🚗 Car (100 km/h)</button>
            <button class="sim-btn" id="btnSpdTrain">🚆 Bullet Train (300 km/h)</button>
            <button class="sim-btn" id="btnSpdJet">✈️ Jet Plane (1,000 km/h)</button>
            <button class="sim-btn" id="btnSpdRocket">🚀 Rocket (40,000 km/h)</button>
          </div>
        </div>
      `;

      let currentSpeed = 5;
      let currentTransportName = "Walking (5 km/h)";

      function calculateJourney() {
        const hrs = Math.round(destDist / currentSpeed);
        const days = (hrs / 24).toFixed(1);
        const years = (hrs / (24 * 365.25)).toFixed(2);

        document.getElementById('lblJourneyDest').textContent = `Destination: ${destName}`;
        document.getElementById('lblTransportSelected').textContent = `Transport: ${currentTransportName}`;
        document.getElementById('lblTimeHours').textContent = `${hrs.toLocaleString()} Hours`;
        document.getElementById('lblTimeDays').textContent = `${parseFloat(days).toLocaleString()} Days`;
        document.getElementById('lblTimeYears').textContent = `${years} Years!`;

        const note = document.getElementById('lblJourneyNote');
        if (destDist > 100000000 && currentSpeed === 5) {
          note.textContent = "Over 3,425 years! Longer than recorded civilization since the Bronze Age!";
        } else if (destDist > 100000000 && currentSpeed === 1000) {
          note.textContent = "A high-speed jet flying day and night takes over 17 uninterrupted years!";
        } else if (currentSpeed === 40000 && destDist < 1000000) {
          note.textContent = "Apollo astronauts reached the Moon in roughly 3 to 4 days!";
        } else {
          note.textContent = "Assuming constant travel speed without stopping for rest or fuel!";
        }
        sfx.playClick();
      }

      document.getElementById('btnDestMoon').addEventListener('click', (e) => {
        document.getElementById('btnDestMoon').classList.add('active');
        document.getElementById('btnDestSun').classList.remove('active');
        destDist = 384400;
        destName = "The Moon (3,84,400 km)";
        calculateJourney();
      });

      document.getElementById('btnDestSun').addEventListener('click', (e) => {
        document.getElementById('btnDestSun').classList.add('active');
        document.getElementById('btnDestMoon').classList.remove('active');
        destDist = 150000000;
        destName = "The Sun (15,00,00,000 km / 15 Crore km)";
        calculateJourney();
      });

      function setSpeed(spd, name, btnId) {
        currentSpeed = spd;
        currentTransportName = name;
        ['btnSpdWalk', 'btnSpdCar', 'btnSpdTrain', 'btnSpdJet', 'btnSpdRocket'].forEach(id => {
          document.getElementById(id).classList.toggle('active', id === btnId);
        });
        calculateJourney();
      }

      document.getElementById('btnSpdWalk').addEventListener('click', () => setSpeed(5, "Walking (5 km/h)", 'btnSpdWalk'));
      document.getElementById('btnSpdCar').addEventListener('click', () => setSpeed(100, "Highway Car (100 km/h)", 'btnSpdCar'));
      document.getElementById('btnSpdTrain').addEventListener('click', () => setSpeed(300, "Bullet Train (300 km/h)", 'btnSpdTrain'));
      document.getElementById('btnSpdJet').addEventListener('click', () => setSpeed(1000, "Commercial Jet Plane (1,000 km/h)", 'btnSpdJet'));
      document.getElementById('btnSpdRocket').addEventListener('click', () => setSpeed(40000, "Apollo Space Rocket (40,000 km/h)", 'btnSpdRocket'));
    }
"""

