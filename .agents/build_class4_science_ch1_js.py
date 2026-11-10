# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 1: Living Together
Generates the complete JavaScript Engine for Chapter 1.
"""

import sys
import os

js_code = r'''
// ============================================================================
// State Management & Audio Setup
// ============================================================================
let currentSlide = 1;
const totalSlides = 20;
let isSpeaking = false;
let currentUtterance = null;
let keepAliveTimer = null;

// Audio SFX Synthesizer
let audioCtx = null;
function getAudioContext() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    return audioCtx;
}

function playSuccessSfx() {
    try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        
        osc.type = 'sine';
        osc.frequency.setValueAtTime(523.25, now);
        osc.frequency.exponentialRampToValueAtTime(659.25, now + 0.1);
        osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.2);
        
        gain.gain.setValueAtTime(0.18, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
        
        osc.start(now);
        osc.stop(now + 0.35);
    } catch(e) {}
}

function playErrorSfx() {
    try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.exponentialRampToValueAtTime(146.83, now + 0.2);
        
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
        
        osc.start(now);
        osc.stop(now + 0.25);
    } catch(e) {}
}

function playClickSfx() {
    try {
        const ctx = getAudioContext();
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(440, now);
        osc.frequency.exponentialRampToValueAtTime(880, now + 0.05);
        
        gain.gain.setValueAtTime(0.12, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.06);
        
        osc.start(now);
        osc.stop(now + 0.06);
    } catch(e) {}
}

// ============================================================================
// Indian English Male Teacher Voice Engine
// ============================================================================
function selectIndianMaleVoice(voices) {
    if (!voices || voices.length === 0) return null;
    
    const femaleTerms = ['female', 'woman', 'girl', 'zira', 'jenny', 'aria', 'samantha', 'priya', 'swara', 'veena', 'neerja', 'heera', 'kavya'];
    const malePreferred = ['microsoft prabhat', 'rishi', 'microsoft ravi', 'pradeep', 'madhav', 'karan', 'mohan', 'google uk english male', 'microsoft david', 'microsoft mark', 'alex'];
    
    for (const pref of malePreferred) {
        const found = voices.find(v => {
            const name = v.name.toLowerCase();
            const lang = v.lang.toLowerCase();
            const isFemale = femaleTerms.some(f => name.includes(f));
            return !isFemale && (name.includes(pref) || (lang.includes('en-in') && name.includes(pref)));
        });
        if (found) return found;
    }
    
    const anyIndian = voices.find(v => {
        const name = v.name.toLowerCase();
        const lang = v.lang.toLowerCase();
        const isFemale = femaleTerms.some(f => name.includes(f));
        return !isFemale && lang.includes('en-in');
    });
    if (anyIndian) return anyIndian;
    
    const fallback = voices.find(v => {
        const name = v.name.toLowerCase();
        const lang = v.lang.toLowerCase();
        const isFemale = femaleTerms.some(f => name.includes(f));
        return !isFemale && lang.startsWith('en');
    });
    return fallback || voices[0];
}

function playAudioLecture() {
    if (!('speechSynthesis' in window)) {
        alert('Web Speech API is not supported in this browser.');
        return;
    }
    
    if (isSpeaking) {
        stopAudioLecture();
        return;
    }
    
    const slide = SLIDES.find(s => s.id === currentSlide);
    if (!slide || !slide.speech || slide.speech.trim() === '') {
        return;
    }
    
    window.speechSynthesis.cancel();
    clearInterval(keepAliveTimer);
    
    currentUtterance = new SpeechSynthesisUtterance(slide.speech);
    currentUtterance.pitch = 0.85;
    currentUtterance.rate = 0.94;
    
    const voices = window.speechSynthesis.getVoices();
    const chosenVoice = selectIndianMaleVoice(voices);
    if (chosenVoice) {
        currentUtterance.voice = chosenVoice;
    }
    
    keepAliveTimer = setInterval(() => {
        if (window.speechSynthesis.speaking) {
            window.speechSynthesis.pause();
            window.speechSynthesis.resume();
        } else {
            clearInterval(keepAliveTimer);
        }
    }, 10000);
    
    currentUtterance.onstart = () => {
        isSpeaking = true;
        updateAudioButtonUI(true);
    };
    
    currentUtterance.onend = () => {
        isSpeaking = false;
        clearInterval(keepAliveTimer);
        updateAudioButtonUI(false);
    };
    
    currentUtterance.onerror = () => {
        isSpeaking = false;
        clearInterval(keepAliveTimer);
        updateAudioButtonUI(false);
    };
    
    window.speechSynthesis.speak(currentUtterance);
}

function stopAudioLecture() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
    clearInterval(keepAliveTimer);
    isSpeaking = false;
    updateAudioButtonUI(false);
}

function updateAudioButtonUI(playing) {
    const btn = document.getElementById('audioLectureBtn');
    if (!btn) return;
    if (playing) {
        btn.classList.add('bg-rose-600', 'text-white', 'animate-pulse');
        btn.classList.remove('bg-emerald-600');
        btn.innerHTML = `
            <svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8 7a1 1 0 00-1 1v4a1 1 0 001 1h4a1 1 0 001-1V8a1 1 0 00-1-1H8z" clip-rule="evenodd"></path></svg>
            Stop Audio
        `;
    } else {
        btn.classList.remove('bg-rose-600', 'animate-pulse');
        btn.classList.add('bg-emerald-600', 'text-white');
        btn.innerHTML = `
            <svg class="w-4 h-4 mr-1.5" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd"></path></svg>
            Audio Lecture
        `;
    }
}

// ============================================================================
// Slide Navigation & Terminal Slide Invariant
// ============================================================================
function showSlide(num) {
    if (num < 1 || num > totalSlides) return;
    stopAudioLecture();
    
    document.querySelectorAll('.slide-pane').forEach(el => el.classList.add('hidden'));
    
    const target = document.getElementById(`slide-${num}`);
    if (target) {
        target.classList.remove('hidden');
    }
    
    currentSlide = num;
    const curNumEl = document.getElementById('currentSlideNum');
    if (curNumEl) curNumEl.innerText = currentSlide;
    
    const progressPct = (currentSlide / totalSlides) * 100;
    const pbar = document.getElementById('chapterProgressBar');
    if (pbar) pbar.style.width = `${progressPct}%`;
    
    const prevBtn = document.getElementById('prevBtn');
    if (prevBtn) {
        if (currentSlide === 1) {
            prevBtn.classList.add('opacity-40', 'cursor-not-allowed');
            prevBtn.disabled = true;
        } else {
            prevBtn.classList.remove('opacity-40', 'cursor-not-allowed');
            prevBtn.disabled = false;
        }
    }
    
    // Terminal Slide Invariant (Strict Rule for Slide 20)
    const nextBtn = document.getElementById('nextBtn');
    const lastNotice = document.getElementById('lastSlideNotice');
    
    if (currentSlide === 20) {
        if (nextBtn) nextBtn.style.display = 'none';
        if (lastNotice) lastNotice.classList.remove('hidden');
    } else {
        if (nextBtn) nextBtn.style.display = 'flex';
        if (lastNotice) lastNotice.classList.add('hidden');
    }
    
    // Hide audio button on challenge slides (17-20)
    const audioBtn = document.getElementById('audioLectureBtn');
    if (audioBtn) {
        if (currentSlide >= 17) {
            audioBtn.classList.add('hidden');
        } else {
            audioBtn.classList.remove('hidden');
        }
    }
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
    initSimulatorForSlide(currentSlide);
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        playClickSfx();
        showSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        playClickSfx();
        showSlide(currentSlide - 1);
    }
}

// ============================================================================
// Checkpoint & Quiz Validation
// ============================================================================
function checkCheckpoint(slideId, cpIdx, optIdx) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.checkpoints || !slide.checkpoints[cpIdx]) return;
    
    const cp = slide.checkpoints[cpIdx];
    const fb = document.getElementById(`cp-fb-${slideId}-${cpIdx}`);
    const btns = document.querySelectorAll(`.cp-btn-${slideId}-${cpIdx}`);
    if (!fb || !btns) return;
    
    const correctIdx = cp.ans;
    
    btns.forEach((btn, idx) => {
        btn.classList.remove('bg-emerald-600', 'bg-rose-600', 'text-white', 'border-emerald-500', 'border-rose-500');
        if (idx === correctIdx) {
            btn.classList.add('bg-emerald-600/30', 'border-emerald-500/60', 'text-emerald-200');
        }
    });
    
    if (optIdx === correctIdx) {
        playSuccessSfx();
        fb.className = 'text-xs p-3 rounded-xl bg-emerald-950/60 border border-emerald-800 text-emerald-200 font-medium block animate-fadeIn';
        fb.innerHTML = `<strong>Correct!</strong> ${cp.exp}`;
    } else {
        playErrorSfx();
        if (btns[optIdx]) {
            btns[optIdx].classList.add('bg-rose-600/30', 'border-rose-500/60', 'text-rose-200');
        }
        fb.className = 'text-xs p-3 rounded-xl bg-rose-950/60 border border-rose-800 text-rose-200 font-medium block animate-fadeIn';
        fb.innerHTML = `<strong>Not quite.</strong> ${cp.exp}`;
    }
}

function checkQuiz(slideId, qIdx, optIdx) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.quizzes || !slide.quizzes[qIdx]) return;
    
    const qz = slide.quizzes[qIdx];
    const fb = document.getElementById(`qz-fb-${slideId}-${qIdx}`);
    const solBtn = document.getElementById(`qz-sol-btn-${slideId}-${qIdx}`);
    const btns = document.querySelectorAll(`.qz-btn-${slideId}-${qIdx}`);
    if (!fb || !btns) return;
    
    const correctIdx = qz.ans;
    
    btns.forEach((btn, idx) => {
        btn.classList.remove('bg-emerald-600', 'bg-rose-600', 'text-white', 'border-emerald-500', 'border-rose-500');
        if (idx === correctIdx) {
            btn.classList.add('bg-emerald-600/30', 'border-emerald-500/60', 'text-emerald-200');
        }
    });
    
    if (optIdx === correctIdx) {
        playSuccessSfx();
        fb.className = 'text-xs p-3 rounded-xl bg-emerald-950/60 border border-emerald-800 text-emerald-200 font-medium block animate-fadeIn';
        fb.innerHTML = `<strong>Correct!</strong> ${qz.exp}`;
    } else {
        playErrorSfx();
        if (btns[optIdx]) {
            btns[optIdx].classList.add('bg-rose-600/30', 'border-rose-500/60', 'text-rose-200');
        }
        fb.className = 'text-xs p-3 rounded-xl bg-rose-950/60 border border-rose-800 text-rose-200 font-medium block animate-fadeIn';
        fb.innerHTML = `<strong>Not quite.</strong> ${qz.exp}`;
    }
    
    if (solBtn) {
        solBtn.classList.remove('hidden');
    }
}

function showSolutionModal(slideId, qIdx) {
    const slide = SLIDES.find(s => s.id === slideId);
    if (!slide || !slide.quizzes || !slide.quizzes[qIdx]) return;
    
    const qz = slide.quizzes[qIdx];
    const modal = document.getElementById('solutionModal');
    const title = document.getElementById('modalQuestionTitle');
    const content = document.getElementById('modalSolutionContent');
    
    if (modal && title && content) {
        playClickSfx();
        title.innerText = `Question ${qIdx + 1}: ${qz.q}`;
        content.innerHTML = qz.sol;
        modal.classList.remove('hidden');
    }
}

function closeSolutionModal() {
    const modal = document.getElementById('solutionModal');
    if (modal) {
        modal.classList.add('hidden');
    }
}

function toggleHint(slideId, qIdx) {
    const hintEl = document.getElementById(`qz-hint-${slideId}-${qIdx}`);
    if (hintEl) {
        playClickSfx();
        hintEl.classList.toggle('hidden');
    }
}

// ============================================================================
// SIMULATOR 1: Village Community Explorer
// ============================================================================
function selectVillageLandmark(landmark) {
    playClickSfx();
    ['banyan', 'ground', 'well', 'chopal'].forEach(l => {
        const btn = document.getElementById(`vce-btn-${l}`);
        if (btn) {
            if (l === landmark) {
                btn.className = 'p-2.5 rounded-xl border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold ring-2 ring-emerald-500 transition-all flex flex-col items-center gap-1';
            } else {
                btn.className = 'p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium transition-all flex flex-col items-center gap-1';
            }
        }
    });
    
    const vBox = document.getElementById('vce-visual-box');
    const iBox = document.getElementById('vce-info-box');
    if (!vBox || !iBox) return;
    
    if (landmark === 'banyan') {
        vBox.innerHTML = `
            <svg class="w-32 h-24" viewBox="0 0 140 100">
                <path d="M60 90 L60 50 Q70 20 100 20 Q130 20 120 50 Q100 70 80 90 Z" fill="#15803d"/>
                <path d="M40 90 L40 50 Q50 20 20 20 Q0 20 10 50 Q30 70 40 90 Z" fill="#16a34a"/>
                <path d="M50 90 L50 40 Q70 10 70 0 Q90 10 90 40 L90 90 Z" fill="#14532d"/>
                <rect x="62" y="45" width="16" height="45" fill="#78350f" rx="3"/>
                <line x1="50" y1="40" x2="48" y2="85" stroke="#92400e" stroke-width="2"/>
                <line x1="90" y1="40" x2="92" y2="85" stroke="#92400e" stroke-width="2"/>
            </svg>
        `;
        iBox.innerHTML = '<strong class="text-emerald-400">The Grand Banyan Tree:</strong> Features vast spreading branches and aerial roots where elders congregate daily for councils, sharing wisdom, and discussing village welfare.';
    } else if (landmark === 'ground') {
        vBox.innerHTML = `
            <svg class="w-32 h-24" viewBox="0 0 140 100">
                <rect x="10" y="20" width="120" height="60" rx="8" fill="#047857" stroke="#10b981" stroke-width="2"/>
                <line x1="70" y1="20" x2="70" y2="80" stroke="#ffffff" stroke-width="1.5" stroke-dasharray="3 3"/>
                <circle cx="40" cy="50" r="8" fill="#3b82f6"/>
                <circle cx="100" cy="50" r="8" fill="#ef4444"/>
            </svg>
        `;
        iBox.innerHTML = '<strong class="text-emerald-400">Village Playground:</strong> Open recreational area where youth play kabaddi and kho-kho, fostering team coordination, agility, and mutual trust.';
    } else if (landmark === 'well') {
        vBox.innerHTML = `
            <svg class="w-32 h-24" viewBox="0 0 140 100">
                <ellipse cx="70" cy="70" rx="35" ry="15" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
                <rect x="45" y="30" width="6" height="40" fill="#78350f"/>
                <rect x="89" y="30" width="6" height="40" fill="#78350f"/>
                <line x1="45" y1="30" x2="95" y2="30" stroke="#78350f" stroke-width="4"/>
                <circle cx="70" cy="30" r="5" fill="#e2e8f0"/>
            </svg>
        `;
        iBox.innerHTML = '<strong class="text-emerald-400">Community Water Well:</strong> Traditional freshwater source where neighbors meet, share daily greetings, and collect clean water.';
    } else if (landmark === 'chopal') {
        vBox.innerHTML = `
            <svg class="w-32 h-24" viewBox="0 0 140 100">
                <polygon points="70,15 15,40 125,40" fill="#b45309"/>
                <rect x="25" y="40" width="90" height="45" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
                <rect x="55" y="55" width="30" height="30" fill="#78350f"/>
            </svg>
        `;
        iBox.innerHTML = '<strong class="text-emerald-400">Panchayat Chopal:</strong> The community council center where village leaders organize development drives, resolve civic concerns, and distribute welfare supplies.';
    }
}

// ============================================================================
// SIMULATOR 2: Community Services Matcher
// ============================================================================
function selectServiceCard(service) {
    playClickSfx();
    ['health', 'police', 'school', 'grocery'].forEach(s => {
        const btn = document.getElementById(`srv-btn-${s}`);
        if (btn) {
            if (s === service) {
                btn.className = 'p-3 rounded-xl border border-cyan-500 bg-cyan-950/40 text-left hover:bg-cyan-900/30 transition-all flex items-start gap-2.5 ring-2 ring-cyan-500';
            } else {
                btn.className = 'p-3 rounded-xl border border-slate-700 bg-slate-800 text-left hover:bg-slate-700 transition-all flex items-start gap-2.5';
            }
        }
    });
    
    const dBox = document.getElementById('srv-detail-box');
    if (!dBox) return;
    
    if (service === 'health') {
        dBox.innerHTML = '<strong>Primary Health Center:</strong> Delivers essential medical care, preventive vaccinations, infant care, and first-aid for farm injuries.';
    } else if (service === 'police') {
        dBox.innerHTML = '<strong>Police Post:</strong> Upholds community peace, enforces traffic safety on rural highways, and safeguards homes from crime.';
    } else if (service === 'school') {
        dBox.innerHTML = '<strong>Primary School:</strong> Educates neighborhood children, provides nutritious mid-day meals, and instills civic values and scientific inquiry.';
    } else if (service === 'grocery') {
        dBox.innerHTML = '<strong>Local Grocery Store:</strong> Ensures reliable daily supply of grains, cooking oil, pulses, and milk, connecting rural farm output with family kitchens.';
    }
}

// ============================================================================
// SIMULATOR 3: Clean Park Stewardship
// ============================================================================
let cleanScore = 40;
const completedCleanActions = {};

function performCleanAction(action) {
    playClickSfx();
    if (completedCleanActions[action]) return;
    completedCleanActions[action] = true;
    
    cleanScore = Math.min(100, cleanScore + 20);
    const badge = document.getElementById('steward-score-badge');
    const pbar = document.getElementById('steward-progress-bar');
    const fbox = document.getElementById('steward-feedback-box');
    const btn = document.getElementById(`act-btn-${action}`);
    
    if (badge) badge.innerText = `${cleanScore}% Clean`;
    if (pbar) pbar.style.width = `${cleanScore}%`;
    if (btn) {
        btn.classList.add('bg-emerald-900/40', 'border-emerald-500', 'text-emerald-300');
        btn.disabled = true;
    }
    
    if (cleanScore === 100) {
        playSuccessSfx();
        if (fbox) fbox.innerHTML = '<span class="text-emerald-400 font-bold">🎉 Outstanding Civic Stewardship!</span> The park is completely clean, water taps are sealed, and benches are sanitary!';
    } else {
        if (fbox) fbox.innerHTML = `<span class="text-teal-300">Action completed: ${action}.</span> Keep going to reach 100% cleanliness!`;
    }
}

// ============================================================================
// SIMULATOR 4: Van Mahotsav Species Guide
// ============================================================================
const TREE_DATA = {
    neem: {
        avatar: '🌿',
        name: 'Neem (Azadirachta indica)',
        desc: 'The village pharmacy. Deep roots bind soil, leaves act as natural antibacterial medicine and pest repellent, cleans air pollutants.'
    },
    peepal: {
        avatar: '🍃',
        name: 'Sacred Peepal (Ficus religiosa)',
        desc: 'Releases rich oxygen day and night, provides vast canopy shade for birds, and supports hundreds of beneficial insect species.'
    },
    banyan: {
        avatar: '🌳',
        name: 'Banyan (Ficus benghalensis)',
        desc: 'National tree of India. Expansive aerial prop roots create a vast living shelter that cools the neighborhood and shelters wildlife.'
    },
    gulmohar: {
        avatar: '🌺',
        name: 'Gulmohar (Delonix regia)',
        desc: 'Vibrant flame-red flowers attract honeybees and butterflies, beautifying public parks and highway avenues.'
    },
    amaltas: {
        avatar: '🌼',
        name: 'Golden Shower (Cassia fistula)',
        desc: 'Drapes parks in hanging golden yellow blossoms, supports native pollinators, and thrives in harsh summer heat.'
    },
    jamun: {
        avatar: '🍇',
        name: 'Jamun (Syzygium cumini)',
        desc: 'Nutritious purple fruits feed children and songbirds; strong roots resist heavy monsoon flood currents along riverbanks.'
    }
};

function selectTreeSpecies(tree) {
    playClickSfx();
    ['neem', 'peepal', 'banyan', 'gulmohar', 'amaltas', 'jamun'].forEach(t => {
        const btn = document.getElementById(`tree-btn-${t}`);
        if (btn) {
            if (t === tree) {
                btn.className = 'p-2.5 rounded-xl border border-green-500 bg-green-950/40 text-green-300 font-bold ring-2 ring-green-500';
            } else {
                btn.className = 'p-2.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium';
            }
        }
    });
    
    const tData = TREE_DATA[tree];
    const av = document.getElementById('tree-avatar');
    const nm = document.getElementById('tree-name');
    const dc = document.getElementById('tree-desc');
    
    if (av) av.innerText = tData.avatar;
    if (nm) nm.innerText = tData.name;
    if (dc) dc.innerText = tData.desc;
}

// ============================================================================
// SIMULATOR 5: Community Poster Designer
// ============================================================================
function updateCommunityPoster() {
    playClickSfx();
    const sVal = document.getElementById('poster-slogan-sel')?.value || 's1';
    const aVal = document.getElementById('poster-art-sel')?.value || 'trees';
    const canvas = document.getElementById('poster-canvas');
    if (!canvas) return;
    
    const slogans = {
        s1: 'Plant a Sapling Today, Gift a Green Tomorrow!',
        s2: 'Clean Park, Joyful Neighborhood, Healthy Life!',
        s3: 'Our Hands, Our Trees, Our Living Community!'
    };
    
    const arts = {
        trees: '🌱 🌳 🚿',
        hands: '🤝 🌍 🌿',
        park: '🪑 🏃 🌺'
    };
    
    canvas.innerHTML = `
        <div class="text-[10px] font-bold uppercase tracking-wider text-emerald-400 border-b border-emerald-800/60 pb-1">
            Van Mahotsav Community Drive
        </div>
        <h4 class="text-sm font-extrabold text-white leading-snug">${slogans[sVal]}</h4>
        <div class="text-3xl py-2 tracking-widest">${arts[aVal]}</div>
        <div class="text-[11px] text-emerald-200 bg-emerald-950/60 p-2 rounded-lg border border-emerald-800/40">
            <strong>When:</strong> Sunday, 8:00 AM | <strong>Where:</strong> Village Banyan Park<br>
            <em>All residents, children, and elders warmly welcome!</em>
        </div>
    `;
}

// ============================================================================
// SIMULATOR 6: Shramdaan Repair Workshop
// ============================================================================
function triggerRepairTask(task) {
    playClickSfx();
    const logBox = document.getElementById('shramdaan-log-box');
    if (!logBox) return;
    
    if (task === 'bench') {
        playSuccessSfx();
        logBox.innerHTML = '<span class="text-amber-400 font-bold">Carpenter Action:</span> Measured seasoned teak planks, hammered new iron nails, and sanded smooth the cracked park bench for village elders.';
    } else if (task === 'light') {
        playSuccessSfx();
        logBox.innerHTML = '<span class="text-yellow-400 font-bold">Electrician Action:</span> Safely replaced faulty wiring, sealed junctions against monsoon rain, and installed bright energy-saving LED streetlamps.';
    } else if (task === 'nursery') {
        playSuccessSfx();
        logBox.innerHTML = '<span class="text-emerald-400 font-bold">Gardener Action:</span> Selected 50 disease-free indigenous neem and gulmohar saplings from the government nursery and loaded them onto the transport trolley.';
    } else if (task === 'guard') {
        playSuccessSfx();
        logBox.innerHTML = '<span class="text-cyan-400 font-bold">Youth Volunteers Action:</span> Wove sturdy lattice bamboo tree guards to surround and shield tender saplings from wandering goats and stray cattle.';
    }
}

// ============================================================================
// SIMULATOR 7: Professional Tool Kit Explorer
// ============================================================================
const TOOLKIT_DATA = {
    mason: {
        title: 'Mason (Raj Mistri)',
        tools: [
            { name: 'Steel Trowel', icon: '🧱', desc: 'Scoops and spreads cement mortar evenly between brick courses.' },
            { name: 'Plumb Line', icon: '⚓', desc: 'Uses gravity to verify that brick walls are perfectly upright and vertical.' },
            { name: 'Spirit Level', icon: '📏', desc: 'Air bubble indicator checks horizontal flatness of foundations and window sills.' }
        ]
    },
    carpenter: {
        title: 'Carpenter (Badhai)',
        tools: [
            { name: 'Handsaw', icon: '🪚', desc: 'Cuts timber planks to precise dimensions for doors, benches, and roof trusses.' },
            { name: 'Wood Chisel', icon: '📐', desc: 'Carves clean mortise-and-tenon interlocking joints in wooden beams.' },
            { name: 'Wooden Mallet', icon: '🔨', desc: 'Drives chisels and tightens wooden dowels without splitting delicate grain.' }
        ]
    },
    plumber: {
        title: 'Plumber (Nal Saaz)',
        tools: [
            { name: 'Pipe Wrench', icon: '🔧', desc: 'Adjustable serrated jaws grip and turn threaded galvanized water pipes.' },
            { name: 'Teflon Seal Tape', icon: '🩹', desc: 'Seals pipe joints watertight to prevent drinking water leakage.' },
            { name: 'Pipe Cutter', icon: '⚙️', desc: 'Cuts metal and PVC conduit cleanly without leaving ragged metal burrs.' }
        ]
    },
    electrician: {
        title: 'Electrician (Bijli Mistri)',
        tools: [
            { name: 'Insulated Pliers', icon: '⚡', desc: 'Rubber-coated handles protect against electric shock while bending wires.' },
            { name: 'Neon Voltage Tester', icon: '💡', desc: 'Glows to detect live electrical currents before undertaking repairs.' },
            { name: 'Wire Stripper', icon: '✂️', desc: 'Peeled plastic insulation cleanly exposes copper conductors.' }
        ]
    }
};

function selectTradeToolKit(trade) {
    playClickSfx();
    ['mason', 'carpenter', 'plumber', 'electrician'].forEach(t => {
        const btn = document.getElementById(`trade-tab-${t}`);
        if (btn) {
            if (t === trade) {
                btn.className = 'px-3 py-1.5 rounded-lg border border-blue-500 bg-blue-950/40 text-blue-300 font-bold ring-2 ring-blue-500';
            } else {
                btn.className = 'px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium';
            }
        }
    });
    
    const tData = TOOLKIT_DATA[trade];
    const box = document.getElementById('toolkit-display-box');
    if (!box) return;
    
    let html = `<h4 class="text-xs font-bold text-blue-400 uppercase tracking-wider mb-2">${tData.title} Tool Kit</h4><div class="grid grid-cols-1 sm:grid-cols-3 gap-2">`;
    tData.tools.forEach(tool => {
        html += `
            <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1">
                <div class="flex items-center gap-1.5 font-bold text-white text-xs">
                    <span class="text-base">${tool.icon}</span> ${tool.name}
                </div>
                <p class="text-[11px] text-slate-300 leading-normal">${tool.desc}</p>
            </div>
        `;
    });
    html += '</div>';
    box.innerHTML = html;
}

// ============================================================================
// SIMULATOR 8: Step-by-Step Tree Planting
// ============================================================================
function goToPlantStep(step) {
    playClickSfx();
    [1, 2, 3, 4].forEach(s => {
        const btn = document.getElementById(`plant-step-${s}`);
        if (btn) {
            if (s === step) {
                btn.className = 'p-2 rounded-lg border border-lime-500 bg-lime-950/40 text-lime-300 font-bold ring-2 ring-lime-500 text-center';
            } else {
                btn.className = 'p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium text-center';
            }
        }
    });
    
    const svg = document.getElementById('plant-stage-svg');
    const desc = document.getElementById('plant-step-desc');
    if (!svg || !desc) return;
    
    if (step === 1) {
        svg.innerHTML = `
            <rect x="20" y="70" width="240" height="20" fill="#78350f" rx="4"/>
            <path d="M50 70 L60 55 L70 70" stroke="#f59e0b" stroke-width="2" fill="none"/>
            <circle cx="140" cy="65" r="4" fill="#94a3b8"/>
            <circle cx="180" cy="66" r="3" fill="#94a3b8"/>
        `;
        desc.innerText = 'Step 1: Volunteers clear stones, thorny weeds, and plastic litter from the designated planting bed.';
    } else if (step === 2) {
        svg.innerHTML = `
            <rect x="20" y="70" width="240" height="20" fill="#78350f" rx="4"/>
            <polygon points="110,70 170,70 160,95 120,95" fill="#451a03"/>
            <circle cx="135" cy="85" r="3" fill="#15803d"/>
            <circle cx="145" cy="88" r="3" fill="#15803d"/>
        `;
        desc.innerText = 'Step 2: Dig a pit 60 cm deep and 60 cm wide, loosening hard subsoil and blending with dark organic compost.';
    } else if (step === 3) {
        svg.innerHTML = `
            <rect x="20" y="70" width="240" height="20" fill="#78350f" rx="4"/>
            <polygon points="110,70 170,70 160,95 120,95" fill="#451a03"/>
            <rect x="138" y="45" width="4" height="35" fill="#166534"/>
            <ellipse cx="140" cy="40" rx="12" ry="16" fill="#22c55e"/>
        `;
        desc.innerText = 'Step 3: Peel off the plastic nursery bag and position the sapling upright, backfilling gently with nutrient-rich topsoil.';
    } else if (step === 4) {
        playSuccessSfx();
        svg.innerHTML = `
            <rect x="20" y="70" width="240" height="20" fill="#78350f" rx="4"/>
            <rect x="138" y="35" width="4" height="45" fill="#166534"/>
            <ellipse cx="140" cy="30" rx="16" ry="20" fill="#15803d"/>
            <!-- Bamboo tree guard -->
            <line x1="122" y1="25" x2="122" y2="75" stroke="#eab308" stroke-width="2"/>
            <line x1="158" y1="25" x2="158" y2="75" stroke="#eab308" stroke-width="2"/>
            <line x1="120" y1="35" x2="160" y2="35" stroke="#ca8a04" stroke-width="1.5"/>
            <line x1="120" y1="50" x2="160" y2="50" stroke="#ca8a04" stroke-width="1.5"/>
            <line x1="120" y1="65" x2="160" y2="65" stroke="#ca8a04" stroke-width="1.5"/>
        `;
        desc.innerText = 'Step 4: Water thoroughly to settle soil, and enclose the sapling in a protective bamboo guard to shield from grazing animals.';
    }
}

// ============================================================================
// SIMULATOR 9: Kanker Bamboo Bridge Simulator
// ============================================================================
function setBridgeTimeline(hours) {
    playClickSfx();
    [0, 12, 24, 48].forEach(h => {
        const btn = document.getElementById(`bridge-btn-${h}`);
        if (btn) {
            if (h === hours) {
                btn.className = 'p-2 rounded-lg border border-sky-500 bg-sky-950/40 text-sky-300 font-bold ring-2 ring-sky-500 text-center';
            } else {
                btn.className = 'p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium text-center';
            }
        }
    });
    
    const svg = document.getElementById('bridge-scene-svg');
    const desc = document.getElementById('bridge-log-desc');
    if (!svg || !desc) return;
    
    if (hours === 0) {
        svg.innerHTML = `
            <rect x="0" y="40" width="300" height="60" fill="#0284c7"/>
            <path d="M0 50 Q75 40 150 50 T300 50" stroke="#38bdf8" stroke-width="3" fill="none"/>
            <rect x="0" y="70" width="50" height="30" fill="#78350f"/>
            <rect x="250" y="70" width="50" height="30" fill="#78350f"/>
        `;
        desc.innerText = 'Hour 0: Monsoon torrents submerge the low culvert along the Chinar river, cutting off food and healthcare for 1,000 villagers.';
    } else if (hours === 12) {
        svg.innerHTML = `
            <rect x="0" y="40" width="300" height="60" fill="#0284c7"/>
            <rect x="0" y="70" width="50" height="30" fill="#78350f"/>
            <rect x="250" y="70" width="50" height="30" fill="#78350f"/>
            <line x1="20" y1="70" x2="40" y2="40" stroke="#eab308" stroke-width="3"/>
            <line x1="260" y1="70" x2="280" y2="40" stroke="#eab308" stroke-width="3"/>
            <circle cx="30" cy="72" r="5" fill="#64748b"/>
        `;
        desc.innerText = 'Hour 12: Villagers mobilize! Farmers donate hundreds of thick bamboo poles while youth haul heavy river boulders for anchor weights.';
    } else if (hours === 24) {
        svg.innerHTML = `
            <rect x="0" y="40" width="300" height="60" fill="#0284c7"/>
            <rect x="0" y="70" width="50" height="30" fill="#78350f"/>
            <rect x="250" y="70" width="50" height="30" fill="#78350f"/>
            <!-- Pillars anchored -->
            <polygon points="90,40 100,40 105,80 85,80" fill="#64748b"/>
            <polygon points="190,40 200,40 205,80 185,80" fill="#64748b"/>
            <line x1="45" y1="40" x2="255" y2="40" stroke="#ca8a04" stroke-width="2" stroke-dasharray="4 2"/>
        `;
        desc.innerText = 'Hour 24: Working day and night, teams sink stone-filled bamboo cribs into the riverbed to anchor stable foundation piers against strong currents.';
    } else if (hours === 48) {
        playSuccessSfx();
        svg.innerHTML = `
            <rect x="0" y="40" width="300" height="60" fill="#0284c7"/>
            <rect x="0" y="70" width="50" height="30" fill="#78350f"/>
            <rect x="250" y="70" width="50" height="30" fill="#78350f"/>
            <polygon points="90,40 100,40 105,80 85,80" fill="#64748b"/>
            <polygon points="190,40 200,40 205,80 185,80" fill="#64748b"/>
            <!-- Sturdy pedestrian bridge -->
            <rect x="40" y="32" width="220" height="6" fill="#eab308" rx="2"/>
            <line x1="40" y1="24" x2="260" y2="24" stroke="#ca8a04" stroke-width="2"/>
            <line x1="70" y1="24" x2="70" y2="34" stroke="#ca8a04" stroke-width="1.5"/>
            <line x1="150" y1="24" x2="150" y2="34" stroke="#ca8a04" stroke-width="1.5"/>
            <line x1="230" y1="24" x2="230" y2="34" stroke="#ca8a04" stroke-width="1.5"/>
            <circle cx="150" cy="20" r="4" fill="#ffffff"/>
        `;
        desc.innerText = 'Hour 48: The 60-foot bamboo-and-stone pedestrian bridge is complete! Over 1,000 citizens cross safely to schools, clinics, and markets.';
    }
}

// ============================================================================
// SIMULATOR 10: Teamwork in Nature (Insects)
// ============================================================================
function selectInsectColony(type) {
    playClickSfx();
    const btnAnt = document.getElementById('insect-tab-ant');
    const btnBee = document.getElementById('insect-tab-bee');
    const box = document.getElementById('colony-display-box');
    if (!box) return;
    
    if (type === 'ant') {
        if (btnAnt) btnAnt.className = 'px-4 py-1.5 rounded-lg border border-indigo-500 bg-indigo-950/40 text-indigo-300 font-bold ring-2 ring-indigo-500 text-xs';
        if (btnBee) btnBee.className = 'px-4 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium text-xs';
        box.innerHTML = `
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1">
                    <span class="text-xl block">👑</span>
                    <span class="font-bold text-amber-400 block">Queen Ant</span>
                    <span class="text-[10px] text-slate-400">Lays thousands of eggs</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1">
                    <span class="text-xl block">🌾</span>
                    <span class="font-bold text-emerald-400 block">Foragers</span>
                    <span class="text-[10px] text-slate-400">Leave pheromone trails</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1">
                    <span class="text-xl block">🛡️</span>
                    <span class="font-bold text-rose-400 block">Soldier Ants</span>
                    <span class="text-[10px] text-slate-400">Guard tunnel entrances</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1">
                    <span class="text-xl block">🍼</span>
                    <span class="font-bold text-cyan-400 block">Nursery Ants</span>
                    <span class="text-[10px] text-slate-400">Feed & groom larvae</span>
                </div>
            </div>
            <p class="text-xs text-indigo-300 text-center">Division of labor ensures all essential colony duties happen continuously without centralized supervision.</p>
        `;
    } else {
        if (btnBee) btnBee.className = 'px-4 py-1.5 rounded-lg border border-indigo-500 bg-indigo-950/40 text-indigo-300 font-bold ring-2 ring-indigo-500 text-xs';
        if (btnAnt) btnAnt.className = 'px-4 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium text-xs';
        box.innerHTML = `
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center text-xs">
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1">
                    <span class="text-xl block">👑</span>
                    <span class="font-bold text-yellow-400 block">Queen Bee</span>
                    <span class="text-[10px] text-slate-400">Lays up to 2,000 eggs/day</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1">
                    <span class="text-xl block">💃</span>
                    <span class="font-bold text-amber-400 block">Scout Bees</span>
                    <span class="text-[10px] text-slate-400">Dance waggle communication</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1">
                    <span class="text-xl block">🏗️</span>
                    <span class="font-bold text-green-400 block">Wax Builders</span>
                    <span class="text-[10px] text-slate-400">Hexagonal honeycomb cells</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 space-y-1">
                    <span class="text-xl block">🌬️</span>
                    <span class="font-bold text-sky-400 block">Fan Ventilators</span>
                    <span class="text-[10px] text-slate-400">Cool hive with wings</span>
                </div>
            </div>
            <p class="text-xs text-yellow-300 text-center">Honeybees communicate food direction and distance using symbolic figure-eight waggle dances.</p>
        `;
    }
}

// ============================================================================
// SIMULATOR 11: Communal Feast Organizer
// ============================================================================
const feastMenu = { rice: true, dal: true, veg: true, lassi: true };

function toggleFeastItem(item) {
    playClickSfx();
    feastMenu[item] = !feastMenu[item];
    const btn = document.getElementById(`feast-btn-${item}`);
    if (btn) {
        if (feastMenu[item]) {
            btn.className = 'p-2 rounded-lg border border-emerald-500 bg-emerald-950/40 text-emerald-300 font-bold';
        } else {
            btn.className = 'p-2 rounded-lg border border-slate-800 bg-slate-900 text-slate-500 font-normal';
        }
    }
    
    const plate = document.getElementById('banana-leaf-plate');
    if (!plate) return;
    
    let icons = '';
    if (feastMenu.rice) icons += '<span>🍚</span>';
    if (feastMenu.dal) icons += '<span>🥣</span>';
    if (feastMenu.veg) icons += '<span>🥗</span>';
    if (feastMenu.lassi) icons += '<span>🥛</span>';
    plate.innerHTML = icons || '<span class="text-xs text-emerald-200">Empty Plate</span>';
}

// ============================================================================
// SIMULATOR 12: Organic Compost Decomposer
// ============================================================================
function updateCompostStage(week) {
    const w = parseInt(week, 10);
    const badge = document.getElementById('compost-week-badge');
    const vBox = document.getElementById('compost-visual-box');
    const desc = document.getElementById('compost-stage-desc');
    
    if (badge) badge.innerText = `Week ${w}: ${w <= 2 ? 'Raw Green Matter' : w <= 5 ? 'Active Decomposition' : 'Mature Organic Humus'}`;
    
    if (vBox) {
        if (w <= 2) {
            vBox.style.backgroundColor = '#166534';
            vBox.innerHTML = '<span class="text-xs text-green-200 font-bold text-center block">Green Leaves & Scraps Layer</span>';
        } else if (w <= 5) {
            vBox.style.backgroundColor = '#78350f';
            vBox.innerHTML = '<span class="text-xs text-amber-200 font-bold text-center block">Decomposing Biomass (Warm: 55°C)</span>';
        } else {
            vBox.style.backgroundColor = '#1c1917';
            vBox.innerHTML = '<span class="text-xs text-emerald-400 font-bold text-center block">✨ Dark Rich Humus (Ready Manure)</span>';
        }
    }
    
    if (desc) {
        if (w <= 2) {
            desc.innerText = 'Week 1-2: Fresh used banana leaves and vegetable scraps layered with dry brown leaves and microbial soil slurry.';
        } else if (w <= 5) {
            desc.innerText = 'Week 3-5: Bacteria and earthworms actively digest cellulose; the compost pile warms up as organic matter breaks down.';
        } else {
            desc.innerText = 'Week 6-8: Complete aerobic transformation! Discarded leaves have turned into nutrient-rich humus ready for tree roots.';
        }
    }
}

// ============================================================================
// SIMULATOR 13: Regional Traditions Showcase
// ============================================================================
function selectRegionalTradition(region) {
    playClickSfx();
    const btnAssam = document.getElementById('trad-btn-assam');
    const btnSikkim = document.getElementById('trad-btn-sikkim');
    const box = document.getElementById('tradition-feature-box');
    if (!box) return;
    
    if (region === 'assam') {
        if (btnAssam) btnAssam.className = 'px-4 py-1.5 rounded-lg border border-purple-500 bg-purple-950/40 text-purple-300 font-bold ring-2 ring-purple-500 text-xs';
        if (btnSikkim) btnSikkim.className = 'px-4 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium text-xs';
        box.innerHTML = `
            <div class="flex items-center gap-3 p-3 bg-slate-900 rounded-xl border border-purple-900/40">
                <span class="text-3xl">🛖</span>
                <div>
                    <h4 class="font-bold text-white text-xs sm:text-sm">Bhela Ghar & Uruka Feast (Assam)</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">During Magh Bihu, communities gather in harvest fields to build temporary thatch-and-bamboo pavilions called Bhela Ghar, sharing grand community feasts before lighting the sacred meji bonfire at dawn.</p>
                </div>
            </div>
        `;
    } else {
        if (btnSikkim) btnSikkim.className = 'px-4 py-1.5 rounded-lg border border-purple-500 bg-purple-950/40 text-purple-300 font-bold ring-2 ring-purple-500 text-xs';
        if (btnAssam) btnAssam.className = 'px-4 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium text-xs';
        box.innerHTML = `
            <div class="flex items-center gap-3 p-3 bg-slate-900 rounded-xl border border-purple-900/40">
                <span class="text-3xl">🌾</span>
                <div>
                    <h4 class="font-bold text-white text-xs sm:text-sm">Khetala Mutual Farming (Sikkim)</h4>
                    <p class="text-xs text-slate-300 leading-relaxed">Himalayan terrace farmers operate reciprocal mutual assistance groups called Khetala, taking turns plowing, planting, and harvesting each other's steep terrace fields without paying cash wages.</p>
                </div>
            </div>
        `;
    }
}

// ============================================================================
// SIMULATOR 14: School Interdependence Matrix
// ============================================================================
const SCHOOL_ROLES = {
    teacher: 'Dedicated teachers ignite curiosity, guide scientific experiments, explain mathematics, and model moral empathy in classrooms.',
    student: 'Students actively learn, help peers solve complex problems, maintain classroom order, and care for campus gardens.',
    caretaker: 'Caretakers and sanitation workers sanitize washrooms, wash corridors, empty waste bins, and keep drinking water stations pristine.',
    driver: 'Bus drivers and conductors navigate morning roadway traffic with vigilance, transporting pupils safely and punctually.',
    guard: 'Security personnel monitor campus gates, welcome visitors, verify identities, and safeguard children from external risks.',
    principal: 'The principal provides administrative leadership, supports teacher development, and builds a joyful, disciplined learning environment.'
};

function selectSchoolRole(role) {
    playClickSfx();
    ['teacher', 'student', 'caretaker', 'driver', 'guard', 'principal'].forEach(r => {
        const btn = document.getElementById(`sch-btn-${r}`);
        if (btn) {
            if (r === role) {
                btn.className = 'p-2 rounded-lg border border-rose-500 bg-rose-950/40 text-rose-300 font-bold ring-2 ring-rose-500';
            } else {
                btn.className = 'p-2 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium';
            }
        }
    });
    
    const box = document.getElementById('school-role-box');
    if (box) box.innerHTML = `<strong>${role.toUpperCase()}:</strong> ${SCHOOL_ROLES[role]}`;
}

// ============================================================================
// SIMULATOR 15: Student Action Project Planner
// ============================================================================
const ACTION_PROJECTS = {
    clean: {
        title: 'Campus Cleanliness & Segregation Drive',
        tools: 'Green wet bins, Blue dry bins, Safety gloves, Rakes',
        steps: 'Survey corridors, position labeled twin bins, educate classmates on wet vs dry waste, and transfer food scraps to the school garden compost pit.',
        impact: 'Zero litter on campus, 100% organic waste composted on site.'
    },
    garden: {
        title: 'Pollinator Herbal Butterfly Garden',
        tools: 'Spades, Watering cans, Organic compost, Bamboo border pegs',
        steps: 'Loosen soil in south-facing courtyard, plant medicinal tulsi, mint, and blooming marigold, and create a small pebble bird bath.',
        impact: 'Attracts butterflies, provides fresh medicinal herbs, beautifies campus.'
    },
    craft: {
        title: 'Eco-Friendly Nature Crafts Project',
        tools: 'Fallen leaves, Pine needles, Seed pods, Recycled paper card',
        steps: 'Gather fallen autumn leaves from grounds, press dry inside heavy books, and paste with natural starch glue to create botanical greeting cards.',
        impact: 'Upcycles natural biomass into art with zero plastic glitter or toxic glues.'
    }
};

function selectActionProject(project) {
    playClickSfx();
    ['clean', 'garden', 'craft'].forEach(p => {
        const btn = document.getElementById(`proj-tab-${p}`);
        if (btn) {
            if (p === project) {
                btn.className = 'px-3 py-1.5 rounded-lg border border-teal-500 bg-teal-950/40 text-teal-300 font-bold ring-2 ring-teal-500';
            } else {
                btn.className = 'px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-800 text-slate-300 hover:bg-slate-700 font-medium';
            }
        }
    });
    
    const pData = ACTION_PROJECTS[project];
    const card = document.getElementById('action-project-card');
    if (!card) return;
    
    card.innerHTML = `
        <h4 class="font-bold text-teal-300 text-sm">${pData.title}</h4>
        <div class="text-xs text-slate-300 space-y-1">
            <div><strong>Equipment Needed:</strong> ${pData.tools}</div>
            <div><strong>Action Steps:</strong> ${pData.steps}</div>
            <div class="text-emerald-400"><strong>Civic Impact:</strong> ${pData.impact}</div>
        </div>
    `;
}

// ============================================================================
// SIMULATOR 16: Public Riddles & Crafts Studio
// ============================================================================
const RIDDLE_ANSWERS = {
    bus: {
        clue: 'I have many platforms, rumbling buses arrive and depart, and ticket booths guide commuters to distant towns.',
        answer: '🚌 The Bus Stand / Depot',
        craft: 'Local Transport: Wooden bullock cart models and painted transport signage.'
    },
    post: {
        clue: 'I have bright red collection boxes, sorted parcels, and stamps carrying handwritten greetings across continents.',
        answer: '📮 The Post Office',
        craft: 'Paper Crafts: Hand-made stationery, block-printed envelopes, and paper seals.'
    },
    market: {
        clue: 'Where farmers, weavers, and shoppers bargain amidst colourful stalls of seasonal fruits, vegetables, and woven textiles.',
        answer: '🛒 The Weekly Market (Haat)',
        craft: 'Bamboo Weaving: Lightweight winnowing trays, storage baskets, and wicker mats.'
    },
    park: {
        clue: 'Where green grass lawns, shade trees, flowerbeds, and swing sets offer quiet relaxation, fresh air, and joyful play.',
        answer: '🌳 The Community Park',
        craft: 'Pottery: Wheel-spun terracotta flower pots, bird baths, and earthen water jugs (matkas).'
    }
};

function revealRiddle(riddle) {
    playSuccessSfx();
    const rData = RIDDLE_ANSWERS[riddle];
    const box = document.getElementById('riddle-output-box');
    if (!box) return;
    
    box.innerHTML = `
        <div class="space-y-1.5">
            <p class="text-xs text-slate-300 italic">"${rData.clue}"</p>
            <div class="text-sm font-bold text-yellow-400">Answer: ${rData.answer}</div>
            <div class="text-xs text-emerald-300 bg-emerald-950/40 p-2 rounded-lg border border-emerald-800/40">
                <strong>Regional Craft Connection:</strong> ${rData.craft}
            </div>
        </div>
    `;
}

// ============================================================================
// Simulator Initialization Dispatcher
// ============================================================================
function initSimulatorForSlide(slideNum) {
    if (slideNum === 1) selectVillageLandmark('banyan');
    if (slideNum === 2) selectServiceCard('health');
    if (slideNum === 4) selectTreeSpecies('neem');
    if (slideNum === 5) updateCommunityPoster();
    if (slideNum === 7) selectTradeToolKit('mason');
    if (slideNum === 8) goToPlantStep(1);
    if (slideNum === 9) setBridgeTimeline(0);
    if (slideNum === 10) selectInsectColony('ant');
    if (slideNum === 12) updateCompostStage(1);
    if (slideNum === 13) selectRegionalTradition('assam');
    if (slideNum === 14) selectSchoolRole('teacher');
    if (slideNum === 15) selectActionProject('clean');
    if (slideNum === 16) revealRiddle('bus');
}

// Global initialization
window.addEventListener('DOMContentLoaded', () => {
    showSlide(1);
    if ('speechSynthesis' in window) {
        window.speechSynthesis.onvoiceschanged = () => {
            // Voices pre-loaded
        };
    }
});
'''

with open(".agents/class4_science_ch1_js.js", "w", encoding="utf-8") as f:
    f.write(js_code)

output_py = f"""# -*- coding: utf-8 -*-
\"\"\"
Class 4 Science Chapter 1: Living Together
Compiled JS Engine String
\"\"\"

JS_ENGINE = '''{js_code}'''
"""

with open(".agents/class4_science_ch1_js.py", "w", encoding="utf-8") as f:
    f.write(output_py)

print("Generated .agents/class4_science_ch1_js.js and .agents/class4_science_ch1_js.py successfully!")

