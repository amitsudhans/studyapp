# -*- coding: utf-8 -*-
"""
Interactive SVG Simulators for NCERT Class 7 Mathematics - Chapter 3: A Peek Beyond the Point (Decimals)
Simulators 1 to 16
"""

SIMULATORS_JS = r"""
    // ========================================================
    // 16 BESPOKE INTERACTIVE SVG SIMULATORS (Ch 3 Decimals)
    // ========================================================

    // Slide 1: Need for Smaller Units (Magnifier on Continuous Scale)
    function simNeedForSmallerUnits() {
      simHeaderTitle.textContent = "The Need for Smaller Units: Beyond Whole Markings";
      let activeItem = 0;
      const items = [
        { name: "Carpenter's Wood Screw", wholePart: 2, fracPart: 0.4, label: "2.4 cm (2 cm + 4 mm)" },
        { name: "Pencil Lead Tip", wholePart: 0, fracPart: 0.7, label: "0.7 cm (7 mm)" },
        { name: "Banyan Leaf Stem", wholePart: 3, fracPart: 0.8, label: "3.8 cm (3 cm + 8 mm)" },
        { name: "Golden Beetle Width", wholePart: 1, fracPart: 0.6, label: "1.6 cm (1 cm + 6 mm)" }
      ];

      function render() {
        const itm = items[activeItem];
        const objWidth = (itm.wholePart + itm.fracPart) * 80;

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <defs>
              <linearGradient id="rulerWood" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#fef08a"/>
                <stop offset="100%" stop-color="#ca8a04"/>
              </linearGradient>
            </defs>
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <!-- Header Badge -->
            <rect x="110" y="15" width="320" height="34" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="37" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">Object: ${itm.name}</text>

            <!-- Physical Object to Measure -->
            <g transform="translate(60, 75)">
              <rect x="0" y="0" width="${objWidth}" height="28" rx="6" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
              <text x="${objWidth / 2}" y="19" fill="#0f172a" font-size="11" font-weight="900" text-anchor="middle">${itm.name}</text>

              <!-- Measurement Arrow -->
              <line x1="0" y1="36" x2="${objWidth}" y2="36" stroke="#f59e0b" stroke-width="2"/>
              <polygon points="0,36 8,32 8,40" fill="#f59e0b"/>
              <polygon points="${objWidth},36 ${objWidth - 8},32 ${objWidth - 8},40" fill="#f59e0b"/>
              <text x="${objWidth / 2}" y="52" fill="#fbbf24" font-size="12" font-weight="900" text-anchor="middle">Exact Length = ${itm.label}</text>
            </g>

            <!-- Standard Metric Ruler with Ticks -->
            <g transform="translate(60, 145)">
              <!-- Ruler Body -->
              <rect x="0" y="0" width="420" height="65" rx="4" fill="url(#rulerWood)" stroke="#854d0e" stroke-width="2"/>

              <!-- Centimetre and Millimetre markings (0 to 5 cm) -->
              ${Array.from({ length: 6 }).map((_, cm) => {
                const x = cm * 80;
                return `
                  <!-- Whole CM Mark -->
                  <line x1="${x}" y1="0" x2="${x}" y2="28" stroke="#1e293b" stroke-width="2.5"/>
                  <text x="${x}" y="45" fill="#1e293b" font-size="14" font-weight="900" text-anchor="middle">${cm}</text>
                  ${cm < 5 ? Array.from({ length: 9 }).map((_, mm) => {
                    const mmX = x + (mm + 1) * 8;
                    const h = (mm === 4) ? 18 : 10;
                    return `<line x1="${mmX}" y1="0" x2="${mmX}" y2="${h}" stroke="#334155" stroke-width="${mm === 4 ? 1.5 : 1}"/>`;
                  }).join('') : ''}
                `;
              }).join('')}
              <text x="405" y="58" fill="#451a03" font-size="9" font-weight="800">CENTIMETRES (cm)</text>
            </g>

            <!-- Bottom Insight Card -->
            <rect x="40" y="235" width="460" height="75" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5"/>
            <text x="270" y="258" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">Why Whole Numbers Fall Short:</text>
            <text x="270" y="278" fill="#f8fafc" font-size="13" font-weight="700" text-anchor="middle">This object ends between ${itm.wholePart} cm and ${itm.wholePart + 1} cm marks.</text>
            <text x="270" y="296" fill="#94a3b8" font-size="10.5" text-anchor="middle">Subdividing each 1 cm into 10 tenths (mm) gives the precise measurement: ${itm.label}!</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Choose Object:</span>
          ${items.map((itm, idx) => `<button class="sim-btn ${idx === activeItem ? 'active' : ''}" data-idx="${idx}">${itm.name}</button>`).join('')}
        </div>
      `;

      simControls.querySelectorAll('.sim-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          activeItem = parseInt(btn.dataset.idx);
          simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          render();
          sfx.playClick();
        });
      });

      render();
    }

    // Slide 2: A Tenth Part Strip Visualizer
    function simTenthPartStrip() {
      simHeaderTitle.textContent = "A Tenth Part: Slicing 1 Whole into 10 Equal Strips";
      let count = 4; // 4 tenths selected

      function render() {
        const decimalVal = (count / 10).toFixed(1);
        const fractionVal = `${count}/10`;
        const percentage = count * 10;

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#070d19"/>

            <!-- Header Badge -->
            <rect x="110" y="15" width="320" height="34" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="37" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">
              Value: ${fractionVal} = ${decimalVal} (${percentage}%)
            </text>

            <!-- 1 Whole Bar divided into 10 Strips -->
            <g transform="translate(60, 75)">
              <text x="210" y="15" fill="#94a3b8" font-size="11" font-weight="700" text-anchor="middle">1 WHOLE UNIT DIVIDED INTO 10 EQUAL TENTH STRIPS</text>
              <rect x="0" y="25" width="420" height="70" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="2"/>

              ${Array.from({ length: 10 }).map((_, i) => {
                const isShaded = i < count;
                const fillCol = isShaded ? "#0284c7" : "transparent";
                const borderCol = isShaded ? "#38bdf8" : "#475569";
                return `
                  <rect x="${i * 42}" y="25" width="42" height="70" fill="${fillCol}" stroke="${borderCol}" stroke-width="1.5"/>
                  <text x="${i * 42 + 21}" y="65" fill="${isShaded ? '#ffffff' : '#64748b'}" font-size="12" font-weight="900" text-anchor="middle">0.1</text>
                  <text x="${i * 42 + 21}" y="82" fill="${isShaded ? '#a7f3d0' : '#475569'}" font-size="9" text-anchor="middle">1/10</text>
                `;
              }).join('')}
            </g>

            <!-- Math Equivalence Cards -->
            <g transform="translate(60, 185)">
              <rect x="0" y="0" width="130" height="60" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="65" y="24" fill="#38bdf8" font-size="10" font-weight="800" text-anchor="middle">Tenths Count</text>
              <text x="65" y="48" fill="#ffffff" font-size="18" font-weight="900" text-anchor="middle">${count} tenths</text>

              <rect x="145" y="0" width="130" height="60" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
              <text x="210" y="24" fill="#fbbf24" font-size="10" font-weight="800" text-anchor="middle">Fraction Form</text>
              <text x="210" y="48" fill="#ffffff" font-size="18" font-weight="900" text-anchor="middle">${fractionVal}</text>

              <rect x="290" y="0" width="130" height="60" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
              <text x="355" y="24" fill="#34d399" font-size="10" font-weight="800" text-anchor="middle">Decimal Form</text>
              <text x="355" y="48" fill="#ffffff" font-size="18" font-weight="900" text-anchor="middle">${decimalVal}</text>
            </g>

            <!-- Bottom Takeaway -->
            <rect x="40" y="260" width="460" height="50" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#64748b" stroke-width="1"/>
            <text x="270" y="280" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">Ten tenths ($10 \\times 0.1$) combine together to make exactly 1 whole!</text>
            <text x="270" y="298" fill="#94a3b8" font-size="9.5" text-anchor="middle">The decimal point separates whole numbers from tenths: 0.1, 0.2, 0.3, ... 0.9, 1.0</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.6rem; justify-content:center; align-items:center;">
          <label style="color:#94a3b8; font-size:0.85rem; font-weight:700;">Shaded Tenths (0 to 10): 
            <input type="range" id="rngTenths" min="0" max="10" value="${count}" style="vertical-align:middle; width:150px;">
          </label>
          <button class="sim-btn" id="btnTenthFull">Full Unit (1.0)</button>
          <button class="sim-btn" id="btnTenthHalf">Half Unit (0.5)</button>
          <button class="sim-btn" id="btnTenthReset">Reset (0.0)</button>
        </div>
      `;

      document.getElementById('rngTenths').oninput = (e) => {
        count = parseInt(e.target.value);
        render();
      };
      document.getElementById('btnTenthFull').onclick = () => {
        count = 10;
        document.getElementById('rngTenths').value = 10;
        render(); sfx.playCelebration();
      };
      document.getElementById('btnTenthHalf').onclick = () => {
        count = 5;
        document.getElementById('rngTenths').value = 5;
        render(); sfx.playClick();
      };
      document.getElementById('btnTenthReset').onclick = () => {
        count = 0;
        document.getElementById('rngTenths').value = 0;
        render(); sfx.playClick();
      };

      render();
    }

    // Slide 3: Millimetres & Centimetres Caliper / Ruler
    function simMmCmRuler() {
      simHeaderTitle.textContent = "Metric Ruler: 1 Millimetre = 0.1 Centimetre";
      let mmVal = 28; // 28 mm = 2.8 cm

      function render() {
        const cmVal = (mmVal / 10).toFixed(1);
        const wholeCm = Math.floor(mmVal / 10);
        const remMm = mmVal % 10;
        const arrowX = 60 + (mmVal * 8);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <!-- Display Screen -->
            <rect x="100" y="15" width="340" height="50" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="2"/>
            <text x="270" y="38" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">DIGITAL METRIC CONVERTER</text>
            <text x="270" y="58" fill="#ffffff" font-size="18" font-weight="900" text-anchor="middle">
              ${mmVal} mm = ${cmVal} cm (${wholeCm} cm and ${remMm} mm)
            </text>

            <!-- Detailed Millimetre-Centimetre Ruler -->
            <g transform="translate(60, 95)">
              <rect x="0" y="0" width="420" height="75" rx="6" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>

              <!-- Ticks up to 5 cm (50 mm) -->
              ${Array.from({ length: 6 }).map((_, c) => {
                const x = c * 80;
                return `
                  <line x1="${x}" y1="0" x2="${x}" y2="35" stroke="#1e293b" stroke-width="2.5"/>
                  <text x="${x}" y="55" fill="#1e293b" font-size="15" font-weight="900" text-anchor="middle">${c}</text>
                  ${c < 5 ? Array.from({ length: 9 }).map((_, m) => {
                    const mx = x + (m + 1) * 8;
                    const h = (m === 4) ? 22 : 12;
                    return `<line x1="${mx}" y1="0" x2="${mx}" y2="${h}" stroke="#334155" stroke-width="${m === 4 ? 1.5 : 1}"/>`;
                  }).join('') : ''}
                `;
              }).join('')}
              <text x="405" y="68" fill="#854d0e" font-size="9" font-weight="800">cm</text>
            </g>

            <!-- Pointer Pin Marking the Selected mm -->
            <polygon points="${arrowX},180 ${arrowX - 8},195 ${arrowX + 8},195" fill="#f43f5e"/>
            <line x1="${arrowX}" y1="170" x2="${arrowX}" y2="95" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3 3"/>
            <text x="${arrowX}" y="212" fill="#f43f5e" font-size="12" font-weight="900" text-anchor="middle">${cmVal} cm</text>

            <!-- Bottom Explanation Card -->
            <rect x="50" y="235" width="440" height="75" rx="10" fill="rgba(30, 41, 59, 0.85)" stroke="#10b981" stroke-width="1.5"/>
            <text x="270" y="258" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">Rule: 1 mm = 1/10 cm = 0.1 cm</text>
            <text x="270" y="280" fill="#f8fafc" font-size="14" font-weight="900" text-anchor="middle">${mmVal} mm = ${mmVal} ÷ 10 = ${cmVal} cm</text>
            <text x="270" y="298" fill="#94a3b8" font-size="10" text-anchor="middle">Converting millimetres to centimetres is simply a single decimal division by 10!</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.8rem; justify-content:center; align-items:center;">
          <label style="color:#94a3b8; font-size:0.85rem; font-weight:700;">Length in mm: 
            <input type="range" id="rngMm" min="1" max="50" value="${mmVal}" style="vertical-align:middle; width:160px;">
          </label>
          <button class="sim-btn" data-val="8">8 mm</button>
          <button class="sim-btn" data-val="14">14 mm</button>
          <button class="sim-btn" data-val="36">36 mm</button>
          <button class="sim-btn" data-val="45">45 mm</button>
        </div>
      `;

      document.getElementById('rngMm').oninput = (e) => {
        mmVal = parseInt(e.target.value);
        render();
      };

      simControls.querySelectorAll('[data-val]').forEach(btn => {
        btn.addEventListener('click', () => {
          mmVal = parseInt(btn.dataset.val);
          document.getElementById('rngMm').value = mmVal;
          render();
          sfx.playClick();
        });
      });

      render();
    }

    // Slide 4: A Hundredth Part 100-Grid Matrix
    function simHundredthGrid() {
      simHeaderTitle.textContent = "A Hundredth Part: The 100-Square Matrix (0.01 to 1.00)";
      let hundredthsCount = 37;

      function render() {
        const decVal = (hundredthsCount / 100).toFixed(2);
        const tenths = Math.floor(hundredthsCount / 10);
        const remHund = hundredthsCount % 10;

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#080e1a"/>

            <!-- 10x10 Grid (200x200 px) -->
            <g transform="translate(45, 60)">
              <rect x="0" y="0" width="200" height="200" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
              ${Array.from({ length: 100 }).map((_, i) => {
                const r = Math.floor(i / 10);
                const c = i % 10;
                const isShaded = i < hundredthsCount;
                return `
                  <rect x="${c * 20}" y="${r * 20}" width="20" height="20" fill="${isShaded ? '#0284c7' : 'transparent'}" stroke="${isShaded ? '#38bdf8' : '#334155'}" stroke-width="0.8"/>
                `;
              }).join('')}
            </g>

            <!-- Information & Place Breakdown Panel -->
            <g transform="translate(270, 60)">
              <rect x="0" y="0" width="230" height="200" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="115" y="26" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">HUNDREDTHS MATRIX</text>
              <line x1="15" y1="36" x2="215" y2="36" stroke="rgba(56, 189, 248, 0.3)"/>

              <text x="15" y="60" fill="#94a3b8" font-size="10">Fraction Shaded:</text>
              <text x="15" y="80" fill="#ffffff" font-size="16" font-weight="900">${hundredthsCount} / 100</text>

              <text x="15" y="108" fill="#94a3b8" font-size="10">Decimal Representation:</text>
              <text x="15" y="132" fill="#34d399" font-size="22" font-weight="900">${decVal}</text>

              <rect x="12" y="145" width="206" height="42" rx="6" fill="#1e293b"/>
              <text x="115" y="162" fill="#fbbf24" font-size="10" font-weight="800" text-anchor="middle">Place Breakdown:</text>
              <text x="115" y="178" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">${tenths} Tenths + ${remHund} Hundredths</text>
            </g>

            <!-- Bottom Insight -->
            <rect x="40" y="275" width="460" height="42" rx="8" fill="rgba(30, 41, 59, 0.85)" stroke="#64748b" stroke-width="1"/>
            <text x="270" y="295" fill="#cbd5e1" font-size="10.5" font-weight="700" text-anchor="middle">10 hundredths = 1 tenth (0.10 = 0.1). 100 hundredths = 1 whole (1.00 = 1).</text>
            <text x="270" y="309" fill="#38bdf8" font-size="9.5" text-anchor="middle">The second place after the dot represents hundredths (1/100).</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.6rem; justify-content:center; align-items:center;">
          <label style="color:#94a3b8; font-size:0.85rem; font-weight:700;">Shaded Hundredths (0 to 100): 
            <input type="range" id="rngHund" min="0" max="100" value="${hundredthsCount}" style="vertical-align:middle; width:150px;">
          </label>
          <button class="sim-btn" data-v="10">10 (0.10)</button>
          <button class="sim-btn" data-v="25">25 (0.25)</button>
          <button class="sim-btn" data-v="50">50 (0.50)</button>
          <button class="sim-btn" data-v="75">75 (0.75)</button>
        </div>
      `;

      document.getElementById('rngHund').oninput = (e) => {
        hundredthsCount = parseInt(e.target.value);
        render();
      };

      simControls.querySelectorAll('[data-v]').forEach(btn => {
        btn.addEventListener('click', () => {
          hundredthsCount = parseInt(btn.dataset.v);
          document.getElementById('rngHund').value = hundredthsCount;
          render();
          sfx.playClick();
        });
      });

      render();
    }

    // Slide 5: Rupees and Paise Currency Piggy Bank
    function simRupeesPaiseCurrency() {
      simHeaderTitle.textContent = "Rupees and Paise: 1 Paisa = ₹0.01 (Hundredths in Currency)";
      let totalPaise = 85;

      function render() {
        const rupeesStr = (totalPaise / 100).toFixed(2);
        const wholeRupees = Math.floor(totalPaise / 100);
        const paisePart = totalPaise % 100;

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <!-- Piggy Bank / Wallet Display Card -->
            <g transform="translate(60, 20)">
              <rect x="0" y="0" width="420" height="90" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#fbbf24" stroke-width="2"/>
              <text x="210" y="28" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">INDIAN DECIMAL CURRENCY BANK</text>

              <text x="210" y="58" fill="#ffffff" font-size="26" font-weight="900" text-anchor="middle">₹ ${rupeesStr}</text>
              <text x="210" y="78" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">
                = ${totalPaise} Paise (${wholeRupees} Rupee${wholeRupees === 1 ? '' : 's'} and ${paisePart} Paise)
              </text>
            </g>

            <!-- Coins Showcase -->
            <g transform="translate(60, 125)">
              <rect x="0" y="0" width="420" height="105" rx="10" fill="rgba(30, 41, 59, 0.7)" stroke="#64748b" stroke-width="1.5"/>
              <text x="210" y="22" fill="#94a3b8" font-size="11" font-weight="700" text-anchor="middle">Tap Coins to Add to Balance (1 Rupee = 100 Paise):</text>

              <!-- Coin 5p -->
              <circle cx="50" cy="62" r="22" fill="#713f12" stroke="#eab308" stroke-width="2"/>
              <text x="50" y="66" fill="#fef08a" font-size="11" font-weight="900" text-anchor="middle">5p</text>
              <text x="50" y="96" fill="#94a3b8" font-size="8" text-anchor="middle">₹0.05</text>

              <!-- Coin 10p -->
              <circle cx="130" cy="62" r="23" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
              <text x="130" y="66" fill="#f8fafc" font-size="11" font-weight="900" text-anchor="middle">10p</text>
              <text x="130" y="96" fill="#94a3b8" font-size="8" text-anchor="middle">₹0.10</text>

              <!-- Coin 25p -->
              <circle cx="210" cy="62" r="24" fill="#0f766e" stroke="#2dd4bf" stroke-width="2"/>
              <text x="210" y="66" fill="#ccfbf1" font-size="11" font-weight="900" text-anchor="middle">25p</text>
              <text x="210" y="96" fill="#94a3b8" font-size="8" text-anchor="middle">₹0.25</text>

              <!-- Coin 50p -->
              <circle cx="290" cy="62" r="25" fill="#1d4ed8" stroke="#60a5fa" stroke-width="2"/>
              <text x="290" y="66" fill="#dbeafe" font-size="11" font-weight="900" text-anchor="middle">50p</text>
              <text x="290" y="96" fill="#94a3b8" font-size="8" text-anchor="middle">₹0.50</text>

              <!-- Coin ₹1 -->
              <circle cx="370" cy="62" r="26" fill="#b45309" stroke="#fbbf24" stroke-width="2.5"/>
              <text x="370" y="66" fill="#fef08a" font-size="12" font-weight="900" text-anchor="middle">₹1</text>
              <text x="370" y="96" fill="#94a3b8" font-size="8" text-anchor="middle">100p</text>
            </g>

            <!-- Warning Card on 5p vs 50p -->
            <rect x="40" y="245" width="460" height="65" rx="8" fill="rgba(239, 68, 68, 0.12)" stroke="#ef4444" stroke-width="1"/>
            <text x="270" y="268" fill="#f87171" font-size="11" font-weight="800" text-anchor="middle">⚠️ Beware the Single-Digit Trap!</text>
            <text x="270" y="286" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">5 paise = ₹0.05 (5 hundredths). Writing ₹0.5 means 50 paise (5 tenths)!</text>
            <text x="270" y="302" fill="#94a3b8" font-size="9.5" text-anchor="middle">Always use two decimal places for paise: ₹1.05 ≠ ₹1.50</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn" id="btnAdd5">+ 5p</button>
          <button class="sim-btn" id="btnAdd10">+ 10p</button>
          <button class="sim-btn" id="btnAdd25">+ 25p</button>
          <button class="sim-btn" id="btnAdd50">+ 50p</button>
          <button class="sim-btn" id="btnAdd100">+ ₹1 (100p)</button>
          <button class="sim-btn" id="btnCoinReset" style="border-color:#ef4444; color:#fca5a5;">Reset</button>
        </div>
      `;

      document.getElementById('btnAdd5').onclick = () => { totalPaise += 5; render(); sfx.playClick(); };
      document.getElementById('btnAdd10').onclick = () => { totalPaise += 10; render(); sfx.playClick(); };
      document.getElementById('btnAdd25').onclick = () => { totalPaise += 25; render(); sfx.playClick(); };
      document.getElementById('btnAdd50').onclick = () => { totalPaise += 50; render(); sfx.playClick(); };
      document.getElementById('btnAdd100').onclick = () => { totalPaise += 100; render(); sfx.playCelebration(); };
      document.getElementById('btnCoinReset').onclick = () => { totalPaise = 0; render(); sfx.playClick(); };

      render();
    }

    // Slide 6: Decimal Place Value Matrix Table
    function simDecimalPlaceValueMatrix() {
      simHeaderTitle.textContent = "The Base-10 Place Value Matrix: Tens, Ones, Tenths, Hundredths";
      let activePreset = 0;
      const presets = [
        { label: "253.48", h: 2, t: 5, o: 3, th: 4, hth: 8, mth: 0 },
        { label: "47.382", h: 0, t: 4, o: 7, th: 3, hth: 8, mth: 2 },
        { label: "8.05", h: 0, t: 0, o: 8, th: 0, hth: 5, mth: 0 },
        { label: "105.7", h: 1, t: 0, o: 5, th: 7, hth: 0, mth: 0 }
      ];

      function render() {
        const p = presets[activePreset];

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#070d19"/>

            <!-- Header Badge -->
            <rect x="120" y="15" width="300" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="38" fill="#38bdf8" font-size="14" font-weight="900" text-anchor="middle">Number: ${p.label}</text>

            <!-- Matrix Columns -->
            <g transform="translate(35, 70)">
              <!-- Hundreds -->
              <rect x="0" y="0" width="70" height="120" rx="8" fill="#0f172a" stroke="#64748b"/>
              <text x="35" y="22" fill="#94a3b8" font-size="9" font-weight="800" text-anchor="middle">HUNDREDS</text>
              <text x="35" y="36" fill="#64748b" font-size="8" text-anchor="middle">(100)</text>
              <text x="35" y="80" fill="#ffffff" font-size="28" font-weight="900" text-anchor="middle">${p.h}</text>
              <text x="35" y="105" fill="#38bdf8" font-size="9" text-anchor="middle">${p.h * 100}</text>

              <!-- Tens -->
              <rect x="75" y="0" width="70" height="120" rx="8" fill="#0f172a" stroke="#64748b"/>
              <text x="110" y="22" fill="#94a3b8" font-size="9" font-weight="800" text-anchor="middle">TENS</text>
              <text x="110" y="36" fill="#64748b" font-size="8" text-anchor="middle">(10)</text>
              <text x="110" y="80" fill="#ffffff" font-size="28" font-weight="900" text-anchor="middle">${p.t}</text>
              <text x="110" y="105" fill="#38bdf8" font-size="9" text-anchor="middle">${p.t * 10}</text>

              <!-- Ones -->
              <rect x="150" y="0" width="70" height="120" rx="8" fill="#0f172a" stroke="#64748b"/>
              <text x="185" y="22" fill="#94a3b8" font-size="9" font-weight="800" text-anchor="middle">ONES</text>
              <text x="185" y="36" fill="#64748b" font-size="8" text-anchor="middle">(1)</text>
              <text x="185" y="80" fill="#ffffff" font-size="28" font-weight="900" text-anchor="middle">${p.o}</text>
              <text x="185" y="105" fill="#38bdf8" font-size="9" text-anchor="middle">${p.o * 1}</text>

              <!-- DECIMAL POINT -->
              <circle cx="235" cy="80" r="7" fill="#f43f5e"/>
              <text x="235" y="105" fill="#f43f5e" font-size="9" font-weight="900" text-anchor="middle">DOT</text>

              <!-- Tenths -->
              <rect x="250" y="0" width="70" height="120" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
              <text x="285" y="22" fill="#38bdf8" font-size="9" font-weight="800" text-anchor="middle">TENTHS</text>
              <text x="285" y="36" fill="#94a3b8" font-size="8" text-anchor="middle">(1/10)</text>
              <text x="285" y="80" fill="#38bdf8" font-size="28" font-weight="900" text-anchor="middle">${p.th}</text>
              <text x="285" y="105" fill="#a7f3d0" font-size="9" text-anchor="middle">${(p.th * 0.1).toFixed(1)}</text>

              <!-- Hundredths -->
              <rect x="325" y="0" width="70" height="120" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
              <text x="360" y="22" fill="#fbbf24" font-size="9" font-weight="800" text-anchor="middle">HUNDREDTHS</text>
              <text x="360" y="36" fill="#94a3b8" font-size="8" text-anchor="middle">(1/100)</text>
              <text x="360" y="80" fill="#fbbf24" font-size="28" font-weight="900" text-anchor="middle">${p.hth}</text>
              <text x="360" y="105" fill="#a7f3d0" font-size="9" text-anchor="middle">${(p.hth * 0.01).toFixed(2)}</text>

              <!-- Thousandths -->
              <rect x="400" y="0" width="70" height="120" rx="8" fill="#0f172a" stroke="#64748b"/>
              <text x="435" y="22" fill="#94a3b8" font-size="8" font-weight="800" text-anchor="middle">THOUSANDTHS</text>
              <text x="435" y="36" fill="#64748b" font-size="8" text-anchor="middle">(1/1000)</text>
              <text x="435" y="80" fill="#ffffff" font-size="28" font-weight="900" text-anchor="middle">${p.mth}</text>
              <text x="435" y="105" fill="#38bdf8" font-size="9" text-anchor="middle">${(p.mth * 0.001).toFixed(3)}</text>
            </g>

            <!-- Aryabhata's Law Banner -->
            <rect x="35" y="215" width="470" height="95" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5"/>
            <text x="270" y="240" fill="#34d399" font-size="12" font-weight="900" text-anchor="middle">Acharya Aryabhata's Law: Sthanam Sthanam Dasha Gunam Syat</text>
            <text x="270" y="265" fill="#f8fafc" font-size="11.5" font-weight="700" text-anchor="middle">
              Moving Left ➔ Multiplies by 10 (÷10 ➔ ×1 ➔ ×10 ➔ ×100)
            </text>
            <text x="270" y="285" fill="#38bdf8" font-size="11.5" font-weight="700" text-anchor="middle">
              Moving Right ➔ Divides by 10 (×100 ➔ ×10 ➔ ×1 ➔ ÷10 ➔ ÷100 ➔ ÷1000)
            </text>
            <text x="270" y="302" fill="#94a3b8" font-size="9" text-anchor="middle">The decimal point marks the sacred boundary between whole units and fractional subdivisions.</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Select Number:</span>
          ${presets.map((p, idx) => `<button class="sim-btn ${idx === activePreset ? 'active' : ''}" data-idx="${idx}">${p.label}</button>`).join('')}
        </div>
      `;

      simControls.querySelectorAll('.sim-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          activePreset = parseInt(btn.dataset.idx);
          simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          render();
          sfx.playClick();
        });
      });

      render();
    }

    // Slide 7: Expanded Form & Trailing Zeroes Invariance
    function simExpandedFormTrailingZeroes() {
      simHeaderTitle.textContent = "Expanded Notation & Trailing Zeroes Invariance (0.4 = 0.40 = 0.400)";
      let trailingMode = 0; // 0: 0.4, 1: 0.40, 2: 0.400

      function render() {
        const valStr = trailingMode === 0 ? "0.4" : (trailingMode === 1 ? "0.40" : "0.400");
        const shadedPercent = 40;

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <!-- Value Display -->
            <rect x="140" y="15" width="260" height="40" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="41" fill="#38bdf8" font-size="18" font-weight="900" text-anchor="middle">Decimal: ${valStr}</text>

            <!-- Visual Bar Representation -->
            <g transform="translate(60, 75)">
              <text x="210" y="18" fill="#94a3b8" font-size="11" font-weight="700" text-anchor="middle">Physical Area Shaded Remains Exactly Identical (40%):</text>
              <rect x="0" y="28" width="420" height="50" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
              <rect x="0" y="28" width="${420 * 0.4}" height="50" rx="6" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="${(420 * 0.4) / 2}" y="58" fill="#ffffff" font-size="14" font-weight="900" text-anchor="middle">40% Shaded</text>
            </g>

            <!-- Equivalence Formula Cards -->
            <g transform="translate(60, 170)">
              <rect x="0" y="0" width="130" height="65" rx="8" fill="#0f172a" stroke="${trailingMode === 0 ? '#38bdf8' : '#475569'}" stroke-width="${trailingMode === 0 ? 2 : 1}"/>
              <text x="65" y="24" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">Tenths Form</text>
              <text x="65" y="46" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">4/10 = 0.4</text>

              <rect x="145" y="0" width="130" height="65" rx="8" fill="#0f172a" stroke="${trailingMode === 1 ? '#fbbf24' : '#475569'}" stroke-width="${trailingMode === 1 ? 2 : 1}"/>
              <text x="210" y="24" fill="#fbbf24" font-size="11" font-weight="800" text-anchor="middle">Hundredths Form</text>
              <text x="210" y="46" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">40/100 = 0.40</text>

              <rect x="290" y="0" width="130" height="65" rx="8" fill="#0f172a" stroke="${trailingMode === 2 ? '#10b981' : '#475569'}" stroke-width="${trailingMode === 2 ? 2 : 1}"/>
              <text x="355" y="24" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">Thousandths Form</text>
              <text x="355" y="46" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">400/1000 = 0.400</text>
            </g>

            <!-- Takeaway Banner -->
            <rect x="40" y="250" width="460" height="65" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5"/>
            <text x="270" y="272" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">The Trailing Zeroes Invariance Law:</text>
            <text x="270" y="292" fill="#f8fafc" font-size="14" font-weight="900" text-anchor="middle">0.4 = 0.40 = 0.400 (Equal Quantities!)</text>
            <text x="270" y="306" fill="#94a3b8" font-size="9" text-anchor="middle">Adding zeroes to the end of a decimal does NOT multiply by 10; it only re-expresses it in smaller slices!</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; gap:1rem; justify-content:center; align-items:center;">
          <button class="sim-btn ${trailingMode === 0 ? 'active' : ''}" id="btnTrail0">View 0.4 (Tenths)</button>
          <button class="sim-btn ${trailingMode === 1 ? 'active' : ''}" id="btnTrail1">View 0.40 (Hundredths)</button>
          <button class="sim-btn ${trailingMode === 2 ? 'active' : ''}" id="btnTrail2">View 0.400 (Thousandths)</button>
        </div>
      `;

      document.getElementById('btnTrail0').onclick = () => { trailingMode = 0; render(); sfx.playClick(); };
      document.getElementById('btnTrail1').onclick = () => { trailingMode = 1; render(); sfx.playClick(); };
      document.getElementById('btnTrail2').onclick = () => { trailingMode = 2; render(); sfx.playClick(); };

      render();
    }

    // Slide 8: Metric Length Ladder Converter (mm, cm, m, km)
    function simMetricLengthConverter() {
      simHeaderTitle.textContent = "Metric Length Ladder: Power-of-10 Decimal Shifts";
      let val = 2450; // default in mm or cm

      function render() {
        const mm = val;
        const cm = (val / 10).toFixed(2);
        const m = (val / 1000).toFixed(3);
        const km = (val / 1000000).toFixed(6);

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#070d19"/>

            <!-- Metric Ladder Steps -->
            <g transform="translate(50, 30)">
              <!-- Millimetres -->
              <rect x="0" y="180" width="100" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
              <text x="50" y="202" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">Millimetres (mm)</text>
              <text x="50" y="225" fill="#ffffff" font-size="13" font-weight="900" text-anchor="middle">${mm} mm</text>

              <!-- Arrow /10 -->
              <text x="120" y="165" fill="#fbbf24" font-size="11" font-weight="900" text-anchor="middle">÷ 10 ➔</text>

              <!-- Centimetres -->
              <rect x="140" y="130" width="100" height="60" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
              <text x="190" y="152" fill="#fbbf24" font-size="11" font-weight="800" text-anchor="middle">Centimetres (cm)</text>
              <text x="190" y="175" fill="#ffffff" font-size="13" font-weight="900" text-anchor="middle">${cm} cm</text>

              <!-- Arrow /100 -->
              <text x="260" y="115" fill="#34d399" font-size="11" font-weight="900" text-anchor="middle">÷ 100 ➔</text>

              <!-- Metres -->
              <rect x="280" y="80" width="100" height="60" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
              <text x="330" y="102" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">Metres (m)</text>
              <text x="330" y="125" fill="#ffffff" font-size="13" font-weight="900" text-anchor="middle">${m} m</text>

              <!-- Arrow /1000 -->
              <text x="400" y="65" fill="#a855f7" font-size="11" font-weight="900" text-anchor="middle">÷ 1000 ➔</text>

              <!-- Kilometres -->
              <rect x="420" y="30" width="90" height="60" rx="8" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
              <text x="465" y="52" fill="#c084fc" font-size="10" font-weight="800" text-anchor="middle">Kilometres (km)</text>
              <text x="465" y="75" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">${km} km</text>
            </g>

            <!-- Output Summary Box -->
            <rect x="50" y="255" width="440" height="65" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="278" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Seamless Metric Conversions via Decimal Point Movement:</text>
            <text x="270" y="300" fill="#f8fafc" font-size="14" font-weight="900" text-anchor="middle">
              ${mm} mm = ${cm} cm = ${m} m
            </text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Preset Measurements:</span>
          <button class="sim-btn" data-v="850">850 mm</button>
          <button class="sim-btn active" data-v="2450">2,450 mm</button>
          <button class="sim-btn" data-v="15000">15,000 mm</button>
          <button class="sim-btn" data-v="350000">3,50,000 mm</button>
        </div>
      `;

      simControls.querySelectorAll('.sim-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          val = parseInt(btn.dataset.v);
          simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          render();
          sfx.playClick();
        });
      });

      render();
    }

    // Slide 9: Mass & Capacity Laboratory Scale & Cylinder
    function simMassCapacityScales() {
      simHeaderTitle.textContent = "Mass & Capacity: Grams to Kilograms, Millilitres to Litres (Thousandths)";
      let mode = "mass"; // "mass" or "capacity"
      let val = 450; // grams or mL

      function render() {
        if (mode === "mass") {
          const kgStr = (val / 1000).toFixed(3);
          simCanvas.innerHTML = `
            <svg viewBox="0 0 540 330" width="100%" height="100%">
              <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

              <rect x="110" y="15" width="320" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#fbbf24" stroke-width="1.5"/>
              <text x="270" y="38" fill="#fbbf24" font-size="13" font-weight="900" text-anchor="middle">DIGITAL LABORATORY BALANCE (MASS)</text>

              <!-- Digital Scale Graphic -->
              <g transform="translate(140, 75)">
                <!-- Weighing Pan -->
                <rect x="30" y="0" width="200" height="15" rx="4" fill="#94a3b8" stroke="#f8fafc" stroke-width="1.5"/>
                <!-- Item on Pan -->
                <circle cx="130" cy="-25" r="24" fill="#10b981" stroke="#34d399" stroke-width="2"/>
                <text x="130" y="-20" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">${val} g</text>

                <!-- Base Body -->
                <path d="M 10,15 L 250,15 L 230,130 L 30,130 Z" fill="#1e293b" stroke="#475569" stroke-width="2"/>

                <!-- LCD Display Screen -->
                <rect x="50" y="45" width="160" height="55" rx="8" fill="#022c22" stroke="#10b981" stroke-width="2"/>
                <text x="130" y="80" fill="#34d399" font-size="22" font-weight="900" text-anchor="middle">${kgStr} kg</text>
                <text x="130" y="94" fill="#a7f3d0" font-size="9" text-anchor="middle">(${val} grams)</text>
              </g>

              <!-- Formula Box -->
              <rect x="50" y="235" width="440" height="75" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5"/>
              <text x="270" y="258" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">Mass Rule: 1 kg = 1000 g ➔ 1 g = 1/1000 kg = 0.001 kg</text>
              <text x="270" y="280" fill="#ffffff" font-size="14" font-weight="900" text-anchor="middle">${val} g = ${val} ÷ 1000 = ${kgStr} kg</text>
              <text x="270" y="298" fill="#94a3b8" font-size="10" text-anchor="middle">Notice three decimal places: 5 g = 0.005 kg, 50 g = 0.050 kg, 500 g = 0.500 kg!</text>
            </svg>
          `;
        } else {
          // Capacity: mL to L
          const lStr = (val / 1000).toFixed(3);
          simCanvas.innerHTML = `
            <svg viewBox="0 0 540 330" width="100%" height="100%">
              <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

              <rect x="110" y="15" width="320" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="270" y="38" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">GRADUATED CYLINDER (CAPACITY)</text>

              <!-- Measuring Cylinder Graphic -->
              <g transform="translate(190, 65)">
                <!-- Glass Cylinder -->
                <rect x="0" y="0" width="80" height="150" rx="4" fill="rgba(56, 189, 248, 0.1)" stroke="#38bdf8" stroke-width="2"/>
                <!-- Liquid Fill -->
                <rect x="2" y="${150 - (val / 1000) * 140}" width="76" height="${(val / 1000) * 140}" fill="#0284c7" opacity="0.8"/>
                <!-- Cylinder Ticks -->
                <line x1="60" y1="30" x2="80" y2="30" stroke="#ffffff" stroke-width="1.5"/>
                <text x="50" y="34" fill="#ffffff" font-size="9">750</text>
                <line x1="60" y1="75" x2="80" y2="75" stroke="#ffffff" stroke-width="1.5"/>
                <text x="50" y="79" fill="#ffffff" font-size="9">500</text>
                <line x1="60" y1="115" x2="80" y2="115" stroke="#ffffff" stroke-width="1.5"/>
                <text x="50" y="119" fill="#ffffff" font-size="9">250</text>

                <!-- Value Callout -->
                <rect x="100" y="45" width="150" height="60" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
                <text x="175" y="70" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">${val} mL</text>
                <text x="175" y="92" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">= ${lStr} L</text>
              </g>

              <rect x="50" y="235" width="440" height="75" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5"/>
              <text x="270" y="258" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Capacity Rule: 1 L = 1000 mL ➔ 1 mL = 1/1000 L = 0.001 L</text>
              <text x="270" y="280" fill="#ffffff" font-size="14" font-weight="900" text-anchor="middle">${val} mL = ${val} ÷ 1000 = ${lStr} Litres</text>
              <text x="270" y="298" fill="#94a3b8" font-size="10" text-anchor="middle">Volume in litres directly corresponds to thousandths of a litre!</text>
            </svg>
          `;
        }
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.6rem; justify-content:center; align-items:center;">
          <button class="sim-btn ${mode === 'mass' ? 'active' : ''}" id="btnMassMode">⚖️ Mass (g ➔ kg)</button>
          <button class="sim-btn ${mode === 'capacity' ? 'active' : ''}" id="btnCapMode">🧪 Capacity (mL ➔ L)</button>
          <span style="color:#94a3b8; font-size:0.85rem; font-weight:700; margin-left:0.5rem;">Amount:</span>
          <button class="sim-btn" data-v="5">5</button>
          <button class="sim-btn" data-v="75">75</button>
          <button class="sim-btn active" data-v="450">450</button>
          <button class="sim-btn" data-v="825">825</button>
        </div>
      `;

      document.getElementById('btnMassMode').onclick = () => { mode = "mass"; render(); sfx.playClick(); };
      document.getElementById('btnCapMode').onclick = () => { mode = "capacity"; render(); sfx.playClick(); };

      simControls.querySelectorAll('[data-v]').forEach(btn => {
        btn.addEventListener('click', () => {
          val = parseInt(btn.dataset.v);
          simControls.querySelectorAll('[data-v]').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          render();
          sfx.playClick();
        });
      });

      render();
    }

    // Slide 10: Number Line Zoomable Locator
    function simNumberLineZoom() {
      simHeaderTitle.textContent = "Locating Decimals on the Number Line: Infinite Zoom";
      let zoomLevel = 1; // 1: 0 to 3 wholes, 2: 1 to 2 tenths, 3: 1.4 to 1.5 hundredths

      function render() {
        let lineSvg = "";
        let desc = "";

        if (zoomLevel === 1) {
          // Whole numbers 0, 1, 2, 3
          desc = "Level 1: Whole Number View (0 to 3). Target decimal: 1.4 lies between 1 and 2.";
          lineSvg = `
            <line x1="40" y1="90" x2="480" y2="90" stroke="#64748b" stroke-width="3"/>
            ${[0, 1, 2, 3].map((w, i) => {
              const x = 50 + i * 140;
              return `
                <line x1="${x}" y1="75" x2="${x}" y2="105" stroke="#38bdf8" stroke-width="2.5"/>
                <text x="${x}" y="125" fill="#f8fafc" font-size="16" font-weight="900" text-anchor="middle">${w}</text>
              `;
            }).join('')}

            <!-- Highlight interval 1 to 2 -->
            <rect x="185" y="70" width="150" height="40" rx="8" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-dasharray="4"/>
            <text x="260" y="60" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">🔍 Click 'Zoom to Tenths' Below</text>
          `;
        } else if (zoomLevel === 2) {
          // Tenths view between 1.0 and 2.0
          desc = "Level 2: Tenths Magnification (1.0 to 2.0). 1.4 is 4 ticks to the right of 1.0!";
          lineSvg = `
            <line x1="40" y1="90" x2="480" y2="90" stroke="#64748b" stroke-width="3"/>
            ${Array.from({ length: 11 }).map((_, i) => {
              const x = 50 + i * 42;
              const val = (1.0 + i * 0.1).toFixed(1);
              const isTarget = (i === 4);
              return `
                <line x1="${x}" y1="${isTarget ? '65' : '75'}" x2="${x}" y2="${isTarget ? '115' : '105'}" stroke="${isTarget ? '#f43f5e' : '#38bdf8'}" stroke-width="${isTarget ? 3 : 1.5}"/>
                <text x="${x}" y="128" fill="${isTarget ? '#f43f5e' : '#cbd5e1'}" font-size="${isTarget ? '13' : '10'}" font-weight="${isTarget ? '900' : '700'}" text-anchor="middle">${val}</text>
                ${isTarget ? `
                  <circle cx="${x}" cy="50" r="12" fill="#f43f5e"/>
                  <text x="${x}" y="55" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">📍</text>
                  <text x="${x}" y="32" fill="#f43f5e" font-size="12" font-weight="900" text-anchor="middle">1.4 TARGET</text>
                ` : ''}
              `;
            }).join('')}
          `;
        } else {
          // Hundredths view between 1.40 and 1.50
          desc = "Level 3: Hundredths Super-Zoom (1.40 to 1.50). Locating 1.47!";
          lineSvg = `
            <line x1="40" y1="90" x2="480" y2="90" stroke="#64748b" stroke-width="3"/>
            ${Array.from({ length: 11 }).map((_, i) => {
              const x = 50 + i * 42;
              const val = (1.40 + i * 0.01).toFixed(2);
              const isTarget = (i === 7);
              return `
                <line x1="${x}" y1="${isTarget ? '65' : '75'}" x2="${x}" y2="${isTarget ? '115' : '105'}" stroke="${isTarget ? '#10b981' : '#fbbf24'}" stroke-width="${isTarget ? 3 : 1.5}"/>
                <text x="${x}" y="128" fill="${isTarget ? '#34d399' : '#cbd5e1'}" font-size="${isTarget ? '12' : '9.5'}" font-weight="${isTarget ? '900' : '700'}" text-anchor="middle">${val}</text>
                ${isTarget ? `
                  <circle cx="${x}" cy="50" r="12" fill="#10b981"/>
                  <text x="${x}" y="55" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">📍</text>
                  <text x="${x}" y="32" fill="#34d399" font-size="12" font-weight="900" text-anchor="middle">1.47 TARGET</text>
                ` : ''}
              `;
            }).join('')}
          `;
        }

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#080e1a"/>

            <rect x="90" y="15" width="360" height="34" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="37" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">Magnification Level ${zoomLevel} of 3</text>

            <!-- Dynamic SVG Number Line -->
            ${lineSvg}

            <!-- Explanation Card -->
            <rect x="40" y="230" width="460" height="80" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="255" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">${desc}</text>
            <text x="270" y="278" fill="#f8fafc" font-size="11" text-anchor="middle">Every decimal has an exact geographic address on the number line.</text>
            <text x="270" y="296" fill="#94a3b8" font-size="9.5" text-anchor="middle">Subdividing by 10 continuously uncovers tenths, hundredths, thousandths...</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; gap:1rem; justify-content:center; align-items:center;">
          <button class="sim-btn ${zoomLevel === 1 ? 'active' : ''}" id="btnZoom1">1. Wholes (0 to 3)</button>
          <button class="sim-btn ${zoomLevel === 2 ? 'active' : ''}" id="btnZoom2">2. Zoom Tenths (1.0 - 2.0)</button>
          <button class="sim-btn ${zoomLevel === 3 ? 'active' : ''}" id="btnZoom3">3. Super-Zoom (1.40 - 1.50)</button>
        </div>
      `;

      document.getElementById('btnZoom1').onclick = () => { zoomLevel = 1; render(); sfx.playClick(); };
      document.getElementById('btnZoom2').onclick = () => { zoomLevel = 2; render(); sfx.playClick(); };
      document.getElementById('btnZoom3').onclick = () => { zoomLevel = 3; render(); sfx.playCelebration(); };

      render();
    }

    // Slide 11: Comparing Decimals Duel Balance
    function simComparingDecimalsDuel() {
      simHeaderTitle.textContent = "Comparing Decimals: Place-by-Place Duel (Whole, Tenths, Hundredths)";
      let activeDuel = 0;
      const duels = [
        { numA: "0.8", padA: "0.80", numB: "0.75", padB: "0.75", winner: "A", reason: "8 Tenths > 7 Tenths (0.80 > 0.75)" },
        { numA: "3.45", padA: "3.45", numB: "3.4", padB: "3.40", winner: "A", reason: "Same wholes & tenths, but 5 hundredths > 0 hundredths" },
        { numA: "6.1", padA: "6.100", numB: "4.999", padB: "4.999", winner: "A", reason: "Whole parts duel: 6 > 4 (Immediate victory for 6.1!)" },
        { numA: "1.2", padA: "1.20", numB: "1.20", padB: "1.20", winner: "Equal", reason: "Trailing zero invariance: 1.2 and 1.20 are exactly identical" }
      ];

      function render() {
        const d = duels[activeDuel];
        const statusColor = d.winner === "A" ? "#38bdf8" : (d.winner === "B" ? "#fbbf24" : "#10b981");
        const symbol = d.winner === "A" ? ">" : (d.winner === "B" ? "<" : "=");

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <!-- Main Comparison Verdict Badge -->
            <rect x="130" y="15" width="280" height="42" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="${statusColor}" stroke-width="2"/>
            <text x="270" y="42" fill="${statusColor}" font-size="20" font-weight="900" text-anchor="middle">
              ${d.numA}  ${symbol}  ${d.numB}
            </text>

            <!-- Side-by-Side Comparison Cards -->
            <g transform="translate(45, 75)">
              <!-- Card A -->
              <rect x="0" y="0" width="210" height="130" rx="10" fill="rgba(56, 189, 248, 0.1)" stroke="#38bdf8" stroke-width="2"/>
              <text x="105" y="24" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">DECIMAL A</text>
              <text x="105" y="60" fill="#ffffff" font-size="28" font-weight="900" text-anchor="middle">${d.numA}</text>
              <rect x="25" y="80" width="160" height="34" rx="6" fill="#0f172a" stroke="#38bdf8"/>
              <text x="105" y="102" fill="#7dd3fc" font-size="11" font-weight="700" text-anchor="middle">Padded: ${d.padA}</text>

              <!-- VS Badge -->
              <circle cx="225" cy="65" r="16" fill="#f59e0b"/>
              <text x="225" y="70" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">VS</text>

              <!-- Card B -->
              <rect x="240" y="0" width="210" height="130" rx="10" fill="rgba(245, 158, 11, 0.1)" stroke="#fbbf24" stroke-width="2"/>
              <text x="345" y="24" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">DECIMAL B</text>
              <text x="345" y="60" fill="#ffffff" font-size="28" font-weight="900" text-anchor="middle">${d.numB}</text>
              <rect x="265" y="80" width="160" height="34" rx="6" fill="#0f172a" stroke="#fbbf24"/>
              <text x="345" y="102" fill="#fde047" font-size="11" font-weight="700" text-anchor="middle">Padded: ${d.padB}</text>
            </g>

            <!-- Comparison Logic Derivation -->
            <rect x="40" y="225" width="460" height="85" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="${statusColor}" stroke-width="1.5"/>
            <text x="270" y="248" fill="${statusColor}" font-size="12" font-weight="800" text-anchor="middle">Pedagogical Step-by-Step Reason:</text>
            <text x="270" y="272" fill="#f8fafc" font-size="13" font-weight="800" text-anchor="middle">${d.reason}</text>
            <text x="270" y="295" fill="#94a3b8" font-size="10" text-anchor="middle">Step 1: Check wholes. Step 2: Check tenths. Step 3: Check hundredths. Zero-padding prevents traps!</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Choose Duel:</span>
          ${duels.map((d, idx) => `<button class="sim-btn ${idx === activeDuel ? 'active' : ''}" data-idx="${idx}">${d.numA} vs ${d.numB}</button>`).join('')}
        </div>
      `;

      simControls.querySelectorAll('.sim-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          activeDuel = parseInt(btn.dataset.idx);
          simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          render();
          sfx.playClick();
        });
      });

      render();
    }

    // Slide 12: Addition of Decimals Alignment & Carrying
    function simDecimalAdditionAlignment() {
      simHeaderTitle.textContent = "Decimal Column Addition: Vertical Alignment & Carrying";
      let step = 0; // 0: unaligned/setup, 1: aligned & padded, 2: hundredths added, 3: tenths added (carry), 4: final sum

      const steps = [
        {
          title: "Problem: Add 14.6 + 5.75",
          disp: ["  14.6", "+  5.75"],
          desc: "Step 1: Notice that 14.6 has 1 decimal place while 5.75 has 2.",
          showRes: false
        },
        {
          title: "Step 1: Align Dots & Pad Trailing Zero",
          disp: ["  14.60  (padded with 0)", "+  5.75"],
          desc: "Always align decimal points vertically and pad with zero to equalize places!",
          showRes: false
        },
        {
          title: "Step 2: Add Hundredths Column",
          disp: ["  14.60", "+  5.75", "-------", "      5  (0 + 5 = 5 hundredths)"],
          desc: "0 hundredths + 5 hundredths = 5 hundredths in the hundredths column.",
          showRes: false
        },
        {
          title: "Step 3: Add Tenths Column & Carry 1",
          disp: ["  [1]   (carried to ones)", "  14.60", "+  5.75", "-------", "     .35  (6 + 7 = 13 tenths)"],
          desc: "6 tenths + 7 tenths = 13 tenths = 1 whole (carried) and 3 tenths remaining.",
          showRes: false
        },
        {
          title: "Step 4: Final Sum Evaluated!",
          disp: ["  14.60", "+  5.75", "-------", "  20.35  (1 + 14 + 5 = 20)"],
          desc: "Drop the decimal point straight down! Final answer = 20.35",
          showRes: true
        }
      ];

      function render() {
        const s = steps[step];

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <rect x="100" y="15" width="340" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="38" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">${s.title}</text>

            <!-- Column Working Sheet -->
            <g transform="translate(140, 65)">
              <rect x="0" y="0" width="260" height="145" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="2"/>
              ${s.disp.map((line, idx) => `
                <text x="130" y="${32 + idx * 26}" fill="${idx === s.disp.length - 1 ? (s.showRes ? '#34d399' : '#fbbf24') : '#f8fafc'}" font-size="16" font-family="monospace" font-weight="900" text-anchor="middle">${line}</text>
              `).join('')}
            </g>

            <!-- Explanation Card -->
            <rect x="40" y="225" width="460" height="85" rx="10" fill="rgba(30, 41, 59, 0.85)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="248" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">${s.desc}</text>
            <text x="270" y="272" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Golden Rule: Dots MUST align in a straight vertical line!</text>
            <text x="270" y="292" fill="#94a3b8" font-size="9.5" text-anchor="middle">Carrying over operates identically to whole numbers: 10 tenths = 1 one, 10 hundredths = 1 tenth.</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; gap:1rem; justify-content:center; align-items:center;">
          <button class="sim-btn" id="btnAddPrev">⏮ Prev Step</button>
          <span id="addStepLbl" style="color:#38bdf8; font-weight:700;">Step 1 of 5</span>
          <button class="sim-btn active" id="btnAddNext">Next Step ⏭</button>
          <button class="sim-btn" id="btnAddReset">🔄 Reset</button>
        </div>
      `;

      function updateControls() {
        document.getElementById('addStepLbl').textContent = `Step ${step + 1} of ${steps.length}`;
        document.getElementById('btnAddPrev').disabled = (step === 0);
        document.getElementById('btnAddNext').disabled = (step === steps.length - 1);
      }

      document.getElementById('btnAddPrev').onclick = () => {
        if (step > 0) { step--; render(); updateControls(); sfx.playClick(); }
      };
      document.getElementById('btnAddNext').onclick = () => {
        if (step < steps.length - 1) {
          step++; render(); updateControls();
          if (step === steps.length - 1) sfx.playCelebration(); else sfx.playClick();
        }
      };
      document.getElementById('btnAddReset').onclick = () => {
        step = 0; render(); updateControls(); sfx.playClick();
      };

      render();
      updateControls();
    }

    // Slide 13: Subtraction of Decimals with Borrowing
    function simDecimalSubtractionBorrow() {
      simHeaderTitle.textContent = "Decimal Column Subtraction: Regrouping & Borrowing Across the Point";
      let step = 0;

      const steps = [
        {
          title: "Problem: Subtract 8.4 - 3.75",
          disp: ["   8.4", "-  3.75"],
          desc: "Warning: Never subtract without padding the top number with zeroes first!",
          showRes: false
        },
        {
          title: "Step 1: Pad Minuend with Trailing Zero",
          disp: ["   8.40  (padded zero)", "-  3.75"],
          desc: "Now we see clearly: we must subtract 5 hundredths from 0 hundredths!",
          showRes: false
        },
        {
          title: "Step 2: Borrow 1 Tenth as 10 Hundredths",
          disp: ["      3  10", "   8.40", "-  3.75", "-------", "      5  (10 - 5 = 5 hundredths)"],
          desc: "Borrow 1 from 4 tenths ➔ 4 becomes 3 tenths; 0 becomes 10 hundredths.",
          showRes: false
        },
        {
          title: "Step 3: Borrow 1 One as 10 Tenths",
          disp: ["   7 13", "   8.40", "-  3.75", "-------", "     .65  (13 - 7 = 6 tenths)"],
          desc: "Borrow 1 from 8 ones ➔ 8 becomes 7 ones; 3 tenths becomes 13 tenths.",
          showRes: false
        },
        {
          title: "Step 4: Subtract Ones & Final Result!",
          disp: ["   8.40", "-  3.75", "-------", "   4.65  (7 - 3 = 4)"],
          desc: "7 - 3 = 4 ones. Final difference = 4.65!",
          showRes: true
        }
      ];

      function render() {
        const s = steps[step];

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <rect x="100" y="15" width="340" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#fbbf24" stroke-width="1.5"/>
            <text x="270" y="38" fill="#fbbf24" font-size="13" font-weight="900" text-anchor="middle">${s.title}</text>

            <!-- Column Working Sheet -->
            <g transform="translate(140, 65)">
              <rect x="0" y="0" width="260" height="145" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#f59e0b" stroke-width="2"/>
              ${s.disp.map((line, idx) => `
                <text x="130" y="${28 + idx * 24}" fill="${idx === s.disp.length - 1 ? (s.showRes ? '#34d399' : '#f87171') : '#f8fafc'}" font-size="15" font-family="monospace" font-weight="900" text-anchor="middle">${line}</text>
              `).join('')}
            </g>

            <!-- Explanation Card -->
            <rect x="40" y="225" width="460" height="85" rx="10" fill="rgba(30, 41, 59, 0.85)" stroke="#fbbf24" stroke-width="1.5"/>
            <text x="270" y="248" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">${s.desc}</text>
            <text x="270" y="272" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Regrouping Law: 1 whole = 10 tenths, 1 tenth = 10 hundredths.</text>
            <text x="270" y="292" fill="#94a3b8" font-size="9.5" text-anchor="middle">Check your answer by adding back: 4.65 + 3.75 = 8.40 ✅</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; gap:1rem; justify-content:center; align-items:center;">
          <button class="sim-btn" id="btnSubPrev">⏮ Prev Step</button>
          <span id="subStepLbl" style="color:#fbbf24; font-weight:700;">Step 1 of 5</span>
          <button class="sim-btn active" id="btnSubNext">Next Step ⏭</button>
          <button class="sim-btn" id="btnSubReset">🔄 Reset</button>
        </div>
      `;

      function updateControls() {
        document.getElementById('subStepLbl').textContent = `Step ${step + 1} of ${steps.length}`;
        document.getElementById('btnSubPrev').disabled = (step === 0);
        document.getElementById('btnSubNext').disabled = (step === steps.length - 1);
      }

      document.getElementById('btnSubPrev').onclick = () => {
        if (step > 0) { step--; render(); updateControls(); sfx.playClick(); }
      };
      document.getElementById('btnSubNext').onclick = () => {
        if (step < steps.length - 1) {
          step++; render(); updateControls();
          if (step === steps.length - 1) sfx.playCelebration(); else sfx.playClick();
        }
      };
      document.getElementById('btnSubReset').onclick = () => {
        step = 0; render(); updateControls(); sfx.playClick();
      };

      render();
      updateControls();
    }

    // Slide 14: Decimal Sequences & Estimation Explorer
    function simDecimalSequencesEstimator() {
      simHeaderTitle.textContent = "Decimal Patterns & Fast Mental Estimation Sanity Checks";
      let activePreset = 0;
      const presets = [
        { seq: [0.4, 0.8, 1.2, 1.6], diff: 0.4, next: 2.0, nextNext: 2.4, label: "Tenths Pattern (+0.4)" },
        { seq: [1.25, 1.50, 1.75, 2.00], diff: 0.25, next: 2.25, nextNext: 2.50, label: "Quarter Pattern (+0.25)" },
        { seq: [5.8, 5.5, 5.2, 4.9], diff: -0.3, next: 4.6, nextNext: 4.3, label: "Decreasing Sequence (-0.3)" }
      ];

      function render() {
        const p = presets[activePreset];

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#080e1a"/>

            <rect x="110" y="15" width="320" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="270" y="38" fill="#38bdf8" font-size="13" font-weight="900" text-anchor="middle">Sequence: ${p.label}</text>

            <!-- Sequence Train Blocks -->
            <g transform="translate(40, 75)">
              ${p.seq.map((val, idx) => `
                <rect x="${idx * 85}" y="20" width="70" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
                <text x="${idx * 85 + 35}" y="52" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">${val}</text>
                ${idx < 3 ? `
                  <text x="${idx * 85 + 77}" y="52" fill="#fbbf24" font-size="11" font-weight="900" text-anchor="middle">➔</text>
                ` : ''}
              `).join('')}

              <!-- Next Predicted Term -->
              <text x="330" y="52" fill="#34d399" font-size="14" font-weight="900" text-anchor="middle">➔</text>
              <rect x="345" y="20" width="70" height="55" rx="8" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="2"/>
              <text x="380" y="52" fill="#34d399" font-size="16" font-weight="900" text-anchor="middle">${p.next}</text>

              <!-- Next-Next Term -->
              <text x="425" y="52" fill="#34d399" font-size="14" font-weight="900" text-anchor="middle">➔</text>
              <rect x="440" y="20" width="70" height="55" rx="8" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="2"/>
              <text x="475" y="52" fill="#34d399" font-size="16" font-weight="900" text-anchor="middle">${p.nextNext}</text>
            </g>

            <!-- Estimation Strategy Card -->
            <g transform="translate(45, 165)">
              <rect x="0" y="0" width="450" height="65" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#fbbf24" stroke-width="1.5"/>
              <text x="225" y="25" fill="#fbbf24" font-size="11" font-weight="800" text-anchor="middle">⚡ Quick Mental Estimation Sanity Check</text>
              <text x="225" y="48" fill="#f8fafc" font-size="13" font-weight="700" text-anchor="middle">
                Calculate $24.85 + 51.15$: Round to $25 + 51 = 76$!
              </text>
            </g>

            <!-- Bottom Insight -->
            <rect x="45" y="245" width="450" height="65" rx="8" fill="rgba(30, 41, 59, 0.85)" stroke="#64748b" stroke-width="1"/>
            <text x="270" y="268" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">Common Step (Difference): ${p.diff > 0 ? '+' : ''}${p.diff}</text>
            <text x="270" y="288" fill="#94a3b8" font-size="10" text-anchor="middle">Estimating before calculating guarantees you will catch any misplaced decimal point!</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Choose Pattern:</span>
          ${presets.map((p, idx) => `<button class="sim-btn ${idx === activePreset ? 'active' : ''}" data-idx="${idx}">${p.label}</button>`).join('')}
        </div>
      `;

      simControls.querySelectorAll('.sim-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          activePreset = parseInt(btn.dataset.idx);
          simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          render();
          sfx.playClick();
        });
      });

      render();
    }

    // Slide 15: Deceptive Dots (Cricket Overs & Time vs True Decimals)
    function simCricketTimeDeceptiveDots() {
      simHeaderTitle.textContent = "Deceptive Dots: Not All Dots Are Decimals (Cricket & Time)";
      let activeCase = 0; // 0: Cricket Overs, 1: Clock Time, 2: Software Version

      const cases = [
        {
          title: "Cricket Overs Scoreboard",
          dotDisp: "Scorecard: 5.5 overs",
          dotMeaning: "5 overs and 5 balls (1 over = 6 balls)",
          mathEquivalent: "5 + 5/6 = 5.833... overs",
          trap: "Mistake: Thinking 5.5 overs means 5 and a half overs! In cricket, 5.3 is 5 and a half overs (3/6 = 0.5)!",
          base: "Base 6 (Balls)"
        },
        {
          title: "Clock Time Format",
          dotDisp: "Digital Clock: 4.30 hours",
          dotMeaning: "4 hours and 30 minutes (1 hour = 60 minutes)",
          mathEquivalent: "4 + 30/60 = 4.5 hours (Half an hour!)",
          trap: "Mistake: Treating 4.30 as 4.3 hours. In decimals, 4.3 hours is 4 hours and 18 minutes!",
          base: "Base 60 (Sexagesimal)"
        },
        {
          title: "Software Version Numbers",
          dotDisp: "Software: App Version 2.10",
          dotMeaning: "Major Release 2, Minor Feature Update 10",
          mathEquivalent: "Not a number! 2.10 follows 2.9 (chronological)",
          trap: "Mistake: In mathematics 2.10 = 2.1 < 2.9. But software 2.10 is newer than version 2.9!",
          base: "Hierarchical String Index"
        }
      ];

      function render() {
        const c = cases[activeCase];

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <rect x="110" y="15" width="320" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="#fbbf24" stroke-width="1.5"/>
            <text x="270" y="38" fill="#fbbf24" font-size="13" font-weight="900" text-anchor="middle">Scenario: ${c.title}</text>

            <!-- Deceptive Dot Display Card -->
            <g transform="translate(60, 65)">
              <rect x="0" y="0" width="200" height="110" rx="10" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="2"/>
              <text x="100" y="24" fill="#f87171" font-size="11" font-weight="800" text-anchor="middle">Everyday Separator Dot</text>
              <text x="100" y="60" fill="#ffffff" font-size="16" font-weight="900" text-anchor="middle">${c.dotDisp}</text>
              <text x="100" y="90" fill="#fca5a5" font-size="9.5" text-anchor="middle">${c.base}</text>
            </g>

            <!-- True Mathematical Decimal Card -->
            <g transform="translate(280, 65)">
              <rect x="0" y="0" width="200" height="110" rx="10" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="2"/>
              <text x="100" y="24" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">True Base-10 Decimal</text>
              <text x="100" y="60" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">${c.mathEquivalent}</text>
              <text x="100" y="90" fill="#a7f3d0" font-size="9.5" text-anchor="middle">Base 10 (Tenths / Hundredths)</text>
            </g>

            <!-- Pitfall Warning Card -->
            <rect x="40" y="195" width="460" height="115" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#fbbf24" stroke-width="1.5"/>
            <text x="270" y="220" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">⚠️ The Cognitive Trap Explained:</text>
            <text x="270" y="245" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">${c.trap}</text>
            <text x="270" y="270" fill="#cbd5e1" font-size="10.5" text-anchor="middle">Meaning: ${c.dotMeaning}</text>
            <text x="270" y="295" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">Mathematical decimals ALWAYS divide by powers of 10 (10, 100, 1000)!</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn ${activeCase === 0 ? 'active' : ''}" id="btnCase0">🏏 Cricket Overs (Base 6)</button>
          <button class="sim-btn ${activeCase === 1 ? 'active' : ''}" id="btnCase1">⏰ Clock Time (Base 60)</button>
          <button class="sim-btn ${activeCase === 2 ? 'active' : ''}" id="btnCase2">💻 Software Versions</button>
        </div>
      `;

      document.getElementById('btnCase0').onclick = () => { activeCase = 0; render(); sfx.playClick(); };
      document.getElementById('btnCase1').onclick = () => { activeCase = 1; render(); sfx.playClick(); };
      document.getElementById('btnCase2').onclick = () => { activeCase = 2; render(); sfx.playClick(); };

      render();
    }

    // Slide 16: Decimal Point Displacement & Floating Point Power
    function simDecimalPointDisplacement() {
      simHeaderTitle.textContent = "The Floating Point: Shifting the Dot (×10 or ÷10 Catastrophes)";
      let shift = 0; // -1: 0.25, 0: 2.5, +1: 25.0

      function render() {
        let valStr = "";
        let impact = "";
        let color = "#38bdf8";

        if (shift === -1) {
          valStr = "0.25 mg";
          impact = "10 times smaller! Underdose: Ineffective treatment.";
          color = "#fbbf24";
        } else if (shift === 0) {
          valStr = "2.50 mg";
          impact = "Standard prescribed therapeutic dose ✅ Safe & effective.";
          color = "#10b981";
        } else {
          valStr = "25.0 mg";
          impact = "10 times larger! 1000% Fatal Overdose ☠️ Critical Medical Emergency!";
          color = "#ef4444";
        }

        simCanvas.innerHTML = `
          <svg viewBox="0 0 540 330" width="100%" height="100%">
            <rect x="0" y="0" width="540" height="330" fill="#090d16"/>

            <!-- Main Title Banner -->
            <rect x="90" y="15" width="360" height="36" rx="8" fill="rgba(30, 41, 59, 0.9)" stroke="${color}" stroke-width="1.5"/>
            <text x="270" y="38" fill="${color}" font-size="13" font-weight="900" text-anchor="middle">Dosage Scale: ${valStr}</text>

            <!-- Floating Point Shifting Display -->
            <g transform="translate(100, 75)">
              <rect x="0" y="0" width="340" height="110" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="${color}" stroke-width="2"/>
              <text x="170" y="32" fill="#94a3b8" font-size="11" font-weight="800" text-anchor="middle">DOSAGE REGISTER</text>
              <text x="170" y="75" fill="${color}" font-size="34" font-weight="900" text-anchor="middle">${valStr}</text>
              <text x="170" y="98" fill="#f8fafc" font-size="11" font-weight="700" text-anchor="middle">${impact}</text>
            </g>

            <!-- Historical Wisdom & Law Card -->
            <rect x="40" y="210" width="460" height="100" rx="10" fill="rgba(30, 41, 59, 0.85)" stroke="#fbbf24" stroke-width="1.5"/>
            <text x="270" y="235" fill="#fbbf24" font-size="12" font-weight="900" text-anchor="middle">The Immense Power of the Decimal Point:</text>
            <text x="270" y="260" fill="#f8fafc" font-size="11.5" font-weight="700" text-anchor="middle">Shifting right 1 place ➔ Multiplies by 10</text>
            <text x="270" y="280" fill="#f8fafc" font-size="11.5" font-weight="700" text-anchor="middle">Shifting left 1 place ➔ Divides by 10</text>
            <text x="270" y="298" fill="#38bdf8" font-size="10" text-anchor="middle">From Aryabhata in 499 CE to modern rocketry, decimal precision governs our universe!</text>
          </svg>
        `;
      }

      simControls.innerHTML = `
        <div style="display:flex; gap:1rem; justify-content:center; align-items:center;">
          <button class="sim-btn ${shift === -1 ? 'active' : ''}" id="btnShiftLeft">⬅ Shift Dot Left (÷10: 0.25 mg)</button>
          <button class="sim-btn ${shift === 0 ? 'active' : ''}" id="btnShiftNorm">🎯 Normal (2.5 mg)</button>
          <button class="sim-btn ${shift === 1 ? 'active' : ''}" id="btnShiftRight" style="border-color:#ef4444; color:#fca5a5;">Shift Dot Right (×10: 25 mg) ➔</button>
        </div>
      `;

      document.getElementById('btnShiftLeft').onclick = () => { shift = -1; render(); sfx.playClick(); };
      document.getElementById('btnShiftNorm').onclick = () => { shift = 0; render(); sfx.playClick(); };
      document.getElementById('btnShiftRight').onclick = () => { shift = 1; render(); sfx.playIncorrect(); };

      render();
    }
""";

