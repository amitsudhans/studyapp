# -*- coding: utf-8 -*-
"""
Generates .agents/class7_science_life_processes_js.py containing all JavaScript logic
for the 16 simulators in Class 7 Science Chapter 9: Life Processes in Animals.
"""

js_code = r'''
/* =========================================================================
   CLASS 7 SCIENCE CHAPTER 9: LIFE PROCESSES IN ANIMALS SIMULATORS JAVASCRIPT
   ========================================================================= */

(function() {
  // Global states
  let macroTab = 'carb';
  let macroCleaved = false;

  let peristalsisTimer = null;
  let peristalsisPos = 150;

  let stomachMucus = true;
  let stomachAcid = true;
  let stomachPepsin = true;
  let stomachChurnTimer = null;

  let emulsified = false;
  let villiPumpTimer = null;

  let waterExtractPct = 85;
  let ruminantStep = 1;

  let respAirTimer = null;
  let breathMode = 'inhale';
  let alveolarFlowTimer = null;

  let animalRespTab = 'fish';
  let animalRespTimer = null;

  let heritageTab = 'frog';
  let frogInWater = false;

  /* -------------------------------------------------------------
     1. MACRONUTRIENT BREAKDOWN SIM
     ------------------------------------------------------------- */
  window.switchMacroTab = function(tab) {
    macroTab = tab;
    macroCleaved = false;
    ['btnMacroCarb', 'btnMacroProtein', 'btnMacroFat'].forEach(id => {
      const b = document.getElementById(id);
      if (b) b.className = 'px-3 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';
    });
    const active = document.getElementById(tab === 'carb' ? 'btnMacroCarb' : tab === 'protein' ? 'btnMacroProtein' : 'btnMacroFat');
    if (active) active.className = 'px-3 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md';

    const expl = document.getElementById('macroExpl');
    const badge = document.getElementById('macroBadge');

    if (tab === 'carb') {
      expl.textContent = 'Digestive enzymes cleave long starch polymer chains into simple, soluble glucose units for cellular energy.';
      badge.textContent = 'Polymer: Insoluble Starch Chain';
    } else if (tab === 'protein') {
      expl.textContent = 'Stomach and pancreatic proteases cleave peptide bonds, dismantling protein chains into 20 essential amino acids.';
      badge.textContent = 'Polymer: Complex Polypeptide Chain';
    } else {
      expl.textContent = 'Bile salts emulsify fats, and pancreatic lipase cleaves ester bonds into glycerol and three fatty acid tails.';
      badge.textContent = 'Lipid: Triglyceride Molecule';
    }
    window.renderMacro();
  };

  window.renderMacro = function() {
    const grp = document.getElementById('macroVisualGroup');
    const badge = document.getElementById('macroBadge');
    if (!grp) return;

    if (macroTab === 'carb') {
      if (!macroCleaved) {
        badge.textContent = 'Polymer: Insoluble Starch Chain (C₆H₁₀O₅)ₙ';
        grp.innerHTML = `
          <!-- Starch long chain -->
          ${[80, 140, 200, 260, 320, 380, 440].map((x, i) => `
            <g transform="translate(${x}, 110)">
              <polygon points="0,-18 20,-6 20,18 0,30 -20,18 -20,-6" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
              <text x="0" y="8" text-anchor="middle" fill="#fff" font-size="9" font-weight="bold">Glucose</text>
              ${i < 6 ? '<line x1="20" y1="6" x2="40" y2="6" stroke="#fbbf24" stroke-width="3"/>' : ''}
            </g>
          `).join('')}
          <text x="300" y="45" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">STARCH (Insoluble Complex Polysaccharide)</text>
        `;
      } else {
        badge.textContent = 'Digested Product: Individual Soluble Glucose Monomers';
        grp.innerHTML = `
          <!-- Dispersed glucose monomers -->
          ${[[80, 80], [180, 140], [280, 70], [380, 130], [480, 80], [230, 160], [340, 170]].map(([x, y]) => `
            <g transform="translate(${x}, ${y})">
              <polygon points="0,-16 18,-5 18,16 0,26 -18,16 -18,-5" fill="#10b981" stroke="#34d399" stroke-width="2"/>
              <text x="0" y="8" text-anchor="middle" fill="#022c22" font-size="9" font-weight="black">Glucose</text>
            </g>
          `).join('')}
          <text x="300" y="40" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">✓ Digested: Free Soluble Glucose (Ready to Enter Blood)</text>
        `;
      }
    } else if (macroTab === 'protein') {
      if (!macroCleaved) {
        badge.textContent = 'Polymer: Folded Polypeptide Chain';
        grp.innerHTML = `
          <path d="M 80,120 Q 150,60 220,120 T 360,120 T 500,120" fill="none" stroke="#f43f5e" stroke-width="12" stroke-linecap="round"/>
          ${[80, 130, 180, 230, 280, 330, 380, 430, 480].map((x, i) => `
            <circle cx="${x}" cy="${120 + Math.sin(i)*25}" r="11" fill="#be123c" stroke="#fff" stroke-width="1.5"/>
            <text x="${x}" y="${123 + Math.sin(i)*25}" text-anchor="middle" fill="#fff" font-size="7">AA</text>
          `).join('')}
          <text x="300" y="45" text-anchor="middle" fill="#f43f5e" font-size="12" font-weight="bold">PROTEIN (Complex Peptide Chain)</text>
        `;
      } else {
        badge.textContent = 'Digested Product: Free Amino Acids (Building Blocks)';
        grp.innerHTML = `
          ${[[90, 80], [160, 150], [230, 90], [300, 140], [370, 75], [440, 135], [200, 170], [350, 175]].map(([x, y]) => `
            <g transform="translate(${x}, ${y})">
              <circle cx="0" cy="0" r="14" fill="#059669" stroke="#34d399" stroke-width="2"/>
              <text x="0" y="4" text-anchor="middle" fill="#fff" font-size="8" font-weight="bold">Amino</text>
            </g>
          `).join('')}
          <text x="300" y="40" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">✓ Cleaved: Individual Amino Acids for Muscle & Tissue Repair</text>
        `;
      }
    } else {
      // Fats
      if (!macroCleaved) {
        badge.textContent = 'Lipid: Triglyceride Molecule';
        grp.innerHTML = `
          <!-- Glycerol head -->
          <rect x="180" y="70" width="30" height="90" rx="6" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
          <text x="195" y="120" text-anchor="middle" fill="#78350f" font-size="8" font-weight="bold" transform="rotate(-90 195 120)">Glycerol</text>
          <!-- 3 Fatty acid tails -->
          <path d="M 210,85 L 360,85" stroke="#e11d48" stroke-width="8" stroke-linecap="round"/>
          <path d="M 210,115 L 380,115" stroke="#e11d48" stroke-width="8" stroke-linecap="round"/>
          <path d="M 210,145 L 350,145" stroke="#e11d48" stroke-width="8" stroke-linecap="round"/>
          <text x="300" y="50" text-anchor="middle" fill="#fbbf24" font-size="12" font-weight="bold">TRIGLYCERIDE (Insoluble Fat Molecule)</text>
        `;
      } else {
        badge.textContent = 'Digested Product: 1 Glycerol + 3 Free Fatty Acids';
        grp.innerHTML = `
          <!-- Separated glycerol -->
          <rect x="100" y="80" width="35" height="75" rx="6" fill="#10b981" stroke="#34d399" stroke-width="2"/>
          <text x="117" y="122" text-anchor="middle" fill="#022c22" font-size="9" font-weight="bold" transform="rotate(-90 117 122)">Glycerol</text>
          <!-- Separated fatty acids -->
          <path d="M 220,60 L 380,60" stroke="#38bdf8" stroke-width="7" stroke-linecap="round"/>
          <text x="430" y="64" fill="#38bdf8" font-size="9">Fatty Acid 1</text>
          <path d="M 220,110 L 400,110" stroke="#38bdf8" stroke-width="7" stroke-linecap="round"/>
          <text x="445" y="114" fill="#38bdf8" font-size="9">Fatty Acid 2</text>
          <path d="M 220,160 L 370,160" stroke="#38bdf8" stroke-width="7" stroke-linecap="round"/>
          <text x="420" y="164" fill="#38bdf8" font-size="9">Fatty Acid 3</text>
          <text x="300" y="35" text-anchor="middle" fill="#34d399" font-size="12" font-weight="bold">✓ Digested: Glycerol + Fatty Acids (Absorbed by Lacteal)</text>
        `;
      }
    }
  };

  window.animateMacroCleavage = function() {
    macroCleaved = true;
    window.renderMacro();
  };

  window.resetMacro = function() {
    macroCleaved = false;
    window.renderMacro();
  };

  /* -------------------------------------------------------------
     2. ALIMENTARY CANAL MAP SIM
     ------------------------------------------------------------- */
  const organData = {
    mouth: {
      name: "Buccal Cavity (Mouth)",
      ph: "pH 6.8 (Neutral)",
      length: "~10 cm",
      secretion: "Saliva (Salivary Amylase)",
      task: "Chewing by teeth & starch conversion to sugar",
      desc: "Teeth mechanically crush food; salivary amylase converts complex starch into simple sweet maltose."
    },
    oesophagus: {
      name: "Oesophagus (Food Pipe)",
      ph: "pH 7.0",
      length: "~25 cm",
      secretion: "Mucus (Lubrication)",
      task: "Peristaltic propulsion to stomach",
      desc: "Flexible muscular tube where coordinated circular and longitudinal muscle contractions push food toward stomach."
    },
    stomach: {
      name: "Stomach (J-Shaped Sac)",
      ph: "pH 1.5–2.0 (Strong Acid)",
      length: "~25 cm (expandable)",
      secretion: "HCl, Pepsin, Mucus",
      task: "Protein breakdown & killing bacteria",
      desc: "Vigorously churns food into semi-liquid chyme. HCl sterilizes food and activates pepsin to break down proteins."
    },
    liver: {
      name: "Liver & Gall Bladder",
      ph: "pH 8.0 (Alkaline)",
      length: "Largest body gland (~1.5 kg)",
      secretion: "Bile Salts (No Enzymes)",
      task: "Neutralize acid & emulsify fats",
      desc: "Liver produces bile stored in gall bladder; bile salts emulsify large fat globules into microscopic droplets."
    },
    pancreas: {
      name: "Pancreas (Gland)",
      ph: "pH 8.2 (Alkaline)",
      length: "~15 cm",
      secretion: "Pancreatic Juice (Amylase, Trypsin, Lipase)",
      task: "Complete chemical digestion",
      desc: "Secretes powerful enzymes into duodenum to break down carbohydrates, proteins, and emulsified fats."
    },
    small_int: {
      name: "Small Intestine (Ileum)",
      ph: "pH 7.5–8.0",
      length: "~6 metres (Longest organ)",
      secretion: "Intestinal Enzymes",
      task: "Final digestion & nutrient absorption",
      desc: "Millions of finger-like villi provide over 250 m² of surface area to absorb sugars, amino acids, and fats into blood."
    },
    large_int: {
      name: "Large Intestine (Colon)",
      ph: "pH 6.5–7.0",
      length: "~1.5 metres",
      secretion: "Mucus",
      task: "Water & salt reabsorption",
      desc: "Reabsorbs up to 90% of water and essential mineral salts, consolidating unabsorbed residue into solid stool."
    },
    rectum: {
      name: "Rectum & Anus",
      ph: "pH 7.0",
      length: "~15 cm",
      secretion: "None",
      task: "Storage & Egestion of faeces",
      desc: "Temporarily stores semi-solid faeces until stretch receptors trigger egestion (defaecation) through the anal sphincter."
    }
  };

  window.inspectOrgan = function(key) {
    const d = organData[key];
    if (!d) return;

    document.getElementById('organName').textContent = d.name;
    document.getElementById('organPhBadge').textContent = d.ph;
    document.getElementById('organLength').textContent = d.length;
    document.getElementById('organSecretion').textContent = d.secretion;
    document.getElementById('organTask').textContent = d.task;
    document.getElementById('organDesc').textContent = d.desc;
  };

  /* -------------------------------------------------------------
     3. MOUTH SALIVA STARCH SIM
     ------------------------------------------------------------- */
  window.dropIodineTest = function() {
    const tubeALiq = document.getElementById('tubeALiquid');
    const tubeBLiq = document.getElementById('tubeBLiquid');
    const resA = document.getElementById('tubeAResult');
    const resB = document.getElementById('tubeBResult');

    if (tubeALiq) tubeALiq.setAttribute('fill', '#1e1b4b'); // Blue-Black
    if (tubeBLiq) tubeBLiq.setAttribute('fill', '#b45309'); // Yellow-Brown

    if (resA) {
      resA.className = 'bg-indigo-950 p-1.5 rounded-lg border border-indigo-500 text-center text-[11px] text-cyan-300 w-full font-mono font-bold';
      resA.textContent = '✓ Blue-Black: Intact Starch Present!';
    }
    if (resB) {
      resB.className = 'bg-emerald-950 p-1.5 rounded-lg border border-emerald-500 text-center text-[11px] text-emerald-300 w-full font-mono font-bold';
      resB.textContent = '✓ Brown/Yellow: Starch Digested into Sugar!';
    }
  };

  /* -------------------------------------------------------------
     4. PERISTALSIS WAVE SIM
     ------------------------------------------------------------- */
  window.setPeristalsisPos = function(x) {
    peristalsisPos = parseFloat(x);
    const bolus = document.getElementById('peristalsisBolus');
    const txt = document.getElementById('bolusText');
    const badge = document.getElementById('peristalsisBadge');
    const arrows = document.getElementById('contractionArrows');

    if (bolus) { bolus.setAttribute('cx', peristalsisPos); }
    if (txt) { txt.setAttribute('x', peristalsisPos); }
    if (arrows) { arrows.setAttribute('transform', `translate(${peristalsisPos - 40}, 0)`); }

    // Wave shape on walls
    const topWall = document.getElementById('oesophTopWall');
    const botWall = document.getElementById('oesophBottomWall');
    if (topWall && botWall) {
      topWall.setAttribute('d', `M 50,60 Q ${peristalsisPos - 20},75 ${peristalsisPos},50 Q ${peristalsisPos + 20},60 450,60`);
      botWall.setAttribute('d', `M 50,140 Q ${peristalsisPos - 20},125 ${peristalsisPos},150 Q ${peristalsisPos + 20},140 450,140`);
    }

    if (badge) {
      if (peristalsisPos < 150) badge.textContent = 'Bolus Transit: Upper Oesophagus (Pharynx Exit)';
      else if (peristalsisPos < 350) badge.textContent = 'Bolus Transit: Mid-Thoracic Oesophagus (Peristaltic Wave)';
      else badge.textContent = 'Bolus Transit: Cardiac Sphincter → Entering Stomach';
    }
  };

  window.autoPeristalsis = function() {
    clearInterval(peristalsisTimer);
    document.getElementById('btnAutoPeristalsis').textContent = 'Propelling...';
    let pos = 80;
    peristalsisTimer = setInterval(() => {
      pos += 5;
      const slider = document.getElementById('peristalsisSlider');
      if (slider) slider.value = pos;
      window.setPeristalsisPos(pos);

      if (pos >= 420) {
        clearInterval(peristalsisTimer);
        document.getElementById('btnAutoPeristalsis').textContent = '▶ Swallow Bolus';
      }
    }, 40);
  };

  window.resetPeristalsis = function() {
    clearInterval(peristalsisTimer);
    document.getElementById('btnAutoPeristalsis').textContent = '▶ Swallow Bolus';
    document.getElementById('peristalsisSlider').value = 150;
    window.setPeristalsisPos(150);
  };

  /* -------------------------------------------------------------
     5. STOMACH CHURNING ACID SIM
     ------------------------------------------------------------- */
  window.toggleStomachMucus = function() {
    stomachMucus = document.getElementById('chkMucus').checked;
    const layer = document.getElementById('stomachMucusLayer');
    const badge = document.getElementById('stomachStatusBadge');
    const feedback = document.getElementById('stomachFeedback');

    if (layer) layer.style.display = stomachMucus ? 'block' : 'none';

    if (!stomachMucus && stomachAcid) {
      badge.className = 'absolute top-2 left-2 bg-rose-950/90 border border-rose-500 text-xs px-2.5 py-1 rounded text-rose-300 font-mono font-bold';
      badge.textContent = '⚠ WARNING: Mucus Shield Absent! Acid Eroding Gastric Wall (Ulcer Formation)';
      feedback.textContent = 'Without protective alkaline mucus, hydrochloric acid corrodes and digests living stomach tissue!';
    } else {
      badge.className = 'absolute top-2 left-2 bg-slate-900/85 border border-slate-700 text-xs px-2.5 py-1 rounded text-slate-300 font-mono';
      badge.textContent = 'Mucus Shield: ACTIVE • Gastric Wall Protected';
      feedback.textContent = 'HCl activates pepsin to cleave proteins; the green alkaline mucus protects the stomach from digesting itself!';
    }
  };

  window.toggleStomachAcid = function() {
    stomachAcid = document.getElementById('chkAcid').checked;
    const pool = document.getElementById('stomachChymePool');
    if (pool) pool.setAttribute('fill', stomachAcid ? '#f59e0b' : '#38bdf8');
    window.toggleStomachMucus();
  };

  window.toggleStomachPepsin = function() {
    stomachPepsin = document.getElementById('chkPepsin').checked;
  };

  window.churnStomach = function() {
    const particles = document.getElementById('stomachProteinParticles');
    if (!particles) return;

    let t = 0;
    clearInterval(stomachChurnTimer);
    stomachChurnTimer = setInterval(() => {
      t += 0.2;
      const dx = Math.sin(t * 5) * 8;
      const dy = Math.cos(t * 5) * 6;
      particles.setAttribute('transform', `translate(${dx}, ${dy})`);

      if (t > 4) {
        clearInterval(stomachChurnTimer);
        particles.setAttribute('transform', 'translate(0, 0)');
      }
    }, 40);
  };

  /* -------------------------------------------------------------
     6. LIVER PANCREAS BILE SIM
     ------------------------------------------------------------- */
  window.triggerEmulsification = function() {
    emulsified = true;
    const drop = document.getElementById('largeFatDrop');
    const micSvg = document.getElementById('micellesSvg');
    const resText = document.getElementById('emulsifyResultText');

    if (drop) drop.setAttribute('opacity', '0.2');

    // Create 30 tiny micelles in micellesSvg
    let html = '';
    for (let i = 0; i < 28; i++) {
      const rx = 25 + Math.random() * 110;
      const ry = 25 + Math.random() * 90;
      html += `<circle cx="${rx}" cy="${ry}" r="6" fill="#f59e0b" stroke="#10b981" stroke-width="2"/>`;
    }
    if (micSvg) micSvg.innerHTML = html;
    if (resText) resText.textContent = '✓ Emulsified into 1000s of microscopic micelles! Lipase digests in seconds.';
  };

  /* -------------------------------------------------------------
     7. INTESTINAL VILLI ABSORPTION SIM
     ------------------------------------------------------------- */
  window.pumpVilliAbsorption = function() {
    const lumen = document.getElementById('lumenNutrients');
    if (!lumen) return;

    // Spawn animated floating nutrient particles
    let html = '';
    for (let i = 0; i < 20; i++) {
      const x = 50 + Math.random() * 400;
      const y = 15 + Math.random() * 35;
      const isFat = Math.random() > 0.5;
      html += `<circle cx="${x}" cy="${y}" r="${isFat ? 4 : 3}" fill="${isFat ? '#facc15' : '#38bdf8'}" opacity="0.8"/>`;
    }
    lumen.innerHTML = html;
  };

  /* -------------------------------------------------------------
     8. LARGE INTESTINE EGESTION SIM
     ------------------------------------------------------------- */
  window.setWaterExtraction = function(val) {
    waterExtractPct = parseFloat(val);
    document.getElementById('waterExtractVal').textContent = `${waterExtractPct}%`;
    const consistency = document.getElementById('stoolConsistency');
    const path = document.getElementById('colonMoisturePath');

    if (waterExtractPct < 50) {
      if (consistency) { consistency.textContent = 'Watery / Liquid (Diarrhea)'; consistency.className = 'text-rose-400 font-bold'; }
      if (path) path.setAttribute('opacity', '0.9');
    } else if (waterExtractPct > 90) {
      if (consistency) { consistency.textContent = 'Hard / Dry (Constipation)'; consistency.className = 'text-amber-400 font-bold'; }
      if (path) path.setAttribute('opacity', '0.3');
    } else {
      if (consistency) { consistency.textContent = 'Semi-Solid (Normal Faeces)'; consistency.className = 'text-emerald-400 font-bold'; }
      if (path) path.setAttribute('opacity', '0.6');
    }
  };

  /* -------------------------------------------------------------
     9. RUMINANT DIGESTION SIM
     ------------------------------------------------------------- */
  window.stepRuminant = function(step) {
    ruminantStep = step;
    [1, 2, 3].forEach(i => {
      const b = document.getElementById(`btnRum${i}`);
      if (b) b.className = i === step ?
        'px-2.5 py-1 rounded bg-amber-500 text-slate-950 font-semibold' :
        'px-2.5 py-1 rounded bg-slate-700 text-slate-300 hover:bg-slate-600';
    });

    const badge = document.getElementById('ruminantStepBadge');
    const cud = document.getElementById('cudParticle');

    if (step === 1) {
      badge.textContent = 'Step 1: Rapidly swallowed grass enters Rumen for anaerobic cellulose fermentation';
      if (cud) { cud.setAttribute('cx', 240); cud.setAttribute('cy', 110); cud.setAttribute('fill', '#22c55e'); }
    } else if (step === 2) {
      badge.textContent = 'Step 2: Rumination! Fermented cud is regurgitated from reticulum to mouth for thorough chewing';
      if (cud) { cud.setAttribute('cx', 60); cud.setAttribute('cy', 90); cud.setAttribute('fill', '#facc15'); }
    } else {
      badge.textContent = 'Step 3: Chewed cud passes through Omasum (water removal) into Abomasum (true stomach digestion)';
      if (cud) { cud.setAttribute('cx', 370); cud.setAttribute('cy', 125); cud.setAttribute('fill', '#ef4444'); }
    }
  };

  window.resetRuminant = function() {
    window.stepRuminant(1);
  };

  /* -------------------------------------------------------------
     10. BIRD GIZZARD MECHANICS SIM
     ------------------------------------------------------------- */
  window.grindGizzard = function() {
    const gizzard = document.getElementById('gizzardBody');
    const seed1 = document.getElementById('seed1');
    const seed2 = document.getElementById('seed2');
    const press = document.getElementById('gizzardPressure');

    if (press) press.textContent = 'MAXIMUM (Contracting)';

    let count = 0;
    const timer = setInterval(() => {
      count++;
      const s = 1 + Math.sin(count) * 0.08;
      if (gizzard) gizzard.setAttribute('transform', `translate(160, 110) scale(${s})`);

      if (count > 12) {
        clearInterval(timer);
        if (gizzard) gizzard.setAttribute('transform', 'translate(160, 110) scale(1)');
        if (seed1) seed1.setAttribute('r', '2');
        if (seed2) seed2.setAttribute('r', '1.5');
        if (press) press.textContent = 'Idle (Grains Pulverized)';
      }
    }, 50);
  };

  /* -------------------------------------------------------------
     11. CELLULAR RESPIRATION SIM
     ------------------------------------------------------------- */
  window.pulseCellularRespiration = function() {
    const badge = document.getElementById('respireBadge');
    if (badge) {
      badge.textContent = '⚡ 1 Mole Glucose oxidized with 6 O₂ → Released 2870 kJ energy (38 ATP) + 6 CO₂ + 6 H₂O!';
      badge.className = 'absolute bottom-2 left-3 bg-amber-950/90 border border-amber-500 text-xs px-3 py-1 rounded-lg text-amber-300 font-mono font-bold';
    }
  };

  /* -------------------------------------------------------------
     12. HUMAN RESPIRATORY TRACT SIM
     ------------------------------------------------------------- */
  window.traceAirflow = function() {
    const dot = document.getElementById('airDot');
    const badge = document.getElementById('respTractBadge');
    if (!dot) return;

    clearInterval(respAirTimer);
    let step = 0;
    const points = [
      [125, 40, 'Nostrils: Dust filtered by hairs & mucus'],
      [145, 55, 'Pharynx & Larynx: Air warmed and humidified'],
      [170, 95, 'Trachea: C-shaped cartilage rings keep tube open'],
      [170, 140, 'Bronchi Carina: Branching into left & right lungs'],
      [100, 190, 'Left Lung: Terminal bronchioles and alveoli'],
      [240, 190, 'Right Lung: 300 million alveoli gas exchange']
    ];

    respAirTimer = setInterval(() => {
      if (step >= points.length) {
        clearInterval(respAirTimer);
        return;
      }
      const [x, y, desc] = points[step];
      dot.setAttribute('cx', x);
      dot.setAttribute('cy', y);
      if (badge) badge.textContent = `Pathway: ${desc}`;
      step++;
    }, 600);
  };

  /* -------------------------------------------------------------
     13. BREATHING DIAPHRAGM SIM
     ------------------------------------------------------------- */
  window.setBreathingAction = function(mode) {
    breathMode = mode;
    document.getElementById('btnInhale').className = mode === 'inhale' ?
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-cyan-500 text-slate-950 shadow-md' :
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';
    document.getElementById('btnExhale').className = mode === 'exhale' ?
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-cyan-500 text-slate-950 shadow-md' :
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';

    const bL = document.getElementById('balloonLeft');
    const bR = document.getElementById('balloonRight');
    const dSheet = document.getElementById('rubberDiaphragm');

    const title = document.getElementById('breathModeTitle');
    const dState = document.getElementById('diaphragmState');
    const cVol = document.getElementById('chestVolumeState');
    const cPress = document.getElementById('chestPressureState');
    const aFlow = document.getElementById('airFlowState');

    if (mode === 'inhale') {
      title.textContent = 'Inhalation (Breathing In)';
      dState.textContent = 'Contracts & Moves DOWNWARD (Flattens)';
      cVol.textContent = 'EXPANDS (Greater Volume)';
      cPress.textContent = 'DROPS below atmospheric pressure';
      aFlow.textContent = 'Rushes into Lungs (Balloons Inflate)';

      if (bL) { bL.setAttribute('rx', 22); bL.setAttribute('ry', 28); }
      if (bR) { bR.setAttribute('rx', 22); bR.setAttribute('ry', 28); }
      if (dSheet) dSheet.setAttribute('d', 'M 40,160 Q 100,185 160,160');
    } else {
      title.textContent = 'Exhalation (Breathing Out)';
      dState.textContent = 'Relaxes & Curves UPWARD into Dome';
      cVol.textContent = 'DECREASES (Smaller Volume)';
      cPress.textContent = 'RISES above atmospheric pressure';
      aFlow.textContent = 'Squeezed OUT of Lungs (Balloons Deflate)';

      if (bL) { bL.setAttribute('rx', 12); bL.setAttribute('ry', 16); }
      if (bR) { bR.setAttribute('rx', 12); bR.setAttribute('ry', 16); }
      if (dSheet) dSheet.setAttribute('d', 'M 40,160 Q 100,135 160,160');
    }
  };

  /* -------------------------------------------------------------
     14. ALVEOLI GAS EXCHANGE SIM
     ------------------------------------------------------------- */
  window.pumpAlveolarBlood = function() {
    const grp = document.getElementById('rbcFlowGroup');
    if (!grp) return;

    let y = 25;
    clearInterval(alveolarFlowTimer);
    alveolarFlowTimer = setInterval(() => {
      y += 8;
      // RBC turns from deoxygenated purple (#7c3aed) to oxygenated crimson (#dc2626) as it passes alveolus midpoint
      const color = y < 110 ? '#7c3aed' : '#ef4444';
      grp.innerHTML = `
        <ellipse cx="250" cy="${y}" rx="10" ry="7" fill="${color}" stroke="#fff" stroke-width="1.5"/>
        <text x="250" y="${y + 3}" text-anchor="middle" fill="#fff" font-size="7">${y < 110 ? 'De-O₂' : 'O₂-Hb'}</text>
      `;

      if (y > 195) {
        clearInterval(alveolarFlowTimer);
      }
    }, 40);
  };

  /* -------------------------------------------------------------
     15. ANIMAL RESPIRATION DIVERSITY SIM
     ------------------------------------------------------------- */
  window.switchAnimalRespTab = function(tab) {
    animalRespTab = tab;
    ['btnRespFish', 'btnRespWorm', 'btnRespInsect'].forEach(id => {
      const b = document.getElementById(id);
      if (b) b.className = 'px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';
    });
    const active = document.getElementById(tab === 'fish' ? 'btnRespFish' : tab === 'earthworm' ? 'btnRespWorm' : 'btnRespInsect');
    if (active) active.className = 'px-2.5 py-1 text-xs font-semibold rounded-lg bg-cyan-500 text-slate-950 shadow-md';

    const expl = document.getElementById('animalRespExpl');
    const badge = document.getElementById('animalRespBadge');

    if (tab === 'fish') {
      expl.innerHTML = '<strong>Fish Gills:</strong> Water flows in through the mouth and over vascularized gill arches beneath the operculum. Blood capillaries absorb dissolved O₂ and release CO₂.';
      badge.textContent = 'Fish Gills: Feathery filaments lined with capillary arches';
    } else if (tab === 'earthworm') {
      expl.innerHTML = '<strong>Earthworm Cutaneous Skin:</strong> Lacks lungs or gills. Dissolved atmospheric O₂ diffuses directly through its thin, mucus-covered moist skin into dermal blood capillaries.';
      badge.textContent = 'Earthworm Skin: Moist mucus layer allows gas diffusion';
    } else {
      expl.innerHTML = '<strong>Insect Tracheal Network:</strong> Air enters lateral body pores called spiracles, traveling through branching tracheal air tubes directly to living cells without needing blood hemoglobin.';
      badge.textContent = 'Insect Spiracles: Direct air delivery via tracheal pipes';
    }
    window.renderAnimalResp();
  };

  window.renderAnimalResp = function() {
    const grp = document.getElementById('animalRespVisualGroup');
    if (!grp) return;

    if (animalRespTab === 'fish') {
      grp.innerHTML = `
        <!-- Fish head & gill chamber -->
        <path d="M 120,110 Q 150,40 280,60 L 380,110 L 280,160 Q 150,180 120,110 Z" fill="#0f172a" stroke="#0284c7" stroke-width="2"/>
        <!-- Fish eye -->
        <circle cx="160" cy="90" r="10" fill="#fff"/>
        <circle cx="160" cy="90" r="5" fill="#0f172a"/>
        <!-- Feathery Gill Filaments (Red) -->
        <g transform="translate(230, 80)">
          <path d="M 0,0 Q 20,25 0,55" stroke="#ef4444" stroke-width="5" fill="none"/>
          <path d="M 10,0 Q 30,25 10,55" stroke="#ef4444" stroke-width="5" fill="none"/>
          <path d="M 20,0 Q 40,25 20,55" stroke="#ef4444" stroke-width="5" fill="none"/>
        </g>
        <!-- Water flow stream (blue) -->
        <path d="M 80,110 Q 180,110 230,105 T 300,90" fill="none" stroke="#38bdf8" stroke-width="4" stroke-dasharray="6 3"/>
        <text x="140" y="135" fill="#38bdf8" font-size="9">Water + Dissolved O₂ In</text>
        <text x="250" y="60" fill="#f87171" font-size="9">Gill Filaments</text>
      `;
    } else if (animalRespTab === 'earthworm') {
      grp.innerHTML = `
        <!-- Earthworm tubular segmented body -->
        <rect x="100" y="90" width="300" height="40" rx="20" fill="#9d174d" stroke="#f472b6" stroke-width="2"/>
        <!-- Segments -->
        ${[140, 180, 220, 260, 300, 340].map(x => `<line x1="${x}" y1="90" x2="${x}" y2="130" stroke="#fbcfe8" stroke-width="1.5" stroke-dasharray="2 2"/>`).join('')}
        <!-- Moist mucus sheen -->
        <rect x="98" y="88" width="304" height="44" rx="22" fill="none" stroke="#38bdf8" stroke-width="3" opacity="0.7"/>
        <!-- O2 diffusion inward -->
        <line x1="220" y1="60" x2="220" y2="85" stroke="#34d399" stroke-width="3"/>
        <polygon points="220,88 216,80 224,80" fill="#34d399"/>
        <text x="220" y="50" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">O₂ Diffuses Through Moist Cuticle</text>
        <text x="250" y="155" text-anchor="middle" fill="#fbcfe8" font-size="9">Superficial Capillary Network</text>
      `;
    } else {
      // Insect
      grp.innerHTML = `
        <!-- Insect abdomen profile -->
        <ellipse cx="250" cy="110" rx="140" ry="45" fill="#78350f" stroke="#d97706" stroke-width="2"/>
        <!-- Spiracles (pores) along bottom -->
        ${[160, 200, 240, 280, 320].map(x => `
          <circle cx="${x}" cy="155" r="5" fill="#f59e0b" stroke="#fff" stroke-width="1.5"/>
          <!-- Tracheal branching tree -->
          <line x1="${x}" y1="150" x2="${x}" y2="110" stroke="#38bdf8" stroke-width="3"/>
          <line x1="${x}" y1="110" x2="${x - 15}" y2="90" stroke="#38bdf8" stroke-width="2"/>
          <line x1="${x}" y1="110" x2="${x + 15}" y2="90" stroke="#38bdf8" stroke-width="2"/>
        `).join('')}
        <text x="250" y="180" text-anchor="middle" fill="#fef08a" font-size="10" font-weight="bold">Spiracles (Lateral Air Pores)</text>
        <text x="250" y="80" text-anchor="middle" fill="#7dd3fc" font-size="9">Tracheal Pipes Deliver Air Directly to Cells</text>
      `;
    }
  };

  window.animateAnimalResp = function() {
    window.renderAnimalResp();
  };

  /* -------------------------------------------------------------
     16. FROG METAMORPHOSIS AYURVEDA SIM
     ------------------------------------------------------------- */
  window.switchHeritageTab = function(tab) {
    heritageTab = tab;
    document.getElementById('btnHeritFrog').className = tab === 'frog' ?
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md' :
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';
    document.getElementById('btnHeritAyur').className = tab === 'ayurveda' ?
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md' :
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';

    const expl = document.getElementById('frogAyurExpl');
    const badge = document.getElementById('frogAyurBadge');
    const btn = document.getElementById('btnActionFrogAyur');

    if (tab === 'frog') {
      expl.innerHTML = 'Frogs are the ultimate respiratory shapeshifters: young tadpoles breathe via gills, underwater adults breathe via moist skin, and land adults breathe via lungs and throat pumping!';
      badge.textContent = 'Frog Mode: Adult on Land (Pulmonary Lungs + Buccal Pumping)';
      btn.textContent = 'Toggle Habitat (Water vs Land)';
    } else {
      expl.innerHTML = '<strong>Ayurvedic Heritage:</strong> Sushruta and Charaka described <em>Jatharagni</em> as the internal metabolic fire transforming ingested food into nutrient essence (<em>Ahararasa</em>), while <em>Prana Vayu</em> powers vital life energy.';
      badge.textContent = 'Ayurvedic Physiology: Jatharagni (Digestive Fire) & Prana Vayu';
      btn.textContent = 'Stoke Jatharagni Flame';
    }
    window.renderFrogAyur();
  };

  window.renderFrogAyur = function() {
    const grp = document.getElementById('frogAyurVisualGroup');
    if (!grp) return;

    if (heritageTab === 'frog') {
      if (!frogInWater) {
        // Frog on Land
        grp.innerHTML = `
          <!-- Land ground -->
          <rect x="50" y="180" width="400" height="20" fill="#1e293b"/>
          <!-- Adult Frog -->
          <ellipse cx="250" cy="140" rx="55" ry="38" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
          <circle cx="280" cy="115" r="12" fill="#22c55e"/>
          <circle cx="283" cy="113" r="5" fill="#022c22"/>
          <!-- Buccal throat pumping -->
          <ellipse cx="270" cy="155" rx="18" ry="12" fill="#166534"/>
          <!-- Internal Lungs highlighted -->
          <ellipse cx="230" cy="135" rx="14" ry="10" fill="#ef4444" opacity="0.8"/>
          <text x="250" y="60" text-anchor="middle" fill="#4ade80" font-size="12" font-weight="bold">Adult Frog on Land: Pulmonary Lungs + Buccal Pumping</text>
        `;
      } else {
        // Frog in Water
        grp.innerHTML = `
          <!-- Water pond background -->
          <rect x="50" y="40" width="400" height="150" fill="#0c4a6e" opacity="0.6"/>
          <ellipse cx="250" cy="120" rx="55" ry="32" fill="#15803d" stroke="#38bdf8" stroke-width="3"/>
          <text x="250" y="125" text-anchor="middle" fill="#fff" font-size="9">Skin Respiration</text>
          <!-- Dissolved O2 bubbles entering moist skin -->
          <circle cx="200" cy="90" r="4" fill="#38bdf8"/>
          <circle cx="300" cy="90" r="4" fill="#38bdf8"/>
          <circle cx="250" cy="165" r="4" fill="#38bdf8"/>
          <text x="250" y="60" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="bold">Underwater / Hibernation: Cutaneous Skin Respiration</text>
        `;
      }
    } else {
      // Ayurveda
      grp.innerHTML = `
        <!-- Digestive cauldron & Jatharagni fire -->
        <g transform="translate(180, 70)">
          <!-- Flame -->
          <path d="M 70,110 Q 50,60 70,30 Q 90,60 70,110 Z" fill="#f59e0b" filter="drop-shadow(0 0 12px rgba(245,158,11,0.9))"/>
          <path d="M 70,110 Q 60,75 70,55 Q 80,75 70,110 Z" fill="#fef08a"/>
          <text x="70" y="130" text-anchor="middle" fill="#fbbf24" font-size="11" font-weight="bold">JATHARAGNI</text>
          <text x="70" y="145" text-anchor="middle" fill="#cbd5e1" font-size="8">Central Metabolic Fire</text>
        </g>
        <g transform="translate(320, 80)">
          <text x="0" y="20" fill="#38bdf8" font-size="11" font-weight="bold">Prana Vayu (Vital Breath)</text>
          <text x="0" y="40" fill="#94a3b8" font-size="9">Energizes Heart & Brain</text>
          <text x="0" y="65" fill="#34d399" font-size="11" font-weight="bold">Ahararasa (Nutrient Essence)</text>
          <text x="0" y="85" fill="#94a3b8" font-size="9">Builds the 7 Sapta Dhatus</text>
        </g>
      `;
    }
  };

  window.actionFrogAyur = function() {
    if (heritageTab === 'frog') {
      frogInWater = !frogInWater;
      const badge = document.getElementById('frogAyurBadge');
      if (badge) {
        badge.textContent = frogInWater ?
          'Frog Mode: Underwater / Winter Sleep (100% Cutaneous Skin Respiration)' :
          'Frog Mode: Adult on Land (Pulmonary Lungs + Buccal Pumping)';
      }
    }
    window.renderFrogAyur();
  };

  /* -------------------------------------------------------------
     GLOBAL SIMULATOR DISPATCHER
     ------------------------------------------------------------- */
  window.initSimulatorForSlide = function(slideId, container) {
    if (!container) return;
    switch(slideId) {
      case 1: if (window.switchMacroTab) window.switchMacroTab('carb'); break;
      case 2: if (window.inspectOrgan) window.inspectOrgan('mouth'); break;
      case 3: break;
      case 4: if (window.setPeristalsisPos) window.setPeristalsisPos(150); break;
      case 5: if (window.toggleStomachMucus) window.toggleStomachMucus(); break;
      case 6: break;
      case 7: break;
      case 8: if (window.setWaterExtraction) window.setWaterExtraction(85); break;
      case 9: if (window.stepRuminant) window.stepRuminant(1); break;
      case 10: break;
      case 11: break;
      case 12: break;
      case 13: if (window.setBreathingAction) window.setBreathingAction('inhale'); break;
      case 14: break;
      case 15: if (window.switchAnimalRespTab) window.switchAnimalRespTab('fish'); break;
      case 16: if (window.switchHeritageTab) window.switchHeritageTab('frog'); break;
    }
  };

  function initSimulatorForSlide(slideId, container) {
    window.initSimulatorForSlide(slideId, container);
  }

  window.initSimulators = function() {
    try { if (window.switchMacroTab) window.switchMacroTab('carb'); } catch(e){}
    try { if (window.inspectOrgan) window.inspectOrgan('mouth'); } catch(e){}
    try { if (window.setPeristalsisPos) window.setPeristalsisPos(150); } catch(e){}
    try { if (window.setWaterExtraction) window.setWaterExtraction(85); } catch(e){}
    try { if (window.stepRuminant) window.stepRuminant(1); } catch(e){}
    try { if (window.setBreathingAction) window.setBreathingAction('inhale'); } catch(e){}
    try { if (window.switchAnimalRespTab) window.switchAnimalRespTab('fish'); } catch(e){}
    try { if (window.switchHeritageTab) window.switchHeritageTab('frog'); } catch(e){}
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', window.initSimulators);
  } else {
    setTimeout(window.initSimulators, 50);
  }
})();
'''

with open(".agents/class7_science_life_processes_js.py", "w", encoding="utf-8") as f:
    f.write('# -*- coding: utf-8 -*-\n"""Simulators JS for Class 7 Science Chapter 9: Life Processes in Animals"""\n\nSIMULATOR_JS = r\'\'\'' + js_code + '\'\'\'\n')

print("Generated .agents/class7_science_life_processes_js.py cleanly.")
