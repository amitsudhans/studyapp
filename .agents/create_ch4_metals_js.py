# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Science Chapter 4 Simulator JavaScript Engines
Outputs .agents/class7_science_metals_js.py
"""

JS_CODE = r"""
// Master Simulator Dispatcher for Chapter 4: The World of Metals and Non-metals
function initSimulatorForSlide(slideId, container) {
  if (!container) return;

  switch(slideId) {
    case 1:
      initCraftspersonForgeSim(container);
      break;
    case 2:
      initMalleabilityLabSim(container);
      break;
    case 3:
      initDuctilityWireSim(container);
      break;
    case 4:
      initSonorityChamberSim(container);
      break;
    case 5:
      initThermalConductionSim(container);
      break;
    case 6:
      initElectricalConductionSim(container);
      break;
    case 7:
      initRustingThreeBottlesSim(container);
      break;
    case 8:
      initRustPreventionSim(container);
      break;
    case 9:
      initBurningMagnesiumSim(container);
      break;
    case 10:
      initCopperPatinaSim(container);
      break;
    case 11:
      initBurningSulfurSim(container);
      break;
    case 12:
      initPhosphorusStorageSim(container);
      break;
    case 13:
      initPropertyMatrixSim(container);
      break;
    case 14:
      initElementBuildingBlocksSim(container);
      break;
    case 15:
      initNonmetalsLifeSim(container);
      break;
    case 16:
      initNagarjunaHeritageSim(container);
      break;
  }
}

// -------------------------------------------------------------
// Sim 1: Craftsperson Blacksmith Forge Lab
// -------------------------------------------------------------
function initCraftspersonForgeSim(c) {
  const btnBellows = c.querySelector('#btnPumpBellows');
  const btnHammer = c.querySelector('#btnHammerStrike');
  const btnSwitch = c.querySelector('#btnSwitchMaterialForge');
  const tempBadge = c.querySelector('#forgeTempBadge');
  const fireEffect = c.querySelector('#forgeFireEffect');
  const emberFlames = c.querySelector('#emberFlames');
  const workpiece = c.querySelector('#forgeWorkpiece');
  const hammerGroup = c.querySelector('#hammerGroup');
  const sparkContainer = c.querySelector('#sparkContainer');
  const matName = c.querySelector('#forgeMatName');
  const feedback = c.querySelector('#forgeFeedback');

  let heated = false;
  let strikes = 0;
  let currentMat = 'iron'; // iron, copper, stone

  if (!btnBellows) return;

  btnBellows.addEventListener('click', () => {
    heated = true;
    fireEffect.classList.remove('opacity-0');
    fireEffect.classList.add('opacity-90');
    emberFlames.classList.remove('opacity-0');
    emberFlames.classList.add('opacity-100');
    tempBadge.textContent = '900°C (Forging Heat)';
    tempBadge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-300 font-bold font-mono animate-pulse';

    if (currentMat === 'iron') {
      workpiece.setAttribute('fill', '#ea580c');
      workpiece.setAttribute('stroke', '#ffedd5');
    } else if (currentMat === 'copper') {
      workpiece.setAttribute('fill', '#d97706');
      workpiece.setAttribute('stroke', '#fed7aa');
    } else {
      workpiece.setAttribute('fill', '#475569');
      workpiece.setAttribute('stroke', '#334155');
    }
    playSfx('buzz');
  });

  btnHammer.addEventListener('click', () => {
    if (!heated) {
      alert('Heat the metal first using the Bellows so it becomes soft and malleable!');
      return;
    }

    // Animate hammer strike
    hammerGroup.style.transform = 'translate(285px, 60px) rotate(15deg)';
    sparkContainer.classList.remove('opacity-0');
    playSfx('ding');

    setTimeout(() => {
      hammerGroup.style.transform = 'translate(285px, 30px) rotate(-25deg)';
      sparkContainer.classList.add('opacity-0');
    }, 150);

    strikes++;
    if (currentMat === 'iron' || currentMat === 'copper') {
      const newWidth = Math.min(85, 55 + strikes * 10);
      const newHeight = Math.max(5, 12 - strikes * 2);
      workpiece.setAttribute('width', newWidth);
      workpiece.setAttribute('height', newHeight);
      workpiece.setAttribute('rx', '1');
      feedback.innerHTML = `🔨 <span class="font-bold text-amber-300">Shaped!</span> Strike count: ${strikes}. Metal spreads into a thin sharp blade without crumbling.`;
    } else {
      // Stone/Coal shatters!
      workpiece.setAttribute('width', '20');
      workpiece.setAttribute('height', '8');
      feedback.innerHTML = `💥 <span class="font-bold text-rose-400">CRACK!</span> Non-metallic stone is brittle and shatters under the hammer instead of shaping!`;
    }
  });

  btnSwitch.addEventListener('click', () => {
    strikes = 0;
    heated = false;
    fireEffect.classList.add('opacity-0');
    emberFlames.classList.add('opacity-0');
    tempBadge.textContent = '25°C (Cold)';
    tempBadge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 font-bold font-mono';
    workpiece.setAttribute('width', '55');
    workpiece.setAttribute('height', '12');

    if (currentMat === 'iron') {
      currentMat = 'copper';
      matName.textContent = 'Copper (Metal)';
      workpiece.setAttribute('fill', '#b45309');
    } else if (currentMat === 'copper') {
      currentMat = 'stone';
      matName.textContent = 'Stone / Coal (Non-metal)';
      workpiece.setAttribute('fill', '#334155');
    } else {
      currentMat = 'iron';
      matName.textContent = 'Iron (Metal)';
      workpiece.setAttribute('fill', '#64748b');
    }
    feedback.innerHTML = `Selected <b>${matName.textContent}</b>. Pump bellows to heat.`;
  });
}

// -------------------------------------------------------------
// Sim 2: Malleability Mechanical Drop Hammer Lab
// -------------------------------------------------------------
function initMalleabilityLabSim(c) {
  const hammer = c.querySelector('#dropHammerHead');
  const specimen = c.querySelector('#specimenShape');
  const crumble = c.querySelector('#crumblePieces');
  const badge = c.querySelector('#malleabilityResultBadge');
  const explanation = c.querySelector('#malleabilityExplanation');
  const btnRelease = c.querySelector('#btnReleaseHammer');
  const btnReset = c.querySelector('#btnResetMalleability');
  const matBtns = c.querySelectorAll('.mat-select-btn');

  let currentMat = 'iron';

  const matConfig = {
    iron: { color: '#cbd5e1', stroke: '#94a3b8', isMetal: true, name: 'Iron Nail' },
    aluminium: { color: '#e2e8f0', stroke: '#cbd5e1', isMetal: true, name: 'Aluminium Block' },
    copper: { color: '#ea580c', stroke: '#c2410c', isMetal: true, name: 'Copper Block' },
    coal: { color: '#1e293b', stroke: '#0f172a', isMetal: false, name: 'Coal Lump' },
    sulfur: { color: '#eab308', stroke: '#ca8a04', isMetal: false, name: 'Sulfur Roll' },
    pencil: { color: '#475569', stroke: '#334155', isMetal: false, name: 'Pencil Lead (Graphite)' }
  };

  matBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      matBtns.forEach(b => {
        b.className = 'mat-select-btn px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';
      });
      btn.className = 'mat-select-btn px-2.5 py-1.5 rounded-lg bg-amber-600 text-white font-bold';
      currentMat = btn.dataset.mat;
      resetSim();
    });
  });

  function resetSim() {
    const cfg = matConfig[currentMat];
    hammer.style.transform = 'translateY(0px)';
    specimen.classList.remove('hidden');
    crumble.classList.add('hidden');
    specimen.setAttribute('width', '30');
    specimen.setAttribute('height', '15');
    specimen.setAttribute('x', '195');
    specimen.setAttribute('y', '130');
    specimen.setAttribute('fill', cfg.color);
    specimen.setAttribute('stroke', cfg.stroke);
    badge.textContent = 'Intact';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold';
    explanation.innerHTML = `<span class="text-amber-400 font-bold">${cfg.name}:</span> Ready for impact testing.`;
  }

  btnRelease.addEventListener('click', () => {
    const cfg = matConfig[currentMat];
    // Drop hammer animation
    hammer.style.transform = 'translateY(70px)';
    playSfx('ding');

    setTimeout(() => {
      hammer.style.transform = 'translateY(0px)';
      if (cfg.isMetal) {
        // Flatten into thin sheet
        specimen.setAttribute('width', '70');
        specimen.setAttribute('height', '4');
        specimen.setAttribute('x', '175');
        specimen.setAttribute('y', '141');
        badge.textContent = 'Malleable: Flattened to Foil';
        badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-400 font-bold';
        explanation.innerHTML = `✨ <span class="font-bold text-emerald-400">Malleable!</span> ${cfg.name} deformed smoothly under pressure into a wide, ultra-thin sheet without any fracturing.`;
      } else {
        // Shatter into crumbles
        specimen.classList.add('hidden');
        crumble.classList.remove('hidden');
        badge.textContent = 'Brittle: Fractured to Dust';
        badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-400 font-bold';
        explanation.innerHTML = `💥 <span class="font-bold text-rose-400">Brittle!</span> ${cfg.name} has zero malleability. The impact shattered its atomic bonds into powdery crumbs.`;
      }
    }, 250);
  });

  btnReset.addEventListener('click', resetSim);
}

// -------------------------------------------------------------
// Sim 3: Ductility Wire Drawing Bench
// -------------------------------------------------------------
function initDuctilityWireSim(c) {
  const select = c.querySelector('#ductilityMatSelect');
  const slider = c.querySelector('#ductilityTensionSlider');
  const tensionDisplay = c.querySelector('#tensionValueDisplay');
  const wireLengthBadge = c.querySelector('#wireLengthBadge');
  const drawnWire = c.querySelector('#drawnWire');
  const winchClamp = c.querySelector('#winchClamp');
  const snapEffect = c.querySelector('#snapEffect');
  const statusText = c.querySelector('#ductilityStatusText');
  const ingot = c.querySelector('#ductilityIngot');

  const configs = {
    copper: { color: '#f59e0b', maxTension: 90, isMetal: true, name: 'Copper' },
    gold: { color: '#facc15', maxTension: 100, isMetal: true, name: 'Gold' },
    aluminium: { color: '#cbd5e1', maxTension: 80, isMetal: true, name: 'Aluminium' },
    iron: { color: '#94a3b8', maxTension: 95, isMetal: true, name: 'Iron' },
    coal: { color: '#334155', maxTension: 20, isMetal: false, name: 'Coal' },
    sulfur: { color: '#eab308', maxTension: 15, isMetal: false, name: 'Sulfur' }
  };

  function update() {
    const mat = configs[select.value];
    const val = parseInt(slider.value, 10);
    tensionDisplay.textContent = `${val} MPa`;
    ingot.setAttribute('fill', mat.color);
    drawnWire.setAttribute('stroke', mat.color);

    if (!mat.isMetal && val > mat.maxTension) {
      // Snap!
      snapEffect.classList.remove('hidden');
      drawnWire.setAttribute('d', 'M 175,90 L 195,90');
      winchClamp.style.transform = `translate(260px, 70px)`;
      wireLengthBadge.textContent = 'SNAPPED!';
      wireLengthBadge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-400 font-mono font-bold';
      statusText.innerHTML = `⚠️ <span class="font-bold text-rose-400">Non-metal Fracture:</span> ${mat.name} cannot undergo plastic elongation. It snapped immediately at ${mat.maxTension} MPa.`;
    } else {
      snapEffect.classList.add('hidden');
      const stretch = Math.floor(10 + val * 1.5);
      const wireX = Math.min(320, 175 + stretch);
      drawnWire.setAttribute('d', `M 175,90 L ${wireX},90`);
      winchClamp.style.transform = `translate(${wireX}px, 70px)`;
      wireLengthBadge.textContent = `Length: ${stretch} mm`;
      wireLengthBadge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-400 font-mono font-bold';
      statusText.innerHTML = `🧵 <span class="font-bold text-amber-300">${mat.name}:</span> Stretching smoothly through the die into a continuous thin filament.`;
    }
  }

  select.addEventListener('change', () => {
    slider.value = 15;
    update();
  });
  slider.addEventListener('input', update);
}

// -------------------------------------------------------------
// Sim 4: Sonority Acoustic Resonance Chamber
// -------------------------------------------------------------
function initSonorityChamberSim(c) {
  const striker = c.querySelector('#strikerMallet');
  const sonorousShape = c.querySelector('#sonorousShape');
  const clapper = c.querySelector('#bellClapperTip');
  const waveRings = c.querySelector('#soundWaveRings');
  const dbBadge = c.querySelector('#sonorityDecibelBadge');
  const feedback = c.querySelector('#sonorityFeedback');
  const trace = c.querySelector('#oscilloscopeTrace');
  const btns = c.querySelectorAll('.sono-mat-btn');
  const btnStrike = c.querySelector('#btnStrikeBell');

  let currentMat = 'bronze';

  const profiles = {
    bronze: {
      d: 'M 140,70 Q 170,60 200,70 L 210,120 Q 170,135 130,120 Z',
      fill: '#d97706',
      stroke: '#f59e0b',
      clapper: true,
      freq: 880,
      decay: 2.2,
      db: '88 dB',
      text: 'Ringing Echo: Brass/Bronze bells sustain acoustic harmonics for several seconds!'
    },
    iron_plate: {
      d: 'M 140,70 L 200,70 L 200,125 L 140,125 Z',
      fill: '#64748b',
      stroke: '#94a3b8',
      clapper: false,
      freq: 550,
      decay: 1.4,
      db: '78 dB',
      text: 'Sharp Clang: Iron plates ring crisply when struck.'
    },
    wood_log: {
      d: 'M 140,75 L 200,75 L 200,120 L 140,120 Z',
      fill: '#78350f',
      stroke: '#b45309',
      clapper: false,
      freq: 180,
      decay: 0.25,
      db: '32 dB',
      text: 'Dull Thud: Wood absorbs vibration energy internally into its fibers.'
    },
    sulfur_block: {
      d: 'M 145,80 L 195,75 L 205,115 L 135,120 Z',
      fill: '#eab308',
      stroke: '#ca8a04',
      clapper: false,
      freq: 120,
      decay: 0.15,
      db: '25 dB',
      text: 'Soft Click: Sulfur produces zero resonance. Non-metals are non-sonorous!'
    }
  };

  btns.forEach(b => {
    b.addEventListener('click', () => {
      btns.forEach(btn => btn.className = 'sono-mat-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700');
      b.className = 'sono-mat-btn p-2 rounded-xl bg-amber-600 text-white font-bold';
      currentMat = b.dataset.mat;
      const p = profiles[currentMat];
      sonorousShape.setAttribute('d', p.d);
      sonorousShape.setAttribute('fill', p.fill);
      sonorousShape.setAttribute('stroke', p.stroke);
      if (p.clapper) clapper.classList.remove('hidden');
      else clapper.classList.add('hidden');
      feedback.textContent = p.text;
    });
  });

  btnStrike.addEventListener('click', () => {
    const p = profiles[currentMat];
    // Mallet animation
    striker.style.transform = 'translate(230px, 95px) rotate(15deg)';
    setTimeout(() => {
      striker.style.transform = 'translate(280px, 80px) rotate(-20deg)';
    }, 120);

    // Audio synth
    playSynthesizedBell(p.freq, p.decay);

    // Wave ring animation
    waveRings.classList.remove('opacity-0');
    setTimeout(() => waveRings.classList.add('opacity-0'), 1500);

    dbBadge.textContent = p.db;
    feedback.innerHTML = `🔔 <span class="font-bold text-amber-300">${p.text}</span>`;

    // Animate oscilloscope
    if (p.decay > 1.0) {
      trace.setAttribute('d', 'M 260,147 Q 275,130 290,147 T 320,147 T 350,147 T 380,147 T 410,147');
      setTimeout(() => trace.setAttribute('d', 'M 260,147 L 410,147'), 1800);
    } else {
      trace.setAttribute('d', 'M 260,147 Q 275,142 290,147 L 410,147');
      setTimeout(() => trace.setAttribute('d', 'M 260,147 L 410,147'), 400);
    }
  });
}

function playSynthesizedBell(freq, duration) {
  try {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (!AudioCtx) return;
    const ctx = new AudioCtx();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = freq > 400 ? 'sine' : 'triangle';
    osc.frequency.setValueAtTime(freq, ctx.currentTime);
    gain.gain.setValueAtTime(0.3, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + duration);

    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + duration);
  } catch(e) {}
}

// -------------------------------------------------------------
// Sim 5: Thermal Conduction Lab
// -------------------------------------------------------------
function initThermalConductionSim(c) {
  const flame = c.querySelector('#bunsenFlame');
  const innerFlame = c.querySelector('#innerFlame');
  const rod = c.querySelector('#conductionRod');
  const overlay = c.querySelector('#heatSpreadOverlay');
  const counter = c.querySelector('#pinFallCounterBadge');
  const explanation = c.querySelector('#thermalExplanation');
  const btnIgnite = c.querySelector('#btnIgniteBurner');
  const btnReset = c.querySelector('#btnResetThermal');
  const rodBtns = c.querySelectorAll('.rod-select-btn');

  let currentRod = 'copper';
  let timerId = null;

  const rodConfigs = {
    copper: { color: '#ea580c', speed: 1.0, name: 'Copper (Fast Conductor)' },
    iron: { color: '#94a3b8', speed: 0.5, name: 'Iron (Moderate Conductor)' },
    glass: { color: '#38bdf8', speed: 0.1, name: 'Glass (Poor Conductor)' },
    wood: { color: '#78350f', speed: 0.0, name: 'Wood (Thermal Insulator)' }
  };

  rodBtns.forEach(b => {
    b.addEventListener('click', () => {
      rodBtns.forEach(btn => btn.className = 'rod-select-btn flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs');
      b.className = 'rod-select-btn flex-1 py-1.5 rounded-lg bg-amber-600 text-white font-bold text-xs';
      currentRod = b.dataset.rod;
      resetSim();
    });
  });

  function resetSim() {
    if (timerId) clearInterval(timerId);
    flame.classList.add('opacity-0');
    innerFlame.classList.add('opacity-0');
    overlay.setAttribute('width', '0');
    rod.setAttribute('fill', rodConfigs[currentRod].color);
    counter.textContent = 'Pins Fallen: 0 / 4';

    for (let i = 1; i <= 4; i++) {
      const pin = c.querySelector(`#waxPin${i}`);
      if (pin) pin.style.transform = 'translateY(0px) rotate(0deg)';
    }
    explanation.innerHTML = `Selected <b>${rodConfigs[currentRod].name}</b>. Click 'Ignite Flame' to test thermal transfer.`;
  }

  btnIgnite.addEventListener('click', () => {
    flame.classList.remove('opacity-0');
    innerFlame.classList.remove('opacity-0');
    playSfx('buzz');

    const cfg = rodConfigs[currentRod];
    let fallen = 0;
    let width = 0;

    if (cfg.speed === 0) {
      explanation.innerHTML = `🪵 <span class="font-bold text-rose-400">Zero Thermal Conduction:</span> Wood lacks free electrons. Heat does not propagate down the rod. All pins remain stuck!`;
      return;
    }

    if (timerId) clearInterval(timerId);
    timerId = setInterval(() => {
      width += 15 * cfg.speed;
      overlay.setAttribute('width', Math.min(260, width));

      if (width >= 50 && fallen < 1) {
        c.querySelector('#waxPin1').style.transform = 'translateY(35px) rotate(35deg)';
        fallen = 1;
        playSfx('click');
      }
      if (width >= 100 && fallen < 2) {
        c.querySelector('#waxPin2').style.transform = 'translateY(35px) rotate(-25deg)';
        fallen = 2;
        playSfx('click');
      }
      if (width >= 150 && fallen < 3) {
        c.querySelector('#waxPin3').style.transform = 'translateY(35px) rotate(40deg)';
        fallen = 3;
        playSfx('click');
      }
      if (width >= 200 && fallen < 4) {
        c.querySelector('#waxPin4').style.transform = 'translateY(35px) rotate(-30deg)';
        fallen = 4;
        playSfx('ding');
        clearInterval(timerId);
      }
      counter.textContent = `Pins Fallen: ${fallen} / 4`;
    }, 300);

    explanation.innerHTML = `🔥 <span class="font-bold text-amber-300">Thermal Gradient:</span> Wax melts sequentially from hottest left end to cooler right end.`;
  });

  btnReset.addEventListener('click', resetSim);
}

// -------------------------------------------------------------
// Sim 6: Electrical Conduction Circuit Tester
// -------------------------------------------------------------
function initElectricalConductionSim(c) {
  const halo = c.querySelector('#circuitBulbHalo');
  const filament = c.querySelector('#circuitFilament');
  const badge = c.querySelector('#circuitContinuityBadge');
  const sampleBar = c.querySelector('#sampleBar');
  const sampleText = c.querySelector('#sampleText');
  const electrons = c.querySelector('#electronDots');
  const explanation = c.querySelector('#electricalExplanation');
  const btns = c.querySelectorAll('.elec-mat-btn');

  const mats = {
    iron_nail: { name: 'Iron Nail', color: '#cbd5e1', conducts: true, note: 'Iron conducts electricity via mobile sea of valence electrons.' },
    copper_wire: { name: 'Copper Wire', color: '#ea580c', conducts: true, note: 'Copper is standard for electrical wiring due to ultra-low resistance.' },
    graphite: { name: 'Pencil Graphite', color: '#334155', conducts: true, note: 'Exception! Graphite is pure carbon non-metal with delocalised pi-electrons between graphene sheets!' },
    sulfur: { name: 'Sulfur Lump', color: '#eab308', conducts: false, note: 'Sulfur is a non-metal insulator with tightly bound localized valence electrons.' },
    rubber: { name: 'Rubber Eraser', color: '#fda4af', conducts: false, note: 'Rubber is an insulator used to coat electrician tools for shock protection.' },
    plastic: { name: 'Plastic Ruler', color: '#38bdf8', conducts: false, note: 'Plastic insulates current and prevents short circuits.' },
    aluminium: { name: 'Al Foil', color: '#e2e8f0', conducts: true, note: 'Aluminium foil is an excellent metallic electrical conductor.' },
    glass: { name: 'Glass Rod', color: '#93c5fd', conducts: false, note: 'Glass is an electrical insulator.' }
  };

  btns.forEach(b => {
    b.addEventListener('click', () => {
      btns.forEach(btn => btn.className = 'elec-mat-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700');
      b.className = 'elec-mat-btn p-2 rounded-xl bg-amber-600 text-white font-bold';
      const m = mats[b.dataset.mat];

      sampleBar.setAttribute('fill', m.color);
      sampleText.textContent = m.name;

      if (m.conducts) {
        halo.classList.remove('opacity-0');
        filament.setAttribute('stroke', '#facc15');
        electrons.classList.remove('opacity-0');
        badge.textContent = 'CLOSED CIRCUIT • GLOWING';
        badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-400 font-bold';
        playSfx('ding');
      } else {
        halo.classList.add('opacity-0');
        filament.setAttribute('stroke', '#64748b');
        electrons.classList.add('opacity-0');
        badge.textContent = 'OPEN CIRCUIT • INSULATOR';
        badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-rose-400 font-bold';
      }
      explanation.innerHTML = `💡 <span class="font-bold text-amber-300">${m.name}:</span> ${m.note}`;
    });
  });
}

// -------------------------------------------------------------
// Sim 7: Rusting of Iron 3-Test-Tube Experiment
// -------------------------------------------------------------
function initRustingThreeBottlesSim(c) {
  const slider = c.querySelector('#rustDaySlider');
  const btnAdvance = c.querySelector('#btnAdvanceWeek');
  const dayDisplay = c.querySelector('#rustDayDisplay');
  const rustA = c.querySelector('#rustCoatingA');
  const conclusion = c.querySelector('#rustingConclusion');

  function updateDay(day) {
    slider.value = day;
    dayDisplay.textContent = `Day ${day} ${day === 0 ? '(Fresh)' : (day === 7 ? '(Final)' : '')}`;
    rustA.style.opacity = (day / 7).toString();

    if (day >= 4) {
      conclusion.innerHTML = `🔬 <span class="font-bold text-rose-400">Result on Day ${day}:</span> Tube A shows extensive hydrated iron(III) oxide (rust: 2Fe₂O₃·xH₂O). Tubes B and C are pristine and rust-free!`;
    } else if (day > 0) {
      conclusion.innerHTML = `⏳ <span class="font-bold text-amber-300">In Progress:</span> Oxygen and water molecules are slowly oxidising iron atoms in Tube A.`;
    } else {
      conclusion.innerHTML = `🔬 <span class="font-bold text-amber-300">Setup:</span> All 3 tubes contain brand new polished iron nails. Advance time to observe rusting.`;
    }
  }

  slider.addEventListener('input', (e) => updateDay(parseInt(e.target.value, 10)));
  btnAdvance.addEventListener('click', () => {
    updateDay(7);
    playSfx('ding');
  });
}

// -------------------------------------------------------------
// Sim 8: Rust Prevention Methods Lab
// -------------------------------------------------------------
function initRustPreventionSim(c) {
  const topLayer = c.querySelector('#protectLayerTop');
  const bottomLayer = c.querySelector('#protectLayerBottom');
  const scratchCut = c.querySelector('#scratchCut');
  const scratchText = c.querySelector('#scratchText');
  const rustBlisters = c.querySelector('#rustBlisters');
  const efficacyBadge = c.querySelector('#protectionEfficacyBadge');
  const note = c.querySelector('#protectionNote');
  const btns = c.querySelectorAll('.shield-btn');
  const btnScratch = c.querySelector('#btnScratchSurface');
  const btnExpose = c.querySelector('#btnSimulateExposure');

  let currentMode = 'galvanise';
  let isScratched = false;

  const modes = {
    bare: {
      color: 'transparent',
      name: 'Bare Iron',
      scratchedRusts: true,
      normalRusts: true,
      text: 'Bare iron has zero protection and rusts heavily in moist air.'
    },
    paint: {
      color: '#f43f5e',
      name: 'Enamel Paint Barrier',
      scratchedRusts: true,
      normalRusts: false,
      text: 'Paint forms a physical barrier. However, once scratched, moisture penetrates and rust spreads underneath!'
    },
    galvanise: {
      color: '#cbd5e1',
      name: 'Galvanised Zinc Coating',
      scratchedRusts: false,
      normalRusts: false,
      text: 'Sacrificial Anode! Even with a deep scratch, zinc oxidises preferentially, preserving the iron cathode.'
    },
    stainless: {
      color: '#38bdf8',
      name: 'Stainless Steel Alloy',
      scratchedRusts: false,
      normalRusts: false,
      text: 'Chromium (18%) and Nickel (8%) alloyed into iron instantly reform a self-healing passive oxide skin!'
    }
  };

  btns.forEach(b => {
    b.addEventListener('click', () => {
      btns.forEach(btn => btn.className = 'shield-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700');
      b.className = 'shield-btn p-2 rounded-xl bg-amber-600 text-white font-bold';
      currentMode = b.dataset.mode;
      resetState();
    });
  });

  function resetState() {
    isScratched = false;
    scratchCut.classList.add('hidden');
    scratchText.classList.add('hidden');
    rustBlisters.classList.add('hidden');
    const m = modes[currentMode];
    topLayer.setAttribute('fill', m.color);
    bottomLayer.setAttribute('fill', m.color);
    efficacyBadge.textContent = currentMode === 'bare' ? 'Unprotected' : 'Protected';
    efficacyBadge.className = currentMode === 'bare'
      ? 'text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-400 font-bold'
      : 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold';
    note.innerHTML = `🛡️ <span class="font-bold text-amber-300">${m.name}:</span> ${m.text}`;
  }

  btnScratch.addEventListener('click', () => {
    isScratched = true;
    scratchCut.classList.remove('hidden');
    scratchText.classList.remove('hidden');
    playSfx('click');
  });

  btnExpose.addEventListener('click', () => {
    const m = modes[currentMode];
    playSfx('buzz');
    if (m.normalRusts || (isScratched && m.scratchedRusts)) {
      rustBlisters.classList.remove('hidden');
      efficacyBadge.textContent = 'RUST FORMED!';
      efficacyBadge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-400 font-bold animate-pulse';
    } else {
      rustBlisters.classList.add('hidden');
      efficacyBadge.textContent = '100% Rust-Free!';
      efficacyBadge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-400 font-bold';
    }
  });

  resetState();
}

// -------------------------------------------------------------
// Sim 9: Burning Magnesium Ribbon & Basic Oxide
// -------------------------------------------------------------
function initBurningMagnesiumSim(c) {
  const btnIgnite = c.querySelector('#btnIgniteMg');
  const btnDissolve = c.querySelector('#btnDissolveAsh');
  const btnLitmus = c.querySelector('#btnDipLitmusMg');
  const ribbon = c.querySelector('#mgRibbon');
  const flash = c.querySelector('#mgFlashBurst');
  const ash = c.querySelector('#whiteAshHeap');
  const station = c.querySelector('#litmusTestingStation');
  const blueTip = c.querySelector('#litmusBlueTip');
  const badge = c.querySelector('#litmusResultBadge');
  const formula = c.querySelector('#mgReactionFormula');

  btnIgnite.addEventListener('click', () => {
    flash.classList.remove('hidden');
    ribbon.classList.add('hidden');
    playSfx('buzz');

    setTimeout(() => {
      flash.classList.add('hidden');
      ash.classList.remove('hidden');
      btnDissolve.disabled = false;
      btnDissolve.className = 'p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow';
      badge.textContent = 'Formed White Ash (MgO)';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 font-bold';
      formula.textContent = '2Mg + O₂ ➔ 2MgO (Magnesium Oxide White Powder)';
    }, 1200);
  });

  btnDissolve.addEventListener('click', () => {
    station.classList.remove('hidden');
    btnLitmus.disabled = false;
    btnLitmus.className = 'p-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs transition shadow';
    badge.textContent = 'Dissolved in H₂O ➔ Mg(OH)₂';
    formula.textContent = 'MgO + H₂O ➔ Mg(OH)₂ (Magnesium Hydroxide Solution)';
    playSfx('click');
  });

  btnLitmus.addEventListener('click', () => {
    blueTip.classList.remove('hidden');
    badge.textContent = 'RED LITMUS TURNED BLUE (BASIC!)';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-blue-950 text-blue-300 font-bold';
    formula.textContent = 'Mg(OH)₂ is a BASE: Turns Red Litmus Paper to BLUE. Metal oxides are BASIC!';
    playSfx('ding');
  });
}

// -------------------------------------------------------------
// Sim 10: Copper Patina Formation & Lemon Cleanse
// -------------------------------------------------------------
function initCopperPatinaSim(c) {
  const greenLayer = c.querySelector('#greenPatinaLayer');
  const lemon = c.querySelector('#lemonTool');
  const badge = c.querySelector('#copperLusterBadge');
  const formula = c.querySelector('#copperReactionText');
  const btnWeather = c.querySelector('#btnWeatherCopper');
  const btnClean = c.querySelector('#btnCleanWithLemon');

  btnWeather.addEventListener('click', () => {
    greenLayer.classList.remove('opacity-0');
    greenLayer.classList.add('opacity-90');
    badge.textContent = 'Green Patina Formed';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-400 font-bold';
    formula.textContent = '2Cu + H₂O + CO₂ + O₂ ➔ CuCO₃·Cu(OH)₂ (Basic Copper Carbonate Green Crust)';
    playSfx('buzz');
  });

  btnClean.addEventListener('click', () => {
    lemon.style.transform = 'translate(220px, 40px)';
    playSfx('click');

    setTimeout(() => {
      greenLayer.classList.remove('opacity-90');
      greenLayer.classList.add('opacity-0');
      lemon.style.transform = 'translate(330px, 70px)';
      badge.textContent = 'Restored Shiny Metallic Luster!';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-400 font-bold';
      formula.textContent = 'Citric acid in lemon neutralises and dissolves basic copper carbonate!';
      playSfx('ding');
    }, 800);
  });
}

// -------------------------------------------------------------
// Sim 11: Burning Sulfur & Acidic Oxide
// -------------------------------------------------------------
function initBurningSulfurSim(c) {
  const btnIgnite = c.querySelector('#btnIgniteSulfur');
  const btnInsert = c.querySelector('#btnInsertGasJar');
  const btnLitmus = c.querySelector('#btnTestAcidicLitmus');
  const flame = c.querySelector('#sulfurBlueFlame');
  const fumes = c.querySelector('#sulfurGasFumes');
  const spoon = c.querySelector('#deflagratingSpoon');
  const strip = c.querySelector('#sulfurLitmusStrip');
  const redTip = c.querySelector('#litmusTurnedRed');
  const badge = c.querySelector('#sulfurLitmusBadge');
  const formula = c.querySelector('#sulfurReactionFormula');

  btnIgnite.addEventListener('click', () => {
    flame.classList.remove('hidden');
    playSfx('buzz');
    btnInsert.disabled = false;
    btnInsert.className = 'p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow';
    badge.textContent = 'Burning with Blue Flame';
  });

  btnInsert.addEventListener('click', () => {
    spoon.style.transform = 'translate(180px, 40px)';
    fumes.classList.remove('opacity-0');
    fumes.classList.add('opacity-70');
    btnLitmus.disabled = false;
    btnLitmus.className = 'p-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs transition shadow';
    badge.textContent = 'Jar Filled with SO₂ Gas';
    formula.textContent = 'S + O₂ ➔ SO₂ (Sulfur Dioxide Pungent Gas)';
    playSfx('click');
  });

  btnLitmus.addEventListener('click', () => {
    strip.classList.remove('hidden');
    redTip.classList.remove('hidden');
    badge.textContent = 'BLUE LITMUS TURNED RED (ACIDIC!)';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-300 font-bold';
    formula.textContent = 'SO₂ + H₂O ➔ H₂SO₃ (Sulfurous Acid: Non-metal oxides are ACIDIC!)';
    playSfx('ding');
  });
}

// -------------------------------------------------------------
// Sim 12: Phosphorus Safe Storage Simulator
// -------------------------------------------------------------
function initPhosphorusStorageSim(c) {
  const btnSubmerge = c.querySelector('#btnKeepSubmerged');
  const btnExpose = c.querySelector('#btnExposeToAir');
  const chunk = c.querySelector('#phosphorusChunk');
  const fumes = c.querySelector('#phosphorusFumes');
  const badge = c.querySelector('#phosphorusSafetyBadge');
  const explanation = c.querySelector('#phosphorusExplanation');

  btnSubmerge.addEventListener('click', () => {
    chunk.style.transform = 'translate(45px, 105px)';
    fumes.classList.add('hidden');
    badge.textContent = 'Submerged & Safe';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold';
    explanation.innerHTML = `💧 <span class="font-bold text-emerald-400">Safe:</span> Water blocks atmospheric oxygen. White phosphorus remains completely inert and safe under water.`;
    playSfx('click');
  });

  btnExpose.addEventListener('click', () => {
    chunk.style.transform = 'translate(45px, 20px)';
    fumes.classList.remove('hidden');
    badge.textContent = 'FIRE HAZARD IN AIR!';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-rose-950 text-rose-300 font-bold animate-pulse';
    explanation.innerHTML = `🔥 <span class="font-bold text-rose-400">Ignition:</span> White phosphorus has an ignition temperature of only ~30°C! It ignites spontaneously in air forming dense white P₄O₁₀ smoke!`;
    playSfx('ding');
  });
}

// -------------------------------------------------------------
// Sim 13: Property Comparison Matrix
// -------------------------------------------------------------
function initPropertyMatrixSim(c) {
  const btns = c.querySelectorAll('.exception-filter-btn');
  btns.forEach(b => {
    b.addEventListener('click', () => {
      btns.forEach(btn => btn.className = 'exception-filter-btn px-2.5 py-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700');
      b.className = 'exception-filter-btn px-2.5 py-1.5 rounded-lg bg-amber-600 text-white font-bold';
      playSfx('click');
    });
  });
}

// -------------------------------------------------------------
// Sim 14: Chemical Elements Building Blocks
// -------------------------------------------------------------
function initElementBuildingBlocksSim(c) {
  const btns = c.querySelectorAll('.elem-group-btn');
  const num = c.querySelector('#elemNum');
  const sym = c.querySelector('#elemSymbol');
  const name = c.querySelector('#elemName');
  const type = c.querySelector('#elemType');
  const badge = c.querySelector('#elementFamilyBadge');

  const groups = {
    metals: {
      num: '26', sym: 'Fe', name: 'Iron (Ferrum)', type: 'Transition Metal • Malleable & Ductile',
      badge: 'Metals (>80% of all Elements)'
    },
    nonmetals: {
      num: '8', sym: 'O', name: 'Oxygen', type: 'Life-Sustaining Non-metal • Respiration',
      badge: 'Non-Metals (18 Elements)'
    },
    metalloids: {
      num: '14', sym: 'Si', name: 'Silicon', type: 'Metalloid • Semiconductor Microchips',
      badge: 'Metalloids (7 Elements)'
    }
  };

  btns.forEach(b => {
    b.addEventListener('click', () => {
      btns.forEach(btn => btn.className = 'elem-group-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs');
      b.className = 'elem-group-btn p-2 rounded-xl bg-amber-600 text-white font-bold text-xs';
      const g = groups[b.dataset.group];
      num.textContent = g.num;
      sym.textContent = g.sym;
      name.textContent = g.name;
      type.textContent = g.type;
      badge.textContent = g.badge;
      playSfx('click');
    });
  });
}

// -------------------------------------------------------------
// Sim 15: Non-metals in Daily Life & Biology
// -------------------------------------------------------------
function initNonmetalsLifeSim(c) {
  const btns = c.querySelectorAll('.life-nm-btn');
  const name = c.querySelector('#lifeElementName');
  const pct = c.querySelector('#lifeElementBodyPct');
  const d1 = c.querySelector('#lifeElementDesc1');
  const d2 = c.querySelector('#lifeElementDesc2');
  const d3 = c.querySelector('#lifeElementDesc3');
  const badge = c.querySelector('#selectedNonmetalRole');

  const data = {
    oxygen: {
      title: 'Oxygen (O₂)', pct: '65% of Human Body Mass',
      d1: '• Cellular respiration for cellular ATP synthesis',
      d2: '• Combustion of fuels and rocket propellants',
      d3: '• Stratospheric ozone layer (O₃) UV shield',
      role: 'Oxygen: Respiration'
    },
    carbon: {
      title: 'Carbon (C)', pct: '18% of Human Body Mass',
      d1: '• Structural backbone of DNA, proteins, sugars',
      d2: '• Graphite (electrical conductor, pencil core)',
      d3: '• Diamond (hardest known cutting tool)',
      role: 'Carbon: Organic Life'
    },
    nitrogen: {
      title: 'Nitrogen (N₂)', pct: '3% of Human Body Mass',
      d1: '• Essential constituent of all amino acids',
      d2: '• Chemical fertilizers (urea) for crop yield',
      d3: '• 78% of atmosphere, prevents runaway fires',
      role: 'Nitrogen: Plant Growth'
    },
    chlorine: {
      title: 'Chlorine (Cl₂)', pct: '0.15% of Body Mass',
      d1: '• Drinking water purification (kills microbes)',
      d2: '• Bleaching agent for paper and textiles',
      d3: '• Stomach hydrochloric acid (HCl) for digestion',
      role: 'Chlorine: Water Disinfection'
    },
    iodine: {
      title: 'Iodine (I₂)', pct: 'Trace / Micronutrient',
      d1: '• Purple antiseptic solution (Tincture of Iodine)',
      d2: '• Essential for thyroid hormone (prevents goitre)',
      d3: '• Unique lustrous non-metallic crystal',
      role: 'Iodine: Antiseptic'
    },
    sulfur: {
      title: 'Sulfur (S)', pct: '0.25% of Body Mass',
      d1: '• Vulcanisation of rubber tires for hardness',
      d2: '• Manufacture of sulfuric acid (king of chemicals)',
      d3: '• Keratin protein in human hair and nails',
      role: 'Sulfur: Vulcanisation'
    }
  };

  btns.forEach(b => {
    b.addEventListener('click', () => {
      btns.forEach(btn => btn.className = 'life-nm-btn p-1.5 rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 text-center');
      b.className = 'life-nm-btn p-1.5 rounded-lg bg-amber-600 text-white font-bold text-center';
      const item = data[b.dataset.elem];
      name.textContent = item.title;
      pct.textContent = item.pct;
      d1.textContent = item.d1;
      d2.textContent = item.d2;
      d3.textContent = item.d3;
      badge.textContent = item.role;
      playSfx('click');
    });
  });
}

// -------------------------------------------------------------
// Sim 16: Ancient Indian Metallurgy Heritage
// -------------------------------------------------------------
function initNagarjunaHeritageSim(c) {
  const btnPillar = c.querySelector('#btnViewDelhiPillar');
  const btnRetort = c.querySelector('#btnViewNagarjunaRetort');
  const viewPillar = c.querySelector('#heritagePillarView');
  const viewRetort = c.querySelector('#heritageRetortView');
  const desc = c.querySelector('#heritageDescription');

  btnPillar.addEventListener('click', () => {
    btnPillar.className = 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs transition shadow';
    btnRetort.className = 'p-2.5 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs transition border border-slate-700';
    viewPillar.classList.remove('hidden');
    viewRetort.classList.add('hidden');
    desc.innerHTML = `🏛️ <span class="font-bold text-amber-300">The Iron Pillar of Delhi (400 CE):</span> High phosphorus content and slag inclusions caused the formation of a protective crystalline film of misawite (δ-FeOOH) that has prevented rusting for over 1600 years!`;
    playSfx('click');
  });

  btnRetort.addEventListener('click', () => {
    btnRetort.className = 'p-2.5 rounded-xl bg-amber-600 text-white font-bold text-xs transition shadow';
    btnPillar.className = 'p-2.5 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold text-xs transition border border-slate-700';
    viewPillar.classList.add('hidden');
    viewRetort.classList.remove('hidden');
    desc.innerHTML = `⚗️ <span class="font-bold text-amber-300">Acharya Nagarjuna & Rasaratnākara:</span> Developed the downward distillation technique (mūṣā-koṣṭhī apparatus) at Zawar, Rajasthan, establishing the world's first industrial production of pure metallic zinc!`;
    playSfx('click');
  });
}
"""

with open(".agents/class7_science_metals_js.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 7 Science Chapter 4 Simulator JavaScript Engines"""\n\n')
    f.write("SIMULATORS_JS = " + repr(JS_CODE) + "\n")

print("Generated .agents/class7_science_metals_js.py successfully.")

