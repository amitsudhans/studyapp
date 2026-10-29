# -*- coding: utf-8 -*-
"""Auto-generated JS controller for Class 7 Science Chapter 11: Light: Shadows and Reflections."""

JAVASCRIPT_CODE = r'''
// Master State
let currentSlide = 1;
const totalSlides = 20;
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

// SIMULATOR DISPATCHER
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

// SIM 1: Luminous vs Non-Luminous Stage
function initSim1() {
    let roomLit = true;
    let currentObj = 'book'; // book, mirror, candle, firefly

    const btnLight = document.getElementById('sim1_btnToggleLight');
    const btnBook = document.getElementById('sim1_btnBook');
    const btnMirror = document.getElementById('sim1_btnMirror');
    const btnCandle = document.getElementById('sim1_btnCandle');
    const btnFirefly = document.getElementById('sim1_btnFirefly');

    function update() {
        const bg = document.getElementById('sim1_roomBg');
        const lamp = document.getElementById('sim1_lampBulb');
        const rays = document.getElementById('sim1_rayLines');
        const objShape = document.getElementById('sim1_objShape');
        const objLabel = document.getElementById('sim1_objLabel');
        const visTag = document.getElementById('sim1_visibilityTag');
        const status = document.getElementById('sim1_status');

        if (roomLit) {
            if (bg) bg.setAttribute('fill', '#0f172a');
            if (lamp) lamp.setAttribute('fill', '#fef08a');
            if (btnLight) {
                btnLight.textContent = "💡 Room Light: ON (Lit)";
                btnLight.className = "w-full py-2 rounded bg-amber-600 text-white text-xs font-bold hover:bg-amber-500 transition";
            }
        } else {
            if (bg) bg.setAttribute('fill', '#020617');
            if (lamp) lamp.setAttribute('fill', '#334155');
            if (btnLight) {
                btnLight.textContent = "🌑 Room Light: OFF (Dark)";
                btnLight.className = "w-full py-2 rounded bg-slate-800 text-slate-300 text-xs font-bold hover:bg-slate-700 transition";
            }
        }

        const isLuminous = (currentObj === 'candle' || currentObj === 'firefly');

        // Configure Object appearance
        if (currentObj === 'book') {
            if (objShape) { objShape.setAttribute('fill', '#3b82f6'); objShape.setAttribute('stroke', '#1d4ed8'); }
            if (objLabel) objLabel.textContent = "Book";
        } else if (currentObj === 'mirror') {
            if (objShape) { objShape.setAttribute('fill', '#38bdf8'); objShape.setAttribute('stroke', '#0284c7'); }
            if (objLabel) objLabel.textContent = "Mirror";
        } else if (currentObj === 'candle') {
            if (objShape) { objShape.setAttribute('fill', '#f59e0b'); objShape.setAttribute('stroke', '#ef4444'); }
            if (objLabel) objLabel.textContent = "🔥 Candle";
        } else if (currentObj === 'firefly') {
            if (objShape) { objShape.setAttribute('fill', '#10b981'); objShape.setAttribute('stroke', '#34d399'); }
            if (objLabel) objLabel.textContent = "✨ Firefly";
        }

        // Visibility rule: Visible if luminous OR if room is lit
        const isVisible = isLuminous || roomLit;

        if (isVisible) {
            if (visTag) {
                visTag.textContent = isLuminous ? "Status: VISIBLE (Emits own light!)" : "Status: VISIBLE (Reflects room light)";
                visTag.className = "text-[11px] text-emerald-400 font-mono mt-1 text-center font-bold";
            }
            if (rays) rays.style.display = 'block';
            if (objShape) objShape.style.opacity = '1';
            if (status) status.textContent = isLuminous ?
                "Luminous object: Emits photons independently. It remains visible even in pitch darkness!" :
                "Non-luminous reflector: Photons from the ceiling bulb strike the object and reflect into the eye, making it visible.";
        } else {
            if (visTag) {
                visTag.textContent = "Status: INVISIBLE (Zero photons reach eye)";
                visTag.className = "text-[11px] text-rose-400 font-mono mt-1 text-center font-bold";
            }
            if (rays) rays.style.display = 'none';
            if (objShape) objShape.style.opacity = '0.05';
            if (status) status.textContent = "In the dark, non-luminous objects emit no light of their own and reflect nothing, rendering them totally invisible.";
        }
    }

    if (btnLight) btnLight.onclick = () => { roomLit = !roomLit; update(); };
    if (btnBook) btnBook.onclick = () => { currentObj = 'book'; update(); };
    if (btnMirror) btnMirror.onclick = () => { currentObj = 'mirror'; update(); };
    if (btnCandle) btnCandle.onclick = () => { currentObj = 'candle'; update(); };
    if (btnFirefly) btnFirefly.onclick = () => { currentObj = 'firefly'; update(); };
}

// SIM 2: Sun-Earth-Moon Cosmic Reflector Orbit
function initSim2() {
    const slider = document.getElementById('sim2_angleSlider');
    if (!slider) return;

    slider.oninput = () => {
        const deg = parseInt(slider.value);
        const rad = (deg * Math.PI) / 180;

        // Moon Orbit position: cx = 180 + 75*cos(rad), cy = 110 + 75*sin(rad)
        const mx = Math.round(180 + 75 * Math.cos(rad));
        const my = Math.round(110 + 75 * Math.sin(rad));

        const moonBody = document.getElementById('sim2_moonBody');
        if (moonBody) moonBody.setAttribute('transform', `translate(${mx}, ${my})`);

        // Phase calculations
        const readout = document.getElementById('sim2_angleVal');
        const phaseName = document.getElementById('sim2_phaseName');
        const phaseShape = document.getElementById('sim2_phaseShape');

        let name = "Moon Phase";
        if (deg >= 350 || deg <= 10) name = "New Moon (Dark)";
        else if (deg > 10 && deg < 80) name = "Waxing Crescent";
        else if (deg >= 80 && deg <= 100) name = "First Quarter (Half)";
        else if (deg > 100 && deg < 170) name = "Waxing Gibbous";
        else if (deg >= 170 && deg <= 190) name = "Full Moon (100% Lit)";
        else if (deg > 190 && deg < 260) name = "Waning Gibbous";
        else if (deg >= 260 && deg <= 280) name = "Third Quarter (Half)";
        else name = "Waning Crescent";

        if (readout) readout.textContent = `${deg}° (${name})`;
        if (phaseName) phaseName.textContent = name;

        // Update lunar phase silhouette
        if (phaseShape) {
            if (deg >= 170 && deg <= 190) { // Full Moon
                phaseShape.setAttribute('d', 'M 30 4 A 26 26 0 1 1 29.9 4 Z');
                phaseShape.setAttribute('fill', '#f8fafc');
            } else if (deg >= 350 || deg <= 10) { // New Moon
                phaseShape.setAttribute('d', 'M 30 4 A 26 26 0 0 0 30 4 Z');
                phaseShape.setAttribute('fill', '#090d16');
            } else if (deg > 10 && deg < 170) { // Waxing
                phaseShape.setAttribute('d', 'M 30 4 A 26 26 0 0 1 30 56 A 14 26 0 0 0 30 4 Z');
                phaseShape.setAttribute('fill', '#f8fafc');
            } else { // Waning
                phaseShape.setAttribute('d', 'M 30 4 A 26 26 0 0 0 30 56 A 14 26 0 0 1 30 4 Z');
                phaseShape.setAttribute('fill', '#f8fafc');
            }
        }
    };
}

// SIM 3: The Three Cardboard Pinholes Alignment Rig
function initSim3() {
    const slider = document.getElementById('sim3_offsetSlider');
    const cardB = document.getElementById('sim3_cardB');
    const beam2 = document.getElementById('sim3_beam2');
    const screenSpot = document.getElementById('sim3_screenSpot');
    const readout = document.getElementById('sim3_offsetVal');
    const status = document.getElementById('sim3_status');

    if (!slider) return;

    slider.oninput = () => {
        const offset = parseInt(slider.value);
        if (cardB) cardB.setAttribute('transform', `translate(280, ${80 + offset})`);

        if (offset === 0) {
            if (readout) { readout.textContent = "0 mm (Collinear Perfect)"; readout.className = "text-emerald-400 font-mono font-bold"; }
            if (beam2) beam2.style.display = 'block';
            if (screenSpot) screenSpot.style.display = 'block';
            if (status) {
                status.textContent = "Collinear alignment achieved! Light travels in a straight line through all three pinholes, forming a bright golden spot on the screen.";
                status.className = "text-xs p-2.5 rounded bg-emerald-950/40 border border-emerald-500/30 text-emerald-200 text-center font-medium";
            }
        } else {
            if (readout) { readout.textContent = `${offset > 0 ? '+' : ''}${offset} mm (Displaced)`; readout.className = "text-rose-400 font-mono font-bold"; }
            if (beam2) beam2.style.display = 'none';
            if (screenSpot) screenSpot.style.display = 'none';
            if (status) {
                status.textContent = "Alignment broken! Light cannot curve around the displaced cardboard B. The straight ray is blocked and the spot vanishes.";
                status.className = "text-xs p-2.5 rounded bg-rose-950/40 border border-rose-500/30 text-rose-200 text-center font-medium";
            }
        }
    };
}

// SIM 4: Straight vs Bent Pipe Visualizer
function initSim4() {
    const btnStraight = document.getElementById('sim4_btnStraight');
    const btnBent = document.getElementById('sim4_btnBent');
    const pipeBody = document.getElementById('sim4_pipeBody');
    const pipeLumen = document.getElementById('sim4_pipeLumen');
    const beam = document.getElementById('sim4_beam');
    const flameIcon = document.getElementById('sim4_flameIcon');
    const viewText = document.getElementById('sim4_viewText');
    const status = document.getElementById('sim4_status');

    if (btnStraight) {
        btnStraight.onclick = () => {
            playSound('correct');
            if (pipeBody) pipeBody.setAttribute('d', 'M 100 110 L 260 110');
            if (pipeLumen) pipeLumen.setAttribute('d', 'M 100 110 L 260 110');
            if (beam) beam.style.display = 'block';
            if (flameIcon) flameIcon.style.display = 'block';
            if (viewText) { viewText.textContent = "Flame Clearly Visible!"; viewText.className = "text-xs font-bold text-emerald-400 block"; }
            if (status) status.textContent = "Straight pipe: Light travels unobstructed in straight lines through the hollow pipe directly into your eye.";
        };
    }

    if (btnBent) {
        btnBent.onclick = () => {
            playSound('wrong');
            if (pipeBody) pipeBody.setAttribute('d', 'M 100 110 Q 180 40 260 110');
            if (pipeLumen) pipeLumen.setAttribute('d', 'M 100 110 Q 180 40 260 110');
            if (beam) beam.style.display = 'none';
            if (flameIcon) flameIcon.style.display = 'none';
            if (viewText) { viewText.textContent = "Pitch Black (No Light)"; viewText.className = "text-xs font-bold text-rose-400 block"; }
            if (status) status.textContent = "Bent pipe: Light cannot bend around the curve. Rays hit the inner opaque rubber wall and are blocked.";
        };
    }
}

// SIM 5: 3-Material Optical Beam Transmissometer
function initSim5() {
    const btn1 = document.getElementById('sim5_btnTransp');
    const btn2 = document.getElementById('sim5_btnTransl');
    const btn3 = document.getElementById('sim5_btnOpaque');
    const slab = document.getElementById('sim5_slab');
    const slabName = document.getElementById('sim5_slabName');
    const transBeam = document.getElementById('sim5_transBeam');
    const screenLight = document.getElementById('sim5_screenLight');
    const screenShadow = document.getElementById('sim5_screenShadow');
    const desc = document.getElementById('sim5_desc');

    if (btn1) {
        btn1.onclick = () => {
            playSound('click');
            if (slab) { slab.setAttribute('fill', '#38bdf8'); slab.setAttribute('opacity', '0.3'); }
            if (slabName) { slabName.textContent = "Clear Optical Glass"; slabName.setAttribute('fill', '#38bdf8'); }
            if (transBeam) transBeam.setAttribute('opacity', '0.38');
            if (screenLight) screenLight.setAttribute('opacity', '0.9');
            if (screenShadow) screenShadow.setAttribute('opacity', '0.02');
            if (desc) desc.innerHTML = '<strong class="text-emerald-400">Transparent:</strong> Transmits 98% of incident photons without deviation. Objects behind are seen with crystal clarity; virtually zero shadow is cast.';
        };
    }

    if (btn2) {
        btn2.onclick = () => {
            playSound('click');
            if (slab) { slab.setAttribute('fill', '#fde047'); slab.setAttribute('opacity', '0.6'); }
            if (slabName) { slabName.textContent = "Butter / Tracing Paper"; slabName.setAttribute('fill', '#fde047'); }
            if (transBeam) transBeam.setAttribute('opacity', '0.15');
            if (screenLight) screenLight.setAttribute('opacity', '0.4');
            if (screenShadow) screenShadow.setAttribute('opacity', '0.4');
            if (desc) desc.innerHTML = '<strong class="text-cyan-400">Translucent:</strong> Transmits light partially while scattering rays diffusely. Objects behind appear blurred and hazy; casts a light-gray shadow.';
        };
    }

    if (btn3) {
        btn3.onclick = () => {
            playSound('click');
            if (slab) { slab.setAttribute('fill', '#78350f'); slab.setAttribute('opacity', '1.0'); }
            if (slabName) { slabName.textContent = "Solid Opaque Wood"; slabName.setAttribute('fill', '#f87171'); }
            if (transBeam) transBeam.setAttribute('opacity', '0.0');
            if (screenLight) screenLight.setAttribute('opacity', '0.0');
            if (screenShadow) screenShadow.setAttribute('opacity', '0.95');
            if (desc) desc.innerHTML = '<strong class="text-rose-400">Opaque:</strong> Completely absorbs and reflects all light (zero transmission). Casts a dense, pitch-black shadow on the screen!';
        };
    }
}

// SIM 6: 3-Component Shadow Physics Bench
function initSim6() {
    let lightOn = true;
    let screenOn = true;

    const slider = document.getElementById('sim6_distSlider');
    const btnLight = document.getElementById('sim6_toggleLight');
    const btnScreen = document.getElementById('sim6_toggleScreen');
    const obstacle = document.getElementById('sim6_obstacle');
    const beam = document.getElementById('sim6_beamPoly');
    const screenGroup = document.getElementById('sim6_screenGroup');
    const shadowDisc = document.getElementById('sim6_shadowDisc');
    const noScreenMsg = document.getElementById('sim6_noScreenMsg');
    const status = document.getElementById('sim6_status');

    function update() {
        const x = parseInt(slider.value);
        document.getElementById('sim6_distVal').textContent = `${x} mm`;
        if (obstacle) obstacle.setAttribute('transform', `translate(${x}, 110)`);

        // Closer to torch (small x) => larger shadow on screen
        const ry = Math.round(75 - (x * 0.16));
        if (shadowDisc) shadowDisc.setAttribute('ry', Math.max(15, ry).toString());

        if (btnLight) {
            btnLight.textContent = lightOn ? "💡 Torch: ON" : "🌑 Torch: OFF";
            btnLight.className = lightOn ? "flex-1 py-2 rounded bg-amber-600 text-white text-xs font-bold hover:bg-amber-500 transition" : "flex-1 py-2 rounded bg-slate-800 text-slate-400 text-xs font-bold hover:bg-slate-700 transition";
        }
        if (btnScreen) {
            btnScreen.textContent = screenOn ? "🖥️ Screen: PRESENT" : "❌ Screen: REMOVED";
            btnScreen.className = screenOn ? "flex-1 py-2 rounded bg-cyan-700 text-white text-xs font-bold hover:bg-cyan-600 transition" : "flex-1 py-2 rounded bg-slate-800 text-slate-400 text-xs font-bold hover:bg-slate-700 transition";
        }

        if (beam) beam.style.display = lightOn ? 'block' : 'none';
        if (screenGroup) screenGroup.style.display = screenOn ? 'block' : 'none';
        if (noScreenMsg) noScreenMsg.style.display = (!screenOn && lightOn) ? 'block' : 'none';

        if (!lightOn) {
            if (status) status.textContent = "Torch is OFF: In the absence of light, no contrast exists and zero shadows can form.";
        } else if (!screenOn) {
            if (status) status.textContent = "Screen REMOVED: Light rays pass into empty space. Without a physical screen to intercept the rays, no shadow is observable!";
        } else {
            if (status) status.textContent = "All 3 components present: Moving the obstacle closer to the torch expands the shadow on the screen.";
        }
    }

    if (slider) slider.oninput = update;
    if (btnLight) btnLight.onclick = () => { lightOn = !lightOn; update(); };
    if (btnScreen) btnScreen.onclick = () => { screenOn = !screenOn; update(); };
}

// SIM 7: Extended Light Source Umbra-Penumbra Ray Tracer
function initSim7() {
    const slider = document.getElementById('sim7_radiusSlider');
    const source = document.getElementById('sim7_source');
    const readout = document.getElementById('sim7_radiusVal');
    const umbra = document.getElementById('sim7_umbraZone');
    const penumbra = document.getElementById('sim7_penumbraZone');
    const rayU1 = document.getElementById('sim7_rayU1');
    const rayU2 = document.getElementById('sim7_rayU2');
    const rayP1 = document.getElementById('sim7_rayP1');
    const rayP2 = document.getElementById('sim7_rayP2');

    if (!slider) return;

    slider.oninput = () => {
        const r = parseInt(slider.value);
        if (source) source.setAttribute('r', r.toString());

        if (r <= 6) {
            if (readout) readout.textContent = "Point Source (Zero Penumbra)";
            if (penumbra) penumbra.style.display = 'none';
            if (umbra) { umbra.setAttribute('y', '70'); umbra.setAttribute('height', '100'); }
            if (rayP1) rayP1.style.display = 'none';
            if (rayP2) rayP2.style.display = 'none';
        } else {
            if (readout) readout.textContent = `Broad Source (R = ${r} mm)`;
            if (penumbra) {
                penumbra.style.display = 'block';
                const pHeight = Math.round(50 + (r * 3));
                const pY = Math.round(120 - (pHeight / 2));
                penumbra.setAttribute('y', pY.toString());
                penumbra.setAttribute('height', pHeight.toString());
            }
            if (umbra) {
                const uHeight = Math.max(10, Math.round(80 - (r * 1.5)));
                const uY = Math.round(120 - (uHeight / 2));
                umbra.setAttribute('y', uY.toString());
                umbra.setAttribute('height', uHeight.toString());
            }
            if (rayP1) rayP1.style.display = 'block';
            if (rayP2) rayP2.style.display = 'block';
        }
    };
}

// SIM 8: 3D Object Rotation & Distance Shadow Projector
function initSim8() {
    const slider = document.getElementById('sim8_rotSlider');
    const rotVal = document.getElementById('sim8_rotVal');
    const shadow = document.getElementById('sim8_shadowShape');
    const shapeName = document.getElementById('sim8_shapeName');

    if (!slider) return;

    slider.oninput = () => {
        const deg = parseInt(slider.value);
        rotVal.textContent = `${deg}°`;

        // At 0 deg: rectangle (w=50, h=70)
        // At 90 deg: circle (rx=ry=35 => w=70, h=70, rx=35)
        const w = Math.round(50 + (deg * 0.22));
        const rx = Math.round(deg * 0.38);

        if (shadow) {
            shadow.setAttribute('width', w.toString());
            shadow.setAttribute('rx', rx.toString());
        }

        if (deg <= 15) {
            if (shapeName) shapeName.textContent = "Rectangular Silhouette";
        } else if (deg >= 75) {
            if (shapeName) shapeName.textContent = "Circular Silhouette";
        } else {
            if (shapeName) shapeName.textContent = "Oblong Rounded Profile";
        }
    };
}

// SIM 9: Celestial Eclipse Simulator
function initSim9() {
    const btnSolar = document.getElementById('sim9_btnSolar');
    const btnLunar = document.getElementById('sim9_btnLunar');
    const solarGroup = document.getElementById('sim9_solarGroup');
    const lunarGroup = document.getElementById('sim9_lunarGroup');
    const phaseNotice = document.getElementById('sim9_phaseNotice');
    const status = document.getElementById('sim9_status');

    if (btnSolar) {
        btnSolar.onclick = () => {
            playSound('click');
            if (solarGroup) solarGroup.style.display = 'block';
            if (lunarGroup) lunarGroup.style.display = 'none';
            btnSolar.className = "px-3 py-1.5 rounded bg-amber-600 text-white text-xs font-bold hover:bg-amber-500 transition";
            btnLunar.className = "px-3 py-1.5 rounded bg-slate-700 text-slate-200 text-xs font-semibold hover:bg-slate-600 transition";
            if (phaseNotice) phaseNotice.textContent = "Phase: New Moon (Daytime Totality)";
            if (status) status.innerHTML = '<strong class="text-amber-400">Solar Eclipse:</strong> The Moon passes directly between the Sun and Earth during a New Moon, casting its small umbra shadow onto Earth\'s surface, turning day into night along the path of totality.';
        };
    }

    if (btnLunar) {
        btnLunar.onclick = () => {
            playSound('click');
            if (solarGroup) solarGroup.style.display = 'none';
            if (lunarGroup) lunarGroup.style.display = 'block';
            btnLunar.className = "px-3 py-1.5 rounded bg-amber-600 text-white text-xs font-bold hover:bg-amber-500 transition";
            btnSolar.className = "px-3 py-1.5 rounded bg-slate-700 text-slate-200 text-xs font-semibold hover:bg-slate-600 transition";
            if (phaseNotice) phaseNotice.textContent = "Phase: Full Moon (Blood Moon Totality)";
            if (status) status.innerHTML = '<strong class="text-rose-400">Lunar Eclipse:</strong> Earth passes directly between the Sun and the Moon during a Full Moon, casting its colossal shadow over the Moon. Refracted atmospheric sunlight tints the eclipsed Moon copper-red!';
        };
    }
}

// SIM 10: Law of Reflection (∠i = ∠r)
function initSim10() {
    const slider = document.getElementById('sim10_angleSlider');
    const incBeam = document.getElementById('sim10_incBeam');
    const refBeam = document.getElementById('sim10_refBeam');
    const readout = document.getElementById('sim10_readout');
    const angleIText = document.getElementById('sim10_angleIText');
    const angleRText = document.getElementById('sim10_angleRText');

    if (!slider) return;

    slider.oninput = () => {
        const deg = parseInt(slider.value);
        const rad = (deg * Math.PI) / 180;
        const length = 160;

        // Incident beam: comes from (270 - length*sin(rad), 180 - length*cos(rad))
        const x1 = Math.round(270 - length * Math.sin(rad));
        const y1 = Math.round(180 - length * Math.cos(rad));

        // Reflected beam: goes to (270 + length*sin(rad), 180 - length*cos(rad))
        const x2 = Math.round(270 + length * Math.sin(rad));
        const y2 = Math.round(180 - length * Math.cos(rad));

        if (incBeam) { incBeam.setAttribute('x1', x1.toString()); incBeam.setAttribute('y1', y1.toString()); }
        if (refBeam) { refBeam.setAttribute('x2', x2.toString()); refBeam.setAttribute('y2', y2.toString()); }

        if (readout) readout.textContent = `∠i = ${deg}° | ∠r = ${deg}° (Exact Match)`;
        if (angleIText) angleIText.textContent = `∠i = ${deg}°`;
        if (angleRText) angleRText.textContent = `∠r = ${deg}°`;
    };
}

// SIM 11: Plane Mirror Virtual Image Geometry
function initSim11() {
    const slider = document.getElementById('sim11_objSlider');
    const obj = document.getElementById('sim11_objCandle');
    const img = document.getElementById('sim11_imgCandle');
    const lineDo = document.getElementById('sim11_lineDo');
    const lineDi = document.getElementById('sim11_lineDi');
    const textDo = document.getElementById('sim11_textDo');
    const textDi = document.getElementById('sim11_textDi');
    const readout = document.getElementById('sim11_distReadout');

    if (!slider) return;

    slider.oninput = () => {
        const d = parseInt(slider.value);
        const ox = 270 - d;
        const ix = 270 + d;

        if (obj) obj.setAttribute('transform', `translate(${ox}, 190)`);
        if (img) img.setAttribute('transform', `translate(${ix}, 190)`);

        if (lineDo) { lineDo.setAttribute('x1', ox.toString()); lineDo.setAttribute('x2', '270'); }
        if (lineDi) { lineDi.setAttribute('x1', '270'); lineDi.setAttribute('x2', ix.toString()); }

        if (textDo) { textDo.setAttribute('x', Math.round((ox + 270) / 2).toString()); textDo.textContent = `d_o = ${d} cm`; }
        if (textDi) { textDi.setAttribute('x', Math.round((270 + ix) / 2).toString()); textDi.textContent = `d_i = ${d} cm`; }

        if (readout) readout.textContent = `d_o = ${d} cm | d_i = ${d} cm`;
    };
}

// SIM 12: Ambulance Text & Lateral Inversion Mirror Box
function initSim12() {
    const btnAmb = document.getElementById('sim12_btnAmb');
    const btnHand = document.getElementById('sim12_btnHand');
    const btnLetters = document.getElementById('sim12_btnLetters');
    const realText = document.getElementById('sim12_realText');
    const mirrorText = document.getElementById('sim12_mirrorText');
    const status = document.getElementById('sim12_status');

    if (btnAmb) {
        btnAmb.onclick = () => {
            playSound('click');
            if (realText) realText.textContent = "ƎƆИA⅃UБMA";
            if (mirrorText) mirrorText.textContent = "AMBULANCE";
            if (status) status.textContent = "Ambulance lettering is painted laterally inverted so that leading vehicle drivers see it right-side-readable in their rear-view mirrors.";
        };
    }

    if (btnHand) {
        btnHand.onclick = () => {
            playSound('click');
            if (realText) realText.textContent = "Raised Right Hand ✋";
            if (mirrorText) mirrorText.textContent = "Reflected Left Hand 🤚";
            if (status) status.textContent = "Raise your right hand: your mirror reflection raises its left hand. This is bilateral lateral inversion.";
        };
    }

    if (btnLetters) {
        btnLetters.onclick = () => {
            playSound('click');
            if (realText) realText.textContent = "A • B • C • D";
            if (mirrorText) mirrorText.textContent = "A • ᗺ • Ɔ • ᗡ";
            if (status) status.textContent = "Symmetrical letter 'A' is unchanged! Asymmetrical letters 'B', 'C', and 'D' clearly show lateral inversion.";
        };
    }
}

// SIM 13: Virtual Pinhole Camera Optical Box
function initSim13() {
    const lenSlider = document.getElementById('sim13_lenSlider');
    const holeSlider = document.getElementById('sim13_holeSlider');
    const invImage = document.getElementById('sim13_invImage');

    function update() {
        const len = parseInt(lenSlider.value);
        const hole = parseInt(holeSlider.value);
        document.getElementById('sim13_lenVal').textContent = `${len} mm`;
        document.getElementById('sim13_holeVal').textContent = hole === 1 ? 'Tiny (Pinpoint Sharp)' : hole === 2 ? 'Small (Crisp)' : 'Large (Blurry)';

        const scale = 0.4 + (len * 0.0012);
        if (invImage) {
            invImage.setAttribute('transform', `translate(460, 115) scale(${scale}, -${scale})`);
            invImage.style.filter = hole > 2 ? `blur(${hole * 0.8}px)` : 'none';
        }
    }

    if (lenSlider) lenSlider.oninput = update;
    if (holeSlider) holeSlider.oninput = update;
}

// SIM 14: Tree Canopy Solar Projection Simulator
function initSim14() {
    const btnToggle = document.getElementById('sim14_btnToggleEclipse');
    const btnReset = document.getElementById('sim14_btnReset');
    const eclMoon = document.getElementById('sim14_eclMoon');
    const spotsGroup = document.getElementById('sim14_spotsGroup');
    const spotLabel = document.getElementById('sim14_spotLabel');
    const sunState = document.getElementById('sim14_sunStateName');
    const status = document.getElementById('sim14_status');

    if (btnToggle) {
        btnToggle.onclick = () => {
            playSound('correct');
            if (eclMoon) eclMoon.style.display = 'block';
            if (spotLabel) spotLabel.textContent = "Eclipse Mode: All spots transform into crescents!";
            if (sunState) sunState.textContent = "Partial Solar Eclipse (Crescent)";
            if (status) status.innerHTML = '<strong class="text-amber-400">Eclipse Phenomenon:</strong> The tiny leaf gaps act as pinhole cameras projecting inverted real images of the source. When the Sun becomes a crescent, every single spot under the canopy turns into a sharp crescent!';

            // Render crescent shapes in spots
            if (spotsGroup) {
                spotsGroup.innerHTML = `
                    <path d="M 40 20 A 12 12 0 0 1 40 44 A 8 12 0 0 0 40 20 Z" />
                    <path d="M 95 32 A 15 15 0 0 1 95 62 A 10 15 0 0 0 95 32 Z" />
                    <path d="M 150 25 A 11 11 0 0 1 150 47 A 7 11 0 0 0 150 25 Z" />
                    <path d="M 65 68 A 14 14 0 0 1 65 96 A 9 14 0 0 0 65 68 Z" />
                    <path d="M 130 72 A 16 16 0 0 1 130 104 A 10 16 0 0 0 130 72 Z" />
                `;
            }
        };
    }

    if (btnReset) {
        btnReset.onclick = () => {
            if (eclMoon) eclMoon.style.display = 'none';
            if (spotLabel) spotLabel.textContent = "Normal Sun: Circular solar disc images";
            if (sunState) sunState.textContent = "Full Solar Disc (Round)";
            if (status) status.textContent = "Gaps between leaves act as pinholes projecting round solar disc images.";
            if (spotsGroup) {
                spotsGroup.innerHTML = `
                    <circle cx="40" cy="30" r="12" />
                    <circle cx="95" cy="45" r="15" />
                    <circle cx="150" cy="35" r="11" />
                    <circle cx="65" cy="80" r="14" />
                    <circle cx="130" cy="85" r="16" />
                    <circle cx="170" cy="95" r="10" />
                `;
            }
        };
    }
}

// SIM 15: Submarine Trench Periscope Ray Simulator
function initSim15() {
    const btn = document.getElementById('sim15_btnAnimate');
    const ray = document.getElementById('sim15_ray');
    const status = document.getElementById('sim15_status');

    if (btn) {
        btn.onclick = () => {
            playSound('correct');
            if (ray) {
                ray.setAttribute('stroke-width', '5');
                ray.setAttribute('stroke', '#38bdf8');
                setTimeout(() => {
                    ray.setAttribute('stroke-width', '3');
                    ray.setAttribute('stroke', '#fde047');
                }, 1200);
            }
            if (status) status.innerHTML = '<strong class="text-emerald-400">Photon Pulse Tracked:</strong> Light travels horizontal → turns 90° down M₁ → travels vertical → turns 90° forward M₂ → enters eye with zero lateral inversion!';
        };
    }
}

// SIM 16: Interactive 60° Kaleidoscope Mandala
function initSim16() {
    const btn = document.getElementById('sim16_btnRotate');
    const group = document.getElementById('sim16_mandalaGroup');
    let angle = 0;

    const colors = ['#ec4899', '#8b5cf6', '#3b82f6', '#10b981', '#f59e0b', '#06b6d4', '#f43f5e'];

    if (btn) {
        btn.onclick = () => {
            playSound('click');
            angle = (angle + 30) % 360;
            const c1 = colors[Math.floor(Math.random() * colors.length)];
            const c2 = colors[Math.floor(Math.random() * colors.length)];

            if (group) {
                group.setAttribute('transform', `translate(120, 120) rotate(${angle})`);
                const petals = group.querySelectorAll('ellipse');
                petals.forEach(p => p.setAttribute('fill', c1));
                const dots = group.querySelectorAll('circle');
                dots.forEach((d, idx) => { if (idx > 0) d.setAttribute('fill', c2); });
            }
        };
    }
}

// Window Onload Initialization
window.addEventListener('DOMContentLoaded', () => {
    goToSlide(1);
});
'''
