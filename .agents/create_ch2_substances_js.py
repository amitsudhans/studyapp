# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Science Chapter 2: Exploring Substances: Acidic, Basic, and Neutral
JavaScript engine: 16 bespoke interactive SVG simulators
"""

JS_CODE = r'''
// Master Simulator Dispatcher for Chapter 2: Exploring Substances: Acidic, Basic, and Neutral
function initSimulatorForSlide(slideId, container) {
  if (!container) return;
  switch (slideId) {
    case 1: initSubstanceMatrixSim(container); break;
    case 2: initLitmusBenchSim(container); break;
    case 3: initRedRoseLabSim(container); break;
    case 4: initTurmericCurrySim(container); break;
    case 5: initChinaRoseSpectrumSim(container); break;
    case 6: initOlfactoryOdorSim(container); break;
    case 7: initPhenolphthaleinSim(container); break;
    case 8: initUniversalPhStripSim(container); break;
    case 9: initNeutralisationChamberSim(container); break;
    case 10: initTitrationBuretteSim(container); break;
    case 11: initAntBiteNeutraliserSim(container); break;
    case 12: initSoilPhManagementSim(container); break;
    case 13: initFactoryEffluentSim(container); break;
    case 14: initBioHealthSim(container); break;
    case 15: initPcRayHeritageSim(container); break;
    case 16: initMasterSubstanceWheelSim(container); break;
  }
}

// -------------------------------------------------------------
// 1. Household Substance Matrix Simulator
// -------------------------------------------------------------
function initSubstanceMatrixSim(container) {
  const svg = container.querySelector('#substanceSvg');
  const badge = container.querySelector('#substanceClassBadge');
  const desc = container.querySelector('#substanceDesc');
  const btns = container.querySelectorAll('.substanceBtn');
  if (!svg) return;

  const items = {
    lemon: {
      name: "Lemon Juice",
      category: "Acidic (Citric Acid)",
      badgeClass: "bg-rose-500/20 text-rose-300 border-rose-500/30",
      color: "#fef08a",
      liquidColor: "#facc15",
      pH: 2.2,
      taste: "Very Sour",
      touch: "Watery",
      litmus: "Blue Litmus ➔ RED",
      desc: "<strong>Lemon Juice:</strong> Contains citric acid (C6H8O7) and ascorbic acid (Vitamin C). Intensely sour taste. Turns blue litmus red. pH ≈ 2.2."
    },
    vinegar: {
      name: "Vinegar (Sirka)",
      category: "Acidic (Acetic Acid)",
      badgeClass: "bg-rose-500/20 text-rose-300 border-rose-500/30",
      color: "#e2e8f0",
      liquidColor: "#cbd5e1",
      pH: 2.8,
      taste: "Pungent Sour",
      touch: "Watery",
      litmus: "Blue Litmus ➔ RED",
      desc: "<strong>Vinegar:</strong> A 4% to 8% aqueous solution of acetic acid (CH3COOH). Produced by bacterial fermentation. Turns blue litmus red. pH ≈ 2.8."
    },
    water: {
      name: "Pure Distilled Water",
      category: "Neutral (Pure H2O)",
      badgeClass: "bg-emerald-500/20 text-emerald-300 border-emerald-500/30",
      color: "#38bdf8",
      liquidColor: "#0284c7",
      pH: 7.0,
      taste: "Tasteless",
      touch: "Watery",
      litmus: "No Color Change",
      desc: "<strong>Distilled Water:</strong> Strictly neutral with equal H+ and OH- ion concentrations. Does not change the color of red or blue litmus paper. pH = 7.0."
    },
    baking: {
      name: "Baking Soda Solution",
      category: "Basic (NaHCO3)",
      badgeClass: "bg-cyan-500/20 text-cyan-300 border-cyan-500/30",
      color: "#f8fafc",
      liquidColor: "#93c5fd",
      pH: 8.4,
      taste: "Bitter",
      touch: "Slippery / Soapy",
      litmus: "Red Litmus ➔ BLUE",
      desc: "<strong>Baking Soda:</strong> Sodium hydrogen carbonate (NaHCO3). Mildly basic salt that releases OH- ions in water. Turns red litmus blue. pH ≈ 8.4."
    },
    soap: {
      name: "Bathing Soap Lather",
      category: "Basic (Alkaline)",
      badgeClass: "bg-blue-500/20 text-blue-300 border-blue-500/30",
      color: "#bae6fd",
      liquidColor: "#60a5fa",
      pH: 9.8,
      taste: "Bitter",
      touch: "Very Slippery / Soapy",
      litmus: "Red Litmus ➔ BLUE",
      desc: "<strong>Soap Water:</strong> Sodium or potassium salts of long-chain fatty acids. Strongly basic, slippery to touch. Turns red litmus blue and turmeric reddish-brown. pH ≈ 9.8."
    },
    lime: {
      name: "Lime Water (Chuna)",
      category: "Basic (Ca(OH)2)",
      badgeClass: "bg-blue-500/20 text-blue-300 border-blue-500/30",
      color: "#f1f5f9",
      liquidColor: "#93c5fd",
      pH: 12.4,
      taste: "Astringent Bitter",
      touch: "Soapy",
      litmus: "Red Litmus ➔ BLUE",
      desc: "<strong>Lime Water:</strong> Calcium hydroxide solution (Ca(OH)2). Strong alkali that turns red litmus blue and turns milky with carbon dioxide gas. pH ≈ 12.4."
    }
  };

  function render(key) {
    const item = items[key];
    if (badge) {
      badge.textContent = item.category;
      badge.className = `px-2 py-0.5 rounded text-[11px] font-mono border font-semibold ${item.badgeClass}`;
    }
    if (desc) desc.innerHTML = item.desc;

    svg.innerHTML = `
      <!-- Beaker Outline -->
      <rect x="190" y="60" width="120" height="130" rx="8" fill="#0f172a" stroke="#475569" stroke-width="2.5" />
      
      <!-- Liquid in Beaker -->
      <rect x="192" y="100" width="116" height="88" rx="4" fill="${item.liquidColor}" fill-opacity="0.5" />
      <ellipse cx="250" cy="100" rx="58" ry="8" fill="${item.liquidColor}" fill-opacity="0.8" />

      <!-- Sample Name -->
      <text x="250" y="45" fill="#f8fafc" font-size="14" font-weight="extrabold" text-anchor="middle">${item.name}</text>

      <!-- Property Cards on Left and Right -->
      <!-- Left Card: Sensory Properties -->
      <rect x="30" y="70" width="130" height="110" rx="10" fill="#1e293b" stroke="#334155" />
      <text x="40" y="92" fill="#94a3b8" font-size="10" font-weight="bold">SENSORY TRAITS</text>
      <text x="40" y="115" fill="#fde047" font-size="11">Taste: <strong>${item.taste}</strong></text>
      <text x="40" y="135" fill="#38bdf8" font-size="11">Touch: <strong>${item.touch}</strong></text>
      <text x="40" y="160" fill="#a7f3d0" font-size="11">Litmus: <strong>${item.litmus}</strong></text>

      <!-- Right Card: Chemical Metrics -->
      <rect x="340" y="70" width="130" height="110" rx="10" fill="#1e293b" stroke="#334155" />
      <text x="350" y="92" fill="#94a3b8" font-size="10" font-weight="bold">CHEMICAL DATA</text>
      <text x="350" y="118" fill="#38bdf8" font-size="13" font-weight="extrabold">pH ≈ ${item.pH}</text>
      <text x="350" y="142" fill="${item.pH < 7 ? '#f43f5e' : item.pH === 7 ? '#10b981' : '#0284c7'}" font-size="11" font-weight="bold">
        ${item.pH < 7 ? 'ACIDIC MEDIUM' : item.pH === 7 ? 'NEUTRAL MEDIUM' : 'BASIC (ALKALINE)'}
      </text>
      <text x="350" y="165" fill="#cbd5e1" font-size="10">Class 7 Standard</text>
    `;
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.className = "substanceBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition");
      btn.className = "substanceBtn px-2 py-1.5 rounded-lg bg-amber-600 text-white font-bold transition";
      render(btn.dataset.item);
    });
  });

  render('lemon');
}

// -------------------------------------------------------------
// 2. Litmus Paper Test Bench Simulator
// -------------------------------------------------------------
function initLitmusBenchSim(container) {
  const svg = container.querySelector('#litmusSvg');
  const badge = container.querySelector('#litmusResultBadge');
  const redText = container.querySelector('#redLitmusText');
  const blueText = container.querySelector('#blueLitmusText');
  const btns = container.querySelectorAll('.litmusSolBtn');
  if (!svg) return;

  function setSolution(type) {
    if (type === 'acid') {
      badge.textContent = "Acid: Blue Litmus ➔ RED";
      badge.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold";
      if (redText) redText.textContent = "Red Litmus: Stays RED";
      if (blueText) blueText.textContent = "Blue Litmus: Turns RED ✔";

      svg.innerHTML = `
        <!-- Solution Beaker (Acid) -->
        <rect x="170" y="70" width="160" height="130" rx="8" fill="#0284c7" fill-opacity="0.1" stroke="#475569" stroke-width="2" />
        <rect x="172" y="115" width="156" height="83" rx="4" fill="#f43f5e" fill-opacity="0.3" />
        <text x="250" y="195" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">Acidic Sample (Lemon Juice / HCl)</text>

        <!-- Red Litmus Strip (Left) -->
        <g transform="translate(195, 45)">
          <rect x="0" y="0" width="28" height="110" rx="3" fill="#ef4444" stroke="#b91c1c" stroke-width="1.5" />
          <text x="14" y="25" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" transform="rotate(-90 14 25)">RED</text>
          <!-- Submerged tip: stays red -->
          <rect x="0" y="70" width="28" height="40" rx="2" fill="#dc2626" />
          <text x="14" y="90" fill="#ffffff" font-size="8" text-anchor="middle">RED</text>
        </g>

        <!-- Blue Litmus Strip (Right) -->
        <g transform="translate(275, 45)">
          <rect x="0" y="0" width="28" height="110" rx="3" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1.5" />
          <text x="14" y="25" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" transform="rotate(-90 14 25)">BLUE</text>
          <!-- Submerged tip: turns red! -->
          <rect x="0" y="70" width="28" height="40" rx="2" fill="#dc2626" />
          <text x="14" y="90" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">➔ RED</text>
        </g>

        <text x="250" y="30" fill="#f43f5e" font-size="13" font-weight="extrabold" text-anchor="middle">Acidic Medium: Blue Litmus Turns RED</text>
      `;
    } else if (type === 'base') {
      badge.textContent = "Base: Red Litmus ➔ BLUE";
      badge.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-blue-500/20 text-blue-300 border border-blue-500/30 font-semibold";
      if (redText) redText.textContent = "Red Litmus: Turns BLUE ✔";
      if (blueText) blueText.textContent = "Blue Litmus: Stays BLUE";

      svg.innerHTML = `
        <!-- Solution Beaker (Base) -->
        <rect x="170" y="70" width="160" height="130" rx="8" fill="#0284c7" fill-opacity="0.1" stroke="#475569" stroke-width="2" />
        <rect x="172" y="115" width="156" height="83" rx="4" fill="#3b82f6" fill-opacity="0.3" />
        <text x="250" y="195" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">Basic Sample (Soap Solution / NaOH)</text>

        <!-- Red Litmus Strip (Left) -->
        <g transform="translate(195, 45)">
          <rect x="0" y="0" width="28" height="110" rx="3" fill="#ef4444" stroke="#b91c1c" stroke-width="1.5" />
          <text x="14" y="25" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" transform="rotate(-90 14 25)">RED</text>
          <!-- Submerged tip: turns blue! -->
          <rect x="0" y="70" width="28" height="40" rx="2" fill="#2563eb" />
          <text x="14" y="90" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">➔ BLUE</text>
        </g>

        <!-- Blue Litmus Strip (Right) -->
        <g transform="translate(275, 45)">
          <rect x="0" y="0" width="28" height="110" rx="3" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1.5" />
          <text x="14" y="25" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" transform="rotate(-90 14 25)">BLUE</text>
          <!-- Submerged tip: stays blue -->
          <rect x="0" y="70" width="28" height="40" rx="2" fill="#2563eb" />
          <text x="14" y="90" fill="#ffffff" font-size="8" text-anchor="middle">BLUE</text>
        </g>

        <text x="250" y="30" fill="#38bdf8" font-size="13" font-weight="extrabold" text-anchor="middle">Basic Medium: Red Litmus Turns BLUE</text>
      `;
    } else {
      badge.textContent = "Neutral: No Litmus Color Change";
      badge.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold";
      if (redText) redText.textContent = "Red Litmus: Stays RED";
      if (blueText) blueText.textContent = "Blue Litmus: Stays BLUE";

      svg.innerHTML = `
        <rect x="170" y="70" width="160" height="130" rx="8" fill="#0284c7" fill-opacity="0.1" stroke="#475569" stroke-width="2" />
        <rect x="172" y="115" width="156" height="83" rx="4" fill="#0284c7" fill-opacity="0.3" />
        <text x="250" y="195" fill="#67e8f9" font-size="11" font-weight="bold" text-anchor="middle">Neutral Sample (Pure Distilled Water)</text>

        <!-- Red Litmus -->
        <g transform="translate(195, 45)">
          <rect x="0" y="0" width="28" height="110" rx="3" fill="#ef4444" stroke="#b91c1c" stroke-width="1.5" />
          <text x="14" y="25" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" transform="rotate(-90 14 25)">RED</text>
          <rect x="0" y="70" width="28" height="40" rx="2" fill="#ef4444" />
          <text x="14" y="90" fill="#ffffff" font-size="8" text-anchor="middle">RED</text>
        </g>

        <!-- Blue Litmus -->
        <g transform="translate(275, 45)">
          <rect x="0" y="0" width="28" height="110" rx="3" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1.5" />
          <text x="14" y="25" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle" transform="rotate(-90 14 25)">BLUE</text>
          <rect x="0" y="70" width="28" height="40" rx="2" fill="#3b82f6" />
          <text x="14" y="90" fill="#ffffff" font-size="8" text-anchor="middle">BLUE</text>
        </g>

        <text x="250" y="30" fill="#34d399" font-size="13" font-weight="extrabold" text-anchor="middle">Neutral Medium: Zero Color Change</text>
      `;
    }
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.className = "litmusSolBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition");
      btn.className = "litmusSolBtn px-2.5 py-1.5 rounded-lg bg-blue-600 text-white font-bold transition";
      setSolution(btn.dataset.sol);
    });
  });

  setSolution('acid');
}

// -------------------------------------------------------------
// 3. Red Rose Indicator Lab Simulator
// -------------------------------------------------------------
function initRedRoseLabSim(container) {
  const svg = container.querySelector('#roseSvg');
  const badge = container.querySelector('#roseColorBadge');
  const desc = container.querySelector('#roseDesc');
  const btns = container.querySelectorAll('.roseBtn');
  if (!svg) return;

  function render(mode) {
    if (mode === 'acid') {
      badge.textContent = "Acidic Solution: Deep Crimson Red";
      badge.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold";
      desc.innerHTML = "<strong>In Acidic Solution (Lemon Juice / Dilute HCl):</strong> Rose anthocyanins protonate, shifting the absorbed light spectrum to emit a vibrant, deep crimson red.";
      svg.innerHTML = `
        <!-- Test Tube Outline -->
        <rect x="220" y="40" width="60" height="160" rx="10" fill="#0f172a" stroke="#cbd5e1" stroke-width="2" />
        <!-- Solution -->
        <path d="M 222 100 L 222 190 Q 250 205 278 190 L 278 100 Z" fill="#e11d48" fill-opacity="0.8" />
        <text x="250" y="150" fill="#ffffff" font-size="11" font-weight="extrabold" text-anchor="middle">Deep Red</text>

        <!-- Rose Flower Graphic at Left -->
        <circle cx="100" cy="120" r="28" fill="#be123c" stroke="#fb7185" stroke-width="2" />
        <circle cx="100" cy="120" r="14" fill="#881337" />
        <text x="100" y="170" fill="#fda4af" font-size="11" font-weight="bold" text-anchor="middle">Red Rose Extract</text>

        <!-- Pipette dropping into tube -->
        <polygon points="245,15 255,15 252,50 248,50" fill="#94a3b8" />
        <circle cx="250" cy="65" r="4" fill="#e11d48" />

        <text x="380" y="100" fill="#fb7185" font-size="13" font-weight="extrabold">Acid Test</text>
        <text x="380" y="125" fill="#f8fafc" font-size="11">Anthocyanin</text>
        <text x="380" y="145" fill="#94a3b8" font-size="10">Flavylium cation</text>
      `;
    } else if (mode === 'base') {
      badge.textContent = "Basic Solution: Emerald Green";
      badge.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold";
      desc.innerHTML = "<strong>In Basic Solution (Baking Soda / Soap / NaOH):</strong> Hydroxide ions deprotonate the pigment, turning the extract into a striking emerald green / yellowish-green.";
      svg.innerHTML = `
        <rect x="220" y="40" width="60" height="160" rx="10" fill="#0f172a" stroke="#cbd5e1" stroke-width="2" />
        <path d="M 222 100 L 222 190 Q 250 205 278 190 L 278 100 Z" fill="#059669" fill-opacity="0.8" />
        <text x="250" y="150" fill="#ffffff" font-size="11" font-weight="extrabold" text-anchor="middle">Green</text>

        <circle cx="100" cy="120" r="28" fill="#be123c" stroke="#fb7185" stroke-width="2" />
        <circle cx="100" cy="120" r="14" fill="#881337" />
        <text x="100" y="170" fill="#fda4af" font-size="11" font-weight="bold" text-anchor="middle">Red Rose Extract</text>

        <polygon points="245,15 255,15 252,50 248,50" fill="#94a3b8" />
        <circle cx="250" cy="65" r="4" fill="#059669" />

        <text x="380" y="100" fill="#34d399" font-size="13" font-weight="extrabold">Base Test</text>
        <text x="380" y="125" fill="#f8fafc" font-size="11">Anthocyanin</text>
        <text x="380" y="145" fill="#94a3b8" font-size="10">Chalcone form</text>
      `;
    } else {
      badge.textContent = "Neutral Solution: Light Pink (No Change)";
      badge.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-pink-500/20 text-pink-300 border border-pink-500/30 font-semibold";
      desc.innerHTML = "<strong>In Neutral Solution (Distilled Water):</strong> The pigment retains its unperturbed natural light pink hue.";
      svg.innerHTML = `
        <rect x="220" y="40" width="60" height="160" rx="10" fill="#0f172a" stroke="#cbd5e1" stroke-width="2" />
        <path d="M 222 100 L 222 190 Q 250 205 278 190 L 278 100 Z" fill="#f472b6" fill-opacity="0.5" />
        <text x="250" y="150" fill="#ffffff" font-size="11" font-weight="extrabold" text-anchor="middle">Light Pink</text>

        <circle cx="100" cy="120" r="28" fill="#be123c" stroke="#fb7185" stroke-width="2" />
        <circle cx="100" cy="120" r="14" fill="#881337" />
        <text x="100" y="170" fill="#fda4af" font-size="11" font-weight="bold" text-anchor="middle">Red Rose Extract</text>

        <polygon points="245,15 255,15 252,50 248,50" fill="#94a3b8" />
        <circle cx="250" cy="65" r="4" fill="#f472b6" />

        <text x="380" y="100" fill="#f472b6" font-size="13" font-weight="extrabold">Neutral Test</text>
        <text x="380" y="125" fill="#f8fafc" font-size="11">Distilled Water</text>
        <text x="380" y="145" fill="#94a3b8" font-size="10">No color change</text>
      `;
    }
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.className = "roseBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition");
      btn.className = "roseBtn px-2.5 py-1.5 rounded-lg bg-rose-600 text-white font-bold transition";
      render(btn.dataset.test);
    });
  });

  render('acid');
}

// -------------------------------------------------------------
// 4. Turmeric Paper & Curry Stain Simulator
// -------------------------------------------------------------
function initTurmericCurrySim(container) {
  const svg = container.querySelector('#turmericSvg');
  const status = container.querySelector('#turmericStatus');
  const exp = container.querySelector('#turmericExplanation');
  const b1 = container.querySelector('#applyNeutralBtn');
  const b2 = container.querySelector('#applySoapBtn');
  const b3 = container.querySelector('#applyLemonBtn');
  if (!svg || !b1 || !b2 || !b3) return;

  function render(state) {
    let stainColor = "#eab308"; // yellow
    let statusText = "Natural Yellow State";
    let statusClass = "bg-amber-500/20 text-amber-300 border-amber-500/30";
    let expText = "Fresh curry contains natural turmeric (curcumin). In neutral or acidic environments, it maintains a bright yellow hue.";

    if (state === 'soap') {
      stainColor = "#b91c1c"; // deep red
      statusText = "Soap Applied ➔ REDDISH BROWN!";
      statusClass = "bg-rose-500/20 text-rose-300 border-rose-500/30 font-bold";
      expText = "<strong>Chemical Reaction:</strong> Laundry soap is alkaline (contains basic sodium hydroxide / carbonate). Hydroxide ions deprotonate curcumin, creating a deep <strong>reddish-brown</strong> complex!";
    } else if (state === 'lemon') {
      stainColor = "#eab308"; // restored yellow
      statusText = "Lemon Rinse ➔ Restored to YELLOW!";
      statusClass = "bg-emerald-500/20 text-emerald-300 border-emerald-500/30 font-bold";
      expText = "<strong>Neutralisation:</strong> Lemon juice contains citric acid. The acid neutralizes the basic soap residue, returning curcumin to its yellow form!";
    }

    if (status) {
      status.textContent = statusText;
      status.className = `px-2 py-0.5 rounded text-[11px] font-mono border font-semibold ${statusClass}`;
    }
    if (exp) exp.innerHTML = expText;

    svg.innerHTML = `
      <!-- White Cotton Shirt Group -->
      <g transform="translate(140, 30)">
        <polygon points="40,20 80,0 140,0 180,20 220,50 190,80 170,70 170,170 50,170 50,70 30,80 0,50" fill="#f8fafc" stroke="#94a3b8" stroke-width="2" />
        <!-- Collar -->
        <polygon points="80,0 110,40 140,0" fill="#e2e8f0" stroke="#cbd5e1" />
        
        <!-- Curry / Turmeric Stain Spot -->
        <ellipse cx="110" cy="105" rx="35" ry="25" fill="${stainColor}" stroke="${state === 'soap' ? '#991b1b' : '#ca8a04'}" stroke-width="2" />
        <circle cx="125" cy="95" r="8" fill="${stainColor}" />
        <circle cx="95" cy="115" r="10" fill="${stainColor}" />

        <text x="110" y="110" fill="#ffffff" font-size="11" font-weight="extrabold" text-anchor="middle">
          ${state === 'soap' ? 'RED STAIN' : 'YELLOW'}
        </text>
      </g>

      <!-- Reagent Callout -->
      <g transform="translate(380, 80)">
        <rect x="0" y="0" width="100" height="90" rx="8" fill="#1e293b" stroke="#334155" />
        <text x="50" y="25" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Curcumin</text>
        <text x="50" y="50" fill="#94a3b8" font-size="9" text-anchor="middle">In Base ➔ Red</text>
        <text x="50" y="70" fill="#94a3b8" font-size="9" text-anchor="middle">In Acid ➔ Yellow</text>
      </g>
    `;
  }

  b1.addEventListener('click', () => {
    [b1, b2, b3].forEach(b => b.className = "px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition");
    b1.className = "px-2.5 py-1.5 rounded-lg bg-amber-600 text-white font-bold transition";
    render('curry');
  });

  b2.addEventListener('click', () => {
    [b1, b2, b3].forEach(b => b.className = "px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition");
    b2.className = "px-2.5 py-1.5 rounded-lg bg-rose-600 text-white font-bold transition";
    render('soap');
  });

  b3.addEventListener('click', () => {
    [b1, b2, b3].forEach(b => b.className = "px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition");
    b3.className = "px-2.5 py-1.5 rounded-lg bg-emerald-600 text-white font-bold transition";
    render('lemon');
  });

  render('curry');
}

// -------------------------------------------------------------
// 5. China Rose & Floral Spectra Simulator
// -------------------------------------------------------------
function initChinaRoseSpectrumSim(container) {
  const svg = container.querySelector('#chinaRoseSvg');
  const badge = container.querySelector('#chinaRoseBadge');
  const crText = container.querySelector('#crColorText');
  const rcText = container.querySelector('#rcColorText');
  const btns = container.querySelectorAll('.chinaMedBtn');
  if (!svg) return;

  function render(med) {
    let crColor = "#db2777"; // magenta
    let rcColor = "#e11d48"; // red
    let badgeText = "Acidic: China Rose turns Magenta";

    if (med === 'acid') {
      crColor = "#db2777"; // magenta
      rcColor = "#e11d48"; // red
      badgeText = "Acid (pH 2): China Rose = Magenta";
      if (crText) crText.textContent = "Dark Pink (Magenta)";
      if (rcText) rcText.textContent = "Bright Red";
    } else if (med === 'base') {
      crColor = "#059669"; // green
      rcColor = "#65a30d"; // greenish yellow
      badgeText = "Base (pH 11): China Rose = Green";
      if (crText) crText.textContent = "Emerald Green";
      if (rcText) rcText.textContent = "Greenish Yellow";
    } else {
      crColor = "#f472b6"; // light pink
      rcColor = "#7c3aed"; // purple
      badgeText = "Neutral (pH 7): Unchanged Original Color";
      if (crText) crText.textContent = "Light Pink";
      if (rcText) rcText.textContent = "Deep Purple";
    }

    if (badge) badge.textContent = badgeText;

    svg.innerHTML = `
      <!-- China Rose Test Tube (Left) -->
      <g transform="translate(130, 40)">
        <rect x="0" y="0" width="55" height="150" rx="10" fill="#0f172a" stroke="#cbd5e1" stroke-width="2" />
        <path d="M 2 50 L 2 140 Q 27.5 152 53 140 L 53 50 Z" fill="${crColor}" fill-opacity="0.8" />
        <text x="27.5" y="180" fill="#f472b6" font-size="11" font-weight="bold" text-anchor="middle">China Rose</text>
        <text x="27.5" y="100" fill="#ffffff" font-size="10" font-weight="extrabold" text-anchor="middle">
          ${med === 'acid' ? 'Magenta' : med === 'base' ? 'Green' : 'Pink'}
        </text>
      </g>

      <!-- Red Cabbage Test Tube (Right) -->
      <g transform="translate(315, 40)">
        <rect x="0" y="0" width="55" height="150" rx="10" fill="#0f172a" stroke="#cbd5e1" stroke-width="2" />
        <path d="M 2 50 L 2 140 Q 27.5 152 53 140 L 53 50 Z" fill="${rcColor}" fill-opacity="0.8" />
        <text x="27.5" y="180" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle">Red Cabbage</text>
        <text x="27.5" y="100" fill="#ffffff" font-size="10" font-weight="extrabold" text-anchor="middle">
          ${med === 'acid' ? 'Red' : med === 'base' ? 'Green-Yel' : 'Purple'}
        </text>
      </g>

      <text x="250" y="25" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">
        Medium: ${med.toUpperCase()} (Side-by-Side Floral Spectrum)
      </text>
    `;
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.className = "chinaMedBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition");
      btn.className = "chinaMedBtn px-2.5 py-1.5 rounded-lg bg-pink-600 text-white font-bold transition";
      render(btn.dataset.med);
    });
  });

  render('acid');
}

// -------------------------------------------------------------
// 6. Olfactory Odor Meter Simulator
// -------------------------------------------------------------
function initOlfactoryOdorSim(container) {
  const svg = container.querySelector('#olfactorySvg');
  const badge = container.querySelector('#odorStatusBadge');
  const desc = container.querySelector('#odorDesc');
  const bAcid = container.querySelector('#odorAcidBtn');
  const bBase = container.querySelector('#odorBaseBtn');
  if (!svg || !bAcid || !bBase) return;

  function render(isAcid) {
    if (badge) {
      badge.textContent = isAcid ? "Acid: Odor Remains Intact ✔" : "Base: Odor Destroyed & Vanishes!";
      badge.className = isAcid ?
        "px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" :
        "px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold";
    }

    if (desc) {
      desc.innerHTML = isAcid ?
        "<strong>Treated with Acid (Dilute HCl):</strong> The organic sulfur compounds from onion / vanilla are chemically preserved in acidic medium. The aroma is distinct and sharp." :
        "<strong>Treated with Base (NaOH Solution):</strong> Alkaline hydroxide ions react with and deconstruct the volatile aroma molecules. The characteristic scent is <strong>completely eliminated</strong>!";
    }

    svg.innerHTML = `
      <!-- Cloth Strip Infused with Onion Extract -->
      <g transform="translate(180, 50)">
        <rect x="0" y="0" width="50" height="140" rx="4" fill="#fde68a" stroke="#d97706" stroke-width="2" />
        <text x="25" y="75" fill="#78350f" font-size="10" font-weight="bold" text-anchor="middle" transform="rotate(-90 25 75)">ONION CLOTH</text>
      </g>

      <!-- Dropper adding reagent -->
      <g transform="translate(195, 10)">
        <polygon points="5,0 15,0 12,25 8,25" fill="#94a3b8" />
        <circle cx="10" cy="35" r="3.5" fill="${isAcid ? '#ef4444' : '#3b82f6'}" />
      </g>

      <!-- Animated Scent Waves (Only visible in Acid) -->
      ${isAcid ? `
        <g stroke="#22c55e" stroke-width="2" fill="none" opacity="0.8">
          <path d="M 245 70 Q 270 50 300 70 T 360 70" />
          <path d="M 245 100 Q 275 80 310 100 T 375 100" />
          <path d="M 245 130 Q 270 110 300 130 T 360 130" />
        </g>
        <!-- Nose Icon detecting smell -->
        <text x="400" y="110" font-size="28">👃</text>
        <text x="400" y="140" fill="#34d399" font-size="11" font-weight="bold">Smell Detected!</text>
      ` : `
        <!-- Cross Mark indicating zero smell -->
        <text x="350" y="110" font-size="28">🚫👃</text>
        <text x="350" y="140" fill="#f87171" font-size="11" font-weight="bold">Zero Scent (Destroyed)</text>
      `}

      <text x="250" y="220" fill="${isAcid ? '#34d399' : '#f87171'}" font-size="12" font-weight="extrabold" text-anchor="middle">
        ${isAcid ? 'Acidic Medium: Odor PERSISTS' : 'Basic Medium: Odor VANISHES'}
      </text>
    `;
  }

  bAcid.addEventListener('click', () => {
    bAcid.className = "px-3 py-2 rounded-xl bg-emerald-600 text-white font-bold transition";
    bBase.className = "px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition";
    render(true);
  });

  bBase.addEventListener('click', () => {
    bBase.className = "px-3 py-2 rounded-xl bg-rose-600 text-white font-bold transition";
    bAcid.className = "px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition";
    render(false);
  });

  render(true);
}

// -------------------------------------------------------------
// 7. Synthetic Phenolphthalein Chamber Simulator
// -------------------------------------------------------------
function initPhenolphthaleinSim(container) {
  const svg = container.querySelector('#phptSvg');
  const badge = container.querySelector('#phptStateBadge');
  const bAddBase = container.querySelector('#phptAddBaseBtn');
  const bAddAcid = container.querySelector('#phptAddAcidBtn');
  const bReset = container.querySelector('#phptResetBtn');
  if (!svg || !bAddBase || !bAddAcid) return;

  let baseDrops = 0; // if > 0, turns pink!

  function render() {
    const isPink = baseDrops > 0;
    if (badge) {
      badge.textContent = isPink ? "Basic: VIVID MAGENTA-PINK" : "Acidic/Neutral: COLORLESS";
      badge.className = isPink ?
        "px-2 py-0.5 rounded text-[11px] font-mono bg-pink-500/20 text-pink-300 border border-pink-500/30 font-semibold" :
        "px-2 py-0.5 rounded text-[11px] font-mono bg-slate-800 text-slate-400 border border-slate-700 font-semibold";
    }

    svg.innerHTML = `
      <!-- Beaker Outline -->
      <rect x="180" y="60" width="140" height="140" rx="8" fill="#0f172a" stroke="#475569" stroke-width="2.5" />
      
      <!-- Liquid Body -->
      <rect x="182" y="105" width="136" height="93" rx="4" fill="${isPink ? '#ec4899' : '#0284c7'}" fill-opacity="${isPink ? '0.7' : '0.1'}" />
      <ellipse cx="250" cy="105" rx="68" ry="8" fill="${isPink ? '#f472b6' : '#0284c7'}" fill-opacity="${isPink ? '0.9' : '0.2'}" />

      <!-- Chemical Status Label -->
      <text x="250" y="160" fill="${isPink ? '#ffffff' : '#94a3b8'}" font-size="12" font-weight="extrabold" text-anchor="middle">
        ${isPink ? 'Vivid Pink (Alkaline)' : 'Colorless (Acid / Neutral)'}
      </text>

      <!-- Dropper on top -->
      <polygon points="245,15 255,15 252,50 248,50" fill="#94a3b8" />
      <circle cx="250" cy="70" r="4" fill="${isPink ? '#ec4899' : '#38bdf8'}" />

      <!-- Telemetry Box on Right -->
      <rect x="350" y="70" width="125" height="110" rx="8" fill="#1e293b" stroke="#334155" />
      <text x="360" y="95" fill="#f472b6" font-size="11" font-weight="bold">PHENOLPHTHALEIN</text>
      <text x="360" y="120" fill="#cbd5e1" font-size="10">Base Added: ${baseDrops} drops</text>
      <text x="360" y="140" fill="${isPink ? '#f472b6' : '#38bdf8'}" font-size="11" font-weight="bold">
        ${isPink ? 'pH > 8.2 (Pink)' : 'pH < 8.2 (Clear)'}
      </text>
    `;
  }

  bAddBase.addEventListener('click', () => { baseDrops++; render(); });
  bAddAcid.addEventListener('click', () => { if (baseDrops > 0) baseDrops--; render(); });
  if (bReset) bReset.addEventListener('click', () => { baseDrops = 0; render(); });

  render();
}

// -------------------------------------------------------------
// 8. Universal pH Scale Strip Simulator
// -------------------------------------------------------------
function initUniversalPhStripSim(container) {
  const svg = container.querySelector('#phStripSvg');
  const slider = container.querySelector('#phSlider');
  const badge = container.querySelector('#phValueBadge');
  const sampleName = container.querySelector('#phSampleName');
  const colorName = container.querySelector('#phColorName');
  if (!svg || !slider) return;

  const phData = {
    0: { name: "Battery Acid (H2SO4)", color: "#ef4444", text: "Deep Red" },
    1: { name: "Stomach Gastric Acid (HCl)", color: "#f87171", text: "Red" },
    2: { name: "Lemon Juice", color: "#fb923c", text: "Red-Orange" },
    3: { name: "Vinegar (Acetic Acid)", color: "#f97316", text: "Orange" },
    4: { name: "Tomato Juice", color: "#fbbf24", text: "Orange-Yellow" },
    5: { name: "Black Coffee", color: "#facc15", text: "Yellow" },
    6: { name: "Fresh Cow Milk", color: "#a3e635", text: "Green-Yellow" },
    7: { name: "Pure Distilled Water", color: "#10b981", text: "Emerald Green" },
    8: { name: "Human Blood / Sea Water", color: "#06b6d4", text: "Blue-Green" },
    9: { name: "Baking Soda Solution", color: "#0ea5e9", text: "Cyan-Blue" },
    10: { name: "Bathing Soap Lather", color: "#3b82f6", text: "Blue" },
    11: { name: "Milk of Magnesia (Mg(OH)2)", color: "#6366f1", text: "Indigo" },
    12: { name: "Lime Water (Ca(OH)2)", color: "#8b5cf6", text: "Purple" },
    13: { name: "Household Bleach", color: "#a855f7", text: "Violet" },
    14: { name: "Drain Cleaner (NaOH)", color: "#7e22ce", text: "Deep Purple" }
  };

  function render() {
    const ph = parseFloat(slider.value);
    const rounded = Math.round(ph);
    const data = phData[rounded] || phData[7];

    if (badge) {
      badge.textContent = `pH ${ph.toFixed(1)}: ${data.name}`;
      badge.className = ph < 6.5 ?
        "px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold" :
        ph > 7.5 ?
        "px-2 py-0.5 rounded text-[11px] font-mono bg-blue-500/20 text-blue-300 border border-blue-500/30 font-semibold" :
        "px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold";
    }

    if (sampleName) sampleName.textContent = data.name;
    if (colorName) {
      colorName.textContent = data.text;
      colorName.style.color = data.color;
    }

    // Spectrum bar coordinates
    const barX = 30, barY = 60, barW = 440, barH = 30;
    const markerX = barX + (ph / 14) * barW;

    svg.innerHTML = `
      <defs>
        <linearGradient id="phRainbow" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#ef4444" />
          <stop offset="25%" stop-color="#f97316" />
          <stop offset="40%" stop-color="#facc15" />
          <stop offset="50%" stop-color="#10b981" />
          <stop offset="70%" stop-color="#0ea5e9" />
          <stop offset="85%" stop-color="#6366f1" />
          <stop offset="100%" stop-color="#7e22ce" />
        </linearGradient>
      </defs>

      <!-- Spectrum Bar -->
      <rect x="${barX}" y="${barY}" width="${barW}" height="${barH}" rx="6" fill="url(#phRainbow)" />

      <!-- Scale Ticks (0, 7, 14) -->
      <text x="${barX + 5}" y="${barY + 20}" fill="#ffffff" font-size="11" font-weight="extrabold">0</text>
      <text x="${barX + barW / 2}" y="${barY + 20}" fill="#ffffff" font-size="11" font-weight="extrabold" text-anchor="middle">7</text>
      <text x="${barX + barW - 15}" y="${barY + 20}" fill="#ffffff" font-size="11" font-weight="extrabold">14</text>

      <!-- Active Position Pointer -->
      <polygon points="${markerX - 8},${barY - 14} ${markerX + 8},${barY - 14} ${markerX},${barY - 2}" fill="#ffffff" />
      <line x1="${markerX}" y1="${barY}" x2="${markerX}" y2="${barY + barH}" stroke="#ffffff" stroke-width="3" />

      <!-- Sample Indicator Flask -->
      <circle cx="250" cy="155" r="30" fill="${data.color}" stroke="#ffffff" stroke-width="2.5" />
      <text x="250" y="160" fill="#ffffff" font-size="14" font-weight="extrabold" text-anchor="middle">pH ${ph.toFixed(1)}</text>
      <text x="250" y="205" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">${data.name}</text>
    `;
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 9. Neutralisation Reaction Chamber Simulator
// -------------------------------------------------------------
function initNeutralisationChamberSim(container) {
  const svg = container.querySelector('#neutReactSvg');
  const badge = container.querySelector('#reactionStateBadge');
  const tempEl = container.querySelector('#tempReadout');
  const btn = container.querySelector('#triggerReactionBtn');
  if (!svg || !btn) return;

  let reacted = false;

  function render() {
    if (badge) {
      badge.textContent = reacted ? "Neutralised: Salt + Water + Heat Released!" : "Ready: Unmixed Acid & Base";
      badge.className = reacted ?
        "px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" :
        "px-2 py-0.5 rounded text-[11px] font-mono bg-slate-800 text-slate-300 border border-slate-700 font-semibold";
    }

    if (tempEl) {
      tempEl.textContent = reacted ? "Thermometer: 38.5°C (+14.5°C Rise Exothermic!)" : "Thermometer: 24.0°C (Ambient)";
    }

    svg.innerHTML = `
      <!-- Center Reaction Beaker -->
      <rect x="180" y="70" width="140" height="130" rx="8" fill="#0f172a" stroke="#475569" stroke-width="2.5" />
      <rect x="182" y="115" width="136" height="83" rx="4" fill="${reacted ? '#10b981' : '#334155'}" fill-opacity="${reacted ? '0.4' : '0.2'}" />

      ${reacted ? `
        <!-- Steam heat waves -->
        <path d="M 220 100 Q 225 80 220 60" stroke="#f59e0b" stroke-width="2" fill="none" opacity="0.8" />
        <path d="M 250 95 Q 255 75 250 55" stroke="#f59e0b" stroke-width="2" fill="none" opacity="0.8" />
        <path d="M 280 100 Q 285 80 280 60" stroke="#f59e0b" stroke-width="2" fill="none" opacity="0.8" />
        <!-- Salt crystals forming -->
        <rect x="235" y="170" width="8" height="8" fill="#ffffff" />
        <rect x="255" y="175" width="8" height="8" fill="#ffffff" />
        <text x="250" y="150" fill="#a7f3d0" font-size="12" font-weight="extrabold" text-anchor="middle">NaCl + H2O (Warm)</text>
      ` : `
        <text x="250" y="150" fill="#94a3b8" font-size="11" text-anchor="middle">Click Below to Mix</text>
      `}

      <!-- Left Flask: HCl Acid -->
      <g transform="translate(60, 80)">
        <polygon points="20,0 40,0 55,60 5,60" fill="#f43f5e" fill-opacity="0.4" stroke="#f43f5e" stroke-width="2" />
        <text x="30" y="80" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">HCl (Acid)</text>
      </g>

      <!-- Right Flask: NaOH Base -->
      <g transform="translate(380, 80)">
        <polygon points="20,0 40,0 55,60 5,60" fill="#0284c7" fill-opacity="0.4" stroke="#0284c7" stroke-width="2" />
        <text x="30" y="80" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">NaOH (Base)</text>
      </g>

      <!-- Reaction Formula -->
      <text x="250" y="35" fill="#facc15" font-size="12" font-weight="bold" text-anchor="middle">
        HCl + NaOH ➔ NaCl (Salt) + H2O + Heat
      </text>
    `;
  }

  btn.addEventListener('click', () => {
    reacted = !reacted;
    render();
  });

  render();
}

// -------------------------------------------------------------
// 10. Titration Burette Simulator
// -------------------------------------------------------------
function initTitrationBuretteSim(container) {
  const svg = container.querySelector('#titrationSvg');
  const badge = container.querySelector('#titrationBadge');
  const dropsText = container.querySelector('#titrationDropsText');
  const bDrop = container.querySelector('#dispenseDropBtn');
  const bReset = container.querySelector('#resetTitrationBtn');
  if (!svg || !bDrop) return;

  let drops = 0; // at 10 drops, turns permanent pink!

  function render() {
    const isPink = drops >= 10;
    if (badge) {
      badge.textContent = isPink ? "End-Point Reached: PERMANENT FAINT PINK ✔" : "Flask Solution: Acidic (Colorless)";
      badge.className = isPink ?
        "px-2 py-0.5 rounded text-[11px] font-mono bg-pink-500/20 text-pink-300 border border-pink-500/30 font-semibold" :
        "px-2 py-0.5 rounded text-[11px] font-mono bg-slate-800 text-slate-300 border border-slate-700 font-semibold";
    }

    if (dropsText) {
      dropsText.textContent = `Base Added: ${(drops * 1.0).toFixed(1)} mL (${drops} drops)`;
    }

    svg.innerHTML = `
      <!-- Burette Stand -->
      <line x1="210" y1="20" x2="210" y2="210" stroke="#475569" stroke-width="4" />
      <line x1="160" y1="210" x2="260" y2="210" stroke="#475569" stroke-width="6" />

      <!-- Glass Burette Tube -->
      <rect x="235" y="20" width="20" height="110" rx="2" fill="#0284c7" fill-opacity="0.2" stroke="#94a3b8" stroke-width="1.5" />
      <!-- Stopcock valve -->
      <rect x="230" y="130" width="30" height="8" rx="2" fill="#f59e0b" />
      <polygon points="245,138 245,148" stroke="#94a3b8" stroke-width="2" />

      <!-- Falling Droplet -->
      ${drops > 0 ? `<circle cx="245" cy="155" r="3" fill="#38bdf8" />` : ''}

      <!-- Conical Flask Below -->
      <polygon points="230,165 260,165 295,210 195,210" fill="${isPink ? '#ec4899' : '#0284c7'}" fill-opacity="${isPink ? '0.7' : '0.1'}" stroke="#cbd5e1" stroke-width="2" />
      <text x="245" y="195" fill="${isPink ? '#ffffff' : '#94a3b8'}" font-size="10" font-weight="bold" text-anchor="middle">
        ${isPink ? 'Pink End-point!' : 'Colorless'}
      </text>

      <!-- Legend Card -->
      <g transform="translate(330, 60)">
        <rect x="0" y="0" width="140" height="100" rx="8" fill="#1e293b" stroke="#334155" />
        <text x="15" y="25" fill="#f472b6" font-size="11" font-weight="bold">TITRATION STATUS</text>
        <text x="15" y="48" fill="#94a3b8" font-size="10">Target: 10.0 mL</text>
        <text x="15" y="68" fill="#cbd5e1" font-size="10">Current: ${(drops * 1.0).toFixed(1)} mL</text>
        <text x="15" y="88" fill="${isPink ? '#34d399' : '#fb7185'}" font-size="10" font-weight="bold">
          ${isPink ? 'Exact Equivalence ✔' : 'Acid in Excess...'}
        </text>
      </g>
    `;
  }

  bDrop.addEventListener('click', () => {
    if (drops < 12) drops++;
    render();
  });

  if (bReset) {
    bReset.addEventListener('click', () => {
      drops = 0;
      render();
    });
  }

  render();
}

// -------------------------------------------------------------
// 11. Ant Bite Neutraliser Simulator
// -------------------------------------------------------------
function initAntBiteNeutraliserSim(container) {
  const svg = container.querySelector('#antBiteSvg');
  const status = container.querySelector('#antBiteStatus');
  const bBaking = container.querySelector('#applyBakingSodaBtn');
  const bCalamine = container.querySelector('#applyCalamineBtn');
  if (!svg || !bBaking || !bCalamine) return;

  function render(remedy) {
    const isNeutralized = remedy !== 'none';
    if (status) {
      status.textContent = isNeutralized ? `Neutralised with ${remedy}! Pain Relieved ✔` : "Skin: Acidic Formic Injection ⚠️";
      status.className = isNeutralized ?
        "px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" :
        "px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold";
    }

    svg.innerHTML = `
      <!-- Skin Cross-Section -->
      <rect x="40" y="120" width="420" height="90" rx="8" fill="#fda4af" stroke="#f43f5e" stroke-width="2" />
      <text x="60" y="140" fill="#9f1239" font-size="10" font-weight="bold">Epidermis (Skin Layer)</text>

      ${isNeutralized ? `
        <!-- White soothing paste applied on top -->
        <path d="M 200 120 Q 250 105 300 120 Z" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" />
        <text x="250" y="112" fill="#0284c7" font-size="10" font-weight="bold" text-anchor="middle">${remedy}</text>
        
        <!-- Neutralised Salt & Water droplet inside skin -->
        <circle cx="250" cy="160" r="14" fill="#34d399" opacity="0.6" />
        <text x="250" y="164" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Neutral Salt</text>

        <text x="250" y="55" fill="#34d399" font-size="13" font-weight="extrabold" text-anchor="middle">
          Pain & Inflammation Relieved! (Acid + Base ➔ Salt + H2O)
        </text>
      ` : `
        <!-- Ant Stinger injecting Formic Acid (Red) -->
        <polygon points="250,90 245,125 255,125" fill="#1e293b" />
        <circle cx="250" cy="155" r="24" fill="#ef4444" opacity="0.8" />
        <text x="250" y="159" fill="#ffffff" font-size="10" font-weight="extrabold" text-anchor="middle">Formic Acid</text>
        
        <text x="250" y="55" fill="#f43f5e" font-size="13" font-weight="extrabold" text-anchor="middle">
          Stinging Burning Sensation! (HCOOH Injected)
        </text>
      `}
    `;
  }

  bBaking.addEventListener('click', () => render('Baking Soda (NaHCO3)'));
  bCalamine.addEventListener('click', () => render('Calamine (ZnCO3)'));

  render('none');
}

// -------------------------------------------------------------
// 12. Soil pH Management Simulator
// -------------------------------------------------------------
function initSoilPhManagementSim(container) {
  const svg = container.querySelector('#soilSvg');
  const badge = container.querySelector('#soilStatusBadge');
  const bLime = container.querySelector('#addLimeBtn');
  const bManure = container.querySelector('#addManureBtn');
  if (!svg || !bLime || !bManure) return;

  function render(state) {
    let ph = 4.8;
    let cropColor = "#ca8a04"; // yellowed/wilted
    let badgeText = "Soil: Excessively Acidic (pH 4.8)";

    if (state === 'limed') {
      ph = 6.8;
      cropColor = "#22c55e"; // lush green
      badgeText = "Slaked Lime Added ➔ Optimal Fertile pH (6.8) ✔";
    } else if (state === 'manure') {
      ph = 7.0;
      cropColor = "#22c55e";
      badgeText = "Organic Manure Added ➔ Balanced Neutral Soil (7.0) ✔";
    }

    if (badge) {
      badge.textContent = badgeText;
      badge.className = ph >= 6.5 && ph <= 7.5 ?
        "px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" :
        "px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold";
    }

    svg.innerHTML = `
      <!-- Soil Ground Base -->
      <rect x="40" y="130" width="420" height="80" rx="4" fill="#78350f" stroke="#451a03" stroke-width="2" />
      <text x="60" y="195" fill="#d97706" font-size="10" font-weight="bold">Agricultural Soil Layer</text>

      <!-- Crops / Plants -->
      ${[120, 200, 280, 360].map(x => `
        <line x1="${x}" y1="130" x2="${x}" y2="75" stroke="${cropColor}" stroke-width="4" />
        <ellipse cx="${x - 10}" cy="90" rx="12" ry="6" fill="${cropColor}" transform="rotate(-30 ${x - 10} 90)" />
        <ellipse cx="${x + 10}" cy="85" rx="12" ry="6" fill="${cropColor}" transform="rotate(30 ${x + 10} 85)" />
      `).join('')}

      <!-- Soil pH Meter Probe -->
      <g transform="translate(60, 40)">
        <rect x="0" y="0" width="60" height="50" rx="6" fill="#1e293b" stroke="#64748b" />
        <text x="30" y="22" fill="#94a3b8" font-size="9" text-anchor="middle">SOIL pH</text>
        <text x="30" y="42" fill="${ph >= 6.5 ? '#34d399' : '#f87171'}" font-size="14" font-weight="extrabold" text-anchor="middle">${ph.toFixed(1)}</text>
        <line x1="30" y1="50" x2="30" y2="140" stroke="#94a3b8" stroke-width="2.5" />
      </g>
    `;
  }

  bLime.addEventListener('click', () => render('limed'));
  bManure.addEventListener('click', () => render('manure'));

  render('acid');
}

// -------------------------------------------------------------
// 13. Factory Effluent Plant Simulator
// -------------------------------------------------------------
function initFactoryEffluentSim(container) {
  const svg = container.querySelector('#effluentSvg');
  const slider = container.querySelector('#limeValveSlider');
  const badge = container.querySelector('#riverSafetyBadge');
  const doseText = container.querySelector('#limeDoseText');
  if (!svg || !slider) return;

  function render() {
    const valve = parseInt(slider.value, 10); // 0 to 100%
    const ph = (2.5 + (valve / 100) * 4.6).toFixed(1);
    const isSafe = ph >= 6.5;

    if (doseText) doseText.textContent = `Lime Dosing: ${valve}% (Treated pH: ${ph})`;

    if (badge) {
      badge.textContent = isSafe ? `River Ecosystem Safe (pH ${ph}) ✔` : `CRITICAL HAZARD: Acid Polluting River (pH ${ph}) ⚠️`;
      badge.className = isSafe ?
        "px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" :
        "px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold";
    }

    svg.innerHTML = `
      <!-- Factory Outline at Left -->
      <polygon points="30,120 70,80 70,120 110,80 110,160 30,160" fill="#334155" stroke="#64748b" />
      <text x="70" y="150" fill="#ffffff" font-size="9" text-anchor="middle">Chemical Plant</text>

      <!-- Acid Pipe Flowing Out -->
      <rect x="110" y="130" width="70" height="15" fill="#f43f5e" />

      <!-- Neutralisation Reaction Tank in Middle -->
      <rect x="180" y="90" width="120" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
      <rect x="182" y="125" width="116" height="53" rx="4" fill="${isSafe ? '#10b981' : '#f43f5e'}" fill-opacity="0.4" />
      <text x="240" y="112" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">ETP Tank (pH ${ph})</text>

      <!-- Lime Hopper adding base -->
      <polygon points="225,50 255,50 245,85 235,85" fill="#ffffff" stroke="#94a3b8" />
      <text x="240" y="42" fill="#ffffff" font-size="9" text-anchor="middle">Slaked Lime (${valve}%)</text>

      <!-- Outflow into River at Right -->
      <rect x="300" y="130" width="50" height="15" fill="${isSafe ? '#0284c7' : '#f43f5e'}" />

      <!-- River with Fish -->
      <rect x="350" y="100" width="120" height="80" rx="6" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" />
      ${isSafe ? `
        <text x="410" y="135" font-size="18">🐟</text>
        <text x="390" y="155" font-size="14">🐠</text>
        <text x="410" y="172" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">Thriving Aquatic Life</text>
      ` : `
        <text x="410" y="135" font-size="16">💀</text>
        <text x="410" y="165" fill="#f87171" font-size="9" font-weight="bold" text-anchor="middle">Acidic Danger!</text>
      `}
    `;
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 14. Antacid & Dental Health Simulator
// -------------------------------------------------------------
function initBioHealthSim(container) {
  const svg = container.querySelector('#bioHealthSvg');
  const badge = container.querySelector('#bioModeBadge');
  const bStomach = container.querySelector('#toggleStomachBtn');
  const bDental = container.querySelector('#toggleDentalBtn');
  if (!svg || !bStomach || !bDental) return;

  function render(mode) {
    if (mode === 'stomach') {
      badge.textContent = "Stomach: Antacid Neutralises Excess HCl";
      badge.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-blue-500/20 text-blue-300 border border-blue-500/30 font-semibold";

      svg.innerHTML = `
        <!-- Stomach Outline -->
        <path d="M 170 80 Q 140 130 190 180 Q 250 200 300 160 Q 320 110 270 80 Z" fill="#f43f5e" fill-opacity="0.2" stroke="#f43f5e" stroke-width="2.5" />
        <text x="240" y="115" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Stomach Cavity</text>
        
        <!-- Gastric HCl + Milk of Magnesia -->
        <rect x="200" y="130" width="80" height="35" rx="6" fill="#38bdf8" fill-opacity="0.6" />
        <text x="240" y="152" fill="#ffffff" font-size="10" font-weight="extrabold" text-anchor="middle">Mg(OH)2 + HCl</text>

        <!-- Explanation Callout -->
        <text x="250" y="45" fill="#38bdf8" font-size="13" font-weight="extrabold" text-anchor="middle">
          Mg(OH)2 + 2HCl ➔ MgCl2 + 2H2O (Heartburn Relieved!)
        </text>
      `;
    } else {
      badge.textContent = "Dental: Alkaline Toothpaste Neutralises Mouth Acid";
      badge.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold";

      svg.innerHTML = `
        <!-- Healthy White Tooth with Enamel Shield -->
        <path d="M 220 70 C 200 70 190 110 200 160 C 210 190 230 170 240 140 C 250 170 270 190 280 160 C 290 110 280 70 260 70 Z" fill="#f8fafc" stroke="#38bdf8" stroke-width="3" />
        
        <!-- Toothpaste Lather (Mild Alkali) -->
        <circle cx="230" cy="95" r="12" fill="#06b6d4" fill-opacity="0.5" />
        <circle cx="250" cy="90" r="10" fill="#06b6d4" fill-opacity="0.5" />
        
        <text x="240" y="125" fill="#0284c7" font-size="10" font-weight="bold" text-anchor="middle">Enamel Shield</text>

        <text x="250" y="45" fill="#34d399" font-size="13" font-weight="extrabold" text-anchor="middle">
          Alkaline Toothpaste Neutralises Bacterial Acid (Prevents Cavities)
        </text>
      `;
    }
  }

  bStomach.addEventListener('click', () => {
    bStomach.className = "px-3 py-2 rounded-xl bg-blue-600 text-white font-bold transition";
    bDental.className = "px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition";
    render('stomach');
  });

  bDental.addEventListener('click', () => {
    bDental.className = "px-3 py-2 rounded-xl bg-emerald-600 text-white font-bold transition";
    bStomach.className = "px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition";
    render('dental');
  });

  render('stomach');
}

// -------------------------------------------------------------
// 15. Acharya P.C. Ray Historical Lab Simulator
// -------------------------------------------------------------
function initPcRayHeritageSim(container) {
  const svg = container.querySelector('#pcRaySvg');
  const badge = container.querySelector('#pcRayBadge');
  const btns = container.querySelectorAll('.rayBtn');
  if (!svg) return;

  function render(view) {
    if (view === 'nitrite') {
      if (badge) badge.textContent = "Mercurous Nitrite Discovery (1896)";
      svg.innerHTML = `
        <rect x="30" y="30" width="440" height="180" rx="12" fill="#0f172a" stroke="#f59e0b" stroke-width="2" />
        <circle cx="85" cy="85" r="32" fill="#1e293b" stroke="#f59e0b" stroke-width="2" />
        <text x="85" y="93" font-size="24" text-anchor="middle">🧪</text>
        <text x="135" y="65" fill="#f8fafc" font-size="14" font-weight="extrabold">Synthesis of Mercurous Nitrite [Hg2(NO2)2]</text>
        <text x="135" y="85" fill="#f59e0b" font-size="11" font-weight="bold">Presidency College Laboratory, Kolkata (1896)</text>
        
        <foreignObject x="60" y="115" width="380" height="80">
          <div xmlns="http://www.w3.org/1999/xhtml" style="font-size: 11px; color: #cbd5e1; line-height: 1.45;">
            By reacting liquid mercury with dilute nitric acid under carefully controlled temperature, P.C. Ray synthesized yellow crystalline mercurous nitrite, a compound previously declared impossible by Western chemists!
          </div>
        </foreignObject>
      `;
    } else if (view === 'bengal') {
      if (badge) badge.textContent = "Bengal Chemicals (1901)";
      svg.innerHTML = `
        <rect x="30" y="30" width="440" height="180" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2" />
        <circle cx="85" cy="85" r="32" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
        <text x="85" y="93" font-size="24" text-anchor="middle">🏭</text>
        <text x="135" y="65" fill="#f8fafc" font-size="14" font-weight="extrabold">Bengal Chemical & Pharmaceutical Works</text>
        <text x="135" y="85" fill="#38bdf8" font-size="11" font-weight="bold">India's First Indigenous Pharmaceutical Enterprise (1901)</text>

        <foreignObject x="60" y="115" width="380" height="80">
          <div xmlns="http://www.w3.org/1999/xhtml" style="font-size: 11px; color: #cbd5e1; line-height: 1.45;">
            Founded with modest capital in his rented home, Ray built an industrial giant manufacturing sulfuric acid, pharmaceutical syrups, and surgical dressings to free India from dependence on foreign imports.
          </div>
        </foreignObject>
      `;
    } else {
      if (badge) badge.textContent = "History of Hindu Chemistry";
      svg.innerHTML = `
        <rect x="30" y="30" width="440" height="180" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="2" />
        <circle cx="85" cy="85" r="32" fill="#1e293b" stroke="#10b981" stroke-width="2" />
        <text x="85" y="93" font-size="24" text-anchor="middle">📜</text>
        <text x="135" y="65" fill="#f8fafc" font-size="14" font-weight="extrabold">Rasashastra: A History of Hindu Chemistry</text>
        <text x="135" y="85" fill="#10b981" font-size="11" font-weight="bold">Masterwork of Ancient Indian Alchemical Heritage</text>

        <foreignObject x="60" y="115" width="380" height="80">
          <div xmlns="http://www.w3.org/1999/xhtml" style="font-size: 11px; color: #cbd5e1; line-height: 1.45;">
            Ray translated ancient Sanskrit manuscripts to demonstrate that Indian metallurgists had mastered caustic alkalis (Kṣāra), mineral acids (Amla), zinc smelting, and distillation centuries before the West.
          </div>
        </foreignObject>
      `;
    }
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.className = "rayBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition");
      btn.className = "rayBtn px-2 py-1.5 rounded-lg bg-amber-600 text-white font-bold transition";
      render(btn.dataset.view);
    });
  });

  render('nitrite');
}

// -------------------------------------------------------------
// 16. Master Substance Wheel & Equation Generator Simulator
// -------------------------------------------------------------
function initMasterSubstanceWheelSim(container) {
  const svg = container.querySelector('#synthSvg');
  const badge = container.querySelector('#synthSaltBadge');
  const selAcid = container.querySelector('#synthAcidSelect');
  const selBase = container.querySelector('#synthBaseSelect');
  if (!svg || !selAcid || !selBase) return;

  const pairs = {
    "hcl-naoh": { salt: "Sodium Chloride (NaCl)", eq: "HCl + NaOH ➔ NaCl + H2O + Heat" },
    "hcl-koh": { salt: "Potassium Chloride (KCl)", eq: "HCl + KOH ➔ KCl + H2O + Heat" },
    "hcl-caoh2": { salt: "Calcium Chloride (CaCl2)", eq: "2HCl + Ca(OH)2 ➔ CaCl2 + 2H2O + Heat" },
    "hcl-mgoh2": { salt: "Magnesium Chloride (MgCl2)", eq: "2HCl + Mg(OH)2 ➔ MgCl2 + 2H2O + Heat" },
    "h2so4-naoh": { salt: "Sodium Sulfate (Na2SO4)", eq: "H2SO4 + 2NaOH ➔ Na2SO4 + 2H2O + Heat" },
    "h2so4-koh": { salt: "Potassium Sulfate (K2SO4)", eq: "H2SO4 + 2KOH ➔ K2SO4 + 2H2O + Heat" },
    "h2so4-caoh2": { salt: "Calcium Sulfate (CaSO4)", eq: "H2SO4 + Ca(OH)2 ➔ CaSO4 + 2H2O + Heat" },
    "h2so4-mgoh2": { salt: "Magnesium Sulfate (MgSO4)", eq: "H2SO4 + Mg(OH)2 ➔ MgSO4 + 2H2O + Heat" },
    "hno3-naoh": { salt: "Sodium Nitrate (NaNO3)", eq: "HNO3 + NaOH ➔ NaNO3 + H2O + Heat" },
    "hno3-koh": { salt: "Potassium Nitrate (KNO3)", eq: "HNO3 + KOH ➔ KNO3 + H2O + Heat" },
    "hno3-caoh2": { salt: "Calcium Nitrate (Ca(NO3)2)", eq: "2HNO3 + Ca(OH)2 ➔ Ca(NO3)2 + 2H2O + Heat" },
    "hno3-mgoh2": { salt: "Magnesium Nitrate (Mg(NO3)2)", eq: "2HNO3 + Mg(OH)2 ➔ Mg(NO3)2 + 2H2O + Heat" },
    "ch3cooh-naoh": { salt: "Sodium Acetate (CH3COONa)", eq: "CH3COOH + NaOH ➔ CH3COONa + H2O + Heat" },
    "ch3cooh-koh": { salt: "Potassium Acetate (CH3COOK)", eq: "CH3COOH + KOH ➔ CH3COOK + H2O + Heat" },
    "ch3cooh-caoh2": { salt: "Calcium Acetate ((CH3COO)2Ca)", eq: "2CH3COOH + Ca(OH)2 ➔ (CH3COO)2Ca + 2H2O + Heat" },
    "ch3cooh-mgoh2": { salt: "Magnesium Acetate ((CH3COO)2Mg)", eq: "2CH3COOH + Mg(OH)2 ➔ (CH3COO)2Mg + 2H2O + Heat" }
  };

  function render() {
    const key = `${selAcid.value}-${selBase.value}`;
    const data = pairs[key] || pairs["hcl-naoh"];

    if (badge) badge.textContent = `Salt: ${data.salt}`;

    svg.innerHTML = `
      <!-- Equation Box -->
      <rect x="30" y="25" width="440" height="60" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2" />
      <text x="250" y="55" fill="#a7f3d0" font-size="14" font-weight="extrabold" text-anchor="middle">
        ${data.eq}
      </text>
      <text x="250" y="73" fill="#fde68a" font-size="10" text-anchor="middle">Exothermic Enthalpy: ΔH = -57.3 kJ/mol</text>

      <!-- Three Metric Cards -->
      <!-- Acid Card -->
      <g transform="translate(40, 100)">
        <rect x="0" y="0" width="120" height="95" rx="8" fill="#1e293b" stroke="#f43f5e" />
        <text x="60" y="25" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">ACID REACTANT</text>
        <text x="60" y="50" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">${selAcid.value.toUpperCase()}</text>
        <text x="60" y="75" fill="#94a3b8" font-size="9" text-anchor="middle">Blue Litmus ➔ Red</text>
      </g>

      <!-- Plus Sign -->
      <text x="180" y="155" fill="#94a3b8" font-size="20" font-weight="bold" text-anchor="middle">+</text>

      <!-- Base Card -->
      <g transform="translate(200, 100)">
        <rect x="0" y="0" width="120" height="95" rx="8" fill="#1e293b" stroke="#38bdf8" />
        <text x="60" y="25" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">BASE REACTANT</text>
        <text x="60" y="50" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">${selBase.value.toUpperCase()}</text>
        <text x="60" y="75" fill="#94a3b8" font-size="9" text-anchor="middle">Red Litmus ➔ Blue</text>
      </g>

      <!-- Equals Arrow -->
      <text x="340" y="155" fill="#94a3b8" font-size="20" font-weight="bold" text-anchor="middle">➔</text>

      <!-- Salt Product Card -->
      <g transform="translate(360, 100)">
        <rect x="0" y="0" width="110" height="95" rx="8" fill="#064e3b" stroke="#10b981" />
        <text x="55" y="25" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">SALT PRODUCT</text>
        <text x="55" y="55" fill="#ffffff" font-size="10" font-weight="extrabold" text-anchor="middle">${data.salt.split(' ')[0]}</text>
        <text x="55" y="75" fill="#a7f3d0" font-size="9" text-anchor="middle">+ Water + Heat</text>
      </g>
    `;
  }

  selAcid.addEventListener('change', render);
  selBase.addEventListener('change', render);
  render();
}
'''

with open(".agents/class7_science_substances_js.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 7 Science Chapter 2: Exploring Substances JS Engine"""\n\n')
    f.write("SIMULATORS_JS = " + repr(JS_CODE) + "\n")

print("Generated .agents/class7_science_substances_js.py successfully.")

