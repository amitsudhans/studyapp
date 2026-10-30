# -*- coding: utf-8 -*-
"""
Generates the comprehensive JavaScript module for NCERT Class 7 Science Chapter 12: Earth, Moon, and the Sun.
Output: .agents/class7_science_earth_moon_sun_js.py
Strictly zero raw LaTeX. Clean Unicode everywhere.
"""

def create_js_file():
    print("Generating class7_science_earth_moon_sun_js.py...")

    code = '''# -*- coding: utf-8 -*-
"""
Client-side interactivity script for NCERT Class 7 Science Chapter 12: Earth, Moon, and the Sun.
Strictly zero raw LaTeX code. Clean Unicode everywhere.
"""

JAVASCRIPT_CODE = """
// State variables
let currentSlide = 1;
const totalSlides = 20;
let isSpeaking = false;
let synth = window.speechSynthesis;
let currentUtterance = null;

// Sound Effects via Web Audio API
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

function playSound(type) {
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);

    if (type === 'correct') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(587.33, audioCtx.currentTime); // D5
        osc.frequency.setValueAtTime(880, audioCtx.currentTime + 0.1); // A5
        gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.35);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.35);
    } else if (type === 'wrong') {
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220, audioCtx.currentTime); // A3
        osc.frequency.setValueAtTime(164.81, audioCtx.currentTime + 0.1); // E3
        gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.35);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.35);
    } else if (type === 'click') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.05, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.08);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.08);
    }
}

// Navigation Functions
function goToSlide(slideNum) {
    if (slideNum < 1 || slideNum > totalSlides) return;
    
    stopSpeech();
    playSound('click');
    
    // Hide current slide
    const curEl = document.getElementById(`slide-${currentSlide}`);
    if (curEl) curEl.classList.add('hidden');
    
    currentSlide = slideNum;
    
    // Show new slide
    const nextEl = document.getElementById(`slide-${currentSlide}`);
    if (nextEl) nextEl.classList.remove('hidden');
    
    // Update navigation controls
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');
    
    if (prevBtn) prevBtn.disabled = (currentSlide === 1);
    
    // TERMINAL SLIDE RULE: Slide 20 hides next button and shows lastSlideNotice
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
    
    // Update select dropdown
    const select = document.querySelector('select');
    if (select) select.value = currentSlide;

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        goToSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        goToSlide(currentSlide - 1);
    }
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
    if (!('speechSynthesis' in window)) {
        alert('Web Speech API is not supported in this browser.');
        return;
    }
    
    stopSpeech();
    
    const curSlideEl = document.getElementById(`slide-${currentSlide}`);
    if (!curSlideEl) return;
    
    const title = curSlideEl.querySelector('h2') ? curSlideEl.querySelector('h2').innerText : '';
    const summary = curSlideEl.querySelector('.slide-summary') ? curSlideEl.querySelector('.slide-summary').innerText : '';
    
    let textToSpeak = `${title}. ${summary}`;
    
    currentUtterance = new SpeechSynthesisUtterance(textToSpeak);
    currentUtterance.rate = 1.0;
    currentUtterance.pitch = 1.0;
    
    currentUtterance.onstart = function() {
        isSpeaking = true;
        const narrateBtn = document.getElementById('narrateBtn');
        if (narrateBtn) {
            narrateBtn.classList.add('bg-amber-500/20', 'border-amber-500');
            narrateBtn.querySelector('span').textContent = 'Pause Voice';
        }
    };
    
    currentUtterance.onend = function() {
        stopSpeech();
    };
    
    currentUtterance.onerror = function() {
        stopSpeech();
    };
    
    synth.speak(currentUtterance);
}

function stopSpeech() {
    if (synth && synth.speaking) {
        synth.cancel();
    }
    isSpeaking = false;
    const narrateBtn = document.getElementById('narrateBtn');
    if (narrateBtn) {
        narrateBtn.classList.remove('bg-amber-500/20', 'border-amber-500');
        narrateBtn.querySelector('span').textContent = 'Voice Narration';
    }
}

// Checkpoint Verification
function checkCheckpoint(cpId, selectedIdx, correctIdx, explanation) {
    const card = document.getElementById(`cp_card_${cpId}`);
    const feedback = document.getElementById(`cp_feedback_${cpId}`);
    if (!card || !feedback) return;
    
    const buttons = card.querySelectorAll('.cp-option-btn');
    buttons.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === correctIdx) {
            btn.classList.remove('bg-slate-800', 'border-slate-700');
            btn.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-200');
        } else if (idx === selectedIdx) {
            btn.classList.remove('bg-slate-800', 'border-slate-700');
            btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-200');
        }
    });
    
    feedback.classList.remove('hidden');
    if (selectedIdx === correctIdx) {
        playSound('correct');
        feedback.className = 'mt-3 p-3 rounded-lg bg-emerald-950/70 border border-emerald-500/50 text-xs text-emerald-200';
        feedback.innerHTML = `<div class="flex items-center gap-1.5 font-bold mb-1"><span>✅ Correct!</span></div><p class="leading-relaxed">${explanation}</p>`;
    } else {
        playSound('wrong');
        feedback.className = 'mt-3 p-3 rounded-lg bg-rose-950/70 border border-rose-500/50 text-xs text-rose-200';
        feedback.innerHTML = `<div class="flex items-center gap-1.5 font-bold mb-1"><span>❌ Incorrect</span></div><p class="leading-relaxed">${explanation}</p>`;
    }
}

// Solution Modal
function openSolutionModal(qNum, qText, solText) {
    playSound('click');
    const modal = document.getElementById('solutionModal');
    const title = document.getElementById('modalTitle');
    const body = document.getElementById('modalBody');
    
    if (modal && title && body) {
        title.textContent = `Mastery Solution • Question ${qNum}`;
        body.innerHTML = `
            <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-700 text-xs sm:text-sm text-slate-200 font-semibold mb-3">
                ${qText}
            </div>
            <div class="p-4 rounded-xl bg-cyan-950/40 border border-cyan-500/40 text-xs sm:text-sm text-cyan-200 leading-relaxed space-y-2">
                <div class="flex items-center gap-2 text-cyan-300 font-bold uppercase tracking-wider text-[11px]">
                    <span>💡</span> Step-by-Step Teacher Explanation
                </div>
                <p>${solText}</p>
            </div>
        `;
        modal.style.display = 'flex';
    }
}

function closeSolutionModal() {
    playSound('click');
    const modal = document.getElementById('solutionModal');
    if (modal) modal.style.display = 'none';
}

// ==========================================
// BESPOKE SIMULATOR LOGIC
// ==========================================

// Simulator 1: Photon Launch
let sim1Orbiting = true;
let sim1Angle = 0;
function sim1AnimatePhoton() {
    playSound('click');
    const photon = document.getElementById('sim1_photon');
    if (!photon) return;
    
    let startX = 100;
    let endX = 350;
    let currentX = startX;
    
    const anim = setInterval(() => {
        currentX += 8;
        photon.setAttribute('cx', currentX);
        if (currentX >= endX) {
            clearInterval(anim);
            photon.setAttribute('cx', startX);
            playSound('correct');
        }
    }, 16);
}

function sim1ToggleOrbit() {
    playSound('click');
    sim1Orbiting = !sim1Orbiting;
    const btn = document.getElementById('sim1_orbit_btn');
    if (btn) btn.textContent = sim1Orbiting ? 'Pause Lunar Orbit' : 'Resume Lunar Orbit';
}

setInterval(() => {
    if (sim1Orbiting) {
        sim1Angle = (sim1Angle + 2) % 360;
        const rad = (sim1Angle * Math.PI) / 180;
        const moon = document.getElementById('sim1_moon');
        if (moon) {
            const mx = Math.cos(rad) * 38;
            const my = Math.sin(rad) * 38;
            moon.setAttribute('transform', `translate(${mx}, ${my})`);
        }
    }
}, 40);

// Simulator 2: Earth Axial Rotation
let sim2Spinning = false;
let sim2Timer = null;
let sim2AngleVal = 0;

function sim2UpdateAngle(val) {
    sim2AngleVal = parseInt(val);
    const sliderVal = document.getElementById('sim2_angle_val');
    const phaseText = document.getElementById('sim2_phase_text');
    const timeText = document.getElementById('sim2_time_text');
    const continents = document.getElementById('sim2_continents');
    const delhiDot = document.getElementById('sim2_delhi_dot');

    if (sliderVal) sliderVal.textContent = `${sim2AngleVal}°`;

    // Map 0-360 degrees to 24 hours (0° = 12:00 PM Noon)
    const hours = (12 + (sim2AngleVal / 360) * 24) % 24;
    const wholeH = Math.floor(hours);
    const mins = Math.floor((hours - wholeH) * 60);
    const ampm = wholeH >= 12 ? 'PM' : 'AM';
    const displayH = wholeH % 12 === 0 ? 12 : wholeH % 12;
    const displayM = mins < 10 ? '0' + mins : mins;

    if (timeText) timeText.textContent = `${displayH}:${displayM} ${ampm}`;

    // Continents shift horizontally
    if (continents) {
        const shiftX = (sim2AngleVal / 360) * 160;
        continents.setAttribute('transform', `translate(${shiftX - 80}, 0)`);
    }

    // Delhi marker position
    if (delhiDot) {
        const dotX = Math.sin((sim2AngleVal * Math.PI) / 180) * 45;
        delhiDot.setAttribute('cx', dotX);
    }

    if (phaseText) {
        if (sim2AngleVal >= 315 || sim2AngleVal < 45) {
            phaseText.textContent = 'Status: Mid-Day (Direct Sunlight)';
            phaseText.className = 'text-amber-400 font-bold';
        } else if (sim2AngleVal >= 45 && sim2AngleVal < 135) {
            phaseText.textContent = 'Status: Afternoon ➔ Dusk (Sunset)';
            phaseText.className = 'text-orange-400 font-bold';
        } else if (sim2AngleVal >= 135 && sim2AngleVal < 225) {
            phaseText.textContent = 'Status: Nighttime (Deep Shadow)';
            phaseText.className = 'text-indigo-400 font-bold';
        } else {
            phaseText.textContent = 'Status: Dawn ➔ Sunrise (Entering Light)';
            phaseText.className = 'text-cyan-400 font-bold';
        }
    }
}

function sim2ToggleAutoSpin() {
    playSound('click');
    sim2Spinning = !sim2Spinning;
    const btn = document.getElementById('sim2_spin_btn');
    if (btn) btn.textContent = sim2Spinning ? '⏸ Pause Spin' : '▶ Auto Spin Globe';

    if (sim2Spinning) {
        sim2Timer = setInterval(() => {
            sim2AngleVal = (sim2AngleVal + 2) % 360;
            const slider = document.getElementById('sim2_slider');
            if (slider) slider.value = sim2AngleVal;
            sim2UpdateAngle(sim2AngleVal);
        }, 50);
    } else {
        clearInterval(sim2Timer);
    }
}

// Simulator 3: Circle of Illumination (Pin angle)
function sim3SetPin(deg) {
    const pin = document.getElementById('sim3_pin');
    const label = document.getElementById('sim3_slider_val');
    const posName = document.getElementById('sim3_pos_name');
    const shadowText = document.getElementById('sim3_shadow_text');
    
    const angle = parseInt(deg);
    if (pin) pin.setAttribute('transform', `rotate(${angle})`);
    if (label) label.textContent = `${angle}°`;

    if (posName && shadowText) {
        if (Math.abs(angle) <= 20) {
            posName.textContent = 'Solar Noon (Sub-solar point)';
            shadowText.textContent = 'Zero / Minimal Shadow';
        } else if (angle > 20 && angle < 80) {
            posName.textContent = 'Afternoon (Approaching Dusk)';
            shadowText.textContent = 'Elongating Eastward';
        } else if (angle >= 80 && angle <= 100) {
            posName.textContent = 'Crossing Terminator: Sunset / Twilight';
            shadowText.textContent = 'Maximum Long Shadow';
        } else if (angle < -20 && angle > -80) {
            posName.textContent = 'Morning (Sun Rising in East)';
            shadowText.textContent = 'Long Westward Shadow';
        } else if (angle <= -80 && angle >= -100) {
            posName.textContent = 'Crossing Terminator: Sunrise / Dawn';
            shadowText.textContent = 'Maximum Long Shadow';
        } else {
            posName.textContent = 'Night Hemisphere (Planetary Shadow)';
            shadowText.textContent = 'Complete Night Darkness';
        }
    }
}

// Simulator 4: Apparent Diurnal Motion
function sim4SetTime(h) {
    const hour = parseFloat(h);
    const sun = document.getElementById('sim4_sun');
    const shadow = document.getElementById('sim4_shadow');
    const timeLabel = document.getElementById('sim4_time_label');
    const motionDesc = document.getElementById('sim4_motion_desc');
    const sliderVal = document.getElementById('sim4_slider_val');

    // Hour ranges from 6 to 18 (12 hours)
    const t = (hour - 6) / 12; // 0.0 to 1.0
    // Parabolic arc for Sun: X from 50 to 400, Y from 150 to 30 to 150
    const sunX = 50 + t * 350;
    const sunY = 150 - Math.sin(t * Math.PI) * 125;

    if (sun) sun.setAttribute('transform', `translate(${sunX}, ${sunY})`);

    // Shadow moves opposite to Sun
    if (shadow) {
        const shadowLen = (0.5 - t) * 100;
        shadow.setAttribute('x2', 225 + shadowLen);
    }

    const wholeH = Math.floor(hour);
    const mins = (hour - wholeH) * 60 === 30 ? '30' : '00';
    const ampm = wholeH >= 12 ? 'PM' : 'AM';
    const dispH = wholeH > 12 ? wholeH - 12 : wholeH;

    if (timeLabel) timeLabel.textContent = `${dispH}:${mins} ${ampm}`;
    if (sliderVal) sliderVal.textContent = `${dispH}:${mins} ${ampm}`;

    if (motionDesc) {
        if (hour < 9) {
            motionDesc.textContent = 'Rising over East horizon ➔ Climbing South';
        } else if (hour >= 9 && hour < 14) {
            motionDesc.textContent = 'Near Zenith (South highest elevation at Noon)';
        } else {
            motionDesc.textContent = 'Descending toward West ➔ Setting';
        }
    }
}

// Simulator 5: Aryabhata Boat Analogy
let sim5Active = false;
let sim5Timer = null;
let sim5Pos = 180;
let sim5TreeOffset = 0;

function sim5ToggleAnimation() {
    playSound('click');
    sim5Active = !sim5Active;
    const btn = document.getElementById('sim5_btn');
    if (btn) btn.textContent = sim5Active ? "⏸ Rest Oars" : "▶ Row Aryabhata\'s Boat";

    if (sim5Active) {
        sim5Timer = setInterval(() => {
            sim5TreeOffset = (sim5TreeOffset - 2.5) % 150;
            const trees = document.getElementById('sim5_trees');
            if (trees) trees.setAttribute('transform', `translate(${sim5TreeOffset}, 0)`);
        }, 40);
    } else {
        clearInterval(sim5Timer);
    }
}

// Simulator 6: Leap Year Stepper
let sim6Year = 1;
function sim6StepYear() {
    playSound('click');
    sim6Year = (sim6Year % 4) + 1;
    const accumLabel = document.getElementById('sim6_accum_hours');
    const bar = document.getElementById('sim6_hours_bar');
    const febDays = document.getElementById('sim6_feb_days');

    if (accumLabel) accumLabel.textContent = `+${sim6Year * 6} Hours (Year ${sim6Year})`;
    if (bar) bar.style.width = `${(sim6Year / 4) * 100}%`;

    if (febDays) {
        if (sim6Year === 4) {
            playSound('correct');
            febDays.textContent = '29 Days (LEAP YEAR! 🎉)';
            febDays.className = 'text-emerald-400 font-mono font-bold text-sm animate-pulse';
        } else {
            febDays.textContent = '28 Days (Common)';
            febDays.className = 'text-cyan-300 font-mono font-bold text-sm';
        }
    }
}

// Simulator 7: Seasonal Constellations
const sim7Months = [
    { name: 'December', season: 'Winter', stars: 'Orion, Taurus, Sirius', angle: 0 },
    { name: 'January', season: 'Winter', stars: 'Orion, Gemini, Canis Major', angle: 30 },
    { name: 'February', season: 'Winter', stars: 'Gemini, Cancer, Procyon', angle: 60 },
    { name: 'March', season: 'Spring', stars: 'Leo, Cancer, Ursa Major', angle: 90 },
    { name: 'April', season: 'Spring', stars: 'Leo, Virgo, Arcturus', angle: 120 },
    { name: 'May', season: 'Spring', stars: 'Virgo, Bootes, Spica', angle: 150 },
    { name: 'June', season: 'Summer', stars: 'Scorpius, Sagittarius, Vega', angle: 180 },
    { name: 'July', season: 'Summer', stars: 'Scorpius, Antares, Cygnus', angle: 210 },
    { name: 'August', season: 'Summer', stars: 'Sagittarius, Aquila, Altair', angle: 240 },
    { name: 'September', season: 'Autumn', stars: 'Pegasus, Cygnus, Deneb', angle: 270 },
    { name: 'October', season: 'Autumn', stars: 'Pegasus, Andromeda, Pisces', angle: 300 },
    { name: 'November', season: 'Autumn', stars: 'Andromeda, Cassiopeia, Aries', angle: 330 }
];

function sim7SetMonth(idx) {
    const m = sim7Months[parseInt(idx)];
    const monthLabel = document.getElementById('sim7_month_label');
    const starsLabel = document.getElementById('sim7_visible_stars');
    const sliderVal = document.getElementById('sim7_slider_val');
    const earthGroup = document.getElementById('sim7_earth_group');
    const gaze = document.getElementById('sim7_gaze');

    if (monthLabel) monthLabel.textContent = `${m.name} (${m.season})`;
    if (starsLabel) starsLabel.textContent = m.stars;
    if (sliderVal) sliderVal.textContent = m.name;

    // Orbit position around Sun (cx=225, cy=110, r=65)
    // Angle in radians (0 at bottom Dec, counter-clockwise)
    const rad = ((m.angle + 90) * Math.PI) / 180;
    const ex = 225 + Math.cos(rad) * 65;
    const ey = 110 + Math.sin(rad) * 65;

    if (earthGroup) {
        earthGroup.setAttribute('transform', `translate(${ex}, ${ey})`);
    }

    if (gaze) {
        // Gaze points outward away from (225, 110)
        const rotDeg = m.angle;
        gaze.setAttribute('transform', `rotate(${rotDeg})`);
    }
}

// Simulator 9: Sunlight Elevation Angle & Insolation
function sim9SetAngle(deg) {
    const angle = parseInt(deg);
    const sliderVal = document.getElementById('sim9_slider_val');
    const readout = document.getElementById('sim9_angle_readout');
    const intensity = document.getElementById('sim9_intensity_text');
    const footprint = document.getElementById('sim9_footprint');
    const beam = document.getElementById('sim9_beam');
    const areaLabel = document.getElementById('sim9_area_label');
    const source = document.getElementById('sim9_source');

    if (sliderVal) sliderVal.textContent = `${angle}°`;

    // Calculate footprint width based on 1/sin(angle)
    const rad = (angle * Math.PI) / 180;
    const baseW = 60;
    const footW = baseW / Math.sin(rad);

    const x1 = 210 - footW / 2;
    const x2 = 210 + footW / 2;

    if (footprint) {
        footprint.setAttribute('x1', x1);
        footprint.setAttribute('x2', x2);
    }

    if (areaLabel) {
        areaLabel.textContent = `Footprint: ${Math.round(footW)} mm`;
    }

    // Source tilt position
    const sourceX = 210 - Math.cos(rad) * 140;
    const sourceY = 160 - Math.sin(rad) * 140;

    if (source) {
        source.setAttribute('cx', sourceX);
        source.setAttribute('cy', sourceY);
    }

    if (beam) {
        beam.setAttribute('points', `${sourceX},${sourceY} ${x1},160 ${x2},160`);
    }

    if (readout && intensity) {
        if (angle >= 75) {
            readout.textContent = `${angle}° (Direct / Summer)`;
            intensity.textContent = 'MAXIMUM (Intense Summer Heat)';
            intensity.className = 'text-rose-400 font-bold text-sm';
        } else if (angle >= 50) {
            readout.textContent = `${angle}° (Moderate / Spring-Autumn)`;
            intensity.textContent = 'MODERATE (Mild Pleasant Heat)';
            intensity.className = 'text-amber-300 font-bold text-sm';
        } else {
            readout.textContent = `${angle}° (Slanted / Winter)`;
            intensity.textContent = 'WEAK & DIFFUSE (Cold Winter Climate)';
            intensity.className = 'text-cyan-300 font-bold text-sm';
        }
    }
}

// Simulator 10: Solstices Toggle
function sim10SetSolstice(type) {
    playSound('click');
    const axis = document.getElementById('sim10_axis');
    const npText = document.getElementById('sim10_np_text');
    const northStatus = document.getElementById('sim10_north_status');
    const southStatus = document.getElementById('sim10_south_status');
    const juneBtn = document.getElementById('sim10_june_btn');
    const decBtn = document.getElementById('sim10_dec_btn');

    if (type === 'june') {
        if (axis) {
            axis.setAttribute('x1', '-25');
            axis.setAttribute('x2', '25');
        }
        if (npText) {
            npText.setAttribute('x', '-30');
            npText.textContent = 'North Pole (Tilts TOWARD Sun)';
        }
        if (northStatus) northStatus.textContent = 'Peak Summer (14h Daylight in Delhi • 24h Arctic Sun)';
        if (southStatus) southStatus.textContent = 'Peak Winter (Short days in Sydney • Cold nights)';
        if (juneBtn) juneBtn.className = 'flex-1 py-2 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition shadow-md';
        if (decBtn) decBtn.className = 'flex-1 py-2 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition';
    } else {
        if (axis) {
            axis.setAttribute('x1', '25');
            axis.setAttribute('x2', '-25');
        }
        if (npText) {
            npText.setAttribute('x', '30');
            npText.textContent = 'North Pole (Tilts AWAY from Sun)';
        }
        if (northStatus) northStatus.textContent = 'Peak Winter (10h Daylight in Delhi • 24h Polar Night)';
        if (southStatus) southStatus.textContent = 'Peak Summer (14h+ Daylight in Sydney • Warm beaches)';
        if (decBtn) decBtn.className = 'flex-1 py-2 rounded-xl bg-cyan-600 text-white font-bold text-xs transition shadow-md';
        if (juneBtn) juneBtn.className = 'flex-1 py-2 rounded-xl bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition';
    }
}

// Simulator 11: Equinoxes Toggle
function sim11SetEquinox(type) {
    playSound('click');
    const springBtn = document.getElementById('sim11_spring_btn');
    const autumnBtn = document.getElementById('sim11_autumn_btn');

    if (type === 'spring') {
        if (springBtn) springBtn.className = 'flex-1 py-1.5 rounded-lg bg-emerald-600 text-white font-bold text-xs transition';
        if (autumnBtn) autumnBtn.className = 'flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition';
    } else {
        if (autumnBtn) autumnBtn.className = 'flex-1 py-1.5 rounded-lg bg-amber-600 text-white font-bold text-xs transition';
        if (springBtn) springBtn.className = 'flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition';
    }
}

// Simulator 12: Umbra & Penumbra Probe
function sim12SetProbeY(val) {
    const y = parseInt(val);
    const probe = document.getElementById('sim12_probe');
    const zoneText = document.getElementById('sim12_zone_text');
    const viewText = document.getElementById('sim12_view_text');
    const sliderVal = document.getElementById('sim12_slider_val');

    if (probe) probe.setAttribute('transform', `translate(360, ${y})`);
    if (sliderVal) sliderVal.textContent = `Y = ${y}`;

    if (zoneText && viewText) {
        if (y >= 92 && y <= 108) {
            zoneText.textContent = 'Deep Umbra Cone (Total Shadow)';
            zoneText.className = 'text-rose-400 font-bold';
            viewText.textContent = '100% Sun Obscured (Total Solar Eclipse)';
        } else if (y >= 65 && y <= 135) {
            zoneText.textContent = 'Penumbra (Partial Shadow Zone)';
            zoneText.className = 'text-amber-300 font-bold';
            viewText.textContent = 'Partial Eclipse (Part of Solar Disc Hidden)';
        } else {
            zoneText.textContent = 'Direct Sunlight (Outside Shadow)';
            zoneText.className = 'text-cyan-300 font-bold';
            viewText.textContent = 'Normal Daytime (Zero Eclipse)';
        }
    }
}

// Simulator 13: Solar Eclipse Offset
function sim13SetMoonOffset(val) {
    const offset = parseInt(val);
    const moon = document.getElementById('sim13_moon');
    const skyMoon = document.getElementById('sim13_sky_moon');
    const statusLabel = document.getElementById('sim13_status_label');
    const sliderVal = document.getElementById('sim13_slider_val');

    if (moon) moon.setAttribute('transform', `translate(230, ${100 + offset})`);
    if (skyMoon) skyMoon.setAttribute('cy', 28 + offset * 1.5);
    if (sliderVal) sliderVal.textContent = offset === 0 ? 'Exact Syzygy (0)' : `Offset ${offset}`;

    if (statusLabel) {
        if (Math.abs(offset) <= 2) {
            playSound('correct');
            statusLabel.textContent = 'Total Solar Eclipse (Totality!)';
            statusLabel.className = 'text-emerald-400 font-bold text-sm block';
        } else if (Math.abs(offset) <= 12) {
            statusLabel.textContent = 'Partial Solar Eclipse (Solar Bite)';
            statusLabel.className = 'text-amber-300 font-bold text-sm block';
        } else {
            statusLabel.textContent = 'No Eclipse (Moon Shadow Misses Earth)';
            statusLabel.className = 'text-slate-400 font-bold text-sm block';
        }
    }
}

// Simulator 15: Lunar Eclipse Y-position
function sim15SetMoonY(val) {
    const y = parseInt(val);
    const moon = document.getElementById('sim15_moon');
    const phaseText = document.getElementById('sim15_phase_text');
    const colorText = document.getElementById('sim15_color_text');
    const sliderVal = document.getElementById('sim15_slider_val');

    if (moon) moon.setAttribute('transform', `translate(300, ${y})`);
    if (sliderVal) sliderVal.textContent = y === 100 ? 'Center Umbra' : `Y = ${y}`;

    if (phaseText && colorText) {
        if (Math.abs(y - 100) <= 8) {
            playSound('correct');
            phaseText.textContent = 'Total Lunar Eclipse (Totality)';
            colorText.textContent = 'Glowing Copper-Red (Blood Moon)';
            phaseText.className = 'text-rose-400 font-bold text-sm';
            colorText.className = 'text-rose-300 font-bold text-sm';
            if (moon) {
                const c = moon.querySelector('circle');
                if (c) c.setAttribute('fill', '#ef4444');
            }
        } else if (Math.abs(y - 100) <= 25) {
            phaseText.textContent = 'Partial Umbral Lunar Eclipse';
            colorText.textContent = 'Curved Dark Bite Across Lunar Disc';
            phaseText.className = 'text-amber-300 font-bold text-sm';
            colorText.className = 'text-amber-200 font-bold text-sm';
            if (moon) {
                const c = moon.querySelector('circle');
                if (c) c.setAttribute('fill', '#94a3b8');
            }
        } else {
            phaseText.textContent = 'Normal Full Moon (Purnima)';
            colorText.textContent = 'Bright Pearly-White Disc';
            phaseText.className = 'text-slate-200 font-bold text-sm';
            colorText.className = 'text-slate-200 font-bold text-sm';
            if (moon) {
                const c = moon.querySelector('circle');
                if (c) c.setAttribute('fill', '#f8fafc');
            }
        }
    }
}

// Simulator 16: 5.14° Tilt Toggle
function sim16SetTilt(deg) {
    playSound('click');
    const tiltedOrbit = document.getElementById('sim16_tilted_orbit');
    const label = document.getElementById('sim16_tilt_label');
    const feas = document.getElementById('sim16_feasibility');
    const realBtn = document.getElementById('sim16_real_btn');
    const zeroBtn = document.getElementById('sim16_zero_btn');

    if (deg > 0) {
        if (tiltedOrbit) tiltedOrbit.setAttribute('transform', 'rotate(5.14, 230, 100)');
        if (label) label.textContent = '5.14° (Real Moon Orbit)';
        if (feas) {
            feas.textContent = 'Moon Misses Earth Shadow ➔ Eclipses Rare';
            feas.className = 'text-cyan-300 font-bold';
        }
        if (realBtn) realBtn.className = 'flex-1 py-1.5 rounded-lg bg-rose-600 text-white font-bold text-xs transition shadow-md';
        if (zeroBtn) zeroBtn.className = 'flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition';
    } else {
        if (tiltedOrbit) tiltedOrbit.setAttribute('transform', 'rotate(0, 230, 100)');
        if (label) label.textContent = '0.0° (Hypothetical Flat Orbit)';
        if (feas) {
            feas.textContent = 'Automatic Eclipse Every 29.5 Days!';
            feas.className = 'text-amber-400 font-bold';
        }
        if (zeroBtn) zeroBtn.className = 'flex-1 py-1.5 rounded-lg bg-amber-600 text-white font-bold text-xs transition shadow-md';
        if (realBtn) realBtn.className = 'flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition';
    }
}

// Initialize on page load
window.addEventListener('DOMContentLoaded', () => {
    goToSlide(1);
});
"""
'''
    with open(".agents/class7_science_earth_moon_sun_js.py", "w", encoding="utf-8") as f:
        f.write(code)

    print("Successfully generated .agents/class7_science_earth_moon_sun_js.py.")

if __name__ == "__main__":
    create_js_file()
