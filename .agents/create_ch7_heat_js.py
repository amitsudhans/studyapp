# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Science Chapter 7 Simulator JavaScript Engines
Outputs .agents/class7_science_heat_js.py
"""

JS_CODE = r"""
// Master Simulator Dispatcher for Chapter 7: Heat Transfer in Nature
function initSimulatorForSlide(slideId, container) {
  if (!container) return;

  switch(slideId) {
    case 1:
      initConductionWaxPinsSim(container);
      break;
    case 2:
      initConductorsInsulatorsSim(container);
      break;
    case 3:
      initTrappedAirInsulationSim(container);
      break;
    case 4:
      initConvectionCurrentsSim(container);
      break;
    case 5:
      initGasConvectionSpiralSim(container);
      break;
    case 6:
      initSeaBreezeSim(container);
      break;
    case 7:
      initLandBreezeSim(container);
      break;
    case 8:
      initThermalRadiationSim(container);
      break;
    case 9:
      initBlackWhiteRadiationSim(container);
      break;
    case 10:
      initThermosFlaskSim(container);
      break;
    case 11:
      initWaterCycleEvapSim(container);
      break;
    case 12:
      initCloudCondensationSim(container);
      break;
    case 13:
      initPrecipitationTypesSim(container);
      break;
    case 14:
      initSoilInfiltrationSim(container);
      break;
    case 15:
      initAquiferIceStupaSim(container);
      break;
    case 16:
      initAncientHeritageCoolingSim(container);
      break;
  }
}

// -------------------------------------------------------------
// Sim 1: Conduction: Metal Strip with Wax-Attached Pins
// -------------------------------------------------------------
function initConductionWaxPinsSim(c) {
  const badge = c.querySelector('#conductionStatusBadge');
  const btnIgnite = c.querySelector('#btnIgniteBurner');
  const btnReset = c.querySelector('#btnResetConduction');
  const flame = c.querySelector('#burnerFlame');
  const gradientOverlay = c.querySelector('#thermalGradientOverlay');
  const annotation = c.querySelector('#conductionAnnotation');
  const explanation = c.querySelector('#conductionExplanation');

  const pins = [
    { group: c.querySelector('#pinGroup1'), wax: c.querySelector('#wax1'), origX: 130 },
    { group: c.querySelector('#pinGroup2'), wax: c.querySelector('#wax2'), origX: 195 },
    { group: c.querySelector('#pinGroup3'), wax: c.querySelector('#wax3'), origX: 260 },
    { group: c.querySelector('#pinGroup4'), wax: c.querySelector('#wax4'), origX: 325 }
  ];

  let timers = [];
  let isHeating = false;

  function resetApparatus() {
    timers.forEach(t => clearTimeout(t));
    timers = [];
    isHeating = false;

    if (flame) flame.classList.add('hidden');
    if (gradientOverlay) gradientOverlay.setAttribute('width', '0');
    if (badge) {
      badge.textContent = 'Burner: OFF';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-mono font-bold';
    }
    if (annotation) {
      annotation.textContent = 'Click "Ignite Burner" to observe progressive heat conduction';
      annotation.setAttribute('fill', '#94a3b8');
    }

    pins.forEach((p, idx) => {
      if (p.group) {
        p.group.setAttribute('transform', `translate(${p.origX}, 58)`);
      }
      if (p.wax) {
        p.wax.setAttribute('fill', '#fef08a');
      }
    });

    if (explanation) {
      explanation.innerHTML = `🧪 <span class="font-bold text-amber-300">Activity 7.1 Observation:</span> Solid metal particles vibrate in fixed positions. Heat conducts progressively from the flame toward the cold end. Pins drop off one by one as the conduction wave melts each wax seal!`;
    }
  }

  function igniteBurner() {
    if (isHeating) return;
    resetApparatus();
    isHeating = true;

    if (flame) flame.classList.remove('hidden');
    if (badge) {
      badge.textContent = 'Burner: ACTIVE (Heating Left End)';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-rose-400 font-mono font-bold';
    }
    if (annotation) {
      annotation.textContent = 'Thermal kinetic wave conducting left to right →';
      annotation.setAttribute('fill', '#f59e0b');
    }

    // Animate gradient expansion across the rod
    let start = null;
    function expandGradient(timestamp) {
      if (!isHeating) return;
      if (!start) start = timestamp;
      const progress = Math.min((timestamp - start) / 8000, 1);
      if (gradientOverlay) {
        gradientOverlay.setAttribute('width', `${progress * 310}`);
      }
      if (progress < 1) {
        requestAnimationFrame(expandGradient);
      }
    }
    requestAnimationFrame(expandGradient);

    // Sequential pin drop schedule
    // Pin 1 at t = 1.6s
    timers.push(setTimeout(() => {
      if (!isHeating) return;
      pins[0].group.setAttribute('transform', `translate(130, 140) rotate(70)`);
      pins[0].wax.setAttribute('fill', '#a1a1aa');
      if (annotation) annotation.textContent = 'Pin 1 dropped! Wax melted at 55 °C.';
    }, 1600));

    // Pin 2 at t = 3.6s
    timers.push(setTimeout(() => {
      if (!isHeating) return;
      pins[1].group.setAttribute('transform', `translate(195, 140) rotate(75)`);
      pins[1].wax.setAttribute('fill', '#a1a1aa');
      if (annotation) annotation.textContent = 'Pin 2 dropped! Heat wave reaches mid-rod.';
    }, 3600));

    // Pin 3 at t = 5.6s
    timers.push(setTimeout(() => {
      if (!isHeating) return;
      pins[2].group.setAttribute('transform', `translate(260, 140) rotate(80)`);
      pins[2].wax.setAttribute('fill', '#a1a1aa');
      if (annotation) annotation.textContent = 'Pin 3 dropped! Conduction continuing outward.';
    }, 5600));

    // Pin 4 at t = 7.6s
    timers.push(setTimeout(() => {
      if (!isHeating) return;
      pins[3].group.setAttribute('transform', `translate(325, 140) rotate(85)`);
      pins[3].wax.setAttribute('fill', '#a1a1aa');
      if (annotation) annotation.textContent = 'All 4 pins dropped! Progressive conduction demonstrated.';
      if (badge) {
        badge.textContent = 'Conduction: Full Propagation';
        badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-mono font-bold';
      }
    }, 7600));
  }

  if (btnIgnite) btnIgnite.addEventListener('click', igniteBurner);
  if (btnReset) btnReset.addEventListener('click', resetApparatus);

  resetApparatus();
}

// -------------------------------------------------------------
// Sim 2: Thermal Conductors vs Insulators
// -------------------------------------------------------------
function initConductorsInsulatorsSim(c) {
  const badge = c.querySelector('#materialClassificationBadge');
  const shaft = c.querySelector('#testedRodShaft');
  const sensor = c.querySelector('#handleHeatSensor');
  const tempText = c.querySelector('#handleTempText');

  const cardName = c.querySelector('#cardMatName');
  const cardK = c.querySelector('#cardMatK');
  const cardSpeed = c.querySelector('#cardMatSpeed');
  const cardVerdict = c.querySelector('#cardMatVerdict');
  const explanation = c.querySelector('#materialExplanation');
  const matBtns = c.querySelectorAll('.mat-btn');

  const materials = {
    copper: {
      name: "Copper Rod",
      fill: "#b45309", stroke: "#78350f",
      k: "k ≈ 385 W/(m·K)",
      speed: "Extremely Fast (~3s)",
      temp: "88 °C (Very Hot!)",
      tempColor: "#ef4444", sensorColor: "#ef4444",
      verdict: "Superior Conductor", verdictColor: "#4ade80",
      badgeText: "Good Conductor (Metals)", badgeClass: "text-emerald-400",
      desc: "Copper possesses a massive density of free conduction electrons. Energy transfers along the rod in seconds, making it ideal for cookware bottoms and heat exchangers."
    },
    aluminium: {
      name: "Aluminium Rod",
      fill: "#94a3b8", stroke: "#475569",
      k: "k ≈ 205 W/(m·K)",
      speed: "Very Fast (~5s)",
      temp: "82 °C (Hot!)",
      tempColor: "#f97316", sensorColor: "#f97316",
      verdict: "Good Conductor", verdictColor: "#4ade80",
      badgeText: "Good Conductor (Metals)", badgeClass: "text-emerald-400",
      desc: "Aluminium is lightweight with excellent thermal conductivity (~205 W/(m·K)). It is widely chosen for pressure cookers, saucepans, and vehicle engine blocks."
    },
    iron: {
      name: "Iron / Steel Rod",
      fill: "#64748b", stroke: "#334155",
      k: "k ≈ 79 W/(m·K)",
      speed: "Moderate (~12s)",
      temp: "72 °C (Warm)",
      tempColor: "#fbbf24", sensorColor: "#fbbf24",
      verdict: "Good Conductor", verdictColor: "#4ade80",
      badgeText: "Good Conductor (Metals)", badgeClass: "text-emerald-400",
      desc: "Iron conducts heat moderately well, sufficient for heavy tavas, frying pans, and radiators that retain heat evenly."
    },
    glass: {
      name: "Glass Rod",
      fill: "#38bdf8", stroke: "#0284c7",
      k: "k ≈ 0.8 W/(m·K)",
      speed: "Very Slow (~90s)",
      temp: "28 °C (Mild)",
      tempColor: "#38bdf8", sensorColor: "#38bdf8",
      verdict: "Thermal Insulator", verdictColor: "#f87171",
      badgeText: "Poor Conductor (Insulator)", badgeClass: "text-rose-400",
      desc: "Glass is an amorphous non-metal lacking free electrons. Heat conducts through sluggish molecular vibrations, making glass containers safe to handle."
    },
    wood: {
      name: "Wooden Spatula",
      fill: "#854d0e", stroke: "#451a03",
      k: "k ≈ 0.15 W/(m·K)",
      speed: "Negligible (>10 min)",
      temp: "24 °C (Cool)",
      tempColor: "#38bdf8", sensorColor: "#38bdf8",
      verdict: "Superior Insulator", verdictColor: "#f87171",
      badgeText: "Poor Conductor (Insulator)", badgeClass: "text-rose-400",
      desc: "Dry wood has microscopic cellulose air cavities that heavily restrict heat conduction. Wooden cooking spoons never burn your hands while stirring boiling curries!"
    },
    plastic: {
      name: "Bakelite / Plastic Rod",
      fill: "#0284c7", stroke: "#0369a1",
      k: "k ≈ 0.20 W/(m·K)",
      speed: "Negligible (>10 min)",
      temp: "24 °C (Cool)",
      tempColor: "#38bdf8", sensorColor: "#38bdf8",
      verdict: "Superior Insulator", verdictColor: "#f87171",
      badgeText: "Poor Conductor (Insulator)", badgeClass: "text-rose-400",
      desc: "Bakelite is a thermosetting plastic with low thermal conductivity. It is molded into cool-touch handles for pressure cookers, electric irons, and tea kettles."
    }
  };

  function selectMaterial(key) {
    const m = materials[key];
    if (!m) return;

    badge.textContent = m.badgeText;
    badge.className = `text-[11px] px-2 py-0.5 rounded-full bg-slate-800 ${m.badgeClass} font-bold`;

    shaft.setAttribute('fill', m.fill);
    shaft.setAttribute('stroke', m.stroke);

    sensor.setAttribute('fill', m.sensorColor);
    tempText.textContent = m.temp;
    tempText.setAttribute('fill', m.tempColor);

    cardName.textContent = m.name;
    cardK.textContent = m.k;
    cardSpeed.textContent = m.speed;
    cardVerdict.textContent = m.verdict;
    cardVerdict.setAttribute('fill', m.verdictColor);

    matBtns.forEach(b => {
      b.className = 'mat-btn p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs transition';
      if (b.dataset.mat === key) {
        b.className = 'mat-btn p-1.5 rounded-lg bg-amber-600 text-white font-bold text-xs transition shadow';
      }
    });

    explanation.innerHTML = `⚡ <span class="font-bold text-amber-300">${m.name}:</span> ${m.desc}`;
  }

  matBtns.forEach(btn => {
    btn.addEventListener('click', () => selectMaterial(btn.dataset.mat));
  });

  selectMaterial('copper');
}

// -------------------------------------------------------------
// Sim 3: Trapped Air Insulation Simulator
// -------------------------------------------------------------
function initTrappedAirInsulationSim(c) {
  const badge = c.querySelector('#blanketInsulBadge');
  const airGap = c.querySelector('#trappedAirGap');
  const layerInner = c.querySelector('#layerInner');
  const layerInnerTxt = c.querySelector('#layerInnerTxt');
  const layerOuter = c.querySelector('#layerOuter');
  const layerOuterTxt = c.querySelector('#layerOuterTxt');

  const heatBar = c.querySelector('#heatLossBar');
  const heatVal = c.querySelector('#heatLossVal');
  const verdict = c.querySelector('#thermalVerdict');
  const airNote = c.querySelector('#airLayerNote');
  const explanation = c.querySelector('#trappedAirExplanation');

  const btn2Thin = c.querySelector('#btnTwoThinBlankets');
  const btn1Thick = c.querySelector('#btnOneThickBlanket');
  const btnHollow = c.querySelector('#btnHollowBrick');

  function setTwoThin() {
    badge.textContent = '2 Thin Blankets Selected';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 font-bold';

    if (airGap) airGap.classList.remove('hidden');
    layerInner.setAttribute('width', '40');
    layerInner.setAttribute('fill', '#d97706');
    layerInnerTxt.textContent = 'Blanket 1';

    layerOuter.classList.remove('hidden');
    layerOuter.setAttribute('x', '65');
    layerOuter.setAttribute('width', '40');
    layerOuter.setAttribute('fill', '#d97706');
    layerOuterTxt.classList.remove('hidden');
    layerOuterTxt.textContent = 'Blanket 2';

    heatBar.setAttribute('width', '30');
    heatBar.setAttribute('fill', '#22c55e');
    heatVal.textContent = '14 W/m²';
    heatVal.setAttribute('fill', '#4ade80');
    verdict.textContent = 'Superior Warmth!';
    airNote.textContent = 'Trapped air layer blocks heat';

    explanation.innerHTML = `🛏️ <span class="font-bold text-amber-300">Why 2 Thin > 1 Thick:</span> The narrow space between two separate blankets traps a cushion of stationary air. Because still air is an exceptionally poor conductor of heat (k ≈ 0.026 W/(m·K)), this extra trapped air layer keeps you significantly warmer!`;
  }

  function setOneThick() {
    badge.textContent = '1 Thick Blanket Selected';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-rose-300 font-bold';

    if (airGap) airGap.classList.add('hidden');
    layerInner.setAttribute('width', '80');
    layerInner.setAttribute('fill', '#d97706');
    layerInnerTxt.textContent = 'Thick Blanket (80mm)';

    layerOuter.classList.add('hidden');
    layerOuterTxt.classList.add('hidden');

    heatBar.setAttribute('width', '65');
    heatBar.setAttribute('fill', '#f59e0b');
    heatVal.textContent = '38 W/m²';
    heatVal.setAttribute('fill', '#fbbf24');
    verdict.textContent = 'Moderate Warmth';
    airNote.textContent = 'No extra trapped air gap';

    explanation.innerHTML = `⚠️ <span class="font-bold text-amber-300">Single Layer Limitation:</span> Even though a thick blanket has identical wool mass, it lacks the secondary trapped air gap. Conduction proceeds continuously through the fibers, resulting in 2.7 times greater heat loss!`;
  }

  function setHollowBrick() {
    badge.textContent = 'Hollow Architectural Brick';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-bold';

    if (airGap) airGap.classList.remove('hidden');
    layerInner.setAttribute('width', '30');
    layerInner.setAttribute('fill', '#b45309');
    layerInnerTxt.textContent = 'Terracotta';

    layerOuter.classList.remove('hidden');
    layerOuter.setAttribute('x', '55');
    layerOuter.setAttribute('width', '30');
    layerOuter.setAttribute('fill', '#b45309');
    layerOuterTxt.classList.remove('hidden');
    layerOuterTxt.textContent = 'Terracotta';

    heatBar.setAttribute('width', '22');
    heatBar.setAttribute('fill', '#22c55e');
    heatVal.textContent = '10 W/m²';
    heatVal.setAttribute('fill', '#4ade80');
    verdict.textContent = 'Thermal Passive Shell';
    airNote.textContent = 'Air cavities shield indoor space';

    explanation.innerHTML = `🏛️ <span class="font-bold text-cyan-300">Architectural Efficiency:</span> Hollow bricks enclose motionless air cores. In blazing summer, outdoor heat cannot easily conduct into the house; in winter, interior warmth is retained, cutting AC and heater power bills.`;
  }

  if (btn2Thin) btn2Thin.addEventListener('click', setTwoThin);
  if (btn1Thick) btn1Thick.addEventListener('click', setOneThick);
  if (btnHollow) btnHollow.addEventListener('click', setHollowBrick);

  setTwoThin();
}

// -------------------------------------------------------------
// Sim 4: Liquid Convection (KMnO4 Plumes)
// -------------------------------------------------------------
function initConvectionCurrentsSim(c) {
  const badge = c.querySelector('#convectionIntensityBadge');
  const plume = c.querySelector('#risingPlume');
  const flame = c.querySelector('#liquidBurnerFlame');
  const btnToggle = c.querySelector('#btnToggleConvectionHeat');
  const btnCrystal = c.querySelector('#btnAddKMnO4Crystal');
  const explanation = c.querySelector('#liquidConvectionExplanation');

  let isHighHeat = true;

  function updateState() {
    if (isHighHeat) {
      badge.textContent = 'Convection: High Speed Loop';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-purple-300 font-bold';
      if (flame) flame.classList.remove('opacity-40');
      if (plume) {
        plume.setAttribute('stroke-width', '5');
        plume.setAttribute('stroke', '#a855f7');
      }
      explanation.innerHTML = `🌊 <span class="font-bold text-purple-300">Rapid Convection Loop:</span> High heat expands water at the bottom, sharply dropping density. Buoyant purple plumes surge upward rapidly, while cold surface water plunges down the outer glass walls to maintain continuous fluid turnover!`;
    } else {
      badge.textContent = 'Convection: Slow Steady Drift';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-bold';
      if (flame) flame.classList.add('opacity-40');
      if (plume) {
        plume.setAttribute('stroke-width', '2.5');
        plume.setAttribute('stroke', '#c084fc');
      }
      explanation.innerHTML = `🌊 <span class="font-bold text-cyan-300">Gentle Convection:</span> Under low heat, the density differential between top and bottom is smaller, causing slower, gentle convection currents.`;
    }
  }

  if (btnToggle) {
    btnToggle.addEventListener('click', () => {
      isHighHeat = !isHighHeat;
      updateState();
    });
  }

  if (btnCrystal) {
    btnCrystal.addEventListener('click', () => {
      if (plume) {
        plume.classList.remove('animate-pulse');
        void plume.offsetWidth;
        plume.classList.add('animate-pulse');
      }
    });
  }

  updateState();
}

// -------------------------------------------------------------
// Sim 5: Gas Convection: Rising Paper Spiral
// -------------------------------------------------------------
function initGasConvectionSpiralSim(c) {
  const badge = c.querySelector('#spiralStatusBadge');
  const spiral = c.querySelector('#paperSpiral');
  const arrows = c.querySelector('#updraftArrows');
  const flame = c.querySelector('#candleFlameGroup');
  const rpmTxt = c.querySelector('#spiralRpmTxt');
  const btnLight = c.querySelector('#btnLightCandle');
  const btnBlow = c.querySelector('#btnBlowOutCandle');
  const explanation = c.querySelector('#gasConvectionExplanation');

  let isLit = true;
  let angle = 0;
  let animId = null;

  function loop() {
    if (isLit) {
      angle = (angle + 3.5) % 360;
      if (spiral) spiral.setAttribute('transform', `translate(220, 70) rotate(${angle})`);
    }
    animId = requestAnimationFrame(loop);
  }

  function lightCandle() {
    isLit = true;
    if (flame) flame.classList.remove('hidden');
    if (arrows) arrows.classList.remove('hidden');
    badge.textContent = 'Spiral: Rotating Continuously';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold';
    rpmTxt.textContent = 'Speed: 52 RPM';
    explanation.innerHTML = `🌪️ <span class="font-bold text-amber-300">Thermal Updraft:</span> Air directly over the candle flame heats up rapidly, expands, and surges upward in a buoyant convection current. This rising air pushes against the curved blades of the spiral, causing it to spin!`;
  }

  function blowOut() {
    isLit = false;
    if (flame) flame.classList.add('hidden');
    if (arrows) arrows.classList.add('hidden');
    badge.textContent = 'Spiral: Stopped (No Updraft)';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 font-bold';
    rpmTxt.textContent = 'Speed: 0 RPM';
    explanation.innerHTML = `💨 <span class="font-bold text-slate-400">Extinguished:</span> Without heat, air density remains uniform. Convection updrafts cease immediately, and friction brings the paper spiral to a halt.`;
  }

  if (btnLight) btnLight.addEventListener('click', lightCandle);
  if (btnBlow) btnBlow.addEventListener('click', blowOut);

  loop();
  lightCandle();
}

// -------------------------------------------------------------
// Sim 6: Day Sea Breeze
// -------------------------------------------------------------
function initSeaBreezeSim(c) {
  // Static visual with explanation
}

// -------------------------------------------------------------
// Sim 7: Night Land Breeze
// -------------------------------------------------------------
function initLandBreezeSim(c) {
  // Static visual with explanation
}

// -------------------------------------------------------------
// Sim 8: Thermal Radiation Across Cosmic Vacuum
// -------------------------------------------------------------
function initThermalRadiationSim(c) {
  const btnSolar = c.querySelector('#btnPulseSolarRadiation');
  const btnCamp = c.querySelector('#btnCampfireComparison');
  const explanation = c.querySelector('#radiationExplanation');

  if (btnSolar) {
    btnSolar.addEventListener('click', () => {
      explanation.innerHTML = `☀️ <span class="font-bold text-amber-300">Solar Radiation:</span> 150 million km of airless space cannot stop thermal radiation. Infrared electromagnetic waves travel at the speed of light (300,000 km/s), providing life-sustaining warmth to Earth without needing any solid, liquid, or gas medium!`;
    });
  }

  if (btnCamp) {
    btnCamp.addEventListener('click', () => {
      explanation.innerHTML = `🔥 <span class="font-bold text-rose-400">Campfire Radiation:</span> Hot air from a fire rises upward due to convection. The intense warmth you feel on your face sitting beside the campfire is transferred horizontally directly by thermal radiation!`;
    });
  }
}

// -------------------------------------------------------------
// Sim 9: Absorption & Emission (Black vs White Surfaces)
// -------------------------------------------------------------
function initBlackWhiteRadiationSim(c) {
  const badge = c.querySelector('#radExpModeBadge');
  const btnAbs = c.querySelector('#btnModeAbsorption');
  const btnEmi = c.querySelector('#btnModeEmission');
  const lamp = c.querySelector('#heatSourceLamp');

  const thermBlack = c.querySelector('#thermBlackLiquid');
  const thermWhite = c.querySelector('#thermWhiteLiquid');
  const tempBlack = c.querySelector('#tempBlackTxt');
  const tempWhite = c.querySelector('#tempWhiteTxt');
  const deltaTxt = c.querySelector('#radiationDeltaTxt');
  const explanation = c.querySelector('#blackWhiteExplanation');

  function setAbsorption() {
    badge.textContent = 'Mode: Solar Heating (Sunlight)';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-400 font-bold';

    if (lamp) lamp.classList.remove('opacity-20');

    thermBlack.setAttribute('height', '35');
    thermBlack.setAttribute('y', '-5');
    tempBlack.textContent = '48 °C';

    thermWhite.setAttribute('height', '15');
    thermWhite.setAttribute('y', '15');
    tempWhite.textContent = '28 °C';

    deltaTxt.textContent = 'Temperature Difference: ΔT = +20 °C in Black Can!';
    deltaTxt.setAttribute('fill', '#facc15');

    explanation.innerHTML = `☀️ <span class="font-bold text-amber-300">Absorption Test:</span> Dark matte surfaces absorb nearly 95% of incident radiant infrared rays, raising water temperature rapidly to 48 °C. White shiny surfaces reflect most radiation, staying at 28 °C.`;
  }

  function setEmission() {
    badge.textContent = 'Mode: Radiative Cooling (In Dark)';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-400 font-bold';

    if (lamp) lamp.classList.add('opacity-20');

    // Both started at 90 °C; black emits heat faster!
    thermBlack.setAttribute('height', '18');
    thermBlack.setAttribute('y', '12');
    tempBlack.textContent = '32 °C';

    thermWhite.setAttribute('height', '32');
    thermWhite.setAttribute('y', '-2');
    tempWhite.textContent = '64 °C';

    deltaTxt.textContent = 'Cooling Result: Black Can Radiated Away Heat 2× Faster!';
    deltaTxt.setAttribute('fill', '#4ade80');

    explanation.innerHTML = `❄️ <span class="font-bold text-cyan-300">Kirchhoff's Emission Law:</span> In the dark, the black can radiated away its internal heat twice as fast as the white can. <span class="text-emerald-400 font-bold">Good absorbers are always good emitters!</span>`;
  }

  if (btnAbs) btnAbs.addEventListener('click', setAbsorption);
  if (btnEmi) btnEmi.addEventListener('click', setEmission);

  setAbsorption();
}

// -------------------------------------------------------------
// Sim 10: The Thermos Flask Tri-Mode Barrier
// -------------------------------------------------------------
function initThermosFlaskSim(c) {
  // Static visual with explanation
}

// -------------------------------------------------------------
// Sim 11: Global Water Cycle: Evaporation & Transpiration
// -------------------------------------------------------------
function initWaterCycleEvapSim(c) {
  // Static visual with explanation
}

// -------------------------------------------------------------
// Sim 12: Atmospheric Condensation & Cloud Formation
// -------------------------------------------------------------
function initCloudCondensationSim(c) {
  const slider = c.querySelector('#cloudAltSlider');
  const display = c.querySelector('#cloudAltDisplay');
  const badge = c.querySelector('#altitudeTempBadge');
  const cloud = c.querySelector('#formedCloud');
  const explanation = c.querySelector('#cloudExplanation');

  if (!slider) return;

  function update() {
    const alt = parseInt(slider.value, 10);
    display.textContent = `${alt.toLocaleString()} m`;

    // Temperature drops by 6.5 °C per 1,000 m from 26 °C baseline
    const temp = Math.round(26 - (alt / 1000) * 6.5);
    badge.textContent = `Alt: ${alt.toLocaleString()}m (${temp} °C)`;

    if (alt >= 1500) {
      cloud.classList.remove('opacity-30');
      cloud.setAttribute('transform', `translate(160, ${110 - (alt * 0.035)}) scale(1.1)`);
      explanation.innerHTML = `☁️ <span class="font-bold text-cyan-300">Cloud Saturation (Alt ${alt}m):</span> At ${temp} °C, air has cooled below its dew point. Invisible water vapour condenses around microscopic dust particles (CCN), coalescing into thick cumulus clouds!`;
    } else {
      cloud.classList.add('opacity-30');
      cloud.setAttribute('transform', `translate(160, 60) scale(0.7)`);
      explanation.innerHTML = `☀️ <span class="font-bold text-amber-300">Warm Lower Air (Alt ${alt}m):</span> At ${temp} °C, warm air holds water in the invisible gaseous vapour phase. Relative humidity is below 100%, so cloud droplets cannot condense yet.`;
    }
  }

  slider.addEventListener('input', update);
  update();
}

// -------------------------------------------------------------
// Sim 13: Precipitation Types & Watershed Runoff
// -------------------------------------------------------------
function initPrecipitationTypesSim(c) {
  const badge = c.querySelector('#precipTypeBadge');
  const particles = c.querySelector('#rainParticlesGroup');
  const title = c.querySelector('#precipCardTitle');
  const temp = c.querySelector('#precipCardTemp');
  const size = c.querySelector('#precipCardSize');
  const speed = c.querySelector('#precipCardSpeed');
  const btns = c.querySelectorAll('.precip-btn');
  const explanation = c.querySelector('#precipitationExplanation');

  const modes = {
    rain: {
      badge: "Type: Liquid Rain",
      title: "Liquid Rain",
      temp: "Column: > 0 °C",
      size: "Diameter: 0.5 - 4 mm",
      speed: "Fall: ~8 m/s",
      color: "bg-cyan-600 text-white font-bold",
      svg: `
        <line x1="160" y1="80" x2="155" y2="95"/>
        <line x1="190" y1="90" x2="185" y2="105"/>
        <line x1="220" y1="75" x2="215" y2="90"/>
        <line x1="250" y1="85" x2="245" y2="100"/>
        <line x1="170" y1="110" x2="165" y2="125"/>
        <line x1="200" y1="120" x2="195" y2="135"/>
        <line x1="230" y1="105" x2="225" y2="120"/>
        <line x1="260" y1="115" x2="255" y2="130"/>
      `,
      desc: "Liquid raindrops form when coalescing cloud droplets exceed 0.1 mm in diameter and gravity overcomes atmospheric updrafts in columns above 0 °C."
    },
    snow: {
      badge: "Type: Hexagonal Snowflakes",
      title: "Crystalline Snow",
      temp: "Column: < 0 °C Subzero",
      size: "Dendrites: 2 - 8 mm",
      speed: "Fall: ~1 m/s (Gentle)",
      color: "bg-indigo-600 text-white font-bold",
      svg: `
        <circle cx="160" cy="85" r="3" fill="#ffffff"/>
        <circle cx="195" cy="95" r="3.5" fill="#ffffff"/>
        <circle cx="225" cy="80" r="2.5" fill="#ffffff"/>
        <circle cx="255" cy="90" r="3" fill="#ffffff"/>
        <circle cx="175" cy="115" r="3" fill="#ffffff"/>
        <circle cx="205" cy="125" r="2.5" fill="#ffffff"/>
        <circle cx="235" cy="110" r="3.5" fill="#ffffff"/>
        <circle cx="265" cy="120" r="3" fill="#ffffff"/>
      `,
      desc: "When temperatures remain sub-zero from cloud to ground, water vapour deposits directly into intricate hexagonal ice crystals (snowflakes) that drift gently to Earth."
    },
    hail: {
      badge: "Type: Solid Concentric Hailstones",
      title: "Solid Hailstones",
      temp: "Storm Updraft Cycles",
      size: "Diameter: 5 - 50 mm",
      speed: "Fall: ~25 m/s (Heavy)",
      color: "bg-rose-600 text-white font-bold",
      svg: `
        <circle cx="170" cy="90" r="6" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5"/>
        <circle cx="210" cy="80" r="7" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5"/>
        <circle cx="245" cy="95" r="6" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5"/>
        <circle cx="185" cy="120" r="7" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5"/>
        <circle cx="225" cy="115" r="8" fill="#bae6fd" stroke="#0284c7" stroke-width="1.5"/>
      `,
      desc: "In fierce cumulonimbus storm clouds, powerful updrafts repeatedly loft ice pellets through subzero cloud zones, accumulating concentric ice coats until heavy hailstones plunge downward!"
    }
  };

  function setMode(key) {
    const m = modes[key];
    if (!m) return;

    badge.textContent = m.badge;
    title.textContent = m.title;
    temp.textContent = m.temp;
    size.textContent = m.size;
    speed.textContent = m.speed;
    if (particles) particles.innerHTML = m.svg;

    btns.forEach(b => {
      b.className = 'precip-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs transition';
      if (b.dataset.mode === key) {
        b.className = `precip-btn p-2 rounded-xl ${m.color} text-xs transition shadow`;
      }
    });

    explanation.innerHTML = `🌧️ <span class="font-bold text-cyan-300">${m.title}:</span> ${m.desc}`;
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => setMode(btn.dataset.mode));
  });

  setMode('rain');
}

// -------------------------------------------------------------
// Sim 14: Soil Infiltration & Seepage Rates Lab
// -------------------------------------------------------------
function initSoilInfiltrationSim(c) {
  const btnPour = c.querySelector('#btnPour100mlWater');
  const btnReset = c.querySelector('#btnResetInfiltration');
  const badge = c.querySelector('#soilSelectedBadge');

  const bGravel = c.querySelector('#beakerLevelGravel');
  const bSand = c.querySelector('#beakerLevelSand');
  const bLoam = c.querySelector('#beakerLevelLoam');
  const bClay = c.querySelector('#beakerLevelClay');
  const explanation = c.querySelector('#infiltrationExplanation');

  function pourWater() {
    badge.textContent = 'Percolation In Progress...';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-400 font-bold';

    // Gravel fills rapidly to max
    bGravel.setAttribute('height', '28');
    bGravel.setAttribute('y', '115');

    // Sand fills moderately
    bSand.setAttribute('height', '22');
    bSand.setAttribute('y', '122');

    // Loam fills steadily
    bLoam.setAttribute('height', '16');
    bLoam.setAttribute('y', '128');

    // Clay barely fills
    bClay.setAttribute('height', '5');
    bClay.setAttribute('y', '140');

    explanation.innerHTML = `💧 <span class="font-bold text-cyan-300">Percolation Dynamics:</span> Infiltration occurred fastest through gravel due to large open void channels. Clay's microscopic packed platelets trapped water on top as a surface puddle, with minimal seepage!`;
  }

  function resetTubes() {
    badge.textContent = 'Soil: Gravel (Fastest)';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 font-bold';

    bGravel.setAttribute('height', '18'); bGravel.setAttribute('y', '125');
    bSand.setAttribute('height', '13'); bSand.setAttribute('y', '132');
    bLoam.setAttribute('height', '7'); bLoam.setAttribute('y', '138');
    bClay.setAttribute('height', '2'); bClay.setAttribute('y', '143');

    explanation.innerHTML = `⏳ <span class="font-bold text-amber-300">Pore Size Dictates Flow:</span> Gravel and sand have large, wide open pore channels, allowing water to infiltrate rapidly. Clay consists of tightly packed microscopic platelets that swell upon wetting, creating very low permeability!`;
  }

  if (btnPour) btnPour.addEventListener('click', pourWater);
  if (btnReset) btnReset.addEventListener('click', resetTubes);
}

// -------------------------------------------------------------
// Sim 15: Aquifers & Ladakh's Ice Stupas (Sonam Wangchuk)
// -------------------------------------------------------------
function initAquiferIceStupaSim(c) {
  const btnFreeze = c.querySelector('#btnWinterFreezeStupa');
  const btnMelt = c.querySelector('#btnSpringMeltIrrigate');
  const explanation = c.querySelector('#stupaExplanation');

  if (btnFreeze) {
    btnFreeze.addEventListener('click', () => {
      explanation.innerHTML = `❄️ <span class="font-bold text-cyan-300">Winter Stupa Construction (-20 °C):</span> Wasted winter stream runoff is sprayed upward from a vertical pipe under natural gravity. Freezing in cold desert air, it builds a massive ice cone storing up to 2 million liters of water!`;
    });
  }

  if (btnMelt) {
    btnMelt.addEventListener('click', () => {
      explanation.innerHTML = `🌾 <span class="font-bold text-amber-400">Spring Irrigation (April-May):</span> Due to its minimal conical surface area, the Ice Stupa resists early solar radiation and melts gradually in spring, watering barley and willow saplings before natural mountain glaciers thaw in July!`;
    });
  }
}

// -------------------------------------------------------------
// Sim 16: Ancient Indian Thermal Heritage: Matka & Jaali Screens
// -------------------------------------------------------------
function initAncientHeritageCoolingSim(c) {
  const btnMatka = c.querySelector('#btnExploreMatkaPhysics');
  const btnJaali = c.querySelector('#btnExploreJaaliPhysics');
  const explanation = c.querySelector('#ancientHeritageExplanation');

  if (btnMatka) {
    btnMatka.addEventListener('click', () => {
      explanation.innerHTML = `🏺 <span class="font-bold text-amber-300">Terracotta Matka Evaporative Chilling:</span> Water seeps through millions of clay capillaries. Evaporating water extracts 2,260 Joules of latent heat per gram from the water inside the pot, chilling it by 5 to 10 °C without electricity!`;
    });
  }

  if (btnJaali) {
    btnJaali.addEventListener('click', () => {
      explanation.innerHTML = `🏛️ <span class="font-bold text-cyan-300">Rajputana Jaali Screens (Venturi Effect):</span> When hot desert winds are squeezed through thousands of tiny carved stone perforations, airflow accelerates, air pressure drops, and expansion cools the incoming air, providing natural air conditioning in palaces like Hawa Mahal!`;
    });
  }
}
"""

with open('.agents/class7_science_heat_js.py', 'w', encoding='utf-8') as f:
    f.write(f'# -*- coding: utf-8 -*-\n"""Generated JS for Class 7 Science Chapter 7"""\n\nSIMULATOR_JS = r\'\'\'{JS_CODE}\'\'\'\n')

print("Generated .agents/class7_science_heat_js.py successfully.")
