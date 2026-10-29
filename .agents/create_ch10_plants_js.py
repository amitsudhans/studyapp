# -*- coding: utf-8 -*-
"""
Generates the JavaScript controller for Chapter 10: Life Processes in Plants.
Strictly zero raw LaTeX commands. Clean Unicode.
"""

def generate_js():
    js_content = r"""
// Master State
let currentSlide = 1;
const totalSlides = 20;
let userAnswers = {};
let checkpointsDone = {};
let speechSynth = window.speechSynthesis;
let speechUtterance = null;
let isSpeaking = false;

// Audio context for sound effects
let audioCtx = null;
function playSound(type) {
    try {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        
        const now = audioCtx.currentTime;
        if (type === 'correct') {
            osc.type = 'sine';
            osc.frequency.setValueAtTime(523.25, now); // C5
            osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.1); // E5
            osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.2); // G5
            gain.gain.setValueAtTime(0.2, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
            osc.start(now);
            osc.stop(now + 0.35);
        } else if (type === 'wrong') {
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(220, now); // A3
            osc.frequency.exponentialRampToValueAtTime(146.83, now + 0.2); // D3
            gain.gain.setValueAtTime(0.2, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
            osc.start(now);
            osc.stop(now + 0.3);
        } else if (type === 'click') {
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(440, now);
            gain.gain.setValueAtTime(0.08, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
            osc.start(now);
            osc.stop(now + 0.08);
        }
    } catch(e) {}
}

// Navigation
function goToSlide(n) {
    if (n < 1 || n > totalSlides) return;
    playSound('click');
    
    // Hide current
    const prevEl = document.getElementById(`slide-${currentSlide}`);
    if (prevEl) prevEl.classList.add('hidden');
    
    currentSlide = n;
    
    // Show new
    const nextEl = document.getElementById(`slide-${currentSlide}`);
    if (nextEl) nextEl.classList.remove('hidden');
    
    // Update navigation controls
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');
    
    if (prevBtn) prevBtn.disabled = (currentSlide === 1);
    
    if (currentSlide === totalSlides) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.classList.remove('hidden');
    } else {
        if (nextBtn) nextBtn.style.display = 'inline-flex';
        if (lastNotice) lastNotice.classList.add('hidden');
    }
    
    // Update slide indicator and progress bar
    const indicator = document.getElementById('slideIndicator');
    if (indicator) indicator.textContent = `${currentSlide} / ${totalSlides}`;
    
    const progress = document.getElementById('progressBar');
    if (progress) progress.style.width = `${(currentSlide / totalSlides) * 100}%`;
    
    // Stop speech if switching slides
    stopSpeech();
    
    // Initialize simulator for this slide if needed
    initSimulator(currentSlide);
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function nextSlide() {
    if (currentSlide < totalSlides) goToSlide(currentSlide + 1);
}

function prevSlide() {
    if (currentSlide > 1) goToSlide(currentSlide - 1);
}

// Checkpoint Answer Handling
function checkCheckpoint(cpId, selectedIdx, correctIdx, explanation) {
    const card = document.getElementById(`cp_card_${cpId}`);
    if (!card) return;
    
    const optBtns = card.querySelectorAll('.cp-option-btn');
    optBtns.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === correctIdx) {
            btn.classList.remove('bg-slate-800', 'border-slate-700');
            btn.classList.add('bg-emerald-900/60', 'border-emerald-500', 'text-emerald-200');
        } else if (idx === selectedIdx && selectedIdx !== correctIdx) {
            btn.classList.remove('bg-slate-800', 'border-slate-700');
            btn.classList.add('bg-rose-900/60', 'border-rose-500', 'text-rose-200');
        }
    });
    
    const feedbackEl = document.getElementById(`cp_feedback_${cpId}`);
    if (feedbackEl) {
        feedbackEl.classList.remove('hidden');
        if (selectedIdx === correctIdx) {
            playSound('correct');
            feedbackEl.className = 'mt-3 p-3 rounded-lg bg-emerald-950/60 border border-emerald-500/40 text-xs text-emerald-200';
            feedbackEl.innerHTML = `<strong class="text-emerald-300 font-bold block mb-1">✓ Correct!</strong>${explanation}`;
        } else {
            playSound('wrong');
            feedbackEl.className = 'mt-3 p-3 rounded-lg bg-rose-950/60 border border-rose-500/40 text-xs text-rose-200';
            feedbackEl.innerHTML = `<strong class="text-rose-300 font-bold block mb-1">✗ Incorrect.</strong>${explanation}`;
        }
    }
}

// Quiz Solution Modal
function openSolutionModal(qNum, questionText, solutionText) {
    playSound('click');
    const modal = document.getElementById('solutionModal');
    const title = document.getElementById('modalTitle');
    const body = document.getElementById('modalBody');
    if (!modal || !title || !body) return;
    
    title.textContent = `Question ${qNum} • Step-by-Step Solution`;
    body.innerHTML = `
        <div class="mb-3 p-3 rounded-lg bg-slate-900 border border-slate-700 text-xs text-slate-200">
            <strong class="text-amber-300 block mb-1">Question:</strong>
            ${questionText}
        </div>
        <div class="p-3 rounded-lg bg-emerald-950/50 border border-emerald-500/30 text-xs text-emerald-200 leading-relaxed">
            <strong class="text-emerald-300 block mb-1">Scientific Derivation:</strong>
            ${solutionText}
        </div>
    `;
    modal.style.display = 'flex';
}

function closeSolutionModal() {
    playSound('click');
    const modal = document.getElementById('solutionModal');
    if (modal) modal.style.display = 'none';
}

// Speech Narration
function toggleSpeech() {
    if (isSpeaking) {
        stopSpeech();
    } else {
        startSpeech();
    }
}

function startSpeech() {
    if (!('speechSynthesis' in window)) return;
    stopSpeech();
    
    const slide = document.getElementById(`slide-${currentSlide}`);
    if (!slide) return;
    
    const title = slide.querySelector('h2') ? slide.querySelector('h2').textContent : '';
    const subtitle = slide.querySelector('h3') ? slide.querySelector('h3').textContent : '';
    const summary = slide.querySelector('.slide-summary') ? slide.querySelector('.slide-summary').textContent : '';
    
    const fullText = `${title}. ${subtitle}. ${summary}`;
    speechUtterance = new SpeechSynthesisUtterance(fullText);
    speechUtterance.rate = 0.95;
    speechUtterance.pitch = 1.0;
    
    speechUtterance.onend = () => {
        isSpeaking = false;
        updateSpeechBtn(false);
    };
    
    speechUtterance.onerror = () => {
        isSpeaking = false;
        updateSpeechBtn(false);
    };
    
    speechSynth.speak(speechUtterance);
    isSpeaking = true;
    updateSpeechBtn(true);
}

function stopSpeech() {
    if (speechSynth && isSpeaking) {
        speechSynth.cancel();
        isSpeaking = false;
        updateSpeechBtn(false);
    }
}

function updateSpeechBtn(speaking) {
    const btn = document.getElementById('narrateBtn');
    if (!btn) return;
    if (speaking) {
        btn.innerHTML = `
            <svg class="w-4 h-4 animate-spin text-amber-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path>
            </svg>
            <span class="text-amber-300 font-semibold text-xs">Mute Narration</span>
        `;
        btn.classList.add('border-amber-500/50', 'bg-amber-950/40');
    } else {
        btn.innerHTML = `
            <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
            </svg>
            <span class="text-slate-300 font-semibold text-xs">Voice Narration</span>
        `;
        btn.classList.remove('border-amber-500/50', 'bg-amber-950/40');
    }
}

// SIMULATOR LOGIC DISPATCHER
function initSimulator(n) {
    if (n === 1) initSim1();
    else if (n === 2) initSim2();
    else if (n === 3) initSim3();
    else if (n === 4) initSim4();
    else if (n === 5) initSim5();
    else if (n === 6) initSim6();
    else if (n === 7) initSim7();
    else if (n === 8) initSim8();
    else if (n === 9) initSim9();
    else if (n === 10) initSim10();
    else if (n === 11) initSim11();
    else if (n === 12) initSim12();
    else if (n === 13) initSim13();
    else if (n === 14) initSim14();
    else if (n === 15) initSim15();
    else if (n === 16) initSim16();
}

// SIM 1: Autotrophic Solar Power Plant
function initSim1() {
    const sunSlider = document.getElementById('sim1_sunSlider');
    const waterSlider = document.getElementById('sim1_waterSlider');
    if (!sunSlider || !waterSlider) return;

    function update() {
        const sun = parseInt(sunSlider.value);
        const water = parseInt(waterSlider.value);
        document.getElementById('sim1_sunVal').textContent = `${sun}%`;
        document.getElementById('sim1_waterVal').textContent = `${water}%`;

        const yieldVal = Math.round((sun * 0.6) + (water * 0.4));
        const bar = document.getElementById('sim1_glucoseBar');
        if (bar) bar.setAttribute('width', (yieldVal * 1.5).toString());
        
        const label = document.getElementById('sim1_yieldText');
        if (label) label.textContent = `${yieldVal}% ${yieldVal > 60 ? 'High Biomass' : yieldVal > 30 ? 'Moderate Growth' : 'Deficient Stunted'}`;

        const rays = document.getElementById('sim1_rays');
        if (rays) rays.setAttribute('opacity', (sun / 100).toString());

        const status = document.getElementById('sim1_status');
        if (status) {
            if (sun > 40 && water > 40) {
                status.textContent = 'Optimal autotrophic state: High photosynthetic rate generates abundant glucose and O₂ sustaining the food chain.';
                status.className = 'text-xs p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30 text-emerald-200 text-center font-medium';
            } else if (sun <= 40) {
                status.textContent = 'Light deficit: Insufficient photon capture limits ATP synthesis and photolysis of water.';
                status.className = 'text-xs p-2.5 rounded bg-amber-950/40 border border-amber-500/30 text-amber-200 text-center font-medium';
            } else {
                status.textContent = 'Water deficit: Low soil moisture forces stomata to close, shutting off carbon dioxide intake.';
                status.className = 'text-xs p-2.5 rounded bg-rose-950/40 border border-rose-500/30 text-rose-200 text-center font-medium';
            }
        }
    }
    sunSlider.oninput = update;
    waterSlider.oninput = update;
}

// SIM 2: The Four-Chamber Growth Laboratory
function initSim2() {
    const slider = document.getElementById('sim2_daySlider');
    if (!slider) return;

    slider.oninput = function() {
        const day = parseInt(slider.value);
        document.getElementById('sim2_dayLabel').textContent = `Day ${day}`;

        // Pot A height (grows up to 22cm)
        const hA = Math.round(5 + (day * 1.2));
        document.getElementById('sim2_potA_desc').textContent = `Height: ${hA} cm (Vigorous)`;

        // Pot B wilting
        const descB = document.getElementById('sim2_potB_desc');
        if (descB) descB.textContent = day > 4 ? 'Wilted / Drooping' : 'Slight Turgor Loss';

        // Pot C etiolation
        const descC = document.getElementById('sim2_potC_desc');
        const hC = Math.round(5 + (day * 1.0));
        if (descC) descC.textContent = day > 3 ? `Etiolated: ${hC} cm (Yellow/Thin)` : 'Normal Sprout';
    };
}

// SIM 3: Leaf Microscopic Layer Dissector
function initSim3() {
    const btnAll = document.getElementById('sim3_btn_all');
    const btnPalisade = document.getElementById('sim3_btn_palisade');
    const btnVein = document.getElementById('sim3_btn_vein');
    const btnStoma = document.getElementById('sim3_btn_stoma');
    const info = document.getElementById('sim3_info');

    function resetHighlights() {
        const layers = ['sim3_cuticle', 'sim3_upperEpidermis', 'sim3_palisade', 'sim3_spongy', 'sim3_lowerEpidermis'];
        layers.forEach(id => {
            const el = document.getElementById(id);
            if (el) el.setAttribute('opacity', '1');
        });
    }

    if (btnAll) btnAll.onclick = () => {
        resetHighlights();
        if (info) info.innerHTML = '<strong class="text-emerald-400">All Layers Visible:</strong> From the top waxy cuticle to lower stomata, every tissue layer is optimized for solar capture and vascular circulation.';
    };

    if (btnPalisade) btnPalisade.onclick = () => {
        resetHighlights();
        const pal = document.getElementById('sim3_palisade');
        if (pal) pal.setAttribute('opacity', '1');
        if (info) info.innerHTML = '<strong class="text-emerald-300">Palisade Mesophyll:</strong> Packed with vertically oriented columnar cells containing the greatest density of chlorophyll-rich chloroplasts for maximum photon absorption.';
    };

    if (btnVein) btnVein.onclick = () => {
        resetHighlights();
        if (info) info.innerHTML = '<strong class="text-cyan-300">Vascular Vein:</strong> Upper red xylem vessels deliver soil water; lower blue phloem sieve tubes export synthesized sucrose sugars to roots and flowers.';
    };

    if (btnStoma) btnStoma.onclick = () => {
        resetHighlights();
        if (info) info.innerHTML = '<strong class="text-amber-300">Stomatal Pores:</strong> Located on the lower epidermis to reduce evaporative water loss while allowing atmospheric CO₂ to diffuse into spongy air spaces.';
    };
}

// SIM 4: Starch Laboratory Workbench (4-Step Stepper)
let sim4_step = 1;
function initSim4() {
    const prev = document.getElementById('sim4_prevBtn');
    const next = document.getElementById('sim4_nextBtn');
    const indicator = document.getElementById('sim4_stepIndicator');
    const desc = document.getElementById('sim4_stepDesc');

    const steps = [
        {
            num: 1,
            title: "Step 1 of 4: Boiling Water",
            desc: "<strong class='text-amber-400'>Step 1 (Water Boiling):</strong> The leaf is boiled in water for 2 minutes to disrupt cell membranes and halt all enzymatic activity, making the tissue permeable to reagents."
        },
        {
            num: 2,
            title: "Step 2 of 4: Ethanol Water Bath",
            desc: "<strong class='text-emerald-400'>Step 2 (Ethanol Decolourisation):</strong> The leaf is boiled inside a test tube of ethanol placed in a water bath. Chlorophyll dissolves into the alcohol, bleaching the leaf to a pale creamy-white."
        },
        {
            num: 3,
            title: "Step 3 of 4: Warm Water Rinse",
            desc: "<strong class='text-cyan-400'>Step 3 (Warm Water Rinse):</strong> Alcohol makes the decolourised leaf brittle. Rinsing in warm water softens the cellulose walls and clears away residual ethanol."
        },
        {
            num: 4,
            title: "Step 4 of 4: Iodine Solution Test",
            desc: "<strong class='text-blue-400'>Step 4 (Iodine Reaction):</strong> Dropping dilute amber iodine solution onto the leaf produces an intense <strong class='text-blue-400'>blue-black</strong> coloration, confirming that starch was manufactured during photosynthesis!"
        }
    ];

    function showStep(s) {
        sim4_step = s;
        if (prev) prev.disabled = (sim4_step === 1);
        if (next) next.disabled = (sim4_step === 4);
        if (indicator) indicator.textContent = steps[sim4_step - 1].title;
        if (desc) desc.innerHTML = steps[sim4_step - 1].desc;

        for (let i = 1; i <= 4; i++) {
            const el = document.getElementById(`sim4_stage${i}`);
            if (el) el.style.display = (i === sim4_step) ? 'block' : 'none';
        }
    }

    if (prev) prev.onclick = () => { if (sim4_step > 1) showStep(sim4_step - 1); };
    if (next) next.onclick = () => { if (sim4_step < 4) showStep(sim4_step + 1); };
    showStep(1);
}

// SIM 5: Moll's Half-Leaf Gas Chamber Simulator
let sim5_hasKOH = true;
function initSim5() {
    const btnKOH = document.getElementById('sim5_toggleKOH');
    const btnTest = document.getElementById('sim5_runTest');
    const btnReset = document.getElementById('sim5_reset');
    const leafOuter = document.getElementById('sim5_leafOuter');
    const leafInner = document.getElementById('sim5_leafInner');
    const kohLayer = document.getElementById('sim5_koh_layer');
    const kohText = document.getElementById('sim5_koh_text');
    const resultGroup = document.getElementById('sim5_resultGroup');
    const feedback = document.getElementById('sim5_feedback');

    if (btnKOH) btnKOH.onclick = () => {
        sim5_hasKOH = !sim5_hasKOH;
        if (sim5_hasKOH) {
            btnKOH.textContent = "Remove KOH (Control Setup)";
            btnKOH.className = "px-3 py-1.5 rounded bg-rose-700 text-white hover:bg-rose-600 text-xs font-semibold transition";
            if (kohLayer) kohLayer.style.display = 'block';
            if (kohText) kohText.textContent = "KOH Pellets (Absorbing all CO₂)";
        } else {
            btnKOH.textContent = "Insert KOH Pellets";
            btnKOH.className = "px-3 py-1.5 rounded bg-slate-700 text-slate-200 hover:bg-slate-600 text-xs font-semibold transition";
            if (kohLayer) kohLayer.style.display = 'none';
            if (kohText) kohText.textContent = "No KOH (Air contains normal CO₂)";
        }
    };

    if (btnTest) btnTest.onclick = () => {
        playSound('click');
        if (resultGroup) resultGroup.style.display = 'block';
        if (leafOuter) leafOuter.setAttribute('fill', '#1e3a8a'); // Blue-black

        if (sim5_hasKOH) {
            if (leafInner) leafInner.setAttribute('fill', '#b45309'); // Brown (no starch)
            if (feedback) feedback.innerHTML = '<strong class="text-emerald-400">Result:</strong> The outer half with CO₂ turns <strong class="text-blue-400">blue-black</strong>. The inner half starved of CO₂ by KOH remains <strong class="text-amber-500">brown</strong>. CO₂ is mandatory!';
        } else {
            if (leafInner) leafInner.setAttribute('fill', '#1e3a8a'); // Both blue-black
            if (feedback) feedback.innerHTML = '<strong class="text-emerald-400">Control Result:</strong> Without KOH, atmospheric CO₂ was available inside the bottle too, so both halves turn <strong class="text-blue-400">blue-black</strong>.';
        }
    };

    if (btnReset) btnReset.onclick = () => {
        if (leafOuter) leafOuter.setAttribute('fill', '#10b981');
        if (leafInner) leafInner.setAttribute('fill', '#10b981');
        if (resultGroup) resultGroup.style.display = 'none';
        if (feedback) feedback.textContent = "Click 'Apply Iodine Starch Test' to observe the starch synthesis boundary.";
    };
}

// SIM 6: Photosynthesis Molecular Reaction Engine
function initSim6() {
    const lightSlider = document.getElementById('sim6_lightSlider');
    const co2Slider = document.getElementById('sim6_co2Slider');
    if (!lightSlider || !co2Slider) return;

    function update() {
        const light = parseInt(lightSlider.value);
        const co2 = parseInt(co2Slider.value);
        document.getElementById('sim6_lightVal').textContent = `${light}%`;
        document.getElementById('sim6_co2Val').textContent = co2 > 70 ? 'High (0.08%)' : co2 > 30 ? 'Normal (0.04%)' : 'Deficient (<0.01%)';

        const photonText = document.getElementById('sim6_photonState');
        if (photonText) {
            photonText.textContent = light > 20 ? '⚡ Photons ⚡' : '🌑 Dark';
            photonText.setAttribute('fill', light > 20 ? '#fef08a' : '#64748b');
        }

        const status = document.getElementById('sim6_status');
        if (status) {
            if (light < 20) {
                status.textContent = 'Photolysis stalled: In darkness, light-dependent water splitting halts completely; no oxygen is evolved.';
            } else if (co2 < 30) {
                status.textContent = 'Substrate limitation: Insufficient carbon dioxide limits glucose production despite abundant photons.';
            } else {
                status.textContent = 'Optimal stoichiometry: 6 molecules of CO₂ + 6 molecules of H₂O yield exactly 1 glucose molecule and 6 oxygen molecules.';
            }
        }
    }
    lightSlider.oninput = update;
    co2Slider.oninput = update;
}

// SIM 7: Ingenhousz Hydrilla Photometer
function initSim7() {
    const distSlider = document.getElementById('sim7_distSlider');
    const igniteBtn = document.getElementById('sim7_igniteBtn');
    const splinterGroup = document.getElementById('sim7_splinterGroup');
    const rateText = document.getElementById('sim7_bubbleRate');

    if (distSlider) {
        distSlider.oninput = () => {
            const dist = parseInt(distSlider.value);
            document.getElementById('sim7_distVal').textContent = `${dist} cm`;
            // Inverse square approximation for bubble rate
            const rate = Math.round(1800 / (dist + 10));
            if (rateText) rateText.textContent = `${rate} Bubbles / min`;
            
            const cone = document.getElementById('sim7_lightCone');
            if (cone) cone.setAttribute('opacity', ((90 - dist) / 100).toString());
        };
    }

    if (igniteBtn) {
        igniteBtn.onclick = () => {
            playSound('correct');
            if (splinterGroup) {
                splinterGroup.style.display = 'block';
                setTimeout(() => {
                    splinterGroup.style.display = 'none';
                }, 3500);
            }
        };
    }
}

// SIM 8: Microscopic Guard Cell Stomatal Aperture
function initSim8() {
    const slider = document.getElementById('sim8_turgorSlider');
    const toggle = document.getElementById('sim8_toggleLight');
    const pore = document.getElementById('sim8_pore');
    const poreLabel = document.getElementById('sim8_poreLabel');
    const arrows = document.getElementById('sim8_arrows');
    const status = document.getElementById('sim8_status');
    let isDay = true;

    function update() {
        const turgor = parseInt(slider.value);
        document.getElementById('sim8_turgorVal').textContent = `${turgor}% (${turgor > 50 ? 'Turgid' : 'Flaccid'})`;

        const rx = Math.round(turgor * 0.22);
        if (pore) pore.setAttribute('rx', rx.toString());

        if (turgor > 30) {
            if (poreLabel) { poreLabel.textContent = "OPEN PORE"; poreLabel.setAttribute('fill', '#38bdf8'); }
            if (arrows) arrows.style.display = 'block';
            if (status) status.innerHTML = '<strong class="text-emerald-400">Turgid State:</strong> Water inflates guard cells; their inelastic thick inner walls resist stretching while elastic outer walls bow outward, opening the central pore for CO₂ uptake.';
        } else {
            if (poreLabel) { poreLabel.textContent = "CLOSED"; poreLabel.setAttribute('fill', '#94a3b8'); }
            if (arrows) arrows.style.display = 'none';
            if (status) status.innerHTML = '<strong class="text-amber-400">Flaccid State:</strong> Water loss causes guard cells to go limp; thick inner walls spring together, sealing the pore to prevent desiccation.';
        }
    }

    if (slider) slider.oninput = update;
    if (toggle) {
        toggle.onclick = () => {
            isDay = !isDay;
            if (isDay) {
                toggle.textContent = "☀️ Daylight (Open)";
                toggle.className = "px-3 py-1.5 rounded bg-amber-600 text-white text-xs font-semibold hover:bg-amber-500 transition";
                if (slider) { slider.value = 100; update(); }
            } else {
                toggle.textContent = "🌑 Night Darkness (Closed)";
                toggle.className = "px-3 py-1.5 rounded bg-slate-700 text-slate-300 text-xs font-semibold hover:bg-slate-600 transition";
                if (slider) { slider.value = 10; update(); }
            }
        };
    }
}

// SIM 9: Stem Cross-Section Vascular Scanner
function initSim9() {
    const btnXylem = document.getElementById('sim9_toggleXylem');
    const btnPhloem = document.getElementById('sim9_togglePhloem');
    const info = document.getElementById('sim9_info');

    if (btnXylem) btnXylem.onclick = () => {
        playSound('click');
        if (info) info.innerHTML = '<strong class="text-rose-400">Xylem Active:</strong> Dead, lignified hollow tubes conducting water and dissolved soil minerals strictly upward from roots to leaves via transpiration suction.';
    };

    if (btnPhloem) btnPhloem.onclick = () => {
        playSound('click');
        if (info) info.innerHTML = '<strong class="text-cyan-400">Phloem Active:</strong> Living sieve tube cells translocating soluble sucrose and amino acids bidirectionally (upward to buds and downward to roots).';
    };
}

// SIM 10: Root Hair Osmosis & Mineral Active Transport Lab
function initSim10() {
    const soilSlider = document.getElementById('sim10_soilWaterSlider');
    const soluteSlider = document.getElementById('sim10_soluteSlider');
    const arrow = document.getElementById('sim10_flowArrow');
    const status = document.getElementById('sim10_status');

    function update() {
        const sw = parseInt(soilSlider.value);
        const sol = parseInt(soluteSlider.value);
        document.getElementById('sim10_soilWaterVal').textContent = `${sw}% (${sw > 60 ? 'Moist' : sw > 30 ? 'Moderate' : 'Dry'})`;
        document.getElementById('sim10_soluteVal').textContent = sol > 3 ? 'High (Steep Gradient)' : 'Low (Weak Gradient)';

        if (sw > 30 && sol > 2) {
            if (arrow) arrow.setAttribute('stroke-width', '5');
            if (status) status.textContent = "Active osmosis: Dilute soil moisture diffuses across root hair cell membranes into concentrated vacuoles, driving water into central xylem.";
        } else {
            if (arrow) arrow.setAttribute('stroke-width', '1.5');
            if (status) status.textContent = "Osmotic stagnation: Insufficient soil water or weak solute gradient restricts water uptake, risking plant wilting.";
        }
    }

    if (soilSlider) soilSlider.oninput = update;
    if (soluteSlider) soluteSlider.oninput = update;
}

// SIM 11: The Balsam Plant Red Ink Transpiration Column
function initSim11() {
    const windSlider = document.getElementById('sim11_windSlider');
    const tempSlider = document.getElementById('sim11_tempSlider');
    const dyeCol = document.getElementById('sim11_dyeCol');
    const flower = document.getElementById('sim11_flower');

    function update() {
        const wind = parseInt(windSlider.value);
        const temp = parseInt(tempSlider.value);
        const windNames = ['Zero Calm', 'Light Breeze', 'Medium (Speed 2)', 'Gale Wind'];
        document.getElementById('sim11_windVal').textContent = windNames[wind];
        document.getElementById('sim11_tempVal').textContent = `${temp}°C ${temp > 30 ? 'Hot' : 'Warm'}`;

        const ascentRate = (wind * 25) + ((temp - 15) * 3);
        const topY = Math.max(60, 210 - (ascentRate * 1.5));
        if (dyeCol) dyeCol.setAttribute('y2', topY.toString());

        if (topY <= 80 && flower) {
            flower.setAttribute('fill', '#f43f5e'); // Deep pink
        } else if (flower) {
            flower.setAttribute('fill', '#fda4af'); // Light pink
        }
    }

    if (windSlider) windSlider.oninput = update;
    if (tempSlider) tempSlider.oninput = update;
}

// SIM 12: Source-to-Sink Phloem Translocation Model
function initSim12() {
    const btnSeason = document.getElementById('sim12_btnSeason');
    const btnGirdle = document.getElementById('sim12_btnGirdle');
    const btnReset = document.getElementById('sim12_btnReset');
    const girdleCut = document.getElementById('sim12_girdleCut');
    const swelling = document.getElementById('sim12_swelling');
    const status = document.getElementById('sim12_status');
    let isSummer = true;
    let isGirdled = false;

    if (btnSeason) {
        btnSeason.onclick = () => {
            isSummer = !isSummer;
            btnSeason.textContent = isSummer ? "Mode: Summer Storage (Leaf → Tuber)" : "Mode: Spring Sprouting (Tuber → Bud)";
            if (status) status.textContent = isSummer ?
                "Summer: Active leaves export sucrose downward to roots and storage tubers." :
                "Spring: Stored starch in underground tubers converts to sucrose, flowing upward to fuel opening leaf buds.";
        };
    }

    if (btnGirdle) {
        btnGirdle.onclick = () => {
            playSound('wrong');
            isGirdled = true;
            if (girdleCut) girdleCut.style.display = 'block';
            if (swelling) swelling.style.display = 'block';
            if (status) status.innerHTML = '<strong class="text-rose-400">Girdling Cut Applied:</strong> Outer bark phloem is removed. Downward sugar flow is blocked, causing dramatic tissue swelling immediately above the cut.';
        };
    }

    if (btnReset) {
        btnReset.onclick = () => {
            isGirdled = false;
            if (girdleCut) girdleCut.style.display = 'none';
            if (swelling) swelling.style.display = 'none';
            if (status) status.textContent = "Phloem highway restored to continuous operation.";
        };
    }
}

// SIM 13: 24-Hour Diurnal Gas Exchange Balance
function initSim13() {
    const slider = document.getElementById('sim13_timeSlider');
    const timeVal = document.getElementById('sim13_timeVal');
    const sky = document.getElementById('sim13_sky');
    const celestial = document.getElementById('sim13_celestial');
    const celestialLabel = document.getElementById('sim13_celestialLabel');
    const photoRate = document.getElementById('sim13_photoRate');
    const netGas = document.getElementById('sim13_netGas');
    const compStatus = document.getElementById('sim13_compStatus');

    if (!slider) return;

    slider.oninput = () => {
        const h = parseInt(slider.value);
        timeVal.textContent = `${h.toString().padStart(2, '0')}:00`;

        if (h >= 8 && h <= 16) { // Midday
            if (sky) sky.setAttribute('fill', '#0284c7');
            if (celestial) { celestial.setAttribute('fill', '#fef08a'); celestial.setAttribute('cx', '270'); }
            if (celestialLabel) celestialLabel.textContent = "Bright Daylight Sun";
            if (photoRate) photoRate.textContent = "100% (High)";
            if (netGas) { netGas.textContent = "NET: Absorbing CO₂, Releasing O₂"; netGas.setAttribute('fill', '#38bdf8'); }
            if (compStatus) compStatus.textContent = "Photosynthesis >> Respiration";
        } else if (h === 6 || h === 7 || h === 17 || h === 18) { // Compensation points (dawn/dusk)
            if (sky) sky.setAttribute('fill', '#b45309');
            if (celestial) { celestial.setAttribute('fill', '#f97316'); celestial.setAttribute('cx', h <= 7 ? '100' : '440'); }
            if (celestialLabel) celestialLabel.textContent = "Twilight / Horizon";
            if (photoRate) photoRate.textContent = "10% (Matches Respiration)";
            if (netGas) { netGas.textContent = "NET GAS EXCHANGE: EXACTLY ZERO"; netGas.setAttribute('fill', '#fde047'); }
            if (compStatus) compStatus.textContent = "⚡ COMPENSATION POINT REACHED ⚡";
        } else { // Night
            if (sky) sky.setAttribute('fill', '#090d16');
            if (celestial) { celestial.setAttribute('fill', '#f8fafc'); celestial.setAttribute('cx', '270'); }
            if (celestialLabel) celestialLabel.textContent = "Night Crescent Moon";
            if (photoRate) photoRate.textContent = "0% (Zero Light)";
            if (netGas) { netGas.textContent = "NET: Absorbing O₂, Releasing CO₂"; netGas.setAttribute('fill', '#f43f5e'); }
            if (compStatus) compStatus.textContent = "Respiration Only (No Photosynthesis)";
        }
    };
}

// SIM 14: Respirometer Germination Lab
function initSim14() {
    const btnToggle = document.getElementById('sim14_btnToggleSeeds');
    const btnLime = document.getElementById('sim14_btnLimeWater');
    const riseLine = document.getElementById('sim14_riseLine');
    const tempDisplay = document.getElementById('sim14_tempDisplay');
    const seeds = document.getElementById('sim14_seeds');
    const status = document.getElementById('sim14_status');
    let isLive = true;

    if (btnToggle) {
        btnToggle.onclick = () => {
            isLive = !isLive;
            if (isLive) {
                btnToggle.textContent = "Specimen: Live Germinating Seeds";
                btnToggle.className = "px-3 py-1.5 rounded bg-emerald-700 text-white hover:bg-emerald-600 text-xs font-semibold transition";
                if (seeds) seeds.setAttribute('fill', '#d97706');
                if (riseLine) riseLine.setAttribute('y2', '100');
                if (tempDisplay) { tempDisplay.textContent = "+3.5°C Rise"; tempDisplay.setAttribute('fill', '#f87171'); }
                if (status) status.textContent = "Live seeds respire actively: O₂ consumption creates suction, raising the water level. Heat is generated!";
            } else {
                btnToggle.textContent = "Specimen: Boiled Dead Seeds (Control)";
                btnToggle.className = "px-3 py-1.5 rounded bg-slate-700 text-slate-200 hover:bg-slate-600 text-xs font-semibold transition";
                if (seeds) seeds.setAttribute('fill', '#78350f');
                if (riseLine) riseLine.setAttribute('y2', '170'); // No rise
                if (tempDisplay) { tempDisplay.textContent = "0.0°C (No Rise)"; tempDisplay.setAttribute('fill', '#94a3b8'); }
                if (status) status.textContent = "Dead seeds control: Cellular enzymes denatured. Zero respiration, zero water level rise, zero temperature change.";
            }
        };
    }

    if (btnLime) {
        btnLime.onclick = () => {
            playSound('correct');
            if (isLive) {
                if (status) status.innerHTML = '<strong class="text-emerald-300">Lime Water Test:</strong> Gas passed into Ca(OH)₂ turns <strong class="text-slate-100 font-bold">milky white</strong> precipitate (CaCO₃), confirming carbon dioxide production by live seeds!';
            } else {
                if (status) status.innerHTML = '<strong class="text-slate-400">Lime Water Test:</strong> Lime water remains completely clear with boiled dead seeds. No CO₂ emitted.';
            }
        };
    }
}

// SIM 15: Soil Aeration & Mangrove Pneumatophore Simulator
function initSim15() {
    const slider = document.getElementById('sim15_floodSlider');
    const floodWater = document.getElementById('sim15_floodWater');
    const potDesc = document.getElementById('sim15_potDesc');
    const airPockets = document.getElementById('sim15_airPockets');
    const roots = document.getElementById('sim15_roots');
    const status = document.getElementById('sim15_status');

    if (!slider) return;

    slider.oninput = () => {
        const val = parseInt(slider.value);
        document.getElementById('sim15_levelText').textContent = val > 75 ? 'Flooded / Waterlogged' : val > 25 ? 'Moist Aerated' : 'Dry Soil';
        if (floodWater) floodWater.setAttribute('opacity', (val / 100).toString());

        if (val > 70) {
            if (airPockets) airPockets.style.display = 'none';
            if (roots) roots.setAttribute('stroke', '#78350f'); // Brown rotting
            if (potDesc) { potDesc.textContent = "Asphyxiation! Roots rot without soil O₂"; potDesc.className = "text-[11px] text-rose-400 font-semibold text-center"; }
            if (status) status.textContent = "Waterlogged soil displaces all air pockets. Terrestrial plant roots suffocate and rot. Mangroves survive using aerial pneumatophores!";
        } else {
            if (airPockets) airPockets.style.display = 'block';
            if (roots) roots.setAttribute('stroke', '#fde047'); // Healthy yellow-white
            if (potDesc) { potDesc.textContent = "Aerated: Roots breathe soil O₂ normally"; potDesc.className = "text-[11px] text-emerald-400 font-semibold text-center"; }
            if (status) status.textContent = "Optimal aeration: Root hairs absorb dissolved oxygen from soil air pockets to power mineral transport.";
        }
    };
}

// SIM 16: Bose Crescograph & Parashara Herbal Anatomy
function initSim16() {
    const btnStim = document.getElementById('sim16_btnStimulant');
    const btnPoison = document.getElementById('sim16_btnPoison');
    const btnMag = document.getElementById('sim16_btnMag');
    const wave = document.getElementById('sim16_traceWave');
    const magText = document.getElementById('sim16_magText');
    const status = document.getElementById('sim16_status');
    let highMag = false;

    if (btnStim) {
        btnStim.onclick = () => {
            playSound('correct');
            if (wave) wave.setAttribute('stroke', '#34d399');
            if (status) status.innerHTML = '<strong class="text-emerald-400">Warm Stimulant Applied:</strong> Crescograph records elevated pulsation frequency and accelerated growth rate. Plant tissues demonstrate heightened vitality!';
        };
    }

    if (btnPoison) {
        btnPoison.onclick = () => {
            playSound('wrong');
            if (wave) wave.setAttribute('stroke', '#f43f5e');
            if (status) status.innerHTML = '<strong class="text-rose-400">Anesthetic (Ether) Applied:</strong> Cellular pulsation flattens into an inert line. Bose proved plants enter unconscious sedation, just like animals!';
        };
    }

    if (btnMag) {
        btnMag.onclick = () => {
            highMag = !highMag;
            if (magText) magText.textContent = highMag ? "Magnification: 100,000×" : "Magnification: 10,000×";
            btnMag.textContent = highMag ? "Toggle Magnification (10,000×)" : "Toggle Magnification (100,000×)";
        };
    }
}

// Window Onload Initialization
window.addEventListener('DOMContentLoaded', () => {
    goToSlide(1);
});
"""

    with open(".agents/class7_science_plants_js.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Auto-generated JS controller for Class 7 Science Chapter 10: Life Processes in Plants."""\n\n')
        f.write("JAVASCRIPT_CODE = r'''" + js_content + "'''\n")

    print("Successfully generated class7_science_plants_js.py.")

if __name__ == "__main__":
    generate_js()

