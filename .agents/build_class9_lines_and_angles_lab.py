# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 8
LINES AND ANGLES (Competencies CG-7, C-7.1, C-7.3, CG-9)
Generates public/animations/class9-lines-and-angles.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_lines_and_angles_data import SLIDES, QUIZZES

OUTPUT_PATH = "public/animations/class9-lines-and-angles.html"

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
    <title>NCERT Class 9 Mathematics • Lines and Angles Lab</title>
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
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col selection:bg-emerald-500 selection:text-white">

    <!-- Top Navigation Header -->
    <header class="bg-slate-900/90 backdrop-blur-md border-b border-slate-800 sticky top-0 z-40 px-4 py-2.5">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 flex items-center justify-center shadow-lg shadow-emerald-500/30">
                    <i data-lucide="triangle" class="w-5 h-5 text-white"></i>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">Class 9 Maths • Chapter 8</span>
                        <span id="currentBadge" class="hidden sm:inline-block text-xs text-teal-400 bg-teal-500/10 px-2 py-0.5 rounded border border-teal-500/20 font-semibold">CG-7 • Rays & Angles</span>
                    </div>
                    <h1 class="text-sm sm:text-base font-extrabold text-white tracking-tight">Lines and Angles Lab</h1>
                </div>
            </div>

            <!-- Central Slide Indicator -->
            <div class="flex items-center gap-2 bg-slate-950/80 px-3 py-1.5 rounded-xl border border-slate-800">
                <span class="text-xs text-slate-400">Slide</span>
                <span id="slideCounter" class="text-sm font-bold text-emerald-400 font-mono">1 / 20</span>
                <div class="w-20 sm:w-28 bg-slate-800 h-2 rounded-full overflow-hidden ml-1">
                    <div id="progressBar" class="bg-gradient-to-r from-emerald-500 to-teal-500 h-full w-[5%] transition-all duration-300"></div>
                </div>
            </div>

            <!-- Voice Controls & Speed -->
            <div class="flex items-center gap-2">
                <div class="flex items-center bg-slate-800/80 rounded-lg p-0.5 border border-slate-700">
                    <button onclick="changeSpeed(0.8)" id="spd08" class="px-2 py-1 text-[11px] rounded font-medium text-slate-300 hover:text-white transition">0.8x</button>
                    <button onclick="changeSpeed(1.0)" id="spd10" class="px-2 py-1 text-[11px] rounded font-bold bg-emerald-600 text-white transition">1.0x</button>
                    <button onclick="changeSpeed(1.2)" id="spd12" class="px-2 py-1 text-[11px] rounded font-medium text-slate-300 hover:text-white transition">1.2x</button>
                </div>
                <button onclick="toggleAudio()" id="voiceToggleBtn" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white transition shadow-md shadow-emerald-600/30">
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
                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-emerald-500 to-teal-600 p-0.5 shadow-md shadow-emerald-500/20">
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
                    <span class="text-xs font-bold text-emerald-400">Prof. Sophia</span>
                    <span class="text-[10px] text-slate-400">• Geometry & Angle Relationships Guide</span>
                </div>
                <p id="narrationText" class="text-xs sm:text-sm text-slate-200 truncate font-normal">
                    Welcome to Lines and Angles! Explore rays, linear pairs, parallel line theorems, and triangle angle constraints.
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
            <div class="bg-slate-900 border border-emerald-500/30 rounded-2xl max-w-xl w-full p-5 sm:p-6 shadow-2xl relative max-h-[85vh] overflow-y-auto">
                <div class="flex items-start justify-between gap-3 border-b border-slate-800 pb-3 mb-4">
                    <div class="flex items-center gap-2">
                        <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center">
                            <i data-lucide="check-square" class="w-4 h-4"></i>
                        </div>
                        <div>
                            <h3 class="text-sm font-bold text-white">Step-by-Step Mathematical Solution</h3>
                            <span id="modalQSubtitle" class="text-xs text-emerald-400 font-mono"></span>
                        </div>
                    </div>
                    <button onclick="closeSolutionModal()" class="p-1 rounded-lg hover:bg-slate-800 text-slate-400 hover:text-white transition">
                        <i data-lucide="x" class="w-5 h-5"></i>
                    </button>
                </div>
                <div class="mb-4 p-3 bg-slate-950 rounded-xl border border-slate-800 text-xs sm:text-sm text-slate-300 font-medium leading-relaxed" id="modalQuestionText">
                    <!-- Question text -->
                </div>
                <div class="p-4 bg-emerald-950/20 rounded-xl border border-emerald-500/20 text-xs sm:text-sm text-emerald-200 leading-relaxed font-mono space-y-2" id="modalSolutionText">
                    <!-- Solution derivation -->
                </div>
                <div class="mt-5 flex justify-end">
                    <button onclick="closeSolutionModal()" class="px-4 py-2 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition">
                        Understood & Close
                    </button>
                </div>
            </div>
        </div>

        <!-- Last Slide Notice Banner -->
        <div id="lastSlideNotice" class="hidden mt-6 p-4 rounded-xl bg-gradient-to-r from-emerald-950/60 via-slate-900 to-teal-950/60 border border-emerald-500/40 text-center">
            <div class="flex items-center justify-center gap-2 text-emerald-400 font-bold text-sm sm:text-base">
                <i data-lucide="check-circle" class="w-5 h-5"></i>
                <span>You have reached the last slide of this chapter</span>
            </div>
            <p class="text-xs text-slate-300 mt-1">
                Outstanding accomplishment! You have mastered rays, angle classifications, linear pairs, vertically opposite angles, parallel transversals, corresponding/alternate/interior angles, transitivity of parallelism, triangle angle sum proofs, exterior angles, and contradiction constraints in Lines and Angles.
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

            <button onclick="nextSlide()" id="nextBtn" class="flex items-center gap-2 px-5 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white shadow-lg shadow-emerald-600/30 transition">
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
                btn.className = "flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white transition shadow-md shadow-emerald-600/30";
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
                activeEl.className = "px-2 py-1 text-[11px] rounded font-bold bg-emerald-600 text-white transition";
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
            document.getElementById('currentBadge').textContent = slide.badge || "Lines and Angles";
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
                                <span class="text-xs font-bold text-emerald-400 font-mono">CONCEPT #${currNum}</span>
                                <h2 class="text-xl sm:text-2xl font-black text-white tracking-tight">${slide.title}</h2>
                                <p class="text-xs sm:text-sm text-slate-400 font-medium mt-0.5">${slide.subtitle}</p>
                            </div>
                            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 font-semibold">${slide.category}</span>
                        </div>

                        <!-- 2-Column Split: Theory on Left, Simulator on Right -->
                        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 items-start">
                            <!-- Left: Theory & Checkpoints -->
                            <div class="space-y-4">
                                <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800/90 shadow-lg">
                                    <h3 class="text-xs font-bold uppercase tracking-wider text-emerald-400 mb-2 flex items-center gap-1.5">
                                        <i data-lucide="book-open" class="w-4 h-4"></i>
                                        Conceptual Overview
                                    </h3>
                                    <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                                        ${slide.summary}
                                    </p>
                                </div>

                                <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800/90 shadow-lg">
                                    <h3 class="text-xs font-bold uppercase tracking-wider text-teal-400 mb-2.5 flex items-center gap-1.5">
                                        <i data-lucide="sparkles" class="w-4 h-4"></i>
                                        Key Mathematical Insights
                                    </h3>
                                    <ul class="text-xs text-slate-300 space-y-2">
                                        ${slide.key_points.map(kp => `
                                            <li class="flex items-start gap-2">
                                                <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-emerald-400 shrink-0 mt-0.5"></i>
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
                                                        <button onclick="checkCheckpoint(${cIdx}, ${oIdx}, ${cp.ans})" id="cp_${cIdx}_${oIdx}" class="w-full text-left text-xs px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-800 hover:border-emerald-500/50 text-slate-300 transition flex items-center justify-between">
                                                            <span>${opt}</span>
                                                            <span id="cp_ind_${cIdx}_${oIdx}" class="hidden font-bold text-xs"></span>
                                                        </button>
                                                    `).join('')}
                                                </div>
                                                <div id="cp_exp_${cIdx}" class="hidden text-[11px] p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-emerald-200">
                                                    ${cp.explanation}
                                                </div>
                                            </div>
                                        `).join('')}
                                    </div>
                                </div>
                            </div>

                            <!-- Right: Bespoke Interactive Simulator -->
                            <div class="p-5 rounded-2xl bg-slate-900/90 border border-emerald-500/30 shadow-xl flex flex-col justify-between min-h-[460px]">
                                <div>
                                    <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
                                        <div class="flex items-center gap-2">
                                            <div class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></div>
                                            <h4 class="text-xs sm:text-sm font-bold text-emerald-300">${slide.sim_title}</h4>
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
                                            <span class="text-xs font-bold text-emerald-400 font-mono">Question ${q.id}</span>
                                            <button onclick="showSolution(${currentSlideIndex}, ${qIdx})" class="px-2.5 py-1 rounded-lg text-[10px] font-bold bg-amber-500/10 hover:bg-amber-500/20 text-amber-300 border border-amber-500/30 transition flex items-center gap-1.5 shadow-sm">
                                                <i data-lucide="eye" class="w-3.5 h-3.5"></i>
                                                View Solution
                                            </button>
                                        </div>
                                        <p class="text-xs sm:text-sm text-slate-200 font-medium mb-3">${q.q}</p>
                                        <div class="space-y-1.5 mb-2">
                                            ${q.options.map((opt, oIdx) => `
                                                <button onclick="answerQuiz(${q.id}, ${oIdx}, ${q.ans})" id="quiz_${q.id}_${oIdx}" class="w-full text-left text-xs px-3 py-2 rounded-xl bg-slate-950/80 border border-slate-800 hover:border-emerald-500/50 text-slate-300 transition flex items-center justify-between">
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
                    ? (isQuiz ? 'bg-amber-400 ring-2 ring-amber-400/50 scale-125' : 'bg-emerald-400 ring-2 ring-emerald-400/50 scale-125')
                    : (isQuiz ? 'bg-amber-900/60 hover:bg-amber-600' : 'bg-slate-700 hover:bg-slate-500');
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

        // SIMULATOR 1: Ray Spinner & Angle Generator
        function renderSim1(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="raySpinSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Rotate Ray OB (Measure θ):</span>
                            <span id="rayAngleVal" class="text-emerald-400 font-bold">50°</span>
                        </label>
                        <input type="range" min="0" max="360" value="50" step="5" id="rayAngleSlider" oninput="updateRaySpinner()" class="w-full accent-emerald-500">
                    </div>
                    <div id="rayAngleReadout" class="p-2.5 bg-slate-950 rounded-xl border border-emerald-500/30 text-xs font-mono text-center text-emerald-300">
                        Angle ∠AOB = 50° | Vertex O(0,0), Arms OA & OB
                    </div>
                </div>
            `;
            updateRaySpinner();
        }

        function updateRaySpinner() {
            const deg = parseInt(document.getElementById('rayAngleSlider').value);
            document.getElementById('rayAngleVal').textContent = `${deg}°`;
            document.getElementById('rayAngleReadout').textContent = `Angle ∠AOB = ${deg}° | Vertex O(0,0), Arms OA & OB`;

            const svg = document.getElementById('raySpinSvg');
            if (!svg) return;

            const cx = 150, cy = 150, r = 110;
            const ax = cx + r, ay = cy;
            const rad = (deg * Math.PI) / 180;
            const bx = cx + r * Math.cos(rad);
            const by = cy - r * Math.sin(rad);

            const largeArc = deg > 180 ? 1 : 0;
            const pathD = deg === 360
                ? `M ${cx} ${cy} m -${r}, 0 a ${r},${r} 0 1,0 ${r*2},0 a ${r},${r} 0 1,0 -${r*2},0`
                : (deg === 0 ? '' : `M ${cx} ${cy} L ${ax} ${ay} A ${r} ${r} 0 ${largeArc} 0 ${bx} ${by} Z`);

            svg.innerHTML = `
                <!-- Dial Rim -->
                <circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="#1e293b" stroke-width="1.5" stroke-dasharray="4"/>

                <!-- Interior Shading -->
                ${pathD ? `<path d="${pathD}" fill="#10b981" fill-opacity="0.2"/>` : ''}

                <!-- Arm OA (Fixed Base) -->
                <line x1="${cx}" y1="${cy}" x2="${ax + 15}" y2="${ay}" stroke="#38bdf8" stroke-width="3"/>
                <polygon points="${ax + 15},${ay} ${ax + 5},${ay - 4} ${ax + 5},${ay + 4}" fill="#38bdf8"/>
                <text x="${ax + 20}" y="${ay + 4}" fill="#38bdf8" font-size="11" font-weight="bold">A</text>

                <!-- Arm OB (Rotatable) -->
                <line x1="${cx}" y1="${cy}" x2="${bx}" y2="${by}" stroke="#f59e0b" stroke-width="3"/>
                <text x="${bx + 8}" y="${by + 4}" fill="#f59e0b" font-size="11" font-weight="bold">B</text>

                <!-- Vertex O -->
                <circle cx="${cx}" cy="${cy}" r="5" fill="#f8fafc"/>
                <text x="${cx - 15}" y="${cy + 15}" fill="#94a3b8" font-size="11" font-weight="bold">O</text>
            `;
        }

        // SIMULATOR 2: Interactive Angle Gauge & Dynamic Classifier
        function renderSim2(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="gaugeSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Adjust Angle Magnitude (θ):</span>
                            <span id="gaugeDegVal" class="text-emerald-400 font-bold">60°</span>
                        </label>
                        <input type="range" min="0" max="360" value="60" step="5" id="gaugeSlider" oninput="updateAngleGauge()" class="w-full accent-emerald-500">
                    </div>
                    <div id="gaugeBadge" class="p-2.5 rounded-xl border text-xs font-mono text-center font-bold">
                        <!-- Populated by updateAngleGauge() -->
                    </div>
                </div>
            `;
            updateAngleGauge();
        }

        function updateAngleGauge() {
            const deg = parseInt(document.getElementById('gaugeSlider').value);
            document.getElementById('gaugeDegVal').textContent = `${deg}°`;
            const badge = document.getElementById('gaugeBadge');

            if (deg === 0) {
                badge.className = "p-2.5 rounded-xl border border-slate-700 bg-slate-900 text-slate-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `ZERO ANGLE (θ = 0°)`;
            } else if (deg < 90) {
                badge.className = "p-2.5 rounded-xl border border-emerald-500/50 bg-emerald-950/40 text-emerald-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `ACUTE ANGLE (0° < θ < 90°)`;
            } else if (deg === 90) {
                badge.className = "p-2.5 rounded-xl border border-cyan-500/50 bg-cyan-950/40 text-cyan-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `★ RIGHT ANGLE (θ = 90°, Exactly 1 Quarter Turn)`;
            } else if (deg < 180) {
                badge.className = "p-2.5 rounded-xl border border-amber-500/50 bg-amber-950/40 text-amber-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `OBTUSE ANGLE (90° < θ < 180°)`;
            } else if (deg === 180) {
                badge.className = "p-2.5 rounded-xl border border-rose-500/50 bg-rose-950/40 text-rose-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `★ STRAIGHT ANGLE (θ = 180°, Exactly 2 Right Angles)`;
            } else if (deg < 360) {
                badge.className = "p-2.5 rounded-xl border border-violet-500/50 bg-violet-950/40 text-violet-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `REFLEX ANGLE (180° < θ < 360°)`;
            } else {
                badge.className = "p-2.5 rounded-xl border border-emerald-500/50 bg-emerald-950/40 text-emerald-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `★ COMPLETE ANGLE (θ = 360°, One Full Turn)`;
            }

            const svg = document.getElementById('gaugeSvg');
            if (!svg) return;

            const cx = 150, cy = 150, r = 100;
            const ax = cx + r, ay = cy;
            const rad = (deg * Math.PI) / 180;
            const bx = cx + r * Math.cos(rad);
            const by = cy - r * Math.sin(rad);

            svg.innerHTML = `
                <circle cx="${cx}" cy="${cy}" r="${r}" fill="#0f172a" stroke="#334155" stroke-width="2"/>
                <line x1="${cx}" y1="${cy}" x2="${ax}" y2="${ay}" stroke="#38bdf8" stroke-width="3"/>
                <line x1="${cx}" y1="${cy}" x2="${bx}" y2="${by}" stroke="#10b981" stroke-width="3"/>
                <circle cx="${cx}" cy="${cy}" r="4" fill="#f8fafc"/>
            `;
        }

        // SIMULATOR 3: Twin Angle Complement & Supplement Balancer
        function renderSim3(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="compSuppSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Adjust Angle θ:</span>
                            <span id="csThetaVal" class="text-emerald-400 font-bold">35°</span>
                        </label>
                        <input type="range" min="10" max="80" value="35" step="5" id="csThetaSlider" oninput="updateCompSupp()" class="w-full accent-emerald-500">
                    </div>
                    <div id="csCalculations" class="p-2.5 bg-slate-950 rounded-xl border border-emerald-500/30 text-xs font-mono grid grid-cols-2 gap-2 text-center">
                        <!-- Populated by updateCompSupp() -->
                    </div>
                </div>
            `;
            updateCompSupp();
        }

        function updateCompSupp() {
            const th = parseInt(document.getElementById('csThetaSlider').value);
            document.getElementById('csThetaVal').textContent = `${th}°`;

            const comp = 90 - th;
            const supp = 180 - th;

            document.getElementById('csCalculations').innerHTML = `
                <div class="p-1.5 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">Complement: 90° - θ</span>
                    <span class="text-cyan-300 font-bold">${comp}°</span>
                </div>
                <div class="p-1.5 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">Supplement: 180° - θ</span>
                    <span class="text-amber-300 font-bold">${supp}°</span>
                </div>
            `;

            const svg = document.getElementById('compSuppSvg');
            if (!svg) return;

            const rad = (th * Math.PI) / 180;
            const r = 90;
            const cx = 150, cy = 180;
            const armX = cx + r * Math.cos(rad);
            const armY = cy - r * Math.sin(rad);

            svg.innerHTML = `
                <!-- Straight Line for Supplement -->
                <line x1="30" y1="180" x2="270" y2="180" stroke="#64748b" stroke-width="2"/>
                <line x1="150" y1="180" x2="150" y2="90" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3"/>

                <!-- Middle Shared Ray -->
                <line x1="150" y1="180" x2="${armX}" y2="${armY}" stroke="#10b981" stroke-width="3"/>

                <circle cx="150" cy="180" r="4" fill="#f8fafc"/>

                <text x="180" y="165" fill="#10b981" font-size="11" font-weight="bold">θ = ${th}°</text>
                <text x="75" y="165" fill="#f59e0b" font-size="11" font-weight="bold">Supp = ${supp}°</text>
                <text x="160" y="115" fill="#06b6d4" font-size="11" font-weight="bold">Comp = ${comp}°</text>
            `;
        }

        // SIMULATOR 4: Linear Pair Dynamic Beam Visualizer
        function renderSim4(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="linPairSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Tilt Ray OC (∠BOC):</span>
                            <span id="lpAngleVal" class="text-emerald-400 font-bold">65°</span>
                        </label>
                        <input type="range" min="20" max="160" value="65" step="5" id="lpSlider" oninput="updateLinearPair()" class="w-full accent-emerald-500">
                    </div>
                    <div id="lpFormula" class="p-2.5 bg-slate-950 rounded-xl border border-emerald-500/30 text-xs font-mono text-center text-emerald-300 font-bold">
                        Axiom 6.1: ∠AOC (115°) + ∠BOC (65°) = 180°
                    </div>
                </div>
            `;
            updateLinearPair();
        }

        function updateLinearPair() {
            const bAngle = parseInt(document.getElementById('lpSlider').value);
            const aAngle = 180 - bAngle;
            document.getElementById('lpAngleVal').textContent = `${bAngle}°`;
            document.getElementById('lpFormula').textContent = `Axiom 6.1: ∠AOC (${aAngle}°) + ∠BOC (${bAngle}°) = 180°`;

            const svg = document.getElementById('linPairSvg');
            if (!svg) return;

            const cx = 150, cy = 180, r = 100;
            const rad = (bAngle * Math.PI) / 180;
            const cxPt = cx + r * Math.cos(rad);
            const cyPt = cy - r * Math.sin(rad);

            svg.innerHTML = `
                <!-- Line AB -->
                <line x1="30" y1="180" x2="270" y2="180" stroke="#38bdf8" stroke-width="3"/>
                <text x="25" y="200" fill="#38bdf8" font-size="11" font-weight="bold">A</text>
                <text x="265" y="200" fill="#38bdf8" font-size="11" font-weight="bold">B</text>

                <!-- Standing Ray OC -->
                <line x1="${cx}" y1="${cy}" x2="${cxPt}" y2="${cyPt}" stroke="#f59e0b" stroke-width="3"/>
                <circle cx="${cx}" cy="${cy}" r="4" fill="#f8fafc"/>
                <text x="${cx - 5}" y="${cy + 15}" fill="#94a3b8" font-size="10">O</text>
                <text x="${cxPt - 5}" y="${cyPt - 8}" fill="#f59e0b" font-size="11" font-weight="bold">C</text>

                <text x="180" y="165" fill="#10b981" font-size="11" font-weight="bold">${bAngle}°</text>
                <text x="80" y="165" fill="#f43f5e" font-size="11" font-weight="bold">${aAngle}°</text>
            `;
        }

        // SIMULATOR 5: Straight Line Alignment Verifier
        function renderSim5(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="alignSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Adjust Sum (∠1 + ∠2):</span>
                            <span id="alignSumVal" class="text-emerald-400 font-bold">180°</span>
                        </label>
                        <input type="range" min="150" max="210" value="180" step="5" id="alignSlider" oninput="updateAlign()" class="w-full accent-emerald-500">
                    </div>
                    <div id="alignBadge" class="p-2.5 rounded-xl border text-xs font-mono text-center font-bold">
                        <!-- Populated by updateAlign() -->
                    </div>
                </div>
            `;
            updateAlign();
        }

        function updateAlign() {
            const sum = parseInt(document.getElementById('alignSlider').value);
            document.getElementById('alignSumVal').textContent = `${sum}°`;
            const badge = document.getElementById('alignBadge');

            if (sum === 180) {
                badge.className = "p-2.5 rounded-xl border border-emerald-500/50 bg-emerald-950/40 text-emerald-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `★ AXIOM 6.2 VERIFIED: Sum = 180° ⇒ Non-common arms form a STRAIGHT LINE!`;
            } else {
                badge.className = "p-2.5 rounded-xl border border-rose-500/50 bg-rose-950/30 text-rose-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `Sum = ${sum}° ≠ 180°: Arms do NOT form a straight line (Bent at vertex O)`;
            }

            const svg = document.getElementById('alignSvg');
            if (!svg) return;

            const bend = (sum - 180) * 0.7;
            const isStraight = (sum === 180);

            svg.innerHTML = `
                <!-- Arm OA -->
                <line x1="50" y1="${150 + bend}" x2="150" y2="150" stroke="${isStraight ? '#10b981' : '#f43f5e'}" stroke-width="3"/>
                <!-- Arm OB -->
                <line x1="150" y1="150" x2="250" y2="150" stroke="${isStraight ? '#10b981' : '#f43f5e'}" stroke-width="3"/>
                <!-- Ray OC -->
                <line x1="150" y1="150" x2="150" y2="60" stroke="#f59e0b" stroke-width="2.5"/>

                <circle cx="150" cy="150" r="5" fill="#f8fafc"/>
                <text x="145" y="170" fill="#94a3b8" font-size="10">O</text>
            `;
        }

        // SIMULATOR 6: Radial Angle Wheel & 360° Sum Engine
        function renderSim6(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="wheelSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="flex items-center justify-between text-xs">
                        <span class="text-slate-400">Number of Equal Sectors:</span>
                        <div class="flex gap-1.5">
                            <button onclick="setWheelSectors(4)" id="w4Btn" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">4 (90°)</button>
                            <button onclick="setWheelSectors(5)" id="w5Btn" class="px-2 py-0.5 rounded bg-emerald-600 text-white font-bold">5 (72°)</button>
                            <button onclick="setWheelSectors(6)" id="w6Btn" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">6 (60°)</button>
                        </div>
                    </div>
                    <div id="wheelStatus" class="p-2.5 bg-slate-950 rounded-xl border border-emerald-500/30 text-xs font-mono text-center text-emerald-300">
                        Sum around point = 5 × 72° = 360° (Complete Angle)
                    </div>
                </div>
            `;
            setWheelSectors(5);
        }

        function setWheelSectors(n) {
            [4, 5, 6].forEach(i => {
                document.getElementById(`w${i}Btn`).className = (i === n) ? 'px-2 py-0.5 rounded bg-emerald-600 text-white font-bold' : 'px-2 py-0.5 rounded bg-slate-800 text-slate-300';
            });
            const deg = 360 / n;
            document.getElementById('wheelStatus').textContent = `Sum around point = ${n} × ${deg}° = 360° (Complete Angle)`;

            const svg = document.getElementById('wheelSvg');
            if (!svg) return;

            const cx = 150, cy = 150, r = 100;
            let lines = '';
            for (let i = 0; i < n; i++) {
                const rad = (i * deg * Math.PI) / 180;
                const x = cx + r * Math.cos(rad);
                const y = cy - r * Math.sin(rad);
                lines += `<line x1="${cx}" y1="${cy}" x2="${x}" y2="${y}" stroke="#10b981" stroke-width="2"/>`;
            }

            svg.innerHTML = `
                <circle cx="${cx}" cy="${cy}" r="${r}" fill="#0f172a" stroke="#334155" stroke-width="2"/>
                ${lines}
                <circle cx="${cx}" cy="${cy}" r="5" fill="#f59e0b"/>
            `;
        }

        // SIMULATOR 7: Scissors Mechanism & Vertically Opposite Angle Prover
        function renderSim7(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="scissorSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Scissors Opening Angle (θ):</span>
                            <span id="sciAngleVal" class="text-emerald-400 font-bold">50°</span>
                        </label>
                        <input type="range" min="20" max="80" value="50" step="5" id="sciSlider" oninput="updateScissors()" class="w-full accent-emerald-500">
                    </div>
                    <div id="sciProofDisplay" class="p-2.5 bg-slate-950 rounded-xl border border-emerald-500/30 text-xs font-mono text-center text-emerald-300 font-bold">
                        Theorem 6.1: ∠1 = ∠3 = 50° & ∠2 = ∠4 = 130°
                    </div>
                </div>
            `;
            updateScissors();
        }

        function updateScissors() {
            const deg = parseInt(document.getElementById('sciSlider').value);
            const supp = 180 - deg;
            document.getElementById('sciAngleVal').textContent = `${deg}°`;
            document.getElementById('sciProofDisplay').textContent = `Theorem 6.1: ∠1 = ∠3 = ${deg}° & ∠2 = ∠4 = ${supp}°`;

            const svg = document.getElementById('scissorSvg');
            if (!svg) return;

            const cx = 150, cy = 150, len = 120;
            const rad = (deg * Math.PI) / 360;

            const x1 = cx - len * Math.cos(rad), y1 = cy - len * Math.sin(rad);
            const x2 = cx + len * Math.cos(rad), y2 = cy + len * Math.sin(rad);

            const x3 = cx - len * Math.cos(rad), y3 = cy + len * Math.sin(rad);
            const x4 = cx + len * Math.cos(rad), y4 = cy - len * Math.sin(rad);

            svg.innerHTML = `
                <!-- Line 1 -->
                <line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#38bdf8" stroke-width="3"/>
                <!-- Line 2 -->
                <line x1="${x3}" y1="${y3}" x2="${x4}" y2="${y4}" stroke="#f59e0b" stroke-width="3"/>

                <circle cx="${cx}" cy="${cy}" r="5" fill="#f8fafc"/>

                <text x="210" y="155" fill="#10b981" font-size="11" font-weight="bold">∠1=${deg}°</text>
                <text x="50" y="155" fill="#10b981" font-size="11" font-weight="bold">∠3=${deg}°</text>
                <text x="135" y="80" fill="#f43f5e" font-size="11" font-weight="bold">∠2=${supp}°</text>
                <text x="135" y="230" fill="#f43f5e" font-size="11" font-weight="bold">∠4=${supp}°</text>
            `;
        }

        // SIMULATOR 8: Linear Pair Bisector Orthogonality Tool
        function renderSim8(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="bisectorSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Tilt Center Ray OC:</span>
                            <span id="bisectAngleVal" class="text-emerald-400 font-bold">70°</span>
                        </label>
                        <input type="range" min="30" max="150" value="70" step="5" id="bisectSlider" oninput="updateBisectors()" class="w-full accent-emerald-500">
                    </div>
                    <div class="p-2.5 bg-slate-950 rounded-xl border border-emerald-500/30 text-xs font-mono text-center text-emerald-400 font-bold">
                        ★ PROVEN: Bisector OE ⊥ Bisector OF (Enclosed Angle is ALWAYS 90°!)
                    </div>
                </div>
            `;
            updateBisectors();
        }

        function updateBisectors() {
            const bAng = parseInt(document.getElementById('bisectSlider').value);
            document.getElementById('bisectAngleVal').textContent = `${bAng}°`;

            const svg = document.getElementById('bisectorSvg');
            if (!svg) return;

            const cx = 150, cy = 180, r = 100;
            const radOC = (bAng * Math.PI) / 180;
            const radOE = (bAng / 2 * Math.PI) / 180;
            const radOF = ((bAng + (180 - bAng)/2) * Math.PI) / 180;

            const xC = cx + r * Math.cos(radOC), yC = cy - r * Math.sin(radOC);
            const xE = cx + r * Math.cos(radOE), yE = cy - r * Math.sin(radOE);
            const xF = cx + r * Math.cos(radOF), yF = cy - r * Math.sin(radOF);

            svg.innerHTML = `
                <!-- Line AB -->
                <line x1="30" y1="180" x2="270" y2="180" stroke="#64748b" stroke-width="2"/>
                <!-- Ray OC -->
                <line x1="${cx}" y1="${cy}" x2="${xC}" y2="${yC}" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3"/>

                <!-- Bisectors OE and OF -->
                <line x1="${cx}" y1="${cy}" x2="${xE}" y2="${yE}" stroke="#10b981" stroke-width="3"/>
                <line x1="${cx}" y1="${cy}" x2="${xF}" y2="${yF}" stroke="#10b981" stroke-width="3"/>

                <text x="${xE + 5}" y="${yE}" fill="#10b981" font-size="10" font-weight="bold">OE</text>
                <text x="${xF - 15}" y="${yF}" fill="#10b981" font-size="10" font-weight="bold">OF</text>

                <!-- Right Angle Marker -->
                <circle cx="${cx}" cy="${cy}" r="4" fill="#f8fafc"/>
                <text x="135" y="140" fill="#f59e0b" font-size="12" font-weight="bold">90°</text>
            `;
        }

        // SIMULATOR 9: Transversal 8-Angle Color-Coded Inspector
        function renderSim9(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="grid grid-cols-2 gap-1.5 text-[11px] font-mono">
                        <button onclick="highlight8Angles('corr')" id="hCorrBtn" class="p-1.5 rounded bg-emerald-600 text-white font-bold">Corresponding</button>
                        <button onclick="highlight8Angles('alt')" id="hAltBtn" class="p-1.5 rounded bg-slate-800 text-slate-300">Alt. Interior</button>
                        <button onclick="highlight8Angles('co')" id="hCoBtn" class="p-1.5 rounded bg-slate-800 text-slate-300">Co-Interior</button>
                        <button onclick="highlight8Angles('vert')" id="hVertBtn" class="p-1.5 rounded bg-slate-800 text-slate-300">Vert. Opposite</button>
                    </div>
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="transSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div id="trans8Info" class="p-2.5 bg-slate-950 rounded-xl border border-emerald-500/30 text-xs font-mono text-center text-emerald-300">
                        <!-- Populated by highlight8Angles() -->
                    </div>
                </div>
            `;
            highlight8Angles('corr');
        }

        function highlight8Angles(mode) {
            ['corr', 'alt', 'co', 'vert'].forEach(k => {
                const b = document.getElementById(`h${k.charAt(0).toUpperCase() + k.slice(1)}Btn`);
                if (b) b.className = (k === mode) ? 'p-1.5 rounded bg-emerald-600 text-white font-bold' : 'p-1.5 rounded bg-slate-800 text-slate-300';
            });

            const info = document.getElementById('trans8Info');
            const svg = document.getElementById('transSvg');
            if (!info || !svg) return;

            if (mode === 'corr') {
                info.innerHTML = `Corresponding Angles: <span class="text-emerald-400 font-bold">(1,5), (2,6), (3,7), (4,8)</span> [Equal]`;
            } else if (mode === 'alt') {
                info.innerHTML = `Alternate Interior Angles: <span class="text-cyan-400 font-bold">(3,5) and (4,6)</span> [Z-Pattern, Equal]`;
            } else if (mode === 'co') {
                info.innerHTML = `Co-Interior Angles: <span class="text-rose-400 font-bold">(4,5) and (3,6)</span> [C-Pattern, Sum = 180°]`;
            } else {
                info.innerHTML = `Vertically Opposite Angles: <span class="text-amber-400 font-bold">(1,3), (2,4), (5,7), (6,8)</span> [Equal]`;
            }

            svg.innerHTML = `
                <!-- Parallel Lines l and m -->
                <line x1="30" y1="100" x2="270" y2="100" stroke="#64748b" stroke-width="2.5"/>
                <line x1="30" y1="200" x2="270" y2="200" stroke="#64748b" stroke-width="2.5"/>
                <!-- Transversal Line t -->
                <line x1="90" y1="30" x2="210" y2="270" stroke="#f59e0b" stroke-width="2.5"/>

                <!-- Top Intersection Angles 1,2,3,4 -->
                <text x="135" y="85" fill="#f8fafc" font-size="10" font-weight="bold">1</text>
                <text x="165" y="85" fill="#f8fafc" font-size="10" font-weight="bold">2</text>
                <text x="165" y="125" fill="#f8fafc" font-size="10" font-weight="bold">3</text>
                <text x="135" y="125" fill="#f8fafc" font-size="10" font-weight="bold">4</text>

                <!-- Bottom Intersection Angles 5,6,7,8 -->
                <text x="185" y="185" fill="#f8fafc" font-size="10" font-weight="bold">5</text>
                <text x="215" y="185" fill="#f8fafc" font-size="10" font-weight="bold">6</text>
                <text x="215" y="225" fill="#f8fafc" font-size="10" font-weight="bold">7</text>
                <text x="185" y="225" fill="#f8fafc" font-size="10" font-weight="bold">8</text>
            `;
        }

        // SIMULATOR 10: T-Square & Parallel Glide Simulator
        function renderSim10(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="tsquareSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Slide T-Square along Ruler:</span>
                            <span id="tsquareYVal" class="text-emerald-400 font-bold">Position Y</span>
                        </label>
                        <input type="range" min="60" max="220" value="130" step="5" id="tsquareSlider" oninput="updateTSquare()" class="w-full accent-emerald-500">
                    </div>
                    <div class="p-2.5 bg-slate-950 rounded-xl border border-emerald-500/30 text-xs font-mono text-center text-emerald-300">
                        Axiom 6.4: Constant 90° corresponding angle guarantees parallel lines!
                    </div>
                </div>
            `;
            updateTSquare();
        }

        function updateTSquare() {
            const y = parseInt(document.getElementById('tsquareSlider').value);
            const svg = document.getElementById('tsquareSvg');
            if (!svg) return;

            svg.innerHTML = `
                <!-- Vertical Drawing Board Edge (Ruler) -->
                <rect x="30" y="20" width="20" height="260" fill="#334155" stroke="#64748b"/>
                <text x="20" y="290" fill="#64748b" font-size="9">Ruler</text>

                <!-- Reference Horizontal Line 1 -->
                <line x1="50" y1="60" x2="270" y2="60" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3"/>

                <!-- Sliding T-Square Blade -->
                <rect x="50" y="${y - 8}" width="220" height="16" fill="#10b981" fill-opacity="0.3" stroke="#10b981" stroke-width="2"/>
                <rect x="25" y="${y - 25}" width="25" height="50" rx="3" fill="#047857"/>

                <!-- 90° Angle Marker -->
                <rect x="50" y="${y - 18}" width="10" height="10" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
                <text x="65" y="${y - 5}" fill="#f59e0b" font-size="9" font-weight="bold">90°</text>
            `;
        }

        // SIMULATOR 11: The "Z-Pattern" Alternate Interior Angle Prover
        function renderSim11(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="zPatternSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Adjust Transversal Angle:</span>
                            <span id="zAngleVal" class="text-emerald-400 font-bold">55°</span>
                        </label>
                        <input type="range" min="35" max="75" value="55" step="5" id="zSlider" oninput="updateZPattern()" class="w-full accent-emerald-500">
                    </div>
                    <div class="p-2.5 bg-slate-950 rounded-xl border border-emerald-500/30 text-xs font-mono text-center text-emerald-400 font-bold">
                        ★ Z-PATTERN: Alternate Interior Angles are ALWAYS EQUAL!
                    </div>
                </div>
            `;
            updateZPattern();
        }

        function updateZPattern() {
            const ang = parseInt(document.getElementById('zSlider').value);
            document.getElementById('zAngleVal').textContent = `${ang}°`;

            const svg = document.getElementById('zPatternSvg');
            if (!svg) return;

            const rad = (ang * Math.PI) / 180;
            const dy = 100;
            const dx = dy / Math.tan(rad);

            const x1 = 150 - dx/2, y1 = 100;
            const x2 = 150 + dx/2, y2 = 200;

            svg.innerHTML = `
                <!-- Parallel Lines -->
                <line x1="30" y1="100" x2="270" y2="100" stroke="#475569" stroke-width="2"/>
                <line x1="30" y1="200" x2="270" y2="200" stroke="#475569" stroke-width="2"/>

                <!-- Glowing Neon Z -->
                <path d="M 60 100 L ${x1} 100 L ${x2} 200 L 240 200" fill="none" stroke="#10b981" stroke-width="4"/>

                <!-- Alternate Interior Angles -->
                <text x="${x1 + 10}" y="125" fill="#10b981" font-size="12" font-weight="bold">${ang}°</text>
                <text x="${x2 - 35}" y="190" fill="#10b981" font-size="12" font-weight="bold">${ang}°</text>
            `;
        }

        // SIMULATOR 12: The "C-Pattern" Co-Interior Sum Gauge
        function renderSim12(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="cPatternSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Adjust Co-Interior Angle 1:</span>
                            <span id="cAngleVal" class="text-emerald-400 font-bold">115°</span>
                        </label>
                        <input type="range" min="95" max="145" value="115" step="5" id="cSlider" oninput="updateCPattern()" class="w-full accent-emerald-500">
                    </div>
                    <div id="cSumInfo" class="p-2.5 bg-slate-950 rounded-xl border border-emerald-500/30 text-xs font-mono text-center text-emerald-400 font-bold">
                        <!-- Populated by updateCPattern() -->
                    </div>
                </div>
            `;
            updateCPattern();
        }

        function updateCPattern() {
            const a1 = parseInt(document.getElementById('cSlider').value);
            const a2 = 180 - a1;
            document.getElementById('cAngleVal').textContent = `${a1}°`;
            document.getElementById('cSumInfo').innerHTML = `★ C-PATTERN: ${a1}° + ${a2}° = <span class="text-amber-300">180° (Supplementary)</span>`;

            const svg = document.getElementById('cPatternSvg');
            if (!svg) return;

            svg.innerHTML = `
                <!-- Parallel Lines -->
                <line x1="30" y1="100" x2="270" y2="100" stroke="#475569" stroke-width="2"/>
                <line x1="30" y1="200" x2="270" y2="200" stroke="#475569" stroke-width="2"/>

                <!-- Glowing C Frame on Right -->
                <path d="M 220 100 L 160 100 L 190 200 L 250 200" fill="none" stroke="#f43f5e" stroke-width="4"/>

                <!-- Angle Labels -->
                <text x="145" y="125" fill="#f43f5e" font-size="12" font-weight="bold">${a1}°</text>
                <text x="175" y="190" fill="#f43f5e" font-size="12" font-weight="bold">${a2}°</text>
            `;
        }

        // SIMULATOR 13: Venetian Blinds & Multi-Line Parallelism Rail
        function renderSim13(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="blindSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Rotate Venetian Blinds Slats:</span>
                            <span id="blindAngleVal" class="text-emerald-400 font-bold">20°</span>
                        </label>
                        <input type="range" min="-30" max="30" value="20" step="5" id="blindSlider" oninput="updateBlinds()" class="w-full accent-emerald-500">
                    </div>
                    <div class="p-2.5 bg-slate-950 rounded-xl border border-emerald-500/30 text-xs font-mono text-center text-emerald-300 font-bold">
                        Theorem 6.6: Line 1 ∥ Line 2 ∥ Line 3 ∥ Line 4 (Transitivity!)
                    </div>
                </div>
            `;
            updateBlinds();
        }

        function updateBlinds() {
            const rot = parseInt(document.getElementById('blindSlider').value);
            document.getElementById('blindAngleVal').textContent = `${rot}°`;

            const svg = document.getElementById('blindSvg');
            if (!svg) return;

            let slats = '';
            for (let y = 60; y <= 240; y += 45) {
                slats += `
                    <g transform="translate(150, ${y}) rotate(${rot})">
                        <line x1="-100" y1="0" x2="100" y2="0" stroke="#10b981" stroke-width="4"/>
                    </g>
                `;
            }

            svg.innerHTML = `
                <!-- Blind strings -->
                <line x1="80" y1="30" x2="80" y2="270" stroke="#475569" stroke-width="1.5" stroke-dasharray="3"/>
                <line x1="220" y1="30" x2="220" y2="270" stroke="#475569" stroke-width="1.5" stroke-dasharray="3"/>
                ${slats}
            `;
        }

        // SIMULATOR 14: Triangle Angle Sum Unfolder
        function renderSim14(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="triSumSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Adjust Vertex A Position:</span>
                            <span id="triAVertexVal" class="text-emerald-400 font-bold">A(150, 70)</span>
                        </label>
                        <input type="range" min="80" max="220" value="150" step="10" id="triASlider" oninput="updateTriSum()" class="w-full accent-emerald-500">
                    </div>
                    <div id="triSumProof" class="p-2.5 bg-slate-950 rounded-xl border border-emerald-500/30 text-xs font-mono text-center text-emerald-400 font-bold">
                        Theorem 6.7: ∠A + ∠B + ∠C = 180° (Proved via Parallel Auxiliary Line!)
                    </div>
                </div>
            `;
            updateTriSum();
        }

        function updateTriSum() {
            const ax = parseInt(document.getElementById('triASlider').value);
            document.getElementById('triAVertexVal').textContent = `A(${ax}, 70)`;

            const svg = document.getElementById('triSumSvg');
            if (!svg) return;

            const bx = 60, by = 210;
            const cxPt = 240, cyPt = 210;

            svg.innerHTML = `
                <!-- Auxiliary Parallel Line XAY ∥ BC -->
                <line x1="20" y1="70" x2="280" y2="70" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
                <text x="25" y="65" fill="#f59e0b" font-size="10" font-weight="bold">X</text>
                <text x="270" y="65" fill="#f59e0b" font-size="10" font-weight="bold">Y (Parallel to BC)</text>

                <!-- Triangle ABC -->
                <polygon points="${ax},70 ${bx},${by} ${cxPt},${cyPt}" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="3"/>

                <circle cx="${ax}" cy="70" r="5" fill="#f8fafc"/>
                <text x="${ax - 5}" y="95" fill="#ffffff" font-size="11" font-weight="bold">A</text>

                <circle cx="${bx}" cy="${by}" r="5" fill="#38bdf8"/>
                <text x="${bx - 15}" y="${by + 15}" fill="#38bdf8" font-size="11" font-weight="bold">B</text>

                <circle cx="${cxPt}" cy="${cyPt}" r="5" fill="#a855f7"/>
                <text x="${cxPt + 8}" y="${cyPt + 15}" fill="#a855f7" font-size="11" font-weight="bold">C</text>
            `;
        }

        // SIMULATOR 15: Triangle Angle Constraints & Contradiction Tester
        function renderSim15(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="text-xs">
                        <label class="text-slate-400">Test Impossible Triangle Scenarios:</label>
                        <select id="contraSelect" onchange="testContradiction()" class="w-full mt-1 bg-slate-900 border border-slate-700 text-rose-300 rounded p-1 font-mono">
                            <option value="twoRight">Scenario 1: Triangle with two 90° Right Angles</option>
                            <option value="twoObtuse">Scenario 2: Triangle with two 100° Obtuse Angles</option>
                            <option value="allSmall">Scenario 3: Triangle with all three angles < 60° (e.g. 50°, 50°, 50°)</option>
                        </select>
                    </div>
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden flex items-center justify-center">
                        <div id="contraVisual" class="text-center space-y-2 p-3">
                            <!-- Visual feedback -->
                        </div>
                    </div>
                    <div id="contraAlert" class="p-2.5 rounded-xl border border-rose-500/50 bg-rose-950/40 text-xs font-mono text-center text-rose-300 font-bold">
                        <!-- Populated by testContradiction() -->
                    </div>
                </div>
            `;
            testContradiction();
        }

        function testContradiction() {
            const sc = document.getElementById('contraSelect').value;
            const vis = document.getElementById('contraVisual');
            const alert = document.getElementById('contraAlert');

            if (sc === 'twoRight') {
                vis.innerHTML = `
                    <div class="text-4xl text-rose-500 font-black">🚫 CONTRADICTION!</div>
                    <div class="text-slate-300 text-xs">90° + 90° = 180°</div>
                    <div class="text-amber-400 text-xs font-mono">Third angle = 180° - 180° = 0° (Impossible!)</div>
                `;
                alert.textContent = "Proof by Contradiction: A triangle can have at most ONE right angle!";
            } else if (sc === 'twoObtuse') {
                vis.innerHTML = `
                    <div class="text-4xl text-rose-500 font-black">🚫 CONTRADICTION!</div>
                    <div class="text-slate-300 text-xs">100° + 100° = 200° > 180°</div>
                    <div class="text-amber-400 text-xs font-mono">Sum already exceeds 180°!</div>
                `;
                alert.textContent = "Proof by Contradiction: A triangle can have at most ONE obtuse angle!";
            } else {
                vis.innerHTML = `
                    <div class="text-4xl text-rose-500 font-black">🚫 CONTRADICTION!</div>
                    <div class="text-slate-300 text-xs">50° + 50° + 50° = 150° < 180°</div>
                    <div class="text-amber-400 text-xs font-mono">Cannot close into a triangle!</div>
                `;
                alert.textContent = "Proof by Contradiction: A triangle CANNOT have all three angles < 60°!";
            }
            playErrorSound();
        }

        // SIMULATOR 16: Geometric Rule-Based Forward Chaining Engine
        function renderSim16(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="flex items-center justify-between text-xs">
                        <span class="text-slate-400">AI Inference Engine:</span>
                        <button onclick="runInferenceEngine()" class="px-3 py-1 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold transition">
                            ▶ Run Deduction Steps
                        </button>
                    </div>
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 font-mono text-[11px] space-y-1.5 h-[190px] overflow-y-auto" id="inferLog">
                        <div class="text-slate-500">// Given: Line AB ∥ CD, Transversal t, ∠1 = 65°</div>
                        <div class="text-cyan-400">Ready to execute forward-chaining rules...</div>
                    </div>
                    <div id="inferResult" class="p-2.5 bg-slate-950 rounded-xl border border-emerald-500/30 text-xs font-mono text-center text-emerald-400 font-bold">
                        Click 'Run Deduction Steps' to trigger automated geometric inference!
                    </div>
                </div>
            `;
        }

        function runInferenceEngine() {
            const log = document.getElementById('inferLog');
            const res = document.getElementById('inferResult');
            log.innerHTML = `<div class="text-slate-500">// Executing Forward-Chaining Deduction...</div>`;

            setTimeout(() => {
                log.innerHTML += `<div class="text-amber-300">Rule 1 applied: vert_opposite(∠1, ∠3) ⇒ ∠3 = 65°</div>`;
                playTone(400, 'sine', 0.1);
            }, 300);

            setTimeout(() => {
                log.innerHTML += `<div class="text-amber-300">Rule 2 applied: linear_pair(∠1, ∠2) ⇒ ∠2 = 180° - 65° = 115°</div>`;
                playTone(480, 'sine', 0.1);
            }, 700);

            setTimeout(() => {
                log.innerHTML += `<div class="text-cyan-300">Rule 3 applied: alt_interior(∠3, ∠5) ⇒ ∠5 = 65°</div>`;
                playTone(560, 'sine', 0.1);
            }, 1100);

            setTimeout(() => {
                log.innerHTML += `<div class="text-emerald-400 font-bold">Rule 4 applied: co_interior(∠4, ∠5) ⇒ ∠4 = 180° - 65° = 115°</div>`;
                res.innerHTML = `★ SUCCESS: All 8 angles deduced in 4 computational inference steps!`;
                playSuccessSound();
            }, 1500);
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

