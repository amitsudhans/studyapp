# -*- coding: utf-8 -*-
"""
Generates the comprehensive JavaScript module for NCERT Class 6 Mathematics Chapter 1: Patterns in Mathematics.
Output: .agents/class6_math_patterns_js.py
Strictly zero raw LaTeX. Clean Unicode everywhere.
"""

def create_js_file():
    print("Generating class6_math_patterns_js.py...")

    code = '''# -*- coding: utf-8 -*-
"""
Client-side interactivity script for NCERT Class 6 Mathematics Chapter 1: Patterns in Mathematics.
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

// Simulator 1: Nature's Pattern Detector
function sim1SetMode(mode) {
    playSound('click');
    const sunG = document.getElementById('sim1_sunflower');
    const hexG = document.getElementById('sim1_honeycomb');
    const wavG = document.getElementById('sim1_waves');
    const nameL = document.getElementById('sim1_type_name');
    const mathL = document.getElementById('sim1_math_secret');
    const btnSun = document.getElementById('sim1_btn_sun');
    const btnHex = document.getElementById('sim1_btn_hex');
    const btnWav = document.getElementById('sim1_btn_wav');

    const defaultBtn = 'py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition';
    if (btnSun) btnSun.className = defaultBtn;
    if (btnHex) btnHex.className = defaultBtn;
    if (btnWav) btnWav.className = defaultBtn;

    if (mode === 'sunflower') {
        if (sunG) sunG.classList.remove('hidden');
        if (hexG) hexG.classList.add('hidden');
        if (wavG) wavG.classList.add('hidden');
        if (nameL) nameL.textContent = 'Sunflower Spiral Packings';
        if (mathL) mathL.textContent = 'Virahānka / Fibonacci Numbers (21 & 34 Spirals)';
        if (btnSun) btnSun.className = 'py-1.5 rounded-lg bg-amber-500 text-slate-950 font-bold text-xs transition shadow';
    } else if (mode === 'honeycomb') {
        if (sunG) sunG.classList.add('hidden');
        if (hexG) hexG.classList.remove('hidden');
        if (wavG) wavG.classList.add('hidden');
        if (nameL) nameL.textContent = 'Hexagonal Tessellation (Honeycomb)';
        if (mathL) mathL.textContent = 'Optimal 120° Angle Tiling & Centered Hexagonal Numbers';
        if (btnHex) btnHex.className = 'py-1.5 rounded-lg bg-amber-500 text-slate-950 font-bold text-xs transition shadow';
        sim1RenderHoneycomb();
    } else {
        if (sunG) sunG.classList.add('hidden');
        if (hexG) hexG.classList.add('hidden');
        if (wavG) wavG.classList.remove('hidden');
        if (nameL) nameL.textContent = 'Harmonic Rhythm & Sound Waves';
        if (mathL) mathL.textContent = 'Periodic Sine Wave Frequencies & Musical Pitch Intervals';
        if (btnWav) btnWav.className = 'py-1.5 rounded-lg bg-cyan-600 text-white font-bold text-xs transition shadow';
    }
}

function sim1InitSunflower() {
    const seedsG = document.getElementById('sim1_seeds');
    const petalsG = document.getElementById('sim1_petals');
    if (!seedsG || !petalsG) return;

    // Golden angle ~137.5° in radians
    const goldenAngle = 137.507764 * (Math.PI / 180);
    let seedsHtml = '';
    for (let i = 1; i <= 140; i++) {
        const r = 6 * Math.sqrt(i);
        const theta = i * goldenAngle;
        const x = 200 + r * Math.cos(theta);
        const y = 100 + r * Math.sin(theta);
        seedsHtml += `<circle cx="${x}" cy="${y}" r="2.2" fill="#fbbf24" opacity="0.9"/>`;
    }
    seedsG.innerHTML = seedsHtml;

    // Petals
    let petalsHtml = '';
    for (let p = 0; p < 24; p++) {
        const angle = (p * 360 / 24) * (Math.PI / 180);
        const px = 200 + 82 * Math.cos(angle);
        const py = 100 + 82 * Math.sin(angle);
        petalsHtml += `<ellipse cx="${px}" cy="${py}" rx="14" ry="5" transform="rotate(${p * 15}, ${px}, ${py})" fill="#f59e0b" opacity="0.8"/>`;
    }
    petalsG.innerHTML = petalsHtml;
}

function sim1RenderHoneycomb() {
    const hexG = document.getElementById('sim1_hex_grid');
    if (!hexG) return;
    let html = '';
    const r = 18;
    const dx = 1.5 * r;
    const dy = Math.sqrt(3) * r;

    for (let q = -4; q <= 4; q++) {
        for (let row = -2; row <= 2; row++) {
            const cx = 200 + q * dx;
            const cy = 100 + row * dy + (q % 2 !== 0 ? dy / 2 : 0);
            if (cx > 40 && cx < 360 && cy > 20 && cy < 180) {
                let pts = [];
                for (let a = 0; a < 6; a++) {
                    const rad = (a * 60) * (Math.PI / 180);
                    pts.push(`${cx + r * Math.cos(rad)},${cy + r * Math.sin(rad)}`);
                }
                html += `<polygon points="${pts.join(' ')}" fill="#1e293b" stroke="#facc15" stroke-width="1.5" opacity="0.85"/>`;
                html += `<circle cx="${cx}" cy="${cy}" r="3" fill="#f59e0b"/>`;
            }
        }
    }
    hexG.innerHTML = html;
}

// Simulator 2: Sequence Generator
function sim2Generate() {
    const startIn = document.getElementById('sim2_start');
    const stepIn = document.getElementById('sim2_step');
    const countSlider = document.getElementById('sim2_count_slider');
    const container = document.getElementById('sim2_term_container');
    const ruleDesc = document.getElementById('sim2_rule_desc');
    const countVal = document.getElementById('sim2_count_val');

    if (!startIn || !stepIn || !container) return;

    let start = parseInt(startIn.value) || 0;
    const stepType = stepIn.value;
    const count = parseInt(countSlider.value) || 6;
    if (countVal) countVal.textContent = `${count} Terms`;

    let terms = [start];
    let desc = '';

    for (let i = 1; i < count; i++) {
        let prev = terms[i - 1];
        if (stepType === 'add_1') {
            terms.push(prev + 1);
            desc = `Start at ${start}, Add 1 each step (Counting Numbers)`;
        } else if (stepType === 'add_2') {
            terms.push(prev + 2);
            desc = `Start at ${start}, Add 2 each step (${start % 2 === 0 ? 'Even' : 'Odd'} Numbers)`;
        } else if (stepType === 'add_3') {
            terms.push(prev + 3);
            desc = `Start at ${start}, Add 3 each step`;
        } else if (stepType === 'add_5') {
            terms.push(prev + 5);
            desc = `Start at ${start}, Add 5 each step`;
        } else if (stepType === 'mul_2') {
            terms.push(prev * 2);
            desc = `Start at ${start}, Multiply by 2 (Doubling / Powers of 2)`;
        } else if (stepType === 'mul_3') {
            terms.push(prev * 3);
            desc = `Start at ${start}, Multiply by 3 (Tripling / Powers of 3)`;
        }
    }

    if (ruleDesc) ruleDesc.textContent = desc;

    let html = '';
    terms.forEach((t, idx) => {
        html += `
            <div class="flex items-center gap-1.5">
                <div class="px-3 py-2 rounded-xl bg-slate-900 border border-slate-700 text-center shadow-md">
                    <span class="block text-[9px] text-slate-400 font-mono">Term ${idx + 1}</span>
                    <span class="text-base font-black text-amber-300 font-mono">${t}</span>
                </div>
                ${idx < terms.length - 1 ? '<span class="text-cyan-400 font-bold text-xs">➔</span>' : '<span class="text-slate-400 font-mono font-bold text-xs">...</span>'}
            </div>
        `;
    });
    container.innerHTML = html;
}

// Simulator 3: Even-Odd Sieve
function sim3SetNumber(val) {
    const n = parseInt(val);
    const numLabel = document.getElementById('sim3_num_label');
    const badge = document.getElementById('sim3_parity_badge');
    const container = document.getElementById('sim3_dots_container');
    const text = document.getElementById('sim3_pairing_text');
    const sliderVal = document.getElementById('sim3_slider_val');

    if (numLabel) numLabel.textContent = n;
    if (sliderVal) sliderVal.textContent = n;

    const isEven = (n % 2 === 0);
    const pairs = Math.floor(n / 2);
    const leftover = n % 2;

    if (badge) {
        if (isEven) {
            badge.textContent = 'EVEN NUMBER (2n)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
        } else {
            badge.textContent = 'ODD NUMBER (2n - 1)';
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30';
        }
    }

    if (text) {
        if (isEven) {
            text.innerHTML = `${n} dots = <strong class="text-emerald-400">${pairs} complete pairs</strong> with <strong class="text-slate-100">0 remainder!</strong>`;
        } else {
            text.innerHTML = `${n} dots = ${pairs} complete pairs + <strong class="text-amber-400">1 lone leftover dot!</strong>`;
        }
    }

    if (container) {
        let html = '';
        for (let p = 0; p < pairs; p++) {
            html += `
                <div class="p-1 rounded-lg bg-slate-900 border border-slate-700 flex flex-col gap-1 items-center">
                    <span class="w-3.5 h-3.5 rounded-full bg-emerald-400"></span>
                    <span class="w-3.5 h-3.5 rounded-full bg-emerald-400"></span>
                </div>
            `;
        }
        if (leftover === 1) {
            html += `
                <div class="p-1 rounded-lg bg-amber-950/60 border border-amber-500/50 flex flex-col gap-1 items-center animate-pulse">
                    <span class="w-3.5 h-3.5 rounded-full bg-amber-400"></span>
                    <span class="w-3.5 h-3.5 rounded-full bg-transparent border border-dashed border-amber-400/40"></span>
                </div>
            `;
        }
        container.innerHTML = html;
    }
}

// Simulator 4: Triangular Numbers Builder
function sim4SetRows(r) {
    const rows = parseInt(r);
    const sliderVal = document.getElementById('sim4_slider_val');
    const termLabel = document.getElementById('sim4_term_label');
    const formulaLabel = document.getElementById('sim4_sum_formula');
    const group = document.getElementById('sim4_dots_group');

    if (sliderVal) sliderVal.textContent = `${rows} Rows`;

    const totalDots = (rows * (rows + 1)) / 2;
    if (termLabel) termLabel.textContent = `T${rows} = ${totalDots} Dots`;

    // Row addition formula string
    let formulaArr = [];
    for (let i = 1; i <= rows; i++) formulaArr.push(i);
    if (formulaLabel) formulaLabel.textContent = `${formulaArr.join(' + ')} = ${totalDots}`;

    if (group) {
        let html = '';
        const spacingX = 22;
        const spacingY = 20;

        for (let row = 1; row <= rows; row++) {
            const startX = -((row - 1) * spacingX) / 2;
            const y = (row - 1) * spacingY;
            for (let col = 0; col < row; col++) {
                const x = startX + col * spacingX;
                html += `<circle cx="${x}" cy="${y}" r="6.5" fill="#f59e0b" stroke="#fef08a" stroke-width="1.2"/>`;
            }
        }
        group.innerHTML = html;
    }
}

// Simulator 5: Square Numbers Builder
function sim5SetSide(s) {
    const side = parseInt(s);
    const sliderVal = document.getElementById('sim5_slider_val');
    const dimLabel = document.getElementById('sim5_dim_label');
    const valLabel = document.getElementById('sim5_val_label');
    const group = document.getElementById('sim5_grid_group');

    if (sliderVal) sliderVal.textContent = side;
    if (dimLabel) dimLabel.textContent = `${side} × ${side} Grid`;
    if (valLabel) valLabel.textContent = `${side * side} Dots (${side}²)`;

    if (group) {
        let html = '';
        const spacing = 18;
        const startX = -((side - 1) * spacing) / 2;
        const startY = -((side - 1) * spacing) / 2;

        for (let r = 0; r < side; r++) {
            for (let c = 0; c < side; c++) {
                const x = startX + c * spacing;
                const y = startY + r * spacing;
                // Highlight the outer gnomon (last row or last column)
                const isOuter = (r === side - 1 || c === side - 1);
                const dotColor = isOuter ? '#38bdf8' : '#64748b';
                html += `<circle cx="${x}" cy="${y}" r="5.5" fill="${dotColor}"/>`;
            }
        }
        group.innerHTML = html;
    }
}

// Simulator 6: 3D Isometric Cube Stacker
function sim6SetCube(nVal) {
    const n = parseInt(nVal);
    const sliderVal = document.getElementById('sim6_slider_val');
    const dimLabel = document.getElementById('sim6_dim_label');
    const valLabel = document.getElementById('sim6_val_label');
    const group = document.getElementById('sim6_isometric_group');

    if (sliderVal) sliderVal.textContent = `n = ${n}`;
    if (dimLabel) dimLabel.textContent = `${n} × ${n} × ${n}`;
    if (valLabel) valLabel.textContent = `${n * n * n} Blocks (${n}³)`;

    if (group) {
        let html = '';
        const s = 18; // cube size

        // Isometric projection constants:
        // x_iso = (x - y) * cos(30) * s
        // y_iso = (x + y) * sin(30) * s - z * s
        const cos30 = Math.cos(Math.PI / 6);
        const sin30 = Math.sin(Math.PI / 6);

        for (let z = 0; z < n; z++) {
            for (let y = n - 1; y >= 0; y--) {
                for (let x = 0; x < n; x++) {
                    const cx = (x - y) * cos30 * s;
                    const cy = (x + y) * sin30 * s - z * s * 1.1;

                    // Draw 3 visible faces of unit cube
                    // Top Face
                    const pTop = `${cx},${cy - s * sin30 * 2} ${cx + s * cos30},${cy - s * sin30} ${cx},${cy} ${cx - s * cos30},${cy - s * sin30}`;
                    // Left Face
                    const pLeft = `${cx - s * cos30},${cy - s * sin30} ${cx},${cy} ${cx},${cy + s} ${cx - s * cos30},${cy + s - s * sin30}`;
                    // Right Face
                    const pRight = `${cx},${cy} ${cx + s * cos30},${cy - s * sin30} ${cx + s * cos30},${cy + s - s * sin30} ${cx},${cy + s}`;

                    html += `<polygon points="${pTop}" fill="#818cf8" stroke="#312e81" stroke-width="0.8"/>`;
                    html += `<polygon points="${pLeft}" fill="#4f46e5" stroke="#312e81" stroke-width="0.8"/>`;
                    html += `<polygon points="${pRight}" fill="#3730a3" stroke="#312e81" stroke-width="0.8"/>`;
                }
            }
        }
        group.innerHTML = html;
    }
}

// Simulator 7: Virahānka Stepper
let sim7Seq = [1, 1, 2, 3, 5, 8, 13];
function sim7Step() {
    playSound('click');
    const len = sim7Seq.length;
    const nextVal = sim7Seq[len - 1] + sim7Seq[len - 2];
    sim7Seq.push(nextVal);
    sim7UpdateUI();
}

function sim7Reset() {
    playSound('click');
    sim7Seq = [1, 1, 2, 3, 5, 8, 13];
    sim7UpdateUI();
}

function sim7UpdateUI() {
    const len = sim7Seq.length;
    const curVal = sim7Seq[len - 1];
    const prev1 = sim7Seq[len - 2];
    const prev2 = sim7Seq[len - 3];

    const termL = document.getElementById('sim7_term_label');
    const calcL = document.getElementById('sim7_calc_label');
    const group = document.getElementById('sim7_tiles_group');

    if (termL) termL.textContent = `V${len} = ${curVal}`;
    if (calcL) calcL.textContent = `${prev2} + ${prev1} = ${curVal}`;

    if (group) {
        let html = '';
        // Draw Fibonacci spiral tiles
        let w = 15;
        html += `<rect x="-10" y="-10" width="20" height="20" fill="#38bdf8" opacity="0.7" stroke="#ffffff"/>`;
        html += `<rect x="10" y="-10" width="20" height="20" fill="#facc15" opacity="0.7" stroke="#ffffff"/>`;
        html += `<rect x="-10" y="10" width="40" height="40" fill="#22c55e" opacity="0.7" stroke="#ffffff"/>`;
        html += `<rect x="-70" y="-10" width="60" height="60" fill="#ec4899" opacity="0.7" stroke="#ffffff"/>`;
        group.innerHTML = html;
    }
}

// Simulator 8: Exponential Tree
let sim8Base = 2;
function sim8SetBase(b) {
    playSound('click');
    sim8Base = parseInt(b);
    const b2 = document.getElementById('sim8_btn_2');
    const b3 = document.getElementById('sim8_btn_3');
    if (sim8Base === 2) {
        if (b2) b2.className = 'flex-1 py-1.5 rounded-lg bg-cyan-600 text-white font-bold text-xs transition';
        if (b3) b3.className = 'flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition';
    } else {
        if (b3) b3.className = 'flex-1 py-1.5 rounded-lg bg-amber-600 text-white font-bold text-xs transition';
        if (b2) b2.className = 'flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition';
    }
    const slider = document.getElementById('sim8_slider');
    sim8SetLevel(slider ? slider.value : 4);
}

function sim8SetLevel(val) {
    const level = parseInt(val);
    const lvlLabel = document.getElementById('sim8_level_label');
    const totLabel = document.getElementById('sim8_total_label');
    const group = document.getElementById('sim8_tree_group');

    const totalNodes = Math.pow(sim8Base, level);
    if (lvlLabel) lvlLabel.textContent = `Step n = ${level}`;
    if (totLabel) totLabel.textContent = `${sim8Base}ⁿ = ${totalNodes} Nodes`;

    if (group) {
        let html = '';
        // Draw simple branching tree
        const depth = Math.min(level, 4); // limit visual rendering to depth 4
        function drawBranches(x, y, d, spread) {
            if (d >= depth) {
                html += `<circle cx="${x}" cy="${y}" r="3.5" fill="#facc15"/>`;
                return;
            }
            html += `<circle cx="${x}" cy="${y}" r="4" fill="#38bdf8"/>`;
            const nextY = y + 36;
            if (sim8Base === 2) {
                const x1 = x - spread;
                const x2 = x + spread;
                html += `<line x1="${x}" y1="${y}" x2="${x1}" y2="${nextY}" stroke="#64748b" stroke-width="1.2"/>`;
                html += `<line x1="${x}" y1="${y}" x2="${x2}" y2="${nextY}" stroke="#64748b" stroke-width="1.2"/>`;
                drawBranches(x1, nextY, d + 1, spread / 2);
                drawBranches(x2, nextY, d + 1, spread / 2);
            } else {
                const x1 = x - spread;
                const x2 = x;
                const x3 = x + spread;
                html += `<line x1="${x}" y1="${y}" x2="${x1}" y2="${nextY}" stroke="#64748b" stroke-width="1.2"/>`;
                html += `<line x1="${x}" y1="${y}" x2="${x2}" y2="${nextY}" stroke="#64748b" stroke-width="1.2"/>`;
                html += `<line x1="${x}" y1="${y}" x2="${x3}" y2="${nextY}" stroke="#64748b" stroke-width="1.2"/>`;
                drawBranches(x1, nextY, d + 1, spread / 2.8);
                drawBranches(x2, nextY, d + 1, spread / 2.8);
                drawBranches(x3, nextY, d + 1, spread / 2.8);
            }
        }
        drawBranches(190, 25, 0, 80);
        group.innerHTML = html;
    }
}

// Simulator 9: The Chameleon 36 Morphing Lab
let sim9IsSquare = false;
function sim9ToggleMorph() {
    playSound('click');
    sim9IsSquare = !sim9IsSquare;
    const btn = document.getElementById('sim9_morph_btn');
    const roleL = document.getElementById('sim9_role_label');
    const formulaL = document.getElementById('sim9_formula_label');
    const group = document.getElementById('sim9_dots_group');

    if (sim9IsSquare) {
        if (btn) btn.textContent = '🔄 Morph 36: Square (6 × 6) ➔ Triangle (T₈)';
        if (roleL) roleL.textContent = 'Square Number (6²)';
        if (formulaL) formulaL.textContent = '6 × 6 = 6² = 36 Dots';
    } else {
        if (btn) btn.textContent = '🔄 Morph 36: Triangle (T₈) ➔ Square (6 × 6)';
        if (roleL) roleL.textContent = 'Triangular Number (T₈)';
        if (formulaL) formulaL.textContent = '1+2+3+4+5+6+7+8 = 36 Dots';
    }

    if (group) {
        let html = '';
        if (sim9IsSquare) {
            // 6x6 square
            const spacing = 20;
            const startX = -2.5 * spacing;
            const startY = -2.5 * spacing;
            for (let r = 0; r < 6; r++) {
                for (let c = 0; c < 6; c++) {
                    const x = startX + c * spacing;
                    const y = startY + r * spacing;
                    html += `<circle cx="${x}" cy="${y}" r="6" fill="#38bdf8" stroke="#ffffff" stroke-width="1"/>`;
                }
            }
        } else {
            // 8-row triangle
            const spacingX = 20;
            const spacingY = 18;
            let count = 0;
            for (let row = 1; row <= 8; row++) {
                const startX = -((row - 1) * spacingX) / 2;
                const y = -70 + (row - 1) * spacingY;
                for (let col = 0; col < row; col++) {
                    const x = startX + col * spacingX;
                    html += `<circle cx="${x}" cy="${y}" r="6" fill="#f59e0b" stroke="#ffffff" stroke-width="1"/>`;
                    count++;
                }
            }
        }
        group.innerHTML = html;
    }
}

// Simulator 10: Centered Hexagonal Numbers
function sim10SetRing(val) {
    const ring = parseInt(val);
    const ringL = document.getElementById('sim10_ring_label');
    const totL = document.getElementById('sim10_total_label');
    const group = document.getElementById('sim10_hex_group');

    // Centered hex formula: 3n(n-1) + 1 for n=1..5 (or 3*r*(r+1) + 1)
    const total = 3 * ring * (ring + 1) + 1;
    const addedThisRing = ring === 0 ? 1 : 6 * ring;

    if (ringL) ringL.textContent = ring === 0 ? 'Center Dot (+1)' : `Ring ${ring} (+${addedThisRing} dots)`;
    if (totL) totL.textContent = `${total} Dots (H${ring + 1})`;

    if (group) {
        let html = '';
        // Central dot
        html += `<circle cx="0" cy="0" r="6" fill="#facc15"/>`;

        const colors = ['#f59e0b', '#22c55e', '#38bdf8', '#a855f7'];
        const stepR = 20;

        for (let r = 1; r <= ring; r++) {
            const cColor = colors[(r - 1) % colors.length];
            for (let side = 0; side < 6; side++) {
                const a1 = (side * 60) * (Math.PI / 180);
                const a2 = ((side + 1) * 60) * (Math.PI / 180);
                const cornerX1 = r * stepR * Math.cos(a1);
                const cornerY1 = r * stepR * Math.sin(a1);
                const cornerX2 = r * stepR * Math.cos(a2);
                const cornerY2 = r * stepR * Math.sin(a2);

                for (let step = 0; step < r; step++) {
                    const frac = step / r;
                    const x = cornerX1 + frac * (cornerX2 - cornerX1);
                    const y = cornerY1 + frac * (cornerY2 - cornerY1);
                    html += `<circle cx="${x}" cy="${y}" r="5" fill="${cColor}"/>`;
                }
            }
        }
        group.innerHTML = html;
    }
}

// Simulator 11: L-Shaped Gnomon Builder
function sim11SetLayer(val) {
    const n = parseInt(val);
    const sumEq = document.getElementById('sim11_sum_eq');
    const sqEq = document.getElementById('sim11_square_eq');
    const sliderVal = document.getElementById('sim11_slider_val');
    const group = document.getElementById('sim11_gnomon_group');

    if (sliderVal) sliderVal.textContent = `n = ${n}`;

    let oddArr = [];
    for (let i = 1; i <= n; i++) oddArr.push(2 * i - 1);
    if (sumEq) sumEq.textContent = `${oddArr.join(' + ')} = ${n * n}`;
    if (sqEq) sqEq.textContent = `${n} × ${n} = ${n}² = ${n * n} Dots`;

    if (group) {
        let html = '';
        const spacing = 20;
        const startX = -((n - 1) * spacing) / 2;
        const startY = -((n - 1) * spacing) / 2;
        const layerColors = ['#facc15', '#38bdf8', '#22c55e', '#f97316', '#a855f7', '#ec4899'];

        for (let r = 0; r < n; r++) {
            for (let c = 0; c < n; c++) {
                const layer = Math.max(r, c);
                const color = layerColors[layer % layerColors.length];
                const x = startX + c * spacing;
                const y = startY + r * spacing;
                html += `<circle cx="${x}" cy="${y}" r="6.5" fill="${color}" stroke="#030712" stroke-width="1"/>`;
            }
        }
        group.innerHTML = html;
    }
}

// Simulator 12: Mountain Sum Visualizer
function sim12SetPeak(val) {
    const peak = parseInt(val);
    const sumText = document.getElementById('sim12_sum_text');
    const peakText = document.getElementById('sim12_peak_text');
    const group = document.getElementById('sim12_diag_group');

    let arr = [];
    for (let i = 1; i <= peak; i++) arr.push(i);
    for (let i = peak - 1; i >= 1; i--) arr.push(i);

    const total = peak * peak;
    if (sumText) sumText.textContent = `${arr.join(' + ')} = ${total}`;
    if (peakText) peakText.textContent = `Peak = ${peak} ➔ ${peak}² = ${total}`;

    if (group) {
        let html = '';
        const spacing = 20;
        const startX = -((peak - 1) * spacing) / 2;
        const startY = -((peak - 1) * spacing) / 2;

        const diagColors = ['#38bdf8', '#22c55e', '#facc15', '#ec4899', '#a855f7', '#f97316'];

        for (let r = 0; r < peak; r++) {
            for (let c = 0; c < peak; c++) {
                const diagIdx = r + c; // diagonal slice index
                const color = diagColors[diagIdx % diagColors.length];
                const x = startX + c * spacing;
                const y = startY + r * spacing;
                html += `<circle cx="${x}" cy="${y}" r="6" fill="${color}"/>`;
            }
        }
        group.innerHTML = html;
    }
}

// Simulator 13: Regular Polygon Morphing
const polyNames = {
    3: 'Equilateral Triangle',
    4: 'Square',
    5: 'Regular Pentagon',
    6: 'Regular Hexagon',
    7: 'Regular Heptagon',
    8: 'Regular Octagon',
    9: 'Regular Nonagon',
    10: 'Regular Decagon'
};

function sim13SetSides(val) {
    const n = parseInt(val);
    const nameL = document.getElementById('sim13_name_label');
    const angleL = document.getElementById('sim13_angle_label');
    const sliderVal = document.getElementById('sim13_slider_val');
    const group = document.getElementById('sim13_poly_group');

    if (nameL) nameL.textContent = `${polyNames[n]} (${n})`;
    if (angleL) angleL.textContent = `(${n}−2) × 180° = ${(n - 2) * 180}°`;
    if (sliderVal) sliderVal.textContent = `${n} Sides`;

    if (group) {
        let pts = [];
        let html = '';
        const r = 70;
        for (let i = 0; i < n; i++) {
            const rad = (i * 360 / n - 90) * (Math.PI / 180);
            const x = r * Math.cos(rad);
            const y = r * Math.sin(rad);
            pts.push(`${x},${y}`);
        }
        html += `<polygon points="${pts.join(' ')}" fill="#0284c7" stroke="#38bdf8" stroke-width="2.5" opacity="0.6"/>`;
        // Vertices dots
        for (let i = 0; i < n; i++) {
            const rad = (i * 360 / n - 90) * (Math.PI / 180);
            const x = r * Math.cos(rad);
            const y = r * Math.sin(rad);
            html += `<circle cx="${x}" cy="${y}" r="5" fill="#facc15" stroke="#ffffff" stroke-width="1.5"/>`;
        }
        group.innerHTML = html;
    }
}

// Simulator 14: Complete Graph Simulator
function sim14SetVertices(val) {
    const n = parseInt(val);
    const vertL = document.getElementById('sim14_vert_label');
    const edgeL = document.getElementById('sim14_edge_label');
    const sliderVal = document.getElementById('sim14_slider_val');
    const group = document.getElementById('sim14_graph_group');

    const edges = (n * (n - 1)) / 2;
    if (vertL) vertL.textContent = `n = ${n} Points (K${n})`;
    if (edgeL) edgeL.textContent = `${edges} Edges (T${n - 1})`;
    if (sliderVal) sliderVal.textContent = `${n} Vertices`;

    if (group) {
        let html = '';
        const r = 70;
        let coords = [];
        for (let i = 0; i < n; i++) {
            const rad = (i * 360 / n - 90) * (Math.PI / 180);
            coords.push({ x: r * Math.cos(rad), y: r * Math.sin(rad) });
        }

        // Draw all chords
        for (let i = 0; i < n; i++) {
            for (let j = i + 1; j < n; j++) {
                html += `<line x1="${coords[i].x}" y1="${coords[i].y}" x2="${coords[j].x}" y2="${coords[j].y}" stroke="#38bdf8" stroke-width="1.2" opacity="0.7"/>`;
            }
        }
        // Draw vertex dots
        coords.forEach(pt => {
            html += `<circle cx="${pt.x}" cy="${pt.y}" r="6" fill="#f59e0b" stroke="#ffffff" stroke-width="1.5"/>`;
        });
        group.innerHTML = html;
    }
}

// Simulator 15: Stacked Pyramids
let sim15Mode = 'square';
function sim15SetMode(m) {
    playSound('click');
    sim15Mode = m;
    const btnSq = document.getElementById('sim15_btn_sq');
    const btnTri = document.getElementById('sim15_btn_tri');
    if (m === 'square') {
        if (btnSq) btnSq.className = 'flex-1 py-1.5 rounded-lg bg-indigo-600 text-white font-bold text-xs transition';
        if (btnTri) btnTri.className = 'flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition';
    } else {
        if (btnTri) btnTri.className = 'flex-1 py-1.5 rounded-lg bg-amber-600 text-white font-bold text-xs transition';
        if (btnSq) btnSq.className = 'flex-1 py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition';
    }
    const slider = document.getElementById('sim15_slider');
    sim15SetLevel(slider ? slider.value : 3);
}

function sim15SetLevel(val) {
    const level = parseInt(val);
    const typeL = document.getElementById('sim15_type_label');
    const totL = document.getElementById('sim15_total_label');
    const group = document.getElementById('sim15_pyramid_group');

    if (sim15Mode === 'square') {
        let total = 0;
        let terms = [];
        for (let i = 1; i <= level; i++) {
            total += i * i;
            terms.push(`${i * i}`);
        }
        if (typeL) typeL.textContent = `Stacked Squares (${level} Levels)`;
        if (totL) totL.textContent = `${terms.join(' + ')} = ${total} Blocks`;
    } else {
        let total = 0;
        let terms = [];
        for (let i = 1; i <= level; i++) {
            const tri = (i * (i + 1)) / 2;
            total += tri;
            terms.push(`${tri}`);
        }
        if (typeL) typeL.textContent = `Stacked Triangles (Tetrahedral)`;
        if (totL) totL.textContent = `${terms.join(' + ')} = ${total} Blocks`;
    }

    if (group) {
        let html = '';
        // Draw stacked isometric tiers
        const s = 14;
        const cos30 = Math.cos(Math.PI / 6);
        const sin30 = Math.sin(Math.PI / 6);

        for (let lvl = 0; lvl < level; lvl++) {
            const countOnSide = level - lvl;
            const z = lvl * s * 1.2;
            const startX = -((countOnSide - 1) * s * cos30) / 2;
            const startY = ((countOnSide - 1) * s * sin30) / 2;

            for (let r = 0; r < countOnSide; r++) {
                const limit = sim15Mode === 'square' ? countOnSide : (countOnSide - r);
                for (let c = 0; c < limit; c++) {
                    const cx = (c - r) * cos30 * s;
                    const cy = (c + r) * sin30 * s - z;

                    const pTop = `${cx},${cy - s * sin30 * 2} ${cx + s * cos30},${cy - s * sin30} ${cx},${cy} ${cx - s * cos30},${cy - s * sin30}`;
                    html += `<polygon points="${pTop}" fill="#6366f1" stroke="#312e81" stroke-width="0.8"/>`;
                }
            }
        }
        group.innerHTML = html;
    }
}

// Simulator 16: Koch Snowflake Fractal
function sim16SetIter(iter) {
    playSound('click');
    const k = parseInt(iter);
    const iterL = document.getElementById('sim16_iter_label');
    const edgesL = document.getElementById('sim16_edges_label');
    const group = document.getElementById('sim16_fractal_group');

    for (let i = 0; i <= 3; i++) {
        const b = document.getElementById(`sim16_btn_${i}`);
        if (b) {
            b.className = (i === k) ? 'py-1.5 rounded-lg bg-cyan-600 text-white font-bold text-xs transition shadow' : 'py-1.5 rounded-lg bg-slate-800 text-slate-300 font-bold text-xs border border-slate-700 transition';
        }
    }

    const totalEdges = 3 * Math.pow(4, k);
    if (iterL) iterL.textContent = `Iteration ${k}`;
    if (edgesL) edgesL.textContent = `3 × 4^${k} = ${totalEdges} Edges`;

    if (group) {
        let r = 75;
        // 3 initial vertices of equilateral triangle
        let v1 = { x: 0, y: -r };
        let v2 = { x: r * Math.cos(Math.PI / 6), y: r * Math.sin(Math.PI / 6) };
        let v3 = { x: -r * Math.cos(Math.PI / 6), y: r * Math.sin(Math.PI / 6) };

        function getKochPoints(p1, p2, depth) {
            if (depth === 0) return [p1];
            const dx = (p2.x - p1.x) / 3;
            const dy = (p2.y - p1.y) / 3;

            const a = p1;
            const b = { x: p1.x + dx, y: p1.y + dy };
            const d = { x: p1.x + 2 * dx, y: p1.y + 2 * dy };

            // Apex point c rotated 60 deg outward
            const cos60 = Math.cos(Math.PI / 3);
            const sin60 = Math.sin(Math.PI / 3);
            const cx = b.x + dx * cos60 + dy * sin60;
            const cy = b.y - dx * sin60 + dy * cos60;
            const c = { x: cx, y: cy };

            return [
                ...getKochPoints(a, b, depth - 1),
                ...getKochPoints(b, c, depth - 1),
                ...getKochPoints(c, d, depth - 1),
                ...getKochPoints(d, p2, depth - 1)
            ];
        }

        const pts = [
            ...getKochPoints(v1, v2, k),
            ...getKochPoints(v2, v3, k),
            ...getKochPoints(v3, v1, k)
        ];

        let polyStr = pts.map(p => `${p.x},${p.y}`).join(' ');
        group.innerHTML = `<polygon points="${polyStr}" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5" opacity="0.75"/>`;
    }
}

// Initialize on page load
window.addEventListener('DOMContentLoaded', () => {
    goToSlide(1);
    sim1InitSunflower();
    sim2Generate();
    sim3SetNumber(7);
    sim4SetRows(4);
    sim5SetSide(5);
    sim6SetCube(3);
    sim7Reset();
    sim8SetLevel(4);
    sim9ToggleMorph(); // initialize triangle
    sim10SetRing(2);
    sim11SetLayer(4);
    sim12SetPeak(4);
    sim13SetSides(6);
    sim14SetVertices(5);
    sim15SetLevel(3);
    sim16SetIter(1);
});
"""
'''
    with open(".agents/class6_math_patterns_js.py", "w", encoding="utf-8") as f:
        f.write(code)

    print("Successfully generated .agents/class6_math_patterns_js.py.")

if __name__ == "__main__":
    create_js_file()

