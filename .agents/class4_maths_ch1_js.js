
// Web Audio API Synthesizer for Interactive Feedback
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
function playChime(isCorrect) {
    if (!audioCtx) return;
    try {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        const now = audioCtx.currentTime;
        if (isCorrect) {
            osc.type = 'sine';
            osc.frequency.setValueAtTime(523.25, now); // C5
            osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.12); // E5
            osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.25); // G5
            gain.gain.setValueAtTime(0.15, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
            osc.start(now);
            osc.stop(now + 0.35);
        } else {
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(220, now);
            osc.frequency.exponentialRampToValueAtTime(160, now + 0.2);
            gain.gain.setValueAtTime(0.12, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
            osc.start(now);
            osc.stop(now + 0.25);
        }
    } catch(e) {}
}

// Global State
let currentSlide = 1;
const totalSlides = 20;
let isAudioPlaying = false;
let currentUtterance = null;
let speechPingInterval = null;

// Speech Synthesis: Authentic Indian English Male Priority
function selectIndianMaleVoice(voices) {
    if (!voices || voices.length === 0) return null;
    
    // Hard filter female names
    const femaleRegex = /female|woman|girl|zira|jenny|aria|samantha|priya|swara|veena|neerja|heera|kavya|shreya|ananya|aditi/i;
    
    // Top Priority: Dedicated Indian Male voices
    const indianMaleKeywords = ['prabhat', 'rishi', 'ravi', 'pradeep', 'madhav', 'karan', 'mohan'];
    for (const v of voices) {
        const name = v.name.toLowerCase();
        const lang = (v.lang || '').toLowerCase();
        if (femaleRegex.test(name)) continue;
        if ((lang.includes('en-in') || lang.includes('hi')) && indianMaleKeywords.some(k => name.includes(k))) {
            return v;
        }
    }
    
    // Second: Any Indian English male voice
    for (const v of voices) {
        const name = v.name.toLowerCase();
        const lang = (v.lang || '').toLowerCase();
        if (femaleRegex.test(name)) continue;
        if (lang.includes('en-in') && (name.includes('male') || !femaleRegex.test(name))) {
            return v;
        }
    }
    
    // Third: Standard male fallbacks
    const maleFallbacks = ['google uk english male', 'microsoft david', 'microsoft mark', 'alex', 'daniel', 'oliver', 'george'];
    for (const v of voices) {
        const name = v.name.toLowerCase();
        if (femaleRegex.test(name)) continue;
        if (maleFallbacks.some(f => name.includes(f))) {
            return v;
        }
    }
    
    // Fourth: Any English voice that is not female
    for (const v of voices) {
        const name = v.name.toLowerCase();
        const lang = (v.lang || '').toLowerCase();
        if (!femaleRegex.test(name) && lang.startsWith('en')) {
            return v;
        }
    }
    return voices[0] || null;
}

function speakCurrentLecture() {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    if (speechPingInterval) {
        clearInterval(speechPingInterval);
        speechPingInterval = null;
    }
    
    if (currentSlide > 16) {
        setAudioUI(false);
        return;
    }
    
    const slideData = slidesData[currentSlide - 1];
    if (!slideData || !slideData.lecture) {
        setAudioUI(false);
        return;
    }
    
    currentUtterance = new SpeechSynthesisUtterance(slideData.lecture);
    currentUtterance.rate = 0.94;
    currentUtterance.pitch = 0.85;
    
    const voices = window.speechSynthesis.getVoices();
    const chosenVoice = selectIndianMaleVoice(voices);
    if (chosenVoice) {
        currentUtterance.voice = chosenVoice;
    }
    
    currentUtterance.onstart = () => {
        setAudioUI(true);
        // Chrome watchdog keep-alive (every 10s)
        speechPingInterval = setInterval(() => {
            if (window.speechSynthesis.speaking) {
                window.speechSynthesis.pause();
                window.speechSynthesis.resume();
            } else {
                clearInterval(speechPingInterval);
                speechPingInterval = null;
            }
        }, 10000);
    };
    
    currentUtterance.onend = () => {
        setAudioUI(false);
        if (speechPingInterval) {
            clearInterval(speechPingInterval);
            speechPingInterval = null;
        }
    };
    
    currentUtterance.onerror = () => {
        setAudioUI(false);
        if (speechPingInterval) {
            clearInterval(speechPingInterval);
            speechPingInterval = null;
        }
    };
    
    window.speechSynthesis.speak(currentUtterance);
}

function stopSpeech() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    if (speechPingInterval) {
        clearInterval(speechPingInterval);
        speechPingInterval = null;
    }
    setAudioUI(false);
}

function toggleAudio() {
    if (isAudioPlaying) {
        stopSpeech();
    } else {
        speakCurrentLecture();
    }
}

function setAudioUI(playing) {
    isAudioPlaying = playing;
    const btn = document.getElementById('audioToggleBtn');
    const label = document.getElementById('audioStatusLabel');
    if (btn && label) {
        if (playing) {
            btn.classList.add('bg-amber-500', 'text-slate-950', 'animate-pulse');
            btn.classList.remove('bg-slate-800', 'text-slate-300');
            label.textContent = "Narration Playing";
        } else {
            btn.classList.remove('bg-amber-500', 'text-slate-950', 'animate-pulse');
            btn.classList.add('bg-slate-800', 'text-slate-300');
            label.textContent = "Start Narration";
        }
    }
}

// Navigation & Slide Rendering
function goToSlide(slideNum) {
    if (slideNum < 1 || slideNum > totalSlides) return;
    stopSpeech();
    
    // Hide previous slide
    const prevEl = document.getElementById(`slide-${currentSlide}`);
    if (prevEl) prevEl.classList.add('hidden');
    
    currentSlide = slideNum;
    
    // Show new slide
    const curEl = document.getElementById(`slide-${currentSlide}`);
    if (curEl) curEl.classList.remove('hidden');
    
    // Update counter & progress bar
    const counterEl = document.getElementById('slideCounter');
    if (counterEl) counterEl.textContent = `Slide ${currentSlide} of ${totalSlides}`;
    
    const progressEl = document.getElementById('progressBar');
    if (progressEl) {
        const pct = (currentSlide / totalSlides) * 100;
        progressEl.style.width = `${pct}%`;
    }
    
    // Update Prev / Next buttons
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');
    
    if (prevBtn) {
        prevBtn.disabled = (currentSlide === 1);
        if (currentSlide === 1) {
            prevBtn.classList.add('opacity-40', 'cursor-not-allowed');
        } else {
            prevBtn.classList.remove('opacity-40', 'cursor-not-allowed');
        }
    }
    
    // Terminal Slide Invariant for Slide 20
    if (currentSlide === 20) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) {
            lastNotice.style.display = 'block';
            lastNotice.classList.remove('hidden');
        }
    } else {
        if (nextBtn) {
            nextBtn.style.display = 'inline-flex';
            nextBtn.classList.remove('hidden');
        }
        if (lastNotice) {
            lastNotice.style.display = 'none';
            lastNotice.classList.add('hidden');
        }
    }
    
    // Re-initialize active simulator
    initSimulator(currentSlide);
    
    // Scroll view to top of content
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

// Solution Modal Handlers
function openSolutionModal(slideIndex, qIndex) {
    const slide = slidesData[slideIndex];
    if (!slide || !slide.questions) return;
    const q = slide.questions[qIndex];
    if (!q) return;
    
    const modal = document.getElementById('solutionModal');
    const title = document.getElementById('modalQuestionTitle');
    const content = document.getElementById('modalSolutionContent');
    
    if (title) title.textContent = `Challenge Question ${slideIndex === 16 ? qIndex + 1 : (slideIndex === 17 ? qIndex + 11 : (slideIndex === 18 ? qIndex + 21 : qIndex + 31))}`;
    if (content) {
        content.innerHTML = `
            <div class="mb-4">
                <p class="font-bold text-slate-100 text-base mb-2">${q.q}</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                    ${q.options.map((opt, i) => `
                        <div class="p-2 rounded-lg ${i === q.ans ? 'bg-emerald-950/80 border border-emerald-500/60 text-emerald-300 font-bold' : 'bg-slate-800/60 border border-slate-700/60 text-slate-400'}">
                            ${String.fromCharCode(65 + i)}. ${opt} ${i === q.ans ? '✓ (Correct)' : ''}
                        </div>
                    `).join('')}
                </div>
            </div>
            ${q.solution_html}
        `;
    }
    if (modal) modal.classList.remove('hidden');
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) modal.classList.add('hidden');
}

// Checkpoint Interaction
function handleCheckpoint(slideId, cpIdx, selectedOpt, correctOpt) {
    const cpContainer = document.getElementById(`cp-${slideId}-${cpIdx}`);
    if (!cpContainer) return;
    
    const opts = cpContainer.querySelectorAll('.cp-opt-btn');
    const expl = document.getElementById(`cp-expl-${slideId}-${cpIdx}`);
    
    opts.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === correctOpt) {
            btn.classList.add('bg-emerald-600', 'text-white', 'border-emerald-400');
            btn.classList.remove('bg-slate-800', 'text-slate-300');
        } else if (idx === selectedOpt && selectedOpt !== correctOpt) {
            btn.classList.add('bg-rose-600', 'text-white', 'border-rose-400');
            btn.classList.remove('bg-slate-800', 'text-slate-300');
        }
    });
    
    const isCorrect = (selectedOpt === correctOpt);
    playChime(isCorrect);
    
    if (expl) {
        expl.classList.remove('hidden');
    }
}

// Quiz Interaction (Slides 17 to 20)
function handleQuizAnswer(slideIndex, qIndex, selectedOpt, correctOpt) {
    const qContainer = document.getElementById(`quiz-${slideIndex}-${qIndex}`);
    if (!qContainer) return;
    
    const opts = qContainer.querySelectorAll('.quiz-opt-btn');
    const feedback = document.getElementById(`quiz-feedback-${slideIndex}-${qIndex}`);
    
    opts.forEach((btn, idx) => {
        btn.disabled = true;
        if (idx === correctOpt) {
            btn.classList.add('bg-emerald-600', 'text-white', 'border-emerald-400');
            btn.classList.remove('bg-slate-800', 'text-slate-300');
        } else if (idx === selectedOpt && selectedOpt !== correctOpt) {
            btn.classList.add('bg-rose-600', 'text-white', 'border-rose-400');
            btn.classList.remove('bg-slate-800', 'text-slate-300');
        }
    });
    
    const isCorrect = (selectedOpt === correctOpt);
    playChime(isCorrect);
    
    if (feedback) {
        feedback.classList.remove('hidden');
    }
}

function toggleQuizHint(slideIndex, qIndex) {
    const hintBox = document.getElementById(`quiz-hint-${slideIndex}-${qIndex}`);
    if (hintBox) {
        hintBox.classList.toggle('hidden');
    }
}

// ==========================================
// BESPOKE SIMULATOR CONTROLLERS (1 to 16)
// ==========================================

function initSimulator(slideId) {
    switch (slideId) {
        case 1: sim1Step(0); break;
        case 2: sim2SetTab(1); break;
        case 3: sim3Render(); break;
        case 4: sim4Render(); break;
        case 5: sim5SetTab(1); break;
        case 6: sim6Reset(); break;
        case 7: sim7Render(); break;
        case 8: sim8Render(); break;
        case 9: sim9Render(); break;
        case 10: sim10Render(); break;
        case 11: sim11Render(); break;
        case 12: sim12Render(); break;
        case 13: sim13Render(); break;
        case 14: sim14SetState('original'); break;
        case 15: sim15ResetMatches(); break;
        case 16: sim16Render(); break;
    }
}

// Sim 1: India Gate Monument Block Builder
let sim1CurrentStep = 0;
function sim1Step(step) {
    sim1CurrentStep = step;
    const base = document.getElementById('sim1-base');
    const pLeft = document.getElementById('sim1-pillar-left');
    const pRight = document.getElementById('sim1-pillar-right');
    const arch = document.getElementById('sim1-arch');
    const roof = document.getElementById('sim1-roof');
    const info = document.getElementById('sim1-info');
    
    if (!base) return;
    
    // Reset all
    [base, pLeft, pRight, arch, roof].forEach(el => {
        if (el) {
            el.classList.add('opacity-0');
            el.classList.remove('opacity-100', 'translate-y-0');
        }
    });
    
    if (step >= 1 && base) {
        base.classList.remove('opacity-0');
        base.classList.add('opacity-100');
    }
    if (step >= 2) {
        if (pLeft) pLeft.classList.remove('opacity-0');
        if (pRight) pRight.classList.remove('opacity-0');
    }
    if (step >= 3 && arch) {
        arch.classList.remove('opacity-0');
    }
    if (step >= 4 && roof) {
        roof.classList.remove('opacity-0');
    }
    
    const msgs = [
        "Click step buttons below to assemble India Gate piece by piece!",
        "Step 1: Solid foundation base added! A wide cuboid provides flat ground support.",
        "Step 2: Two vertical cuboid pillars rise symmetrically to support upper weight.",
        "Step 3: Curved arch spans the central portal, distributing downward loads to pillars.",
        "Step 4: Horizontal cornice slab rests across the top to complete India Gate monument!"
    ];
    if (info) info.textContent = msgs[step];
}

// Sim 2: Qutub Minar Storeys & Brick Bond
let sim2CurrentTab = 1;
function sim2SetTab(t) {
    sim2CurrentTab = t;
    const tab1 = document.getElementById('sim2-tab1');
    const tab2 = document.getElementById('sim2-tab2');
    const btn1 = document.getElementById('sim2-tab1-btn');
    const btn2 = document.getElementById('sim2-tab2-btn');
    
    if (t === 1) {
        if (tab1) tab1.classList.remove('hidden');
        if (tab2) tab2.classList.add('hidden');
        if (btn1) { btn1.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition'; }
        if (btn2) { btn2.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition'; }
    } else {
        if (tab1) tab1.classList.add('hidden');
        if (tab2) tab2.classList.remove('hidden');
        if (btn2) { btn2.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition'; }
        if (btn1) { btn1.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition'; }
        sim2SetBond('running');
    }
}

function sim2SelectStorey(s) {
    const title = document.getElementById('sim2-storey-title');
    const desc = document.getElementById('sim2-storey-desc');
    const storeyData = [
        {},
        { name: "Storey 1 (Base Floor)", text: "Built with red sandstone fluting and angular ribs. Forms the widest base foundation anchor." },
        { name: "Storey 2 (Second Balcony)", text: "Features alternating rounded and sharp vertical flutes in carved red sandstone." },
        { name: "Storey 3 (Third Balcony)", text: "Comprises purely rounded flutes and decorative Arabic calligraphy bands." },
        { name: "Storey 4 (Marble Floor)", text: "Reconstructed using white Makrana marble and red sandstone with arched balconies." },
        { name: "Storey 5 (Top Storey)", text: "The highest crown level at 72.5 meters. 379 winding internal spiral stairs lead here." }
    ];
    if (title && storeyData[s]) title.textContent = storeyData[s].name;
    if (desc && storeyData[s]) desc.textContent = storeyData[s].text;
}

let sim2CurrentBond = 'running';
function sim2SetBond(bond) {
    sim2CurrentBond = bond;
    const btnR = document.getElementById('sim2-bond-running');
    const btnS = document.getElementById('sim2-bond-stack');
    const svg = document.getElementById('sim2-brick-svg');
    const verdict = document.getElementById('sim2-bond-verdict');
    
    if (btnR && btnS) {
        if (bond === 'running') {
            btnR.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600 text-white shadow';
            btnS.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white';
            if (verdict) verdict.textContent = "Running bond staggers vertical seams, spreading load across multiple bricks without continuous cracks!";
        } else {
            btnS.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold bg-rose-600 text-white shadow';
            btnR.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white';
            if (verdict) verdict.textContent = "Stack bond aligns vertical joints in a straight line: vertical cracks split through easily!";
        }
    }
    
    if (!svg) return;
    let html = '';
    const rows = 4;
    const bW = 60, bH = 26;
    
    for (let r = 0; r < rows; r++) {
        const y = 20 + r * (bH + 4);
        if (bond === 'running') {
            const offset = (r % 2 === 1) ? bW / 2 : 0;
            for (let x = 10 - offset; x < 350; x += (bW + 4)) {
                html += `<rect x="${x}" y="${y}" width="${bW}" height="${bH}" rx="3" fill="#ea580c" stroke="#f97316" stroke-width="1.5"/>`;
            }
        } else {
            for (let x = 20; x < 340; x += (bW + 4)) {
                html += `<rect x="${x}" y="${y}" width="${bW}" height="${bH}" rx="3" fill="#dc2626" stroke="#ef4444" stroke-width="1.5"/>`;
            }
        }
    }
    
    // Add load arrow and crack line
    if (bond === 'stack') {
        html += `<path d="M 148,15 L 148,135" stroke="#facc15" stroke-width="3" stroke-dasharray="4,2"/>`;
        html += `<text x="148" y="150" text-anchor="middle" fill="#f87171" font-size="10" font-weight="bold">CRACK PROPAGATION LINE</text>`;
    } else {
        html += `<polygon points="180,20 120,125 240,125" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4,3"/>`;
        html += `<text x="180" y="80" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">Distributed Load Cone</text>`;
    }
    svg.innerHTML = html;
}

// Sim 3: 3D Net Folder
let sim3Shape = 'prism';
let sim3Fold = 0;
function sim3SetShape(sh) {
    sim3Shape = sh;
    const btnPrism = document.getElementById('sim3-shape-prism');
    const btnPyr = document.getElementById('sim3-shape-pyramid');
    const pName = document.getElementById('sim3-prop-name');
    const pBases = document.getElementById('sim3-prop-bases');
    const pSides = document.getElementById('sim3-prop-sides');
    const pFaces = document.getElementById('sim3-prop-faces');
    
    if (sh === 'prism') {
        if (btnPrism) btnPrism.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-indigo-600 text-white transition';
        if (btnPyr) btnPyr.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
        if (pName) pName.textContent = "Triangular Prism";
        if (pBases) pBases.textContent = "2 Triangles";
        if (pSides) pSides.textContent = "3 Rectangles";
        if (pFaces) pFaces.textContent = "5 Faces";
    } else {
        if (btnPyr) btnPyr.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-indigo-600 text-white transition';
        if (btnPrism) btnPrism.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
        if (pName) pName.textContent = "Square Pyramid";
        if (pBases) pBases.textContent = "1 Square";
        if (pSides) pSides.textContent = "4 Triangles";
        if (pFaces) pFaces.textContent = "5 Faces";
    }
    sim3Render();
}

function sim3OnFold(v) {
    sim3Fold = parseInt(v, 10);
    const disp = document.getElementById('sim3-fold-val');
    if (disp) disp.textContent = `${sim3Fold}%`;
    sim3Render();
}

function sim3Render() {
    const svg = document.getElementById('sim3-svg');
    if (!svg) return;
    const f = sim3Fold / 100; // 0 to 1
    let html = '';
    
    if (sim3Shape === 'prism') {
        // Base rectangle
        html += `<rect x="150" y="90" width="100" height="60" fill="#4338ca" stroke="#6366f1" stroke-width="2"/>`;
        html += `<text x="200" y="125" text-anchor="middle" fill="#e0e7ff" font-size="10">Base Rect</text>`;
        
        // Flap Left rectangle folding up
        const leftW = 100 * (1 - f * 0.75);
        html += `<rect x="${150 - leftW}" y="90" width="${leftW}" height="60" fill="#3730a3" stroke="#818cf8" stroke-width="1.5" stroke-dasharray="${f > 0.05 ? '0' : '4,3'}"/>`;
        
        // Flap Right rectangle folding up
        const rightW = 100 * (1 - f * 0.75);
        html += `<rect x="250" y="90" width="${rightW}" height="60" fill="#3730a3" stroke="#818cf8" stroke-width="1.5" stroke-dasharray="${f > 0.05 ? '0' : '4,3'}"/>`;
        
        // Top & Bottom Triangular Bases
        const triH = 65 * (1 - f * 0.65);
        const topY = 90 - triH;
        html += `<polygon points="150,90 250,90 200,${topY}" fill="#312e81" stroke="#a5b4fc" stroke-width="1.5"/>`;
        
        const botY = 150 + triH;
        html += `<polygon points="150,150 250,150 200,${botY}" fill="#312e81" stroke="#a5b4fc" stroke-width="1.5"/>`;
        
        if (f > 0.8) {
            html += `<text x="200" y="25" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Closed 3D Triangular Prism!</text>`;
        }
    } else {
        // Square Pyramid Net
        const sqSize = 80;
        const cx = 200, cy = 120;
        html += `<rect x="${cx - sqSize/2}" y="${cy - sqSize/2}" width="${sqSize}" height="${sqSize}" fill="#b45309" stroke="#f59e0b" stroke-width="2"/>`;
        html += `<text x="${cx}" y="${cy + 4}" text-anchor="middle" fill="#fef3c7" font-size="10">Square Base</text>`;
        
        const flapH = 60 * (1 - f * 0.85);
        // Top triangle flap
        html += `<polygon points="${cx - sqSize/2},${cy - sqSize/2} ${cx + sqSize/2},${cy - sqSize/2} ${cx},${cy - sqSize/2 - flapH}" fill="#d97706" stroke="#fbbf24" stroke-width="1.5"/>`;
        // Bottom triangle flap
        html += `<polygon points="${cx - sqSize/2},${cy + sqSize/2} ${cx + sqSize/2},${cy + sqSize/2} ${cx},${cy + sqSize/2 + flapH}" fill="#d97706" stroke="#fbbf24" stroke-width="1.5"/>`;
        // Left triangle flap
        html += `<polygon points="${cx - sqSize/2},${cy - sqSize/2} ${cx - sqSize/2},${cy + sqSize/2} ${cx - sqSize/2 - flapH},${cy}" fill="#92400e" stroke="#fbbf24" stroke-width="1.5"/>`;
        // Right triangle flap
        html += `<polygon points="${cx + sqSize/2},${cy - sqSize/2} ${cx + sqSize/2},${cy + sqSize/2} ${cx + sqSize/2 + flapH},${cy}" fill="#92400e" stroke="#fbbf24" stroke-width="1.5"/>`;
        
        if (f > 0.8) {
            html += `<circle cx="${cx}" cy="${cy}" r="5" fill="#f43f5e"/>`;
            html += `<text x="${cx}" y="${cy - 12}" text-anchor="middle" fill="#f43f5e" font-size="10" font-weight="bold">Apex Vertex</text>`;
            html += `<text x="200" y="25" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Closed 3D Square Pyramid!</text>`;
        }
    }
    svg.innerHTML = html;
}

// Sim 4: Euler Formula Calculator
let sim4ActiveShape = 'cube';
function sim4SelectShape(sh) {
    sim4ActiveShape = sh;
    ['cube', 'triprism', 'sqpyr', 'pentpyr'].forEach(id => {
        const btn = document.getElementById(`sim4-btn-${id}`);
        if (btn) {
            if (id === sh) {
                btn.className = 'px-2 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
            } else {
                btn.className = 'px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
            }
        }
    });
    sim4Render();
}

function sim4Render() {
    const svg = document.getElementById('sim4-svg');
    const fEl = document.getElementById('sim4-f');
    const vEl = document.getElementById('sim4-v');
    const eEl = document.getElementById('sim4-e');
    const resEl = document.getElementById('sim4-result');
    if (!svg) return;
    
    let F=6, V=8, E=12, formula="6 + 8 - 12 = 2";
    let svgContent = '';
    
    if (sim4ActiveShape === 'cube') {
        F = 6; V = 8; E = 12; formula = "6 + 8 - 12 = 2";
        // 3D wireframe cube
        svgContent = `
            <!-- Edges (Straws) -->
            <polygon points="120,60 220,60 220,160 120,160" fill="none" stroke="#38bdf8" stroke-width="3"/>
            <polygon points="170,30 270,30 270,130 170,130" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
            <line x1="120" y1="60" x2="170" y2="30" stroke="#38bdf8" stroke-width="3"/>
            <line x1="220" y1="60" x2="270" y2="30" stroke="#38bdf8" stroke-width="3"/>
            <line x1="220" y1="160" x2="270" y2="130" stroke="#38bdf8" stroke-width="3"/>
            <line x1="120" y1="160" x2="170" y2="130" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
            <!-- Vertices (Clay balls) -->
            ${[ [120,60], [220,60], [220,160], [120,160], [170,30], [270,30], [270,130], [170,130] ].map(p => `
                <circle cx="${p[0]}" cy="${p[1]}" r="6" fill="#f59e0b" stroke="#fff" stroke-width="1.5"/>
            `).join('')}
            <text x="195" y="195" text-anchor="middle" fill="#94a3b8" font-size="11">Cube: 12 Straws + 8 Clay Beads</text>
        `;
    } else if (sim4ActiveShape === 'triprism') {
        F = 5; V = 6; E = 9; formula = "5 + 6 - 9 = 2";
        svgContent = `
            <!-- Front triangle -->
            <polygon points="140,160 220,160 180,80" fill="none" stroke="#38bdf8" stroke-width="3"/>
            <!-- Back triangle -->
            <polygon points="190,130 270,130 230,50" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
            <!-- Connecting edges -->
            <line x1="140" y1="160" x2="190" y2="130" stroke="#38bdf8" stroke-width="3"/>
            <line x1="220" y1="160" x2="270" y2="130" stroke="#38bdf8" stroke-width="3"/>
            <line x1="180" y1="80" x2="230" y2="50" stroke="#38bdf8" stroke-width="3"/>
            <!-- Vertices -->
            ${[ [140,160], [220,160], [180,80], [190,130], [270,130], [230,50] ].map(p => `
                <circle cx="${p[0]}" cy="${p[1]}" r="6" fill="#f59e0b" stroke="#fff" stroke-width="1.5"/>
            `).join('')}
            <text x="205" y="195" text-anchor="middle" fill="#94a3b8" font-size="11">Triangular Prism: 9 Straws + 6 Clay Beads</text>
        `;
    } else if (sim4ActiveShape === 'sqpyr') {
        F = 5; V = 5; E = 8; formula = "5 + 5 - 8 = 2";
        svgContent = `
            <!-- Base square -->
            <polygon points="130,160 250,160 270,120 150,120" fill="none" stroke="#38bdf8" stroke-width="3"/>
            <!-- Apex edges -->
            <line x1="130" y1="160" x2="200" y2="40" stroke="#38bdf8" stroke-width="3"/>
            <line x1="250" y1="160" x2="200" y2="40" stroke="#38bdf8" stroke-width="3"/>
            <line x1="270" y1="120" x2="200" y2="40" stroke="#38bdf8" stroke-width="3"/>
            <line x1="150" y1="120" x2="200" y2="40" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
            <!-- Vertices -->
            ${[ [130,160], [250,160], [270,120], [150,120], [200,40] ].map(p => `
                <circle cx="${p[0]}" cy="${p[1]}" r="6" fill="#f59e0b" stroke="#fff" stroke-width="1.5"/>
            `).join('')}
            <text x="200" y="195" text-anchor="middle" fill="#94a3b8" font-size="11">Square Pyramid: 8 Straws + 5 Clay Beads</text>
        `;
    } else {
        F = 6; V = 6; E = 10; formula = "6 + 6 - 10 = 2";
        svgContent = `
            <!-- Pentagon Base -->
            <polygon points="150,160 210,170 250,140 220,110 160,115" fill="none" stroke="#38bdf8" stroke-width="3"/>
            <!-- Apex edges -->
            <line x1="150" y1="160" x2="200" y2="40" stroke="#38bdf8" stroke-width="3"/>
            <line x1="210" y1="170" x2="200" y2="40" stroke="#38bdf8" stroke-width="3"/>
            <line x1="250" y1="140" x2="200" y2="40" stroke="#38bdf8" stroke-width="3"/>
            <line x1="220" y1="110" x2="200" y2="40" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
            <line x1="160" y1="115" x2="200" y2="40" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,3"/>
            <!-- Vertices -->
            ${[ [150,160], [210,170], [250,140], [220,110], [160,115], [200,40] ].map(p => `
                <circle cx="${p[0]}" cy="${p[1]}" r="6" fill="#f59e0b" stroke="#fff" stroke-width="1.5"/>
            `).join('')}
            <text x="200" y="195" text-anchor="middle" fill="#94a3b8" font-size="11">Pentagonal Pyramid: 10 Straws + 6 Clay Beads</text>
        `;
    }
    
    svg.innerHTML = svgContent;
    if (fEl) fEl.textContent = F;
    if (vEl) vEl.textContent = V;
    if (eEl) eEl.textContent = E;
    if (resEl) resEl.textContent = formula;
}

// Sim 5: Cube Face Views
let sim5Tab = 1;
function sim5SetTab(t) {
    sim5Tab = t;
    const tab1 = document.getElementById('sim5-tab1');
    const tab2 = document.getElementById('sim5-tab2');
    const btn1 = document.getElementById('sim5-tab1-btn');
    const btn2 = document.getElementById('sim5-tab2-btn');
    if (t === 1) {
        if (tab1) tab1.classList.remove('hidden');
        if (tab2) tab2.classList.add('hidden');
        if (btn1) btn1.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
        if (btn2) btn2.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
    } else {
        if (tab1) tab1.classList.add('hidden');
        if (tab2) tab2.classList.remove('hidden');
        if (btn2) btn2.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
        if (btn1) btn1.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
    }
}

function sim5SelectDieFace(f) {
    const opp = 7 - f;
    const res = document.getElementById('sim5-die-result');
    if (res) {
        res.innerHTML = `
            <span class="text-amber-400 font-bold text-sm">Face ${f} Selected</span>
            <div class="text-emerald-400 font-semibold text-sm">Opposite Face is ${opp} (${f} + ${opp} = 7)</div>
            <p class="text-slate-400 text-[11px]">Opposite faces are parallel across the cube and never share an edge!</p>
        `;
    }
}

function sim5SolveColorPuzzle() {
    const verdict = document.getElementById('sim5-color-verdict');
    if (verdict) {
        verdict.innerHTML = `
            <div class="bg-emerald-950/80 border border-emerald-500/50 p-2.5 rounded-lg text-emerald-300">
                <span class="font-bold block">✓ Systematic Deduction Result:</span>
                Green touches Red, Blue, Yellow, and Purple across the 3 views.
                None of those 4 colors can be opposite Green.
                Therefore, the opposite face of Green is the <strong>White</strong> face!
            </div>
        `;
    }
}

// Sim 6: Venn Diagram Sorter
let sim6Placed = {};
function sim6Reset() {
    sim6Placed = {};
    const g = document.getElementById('sim6-placed-shapes');
    if (g) g.innerHTML = '';
    const fb = document.getElementById('sim6-feedback');
    if (fb) fb.textContent = "Click a shape above to classify its position in the Venn Diagram!";
}

function sim6PlaceShape(sh) {
    const coords = {
        'cube': { x: 120, y: 110, label: 'Cube (Rect only)' },
        'sqpyr': { x: 320, y: 110, label: 'Sq Pyramid (Tri)' },
        'triprism': { x: 220, y: 155, label: 'Tri Prism (BOTH)' },
        'cylinder': { x: 60, y: 190, label: 'Cylinder (Outside)' },
        'cone': { x: 380, y: 190, label: 'Cone (Outside)' },
        'sphere': { x: 220, y: 200, label: 'Sphere (Outside)' }
    };
    
    const info = coords[sh];
    if (!info) return;
    sim6Placed[sh] = true;
    
    const g = document.getElementById('sim6-placed-shapes');
    const fb = document.getElementById('sim6-feedback');
    if (g) {
        g.innerHTML += `
            <circle cx="${info.x}" cy="${info.y}" r="14" fill="#10b981" stroke="#fff" stroke-width="1.5"/>
            <text x="${info.x}" y="${info.y - 18}" text-anchor="middle" fill="#34d399" font-size="9" font-weight="bold">${info.label}</text>
        `;
    }
    if (fb) {
        if (sh === 'triprism') {
            fb.innerHTML = "<span class='text-emerald-400 font-bold'>✓ Correct!</span> Triangular Prism has 3 rectangular faces AND 2 triangular bases, placing it directly in the Venn intersection!";
        } else if (sh === 'cube') {
            fb.innerHTML = "<span class='text-sky-400 font-bold'>✓ Correct!</span> A Cube has 6 flat rectangular faces (squares are special rectangles).";
        } else if (sh === 'sqpyr') {
            fb.innerHTML = "<span class='text-amber-400 font-bold'>✓ Correct!</span> Square Pyramid has 4 triangular side faces sloping to the apex.";
        } else {
            fb.innerHTML = `<span class='text-purple-400 font-bold'>✓ Correct!</span> ${info.label} has curved surfaces, so it sits outside the flat polygon regions.`;
        }
    }
}

// Sim 7: Cube Tower Counting
let sim7Mode = 'all';
function sim7SetView(m) {
    sim7Mode = m;
    const btnAll = document.getElementById('sim7-view-all');
    const btnLay = document.getElementById('sim7-view-layers');
    if (m === 'all') {
        if (btnAll) btnAll.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
        if (btnLay) btnLay.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
    } else {
        if (btnLay) btnLay.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
        if (btnAll) btnAll.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
    }
    sim7Render();
}

function sim7Render() {
    const svg = document.getElementById('sim7-svg');
    if (!svg) return;
    
    // Isometric draw helper
    function drawIsoCube(cx, cy, size, colorTop, colorFront, colorSide) {
        const dx = size * 0.866;
        const dy = size * 0.5;
        return `
            <!-- Top Face -->
            <polygon points="${cx},${cy - size} ${cx + dx},${cy - dy} ${cx},${cy} ${cx - dx},${cy - dy}" fill="${colorTop}" stroke="#0f172a" stroke-width="1"/>
            <!-- Front Left Face -->
            <polygon points="${cx - dx},${cy - dy} ${cx},${cy} ${cx},${cy + size} ${cx - dx},${cy + dy}" fill="${colorFront}" stroke="#0f172a" stroke-width="1"/>
            <!-- Front Right Face -->
            <polygon points="${cx},${cy} ${cx + dx},${cy - dy} ${cx + dx},${cy + dy} ${cx},${cy + size}" fill="${colorSide}" stroke="#0f172a" stroke-width="1"/>
        `;
    }
    
    let html = '';
    if (sim7Mode === 'all') {
        // Draw 3-tier stepped tower in full isometric
        // Tier 1 Base: 3x3 = 9 cubes
        for (let r = 0; r < 3; r++) {
            for (let c = 0; c < 3; c++) {
                const x = 190 + (c - r) * 26;
                const y = 140 + (c + r) * 15;
                html += drawIsoCube(x, y, 16, '#f87171', '#dc2626', '#b91c1c');
            }
        }
        // Tier 2 Mid: 2x2 = 4 cubes
        for (let r = 0; r < 2; r++) {
            for (let c = 0; c < 2; c++) {
                const x = 190 + (c - r) * 26;
                const y = 140 + (c + r) * 15 - 20;
                html += drawIsoCube(x, y, 16, '#fbbf24', '#f59e0b', '#d97706');
            }
        }
        // Tier 3 Top: 1 cube
        html += drawIsoCube(190, 140 - 40, 16, '#38bdf8', '#0284c7', '#0369a1');
    } else {
        // Separated layer slices
        // Tier 3 (Top)
        html += `<text x="70" y="30" fill="#38bdf8" font-size="11" font-weight="bold">Layer 3: 1 cube</text>`;
        html += drawIsoCube(70, 80, 16, '#38bdf8', '#0284c7', '#0369a1');
        
        // Tier 2 (Mid)
        html += `<text x="190" y="30" fill="#fbbf24" font-size="11" font-weight="bold">Layer 2: 4 cubes (2×2)</text>`;
        for (let r = 0; r < 2; r++) {
            for (let c = 0; c < 2; c++) {
                const x = 190 + (c - r) * 20;
                const y = 70 + (c + r) * 12;
                html += drawIsoCube(x, y, 14, '#fbbf24', '#f59e0b', '#d97706');
            }
        }
        
        // Tier 1 (Base)
        html += `<text x="310" y="30" fill="#f87171" font-size="11" font-weight="bold">Layer 1: 9 cubes (3×3)</text>`;
        for (let r = 0; r < 3; r++) {
            for (let c = 0; c < 3; c++) {
                const x = 310 + (c - r) * 16;
                const y = 70 + (c + r) * 10;
                html += drawIsoCube(x, y, 12, '#f87171', '#dc2626', '#b91c1c');
            }
        }
    }
    svg.innerHTML = html;
}

// Sim 8: Isometric Net Matching
let sim8Net = 1;
function sim8SelectNet(n) {
    sim8Net = n;
    [1, 2, 3, 4].forEach(i => {
        const btn = document.getElementById(`sim8-btn-net${i}`);
        if (btn) {
            if (i === n) {
                btn.className = 'p-2 rounded-xl bg-amber-500 text-slate-950 font-bold text-xs transition border border-amber-400 flex flex-col items-center';
            } else {
                btn.className = 'p-2 rounded-xl bg-slate-800 text-slate-300 hover:text-white font-medium text-xs transition border border-slate-700 flex flex-col items-center';
            }
        }
    });
    const status = document.getElementById('sim8-status');
    const msgs = [
        "",
        "Net A (Latin Cross): Valid! 4 in a line + 2 wings fold into a perfect closed cube.",
        "Net B (Stair Step): Valid! 2-2-2 stair net folds into a complete cube.",
        "Net C (Overlapping Flaps): INVALID! Two flaps fold onto the same face, leaving one side open.",
        "Net D (Long Strip): INVALID! 5 squares in a row overlap when wrapped, leaving ends uncovered."
    ];
    if (status) status.textContent = msgs[n];
    sim8Render();
}

function sim8Render() {
    const svg = document.getElementById('sim8-svg');
    if (!svg) return;
    const s = 30; // square size
    let html = '';
    
    if (sim8Net === 1) {
        // Latin cross: 4 in col 2, flaps at row 1 left & right
        const coords = [ [2,0], [2,1], [2,2], [2,3], [1,1], [3,1] ];
        coords.forEach(p => {
            html += `<rect x="${100 + p[0]*s}" y="${30 + p[1]*s}" width="${s}" height="${s}" fill="#3b82f6" stroke="#fff" stroke-width="1.5"/>`;
        });
        html += `<text x="190" y="175" text-anchor="middle" fill="#60a5fa" font-size="11">Latin Cross: Valid 6-Square Net</text>`;
    } else if (sim8Net === 2) {
        // Stair step: [1,0],[2,0], [2,1],[3,1], [3,2],[4,2]
        const coords = [ [1,0],[2,0], [2,1],[3,1], [3,2],[4,2] ];
        coords.forEach(p => {
            html += `<rect x="${80 + p[0]*s}" y="${35 + p[1]*s}" width="${s}" height="${s}" fill="#10b981" stroke="#fff" stroke-width="1.5"/>`;
        });
        html += `<text x="190" y="175" text-anchor="middle" fill="#34d399" font-size="11">Stair Step Net: Valid 6-Square Net</text>`;
    } else if (sim8Net === 3) {
        // Overlapping net: two flaps on the same side
        const coords = [ [2,0], [2,1], [2,2], [2,3], [3,1], [3,2] ];
        coords.forEach(p => {
            html += `<rect x="${100 + p[0]*s}" y="${30 + p[1]*s}" width="${s}" height="${s}" fill="#ef4444" stroke="#fff" stroke-width="1.5"/>`;
        });
        html += `<text x="190" y="175" text-anchor="middle" fill="#f87171" font-size="11">Invalid: 2 Flaps Fold to Same Face!</text>`;
    } else {
        // 5 in a row + 1 flap
        const coords = [ [0,1], [1,1], [2,1], [3,1], [4,1], [2,0] ];
        coords.forEach(p => {
            html += `<rect x="${60 + p[0]*s}" y="${45 + p[1]*s}" width="${s}" height="${s}" fill="#f59e0b" stroke="#fff" stroke-width="1.5"/>`;
        });
        html += `<text x="190" y="175" text-anchor="middle" fill="#fbbf24" font-size="11">Invalid: 5 in a row creates double overlap!</text>`;
    }
    svg.innerHTML = html;
}

function sim8TestFold() {
    playChime(sim8Net === 1 || sim8Net === 2);
    const status = document.getElementById('sim8-status');
    if (status) {
        if (sim8Net === 1 || sim8Net === 2) {
            status.innerHTML = "<span class='text-emerald-400 font-bold'>✓ Success!</span> The net folds smoothly into a closed 3D cube with zero gaps!";
        } else {
            status.innerHTML = "<span class='text-rose-400 font-bold'>✗ Failed!</span> Flaps collided on the same face. A cube face remained uncovered!";
        }
    }
}

// Sim 9: Angles at Intersections
let sim9Angle = 60;
let sim9Mode = 'straw';
let sim9LongStraws = false;

function sim9SetMode(m) {
    sim9Mode = m;
    ['straw', 'scissors', 'roof'].forEach(id => {
        const btn = document.getElementById(`sim9-btn-${id}`);
        if (btn) {
            if (id === m) {
                btn.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
            } else {
                btn.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
            }
        }
    });
    sim9Render();
}

function sim9OnAngleChange(v) {
    sim9Angle = parseInt(v, 10);
    const sliderDisp = document.getElementById('sim9-slider-val');
    const angleDisp = document.getElementById('sim9-angle-disp');
    const typeDisp = document.getElementById('sim9-type-disp');
    
    if (sliderDisp) sliderDisp.textContent = `${sim9Angle}°`;
    if (angleDisp) angleDisp.textContent = `${sim9Angle}°`;
    
    if (typeDisp) {
        if (sim9Angle < 90) {
            typeDisp.textContent = "Acute (< 90°)";
            typeDisp.className = "text-sky-400 font-semibold";
        } else if (sim9Angle === 90) {
            typeDisp.textContent = "Right Angle (90°)";
            typeDisp.className = "text-emerald-400 font-semibold";
        } else {
            typeDisp.textContent = "Obtuse (> 90°)";
            typeDisp.className = "text-rose-400 font-semibold";
        }
    }
    sim9Render();
}

function sim9ToggleStrawLength() {
    sim9LongStraws = !sim9LongStraws;
    sim9Render();
}

function sim9Render() {
    const svg = document.getElementById('sim9-svg');
    if (!svg) return;
    
    const cx = 190, cy = 160;
    const len = sim9LongStraws ? 130 : 90;
    const rad = (sim9Angle * Math.PI) / 180;
    
    // Ray 1 along baseline (to the right)
    const x1 = cx + len, y1 = cy;
    // Ray 2 rotated upward by sim9Angle
    const x2 = cx + len * Math.cos(rad);
    const y2 = cy - len * Math.sin(rad);
    
    // Arc coordinates
    const arcR = 40;
    const arcX = cx + arcR * Math.cos(rad);
    const arcY = cy - arcR * Math.sin(rad);
    const largeArc = sim9Angle > 180 ? 1 : 0;
    
    let html = `
        <!-- Ray 1 (Baseline) -->
        <line x1="${cx}" y1="${cy}" x2="${x1}" y2="${y1}" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
        <!-- Ray 2 (Rotated) -->
        <line x1="${cx}" y1="${cy}" x2="${x2}" y2="${y2}" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
        
        <!-- Vertex Pin -->
        <circle cx="${cx}" cy="${cy}" r="7" fill="#ef4444" stroke="#fff" stroke-width="2"/>
        <text x="${cx}" y="${cy + 22}" text-anchor="middle" fill="#94a3b8" font-size="11" font-weight="bold">Vertex</text>
        
        <!-- Angle Arc -->
        <path d="M ${cx + arcR},${cy} A ${arcR} ${arcR} 0 ${largeArc} 0 ${arcX} ${arcY}" fill="none" stroke="#10b981" stroke-width="2.5"/>
        <text x="${cx + 50 * Math.cos(rad/2)}" y="${cy - 50 * Math.sin(rad/2)}" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">${sim9Angle}°</text>
    `;
    
    if (sim9Mode === 'scissors') {
        html += `<text x="190" y="30" text-anchor="middle" fill="#e2e8f0" font-size="11">✂️ Scissor Blades Open by ${sim9Angle}°</text>`;
    } else if (sim9Mode === 'roof') {
        html += `<text x="190" y="30" text-anchor="middle" fill="#e2e8f0" font-size="11">🏠 Roof Rafter Pitch Angle: ${sim9Angle}°</text>`;
    }
    
    svg.innerHTML = html;
}

// Sim 10: Classifying Angle Types
let sim10Fold = 0;
let sim10Target = 'acute';

function sim10SetFold(f) {
    sim10Fold = f;
    [0, 1, 2].forEach(i => {
        const btn = document.getElementById(`sim10-fold${i}`);
        if (btn) {
            if (i === f) {
                btn.className = 'px-2 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
            } else {
                btn.className = 'px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
            }
        }
    });
    const status = document.getElementById('sim10-status-pill');
    if (status) {
        if (f === 0) status.textContent = "Step 1: Flat unfolded sheet of paper (360° circle / flat sheet).";
        else if (f === 1) status.textContent = "Step 2: Folded neatly in half! The straight edge forms a 180° straight angle.";
        else status.textContent = "Step 3: Folded in half again! You now hold a 90° right-angle tester shaped like an L!";
    }
    sim10Render();
}

function sim10TestTarget(t) {
    sim10Target = t;
    sim10Render();
}

function sim10Render() {
    const svg = document.getElementById('sim10-svg');
    if (!svg) return;
    let html = '';
    
    // Target display on right
    let targetAngle = 45;
    let targetLabel = "Acute Angle (45°)";
    let targetColor = "#38bdf8";
    
    if (sim10Target === 'acute') {
        targetAngle = 45; targetLabel = "Acute Angle (< 90°)"; targetColor = "#38bdf8";
    } else if (sim10Target === 'right') {
        targetAngle = 90; targetLabel = "Right Angle (Exactly 90°)"; targetColor = "#10b981";
    } else if (sim10Target === 'obtuse') {
        targetAngle = 130; targetLabel = "Obtuse Angle (> 90°)"; targetColor = "#f43f5e";
    } else if (sim10Target === 'letterV') {
        targetAngle = 40; targetLabel = "Letter 'V' Bottom Vertex: Acute!"; targetColor = "#38bdf8";
    } else if (sim10Target === 'letterL') {
        targetAngle = 90; targetLabel = "Letter 'L' Corner: Right Angle!"; targetColor = "#10b981";
    } else if (sim10Target === 'letterA') {
        targetAngle = 35; targetLabel = "Letter 'A' Top Peak: Acute!"; targetColor = "#38bdf8";
    }
    
    // Draw Paper on Left
    if (sim10Fold === 0) {
        html += `<rect x="30" y="40" width="110" height="110" rx="4" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>`;
        html += `<text x="85" y="100" text-anchor="middle" fill="#475569" font-size="10">Flat Paper</text>`;
    } else if (sim10Fold === 1) {
        html += `<rect x="30" y="40" width="55" height="110" rx="4" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5"/>`;
        html += `<text x="57" y="100" text-anchor="middle" fill="#475569" font-size="10">Half Fold (180°)</text>`;
    } else {
        html += `<polygon points="30,40 30,120 110,120 110,40" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>`;
        // Draw 90° corner square
        html += `<rect x="30" y="95" width="25" height="25" fill="#fde047" stroke="#eab308" stroke-width="2"/>`;
        html += `<text x="70" y="80" text-anchor="middle" fill="#854d0e" font-size="10" font-weight="bold">90° L-Corner</text>`;
    }
    
    // Draw Test Angle on Right
    const tx = 270, ty = 140, rLen = 70;
    const rad = (targetAngle * Math.PI) / 180;
    html += `
        <line x1="${tx}" y1="${ty}" x2="${tx + rLen}" y2="${ty}" stroke="${targetColor}" stroke-width="4"/>
        <line x1="${tx}" y1="${ty}" x2="${tx + rLen * Math.cos(rad)}" y2="${ty - rLen * Math.sin(rad)}" stroke="${targetColor}" stroke-width="4"/>
        <circle cx="${tx}" cy="${ty}" r="6" fill="#f59e0b"/>
        <text x="270" y="30" text-anchor="middle" fill="${targetColor}" font-size="12" font-weight="bold">${targetLabel}</text>
    `;
    
    // If fold === 2, show L-tester comparison overlay
    if (sim10Fold === 2) {
        html += `
            <polygon points="${tx},${ty} ${tx + 50},${ty} ${tx},${ty - 50}" fill="#fde047" fill-opacity="0.3" stroke="#eab308" stroke-width="1.5" stroke-dasharray="3,2"/>
            <text x="${tx + 30}" y="${ty - 25}" fill="#fde047" font-size="9">L-Tester Overlay</text>
        `;
    }
    
    svg.innerHTML = html;
}

// Sim 11: Triangle Structural Rigidity
let sim11Shape = 'quad';
let sim11Pushed = false;
let sim11Braced = false;

function sim11SetShape(sh) {
    sim11Shape = sh;
    sim11Pushed = false;
    sim11Braced = false;
    const btnQ = document.getElementById('sim11-btn-quad');
    const btnT = document.getElementById('sim11-btn-tri');
    if (sh === 'quad') {
        if (btnQ) btnQ.className = 'px-3 py-2 rounded-lg bg-amber-500 text-slate-950 font-bold text-xs transition shadow';
        if (btnT) btnT.className = 'px-3 py-2 rounded-lg bg-slate-800 text-slate-300 hover:text-white font-medium text-xs transition border border-slate-700';
    } else {
        if (btnT) btnT.className = 'px-3 py-2 rounded-lg bg-amber-500 text-slate-950 font-bold text-xs transition shadow';
        if (btnQ) btnQ.className = 'px-3 py-2 rounded-lg bg-slate-800 text-slate-300 hover:text-white font-medium text-xs transition border border-slate-700';
    }
    sim11Render();
}

function sim11PushForce() {
    sim11Pushed = !sim11Pushed;
    playChime(!sim11Pushed || (sim11Shape === 'tri' || sim11Braced));
    const alert = document.getElementById('sim11-alert');
    if (alert) {
        if (sim11Shape === 'quad' && !sim11Braced) {
            alert.innerHTML = "<span class='text-rose-400 font-bold'>⚠️ Collapse!</span> 4-straw quadrilateral wobbles and distorts into a slanted parallelogram!";
        } else if (sim11Shape === 'tri') {
            alert.innerHTML = "<span class='text-emerald-400 font-bold'>🛡️ Rock-Solid!</span> Triangle cannot deform! Three side lengths fix the three angles permanently.";
        } else {
            alert.innerHTML = "<span class='text-emerald-400 font-bold'>🛡️ Braced!</span> Diagonal brace divided the square into two triangles, making it completely rigid!";
        }
    }
    sim11Render();
}

function sim11ToggleBrace() {
    if (sim11Shape === 'quad') {
        sim11Braced = !sim11Braced;
        sim11Render();
    }
}

function sim11Render() {
    const svg = document.getElementById('sim11-svg');
    if (!svg) return;
    let html = '';
    
    if (sim11Shape === 'quad') {
        const offset = (sim11Pushed && !sim11Braced) ? 45 : 0;
        const p1 = [120 + offset, 60];
        const p2 = [240 + offset, 60];
        const p3 = [240, 170];
        const p4 = [120, 170];
        
        html += `<polygon points="${p1[0]},${p1[1]} ${p2[0]},${p2[1]} ${p3[0]},${p3[1]} ${p4[0]},${p4[1]}" fill="#1e293b" stroke="#f59e0b" stroke-width="4"/>`;
        
        if (sim11Braced) {
            html += `<line x1="${p1[0]}" y1="${p1[1]}" x2="${p3[0]}" y2="${p3[1]}" stroke="#10b981" stroke-width="4"/>`;
            html += `<text x="200" y="110" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">Diagonal Brace</text>`;
        }
        
        // Pins
        [p1, p2, p3, p4].forEach(p => {
            html += `<circle cx="${p[0]}" cy="${p[1]}" r="6" fill="#ef4444" stroke="#fff" stroke-width="1.5"/>`;
        });
        
        if (sim11Pushed && !sim11Braced) {
            html += `<text x="190" y="30" text-anchor="middle" fill="#f87171" font-size="11" font-weight="bold">Deformed into Wobbly Parallelogram!</text>`;
        }
    } else {
        // Triangle
        const p1 = [190, 50];
        const p2 = [260, 170];
        const p3 = [120, 170];
        
        html += `<polygon points="${p1[0]},${p1[1]} ${p2[0]},${p2[1]} ${p3[0]},${p3[1]}" fill="#1e293b" stroke="#10b981" stroke-width="4"/>`;
        [p1, p2, p3].forEach(p => {
            html += `<circle cx="${p[0]}" cy="${p[1]}" r="6" fill="#f59e0b" stroke="#fff" stroke-width="1.5"/>`;
        });
        html += `<text x="190" y="30" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">Rigid Triangle: Resists All Deformation!</text>`;
    }
    
    svg.innerHTML = html;
}

// Sim 12: Circle Radius Diameter
let sim12Radius = 5;
let sim12ShowRadius = true;
let sim12ShowDiameter = true;
let sim12ShowCrease = false;

function sim12OnRadiusChange(v) {
    sim12Radius = parseInt(v, 10);
    const slDisp = document.getElementById('sim12-slider-val');
    const rDisp = document.getElementById('sim12-r-disp');
    const dDisp = document.getElementById('sim12-d-disp');
    if (slDisp) slDisp.textContent = `${sim12Radius} cm`;
    if (rDisp) rDisp.textContent = `${sim12Radius} cm`;
    if (dDisp) dDisp.textContent = `${sim12Radius * 2} cm`;
    sim12Render();
}

function sim12ToggleLine(type) {
    if (type === 'radius') sim12ShowRadius = !sim12ShowRadius;
    if (type === 'diameter') sim12ShowDiameter = !sim12ShowDiameter;
    if (type === 'crease') sim12ShowCrease = !sim12ShowCrease;
    sim12Render();
}

function sim12Render() {
    const svg = document.getElementById('sim12-svg');
    if (!svg) return;
    const cx = 190, cy = 110;
    const pxR = sim12Radius * 12; // scale for screen
    
    let html = `
        <!-- Circular Disc -->
        <circle cx="${cx}" cy="${cy}" r="${pxR}" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5"/>
        <circle cx="${cx}" cy="${cy}" r="4" fill="#ef4444"/>
        <text x="${cx}" y="${cy - 8}" text-anchor="middle" fill="#f87171" font-size="10" font-weight="bold">Center O</text>
    `;
    
    if (sim12ShowDiameter) {
        html += `
            <line x1="${cx - pxR}" y1="${cy}" x2="${cx + pxR}" y2="${cy}" stroke="#f59e0b" stroke-width="3"/>
            <text x="${cx}" y="${cy + 16}" text-anchor="middle" fill="#fbbf24" font-size="10" font-weight="bold">Diameter = ${sim12Radius * 2} cm</text>
        `;
    }
    
    if (sim12ShowRadius) {
        html += `
            <line x1="${cx}" y1="${cy}" x2="${cx + pxR * 0.707}" y2="${cy - pxR * 0.707}" stroke="#10b981" stroke-width="3"/>
            <text x="${cx + 25}" y="${cy - 20}" fill="#34d399" font-size="10" font-weight="bold">Radius = ${sim12Radius} cm</text>
        `;
    }
    
    if (sim12ShowCrease) {
        html += `
            <line x1="${cx}" y1="${cy - pxR}" x2="${cx}" y2="${cy + pxR}" stroke="#e2e8f0" stroke-width="2" stroke-dasharray="4,3"/>
            <text x="${cx + 6}" y="${cy - pxR + 15}" fill="#cbd5e1" font-size="9">Fold Crease</text>
        `;
    }
    
    svg.innerHTML = html;
}

// Sim 13: Compass Circle Art
let sim13Radius = 50;
let sim13Rings = [50];

function sim13OnRadiusChange(v) {
    sim13Radius = parseInt(v, 10);
    const disp = document.getElementById('sim13-val-disp');
    const readout = document.getElementById('sim13-radius-readout');
    if (disp) disp.textContent = `${sim13Radius} px`;
    if (readout) readout.textContent = `${sim13Radius} px`;
    sim13Render();
}

function sim13DrawCurrentCircle() {
    if (!sim13Rings.includes(sim13Radius)) {
        sim13Rings.push(sim13Radius);
        playChime(true);
        sim13Render();
    }
}

function sim13AddStepRing() {
    sim13Radius = Math.min(sim13Radius + 15, 95);
    sim13Rings.push(sim13Radius);
    playChime(true);
    sim13Render();
}

function sim13Preset(p) {
    if (p === 'concentric') {
        sim13Rings = [25, 45, 65, 85];
    } else {
        sim13Rings = [50];
    }
    playChime(true);
    sim13Render();
}

function sim13Clear() {
    sim13Rings = [50];
    sim13Render();
}

function sim13Render() {
    const svg = document.getElementById('sim13-svg');
    if (!svg) return;
    const cx = 190, cy = 110;
    
    let html = `
        <!-- Central Needle Point -->
        <circle cx="${cx}" cy="${cy}" r="4" fill="#ef4444"/>
        <text x="${cx}" y="${cy - 8}" text-anchor="middle" fill="#f87171" font-size="9" font-weight="bold">Pivot (0,0)</text>
    `;
    
    // Draw rings
    sim13Rings.forEach((r, idx) => {
        const colors = ['#38bdf8', '#10b981', '#f59e0b', '#ec4899', '#a855f7'];
        const col = colors[idx % colors.length];
        html += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${col}" stroke-width="2"/>`;
    });
    
    // Compass arm illustration
    html += `
        <!-- Compass Arm -->
        <line x1="${cx}" y1="${cy}" x2="${cx + sim13Radius}" y2="${cy}" stroke="#fbbf24" stroke-width="2" stroke-dasharray="3,2"/>
        <circle cx="${cx + sim13Radius}" cy="${cy}" r="3" fill="#f59e0b"/>
        <text x="${cx + sim13Radius/2}" y="${cy - 4}" text-anchor="middle" fill="#fbbf24" font-size="9">${sim13Radius}px</text>
    `;
    
    svg.innerHTML = html;
}

// Sim 14: Geometric Dissection
let sim14Tab = 1;
let sim14State = 'original';

function sim14SetTab(t) {
    sim14Tab = t;
    const tab1 = document.getElementById('sim14-tab1');
    const tab2 = document.getElementById('sim14-tab2');
    const btn1 = document.getElementById('sim14-tab1-btn');
    const btn2 = document.getElementById('sim14-tab2-btn');
    if (t === 1) {
        if (tab1) tab1.classList.remove('hidden');
        if (tab2) tab2.classList.add('hidden');
        if (btn1) btn1.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
        if (btn2) btn2.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
    } else {
        if (tab1) tab1.classList.add('hidden');
        if (tab2) tab2.classList.remove('hidden');
        if (btn2) btn2.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
        if (btn1) btn1.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
    }
}

function sim14SetState(st) {
    sim14State = st;
    ['original', 'dissect', 'rearrange'].forEach(id => {
        const btn = document.getElementById(`sim14-btn-${id}`);
        if (btn) {
            if (id === st) {
                btn.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
            } else {
                btn.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
            }
        }
    });
    sim14Render();
}

function sim14Render() {
    const svg = document.getElementById('sim14-svg');
    if (!svg) return;
    let html = '';
    
    if (sim14State === 'original') {
        html = `
            <polygon points="190,30 280,150 100,150" fill="#4338ca" stroke="#818cf8" stroke-width="2"/>
            <text x="190" y="105" text-anchor="middle" fill="#e0e7ff" font-size="12" font-weight="bold">Original Triangle</text>
        `;
    } else if (sim14State === 'dissect') {
        html = `
            <!-- Square in center -->
            <rect x="150" y="90" width="80" height="60" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
            <text x="190" y="125" text-anchor="middle" fill="#78350f" font-size="11" font-weight="bold">1 Square</text>
            <!-- Left Wing Triangle -->
            <polygon points="100,150 150,150 150,90" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
            <!-- Right Wing Triangle -->
            <polygon points="230,90 230,150 280,150" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
            <text x="190" y="45" text-anchor="middle" fill="#38bdf8" font-size="10">Dissected: 1 Square + 2 Smaller Triangles</text>
        `;
    } else {
        html = `
            <!-- Reassembled into a rectangle -->
            <rect x="110" y="60" width="160" height="60" fill="#10b981" stroke="#34d399" stroke-width="2"/>
            <text x="190" y="95" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold">Reassembled Rectangle</text>
            <text x="190" y="145" text-anchor="middle" fill="#34d399" font-size="10">Same total area conserved!</text>
        `;
    }
    svg.innerHTML = html;
}

// Sim 15: Matchstick Logic & Spiderweb
let sim15Tab = 1;
let sim15Removed = false;

function sim15SetTab(t) {
    sim15Tab = t;
    const tab1 = document.getElementById('sim15-tab1');
    const tab2 = document.getElementById('sim15-tab2');
    const btn1 = document.getElementById('sim15-tab1-btn');
    const btn2 = document.getElementById('sim15-tab2-btn');
    if (t === 1) {
        if (tab1) tab1.classList.remove('hidden');
        if (tab2) tab2.classList.add('hidden');
        if (btn1) btn1.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
        if (btn2) btn2.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
        sim15Render();
    } else {
        if (tab1) tab1.classList.add('hidden');
        if (tab2) tab2.classList.remove('hidden');
        if (btn2) btn2.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
        if (btn1) btn1.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
        sim15RenderWeb();
    }
}

function sim15RemoveMatches() {
    sim15Removed = true;
    playChime(true);
    const fb = document.getElementById('sim15-match-feedback');
    if (fb) fb.innerHTML = "<span class='text-emerald-400 font-bold'>✓ Puzzle Solved!</span> 2 matchsticks removed, leaving exactly 1 standalone triangle!";
    sim15Render();
}

function sim15ResetMatches() {
    sim15Removed = false;
    const fb = document.getElementById('sim15-match-feedback');
    if (fb) fb.textContent = "6 matchsticks currently form 3 contiguous triangles.";
    sim15Render();
}

function sim15Render() {
    const svg = document.getElementById('sim15-svg');
    if (!svg) return;
    
    // Draw matchsticks
    let html = `
        <!-- Base match 1 -->
        <line x1="120" y1="140" x2="180" y2="140" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
        <!-- Slant match 1 -->
        <line x1="120" y1="140" x2="150" y2="80" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
        <!-- Slant match 2 -->
        <line x1="180" y1="140" x2="150" y2="80" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
    `;
    
    if (!sim15Removed) {
        html += `
            <!-- Triangle 2 & 3 extra matches -->
            <line x1="180" y1="140" x2="240" y2="140" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
            <line x1="240" y1="140" x2="210" y2="80" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>
            <line x1="180" y1="140" x2="210" y2="80" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>
        `;
    }
    svg.innerHTML = html;
}

function sim15RenderWeb() {
    const svg = document.getElementById('sim15-web-svg');
    if (!svg) return;
    const cx = 190, cy = 90;
    let html = '';
    
    // Radial spokes
    for (let a = 0; a < 360; a += 45) {
        const rad = (a * Math.PI) / 180;
        html += `<line x1="${cx}" y1="${cy}" x2="${cx + 80 * Math.cos(rad)}" y2="${cy + 80 * Math.sin(rad)}" stroke="#475569" stroke-width="1.5"/>`;
    }
    
    // Spiral polygon rings
    [25, 45, 65, 80].forEach(r => {
        let pts = [];
        for (let a = 0; a <= 360; a += 45) {
            const rad = (a * Math.PI) / 180;
            pts.push(`${cx + r * Math.cos(rad)},${cy + r * Math.sin(rad)}`);
        }
        html += `<polygon points="${pts.join(' ')}" fill="none" stroke="#94a3b8" stroke-width="1"/>`;
    });
    
    svg.innerHTML = html;
}

function sim15HighlightSpokes() {
    playChime(true);
    const fb = document.getElementById('sim15-web-feedback');
    if (fb) fb.innerHTML = "<span class='text-sky-400 font-bold'>8 Radial Threads</span> radiate straight outward like wheel spokes!";
}

function sim15HighlightPolygons() {
    playChime(true);
    const fb = document.getElementById('sim15-web-feedback');
    if (fb) fb.innerHTML = "<span class='text-emerald-400 font-bold'>4 Concentric Octagonal Loops</span> create dozens of geometric polygons!";
}

// Sim 16: Polygon Angle Relations
let sim16N = 3;
function sim16Select(n) {
    sim16N = n;
    [3, 4, 5, 6, 8].forEach(id => {
        const btn = document.getElementById(`sim16-btn-${id}`);
        if (btn) {
            if (id === n) {
                btn.className = 'px-2 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
            } else {
                btn.className = 'px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
            }
        }
    });
    const sidesEl = document.getElementById('sim16-sides');
    const anglesEl = document.getElementById('sim16-angles');
    const groupEl = document.getElementById('sim16-group');
    if (sidesEl) sidesEl.textContent = `${n} sides`;
    if (anglesEl) anglesEl.textContent = `${n} angles`;
    if (groupEl) {
        groupEl.textContent = n < 5 ? "< 5 Angles" : "≥ 5 Angles";
        groupEl.className = n < 5 ? "text-rose-400 font-bold text-sm" : "text-emerald-400 font-bold text-sm";
    }
    sim16Render();
}

function sim16Render() {
    const svg = document.getElementById('sim16-svg');
    if (!svg) return;
    const cx = 190, cy = 100, r = 70;
    const n = sim16N;
    
    let pts = [];
    for (let i = 0; i < n; i++) {
        const angle = (i * 2 * Math.PI) / n - Math.PI / 2;
        pts.push([cx + r * Math.cos(angle), cy + r * Math.sin(angle)]);
    }
    
    let html = `
        <polygon points="${pts.map(p => p.join(',')).join(' ')}" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
    `;
    
    // Draw vertex pins and angle arcs
    pts.forEach((p, idx) => {
        html += `<circle cx="${p[0]}" cy="${p[1]}" r="5" fill="#f59e0b" stroke="#fff" stroke-width="1.5"/>`;
    });
    
    html += `<text x="190" y="190" text-anchor="middle" fill="#94a3b8" font-size="11">Rule verified: ${n} straight sides = ${n} interior angles!</text>`;
    svg.innerHTML = html;
}

// Global initialization on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    // Populate voice list
    if ('speechSynthesis' in window) {
        window.speechSynthesis.onvoiceschanged = () => {
            window.speechSynthesis.getVoices();
        };
    }
    // Initialize slide 1
    goToSlide(1);
});
