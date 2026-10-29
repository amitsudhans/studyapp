# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Science Chapter 1: The Ever-Evolving World of Science
JavaScript engine: 16 bespoke interactive SVG simulators
"""

JS_CODE = r'''
// Master Simulator Dispatcher for Chapter 1: The Ever-Evolving World of Science
function initSimulatorForSlide(slideId, container) {
  if (!container) return;
  switch (slideId) {
    case 1: initInquiryCycleSim(container); break;
    case 2: initPlaneFlightSim(container); break;
    case 3: initCosmicScaleSim(container); break;
    case 4: initMindsetSorterSim(container); break;
    case 5: initQuestionMilkSim(container); break;
    case 6: initRaindropOpticsSim(container); break;
    case 7: initReactorSim(container); break;
    case 8: initCircuitElectromagnetSim(container); break;
    case 9: initEclipseShadowSim(container); break;
    case 10: initGalileoPendulumSim(container); break;
    case 11: initPhotosynthesisSim(container); break;
    case 12: initEarthSeasonsSim(container); break;
    case 13: initSustainabilityDashboardSim(container); break;
    case 14: initMeniscusParallaxSim(container); break;
    case 15: initIndianPioneersSim(container); break;
    case 16: initYoungScientistConstellationSim(container); break;
  }
}

// -------------------------------------------------------------
// 1. The Scientific Inquiry Cycle Simulator
// -------------------------------------------------------------
function initInquiryCycleSim(container) {
  const svg = container.querySelector('#cycleSvg');
  const badge = container.querySelector('#cycleStepBadge');
  const titleEl = container.querySelector('#cycleStepTitle');
  const descEl = container.querySelector('#cycleStepDesc');
  const btns = container.querySelectorAll('.cycleBtn');
  if (!svg) return;

  const steps = [
    {
      num: 1,
      title: "1. Careful Observation",
      badge: "Step 1: Observation",
      desc: "Observing natural phenomena using our senses and tools without bias. E.g., Alexander Fleming observing clear bacterial death zones around green penicillium mold in a culture dish.",
      color: "#f59e0b"
    },
    {
      num: 2,
      title: "2. Posing Precise Questions",
      badge: "Step 2: Questioning",
      desc: "Transforming curiosity into a focused, investigable question: 'What chemical substance is the mold producing that kills surrounding Staphylococcus bacteria?'",
      color: "#38bdf8"
    },
    {
      num: 3,
      title: "3. Formulating a Hypothesis",
      badge: "Step 3: Hypothesis",
      desc: "Proposing a testable, causal explanation: 'If bacteria are exposed to filtered liquid from penicillium mold broth, then their cell walls will lyse and burst.'",
      color: "#ec4899"
    },
    {
      num: 4,
      title: "4. Controlled Experimentation",
      badge: "Step 4: Experiment",
      desc: "Designing fair tests with controlled variables: comparing bacterial growth in dishes with mold extract (experimental group) vs plain broth (control group).",
      color: "#10b981"
    },
    {
      num: 5,
      title: "5. Data Analysis & Evidence",
      badge: "Step 5: Analysis",
      desc: "Gathering objective measurements, calculating survival rates, and determining whether empirical evidence supports or refutes the hypothesis.",
      color: "#a855f7"
    },
    {
      num: 6,
      title: "6. Conclusion & Refinement",
      badge: "Step 6: Refinement",
      desc: "Drawing valid conclusions, publishing peer-reviewed results (Penicillin discovery), and opening new inquiries: 'Can this antibiotic cure human infections safely?'",
      color: "#06b6d4"
    }
  ];

  let currentStep = 1;

  function render() {
    const s = steps[currentStep - 1];
    if (badge) badge.textContent = s.badge;
    if (titleEl) {
      titleEl.textContent = s.title;
      titleEl.style.color = s.color;
    }
    if (descEl) descEl.textContent = s.desc;

    const cx = 250, cy = 135, r = 85;
    let nodesHtml = '';

    for (let i = 0; i < 6; i++) {
      const angle = (i * 60 - 90) * Math.PI / 180;
      const nx = cx + r * Math.cos(angle);
      const ny = cy + r * Math.sin(angle);
      const isCur = (i + 1) === currentStep;

      // Draw connector arrow
      const nextAngle = ((i + 1) * 60 - 90) * Math.PI / 180;
      const nextX = cx + r * Math.cos(nextAngle);
      const nextY = cy + r * Math.sin(nextAngle);

      nodesHtml += `
        <!-- Flow Arc Line -->
        <line x1="${nx}" y1="${ny}" x2="${nextX}" y2="${nextY}" stroke="#334155" stroke-width="3" stroke-dasharray="3,3" />
        
        <!-- Node Circle -->
        <g style="cursor: pointer;" onclick="document.querySelectorAll('.cycleBtn')[${i}].click()">
          <circle cx="${nx}" cy="${ny}" r="${isCur ? 22 : 16}" fill="${isCur ? s.color : '#1e293b'}" stroke="${isCur ? '#ffffff' : '#475569'}" stroke-width="${isCur ? 3 : 1.5}" />
          <text x="${nx}" y="${ny + 4}" fill="${isCur ? '#ffffff' : '#94a3b8'}" font-size="${isCur ? 12 : 10}" font-weight="bold" text-anchor="middle">${i + 1}</text>
        </g>
      `;
    }

    svg.innerHTML = `
      <!-- Center Emblem -->
      <circle cx="${cx}" cy="${cy}" r="45" fill="#0f172a" stroke="${s.color}" stroke-width="2.5" />
      <text x="${cx}" y="${cy - 8}" fill="${s.color}" font-size="11" font-weight="extrabold" text-anchor="middle">SCIENTIFIC</text>
      <text x="${cx}" y="${cy + 8}" fill="#f8fafc" font-size="12" font-weight="extrabold" text-anchor="middle">METHOD</text>
      <text x="${cx}" y="${cy + 22}" fill="#94a3b8" font-size="9" text-anchor="middle">Cycle of Discovery</text>

      ${nodesHtml}
    `;
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.className = "cycleBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] font-bold transition");
      btn.className = "cycleBtn px-2 py-1.5 rounded-lg bg-amber-600 text-white text-[11px] font-bold transition";
      currentStep = parseInt(btn.dataset.step, 10);
      render();
    });
  });

  render();
}

// -------------------------------------------------------------
// 2. Paper Plane Aerodynamics Simulator
// -------------------------------------------------------------
function initPlaneFlightSim(container) {
  const svg = container.querySelector('#planeSvg');
  const aoaSlider = container.querySelector('#aoaSlider');
  const velSlider = container.querySelector('#velSlider');
  const aoaVal = container.querySelector('#aoaVal');
  const velVal = container.querySelector('#velVal');
  const statusEl = container.querySelector('#flightStatus');
  const liftEl = container.querySelector('#liftReadout');
  const weightEl = container.querySelector('#weightReadout');
  const thrustEl = container.querySelector('#thrustReadout');
  const dragEl = container.querySelector('#dragReadout');
  if (!svg || !aoaSlider || !velSlider) return;

  function render() {
    const alpha = parseFloat(aoaSlider.value); // degrees
    const v = parseFloat(velSlider.value); // m/s
    if (aoaVal) aoaVal.textContent = alpha + '°';
    if (velVal) velVal.textContent = v + ' m/s';

    const weight = 0.50; // constant gravity
    const thrust = (v * 0.07).toFixed(2);

    let lift = 0;
    let drag = 0;
    let statusText = "Level Glide ✔";
    let statusClass = "text-cyan-300 bg-cyan-500/20 border-cyan-500/30";

    if (alpha > 18) {
      // Aerodynamic stall
      lift = Math.max(0.1, (0.015 * v * v * Math.sin((35 - alpha) * Math.PI / 180))).toFixed(2);
      drag = (0.012 * v * v * (1 + Math.sin(alpha * Math.PI / 180) * 1.8)).toFixed(2);
      statusText = "AERODYNAMIC STALL! (Lift Drops) ⚠️";
      statusClass = "text-rose-400 bg-rose-500/20 border-rose-500/30";
    } else {
      lift = (0.014 * v * v * Math.sin((alpha + 8) * Math.PI / 180)).toFixed(2);
      drag = (0.006 * v * v * (1 + Math.sin(alpha * Math.PI / 180))).toFixed(2);

      const diff = lift - weight;
      if (Math.abs(diff) < 0.08) {
        statusText = "Level Stable Glide ✔";
        statusClass = "text-emerald-400 bg-emerald-500/20 border-emerald-500/30";
      } else if (diff > 0.08) {
        statusText = "Climbing Flight ↗";
        statusClass = "text-amber-400 bg-amber-500/20 border-amber-500/30";
      } else {
        statusText = "Descending Glide ↘";
        statusClass = "text-cyan-400 bg-cyan-500/20 border-cyan-500/30";
      }
    }

    if (statusEl) {
      statusEl.textContent = statusText;
      statusEl.className = `px-2 py-0.5 rounded text-[11px] font-mono border font-semibold ${statusClass}`;
    }

    if (liftEl) liftEl.textContent = `Lift: ${lift} N`;
    if (weightEl) weightEl.textContent = `Weight: ${weight} N`;
    if (thrustEl) thrustEl.textContent = `Thrust: ${thrust} N`;
    if (dragEl) dragEl.textContent = `Drag: ${drag} N`;

    const cx = 250, cy = 135;
    const rad = (-alpha * Math.PI) / 180;

    // Vector arrow lengths
    const liftLen = Math.min(65, lift * 90);
    const weightLen = 45;
    const thrustLen = Math.min(65, thrust * 110);
    const dragLen = Math.min(65, drag * 100);

    svg.innerHTML = `
      <!-- Sky Background Grid -->
      <defs>
        <pattern id="skyGrid" width="25" height="25" patternUnits="userSpaceOnUse">
          <path d="M 25 0 L 0 0 0 25" fill="none" stroke="#1e293b" stroke-width="0.8" />
        </pattern>
        <marker id="arrowLift" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <polygon points="0 0, 6 3, 0 6" fill="#10b981" />
        </marker>
        <marker id="arrowWeight" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <polygon points="0 0, 6 3, 0 6" fill="#f59e0b" />
        </marker>
        <marker id="arrowThrust" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <polygon points="0 0, 6 3, 0 6" fill="#38bdf8" />
        </marker>
        <marker id="arrowDrag" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <polygon points="0 0, 6 3, 0 6" fill="#f43f5e" />
        </marker>
      </defs>
      
      <rect width="500" height="260" fill="url(#skyGrid)" />

      <!-- Relative Airflow Streamlines -->
      <path d="M 30 ${cy - 40} Q 180 ${cy - 40} 240 ${cy - 50} T 470 ${cy - 45}" stroke="#475569" stroke-width="1.5" stroke-dasharray="4,4" fill="none" opacity="0.6" />
      <path d="M 30 ${cy} Q 180 ${cy} 240 ${cy + 10} T 470 ${cy + 20}" stroke="#475569" stroke-width="1.5" stroke-dasharray="4,4" fill="none" opacity="0.6" />
      <path d="M 30 ${cy + 40} Q 180 ${cy + 40} 240 ${cy + 55} T 470 ${cy + 65}" stroke="#475569" stroke-width="1.5" stroke-dasharray="4,4" fill="none" opacity="0.6" />

      <!-- Paper Plane Group (Rotated by Angle of Attack) -->
      <g transform="translate(${cx}, ${cy}) rotate(${-alpha})">
        <!-- Folded Paper Plane Geometry -->
        <polygon points="70,0 -50,-24 -30,0" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" />
        <polygon points="70,0 -50,24 -30,0" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.5" />
        <polygon points="70,0 -30,0 -60,0" stroke="#64748b" stroke-width="2" />
        <!-- Cockpit Center Dot -->
        <circle cx="0" cy="0" r="4" fill="#38bdf8" />
      </g>

      <!-- Center of Mass Force Vectors -->
      <!-- Upward Lift -->
      <line x1="${cx}" y1="${cy}" x2="${cx}" y2="${cy - liftLen}" stroke="#10b981" stroke-width="3" marker-end="url(#arrowLift)" />
      <text x="${cx + 8}" y="${cy - liftLen + 10}" fill="#10b981" font-size="11" font-weight="bold">Lift (${lift}N)</text>

      <!-- Downward Weight -->
      <line x1="${cx}" y1="${cy}" x2="${cx}" y2="${cy + weightLen}" stroke="#f59e0b" stroke-width="3" marker-end="url(#arrowWeight)" />
      <text x="${cx + 8}" y="${cy + weightLen - 5}" fill="#f59e0b" font-size="11" font-weight="bold">Gravity (${weight}N)</text>

      <!-- Forward Thrust -->
      <line x1="${cx}" y1="${cy}" x2="${cx + thrustLen}" y2="${cy}" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrowThrust)" />
      <text x="${cx + thrustLen - 30}" y="${cy - 8}" fill="#38bdf8" font-size="11" font-weight="bold">Thrust</text>

      <!-- Backward Drag -->
      <line x1="${cx}" y1="${cy}" x2="${cx - dragLen}" y2="${cy}" stroke="#f43f5e" stroke-width="3" marker-end="url(#arrowDrag)" />
      <text x="${cx - dragLen - 32}" y="${cy - 8}" fill="#f43f5e" font-size="11" font-weight="bold">Drag</text>
    `;
  }

  aoaSlider.addEventListener('input', render);
  velSlider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 3. Cosmic Zoom Scale Simulator (Powers of 10)
// -------------------------------------------------------------
function initCosmicScaleSim(container) {
  const svg = container.querySelector('#scaleSvg');
  const slider = container.querySelector('#scaleSlider');
  const orderEl = container.querySelector('#scaleOrder');
  const dimEl = container.querySelector('#scaleDimension');
  const descEl = container.querySelector('#scaleDescription');
  if (!svg || !slider) return;

  const scales = [
    {
      order: "10^-10 m (Subatomic)",
      name: "Hydrogen Atom & Nucleus",
      desc: "An electron cloud surrounds a single proton. Atoms are the building blocks of all chemical elements.",
      color: "#ec4899",
      draw: (svg) => {
        svg.innerHTML = `
          <circle cx="250" cy="130" r="6" fill="#f43f5e" />
          <circle cx="250" cy="130" r="60" fill="none" stroke="#38bdf8" stroke-dasharray="3,3" stroke-width="1.5" />
          <circle cx="190" cy="130" r="4" fill="#38bdf8" />
          <text x="250" y="50" fill="#f43f5e" font-size="12" font-weight="bold" text-anchor="middle">Proton (+e)</text>
          <text x="250" y="215" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Orbiting Electron (-e) • Diameter: 0.1 nm (1 Å)</text>
        `;
      }
    },
    {
      order: "10^-9 m (Nanoscale)",
      name: "DNA Double Helix",
      desc: "The genetic instruction manual of living organisms. The double helix width measures exactly 2 nanometers.",
      color: "#a855f7",
      draw: (svg) => {
        let helix = '<path d="';
        for (let x = 70; x <= 430; x += 10) {
          const y1 = 130 + 40 * Math.sin(x * 0.05);
          helix += `${x === 70 ? 'M' : 'L'} ${x} ${y1} `;
        }
        helix += '" fill="none" stroke="#a855f7" stroke-width="3" />';
        let helix2 = '<path d="';
        for (let x = 70; x <= 430; x += 10) {
          const y2 = 130 - 40 * Math.sin(x * 0.05);
          helix2 += `${x === 70 ? 'M' : 'L'} ${x} ${y2} `;
        }
        helix2 += '" fill="none" stroke="#38bdf8" stroke-width="3" />';
        svg.innerHTML = `
          ${helix}
          ${helix2}
          <text x="250" y="45" fill="#c084fc" font-size="12" font-weight="bold" text-anchor="middle">DNA Macromolecule (Width ≈ 2 nm)</text>
          <text x="250" y="225" fill="#94a3b8" font-size="11" text-anchor="middle">Nucleotide base pairs (Adenine, Thymine, Guanine, Cytosine)</text>
        `;
      }
    },
    {
      order: "10^-6 m (Microscale)",
      name: "Plant Cell & Chloroplasts (~50 µm)",
      desc: "Microscopic biological factory: cell wall, central vacuole, and green chloroplasts synthesizing sugars via sunlight.",
      color: "#10b981",
      draw: (svg) => {
        svg.innerHTML = `
          <!-- Cell Wall -->
          <polygon points="120,60 380,60 410,200 90,200" fill="#064e3b" stroke="#10b981" stroke-width="3" />
          <!-- Vacuole -->
          <ellipse cx="250" cy="130" rx="90" ry="45" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" />
          <!-- Chloroplasts -->
          <circle cx="160" cy="100" r="14" fill="#22c55e" />
          <circle cx="340" cy="110" r="14" fill="#22c55e" />
          <circle cx="180" cy="165" r="14" fill="#22c55e" />
          <circle cx="320" cy="165" r="14" fill="#22c55e" />
          <text x="250" y="45" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Plant Cell Structure (50 µm)</text>
          <text x="250" y="235" fill="#94a3b8" font-size="11" text-anchor="middle">Cellulose wall with photosynthetic chloroplast organelles</text>
        `;
      }
    },
    {
      order: "10^-3 m (Millimeter)",
      name: "Water Droplet & Tiny Ant (~2 mm)",
      desc: "Surface tension holds a rain droplet into a spherical dome; tiny insects walk across using hydrophobic leg hairs.",
      color: "#38bdf8",
      draw: (svg) => {
        svg.innerHTML = `
          <!-- Leaf Surface -->
          <path d="M 60 170 Q 250 185 440 170" stroke="#15803d" stroke-width="6" fill="none" />
          <!-- Water Droplet -->
          <ellipse cx="250" cy="160" rx="45" ry="32" fill="#0284c7" fill-opacity="0.5" stroke="#38bdf8" stroke-width="2" />
          <circle cx="235" cy="150" r="6" fill="#ffffff" opacity="0.6" />
          <text x="250" y="55" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Spherical Water Droplet (2 mm)</text>
          <text x="250" y="225" fill="#94a3b8" font-size="11" text-anchor="middle">Cohesion and surface tension minimize exposed surface area</text>
        `;
      }
    },
    {
      order: "10^0 m (Human Scale)",
      name: "Human & School Desk (1 to 2 m)",
      desc: "The familiar macroscopic realm of everyday experience, paper planes, bicycles, and laboratory glassware.",
      color: "#f59e0b",
      draw: (svg) => {
        svg.innerHTML = `
          <!-- Student figure -->
          <circle cx="210" cy="95" r="16" fill="#fde68a" />
          <line x1="210" y1="111" x2="210" y2="170" stroke="#38bdf8" stroke-width="4" />
          <!-- Arm holding paper plane -->
          <line x1="210" y1="125" x2="250" y2="105" stroke="#fde68a" stroke-width="3" />
          <polygon points="265,100 245,95 250,105" fill="#ffffff" />
          <!-- Desk -->
          <rect x="270" y="140" width="120" height="10" fill="#78350f" />
          <line x1="285" y1="150" x2="285" y2="200" stroke="#451a03" stroke-width="4" />
          <line x1="375" y1="150" x2="375" y2="200" stroke="#451a03" stroke-width="4" />
          <text x="250" y="50" fill="#fde68a" font-size="13" font-weight="bold" text-anchor="middle">Human Laboratory Scale (1.5 m)</text>
          <text x="250" y="235" fill="#94a3b8" font-size="11" text-anchor="middle">The domain of direct human sensory observation</text>
        `;
      }
    },
    {
      order: "10^7 m (Planetary Scale)",
      name: "Planet Earth (Diameter: 12,742 km)",
      desc: "Our celestial oasis: a protective nitrogen-oxygen atmosphere, vast liquid water oceans, and a dynamic biosphere.",
      color: "#0284c7",
      draw: (svg) => {
        svg.innerHTML = `
          <!-- Earth Globe -->
          <circle cx="250" cy="130" r="70" fill="#0284c7" stroke="#38bdf8" stroke-width="2" />
          <!-- Continents -->
          <path d="M 220 100 Q 240 85 260 100 Q 270 120 250 140 Q 230 130 220 100 Z" fill="#15803d" />
          <path d="M 270 110 Q 295 125 285 145 Q 265 150 270 110 Z" fill="#15803d" />
          <!-- Atmospheric Halo -->
          <circle cx="250" cy="130" r="75" fill="none" stroke="#67e8f9" stroke-width="1.5" opacity="0.6" />
          <text x="250" y="45" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Planet Earth (1.27 × 10^7 m)</text>
          <text x="250" y="235" fill="#94a3b8" font-size="11" text-anchor="middle">Home to all known life in the universe</text>
        `;
      }
    },
    {
      order: "10^21 m (Galactic Scale)",
      name: "The Milky Way Galaxy (~100,000 Light-Years)",
      desc: "A barred spiral galaxy containing over 200 billion stars, orbiting around a supermassive central black hole.",
      color: "#818cf8",
      draw: (svg) => {
        svg.innerHTML = `
          <!-- Galaxy Spiral -->
          <ellipse cx="250" cy="130" rx="140" ry="45" fill="#1e1b4b" opacity="0.4" />
          <ellipse cx="250" cy="130" rx="90" ry="25" fill="#312e81" opacity="0.6" />
          <circle cx="250" cy="130" r="16" fill="#fef08a" />
          <!-- Solar system pointer -->
          <circle cx="310" cy="125" r="3" fill="#f43f5e" />
          <line x1="310" y1="125" x2="350" y2="85" stroke="#f43f5e" stroke-width="1.5" />
          <text x="355" y="85" fill="#f43f5e" font-size="10" font-weight="bold">Our Sun</text>
          <text x="250" y="40" fill="#a5b4fc" font-size="13" font-weight="bold" text-anchor="middle">Milky Way Galaxy (10^21 m)</text>
          <text x="250" y="235" fill="#94a3b8" font-size="11" text-anchor="middle">Diameter: ~100,000 light-years (9.5 × 10^20 m)</text>
        `;
      }
    }
  ];

  function render() {
    const idx = parseInt(slider.value, 10);
    const item = scales[idx];
    if (orderEl) orderEl.textContent = item.order;
    if (dimEl) dimEl.textContent = item.name;
    if (descEl) descEl.textContent = item.desc;
    item.draw(svg);
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 4. Scientific Mindset Sorter Simulator
// -------------------------------------------------------------
function initMindsetSorterSim(container) {
  const statementEl = container.querySelector('#mindsetStatement');
  const feedbackEl = container.querySelector('#mindsetFeedback');
  const nextBtn = container.querySelector('#nextStatementBtn');
  const choiceBtns = container.querySelectorAll('.mindsetChoiceBtn');
  if (!statementEl || !feedbackEl) return;

  const dataset = [
    {
      text: '"Water freezes into ice at 0°C under standard atmospheric pressure."',
      correct: "fact",
      feedback: "Correct! This is a verifiable Scientific Fact confirmed by reproducible thermometric measurements worldwide."
    },
    {
      text: '"Chocolate ice cream is the absolute most delicious dessert on Earth."',
      correct: "opinion",
      feedback: "Spot On! Taste preference is a Subjective Opinion based on personal neural sensation, not an empirical universal measurement."
    },
    {
      text: '"Green bean seeds will germinate faster under blue light than under red light."',
      correct: "hypothesis",
      feedback: "Precisely! This is a Testable Hypothesis proposing a causal link between light wavelength and germination speed."
    },
    {
      text: '"Planet Earth completes one full orbit around the Sun in approximately 365.25 days."',
      correct: "fact",
      feedback: "Correct! This is an astronomical Scientific Fact established by observational orbital mechanics."
    },
    {
      text: '"Spiders are terrifying creatures that should be removed from all houses."',
      correct: "opinion",
      feedback: "Correct! Fear and aesthetic dislike are Subjective Opinions. Ecologically, spiders are beneficial insect predators."
    },
    {
      text: '"Adding dissolved sodium chloride to water will elevate its boiling point above 100°C."',
      correct: "hypothesis",
      feedback: "Spot on! This is a Testable Hypothesis (collivative properties) that can be verified with a beaker, salt, and thermometer."
    }
  ];

  let currentIdx = 0;

  function loadStatement() {
    const d = dataset[currentIdx];
    statementEl.textContent = d.text;
    feedbackEl.textContent = "Click a button above to evaluate whether this statement is a Fact, Opinion, or Hypothesis.";
    feedbackEl.className = "p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 leading-snug";
  }

  choiceBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const chosen = btn.dataset.type;
      const d = dataset[currentIdx];
      if (chosen === d.correct) {
        feedbackEl.className = "p-2.5 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-xs text-emerald-300 leading-snug";
        feedbackEl.innerHTML = `<strong>Spot On! ✔</strong> ${d.feedback}`;
      } else {
        feedbackEl.className = "p-2.5 rounded-xl bg-rose-950/60 border border-rose-500/40 text-xs text-rose-300 leading-snug";
        feedbackEl.innerHTML = `<strong>Incorrect.</strong> This statement is actually a <strong>${d.correct.toUpperCase()}</strong>: ${d.feedback}`;
      }
    });
  });

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      currentIdx = (currentIdx + 1) % dataset.length;
      loadStatement();
    });
  }

  loadStatement();
}

// -------------------------------------------------------------
// 5. Question the Answer (Milk Edition)
// -------------------------------------------------------------
function initQuestionMilkSim(container) {
  const svg = container.querySelector('#milkSvg');
  const expEl = container.querySelector('#milkExplanation');
  const btns = container.querySelectorAll('.milkModeBtn');
  if (!svg) return;

  function renderMode(mode) {
    if (mode === 'capsaicin') {
      svg.innerHTML = `
        <!-- Tongue Nerve Receptor -->
        <rect x="50" y="160" width="400" height="40" rx="10" fill="#be123c" />
        <text x="250" y="185" fill="#fecdd3" font-size="12" font-weight="bold" text-anchor="middle">Sensory Nerve Membrane (Pain Receptor TRPV1)</text>

        <!-- Capsaicin molecules -->
        <circle cx="150" cy="140" r="12" fill="#ef4444" stroke="#fca5a5" stroke-width="2" />
        <text x="150" y="144" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Spice</text>

        <!-- Casein Micelle Engulfing Capsaicin -->
        <circle cx="280" cy="110" r="28" fill="#f8fafc" stroke="#38bdf8" stroke-width="2.5" />
        <circle cx="280" cy="110" r="10" fill="#ef4444" />
        <text x="280" y="90" fill="#0284c7" font-size="10" font-weight="extrabold" text-anchor="middle">Casein Micelle</text>
        <text x="280" y="150" fill="#38bdf8" font-size="10" text-anchor="middle">(Traps Capsaicin)</text>

        <!-- Wash away arrow -->
        <path d="M 320 110 L 420 110" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrowLift)" />
        <text x="370" y="100" fill="#38bdf8" font-size="11" font-weight="bold">Washed Away!</text>
      `;
      expEl.innerHTML = `<strong>Question:</strong> <em>Why does milk instantly soothe chili spice while water does nothing?</em><br>Chili heat comes from oily capsaicin. Water cannot dissolve non-polar oil, but casein protein in milk acts like a detergent, engulfing capsaicin and pulling it away from pain receptors!`;
    } else if (mode === 'tyndall') {
      svg.innerHTML = `
        <!-- Laser pointer -->
        <rect x="40" y="110" width="50" height="20" rx="4" fill="#475569" />
        <polygon points="90,120 100,115 100,125" fill="#ef4444" />
        
        <!-- Glass of water with milk drops -->
        <rect x="150" y="60" width="160" height="130" rx="8" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2" />
        
        <!-- Tyndall Scattering Cone -->
        <polygon points="150,120 310,105 310,135" fill="#f43f5e" fill-opacity="0.5" />
        <line x1="90" y1="120" x2="440" y2="120" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2" />

        <!-- Suspended fat droplets -->
        <circle cx="180" cy="100" r="3" fill="#ffffff" />
        <circle cx="230" cy="140" r="3" fill="#ffffff" />
        <circle cx="270" cy="115" r="3" fill="#ffffff" />

        <text x="230" y="50" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Colloid: Tyndall Beam Visible</text>
        <text x="230" y="215" fill="#fca5a5" font-size="11" text-anchor="middle">Sub-micron fat globules scatter red laser photons!</text>
      `;
      expEl.innerHTML = `<strong>Question:</strong> <em>How can you make an invisible light beam clearly visible through water?</em><br>Adding a drop of milk creates a colloid emulsion. Suspended microscopic fat droplets scatter light (Tyndall Effect), revealing the beam's geometric path!`;
    } else {
      svg.innerHTML = `
        <!-- Beaker with warm milk -->
        <rect x="160" y="70" width="180" height="120" rx="10" fill="#f8fafc" stroke="#94a3b8" stroke-width="2.5" />
        <!-- Curdled protein mesh -->
        <path d="M 180 120 Q 200 140 230 120 T 280 130 T 320 110" stroke="#f59e0b" stroke-width="3" fill="none" />
        <path d="M 180 150 Q 210 130 250 160 T 310 140" stroke="#f59e0b" stroke-width="3" fill="none" />
        <!-- Bacteria -->
        <ellipse cx="210" cy="100" rx="8" ry="4" fill="#10b981" />
        <ellipse cx="270" cy="105" rx="8" ry="4" fill="#10b981" />
        <text x="250" y="50" fill="#fde68a" font-size="12" font-weight="bold" text-anchor="middle">Lactobacillus Fermentation</text>
        <text x="250" y="215" fill="#34d399" font-size="11" text-anchor="middle">Lactose converted to lactic acid; pH drops, coagulating milk into curd</text>
      `;
      expEl.innerHTML = `<strong>Question:</strong> <em>How do we cultivate millions of friendly bacteria to make probiotic breakfast food?</em><br>Adding a spoonful of starter curd to warm milk inoculates it with <em>Lactobacillus</em>. The bacteria ferment lactose into lactic acid, causing casein proteins to coagulate into solid curd!`;
    }
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.className = "milkModeBtn px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold transition");
      btn.className = "milkModeBtn px-2.5 py-1.5 rounded-lg bg-amber-600 text-white text-xs font-bold transition";
      renderMode(btn.dataset.mode);
    });
  });

  renderMode('capsaicin');
}

// -------------------------------------------------------------
// 6. Raindrop Optics & 42° Rainbow Angle Simulator
// -------------------------------------------------------------
function initRaindropOpticsSim(container) {
  const svg = container.querySelector('#raindropSvg');
  const slider = container.querySelector('#impactSlider');
  const impactVal = container.querySelector('#impactVal');
  const angleReadout = container.querySelector('#rainbowAngleReadout');
  if (!svg || !slider) return;

  function render() {
    const hRel = parseFloat(slider.value); // 0.1 to 0.95
    if (impactVal) {
      impactVal.textContent = hRel.toFixed(2) + (Math.abs(hRel - 0.86) < 0.03 ? " (Caustic Focus!)" : "");
    }

    const cx = 250, cy = 125, R = 75;
    const h = hRel * R;

    // Entry point on sphere
    const i = Math.asin(hRel); // radians
    const n = 1.333; // refractive index of water
    const r = Math.asin(Math.sin(i) / n); // refracted angle

    // Total deflection angle for 1 internal reflection: theta = 4r - 2i
    const thetaRad = 4 * r - 2 * i;
    const exitAngleDeg = (thetaRad * 180 / Math.PI).toFixed(1);

    if (angleReadout) {
      angleReadout.textContent = `Exit Angle: ${exitAngleDeg}°`;
      angleReadout.className = Math.abs(parseFloat(exitAngleDeg) - 42.0) < 1.0 ?
        "px-2 py-0.5 rounded text-[11px] font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 font-bold" :
        "px-2 py-0.5 rounded text-[11px] font-mono bg-slate-800 text-slate-400 font-semibold";
    }

    // Coordinates on circle
    const x1 = cx - Math.sqrt(R * R - h * h);
    const y1 = cy - h;

    // Rear reflection point: angle from horizontal is (i - 2r)
    const phi = Math.PI - 2 * r + i;
    const x2 = cx + R * Math.cos(phi - Math.PI);
    const y2 = cy + R * Math.sin(phi - Math.PI);

    // Exit point: angle phi2
    const phi2 = phi - 2 * r;
    const x3 = cx + R * Math.cos(phi2 - Math.PI);
    const y3 = cy + R * Math.sin(phi2 - Math.PI);

    // Exit ray direction
    const exitDir = Math.PI - thetaRad;
    const x4 = x3 - 120 * Math.cos(exitDir);
    const y4 = y3 + 120 * Math.sin(exitDir);

    svg.innerHTML = `
      <!-- Raindrop Water Sphere -->
      <circle cx="${cx}" cy="${cy}" r="${R}" fill="#0284c7" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2.5" />
      
      <!-- Incident White Solar Ray -->
      <line x1="30" y1="${y1}" x2="${x1}" y2="${y1}" stroke="#ffffff" stroke-width="2.5" />
      <text x="60" y="${y1 - 8}" fill="#f8fafc" font-size="11" font-weight="bold">Incoming Sunlight</text>

      <!-- Inside Droplet Ray 1: Refraction -->
      <line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#f43f5e" stroke-width="2.5" />

      <!-- Inside Droplet Ray 2: Internal Reflection -->
      <line x1="${x2}" y1="${y2}" x2="${x3}" y2="${y3}" stroke="#f43f5e" stroke-width="2.5" />

      <!-- Emerging Refracted Ray (Red light caustic) -->
      <line x1="${x3}" y1="${y3}" x2="${x4}" y2="${y4}" stroke="#ef4444" stroke-width="3" />
      
      <!-- Violet Ray Offset (Dispersion) -->
      <line x1="${x3}" y1="${y3}" x2="${x4 - 10}" y2="${y4 - 8}" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="2,2" />

      <!-- Angle Measurement Arc -->
      <text x="${x4 - 15}" y="${y4 + 15}" fill="#ef4444" font-size="13" font-weight="extrabold">Red: ${exitAngleDeg}°</text>
      <text x="${x4 - 15}" y="${y4 + 30}" fill="#a78bfa" font-size="10">Violet: ~40.4°</text>

      <text x="250" y="30" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Spherical Raindrop Cross-Section (n = 1.33)</text>
    `;
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 7. Physical vs Chemical Reactor Simulator
// -------------------------------------------------------------
function initReactorSim(container) {
  const svg = container.querySelector('#reactorSvg');
  const badge = container.querySelector('#reactionBadge');
  const desc = container.querySelector('#reactionDesc');
  const btns = container.querySelectorAll('.reactBtn');
  if (!svg) return;

  function setReaction(type) {
    if (type === 'ice') {
      badge.textContent = "Physical Change (Reversible)";
      badge.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-blue-500/20 text-blue-300 border border-blue-500/30 font-semibold";
      desc.innerHTML = "<strong>Melting Ice:</strong> Solid ice turns into liquid water. The molecules remain strictly $\\text{H}_2\\text{O}$; only intermolecular spacing changes. Easily reversible by freezing!";
      svg.innerHTML = `
        <!-- Melting Ice Beaker -->
        <rect x="180" y="70" width="140" height="120" rx="8" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2" />
        <rect x="180" y="140" width="140" height="50" rx="4" fill="#0284c7" fill-opacity="0.5" />
        <!-- Ice cubes -->
        <rect x="200" y="120" width="30" height="30" rx="4" fill="#e0f2fe" stroke="#38bdf8" />
        <rect x="250" y="125" width="28" height="28" rx="4" fill="#e0f2fe" stroke="#38bdf8" />
        <text x="250" y="45" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">H2O(s) ➔ H2O(l) (State Change Only)</text>
        <text x="250" y="215" fill="#94a3b8" font-size="11" text-anchor="middle">Zero new molecules formed; reversible upon cooling</text>
      `;
    } else if (type === 'sugar') {
      badge.textContent = "Physical Change (Solution)";
      badge.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 font-semibold";
      desc.innerHTML = "<strong>Dissolving Sugar:</strong> Sucrose crystals disperse between water molecules. No chemical bonds break; evaporating water recovers 100% of the solid sugar crystals.";
      svg.innerHTML = `
        <rect x="180" y="70" width="140" height="120" rx="8" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2" />
        <rect x="180" y="110" width="140" height="80" rx="4" fill="#0284c7" fill-opacity="0.4" />
        <!-- Dispersed sugar dots -->
        <circle cx="210" cy="130" r="3" fill="#ffffff" />
        <circle cx="240" cy="160" r="3" fill="#ffffff" />
        <circle cx="270" cy="135" r="3" fill="#ffffff" />
        <circle cx="290" cy="170" r="3" fill="#ffffff" />
        <text x="250" y="45" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Solvation: Sugar Crystals Dispersing</text>
        <text x="250" y="215" fill="#94a3b8" font-size="11" text-anchor="middle">Reversible via boiling/evaporation</text>
      `;
    } else if (type === 'vinegar') {
      badge.textContent = "Chemical Change (Irreversible)";
      badge.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold";
      desc.innerHTML = "<strong>Vinegar + Baking Soda:</strong> Vigorous effervescence! Produces bubbling carbon dioxide gas ($\\text{CO}_2$), water, and sodium acetate. New chemical bonds formed.";
      svg.innerHTML = `
        <rect x="180" y="70" width="140" height="120" rx="8" fill="#be123c" fill-opacity="0.2" stroke="#f43f5e" stroke-width="2" />
        <rect x="180" y="120" width="140" height="70" rx="4" fill="#be123c" fill-opacity="0.4" />
        <!-- Rising CO2 bubbles -->
        <circle cx="210" cy="140" r="5" fill="#ffffff" opacity="0.8" />
        <circle cx="240" cy="100" r="7" fill="#ffffff" opacity="0.9" />
        <circle cx="270" cy="120" r="6" fill="#ffffff" opacity="0.8" />
        <circle cx="250" cy="80" r="8" fill="#ffffff" opacity="0.9" />
        <text x="250" y="45" fill="#f43f5e" font-size="12" font-weight="bold" text-anchor="middle">Effervescence: CO2 Gas Escaping!</text>
        <text x="250" y="215" fill="#fca5a5" font-size="11" text-anchor="middle">CH3COOH + NaHCO3 ➔ CH3COONa + H2O + CO2 ↑</text>
      `;
    } else {
      badge.textContent = "Chemical Change (Oxidation)";
      badge.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-amber-500/20 text-amber-300 border border-amber-500/30 font-semibold";
      desc.innerHTML = "<strong>Iron Rusting:</strong> Iron combines with atmospheric oxygen and water to form hydrated iron(III) oxide (rust). Irreversible change destroying metal strength.";
      svg.innerHTML = `
        <!-- Iron Nail with Rust Coating -->
        <polygon points="120,120 380,120 400,125 380,130 120,130" fill="#78350f" stroke="#b45309" stroke-width="2" />
        <rect x="110" y="112" width="15" height="26" rx="2" fill="#94a3b8" />
        <!-- Rust patches -->
        <circle cx="200" cy="123" r="6" fill="#ea580c" />
        <circle cx="260" cy="127" r="7" fill="#c2410c" />
        <circle cx="320" cy="124" r="5" fill="#ea580c" />
        <text x="250" y="55" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">Iron Oxidation: Rusting (Fe2O3 · xH2O)</text>
        <text x="250" y="195" fill="#fdba74" font-size="11" text-anchor="middle">4Fe + 3O2 + 2xH2O ➔ 2Fe2O3 · xH2O</text>
      `;
    }
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.className = "reactBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition");
      btn.className = "reactBtn px-2 py-1.5 rounded-lg bg-rose-600 text-white font-bold transition";
      setReaction(btn.dataset.reaction);
    });
  });

  setReaction('vinegar');
}

// -------------------------------------------------------------
// 8. DC Circuit & Electromagnet Simulator
// -------------------------------------------------------------
function initCircuitElectromagnetSim(container) {
  const svg = container.querySelector('#circuitSvg');
  const statusEl = container.querySelector('#circuitStatus');
  const btn = container.querySelector('#toggleSwitchBtn');
  const compassEl = container.querySelector('#compassReading');
  if (!svg || !btn) return;

  let isClosed = true;

  function render() {
    if (statusEl) {
      statusEl.textContent = isClosed ? "Circuit: CLOSED (ON)" : "Circuit: OPEN (OFF)";
      statusEl.className = isClosed ?
        "px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold" :
        "px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold";
    }

    if (compassEl) {
      compassEl.textContent = isClosed ? "Compass Deflection: 45° E (Field Active)" : "Compass: 0° N (Earth Field Only)";
    }

    const wireColor = isClosed ? "#eab308" : "#475569";
    const bulbGlow = isClosed ? "#fde047" : "#334155";
    const needleAngle = isClosed ? 45 : 0;

    svg.innerHTML = `
      <!-- Circuit Wires -->
      <path d="M 100 70 L 400 70 L 400 180 L 100 180 Z" fill="none" stroke="${wireColor}" stroke-width="4" stroke-linejoin="round" />

      <!-- DC Battery Cell -->
      <rect x="80" y="110" width="40" height="30" rx="4" fill="#1e293b" stroke="#64748b" />
      <line x1="85" y1="125" x2="115" y2="125" stroke="#38bdf8" stroke-width="3" />
      <text x="75" y="105" fill="#f8fafc" font-size="10" font-weight="bold">+ 1.5V -</text>

      <!-- Light Bulb -->
      <circle cx="250" cy="70" r="16" fill="${bulbGlow}" stroke="#cbd5e1" stroke-width="2" />
      <path d="M 245 74 Q 250 63 255 74" stroke="#e2e8f0" stroke-width="1.5" fill="none" />
      <text x="250" y="45" fill="${isClosed ? '#fef08a' : '#94a3b8'}" font-size="11" font-weight="bold" text-anchor="middle">
        ${isClosed ? 'Bulb GLOWING 💡' : 'Bulb OFF'}
      </text>

      <!-- Knife Switch -->
      <g transform="translate(180, 180)">
        <circle cx="0" cy="0" r="4" fill="#94a3b8" />
        <circle cx="35" cy="0" r="4" fill="#94a3b8" />
        <line x1="0" y1="0" x2="${isClosed ? 35 : 25}" y2="${isClosed ? 0 : -20}" stroke="#f59e0b" stroke-width="3.5" />
        <text x="17" y="20" fill="#94a3b8" font-size="10" text-anchor="middle">${isClosed ? 'Switch ON' : 'Switch OFF'}</text>
      </g>

      <!-- Iron Nail with Solenoid Coil -->
      <g transform="translate(360, 125)">
        <rect x="-6" y="-30" width="12" height="60" rx="3" fill="#64748b" stroke="#94a3b8" />
        <!-- Coiled turns -->
        <line x1="-12" y1="-20" x2="12" y2="-15" stroke="${wireColor}" stroke-width="2.5" />
        <line x1="-12" y1="-5" x2="12" y2="0" stroke="${wireColor}" stroke-width="2.5" />
        <line x1="-12" y1="10" x2="12" y2="15" stroke="${wireColor}" stroke-width="2.5" />
        <text x="22" y="5" fill="#38bdf8" font-size="10" font-weight="bold">Electromagnet</text>
      </g>

      <!-- Magnetic Compass Needle -->
      <g transform="translate(440, 125)">
        <circle cx="0" cy="0" r="22" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5" />
        <text x="0" y="-12" fill="#94a3b8" font-size="8" text-anchor="middle">N</text>
        <g transform="rotate(${needleAngle})">
          <polygon points="0,-18 -4,0 4,0" fill="#ef4444" />
          <polygon points="0,18 -4,0 4,0" fill="#38bdf8" />
          <circle cx="0" cy="0" r="2.5" fill="#ffffff" />
        </g>
      </g>
    `;
  }

  btn.addEventListener('click', () => {
    isClosed = !isClosed;
    render();
  });

  render();
}

// -------------------------------------------------------------
// 9. Light, Shadows & Eclipse Simulator
// -------------------------------------------------------------
function initEclipseShadowSim(container) {
  const svg = container.querySelector('#eclipseSvg');
  const slider = container.querySelector('#moonSlider');
  const titleEl = container.querySelector('#eclipseTitle');
  const textEl = container.querySelector('#moonPosText');
  if (!svg || !slider) return;

  function render() {
    const moonDy = parseFloat(slider.value); // -80 to +80
    const sunX = 70, sunY = 120, sunR = 40;
    const earthX = 420, earthY = 120, earthR = 30;
    const moonX = 240, moonY = 120 + moonDy, moonR = 12;

    let eclipseType = "No Eclipse";
    let badgeClass = "text-slate-400 bg-slate-800 border-slate-700";

    if (Math.abs(moonDy) < 8) {
      eclipseType = "TOTAL SOLAR ECLIPSE! 🌑";
      badgeClass = "text-amber-300 bg-amber-500/20 border-amber-500/30";
      if (textEl) textEl.textContent = "Direct Centerline: Moon Umbra strikes Earth";
    } else if (Math.abs(moonDy) < 28) {
      eclipseType = "Partial Solar Eclipse 🌗";
      badgeClass = "text-indigo-300 bg-indigo-500/20 border-indigo-500/30";
      if (textEl) textEl.textContent = "Partial Obscuration: Penumbra cone sweeps Earth";
    } else {
      eclipseType = "No Eclipse (Shadow Misses)";
      if (textEl) textEl.textContent = "Moon shadow cone passes harmlessly above/below Earth";
    }

    if (titleEl) {
      titleEl.textContent = eclipseType;
      titleEl.className = `px-2 py-0.5 rounded text-[11px] font-mono border font-semibold ${badgeClass}`;
    }

    // Shadow ray projection
    // Umbra cone apex from Sun tangents
    const umbraApexX = moonX + 160;
    const umbraApexY = moonY;

    svg.innerHTML = `
      <!-- Space Background -->
      <rect width="500" height="240" fill="#020617" />

      <!-- Penumbra Cone (Light Gray) -->
      <polygon points="${sunX},${sunY - sunR} ${moonX},${moonY + moonR} 480,${moonY + 80} 480,${moonY - 80} ${moonX},${moonY - moonR} ${sunX},${sunY + sunR}" fill="#334155" fill-opacity="0.3" />

      <!-- Umbra Cone (Dark Black) -->
      <polygon points="${moonX},${moonY - moonR} ${moonX},${moonY + moonR} ${umbraApexX},${umbraApexY}" fill="#0f172a" stroke="#000000" stroke-width="1" />

      <!-- Tangent Ray Lines -->
      <line x1="${sunX}" y1="${sunY - sunR}" x2="${moonX}" y2="${moonY - moonR}" stroke="#eab308" stroke-width="1" stroke-dasharray="2,2" opacity="0.6" />
      <line x1="${sunX}" y1="${sunY + sunR}" x2="${moonX}" y2="${moonY + moonR}" stroke="#eab308" stroke-width="1" stroke-dasharray="2,2" opacity="0.6" />

      <!-- The Sun -->
      <circle cx="${sunX}" cy="${sunY}" r="${sunR}" fill="#facc15" stroke="#f59e0b" stroke-width="3" />
      <circle cx="${sunX}" cy="${sunY}" r="${sunR + 8}" fill="none" stroke="#fef08a" stroke-width="2" opacity="0.4" />
      <text x="${sunX}" y="${sunY + 4}" fill="#78350f" font-size="12" font-weight="extrabold" text-anchor="middle">SUN</text>

      <!-- The Moon -->
      <circle cx="${moonX}" cy="${moonY}" r="${moonR}" fill="#94a3b8" stroke="#cbd5e1" stroke-width="1.5" />
      <text x="${moonX}" y="${moonY - 16}" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">Moon</text>

      <!-- Planet Earth -->
      <circle cx="${earthX}" cy="${earthY}" r="${earthR}" fill="#0284c7" stroke="#38bdf8" stroke-width="2" />
      <path d="M 405 110 Q 420 100 435 115 Q 430 135 415 130 Z" fill="#15803d" />
      <text x="${earthX}" y="${earthY + 45}" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Earth</text>
    `;
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 10. Galileo Simple Pendulum Simulator
// -------------------------------------------------------------
function initGalileoPendulumSim(container) {
  const svg = container.querySelector('#pendulumSvg');
  const lenSlider = container.querySelector('#lenSlider');
  const gravSelect = container.querySelector('#gravSelect');
  const lenVal = container.querySelector('#lenVal');
  const periodEl = container.querySelector('#pendulumPeriod');
  if (!svg || !lenSlider || !gravSelect) return;

  let animFrameId = null;
  let startTime = Date.now();

  function loop() {
    const L = parseFloat(lenSlider.value); // meters (0.2 to 2.0)
    const g = parseFloat(gravSelect.value); // m/s^2

    if (lenVal) lenVal.textContent = L.toFixed(1) + ' m';

    // Time period T = 2 * pi * sqrt(L / g)
    const T = 2 * Math.PI * Math.sqrt(L / g);
    if (periodEl) periodEl.textContent = `T = ${T.toFixed(2)} s`;

    const omega = 2 * Math.PI / T;
    const elapsedSec = (Date.now() - startTime) / 1000;
    const maxTheta = 0.35; // radians (~20 deg)
    const currentTheta = maxTheta * Math.cos(omega * elapsedSec);

    const pivotX = 250, pivotY = 30;
    const visualLen = 40 + L * 75; // pixels

    const bobX = pivotX + visualLen * Math.sin(currentTheta);
    const bobY = pivotY + visualLen * Math.cos(currentTheta);

    svg.innerHTML = `
      <!-- Ceiling Stand -->
      <line x1="180" y1="${pivotY}" x2="320" y2="${pivotY}" stroke="#64748b" stroke-width="4" />
      <circle cx="${pivotX}" cy="${pivotY}" r="5" fill="#f59e0b" />

      <!-- Swing Arc Guideline -->
      <path d="M ${pivotX - visualLen * Math.sin(maxTheta)} ${pivotY + visualLen * Math.cos(maxTheta)} Q ${pivotX} ${pivotY + visualLen + 5} ${pivotX + visualLen * Math.sin(maxTheta)} ${pivotY + visualLen * Math.cos(maxTheta)}" stroke="#334155" stroke-width="1.5" stroke-dasharray="3,3" fill="none" />

      <!-- Pendulum String -->
      <line x1="${pivotX}" y1="${pivotY}" x2="${bobX}" y2="${bobY}" stroke="#94a3b8" stroke-width="2" />

      <!-- Brass Bob -->
      <circle cx="${bobX}" cy="${bobY}" r="14" fill="#f59e0b" stroke="#d97706" stroke-width="2" />
      <circle cx="${bobX - 4}" cy="${bobY - 4}" r="3" fill="#fef08a" />

      <!-- Telemetry Readout -->
      <text x="30" y="50" fill="#38bdf8" font-size="11" font-weight="bold">Length L: ${L.toFixed(1)} m</text>
      <text x="30" y="70" fill="#a7f3d0" font-size="11" font-weight="bold">Gravity g: ${g} m/s²</text>
      <text x="30" y="90" fill="#fde68a" font-size="13" font-weight="extrabold">Period T: ${T.toFixed(2)} s</text>
    `;

    animFrameId = requestAnimationFrame(loop);
  }

  lenSlider.addEventListener('input', () => { startTime = Date.now(); });
  gravSelect.addEventListener('change', () => { startTime = Date.now(); });

  loop();
}

// -------------------------------------------------------------
// 11. Photosynthesis Rate Simulator
// -------------------------------------------------------------
function initPhotosynthesisSim(container) {
  const svg = container.querySelector('#photoSvg');
  const lightSlider = container.querySelector('#lightSlider');
  const co2Slider = container.querySelector('#co2Slider');
  const lightVal = container.querySelector('#lightVal');
  const co2Val = container.querySelector('#co2Val');
  const rateBadge = container.querySelector('#bubbleRateBadge');
  if (!svg || !lightSlider || !co2Slider) return;

  function render() {
    const light = parseInt(lightSlider.value, 10);
    const co2 = parseInt(co2Slider.value, 10); // 1, 2, 3
    if (lightVal) lightVal.textContent = light + '%';
    if (co2Val) co2Val.textContent = co2 === 1 ? 'Low' : co2 === 2 ? 'Moderate' : 'High';

    const rate = Math.round((light / 100) * co2 * 24);
    if (rateBadge) rateBadge.textContent = `Rate: ${rate} O2 bubbles/min`;

    // Lamp brightness
    const lampOpacity = Math.max(0.2, light / 100);

    svg.innerHTML = `
      <!-- Beaker filled with water -->
      <rect x="180" y="60" width="160" height="150" rx="10" fill="#0284c7" fill-opacity="0.25" stroke="#38bdf8" stroke-width="2.5" />
      
      <!-- Inverted Funnel -->
      <polygon points="200,190 320,190 265,110 255,110" fill="#cbd5e1" fill-opacity="0.2" stroke="#94a3b8" stroke-width="1.5" />
      <!-- Inverted Test Tube on top -->
      <rect x="252" y="50" width="16" height="60" rx="4" fill="#e2e8f0" fill-opacity="0.3" stroke="#94a3b8" stroke-width="1.5" />
      
      <!-- Oxygen Gas Pocket collected at top -->
      <rect x="253" y="51" width="14" height="${Math.min(30, rate * 0.4)}" fill="#ffffff" fill-opacity="0.8" />

      <!-- Green Hydrilla Plant -->
      <path d="M 260 200 Q 240 170 245 140" stroke="#15803d" stroke-width="4" fill="none" />
      <path d="M 260 200 Q 280 165 275 145" stroke="#15803d" stroke-width="4" fill="none" />
      <!-- Leaves -->
      <ellipse cx="240" cy="160" rx="8" ry="4" fill="#22c55e" />
      <ellipse cx="255" cy="145" rx="8" ry="4" fill="#22c55e" />
      <ellipse cx="270" cy="170" rx="8" ry="4" fill="#22c55e" />

      <!-- Rising Oxygen Bubbles -->
      ${rate > 5 ? `<circle cx="260" cy="130" r="3" fill="#ffffff" opacity="0.9" />` : ''}
      ${rate > 15 ? `<circle cx="258" cy="100" r="4" fill="#ffffff" opacity="0.9" />` : ''}
      ${rate > 30 ? `<circle cx="261" cy="75" r="3.5" fill="#ffffff" opacity="0.9" />` : ''}

      <!-- Light Source (Lamp) at Left -->
      <g transform="translate(60, 100)">
        <polygon points="0,-20 30,-30 30,30 0,20" fill="#475569" stroke="#64748b" />
        <!-- Radiant Light Cone -->
        <polygon points="30,-25 180,60 180,180 30,25" fill="#facc15" fill-opacity="${lampOpacity * 0.4}" />
        <circle cx="15" cy="0" r="12" fill="#fef08a" opacity="${lampOpacity}" />
        <text x="15" y="45" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">Sunlight (${light}%)</text>
      </g>
    `;
  }

  lightSlider.addEventListener('input', render);
  co2Slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 12. Earth Seasons & 23.5° Tilt Simulator
// -------------------------------------------------------------
function initEarthSeasonsSim(container) {
  const svg = container.querySelector('#seasonsSvg');
  const slider = container.querySelector('#orbitSlider');
  const badge = container.querySelector('#seasonBadge');
  const degText = container.querySelector('#orbitDegText');
  const detail = container.querySelector('#seasonDetail');
  if (!svg || !slider) return;

  function render() {
    const deg = parseInt(slider.value, 10); // 0 to 360
    const rad = (deg * Math.PI) / 180;

    let seasonName = "June Solstice";
    let detailText = "Northern Hemisphere tilted toward the Sun (Summer). Direct sunlight concentrates intense heat; long days!";

    if (deg >= 45 && deg < 135) {
      seasonName = "June Solstice (North Summer / South Winter)";
      detailText = "Sun rays strike Tropic of Cancer directly at 90°. Northern Hemisphere enjoys maximum warmth and longest daylight!";
    } else if (deg >= 135 && deg < 225) {
      seasonName = "September Equinox (Autumn in North)";
      detailText = "Sun directly over the Equator. Equal 12-hour day and 12-hour night across all continents.";
    } else if (deg >= 225 && deg < 315) {
      seasonName = "December Solstice (North Winter / South Summer)";
      detailText = "Northern Hemisphere tilts away from Sun. Solar rays hit at an oblique angle, spreading heat over wider area; short days.";
    } else {
      seasonName = "March Equinox (Spring in North)";
      detailText = "Subsolar point crosses Equator northward. Day and night are of equal duration globally.";
    }

    if (badge) badge.textContent = seasonName;
    if (degText) degText.textContent = `Orbital Angle: ${deg}°`;
    if (detail) detail.innerHTML = `<strong>${seasonName}:</strong> ${detailText}`;

    // Sun at center
    const sunX = 250, sunY = 120;
    const a = 160, b = 60; // ellipse axes

    const earthX = sunX + a * Math.cos(rad);
    const earthY = sunY + b * Math.sin(rad);

    // Fixed 23.5 deg axis (tilted toward top-right: angle -23.5 deg)
    const tiltRad = (-23.5 * Math.PI) / 180;
    const axisLen = 28;

    svg.innerHTML = `
      <!-- Orbit Ellipse -->
      <ellipse cx="${sunX}" cy="${sunY}" rx="${a}" ry="${b}" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4" />

      <!-- Center Sun -->
      <circle cx="${sunX}" cy="${sunY}" r="26" fill="#facc15" stroke="#f59e0b" stroke-width="2.5" />
      <text x="${sunX}" y="${sunY + 4}" fill="#78350f" font-size="10" font-weight="extrabold" text-anchor="middle">SUN</text>

      <!-- Solar rays toward Earth -->
      <line x1="${sunX}" y1="${sunY}" x2="${earthX}" y2="${earthY}" stroke="#fef08a" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6" />

      <!-- Earth Group -->
      <g transform="translate(${earthX}, ${earthY})">
        <!-- Rotational Axis (23.5 deg tilt) -->
        <line x1="${-axisLen * Math.sin(tiltRad)}" y1="${axisLen * Math.cos(tiltRad)}" x2="${axisLen * Math.sin(tiltRad)}" y2="${-axisLen * Math.cos(tiltRad)}" stroke="#f43f5e" stroke-width="2" />
        <!-- Earth body -->
        <circle cx="0" cy="0" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" />
        <ellipse cx="2" cy="0" rx="6" ry="12" fill="#15803d" />
        <!-- Equator line -->
        <line x1="-15" y1="0" x2="15" y2="0" stroke="#fde047" stroke-width="1" stroke-dasharray="2,2" transform="rotate(-23.5)" />
      </g>
    `;
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 13. Sustainability Energy Dashboard
// -------------------------------------------------------------
function initSustainabilityDashboardSim(container) {
  const svg = container.querySelector('#sustainSvg');
  const slider = container.querySelector('#renewSlider');
  const shareVal = container.querySelector('#renewShareVal');
  const emissionsVal = container.querySelector('#emissionsVal');
  const warmingVal = container.querySelector('#warmingVal');
  const statusEl = container.querySelector('#climateStatus');
  if (!svg || !slider) return;

  function render() {
    const renew = parseInt(slider.value, 10); // 10 to 100%
    const fossil = 100 - renew;

    if (shareVal) shareVal.textContent = `${renew}% Clean`;

    // Calculate emissions: 36 Gt baseline
    const emissions = (36 * (fossil / 100) + 2.0).toFixed(1);
    if (emissionsVal) emissionsVal.textContent = `${emissions} Gt/yr`;

    // Calculate warming: +1.2 to +3.6 C
    const warming = (1.2 + (fossil / 100) * 2.4).toFixed(1);
    if (warmingVal) warmingVal.textContent = `+${warming}°C`;

    if (statusEl) {
      if (renew >= 75) {
        statusEl.textContent = "Climate Target < 1.5°C Achieved! ✔";
        statusEl.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold";
      } else if (renew >= 45) {
        statusEl.textContent = "Moderate Warming (+2.0°C Target)";
        statusEl.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-amber-500/20 text-amber-300 border border-amber-500/30 font-semibold";
      } else {
        statusEl.textContent = "Dangerous Climate Warming > 2.5°C! ⚠️";
        statusEl.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/20 text-rose-300 border border-rose-500/30 font-semibold";
      }
    }

    svg.innerHTML = `
      <!-- Energy Mix Bar Chart -->
      <text x="30" y="35" fill="#f8fafc" font-size="12" font-weight="bold">Global Energy Generation Grid</text>

      <!-- Background Bar -->
      <rect x="30" y="55" width="440" height="35" rx="8" fill="#1e293b" />
      
      <!-- Renewable Portion (Green) -->
      <rect x="30" y="55" width="${440 * (renew / 100)}" height="35" rx="8" fill="#10b981" />
      
      <!-- Labels on Bar -->
      <text x="${30 + 440 * (renew / 200)}" y="77" fill="#ffffff" font-size="11" font-weight="extrabold" text-anchor="middle">
        ${renew >= 20 ? `Clean (${renew}%)` : ''}
      </text>

      <!-- Wind Turbine & Solar Icon Graphic -->
      <circle cx="100" cy="140" r="14" fill="#0284c7" />
      <text x="100" y="145" fill="#ffffff" font-size="14" text-anchor="middle">☀️</text>
      <text x="100" y="175" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Solar PV</text>

      <circle cx="250" cy="140" r="14" fill="#059669" />
      <text x="250" y="145" fill="#ffffff" font-size="14" text-anchor="middle">💨</text>
      <text x="250" y="175" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Wind Turbines</text>

      <circle cx="400" cy="140" r="14" fill="#dc2626" />
      <text x="400" y="145" fill="#ffffff" font-size="14" text-anchor="middle">🏭</text>
      <text x="400" y="175" fill="#f87171" font-size="11" font-weight="bold" text-anchor="middle">Fossil Fuels (${fossil}%)</text>
    `;
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 14. Precision Measurement & Parallax Simulator
// -------------------------------------------------------------
function initMeniscusParallaxSim(container) {
  const svg = container.querySelector('#meniscusSvg');
  const slider = container.querySelector('#eyeSlider');
  const statusEl = container.querySelector('#parallaxStatus');
  const eyeText = container.querySelector('#eyePosText');
  const apparentVol = container.querySelector('#apparentVol');
  if (!svg || !slider) return;

  function render() {
    const angle = parseInt(slider.value, 10); // -30 to +30 deg
    const trueVol = 50.0;
    const apparent = (trueVol + angle * 0.12).toFixed(1);

    if (apparentVol) apparentVol.textContent = `${apparent} mL`;

    if (eyeText) {
      if (angle === 0) eyeText.textContent = "Perpendicular to Meniscus (0° - True Reading)";
      else if (angle > 0) eyeText.textContent = `Looking Down from Above (+${angle}° High View)`;
      else eyeText.textContent = `Looking Up from Below (${angle}° Low View)`;
    }

    if (statusEl) {
      if (angle === 0) {
        statusEl.textContent = "True Eye Level (Zero Parallax Error) ✔";
        statusEl.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-semibold";
      } else {
        statusEl.textContent = `Parallax Error! (${angle > 0 ? 'Over-estimate' : 'Under-estimate'}) ⚠️`;
        statusEl.className = "px-2 py-0.5 rounded text-[11px] font-mono bg-amber-500/20 text-amber-300 border border-amber-500/30 font-semibold";
      }
    }

    const cylX = 220, cylY = 40, cylW = 60, cylH = 160;
    const waterY = 120; // 50 mL level
    const eyeX = 380, eyeY = waterY - angle * 2.5;

    svg.innerHTML = `
      <!-- Graduated Cylinder Glass Body -->
      <rect x="${cylX}" y="${cylY}" width="${cylW}" height="${cylH}" rx="6" fill="#0284c7" fill-opacity="0.15" stroke="#38bdf8" stroke-width="2" />
      
      <!-- Liquid Water Body -->
      <path d="M ${cylX} ${waterY} Q ${cylX + cylW/2} ${waterY + 12} ${cylX + cylW} ${waterY} L ${cylX + cylW} ${cylY + cylH} L ${cylX} ${cylY + cylH} Z" fill="#0284c7" fill-opacity="0.5" />

      <!-- Concave Meniscus Curve -->
      <path d="M ${cylX} ${waterY} Q ${cylX + cylW/2} ${waterY + 12} ${cylX + cylW} ${waterY}" stroke="#38bdf8" stroke-width="2.5" fill="none" />

      <!-- Graduated Markings (mL) -->
      ${[40, 45, 50, 55, 60].map(v => {
        const my = cylY + cylH - (v - 35) * 6;
        return `
          <line x1="${cylX}" y1="${my}" x2="${cylX + 12}" y2="${my}" stroke="#94a3b8" stroke-width="1.5" />
          <text x="${cylX - 6}" y="${my + 4}" fill="#94a3b8" font-size="9" text-anchor="end">${v}</text>
        `;
      }).join('')}

      <!-- Observer Line of Sight Ray -->
      <line x1="${eyeX}" y1="${eyeY}" x2="${cylX + cylW/2}" y2="${waterY + 12}" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3" />

      <!-- Eye Icon -->
      <g transform="translate(${eyeX}, ${eyeY})">
        <path d="M -15 0 Q 0 -10 15 0 Q 0 10 -15 0 Z" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" />
        <circle cx="0" cy="0" r="5" fill="#0284c7" />
        <text x="22" y="4" fill="#f8fafc" font-size="10" font-weight="bold">Eye</text>
      </g>

      <!-- True Bottom Indicator Arrow -->
      <line x1="${cylX + cylW + 8}" y1="${waterY + 12}" x2="${cylX + cylW + 25}" y2="${waterY + 12}" stroke="#10b981" stroke-width="2" />
      <text x="${cylX + cylW + 30}" y="${waterY + 15}" fill="#10b981" font-size="10" font-weight="bold">True 50 mL</text>
    `;
  }

  slider.addEventListener('input', render);
  render();
}

// -------------------------------------------------------------
// 15. Indian Scientists Timeline Simulator
// -------------------------------------------------------------
function initIndianPioneersSim(container) {
  const svg = container.querySelector('#pioneerSvg');
  const badge = container.querySelector('#pioneerBadge');
  const btns = container.querySelectorAll('.pioneerBtn');
  if (!svg) return;

  const pioneers = {
    jcbose: {
      name: "Acharya Jagadish Chandra Bose",
      period: "1858–1937 • Kolkata",
      title: "Pioneer of Radio Waves & Plant Neurobiology",
      detail: "Invented millimeter microwave wireless communication and the Crescograph. Demonstrated that plants exhibit electrical and nervous responses to mechanical and chemical stimuli.",
      color: "#f59e0b",
      badge: "J.C. Bose (Crescograph)"
    },
    cvraman: {
      name: "Sir Chandrasekhara Venkata Raman",
      period: "1888–1970 • Nobel Prize 1930",
      title: "Discoverer of the Raman Effect (Molecular Light Scattering)",
      detail: "Proved that when photons pass through a transparent medium, they scatter inelastically, shifting frequency. Celebrated across India every February 28 as National Science Day.",
      color: "#38bdf8",
      badge: "C.V. Raman (Nobel 1930)"
    },
    sarabhai: {
      name: "Dr. Vikram Ambalal Sarabhai",
      period: "1919–1971 • Ahmedabad",
      title: "Architect of the Indian Space Program (ISRO)",
      detail: "Established India's space program to apply high technology directly to national development (weather forecasting, remote sensing, tele-education, satellite communications).",
      color: "#10b981",
      badge: "Vikram Sarabhai (ISRO)"
    },
    kalam: {
      name: "Dr. A.P.J. Abdul Kalam",
      period: "1931–2015 • Rameswaram",
      title: "People's President & Visionary Aerospace Scientist",
      detail: "Project Director of India's first satellite launch vehicle (SLV-3) and developer of indigenous defense capability. Championed ignited young minds to dream and build an equitable nation.",
      color: "#ec4899",
      badge: "A.P.J. Kalam (Visionary)"
    }
  };

  function render(p) {
    if (badge) badge.textContent = p.badge;

    svg.innerHTML = `
      <!-- Card Container -->
      <rect x="30" y="30" width="440" height="180" rx="14" fill="#0f172a" stroke="${p.color}" stroke-width="2" />
      
      <!-- Pioneer Emblem -->
      <circle cx="85" cy="85" r="35" fill="#1e293b" stroke="${p.color}" stroke-width="2" />
      <text x="85" y="93" fill="${p.color}" font-size="28" text-anchor="middle">🔬</text>

      <!-- Name & Dates -->
      <text x="140" y="65" fill="#f8fafc" font-size="15" font-weight="extrabold">${p.name}</text>
      <text x="140" y="85" fill="${p.color}" font-size="11" font-weight="bold">${p.period}</text>
      <text x="140" y="105" fill="#94a3b8" font-size="11" font-style="italic">${p.title}</text>

      <!-- Contribution Paragraph -->
      <foreignObject x="60" y="125" width="380" height="75">
        <div xmlns="http://www.w3.org/1999/xhtml" style="font-size: 11px; color: #cbd5e1; line-height: 1.45;">
          ${p.detail}
        </div>
      </foreignObject>
    `;
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.className = "pioneerBtn px-2 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold transition");
      btn.className = "pioneerBtn px-2 py-1.5 rounded-lg bg-amber-600 text-white font-bold transition";
      render(pioneers[btn.dataset.pioneer]);
    });
  });

  render(pioneers.cvraman);
}

// -------------------------------------------------------------
// 16. Young Scientist Constellation Map
// -------------------------------------------------------------
function initYoungScientistConstellationSim(container) {
  const svg = container.querySelector('#constellationSvg');
  const badge = container.querySelector('#constellationBadge');
  const detail = container.querySelector('#constellationDetail');
  if (!svg) return;

  const nodes = [
    { id: 1, name: "Inquiry & Methods", x: 250, y: 55, color: "#f59e0b", desc: "The core engine: Questioning, careful hypothesis testing, controlled variables, and peer review." },
    { id: 2, name: "Living World (Biology)", x: 120, y: 125, color: "#10b981", desc: "Photosynthesis, cellular respiration, human organ systems, ecosystems, and microbiology." },
    { id: 3, name: "Matter & Energy (Physics)", x: 380, y: 125, color: "#38bdf8", desc: "Forces of flight, DC electricity, heating and magnetic effects, simple pendulums, and light optics." },
    { id: 4, name: "Earth & Cosmos (Space)", x: 160, y: 200, color: "#a855f7", desc: "Earth's 23.5° axial tilt, planetary orbits, lunar phases, eclipses, and geological resources." },
    { id: 5, name: "Sustainability & Ethics", x: 340, y: 200, color: "#06b6d4", desc: "Renewable energy, rainwater harvesting, conservation, and responsible technology for the planet." }
  ];

  let activeNode = 2;

  function render() {
    const cur = nodes.find(n => n.id === activeNode);
    if (badge) badge.textContent = cur.name;
    if (detail) detail.innerHTML = `<strong>${cur.name}:</strong> ${cur.desc}`;

    let linesHtml = '';
    // Draw interconnecting constellation lines
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        linesHtml += `
          <line x1="${nodes[i].x}" y1="${nodes[i].y}" x2="${nodes[j].x}" y2="${nodes[j].y}" stroke="#334155" stroke-width="1.5" stroke-dasharray="3,3" />
        `;
      }
    }

    let nodesHtml = '';
    nodes.forEach(n => {
      const isCur = n.id === activeNode;
      nodesHtml += `
        <g style="cursor: pointer;" onclick="window.selectConstellationNode(${n.id})">
          <circle cx="${n.x}" cy="${n.y}" r="${isCur ? 22 : 15}" fill="${isCur ? n.color : '#1e293b'}" stroke="${isCur ? '#ffffff' : n.color}" stroke-width="${isCur ? 3 : 1.5}" />
          <text x="${n.x}" y="${n.y + 4}" fill="${isCur ? '#ffffff' : '#f8fafc'}" font-size="10" font-weight="bold" text-anchor="middle">${n.id}</text>
          <text x="${n.x}" y="${n.y + (n.y > 150 ? 24 : -18)}" fill="${isCur ? '#fde047' : '#94a3b8'}" font-size="9" font-weight="bold" text-anchor="middle">${n.name}</text>
        </g>
      `;
    });

    svg.innerHTML = `
      ${linesHtml}
      ${nodesHtml}
    `;
  }

  window.selectConstellationNode = function(id) {
    activeNode = id;
    render();
  };

  render();
}
'''

with open(".agents/class7_science_ever_evolving_world_js.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""Class 7 Science Chapter 1: The Ever-Evolving World of Science JS Engine"""\n\n')
    f.write("SIMULATORS_JS = " + repr(JS_CODE) + "\n")

print("Generated .agents/class7_science_ever_evolving_world_js.py successfully.")

