# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Science Chapter 3 Simulator JavaScript Engines
Outputs .agents/class7_science_circuits_js.py
"""

JS_CODE = r"""
// Master Simulator Dispatcher for Chapter 3: Electricity: Circuits and their Components
function initSimulatorForSlide(slideId, container) {
  if (!container) return;
  
  switch(slideId) {
    case 1:
      initTorchlightAnatomySim(container);
      break;
    case 2:
      initCellAnatomySim(container);
      break;
    case 3:
      initBatterySeriesSim(container);
      break;
    case 4:
      initLampVsLedSim(container);
      break;
    case 5:
      initCircuitLoopLabSim(container);
      break;
    case 6:
      initCurrentFlowSim(container);
      break;
    case 7:
      initFusedBulbSim(container);
      break;
    case 8:
      initLedPolaritySim(container);
      break;
    case 9:
      initSwitchMechanismSim(container);
      break;
    case 10:
      initSymbolsRosettaSim(container);
      break;
    case 11:
      initSchematicDesignerSim(container);
      break;
    case 12:
      initSeriesParallelSim(container);
      break;
    case 13:
      initConductionTesterSim(container);
      break;
    case 14:
      initWireInsulationSim(container);
      break;
    case 15:
      initElectricianSafetySim(container);
      break;
    case 16:
      initJcBoseHeritageSim(container);
      break;
    default:
      break;
  }
}

// -------------------------------------------------------------
// Sim 1: Torchlight Anatomy & Safety
// -------------------------------------------------------------
function initTorchlightAnatomySim(container) {
  const toggleBtn = container.querySelector('#toggleTorchBtn');
  const inspectBtn = container.querySelector('#inspectTorchPartsBtn');
  const sliderBtn = container.querySelector('#switchSliderBtn');
  const beamCone = container.querySelector('#torchBeamCone');
  const bulb = container.querySelector('#torchBulb');
  const bulbGlow = container.querySelector('#torchBulbGlow');
  const statusBadge = container.querySelector('#torchStatusBadge');
  const btnLabel = container.querySelector('#torchBtnLabel');
  const infoBox = container.querySelector('#torchInfoBox');
  const strip = container.querySelector('#metalStrip');

  let isOn = false;

  function updateTorchState() {
    if (isOn) {
      if (sliderBtn) sliderBtn.setAttribute('x', '195');
      if (beamCone) beamCone.classList.remove('hidden');
      if (bulb) { bulb.setAttribute('fill', '#facc15'); bulb.setAttribute('stroke', '#ca8a04'); }
      if (bulbGlow) bulbGlow.classList.remove('hidden');
      if (strip) strip.setAttribute('stroke', '#eab308');
      if (statusBadge) {
        statusBadge.textContent = "ON (Beam Active)";
        statusBadge.className = "text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-300 border border-emerald-500/40 font-bold";
      }
      if (btnLabel) btnLabel.textContent = "Slide Switch OFF";
      if (infoBox) infoBox.innerHTML = '<strong class="text-emerald-400">Switch Closed:</strong> The metallic strip completes the continuous electrical circuit between the dry cells, reflector bulb, and base spring. Electrical current flows and light beams forth!';
      playSfx('correct');
    } else {
      if (sliderBtn) sliderBtn.setAttribute('x', '177');
      if (beamCone) beamCone.classList.add('hidden');
      if (bulb) { bulb.setAttribute('fill', '#64748b'); bulb.setAttribute('stroke', '#94a3b8'); }
      if (bulbGlow) bulbGlow.classList.add('hidden');
      if (strip) strip.setAttribute('stroke', '#64748b');
      if (statusBadge) {
        statusBadge.textContent = "OFF";
        statusBadge.className = "text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 font-bold";
      }
      if (btnLabel) btnLabel.textContent = "Slide Switch ON";
      if (infoBox) infoBox.innerHTML = '<strong class="text-amber-400">Switch Open:</strong> The sliding metallic contact is pulled back, introducing an air gap. The circuit is open, stopping all electric current.';
      playSfx('click');
    }
  }

  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      isOn = !isOn;
      updateTorchState();
    });
  }

  if (sliderBtn) {
    sliderBtn.addEventListener('click', () => {
      isOn = !isOn;
      updateTorchState();
    });
  }

  let inspectStep = 0;
  if (inspectBtn) {
    inspectBtn.addEventListener('click', () => {
      playSfx('click');
      inspectStep = (inspectStep + 1) % 4;
      const steps = [
        '<strong class="text-cyan-400">Dry Cells (1.5V x 2):</strong> Connected in series (+ to -) to provide 3.0V DC. Chemical reactions supply continuous direct current.',
        '<strong class="text-amber-400">Parabolic Reflector & Bulb:</strong> A curved mirror gathers scattered light rays from the tiny filament and focuses them into an intense, parallel beam.',
        '<strong class="text-purple-400">Helical Base Spring:</strong> Made of conductive spring brass or steel. It exerts continuous elastic pressure keeping all cells firmly touching.',
        '<strong class="text-emerald-400">Slide Switch Contact:</strong> A sliding copper or brass strip that physically bridges the gap between the cell terminals and the bulb base.'
      ];
      if (infoBox) infoBox.innerHTML = steps[inspectStep];
    });
  }
}

// -------------------------------------------------------------
// Sim 2: Anatomy of an Electric Cell
// -------------------------------------------------------------
function initCellAnatomySim(container) {
  const buttons = container.querySelectorAll('.cell-select-btn');
  const infoText = container.querySelector('#cellInfoText');
  const probeBtn = container.querySelector('#probeTestBtn');

  const partDetails = {
    cap: '<strong class="text-cyan-400">Metal Cap (+ Terminal):</strong> The positive terminal connected to the inner central carbon/graphite rod. Excess positive charges accumulate here via electrochemical oxidation-reduction reactions.',
    carbon: '<strong class="text-slate-200">Carbon (Graphite) Rod:</strong> An inert, conductive central cylinder made of carbon. It acts as the positive electrode (cathode) collecting electrons without reacting away.',
    paste: '<strong class="text-purple-400">Chemical Electrolyte Paste:</strong> A moist blend of Manganese Dioxide (MnO2), Ammonium Chloride (NH4Cl), and Zinc Chloride. It provides mobile ions for charge transfer.',
    zinc: '<strong class="text-slate-300">Outer Zinc Canister:</strong> The cylindrical shell made of zinc metal. It serves as the negative electrode (anode), slowly oxidizing and releasing electrons.',
    base: '<strong class="text-rose-400">Flat Metal Base (- Terminal):</strong> The flat circular bottom disc connected to the zinc container. Electrons exit this terminal to flow through the external circuit.'
  };

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const part = btn.getAttribute('data-part');
      if (!part) return;
      playSfx('click');

      buttons.forEach(b => {
        b.className = "cell-select-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300";
      });
      btn.className = "cell-select-btn px-2 py-1.5 rounded-lg bg-cyan-950 border border-cyan-500/40 text-cyan-200 font-semibold";

      if (infoText && partDetails[part]) {
        infoText.innerHTML = partDetails[part];
      }
    });
  });

  if (probeBtn) {
    probeBtn.addEventListener('click', () => {
      playSfx('correct');
      if (infoText) {
        infoText.innerHTML = '<strong class="text-emerald-400">Digital Multimeter Probe Reading:</strong> <code>+1.52 V DC</code> measured between the top metal cap (+) and flat bottom disc (-). A healthy, fresh dry cell!';
      }
    });
  }
}

// -------------------------------------------------------------
// Sim 3: Battery Series Cell Combinations
// -------------------------------------------------------------
function initBatterySeriesSim(container) {
  const addCellBtn = container.querySelector('#addCellCountBtn');
  const flipBtn = container.querySelector('#flipCellPolarityBtn');
  const voltsDisplay = container.querySelector('#seriesVoltsDisplay');
  const cellCountLabel = container.querySelector('#cellCountLabel');
  const statusMsg = container.querySelector('#batteryStatusMsg');
  const bulbHalo = container.querySelector('#batteryBulbHalo');
  const bulb = container.querySelector('#batteryBulb');

  let cellCount = 2;
  let isOpposed = false;

  function updateBattery() {
    let volts = 0;
    if (!isOpposed) {
      volts = cellCount * 1.5;
    } else {
      volts = Math.max(0, (cellCount - 2) * 1.5);
    }

    if (voltsDisplay) voltsDisplay.textContent = volts.toFixed(1) + " V";
    if (cellCountLabel) cellCountLabel.textContent = `Cells: ${cellCount} (${volts.toFixed(1)}V)`;

    if (volts > 0) {
      const haloR = 14 + (volts * 5);
      const opacity = Math.min(0.9, 0.2 + (volts * 0.15));
      if (bulbHalo) {
        bulbHalo.setAttribute('r', haloR);
        bulbHalo.setAttribute('opacity', opacity);
      }
      if (bulb) {
        bulb.setAttribute('fill', '#facc15');
        bulb.setAttribute('stroke', '#ca8a04');
      }
    } else {
      if (bulbHalo) bulbHalo.setAttribute('opacity', '0');
      if (bulb) {
        bulb.setAttribute('fill', '#64748b');
        bulb.setAttribute('stroke', '#94a3b8');
      }
    }

    if (statusMsg) {
      if (!isOpposed) {
        statusMsg.innerHTML = `<strong class="text-emerald-400">Series Alignment (+ to -):</strong> All ${cellCount} cells face the same direction. Voltages add constructively: $V = ${Array(cellCount).fill('1.5').join(' + ')} = ${volts.toFixed(1)} V$. Bulb shines bright!`;
      } else {
        statusMsg.innerHTML = `<strong class="text-rose-400">Opposing Cells (+ to +):</strong> Cell 2 is reversed! Equal and opposite voltages cancel each other (1.5 V − 1.5 V = 0.0 V). Net potential difference is 0V, so no current flows!`;
      }
    }

    renderAllMath(statusMsg);
  }

  if (addCellBtn) {
    addCellBtn.addEventListener('click', () => {
      playSfx('click');
      cellCount = (cellCount % 4) + 1;
      updateBattery();
    });
  }

  if (flipBtn) {
    flipBtn.addEventListener('click', () => {
      playSfx('click');
      isOpposed = !isOpposed;
      flipBtn.textContent = isOpposed ? "🔄 Restore Normal (+ to -)" : "🔄 Flip Cell 2 (+ to +)";
      updateBattery();
    });
  }
}

// -------------------------------------------------------------
// Sim 4: Incandescent Lamp vs Modern LED Anatomy
// -------------------------------------------------------------
function initLampVsLedSim(container) {
  const bulbTabBtn = container.querySelector('#showBulbTabBtn');
  const ledTabBtn = container.querySelector('#showLedTabBtn');
  const bulbSvg = container.querySelector('#bulbAnatomySvg');
  const ledSvg = container.querySelector('#ledAnatomySvg');

  if (bulbTabBtn && ledTabBtn) {
    bulbTabBtn.addEventListener('click', () => {
      playSfx('click');
      bulbTabBtn.className = "px-2 py-0.5 rounded bg-amber-500 text-slate-950 font-bold text-[10px]";
      ledTabBtn.className = "px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-semibold text-[10px]";
      if (bulbSvg) bulbSvg.classList.remove('hidden');
      if (ledSvg) ledSvg.classList.add('hidden');
    });

    ledTabBtn.addEventListener('click', () => {
      playSfx('click');
      ledTabBtn.className = "px-2 py-0.5 rounded bg-cyan-600 text-white font-bold text-[10px]";
      bulbTabBtn.className = "px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-semibold text-[10px]";
      if (ledSvg) ledSvg.classList.remove('hidden');
      if (bulbSvg) bulbSvg.classList.add('hidden');
    });
  }
}

// -------------------------------------------------------------
// Sim 5: Circuit Loop Construction Lab
// -------------------------------------------------------------
function initCircuitLoopLabSim(container) {
  const buttons = container.querySelectorAll('.loop-preset-btn');
  const badge = container.querySelector('#loopResultBadge');
  const expl = container.querySelector('#loopExplanationText');
  const bulb = container.querySelector('#loopBulb');
  const halo = container.querySelector('#loopBulbHalo');
  const wire1 = container.querySelector('#wire1Path');
  const wire2 = container.querySelector('#wire2Path');

  const setups = {
    A: {
      badge: "Closed Loop (GLOWS)",
      badgeClass: "text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-300 border border-emerald-500/40 font-bold",
      glow: true,
      w1: "M 40,75 C 40,20 254,20 254,87",
      w2: "M 130,75 C 130,135 260,135 260,99",
      text: "<strong class='text-emerald-400'>Setup A (Complete Loop):</strong> Unbroken continuous path! Wire 1 connects cell (+) to bulb casing; Wire 2 connects cell (-) to base tip. Current circulates freely and the lamp glows!"
    },
    B: {
      badge: "Open Loop: Cut Top (DARK)",
      badgeClass: "text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-300 border border-rose-500/40 font-bold",
      glow: false,
      w1: "M 40,75 C 40,20 130,20 130,35",
      w2: "M 130,75 C 130,135 260,135 260,99",
      text: "<strong class='text-rose-400'>Setup B (Cut Top Wire):</strong> The top wire is broken with an air gap. Air is an insulator, so the circuit is open and current cannot flow."
    },
    C: {
      badge: "Open Loop: Disconnected (-) (DARK)",
      badgeClass: "text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-300 border border-rose-500/40 font-bold",
      glow: false,
      w1: "M 40,75 C 40,20 254,20 254,87",
      w2: "M 160,135 C 200,135 260,135 260,99",
      text: "<strong class='text-rose-400'>Setup C (Disconnected Bottom):</strong> The bottom wire fails to touch the negative flat disc of the cell. The circuit is open, so the bulb stays dark."
    },
    D: {
      badge: "SHORT CIRCUIT (DANGER!)",
      badgeClass: "text-[11px] px-2 py-0.5 rounded-full bg-amber-950 text-amber-300 border border-amber-500/40 font-bold",
      glow: false,
      w1: "M 40,75 C 40,20 130,20 130,75",
      w2: "M 130,75 C 130,135 260,135 260,99",
      text: "<strong class='text-amber-400'>Setup D (Short Circuit):</strong> A wire connects (+) directly to (-) without passing through the bulb! Massive current rushes through the wire, generating intense heat while leaving the bulb dark."
    }
  };

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const sKey = btn.getAttribute('data-setup');
      const data = setups[sKey];
      if (!data) return;

      buttons.forEach(b => b.className = "loop-preset-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300");
      btn.className = "loop-preset-btn px-2 py-1.5 rounded-lg bg-emerald-950 border border-emerald-500/40 text-emerald-200 font-bold";

      if (badge) {
        badge.textContent = data.badge;
        badge.className = data.badgeClass;
      }
      if (expl) expl.innerHTML = data.text;
      if (wire1) wire1.setAttribute('d', data.w1);
      if (wire2) wire2.setAttribute('d', data.w2);

      if (data.glow) {
        playSfx('correct');
        if (bulb) { bulb.setAttribute('fill', '#facc15'); bulb.setAttribute('stroke', '#ca8a04'); }
        if (halo) halo.setAttribute('opacity', '0.6');
      } else {
        playSfx('incorrect');
        if (bulb) { bulb.setAttribute('fill', '#64748b'); bulb.setAttribute('stroke', '#94a3b8'); }
        if (halo) halo.setAttribute('opacity', '0');
      }
    });
  });
}

// -------------------------------------------------------------
// Sim 6: Conventional Current vs Electron Flow
// -------------------------------------------------------------
function initCurrentFlowSim(container) {
  const modeBtn = container.querySelector('#toggleCurrentModeBtn');
  const powerBtn = container.querySelector('#toggleCircuitPowerBtn');
  const powerLabel = container.querySelector('#powerBtnLabel');
  const expl = container.querySelector('#flowExplText');

  let isConventional = true;
  let isRunning = true;

  if (modeBtn) {
    modeBtn.addEventListener('click', () => {
      playSfx('click');
      isConventional = !isConventional;
      modeBtn.textContent = isConventional ? "Mode: Conventional (+ to -)" : "Mode: Real Electrons (- to +)";
      if (expl) {
        expl.innerHTML = isConventional
          ? '<strong class="text-cyan-400">Conventional Current:</strong> By historical scientific convention, current is defined as positive charge carriers flowing from (+) to (-) outside the cell.'
          : '<strong class="text-purple-400">Real Electron Drift:</strong> Inside metallic copper wires, negative electrons actually drift in the opposite direction: from the negative (-) disc toward the positive (+) cap!';
      }
    });
  }

  if (powerBtn) {
    powerBtn.addEventListener('click', () => {
      playSfx('click');
      isRunning = !isRunning;
      if (powerLabel) powerLabel.textContent = isRunning ? "Pause Current" : "Resume Current";
    });
  }
}

// -------------------------------------------------------------
// Sim 7: Fused Lamp Diagnostics
// -------------------------------------------------------------
function initFusedBulbSim(container) {
  const goodBtn = container.querySelector('#setBulbGoodBtn');
  const fusedBtn = container.querySelector('#setBulbFusedBtn');
  const goodSvg = container.querySelector('#goodFilamentSvg');
  const fusedSvg = container.querySelector('#fusedFilamentSvg');
  const meter = container.querySelector('#multimeterDisplay');
  const infoBox = container.querySelector('#fusedInfoBox');

  if (goodBtn) {
    goodBtn.addEventListener('click', () => {
      playSfx('correct');
      if (goodSvg) goodSvg.classList.remove('hidden');
      if (fusedSvg) fusedSvg.classList.add('hidden');
      if (meter) {
        meter.textContent = "2.5 Ω (OK)";
        meter.className = "text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-950 border border-slate-800 text-emerald-400";
      }
      if (infoBox) {
        infoBox.innerHTML = '<strong class="text-emerald-400">Intact Filament:</strong> Coiled tungsten wire connects both support posts without breaks. Multimeter registers low resistance (2.5 Ω). Circuit conducts current properly!';
      }
      renderAllMath(infoBox);
    });
  }

  if (fusedBtn) {
    fusedBtn.addEventListener('click', () => {
      playSfx('incorrect');
      if (goodSvg) goodSvg.classList.add('hidden');
      if (fusedSvg) fusedSvg.classList.remove('hidden');
      if (meter) {
        meter.textContent = "OL (Open Circuit)";
        meter.className = "text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-950 border border-slate-800 text-rose-400";
      }
      if (infoBox) {
        infoBox.innerHTML = '<strong class="text-rose-400">Snapped Filament (Fused):</strong> High heat or evaporation melted the thin tungsten wire. A physical air gap is created inside the bulb. Multimeter shows infinite resistance (OL / Open Loop). Circuit is broken!';
      }
      renderAllMath(infoBox);
    });
  }
}

// -------------------------------------------------------------
// Sim 8: LED Polarity & Forward Bias Tester
// -------------------------------------------------------------
function initLedPolaritySim(container) {
  const fwdBtn = container.querySelector('#setForwardBiasBtn');
  const revBtn = container.querySelector('#setReverseBiasBtn');
  const badge = container.querySelector('#biasStateBadge');
  const halo = container.querySelector('#ledGlowHalo');
  const dome = container.querySelector('#ledDomeSvg');
  const infoText = container.querySelector('#ledBiasInfoText');

  if (fwdBtn) {
    fwdBtn.addEventListener('click', () => {
      playSfx('correct');
      if (badge) {
        badge.textContent = "Forward Bias (GLOWS)";
        badge.className = "text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-300 border border-emerald-500/40 font-bold";
      }
      if (halo) halo.setAttribute('opacity', '0.6');
      if (dome) { dome.setAttribute('fill', '#15803d'); dome.setAttribute('stroke', '#4ade80'); }
      if (infoText) {
        infoText.innerHTML = '<strong class="text-emerald-400">Forward Bias:</strong> Cell positive (+) connects to the longer Anode lead (+). Charge carriers easily traverse the semiconductor junction, recombining to emit brilliant photons!';
      }
    });
  }

  if (revBtn) {
    revBtn.addEventListener('click', () => {
      playSfx('incorrect');
      if (badge) {
        badge.textContent = "Reverse Bias (BLOCKED)";
        badge.className = "text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-300 border border-rose-500/40 font-bold";
      }
      if (halo) halo.setAttribute('opacity', '0');
      if (dome) { dome.setAttribute('fill', '#1e293b'); dome.setAttribute('stroke', '#475569'); }
      if (infoText) {
        infoText.innerHTML = '<strong class="text-rose-400">Reverse Bias:</strong> Cell positive (+) is connected to the shorter Cathode lead (-). The internal depletion barrier widens dramatically, blocking all current flow. The LED remains dark!';
      }
    });
  }
}

// -------------------------------------------------------------
// Sim 9: DIY Safety Pin Switch Builder
// -------------------------------------------------------------
function initSwitchMechanismSim(container) {
  const toggleBtn = container.querySelector('#toggleDiySwitchBtn');
  const airGapBtn = container.querySelector('#showAirGapExplBtn');
  const badge = container.querySelector('#diySwitchStatusBadge');
  const arm = container.querySelector('#safetyPinArm');
  const halo = container.querySelector('#switchBulbHalo');
  const bulb = container.querySelector('#switchBulb');
  const btnText = container.querySelector('#diyBtnText');
  const expl = container.querySelector('#switchExplText');

  let isOn = false;

  function updateSwitch() {
    if (isOn) {
      if (arm) arm.setAttribute('transform', 'rotate(0, 80, 75)');
      if (halo) halo.setAttribute('opacity', '0.6');
      if (bulb) { bulb.setAttribute('fill', '#facc15'); bulb.setAttribute('stroke', '#ca8a04'); }
      if (badge) {
        badge.textContent = "ON (Closed Circuit)";
        badge.className = "text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-300 border border-emerald-500/40 font-bold";
      }
      if (btnText) btnText.textContent = "Rotate Pin: Open Switch (OFF)";
      if (expl) expl.innerHTML = '<strong class="text-emerald-400">Switch ON (Closed):</strong> The steel safety pin bridges both brass drawing pins, forming a continuous metallic path. Electric current flows and the bulb illuminates!';
      playSfx('correct');
    } else {
      if (arm) arm.setAttribute('transform', 'rotate(-30, 80, 75)');
      if (halo) halo.setAttribute('opacity', '0');
      if (bulb) { bulb.setAttribute('fill', '#64748b'); bulb.setAttribute('stroke', '#94a3b8'); }
      if (badge) {
        badge.textContent = "OFF (Open Air Gap)";
        badge.className = "text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 font-bold";
      }
      if (btnText) btnText.textContent = "Rotate Pin: Close Switch (ON)";
      if (expl) expl.innerHTML = '<strong class="text-rose-400">Switch OFF (Open):</strong> The safety pin swings away from the second drawing pin, leaving an air gap. Air is an insulator, so the circuit is open and current stops!';
      playSfx('click');
    }
  }

  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      isOn = !isOn;
      updateSwitch();
    });
  }

  if (arm) {
    arm.addEventListener('click', () => {
      isOn = !isOn;
      updateSwitch();
    });
  }

  if (airGapBtn) {
    airGapBtn.addEventListener('click', () => {
      playSfx('click');
      if (expl) {
        expl.innerHTML = '<strong class="text-cyan-400">Air Gap Physics:</strong> Air molecules are neutral and lack free mobile electrons. At low voltages (1.5V to 9V), air offers virtually infinite resistance (R > 10¹⁴ Ω), preventing electric current from crossing the gap.';
      }
    });
  }
}

// -------------------------------------------------------------
// Sim 10: Circuit Symbols Rosetta Stone
// -------------------------------------------------------------
function initSymbolsRosettaSim(container) {
  const buttons = container.querySelectorAll('.symbol-btn');
  const realGraphic = container.querySelector('#symbolRealGraphic');
  const realName = container.querySelector('#symbolRealName');
  const schemGraphic = container.querySelector('#symbolSchematicGraphic');
  const symbolRule = container.querySelector('#symbolSymbolRule');
  const explBox = container.querySelector('#symbolExplBox');

  const compData = {
    cell: {
      emoji: "🔋",
      name: "Electric Dry Cell",
      svg: `<svg viewBox="0 0 100 60" class="w-24 h-16"><line x1="10" y1="30" x2="45" y2="30" stroke="#38bdf8" stroke-width="2"/><line x1="45" y1="12" x2="45" y2="48" stroke="#38bdf8" stroke-width="1.5"/><line x1="55" y1="20" x2="55" y2="40" stroke="#f43f5e" stroke-width="4"/><line x1="55" y1="30" x2="90" y2="30" stroke="#f43f5e" stroke-width="2"/><text x="43" y="10" font-size="8" fill="#38bdf8" text-anchor="middle">+</text><text x="56" y="16" font-size="9" fill="#f43f5e" text-anchor="middle">-</text></svg>`,
      rule: "Long Thin (+) & Short Thick (-)",
      expl: "<strong class='text-purple-400'>Electric Cell:</strong> Long thin parallel line represents the positive (+) terminal; shorter thicker parallel line represents the negative (-) terminal."
    },
    battery: {
      emoji: "⚡",
      name: "Battery (Cells in Series)",
      svg: `<svg viewBox="0 0 100 60" class="w-24 h-16"><line x1="5" y1="30" x2="25" y2="30" stroke="#38bdf8" stroke-width="2"/><line x1="25" y1="14" x2="25" y2="46" stroke="#38bdf8" stroke-width="1.5"/><line x1="35" y1="20" x2="35" y2="40" stroke="#f43f5e" stroke-width="3"/><line x1="35" y1="30" x2="55" y2="30" stroke="#64748b" stroke-width="1.5" stroke-dasharray="2,2"/><line x1="55" y1="14" x2="55" y2="46" stroke="#38bdf8" stroke-width="1.5"/><line x1="65" y1="20" x2="65" y2="40" stroke="#f43f5e" stroke-width="3"/><line x1="65" y1="30" x2="95" y2="30" stroke="#f43f5e" stroke-width="2"/></svg>`,
      rule: "Series of Alternating Cell Lines",
      expl: "<strong class='text-purple-400'>Battery:</strong> Two or more cell symbols joined end-to-end (+ connected to -). Indicates combined voltage."
    },
    bulb: {
      emoji: "💡",
      name: "Electric Bulb / Lamp",
      svg: `<svg viewBox="0 0 100 60" class="w-24 h-16"><line x1="10" y1="30" x2="35" y2="30" stroke="#eab308" stroke-width="2"/><circle cx="50" cy="30" r="15" fill="none" stroke="#eab308" stroke-width="2"/><path d="M 43,30 Q 50,20 57,30" fill="none" stroke="#eab308" stroke-width="2"/><line x1="65" y1="30" x2="90" y2="30" stroke="#eab308" stroke-width="2"/></svg>`,
      rule: "Circle with Inner Filament Loop",
      expl: "<strong class='text-purple-400'>Electric Bulb:</strong> A circle enclosing a curved loop that represents the coiled tungsten filament."
    },
    switch_on: {
      emoji: "🟢",
      name: "Switch in ON Position",
      svg: `<svg viewBox="0 0 100 60" class="w-24 h-16"><line x1="10" y1="30" x2="35" y2="30" stroke="#22c55e" stroke-width="2"/><circle cx="35" cy="30" r="3" fill="#22c55e"/><line x1="35" y1="30" x2="65" y2="30" stroke="#22c55e" stroke-width="2.5"/><circle cx="65" cy="30" r="3" fill="#22c55e"/><line x1="65" y1="30" x2="90" y2="30" stroke="#22c55e" stroke-width="2"/></svg>`,
      rule: "Closed Conducting Bridge",
      expl: "<strong class='text-emerald-400'>Switch ON:</strong> A horizontal straight line touches both circular terminal dots, indicating a closed, continuous circuit."
    },
    switch_off: {
      emoji: "🔴",
      name: "Switch in OFF Position",
      svg: `<svg viewBox="0 0 100 60" class="w-24 h-16"><line x1="10" y1="30" x2="35" y2="30" stroke="#f43f5e" stroke-width="2"/><circle cx="35" cy="30" r="3" fill="#f43f5e"/><line x1="35" y1="30" x2="62" y2="12" stroke="#f43f5e" stroke-width="2.5"/><circle cx="65" cy="30" r="3" fill="#f43f5e"/><line x1="65" y1="30" x2="90" y2="30" stroke="#f43f5e" stroke-width="2"/></svg>`,
      rule: "Tilted Line Showing Air Gap",
      expl: "<strong class='text-rose-400'>Switch OFF:</strong> The line is tilted upward away from the second dot, visually proving the presence of an open air gap."
    },
    wire: {
      emoji: "〰️",
      name: "Connecting Wire",
      svg: `<svg viewBox="0 0 100 60" class="w-24 h-16"><line x1="10" y1="30" x2="90" y2="30" stroke="#38bdf8" stroke-width="2.5"/></svg>`,
      rule: "Straight Horizontal or Vertical Line",
      expl: "<strong class='text-cyan-400'>Connecting Wire:</strong> Clean straight lines represent conductors with negligible resistance connecting components together."
    }
  };

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const comp = btn.getAttribute('data-comp');
      const data = compData[comp];
      if (!data) return;
      playSfx('click');

      buttons.forEach(b => b.className = "symbol-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300");
      btn.className = "symbol-btn px-2 py-1.5 rounded-lg bg-purple-950 border border-purple-500/40 text-purple-200 font-bold";

      if (realGraphic) realGraphic.textContent = data.emoji;
      if (realName) realName.textContent = data.name;
      if (schemGraphic) schemGraphic.innerHTML = data.svg;
      if (symbolRule) symbolRule.textContent = data.rule;
      if (explBox) explBox.innerHTML = data.expl;
    });
  });
}

// -------------------------------------------------------------
// Sim 11: Schematic vs Pictorial View
// -------------------------------------------------------------
function initSchematicDesignerSim(container) {
  const pictBtn = container.querySelector('#viewPictorialBtn');
  const schemBtn = container.querySelector('#viewSchematicBtn');
  const pictSvg = container.querySelector('#canvasPictorialSvg');
  const schemSvg = container.querySelector('#canvasSchematicSvg');
  const switchToggleBtn = container.querySelector('#toggleSchemSwitchBtn');
  const switchLabel = container.querySelector('#schemSwitchLabel');

  let isOn = true;

  if (pictBtn && schemBtn) {
    pictBtn.addEventListener('click', () => {
      playSfx('click');
      pictBtn.className = "px-2 py-0.5 rounded bg-cyan-600 text-white font-bold text-[10px]";
      schemBtn.className = "px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-semibold text-[10px]";
      if (pictSvg) pictSvg.classList.remove('hidden');
      if (schemSvg) schemSvg.classList.add('hidden');
    });

    schemBtn.addEventListener('click', () => {
      playSfx('click');
      schemBtn.className = "px-2 py-0.5 rounded bg-cyan-600 text-white font-bold text-[10px]";
      pictBtn.className = "px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-semibold text-[10px]";
      if (schemSvg) schemSvg.classList.remove('hidden');
      if (pictSvg) pictSvg.classList.add('hidden');
    });
  }

  if (switchToggleBtn) {
    switchToggleBtn.addEventListener('click', () => {
      isOn = !isOn;
      playSfx(isOn ? 'correct' : 'click');
      if (switchLabel) switchLabel.textContent = isOn ? "Switch: ON" : "Switch: OFF";
      
      const pictGlow = container.querySelector('#pictBulbGlow');
      const pictBulb = container.querySelector('#pictBulb');
      const schemGlow = container.querySelector('#schemBulbGlow');
      const pictLine = container.querySelector('#pictSwitchLine');
      const schemLine = container.querySelector('#schemSwitchLine');

      if (isOn) {
        if (pictGlow) pictGlow.setAttribute('opacity', '0.6');
        if (pictBulb) pictBulb.setAttribute('fill', '#facc15');
        if (schemGlow) schemGlow.setAttribute('opacity', '0.6');
        if (pictLine) pictLine.setAttribute('y2', '40');
        if (schemLine) schemLine.setAttribute('y2', '30');
      } else {
        if (pictGlow) pictGlow.setAttribute('opacity', '0');
        if (pictBulb) pictBulb.setAttribute('fill', '#64748b');
        if (schemGlow) schemGlow.setAttribute('opacity', '0');
        if (pictLine) pictLine.setAttribute('y2', '25');
        if (schemLine) schemLine.setAttribute('y2', '18');
      }
    });
  }
}

// -------------------------------------------------------------
// Sim 12: Series vs Parallel Circuit Preview
// -------------------------------------------------------------
function initSeriesParallelSim(container) {
  const serBtn = container.querySelector('#modeSeriesBtn');
  const parBtn = container.querySelector('#modeParallelBtn');
  const serSvg = container.querySelector('#circuitSeriesSvg');
  const parSvg = container.querySelector('#circuitParallelSvg');
  const unscrewBtn = container.querySelector('#toggleBulb1UnscrewBtn');
  const unscrewLabel = container.querySelector('#unscrewBtnLabel');
  const summaryText = container.querySelector('#archSummaryText');

  let isParallel = false;
  let isUnscrewed = false;

  function updateVisuals() {
    const serB1 = container.querySelector('#serBulb1');
    const serB1Halo = container.querySelector('#serBulb1Halo');
    const serB2 = container.querySelector('#serBulb2');
    const serB2Halo = container.querySelector('#serBulb2Halo');

    const parB1 = container.querySelector('#parBulb1');
    const parB1Halo = container.querySelector('#parBulb1Halo');
    const parB2 = container.querySelector('#parBulb2');
    const parB2Halo = container.querySelector('#parBulb2Halo');

    if (!isParallel) {
      // Series
      if (isUnscrewed) {
        if (serB1) serB1.setAttribute('fill', '#334155');
        if (serB1Halo) serB1Halo.setAttribute('opacity', '0');
        if (serB2) serB2.setAttribute('fill', '#334155');
        if (serB2Halo) serB2Halo.setAttribute('opacity', '0');
        if (summaryText) summaryText.textContent = "Series Loop Broken: Unscrewing Bulb 1 stops current everywhere! Bulb 2 goes dark.";
      } else {
        if (serB1) serB1.setAttribute('fill', '#facc15');
        if (serB1Halo) serB1Halo.setAttribute('opacity', '0.4');
        if (serB2) serB2.setAttribute('fill', '#facc15');
        if (serB2Halo) serB2Halo.setAttribute('opacity', '0.4');
        if (summaryText) summaryText.textContent = "Series Intact: Both bulbs share the single loop and voltage (each glows at medium brightness).";
      }
    } else {
      // Parallel
      if (isUnscrewed) {
        if (parB1) parB1.setAttribute('fill', '#334155');
        if (parB1Halo) parB1Halo.setAttribute('opacity', '0');
        if (parB2) parB2.setAttribute('fill', '#facc15');
        if (parB2Halo) parB2Halo.setAttribute('opacity', '0.6');
        if (summaryText) summaryText.textContent = "Parallel Independent: Bulb 1 is unscrewed, but Bulb 2 has its own complete branch and stays lit!";
      } else {
        if (parB1) parB1.setAttribute('fill', '#facc15');
        if (parB1Halo) parB1Halo.setAttribute('opacity', '0.6');
        if (parB2) parB2.setAttribute('fill', '#facc15');
        if (parB2Halo) parB2Halo.setAttribute('opacity', '0.6');
        if (summaryText) summaryText.textContent = "Parallel Intact: Both branches receive full cell voltage; both glow at maximum brightness!";
      }
    }
  }

  if (serBtn && parBtn) {
    serBtn.addEventListener('click', () => {
      playSfx('click');
      isParallel = false;
      serBtn.className = "px-2 py-0.5 rounded bg-amber-500 text-slate-950 font-bold text-[10px]";
      parBtn.className = "px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-semibold text-[10px]";
      if (serSvg) serSvg.classList.remove('hidden');
      if (parSvg) parSvg.classList.add('hidden');
      updateVisuals();
    });

    parBtn.addEventListener('click', () => {
      playSfx('click');
      isParallel = true;
      parBtn.className = "px-2 py-0.5 rounded bg-emerald-600 text-white font-bold text-[10px]";
      serBtn.className = "px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-semibold text-[10px]";
      if (parSvg) parSvg.classList.remove('hidden');
      if (serSvg) serSvg.classList.add('hidden');
      updateVisuals();
    });
  }

  if (unscrewBtn) {
    unscrewBtn.addEventListener('click', () => {
      playSfx('click');
      isUnscrewed = !isUnscrewed;
      if (unscrewLabel) unscrewLabel.textContent = isUnscrewed ? "Re-screw Bulb 1" : "Unscrew Bulb 1";
      updateVisuals();
    });
  }
}

// -------------------------------------------------------------
// Sim 13: Conduction Tester Laboratory
// -------------------------------------------------------------
function initConductionTesterSim(container) {
  const buttons = container.querySelectorAll('.mat-test-btn');
  const badge = container.querySelector('#conductionResultBadge');
  const bulb = container.querySelector('#testerBulb');
  const halo = container.querySelector('#testerBulbHalo');
  const objShape = container.querySelector('#objShape');
  const objLabel = container.querySelector('#objLabel');
  const expl = container.querySelector('#conductionExplText');

  const materials = {
    copper: { name: "Copper Strip", color: "#b45309", isConductor: true, note: "Copper is an outstanding metal conductor packed with free mobile electrons. Current flows effortlessly; bulb glows brightly!" },
    iron: { name: "Iron Nail", color: "#64748b", isConductor: true, note: "Iron is a metallic conductor. Its valence electrons carry charge across the probes, closing the circuit loop." },
    graphite: { name: "Pencil Graphite", color: "#1e293b", isConductor: true, note: "Graphite is an extraordinary non-metal conductor made of carbon with delocalized pi-electrons. Bulb glows clearly!" },
    lemon: { name: "Lemon Juice", color: "#eab308", isConductor: true, note: "Lemon juice contains citric acid which dissociates into mobile H+ and citrate ions. The electrolytic liquid conducts current!" },
    plastic: { name: "Plastic Ruler", color: "#0284c7", isConductor: false, note: "Plastic is a polymer insulator whose electrons are tightly locked in covalent bonds. Current is blocked; bulb is dark." },
    rubber: { name: "Rubber Eraser", color: "#f43f5e", isConductor: false, note: "Rubber is a high-resistance electrical insulator. It halts electric charges completely." },
    wood: { name: "Dry Toothpick", color: "#78350f", isConductor: false, note: "Dry wood consists of cellulose without free ions or electrons. It acts as an insulator, leaving the bulb off." },
    glass: { name: "Glass Rod", color: "#94a3b8", isConductor: false, note: "Glass has massive electrical resistivity (> 10^12 Ω). Charges cannot flow across the gap." }
  };

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const matKey = btn.getAttribute('data-mat');
      const mat = materials[matKey];
      if (!mat) return;

      buttons.forEach(b => b.className = "mat-test-btn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300");
      btn.className = mat.isConductor
        ? "mat-test-btn px-2 py-1.5 rounded-lg bg-emerald-950 border border-emerald-500/40 text-emerald-200 font-bold"
        : "mat-test-btn px-2 py-1.5 rounded-lg bg-rose-950 border border-rose-500/40 text-rose-200 font-bold";

      if (objShape) objShape.setAttribute('fill', mat.color);
      if (objLabel) objLabel.textContent = mat.name;

      if (mat.isConductor) {
        playSfx('correct');
        if (badge) {
          badge.textContent = "CONDUCTOR (Glows!)";
          badge.className = "text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-300 border border-emerald-500/40 font-bold";
        }
        if (bulb) { bulb.setAttribute('fill', '#facc15'); bulb.setAttribute('stroke', '#ca8a04'); }
        if (halo) halo.setAttribute('opacity', '0.6');
      } else {
        playSfx('incorrect');
        if (badge) {
          badge.textContent = "INSULATOR (Dark)";
          badge.className = "text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-300 border border-rose-500/40 font-bold";
        }
        if (bulb) { bulb.setAttribute('fill', '#64748b'); bulb.setAttribute('stroke', '#94a3b8'); }
        if (halo) halo.setAttribute('opacity', '0');
      }

      if (expl) expl.innerHTML = `<strong class="${mat.isConductor ? 'text-emerald-400' : 'text-rose-400'}">${mat.name}:</strong> ${mat.note}`;
    });
  });
}

// -------------------------------------------------------------
// Sim 14: Engineering Wire Insulation
// -------------------------------------------------------------
function initWireInsulationSim(container) {
  const pvcBtn = container.querySelector('#touchPvcBtn');
  const copperBtn = container.querySelector('#touchCopperBtn');
  const infoText = container.querySelector('#insulationInfoText');

  if (pvcBtn) {
    pvcBtn.addEventListener('click', () => {
      playSfx('correct');
      if (infoText) {
        infoText.innerHTML = '<strong class="text-emerald-400">Touching PVC Sheath:</strong> Completely safe! PVC has a dielectric breakdown voltage of over 10,000 V. Zero electrical leakage occurs to human fingers.';
      }
    });
  }

  if (copperBtn) {
    copperBtn.addEventListener('click', () => {
      playSfx('incorrect');
      if (infoText) {
        infoText.innerHTML = '<strong class="text-rose-400">Touching Bare Copper Core:</strong> High shock hazard! If the wire is carrying mains AC current (230V), electricity will flow directly into your body toward the ground.';
      }
    });
  }
}

// -------------------------------------------------------------
// Sim 15: Electrician Safety & Human Body Conduction
// -------------------------------------------------------------
function initElectricianSafetySim(container) {
  const wetBtn = container.querySelector('#toggleWetSkinBtn');
  const ppeBtn = container.querySelector('#togglePpeBootsBtn');
  const rBadge = container.querySelector('#resistanceBadge');
  const skinLabel = container.querySelector('#skinMoistureLabel');
  const ppeLabel = container.querySelector('#ppeLabel');
  const hazardText = container.querySelector('#safetyHazardText');
  const boots = [container.querySelector('#bootLeft'), container.querySelector('#bootRight')];

  let isWet = false;
  let hasBoots = true;

  function updateSafety() {
    if (isWet) {
      if (skinLabel) skinLabel.textContent = "Mode: Wet Skin (Sweat/Water)";
      if (rBadge) {
        rBadge.textContent = "R = 1,000 Ω (Wet Skin Hazard!)";
        rBadge.className = "text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-950 border border-slate-800 text-rose-400";
      }
    } else {
      if (skinLabel) skinLabel.textContent = "Mode: Dry Skin";
      if (rBadge) {
        rBadge.textContent = "R = 100,000 Ω (Dry Skin)";
        rBadge.className = "text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-950 border border-slate-800 text-cyan-400";
      }
    }

    if (hasBoots) {
      if (ppeLabel) ppeLabel.textContent = "Rubber Boots: ON";
      boots.forEach(b => { if (b) b.setAttribute('fill', '#0f172a'); });
      if (hazardText) {
        hazardText.innerHTML = '<strong class="text-emerald-400">Safe with Rubber PPE:</strong> Thick rubber boots and gloves introduce gigohms of resistance, completely breaking the circuit path to ground!';
      }
    } else {
      if (ppeLabel) ppeLabel.textContent = "Rubber Boots: OFF (Barefoot)";
      boots.forEach(b => { if (b) b.setAttribute('fill', '#fed7aa'); });
      if (hazardText) {
        hazardText.innerHTML = isWet
          ? '<strong class="text-rose-400">CATASTROPHIC DANGER!</strong> Wet hands + barefoot on floor: Body resistance is just 1,000 Ω. Current at 230V would be I = 230 / 1000 = 230 mA, causing lethal cardiac arrest!'
          : '<strong class="text-amber-400">Elevated Shock Risk:</strong> Barefoot on ground provides a return path to earth. Electricians must always wear thick rubber-soled footwear.';
      }
    }

    renderAllMath(hazardText);
  }

  if (wetBtn) {
    wetBtn.addEventListener('click', () => {
      isWet = !isWet;
      playSfx('click');
      updateSafety();
    });
  }

  if (ppeBtn) {
    ppeBtn.addEventListener('click', () => {
      hasBoots = !hasBoots;
      playSfx('click');
      updateSafety();
    });
  }
}

// -------------------------------------------------------------
// Sim 16: Heritage of Indian Electrical Science: Acharya J.C. Bose
// -------------------------------------------------------------
function initJcBoseHeritageSim(container) {
  const transmitBtn = container.querySelector('#transmitSignalBtn');
  const inspectBtn = container.querySelector('#inspectGalenaBtn');
  const waves = container.querySelector('#microwaveWaves');
  const bell = container.querySelector('#heritageBell');
  const badge = container.querySelector('#bellStatusBadge');
  const infoText = container.querySelector('#boseHeritageText');

  if (transmitBtn) {
    transmitBtn.addEventListener('click', () => {
      playSfx('correct');
      if (waves) waves.classList.remove('hidden');
      if (badge) {
        badge.textContent = "🔔 Bell Ringing Wirelessly!";
        badge.className = "text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-300 border border-emerald-500/40 font-bold";
      }
      if (bell) {
        bell.setAttribute('fill', '#facc15');
      }
      if (infoText) {
        infoText.innerHTML = '<strong class="text-emerald-400">Wireless Transmission Success:</strong> 60 GHz microwave radiation traveled right through the solid brick wall! Bose\'s galena crystal detected the signal and triggered the electric bell!';
      }

      setTimeout(() => {
        if (waves) waves.classList.add('hidden');
        if (bell) bell.setAttribute('fill', '#ca8a04');
        if (badge) {
          badge.textContent = "Bell Silent";
          badge.className = "text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 font-bold";
        }
      }, 2000);
    });
  }

  if (inspectBtn) {
    inspectBtn.addEventListener('click', () => {
      playSfx('click');
      if (infoText) {
        infoText.innerHTML = '<strong class="text-purple-400">Galena Crystal Detector (1904):</strong> Acharya J.C. Bose pressed a fine metallic point against a crystal of galena (lead sulfide, PbS). This formed the world\'s first solid-state semiconductor diode detector, paving the way for modern radio diodes and LEDs!';
      }
    });
  }
}
"""

if __name__ == "__main__":
    with open(".agents/class7_science_circuits_js.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Class 7 Science Chapter 3 Simulator JavaScript Engines"""\n\n')
        f.write("SIMULATORS_JS = " + repr(JS_CODE) + "\n")
    print("Generated .agents/class7_science_circuits_js.py successfully.")

