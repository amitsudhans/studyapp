
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
        case 1: sim1SetView('ground'); break;
        case 2: sim2SetView('iso'); break;
        case 3: sim3SelectObj('bus'); break;
        case 4: sim4SelectSolid('cube'); break;
        case 5: sim5SetTier(1); break;
        case 6: sim6SetView('front'); break;
        case 7: sim7SetMode('3d'); break;
        case 8: sim8SelectDesk(1, 3); break;
        case 9: sim9Render(); break;
        case 10: sim10PlaceItem('ball', 1, 1); break;
        case 11: sim11Reset(); break;
        case 12: sim12SetPath(1); break;
        case 13: sim13OnAltChange(0); break;
        case 14: sim14Inspect('gate'); break;
        case 15: sim15SetRoute('A'); break;
        case 16: sim16Render(); break;
    }
}

// Sim 1: Vantage Point Perspectives
let sim1View = 'ground';
function sim1SetView(v) {
    sim1View = v;
    const btnG = document.getElementById('sim1-view-ground');
    const btnT = document.getElementById('sim1-view-tree');
    const info = document.getElementById('sim1-info');
    
    if (v === 'ground') {
        if (btnG) btnG.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
        if (btnT) btnT.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
        if (info) info.innerHTML = "Ground Level View: The solid brick wall blocks straight line-of-sight, creating a <span class='text-rose-400 font-bold'>red blind spot</span>!";
    } else {
        if (btnT) btnT.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-emerald-600 text-white transition';
        if (btnG) btnG.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
        if (info) info.innerHTML = "Tree Observer View: High elevated vantage point provides a <span class='text-emerald-400 font-bold'>clear green sight line</span> over the wall, exposing the hider!";
    }
    playChime(v === 'tree');
    sim1Render();
}

function sim1Render() {
    const svg = document.getElementById('sim1-svg');
    if (!svg) return;
    let html = `
        <!-- Ground Line -->
        <line x1="20" y1="200" x2="400" y2="200" stroke="#475569" stroke-width="3"/>
        
        <!-- Tree on Left -->
        <rect x="50" y="90" width="25" height="110" fill="#78350f" rx="3"/>
        <circle cx="62" cy="70" r="45" fill="#15803d"/>
        <circle cx="45" cy="60" r="30" fill="#16a34a"/>
        <circle cx="80" cy="65" r="32" fill="#22c55e"/>
        
        <!-- Observer in Tree -->
        <circle cx="62" cy="40" r="7" fill="#fbbf24"/>
        <text x="62" y="25" text-anchor="middle" fill="#fde047" font-size="9" font-weight="bold">Tree Observer</text>
        
        <!-- Seeker at Tree Base -->
        <circle cx="105" cy="180" r="7" fill="#38bdf8"/>
        <text x="105" y="165" text-anchor="middle" fill="#7dd3fc" font-size="9" font-weight="bold">Ground Seeker</text>
        
        <!-- Brick Wall in Middle -->
        <rect x="210" y="125" width="20" height="75" fill="#dc2626" stroke="#991b1b" stroke-width="1.5" rx="2"/>
        <text x="220" y="115" text-anchor="middle" fill="#f87171" font-size="9" font-weight="bold">Wall</text>
        
        <!-- Hider Behind Wall -->
        <circle cx="280" cy="180" r="7" fill="#a855f7"/>
        <text x="280" y="165" text-anchor="middle" fill="#d8b4fe" font-size="9" font-weight="bold">Hider</text>
    `;
    
    if (sim1View === 'ground') {
        // Sight line hits wall and stops
        html += `
            <line x1="110" y1="180" x2="210" y2="180" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4,3"/>
            <circle cx="210" cy="180" r="4" fill="#ef4444"/>
            <!-- Blind spot zone -->
            <polygon points="230,125 400,125 400,200 230,200" fill="#ef4444" fill-opacity="0.25" stroke="#ef4444" stroke-width="1" stroke-dasharray="4,3"/>
            <text x="315" y="145" text-anchor="middle" fill="#f87171" font-size="10" font-weight="bold">BLIND SPOT (Blocked)</text>
        `;
    } else {
        // Sight line from tree clears the wall
        html += `
            <line x1="65" y1="45" x2="280" y2="175" stroke="#10b981" stroke-width="3"/>
            <circle cx="280" cy="175" r="14" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="3,2"/>
            <text x="280" y="145" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">FOUND! (Clear View)</text>
        `;
    }
    svg.innerHTML = html;
}

// Sim 2: 3D Brick Orthogonal Views
let sim2View = 'iso';
function sim2SetView(v) {
    sim2View = v;
    ['iso', 'top', 'front', 'side'].forEach(id => {
        const btn = document.getElementById(`sim2-btn-${id}`);
        if (btn) {
            if (id === v) {
                btn.className = 'px-2 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
            } else {
                btn.className = 'px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
            }
        }
    });
    const pill = document.getElementById('sim2-desc-pill');
    const descs = {
        'iso': "3D Isometric View: Showing Top, Front, and Side faces together in solid space.",
        'top': "Top View: Looking directly down. Shows the wide upper face with the indentation frog.",
        'front': "Front View: Looking straight at the long face. Shows length × height rectangle.",
        'side': "Side View: Looking at the narrow end. Shows width × height profile."
    };
    if (pill) pill.textContent = descs[v];
    playChime(true);
    sim2Render();
}

function sim2Render() {
    const svg = document.getElementById('sim2-svg');
    if (!svg) return;
    let html = '';
    
    if (sim2View === 'iso') {
        // Isometric 3D Brick
        html = `
            <!-- Top Face -->
            <polygon points="190,40 310,75 220,115 100,80" fill="#f97316" stroke="#ea580c" stroke-width="2"/>
            <!-- Frog Indentation on top -->
            <polygon points="190,65 260,85 220,100 150,80" fill="#c2410c" stroke="#9a3412" stroke-width="1.5"/>
            <text x="205" y="86" text-anchor="middle" fill="#fde047" font-size="9" font-weight="bold">Frog</text>
            <!-- Front Face -->
            <polygon points="100,80 220,115 220,175 100,140" fill="#ea580c" stroke="#c2410c" stroke-width="2"/>
            <text x="160" y="135" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">Front Face</text>
            <!-- Side Face -->
            <polygon points="220,115 310,75 310,135 220,175" fill="#9a3412" stroke="#7c2d12" stroke-width="2"/>
            <text x="265" y="130" text-anchor="middle" fill="#fed7aa" font-size="10" font-weight="bold">Side Face</text>
        `;
    } else if (sim2View === 'top') {
        html = `
            <rect x="90" y="45" width="200" height="110" rx="4" fill="#f97316" stroke="#ea580c" stroke-width="3"/>
            <!-- Indentation Frog -->
            <rect x="130" y="70" width="120" height="60" rx="4" fill="#c2410c" stroke="#9a3412" stroke-width="2"/>
            <text x="190" y="105" text-anchor="middle" fill="#fde047" font-size="12" font-weight="bold">TOP VIEW (Plan)</text>
            <text x="190" y="180" text-anchor="middle" fill="#94a3b8" font-size="11">Dimensions: Length (22 cm) × Width (10 cm)</text>
        `;
    } else if (sim2View === 'front') {
        html = `
            <rect x="70" y="65" width="240" height="75" rx="3" fill="#ea580c" stroke="#c2410c" stroke-width="3"/>
            <text x="190" y="110" text-anchor="middle" fill="#fff" font-size="12" font-weight="bold">FRONT VIEW (Elevation)</text>
            <text x="190" y="175" text-anchor="middle" fill="#94a3b8" font-size="11">Dimensions: Length (22 cm) × Height (7 cm)</text>
        `;
    } else {
        html = `
            <rect x="130" y="60" width="120" height="80" rx="3" fill="#9a3412" stroke="#7c2d12" stroke-width="3"/>
            <text x="190" y="105" text-anchor="middle" fill="#fed7aa" font-size="11" font-weight="bold">SIDE VIEW (End)</text>
            <text x="190" y="175" text-anchor="middle" fill="#94a3b8" font-size="11">Dimensions: Width (10 cm) × Height (7 cm)</text>
        `;
    }
    svg.innerHTML = html;
}

// Sim 3: Identifying Common Views
let sim3Obj = 'bus';
function sim3SelectObj(obj) {
    sim3Obj = obj;
    ['bus', 'tv', 'sofa', 'helmet', 'pencil', 'cutter'].forEach(id => {
        const btn = document.getElementById(`sim3-btn-${id}`);
        if (btn) {
            if (id === obj) {
                btn.className = 'px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-amber-500 text-slate-950 transition';
            } else {
                btn.className = 'px-2 py-1.5 rounded-lg text-[11px] font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
            }
        }
    });
    const fb = document.getElementById('sim3-feedback');
    if (fb) fb.textContent = "Which view of the object is shown above? Click a view button!";
    sim3Render();
}

function sim3CheckAnswer(ans) {
    const correctMap = {
        'bus': 'side',
        'tv': 'front',
        'sofa': 'top',
        'helmet': 'front',
        'pencil': 'top',
        'cutter': 'side'
    };
    const isCorrect = (ans === correctMap[sim3Obj]);
    playChime(isCorrect);
    const fb = document.getElementById('sim3-feedback');
    if (fb) {
        if (isCorrect) {
            fb.innerHTML = `<span class="text-emerald-400 font-bold">✓ Correct!</span> That is indeed the ${ans.toUpperCase()} VIEW of the ${sim3Obj.toUpperCase()}!`;
        } else {
            fb.innerHTML = `<span class="text-rose-400 font-bold">✗ Not quite!</span> Look carefully at the angles and features. Try again!`;
        }
    }
}

function sim3Render() {
    const svg = document.getElementById('sim3-svg');
    if (!svg) return;
    let html = '';
    
    if (sim3Obj === 'bus') {
        // Side view of school bus
        html = `
            <rect x="60" y="50" width="260" height="85" rx="10" fill="#eab308" stroke="#ca8a04" stroke-width="3"/>
            <!-- Windows -->
            <rect x="80" y="62" width="35" height="30" rx="3" fill="#38bdf8"/>
            <rect x="125" y="62" width="35" height="30" rx="3" fill="#38bdf8"/>
            <rect x="170" y="62" width="35" height="30" rx="3" fill="#38bdf8"/>
            <rect x="215" y="62" width="35" height="30" rx="3" fill="#38bdf8"/>
            <rect x="260" y="62" width="40" height="30" rx="3" fill="#38bdf8"/>
            <!-- Wheels -->
            <circle cx="110" cy="140" r="20" fill="#1e293b" stroke="#0f172a" stroke-width="4"/>
            <circle cx="110" cy="140" r="8" fill="#94a3b8"/>
            <circle cx="270" cy="140" r="20" fill="#1e293b" stroke="#0f172a" stroke-width="4"/>
            <circle cx="270" cy="140" r="8" fill="#94a3b8"/>
            <text x="190" y="112" text-anchor="middle" fill="#713f12" font-size="12" font-weight="extrabold">SCHOOL BUS</text>
        `;
    } else if (sim3Obj === 'tv') {
        // Front view of television
        html = `
            <rect x="90" y="30" width="200" height="120" rx="6" fill="#0f172a" stroke="#334155" stroke-width="4"/>
            <rect x="100" y="40" width="180" height="100" rx="4" fill="#0284c7"/>
            <polygon points="160,70 160,110 200,90" fill="#fff"/>
            <rect x="175" y="150" width="30" height="18" fill="#475569"/>
            <ellipse cx="190" cy="170" rx="40" ry="8" fill="#334155"/>
        `;
    } else if (sim3Obj === 'sofa') {
        // Top view of sofa
        html = `
            <rect x="80" y="45" width="220" height="100" rx="14" fill="#6366f1" stroke="#4f46e5" stroke-width="3"/>
            <!-- Backrest strip at top -->
            <rect x="85" y="48" width="210" height="28" rx="6" fill="#4338ca"/>
            <!-- Cushions -->
            <rect x="115" y="80" width="70" height="55" rx="5" fill="#818cf8"/>
            <rect x="195" y="80" width="70" height="55" rx="5" fill="#818cf8"/>
            <!-- Armrests -->
            <rect x="85" y="78" width="25" height="60" rx="6" fill="#4338ca"/>
            <rect x="270" y="78" width="25" height="60" rx="6" fill="#4338ca"/>
            <text x="190" y="175" text-anchor="middle" fill="#94a3b8" font-size="11">Cushions & Backrest Viewed Directly Overhead</text>
        `;
    } else if (sim3Obj === 'helmet') {
        // Front view of helmet
        html = `
            <path d="M 120,130 A 70 70 0 1 1 260,130 L 250,150 L 130,150 Z" fill="#ef4444" stroke="#b91c1c" stroke-width="3"/>
            <!-- Visor -->
            <path d="M 135,100 Q 190,120 245,100 L 240,125 Q 190,140 140,125 Z" fill="#38bdf8" fill-opacity="0.8" stroke="#0284c7" stroke-width="2"/>
        `;
    } else if (sim3Obj === 'pencil') {
        // Top view of pencil: circle with lead dot
        html = `
            <circle cx="190" cy="95" r="50" fill="#f59e0b" stroke="#d97706" stroke-width="3"/>
            <circle cx="190" cy="95" r="30" fill="#fed7aa"/>
            <circle cx="190" cy="95" r="8" fill="#1e293b"/>
            <text x="190" y="175" text-anchor="middle" fill="#94a3b8" font-size="11">Unsharpened Pencil Hexagon/Circular Top</text>
        `;
    } else {
        // Pizza cutter: side view showing wheel and handle
        html = `
            <circle cx="130" cy="110" r="45" fill="#cbd5e1" stroke="#94a3b8" stroke-width="3"/>
            <circle cx="130" cy="110" r="8" fill="#475569"/>
            <!-- Handle -->
            <rect x="130" y="104" width="140" height="14" rx="4" fill="#dc2626" transform="rotate(-25 130 110)"/>
        `;
    }
    svg.innerHTML = html;
}

// Sim 4: Matching Geometric Views
let sim4Solid = 'cube';
function sim4SelectSolid(s) {
    sim4Solid = s;
    ['cube', 'triprism', 'sqpyr', 'cylinder'].forEach(id => {
        const btn = document.getElementById(`sim4-btn-${id}`);
        if (btn) {
            if (id === s) {
                btn.className = 'px-2 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
            } else {
                btn.className = 'px-2 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
            }
        }
    });
    const summary = document.getElementById('sim4-summary');
    const texts = {
        'cube': "Cube: Top = Square, Front = Square, Side = Square (All 3 projections are identical squares!).",
        'triprism': "Triangular Prism: Front = Triangle, Top = Divided Rectangle, Side = Rectangle.",
        'sqpyr': "Square Pyramid: Front = Triangle, Side = Triangle, Top = Square with diagonal apex lines (X).",
        'cylinder': "Cylinder: Top = Circle, Front = Rectangle, Side = Rectangle."
    };
    if (summary) summary.textContent = texts[s];
    playChime(true);
    sim4Render();
}

function sim4Render() {
    const svg = document.getElementById('sim4-svg');
    if (!svg) return;
    let html = '';
    
    // 3 Boxes: Top View (Left), Front View (Middle), Side View (Right)
    const bx = [60, 200, 340];
    const labels = ["Top View", "Front View", "Side View"];
    
    labels.forEach((lbl, idx) => {
        html += `<text x="${bx[idx]}" y="30" text-anchor="middle" fill="#94a3b8" font-size="11" font-weight="bold">${lbl}</text>`;
    });
    
    if (sim4Solid === 'cube') {
        bx.forEach(x => {
            html += `<rect x="${x - 35}" y="55" width="70" height="70" fill="#3b82f6" stroke="#60a5fa" stroke-width="2"/>`;
        });
    } else if (sim4Solid === 'triprism') {
        // Top: Rectangle with center crease
        html += `
            <rect x="${bx[0] - 40}" y="60" width="80" height="60" fill="#6366f1" stroke="#818cf8" stroke-width="2"/>
            <line x1="${bx[0]}" y1="60" x2="${bx[0]}" y2="120" stroke="#fbbf24" stroke-width="2"/>
        `;
        // Front: Triangle
        html += `<polygon points="${bx[1]},55 ${bx[1] + 40},125 ${bx[1] - 40},125" fill="#ec4899" stroke="#f472b6" stroke-width="2"/>`;
        // Side: Rectangle
        html += `<rect x="${bx[2] - 40}" y="60" width="80" height="65" fill="#6366f1" stroke="#818cf8" stroke-width="2"/>`;
    } else if (sim4Solid === 'sqpyr') {
        // Top: Square with diagonals
        html += `
            <rect x="${bx[0] - 35}" y="55" width="70" height="70" fill="#d97706" stroke="#f59e0b" stroke-width="2"/>
            <line x1="${bx[0] - 35}" y1="55" x2="${bx[0] + 35}" y2="125" stroke="#fef08a" stroke-width="1.5"/>
            <line x1="${bx[0] + 35}" y1="55" x2="${bx[0] - 35}" y2="125" stroke="#fef08a" stroke-width="1.5"/>
            <circle cx="${bx[0]}" cy="90" r="4" fill="#ef4444"/>
        `;
        // Front: Triangle
        html += `<polygon points="${bx[1]},55 ${bx[1] + 35},125 ${bx[1] - 35},125" fill="#b45309" stroke="#fbbf24" stroke-width="2"/>`;
        // Side: Triangle
        html += `<polygon points="${bx[2]},55 ${bx[2] + 35},125 ${bx[2] - 35},125" fill="#b45309" stroke="#fbbf24" stroke-width="2"/>`;
    } else {
        // Cylinder
        // Top: Circle
        html += `<circle cx="${bx[0]}" cy="90" r="35" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>`;
        // Front: Rectangle
        html += `<rect x="${bx[1] - 35}" y="55" width="70" height="75" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>`;
        // Side: Rectangle
        html += `<rect x="${bx[2] - 35}" y="55" width="70" height="75" fill="#0369a1" stroke="#38bdf8" stroke-width="2"/>`;
    }
    svg.innerHTML = html;
}

// Sim 5: Matchbox Block Buildings
let sim5Tier = 1;
function sim5SetTier(t) {
    sim5Tier = t;
    [1, 2, 3].forEach(id => {
        const btn = document.getElementById(`sim5-btn-${id === 1 ? 'base' : (id === 2 ? 't2' : 't3')}`);
        if (btn) {
            if (id === t) {
                btn.className = 'px-2.5 py-2 rounded-lg bg-amber-500 text-slate-950 font-bold text-xs transition';
            } else {
                btn.className = 'px-2.5 py-2 rounded-lg bg-slate-800 text-slate-300 hover:text-white font-medium text-xs transition border border-slate-700';
            }
        }
    });
    const cnt = document.getElementById('sim5-block-count');
    const totalMap = { 1: "4 Matchboxes", 2: "6 Matchboxes (4 + 2)", 3: "7 Matchboxes (4 + 2 + 1)" };
    if (cnt) cnt.textContent = totalMap[t];
    playChime(true);
    sim5Render();
}

function sim5Reset() {
    sim5SetTier(1);
}

function sim5Render() {
    const svg = document.getElementById('sim5-svg');
    if (!svg) return;
    
    function drawMatchbox(cx, cy, colorTop, colorFront, colorSide) {
        const dx = 32, dy = 16, h = 18;
        return `
            <!-- Top -->
            <polygon points="${cx},${cy - h} ${cx + dx},${cy - dy - h} ${cx},${cy - 2*dy - h} ${cx - dx},${cy - dy - h}" fill="${colorTop}" stroke="#0f172a" stroke-width="1"/>
            <!-- Front Left -->
            <polygon points="${cx - dx},${cy - dy - h} ${cx},${cy - h} ${cx},${cy} ${cx - dx},${cy - dy}" fill="${colorFront}" stroke="#0f172a" stroke-width="1"/>
            <!-- Front Right -->
            <polygon points="${cx},${cy - h} ${cx + dx},${cy - dy - h} ${cx + dx},${cy - dy} ${cx},${cy}" fill="${colorSide}" stroke="#0f172a" stroke-width="1"/>
        `;
    }
    
    let html = '';
    // Tier 1 Base: 2x2 = 4 matchboxes
    const baseCoords = [ [0,0], [1,0], [0,1], [1,1] ];
    baseCoords.forEach(c => {
        const x = 190 + (c[0] - c[1]) * 32;
        const y = 140 + (c[0] + c[1]) * 16;
        html += drawMatchbox(x, y, '#f59e0b', '#d97706', '#b45309');
    });
    
    if (sim5Tier >= 2) {
        // Tier 2: 2 matchboxes on top
        const t2Coords = [ [0,0], [1,0] ];
        t2Coords.forEach(c => {
            const x = 190 + (c[0] - c[1]) * 32;
            const y = 140 + (c[0] + c[1]) * 16 - 18;
            html += drawMatchbox(x, y, '#38bdf8', '#0284c7', '#0369a1');
        });
    }
    
    if (sim5Tier >= 3) {
        // Tier 3: 1 matchbox tower
        html += drawMatchbox(190, 140 - 36, '#10b981', '#059669', '#047857');
    }
    
    svg.innerHTML = html;
}

// Sim 6: Multi-Angle Building Views
let sim6View = 'front';
function sim6SetView(v) {
    sim6View = v;
    ['front', 'back', 'side', 'top'].forEach(id => {
        const btn = document.getElementById(`sim6-btn-${id}`);
        if (btn) {
            if (id === v) {
                btn.className = 'px-2 py-1 rounded text-xs font-semibold bg-amber-500 text-slate-950 transition';
            } else {
                btn.className = 'px-2 py-1 rounded text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
            }
        }
    });
    const note = document.getElementById('sim6-note');
    const notes = {
        'front': "Front View: Left column has 3 blocks, Middle has 2 blocks, Right has 1 block.",
        'back': "Back View: REVERSED! Left column now has 1 block, Middle has 2, Right has 3 blocks.",
        'side': "Side View: Shows depth. Tallest 3-block column obscures the shorter blocks behind it.",
        'top': "Top Plan View: 2D Footprint showing occupied ground tiles; vertical height disappears!"
    };
    if (note) note.textContent = notes[v];
    playChime(true);
    sim6Render();
}

function sim6Render() {
    const svg = document.getElementById('sim6-svg');
    if (!svg) return;
    const bW = 40, bH = 30;
    let html = '';
    
    if (sim6View === 'front') {
        // Front: 3 on left, 2 in mid, 1 on right
        // Left col (x=110): 3 blocks
        for (let i=0; i<3; i++) html += `<rect x="110" y="${140 - i*bH}" width="${bW}" height="${bH}" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>`;
        // Mid col (x=170): 2 blocks
        for (let i=0; i<2; i++) html += `<rect x="170" y="${140 - i*bH}" width="${bW}" height="${bH}" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>`;
        // Right col (x=230): 1 block
        html += `<rect x="230" y="140" width="${bW}" height="${bH}" fill="#10b981" stroke="#059669" stroke-width="2"/>`;
    } else if (sim6View === 'back') {
        // Back: 1 on left, 2 in mid, 3 on right (horizontally reversed)
        html += `<rect x="110" y="140" width="${bW}" height="${bH}" fill="#10b981" stroke="#059669" stroke-width="2"/>`;
        for (let i=0; i<2; i++) html += `<rect x="170" y="${140 - i*bH}" width="${bW}" height="${bH}" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>`;
        for (let i=0; i<3; i++) html += `<rect x="230" y="${140 - i*bH}" width="${bW}" height="${bH}" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>`;
    } else if (sim6View === 'side') {
        // Side: 3 blocks high
        for (let i=0; i<3; i++) html += `<rect x="170" y="${140 - i*bH}" width="${bW}" height="${bH}" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>`;
    } else {
        // Top Plan: 3 squares in a row
        html += `
            <rect x="110" y="80" width="${bW}" height="${bW}" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
            <rect x="170" y="80" width="${bW}" height="${bW}" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
            <rect x="230" y="80" width="${bW}" height="${bW}" fill="#10b981" stroke="#059669" stroke-width="2"/>
            <text x="130" y="105" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">3</text>
            <text x="190" y="105" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">2</text>
            <text x="250" y="105" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">1</text>
        `;
    }
    svg.innerHTML = html;
}

// Sim 7: Classroom Spatial Mapping
let sim7Mode = '3d';
function sim7SetMode(m) {
    sim7Mode = m;
    const btn3 = document.getElementById('sim7-btn-3d');
    const btn2 = document.getElementById('sim7-btn-2d');
    const desc = document.getElementById('sim7-desc');
    if (m === '3d') {
        if (btn3) btn3.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
        if (btn2) btn2.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
        if (desc) desc.textContent = "3D Window View: The cat sits on the open window sill, looking inside at rows of desks!";
    } else {
        if (btn2) btn2.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
        if (btn3) btn3.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
        if (desc) desc.textContent = "2D Floor Plan: Overhead bird's-eye architectural blueprint of desks, doors, and boards.";
    }
    playChime(true);
    sim7Render();
}

function sim7Render() {
    const svg = document.getElementById('sim7-svg');
    if (!svg) return;
    let html = '';
    
    if (sim7Mode === '3d') {
        // Perspective room view from window
        html = `
            <!-- Window Frame -->
            <rect x="20" y="20" width="360" height="180" fill="none" stroke="#64748b" stroke-width="8" rx="4"/>
            <!-- Cat Silhouette on sill -->
            <ellipse cx="60" cy="180" rx="14" ry="10" fill="#f59e0b"/>
            <circle cx="68" cy="172" r="7" fill="#f59e0b"/>
            <!-- Classroom Interior -->
            <polygon points="50,160 350,160 380,20 20,20" fill="#1e293b"/>
            <!-- Chalkboard on front wall -->
            <rect x="130" y="35" width="140" height="45" fill="#065f46" stroke="#047857" stroke-width="3"/>
            <text x="200" y="62" text-anchor="middle" fill="#a7f3d0" font-size="10" font-weight="bold">CHALKBOARD</text>
            <!-- Desks rows in perspective -->
            <rect x="100" y="100" width="60" height="20" fill="#78350f" rx="2"/>
            <rect x="180" y="100" width="60" height="20" fill="#78350f" rx="2"/>
            <rect x="80" y="130" width="70" height="22" fill="#92400e" rx="2"/>
            <rect x="170" y="130" width="70" height="22" fill="#92400e" rx="2"/>
        `;
    } else {
        // 2D Overhead Blueprint
        html = `
            <!-- Room Outline -->
            <rect x="40" y="25" width="320" height="160" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
            <!-- Door -->
            <line x1="360" y1="130" x2="360" y2="165" stroke="#ef4444" stroke-width="4"/>
            <text x="375" y="152" fill="#f87171" font-size="9" font-weight="bold">Door</text>
            <!-- Chalkboard -->
            <rect x="130" y="25" width="140" height="8" fill="#10b981"/>
            <text x="200" y="45" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">Front Chalkboard (Row 1 is here)</text>
            <!-- Desk Matrix (3 rows x 3 cols) -->
            ${[0, 1, 2].map(r => [0, 1, 2].map(c => `
                <rect x="${85 + c*80}" y="${65 + r*36}" width="50" height="22" rx="3" fill="#1e3a8a" stroke="#60a5fa" stroke-width="1.5"/>
                <text x="${110 + c*80}" y="${80 + r*36}" text-anchor="middle" fill="#bfdbfe" font-size="8">R${r+1},C${c+1}</text>
            `).join('')).join('')}
        `;
    }
    svg.innerHTML = html;
}

// Sim 8: Desk Positional Terms
let sim8ActiveR = 1;
let sim8ActiveC = 3;
function sim8SelectDesk(r, c) {
    sim8ActiveR = r;
    sim8ActiveC = c;
    const verdict = document.getElementById('sim8-verdict');
    const descs = {
        '1_3': "Target: Third desk in the first row (Front row nearest the chalkboard, 3rd from left).",
        '2_2': "Target: Middle desk of the second row (Central seat in row 2).",
        '3_1': "Target: First desk in the third row (Back-left aisle seat).",
        '3_4': "Target: Back-right corner desk (Row 3, Column 4)."
    };
    if (verdict) verdict.textContent = descs[`${r}_${c}`] || `Desk: Row ${r}, Column ${c}`;
    playChime(true);
    sim8Render();
}

function sim8Render() {
    const svg = document.getElementById('sim8-svg');
    if (!svg) return;
    let html = `
        <!-- Chalkboard at top -->
        <rect x="100" y="10" width="180" height="8" fill="#059669"/>
        <text x="190" y="30" text-anchor="middle" fill="#34d399" font-size="10" font-weight="bold">FRONT OF CLASSROOM (CHALKBOARD)</text>
    `;
    
    // 3 rows x 4 columns of desks
    for (let r = 1; r <= 3; r++) {
        for (let c = 1; c <= 4; c++) {
            const x = 50 + (c - 1) * 75;
            const y = 45 + (r - 1) * 45;
            const isTarget = (r === sim8ActiveR && c === sim8ActiveC);
            const fill = isTarget ? '#10b981' : '#1e293b';
            const stroke = isTarget ? '#34d399' : '#475569';
            
            html += `
                <rect x="${x}" y="${y}" width="55" height="30" rx="4" fill="${fill}" stroke="${stroke}" stroke-width="${isTarget ? '3' : '1.5'}"/>
                <text x="${x + 27}" y="${y + 19}" text-anchor="middle" fill="${isTarget ? '#fff' : '#94a3b8'}" font-size="9" font-weight="${isTarget ? 'bold' : 'normal'}">R${r}, C${c}</text>
            `;
        }
    }
    svg.innerHTML = html;
}

// Sim 9: Grid System Navigation
let sim9SelectedR = 2;
let sim9SelectedC = 2;
function sim9ClickCell(r, c) {
    sim9SelectedR = r;
    sim9SelectedC = c;
    const status = document.getElementById('sim9-status');
    if (status) {
        status.innerHTML = `Selected Coordinate: <span class="text-amber-400 font-bold">Row ${r}, Column ${c}</span> (Intersection of Horizontal Row ${r} and Vertical Column ${c})!`;
    }
    playChime(true);
    sim9Render();
}

function sim9Render() {
    const svg = document.getElementById('sim9-svg');
    if (!svg) return;
    const s = 50; // cell size
    const ox = 115, oy = 35;
    let html = '';
    
    // Column headers
    for (let c = 1; c <= 3; c++) {
        html += `<text x="${ox + (c - 0.5)*s}" y="${oy - 10}" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="bold">Col ${c}</text>`;
    }
    // Row headers
    for (let r = 1; r <= 3; r++) {
        html += `<text x="${ox - 15}" y="${oy + (r - 0.5)*s + 4}" text-anchor="end" fill="#f59e0b" font-size="11" font-weight="bold">Row ${r}</text>`;
    }
    
    // Highlight active row & col bands
    html += `
        <!-- Active Row Band -->
        <rect x="${ox}" y="${oy + (sim9SelectedR - 1)*s}" width="${3*s}" height="${s}" fill="#f59e0b" fill-opacity="0.15"/>
        <!-- Active Col Band -->
        <rect x="${ox + (sim9SelectedC - 1)*s}" y="${oy}" width="${s}" height="${3*s}" fill="#38bdf8" fill-opacity="0.15"/>
    `;
    
    // Draw 3x3 cells
    for (let r = 1; r <= 3; r++) {
        for (let c = 1; c <= 3; c++) {
            const x = ox + (c - 1)*s;
            const y = oy + (r - 1)*s;
            const isMatch = (r === sim9SelectedR && c === sim9SelectedC);
            html += `
                <rect x="${x}" y="${y}" width="${s}" height="${s}" fill="${isMatch ? '#10b981' : '#1e293b'}" stroke="#475569" stroke-width="1.5" class="cursor-pointer transition hover:opacity-80" onclick="sim9ClickCell(${r}, ${c})"/>
                <text x="${x + s/2}" y="${y + s/2 + 4}" text-anchor="middle" fill="${isMatch ? '#fff' : '#cbd5e1'}" font-size="10" font-weight="bold" onclick="sim9ClickCell(${r}, ${c})">(${r},${c})</text>
            `;
        }
    }
    svg.innerHTML = html;
}

// Sim 10: Locating Grid Coordinates
let sim10Items = { 'ball': [1,1] };
function sim10PlaceItem(item, r, c) {
    sim10Items[item] = [r, c];
    const fb = document.getElementById('sim10-feedback');
    const itemNames = {
        'ball': "⚽ Soccer Ball placed at Row 1, Column 1 (Top-Left corner)!",
        'apple': "🍎 Red Apple placed at Row 2, Column 2 (Exact Center)!",
        'flower': "🌸 Flower placed at Row 3, Column 2 (Bottom Middle)!",
        'book': "📖 Storybook placed at Row 1, Column 3 (Top-Right corner)!"
    };
    if (fb) fb.innerHTML = `<span class="text-emerald-400 font-bold">✓ Clue Solved:</span> ${itemNames[item]}`;
    playChime(true);
    sim10Render();
}

function sim10Render() {
    const svg = document.getElementById('sim10-svg');
    if (!svg) return;
    const s = 45;
    const ox = 120, oy = 25;
    let html = '';
    
    // Headers
    for (let c = 1; c <= 3; c++) html += `<text x="${ox + (c - 0.5)*s}" y="${oy - 8}" text-anchor="middle" fill="#38bdf8" font-size="10">Col ${c}</text>`;
    for (let r = 1; r <= 3; r++) html += `<text x="${ox - 10}" y="${oy + (r - 0.5)*s + 4}" text-anchor="end" fill="#f59e0b" font-size="10">Row ${r}</text>`;
    
    // Draw cells
    for (let r = 1; r <= 3; r++) {
        for (let c = 1; c <= 3; c++) {
            const x = ox + (c - 1)*s;
            const y = oy + (r - 1)*s;
            html += `<rect x="${x}" y="${y}" width="${s}" height="${s}" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>`;
            
            // Check for placed items
            for (let [it, pos] of Object.entries(sim10Items)) {
                if (pos[0] === r && pos[1] === c) {
                    const icons = { 'ball': '⚽', 'apple': '🍎', 'flower': '🌸', 'book': '📖' };
                    html += `<text x="${x + s/2}" y="${y + s/2 + 6}" text-anchor="middle" font-size="20">${icons[it]}</text>`;
                }
            }
        }
    }
    svg.innerHTML = html;
}

// Sim 11: Treasure Hunt Grid
let sim11Pos = [4, 1]; // Row 4, Col 1
function sim11Move(dir) {
    let r = sim11Pos[0];
    let c = sim11Pos[1];
    if (dir === 'up' && r > 1) r--;
    if (dir === 'down' && r < 4) r++;
    if (dir === 'left' && c > 1) c--;
    if (dir === 'right' && c < 4) c++;
    
    sim11Pos = [r, c];
    const info = document.getElementById('sim11-info');
    const treasures = {
        '2_3': '🥭 Sweet Mango reached at Row 2, Column 3!',
        '1_4': '👑 Golden Crown found at Row 1, Column 4!',
        '3_4': '🐱 Sleeping Cat found at Row 3, Column 4!',
        '2_2': '🌸 Flower Blossom found at Row 2, Column 2!'
    };
    playChime(true);
    if (info) {
        info.innerHTML = treasures[`${r}_${c}`] || `Explorer moved to: <span class="text-amber-400 font-bold">Row ${r}, Column ${c}</span>`;
    }
    sim11Render();
}

function sim11Reset() {
    sim11Pos = [4, 1];
    const info = document.getElementById('sim11-info');
    if (info) info.textContent = "Start at Bottom-Left (Row 4, Col 1). Use directional buttons to reach hidden treasures!";
    sim11Render();
}

function sim11Render() {
    const svg = document.getElementById('sim11-svg');
    if (!svg) return;
    const s = 50;
    const ox = 20, oy = 20;
    let html = '';
    
    const targets = {
        '2_3': '🥭',
        '1_4': '👑',
        '3_4': '🐱',
        '2_2': '🌸'
    };
    
    for (let r = 1; r <= 4; r++) {
        for (let c = 1; c <= 4; c++) {
            const x = ox + (c - 1)*s;
            const y = oy + (r - 1)*s;
            const isPlayer = (r === sim11Pos[0] && c === sim11Pos[1]);
            
            html += `<rect x="${x}" y="${y}" width="${s}" height="${s}" fill="${isPlayer ? '#10b981' : '#1e293b'}" stroke="#334155" stroke-width="1.5"/>`;
            
            if (isPlayer) {
                html += `<circle cx="${x + s/2}" cy="${y + s/2}" r="14" fill="#38bdf8"/>`;
                html += `<text x="${x + s/2}" y="${y + s/2 + 5}" text-anchor="middle" font-size="14">🚶</text>`;
            } else if (targets[`${r}_${c}`]) {
                html += `<text x="${x + s/2}" y="${y + s/2 + 7}" text-anchor="middle" font-size="18">${targets[`${r}_${c}`]}</text>`;
            }
        }
    }
    svg.innerHTML = html;
}

// Sim 12: Path Step Counting
let sim12ActivePath = 1;
function sim12SetPath(p) {
    sim12ActivePath = p;
    const btn1 = document.getElementById('sim12-btn-p1');
    const btn2 = document.getElementById('sim12-btn-p2');
    const vert = document.getElementById('sim12-vert');
    const horiz = document.getElementById('sim12-horiz');
    if (p === 1) {
        if (btn1) btn1.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
        if (btn2) btn2.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
        if (vert) vert.textContent = "3 steps Up first";
        if (horiz) horiz.textContent = "2 steps Right second";
    } else {
        if (btn2) btn2.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 transition';
        if (btn1) btn1.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
        if (horiz) horiz.textContent = "2 steps Right first";
        if (vert) vert.textContent = "3 steps Up second";
    }
    playChime(true);
    sim12Render();
}

function sim12Render() {
    const svg = document.getElementById('sim12-svg');
    if (!svg) return;
    const s = 45;
    const ox = 70, oy = 20;
    let html = '';
    
    // Draw 4x4 grid lines
    for (let r = 1; r <= 4; r++) {
        for (let c = 1; c <= 4; c++) {
            const x = ox + (c - 1)*s;
            const y = oy + (r - 1)*s;
            html += `<rect x="${x}" y="${y}" width="${s}" height="${s}" fill="#1e293b" stroke="#334155" stroke-width="1"/>`;
        }
    }
    
    // Start (Row 4, Col 1) and Target (Row 1, Col 3)
    const sx = ox + 0.5*s, sy = oy + 3.5*s;
    const tx = ox + 2.5*s, ty = oy + 0.5*s;
    
    // Draw Path
    if (sim12ActivePath === 1) {
        // Up 3 steps, then Right 2 steps
        html += `
            <line x1="${sx}" y1="${sy}" x2="${sx}" y2="${ty}" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
            <line x1="${sx}" y1="${ty}" x2="${tx}" y2="${ty}" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>
        `;
    } else {
        // Right 2 steps, then Up 3 steps
        html += `
            <line x1="${sx}" y1="${sy}" x2="${tx}" y2="${sy}" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>
            <line x1="${tx}" y1="${sy}" x2="${tx}" y2="${ty}" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
        `;
    }
    
    // Start & End markers
    html += `
        <circle cx="${sx}" cy="${sy}" r="9" fill="#10b981"/>
        <text x="${sx}" y="${sy + 18}" text-anchor="middle" fill="#34d399" font-size="9" font-weight="bold">Start</text>
        <circle cx="${tx}" cy="${ty}" r="9" fill="#ef4444"/>
        <text x="${tx}" y="${ty - 12}" text-anchor="middle" fill="#f87171" font-size="9" font-weight="bold">Target (🥭)</text>
    `;
    svg.innerHTML = html;
}

// Sim 13: Drone Aerial Views
let sim13Alt = 0;
function sim13OnAltChange(v) {
    sim13Alt = parseInt(v, 10);
    const disp = document.getElementById('sim13-alt-disp');
    const val = document.getElementById('sim13-val');
    if (disp) disp.textContent = `${sim13Alt} m`;
    if (val) val.textContent = `${sim13Alt}m`;
    sim13Render();
}

function sim13Render() {
    const svg = document.getElementById('sim13-svg');
    if (!svg) return;
    const f = sim13Alt / 100; // 0 to 1
    let html = '';
    
    // Pitch height shrinks from 50px at ground level to 0px at overhead
    const pitchH = 50 * (1 - f);
    const cx = 190, cy = 110;
    
    // Pitched building roof
    html += `
        <!-- Left roof slope -->
        <polygon points="${cx - 80},${cy + 40} ${cx},${cy - pitchH} ${cx},${cy - pitchH + 60} ${cx - 80},${cy + 100}" fill="#dc2626" stroke="#b91c1c" stroke-width="1.5"/>
        <!-- Right roof slope -->
        <polygon points="${cx},${cy - pitchH} ${cx + 80},${cy + 40} ${cx + 80},${cy + 100} ${cx},${cy - pitchH + 60}" fill="#ea580c" stroke="#c2410c" stroke-width="1.5"/>
        <line x1="${cx}" y1="${cy - pitchH}" x2="${cx}" y2="${cy - pitchH + 60}" stroke="#facc15" stroke-width="3"/>
    `;
    
    if (f > 0.8) {
        html += `<text x="190" y="30" text-anchor="middle" fill="#34d399" font-size="11" font-weight="bold">True 2D Plan Footprint Formed!</text>`;
    } else {
        html += `<text x="190" y="30" text-anchor="middle" fill="#94a3b8" font-size="11">Ascend drone slider to flatten 3D into 2D map</text>`;
    }
    svg.innerHTML = html;
}

// Sim 14: School Campus Blueprint
function sim14Inspect(fac) {
    const pill = document.getElementById('sim14-inspect-pill');
    const details = {
        'gate': "Entrance Gate: Located at bottom perimeter boundary baseline.",
        'stage': "Assembly Stage: Elevated platform on western side of central courtyard.",
        'class': "Class 4 Rooms: West academic wing across from the courtyard.",
        'lib': "Library: North-west corner; quiet study zone.",
        'kitchen': "MDM Kitchen: East wing where warm midday lunches are cooked.",
        'play': "Playground: Expansive north sports grounds with football goalposts."
    };
    if (pill && details[fac]) pill.innerHTML = `<span class="text-amber-400 font-bold">Facility Inspected:</span> ${details[fac]}`;
    playChime(true);
}

function sim14Render() {
    const svg = document.getElementById('sim14-svg');
    if (!svg) return;
    let html = `
        <!-- Campus Boundary -->
        <rect x="30" y="20" width="340" height="175" fill="#0f172a" stroke="#475569" stroke-width="2" rx="4"/>
        
        <!-- Entrance Gate (Bottom) -->
        <rect x="160" y="185" width="80" height="10" fill="#f59e0b" class="cursor-pointer" onclick="sim14Inspect('gate')"/>
        <text x="200" y="180" text-anchor="middle" fill="#fbbf24" font-size="9" font-weight="bold" class="cursor-pointer" onclick="sim14Inspect('gate')">Main Gate</text>
        
        <!-- Assembly Stage (Left of center) -->
        <rect x="60" y="110" width="60" height="35" rx="3" fill="#6366f1" class="cursor-pointer" onclick="sim14Inspect('stage')"/>
        <text x="90" y="132" text-anchor="middle" fill="#e0e7ff" font-size="8" font-weight="bold" class="cursor-pointer" onclick="sim14Inspect('stage')">Stage</text>
        
        <!-- Class 4 Classrooms (West wing) -->
        <rect x="60" y="55" width="60" height="45" rx="3" fill="#0284c7" class="cursor-pointer" onclick="sim14Inspect('class')"/>
        <text x="90" y="82" text-anchor="middle" fill="#e0f2fe" font-size="8" font-weight="bold" class="cursor-pointer" onclick="sim14Inspect('class')">Class 4</text>
        
        <!-- Library (Top West) -->
        <rect x="135" y="30" width="55" height="30" rx="3" fill="#a855f7" class="cursor-pointer" onclick="sim14Inspect('lib')"/>
        <text x="162" y="48" text-anchor="middle" fill="#f3e8ff" font-size="8" font-weight="bold" class="cursor-pointer" onclick="sim14Inspect('lib')">Library</text>
        
        <!-- MDM Kitchen (East wing) -->
        <rect x="280" y="110" width="65" height="40" rx="3" fill="#ea580c" class="cursor-pointer" onclick="sim14Inspect('kitchen')"/>
        <text x="312" y="133" text-anchor="middle" fill="#fff" font-size="8" font-weight="bold" class="cursor-pointer" onclick="sim14Inspect('kitchen')">Kitchen</text>
        
        <!-- Sports Playground (North East) -->
        <rect x="210" y="30" width="135" height="65" rx="4" fill="#065f46" class="cursor-pointer" onclick="sim14Inspect('play')"/>
        <text x="277" y="66" text-anchor="middle" fill="#a7f3d0" font-size="9" font-weight="bold" class="cursor-pointer" onclick="sim14Inspect('play')">Playground</text>
        
        <!-- Central Courtyard / Paths -->
        <line x1="200" y1="185" x2="200" y2="105" stroke="#94a3b8" stroke-width="12" stroke-dasharray="4,2"/>
        <line x1="120" y1="125" x2="280" y2="125" stroke="#94a3b8" stroke-width="10"/>
    `;
    svg.innerHTML = html;
}

// Sim 15: Shortest Route Navigation
let sim15Route = 'A';
function sim15SetRoute(r) {
    sim15Route = r;
    const btnA = document.getElementById('sim15-btn-ra');
    const btnB = document.getElementById('sim15-btn-rb');
    if (r === 'A') {
        if (btnA) btnA.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-emerald-600 text-white transition';
        if (btnB) btnB.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
    } else {
        if (btnB) btnB.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-rose-600 text-white transition';
        if (btnA) btnA.className = 'px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:text-white transition';
    }
    playChime(r === 'A');
    sim15Render();
}

function sim15Render() {
    const svg = document.getElementById('sim15-svg');
    if (!svg) return;
    let html = `
        <!-- Classroom Box -->
        <rect x="50" y="60" width="70" height="50" rx="4" fill="#0284c7"/>
        <text x="85" y="88" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">Class 4</text>
        
        <!-- Stage Box -->
        <rect x="50" y="150" width="70" height="45" rx="4" fill="#6366f1"/>
        <text x="85" y="176" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">Stage</text>
        
        <!-- Playground Obstacle -->
        <rect x="160" y="50" width="160" height="90" rx="6" fill="#065f46"/>
        <text x="240" y="98" text-anchor="middle" fill="#a7f3d0" font-size="11" font-weight="bold">Playground</text>
    `;
    
    if (sim15Route === 'A') {
        // Direct indoor corridor: 60m
        html += `
            <line x1="85" y1="110" x2="85" y2="150" stroke="#10b981" stroke-width="6" stroke-linecap="round"/>
            <text x="105" y="133" fill="#34d399" font-size="11" font-weight="extrabold">Route A: 60m</text>
        `;
    } else {
        // Circuitous route around playground: 95m
        html += `
            <path d="M 120,80 L 335,80 L 335,170 L 120,170" fill="none" stroke="#f43f5e" stroke-width="5" stroke-dasharray="6,3"/>
            <text x="240" y="160" text-anchor="middle" fill="#fb7185" font-size="11" font-weight="extrabold">Route B: 95m (Around Playground)</text>
        `;
    }
    svg.innerHTML = html;
}

// Sim 16: Campus Sight Mapping
let sim16Step = 1;
function sim16StepNext() {
    sim16Step = (sim16Step % 6) + 1;
    const pill = document.getElementById('sim16-waypoint-pill');
    const waypoints = [
        "",
        "Waypoint 1: Start at the Main Security Entrance Gate.",
        "Waypoint 2: Walk straight ahead past the Drinking Water Fountain on the right.",
        "Waypoint 3: Turn 90° LEFT at the tall green Ashoka tree.",
        "Waypoint 4: Continue straight past the Principal's Administration Office.",
        "Waypoint 5: Ascend the central stone staircase to the first floor corridor.",
        "Waypoint 6: Turn RIGHT into Doorway 2: Arrived at Classroom Desk!"
    ];
    if (pill) pill.textContent = waypoints[sim16Step];
    playChime(true);
    sim16Render();
}

function sim16Render() {
    const svg = document.getElementById('sim16-svg');
    if (!svg) return;
    
    const pts = [
        [190, 200], // Gate
        [190, 150], // Water fountain
        [190, 110], // Ashoka tree (turn left)
        [110, 110], // Office
        [110, 60],  // Stairs
        [70, 60]    // Desk
    ];
    
    let html = `
        <!-- Compass Rose -->
        <g transform="translate(330, 45)">
            <circle cx="0" cy="0" r="18" fill="#1e293b" stroke="#475569"/>
            <text x="0" y="-5" text-anchor="middle" fill="#f59e0b" font-size="9" font-weight="bold">N</text>
            <text x="0" y="13" text-anchor="middle" fill="#94a3b8" font-size="8">S</text>
            <text x="10" y="4" text-anchor="middle" fill="#94a3b8" font-size="8">E</text>
            <text x="-10" y="4" text-anchor="middle" fill="#94a3b8" font-size="8">W</text>
        </g>
    `;
    
    // Draw trail up to current step
    for (let i = 0; i < sim16Step - 1; i++) {
        html += `<line x1="${pts[i][0]}" y1="${pts[i][1]}" x2="${pts[i+1][0]}" y2="${pts[i+1][1]}" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>`;
    }
    
    // Draw Waypoint dots
    pts.forEach((p, idx) => {
        const isReached = (idx + 1 <= sim16Step);
        const isCurrent = (idx + 1 === sim16Step);
        html += `
            <circle cx="${p[0]}" cy="${p[1]}" r="${isCurrent ? '8' : '5'}" fill="${isCurrent ? '#10b981' : (isReached ? '#f59e0b' : '#334155')}" stroke="#fff" stroke-width="1.5"/>
            <text x="${p[0] + 14}" y="${p[1] + 4}" fill="${isCurrent ? '#34d399' : '#94a3b8'}" font-size="9" font-weight="${isCurrent ? 'bold' : 'normal'}">W${idx + 1}</text>
        `;
    });
    
    svg.innerHTML = html;
}

// Global initialization on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.onvoiceschanged = () => {
            window.speechSynthesis.getVoices();
        };
    }
    goToSlide(1);
});
