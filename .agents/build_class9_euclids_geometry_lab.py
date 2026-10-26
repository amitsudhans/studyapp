# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 7
INTRODUCTION TO EUCLID'S GEOMETRY: AXIOMS AND POSTULATES (Competencies CG-7, C-7.1, C-7.3)
Generates public/animations/class9-euclids-geometry.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_euclids_geometry_data import SLIDES, QUIZZES

OUTPUT_PATH = "public/animations/class9-euclids-geometry.html"

# Ensure exp is duplicated to explanation for checkpoints
for s in SLIDES:
    for cp in s["checkpoints"]:
        cp["explanation"] = cp.get("exp", cp.get("explanation", ""))

def generate_html():
    slides_json = json.dumps(SLIDES)
    quizzes_json = json.dumps(QUIZZES)

    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 9 Mathematics • Introduction to Euclid's Geometry Lab</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- KaTeX CSS & JS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
            onload="renderMathInElement(document.body);"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        .font-mono {
            font-family: 'JetBrains Mono', monospace;
        }
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #0f172a;
        }
        ::-webkit-scrollbar-thumb {
            background: #334155;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #475569;
        }
        .mouth-talking {
            animation: mouthTalk 0.25s infinite alternate ease-in-out;
            transform-origin: 50% 65%;
        }
        @keyframes mouthTalk {
            0% { transform: scaleY(0.2); }
            100% { transform: scaleY(1.4); }
        }
        .slide-fade-in {
            animation: fadeIn 0.3s ease-out forwards;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col selection:bg-amber-500 selection:text-white">

    <!-- Top Navigation Header -->
    <header class="bg-slate-900/90 backdrop-blur-md border-b border-slate-800 sticky top-0 z-40 px-4 py-2.5">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-amber-600 to-rose-500 flex items-center justify-center shadow-lg shadow-amber-500/30">
                    <i data-lucide="compass" class="w-5 h-5 text-white"></i>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-bold uppercase tracking-wider text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20">Class 9 Maths • Chapter 7</span>
                        <span id="currentBadge" class="hidden sm:inline-block text-xs text-rose-400 bg-rose-500/10 px-2 py-0.5 rounded border border-rose-500/20 font-semibold">CG-7 • Ancient Origins</span>
                    </div>
                    <h1 class="text-sm sm:text-base font-extrabold text-white tracking-tight">Introduction to Euclid's Geometry Lab</h1>
                </div>
            </div>

            <!-- Central Slide Indicator -->
            <div class="flex items-center gap-2 bg-slate-950/80 px-3 py-1.5 rounded-xl border border-slate-800">
                <span class="text-xs text-slate-400">Slide</span>
                <span id="slideCounter" class="text-sm font-bold text-amber-400 font-mono">1 / 20</span>
                <div class="w-20 sm:w-28 bg-slate-800 h-2 rounded-full overflow-hidden ml-1">
                    <div id="progressBar" class="bg-gradient-to-r from-amber-500 to-rose-500 h-full w-[5%] transition-all duration-300"></div>
                </div>
            </div>

            <!-- Voice Controls & Speed -->
            <div class="flex items-center gap-2">
                <div class="flex items-center bg-slate-800/80 rounded-lg p-0.5 border border-slate-700">
                    <button onclick="changeSpeed(0.8)" id="spd08" class="px-2 py-1 text-[11px] rounded font-medium text-slate-300 hover:text-white transition">0.8x</button>
                    <button onclick="changeSpeed(1.0)" id="spd10" class="px-2 py-1 text-[11px] rounded font-bold bg-amber-600 text-white transition">1.0x</button>
                    <button onclick="changeSpeed(1.2)" id="spd12" class="px-2 py-1 text-[11px] rounded font-medium text-slate-300 hover:text-white transition">1.2x</button>
                </div>
                <button onclick="toggleAudio()" id="voiceToggleBtn" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-amber-600 hover:bg-amber-500 text-white transition shadow-md shadow-amber-600/30">
                    <i data-lucide="volume-2" class="w-4 h-4"></i>
                    <span id="voiceBtnText">Voice On</span>
                </button>
                <button onclick="replayAudio()" title="Replay Audio" class="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition">
                    <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
                </button>
            </div>
        </div>
    </header>

    <!-- Teacher Avatar & Live Narration Banner -->
    <div class="bg-slate-900/60 border-b border-slate-800/80 px-4 py-2.5">
        <div class="max-w-7xl mx-auto flex items-center gap-3">
            <div class="relative shrink-0">
                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-amber-500 to-rose-600 p-0.5 shadow-md shadow-amber-500/20">
                    <svg viewBox="0 0 100 100" class="w-full h-full rounded-full bg-slate-900">
                        <circle cx="50" cy="50" r="48" fill="#1e293b"/>
                        <path d="M50 18 C32 18 24 32 24 48 C24 64 34 82 50 82 C66 82 76 64 76 48 C76 32 68 18 50 18 Z" fill="#fed7aa"/>
                        <path d="M22 38 C22 20 34 12 50 12 C66 12 78 20 78 38 C78 44 74 46 72 38 C68 22 32 22 28 38 C26 46 22 44 22 38 Z" fill="#334155"/>
                        <ellipse cx="38" cy="46" rx="4" ry="5" fill="#0f172a"/>
                        <ellipse cx="62" cy="46" rx="4" ry="5" fill="#0f172a"/>
                        <circle cx="39" cy="44" r="1.5" fill="#ffffff"/>
                        <circle cx="63" cy="44" r="1.5" fill="#ffffff"/>
                        <circle cx="38" cy="46" r="8" fill="none" stroke="#64748b" stroke-width="2"/>
                        <circle cx="62" cy="46" r="8" fill="none" stroke="#64748b" stroke-width="2"/>
                        <line x1="46" y1="46" x2="54" y2="46" stroke="#64748b" stroke-width="2"/>
                        <path d="M48 50 L52 50 L50 56 Z" fill="#fbcfe8"/>
                        <g id="teacherMouth">
                            <ellipse cx="50" cy="65" rx="5" ry="2.5" fill="#be123c"/>
                        </g>
                    </svg>
                </div>
                <div id="speakingPulse" class="hidden absolute -top-1 -right-1 w-3.5 h-3.5 rounded-full bg-emerald-500 border-2 border-slate-900 animate-ping"></div>
            </div>
            <div class="flex-1 min-w-0">
                <div class="flex items-center gap-2">
                    <span class="text-xs font-bold text-amber-400">Prof. Sophia</span>
                    <span class="text-[10px] text-slate-400">• Ancient Mathematics & Logic Guide</span>
                </div>
                <p id="narrationText" class="text-xs sm:text-sm text-slate-200 truncate font-normal">
                    Welcome to Euclid's Geometry! Discover how geometry grew from the flooded Nile and Vedic altars into Euclid's axioms.
                </p>
            </div>
        </div>
    </div>

    <!-- Main Workspace Container -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 flex flex-col justify-between">
        <div id="slideContentContainer">
            <!-- Dynamically populated slide content -->
        </div>

        <!-- Universal Pop-up Solution Modal -->
        <div id="solutionModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
            <div class="bg-slate-900 border border-amber-500/30 rounded-2xl max-w-xl w-full p-5 sm:p-6 shadow-2xl relative max-h-[85vh] overflow-y-auto">
                <div class="flex items-start justify-between gap-3 border-b border-slate-800 pb-3 mb-4">
                    <div class="flex items-center gap-2">
                        <div class="w-7 h-7 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center">
                            <i data-lucide="book-marked" class="w-4 h-4"></i>
                        </div>
                        <div>
                            <h3 class="text-sm font-bold text-white">Step-by-Step Mathematical Solution</h3>
                            <span id="modalQSubtitle" class="text-xs text-amber-400 font-mono"></span>
                        </div>
                    </div>
                    <button onclick="closeSolutionModal()" class="p-1 rounded-lg hover:bg-slate-800 text-slate-400 hover:text-white transition">
                        <i data-lucide="x" class="w-5 h-5"></i>
                    </button>
                </div>
                <div class="mb-4 p-3 bg-slate-950 rounded-xl border border-slate-800 text-xs sm:text-sm text-slate-300 font-medium leading-relaxed" id="modalQuestionText">
                    <!-- Question text -->
                </div>
                <div class="p-4 bg-amber-950/20 rounded-xl border border-amber-500/20 text-xs sm:text-sm text-amber-200 leading-relaxed font-mono space-y-2" id="modalSolutionText">
                    <!-- Solution derivation -->
                </div>
                <div class="mt-5 flex justify-end">
                    <button onclick="closeSolutionModal()" class="px-4 py-2 rounded-xl text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition">
                        Understood & Close
                    </button>
                </div>
            </div>
        </div>

        <!-- Last Slide Notice Banner -->
        <div id="lastSlideNotice" class="hidden mt-6 p-4 rounded-xl bg-gradient-to-r from-emerald-950/60 via-slate-900 to-amber-950/60 border border-emerald-500/40 text-center">
            <div class="flex items-center justify-center gap-2 text-emerald-400 font-bold text-sm sm:text-base">
                <i data-lucide="check-circle" class="w-5 h-5"></i>
                <span>You have reached the last slide of this chapter</span>
            </div>
            <p class="text-xs text-slate-300 mt-1">
                Outstanding accomplishment! You have mastered the historical origins of geometry, Harappan urban ratios, Baudhayana's Sulbasutras, Euclid's 23 definitions, 7 common notions, 5 postulates, Playfair's parallel axiom, and non-Euclidean geometries.
            </p>
        </div>

        <!-- Bottom Navigation Bar -->
        <footer class="mt-6 pt-4 border-t border-slate-800/80 flex items-center justify-between gap-3">
            <button onclick="prevSlide()" id="prevBtn" class="flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold bg-slate-900 hover:bg-slate-800 text-slate-200 border border-slate-800 hover:border-slate-700 transition">
                <i data-lucide="arrow-left" class="w-4 h-4"></i>
                Previous Slide
            </button>

            <!-- Slide Thumbnails Indicator -->
            <div class="hidden md:flex items-center gap-1" id="thumbnailTrack">
                <!-- 20 mini dot indicators -->
            </div>

            <button onclick="nextSlide()" id="nextBtn" class="flex items-center gap-2 px-5 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-amber-600 to-rose-600 hover:from-amber-500 hover:to-rose-500 text-white shadow-lg shadow-amber-600/30 transition">
                Next Slide
                <i data-lucide="arrow-right" class="w-4 h-4"></i>
            </button>
        </footer>
    </main>

    <script>
        // --- DATA STRUCTURES ---
        const SLIDES = __SLIDES_JSON__;
        const QUIZZES = __QUIZZES_JSON__;
        const ALL_SLIDES = [...SLIDES, ...QUIZZES];

        let currentSlideIndex = 0;
        let speechRate = 1.0;
        let isAudioMuted = false;
        let synth = window.speechSynthesis;
        let activeUtterance = null;
        let audioCtx = null;

        function initAudioContext() {
            if (!audioCtx) {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                if (AudioContext) {
                    audioCtx = new AudioContext();
                }
            }
            if (audioCtx && audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
        }

        function playTone(freq, type = 'sine', duration = 0.2) {
            try {
                initAudioContext();
                if (!audioCtx) return;
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + duration);
            } catch (e) {
                console.warn('Audio tone error:', e);
            }
        }

        function playSuccessSound() {
            playTone(523.25, 'triangle', 0.15);
            setTimeout(() => playTone(659.25, 'triangle', 0.15), 100);
            setTimeout(() => playTone(783.99, 'triangle', 0.25), 200);
        }

        function playErrorSound() {
            playTone(220.00, 'sawtooth', 0.2);
            setTimeout(() => playTone(196.00, 'sawtooth', 0.25), 150);
        }

        function speakCurrentSlide() {
            if (isAudioMuted || !('speechSynthesis' in window)) return;
            synth.cancel();

            const slide = ALL_SLIDES[currentSlideIndex];
            const textToSpeak = slide.narration || (slide.title + ". " + slide.subtitle);

            const mouth = document.getElementById('teacherMouth');
            const pulse = document.getElementById('speakingPulse');

            activeUtterance = new SpeechSynthesisUtterance(textToSpeak);
            activeUtterance.rate = speechRate;
            activeUtterance.lang = 'en-US';

            activeUtterance.onstart = () => {
                if (mouth) mouth.classList.add('mouth-talking');
                if (pulse) pulse.classList.remove('hidden');
            };

            activeUtterance.onend = () => {
                if (mouth) mouth.classList.remove('mouth-talking');
                if (pulse) pulse.classList.add('hidden');
            };

            activeUtterance.onerror = () => {
                if (mouth) mouth.classList.remove('mouth-talking');
                if (pulse) pulse.classList.add('hidden');
            };

            synth.speak(activeUtterance);
        }

        function toggleAudio() {
            initAudioContext();
            isAudioMuted = !isAudioMuted;
            const btnText = document.getElementById('voiceBtnText');
            const btn = document.getElementById('voiceToggleBtn');

            if (isAudioMuted) {
                synth.cancel();
                btnText.textContent = "Voice Muted";
                btn.className = "flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 text-slate-400 hover:text-white transition";
                const mouth = document.getElementById('teacherMouth');
                if (mouth) mouth.classList.remove('mouth-talking');
            } else {
                btnText.textContent = "Voice On";
                btn.className = "flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-amber-600 hover:bg-amber-500 text-white transition shadow-md shadow-amber-600/30";
                speakCurrentSlide();
            }
        }

        function replayAudio() {
            initAudioContext();
            speakCurrentSlide();
        }

        function changeSpeed(rate) {
            speechRate = rate;
            ['spd08', 'spd10', 'spd12'].forEach(id => {
                const el = document.getElementById(id);
                if (el) {
                    el.className = "px-2 py-1 text-[11px] rounded font-medium text-slate-400 hover:text-white transition";
                }
            });
            const activeId = rate === 0.8 ? 'spd08' : (rate === 1.0 ? 'spd10' : 'spd12');
            const activeEl = document.getElementById(activeId);
            if (activeEl) {
                activeEl.className = "px-2 py-1 text-[11px] rounded font-bold bg-amber-600 text-white transition";
            }
            speakCurrentSlide();
        }

        function renderCurrentSlide() {
            const slide = ALL_SLIDES[currentSlideIndex];
            const total = ALL_SLIDES.length;
            const currNum = currentSlideIndex + 1;

            // Update Progress & Badges
            document.getElementById('slideCounter').textContent = `${currNum} / ${total}`;
            document.getElementById('progressBar').style.width = `${(currNum / total) * 100}%`;
            document.getElementById('currentBadge').textContent = slide.badge || "Euclid's Geometry";
            document.getElementById('narrationText').textContent = slide.narration || slide.summary || slide.subtitle;

            // Render Thumbnails
            renderThumbnails();

            const container = document.getElementById('slideContentContainer');
            const lastNotice = document.getElementById('lastSlideNotice');
            const nextBtn = document.getElementById('nextBtn');
            const prevBtn = document.getElementById('prevBtn');

            // Handle Previous button state
            prevBtn.disabled = (currentSlideIndex === 0);
            prevBtn.style.opacity = (currentSlideIndex === 0) ? '0.5' : '1';

            if (currentSlideIndex < 16) {
                // Content Slide (1 - 16)
                lastNotice.classList.add('hidden');
                nextBtn.style.display = 'flex';

                container.innerHTML = `
                    <div class="slide-fade-in space-y-6">
                        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
                            <div>
                                <span class="text-xs font-bold text-amber-400 font-mono">CONCEPT #${currNum}</span>
                                <h2 class="text-xl sm:text-2xl font-black text-white tracking-tight">${slide.title}</h2>
                                <p class="text-xs sm:text-sm text-slate-400 font-medium mt-0.5">${slide.subtitle}</p>
                            </div>
                            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-300 font-semibold">${slide.category}</span>
                        </div>

                        <!-- 2-Column Split: Theory on Left, Simulator on Right -->
                        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 items-start">
                            <!-- Left: Theory & Checkpoints -->
                            <div class="space-y-4">
                                <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800/90 shadow-lg">
                                    <h3 class="text-xs font-bold uppercase tracking-wider text-amber-400 mb-2 flex items-center gap-1.5">
                                        <i data-lucide="book-open" class="w-4 h-4"></i>
                                        Conceptual Overview
                                    </h3>
                                    <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                                        ${slide.summary}
                                    </p>
                                </div>

                                <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800/90 shadow-lg">
                                    <h3 class="text-xs font-bold uppercase tracking-wider text-rose-400 mb-2.5 flex items-center gap-1.5">
                                        <i data-lucide="sparkles" class="w-4 h-4"></i>
                                        Key Mathematical Insights
                                    </h3>
                                    <ul class="text-xs text-slate-300 space-y-2">
                                        ${slide.key_points.map(kp => `
                                            <li class="flex items-start gap-2">
                                                <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-amber-400 shrink-0 mt-0.5"></i>
                                                <span>${kp}</span>
                                            </li>
                                        `).join('')}
                                    </ul>
                                </div>

                                <!-- In-Slide 2 Checkpoint Questions -->
                                <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800/90 shadow-lg space-y-4">
                                    <h3 class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-1.5">
                                        <i data-lucide="help-circle" class="w-4 h-4"></i>
                                        Slide Checkpoints (2 Questions)
                                    </h3>
                                    <div class="space-y-4">
                                        ${slide.checkpoints.map((cp, cIdx) => `
                                            <div class="p-3 bg-slate-950/80 rounded-xl border border-slate-800">
                                                <div class="text-xs font-semibold text-slate-200 mb-2">Q${cIdx + 1}: ${cp.q}</div>
                                                <div class="space-y-1.5 mb-2">
                                                    ${cp.options.map((opt, oIdx) => `
                                                        <button onclick="checkCheckpoint(${cIdx}, ${oIdx}, ${cp.ans})" id="cp_${cIdx}_${oIdx}" class="w-full text-left text-xs px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-800 hover:border-amber-500/50 text-slate-300 transition flex items-center justify-between">
                                                            <span>${opt}</span>
                                                            <span id="cp_ind_${cIdx}_${oIdx}" class="hidden font-bold text-xs"></span>
                                                        </button>
                                                    `).join('')}
                                                </div>
                                                <div id="cp_exp_${cIdx}" class="hidden text-[11px] p-2.5 rounded-lg bg-amber-950/40 border border-amber-500/30 text-amber-200">
                                                    ${cp.explanation}
                                                </div>
                                            </div>
                                        `).join('')}
                                    </div>
                                </div>
                            </div>

                            <!-- Right: Bespoke Interactive Simulator -->
                            <div class="p-5 rounded-2xl bg-slate-900/90 border border-amber-500/30 shadow-xl flex flex-col justify-between min-h-[460px]">
                                <div>
                                    <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
                                        <div class="flex items-center gap-2">
                                            <div class="w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></div>
                                            <h4 class="text-xs sm:text-sm font-bold text-amber-300">${slide.sim_title}</h4>
                                        </div>
                                        <span class="text-[10px] text-slate-400 font-mono">Interactive Model</span>
                                    </div>
                                    <div id="simContainer_${currNum}" class="w-full flex flex-col items-center justify-center">
                                        <!-- Interactive Simulator Injected Here -->
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                `;

                // Initialize specific slide simulator
                setTimeout(() => {
                    initSlideSimulator(currNum);
                    if (window.renderMathInElement) renderMathInElement(container);
                    if (window.lucide) lucide.createIcons();
                }, 50);

            } else {
                // Quiz Slide (17 - 20)
                const isLast = (currentSlideIndex === total - 1);
                if (isLast) {
                    lastNotice.classList.remove('hidden');
                    nextBtn.style.display = 'none';
                } else {
                    lastNotice.classList.add('hidden');
                    nextBtn.style.display = 'flex';
                }

                container.innerHTML = `
                    <div class="slide-fade-in space-y-5">
                        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
                            <div>
                                <span class="text-xs font-bold text-amber-400 font-mono">MASTERY CHALLENGE</span>
                                <h2 class="text-xl sm:text-2xl font-black text-white tracking-tight">${slide.title}</h2>
                                <p class="text-xs sm:text-sm text-slate-400 font-medium">${slide.subtitle}</p>
                            </div>
                            <span class="text-xs px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-300 font-bold">10 Multi-Step Questions</span>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            ${slide.questions.map((q, qIdx) => `
                                <div class="p-4 bg-slate-900/80 rounded-2xl border border-slate-800 flex flex-col justify-between shadow-md">
                                    <div>
                                        <div class="flex items-center justify-between gap-2 mb-2">
                                            <span class="text-xs font-bold text-amber-400 font-mono">Question ${q.id}</span>
                                            <button onclick="showSolution(${currentSlideIndex}, ${qIdx})" class="px-2.5 py-1 rounded-lg text-[10px] font-bold bg-amber-500/10 hover:bg-amber-500/20 text-amber-300 border border-amber-500/30 transition flex items-center gap-1.5 shadow-sm">
                                                <i data-lucide="eye" class="w-3.5 h-3.5"></i>
                                                View Solution
                                            </button>
                                        </div>
                                        <p class="text-xs sm:text-sm text-slate-200 font-medium mb-3">${q.q}</p>
                                        <div class="space-y-1.5 mb-2">
                                            ${q.options.map((opt, oIdx) => `
                                                <button onclick="answerQuiz(${q.id}, ${oIdx}, ${q.ans})" id="quiz_${q.id}_${oIdx}" class="w-full text-left text-xs px-3 py-2 rounded-xl bg-slate-950/80 border border-slate-800 hover:border-amber-500/50 text-slate-300 transition flex items-center justify-between">
                                                    <span>${opt}</span>
                                                    <span id="quiz_ind_${q.id}_${oIdx}" class="hidden font-bold"></span>
                                                </button>
                                            `).join('')}
                                        </div>
                                    </div>
                                    <div id="quiz_sol_preview_${q.id}" class="hidden mt-2 p-2 rounded-lg bg-slate-950 text-[10px] text-slate-400 border border-slate-800 flex items-center justify-between">
                                        <span class="text-emerald-400 font-bold">Answered</span>
                                        <button onclick="showSolution(${currentSlideIndex}, ${qIdx})" class="text-amber-400 hover:underline">Click to view derivation</button>
                                    </div>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                `;

                setTimeout(() => {
                    if (window.renderMathInElement) renderMathInElement(container);
                    if (window.lucide) lucide.createIcons();
                }, 50);
            }

            speakCurrentSlide();
        }

        function renderThumbnails() {
            const track = document.getElementById('thumbnailTrack');
            if (!track) return;
            track.innerHTML = ALL_SLIDES.map((s, idx) => {
                const isActive = (idx === currentSlideIndex);
                const isQuiz = (idx >= 16);
                let colorClass = isActive
                    ? (isQuiz ? 'bg-rose-400 ring-2 ring-rose-400/50 scale-125' : 'bg-amber-400 ring-2 ring-amber-400/50 scale-125')
                    : (isQuiz ? 'bg-rose-900/60 hover:bg-rose-600' : 'bg-slate-700 hover:bg-slate-500');
                return `
                    <button onclick="goToSlide(${idx})" title="Slide ${idx + 1}" class="w-2.5 h-2.5 rounded-full transition-all duration-200 ${colorClass}"></button>
                `;
            }).join('');
        }

        function nextSlide() {
            if (currentSlideIndex < ALL_SLIDES.length - 1) {
                currentSlideIndex++;
                renderCurrentSlide();
            }
        }

        function prevSlide() {
            if (currentSlideIndex > 0) {
                currentSlideIndex--;
                renderCurrentSlide();
            }
        }

        function goToSlide(idx) {
            if (idx >= 0 && idx < ALL_SLIDES.length) {
                currentSlideIndex = idx;
                renderCurrentSlide();
            }
        }

        function checkCheckpoint(cIdx, oIdx, ans) {
            initAudioContext();
            const slide = ALL_SLIDES[currentSlideIndex];
            const numOpts = slide.checkpoints[cIdx].options.length;

            for (let i = 0; i < numOpts; i++) {
                const btn = document.getElementById(`cp_${cIdx}_${i}`);
                const ind = document.getElementById(`cp_ind_${cIdx}_${i}`);
                if (!btn || !ind) continue;
                btn.disabled = true;

                if (i === ans) {
                    btn.classList.add('border-emerald-500', 'bg-emerald-950/30', 'text-emerald-300');
                    ind.textContent = '✓';
                    ind.classList.remove('hidden');
                    ind.classList.add('text-emerald-400');
                } else if (i === oIdx && oIdx !== ans) {
                    btn.classList.add('border-rose-500', 'bg-rose-950/30', 'text-rose-300');
                    ind.textContent = '✗';
                    ind.classList.remove('hidden');
                    ind.classList.add('text-rose-400');
                }
            }

            const exp = document.getElementById(`cp_exp_${cIdx}`);
            if (exp) exp.classList.remove('hidden');

            if (oIdx === ans) playSuccessSound();
            else playErrorSound();
        }

        function answerQuiz(qId, oIdx, ans) {
            initAudioContext();
            const slide = ALL_SLIDES[currentSlideIndex];
            const qObj = slide.questions.find(q => q.id === qId);
            if (!qObj) return;

            for (let i = 0; i < qObj.options.length; i++) {
                const btn = document.getElementById(`quiz_${qId}_${i}`);
                const ind = document.getElementById(`quiz_ind_${qId}_${i}`);
                if (!btn || !ind) continue;
                btn.disabled = true;

                if (i === ans) {
                    btn.classList.add('border-emerald-500', 'bg-emerald-950/30', 'text-emerald-300');
                    ind.textContent = '✓ Correct';
                    ind.classList.remove('hidden');
                    ind.classList.add('text-emerald-400');
                } else if (i === oIdx && oIdx !== ans) {
                    btn.classList.add('border-rose-500', 'bg-rose-950/30', 'text-rose-300');
                    ind.textContent = '✗';
                    ind.classList.remove('hidden');
                    ind.classList.add('text-rose-400');
                }
            }

            const preview = document.getElementById(`quiz_sol_preview_${qId}`);
            if (preview) preview.classList.remove('hidden');

            if (oIdx === ans) playSuccessSound();
            else playErrorSound();
        }

        function showSolution(slideIdx, qIdx) {
            initAudioContext();
            const slide = ALL_SLIDES[slideIdx];
            const qObj = slide.questions[qIdx];
            if (!qObj) return;

            document.getElementById('modalQSubtitle').textContent = `Slide ${slideIdx + 1} • Question ${qObj.id}`;
            document.getElementById('modalQuestionText').textContent = qObj.q;

            const solEl = document.getElementById('modalSolutionText');
            solEl.innerHTML = qObj.solution;

            document.getElementById('solutionModal').classList.remove('hidden');
            if (window.renderMathInElement) renderMathInElement(solEl);
            if (window.lucide) lucide.createIcons();
            playTone(440, 'sine', 0.1);
        }

        function closeSolutionModal() {
            document.getElementById('solutionModal').classList.add('hidden');
        }

        window.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight') nextSlide();
            if (e.key === 'ArrowLeft') prevSlide();
            if (e.key === 'Escape') closeSolutionModal();
        });

        // --- 16 BESPOKE SIMULATORS LOGIC ---

        function initSlideSimulator(sNum) {
            const container = document.getElementById(`simContainer_${sNum}`);
            if (!container) return;

            if (sNum === 1) renderSim1(container);
            else if (sNum === 2) renderSim2(container);
            else if (sNum === 3) renderSim3(container);
            else if (sNum === 4) renderSim4(container);
            else if (sNum === 5) renderSim5(container);
            else if (sNum === 6) renderSim6(container);
            else if (sNum === 7) renderSim7(container);
            else if (sNum === 8) renderSim8(container);
            else if (sNum === 9) renderSim9(container);
            else if (sNum === 10) renderSim10(container);
            else if (sNum === 11) renderSim11(container);
            else if (sNum === 12) renderSim12(container);
            else if (sNum === 13) renderSim13(container);
            else if (sNum === 14) renderSim14(container);
            else if (sNum === 15) renderSim15(container);
            else if (sNum === 16) renderSim16(container);
        }

        // SIMULATOR 1: Nile Flood & Land Re-Surveyor
        function renderSim1(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="nileSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="flex items-center justify-between gap-2">
                        <button onclick="floodNile()" class="flex-1 px-3 py-1.5 rounded-xl text-xs font-bold bg-blue-600 hover:bg-blue-500 text-white transition">
                            🌊 Trigger Nile Flood
                        </button>
                        <button onclick="surveyNile()" class="flex-1 px-3 py-1.5 rounded-xl text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition">
                            📏 Stretch Surveyor Ropes
                        </button>
                    </div>
                    <div id="nileStatus" class="p-2.5 rounded-xl border border-amber-500/30 bg-slate-950 text-xs font-mono text-center text-amber-300">
                        Fields marked with pegs. Press 'Trigger Nile Flood' to wash away boundaries!
                    </div>
                </div>
            `;
            window.nileState = 'dry';
            drawNile();
        }

        function floodNile() {
            window.nileState = 'flooded';
            document.getElementById('nileStatus').innerHTML = `<span class="text-blue-400 font-bold">The Nile flooded!</span> All farm boundaries washed away. Surveyors needed!`;
            drawNile();
            playTone(180, 'sine', 0.4);
        }

        function surveyNile() {
            window.nileState = 'surveyed';
            document.getElementById('nileStatus').innerHTML = `<span class="text-emerald-400 font-bold">Ropes stretched!</span> 4 square plots restored: 100 royal cubits × 100 cubits each.`;
            drawNile();
            playSuccessSound();
        }

        function drawNile() {
            const svg = document.getElementById('nileSvg');
            if (!svg) return;
            const state = window.nileState;

            let waterOverlay = '';
            let boundaries = '';

            if (state === 'flooded') {
                waterOverlay = `<rect x="0" y="0" width="300" height="300" fill="#0284c7" fill-opacity="0.6"/>
                    <path d="M0 100 Q 75 80 150 100 T 300 100 L 300 300 L 0 300 Z" fill="#0369a1" fill-opacity="0.8"/>
                    <text x="70" y="150" fill="#ffffff" font-size="14" font-weight="bold">NILE INUNDATION</text>`;
            } else if (state === 'surveyed' || state === 'dry') {
                boundaries = `
                    <!-- 4 Farm Plots -->
                    <rect x="30" y="30" width="110" height="110" fill="#15803d" fill-opacity="0.2" stroke="#eab308" stroke-width="2" stroke-dasharray="${state === 'surveyed' ? 'none' : '4'}"/>
                    <rect x="160" y="30" width="110" height="110" fill="#15803d" fill-opacity="0.2" stroke="#eab308" stroke-width="2" stroke-dasharray="${state === 'surveyed' ? 'none' : '4'}"/>
                    <rect x="30" y="160" width="110" height="110" fill="#15803d" fill-opacity="0.2" stroke="#eab308" stroke-width="2" stroke-dasharray="${state === 'surveyed' ? 'none' : '4'}"/>
                    <rect x="160" y="160" width="110" height="110" fill="#15803d" fill-opacity="0.2" stroke="#eab308" stroke-width="2" stroke-dasharray="${state === 'surveyed' ? 'none' : '4'}"/>

                    <!-- Pegs -->
                    <circle cx="30" cy="30" r="4" fill="#f59e0b"/>
                    <circle cx="140" cy="30" r="4" fill="#f59e0b"/>
                    <circle cx="30" cy="140" r="4" fill="#f59e0b"/>
                    <circle cx="140" cy="140" r="4" fill="#f59e0b"/>
                    <text x="65" y="90" fill="#fef08a" font-size="11" font-weight="bold">Plot 1</text>
                    <text x="195" y="90" fill="#fef08a" font-size="11" font-weight="bold">Plot 2</text>
                    <text x="65" y="220" fill="#fef08a" font-size="11" font-weight="bold">Plot 3</text>
                    <text x="195" y="220" fill="#fef08a" font-size="11" font-weight="bold">Plot 4</text>
                `;
            }

            svg.innerHTML = `
                <!-- Sand Background -->
                <rect width="300" height="300" fill="#78350f" fill-opacity="0.4"/>
                ${boundaries}
                ${waterOverlay}
            `;
        }

        // SIMULATOR 2: Harappan Standard Brick & City Grid Planner
        function renderSim2(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="harappaSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="flex items-center justify-between text-xs">
                        <span class="text-slate-400">View Mode:</span>
                        <div class="flex gap-2">
                            <button onclick="setHarappaMode('brick')" id="hBrickBtn" class="px-2.5 py-1 rounded bg-amber-600 text-white font-bold">Standard 4:2:1 Brick</button>
                            <button onclick="setHarappaMode('city')" id="hCityBtn" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300">Harappan City Grid</button>
                        </div>
                    </div>
                    <div id="harappaInfo" class="p-2.5 bg-slate-950 rounded-xl border border-amber-500/30 text-xs font-mono text-center text-amber-300">
                        Harappan Brick: Length (28cm) : Breadth (14cm) : Height (7cm) = 4 : 2 : 1
                    </div>
                </div>
            `;
            window.harappaMode = 'brick';
            drawHarappa();
        }

        function setHarappaMode(m) {
            window.harappaMode = m;
            document.getElementById('hBrickBtn').className = m === 'brick' ? 'px-2.5 py-1 rounded bg-amber-600 text-white font-bold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300';
            document.getElementById('hCityBtn').className = m === 'city' ? 'px-2.5 py-1 rounded bg-amber-600 text-white font-bold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300';
            drawHarappa();
        }

        function drawHarappa() {
            const svg = document.getElementById('harappaSvg');
            if (!svg) return;
            const mode = window.harappaMode || 'brick';

            if (mode === 'brick') {
                document.getElementById('harappaInfo').innerHTML = `
                    <div class="text-amber-400 font-bold">Kiln-Burnt Brick: 28 cm × 14 cm × 7 cm</div>
                    <div class="text-slate-400 text-[11px]">Ratio = 4 : 2 : 1 (Enables interlocking header-stretcher masonry)</div>
                `;
                svg.innerHTML = `
                    <!-- 3D Isometric Brick -->
                    <g transform="translate(60, 80)">
                        <!-- Front Face (Length x Height = 4 x 1) -->
                        <rect x="0" y="40" width="160" height="40" fill="#b45309" stroke="#d97706" stroke-width="2"/>
                        <text x="60" y="65" fill="#fef3c7" font-size="12" font-weight="bold">Length: 4u</text>

                        <!-- Top Face (Length x Breadth = 4 x 2) -->
                        <polygon points="0,40 50,0 210,0 160,40" fill="#d97706" stroke="#f59e0b" stroke-width="2"/>
                        <text x="90" y="25" fill="#ffffff" font-size="11" font-weight="bold">Breadth: 2u</text>

                        <!-- Right Side Face (Breadth x Height = 2 x 1) -->
                        <polygon points="160,40 210,0 210,40 160,80" fill="#78350f" stroke="#b45309" stroke-width="2"/>
                        <text x="175" y="55" fill="#fef3c7" font-size="10" font-weight="bold">1u</text>
                    </g>
                `;
            } else {
                document.getElementById('harappaInfo').innerHTML = `
                    <div class="text-amber-400 font-bold">Mohenjo-daro Orthogonal City Grid</div>
                    <div class="text-slate-400 text-[11px]">Streets intersect at strict 90° right angles with covered drains</div>
                `;
                svg.innerHTML = `
                    <!-- City Blocks -->
                    <rect x="30" y="30" width="70" height="70" fill="#334155" stroke="#64748b"/>
                    <rect x="115" y="30" width="70" height="70" fill="#334155" stroke="#64748b"/>
                    <rect x="200" y="30" width="70" height="70" fill="#334155" stroke="#64748b"/>

                    <rect x="30" y="115" width="70" height="70" fill="#334155" stroke="#64748b"/>
                    <rect x="115" y="115" width="70" height="70" fill="#334155" stroke="#64748b"/>
                    <rect x="200" y="115" width="70" height="70" fill="#334155" stroke="#64748b"/>

                    <rect x="30" y="200" width="70" height="70" fill="#334155" stroke="#64748b"/>
                    <rect x="115" y="200" width="70" height="70" fill="#334155" stroke="#64748b"/>
                    <rect x="200" y="200" width="70" height="70" fill="#334155" stroke="#64748b"/>

                    <!-- 90° Intersecting Streets -->
                    <line x1="107" y1="20" x2="107" y2="280" stroke="#f59e0b" stroke-width="3"/>
                    <line x1="192" y1="20" x2="192" y2="280" stroke="#f59e0b" stroke-width="3"/>
                    <line x1="20" y1="107" x2="280" y2="107" stroke="#f59e0b" stroke-width="3"/>
                    <line x1="20" y1="192" x2="280" y2="192" stroke="#f59e0b" stroke-width="3"/>

                    <text x="112" y="103" fill="#ef4444" font-size="10" font-weight="bold">90°</text>
                `;
            }
        }

        // SIMULATOR 3: Vedic Sacred Altar Transformer
        function renderSim3(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="altarSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Square Altar Side (a):</span>
                            <span id="altarSideVal" class="text-amber-400 font-bold">10 units</span>
                        </label>
                        <input type="range" min="6" max="14" value="10" step="1" id="altarSideSlider" oninput="updateAltar()" class="w-full accent-amber-500">
                    </div>
                    <div id="altarCalc" class="p-2.5 bg-slate-950 rounded-xl border border-amber-500/30 text-xs font-mono grid grid-cols-2 gap-2 text-center">
                        <!-- Populated by updateAltar() -->
                    </div>
                </div>
            `;
            updateAltar();
        }

        function updateAltar() {
            const a = parseFloat(document.getElementById('altarSideSlider').value);
            document.getElementById('altarSideVal').textContent = `${a} units`;

            const area = a * a;
            const r = Math.sqrt(area / Math.PI).toFixed(2);

            document.getElementById('altarCalc').innerHTML = `
                <div class="p-1.5 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">Ahavaniya (Square):</span>
                    <span class="text-amber-300 font-bold">Area = a² = ${area}</span>
                </div>
                <div class="p-1.5 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">Garhapatya (Circle):</span>
                    <span class="text-rose-300 font-bold">r = a/√π = ${r} (Equal Area!)</span>
                </div>
            `;

            const svg = document.getElementById('altarSvg');
            if (!svg) return;

            const sc = 8;
            const sqSize = a * sc;
            const ox = 150 - sqSize / 2;
            const oy = 150 - sqSize / 2;
            const rPx = r * sc;

            svg.innerHTML = `
                <!-- Square Altar (Ahavaniya) -->
                <rect x="${ox}" y="${oy}" width="${sqSize}" height="${sqSize}" fill="#b45309" fill-opacity="0.3" stroke="#f59e0b" stroke-width="2.5"/>
                <text x="${ox + 10}" y="${oy + 20}" fill="#f59e0b" font-size="11" font-weight="bold">Ahavaniya (Square)</text>

                <!-- Circle Altar (Garhapatya of equal area) -->
                <circle cx="150" cy="150" r="${rPx}" fill="#be123c" fill-opacity="0.25" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="4"/>
                <text x="110" y="155" fill="#f43f5e" font-size="11" font-weight="bold">Garhapatya (Circle)</text>

                <!-- Flame in Center -->
                <circle cx="150" cy="150" r="8" fill="#fbbf24" class="animate-ping" opacity="0.6"/>
                <circle cx="150" cy="150" r="5" fill="#f59e0b"/>
            `;
        }

        // SIMULATOR 4: Baudhayana Sulba Rope-and-Peg Square Constructor
        function renderSim4(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="baudhayanaSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="flex items-center justify-between text-xs">
                        <span class="text-slate-400">Construction Step:</span>
                        <div class="flex gap-1.5">
                            <button onclick="setBaudhStep(1)" id="bStep1" class="px-2 py-0.5 rounded bg-amber-600 text-white font-bold">1. Praci</button>
                            <button onclick="setBaudhStep(2)" id="bStep2" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">2. Arcs</button>
                            <button onclick="setBaudhStep(3)" id="bStep3" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">3. Udici</button>
                            <button onclick="setBaudhStep(4)" id="bStep4" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">4. Square</button>
                        </div>
                    </div>
                    <div id="baudhayanaDesc" class="p-2.5 bg-slate-950 rounded-xl border border-amber-500/30 text-xs font-mono text-center text-amber-300">
                        <!-- Step description -->
                    </div>
                </div>
            `;
            window.baudhStep = 1;
            drawBaudhayana();
        }

        function setBaudhStep(st) {
            window.baudhStep = st;
            [1, 2, 3, 4].forEach(i => {
                document.getElementById(`bStep${i}`).className = (i === st) ? 'px-2 py-0.5 rounded bg-amber-600 text-white font-bold' : 'px-2 py-0.5 rounded bg-slate-800 text-slate-300';
            });
            drawBaudhayana();
            playTone(400 + st * 60, 'triangle', 0.15);
        }

        function drawBaudhayana() {
            const svg = document.getElementById('baudhayanaSvg');
            if (!svg) return;
            const st = window.baudhStep || 1;
            const desc = document.getElementById('baudhayanaDesc');

            const p1 = {x: 80, y: 190}, p2 = {x: 220, y: 190};
            const p3 = {x: 220, y: 50}, p4 = {x: 80, y: 50};

            if (st === 1) {
                desc.textContent = "Step 1: Stretch baseline rope AB along East-West line ('Praci'). Fix wooden pegs at A and B.";
                svg.innerHTML = `
                    <line x1="80" y1="190" x2="220" y2="190" stroke="#f59e0b" stroke-width="3"/>
                    <circle cx="80" cy="190" r="5" fill="#f59e0b"/>
                    <text x="65" y="210" fill="#f59e0b" font-size="11" font-weight="bold">Peg A</text>
                    <circle cx="220" cy="190" r="5" fill="#f59e0b"/>
                    <text x="210" y="210" fill="#f59e0b" font-size="11" font-weight="bold">Peg B</text>
                    <text x="130" y="180" fill="#fef08a" font-size="10">Praci (East-West)</text>
                `;
            } else if (st === 2) {
                desc.textContent = "Step 2: Sweep circular cord arcs from A and B with rope to construct perpendicular line ('Udici').";
                svg.innerHTML = `
                    <line x1="80" y1="190" x2="220" y2="190" stroke="#f59e0b" stroke-width="2"/>
                    <path d="M 80 190 A 100 100 0 0 1 180 90" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3"/>
                    <path d="M 220 190 A 100 100 0 0 0 120 90" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3"/>
                    <circle cx="150" cy="120" r="4" fill="#38bdf8"/>
                    <text x="160" y="120" fill="#38bdf8" font-size="10">Arc Intersection</text>
                `;
            } else if (st === 3) {
                desc.textContent = "Step 3: Erect perpendiculars along Udici (North-South) and measure length 'a' upwards.";
                svg.innerHTML = `
                    <line x1="80" y1="190" x2="220" y2="190" stroke="#f59e0b" stroke-width="2"/>
                    <line x1="80" y1="190" x2="80" y2="50" stroke="#34d399" stroke-width="2.5"/>
                    <line x1="220" y1="190" x2="220" y2="50" stroke="#34d399" stroke-width="2.5"/>
                    <circle cx="80" cy="50" r="5" fill="#34d399"/>
                    <text x="60" y="45" fill="#34d399" font-size="11" font-weight="bold">Peg D</text>
                    <circle cx="220" cy="50" r="5" fill="#34d399"/>
                    <text x="225" y="45" fill="#34d399" font-size="11" font-weight="bold">Peg C</text>
                `;
            } else {
                desc.textContent = "Step 4: Connect pegs to complete square ABCD! Rope diagonal AC produces area equal to AB² + BC².";
                svg.innerHTML = `
                    <!-- Completed Square -->
                    <polygon points="80,190 220,190 220,50 80,50" fill="#b45309" fill-opacity="0.25" stroke="#f59e0b" stroke-width="3"/>
                    <!-- Diagonal -->
                    <line x1="80" y1="190" x2="220" y2="50" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4"/>
                    <text x="125" y="125" fill="#f43f5e" font-size="10" font-weight="bold">Diagonal d = a√2</text>
                    <circle cx="80" cy="190" r="4" fill="#f59e0b"/>
                    <circle cx="220" cy="190" r="4" fill="#f59e0b"/>
                    <circle cx="220" cy="50" r="4" fill="#f59e0b"/>
                    <circle cx="80" cy="50" r="4" fill="#f59e0b"/>
                `;
            }
        }

        // SIMULATOR 5: Thales' Circle Bisection & Inscribed Angle Theorem
        function renderSim5(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="thalesSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Rotate Point C along Semicircle:</span>
                            <span id="thalesAngleVal" class="text-amber-400 font-bold">Inscribed Angle = 90°</span>
                        </label>
                        <input type="range" min="20" max="160" value="70" step="5" id="thalesAngleSlider" oninput="updateThales()" class="w-full accent-amber-500">
                    </div>
                    <div class="p-2.5 bg-slate-950 rounded-xl border border-amber-500/30 text-xs font-mono text-center text-emerald-400 font-bold">
                        Thales' Theorem: Angle subtended by a diameter at the circumference is ALWAYS 90°!
                    </div>
                </div>
            `;
            updateThales();
        }

        function updateThales() {
            const ang = parseFloat(document.getElementById('thalesAngleSlider').value);
            const rad = (ang * Math.PI) / 180;

            const cx = 150, cy = 150, r = 100;
            const ax = cx - r, ay = cy;
            const bx = cx + r, by = cy;
            const cX = cx - r * Math.cos(rad);
            const cY = cy - r * Math.sin(rad);

            const svg = document.getElementById('thalesSvg');
            if (!svg) return;

            svg.innerHTML = `
                <!-- Circle -->
                <circle cx="${cx}" cy="${cy}" r="${r}" fill="#0f172a" stroke="#475569" stroke-width="2"/>

                <!-- Top Semicircle Shading -->
                <path d="M ${ax} ${ay} A ${r} ${r} 0 0 1 ${bx} ${by} Z" fill="#0284c7" fill-opacity="0.1"/>

                <!-- Diameter AB (Bisects Circle) -->
                <line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#f59e0b" stroke-width="2.5"/>
                <circle cx="${cx}" cy="${cy}" r="3" fill="#f8fafc"/>
                <text x="${cx - 5}" y="${cy + 15}" fill="#94a3b8" font-size="9">O</text>

                <!-- Inscribed Triangle ABC -->
                <polygon points="${ax},${ay} ${bx},${by} ${cX},${cY}" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="2"/>

                <!-- 90° Angle Marker at C -->
                <circle cx="${cX}" cy="${cY}" r="6" fill="#f43f5e"/>
                <text x="${cX - 5}" y="${cY - 10}" fill="#f43f5e" font-size="11" font-weight="bold">C (90°)</text>

                <text x="${ax - 15}" y="${ay + 4}" fill="#f59e0b" font-size="10" font-weight="bold">A</text>
                <text x="${bx + 8}" y="${by + 4}" fill="#f59e0b" font-size="10" font-weight="bold">B</text>
            `;
        }

        // SIMULATOR 6: Euclid's 13 Books of Elements Explorer
        function renderSim6(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="grid grid-cols-4 gap-1.5 text-[11px] font-mono">
                        <button onclick="setElemBook(1)" id="bBtn1" class="p-1.5 rounded bg-amber-600 text-white font-bold">Book I</button>
                        <button onclick="setElemBook(2)" id="bBtn2" class="p-1.5 rounded bg-slate-800 text-slate-300">Book II</button>
                        <button onclick="setElemBook(3)" id="bBtn3" class="p-1.5 rounded bg-slate-800 text-slate-300">Book III</button>
                        <button onclick="setElemBook(4)" id="bBtn4" class="p-1.5 rounded bg-slate-800 text-slate-300">Book IV-VI</button>
                    </div>
                    <div class="p-4 bg-slate-950 rounded-xl border border-slate-800 min-h-[170px] space-y-2 text-xs" id="elemBookDetails">
                        <!-- Populated by setElemBook() -->
                    </div>
                    <div class="p-2.5 bg-slate-950 rounded-xl border border-amber-500/30 text-[11px] font-mono text-center text-amber-300">
                        Total 13 Books: 23 Definitions, 5 Postulates, 5 Axioms & 465 Propositions!
                    </div>
                </div>
            `;
            setElemBook(1);
        }

        function setElemBook(b) {
            [1, 2, 3, 4].forEach(i => {
                const btn = document.getElementById(`bBtn${i}`);
                if (btn) btn.className = (i === b) ? 'p-1.5 rounded bg-amber-600 text-white font-bold' : 'p-1.5 rounded bg-slate-800 text-slate-300';
            });

            const det = document.getElementById('elemBookDetails');
            if (!det) return;

            if (b === 1) {
                det.innerHTML = `
                    <div class="text-amber-400 font-bold text-sm">Book I: Fundamentals of Plane Geometry</div>
                    <div class="text-slate-300 leading-relaxed">Contains 23 Definitions, 5 Postulates, and 5 Common Notions. Ends with Proposition 47 (Pythagorean Theorem) and Proposition 48 (its converse).</div>
                    <div class="text-emerald-400 font-mono text-[11px] mt-1">Key: Congruence of triangles, parallel lines, sum of angles in triangle = 180°.</div>
                `;
            } else if (b === 2) {
                det.innerHTML = `
                    <div class="text-amber-400 font-bold text-sm">Book II: Geometric Algebra</div>
                    <div class="text-slate-300 leading-relaxed">Translates algebraic identities into geometric rectangle areas: (a + b)², difference of squares, and the golden ratio.</div>
                    <div class="text-emerald-400 font-mono text-[11px] mt-1">Key: Law of cosines formulated geometrically without trigonometry.</div>
                `;
            } else if (b === 3) {
                det.innerHTML = `
                    <div class="text-amber-400 font-bold text-sm">Book III: Properties of Circles</div>
                    <div class="text-slate-300 leading-relaxed">37 propositions regarding circles, chords, tangents, inscribed angles, and intersecting chord powers.</div>
                    <div class="text-emerald-400 font-mono text-[11px] mt-1">Key: Angle at center is double the angle at circumference.</div>
                `;
            } else {
                det.innerHTML = `
                    <div class="text-amber-400 font-bold text-sm">Books IV – XIII: Advanced Geometry & Number Theory</div>
                    <div class="text-slate-300 leading-relaxed">Book IV: Inscribed/circumscribed polygons. Book V-VI: Eudoxus' proportion theory. Books VII-IX: Number theory (infinitude of primes). Books X-XIII: 3D solids and the 5 Platonic Solids.</div>
                    <div class="text-emerald-400 font-mono text-[11px] mt-1">Culmination: Proof that exactly 5 regular convex polyhedra exist.</div>
                `;
            }
        }

        // SIMULATOR 7: Dimensional Hierarchy & Boundary Peeler Simulator
        function renderSim7(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="flex items-center justify-between text-xs">
                        <span class="text-slate-400">Select Dimension:</span>
                        <div class="flex gap-1">
                            <button onclick="setDimension(3)" id="dim3Btn" class="px-2 py-0.5 rounded bg-amber-600 text-white font-bold">3D Solid</button>
                            <button onclick="setDimension(2)" id="dim2Btn" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">2D Surface</button>
                            <button onclick="setDimension(1)" id="dim1Btn" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">1D Line</button>
                            <button onclick="setDimension(0)" id="dim0Btn" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">0D Point</button>
                        </div>
                    </div>
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="dimSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div id="dimDesc" class="p-2.5 bg-slate-950 rounded-xl border border-amber-500/30 text-xs font-mono text-center text-amber-300">
                        <!-- Populated by setDimension() -->
                    </div>
                </div>
            `;
            setDimension(3);
        }

        function setDimension(d) {
            [0, 1, 2, 3].forEach(i => {
                const btn = document.getElementById(`dim${i}Btn`);
                if (btn) btn.className = (i === d) ? 'px-2 py-0.5 rounded bg-amber-600 text-white font-bold' : 'px-2 py-0.5 rounded bg-slate-800 text-slate-300';
            });

            const svg = document.getElementById('dimSvg');
            const desc = document.getElementById('dimDesc');
            if (!svg || !desc) return;

            if (d === 3) {
                desc.innerHTML = `<span class="text-amber-400 font-bold">SOLID (3D):</span> Has length, breadth, and thickness. Boundaries are 2D Surfaces.`;
                svg.innerHTML = `
                    <g transform="translate(60, 60)">
                        <rect x="0" y="40" width="120" height="120" fill="#b45309" fill-opacity="0.3" stroke="#f59e0b" stroke-width="2"/>
                        <polygon points="0,40 50,0 170,0 120,40" fill="#d97706" fill-opacity="0.4" stroke="#f59e0b" stroke-width="2"/>
                        <polygon points="120,40 170,0 170,120 120,160" fill="#78350f" fill-opacity="0.5" stroke="#f59e0b" stroke-width="2"/>
                    </g>
                `;
            } else if (d === 2) {
                desc.innerHTML = `<span class="text-rose-400 font-bold">SURFACE (2D):</span> Has length and breadth only. Boundaries are 1D Lines.`;
                svg.innerHTML = `
                    <g transform="translate(60, 60)">
                        <rect x="0" y="40" width="120" height="120" fill="#f43f5e" fill-opacity="0.25" stroke="#f43f5e" stroke-width="3"/>
                        <text x="35" y="105" fill="#f43f5e" font-size="12" font-weight="bold">2D Face</text>
                    </g>
                `;
            } else if (d === 1) {
                desc.innerHTML = `<span class="text-cyan-400 font-bold">LINE (1D):</span> Breadthless length. Boundaries/ends are 0D Points.`;
                svg.innerHTML = `
                    <g transform="translate(60, 60)">
                        <line x1="0" y1="100" x2="160" y2="100" stroke="#06b6d4" stroke-width="4"/>
                        <circle cx="0" cy="100" r="4" fill="#f8fafc"/>
                        <circle cx="160" cy="100" r="4" fill="#f8fafc"/>
                        <text x="30" y="85" fill="#06b6d4" font-size="12" font-weight="bold">1D Line Segment</text>
                    </g>
                `;
            } else {
                desc.innerHTML = `<span class="text-emerald-400 font-bold">POINT (0D):</span> 'That which has no part'—zero dimensions, only position.`;
                svg.innerHTML = `
                    <g transform="translate(150, 150)">
                        <circle cx="0" cy="0" r="7" fill="#10b981"/>
                        <circle cx="0" cy="0" r="16" fill="none" stroke="#10b981" stroke-width="2" class="animate-ping" opacity="0.6"/>
                        <text x="12" y="4" fill="#10b981" font-size="12" font-weight="bold">Point P (0D)</text>
                    </g>
                `;
            }
        }

        // SIMULATOR 8: Axiom vs Postulate Categorizer
        function renderSim8(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-xs text-center">
                        <span class="text-slate-400 block mb-1">Classify this statement:</span>
                        <div id="sim8Statement" class="text-amber-300 font-bold font-mono">
                            "A circle can be described with any centre and any radius."
                        </div>
                    </div>
                    <div class="flex items-center gap-3">
                        <button onclick="testSim8Choice('postulate')" class="flex-1 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition">
                            Geometric Postulate
                        </button>
                        <button onclick="testSim8Choice('axiom')" class="flex-1 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition">
                            Universal Axiom
                        </button>
                    </div>
                    <div id="sim8Result" class="p-2.5 rounded-xl border border-amber-500/30 bg-slate-950 text-xs font-mono text-center">
                        Click a button to test your classification!
                    </div>
                </div>
            `;
            window.sim8Index = 0;
            loadSim8Card();
        }

        function loadSim8Card() {
            const cards = [
                { q: "A circle can be described with any centre and any radius.", type: "postulate", exp: "Specific to geometry = Postulate 3." },
                { q: "The whole is greater than the part.", type: "axiom", exp: "Applies to numbers, volumes, and geometry = Axiom 5." },
                { q: "All right angles are equal to one another.", type: "postulate", exp: "Geometric assumption = Postulate 4." },
                { q: "If equals are added to equals, the wholes are equal.", type: "axiom", exp: "Universal mathematical truth = Axiom 2." }
            ];
            const item = cards[window.sim8Index % cards.length];
            document.getElementById('sim8Statement').textContent = `"${item.q}"`;
            window.currentSim8Item = item;
        }

        function testSim8Choice(ch) {
            const item = window.currentSim8Item;
            const res = document.getElementById('sim8Result');
            if (ch === item.type) {
                res.className = "p-2.5 rounded-xl border border-emerald-500/50 bg-emerald-950/40 text-emerald-300 text-xs font-mono text-center font-bold";
                res.innerHTML = `✓ CORRECT! ${item.exp}`;
                playSuccessSound();
                setTimeout(() => {
                    window.sim8Index++;
                    loadSim8Card();
                }, 1800);
            } else {
                res.className = "p-2.5 rounded-xl border border-rose-500/50 bg-rose-950/40 text-rose-300 text-xs font-mono text-center font-bold";
                res.innerHTML = `✗ Try Again! Hint: Is it strictly about geometry or all mathematics?`;
                playErrorSound();
            }
        }

        // SIMULATOR 9: Euclid's 7 Axioms Interactive Balance Scale
        function renderSim9(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="text-xs">
                        <label class="text-slate-400">Select Axiom to Demonstrate:</label>
                        <select id="axiomSelect" onchange="updateAxiomScale()" class="w-full mt-1 bg-slate-900 border border-slate-700 text-amber-300 rounded-lg p-1.5 font-mono">
                            <option value="1">Axiom 1: Things equal to same thing are equal (a=c, b=c ⇒ a=b)</option>
                            <option value="2">Axiom 2: If equals are added to equals, wholes are equal (a+c = b+c)</option>
                            <option value="3">Axiom 3: If equals are subtracted, remainders are equal (a-c = b-c)</option>
                            <option value="5">Axiom 5: The whole is greater than the part (Whole > Part)</option>
                            <option value="6">Axiom 6: Things double of the same things are equal (2a = 2b)</option>
                        </select>
                    </div>
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="scaleSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div id="scaleProofText" class="p-2.5 bg-slate-950 rounded-xl border border-amber-500/30 text-xs font-mono text-center text-emerald-400 font-bold">
                        <!-- Scale text -->
                    </div>
                </div>
            `;
            updateAxiomScale();
        }

        function updateAxiomScale() {
            const ax = document.getElementById('axiomSelect').value;
            const svg = document.getElementById('scaleSvg');
            const txt = document.getElementById('scaleProofText');
            if (!svg || !txt) return;

            if (ax === '1') {
                txt.textContent = "A = 10 kg, C = 10 kg and B = 10 kg, C = 10 kg ⇒ A = B (Perfect Balance!)";
            } else if (ax === '2') {
                txt.textContent = "Start: 5 kg = 5 kg. Add +3 kg to both sides ⇒ 8 kg = 8 kg (Still Balanced!)";
            } else if (ax === '3') {
                txt.textContent = "Start: 10 kg = 10 kg. Subtract -4 kg from both sides ⇒ 6 kg = 6 kg (Balanced!)";
            } else if (ax === '5') {
                txt.textContent = "Left: Whole (10 kg) vs Right: Part (3 kg) ⇒ Scale Tilts! Whole > Part.";
            } else {
                txt.textContent = "Double both equal weights: 2(6 kg) = 2(6 kg) ⇒ 12 kg = 12 kg (Balanced!)";
            }

            const tilt = (ax === '5') ? 15 : 0;
            const yLeft = 140 + tilt;
            const yRight = 140 - tilt;

            svg.innerHTML = `
                <!-- Balance Stand -->
                <line x1="150" y1="90" x2="150" y2="240" stroke="#64748b" stroke-width="4"/>
                <polygon points="120,240 180,240 150,220" fill="#475569"/>

                <!-- Beam -->
                <line x1="60" y1="${yLeft}" x2="240" y2="${yRight}" stroke="#f59e0b" stroke-width="4"/>
                <circle cx="150" cy="90" r="5" fill="#f8fafc"/>

                <!-- Left Pan -->
                <line x1="60" y1="${yLeft}" x2="60" y2="${yLeft + 50}" stroke="#94a3b8" stroke-width="1.5"/>
                <rect x="35" y="${yLeft + 50}" width="50" height="8" rx="3" fill="#cbd5e1"/>
                <rect x="45" y="${yLeft + 30}" width="30" height="20" rx="3" fill="#10b981"/>
                <text x="50" y="${yLeft + 45}" fill="#ffffff" font-size="10" font-weight="bold">${ax === '5' ? '10kg' : 'A'}</text>

                <!-- Right Pan -->
                <line x1="240" y1="${yRight}" x2="240" y2="${yRight + 50}" stroke="#94a3b8" stroke-width="1.5"/>
                <rect x="215" y="${yRight + 50}" width="50" height="8" rx="3" fill="#cbd5e1"/>
                <rect x="${ax === '5' ? 230 : 225}" y="${ax === '5' ? yRight + 38 : yRight + 30}" width="${ax === '5' ? 20 : 30}" height="${ax === '5' ? 12 : 20}" rx="3" fill="${ax === '5' ? '#f43f5e' : '#10b981'}"/>
                <text x="230" y="${yRight + 45}" fill="#ffffff" font-size="10" font-weight="bold">${ax === '5' ? '3kg' : 'B'}</text>
            `;
        }

        // SIMULATOR 10: Unique Line & Infinite Extension Ray Gun
        function renderSim10(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="rayGunSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="flex items-center justify-between gap-2">
                        <button onclick="toggleRayExtender()" id="rayBtn" class="flex-1 py-1.5 rounded-xl text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition">
                            ⚡ Fire Postulate 2 Extender
                        </button>
                    </div>
                    <div id="rayStatus" class="p-2.5 bg-slate-950 rounded-xl border border-amber-500/30 text-xs font-mono text-center text-amber-300">
                        Axiom 5.1: Exactly ONE unique line connects points P and Q!
                    </div>
                </div>
            `;
            window.raysExtended = false;
            drawRays();
        }

        function toggleRayExtender() {
            window.raysExtended = !window.raysExtended;
            const btn = document.getElementById('rayBtn');
            const st = document.getElementById('rayStatus');
            if (window.raysExtended) {
                btn.textContent = "Reset to Segment";
                st.innerHTML = `<span class="text-cyan-400 font-bold">Postulate 2 Activated:</span> Line segment produced indefinitely into an infinite line!`;
                playSuccessSound();
            } else {
                btn.textContent = "⚡ Fire Postulate 2 Extender";
                st.textContent = "Axiom 5.1: Exactly ONE unique line connects points P and Q!";
            }
            drawRays();
        }

        function drawRays() {
            const svg = document.getElementById('rayGunSvg');
            if (!svg) return;
            const ext = window.raysExtended;

            svg.innerHTML = `
                <!-- Background Grid -->
                <line x1="20" y1="150" x2="280" y2="150" stroke="#1e293b" stroke-width="1"/>
                <line x1="150" y1="20" x2="150" y2="280" stroke="#1e293b" stroke-width="1"/>

                <!-- Segment PQ or Extended Line -->
                ${ext ? `
                    <line x1="10" y1="210" x2="290" y2="90" stroke="#06b6d4" stroke-width="3"/>
                    <!-- Arrows -->
                    <polygon points="10,210 20,205 18,217" fill="#06b6d4"/>
                    <polygon points="290,90 280,95 282,83" fill="#06b6d4"/>
                ` : `
                    <line x1="80" y1="180" x2="220" y2="120" stroke="#f59e0b" stroke-width="3"/>
                `}

                <!-- Points P and Q -->
                <circle cx="80" cy="180" r="6" fill="#f59e0b"/>
                <text x="65" y="175" fill="#f59e0b" font-size="11" font-weight="bold">P</text>

                <circle cx="220" cy="120" r="6" fill="#f59e0b"/>
                <text x="230" y="125" fill="#f59e0b" font-size="11" font-weight="bold">Q</text>
            `;
        }

        // SIMULATOR 11: Universal Circle Compass & Right-Angle Superposition
        function renderSim11(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="compSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Postulate 3 Compass Radius:</span>
                            <span id="compRVal" class="text-amber-400 font-bold">60 units</span>
                        </label>
                        <input type="range" min="30" max="110" value="60" step="5" id="compRSlider" oninput="updateCompass()" class="w-full accent-amber-500">
                    </div>
                    <div class="p-2.5 bg-slate-950 rounded-xl border border-amber-500/30 text-xs font-mono text-center text-cyan-300">
                        Postulate 4: Every right angle (90°) superimposes perfectly onto any other right angle!
                    </div>
                </div>
            `;
            updateCompass();
        }

        function updateCompass() {
            const r = parseFloat(document.getElementById('compRSlider').value);
            document.getElementById('compRVal').textContent = `${r} units`;

            const svg = document.getElementById('compSvg');
            if (!svg) return;

            svg.innerHTML = `
                <!-- Concentric/Custom Circles -->
                <circle cx="150" cy="150" r="${r}" fill="#06b6d4" fill-opacity="0.15" stroke="#06b6d4" stroke-width="2.5"/>
                <circle cx="150" cy="150" r="4" fill="#f8fafc"/>
                <text x="155" y="145" fill="#94a3b8" font-size="10">Center (h,k)</text>

                <!-- Right Angles to Superimpose -->
                <g transform="translate(40, 40)">
                    <line x1="0" y1="40" x2="40" y2="40" stroke="#f43f5e" stroke-width="2"/>
                    <line x1="40" y1="40" x2="40" y2="0" stroke="#f43f5e" stroke-width="2"/>
                    <rect x="30" y="30" width="10" height="10" fill="none" stroke="#f43f5e"/>
                    <text x="5" y="30" fill="#f43f5e" font-size="9">90°</text>
                </g>

                <g transform="translate(220, 200) rotate(45)">
                    <line x1="0" y1="40" x2="40" y2="40" stroke="#10b981" stroke-width="2"/>
                    <line x1="40" y1="40" x2="40" y2="0" stroke="#10b981" stroke-width="2"/>
                    <rect x="30" y="30" width="10" height="10" fill="none" stroke="#10b981"/>
                    <text x="5" y="30" fill="#10b981" font-size="9">90°</text>
                </g>
            `;
        }

        // SIMULATOR 12: Euclid's 5th Postulate Transversal & Intersection Engine
        function renderSim12(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="post5Svg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Adjust Interior Angle Sum (∠1 + ∠2):</span>
                            <span id="post5SumVal" class="text-amber-400 font-bold">160° (< 180°)</span>
                        </label>
                        <input type="range" min="140" max="200" value="160" step="5" id="post5Slider" oninput="updatePost5()" class="w-full accent-amber-500">
                    </div>
                    <div id="post5Status" class="p-2.5 rounded-xl border text-xs font-mono text-center font-bold">
                        <!-- Populated by updatePost5() -->
                    </div>
                </div>
            `;
            updatePost5();
        }

        function updatePost5() {
            const sum = parseInt(document.getElementById('post5Slider').value);
            const status = document.getElementById('post5Status');

            if (sum < 180) {
                status.className = "p-2.5 rounded-xl border border-rose-500/50 bg-rose-950/40 text-rose-300 text-xs font-mono text-center font-bold";
                status.innerHTML = `Sum = ${sum}° < 180°: LINES INTERSECT on the Right!`;
                document.getElementById('post5SumVal').textContent = `${sum}° (< 180°)`;
            } else if (sum === 180) {
                status.className = "p-2.5 rounded-xl border border-emerald-500/50 bg-emerald-950/40 text-emerald-300 text-xs font-mono text-center font-bold";
                status.innerHTML = `Sum = 180°: PARALLEL LINES! Zero intersection.`;
                document.getElementById('post5SumVal').textContent = `180° (Parallel!)`;
            } else {
                status.className = "p-2.5 rounded-xl border border-cyan-500/50 bg-cyan-950/40 text-cyan-300 text-xs font-mono text-center font-bold";
                status.innerHTML = `Sum = ${sum}° > 180°: Lines diverge on right; intersect on the Left!`;
                document.getElementById('post5SumVal').textContent = `${sum}° (> 180°)`;
            }

            const svg = document.getElementById('post5Svg');
            if (!svg) return;

            const slopeOffset = (sum - 180) * 0.8;
            svg.innerHTML = `
                <!-- Transversal Line -->
                <line x1="80" y1="30" x2="120" y2="270" stroke="#f59e0b" stroke-width="2.5"/>
                <text x="70" y="25" fill="#f59e0b" font-size="10" font-weight="bold">Transversal t</text>

                <!-- Line 1 -->
                <line x1="20" y1="100" x2="280" y2="${100 + slopeOffset}" stroke="#38bdf8" stroke-width="2"/>
                <text x="20" y="90" fill="#38bdf8" font-size="10">Line l</text>

                <!-- Line 2 -->
                <line x1="20" y1="200" x2="280" y2="${200 - slopeOffset}" stroke="#34d399" stroke-width="2"/>
                <text x="20" y="220" fill="#34d399" font-size="10">Line m</text>

                <!-- Angle arcs -->
                <path d="M 110 100 A 20 20 0 0 1 95 125" fill="none" stroke="#f43f5e" stroke-width="2"/>
                <text x="115" y="125" fill="#f43f5e" font-size="10" font-weight="bold">∠1</text>

                <path d="M 125 180 A 20 20 0 0 1 110 200" fill="none" stroke="#f43f5e" stroke-width="2"/>
                <text x="125" y="195" fill="#f43f5e" font-size="10" font-weight="bold">∠2</text>
            `;
        }

        // SIMULATOR 13: Playfair's Parallel Line Beam Generator
        function renderSim13(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="playfairSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Rotate Beam through Point P:</span>
                            <span id="playfairDeg" class="text-amber-400 font-bold">0° (Parallel)</span>
                        </label>
                        <input type="range" min="-30" max="30" value="0" step="5" id="playfairSlider" oninput="updatePlayfair()" class="w-full accent-amber-500">
                    </div>
                    <div id="playfairStatus" class="p-2.5 rounded-xl border text-xs font-mono text-center font-bold">
                        <!-- Populated by updatePlayfair() -->
                    </div>
                </div>
            `;
            updatePlayfair();
        }

        function updatePlayfair() {
            const rot = parseInt(document.getElementById('playfairSlider').value);
            document.getElementById('playfairDeg').textContent = `${rot}°`;
            const st = document.getElementById('playfairStatus');

            if (rot === 0) {
                st.className = "p-2.5 rounded-xl border border-emerald-500/50 bg-emerald-950/40 text-emerald-300 text-xs font-mono text-center font-bold";
                st.innerHTML = `★ PLAYFAIR'S PARALLEL: Exactly ONE line through P is parallel to line l!`;
            } else {
                st.className = "p-2.5 rounded-xl border border-slate-800 bg-slate-950 text-slate-400 text-xs font-mono text-center";
                st.innerHTML = `Beam intersects line l at distance ≈ ${(200 / Math.tan(Math.abs(rot)*Math.PI/180)).toFixed(0)} units.`;
            }

            const svg = document.getElementById('playfairSvg');
            if (!svg) return;

            const rad = (rot * Math.PI) / 180;
            const x1 = 150 - 130 * Math.cos(rad);
            const y1 = 90 - 130 * Math.sin(rad);
            const x2 = 150 + 130 * Math.cos(rad);
            const y2 = 90 + 130 * Math.sin(rad);

            svg.innerHTML = `
                <!-- Fixed Line l -->
                <line x1="20" y1="210" x2="280" y2="210" stroke="#64748b" stroke-width="2.5"/>
                <text x="250" y="230" fill="#64748b" font-size="11" font-weight="bold">Line l</text>

                <!-- Rotatable Line m through P -->
                <line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${rot === 0 ? '#10b981' : '#f59e0b'}" stroke-width="${rot === 0 ? '3' : '2'}"/>

                <!-- Point P -->
                <circle cx="150" cy="90" r="6" fill="#f43f5e"/>
                <text x="145" y="75" fill="#f43f5e" font-size="11" font-weight="bold">Point P</text>
            `;
        }

        // SIMULATOR 14: Euclid Proposition 1 Step-by-Step Triangle Prover
        function renderSim14(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="prop1Svg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="flex items-center justify-between text-xs">
                        <span class="text-slate-400">Proposition 1 Step:</span>
                        <div class="flex gap-1">
                            <button onclick="setProp1Step(1)" id="pr1Btn" class="px-2 py-0.5 rounded bg-amber-600 text-white font-bold">1. AB</button>
                            <button onclick="setProp1Step(2)" id="pr2Btn" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">2. Circle A</button>
                            <button onclick="setProp1Step(3)" id="pr3Btn" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">3. Circle B</button>
                            <button onclick="setProp1Step(4)" id="pr4Btn" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">4. Proof</button>
                        </div>
                    </div>
                    <div id="prop1ProofText" class="p-2.5 bg-slate-950 rounded-xl border border-amber-500/30 text-xs font-mono text-center text-amber-300">
                        <!-- Populated by setProp1Step() -->
                    </div>
                </div>
            `;
            setProp1Step(1);
        }

        function setProp1Step(st) {
            [1, 2, 3, 4].forEach(i => {
                document.getElementById(`pr${i}Btn`).className = (i === st) ? 'px-2 py-0.5 rounded bg-amber-600 text-white font-bold' : 'px-2 py-0.5 rounded bg-slate-800 text-slate-300';
            });

            const txt = document.getElementById('prop1ProofText');
            const svg = document.getElementById('prop1Svg');
            if (!txt || !svg) return;

            const ax = 110, ay = 190;
            const bx = 190, by = 190;
            const cx = 150, cy = 190 - 80 * 0.866; // Equilateral height = 69.28 -> cy = 120.7

            if (st === 1) {
                txt.textContent = "Given finite line segment AB (Length = 80).";
                svg.innerHTML = `
                    <line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#f59e0b" stroke-width="3"/>
                    <circle cx="${ax}" cy="${ay}" r="4" fill="#f59e0b"/>
                    <circle cx="${bx}" cy="${by}" r="4" fill="#f59e0b"/>
                    <text x="${ax - 15}" y="${ay + 15}" fill="#f59e0b" font-size="10" font-weight="bold">A</text>
                    <text x="${bx + 8}" y="${ay + 15}" fill="#f59e0b" font-size="10" font-weight="bold">B</text>
                `;
            } else if (st === 2) {
                txt.textContent = "Postulate 3: Draw circle with center A and radius AB.";
                svg.innerHTML = `
                    <circle cx="${ax}" cy="${ay}" r="80" fill="none" stroke="#06b6d4" stroke-width="2"/>
                    <line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#f59e0b" stroke-width="2.5"/>
                    <circle cx="${ax}" cy="${ay}" r="4" fill="#f59e0b"/>
                    <circle cx="${bx}" cy="${by}" r="4" fill="#f59e0b"/>
                `;
            } else if (st === 3) {
                txt.textContent = "Postulate 3: Draw circle with center B and radius BA.";
                svg.innerHTML = `
                    <circle cx="${ax}" cy="${ay}" r="80" fill="none" stroke="#06b6d4" stroke-width="1.5"/>
                    <circle cx="${bx}" cy="${by}" r="80" fill="none" stroke="#a855f7" stroke-width="1.5"/>
                    <line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#f59e0b" stroke-width="2"/>
                    <circle cx="${cx}" cy="${cy}" r="5" fill="#f43f5e"/>
                    <text x="${cx - 5}" y="${cy - 8}" fill="#f43f5e" font-size="10" font-weight="bold">C</text>
                `;
            } else {
                txt.innerHTML = `<span class="text-emerald-400 font-bold">Axiom 1:</span> AC = AB & BC = AB ⇒ AC = BC = AB. Equilateral proven!`;
                svg.innerHTML = `
                    <polygon points="${ax},${ay} ${bx},${by} ${cx},${cy}" fill="#10b981" fill-opacity="0.25" stroke="#10b981" stroke-width="3"/>
                    <circle cx="${ax}" cy="${ay}" r="4" fill="#f59e0b"/>
                    <circle cx="${bx}" cy="${by}" r="4" fill="#f59e0b"/>
                    <circle cx="${cx}" cy="${cy}" r="5" fill="#f43f5e"/>
                    <text x="${cx - 5}" y="${cy - 8}" fill="#f43f5e" font-size="10" font-weight="bold">C</text>
                `;
                playSuccessSound();
            }
        }

        // SIMULATOR 15: Euclidean vs Spherical vs Hyperbolic Universe Comparer
        function renderSim15(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="flex items-center justify-between text-xs">
                        <span class="text-slate-400">Curvature:</span>
                        <div class="flex gap-1">
                            <button onclick="setGeomUniv('flat')" id="uFlatBtn" class="px-2 py-0.5 rounded bg-amber-600 text-white font-bold">Euclidean (Flat)</button>
                            <button onclick="setGeomUniv('sphere')" id="uSphBtn" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">Spherical (+)</button>
                            <button onclick="setGeomUniv('saddle')" id="uSadBtn" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">Hyperbolic (-)</button>
                        </div>
                    </div>
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="univSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div id="univReadout" class="p-2.5 bg-slate-950 rounded-xl border border-amber-500/30 text-xs font-mono text-center text-amber-300">
                        <!-- Populated by setGeomUniv() -->
                    </div>
                </div>
            `;
            setGeomUniv('flat');
        }

        function setGeomUniv(m) {
            ['flat', 'sphere', 'saddle'].forEach(k => {
                const b = document.getElementById(k === 'flat' ? 'uFlatBtn' : (k === 'sphere' ? 'uSphBtn' : 'uSadBtn'));
                if (b) b.className = (k === m) ? 'px-2 py-0.5 rounded bg-amber-600 text-white font-bold' : 'px-2 py-0.5 rounded bg-slate-800 text-slate-300';
            });

            const svg = document.getElementById('univSvg');
            const rd = document.getElementById('univReadout');
            if (!svg || !rd) return;

            if (m === 'flat') {
                rd.innerHTML = `
                    <div class="text-amber-400 font-bold">Flat Euclidean Plane (Zero Curvature)</div>
                    <div class="text-[11px] text-slate-300">Triangle Sum = 180° | Exactly 1 Parallel line through P</div>
                `;
                svg.innerHTML = `
                    <polygon points="60,200 240,200 150,70" fill="#f59e0b" fill-opacity="0.2" stroke="#f59e0b" stroke-width="2.5"/>
                    <text x="140" y="160" fill="#fef08a" font-size="11" font-weight="bold">Sum = 180°</text>
                `;
            } else if (m === 'sphere') {
                rd.innerHTML = `
                    <div class="text-rose-400 font-bold">Spherical Surface (Positive Curvature)</div>
                    <div class="text-[11px] text-slate-300">Triangle Sum > 180° (e.g. 270°) | ZERO Parallel lines (all intersect!)</div>
                `;
                svg.innerHTML = `
                    <!-- Sphere Sphere -->
                    <circle cx="150" cy="150" r="100" fill="#0f172a" stroke="#f43f5e" stroke-width="2"/>
                    <ellipse cx="150" cy="150" rx="100" ry="30" fill="none" stroke="#64748b" stroke-dasharray="3"/>
                    <path d="M 150 50 A 100 100 0 0 1 250 150 A 100 30 0 0 1 150 180 A 100 100 0 0 1 150 50" fill="#f43f5e" fill-opacity="0.25" stroke="#f43f5e" stroke-width="2.5"/>
                    <text x="160" y="130" fill="#fecdd3" font-size="11" font-weight="bold">Sum = 270°</text>
                `;
            } else {
                rd.innerHTML = `
                    <div class="text-cyan-400 font-bold">Hyperbolic Saddle Surface (Negative Curvature)</div>
                    <div class="text-[11px] text-slate-300">Triangle Sum < 180° | INFINITELY MANY Parallel lines through P</div>
                `;
                svg.innerHTML = `
                    <!-- Saddle Triangle -->
                    <path d="M 60 190 Q 150 170 240 190 Q 190 120 150 60 Q 110 120 60 190" fill="#06b6d4" fill-opacity="0.25" stroke="#06b6d4" stroke-width="2.5"/>
                    <text x="130" y="150" fill="#cffafe" font-size="11" font-weight="bold">Sum < 180°</text>
                `;
            }
        }

        // SIMULATOR 16: Axiomatic Sandbox & Logic Chain Verifier
        function renderSim16(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-xs">
                        <span class="text-slate-400 block mb-1">Prove Theorem: "Vertically opposite angles are equal"</span>
                        <div class="space-y-1.5 font-mono text-[11px]">
                            <div class="p-1.5 rounded bg-slate-900 border border-slate-800 text-amber-300">Step 1: ∠1 + ∠2 = 180° (Linear Pair Axiom)</div>
                            <div class="p-1.5 rounded bg-slate-900 border border-slate-800 text-amber-300">Step 2: ∠2 + ∠3 = 180° (Linear Pair Axiom)</div>
                            <div class="p-1.5 rounded bg-slate-900 border border-slate-800 text-cyan-300">Step 3: ∠1 + ∠2 = ∠2 + ∠3 (Axiom 1: Equals to 180°)</div>
                            <div class="p-1.5 rounded bg-slate-900 border border-emerald-500/40 text-emerald-300 font-bold">Step 4: Subtract ∠2 ⇒ ∠1 = ∠3 (Axiom 3: Subtract Equals)</div>
                        </div>
                    </div>
                    <div class="p-2.5 bg-slate-950 rounded-xl border border-amber-500/30 text-xs font-mono text-center text-emerald-400 font-bold">
                        ★ Q.E.D. (Quod Erat Demonstrandum) — What was to be demonstrated!
                    </div>
                </div>
            `;
        }

        // --- INITIALIZATION ---
        window.addEventListener('DOMContentLoaded', () => {
            renderCurrentSlide();
        });
    </script>
</body>
</html>
"""

    html_content = html_content.replace("__SLIDES_JSON__", slides_json).replace("__QUIZZES_JSON__", quizzes_json)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Generated {OUTPUT_PATH} ({len(html_content)} bytes)")

if __name__ == "__main__":
    generate_html()

