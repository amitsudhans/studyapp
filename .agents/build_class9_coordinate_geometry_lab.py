# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 9 Mathematics, Chapter 6
COORDINATE GEOMETRY (Competencies CG-4, C-4.5, CG-9)
Generates public/animations/class9-coordinate-geometry.html
"""

import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from class9_coordinate_geometry_data import SLIDES, QUIZZES

OUTPUT_PATH = "public/animations/class9-coordinate-geometry.html"

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
    <title>NCERT Class 9 Mathematics • Chapter 6 • Coordinate Geometry Lab</title>
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
        .radar-sweep {
            animation: radarRotate 4s linear infinite;
            transform-origin: 50% 50%;
        }
        @keyframes radarRotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col selection:bg-indigo-500 selection:text-white">

    <!-- Top Navigation Header -->
    <header class="bg-slate-900/90 backdrop-blur-md border-b border-slate-800 sticky top-0 z-40 px-4 py-2.5">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-cyan-600 to-indigo-500 flex items-center justify-center shadow-lg shadow-cyan-500/30">
                    <i data-lucide="crosshair" class="w-5 h-5 text-white"></i>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="text-xs font-bold uppercase tracking-wider text-cyan-400 bg-cyan-500/10 px-2 py-0.5 rounded border border-cyan-500/20">Class 9 Maths • Chapter 6</span>
                        <span id="currentBadge" class="hidden sm:inline-block text-xs text-indigo-400 bg-indigo-500/10 px-2 py-0.5 rounded border border-indigo-500/20 font-semibold">CG-4 • Historical Foundations</span>
                    </div>
                    <h1 class="text-sm sm:text-base font-extrabold text-white tracking-tight">Coordinate Geometry Lab</h1>
                </div>
            </div>

            <!-- Central Slide Indicator -->
            <div class="flex items-center gap-2 bg-slate-950/80 px-3 py-1.5 rounded-xl border border-slate-800">
                <span class="text-xs text-slate-400">Slide</span>
                <span id="slideCounter" class="text-sm font-bold text-cyan-400 font-mono">1 / 20</span>
                <div class="w-20 sm:w-28 bg-slate-800 h-2 rounded-full overflow-hidden ml-1">
                    <div id="progressBar" class="bg-gradient-to-r from-cyan-500 to-indigo-500 h-full w-[5%] transition-all duration-300"></div>
                </div>
            </div>

            <!-- Voice Controls & Speed -->
            <div class="flex items-center gap-2">
                <div class="flex items-center bg-slate-800/80 rounded-lg p-0.5 border border-slate-700">
                    <button onclick="changeSpeed(0.8)" id="spd08" class="px-2 py-1 text-[11px] rounded font-medium text-slate-300 hover:text-white transition">0.8x</button>
                    <button onclick="changeSpeed(1.0)" id="spd10" class="px-2 py-1 text-[11px] rounded font-bold bg-indigo-600 text-white transition">1.0x</button>
                    <button onclick="changeSpeed(1.2)" id="spd12" class="px-2 py-1 text-[11px] rounded font-medium text-slate-300 hover:text-white transition">1.2x</button>
                </div>
                <button onclick="toggleAudio()" id="voiceToggleBtn" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-cyan-600 hover:bg-cyan-500 text-white transition shadow-md shadow-cyan-600/30">
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
                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-cyan-500 to-indigo-600 p-0.5 shadow-md shadow-cyan-500/20">
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
                    <span class="text-xs font-bold text-cyan-400">Prof. Sophia</span>
                    <span class="text-[10px] text-slate-400">• Interactive Mathematics Guide</span>
                </div>
                <p id="narrationText" class="text-xs sm:text-sm text-slate-200 truncate font-normal">
                    Welcome to Coordinate Geometry! Let's explore how Descartes bridged Algebra and Geometry with coordinates.
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
            <div class="bg-slate-900 border border-cyan-500/30 rounded-2xl max-w-xl w-full p-5 sm:p-6 shadow-2xl relative max-h-[85vh] overflow-y-auto">
                <div class="flex items-start justify-between gap-3 border-b border-slate-800 pb-3 mb-4">
                    <div class="flex items-center gap-2">
                        <div class="w-7 h-7 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center">
                            <i data-lucide="file-text" class="w-4 h-4"></i>
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
                <div class="p-4 bg-cyan-950/20 rounded-xl border border-cyan-500/20 text-xs sm:text-sm text-cyan-200 leading-relaxed font-mono space-y-2" id="modalSolutionText">
                    <!-- Solution derivation -->
                </div>
                <div class="mt-5 flex justify-end">
                    <button onclick="closeSolutionModal()" class="px-4 py-2 rounded-xl text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white transition">
                        Understood & Close
                    </button>
                </div>
            </div>
        </div>

        <!-- Last Slide Notice Banner -->
        <div id="lastSlideNotice" class="hidden mt-6 p-4 rounded-xl bg-gradient-to-r from-emerald-950/60 via-slate-900 to-indigo-950/60 border border-emerald-500/40 text-center">
            <div class="flex items-center justify-center gap-2 text-emerald-400 font-bold text-sm sm:text-base">
                <i data-lucide="check-circle" class="w-5 h-5"></i>
                <span>You have reached the last slide of this chapter</span>
            </div>
            <p class="text-xs text-slate-300 mt-1">
                Outstanding accomplishment! You have mastered the 2D Cartesian plane, distance formula, midpoints, collinearity, geometric shape proofs, and computational thinking in Coordinate Geometry.
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

            <button onclick="nextSlide()" id="nextBtn" class="flex items-center gap-2 px-5 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-cyan-600 to-indigo-600 hover:from-cyan-500 hover:to-indigo-500 text-white shadow-lg shadow-cyan-600/30 transition">
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
                btn.className = "flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-cyan-600 hover:bg-cyan-500 text-white transition shadow-md shadow-cyan-600/30";
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
                activeEl.className = "px-2 py-1 text-[11px] rounded font-bold bg-indigo-600 text-white transition";
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
            document.getElementById('currentBadge').textContent = slide.badge || "Coordinate Geometry";
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
                                <span class="text-xs font-bold text-cyan-400 font-mono">CONCEPT #${currNum}</span>
                                <h2 class="text-xl sm:text-2xl font-black text-white tracking-tight">${slide.title}</h2>
                                <p class="text-xs sm:text-sm text-slate-400 font-medium mt-0.5">${slide.subtitle}</p>
                            </div>
                            <span class="text-xs px-2.5 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 font-semibold">${slide.category}</span>
                        </div>

                        <!-- 2-Column Split: Theory on Left, Simulator on Right -->
                        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 items-start">
                            <!-- Left: Theory & Checkpoints -->
                            <div class="space-y-4">
                                <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800/90 shadow-lg">
                                    <h3 class="text-xs font-bold uppercase tracking-wider text-cyan-400 mb-2 flex items-center gap-1.5">
                                        <i data-lucide="book-open" class="w-4 h-4"></i>
                                        Conceptual Overview
                                    </h3>
                                    <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                                        ${slide.summary}
                                    </p>
                                </div>

                                <div class="p-4 rounded-2xl bg-slate-900/80 border border-slate-800/90 shadow-lg">
                                    <h3 class="text-xs font-bold uppercase tracking-wider text-indigo-400 mb-2.5 flex items-center gap-1.5">
                                        <i data-lucide="sparkles" class="w-4 h-4"></i>
                                        Key Mathematical Insights
                                    </h3>
                                    <ul class="text-xs text-slate-300 space-y-2">
                                        ${slide.key_points.map(kp => `
                                            <li class="flex items-start gap-2">
                                                <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-cyan-400 shrink-0 mt-0.5"></i>
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
                                                        <button onclick="checkCheckpoint(${cIdx}, ${oIdx}, ${cp.ans})" id="cp_${cIdx}_${oIdx}" class="w-full text-left text-xs px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-800 hover:border-cyan-500/50 text-slate-300 transition flex items-center justify-between">
                                                            <span>${opt}</span>
                                                            <span id="cp_ind_${cIdx}_${oIdx}" class="hidden font-bold text-xs"></span>
                                                        </button>
                                                    `).join('')}
                                                </div>
                                                <div id="cp_exp_${cIdx}" class="hidden text-[11px] p-2.5 rounded-lg bg-cyan-950/40 border border-cyan-500/30 text-cyan-200">
                                                    ${cp.explanation}
                                                </div>
                                            </div>
                                        `).join('')}
                                    </div>
                                </div>
                            </div>

                            <!-- Right: Bespoke Interactive Simulator -->
                            <div class="p-5 rounded-2xl bg-slate-900/90 border border-cyan-500/30 shadow-xl flex flex-col justify-between min-h-[460px]">
                                <div>
                                    <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
                                        <div class="flex items-center gap-2">
                                            <div class="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-pulse"></div>
                                            <h4 class="text-xs sm:text-sm font-bold text-cyan-300">${slide.sim_title}</h4>
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
                                            <span class="text-xs font-bold text-cyan-400 font-mono">Question ${q.id}</span>
                                            <button onclick="showSolution(${currentSlideIndex}, ${qIdx})" class="px-2.5 py-1 rounded-lg text-[10px] font-bold bg-amber-500/10 hover:bg-amber-500/20 text-amber-300 border border-amber-500/30 transition flex items-center gap-1.5 shadow-sm">
                                                <i data-lucide="eye" class="w-3.5 h-3.5"></i>
                                                View Solution
                                            </button>
                                        </div>
                                        <p class="text-xs sm:text-sm text-slate-200 font-medium mb-3">${q.q}</p>
                                        <div class="space-y-1.5 mb-2">
                                            ${q.options.map((opt, oIdx) => `
                                                <button onclick="answerQuiz(${q.id}, ${oIdx}, ${q.ans})" id="quiz_${q.id}_${oIdx}" class="w-full text-left text-xs px-3 py-2 rounded-xl bg-slate-950/80 border border-slate-800 hover:border-cyan-500/50 text-slate-300 transition flex items-center justify-between">
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
                    ? (isQuiz ? 'bg-amber-400 ring-2 ring-amber-400/50 scale-125' : 'bg-cyan-400 ring-2 ring-cyan-400/50 scale-125')
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

        // SIMULATOR 1: Descartes Fly on Ceiling
        function renderSim1(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2">
                        <svg id="flySvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="flex items-center justify-between gap-4 text-xs">
                        <div class="flex-1">
                            <label class="text-slate-400 flex justify-between">
                                <span>Left Wall (x):</span>
                                <span id="flyXVal" class="text-cyan-400 font-bold">4</span>
                            </label>
                            <input type="range" min="0" max="8" value="4" step="1" id="flyXSlider" oninput="updateFly()" class="w-full accent-cyan-500">
                        </div>
                        <div class="flex-1">
                            <label class="text-slate-400 flex justify-between">
                                <span>Bottom Wall (y):</span>
                                <span id="flyYVal" class="text-cyan-400 font-bold">5</span>
                            </label>
                            <input type="range" min="0" max="8" value="5" step="1" id="flyYSlider" oninput="updateFly()" class="w-full accent-cyan-500">
                        </div>
                    </div>
                    <div class="p-2.5 bg-slate-950 rounded-xl border border-cyan-500/30 text-center text-xs font-mono">
                        <span class="text-slate-400">Position of Fly:</span>
                        <span id="flyCoordText" class="text-amber-300 font-bold ml-1 text-sm">(4, 5)</span>
                        <div class="text-[11px] text-cyan-400 mt-1">4 units right from Left Wall, 5 units up from Bottom Wall</div>
                    </div>
                </div>
            `;
            updateFly();
        }

        function updateFly() {
            const xSlider = document.getElementById('flyXSlider');
            const ySlider = document.getElementById('flyYSlider');
            if (!xSlider || !ySlider) return;
            const x = parseInt(xSlider.value);
            const y = parseInt(ySlider.value);

            document.getElementById('flyXVal').textContent = x;
            document.getElementById('flyYVal').textContent = y;
            document.getElementById('flyCoordText').textContent = `(${x}, ${y})`;

            const svg = document.getElementById('flySvg');
            if (!svg) return;

            const pad = 30;
            const size = 240;
            const step = size / 8;
            const px = pad + x * step;
            const py = pad + (8 - y) * step;

            let gridLines = '';
            for (let i = 0; i <= 8; i++) {
                const pos = pad + i * step;
                gridLines += `<line x1="${pos}" y1="${pad}" x2="${pos}" y2="${pad + size}" stroke="#1e293b" stroke-width="1"/>`;
                gridLines += `<line x1="${pad}" y1="${pos}" x2="${pad + size}" y2="${pos}" stroke="#1e293b" stroke-width="1"/>`;
            }

            svg.innerHTML = `
                ${gridLines}
                <!-- Walls (Axes) -->
                <line x1="${pad}" y1="${pad}" x2="${pad}" y2="${pad + size}" stroke="#06b6d4" stroke-width="3"/>
                <line x1="${pad}" y1="${pad + size}" x2="${pad + size}" y2="${pad + size}" stroke="#06b6d4" stroke-width="3"/>
                <text x="${pad - 12}" y="${pad + 15}" fill="#06b6d4" font-size="10" font-weight="bold">Left Wall (y-axis)</text>
                <text x="${pad + size - 80}" y="${pad + size + 15}" fill="#06b6d4" font-size="10" font-weight="bold">Bottom Wall (x-axis)</text>

                <!-- Projections -->
                <line x1="${pad}" y1="${py}" x2="${px}" y2="${py}" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
                <line x1="${px}" y1="${pad + size}" x2="${px}" y2="${py}" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4"/>

                <!-- Fly Icon -->
                <g transform="translate(${px - 10}, ${py - 10})">
                    <circle cx="10" cy="10" r="6" fill="#ef4444"/>
                    <ellipse cx="6" cy="6" rx="4" ry="2" fill="#94a3b8" transform="rotate(-30 6 6)"/>
                    <ellipse cx="14" cy="6" rx="4" ry="2" fill="#94a3b8" transform="rotate(30 14 6)"/>
                    <circle cx="8" cy="8" r="1.5" fill="#ffffff"/>
                    <circle cx="12" cy="8" r="1.5" fill="#ffffff"/>
                </g>
                <circle cx="${px}" cy="${py}" r="12" fill="none" stroke="#ef4444" stroke-width="1.5" class="animate-ping" opacity="0.4"/>
            `;
        }

        // SIMULATOR 2: Four Quadrants Explorer
        function renderSim2(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2">
                        <svg id="quadSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="grid grid-cols-2 gap-3 text-xs">
                        <div>
                            <label class="text-slate-400 flex justify-between">
                                <span>Abscissa (x):</span>
                                <span id="quadXVal" class="text-cyan-400 font-bold">-3</span>
                            </label>
                            <input type="range" min="-6" max="6" value="-3" step="1" id="quadXSlider" oninput="updateQuad()" class="w-full accent-cyan-500">
                        </div>
                        <div>
                            <label class="text-slate-400 flex justify-between">
                                <span>Ordinate (y):</span>
                                <span id="quadYVal" class="text-indigo-400 font-bold">4</span>
                            </label>
                            <input type="range" min="-6" max="6" value="4" step="1" id="quadYSlider" oninput="updateQuad()" class="w-full accent-indigo-500">
                        </div>
                    </div>
                    <div id="quadBadge" class="p-2.5 rounded-xl border text-center text-xs font-mono font-bold">
                        <!-- Populated by updateQuad() -->
                    </div>
                </div>
            `;
            updateQuad();
        }

        function updateQuad() {
            const xs = document.getElementById('quadXSlider');
            const ys = document.getElementById('quadYSlider');
            if (!xs || !ys) return;
            const x = parseInt(xs.value);
            const y = parseInt(ys.value);

            document.getElementById('quadXVal').textContent = x;
            document.getElementById('quadYVal').textContent = y;

            const badge = document.getElementById('quadBadge');
            if (x > 0 && y > 0) {
                badge.className = "p-2.5 rounded-xl border border-emerald-500/40 bg-emerald-950/30 text-emerald-300 text-center text-xs font-mono font-bold";
                badge.innerHTML = `Point P(${x}, ${y}) lies in <span class="text-emerald-400">QUADRANT I (+, +)</span>`;
            } else if (x < 0 && y > 0) {
                badge.className = "p-2.5 rounded-xl border border-cyan-500/40 bg-cyan-950/30 text-cyan-300 text-center text-xs font-mono font-bold";
                badge.innerHTML = `Point P(${x}, ${y}) lies in <span class="text-cyan-400">QUADRANT II (-, +)</span>`;
            } else if (x < 0 && y < 0) {
                badge.className = "p-2.5 rounded-xl border border-amber-500/40 bg-amber-950/30 text-amber-300 text-center text-xs font-mono font-bold";
                badge.innerHTML = `Point P(${x}, ${y}) lies in <span class="text-amber-400">QUADRANT III (-, -)</span>`;
            } else if (x > 0 && y < 0) {
                badge.className = "p-2.5 rounded-xl border border-violet-500/40 bg-violet-950/30 text-violet-300 text-center text-xs font-mono font-bold";
                badge.innerHTML = `Point P(${x}, ${y}) lies in <span class="text-violet-400">QUADRANT IV (+, -)</span>`;
            } else if (x === 0 && y === 0) {
                badge.className = "p-2.5 rounded-xl border border-white/40 bg-slate-800 text-white text-center text-xs font-mono font-bold";
                badge.innerHTML = `Point P(0, 0) is the <span class="text-white">ORIGIN O(0, 0)</span>`;
            } else if (y === 0) {
                badge.className = "p-2.5 rounded-xl border border-sky-500/40 bg-sky-950/30 text-sky-300 text-center text-xs font-mono font-bold";
                badge.innerHTML = `Point P(${x}, 0) lies strictly on the <span class="text-sky-400">X-AXIS</span>`;
            } else {
                badge.className = "p-2.5 rounded-xl border border-indigo-500/40 bg-indigo-950/30 text-indigo-300 text-center text-xs font-mono font-bold";
                badge.innerHTML = `Point P(0, ${y}) lies strictly on the <span class="text-indigo-400">Y-AXIS</span>`;
            }

            const svg = document.getElementById('quadSvg');
            if (!svg) return;

            const cx = 150;
            const cy = 150;
            const scale = 20;
            const px = cx + x * scale;
            const py = cy - y * scale;

            svg.innerHTML = `
                <!-- Background Quadrant Shading -->
                <rect x="${x >= 0 ? 150 : 20}" y="${y >= 0 ? 20 : 150}" width="130" height="130" fill="#06b6d4" fill-opacity="0.08"/>

                <!-- Coordinate Axes -->
                <line x1="20" y1="150" x2="280" y2="150" stroke="#64748b" stroke-width="2"/>
                <line x1="150" y1="20" x2="150" y2="280" stroke="#64748b" stroke-width="2"/>

                <text x="275" y="145" fill="#94a3b8" font-size="10" font-weight="bold">X</text>
                <text x="155" y="30" fill="#94a3b8" font-size="10" font-weight="bold">Y</text>
                <text x="135" y="165" fill="#64748b" font-size="9">O</text>

                <!-- Labels for Quadrants -->
                <text x="220" y="70" fill="#334155" font-size="14" font-weight="bold">Q I</text>
                <text x="60" y="70" fill="#334155" font-size="14" font-weight="bold">Q II</text>
                <text x="60" y="230" fill="#334155" font-size="14" font-weight="bold">Q III</text>
                <text x="220" y="230" fill="#334155" font-size="14" font-weight="bold">Q IV</text>

                <!-- Projection Lines -->
                <line x1="${px}" y1="150" x2="${px}" y2="${py}" stroke="#38bdf8" stroke-dasharray="3" stroke-width="1.5"/>
                <line x1="150" y1="${py}" x2="${px}" y2="${py}" stroke="#818cf8" stroke-dasharray="3" stroke-width="1.5"/>

                <!-- Point Marker -->
                <circle cx="${px}" cy="${py}" r="6" fill="#38bdf8"/>
                <circle cx="${px}" cy="${py}" r="12" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.5"/>
                <text x="${px + 8}" y="${py - 8}" fill="#f8fafc" font-size="11" font-weight="bold" font-family="monospace">P(${x}, ${y})</text>
            `;
        }

        // SIMULATOR 3: City Landmark Relative Navigator
        function renderSim3(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2">
                        <svg id="citySvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="grid grid-cols-2 gap-3 text-xs">
                        <div>
                            <label class="text-slate-400">Start Location:</label>
                            <select id="startLandmark" onchange="updateCityNav()" class="w-full mt-1 bg-slate-900 border border-slate-700 text-cyan-300 rounded-lg p-1.5">
                                <option value="home">Home (2, 2)</option>
                                <option value="school">School (-4, 3)</option>
                                <option value="library">Library (6, 8)</option>
                                <option value="park">Park (-3, -5)</option>
                            </select>
                        </div>
                        <div>
                            <label class="text-slate-400">Destination:</label>
                            <select id="destLandmark" onchange="updateCityNav()" class="w-full mt-1 bg-slate-900 border border-slate-700 text-amber-300 rounded-lg p-1.5">
                                <option value="library">Library (6, 8)</option>
                                <option value="home">Home (2, 2)</option>
                                <option value="school">School (-4, 3)</option>
                                <option value="park">Park (-3, -5)</option>
                            </select>
                        </div>
                    </div>
                    <div id="cityNavResult" class="p-2.5 bg-slate-950 rounded-xl border border-cyan-500/30 text-xs font-mono space-y-1">
                        <!-- Populated by updateCityNav() -->
                    </div>
                </div>
            `;
            updateCityNav();
        }

        function updateCityNav() {
            const landmarks = {
                home: { name: "Home", x: 2, y: 2, color: "#38bdf8" },
                school: { name: "School", x: -4, y: 3, color: "#34d399" },
                library: { name: "Library", x: 6, y: 8, color: "#f59e0b" },
                park: { name: "Park", x: -3, y: -5, color: "#a855f7" }
            };

            const sKey = document.getElementById('startLandmark').value;
            const dKey = document.getElementById('destLandmark').value;
            const p1 = landmarks[sKey];
            const p2 = landmarks[dKey];

            const dx = p2.x - p1.x;
            const dy = p2.y - p1.y;
            const xDir = dx >= 0 ? "East" : "West";
            const yDir = dy >= 0 ? "North" : "South";

            document.getElementById('cityNavResult').innerHTML = `
                <div class="flex justify-between text-slate-300">
                    <span>Displacement Vector:</span>
                    <span class="text-amber-300 font-bold">Δx = ${dx}, Δy = ${dy}</span>
                </div>
                <div class="text-cyan-300 font-bold">
                    Directions: Walk ${Math.abs(dx)} units ${xDir}, then ${Math.abs(dy)} units ${yDir}.
                </div>
            `;

            const svg = document.getElementById('citySvg');
            if (!svg) return;

            const cx = 150, cy = 150, sc = 12;
            const x1 = cx + p1.x * sc, y1 = cy - p1.y * sc;
            const x2 = cx + p2.x * sc, y2 = cy - p2.y * sc;

            let marks = Object.values(landmarks).map(lm => {
                const lx = cx + lm.x * sc;
                const ly = cy - lm.y * sc;
                return `
                    <circle cx="${lx}" cy="${ly}" r="5" fill="${lm.color}"/>
                    <text x="${lx + 7}" y="${ly + 4}" fill="${lm.color}" font-size="9" font-weight="bold">${lm.name} (${lm.x},${lm.y})</text>
                `;
            }).join('');

            svg.innerHTML = `
                <!-- Grid Lines -->
                <line x1="20" y1="150" x2="280" y2="150" stroke="#334155" stroke-width="1.5"/>
                <line x1="150" y1="20" x2="150" y2="280" stroke="#334155" stroke-width="1.5"/>
                ${marks}

                <!-- Vector Arrow -->
                <defs>
                    <marker id="navArrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
                        <polygon points="0 0, 6 3, 0 6" fill="#f59e0b"/>
                    </marker>
                </defs>
                <line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#navArrow)"/>
                <line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y1}" stroke="#38bdf8" stroke-dasharray="3" stroke-width="1.5"/>
                <line x1="${x2}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#34d399" stroke-dasharray="3" stroke-width="1.5"/>
            `;
        }

        // SIMULATOR 4: Architectural Floor Plan Modeler
        function renderSim4(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2">
                        <svg id="floorSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="grid grid-cols-2 gap-3 text-xs">
                        <div>
                            <label class="text-slate-400 flex justify-between">
                                <span>Room Width (m):</span>
                                <span id="roomWVal" class="text-cyan-400 font-bold">6</span>
                            </label>
                            <input type="range" min="3" max="10" value="6" step="1" id="roomW" oninput="updateFloorPlan()" class="w-full accent-cyan-500">
                        </div>
                        <div>
                            <label class="text-slate-400 flex justify-between">
                                <span>Room Length (m):</span>
                                <span id="roomLVal" class="text-indigo-400 font-bold">8</span>
                            </label>
                            <input type="range" min="3" max="10" value="8" step="1" id="roomL" oninput="updateFloorPlan()" class="w-full accent-indigo-500">
                        </div>
                    </div>
                    <div id="floorCalcResult" class="p-2.5 bg-slate-950 rounded-xl border border-cyan-500/30 text-xs font-mono grid grid-cols-2 gap-2 text-center">
                        <!-- Populated by updateFloorPlan() -->
                    </div>
                </div>
            `;
            updateFloorPlan();
        }

        function updateFloorPlan() {
            const wInput = document.getElementById('roomW');
            const lInput = document.getElementById('roomL');
            if (!wInput || !lInput) return;
            const w = parseInt(wInput.value);
            const l = parseInt(lInput.value);

            document.getElementById('roomWVal').textContent = w;
            document.getElementById('roomLVal').textContent = l;

            const perimeter = 2 * (w + l);
            const area = w * l;

            document.getElementById('floorCalcResult').innerHTML = `
                <div class="p-1.5 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">Perimeter: 2(W+L)</span>
                    <span class="text-cyan-300 font-bold">${perimeter} meters</span>
                </div>
                <div class="p-1.5 rounded bg-slate-900 border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">Floor Area: W × L</span>
                    <span class="text-emerald-300 font-bold">${area} m²</span>
                </div>
            `;

            const svg = document.getElementById('floorSvg');
            if (!svg) return;

            const scale = 18;
            const svgW = w * scale;
            const svgH = l * scale;
            const ox = (300 - svgW) / 2;
            const oy = (300 - svgH) / 2;

            svg.innerHTML = `
                <!-- Grid pattern -->
                <rect x="${ox}" y="${oy}" width="${svgW}" height="${svgH}" fill="#06b6d4" fill-opacity="0.15" stroke="#06b6d4" stroke-width="2.5"/>

                <!-- Corner Coordinates -->
                <circle cx="${ox}" cy="${oy + svgH}" r="4" fill="#f59e0b"/>
                <text x="${ox - 10}" y="${oy + svgH + 15}" fill="#94a3b8" font-size="9" font-family="monospace">(1, 1)</text>

                <circle cx="${ox + svgW}" cy="${oy + svgH}" r="4" fill="#f59e0b"/>
                <text x="${ox + svgW - 10}" y="${oy + svgH + 15}" fill="#94a3b8" font-size="9" font-family="monospace">(${1 + w}, 1)</text>

                <circle cx="${ox + svgW}" cy="${oy}" r="4" fill="#f59e0b"/>
                <text x="${ox + svgW - 10}" y="${oy - 8}" fill="#94a3b8" font-size="9" font-family="monospace">(${1 + w}, ${1 + l})</text>

                <circle cx="${ox}" cy="${oy}" r="4" fill="#f59e0b"/>
                <text x="${ox - 10}" y="${oy - 8}" fill="#94a3b8" font-size="9" font-family="monospace">(1, ${1 + l})</text>

                <!-- Dimension Lines -->
                <text x="${ox + svgW / 2 - 20}" y="${oy + svgH - 8}" fill="#38bdf8" font-size="11" font-weight="bold">W = ${w} m</text>
                <text x="${ox + 8}" y="${oy + svgH / 2}" fill="#818cf8" font-size="11" font-weight="bold">L = ${l} m</text>
            `;
        }

        // SIMULATOR 5: Axis-Parallel Dynamic Distance Ruler
        function renderSim5(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="flex items-center justify-between text-xs">
                        <span class="text-slate-400">Orientation:</span>
                        <div class="flex gap-2">
                            <button onclick="setSim5Mode('horizontal')" id="sim5HBtn" class="px-2.5 py-1 rounded bg-cyan-600 text-white font-bold">Horizontal</button>
                            <button onclick="setSim5Mode('vertical')" id="sim5VBtn" class="px-2.5 py-1 rounded bg-slate-800 text-slate-300">Vertical</button>
                        </div>
                    </div>
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2">
                        <svg id="rulerSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="grid grid-cols-2 gap-3 text-xs">
                        <div>
                            <label class="text-slate-400 flex justify-between">
                                <span id="rulerP1Label">Point A (x₁):</span>
                                <span id="rulerP1Val" class="text-cyan-400 font-bold">-4</span>
                            </label>
                            <input type="range" min="-7" max="7" value="-4" step="1" id="rulerP1" oninput="updateRuler()" class="w-full accent-cyan-500">
                        </div>
                        <div>
                            <label class="text-slate-400 flex justify-between">
                                <span id="rulerP2Label">Point B (x₂):</span>
                                <span id="rulerP2Val" class="text-amber-400 font-bold">5</span>
                            </label>
                            <input type="range" min="-7" max="7" value="5" step="1" id="rulerP2" oninput="updateRuler()" class="w-full accent-amber-500">
                        </div>
                    </div>
                    <div id="rulerCalcResult" class="p-2.5 bg-slate-950 rounded-xl border border-cyan-500/30 text-xs font-mono text-center font-bold text-cyan-300">
                        <!-- Populated by updateRuler() -->
                    </div>
                </div>
            `;
            window.sim5Mode = 'horizontal';
            updateRuler();
        }

        function setSim5Mode(m) {
            window.sim5Mode = m;
            document.getElementById('sim5HBtn').className = m === 'horizontal' ? 'px-2.5 py-1 rounded bg-cyan-600 text-white font-bold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300';
            document.getElementById('sim5VBtn').className = m === 'vertical' ? 'px-2.5 py-1 rounded bg-cyan-600 text-white font-bold' : 'px-2.5 py-1 rounded bg-slate-800 text-slate-300';
            document.getElementById('rulerP1Label').textContent = m === 'horizontal' ? 'Point A (x₁):' : 'Point A (y₁):';
            document.getElementById('rulerP2Label').textContent = m === 'horizontal' ? 'Point B (x₂):' : 'Point B (y₂):';
            updateRuler();
        }

        function updateRuler() {
            const p1 = parseInt(document.getElementById('rulerP1').value);
            const p2 = parseInt(document.getElementById('rulerP2').value);
            document.getElementById('rulerP1Val').textContent = p1;
            document.getElementById('rulerP2Val').textContent = p2;

            const dist = Math.abs(p2 - p1);
            const mode = window.sim5Mode || 'horizontal';

            document.getElementById('rulerCalcResult').innerHTML = mode === 'horizontal'
                ? `Distance d = |x₂ - x₁| = |${p2} - (${p1})| = <span class="text-amber-300 text-sm">${dist} units</span>`
                : `Distance d = |y₂ - y₁| = |${p2} - (${p1})| = <span class="text-amber-300 text-sm">${dist} units</span>`;

            const svg = document.getElementById('rulerSvg');
            if (!svg) return;

            const cx = 150, cy = 150, scale = 16;
            if (mode === 'horizontal') {
                const x1 = cx + p1 * scale;
                const x2 = cx + p2 * scale;
                svg.innerHTML = `
                    <line x1="20" y1="150" x2="280" y2="150" stroke="#64748b" stroke-width="2"/>
                    <line x1="150" y1="20" x2="150" y2="280" stroke="#334155" stroke-width="1.5"/>

                    <!-- Dimension Line -->
                    <line x1="${x1}" y1="130" x2="${x2}" y2="130" stroke="#f59e0b" stroke-width="2.5"/>
                    <line x1="${x1}" y1="120" x2="${x1}" y2="140" stroke="#f59e0b" stroke-width="2"/>
                    <line x1="${x2}" y1="120" x2="${x2}" y2="140" stroke="#f59e0b" stroke-width="2"/>
                    <text x="${(x1 + x2) / 2 - 12}" y="115" fill="#f59e0b" font-size="12" font-weight="bold">${dist}</text>

                    <!-- Points -->
                    <circle cx="${x1}" cy="150" r="5" fill="#06b6d4"/>
                    <text x="${x1 - 10}" y="170" fill="#06b6d4" font-size="10" font-weight="bold">A(${p1}, 0)</text>

                    <circle cx="${x2}" cy="150" r="5" fill="#a855f7"/>
                    <text x="${x2 - 10}" y="170" fill="#a855f7" font-size="10" font-weight="bold">B(${p2}, 0)</text>
                `;
            } else {
                const y1 = cy - p1 * scale;
                const y2 = cy - p2 * scale;
                svg.innerHTML = `
                    <line x1="20" y1="150" x2="280" y2="150" stroke="#334155" stroke-width="1.5"/>
                    <line x1="150" y1="20" x2="150" y2="280" stroke="#64748b" stroke-width="2"/>

                    <!-- Dimension Line -->
                    <line x1="170" y1="${y1}" x2="170" y2="${y2}" stroke="#f59e0b" stroke-width="2.5"/>
                    <line x1="160" y1="${y1}" x2="180" y2="${y1}" stroke="#f59e0b" stroke-width="2"/>
                    <line x1="160" y1="${y2}" x2="180" y2="${y2}" stroke="#f59e0b" stroke-width="2"/>
                    <text x="185" y="${(y1 + y2) / 2 + 4}" fill="#f59e0b" font-size="12" font-weight="bold">${dist}</text>

                    <!-- Points -->
                    <circle cx="150" cy="${y1}" r="5" fill="#06b6d4"/>
                    <text x="90" y="${y1 + 4}" fill="#06b6d4" font-size="10" font-weight="bold">A(0, ${p1})</text>

                    <circle cx="150" cy="${y2}" r="5" fill="#a855f7"/>
                    <text x="90" y="${y2 + 4}" fill="#a855f7" font-size="10" font-weight="bold">B(0, ${p2})</text>
                `;
            }
        }

        // SIMULATOR 6: Pythagorean Distance Formula Derivation
        function renderSim6(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2">
                        <svg id="pythDistSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="grid grid-cols-2 gap-3 text-xs">
                        <div>
                            <label class="text-slate-400">Point P(x₁, y₁):</label>
                            <div class="flex gap-2 mt-1">
                                <input type="number" id="p6_x1" value="1" min="-5" max="5" onchange="updatePythDist()" class="w-1/2 bg-slate-900 border border-slate-700 text-cyan-300 rounded p-1 text-center font-mono">
                                <input type="number" id="p6_y1" value="2" min="-5" max="5" onchange="updatePythDist()" class="w-1/2 bg-slate-900 border border-slate-700 text-cyan-300 rounded p-1 text-center font-mono">
                            </div>
                        </div>
                        <div>
                            <label class="text-slate-400">Point Q(x₂, y₂):</label>
                            <div class="flex gap-2 mt-1">
                                <input type="number" id="p6_x2" value="4" min="-5" max="5" onchange="updatePythDist()" class="w-1/2 bg-slate-900 border border-slate-700 text-amber-300 rounded p-1 text-center font-mono">
                                <input type="number" id="p6_y2" value="6" min="-5" max="5" onchange="updatePythDist()" class="w-1/2 bg-slate-900 border border-slate-700 text-amber-300 rounded p-1 text-center font-mono">
                            </div>
                        </div>
                    </div>
                    <div id="pythDistStepFormula" class="p-2.5 bg-slate-950 rounded-xl border border-cyan-500/30 text-xs font-mono text-center space-y-1">
                        <!-- Populated by updatePythDist() -->
                    </div>
                </div>
            `;
            updatePythDist();
        }

        function updatePythDist() {
            const x1 = parseFloat(document.getElementById('p6_x1').value) || 0;
            const y1 = parseFloat(document.getElementById('p6_y1').value) || 0;
            const x2 = parseFloat(document.getElementById('p6_x2').value) || 0;
            const y2 = parseFloat(document.getElementById('p6_y2').value) || 0;

            const dx = x2 - x1;
            const dy = y2 - y1;
            const distSq = dx * dx + dy * dy;
            const dist = Math.sqrt(distSq).toFixed(2);

            document.getElementById('pythDistStepFormula').innerHTML = `
                <div class="text-slate-400">d = √[(x₂ - x₁)² + (y₂ - y₁)²] = √[(${dx})² + (${dy})²]</div>
                <div class="text-cyan-300 font-bold text-sm">d = √[${dx*dx} + ${dy*dy}] = √${distSq} ≈ <span class="text-amber-300">${dist} units</span></div>
            `;

            const svg = document.getElementById('pythDistSvg');
            if (!svg) return;

            const cx = 150, cy = 150, sc = 18;
            const px = cx + x1 * sc, py = cy - y1 * sc;
            const qx = cx + x2 * sc, qy = cy - y2 * sc;
            const rx = qx, ry = py; // Right-angle vertex

            svg.innerHTML = `
                <!-- Axes -->
                <line x1="20" y1="150" x2="280" y2="150" stroke="#334155" stroke-width="1.5"/>
                <line x1="150" y1="20" x2="150" y2="280" stroke="#334155" stroke-width="1.5"/>

                <!-- Right Triangle legs -->
                <line x1="${px}" y1="${py}" x2="${rx}" y2="${ry}" stroke="#38bdf8" stroke-width="2.5"/>
                <line x1="${rx}" y1="${ry}" x2="${qx}" y2="${qy}" stroke="#a855f7" stroke-width="2.5"/>

                <!-- Right Angle Symbol -->
                <rect x="${rx > px ? rx - 10 : rx}" y="${qy < py ? ry - 10 : ry}" width="10" height="10" fill="none" stroke="#64748b" stroke-width="1.5"/>

                <!-- Hypotenuse -->
                <line x1="${px}" y1="${py}" x2="${qx}" y2="${qy}" stroke="#f59e0b" stroke-width="3"/>

                <!-- Labels -->
                <circle cx="${px}" cy="${py}" r="5" fill="#38bdf8"/>
                <text x="${px - 15}" y="${py - 8}" fill="#38bdf8" font-size="10" font-weight="bold">P(${x1},${y1})</text>

                <circle cx="${qx}" cy="${qy}" r="5" fill="#f59e0b"/>
                <text x="${qx + 8}" y="${qy - 8}" fill="#f59e0b" font-size="10" font-weight="bold">Q(${x2},${y2})</text>

                <text x="${(px + rx) / 2}" y="${py + 15}" fill="#38bdf8" font-size="10" font-weight="bold">Δx = ${Math.abs(dx)}</text>
                <text x="${rx + 8}" y="${(py + qy) / 2}" fill="#a855f7" font-size="10" font-weight="bold">Δy = ${Math.abs(dy)}</text>
            `;
        }

        // SIMULATOR 7: Equidistant Point & Perpendicular Bisector
        function renderSim7(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2">
                        <svg id="equidistSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Slide Point P(x, 0) on X-Axis:</span>
                            <span id="equiXVal" class="text-amber-400 font-bold">-7</span>
                        </label>
                        <input type="range" min="-12" max="2" value="-7" step="1" id="equiXSlider" oninput="updateEquidist()" class="w-full accent-amber-500">
                    </div>
                    <div id="equidistStatus" class="p-2.5 rounded-xl border text-xs font-mono text-center">
                        <!-- Populated by updateEquidist() -->
                    </div>
                </div>
            `;
            updateEquidist();
        }

        function updateEquidist() {
            const x = parseInt(document.getElementById('equiXSlider').value);
            document.getElementById('equiXVal').textContent = x;

            const ax = 2, ay = -5;
            const bx = -2, by = 9;

            const pa = Math.sqrt((x - ax)**2 + (0 - ay)**2);
            const pb = Math.sqrt((x - bx)**2 + (0 - by)**2);

            const isEqui = (x === -7);
            const status = document.getElementById('equidistStatus');

            if (isEqui) {
                status.className = "p-2.5 rounded-xl border border-emerald-500/50 bg-emerald-950/40 text-emerald-300 text-xs font-mono text-center font-bold";
                status.innerHTML = `★ EQUIDISTANT FOUND! P(-7, 0): PA = PB = √106 ≈ 10.30 units`;
            } else {
                status.className = "p-2.5 rounded-xl border border-slate-800 bg-slate-950 text-slate-300 text-xs font-mono text-center";
                status.innerHTML = `P(${x}, 0) → PA = ${pa.toFixed(2)}, PB = ${pb.toFixed(2)} (Diff: ${Math.abs(pa - pb).toFixed(2)})`;
            }

            const svg = document.getElementById('equidistSvg');
            if (!svg) return;

            const cx = 170, cy = 150, sc = 10;
            const pX = cx + x * sc, pY = cy;
            const aX = cx + ax * sc, aY = cy - ay * sc;
            const bX = cx + bx * sc, bY = cy - by * sc;

            svg.innerHTML = `
                <!-- Axes -->
                <line x1="20" y1="150" x2="280" y2="150" stroke="#64748b" stroke-width="2"/>
                <line x1="170" y1="20" x2="170" y2="280" stroke="#334155" stroke-width="1.5"/>

                <!-- Segment AB -->
                <line x1="${aX}" y1="${aY}" x2="${bX}" y2="${bY}" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3"/>

                <!-- Perpendicular Bisector (x = -7 is on it) -->
                ${isEqui ? `<line x1="${pX}" y1="20" x2="${pX + 40}" y2="280" stroke="#10b981" stroke-width="2"/>` : ''}

                <!-- Lines to P -->
                <line x1="${pX}" y1="${pY}" x2="${aX}" y2="${aY}" stroke="${isEqui ? '#10b981' : '#38bdf8'}" stroke-width="${isEqui ? '2.5' : '1.5'}"/>
                <line x1="${pX}" y1="${pY}" x2="${bX}" y2="${bY}" stroke="${isEqui ? '#10b981' : '#f59e0b'}" stroke-width="${isEqui ? '2.5' : '1.5'}"/>

                <!-- Points -->
                <circle cx="${aX}" cy="${aY}" r="5" fill="#38bdf8"/>
                <text x="${aX + 8}" y="${aY + 4}" fill="#38bdf8" font-size="9" font-weight="bold">A(2,-5)</text>

                <circle cx="${bX}" cy="${bY}" r="5" fill="#f59e0b"/>
                <text x="${bX + 8}" y="${bY + 4}" fill="#f59e0b" font-size="9" font-weight="bold">B(-2,9)</text>

                <circle cx="${pX}" cy="${pY}" r="${isEqui ? '7' : '5'}" fill="${isEqui ? '#10b981' : '#e2e8f0'}"/>
                <text x="${pX - 10}" y="${pY - 10}" fill="${isEqui ? '#10b981' : '#e2e8f0'}" font-size="10" font-weight="bold">P(${x},0)</text>
            `;
        }

        // SIMULATOR 8: Interactive Midpoint Balancer
        function renderSim8(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2">
                        <svg id="midpointSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="grid grid-cols-2 gap-3 text-xs">
                        <div>
                            <label class="text-slate-400">Endpoint A (x₁, y₁):</label>
                            <div class="flex gap-2 mt-1">
                                <input type="number" id="sim8_x1" value="-3" min="-6" max="6" onchange="updateMidpoint()" class="w-1/2 bg-slate-900 border border-slate-700 text-cyan-300 rounded p-1 text-center font-mono">
                                <input type="number" id="sim8_y1" value="7" min="-6" max="6" onchange="updateMidpoint()" class="w-1/2 bg-slate-900 border border-slate-700 text-cyan-300 rounded p-1 text-center font-mono">
                            </div>
                        </div>
                        <div>
                            <label class="text-slate-400">Endpoint B (x₂, y₂):</label>
                            <div class="flex gap-2 mt-1">
                                <input type="number" id="sim8_x2" value="5" min="-6" max="6" onchange="updateMidpoint()" class="w-1/2 bg-slate-900 border border-slate-700 text-amber-300 rounded p-1 text-center font-mono">
                                <input type="number" id="sim8_y2" value="-1" min="-6" max="6" onchange="updateMidpoint()" class="w-1/2 bg-slate-900 border border-slate-700 text-amber-300 rounded p-1 text-center font-mono">
                            </div>
                        </div>
                    </div>
                    <div id="midpointCalcDisplay" class="p-2.5 bg-slate-950 rounded-xl border border-cyan-500/30 text-xs font-mono text-center">
                        <!-- Populated by updateMidpoint() -->
                    </div>
                </div>
            `;
            updateMidpoint();
        }

        function updateMidpoint() {
            const x1 = parseFloat(document.getElementById('sim8_x1').value) || 0;
            const y1 = parseFloat(document.getElementById('sim8_y1').value) || 0;
            const x2 = parseFloat(document.getElementById('sim8_x2').value) || 0;
            const y2 = parseFloat(document.getElementById('sim8_y2').value) || 0;

            const xm = ((x1 + x2) / 2).toFixed(1);
            const ym = ((y1 + y2) / 2).toFixed(1);

            document.getElementById('midpointCalcDisplay').innerHTML = `
                <div class="text-slate-400">M = ((x₁+x₂)/2, (y₁+y₂)/2) = ((${x1}+${x2})/2, (${y1}+${y2})/2)</div>
                <div class="text-emerald-400 font-bold text-sm mt-1">Midpoint M = (${xm}, ${ym})</div>
            `;

            const svg = document.getElementById('midpointSvg');
            if (!svg) return;

            const cx = 150, cy = 150, sc = 18;
            const ax = cx + x1 * sc, ay = cy - y1 * sc;
            const bx = cx + x2 * sc, by = cy - y2 * sc;
            const mx = cx + xm * sc, my = cy - ym * sc;

            svg.innerHTML = `
                <!-- Axes -->
                <line x1="20" y1="150" x2="280" y2="150" stroke="#334155" stroke-width="1.5"/>
                <line x1="150" y1="20" x2="150" y2="280" stroke="#334155" stroke-width="1.5"/>

                <!-- Segment AB -->
                <line x1="${ax}" y1="${ay}" x2="${bx}" y2="${by}" stroke="#64748b" stroke-width="2"/>

                <!-- Equal Half Segments -->
                <line x1="${ax}" y1="${ay}" x2="${mx}" y2="${my}" stroke="#06b6d4" stroke-width="3"/>
                <line x1="${mx}" y1="${my}" x2="${bx}" y2="${by}" stroke="#f59e0b" stroke-width="3"/>

                <!-- Endpoints -->
                <circle cx="${ax}" cy="${ay}" r="5" fill="#06b6d4"/>
                <text x="${ax - 12}" y="${ay - 8}" fill="#06b6d4" font-size="10" font-weight="bold">A(${x1},${y1})</text>

                <circle cx="${bx}" cy="${by}" r="5" fill="#f59e0b"/>
                <text x="${bx + 8}" y="${by + 12}" fill="#f59e0b" font-size="10" font-weight="bold">B(${x2},${y2})</text>

                <!-- Midpoint -->
                <circle cx="${mx}" cy="${my}" r="6" fill="#10b981"/>
                <circle cx="${mx}" cy="${my}" r="12" fill="none" stroke="#10b981" stroke-width="1.5" class="animate-ping" opacity="0.5"/>
                <text x="${mx + 10}" y="${my - 8}" fill="#10b981" font-size="11" font-weight="bold">M(${xm}, ${ym})</text>
            `;
        }

        // SIMULATOR 9: Triangle Side Length Classifier
        function renderSim9(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="flex items-center justify-between text-xs">
                        <span class="text-slate-400">Presets:</span>
                        <div class="flex gap-1.5">
                            <button onclick="setSim9Preset('equi')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-cyan-300">Equilateral</button>
                            <button onclick="setSim9Preset('iso')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-indigo-300">Isosceles</button>
                            <button onclick="setSim9Preset('scal')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-amber-300">Scalene</button>
                        </div>
                    </div>
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2">
                        <svg id="triangleSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div id="triangleStatusBadge" class="p-2.5 rounded-xl border text-xs font-mono text-center font-bold">
                        <!-- Populated by updateTriangleClassifier() -->
                    </div>
                </div>
            `;
            window.sim9Vertices = [ {x: 0, y: 5.2}, {x: -3, y: 0}, {x: 3, y: 0} ]; // Equilateral approx
            updateTriangleClassifier();
        }

        function setSim9Preset(type) {
            if (type === 'equi') window.sim9Vertices = [ {x: 0, y: 5.2}, {x: -3, y: 0}, {x: 3, y: 0} ];
            else if (type === 'iso') window.sim9Vertices = [ {x: 0, y: 6}, {x: -3, y: 0}, {x: 3, y: 0} ];
            else if (type === 'scal') window.sim9Vertices = [ {x: 1, y: 5}, {x: -4, y: 0}, {x: 3, y: -2} ];
            updateTriangleClassifier();
        }

        function updateTriangleClassifier() {
            const [A, B, C] = window.sim9Vertices;
            const ab = Math.sqrt((B.x - A.x)**2 + (B.y - A.y)**2);
            const bc = Math.sqrt((C.x - B.x)**2 + (C.y - B.y)**2);
            const ca = Math.sqrt((A.x - C.x)**2 + (A.y - C.y)**2);

            const badge = document.getElementById('triangleStatusBadge');
            const tol = 0.15;
            if (Math.abs(ab - bc) < tol && Math.abs(bc - ca) < tol) {
                badge.className = "p-2.5 rounded-xl border border-cyan-500/50 bg-cyan-950/40 text-cyan-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `EQUILATERAL TRIANGLE (AB ≈ BC ≈ CA ≈ ${ab.toFixed(1)})`;
            } else if (Math.abs(ab - ca) < tol || Math.abs(ab - bc) < tol || Math.abs(bc - ca) < tol) {
                badge.className = "p-2.5 rounded-xl border border-indigo-500/50 bg-indigo-950/40 text-indigo-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `ISOSCELES TRIANGLE (Two Sides Equal: ${ab.toFixed(1)}, ${bc.toFixed(1)}, ${ca.toFixed(1)})`;
            } else {
                badge.className = "p-2.5 rounded-xl border border-amber-500/50 bg-amber-950/40 text-amber-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `SCALENE TRIANGLE (All 3 sides distinct: ${ab.toFixed(1)}, ${bc.toFixed(1)}, ${ca.toFixed(1)})`;
            }

            const svg = document.getElementById('triangleSvg');
            if (!svg) return;

            const cx = 150, cy = 160, sc = 18;
            const ax = cx + A.x * sc, ay = cy - A.y * sc;
            const bx = cx + B.x * sc, by = cy - B.y * sc;
            const cX = cx + C.x * sc, cY = cy - C.y * sc;

            svg.innerHTML = `
                <!-- Axes -->
                <line x1="20" y1="160" x2="280" y2="160" stroke="#334155" stroke-width="1.5"/>
                <line x1="150" y1="20" x2="150" y2="280" stroke="#334155" stroke-width="1.5"/>

                <!-- Triangle Shading & Border -->
                <polygon points="${ax},${ay} ${bx},${by} ${cX},${cY}" fill="#06b6d4" fill-opacity="0.15" stroke="#06b6d4" stroke-width="2.5"/>

                <!-- Vertices -->
                <circle cx="${ax}" cy="${ay}" r="5" fill="#38bdf8"/>
                <text x="${ax - 5}" y="${ay - 10}" fill="#38bdf8" font-size="10" font-weight="bold">A</text>

                <circle cx="${bx}" cy="${by}" r="5" fill="#a855f7"/>
                <text x="${bx - 15}" y="${by + 15}" fill="#a855f7" font-size="10" font-weight="bold">B</text>

                <circle cx="${cX}" cy="${cY}" r="5" fill="#f59e0b"/>
                <text x="${cX + 8}" y="${cY + 15}" fill="#f59e0b" font-size="10" font-weight="bold">C</text>

                <!-- Side Length Labels -->
                <text x="${(ax + bx)/2 - 20}" y="${(ay + by)/2}" fill="#94a3b8" font-size="9">${ab.toFixed(1)}</text>
                <text x="${(bx + cX)/2}" y="${by + 15}" fill="#94a3b8" font-size="9">${bc.toFixed(1)}</text>
                <text x="${(ax + cX)/2 + 10}" y="${(ay + cY)/2}" fill="#94a3b8" font-size="9">${ca.toFixed(1)}</text>
            `;
        }

        // SIMULATOR 10: Right-Angle Detector
        function renderSim10(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2">
                        <svg id="rightTriSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Adjust Vertex B along y = x - 4:</span>
                            <span id="rightTriBVal" class="text-cyan-400 font-bold">B(8, 4)</span>
                        </label>
                        <input type="range" min="4" max="10" value="8" step="1" id="rtBSlider" oninput="updateRightTri()" class="w-full accent-cyan-500">
                    </div>
                    <div id="rightTriCalcResult" class="p-2.5 rounded-xl border text-xs font-mono text-center font-bold">
                        <!-- Populated by updateRightTri() -->
                    </div>
                </div>
            `;
            updateRightTri();
        }

        function updateRightTri() {
            const bVal = parseInt(document.getElementById('rtBSlider').value);
            const bx = bVal;
            const by = bVal - 4; // B moves on line
            document.getElementById('rightTriBVal').textContent = `B(${bx}, ${by})`;

            const ax = 2, ay = -2;
            const cx = 5, cy = 7;

            const ab2 = (bx - ax)**2 + (by - ay)**2;
            const bc2 = (cx - bx)**2 + (cy - by)**2;
            const ac2 = (cx - ax)**2 + (cy - ay)**2; // 9 + 81 = 90

            const isRight = (ab2 + bc2 === ac2);
            const badge = document.getElementById('rightTriCalcResult');

            if (isRight) {
                badge.className = "p-2.5 rounded-xl border border-emerald-500/50 bg-emerald-950/40 text-emerald-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `★ RIGHT-ANGLED AT B! AB² (${ab2}) + BC² (${bc2}) = AC² (${ac2})`;
            } else {
                badge.className = "p-2.5 rounded-xl border border-slate-800 bg-slate-950 text-slate-400 text-xs font-mono text-center";
                badge.innerHTML = `AB² + BC² = ${ab2 + bc2} vs AC² = ${ac2} (Not 90°)`;
            }

            const svg = document.getElementById('rightTriSvg');
            if (!svg) return;

            const ox = 50, oy = 220, sc = 18;
            const aX = ox + ax * sc, aY = oy - ay * sc;
            const bX = ox + bx * sc, bY = oy - by * sc;
            const cX = ox + cx * sc, cY = oy - cy * sc;

            svg.innerHTML = `
                <!-- Triangle -->
                <polygon points="${aX},${aY} ${bX},${bY} ${cX},${cY}" fill="${isRight ? '#10b981' : '#334155'}" fill-opacity="0.15" stroke="${isRight ? '#10b981' : '#64748b'}" stroke-width="2.5"/>

                ${isRight ? `<rect x="${bX - 12}" y="${bY - 12}" width="12" height="12" fill="none" stroke="#10b981" stroke-width="2"/>` : ''}

                <!-- Vertices -->
                <circle cx="${aX}" cy="${aY}" r="5" fill="#38bdf8"/>
                <text x="${aX - 15}" y="${aY + 15}" fill="#38bdf8" font-size="10" font-weight="bold">A(2,-2)</text>

                <circle cx="${bX}" cy="${bY}" r="6" fill="${isRight ? '#10b981' : '#f59e0b'}"/>
                <text x="${bX + 8}" y="${bY + 5}" fill="${isRight ? '#10b981' : '#f59e0b'}" font-size="10" font-weight="bold">B(${bx},${by})</text>

                <circle cx="${cX}" cy="${cY}" r="5" fill="#a855f7"/>
                <text x="${cX - 15}" y="${cY - 8}" fill="#a855f7" font-size="10" font-weight="bold">C(5,7)</text>
            `;
        }

        // SIMULATOR 11: Collinearity Alignment Tester
        function renderSim11(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2">
                        <svg id="collinearSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="text-xs">
                        <label class="text-slate-400 flex justify-between">
                            <span>Adjust Point B(4, k):</span>
                            <span id="collinearKVal" class="text-cyan-400 font-bold">k = 0</span>
                        </label>
                        <input type="range" min="-4" max="4" value="0" step="1" id="collinearK" oninput="updateCollinear()" class="w-full accent-cyan-500">
                    </div>
                    <div id="collinearBadge" class="p-2.5 rounded-xl border text-xs font-mono text-center font-bold">
                        <!-- Populated by updateCollinear() -->
                    </div>
                </div>
            `;
            updateCollinear();
        }

        function updateCollinear() {
            const k = parseInt(document.getElementById('collinearK').value);
            document.getElementById('collinearKVal').textContent = `k = ${k}`;

            const ax = 2, ay = 3;
            const bx = 4, by = k;
            const cx = 6, cy = -3;

            const slopeAB = (by - ay) / (bx - ax);
            const slopeBC = (cy - by) / (cx - bx);

            const isCollinear = (k === 0);
            const badge = document.getElementById('collinearBadge');

            if (isCollinear) {
                badge.className = "p-2.5 rounded-xl border border-emerald-500/50 bg-emerald-950/40 text-emerald-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `★ COLLINEAR! Slope AB = Slope BC = -1.5 (Lie on y = -1.5x + 6)`;
            } else {
                badge.className = "p-2.5 rounded-xl border border-rose-500/30 bg-rose-950/20 text-rose-300 text-xs font-mono text-center";
                badge.innerHTML = `NON-COLLINEAR: Slope AB (${slopeAB.toFixed(1)}) ≠ Slope BC (${slopeBC.toFixed(1)})`;
            }

            const svg = document.getElementById('collinearSvg');
            if (!svg) return;

            const ox = 50, oy = 150, sc = 20;
            const aX = ox + ax * sc, aY = oy - ay * sc;
            const bX = ox + bx * sc, bY = oy - by * sc;
            const cX = ox + cx * sc, cY = oy - cy * sc;

            svg.innerHTML = `
                <!-- Line through AC -->
                <line x1="${aX - 30}" y1="${aY + 45}" x2="${cX + 30}" y2="${cY - 45}" stroke="#334155" stroke-width="1.5" stroke-dasharray="4"/>

                <!-- Segments AB and BC -->
                <line x1="${aX}" y1="${aY}" x2="${bX}" y2="${bY}" stroke="${isCollinear ? '#10b981' : '#38bdf8'}" stroke-width="${isCollinear ? '3' : '2'}"/>
                <line x1="${bX}" y1="${bY}" x2="${cX}" y2="${cY}" stroke="${isCollinear ? '#10b981' : '#f59e0b'}" stroke-width="${isCollinear ? '3' : '2'}"/>

                <!-- Vertices -->
                <circle cx="${aX}" cy="${aY}" r="5" fill="#38bdf8"/>
                <text x="${aX - 15}" y="${aY - 10}" fill="#38bdf8" font-size="10" font-weight="bold">A(2,3)</text>

                <circle cx="${bX}" cy="${bY}" r="6" fill="${isCollinear ? '#10b981' : '#ec4899'}"/>
                <text x="${bX + 8}" y="${bY - 8}" fill="${isCollinear ? '#10b981' : '#ec4899'}" font-size="10" font-weight="bold">B(4,${k})</text>

                <circle cx="${cX}" cy="${cY}" r="5" fill="#f59e0b"/>
                <text x="${cX + 8}" y="${cY + 12}" fill="#f59e0b" font-size="10" font-weight="bold">C(6,-3)</text>
            `;
        }

        // SIMULATOR 12: Quadrilateral Shape Inspector
        function renderSim12(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="flex items-center justify-between text-xs">
                        <span class="text-slate-400">Shape:</span>
                        <div class="flex gap-1">
                            <button onclick="setSim12Shape('square')" class="px-2 py-0.5 rounded bg-cyan-600 text-white font-bold">Square</button>
                            <button onclick="setSim12Shape('rhombus')" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">Rhombus</button>
                            <button onclick="setSim12Shape('rect')" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">Rectangle</button>
                            <button onclick="setSim12Shape('para')" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">Parallelogram</button>
                        </div>
                    </div>
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2">
                        <svg id="quadShapeSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div id="quadShapeProof" class="p-2 bg-slate-950 rounded-xl border border-cyan-500/30 text-xs font-mono space-y-1">
                        <!-- Populated by updateQuadShape() -->
                    </div>
                </div>
            `;
            window.sim12Shape = 'square';
            updateQuadShape();
        }

        function setSim12Shape(s) {
            window.sim12Shape = s;
            updateQuadShape();
        }

        function updateQuadShape() {
            const s = window.sim12Shape || 'square';
            let A, B, C, D, name, reason;

            if (s === 'square') {
                A = {x: 1, y: 7}; B = {x: 4, y: 2}; C = {x: -1, y: -1}; D = {x: -4, y: 4};
                name = "SQUARE";
                reason = "All 4 sides equal (√34) AND both diagonals equal (√68)";
            } else if (s === 'rhombus') {
                A = {x: 3, y: 0}; B = {x: 4, y: 5}; C = {x: -1, y: 4}; D = {x: -2, y: -1};
                name = "RHOMBUS";
                reason = "All 4 sides equal (√26), but diagonals unequal (2√26 ≠ 2√6)";
            } else if (s === 'rect') {
                A = {x: -2, y: -1}; B = {x: 4, y: -1}; C = {x: 4, y: 3}; D = {x: -2, y: 3};
                name = "RECTANGLE";
                reason = "Opposite sides equal (6 & 4) AND equal diagonals (√52 = √52)";
            } else {
                A = {x: -3, y: 0}; B = {x: 2, y: 0}; C = {x: 4, y: 4}; D = {x: -1, y: 4};
                name = "PARALLELOGRAM";
                reason = "Opposite sides equal, diagonals bisect each other at identical midpoint";
            }

            document.getElementById('quadShapeProof').innerHTML = `
                <div class="text-cyan-400 font-bold flex justify-between">
                    <span>Classification:</span>
                    <span class="text-amber-300 font-black">${name}</span>
                </div>
                <div class="text-[11px] text-slate-300">${reason}</div>
            `;

            const svg = document.getElementById('quadShapeSvg');
            if (!svg) return;

            const cx = 150, cy = 150, sc = 18;
            const ax = cx + A.x * sc, ay = cy - A.y * sc;
            const bx = cx + B.x * sc, by = cy - B.y * sc;
            const cxPt = cx + C.x * sc, cyPt = cy - C.y * sc;
            const dx = cx + D.x * sc, dy = cy - D.y * sc;

            svg.innerHTML = `
                <!-- Quadrilateral -->
                <polygon points="${ax},${ay} ${bx},${by} ${cxPt},${cyPt} ${dx},${dy}" fill="#06b6d4" fill-opacity="0.12" stroke="#06b6d4" stroke-width="2.5"/>

                <!-- Diagonals -->
                <line x1="${ax}" y1="${ay}" x2="${cxPt}" y2="${cyPt}" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3"/>
                <line x1="${bx}" y1="${by}" x2="${dx}" y2="${dy}" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="3"/>

                <!-- Vertices -->
                <circle cx="${ax}" cy="${ay}" r="4" fill="#38bdf8"/>
                <text x="${ax - 10}" y="${ay - 6}" fill="#38bdf8" font-size="9" font-weight="bold">A</text>

                <circle cx="${bx}" cy="${by}" r="4" fill="#38bdf8"/>
                <text x="${bx + 6}" y="${by - 6}" fill="#38bdf8" font-size="9" font-weight="bold">B</text>

                <circle cx="${cxPt}" cy="${cyPt}" r="4" fill="#38bdf8"/>
                <text x="${cxPt + 6}" y="${cyPt + 12}" fill="#38bdf8" font-size="9" font-weight="bold">C</text>

                <circle cx="${dx}" cy="${dy}" r="4" fill="#38bdf8"/>
                <text x="${dx - 12}" y="${dy + 12}" fill="#38bdf8" font-size="9" font-weight="bold">D</text>
            `;
        }

        // SIMULATOR 13: Circle Radar Proximity Scanner
        function renderSim13(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="circleRadarSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="grid grid-cols-2 gap-3 text-xs">
                        <div>
                            <label class="text-slate-400 flex justify-between">
                                <span>Circle Radius (r):</span>
                                <span id="circRVal" class="text-cyan-400 font-bold">5</span>
                            </label>
                            <input type="range" min="3" max="8" value="5" step="1" id="circR" oninput="updateCircleRadar()" class="w-full accent-cyan-500">
                        </div>
                        <div>
                            <label class="text-slate-400 flex justify-between">
                                <span>Point Distance (d):</span>
                                <span id="circDistVal" class="text-amber-400 font-bold">4.47</span>
                            </label>
                            <input type="range" min="1" max="9" value="4.5" step="0.5" id="circDistSlider" oninput="updateCircleRadar()" class="w-full accent-amber-500">
                        </div>
                    </div>
                    <div id="circRadarBadge" class="p-2.5 rounded-xl border text-xs font-mono text-center font-bold">
                        <!-- Populated by updateCircleRadar() -->
                    </div>
                </div>
            `;
            updateCircleRadar();
        }

        function updateCircleRadar() {
            const r = parseFloat(document.getElementById('circR').value);
            const d = parseFloat(document.getElementById('circDistSlider').value);

            document.getElementById('circRVal').textContent = r;
            document.getElementById('circDistVal').textContent = d.toFixed(1);

            const badge = document.getElementById('circRadarBadge');
            const diff = Math.abs(d - r);

            if (diff < 0.25) {
                badge.className = "p-2.5 rounded-xl border border-emerald-500/50 bg-emerald-950/40 text-emerald-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `★ ON THE BOUNDARY (d = r = ${r}): (x-h)² + (y-k)² = r²`;
            } else if (d < r) {
                badge.className = "p-2.5 rounded-xl border border-cyan-500/50 bg-cyan-950/40 text-cyan-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `INSIDE CIRCLE (d = ${d.toFixed(1)} < r = ${r}): Point is Interior`;
            } else {
                badge.className = "p-2.5 rounded-xl border border-rose-500/50 bg-rose-950/30 text-rose-300 text-xs font-mono text-center font-bold";
                badge.innerHTML = `OUTSIDE CIRCLE (d = ${d.toFixed(1)} > r = ${r}): Point is Exterior`;
            }

            const svg = document.getElementById('circleRadarSvg');
            if (!svg) return;

            const cx = 150, cy = 150, sc = 16;
            const rPx = r * sc;
            const px = cx + d * sc * 0.707;
            const py = cy - d * sc * 0.707;

            svg.innerHTML = `
                <!-- Radar background rings -->
                <circle cx="${cx}" cy="${cy}" r="${sc * 3}" fill="none" stroke="#1e293b" stroke-width="1"/>
                <circle cx="${cx}" cy="${cy}" r="${sc * 6}" fill="none" stroke="#1e293b" stroke-width="1"/>
                <circle cx="${cx}" cy="${cy}" r="${sc * 8}" fill="none" stroke="#1e293b" stroke-width="1"/>

                <!-- Radar beam sweep -->
                <path d="M150 150 L270 150 A120 120 0 0 0 235 65 Z" fill="url(#radarGradient)" opacity="0.25" class="radar-sweep"/>
                <defs>
                    <linearGradient id="radarGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stop-color="#06b6d4" stop-opacity="0.8"/>
                        <stop offset="100%" stop-color="#06b6d4" stop-opacity="0"/>
                    </linearGradient>
                </defs>

                <!-- Circle Boundary -->
                <circle cx="${cx}" cy="${cy}" r="${rPx}" fill="#06b6d4" fill-opacity="0.1" stroke="#06b6d4" stroke-width="2.5"/>

                <!-- Center -->
                <circle cx="${cx}" cy="${cy}" r="4" fill="#f8fafc"/>
                <text x="${cx - 10}" y="${cy + 15}" fill="#94a3b8" font-size="9">C(0,0)</text>

                <!-- Test Point -->
                <line x1="${cx}" y1="${cy}" x2="${px}" y2="${py}" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3"/>
                <circle cx="${px}" cy="${py}" r="6" fill="#f59e0b"/>
                <text x="${px + 8}" y="${py - 4}" fill="#f59e0b" font-size="10" font-weight="bold">P</text>
            `;
        }

        // SIMULATOR 14: GPS Cell Tower Triangulation
        function renderSim14(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 overflow-hidden">
                        <svg id="gpsSvg" viewBox="0 0 300 300" class="w-full h-full"></svg>
                    </div>
                    <div class="flex items-center justify-between text-xs">
                        <span class="text-slate-400">Position Hiker (x, y):</span>
                        <div class="flex gap-2">
                            <button onclick="setHikerPos(4, 5)" class="px-2 py-0.5 rounded bg-cyan-600 text-white font-bold">Camp (4, 5)</button>
                            <button onclick="setHikerPos(2, 2)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">Ridge (2, 2)</button>
                            <button onclick="setHikerPos(6, 3)" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">Lake (6, 3)</button>
                        </div>
                    </div>
                    <div id="gpsReadout" class="p-2.5 bg-slate-950 rounded-xl border border-cyan-500/30 text-xs font-mono space-y-1">
                        <!-- Populated by updateGPS() -->
                    </div>
                </div>
            `;
            window.hikerPos = { x: 4, y: 5 };
            updateGPS();
        }

        function setHikerPos(x, y) {
            window.hikerPos = { x, y };
            updateGPS();
        }

        function updateGPS() {
            const { x, y } = window.hikerPos;
            const t1 = { name: "Tower A", x: 1, y: 1 };
            const t2 = { name: "Tower B", x: 7, y: 2 };
            const t3 = { name: "Tower C", x: 3, y: 8 };

            const r1 = Math.sqrt((x - t1.x)**2 + (y - t1.y)**2).toFixed(1);
            const r2 = Math.sqrt((x - t2.x)**2 + (y - t2.y)**2).toFixed(1);
            const r3 = Math.sqrt((x - t3.x)**2 + (y - t3.y)**2).toFixed(1);

            const manh = Math.abs(x) + Math.abs(y);
            const eucl = Math.sqrt(x*x + y*y).toFixed(2);

            document.getElementById('gpsReadout').innerHTML = `
                <div class="flex justify-between text-cyan-300 font-bold">
                    <span>Hiker Location: (${x}, ${y})</span>
                    <span class="text-emerald-400">Trilateration Locked</span>
                </div>
                <div class="text-[11px] text-slate-300">Tower Signals: rA = ${r1} km, rB = ${r2} km, rC = ${r3} km</div>
                <div class="text-[11px] text-amber-300">Manhattan: ${manh} blocks vs Euclidean: ${eucl} km</div>
            `;

            const svg = document.getElementById('gpsSvg');
            if (!svg) return;

            const sc = 26, ox = 30, oy = 260;
            const hx = ox + x * sc, hy = oy - y * sc;

            const towers = [t1, t2, t3].map((t, idx) => {
                const tx = ox + t.x * sc, ty = oy - t.y * sc;
                const r = [r1, r2, r3][idx] * sc;
                return `
                    <circle cx="${tx}" cy="${ty}" r="${r}" fill="none" stroke="#06b6d4" stroke-width="1.5" stroke-dasharray="3" opacity="0.6"/>
                    <circle cx="${tx}" cy="${ty}" r="6" fill="#3b82f6"/>
                    <text x="${tx - 12}" y="${ty + 15}" fill="#94a3b8" font-size="9" font-weight="bold">${t.name}</text>
                `;
            }).join('');

            svg.innerHTML = `
                ${towers}
                <!-- Hiker -->
                <circle cx="${hx}" cy="${hy}" r="7" fill="#ef4444"/>
                <circle cx="${hx}" cy="${hy}" r="15" fill="none" stroke="#ef4444" stroke-width="2" class="animate-ping" opacity="0.6"/>
                <text x="${hx + 10}" y="${hy - 6}" fill="#f8fafc" font-size="11" font-weight="bold">Hiker (${x},${y})</text>
            `;
        }

        // SIMULATOR 15: Computational Geometry Algorithm Runner
        function renderSim15(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="flex items-center justify-between text-xs">
                        <span class="text-slate-400">Algorithm:</span>
                        <select id="algoSelect" onchange="runAlgo()" class="bg-slate-900 border border-slate-700 text-cyan-300 rounded p-1 font-mono">
                            <option value="dist">euclideanDistance(p1, p2)</option>
                            <option value="mid">midpoint(p1, p2)</option>
                            <option value="collinear">isCollinearCrossProduct(p1, p2, p3)</option>
                            <option value="pyth">isRightTriangle(p1, p2, p3)</option>
                        </select>
                    </div>
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 font-mono text-[11px] text-cyan-300 space-y-1 h-[180px] overflow-y-auto" id="algoCodeBox">
                        <!-- Populated by runAlgo() -->
                    </div>
                    <div id="algoExecResult" class="p-2.5 rounded-xl border border-cyan-500/30 bg-slate-950 text-xs font-mono">
                        <!-- Populated by runAlgo() -->
                    </div>
                </div>
            `;
            runAlgo();
        }

        function runAlgo() {
            const algo = document.getElementById('algoSelect').value;
            const codeBox = document.getElementById('algoCodeBox');
            const res = document.getElementById('algoExecResult');

            if (algo === 'dist') {
                codeBox.innerHTML = `
                    <div class="text-slate-500">// O(1) Time, O(1) Space</div>
                    <div class="text-amber-300">function euclideanDistance(p1, p2) {</div>
                    <div class="pl-4">const dx = p2.x - p1.x;</div>
                    <div class="pl-4">const dy = p2.y - p1.y;</div>
                    <div class="pl-4 text-emerald-400">return Math.sqrt(dx * dx + dy * dy);</div>
                    <div class="text-amber-300">}</div>
                `;
                res.innerHTML = `
                    <div class="text-cyan-400 font-bold">Input: P1(1, 2), P2(4, 6)</div>
                    <div class="text-emerald-400">Output: 5.0 units [Executed in 0.04 ms]</div>
                `;
            } else if (algo === 'mid') {
                codeBox.innerHTML = `
                    <div class="text-slate-500">// O(1) Time, O(1) Space</div>
                    <div class="text-amber-300">function midpoint(p1, p2) {</div>
                    <div class="pl-4 text-emerald-400">return { x: (p1.x + p2.x) / 2, y: (p1.y + p2.y) / 2 };</div>
                    <div class="text-amber-300">}</div>
                `;
                res.innerHTML = `
                    <div class="text-cyan-400 font-bold">Input: A(-3, 8), B(7, -2)</div>
                    <div class="text-emerald-400">Output: Midpoint M(2.0, 3.0)</div>
                `;
            } else if (algo === 'collinear') {
                codeBox.innerHTML = `
                    <div class="text-slate-500">// Cross-product avoids division by zero</div>
                    <div class="text-amber-300">function isCollinear(p1, p2, p3, eps = 1e-7) {</div>
                    <div class="pl-4">const cross = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x);</div>
                    <div class="pl-4 text-emerald-400">return Math.abs(cross) < eps;</div>
                    <div class="text-amber-300">}</div>
                `;
                res.innerHTML = `
                    <div class="text-cyan-400 font-bold">Input: A(2, 3), B(4, 0), C(6, -3)</div>
                    <div class="text-emerald-400">Cross-Product = 0.0 → Result: TRUE (Collinear)</div>
                `;
            } else {
                codeBox.innerHTML = `
                    <div class="text-slate-500">// Converse of Pythagoras check</div>
                    <div class="text-amber-300">function isRightTriangle(p1, p2, p3) {</div>
                    <div class="pl-4">const d2 = [distSq(p1, p2), distSq(p2, p3), distSq(p3, p1)].sort((a,b) => a-b);</div>
                    <div class="pl-4 text-emerald-400">return Math.abs(d2[0] + d2[1] - d2[2]) < 1e-6;</div>
                    <div class="text-amber-300">}</div>
                `;
                res.innerHTML = `
                    <div class="text-cyan-400 font-bold">Input: A(0,0), B(3,0), C(0,4)</div>
                    <div class="text-emerald-400">Sorted d²: [9, 16, 25] → 9 + 16 == 25 → Result: TRUE</div>
                `;
            }
        }

        // SIMULATOR 16: Master Coordinate Sandbox Playground
        function renderSim16(container) {
            container.innerHTML = `
                <div class="w-full space-y-3">
                    <div class="flex items-center justify-between text-xs">
                        <span class="text-slate-400">Canvas Sandbox: Click to plot points</span>
                        <button onclick="clearSandbox()" class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 hover:text-white">Clear</button>
                    </div>
                    <div class="relative w-full max-w-[340px] aspect-square mx-auto bg-slate-950 rounded-xl border border-slate-800 p-2 cursor-crosshair">
                        <svg id="sandboxSvg" viewBox="0 0 300 300" class="w-full h-full" onclick="handleSandboxClick(event)"></svg>
                    </div>
                    <div id="sandboxReadout" class="p-2.5 bg-slate-950 rounded-xl border border-cyan-500/30 text-xs font-mono text-center">
                        Plotted: 2 Points. Distance = 7.21 units, Midpoint = (1.5, 2.0)
                    </div>
                </div>
            `;
            window.sandboxPoints = [ {x: -2, y: 0}, {x: 5, y: 4} ];
            updateSandbox();
        }

        function handleSandboxClick(e) {
            const svg = document.getElementById('sandboxSvg');
            if (!svg) return;
            const rect = svg.getBoundingClientRect();
            const clickX = e.clientX - rect.left;
            const clickY = e.clientY - rect.top;

            const cx = 150, cy = 150, sc = 15;
            const gridX = Math.round((clickX - cx) / sc);
            const gridY = Math.round((cy - clickY) / sc);

            if (window.sandboxPoints.length >= 4) window.sandboxPoints = [];
            window.sandboxPoints.push({ x: gridX, y: gridY });
            updateSandbox();
            playTone(500, 'triangle', 0.1);
        }

        function clearSandbox() {
            window.sandboxPoints = [];
            updateSandbox();
        }

        function updateSandbox() {
            const pts = window.sandboxPoints || [];
            const readout = document.getElementById('sandboxReadout');

            if (pts.length < 2) {
                readout.innerHTML = `<span class="text-slate-400">Click on the grid to add points (up to 4 points)</span>`;
            } else if (pts.length === 2) {
                const [p1, p2] = pts;
                const d = Math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2).toFixed(2);
                const mx = ((p1.x + p2.x)/2).toFixed(1);
                const my = ((p1.y + p2.y)/2).toFixed(1);
                readout.innerHTML = `
                    <div class="text-cyan-300 font-bold">Points: A(${p1.x},${p1.y}) & B(${p2.x},${p2.y})</div>
                    <div class="text-emerald-400">Distance = ${d} units | Midpoint M = (${mx}, ${my})</div>
                `;
            } else {
                readout.innerHTML = `
                    <div class="text-cyan-300 font-bold">${pts.length}-Point Polygon Active</div>
                    <div class="text-amber-300">Click anywhere to clear and restart</div>
                `;
            }

            const svg = document.getElementById('sandboxSvg');
            if (!svg) return;

            const cx = 150, cy = 150, sc = 15;
            let lines = '';
            for (let i = 0; i < pts.length; i++) {
                const next = (i + 1) % pts.length;
                if (pts.length === 2 && i === 1) break;
                const x1 = cx + pts[i].x * sc, y1 = cy - pts[i].y * sc;
                const x2 = cx + pts[next].x * sc, y2 = cy - pts[next].y * sc;
                lines += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#06b6d4" stroke-width="2"/>`;
            }

            let dots = pts.map((p, idx) => {
                const px = cx + p.x * sc, py = cy - p.y * sc;
                return `
                    <circle cx="${px}" cy="${py}" r="5" fill="#f59e0b"/>
                    <text x="${px + 6}" y="${py - 6}" fill="#f8fafc" font-size="9" font-weight="bold">${String.fromCharCode(65 + idx)}(${p.x},${p.y})</text>
                `;
            }).join('');

            svg.innerHTML = `
                <!-- Axes -->
                <line x1="20" y1="150" x2="280" y2="150" stroke="#334155" stroke-width="1.5"/>
                <line x1="150" y1="20" x2="150" y2="280" stroke="#334155" stroke-width="1.5"/>
                ${lines}
                ${dots}
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

