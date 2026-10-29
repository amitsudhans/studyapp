# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Science Chapter 5 Simulator JavaScript Engines
Outputs .agents/class7_science_changes_js.py
"""

JS_CODE = r"""
// Master Simulator Dispatcher for Chapter 5: Changes Around Us: Physical and Chemical
function initSimulatorForSlide(slideId, container) {
  if (!container) return;

  switch(slideId) {
    case 1:
      initPhysicalChangesExplorerSim(container);
      break;
    case 2:
      initStateTransformationsSim(container);
      break;
    case 3:
      initVinegarBakingSodaSim(container);
      break;
    case 4:
      initLimeWaterTestSim(container);
      break;
    case 5:
      initRustingChemicalSim(container);
      break;
    case 6:
      initCombustionReactionsSim(container);
      break;
    case 7:
      initFireTriangleSim(container);
      break;
    case 8:
      initCandleDualChangesSim(container);
      break;
    case 9:
      initReversibilityClassifierSim(container);
      break;
    case 10:
      initDesirableUndesirableSim(container);
      break;
    case 11:
      initPhysicalWeatheringSim(container);
      break;
    case 12:
      initChemicalWeatheringSim(container);
      break;
    case 13:
      initSoilErosionSim(container);
      break;
    case 14:
      initEnergyDynamicsSim(container);
      break;
    case 15:
      initConservationOfMassSim(container);
      break;
    case 16:
      initKanadaHeritageSim(container);
      break;
  }
}

// -------------------------------------------------------------
// Sim 1: Physical Changes Explorer (Paper, Balloon, Chalk)
// -------------------------------------------------------------
function initPhysicalChangesExplorerSim(c) {
  const badge = c.querySelector('#physModeBadge');
  const explanation = c.querySelector('#physExplanation');
  const btnTransform = c.querySelector('#btnTransformPhys');
  const btnReset = c.querySelector('#btnResetPhys');
  const modeBtns = c.querySelectorAll('.phys-obj-btn');

  const paperWs = c.querySelector('#paperWorkspace');
  const balloonWs = c.querySelector('#balloonWorkspace');
  const chalkWs = c.querySelector('#chalkWorkspace');

  const flatPaper = c.querySelector('#flatPaperSheet');
  const foldedPlane = c.querySelector('#foldedPlane');
  const shreddedPaper = c.querySelector('#shreddedPaper');

  const inflatedBalloon = c.querySelector('#inflatedBalloon');
  const poppedBalloon = c.querySelector('#poppedBalloon');

  const solidChalk = c.querySelector('#solidChalk');
  const crushedChalk = c.querySelector('#crushedChalk');

  let currentMode = 'paper';
  let isTransformed = false;

  modeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      modeBtns.forEach(b => b.className = 'phys-obj-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs');
      btn.className = 'phys-obj-btn p-2 rounded-xl bg-amber-600 text-white font-bold text-xs';
      currentMode = btn.dataset.mode;
      resetState();
    });
  });

  function resetState() {
    isTransformed = false;
    paperWs.classList.add('hidden');
    balloonWs.classList.add('hidden');
    chalkWs.classList.add('hidden');

    if (currentMode === 'paper') {
      paperWs.classList.remove('hidden');
      foldedPlane.classList.remove('hidden');
      flatPaper.classList.add('hidden');
      shreddedPaper.classList.add('hidden');
      badge.textContent = 'Paper Airplane';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-bold';
      explanation.innerHTML = `📐 <span class="font-bold text-amber-300">Paper:</span> Folding or cutting alters dimensions and shape, but cellulose fibers remain 100% paper!`;
    } else if (currentMode === 'balloon') {
      balloonWs.classList.remove('hidden');
      inflatedBalloon.classList.remove('hidden');
      poppedBalloon.classList.add('hidden');
      badge.textContent = 'Inflated Balloon';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold';
      explanation.innerHTML = `🎈 <span class="font-bold text-amber-300">Rubber Balloon:</span> Inflating stretches the elastic latex membrane. Even if popped, the shreds remain rubber.`;
    } else {
      chalkWs.classList.remove('hidden');
      solidChalk.classList.remove('hidden');
      crushedChalk.classList.add('hidden');
      badge.textContent = 'Solid Chalk Stick';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 font-bold';
      explanation.innerHTML = `🖍️ <span class="font-bold text-amber-300">Chalk:</span> Crushing chalk to fine dust alters particle size, yet every grain is chemically pure calcium carbonate (CaCO₃)!`;
    }
  }

  btnTransform.addEventListener('click', () => {
    isTransformed = !isTransformed;
    if (currentMode === 'paper') {
      if (isTransformed) {
        foldedPlane.classList.add('hidden');
        shreddedPaper.classList.remove('hidden');
        badge.textContent = 'Cut into Strips';
        playSfx('click');
        explanation.innerHTML = `✂️ <span class="font-bold text-cyan-300">Cut Strips:</span> Paper pieces are smaller in size, but no new chemical substance is formed—pure physical change.`;
      } else {
        foldedPlane.classList.remove('hidden');
        shreddedPaper.classList.add('hidden');
        badge.textContent = 'Folded Plane';
      }
    } else if (currentMode === 'balloon') {
      if (isTransformed) {
        inflatedBalloon.classList.add('hidden');
        poppedBalloon.classList.remove('hidden');
        badge.textContent = 'Popped Latex Shreds';
        badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-300 font-bold';
        playSfx('buzz');
        explanation.innerHTML = `💥 <span class="font-bold text-rose-400">Irreversible Physical Change:</span> The balloon membrane burst under pin pressure; it cannot be re-inflated, but it is still chemically rubber!`;
      } else {
        inflatedBalloon.classList.remove('hidden');
        poppedBalloon.classList.add('hidden');
      }
    } else {
      if (isTransformed) {
        solidChalk.classList.add('hidden');
        crushedChalk.classList.remove('hidden');
        badge.textContent = 'Crushed Chalk Powder';
        badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-amber-950 text-amber-300 font-bold';
        playSfx('click');
        explanation.innerHTML = `💨 <span class="font-bold text-amber-300">Powdered Chalk:</span> Adding water creates chalk paste that can be rolled into a fresh stick—demonstrating physical reversibility!`;
      } else {
        solidChalk.classList.remove('hidden');
        crushedChalk.classList.add('hidden');
      }
    }
  });

  btnReset.addEventListener('click', resetState);
  resetState();
}

// -------------------------------------------------------------
// Sim 2: State Transformations of Matter
// -------------------------------------------------------------
function initStateTransformationsSim(c) {
  const flame = c.querySelector('#phaseFlame');
  const ice = c.querySelector('#iceCubesGroup');
  const liquid = c.querySelector('#liquidWater');
  const steam = c.querySelector('#steamFumes');
  const drops = c.querySelector('#condensedDrops');
  const badge = c.querySelector('#waterPhaseBadge');
  const explanation = c.querySelector('#phaseExplanation');
  const btnHeat = c.querySelector('#btnHeatWater');
  const btnCondense = c.querySelector('#btnCondenseSteam');
  const btnReset = c.querySelector('#btnResetPhase');

  btnHeat.addEventListener('click', () => {
    flame.classList.remove('opacity-0');
    playSfx('buzz');

    setTimeout(() => {
      // Ice melts to water
      ice.classList.add('opacity-0');
      liquid.classList.remove('opacity-0');
      liquid.setAttribute('height', '45');
      badge.textContent = 'Liquid Water (50°C)';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-cyan-950 text-cyan-300 font-mono font-bold';
    }, 600);

    setTimeout(() => {
      // Water boils to steam
      steam.classList.remove('opacity-0');
      badge.textContent = 'Boiling Steam (100°C)';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-300 font-mono font-bold animate-pulse';
      explanation.innerHTML = `♨️ <span class="font-bold text-rose-400">Boiling:</span> Liquid water molecules absorb latent heat of vaporization, separating into gaseous H₂O vapor. Still pure water!`;
      playSfx('ding');
    }, 1200);
  });

  btnCondense.addEventListener('click', () => {
    drops.classList.remove('opacity-0');
    playSfx('click');
    badge.textContent = 'Liquid Condensate';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-300 font-mono font-bold';
    explanation.innerHTML = `❄️ <span class="font-bold text-emerald-400">Condensation:</span> Fast gaseous steam loses thermal kinetic energy on touching the cold metal lid, reconstituting into liquid water drops!`;
  });

  btnReset.addEventListener('click', () => {
    flame.classList.add('opacity-0');
    ice.classList.remove('opacity-0');
    liquid.classList.add('opacity-0');
    steam.classList.add('opacity-0');
    drops.classList.add('opacity-0');
    badge.textContent = 'Solid Ice (0°C)';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-mono font-bold';
    explanation.innerHTML = `💧 Selected Solid Ice. Click 'Heat' to begin physical phase transitions.`;
  });
}

// -------------------------------------------------------------
// Sim 3: Vinegar & Baking Soda Reaction Lab
// -------------------------------------------------------------
function initVinegarBakingSodaSim(c) {
  const btnAdd = c.querySelector('#btnAddBakingSoda');
  const btnReset = c.querySelector('#btnResetReaction');
  const spatula = c.querySelector('#spatulaTool');
  const pile = c.querySelector('#bakingSodaPile');
  const bubbles = c.querySelector('#bubbleGroup');
  const deflated = c.querySelector('#deflatedBalloon');
  const inflated = c.querySelector('#inflatedBalloonCO2');
  const badge = c.querySelector('#reactionStatusBadge');
  const formula = c.querySelector('#vinegarReactionFormula');

  btnAdd.addEventListener('click', () => {
    spatula.style.transform = 'translate(200px, 30px) rotate(-35deg)';
    playSfx('click');

    setTimeout(() => {
      spatula.style.transform = 'translate(290px, 45px) rotate(0deg)';
      pile.classList.remove('hidden');
      bubbles.classList.remove('hidden');
      deflated.classList.add('hidden');
      inflated.classList.remove('hidden');

      badge.textContent = 'REACTING • CO₂ INFLATING';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-400 font-bold animate-pulse';
      formula.textContent = 'CH₃COOH + NaHCO₃ ➔ CH₃COONa + H₂O + CO₂↑ (Chemical Bonds Rearranged!)';
      playSfx('ding');
    }, 600);
  });

  btnReset.addEventListener('click', () => {
    pile.classList.add('hidden');
    bubbles.classList.add('hidden');
    deflated.classList.remove('hidden');
    inflated.classList.add('hidden');
    badge.textContent = 'Unmixed';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 font-bold';
    formula.textContent = 'CH₃COOH (Vinegar) + NaHCO₃ (Baking Soda) ➔ CH₃COONa + H₂O + CO₂↑ (Inflates Balloon!)';
  });
}

// -------------------------------------------------------------
// Sim 4: Lime Water Testing Lab
// -------------------------------------------------------------
function initLimeWaterTestSim(c) {
  const btnBlow = c.querySelector('#btnBlowBreath');
  const btnExcess = c.querySelector('#btnExcessCO2');
  const liquid = c.querySelector('#limeLiquidBody');
  const bubbles = c.querySelector('#breathBubbles');
  const badge = c.querySelector('#limeWaterClarityBadge');
  const formula = c.querySelector('#limeReactionFormula');

  btnBlow.addEventListener('click', () => {
    bubbles.classList.remove('hidden');
    playSfx('buzz');

    setTimeout(() => {
      bubbles.classList.add('hidden');
      liquid.setAttribute('fill', '#f8fafc');
      liquid.setAttribute('fill-opacity', '0.85');
      badge.textContent = 'Milky: Insoluble CaCO₃';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 font-bold';
      formula.textContent = 'Ca(OH)₂ (Lime Water) + CO₂ ➔ CaCO₃↓ (Milky White Solid) + H₂O';
      playSfx('ding');
    }, 800);
  });

  btnExcess.addEventListener('click', () => {
    bubbles.classList.remove('hidden');
    playSfx('buzz');

    setTimeout(() => {
      bubbles.classList.add('hidden');
      liquid.setAttribute('fill', '#38bdf8');
      liquid.setAttribute('fill-opacity', '0.2');
      badge.textContent = 'Clear: Soluble Ca(HCO₃)₂';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-400 font-bold';
      formula.textContent = 'CaCO₃ + H₂O + CO₂ ➔ Ca(HCO₃)₂ (Soluble Calcium Hydrogencarbonate: Clears!)';
      playSfx('ding');
    }, 800);
  });
}

// -------------------------------------------------------------
// Sim 5: Rusting Chemical Change (Mass & Magnetism)
// -------------------------------------------------------------
function initRustingChemicalSim(c) {
  const slider = c.querySelector('#rustExposureSlider');
  const scale = c.querySelector('#digitalScaleReadout');
  const rustFlakes = c.querySelector('#rustFlakesOverlay');
  const magnet = c.querySelector('#magnetTool');
  const nail = c.querySelector('#ironNailAssembly');
  const massBadge = c.querySelector('#rustMassBadge');
  const explanation = c.querySelector('#rustExplanation');
  const btnMagnet = c.querySelector('#btnTestMagnet');

  slider.addEventListener('input', (e) => {
    const val = parseInt(e.target.value, 10);
    const mass = (10.00 + val * 0.28).toFixed(2);
    scale.textContent = `${mass} g`;
    rustFlakes.style.opacity = (val / 10).toString();

    if (val === 0) {
      massBadge.textContent = 'Mass: 10.00 g (Shiny Fe)';
      massBadge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-400 font-mono font-bold';
      explanation.innerHTML = `Shiny polished iron nail. Zero rust. Click 'Test Magnetism'.`;
    } else {
      massBadge.textContent = `Mass: ${mass} g (Hydrated Rust)`;
      massBadge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-amber-950 text-amber-300 font-mono font-bold';
      explanation.innerHTML = `🔩 <span class="font-bold text-amber-300">Oxidation:</span> 4Fe + 3O₂ + 2xH₂O ➔ 2Fe₂O₃·xH₂O. Mass increased from 10.00 g to ${mass} g as oxygen and water bonded!`;
    }
  });

  btnMagnet.addEventListener('click', () => {
    magnet.style.transform = 'translate(260px, 90px)';
    playSfx('click');

    setTimeout(() => {
      const val = parseInt(slider.value, 10);
      if (val < 5) {
        nail.style.transform = 'translate(185px, 95px)';
        playSfx('ding');
      } else {
        // High rust: brittle flakes non-magnetic
        nail.style.transform = 'translate(180px, 110px)';
        playSfx('buzz');
      }
    }, 250);

    setTimeout(() => {
      magnet.style.transform = 'translate(340px, 60px)';
      nail.style.transform = 'translate(180px, 110px)';
    }, 1200);
  });
}

// -------------------------------------------------------------
// Sim 6: Combustion Reactions Lab
// -------------------------------------------------------------
function initCombustionReactionsSim(c) {
  const btnIgnite = c.querySelector('#btnIgniteRibbon');
  const btnDissolve = c.querySelector('#btnDissolveAshMgO');
  const ribbon = c.querySelector('#combustionMgRibbon');
  const flare = c.querySelector('#mgFlareBurst');
  const ash = c.querySelector('#mgWhiteAsh');
  const badge = c.querySelector('#combustionStatusBadge');
  const text = c.querySelector('#combustionReactionText');

  btnIgnite.addEventListener('click', () => {
    flare.classList.remove('hidden');
    ribbon.classList.add('hidden');
    playSfx('buzz');

    setTimeout(() => {
      flare.classList.add('hidden');
      ash.classList.remove('hidden');
      badge.textContent = 'BURNT • MgO ASH FORMED';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 font-bold';
      text.textContent = '2Mg + O₂ ➔ 2MgO (Magnesium Oxide White Ash + Dazzling Flare)';
      btnDissolve.disabled = false;
      btnDissolve.className = 'p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow';
      playSfx('ding');
    }, 1200);
  });

  btnDissolve.addEventListener('click', () => {
    badge.textContent = 'BASIC SOLUTION: Mg(OH)₂';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-blue-950 text-blue-300 font-bold';
    text.textContent = 'MgO + H₂O ➔ Mg(OH)₂ (Red litmus turns BLUE: Metal oxides are BASIC!)';
    playSfx('ding');
  });
}

// -------------------------------------------------------------
// Sim 7: The Fire Triangle & Extinguishment
// -------------------------------------------------------------
function initFireTriangleSim(c) {
  const flame = c.querySelector('#centerFlame');
  const smoke = c.querySelector('#extinguishedSmoke');
  const badge = c.querySelector('#fireStatusBadge');
  const explanation = c.querySelector('#fireTriangleExplanation');

  const edgeFuel = c.querySelector('#edgeFuel');
  const edgeOxygen = c.querySelector('#edgeOxygen');
  const edgeHeat = c.querySelector('#edgeHeat');

  const btnO2 = c.querySelector('#btnCutOxygen');
  const btnHeat = c.querySelector('#btnCoolHeat');
  const btnFuel = c.querySelector('#btnRemoveFuel');

  function extinguish(reason, edge) {
    edge.setAttribute('stroke', '#475569');
    flame.classList.add('hidden');
    smoke.classList.remove('hidden');
    badge.textContent = 'EXTINGUISHED!';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 font-bold';
    explanation.innerHTML = `🧯 <span class="font-bold text-emerald-400">Extinguished:</span> ${reason}! Without all three vertices active, the Fire Triangle collapses.`;
    playSfx('buzz');

    setTimeout(() => {
      edge.setAttribute('stroke', edge === edgeFuel ? '#f59e0b' : (edge === edgeOxygen ? '#38bdf8' : '#ef4444'));
      flame.classList.remove('hidden');
      smoke.classList.add('hidden');
      badge.textContent = 'FLAME BURNING';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-300 font-bold animate-pulse';
    }, 2500);
  }

  btnO2.addEventListener('click', () => extinguish('Oxygen smothered by fire blanket / carbon dioxide', edgeOxygen));
  btnHeat.addEventListener('click', () => extinguish('Cooled below ignition temperature by water spray', edgeHeat));
  btnFuel.addEventListener('click', () => extinguish('Combustible fuel source cut off and isolated', edgeFuel));
}

// -------------------------------------------------------------
// Sim 8: Dual Changes in a Burning Candle
// -------------------------------------------------------------
function initCandleDualChangesSim(c) {
  const btnPhys = c.querySelector('#btnFocusPhysicalCandle');
  const btnChem = c.querySelector('#btnFocusChemicalCandle');
  const insight = c.querySelector('#candleInsightText');

  btnPhys.addEventListener('click', () => {
    insight.innerHTML = `💧 <span class="font-bold text-cyan-300">Physical Phase Transitions:</span> Solid wax absorbs heat, melts into liquid wax, climbs wick via capillary force, and vaporizes into gas. Resolves back to solid wax on cooling!`;
    playSfx('click');
  });

  btnChem.addEventListener('click', () => {
    insight.innerHTML = `🔥 <span class="font-bold text-amber-400">Chemical Combustion Reaction:</span> Wax vapor reacts with oxygen in the flame zone: CₙH₂ₙ₊₂ + O₂ ➔ CO₂ + H₂O + Light + Heat. Irreversible!`;
    playSfx('ding');
  });
}

// -------------------------------------------------------------
// Sim 9: Reversibility Classifier Lab
// -------------------------------------------------------------
function initReversibilityClassifierSim(c) {
  const sampleName = c.querySelector('#currentSampleName');
  const listRev = c.querySelector('#listReversible');
  const listIrrev = c.querySelector('#listIrreversible');
  const badge = c.querySelector('#reversibilityScoreBadge');
  const feedback = c.querySelector('#classifierFeedback');
  const btns = c.querySelectorAll('.btn-classify');

  const dataset = [
    { name: 'Melting Ice into Water', rev: true, note: 'Reversible: Freezing water restores solid ice.' },
    { name: 'Frying a Fresh Egg', rev: false, note: 'Irreversible: Denatured proteins cannot revert.' },
    { name: 'Stretching a Rubber Band', rev: true, note: 'Reversible: Elastic chains relax back.' },
    { name: 'Popping Corn Kernels', rev: false, note: 'Irreversible: Exploded starch matrix cannot reconstitute.' },
    { name: 'Dissolving Sugar in Water', rev: true, note: 'Reversible: Evaporating water recovers crystalline sugar.' },
    { name: 'Burning a Sheet of Paper', rev: false, note: 'Irreversible: Cellulose oxidises to ash, CO₂, and smoke.' }
  ];

  let currentIdx = 0;
  let score = 0;

  function loadSample() {
    if (currentIdx >= dataset.length) {
      sampleName.textContent = 'All Samples Classified!';
      feedback.innerHTML = `🎉 <span class="font-bold text-emerald-400">Mastery Complete:</span> Classified all 6 items with scientific precision!`;
      return;
    }
    sampleName.textContent = dataset[currentIdx].name;
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      if (currentIdx >= dataset.length) return;
      const item = dataset[currentIdx];
      const choiceIsRev = btn.dataset.choice === 'reversible';

      if (choiceIsRev === item.rev) {
        score++;
        playSfx('correct');
        feedback.innerHTML = `✅ <span class="font-bold text-emerald-400">Correct!</span> ${item.note}`;
      } else {
        playSfx('incorrect');
        feedback.innerHTML = `❌ <span class="font-bold text-rose-400">Incorrect:</span> ${item.note}`;
      }

      const pill = document.createElement('div');
      pill.className = `p-1 px-2 rounded text-[11px] ${item.rev ? 'bg-emerald-950 text-emerald-300' : 'bg-rose-950 text-rose-300'} font-semibold`;
      pill.textContent = item.name;

      if (item.rev) listRev.appendChild(pill);
      else listIrrev.appendChild(pill);

      currentIdx++;
      badge.textContent = `Tested: ${score} / ${dataset.length}`;
      loadSample();
    });
  });

  loadSample();
}

// -------------------------------------------------------------
// Sim 10: Desirable vs Undesirable Matrix
// -------------------------------------------------------------
function initDesirableUndesirableSim(c) {
  const btns = c.querySelectorAll('.impact-btn');
  const exp = c.querySelector('#impactExplanation');

  const notes = {
    curd: '🥛 Milk to Curd: Probiotic lactic acid bacteria ferment lactose into lactic acid, creating delicious, nutritious curd (Desirable chemical change).',
    rust: '🔩 Bridge Rusting: Moisture and oxygen oxidise structural iron girders, weakening bridges and costing millions in structural repairs (Undesirable chemical change).',
    fruit: '🥭 Fruit Ripening: Plant hormones convert complex sour starches into sweet fructose sugars and aromatic esters (Desirable biochemical change).',
    smog: '🏭 Vehicle Smog: Fuel combustion releases unburnt hydrocarbons, NO₂, and ozone, producing toxic respiratory smog (Undesirable chemical change).'
  };

  btns.forEach(b => {
    b.addEventListener('click', () => {
      btns.forEach(btn => btn.className = 'impact-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700');
      b.className = 'impact-btn p-2 rounded-xl bg-amber-600 text-white font-bold';
      exp.innerHTML = notes[b.dataset.item];
      playSfx('click');
    });
  });
}

// -------------------------------------------------------------
// Sim 11: Physical Weathering (Frost Wedging)
// -------------------------------------------------------------
function initPhysicalWeatheringSim(c) {
  const btnRain = c.querySelector('#btnRainInfiltrate');
  const btnFreeze = c.querySelector('#btnFreezeWater');
  const btnThermal = c.querySelector('#btnThermalCycle');
  const water = c.querySelector('#seepingWater');
  const ice = c.querySelector('#frostWedgeIce');
  const leftRock = c.querySelector('#boulderHalfLeft');
  const rightRock = c.querySelector('#boulderHalfRight');
  const badge = c.querySelector('#weatheringStateBadge');
  const exp = c.querySelector('#weatheringExplanation');

  btnRain.addEventListener('click', () => {
    water.classList.remove('hidden');
    btnFreeze.disabled = false;
    btnFreeze.className = 'p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow';
    badge.textContent = 'Water in Fissure';
    exp.innerHTML = `🌧️ Rainwater seeps deep into natural hairline cracks of the granite boulder.`;
    playSfx('click');
  });

  btnFreeze.addEventListener('click', () => {
    water.classList.add('hidden');
    ice.classList.remove('hidden');
    leftRock.style.transform = 'translateX(-15px)';
    rightRock.style.transform = 'translateX(15px)';
    badge.textContent = 'SPLIT! Ice Expands (+9%)';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-cyan-950 text-cyan-300 font-bold';
    exp.innerHTML = `💥 <span class="font-bold text-cyan-300">Frost Wedging:</span> Freezing water expanded by 9% in volume, exerting immense hydraulic pressure that snapped the massive rock in two!`;
    playSfx('ding');
  });

  btnThermal.addEventListener('click', () => {
    exp.innerHTML = `☀️ <span class="font-bold text-amber-300">Thermal Exfoliation:</span> Extreme daytime desert heat expands outer mineral layers while chilly nights contract them, causing surface layers to peel off like onion skin!`;
    playSfx('click');
  });
}

// -------------------------------------------------------------
// Sim 12: Chemical Weathering (Caves & Oxidation)
// -------------------------------------------------------------
function initChemicalWeatheringSim(c) {
  const btnCave = c.querySelector('#btnCarbonicAcidCave');
  const btnOxidise = c.querySelector('#btnOxidiseIronRock');
  const cave = c.querySelector('#caveHollow');
  const stalactites = c.querySelector('#stalactites');
  const redStain = c.querySelector('#redOxideStain');
  const badge = c.querySelector('#chemWeatheringBadge');
  const formula = c.querySelector('#chemWeatheringFormula');

  btnCave.addEventListener('click', () => {
    cave.classList.remove('opacity-0');
    stalactites.classList.remove('opacity-0');
    redStain.classList.add('opacity-0');
    badge.textContent = 'Limestone Cave Formed';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-cyan-950 text-cyan-300 font-bold';
    formula.textContent = 'CaCO₃ (Limestone) + H₂CO₃ (Acid Rain) ➔ Ca(HCO₃)₂ (Soluble, Carves Caves!)';
    playSfx('ding');
  });

  btnOxidise.addEventListener('click', () => {
    redStain.classList.remove('opacity-0');
    cave.classList.add('opacity-0');
    stalactites.classList.add('opacity-0');
    badge.textContent = 'Iron Mineral Oxidation';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-amber-950 text-amber-300 font-bold';
    formula.textContent = '4Fe²⁺ + 3O₂ + 6H₂O ➔ 2Fe₂O₃·3H₂O (Red Hematite & Limonite Soil)';
    playSfx('ding');
  });
}

// -------------------------------------------------------------
// Sim 13: Soil Genesis & Erosion Dynamics
// -------------------------------------------------------------
function initSoilErosionSim(c) {
  const btnPlant = c.querySelector('#btnPlantForest');
  const btnMonsoon = c.querySelector('#btnTriggerMonsoon');
  const forest = c.querySelector('#plantedVegetation');
  const runoff = c.querySelector('#muddyRunoff');
  const badge = c.querySelector('#vegetationStatusBadge');
  const exp = c.querySelector('#erosionExplanation');

  let isPlanted = false;

  btnPlant.addEventListener('click', () => {
    isPlanted = true;
    forest.classList.remove('hidden');
    badge.textContent = 'Forested Slope (Root Web)';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-400 font-bold';
    exp.innerHTML = `🌳 <span class="font-bold text-emerald-400">Protected:</span> Deep fibrous tree roots mechanically anchor the topsoil in place and absorb heavy rainfall runoff!`;
    playSfx('click');
  });

  btnMonsoon.addEventListener('click', () => {
    runoff.classList.remove('opacity-0');
    playSfx('buzz');

    setTimeout(() => {
      runoff.classList.add('opacity-0');
      if (isPlanted) {
        exp.innerHTML = `🌧️ <span class="font-bold text-emerald-400">Zero Erosion:</span> The forest canopy cushioned the raindrops, and root networks held the fertile topsoil firmly intact!`;
      } else {
        exp.innerHTML = `⚠️ <span class="font-bold text-rose-400">Severe Erosion:</span> Without roots to anchor the hillside, torrential runoff stripped away millions of tons of fertile topsoil!`;
      }
    }, 1500);
  });
}

// -------------------------------------------------------------
// Sim 14: Thermochemistry: Exo vs Endo Lab
// -------------------------------------------------------------
function initEnergyDynamicsSim(c) {
  const btnExo = c.querySelector('#btnTestQuicklimeExo');
  const btnEndo = c.querySelector('#btnTestGlucoseEndo');
  const col = c.querySelector('#thermoLiquidColumn');
  const badge = c.querySelector('#thermometerTempBadge');
  const formula = c.querySelector('#thermoReactionFormula');
  const frost = c.querySelector('#frostCrystals');
  const boiling = c.querySelector('#boilingBubbles');

  btnExo.addEventListener('click', () => {
    frost.classList.add('hidden');
    boiling.classList.remove('hidden');
    col.setAttribute('y', '15');
    col.setAttribute('height', '95');
    badge.textContent = 'Temp: 95.0°C (Boiling!)';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-300 font-mono font-bold animate-pulse';
    formula.textContent = 'CaO (Quicklime) + H₂O ➔ Ca(OH)₂ + Substantial Heat (Exothermic: ΔT > 0)';
    playSfx('buzz');
  });

  btnEndo.addEventListener('click', () => {
    boiling.classList.add('hidden');
    frost.classList.remove('hidden');
    col.setAttribute('y', '85');
    col.setAttribute('height', '25');
    badge.textContent = 'Temp: 12.0°C (Chilled!)';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-cyan-950 text-cyan-300 font-mono font-bold';
    formula.textContent = 'Glucose(s) + H₂O + Heat ➔ Glucose(aq) (Endothermic: ΔT < 0 Chilling effect)';
    playSfx('ding');
  });
}

// -------------------------------------------------------------
// Sim 15: Law of Conservation of Mass
// -------------------------------------------------------------
function initConservationOfMassSim(c) {
  const btnTilt = c.querySelector('#btnTiltFlaskToReact');
  const btnReset = c.querySelector('#btnResetMassExp');
  const tube = c.querySelector('#internalIgnitionTube');
  const bubbles = c.querySelector('#massBubbles');
  const scale = c.querySelector('#massDisplay');
  const exp = c.querySelector('#massExplanation');

  btnTilt.addEventListener('click', () => {
    tube.style.transform = 'translate(15px, 60px) rotate(60deg)';
    playSfx('click');

    setTimeout(() => {
      bubbles.classList.remove('hidden');
      scale.textContent = '250.00 g';
      exp.innerHTML = `⚖️ <span class="font-bold text-emerald-400">Law Verified:</span> Vigorous bubbling occurred, yet total mass is EXACTLY 250.00 g! In a sealed vessel, atoms rearrange but zero mass is lost!`;
      playSfx('ding');
    }, 500);
  });

  btnReset.addEventListener('click', () => {
    tube.style.transform = 'translate(25px, 45px) rotate(20deg)';
    bubbles.classList.add('hidden');
    scale.textContent = '250.00 g';
    exp.innerHTML = `Sealed container ready. Click 'Tilt Flask & Mix Reactants' to test mass conservation.`;
  });
}

// -------------------------------------------------------------
// Sim 16: Ancient Indian Philosophy (Kanada)
// -------------------------------------------------------------
function initKanadaHeritageSim(c) {
  const btnPitharapaka = c.querySelector('#btnPitharapakaDemo');
  const btnPilupaka = c.querySelector('#btnPilupakaDemo');
  const pot = c.querySelector('#rawClayPot');
  const kilnGlow = c.querySelector('#kilnHeatTejas');
  const exp = c.querySelector('#kanadaHeritageExplanation');

  btnPitharapaka.addEventListener('click', () => {
    pot.setAttribute('d', 'M 115,75 Q 100,110 115,135 L 165,135 Q 180,110 165,75 Z');
    exp.innerHTML = `🌀 <span class="font-bold text-cyan-300">Pitharapaka (Physical Change):</span> Shaping wet gray clay on the potter's wheel changes macroscopic form and volume, but clay molecules remain chemically unchanged!`;
    playSfx('click');
  });

  btnPilupaka.addEventListener('click', () => {
    kilnGlow.classList.add('animate-ping');
    exp.innerHTML = `🔥 <span class="font-bold text-amber-400">Pilupaka (Chemical Metamorphosis):</span> Extreme heat (tejas) in the kiln severs molecular atomic bonds, permanently transforming gray soft clay into hard, insoluble red terracotta!`;
    playSfx('ding');
  });
}
"""

with open(".agents/class7_science_changes_js.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 7 Science Chapter 5 Simulator JavaScript Engines"""\n\n')
    f.write("SIMULATORS_JS = " + repr(JS_CODE) + "\n")

print("Generated .agents/class7_science_changes_js.py successfully.")

