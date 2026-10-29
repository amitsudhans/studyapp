# -*- coding: utf-8 -*-
"""Generated JS for Class 7 Science Chapter 6"""

SIMULATOR_JS = r'''
// Master Simulator Dispatcher for Chapter 6: Adolescence: A Stage of Growth and Change
function initSimulatorForSlide(slideId, container) {
  if (!container) return;

  switch(slideId) {
    case 1:
      initGrowthSpurtSim(container);
      break;
    case 2:
      initSecondaryTraitsSim(container);
      break;
    case 3:
      initAdamsAppleSim(container);
      break;
    case 4:
      initSkinAcneSim(container);
      break;
    case 5:
      initMenstrualCycleSim(container);
      break;
    case 6:
      initMythBusterSim(container);
      break;
    case 7:
      initEmotionalLandscapeSim(container);
      break;
    case 8:
      initNutritionPlateSim(container);
      break;
    case 9:
      initHygieneProtocolSim(container);
      break;
    case 10:
      initPhysicalActivitySim(container);
      break;
    case 11:
      initDigitalSafetySim(container);
      break;
    case 12:
      initSayNoAssertivenessSim(container);
      break;
    case 13:
      initBodyDamageScannerSim(container);
      break;
    case 14:
      initPituitaryEndocrineSim(container);
      break;
    case 15:
      initHormoneFeedbackSim(container);
      break;
    case 16:
      initAyurvedaHeritageSim(container);
      break;
  }
}

// -------------------------------------------------------------
// Sim 1: Growth Spurt Simulator (Age 10-19)
// -------------------------------------------------------------
function initGrowthSpurtSim(c) {
  const badge = c.querySelector('#growthAgeBadge');
  const slider = c.querySelector('#growthAgeSlider');
  const display = c.querySelector('#sliderValueDisplay');
  const explanation = c.querySelector('#growthInsightText');

  const boyFigure = c.querySelector('#figureBoy');
  const girlFigure = c.querySelector('#figureGirl');
  const boyTxt = c.querySelector('#boyHeightTxt');
  const girlTxt = c.querySelector('#girlHeightTxt');
  const plateGlow = c.querySelector('#growthPlateGlow');

  if (!slider) return;

  // Height data benchmarks (Age: [Boy cm, Girl cm, status])
  const heightData = {
    10: { b: 138, g: 138, pctB: 78, pctG: 84, note: "Pre-pubertal baseline: Boys and girls are of similar height. Girls begin their adolescent growth spurt slightly earlier than boys." },
    11: { b: 143, g: 144, pctB: 81, pctG: 88, note: "Girls' growth accelerates first: Estrogen initiates pelvic development and rapid skeletal elongation." },
    12: { b: 149, g: 152, pctB: 84, pctG: 91, note: "Peak velocity for girls: Around age 12, many girls temporarily stand noticeably taller than boys of the same age." },
    13: { b: 156, g: 157, pctB: 88, pctG: 95, note: "Boys' growth spurt begins: Testosterone surges, stimulating growth hormone secretion and cartilage proliferation." },
    14: { b: 163, g: 160, pctB: 92, pctG: 98, note: "Boys overtake girls: Boy growth velocity reaches maximum (approx 8-10 cm/year). Girls approach adult stature." },
    15: { b: 170, g: 162, pctB: 95, pctG: 99, note: "Skeletal widening: Boys experience rapid shoulder expansion and bone mineralization. Epiphyseal plates in girls begin fusing." },
    16: { b: 174, g: 163, pctB: 98, pctG: 100, note: "Growth plate ossification: In girls, long bone cartilage has fully converted into solid bone. Final height is reached." },
    17: { b: 176, g: 163.5, pctB: 99, pctG: 100, note: "Boys nearing terminal height: Long bones (femur, tibia) complete lengthening as epiphyseal cartilage thin out." },
    18: { b: 177, g: 164, pctB: 100, pctG: 100, note: "Complete adult height attained: Growth plates in both males and females are fully ossified. Skeletal height remains fixed." },
    19: { b: 177, g: 164, pctB: 100, pctG: 100, note: "Full physical maturity: 100% of genetic height potential achieved; bone density continues to optimize through balanced nutrition." }
  };

  function update() {
    const age = parseInt(slider.value, 10);
    display.textContent = `${age} Yrs`;
    badge.textContent = `Age: ${age} Years`;

    const d = heightData[age] || heightData[14];
    boyTxt.textContent = `${d.b} cm (${d.pctB}%)`;
    girlTxt.textContent = `${d.g} cm (${d.pctG}%)`;

    // Visual scale adjustments
    // Baseline scale at age 10: boy scale 0.85, girl scale 0.85; at age 18: boy scale 1.15, girl scale 1.05
    const bScale = 0.82 + (d.b - 138) / 100;
    const gScale = 0.82 + (d.g - 138) / 80;

    boyFigure.setAttribute('transform', `translate(100, ${150 - (d.b * 0.65)}) scale(1, ${bScale})`);
    girlFigure.setAttribute('transform', `translate(180, ${150 - (d.g * 0.65)}) scale(1, ${gScale})`);

    // Epiphyseal plate active pulse check
    if (age >= 18) {
      plateGlow.setAttribute('fill', '#64748b');
      plateGlow.classList.remove('animate-pulse');
    } else {
      plateGlow.setAttribute('fill', '#38bdf8');
      plateGlow.classList.add('animate-pulse');
    }

    explanation.innerHTML = `🧬 <span class="font-bold text-amber-300">Growth Spurt Dynamics (Age ${age}):</span> ${d.note} <span class="text-cyan-400 font-semibold">[Boy: ${d.b} cm | Girl: ${d.g} cm]</span>`;
  }

  slider.addEventListener('input', update);
  update();
}

// -------------------------------------------------------------
// Sim 2: Secondary Sexual Characteristics Scanner
// -------------------------------------------------------------
function initSecondaryTraitsSim(c) {
  const badge = c.querySelector('#genderSelectBadge');
  const btnMale = c.querySelector('#btnSelectMaleTraits');
  const btnFemale = c.querySelector('#btnSelectFemaleTraits');

  const facialHair = c.querySelector('#facialHair');
  const neckAdamsApple = c.querySelector('#neckAdamsApple');
  const maleTorso = c.querySelector('#maleTorso');
  const femaleTorso = c.querySelector('#femaleTorso');
  const femaleBreasts = c.querySelector('#femaleBreasts');

  const cardTitle = c.querySelector('#traitCardTitle');
  const trait1 = c.querySelector('#trait1');
  const trait2 = c.querySelector('#trait2');
  const trait3 = c.querySelector('#trait3');
  const trait4 = c.querySelector('#trait4');
  const trait5 = c.querySelector('#trait5');
  const explanation = c.querySelector('#secondaryTraitsExplanation');

  function setGender(gender) {
    if (gender === 'male') {
      badge.textContent = 'Adolescent Male (Testosterone Mediated)';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-400 font-bold';

      btnMale.className = 'p-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow';
      btnFemale.className = 'p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition';

      facialHair.classList.remove('hidden');
      neckAdamsApple.classList.remove('hidden');
      maleTorso.classList.remove('hidden');
      femaleTorso.classList.add('hidden');
      femaleBreasts.classList.add('hidden');

      cardTitle.textContent = 'Male Secondary Traits';
      cardTitle.setAttribute('fill', '#38bdf8');
      trait1.textContent = '• Broad shoulders & chest expansion';
      trait2.textContent = "• Protruding Adam's apple (larynx enlargement)";
      trait3.textContent = '• Deepening vocal pitch (~110 Hz)';
      trait4.textContent = '• Facial, underarm, and pubic hair';
      trait5.textContent = '• Lean muscle mass acceleration (testosterone)';

      explanation.innerHTML = `♂️ <span class="font-bold text-cyan-300">Testosterone Surge:</span> Produced by the testes under pituitary LH/FSH signals, testosterone triggers broadening of shoulders, facial beard/mustache development, vocal fold thickening, and spermatogenesis capability.`;
    } else {
      badge.textContent = 'Adolescent Female (Estrogen Mediated)';
      badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-rose-400 font-bold';

      btnMale.className = 'p-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition';
      btnFemale.className = 'p-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs transition shadow';

      facialHair.classList.add('hidden');
      neckAdamsApple.classList.add('hidden');
      maleTorso.classList.add('hidden');
      femaleTorso.classList.remove('hidden');
      femaleBreasts.classList.remove('hidden');

      cardTitle.textContent = 'Female Secondary Traits';
      cardTitle.setAttribute('fill', '#f43f5e');
      trait1.textContent = '• Pelvic & hip widening (birth canal preparation)';
      trait2.textContent = '• Breast development & mammary gland budding';
      trait3.textContent = '• High-pitched melodious voice (~220-260 Hz)';
      trait4.textContent = '• Underarm and pubic hair appearance';
      trait5.textContent = '• Onset of menstrual cycle (menarche indicator)';

      explanation.innerHTML = `♀️ <span class="font-bold text-rose-400">Estrogen Surge:</span> Secreted by the ovaries upon pituitary stimulation, estrogen directs hip widening, breast enlargement, uterine endometrial thickening, and initiates periodic ovulation and menstruation.`;
    }
  }

  if (btnMale) btnMale.addEventListener('click', () => setGender('male'));
  if (btnFemale) btnFemale.addEventListener('click', () => setGender('female'));

  setGender('male');
}

// -------------------------------------------------------------
// Sim 3: Adam's Apple & Voice Pitch Lab
// -------------------------------------------------------------
function initAdamsAppleSim(c) {
  const badge = c.querySelector('#voicePitchBadge');
  const slider = c.querySelector('#larynxSizeSlider');
  const btnPlay = c.querySelector('#btnPlayVocalNote');
  const explanation = c.querySelector('#voiceExplanation');

  const larynx = c.querySelector('#thyroidCartilage');
  const cordL = c.querySelector('#vocalCordLeft');
  const cordR = c.querySelector('#vocalCordRight');
  const wave = c.querySelector('#voiceWaveform');

  if (!slider) return;

  const larynxLevels = {
    1: { hz: 260, label: "260 Hz (High Pitch)", scale: 0.8, cordW: 2, desc: "Childhood voice: Small thyroid cartilage, vocal folds are short and thin, producing rapid high-frequency sound vibrations (~260 Hz)." },
    2: { hz: 220, label: "220 Hz (Adolescent Female / Youth)", scale: 0.9, cordW: 2.5, desc: "Juvenile pitch: Cartilage slightly enlarges; vocal cords remain relatively short, characteristic of female and early teen voices." },
    3: { hz: 170, label: "170 Hz (Voice Cracking Transition)", scale: 1.1, cordW: 3.2, desc: "Pubertal cracking: As testosterone surges, larynx cartilage expands faster than muscle control adapts, causing fluctuating voice breaks." },
    4: { hz: 130, label: "130 Hz (Deepening Baritone)", scale: 1.3, cordW: 4.2, desc: "Significant larynx enlargement: The thyroid cartilage protrudes visibly at the throat as the Adam's apple; vocal cords lengthen." },
    5: { hz: 105, label: "105 Hz (Deep Resonant Bass)", scale: 1.5, cordW: 5.5, desc: "Mature adult male voice: Long, thick vocal cords vibrate slowly, producing a deep, resonant pitch with a pronounced Adam's apple." }
  };

  function update() {
    const level = parseInt(slider.value, 10);
    const d = larynxLevels[level] || larynxLevels[4];

    badge.textContent = `Pitch: ${d.label}`;

    // Scale thyroid cartilage protrusion
    larynx.setAttribute('transform', `scale(${d.scale})`);
    cordL.setAttribute('stroke-width', d.cordW);
    cordR.setAttribute('stroke-width', d.cordW);

    // Waveform visualization: dense vs stretched waves
    if (level <= 2) {
      wave.setAttribute('d', 'M 10,25 Q 20,5 30,25 T 50,25 T 70,25 T 90,25 T 110,25 T 130,25');
      wave.setAttribute('stroke', '#38bdf8');
    } else if (level === 3) {
      wave.setAttribute('d', 'M 10,25 Q 22,7 35,25 T 65,25 T 95,25 T 125,25');
      wave.setAttribute('stroke', '#fbbf24');
    } else {
      wave.setAttribute('d', 'M 10,25 Q 35,0 60,25 T 110,25 T 160,25');
      wave.setAttribute('stroke', '#22c55e');
    }

    explanation.innerHTML = `🎙️ <span class="font-bold text-amber-300">Acoustic Anatomy:</span> ${d.desc}`;
  }

  function playTone() {
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      const ctx = new AudioCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      const level = parseInt(slider.value, 10);
      const freq = (larynxLevels[level] && larynxLevels[level].hz) || 130;

      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, ctx.currentTime);

      gain.gain.setValueAtTime(0.2, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.6);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start();
      osc.stop(ctx.currentTime + 0.6);
    } catch(e) {
      console.log('AudioContext preview not allowed or disabled', e);
    }
  }

  slider.addEventListener('input', update);
  if (btnPlay) btnPlay.addEventListener('click', playTone);

  update();
}

// -------------------------------------------------------------
// Sim 4: Skin Glands & Acne Genesis Lab
// -------------------------------------------------------------
function initSkinAcneSim(c) {
  const badge = c.querySelector('#skinPoreStatusBadge');
  const pimple = c.querySelector('#pimpleInflammation');
  const btnSurge = c.querySelector('#btnSurgeHormoneSebum');
  const btnCleanse = c.querySelector('#btnCleanseFace');
  const explanation = c.querySelector('#skinAcneExplanation');

  function triggerAcne() {
    badge.textContent = 'Pore Status: Clogged & Inflamed (Acne)';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-rose-400 font-bold';

    if (pimple) pimple.classList.remove('hidden');

    explanation.innerHTML = `⚡ <span class="font-bold text-rose-400">Sebaceous Overactivity:</span> During puberty, sex hormones (especially androgens) stimulate sebaceous and sweat glands to secrete excess oily sebum. When sticky sebum mixes with shed dead epidermal cells, it plugs the hair follicle pore. Trapped skin bacteria (Cutibacterium acnes) multiply, creating inflammation, redness, and pimples!`;
  }

  function cleanseFace() {
    badge.textContent = 'Pore Status: Clean & Healthy Flow';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold';

    if (pimple) pimple.classList.add('hidden');

    explanation.innerHTML = `🧼 <span class="font-bold text-emerald-400">Dermatological Care:</span> Washing the face twice daily with clean water and mild soap removes excess surface sebum and unclogs follicular pores. <span class="text-amber-300 font-bold">Never squeeze or scratch pimples</span>, as that drives infection deeper and causes permanent scarring!`;
  }

  if (btnSurge) btnSurge.addEventListener('click', triggerAcne);
  if (btnCleanse) btnCleanse.addEventListener('click', cleanseFace);

  cleanseFace();
}

// -------------------------------------------------------------
// Sim 5: 28-Day Menstrual Cycle Clock
// -------------------------------------------------------------
function initMenstrualCycleSim(c) {
  const badge = c.querySelector('#cyclePhaseBadge');
  const hand = c.querySelector('#cycleHand');
  const lining = c.querySelector('#endometriumLining');
  const liningDesc = c.querySelector('#endometriumDesc');
  const ovum = c.querySelector('#ovumStatus');
  const explanation = c.querySelector('#cycleExplanation');
  const phaseBtns = c.querySelectorAll('.cycle-btn');

  const phaseData = {
    menstruation: {
      title: "Days 1 to 5: Menstruation (Menses)",
      colorClass: "text-rose-400",
      rotAngle: 30, // hand rotation degrees
      liningHeight: 4,
      liningFill: "#f43f5e",
      liningLabel: "Lining Shedding: 1-2 mm",
      ovumLabel: "No live ovum",
      btnClass: "bg-rose-600 text-white font-bold",
      desc: "If fertilization did not occur in the previous cycle, the hormone progesterone drops sharply. The spongy, vascular uterine lining (endometrium) breaks down and is discharged through the vagina along with unfertilized ovum tissue and 30-50 mL of sterile blood over 3 to 7 days."
    },
    follicular: {
      title: "Days 6 to 13: Follicular / Repair Phase",
      colorClass: "text-amber-300",
      rotAngle: 120,
      liningHeight: 12,
      liningFill: "#fb7185",
      liningLabel: "Regenerating Lining: 4-6 mm",
      ovumLabel: "Follicle maturing in ovary",
      btnClass: "bg-amber-600 text-white font-bold",
      desc: "Pituitary FSH stimulates an ovarian follicle to mature an egg. Concurrently, developing ovaries secrete estrogen, which stimulates rapid cell proliferation to repair and rebuild a rich new endometrial lining lined with fresh capillary blood vessels."
    },
    ovulation: {
      title: "Day 14: Ovulation (Peak Fertility)",
      colorClass: "text-emerald-400",
      rotAngle: 180,
      liningHeight: 18,
      liningFill: "#e11d48",
      liningLabel: "Prepared Lining: 8-10 mm",
      ovumLabel: "Egg released into fallopian tube!",
      btnClass: "bg-emerald-600 text-white font-bold",
      desc: "A mid-cycle surge in pituitary Luteinizing Hormone (LH) triggers the mature Graafian follicle to rupture. One mature ovum (egg) is released into the fallopian tube (oviduct), where it survives for approximately 24 hours awaiting potential sperm fertilization."
    },
    luteal: {
      title: "Days 15 to 28: Luteal / Secretory Phase",
      colorClass: "text-purple-300",
      rotAngle: 280,
      liningHeight: 24,
      liningFill: "#be123c",
      liningLabel: "Spongy Glandular Lining: 12 mm",
      ovumLabel: "Corpus luteum secreting progesterone",
      btnClass: "bg-purple-600 text-white font-bold",
      desc: "The ruptured follicle transforms into the temporary endocrine structure corpus luteum, pumping out progesterone. This causes the endometrium to become highly vascular, nutrient-rich, and ready to nourish an embryo. If no sperm fertilizes the egg, the corpus luteum degenerates, triggering menstruation anew."
    }
  };

  function setPhase(key) {
    const p = phaseData[key];
    if (!p) return;

    badge.textContent = p.title;
    badge.className = `text-[11px] px-2 py-0.5 rounded-full bg-slate-800 ${p.colorClass} font-mono font-bold`;

    phaseBtns.forEach(btn => {
      btn.className = 'cycle-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs transition';
      if (btn.dataset.phase === key) {
        btn.className = `cycle-btn p-2 rounded-xl ${p.btnClass} text-xs transition shadow`;
      }
    });

    if (hand) hand.setAttribute('transform', `rotate(${p.rotAngle})`);
    if (lining) {
      lining.setAttribute('height', p.liningHeight);
      lining.setAttribute('y', 150 - p.liningHeight);
      lining.setAttribute('fill', p.liningFill);
    }
    if (liningDesc) liningDesc.textContent = p.liningLabel;
    if (ovum) ovum.textContent = p.ovumLabel;

    explanation.innerHTML = `🗓️ <span class="font-bold text-amber-300">${p.title}:</span> ${p.desc}`;
  }

  phaseBtns.forEach(btn => {
    btn.addEventListener('click', () => setPhase(btn.dataset.phase));
  });

  setPhase('menstruation');
}

// -------------------------------------------------------------
// Sim 6: Menstrual Myth-Busting Interactive Chamber
// -------------------------------------------------------------
function initMythBusterSim(c) {
  const mythTxt = c.querySelector('#mythText');
  const truthTxt = c.querySelector('#truthText');
  const note = c.querySelector('#mythBusterNote');
  const mythBtns = c.querySelectorAll('.myth-btn');

  const myths = [
    {
      myth: "MYTH 1: 'A menstruating girl is impure, should be isolated in dark rooms, and must never touch food, water pots, or pickles lest they rot!'",
      truth: "SCIENTIFIC FACT: Menstrual blood is entirely clean, natural, and sterile biological fluid containing shed endometrium and blood. It emits NO toxic fumes or rays and CANNOT spoil food, curds, or pickles. Isolation causes psychological trauma and dangerous unhygienic conditions.",
      note: "Scientific Consensus: Food spoiling is caused exclusively by bacteria and airborne mold spores, completely unrelated to human hormones or menstruation!"
    },
    {
      myth: "MYTH 2: 'Girls should avoid bathing, hair-washing, physical play, and school sports during their monthly periods.'",
      truth: "SCIENTIFIC FACT: Regular warm baths with soap are essential for personal hygiene to prevent bacterial infection and relieve cramps. Light exercise, walking, and sports stimulate endorphin release, actually reducing pelvic pain and uplifting mood!",
      note: "Global Health Recommendation: Active physical movement boosts circulation and relieves tension. Female Olympic athletes routinely win medals during their cycles!"
    },
    {
      myth: "MYTH 3: 'Menstruation is a disease, an embarrassing family secret, or a curse that signals physical weakness.'",
      truth: "SCIENTIFIC FACT: Menarche (first cycle) and regular menstruation are universal indicators of optimal reproductive health, endocrine harmony, and biological vitality in half of the human species. Open conversations eliminate stigma.",
      note: "Ancient & Modern Unity: Sushruta Samhita describes Artava Pravritti as an auspicious natural phenomenon. It should be celebrated with dignity, empathy, and scientific pride!"
    }
  ];

  function showMyth(idx) {
    const item = myths[idx] || myths[0];
    if (mythTxt) mythTxt.textContent = item.myth;
    if (truthTxt) truthTxt.textContent = item.truth;
    if (note) note.innerHTML = `💡 <span class="font-bold text-emerald-400">Scientific Truth:</span> ${item.note}`;

    mythBtns.forEach((b, i) => {
      b.className = 'myth-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs transition';
      if (i === idx) {
        b.className = 'myth-btn p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs transition shadow';
      }
    });
  }

  mythBtns.forEach(btn => {
    btn.addEventListener('click', () => showMyth(parseInt(btn.dataset.idx, 10)));
  });

  showMyth(0);
}

// -------------------------------------------------------------
// Sim 7: Adolescent Brain & Emotional Landscape Lab
// -------------------------------------------------------------
function initEmotionalLandscapeSim(c) {
  const badge = c.querySelector('#brainStateBadge');
  const pfc = c.querySelector('#pfcZone');
  const amygdala = c.querySelector('#amygdalaGlow');
  const reaction = c.querySelector('#scenarioReaction');
  const btnImpulsive = c.querySelector('#btnReactImpulsive');
  const btnReflect = c.querySelector('#btnPauseReflect');
  const insight = c.querySelector('#emotionalInsight');

  function reactImpulsive() {
    badge.textContent = 'Brain State: Amygdala Hijack (High Emotion)';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-rose-400 font-bold';

    if (amygdala) {
      amygdala.setAttribute('fill', '#f43f5e');
      amygdala.setAttribute('r', '18');
      amygdala.classList.add('animate-ping');
    }
    if (pfc) {
      pfc.setAttribute('fill', '#334155');
    }

    if (reaction) {
      reaction.textContent = '"I yelled back angrily, slammed the door, and regret saying hurtful words later."';
      reaction.setAttribute('fill', '#fca5a5');
    }

    insight.innerHTML = `⚡ <span class="font-bold text-rose-400">The Reactive Amygdala:</span> In adolescents, the emotional processing center (amygdala) matures years before the prefrontal cortex (rational decision-making). Under stress or peer friction, immediate gut reactions dominate, causing dramatic mood swings and impulsive outbursts.`;
  }

  function pauseReflect() {
    badge.textContent = 'Brain State: Prefrontal Cortex Engaged (Mindful)';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold';

    if (amygdala) {
      amygdala.setAttribute('fill', '#64748b');
      amygdala.setAttribute('r', '10');
      amygdala.classList.remove('animate-ping');
    }
    if (pfc) {
      pfc.setAttribute('fill', '#22c55e');
    }

    if (reaction) {
      reaction.textContent = '"I took 3 slow, deep breaths, counted to 5, and calmly explained my boundaries."';
      reaction.setAttribute('fill', '#86efac');
    }

    insight.innerHTML = `🧠 <span class="font-bold text-emerald-400">Prefrontal Impulse Control:</span> By taking a brief pause and slow breaths, adolescents give neural signals time to cross to the prefrontal cortex. This transforms emotional conflict into constructive problem-solving, building resilience and emotional intelligence.`;
  }

  if (btnImpulsive) btnImpulsive.addEventListener('click', reactImpulsive);
  if (btnReflect) btnReflect.addEventListener('click', pauseReflect);

  pauseReflect();
}

// -------------------------------------------------------------
// Sim 8: Balanced Adolescent Nutrition Plate Lab
// -------------------------------------------------------------
function initNutritionPlateSim(c) {
  const badge = c.querySelector('#plateBalanceBadge');
  const quadCarbs = c.querySelector('#quadCarbs');
  const quadProteins = c.querySelector('#quadProteins');
  const quadGreens = c.querySelector('#quadGreens');
  const quadDairy = c.querySelector('#quadDairy');

  const nutriProtein = c.querySelector('#nutriProtein');
  const nutriIron = c.querySelector('#nutriIron');
  const nutriCalcium = c.querySelector('#nutriCalcium');
  const nutriCarbs = c.querySelector('#nutriCarbs');
  const verdict = c.querySelector('#nutriVerdict');
  const nutriBtns = c.querySelectorAll('.nutri-btn');

  const foodProfiles = {
    carbs: {
      title: "Complex Carbohydrates (Roti, Brown Rice, Oats)",
      carbs: "90%", prot: "20%", iron: "30%", calc: "15%",
      badge: "Carbohydrates: High Sustained Energy",
      note: "Complex starches provide prolonged glycogen release to fuel rapid metabolism, study concentration, and active games without sugar crashes."
    },
    protein: {
      title: "Proteins (Dal, Pulses, Soybeans, Eggs, Paneer)",
      carbs: "25%", prot: "95%", iron: "65%", calc: "40%",
      badge: "Proteins: Muscle & Cellular Growth",
      note: "Essential amino acids are the vital building blocks for expanding muscle fibers, cellular division, tissue repair, and enzyme synthesis during pubertal spurts."
    },
    greens: {
      title: "Green Leafy Vegetables & Fruits (Palak, Jaggery, Citrus)",
      carbs: "30%", prot: "25%", iron: "98%", calc: "50%",
      badge: "Iron & Micronutrients: Anemia Shield",
      note: "Rich in iron and vitamin C, leafy greens are crucial for hemoglobin synthesis and blood volume expansion, especially safeguarding adolescent girls against iron-deficiency anemia."
    },
    dairy: {
      title: "Dairy Products (Milk, Curd, Buttermilk, Cheese)",
      carbs: "35%", prot: "70%", iron: "20%", calc: "95%",
      badge: "Calcium & Vitamin D: Peak Bone Mass",
      note: "High bioavailable calcium mineralizes growing epiphyseal cartilage, building dense skeletal bone mass that protects against fractures throughout adult life."
    },
    junk: {
      title: "Empty Junk Food (Chips, Colas, Instant Noodles)",
      carbs: "95% (Sugar/Fat)", prot: "5%", iron: "0%", calc: "0%",
      badge: "Deficient: Empty Calories Warning!",
      note: "High refined sugars and unhealthy trans-fats satisfy immediate appetite but starve growing organs of vital iron, calcium, and protein, leading to fatigue and poor immunity."
    }
  };

  function selectFood(key) {
    const p = foodProfiles[key];
    if (!p) return;

    badge.textContent = p.badge;
    nutriProtein.style.width = p.prot;
    nutriIron.style.width = p.iron;
    nutriCalcium.style.width = p.calc;
    nutriCarbs.style.width = p.carbs;

    nutriBtns.forEach(b => {
      b.className = 'nutri-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs transition';
      if (b.dataset.food === key) {
        b.className = (key === 'junk') 
          ? 'nutri-btn p-2 rounded-xl bg-rose-600 text-white font-bold text-xs transition shadow'
          : 'nutri-btn p-2 rounded-xl bg-amber-600 text-white font-bold text-xs transition shadow';
      }
    });

    verdict.innerHTML = `🥗 <span class="font-bold text-amber-300">${p.title}:</span> ${p.note}`;
  }

  nutriBtns.forEach(btn => {
    btn.addEventListener('click', () => selectFood(btn.dataset.food));
  });

  selectFood('greens');
}

// -------------------------------------------------------------
// Sim 9: Personal & Menstrual Hygiene Protocol
// -------------------------------------------------------------
function initHygieneProtocolSim(c) {
  const btnGovt = c.querySelector('#btnGovtSchemes');
  const btnDisposal = c.querySelector('#btnDisposalRules');
  const explanation = c.querySelector('#hygieneExplanation');

  function showGovt() {
    explanation.innerHTML = `🏛️ <span class="font-bold text-cyan-300">National Adolescent Health Initiatives:</span>
    <ul class="list-disc pl-5 mt-1 space-y-1">
      <li><span class="text-amber-300 font-bold">MHS (Menstrual Hygiene Scheme):</span> Provides high-quality, subsidized sanitary napkins through ASHA workers to adolescent girls in rural schools across India.</li>
      <li><span class="text-emerald-400 font-bold">RKSK (Rashtriya Kishor Swasthya Karyakram):</span> Community health program offering counseling, iron-folic acid (IFA) supplements, and Adolescent Friendly Health Clinics (AFHC).</li>
    </ul>`;
  }

  function showDisposal() {
    explanation.innerHTML = `🚯 <span class="font-bold text-rose-400">Strict Sanitary Disposal Protocol:</span>
    <ol class="list-decimal pl-5 mt-1 space-y-1">
      <li><span class="text-amber-300 font-bold">Never flush pads:</span> Modern sanitary pads contain absorbent polymers that expand and cause massive sewer blockages, pipe damage, and environmental pollution.</li>
      <li><span class="text-emerald-400 font-bold">Wrap in paper:</span> Always wrap used pads neatly in discarded newspaper or biodegradable wrapper.</li>
      <li><span class="text-cyan-300 font-bold">Dispose in closed trash bin:</span> Place in dedicated dry-waste dustbins for safe incineration or sanitary landfill disposal. Wash hands thoroughly with soap.</li>
    </ol>`;
  }

  if (btnGovt) btnGovt.addEventListener('click', showGovt);
  if (btnDisposal) btnDisposal.addEventListener('click', showDisposal);

  showGovt();
}

// -------------------------------------------------------------
// Sim 10: Physical Activity & Mood Endorphin Lab
// -------------------------------------------------------------
function initPhysicalActivitySim(c) {
  const badge = c.querySelector('#endorphinBadge');
  const staminaBar = c.querySelector('#staminaBar');
  const endorphinBar = c.querySelector('#endorphinBar');
  const boneBar = c.querySelector('#boneBar');
  const explanation = c.querySelector('#activityExplanation');
  const actBtns = c.querySelectorAll('.activity-btn');
  const runner = c.querySelector('#runnerAthlete');

  const actData = {
    sedentary: {
      badge: "Sedentary Screen Time (Lethargy)",
      badgeClass: "text-rose-400",
      stamina: "25%", endorphin: "15%", bone: "30%",
      desc: "Sitting for prolonged periods with mobile phones or TVs leads to poor posture, sluggish blood flow, weak bone mineralization, and irritability.",
      btnClass: "bg-rose-600 text-white font-bold"
    },
    yoga: {
      badge: "30 Mins Daily Yoga & Pranayama (Mental Calm)",
      badgeClass: "text-amber-300",
      stamina: "65%", endorphin: "75%", bone: "70%",
      desc: "Gentle stretching improves spinal flexibility, reduces menstrual cramps, balances cortisol stress levels, and fosters deep concentration.",
      btnClass: "bg-amber-600 text-white font-bold"
    },
    run: {
      badge: "60 Mins Active Sports / Running (Peak Fitness)",
      badgeClass: "text-emerald-400",
      stamina: "95%", endorphin: "90%", bone: "92%",
      desc: "Aerobic outdoor sports stimulate the brain to release natural mood-elevating neurotransmitters (endorphins and dopamine), while weight-bearing impact triggers osteoblasts to build dense bones.",
      btnClass: "bg-emerald-600 text-white font-bold"
    }
  };

  function setActivity(key) {
    const a = actData[key];
    if (!a) return;

    badge.textContent = a.badge;
    badge.className = `text-[11px] px-2 py-0.5 rounded-full bg-slate-800 ${a.badgeClass} font-bold`;

    staminaBar.style.width = a.stamina;
    endorphinBar.style.width = a.endorphin;
    boneBar.style.width = a.bone;

    actBtns.forEach(b => {
      b.className = 'activity-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs transition';
      if (b.dataset.level === key) {
        b.className = `activity-btn p-2 rounded-xl ${a.btnClass} text-xs transition shadow`;
      }
    });

    if (runner) {
      if (key === 'run') {
        runner.classList.add('animate-bounce');
      } else {
        runner.classList.remove('animate-bounce');
      }
    }

    explanation.innerHTML = `🏃 <span class="font-bold text-amber-300">Physiological Impact:</span> ${a.desc}`;
  }

  actBtns.forEach(btn => {
    btn.addEventListener('click', () => setActivity(btn.dataset.level));
  });

  setActivity('run');
}

// -------------------------------------------------------------
// Sim 11: Digital Safety & Cyberbullying Defense Shield
// -------------------------------------------------------------
function initDigitalSafetySim(c) {
  const badge = c.querySelector('#privacyStatusBadge');
  const bubble = c.querySelector('#bullyMessageBubble');
  const text = c.querySelector('#bullyText');
  const btnThreat = c.querySelector('#btnSimulateCyberThreat');
  const btnShield = c.querySelector('#btnDeploySafetyShield');
  const explanation = c.querySelector('#cyberSafetyExplanation');

  function simulateThreat() {
    badge.textContent = 'Alert: Cyberbullying Threat Detected';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-rose-400 font-bold';

    if (bubble) bubble.classList.remove('hidden');
    if (text) text.textContent = '"Unknown_User: Forwarding personal pictures or rumors to the group!"';

    explanation.innerHTML = `⚠️ <span class="font-bold text-rose-400">Cyber Vulnerability:</span> Cyberbullying includes hurtful comments, sharing fake or private photos without consent, exclusion, and threatening messages online. Never reply with anger or retaliate.`;
  }

  function deployShield() {
    badge.textContent = 'Protected: Cyber Safety Shield Activated';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-emerald-400 font-bold';

    if (bubble) bubble.classList.add('hidden');

    explanation.innerHTML = `🛡️ <span class="font-bold text-emerald-400">The 4-Step Digital Safety Protocol:</span>
    <ol class="list-decimal pl-5 mt-1 space-y-1">
      <li><span class="text-amber-300 font-bold">Do NOT respond:</span> Trolls feed on reactions.</li>
      <li><span class="text-cyan-300 font-bold">Screenshot evidence:</span> Save timestamps and chat history before blocking.</li>
      <li><span class="text-emerald-400 font-bold">Block & report:</span> Use in-app reporting tools to block the offending profile.</li>
      <li><span class="text-purple-300 font-bold">Confide in trusted adults:</span> Tell parents, school counselors, or report to the National Cyber Crime Portal (helpline 1930).</li>
    </ol>`;
  }

  if (btnThreat) btnThreat.addEventListener('click', simulateThreat);
  if (btnShield) btnShield.addEventListener('click', deployShield);

  deployShield();
}

// -------------------------------------------------------------
// Sim 12: Peer Pressure & The 'Say NO!' Assertiveness Tree
// -------------------------------------------------------------
function initSayNoAssertivenessSim(c) {
  const badge = c.querySelector('#assertivenessBadge');
  const bubble = c.querySelector('#responseBubble');
  const text = c.querySelector('#responseText');
  const explanation = c.querySelector('#sayNoExplanation');
  const refuseBtns = c.querySelectorAll('.refuse-btn');
  const empowered = c.querySelector('#empoweredAdolescent');

  const responses = {
    firm_no: {
      badge: "Refusal Tactic: Clear, Direct 'NO'",
      speech: '"No thanks. I have decided not to smoke or vape, and I stand by my choice."',
      color: "bg-emerald-600 text-white font-bold",
      desc: "Direct Refusal: Look directly in the eye and speak in a calm, confident voice. You do not need to make excuses or apologize for protecting your health."
    },
    reason: {
      badge: "Refusal Tactic: Provide a Personal Health Fact",
      speech: '"No, I train for athletics and track. Inhaling toxins destroys lung alveoli."',
      color: "bg-cyan-600 text-white font-bold",
      desc: "Factual Assertion: Citing sports, goals, or medical reality leaves zero room for peer argument, proving maturity and self-respect."
    },
    walk_away: {
      badge: "Refusal Tactic: Exit the Situation Promptly",
      speech: '"I am heading home now. See you in class tomorrow."',
      color: "bg-amber-600 text-white font-bold",
      desc: "Decisive Disengagement: If friends persist in pressurizing you, calmly turn around and walk away to join safe company or trusted adults."
    }
  };

  function applyTactic(key) {
    const r = responses[key];
    if (!r) return;

    badge.textContent = r.badge;
    if (bubble) bubble.classList.remove('hidden');
    if (text) text.textContent = r.speech;

    refuseBtns.forEach(b => {
      b.className = 'refuse-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs transition';
      if (b.dataset.action === key) {
        b.className = `refuse-btn p-2 rounded-xl ${r.color} text-xs transition shadow`;
      }
    });

    explanation.innerHTML = `🛑 <span class="font-bold text-amber-300">Empowerment Principle:</span> ${r.desc}`;
  }

  refuseBtns.forEach(btn => {
    btn.addEventListener('click', () => applyTactic(btn.dataset.action));
  });

  applyTactic('firm_no');
}

// -------------------------------------------------------------
// Sim 13: Substance Abuse Pathology Scanner
// -------------------------------------------------------------
function initBodyDamageScannerSim(c) {
  const badge = c.querySelector('#toxinScanBadge');
  const lungL = c.querySelector('#scanLungLeft');
  const lungR = c.querySelector('#scanLungRight');
  const liver = c.querySelector('#scanLiver');
  const brain = c.querySelector('#scanBrain');

  const title = c.querySelector('#organScanTitle');
  const dmg1 = c.querySelector('#organDmg1');
  const dmg2 = c.querySelector('#organDmg2');
  const dmg3 = c.querySelector('#organDmg3');
  const dmg4 = c.querySelector('#organDmg4');
  const recovery = c.querySelector('#organRecovery');
  const explanation = c.querySelector('#pathologyExplanation');
  const toxinBtns = c.querySelectorAll('.toxin-btn');

  const toxins = {
    tobacco: {
      badge: "Toxin Scanned: Tobacco Smoke & Nicotine",
      title: "Lungs & Respiratory Tract",
      d1: "• 7,000+ chemicals including arsenic & formaldehyde",
      d2: "• Black carcinogenic tar permanently coats alveoli",
      d3: "• Highly addictive nicotine hijacks dopamine pathways",
      d4: "• Chronic bronchitis, asthma attacks & lung cancer",
      rec: "Clean air lifestyle maintains 100% lung expansion!",
      btnClass: "bg-rose-600 text-white font-bold",
      lungFill: "#1e1e24", lungStroke: "#ef4444",
      liverOp: "0.2", brainFill: "#64748b",
      desc: "Tobacco (smoked in bidis, cigarettes, vapes, or chewed as gutkha) damages the delicate cilia in the airways, preventing mucus expulsion and leading to severe chronic pulmonary disease."
    },
    alcohol: {
      badge: "Toxin Scanned: Alcohol (Ethanol)",
      title: "Liver & Central Nervous System",
      d1: "• Toxic acetaldehyde inflames hepatic tissue cells",
      d2: "• Fatty liver progressing to irreversible cirrhosis",
      d3: "• Depresses cerebellum motor control and reflex speed",
      d4: "• Impairs judgment, emotional control, and memory retention",
      rec: "Complete abstinence preserves vibrant liver regeneration!",
      btnClass: "bg-amber-600 text-white font-bold",
      lungFill: "#0f172a", lungStroke: "#475569",
      liverOp: "0.9", brainFill: "#e11d48",
      desc: "Alcohol is a neurotoxin. In developing adolescent brains, it permanently alters neuroplasticity, disrupts memory consolidation, and severely strains liver metabolic enzymes."
    },
    drugs: {
      badge: "Toxin Scanned: Narcotics & Synthetic Drugs",
      title: "Brain Receptors & Cardiovascular System",
      d1: "• Destroys natural dopamine and serotonin equilibrium",
      d2: "• Triggers violent withdrawal symptoms and dependency",
      d3: "• Severe cardiac arrhythmias and elevated stroke risk",
      d4: "• Rapid psychological breakdown, depression, and death",
      rec: "Saying NO preserves mental brilliance and freedom!",
      btnClass: "bg-purple-600 text-white font-bold",
      lungFill: "#0f172a", lungStroke: "#475569",
      liverOp: "0.5", brainFill: "#a855f7",
      desc: "Illegal drugs ruin personal lives, families, and academic futures. Addicts often resort to crime to sustain their habit. A single trial can trigger irreversible dependency."
    }
  };

  function scanToxin(key) {
    const t = toxins[key];
    if (!t) return;

    badge.textContent = t.badge;
    title.textContent = t.title;
    dmg1.textContent = t.d1;
    dmg2.textContent = t.d2;
    dmg3.textContent = t.d3;
    dmg4.textContent = t.d4;
    recovery.textContent = t.rec;

    if (lungL) { lungL.setAttribute('fill', t.lungFill); lungL.setAttribute('stroke', t.lungStroke); }
    if (lungR) { lungR.setAttribute('fill', t.lungFill); lungR.setAttribute('stroke', t.lungStroke); }
    if (liver) liver.setAttribute('class', `opacity-${Math.round(parseFloat(t.liverOp) * 100)} transition-all duration-300`);
    if (brain) brain.setAttribute('fill', t.brainFill);

    toxinBtns.forEach(b => {
      b.className = 'toxin-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs transition';
      if (b.dataset.toxin === key) {
        b.className = `toxin-btn p-2 rounded-xl ${t.btnClass} text-xs transition shadow`;
      }
    });

    explanation.innerHTML = `🩻 <span class="font-bold text-rose-400">Pathology Warning:</span> ${t.desc}`;
  }

  toxinBtns.forEach(btn => {
    btn.addEventListener('click', () => scanToxin(btn.dataset.toxin));
  });

  scanToxin('tobacco');
}

// -------------------------------------------------------------
// Sim 14: Endocrine Switchboard: The Master Pituitary
// -------------------------------------------------------------
function initPituitaryEndocrineSim(c) {
  const dotsContainer = c.querySelector('#circulatingHormoneDots');
  const btnLH = c.querySelector('#btnReleaseLH_FSH');
  const btnGH = c.querySelector('#btnReleaseGH');
  const explanation = c.querySelector('#pituitaryExplanation');

  function pulseGonadotropins() {
    if (dotsContainer) {
      dotsContainer.innerHTML = `
        <circle cx="220" cy="55" r="4" fill="#f59e0b" class="animate-ping"/>
        <circle cx="160" cy="90" r="3" fill="#f59e0b"/>
        <circle cx="280" cy="90" r="3" fill="#f59e0b"/>
        <circle cx="120" cy="130" r="4" fill="#38bdf8"/>
        <circle cx="320" cy="130" r="4" fill="#f43f5e"/>
      `;
    }

    explanation.innerHTML = `⚡ <span class="font-bold text-amber-400">Gonadotropin Pulse (LH & FSH):</span> The master pituitary gland secretes Luteinizing Hormone (LH) and Follicle Stimulating Hormone (FSH) directly into bloodstream capillaries. Traveling through the vascular network without ducts, they bind to receptors in the testes (stimulating testosterone) and ovaries (stimulating estrogen and progesterone).`;
  }

  function pulseGH() {
    if (dotsContainer) {
      dotsContainer.innerHTML = `
        <circle cx="220" cy="55" r="4" fill="#38bdf8" class="animate-ping"/>
        <circle cx="220" cy="95" r="3.5" fill="#38bdf8"/>
        <circle cx="200" cy="140" r="4" fill="#22c55e"/>
        <circle cx="240" cy="140" r="4" fill="#22c55e"/>
      `;
    }

    explanation.innerHTML = `🦴 <span class="font-bold text-cyan-300">Growth Hormone Pulse (GH):</span> Pituitary GH targets chondrocytes at the epiphyseal plates of long bones (arms, legs) and skeletal muscle cells, accelerating protein synthesis, cell division, and height elongation throughout adolescence.`;
  }

  if (btnLH) btnLH.addEventListener('click', pulseGonadotropins);
  if (btnGH) btnGH.addEventListener('click', pulseGH);

  pulseGonadotropins();
}

// -------------------------------------------------------------
// Sim 15: Sex Hormone Biological Feedback Dial
// -------------------------------------------------------------
function initHormoneFeedbackSim(c) {
  const badge = c.querySelector('#feedbackDialBadge');
  const needle = c.querySelector('#dialNeedle');
  const cardTitle = c.querySelector('#respCardTitle');
  const r1 = c.querySelector('#resp1');
  const r2 = c.querySelector('#resp2');
  const r3 = c.querySelector('#resp3');
  const r4 = c.querySelector('#resp4');
  const r5 = c.querySelector('#resp5');
  const btnTesto = c.querySelector('#btnSwitchTestosterone');
  const btnEstro = c.querySelector('#btnSwitchEstrogen');
  const explanation = c.querySelector('#feedbackExplanation');

  function setTestosterone() {
    badge.textContent = 'Feedback Loop: Male Testosterone Axis';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-cyan-400 font-bold';

    btnTesto.className = 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold transition shadow';
    btnEstro.className = 'p-2.5 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold transition';

    if (needle) needle.setAttribute('transform', 'rotate(25, 0, 0)');

    cardTitle.textContent = 'Testosterone Biological Action';
    cardTitle.setAttribute('fill', '#38bdf8');
    r1.textContent = '• Stimulates testicular sperm production (spermatogenesis)';
    r2.textContent = '• Enforces vocal fold lengthening and larynx enlargement';
    r3.textContent = '• Drives facial, chest, and pubic hair follicular patterns';
    r4.textContent = '• Enhances muscle tissue protein synthesis & bone density';
    r5.textContent = '• Negative feedback: High testosterone inhibits pituitary LH release';

    explanation.innerHTML = `🔄 <span class="font-bold text-cyan-400">Negative Feedback Regulation:</span> When circulating testosterone reaches the required physiological threshold, it signals the hypothalamus and pituitary gland to decrease GnRH and LH secretion. This self-regulating biological thermostat prevents hormone over-accumulation!`;
  }

  function setEstrogen() {
    badge.textContent = 'Feedback Loop: Female Estrogen & Progesterone Axis';
    badge.className = 'text-[11px] px-2 py-0.5 rounded-full bg-slate-800 text-rose-400 font-bold';

    btnTesto.className = 'p-2.5 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 font-bold transition';
    btnEstro.className = 'p-2.5 rounded-xl bg-rose-600 text-white font-bold transition shadow';

    if (needle) needle.setAttribute('transform', 'rotate(-25, 0, 0)');

    cardTitle.textContent = 'Estrogen & Progesterone Action';
    cardTitle.setAttribute('fill', '#f43f5e');
    r1.textContent = '• Stimulates cyclic maturation of ovarian ova (eggs)';
    r2.textContent = '• Directs breast development & mammary gland alveolar growth';
    r3.textContent = '• Initiates monthly endometrial thickening & menstruation';
    r4.textContent = '• Directs pelvic bone widening for future childbearing';
    r5.textContent = '• Negative feedback: Regulates cyclic FSH/LH release in 28-day waves';

    explanation.innerHTML = `🔄 <span class="font-bold text-rose-400">Cyclic Hormonal Orchestration:</span> Unlike constant male hormone secretion, female endocrine regulation operates in monthly undulating rhythms. Estrogen and progesterone alternately stimulate and inhibit pituitary gonadotropins to govern ovulation and the menstrual cycle.`;
  }

  if (btnTesto) btnTesto.addEventListener('click', setTestosterone);
  if (btnEstro) btnEstro.addEventListener('click', setEstrogen);

  setTestosterone();
}

// -------------------------------------------------------------
// Sim 16: Ancient Indian Heritage: Kishoravastha & Sapta Dhatus
// -------------------------------------------------------------
function initAyurvedaHeritageSim(c) {
  const btnDin = c.querySelector('#btnDinacharyaRules');
  const btnArtava = c.querySelector('#btnArtavaDignity');
  const explanation = c.querySelector('#ayurvedaExplanation');
  const dhatuBtns = c.querySelectorAll('.dhatu-btn');

  const dhatuData = {
    rasa: { name: "1. Rasa (Nutrient Plasma / Chyle)", desc: "Derived directly from digested Ahara (food). Nourishes every tissue and gives youthful radiance." },
    rakta: { name: "2. Rakta (Oxygenated Blood Tissue)", desc: "Enriches vitality and complexion. During adolescence, blood volume expands rapidly to support muscle mass and menstruation." },
    mamsa: { name: "3. Mamsa (Muscle Tissue)", desc: "Testosterone and growth hormone synthesize lean muscle fibers, giving strength and stability." },
    meda: { name: "4. Meda (Adipose / Fat Tissue)", desc: "Lubricates bodily channels and forms healthy subcutaneous protective contours." },
    asthi: { name: "5. Asthi (Skeletal Bone Tissue)", desc: "Calcium and minerals build peak bone density and elongated stature during pubertal spurts." },
    majja: { name: "6. Majja (Bone Marrow & Nervous Tissue)", desc: "Fills bone cavities, produces blood cells, and enables rapid brain and synaptic communication." },
    shukra: { name: "7. Shukra / Artava (Reproductive Essence)", desc: "The pinnacle seventh tissue signifying biological maturity: sperm in young men and ovum/menstrual artava in young women." }
  };

  function showDhatu(key) {
    const d = dhatuData[key];
    if (!d) return;

    dhatuBtns.forEach(b => {
      b.className = 'dhatu-btn p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs transition';
      if (b.dataset.dhatu === key) {
        b.className = 'dhatu-btn p-2 rounded-xl bg-amber-600 text-white font-bold text-xs transition shadow';
      }
    });

    explanation.innerHTML = `🏛️ <span class="font-bold text-amber-300">${d.name}:</span> ${d.desc}`;
  }

  function showDinacharya() {
    explanation.innerHTML = `🧘 <span class="font-bold text-amber-300">Ayurvedic Dinacharya (Daily Routine for Adolescents):</span>
    <ul class="list-disc pl-5 mt-1 space-y-1">
      <li><span class="text-cyan-300 font-bold">Brahma Muhurta waking:</span> Rising early aligns circadian rhythms with hormonal peak periods.</li>
      <li><span class="text-emerald-400 font-bold">Vyayama (Exercise):</span> Daily physical activity up to half of one's capacity builds stamina without exhaustion.</li>
      <li><span class="text-rose-400 font-bold">Mitahara (Mindful pure diet):</span> Fresh, seasonal, balanced meals without excess spicy, salty, or stale junk foods.</li>
    </ul>`;
  }

  function showArtavaDignity() {
    explanation.innerHTML = `🌸 <span class="font-bold text-rose-400">Artava Pravritti (Menstrual Dignity in Sushruta Samhita):</span>
    Acharya Sushruta treated the onset of menstruation (Artava) as an auspicious, sacred biological sign that the female body has developed optimal reproductive vitality and purification capabilities. Sushruta emphasized physical rest, calm mind, warm nourishing food, and pristine personal hygiene, completely rejecting social stigma and superstition!`;
  }

  dhatuBtns.forEach(btn => {
    btn.addEventListener('click', () => showDhatu(btn.dataset.dhatu));
  });

  if (btnDin) btnDin.addEventListener('click', showDinacharya);
  if (btnArtava) btnArtava.addEventListener('click', showArtavaDignity);

  showDhatu('shukra');
}
'''
